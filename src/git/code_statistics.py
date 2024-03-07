#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# SPDX-FileCopyrightText: 2023 UnionTech Software Technology Co., Ltd.
# SPDX-License-Identifier: GPL-2.0-only
import os
import json
import re
from difflib import unified_diff

from setting import conf
from src.rtk._base import transform_app_name
from src.git.commit import Commit


class CodeStatistics(Commit):
    __author__ = "mikigo<huangmingqiang@uniontech.com>"

    def __init__(
            self,
            app_name: str,
            branch: str,
            commit_old: str = None,
            commit_new: str = None,
            startdate: str = None,
            enddate: str = None,
            **kwargs,
    ):
        if (commit_old or commit_new) and startdate:
            raise ValueError("commit id 和 startdate是两种不同的方式，不能同时使用")
        if (commit_old and commit_new is None) or (commit_old is None and commit_new):
            raise ValueError("commit_old 和 commit_new 两个参数必须同时传入")

        self.app_name = transform_app_name(app_name)
        self.branch = branch
        self.repo_path = f"{conf.APPS_PATH}/{self.app_name}"
        self.commit_old = commit_old
        self.commit_new = commit_new
        self.startdate = startdate

        if startdate:
            super().__init__(app_name, branch=branch, startdate=startdate, enddate=enddate)
        self.ignore_txt = ["from", "import", ""]

        for i in range(100):
            self.ignore_txt.append(" " * i + "#")

    def get_git_files(self, commit_old, commit_new):
        diffs = (
            os.popen(f"cd {self.repo_path};git diff {commit_old} {commit_new}")
            .read()
            .split("\n")
        )
        git_files = []
        file_info = {}
        for diff in diffs:
            if diff.startswith("diff --git "):
                if file_info:
                    git_files.append(file_info)
                    file_info = {}
                file_info["file"] = diff
            else:
                if file_info.get("content"):
                    file_info["content"].append(diff)
                else:
                    file_info["content"] = [diff]
        git_files.append(file_info)
        return git_files

    def compare_files(self, commit_old, commit_new, author):
        _fix_debug = []
        _new_debug = []
        new_test_case_num = 0
        del_test_case_num = 0
        fix_test_case_num = 0
        new_method_num = 0
        del_method_num = 0
        fix_method_num = 0
        git_files = self.get_git_files(commit_old, commit_new)
        for git_file in git_files:
            filepath = git_file.get("file").split(" ")[-1].strip("b/")
            filename = filepath.split("/")[-1]

            if not filename.endswith(".py"):
                print("===== ignored:", filepath, "\n")
                continue

            print("filepath:", filepath, "\n")
            new_code = (
                    os.popen(f"cd {self.repo_path}/;git show {commit_new}:{filepath}")
                    .read()
                    .splitlines()
                    or ""
            )
            old_code = (
                    os.popen(f"cd {self.repo_path}/;git show {commit_old}:{filepath}")
                    .read()
                    .splitlines()
                    or ""
            )
            dif_gen = unified_diff(old_code, new_code)
            print("=" * 100)
            # case
            if filename.startswith("test_"):
                contents = git_file.get("content")
                for content in contents:
                    if content.startswith("--- /dev/null"):
                        new_test_case_num += 1
                        break
                    elif content.startswith("+++ /dev/null"):
                        del_test_case_num += 1
                        break
                else:
                    fix_test_case_num += 1
            # method
            else:
                dif_txt = "\n".join(dif_gen)
                print(dif_txt)
                methods = []
                method_info = {}
                for line in dif_txt.splitlines():
                    if line.startswith(("---", "+++", "@@", "@")):
                        continue
                    if "def " in line:
                        if method_info:
                            methods.append(method_info)
                            method_info = {}
                        method_info["name"] = line
                    else:
                        if method_info.get("method_content"):
                            method_info["method_content"].append(line)
                        else:
                            method_info["method_content"] = [line]
                methods.append(method_info)
                for method in methods:
                    method_name = method.get("name")
                    method_content = method.get("method_content")

                    if method_name is None:
                        if method_content:
                            for content in method_content:
                                if content.startswith(("-", "+")):
                                    if content[1:].startswith(tuple(self.ignore_txt)):
                                        continue
                                    _fix_debug.append(method)
                                    fix_method_num += 1
                                    break

                    # 正常出现的方法
                    # 方法名称是+开头，直接视为新增方法
                    elif method_name.startswith("+"):
                        _new_debug.append(method)
                        new_method_num += 1
                    # 方法名称是-开头，直接视为删除方法
                    elif method_name.startswith("-"):
                        del_method_num += 1
                    else:
                        if method_content:
                            for content in method_content:
                                if content.startswith(("-", "+")):
                                    _fix_debug.append(method)
                                    fix_method_num += 1
                                    break

        res = {
            "commit_new": commit_new,
            "commit_old": commit_old,
            "author": author,
            "新增用例": new_test_case_num,
            "删除用例": del_test_case_num,
            "修改用例": fix_test_case_num,
            "新增方法": new_method_num,
            "删除方法": del_method_num,
            "修改方法": fix_method_num,
        }
        return res

    def write_result(self, res):
        if not os.path.exists(conf.REPORT_PATH):
            os.makedirs(conf.REPORT_PATH)
        result_file = os.path.join(conf.REPORT_PATH, f"{self.app_name}_git_compare_result.json")
        with open(result_file, "w", encoding="utf-8") as f:
            f.write(json.dumps(res, ensure_ascii=False, indent=2))

        with open(result_file, "r", encoding="utf-8") as f:
            print(f.read())

    def codex(self):
        if self.startdate:
            commit_id_pairs = self.commit_id()
            results = []
            for _commit_old, _commit_new, _author in commit_id_pairs:
                res = self.compare_files(_commit_old, _commit_new, _author)
                results.append(res)

        elif self.commit_new and self.commit_old:
            a = os.popen(f"cd {self.repo_path} && git show {self.commit_new}").read()
            re_author = re.findall(r"Author: (.*?)\n", a)
            if re_author:
                # self.write_result(self.commit_old, self.commit_new, re_author[0])
                re_author = re_author[0]
            else:
                raise ValueError()
            results = self.compare_files(self.commit_old, self.commit_new, re_author)
        self.write_result(results)


if __name__ == "__main__":
    app_name = "apps/autotest_deepin_downloader"
    # commit_new = "059632e9e2dfc7fe580abefe3c51f15d8672d213"
    # commit_old = "c30572e113a2e90cf340426a8c16c44b7605bfd7"
    CodeStatistics(
        app_name=app_name,
        branch="master",
        # commit_old=commit_old,
        # commit_new=commit_new,
        startdate="2024-02-25",
        # enddate="2024-02-27",
    ).codex()

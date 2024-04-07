#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# SPDX-FileCopyrightText: 2023 UnionTech Software Technology Co., Ltd.
# SPDX-License-Identifier: GPL-2.0-only
from funnylog import logger

from src.remotectl._remote_dogtail_ctl import remote_dogtail_ctl as remote_dogtail_ctl
from src.remotectl._remote_other_ctl import remote_other_ctl as remote_other_ctl
from src.dogtail_utils import DogtailUtils
from src import Src
from src.shortcut import ShortCut
from src.cmdctl import CmdCtl
from setting import conf


class Remote(ShortCut, CmdCtl):

    def __init__(self, ip, user, password, transfer_appname=None):
        self.user = user
        self.ip = ip
        self.password = password
        self.transfer_appname = transfer_appname
        self.tmp_obj = None

    def __getattribute__(self, item):
        if not item.startswith("__") and not item.endswith("__"):
            for cls_obj in [ShortCut, CmdCtl]:
                if hasattr(cls_obj, item):
                    self.tmp_obj = {"cls_obj": cls_obj, "item_obj": getattr(cls_obj, item)}
                    delattr(cls_obj, item)
        return super().__getattribute__(item)

    def __getattr__(self, item):
        def func(*args, **kwargs):
            ar = ""
            if args:
                for arg in args:
                    ar += f"'{arg}', "
            if kwargs:
                for k, v in kwargs.items():
                    ar += f"{k}='{v}', "
            logger.debug(
                f"Remote(user='{self.user}', ip='{self.ip}', password='{self.password}').rctl.{item}({ar.rstrip(', ')})"
            )

            getattr(self.rctl, item)(*args, **kwargs)

            self.remote_method_has_arguments = True
            if self.tmp_obj:
                setattr(self.tmp_obj["cls_obj"], item, self.tmp_obj["item_obj"])

        return func

    @property
    def rdog(self) -> DogtailUtils:
        return remote_dogtail_ctl(user=self.user, ip=self.ip, password=self.password)

    def click_element_by_attr(self, element, button=1):
        self.rdog.element_click(element, button=button)

    @property
    def rctl(self) -> Src:
        return remote_other_ctl(user=self.user, ip=self.ip, password=self.password)

    @property
    def rctl_plus(self) -> Src:
        return remote_other_ctl(
            user=self.user, ip=self.ip, password=self.password, transfer_appname=self.transfer_appname
        )

    def find_image(self, image_path):
        _image_path = image_path.replace(conf.HOME, "~", Maximum=1)
        return self.rctl_plus.find_image(_image_path)


if __name__ == '__main__':
    r = Remote(ip="10.8.11.12", user="autotest", password="123")
    r.ctrl_alt_t()

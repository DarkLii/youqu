# 版本更新记录

## 2.10.0（2024/11/08）

**Fix 🐛**

- 不再生成 xml 报告；
- 修复远程执行模式下，代码发送失败退出码为0的问题；

## 2.9.0（2024/11/01）

**Fix 🐛**

- 修复远程交互式控制文件描述符占用超限的问题；

## 2.6.9（2024/08/05）

**Fix 🐛**

- `Cmd.sudo_run_cmd` 增加 `workdir` 功能。
- 将 `run_cmd` 固定 `shell` 默认指定为 `/bin/bash`。
- 临时处理 `input_message` 方法，在 `wayland` 输入中文末尾多出空格的问题。
- 修改部署客户端设备 `youqu` 环境时，阻塞在密码输入。
- 扩展 `OCR` 断言支持区域断言，提升精准度，优化 `OCR` 识别范围筛选方法。

## 2.6.8（2024/07/15）

**New 🌟**

- `git commit` 功能增加显示明细数据。
- 新增在所有属性中查找同名节点的功能。

## 2.6.7（2024/07/15）

**Fix 🐛**

- 修复 `Wayland` 下窗管返回的 `window_info` 内获取应用名称的逻辑错误的问题。

## 2.6.6（2024/07/05）

**New 🌟**

- `git commit` 统计功能新增 `commit msg` 信息获取。

**Fix 🐛**

- 修复测试单驱动收集用例数量为 0 的问题；
- 修复 `Wayland` 下窗管返回的应用名称错误的问题；

## 2.6.5（2024/06/11）

**Fix 🐛**

- 修复用例失败截图添加到测试报告时报错的问题；

## 2.6.4（2024/06/07）

**Fix 🐛**

- 由于窗管团队修改获取窗口信息的返回值，导致 Wayland 下相对位移定位方案报错，YouQu 进行适配。

## 2.6.3（2024/06/07）

**New 🌟**

- 新增 `ocr` 范围识别；

**Fix 🐛**

- 测试单驱动，手动回填模式报错；
- 修改 `Wayland` 下中文写入剪贴版问题，改为使用 `wl-copy` 命令实现；
- 修复远程交互控制测试机注销后 RPC 服务不响应的问题；

## 2.6.2（2024/05/29）

**New 🌟**

- `JSON` 报告功能优化

  **`run` 模式下：**

  - `/report/json/detail_report.json` 包含每条 `py` 脚本的结果；
  - `/report/json/summarize.json` 根据 `detail_report.json` 计算的汇总数据；

  **`remote` 模式下：**

  - 收集远程测试机上所有的 `/report/json/${timestr}_remote/detail_report_${IP}.json` ；
  - 收集远程测试机上所有的 `/report/json/${timestr}_remote/summarize_${IP}.json`；
  - 负载均衡驱动模式下自动汇总 `summarize` 数据：`/report/json/${timestr}_remote/summarize.json`；

- `remote` 模式新增参数：`git_url`、`git_user`、`git_password`、`branch`、`depth` 用以控制拉取 `git` 仓库代码；

- 由于 [letmego](https://linuxdeepin.github.io/letmego/) 方案使用场景较少，默认环境中移除此模块，子项目需要时通过新增依赖机制进行安装；

- 支持将测试结果回传给测试平台；

- 文档更新：实践/HTTP接口自动化测试/创建一条完整的用例。[@003307](https://github.com/003307)

- `YouQu` 插件 `pdocr-rpc` 更新：支持Windows和MacOS，图片入参支持多种图片格式，并兼容不带文件后缀名入参方式。[@CCrazyPeter](https://github.com/CCrazyPeter)

**Fix 🐛**

- 修复测试单驱动执行报错的问题；
- `YouQu` 插件 `pdocr-rpc` 修复服务器系统获取显示协议错误的问题；

## 2.6.1（2024/05/21）

这个版本中，我们成功在欧拉社区开源 **[src-openeuler](https://gitee.com/src-openeuler/youqu)** ，后续将以 `patch` 的方式持续在欧拉社区进行代码更新，希望欧拉系统上使用到 `YouQu` 的同学们能给我们反馈使用情况。

此外，重点对统计 `commit` 功能进行了优化和 `Bug` 修复，此功能目前还处于内部灰度阶段，未来有希望成为 `YouQu` 的另一个亮点，能自动分析统计每次提交中包含的用例和方法的增删改的数据，数据汇报者统计者的利器。

**New 🌟**

- 新增 `skipif_not_xxx` 条件跳过逻辑；[PR #68](https://github.com/linuxdeepin/youqu/pull/68) by [@DarkLii](https://github.com/DarkLii)
- 对生成的 `JSON` 报告的路径、文件名称、报告内容进行了重新规划，将在下一个版本开发并发布；[@mikigo](https://github.com/mikigo)
- 文档更新：指南/框架必备/执行管理器，新增用例驱动方式章节，用以集中说明 `YouQu` 支持的驱动方式。[@mikigo](https://github.com/mikigo)
- `YouQu` 插件 `image-center` 更新：支持 `Windows` 和 `MacOS`，图片入参支持多种图片格式，并兼容不带文件后缀名入参方式。[@CCrazyPeter](https://github.com/CCrazyPeter)

**Fix 🐛**

- 修复统计 `commit` 数据中修复方法数量错误的问题；[@mikigo](https://github.com/mikigo)
- 修改 `JSON` 报告计算逻辑：[@mikigo](https://github.com/mikigo)

  - 用例总数 = 通过数 + 失败数 （剔除跳过数）
  
  - 失败数：剔除跳过数
  
  - 跳过数：跳过用例数
  
  - 通过率 = 通过数 / 用例总数
- 修复 `env.sh` 提示找不到 `youqu-shell-rm` 的问题，将删除虚拟环境的命令修改为：`youqu-rm`；[@mikigo](https://github.com/mikigo)
- 修复统计 `commit` 功能 `enddate` 报错的问题；[@mikigo](https://github.com/mikigo)

## 2.6.0（2024/05/14）

近期，`YouQu` 自动化测试框架迎来了一系列令人振奋的更新，这些更新不仅提升了框架的性能和稳定性，也拓展了其功能和适用范围。通过引入 `OCR` 服务集群化部署和模型 `v4`，我们显著提高了文本识别的准确性和效率。新增的链式调用函数接口使操作更加直观和便捷。

在功能创新方面，我们推出了 `Web UI` 自动化测试功能和远程交互式控制功能，为自动化测试提供了更加丰富和灵活的手段。同时，我们还增强了报告的功能，新增了生成的` json` 结果以 `py` 维度统计，为测试数据的分析和解读提供了更多维度。

平台兼容适配性方面，我们对 `openEuler` 系统完成了适配，为后续开源到 `openEuler` 社区做好准备。

在问题修复方面，我们针对用户反馈的多个问题进行了积极的调查和解决，包括报告生成时的错误处理、远程调用的稳定性和兼容性等问题，这些修复进一步提升了用户体验，确保了框架的稳定性和可靠性。

总的来说，这一系列的更新标志着 `YouQu` 自动化测试框架在便捷性和稳定性方面迈出了重要的一步，我们坚信这些更新将极大地提升开发者和测试人员的效率，推动自动化测试技术向前发展。

**New 🌟**

- `OCR` 服务性能优化，使用 OCR 服务集群化部署，框架自动做负载均衡，同时启用 `OCR` 识别模型 `v4`，进一步提高识别稳定性和准确性。[@mikigo](https://github.com/mikigo)

- YouQu OCR 新增支持链式调用函数接口，使用更方便更符合语义，原函数接口使用方法不变以保持兼容性。[@mikigo](https://github.com/mikigo)

  ```python
  from src import OCR
  
  # 新的函数接口ocrx，支持链式调用
  OCR.ocrx("确定").click()
  OCR.ocrx("确定").center()
  # 原函数接口ocr，返回坐标
  OCR.ocr("确定")
  ```

- 完成 `openEuler` 系统适配。[@mikigo](https://github.com/mikigo)

**Fix 🐛**

- 修复 `json` 报告失败数量没有剔除跳过数量的问题。[@mikigo](https://github.com/mikigo)
- 修复内网文档不能加载 `favicon` 的问题。[@mikigo](https://github.com/mikigo)
- 修复远程调用时，调用函数同时传入可变参数和默认参数，远端无法解析默认参数的问题。[@mikigo](https://github.com/mikigo)

## 2.5.5（2024/05/10）

**New 🌟**

- 文档新增 `指南/框架必备/Ruff代码检查` 章节；[@mikigo](https://github.com/mikigo)

**Fix 🐛**

- 修复生成测试报告阶段，机器密码不对时报错；[@mikigo](https://github.com/mikigo)
- 文档界面UI调整；[@mikigo](https://github.com/mikigo)
- 修改 HTML 报告中用例总数为包含跳过用例数量；[@mikigo](https://github.com/mikigo)

## 2.5.4（2024/05/08）

**New 🌟**

- 将项目根目录下 `_env_base.sh` 移动到 `setting` 目录下，简化项目根目录下文件目录结构；[@mikigo](https://github.com/mikigo)
- 将项目根目录下 `pylint.sh` 移动到 `src/utils` 目录下，YouQu 目前已经启用了更先进的 Ruff，Pylint 后续默认不再使用，但考虑到有些同学仍然有使用 Pylint 的需求，因此暂留。[@mikigo](https://github.com/mikigo)
- 添加 `CODE_OF_CONDUCT.md` 。[@mikigo](https://github.com/mikigo)
- 在线文档增加团队页。[@mikigo](https://github.com/mikigo)
- 报告增加 `PMS` 用例维度统计数据；[@mikigo](https://github.com/mikigo)
- 将生成的 `json` 用例结果以 `py` 维度统计；[@mikigo](https://github.com/mikigo)
- 整合 `env.sh` 和 `env_dev.sh` 为一个脚本，通过选项来控制安装逻辑；[@mikigo](https://github.com/mikigo)

**Fix 🐛**

- 修复远程调用返回 `None` 报错的问题；
- 修复无法连续多次调用对远程终端的键鼠操作；[issues #64](https://github.com/linuxdeepin/youqu/issues/64) Fix by [@mikigo](https://github.com/mikigo)

## 2.5.3（2024/04/24）

**New 🌟**

- YouQu 在线文档 **3.0** 版本上线，重新整理了章节结构和排版，界面UI也进行了优化调整。[@mikigo](https://github.com/mikigo)

- **新增尝鲜版 `Web UI` 自动化测试功能**：[@mikigo](https://github.com/mikigo)
	- 框架为 `Web UI`自动化测试提供一个 `Fixture` 对象：`page`，它默认使用系统自带的浏览器进行测试，如果需要指定其他第三方的浏览器，提供配置项可以指定浏览器对应的路径。
	- 还提供一个 `Fixture` 对象：`native_page`，它使用 `playwright` 最新的 `chromium` 浏览器进行测试。
	- 重写了 `Playwright` 的断言语句，以保持统一的断言语句风格。
	
- **新增远程控制功能**，在用例步骤中操作远程机器，且远程操作方法实现了编辑器代码补全。[@mikigo](https://github.com/mikigo)
- 新增命令行入参或配置文件传入远程机器的 `user`、`ip`、`password` 信息，用例中通过框架提供的 `Fixture` 对象：`slaves` 获取数据，供用例层使用。[@mikigo](https://github.com/mikigo)
- 分辨率检查功能支持多组分辨率；[@mikigo](https://github.com/mikigo)
- `env_dev.sh` 初步适配欧拉系统；[@mikigo](https://github.com/mikigo)

**Fix 🐛**

- 修复远程调用报错后，本地再次调用报属性找不到的问题； [@mikigo](https://github.com/mikigo)

- 修复使用远程执行命令时，返回值为 `None`； [@mikigo](https://github.com/mikigo)
- 修复实例化远程类时，传入 `transfer_appname="xxx"` 参数后，远程路径错误的问题； [@mikigo](https://github.com/mikigo)
- 修复 `CmdCtl.sudo_run_cmd("xxx")` 方法没有返回值；[PR #62](https://github.com/linuxdeepin/youqu/pull/62) by [@DarkLii](https://github.com/DarkLii)
- 修复从 PMS 同步标签到 CSV 文件用例列表不完整的问题；[@mikigo](https://github.com/mikigo)

## 2.5.2（2024/03/27）

**New 🌟**

- `env.sh` 增加 `-p` 选项用于传递系统密码；[@mikigo](https://github.com/mikigo)
- 自动输入日志增加以 `Page` 结尾的 `class` 名称，以适应 `Web UI` 类自动化；[@mikigo](https://github.com/mikigo)

**Fix 🐛**

- 修复统计用例和方法数量功能在子项目为 `gitlab` 时，无法获取到 `commit` 详细记录的问题；[@mikigo](https://github.com/mikigo)
- 修复基于 `Python` 标准库`difflib` 做 `commit` 文件对比时，输出原始数据错误的问题；[@mikigo](https://github.com/mikigo)
- 修复域管环境下，写日志文件报权限不够的问题；[@mikigo](https://github.com/mikigo)

## 2.5.1（2024/03/14）

**New 🌟**

- `startapp` 初始化应用新增 2 条示例用例和一个方法；[issues #46](https://github.com/linuxdeepin/youqu/issues/46) by [@mikigo](https://github.com/mikigo)
- 新增子命令 `youqu manage.py git` 可用于拉取 `git` 仓库代码到 `apps` 目录下，支持统计分析仓库新增修复的用例或方法数量；[issues #40](https://github.com/linuxdeepin/youqu/issues/40) by [@mikigo](https://github.com/mikigo)
- 更新[贡献者名单](https://linuxdeepin.github.io/youqu/#_4)；

**Fix 🐛**

- 修复 `env.sh` 中 Python 虚拟环境的解释器版本没有动态获取系统中的 Python 版本的问题；[PR #51](https://github.com/linuxdeepin/youqu/pull/51) by [@saifeiLee](https://github.com/saifeiLee)
- 修复 `wayland` 环境下 `XAUTHORITY` 环境变量缺失问题；[PR #55](https://github.com/linuxdeepin/youqu/pull/55) by [@DarkLii](https://github.com/DarkLii)
- `assert_ocr_exist` 新增 `any` 匹配模式，即任意一个匹配成功则通过；[PR #55](https://github.com/linuxdeepin/youqu/pull/55) by [@DarkLii](https://github.com/DarkLii)

## 2.5.0（2024/03/04）

**New 🌟**

- `startapp` 初始化工程新增 `.gitignore` 文件；[issues #43](https://github.com/linuxdeepin/youqu/issues/43) by [@mikigo](https://github.com/mikigo)

**Fix 🐛**

- 修复 `startapp` 初始化工程中的错误；[@mikigo](https://github.com/mikigo)
- 修复 `skip` 用例在收集阶段报错；[issues #44](https://github.com/linuxdeepin/youqu/issues/44) by [@mikigo](https://github.com/mikigo)

## 2.4.6（2024/02/26）

**New 🌟**

- 计算收集用例数量剔除 `skip` 和 `skipif` 的用例数量；[@mikigo](https://github.com/mikigo)
- 报告新增显示当前目录；[@mikigo](https://github.com/mikigo)
- 启用 `Ruff` 代码检查；[issues #38](https://github.com/linuxdeepin/youqu/issues/38) by [@mikigo](https://github.com/mikigo)
- 新增定制依赖功能支持应用库定义 `deb` 形式 `Python` 包；[issues #37](https://github.com/linuxdeepin/youqu/issues/37) by [@mikigo](https://github.com/mikigo)

**Fix 🐛**

- 修复 `--noskip` 参数不能对 `skipif` 标签生效的问题；[@mikigo](https://github.com/mikigo)
- 修复 `dogtail` 获取 `application` 阻塞问题；感谢 **[@有志](https://github.com/zhao-george)**

## 2.4.5（2024/01/20）

**Fix 🐛**

- 修复 1070 华为机型 Wayland 下报错：`Xlib.error.DisplayConnectionError`；[@mikigo](https://github.com/mikigo)
- 增加 `CSV` 多条件跳过用例功能，多个以 `&&` 符号隔开即可；感谢 **[@有志](https://github.com/zhao-george)**

## 2.4.4（2024/01/19）

**New 🌟**

- 切换 `YouQu` 的正式域名为：`youqu.uniontech.com` ；[@mikigo](https://github.com/mikigo)
- 重新构建了文档 UI 布局，对多个文档模块及文档内容进行了修改、调整、优化，增加了留言模块；[@mikigo](https://github.com/mikigo)
- 1070 窗管获取窗口信息的接口 `GetAllWindowStatesList` 换了调用逻辑，YouQu 适配最新的接口；感谢 **[@泽铭](https://github.com/Jimijun)**

## 2.4.2（2023/12/27）

**New 🌟**

- 将 `IMAGE_RATE` 默认值设置为 `0.8`；经过和业务专家多轮次讨论和反复验证观察，我们认为取 `0.8` 是一个相对平衡识别准确性和用例稳定性的值；[@mikigo](https://github.com/mikigo)

## 2.4.1（2023/12/26）

**New 🌟**

- `dagtail` 新增 `center` 方法；[@mikigo](https://github.com/mikigo)

**Fix 🐛**

- 修复 `AssertCommon.assert_image_exist` 参数 `rate` 主动传入，没有用到全局配置 `IMAGE_RATE`；[@mikigo](https://github.com/mikigo)

## 2.4.0（2023/12/22）

**New 🌟**

- `UOS 1070` `Wayland` 下窗管团队提供了新的接口（`GetAllWindowStatesList`）用于获取桌面所有窗口的信息，`YouQu` 进行开发适配并兼容新老接口，至此基于 `UI` 的元素定位方案在 `Wayland` 下表现和 `X11` 下表现一致，堪称完美；[issues #21](https://github.com/linuxdeepin/youqu/issues/21)

	本次功能更新离不开多个部门领导和同事们的协助，这里特别感谢：**[@佳斌](https://github.com/king123666)** **[@孙翠](https://gitlabbj.uniontech.com/ut003620)** **[@泽铭](https://github.com/Jimijun)** **[@任斌](https://github.com/rb-union)**
	
- 新增贡献者名单及贡献规则文档；[issues #23](https://github.com/linuxdeepin/youqu/issues/23)

**Fix 🐛**

- 修复 `Wayland` 下 `sniff` 命令报错 `~/.Xauthorty` 文件不存在；[issues #22](https://github.com/linuxdeepin/youqu/issues/22)
- 修复远程执行数据回填过程中报 `HTTPError`；[issues #24](https://github.com/linuxdeepin/youqu/issues/24)
- 修复偶现测试报告生成阶段报错；[issues #25](https://github.com/linuxdeepin/youqu/issues/25)
- 修复 `globalconfig.ini` 配置文件中 `IMAGE_RATE` 配置项不生效；[issues #26](https://github.com/linuxdeepin/youqu/issues/26)

## 2.3.7（2023/12/15）

**New 🌟**

- `src/__init__.py` 里面的导入全部设置别名，以便后续各组件重命名之后仍能保持接口一致性和兼容性；[@mikigo](https://github.com/mikigo)
- 将 `Wayland` 下输入的方法区分中英文，中文按现有 `input_message` 处理，英文数字字符等使用 `press_key` 处理； [issues #17](https://github.com/linuxdeepin/youqu/issues/17)
- 有些镜像没有 `$HOME/.Xauthority` 文件（咱也不知道为啥），`YouQu` 执行会报错，我们只能创建一个空的同名文件，以确保程序能正常运行，但 `Xlib.xauth` 获取不到有效信息会有一些 `warning` 日志，看着烦人我都能接受，不能接受的是经常会导致大家在分析用例失败原因的时候将矛头指向它，然后每次我就需要解释这个 `warning` 提示不是问题，因此在底层将这部分日志输出屏蔽掉；[@mikigo](https://github.com/mikigo)

**Fix 🐛**

- 修改 `public` 目录权限，以解决远程开发时无法同步文件的问题；[@mikigo](https://github.com/mikigo)
- 修复通过标签批量执行时，传入的标签超过 `1000` 个，报错超过 `Python` 默认最大递归深度的问题；感谢 **[@有志](https://github.com/zhao-george)**

## 2.3.6（2023/12/13）

**New 🌟**

- 标签化管理支持判断系统版本跳过用例，用 `/etc/os-version` 里面的 `MinorVersion` 字段作为判断依据，在 `setting/skipif.py` 插件中实现了此功能，后续在 `CSV` 文件中可以使用此方法进行条件跳过；[issues #16](https://github.com/linuxdeepin/youqu/issues/16)

  ```python hl_lines="59-68"
  --8<-- "setting/skipif.py:59:68"
  ```

**Fix 🐛**

- 修复 `Wayland` 下系统监视器使用 `WaylandWindowInfo.window_info()`，获取的窗口名称为空；[issues #18](https://github.com/linuxdeepin/youqu/issues/20)
- 解除 `env.sh` 中某个 `deb` 包安装失败后替换源 `retry` 机制，因为用固定的源替换之后，容易出现某些包安装失败，而不容易关注到首次包安装失败的问题，给定位环境安装失败带来困难；[issues #19](https://github.com/linuxdeepin/youqu/issues/19)
- 修复 `env.sh` 里面报错 `ERROR: unknown command "cache" - maybe you meant "check"`；[@mikigo](https://github.com/mikigo)
- 修复用例收集数量为 `0` 时，报错 `ci_result.json` 文件找不到；[issues #20](https://github.com/linuxdeepin/youqu/issues/20)

## 2.3.5（2023/12/04）

**Fix 🐛**

- 修复在低版本系统上安装的 `libkf5wayland-dev` 版本问题；上个版本此问题没有完全修复，本次彻底解决；感谢 **[@玉婷](https://github.com/momiji33)**；

## 2.3.4（2023/12/04） 

**New 🌟**

- 用例执行过程中输出执行进度百分比；[@mikigo](https://github.com/mikigo)

**Fix 🐛**

- `env.sh` 增加清理 `pip` 缓存；[@mikigo](https://github.com/mikigo)
- 修复在低版本系统上安装的 `libkf5wayland-dev` 版本过高与 `libkf5waylandclient5` 版本不匹配，根据获取 `libkf5waylandclient5` 版本指定 `libkf5wayland-dev` 版；感谢 **[@玉婷](https://github.com/momiji33)**；

## 2.3.3（2023/11/22）

**Fix 🐛**

- 使用 `Xdotool` 检索窗口 ID 时，如果有多个窗口，则输出以 `\n` 结尾。在原始代码中，使用 `split("\n")` 直接拆分字符串可能会导致结果列表的最后一个元素为空字符串。在迭代窗口 ID 并将其转换为 `int` 类型时，这种情况会导致错误。感谢 **[@有志](https://github.com/zhao-george)**
- 图像识别（`image-center`）发布了新版本 `2023.11.22`  **[@有志](https://github.com/zhao-george)**，OCR（`pdocr-rpc`）发布了新版本 `2023.11.17`，增加了识别的总耗时、每次识别间隔时间；[@mikigo](https://github.com/mikigo)

## 2.3.2（2023/11/14）

**New 🌟**

- 由于 `PMS` 用例管理系统存在缺陷，框架移除从 `CSV` 反向同步标签到 `PMS` 功能；[@mikigo](https://github.com/mikigo)

**Fix 🐛**

- 优化数据回填逻辑，修复同一个用例 `py` 包含多个用例，数据回填时，中间的失败结果被后续用例更新为成功的问题；[@mikigo](https://github.com/mikigo)
- 修复某些机型下（`华为W525`）失败录屏进程阻塞的问题，是由于特殊机型下 `FFmpeg` 的 Bug 导致，但 `FFmpeg` 修复更新太耗时，框架先做异常处理；[@mikigo](https://github.com/mikigo)

## 2.3.1（2023/11/08）

**New 🌟**

- 集成 `ydotool` 键鼠控制方案，解决注销登录界面无法控制键鼠的问题；[@mikigo](https://github.com/mikigo)

**Fix 🐛**

- 修复 `PMS` 回填数据时，`timeout` 报错的问题；[@mikigo](https://github.com/mikigo)
- 修复反向同步标签，导致 `PMS` 产品库用例 `title` 为空的问题；[@mikigo](https://github.com/mikigo)

## 2.3.0（2023/10/27）

**New 🌟**

- 增加了 `YouQu` 最新版本的检查，如果本地执行版本不是最新的，会打印更新提示信息；[@mikigo](https://github.com/mikigo)
- `public` 独立发布，基础框架移除此模块，在环境部署阶段进行 `public` 模块的初始化；[@mikigo](https://github.com/mikigo)

**Fix 🐛**

- 修复 `youqu` 命令无法接收带空格的参数的问题；感谢 **[@禄烨](https://github.com/lu-xianseng)** ；
- `OCR` 检测模型升级到 `V4` 之后，在识别某些文本情况下出现不能识别的问题，暂时先回滚到 `V3` ；[@mikigo](https://github.com/mikigo)
- 修复了不同的 `case` 目录下 `py` 文件的名称一样，导出（`manage.py csvctl -p2c`）数据错误的问题；感谢 **[@有志](https://github.com/zhao-george)**；

-----------------------

## 2.2.4（2023/10/16）

**New 🌟**

- `OCR` 检测模型升级到 `V4` ，中英文场景检测模型准确率提升 4.9%，识别模型准确率提升 2%；[@mikigo](https://github.com/mikigo)

- 支持标签反向同步：将 `csv` 中的标签同步到 `pms` ； [@mikigo](https://github.com/mikigo)

- 解除子项目的工程名称以 `autotest_` 开头的限制，子项目工程名称可以为任意名称；[@mikigo](https://github.com/mikigo)

    配置文件 `globalconfig.ini` 中的 `APP_NAME` 和命令行参数 `-a/--app` 仅支持传入工程名称的全称：

    ```shell
    youqu manage.py run -a apps/autotest_deepin_music
    # 或
    youqu manage.py run -a autotest_deepin_music
    ```

- 新增导入全局配置对象：[@mikigo](https://github.com/mikigo)

    ```python
    from setting import conf
    ```

    这种写法和之前的写法效果是一样的；

    ```python
    from setting.globalconfig import GlobalConfig
    ```

- 继续尝试将一些功能模块拆分为独立构件；[@mikigo](https://github.com/mikigo)

- 增加了在线文档的显示宽度；[@mikigo](https://github.com/mikigo)

- 增加执行前显示执行的Python文件数量；[@mikigo](https://github.com/mikigo)

**Fix 🐛**

- 修复从 `pms` 标签【设备类型】为 `null` 时，同步到 `csv` 文件写入为 `null`；[@mikigo](https://github.com/mikigo)
- 修复无法导出 `csv` 文件的问题；[@mikigo](https://github.com/mikigo)
- 修复了键盘 `printscreen` 按钮无效的问题； [@mikigo](https://github.com/mikigo)
- 修复了 `sniff` 命令报错无法找到 `src` 模块的问题；[@mikigo](https://github.com/mikigo)
- 修复 `assert_ocr_not_exist` 传入多个识别目标逻辑判断错误的问题；[@mikigo](https://github.com/mikigo)

--------------------------

## 2.2.3（2023/09/15）

**New 🌟**

- 尝试将一些功能模块拆分为独立构件；[@mikigo](https://github.com/mikigo)

**Fix 🐛**

- 修复了远程执行传入 `app_name` 无法收集到用例的问题； [@mikigo](https://github.com/mikigo)
- 优化了 `docs` 文档内容及排版；[@mikigo](https://github.com/mikigo)

-----------------------------

## 2.2.1（2023/09/13）

New 🌟

- 新增用例脚本 `py` 文件 `id` 自动同步到 `csv` 文件功能；[@mikigo](https://github.com/mikigo)
- 新增自动从 `pms` 上获取用例相关标签的功能；[@mikigo](https://github.com/mikigo)

Fix 🐛

- 修复了 `letmego` 在开发调试时也会记录执行过程的问题；[@mikigo](https://github.com/mikigo)
- 优化了在线文档内容和排版；[@mikigo](https://github.com/mikigo)

----------------------------------

## 2.2.0（2023/09/05）

New 🌟

- 正式启用 `letmego` 技术方案；[@mikigo](https://github.com/mikigo)

Fix 🐛

- 对 `docs` 里面细化了远程执行章节的描述；[@mikigo](https://github.com/mikigo)
- 对 `docs` 里面优化了标签化管理章节的描述；[@mikigo](https://github.com/mikigo)

## 2.1.5（2023/08/31）

New 🌟

- 将有趣的文档系统迁移到 **[@linuxdeepin](https://github.com/linuxdeepin/youqu)** ，剥离文档中的图片资源，采用 `CDN` 网络加速方式加载；[@mikigo](https://github.com/mikigo)

- 尝试合入一个有趣的功能；

Fix 🐛

- 修复了 `Wayland` 键鼠工具没有鼠标相对移动方法 `moveRel` 的问题； [@mikigo](https://github.com/mikigo)
- 修复了` Wayland` 下获取窗口信息功能模块中环境变量的问题；[@mikigo](https://github.com/mikigo)
- 优化了 `startproject` 功能的一些信息输出；[@mikigo](https://github.com/mikigo)
- 修复了特殊场景下 `env_dev.sh` 开发环境部署是可能影响到正式环境 `env.sh` 的问题；[@mikigo](https://github.com/mikigo)

## 2.1.2（2023/08/22）

New 🌟

- 增加 `OCR` 识别自动重试机制，默认重试 2 次，支持动态传入重试次数；[@mikigo](https://github.com/mikigo)
- 使用窗管最新提供的二进制接口，优化基于 `UI` 的元素定位方案在 `Wayland` 下获取窗口信息的方法；感谢桌面测试部 **@何权 @孙翠** 、窗管研发 **@泽铭** 的大力支持。
- 扩充 `skipif` 条件跳过的功能函数：[@mikigo](https://github.com/mikigo)
  - `skipif_xdg_type` 支持 `x11` 或 `wayland` 上跳过；
  - `skipif_cpu_name` 支持不同 `cpu` 上跳过，比如：`skipif_cpu_name-KLVVW5821`；


## 2.1.0（2023/08/18）

Fix 🐛

- 修复 SW 架构环境依赖的问题，原因是之前我这里本地没有 SW 的机器，没有做相关适配；[@mikigo](https://github.com/mikigo)

- 修复子项目单独需要三方包 `pexpect`，由于之前是预装到镜像里面的，但基础框架不需要，因此没有装载到虚拟环境里面，导致子项目依赖报错。[@mikigo](https://github.com/mikigo)

- 修复子项目 cv 导入报错的问题；[@mikigo](https://github.com/mikigo)

    原因为：youqu 的图像识别功能兼容两种情况，一种是面向服务，就是本地测试机不需要安装 `OpenCV`，用例中的图像识别会通过远程服务接口进行图像识别和结果获取；第二种是原生，就是本地直接安装 `OpenCV` 直接用。两个情况的优先级是优先判断本地存在，否则走服务。

    前面我们已经把 OCR 功能做了服务化，基于 1 年多以来的观察，用起来很稳定，再一个就是 `OpenCV` 安装包是比较臃肿的，粗略数了下依赖有 `30+` 个，而且在各架构上依赖包还不尽相同，装载到虚拟环境方案中不太好处理，所以本次 2.0 版本我们大胆的将图像识别的默认功能修改为面向服务的方式，前期测试一切看起来都很和谐。

    但是没注意到之前给海燕姐那边项目单独定制做了个图像识别接口（为了能简单平滑的迁移到 youqu），此接口底层没有兼容服务化，所以她那边的项目调用此定制接口会报 cv 导入的问题。

    由于将这个定制图像识别接口进行服务化兼容改造需要一定时间，改完还需要测试，但本次时间比较紧，因此先把 `OpenCV` 装进虚拟环境，后续版本再考虑针对此接口做修改。

## 2.0.0（2023/08/16）

`YouQu`（自动化测试基础框架）开源了，同时推出了 2.0 版本。

感谢**王波总、架构师徐小东、研发经理郑幼戈、刘郑**等研发同事的大力支持。

New 🌟

**1、新的基础框架代码获取方式及新的初始化工程命令**

`YouQu` 后续均通过 `PyPI` 进行包的发布，也就是说后续可以使用 pip 进行安装：

```sh
sudo pip3 install youqu==2.0.0
```

这里有 2 个小点要注意：

- 推荐使用 `sudo pip3` （加 sudo）进行安装；

    如果不加 sudo 有些机器可能 `$HOME/.local/bin` 不在系统 PATH 环境目录下，在不添加环境变量的情况下，会出现 `YouQu` 的初始化工程命令（youqu-startproject）无法使用的问题；

    当然，将上述路径添加到环境变量之后也是可以用的，所以我这里是推荐加 sudo，不加 sudo 也是可以的，只是需要关注下环境变量的问题。

- 推荐指定版本号（`youqu==2.0.0`）安装，如果不指定版本号默认是安装最新发布的 YouQu 版本，你可以在 [PyPI](https://pypi.org/project/youqu/) 上的 Release history 里面查看有哪些版本。

    安装之后会自动生成一个系统命令 youqu-startproject，使用它可以初始化工程，这里以音乐举例；

    ```shell
    youqu-startproject autotest_deepin_music
    ```

    这样就会在当前目录下生成一个 `autotest_deepin_music` 目录，里面包含了基础框架所有的代码；

    之后，还是在 `apps` 目录下，放入子项目的AT代码即可，使用方法和过去一样，这里就不多介绍。

    另外，除了通过 pip 获取以外，仍然可以通过源码获取（直接 git clone）。

    值得一提的是，使用 pip 安装 `YouQu` 时，`YouQu` 包的大小才 `600+` k，安装速度起飞。

**2、新的AT虚拟化环境部署方案**

为了解决以下问题：

- 过去一段时间咱们经常出现的，不同的AT项目在同一台机器上部署环境时依赖版本冲突的问题，新方案不同的项目会动态生成自己的虚拟环境，相互之间不影响；
- 业内为了解决版本冲突问题一般都会使用 `Python` 虚拟环境的工具，但是都有个问题，无法管理 deb 包形式发布的 Python 包，本次我们解决了这个问题，能够完全管理常规的 `Python` 包，也能管理到 deb 包形式发布的 Python 三方包；

    虚拟化环境部署使用方法：

    ```shell
    bash env.sh
    ```

    可以看出来和原来使用方法没有变化，也就是说从使用的角度是完全没有区别的，只是内部做了不同的事情。

    值得一提的是，本机部署的功能仍然保留 `env_dev.sh`，可以作为开发时的环境部署。

**3、新的驱动命令**

过去咱们都是使用这样的命令来驱动执行：

```shell
python3 manage.py run
```

由于默认基于虚拟化环境部署方案，因此我们增加了一个系统命令 `youqu`；

**新的驱动方式：**

```shell
youqu manage.py run
```

只需要把 python3 替换成 youqu 就可以了，看起来很和谐~

**4、新的文档地址**

过去咱们 `YouQu` 的在线文档是部署在公司内网的，现在开源到 github 了，外部开发者肯定访问不到内网的文档，因此需要将文档部署到公网【[公网文档](https://linuxdeepin.github.io/youqu/)】；

公网文档使用的是 github pages（白嫖怪一顿狂喜~~），但可能会出现文档速度慢的问题（代理下就好了），不过没关系，咱们【[内网文档](http://youqu.uniontech.com/)】仍然保留，文档内容一样，访问速度更快。

**5、其他一些小小功能更新：**

（1）新增关闭分辨率检测的参数值；[@mikigo](https://github.com/mikigo)

```sh
youqu manage.py run --resolution no
```

或者修改 `setting/globalconfig.ini` 里面的配置：

```ini
;检查测试机分辨率, 比如：1920x1080
;no: 表示不做分辨率校验
RESOLUTION = 1920x1080
```

`resolution` 这个参数一直都有的，只不过之前是用于指定分辨率大小，比如 `--resolution 1920x1080`，但有些接口的项目不需要这个检查，可以给它个 no 就好了，当然 CICD 上关闭，需要流水线上把这个参数加上；

（2）新增失败录屏从第几次失败开始录制视频的命令行参数；[@mikigo](https://github.com/mikigo)

之前这个配置项只能在 `setting/globalconfig.ini` 里面的配置：

```ini
;失败录屏从第几次失败开始录制视频。
;比如 RECORD_FAILED_CASE = 1 ，表示用例第 1 次执行失败之后开始录屏，RERUN >= RECORD_FAILED_CASE。
;1.关闭录屏：RECORD_FAILED_CASE > RERUN
;2.每条用例都录屏：RECORD_FAILED_CASE = 0
RECORD_FAILED_CASE = 1
```

现在将开发到命令行参数。

```sh
youqu manage.py run --record_failed_case 2
```

Fix 🐛

- 修复 `remote` 执行时，在某些情况下无法生成测试报告的问题；[@mikigo](https://github.com/mikigo)

## 1.3.0（2023/07/10）

Fix 🐛 

- 进一步优化了 `env.sh` 安装 `Python` 的三方源；参考：[配置Python源的几种方法](https://funny-dream.github.io/funny-docs/Python/配置Python源的几种方法/)
- 修复 `wayland_autotool` 受安全管控的问题；[@mikigo](https://github.com/mikigo)
- 修复了`wayland`下偶现找不到 `.Xauthority` 文件的问题； [@mikigo](https://github.com/mikigo)

## 1.2.9（2023/06/26）

Fix 🐛

- 优化远程执行 `remote` 的参数直接传给远程机器的 `run` 命令，不用再单独处理远程执行的参数逻辑，后续专注于本地执行功能开发，远程执行自动适用；[@mikigo](https://github.com/mikigo)

- `env.sh` 移除 `pyyaml` 安装，由子项目在 `requirement.txt` 里面定义，框架自动加载；[@mikigo](https://github.com/mikigo)

- 优化了 `env.sh` 安装 `Python` 的三方源；[@mikigo](https://github.com/mikigo)

## 1.2.8（2023/06/09）

Fix 🐛

- 修复了 `pypi` 安装 `numpy` 存在系统安全管控的问题；[@mikigo](https://github.com/mikigo)

## 1.2.7（2023/06/08）

Fix 🐛

- `env.sh` 中安装 `Python` 包未指定版本时，日志输出安装的版本；[@mikigo](https://github.com/mikigo)

  ```shell
  pdocr-rpc                       2.0.1
  allure-custom                   1.2.1
  funnylog                        1.1.3
  ```

- 修复 `-f` 测试套件执行报错的的问题；[@mikigo](https://github.com/mikigo)

## 1.2.6（2023/06/07）

Fix 🐛

- 修复 `wayland` 上调用鼠标中键、右键不生效的问题；[@mikigo](https://github.com/mikigo)
- 修复 `pubilic/dde_desktop_public_widget` 里面通过配置文件定位桌面文件的方法，坐标没有拆包的问题；[@mikigo](https://github.com/mikigo)
- 优化了等待的日志输出；[@mikigo](https://github.com/mikigo)
- `pycreeze` 版本升级到 `0.1.29`，导致与 `pyautogui` `0.9.53` 不兼容，`env.sh` 里面增加指定 `pycreeze` 版本为 `0.1.28`；[@mikigo](https://github.com/mikigo)


## 1.2.5（2023/05/16）

New 🌟

-  `--app` 参数后面新增支持 `autotest_xxx` 和 `apps/autotest_xxx` 两种写法，目前支持三种参数传入方式：

  ```shell
  ~$: youqu run -a deepin-music
  ~$: youqu run -a autotest_deepin_music
  ~$: youqu run -a apps/autotest_deepin_music
  ```

​		后两种入参方式可以很方便在输入命令的过程中使用补全。[@mikigo](https://github.com/mikigo)

- remote 远程执行新增从命令行传入测试机信息，远程机器的`user@ip:password`,多个机器用'/'连接,如果 `password` 不传入,默认取 `setting/remote.ini` 中 `CLIENT_PASSWORD` 的值,比如：`uos@10.8.13.xx:1` 或 `uos@10.8.13.xx` ；[@mikigo](https://github.com/mikigo)

  ```shell
  python3 manage.py remote -c uos@10.8.13.xx/uos@10.8.13.xx
  python3 manage.py remote -c uos@10.8.13.xx:1/uos@10.8.13.xx:2
  ```

Fix 🐛

- 日志模块修改为函数执行之前打印日志；[@mikigo](https://github.com/mikigo)
- 日志模块增加白名单，通过类名开头，结束，包含等关键字控制需要打印的函数日志；[@mikigo](https://github.com/mikigo)
- 远程执行时，如果传入了 `app_name` 只会将 `apps` 目录下 `app_name` 的目录发送到测试机；[@mikigo](https://github.com/mikigo)
- `env.sh` 移除 `python3-dev`；[@mikigo](https://github.com/mikigo)
- 修复 `Wayland` 下 `env.sh` 环境安装失败的问题，优化了 `deb` 依赖安装的逻辑；[@mikigo](https://github.com/mikigo)
- 将 `env.sh` 刷新源的日志在终端显示，解决在 `CI` 环境下，长时间不输出日志连接中断的问题；[@mikigo](https://github.com/mikigo)
- 修复`1060` 华为机型安装键鼠工具时依赖不兼容的问题；[@mikigo](https://github.com/mikigo)

## 1.2.4（2023/02/27）

Fix 🐛

- 修改 `CURRENT` 文件；[@mikigo](https://github.com/mikigo)

## 1.2.3（2023/02/27）

New 🌟

- `pylint.sh` 支持通过位置参数传入文件路径：`bash pylint.sh apps/autotest_deepin_music`,好处是参数路径可以在终端补全；[@mikigo](https://github.com/mikigo)
- 新增系统命令 `youqu-pylint` ，用于静态代码扫描，使用方法: `youqu-pylint apps/autotest_deepin_music`；[@mikigo](https://github.com/mikigo)
- 由于系统一些 `dbus` 接口改变，公共库中的 `dbus` 方法将不再维护，由子项目在 `other_widget.py` 里面进行维护；[@mikigo](https://github.com/mikigo)

Fix 🐛

- 修复 `ssh` 环境下运行提示 “无法连接” 的问题；[@mikigo](https://github.com/mikigo)
- 修复运行时程序退出，不输出异常日志的问题；[@mikigo](https://github.com/mikigo)
- 修复`youqu remote xxx` 远程执行时，在服务端 `Ctrl + C` 无法停止程序运行的问题；[@mikigo](https://github.com/mikigo)

## 1.2.2（2023/02/08）

New 🌟

- 新增气泡类图像识别方案；`image_utils.py::ImageUtil::get_during`；[@mikigo](https://github.com/mikigo)
- 图像识别新增指定区域识别，传入 `[x, y, w, h]`，x: 左上角横坐标；y: 左上角纵坐标；w: 宽度；h: 高度；根据匹配度返回坐标；[@mikigo](https://github.com/mikigo)
- 图像识别新增指定目标图片，传入目标图片路径；[@mikigo](https://github.com/mikigo)
- `env.sh` 移除 `pypinyin`；[@mikigo](https://github.com/mikigo)
- 优化执行 `env.sh` 时的日志输出；[@mikigo](https://github.com/mikigo)
- `manage.py` 移除了参数 `session_timeout` ，框架根据全局的 `timeout` 以及用例自定义的 `timeout` 自动计算出 `sessiontimeout` 的值；[@mikigo](https://github.com/mikigo)
- 新增 ocr 服务器链接重试，默认重试1次，支持动态传入参数；[@mikigo](https://github.com/mikigo)

Fix 🐛

- 修复了一些 pylint 扫描的代码风格问题；[@mikigo](https://github.com/mikigo)
- 重新设计了测试报告主题；[@mikigo](https://github.com/mikigo)

## 1.2.1（2023/01/06）

New 🌟

- 支持使用系统命令 `youqu` 执行用例；可将`python3 manage.py` 替换为 `youqu` ：

  ``` shell
  youqu run -a deepin-music -k 001
  ```

- `RPC` 服务 `IP` 地址修改为域名：http://youqu.uniontech.com，指定不同的端口；[@mikigo](https://github.com/mikigo)
- 在线文档地址修改为域名：http://youqu.uniontech.com，原来的地址 10.8.10.215 将不在使用；[@mikigo](https://github.com/mikigo)

Fix 🐛

- 修复 `--count` 参数可能出现与其他框架的工程依赖存在冲突，报错重复注册的问题；[@mikigo](https://github.com/mikigo)
- 修复 CI 环境下多个工程存在 Python 环境变量指向错误，导包报错的问题；[@mikigo](https://github.com/mikigo)
- 修复单独运行方法时无日志输出的 Bug；[@mikigo](https://github.com/mikigo)


## 1.2.0（2022/12/30）

1.1.4 版本适配持续集成流水线且新增了较多新特性，我们计划使用 1.1.4 版本运行一段时间，1.2.0 版本将修复期间出现的 Bug，然后作为稳定版本发布。

New 🌟

- 修改工程名称为 `youqu`；[@mikigo](https://github.com/mikigo)
- 将 sphinx 文档工程迁移到单独的仓库；[@mikigo](https://github.com/mikigo)

Fix 🐛

- 修复 startapp 创建工程时存在工程名称时无法继续创建；[@mikigo](https://github.com/mikigo)
- 修复了 OCR 服务在并发时可能出现无法返回结果的问题，提升 OCR 服务高并发稳定性；[@mikigo](https://github.com/mikigo)
- 修复 PMS 同步标签到 CSV 文件不支持用例库的问题；[@mikigo](https://github.com/mikigo)

## 1.1.4（2022/12/14）

New 🌟

- 新增 `startapp` 子命令创建子项目工程模板: `python3 manage.py startapp autotest_deepin_xxx` ；[@mikigo](https://github.com/mikigo)

- 新增指定用例重复执行次数；[@mikigo](https://github.com/mikigo)

- 去掉批量执行前收集用例的步骤；[@mikigo](https://github.com/mikigo)

- 增加开始执行时打印一些执行参数，如：

  ```shell
  用例收集数量:	99
  失败重跑次数:	1
  最大失败次数:	49
  用例超时时间:	200.0s (03分20秒)
  会话超时时间:	11880s (3小时18分0秒)
  ```

- 定制修改allure报告logo、title、默认语言；[@mikigo](https://github.com/mikigo)

- `manage.py` 执行开始时打印 logo 和当前版本：[@mikigo](https://github.com/mikigo)

  ```shell
   ██╗   ██╗  ██████╗  ██╗   ██╗  ██████╗  ██╗   ██╗ 
   ╚██╗ ██╔╝ ██╔═══██╗ ██║   ██║ ██╔═══██╗ ██║   ██║ 
    ╚████╔╝  ██║   ██║ ██║   ██║ ██║   ██║ ██║   ██║ 
     ╚██╔╝   ██║   ██║ ██║   ██║ ██║▄▄ ██║ ██║   ██║ 
      ██║    ╚██████╔╝ ╚██████╔╝ ╚██████╔╝ ╚██████╔╝ 
      ╚═╝     ╚═════╝   ╚═════╝   ╚══▀▀═╝   ╚═════╝  
  
  
   ▄█   ▄█   █ █ 
    █ ▄  █ ▄ ▀▀█ 
  ```

- 新增指定用例执行次数；[@mikigo](https://github.com/mikigo)

  - 装饰器方法指定次数；

    ```python
    @pytest.mark.count(2)
    def test_music_679537():
        pass
    ```

  - 命令行参数指定次数；

    ```shell
    python3 manage.py run -a deepin-music -k 001 --count 2
    ```

- ​	image_utils 增加函数 save_temporary_picture，支持指定屏幕区域截图并返回图片存放的本地路径，后续使用 assert_image_exist 进行断言；[@mikigo](https://github.com/mikigo)

  - ```Python
    def test_music_679537(self):
        pic_path = DeepinMusicWidget.save_temporary_picture(x, y, width, height)
        ...... # 中间操作
        self.assert_image_exit(pic_path)
    ```

- button_center 新增 btn_size 获取控件左上角坐标及长宽，用于动态的截取元素的图片，可用于定位断言；[@mikigo](https://github.com/mikigo)

  - ```python
    def test_music_679537(self):
        pic_path = DeepinMusicWidget.save_temporary_picture(*DeepinMusicWidget().ui.btn_size("所有音乐按钮"))
        ...... # 中间操作
        self.assert_image_exit(pic_path)
    ```

- allure 报告中定位问题除了日志、截图、录屏外，调用的函数增加了 step 步骤展示；[@mikigo](https://github.com/mikigo)

- `env.sh` 新增安装子项目 `Python` 三方依赖，在子项目根目录下写 `requirement.txt` 文件，`env.sh` 会自动加载；[@mikigo](https://github.com/mikigo)

- ocr 识别新增支持传入目标图片路径进行文字识别，减少因全屏识别时，其他文字的干扰；[@mikigo](https://github.com/mikigo)

  - ```Python
    # 断言音乐的删除弹窗中，包含了“确认”的文字
    self.assert_ocr_exist("确认", picture_abspath=DeepinMusicWidget.save_temporary_picture(*DeepinMusicWidget().ui.btn_size("删除弹窗")))
    ```

- 断言函数的调用也会自动打印日志;[@mikigo](https://github.com/mikigo)

- `env.sh` 新增裁剪依赖的方案；[@mikigo](https://github.com/mikigo)

Fix 🐛

- 修复 `Jenkins` 环境下， `apps` 目录下子项目存在 `auotest_deepin_xxx@tmp` 目录，在传入 `app_name` 后无法执行用例的问题；[@mikigo](https://github.com/mikigo)
- 修复自动生成 `case_list.csv` 文件时，用例顺序被调整的问题；[@mikigo](https://github.com/mikigo)
- `env.sh` 环境安装移除 git 和 curl；[@mikigo](https://github.com/mikigo)
- 修复用例在 setup 阶段报错后，未写入 ci_result.json 的问题；[@mikigo](https://github.com/mikigo)
- 移除 `uos_ci.py`；[@mikigo](https://github.com/mikigo)

## 1.1.3（2022/10/28）

New 🌟

- 新增图像断言成功输出匹配度；[@mikigo](https://github.com/mikigo)
- 新增环境安装 yaml 依赖；[@mikigo](https://github.com/mikigo)
- 新增测试套执行、数据回填兼容用例库ID和产品库ID；[@mikigo](https://github.com/mikigo)
- 新增测试结果表情显示，并优化了日志的排版；[@mikigo](https://github.com/mikigo)
- 新增 `--top {number}` 用于记录系统资源占用情况，日志生成到 `report/logs/top.log`；[@mikigo](https://github.com/mikigo)

Fix 🐛

- 修复用例收集阶段报错，但终端没有错误日志输出的问题；[@mikigo](https://github.com/mikigo)
- 修改失败用例回溯日志为详细级别；[@mikigo](https://github.com/mikigo)
- 修复了执行进度未计算跳过用例的问题，并优化了进度获取的算法；[@mikigo](https://github.com/mikigo)
- 修复 `env.sh` 在 V23 环境下安装无法读取密码的问题；[@mikigo](https://github.com/mikigo)
- 修复了 pms 测试套执行或测试单执行时，用例ID兼容用例库ID和产品库ID；[@mikigo](https://github.com/mikigo)
- env.sh 里面 hub.deepin.com 更换成 it.uniontech.com；[@mikigo](https://github.com/mikigo)
- uos_ci.py 测试结果统计时，总数剔除 skip 的数量；[@mikigo](https://github.com/mikigo)

## 1.1.2（2022/09/21）

New 🌟

- 在没有安装 `dogtail` 的情况下，也能使用 `sniff` 工具；[@mikigo](https://github.com/mikigo)

Fix 🐛

- 修复持续集成流水线中没有安装 AT 环境执行 `uos_ci.py` 报错的问题；[@mikigo](https://github.com/mikigo)

## 1.1.1（2022/09/19）

New 🌟

- 新增执行进度显示，每条用例执行时日志输出当前进度：[当前指定第几条/用例总数]；[@mikigo](https://github.com/mikigo)
- 新增终端输出用例执行结束之后所有失败用例的列表；[@mikigo](https://github.com/mikigo)
- 关闭终端输出捕获用例执行过程日志快照；[@mikigo](https://github.com/mikigo)
- 优化终端输出失败信息冗长为简要信息输出；[@mikigo](https://github.com/mikigo)
- 新增终端输出显示 10 个执行最慢的用例列表，并详细列出各个阶段的耗时；[@mikigo](https://github.com/mikigo)
- 失败重跑用例重跑之前延迟 1 秒；[@mikigo](https://github.com/mikigo)
- 新增收集阶段报错，仍然强制执行；[@mikigo](https://github.com/mikigo)
- 用例收集时仅在 `apps` 目录下进行，忽略 `src,setting,public` 目录；[@mikigo](https://github.com/mikigo)
- 新增 `allure` 报告备份功能，默认备份至 `allure_back` 目录下；[@mikigo](https://github.com/mikigo)
- `manage.py`新增参数 `--lastfailed` 用于只跑上次失败用例的功能；[@mikigo](https://github.com/mikigo)

Fix 🐛

- 修复了在没有指定应用名称执行时，xml 报告生成路径异常的问题；[@mikigo](https://github.com/mikigo)
- 修复了 `uos_ci.py` 传入 `timeout` 和 `session_timeout` 不生效的问题；[@mikigo](https://github.com/mikigo)

## 1.1.0（2022/09/16）

New 🌟

- 新增PMS数据回填功能，支持多种数据回填模式；[@mikigo](https://github.com/mikigo)
- 优化了通过测试套件执行时PMS 爬虫的性能；[@mikigo](https://github.com/mikigo)
- 新增 `.gitmodules` 文件，用于标记所有子项目，方便统一拉取代码；[@mikigo](https://github.com/mikigo)
- `env.sh` 适配社区版上安装自动化环境；[@mikigo](https://github.com/mikigo)
- 增加执行过程中立即显示错误的功能；[@mikigo](https://github.com/mikigo)
- `README.md` 增加 `Wayland` 下使用、测试报告查看、常见问题等的文档说明；[@mikigo](https://github.com/mikigo)
- 增加了用例执行过程中对 `setup`、`call`、`teardown` 进行日志分段；[@mikigo](https://github.com/mikigo)

Fix 🐛

- 修复了 `确认修复` 列没写表头，但写了 `Fix 🐛ed-xxx` 标签，出现的程序报错问题；[@mikigo](https://github.com/mikigo)
- 修复了同一应用内多个 `csv` 文件中 `确认修复` 列有的写了，有的没写，可能出现的程序报错的问题；[@mikigo](https://github.com/mikigo)
- 修复了 `INFO` 日志，显示为 `DEBUG` 的问题；修复了部分机器上 `INFO` 日志内容显示为红色的问题；[@mikigo](https://github.com/mikigo)
- 修复了用例收集阶段报错看不到详细信息的问题；[@mikigo](https://github.com/mikigo)

## 1.0.2（2022/08/22）

New 🌟

- 移除 `loguru`，替换为 `logging`，接口保持不变，上层用例不受影响；[@mikigo](https://github.com/mikigo)
- 默认开启 `coredump`；[@mikigo](https://github.com/mikigo)

Fix 🐛

- 修复了三方库 `loguru` 偶现异常，导致程序中断的问题；[@mikigo](https://github.com/mikigo)
- 修复了第一次失败不会关闭文件选择框的问题；[@mikigo](https://github.com/mikigo)

## 1.0.1（2022/08/12）

New 🌟

- 新增 `RELEASE.md` 文件，用于记录历史发布版本的更新内容；[@mikigo](https://github.com/mikigo)

- 兼容 `Wayland` 模式下执行用例，上层用例不用管当前测试机执行环境，框架会自动根据当前环境走不同的代码逻辑；[@mikigo](https://github.com/mikigo)
- 由于需要修改 `dogtail` 源代码，因此将修改后的源码放入到核心库里面 `src/depends/dogtail` 后续版本**将**不需要在系统中安装`dogtail`；[@mikigo](https://github.com/mikigo)
- 如果应用库同样使用了系统安装的 `dogtail` 可能会报错，解决方案是将代码中的 `import dogtail` 修改为 `from src.depends import dogtail` ;[@mikigo](https://github.com/mikigo)

Fix 🐛

- 重跑失败之后才会关闭文件选择框，修改为失败之后会关闭文件选择框；[@mikigo](https://github.com/mikigo)






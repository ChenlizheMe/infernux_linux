# Infernux Linux 平台插件

这是 [Infernux](https://github.com/ChenlizheMe/Infernux) 游戏引擎的官方 Linux 构建插件。它为编辑器提供 Linux x64 导出能力，并随包提供已经为对应引擎版本编译好的 Player 和 Python 运行时。

[English](README.md) · [Infernux 引擎](https://github.com/ChenlizheMe/Infernux) · [插件模板](https://github.com/ChenlizheMe/infernux_plugin_template) · [发布制品](https://github.com/ChenlizheMe/infernux_linux/releases)

![Infernux Linux 导出流程](package/plugin_pages/media/overview.png)

## 插件提供什么

- 编辑器中的 `linux-x64` 构建目标
- 预编译的原生 Player、CPython 3.13 运行时和并行模块
- Vulkan 渲染与 Linux 导出流程
- 不暴露可编辑项目目录的二进制内容包

| 包标识 | 版本 | 适配引擎 | 构建环境 | 目标平台 |
| --- | --- | --- | --- | --- |
| `infernux/platform-linux` | 0.2.0 | Infernux 0.4.0 | Linux x64 | Linux x64 |

## 安装与导出

在 Infernux 中打开**插件**窗口，从官方列表选择 **Infernux Linux Platform**，导入并启用即可。官方安装优先使用 Infernux 分发服务，网络不可用时回退到 GitHub Releases；也可以从本仓库下载 `infernux.platform-linux.inxpkg` 手动导入。

在构建设置中选择 `linux-x64` 后导出。发布时需要保留完整输出目录以及 Player 的可执行权限。目标机器还需要可用的 Vulkan 驱动和 Player 报告的系统库。普通用户不需要引擎源码、CMake 或编译工具链。

该插件在 Linux 上构建 Linux，不提供从 Windows 交叉构建 Linux 的能力。

## 仓库说明

只有 `package/` 会进入插件包；仓库文档、构建脚本、测试和 CI 都留在包外。

```text
package/
  inx_package.json
  editor/infernux_linux/
  plugin_pages/
```

维护者使用引擎的 `linux-clang-player` preset，把 Player 直接产出到本仓库。推送与版本一致的 `v<version>` 标签后，GitHub Actions 会自动发布插件及 release manifest。

## 许可证

[MIT](LICENSE)。随包提供的第三方组件继续遵守各自的许可证。

# Infernux Linux 平台插件

[English](README.md) · [发布制品](https://github.com/ChenlizheMe/infernux_linux/releases) · [Infernux](https://github.com/ChenlizheMe/Infernux)

![Linux 构建流程](package/plugin_pages/media/overview.png)

插件携带预编译 Linux Player、CPython 运行时和可选并行模块。普通导出只组装这些文件和项目 cook 内容，不需要引擎源码、CMake 或编译工具链。

## 基本信息

| 项目 | 内容 |
| --- | --- |
| 包标识 | `infernux/platform-linux` |
| 插件版本 | 0.2.0 |
| 引擎兼容范围 | ==0.4.0 |
| 构建目标 | `linux-x64` |
| 构建宿主 | Linux x64 |

## 安装

1. 在 Infernux 0.4.0 中打开项目，进入插件面板。
2. 在官方列表选择 Infernux Linux Platform，导入并启用。
3. 打开构建设置，选择目标，按诊断补齐依赖后导出。

如果编辑器仍使用旧版内置目录，可以手动添加 GitHub 源 `https://github.com/ChenlizheMe/infernux_linux`，或从 [Releases](https://github.com/ChenlizheMe/infernux_linux/releases/latest) 下载 `infernux.platform-linux.inxpkg` 后导入。GitHub 自动生成的源码 ZIP 是作者仓库，不是插件安装制品。

## 环境要求

Linux x64 的 Infernux 0.4.0（Python 3.13）。对应的预编译 Player 载荷由本插件提供。运行游戏需要可用的 Vulkan 驱动和引擎要求的平台库。

## 宿主边界

Linux 构建 Linux。此包不提供从 Windows 交叉编译 Linux Player 的能力。禁用或卸载只移除其目标，不改变公共构建服务。

## 输出与排错

分发完整的游戏目录，包括原生可执行文件、运行库和打包内容；传输时保留可执行权限。cook 后的内容进入引擎二进制包，不直接暴露可编辑的 Assets/Library 目录树；这不是 DRM。

目标未出现时检查编辑器是否运行在 Linux x64，以及插件是否启用。Player 载荷缺失或不兼容时，通过插件的版本页显式安装兼容的完整平台制品。Player 启动失败时，检查可执行权限、Vulkan 驱动和报错指出的系统库。

## 开发与打包

只有 `package/` 内的内容进入 InxPackage。外层 README、SVG 配图源文件、发布流程和构建脚本属于仓库，不进入插件。引擎内文档独立位于 `package/plugin_pages/`。

```text
package/
  inx_package.json
  editor/infernux_linux/
  plugin_pages/
package.py
release.py
README.md
README.zh-CN.md
```

运行 `python package.py dist/infernux.platform-linux.inxpkg` 本地打包。脚本仅使用 Python 标准库，不需要导入或安装 Infernux。在外层进行构建，最后将需要交付的文件放进 package/ 即可。

维护者构建引擎的 `linux-clang-player` CMake preset。它直接将载荷产出到本仓库的 `package/editor/infernux_linux/player/`，将最终 `.inxpkg` 和发布清单产出到 `dist/`。发布 CI 在 Linux 宿主上，用对应引擎发布线构建本插件的精确版本；不生成或传递中间运行时 ZIP，也没有独立压缩包中转渠道。

维护者运行 `python release.py v0.2.0` 生成插件和发布清单；推送与插件版本一致的标签后，由 GitHub Actions 打包并上传两个文件。编辑器根据发布清单选择兼容版本。

## 许可证

[MIT](LICENSE)。第三方 SDK 和引擎运行时各自遵守原有许可证，不因本插件而改变。

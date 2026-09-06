# Linux 平台

![构建流程](media/overview.png)

使用 Linux 引擎 wheel 中的原生运行时构建 Linux x64 Player。插件负责注册 Linux 导出器，公共 cook 与打包流程由引擎提供。

## 构建前准备

Linux x64 的 Infernux 0.4.0，包含原生 Player 和 Python 3.13 运行时包。运行游戏需要可用的 Vulkan 驱动和引擎要求的平台库。

## 宿主边界

Linux 构建 Linux。此包不提供从 Windows 交叉编译 Linux Player 的能力。禁用或卸载只移除其目标，不改变公共构建服务。

## 输出与排错

分发完整的游戏目录，包括原生可执行文件、运行库和打包内容；传输时保留可执行权限。cook 后的内容进入引擎二进制包，不直接暴露可编辑的 Assets/Library 目录树；这不是 DRM。

目标未出现时检查编辑器是否运行在 Linux x64，以及插件是否启用。原生运行时缺失需修复引擎安装。Player 启动失败时，检查可执行权限、Vulkan 驱动和报错指出的系统库。

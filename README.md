# Infernux Linux Platform

The official Linux build plugin for [Infernux](https://github.com/ChenlizheMe/Infernux), an open-source game engine with a C++17/Vulkan core and Python authoring layer. It turns an Infernux project into a native Linux x64 game using a Player already compiled for the engine release.

[简体中文](README.zh-CN.md) · [Infernux Engine](https://github.com/ChenlizheMe/Infernux) · [Plugin Template](https://github.com/ChenlizheMe/infernux_plugin_template) · [Releases](https://github.com/ChenlizheMe/infernux_linux/releases)

![Infernux Linux export workflow](package/plugin_pages/media/overview.png)

## What this plugin provides

- The `linux-x64` build target in the Infernux Editor
- A precompiled native Player, CPython 3.13 runtime, and parallel module
- Vulkan rendering and the Linux export pipeline
- Binary game-content packaging instead of an editable project tree

| Package | Version | Compatible engine | Build host | Target |
| --- | --- | --- | --- | --- |
| `infernux/platform-linux` | 0.2.0 | Infernux 0.4.0 | Linux x64 | Linux x64 |

## Install and use

Open **Plugins** in Infernux, select **Infernux Linux Platform** from the official catalog, then import and enable it. Official installs use the Infernux distribution service first and GitHub Releases if that channel is unavailable. Manual installation is available through `infernux.platform-linux.inxpkg` on the Releases page.

Choose `linux-x64` in the build settings and export. Ship the executable, runtime libraries, and packaged game data as one directory, preserving executable permissions. A Vulkan-capable driver and the system libraries reported by the Player are required at runtime. Users do not compile the engine or run CMake.

Linux builds Linux; this package does not cross-compile a Linux Player from Windows.

## Repository guide

Only `package/` becomes the installable plugin. Repository documentation, build scripts, tests, and CI stay outside the `.inxpkg`.

```text
package/
  inx_package.json
  editor/infernux_linux/
  plugin_pages/
```

Maintainers build the engine's `linux-clang-player` preset, which publishes the Player directly into this repository. Pushing a matching `v<version>` tag makes GitHub Actions build and publish the plugin and release manifest.

## License

[MIT](LICENSE). Bundled third-party components retain their own licenses.

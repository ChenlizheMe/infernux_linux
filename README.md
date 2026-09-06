# Infernux Linux Platform

[简体中文](README.zh-CN.md) · [Releases](https://github.com/ChenlizheMe/infernux_linux/releases) · [Infernux](https://github.com/ChenlizheMe/Infernux)

![Linux build workflow](package/plugin_pages/media/overview.png)

Build Linux x64 Players using the precompiled Player, CPython runtime and optional parallel module shipped in this plugin. Ordinary exports assemble these files with cooked project content; no engine checkout, CMake, or compiler SDK is required.

## At a glance

| Item | Value |
| --- | --- |
| Package | `infernux/platform-linux` |
| Plugin version | 0.2.0 |
| Engine compatibility | ==0.4.0 |
| Target | `linux-x64` |
| Build host | Linux x64 |
| Rendering | Native Player / Vulkan |

## Install

1. Open your project in Infernux 0.4.0 and open the Plugins panel.
2. Select Infernux Linux Platform in the official list, then import and enable it.
3. Open the build settings and select the target. Resolve the reported prerequisites before exporting.

If your editor's bundled catalog predates this repository, add `https://github.com/ChenlizheMe/infernux_linux` as a GitHub plugin source, or import `infernux.platform-linux.inxpkg` from [Releases](https://github.com/ChenlizheMe/infernux_linux/releases/latest). GitHub's automatic source ZIP is the author repository, not the installable plugin artifact.

## Requirements

Infernux 0.4.0 for Linux x64 with Python 3.13. This plugin owns the matching precompiled Player payload. Running the game requires a working Vulkan driver and the platform libraries required by the engine.

## Host boundary

Linux builds Linux. This package does not cross-compile a Linux Player from Windows. Disabling or uninstalling it removes its target without changing the shared build service.

## Output and troubleshooting

Distribute the complete game directory: native executable, runtime libraries and packaged content. Preserve the executable permission when transferring the Player. Cooked game content uses the engine's binary package rather than exposing the editable Assets/Library directory tree; this is not DRM.

If the target is absent, confirm that the editor host is Linux x64 and the package is enabled. Missing or incompatible Player files require explicitly installing a compatible complete platform release through the plugin's Versions tab. For a Player launch failure, check executable permissions, Vulkan availability and the reported missing system libraries.

## Develop and package

Only `package/` becomes the InxPackage payload. The outer README, SVG illustration sources, release automation and build scripts remain repository files. In-editor documentation is separate, under `package/plugin_pages/`.

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

Run `python package.py dist/infernux.platform-linux.inxpkg` to package locally. This standalone script uses only Python's standard library and does not require an engine installation. Build outside package/, then place the files to ship inside package/ before packaging.

Maintainers build the engine's `linux-clang-player` CMake preset. It produces the payload directly in this repository's `package/editor/infernux_linux/player/` and the final `.inxpkg` plus release manifest in `dist/`. Release CI builds this exact plugin revision with the matching engine release line on a Linux host. There is no intermediate runtime ZIP or separate archive-transfer channel.

Maintainers run `python release.py v0.2.0` to create the archive and its release manifest. Pushing a matching version tag publishes both files through GitHub Actions. The editor uses that manifest to select a compatible release.

## License

[MIT](LICENSE). Third-party SDKs and the engine runtime keep their own licenses; they are not relicensed by this plugin.

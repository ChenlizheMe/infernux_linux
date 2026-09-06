# Infernux Linux Platform

[简体中文](README.zh-CN.md) · [Releases](https://github.com/ChenlizheMe/infernux_linux/releases) · [Infernux](https://github.com/ChenlizheMe/Infernux)

![Linux build workflow](package/plugin_pages/media/overview.png)

Build Linux x64 Players using the native runtime shipped with the Linux engine wheel. This package registers the Linux exporter and delegates shared cooking and packaging to the engine.

## At a glance

| Item | Value |
| --- | --- |
| Package | `infernux/platform-linux` |
| Plugin version | 0.1.0 |
| Engine compatibility | >=0.4.0,<0.5 |
| Target | `linux-x64` |
| Build host | Linux x64 |
| Rendering | Native Player / Vulkan |

## Install

1. Open your project in Infernux 0.4.0 and open the Plugins panel.
2. Select Infernux Linux Platform in the official list, then import and enable it.
3. Open the build settings and select the target. Resolve the reported prerequisites before exporting.

If your editor's bundled catalog predates this repository, add `https://github.com/ChenlizheMe/infernux_linux` as a GitHub plugin source, or import `infernux.platform-linux.inxpkg` from [Releases](https://github.com/ChenlizheMe/infernux_linux/releases/latest). GitHub's automatic source ZIP is the author repository, not the installable plugin artifact.

## Requirements

A Linux x64 installation of Infernux 0.4.0 with its native Player and Python 3.13 runtime pack. Running the game requires a working Vulkan driver and the platform libraries required by the engine.

## Host boundary

Linux builds Linux. This package does not cross-compile a Linux Player from Windows. Disabling or uninstalling it removes its target without changing the shared build service.

## Output and troubleshooting

Distribute the complete game directory: native executable, runtime libraries and packaged content. Preserve the executable permission when transferring the Player. Cooked game content uses the engine's binary package rather than exposing the editable Assets/Library directory tree; this is not DRM.

If the target is absent, confirm that the editor host is Linux x64 and the package is enabled. Missing native runtime files require repairing the engine installation. For a Player launch failure, check executable permissions, Vulkan availability and the reported missing system libraries.

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

Maintainers run `python release.py v0.1.0` to create the archive and its release manifest. Pushing a matching version tag publishes both files through GitHub Actions. The editor uses that manifest to select a compatible release.

## License

[MIT](LICENSE). Third-party SDKs and the engine runtime keep their own licenses; they are not relicensed by this plugin.

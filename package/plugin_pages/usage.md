# Linux Platform

![Build workflow](media/overview.png)

Build Linux x64 Players using the native runtime shipped with the Linux engine wheel. This package registers the Linux exporter and delegates shared cooking and packaging to the engine.

## Before building

A Linux x64 installation of Infernux 0.4.0 with its native Player and Python 3.13 runtime pack. Running the game requires a working Vulkan driver and the platform libraries required by the engine.

## Host boundary

Linux builds Linux. This package does not cross-compile a Linux Player from Windows. Disabling or uninstalling it removes its target without changing the shared build service.

## Output and troubleshooting

Distribute the complete game directory: native executable, runtime libraries and packaged content. Preserve the executable permission when transferring the Player. Cooked game content uses the engine's binary package rather than exposing the editable Assets/Library directory tree; this is not DRM.

If the target is absent, confirm that the editor host is Linux x64 and the package is enabled. Missing native runtime files require repairing the engine installation. For a Player launch failure, check executable permissions, Vulkan availability and the reported missing system libraries.

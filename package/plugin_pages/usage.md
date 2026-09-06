# Linux Platform

![Build workflow](media/overview.png)

Build Linux x64 Players using the precompiled Player, CPython runtime and optional parallel module shipped in this plugin. Ordinary exports assemble these files with cooked project content; no engine checkout, CMake, or compiler SDK is required.

## Before building

Infernux 0.4.0 for Linux x64 with Python 3.13. This plugin owns the matching precompiled Player payload. Running the game requires a working Vulkan driver and the platform libraries required by the engine.

## Host boundary

Linux builds Linux. This package does not cross-compile a Linux Player from Windows. Disabling or uninstalling it removes its target without changing the shared build service.

## Output and troubleshooting

Distribute the complete game directory: native executable, runtime libraries and packaged content. Preserve the executable permission when transferring the Player. Cooked game content uses the engine's binary package rather than exposing the editable Assets/Library directory tree; this is not DRM.

If the target is absent, confirm that the editor host is Linux x64 and the package is enabled. Missing or incompatible Player files require explicitly installing a compatible complete platform release through the plugin's Versions tab. For a Player launch failure, check executable permissions, Vulkan availability and the reported missing system libraries.

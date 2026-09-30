"""Linux x64 Player exporter."""

from __future__ import annotations

import sys
from pathlib import Path

from Infernux.engine.build.contracts import (
    BuildOption,
    BuildOptionChoice,
    BuildOptionKind,
    BuildTarget,
    PlatformExporter,
)
from Infernux.engine.build.host_player_export import (
    HOST_PLAYER_CAPABILITIES,
    create_host_player_plan,
    execute_host_player_build,
    host_machine_is_x64,
    inspect_host_player_request,
)


def linux_target() -> BuildTarget | None:
    if not sys.platform.startswith("linux") or not host_machine_is_x64():
        return None
    return BuildTarget(
        "linux-x64",
        "Linux x64",
        "linux",
        "x86_64",
        HOST_PLAYER_CAPABILITIES,
    )


class LinuxPlatformExporter(PlatformExporter):
    @property
    def exporter_id(self) -> str:
        return "infernux/platform-linux"

    def targets(self):
        target = linux_target()
        return (target,) if target is not None else ()

    def build_options(self, target):
        if target.id != "linux-x64":
            raise ValueError(f"Unsupported Linux build target: {target.id}")
        return (
            BuildOption(
                "display_mode", "build.display_mode", BuildOptionKind.ENUM,
                "fullscreen_borderless",
                choices=(
                    BuildOptionChoice("fullscreen_borderless", "build.fullscreen_borderless"),
                    BuildOptionChoice("windowed", "build.windowed"),
                ),
            ),
            BuildOption(
                "window_width", "build.width", BuildOptionKind.INTEGER, 1280,
                minimum=320, maximum=7680,
                visible_when={"display_mode": "windowed"},
            ),
            BuildOption(
                "window_height", "build.height", BuildOptionKind.INTEGER, 720,
                minimum=240, maximum=4320,
                visible_when={"display_mode": "windowed"},
            ),
            BuildOption(
                "window_resizable", "build.window_resizable",
                BuildOptionKind.BOOLEAN, True,
                visible_when={"display_mode": "windowed"},
            ),
        )

    def doctor(self, request):
        return inspect_host_player_request(
            request,
            linux_target(),
            exporter_id=self.exporter_id,
            player_runtime_root=str(Path(__file__).parent / "player"),
        )

    def create_plan(self, request):
        return create_host_player_plan(request)

    def execute(self, request, plan):
        return execute_host_player_build(
            request, plan, player_runtime_root=str(Path(__file__).parent / "player"),
        )


__all__ = ["LinuxPlatformExporter", "linux_target"]

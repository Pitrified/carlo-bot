"""CarloBot project configuration."""

from loguru import logger as lg

from carlo_bot.config.carlo_bot_paths import CarloBotPaths
from carlo_bot.config.singleton import Singleton


class CarloBotConfig(metaclass=Singleton):
    """CarloBot project configuration."""

    def __init__(self) -> None:
        lg.info(f"Loading CarloBot config")
        self.paths = CarloBotPaths()

    def __str__(self) -> str:
        s = "CarloBotConfig:"
        s += f"\n{self.paths}"
        return s

    def __repr__(self) -> str:
        return str(self)


def get_carlo_bot_config() -> CarloBotConfig:
    """Get the carlo_bot config."""
    return CarloBotConfig()


def get_carlo_bot_paths() -> CarloBotPaths:
    """Get the carlo_bot paths."""
    return get_carlo_bot_config().paths

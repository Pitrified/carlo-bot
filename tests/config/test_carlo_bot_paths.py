"""Test the carlo_bot paths."""

import pytest

from carlo_bot.config.carlo_bot_config import get_carlo_bot_paths


def test_carlo_bot_paths() -> None:
    """Test the carlo_bot paths."""
    carlo_bot_paths = get_carlo_bot_paths()
    assert carlo_bot_paths.src_fol.name == "carlo_bot"
    assert carlo_bot_paths.root_fol.name == "carlo_bot"
    assert carlo_bot_paths.data_fol.name == "data"

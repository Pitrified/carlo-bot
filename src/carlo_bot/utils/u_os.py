"""Utils for OS operations."""

import os
from typing import Optional

from loguru import logger as lg


def get_env_var(env_var: str, default: str | None = None) -> str:
    """Get an environment variable."""
    value = os.getenv(env_var, default)
    if value is None:
        msg = f"Environment variable {env_var} is not set"
        msg += f" and no default value provided"
        lg.error(msg)
        raise ValueError(msg)
    return value

"""Load the X configuration."""

from loguru import logger as lg

from carlo_bot.utils.u_os import get_env_var


class XConfig:
    """X configuration."""

    def __init__(self) -> None:
        lg.info(f"Loading X config")
        self.load_tokens()

    def load_tokens(self) -> None:
        """Load tokens."""
        self.bearer_token = get_env_var("X_BEARER_TOKEN")
        self.consumer_api_key = get_env_var("X_CONSUMER_API_KEY")
        self.consumer_api_key_secret = get_env_var("X_CONSUMER_API_KEY_SECRET")
        self.access_token_pyn = get_env_var("X_ACCESS_TOKEN_PYN")
        self.access_token_secret_pyn = get_env_var("X_ACCESS_TOKEN_SECRET_PYN")

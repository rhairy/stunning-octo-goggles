"""Data module for The Room dialogue quotes."""
from room_api.data.quotes import (
    QUOTES,
    get_all_quotes,
    get_quote_by_slug,
    get_quotes_by_character,
    get_random_quote,
    search_quotes,
    get_characters,
)

__all__ = [
    "QUOTES",
    "get_all_quotes",
    "get_quote_by_slug",
    "get_quotes_by_character",
    "get_random_quote",
    "search_quotes",
    "get_characters",
]

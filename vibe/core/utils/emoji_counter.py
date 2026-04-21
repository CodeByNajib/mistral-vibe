from __future__ import annotations

ASCII_MAX = 127


def count_emojis(text: str) -> int:
    """Count the number of emojis in a string."""
    return sum(1 for char in text if ord(char) > ASCII_MAX)

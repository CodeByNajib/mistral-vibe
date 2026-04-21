from __future__ import annotations

from vibe.core.utils.emoji_counter import count_emojis


def test_count_emojis_with_emojis():
    assert count_emojis("Hello 😊 world 🚀 ") == 2


def test_count_emojis_without_emojis():
    assert count_emojis("No emojis here") == 0


def test_count_emojis_only_emojis():
    assert count_emojis("🔥🔥🔥") == 3


def test_count_emojis_empty_string():
    assert count_emojis("") == 0

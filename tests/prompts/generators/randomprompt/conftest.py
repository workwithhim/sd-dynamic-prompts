import random

import pytest

from pathlib import Path
from prompts.generators.randomprompt import RandomPromptGenerator
from prompts.wildcardmanager import WildcardManager


@pytest.fixture
def wildcard_manager() -> WildcardManager:
    return WildcardManager(Path("test_data/wildcards"))


@pytest.fixture
def seed() -> int:
    s = 0
    random.seed(s)

    return s


@pytest.fixture
def generator(wildcard_manager: WildcardManager, seed: int) -> RandomPromptGenerator:
    return RandomPromptGenerator(
        wildcard_manager, "A template", seed=seed, unlink_seed_from_prompt=False
    )

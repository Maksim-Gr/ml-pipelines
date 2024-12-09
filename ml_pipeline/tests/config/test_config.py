import pathlib

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    import pytest


from omegaconf import DictConfig, OmegaConf

from ml_pipeline.config import Config


def get_config(config_type: "pathlib.Path") -> DictConfig:
    common_config_str = """
        common_item_a: a
    """

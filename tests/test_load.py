from typing import Any, Dict

from homeassistant.components.blueprint import models
from homeassistant.util import yaml

from . import BLUEPRINT


def test_validation():
    data: Dict[Any, Any] = yaml.load_yaml(BLUEPRINT)  # type: ignore
    assert models.Blueprint(data, expected_domain="automation").validate() is None

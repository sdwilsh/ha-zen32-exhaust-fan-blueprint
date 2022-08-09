import os
from typing import Any, Dict

from homeassistant.components.blueprint import models
from homeassistant.util import yaml

BLUEPRINT = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "zen32_exhaust_fan.yaml"
)


def test_validation():
    data: Dict[Any, Any] = yaml.load_yaml(BLUEPRINT)  # type: ignore
    assert models.Blueprint(data, expected_domain="automation").validate() is None

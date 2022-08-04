from __future__ import annotations
from typing import Any, Dict

from extractor.base import NotExists  # noqa
from extractor.field import ArrayField, Field, FloatField, IntegerField, MappingField, NestedField, StringField  # noqa
from extractor.manager import ModelManager  # noqa
from extractor.simple import SimpleExtractor

_VALIDATE_FUNCTION = "validate"
SimpleDictModel = SimpleExtractor


class ObjectDict(Dict[str, Any]):
    """Makes a dictionary behave like an object, with attribute-style access."""

    def __getattr__(self, name: str) -> Any:
        try:
            v = self[name]
            if isinstance(v, dict):
                return ObjectDict(v)
            return v
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name: str, value: Any) -> None:
        self[name] = value

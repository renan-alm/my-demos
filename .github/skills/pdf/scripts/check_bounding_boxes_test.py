"""Tests for bounding box detection."""
import pytest
from check_bounding_boxes import get_bounding_boxes


def test_get_bounding_boxes_returns_list():
    """Verify bounding boxes are returned as a list."""
    result = get_bounding_boxes("sample.pdf")
    assert isinstance(result, list)

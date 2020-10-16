import pytest
from src.nfr_badge import Checklist

def test__checklist__get_name_from_fname__should_return_name():
    # Arrange
    fname = "/one/two/three/four.md"
    # Act
    name = Checklist.get_name_from_fname(fname)
    # Assert
    assert name == 'four'

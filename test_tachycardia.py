import pytest
from tachycardia import is_tachycardic


@pytest.mark.parametrize("stringToCheck, expected", [
                        ("tachycardic", True),
                        ("tachycardiC", True),
                        ("TachycardiC", True),
                        ("TACHYCARDIC", True),
                        ("tachycardiC", True),
                        (" tachycardic", True),
                        ("tachycardic ", True),
                        ("tachycardic!!!", True),
                        ("!!!tachycardic ", True),
                        ("!!!tachycardic!!!", True),
                        ("tachycardic3", True),
                        ("3tachycardic", True),
                        ("Ztachycardic", True),
                        ("tachycardicZ", True),
                        ("tachy3cardic", False),
                        ("tachyZcardic", False),
                        ("3achycardic", False),
                        ("tachycardi3", False),
                        ("tachy cardic", False),
                        ])
def test_is_tachycardic(stringToCheck, expected):
    result = is_tachycardic(stringToCheck)
    assert result is expected

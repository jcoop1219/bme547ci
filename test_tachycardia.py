def test_is_tachycardic():
    from tachycardia import is_tachycardic

    stringToCheck = "tachycardic"
    result = is_tachycardic(stringToCheck)

    assert result is True

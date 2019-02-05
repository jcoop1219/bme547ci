def test_is_tachycardic():
    from tachycardia import is_tachycardic

    result = is_tachycardic("134dwqtachycardic13445")
    assert result == True

import pytest
from tachycardia import is_tachycardic


# Test case of uppercase entry
@pytest.mark.parametrize("stringToCheck, expected", [
                        ("tachycardic", True),
                        ("tachycardiC", True),
                        ("TachycardiC", True),
                        ("TACHYCARDIC", True),
                        ("tachycardiC", True),
                        ])
def test_uppercase_is_tachycardic(stringToCheck, expected):
    result = is_tachycardic(stringToCheck)
    assert result is expected


# Test case of leading/trailing punctuation, spaces, or numbers
@pytest.mark.parametrize("stringToCheck, expected", [
                        (" tachycardic", True),
                        ("tachycardic ", True),
                        (" tachycardic ", True),
                        ("tachycardic!!!", True),
                        ("!!!tachycardic", True),
                        (" tachycardic!!!", True),
                        ("!!!tachycardic ", True),
                        ("!!!tachycardic!!!", True),
                        ("tachycardic3", True),
                        ("3tachycardic", True),
                        ])
def test_leadTrail_is_tachycardic(stringToCheck, expected):
    result = is_tachycardic(stringToCheck)
    assert result is expected


# Test case of one letter missing
@pytest.mark.parametrize("stringToCheck, expected", [
                        ("achycardic", True),
                        ("tchycardic", True),
                        ("tahycardic", True),
                        ("tacycardic", True),
                        ("tachcardic", True),
                        ("tachyardic", True),
                        ("tachycrdic", True),
                        ("tachycadic", True),
                        ("tachycaric", True),
                        ("tachycardc", True),
                        ("tachycardi", True),
                        ])
def test_missingOneLetter_is_tachycardic(stringToCheck, expected):
    result = is_tachycardic(stringToCheck)
    assert result is expected


# Test case of two letters missing
@pytest.mark.parametrize("stringToCheck, expected", [
                        ("chycardic", True),
                        ("ahycardic", True),
                        ("acycardic", True),
                        ("achcardic", True),
                        ("achyardic", True),
                        ("achycrdic", True),
                        ("achycadic", True),
                        ("achycaric", True),
                        ("achycardc", True),
                        ("achycardi", True),
                        ("thycardic", True),
                        ("tcycardic", True),
                        ("tchcardic", True),
                        ("tchyardic", True),
                        ("tchycrdic", True),
                        ("tchycadic", True),
                        ("tchycaric", True),
                        ("tchycardc", True),
                        ("tchycardi", True),
                        ("taycardic", True),
                        ("tahcardic", True),
                        ("tahyardic", True),
                        ("tahycrdic", True),
                        ("tahycadic", True),
                        ("tahycaric", True),
                        ("tahycardc", True),
                        ("tahycardi", True),
                        ("taccardic", True),
                        ("tacyardic", True),
                        ("tacycrdic", True),
                        ("tacycadic", True),
                        ("tacycaric", True),
                        ("tacycardc", True),
                        ("tacycardi", True),
                        ("tachardic", True),
                        ("tachcrdic", True),
                        ("tachcadic", True),
                        ("tachcaric", True),
                        ("tachcardc", True),
                        ("tachcardi", True),
                        ("tachyrdic", True),
                        ("tachyadic", True),
                        ("tachyaric", True),
                        ("tachyardc", True),
                        ("tachyardi", True),
                        ("tachycdic", True),
                        ("tachycric", True),
                        ("tachycrdc", True),
                        ("tachycrdi", True),
                        ("tachycaic", True),
                        ("tachycadc", True),
                        ("tachycadi", True),
                        ("tachycarc", True),
                        ("tachycari", True),
                        ("tachycard", True),
                        ])
def test_missingTwoLetters_is_tachycardic(stringToCheck, expected):
    result = is_tachycardic(stringToCheck)
    assert result is expected


# Test case of three letters missing
@pytest.mark.parametrize("stringToCheck, expected", [
                        ("hycardic", False),
                        ("achcaric", False),
                        ("tachycar", False),
                        ("chycardi", False),
                        ("achycard", False),
                        ("tacardic", False),
                        ("tacycaic", False),
                        ])
def test_missingThreeLetters_is_tachycardic(stringToCheck, expected):
    result = is_tachycardic(stringToCheck)
    assert result is expected


# Test case of one letter added
@pytest.mark.parametrize("stringToCheck, expected", [
                        ("tachyacardic", True),
                        ("atachycardic", True),
                        ("tachycardica", True),
                        ])
def test_addedOneLetter_is_tachycardic(stringToCheck, expected):
    result = is_tachycardic(stringToCheck)
    assert result is expected


# Test case of two letters added
@pytest.mark.parametrize("stringToCheck, expected", [
                        ("taatchycardic", True),
                        ("tacahycatrdic", True),
                        ("atachycardict", True),
                        ("ttachycardica", True),
                        ("ttachycardicc", True),
                        ("ctachycardict", True),
                        ("tachycaatrdic", True),
                        ])
def test_addedTwoLetters_is_tachycardic(stringToCheck, expected):
    result = is_tachycardic(stringToCheck)
    assert result is expected


# Test case of three letters added
@pytest.mark.parametrize("stringToCheck, expected", [
                        ("tachyatccardic", False),
                        ("ttaacchycardic", False),
                        ("atachycatrdicc", False),
                        ("ttachycaardicc", False),
                        ])
def test_addedThreeLetters_is_tachycardic(stringToCheck, expected):
    result = is_tachycardic(stringToCheck)
    assert result is expected


# Test case of one letter substituted
@pytest.mark.parametrize("stringToCheck, expected", [
                        ("tachycsrdic", True),
                        ("tacGycardic", True),
                        ("tachycardoc", True),
                        ("tachycardiV", True),
                        ("zachycardic", True),
                        ])
def test_subOneLetter_is_tachycardic(stringToCheck, expected):
    result = is_tachycardic(stringToCheck)
    assert result is expected


# Test case of two letters substituted
@pytest.mark.parametrize("stringToCheck, expected", [
                        ("taxhycSrdic", True),
                        ("zachycareic", True),
                        ("tavhycardin", True),
                        ("zachycardin", True),
                        ])
def test_subTwoLetters_is_tachycardic(stringToCheck, expected):
    result = is_tachycardic(stringToCheck)
    assert result is expected


# Test case of three letters substituted
@pytest.mark.parametrize("stringToCheck, expected", [
                        ("tavhucabdic", False),
                        ("tschycbrdoc", False),
                        ("zaccycbrdic", False),
                        ("taxhyxardiv", False),
                        ("zachyxardiv", False),
                        ])
def test_subThreeLetters_is_tachycardic(stringToCheck, expected):
    result = is_tachycardic(stringToCheck)
    assert result is expected

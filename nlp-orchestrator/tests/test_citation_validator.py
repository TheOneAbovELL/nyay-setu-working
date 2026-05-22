from validators.citation_validator import validate_citation


def test_valid_bns_section_302():
    result = validate_citation("BNS", "302")
    assert result["valid"] is True
    assert result["message"] == "Valid legal citation"


def test_valid_bns_section_350():
    result = validate_citation("BNS", "350")
    assert result["valid"] is True


def test_valid_bnss_section_482():
    result = validate_citation("BNSS", "482")
    assert result["valid"] is True


def test_valid_bnss_section_531():
    result = validate_citation("BNSS", "531")
    assert result["valid"] is True


def test_invalid_bns_section_999():
    result = validate_citation("BNS", "999")
    assert result["valid"] is False


def test_invalid_bnss_section_999():
    result = validate_citation("BNSS", "999")
    assert result["valid"] is False


def test_existing_lower_section_bns_10():
    result = validate_citation("BNS", "10")
    assert result["valid"] is True


def test_existing_lower_section_bnss_50():
    result = validate_citation("BNSS", "50")
    assert result["valid"] is True

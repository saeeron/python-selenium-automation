import pytest


def abbrev_name(name: str) -> str:
    return ".".join(name_[0].upper() for name_ in name.split(" "))


@pytest.mark.parametrize("input_names, expected_results", [
    ("Sam Harris", "S.H"),
    ("Nick SIMONS", "N.S"),
    ("Bob Anderson", "B.A"),
    ("RODIN zaNetti", "R.Z") ])
def test_abbrev_name(input_names: str, expected_results: str) -> None:
    actual_name = abbrev_name(input_names)
    assert actual_name == expected_results, f"Expected {expected_results} but got {actual_name}!"

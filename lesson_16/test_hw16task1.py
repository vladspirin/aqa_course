"""
Check for the presence of attributes.

Attributes from the Manager and Developer
must be present in the TeamLead class.
"""

import hw16task1 as ca


def test_attr_match():
    """Test to verify that all attributes from parent classes are present."""
    keys1 = set(ca.Developer('Manoj', 4000, 'Java').__dict__.keys())
    keys2 = set(ca.Manager('Ana', 10000, 'R&D').__dict__.keys())
    keys3 = set(ca.TeamLead('Shradha', 7000, 'R&D', 5).__dict__.keys())
    combined_keys = keys1 | keys2
    assert combined_keys <= keys3, 'TL contains attributes not in MNG or Dev'

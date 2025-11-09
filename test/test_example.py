import pytest

@pytest.mark.first
def test_first():
    assert 'Hello' in 'Hello World'

@pytest.mark.second
def test_second():
    assert len('Hello') == 5

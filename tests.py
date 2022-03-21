import pytest
from testbook import testbook


# Set up a shared notebook context to speed up tests.
@pytest.fixture(scope='module')
def tb():
    with testbook('Webinar.ipynb', execute=True) as tb:
        yield tb


@pytest.mark.parametrize(
    "input_value, expected", 
    [
        (10, 1000),
        (2, 8),
        (3, 27),
    ]
)
def test_cubed(tb, input_value, expected):
    # Retrieve a reference to the function definiton in the notebook
    cubed = tb.ref("cubed")
    assert cubed(input_value) == expected
    
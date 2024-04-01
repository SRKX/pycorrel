import pytest
from src.correl import CorrelationMatrix

def query_non_existing_same():

    rho = CorrelationMatrix()
    x = rho[ "A", "A" ]

def test_answer():

    with pytest.raises( IndexError ):
        query_non_existing_same()
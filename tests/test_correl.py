import pytest
from src.correl import CorrelationMatrix


def test_non_existing_same_key():

    rho = CorrelationMatrix()
    with pytest.raises( IndexError ):
        #Should not be allowd
        x = rho[ "A", "A" ]
        
    rho[ "A", "A" ] = 1.0
    
    pass

def test_set_key_pair():
    
    rho = CorrelationMatrix()
    
    val = 0.5   
    
    rho[ "A", "B" ] = 0.5
    
    assert rho[ "B", "A" ] == val
    
    val2 = -0.2
    
    rho[ "B", "A" ] = val2
    
    assert rho[ "A", "B" ] == val2


def test_set_key_pair_invalid():
    
    rho = CorrelationMatrix()
    
    with pytest.raises( ValueError ):
        rho[ "A", "B" ] = 1.1
        
    with pytest.raises( ValueError ):
        rho[ "A", "B" ] = -1.1
    
    
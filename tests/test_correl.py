import pytest
from src.symmetric_matrix import SymmetricMatrix
from src.correl import CorrelationMatrix


    

def test_set_key_pair():
    """Tests Assignments of correlation and symmetric properties"""
    rho = CorrelationMatrix()
    
    val = 0.5   
    
    rho[ "A", "B" ] = 0.5
    
    assert rho[ "B", "A" ] == val
    
    val2 = -0.2
    
    rho[ "B", "A" ] = val2
    
    assert rho[ "A", "B" ] == val2


def test_set_key_pair_invalid_value():
    """Ensure correlation matrices cannot have values > 1 or < -1"""
    rho = CorrelationMatrix()
    
    with pytest.raises( ValueError ):
        rho[ "A", "B" ] = 1.1
        
    with pytest.raises( ValueError ):
        rho[ "A", "B" ] = -1.1
    
import pytest


def test_initialization():
    # Test if the matrix is initialized with the correct keys
    matrix = SymmetricMatrix(keys=['a', 'b', 'c'])
    assert set(matrix.keys) == {'a', 'b', 'c'}

def test_set_and_get_item():
    # Test setting and getting an item in the matrix
    matrix = SymmetricMatrix()
    matrix['a', 'b'] = 0.5
    assert matrix['a', 'b'] == 0.5
    # Test if the matrix is symmetric
    assert matrix['b', 'a'] == 0.5

def test_set_and_get_item_initialized():
    # Test setting and getting an item in the matrix
    matrix = SymmetricMatrix(keys=['a','b'])
    #The value is not yet set
    assert ('a','b') not in matrix
    assert ('b','a') not in matrix
    
    #We set the value
    matrix['a', 'b'] = 0.5
    
    #The value is now set
    assert ('a','b') in matrix
    assert ('b','a') in matrix
    
    
    assert matrix['a', 'b'] == 0.5
    # Test if the matrix is symmetric
    assert matrix['b', 'a'] == 0.5

def test_key_error():
    # Test if an IndexError is raised when trying to access a non-existent key
    matrix = SymmetricMatrix()
    with pytest.raises(IndexError):
        matrix['a', 'b']

def test_key_type_error():
    # Test if a TypeError is raised when the key is not a 2-tuple
    matrix = SymmetricMatrix()
    with pytest.raises(TypeError):
        matrix['a'] = 0.5
    with pytest.raises(TypeError):
        matrix[('a', 'b', 'c')] = 0.5

def test_value_type_error():
    # Test if a TypeError is raised when the value is not a float
    matrix = SymmetricMatrix()
    with pytest.raises(TypeError):
        matrix['a', 'b'] = 'not a float'
        

def test_frozen_keys():
    # Test if keys are frozen and cannot be added after initialization
    matrix = SymmetricMatrix(keys=['a', 'b'], frozen_keys=True)
    with pytest.raises(IndexError):
        matrix['a', 'c'] = 0.5
    assert 'a' in matrix.keys
    assert 'c' not in matrix.keys

def test_contains():
    # Test if the __contains__ method works correctly
    matrix = SymmetricMatrix()
    matrix['a', 'b'] = 0.5
    assert ('a', 'b') in matrix
    assert ('b', 'a') in matrix
    assert ('a', 'c') not in matrix



def test_non_existing_same_key():

    rho = CorrelationMatrix()
    with pytest.raises( IndexError ):
        #Should not be allowd
        x = rho[ "A", "A" ]
    
    #Should work 
    rho[ "A", "A" ] = 1.0
    
    val = rho[ "A", "A" ]
    assert val == 1.0
    
def test_existing_same_key():

    rho = CorrelationMatrix(keys=['a','b'])
    
    assert ('a', 'a') in rho
    assert ('b', 'b') in rho
    assert ('a', 'b') not in rho
    
    
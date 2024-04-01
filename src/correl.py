from symmetric_matrix import SymmetricMatrix

class CorrelationMatrix( SymmetricMatrix ):
    
    def __init__( self, keys = None, frozen_keys = False ):
        
        super().__init__( keys, frozen_keys )
    
    def __getitem__( self, key ) -> float:
       
        if self._check_key_type( key ):

            #We get the two keys requested
            key1, key2 = key

            if key1 == key2:
                #We have the same key
                if key1 in self.keys:
                    #The key exists
                    return 1
                else:
                    #The key does not exists
                    raise IndexError( f"Key '{key1}' does not exist in the matrix" )
            else:
                return super().__getitem__( key )

        else:
            raise TypeError( f"Correlation keys should be expressed as 2-tuple, provided {type(key)}")


    def __setitem__( self, key, value:float ) -> None:

        if not self._check_key_type( key ):
            raise TypeError( f"Correlation keys should be expressed as 2-tuple, provided {type(key)}")
        else:
            key1, key2 = key
            if key1 == key2 and value != 1:
                raise ValueError( "Correlation between an two identical keys should only be 1" )
            else:
                super().__setitem__( key, value )


def test():
    rho = CorrelationMatrix()
    rho[ "A", "B"] = 0.5
    print( rho[ "A", "B" ] )
    print( rho[ "B", "A" ] )


if __name__ == "__main__":
    test()
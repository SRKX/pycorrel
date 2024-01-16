
class CorrelationMatrix:
    
    def __init__( self, keys = None, frozen_keys = False ):
        
        #The keys of the correlation matrix are stored in a set
        self.__keys = set( key for key in keys ) if keys is not None else None

        #Determines whether the keys should be frozen or not
        self.__frozen_keys = frozen_keys


        #TODO Handle values initializer
        self.__values = {}

    @property
    def keys( self ):
        #We return a copy of the keys
        return self.__keys.copy()


    @staticmethod
    def __check_key_type( key ) -> bool:
        return isinstance( key, tuple ) and len( key ) == 2
        
    def __keys_exist( self, key1, key2 ) -> bool:
        return key1 in self.__keys and key2 in self.__keys

    def __initiate_key( self, key ) -> None:

        for k in self.__keys:
            self.__values[ ( k, key ) ] = None

    def __getitem__( self, key ) -> float:
       
        if self.__check_key_type( key ):

            #We get the two keys requested
            key1, key2 = key

            return self.get_correl( key1, key2 ) #Note: we could also write self.get_correl( *key )
        else:
            raise TypeError( f"Correlation keys should be expressed as 2-tuple, provided {type(key)}")

    def __setitem__( self, key, value ) -> None:

        if not self.__check_key_type( key ):
            raise TypeError( f"Correlation keys should be expressed as 2-tuple, provided {type(key)}")

        key1, key2 = key

        if self.__keys_exist( *key ):
            the_key = self.get_values_key( key1, key2 )
            self.__values[ the_key ] = value 

        elif not self.__frozen_keys:
            

            if key1 not in self.__keys:
                self.__initiate_key( key1 )

            if key2 not in self.__keys:
                self.__initiate_key( key2 )

            the_key = self.get_values_key( key1, key2 )
            self.__values[ the_key ] = value 
            


    def __contains__( self, key1, key2 ) -> bool:
        return ( key1, key2 ) in self.__values or ( key2, key1 ) in self.__values

    def get_values_key( self, key1, key2 ) :

        if ( key1, key2 ) in self.__values:
            return ( key1, key2 )
        elif ( key2, key1 ) in self.__values:
            return ( key2, key1 )
        else:
            raise IndexError( ( key1, key2 ) )

    def get_correl( self, key1, key2 ) -> float:
        
        try:
            the_key = self.get_values_key( ( key1, key2 ) )
            return self.__values[ the_key ]
        except:
            #We did not find the key
            raise
#Define a custom exception class which takes a
#string message as attribute.

class myError(Exception):
    '''My own exception class

    Attributes:
        msg -- explanation of error
    '''
    
    def __init__(self, msg):
        self.msg = msg
        
error = myError("something wrong")
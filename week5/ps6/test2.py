class PlaintextMessage(Message):
    def __init__(self, text, shift):
    '''
    Initializes a PlaintextMessage object        
    
    text (string): the message's text
    shift (integer): the shift associated with this message

    A PlaintextMessage object inherits from Message and has five attributes:
        self.message_text (string, determined by input text)
        self.valid_words (list, determined using helper function load_words)
        self.shift (integer, determined by input shift)
        self.encrypting_dict (dictionary, built using shift)
        self.message_text_encrypted (string, created using shift)

    Hint: consider using the parent class constructor so less 
    code is repeated
    '''
        super(PlaintextMessage, self).__init__()
        self.shift=shift
        self.encrypting_dict=build_shift_dict(shift)
        self.message_text_encrypted(shift)
    

    def get_shift(self):
    '''
    Used to safely access self.shift outside of the class
    
    Returns: self.shift
    '''
        return self.shift 

    def get_encrypting_dict(self):
    '''
    Used to safely access a copy self.encrypting_dict outside of the class
    
    Returns: a COPY of self.encrypting_dict
    '''
        from copy import deepcopy
        copy=deepcopy(self.encrypting_dict())
        return copy

    def get_message_text_encrypted(self):
    '''
    Used to safely access self.message_text_encrypted outside of the class
    
    Returns: self.message_text_encrypted
    '''
        return self.get_message_text_encrypted 

    def change_shift(self, shift):
    '''
    Changes self.shift of the PlaintextMessage and updates other 
    attributes determined by shift (ie. self.encrypting_dict and 
    message_text_encrypted).
    
    shift (integer): the new shift that should be associated with this message.
    0 <= shift < 26

    Returns: nothing
    '''
        if shift<0 or >=26:
            raise error
        else:
            self.shift=shift


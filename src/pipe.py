'''
Created on Aug 5, 2011

@author: Japskua
@contact: japskua@gmail.com
'''

import pipes

class Pipe(object):
    '''
    @summary: This is the pipe class that can be used to create either a 
              read pipe or a write pipe. The type of the pipe is defined at 
              creation as well as the pipename for writing/reading. 
    '''
    pipe_name = None
    pipe_type = None
    pipe = None

    def __init__(self, pipe_name, pipe_type):
        '''
        @summary: Constructor for the pipe class
        @param pipe_name: The name of the pipe
        @type pipe_name: String
        @param pipe_type: The type of the pipe (read/write)
        @type pipe_type: String, either READ or WRITE
        '''
        self.pipe_name = pipe_name
        self.pipe_type = pipe_type
        
        # Create the pipe
        self.pipe = pipes.Template()
        self.filepath = "/tmp/" + self.pipe_name
        
    def Write(self, data):
        """
        @summary: The function for writing to a path
        @param data: The input data to be written to the pipe
        """
        if self.pipe_type == "WRITE":
            try:
                f = self.pipe.open(self.filepath, "w")
                f.write(data)
                f.close()
            except Exception:
                print "Error opening pipe", self.filepath
        else:
            print "Error, the pipe in question is not a write pipe"
        
    def Read(self):
        """
        @summary: The function for reading from a specified pipe
        @return: Returns the data written to the pipe
        """
        read = None
        
        if self.pipe_type == "READ":   
            try:
                read = open(self.filepath).read()
            except Exception:
                "Error reading the pipe", self.filepath
        else:
            print "Error, the pipe in question is not a read pipe"    
            
        return read
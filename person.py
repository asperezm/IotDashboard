

class user:

    def __init__(self, username, password):
        self.username = username 
        self.secret = password
        self.authenticated = True
        self.auth()
        self.get_details()
        self.get_devices()

    def auth (self):
        #this is the place where user will get authenticated
        return True

    def get_details (self):
        
        return True
    
    def get_devices(self):

        dummy = ["dummy"]
        return dummy


    def dev_info(self, deviceID):
        output=["output"]
        return output[0]
    
    def field_values(self, fieldname):
        output=["output"]
        return output[0]

    def device_values(self, fieldname, deviceID):
        output=["output"]
        return output[0]

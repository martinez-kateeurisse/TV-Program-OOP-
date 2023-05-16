#Kate Eurisse L. Martinez_BSCPE 1-5_TV-Class

#Create Class
class TV:
    #Constructs a default TV object.
    def __init__ (self, channel = 1, volume_level = 1, on = False):
        #instance variables
        self.channel = channel
        self.volume_level = volume_level
        self.on = on
 
    #Turns on this TV.
    def tv_on(self):
        self.on = True
    
    #Turns off this TV.
    def tv_off(self):
        self.on = False
    
    #Returns the channel for this TV.
    def get_channel(self):
        return str(self.channel)
    
    #Sets a new channel for this TV.
    def set_channel(self, channel):
        #If statement
        if self.channel >= 1 and channel <= 120:
            self.channel = channel
    
    #Gets the volume level for this TV.
    def get_volume(self):
        return str(self.volume_level) 
    
    #Sets a new volume level for this TV.
    def set_volume(self, volume_level):
        #If statement
        if self.volume_level >= 1 and volume_level <= 7:
            self.volume_level = volume_level
    
    #Increases the channel number by 1.
    def channel_up(self):
        #If statement
        if self.channel < 120:
            self.channel =+ 1
        else:
            self.channel = 1
    
    #Decreases the channel number by 1.
    def channel_down(self):
        #If statement
        if self.channel > 1:
            self.channel -= 1
        else:
            self.channel = 120
    
    #Increases the volume level by 1.
    def volume_up(self):
        #If statement
        if self.channel < 7:
            self.channel += 1
        else:
            self.channel = 1
    
    #Decreases the volume level by 1.
    def volume_down(self):
        #If statement
        if self.channel > 1:
            self.channel -= 1
        else:
            self.channel = 7
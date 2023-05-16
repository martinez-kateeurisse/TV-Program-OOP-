#Kate Eurisse L. Martinez_BSCPE 1-5_TV-Class

#The current channel (1 to 120) of this TV.
#The current volume level (1 to 7) of this TV.
#Indicates whether this TV is on/off.

#Create Class
class TV:
    #Constructs a default TV object.
    def __init__ (self):
        self.channel = 1
        self.volume_level = 1
        self.on = False
 
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
        #self.channel = input(int("Channel: "))
        if self.channel >= 1 and channel <= 120:
            self.channel = channel
    #Gets the volume level for this TV.
    def get_volume(self):
        return str(self.volume_level) 
    #Sets a new volume level for this TV.
    def set_volume(self, volume_level):
        #self.volume_level = input(int("Volume Level: "))
        if self.volume_level >= 1 and volume_level <= 7:
            self.volume_level = volume_level
    #Increases the channel number by 1.
    def channel_up(self):
        if self.channel < 120:
            self.channel =+ 1
        else:
            self.channel = 1
    #Decreases the channel number by 1.
    def channel_down(self):
        if self.channel > 1:
            self.channel -= 1
        else:
            self.channel = 120
    #Increases the volume level by 1.
    def volume_up(self):
        if self.channel < 7:
            self.channel += 1
        else:
            self.channel = 1
    #Decreases the volume level by 1.
    def volume_down(self):
        if self.channel > 1:
            self.channel -= 1
        else:
            self.channel = 7
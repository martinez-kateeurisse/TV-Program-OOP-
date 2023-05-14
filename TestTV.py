#Kate Eurisse L. Martinez_BSCPE 1-5_Test Driver program

#Create python files

#Import python file (Class - TV)

class TV:
    #Create Objects
    def __init__ (self, channel, volume_level, on):
        self.channel = channel
        self.volume_level = volume_level
        self.on = on

    #Create Methods
    def tv1(self):
        return "tv1's channel is" + self.channel , "and volume level is" + self.volume_level 
    def tv2(self):
        return "tv2's channel is" + self.channel , "and volume level is" + self.volume_level 
    
#Assign values
tv1 = TV(30, 3, "on")
tv2 = TV(3, 2, "on")
#Call methods

#The current channel (1 to 120) of this TV.
#The current volume level (1 to 7) of this TV.
#Indicates whether this TV is on/off.

#Constructs a default TV object.
#Turns on this TV.
#Turns off this TV.
#Returns the channel for this TV.
#Sets a new volume level for this TV.
#Increases the channel number by 1.
#Decreases the channel number by 1.
#Increases the volume level by 1.
#Decreases the volume level by 1.
#Kate Eurisse L. Martinez_BSCPE 1-5_TV-Class

#The current channel (1 to 120) of this TV.
#The current volume level (1 to 7) of this TV.
#Indicates whether this TV is on/off.

#Constructs a default TV object.
def __init__ (self, channel, volume_level, on):
    self.channel = channel
    self.volume_level = volume_level
    self.on = on

#Turns on this TV.
def tvOn(self):
    self.on = True
#Turns off this TV.
def tvOff(self):
    self.on = False
#Returns the channel for this TV.
#Sets a new volume level for this TV.
#Increases the channel number by 1.
#Decreases the channel number by 1.
#Increases the volume level by 1.
#Decreases the volume level by 1.
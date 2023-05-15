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
def getChannel(self):
    return f"channel" + self.channel 
#Sets a new channel for this TV.
def setChannel(self):
    self.channel = input(int("Channel: "))
#Gets the volume level for this TV.
def getVolume(self):
    print("Volume level:" + self.volume_level)
#Sets a new volume level for this TV.
def setVolume(self):
    self.volume_level = input(int("Volume Level: "))
#Increases the channel number by 1.
def channelUp(self):
    channel_up = self.channel + 1
#Decreases the channel number by 1.
def channelDown(self):
    channel_down = self.channel - 1
#Increases the volume level by 1.
#Decreases the volume level by 1.

#channel: int
#volume_level: int
#on: boolean

#TV ()
#turnOn(): None
#turnOff(): None
#getChannel(): int
#setChannel (channel: int): None
#getVolume(): int
#setVolume (volumeLevel: int): None
#channelUp(): None
#channelDown(): None
#volumeUp(): None
#volumeDown(): None
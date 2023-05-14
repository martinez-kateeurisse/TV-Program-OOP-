#Kate Eurisse L. Martinez_BSCPE 1-5_TV-Class

class TV:
    #Create Objects
    def __init__ (self, channel, volume_level, on):
        self.channel = channel
        self.volume_level = volume_level
        self.on = on

    #Create Methods
    def tv1(self):
        print("tv1's channel is" + self.channel , "and volume level is" + self.volume_level)
    def tv2(self):
        print("tv2's channel is" + self.channel , "and volume level is" + self.volume_level)
    
#Assign values
tv1 = TV(30, 3, "on")
tv2 = TV(3, 2, "on")
#Call methods
tv1.tv1()
tv1.tv1()

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
#Kate Eurisse L. Martinez_BSCPE 1-5_Test Driver program

#Import class file
from Television import TV

#call methods for tv1
tv1 = TV()
#Turning tv1 on
tv1.tv_on()
#Setting channel for tv1
tv1.set_channel(30)
#Settng volume for tv1
tv1.set_volume(3)

#Print output for tv 1
print("tv1's channel is " + tv1.get_channel(), "and volume level is " +  tv1.get_volume())

#Call methods for tv2
tv2 = TV()
#Turing tv2 on
tv2.tv_on()
#Setting channel for tv2
tv2.set_channel(3)
#Setting volume for tv2
tv2.set_volume(2)

#Print output for tv 2
print("tv2's channel is " + tv2.get_channel(), "and volume level is " +  tv2.get_volume())
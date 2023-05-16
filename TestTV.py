#Kate Eurisse L. Martinez_BSCPE 1-5_Test Driver program

#Import class file
#from TV import television
from Television import TV

#call methods for tv1
tv1 = TV()
#Turning tv1 on
tv1.tv_on()
#Setting channel for tv1
tv1.set_channel(30)
#Settng volume for tv1
tv1.set_volume(3)

#Call methods for tv2
tv2 = TV()
#Turing tv2 on
tv2.tv_on()
#Setting channel for tv2
tv2.set_channel(3)
#Setting volume for tv2
tv2.set_volume(2)

#Print output
print(tv1.get_channel(), tv1.get_volume())
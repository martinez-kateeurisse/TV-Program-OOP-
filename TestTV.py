#Kate Eurisse L. Martinez_BSCPE 1-5_Test Driver program

#Import class file
#from TV import television
from Television import TV

#call methods
tv1 = TV()
tv1.tv_on()
tv1.set_channel(30)
tv1.set_volume(3)
#print output
print(tv1.get_channel(), tv1.get_volume())
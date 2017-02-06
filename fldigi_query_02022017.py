"""
fldigi autotuner script
Released into the public domain by Adam Greig in 2010
"""

import xmlrpclib
import math
import time
import string
import time

def cksumcheck(mystring):
		myval=0
		mylen=len(mystring)
		for i in range(2, mylen-3):
			myval=(ord(mystring[i]) ^ myval)
		return myval

# Desired audio frequency (Hz)
demand_freq = 1500

# Loop time (s)
loop_time = 0.1

# The highest step change we will retune the radio by (Hz/loop)
max_change = 3

# How quickly we react to errors. Too high will cause oscillation.
error_gain = 0.1

# Connect to fldigi
s = xmlrpclib.ServerProxy("http://localhost:7362")

mystart=0
mychunk=''
mydata=''

while 1:
	
	myanswer= s.text.get_rx_length()
	print mystart, myanswer
	sw=0
	if mystart>myanswer:
		mystart=myanswer
		
	if myanswer>63:
		del mychunk
		mychunk=str(s.text.get_rx(mystart,mystart+64))
		#print mychunk
		k1=mychunk.find("$$B900")
		k2=mychunk.find("*",k1)
		k3=mychunk.find(chr(10),k2)
		print "k1, k2, k3", k1,k2,k3
		
		if k1>=0 and k2>k1 and k3>k2:
			del mydata
			mydata=mychunk[k1:k3]
			print mydata
			mystart=mystart+k3
			sw=1
			
			mych=cksumcheck(mydata)
			mych=hex(mych)
			mych=str(mych)
			if (mydata[-2:]==mych[-2:]):
				print 'check ok'
		
		if sw==0:
			mystart=mystart+1	
		
	time.sleep(5)
		
		


		
			
			
	
	
	
	
	
	
	
	
	
	
#mychar=s.text.get_rx(1,myanswer)


#s.text.add_tx("Ciao Ciao")



#print mychar
#print myanswer

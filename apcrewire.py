import mido

#config
first={
'control_change':'control_change',
'note_on':'note_on',
'note_off':'note_off'
}
second={
'channel=0':'channel=0',
'channel=1':'channel=1',
'channel=2':'channel=2',
'channel=3':'channel=3',
'channel=4':'channel=4',
'channel=5':'channel=5',
'channel=6':'channel=6',
'channel=7':'channel=7'
}
third={
'control=5':'control=5'
}
fourth={}
fifth={}



devices=mido.get_input_names()

for x in range(0, len(devices)):
	print str(x) + ":  " + devices[x]

x=input("Enter input Device: ")
devicename=devices[x]
print devicename

inport=mido.open_input(devicename)
outport=mido.open_output('APCRewire',virtual=True)

for message in inport:
	messagestr=mido.format_as_string(message)
	parts=messagestr.split(' ')
	try:
		c1=first[parts[0]]+' '
	except:
		c1=parts[0]+' '
	try:
		c2=second[parts[1]]+' '
	except:
		c2=parts[1]+' '
	try:
		c3=third[parts[2]]+' '
	except:
		c3=parts[2]+' '
	try:
		c4=fourth[parts[3]]+' '
	except:
		c4=parts[3]+' '
	try:
		c5=fifth[parts[4]]
	except:
		c5=parts[4]
	
	newmessage=mido.Message.from_str(c1+c2+c3+c4+c5)
	print newmessage
	outport.send(newmessage)



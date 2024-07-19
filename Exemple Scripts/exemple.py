import ElgatoWavePy

identifier = "USB#VID_046D&PID_0ABA&MI_00#7&3B11137E&0&0000#{6994AD04-93EF-11D0-A3CC-00A0C9223196}\\GLOBAL"
name= "Haut-parleurs (Logitech PRO X Wireless Gaming Headset)"

input = "Game"

mixer = "local"

vol = 50

ElgatoWavePy.SetOutput(identifier, name)
ElgatoWavePy.SetVolumeInput(vol, input, mixer)


#This little script will Put my Headset on the Monitoring mix Output and will put the Game input to 50% on the monitoring mix
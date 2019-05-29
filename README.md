# PSO

###Raspi ssh configuration

1- ativar SSH.
		-In a terminal type “sudo raspi-config”.
		-Scroll down the menu options and enable SSH.
		-type “ifconfig” into a terminal
		-Write down your IP address, which should be listed under “inet addr”. Restart the computer to save your config changes.
2- instalar 'xrdp' nos Raspberry
		- sudo apt-get install xrdp
	
3-(não deu) re-install xrdp and vncserver
		-sudo apt-get remove xrdp vnc4server thightvncserver		
		-sudo apt-get install xrdp vnc4server thightvncserver

# PSO

### Raspi ssh configuration

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

# BLE

### parrot developer statement

5 ARStream protocol
The ARStream library is designed to send and receive arbitraty binary streams
using ARNetwork as its network back-end. It is used to transport live audio
and video data between the product and the controller.
The ARStream library used an acknowledge system on Bebop Drone
firmwares before 2.0.17, while the Jumping Sumo never used them. This
feature won’t be used on newer firmwares (for all products), so implementing it is optionnal for an ARStream compatible library.
# The ARStream library is not designed to be used on BLE networks.
(retirado do ARSDK_protocol.pdf)


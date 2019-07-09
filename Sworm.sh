#!/bin/bash
sudo python3 /home/pi/PSO/findMinidrone.py
pid=$!
wait $pid
python3 /home/pi/PSO/piServer.py &
#pid2=$!
#kill $pid2
#wait $pid2
#echo $pid2 was terminated
python3 /home/pi/PSO/socketTest.py &  
python3 /home/pi/PSO/socketTest.py & 
python3 /home/pi/PSO/socketTest.py & 
python3 /home/pi/PSO/socketTest.py & 
python3 /home/pi/PSO/socketTest.py & 
python3 /home/pi/PSO/socketTest.py & 
python3 /home/pi/PSO/socketTest.py & 
python3 /home/pi/PSO/socketTest.py & 

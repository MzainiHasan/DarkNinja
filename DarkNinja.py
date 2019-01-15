#!/bin/bash

# Tools For penetration <3
# Coded By Mz Hasan
# happy hacking

# Bersihkan Layar
clear

#This colour
blue='\e[0;34'
cyan='\e[0;36m'
green='\e[0;34m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[1;33m'

figlet DarkNinja V1
###################################################
# CTRL C
###################################################
trap ctrl_c INT
ctrl_c() {
clear
echo -e $red"[#]> (Ctrl + C ) Detected, Trying To Exit ... "
sleep 1
echo ""
echo -e $yellow"[#]> Thank You For Using My Tools ... "
sleep 1
echo ""
echo -e $white"[#]> Happy Hacking :v ... "
sleep 1
exit
}

# Isi oc 
echo ""
echo -e $white"         ***********************************************"
echo -e $white"         #                                             "
echo -e $white"         # $cyan  Toolkit For$red Penetration$white    "
echo -e $white"         # $cyan  Coded by$red Mz Hasan$white          "
echo -e $white"         # $cyan  Follow Me On Github:$red @MzainiHasan$white"
echo -e $white"         # $cyan  Contact Me In:$red zaini.hasan13@gmail.com$white"
echo -e $white"         # $cyan  update 2019                                             "
echo -e $white"         ***********************************************"
echo ""
echo -e $red" 01) RED_HAWK"
echo -e $red" 02) XAttacker"
echo -e $red" 03) Metasploit-framework "
echo -e $red" 04) sqlmap"
echo -e $red" 05) D-tect"
echo -e $red" 06) Vegile"
echo -e $red" 07) Brutesploit"
echo -e $red" 08) Joomscan"
echo -e $red" 09) Opendoor"
echo -e $red" 10) TheHarvester"
echo -e $green" 00) Menu Spesial"
echo -e $red" 99) Exit"
echo -e $green""
read -p "[DarkNinja]> " act;

if [ $act = 1 ] || [ $act = 01 ]
then
clear
echo -e $red" Installing Red Hawk "
sleep 1
apt update && apt upgrade
apt install php
apt install git
git clone https://github.com/Tuhinshubhra/RED_HAWK
echo -e $red" D O N E "
fi

if [ $act = 2 ] || [ $act = 02 ]
then
clear
echo -e $red" Installing Xattacker "
sleep 1
apt install perlpip install argparse
pip install netaddr
git clone https://github.com/Moham3dRiahi/XAttacker
cd XAttacker
cd ~/
echo -e $red" D O N E "
fi

if [ $act = 3 ] || [ $act = 03 ]
then
clear
echo -e $red" Installing Metasploit "
sleep 1
apt update && apt upgrade
apt install git
apt install wget
wget https://raw.githubusercontent.com/verluchie/termux-metasploit/maste
r/install.sh
chmod 777 install.sh
sh install.sh
echo -e $red" D O N E "
fi

if [ $act = 04 ] || [ $act = 4 ]
then
clear
echo -e $red" Installing SQLMap "
sleep 1
apt update && apt upgrade
apt install python2
git clone https://github.com/sqlmapproject/sqlmap.git
cd ~/
echo -e $red" D O N E "
fi

if [ $act = 5 ] || [ $act = 05 ]
then
clear
echo -e $red" Installing D-Tect "
sleep 1
apt-get update && apt-get upgrade
apt-get install git
apt-get install python2
git clone https://github.com/shawarkhanethicalhacker/D-TECT
echo -e $red" D O N E "
fi

if [ $act = 6 ] || [ $act = 06 ]
then
clear
echo -e $red" Installing Vegile "
sleep 1
git clone https://github.com/Screetsec/Vegile.git
cd Vegile
chmod +x Vegile
cd ~/
echo -e $red" D O N E "
echo -e $yellow" Usage : ./Vegile --h  = for help "
fi

if [ $act = 07 ] || [ $act = 7 ]
then
clear
echo -e $red" Installing brutesploit "
sleep 1
git clone https://github.com/Screetsec/Brutesploit.git
cd Brutesploit
chmod +x Brutesploit
cd ~/
echo -e $red" D O N E "
echo -e $yellow" Usage : ./Brutesploit or sudo ./Brutesploit "
fi

if [ $act = 8 ] || [ $act = 08 ]
then
clear
echo -e $red" Installing Joomscan "
sleep 1
apt install perl
apt install git
git clone https://github.com/rezasp/joomscan
echo -e $red" D O N E "
fi

if [ $act = 9 ] || [ $act = 09 ]
then
clear
echo -e $red" Installing opendoor "
sleep 1
apt update && apt upgrade
apt install python3
git clone https://github.com/stanislav-web/OpenDoor
cd ~/opendoor
pip3 install -r requirements.txt
chmod +x opendoor.py
cd ~/
echo -e $red" D O N E "
fi

if [ $act = 10 ] || [ $act = 10 ]
then
clear
echo -e $red" Installing theharvester "
sleep 1
git clone https://github.com/laramies/theHarvester/
cd theHarvester/
sudo pip install requests
cd ~/
echo -e $red" D O N E "
echo -e $yellow" Usage : python theHarvester.py -d yourweb.c
om -l 100 -b google "
fi

if [ $act = Menu spesial ] || [$act = Menu spesial ]
then
clear
echo -e $green" Installing Menu spesial "
sleep 1
apt update
apt install git
git clone https://github.com/Rajkumrdusad/Tool-X.git
echo -e $green" D O N E "
fi

if [ $act = 99 ] || [ $act = 99  ]
then
echo -e $green" Thanks For Using My Tools "
sleep 1
echo -e $green" Happy Hacking "
sleep 1
exit
fi

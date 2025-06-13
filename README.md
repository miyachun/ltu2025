-虛擬環境安裝-  
  
*查詢: python --version  
  
*python下載: Note that Python 3.10.10 cannot be used on Windows 7 or earlier.  
Download Windows installer (64-bit)  
  
1->環境變數  
C:\Users\XXXX\AppData\Local\Programs\Python\Python310\Scripts\  
C:\Users\XXXX\AppData\Local\Programs\Python\Python310\  
  
2->安裝virtualenv  
pip install virtualenv  
virtualenv 取一個名稱  
  
3->啟動  
到虛擬環境Scripts目錄中啟動  
activate  

------------------------------------------------------------------------------  
-pi4 with dht22-  
  
https://www.raspberrypi.com/software/  
https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html  
https://www.realvnc.com/en/connect/download/viewer/?lai_sr=0-4&lai_sl=l  
https://images.theengineeringprojects.com/image/webp/2021/03/raspberry-pi-4.png.webp?ssl=1  
  
*指令:  
sudo apt update  
sudo apt upgrade  
sudo raspi-config  
ifconfig  
sudo reboot  

*建立Virtualenv:  
python -m venv myenv  
source myenv/bin/activate  
  
*安裝GPIO  
pip install rpi.gpio  
  
*設定DHT11,DHT22:  
Python Setup  
https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup  
Installing the CircuitPython-DHT Library  
https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi  


------------------------------------------------------------------------------  

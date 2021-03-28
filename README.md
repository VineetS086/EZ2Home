# HaXplore 2.0 - Submission Report Format
<img src="https://github.com/VineetS086/EZ2Home/blob/main/Screenshots/logo.png" height="300">

This is the official code repository for _Talent-404_ . This _type of application_ was developed during HaXplore 2.0, 
the online hackathon conducted by Codefest, the annual departmental fest of Computer Science department, IIT BHU Varanasi.

## _Talent-404_

* _[VineetS086](https://github.com/VineetS086)_
* _[rahuljandial2](https://github.com/rahuljandial2)_
* _[pranavsambyal](https://github.com/pranavsambyal)_
* _[swayamgupta74](https://github.com/swayamgupta74)_

# _EZ2Home_
#### Home Automation is Cool🤩! But it's Expansive🥲. 
#### EZ2Home enables you to automate your Home using basic hardware that costs under ₹600/room.🤑



## Overview
EZ2Home is a Home Automation System that can be used to control Home Appliances over Internet or Home Wi-Fi network. 
The Hadware requirement is only ESP module and Relays and you can automate your home.
Here we will use APIs to connect to the microcontrollers and appliances are attached to that microcontroller can be 
controlled directly from the site with just a click.

#### How it works
Our project has a main page which contain all the rooms that can be controlled by the microprocessors.

Each room has their own page to show the available appliances that can be controlled from the buttons.

If the appliances button is green it means the appliance is ON and if it's grey it means the appliance is OFF.

## Technology used
Python, Django, MicroPython


## Usage

### Minimum Hardware Required For Usage
* Any ESP module that supports MicroPython (eq-ESP8266, ESP32)
* 5V multi-channel Relay module
* Wi-Fi Network

### Required Installations
* Python 3.8 
* Django 3.2
* DjangoRestFramework 3.12

* MicroPython- esp8266-20200911-v1.13.bin


### Installation
#### MicroController
* Download the Firmware from this link - https://micropython.org/download/esp8266/
* Installation guide- https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html
* Copy the content of EZ2Home/Micro-Controller/Lan/ to the ESP module
* edit EZ2Home/Micro-Controller/Lan/wifi.json
* edit host name in EZ2Home/Micro-Controller/Lan/main.py at line 14.

#### Server Setup
* open mysite.
* reset the database.
* run `$ python3 manage.py runserver 0.0.0.0:8888`
* to know the host name run `$ ifconfig en0 inet` 

### ENJOY


## Screenshots/Demo Video
### Video Link:
*

### Simple Layout
<div class="row">
  <div class="column">
<img src="https://github.com/VineetS086/EZ2Home/blob/main/Screenshots/home.png" height="300">
  </div>
  <div class="column">
<img src="https://github.com/VineetS086/EZ2Home/blob/main/Screenshots/room.png" height="300">
  </div>
</div>

### Secure Login
<img src="https://github.com/VineetS086/EZ2Home/blob/main/Screenshots/login.png" width="200">

### Add/Delete Appliances Easily
<img src="https://github.com/VineetS086/EZ2Home/blob/main/Screenshots/add%20appliance.png" width="300">


#### Tracks used
TO BE added


#### AWS Services Used
TO BE added






# Space Instagram
This program consists of several modules: two of them
download images from Spacex last launch and Hubble collection,
the last one resizes downloaded images and uploads them to 
instagram account.

### How to Install
Python3 should be already installed. Then use pip (or pip3,
if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
Create **.env** file and save there username and 
password for your instagram account in the following format:
```
USER: "your user name"
PASSWORD: "your password"
```
By default all images will be saved in **images** folder
which will be created in your current directory.
### Project Goals
The code is written for educational purposes on online-course 
for web-developers [dvmn.org](https://dvmn.org).
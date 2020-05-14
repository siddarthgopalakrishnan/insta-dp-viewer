import requests
import datetime
import os
import subprocess
import sys

#Asks user to enter username
username=input("Enter User Name: ")

#Gets the source code of the webpage of given user
sourceCode = str(requests.get(f'https://www.instagram.com/{username}/').text)

#gets date to be saved in filename
date = datetime.datetime.now()
time = f"{date.day}-{date.month}-{date.year}"

#filename is the final name of file
filename = f"{username} ({time}).jpg"

#left and right are the indices in source code, which has url of the DP
left = sourceCode.find("pic_url_hd")+13
right = sourceCode.find("requested_by_viewer")-3

#hdurl is the url of the DP
hdurl = sourceCode[left:right]
#reponse has the Display Picture Stored
response = requests.get(hdurl)

f = open(filename,'wb')
#writing image in a image file called filename
f.write(response.content)
f.close()

#to open the image on Windows
if sys.platform == "win32":
        os.startfile(filename)
#to open the image on Mac&Linux
else:
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, filename])

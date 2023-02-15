
# music player by khushal sharma
from playsound import playsound
print("List of songs available\n1-All Black\n2-Believer.mp3\n3-Chaar Kadam.mp3")
a=(int(input("Enter name of the song Number you want to play : ")))
print("Enjoy your music")
if a==1:
    playsound("C:\\Users\\acer\\Videos\\Coding Projects\\Music player in Python\\All Black.mp3")

elif a==2:
    playsound("C:\\Users\\acer\\Videos\\Coding Projects\\Music player in Python\\Believer.mp3")
else :
     playsound("C:\\Users\\acer\\Videos\\Coding Projects\\Music player in Python\\Chaar Kadam.mp3")

from gtts import gTTS
import os

#text = "Hello , How are you? Hope you doing great"

#you can also insert a whole file instead of text
abc = open("sample.txt")
text = abc.read()

language = 'en' #en for english
obj = gTTS(text=text,lang=language,slow=False) #we have used slow = False because our converted video will have a high speed
obj.save("sample.mp3")

 #to open video file automaticallly we have to use os
os.system("sample.mp3")
# pip install pytube
from pytube import YouTube
link = "https://youtu.be/enHZcA2XPR8"
yt = YouTube(link)

videos = yt.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print (i)
print()
strm = int(input("Enter here: "))
videos[strm].download()
#print(yt.title)
#print(yt.thumbnail_url)
print(yt.title+" is successfully downloaded")

from pytube import YouTube

url = input("Enter YouTube video URL: ")

yt = YouTube(url)
print("Title:", yt.title)

video = yt.streams.get_highest_resolution()
video.download()

print("Download completed!")

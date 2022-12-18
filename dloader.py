from pytube import Playlist
import os

#add path
path = ""

#add playlist link (make sure to set playlist as public)
playlist = Playlist("")
  
for video in playlist.videos:
    try:
        videodl = video.streams.filter(only_audio=True).first()
        out_file = videodl.download(output_path=path)

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print(video.title + " has been downloaded.")
    except:
        print("Something went wrong while downloading: "+video.title)


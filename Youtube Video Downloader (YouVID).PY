from pytube import YouTube #install the requied module using pip
                           # "pip install pytube"
                           # CODE by APURBO KARMOKAR

link = input("Enter YOUTUBE video's URL : ")

print("\nPlease wait we are looking for the available formats of the File.\n")

yt = YouTube(link)
videos = yt.streams.all() # This will stream all the format avaialbe for the video

video = list(enumerate(videos)) # this will be index all the format in list starting with zero

for i in video:
    print(i) # this will print all the available format of video with proper index

dn_option = int(input("\nEnter the desired option to download the format : ")) 
                          # Ask user that which format he wanted to download

if dn_option >= len(video):
   print("Error! [File not Availabe]")
elif dn_option < len(video):
        dn_video = videos[dn_option]
        print("\nPlease wait a minute, the file is under downloading process...")
        dn_video.download()

        print ("\nDownload Successfully.")



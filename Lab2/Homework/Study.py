from youtube_dl import YoutubeDL

# Download a single video
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=HXkh7EOqcQ4'])

#  Download audio
options = {
    'format': 'bestaudio/audio' 
}
d2 = YoutubeDL(options)
d2.download(['https://www.youtube.com/watch?v=HXkh7EOqcQ4'])

# Search and then download the first video
options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1 
}
d3 = YoutubeDL(options)
d3.download(['Thanh xuân Da LAB'])

options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1, 
    'format': 'bestaudio/audio'
}
d4 = YoutubeDL(options)
d4.download(['Thu cuối yanbi'])
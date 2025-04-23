# %% 
import requests
import pandas as pd

# %% 
api_key = "AIzaSyANOovfLBRYlDRfMycJtUlNk5b2PR2qnfw"

# %% 
handle_name = "boilerroom"

# %% 
search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=channel&q={handle_name}&key={api_key}"
search_response = requests.get(search_url).json()
channel_id = search_response['items'][0]['id']['channelId']

print("Resolved Channel ID:", channel_id)

# %% 
videos_url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=10"
video_response = requests.get(videos_url).json()

# %% 
video_info = []

for item in video_response['items']:
    video_id = item['id'].get('videoId')
    title = item['snippet']['title']
    published = item['snippet']['publishedAt']
    video_info.append({'video_id': video_id, 'title': title, 'published_at': published})

df = pd.DataFrame(video_info)
print(df)

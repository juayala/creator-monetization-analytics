# %% 
import requests
import pandas as pd
import html
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables
load_dotenv()

# Get the API key 
api_key = os.getenv('API_KEY')
# %%
# Postgres databse connection details 
pg_user = os.environ['PG_USER']
pg_password = os.environ['PG_PASSWORD']
pg_host = os.environ['PG_HOST']
pg_db = os.environ['PG_DB']

# %%
pg_conn_str = f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}/{pg_db}'
pg_engine = create_engine(pg_conn_str)

# %%
# Test the API key
handle_name = "boilerroom"
search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=channel&q={handle_name}&key={api_key}"
search_response = requests.get(search_url).json()

# Safely check for valid results
if 'items' in search_response and len(search_response['items']) > 0:
    channel_id = search_response['items'][0]['id']['channelId']
    print("Resolved Channel ID:", channel_id)
else:
    print("Channel not found. Response:")
    print(search_response)

channel_id = search_response['items'][0]['id']['channelId']

print("Resolved Channel ID:", channel_id)

# %% 
videos_url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=10"
video_response = requests.get(videos_url).json()

# %% 
video_info = []

for item in video_response.get('items', []):
        video_id = item['id'].get('videoId')
        title = html.unescape(item['snippet']['title'])  # Decode "&amp;" etc.
        published = item['snippet']['publishedAt']
        video_info.append({
            'Video ID': video_id,
            'Video Title': title,
            'Published Date': published
        })

# Convert to DataFrame
df = pd.DataFrame(video_info)

# Format 'Published Date' column
df['Published Date'] = pd.to_datetime(df['Published Date']).dt.strftime('%Y-%m-%d %H:%M')

# Sort by newest first
df = df.sort_values(by='Published Date', ascending=False).reset_index(drop=True)

# Adjust Pandas display options
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_rows', None)     # Show all rows
pd.set_option('display.max_colwidth', None) # Do not truncate column content
pd.set_option('display.width', 1000)        # Set the display width to avoid wrapping

# Output cleaned DataFrame
print(df)

# %%
# Write DataFrame to videos table in Postgres (raw schema)
df.to_sql('videos', pg_engine, schema='raw', if_exists='replace', index=False)

# %%
# Print confirmation message
print(f'{len(df)} records loaded into Postgres videos table.')

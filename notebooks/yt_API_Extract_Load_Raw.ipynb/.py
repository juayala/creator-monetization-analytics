# %% 
import os
import pandas as pd
from googleapiclient.discovery import build
from sqlalchemy import create_engine
from dotenv import load_dotenv
import re

load_dotenv()

# %%
# Initialize clients
youtube = build("youtube", "v3", developerKey=os.getenv("API_KEY"))

def iso8601_to_seconds(dur: str) -> int:
    m = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", dur)
    if not m:
        return 0
    h, mi, s = m.groups(default="0")
    return int(h) * 3600 + int(mi) * 60 + int(s)

# %%
# Fetch today’s top 50 trending Music videos in the US
resp = youtube.videos().list(
    part="snippet,statistics,contentDetails",
    chart="mostPopular",
    regionCode="US",
    videoCategoryId="10",  # Music
    maxResults=21
).execute()

rows = []
for v in resp["items"]:
    snip = v["snippet"]
    stats = v.get("statistics", {})
    dur_s = iso8601_to_seconds(v["contentDetails"]["duration"])
    # skip YouTube Shorts (<= 60s)
    if dur_s <= 60:
        continue

    rows.append({
        "published_at":  snip["publishedAt"],
        "video_id":      v["id"],
        "title":         snip["title"],
        "channel_id":    snip["channelId"],
        "channel_name":  snip["channelTitle"],
        "duration_s":    dur_s,
        "view_count":    int(stats.get("viewCount", 0)),
        "like_count":    int(stats.get("likeCount", 0)),
        "comment_count": int(stats.get("commentCount", 0)),
    })

# %%
# Build the DataFrame
df = pd.DataFrame(rows)

# convert the publishedAt string into a date-only column
df['published_at'] = pd.to_datetime(df['published_at']) \
                       .dt.strftime('%Y-%m-%d')

# %%
# Preview
print(df.head(21))


# %%
# Postgres databse connection details 
pg_user = os.environ['PG_USER']
pg_password = os.environ['PG_PASSWORD']
pg_host = os.environ['PG_HOST']
pg_db = os.environ['PG_DB']

# %%
pg_conn_str = f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}/{pg_db}'
pg_engine = create_engine(pg_conn_str)

# Write DataFrame to yt_trending table in Postgres (raw schema)
df.to_sql('yt_trending', pg_engine, schema='raw', if_exists='replace', index=False)

# %%
# Print confirmation message
print(f'{len(df)} records loaded into Postgres yt_trending table.')
# %%

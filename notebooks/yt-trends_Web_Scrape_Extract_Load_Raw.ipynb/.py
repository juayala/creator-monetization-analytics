# %%
from firecrawl import FirecrawlApp
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv


load_dotenv()
# %%
api_key = os.getenv("FIRECRAWL_API_KEY")

app = FirecrawlApp(api_key=api_key)

scrape_result = app.scrape_url(
    "https://yt-trends.iamrohit.in/United-States-of-America/music",
    formats    = ["json"],
    jsonOptions= {
      "prompt": (
        "Extract the video id, video name, channel name, view count, "
        "like count, comment count, and rank from the page. "
        "Iterate these steps for the entire list on the website until you reach rank 21."
      )
    }
)

scrape_result
# %%
youtube = scrape_result.json['videos']

# Convert the scraped JSON data to a DataFrame
df = pd.DataFrame(youtube)

# Keep only the required columns: video_id, video_name, channel_name, view_count, like_count, and comment_count
df = df[['video_id', 'video_name', 'channel_name', 'view_count', 'like_count', 'comment_count']]
df = df.head(21)
# %%
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

# Write DataFrame to yt_video table in Postgres (raw schema)
df.to_sql('yt_video', pg_engine, schema='raw', if_exists='replace', index=False)

# %%
# Print confirmation message
print(f'{len(df)} records loaded into Postgres yt_video table.')
# %%
from firecrawl import FirecrawlApp
import pandas as pd
from sqlalchemy import create_engine
import os


# %%
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="fc-9d84309514864cea803c826ecbdbe7f2")

url = 'https://playboard.co/en/chart/video/most-viewed-music-videos-in-united-states-daily'

scrape_result = app.scrape_url(url, {
    'formats': ['json'],
    'jsonOptions': {
        'prompt': 'Extract the rank, title, views, and channel name from the page. Iterate these steps for the entire list on the website until you get to rank 25.'
    }
})
scrape_result

# %%
youtube = scrape_result['json']['videos']

# %%
df = pd.DataFrame(youtube)
df = df.drop(columns=['rank'])

# %%
df
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
# %%

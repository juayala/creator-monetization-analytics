# %%
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import re


# from firecrawl import FirecrawlApp

# url = "https://playboard.co/en/youtube-ranking/most-popular-music-channels-in-united-states-monthly"
# headers = {"User-Agent": "Mozilla/5.0"}


# # 1) Try the simple requests fetch
# resp = requests.get(url, headers=headers)
# soup = BeautifulSoup(resp.text, "html.parser")

# # 2) Grab all rows in any <tbody>
# rows = soup.select("tbody tr")
# if not rows:
#     # fallback to Firecrawl if nothing found
#     app = FirecrawlApp(api_key='FIRECRAWL_API_KEY')
#     result = app.scrape_url(url)  # returns a ScrapeResponse
#     html   = result.html          # access the .html attribute
#     soup   = BeautifulSoup(html, "html.parser")
#     rows = soup.select("tbody tr")

# # 3) Parse each row by column position
# data = []
# for row in rows:
#     cols = row.find_all("td")
#     if len(cols) < 7: continue

#     data.append({
#         "Channel Name":        cols[2].get_text(strip=True),
#         "Monthly Subscribers": cols[3].get_text(strip=True),
#         "Total Views":         cols[4].get_text(strip=True),
#         "Avg Views/Video":     cols[5].get_text(strip=True),
#         "Est. Earnings":       cols[6].get_text(strip=True),
#     })

# df = pd.DataFrame(data)

# # 4) Clean the numeric columns
# def parse_num(s):
#     if not s or s == "—":
#         return None
#     s_clean = s.replace(",", "").strip()
#     # grab first number + optional decimal + optional K/M
#     m = re.search(r"([0-9]+(?:\.[0-9]+)?)([KM]?)", s_clean)
#     if not m:
#         return None
#     num, suffix = m.group(1), m.group(2)
#     val = float(num)
#     if suffix == "M":
#         val *= 1_000_000
#     elif suffix == "K":
#         val *= 1_000
#     return val


# for col in ["Monthly Subscribers", "Total Views", "Avg Views/Video"]:
#     df[col] = df[col].apply(parse_num)

# def parse_earn(s):
#     # same cleaning for $ + ranges
#     if not s or s == "—":
#         return None
#     s_clean = s.replace("$","").replace(",", "").strip()
#     # take everything before any dash or space
#     first = re.split(r"[-\s]", s_clean)[0]
#     return parse_num(first)


# df["Est. Earnings"] = df["Est. Earnings"].apply(parse_earn)

# # 5) Preview
# df.head()






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

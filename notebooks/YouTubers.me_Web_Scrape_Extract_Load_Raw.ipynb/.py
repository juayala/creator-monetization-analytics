# %% 
# Import Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# %%
pg_user = os.environ['PG_USER']
pg_password = os.environ['PG_PASSWORD']
pg_host = os.environ['PG_HOST']
pg_db = os.environ['PG_DB']

# %%
pg_conn_str = f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}/{pg_db}'
pg_engine = create_engine(pg_conn_str)
# %%
# Load the Page
url = "https://youtubers.me/boiler-room/youtube-statistics"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Optional: print some HTML for inspection
print(soup.prettify()[:2000])

# %%
# Initialize and Populate Data Dictionary
data = {
    "Channel Name": "Boiler Room",
    "Subscribers": None,
    "Total Views": None,
    "Video Count": None

}

items = soup.find_all("div", class_="item")


# Get all <div class="bottom"> tags that contain stats
bottom_tags = soup.find_all("div", class_="bottom")

top_tags = soup.find_all("div", class_="top")


# Use known index positions based on visual inspection
data["Subscribers"] = bottom_tags[0].text.strip() if len(bottom_tags) > 0 else None
data["Total Views"] = bottom_tags[1].text.strip() if len(bottom_tags) > 1 else None
data["Video Count"] = bottom_tags[2].text.strip() if len(bottom_tags) > 2 else None
data["Estimated earnings (Last 30 days)"] = bottom_tags[3].text.strip() if len(bottom_tags) > 3 else None


# Views Per Day
views_per_day_tag = soup.find("div", string=lambda x: x and "views per day" in x.lower())
if views_per_day_tag:
    parent = views_per_day_tag.find_parent("div", class_="profile-statistics")
    if parent:
        views_value = parent.find("div", class_="count")
        if views_value:
            data["Views Per Day"] = views_value.text.strip()

# %%
# Create DataFrame
df = pd.DataFrame([data])
pd.set_option('display.max_colwidth', None)
df

# %%
df.to_sql('YouTube_Channel', pg_engine, schema='raw', if_exists='replace', index=False)

# %%
# Print confirmation message
print(f'{len(df)} records loaded into Postgres YouTube_Channel table.')
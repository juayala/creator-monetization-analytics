# 🎬 Creator Monetization Analytics Platform

## 🛠️ Tech Stack
- **Python** – For API requests and web scraping
- **SQL** – For querying and analyzing structured data
- **dbt** – For data transformation and dimensional modeling
- **AWS RDS PostgreSQL** – Cloud-hosted database for storing raw and transformed data
- **GitHub Actions** – For workflow automation of extract, transform, and load processes
- **Google Looker Studio** – For building interactive dashboards and data visualizations

---

## 🎯 Project Objective
This project emulates a real-world data analyst role at YouTube Ads by building a data product that analyzes creator monetization trends. The goal is to identify which content categories, creators, and engagement patterns drive the most ad revenue on the platform.

We leverage YouTube video performance data alongside monetization benchmarks to deliver actionable insights that support business teams in optimizing creator partnerships and content strategies.

---

## 💼 Job Description Alignment
**Role:** Data Products Analyst  
**Company:** YouTube (Google)  
**Team:** YouTube Ads  

This project mirrors the responsibilities in the job posting by:
- Designing ETL pipelines using Python and SQL
- Structuring analytics-ready tables with dbt
- Running SQL-based insights on creator engagement
- Visualizing findings via Looker Studio dashboards

📎 [Job_Description.pdf](./proposal/Job_Description.pdf)

---

## 📊 Data

### 📡 Sources
- **YouTube Data API v3**  
  [YouTube API Docs](https://developers.google.com/youtube/v3)  
  Collects trending video metadata including title, channel, views, likes, and rank.

- **Web Scrape – yt-trends.iamrohit.in**  
  Uses Firecrawl and BeautifulSoup to extract reaction and ranking data from trending music videos in the U.S.  
  Supports benchmarking creator popularity and breakout content performance.

### 🔍 Characteristics
- Real-time trending data from a third-party site tracking YouTube video stats
- Rich with creator/channel-level insights such as views, likes, and rank metrics

---

## 📁 Repository Structure
├── .github/workflows/
│ ├── yt_trends_api_pipeline.yml
│ ├── yt_trends_web_scrape_pipeline.yml
│ └── dbt_pipeline.yml
├── data/
│ ├── yt_trends_API_Data_Pipeline.pdf
│ ├── yt_trends_Web_Scrape_Data_Pipeline.pdf
│ ├── yt_trends_API_ERD.pdf
│ └── yt_trends_Web_Scrape_ERD.pdf
├── notebooks/
│ ├── yt_trends_API_Extract_Load_Raw.ipynb
│ ├── yt_trends_Web_Scrape_Extract_Load_Raw.ipynb
│ ├── yt_trends_API_SQL_Analysis.ipynb
│ └── yt_trends_Web_Scrape_SQL_Analysis.ipynb
├── dbt/
│ ├── models/
│ │ ├── staging/
│ │ │ ├── stg_yt_trends_api.sql
│ │ │ └── stg_yt_trends_web_scrape.sql
│ │ └── warehouse/
│ │ ├── dim_channel.sql
│ │ └── fct_creator_reactions.sql
│ └── dbt_project.yml
├── proposal/
│ ├── Project_Proposal.pdf
│ └── Job_Description.pdf
├── reports/
│ ├── Presentation.pdf
│ └── Visualizations.pdf
└── README.md


---

## 📁 Notebooks / Python Scripts
- `yt_trends_API_Extract_Load_Raw.ipynb`  
  Fetches top 50 trending music videos via yt-trends API and stores in PostgreSQL.

- `yt_trends_Web_Scrape_Extract_Load_Raw.ipynb`  
  Scrapes additional engagement metrics such as reaction counts and ranks.

- `yt_trends_API_SQL_Analysis.ipynb`  
  Includes descriptive and diagnostic SQL queries on view counts and top creators.

- `yt_trends_Web_Scrape_SQL_Analysis.ipynb`  
  Ranks channels by total reactions and identifies top-performing videos per channel.

---

## 🧠 Insight Example
![Sample Analysis]

From `yt_trends_Web_Scrape_SQL_Analysis.ipynb`:
- **HYBE LABELS** leads with 972,000 total reactions across multiple uploads.
- **Maroon5VEVO** follows with 672,600 reactions—entirely from a single hit video.
- **Recommendation**: Avoid overdependence on one hit; spread engagement with sequels, clips, and smart thumbnails.
- **Prediction**: Channels mimicking these tactics may increase reactions by 15–20% in the next month.

---

## 📊 Visualizations
All visualizations were created in **Google Looker Studio**, connecting to PostgreSQL for live querying and dashboard development.

📎 [Visualizations.pdf](./reports/Visualizations.pdf)

Highlights include:
- Bar chart: Total reactions by channel
- Line chart: Engagement trends over time
- Comparison: CPM estimates vs actual view counts

---

## 🔮 Future Improvements
- Add NLP-based sentiment analysis on video comments
- Enrich dataset with upload cadence and audience retention metrics
- Expand beyond U.S. market to track global trends by region

---

## 📦 Analytics Framework Reference

**1. Define the business problem**  
Which creators and content types drive the most monetizable engagement?

**2. Collect and prepare data**  
Extracted video metrics via yt-trends API and scraped additional benchmarks.

**3. Analyze the data**  
SQL queries with aggregation, window functions, joins, and CTEs.

**4. Communicate insights**  
Google Looker dashboards supported with clear recommendations.

**5. Take action**  
Target content production and creator collaboration based on the top monetization signals.

---

## 👤 About Me
**Jonathan Ayala**  
📍 Los Angeles, CA  
🎓 LMU ISBA 2025 | 🎯 Deloitte Incoming Analyst  
📧 j.ayala0014@gmail.com | 🔗 [LinkedIn](https://www.linkedin.com/in/ju-ayala)


# 🎬 Creator Monetization Analytics Platform

## 🛠️ Tech Stack
- **Python** – For API requests and web scraping
- **SQL** – For querying and analyzing structured data
- **dbt** – For data transformation and modeling (dimensional models)
- **AWS RDS PostgreSQL** – Cloud-hosted database for storing raw and transformed data
- **GitHub Actions** – For automation of data extraction and transformation workflows
- **Power BI / Tableau** – For building dashboards and visualizations

## 🎯 Project Objective
This project supports YouTube Ads’ internal business intelligence efforts by building an analytics-ready dataset focused on creator monetization. The goal is to surface insights that help internal business users understand how different content categories, creators, and engagement levels influence revenue generation on the platform.

By integrating YouTube API data with external monetization benchmarks, this project empowers decision-makers to scale insights and identify high-impact monetization strategies.

## 💼 Job Description
**Role:** Data Products Analyst  
**Company:** YouTube (Google)  
**Team:** YouTube Ads  

The position focuses on designing and maintaining scalable data pipelines, building BI products, and ensuring robust and trustworthy data for teams managing content partnerships, advertising, and platform operations. It requires fluency in SQL, Python, and data infrastructure tools.

**Alignment:** This project mirrors the job by:
- Designing custom data pipelines using real-world public APIs
- Modeling data with dbt to improve usability and governance
- Delivering insights via SQL queries and visualizations

👉 [Job_Description.pdf](./proposal/Job_Description.pdf)

## 📊 Data

### Sources
- **YouTube Data API v3**  
  [YouTube API Docs](https://developers.google.com/youtube/v3)  
  Collects video-level metadata, engagement stats, and channel details from YouTube.

- **Web Scrape**: [InfluencerMarketingHub.com](https://influencermarketinghub.com/youtube-money-calculator/) or [SocialBlade.com](https://socialblade.com/)  
  Provides creator CPM benchmarks, estimated ad revenue, and content category monetization insights.

### Characteristics
- **API data**: Dynamic and reliable, with direct relevance to YouTube’s creator ecosystem.
- **Web scraped data**: Public-facing benchmarks and trends that complement internal creator data with market-wide revenue indicators.

## 📁 Notebooks / Python Scripts
- `notebooks/youtube_API_Extract_Load_Raw.ipynb`  
  Extracts video and channel metadata from the YouTube API and loads it into AWS PostgreSQL.

- `notebooks/youtube_Web_Scrape_Extract_Load_Raw.ipynb`  
  Scrapes CPM and monetization data from benchmark sites and stores it in the database.

- `dbt/models/staging/stg_youtube_api.sql`  
  Cleans and formats API-sourced data for analytics.

- `dbt/models/staging/stg_youtube_web_scrape.sql`  
  Transforms scraped monetization data for reporting.

- `dbt/models/warehouse/fct_creator_revenue.sql`, `dim_content_category.sql`  
  Final fact/dimension models used to power BI dashboards and insights.

## 🔮 Future Improvements
- Include sentiment analysis on video comments or titles using NLP.
- Blend in upload frequency and subscriber growth for creator performance modeling.
- Add geographic-level analysis of monetization using location-based metadata (if available from the API).

# 🚀 Optimizing Supply Chain Efficiency for SpaceX (Starlink)

## 🛠️ Tech Stack
- Python
- SQL
- dbt
- AWS RDS PostgreSQL
- GitHub Actions
- Power BI / Tableau

## 🎯 Project Objective
This project is designed to support SpaceX's mission by enhancing supply chain operations through data-driven insights. It focuses on identifying inefficiencies in transportation and vendor performance using real-world public datasets, SQL queries, automated data pipelines, and BI visualizations. 

By building tools to monitor and optimize delivery performance, this project mirrors the type of work expected from a Supply Chain Data Analyst at SpaceX — enabling operational improvements and systemic risk reduction.

## 💼 Job Description
**Position:** Data Analyst, Supply Chain (Starlink)  
**Company:** SpaceX  
**Location:** Redmond, WA  

As part of the Starlink supply chain team, the role involves developing data-driven tools and systems to optimize vendor performance, streamline logistics, and improve delivery outcomes. Key skills include SQL, Power BI/Tableau, data pipeline development, and cross-functional collaboration to support supply chain improvements and Starlink scalability.

This project aligns with the position by:
- Using SQL and data modeling to find trends in transportation and vendor efficiency.
- Building a data pipeline that mimics the responsibilities of owning system maintenance and reporting.
- Visualizing metrics relevant to procurement and logistics.

👉 [Job_Description.pdf](./proposal/Job_Description.pdf)

## 📊 Data

### Sources
- **[U.S. Department of Transportation (DOT) API](https://www.transportation.gov/data)**  
  Source of public infrastructure and logistics data such as travel times, road bottlenecks, and traffic incidents.
  
- **[Federal Motor Carrier Safety Administration (FMCSA)](https://www.fmcsa.dot.gov/)**  
  Provides detailed data on fleet safety, carrier violations, and inspection results—key for evaluating vendor delivery performance.

### Characteristics
- Publicly accessible, regulatory-compliant data
- Includes timestamps, geographic metadata, safety scores, and inspection events
- Requires cleaning and filtering to focus on business-relevant metrics like delay frequency and vendor risk indicators

## 📁 Notebooks / Python Scripts
- [`notebooks/FMCSA_API_Extract_Load_Raw.ipynb`](./notebooks/FMCSA_API_Extract_Load_Raw.ipynb):  
  Extracts and stores FMCSA data in AWS PostgreSQL.

- [`notebooks/DOT_Web_Scrape_Extract_Load_Raw.ipynb`](./notebooks/DOT_Web_Scrape_Extract_Load_Raw.ipynb):  
  Scrapes DOT infrastructure and logistics data and loads it to the database.

- `dbt/models/staging/stg_fmcsa_api.sql` & `stg_dot_web_scrape.sql`:  
  Cleans and normalizes raw data for analytics.

- `dbt/models/warehouse/fct_delivery_performance.sql` & `dim_vendors.sql`:  
  Fact and dimension tables designed to support descriptive and diagnostic analytics.

## 🔮 Future Improvements
- Integrate SpaceX vendor names and delivery logs (if accessible) to enrich the analysis.
- Expand the dashboard to support drill-down insights by region, vendor, or carrier.
- Deploy the pipeline on a regular schedule via GitHub Actions with monitoring alerts for SLA breaches.

---


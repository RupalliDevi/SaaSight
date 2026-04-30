# SaaSight – End-to-End SaaS Analytics Data Platform

## 🚀 Overview

SaaSight is an end-to-end, production-inspired data engineering project designed to simulate the analytics backbone of a modern SaaS business. Rather than relying on static datasets, the platform uses a custom-built Python data generator to create realistic synthetic SaaS data — including user activity, subscription lifecycles, and revenue events — enabling a fully controlled and scalable analytics workflow.

The project showcases how raw operational data can be transformed into business-ready intelligence through a modern cloud-based data stack. It covers the complete pipeline from data generation and orchestration to warehousing, transformation, and visualization, reflecting real-world engineering practices used in production environments.

At its core, SaaSight demonstrates the implementation of layered data architecture, automated workflows, and analytics modeling to support executive decision-making.

---

## 🧱 Architecture

Python Data Generator → Apache Airflow → Snowflake (RAW Layer) → dbt (STAGING & ANALYTICS) → Power BI Dashboard

---

## 🛠 Tech Stack

- Python  
- Apache Airflow  
- Snowflake  
- dbt  
- Power BI  
- Git & GitHub  

---

## 📊 Business Metrics

- 💰 Monthly Recurring Revenue (MRR)  
- 📉 Churn Rate  
- 👥 Monthly Active Users (MAU)  
- 📈 Subscription Trends  
- 🔍 Feature Usage Insights  

---

## ⚙️ What This Project Demonstrates

- End-to-end data pipeline development  
- Workflow orchestration with Airflow  
- Cloud data warehousing with Snowflake  
- Data transformation with dbt  
- KPI-driven analytics modeling  
- Business intelligence visualization  

---

## 📂 Project Structure

SaaSight/  
├── airflow/                # DAGs and orchestration setup  
├── dbt_project/            # dbt models, sources, and configs  
├── scripts/                # Data generation and ingestion scripts  
├── data/                   # Generated datasets / CSV files  
├── docs/                   # Documentation and screenshots  
├── .gitignore  
├── docker-compose.yml  
├── requirements.txt  
└── README.md    

---

# What This Project Highlights
-Synthetic Data Engineering
Designed and generated realistic SaaS business datasets using Python to simulate production-scale operational data.
-Workflow Orchestration
Automated ingestion pipelines using Apache Airflow for scheduled and reliable execution.
-Cloud Data Warehousing
Loaded and managed structured data in Snowflake using a layered architecture approach.
-Data Transformation & Modeling
Applied dbt to build staging and analytics models following best practices in modular SQL development.
-Business Intelligence Delivery
Developed an interactive Microsoft Power BI dashboard to surface KPIs, trends, and strategic insights 

---

## 📌 Status

✅ Core pipeline functional
✅ Snowflake integration completed
✅ dbt transformations validated
✅ Apache Airflow orchestration operational
✅ Microsoft Power BI dashboard developed and insights delivered 

---

© 2026 Rupalli Devi. All Rights Reserved.

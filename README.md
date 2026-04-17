# E-Commerce Data Analytics Portfolio
**Organisation:** DecodeLabs (4-Week Developer Training)

## 🚀 Project Overview
This repository contains the end-to-end data science workflow completed during my internship at **DecodeLabs**. The project focuses on learning data science through practical application, transforming raw business data into actionable insights.

The journey progressed through four critical stages of the data lifecycle:
1. **Data Collection & Understanding**
2. **Data Cleaning & Preprocessing**
3. **Exploratory Data Analysis (EDA)**
4. **Data Visualization**

## 🛠️ Tech Stack
* **Language:** Python
* **Libraries:** Pandas (Data Manipulation), Matplotlib & Seaborn (Visualization)
* **Engines:** Openpyxl (Excel Integration)

## 📋 Task Breakdown

### **Task 1: Data Collection & Understanding**
* **Goal:** Load the dataset and identify its structural characteristics.
* **Implementation:** Loaded `Dataset for Data Analytics.xlsx` using Python's raw string path handling.
* **Key Discovery:** Identified the dataset size (total rows and columns) and distinguished between numeric types (`int64`, `float64`) and categorical types (`object`).

### **Task 2: Data Cleaning & Preprocessing**
* **Goal:** Prepare the raw dataset for reliable analysis by managing data quality.
* **Duplicate Handling:** Verified the dataset and removed redundant entries to prevent skewed results.
* **Missing Values:** Addressed a critical gap of **309 missing values** in the `CouponCode` column. These were categorised as "Non-Coupon Transactions" using "Unknown" placeholders to ensure they weren't excluded from the analysis.
* **Formatting:** Standardised the `Date` column into proper Python `datetime` objects to enable future time-series analysis.

### **Task 3 & 4: EDA & Data Visualization**
* **Goal:** Discover patterns, identify trends, and communicate insights clearly through charts.
* **Statistical Patterns:** Calculated basic statistics to understand the distribution of order values (`TotalPrice`).
* **Visual Storytelling:**
    * **Bar Charts:** Identified top-performing products generating the highest revenue.
    * **Line Charts:** Pinpointed specific dates where sales peaked significantly.
    * **Pie Charts:** Visualised the most preferred payment methods among customers.

## 📈 Final Outcome
By completing these tasks, I produced a **100% complete, cleaned dataset** (`Cleaned_Dataset.xlsx`) and a suite of visualisations that answer key business questions. This project serves as a real-world portfolio that showcases my skills in data understanding, preprocessing, and storytelling for future employers.

## 📸 Screenshots

### Task 1 — Dataset Structure & Column Info
![image alt](https://github.com/sumeetmolani/internship_DecodeLabs/blob/3ee05f3a93dd1980b0cdcf8a816f4ee12aab23de/task1_dataset_info.png.png)

### Task 1 — Statistical Summary & Missing Values
![image alt](https://github.com/sumeetmolani/internship_DecodeLabs/blob/3ee05f3a93dd1980b0cdcf8a816f4ee12aab23de/task1_statistical_summary.png.png)

### Task 2 — Data Cleaning Output
![image alt](https://github.com/sumeetmolani/internship_DecodeLabs/blob/3ee05f3a93dd1980b0cdcf8a816f4ee12aab23de/task2_cleaning_output.png.png)

### Task 3 & 4 — Bar Chart: Total Revenue by Product
![image alt](https://github.com/sumeetmolani/internship_DecodeLabs/blob/3ee05f3a93dd1980b0cdcf8a816f4ee12aab23de/task3_bar_chart.png.png)

### Task 3 & 4 — Line Chart: Daily Sales Trend
![image alt](https://github.com/sumeetmolani/internship_DecodeLabs/blob/3ee05f3a93dd1980b0cdcf8a816f4ee12aab23de/task3_line_chart.png.png)

### Task 3 & 4 — Pie Chart: Distribution of Payment Methods
![image alt](https://github.com/sumeetmolani/internship_DecodeLabs/blob/3ee05f3a93dd1980b0cdcf8a816f4ee12aab23de/task3_pie_chart.png.png)

> 📌 *To display these on GitHub, create a `screenshots/` folder in your repo root and upload the images with the filenames shown above.*

## 🔧 How to Run
1. Ensure Python 3.11+ is installed.
2. Install dependencies:
   ```bash
   pip install pandas openpyxl matplotlib seaborn
   ```
3. Update the file path in the scripts to match your local directory.
4. Run the tasks sequentially: `Data Cleaning & Preprocessing.py`, `Data Collection & Dataset Underst.py`, `Data Collection & Dataset Underst.py`.


# 📊 Data Cleaning & Preprocessing – Task 1

## 🎯 Objective
This project is part of my **Data Analyst Internship – Task 1**.  
The objective is to **clean and preprocess a raw dataset** by handling missing values, duplicates, inconsistent formats, and preparing it for analysis.

Dataset used: **Netflix Movies and TV Shows (`netflix_titles.csv`)**

## 📂 Repository Structure

## 🛠 Tools & Libraries
- **Python 3.x**
- **Pandas**
- **NumPy**

## 🔄 Cleaning Steps Performed
1. **Column renaming** → converted to `snake_case`.  
2. **Date formatting** → `date_added` converted to datetime (`dd-mm-yyyy`).  
3. **Duration parsing** → separated into:
   - `duration_int` → numeric value (e.g., 90, 2)  
   - `duration_type` → unit (`minutes` or `seasons`)  
4. **Missing values handling**:
   - `director`, `cast` → filled with `"Unknown"`  
   - `rating` → filled with most common value (mode)  
   - `date_added` → left as `NaT` (unknown)  
5. **Categorical cleaning**:
   - `type` standardized to `"Movie"` / `"TV Show"`  
   - `country` → kept only the first country if multiple were listed  
6. **Feature engineering**:
   - `added_year`, `added_month` → extracted from `date_added`  
   - `title_lower` → lowercase version of title for search  
   - `num_cast` → count of cast members  

## 🚀 How to Run the Script
### 1. Clone this repository
```bash
git clone https://github.com/mahiyikes/data-cleaning-task1.git
cd data-cleaning-task1

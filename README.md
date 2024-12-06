# Data Exploration and Visualization Lab

## Lab Objectives
In this lab, students will:
1. Learn how to perform **data cleaning** on a dataset using Python libraries.
2. Apply **data transformation techniques** to derive meaningful insights from raw data.
3. Create **visualizations** to summarize and analyze the data.
4. Understand how to use **Matplotlib**, **Pandas**, and **NumPy** for data science workflows.


## Lab Instructions
### Task Overview
Students are required to:
1. Load a CSV dataset.
2. Perform data cleaning:
   - Replace missing values with appropriate substitutes.
   - Drop invalid rows.
3. Apply transformations:
   - Calculate the total score from individual scores.
   - Assign grades based on the total score.
   - Add a percentage column to standardize scores.
4. Create visualizations:
   - Bar chart for the number of students by grade.
   - Histogram of total scores.
   - Box plot of percentage scores.


### Requirements
The following Python libraries are required to complete the lab:
- **Matplotlib**: For visualizations.
- **Pandas**: For data manipulation and cleaning.
- **NumPy**: For numerical computations.

To install the required libraries, use:
---```bash
	pip install matplotlib pandas numpy


## Instructions for Reading and Processing the CSV File
Dataset Location: The CSV dataset, student_marks_dataset.csv, is included in the repository. Download it if working locally.

### Loading the Dataset: Use Pandas to load the CSV:
	import pandas as pd
	df = pd.read_csv('student_marks_dataset.csv')

### Data Cleaning:
	Replace missing values using the mean:
	df['column_name'] = df['column_name'].fillna(df['column_name'].mean())

### Drop rows with critical missing values:
	df = df.dropna(subset=['critical_column'])

### Data Transformation:
    - Calculate total scores:
	df['Total Score'] = df[['score1', 'score2', 'score3']].sum(axis=1)

    - Assign grades using conditional logic:
	def assign_grade(score):
		if score >= 475:
			return 'A'
		elif score >= 450:
			return 'A-'
		...
		df['Grade'] = df['Total Score'].apply(assign_grade)

## Creating Visualizations:
 - Example of a bar chart for grades:
	import matplotlib.pyplot as plt
	grade_counts = df['Grade'].value_counts()
	grade_counts.plot(kind='bar')
	plt.show()


### Deliverables
1. A cleaned and transformed dataset (cleaned_student_marks.csv) saved after processing.
2. The following visualizations:
	- Bar chart: Number of students by grade.
	- Histogram: Total score distribution.
	- Box plot: Percentage score distribution.
3. A Python script (main.py) with all code.

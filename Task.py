#Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
def load_dataset(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Dataset successfully loaded.")
        return data
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

# Explore the dataset
def explore_data(df):
    print("First 10 rows of the dataset:")
    print(df.head(10))
    print("\nDataset Summary:")
    print(df.info())
    print("\nMissing or Invalid Values Summary:")
    print(df.isnull().sum())
    print("\nInvalid Values in Scores (Negative Values):")
    print(df[(df['IDS Lab-1 Score'] < 0) | (df['IDS Lab-2 Score'] < 0) | (df['IDS Lab-3 Score'] < 0) | (df['IDS Exam-1 Score'] < 0) | (df['IDS Exam-2 Score'] < 0)])

def clean_data(df):
    numeric_columns = ['IDS Lab-1 Score', 'IDS Lab-2 Score', 'IDS Lab-3 Score', 'IDS Exam-1 Score', 'IDS Exam-2 Score']

    # Replace missing values with the mean for numeric columns
    for col in numeric_columns:
        if col in df.columns:
            mean_value = np.nanmean(df[col])  # NumPy function to calculate mean, ignoring NaNs
            df.loc[:, col] = df[col].fillna(mean_value).round(0).astype(int)  # Convert to integers

    # Handle UFID: Drop rows with missing UFIDs
    print("\nValidating and handling UFID column...")
    if 'UFID' in df.columns:
        # Drop rows where UFID is missing
        df = df.dropna(subset=['UFID']).copy()

        # Ensure UFID is numeric and convert to integer
        df['UFID'] = pd.to_numeric(df['UFID'], errors='coerce')  # Convert to numeric, set invalid to NaN
        df = df.dropna(subset=['UFID']).copy()  # Drop rows with invalid UFIDs
        df['UFID'] = df['UFID'].astype(int)  # Convert UFID to integer

    # Automatically calculate the Total Score
    print("\nCalculating Total Score...")
    df['Calculated Total Score'] = np.sum(df[numeric_columns].values, axis=1)

    # Assign grades based on the calculated total score
    def assign_grade(scores):
        conditions = [
            scores >= 475,
            (scores >= 450) & (scores < 475),
            (scores >= 435) & (scores < 450),
            (scores >= 425) & (scores < 435),
            (scores >= 415) & (scores < 425),
            (scores >= 400) & (scores < 415),
            (scores >= 350) & (scores < 400),
            scores < 350
        ]
        grades = ['A', 'A-', 'B+', 'B', 'B-', 'C', 'D', 'F']
        return np.select(conditions, grades)

    print("\nAssigning Grades...")
    df['Calculated Grade'] = df['Calculated Total Score'].apply(assign_grade)

    # Ensure all relevant columns are integers
    for col in numeric_columns + ['Calculated Total Score']:
        df[col] = df[col].astype(int)

    return df

def transform_data(df):
    #Transformation Column
    df['Percentage Score'] = (df['Calculated Total Score'] / 500 * 100).round(2)

    return df

def create_visualizations(df):
    # Check if the 'Calculated Grade' column exists
    if 'Calculated Grade' not in df.columns:
        raise ValueError("'Calculated Grade' column is missing in the dataset.")

    # Visualization 1: Number of Students by Grade
    grade_counts = df['Calculated Grade'].value_counts().sort_index()
    grade_counts.plot(kind='bar', color='skyblue', title='Number of Students by Grade')
    plt.xlabel('Grade')
    plt.ylabel('Number of Students')
    plt.xticks(rotation=0)
    plt.savefig('students_by_grade.png')
    plt.close()

    # Visualization 2: Distribution of Total Scores
    plt.hist(df['Calculated Total Score'], bins=10, color='green', alpha=0.7, edgecolor='black')
    plt.title('Distribution of Total Scores')
    plt.xlabel('Total Score')
    plt.ylabel('Frequency')
    plt.savefig('total_score_distribution.png')
    plt.close()

    # Visualization 3: Percentage Scores Box Plot
    plt.boxplot(df['Percentage Score'], vert=False, patch_artist=True)
    plt.title('Distribution of Percentage Scores')
    plt.xlabel('Percentage')
    plt.savefig('percentage_score_distribution.png')
    plt.close()

# Main function to execute the workflow
def main():
    file_path = '/content/student_marks_dataset.csv'  # Replace with your actual file path

    print("Loading dataset...")
    # Load the dataset
    df = load_dataset(file_path)
    if df is None:
        print("Dataset loading failed. Exiting workflow.")
        return

    print("\nCleaning the dataset...")
    # Clean the data
    try:
        df = clean_data(df)
        print("\nData cleaned successfully!")
    except ValueError as e:
        print(f"Error during data cleaning: {e}")
        return
    except Exception as e:
        print(f"An unexpected error occurred during data cleaning: {e}")
        return

    print("\nTransforming the dataset...")
    # Apply transformations
    try:
        df = transform_data(df)
        print("\nData transformed successfully!")
    except Exception as e:
        print(f"An unexpected error occurred during data transformation: {e}")
        return

    print("\nDisplaying the first 10 rows of the cleaned and transformed dataset:")
    numeric_columns = ['UFID', 'IDS Lab-1 Score', 'IDS Lab-2 Score', 'IDS Lab-3 Score', 'IDS Exam-1 Score', 'IDS Exam-2 Score', 'Calculated Total Score']
    for col in numeric_columns:
        df[col] = df[col].astype(int)
    print(df.head(10))

    print("\nCreating visualizations...")
    # Create visualizations
    try:
        create_visualizations(df)
        print("\nVisualizations created and saved.")
    except ValueError as e:
        print(f"Error during visualization creation: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during visualization creation: {e}")
        return

    print("\nSaving the cleaned and transformed dataset...")
    # Save the cleaned dataset
    try:
        df.to_csv('cleaned_transformed_student_marks.csv', index=False)
        print("\nData cleaning, transformation, and processing completed. Files saved as 'cleaned_transformed_student_marks.csv'.")
    except Exception as e:
        print(f"An unexpected error occurred while saving the file: {e}")

if __name__ == "__main__":
    main()

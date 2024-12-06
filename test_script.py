import pandas as pd

# Test 1: Check if cleaned dataset exists
try:
    df = pd.read_csv('cleaned_student_marks.csv')
    assert 'Calculated Total Score' in df.columns, "Total Score not calculated correctly"
    assert 'Calculated Grade' in df.columns, "Grade not assigned correctly"
    print("Test 1 Passed: Dataset cleaning and transformations successful")
except Exception as e:
    print(f"Test 1 Failed: {e}")

# Test 2: Check if visualizations are generated
import os
visualizations = [
    'students_by_grade.png',
    'total_score_distribution.png',
    'percentage_score_distribution.png'
]
for vis in visualizations:
    if os.path.exists(vis):
        print(f"Test 2 Passed: Visualization {vis} exists")
    else:
        print(f"Test 2 Failed: Visualization {vis} missing")

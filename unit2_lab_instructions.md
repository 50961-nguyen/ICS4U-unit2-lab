# Student Report Card Analyzer

It's the end of the semester for university and the school needs a program to analyze student report cards! You've been asked to write a Python program that processes student data using strings, lists, tuples, and dictionaries. The lab has three tiers: work through them in order and keep all code in a **single file**.

**File naming:** use the tier you completed, e.g. `unit2_lab_gold.py`  
**Submission:** push your completed file to your GitHub repository in the correct folder.
**See starter code below**

---

## Bronze Tier - Max Grade: 70%

Implement `analyze_name()` which takes a student's full name as a string and returns useful information about it as a **tuple**. 

You will then use **tuple unpacking** in `main()` to print the results.

### `analyze_name()` Details
Given a full name string (e.g. `"Sherlock Holmes  "`), the function should:
1. **Strip** leading/trailing whitespace from the name
2. **Split** the cleaned name into a list of words
3. Count the **total number of vowels** (a, e, i, o, u: case-insensitive) in the full name (ignore spaces)
4. Create an **uppercase initials** using the first letter of each word (e.g. `"SH" for Sherlock Homes`)
5. **Return a tuple** of: `(cleaned_name, word_count, vowel_count, initials)`

### Your Tasks
1. **Write the docstring** for `analyze_name()` — explain what it does, its parameters, and its return value.
2. **Implement the function** 
3. **Call the function in `main()`** and use **tuple unpacking** to store the returned values in separate variables, then print each one.

### Sample Output
```
Welcome to the Student Report Card Analyzer!

Enter student full name:   Sherlock Holmes  
Cleaned Name: Sherlock Holmes
Word Count: 2
Vowel Count: 4
Initals: SH
```

---

## Silver Tier - Max Grade: 85%

Keep all Bronze code. The function `build_seating_chart()` is provided but contains **bugs related to list aliasing and 2D lists**. 

You must **find and fix all the bugs** so the function works correctly.

### What `build_seating_chart()` should do
Given a number of `rows` and `cols`, the function should:
1. Create a 2D list (list of lists) where every seat is initialized to `"empty"`
2. Assign `"Alice"` to seat `[0][0]` (row 0, col 0)
3. Assign `"Bob"` to seat `[1][2]` (row 1, col 2)
4. Create a **separate copy** of the seating chart called `backup` — changes to the original should **not** affect the backup
5. Assign `"Charlie"` to seat `[2][1]` in the **original only**
6. Return both the original and the backup as a tuple

### Your Tasks
1. **Read the code** in `build_seating_chart()` carefully
2. **Identify and fix all 3 bugs** so the function works correctly
3. **Add a comment above each fix** explaining what the bug was and why your fix works
4. **Call the function in `main()`** and use tuple unpacking. Print both the original and backup to show they are independent.

### Sample Output
```
Welcome to the Student Report Card Analyzer!

Enter student full name:   Sherlock Holmes  
Cleaned Name: Sherlock Holmes
Word Count: 2
Vowel Count: 4
Initals: SH

Building Seating Chart...
Original Chart:
  ['Alice', 'empty', 'empty']
  ['empty', 'empty', 'Bob']
  ['empty', 'Charlie', 'empty']
Backup Chart (should NOT have Charlie):
  ['Alice', 'empty', 'empty']
  ['empty', 'empty', 'Bob']
  ['empty', 'empty', 'empty']
```

---

## Gold Tier - Max Grade: 100% (You are on your Own!)

Keep all Bronze and Silver code. Implement `calculate_grade_report()` which uses a **dictionary** to process student grades and produce a summary report.

### How `calculate_grade_report()` works
You are given a dictionary of student names mapped to a **list of their test scores**:
```python
grades = {
    "Alice": [85, 92, 78, 90],
    "Bob": [72, 68, 81, 75],
    "Charlie": [95, 98, 100, 92],
    "Diana": [60, 55, 70, 65]
}
```

The function should:
1. Create a new dictionary called `report` where each student name maps to a **tuple** of `(average, highest_score, lowest_score)`
2. Calculate who has the **highest overall average** and the **lowest overall average**
3. Return a tuple of: `(report, top_student, lowest_student)`

### Your Tasks
1. **Implement `calculate_grade_report()`** — iterate through the dictionary using `.items()`, calculate stats for each student, and build the report dictionary
2. **Call the function in `main()`** with the provided sample data
3. **Print a formatted report** showing each student's average, highest score, and lowest score
4. **Print** who is the top student and who needs the most improvement

### Sample Output
```
Welcome to the Student Report Card Analyzer!

Enter student full name:   Sherlock Holmes  
Cleaned Name: Sherlock Holmes
Word Count: 2
Vowel Count: 4
Initals: SH

Building Seating Chart...
Original Chart:
  ['Alice', 'empty', 'empty']
  ['empty', 'empty', 'Bob']
  ['empty', 'Charlie', 'empty']
Backup Chart: # NOTE THERE SHOULD BE NO CHARLIE!
  ['Alice', 'empty', 'empty']
  ['empty', 'empty', 'Bob']
  ['empty', 'empty', 'empty']

Grade Report:
  Alice   - Avg: 86.3  High: 92   Low: 78
  Bob     - Avg: 74.0  High: 81   Low: 68
  Charlie - Avg: 96.3  High: 100  Low: 92
  Diana   - Avg: 62.5  High: 70   Low: 55

Top Student: Charlie
Needs Improvement: Diana
```

---

## Starter Code

Copy this into your file and work within it. **Do not change function signatures or type annotations.**

```python
# TODO: ADD HEADER COMMENTS


# BRONZE FUNCTION

def analyze_name(full_name: str) -> tuple:
    """
    # TODO: Write a complete docstring.
    """
    # TODO: Implement this function
    pass


# SILVER FUNCTION

def build_seating_chart(rows: int, cols: int) -> tuple:
    """
    Creates a 2D seating chart and a backup copy.
    Assigns students to specific seats in the original.

    Args:
        rows (int): number of rows in the seating chart
        cols (int): number of columns in the seating chart

    Returns:
        tuple: (original_chart, backup_chart)
    """
    # TODO: find the 3 bugs, write the comments above the code to explain the boug, and fix it

    row = ["empty"] * cols
    chart = []
    for i in range(rows):
        chart.append(row)

    chart[0][0] = "Alice"
    chart[1][2] = "Bob"

    backup = chart

    chart[2][1] = "Charlie"

    return chart, backup


# GOLD FUNCTION

def calculate_grade_report(grades: dict) -> tuple:
    """
    Processes a dictionary of student grades and returns a report.

    Args:
        grades (dict): a dictionary where keys are student names (str)
                       and values are lists of test scores (list[int])

    Returns:
        tuple: (report_dict, top_student, lowest_student)
            - report_dict: dict mapping each student to a tuple of (average, highest, lowest)
            - top_student: name of the student with the highest average
            - lowest_student: name of the student with the lowest average
    """
    # TODO: Implement this function
    pass


# ==================== MAIN ====================

def main() -> None:
    """Main function to run the Student Report Card Analyzer."""
    print("Welcome to the Student Report Card Analyzer!\n")

    # Remember to write IPO comments for each tier since each has their own program purpose. 

    # TODO (Bronze): Call analyze_name() and use tuple unpacking to print results

    # TODO (Silver): Call build_seating_chart(3, 3) and print both charts
    # uncomment these lines for testing Silver
    # print("\nBuilding Seating Chart...")

    # TODO (Gold): Call calculate_grade_report() and print the report
    # uncomment these lines for testing Gold
    # print("\nGrade Report:")
    # grades = {
    #     "Alice": [85, 92, 78, 90],
    #     "Bob": [72, 68, 81, 75],
    #     "Charlie": [95, 98, 100, 92],
    #     "Diana": [60, 55, 70, 65]
    # }


if __name__ == '__main__':
    main()
```


# Log Analyzer

## Overview
This is a **Python script** that analyzes log files and summarizes errors by **date** and **type**. It demonstrates practical use of **file handling**, **regex**, and **nested dictionaries** for data aggregation.  

---

## Features
- Reads a `.log` file line by line  
- Extracts **dates** using regex (`YYYY-MM-DD`)  
- Detects **ERROR messages**  
- Counts:  
  - Total errors per date  
  - Number of occurrences of each error message  
- Organizes the data in a **nested dictionary** for easy access and reporting  

---

## Example Output

```python
{
  "2024-03-10": {
    "error_count": 3,
    "Failed to connect to database": 2,
    "Timeout while waiting for response": 1
  },
  "2024-03-11": {
    "error_count": 1,
    "Invalid input": 1
  }
}
```
Learning Goals

Master regex for pattern matching

Practice nested dictionaries for data organization

Strengthen file handling in Python (with open(...))

Build experience with data parsing and aggregation, useful for backend or data tasks

How to Use

Place your log file in a known location.

Update the path in the script:

with open("path/to/your/logfile.log", "r", encoding="utf-8") as file:

Run the script:

python log_analyzer.py

Review the printed nested dictionary showing errors per date and type.

Notes

Works with logs where dates are formatted as YYYY-MM-DD at the beginning of each line

Easily expandable for other log formats or additional filtering

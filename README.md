# Project Workflow: Converting Questions from PDF to Database

This document outlines the process of converting questions from a PDF format to a database using various tools and scripts.

## Steps

### Step 1: Save Questions as PDF
- Start by saving the set of questions in PDF format.

### Step 2: Use Tabula Tool
- Upload the saved PDF to the Tabula tool, which will assist in extracting data from PDF files.

### Step 3: Select Questions for JSON
- In Tabula, select the specific questions that you want to include in the JSON dataset.

### Step 4: Export JSON
- Export the selected questions from Tabula in JSON format.

### Step 5: Run JSON to Excel Code (streamlit.py)
- Execute the "pdf.py" script to convert the JSON data to an Excel spreadsheet for easier manipulation.

### Step 6: Verify Excel Data
- Review the Excel spreadsheet to ensure that the data has been accurately extracted.

### Step 7: Manual Adjustments
- Due to possible issues with incorrect question grouping in Tabula, carefully review the data in Excel and make necessary adjustments.

### Step 8: Load Excel Data into the Database
- Upload the Excel file containing the questions' data into your target database.

## Conclusion
By following these steps, you will be able to efficiently convert questions from a PDF format to a structured database, enabling better organization and accessibility.
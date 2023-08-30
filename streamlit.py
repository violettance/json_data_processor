import streamlit as st
import json
import pandas as pd
import tempfile
import os

class JsonProcessor:
    def __init__(self, json_file):
        self.json_file = json_file
        self.json_data = None
        self.questions = []
        self.options = {'A': [], 'B': [], 'C': [], 'D': [], 'E': []}
    
    def read_json_file(self):
        with open(self.json_file, "r", encoding="utf-8") as file:
            self.json_data = json.load(file)
    
    def extract_questions(self):
        for data in self.json_data:
            question = ''
            for row in data['data']:
                text = row[0]['text']
                if '?' in text:
                    question += text[:text.index('?')+1]
                    break
                else:
                    question += text
            self.questions.append(question)
    
    def extract_options(self):
        for question_data in self.json_data:
            options = {'A': '', 'B': '', 'C': '', 'D': '', 'E': ''}
            for row in question_data['data']:
                text = row[0]['text']
                for option in options:
                    if text.startswith(option + ')'):
                        options[option] += text[len(option) + 2:]
                        break
            for key, value in options.items():
                self.options[key].append(value)
    
    def create_dataframe(self):
        data = {
            'Question': self.questions,
            'A': self.options['A'],
            'B': self.options['B'],
            'C': self.options['C'],
            'D': self.options['D'],
            'E': self.options['E']
        }
        self.df = pd.DataFrame(data)
    
    def export_to_excel(self, excel_file):
        self.df.to_excel(excel_file, index=False)

# Create Streamlit UI
st.title("JSON Data Processor")

# File Upload
uploaded_file = st.file_uploader("Upload JSON File", type=["json"])

# Manual filename input
output_filename = st.text_input("Enter the output Excel file name (e.g., final_output.xlsx):")

if uploaded_file is not None and output_filename:
    # Save the uploaded file to a temporary location
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(uploaded_file.read())
    temp_file_path = temp_file.name

    # Process the uploaded JSON file
    processor = JsonProcessor(temp_file_path)

    processor.read_json_file()
    processor.extract_questions()
    processor.extract_options()
    processor.create_dataframe()

    # Filter out rows with missing values
    filtered_df = processor.df.dropna(subset=['Question'])

    # Export to Excel
    excel_file = "streamlit_test_filtered.xlsx"
    filtered_df.to_excel(excel_file, index=False)

    # Load the modified Excel file
    df = pd.read_excel(excel_file)

    # Remove numbers from the beginning of the first column
    df['Question'] = df['Question'].str.replace(r'^\d+\.\s+', '', regex=True)

    # Save the modified DataFrame back to Excel
    final_output_file = output_filename
    df.to_excel(final_output_file, index=False)

    # Display filtered DataFrame
    st.write(df)

    # Download Button for the final output Excel
    with open(final_output_file, "rb") as f:
        st.download_button(
            label="Download Output",
            data=f.read(),
            file_name=final_output_file,
            key=None,
        )

    # Clean up temporary file
    temp_file.close()
    os.remove(temp_file_path)
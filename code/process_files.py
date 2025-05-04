'''
In this final program, you will re-write your `process_file.py` 
to keep track of the number of files and total number of lines 
that have been processed.

For each file you read, you only need to output the 
summary information eg. "X packages written to file.json".

Screenshot available as process_files.png
'''
import streamlit as st
import packaging
from io import StringIO
import json

st.title("Process Multiple Package Files")

# Initialize session state variables
if 'total_files' not in st.session_state:
    st.session_state.total_files = 0
if 'total_packages' not in st.session_state:
    st.session_state.total_packages = 0

file = st.file_uploader("Upload package file:")

if file:
    filename = file.name
    json_filename = filename.replace(".txt", ".json")
    packages = []
    text = StringIO(file.getvalue().decode("utf-8")).read()
    
    # Count packages in this file
    file_packages = 0
    for line in text.split("\n"):
        line = line.strip()
        if line:  # Only process non-empty lines
            package = packaging.parse_packaging(line)
            packages.append(package)
            file_packages += 1
    
    # Update totals
    st.session_state.total_files += 1
    st.session_state.total_packages += file_packages
    
    # Save JSON file
    with open(f"./data/{json_filename}", "w") as f:
        json.dump(packages, f, indent=4)
    
    # Show summary
    st.success(f"{file_packages} packages written to {json_filename}")
    
    # Display totals
    st.subheader("Totals")
    st.write(f"Files processed: {st.session_state.total_files}")
    st.write(f"Total packages processed: {st.session_state.total_packages}")
    


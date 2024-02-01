# ATS (gemini-pro-vision) with some added features.
---

Create new venv using Conda and activate the venv
---
`conda create -p venv python==3.10`

`conda activate <venv_path>`

Installing required libraries with important "Poppler"
---
`pip install -r requirements.txt`

`conda insall poppler`


Run app.py
---
`streamlit run app.py`

**Note**: 
Add .env file in the same folder with GOOGLE_API_KEY="YOUR-API-KEY"

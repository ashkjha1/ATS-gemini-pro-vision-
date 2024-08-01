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
Add .env file in the same folder with environment variable GOOGLE_API_KEY="YOUR-API-KEY"

To get your own Google API key go to the [Google API](https://makersuite.google.com/app/apikey)



Update: 01-08-2024

Google's Gemini 1.0 Pro Vision model has been deprecated as of July 12, 2024.

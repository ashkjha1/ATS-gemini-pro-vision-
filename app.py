from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os, io
from PIL import Image
import pdf2image
import google.generativeai as genai 
import base64

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def getGeminiResponse(usrInput, pdfContent, prompt):
    model = genai.GenerativeModel("gemini-pro-vision")
    response = model.generate_content([usrInput, pdfContent[0], prompt])
    return response.text

def inputPDFSetup(uploaded_file):
    if uploaded_file is not None:
        #Converting PDF to Image
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        firstPage = images[0]

        #Convert to bytes
        imgByteArr = io.BytesIO()
        firstPage.save(imgByteArr, format="JPEG")
        imgByteArr = imgByteArr.getvalue()

        pdfParts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(imgByteArr).decode()  # encode to base64
            }
        ]
        return pdfParts
    
    else:
        raise FileNotFoundError("No File uploaded")
    

# Streamlit app
    
    
st.set_page_config(page_title="ATS Resume Expert")
st.header("Application Tracking System (ATS)")
choice = st.selectbox(label="Select Job Profile", options=["Data Science", "Data Analyst", "Data Engineering", "Python Developer", "Automation Test Engineer"])
inputText = st.text_area("Job Description: ", key="usrinput")
uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    st.write("File Uploaded Successfully")

submit1 = st.button("Tell Me About The Resume")
submit2 = st.button("Percentage match")

questionText = st.text_input("Ask the Question: ", key="question")
submitQuestion = st.button("Get Answer")

input_prompt1 = f"""
 You are an experienced Technical Human Resource Manager with the experience of about 15-20 years in the field {choice} your task is to review the provided resume against the job description for these profiles. 
1. Please share your professional evaluation on whether the candidate's profile aligns with the role mentioned in {choice}. 
2. Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements with the headings.
Divide the 2nd point into A and B (A for Strengths and B for weakness)
"""

input_prompt2 = f"""
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of job role in {choice} and ATS functionalities, your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches with the job description else return what to learn to increase the match percentage. First the output should come as percentage with the feedback and then keywords missing and last final thoughts.
"""

question_prompt = f"""
Assume you are the person applying to the Job opening based on the work Experience in the Resume and Work related projects answer the question and make sure to not add anything exaggerating from yourself: {questionText}
"""

if submit1:

    if uploaded_file is not None:
        pdf_content=inputPDFSetup(uploaded_file)
        response=getGeminiResponse(input_prompt1,pdf_content,inputText)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content=inputPDFSetup(uploaded_file)
        response=getGeminiResponse(input_prompt2,pdf_content,inputText)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submitQuestion:
    if uploaded_file is not None:
        pdf_content=inputPDFSetup(uploaded_file)
        response=getGeminiResponse(question_prompt,pdf_content,inputText)
        st.subheader("The Answer to the Question is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")
    
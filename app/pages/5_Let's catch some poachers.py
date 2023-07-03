import streamlit as st
import torch
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import os
import pickle
import google_auth_oauthlib.flow
import googleapiclient.discovery
from google.auth.transport.requests import Request
import base64
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import yaml
import requests 


st.set_page_config(
    page_title="Poacher Detector",
    page_icon=":elephant:",
    layout="wide"
)

st.title("Let's catch the poachers")


model = torch.hub.load('/Users/aliyajanmohamed/Downloads/Ironhack/FinalProject/yolov5', 'custom', 
                       path='/Users/aliyajanmohamed/Downloads/Ironhack/FinalProject/yolov5/runs/train/exp18/weights/best.pt',
                       force_reload=True,source='local')

uploaded_file = st.file_uploader("Upload a video", type=["mp4"])


if uploaded_file is not None:
        # Read the video file
        video_np = np.frombuffer(uploaded_file.read(), np.uint8)
        video = cv2.imdecode(video_np, cv2.IMREAD_COLOR)
        #video_bytes = uploaded_file.read()
        #video_np = np.asarray(bytearray(video_bytes), dtype=np.uint8)
        #video = cv2.imdecode(video_np, 1)

        # Process each frame and display predictions
        #for frame in video:
            #processed_frame = process_frame(frame)

            # Display the video
            #st.video(processed_frame)        
        
if uploaded_file is not None:
    video_path = "uploaded_video.mp4"
    with open(video_path, "wb") as file:
        file.write(uploaded_file.getvalue())

    cap = cv2.VideoCapture(video_path)

    target_class = 'poachers'
    email_subject = 'POACHER DETECTED!'
    email_body = 'A poacher has been detected, send in your team NOW!'

    sender_email = 'aliya.janmohamed30@gmail.com'
    receiver_email = 'aliyaironhack@gmail.com'

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'aliya.janmohamed30@gmail.com'
    smtp_password = 'ugfctanhdefpsmmd'


    context = ssl.create_default_context()

    email_sent = False
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame is None:
            continue

        results = model(frame)
        #cv2.imshow('Poacher Detector', np.squeeze(results.render()))
        img = st.image(results.render(), width=1000)

        pred_boxes = results.pandas().xyxy[0]
        detected_classes = pred_boxes['name'].tolist()

        if target_class in detected_classes:

            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = receiver_email
            message['Subject'] = email_subject
            message.attach(MIMEText(email_body, 'plain'))

            if email_sent == False:
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls(context=context)
                    server.login(smtp_username, smtp_password)
                    server.sendmail(sender_email, receiver_email, message.as_string())
                email_sent = True
   

        #st.video('Poacher Detector', frame)
        #cv2.imshow('Poacher Detector', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
        #cv2.destroyAllWindows()

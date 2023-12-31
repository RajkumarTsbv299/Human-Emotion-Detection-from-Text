# -*- coding: utf-8 -*-
"""NLP PROJECT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n0lF7-3ThSJvrttbrEcMMI3qVRsCyZXc
"""

import pandas as pd
import numpy as np

import seaborn as sns

pip install neattext

import neattext.functions as nfx

import sklearn 
from sklearn.linear_model import LogisticRegression 
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

df = pd.read_csv("/content/emotion_dataset_2.csv")

df.head()

df['Emotion'].value_counts()

sns.countplot(x='Emotion',data=df)

dir(nfx)

df['Clean_Text'] = df['Text'].apply(nfx.remove_userhandles)

df['Clean_Text'] = df['Clean_Text'].apply(nfx.remove_stopwords)

df['Clean_Text'] = df['Clean_Text'].apply(nfx.remove_special_characters)

df

Xfeatures = df['Clean_Text']
ylabels = df['Emotion']

x_train,x_test,y_train,y_test = train_test_split(Xfeatures,ylabels,test_size=0.4,random_state=42)

from sklearn.pipeline import Pipeline

pipe_lr = Pipeline(steps=[('cv',CountVectorizer()),('lr',LogisticRegression())])

pipe_lr.fit(x_train,y_train)

pipe_lr.score(x_test,y_test)

pipe_lr

ex1 = "The product is fantastic as expected from realme thanks to flipkart😊😊 the front cam is very nice and the rear one is pretty good performance is nice too smooth and the case quality is also nice... It's a value for money product"

pipe_lr.predict([ex1])

pipe_lr.predict_proba([ex1])

pipe_lr.classes_

import joblib
pipeline_file = open("emotion_classifier_pipe_lr.pkl","wb")
joblib.dump(pipe_lr,pipeline_file)
pipeline_file.close()

pip install streamlit

pip install altair

pip install joblib

pip install gTTS

pip install langdetect

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py 
# import streamlit as st
# import altair as alt
# import joblib
# import pandas as pd
# import numpy as np
# from gtts import gTTS 
# from IPython.display import Audio
# from langdetect import detect
# pipe_lr=joblib.load(open("emotion_classifier.pkl","rb"))
# def predict_emotions(docx):
#     results=pipe_lr.predict([docx])
#     return results[0]
# def get_prediction_proba(docx):
#     results=pipe_lr.predict_proba([docx])
#     return results
# emotions_emoji_dict = {"anger":"😠","disgust":"🤮", "fear":"😨😱", "happy":"🤗", "joy":"😂", "neutral":"😐", "sad":"😔", "sadness":"😔", "shame":"😳", "surprise":"😮"}
# def main():
#     st.title("Text Emotion Recognition System")
#     menu=["Home","About"]
#     choice=st.sidebar.selectbox("Menu",menu)
#     if choice=="Home":
#         st.subheader("Enter the text for emotion prediction")
#         with st.form(key='emotion_clf_form'):
#             raw_text=st.text_area("Type Here")
#             submit_text=st.form_submit_button(label='Submit')
# 
#         if submit_text:
#             col1,col2,col3=st.columns(3)
#             prediction=predict_emotions(raw_text)
#             probability=get_prediction_proba(raw_text)
#             with col1:
#                 st.success("Original Text")
#                 st.write(raw_text)
# 
#                 st.success('Prediction')
#                 
#                 emoji_icon=emotions_emoji_dict[prediction]
#                 st.write("{}:{}".format(prediction,emoji_icon))
#                 st.write("Confidence:{}".format(np.max(probability)))
#             with col2:
#                 st.success("Prediction Probability")
#                 st.write(probability)
#                 proba_df=pd.DataFrame(probability,columns=pipe_lr.classes_)
#                 st.write(proba_df.T)
#                 proba_df_clean=proba_df.T.reset_index()
#                 proba_df_clean.columns=["emotions","probability"]
# 
#                 fig=alt.Chart(proba_df_clean).mark_bar().encode(x='emotions',y='probability',color='emotions')
#                 st.altair_chart(fig,use_container_width=True)
#             with col3:
#                 st.success("Audio")
#                 tts = gTTS(raw_text)
#                 tts.save('1.wav')
#                 sound_file = '1.wav'
#                 Audio(sound_file,autoplay=True)
#                 audio1 = open("1.wav", "rb")
#                 st.audio(audio1)
#     if choice=="About":
#         from PIL import Image
#         image = Image.open('logo1.png')
#         st.image(image, caption='NLP')
# 
# def add_bg_from_url():
#     st.markdown(
#          f"""
#          <style>
#          .stApp {{
#              background-image: url("https://garden.spoonflower.com/c/9488458/p/f/m/KSfPv4WgxTcnXDXjxrmWy7s6M1ucitW-StC-E41r9greBWad2pc/Medium%20Dark%20Cyan%20Blue%20Clear%20Spring%20Seasonal%20Color%20Palette.jpg");
#              background-attachment: fixed;
#              background-size: cover
#          }}
#          </style>
#          """,
#          unsafe_allow_html=True
#      )
# 
# add_bg_from_url() 
#           
# if __name__=='__main__':
#     main()

!streamlit run app.py & npx localtunnel --port 8501
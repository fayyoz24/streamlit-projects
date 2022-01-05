import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px
dataFrameSerialization = "legacy"

st.markdown("<h1 style='text-align: center; color: blue;'>FRIDAY CHALLENGE!</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: blue;'>OBESITY PROBLEM</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: red;'>What is Obesity? 🤔</h1>", unsafe_allow_html=True)
# gender_select = st.sidebar.selectbox("choose gender!", ("about data", "Male", "Female"))
# bmi_select = st.sidebar.selectbox("Obesity by index", ('bmi', 0, 1, 2, 3, 4))

img = Image.open("sampl.jpg")
st.image(img, width=700)
video = open("obesity.mp4", 'rb').read()
st.video(video)


df = pd.read_csv("https://raw.githubusercontent.com/chriswmann/datasets/master/500_Person_Gender_Height_Weight_Index.csv", index_col=False)
st.write(df)
# gender = st.multiselect('Which Gender would you like to see',
#             gend_opt, 0)

gen = df["Gender"].unique().tolist()
gen.append('Both')
gender_opt = st.sidebar.selectbox('which gender would you like to see',
            gen, 0)

male_df = df[(df['Gender']=='Male')]
female_df = df[(df['Gender']=='Female')]
a = male_df
if gender_opt == 'Female':
    a = female_df
if gender_opt == 'Both':
    a = df
if gender_opt == 'Male':
    a = male_df
fig = px.scatter(a, x= 'Weight', y= 'Height',
        size='Index',
        color ='Index', hover_name='Index',
        log_x=True, size_max=30, range_x=[40, 180], 
        range_y=[130, 210])
fig.update_layout(width=800)
st.write(fig)

describ = st.sidebar.selectbox('which gender description',
        gen, 0)
desc = df.describe()
if describ == 'Male':
    desc = male_df.describe()
if describ == 'Female':
    desc = female_df.describe()
if describ == 'Both':
    desc = df.describe()
fig1 = px.scatter(desc, x= 'Weight', y= 'Height',
        color = desc.index, hover_name=desc.index,
        log_x=True, size_max=30, range_x=[30, 180], 
        range_y=[10, 210])

# df1 = df1.astype(str)
print(df.head(1))
fig1.update_layout(width=800)
st.write(fig1)
# df['Index'] = df['Index'].replace([0,1,2,3,4,5], ['Extremely Weak','Weak','Normal','Overweight','Obesity','Extreme Obesity'])
# groups = df.groupby('Index')
# male_df = df[(df['Gender']=='Male')]
# male_df = male_df.astype(str)


# df['Index'] = df['Index'].replace([0,1,2,3,4,5], ['Extremely Weak','Weak','Normal','Overweight','Obesity','Extreme Obesity'])
# groups = df.groupby('Index')
# female_df = df[(df['Gender']=='Female')]










# def gender_sel(gender_select):
#     if gender_select == 'about data':
#         st.header("There is given collected some data about 500 samples of people.")
#         st.header("Information about the weight, the height, the gender and the BMI of the person.")   
#         st.line_chart(df['Height'])
#         img1 = Image.open("about_data.png")
#         st.image(img1, width=700)
#         st.header("MEAN points")
#         img6 = Image.open("abou_H_W.png")
#         st.image(img6, width=700)

#     elif gender_select == 'Male':
#         st.header("The Males Height and Weight correlation.")
#         img2 = Image.open("Males.png")
#         st.image(img2, width=700)
#         st.header("The Males Height")
#         st.text('The maximum Height of men is 199 sm')
#         st.text('The minimum Height of men is 140 sm')
#         img4 = Image.open("Males_H.png")
#         st.image(img4, width=700)
#         st.header("The Males Weight")
#         st.text('The maximum Weight of men is 160 kg')
#         st.text('The minimum Weight of men is 50 kg')
#         img5 = Image.open("Males_W.png")
#         st.image(img5, width=700)
#     elif gender_select == 'Female':
#         st.header("The Females Height and Weight correlation.")
#         img3 = Image.open("Females.png")
#         st.image(img3, width=700)
#         st.header("The Females Weight.")
#         img6 = Image.open("img6.png")
#         st.image(img6, width=700)
#         st.header("The Females Height")
#         img7 = Image.open("img7.png")
#         st.image(img7, width=700)
# gender_sel(gender_select)
# def bmi(bmi_select):
#     if bmi_select == 0:
#         st.title("Extremely Weak")
#         st.header("we have 13 cases like that")
#         st.header("6 of them are MALE")
#     elif bmi_select == 1:
#         st.title("Weak")
#         st.header("we have 22 cases like that")
#         st.header("15 of them are MALE")
#     elif bmi_select == 2:
#         st.title("Normal")
#         st.header("we have 69 cases like that")
#         st.header("28 of them are MALE")
#     elif bmi_select == 3:
#         st.title("Overweight")
#         st.header("we have 68 cases like that")
#         st.header("32 of them are MALE")
#     elif bmi_select == 4:
#         st.title("Extremely Weak")
#         st.header("we have 130 cases like that")
#         st.header("59 of them are MALE")

#     elif bmi_select == 5:
#         st.title("Extremely Weak")
#         st.header("we have 198 cases like that")
#         st.header("105 of them are MALE")

#     elif bmi_select == 'bmi':
#         st.header("Body Mass Index is a simple calculation using a person's height and weight")

# bmi(bmi_select)

about = st.sidebar.button("contributors")
if about:
    st.title("Fayyozjon Usmonov")
    st.title("Vishwanath Singa")
    st.title("Issifu Siaw Awudu")
    st.markdown("<h1 style='text-align: center; color: blue;'>Thanks for your attention!</h1>", unsafe_allow_html=True)
      

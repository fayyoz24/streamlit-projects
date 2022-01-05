import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

data = pd.read_csv('Solar_prediction.csv')
#data.Time = data.Time.split('12:00:00 AM')
data['Data'] = data['Data'].map(lambda x: x.rstrip('12:00:00 AM')).add(' ')
data['Data_Time'] = data["Data"] + data['Time']
data = data.drop(['Data', 'Time'], axis=1)




year_options = data['Data_Time']
data['Data_Time'] = pd.to_datetime(data['Data_Time']).dt.strftime('%Y-%m-%d %H:%M:%S')

st.write(data)
date_options = data['Data_Time'].unique().tolist()
date = st.selectbox('Which date would you like?', date_options, 1)
#options = [data['Humidity'], data['Speed']]
#option = st.multiselect('hjk', options, 'Speed')
#data = data.columns.isin(option)
fig = px.bar(data[:50], x='Speed', y='Humidity',

             animation_frame = 'Data_Time', animation_group='Speed')
st.write(fig)

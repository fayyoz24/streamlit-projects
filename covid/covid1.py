import pandas as pd
import streamlit as st
import plotly.express as px


#data = pd.read_csv('cov19.csv')

df = px.data.gapminder()
st.write(df)     # to print the whole data
year_options = df['year']
year = st.selectbox('Which year', year_options,1) #selecting the yaer starting with zero index


fig = px.scatter(df, x="gdpPercap", y="lifeExp",
            size="pop", color="continent", hover_name="continent",
            log_x=True, size_max=55, range_x=[100, 100000], range_y=[25,90],
            animation_frame = 'year', animation_group='country')

fig.update_layout(width=800) # to change the size of thr figure

st.write(fig) # to print it in our st

cov = pd.read_csv('cov19.csv', index_col=0)
print(cov.head(3))
#cov1 = cov.reset_index(drop=True)
cov.columns = ['Country', 'Code', 'Date', 'Confirmed', 'Days since confirmed']
cov["Date"]=pd.to_datetime(cov['Date']).dt.strftime('%Y-%m-%d')
#print(cov.columns)
country_options = cov['Country'].unique().tolist()

#st.write(cov)

date_options = cov["Date"]

date = st.selectbox("WHich date would you like to see?", date_options, 0)
country = st.multiselect('which country', country_options, "Uzbekistan")

cov = cov[cov['Country'].isin(country)]
cov = cov[cov['Date']==date]

fig2 = px.bar(cov, x='Country', y='Confirmed', color="Country", range_y=[0, 35000],
animation_frame = 'Date', animation_group='Country')

fig2.update_layout(width=800)

st.write(fig2)
#st.plotly_chart(fig2)

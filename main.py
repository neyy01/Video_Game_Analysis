import streamlit as st
import streamlit as st
import pandas as pd
from visualization import *

def readData():
    Video_Games = pd.read_csv('vgsales.csv')
    Video_Games.rename(columns={'Platform':'Plateform'}, inplace=True)
    Video_Games['Year'] = Video_Games['Year'].fillna(0).astype('int')
    return Video_Games



df = readData()


sidebar = st.sidebar

sidebar.title('User Options')


def introduction():
    st.image('gaming.png', use_column_width=True)
    st.markdown("""
        ## Heading Level 2
        - Feature 1
        - Feature 2
        - Feature 3
    """)

    c1, c2 = st.columns(2)

    c1.header("Column 1 Content")
    c2.header("Column 2 Content")


def execute():
    
    st.image('image.png', use_column_width=True)
    st.subheader('project working here')
    st.dataframe(df)

    # sales in numbers

    st.title("Sales in Various Regions")
    start, end = st.slider("Double Ended Slider",value=[2005,2008], min_value=1980, max_value=2020)
    selRegion = st.selectbox("Select Region", ['NA_Sales', 'EU_Sales', 'JP_Sales','Other_Sales','Global_Sales'])
    year_count = (i for i in range(start,end))
    count_in_range = df.loc[df['Year'].isin(year_count)] 
    ns = sum(count_in_range[selRegion])
    st.header(round(ns),)

    # Genre in various regions

    st.title("Top Genre in Various Regions")
    genregion = st.selectbox("Select Regions", ['NA_Sales', 'EU_Sales', 'JP_Sales','Other_Sales','Global_Sales'])
    data = df.groupby('Genre', as_index=False).sum().sort_values('NA_Sales', ascending=False)
    #st.dataframe(data)
    fig = plotBar(data, 'Genre', genregion)
    st.plotly_chart(fig, use_container_width=True)

    # Top 10 Publishers in various regions

    st.title("Top 10 Publishers in Various Regions")
    pubregion = st.selectbox("Select any Regions", ['NA_Sales', 'EU_Sales', 'JP_Sales','Other_Sales','Global_Sales'])
    data = df.groupby('Publisher', as_index=False).sum().sort_values('NA_Sales', ascending=False).head(10)
    
    fig = plotBar(data,'Publisher', pubregion)
    st.plotly_chart(fig, use_container_width=True)

    #Top 10 publishers in game count

    st.title("Top 10 Publishers in Game Count ")
    gcregion = st.selectbox("Select one Regions", ['NA_Sales', 'EU_Sales', 'JP_Sales','Other_Sales','Global_Sales'])
    data = df.groupby('Publisher', as_index=False).count().sort_values('NA_Sales', ascending=False).head(10)

    fig = plotBar(data,'Publisher', gcregion)
    st.plotly_chart(fig, use_container_width=True)

    # Top 10 Video Games by Sales

    st.title('Top 10 Video Games by Sales')
    top_10_sales = st.selectbox("Select any option", ['NA_Sales', 'EU_Sales', 'JP_Sales','Other_Sales','Global_Sales'])
    data = df.groupby('Publisher', as_index=False).sum().sort_values('NA_Sales', ascending=False).head(10)

    fig = plotBar(data,'Publisher', top_10_sales)
    st.plotly_chart(fig, use_container_width=True)

    # No. of games published per year

    st.title('No. of Games Published Per Year')
    data = df.groupby('Year', as_index=False).count().sort_values('Year',ascending=True)[df['Year']!=0]
    #st.dataframe(data)
    fig = plotLine(data, 'Year', 'Publisher')
    st.plotly_chart(fig, use_container_width=True)
    


    # top 10 plateforms

    st.title('Top 10 Platforms Per Year')
    top_10_plt = st.selectbox("Select any one option", ['NA_Sales', 'EU_Sales', 'JP_Sales','Other_Sales','Global_Sales'])
    data = df.sort_values('NA_Sales').head(10)

    fig = plotLine(data,'Plateform', top_10_plt)
    st.plotly_chart(fig, use_container_width=True)
    
    
    #sizes = [15, 30, 45, 10]
    

    st.title('Top 10 Genre in the US')
    fig=plotPie(data,['NA_Sales', 'EU_Sales', 'JP_Sales','Other_Sales','Global_Sales'])

    st.plotly_chart(fig, use_container_width=True)
    
    
    # Top 10 Genre in North America
    st.title('Top 10 Genre in the US')
    top_us = df.sort_values('NA_Sales', ascending=False)
    top_us_genre = top_us.Genre.value_counts()
    fig = plotPie(data,top_us_genre)
    st.plotly_chart(fig, use_container_width=True)


    

options = ['Project Introduction', 'Execution']

selOption = sidebar.selectbox("Select an Option", options)

if selOption == options[0]:
    introduction()
elif selOption == options[1]:
    execute()
import streamlit as st
import streamlit as st
import pandas as pd
from visualization import *
import plotly.graph_objs as go

def readData():
    Video_Games = pd.read_csv('vgsales.csv')
    Video_Games.rename(columns={'Platform':'Plateform'}, inplace=True)
    Video_Games['Year'] = Video_Games['Year'].fillna(0).astype('int')
    return Video_Games



df = readData()


sidebar = st.sidebar

sidebar.title('User Options')


def introduction():
    st.image('vg.gif', width=None)
    st.markdown("""
        ## EDA and Viz. of Video Games Sales data
    
    Name : HARSHIT KUMAR
    \nQualification : Bachelor of Business Administration(BBA)
    \nStream : Management 
    \nUniversity : University of Lucknow
    \nLocation : Lucknow, INDIA
    \nThis Project is to perform the analysis on the Video Games Sales dataset. Here we use various libraries of Python for visualization of Data. The Dataset which is Used in Project is from Data World (👈 Click to Download)
        
        - The Libraries I used in Project are:

            Matplotlib Explore here
            Seaborn Explore here
            Plotly Explore here  
            Pandas Explore here
            Streamlit Explore here
        
        - Their Following Tasks are Implemented in the Project:

            Data Preparation and Cleaning
            Exploratory Analysis and Visualization
            Asking and Answering Questions
            Inferences and Conclusion
            References and Future Work

    """)

    c1, c2 = st.columns(2)

    c1.header("Column 1 Content")
    c2.header("Column 2 Content")


def execute():
    
    st.image('image.png')
    st.markdown("""# Let's Begin Our Analysis""")
    st.dataframe(df)

    st.markdown("""
       - ##### 500 games are ranked based on their sales in millions
       - ##### Games released between 1980 to 2020""")


    # sales in numbers

    st.markdown("## Sales in Various Regions")
    start, end = st.slider("Double Ended Slider",value=[2005,2008], min_value=1980, max_value=2020)
    selRegion = st.selectbox("Select Region", ['NA_Sales', 'EU_Sales', 'JP_Sales','Other_Sales','Global_Sales'])
    year_count = (i for i in range(start,end))
    count_in_range = df.loc[df['Year'].isin(year_count)] 
    ns = sum(count_in_range[selRegion])
    st.header(round(ns))

    st.markdown(""" 
    - With the Help of Above Slider (in years):

            - As seen in the above Slider, you can select any range Start and End.
            - Then Select any Region, and it Shows the Total No. of sales(in millions)""")

    # Genre in various regions

    st.markdown("## Top Genre in Various Regions")
    genregion = st.selectbox("Select Regions", ['NA_Sales', 'EU_Sales', 'JP_Sales','Other_Sales','Global_Sales'])
    data = df.groupby('Genre', as_index=False).sum().sort_values('NA_Sales', ascending=False)
    #st.dataframe(data)
    fig = plotBar(data, 'Genre', genregion)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(""" 
    - With the Help of Above Selectbox Region(in sales):

            - As seen in the above Dropdown selectbox, you can select any Region.
            - Then it shows the Top Genre from that Selcted Region.
            - it Seems Action Genre is most Popular in Most Regions""")

    # Top 10 Publishers in various regions

    st.markdown("## Top 10 Publishers in Various Regions")
    pubregion = st.selectbox("Select any Regions", ['NA_Sales', 'EU_Sales', 'JP_Sales','Other_Sales','Global_Sales'])
    data = df.groupby('Publisher', as_index=False).sum().sort_values('NA_Sales', ascending=False).head(10)
    
    fig = plotBar(data,'Publisher', pubregion)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(""" 
    - With the Help of Above Selectbox Region(in sales):

            - As seen in the above Dropdown selectbox, you can select any Region.
            - Then it shows the Top Publishers from that Selcted Region.""")
    

    #Top 10 publishers in game count

    st.markdown("## Top 10 Publishers in Game Count ")
    gcregion = st.selectbox("Select one Regions", ['NA_Sales', 'EU_Sales', 'JP_Sales','Other_Sales','Global_Sales'])
    data = df.groupby('Publisher', as_index=False).count().sort_values('NA_Sales', ascending=False).head(10)

    fig = plotBar(data,'Publisher', gcregion)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(""" 
    - With the Help of Above Selectbox Region(in sales):

            - As seen in the above Dropdown selectbox, you can select any Region.
            - Then it shows the Top 10 Publishers in Game Count from that Selcted Region.""")

    # Top 10 Video Games by Sales

    st.markdown('## Top 10 Video Games by Sales')
    top_10_sales = st.selectbox("Select any option", ['NA_Sales', 'EU_Sales', 'JP_Sales','Other_Sales','Global_Sales'])
    data = df.groupby('Publisher', as_index=False).sum().sort_values('NA_Sales', ascending=False).head(10)

    fig = plotBar(data,'Publisher', top_10_sales)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(""" 
    - With the Help of Above Selectbox Region(in sales):

            - As seen in the above Dropdown selectbox, you can select any Region.
            - Then it shows the Top 10 Video Game by Sales from that Selcted Region.
            - it Seems that Nintendo is most Popular Game in Most Regions""")

    # No. of games published per year

    st.markdown('## No. of Games Published Per Year')
    data = df[df['Year'] != 0].groupby('Year', as_index=False).count()
    #st.dataframe(data)
    fig = plotLine(data, 'Year', 'Publisher')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    - Observations Based on above linear Graph 

            - As seen in the graph above video-game sales peaked in 2005-2010 across the globe.
            - With the Highest of 1428 millions Game were sold.""")


    # Most popular Genre
    st.markdown('## Most Popular Genre Globally')
    data1 = df.groupby('Genre', as_index=False).count()
    fig= px.pie(data1, labels='Genre', values='Rank', names='Genre')

    data3 = df[df['Year']!=0].groupby('Year', as_index=False).sum()
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    - Observations Based on above Pie Chart 

            - As seen in the graph above, Action Genre is the Highest across the globe.
            - so this Data Shows People like more Action Games related to any other.""")

    
    
    # Various Sales in years according to their Regions
    
    st.markdown('## Sales in Various Regions')
    data = df[df['Year'] != 0].groupby('Year', as_index=False).count()
    px.line(data, 'Year', 'Name')

    fig = go.Figure()
    fig.add_trace(go.Line(x = data3.Year, y = data3.NA_Sales, name="NA Sales"))
    fig.add_trace(go.Line(x = data3.Year, y = data3.EU_Sales, name="EU Sales"))
    fig.add_trace(go.Line(x = data3.Year, y = data3.JP_Sales, name="JP Sales"))
    fig.add_trace(go.Line(x = data3.Year, y = data3.Other_Sales, name="Other Sales"))
    fig.add_trace(go.Line(x = data3.Year, y = data3.Global_Sales, name="Global Sales"))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    - Observations Based on above linear Graph 

            - As seen in the graph above video-game sales from 1980-2020 across the globe.
            - as you can see in 2008 it was the Highest of all time sales with 678.9 million.""")



options = ['Project Introduction', 'Execution']

selOption = sidebar.selectbox("Select an Option", options)

if selOption == options[0]:
    introduction()
elif selOption == options[1]:
    execute()
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Teams', 
                   page_icon='⛹️', 
                   layout='wide')

tab1, tab2, tab3 = st.tabs(["Offensive", "Defensive", "Specific"])

df_times = pd.read_csv('/home/bruno/repos/aulas_Streamlit_teste/data/df_times.csv', index_col=0)


with tab1:
    with st.container():
        st.title("Teams Offensive View")
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        no_of_teams = df_times.index.nunique()
        most_PTS = df_times['PTS'].idxmax()
        most_3PM = df_times['3PM'].idxmax()
        most_2PM = df_times['2PM'].idxmax()
        most_FTP = df_times['FT%'].idxmax()
        
        col1.metric(label='No of teams',
                      value=no_of_teams)
        col2.metric(label='Most PTS',
                      value=most_PTS)
        col3.metric(label='Most 3PM',
                      value=most_3PM)
        col4.metric(label='Most 2PM',
                      value=most_2PM)
        col5.metric(label='Most FT%',
                      value=most_FTP)
    
    with st.container():
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig1 = px.bar(data_frame=df_times,
                    y=df_times.index,
                    x='PTS',
                    orientation='h',
                    color=df_times.index,
                    template='plotly_dark',
                    height=850).update_layout(title='Total points made per team', 
                                                          xaxis_title='Points made by all players', yaxis_title='Team', showlegend=False,
                                                          title_x=0.35,
                                                          yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            
            st.write('')
            st.write('')
            
            TPP_max=int(df_times['3P%'].max())
            FGP_max=int(df_times['FG%'].max())
            TPP_max=int(df_times['2P%'].max())
            FT_max=int(df_times['FT%'].max())
            
            st.dataframe(df_times[['3P%', 'FG%', '2P%', 'FT%']],
                        height=800,
                        column_config={
                            "3P%": st.column_config.ProgressColumn(format='%f', min_value=0, max_value=TPP_max),
                            "FG%": st.column_config.ProgressColumn(format='%f', min_value=0, max_value=FGP_max),
                            "2P%": st.column_config.ProgressColumn(format='%f', min_value=0, max_value=TPP_max),
                            "FT%": st.column_config.ProgressColumn(format='%f', min_value=0, max_value=FT_max)
                        })
with tab2:
    
    with st.container():
        st.title('Teams Defensive View')
        col1, col2, col3, col4, col5 = st.columns(5)
        
        no_of_teams = df_times.index.nunique()
        most_DREB = df_times['DREB'].idxmax()
        most_STL = df_times['STL'].idxmax()
        most_BLK = df_times['BLK'].idxmax()
        most_PF = df_times['PF'].idxmax()
        
        col1.metric(label='No of teams',
                        value=no_of_teams)
        col2.metric(label='Most DREB',
                        value=most_DREB)
        col3.metric(label='Most STL',
                        value=most_STL)
        col4.metric(label='Most BLK',
                        value=most_BLK)
        col5.metric(label='Most PF',
                        value=most_PF)

    with st.container():
        
        col1, col2 = st.columns(2)
        
        with col1:
            
            fig2 = px.bar(data_frame=df_times,
                          x='defensive',
                          y=df_times.index,
                          color=df_times.index,
                          orientation='h',
                          template='plotly_dark',
                          height=800).update_layout(title='Total defensive acts per team',
                                                    xaxis_title='Defensive acts made',
                                                    yaxis_title='Team',
                                                    showlegend=False,
                                                    title_x=0.35,
                                                    yaxis={'categoryorder':'total ascending'})
                          
            st.plotly_chart(fig2, use_container_width=True)
            
        with col2:
            
            st.write('')
            st.write('')            
            DREB_max=int(df_times['DREB'].max())
            STL_max=int(df_times['STL'].max())
            BLK_max=int(df_times['BLK'].max())
            PF_max=int(df_times['PF'].max())
            
            st.dataframe(df_times[['DREB', 'STL', 'BLK', 'PF']],
                            height=1080,
                        column_config={
                            "DREB": st.column_config.ProgressColumn(format='%f', min_value=0, max_value=DREB_max),
                            "STL": st.column_config.ProgressColumn(format='%f', min_value=0, max_value=STL_max),                        
                            "BLK": st.column_config.ProgressColumn(format='%f', min_value=0, max_value=BLK_max),
                            "PF": st.column_config.ProgressColumn(format='%f', min_value=0, max_value=PF_max)
                        })

with tab3:
    teams = df_times.index.unique().sort_values()
    st.title('Single Team View')
    team = st.selectbox(label='Select a team',
                 options=teams)
    col1, col2 = st.columns([1,6])

    # Trocar o link da logo e o nomes do time por um selecionador de time e filtro a partir dele
    link_logo = df_times[df_times.index == team]['Logo'][0]
    nome_time = df_times[df_times.index == team]['Names'][0]

    with col1: 
        st.markdown(f'![]({link_logo})')
        
    with col2:
        st.markdown(f'## {nome_time}')
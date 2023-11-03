import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Teams', 
                   page_icon='⛹️', 
                   layout='wide')

tab1, tab2, tab3 = st.tabs(["Offensive", "Defensive", "Specific"])

df_times = pd.read_csv('/home/bruno/repos/aula_dsfame/data/df_times.csv', index_col=0)

df_jogadores = pd.read_csv('/home/bruno/repos/aula_dsfame/data/df_jogadores.csv')

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
            off_00 = px.bar(data_frame=df_times,
                    y=df_times.index,
                    x='PTS',
                    orientation='h',
                    color=df_times.index,
                    template='plotly_dark',
                    height=850).update_layout(title='Total points made per team', 
                                                          xaxis_title='Points made by all players', yaxis_title='Team', showlegend=False,
                                                          title_x=0.35,
                                                          yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(off_00, use_container_width=True)
        
        with col2:
            
            st.write('')
            st.write('')
            
            max_3PP = df_times['3P%'].max()
            max_FGP = df_times['FG%'].max()
            max_2PP = df_times['2P%'].max()
            max_FT = df_times['FT%'].max()
            
            st.dataframe(df_times[['3P%', 'FG%', '2P%', 'FT%']],
                        height=800,
                        column_config={
                            "3P%": st.column_config.ProgressColumn(format='%f', min_value=0, max_value=max_3PP),
                            "FG%": st.column_config.ProgressColumn(format='%f', min_value=0, max_value=max_FGP),
                            "2P%": st.column_config.ProgressColumn(format='%f', min_value=0, max_value=max_2PP),
                            "FT%": st.column_config.ProgressColumn(format='%f', min_value=0, max_value=max_FT)
                        })
        
        off_01 = px.scatter(data_frame=df_times,
                            x = '2PM',
                            y = '3PM', 
                            color = df_times.index,
                            template='plotly_dark',
                            opacity=0.6,
                            title='3PM and 2PM by all players per team').update_traces(marker_size=40)
        st.plotly_chart(off_01, use_container_width=True)
        
        off_02 = px.scatter(df_times,
                            y='3P%', 
                            x='2P%',
                            template='plotly_dark',
                            color=df_times.index,
                            title='Mean 3P percentage vs 2P percentage for all players per team',
                            opacity=0.6).update_traces(marker_size=40)
        st.plotly_chart(off_02, use_container_width=True)
        
        
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
            
            def_00 = px.bar(data_frame=df_times,
                          x='defensive',
                          y=df_times.index,
                          color=df_times.index,
                          orientation='h',
                          template='plotly_dark',
                          height=850).update_layout(title='Total defensive acts per team',
                                                    xaxis_title='Defensive acts made',
                                                    yaxis_title='Team',
                                                    showlegend=False,
                                                    title_x=0.35,
                                                    yaxis={'categoryorder':'total ascending'})
                          
            st.plotly_chart(def_00, use_container_width=True)
            
        with col2:
            
            st.write('')
            st.write('')            
            DREB_max=int(df_times['DREB'].max())
            STL_max=int(df_times['STL'].max())
            BLK_max=int(df_times['BLK'].max())
            PF_max=int(df_times['PF'].max())
            
            st.dataframe(df_times[['DREB', 'STL', 'BLK', 'PF']],
                            height=800,
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

    link_logo = df_times[df_times.index == team]['Logo'][0]
    nome_time = df_times[df_times.index == team]['Names'][0]

    
    with st.container():
        with col1: 
            st.markdown(f'![]({link_logo})')
        
        with col2:
            with st.container():
                st.markdown(f'## {nome_time}')
                
                team_row = df_times[df_times.index == team]
                
                col1, col2, col3, col4, col5, col6 = st.columns(6)
                col1.metric(label='Points', value=team_row['PTS'])
                col2.metric(label='Assists', value=team_row['AST'])
                col3.metric(label='Rebounds', value=team_row['REB'])
                col4.metric(label='Steals', value=team_row['STL'])
                col5.metric(label='Blocks', value=team_row['BLK'])
                col6.metric(label='Turnovers', value=team_row['TOV'])
        
        with st.container():
            
            col1, col2 = st.columns([2, 4])
            selected_team_df = df_jogadores[df_jogadores['Team']==team]
            
            spec_04 = px.histogram(data_frame=df_jogadores[df_jogadores['Team'] == 'BOS'],
                                   x='POS',
                                   template='plotly_dark',
                                   color='POS')
            col1.plotly_chart(spec_04, use_container_width=True)
            
            spec_00 = px.pie(data_frame=selected_team_df,
                             names='POS',
                             values='PTS',
                             hole=0.5,
                             template='plotly_dark',
                             title='Points per player position'
                             ).update_layout(title_x=0.23)
            col1.plotly_chart(spec_00, use_container_width=True)
            
            spec_01 = px.scatter(data_frame=selected_team_df, 
                                y='3PM',
                                x='2PM',
                                size='GP',
                                hover_data='PName',
                                template='plotly_dark',
                                title='3PM versus 2PM with size prportional to the Games Played',
                                height=400).update_layout(title_x=0.25)
            
            col2.plotly_chart(spec_01, use_container_width=True)
            
            spec_02 = px.scatter(data_frame=selected_team_df,
                                x='BLK',
                                y='STL',
                                size='DREB',
                                hover_data='PName', 
                                template='plotly_dark',
                                title='Blocks versus steals with size proportional to the DREB value').update_layout(title_x=0.25)
            col2.plotly_chart(spec_02, use_container_width=True)
            
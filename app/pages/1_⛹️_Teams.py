import streamlit as st
import pandas as pd

tab1, tab2, tab3 = st.tabs(["Offensive", "Defensive", "Specific"])

df_times = pd.read_csv('/home/bruno/repos/aulas_Streamlit_teste/data/df_times.csv', index_col=0)

with tab1:
    with st.container():
        st.title('Teams')
    
        col1, col2 = st.columns([1,6])
        with col1:
            st.write('oi')
        with col2:
            st.dataframe(df_times[['3P%', 'FG%', 'FT%', '2P%']],
                        width=800,
                        height=1090,
                        column_config={
                            "3P%": st.column_config.ProgressColumn(format='%f', min_value=0, max_value=100),
                            "FG%": st.column_config.ProgressColumn(format='%f', min_value=0, max_value=100),\
                            "FT%": st.column_config.ProgressColumn(format='%f', min_value=0, max_value=100),
                            "2P%": st.column_config.ProgressColumn(format='%f', min_value=0, max_value=100)
                        })

with tab2:
    st.write('oi')

with tab3:
    col1, col2 = st.columns([1,6])

    # Trocar o link da logo e o nomes do time por um selecionador de time e filtro a partir dele
    link_logo = 'https://cdn.nba.com/logos/nba/1610612738/global/L/logo.svg'
    nome_time = 'Boston Celtics'

    with col1: 
        st.markdown(f'![]({link_logo})')
        st.markdown(f'## {nome_time}')
    with col2:
        st.write('oi')
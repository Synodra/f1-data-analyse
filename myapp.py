import streamlit as st
from matplotlib import pyplot as plt

import fastf1
import pandas as pd
import modules


## ====== > Page functions

# Sidebar selector to choose a GP
def select_race_session():
    st.write("Yes")



## ====== > Streamlit main
#### Steamlit page configuration
st.set_page_config(
    page_title="Fast F1 Sandbox",
    page_icon="🏎️",
    layout="wide",
)
st.title("Fast F1 Sandbox")

#### Select a session
st.sidebar.markdown("## First select a session")
# Select an F1 Season
if 'selected_season' not in st.session_state:
    st.session_state.selected_season = 2023
selected_season = st.sidebar.multiselect(
    'Season:',
    modules.get_season_list(),
    default=st.session_state.selected_season,
    max_selections=1)

# Select an F1 Race
df_race_schedule = fastf1.get_event_schedule(st.session_state.selected_season)
st.sidebar.selectbox(
    'Race:',
    df_race_schedule['EventName'].values.tolist(),
    key='selected_race'
)

# Select an F1 Session
list_session = df_race_schedule.loc[
            df_race_schedule['EventName'] == st.session_state.selected_race,
            ['Session1', 'Session2', 'Session3', 'Session4', 'Session5']
        ].T.iloc[:,0].tolist()
st.sidebar.selectbox(
    'Session:',
    list_session,
    key='selected_sessions'
)
    

#### Module to load session data
# if 'session' not in st.session_state:
#     st.session_state.session = fastf1.get_session(2019, 'Monza', 'Q')
#     st.session_state.is_session_loaded = False
    
# if st.sidebar.button('Load session'):
#     st.session_state.session = fastf1.get_session(
#         st.session_state.selected_season,
#         st.session_state.selected_race,
#         st.session_state.selected_sessions
#     )
#     # st.session_state['session'].load(telemetry=False, laps=False, weather=False)
#     st.session_state.session.load(weather=False)
#     st.session_state.is_session_loaded = True


# Tell the user what data he is watching
st.write('You are watching the ', st.session_state.selected_sessions,
         'session data of the ', st.session_state.selected_season,
         st.session_state.selected_race, '.')


# if not st.session_state.is_session_loaded: 
#     st.info("""Veuillez d'abord charger les donnees afin de pouvoir visualiser 
#             les analyses.""")

#### Data Viz module
# if st.session_state.is_session_loaded:
    
#     tab1, tab2 = st.tabs(["Global Session", "Deep Dive Pilot"])

#     with tab1:
#         st.header("Global Session")
        
#         st.code(st.session_state['session'].results.iloc[0:10].loc[:, ['Abbreviation', 'GridPosition']])
        
#     # lister les parametres puis afficher les data du gp
    
#     with tab2:
#         st.header("Deep Dive")
        
#         df_driver = modules.get_driver_info(st.session_state['session'])
#         list_drivers = df_driver['BroadcastName'].tolist()

#         selected_driver = st.selectbox('Driver:', list_drivers)
        
#         driver_abbreviation = df_driver.loc[
#             df_driver['BroadcastName'] == selected_driver,
#             ['Abbreviation']
#         ].iloc[0,0]
        
#         fast_driver = st.session_state['session'].laps.pick_driver(driver_abbreviation).pick_fastest()
#         driver_car_data = fast_driver.get_car_data()
#         t = driver_car_data['Time']
#         vCar = driver_car_data['Speed']
        
#         fig, ax = plt.subplots()
#         ax.plot(t, vCar, label='Fast')
#         ax.set_xlabel('Time')
#         ax.set_ylabel('Speed [Km/h]')
#         ax.set_title(f'{selected_driver} is')
#         ax.legend()
        
#         st.pyplot(fig)
    
# else : 
#     st.info("""Veuillez d'abord charger les donnees afin de pouvoir visualiser 
#             les analyses.""")







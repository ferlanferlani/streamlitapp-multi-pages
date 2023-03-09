import streamlit as st
from streamlit_option_menu import option_menu

menu_selected = option_menu(
  menu_title='Main menu',
  options=['data 1', 'data 2', 'data 3'],
  icons=['house', 'eye', 'mouse'],
  orientation='horizontal',
)

if menu_selected == 'data 1':
  st.header('this is menu selected menu data 1')
elif menu_selected == 'data 2':
  st.header('this is menu selected menu data 2')
elif menu_selected == 'data 3':
  st.header('this is menu selected menu data 3')

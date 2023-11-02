import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🎂Omega 3 & Blueberry Oatmeal')
streamlit.text('☕Kale,Spinach & Rocket Smoothie')
streamlit.text('🎁Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍆Avocado Toast🥦🥬')
import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#fruits_to_show = my_fruit_list.loc[fruits_selected]
fruits_selected = streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
#new session
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
streamlit.header("Fruityvice Fruit Advice!")
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

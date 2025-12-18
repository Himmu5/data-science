import joblib as jb
import streamlit as st 
import pandas as pd


def load_model(path = "model/xgmodel.pkl"):
    return jb.load(path)


model = load_model()

st.title("Housing Price Prediction App")

with st.form("user_info_form", clear_on_submit=True):
    st.write("Please enter your information:")
    block_income = st.number_input("Enter median income in block", min_value=0.0, max_value=20.0, value=3.87)   
    house_age = st.number_input("Enter median house age in block", min_value=1.0, max_value=52.0, value=29.0)  
    avg_room = st.number_input("Enter average number of rooms", min_value=1.0, max_value=141.0, value=5.43)   
    avg_beds = st.number_input("Enter average number of bedrooms", min_value=1.0, max_value=35.0, value=1.10)    
    block_population = st.number_input("Enter block population", min_value=3.0, max_value=35682.0, value=1425.0)  
    avg_occupancy = st.number_input("Enter average house occupancy", min_value=0.5, max_value=1243.0, value=3.07)  
    avg_latitude = st.number_input("Enter house block latitude", min_value=32.5, max_value=42.0, value=34.26)  
    avg_longitude = st.number_input("Enter house block longitude", min_value=-124.35, max_value=-114.31, value=-118.4)  

    submitted = st.form_submit_button("Submit")
if submitted:
    input_data = pd.DataFrame({ 
        "MedInc":block_income,
        "HouseAge": house_age,
        "AveRooms": avg_room,
        "AveBedrms": avg_beds,
        "Population": block_population,
        "AveOccup": avg_occupancy,
        "Latitude": avg_latitude,
        "Longitude": avg_longitude
    }, index=[0])
    print(input_data)
    pred = model.predict(input_data)[0]
    print(pred)
    st.success(f"Predicted House Price: ${round(pred * 10**5)}")
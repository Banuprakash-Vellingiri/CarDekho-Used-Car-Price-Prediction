#------------------------------------ CarDekho Used Car Price Prediction Streamlit Web Appplication -----------------------------------
#importing necessary libraries
import streamlit as st
import pandas as pd
import pickle
import numpy as np
from PIL import Image

#-------------------= Image.open("path_to_your_image.jp-----------------------------------------------------------------------------------
#Streamlit environment
#Page Layout
st.set_page_config (
                    page_title="CarDekho Used Car Price Prediction by Banuprakash",
                    page_icon= "🚘",  
                    layout="wide", 
                    initial_sidebar_state="expanded",  
                   )
#-------------------------------------------------------------------------------------------------------
#Title 
st.markdown("# 🚗 :red[CarDekho] Used Car Price Prediction")
st.markdown("__________________________________________________________________________________________")
st.markdown("### Enter the Details of the Car ⬇️")
# image = Image.open(r"C:\Users\banup\Desktop\CarDekho Used Car Price Prediction\Untitled design (26).png")
# st.image(image)
#--------------------------------------------------------------------------------------------------------
manufacturer_list=['Audi', 'BMW', 'Chevrolet', 'Citroen', 'Datsun', 'Fiat', 'Ford', 'Hindustan Motors', 'Honda', 'Hyundai', 'Isuzu', 'Jaguar', 'Jeep', 'Kia', 'Land Rover', 'MG', 'Mahindra', 'Maruti', 'Mercedes-Benz', 'Mini', 'Mitsubishi', 'Nissan', 'Opel', 'Renault', 'Skoda', 'Tata', 'Toyota', 'Volkswagen', 'Volvo']
model_year_list=[2015, 2018, 2014, 2020, 2017, 2021, 2019, 2022, 2016, 2011, 2013,2010, 2008, 2006, 2012, 2009, 2005, 2007, 2023, 2004, 2003, 2002],
body_type_list=['Hatchback', 'MUV', 'Others', 'SUV', 'Sedan']
fuel_type_list=['Diesel', 'Petrol']
transmission_list=['Automatic', 'Manual']
#---------------------------------------------------------------------------------------------------------
cola,colb=st.columns([1,1])
with cola:
    col1,col2=st.columns([5,5]) 
    with st.form("form_1"): 
        with col1 :   
                manufacturer = st.selectbox("Manufacturer :", manufacturer_list)
                body_type= st.selectbox("Body Type :", body_type_list)
                model_year = st.slider('Model Year:',2002,2023)
                fuel_type= st.selectbox("Fuel Type :",fuel_type_list)  
        with col2: 
                transmission=st.selectbox("Transmission :", transmission_list)
                power=st.number_input("Power (bhp):", min_value=46, max_value=282)
                mileage=st.number_input("Mileage (kmpl) (8-28):", min_value=8, max_value=28) 
                kilometers=st.number_input("Kilometers (0-159000) :", min_value=0, max_value=159000)
            
        predict_button= st.form_submit_button(label=" :orange[Predict Selling Price]")
        

    if predict_button:
                    #mapping the input with desired numerical value
                    manufacturer_dict={'Audi': 0.01741261447181736, 'BMW': 0.014832967883399974, 'Chevrolet': 0.0096736747065652, 'Citroen': 0.0010318586353669547, 'Datsun': 0.009544692377144332, 'Fiat': 0.0038694698826260802, 'Ford': 0.03727589320263124, 'Hindustan Motors': 0.00025796465884173866, 'Honda': 0.1093770153488972, 'Hyundai': 0.20650070940281182, 'Isuzu': 0.0006449116471043467, 'Jaguar': 0.003095575906100864, 'Jeep': 0.01367212691861215, 'Kia': 0.01986327873081388, 'Land Rover': 0.002321681929575648, 'MG': 0.010060621694827809, 'Mahindra': 0.04772346188572166, 'Maruti': 0.2729266090545595, 'Mercedes-Benz': 0.018186508448342575, 'Mini': 0.001160840964787824, 'Mitsubishi': 0.001547787953050432, 'Nissan': 0.00993163936540694, 'Opel': 0.000386946988262608, 'Renault': 0.03972655746162776, 'Skoda': 0.020250225719076486, 'Tata': 0.05043209080355991, 'Toyota': 0.03830775183799819, 'Volkswagen': 0.03675996388494776, 'Volvo': 0.0032245582355217334}
                    body_type_dict= {'Hatchback': 0.4390558493486392, 'MUV': 0.041661292402940794, 'Others': 0.0034825228943634722, 'SUV': 0.25757771185347605, 'Sedan': 0.2582226235005804}    
                    fuel_type_dict={'Diesel': 0.31523281310460466, 'Petrol': 0.6847671868953953}
                    transmission_dict={'Automatic': 0.2539662066296917, 'Manual': 0.7460337933703083}
                    #input features of the model
                    input_features=[manufacturer_dict[manufacturer],model_year,body_type_dict[body_type],fuel_type_dict[fuel_type],transmission_dict[transmission],power,mileage,kilometers]
                    #----------------------------------------------------------------------------------------------------
                    #Loading the model
                    with open("xgb_regressor_model.pkl","rb") as f :
                        xgb_regressor_model=pickle.load(f)
                    #Fit the input with the model
                    input_feature_array = np.array(input_features).reshape(1, -1)
                    selling_price=xgb_regressor_model.predict(input_feature_array)
                    selling_price=selling_price[0]
                    st.markdown("## :green[Selling Price(₹):] {:.3f} Lakhs".format(selling_price))
    st.text("created by banuprakash vellingiri ❤︎ ")               
    st.text("Note : This GUI is just for demonstration,values and predictions may differ.")
    st.text("Thank you 👍")
with colb:
       image = Image.open(r"C:\Users\banup\Desktop\CarDekho Used Car Price Prediction\cardekho_logo.png")
       image = image.resize((800, 800))
       st.image(image)
st.text("Note : This GUI is just for demonstration,values and predictions may differ.Thank you.")
#----------------------------------------------------------------------------------------------------------------------
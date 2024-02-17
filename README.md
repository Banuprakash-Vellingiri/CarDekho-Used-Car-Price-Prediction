
# 🚗 CarDekho Used Car Price Prediction

### 🎯 Aim :
   The goal of this  project is to predict the current selling price of used cars in the market. This can be achieved by  building a machine learning model which is trained by the diverse data of cars taken from 🔗[cardekho.com](https://www.cardekho.com/).

### 📄Dataset information :
 As i had mentioned above, the dataset was taken from the 🔗[cardekho.com](https://www.cardekho.com/) by web scraping.
 - __About🚘Cardekho__:
            CarDekho is a prominent online platform in the Indian automotive industry, offering a comprehensive range of services. Users can access detailed information, specifications, and reviews for various car models, aiding in informed decision-making. The platform features listings for both new and used cars, providing a marketplace for buying and selling vehicles. CarDekho also offers comparison tools, enabling users to assess different models based on specific criteria.
 
 I had recieved this scraped dataset from a authorised team in 🔗[guvi](https://www.guvi.in/).The dataset holds huge information about cars which includes **car name,model name,manufacturing year, mileage, engine power, transmission power, fuel type, interior and exterior features availability,selling price  and so on**.There are 6 different chunks of datasets are available which belongs to cities such as bangalore,coimbatore, chennai,delhi, jaipur and kolkata. The datasets are in ".xlsx" format.
### 🐾 Steps involved :
This project involves a basic machine learning pipeline.

      - Data cleaning
      - Exploratory Data Analysis(EDA)
      - Data preprocssing
      - Feature Engineering
      - Model selection 
      - Model training
      - Model Evaluation
      - Selling Price prediction
### 🛠️ Tools and libraries used :
      - Python
      - Pandas
      - NumPy
      - Matplotlib and Seaborn (visualization)
      - Sci-kit learn (machine learning)
      - streamlit (GUI)
### 👨‍💻 Approach :
  - Initially the  datasets are loaded in pandas dataframe and are grouped together
  - Since the dataset was too clumsy and messy, so the meaningfull informations considered and neglected the irrelavant informations.
  - Checked for the outliers and missing values by visualizations and handled them in a proper way by filling or removing them.
  - The data is normalized and scaled to the appropiate values
  - EDA has done and gained insights between the feature variables and the target variable(selling price).
  - From the insights of EDA ,the best features were selected.
  - The categorical feature variables were encoded.
  - Appropiate regression model was selected and the model was trained under various various hyper parameters to select the best model parameter,cross validation was also done to ensure the model performance at various folds.
  - Various evaluation metrics were calculated and the model was fine tunned.
  - Finally a machine learning model was built with a good accuracy in predicting the selling price of the cars.
### 🌐Streamlit application :
 - A web application (GUI) was built by streamlit, to intake input from the user and to display the predicted sellining price.





### 📰 Documentation :

- [Python](https://docs.python.org/3/)
- [pandas](https://pandas.pydata.org/docs/)
- [Matplotlib](https://matplotlib.org/stable/index.html)
- [Seaborn](https://seaborn.pydata.org/)
- [Sci-kit learn](https://scikit-learn.org/stable/)
- [Streamlit](https://docs.streamlit.io/)



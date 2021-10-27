# import libraries
import data_handler as dh
import numpy as np
import pandas as pd
from joblib import load

model = load('./data/best_model.joblib')


smoke_options = ['yes', 'no']
sex_options = ['male', 'female']
region_options = set(pd.read_csv("./insurance.csv").values[:,5])

print("\nCHECK YOUR INSURANCE CHARGES")
print("="*50)
no_check = 1

while True:

    # reset values
    check = True
    smoke = -1
    sex = -1
    region = -1
    to_continue = -1

    print("\nCheck number:",no_check)
    print('-'*25,"\n")

    # gather input features
    while check:
        try:
            age = int(input("1. How old are you? \t"))
            child = int(input("2. How many children do you have? \t"))
            bmi = float(input("3. What's your bmi? \t"))
            check = False
        except:
            print('Age, no of children and bmi must be valid numbers')

    while smoke not in smoke_options:
        smoke = (input("4. Do you smoke? (yes, no)\t")).lower()
    while sex not in sex_options:    
        sex = (input("5. What's your sex? (male, female) \t")).lower()
    while region not in region_options: 
        region = (input("6. What region are you from? ("+', '.join(region_options)+")\t")).lower()

    # get and transform data
    data = np.array([age,sex,bmi,child,smoke,region]).reshape(1, -1)
    data = dh.transform(data)

    #predict with saved model
    prediction = model.predict(data)
    print("\nYour charge is: ",prediction[0])

    #check if user wants to check more
    while to_continue not in ['yes', 'no']:
        to_continue = (input("\nDo you want to continue? (yes, no)\t")).lower()
    if to_continue == 'no':
        print('\nThanks and bye\n')
        break
    
    #keep counts of checks done
    no_check += 1

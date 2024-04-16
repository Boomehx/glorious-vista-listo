import pandas as pd
import numpy as npy


df = pd.read_csv("https://docs.google.com/spreadsheets/d/1yiTNYyfjpvOmbg1_YBhTFs4vp-f8Mcc5vBoMf0a2skI/export?format=csv")

def modeQrtATK(district, df):
    return (df[(df["distNameATK"] == str(district))]["distQrtATK"].mode().to_string(index = False)).replace('\n','&')

def modeQrtDEF(district, df):
    return df[(df["distNameDEF"] == str(district))]["distQrtDEF"].mode().to_string(index = False).replace('\n','&')


def main():
    active = True
    district = input("Please select what district you want to spy on: ")

    

    while (active == True):

        option = input("Please select option: ")

        match option:

            case "Exit":
                active = False
        
            #modeQrtATK
            case "1":
                print(modeQrtATK(district, df))

            case "2":
                print(modeQrtDEF(district, df))


            case "District":
                district = input("Please select what district you want to spy on: ")
            
            case _:
                print("Option doesn't exist please select another option!")
        

    return print("bleh")

main()


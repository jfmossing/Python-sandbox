# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 19:05:01 2021

@author: Josh Mossing    
"""
#The function below takes in gallons and the type of fuel and outputs the price
def compute_gas_price (gallons: float, FuelType: float) -> float :
    if FuelType == 87:
        price = gallons * 2.20
    elif FuelType == 89:
        price = gallons * 2.40
    elif FuelType == 92:
        price = gallons * 2.80
    else:
        price = "error, not a valid fuel type"
    print(price)
    return price 
   
compute_gas_price(16, 87)
compute_gas_price(25, 92)

# the function below returns the amount of gas used in gallons
def compute_gas_used (miles: float, MPG: float) -> float :
    gallons_used = (miles / MPG)
    return gallons_used 

print(compute_gas_used(300.5, 28.6))
print(compute_gas_used(1400, 19.2))
    
# the function compute_total_price utilizes a different function compute_gas_price
# It uses the function compute gas used as well
def compute_total_price (FuelType: float, miles: float, MPG: float) -> float:
    gallons = compute_gas_used(miles, MPG)
    # print(compute_gas_price(gallons, FuelType))
    return compute_gas_price(gallons, FuelType)

compute_total_price(87, 600, 19.6)
compute_total_price(92, 1400, 19.6)


# this function takes in a str for the car make and a list for the car model
# It uses a for loop for the number of car models and executes code to 
#match the make and model to those elements in the dictionary

def output_make_popular_model(car_make: str, car_model: list) -> dict: 
    name_brand_dict = {"make":[],"model":[]}
  
    for amount in car_model:
       
        if car_make == "honda" :
            name_brand_dict["make"]="honda"
        elif car_make == "toyota":
            name_brand_dict["make"]="toyota"
        elif car_make == "ford":
             name_brand_dict["make"]="toyota"
        else:
            print("pick honda, toyota, or ford")
            
    name_brand_dict["model"].append(car_model)
    print(name_brand_dict)
    return car_make

output_make_popular_model("honda",["crv","accord","civic"])
output_make_popular_model("toyota",["camry", "tundra","tacoma"])


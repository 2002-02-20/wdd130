
from datetime import datetime

def calculate_tire_volume(width, aspect_ratio, diameter):
  
    import math
    width = width / 10 
    aspect_ratio = aspect_ratio / 100  
    volume = (math.pi * width**2 * aspect_ratio * (diameter + (2 * width)))/1000 
    return round(volume, 2)

current_date_and_time = datetime.now()
current_date = current_date_and_time.strftime("%Y-%m-%d") 

width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = calculate_tire_volume(width, aspect_ratio, diameter)

print(f"The approximate volume is {volume} liters")

data = f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume}"

with open("volumes.txt", "at") as file:
    print(data, file=file)


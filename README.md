# Battery Life and Charging Time Predictor Using Python

## Overview
This project predicts real-time remaining battery usage duration, charging time required, and battery health for mobile phones and laptops. Unlike standard battery indicators that only display percentage, this system calculates performance using time since last full charge, battery capacity, charger watt rating and device type. It aims to help users manage battery usage more accurately and efficiently.

## Features
- Prediction of remaining battery usage time (in hours)
- Charging duration estimation based on charger watt rating
- Calculation of battery health using drain behavior
- Support for both Mobile and Laptop devices
- Simple and user-friendly command-line interface

## Technologies Used
- Python 3.x
- VS Code / Terminal
- Command-line based application

## How to Run the Program
1. Download or clone the repository
2. Open the project folder in VS Code or terminal
3. Run the following command:
Baterry_Life_Predictor.py
4. Respond to input prompts to receive predictions

## Input Parameters
- Current battery percentage
- Hours since last full charge
- Battery capacity in mAh
- Charger watt rating
- Device type selection (Mobile / Laptop)

## Example Output
Estimated usage time remaining: 5.20 hours  
Battery Health: 82.34%  
Charging Time Required: 1.45 hours  
Status: Low for Laptop – Plug in charger soon

## Testing
- Tested across different battery percentages (10%–90%)
- Tested with charger wattages (10W–120W)
- Tested separately for Mobile and Laptop
- Performed boundary and comparison testing

## Challenges Faced
- Achieving realistic battery health calculation
- Optimizing formula accuracy based on real usage
- Designing simple but effective input structure

## Future Enhancements
- Graphical user interface (GUI)
- Automated device hardware detection
- Mobile application version
- Historical analytics and graph reports

## Project Documentation
Screenshots, project report PDF and flow diagrams are included separately in the documentation section.

## Developed By
Student Name: Mousam Mishra 
Registration No: 25BCE10773
Project Title: Battery Life & Charging Time Predictor
   

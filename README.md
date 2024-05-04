# Flight Delay Predictor ✈️

## Project Details 📜
#### The flight delay predictor is a tool I built in Python for my Computational Thinking class. It takes flight data from July 2023 for all domestic flights that happened during the month. This data is stored in the July23_Flight_Delays.csv file. Ultimately, the predictor will return a text file that compares factors like duration of delay and number of flights in and out of two airports of the user's choosing. Airport codes and their corresponding city can be found at https://www.leonardsguide.com/us-airport-codes.shtml. 

## Example Output:
#### The screenshot below shows what a successful output text file would look like for this project. This example compares flight information from Las Vegas McCarran International Airport (LAS) and Washington National Airport (DCA) in Washington, D.C. This txt file is found in this repository for reference.

<img width="675" alt="Screen Shot 2024-05-04 at 5 09 21 PM" src="https://github.com/carsonkirby/flight_delay_predictor/assets/145626359/c8397041-67ec-4e3b-a553-ce1d7a9be45d">



## What I Learned 📚 
#### Through this project, I learned how to built dictinaries in Python and implement them in functions that return useful information. I was challenged to use several functions that took the dictinaries as arguments and wrote the appopriate stats onto a new file. 

## How to Run the Program 💻
#### 1. Clone this repository on your local machine or just download the July23_Flight_Delays.csv file and the flight_delay_predictor.py file.
#### 2. Open a Python terminal. I use a program called Spyder through Anconda Navigator.
#### 3. Ensure that the python file and CSV file are in the same directory or folder. 
#### 4. Run the python file
#### 5. Input the airport codes of the two airports you want to compare when prompted
#### 6. If successful, a txt file should be created in the same directory with the titled formatted as AirportCode1&AirportCode2.txt (LAS&DCA.txt)

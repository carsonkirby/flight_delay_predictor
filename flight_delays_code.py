######################
### Lab Activity 2 ###
######################


'''
Flight Delay Tracker
'''

def main ():
    file = open("July23_Flight_Delays.csv")
    airline, delays, airports = build_dicts(file)
    airport_1 = input("Name the first aiprort: ")
    airport_2 = input("Name the second airport: ")
    stats(airline, delays, airports, airport_1, airport_2)
    file.close()
    
     
def build_dicts(file_1):
    airlines_dict, airports_dict, delays_dict = {}, {}, {}
    
    for line in file_1:
        data = line.strip().split(",")
        
        if line.startswith("Airline"):
            continue
        
        temp_airline, temp_origin, temp_dst, temp_delay = data
        
        temp_delay = int(temp_delay.strip())  # Converting delay time to an integer
        
        if temp_dst not in airlines_dict:
            airlines_dict[temp_dst] = [temp_airline]
            airports_dict[temp_dst] = [temp_origin]
            delays_dict[temp_dst] = [temp_delay]
        else:
            if temp_airline not in airlines_dict[temp_dst]:
                airlines_dict[temp_dst].append(temp_airline)
            
            if temp_origin not in airports_dict[temp_dst]:
                airports_dict[temp_dst].append(temp_origin)
            
            delays_dict[temp_dst].append(temp_delay)
    
    return airlines_dict, delays_dict, airports_dict           
    
    
def stats(airlines_dict, delays_dict, airports_dict, airport_1, airport_2):

    file_name = airport_1 + "&" + airport_2 + ".txt"    
    
    file_2 = open(file_name, "w")
    
    file_2.write("These airlines fly into %s: %s" % (airport_1, str(airlines_dict[airport_1])))

    file_2.write("\nThese airlines fly into %s: %s" % (airport_2, str(airlines_dict[airport_2])))
    
    
    file_2. write("\nThese airports have direct flights into %s: %s" % (airport_1, str(airports_dict[airport_1])))
    file_2. write("\nThese airports have direct flights into %s: %s" % (airport_2, str(airports_dict[airport_2])))
    
    num_airlines_1 = len(airlines_dict[airport_1])
    num_airlines_2 = len(airlines_dict[airport_2])
    
    num_airports_1 = len(airports_dict[airport_1])
    num_airports_2 = len(airports_dict[airport_2])
    
    if num_airlines_1 > num_airlines_2: 
        file_2.write ("\n%s has %d more airlines inbound than %s. %d vs. %d" % (airport_1, (num_airlines_1 - num_airlines_2), airport_2, num_airlines_1, num_airlines_2))
   
    else:
        file_2.write ("\n%s has %d more airlines inbound than %s. %d vs. %d" % (airport_2, (num_airlines_2 - num_airlines_1), airport_1, num_airlines_2, num_airlines_1))
    
    
    if num_airports_1 > num_airports_2:
        file_2.write("\n%s has %d more airports that connect than %s. %d vs. %d" % (airport_1, (num_airports_1 - num_airports_2), airport_2, num_airports_1, num_airports_2))
    
    else: 
        file_2.write("\n%s has %d more airports that connect than %s. %d vs. %d" % (airport_2, (num_airports_2 - num_airports_1), airport_1, num_airports_2, num_airports_1))
       
    
    avg_delay_1 = sum(delays_dict[airport_1]) / len(delays_dict[airport_1])
    avg_delay_2 = sum(delays_dict[airport_2]) / len(delays_dict[airport_2])
    
  
    file_2.write("\nAverage delay for %s: %.0f minutes" % (airport_1,  avg_delay_1))
    file_2.write("\nAverage delay for %s: %.0f minutes" % (airport_2,  avg_delay_2))
    

    late_flights_1 = sum(1 for delay in delays_dict[airport_1] if delay > 14)
    percent_late_1 = (late_flights_1 / len(delays_dict[airport_1])) * 100

 
    late_flights_2 = sum(1 for delay in delays_dict[airport_2] if delay > 14)
    percent_late_2 = (late_flights_2 / len(delays_dict[airport_2])) * 100

    file_2.write("\nFor %s in July, %.1f%% of flights were late" % (airport_1, percent_late_1))
    file_2.write("\nFor %s in July, %.1f%% of flights were late" % (airport_2, percent_late_2))

               
    
        
   
if __name__== "__main__":
       
    main()    
    


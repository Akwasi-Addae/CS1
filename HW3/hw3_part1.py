from math import log

# Function to calculate the number of tourists based on bear population
def get_tourists(bears):
    if bears < 4 or bears > 15:
        return 0
    tourists = bears * 10000
    if bears > 10:
        tourists += (bears - 10) * 20000
    return tourists

# # Function to calculate the next year's bear population and berry field area
def find_next(bears, berries, tourists):
    # Calculate next year’s values for bears and berries
    bears_next = berries / (50 * (bears + 1)) + bears * 0.60 - (log(1 + tourists, 10) * 0.1)
    berries_next = (berries * 1.5) - (bears + 1) * (berries / 14) - (log(1 + tourists, 10) * 0.05)

    # Ensure bears and berries are not negative and clip to minimum 0
    bears_next = max(0, int(bears_next))  # Bears should be an integer
    berries_next = max(0, berries_next, 1)  # Berries should be a float with 1 decimal place
    
    return bears_next, berries_next

# # Main program
max_tourists = min_tourists = 0

bears = int(input("Number of bears => "))
max_bears = min_bears = bears
print(bears)
berries = float(input("Size of berry area => "))
min_berry = max_berry = berries

print(int(berries))

print("Year" + " "*6 + "Bears" + " "*5 + "Berry" + " "*5 + "Tourists" + " "*2)

for year in range(1, 11):
    # Get max and min tourists
    tourists = get_tourists(bears)
    max_tourists = max(max_tourists, tourists)
    min_tourists = min(min_tourists, tourists)

    print(str(year) + " "*(10-len(str(year))) + 
      str(bears) + " "*(10-len(str(bears))) + 
      str(round(berries, 1)) + " "*(10-len(str(round(berries, 1)))) + 
      str(tourists) + " "*(10-len(str(tourists))))

    # Calculate next year's bears and berries
    if year != 10:
        bears, berries = find_next(bears, berries, tourists)
        min_bears = min(min_bears, bears)
        max_bears = max(max_bears, bears)
        min_berry = min(min_berry, berries)
        max_berry = max(max_berry, berries)

print()
print("Min:     ", str(min_bears) + " "*(10-len(str(min_bears))) + str(min_berry) + " "*(10-len(str(min_berry))) + str(min_tourists) + ' '*(10-len(str(min_tourists))))
print("Max:     ", str(max_bears) + " "*(10-1-len(str(max_bears))), str(round(max_berry,1))+  " "*(10-len(str(round(max_berry,1)))) + str(max_tourists)+ ' '*(10-len(str(max_tourists))))


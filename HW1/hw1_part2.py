minutes = (input("Minutes ==> "))
print(minutes)
minutes = int(minutes)

seconds = (input("Seconds ==> "))
print(seconds)
seconds = int(seconds)

miles = (input("Miles ==> "))
print(float(miles))
miles = float(miles)

target_miles = float(input("Target Miles ==> "))
print(target_miles)

# Calculate values for final output
pace = ((minutes*60+seconds)/miles)
speed = miles/(minutes*60+seconds)*60*60
total_minutes = target_miles / speed * 60
whole_minutes = int(total_minutes)
remaining_seconds = int((total_minutes - whole_minutes) * 60)

print()
print("Pace is", str(int(pace/60)) + " minutes and", str(int(pace%60)), "seconds per mile.")
print("Speed is", str(round(speed,2)),"miles per hour.")
print("Time to run the target distance of {0:.2f} miles is".format(target_miles), str(int(target_miles/speed*60)), "minutes and", str(int((total_minutes - whole_minutes) * 60)), "seconds.")
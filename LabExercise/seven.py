#you have 4 miles from university. the bus drives at 25 mph but spends 2 minutes at each of the 10 stops on the way .how long will the bus journey take ?
# alternatively ,you could run to university .you jog the first mile at 7mph.then run the next two at 15mph:before jogging the last at 7mph again .
# will this be quicker or slower than the bus.
distance=4
speed=25
bus_time= (distance/speed + 1/3)*60
print(f"the time taken by bus is {bus_time}")
jog_one=1/7
jog_two=2/15
jog_three=1/7
total_run_time=(jog_one+jog_two+jog_three)*60
print(f"your total run time is {total_run_time}")
if(total_run_time < bus_time):
    print("you jog faster than that slow bus :)")
else:
    print("you run slower than the bus")
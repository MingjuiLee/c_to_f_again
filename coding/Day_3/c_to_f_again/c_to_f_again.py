# let user inputs C, output F
temp_c = input("Please input temperature in C: ")
temp_c = float(temp_c)  # input is a str, need casting to float or integer
temp_f = temp_c * 9 / 5 + 32	# create a new variable 
print("temperature in F: ", temp_f)
import math as m
import csv
import pandas as pd

input_file = "mobility-simulation.csv"

# Given 2 points (lat, lon), it gives the distance in meters
def haversine(lat1, lon1, lat2, lon2):
	R = 6371000		# Earth radius [m]
	fi1 = lat1 * m.pi/180
	fi2 = lat2 * m.pi/180
	delta_fi = (lat2-lat1) * m.pi/180
	delta_lambda = (lon2-lon1) * m.pi/180
	
	term1 = m.sin(delta_fi/2) * m.sin(delta_fi/2)
	term2 = m.cos(fi1)*m.cos(fi2)*m.sin(delta_lambda/2)*m.sin(delta_lambda/2)
	a = term1 + term2
	
	return R * 2 * m.atan2(m.sqrt(a),m.sqrt(1-a))

# READ CSV FILE WITH PANDAS
output_file = open('output-file.txt', 'w')
output_file.write("user_a, user_b, time_step\n")
df = pd.read_csv('mobility-simulation.csv')
print(df)

# Variables
num_steps = 100
dist_range = 10
num_users = 10

for x in range(0, num_steps):
	print("# Step " + str(num_steps) + " #")
	step = df.loc[df['step'] == x]
	for i in range(0, num_users):
		for j in range(0, num_users):
			print("Users: " + str(i) + ", " + str(j))
			user_a = step.loc[step['user'] == i]
			user_b = step.loc[step['user'] == j]
			dist = haversine(user_a.values[0][2], user_a.values[0][3], user_b.values[0][2], user_b.values[0][3])
			print("Dist: " + str(dist))
			
			if(dist <= dist_range):
				output_file.write(str(i) + ',' + str(j) + ',' + str(x) + '\n')

output_file.close()

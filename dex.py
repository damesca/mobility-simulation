import pandas as pd

# Open file and parse data
f = open('output/outputtrace1.txt', 'r')
line = f.readline()
header = line.split('	');

f_csv = open('output/outputtrace1.csv', 'w')

for l in f:
	f_csv.write(l.replace('	', ','))

f.close()
f_csv.close()

data = pd.read_csv('output/outputtrace1.csv')
print(data)

number_iter = header[0].split('=')[1]
print(number_iter)

# Handle data
f_out = open('output/trace1res.csv', 'w')
f_out.write('Iter,refId,refPX,refPY,cmpId,cmpPX,cmpPY\n')

for i in range(1, int(number_iter)+1):
	elements = data.loc[data['Time'] == i]

	positionX = elements['PositionX'].tolist()
	positionY = elements['PositionY'].tolist()
	
	def inRange(px0, px1, length):
		return abs(px0 - px1) < length
	
	length = 50
	for ref_id in range(0, len(positionX)):
		for comp_id in range(0, len(positionX)):
			if(ref_id != comp_id):
				if(inRange(positionX[ref_id], positionX[comp_id], length) and inRange(positionY[ref_id], positionY[comp_id], length)):
					f_out.write(str(i) + ',' + str(ref_id) + ',' + str(positionX[ref_id]) + ',' + str(positionY[ref_id]) + ',' + str(comp_id) + ',' + str(positionX[comp_id]) + ',' + str(positionY[comp_id]) + '\n')


# Close files		
f_out.close()

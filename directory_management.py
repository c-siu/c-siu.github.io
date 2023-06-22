import os

#path = 'teaching/1809_4060'
path = 'teaching/1801_2010'

for file in os.listdir(path):
#    if file[:4] == '1901':
    if file[:4] == '1901':
    	os.rename(
        	os.path.join(path, file),
#        	os.path.join(path, '1809' + file[4:])
            os.path.join(path, '1801' + file[4:])
    	)
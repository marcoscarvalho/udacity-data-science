# coding: utf-8

import glob, os

def create_master_turnstile_file(filenames, output_file):
    try:
    	with open(output_file, 'w') as master_file:
    		master_file.write('C/A,UNIT,SCP,DATE,TIME,DESC,ENTRIES,EXITS\n')
    		for filename in filenames:
    			with open(filename) as f:
    				next(f)
    					
    				for line in f:
    					data = line.strip().split(",")
    					ca,unit,scp,station,linename,division,date,time,desc,entries,exits = data
    					master_file.write('{},{},{},{},{},{},{},{}\n'.format(ca, unit, scp, date, time, desc, entries, exits))
    except Exception as e:
        print('Erro na escrita do arquivo', e)

output_file = 'turnstile_1706.txt'
filenames = []

os.chdir(".")
for file in glob.glob("*.txt"):
    filenames.append(file)
	
create_master_turnstile_file(filenames, output_file)
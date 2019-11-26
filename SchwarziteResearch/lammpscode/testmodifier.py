#Christopher Aquino
#.xyz file modifier for LAMMPS

xyz = open('P8-31_D3_15.xyz','r')

coordinates = []
for line in xyz:
    line = line.strip('\n')
    line=line.split('\t')
    coordinates.append(line)

xyz.close()

i=1
for line1 in coordinates:
    print(str(i)+' 1 ' + line1[1] + ' ' + line1[2] + ' ' + line1[3] + ' #C')
    i+=1
    

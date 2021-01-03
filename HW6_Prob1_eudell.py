# HW6 Programming Problem 1
# File: hw6_prob1_eudell.py
# Date: 10 October 2021
# By: Emily Udell
# Login Id: eudell
#
#
# ELECTRONIC SIGNATURE
# Emily Udell
#
# The electronic signature above indicates that the program
# submitted for evaluation is my individual work. I have
# a general understanding of all aspects of its development
# and execution.
#
#This program organizes plant data according to the users organization code
#and then creates a new file containing the sorted values of plant health
#data.
#
#---------------------------------------------------
#  Inputs
#---------------------------------------------------
from operator import itemgetter

treatmentData = str(input("Enter a file name for the reorganized data: "))
code = str(input("Enter a code for the reorganization: "))


plantData = open('C:/Users/emily/Downloads/plant_treatment_data.txt')

#---------------------------------------------------
#  Calculations
#---------------------------------------------------

def orgColumn(p,q):
    plantList = []
    for i in range(5):
        plantData.readline()
        plantData.read(p)
        plantList.append(float((plantData.read(q))))
    plantData.seek(0)
    return(plantList)

plantID = orgColumn(0,3)
status = orgColumn(9,1)
startingHeight = orgColumn(17,5)
endingHeight = orgColumn(33,5)
concentration = orgColumn(47,4)


growth = []
for i in range(5):
    growth.append(round(float(endingHeight[i])-float(startingHeight[i]),3))


zipped = list(zip(plantID, status, growth, concentration ))

if code[1] == 'A': 
    if code [0] == 'P':
        newList = sorted(zipped, key=itemgetter(0)) 
    elif code[0] == 'S': 
        newList = sorted(zipped, key=itemgetter(1))
    elif code[0] == 'G': 
        newList = sorted(zipped, key=itemgetter(2))
    else:
        newList = sorted(zipped, key=itemgetter(3))
elif code[1] == 'D': 
    if code [0] == 'P':
        newList = sorted(zipped, key=itemgetter(0), reverse = True)
    elif code[0] == 'S': 
        newList = sorted(zipped, key=itemgetter(1), reverse = True)
    elif code[0] == 'G': 
        newList = sorted(zipped, key=itemgetter(2), reverse = True)
    else:
        newList = sorted(zipped, key=itemgetter(3), reverse = True)
    
finalList = [list(m) for m in zip(*newList)]

finalPlantID = finalList[0]
finalStatus = finalList[1]
finalGrowth = finalList[2]
finalConcentration = finalList[3]

#---------------------------------------------------
#  Outputs
#---------------------------------------------------

newPlant = open('C:/Users/emily/Documents/'+ treatmentData + '.txt','w+')

newPlant.write(str("PlantID"))
newPlant.write(str("  Status"))
newPlant.write(str("  Growth"))
newPlant.write(str("  Concentration"))

for n in range(5):
    newPlant.write('\n'+str(int(finalList[0][n])))
    newPlant.write('\t'+" "+str(int(finalList[1][n])))
    newPlant.write('\t'+" "+str(finalList[2][n]))
    newPlant.write('\t'+" "+str('%.2f'%(finalList[3][n])))

print("File "+ treatmentData +" has now been created")

newPlant.close()
plantData.seek(0)
plantData.close()


import os


def extract_coordinates(file_name):
    with open(file_name, "r") as file:
        text = file.read()
        begin = text.find("<coordinates>") + 13
        end = text.find("</coordinates>")
        coordinates = text[begin:end]
        return coordinates.split(" ")


file_names = ["1.kml", "2.kml", "3.kml", "4.kml", "5.kml"]# "6.kml", "7.kml", "8.kml", "9.kml", "10.kml", "11.kml", "12.kml", "13.kml", "14.kml", "15.kml"]
data_list = []

for file_name in file_names:
    data = extract_coordinates(file_name)
    data_list.append(data)
    os.remove(file_name)

output = [data_list[0]]
data_list.pop(0)

for list_in_output in output:
    for data in data_list:
        if data[0] == list_in_output[-1]:
            output.append(data[1:])
            data_list.remove(data)
        elif data[-1] == list_in_output[-1]:
            x = data[::-1]
            output.append(x[1:])
            data_list.remove(data)

outputList = []
for inner_list in output:
    for element in inner_list:
        outputList.append(element)

outputData = " ".join(outputList)

zacateksoubor = open("zacatekfinalu.txt", "r")
zacatekfinalu = zacateksoubor.read()
zacateksoubor.close()

konecsoubor = open("konecfinalu.txt", "r")
konecfinalu = konecsoubor.read()
konecsoubor.close()

outputfile = open("output.kml", "w")
vystupdat = zacatekfinalu + outputData + konecfinalu
outputfile.write(vystupdat)
outputfile.close()
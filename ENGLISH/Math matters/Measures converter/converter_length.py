measures_current = input("Inform the measure current:\nM ==> Meter\nCM ==> Centimeter\nKM ==> Kilometers\nMM ==> Millimeters\nDM ==> Decimeters\nDAM ==> Decameters\nHM ==> Hectometer\n==> ").upper()
value = float(input("Inform the value: "))
next_measures = input("Inform the next measure:\nM ==> Meter\nCM ==> Centimeter\nKM ==> Kilometers\nMM ==> Millimeters\nDM ==> Decimeters\nDAM ==> Decameters\nHM ==> Hectometer\n==> ").upper()

if(measures_current != "M" and measures_current != "CM" and measures_current != "KM" and measures_current != "MM" and measures_current != "DM" and measures_current != "DAM" and measures_current != "HM"):
    print("Error, measures inválid!")
elif(next_measures != "M" and next_measures != "CM" and next_measures != "KM" and next_measures != "MM" and next_measures != "DM" and next_measures != "DAM" and next_measures != "HM"):
    print("Error, measures inválid!!")
else:
    #Meter for ...
    if(measures_current == "M" and next_measures == "CM"):
        print(f"{value}m ==> {value * 100}cm")
    elif(measures_current == "M" and next_measures == "KM"):
        print(f"{value}m ==> {value / 1000}km")
    elif(measures_current == "M" and next_measures == "MM"):
        print(f"{value}m ==> {value * 1000}mm")
    elif(measures_current == "M" and next_measures == "DM"):
        print(f"{value}m ==> {value * 10}dm")
    elif(measures_current == "M" and next_measures == "DAM"):
        print(f"{value}m ==> {value / 10}dam")
    elif(measures_current == "M" and next_measures == "HM"):
        print(f"{value}m ==> {value / 100}hm")
    #Centimeter for ...
    if(measures_current == "CM" and next_measures == "M"):
        print(f"{value}cm ==> {value / 100}m")
    elif(measures_current == "CM" and next_measures == "KM"):
        print(f"{value}cm ==> {value / 100000}km")
    elif(measures_current == "CM" and next_measures == "MM"):
        print(f"{value}cm ==> {value / 10}mm")
    elif(measures_current == "CM" and next_measures == "DM"):
        print(f"{value}cm ==> {value / 1000}dm")
    elif(measures_current == "CM" and next_measures == "DAM"):
        print(f"{value}cm ==> {value / 10000}dam")
    elif(measures_current == "CM" and next_measures == "HM"):
        print(f"{value}cm ==> {value * 10}hm")
    #Kilometers for ...

    
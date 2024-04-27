with open("data.csv") as file:
    s = 0
    fare = 0
    averageFare = 0
    fareSum = 0
    count = 0
    fareBool = True

    for line in file:
        if line.count("Sex") == 1:
            continue
        data = line.split(",")
        if data[5] != 'male':
            continue
        else:
            if fareBool:
                minFare = float(data[10])
                maxFare = float(data[10])
                fareBool = False

            fare = float(data[10])
            fareSum = fareSum + fare
            count += 1
            if fare < minFare:
                minFare = fare
            if fare > maxFare:
                maxFare = fare
    averageFare = fareSum / count

averageFare = round(averageFare, 2)
maxFare = round (maxFare,2)
minFare = round(minFare,2)

print("Средняя цена: " + str(averageFare)  + "\nМаксимальная цена: " + str(maxFare) + "\nМинимальная цена: " + str(minFare))


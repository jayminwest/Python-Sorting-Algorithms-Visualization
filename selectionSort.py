import time

def selection_sort(data, drawData, timeTick):
    indexingLength = range(0, len(data) - 1)

    for i in indexingLength:
        minValue = i #This changes the default min with each itteration
        drawData(data, ['green' if x < i else 'red' for x in range(len(data))])

        for j in range(i + 1, len(data)): # All items to the right of where i is
            drawData(data, ['grey' if x == j else 'green' if x <= i else 'red' for x in range(len(data))])
            time.sleep(timeTick)

            if data[j] < data[minValue]:
                minValue = j 

        if minValue != i:
            data[minValue], data[i] = data[i], data[minValue]

    drawData(data, ['green' for x in range(len(data))])
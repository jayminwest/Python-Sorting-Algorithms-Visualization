#ALL OF THIS TAKEN FROM THIS TUTORIAL SERIES: Python GUI with Tkinter Tutorial | Beginner Friendly | Sorting Algorithm Visualization https://www.youtube.com/watch?v=y6Nz56RHK_Q&ab_channel=Dennis
import time

def selection_sort(data, drawData, timeTick):
    indexingLength = range(0, len(data) - 1)

    for i in indexingLength:
        minValue = i #This changes the default min with each itteration

        for j in range(i + 1, len(data)): # All items to the right of where i is
            drawData(data, ['green' if x == j or x == i else 'red' for x in range(len(data))])
            time.sleep(timeTick)

            if data[j] < data[minValue]:
                minValue = j 

        if minValue != i:
            data[minValue], data[i] = data[i], data[minValue]

    drawData(data, ['green' for x in range(len(data))])
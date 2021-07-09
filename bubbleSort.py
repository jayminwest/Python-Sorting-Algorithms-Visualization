#ALL OF THIS TAKEN FROM THIS TUTORIAL SERIES: Python GUI with Tkinter Tutorial | Beginner Friendly | Sorting Algorithm Visualization
#DEFINITLEY CONTINUE THIS https://www.youtube.com/watch?v=y6Nz56RHK_Q&ab_channel=Dennis
import time

def bubble_sort(data, drawData, timeTick):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['green' if x == j or x ==j+1 else 'red' for x in range(len(data))])
                time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])

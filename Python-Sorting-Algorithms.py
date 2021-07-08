#Sorting Algorithms for Refrence
#ALL OF THIS TAKEN FROM THIS TUTORIAL SERIES: Python GUI with Tkinter Tutorial | Beginner Friendly | Sorting Algorithm Visualization
#DEFINITLEY CONTINUE THIS https://www.youtube.com/watch?v=y6Nz56RHK_Q&ab_channel=Dennis
from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title('Sorting Algorithms')
root.maxsize(900, 600)
root.config(bg='black')

#vars
selected_alg = StringVar()

def drawData(data):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1) #Changes based on the data being entred, bar size
    offset = 30
    spacing = 10
    normalizedData = [i / max(data) for i in data] #Makes it so the bargraph is realative to the values' sizes

    for i, height in enumerate(normalizedData):
        #Top Left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #Bottom Right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill="red")
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

def Generate():
    print('Alg Selected: ' + selected_alg.get())
    try:
        minVal = int(minEntry.get())
    except:
        minVal = 1
    try:
        maxVal = int(maxEntry.get())
    except:
        maxVal = 10
    try:
        size = int(sizeEntry.get())
    except:
        size = 10

    if minVal < 0: minVal = 0
    if maxVal > 100: maxVal = 100
    if size > 50 or size < 3: size = 25
    if minVal > maxVal: minVal, maxVal = maxVal, minVal

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal + 1))

    drawData(data)

UI_frame = Frame(root, width = 600, height= 200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

#GUI
#Row[0]
Label(UI_frame, text = "Algorithm", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Quick Sort', 'Insertion Sort', 'Selection Sort', 'Bubble Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)
Button(UI_frame, text="Generate", command=Generate, bg='red').grid(row=0, column=2, padx=5, pady=5)

#Row[1]
Label(UI_frame, text="Size ", bg="grey").grid(row=1, column=0, padx = 5, pady = 5, sticky=W)
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

Label(UI_frame, text="Min Value ", bg="grey").grid(row=1, column=2, padx = 5, pady = 5, sticky=W)
minEntry = Entry(UI_frame)
minEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

Label(UI_frame, text="Max Value ", bg="grey").grid(row=1, column=4, padx = 5, pady = 5, sticky=W)
maxEntry = Entry(UI_frame)
maxEntry.grid(row=1, column=5, padx=5, pady=5, sticky=W)


def makeRandomSequence():
    testSequence = []
    for i in range(20):
        testSequence.append(random.randint(0, 100))

    return testSequence

#n^2 or Nlog(n)
#Sorts based on a 'pivot' point, finds its position, then takes first and last unsorted items as next pivots
def quickSort(sequence):
    length = len(sequence)
    
    if length <= 1: #This is here to ignore sequences of just one number
        return sequence
    else: #this is everyother case
        pivot = sequence.pop() #.pop() takes the last element and returns it

    largerItems = []
    smallerItems = []

    for item in sequence:
        if item > pivot:
            largerItems.append(item)
        else: #less than and equal to items
            smallerItems.append(item)

    return quickSort(smallerItems) + [pivot] + quickSort(largerItems) #This puts the pivot point in the center of the sequence. Lower items on one side, larger on the other

#Divides sequence into two lists (sorted, unsorted), takes leftmost item in unsorted, puts it in sorted side and sorts it by comparing it to the first item in the sorted list until it is in place
#Faster than bubble and selection but at the same complexity
def insertionSort(sequenceA):
    indexingLength = range(1, len(sequenceA))

    for i in indexingLength:
        valueToSort = sequenceA[i]

        while sequenceA[i-1] > valueToSort and i > 0: #Item to left greater than item to right
            sequenceA[i], sequenceA[i-1] = sequenceA[i-1], sequenceA[i] #swaps values
            i = i - 1 #Stepping down the list

    return sequenceA

#Sets first item as minimum, every item smaller than that moves down the list, sorted list ends up on the left
#Less swaps needed than bubble sort
def selectionSort(sequenceA):
    indexingLength = range(0, len(sequenceA) - 1)

    for i in indexingLength:
        minValue = i #This changes the default min with each itteration

        for j in range(i + 1, len(sequenceA)): # All items to the right of where i is
            if sequenceA[j] < sequenceA[minValue]:
                minValue = j 

        if minValue != i:
            sequenceA[minValue], sequenceA[i] = sequenceA[i], sequenceA[minValue]

    return sequenceA

#Least efficent
#"bubbles" higher numbers to the top of the list
def bubbleSort(list):
    indexingLength = len(list) - 1
    sorted = False

    while not sorted:
         sorted = True
         for i in range(0, indexingLength):
             if list[i] > list[i + 1]:
                 sorted = False
                 list[i], list[i + 1] = list[i + 1], list[i]

    return list

# print("Quick Sort: ", quickSort(makeRandomSequence()))
# print("Insertion Sort: ", insertionSort(makeRandomSequence()))
# print("Selection Sort: ", selectionSort(makeRandomSequence()))
# print("Bubble Sort: ", bubbleSort(makeRandomSequence()))

root.mainloop()
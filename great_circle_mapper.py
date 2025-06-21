import airportsdata
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from itertools import pairwise
import requests
import os

API_KEY = os.getenv("MAPS_STATIC_API_KEY")

#Load data from airport data library
airports = airportsdata.load()  # key is the ICAO identifier (the default)

#Create root window
parent = tk.Tk()
parent.title("Airport Entries")
 


#Function for opening world map
def displayMap():
    worldMapWindow = Toplevel(parent)
    worldMapWindow.title("Great Circle Mapper")

    worldMapCanvas = Canvas(worldMapWindow, width=1020, height=800)  
    worldMapCanvas.pack()
    
    worldMap = tk.PhotoImage(file="worldMap.gif")
    worldMapCanvas.create_image(0, 0, anchor=NW, image=worldMap)

    parent.mainloop()



def mapRequest(coordinatesList):
    api = API_KEY
    url = "https://maps.googleapis.com/maps/api/staticmap?"
    markers = ""
    paths = ""

    for airport, nextAirport in pairwise(coordinatesList):
        #airport[0] is the latitude and airport[1] is the longitude
        markers += "&markers=anchor:center%7Cicon:https://tinyurl.com/y9f45hdh%7C" + str(airport[0]) + "," + str(airport[1]) 
        paths += "&path=color:0xff0404%7Cweight:1%7Cgeodesic:true%7C" + str(airport[0]) + "," + str(airport[1]) + "%7C" + str(nextAirport[0]) + "," + str(nextAirport[1])
        
    #Ensures that last airport in coordinatesList gets a marker
    lastAirport = coordinatesList[-1]
    markers += "&markers=anchor:center%7Cicon:https://tinyurl.com/y9f45hdh%7C" + str(lastAirport[0]) + "," + str(lastAirport[1]) 

    # get method of requests module, returns response object
    request = requests.get(url + "center=30,10.5&zoom=1&scale=2&maptype=satellite&size=510x400&key=" + api + markers + paths)
    
    # wb mode is stand for write binary mode. Typical mode when working with images
    file = open('worldMap.gif', 'wb')
    
    # request.content obtains the contents of the request. The image is placed in the file
    file.write(request.content)
    file.close()

    #Calls displayMap() function to display the map
    displayMap()



#Sort input into list, obtain latitude and longitude from library, call mercator projection function to convert to coordinates, call displaymap function
def inputHandling():
    try:
        input = entry2_value.get()
        inputList = input.split("-")
        coordinatesList = []

        for code in inputList:
            latitude = airports[code]["lat"]
            longitude = airports[code]["lon"]
            coordinates = [latitude, longitude]
            coordinatesList.append(coordinates) 
            
        #Calls maps request function 
        mapRequest(coordinatesList)
    
    except KeyError:
        entry3 = Label(parent, text = "Invalid airport code.")
        entry3.pack()
        return


entry1 = Label(parent, text = "Type in ICAO airport codes separated by dash to display route." )
entry2_value = StringVar()
entry2 = Entry(parent, width=50, textvariable=entry2_value)
button = Button(parent, text="Check Route", command=inputHandling)

entry1.pack()
entry2.pack()
button.pack()
parent.mainloop()
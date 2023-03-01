import cmpt120imageProjHelper
import cmpt120imageManip
import tkinter.filedialog
import pygame

pygame.init()

# list of system options
system = [
    "Q: Quit",
    "O: Open Image",
    "S: Save Current Image",
    "R: Reload Original Image",
]

# list of basic operation options
basic = [
    "1: Apply Red Filter",
    "2: Apply Green Filter",
    "3: Apply Blue Filter",
    "4: Apply Sepia Filter",
    "5: Apply Warm Filter",
    "6: Apply Cold Filter",
    "7: Switch to Advanced Fuctions",
]

# list of advanced operation options
advanced = [
    "1: Rotate Left",
    "2: Rotate Right",
    "3: Double Size",
    "4: Half Size",
    "5: Locate Fish",
    "6: Switch to Basic Functions",
]

# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    menuString = ["Welcome to CMPT 120 Image Processer!"]
    menuString.append("")  # an empty line
    menuString.append("Choose the following options:")
    menuString.append("")  # an empty line
    menuString += system
    menuString.append("")  # an empty line

    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-7)...")
    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-6)...")
    else:
        menuString.append("Error: Unknown mode!")

    return menuString


# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary (e.g, the mode attribute if the user switches mode)
def handleUserInput(state, img):
    """
    Input:  state - a dictionary containing the state values of the application
            img - the 2d array of RGB values to be operated on
    Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """
    userInput = state["lastUserInput"].upper()
    # handle the system functionalities
    if userInput.isalpha():  # check if the input is an alphabet
        print("Log: Doing system functionalities " + userInput)

        if userInput == "Q":  # this case actually won't happen, it's here as an example
            print("Log: Quitting...")

        elif userInput == "O": # open image
            print("Log: Opening Image...")
            tkinter.Tk().withdraw()
            global openFilename
            openFilename = tkinter.filedialog.askopenfilename()
            img = cmpt120imageProjHelper.getImage(openFilename)
            cmpt120imageProjHelper.showInterface(img, "Image Opened",generateMenu(appStateValues))

        elif userInput == "S": # save image
            print("Log: Saving Current Image...")
            tkinter.Tk().withdraw()
            saveFilename = tkinter.filedialog.asksaveasfilename()
            cmpt120imageProjHelper.saveImage(img, f"{saveFilename}.jpg")
            cmpt120imageProjHelper.showInterface(img, "Image Saved",generateMenu(state))

        elif userInput == "R": # reload image
            print("Log: Reloading Orginal Image")
            img = cmpt120imageProjHelper.getImage(openFilename)
            cmpt120imageProjHelper.showInterface(img, "Image Reloaded",generateMenu(state))

        else: # unrecognized user input
            print("Log: Unrecognized user input: " + userInput) 
            cmpt120imageProjHelper.showInterface(img, "Choose Q,O,S or R",generateMenu(state))

    # or handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit():  # has to be a digit for manipulation options
        print("Log: Doing manipulation functionalities " + userInput)

        if state["mode"] == "basic":
            if userInput == "1": # red
                print("Log: Performing " + basic[int(userInput) - 1])
                img = cmpt120imageManip.redFilter(img)
                cmpt120imageProjHelper.showInterface(img, "Red Filter Applied",generateMenu(state))

            elif userInput == "2": # green
                print("Log: Performing " + basic[int(userInput) - 1])
                img = cmpt120imageManip.greenFilter(img)
                cmpt120imageProjHelper.showInterface(img,"Green Filter Applied",generateMenu(state))

            elif userInput == "3": # blue
                print("Log: Performing " + basic[int(userInput) - 1])
                img = cmpt120imageManip.blueFilter(img)
                cmpt120imageProjHelper.showInterface(img,"Blue Filter Applied",generateMenu(state))

            elif userInput == "4": # sepia
                print("Log: Performing " + basic[int(userInput) - 1])
                img = cmpt120imageManip.sepiaFilter(img)
                cmpt120imageProjHelper.showInterface(img,"Sepia Filter Applied",generateMenu(state))

            elif userInput == "5": # warm
                print("Log: Performing " + basic[int(userInput) - 1])
                img = cmpt120imageManip.warmFilter(img)
                cmpt120imageProjHelper.showInterface(img,"Warm Filter Applied",generateMenu(state))

            elif userInput == "6": # cold
                print("Log: Performing " + basic[int(userInput) - 1])
                img = cmpt120imageManip.coldFilter(img)
                cmpt120imageProjHelper.showInterface(img,"Cold Filter Applied",generateMenu(state))

            elif userInput == "7": # switch to advanced
                print("Log: Performing " + basic[int(userInput) - 1])
                state["mode"] = "advanced"
                cmpt120imageProjHelper.showInterface(img, "Advanced Mode ",generateMenu(state))

            else: # unrecognized user input
                print("Log: Unrecognized user input: " + userInput)
                cmpt120imageProjHelper.showInterface(img, "Choose from 1-7",generateMenu(state))

        elif state["mode"] == "advanced": # check mode

            if userInput == "1": # rotate left
                print("Log: Performing " + advanced[int(userInput) - 1])
                img = cmpt120imageManip.rotateLeft(img)
                cmpt120imageProjHelper.showInterface(img, "Rotated Left",generateMenu(state))

            elif userInput == "2": # rotate right
                print("Log: Performing " + advanced[int(userInput) - 1])
                img = cmpt120imageManip.rotateRight(img)
                cmpt120imageProjHelper.showInterface(img, "Rotated Right",generateMenu(state))

            elif userInput == "3": # double size
                print("Log: Performing " + advanced[int(userInput) - 1])
                img = cmpt120imageManip.doubleSize(img)
                cmpt120imageProjHelper.showInterface(img, "Size Doubled",generateMenu(state))

            elif userInput == "4": # half size
                print("Log: Performing " + advanced[int(userInput) - 1])
                img = cmpt120imageManip.halfSize(img)
                cmpt120imageProjHelper.showInterface(img, "Size Halved",generateMenu(state))

            elif userInput == "5": # locate fish
                print("Log: Performing " + advanced[int(userInput) - 1])
                box = cmpt120imageManip.locateFish(img)
                cmpt120imageManip.makeGreenBox(img, box[0], box[1], box[2], box[3])
                cmpt120imageProjHelper.showInterface(img, "Fish Located",generateMenu(state))

            elif userInput == "6": # switch to basic
                print("Log: Performing " + advanced[int(userInput) - 1])
                state["mode"] = "basic"
                cmpt120imageProjHelper.showInterface(img, "Basic Mode",generateMenu(state))

            else: # unrecognized user input
                print("Log: Unrecognized user input: " + userInput)
                cmpt120imageProjHelper.showInterface(img, "Choose from 1-6",generateMenu(state))

    else:  # unrecognized user input
        print("Log: Unrecognized user input: " + userInput)
    return img


# *** DO NOT change any of the code below this point ***

# use a dictionary to remember several state values of the application
appStateValues = {
    "mode": "basic",
    "lastOpenFilename": "",
    "lastSaveFilename": "",
    "lastUserInput": ""
}

currentImg = cmpt120imageProjHelper.getBlackImage(300, 200)  # create a default 300 x 200 black image
cmpt120imageProjHelper.showInterface(currentImg,"No Image",generateMenu(appStateValues))  # note how it is used

# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.QUIT:  #another way to quit the program is to click the close botton
            keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")

import pyautogui
screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight) # Screen Height and Width

currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY) # Mouse Pointer position
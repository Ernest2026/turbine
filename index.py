import pyautogui
# import pytesseract
# from PIL import Image

# If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\\tesseract'
# imgsrc = r'C:\Users\Ernesto\Pydesktop\image.png'

# imgg = Image.open(imgsrc)
# count = pytesseract.image_to_string(imgg).splitlines()[1:15]
# for x in count:
#     if len(x.split(" ")) > 1:
#         print(x.split(" ")[1])


# print(pytesseract.get_languages(config=''))


# screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
# print('screen is ', screenWidth, screenHeight)
# # (2560, 1440)

# try:
#     while True:
#         currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
#         print('current mouse is ', currentMouseX, currentMouseY)
# except KeyboardInterrupt:
#     print("keyboard interrupt")
# (1314, 345)

# pyautogui.moveTo(694, 1563) # Move the mouse to XY coordinates.

# pyautogui.click()          # Click the mouse.

# pyautogui.moveTo(2014, 332)      # Move the mouse 400 pixels to the right of its current position.
# pyautogui.click()     # Double click the mouse.

im = pyautogui.screenshot('hello.png')
# print("image is ")
# print(im)

# # pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked.









# import easyocr
# reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
# result = reader.readtext('image.png')

# import torch
# print(torch.cuda.is_available())




# To install easyocr
# https://github.com/pytorch/pytorch/issues/114127#issuecomment-1910956339

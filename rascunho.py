
>>> pyautogui.click(x=100, y=200)  # move to 100, 200, then click the left mouse button.

>>> pyautogui.click(button='right')  # right-click the mouse

>>> pyautogui.click(clicks=2)  # double-click the left mouse button
>>> pyautogui.click(clicks=2, interval=0.25)  # double-click the left mouse button, but with a quarter second pause in between clicks
>>> pyautogui.click(button='right', clicks=3, interval=0.25)  ## triple-click the right mouse button with a quarter second pause in between clicks


>>> pyautogui.doubleClick()  # perform a left-button double click


from PIL import ImageGrab

image = ImageGrab.grab(bbox=(200,300,1,1))
image.save('image2.png')



import PIL.ImageGrab
import mouse


while True:
    rgb = PIL.ImageGrab.grab(bbox = None)
    rgb2=(253, 146, 134)
    print (rgb.getpixel((510, 510)))
    if (rgb.getpixel((510, 510))) == rgb2:
        mouse.click()
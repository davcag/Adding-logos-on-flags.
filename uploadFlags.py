import pyautogui, os, time
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

for filename in os.listdir("done"):
    pyautogui.click(1212, 988) # click +
    pyautogui.typewrite('d:\\pl\\python\\FlagsForPierre\\done\\' + filename)
    pyautogui.click(798, 509) # choose file
    pyautogui.typewrite(filename[:-(len(".png"))])
    pyautogui.click(1594, 803) # click upload
    time.sleep(3)

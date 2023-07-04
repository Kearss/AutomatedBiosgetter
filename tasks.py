from RPA.Desktop import Desktop
from RPA.Windows import Windows
from robocorp import browser
import time
from robocorp.tasks import task

desktop = Desktop()
Windows = Windows()

@task
@task
def openmsinfo():
    Windows.click("id:SearchButton")
    time.sleep(1)
    desktop.type_text("run")
    desktop.press_keys("enter")
    desktop.type_text("msinfo32")
    desktop.press_keys("enter")
    desktop.move_mouse("offset:0,-600")
    time.sleep(10)
    desktop.click()
    desktop.press_keys("CTRL","C")    

    browser.configure(
            browser_engine="chrome",
            screenshot="only-on-failure",
            headless=False,
        )
    page = browser.goto("https://www.google.com/")
    page.click("id=W0wltc")
    page.click("id=APjFqb")
    desktop.press_keys("CTRL","V")
    desktop.press_keys("ENTER")
    desktop.move_mouse("offset:-550,-150")
    time.sleep(5)
    desktop.click()
 


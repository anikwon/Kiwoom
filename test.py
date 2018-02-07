from pywinauto import application
from pywinauto import timings
import time
import os
app = application.Application()
app.start("D:/Program Files2/KiwoomHero4/Bin/NKStarter.exe")

title = "영웅문4 Login"
dlg = timings.WaitUntilPasses(20, 0.5, lambda: app.window_(title=title))

# pass_ctrl = dlg.Edit2
# pass_ctrl.SetFocus()
# pass_ctrl.TypeKeys('gjrenek1')
#
# cert_ctrl = dlg.Edit3
# cert_ctrl.SetFocus()
# cert_ctrl.TypeKeys('gjrenek1KB*')

btn_ctrl = dlg.Button0
btn_ctrl.Click()

time.sleep(50)
os.system("taskkill /im nkrunlite.exe")
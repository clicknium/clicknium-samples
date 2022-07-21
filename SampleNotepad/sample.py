import subprocess
from clicknium import locator, ui

process = subprocess.Popen("notepad")
ui(locator.notepad.document_15).set_text("hello automation")
ui(locator.notepad.button_close).click()
ui(locator.notepad.button_commandbutton_7).click()

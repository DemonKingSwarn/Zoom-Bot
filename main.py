import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

def sign_in(meetingid, pswd):
  #opens up the zoom app
  subprocess.call("./Applications/zoom.us.app")

  time.sleep(10)

  #clicks the join button
  join_btn = pyautogui.locateCenterOnScreen('join_button.PNG')
  pyautogui.moveTo(join_btn)
  pyautogui.click()

  #type the meeting id
  meetingID_btn = pyautogui.locateCenterOnScreen('meeting_id_button.PNG')
  pyautogui.moveTo(meetingID_btn)
  pyautogui.click()
  pyautogui.write(meetingid)

  #disable both camera and mic 
  media_btn = pyautogui.locateAllOnScreen('media_button.PNG')
  for btn in media_btn:
    pyautogui.moveTo(btn)
    pyautogui.click()
    time.sleep(2)

  #hits the join button
  join_button = pyautogui.locateCenterOnScreen('join_btn.PNG')
  pyautogui.moveTo(join_button)
  pyautogui.click()

  time.sleep(5)
  #type the password and hit enter 
  meeting_pswd_btn = pyautogui.locateCenterOnScreen('password.jpeg')
  pyautogui.moveTo(meeting_pswd_btn)
  pyautogui.click()
  pyautogui.write(pswd)
  pyautogui.press('enter')

  #reading the file
  df = pd.read_csv('./timings.csv')

  while True:
    #checking of the current time exists in our csv file
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):

      row = df.loc[df['timings'] == now]
      m_id = str(row.iloc[0, 1])
      m_pswd = str(row.iloc[0, 2])

      sign_in(m_id, m_pswd)
      time.sleep(40)
      print("signed in")



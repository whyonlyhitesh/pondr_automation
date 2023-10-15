import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui

# Creating seperate file for each sequence
with open('sequence-analyse.txt', 'r') as file:
    contents = file.read()
    groups = contents.split('\n\n')
    for i, group in enumerate(groups):
        with open(f'seq_{i}.txt', 'w') as file:
            file.write(group)

# Setting number of sequences 
for n in range(0, i+1):
    with open(f'seq_{n}.txt', 'r') as file: # Reading the data  
        sequence = file.readlines()    # Setting sequence 
        url="http://pondr.com/" # URL of PONDR
        predictor1="checked"
        
        # Setting Firefox browser to be used
        browser = webdriver.Firefox() 
        browser.get(url)
        
        # wait for page to refresh
        browser.implicitly_wait(10) 
        
        # Selecting Predictor
        browser.find_element(By.NAME, 'VLXT')
        browser.find_element(By.NAME, 'XL1').click()
        browser.find_element(By.NAME, 'CAN').click()
        browser.find_element(By.NAME, 'VL3').click()
        browser.find_element(By.NAME, 'VSL2').click()
        browser.find_element(By.NAME, 'CDF').click()
        browser.find_element(By.NAME, 'CH').click()

        # Setting sequence
        password = browser.find_element(By.NAME, 'Sequence')
        password.send_keys(sequence)

        # Submiting query
        password = browser.find_element(By.NAME, 'submit_result').click()

        sleep(5)
        # Saving the results 
        pyautogui.hotkey('ctrl', 'p')
        pyautogui.hotkey('enter')
        sleep(3)
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')       
        sleep(7)
        # Quiting the browser
        browser.quit()
        # Renaming the saved pdf
        os.rename('Predictor of Natural Disordered Regions (PONDR).pdf', f'seq_{n}.pdf')

print("Data Saved")

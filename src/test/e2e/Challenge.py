#! /usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\\Users\\nagar\\Drivers\\chromedriver.exe")

driver.maximize_window()

driver.get("http://localhost:3000/")

#Clicking the button
driver.find_element(By.XPATH, "//*[@id='home']/div/div/button/div/div/span").click()
time.sleep(2)

#Scrolling  till arrays challenge element found
element=driver.find_element_by_xpath("//*[@id='challenge']/div/div/h1")
driver.execute_script("arguments[0].scrollIntoView();",element)

#Wokring with table
get_table=driver.find_element(By.XPATH, "//*[@id='challenge']/div/div/div[1]/div/div[2]/table/tbody")

row_one=get_table.find_elements_by_xpath("//*[@id='challenge']/div/div/div[1]/div/div[2]/table/tbody/tr[1]/td")
r1_list=[]
for d in row_one:
    row1=d.text
    r1_list.append(int(row1))
#print(r1_list)

row_two=get_table.find_elements_by_xpath("//*[@id='challenge']/div/div/div[1]/div/div[2]/table/tbody/tr[2]/td")
r2_list=[]
for d in row_two:
    row2=d.text
    r2_list.append(int(row2))
#print(r2_list)

row_three=get_table.find_elements_by_xpath("//*[@id='challenge']/div/div/div[1]/div/div[2]/table/tbody/tr[3]/td")
r3_list=[]

for d in row_three:
    row3=d.text
    r3_list.append(int(row3))
#print(r3_list)

def findElement(arr,size):

    right_sum, left_sum = 0, 0

    for i in range(1, size):
        right_sum += arr[i]

    i, j = 0, 1

    while j < size:
        right_sum -= arr[j]
        left_sum += arr[i]

        if left_sum == right_sum:
            return i+1
        j += 1
        i += 1
    return -1

if __name__=="__main__":
    arr = r1_list
    n = len(arr)
    print(findElement(arr, n))
    arr = r2_list
    n = len(arr)
    print(findElement(arr, n))
    arr = r3_list
    n = len(arr)
    print(findElement(arr, n))

import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://todomvc.com/")

# Clicking on the React link
driver.find_element(By.CLASS_NAME, "link").click()

# Element through which all the tasks will be added
input_box = driver.find_element(By.ID, "todo-input")

# Task - 1

tasks = ["Learn Python", "Complete Wellfound Profile", "Apply on Linkedin - 10 companies"]
for task in tasks:
    input_box.send_keys(task)
    input_box.send_keys(Keys.ENTER)

time.sleep(2)

# Task - 2 - Mark the second task as complete

# These are all the added Tasks
all_tasks = driver.find_elements(By.XPATH, "//ul[@class='todo-list']/li")

second_task = all_tasks[1].find_element(By.CLASS_NAME, 'toggle')
second_task.click()

# Task - 3 -Delete the first one.

action = ActionChains(driver)
third_task = all_tasks[0]
action.move_to_element(third_task.find_element(By.CLASS_NAME, 'toggle')).perform()
action.move_to_element(third_task.find_element(By.CLASS_NAME, 'destroy')).click().perform()

# Task - 4  (Validate the task count)

time.sleep(2)
task_count = driver.find_element(By.CLASS_NAME, "todo-count").text
print(task_count)
assert "1" in task_count

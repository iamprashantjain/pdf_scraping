from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service	
import time
import pyautogui
from bs4 import BeautifulSoup



# # Set up WebDriver
# s = Service("E:\CampusX_DS\extra\webscraping\webscraping_complete_course\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Chrome(service=s)

# # Open URL
# url = "https://findaprovider.coordinatedcarehealth.com/search-results"
# driver.get(url)

# time.sleep(10)

# # Enter location
# location = driver.find_element(By.XPATH, "/html/body/div[1]/page-component/search-component/div/div/location-page/main/div/div[2]/div/md-card/location-selection/form/div/div[1]/div[1]/div/input")
# location.send_keys("Seattle, WA, USA")
# location.send_keys(Keys.ENTER)

# time.sleep(10)

# # Select plan from dropdown
# plan_dropdown = driver.find_element(By.XPATH, "/html/body/div[1]/page-component/search-component/div/div/location-page/main/div/div[2]/div/md-card/location-selection/form/div/div[1]/div[4]/div/div/div/select")
# select = Select(plan_dropdown)
# select.select_by_visible_text("Coordinated Care Medicaid")
# plan_dropdown.send_keys(Keys.TAB)
# driver.switch_to.active_element.send_keys(Keys.ENTER)
# time.sleep(2)

# # Click on Behavioral Health category
# wait = WebDriverWait(driver, 20)
# behavorial_health = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/page-component/search-component/div/div/main-component/main/div[6]/div[2]/div/div[2]/div/md-card/categories-container/div/category-tiles/category-tile-group[1]/div[3]/category-tile/p-standard-component/span")))
# behavorial_health.click()
# time.sleep(2)


# #clicking on professional using image
# professional = r"C:\Users\iampr\Desktop\1.png"
# professional_location = pyautogui.locateOnScreen(professional)

# if professional_location:
#     x, y, width, height = professional_location
#     center_x = x + width // 2
#     center_y = y + height // 2

#     pyautogui.click(center_x, center_y)



# #clicking on search using image
# search_box = r"C:\Users\iampr\Desktop\2.png"
# search_box_location = pyautogui.locateOnScreen(search_box)

# if search_box_location:
#     x, y, width, height = search_box_location
#     center_x = x + width // 2
#     center_y = y + height // 2

#     pyautogui.click(center_x, center_y)



# #infinite scrolling
# height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     time.sleep(10)
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if height == new_height:
#         break
#     height = new_height



# #saving complete html
# complete_html = driver.page_source


# # Save the complete HTML content to a file
# with open('acuity_page.html', 'w', encoding='utf-8') as f:
#     f.write(complete_html)



with open('acuity_page.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all provider div elements
provider_divs = soup.find_all("div", class_="row search-result-row")

names_list = []

for provider_div in provider_divs:
    # Extract name
    name_element = provider_div.find("h2", class_="text-theme-black")
    name = name_element.get_text()
    names_list.append(name)

# Print each name
for name in names_list:
    print(name)

# Print the total number of names
print("Total number of names:", len(names_list))
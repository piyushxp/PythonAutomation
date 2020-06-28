#automation Tests
from selenium import webdriver
chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()
chrome_browser.get('url')


#working with some html titles,Tests
print('Is this Title' in chrome_browser.title)

assert 'This is a Title' in chrome_browser.title

#Using some selectors given by selenium to work with element tags in html
button_text = chrome_browser.find_element_by_class_name('btn-primary')
print(button_text.get_attribute('innerHTML'))  # Prints the text 
#We can check if sthe text exists with this
assert 'The text in the tag' in chrome_browser.page_source


#Let's automate SIGN IN into a website with input tag
chrome_browser.find_elements_by_id('user-message')
user_message.clear()
user.message.send_keys('THE TEXT THAT NEEDS TO BE ADDED')

#Lets select the button and perform a click simulation after the automatd input
show_message_button = chrome_browser.find_element_by_class_name('btn-primary')
show_message_button.click()

output_message = chrome_browser.find_elements_by_id('display')

assert 'THIS IS AN SIMULATED AUTOMATED TEXT WITH PYTHON' in output_message.text



#Let's work with CSS
userbutton2 = chrome_browser.find_elements_by_css_selector()

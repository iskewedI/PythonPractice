from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://github.com")

signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

username_field = browser.find_element_by_id("login_field")
username_field.send_keys("username")

password_field = browser.find_element_by_id("password")
password_field.send_keys("password")

password_field.submit()

profile_link = browser.find_element_by_class_name("user-profile-link")

link_label = profile_link.get_attribute("innerHTML")

assert "anusername32" in link_label

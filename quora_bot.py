from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from openai import OpenAI

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open Quora login page
driver.get("https://www.quora.com/")

# Wait for the page to load
time.sleep(5)

# Find and click the login button
login_button = driver.find_element(By.XPATH, "//div[text()='Login']")
login_button.click()

# Wait for the login form to appear
time.sleep(5)

# Enter email
email_input = driver.find_element(By.NAME, "email")
email_input.send_keys("your_email@example.com")  # Replace with placeholder

# Enter password
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("your_password")  # Replace with placeholder

# Submit the form
password_input.send_keys(Keys.RETURN)

# Wait for the login process to complete
time.sleep(10)

driver.get("https://www.quora.com/answer")
time.sleep(5)

# Wait for the answer button to appear
# time.sleep(5)

# Find and click the answer button
answer_button = driver.find_element(By.XPATH, "//button[@role='button' and .//div[text()='Answer']]")
answer_button.click()

# Wait for the answer text to appear
time.sleep(5)

# Find the answer text
answer_text_element = driver.find_element(By.XPATH, "//span[@class='q-box qu-userSelect--text']//span")
extracted_text = answer_text_element.text

# Print the extracted text
print(extracted_text)

# Initialize OpenAI client
client = OpenAI()

response = client.chat.completions.create(
    model="databricks-meta-llama-3-3-70b-instruct",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant. Help me in writing answers to Quora questions."
        },
        {
            "role": "user",
            "content": extracted_text
        }
    ],
    temperature=0,
    top_p=0.95
)

print(response.choices[0].message.content)
llm_response = response.choices[0].message.content

time.sleep(10)

# Locate the editable div where the answer should be inserted
editable_div = driver.find_element(By.XPATH, "//div[@class='doc dark_mode empty' and @data-placeholder='Write your answer']")

# Insert the generated text into the editable div
driver.execute_script("arguments[0].innerHTML = arguments[1];", editable_div, llm_response)

# Find and click the post button
post_button = driver.find_element(By.XPATH, "//button[@class='q-click-wrapper puppeteer_test_modal_submit b17i7nxr b1l8alrs bobc9nh b1cg7ppz c1nud10e qu-active--textDecoration--none qu-focus--textDecoration--none qu-borderRadius--pill qu-alignItems--center qu-justifyContent--center qu-whiteSpace--nowrap qu-userSelect--none qu-display--inline-flex qu-bg--blue qu-tapHighlight--white qu-textAlign--center qu-cursor--pointer qu-hover--textDecoration--none' and @role='button']")
post_button.click()

time.sleep(10)

# Locate the radio button input element
radio_button = driver.find_element(By.XPATH, "//input[@type='radio' and @value='195177858']")

# Click the radio button to select it
radio_button.click()

time.sleep(5)

# Find and click the done button
done_button = driver.find_element(By.XPATH, "//button[@class='q-click-wrapper puppeteer_test_modal_submit b17i7nxr b1l8alrs bobc9nh b1cg7ppz c1nud10e qu-active--textDecoration--none qu-focus--textDecoration--none qu-borderRadius--pill qu-alignItems--center qu-justifyContent--center qu-whiteSpace--nowrap qu-userSelect--none qu-display--inline-flex qu-bg--blue qu-tapHighlight--white qu-textAlign--center qu-cursor--pointer qu-hover--textDecoration--none' and @role='button']")
done_button.click()

time.sleep(10)

# Close the browser
driver.quit()

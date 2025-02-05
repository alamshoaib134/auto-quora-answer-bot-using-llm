# Quora Bot

This project automates the process of logging into Quora, extracting a specific answer, generating a response using OpenAI, and posting the generated response back to Quora. It leverages Selenium for web automation and OpenAI's API for generating intelligent responses. This bot can be useful for automating repetitive tasks on Quora, such as answering frequently asked questions.

## Features

- **Automated Login**: Automatically logs into Quora using provided credentials.
- **Answer Extraction**: Extracts specific answers from Quora.
- **AI Response Generation**: Uses OpenAI to generate intelligent responses based on extracted answers.
- **Automated Posting**: Posts the generated responses back to Quora.
- **Error Handling**: Includes basic error handling for common issues like element not found.

## Requirements

- Python 3.9+
- Selenium
- WebDriver Manager
- OpenAI

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Quora_bot.git
    cd Quora_bot
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Set up your OpenAI API key as an environment variable:
    ```sh
    export OPENAI_API_KEY='your_openai_api_key'
    ```

2. Update the `quora_bot.py` file with your Quora email and password:
    ```python
    email_input.send_keys("your_email@example.com")  # Replace with your email
    password_input.send_keys("your_password")  # Replace with your password
    ```

3. Run the script:
    ```sh
    python quora_bot.py
    ```

## Demo

![Working Demo](Automated Quora Response using LLM.mp4)

## Notes

- Ensure that you have Chrome installed on your machine.
- The script uses `webdriver_manager` to automatically manage the ChromeDriver binary.
- The script includes a placeholder for the OpenAI API key. Make sure to set it up correctly before running the script.

## License

This project is licensed under the MIT License.

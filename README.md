# Discord Question-Answer Bot: Personal Studying Assistant

This repository contains the code and instructions to build an AI-powered Discord bot that serves as a personal studying assistant. The bot uses LlamaIndex, an open-source Python library, and the discord.py library to provide question-answering capabilities within a Discord server.

A more detailed tutorial is [here](https://medium.com/@wxxq84/building-a-discord-question-answer-bot-my-personal-studying-assistant-a57666979c3d).

## Getting Started

To set up the Discord bot and run it on your own server, follow these steps:

### Prerequisites

- Python3 installed on your machine
- Discord account and a personal server
- A Discord bot in the server and its token
- OpenAI API key

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/WENXU-codinglife/ReadingAssisBot.git
   ```

2. Navigate to the project directory:

    ```bash
    cd ReadingAssisBot
    ```

3. Create a virtual environment:

    ```bash
    python3 -m venv env
    ```

4. Activate the virtual environment:

    For Windows:
    ```bash
    env\Scripts\activate
    ```
    For macOS/Linux:
    ```bash
    source env/bin/activate
    ```   

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```    

### Configuration

1. Create a .env file in the project root.

2. Open the .env file and add your OpenAI API key:

    ```bash
    OPENAI_API_KEY=your_api_key_here
    DISCORD_BOT_TOKEN=your_discord_bot_token_here
    ```
### Running the Bot

    python3 RABot.py

### Usage

To interact with the bot, you can mention it in a Discord channel and ask questions. The bot will provide answers based on the provided data and materials. Make sure to feed the bot with relevant materials by following the instructions in the article.

### License

This project is licensed under the MIT License.
# penguin-translator

# **Overview**
This Python application listens for an Alt key press and translates selected text from the clipboard to Ukrainian, displaying the translation as a desktop notification.

# **Features**
**Translation:** Automatically translates selected text from the clipboard using Google Translate API.
**Notification:** Displays the translated text as a desktop notification with a 10-second timeout.

# **Requirements**
Python 3.x
Required Libraries:
- pynput
- pyperclip
- googletrans
- notify2
  
# **Installation**

### Clone the repository:

Copy code
```
git clone https://github.com/p-i-r-u-m/penguin-translator
```

### Install dependencies:
Copy code
```
pip install pynput
pip install pyperclip
pip install googletrans==4.0.0-rc1
pip install notify2
```

# Usage
Run the script:
Copy code
```
python3 PenguinTranslator.py
```
### How to use
1. Copy text to clipboard.
2. Press Alt key (Right Alt) to trigger translation and notification.
   
# Notes
Ensure your system has access to the internet for translation API calls.
Adjust notification timeout (notification.set_timeout(10000)) in translate_text() function if needed.

# Author
Created by pirum.


# AI-Powered-Medical-Chatbot
An AI-powered medical chatbot that assists users with general health inquiries through voice and text. It may include support for medical image analysis using computer vision, enabling a more interactive and accessible healthcare experience. Built with NLP, speech recognition, and vision models for end-to-end functionality.


Check python & pip is installed
python3 --version #Python 3.12.x
pip3 --version  #pip 24.x.x or newer

# To Upgrade
pip3 install --upgrade pip

# Step by step guide to setup an environment locally
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
brew --version  #Homebrew 4.x.x

brew install python 
brew reinstall python@3.13 #if it still point to old
which python3  #/opt/homebrew/bin/python3
/opt/homebrew/bin/python3 --version  #Python 3.13.x


### Using `pip` and `venv`
#### Create a Virtual Environment:
```
python -m venv venv
```

#### Activate the Virtual Environment:
**macOS/Linux:**
```
source venv/bin/activate
```

**Windows:**
```
venv\Scripts\activate
```

#### Install Dependencies:
```
pip install -r requirements.txt
```







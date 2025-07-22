Installation Guide for RSA Encryption GUI Project
---------------------------------------------------

## ✅ Prerequisites
- Python 3.7 or newer
- Internet connection to install dependencies


## 🔧 macOS / Linux

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install required dependencies
pip install -r requirements.txt

# Run the application
python main.py
```


## 🪟 Windows

```cmd
:: Create virtual environment
python -m venv venv

:: Activate virtual environment
venv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt

:: Run the application
python main.py
```


## 📌 Notes
- On first run, keys will be generated and saved under the `keys/` directory.
- Encrypted files are saved automatically in the `output/` folder with a timestamp.
- Only `.txt` files encoded in UTF-8 are supported for input.

---
Happy encrypting! 🔐
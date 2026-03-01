<h1 align="center">🔳 QR Code Generator</h1>

<p align="center">
  <b>A clean, minimal Python script that turns any URL or text into a scannable QR code — instantly.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Library-qrcode-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Image-Pillow-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Day-1%20of%20Daily%20Build-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" />
</p>

---

## 📖 About

This is **Day 1** of my daily project-building challenge — where I build and ship one project every single day until I land my first dev role.

The goal of this project isn't to be complex — it's to be clean, complete, and well-documented. A simple QR Code Generator built from scratch using Python, packaged with a proper repo structure, README, and license.

> **Input a URL or text → Get a QR code image saved instantly.** That's it. Simple wins.

---

## ✨ Features

- 📥 Accepts any URL or text as input
- ⚡ Generates a QR code in seconds
- 💾 Saves output as `qrcode.png` in the project directory
- 🧹 Clean, well-commented beginner-friendly code
- 📦 Proper repo structure with `.gitignore`, `LICENSE`, and `requirements.txt`

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Core scripting language |
| `qrcode` | QR code generation |
| `Pillow` | Image rendering and saving |

---

## 📁 Project Structure

```
qr-code-generator/
├── main.py            # Core script
├── requirements.txt   # Dependencies
├── .gitignore         # Ignores cache, venv, generated files
├── LICENSE            # MIT License
└── README.md          # You're here!
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/MohammadFayasKhan/qr-code-generator.git
cd qr-code-generator
```

### 2. Set up a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the script
```bash
python main.py
```

You'll be prompted to enter a URL or any text. The QR code image will be saved as `qrcode.png` in the project folder.

---

## 💡 How It Works

```python
import qrcode

url = input("Enter the URL:").strip()   # Take user input
qr = qrcode.QRCode()                    # Create QR object
qr.add_data(url)                        # Add data
img = qr.make_image()                   # Generate image
img.save("qrcode.png")                  # Save to disk
```

Clean. Simple. Does exactly what it needs to.

---

## 🧠 Skills Demonstrated

- ✅ Python scripting fundamentals
- ✅ User input handling
- ✅ Third-party library integration
- ✅ File I/O in Python
- ✅ GitHub repo setup best practices (README, `.gitignore`, LICENSE)

---

## 📅 Daily Build Challenge

This is **Day 1** of a public challenge where I build one project every day.  
Follow along on [LinkedIn](https://linkedin.com) as I post daily updates.

| Day | Project | Status |
|-----|---------|--------|
| 01  | QR Code Generator | ✅ Done |
| 02  | Coming soon... | ⏳ |

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

<p align="center">
  Made with ❤️ as part of a daily build challenge · <b>Day 1 of ∞</b>
</p>

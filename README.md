# 🎨 Photo Palette Generator

**Photo Palette Generator** is a Flask-based web application that lets you upload an image and instantly extract its top colors.  
It displays both **HEX** and **RGB** codes in a clean, modern UI, perfect for designers, developers, and artists.

---

## 📸 Screenshots

### 🏠 Homepage
<img width="2235" height="1194" alt="Screenshot 2025-08-15 201941" src="https://github.com/user-attachments/assets/b5934cd6-d781-44fe-a8d1-61a7c88259d1" />


### 🎯 Color Palette Result
<img width="2235" height="1195" alt="Screenshot 2025-08-15 202000" src="https://github.com/user-attachments/assets/b3b3ba1d-8302-4f2e-bba5-7a6ee29f4297" />


---

## 🚀 Features

- 📂 **Upload Images** and extract top colors  
- 🎨 **View HEX & RGB** values instantly  
- 📋 **Copy color codes** with a click  
- ⚡ **Fast & lightweight** — powered by [Colorgram.py](https://pypi.org/project/colorgram.py/)  
- 💡 **Responsive design** using Bootstrap 5  
- 🔒 **File upload limit** to prevent large uploads (default: 2 MB)  

---

## 🛠️ Technologies Used

- **Python 3.11+**
- **Flask** (web framework)
- **Colorgram.py** (color extraction)
- **Bootstrap 5** (UI styling)
- **Werkzeug** (secure file handling)
- **HTML / CSS / JavaScript** (frontend)

---
---

## 📂 Project Structure
Photo-Palette-Generator/
│
├── static/               # CSS, JS, and images (if any separate files added)
├── templates/            # HTML template files
│   └── index.html        # Main homepage template with upload form and color results
├── app.py                # Main Flask application file with routes and color extraction
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation

```


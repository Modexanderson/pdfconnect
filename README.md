# 📚 PDFConnect

**PDFConnect** is an academic resource hub built with Django that organizes and serves categorized PDFs across various fields of study. It is designed to help students easily access learning materials in disciplines such as medicine, law, engineering, agriculture, education, and more.

---

## 🌟 Features

* 🗂 **Organized by Discipline**: PDFs grouped by faculties like Clinical Sciences, Engineering, Law, etc.
* 🔍 **Search & Filter**: Easily find documents relevant to your field.
* 🧾 **Static Resource Hosting**: PDFs are hosted and accessible via a structured folder system.
* 🌐 **Template-based UI**: Clean, template-driven front end.
* 💠 **Django-Powered**: Built with Django for rapid deployment and scalability.

---

## 📁 Repository Structure

```
pdfconnect/
├── agriculture/
├── art/
├── basicmedicalsciences/
├── clinicalsciences/
├── dentalsciences/
├── education/
├── engineering/
├── enviromentalsciences/
├── healthsciencesandtechnology/
├── law/
├── managementsciences/
├── naturalsciences/
├── pharmaceuticalsciences/
├── socialsciences/
├── veterinarymedecine/
├── pdfs/                  # Centralized PDF storage
├── static/images/         # Static assets like icons or thumbnails
├── templates/             # HTML templates
├── db.sqlite3             # SQLite database
├── manage.py              # Django management script
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Modexanderson/pdfconnect.git
cd pdfconnect
```

### 2. Set Up a Virtual Environment (optional but recommended)

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt  # (create this if not already present)
```

### 4. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to access the app.

---

## 🛠 Technologies Used

* **Python 3**
* **Django**
* **SQLite** (default dev database)
* **HTML/CSS (Django templates)**

---

## ✅ To Do / Improvements

* 🔐 Add user authentication (students, admins)
* 📄 Add upload interface for admin users
* 📝 Add metadata (e.g., tags, year, course title)
* 📱 Improve responsive design for mobile
* 🔎 Enable advanced search and filtering

---

## 🤝 Contributing

Want to help improve PDFConnect?

1. Fork the repo
2. Create your feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add my feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Submit a pull request

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).
Use it, modify it, share it.

---

## 🙌 Acknowledgements

Developed by [Modexanderson](https://github.com/Modexanderson).
Designed to help students connect with the resources they need, faster and simpler.

# progammieren_2_aufgabe_2-4
This repository is used for exercise 2 - 4 of the programming lecture.

Fictitious sensor data is imported from CSV-file and text-files. On the Homepage (main.py) a user is selected.    
read_data.py contains the functions to import data for the user selection.    
red_pandas.py contains the functions to create and adapt dataframes for visualisation in interactive_plot.py.

---

### Requirements

- Python 3.12 or newer
- Git
- Internet connection for installing dependencies
- PDM 2.26 or newer

to install PDM, follow the instructions on the official project website: https://pdm-project.org/

---

### Clone the Project

Clone the repository:

```bash
git https://github.com/MarcWechselberger/programmieren_2_aufgabe_2-4.git
cd programmieren_2_aufgabe_2-4
```

---

### Install Dependencies

Install all required packages:

```bash
pdm install
```

This will:

- install all Python dependencies
- create a virtual environment
- use the versions defined in `pdm.lock`

---

### Start the Streamlit Application

Run the following command to start the Streamlit app:

```bash
streamlit run main.py
```
or

```bash
streamlit run interactive_plot.py
```

After executing the command, Streamlit starts a local web server and opens the application in your browser.

By default, the app will be available at:

```text
http://localhost:8501
```

If the browser does not open automatically, copy the URL from the terminal and open it manually.

---

### Screenshot

![Hier sollte jetzt ein Screenshot sein!](/data/pictures/screenshot.png)

---

### Project Structure

```text
programmieren_2_aufgabe_2-4/
│
├── data/
│   ├── activities/
│   │   └── activity.csv
│   ├── ekg_data
│   │   ├── 01_Ruhe.txt
│   │   ├── 02_Ruhe.txt
│   │   ├── 03_Ruhe.txt
│   │   ├── 04_Ruhe.txt
│   │   └── ReadMe.txt
│   ├── pictures
│   │   ├── bl.jpg
│   │   ├── js.jpg
│   │   ├── none.jpg
│   │   ├── screenshot.png
│   │   └── tb.jpg
│   └── person_db.json
├── interactive_plot.py
├── main.py
├── my_first_pandas.py
├── pdm.lock
├── pyproject.toml
├── read_data.py
├── read_pandas.py
└── README.md
```

---

### License

No License

---

### Authors

Nicolas Unterweger   
Emmanuel Tilg   
Marc Wechselberger   
GitHub: https://github.com/MarcWechselberger
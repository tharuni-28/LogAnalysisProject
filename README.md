# Log Analysis Project

A Flask-based web application designed to parse, analyze, and visualize log files.

## Project Structure

```

LogAnalysisProject/
│
├── templates/
│   ├── index.html       # Main upload / input dashboard
│   └── result.html      # Results and analysis visualization page
│
├── venv/                # Python virtual environment
├── app.py               # Main Flask application entry point
└── README.md

```

## Features

- **Log File Upload:** Upload and process log files directly through the web UI (`index.html`).
- **Log Parsing & Analysis:** Backend analysis implemented in Python (`app.py`).
- **Results Display:** Interactive output and results rendered via `result.html`.

## Prerequisites

- Python 3.x
- `pip` (Python package installer)

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/tharuni-28/LogAnalysisProject.git](https://github.com/tharuni-28/LogAnalysisProject.git)
   cd LogAnalysisProject

```

2. **Create and activate a virtual environment:**
* **On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1

```


* **On Windows (CMD):**
```cmd
venv\Scripts\activate.bat

```


* **On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate

```




3. **Install dependencies:**
```bash
pip install flask Werkzeug Jinja2 Click

```



## Running the Application

1. Ensure your virtual environment is active.
2. Start the Flask server:
```bash
python app.py

```


3. Open your browser and navigate to:
```
[http://127.0.0.1:5000](http://127.0.0.1:5000)

```



## Usage

1. Open the homepage (`index.html`).
2. Upload or submit your log file for analysis.
3. View the detailed log breakdown on the results page (`result.html`).

```

> **Tip:** Consider adding a `.gitignore` file to exclude the `venv/` directory from being tracked by Git, as virtual environments should generally not be committed to GitHub.

```

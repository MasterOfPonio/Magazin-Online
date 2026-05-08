# Magazin-Online
Exemplu proiect pentru folosire python UI, baze de date si REST API <br/>
Exmeplifcam si lucrul cu Git

## Setup & Run

```bash
# 1. Clone the repository
git clone https://github.com/MasterOfPonio/Magazin-Online.git
cd Magazin-Online

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations  ← REQUIRED (db.sqlite3 is not committed)
cd magazin_online
python manage.py migrate

# 5. Start the development server
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

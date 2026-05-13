# Windows Environment Setup Guide

## Prerequisites Installation 

### Step 1: Install Visual Studio Code
- Download Visual Studio Code from https://code.visualstudio.com/
- Install and launch Visual Studio Code

### Step 2: Install Python
- Download Python 3.8+ from https://www.python.org/downloads/windows/
- **Important**: Check "Add Python to PATH" during installation
- Verify installation: `python --version`

### Step 3: Install Make (Optional)
- Download from http://gnuwin32.sourceforge.net/packages/make.htm
- Add to Windows PATH: `C:\Program Files (x86)\GnuWin32\bin`
- Verify installation: `make --version`

**Note:** Make will have to be added to the path manually. Go to 'Edit environment variables' on your windows laptop and click on the PATH configurations. Add the path as above, and OK.

## Project Setup

### Step 1: Download ZIP
**Note:** Project team will likely do this, and distribute copies to the WEX laptops.
- https://github.com/jasmine-smith_hpeprod/stem-work-experience-2026
- `<> Code`
- `Download ZIP `

### Step 2: Create Virtual Environment
```powershell
python -m venv venv

# In order to run scripts, you may need to use the following:
Set-ExecutionPolicy -Scope CurrentUser Unrestricted

venv\Scripts\activate
pip install -r requirements.txt
```

### Step 3: Database Setup
```powershell
# Setup database schema and data
make setup-db

# Or without make:
python database/migrations/migrate.py

# Test database connection (if sqlite3 is installed)
make db-shell

# Or without make:
sqlite3 facts.db

# Quit database shell
.quit
```

### Step 4: Run Application
```powershell
python app.py
```

## Expected Output Sequence
- **Setup DB**: "Migration complete: facts table created and sample data inserted."
- **DB Shell**: Opens SQLite prompt `sqlite>`
- **Success**: Can run SQL commands like `SELECT * FROM facts;`

## Cleanup (Before Distributing to Students)
```powershell
# Deactivate virtual environment
deactivate

# Delete the database file
Remove-Item facts.db

# Remove virtual environment folder
Remove-Item -Recurse -Force venv
```

## Troubleshooting Notes
- If `make` fails: Run `python database/migrations/migrate.py` directly
- Database file is stored as: `facts.db` in the project root
- To inspect database: `sqlite3 facts.db` then run SQL commands

---

This setup ensures all Windows laptops will have the necessary tools properly configured and PATH variables set correctly.
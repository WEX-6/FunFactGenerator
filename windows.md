# Windows Environment Setup Guide

## Prerequisites Installation 

### Step 1: Install Python
- Download Python 3.8+ from https://www.python.org/downloads/windows/
- **Important**: Check "Add Python to PATH" during installation
- Verify installation: `python --version`

### Step 2: Install Docker Desktop
- Download from https://www.docker.com/products/docker-desktop/
- Install and start Docker Desktop
- Verify installation: `docker --version`

### Step 3: Install Make
- Download from http://gnuwin32.sourceforge.net/packages/make.htm
- Add to Windows PATH: `C:\Program Files (x86)\GnuWin32\bin`
- Verify installation: `make --version`

### Step 4: Install PostgreSQL Client (psql)
- Download PostgreSQL from https://www.postgresql.org/download/windows/
- During installation, ensure "Command Line Tools" is selected
- Add to Windows PATH: `C:\Program Files\PostgreSQL\[version]\bin`
- Verify installation: `psql --version`

## Project Setup

### Step 1: Download ZIP
**Note:** Project team will likely do this, and distribute copies to the WEX laptops.
- https://github.com/jasmine-smith_hpeprod/stem-work-experience-2026
- `<> Code`
- `Download ZIP `

### Step 2: Create Virtual Environment
```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Step 3: Database Setup
```powershell
# Start database container
make docker-compose

# Wait 10-15 seconds for initialization, then setup database
make setup-db

# Test database connection
make db-shell
```

### Step 4: Run Application
```powershell
python app.py
```

## Expected Output Sequence
- **Docker Compose**: Shows container starting (ignore version warning)
- **Setup DB**: "Migration complete: facts table created and sample data inserted."
- **DB Shell**: Prompts for password (enter: `password`)
- **Success**: PostgreSQL prompt `factsdb=#`

## Troubleshooting Notes
- If `make` fails: Use `docker compose -f docker-compose.yaml up -d db` directly
- If `psql` fails: Ensure PostgreSQL bin directory is in PATH
- Database password is always: `password`
- Alternative db-shell: `docker compose exec db psql -U postgres -d factsdb`

---

This setup ensures all Windows laptops will have the necessary tools properly configured and PATH variables set correctly.
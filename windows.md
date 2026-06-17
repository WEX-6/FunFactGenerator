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

### Step 4: Install Git
- Download Git from https://git-scm.com/download/win
- Run the installer and accept all default settings (Git Bash and OpenSSH are included)
- Make sure you allow git to be installed **globally** so it can be used in all environments
- Verify installation by opening **Command Prompt** and running:

```cmd
git --version
```

**Note:** Make will have to be added to the path manually. Go to 'Edit environment variables' on your windows laptop and click on the PATH configurations. Add the path as above, and OK.

## Project Setup

### Step 1: Generate a Deploy Key

Open **Command Prompt** or **Windows Powershell** and run (replace `laptop-1` with the laptop's name or number):

```cmd
ssh-keygen -t ed25519 -C "wex-laptop-1" 
```

- When asked for a passphrase, press **Enter** twice to leave it empty

Print the public key so I can copy it:

```cmd
type Users\%WEX-[no. on laptop]%\.ssh\id_ed25519.pub
```

Give the output to Jasmine — I will add it to the repository on GitHub as a **read-only deploy key**.

### Step 2: Configure SSH

Create (or open) the SSH config file:

```cmd
edit Users\%USERPROFILE%\.ssh\config
```

Add the following text and save:

```
Host github-stem
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519
```

### Step 3: Clone the Repository

Once I confirm the deploy key has been added, run:

```cmd
git clone git@github-stem:jasmine-smith_hpeprod/stem-work-experience-2026.git
cd stem-work-experience-2026
```

### Step 4: Create Personal Access Token + Test Access

1. On the WEX GitHub account, generate a PAT with read + write content permissions.
2. Copy this key to a text file, saving at the user root (WEX[No]) as `git_password.txt`
3. Create a blank repository on the WEX github account.
4. Within your new repository code checkout, check that `HTTPS` is selected. Copy the URL given 
5. Run `git remote remove origin` in your terminal (integrated or CommandPrompt/Windows PowerShell)
6. Run `git remote add origin <PAT><URL-from-above>` in your terminal (follows the format` https://PAT@github.com/<your-username>/<your-repo-name>.git`).
7. Run `git remote -v` to verify the remote is correct
8. Run `git push -u main` to transfer the work experience files to the new repository

### Step 5: Git Config

- Set the git config identity in terminal, replacing "0" with the number of your laptop

```
$ git config --global user.name "WEX 0"
$ git config --global user.email work-experience0@outlook.com
```

### Step 6: Create Virtual Environment
```powershell
python -m venv venv

# In order to run scripts, you may need to use the following:
Set-ExecutionPolicy -Scope CurrentUser Unrestricted

venv\Scripts\activate

pip install -r requirements.txt
```

### Step 7: Database Setup
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

### Step 8: Run Application
```powershell
python app.py
```

## Expected Output Sequence
- **Setup DB**: "Migration complete: facts table created and sample data inserted."
- **DB Shell**: Opens SQLite prompt `sqlite>`
- **Success**: Can run SQL commands like `SELECT * FROM facts;`

## Cleanup (Before Distributing to Students)

- Delete existing repository files from desktop, so that students can clone the repository themselves through git.
- Delete repository created on work experience github account.
- Clear browsing data.


## Troubleshooting Notes
- If `make` fails: Run `python database/migrations/migrate.py` directly
- Database file is stored as: `facts.db` in the project root
- To inspect database: `sqlite3 facts.db` then run SQL commands

---

This setup ensures all Windows laptops will have the necessary tools properly configured and PATH variables set correctly.
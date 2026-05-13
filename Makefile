## setup-db: Set up the SQLite database.
.PHONY: setup-db
setup-db:
	python3 database/migrations/migrate.py

## db-shell: Open the SQLite database shell.
.PHONY: db-shell
db-shell:
	sqlite3 facts.db

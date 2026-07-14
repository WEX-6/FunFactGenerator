## setup-db: Set up the SQLite database.
.PHONY: setup-db
setup-db:
	python database/migrations/migrate.py

## db-shell: Open the SQLite database shell.
.PHONY: db-shell
db-shell:
	sqlite3 facts.db

## test: Run all tests.
.PHONY: test
test:
	pytest -v

## test-p0: Run P0 unit tests (random fact generator).
.PHONY: test-p0
test-p0:
	pytest database/get_fact_test.py rest/get_fact_test.py rest/router_test.py::TestCreateApp::test_create_app_generate_route_registration -v

## test-p1: Run P1 unit tests (fact creator).
.PHONY: test-p1
test-p1:
	pytest database/create_fact_test.py rest/create_fact_test.py rest/router_test.py::TestCreateApp::test_create_app_create_route_registration -v

## test-p3: Run P3 unit tests (voting system).
.PHONY: test-p3
test-p3:
	pytest database/vote_fact_test.py rest/vote_fact_test.py rest/router_test.py::TestCreateApp::test_create_app_vote_route_registration -v

## test-p5: Run P5 unit tests (category filtering).
.PHONY: test-p5
test-p5:
	pytest database/get_fact_test.py::TestGetFactsByCategory rest/get_facts_by_category_test.py -v

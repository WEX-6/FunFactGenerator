# User Stories

## First, let us come up with a project and team name together

`Project Name:` `YOUR NAME`

`Team Name:` `YOUR NAME`

# Prequisites
Before we begin, let us set up out developer environment. This allows us to access all of the necessary libraries, and our database.

## Development Instructions

### First, open a terminal in VSCode

1. Click on the bottom left corner of the screen, where you will see a cross and warning symbol (ask your mentor if you need help finding it!)
2. Navigate to the terminal, where you will be able to type commands.
3. Copy and paste the following commands into the terminal and press enter.
4. This will complete the setup of your developer environment!

### To setup the virtual environment

1. Create a virtual environment:

```python3 -m venv venv```

2. Activate the virtual environment:

```venv\Scripts\activate```

You should now see ```(venv)``` at the beginning of your terminal.

3. Install dependencies:

```pip install -r requirements.txt```

### To setup the database

1. Run ```make setup-db``` to create the SQLite database (facts.db), create a facts table, and insert sample data.

2. Verify the migration worked by running ```make db-shell``` and then executing:

```SELECT * FROM facts;```

**Tip:** You can run ```make db-shell``` at any time to open the SQLite database shell (useful for debugging purposes).

### To run the app

1. Run the app:

```python app.py```

# P0: Random Fun Fact Generator
As an engineer, I want to be able to get a random fun fact from a database, so that I can share them with my team.

## Implementation Details

### Database Layer
The database implementation fetches a single random fact from the SQLite database.

You can complete the [SQL worksheet](../../database/worksheet.md) before moving on to the next steps.

#### Steps:
**P0.1 Implement the get_fact function** in `database/get_fact.py`:
   - Execute a SQL query to select a random fact from the facts table
   - Return a Fact object with the retrieved data, or a "No facts found" message if empty

---

### HTTP Handler (REST)
The handler bridges the database and the User Interface (UI), allowing the random fact generator page to display facts and fetch new ones without having to refresh the page.

You can complete the [HTTP worksheet](../../rest/worksheet.md) before moving on to the next steps.

#### Steps:
**P0.2 Implement the get_route function** in `rest/get_fact.py`:
   - Update the function that calls the database `get_fact` function
   - Return either JSON data or render an HTML template with the fact
   
---
### REST Router
#### Steps:
**P0.3 Update the router** in `rest/router.py`:
   - Import the get_route function from get_fact module
   - Add a new URL rule for "/generate" that accepts GET requests
   - Connect this route to your get_route function
   - Test by visiting `/generate` on localhost to see a fact in JSON format

---

### Unit Tests
**P0.4 Implement unit tests** in the test files which are following the pattern `filename_test.py`:

You can read the [unit test guide](../../tests/unit-test-guide.md) before moving on to the next steps.

Some unit tests have been implemented for you as an example, you may not need to complete all of the steps below.

   - Test the happy path (e.g. successful fact retrieval)
   - Test edge cases (e.g. empty database, connection errors)
   - Place tests in the same directory as the file being tested
   - PowerPoint: Why would we want unit tests to validate functions are working correctly as a software development team?

# P1: Random Fun Fact Creator
As an engineer, I want to be able to create my own fun facts, so that I can expand the fact list and never run out of new ones.

## Implementation Details

### Database Layer
#### Steps:
**P1.1 Implement the create_fact function** in `database/create_fact.py`:
   - Accept a fact_text parameter
   - Execute a SQL query to insert the new fact
   - Use RETURNING clause to get the new fact's ID
   - Return a Fact object with the new fact data

---

### HTTP Handler (REST)
#### Steps:
**P1.2 Edit the create_route function** in `rest/create_fact.py`:
   - Handle both GET and POST requests in the same function
   - For GET requests: render a form template
   - For POST requests: extract the fact text from the form data
   - Validate that the fact text is provided
   - Call the database `create_fact` function
   - Return the template with the newly created fact


---

### REST Router
#### Steps:
**P1.3 Update the router** in `rest/router.py`:
   - Import the create_route function
   - Add a new URL rule for "/create" that accepts both GET and POST methods
   - Test by visiting `/create` to see the form and submit new facts

---

### Unit Tests
**P1.4 Implement unit tests** in the test files which are following the pattern `filename_test.py`:

You can use the tests from the previous tasks as a guide here.

# P2: Random Fun Fact Website Design
As a UI/UX engineer, I want my random fun fact generator to provide an accessible user experience whilst maintaining a clear theme.

## Implementation Details

### CSS Implementation
**P2.1 Customize the stylesheet** in `static/css/styles.css`:
   - Look for `#TASK` comments that indicate customizable areas
   - Update colors, fonts, and layout to match your team's theme
   - Ensure accessibility with proper contrast ratios
   - PowerPoint: What other considerations could we have made to improve user experience?

---

# P3: Random Fun Fact Voting System
As an engineer, I want to be able to add a voting system to my fact service, so that I can track which facts my team like or dislike.

## Implementation Details

### Database Layer
#### Steps:
**P3.1 Create the vote_fact function** in `database/vote_fact.py`:
   - Update the appropriate vote count (likes or dislikes) in the database
   - Validate the vote_type parameter
   - Retrieve the updated Fact from the database
   - Return the updated Fact object with current vote counts
   - Handle cases where the fact doesn't exist

**P3.1 Update the get_fact function** in `database/get_fact.py`:
   - Update the SQL query to get likes and dislikes from the database
   - Update the returned Fact object to return likes and dislikes

**P3.1 Update the create_fact function** in `database/create_fact.py`:
   - Update the SQL query to add likes and dislikes counts
   - Update the returned Fact object to return likes and dislikes
   
---

### HTTP Handler (REST)
#### Steps:
**P3.2 Create the vote_route function** in `rest/vote_fact.py`:
   - Extract fact_id and vote_type from the request
   - Call the database vote_fact function
   - Return updated vote counts as JSON
   - Handle errors appropriately

**P3.2 Update the get_route function** in `rest/get_fact.py`:
   - Include like and dislike counts in both JSON and template responses
   - Pass vote counts to the HTML template

---

### REST Router
#### Steps:
**P3.3 Update the router** in `rest/router.py`:
   - Import the vote_route function
   - Add a new URL rule for "/api/vote" that accepts POST requests
   - This creates an API endpoint for voting functionality

---

### Frontend (HTML and JavaScript)
**P3.4 Update the vote function** in `generate.html`:
   - Set the correct URL for the vote endpoint
   - Set the correct IDs for the like and dislike count elements based on the fact ID
   - Set the HTTP method for the fetch call
   - Include the fact ID and vote type in the request body
   - Update the like and dislike count on the page to use the updated like/dislike count

---

### Unit Tests
**P3.5 Test the voting functionality**:
   - Test successful like and dislike votes
   - Test invalid vote types
   - Test voting on non-existent facts

---

# P4: Random Fun Fact Filter
As an engineer, I want to be able to filter facts by categories, so that I can tailor my facts to the audience.

## Implementation Details

First, we want to modify our existing workflows to include category information, so we can input a category when creating a fact and include that information in the display.

### Database Layer
#### Steps:
**P4.1 Update the get_fact function** in `database/get_fact.py`:
   - Modify the SQL queries to include the category column
   - Update the Fact object creations to include category information

**P4.2 Update the get_categories function** in `database/get_fact.py`:
   - Add the SQL query to select distinct categories from the database

**P4.3 Update the create_fact function** in `database/create_fact.py`:
   - Add category as an input parameter
   - Modify the SQL query to include the category column
   - Update the Fact object creation to include category information

**P4.4 Update the Fact entity** in `fact.py`:
   - Store category information as a variable in the entity
   - Add category information to the string representation

---

### HTTP Handler (REST)
#### Steps:
**P4.5 Update the get_route function** in `rest/get_fact.py`:
   - Get category from query parameters if provided, or set to None if not provided
   - Include category information in JSON responses
   - Pass category data to the HTML template

**P4.6 Update the get_categories_route function** in `rest/get_fact.py`:
   - Get the categories from the database

**P4.7 Update the create_route function** in `rest/create_fact.py`:
   - Get the category data from the form
   - Pass the category data to the render_template function

**P4.8 Add an `api/categories` route with a `GET` method** to `router.py`:
   - Import the get_categories_route function
   - Add a URL rule for the get_categories route

---

### Frontend (HTML and JavaScript)
#### Steps:
**P4.9 Update the loadCategories function** in `generate.html`:
   - Update the URL to use the categories endpoint

**P4.10 Add HTML** t0 `generate.html`:
   - Add a category filtering dropdown with the `category-filter` id
   - Display the category and add the `fact-category` id to the text

**P4.11 Update the loadCategories function** in `create.html`:
   - Update the URL to use the categories endpoint

**P4.12 Add HTML** to `create.html`:
   - Add a category textarea with the name `fact_text`
   - Display the created fact's category

---

### Unit Tests
#### Steps:
**P4.13 Update the unit tests**:
   - Update any implemented unit tests to include the addition of a category field.

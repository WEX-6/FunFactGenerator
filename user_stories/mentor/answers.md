# User Stories

# Prequisites
Before we begin, let us set up out developer environment. If students are strugging to understand the setup instructions, feel free to step in and help out.

## Development Instructions

Mentor note: Use the student guide for exact step-by-step setup instructions: [student/stories.md](../student/stories.md).

### To setup Git

1. Clone the repository:

```git clone <repository-url>```

2. Navigate to the project directory:

```cd stem-work-experience-2026```

3. Verify the clone was successful:

```git status```

You should see the project files and branches available.

Mentor checkpoints (Git setup):
- Confirm students are in the expected folder after clone by running `pwd` and checking the directory name.
- If clone fails, ask students to copy the full error message and verify the repository URL format.
- If `git status` fails, ensure they ran `cd stem-work-experience-2026` first.

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

---

## Implementation Details

### Database Layer
The database implementation fetches a single random fact from the SQLite database.

#### Steps:
1. P0.1 Implement the `get_fact()` method in `get_fact.py`.

```python
def get_fact() -> Fact:
    provider = SQLiteConnectionProvider()
    with provider.cursor() as cur:
        cur.execute("SELECT id, fact FROM facts ORDER BY RANDOM() LIMIT 1;") # TASK
        result = cur.fetchone()
        if result:
            return Fact(id=result[0], fact=result[1]) # TASK
        else:
            return Fact(id=None, fact="No facts found.") # TASK
```

---

### HTTP Handler (REST)
The handler bridges the database layer and the UI layer, allowing the random fact generator page to display facts and fetch new ones without page refreshes. Prior to the implementation of HTML, this will just be a JSON response.

#### Steps:
1. P0.2 Implement the `get_route()` method in `get_fact.py`.

```python
def get_route():
    fact = get_fact() # TASK
    wants_json = request.args.get("json") in ("1", "true", "True")
    if wants_json:
        return jsonify({
            "id": getattr(fact, "id", None),
            "fact": fact.fact,
        })
    return render_template("generate.html",
                         random_fact=fact.fact, # TASK
                         random_fact_id=fact.id, # TASK
    )
```

---

### REST Router
#### Steps:
1. P0.3 Add a `generate` route with a `GET` method to `router.py`.

```python
from flask import Flask
from .home import home_route
from .get_fact import get_route # TASK

def create_app():
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')
    app.add_url_rule("/", view_func=home_route, methods=["GET"])
    app.add_url_rule("/generate", view_func=get_route, methods=["GET"]) # TASK
```
2. Visit `http://127.0.0.1:5000/generate` on localhost to see a fact.

```
{
    "fact": "Honey never spoils."
}
```
---

### Unit Tests (P0.4)
1. Add unit tests to cover the generate fact logic.
2. Place tests in the same directory as the original file, following the convention `filename_test.py`.
3. Reference the given happy path & unit test guide located in the same folder and encourage students to think about negative cases to improve test coverage.

---

# P1: Random Fun Fact Creator
As an engineer, I want to be able to create my own fun facts, so that I can expand the fact list and never run out of new ones.

---

## Implementation Details

### Database Layer
The database implementation fetches a single random fact from the SQLite database.

#### Steps:
1. P1.1 Implement the `create_fact()` method in `create_fact.py`.

```python
def create_fact(fact_text: str) -> Fact: # TASK
    provider = SQLiteConnectionProvider()
    with provider.cursor() as cur:
        cur.execute(
            "INSERT INTO facts (fact) VALUES (%s, %s) RETURNING id, fact;", # TASK
            (fact_text) # TASK
        )
        result = cur.fetchone()
        provider.commit()
        return Fact(id=result[0], fact=result[1]) # TASK
```

---

### HTTP Handler (REST)
The handler bridges the database layer and the UI layer, allowing the random fact generator page to display facts and fetch new ones without page refreshes. Prior to the implementation of HTML, this will just be a JSON response.

#### Steps:
1. P1.2 Edit the `create_route()` method in `create_fact.py`.

```python
def create_route():
    if request.method == "GET":
        return render_template("create.html") # TASK
        # GET method to render the create form
    if request.method == "POST":
        fact_text = request.form.get("fact_text") # TASK
        if not fact_text: # TASK
            return "Fact text is required", 400 # TASK
        fact_create_entity = create_fact(fact_text) # TASK
        return render_template("create.html", random_fact=fact_create_entity.fact) # TASK
```

---

### REST Router
#### Steps:
1. P1.3 Add a `create` route with a `GET` and a `POST` method to `router.py`. 

Both methods are needed: 

- `GET` to render the create fact form on the frontend.
- `POST` to insert the new fact into the database.

```python
from flask import Flask
from .home import home_route
from .get_fact import get_route
from .create_fact import create_route # TASK

def create_app():
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')
    app.add_url_rule("/", view_func=home_route, methods=["GET"])
    app.add_url_rule("/generate", view_func=get_route, methods=["GET"])
    app.add_url_rule("/create", view_func=create_route, methods=["GET","POST"]) # TASK
    return app
```
2. Visit `http://127.0.0.1:5000/create` on localhost to see a fact.

```
{
    "fact": "Honey never spoils."
}
```
---

### Unit Tests (P1.4)
1. Add unit tests to cover the create fact logic.
2. Place tests in the same directory as the original file, following the convention `filename_test.py`.
3. Reference the given happy path & unit test guide located in the same folder and encourage students to think about negative cases to improve test coverage.

---

# P2: Random Fun Fact Website Design
As a UI/UX engineer, I want my random fun fact generator to provide an accessible user experience whilst maintaining a clear theme.

## Implementation Details

### P2.1 CSS Implementation

In `static/css/styles.css`, identify areas you would like to update:

 - You will see a `# TASK` comment next to any colour or fonts that can be customised.
 - This task is flexible, so collaborate with your team to come up with a cohesive theme that will fit with your implementation and branding.

# P3: Random Fun Fact Voting System
As an engineer, I want to be able to add a voting system to my fact service, so that I can track which facts my team like or dislike.

---

## Implementation Details

### Database Layer
The database implementation fetches a single random fact from the SQLite database.

#### Steps:
1. P3.1 Implement the `vote_fact()` method in `vote_fact.py`.

```python
def vote_fact(fact_id: int, vote_type: str) -> Fact:
    provider = SQLiteConnectionProvider()
    with provider.cursor() as cur:
        if vote_type == "like":
            cur.execute(
                "UPDATE facts SET likes = likes + 1 WHERE id = %s;", # TASK
                (fact_id,) # TASK
            )
        elif vote_type == "dislike":
            cur.execute(
                "UPDATE facts SET dislikes = dislikes + 1 WHERE id = %s;", # TASK
                (fact_id,) # TASK
            )
        else:
            raise ValueError("Invalid vote type") # TASK

        cur.execute(
            "SELECT id, fact, likes, dislikes FROM facts WHERE id = %s;", # TASK
            (fact_id,) # TASK
        )
        result = cur.fetchone()
        provider.commit()
        if result:
            return Fact(id=result[0], fact=result[1], likes=result[3], dislikes=result[4]) # TASK
        else:
            raise ValueError("Fact not found") # TASK
```

---

### HTTP Handler (REST)
The handler bridges the database layer and the UI layer, allowing the random fact generator page to display facts and fetch new ones without page refreshes. Prior to the implementation of HTML, this will just be a JSON response.

#### Steps:
1. P3.2 Implement the `vote_route()` method in `vote_fact.py`.

```python
def vote_route():
    data = request.json # TASK
    fact_id = data.get("fact_id") # TASK
    vote_type = data.get("vote_type") # TASK

    try:
        updated_fact = vote_fact(fact_id, vote_type) # TASK
        
        new_count = updated_fact.likes if vote_type == 'like' else updated_fact.dislikes # TASK
        
        response = { # TASK
            "fact_id": updated_fact.id,
            "new_count": new_count,
            "likes": updated_fact.likes,
            "dislikes": updated_fact.dislikes
        }
        return jsonify(response), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
```

---

2. P3.2 Update the `get_route()` method in `get_fact.py`.

```python
def get_route():
    fact = get_fact()
    wants_json = request.args.get("json") in ("1", "true", "True")
    if wants_json:
        return jsonify({
            "id": getattr(fact, "id", None),
            "fact": fact.fact,
            "likes": getattr(fact, "likes", 0), # TASK
            "dislikes": getattr(fact, "dislikes", 0) # TASK
        })
    return render_template("generate.html",
                         random_fact=fact.fact,
                         random_fact_id=fact.id,
                         random_fact_likes=getattr(fact, "likes", 0), # TASK
                         random_fact_dislikes=getattr(fact, "dislikes", 0)) # TASK
```

---

### Database Layer
The database implementation fetches a single random fact from the SQLite database.

#### Steps:
1. Implement the `vote_fact()` method in `vote_fact.py`.

```python
def vote_fact(fact_id: int, vote_type: str) -> Fact:
    provider = SQLiteConnectionProvider()
    with provider.cursor() as cur:
        if vote_type == "like":
            cur.execute(
                "UPDATE facts SET likes = likes + 1 WHERE id = %s;", # TASK
                (fact_id,) # TASK
            )
        elif vote_type == "dislike":
            cur.execute(
                "UPDATE facts SET dislikes = dislikes + 1 WHERE id = %s;", # TASK
                (fact_id,) # TASK
            )
        else:
            raise ValueError("Invalid vote type") # TASK

        cur.execute(
            "SELECT id, fact, category, likes, dislikes FROM facts WHERE id = %s;", # TASK
            (fact_id,) # TASK
        )
        result = cur.fetchone()
        provider.commit()
        if result:
            return Fact(id=result[0], fact=result[1], category=result[2], likes=result[3], dislikes=result[4]) # TASK
        else:
            raise ValueError("Fact not found") # TASK
```

2. Update the `get_fact()` method in `get_fact.py`.

```python
def get_fact() -> Fact:
    provider = SQLiteConnectionProvider()
    with provider.cursor() as cur:    # TASK
        cur.execute("SELECT id, fact, likes, dislikes FROM facts ORDER BY RANDOM() LIMIT 1;") # TASK
        result = cur.fetchone()
        if result:                                      # TASK
            return Fact(id=result[0], fact=result[1], likes=result[3], dislikes=result[4]) # TASK
        else:                                           # TASK
            return Fact(id=None, fact="No facts found.", likes=0, dislikes=0) # TASK
```

3. Update the `create_fact()` method in `create_fact.py`.

```python
def create_fact(fact_text: str, category: str) -> Fact:
    provider = SQLiteConnectionProvider()
    with provider.cursor() as cur:
        cur.execute(
            "INSERT INTO facts (fact) VALUES (%s) RETURNING id, fact, category, likes, dislikes;",    # TASK
            (fact_text,)   # TASK
        )
        result = cur.fetchone()
        provider.commit()
        return Fact(id=result[0], fact=result[1], likes=result[3] or 0, dislikes=result[4] or 0)    # TASK
```

---

### REST Router
#### Steps:
1. P3.3 Add an `api/vote` route with a `POST` method to `router.py`. 

- `POST` to insert the vote into the database.

```python
from flask import Flask
from .home import home_route
from .get_fact import get_route
from .create_fact import create_route
from .vote_fact import vote_route # TASK

def create_app():
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')
    app.add_url_rule("/", view_func=home_route, methods=["GET"])
    app.add_url_rule("/generate", view_func=get_route, methods=["GET"])
    app.add_url_rule("/create", view_func=create_route, methods=["GET","POST"]) 
    app.add_url_rule("/api/vote", view_func=vote_route, methods=["POST"]) # TASK

    return app
```

---

### Frontend (HTML and JavaScript)
#### Steps

1. P3.4 Update the `vote(type, factId)` function in `generate.html`.

```javascript
async function vote(type, factId) {
    if (!factId) {
        console.error('No fact ID provided');
        return;
    }
    const url = '/api/vote'; // TASK
    const likeCount = document.getElementById(`like-count-${factId}`); // TASK
    const dislikeCount = document.getElementById(`dislike-count-${factId}`); // TASK

    try {
        const response = await fetch(url, {
            method: 'POST', // TASK
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ fact_id: factId, vote_type: type }) // TASK
        });

        if (!response.ok) {
            const errorData = await response.json();
            console.error('Error voting:', errorData.error);
            return;
        }

        // Get the data with the new like/dislike count from the response
        const data = await response.json();
        if (type === 'like') {
            likeCount.textContent = data.new_count; // TASK
        } else {
            dislikeCount.textContent = data.new_count; // TASK
        }
    } catch (error) {
        console.error('Error voting:', error);
    }
}
```

---

### Unit Tests (P3.5)
1. Add unit tests to cover the vote fact logic.
2. Place tests in the same directory as the original file, following the convention `filename_test.py`.
3. Reference the given happy path & unit test guide located in the same folder and encourage students to think about negative cases to improve test coverage.

---

# P4: Add Fact Category
As an engineer, I want to be able to add categories to facts, so that each fact has useful context for the audience.

---

## Implementation Details

### Database Layer
The database implementation fetches a single random fact from the SQLite database.

#### Steps:
1. P4.1 Update the `Fact` constructor in `fact.py`.

```python
class Fact:
    def __init__(self, id: int, fact: str, category: str = None, likes: int = 0, dislikes: int = 0):
        self.id = id
        self.fact = fact
        self.category = category # TASK
        self.likes = likes
        self.dislikes = dislikes

    def __repr__(self):
        return f"<Fact id={self.id} fact='{self.fact}' category={self.category} likes={self.likes}, dislikes={self.dislikes}>" # TASK
```

2. P4.2 Update the `get_fact()` method in `get_fact.py`.

```python
def get_fact() -> Fact:
    provider = SQLiteConnectionProvider()
    with provider.cursor() as cur:
        cur.execute("SELECT id, fact, category, likes, dislikes FROM facts ORDER BY RANDOM() LIMIT 1;") # TASK
        result = cur.fetchone()
        if result:
            return Fact(id=result[0], fact=result[1], category=result[2], likes=result[3], dislikes=result[4]) # TASK
        else:
            return Fact(id=None, fact="No facts found", category=None, likes=0, dislikes=0) # TASK
```

3. P4.3 Update the `create_fact()` method in `create_fact.py`.

```python
def create_fact(fact_text: str, category: str) -> Fact: # TASK
    provider = SQLiteConnectionProvider()
    with provider.cursor() as cur:
        cur.execute(
            "INSERT INTO facts (fact, category) VALUES (%s, %s) RETURNING id, fact, category, likes, dislikes;",    # TASK
            (fact_text, category)   # TASK
        )
        result = cur.fetchone()
        provider.commit()
        return Fact(id=result[0], fact=result[1], category=result[2], likes=result[3] or 0, dislikes=result[4] or 0)    # TASK
```

### HTTP Handler (REST)
The handler bridges the database layer and the UI layer, allowing the random fact generator page to display facts and fetch new ones without page refreshes. 

#### Steps:
1. P4.4 Update the `get_route()` method in `get_fact.py`.

```python
def get_route():
    fact = get_fact() # TASK

    # Check if the client wants JSON response based on query parameters
    wants_json = request.args.get("json") in ("1", "true", "True")

    if wants_json:
        return jsonify({
            "id": getattr(fact, "id", None),
            "fact": fact.fact,
            "category": getattr(fact, "category", None), # TASK
            "likes": getattr(fact, "likes", 0),
            "dislikes": getattr(fact, "dislikes", 0)
        })
    return render_template("generate.html",
                         random_fact=fact.fact,
                         random_fact_id=fact.id,
                         random_fact_category=getattr(fact, "category", "Uncategorized"), # TASK
                         random_fact_likes=getattr(fact, "likes", 0),
                         random_fact_dislikes=getattr(fact, "dislikes", 0))
```

2. P4.5 Update the `create_route()` method in `create_fact.py`.

```python
def create_route():
    if request.method == "GET":
        return render_template("create.html")
    if request.method == "POST":
        fact_text = request.form.get("fact_text")
        category = request.form.get("category") # TASK
        if not fact_text:
            return "Fact text is required", 400
        fact_create_entity = create_fact(fact_text, category) # TASK
        return render_template("create.html", random_fact=fact_create_entity.fact, category=fact_create_entity.category) # TASK
```

---

### Frontend (HTML and JavaScript)

#### Steps
1. P4.6 Update `generate.html` and `create.html` to display and create categories.

```html
<div class="main-container">
    <h1>Random Fact Generator</h1>
    <div class="fact-container">
        <!-- TASK -->
        <p>Your random <strong id="fact-category">{{ random_fact_category }}</strong> fact is: </p> <!-- TASK -->
        <strong id="fact-text">{{ random_fact }}</strong>
    </div>
    ...
</div>

<h1>Create a New Fact</h1>
    <div class="create-fact-container" id="createForm">
        <form action="/create" method="POST">
            <!-- TASK -->
            <textarea name="fact_text" placeholder="Enter your fact here..." required></textarea>
            <textarea name="category" placeholder="Enter a category here..."></textarea> <!-- TASK -->
            <button type="submit" class="fact-generator-button">Submit</button>
        </form>
    </div>

    {% if random_fact %}
    <div id="factDisplay">
        <div class="fact-container">
            <p>New fact created:</p>
            <strong>{{ random_fact.fact }}</strong>
            {% if random_fact_category %}
            <!-- TASK -->
            <p>Category: <strong>{{ random_fact_category }}</strong></p> <!-- TASK -->
            {% endif %}
        </div>
        <button type="button" class="fact-generator-button" onclick="showCreateForm()">Create New Fact</button>
    </div>
    {% endif %}
</div>
```

---

### Unit Tests (P4.7)
1. Update unit tests to include the addition of a category field.
2. Place tests in the same directory as the original file, following the convention `filename_test.py`.
3. Reference the given happy path & unit test guide located in the same folder and encourage students to think about negative cases to improve test coverage.

---

# P5: Add Category Filtering
As an engineer, I want to be able to filter facts by categories, so that I can tailor my facts to the audience.

---

## Implementation Details

### Database Layer
The database implementation fetches a single random fact from the SQLite database, optionally filtered by category.

#### Steps:
1. P5.1 Update the `get_fact()` method in `get_fact.py`.

```python
def get_fact(category: Optional[str] = None) -> Fact: # TASK
    provider = SQLiteConnectionProvider()
    with provider.cursor() as cur:
        if category: # TASK
            cur.execute( # TASK
                "SELECT id, fact, category, likes, dislikes FROM facts WHERE category = %s ORDER BY RANDOM() LIMIT 1;",
                (category,)
            )
        else:
            cur.execute("SELECT id, fact, category, likes, dislikes FROM facts ORDER BY RANDOM() LIMIT 1;") # TASK
        result = cur.fetchone()
        if result:
            return Fact(id=result[0], fact=result[1], category=result[2], likes=result[3], dislikes=result[4]) # TASK
        else:
            return Fact(id=None, fact="No facts found", category=None, likes=0, dislikes=0) # TASK
```

2. P5.2 Update the `get_facts_by_category()` method in `get_fact.py`.

```python
def get_facts_by_category() -> List[str]:
    provider = SQLiteConnectionProvider()
    with provider.cursor() as cur:
        cur.execute("SELECT DISTINCT category FROM facts WHERE category IS NOT NULL ORDER BY category;") # TASK
        rows = cur.fetchall()
        return [row[0] for row in rows]
```

### HTTP Handler (REST)
The handler bridges the database layer and the UI layer, allowing the random fact generator page to display facts and fetch new ones without page refreshes.

#### Steps:
3. P5.3 Update the `get_route()` method in `get_fact.py`.

```python
def get_route():
    category = request.args.get("category") or None # TASK
    fact = get_fact(category=category) # TASK
    wants_json = request.args.get("json") in ("1", "true", "True")
    ...
```

4. P5.4 Update the `get_facts_by_category_route()` method in `get_facts_by_category.py`.

```python
def get_facts_by_category_route():
    categories = get_facts_by_category() # TASK
    return jsonify({"categories": categories})
```

5. P5.5 Add an `api/categories` route with a `GET` method to `router.py`.

```python
from .get_facts_by_category import get_facts_by_category_route # TASK

def create_app():
    ...
    app.add_url_rule("/api/categories", view_func=get_facts_by_category_route, methods=["GET"]) # TASK
    return app
```

---

### Frontend (HTML and JavaScript)

#### Steps
6. P5.6 Update the `loadCategories()` function in `generate.html`.

```javascript
async function loadCategories() {
    try {
        const response = await fetch('/api/categories'); // TASK
        const data = await response.json();
        const select = document.getElementById('category-filter');
        data.categories.forEach(cat => {
            const option = document.createElement('option');
            option.value = cat;
            option.textContent = cat.charAt(0).toUpperCase() + cat.slice(1);
            select.appendChild(option);
        });
    } catch (error) {
        console.error('Error loading categories:', error);
    }
}
```

7. P5.7 Update `generate.html` to include a category filtering dropdown with an id of `category-filter`.

```html
<div class="filter-container"> <!-- TASK -->
    <label for="category-filter">Filter by category:</label>
    <select id="category-filter" class="category-filter" onchange="getNewFact()"> <!-- TASK -->
        <option value="">All categories</option>
    </select>
</div>
```

8. P5.8 Update the `loadCategories()` function in `create.html`.

```javascript
async function loadCategories() {
    try {
        const response = await fetch('/api/categories'); // TASK
        const data = await response.json();
        const select = document.getElementById('category-select');
        data.categories.forEach(cat => {
            const option = document.createElement('option');
            option.value = cat;
            option.textContent = cat.charAt(0).toUpperCase() + cat.slice(1);
            select.appendChild(option);
        });
    } catch (error) {
        console.error('Error loading categories:', error);
    }
}
```

---

### Unit Tests (P5.9)
1. Add unit tests to cover the fact filtering logic.
2. Place tests in the same directory as the original file, following the convention `filename_test.py`.
3. Reference the given happy path & unit test guide located in the same folder and encourage students to think about negative cases to improve test coverage.

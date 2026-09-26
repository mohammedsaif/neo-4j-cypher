# README.md

````markdown
# 🎓 Learning Platform Graph with Neo4j & Python

A graph-based Learning Platform project built using **Neo4j, Cypher, and Python**.

This project demonstrates how a learning ecosystem can be represented as a graph containing students, courses, mentors, skills, projects, and companies.

The project focuses on understanding:

- Graph databases
- Neo4j
- Cypher query language
- Nodes and labels
- Properties
- Relationships
- Relationship direction
- CRUD operations
- Search and filtering
- Graph visualization
- Python integration with Neo4j
- Parameterized Cypher queries

---

## 📌 Project Overview

Traditional relational databases represent data primarily through tables and foreign-key relationships.

A graph database such as Neo4j represents data using:

```text
Nodes + Relationships + Properties
````

For this project, we model a learning platform where:

* Students enroll in courses
* Mentors teach courses
* Courses teach specific skills
* Students build projects
* Projects use skills
* Students are interested in companies

This creates a connected graph that can be queried to discover relationships between learners, courses, skills, projects, and companies.

---

# 🏗️ Architecture

```text
                         ┌──────────────┐
                         │    Mentor    │
                         └──────┬───────┘
                                │
                             TEACHES
                                │
                                ▼
                         ┌──────────────┐
                         │    Course    │
                         └──────┬───────┘
                                │
                         TEACHES_SKILL
                                │
                                ▼
                         ┌──────────────┐
                         │    Skill     │
                         └──────▲───────┘
                                │
                              USES
                                │
                         ┌──────┴───────┐
                         │   Project    │
                         └──────▲───────┘
                                │
                              BUILT
                                │
                         ┌──────┴───────┐
                         │   Student    │
                         └──────┬───────┘
                                │
                           ENROLLED_IN
                                │
                                ▼
                         ┌──────────────┐
                         │    Course    │
                         └──────────────┘

Student ──INTERESTED_IN──> Company
```

---

# 🎯 Objectives

The main objectives of this project are:

1. Understand the fundamentals of graph databases.
2. Create nodes using Cypher.
3. Add properties to nodes.
4. Create relationships between nodes.
5. Understand relationship direction.
6. Query connected data.
7. Search and filter graph data.
8. Update node properties.
9. Delete relationships.
10. Delete nodes.
11. Connect Python with Neo4j.
12. Use parameterized Cypher queries.
13. Visualize the complete graph using Neo4j Browser.
14. Manage the project using Git and GitHub.

---

# 🧩 Graph Entities

The graph contains six major types of nodes.

| Node Label | Description                                     |
| ---------- | ----------------------------------------------- |
| `Student`  | Represents learners using the platform          |
| `Course`   | Represents courses available on the platform    |
| `Mentor`   | Represents instructors or mentors               |
| `Skill`    | Represents technical skills                     |
| `Project`  | Represents projects built by students           |
| `Company`  | Represents companies students are interested in |

---

# 🔗 Relationships

The following relationships are implemented:

| Source  | Relationship    | Target  |
| ------- | --------------- | ------- |
| Student | `ENROLLED_IN`   | Course  |
| Mentor  | `TEACHES`       | Course  |
| Course  | `TEACHES_SKILL` | Skill   |
| Student | `BUILT`         | Project |
| Project | `USES`          | Skill   |
| Student | `INTERESTED_IN` | Company |

---

# 📊 Graph Statistics

The initial graph contains:

```text
25 Nodes
34 Relationships
6 Node Labels
6 Relationship Types
```

### Node distribution

| Node Type |  Count |
| --------- | -----: |
| Students  |      5 |
| Courses   |      4 |
| Mentors   |      3 |
| Skills    |      5 |
| Projects  |      4 |
| Companies |      4 |
| **Total** | **25** |

### Relationship distribution

| Relationship    |  Count |
| --------------- | -----: |
| `ENROLLED_IN`   |      8 |
| `TEACHES`       |      4 |
| `TEACHES_SKILL` |      7 |
| `BUILT`         |      4 |
| `USES`          |      6 |
| `INTERESTED_IN` |      5 |
| **Total**       | **34** |

This exceeds the assignment requirement of:

```text
Minimum Nodes        = 20
Minimum Relationships = 25
```

---

# 🛠️ Technologies Used

## Backend / Programming

* Python 3
* Neo4j Python Driver

## Database

* Neo4j
* Neo4j Aura

## Query Language

* Cypher

## Development Tools

* Visual Studio Code
* Git
* GitHub
* Neo4j Browser

---

# 📁 Project Structure

```text
learning-platform-neo4j/
│
├── cypher/
│   │
│   ├── 01_constraints.cypher
│   ├── 02_create_nodes.cypher
│   ├── 03_create_relationships.cypher
│   ├── 04_read_queries.cypher
│   ├── 05_update_queries.cypher
│   └── 06_delete_queries.cypher
│
├── python/
│   │
│   ├── neo4j_connection.py
│   └── graph_operations.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

> `.env` should not be committed to GitHub because it contains database credentials.

---

# ⚙️ Prerequisites

Before running the project, install:

* Python 3.10+
* Git
* Visual Studio Code
* Neo4j Aura account
* GitHub account

Verify Python:

```bash
python --version
```

Verify Git:

```bash
git --version
```

Verify pip:

```bash
pip --version
```

---

# 🚀 Getting Started

## Step 1 — Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate into the project:

```bash
cd learning-platform-neo4j
```

---

# Step 2 — Create Python Virtual Environment

Windows:

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

---

# Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
neo4j
python-dotenv
```

---

# Step 4 — Configure Neo4j Aura

Create a Neo4j Aura database.

You will need:

```text
NEO4J_URI
NEO4J_USERNAME
NEO4J_PASSWORD
```

Example:

```text
NEO4J_URI=neo4j+s://xxxxxxxx.databases.neo4j.io
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password
```

Create a `.env` file in the project root.

```env
NEO4J_URI=your_neo4j_uri
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password
```

---

# 🔐 Environment Variables

The application reads database credentials from environment variables.

```python
import os

from dotenv import load_dotenv

load_dotenv()

URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")
```

Credentials are never hardcoded inside the Python source code.

---

# 🚫 Security

Never commit:

```text
.env
```

to GitHub.

The `.gitignore` file should contain:

```gitignore
.venv/
__pycache__/
.env
*.pyc
```

Before pushing to GitHub, verify:

```bash
git status
```

Make sure `.env` is not listed as a file to commit.

---

# 🗄️ Database Schema

## Student

Example:

```cypher
(:Student {
    id: "S001",
    name: "Rahul",
    email: "rahul@example.com",
    experience: 2
})
```

Properties:

| Property     | Description               |
| ------------ | ------------------------- |
| `id`         | Unique student identifier |
| `name`       | Student name              |
| `email`      | Student email             |
| `experience` | Years of experience       |

---

## Course

```cypher
(:Course {
    id: "C001",
    name: "Python Programming",
    level: "Beginner"
})
```

Properties:

| Property | Description              |
| -------- | ------------------------ |
| `id`     | Unique course identifier |
| `name`   | Course name              |
| `level`  | Course difficulty        |

---

## Mentor

```cypher
(:Mentor {
    id: "M001",
    name: "Amit Sharma",
    expertise: "Python"
})
```

---

## Skill

```cypher
(:Skill {
    id: "SK001",
    name: "Python"
})
```

---

## Project

```cypher
(:Project {
    id: "P001",
    name: "AI Data Analyst",
    status: "Completed"
})
```

---

## Company

```cypher
(:Company {
    id: "CO001",
    name: "Microsoft",
    industry: "Technology"
})
```

---

# 🔗 Relationship Model

## Student → Course

```text
(Student)-[:ENROLLED_IN]->(Course)
```

Meaning:

> A student is enrolled in a course.

Example:

```cypher
(:Student)-[:ENROLLED_IN]->(:Course)
```

---

## Mentor → Course

```text
(Mentor)-[:TEACHES]->(Course)
```

Meaning:

> A mentor teaches a course.

---

## Course → Skill

```text
(Course)-[:TEACHES_SKILL]->(Skill)
```

Meaning:

> A course teaches a particular skill.

---

## Student → Project

```text
(Student)-[:BUILT]->(Project)
```

Meaning:

> A student built a project.

---

## Project → Skill

```text
(Project)-[:USES]->(Skill)
```

Meaning:

> A project uses a particular skill.

---

## Student → Company

```text
(Student)-[:INTERESTED_IN]->(Company)
```

Meaning:

> A student is interested in working for a company.

---

# 🧠 Understanding Relationship Direction

Neo4j relationships have a direction.

For example:

```text
Student ──ENROLLED_IN──> Course
```

The direction is:

```text
Student → Course
```

We can query this direction using:

```cypher
MATCH (s:Student)-[:ENROLLED_IN]->(c:Course)
RETURN s, c;
```

We can also query relationships without specifying direction:

```cypher
MATCH (s:Student)-[:ENROLLED_IN]-(c:Course)
RETURN s, c;
```

Direction is useful when the meaning of the relationship matters.

---

# 🔒 Constraints

The project creates unique constraints for entity IDs.

Example:

```cypher
CREATE CONSTRAINT student_id IF NOT EXISTS
FOR (s:Student)
REQUIRE s.id IS UNIQUE;
```

This prevents multiple students from having the same ID.

Similar constraints are created for:

```text
Student
Course
Mentor
Skill
Project
Company
```

---

# ✏️ Creating Nodes

Nodes are created using Cypher.

Example:

```cypher
CREATE (:Student {
    id: "S001",
    name: "Rahul",
    email: "rahul@example.com",
    experience: 2
});
```

Multiple nodes can also be created in one query:

```cypher
CREATE
(:Student {
    id: "S001",
    name: "Rahul"
}),
(:Student {
    id: "S002",
    name: "Priya"
});
```

---

# 🔗 Creating Relationships

Relationships are created by matching existing nodes.

Example:

```cypher
MATCH (s:Student {id: "S001"}),
      (c:Course {id: "C001"})

CREATE (s)-[:ENROLLED_IN]->(c);
```

The nodes are identified first, then the relationship is created.

---

# 📖 READ Operations

## Read all students

```cypher
MATCH (s:Student)
RETURN s;
```

---

## Read all courses

```cypher
MATCH (c:Course)
RETURN c;
```

---

## Read students and courses

```cypher
MATCH (s:Student)-[:ENROLLED_IN]->(c:Course)
RETURN
    s.name AS Student,
    c.name AS Course;
```

---

## Read mentors and courses

```cypher
MATCH (m:Mentor)-[:TEACHES]->(c:Course)
RETURN
    m.name AS Mentor,
    c.name AS Course;
```

---

## Read courses and skills

```cypher
MATCH (c:Course)-[:TEACHES_SKILL]->(s:Skill)
RETURN
    c.name AS Course,
    collect(s.name) AS Skills;
```

---

## Read students and projects

```cypher
MATCH (s:Student)-[:BUILT]->(p:Project)
RETURN
    s.name AS Student,
    p.name AS Project;
```

---

# 🔎 Search and Filtering

## Find students with 3+ years of experience

```cypher
MATCH (s:Student)
WHERE s.experience >= 3
RETURN
    s.name,
    s.experience;
```

---

## Find advanced courses

```cypher
MATCH (c:Course)
WHERE c.level = "Advanced"
RETURN c;
```

---

## Find projects using Python

```cypher
MATCH (p:Project)-[:USES]->(s:Skill)
WHERE s.name = "Python"
RETURN p.name AS Project;
```

---

## Find students interested in Microsoft

```cypher
MATCH (s:Student)-[:INTERESTED_IN]->(c:Company)
WHERE c.name = "Microsoft"
RETURN
    s.name AS Student,
    c.name AS Company;
```

---

# 🔄 Update Operations

## Update student experience

```cypher
MATCH (s:Student {id: "S001"})
SET s.experience = 3
RETURN s;
```

---

## Update project status

```cypher
MATCH (p:Project {id: "P003"})
SET p.status = "Completed"
RETURN p;
```

---

## Add a new property

```cypher
MATCH (c:Course {id: "C004"})
SET c.duration = "8 weeks"
RETURN c;
```

---

# 🗑️ Delete Operations

## Delete a relationship

```cypher
MATCH (s:Student {id: "S005"})
      -[r:INTERESTED_IN]->
      (c:Company {id: "CO001"})

DELETE r;
```

---

## Delete a node without relationships

```cypher
MATCH (s:Skill {id: "SK999"})
DELETE s;
```

---

## Delete a node with relationships

```cypher
MATCH (p:Project {id: "P004"})
DETACH DELETE p;
```

`DETACH DELETE` removes the node and its connected relationships.

---

# 📊 Graph Visualization

To visualize the complete graph in Neo4j Browser:

```cypher
MATCH (n)-[r]->(m)
RETURN n, r, m;
```

Neo4j Browser will display the result as a graph.

The visualization allows us to see:

```text
Student
   │
   ├── ENROLLED_IN ──> Course
   │                      │
   │                      └── TEACHES_SKILL ──> Skill
   │
   ├── BUILT ──> Project
   │                │
   │                └── USES ──> Skill
   │
   └── INTERESTED_IN ──> Company

Mentor ── TEACHES ──> Course
```

---

# 🔥 Advanced Graph Query

One of the most useful queries in the project is finding a student's learning path.

```cypher
MATCH
    (s:Student)-[:ENROLLED_IN]->(c:Course)
    -[:TEACHES_SKILL]->(skill:Skill)

RETURN
    s.name AS Student,
    c.name AS Course,
    skill.name AS Skill;
```

This answers:

> Which skills is a student learning through their enrolled courses?

---

# 🚀 Project Skill Analysis

Find students who have built projects using skills taught by their courses:

```cypher
MATCH
    (s:Student)-[:ENROLLED_IN]->(c:Course)
    -[:TEACHES_SKILL]->(skill:Skill),

    (s)-[:BUILT]->(p:Project)
    -[:USES]->(skill)

RETURN
    s.name AS Student,
    c.name AS Course,
    skill.name AS Skill,
    p.name AS Project;
```

This demonstrates the strength of graph databases because multiple relationships can be traversed in a single query.

---

# 🐍 Python Integration

The project also connects Python to Neo4j using the official Neo4j Python driver.

Basic connection:

```python
from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)
```

---

# 🔐 Parameterized Queries

The Python implementation uses parameters rather than directly inserting user values into Cypher.

Example:

```python
query = """
CREATE (s:Student {
    id: $id,
    name: $name,
    email: $email,
    experience: $experience
})
RETURN s
"""
```

Parameters:

```python
session.run(
    query,
    id=student_id,
    name=name,
    email=email,
    experience=experience
)
```

This approach keeps the query separate from the data values and is preferable to constructing Cypher using string concatenation.

---

# 🧪 Python CRUD

The Python implementation demonstrates:

```text
CREATE
   ↓
READ
   ↓
UPDATE
   ↓
DELETE
```

Example:

```python
platform.create_student(
    "S100",
    "Test Student",
    "test@example.com",
    1
)
```

Read:

```python
platform.read_students()
```

Update:

```python
platform.update_student(
    "S100",
    2
)
```

Delete:

```python
platform.delete_student(
    "S100"
)
```

---

# ▶️ Running the Python Application

Activate the virtual environment.

Windows:

```bash
.venv\Scripts\activate
```

Run the connection test:

```bash
python python/neo4j_connection.py
```

Expected output:

```text
Neo4j connection successful
```

Run the CRUD demonstration:

```bash
python python/graph_operations.py
```

---

# 🧾 Running the Cypher Scripts

Execute the Cypher files in this order:

```text
1. 01_constraints.cypher
2. 02_create_nodes.cypher
3. 03_create_relationships.cypher
4. 04_read_queries.cypher
5. 05_update_queries.cypher
6. 06_delete_queries.cypher
```

The recommended order is important because relationships require the corresponding nodes to already exist.

---

# 🔍 Verify Node Count

Run:

```cypher
MATCH (n)
RETURN count(n) AS TotalNodes;
```

Expected initial result:

```text
25
```

---

# 🔍 Verify Relationship Count

Run:

```cypher
MATCH ()-[r]->()
RETURN count(r) AS TotalRelationships;
```

Expected initial result:

```text
34
```

> The delete demonstrations may reduce these numbers after execution.

---

# 🧪 Testing Checklist

Before submitting the project, verify:

* [ ] Neo4j Aura database is running
* [ ] Python environment is working
* [ ] `requirements.txt` installs successfully
* [ ] `.env` contains valid credentials
* [ ] `.env` is excluded from Git
* [ ] Constraints are created
* [ ] 25 nodes are created
* [ ] 34 relationships are created
* [ ] Student → Course relationships work
* [ ] Mentor → Course relationships work
* [ ] Course → Skill relationships work
* [ ] Student → Project relationships work
* [ ] Project → Skill relationships work
* [ ] Student → Company relationships work
* [ ] READ queries work
* [ ] Search/filter queries work
* [ ] UPDATE queries work
* [ ] DELETE relationship works
* [ ] DELETE node works
* [ ] Python connects successfully
* [ ] Python CRUD works
* [ ] Graph visualization works
* [ ] Code is pushed to GitHub
* [ ] YouTube video is recorded

---

# 🎥 YouTube Demonstration Plan

The video should demonstrate the project from beginning to end.

## 1. Introduction

Explain:

> "Hello everyone. In this project, I have built a Learning Platform Graph using Neo4j and Python. The graph represents students, courses, mentors, skills, projects, and companies."

---

## 2. Show Project Structure

Show:

```text
cypher/
python/
README.md
requirements.txt
.gitignore
```

Explain the purpose of each folder.

---

## 3. Explain Nodes

Show:

```text
Student
Course
Mentor
Skill
Project
Company
```

Explain that each is represented using a Neo4j label.

---

## 4. Explain Properties

Show an example:

```cypher
(:Student {
    id: "S001",
    name: "Rahul",
    email: "rahul@example.com",
    experience: 2
})
```

Explain:

```text
Student → Label

id
name
email
experience
     ↓
Properties
```

---

## 5. Explain Relationships

Show:

```text
Student ──ENROLLED_IN──> Course
```

Then explain:

* Source node
* Relationship type
* Target node
* Relationship direction

---

## 6. Show Data Creation

Run:

```cypher
MATCH (n)
RETURN n;
```

Show the created nodes.

---

## 7. Show Relationship Creation

Run:

```cypher
MATCH (n)-[r]->(m)
RETURN n, r, m;
```

Show the graph visualization.

---

## 8. Demonstrate READ

Run:

```cypher
MATCH (s:Student)-[:ENROLLED_IN]->(c:Course)
RETURN s.name, c.name;
```

Explain the result.

---

## 9. Demonstrate Search

Run:

```cypher
MATCH (p:Project)-[:USES]->(s:Skill)
WHERE s.name = "Python"
RETURN p.name;
```

Explain how graph traversal can answer connected-data questions.

---

## 10. Demonstrate UPDATE

Run:

```cypher
MATCH (s:Student {id: "S001"})
SET s.experience = 3
RETURN s;
```

Show the updated property.

---

## 11. Demonstrate DELETE

Create a temporary node and then delete it.

```cypher
CREATE (:Skill {
    id: "SK999",
    name: "Temporary Skill"
});
```

Then:

```cypher
MATCH (s:Skill {id: "SK999"})
DELETE s;
```

---

## 12. Demonstrate Python

Run:

```bash
python python/neo4j_connection.py
```

Then:

```bash
python python/graph_operations.py
```

Explain that Python is communicating with Neo4j using the Neo4j Python driver.

---

## 13. Final Graph Visualization

Run:

```cypher
MATCH (n)-[r]->(m)
RETURN n, r, m;
```

Show the complete graph.

Explain how the graph connects:

```text
Students
   ↓
Courses
   ↓
Skills
   ↑
Projects
   ↑
Students
   ↓
Companies

Mentors
   ↓
Courses
```

---

# 🎬 YouTube Video Title

**I Built a Learning Platform Graph with Neo4j & Python | Cypher CRUD & Graph Visualization**

Alternative:

**Neo4j Graph Database Project in Python | Nodes, Relationships, Cypher & CRUD**

---

# 🖼️ YouTube Thumbnail

Suggested thumbnail text:

```text
NEO4J
GRAPH PROJECT
```

Small text:

```text
Python + Cypher + CRUD
```

Suggested design:

```text
Dark developer background
        +
Neo4j graph visualization
        +
Python code
        +
Connected nodes
        +
Student → Course → Skill
```

---

# 📺 YouTube Description

```text
In this project, I built a Learning Platform Graph using Neo4j and Python.

The project models a connected learning ecosystem containing:

👨‍🎓 Students
📚 Courses
👨‍🏫 Mentors
🧠 Skills
🚀 Projects
🏢 Companies

Relationships implemented:

Student → ENROLLED_IN → Course
Mentor → TEACHES → Course
Course → TEACHES_SKILL → Skill
Student → BUILT → Project
Project → USES → Skill
Student → INTERESTED_IN → Company

In this video, I demonstrate:

✅ Neo4j Aura
✅ Nodes
✅ Labels
✅ Properties
✅ Relationships
✅ Relationship direction
✅ Cypher CREATE
✅ Cypher MATCH
✅ Search and filtering
✅ UPDATE
✅ DELETE
✅ Python + Neo4j Driver
✅ Parameterized queries
✅ Graph visualization

The project contains 25 nodes and 34 relationships.

GitHub:
[ADD YOUR GITHUB LINK]

Thank you for watching!
```

---

# 🏷️ Hashtags

```text
#Neo4j
#GraphDatabase
#Cypher
#Python
#PythonProject
#NoSQL
#Database
#GraphDatabaseProject
#SoftwareEngineering
#BackendDevelopment
#DataEngineering
#AIEngineering
#LearningPlatform
#GitHub
```

---

# 📌 Learning Outcomes

After completing this project, the following concepts have been demonstrated:

### Neo4j

* Graph database fundamentals
* Nodes
* Labels
* Properties
* Relationships
* Relationship direction
* Graph traversal

### Cypher

* `CREATE`
* `MATCH`
* `WHERE`
* `RETURN`
* `SET`
* `DELETE`
* `DETACH DELETE`
* `collect()`
* Parameters
* Constraints

### Python

* Neo4j Python Driver
* Database connection
* Sessions
* Running Cypher from Python
* Parameterized queries
* CRUD operations
* Environment variables

### Development

* Virtual environments
* `requirements.txt`
* `.gitignore`
* Git
* GitHub
* Project documentation

---

# 🚀 Future Improvements

Possible future extensions include:

1. Add student performance scores.
2. Add course completion status.
3. Add course prerequisites.
4. Add mentor expertise relationships.
5. Add student skill proficiency levels.
6. Add project difficulty levels.
7. Add job openings.
8. Connect companies to required skills.
9. Recommend courses based on student interests.
10. Recommend projects based on skills.
11. Recommend companies based on student skills.
12. Build a FastAPI backend.
13. Build a React frontend.
14. Add authentication.
15. Build a graph-based recommendation system.

A future recommendation query could identify companies matching a student's skills:

```cypher
MATCH
    (s:Student)-[:BUILT]->(p:Project)-[:USES]->(skill:Skill),
    (company:Company)
WHERE company.industry = "Technology"
RETURN
    s.name AS Student,
    collect(DISTINCT skill.name) AS Skills,
    company.name AS Company;
```

---

# 👨‍💻 Author

**Mohammed Saif**

Learning and building projects around:

* Python
* Backend Development
* FastAPI
* Databases
* Neo4j
* Data Analytics
* AI Engineering

---

# 📄 License

This project is created for educational and learning purposes.

````

### Final GitHub checklist

Your repository should look like this:

```text
learning-platform-neo4j/
│
├── cypher/
│   ├── 01_constraints.cypher
│   ├── 02_create_nodes.cypher
│   ├── 03_create_relationships.cypher
│   ├── 04_read_queries.cypher
│   ├── 05_update_queries.cypher
│   └── 06_delete_queries.cypher
│
├── python/
│   ├── neo4j_connection.py
│   └── graph_operations.py
│
├── .gitignore
├── requirements.txt
└── README.md
````

**Do not upload `.env`.** Your final submission can then contain the **GitHub repository link + YouTube video link**.

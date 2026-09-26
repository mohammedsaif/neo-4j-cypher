"""Create the full Learning Platform graph (all node types and relationships)
using the Neo4j Python driver directly, rather than relying on a separate
.cypher file being executed manually.

Run:
    python python/seed_graph.py
"""

import os

from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

STUDENTS = [
    {"id": "S001", "name": "RahulG", "email": "rahul@example.com", "experience": 2},
    {"id": "S002", "name": "PriyaJ", "email": "priya@example.com", "experience": 1},
    {"id": "S003", "name": "ArjunR", "email": "arjun@example.com", "experience": 3},
    {"id": "S004", "name": "Sneha", "email": "sneha@example.com", "experience": 2},
    {"id": "S005", "name": "Vikram", "email": "vikram@example.com", "experience": 4},
]

COURSES = [
    {"id": "C001", "name": "Python Programming", "level": "Beginner"},
    {"id": "C002", "name": "FastAPI Development", "level": "Intermediate"},
    {"id": "C003", "name": "Data Analytics", "level": "Intermediate"},
    {"id": "C004", "name": "Generative AI", "level": "Advanced"},
]

MENTORS = [
    {"id": "M001", "name": "Amit Sharma", "expertise": "Python"},
    {"id": "M002", "name": "Neha Kapoor", "expertise": "Data Analytics"},
    {"id": "M003", "name": "Ravi Kumar", "expertise": "Generative AI"},
]

SKILLS = [
    {"id": "SK001", "name": "Python"},
    {"id": "SK002", "name": "FastAPI"},
    {"id": "SK003", "name": "SQL"},
    {"id": "SK004", "name": "Machine Learning"},
    {"id": "SK005", "name": "Generative AI"},
]

PROJECTS = [
    {"id": "P001", "name": "AI Data Analyst", "status": "Completed"},
    {"id": "P002", "name": "Task Management API", "status": "Completed"},
    {"id": "P003", "name": "Customer Support Bot", "status": "In Progress"},
    {"id": "P004", "name": "Sales Dashboard", "status": "Completed"},
]

COMPANIES = [
    {"id": "CO001", "name": "Microsoft", "industry": "Technology"},
    {"id": "CO002", "name": "Google", "industry": "Technology"},
    {"id": "CO003", "name": "Amazon", "industry": "Technology"},
    {"id": "CO004", "name": "Deloitte", "industry": "Consulting"},
]

ENROLLED_IN = [
    ("S001", "C001"), ("S001", "C002"),
    ("S002", "C001"), ("S002", "C003"),
    ("S003", "C002"), ("S003", "C004"),
    ("S004", "C003"),
    ("S005", "C004"),
]

TEACHES = [
    ("M001", "C001"), ("M001", "C002"),
    ("M002", "C003"),
    ("M003", "C004"),
]

TEACHES_SKILL = [
    ("C001", "SK001"),
    ("C002", "SK002"), ("C002", "SK003"),
    ("C003", "SK003"), ("C003", "SK004"),
    ("C004", "SK004"), ("C004", "SK005"),
]

BUILT = [
    ("S001", "P001"),
    ("S003", "P002"),
    ("S004", "P003"),
    ("S005", "P004"),
]

USES = [
    ("P001", "SK001"), ("P001", "SK004"),
    ("P002", "SK002"), ("P002", "SK003"),
    ("P003", "SK004"),
    ("P004", "SK005"),
]

INTERESTED_IN = [
    ("S001", "CO001"),
    ("S002", "CO002"),
    ("S003", "CO003"),
    ("S004", "CO004"),
    ("S005", "CO001"),
]


def create_nodes(session, label, records):
    query = f"""
    UNWIND $records AS record
    MERGE (n:{label} {{id: record.id}})
    SET n += record
    """
    session.run(query, records=records)


def create_relationships(session, from_label, rel_type, to_label, pairs):
    query = f"""
    UNWIND $pairs AS pair
    MATCH (a:{from_label} {{id: pair[0]}}), (b:{to_label} {{id: pair[1]}})
    MERGE (a)-[:{rel_type}]->(b)
    """
    session.run(query, pairs=pairs)


def seed_graph(driver):
    with driver.session() as session:
        create_nodes(session, "Student", STUDENTS)
        create_nodes(session, "Course", COURSES)
        create_nodes(session, "Mentor", MENTORS)
        create_nodes(session, "Skill", SKILLS)
        create_nodes(session, "Project", PROJECTS)
        create_nodes(session, "Company", COMPANIES)

        create_relationships(session, "Student", "ENROLLED_IN", "Course", ENROLLED_IN)
        create_relationships(session, "Mentor", "TEACHES", "Course", TEACHES)
        create_relationships(session, "Course", "TEACHES_SKILL", "Skill", TEACHES_SKILL)
        create_relationships(session, "Student", "BUILT", "Project", BUILT)
        create_relationships(session, "Project", "USES", "Skill", USES)
        create_relationships(session, "Student", "INTERESTED_IN", "Company", INTERESTED_IN)


def main() -> None:
    uri = os.environ["NEO4J_URI"]
    user = os.environ["NEO4J_USERNAME"]
    password = os.environ["NEO4J_PASSWORD"]

    driver = GraphDatabase.driver(uri, auth=(user, password))
    try:
        driver.verify_connectivity()
        seed_graph(driver)
        print("Graph seeded: 25 nodes, 34 relationships created (or already present).")
    finally:
        driver.close()


if __name__ == "__main__":
    main()

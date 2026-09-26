import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")

if not URI or not USERNAME or not PASSWORD:
    raise ValueError("Missing Neo4j configuration")

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))


def verify_connection():
     with driver.session() as session:
          result = session.run("RETURN 'Neo4j connection successful' AS message")
          record = result.single()
          if record is None:
            raise RuntimeError("Neo4j connection check returned no result")
          print(record["message"])

if __name__ == "__main__":
    try:
        verify_connection()
    finally:
        driver.close()
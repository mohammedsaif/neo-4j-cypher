"""Run a .cypher file against Neo4j Aura, with optional parameters.

Usage:
    python run_cypher.py cypher/04_read_queries.cypher
    python run_cypher.py cypher/06_delete_queries.cypher --params params/06_delete_queries.json
"""

import argparse
import json
import os
import sys

from dotenv import load_dotenv
from neo4j import GraphDatabase


def split_statements(text: str) -> list[str]:
    return [stmt.strip() for stmt in text.split(";") if stmt.strip()]


def run_file(driver, database: str, path: str, params: dict) -> None:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    with driver.session(database=database) as session:
        for i, statement in enumerate(split_statements(content), start=1):
            result = session.run(statement, params)
            records = [record.data() for record in result]
            print(f"--- statement {i} ---")
            print(statement)
            if records:
                for record in records:
                    print(record)
            print()


def main() -> None:
    load_dotenv()

    parser = argparse.ArgumentParser(description="Run a .cypher file with parameters.")
    parser.add_argument("cypher_file", help="Path to the .cypher file to run")
    parser.add_argument(
        "--params",
        help="Path to a JSON file of query parameters, or a raw JSON string",
        default=None,
    )
    args = parser.parse_args()

    params: dict = {}
    if args.params:
        if os.path.isfile(args.params):
            with open(args.params, "r", encoding="utf-8") as f:
                params = json.load(f)
        else:
            params = json.loads(args.params)

    uri = os.environ["NEO4J_URI"]
    user = os.environ["NEO4J_USERNAME"]
    password = os.environ["NEO4J_PASSWORD"]
    database = os.environ.get("NEO4J_DATABASE", "neo4j")

    driver = GraphDatabase.driver(uri, auth=(user, password))
    try:
        driver.verify_connectivity()
        run_file(driver, database, args.cypher_file, params)
    finally:
        driver.close()


if __name__ == "__main__":
    sys.exit(main())

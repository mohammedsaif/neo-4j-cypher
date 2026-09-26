import os

from dotenv import load_dotenv
from neo4j import GraphDatabase
from neo4j.exceptions import Neo4jError, ServiceUnavailable


load_dotenv()


class LearningPlatform:

    def __init__(self):
        uri = os.getenv("NEO4J_URI")
        username = os.getenv("NEO4J_USERNAME")
        password = os.getenv("NEO4J_PASSWORD")

        if not uri or not username or not password:
            raise ValueError("Missing Neo4j configuration")

        try:
            self.driver = GraphDatabase.driver(uri, auth=(username, password))
            self.driver.verify_connectivity()
        except (ServiceUnavailable, Neo4jError) as e:
            raise RuntimeError(f"Failed to connect to Neo4j: {e}") from e

    def close(self):
        self.driver.close()

    def create_student(self, student_id, name, email, experience):

        query = """
        MERGE (s:Student {id: $id})
        ON CREATE SET
            s.name = $name,
            s.email = $email,
            s.experience = $experience
        RETURN s
        """

        with self.driver.session() as session:
            result = session.run(
                query,
                id=student_id,
                name=name,
                email=email,
                experience=experience
            )

            record = result.single()
            created = result.consume().counters.nodes_created > 0

            if record and created:
                print("Created:", record["s"])
            elif record:
                print("Student already exists, skipped create:", record["s"])

    def read_students(self):

        query = """
        MATCH (s:Student)
        RETURN s
        ORDER BY s.name
        """

        with self.driver.session() as session:
            result = session.run(query)

            for record in result:
                print(record["s"])

    def update_student(self, student_id, experience):

        query = """
        MATCH (s:Student {id: $id})
        SET s.experience = $experience
        RETURN s
        """

        with self.driver.session() as session:
            result = session.run(
                query,
                id=student_id,
                experience=experience
            )

            record = result.single()

            if record:
                print("Updated:", record["s"])

    def delete_student(self, student_id):

        query = """
        MATCH (s:Student {id: $id})
        DETACH DELETE s
        """

        with self.driver.session() as session:
            session.run(
                query,
                id=student_id
            )

            print("Student deleted:", student_id)


if __name__ == "__main__":

    platform = LearningPlatform()

    try:

        platform.create_student(
            "S100",
            "Test Student",
            "test@example.com",
            1
        )

        print("\n--- Students ---")

        platform.read_students()

        print("\n--- Update ---")

        platform.update_student(
            "S100",
            2
        )

        print("\n--- Delete ---")

        platform.delete_student(
            "S100"
        )

    finally:

        platform.close()
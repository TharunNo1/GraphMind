from neo4j import GraphDatabase
from config import Config
from utils.logger import logger

class Neo4jConnection:
    def __init__(self):
        self.driver = None
        self.connect()

    def connect(self):
        try:
            self.driver = GraphDatabase.driver(
                Config.NEO4J_URI, auth=(Config.NEO4J_USER, Config.NEO4J_PASSWORD)
            )
            logger.info("Successfully connected to Neo4j")
        except Exception as e:
            logger.error(f"Failed to connect to Neo4j: {e}")

    def execute_query(self, query):
        if not self.driver:
            raise Exception("No connection to Neo4j")
        with self.driver.session() as session:
            try:
                result = session.run(query)
                return [record.data() for record in result]
            except Exception as e:
                logger.error(f"Error executing Cypher query: {e}")
                return None

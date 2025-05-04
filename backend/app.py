from flask import Flask, request, jsonify
from services.llama_service import LlamaService
from utils.query_utils import Neo4jConnection
from utils.logger import logger

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query_graph():
    data = request.get_json()
    user_question = data.get("question", "")

    if not user_question:
        return jsonify({"error": "Question is required"}), 400

    # Create the prompt for LLaMA
    prompt = f"""
    You are a system that translates natural language into Cypher queries for a Neo4j knowledge graph.

    Graph schema:
    (:Person {{name}})
    (:Project {{name}})
    (:Organization {{name}})
    Relationships:
    (:Person)-[:WORKS_ON]->(:Project)
    (:Person)-[:MEMBER_OF]->(:Organization)
    (:Project)-[:FUNDED_BY]->(:Organization)

    Convert this question into Cypher:
    \"\"\"{user_question}\"\"\"
    Return only the Cypher query.
    """

    # Use LLaMA service to get Cypher query
    llama_service = LlamaService()
    cypher_query = llama_service.get_cypher_query(prompt)
    print(cypher_query)
    if not cypher_query:
        return jsonify({"error": "Failed to generate Cypher query from LLaMA"}), 500

    # Use Neo4j connection to execute the query
    neo4j_conn = Neo4jConnection()
    results = neo4j_conn.execute_query(cypher_query)

    if results is None:
        return jsonify({"error": "Failed to execute Cypher query on Neo4j"}), 500

    return jsonify({"query": cypher_query, "results": results})

if __name__ == '__main__':
    app.run(debug=True, port=5003 )

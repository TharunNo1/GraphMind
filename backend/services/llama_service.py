import requests
from config import Config
from utils.logger import logger
import json

class LlamaService:
    def __init__(self):
        self.url = Config.OLLAMA_URL

    def get_cypher_query(self, prompt):
        try:
            response = requests.post(self.url, json={"model": "llama3.2", "prompt": prompt})
            response.raise_for_status() 
            
            return self.extract_first_valid_json(str(response.text))
        except requests.exceptions.RequestException as e:
            logger.error(f"Error calling LLaMA API: {e}")
            return None
        except ValueError as e:
            logger.error(f"Error parsing LLaMA response: {e}")
            return None
    import json

    def extract_first_valid_json(self, text):
        try:
            # Try to find the first valid JSON object
            lines = text.strip().splitlines()
            valid_json = True
            parse_jsons = []
            for line in lines:
                try:
                    json_data = json.loads(line)
                    parse_jsons.append(json_data.get("response",""))
                except json.JSONDecodeError:
                    valid_json = False
                    break
            if valid_json:
                return "".join(parse_jsons)
            raise ValueError("No valid JSON found in response.")
        except Exception as e:
            logger.error(f"Failed to parse JSON: {e}")
            return None

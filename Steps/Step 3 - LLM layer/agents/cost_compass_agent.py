import os
import json
import logging
from dotenv import load_dotenv
from pydantic_ai import Agent, RunContext
from prompts.router_prompt import ROUTER_PROMPT
from tools.sql_tool import sql_tool, SQL_TOOL_DOCSTRING
from utils.logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

load_dotenv()

def main() -> None:

    # Create router agent
    router_agent = Agent(model=f"openai:{os.getenv('GPT_LIGHT_MODEL')}", system_prompt=ROUTER_PROMPT)

    # Tools
    router_agent.tool(sql_tool)

    # Execute
    result = router_agent.run_sync("Ejecuta la herramienta de SQL para obtener el precio medio de la vivienda entre 2024 y 2026")


if __name__ == "__main__":
    main()
from typing import Annotated

from langchain.chat_models import init_chat_model
from typing_extensions import TypedDict

from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit

from langchain import hub

from langgraph.prebuilt import create_react_agent


# -------------------------------- INSTANTIATE LLM --------------------------------
import getpass
import os
from dotenv import load_dotenv

load_dotenv()
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")


# llm = init_chat_model("anthropic:claude-3-5-sonnet-latest")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

# -------------------------------- LANGGRAPH --------------------------------
from sqlalchemy import create_engine

# For database in current directory
# engine = create_engine('sqlite:///tysql.sqlite')

db = SQLDatabase.from_uri("sqlite:///tysql.sqlite")
print(db.run("SELECT * FROM Customers LIMIT 10;"))


toolkit = SQLDatabaseToolkit(db=db, llm=llm)
tools = toolkit.get_tools()

prompt_template = hub.pull('langchain-ai/sql-agent-system-prompt')
system_message = prompt_template.format(dialect='SQLite', top_k=5)

sql_agent = create_react_agent(llm, tools, prompt=system_message)

query = 'Find the customer with the most orders.'

for event in sql_agent.stream(
    {"messages": ('user', query)},
    stream_mode='values'
):
    event['messages'][-1].pretty_print()
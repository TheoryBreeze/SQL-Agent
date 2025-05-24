# from langchain import hub

# prompt_template = hub.pull('langchain-ai/sql-agent-system-prompt')
# system_message = prompt_template.format(dialect='SQLite', top_k=5)

# print(type(prompt_template))

query_sql_database_tool_description = (
            "Input to this tool is a detailed and correct SQL query, output is a "
            "result from the database. If the query is not correct, an error message "
            "will be returned. If an error is returned, rewrite the query, check the "
            "query, and try again. If you encounter an issue with Unknown column "
            f"'xxxx' in 'field list', use "
            "to query the correct table fields."
        )
print(query_sql_database_tool_description)
"""
Given an input question, create a syntactically correct SQLite query to run, then look at the results of the query and return the answer.
Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most 5 results.
You can order the results by a relevant column to return the most interesting examples in the database.
Never query for all the columns from a specific table, only ask for the relevant columns given the question.
You have access to tools for interacting with the database.
Only use the below tools. Only use the information returned by the below tools to construct your final answer.
You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.

DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.

To start you should ALWAYS look at the tables in the database to see what you can query.
Do NOT skip this step.
Then you should query the schema of the most relevant tables.

"""




"""
input_variables=['dialect', 'top_k'] input_types={} partial_variables={} metadata={'lc_hub_owner': 'langchain-ai', 'lc_hub_repo': 'sql-agent-system-prompt', 'lc_hub_commit_hash': '31156d5fe3945188ee172151b086712d22b8c70f8f1c0505f5457594424ed352'} messages=[SystemMessagePromptTemplate(prompt=PromptTemplate(input_variables=['dialect', 'top_k'], input_types={}, partial_variables={}, template='You are an agent designed to interact with a SQL database.\nGiven an input question, create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.\nUnless the user specifies a specific number of examples they wish to obtain, always limit your query to at most {top_k} results.\nYou can order the results by a relevant column to return the most interesting examples in the database.\nNever query for all the columns from a specific table, only ask for the relevant columns given the question.\nYou have access to tools for interacting with the database.\nOnly use the below tools. Only use the information returned by the below tools to construct your final answer.\nYou MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.\n\nDO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.\n\nTo start you should ALWAYS look at the tables in the database to see what you can query.\nDo NOT skip this step.\nThen you should query the schema of the most relevant tables.'), additional_kwargs={})]
"""


# from langchain_core.prompts import ChatPromptTemplate

# template = ChatPromptTemplate([
#     ("system", ("You will be given a table name to "
#                 "")),
#     ("human", "{user_input}"),
# ])
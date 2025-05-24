from typing import List
import pandas as pd
from sqlalchemy import (
    create_engine,
    inspect,
    text,
)

class SQLiteDB:
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)

    def get_table_names(self) -> str:
        inspector = inspect(self.engine)
        tables = inspector.get_table_names()
        return ", ".join(sorted(tables))

    def get_table_schema(self, table_names: List[str]) -> str:
        schema_output = []
        with self.engine.connect() as conn:
            for table in table_names:
                table_info = ""
                # Get CREATE TABLE statement
                result = conn.execute(text(f"SELECT sql FROM sqlite_master WHERE type='table' AND name=:table"), {"table": table}).fetchone()
                if result:
                    table_info += result[0]
                # Get sample rows
                df = pd.read_sql_query(f"SELECT * FROM {table} LIMIT 3", conn)
                table_info += "\n\n/*\n3 rows from {} table:\n{}*/".format(table, df.to_csv(index=False, sep='\t'))
                schema_output.append(table_info)
        return "\n\n\n".join(schema_output)

    def get_random_col_examples(self, table_name: str, col_name: str) -> str:
        with self.engine.connect() as conn:
            df = pd.read_sql_query(
                f"SELECT {col_name} FROM {table_name} ORDER BY RANDOM() LIMIT 10",
                conn
            )
        return df.to_csv(index=False)
    

db = SQLiteDB("sqlite:///tysql.sqlite")
result = db.get_random_col_examples("OrderItems", "item_price")
print(result)
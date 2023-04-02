import psycopg2
from commons.constants import (
    DATABASE_NAME,
    DATABASE_USER,
    DATABASE_PASSWORD,
    DATABASE_HOST,
    DATABASE_PORT
)


def _get_database():
   print(f'*** Connecting to the {DATABASE_NAME} dataabse.. ***')
   _connection = None
   _cursor_obj = None

   try:
       _connection = psycopg2.connect(
           database=f"{DATABASE_NAME}",
           user=f"{DATABASE_USER}",
           password=f"{DATABASE_PASSWORD}",
           host=f"{DATABASE_HOST}",
           port=f"{DATABASE_PORT}"
       )

       _cursor_obj = _connection.cursor()

   except psycopg2.OperationalError as e:
       print(f'Unable to connect!\n{e}')
   else:
       print(f'*** Connected to the {DATABASE_NAME} dataabse. ***')
       return _connection, _cursor_obj







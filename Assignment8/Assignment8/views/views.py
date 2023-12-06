import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from openai import OpenAI
import mysql.connector
import os
from dotenv import load_dotenv
import re
def openai_init():
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key = OPENAI_API_KEY)


def test_command():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345678',
        database='travel_agent'
    )

    cursor = connection.cursor()

    # Get all table names in the database
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    schema_str = ""

    # Loop through all tables to describe those starting with "assignment7"
    for table in tables:
        table_name = table[0]
        if table_name.startswith('travel_agent'):
            schema_str += f"Schema of {table_name}\n"

            # Execute DESCRIBE TABLE command to get schema details
            cursor.execute(f"DESCRIBE {table_name}")
            schema = cursor.fetchall()

            for column in schema:
                schema_str += str(column) + "\n"

            schema_str += "\n"  # Separate each table's schema with a newline

    # Close the database connection
    cursor.close()
    connection.close()
    return schema_str

class health_check(APIView):
    def get(self, request):
        payload = {
            "answer": "pong",
            "chat_history_id": "1"
        }
        return Response(payload, status=status.HTTP_200_OK)

class text_to_SQL(APIView):
    def get(self, request):
        openai_init()
        schema = test_command()
        command = request.GET.get('message', 'default')
        print(command)
        gpt = OpenAI().chat.completions.create(
            model="gpt-4",
            temperature=0.9,
            messages=[
                {"role": "system",
                 "content": "You can reply general questions about traveling translate natural language to SQL queries."},
                {"role": "system","content": "This is the schema of the packages of different travel routes."},
                {"role": "system", "content": schema},
                {"role": "system", "content": "if the questions are related to the schema respond with the SQL queries between triple backticks otherwise respond with your knowledge base."},
                {"role": "user", "content": command},
            ]
        )
        # response = {"role": "user", "content": ['content']}
        # gpt.
        sql = gpt.choices[0].message.content
        sql.lower()
        print(sql)
        pattern = r"```sql(.*?)```"
        match = re.findall(pattern, sql, re.DOTALL)
        print(match)
        if match:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='12345678',
                database='text_to_sql'
            )
            cursor = connection.cursor(dictionary=True)
            cursor.execute("use travel_agent")
            # sql = re.findall(pattern, sql, re.S)[0]
            # sql = sql.replace('```sql', "")
            # print(sql)
            cursor.execute(match[0])
            msg = cursor.fetchall()
            cursor.close()
            # print(msg[0])
            # print(gpt.choices[0].message)
            newGpt= OpenAI().chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content":"you need to change this part into natural language"},
                    {"role": "user", "content": json.dumps(msg)},
                ]
            )
            nl = newGpt.choices[0].message.content
            # gpt.choices[0].messages.append({"role": "system", "content": msg[0]})
            print(nl)
            return Response(nl, status=status.HTTP_200_OK)
        else:
            print('sql error')
            msg = sql
            print(msg)
            return Response(msg, status=status.HTTP_201_CREATED)
        # print(sql.replace('```', "").replace('sql', ""))

        # render(request, 'table.html', {'headers': headers, 'data': msg})
        # return render(request, 'table.html', {'headers': headers, 'data': msg})

import sqlite3
from models.TodoModel import TodoModel
def get_connection() -> sqlite3.Connection:
    return sqlite3.connect("todo.db")
class TodoRepository:
    def add(self, todo: TodoModel):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO todo(title, description, start_date, end_date, completed) values(?,?,?,?,?)""",
                       (
                           todo.title,
                           todo.description,
                           todo.start_date,
                           todo.end_date,
                           int(todo.completed)
                       ))
        connection.commit()
        todo_id = cursor.lastrowid
        connection.close()
        return todo_id
    def _row_to_todo(self, todo_row):
        return TodoModel(
            _id = todo_row[0],
            _title= todo_row[1],
            _description= todo_row[2],
            _start_date= todo_row[3],
            _end_date= todo_row[4],
            _completed= todo_row[5],
        )
    def get_all(self) -> list[TodoModel]:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""SELECT * from todo""")
        rows = cursor.fetchall()
        connection.close()
        return [self._row_to_todo(r) for r in rows]

from db.connector import get_connection
from models.TodoModel import TodoModel


class TodoRepository:
    @classmethod
    def add(cls, todo: TodoModel):
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
            _todo_id= todo_row[0],
            _title= todo_row[1],
            _description= todo_row[2],
            _start_date= todo_row[3],
            _end_date= todo_row[4],
            _completed= bool(todo_row[5]),
        )
    def get_all(self) -> list[TodoModel]:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""SELECT * from todo""")
        rows = cursor.fetchall()
        connection.close()
        return [self._row_to_todo(r) for r in rows]
    @staticmethod
    def __delete_todo(func):
        def wrapper(*args, **kwargs):
            query, value = func(*args, **kwargs)
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute(query, value)
            deleted = cursor.rowcount
            connection.close()
            return int(deleted) > 0
        return wrapper
    @staticmethod
    def __update_todo(func):
        def wrapper(*args, **kwargs):
            query, value = func(*args, **kwargs)
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute(query, value)
            todo_id = cursor.lastrowid
            connection.close()
            return int(todo_id) > 0
        return wrapper
    @__delete_todo
    def delete_todo_by_id(self, todo_id: int):
        return "DELETE FROM todo WHERE id = ?", (int(todo_id),)
    @__delete_todo
    def delete_todo_by_title(self, title: str):
        return "DELETE FROM todo WHERE title = ?", (str(title),)
    @__delete_todo
    def delete_todo_by_description(self, description: str):
        return "DELETE FROM todo WHERE description = ?", (str(description),)
    @__delete_todo
    def delete_todo_by_start_date(self, start_date: str):
        return "DELETE FROM todo WHERE start_date = ?", (str(start_date),)
    @__delete_todo
    def delete_todo_by_end_date(self, end_date: str):
        return "DELETE FROM todo WHERE end_date = ?", (str(end_date),)
    @__delete_todo
    def delete_todo_by_completed(self, completed: bool):
        return "DELETE FROM todo WHERE completed = ?", (int(completed),)
    @__update_todo
    def change_todo_title(self, row_id: int, new_title: str):
        return "UPDATE todo SET title = ? WHERE id = ?", (str(new_title), row_id,)
    @__update_todo
    def change_todo_description(self, row_id: int, new_description: str):
        return "UPDATE todo SET description = ? WHERE id = ?", (str(new_description), row_id,)
    @__update_todo
    def change_todo_start_date(self, row_id: int, new_start_date: str):
        return "UPDATE todo SET start_date = ? WHERE id = ?", (str(new_start_date), row_id,)
    @__update_todo
    def change_todo_end_date(self, row_id: int, new_end_date: str):
        return "UPDATE todo SET end_date = ? WHERE id = ?", (str(new_end_date), row_id,)
    @__update_todo
    def change_todo_completed(self, row_id: int, new_completed: bool):
        return "UPDATE todo SET completed = ? WHERE id = ?", (int(new_completed), row_id,)
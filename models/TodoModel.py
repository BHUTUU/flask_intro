from dataclasses import dataclass
@dataclass
class TodoModel:
    _id: int
    _title: str
    _description: str
    _start_date: str
    _end_date: str
    _completed: bool
    @property
    def id(self) -> int:
        return self._id
    @property
    def title(self) -> str:
        return self._title
    @property
    def description(self) -> str:
        return self._description
    @property
    def start_date(self) -> str:
        return self._start_date
    @property
    def end_date(self) -> str:
        return self._end_date
    @property
    def completed(self) -> bool:
        return self._completed
    @id.setter
    def id(self, id: int) -> None:
        if not id:
            raise AttributeError('id cannot be None')
        self._id = id
    @title.setter
    def title(self, title: str) -> None:
        if not title.strip():
            raise AttributeError('title cannot be empty')
        self._title = title
    @description.setter
    def description(self, description: str) -> None:
        if not description.strip():
            raise AttributeError('description cannot be empty')
        self._description = description
    @completed.setter
    def completed(self, completed: bool) -> None:
        if completed is None or completed == "":
            raise AttributeError('completed cannot be empty')
        self._completed = completed
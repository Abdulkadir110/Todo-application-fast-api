from todo_application_fast_api.models.todo import Todo, TodoCreate
from todo_application_fast_api.repositories.todo_repository import TodoRepository

class TodoNotFoundError(Exception):
    """Raised when a todo does not exist. The Controller turns this
into a proper HTTP 404 -- the Service knows nothing about HTTP."""
    pass

class TodoService:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def create_todo(self, payload: TodoCreate) -> Todo:
        todo = Todo(title=payload.title, description=payload.description)
        return self.repository.add(todo)

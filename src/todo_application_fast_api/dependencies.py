from fastapi import Depends
from todo_application_fast_api.repositories.todo_repository import TodoRepository
from todo_application_fast_api.repositories.in_memory_todo_repository import InMemoryTodoRepository
from todo_application_fast_api.services.todo_service import TodoService
_repository = InMemoryTodoRepository()
def get_todo_repository() -> TodoRepository:
    return _repository
def get_todo_service(
    repository: TodoRepository = Depends(get_todo_repository),
) -> TodoService:
    return TodoService(repository)
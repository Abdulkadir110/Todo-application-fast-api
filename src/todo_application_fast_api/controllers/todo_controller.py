from fastapi import APIRouter, Depends, status
from todo_application_fast_api.models.todo import Todo, TodoCreate
from todo_application_fast_api.services.todo_service import TodoService
from todo_application_fast_api.dependencies import get_todo_service
router = APIRouter(prefix="/todos", tags=["Todos"])
@router.post("/", response_model=Todo, status_code=status.HTTP_201_CREATED)
def create_todo(
    payload: TodoCreate,
    service: TodoService = Depends(get_todo_service),
):
    return service.create_todo(payload)
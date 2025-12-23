
from typing import TypedDict


class Task(TypedDict):
    id: int
    title: str
    priority: str
    tags: list[str]
    status: str

PRIORITIES = {"low", "med", "hight"}


t: Task = {
    "id": 1,
    "title": "Вытереть пыль",
    "priority": "low",
    "status": "new",
    "tags": ["Дом"]
}


def make_task(id_: int, title: str, priority: str = "med", tags: list[str] = []) -> Task:
    if priority not in PRIORITIES:
        raise ValueError("Неверный приоритет. Можно только low | med | hight")
    task: Task = {
        "id": id_,
        "title": title.strip(),
        "priority": priority,
        "tags": tags,
        "status": "new"
    }
    return task

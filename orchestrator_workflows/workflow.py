import csv
import httpx
from restate import Workflow, WorkflowContext, WorkflowSharedContext
from app.models import User


red_file_workflow = Workflow("ReadFileWorkflow")


def csv_to_dict(csv_string: str) -> list[dict]:
    reader = csv.reader(csv_string.splitlines())
    columns = next(reader)
    return [dict(zip(columns, row)) for row in reader]


async def generate_uuid() -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get("http://127.0.0.1:8000/uuid")
        return response.json()["uuid"]


async def create_user_serializable(user_data: dict) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.post("http://127.0.0.1:8000/user", json=user_data)
        return response.json()


async def create_user(user: dict) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.post("http://127.0.0.1:8000/user", json=user)
        return response.json()


@red_file_workflow.main()
async def run(context: WorkflowContext, request: dict):
    print(f"request: {request}")
    file_path = request["file_path"]
    print(f"file_path: {file_path}")
    assert file_path.endswith(".csv")
    with open(file_path, "r") as file:
        csv_string = file.read()
        data = csv_to_dict(csv_string)

    for row in data:
        uuid = await context.run("generate_uuid", generate_uuid)
        user = User(id=uuid, **row)
        user_serializable = user.model_dump()

        async def create_user_task():
            return await create_user(user_serializable)

        await context.run("create_user", create_user_task)

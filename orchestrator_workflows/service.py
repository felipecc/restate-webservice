from restate import Service, Context
import httpx
import uuid

activate_service = Service("ActivateService")


@activate_service.handler("active_read_file_wf")
async def activate_workflow(context: Context, workflow_id: str):
    async with httpx.AsyncClient() as client:
        data = {"file_path": "/home/felipecc/projetos/restate-webserice/data/users.csv"}
        workflow_id = str(uuid.uuid4())[:8]

        response = await client.post(
            f"http://127.0.0.1:8080/ReadFileWorkflow/{workflow_id}/run/send", json=data
        )
        return response.json()

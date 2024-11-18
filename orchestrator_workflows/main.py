from orchestrator_workflows.workflow import red_file_workflow
from orchestrator_workflows.service import activate_service
import restate

app = restate.app([red_file_workflow, activate_service])

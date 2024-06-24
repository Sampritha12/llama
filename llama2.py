
from clarifai.client.workflow import Workflow

# Your PAT (Personal Access Token) can be found in the Account's Security section

# Initialize the workflow_url
workflow_url = "https://clarifai.com/49jzh4x0s026/llama2-tutorial-desc/workflows/workflow-f79355"
text_classfication_workflow = Workflow(
    url= workflow_url , pat="72b9e6c3d11047c18e6e259f4f001795"
)
result = text_classfication_workflow.predict_by_bytes(b"I hate you", input_type="text")
print(result.results[0].outputs[0].data)

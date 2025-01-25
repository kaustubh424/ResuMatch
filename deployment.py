from mira_sdk import MiraClient, CompoundFlow
from mira_sdk.exceptions import FlowError

client = MiraClient(config={"API_KEY": "sb-bcb2dbfe4b14cd796fe774bc17654894"})
flow = CompoundFlow(source="C:\\Users\\cherr\\Downloads\\MIRA hackathon\\resume-processing-pipeline.yaml")           # Load flow configuration

try:
    client.flow.deploy(flow)                               # Deploy to platform
    print("Compound flow deployed successfully!")          # Success message
except FlowError as e:
    print(f"Deployment error: {str(e)}")                   # Handle deployment error

from mira_sdk import MiraClient,CompoundFlow
from mira_sdk.exceptions import FlowError

# Initialize the client
client = MiraClient(config={"API_KEY": "sb-bcb2dbfe4b14cd796fe774bc17654894"})
flow= CompoundFlow(source="C:\\Users\\cherr\\Downloads\\MIRA hackathon\\resume-processing-pipeline.yaml")

# Test the flow using the appropriate method (e.g., `run_flow`)
test_input = {
    "Insert Resume Text Here": "John Doe\nSkills: Python",
    "user_interest": "Innovative approaches"

}

try:
    response = client.flow.test(flow, test_input)
    print(response)
except FlowError as e:
    print("Test failed:",str(e)) 

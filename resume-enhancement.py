from mira_sdk import MiraClient, Flow

# Initialize the client
client = MiraClient(config={"API_KEY": "YOUR_API_KEY"})

version = "1.0.0"
input_data = {
    "job_title": "",
    "original_resume": "",
    "job_requirements": ""
}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@stutijain2006/resume-enhancement/{version}"
else:
    flow_name = "@stutijain2006/resume-enhancement"

result = client.flow.execute(flow_name, input_data)
print(result)
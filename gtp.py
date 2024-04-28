from openai import OpenAI

client = OpenAI(
  organization='YOUR_ORG_ID',
  project='$PROJECT_ID',
)

OpenAI.api_key = 'sk-proj-6JvbCHlmMJrr2lNjMG8aT3BlbkFJ9J5ONsGpWQ9GJbjdBnp4'








print(OpenAI.api_key)
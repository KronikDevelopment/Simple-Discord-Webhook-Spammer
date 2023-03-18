import requests

# Set the Discord webhook URL
webhook_url = "https://discord.com/api/webhooks/1086734976151736400/cGLc6SZO-vFAQC-PZxlf0FQdXeXKEVvUr7W0Um6O52uLCP4iyiCrLPNKZxof4IMK58S6"

# Set the number of times to send the webhook
num_times = int(input("Enter the number of times to send the webhook: "))

# Define the message to send to the webhook
message = "Hello, world!"

# Define the webhook data
data = {
    "content": message
}

# Send the webhook multiple times
for i in range(num_times):
    # Send a POST request to the webhook URL with the data
    response = requests.post(webhook_url, json=data)

    # Print the response status code
    print(f"Webhook response code for message {i+1}: {response.status_code}")

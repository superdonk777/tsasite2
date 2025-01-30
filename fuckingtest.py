import requests

# Set the API URL
DEEPSEEK_API_URL = "http://127.0.0.1:11434/api/generate"

# Prepare the data to send
data = {
    "model": "deepseek-r1:1.5b",  # Use the installed model
    "prompt": "Generate a recipe for vegan chocolate cake.",  # Recipe prompt
    "stream": False
}

try:
    # Send the POST request
    response = requests.post(DEEPSEEK_API_URL, json=data)

    # Print the status code and response text for debugging
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    if response.status_code == 200:
        # If the response is successful, try to print the JSON data
        response_data = response.json()
        print("Recipe:", response_data.get("response"))
    else:
        print("Error: Failed to get valid response from the server.")

except requests.exceptions.RequestException as e:
    print(f"Error: {str(e)}")
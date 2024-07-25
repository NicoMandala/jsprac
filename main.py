import streamlit as st
import requests
from openai import OpenAI


# Initialize the OpenAI API key

client = OpenAI()

def get_user_book_review(user_name):
    # Define the API URL
    url = f"http://localhost:3000/v1/reviews?username={user_name}"
    print(f"API URL: {url}")
    
    try:
        # Make the API call
        print("Making API call...")
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        
        # Parse the JSON response
        print("Parsing JSON response...")
        reviews = response.json()
        print(f"Reviews received: {reviews}")
        
        # If the response contains reviews, process them with GPT
        if reviews:
            review_texts = [review['quote_or_review_text'] for review in reviews]
            combined_reviews = "\n".join(review_texts)
            print(f"Combined reviews text: {combined_reviews}")
            
            # Call GPT to process the reviews
            gpt_response = call_gpt(combined_reviews)
            return gpt_response
        
        else:
            print("No reviews found for the specified username.")
            return "No reviews found for the specified username."
    except requests.RequestException as e:
        print(f"An error occurred while fetching reviews: {e}")
        return f"An error occurred while fetching reviews: {e}"

assistant = client.beta.assistants.create(
    instructions="tell the review of the book. use the provided function to get the review of the user",
    model="gpt-4o-mini",
    tools=[
        "type":"function",
        "function": {
            "name": "get_user_book_review",
            "description": "Get the book reviews of the user",
            "parameters":  {
                "type": "string",
                "properties": {
                    "user_name":{
                        "type": "string",
                        "description": "The username of the user"
                    }

            },
            "required": ["user_name"]
        }
    }])

thread = client.beta.threads.create()
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Can you tell me the review of the book of the user with name brenda95?"
)






# Function to call the API and get user book reviews
def get_user_book_reviews(username):
    # Define the API URL
    url = f"http://localhost:3000/v1/reviews?username={username}"
    print(f"API URL: {url}")

    try:
        # Make the API call
        print("Making API call...")
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        # Parse the JSON response
        print("Parsing JSON response...")
        reviews = response.json()
        print(f"Reviews received: {reviews}")

        # If the response contains reviews, process them with GPT
        if reviews:
            review_texts = [review['quote_or_review_text'] for review in reviews]
            combined_reviews = "\n".join(review_texts)
            print(f"Combined reviews text: {combined_reviews}")

            # Call GPT to process the reviews
            gpt_response = call_gpt(combined_reviews)
            return gpt_response

        else:
            print("No reviews found for the specified username.")
            return "No reviews found for the specified username."

    except requests.RequestException as e:
        print(f"An error occurred while fetching reviews: {e}")
        return f"An error occurred while fetching reviews: {e}"

# Function to call GPT with the reviews text
def call_gpt(reviews_text):
    try:
        # Call the GPT model
        print("Calling GPT model...")
        response = client.completions.create(
            model="gpt-4o",  # Replace with the desired GPT engine
            prompt=f"Here are some book reviews:\n{reviews_text}\nSummarize these reviews:",
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7
        )

        # Extract the GPT response
        gpt_output = response.choices[0].text.strip()
        print(f"GPT response: {gpt_output}")
        return gpt_output

    except Exception as e:
        print(f"An error occurred while processing with GPT: {e}")
        return f"An error occurred while processing with GPT: {e}"

# Streamlit app
st.title("Book Review Chatbot")

# Input for username
username = st.text_input("Enter the username to fetch book reviews:")

# Fetch and display the reviews when the button is clicked
if st.button("Get Reviews"):
    if username:
        result = get_user_book_reviews(username)
        st.write(result)
    else:
        st.write("Please enter a username.")

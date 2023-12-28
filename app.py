from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set OpenAI API key
openai.api_key = "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"

#Implement the POST Endpoint
@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        data = request.json
        user_input = data['content']

        #Handle the User Question
        if user_input.lower() == "what services do you provide?":
            #Implement the Local Function
            services = get_services()
            response = generate_chatbot_response(services)
        else:
            #Handle other user inputs
            response = generate_chatbot_response("I'm sorry, I didn't understand the question.")

        return jsonify({'response': response})

    except Exception as e:
        return jsonify({'error': str(e)})

#Create the HTTP Response
def generate_chatbot_response(answer):
    return f"Chatbot Answer: {answer}"

#Implement the Local Function
def get_services():
    # Log the function call
    print("Local function called: get_services()")
    return ["General cleaning", "Specialized cleaning"]

if __name__ == '__main__':
    app.run(debug=True)

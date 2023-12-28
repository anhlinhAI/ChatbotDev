This is a simple project to fulfill these requirements:
1. You need to create a chatbot service, accessible via http api. You can use any language and web framework which you like the most.
2. API has only 1 POST endpoint which accepts JSON with a single parameter named “content”. This field is a user input message for a chatbot.
3. For chatbot implementation you can use any LLM framework (langchain, autogen, semantic kernel), or don’t use any framework and call LLM directly, it’s up to you.
4. Chatbot should be able to answer only 1 user question: “What services do you provide?”. To answer this question LLM must call a local function, which returns hardcoded array [ “General cleaning”, “Specialized cleaning” ]. Inside the function log to stdout any string, to confirm that the function was being called.
5. You can use any LLM you want: GPT3.5/4 with function calling is okay. Or maybe you prefer local phi-2 with custom function calling implementation, this is also fine. Up to you.
6. Chatbot returns http response in JSON format with generated LLM answer.
7. Keep it simple: conversation history, streaming or UI are not needed. You also don’t need to deploy it.
8. Record a screencast demonstrating working service: request/response + function call output message. That’s it.
9. Push source code and recorded video to GitHub.

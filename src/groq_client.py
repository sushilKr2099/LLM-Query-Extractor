from groq import Groq

class GroqClient:
    def __init__(self, api_key):
        self.client = Groq(api_key="your_api_key_here")

    def call_llm_api(self, query):
        try:
            response = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": query}],
                temperature=1,
                max_tokens=1024,
                top_p=1,
                stream=False,
                stop=None,
            )
            if response and hasattr(response, 'choices'):
                completion = response.choices[0].message.content if response.choices else ''
                return {"response": completion}
            else:
                return {"response": "Unexpected response structure: No 'choices' field in response"}
        
        except Exception as e:
            return {"response": f"Error calling API: {str(e)}"}

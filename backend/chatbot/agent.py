from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

# Initialize Ollama LLM (Ensure Ollama is running locally with the mistral model pulled)
# To run Ollama: ollama run mistral
llm = OllamaLLM(model="mistral", base_url="http://localhost:11434")

prompt_template = PromptTemplate(
    input_variables=["context", "user_input"],
    template="""You are a helpful and empathetic academic counselor AI.
You have the following context about the student:
{context}

The student says: "{user_input}"

Provide a supportive, helpful, and concise response addressing their concerns. Do not judge them.
Response:"""
)

def get_chat_response(user_input: str, context: str) -> str:
    try:
        # Create prompt
        prompt = prompt_template.format(context=context, user_input=user_input)
        
        # Call local LLM
        response = llm.invoke(prompt)
        return response.strip()
    except Exception as e:
        print(f"Error calling Ollama: {e}")
        raise ValueError("Ollama unavailable")

import google.generativeai as genai
import os

# Configure the Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyBW4PV146YCV9u6tVXJJ-FJ1rC79N8q8Hc")
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

SYSTEM_PROMPT = """You are a helpful, empathetic, and supportive academic counselor AI assistant integrated into a student dropout prediction dashboard.

Your role is to:
1. Help teachers and counselors understand student risk factors
2. Suggest personalized intervention strategies to prevent dropout
3. Answer questions about student performance, attendance, and academic health
4. Provide motivational and practical advice

IMPORTANT LANGUAGE INSTRUCTION:
- Detect the language of the user's message and ALWAYS respond in that SAME language.
- If the user writes in Hindi, respond fully in Hindi (Devanagari script).
- If the user writes in Hinglish (Hindi-English mix), respond in Hinglish.
- If the user writes in Spanish, respond in Spanish.
- If the user writes in French, respond in French.
- If the user writes in Tamil, Telugu, Bengali, Marathi, Gujarati, or any other language, respond in that language.
- If the user writes in English, respond in English.
- Never switch languages unless the user explicitly asks you to.

Be concise, warm, professional, and non-judgmental. Focus on actionable advice."""


def get_chat_response(user_input: str, context: str, language: str = "auto") -> str:
    """
    Generate a multilingual chat response using Google Gemini API.
    
    Args:
        user_input: The message from the user/teacher
        context: Student context information
        language: Language hint ('auto' to detect from message, or explicit language name)
    
    Returns:
        AI response string
    """
    try:
        # Build language instruction
        if language and language != "auto":
            lang_instruction = f"\nIMPORTANT: The user has selected '{language}' as their preferred language. Respond ONLY in {language}, regardless of the language of the user's message."
        else:
            lang_instruction = "\nDetect the language of the user's message and respond in the SAME language."

        # Compose the full prompt
        full_prompt = f"""{SYSTEM_PROMPT}{lang_instruction}

Student Context:
{context}

Teacher/Counselor's Message: "{user_input}"

Please provide a helpful, empathetic, and actionable response. If suggesting interventions, make them specific to the student's situation described in the context."""

        response = model.generate_content(full_prompt)
        
        if response and response.text:
            return response.text.strip()
        else:
            return "I'm sorry, I couldn't generate a response. Please try again."
            
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        error_msg = str(e)
        if "API_KEY" in error_msg.upper() or "PERMISSION" in error_msg.upper():
            raise ValueError("Gemini API key is invalid or has insufficient permissions.")
        elif "QUOTA" in error_msg.upper() or "RATE" in error_msg.upper():
            raise ValueError("Gemini API quota exceeded. Please try again later.")
        else:
            raise ValueError(f"Gemini API error: {error_msg}")

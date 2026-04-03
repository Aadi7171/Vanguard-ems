import google.generativeai as genai
import os

# Set your API key in env or replace string here.
API_KEY = os.getenv("GEMINI_API_KEY", "")
if API_KEY:
    genai.configure(api_key=API_KEY)

def verify_unmapped_obstacle(image_path: str):
    """
    Calls Google Gemini to verify what an unmapped obstacle is (e.g., protest, street vendor).
    """
    if not API_KEY:
        return {"error": "API key not set", "prediction": "Mocked Protest Detected (Missing API Key)"}
        
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        sample_file = genai.upload_file(path=image_path)
        
        prompt = "This is a snapshot from an emergency route camera. Are there any physical roadblocks like a protest, street vendors, or construction blocking the road? Respond with YES or NO and a brief 1-sentence reason."
        
        response = model.generate_content([sample_file, prompt])
        return {"prediction": response.text}
        
    except Exception as e:
        return {"error": str(e)}

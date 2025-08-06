from config import get_gemini_model

class ItemAgent:
    def __init__(self):
        self.model = get_gemini_model()

    def reward(self):
        prompt = "The player finds a magical item after exploring. Describe the item and its powers."
        response = self.model.generate_content(prompt)
        return response.text

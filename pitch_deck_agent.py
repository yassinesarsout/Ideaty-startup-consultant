import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompt_utils import create_pitch_prompt
from utils import config_gemini, generate_text

load_dotenv()
gemini_client = config_gemini()

class PitchDeckAgent:
    def __init__(self, business_plan_agent):
        self.business_plan_agent = business_plan_agent

    def request_business_plan(self, idea):
        return self.business_plan_agent.generate_business_plan(idea)

    def generate_pitch_deck(self, idea):
        print("🎯 Requesting business plan...")
        plan = self.request_business_plan(idea)
        print("✅ Business plan received. Generating pitch deck...")

        prompt = create_pitch_prompt(plan)
        response = generate_text(gemini_client, prompt)
        return response

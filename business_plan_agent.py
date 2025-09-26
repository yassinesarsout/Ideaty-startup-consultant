# business_plan_agent.py

import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
from tools.market_analyst import analyze_market
from prompts2 import create_prompt
from google import genai

load_dotenv()

# ---------- Gemini Setup ----------
def config_gemeni():
    return genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_text(client, prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

# ---------- Agent 1: Business Idea Generator ----------
def generate_business_ideas(domain):
    prompt = create_prompt(domain)
    client = config_gemeni()
    response = generate_text(client, prompt)
    return response

# ---------- Agent 2: Market Research Agent ----------
AgentState = dict

def research_state(state: AgentState) -> AgentState:
    business_idea = state.get("business_idea", "")
    analysis = analyze_market(business_idea)
    state["market_analysis"] = analysis
    return state

def report_state(state: AgentState) -> AgentState:
    client = config_gemeni()
    analysis = state["market_analysis"]

    prompt = f"""
You are a market research analyst.

Summarize the following market analysis into a concise business intelligence report:

Business Idea: {analysis['business_idea']}
Market Size: {analysis['market_size']}
Competition: {analysis['competition']}
Growth Potential: {analysis['growth_potential']}
Challenges: {analysis['challenges']}
"""
    summary = generate_text(client, prompt)
    state["summary_report"] = summary
    return state

def create_market_research_agent():
    graph = StateGraph(AgentState)
    graph.add_node("research", research_state)
    graph.add_node("report", report_state)
    graph.set_entry_point("research")
    graph.add_edge("research", "report")
    graph.add_edge("report", END)
    return graph.compile()

# ---------- Agent 3: Business Plan Generator ----------
def generate_business_plan(business_idea, market_summary):
    client = config_gemeni()
    prompt = f"""
You are a startup consultant. Create a full business plan for the idea: "{business_idea}".

Use this market research summary:
{market_summary}

Include:
- Executive Summary
- Product Description
- Market Analysis
- Competitive Advantage
- Marketing Strategy
- Financial Plan
- Conclusion
"""
    return generate_text(client, prompt)

# ---------- Agent 4: Pitch Deck Generator ----------
def generate_pitch_deck(business_idea):
    print("🔍 Running market research...")
    market_agent = create_market_research_agent()
    state = {"business_idea": business_idea}
    output = market_agent.invoke(state)
    market_summary = output["summary_report"]

    print("📄 Generating business plan...")
    business_plan = generate_business_plan(business_idea, market_summary)

    print("🎯 Generating pitch deck...")
    client = config_gemeni()
    prompt = f"""
You are a startup coach and pitch deck writer.

Based on the business plan below, generate a pitch deck with 10 slides.
Each slide must have:
- A clear title
- 3 to 5 bullet points

### Business Plan:
{business_plan}

### Format:
Slide 1: Title
- Bullet 1
- Bullet 2

Slide 2: Problem
- Bullet 1
...

Slide 10: Closing
- Bullet 1
"""
    return generate_text(client, prompt)

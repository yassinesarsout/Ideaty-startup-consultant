# AI Business Builder & Pitch Deck Generator

This project is an AI-powered application designed to assist users in generating business ideas and creating comprehensive pitch decks. It leverages Google's Gemini API for natural language generation and `langgraph` for orchestrating multi-agent workflows, specifically for market research.

## Features

- **Business Idea Generation**: Suggests innovative business ideas based on a user-specified domain.
- **Market Research Simulation**: Conducts a simulated market analysis for a chosen business idea, providing insights into market size, competition, growth potential, and challenges.
- **Business Plan Generation**: Creates a detailed business plan incorporating executive summary, product description, market analysis, competitive advantage, marketing strategy, and financial plan.
- **Pitch Deck Generation**: Produces a 10-slide pitch deck in Markdown format, summarizing the business plan for presentation.

## How it Works

The application follows a sequential workflow:

1.  **Domain Input**: The user provides a domain of interest (e.g., health, education, energy).
2.  **Idea Generation**: The system generates several business ideas relevant to the specified domain, including business name, short description, target audience, and potential revenue streams.
3.  **Idea Selection**: The user selects one of the generated business ideas.
4.  **Market Research**: A multi-agent system (orchestrated by `langgraph`) simulates market research for the chosen idea. This involves:
    *   **Research State**: Gathers simulated market data (market size, competition, growth potential, challenges).
    *   **Report State**: Summarizes the market analysis into a concise business intelligence report.
5.  **Business Plan Creation**: Based on the chosen business idea and the market research summary, a comprehensive business plan is generated.
6.  **Pitch Deck Creation**: Finally, a 10-slide pitch deck is generated from the detailed business plan, formatted with titles and bullet points for each slide.
7.  **Output**: The generated pitch deck is saved as `pitch_deck.md` in the project directory.

## Project Structure

```
. 
├── main.py
├── business_plan_agent.py
├── pitch_deck.md
├── prompt_utils.py
├── prompts2.py
├── pyvenv.cfg
├── requirements.txt
├── utils.py
└── tools/
    ├── __pycache__/
    └── market_analyst.py
```

-   **`main.py`**: The main entry point of the application. It handles user interaction, calls the business plan agent, and saves the final pitch deck.
-   **`business_plan_agent.py`**: Contains the core logic for generating business ideas, orchestrating the market research agent, generating the business plan, and creating the pitch deck. It integrates with the Gemini API and `langgraph`.
-   **`tools/market_analyst.py`**: A simulated tool that provides market analysis data for a given business idea. In a real-world scenario, this would involve actual data retrieval and analysis.
-   **`prompt_utils.py`**: Contains utility functions for creating specific prompts, such as the pitch deck prompt.
-   **`prompts2.py`**: Defines the prompt template used for generating initial business ideas based on a domain.
-   **`requirements.txt`**: Lists all Python dependencies required to run the project.
-   **`pitch_deck.md`**: The output file where the generated pitch deck is saved.

## Setup and Installation

To run this project, you will need Python 3.x and a Google Gemini API key.

1.  **Clone the repository (if applicable) or navigate to the project directory.**

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your Gemini API Key:**
    Create a `.env` file in the root directory of the project and add your Gemini API key:
    ```
    GEMINI_API_KEY='YOUR_GEMINI_API_KEY'
    ```
    You can obtain a Gemini API key from the [Google AI Studio](https://aistudio.google.com/app/apikey).

4.  **Run the application:**
    ```bash
    python main.py
    ```

## Dependencies

The project relies on the following key Python libraries:

-   `google-genai`: For interacting with the Google Gemini API.
-   `langgraph`: For building stateful, multi-actor applications with LLMs.
-   `python-dotenv`: For loading environment variables (like the Gemini API key).

(See `requirements.txt` for a complete list of dependencies.)

## Usage

Upon running `main.py`, the application will guide you through the process:

1.  Enter a domain of interest.
2.  Review the suggested business ideas.
3.  Enter your chosen business idea.
4.  The application will then proceed to run market research, generate a business plan, and finally create a pitch deck.
5.  The pitch deck will be displayed in the console and saved to `pitch_deck.md`.

## Example Output

```markdown
# Final Pitch Deck:

Slide 1: Introduction
- Welcome to [Your Business Name]
- Revolutionizing [Industry/Problem]
- Our Vision: [Brief Vision Statement]

Slide 2: Problem
- The current market faces [Problem 1]
- Consumers struggle with [Problem 2]
- Existing solutions are [Limitations of current solutions]
...
```

## Author

Manus AI


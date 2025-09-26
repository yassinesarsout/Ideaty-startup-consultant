def create_pitch_prompt(business_plan):
    return f"""
You are an expert startup advisor and pitch deck designer.

Based on the business plan below, generate a 10-slide pitch deck in **text format**.
Each slide should include:
- A slide title
- 3-5 bullet points

### Business Plan:
{business_plan}

### Format:
Slide 1: Title
- Bullet 1
- Bullet 2

Slide 2: Problem
- ...
...
Slide 10: Closing
- ...
"""

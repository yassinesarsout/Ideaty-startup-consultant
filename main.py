# main.py

from business_plan_agent import (
    generate_business_ideas,
    generate_pitch_deck
)

def main():
    print("💡 AI Business Builder & Pitch Deck Generator\n")
    domain = input("🌐 Enter a domain you're interested in (e.g., health, education, energy): ")

    print("\n🤖 Generating business ideas...")
    ideas = generate_business_ideas(domain)
    print("\n✨ Suggested Business Ideas:\n")
    print(ideas)

    business_idea = input("\n✍️ Enter your chosen business idea (in one sentence): ")

    pitch = generate_pitch_deck(business_idea)

    print("\n📊 Final Pitch Deck:\n")
    print(pitch)

    with open("pitch_deck.md", "w", encoding="utf-8") as f:
        f.write(pitch)
        print("\n💾 Pitch deck saved to pitch_deck.md")

if __name__ == "__main__":
    main()

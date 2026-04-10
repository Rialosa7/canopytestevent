import random

def generate_tasks(goal):
    goal = goal.lower()
    tasks = []

    # AI-like understanding
    if any(word in goal for word in ["learn", "study", "improve"]):
        tasks += [
            "Research the fundamentals of the topic",
            "Watch beginner-friendly tutorials",
            "Practice consistently every day"
        ]

    if any(word in goal for word in ["money", "earn", "income"]):
        tasks += [
            "Identify possible income sources",
            "Start with small, manageable steps",
            "Track and optimize your progress"
        ]

    if any(word in goal for word in ["trading", "crypto", "invest"]):
        tasks += [
            "Understand market fundamentals",
            "Use demo accounts before real trading",
            "Analyze charts and trends daily"
        ]

    if not tasks:
        tasks = [
            "Break your goal into smaller tasks",
            "Create a daily schedule",
            "Stay consistent and evaluate progress"
        ]

    return list(dict.fromkeys(tasks))  # remove duplicates


def check_scam(url):
    score = 0
    reasons = []

    suspicious_keywords = ["free", "win", "bonus", "guarantee", "fast", "profit"]

    for word in suspicious_keywords:
        if word in url.lower():
            score += 1
            reasons.append(f"Suspicious keyword: {word}")

    if not url.startswith("https"):
        score += 1
        reasons.append("No HTTPS (not secure)")

    if len(url) > 30:
        score += 1
        reasons.append("URL looks unusually long")

    # AI-like decision
    if score >= 2:
        status = "⚠️ HIGH RISK: Potential Scam"
    elif score == 1:
        status = "⚠️ MEDIUM RISK: Be Careful"
    else:
        status = "✅ LOW RISK: Looks Safe"

    return status, reasons


def ai_tip():
    tips = [
        "Consistency beats intensity.",
        "Small steps lead to big results.",
        "Focus on progress, not perfection.",
        "Learn, apply, and improve daily.",
        "Discipline is the real key to success."
    ]
    return random.choice(tips)


def main():
    print("\n=== 🤖 SmartGuard AI ===")
    print("1. Generate AI Tasks")
    print("2. Scan URL for Scam Risk")

    choice = input("\nChoose option (1/2): ")

    if choice == "1":
        goal = input("\nEnter your goal: ")
        tasks = generate_tasks(goal)

        print("\n🎯 AI Generated Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

        print("\n💡 AI Tip:", ai_tip())

    elif choice == "2":
        url = input("\nEnter URL: ")
        status, reasons = check_scam(url)

        print("\n🔍 Scan Result:")
        print(status)

        if reasons:
            print("\nReasons:")
            for r in reasons:
                print("-", r)

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
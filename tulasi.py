client = genai.Client(api_key=getpass("Enter Gemini API key: "))

print("Learning Path Generator Agent")

while True:
    topic = input("\nEnter a topic to learn (or exit): ").strip()
    if topic.lower() == "exit":
        print("Goodbye!")
        break
    if not topic:
        print("Please enter a topic.")
        continue

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=f"""Create a beginner-friendly learning path for: {topic}
Include prerequisites, 5 learning steps, practical projects,
free learning resources to search for, and a weekly study plan."""
        )
        print("\nYour Learning Path:\n", response.text or "No response received.")
    except Exception as e:
        if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
            print("Gemini quota exceeded. Check your API usage and limits.")
        elif "API_KEY_INVALID" in str(e) or "API key not valid" in str(e):
            print("Invalid API key. Check your Gemini API key.")
        else:
            print("Error:", e)
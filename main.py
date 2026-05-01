def main():
    print("PyAgent v0.1 — Your AI Agent")
    history = []

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            break
        history.append({"role": "user", "content": user_input})
        print(f"Agent: Got your message. AI coming soon.")


if __name__ == "__main__":
    main()
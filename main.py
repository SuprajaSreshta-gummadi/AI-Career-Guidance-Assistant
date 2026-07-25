from chatbot import CareerGuidanceChatbot


def main():

    print("=" * 60)
    print("🤖 AI CAREER GUIDANCE ASSISTANT")
    print("=" * 60)

    print("\nHello! I can help you with:")
    print("• Career exploration")
    print("• Required skills")
    print("• Career recommendations")
    print("• Industry trends")
    print("• Salary insights")
    print("• Interview preparation")
    print("• Career goal setting")

    print("\nType 'exit' or 'quit' to close the assistant.\n")

    # Create chatbot object
    chatbot = CareerGuidanceChatbot()

    while True:

        user_message = input("You: ")

        # Exit the program
        if user_message.lower() in ["exit", "quit", "bye"]:

            print(
                "\nAssistant: Thank you for using the "
                "AI Career Guidance Assistant!"
            )

            break

        # Avoid empty input
        if user_message.strip() == "":

            print("Assistant: Please enter a question.")

            continue

        # Get chatbot response
        response = chatbot.get_response(user_message)

        print(f"\nAssistant: {response}\n")


if __name__ == "__main__":
    main()
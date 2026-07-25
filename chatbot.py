import json
import pickle
import random


class CareerGuidanceChatbot:

    def __init__(self):

        # Load trained machine learning model
        with open("intent_model.pkl", "rb") as file:
            self.model = pickle.load(file)

        # Load TF-IDF vectorizer
        with open("vectorizer.pkl", "rb") as file:
            self.vectorizer = pickle.load(file)

        # Load intents
        with open("intents.json", "r") as file:
            self.intents = json.load(file)

        # Load career information
        with open("careers.json", "r") as file:
            self.careers = json.load(file)

    def predict_intent(self, user_message):

        # Convert user message into numerical format
        message_vector = self.vectorizer.transform([user_message])

        # Predict intent
        predicted_intent = self.model.predict(message_vector)[0]

        return predicted_intent

    def get_response(self, user_message):

        # Predict user intent
        intent = self.predict_intent(user_message)

        # Career information queries
        for career_name, career_info in self.careers.items():

            if career_name.lower() in user_message.lower():

                if "skill" in user_message.lower():
                    return (
                        f"\nSkills required for {career_name}:\n"
                        + "\n".join(
                            f"- {skill}"
                            for skill in career_info["skills"]
                        )
                    )

                elif (
                    "career" in user_message.lower()
                    or "about" in user_message.lower()
                    or "what is" in user_message.lower()
                ):
                    return (
                        f"\n{career_name}\n"
                        f"{career_info['description']}\n"
                        f"\nCareer Path:\n"
                        + "\n".join(
                            f"- {step}"
                            for step in career_info["career_path"]
                        )
                    )

                elif "trend" in user_message.lower():
                    return (
                        f"\nIndustry Trend for {career_name}:\n"
                        f"{career_info['industry_trend']}"
                    )

        # Career recommendation based on skills
        if intent == "career_recommendation":

            user_message = user_message.lower()

            recommendations = []

            for career_name, career_info in self.careers.items():

                matching_skills = []

                for skill in career_info["skills"]:

                    if skill.lower() in user_message:
                        matching_skills.append(skill)

                if matching_skills:
                    recommendations.append(
                        (career_name, matching_skills)
                    )

            if recommendations:

                response = "\nBased on your skills, you may consider:\n"

                for career, skills in recommendations:

                    response += (
                        f"\n{career}"
                        f"\nMatching skills: "
                        f"{', '.join(skills)}\n"
                    )

                return response

            return (
                "\nI can recommend a career based on your skills.\n"
                "Please mention skills such as Python, SQL, "
                "Machine Learning, or Statistics."
            )

        # Find response for predicted intent
        for intent_data in self.intents["intents"]:

            if intent_data["tag"] == intent:

                return random.choice(
                    intent_data["responses"]
                )

        return (
            "Sorry, I could not understand your question. "
            "Please try asking about careers, skills, "
            "industry trends, or interview preparation."
        )
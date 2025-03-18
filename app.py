import streamlit as st
import datetime
import google.generativeai as genai

# Configure API Key
API_KEY = "AIzaSyDqG_n-YApNnD5gNySZH9SyiJXW6zeStSU"  # Replace with your actual API key
genai.configure(api_key=API_KEY)

def get_ai_response(prompt, fallback_message):
    try:
        model = genai.GenerativeModel("gemini-2-flash")
        response = model.generate_content(prompt)
        return response.text.strip() if hasattr(response, "text") and response.text.strip() else fallback_message
    except Exception as e:
        return f"⚠️ AI Error: {str(e)}\n{fallback_message}"

def get_event_recommendation():
    today = datetime.datetime.today().strftime("%B %d")
    prompt = f"""
    Today is {today}. Identify any special occasion (e.g., Valentine's Day, Christmas, Thanksgiving) and recommend:
    - A restaurant theme
    - Ideal cuisine (Veg, Non-Veg, Vegan)
    - Drinks (Soft Drinks, Mocktails, Cocktails, Beer)
    - A dessert pairing
    - A discount strategy based on demand trends
    - A short marketing slogan
    - AI-generated Instagram caption and trending hashtags
    - AI-optimized lighting and music
    - AI-driven sustainability strategies
    - AI-suggested seating arrangement
    - AI-predicted customer sentiment & demand
    - AI-enhanced pricing strategy for discounts
    - AI-recommended event entertainment options
    - AI-suggested staff dress code for the theme
    - AI-driven social media engagement tips
    """
    return get_ai_response(prompt, "⚠️ AI response unavailable. Please try again later.")

def get_reservation_recommendation(occasion, people, cuisine_type, drink_type, budget):
    if not all([occasion, people, cuisine_type, drink_type, budget]):
        return "⚠️ Please fill in all fields before generating a recommendation."
    
    prompt = f"""
    A restaurant reservation has been made with:
    - Occasion: {occasion}
    - Guests: {people}
    - Cuisine: {cuisine_type}
    - Drinks: {drink_type}
    - Budget: {budget}
    
    Recommend:
    - A suitable event theme
    - Decoration style
    - Custom menu (Dishes, Drinks, Dessert Combo)
    - Discount offer
    - A unique marketing slogan
    - Instagram caption & trending hashtags
    - AI-powered seating optimization
    - Allergy-friendly & diet-specific recommendations
    - Sustainable dining strategies
    - AI-generated personalized thank-you message
    - AI-recommended music playlist
    - AI-optimized table arrangements for group dynamics
    - AI-driven guest experience enhancements
    """
    return get_ai_response(prompt, "⚠️ AI response unavailable. Please try again later.")

st.set_page_config(page_title="AI-Powered Restaurant Manager", layout="wide")
st.title("🍽️ AI-Powered Smart Restaurant Management")

st.header("📅 AI-Powered Event Recommendation for Today")
if st.button("Generate Event Recommendation"):
    st.text_area("Event Recommendation:", get_event_recommendation(), height=300)

st.header("🎊 Custom AI-Powered Event Recommendation")

occasion = st.text_input("🎉 Occasion (e.g., Birthday, Anniversary, Business Meeting)")
people = st.number_input("👥 Number of Guests", min_value=1, value=2)
cuisine_type = st.selectbox("🍽 Preferred Cuisine", ["Veg", "Non-Veg", "Vegan"])
drink_type = st.selectbox("🍹 Preferred Drink", ["Soft Drinks", "Mocktails", "Cocktails", "Beer"])
budget = st.text_input("💰 Budget Range")

if st.button("Generate Reservation Recommendation"):
    st.text_area("Reservation Recommendation:", get_reservation_recommendation(occasion, people, cuisine_type, drink_type, budget), height=300)

st.write("\n🚀 Powered by Gemini AI")

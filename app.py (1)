import streamlit as st
import google.generativeai as genai
import firebase_admin
from firebase_admin import credentials, firestore
from PIL import Image
import io

# ✅ Configure API Key securely
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
else:
    st.error("⚠️ API Key is missing. Go to Streamlit Cloud → Settings → Secrets and add your API key.")
    st.stop()

# ✅ Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_credentials.json")
    firebase_admin.initialize_app(cred)
db = firestore.client()

# ✅ AI Response Generator
def get_ai_response(prompt, fallback_message="⚠️ AI response unavailable. Please try again later."):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)
        return response.text.strip() if hasattr(response, "text") and response.text.strip() else fallback_message
    except Exception as e:
        return f"⚠️ AI Error: {str(e)}\n{fallback_message}"

# ✅ AI Image Generator
def generate_ai_image(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-vision")
        image_response = model.generate_content(prompt)
        if hasattr(image_response, "image"):
            return Image.open(io.BytesIO(image_response.image))
    except Exception as e:
        st.error(f"⚠️ Image Generation Error: {str(e)}")
        return None

# ✅ AI-Powered Features
def get_pricing_strategy(dish_name):
    prompt = f"Generate an optimal pricing strategy for the dish {dish_name}, considering demand, seasonality, and competitor pricing."
    return get_ai_response(prompt)

def get_demand_forecast(meal_type):
    prompt = f"Predict the demand for {meal_type} based on trends, time of day, and customer preferences."
    return get_ai_response(prompt)

def track_inventory(ingredient):
    prompt = f"Analyze the stock level and suggest restocking strategy for {ingredient}."
    return get_ai_response(prompt)

def customer_preference_analysis():
    prompt = "Analyze recent customer reviews and order trends to identify popular dishes and improvement areas."
    return get_ai_response(prompt)

def customer_sentiment_analysis():
    prompt = "Perform sentiment analysis on recent customer feedback and provide insights."
    return get_ai_response(prompt)

def ai_chatbot_response(user_input):
    prompt = f"Customer inquiry: {user_input}\nProvide a helpful and friendly AI response."
    return get_ai_response(prompt)

# ✅ Streamlit UI Configuration
st.set_page_config(page_title="Smart Restaurant Menu Management App", layout="wide")
st.title("🍽️ Smart Restaurant Management with Gemini 1.5 Pro")
st.write("🚀 Manage events, recommend menus, optimize leftovers, forecast demand, track inventory, analyze customer feedback, and provide AI chatbot support using GenAI.")

# 🎯 **Event Manager**
st.header("🎉 Event Manager")
occasion = st.text_input("🎊 Occasion")
people = st.number_input("👥 Number of Guests", min_value=1, value=2)
cuisine_type = st.selectbox("🍱 Cuisine Preference", ["Veg", "Non-Veg", "Vegan", "Mixed"])
budget = st.text_input("💰 Budget Range (e.g., $100-$300)")

if st.button("✨ Generate Event Plan"):
    if not all([occasion, people, cuisine_type, budget]):
        st.error("⚠️ Please fill in all fields before generating a recommendation.")
    else:
        prompt = f"Create an event plan for {occasion} with {people} guests, cuisine preference: {cuisine_type}, budget: {budget}."
        event_plan = get_ai_response(prompt)
        st.text_area("📋 Event Plan:", event_plan, height=300)
        db.collection("events").add({"occasion": occasion, "people": people, "cuisine": cuisine_type, "budget": budget, "plan": event_plan})

# 🍽️ **Food Menu Recommendation**
st.header("🍴 Food Menu Recommendation")
meal_type = st.selectbox("🍔 Meal Type", ["Breakfast", "Lunch", "Dinner", "Snack"])
dietary_pref = st.selectbox("🥗 Dietary Preference", ["Vegetarian", "Non-Vegetarian", "Vegan", "Keto", "Gluten-Free"])

if st.button("🔍 Recommend Food Menu"):
    if not all([meal_type, dietary_pref]):
        st.error("⚠️ Please fill in all fields before generating a recommendation.")
    else:
        prompt = f"Generate a food menu for {meal_type} with {dietary_pref} preference."
        menu_recommendation = get_ai_response(prompt)
        st.text_area("🍽️ Menu Recommendation:", menu_recommendation, height=300)
        db.collection("menus").add({"meal_type": meal_type, "dietary_pref": dietary_pref, "menu": menu_recommendation})
        image = generate_ai_image(f"Realistic image of {meal_type} menu with {dietary_pref} dishes.")
        if image:
            st.image(image, caption="🍽️ AI-Generated Menu Image")

# 🥡 **Leftover Management**
st.header("♻️ Leftover Management")
leftover_type = st.selectbox("🥩 Leftover Type", ["Meat", "Vegetables", "Dairy", "Grains", "Fruits"])
quantity = st.number_input("📦 Quantity (kg)", min_value=0.1, value=1.0)

if st.button("♻️ Optimize Leftover Usage"):
    if not all([leftover_type, quantity]):
        st.error("⚠️ Please fill in all fields before generating a recommendation.")
    else:
        prompt = f"Suggestions for using {quantity} kg of {leftover_type} leftovers."
        leftover_plan = get_ai_response(prompt)
        st.text_area("♻️ Leftover Optimization:", leftover_plan, height=300)
        db.collection("leftovers").add({"type": leftover_type, "quantity": quantity, "plan": leftover_plan})

# 💬 **AI Chatbot Support**
st.header("🤖 AI Chatbot Support")
user_query = st.text_input("💬 Ask a question about restaurant management:")
if st.button("📩 Get AI Response"):
    if user_query:
        chatbot_reply = ai_chatbot_response(user_query)
        st.text_area("🤖 AI Chatbot Response:", chatbot_reply, height=150)
    else:
        st.error("⚠️ Please enter a question.")

# ✅ Footer
st.write("🚀 Powered by Gemini 1.5 Pro & Firebase")

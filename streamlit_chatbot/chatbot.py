import streamlit as st
import pandas as pd

# Sample food database
FOOD_DATA = {
    "Apple (1 medium)": 95,
    "Banana (1 medium)": 105,
    "Chicken Breast (100g)": 165,
    "Rice (1 cup cooked)": 200,
    "Egg (1 large)": 78,
    "Broccoli (1 cup)": 55,
    "Salmon (100g)": 208,
    "Bread (1 slice)": 80,
    "Milk (1 cup)": 103,
    "Oatmeal (1 cup)": 150,
    "Cheese (1 slice)": 113,
    "Peanut Butter (1 tbsp)": 94,
    "Potato (1 medium)": 110,
    "Yogurt (1 cup)": 150,
    "Nasi Lemak(sambal, kacang)": 650,
    "Roti Canai (1 piece with dhal)": 350,
    "Char Kway Teow (1 plate)": 750,
    "Laksa (Penang Asam Laksa, 1 bowl)": 450,
    "Mee Goreng Mamak (1 plate)": 680,
    "Nasi Goreng Kampung (1 plate)": 550,
    "Satay (3 sticks + peanut sauce)": 300,
    "Teh Tarik (1 cup)": 130,
    "Kuih Lapis (1 piece)": 180,
    "Chicken Curry (1 serving)": 350,
    "Roti Jala with Chicken Curry": 480,
    "Pisang Goreng (2 pieces)": 270,
    "Cendol (1 bowl)": 380,
    "Ais Kacang (ABC, 1 bowl)": 400,
    "Nasi Kerabu (with fish and sides)": 570,
    "Nasi Kandar (with curry, egg, and sides)": 900,
    "Maggi Goreng (1 plate)": 500,
    "Mee Rebus (1 bowl)": 430,
    "Lontong (1 serving)": 450,
    "Kaya Toast (2 slices)": 320,
    "Milo (1 cup, sweetened)": 160,
    "Sambal Udang (prawns in chili paste)": 300,
    "Ikan Bakar (grilled fish)": 250,
    "Sayur Lodeh (vegetable curry)": 200,
    "Keropok Lekor (3 pieces)": 240,
    "Otak-otak (2 pieces)": 180,
    "Rendang Daging (1 serving)": 450,
    "Pulut Panggang (1 roll)": 220,
    "Kuih Seri Muka (1 piece)": 200,
    "Lemang with Rendang (1 serving)": 600,
    "Popiah Basah (1 roll)": 150,
    "Chicken Rice": 730,
}

# For storing user food input
if "food_log" not in st.session_state:
    st.session_state.food_log = []

if "goal" not in st.session_state:
    st.session_state.goal = 2000

if "gender" not in st.session_state:
    st.session_state.gender = "Other"

if "activity" not in st.session_state:
    st.session_state.activity = "Sedentary"

# --- Sidebar for user settings ---
with st.sidebar:
    st.header("User Profile")
    st.session_state.gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    st.session_state.activity = st.selectbox("Physical Activity Level", ["Sedentary", "Moderate", "Active"])
    st.session_state.goal = st.slider("Set your daily caloric goal", 1200, 4000, 2000)

# --- Tabs ---
tab1, tab2, tab3 = st.tabs(["📊 Calorie Tracker", "🥗 Meal Plan Suggestion", "📈 Summary"])

# --- Tab 1: Calorie Tracker ---
with tab1:
    st.title("Calorie Tracker")

    food = st.selectbox("Select Food", list(FOOD_DATA.keys()))
    quantity = st.number_input("Quantity", 1, 10, 1)
    if st.button("Add"):
        st.session_state.food_log.append((food, quantity, FOOD_DATA[food] * quantity))
        st.success(f"Added {quantity} x {food}")

    st.subheader("Food Log")
    if st.session_state.food_log:
        df = pd.DataFrame(st.session_state.food_log, columns=["Food", "Quantity", "Calories"])
        st.dataframe(df)
        total_calories = df["Calories"].sum()
        st.metric("Total Calories Consumed", f"{total_calories} kcal")
    else:
        st.info("No food logged yet.")

# --- Tab 2: Meal Plan Suggestion ---
with tab2:
    st.title("Meal Plan Suggestion")

    st.markdown("Here's a sample meal plan based on your goal and activity level:")
    activity_factor = {"Sedentary": 1.0, "Moderate": 1.2, "Active": 1.4}
    recommended_intake = int(st.session_state.goal * activity_factor[st.session_state.activity])

    st.metric("Adjusted Caloric Need", f"{recommended_intake} kcal")

    st.write("🔹 **Breakfast**: Oatmeal with banana and milk (~400 kcal)")
    st.write("🔹 **Lunch**: Grilled chicken with rice and broccoli (~700 kcal)")
    st.write("🔹 **Snack**: Apple and peanut butter (~250 kcal)")
    st.write("🔹 **Dinner**: Salmon with potato and veggies (~600 kcal)")
    st.write("🔹 **Yogurt dessert** (~200 kcal)")

# --- Tab 3: Summary Page ---
with tab3:
    st.title("Daily Summary")

    if st.session_state.food_log:
        df = pd.DataFrame(st.session_state.food_log, columns=["Food", "Quantity", "Calories"])
        total_calories = df["Calories"].sum()
        goal = st.session_state.goal
        diff = total_calories - goal

        st.metric("Calories Consumed", f"{total_calories} kcal")
        st.metric("Daily Goal", f"{goal} kcal")
        st.metric("Difference", f"{diff:+} kcal")

        if diff < 0:
            st.success("You are under your goal. Great job!")
        elif diff == 0:
            st.info("You met your calorie goal perfectly!")
        else:
            st.warning("You exceeded your calorie goal.")
    else:
        st.info("No data to summarize yet.")

# Run with: streamlit run filename.py

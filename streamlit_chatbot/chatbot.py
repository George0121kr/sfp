import streamlit as st
import pandas as pd
import random

def generate_meal_plan(calorie_goal, food_data):
    # Distribute calorie target across meals
    meal_targets = {
        "Breakfast": int(calorie_goal * 0.25),
        "Lunch": int(calorie_goal * 0.45),
        "Dinner": int(calorie_goal * 0.30),
    }

    used_foods = set()  # ✅ Track all used items to avoid duplicates

    def pick_foods_for_meal(target, available_foods, used_foods):
        selected = []
        total = 0
        attempts = 0

        # Filter out already used foods
        foods = [(food, kcal) for food, kcal in available_foods.items() if food not in used_foods]
        random.shuffle(foods)

        while total < target and attempts < 1000 and foods:
            food, kcal = random.choice(foods)
            if total + kcal <= target:
                selected.append((food, 1, kcal))
                total += kcal
                used_foods.add(food)  # ✅ Mark as used
                foods.remove((food, kcal))  # Remove to prevent repeat
            attempts += 1

        return selected, total, used_foods

    # Generate meals
    meal_plan = {}
    for meal, target in meal_targets.items():
        items, total, used_foods = pick_foods_for_meal(target, food_data, used_foods)
        meal_plan[meal] = {"items": items, "total": total}

    return meal_plan

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
    "Chicken Rice (1 plate)": 730,
    "pasta (cabonara)": 250,
    "speghetti":220,
    "Mixed Rice ( 1 meat, 1 vege, 1 other)": 750,
    "Nasi Lemak (full plate)": 644,
    "Chicken Satay (10 sticks)": 365,
    "Beef Rendang (small portion)": 228,
    "Fish Head Curry": 288,
    "Nasi Briyani with mutton": 587,
    "Nasi Minyak + Beef Rendang": 664,
    "Nasi Kerabu (1 plate)": 360,
    "Nasi Campur (economy rice, 3 dishes)": 620,
    "Claypot Chicken Rice": 898,
    "Mee Goreng Mamak": 660,
    "Mee Rebus": 556,
    "Laksa Kari (Curry Laksa)": 586,
    "Penang Asam Laksa": 436,
    "Bak Kut Teh (1 bowl)": 348,
    "Roti Canai (plain)": 301,
    "Roti Telur & Dhal": 414,
    "Murtabak (1 piece)": 722,
    "Nasi Ayam (Hainanese chicken rice)": 600,
    "Mee Bandung Muar": 549,
    "Lor Mee": 383,
    "Pasembur (Indian rojak)": 752,
    "Rojak Buah": 443,
    "Char Kway Teow": 324,
    "Chicken Rice (Hainanese)": 600, 
    "Claypot Chicken Rice": 898,
    "Bak Kut Teh": 348, 
    "Century Egg Porridge": 423,
    "Mee Soup": 380,
    "Mee Hailam": 277,
    "Wanton Mee": 409,
    "Yong Tau Foo Soup (1 bowl)": 49,
    "Chapati": 100,
    "Thosai (dosa)": 80,
    "Chicken Curry (medium piece)": 195,
    "Tandoori Chicken (leg/thigh)": 300,
    "Sotong Sambal": 170,
    "Curry Puff (Karipap)": 130,
    "Kuih Seri Muka": 192,
    "Kuih Lapis": 90,
    "Kuih Koci": 92,
    "Kuih Keria": 99,
    "Kuih Apam Balik": 240,
    "Pisang Goreng (1 piece)": 120,
    "Cendol (1 bowl)": 199,
    "Ice Kacang (Ais Kacang)": 258,
    "Tai Foo Fah (tau foo far sweetened)": 144,
    "Agar‑agar (1 piece)": 37,
    "Popiah (1 piece)": 188,
    "Prawn Crackers (small packet)": 106,
     "Ambuyat (Sarawak/Sabah staple)": 842,
    "Kinilaw (fish salad, Filipino‑inspired)": 147,
    "Fish & Chips (local portion)": 848,
    "Beef Burger (regular)": 317,
    "Cheese Burger": 341,
    "Hot Dog (1 whole)": 225,
    "Spaghetti with Chicken & Mushroom": 444,
    "Thai Yam Khanom Chin (rice noodle salad)": 220,
    "Japanese Sushi (6 pieces mixed)": 250, 
    "Korean Bibimbap (vegetarian)": 500,   
    "Teh Tarik (1 cup)": 83,
    "Milo (sweetened, 1 cup)": 133,
    "Chinese Tea (1 Cup)": 0,
    "Air Bandung (rose milk, 1 glass)": 150,
    "Soft drink (1 can)": 120,
    "Coconut Water (1 fruit)": 110,
    "Fresh juice (sweetened, 1 glass)": 120,
    "One Half-Boiled Egg": 77,
    "Kaya Butter Bread toast": 330,
    "Barley water (1 Cup)": 45,
    "Chrysanthemum Tea (1 cup)": 35,
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

def calculate_recommended_calories(gender, activity_level):
    base_calorie = {
        "Male": 2500,
        "Female": 2000,
        "Other": 2200
    }.get(gender, 2200)

    activity_factor = {
        "Sedentary": 1.0,
        "Moderate": 1.2,
        "Active": 1.4
    }.get(activity_level, 1.0)

    return int(base_calorie * activity_factor)

# --- Sidebar for user settings ---
with st.sidebar:
    st.header("User Profile")
    st.session_state.gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    st.session_state.activity = st.selectbox("Physical Activity Level", ["Sedentary", "Moderate", "Active"])
    
    # Get recommended calories
    recommended = calculate_recommended_calories(st.session_state.gender, st.session_state.activity)
    
    st.session_state.goal = st.slider("Set your daily caloric goal", 1200, 4000, recommended)
    st.caption(f"Recommended based on your profile: **{recommended} kcal**")

# --- Tabs ---
tab1, tab2, tab3 = st.tabs(["📊 Calorie Tracker", "🥗 Meal Plan Suggestion", "📈 Summary"])

# --- Tab 1: Calorie Tracker ---
with tab1:
    st.title("Calorie Tracker")

    # Select meal type (Breakfast, Lunch, Dinner)
    meal_type = st.selectbox("Meal Type", ["Breakfast", "Lunch", "Dinner"])

    # Select food and quantity
    food = st.selectbox("Select Food", list(FOOD_DATA.keys()))
    quantity = st.number_input("Quantity", 1, 10, 1)

    # Layout: Add and Delete Buttons side by side
    col1, col2 = st.columns(2)
    with col1:
        if st.button("➕ Add"):
            st.session_state.food_log.append(
                {"Meal": meal_type, "Food": food, "Quantity": quantity, "Calories": FOOD_DATA[food] * quantity}
            )
            st.success(f"Added {quantity}x {food} to {meal_type}")

    with col2:
        if st.button("🗑️ Delete"):
            if st.session_state.food_log:
                deleted = st.session_state.food_log.pop()
                st.warning(f"Deleted: {deleted['Food']} ({deleted['Calories']} kcal)")
            else:
                st.info("No entries to delete.")

    # Show food log
    st.subheader("Food Log")
    if st.session_state.food_log:
        df = pd.DataFrame(st.session_state.food_log)
        st.dataframe(df)
        total_calories = df["Calories"].sum()
        st.metric("Total Calories Consumed", f"{total_calories} kcal")
    else:
        st.info("No food logged yet.")

# --- Tab 2: Meal Plan Suggestion ---
with tab2:
    st.title("Meal Plan Suggestion")

    goal = st.session_state.goal
    st.markdown(f"📌 Based on your target of **{goal} kcal/day**, here's a custom daily plan:")

    # ✅ Only run this when the user clicks the button
    regenerate = st.button("🔄 Regenerate Meal Plan")

    # Generate the plan
    if regenerate or "meal_plan" not in st.session_state:
        st.session_state.meal_plan = generate_meal_plan(goal, FOOD_DATA)

    plan = st.session_state.meal_plan

    # Display each meal
    for meal_name, meal_data in plan.items():
        st.subheader(f"🍽 {meal_name} — {meal_data['total']} kcal")
        for food_name, qty, kcal in meal_data["items"]:
            st.markdown(f"- {qty}x {food_name} ({kcal} kcal)")

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

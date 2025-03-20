import streamlit as st

# App title
st.title("🎭 Multi-Service Management System")

# Sidebar for service selection
service = st.sidebar.selectbox("Choose a Service", ["☕ Coffee Management", "🛒 Grocery Tour", "🎬 Movie Ticket Booking", "💇‍♀️ Salon Appointment"])

# Coffee Management
if service == "☕ Coffee Management":
    st.header("☕ Coffee Order System")

    menu = {
        "Espresso ☕": 50,
        "Cappuccino ☕": 70,
        "Latte ☕": 80,
        "Mocha ☕": 90
    }

    st.write("### Menu:")
    st.table([{"Item": item, "Price (₹)": price} for item, price in menu.items()])

    if 'coffee_order' not in st.session_state:
        st.session_state.coffee_order = []

    selected_item = st.selectbox("Select a coffee", list(menu.keys()))

    if st.button("Add to Order"):
        st.session_state.coffee_order.append(selected_item)
        st.success(f"{selected_item} added to your order!")

    if st.session_state.coffee_order:
        st.write("### Your Coffee Order:")
        st.write(st.session_state.coffee_order)

        # **Calculate total price**
        total_price = sum(menu[item] for item in st.session_state.coffee_order)
        st.write(f"### Total Price: ₹{total_price}")

        if st.button("Confirm Order"):
            st.success(f"Your coffee order is confirmed! ☕ Enjoy! Total bill: ₹{total_price}")
            st.session_state.coffee_order = []  # Reset order


# Grocery Tour
elif service == "🛒 Grocery Tour":
    st.header("🛒 Grocery Shopping")

    grocery_items = {
        "🍞 Bread": 40,
        "🥚 Eggs (12 pcs)": 80,
        "🥛 Milk (1L)": 50,
        "🍎 Apples (1kg)": 100,
        "🍚 Rice (5kg)": 250
    }

    st.write("### Grocery Items:")
    st.table([{"Item": item, "Price (₹)": price} for item, price in grocery_items.items()])

    selected_grocery = st.multiselect("Select grocery items", list(grocery_items.keys()))

    if st.button("Confirm Purchase"):
        total_price = sum([grocery_items[item] for item in selected_grocery])
        st.success(f"Your total bill is ₹{total_price}. Thank you for shopping! 🛒")

# Movie Ticket Booking
elif service == "🎬 Movie Ticket Booking":
    st.header("🎬 Movie Ticket Booking")

    movies = {
        "🎥 Avengers: Endgame": 250,
        "🎥 Interstellar": 200,
        "🎥 Inception": 220,
        "🎥 The Dark Knight": 230
    }

    st.write("### Available Movies:")
    selected_movie = st.radio("Choose a movie", list(movies.keys()))
    ticket_count = st.number_input("Number of Tickets", min_value=1, max_value=10, value=1)

    if st.button("Book Ticket"):
        total_price = movies[selected_movie] * ticket_count
        st.success(f"🎟️ {ticket_count} tickets booked for {selected_movie}! Total: ₹{total_price}")

# Salon Appointment Booking
elif service == "💇‍♀️ Salon Appointment":
    st.header("💇‍♀️ Salon Appointment Booking")

    services = {
        "💆 Haircut": 300,
        "💅 Manicure": 250,
        "💄 Makeup": 500,
        "🧖 Facial": 400
    }

    st.write("### Available Salon Services:")
    selected_service = st.selectbox("Choose a service", list(services.keys()))

    date = st.date_input("Select Appointment Date")
    time = st.time_input("Select Time")

    if st.button("Confirm Appointment"):
        st.success(f"Your appointment for {selected_service} on {date} at {time} is confirmed! 💇‍♀️")


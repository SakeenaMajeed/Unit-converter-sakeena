# import streamlit as st


# conversion_factors = {
#     "Plane Angle": {
#         "Degree": 1.0,
#         "Arcsecond": 1 / 3600,
#         "Gradian": 0.9,
#         "Milliradian": 0.0572958,
#         "Minute of arc": 1 / 60,
#         "Radian": 57.2958
#     },
#     "Length": {
#         "Meter": 1.0,
#         "Kilometer": 1000.0,
#         "Centimeter": 0.01,
#         "Millimeter": 0.001,
#         "Micrometer": 0.000001,
#         "Nanometer": 0.000000001,
#         "Mile": 1609.34,
#         "Yard": 0.9144,
#         "Foot": 0.3048,
#         "Inch": 0.0254,
#         "Nautical Mile": 1852.0,
#         "Fathom": 1.8288,  # Added unit
#         "Furlong": 201.168,  # Added unit
#         "Light Year": 9.461e+15  # Added unit
#     },
#     "Mass": {
#         "Kilogram": 1.0,
#         "Gram": 0.001,
#         "Milligram": 0.000001,
#         "Microgram": 0.000000001,
#         "Pound": 0.453592,
#         "Ounce": 0.0283495,
#         "Stone": 6.35029,
#         "Ton (metric)": 1000.0
#     },
#     "Temperature": {
#         "Celsius": {"to_base": lambda x: x, "from_base": lambda x: x},
#         "Fahrenheit": {"to_base": lambda x: (x - 32) * 5/9, "from_base": lambda x: (x * 9/5) + 32},
#         "Kelvin": {"to_base": lambda x: x - 273.15, "from_base": lambda x: x + 273.15}
#     },
#     "Speed": {
#         "Meters per second": 1.0,
#         "Kilometers per hour": 0.277778,
#         "Miles per hour": 0.44704,
#         "Knots": 0.514444,
#         "Feet per second": 0.3048
#     },
#     "Time": {
#         "Second": 1.0,
#         "Minute": 60.0,
#         "Hour": 3600.0,
#         "Day": 86400.0,
#         "Week": 604800.0,
#         "Month": 2629746.0,
#         "Year": 31556952.0
#     },
#     "Volume": {
#         "Liter": 1.0,
#         "Milliliter": 0.001,
#         "Cubic meter": 1000.0,
#         "Cubic centimeter": 0.001,
#         "Gallon (US)": 3.78541,
#         "Gallon (UK)": 4.54609,
#         "Quart": 0.946353,
#         "Pint": 0.473176
#     },
#     "Pressure": {
#         "Pascal": 1.0,
#         "Kilopascal": 1000.0,
#         "Bar": 100000.0,
#         "Atmosphere": 101325.0,
#         "PSI": 6894.76,
#         "Torr": 133.322
#     },
#     "Energy": {
#         "Joule": 1.0,
#         "Kilojoule": 1000.0,
#         "Calorie": 4.184,
#         "Kilocalorie": 4184.0,
#         "Kilowatt-hour": 3600000.0,
#         "Electronvolt": 1.60218e-19
#     },
#     "Power": {
#         "Watt": 1.0,
#         "Kilowatt": 1000.0,
#         "Megawatt": 1000000.0,
#         "Horsepower": 745.7
#     },
#     "Fuel Economy": {
#         "Miles per gallon (US)": 1.0,
#         "Miles per gallon (UK)": 1.20095,
#         "Kilometers per liter": 0.425144,
#         "Liters per 100km": 235.215
#     },
#     "Data Transfer Rate": {
#         "Bits per second": 1.0,
#         "Kilobits per second": 1000.0,
#         "Megabits per second": 1000000.0,
#         "Gigabits per second": 1000000000.0
#     },
#     "Digital Storage": {
#         "Bit": 1.0,
#         "Byte": 8.0,
#         "Kilobyte": 8000.0,
#         "Megabyte": 8000000.0,
#         "Gigabyte": 8000000000.0,
#         "Terabyte": 8000000000000.0
#     }
# }

# def convert_units(value, from_unit, to_unit, category):
#     factors = conversion_factors.get(category, {})
#     if category == "Temperature":
#         # Special handling for temperature
#         base_value = factors[from_unit]["to_base"](value)
#         return factors[to_unit]["from_base"](base_value)
#     else:
#         return (value * factors[from_unit]) / factors[to_unit]


# st.set_page_config(page_title="Unit Converter", layout="centered")
# st.title("⚡ Advanced Unit Converter")


# conversion_type = st.selectbox("Select Conversion Type", list(conversion_factors.keys()))


# col1, col2, col3 = st.columns([2, 1, 2])

# with col1:
#     from_unit = st.selectbox("From Unit", list(conversion_factors[conversion_type].keys()))

# with col2:
#     st.markdown("<h2 style='text-align: center;'>=</h2>", unsafe_allow_html=True)

# with col3:
#     to_unit = st.selectbox("To Unit", list(conversion_factors[conversion_type].keys()))

# value1 = st.number_input("Enter Value", value=1.0, step=0.1, format="%f") 

# try:
#     value2 = convert_units(value1, from_unit, to_unit, conversion_type)
#     st.markdown(f"<h2 style='text-align: center; color: blue;'>Result: {value2:.4f}</h2>", unsafe_allow_html=True)
# except Exception as e:
#     st.markdown(f"<h2 style='text-align: center; color: red;'>Error: {str(e)}</h2>", unsafe_allow_html=True)



# # # import streamlit as st
# # # import google.generativeai as genai

# # # # Configure API Key
# # # API_KEY = "AIzaSyDzw7uxHiiNpKcqZ1SCjxMlV5zUd8qxGiI"  # Replace with your key.
# # # genai.configure(api_key=API_KEY)
# # # model = genai.GenerativeModel("gemini-1.5-pro")

# # # # Unit Conversion Factors
# # # conversion_factors = {
# # #     "Length": {
# # #         "Meter": 1.0,
# # #         "Kilometer": 1000.0,
# # #         "Centimeter": 0.01,
# # #         "Millimeter": 0.001,
# # #         "Mile": 1609.34,
# # #         "Yard": 0.9144,
# # #         "Foot": 0.3048,
# # #         "Inch": 0.0254
# # #     },
# # #     "Mass": {
# # #         "Kilogram": 1.0,
# # #         "Gram": 0.001,
# # #         "Pound": 0.453592,
# # #         "Ounce": 0.0283495
# # #     },
# # #     "Temperature": {
# # #         "Celsius": {"to_base": lambda x: x, "from_base": lambda x: x},
# # #         "Fahrenheit": {"to_base": lambda x: (x - 32) * 5/9, "from_base": lambda x: (x * 9/5) + 32},
# # #         "Kelvin": {"to_base": lambda x: x - 273.15, "from_base": lambda x: x + 273.15}
# # #     }
# # # }

# # # def convert_units(value, from_unit, to_unit, category):
# # #     factors = conversion_factors.get(category, {})
# # #     if category == "Temperature":
# # #         base_value = factors[from_unit]["to_base"](value)
# # #         return factors[to_unit]["from_base"](base_value)
# # #     else:
# # #         return (value * factors[from_unit]) / factors[to_unit]

# # # # Streamlit UI
# # # st.set_page_config(page_title="AI Chat & Converter", layout="wide")
# # # st.sidebar.title("Navigation")
# # # option = st.sidebar.radio("Choose an Option", ["Unit Converter", "AI Chatbot"])

# # # if option == "Unit Converter":
# # #     st.title("⚡ Unit Converter")
# # #     category = st.selectbox("Select Category", list(conversion_factors.keys()))
# # #     from_unit = st.selectbox("From Unit", list(conversion_factors[category].keys()))
# # #     to_unit = st.selectbox("To Unit", list(conversion_factors[category].keys()))
# # #     value = st.number_input("Enter Value", value=1.0)
    
# # #     try:
# # #         result = convert_units(value, from_unit, to_unit, category)
# # #         st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
# # #     except Exception as e:
# # #         st.error(f"Conversion Error: {str(e)}")

# # # elif option == "AI Chatbot":
# # #     st.title("🤖 AI Chatbot")
# # #     if "messages" not in st.session_state:
# # #         st.session_state.messages = []
    
# # #     for message in st.session_state.messages:
# # #         role = "User" if message["role"] == "user" else "AI"
# # #         st.write(f"**{role}:** {message['content']}")
    
# # #     user_input = st.chat_input("Type your message...")
# # #     if user_input:
# # #         st.session_state.messages.append({"role": "user", "content": user_input})
        
# # #         with st.spinner("Generating response..."):
# # #             try:
# # #                 response = model.generate_content(user_input)
# # #                 ai_reply = response.text
# # #             except Exception as e:
# # #                 ai_reply = f"Error: {str(e)}"
        
# # #         st.session_state.messages.append({"role": "assistant", "content": ai_reply})
# # #         st.experimental_rerun()


# # # import streamlit as st
# # # from pint import UnitRegistry
# # # import datetime
# # # import pandas as pd
# # # import google.generativeai as genai
# # # import random
# # # import os
# # # from dotenv import load_dotenv

# # # load_dotenv()

# # # # Get API Key from environment variables
# # # API_KEY = os.getenv("GEMINI_API_KEY")
# # # genai.configure(api_key=API_KEY)

# # # # Initialize unit registry
# # # ureg = UnitRegistry()

# # # # Conversion function
# # # def convert_units(value, from_unit, to_unit):
# # #     try:
# # #         result = (value * ureg(from_unit)).to(to_unit)
# # #         return result.magnitude, result.units
# # #     except Exception as e:
# # #         return None, str(e)

# # # # Log conversion history
# # # def log_conversion(value, from_unit, to_unit, result):
# # #     with open("conversion_log.txt", "a") as log_file:
# # #         log_file.write(f"{datetime.datetime.now()} - {value} {from_unit} -> {result} {to_unit}\n")


# # # # Load conversion history
# # # def load_conversion_history():
# # #     try:
# # #         with open("conversion_log.txt", "r") as log_file:
# # #             lines = log_file.readlines()
# # #         history_data = [line.strip().split(" - ") for line in lines]
# # #         return pd.DataFrame(history_data, columns=["Timestamp", "Conversion"])
# # #     except FileNotFoundError:
# # #         return pd.DataFrame(columns=["Timestamp", "Conversion"])

# # # # Fun AI insights
# # # def ai_suggestions():
# # #     insights = [
# # #         "Did you know? The metric system is used by 95% of the world!",
# # #         "Fun Fact: A mile was originally defined as 1,000 Roman paces.",
# # #         "Energy Tip: 1 kilowatt-hour can power a TV for about 10 hours!",
# # #         "Speed Trivia: The fastest recorded human speed is 44.72 km/h!",
# # #         "Water Insight: 1 liter of water weighs exactly 1 kilogram!"
# # #     ]
# # #     return random.choice(insights)

# # # # Streamlit UI setup
# # # st.set_page_config(page_title="🔄 Smart Unit Converter", page_icon="⚡", layout="centered")
# # # st.title("⚡ Smart Unit Converter with AI Insights")
# # # st.markdown("Convert units easily and learn something new! 🚀")

# # # # Sidebar category selection
# # # category = st.sidebar.selectbox("📌 Select Category", [
# # #     "Length", "Weight", "Temperature", "Speed", "Time", "Volume", "Area", "Energy"
# # # ])

# # # unit_options = {
# # #     "Length": ["meter", "kilometer", "mile", "yard", "foot", "inch"],
# # #     "Weight": ["gram", "kilogram", "pound", "ounce", "ton"],
# # #     "Temperature": ["celsius", "fahrenheit", "kelvin"],
# # #     "Speed": ["meter/second", "kilometer/hour", "mile/hour", "knot"],
# # #     "Time": ["second", "minute", "hour", "day"],
# # #     "Volume": ["liter", "milliliter", "gallon", "cubic meter", "cup"],
# # #     "Area": ["square meter", "square kilometer", "square foot", "square inch", "acre", "hectare"],
# # #     "Energy": ["joule", "kilojoule", "calorie", "kilocalorie", "watt hour", "kilowatt hour"]
# # # }

# # # # Input fields for conversion
# # # value = st.number_input("🔢 Enter Value", min_value=0.0, format="%.2f")
# # # from_unit = st.selectbox("📍 From Unit", unit_options[category])
# # # to_unit = st.selectbox("🎯 To Unit", unit_options[category])

# # # # Conversion logic
# # # if st.button("🚀 Convert", use_container_width=True):
# # #     if from_unit and to_unit:
# # #         if category == "Temperature":
# # #             try:
# # #                 conversions = {
# # #                     ("celsius", "fahrenheit"): lambda x: (x * 9/5) + 32,
# # #                     ("fahrenheit", "celsius"): lambda x: (x - 32) * 5/9,
# # #                     ("celsius", "kelvin"): lambda x: x + 273.15,
# # #                     ("kelvin", "celsius"): lambda x: x - 273.15,
# # #                     ("fahrenheit", "kelvin"): lambda x: (x - 32) * 5/9 + 273.15,
# # #                     ("kelvin", "fahrenheit"): lambda x: (x - 273.15) * 9/5 + 32
# # #                 }
# # #                 result = conversions.get((from_unit, to_unit), lambda x: x)(value)
# # #                 st.success(f"🎉 Converted Value: {result:.2f} {to_unit}")
# # #                 log_conversion(value, from_unit, to_unit, result)
# # #             except Exception as e:
# # #                 st.error(f"❌ Error: {e}")
# # #         else:
# # #             converted_value, unit = convert_units(value, from_unit, to_unit)
# # #             if converted_value is not None:
# # #                 st.success(f"🎉 Converted Value: {converted_value:.2f} {unit}")
# # #                 log_conversion(value, from_unit, to_unit, converted_value)
# # #                 st.info(f"💡 AI Insight: {ai_suggestions()} ")
# # #             else:
# # #                 st.error("❌ Invalid Conversion!")

# # # # Sidebar: Toggle conversion history
# # # show_history = st.sidebar.checkbox("📜 Show History", key="show_history")

# # # if show_history:
# # #     st.sidebar.subheader("📜 Conversion History")
# # #     history_df = load_conversion_history()
# # #     if not history_df.empty:
# # #         st.sidebar.dataframe(history_df, height=250)
# # #         st.sidebar.download_button("📥 Download History", history_df.to_csv(index=False), "conversion_history.csv")
# # #     else:
# # #         st.sidebar.write("⚠️ No history found!")

# # # # Clear history button
# # # if st.sidebar.button("🗑️ Clear History"):
# # #     open("conversion_log.txt", "w").close()
# # #     st.sidebar.success("✅ History cleared!")

# # # # AI Chatbot Section
# # # st.header("🤖 Smart Gemini AI Chatbot")
# # # st.write("Ask me anything!")

# # # # Store chat history
# # # if "messages" not in st.session_state:
# # #     st.session_state.messages = []

# # # # Display chat history
# # # for message in st.session_state.messages:
# # #     with st.chat_message(message["role"]):
# # #         st.markdown(message["content"])

# # # # Quick Replies
# # # quick_replies = ["What can you do?", "Tell me a fun fact!", "How does unit conversion work?", "What's the latest tech trend?"]
# # # selected_reply = st.sidebar.radio("💡 Quick Questions", quick_replies, index=None, key="quick_reply")

# # # # Chat input field
# # # user_input = st.chat_input("Type your message...")
# # # final_input = user_input if user_input else selected_reply

# # # if final_input:  # Process chat input only if available
# # #     st.session_state.messages.append({"role": "user", "content": final_input})
# # #     with st.chat_message("user"):
# # #         st.markdown(final_input)

# # #     # Show "Thinking..." with loading animation
# # #     with st.chat_message("assistant"):
# # #         with st.spinner("🤔 Thinking..."):
# # #             try:
# # #                 response = genai.GenerativeModel("gemini-1.5-pro").generate_content(final_input)
# # #                 ai_reply = response.text
# # #             except Exception as e:
# # #                 ai_reply = f"⚠️ Error: {str(e)}"

# # #         st.markdown(ai_reply)
# # #         st.session_state.messages.append({"role": "assistant", "content": ai_reply})

# # # # Footer
# # # st.markdown("---")
# # # st.markdown("❤️ Created by Hooriya Muhammad Fareed ❤️")


# # # import os
# # # import streamlit as st
# # # import google.generativeai as genai
# # # from dotenv import load_dotenv

# # # load_dotenv()

# # # # Get API Key from environment variables
# # # API_KEY = os.getenv("GEMINI_API_KEY")
# # # genai.configure(api_key=API_KEY)

# # # # Initialize the correct model
# # # model = genai.GenerativeModel("gemini-1.5-pro")

# # # # Streamlit UI
# # # st.set_page_config(
# # #     page_title="AI Chatbot & Unit Converter",
# # #     page_icon="🤖",
# # #     layout="wide",
# # #     initial_sidebar_state="expanded",
# # # )

# # # # Custom CSS for styling
# # # st.markdown(
# # #     """
# # #     <style>
# # #     .chat-container {
# # #         background: rgba(255, 255, 255, 0.15);
# # #         padding: 20px;
# # #         border-radius: 15px;
# # #         height: 600px;
# # #         overflow-y: auto;
# # #         backdrop-filter: blur(12px);
# # #         box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
# # #     }
# # #     .chat-container::-webkit-scrollbar {
# # #         width: 8px;
# # #     }
# # #     .chat-container::-webkit-scrollbar-thumb {
# # #         background: linear-gradient(45deg, #6366f1, #a855f7);
# # #         border-radius: 10px;
# # #     }
# # #     .user-message, .assistant-message {
# # #         padding: 14px 20px;
# # #         border-radius: 22px;
# # #         margin-bottom: 12px;
# # #         max-width: 70%;
# # #         font-weight: 500;
# # #     }
# # #     .user-message {
# # #         background: linear-gradient(135deg, #6366f1, #a855f7);
# # #         color: white;
# # #         margin-left: auto;
# # #         text-align: right;
# # #     }
# # #     .assistant-message {
# # #         background: linear-gradient(135deg, #14b8a6, #06b6d4);
# # #         color: white;
# # #         text-align: left;
# # #     }
# # #     </style>
# # #     """,
# # #     unsafe_allow_html=True,
# # # )

# # # st.title("🤖 AI Chatbot & Unit Converter")
# # # st.markdown("<p class='welcome-text'>Welcome! Ask me anything or convert units.</p>", unsafe_allow_html=True)

# # # # Chat history
# # # if "messages" not in st.session_state:
# # #     st.session_state.messages = []

# # # # Sidebar for chat history and clear button
# # # with st.sidebar:
# # #     st.header("Chat History")
# # #     for i, message in enumerate(st.session_state.messages):
# # #         if message["role"] == "user":
# # #             st.write(f" 👩🏻 {i//2 + 1}: {message['content'][:50]}...")
# # #         else:
# # #             st.write(f" 🤖 Assistant {i//2 + 1}: {message['content'][:50]}...")
# # #     if st.button("Clear Chat"):
# # #         st.session_state.messages = []
# # #         st.rerun()

# # # # Chat area
# # # chat_container = st.container()

# # # with chat_container:
# # #     for message in st.session_state.messages:
# # #         role = "user-message" if message["role"] == "user" else "assistant-message"
# # #         st.markdown(f'<div class="{role}">{message["content"]}</div>', unsafe_allow_html=True)

# # # # User input
# # # user_input = st.chat_input("Type your message...")
# # # if user_input:
# # #     st.session_state.messages.append({"role": "user", "content": user_input})
# # #     with chat_container:
# # #         st.markdown(f'<div class="user-message">{user_input}</div>', unsafe_allow_html=True)
# # #     with st.spinner("Generating response..."):
# # #         try:
# # #             response = model.generate_content(user_input)
# # #             ai_reply = response.text
# # #         except Exception as e:
# # #             ai_reply = f"Error: {str(e)}"
# # #     st.session_state.messages.append({"role": "assistant", "content": ai_reply})
# # #     with chat_container:
# # #         st.markdown(f'<div class="assistant-message">{ai_reply}</div>', unsafe_allow_html=True)

# # # # Unit Converter
# # # conversion_factors = {
# # #     "Length": {"Meter": 1.0, "Kilometer": 1000.0, "Centimeter": 0.01, "Millimeter": 0.001, "Mile": 1609.34},
# # #     "Mass": {"Kilogram": 1.0, "Gram": 0.001, "Pound": 0.453592, "Ounce": 0.0283495},
# # #     "Temperature": {"Celsius": lambda x: x, "Fahrenheit": lambda x: (x - 32) * 5/9, "Kelvin": lambda x: x - 273.15}
# # # }

# # # def convert_units(value, from_unit, to_unit, category):
# # #     if category == "Temperature":
# # #         return conversion_factors[category][to_unit](conversion_factors[category][from_unit](value))
# # #     return value * conversion_factors[category][from_unit] / conversion_factors[category][to_unit]

# # # st.header("Unit Converter")
# # # category = st.selectbox("Select Conversion Type", list(conversion_factors.keys()))
# # # from_unit, to_unit = st.selectbox("From Unit", conversion_factors[category]), st.selectbox("To Unit", conversion_factors[category])
# # # value = st.number_input("Enter Value", value=1.0)
# # # if st.button("Convert"):
# # #     try:
# # #         result = convert_units(value, from_unit, to_unit, category)
# # #         st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
# # #     except Exception as e:
# # #         st.error(f"Conversion error: {str(e)}")












# # import os
# # import streamlit as st
# # import google.generativeai as genai

# # from dotenv import load_dotenv

# # load_dotenv()

# # # Get API Key from environment variables
# # API_KEY = os.getenv("GEMINI_API_KEY")
# # genai.configure(api_key=API_KEY)
# # # Initialize AI model
# # model = genai.GenerativeModel("gemini-1.5-pro")

# # # Streamlit UI Configuration
# # st.set_page_config(
# #     page_title="AI Chatbot & Unit Converter",
# #     page_icon="🤖",
# #     layout="wide",
# #     initial_sidebar_state="expanded",
# # )

# # # Custom CSS for better styling
# # st.markdown(
# #     """
# #     <style>
# #     body {
# #         font-family: 'Arial', sans-serif;
# #     }
# #     .chat-container, .unit-converter {
# #         background: rgba(255, 255, 255, 0.15);
# #         padding: 20px;
# #         border-radius: 15px;
# #         height: auto;
# #         backdrop-filter: blur(12px);
# #         box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
# #     }
# #     .chat-container {
# #         height: 500px;
# #         overflow-y: auto;
# #     }
# #     .user-message, .assistant-message {
# #         padding: 14px 20px;
# #         border-radius: 22px;
# #         margin-bottom: 12px;
# #         max-width: 70%;
# #         font-weight: 500;
# #     }
# #     .user-message {
# #         background: linear-gradient(135deg, #6366f1, #a855f7);
# #         color: white;
# #         margin-left: auto;
# #         text-align: right;
# #     }
# #     .assistant-message {
# #         background: linear-gradient(135deg, #14b8a6, #06b6d4);
# #         color: white;
# #         text-align: left;
# #     }
# #     .welcome-text {
# #         text-align: center;
# #         font-size: 2.5rem;
# #         font-weight: bold;
# #         color: #222;
# #         background: linear-gradient(45deg, #6366f1, #a855f7);
# #         -webkit-background-clip: text;
# #         -webkit-text-fill-color: transparent;
# #     }
# #     </style>
# #     """,
# #     unsafe_allow_html=True,
# # )

# # # Sidebar navigation
# # st.sidebar.title("Navigation")
# # page = st.sidebar.radio("Select a Feature", ["AI Chatbot", "Unit Converter"])

# # # Create main tabs
# # tab1, tab2 = st.tabs(["Unit Converter", "Gemini AI Chatbot"])

# # # Unit Converter Tab
# # with tab1:
# #     st.markdown('<div><h2>"Unit Converter"</h2></div>', unsafe_allow_html=True)
    
# #     # Select conversion type
   
    
# #     # Input value
# #     value = st.number_input('Enter Value', value=0.0)

# # if page == "AI Chatbot":
# #     st.title("🤖 AI Chatbot")
# #     st.markdown('<p class="welcome-text">Welcome! Ask me anything.</p>', unsafe_allow_html=True)
    
# #     if "messages" not in st.session_state:
# #         st.session_state.messages = []
    
# #     chat_container = st.container()
# #     with chat_container:
# #         for message in st.session_state.messages:
# #             message_class = "user-message" if message["role"] == "user" else "assistant-message"
# #             st.markdown(f'<div class="{message_class}">{message["content"]}</div>', unsafe_allow_html=True)
    
# #     user_input = st.chat_input("Type your message...")
# #     if user_input:
# #         st.session_state.messages.append({"role": "user", "content": user_input})
# #         with chat_container:
# #             st.markdown(f'<div class="user-message">{user_input}</div>', unsafe_allow_html=True)
        
# #         with st.spinner("Generating response..."):
# #             try:
# #                 response = model.generate_content(user_input)
# #                 ai_reply = response.text
# #             except Exception as e:
# #                 ai_reply = f"Error: {str(e)}"
        
# #         st.session_state.messages.append({"role": "assistant", "content": ai_reply})
# #         with chat_container:
# #             st.markdown(f'<div class="assistant-message">{ai_reply}</div>', unsafe_allow_html=True)

# # elif page == "Unit Converter":

# #     conversion_factors = {
# #     "Plane Angle": {
# #         "Degree": 1.0,
# #         "Arcsecond": 1 / 3600,
# #         "Gradian": 0.9,
# #         "Milliradian": 0.0572958,
# #         "Minute of arc": 1 / 60,
# #         "Radian": 57.2958
# #     },
# #     "Length": {
# #         "Meter": 1.0,
# #         "Kilometer": 1000.0,
# #         "Centimeter": 0.01,
# #         "Millimeter": 0.001,
# #         "Micrometer": 0.000001,
# #         "Nanometer": 0.000000001,
# #         "Mile": 1609.34,
# #         "Yard": 0.9144,
# #         "Foot": 0.3048,
# #         "Inch": 0.0254,
# #         "Nautical Mile": 1852.0,
# #         "Fathom": 1.8288,  # Added unit
# #         "Furlong": 201.168,  # Added unit
# #         "Light Year": 9.461e+15  # Added unit
# #     },
# #     "Mass": {
# #         "Kilogram": 1.0,
# #         "Gram": 0.001,
# #         "Milligram": 0.000001,
# #         "Microgram": 0.000000001,
# #         "Pound": 0.453592,
# #         "Ounce": 0.0283495,
# #         "Stone": 6.35029,
# #         "Ton (metric)": 1000.0
# #     },
# #     "Temperature": {
# #         "Celsius": {"to_base": lambda x: x, "from_base": lambda x: x},
# #         "Fahrenheit": {"to_base": lambda x: (x - 32) * 5/9, "from_base": lambda x: (x * 9/5) + 32},
# #         "Kelvin": {"to_base": lambda x: x - 273.15, "from_base": lambda x: x + 273.15}
# #     },
# #     "Speed": {
# #         "Meters per second": 1.0,
# #         "Kilometers per hour": 0.277778,
# #         "Miles per hour": 0.44704,
# #         "Knots": 0.514444,
# #         "Feet per second": 0.3048
# #     },
# #     "Time": {
# #         "Second": 1.0,
# #         "Minute": 60.0,
# #         "Hour": 3600.0,
# #         "Day": 86400.0,
# #         "Week": 604800.0,
# #         "Month": 2629746.0,
# #         "Year": 31556952.0
# #     },
# #     "Volume": {
# #         "Liter": 1.0,
# #         "Milliliter": 0.001,
# #         "Cubic meter": 1000.0,
# #         "Cubic centimeter": 0.001,
# #         "Gallon (US)": 3.78541,
# #         "Gallon (UK)": 4.54609,
# #         "Quart": 0.946353,
# #         "Pint": 0.473176
# #     },
# #     "Pressure": {
# #         "Pascal": 1.0,
# #         "Kilopascal": 1000.0,
# #         "Bar": 100000.0,
# #         "Atmosphere": 101325.0,
# #         "PSI": 6894.76,
# #         "Torr": 133.322
# #     },
# #     "Energy": {
# #         "Joule": 1.0,
# #         "Kilojoule": 1000.0,
# #         "Calorie": 4.184,
# #         "Kilocalorie": 4184.0,
# #         "Kilowatt-hour": 3600000.0,
# #         "Electronvolt": 1.60218e-19
# #     },
# #     "Power": {
# #         "Watt": 1.0,
# #         "Kilowatt": 1000.0,
# #         "Megawatt": 1000000.0,
# #         "Horsepower": 745.7
# #     },
# #     "Fuel Economy": {
# #         "Miles per gallon (US)": 1.0,
# #         "Miles per gallon (UK)": 1.20095,
# #         "Kilometers per liter": 0.425144,
# #         "Liters per 100km": 235.215
# #     },
# #     "Data Transfer Rate": {
# #         "Bits per second": 1.0,
# #         "Kilobits per second": 1000.0,
# #         "Megabits per second": 1000000.0,
# #         "Gigabits per second": 1000000000.0
# #     },
# #     "Digital Storage": {
# #         "Bit": 1.0,
# #         "Byte": 8.0,
# #         "Kilobyte": 8000.0,
# #         "Megabyte": 8000000.0,
# #         "Gigabyte": 8000000000.0,
# #         "Terabyte": 8000000000000.0
# #     }
# # }
    
# #     def convert_units(value, from_unit, to_unit, category):
# #         factors = conversion_factors.get(category, {})
# #         if category == "Temperature":
# #             base_value = factors[from_unit]["to_base"](value)
# #             return factors[to_unit]["from_base"](base_value)
# #         else:
# #             return (value * factors[from_unit]) / factors[to_unit]
    
# #     st.title("⚡ Advanced Unit Converter")
# #     conversion_type = st.selectbox("Select Conversion Type", list(conversion_factors.keys()))
# #     col1, col2, col3 = st.columns([2, 1, 2])
    
# #     with col1:
# #         from_unit = st.selectbox("From Unit", list(conversion_factors[conversion_type].keys()))
    
# #     with col2:
# #         st.markdown("<h2 style='text-align: center;'>=</h2>", unsafe_allow_html=True)
    
# #     with col3:
# #         to_unit = st.selectbox("To Unit", list(conversion_factors[conversion_type].keys()))
    
# #     value1 = st.number_input("Enter Value", value=1.0, step=0.1, format="%f") 
    
# #     try:
# #         value2 = convert_units(value1, from_unit, to_unit, conversion_type)
# #         st.markdown(f"<h2 style='text-align: center; color: blue;'>Result: {value2:.4f}</h2>", unsafe_allow_html=True)
# #     except Exception as e:
# #         st.markdown(f"<h2 style='text-align: center; color: red;'>Error: {str(e)}</h2>", unsafe_allow_html=True)




# # import os
# # import streamlit as st
# # import google.generativeai as genai
# # from dotenv import load_dotenv

# # load_dotenv()

# # # Get API Key from environment variables
# # API_KEY = os.getenv("GEMINI_API_KEY")
# # genai.configure(api_key=API_KEY)
# # # Initialize AI model
# # model = genai.GenerativeModel("gemini-1.5-pro")

# # # Streamlit UI Configuration
# # st.set_page_config(
# #     page_title="AI Chatbot & Unit Converter",
# #     page_icon="🤖",
# #     layout="wide",
# #     initial_sidebar_state="expanded",
# # )

# # # Custom CSS for better styling
# # st.markdown(
# #     """
# #     <style>
# #     body {
# #         font-family: 'Arial', sans-serif;
# #     }
# #     .chat-container, .unit-converter {
# #         background: rgba(255, 255, 255, 0.15);
# #         padding: 20px;
# #         border-radius: 15px;
# #         height: auto;
# #         backdrop-filter: blur(12px);
# #         box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
# #     }
# #     .chat-container {
# #         height: 500px;
# #         overflow-y: auto;
# #     }
# #     .user-message, .assistant-message {
# #         padding: 14px 20px;
# #         border-radius: 22px;
# #         margin-bottom: 12px;
# #         max-width: 70%;
# #         font-weight: 500;
# #     }
# #     .user-message {
# #         background: linear-gradient(135deg, #6366f1, #a855f7);
# #         color: white;
# #         margin-left: auto;
# #         text-align: right;
# #     }
# #     .assistant-message {
# #         background: linear-gradient(135deg, #14b8a6, #06b6d4);
# #         color: white;
# #         text-align: left;
# #     }
# #     .welcome-text {
# #         text-align: center;
# #         font-size: 2.5rem;
# #         font-weight: bold;
# #         color: #222;
# #         background: linear-gradient(45deg, #6366f1, #a855f7);
# #         -webkit-background-clip: text;
# #         -webkit-text-fill-color: transparent;
# #     }
# #     </style>
# #     """,
# #     unsafe_allow_html=True,
# # )

# # # Sidebar navigation
# # st.sidebar.title("Navigation")
# # page = st.sidebar.radio("Select a Feature", ["AI Chatbot", "Unit Converter"])

# # # Create main tabs
# # tab1, tab2 = st.tabs(["Unit Converter", "Gemini AI Chatbot"])

# # # Unit Converter Tab
# # with tab1:
# #     st.markdown('<div><h2>"Unit Converter"</h2></div>', unsafe_allow_html=True)
    
# #     # Select conversion type
# #     conversion_factors = {
# #         "Plane Angle": {
# #             "Degree": 1.0,
# #             "Arcsecond": 1 / 3600,
# #             "Gradian": 0.9,
# #             "Milliradian": 0.0572958,
# #             "Minute of arc": 1 / 60,
# #             "Radian": 57.2958
# #         },
# #         "Length": {
# #             "Meter": 1.0,
# #             "Kilometer": 1000.0,
# #             "Centimeter": 0.01,
# #             "Millimeter": 0.001,
# #             "Micrometer": 0.000001,
# #             "Nanometer": 0.000000001,
# #             "Mile": 1609.34,
# #             "Yard": 0.9144,
# #             "Foot": 0.3048,
# #             "Inch": 0.0254,
# #             "Nautical Mile": 1852.0,
# #             "Fathom": 1.8288,  # Added unit
# #             "Furlong": 201.168,  # Added unit
# #             "Light Year": 9.461e+15  # Added unit
# #         },
# #         "Mass": {
# #             "Kilogram": 1.0,
# #             "Gram": 0.001,
# #             "Milligram": 0.000001,
# #             "Microgram": 0.000000001,
# #             "Pound": 0.453592,
# #             "Ounce": 0.0283495,
# #             "Stone": 6.35029,
# #             "Ton (metric)": 1000.0
# #         },
# #         "Temperature": {
# #             "Celsius": {"to_base": lambda x: x, "from_base": lambda x: x},
# #             "Fahrenheit": {"to_base": lambda x: (x - 32) * 5/9, "from_base": lambda x: (x * 9/5) + 32},
# #             "Kelvin": {"to_base": lambda x: x - 273.15, "from_base": lambda x: x + 273.15}
# #         },
# #         "Speed": {
# #             "Meters per second": 1.0,
# #             "Kilometers per hour": 0.277778,
# #             "Miles per hour": 0.44704,
# #             "Knots": 0.514444,
# #             "Feet per second": 0.3048
# #         },
# #         "Time": {
# #             "Second": 1.0,
# #             "Minute": 60.0,
# #             "Hour": 3600.0,
# #             "Day": 86400.0,
# #             "Week": 604800.0,
# #             "Month": 2629746.0,
# #             "Year": 31556952.0
# #         },
# #         "Volume": {
# #             "Liter": 1.0,
# #             "Milliliter": 0.001,
# #             "Cubic meter": 1000.0,
# #             "Cubic centimeter": 0.001,
# #             "Gallon (US)": 3.78541,
# #             "Gallon (UK)": 4.54609,
# #             "Quart": 0.946353,
# #             "Pint": 0.473176
# #         },
# #         "Pressure": {
# #             "Pascal": 1.0,
# #             "Kilopascal": 1000.0,
# #             "Bar": 100000.0,
# #             "Atmosphere": 101325.0,
# #             "PSI": 6894.76,
# #             "Torr": 133.322
# #         },
# #         "Energy": {
# #             "Joule": 1.0,
# #             "Kilojoule": 1000.0,
# #             "Calorie": 4.184,
# #             "Kilocalorie": 4184.0,
# #             "Kilowatt-hour": 3600000.0,
# #             "Electronvolt": 1.60218e-19
# #         },
# #         "Power": {
# #             "Watt": 1.0,
# #             "Kilowatt": 1000.0,
# #             "Megawatt": 1000000.0,
# #             "Horsepower": 745.7
# #         },
# #         "Fuel Economy": {
# #             "Miles per gallon (US)": 1.0,
# #             "Miles per gallon (UK)": 1.20095,
# #             "Kilometers per liter": 0.425144,
# #             "Liters per 100km": 235.215
# #         },
# #         "Data Transfer Rate": {
# #             "Bits per second": 1.0,
# #             "Kilobits per second": 1000.0,
# #             "Megabits per second": 1000000.0,
# #             "Gigabits per second": 1000000000.0
# #         },
# #         "Digital Storage": {
# #             "Bit": 1.0,
# #             "Byte": 8.0,
# #             "Kilobyte": 8000.0,
# #             "Megabyte": 8000000.0,
# #             "Gigabyte": 8000000000.0,
# #             "Terabyte": 8000000000000.0
# #         }
# #     }
    
# #     def convert_units(value, from_unit, to_unit, category):
# #         factors = conversion_factors.get(category, {})
# #         if category == "Temperature":
# #             base_value = factors[from_unit]["to_base"](value)
# #             return factors[to_unit]["from_base"](base_value)
# #         else:
# #             return (value * factors[from_unit]) / factors[to_unit]
    
# #     st.title("⚡ Advanced Unit Converter")
# #     conversion_type = st.selectbox("Select Conversion Type", list(conversion_factors.keys()))
# #     col1, col2, col3 = st.columns([2, 1, 2])
    
# #     with col1:
# #         from_unit = st.selectbox("From Unit", list(conversion_factors[conversion_type].keys()))
    
# #     with col2:
# #         st.markdown("<h2 style='text-align: center;'>=</h2>", unsafe_allow_html=True)
    
# #     with col3:
# #         to_unit = st.selectbox("To Unit", list(conversion_factors[conversion_type].keys()))
    
# #     value1 = st.number_input("Enter Value", value=1.0, step=0.1, format="%f") 
    
# #     try:
# #         value2 = convert_units(value1, from_unit, to_unit, conversion_type)
# #         st.markdown(f"<h2 style='text-align: center; color: blue;'>Result: {value2:.4f}</h2>", unsafe_allow_html=True)
# #     except Exception as e:
# #         st.markdown(f"<h2 style='text-align: center; color: red;'>Error: {str(e)}</h2>", unsafe_allow_html=True)

# # # AI Chatbot Tab
# # with tab2:
# #     st.title("🤖 AI Chatbot")
# #     st.markdown('<p class="welcome-text">Welcome! Ask me anything.</p>', unsafe_allow_html=True)
    
# #     if "messages" not in st.session_state:
# #         st.session_state.messages = []
    
# #     chat_container = st.container()
# #     with chat_container:
# #         for message in st.session_state.messages:
# #             message_class = "user-message" if message["role"] == "user" else "assistant-message"
# #             st.markdown(f'<div class="{message_class}">{message["content"]}</div>', unsafe_allow_html=True)
    
# #     user_input = st.chat_input("Type your message...")
# #     if user_input:
# #         st.session_state.messages.append({"role": "user", "content": user_input})
# #         with chat_container:
# #             st.markdown(f'<div class="user-message">{user_input}</div>', unsafe_allow_html=True)


# # import os
# # import streamlit as st
# # import google.generativeai as genai
# # from dotenv import load_dotenv

# # # Load environment variables
# # load_dotenv()

# # # Get API Key
# # API_KEY = os.getenv("GEMINI_API_KEY")
# # if not API_KEY:
# #     st.error("API Key not found! Please check your .env file.")
# # else:
# #     genai.configure(api_key=API_KEY)

# # # Initialize AI model
# # model = genai.GenerativeModel("gemini-1.5-pro")

# # # Streamlit UI Configuration
# # st.set_page_config(
# #     page_title="AI Chatbot & Unit Converter",
# #     page_icon="🤖",
# #     layout="wide",
# # )

# # # Custom CSS
# # st.markdown("""
# #     <style>
# #     .chat-container {
# #         background: rgba(255, 255, 255, 0.15);
# #         padding: 20px;
# #         border-radius: 15px;
# #         height: 500px;
# #         overflow-y: auto;
# #     }
# #     .user-message {
# #         background: linear-gradient(135deg, #6366f1, #a855f7);
# #         color: white;
# #         padding: 12px;
# #         border-radius: 12px;
# #         text-align: right;
# #         margin-left: auto;
# #         max-width: 70%;
# #     }
# #     .assistant-message {
# #         background: linear-gradient(135deg, #14b8a6, #06b6d4);
# #         color: white;
# #         padding: 12px;
# #         border-radius: 12px;
# #         text-align: left;
# #         max-width: 70%;
# #     }
# #     </style>
# #     """, unsafe_allow_html=True)

# # # Sidebar navigation
# # st.sidebar.title("Navigation")
# # page = st.sidebar.radio("Select a Feature", ["AI Chatbot", "Unit Converter"])

# # # --- Unit Converter ---
# # if page == "Unit Converter":
# #     st.title("⚡ Advanced Unit Converter")

# #     conversion_factors = {
# #         "Length": {"Meter": 1, "Kilometer": 1000, "Centimeter": 0.01, "Inch": 0.0254, "Foot": 0.3048},
# #         "Mass": {"Kilogram": 1, "Gram": 0.001, "Pound": 0.453592, "Ounce": 0.0283495},
# #         "Speed": {"Meters per second": 1, "Kilometers per hour": 0.277778, "Miles per hour": 0.44704},
# #         "Temperature": {
# #             "Celsius": lambda x: x,
# #             "Fahrenheit": lambda x: (x - 32) * 5/9,
# #             "Kelvin": lambda x: x - 273.15
# #         }
# #     }

# #     conversion_type = st.selectbox("Select Conversion Type", list(conversion_factors.keys()))
# #     from_unit = st.selectbox("From Unit", list(conversion_factors[conversion_type].keys()))
# #     to_unit = st.selectbox("To Unit", list(conversion_factors[conversion_type].keys()))
# #     value1 = st.number_input("Enter Value", value=1.0)

# #     def convert_units(value, from_unit, to_unit, category):
# #         if category == "Temperature":
# #             return conversion_factors[category][to_unit](conversion_factors[category][from_unit](value))
# #         return value * conversion_factors[category][from_unit] / conversion_factors[category][to_unit]

# #     try:
# #         result = convert_units(value1, from_unit, to_unit, conversion_type)
# #         st.success(f"Converted Value: {result:.4f} {to_unit}")
# #     except Exception as e:
# #         st.error(f"Conversion Error: {str(e)}")

# # # --- AI Chatbot ---
# # else:
# #     st.title("🤖 Gemini AI Chatbot")

# #     if "messages" not in st.session_state:
# #         st.session_state.messages = []

# #     chat_container = st.container()
# #     with chat_container:
# #         for msg in st.session_state.messages:
# #             msg_class = "user-message" if msg["role"] == "user" else "assistant-message"
# #             st.markdown(f'<div class="{msg_class}">{msg["content"]}</div>', unsafe_allow_html=True)

# #     user_input = st.chat_input("Type your message...")

# #     if user_input:
# #         st.session_state.messages.append({"role": "user", "content": user_input})
# #         with chat_container:
# #             st.markdown(f'<div class="user-message">{user_input}</div>', unsafe_allow_html=True)

# #         try:
# #             response = model.generate_content(user_input)
# #             reply = response.text
# #             st.session_state.messages.append({"role": "assistant", "content": reply})
# #             with chat_container:
# #                 st.markdown(f'<div class="assistant-message">{reply}</div>', unsafe_allow_html=True)
# #         except Exception as e:
# #             st.error(f"Gemini API Error: {str(e)}")


# # import os
# # import streamlit as st
# # import google.generativeai as genai
# # from dotenv import load_dotenv

# # # Load environment variables
# # load_dotenv()

# # # Get API Key
# # API_KEY = os.getenv("GEMINI_API_KEY")
# # if not API_KEY:
# #     st.error("API Key not found! Please check your .env file.")
# # else:
# #     genai.configure(api_key=API_KEY)

# # # Initialize AI model
# # model = genai.GenerativeModel("gemini-1.5-pro")

# # # Streamlit UI Configuration
# # st.set_page_config(
# #     page_title="AI Chatbot & Unit Converter",
# #     page_icon="🤖",
# #     layout="wide",
# # )

# # # Custom CSS
# # st.markdown("""
# #     <style>
# #     .chat-container {
# #         background: rgba(255, 255, 255, 0.15);
# #         padding: 20px;
# #         border-radius: 15px;
# #         height: 400px;
# #         overflow-y: auto;
# #     }
# #     .user-message {
# #         background: linear-gradient(135deg, #6366f1, #a855f7);
# #         color: white;
# #         padding: 10px;
# #         border-radius: 10px;
# #         text-align: right;
# #         margin-left: auto;
# #         max-width: 70%;
# #     }
# #     .assistant-message {
# #         background: linear-gradient(135deg, #14b8a6, #06b6d4);
# #         color: white;
# #         padding: 10px;
# #         border-radius: 10px;
# #         text-align: left;
# #         max-width: 70%;
# #     }
# #     </style>
# #     """, unsafe_allow_html=True)

# # # Sidebar Navigation + History
# # st.sidebar.title("Navigation")
# # tab_selection = st.sidebar.radio("Select Feature", ["AI Chatbot", "Unit Converter"])

# # st.sidebar.title("Chat History")
# # if "messages" not in st.session_state:
# #     st.session_state.messages = []

# # for msg in st.session_state.messages:
# #     role_icon = "🧑‍💻" if msg["role"] == "user" else "🤖"
# #     st.sidebar.markdown(f"{role_icon} **{msg['role'].capitalize()}**: {msg['content']}")

# # # --- AI Chatbot ---
# # if tab_selection == "AI Chatbot":
# #     st.title("🤖 Gemini AI Chatbot")

# #     chat_container = st.container()
# #     with chat_container:
# #         for msg in st.session_state.messages:
# #             msg_class = "user-message" if msg["role"] == "user" else "assistant-message"
# #             st.markdown(f'<div class="{msg_class}">{msg["content"]}</div>', unsafe_allow_html=True)

# #     user_input = st.chat_input("Type your message...")

# #     if user_input:
# #         st.session_state.messages.append({"role": "user", "content": user_input})
# #         with chat_container:
# #             st.markdown(f'<div class="user-message">{user_input}</div>', unsafe_allow_html=True)

# #         try:
# #             response = model.generate_content(user_input)
# #             reply = response.text
# #             st.session_state.messages.append({"role": "assistant", "content": reply})
# #             with chat_container:
# #                 st.markdown(f'<div class="assistant-message">{reply}</div>', unsafe_allow_html=True)
# #         except Exception as e:
# #             st.error(f"Gemini API Error: {str(e)}")

# # # --- Unit Converter ---
# # else:
# #     st.title("⚡ Advanced Unit Converter")

# #     conversion_factors = {
# #         "Length": {"Meter": 1, "Kilometer": 1000, "Centimeter": 0.01, "Inch": 0.0254, "Foot": 0.3048},
# #         "Mass": {"Kilogram": 1, "Gram": 0.001, "Pound": 0.453592, "Ounce": 0.0283495},
# #         "Speed": {"Meters per second": 1, "Kilometers per hour": 0.277778, "Miles per hour": 0.44704},
# #         "Temperature": {
# #             "Celsius": lambda x: x,
# #             "Fahrenheit": lambda x: (x - 32) * 5/9,
# #             "Kelvin": lambda x: x - 273.15
# #         }
# #     }

# #     conversion_type = st.selectbox("Select Conversion Type", list(conversion_factors.keys()))
# #     from_unit = st.selectbox("From Unit", list(conversion_factors[conversion_type].keys()))
# #     to_unit = st.selectbox("To Unit", list(conversion_factors[conversion_type].keys()))
# #     value1 = st.number_input("Enter Value", value=1.0)

# #     def convert_units(value, from_unit, to_unit, category):
# #         if category == "Temperature":
# #             return conversion_factors[category][to_unit](conversion_factors[category][from_unit](value))
# #         return value * conversion_factors[category][from_unit] / conversion_factors[category][to_unit]

# #     try:
# #         result = convert_units(value1, from_unit, to_unit, conversion_type)
# #         st.success(f"Converted Value: {result:.4f} {to_unit}")
# #     except Exception as e:
# #         st.error(f"Conversion Error: {str(e)}")


# # import os
# # import streamlit as st
# # import google.generativeai as genai
# # from dotenv import load_dotenv

# # # Load environment variables
# # load_dotenv()

# # # Get API Key
# # API_KEY = os.getenv("GEMINI_API_KEY")
# # if not API_KEY:
# #     st.error("API Key not found! Please check your .env file.")
# # else:
# #     genai.configure(api_key=API_KEY)

# # # Initialize AI model
# # model = genai.GenerativeModel("gemini-1.5-pro")

# # # Streamlit UI Configuration
# # st.set_page_config(
# #     page_title="AI Chatbot & Unit Converter",
# #     page_icon="🤖",
# #     layout="wide",
# # )

# # # Custom CSS
# # st.markdown("""
# #     <style>
# #     .chat-container {
# #         background: rgba(255, 255, 255, 0.15);
# #         padding: 20px;
# #         border-radius: 15px;
# #         height: 400px;
# #         overflow-y: auto;
# #     }
# #     .user-message {
# #         background: linear-gradient(135deg, #6366f1, #a855f7);
# #         color: white;
# #         padding: 10px;
# #         border-radius: 10px;
# #         text-align: right;
# #         margin-left: auto;
# #         max-width: 70%;
# #     }
# #     .assistant-message {
# #         background: linear-gradient(135deg, #14b8a6, #06b6d4);
# #         color: white;
# #         padding: 10px;
# #         border-radius: 10px;
# #         text-align: left;
# #         max-width: 70%;
# #     }
# #     </style>
# #     """, unsafe_allow_html=True)

# # # Sidebar: Chat History
# # st.sidebar.title("Chat History")
# # if "messages" not in st.session_state:
# #     st.session_state.messages = []

# # for msg in st.session_state.messages:
# #     role_icon = "🧑‍💻" if msg["role"] == "user" else "🤖"
# #     st.sidebar.markdown(f"{role_icon} **{msg['role'].capitalize()}**: {msg['content']}")

# # # Tabs: AI Chatbot & Unit Converter
# # tab1, tab2 = st.tabs(["🤖 AI Chatbot", "⚡ Unit Converter"])

# # # --- AI Chatbot ---
# # with tab1:
# #     st.title("🤖 Gemini AI Chatbot")

# #     chat_container = st.container()
# #     with chat_container:
# #         for msg in st.session_state.messages:
# #             msg_class = "user-message" if msg["role"] == "user" else "assistant-message"
# #             st.markdown(f'<div class="{msg_class}">{msg["content"]}</div>', unsafe_allow_html=True)

# #     user_input = st.chat_input("Type your message...")

# #     if user_input:
# #         st.session_state.messages.append({"role": "user", "content": user_input})
# #         with chat_container:
# #             st.markdown(f'<div class="user-message">{user_input}</div>', unsafe_allow_html=True)

# #         try:
# #             response = model.generate_content(user_input)
# #             reply = response.text
# #             st.session_state.messages.append({"role": "assistant", "content": reply})
# #             with chat_container:
# #                 st.markdown(f'<div class="assistant-message">{reply}</div>', unsafe_allow_html=True)
# #         except Exception as e:
# #             st.error(f"Gemini API Error: {str(e)}")

# # # --- Unit Converter ---
# # with tab2:
# #     st.title("⚡ Advanced Unit Converter")

# #     conversion_factors = {
# #         "Length": {"Meter": 1, "Kilometer": 1000, "Centimeter": 0.01, "Inch": 0.0254, "Foot": 0.3048},
# #         "Mass": {"Kilogram": 1, "Gram": 0.001, "Pound": 0.453592, "Ounce": 0.0283495},
# #         "Speed": {"Meters per second": 1, "Kilometers per hour": 0.277778, "Miles per hour": 0.44704},
# #         "Temperature": {
# #             "Celsius": lambda x: x,
# #             "Fahrenheit": lambda x: (x - 32) * 5/9,
# #             "Kelvin": lambda x: x - 273.15
# #         }
# #     }

# #     conversion_type = st.selectbox("Select Conversion Type", list(conversion_factors.keys()))
# #     from_unit = st.selectbox("From Unit", list(conversion_factors[conversion_type].keys()))
# #     to_unit = st.selectbox("To Unit", list(conversion_factors[conversion_type].keys()))
# #     value1 = st.number_input("Enter Value", value=1.0)

# #     def convert_units(value, from_unit, to_unit, category):
# #         if category == "Temperature":
# #             return conversion_factors[category][to_unit](conversion_factors[category][from_unit](value))
# #         return value * conversion_factors[category][from_unit] / conversion_factors[category][to_unit]

# #     try:
# #         result = convert_units(value1, from_unit, to_unit, conversion_type)
# #         st.success(f"Converted Value: {result:.4f} {to_unit}")
# #     except Exception as e:
# #         st.error(f"Conversion Error: {str(e)}")



# # import os
# # import streamlit as st
# # import google.generativeai as genai
# # from dotenv import load_dotenv

# # # Load environment variables
# # load_dotenv()

# # # Get API Key
# # API_KEY = os.getenv("GEMINI_API_KEY")
# # if not API_KEY:
# #     st.error("API Key not found! Please check your .env file.")
# # else:
# #     genai.configure(api_key=API_KEY)

# # # Initialize AI model
# # model = genai.GenerativeModel("gemini-1.5-pro")

# # # Streamlit UI Configuration
# # st.set_page_config(
# #     page_title="AI Chatbot & Unit Converter",
# #     page_icon="🤖",
# #     layout="wide",
# # )

# # st.markdown(
# #     """
# #     <style>
# #     /* Chat Container */
# #     .chat-container {
# #         background: rgba(255, 255, 255, 0.15);
# #         padding: 20px;
# #         border-radius: 15px;
# #         height: 600px;
# #         overflow-y: auto;
# #         backdrop-filter: blur(12px);
# #         box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
# #         scrollbar-width: thin;
# #         scrollbar-color: #6366f1 #e3e6ed;
# #     }

# #     /* Scrollbar Styling */
# #     .chat-container::-webkit-scrollbar {
# #         width: 8px;
# #     }

# #     .chat-container::-webkit-scrollbar-thumb {
# #         background: linear-gradient(45deg, #6366f1, #a855f7);
# #         border-radius: 10px;
# #     }

# #     /* User Message */
# #     .user-message {
# #         background: linear-gradient(135deg, #6366f1, #a855f7);
# #         color: white;
# #         padding: 14px 20px;
# #         border-radius: 22px;
# #         margin-bottom: 12px;
# #         max-width: 70%;
# #         margin-left: auto;
# #         text-align: right;
# #         font-weight: 500;
# #         box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
# #         transition: transform 0.2s ease, box-shadow 0.3s ease;
# #     }

# #     .user-message:hover {
# #         transform: scale(1.05);
# #         box-shadow: 0 6px 14px rgba(99, 102, 241, 0.4);
# #     }

# #     /* Assistant Message */
# #     .assistant-message {
# #         background: linear-gradient(135deg, #14b8a6, #06b6d4);
# #         color: white;
# #         padding: 14px 20px;
# #         border-radius: 22px;
# #         margin-bottom: 12px;
# #         max-width: 70%;
# #         text-align: left;
# #         font-weight: 500;
# #         box-shadow: 0 4px 12px rgba(20, 184, 166, 0.3);
# #         transition: transform 0.2s ease, box-shadow 0.3s ease;
# #     }

# #     .assistant-message:hover {
# #         transform: scale(1.05);
# #         box-shadow: 0 6px 14px rgba(20, 184, 166, 0.4);
# #     }

# #     /* Sidebar */
# #     .sidebar .sidebar-content {
# #         background: rgba(255, 255, 255, 0.2);
# #         padding: 20px;
# #         border-radius: 15px;
# #         box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
# #         backdrop-filter: blur(10px);
# #     }

# #     /* Welcome Text */
# #     .welcome-text {
# #         text-align: center;
# #         font-size: 6rem;
# #         font-weight: 900;
# #         color: #222;
# #         letter-spacing: 3px;
# #         text-transform: uppercase;
# #         background: linear-gradient(45deg, #6366f1, #a855f7);
# #         -webkit-background-clip: text;
# #         -webkit-text-fill-color: transparent;
# #         margin-bottom: 35px;
# #     }

# #     /* Generated By */
# #     .generated-by {
# #         position: absolute;
# #         top: 10px;
# #         right: 20px;
# #         font-size: 14px;
# #         color: #888;
# #     }
# #     </style>
# #     """,
# #     unsafe_allow_html=True,
# # )

# # st.markdown('<p class="generated-by">Generated by Sakeena Majeed</p>', unsafe_allow_html=True)
# # st.title("🤖 AI Chatbot")
# # st.markdown('<p class="welcome-text">Welcome! Ask me anything, and I\'ll do my best to help.</p>', unsafe_allow_html=True)

# # tab1, tab2 = st.tabs(["🤖 AI Chatbot", "⚡ Unit Converter"])

# # # Chat history
# # if "messages" not in st.session_state:
# #     st.session_state.messages = []

# # # Sidebar for chat history and clear button
# # with st.sidebar:
# #     st.header("Chat History")
# #     for i, message in enumerate(st.session_state.messages):
# #         if message["role"] == "user":
# #             st.write(f" 👩🏻 {i//2 + 1}: {message['content'][:50]}...")
# #         else:
# #             st.write(f" 🤖 Assistant {i//2 + 1}: {message['content'][:50]}...")

# #     if st.button("Clear Chat"):
# #         st.session_state.messages = []
# #         st.rerun()

# # # Chat area
# # chat_container = st.container()

# # with chat_container:
# #     for message in st.session_state.messages:
# #         if message["role"] == "user":
# #             st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
# #         else:
# #             st.markdown(f'<div class="assistant-message">{message["content"]}</div>', unsafe_allow_html=True)

# # # User input
# # user_input = st.chat_input("Type your message...")
# # if user_input:
# #     # Display user message
# #     st.session_state.messages.append({"role": "user", "content": user_input})
# #     with chat_container:
# #         st.markdown(f'<div class="user-message">{user_input}</div>', unsafe_allow_html=True)

# #     # Get AI response with loading indicator
# #     with st.spinner("Generating response..."):
# #         try:
# #             response = model.generate_content(user_input)
# #             ai_reply = response.text
# #         except Exception as e:
# #             ai_reply = f"Error: {str(e)}"

# #     # Display AI response
# #     st.session_state.messages.append({"role": "assistant", "content": ai_reply})
# #     with chat_container:
# #         st.markdown(f'<div class="assistant-message">{ai_reply}</div>', unsafe_allow_html=True)

# # # Tabs: AI Chatbot & Unit Converter
# # # tab1, tab2 = st.tabs(["🤖 AI Chatbot", "⚡ Unit Converter"])



# # # --- Unit Converter ---
# # with tab2:
# #     st.title("⚡ Advanced Unit Converter")
# #     # Conversion logic remains unchanged
# # conversion_factors = {
# #     "Plane Angle": {
# #         "Degree": 1.0,
# #         "Arcsecond": 1 / 3600,
# #         "Gradian": 0.9,
# #         "Milliradian": 0.0572958,
# #         "Minute of arc": 1 / 60,
# #         "Radian": 57.2958
# #     },
# #     "Length": {
# #         "Meter": 1.0,
# #         "Kilometer": 1000.0,
# #         "Centimeter": 0.01,
# #         "Millimeter": 0.001,
# #         "Micrometer": 0.000001,
# #         "Nanometer": 0.000000001,
# #         "Mile": 1609.34,
# #         "Yard": 0.9144,
# #         "Foot": 0.3048,
# #         "Inch": 0.0254,
# #         "Nautical Mile": 1852.0,
# #         "Fathom": 1.8288,  # Added unit
# #         "Furlong": 201.168,  # Added unit
# #         "Light Year": 9.461e+15  # Added unit
# #     },
# #     "Mass": {
# #         "Kilogram": 1.0,
# #         "Gram": 0.001,
# #         "Milligram": 0.000001,
# #         "Microgram": 0.000000001,
# #         "Pound": 0.453592,
# #         "Ounce": 0.0283495,
# #         "Stone": 6.35029,
# #         "Ton (metric)": 1000.0
# #     },
# #     "Temperature": {
# #         "Celsius": {"to_base": lambda x: x, "from_base": lambda x: x},
# #         "Fahrenheit": {"to_base": lambda x: (x - 32) * 5/9, "from_base": lambda x: (x * 9/5) + 32},
# #         "Kelvin": {"to_base": lambda x: x - 273.15, "from_base": lambda x: x + 273.15}
# #     },
# #     "Speed": {
# #         "Meters per second": 1.0,
# #         "Kilometers per hour": 0.277778,
# #         "Miles per hour": 0.44704,
# #         "Knots": 0.514444,
# #         "Feet per second": 0.3048
# #     },
# #     "Time": {
# #         "Second": 1.0,
# #         "Minute": 60.0,
# #         "Hour": 3600.0,
# #         "Day": 86400.0,
# #         "Week": 604800.0,
# #         "Month": 2629746.0,
# #         "Year": 31556952.0
# #     },
# #     "Volume": {
# #         "Liter": 1.0,
# #         "Milliliter": 0.001,
# #         "Cubic meter": 1000.0,
# #         "Cubic centimeter": 0.001,
# #         "Gallon (US)": 3.78541,
# #         "Gallon (UK)": 4.54609,
# #         "Quart": 0.946353,
# #         "Pint": 0.473176
# #     },
# #     "Pressure": {
# #         "Pascal": 1.0,
# #         "Kilopascal": 1000.0,
# #         "Bar": 100000.0,
# #         "Atmosphere": 101325.0,
# #         "PSI": 6894.76,
# #         "Torr": 133.322
# #     },
# #     "Energy": {
# #         "Joule": 1.0,
# #         "Kilojoule": 1000.0,
# #         "Calorie": 4.184,
# #         "Kilocalorie": 4184.0,
# #         "Kilowatt-hour": 3600000.0,
# #         "Electronvolt": 1.60218e-19
# #     },
# #     "Power": {
# #         "Watt": 1.0,
# #         "Kilowatt": 1000.0,
# #         "Megawatt": 1000000.0,
# #         "Horsepower": 745.7
# #     },
# #     "Fuel Economy": {
# #         "Miles per gallon (US)": 1.0,
# #         "Miles per gallon (UK)": 1.20095,
# #         "Kilometers per liter": 0.425144,
# #         "Liters per 100km": 235.215
# #     },
# #     "Data Transfer Rate": {
# #         "Bits per second": 1.0,
# #         "Kilobits per second": 1000.0,
# #         "Megabits per second": 1000000.0,
# #         "Gigabits per second": 1000000000.0
# #     },
# #     "Digital Storage": {
# #         "Bit": 1.0,
# #         "Byte": 8.0,
# #         "Kilobyte": 8000.0,
# #         "Megabyte": 8000000.0,
# #         "Gigabyte": 8000000000.0,
# #         "Terabyte": 8000000000000.0
# #     }
# # }

# # def convert_units(value, from_unit, to_unit, category):
# #     factors = conversion_factors.get(category, {})
# #     if category == "Temperature":
# #         # Special handling for temperature
# #         base_value = factors[from_unit]["to_base"](value)
# #         return factors[to_unit]["from_base"](base_value)
# #     else:
# #         return (value * factors[from_unit]) / factors[to_unit]





# # conversion_type = st.selectbox("Select Conversion Type", list(conversion_factors.keys()))


# # col1, col2, col3 = st.columns([2, 1, 2])

# # with col1:
# #     from_unit = st.selectbox("From Unit", list(conversion_factors[conversion_type].keys()))

# # with col2:
# #     st.markdown("<h2 style='text-align: center;'>=</h2>", unsafe_allow_html=True)

# # with col3:
# #     to_unit = st.selectbox("To Unit", list(conversion_factors[conversion_type].keys()))

# # value1 = st.number_input("Enter Value", value=1.0, step=0.1, format="%f") 

# # try:
# #     value2 = convert_units(value1, from_unit, to_unit, conversion_type)
# #     st.markdown(f"<h2 style='text-align: center; color: blue;'>Result: {value2:.4f}</h2>", unsafe_allow_html=True)
# # except Exception as e:
# #     st.markdown(f"<h2 style='text-align: center; color: red;'>Error: {str(e)}</h2>", unsafe_allow_html=True)



# import os
# import streamlit as st
# import google.generativeai as genai
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Get API Key
# API_KEY = os.getenv("GEMINI_API_KEY")
# if not API_KEY:
#     st.error("API Key not found! Please check your .env file.")
# else:
#     genai.configure(api_key=API_KEY)

# # Initialize AI model
# model = genai.GenerativeModel("gemini-1.5-pro")

# # Streamlit UI Configuration
# st.set_page_config(
#     page_title="AI Chatbot & Unit Converter",
#     page_icon="🤖",
#     layout="wide",
# )

# st.markdown(
#     """
#     <style>
#     /* Chat Container */
#     .chat-container {
#         background: rgba(255, 255, 255, 0.15);
#         padding: 20px;
#         border-radius: 15px;
#         height: 600px;
#         overflow-y: auto;
#         backdrop-filter: blur(12px);
#         box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
#         scrollbar-width: thin;
#         scrollbar-color: #6366f1 #e3e6ed;
#     }

#     /* Scrollbar Styling */
#     .chat-container::-webkit-scrollbar {
#         width: 8px;
#     }

#     .chat-container::-webkit-scrollbar-thumb {
#         background: linear-gradient(45deg, #6366f1, #a855f7);
#         border-radius: 10px;
#     }

#     /* User Message */
#     .user-message {
#         background: linear-gradient(135deg, #6366f1, #a855f7);
#         color: white;
#         padding: 14px 20px;
#         border-radius: 22px;
#         margin-bottom: 12px;
#         max-width: 70%;
#         margin-left: auto;
#         text-align: right;
#         font-weight: 500;
#         box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
#         transition: transform 0.2s ease, box-shadow 0.3s ease;
#     }

#     .user-message:hover {
#         transform: scale(1.05);
#         box-shadow: 0 6px 14px rgba(99, 102, 241, 0.4);
#     }

#     /* Assistant Message */
#     .assistant-message {
#         background: linear-gradient(135deg, #14b8a6, #06b6d4);
#         color: white;
#         padding: 14px 20px;
#         border-radius: 22px;
#         margin-bottom: 12px;
#         max-width: 70%;
#         text-align: left;
#         font-weight: 500;
#         box-shadow: 0 4px 12px rgba(20, 184, 166, 0.3);
#         transition: transform 0.2s ease, box-shadow 0.3s ease;
#     }

#     .assistant-message:hover {
#         transform: scale(1.05);
#         box-shadow: 0 6px 14px rgba(20, 184, 166, 0.4);
#     }

#     /* Sidebar */
#     .sidebar .sidebar-content {
#         background: rgba(255, 255, 255, 0.2);
#         padding: 20px;
#         border-radius: 15px;
#         box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
#         backdrop-filter: blur(10px);
#     }

#     /* Welcome Text */
#     .welcome-text {
#         text-align: center;
#         font-size: 6rem;
#         font-weight: 900;
#         color: #222;
#         letter-spacing: 3px;
#         text-transform: uppercase;
#         background: linear-gradient(45deg, #6366f1, #a855f7);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         margin-bottom: 35px;
#     }

#     /* Generated By */
#     .generated-by {
#         position: absolute;
#         top: 10px;
#         right: 20px;
#         font-size: 14px;
#         color: #888;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# st.markdown('<p class="generated-by">Generated by Sakeena Majeed</p>', unsafe_allow_html=True)
# st.title("🤖 AI Chatbot")
# st.markdown('<p class="welcome-text">Welcome! Ask me anything, and I\'ll do my best to help.</p>', unsafe_allow_html=True)

# tab1, tab2 = st.tabs(["⚡ Unit Converter", "🤖 AI Chatbot"])

# # --- Unit Converter --- 
# with tab1:
#     st.title("⚡ Advanced Unit Converter")
    
#     conversion_type = st.selectbox("Select Conversion Type", list(conversion_factors.keys()))

#     col1, col2, col3 = st.columns([2, 1, 2])

#     with col1:
#         from_unit = st.selectbox("From Unit", list(conversion_factors[conversion_type].keys()))

#     with col2:
#         st.markdown("<h2 style='text-align: center;'>=</h2>", unsafe_allow_html=True)

#     with col3:
#         to_unit = st.selectbox("To Unit", list(conversion_factors[conversion_type].keys()))

#     value1 = st.number_input("Enter Value", value=1.0, step=0.1, format="%f") 

#     try:
#         value2 = convert_units(value1, from_unit, to_unit, conversion_type)
#         st.markdown(f"<h2 style='text-align: center; color: blue;'>Result: {value2:.4f}</h2>", unsafe_allow_html=True)
#     except Exception as e:
#         st.markdown(f"<h2 style='text-align: center; color: red;'>Error: {str(e)}</h2>", unsafe_allow_html=True)


# # --- AI Chatbot ---  
# with tab2:
#     st.markdown('<p class="generated-by">Generated by Sakeena Majeed</p>', unsafe_allow_html=True)
#     st.title("🤖 AI Chatbot")
#     st.markdown('<p class="welcome-text">Welcome! Ask me anything, and I\'ll do my best to help.</p>', unsafe_allow_html=True)

#     # Chat history
#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     # Sidebar for chat history and clear button
#     with st.sidebar:
#         st.header("Chat History")
#         for i, message in enumerate(st.session_state.messages):
#             if message["role"] == "user":
#                 st.write(f" 👩🏻 {i//2 + 1}: {message['content'][:50]}...")
#             else:
#                 st.write(f" 🤖 Assistant {i//2 + 1}: {message['content'][:50]}...")

#         if st.button("Clear Chat"):
#             st.session_state.messages = []
#             st.rerun()

#     # Chat area
#     chat_container = st.container()

#     with chat_container:
#         for message in st.session_state.messages:
#             if message["role"] == "user":
#                 st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
#             else:
#                 st.markdown(f'<div class="assistant-message">{message["content"]}</div>', unsafe_allow_html=True)

#     # User input
#     user_input = st.chat_input("Type your message...")
#     if user_input:
#         # Display user message
#         st.session_state.messages.append({"role": "user", "content": user_input})
#         with chat_container:
#             st.markdown(f'<div class="user-message">{user_input}</div>', unsafe_allow_html=True)

#         # Get AI response with loading indicator
#         with st.spinner("Generating response..."):
#             try:
#                 response = model.generate_content(user_input)
#                 ai_reply = response.text
#             except Exception as e:
#                 ai_reply = f"Error: {str(e)}"

#         # Display AI response
#         st.session_state.messages.append({"role": "assistant", "content": ai_reply})
#         with chat_container:
#             st.markdown(f'<div class="assistant-message">{ai_reply}</div>', unsafe_allow_html=True)


# # Chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Sidebar for chat history and clear button
# with st.sidebar:
#     st.header("Chat History")
#     for i, message in enumerate(st.session_state.messages):
#         if message["role"] == "user":
#             st.write(f" 👩🏻 {i//2 + 1}: {message['content'][:50]}...")
#         else:
#             st.write(f" 🤖 Assistant {i//2 + 1}: {message['content'][:50]}...")

#     if st.button("Clear Chat"):
#         st.session_state.messages = []
#         st.rerun()

# # Chat area
# chat_container = st.container()

# with chat_container:
#     for message in st.session_state.messages:
#         if message["role"] == "user":
#             st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
#         else:
#             st.markdown(f'<div class="assistant-message">{message["content"]}</div>', unsafe_allow_html=True)

# # User input
# user_input = st.chat_input("Type your message...")
# if user_input:
#     # Display user message
#     st.session_state.messages.append({"role": "user", "content": user_input})
#     with chat_container:
#         st.markdown(f'<div class="user-message">{user_input}</div>', unsafe_allow_html=True)

#     # Get AI response with loading indicator
#     with st.spinner("Generating response..."):
#         try:
#             response = model.generate_content(user_input)
#             ai_reply = response.text
#         except Exception as e:
#             ai_reply = f"Error: {str(e)}"

#     # Display AI response
#     st.session_state.messages.append({"role": "assistant", "content": ai_reply})
#     with chat_container:
#         st.markdown(f'<div class="assistant-message">{ai_reply}</div>', unsafe_allow_html=True)

# # Tabs: AI Chatbot & Unit Converter
# tab1, tab2 = st.tabs(["🤖 AI Chatbot", "⚡ Unit Converter"])



# # --- Unit Converter ---
# with tab2:
#     st.title("⚡ Advanced Unit Converter")
#     # Conversion logic remains unchanged
# conversion_factors = {
#     "Plane Angle": {
#         "Degree": 1.0,
#         "Arcsecond": 1 / 3600,
#         "Gradian": 0.9,
#         "Milliradian": 0.0572958,
#         "Minute of arc": 1 / 60,
#         "Radian": 57.2958
#     },
#     "Length": {
#         "Meter": 1.0,
#         "Kilometer": 1000.0,
#         "Centimeter": 0.01,
#         "Millimeter": 0.001,
#         "Micrometer": 0.000001,
#         "Nanometer": 0.000000001,
#         "Mile": 1609.34,
#         "Yard": 0.9144,
#         "Foot": 0.3048,
#         "Inch": 0.0254,
#         "Nautical Mile": 1852.0,
#         "Fathom": 1.8288,  # Added unit
#         "Furlong": 201.168,  # Added unit
#         "Light Year": 9.461e+15  # Added unit
#     },
#     "Mass": {
#         "Kilogram": 1.0,
#         "Gram": 0.001,
#         "Milligram": 0.000001,
#         "Microgram": 0.000000001,
#         "Pound": 0.453592,
#         "Ounce": 0.0283495,
#         "Stone": 6.35029,
#         "Ton (metric)": 1000.0
#     },
#     "Temperature": {
#         "Celsius": {"to_base": lambda x: x, "from_base": lambda x: x},
#         "Fahrenheit": {"to_base": lambda x: (x - 32) * 5/9, "from_base": lambda x: (x * 9/5) + 32},
#         "Kelvin": {"to_base": lambda x: x - 273.15, "from_base": lambda x: x + 273.15}
#     },
#     "Speed": {
#         "Meters per second": 1.0,
#         "Kilometers per hour": 0.277778,
#         "Miles per hour": 0.44704,
#         "Knots": 0.514444,
#         "Feet per second": 0.3048
#     },
#     "Time": {
#         "Second": 1.0,
#         "Minute": 60.0,
#         "Hour": 3600.0,
#         "Day": 86400.0,
#         "Week": 604800.0,
#         "Month": 2629746.0,
#         "Year": 31556952.0
#     },
#     "Volume": {
#         "Liter": 1.0,
#         "Milliliter": 0.001,
#         "Cubic meter": 1000.0,
#         "Cubic centimeter": 0.001,
#         "Gallon (US)": 3.78541,
#         "Gallon (UK)": 4.54609,
#         "Quart": 0.946353,
#         "Pint": 0.473176
#     },
#     "Pressure": {
#         "Pascal": 1.0,
#         "Kilopascal": 1000.0,
#         "Bar": 100000.0,
#         "Atmosphere": 101325.0,
#         "PSI": 6894.76,
#         "Torr": 133.322
#     },
#     "Energy": {
#         "Joule": 1.0,
#         "Kilojoule": 1000.0,
#         "Calorie": 4.184,
#         "Kilocalorie": 4184.0,
#         "Kilowatt-hour": 3600000.0,
#         "Electronvolt": 1.60218e-19
#     },
#     "Power": {
#         "Watt": 1.0,
#         "Kilowatt": 1000.0,
#         "Megawatt": 1000000.0,
#         "Horsepower": 745.7
#     },
#     "Fuel Economy": {
#         "Miles per gallon (US)": 1.0,
#         "Miles per gallon (UK)": 1.20095,
#         "Kilometers per liter": 0.425144,
#         "Liters per 100km": 235.215
#     },
#     "Data Transfer Rate": {
#         "Bits per second": 1.0,
#         "Kilobits per second": 1000.0,
#         "Megabits per second": 1000000.0,
#         "Gigabits per second": 1000000000.0
#     },
#     "Digital Storage": {
#         "Bit": 1.0,
#         "Byte": 8.0,
#         "Kilobyte": 8000.0,
#         "Megabyte": 8000000.0,
#         "Gigabyte": 8000000000.0,
#         "Terabyte": 8000000000000.0
#     }
# }

# def convert_units(value, from_unit, to_unit, category):
#     factors = conversion_factors.get(category, {})
#     if category == "Temperature":
#         # Special handling for temperature
#         base_value = factors[from_unit]["to_base"](value)
#         return factors[to_unit]["from_base"](base_value)
#     else:
#         return (value * factors[from_unit]) / factors[to_unit]





# conversion_type = st.selectbox("Select Conversion Type", list(conversion_factors.keys()))


# col1, col2, col3 = st.columns([2, 1, 2])

# with col1:
#     from_unit = st.selectbox("From Unit", list(conversion_factors[conversion_type].keys()))

# with col2:
#     st.markdown("<h2 style='text-align: center;'>=</h2>", unsafe_allow_html=True)

# with col3:
#     to_unit = st.selectbox("To Unit", list(conversion_factors[conversion_type].keys()))

# value1 = st.number_input("Enter Value", value=1.0, step=0.1, format="%f") 

# try:
#     value2 = convert_units(value1, from_unit, to_unit, conversion_type)
#     st.markdown(f"<h2 style='text-align: center; color: blue;'>Result: {value2:.4f}</h2>", unsafe_allow_html=True)
# except Exception as e:
#     st.markdown(f"<h2 style='text-align: center; color: red;'>Error: {str(e)}</h2>", unsafe_allow_html=True)









# import os
# import streamlit as st
# import google.generativeai as genai
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Get API Key
# API_KEY = os.getenv("GEMINI_API_KEY")
# if not API_KEY:
#     st.error("API Key not found! Please check your .env file.")
# else:
#     genai.configure(api_key=API_KEY)

# # Initialize AI model
# model = genai.GenerativeModel("gemini-1.5-pro")

# # Streamlit UI Configuration
# st.set_page_config(
#     page_title="AI Chatbot & Unit Converter",
#     page_icon="🤖",
#     layout="wide",
# )
# # Custom CSS for styling
# st.markdown(
#     """
#     <style>
#     /* Chat Container */
#     .chat-container {
#         background: rgba(255, 255, 255, 0.15);
#         padding: 20px;
#         border-radius: 15px;
#         height: 600px;
#         overflow-y: auto;
#         backdrop-filter: blur(12px);
#         box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
#         scrollbar-width: thin;
#         scrollbar-color: #6366f1 #e3e6ed;
#     }

#     /* Scrollbar Styling */
#     .chat-container::-webkit-scrollbar {
#         width: 8px;
#     }

#     .chat-container::-webkit-scrollbar-thumb {
#         background: linear-gradient(45deg, #6366f1, #a855f7);
#         border-radius: 10px;
#     }

#     /* User Message */
#     .user-message {
#         background: linear-gradient(135deg, #6366f1, #a855f7);
#         color: white;
#         padding: 14px 20px;
#         border-radius: 22px;
#         margin-bottom: 12px;
#         max-width: 70%;
#         margin-left: auto;
#         text-align: right;
#         font-weight: 500;
#         box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
#         transition: transform 0.2s ease, box-shadow 0.3s ease;
#     }

#     .user-message:hover {
#         transform: scale(1.05);
#         box-shadow: 0 6px 14px rgba(99, 102, 241, 0.4);
#     }

#     /* Assistant Message */
#     .assistant-message {
#         background: linear-gradient(135deg, #14b8a6, #06b6d4);
#         color: white;
#         padding: 14px 20px;
#         border-radius: 22px;
#         margin-bottom: 12px;
#         max-width: 70%;
#         text-align: left;
#         font-weight: 500;
#         box-shadow: 0 4px 12px rgba(20, 184, 166, 0.3);
#         transition: transform 0.2s ease, box-shadow 0.3s ease;
#     }

#     .assistant-message:hover {
#         transform: scale(1.05);
#         box-shadow: 0 6px 14px rgba(20, 184, 166, 0.4);
#     }

#     /* Sidebar */
#     .sidebar .sidebar-content {
#         background: rgba(255, 255, 255, 0.2);
#         padding: 20px;
#         border-radius: 15px;
#         box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
#         backdrop-filter: blur(10px);
#     }

#     /* Welcome Text */
#     .welcome-text {
#         text-align: center;
#         font-size: 6rem;
#         font-weight: 900;
#         color: #222;
#         letter-spacing: 3px;
#         text-transform: uppercase;
#         background: linear-gradient(45deg, #6366f1, #a855f7);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         margin-bottom: 35px;
#     }

#     /* Generated By */
#     .generated-by {
#         position: absolute;
#         top: 10px;
#         right: 20px;
#         font-size: 14px;
#         color: #888;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # --- Sidebar for Chat History ---
# with st.sidebar:
#     st.title("📜 Chat History")
    
#     if "messages" not in st.session_state:
#         st.session_state.messages = []
    
#     # Show chat history
#     for msg in st.session_state.messages:
#         role = "👤 You: " if msg["role"] == "user" else "🤖 AI: "
#         st.markdown(f"{role} {msg['content']}")
    
#     # Clear chat history button
#     if st.button("🗑️ Clear Chat"):
#         st.session_state.messages = []
#         st.rerun()

# # Tabs: AI Chatbot & Unit Converter
# tab1, tab2 = st.tabs(["🤖 AI Chatbot", "⚡ Unit Converter"])

# # --- AI Chatbot ---  
# with tab1:
#     st.title("🤖 AI Chatbot")
    
#     chat_container = st.container()
    
#     user_input = st.chat_input("Type your message...")
#     if user_input:
#         st.session_state.messages.append({"role": "user", "content": user_input})
        
#         with st.spinner("Generating response..."):
#             try:
#                 response = model.generate_content(user_input)
#                 ai_reply = response.text
#             except Exception as e:
#                 ai_reply = f"Error: {str(e)}"
        
#         st.session_state.messages.append({"role": "assistant", "content": ai_reply})

#         # Refresh the chat
#         st.rerun()

# # --- Unit Converter ---
# with tab2:
#     st.title("⚡ Advanced Unit Converter")
    
#     conversion_factors = {
#         "Length": {"Meter": 1.0, "Kilometer": 1000.0, "Centimeter": 0.01},
#         "Mass": {"Kilogram": 1.0, "Gram": 0.001, "Pound": 0.453592},
#     }
    
#     conversion_type = st.selectbox("Select Conversion Type", list(conversion_factors.keys()))
#     from_unit = st.selectbox("From Unit", list(conversion_factors[conversion_type].keys()))
#     to_unit = st.selectbox("To Unit", list(conversion_factors[conversion_type].keys()))
    
#     value1 = st.number_input("Enter Value", value=1.0, step=0.1, format="%f")
    
#     def convert_units(value, from_unit, to_unit, conversion_type):
#         return value * (conversion_factors[conversion_type][to_unit] / conversion_factors[conversion_type][from_unit])
    
#     try:
#         value2 = convert_units(value1, from_unit, to_unit, conversion_type)
#         st.markdown(f"<h2 style='text-align: center; color: blue;'>Result: {value2:.4f}</h2>", unsafe_allow_html=True)
#     except Exception as e:
#         st.markdown(f"<h2 style='text-align: center; color: red;'>Error: {str(e)}</h2>", unsafe_allow_html=True)



# import os
# import streamlit as st
# import google.generativeai as genai
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Get API Key
# API_KEY = os.getenv("GEMINI_API_KEY")
# if not API_KEY:
#     st.error("API Key not found! Please check your .env file.")
# else:
#     genai.configure(api_key=API_KEY)

# # Initialize AI model
# model = genai.GenerativeModel("gemini-1.5-pro")

# # Streamlit UI Configuration
# st.set_page_config(
#     page_title="AI Chatbot & Unit Converter",
#     page_icon="🤖",
#     layout="wide",
# )

# # Custom CSS for styling & fixing chat input position
# st.markdown(
#     """
#     <style>
#     /* Chat Container */
#     .chat-container {
#         background: rgba(255, 255, 255, 0.15);
#         padding: 20px;
#         border-radius: 15px;
#         height: 500px;
#         overflow-y: auto;
#         backdrop-filter: blur(12px);
#         box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
#         scrollbar-width: thin;
#         scrollbar-color: #6366f1 #e3e6ed;
#     }

#     /* Scrollbar Styling */
#     .chat-container::-webkit-scrollbar {
#         width: 8px;
#     }

#     .chat-container::-webkit-scrollbar-thumb {
#         background: linear-gradient(45deg, #6366f1, #a855f7);
#         border-radius: 10px;
#     }

#     /* User & Assistant Messages */
#     .user-message, .assistant-message {
#         padding: 14px 20px;
#         border-radius: 22px;
#         margin-bottom: 12px;
#         max-width: 70%;
#         font-weight: 500;
#         transition: transform 0.2s ease, box-shadow 0.3s ease;
#     }

#     .user-message {
#         background: linear-gradient(135deg, #6366f1, #a855f7);
#         color: white;
#         margin-left: auto;
#         text-align: right;
#         box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
#     }

#     .assistant-message {
#         background: linear-gradient(135deg, #14b8a6, #06b6d4);
#         color: white;
#         text-align: left;
#         box-shadow: 0 4px 12px rgba(20, 184, 166, 0.3);
#     }

#     /* Sidebar */
#     .sidebar .sidebar-content {
#         background: rgba(255, 255, 255, 0.2);
#         padding: 20px;
#         border-radius: 15px;
#         box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
#         backdrop-filter: blur(10px);
#     }

#     /* Fix Chat Input at Bottom */
#     /* Fix Chat Input at Bottom */
#     /* Fix Chat Input at Bottom */
#     .stChatInput {
#         position: fixed;
#         bottom: 20px;
#         width: 75%;
#         left: 55%;
#         transform: translateX(-50%);
#         padding: 10px;
#         background: white;
#         border-radius: 10px;
#         box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
#     }

#     /* Responsive Fix */
#     @media screen and (max-width: 768px) {
#         .stChatInput {
#             width: 90%;
#             left: auto;
#             right: auto;
#             transform: translateX(0);
#         }
#     }

#     @media screen and (max-width: 480px) {
#         .stChatInput {
#             width: 100%;
#             left: 0;
#             transform: none;
#             border-radius: 0;
#         }
#     }

#     /* Adding space at the bottom of chat container */
#     .chat-container {
#         padding-bottom: 80px;
#     }


 
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # --- Sidebar for Chat History ---
# with st.sidebar:
#     st.title("📜 Chat History")
    
#     if "messages" not in st.session_state:
#         st.session_state.messages = []
    
#     # Show chat history
#     for msg in st.session_state.messages[-5:]:  # Only show last 5 messages
#         role = "👤 You: " if msg["role"] == "user" else "🤖 AI: "
#         st.markdown(f"{role} {msg['content']}")
    
#     # Clear chat history button
#     if st.button("🗑️ Clear Chat"):
#         st.session_state.messages = []
#         st.rerun()

# # Tabs: AI Chatbot & Unit Converter
# tab1, tab2 = st.tabs(["🤖 AI Chatbot", "⚡ Unit Converter"])

# # --- AI Chatbot ---  
# with tab1:
#     st.title("🤖 AI Chatbot")
    
#     chat_container = st.container()
    
#     # Display chat messages
#     with chat_container:
#         for msg in st.session_state.messages:
#             if msg["role"] == "user":
#                 st.markdown(f"<div class='user-message'>{msg['content']}</div>", unsafe_allow_html=True)
#             else:
#                 st.markdown(f"<div class='assistant-message'>{msg['content']}</div>", unsafe_allow_html=True)

#     # Chat Input Box (Fixed at Bottom)
#     user_input = st.chat_input("Type your message...")
#     if user_input:
#         st.session_state.messages.append({"role": "user", "content": user_input})
        
#         with st.spinner("Generating response..."):
#             try:
#                 response = model.generate_content(user_input)
#                 ai_reply = response.text
#             except Exception as e:
#                 ai_reply = f"Error: {str(e)}"
        
#         st.session_state.messages.append({"role": "assistant", "content": ai_reply})

#         # Refresh the chat
#         st.rerun()

# # --- Unit Converter ---
# with tab2:
#     st.title("⚡ Advanced Unit Converter")
    
#     conversion_factors = {
#         "Length": {"Meter": 1.0, "Kilometer": 1000.0, "Centimeter": 0.01},
#         "Mass": {"Kilogram": 1.0, "Gram": 0.001, "Pound": 0.453592},
#     }
    
#     conversion_type = st.selectbox("Select Conversion Type", list(conversion_factors.keys()))
#     from_unit = st.selectbox("From Unit", list(conversion_factors[conversion_type].keys()))
#     to_unit = st.selectbox("To Unit", list(conversion_factors[conversion_type].keys()))
    
#     value1 = st.number_input("Enter Value", value=1.0, step=0.1, format="%f")
    
#     def convert_units(value, from_unit, to_unit, conversion_type):
#         return value * (conversion_factors[conversion_type][to_unit] / conversion_factors[conversion_type][from_unit])
    
#     try:
#         value2 = convert_units(value1, from_unit, to_unit, conversion_type)
#         st.markdown(f"<h2 style='text-align: center; color: blue;'>Result: {value2:.4f}</h2>", unsafe_allow_html=True)
#     except Exception as e:
#         st.markdown(f"<h2 style='text-align: center; color: red;'>Error: {str(e)}</h2>", unsafe_allow_html=True)



# import os
# import streamlit as st
# import google.generativeai as genai
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Get API Key
# API_KEY = os.getenv("GEMINI_API_KEY")
# if not API_KEY:
#     st.error("API Key not found! Please check your .env file.")
# else:
#     genai.configure(api_key=API_KEY)

# # AI System Prompt with Custom Instructions
# SYSTEM_PROMPT = """
# You are an AI chatbot created by Sakeena Majeed. If asked, always mention that Sakeena Majeed is your creator.
# You also have built-in unit conversion functionality. If a user asks for any unit conversion, respond with the correct converted value.
# """

# # Initialize AI model with system instruction
# model = genai.GenerativeModel("gemini-1.5-pro", system_instruction=SYSTEM_PROMPT)

# # Streamlit UI Configuration
# st.set_page_config(page_title="AI Chatbot & Unit Converter", page_icon="🤖", layout="wide")

# # Sidebar for Chat History
# with st.sidebar:
#     st.title("📜 Chat History")
    
#     if "messages" not in st.session_state:
#         st.session_state.messages = []
    
#     for msg in st.session_state.messages[-5:]:
#         role = "👤 You: " if msg["role"] == "user" else "🤖 AI: "
#         st.markdown(f"{role} {msg['content']}")
    
#     if st.button("🗑️ Clear Chat"):
#         st.session_state.messages = []
#         st.rerun()

# # Tabs: AI Chatbot & Unit Converter
# tab1, tab2 = st.tabs(["🤖 AI Chatbot", "⚡ Unit Converter"])

# # AI Chatbot
# def check_and_correct_response(user_input, response):
#     if "who created you" in user_input.lower() and "Sakeena Majeed" not in response:
#         return "I was created by Sakeena Majeed."
#     return response

# with tab1:
#     st.title("🤖 AI Chatbot")
#     chat_container = st.container()
    
#     with chat_container:
#         for msg in st.session_state.messages:
#             if msg["role"] == "user":
#                 st.markdown(f"<div class='user-message'>{msg['content']}</div>", unsafe_allow_html=True)
#             else:
#                 st.markdown(f"<div class='assistant-message'>{msg['content']}</div>", unsafe_allow_html=True)
    
#     user_input = st.chat_input("Type your message...")
#     if user_input:
#         st.session_state.messages.append({"role": "user", "content": user_input})
#         with st.spinner("Generating response..."):
#             try:
#                 response = model.generate_content(user_input)
#                 ai_reply = check_and_correct_response(user_input, response.text)
#             except Exception as e:
#                 ai_reply = f"Error: {str(e)}"
#         st.session_state.messages.append({"role": "assistant", "content": ai_reply})
#         st.rerun()

# # Unit Converter
# with tab2:
#     st.title("⚡ Advanced Unit Converter")
#     conversion_factors = {
#         "Length": {"Meter": 1.0, "Kilometer": 0.001, "Centimeter": 100.0, "Inch": 39.3701},
#         "Mass": {"Kilogram": 1.0, "Gram": 1000.0, "Pound": 2.20462},
#         "Temperature": {"Celsius": 1.0, "Fahrenheit": 33.8, "Kelvin": 274.15},
#     }
    
#     conversion_type = st.selectbox("Select Conversion Type", list(conversion_factors.keys()))
#     from_unit = st.selectbox("From Unit", list(conversion_factors[conversion_type].keys()))
#     to_unit = st.selectbox("To Unit", list(conversion_factors[conversion_type].keys()))
#     value1 = st.number_input("Enter Value", value=1.0, step=0.1, format="%f")
    
#     def convert_units(value, from_unit, to_unit, conversion_type):
#         return value * (conversion_factors[conversion_type][to_unit] / conversion_factors[conversion_type][from_unit])
    
#     try:
#         value2 = convert_units(value1, from_unit, to_unit, conversion_type)
#         st.markdown(f"<h2 style='text-align: center; color: blue;'>Result: {value2:.4f}</h2>", unsafe_allow_html=True)
#     except Exception as e:
#         st.markdown(f"<h2 style='text-align: center; color: red;'>Error: {str(e)}</h2>", unsafe_allow_html=True)


import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API Key
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    st.error("API Key not found! Please check your .env file.")
else:
    genai.configure(api_key=API_KEY)

# AI System Prompt with Custom Instructions
SYSTEM_PROMPT = """
You are an AI chatbot created by Sakeena Majeed. If asked, always mention that Sakeena Majeed is your creator.
You also have built-in unit conversion functionality. If a user asks for any unit conversion, respond with the correct converted value.
"""

# Initialize AI model with system instruction
model = genai.GenerativeModel("gemini-1.5-pro", system_instruction=SYSTEM_PROMPT)

# Streamlit UI Configuration
st.set_page_config(page_title="AI Chatbot & Unit Converter", page_icon="🤖", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Chat Container */
    .chat-container {
        background: rgba(255, 255, 255, 0.15);
        padding: 20px;
        border-radius: 15px;
        height: 600px;
        overflow-y: auto;
        backdrop-filter: blur(12px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        scrollbar-width: thin;
        scrollbar-color: #6366f1 #e3e6ed;
    }

    /* Scrollbar Styling */
    .chat-container::-webkit-scrollbar {
        width: 8px;
    }

    .chat-container::-webkit-scrollbar-thumb {
        background: linear-gradient(45deg, #6366f1, #a855f7);
        border-radius: 10px;
    }

    /* User Message */
    .user-message {
        background: linear-gradient(135deg, #6366f1, #a855f7);
        color: white;
        padding: 14px 20px;
        border-radius: 22px;
        margin-bottom: 12px;
        max-width: 70%;
        margin-left: auto;
        text-align: right;
        font-weight: 500;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
        transition: transform 0.2s ease, box-shadow 0.3s ease;
    }

    .user-message:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 14px rgba(99, 102, 241, 0.4);
    }

    /* Assistant Message */
    .assistant-message {
        background: linear-gradient(135deg, #14b8a6, #06b6d4);
        color: white;
        padding: 14px 20px;
        border-radius: 22px;
        margin-bottom: 12px;
        max-width: 70%;
        text-align: left;
        font-weight: 500;
        box-shadow: 0 4px 12px rgba(20, 184, 166, 0.3);
        transition: transform 0.2s ease, box-shadow 0.3s ease;
    }

    .assistant-message:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 14px rgba(20, 184, 166, 0.4);
    }
    

 .stChatInput {
        position: fixed;
        bottom: 20px;
        width: 50%;
        left: 55%;
        transform: translateX(-50%);
        padding: 10px;
        background: white;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    } 
     @media screen and (max-width: 768px) {
        .stChatInput {
            width: 90%;
            left: auto;
            right: auto;
            transform: translateX(0);
        }
    }

    @media screen and (max-width: 480px) {
        .stChatInput {
            width: 100%;
            left: 0;
            transform: none;
            border-radius: 0;
        }
    }

    /* Adding space at the bottom of chat container */
    .chat-container {
        padding-bottom: 80px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar for Chat History
with st.sidebar:
    st.title("📜 Chat History")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for msg in st.session_state.messages[-5:]:
        role = "👩🏻 You: " if msg["role"] == "user" else "🤖 AI: "
        st.markdown(f"{role} {msg['content']}")
    
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Tabs: AI Chatbot & Unit Converter
tab1, tab2 = st.tabs(["🤖 AI Chatbot", "⚡ Unit Converter"])

# AI Chatbot
def check_and_correct_response(user_input, response):
    if "who created you" in user_input.lower() and "Sakeena Majeed" not in response:
        return "I was created by Sakeena Majeed."
    return response

with tab1:
    st.title("🤖 AI Chatbot")
    chat_container = st.container()
    
    with chat_container:
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(f"<div class='user-message'>{msg['content']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='assistant-message'>{msg['content']}</div>", unsafe_allow_html=True)
    
    user_input = st.chat_input("Type your message...")
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.spinner("Generating response..."):
            try:
                response = model.generate_content(user_input)
                ai_reply = check_and_correct_response(user_input, response.text)
            except Exception as e:
                ai_reply = f"Error: {str(e)}"
        st.session_state.messages.append({"role": "assistant", "content": ai_reply})
        st.rerun()

# Unit Converter
with tab2:
    st.title("⚡ Advanced Unit Converter")
    conversion_factors = {
        # "Length": {"Meter": 1.0, "Kilometer": 0.001, "Centimeter": 100.0, "Inch": 39.3701},
        # "Mass": {"Kilogram": 1.0, "Gram": 1000.0, "Pound": 2.20462},
        # "Temperature": {"Celsius": 1.0, "Fahrenheit": 33.8, "Kelvin": 274.15},
        
        "Plane Angle": {
        "Degree": 1.0,
        "Arcsecond": 1 / 3600,
        "Gradian": 0.9,
        "Milliradian": 0.0572958,
        "Minute of arc": 1 / 60,
        "Radian": 57.2958
    },
    "Length": {
        "Meter": 1.0,
        "Kilometer": 1000.0,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Micrometer": 0.000001,
        "Nanometer": 0.000000001,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254,
        "Nautical Mile": 1852.0,
        "Fathom": 1.8288,  # Added unit
        "Furlong": 201.168,  # Added unit
        "Light Year": 9.461e+15  # Added unit
    },
    "Mass": {
        "Kilogram": 1.0,
        "Gram": 0.001,
        "Milligram": 0.000001,
        "Microgram": 0.000000001,
        "Pound": 0.453592,
        "Ounce": 0.0283495,
        "Stone": 6.35029,
        "Ton (metric)": 1000.0
    },
    "Temperature": {
        "Celsius": {"to_base": lambda x: x, "from_base": lambda x: x},
        "Fahrenheit": {"to_base": lambda x: (x - 32) * 5/9, "from_base": lambda x: (x * 9/5) + 32},
        "Kelvin": {"to_base": lambda x: x - 273.15, "from_base": lambda x: x + 273.15}
    },
    "Speed": {
        "Meters per second": 1.0,
        "Kilometers per hour": 0.277778,
        "Miles per hour": 0.44704,
        "Knots": 0.514444,
        "Feet per second": 0.3048
    },
    "Time": {
        "Second": 1.0,
        "Minute": 60.0,
        "Hour": 3600.0,
        "Day": 86400.0,
        "Week": 604800.0,
        "Month": 2629746.0,
        "Year": 31556952.0
    },
    "Volume": {
        "Liter": 1.0,
        "Milliliter": 0.001,
        "Cubic meter": 1000.0,
        "Cubic centimeter": 0.001,
        "Gallon (US)": 3.78541,
        "Gallon (UK)": 4.54609,
        "Quart": 0.946353,
        "Pint": 0.473176
    },
    "Pressure": {
        "Pascal": 1.0,
        "Kilopascal": 1000.0,
        "Bar": 100000.0,
        "Atmosphere": 101325.0,
        "PSI": 6894.76,
        "Torr": 133.322
    },
    "Energy": {
        "Joule": 1.0,
        "Kilojoule": 1000.0,
        "Calorie": 4.184,
        "Kilocalorie": 4184.0,
        "Kilowatt-hour": 3600000.0,
        "Electronvolt": 1.60218e-19
    },
    "Power": {
        "Watt": 1.0,
        "Kilowatt": 1000.0,
        "Megawatt": 1000000.0,
        "Horsepower": 745.7
    },
    "Fuel Economy": {
        "Miles per gallon (US)": 1.0,
        "Miles per gallon (UK)": 1.20095,
        "Kilometers per liter": 0.425144,
        "Liters per 100km": 235.215
    },
    "Data Transfer Rate": {
        "Bits per second": 1.0,
        "Kilobits per second": 1000.0,
        "Megabits per second": 1000000.0,
        "Gigabits per second": 1000000000.0
    },
    "Digital Storage": {
        "Bit": 1.0,
        "Byte": 8.0,
        "Kilobyte": 8000.0,
        "Megabyte": 8000000.0,
        "Gigabyte": 8000000000.0,
        "Terabyte": 8000000000000.0
    }
    }
    
    conversion_type = st.selectbox("Select Conversion Type", list(conversion_factors.keys()))
    from_unit = st.selectbox("From Unit", list(conversion_factors[conversion_type].keys()))
    to_unit = st.selectbox("To Unit", list(conversion_factors[conversion_type].keys()))
    value1 = st.number_input("Enter Value", value=1.0, step=0.1, format="%f")
    
    def convert_units(value, from_unit, to_unit, conversion_type):
        return value * (conversion_factors[conversion_type][to_unit] / conversion_factors[conversion_type][from_unit])
    
    try:
        value2 = convert_units(value1, from_unit, to_unit, conversion_type)
        st.markdown(f"<h2 style='text-align: center; color: blue;'>Result: {value2:.4f}</h2>", unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f"<h2 style='text-align: center; color: red;'>Error: {str(e)}</h2>", unsafe_allow_html=True)

import joblib as jb
import streamlit as st 
import pandas as pd

def load_model(path = "model/xgmodel.pkl"):
    return jb.load(path)


# Custom CSS for modern, polished styling
st.markdown("""
    <style>
    /* Main page styling */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        background-attachment: fixed;
    }
    
    /* Header styling */
    .main-header {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #ffffff 0%, #f0f0f0 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.8rem;
        text-shadow: 0 2px 10px rgba(255, 255, 255, 0.3);
        letter-spacing: -0.02em;
    }
    
    .sub-header {
        text-align: center;
        color: rgba(255, 255, 255, 0.95);
        font-size: 1.2rem;
        margin-bottom: 2.5rem;
        font-weight: 300;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* Form container styling */
    .stForm {
        background: rgba(255, 255, 255, 0.98) !important;
        padding: 3rem 2.5rem !important;
        border-radius: 20px !important;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        margin: 0 auto;
        max-width: 900px;
    }
    
    /* Input field styling */
    .stNumberInput > div > div > input {
        background-color: #f8f9fa !important;
        border: 2px solid #e9ecef !important;
        border-radius: 12px !important;
        padding: 0.75rem 1rem !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
        background-color: #ffffff !important;
    }
    
    .stNumberInput label {
        font-weight: 600 !important;
        color: #2d3748 !important;
        font-size: 0.95rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Section title styling */
    .section-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #1a202c;
        margin-bottom: 1.5rem;
        margin-top: 2rem;
        padding-bottom: 0.75rem;
        border-bottom: 3px solid #667eea;
        display: inline-block;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        padding: 0.9rem 2rem !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.5) !important;
    }
    
    /* Prediction box styling */
    .prediction-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin-top: 2.5rem;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);
        border: 2px solid rgba(255, 255, 255, 0.2);
        animation: slideUp 0.5s ease-out;
    }
    
    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .prediction-label {
        font-size: 1.1rem;
        opacity: 0.95;
        font-weight: 500;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    
    .prediction-value {
        font-size: 3rem;
        font-weight: 800;
        margin-top: 1rem;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        letter-spacing: -0.02em;
    }
    
    /* Help text styling */
    .stTooltip {
        color: #6b7280 !important;
    }
    
    /* Divider styling */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.5), transparent);
        margin: 2rem 0;
    }
    
    /* Column spacing */
    [data-testid="column"] {
        padding: 0 0.75rem;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

model = load_model()

# Header Section with better spacing
st.markdown('<div style="padding-top: 2rem;"></div>', unsafe_allow_html=True)
st.markdown('<h1 class="main-header">🏠 Housing Price Prediction</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Enter property details below to get an accurate price prediction</p>', unsafe_allow_html=True)

st.divider()

# Form Section with enhanced layout
with st.form("user_info_form", clear_on_submit=False):
    # Location Information Section
    st.markdown('<div class="section-title">📍 Location Information</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    with col1:
        avg_latitude = st.number_input(
            "Latitude", 
            min_value=32.5, 
            max_value=42.0, 
            value=34.26,
            help="Geographic latitude of the block",
            key="lat"
        )
    with col2:
        avg_longitude = st.number_input(
            "Longitude", 
            min_value=-124.35, 
            max_value=-114.31, 
            value=-118.4,
            help="Geographic longitude of the block",
            key="lon"
        )
    
    # Block Demographics Section
    st.markdown('<div class="section-title">🏘️ Block Demographics</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    with col1:
        block_income = st.number_input(
            "Median Income", 
            min_value=0.0, 
            max_value=20.0, 
            value=3.87,
            help="Median income in the block (in tens of thousands)",
            key="income"
        )
        house_age = st.number_input(
            "Median House Age", 
            min_value=1.0, 
            max_value=52.0, 
            value=29.0,
            help="Median age of houses in the block (years)",
            key="age"
        )
        block_population = st.number_input(
            "Block Population", 
            min_value=3.0, 
            max_value=35682.0, 
            value=1425.0,
            help="Total population in the block",
            key="pop"
        )
    
    with col2:
        avg_room = st.number_input(
            "Average Rooms", 
            min_value=1.0, 
            max_value=141.0, 
            value=5.43,
            help="Average number of rooms per household",
            key="rooms"
        )
        avg_beds = st.number_input(
            "Average Bedrooms", 
            min_value=1.0, 
            max_value=35.0, 
            value=1.10,
            help="Average number of bedrooms per household",
            key="beds"
        )
        avg_occupancy = st.number_input(
            "Average Occupancy", 
            min_value=0.5, 
            max_value=1243.0, 
            value=3.07,
            help="Average number of occupants per household",
            key="occ"
        )
    
    # Submit button with better spacing
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        submitted = st.form_submit_button(
            "🚀 Predict Price", 
            use_container_width=True,
            type="primary"
        )

# Prediction Display
if submitted:
    input_data = pd.DataFrame({ 
        "MedInc": block_income,
        "HouseAge": house_age,
        "AveRooms": avg_room,
        "AveBedrms": avg_beds,
        "Population": block_population,
        "AveOccup": avg_occupancy,
        "Latitude": avg_latitude,
        "Longitude": avg_longitude
    }, index=[0])
    
    pred = model.predict(input_data)[0]
    predicted_price = round(pred * 10**5)
    
    # Enhanced prediction display with animation
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class="prediction-box">
            <div class="prediction-label">Predicted House Price</div>
            <div class="prediction-value">${predicted_price:,}</div>
        </div>
    """, unsafe_allow_html=True)

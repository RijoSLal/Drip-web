import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import os
import google.generativeai as genai


genai.configure(api_key=os.environ.get("API_KEY", "your api key"))

# Streamlit app title
st.title("Ⓓ🅡🅐🅦🅘🅝🅖 Ⓡ🅔🅒🅞🅖🅝🅘🅣🅘🅞🅝 Ⓘ🅝🅣🅔🅛🅛🅘🅖🅔🅝🅣 Ⓟ🅡🅞🅖🅡🅐🅜🅜🅔")

# Sidebar settings
st.sidebar.markdown("### Settings")
stroke_color = st.sidebar.color_picker("Pick a Stroke color", "#FFFFFF")
stroke_width = st.sidebar.slider("Select Stroke width", 1, 20, 3)

# Add eraser functionality
eraser_mode = st.sidebar.checkbox("Wiper")

# If eraser mode is enabled, stroke color is set to background color
if eraser_mode:
    stroke_color = "black"


canvas_result = st_canvas(
    fill_color="black", 
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color="black",
    height=500,
    width=int(st.sidebar.slider("Canvas Width (%)", 50, 100, 100) * 5),
    drawing_mode="freedraw",
    key="canvas",
)

# Create a container for the AI response
response_container = st.container()

# Create a responsive layout
col1, col2 = st.columns([3, 1])  # Adjust the proportions as needed

with col1:
    # Placeholder for response text
    response_box = response_container.empty()
    
    # Initial response message
    response_message = "Response will appear here..."
    response_box.markdown(
        f"<div style='border: 2px solid #ccc; border-radius: 10px; padding: 10px; margin-bottom: 20px;'>{response_message}</div>",
        unsafe_allow_html=True
    )

    # Button to save the canvas as an image and generate AI content
    if st.button("Generate"):
        if canvas_result.image_data is not None:
            img = Image.fromarray(canvas_result.image_data.astype("uint8"), "RGBA")
            
  
            home_directory = os.path.expanduser("~")
            file_path = os.path.join(home_directory, "image.png")
            img.save(file_path)

           
            response_message = "Generating response..."
            response_box.markdown(
                f"<div style='border: 2px solid #ccc; border-radius: 10px; padding: 10px; margin-bottom: 20px;'>{response_message}</div>",
                unsafe_allow_html=True
            )
            try:
                model = genai.GenerativeModel(model_name="gemini-1.5-flash")
                response = model.generate_content(["What is the answer?", img])
                
           
                response_message = response.text
                response_box.markdown(
                    f"<div style='border: 2px solid #ccc; border-radius: 10px; padding: 10px; margin-bottom: 20px;'>{response_message}</div>", 
                    unsafe_allow_html=True
                )
            except Exception as e:
                response_message = f"Error generating AI response: {e}"
                response_box.markdown(
                    f"<div style='border: 2px solid #ccc; border-radius: 10px; padding: 10px; margin-bottom: 20px;'>{response_message}</div>", 
                    unsafe_allow_html=True
                )
        else:
            response_message = "Please draw something on the canvas!"
            response_box.markdown(
                f"<div style='border: 2px solid #ccc; border-radius: 10px; padding: 10px; margin-bottom: 20px;'>{response_message}</div>", 
                unsafe_allow_html=True
            )

with col2:
    pass


st.sidebar.markdown("---")
st.sidebar.write("Use the drawing tools on the sidebar to start creating! Toggle the wiper for corrections")
st.markdown("<footer style='text-align: left; margin-top: 20px;'>© 🅡🅘🅙🅞 🅢 🅛🅐🅛</footer>", unsafe_allow_html=True)

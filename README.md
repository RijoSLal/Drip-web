# DRIP 🎨 - Drawing Recognition Intelligent Programme

## Introduction

DRIP is a sophisticated web application developed using Streamlit, designed to enable users to create drawings and generate intelligent responses through Google's Generative AI. This project leverages advanced technologies to provide a seamless and interactive user experience.

## Key Features

- **Interactive Drawing Canvas**: Users can freely create artwork using various brush settings.
- **Customizable Drawing Tools**: Choose from an array of stroke colors and widths tailored to individual preferences.
- **Eraser Functionality**: Easily correct mistakes with an integrated eraser tool.
- **AI-Driven Insights**: Generates contextual responses based on the user's drawings.
- **Responsive Design**: Optimized for a variety of screen sizes, ensuring accessibility on mobile and desktop devices.

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install Required Packages**:
   ```bash
   pip install streamlit streamlit-drawable-canvas pillow google-generativeai
   ```

4. **Configure Google Generative AI API Key**:
   - Insert your API key in the code or set it in your environment variables:
   ```bash
   export API_KEY="your_api_key_here"  # On Windows use `set API_KEY=your_api_key_here`
   ```

## Usage

1. **Launch the Application**:
   ```bash
   streamlit run app.py  # Replace `app.py` with the name of your script
   ```

2. **Access the Application**:
   - Open a web browser and navigate to `http://localhost:8501`.

3. **User Interaction**:
   - Utilize the drawing tools in the sidebar to create drawings.
   - Click the "Generate" button to obtain an AI-generated response based on your artwork.

## Contributing

Contributions are encouraged to enhance the functionality and performance of the application. Please open an issue or submit a pull request for any suggestions or improvements.


## Acknowledgments

- **Streamlit**: A powerful framework for building interactive data applications.
- **Google Generative AI**: For providing robust AI capabilities that enhance user experience.

## Contact

For inquiries or further information, please contact Rijo S Lal at linkdin.

---

Feel free to modify any specific details such as repository URLs, your name, or contact information as needed!

🖼️ Image Analytics using Gemini AI

An AI-powered Image Analytics web application built with Google Gemini (Generative AI) and Streamlit.
The app allows users to upload an image, enter a custom prompt, and receive AI-generated insights or descriptions based on the image content.

🚀 Project Features

📷 Upload images (jpg, png, jpeg)

✍️ Enter custom text prompts

🤖 Uses Google Gemini 2.5 Flash model

⚡ Fast AI-based image understanding

🌐 Interactive Streamlit web interface

🔐 Secure API key handling using .env

🧠 How It Works

User uploads an image

User enters a text prompt (e.g. “Describe the image”)

The image + prompt are sent to Gemini AI

Gemini analyzes the image and generates a response

The response is displayed on the web app

🧑‍💻 Tech Stack

Python

Google Generative AI (Gemini)

Streamlit

PIL (Pillow)

python-dotenv

🗂️ Project Structure
Image-Analytics-Using-Gemini/
│
├── app.py               # Streamlit application
├── .env                 # API key (not pushed to GitHub)
├── requirements.txt     # Dependencies
└── README.md

🔑 Environment Setup
1️⃣ Create a .env file

Create a file named .env in the project root and add:

api=YOUR_GEMINI_API_KEY


⚠️ Do NOT upload .env to GitHub

📦 Install Dependencies
pip install -r requirements.txt

▶️ Run the Application
python -m streamlit run app.py


Then open in browser:

http://localhost:8501

🧪 Example Use Cases

Describe an uploaded image

Identify objects in an image

Generate captions

Analyze visual content with custom prompts

Educational & demo AI applications

🧠 Model Used

Gemini 2.5 Flash

Optimized for:

Fast inference

Multimodal input (text + image)

Real-time applications

⚠️ Important Notes

Ensure a valid Gemini API key

Internet connection required

Large images may take slightly longer to process

Prompt quality directly affects output quality

📌 Future Improvements

Image preprocessing & resizing

Multi-image support

Prompt templates

Downloadable responses

Deployment on Streamlit Cloud

🎯 Interview Talking Points

How multimodal models work (text + image)

Gemini vs GPT vision models

Secure API key management

Streamlit for rapid AI prototyping

Real-world use cases of image analytics

👤 Author

Om Nemade
Aspiring Data Scientist | AI & GenAI Enthusiast

⭐ If you like this project

Give it a ⭐ on GitHub — it helps a lot!

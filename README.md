# **NeuroWheels - AI Doctor for Mobility Support**

## **Overview**

**NeuroWheels** is an AI-powered application designed to provide support to individuals with mobility impairments. It leverages **GPT-3.5 Turbo** to offer real-time, compassionate, and professional responses to user inquiries, acting as a virtual assistant and offering personalized advice and emotional support. The app also includes features like real-time biofeedback monitoring, sign-up/log-in functionality, and upgrade options for additional features and hardware.

## **Features**

* **NeuroGuide (AI Chatbot)**: A GPT-3.5 Turbo-powered assistant providing empathetic, professional responses tailored to mobility challenges.
* **Real-Time Biofeedback Dashboard**: Simulated EEG, heart rate, breathing rate, and stress level monitoring.
* **User Authentication**: Secure sign-up and login system for personalized user experiences.
* **Upgrade Options**: Premium features and additional hardware like robotic arms and tablets.
* **Streamlit Interface**: Easy-to-use web interface connected to GitHub for version control and easy updates.

## **Tech Stack**

* **Streamlit**: For building the web app and handling user interactions.
* **OpenAI API (GPT-3.5 Turbo)**: For conversational AI, offering real-time, contextually accurate responses.
* **PyTorch**: For handling model deployment and managing computation on **CPU**/ **GPU**.
* **GitHub**: For version control and collaboration.
* **JSON**: For storing user data locally.

## **Installation and Setup**

### **1. Clone the Repository**

```bash
git clone https://github.com/your-username/neuro-wheels.git
cd neuro-wheels
```

### **2. Install Dependencies**

Make sure you have Python 3.7 or later installed. You can use `pip` to install the required dependencies.

```bash
pip install -r requirements.txt
```

### **3. Set Up OpenAI API Key**

1. Sign up for an **OpenAI** account if you don't have one: [OpenAI API](https://beta.openai.com/signup/).
2. Create an API key in the OpenAI dashboard.
3. Store your **API key** securely in the **Streamlit secrets** file:

   **.streamlit/secrets.toml**

   ```toml
   [general]
   OPENAI_API_KEY = "your-openai-api-key"
   ```

### **4. Run the App**

To run the app locally, simply use the following command:

```bash
streamlit run app.py
```

Your app will now be live at `http://localhost:8501/` in your web browser.

## **Important Notes**

* This app uses **OpenAI’s GPT-3.5 Turbo**, which requires an active internet connection and a valid API key to function.
* You can modify the **doctor prompt** in the code to customize the chatbot’s responses according to your needs.
* For ease of implementation and collaboration, the app is connected to **GitHub**, allowing for version control and easy updates.

## **Contributing**

We welcome contributions to **NeuroWheels**. If you'd like to contribute, please fork the repository, make your changes, and submit a pull request. Be sure to follow the guidelines and provide clear descriptions of the changes made.

Streamlit Link:
https://neuroguide.streamlit.app/Authentication


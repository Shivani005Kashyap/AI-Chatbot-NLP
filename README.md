🤖 AI Chatbot using NLP, Flask & React

A simple AI-powered chatbot built using **Python (Flask), NLP (NLTK), TensorFlow, and React.js**.  
It uses a trained machine learning model to understand user inputs and generate responses using intents + smart fallback logic.



 🚀 Features

- 🧠 Intent-based NLP chatbot
- 🤖 Machine Learning model (TensorFlow)
- ⚡ Smart rule-based responses (time, name, help, etc.)
- 🌐 React frontend chat UI
- 🔗 Flask REST API backend
- 🔄 Real-time communication using Axios
- 💾 Chat history stored in browser (localStorage)



🛠️ Tech Stack

Frontend
- React.js
- JavaScript
- Axios
- CSS

Backend
- Python
- Flask
- Flask-CORS

AI / NLP
- NLTK (tokenization, stemming)
- TensorFlow (Neural Network)
- NumPy
- Joblib

 📁 Project Structure

AI-Chatbot/
│
├── backend/
│   ├── app.py
│   ├── train.py
│   ├── predict.py
│   ├── model.py
│   ├── nltk_utils.py
│   ├── intents.json
│   ├── chatbot_model.keras
│   ├── words.pkl
│   └── tags.pkl
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   ├── styles/
│   │   └── App.jsx
│
└── README.md



 ⚙️ Installation & Setup
 
 1 Backend Setup (Flask)

```bash
cd backend
pip install -r requirements.txt
python app.py
```

Backend runs at:

```
http://127.0.0.1:5000
```



 3️2 Frontend Setup (React)

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```



 🔗 API Endpoint

 Chat API

```
POST /chat
```

 Request:

```json
{
  "message": "hello"
}
```

 Response:

```json
{
  "response": "Hi there! How can I help you today?"
}
```

---

🧠 How It Works

1. User sends message from React frontend
2. Message is sent to Flask backend
3. NLP model processes input
4. Intent is predicted using trained model
5. Response is selected from intents.json
6. Bot response is returned to frontend

---

💡 Future Improvements

* 🔥 Add OpenAI API integration
* 🔥 Voice chatbot support
* 🔥 User authentication
* 🔥 Improve NLP using transformers
* 🔥 Deploy full stack project online

---

👩‍💻 Author

**Shivani**
MCA (AI & ML) Student
Full Stack + AI Developer (Learning Phase)

---

⭐ If you like this project
Give a ⭐ on GitHub and feel free to fork it!

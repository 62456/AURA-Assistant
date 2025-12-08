# AURA-Assistant

# AURA-Assistant

**AURA-Assistant** is a simple Python-based chatbot / assistant project. It uses a trained model (together with intent definitions) to respond to user inputs. The project includes a GUI (and optionally a web front-end) for interacting with the assistant.  

> ⚠️ **Note:** This is a lightweight / early-stage project. The repository does not have extensive documentation or wide usage yet.  

---

## 🧰 What’s Inside / Structure

The repository currently contains:

- `app.py`, `main.py`, `gui.py` — core Python scripts for running the assistant / GUI / main logic.  
- `model_train.py`, `model_test.py` — scripts for training and testing the underlying model.  
- `intents.json` — intent definitions / patterns & responses for the assistant.  
- `tokenizer.pkl`, `label_encoder.pkl`, `chat_model.h5` — trained model artifacts / serialized tokenizer & label encoder.  
- `index.html` — (optional) front-end / web interface.  
- Other supporting files.  

From GitHub’s language breakdown, the repo uses both **Python** and **HTML**. :contentReference[oaicite:0]{index=0}

---

## ✅ What It Does (Features / Purpose)

- Acts as a simple chatbot / assistant using predefined intents + a trained model.  
- Supports a GUI (or web-based interface) for user interaction.  
- Provides training and testing scripts — so you can retrain / customize intents or add new features.  
- Good as a **learning / experimental** baseline: if you want a small, offline-style assistant, and you’re okay tinkering with code.  

---

## 🚀 How to Run / Use It

Here’s a basic guide to get started:

```bash
# 1. Clone the repo
git clone https://github.com/62456/AURA-Assistant.git
cd AURA-Assistant

# 2. (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
# venv\Scripts\activate    # Windows

# 3. Install dependencies 
# (You’ll need to inspect the code to see which libraries are used — e.g. for ML, GUI, etc.)

# 4. Run the assistant
python app.py       # or `python main.py`, depending on which script is the entry point

# MathGenius - Setup Guide 🚀

## ⭐ COMPLETELY FREE - No API Keys Needed!

MathGenius now uses **Ollama** - a free, open-source AI that runs locally on your computer.

---

## Step 1: Install Ollama

### Windows & Mac:
1. Download from: https://ollama.ai
2. Install and run the app
3. Keep it running in background

### Linux:
```bash
curl https://ollama.ai/install.sh | sh
ollama serve  # Keep this running
```

---

## Step 2: Download a Free AI Model

Open a **new terminal/command prompt** and run:

```bash
ollama pull mistral
```

This downloads Mistral (fast, good for math). Other free options:
- `ollama pull neural-chat` (even faster)
- `ollama pull orca-mini` (smaller, less accurate)

---

## Step 3: Clone the Repository

```bash
git clone https://github.com/Aetherion108/MathGenius.git
cd MathGenius
```

---

## Step 4: Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 5: Run MathGenius

Make sure Ollama is still running, then:

```bash
python main.py
```

---

## Step 6: Ask Your First Problem!

Example problems:
- "Solve x² - 5x + 6 = 0"
- "Prove that √2 is irrational"
- "What is the derivative of e^x sin(x)?"
- "Explain the quadratic formula"

---

## Troubleshooting

### "Connection refused" or "Ollama not running"
- Make sure Ollama app/service is running
- Windows/Mac: Open Ollama app
- Linux: Run `ollama serve` in a terminal

### "Model not found"
- Run: `ollama pull mistral`
- Wait for download to complete (1-2 GB)

### "Timeout: Model is taking too long"
- Use a smaller model: `ollama pull neural-chat`
- Try simpler problems first

### Still having issues?
- Check Python 3.8+ is installed: `python --version`
- Reinstall dependencies: `pip install --upgrade -r requirements.txt`
- Restart Ollama

---

## How It Works

1. **You enter a math problem** ➜ Any complexity level
2. **Local AI analyzes the problem** ➜ Runs on your computer (FREE!)
3. **Step-by-step solution** ➜ Every step explained
4. **Verification** ➜ Checks if answer is correct
5. **Follow-up help** ➜ Ask more questions

---

## Switching to OpenAI (Optional - Costs Money)

If you have OpenAI API credits:

1. Get API key from: https://platform.openai.com/api-keys
2. Create `.env` file:
   ```
   OPENAI_API_KEY=sk-your_key_here
   ```
3. Edit `config.py` - change `USE_LOCAL_MODEL = True` to `False`
4. Run: `python main.py`

---

## Publishing/Hosting MathGenius

### Option 1: Docker (Run Anywhere)
```bash
docker build -t mathgenius .
docker run -p 8000:8000 mathgenius
```

### Option 2: GitHub Pages (Free)
Push to GitHub, enable Pages in repository settings

### Option 3: Heroku / Railway (Free tier available)
Deploy the repo with built-in Python support

---

## Tips for Best Results

✅ Be clear about what you need  
✅ Mention if it's JEE/ICSE/Olympiad level  
✅ Ask for specific concepts you don't understand  
✅ Use follow-up questions for deeper learning  

---

## Cost Breakdown

| Component | Cost |
|-----------|------|
| Ollama | FREE ✅ |
| Mistral Model | FREE ✅ |
| MathGenius Code | FREE ✅ |
| **Total** | **$0** ✅ |

---

Happy learning! 🎓 No money spent! 🚀

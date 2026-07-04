# MathGenius - Setup Guide 🚀

## Step 1: Install Python

Make sure you have Python 3.8 or higher:
```bash
python --version
```

## Step 2: Clone the Repository

```bash
git clone https://github.com/Aetherion108/MathGenius.git
cd MathGenius
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Get OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Sign up or log in
3. Click "Create new secret key"
4. Copy the key (save it somewhere safe!)
5. You'll get **$5 free credits** to start

## Step 5: Create .env File

Create a file named `.env` in the MathGenius folder:

```
OPENAI_API_KEY=sk-your_actual_key_here
```

Replace `sk-your_actual_key_here` with your real API key.

⚠️ **Important**: Never share this key publicly or commit it to GitHub!

## Step 6: Run MathGenius

```bash
python main.py
```

## Step 7: Ask Your First Problem!

Example problems:
- "Solve x² - 5x + 6 = 0"
- "Prove that √2 is irrational"
- "What is the derivative of e^x sin(x)?"
- "Explain the quadratic formula"

---

## Troubleshooting

### "OPENAI_API_KEY not found"
- Make sure `.env` file exists in the MathGenius folder
- Check spelling: it should be exactly `OPENAI_API_KEY`
- Make sure you copied the key correctly from OpenAI

### "Invalid API key"
- Check if your key starts with `sk-`
- Make sure you didn't accidentally add spaces
- Try generating a new key from the OpenAI website

### "Rate limit exceeded"
- You've used up your $5 free credits
- Add a payment method to your OpenAI account to continue
- Pricing: ~$0.002 per problem on average

### Still having issues?
- Check your internet connection
- Make sure Python 3.8+ is installed
- Try: `pip install --upgrade openai`

---

## How It Works

1. **You enter a math problem** ➜ Any complexity level
2. **AI analyzes the problem** ➜ Decides the best approach
3. **Step-by-step solution** ➜ Every step explained simply
4. **Verification** ➜ Checks if answer is correct
5. **Follow-up help** ➜ Ask more questions

---

## Tips for Best Results

✅ Be clear about what you need  
✅ Mention if it's JEE/ICSE/Olympiad level  
✅ Ask for specific concepts you don't understand  
✅ Use follow-up questions for deeper learning  

---

Happy learning! 🎓

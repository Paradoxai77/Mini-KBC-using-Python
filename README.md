# 💰 Mini KBC (Kaun Banega Crorepati) Game in Python

Welcome to the **Mini KBC Game**! This is a fun, interactive command-line Python quiz game inspired by the popular television show *Kaun Banega Crorepati* (Who Wants to Be a Millionaire?).

## ✨ Features

- **Randomized Questions**: Dynamically selects 10 random questions from a built-in question bank.
- **Multiple Choice**: Each question provides four options (A, B, C, D).
- **Lifelines**: Just like the real show, you have four lifelines to help you when you're stuck:
  - 🎭 **50:50**: Removes two incorrect options, leaving you with one correct and one incorrect option.
  - 📊 **Audience Poll**: Suggests the correct answer.
  - 📞 **Phone a Friend**: Gets a friend's opinion on the correct answer.
  - 🔄 **Flip the Question**: Skips the current question and gives you a new one.
- **Time Limit**: You have **20 seconds** to answer each question, adding to the thrill!
- **Prize Money**: The prize money increases with every correct answer you give.

## 🚀 How to Play

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Paradoxai77/How-much-Money-you-will-take-code-using-Python.git
   cd How-much-Money-you-will-take-code-using-Python
   ```

2. **Run the game**:
   Make sure you have Python installed, then run the script from your terminal:
   ```bash
   python miniKBC.py
   ```

3. **Gameplay**:
   - Read the question and the options provided.
   - Choose to use a lifeline by typing its name, or press `Enter` to skip and answer directly.
   - Input your answer (`A`, `B`, `C`, or `D`).
   - Answer before the 20-second timer runs out!

## 🛠️ Requirements

- **Python 3.x**
- No external libraries required! The script relies only on Python's built-in `time` and `random` modules.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! 
Feel free to fork this project, add more questions to the `questions` list in `miniKBC.py`, or enhance the game logic.

## 📜 License

This project is open-source and free to use. Have fun playing!

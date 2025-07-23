# 🪵 Stick Pulling Game 🎮 (Python Edition ft. a salty computer AI 🤖)

Welcome to the **Stick Pulling Game**, where you and a slightly unhinged computer take turns pulling 1 or 2 sticks from a pile. Whoever pulls the **last stick loses** 💀.

You vs. Python. One will walk away with pride, the other will malfunction and throw the emotional equivalent of a blue screen 🌀.
Now with ✨AI strategy✨ baked in! Let’s get into the juicy logic:

---

## 💡 How the Computer (Python) Thinks

> "I calculate, therefore I win. Or… do I?" – Python AI, moments before defeat

The computer isn’t just pulling sticks at random (anymore). It now uses **Nim Game logic**, trying to leave you in a **losing position** (meaning: leaving you with a multiple of 3 sticks 😈).

### 🎯 AI Strategy:

* If there are **n** sticks left:

  * The AI checks if subtracting 1 or 2 would leave **you** with a multiple of 3 (like 3, 6, 9…)
  * It then picks the move that causes maximum player despair 😌
* If it can’t avoid losing? It just shrugs and goes down sassily 💅

Basically:

* If `sticks - x ≡ 0 mod 3`, it tries to make *you* hit that unlucky number.

---

## 🧠 Is it True: If Python Plays First, She’ll Always Win?

> Mmm… depends 😏

### 💥 YES… IF:

* The number of sticks is already a **multiple of 3** (like 3, 6, 9, 12...),
* AND the computer goes first,
* AND she plays perfectly using the strategy above.

She’ll always win and smirk the whole time like a smug NPC with OP stats.

### 💥 NO… IF:

* You (the player) go first, **and** the number of sticks is **NOT** a multiple of 3,
* You also play optimally (leave her with a multiple of 3 after every round),
* THEN… guess what? You can win every time.
  Cue the "I outsmarted a machine" happy dance 💃🤖

---

## 🔄 What If the Stick Number Changes?

Great question, bestie 💅

### 🔢 If the number of sticks is:

* **Small (< 3)**: The game is over fast. No room for brainpower, only vibes.
* **Any other number**:

  * The AI still tries to follow the same rule:

    > Always leave the other player with a multiple of 3 sticks.
  * So yes, **strategy scales** no matter how big the stick pile is.

⚠️ But careful:
If you change the max pull amount (say, pulling 3 sticks instead of 2), **the AI logic needs to update too**. That’s a whole new math rabbit hole 🧠🐇.

---

## 🐣 Play the Game

```bash
python stickgame.py
```

Then just:

* Pull 1 or 2 sticks each turn
* Avoid being the last one to pull
* Bully the computer emotionally when you win (optional but encouraged 💅)

---

## 👩‍💻 Coded with Love (and Vengeance)

Because sometimes, you just wanna beat a Python script at its own game 🫶

---

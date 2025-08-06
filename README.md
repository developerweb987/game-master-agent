# 🎮 Game Master Agent (Fantasy Adventure Game)

## 🧠 What It Does

Game Master Agent is a text-based fantasy adventure game powered by multiple AI agents. It creates an immersive, interactive storyline where player choices influence the path, challenges, and rewards of the game.

### 🔍 Features:
- Narrates a dynamic adventure based on user input.
- Uses tools to control randomness and event generation:
  - `roll_dice()` – Simulates dice rolls for decision-making and combat.
  - `generate_event()` – Creates story events, encounters, or surprises.
- Switches between agents to handle different phases of the game.

### 🤖 Agents:
- **NarratorAgent** – Drives the story and presents choices to the player.
- **MonsterAgent** – Manages combat encounters with enemies.
- **ItemAgent** – Handles inventory updates, item pickups, and rewards.

## ⚙️ Technologies Used:
- **Gemini 2.0 Flash API** (or any compatible multi-agent platform)
- **Multi-Agent Handoff Logic**
- **Tools Integrated**:
  - Dice Roller (`roll_dice()`)
  - Event Generator (`generate_event()`)


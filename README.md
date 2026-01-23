# Optimal Riding System 🚖

**A Smart Fleet Dispatching Simulation**

> "Think of it as a mini-Uber or Ola dispatcher running on your computer."

## 📌 Overview
The **Optimal Riding System** is a Python-based traffic simulation that visualizes the complexity of fleet management. Instead of randomly assigning cars to passengers, this system uses an intelligent dispatch algorithm to calculate the most efficient driver for every new rider request in real-time.

It simulates a live environment where **Drivers** (vehicles with specific efficiencies and tank sizes) interact with **Riders** (request nodes) on a 2D map.

## 🚀 Features
* **Smart Dispatching:** Algorithms calculate the optimal driver-to-rider pairing based on distance and availability.
* **Real-Time Visualization:** Built with **Pygame** to render moving agents and status updates at 60 FPS.
* **Interactive Controls:**
    * **Right Click:** Spawn a new Driver.
    * **Left Click:** Place a Rider (Request) and trigger the dispatch logic.
    * **Spacebar:** Reset the simulation.
* **Object-Oriented Architecture:** Clean separation of logic between `World`, `Driver`, `Rider`, and the `Renderer`.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Engine:** Pygame (for rendering and event loop)
* **Concepts:** Pathfinding, Heuristics, Object-Oriented Programming (OOP)

## 📦 Installation & Usage

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/Shrezz-003/Optimal_Riding_System.git](https://github.com/Shrezz-003/Optimal_Riding_System.git)
    cd Optimal_Riding_System
    ```

2.  **Install Dependencies**
    You only need `pygame` to run this simulation.
    ```bash
    pip install pygame
    ```

3.  **Run the Simulation**
    ```bash
    python main.py
    ```

## 🎮 How to Play
1.  **Start the app:** You will see a blank grid or map.
2.  **Add Drivers:** Right-click anywhere to add a few cars (Drivers) to the fleet.
3.  **Request a Ride:** Left-click to place a passenger (Rider).
4.  **Watch:** The system will instantly highlight the chosen driver and send them to the rider!

---
*Created by [Shrezz-003](https://github.com/Shrezz-003)*

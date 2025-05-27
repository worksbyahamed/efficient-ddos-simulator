# DDoS Simulation Project

**For educational and authorized testing in isolated environments only.**

This project provides:
- An efficient, multi-threaded DDoS simulator for testing and learning purposes.
- A fake web server with a demo HTML page, designed as a safe target for your simulations.

> **Never use this project or any DDoS tool against systems you do not own or do not have explicit, written permission to test. Unauthorized use is illegal and unethical.**

---

## 📁 Project Structure

ddos-simulation/
├── LICENSE
├── README.md
├── DISCLAIMER.md
├── .gitignore
├── requirements.txt
├── src/
│ ├── efficient_ddos_simulator.py
│ ├── fake_server.py
│ └── static/
│ └── index.html

---

## 🚀 Getting Started

### 1. Clone the Repository

git clone https://github.com/worksbyahamed/efficient-ddos-simulation.git
cd efficient-ddos-simulation

### 2. Install Requirements

pip install -r requirements.txt

### 3. Start the Fake Web Server

python src/fake_server.py

- This will serve a demo page at [http://127.0.0.1:8080](http://127.0.0.1:8080).
- Open this URL in your browser to confirm the server is running.

### 4. Run the DDoS Simulator

- By default, the simulator targets the local fake server.
- In `src/efficient_ddos_simulator.py`, ensure:
TARGET_URL = "http://127.0.0.1:8080"

- Then run:
python src/efficient_ddos_simulator.py

---

## ⚡ Components

- `src/fake_server.py`
A simple HTTP server that serves the static HTML demo page from `src/static/index.html`.

- `src/static/index.html`
A basic HTML file to act as your fake target for DDoS testing.

- `src/efficient_ddos_simulator.py`
A multi-threaded and multi-process HTTP request generator simulating a DDoS attack for educational/lab use.

---
Example Output

When you run the simulator, you’ll see output similar to:
Starting DDoS simulation on http://127.0.0.1:8080
Simulation complete. Sent 40000 requests in 12.34 seconds.
You can monitor the fake server’s terminal for incoming requests and observe how it handles the load.

---

## ⚠️ Disclaimer

See [DISCLAIMER.md].

This project is intended solely for educational purposes and authorized DDoS simulation in isolated, controlled environments.  
**Do not use this code on any system for which you do not have explicit, written permission. Unauthorized use may be illegal and is strictly prohibited.**

---

📄 License

MIT License.

---

Credits

All code and documentation produced by **worksbyahamed**.

---

Acknowledgements

Inspired by open-source red team and DDoS simulation projects.

---

Tips
- For best results, use this project in a virtual machine or isolated lab network.
- You can adjust the simulator’s thread and process counts in `efficient_ddos_simulator.py` for different load levels.
- Monitor your system resources (CPU, RAM, network) to observe the impact.

Stay ethical. Stay legal. Use this project to learn, not to harm.

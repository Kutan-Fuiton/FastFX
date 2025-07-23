# 🚀 FastFX - Real-Time Currency Converter

💱 A lightweight, real-time currency converter built with FastAPI and vanilla JavaScript. Fetch live exchange rates and convert between 30+ currencies instantly.


## ✨ Features
- **30+ Currencies** (USD, EUR, JPY, INR, etc.)
- **Live Exchange Rates** via [Frankfurter.app](https://www.frankfurter.app/)
- **Basic UI** with Tailwind CSS
- **FastAPI Backend** - High performance with minimal code

## 🛠️ Tech Stack
- **Backend**: Python + FastAPI
- **Frontend**: Vanilla JS + Tailwind CSS
- **API**: [Frankfurter.app](https://www.frankfurter.app/)

## 🚀 Quick Start
1. Clone the repo:
   ```bash
   git clone https://github.com/Kutan-Fuiton/FastFX.git
   cd FastFX

2. Create and activate virtual env
   ```bash
   python -m venv venv
   # Linux/Mac:
   source venv/bin/activate
   # Windows:
   .\venv\Scripts\activate

3. Install requirements
   ```bash
   pip install -r requirements.txt

4. Launch the app
   ```bash
   uvicorn main:app --reload

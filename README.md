# Virtual Assistant

A Python-based virtual assistant system for managing doctor appointments.

## Project Structure

- `main.py`: Entry point of the application
- `models/nlp_model.py`: Natural Language Processing model for understanding user queries
- `database/db.py`: Database operations for managing doctor information
- `utils/matcher.py`: Pattern matching utilities for text processing
- `data/doctors.db`: SQLite database storing doctor information

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

## Features

- Natural language processing for understanding user queries
- SQLite database integration for doctor information
- Pattern matching for text processing
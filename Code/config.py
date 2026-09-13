import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_DIR = os.path.join(ROOT_DIR, "dataset")
MEDIA_DIR = os.path.join(DATASET_DIR, "media", "images")
OUTPUT_CSV_PATH = os.path.join(ROOT_DIR, "output.csv")
EVAL_DIR = os.path.join(ROOT_DIR, "evaluation")
USAGE_REPORT_PATH = os.path.join(EVAL_DIR, "usage_report.md")

# Simulation defaults
FORECAST_DAYS = 90

# API Keys
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
NVIDIA_API_KEY = os.environ.get("NVIDIA_API_KEY", "")

# Vision model on OpenRouter (Supports receipt/bill parsing)
VISION_MODEL = "qwen/qwen-2.5-vl-72b-instruct:free"  # or meta-llama/llama-3.2-11b-vision-instruct:free

# Fast LLM on Groq (For untrusted message parsing & decision summaries)
GROQ_FAST_MODEL = "llama-3.3-70b-versatile"
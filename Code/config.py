import os

# Base paths (relative to repo root)
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_DIR = os.path.join(ROOT_DIR, "dataset")
MEDIA_DIR = os.path.join(DATASET_DIR, "media", "images")
OUTPUT_CSV_PATH = os.path.join(ROOT_DIR, "output.csv")
EVAL_DIR = os.path.join(ROOT_DIR, "evaluation")
USAGE_REPORT_PATH = os.path.join(EVAL_DIR, "usage_report.md")

# Simulation Parameters
FORECAST_DAYS = 90
DEFAULT_CURRENCY = "USD"

# API & Model Configuration
GEMINI_MODEL = "gemini-2.0-flash"
API_KEY = os.environ.get("GEMINI_API_KEY", "")
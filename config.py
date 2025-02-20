from google import genai
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)


workers_name = [
    "محمد",
    "Aymen",
    "الشعراوى",
    "مصطفى سليم",
    "مرسى",
    "محمد عبدالله",
    "رضا",
    "عبدالقادر",
    "محمد عبدالحليم",
    "عاطف",
    "صادق",
    "اسلام",
    "عبد الحميد",
    "على",
    "Youssif Adel",
    "على عبدالمجيد",
    "مرسى جمال",
    "يحيى",
    "احمد محمود",
    "ايمن",
    "اسلام سيد",
    "صابر السيد",
    "Eslam Sayed",
    "احمد ربيع",
    "رأفت"
]

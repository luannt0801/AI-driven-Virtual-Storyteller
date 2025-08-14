import re
from typing import List

def smart_split(text: str, mode: str = "sentence") -> List[str]:
    """
    Split the story into parts for image prompts.
    mode: "sentence" or "paragraph"
    """
    text = text.strip()
    if mode == "paragraph":
        parts = [p.strip() for p in text.split("\n") if p.strip()]
    else:
        # Sentence split with simple regex for ., !, ?
        parts = re.split(r'(?<=[\.\!\?])\s+', text)
        parts = [s.strip() for s in parts if s.strip()]
    return parts


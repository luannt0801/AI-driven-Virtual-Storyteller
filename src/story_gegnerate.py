from sympy import im
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer
from datasets import load_dataset, load_from_disk
import torch

class StoryGenerator:
    def __init__(self, model_path, tokenized_dataset_path=None, device=None):
        """
        model_path: saved GPT model path
        tokenized_dataset_path: if need to load tokenized dataset (optional)
        device: 'cuda' or 'cpu' (auto detect if None)
        """
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.model_name = "openai-community/gpt2"

        # Load tokenizer and model
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, trust_remote_code=True, cache_dir=model_path)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name, trust_remote_code=True, cache_dir=model_path)
        self.model.to(self.device)

        # Optional: load dataset 
        self.dataset = None
        if tokenized_dataset_path:
            self.dataset = load_from_disk(tokenized_dataset_path)

    def generate_story(self, prompt, max_new_tokens=200, do_sample=True, top_k=50, top_p=0.95):
        """
        Generate story from prompt
        """
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)

        outputs = self.model.generate(
            inputs.input_ids,
            max_new_tokens=max_new_tokens,
            do_sample=do_sample,
            top_k=top_k,
            top_p=top_p,
            eos_token_id=self.tokenizer.eos_token_id
        )

        story = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return story


# if __name__ == "__main__":
#     model_path = "../models/gpt2"
#     dataset_path = "path/to/tokenized_dataset"  

#     storyteller = StoryGenerator(model_path, dataset_path)
#     prompt = "Tell me a story about a princess and a dragon"
#     story_text = storyteller.generate_story(prompt)
#     print(story_text)

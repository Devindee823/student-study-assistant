from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


def get_llm():

    model_name = "google/flan-t5-small"

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    model = AutoModelForSeq2SeqLM.from_pretrained(
        model_name,
        torch_dtype=torch.float32
    )

    model.to("cpu")

    def generate(prompt):

        inputs = tokenizer(
            prompt,
            return_tensors="pt",
            max_length=512,
            truncation=True
        )

        inputs = {k: v.to("cpu") for k, v in inputs.items()}

        outputs = model.generate(
            **inputs,
            max_new_tokens=150
        )

        answer = tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

        return answer

    return generate
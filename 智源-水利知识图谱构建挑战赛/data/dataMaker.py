# -*- coding: utf-8 -*-
import json 
def load_file(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data  

def tag_one_sample(sample):
    text = sample.get("text")
    entities = sample.get("entities")

    # tag sample
    tags = ["O" for _ in text]
    for e_t in entities:
        e, t = e_t.split("-")
        idx = text.find(e)
        tags[idx] = f"B-{t}"
        for i in range(idx+1, idx+len(e)):
            tags[i] = f"I-{t}"
    return zip(text, tags)

def tag_many_samples_gen(samples):
    for sample in samples:
        text_and_tags = tag_one_sample(sample)
        for char, tag in text_and_tags:
            yield f"{char} {tag}\n"
        yield "\n"


if __name__ == "__main__":
    train_path = r"智源-水利知识图谱构建挑战赛\data\bmes_train.json"

    fancynlp_train_path = r"智源-水利知识图谱构建挑战赛\data\bmes_train_fancynlp_sample.txt"
    train_data = load_file(train_path)
    train_samples = train_data[:10]

    with open(fancynlp_train_path, "w", encoding="utf-8", newline="") as f:
        for line in tag_many_samples_gen(train_samples):
            f.write(line)
    




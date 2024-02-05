from transformers import pipeline

input_text = "The morning sun rose above the horizon, casting a warm golden glow across the tranquil meadow. Dewdrops glistened on blades of grass, while a gentle breeze whispered through the trees. Birds chirped melodiously, heralding the start of a new day. As the world awakened, a sense of possibility filled the air, igniting hopes and dreams. In this serene moment, nature's beauty and the promise of a fresh beginning merged, creating a perfect symphony of peace and anticipation."
print(input_text)

# use bart in pytorch
summarizer = pipeline("summarization:")
summarizer("text input :The morning sun rose above the horizon, casting a warm golden glow across the tranquil meadow. Dewdrops glistened on blades of grass, while a gentle breeze whispered through the trees. Birds chirped melodiously, heralding the start of a new day. As the world awakened, a sense of possibility filled the air, igniting hopes and dreams. In this serene moment, nature's beauty and the promise of a fresh beginning merged, creating a perfect symphony of peace and anticipation.")
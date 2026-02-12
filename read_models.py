try:
    with open('models.txt', 'r', encoding='utf-16') as f:
        print(f.read())
except Exception:
    with open('models.txt', 'r', encoding='utf-8') as f:
        print(f.read())

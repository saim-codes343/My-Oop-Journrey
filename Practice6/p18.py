students = {
        "S1": {"name": "Ali", "marks": 85},
        "S2": {"name": "Sara", "marks": 92},
    }
for key, info in students.items():
        print(f"{key}: {info['name']} scored {info['marks']}")
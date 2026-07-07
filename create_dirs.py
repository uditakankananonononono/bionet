import os

dirs = [
    "apps/neuro-hub/src/app",
    "apps/neuro-hub/src/components",
    "apps/neuro-hub/public"
]

for d in dirs:
    os.makedirs(d, exist_ok=True)

print("Directories created.")

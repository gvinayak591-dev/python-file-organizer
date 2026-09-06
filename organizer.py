import os
import shutil

print("=" * 40)
print("        📁 FILE ORGANIZER")
print("=" * 40)
print()

folder = input("Enter Your folder path: ")

if not os.path.exists(folder):
    print("❌ Folder not found!")
    exit()

print(f"\n📂 Organizing: {folder}\n")

count = 0

stats = {
    "Images": 0,
    "Documents": 0,
    "Videos": 0,
    "Audio": 0,
    "Others": 0
}
files = [
    file for file in os.listdir(folder)
    if os.path.isfile(os.path.join(folder, file))
]

folders = ["Images", "Documents", "Videos", "Audio", "Others"]

for folder_name in folders:
    os.makedirs(os.path.join(folder, folder_name), exist_ok=True)

for file in files:
    extension = os.path.splitext(file)[1].lower()

    if extension in [".jpg", ".jpeg", ".png"]:
        destination_folder = "Images"

    elif extension in [".pdf", ".docx", ".txt"]:
        destination_folder = "Documents"

    elif extension in [".mp4", ".avi", ".mov"]:
        destination_folder = "Videos"

    elif extension in [".mp3", ".wav"]:
        destination_folder = "Audio"

    else:
        destination_folder = "Others"

    source = os.path.join(folder, file)
    if os.path.exists(destination):
        name, extension = os.path.splitext(file)
        file = f"{name}_copy{extension}"
        destination = os.path.join(folder, destination_folder, file)

    shutil.move(source, destination)

    count += 1
    stats[destination_folder] += 1
    print(f"✓ {file} → {destination_folder}")
print("\n📊 Summary:")
for catagory, total in stats.items():
    if total > 0:
        print(f"{catagory}: {total} files")

print("-" * 40)
print(f"✅ {count} files organized successfully!")
print("-" * 40)
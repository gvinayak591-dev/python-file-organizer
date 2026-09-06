# 📁 Python File Organizer

A Python automation tool that automatically organizes files into folders based on their file extensions.

## 🚀 Features

- 📂 Automatically organizes files by type
- 🖼️ Images → `Images/`
- 📄 Documents → `Documents/`
- 🎬 Videos → `Videos/`
- 🎵 Audio → `Audio/`
- 📦 Unknown file types → `Others/`
- ⚠️ Handles invalid folder paths
- 🔄 Handles duplicate filenames
- 📊 Displays an organization summary

## 🛠️ Technologies Used

- Python
- `os` module
- `shutil` module

## 📋 Supported File Types

| Category  | Extensions              |
|-----------|--------------------------|
| Images    | `.jpg`, `.jpeg`, `.png` |
| Documents | `.pdf`, `.docx`, `.txt` |
| Videos    | `.mp4`, `.avi`, `.mov`  |
| Audio     | `.mp3`, `.wav`          |
| Others    | All unsupported file types |

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/gvinayak591-dev/python-file-organizer.git
cd python-file-organizer
```

### 2. Run the script

```bash
python organizer.py
```

### 3. Enter your folder path when prompted

```
Enter Your folder path: test_files
```

## 📂 Example

**Before:**

```
test_files/
├── photo.jpg
├── resume.pdf
├── song.mp3
├── movie.mp4
└── random.xyz
```

**After:**

```
test_files/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── resume.pdf
├── Audio/
│   └── song.mp3
├── Videos/
│   └── movie.mp4
└── Others/
    └── random.xyz
```

## 🖥️ Sample Output

```
========================================
        📁 FILE ORGANIZER
========================================
Enter Your folder path: test_files
📁 Organizing: test_files
✓ photo.jpg → Images
✓ resume.pdf → Documents
✓ song.mp3 → Audio
✓ movie.mp4 → Videos
✓ random.xyz → Others

📊 Summary:
Images: 1 files
Documents: 1 files
Videos: 1 files
Audio: 1 files
Others: 1 files
========================================
✅ 5 files organized successfully!
========================================
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

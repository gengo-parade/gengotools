# gengotools
various tools to help
# 1. Genpare - Lyrics Processor

Genpare is a simple lyrics processing tool designed to format and process lyrics efficiently.

### Features:
- Converts newline characters in lyrics directly to '\n'.
- Replaces sequences of 3 or more spaces in lyrics with a single space.
- Automatically copies processed lyrics to the clipboard.

## Prerequisites
To use this tool, you need to have `pyperclip` installed. If not, you can install it via pip:
```bash
pip install pyperclip
```

## How to Use

1. Execute the script.
    ```bash
    python oneline.py
    ```

2. Follow the on-screen instructions:
    - Paste the raw lyrics below.
    - After pasting,  **press ENTER and then press Ctrl-Z (Windows) or Ctrl-D (Unix systems) to process them.**
    - The processed lyrics will be automatically copied to your clipboard.

**Note**: This tool will overwrite your clipboard content. Ensure you've saved any important data from your clipboard before proceeding.

## Example

**Input Lyrics:**
```
Hello
World

    This is a test
```

**Processed Output:**
```
"Hello\\nWorld\\nThis is a test"
```

## Author

- [@GammAsu](https://github.com/GammAsu)

## License
This project is open-sourced under the MIT License.

---

**Disclaimer**: Please ensure that you have the appropriate rights and permissions for the lyrics you process using this tool. The author is not responsible for any copyright infringements.

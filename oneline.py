import pyperclip

def process_lyrics(lyrics):
    # Convert newline characters directly to '\n' and replace sequences of 3 or more spaces with a single space.
    processed_lyrics = lyrics.replace('\n', '\\n')
    processed_lyrics = ' '.join(processed_lyrics.split())
    processed_lyrics = f'"{processed_lyrics}"'
    
    # Automatically copy the result to the clipboard
    pyperclip.copy(processed_lyrics)

    return processed_lyrics

if __name__ == "__main__":
    print("==========================================")
    print("      Genpare -- Lyrics Processor         ")
    print("             by @GammAsu                  ")
    print("==========================================")
    print("--")
    print("INSTRUCTIONS:")
    print("1. Paste the raw lyrics below.")
    print("2. After pasting, press Ctrl-D (or Ctrl-Z on Windows) to process them.")
    print("3. The processed lyrics will be automatically copied to your clipboard.")
    print("--")
    print("WARNING: This tool will overwrite your clipboard content.")
    print("Ensure you've saved any important data from your clipboard before proceeding.")
    print("--")
    lyrics = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        lyrics.append(line)

    lyrics_text = "\n".join(lyrics)
    result = process_lyrics(lyrics_text)
    
    print("--")
    print("Processed Lyrics:")
    print(result)
    print("--")
    print("The lyrics have been copied to your clipboard!")

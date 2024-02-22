FILE_LIST_PATH = "./all_files.txt"
OUTPUT_FILE = "./input.txt"

def main():
    with open(FILE_LIST_PATH, 'r') as f:
        files = f.readlines()
    with open(OUTPUT_FILE, 'w') as output:
        for file in files:
            with open(file.strip(), 'r') as script:
                output.write("<|start_token|>")
                s = script.read().strip()

                # remove unicode characters.
                new_script = "".join(c for c in s if ord(c) < 128)

                output.write(new_script)
                output.write("<|end_token|>")


if __name__ == '__main__':
    main()
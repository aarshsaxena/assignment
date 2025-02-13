class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print(f"Opening file: {self.filename}")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            print(f"Closing file: {self.filename}")


class FileReader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, "r")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            raise StopIteration
        return line.strip()


with FileManager("text_file.txt", "w") as file:
    file.write("Hello, this is a test!")

with FileReader("context_manager.txt") as reader:
    for line in reader:
        print(line)

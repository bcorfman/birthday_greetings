class FileRepository:
    def __init__(self, filename):
        self.filename = filename
        self.records = []
        self.read()

    def read(self):
        with open(self.filename) as f:
            f.readline()  # skip header line
            for line in f.readlines():
                elements = line.strip().split()
                self.records.append(elements)

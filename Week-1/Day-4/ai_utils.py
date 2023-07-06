def preprocess_data(data):
    processed_data = (data - np.mean(data)) / np.std(data)
    return processed_data

def train_model(data, labels):
    print("Training AI model in progress ...")

class AIModel:
    def __init__(self):
        print("Constructing AI model ...")
    
    def predict(self):
        print("Making predictions ...")

class DataProcessor:
    def load_data(self, data_path):
        print(f"Loading data from {data_path} in progress ...")
    
    def preprocess_data(self):
        print(f"Preprocessing in progress ...")
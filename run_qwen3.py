from funasr import AutoModel
import sys
import torch

def main(audio_path):
    # Initializing Qwen3-ASR using Hugging Face hub
    print(f"Loading Qwen/Qwen3-ASR-1.7B from Hugging Face...")
    model = AutoModel(
        model="Qwen/Qwen3-ASR-1.7B",
        hub="hf",
        device="cuda:0" if torch.cuda.is_available() else "cpu"
    )
    
    print(f"Transcribing {audio_path}...")
    results = model.generate(input=audio_path)
    print(results)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_qwen3.py <audio_path>")
        sys.exit(1)
    main(sys.argv[1])

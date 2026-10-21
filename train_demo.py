"""
Demo Training Script for Git <-> Colab Workflow
"""
import time
import sys

def main():
    print("=" * 50)
    print("🚀 [Version 1.0] Khởi động tiến trình Training...")
    print("=" * 50)

    # Giả lập training qua 5 epochs
    epochs = 5
    lr = 0.001

    print(f"⚙️ Config: Epochs = {epochs}, Learning Rate = {lr}")
    print("-" * 50)

    for epoch in range(1, epochs + 1):
        loss = 1.0 / epoch  # Giả lập loss giảm dần
        accuracy = min(0.99, 0.5 + 0.1 * epoch)
        print(f"Epoch [{epoch}/{epochs}] -> Loss: {loss:.4f} | Accuracy: {accuracy * 100:.1f}%")
        time.sleep(1)

    print("-" * 50)
    print("✅ Hoàn thành 5 epochs thành công!")
    print("=" * 50)

if __name__ == "__main__":
    main()

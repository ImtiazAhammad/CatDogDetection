import os
import subprocess


def main():
    dataset_path = "E:\\Python\\DeepLearning\\Image Detection\\Cat and Dog detection using YOLOV5"
    train_path = os.path.join(dataset_path, "train")
    val_path = os.path.join(dataset_path, "valid")
    test_path = os.path.join(dataset_path, "test")
    data_yaml = "data.yaml"

    with open(data_yaml, 'w') as f:
        f.write(f"train: {train_path}\n")
        f.write(f"val: {val_path}\n")
        f.write(f"test: {test_path}\n")
        f.write("nc: 2\n")
        f.write("names: ['cat', 'dog']\n")

    train_cmd = "python train.py --img 640 --batch 16 --epochs 100 --data data.yaml --cfg models/yolov5s.yaml --weights yolov5s.pt --workers 0 --single-cls"
    subprocess.run(train_cmd, shell=True, check=True)


if __name__ == "__main__":
    main()

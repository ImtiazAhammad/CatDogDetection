import subprocess


def main():
    data_yaml = "data.yaml"
    weights_path = "runs/train/exp5/weights/best.pt"

    eval_cmd = f"python val.py --data {data_yaml} --weights {weights_path}"
    subprocess.run(eval_cmd, shell=True, check=True)


if __name__ == "__main__":
    main()

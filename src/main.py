import os
import argparse
from pathlib import Path
from src.utils.common import read_yaml

def main(training, config):
    config = read_yaml(config)
    if not training:
        from src.utils.predict import prediction
        print("do prediction")
        prediction(config)
    else:
        from src.utils.train import training_model
        print("do training")
        training_model(config)

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--train", type=int, default=0)
    args.add_argument("--config", default=Path("config/config.yaml"))

    parsed_args = args.parse_args()
    main(training=bool(parsed_args.train), config=parsed_args.config)

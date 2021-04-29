import os
import argparse

import torch


def get_args():
    parser = argparse.ArgumentParser(description="Semantic Segmentation!!!")
    parser.add_argument("--EPOCHS", default=20, type=int)
    parser.add_argument("--BATCH_SIZE", default=20, type=int)
    parser.add_argument("--LEARNING_RATE", default=0.001, type=float)
    parser.add_argument("--LOSS", default="cross_entropy", type=str)
    parser.add_argument("--SCHEDULER", default="step_lr", type=str)
    parser.add_argument("--OPTIMIZER", default="AdamP", type=str)

    # parser.add_argument("--MODEL", default=None, type=str)
    parser.add_argument("--MODEL", default="DeepLabV3Plus", type=str)
    parser.add_argument("--ENCODER",default=None, type=str)

    parser.add_argument("--FILE_NAME", default="Segmentation", type=str)
    parser.add_argument("--MODEL_PATH", default="/opt/ml/code/saved", type=str)



    args = parser.parse_args()

    args.device = "cuda:0" if torch.cuda.is_available() else "cpu"

    os.makedirs(args.MODEL_PATH, exist_ok=True)
    if args.ENCODER is None:
        MODEL_PATH = os.path.join(args.MODEL_PATH, (args.MODEL))
    else:
        MODEL_PATH = os.path.join(args.MODEL_PATH, (args.MODEL+'_' + args.ENCODER))
    args.MODEL_PATH = f"{MODEL_PATH}_{args.FILE_NAME}.pt"

    return args


if __name__ == "__main__":
    pass

import os
import argparse
import torch


def get_args():
    parser = argparse.ArgumentParser(description="Semantic Segmentation!!!")
    parser.add_argument("--EPOCHS", default=10, type=int)
    parser.add_argument("--BATCH_SIZE", default=8, type=int)
    parser.add_argument("--LEARNING_RATE", default=0.0001, type=float)
    parser.add_argument("--LOSS", default="CEWithL1", type=str)
    parser.add_argument("--SCHEDULER", default="Reduce_lr", type=str)
    parser.add_argument("--OPTIMIZER", default="AdamP", type=str)
    parser.add_argument("--KFOLD", default=5, type=int)
    parser.add_argument("--CHECKPOINT", default=1, type=int)
    parser.add_argument("--LOG_INTERVAL", default=25, type=int)

    # parser.add_argument("--MODEL", default=None, type=str)
    parser.add_argument("--MODEL", default="vision_deeplabv3_resnet101", type=str)
    parser.add_argument("--ENCODER", default=None, type=str)

    parser.add_argument("--FILE_NAME", default="vision_deeplabv3_resnet101", type=str)
    parser.add_argument("--MODEL_PATH", default="/opt/ml/saved", type=str)
    parser.add_argument(
        "--CHECKPOINT_PATH",
        default="/opt/ml/checkpoints/vision_deeplabv3_resnet101",
        type=str,
    )
    parser.add_argument(
        "--LOAD_WEIGHT", default=None, type=str,
    )

    args = parser.parse_args()

    args.device = "cuda:0" if torch.cuda.is_available() else "cpu"

    os.makedirs(args.MODEL_PATH, exist_ok=True)
    if not args.ENCODER:
        MODEL_PATH = os.path.join(args.MODEL_PATH, (args.MODEL))
    else:
        MODEL_PATH = os.path.join(args.MODEL_PATH, (args.MODEL + "_" + args.ENCODER))
    args.MODEL_PATH = f"{MODEL_PATH}_{args.FILE_NAME}.pt"

    return args


if __name__ == "__main__":
    pass
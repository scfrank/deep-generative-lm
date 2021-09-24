#!/usr/bin/env python3
import os

from scripts.generative import train, test, generate_data, novelty, qualitative
from scripts.bayesopt import optimize_bayesian
from scripts.grid import run_grid
from util.error import UnknownArgumentError
from util.predefined import predefined
from util.display import print_flags
from util.settings import parse_arguments

osp = os.path

__author__ = "Tom Pelsmaeker"
__copyright__ = "Copyright 2020"


def main():
    opt, parser = parse_arguments()
    opt = predefined(opt)
    print_flags(opt)

    if not osp.isdir(opt.out_folder):
        os.makedirs(opt.out_folder)

    if opt.script == "generative":
        if opt.mode == "train":
            train(opt)
        elif opt.mode == "test":
            test(opt)
        elif opt.mode == "generate":
            generate_data(opt)
        elif opt.mode == "novelty":
            novelty(opt)
        elif opt.mode == "qualitative":
            qualitative(opt)
        else:
            raise UnknownArgumentError(
                "--mode not recognized, please choose: [train, test, generate, qualitative, novelty]."
            )
    elif opt.script == "bayesopt":
        optimize_bayesian(opt, parser)
    elif opt.script == "grid":
        run_grid(opt, parser)
    else:
        raise UnknownArgumentError(
            "--script not recognized, please choose: [generative, bayesopt, grid]."
        )


if __name__ == "__main__":
    main()

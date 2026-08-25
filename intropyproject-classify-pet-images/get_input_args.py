#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py

# PROGRAMMER: Prateek Malik
# DATE CREATED: 25 August 2026
# REVISED DATE:

# PURPOSE: Create a function that retrieves the following three command-line
#          inputs using the argparse module. Default values are used when
#          arguments are not provided.
#
# Command-line arguments:
#   1. Image folder: --dir
#   2. CNN model architecture: --arch
#   3. Dog names text file: --dogfile


# Import Python modules.
import argparse


def get_input_args():
    """
    Retrieves and parses three command-line arguments:

    1. Image folder as --dir, defaulting to 'pet_images/'.
    2. CNN architecture as --arch, defaulting to 'vgg'.
    3. Dog names file as --dogfile, defaulting to 'dognames.txt'.

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """

    # Create an argument parser.
    parser = argparse.ArgumentParser()

    # Add the pet images directory argument.
    parser.add_argument(
        "--dir",
        type=str,
        default="pet_images/",
        help="Path to the folder containing pet images."
    )

    # Add the CNN model architecture argument.
    parser.add_argument(
        "--arch",
        type=str,
        default="vgg",
        choices=["resnet", "alexnet", "vgg"],
        help="CNN model architecture: resnet, alexnet, or vgg."
    )

    # Add the dog names file argument.
    parser.add_argument(
        "--dogfile",
        type=str,
        default="dognames.txt",
        help="Path to the text file containing dog names."
    )

    # Parse and return all command-line arguments.
    return parser.parse_args()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# */AIPND-revision/intropyproject-classify-pet-images/check_images.py

# PROGRAMMER: Prateek Malik
# DATE CREATED: 25 August 2026
# REVISED DATE:

# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification
#          task. This program compares three CNN architectures:
#          AlexNet, VGG, and ResNet.

# Example command:
# python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt


# Import timing functions.
from time import time, sleep

# Import functions used to check project progress.
from print_functions_for_lab_checks import *

# Import project functions.
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results


def main():
    # TODO 0: Record the program starting time.
    start_time = time()

    # TODO 1: Retrieve command-line arguments.
    in_arg = get_input_args()

    # Check command-line arguments.
    check_command_line_arguments(in_arg)

    # TODO 2: Create pet image labels.
    results = get_pet_labels(in_arg.dir)

    # Check the generated pet image labels.
    check_creating_pet_image_labels(results)

    # TODO 3: Classify images and compare labels.
    classify_images(in_arg.dir, results, in_arg.arch)

    # Check classification results.
    check_classifying_images(results)

    # TODO 4: Determine whether each label represents a dog.
    adjust_results4_isadog(results, in_arg.dogfile)

    # Check dog versus non-dog classifications.
    check_classifying_labels_as_dogs(results)

    # TODO 5: Calculate result statistics.
    results_stats = calculates_results_stats(results)

    # Check the calculated statistics.
    check_calculating_results(results, results_stats)

    # TODO 6: Print the final results and misclassifications.
    print_results(results, results_stats, in_arg.arch, True, True)

    # TODO 0: Record the program ending time.
    end_time = time()

    # TODO 0: Calculate the total runtime in seconds.
    tot_time = end_time - start_time

    # TODO 0: Display runtime in hours:minutes:seconds format.
    print(
        "\n** Total Elapsed Runtime:",
        str(int(tot_time / 3600))
        + ":"
        + str(int((tot_time % 3600) / 60))
        + ":"
        + str(int((tot_time % 3600) % 60))
    )


if __name__ == "__main__":
    main()

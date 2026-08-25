#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# */AIPND-revision/intropyproject-classify-pet-images/print_results.py

# PROGRAMMER: Prateek Malik
# DATE CREATED: 25 August 2026
# REVISED DATE:

# PURPOSE: Print classification statistics and optionally display
#          incorrectly classified dogs and dog breeds.


def print_results(
    results_dic,
    results_stats_dic,
    model,
    print_incorrect_dogs=False,
    print_incorrect_breed=False
):
    """
    Prints classification statistics and optional misclassification details.

    Parameters:
        results_dic (dict): Dictionary containing classification results.

            index 0: Pet image label.
            index 1: Classifier label.
            index 2: Whether the labels match.
            index 3: Whether the actual image is a dog.
            index 4: Whether the classifier identified a dog.

        results_stats_dic (dict): Dictionary containing classification
                                  counts and percentages.

        model (str): CNN architecture: resnet, alexnet, or vgg.

        print_incorrect_dogs (bool): Print incorrectly classified dogs
                                    and non-dogs when True.

        print_incorrect_breed (bool): Print incorrectly classified dog
                                      breeds when True.

    Returns:
        None.
    """

    # Print the selected CNN architecture.
    print(
        "\n\n*** Results Summary for CNN Model Architecture:",
        model.upper()
    )

    # Print the number of total images, dogs, and non-dogs.
    print("\nNumber of Images:", results_stats_dic["n_images"])
    print("Number of Dog Images:", results_stats_dic["n_dogs_img"])
    print("Number of Non-Dog Images:", results_stats_dic["n_notdogs_img"])

    # Print all percentage statistics.
    print("\nClassification Percentages:")

    for statistic_name in results_stats_dic:
        if statistic_name.startswith("pct_"):
            print(
                "{:25}: {:6.2f}%".format(
                    statistic_name,
                    results_stats_dic[statistic_name]
                )
            )

    # Determine whether any dog/non-dog classifications were incorrect.
    incorrect_dogs_exist = (
        results_stats_dic["n_correct_dogs"]
        + results_stats_dic["n_correct_notdogs"]
        != results_stats_dic["n_images"]
    )

    # Print incorrectly classified dogs and non-dogs if requested.
    if print_incorrect_dogs and incorrect_dogs_exist:

        print("\nIncorrect Dog/Non-Dog Classifications:")

        for filename in results_dic:

            result = results_dic[filename]

            # One label represents a dog and the other does not.
            if result[3] != result[4]:

                print("\nFilename:", filename)
                print("Pet Image Label:", result[0])
                print("Classifier Label:", result[1])

    # Determine whether any correctly identified dogs had incorrect breeds.
    incorrect_breeds_exist = (
        results_stats_dic["n_correct_dogs"]
        != results_stats_dic["n_correct_breed"]
    )

    # Print incorrectly classified dog breeds if requested.
    if print_incorrect_breed and incorrect_breeds_exist:

        print("\nIncorrect Dog Breed Classifications:")

        for filename in results_dic:

            result = results_dic[filename]

            # Both labels identify a dog, but the predicted breed is wrong.
            if result[3] == 1 and result[4] == 1 and result[2] == 0:

                print("\nFilename:", filename)
                print("Pet Image Label:", result[0])
                print("Classifier Label:", result[1])

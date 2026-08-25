#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py

# PROGRAMMER: Prateek Malik
# DATE CREATED: 25 August 2026
# REVISED DATE:

# PURPOSE: Calculate counts and percentages from the image-classification
#          results so the three CNN architectures can be compared.


def calculates_results_stats(results_dic):
    """
    Calculates classification statistics and returns them in a dictionary.

    Parameters:
        results_dic (dict): Dictionary where each value contains:

            index 0: Pet image label.
            index 1: Classifier label.
            index 2: 1 if labels match, otherwise 0.
            index 3: 1 if the pet image is a dog, otherwise 0.
            index 4: 1 if the classifier label is a dog, otherwise 0.

    Returns:
        dict: Dictionary containing classification counts and percentages.
    """

    # Initialize the results statistics dictionary.
    results_stats_dic = {
        "n_images": len(results_dic),
        "n_dogs_img": 0,
        "n_notdogs_img": 0,
        "n_match": 0,
        "n_correct_dogs": 0,
        "n_correct_notdogs": 0,
        "n_correct_breed": 0
    }

    # Process the results for every image.
    for filename in results_dic:

        # Store the current image's result list for easier access.
        result = results_dic[filename]

        # Count matching pet and classifier labels.
        if result[2] == 1:
            results_stats_dic["n_match"] += 1

        # Process an actual dog image.
        if result[3] == 1:
            results_stats_dic["n_dogs_img"] += 1

            # The classifier also identified the image as a dog.
            if result[4] == 1:
                results_stats_dic["n_correct_dogs"] += 1

            # The classifier identified the correct dog breed.
            if result[2] == 1:
                results_stats_dic["n_correct_breed"] += 1

        # Process an actual non-dog image.
        else:
            results_stats_dic["n_notdogs_img"] += 1

            # The classifier also identified it as a non-dog.
            if result[4] == 0:
                results_stats_dic["n_correct_notdogs"] += 1

    # Calculate the percentage of matching labels.
    if results_stats_dic["n_images"] > 0:
        results_stats_dic["pct_match"] = (
            results_stats_dic["n_match"]
            / results_stats_dic["n_images"]
        ) * 100
    else:
        results_stats_dic["pct_match"] = 0.0

    # Calculate dog-related percentages.
    if results_stats_dic["n_dogs_img"] > 0:
        results_stats_dic["pct_correct_dogs"] = (
            results_stats_dic["n_correct_dogs"]
            / results_stats_dic["n_dogs_img"]
        ) * 100

        results_stats_dic["pct_correct_breed"] = (
            results_stats_dic["n_correct_breed"]
            / results_stats_dic["n_dogs_img"]
        ) * 100
    else:
        results_stats_dic["pct_correct_dogs"] = 0.0
        results_stats_dic["pct_correct_breed"] = 0.0

    # Calculate the percentage of correctly classified non-dogs.
    if results_stats_dic["n_notdogs_img"] > 0:
        results_stats_dic["pct_correct_notdogs"] = (
            results_stats_dic["n_correct_notdogs"]
            / results_stats_dic["n_notdogs_img"]
        ) * 100
    else:
        results_stats_dic["pct_correct_notdogs"] = 0.0

    # Return the completed statistics dictionary.
    return results_stats_dic

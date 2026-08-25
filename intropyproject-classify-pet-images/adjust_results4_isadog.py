#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py

# PROGRAMMER: Prateek Malik
# DATE CREATED: 25 August 2026
# REVISED DATE:

# PURPOSE: Determine whether the pet image label and classifier label
#          represent dogs by comparing them against names in dognames.txt.


def adjust_results4_isadog(results_dic, dogfile):
    """
    Updates the results dictionary to indicate whether the actual pet
    image label and classifier label represent dogs.

    Parameters:
        results_dic (dict): Dictionary containing classification results.

            index 0: Pet image label.
            index 1: Classifier label.
            index 2: Whether the labels match.
            index 3: Whether the pet image is a dog.
            index 4: Whether the classifier prediction is a dog.

        dogfile (str): Path to the file containing valid dog names.

    Returns:
        None. The results dictionary is modified directly.
    """

    # Create an empty dictionary for valid dog names.
    dognames_dic = {}

    # Open and read the dog names file.
    with open(dogfile, "r") as file:

        # Process each dog name.
        for line in file:

            # Remove whitespace and convert the dog name to lowercase.
            dog_name = line.strip().lower()

            # Ignore empty lines.
            if not dog_name:
                continue

            # Add the dog name if it is not already present.
            if dog_name not in dognames_dic:
                dognames_dic[dog_name] = 1
            else:
                print(
                    "** Warning: Dog name",
                    dog_name,
                    "already exists in dognames_dic."
                )

    # Process each image in the results dictionary.
    for filename in results_dic:

        # Retrieve the pet image label and classifier label.
        pet_label = results_dic[filename][0]
        classifier_label = results_dic[filename][1]

        # Determine whether the pet image label represents a dog.
        if pet_label in dognames_dic:
            pet_is_dog = 1
        else:
            pet_is_dog = 0

        # Determine whether the classifier label represents a dog.
        if classifier_label in dognames_dic:
            classifier_is_dog = 1
        else:
            classifier_is_dog = 0

        # Add both indicators to the existing results list.
        results_dic[filename].extend([pet_is_dog, classifier_is_dog])

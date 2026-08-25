#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py

# PROGRAMMER: Prateek Malik
# DATE CREATED: 25 August 2026
# REVISED DATE:

# PURPOSE: Create pet image labels from filenames and store them in a
#          dictionary where:
#
#          Key: Image filename.
#          Value: List containing the pet image label.


# Import the function used to retrieve filenames from a directory.
from os import listdir


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels based on image filenames.

    Parameters:
        image_dir (str): Path to the directory containing pet images.

    Returns:
        dict: Dictionary where each key is an image filename and its
              value is a list containing the corresponding pet label.

    Example:
        "Boston_terrier_02259.jpg" -> ["boston terrier"]
    """

    # Retrieve all filenames from the image directory.
    filename_list = listdir(image_dir)

    # Create an empty results dictionary.
    results_dic = {}

    # Process each image filename.
    for filename in filename_list:

        # Skip hidden files.
        if filename.startswith("."):
            continue

        # Convert the filename to lowercase and split it at underscores.
        word_list = filename.lower().split("_")

        # Create an empty string for the pet label.
        pet_label = ""

        # Add only alphabetic words to the label.
        for word in word_list:
            if word.isalpha():
                pet_label += word + " "

        # Remove leading and trailing whitespace.
        pet_label = pet_label.strip()

        # Add the filename and label if the filename is not already present.
        if filename not in results_dic:
            results_dic[filename] = [pet_label]
        else:
            print(
                "** Warning: Key =",
                filename,
                "already exists in results_dic with value =",
                results_dic[filename]
            )

    # Return the dictionary containing image filenames and pet labels.
    return results_dic

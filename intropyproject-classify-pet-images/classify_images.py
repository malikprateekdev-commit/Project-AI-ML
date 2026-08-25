#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py

# PROGRAMMER: Prateek Malik
# DATE CREATED: 25 August 2026
# REVISED DATE:

# PURPOSE: Use a pretrained CNN to classify pet images, compare classifier
#          labels with the actual pet labels, and update the results dictionary.


# Import the function for creating complete image paths.
from os.path import join

# Import the provided CNN classifier.
from classifier import classifier


def classify_images(images_dir, results_dic, model):
    """
    Classifies images, compares classifier labels with pet labels, and updates
    the results dictionary.

    Parameters:
        images_dir (str): Path to the folder containing the pet images.

        results_dic (dict): Dictionary where:
            key: Image filename.
            value:
                index 0: Pet image label.
                index 1: Classifier label, added by this function.
                index 2: Match indicator, added by this function:
                    1 if labels match.
                    0 if labels do not match.

        model (str): CNN architecture: resnet, alexnet, or vgg.

    Returns:
        None. The results dictionary is modified directly.
    """

    # Iterate through every image filename in the results dictionary.
    for filename in results_dic:

        # Construct the full path to the image.
        image_path = join(images_dir, filename)

        # Classify the image using the selected CNN model.
        classifier_label = classifier(image_path, model)

        # Convert the classifier label to lowercase and remove extra spaces.
        classifier_label = classifier_label.lower().strip()

        # Retrieve the actual pet image label.
        pet_label = results_dic[filename][0]

        # Check whether the actual label appears in the classifier label.
        if pet_label in classifier_label:
            match = 1
        else:
            match = 0

        # Add the classifier label and match indicator to the results list.
        results_dic[filename].extend([classifier_label, match])

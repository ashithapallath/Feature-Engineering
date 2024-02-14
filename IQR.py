{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNF26FwKGA7xvemx/8UN6Hz",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ashithapallath/Feature-Engineering/blob/main/IQR.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "IQR"
      ],
      "metadata": {
        "id": "Q7gNG6a4GzYp"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def calculate_iqr(data):\n",
        "    sorted_data = sorted(data)\n",
        "    n = len(sorted_data)\n",
        "\n",
        "    # Calculate quartiles and IQR\n",
        "    q1_index = n // 4\n",
        "    q3_index = 3 * n // 4\n",
        "    q1 = sorted_data[q1_index]\n",
        "    q3 = sorted_data[q3_index]\n",
        "    iqr = q3 - q1\n",
        "\n",
        "    # Define lower and upper fences for outliers\n",
        "    lower_fence = q1 - 1.5 * iqr\n",
        "    upper_fence = q3 + 1.5 * iqr\n",
        "\n",
        "    # Identify outliers\n",
        "    outliers = [x for x in sorted_data if x < lower_fence or x > upper_fence]\n",
        "\n",
        "    # Calculate median\n",
        "    median = (sorted_data[(n - 1) // 2] + sorted_data[n // 2]) / 2\n",
        "\n",
        "    return q1, q3, iqr, lower_fence, upper_fence, outliers, median\n",
        "\n",
        "# Get user input for data\n",
        "user_input = input(\"Enter your dataset (comma-separated values): \")\n",
        "data = [float(x.strip()) for x in user_input.split(\",\")]\n",
        "\n",
        "# Calculate quartiles, IQR, fences, median, and identify outliers\n",
        "q1, q3, iqr, lower_fence, upper_fence, outliers, median = calculate_iqr(data)\n",
        "\n",
        "# Print results\n",
        "print(f\"First Quartile (Q1): {q1}\")\n",
        "print(f\"Third Quartile (Q3): {q3}\")\n",
        "print(f\"IQR: {iqr}\")\n",
        "print(f\"Lower Fence: {lower_fence}\")\n",
        "print(f\"Upper Fence: {upper_fence}\")\n",
        "print(f\"Median: {median}\")\n",
        "print(f\"outliers: {outliers}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MiE96wI4JJdJ",
        "outputId": "bc5e8052-c4a0-4f5f-dd1a-c8aeb4cef810"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your dataset (comma-separated values): 26,37,24,28,35,22,31,53,41,64,29\n",
            "First Quartile (Q1): 26.0\n",
            "Third Quartile (Q3): 41.0\n",
            "IQR: 15.0\n",
            "Lower Fence: 3.5\n",
            "Upper Fence: 63.5\n",
            "Median: 31.0\n",
            "outliers: [64.0]\n"
          ]
        }
      ]
    }
  ]
}
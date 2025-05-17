{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
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
      "source": [
        "Running Sum of 1d Array"
      ],
      "metadata": {
        "id": "ZagnTG5F7Ul4"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "Qy-Abk0I7Sma"
      },
      "outputs": [],
      "source": [
        "class Solution(object):\n",
        "    def runningSum(self, nums):\n",
        "        for i in range (1,len(nums)):\n",
        "            nums[i] += nums[i-1]\n",
        "        return nums"
      ]
    }
  ]
}

{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "MAM.ipynb",
      "provenance": [],
      "collapsed_sections": []
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
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1oo0QZRqXvAH",
        "outputId": "44ae7459-206a-43ab-a562-57e8c0408912"
      },
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/gdrive')"
      ],
      "execution_count": 118,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Drive already mounted at /content/gdrive; to attempt to forcibly remount, call drive.mount(\"/content/gdrive\", force_remount=True).\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6kEuOgImE8_c"
      },
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "data=pd.read_csv('/content/gdrive/My Drive/attribution data.csv')"
      ],
      "execution_count": 119,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 417
        },
        "id": "ztLEH3amE9En",
        "outputId": "5ed19e7e-161a-4447-f56b-03183e4e8abd"
      },
      "source": [
        "data"
      ],
      "execution_count": 120,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>cookie</th>\n",
              "      <th>time</th>\n",
              "      <th>interaction</th>\n",
              "      <th>conversion</th>\n",
              "      <th>conversion_value</th>\n",
              "      <th>channel</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>00000FkCnDfDDf0iC97iC703B</td>\n",
              "      <td>2018-07-03T13:02:11Z</td>\n",
              "      <td>impression</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>Instagram</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>00000FkCnDfDDf0iC97iC703B</td>\n",
              "      <td>2018-07-17T19:15:07Z</td>\n",
              "      <td>impression</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>Online Display</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>00000FkCnDfDDf0iC97iC703B</td>\n",
              "      <td>2018-07-24T15:51:46Z</td>\n",
              "      <td>impression</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>Online Display</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>00000FkCnDfDDf0iC97iC703B</td>\n",
              "      <td>2018-07-29T07:44:51Z</td>\n",
              "      <td>impression</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>Online Display</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0000nACkD9nFkBBDECD3ki00E</td>\n",
              "      <td>2018-07-03T09:44:57Z</td>\n",
              "      <td>impression</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>Paid Search</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>586732</th>\n",
              "      <td>ooooEiB0CCoEf9fiiC90Dfhfk</td>\n",
              "      <td>2018-07-12T23:50:45Z</td>\n",
              "      <td>impression</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>Online Display</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>586733</th>\n",
              "      <td>ooooEiB0CCoEf9fiiC90Dfhfk</td>\n",
              "      <td>2018-07-12T23:50:54Z</td>\n",
              "      <td>impression</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>Online Display</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>586734</th>\n",
              "      <td>ooooiBh70D3k3BfAhDFfii9h7</td>\n",
              "      <td>2018-07-03T12:57:25Z</td>\n",
              "      <td>impression</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>Paid Search</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>586735</th>\n",
              "      <td>ooooiBh70D3k3BfAhDFfii9h7</td>\n",
              "      <td>2018-07-19T08:17:59Z</td>\n",
              "      <td>impression</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>Online Video</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>586736</th>\n",
              "      <td>ooooohAFofEnonEikhAi3fF9o</td>\n",
              "      <td>2018-07-14T17:17:12Z</td>\n",
              "      <td>impression</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>Paid Search</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>586737 rows × 6 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "                           cookie  ...         channel\n",
              "0       00000FkCnDfDDf0iC97iC703B  ...       Instagram\n",
              "1       00000FkCnDfDDf0iC97iC703B  ...  Online Display\n",
              "2       00000FkCnDfDDf0iC97iC703B  ...  Online Display\n",
              "3       00000FkCnDfDDf0iC97iC703B  ...  Online Display\n",
              "4       0000nACkD9nFkBBDECD3ki00E  ...     Paid Search\n",
              "...                           ...  ...             ...\n",
              "586732  ooooEiB0CCoEf9fiiC90Dfhfk  ...  Online Display\n",
              "586733  ooooEiB0CCoEf9fiiC90Dfhfk  ...  Online Display\n",
              "586734  ooooiBh70D3k3BfAhDFfii9h7  ...     Paid Search\n",
              "586735  ooooiBh70D3k3BfAhDFfii9h7  ...    Online Video\n",
              "586736  ooooohAFofEnonEikhAi3fF9o  ...     Paid Search\n",
              "\n",
              "[586737 rows x 6 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 120
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eUnBj_5NE9Hm",
        "outputId": "2dd86b13-2a3c-46d0-aefd-bebd3f4128b1"
      },
      "source": [
        "data_path = data.groupby('cookie')['channel'].agg(lambda x: x.tolist()).reset_index()\n",
        "data_path=data_path.rename(columns={\"channel\":\"conv_path\"})\n",
        "sales_conv= data.drop_duplicates('cookie', keep='last')[['cookie', 'conversion', 'conversion_value']]\n",
        "print(data_path.shape)\n",
        "print(sales_conv.shape)"
      ],
      "execution_count": 121,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "(240108, 2)\n",
            "(240108, 3)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 203
        },
        "id": "XPFFzOkbE9J9",
        "outputId": "e45b3a99-39d2-4901-d336-fd800735e76b"
      },
      "source": [
        "\n",
        "clean_data=pd.merge(data_path,sales_conv,how='left', on = 'cookie' )\n",
        "clean_data.head()"
      ],
      "execution_count": 122,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>cookie</th>\n",
              "      <th>conv_path</th>\n",
              "      <th>conversion</th>\n",
              "      <th>conversion_value</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>00000FkCnDfDDf0iC97iC703B</td>\n",
              "      <td>[Instagram, Online Display, Online Display, On...</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0000nACkD9nFkBBDECD3ki00E</td>\n",
              "      <td>[Paid Search, Paid Search, Paid Search, Paid S...</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0003EfE37E93D0BC03iBhBBhF</td>\n",
              "      <td>[Paid Search, Paid Search, Paid Search, Paid S...</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>00073CFE3FoFCn70fBhB3kfon</td>\n",
              "      <td>[Instagram]</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>00079hhBkDF3k3kDkiFi9EFAD</td>\n",
              "      <td>[Paid Search]</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                      cookie  ... conversion_value\n",
              "0  00000FkCnDfDDf0iC97iC703B  ...              0.0\n",
              "1  0000nACkD9nFkBBDECD3ki00E  ...              0.0\n",
              "2  0003EfE37E93D0BC03iBhBBhF  ...              0.0\n",
              "3  00073CFE3FoFCn70fBhB3kfon  ...              0.0\n",
              "4  00079hhBkDF3k3kDkiFi9EFAD  ...              0.0\n",
              "\n",
              "[5 rows x 4 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 122
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 203
        },
        "id": "ZVT2QTBFhNgU",
        "outputId": "7b08f58a-856c-4327-e1da-df764d610b70"
      },
      "source": [
        "def listToString(clean_data):  \n",
        "    str1 = \"\"  \n",
        "    for i in clean_data['conv_path']:\n",
        "      str1 += i + ' > '    \n",
        "    return str1[:-3]\n",
        "\n",
        "clean_data['conv_path'] = clean_data.apply(listToString, axis=1)\n",
        "clean_data.head()"
      ],
      "execution_count": 123,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>cookie</th>\n",
              "      <th>conv_path</th>\n",
              "      <th>conversion</th>\n",
              "      <th>conversion_value</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>00000FkCnDfDDf0iC97iC703B</td>\n",
              "      <td>Instagram &gt; Online Display &gt; Online Display &gt; ...</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0000nACkD9nFkBBDECD3ki00E</td>\n",
              "      <td>Paid Search &gt; Paid Search &gt; Paid Search &gt; Paid...</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0003EfE37E93D0BC03iBhBBhF</td>\n",
              "      <td>Paid Search &gt; Paid Search &gt; Paid Search &gt; Paid...</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>00073CFE3FoFCn70fBhB3kfon</td>\n",
              "      <td>Instagram</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>00079hhBkDF3k3kDkiFi9EFAD</td>\n",
              "      <td>Paid Search</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                      cookie  ... conversion_value\n",
              "0  00000FkCnDfDDf0iC97iC703B  ...              0.0\n",
              "1  0000nACkD9nFkBBDECD3ki00E  ...              0.0\n",
              "2  0003EfE37E93D0BC03iBhBBhF  ...              0.0\n",
              "3  00073CFE3FoFCn70fBhB3kfon  ...              0.0\n",
              "4  00079hhBkDF3k3kDkiFi9EFAD  ...              0.0\n",
              "\n",
              "[5 rows x 4 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 123
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6aqVYDD2qbzm"
      },
      "source": [
        "clean_data['var_null']=[abs(i-1) for i in clean_data['conversion']]"
      ],
      "execution_count": 124,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 417
        },
        "id": "sK22HhQrr-im",
        "outputId": "45bd0121-85e8-42ca-8773-878ce083fb9d"
      },
      "source": [
        "clean_data"
      ],
      "execution_count": 125,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>cookie</th>\n",
              "      <th>conv_path</th>\n",
              "      <th>conversion</th>\n",
              "      <th>conversion_value</th>\n",
              "      <th>var_null</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>00000FkCnDfDDf0iC97iC703B</td>\n",
              "      <td>Instagram &gt; Online Display &gt; Online Display &gt; ...</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0000nACkD9nFkBBDECD3ki00E</td>\n",
              "      <td>Paid Search &gt; Paid Search &gt; Paid Search &gt; Paid...</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0003EfE37E93D0BC03iBhBBhF</td>\n",
              "      <td>Paid Search &gt; Paid Search &gt; Paid Search &gt; Paid...</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>00073CFE3FoFCn70fBhB3kfon</td>\n",
              "      <td>Instagram</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>00079hhBkDF3k3kDkiFi9EFAD</td>\n",
              "      <td>Paid Search</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>240103</th>\n",
              "      <td>ooooE0hkAFBkED90ChDDiBFAf</td>\n",
              "      <td>Online Display</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>240104</th>\n",
              "      <td>ooooEBE0o0D97ACAAAnDoi3F0</td>\n",
              "      <td>Online Display</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>240105</th>\n",
              "      <td>ooooEiB0CCoEf9fiiC90Dfhfk</td>\n",
              "      <td>Online Display &gt; Online Display &gt; Online Display</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>240106</th>\n",
              "      <td>ooooiBh70D3k3BfAhDFfii9h7</td>\n",
              "      <td>Paid Search &gt; Online Video</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>240107</th>\n",
              "      <td>ooooohAFofEnonEikhAi3fF9o</td>\n",
              "      <td>Paid Search</td>\n",
              "      <td>0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>240108 rows × 5 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "                           cookie  ... var_null\n",
              "0       00000FkCnDfDDf0iC97iC703B  ...        1\n",
              "1       0000nACkD9nFkBBDECD3ki00E  ...        1\n",
              "2       0003EfE37E93D0BC03iBhBBhF  ...        1\n",
              "3       00073CFE3FoFCn70fBhB3kfon  ...        1\n",
              "4       00079hhBkDF3k3kDkiFi9EFAD  ...        1\n",
              "...                           ...  ...      ...\n",
              "240103  ooooE0hkAFBkED90ChDDiBFAf  ...        1\n",
              "240104  ooooEBE0o0D97ACAAAnDoi3F0  ...        1\n",
              "240105  ooooEiB0CCoEf9fiiC90Dfhfk  ...        1\n",
              "240106  ooooiBh70D3k3BfAhDFfii9h7  ...        1\n",
              "240107  ooooohAFofEnonEikhAi3fF9o  ...        1\n",
              "\n",
              "[240108 rows x 5 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 125
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aTvnOCVcFX8r",
        "outputId": "a8f377c9-0438-4a43-f9a4-339e89e87d8e"
      },
      "source": [
        "pip install ChannelAttribution"
      ],
      "execution_count": 126,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: ChannelAttribution in /usr/local/lib/python3.7/dist-packages (2.0.10)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.7/dist-packages (from ChannelAttribution) (1.1.5)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.7/dist-packages (from ChannelAttribution) (1.19.5)\n",
            "Requirement already satisfied: pytz>=2017.2 in /usr/local/lib/python3.7/dist-packages (from pandas->ChannelAttribution) (2018.9)\n",
            "Requirement already satisfied: python-dateutil>=2.7.3 in /usr/local/lib/python3.7/dist-packages (from pandas->ChannelAttribution) (2.8.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.7/dist-packages (from python-dateutil>=2.7.3->pandas->ChannelAttribution) (1.15.0)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DG_TvV1XMe9n"
      },
      "source": [
        "import ChannelAttribution\n",
        "from ChannelAttribution import heuristic_models as hm\n"
      ],
      "execution_count": 127,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "S0f-j-WAN06Q"
      },
      "source": [
        "heuristic=hm(clean_data,\"conv_path\",\"conversion\",var_value=\"conversion_value\")"
      ],
      "execution_count": 128,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "myoKkS621Co1",
        "outputId": "cfebe875-f9a4-473b-eea4-35d96808c58e"
      },
      "source": [
        "from ChannelAttribution import markov_model as mm\n",
        "markov=mm(clean_data,\"conv_path\",\"conversion\",var_value=\"conversion_value\")"
      ],
      "execution_count": 129,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Number of simulations: 100000 - Convergence reached: 1.71% < 5.00%\n",
            "Percentage of simulated paths that successfully end before maximum number of steps (48) is reached: 99.99%\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nnCYcNTFL-CZ"
      },
      "source": [
        "import plotly.io as pio"
      ],
      "execution_count": 130,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 542
        },
        "id": "qRj-QLIF59g0",
        "outputId": "5544f8fb-874e-485f-ff9d-1325a63a99b1"
      },
      "source": [
        "R=pd.merge(heuristic,markov,on=\"channel_name\",how=\"inner\")\n",
        "R1=R[[\"channel_name\",\"first_touch_conversions\",\"last_touch_conversions\",\"linear_touch_conversions\",\"total_conversions\"]]\n",
        "R1.columns=[\"channel_name\",\"first_touch\",\"last_touch\",\"linear_touch\",\"markov_model\"]\n",
        "R1=pd.melt(R1, id_vars=\"channel_name\")\n",
        "data = [dict(type = \"histogram\", histfunc=\"sum\",x = R1.channel_name, y = R1.value,transforms = [dict(type = \"groupby\", groups = R1.variable)])]\n",
        "\n",
        "fig = dict({\"data\":data}) \n",
        "pio.show(fig,validate=False)"
      ],
      "execution_count": 166,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "<html>\n",
              "<head><meta charset=\"utf-8\" /></head>\n",
              "<body>\n",
              "    <div>\n",
              "            <script src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG\"></script><script type=\"text/javascript\">if (window.MathJax) {MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}</script>\n",
              "                <script type=\"text/javascript\">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>\n",
              "        <script src=\"https://cdn.plot.ly/plotly-latest.min.js\"></script>    \n",
              "            <div id=\"c5dba27c-0c88-48bd-a1c7-ce874b6b16da\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>\n",
              "            <script type=\"text/javascript\">\n",
              "                \n",
              "                    window.PLOTLYENV=window.PLOTLYENV || {};\n",
              "                    \n",
              "                if (document.getElementById(\"c5dba27c-0c88-48bd-a1c7-ce874b6b16da\")) {\n",
              "                    Plotly.newPlot(\n",
              "                        'c5dba27c-0c88-48bd-a1c7-ce874b6b16da',\n",
              "                        [{\"histfunc\": \"sum\", \"transforms\": [{\"groups\": [\"first_touch\", \"first_touch\", \"first_touch\", \"first_touch\", \"first_touch\", \"last_touch\", \"last_touch\", \"last_touch\", \"last_touch\", \"last_touch\", \"linear_touch\", \"linear_touch\", \"linear_touch\", \"linear_touch\", \"linear_touch\", \"markov_model\", \"markov_model\", \"markov_model\", \"markov_model\", \"markov_model\"], \"type\": \"groupby\"}], \"type\": \"histogram\", \"x\": [\"Instagram\", \"Online Display\", \"Paid Search\", \"Facebook\", \"Online Video\", \"Instagram\", \"Online Display\", \"Paid Search\", \"Facebook\", \"Online Video\", \"Instagram\", \"Online Display\", \"Paid Search\", \"Facebook\", \"Online Video\", \"Instagram\", \"Online Display\", \"Paid Search\", \"Facebook\", \"Online Video\"], \"y\": [2329.0, 2160.0, 4757.0, 5177.0, 3216.0, 2244.0, 2139.0, 4547.0, 5301.0, 3408.0, 2265.179353013687, 2124.315255766789, 4681.198649801593, 5218.90337078549, 3349.4033706324544, 3498.171597633136, 2057.153846153846, 3981.877712031558, 5229.861932938856, 2871.934911242604]}],\n",
              "                        {},\n",
              "                        {\"responsive\": true}\n",
              "                    ).then(function(){\n",
              "                            \n",
              "var gd = document.getElementById('c5dba27c-0c88-48bd-a1c7-ce874b6b16da');\n",
              "var x = new MutationObserver(function (mutations, observer) {{\n",
              "        var display = window.getComputedStyle(gd).display;\n",
              "        if (!display || display === 'none') {{\n",
              "            console.log([gd, 'removed!']);\n",
              "            Plotly.purge(gd);\n",
              "            observer.disconnect();\n",
              "        }}\n",
              "}});\n",
              "\n",
              "// Listen for the removal of the full notebook cells\n",
              "var notebookContainer = gd.closest('#notebook-container');\n",
              "if (notebookContainer) {{\n",
              "    x.observe(notebookContainer, {childList: true});\n",
              "}}\n",
              "\n",
              "// Listen for the clearing of the current output cell\n",
              "var outputEl = gd.closest('.output');\n",
              "if (outputEl) {{\n",
              "    x.observe(outputEl, {childList: true});\n",
              "}}\n",
              "\n",
              "                        })\n",
              "                };\n",
              "                \n",
              "            </script>\n",
              "        </div>\n",
              "</body>\n",
              "</html>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 542
        },
        "id": "JUfiwWGDJ5qU",
        "outputId": "72919f49-9315-43b4-d7a9-fd2995be2f31"
      },
      "source": [
        "R2=R[[\"channel_name\",\"first_touch_value\",\"last_touch_value\",\n",
        "\"linear_touch_value\",\"total_conversion_value\"]]\n",
        "R2.columns=[\"channel_name\",\"first_touch\",\"last_touch\",\"linear_touch\",\"markov_model\"]\n",
        "\n",
        "R2=pd.melt(R2, id_vars=\"channel_name\")\n",
        "data = [dict(type = \"histogram\", histfunc=\"sum\", x = R2.channel_name, y = R2.value,\n",
        "             transforms = [dict(type = \"groupby\",groups = R2.variable)])]\n",
        "\n",
        "fig = dict({\"data\":data})\n",
        "pio.show(fig,validate=False)\n"
      ],
      "execution_count": 132,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "<html>\n",
              "<head><meta charset=\"utf-8\" /></head>\n",
              "<body>\n",
              "    <div>\n",
              "            <script src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG\"></script><script type=\"text/javascript\">if (window.MathJax) {MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}</script>\n",
              "                <script type=\"text/javascript\">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>\n",
              "        <script src=\"https://cdn.plot.ly/plotly-latest.min.js\"></script>    \n",
              "            <div id=\"1d537e52-d6ca-4232-898d-35710571e067\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>\n",
              "            <script type=\"text/javascript\">\n",
              "                \n",
              "                    window.PLOTLYENV=window.PLOTLYENV || {};\n",
              "                    \n",
              "                if (document.getElementById(\"1d537e52-d6ca-4232-898d-35710571e067\")) {\n",
              "                    Plotly.newPlot(\n",
              "                        '1d537e52-d6ca-4232-898d-35710571e067',\n",
              "                        [{\"histfunc\": \"sum\", \"transforms\": [{\"groups\": [\"first_touch\", \"first_touch\", \"first_touch\", \"first_touch\", \"first_touch\", \"last_touch\", \"last_touch\", \"last_touch\", \"last_touch\", \"last_touch\", \"linear_touch\", \"linear_touch\", \"linear_touch\", \"linear_touch\", \"linear_touch\", \"markov_model\", \"markov_model\", \"markov_model\", \"markov_model\", \"markov_model\"], \"type\": \"groupby\"}], \"type\": \"histogram\", \"x\": [\"Instagram\", \"Online Display\", \"Paid Search\", \"Facebook\", \"Online Video\", \"Instagram\", \"Online Display\", \"Paid Search\", \"Facebook\", \"Online Video\", \"Instagram\", \"Online Display\", \"Paid Search\", \"Facebook\", \"Online Video\", \"Instagram\", \"Online Display\", \"Paid Search\", \"Facebook\", \"Online Video\"], \"y\": [14579.5, 13419.0, 29724.0, 32283.0, 20225.5, 14039.5, 13298.5, 28331.5, 33143.5, 21418.0, 14171.723841719675, 13205.187068031722, 29194.45858794034, 32614.30009397833, 21045.330408329908, 21930.79833307923, 12820.789073537633, 24762.060588504344, 32706.28893123952, 18011.063073639274]}],\n",
              "                        {},\n",
              "                        {\"responsive\": true}\n",
              "                    ).then(function(){\n",
              "                            \n",
              "var gd = document.getElementById('1d537e52-d6ca-4232-898d-35710571e067');\n",
              "var x = new MutationObserver(function (mutations, observer) {{\n",
              "        var display = window.getComputedStyle(gd).display;\n",
              "        if (!display || display === 'none') {{\n",
              "            console.log([gd, 'removed!']);\n",
              "            Plotly.purge(gd);\n",
              "            observer.disconnect();\n",
              "        }}\n",
              "}});\n",
              "\n",
              "// Listen for the removal of the full notebook cells\n",
              "var notebookContainer = gd.closest('#notebook-container');\n",
              "if (notebookContainer) {{\n",
              "    x.observe(notebookContainer, {childList: true});\n",
              "}}\n",
              "\n",
              "// Listen for the clearing of the current output cell\n",
              "var outputEl = gd.closest('.output');\n",
              "if (outputEl) {{\n",
              "    x.observe(outputEl, {childList: true});\n",
              "}}\n",
              "\n",
              "                        })\n",
              "                };\n",
              "                \n",
              "            </script>\n",
              "        </div>\n",
              "</body>\n",
              "</html>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 203
        },
        "id": "t50QxV6VJ6a_",
        "outputId": "790112af-0268-4c4c-859a-72deb4751ec5"
      },
      "source": [
        "from ChannelAttribution import transition_matrix \n",
        "transition_matrix = transition_matrix(clean_data, \"conv_path\", \"conversion\", var_null=\"var_null\")\n",
        "transition_matrix['transition_matrix'].head()"
      ],
      "execution_count": 133,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>channel_from</th>\n",
              "      <th>channel_to</th>\n",
              "      <th>transition_probability</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>(start)</td>\n",
              "      <td>1</td>\n",
              "      <td>0.119188</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>(start)</td>\n",
              "      <td>3</td>\n",
              "      <td>0.317399</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>(start)</td>\n",
              "      <td>4</td>\n",
              "      <td>0.278408</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>(start)</td>\n",
              "      <td>5</td>\n",
              "      <td>0.142361</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>(start)</td>\n",
              "      <td>2</td>\n",
              "      <td>0.142644</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "  channel_from channel_to  transition_probability\n",
              "0      (start)          1                0.119188\n",
              "1      (start)          3                0.317399\n",
              "2      (start)          4                0.278408\n",
              "3      (start)          5                0.142361\n",
              "4      (start)          2                0.142644"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 133
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nOLTyvGoGgA4",
        "outputId": "e1d98b7d-fbc5-4f6a-909c-cb7bcd7b9709"
      },
      "source": [
        "transition_matrix"
      ],
      "execution_count": 134,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'channels':    id_channel    channel_name\n",
              " 0           1       Instagram\n",
              " 1           2  Online Display\n",
              " 2           3     Paid Search\n",
              " 3           4        Facebook\n",
              " 4           5    Online Video,\n",
              " 'transition_matrix':    channel_from    channel_to  transition_probability\n",
              " 0       (start)             1                0.119188\n",
              " 1       (start)             3                0.317399\n",
              " 2       (start)             4                0.278408\n",
              " 3       (start)             5                0.142361\n",
              " 4       (start)             2                0.142644\n",
              " 5             1             2                0.018683\n",
              " 6             1        (null)                0.363772\n",
              " 7             1             4                0.372522\n",
              " 8             1             5                0.022247\n",
              " 9             1             1                0.159586\n",
              " 10            1             3                0.033351\n",
              " 11            1  (conversion)                0.029840\n",
              " 12            2             2                0.349007\n",
              " 13            2        (null)                0.457025\n",
              " 14            2             3                0.077351\n",
              " 15            2             1                0.021069\n",
              " 16            2             5                0.016453\n",
              " 17            2             4                0.048992\n",
              " 18            2  (conversion)                0.030104\n",
              " 19            3             3                0.385981\n",
              " 20            3        (null)                0.443073\n",
              " 21            3  (conversion)                0.030025\n",
              " 22            3             5                0.024736\n",
              " 23            3             2                0.041475\n",
              " 24            3             4                0.052054\n",
              " 25            3             1                0.022656\n",
              " 26            4             4                0.373140\n",
              " 27            4             1                0.159394\n",
              " 28            4        (null)                0.363108\n",
              " 29            4  (conversion)                0.030164\n",
              " 30            4             5                0.021987\n",
              " 31            4             3                0.034010\n",
              " 32            4             2                0.018197\n",
              " 33            5             5                0.606062\n",
              " 34            5        (null)                0.280030\n",
              " 35            5             4                0.034765\n",
              " 36            5             3                0.024677\n",
              " 37            5             1                0.014492\n",
              " 38            5  (conversion)                0.030079\n",
              " 39            5             2                0.009894}"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 134
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 265
        },
        "id": "eyheV8BMdWr8",
        "outputId": "94c87ed3-3b68-49ee-d717-1223d38c02ac"
      },
      "source": [
        "matrix = pd.pivot_table(transition_matrix['transition_matrix'], values='transition_probability', index=['channel_from'],\n",
        "                    columns=['channel_to'], aggfunc=np.sum)\n",
        "matrix"
      ],
      "execution_count": 135,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th>channel_to</th>\n",
              "      <th>(conversion)</th>\n",
              "      <th>(null)</th>\n",
              "      <th>1</th>\n",
              "      <th>2</th>\n",
              "      <th>3</th>\n",
              "      <th>4</th>\n",
              "      <th>5</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>channel_from</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>(start)</th>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0.119188</td>\n",
              "      <td>0.142644</td>\n",
              "      <td>0.317399</td>\n",
              "      <td>0.278408</td>\n",
              "      <td>0.142361</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0.029840</td>\n",
              "      <td>0.363772</td>\n",
              "      <td>0.159586</td>\n",
              "      <td>0.018683</td>\n",
              "      <td>0.033351</td>\n",
              "      <td>0.372522</td>\n",
              "      <td>0.022247</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0.030104</td>\n",
              "      <td>0.457025</td>\n",
              "      <td>0.021069</td>\n",
              "      <td>0.349007</td>\n",
              "      <td>0.077351</td>\n",
              "      <td>0.048992</td>\n",
              "      <td>0.016453</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>0.030025</td>\n",
              "      <td>0.443073</td>\n",
              "      <td>0.022656</td>\n",
              "      <td>0.041475</td>\n",
              "      <td>0.385981</td>\n",
              "      <td>0.052054</td>\n",
              "      <td>0.024736</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0.030164</td>\n",
              "      <td>0.363108</td>\n",
              "      <td>0.159394</td>\n",
              "      <td>0.018197</td>\n",
              "      <td>0.034010</td>\n",
              "      <td>0.373140</td>\n",
              "      <td>0.021987</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>0.030079</td>\n",
              "      <td>0.280030</td>\n",
              "      <td>0.014492</td>\n",
              "      <td>0.009894</td>\n",
              "      <td>0.024677</td>\n",
              "      <td>0.034765</td>\n",
              "      <td>0.606062</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "channel_to    (conversion)    (null)         1  ...         3         4         5\n",
              "channel_from                                    ...                              \n",
              "(start)                NaN       NaN  0.119188  ...  0.317399  0.278408  0.142361\n",
              "1                 0.029840  0.363772  0.159586  ...  0.033351  0.372522  0.022247\n",
              "2                 0.030104  0.457025  0.021069  ...  0.077351  0.048992  0.016453\n",
              "3                 0.030025  0.443073  0.022656  ...  0.385981  0.052054  0.024736\n",
              "4                 0.030164  0.363108  0.159394  ...  0.034010  0.373140  0.021987\n",
              "5                 0.030079  0.280030  0.014492  ...  0.024677  0.034765  0.606062\n",
              "\n",
              "[6 rows x 7 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 135
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tOLe_lIbN2Ga"
      },
      "source": [
        "matrix=matrix.rename(columns={'1':'Instagram','2':'Online Display','3':'Paid Search','4':'Facebook','5':'Online Video'},\n",
        "              index={'1':'Instagram','2':'Online Display','3':'Paid Search','4':'Facebook','5':'Online Video'})"
      ],
      "execution_count": 136,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CnM7-ZzHhPU0",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "75a634aa-9485-46c2-ff28-4496c6725ac4"
      },
      "source": [
        "print(help(mm))"
      ],
      "execution_count": 137,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Help on built-in function markov_model in module ChannelAttribution:\n",
            "\n",
            "markov_model(...)\n",
            "    markov_model(Data, var_path, var_conv, var_value=None, var_null=None, order=1, nsim_start=1e5, max_step=None, out_more=False, sep=u'>', ncore=1, nfold=10, seed=0, conv_par=0.05, rate_step_sim=1.5, verbose=True)\n",
            "    \n",
            "    \n",
            "    Estimate a k-order Markov model from customer journey data. Differently from markov_model, this function iterates estimation until a desidered convergence is reached and enables multiprocessing.\n",
            "    \n",
            "    Parameters\n",
            "    ----------\n",
            "    Data : DataFrame\n",
            "        customer journeys.\n",
            "    var_path: string\n",
            "        column of Data containing paths.\n",
            "    var_conv : string\n",
            "        column of Data containing total conversions for each path.\n",
            "    var_value : string, optional, default None\n",
            "        column of Data containing revenue for each path.\n",
            "    var_null : string\n",
            "        column of Data containing total paths that do not lead to conversion.\n",
            "    order : int, default 1\n",
            "        Markov model order.        \n",
            "    nsim_start : int, default 1e5\n",
            "        minimum number of simulations to be used in computation.        \n",
            "    max_step : int, default None\n",
            "        maximum number of steps for a single simulated path. if NULL, it is the maximum number of steps found into Data.        \n",
            "    out_more : bool, default False\n",
            "        if True, transition probabilities between channels and removal effects will be returned.                \n",
            "    sep : string, default \">\"\n",
            "        separator between the channels.    \n",
            "    ncore : int, default 1\n",
            "        number of threads to be used in computation.        \n",
            "    nfold : int, default 10\n",
            "        how many repetitions to be used to verify if convergence has been reached at each iteration.    \n",
            "    seed : int, default 0\n",
            "        random seed. Giving this parameter the same value over different runs guarantees that results will not vary.    \n",
            "    conv_par : double, default 0.05\n",
            "        convergence parameter for the algorithm. The estimation process ends when the percentage of variation of the results over different repetions is less than convergence parameter.    \n",
            "    rate_step_sim : double, default 0\n",
            "        number of simulations used at each iteration is equal to the number of simulations used at previous iteration multiplied by rate_step_sim.    \n",
            "    verbose : bool, default True\n",
            "        if True, additional information about process convergence will be shown.    \n",
            "            \n",
            "    Returns\n",
            "    -------\n",
            "    list of DataFrames\n",
            "        result: Dataframe\n",
            "            (column) channel_name : channel names\n",
            "            (column) total_conversions : conversions attributed to each channel\n",
            "            (column) total_conversion_value : revenues attributed to each channel\n",
            "        transition_matrix : DataFrame\n",
            "            (column) channel_from: channel from\n",
            "            (column) channel_to : channel to\n",
            "            (column) transition_probability : transition probability from channel_from to channel_to\n",
            "        removal_effects:\n",
            "            (column) channel_name : channel names \n",
            "            (column) removal_effects_conversion : removal effects for each channel calculated using total conversions\n",
            "            (column) removal_effects_conversion_value : removal effects for each channel calculated using revenues\n",
            "                \n",
            "                        \n",
            "    Examples\n",
            "    --------\n",
            "    \n",
            "    Load Data\n",
            "    \n",
            "    >>> import pandas as pd    \n",
            "    >>> from ChannelAttribution import *\n",
            "    >>> Data = pd.read_csv('http://www.channelattribution.net/csv/Data.csv',sep=\";\")\n",
            "    \n",
            "    Estimate a Makov model using total conversions \n",
            "    \n",
            "    >>> markov_model(Data, \"path\", \"total_conversions\")\n",
            "    \n",
            "    Estimate a Makov model using total conversions and revenues \n",
            "    \n",
            "    >>> markov_model(Data, \"path\", \"total_conversions\", var_value=\"total_conversion_value\")\n",
            "    \n",
            "    Estimate a Makov model using total conversions, revenues and paths that do not lead to conversions \n",
            "    \n",
            "    >>> markov_model(Data, \"path\", \"total_conversions\", var_value=\"total_conversion_value\", var_null=\"total_null\")\n",
            "    \n",
            "    Estimate a Makov model returning transition matrix and removal effects \n",
            "    \n",
            "    >>> markov_model(Data, \"path\", \"total_conversions\", var_value=\"total_conversion_value\", var_null=\"total_null\", out_more=True)\n",
            "    \n",
            "    Estimate a Markov model using 4 threads\n",
            "    \n",
            "    >>> markov_model(Data, \"path\", \"total_conversions\", var_value=\"total_conversion_value\", ncore=4)\n",
            "\n",
            "None\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MEIoolH9c4g3",
        "outputId": "fba9e12c-7d83-45a8-9d36-e04d73340883"
      },
      "source": [
        "pip install pychattr"
      ],
      "execution_count": 138,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: pychattr in /usr/local/lib/python3.7/dist-packages (0.2.1)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.7/dist-packages (from pychattr) (1.1.5)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.7/dist-packages (from pychattr) (1.19.5)\n",
            "Requirement already satisfied: python-dateutil>=2.7.3 in /usr/local/lib/python3.7/dist-packages (from pandas->pychattr) (2.8.1)\n",
            "Requirement already satisfied: pytz>=2017.2 in /usr/local/lib/python3.7/dist-packages (from pandas->pychattr) (2018.9)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.7/dist-packages (from python-dateutil>=2.7.3->pandas->pychattr) (1.15.0)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MhlHz3Zpgh6W"
      },
      "source": [
        "from pychattr.channel_attribution import MarkovModel"
      ],
      "execution_count": 139,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nCQeR9azgofY",
        "outputId": "e376b7b9-cf7f-4cab-89d8-c72b7a4ea7c1"
      },
      "source": [
        "print(help(MarkovModel))"
      ],
      "execution_count": 140,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Help on class MarkovModel in module pychattr.channel_attribution.markov:\n",
            "\n",
            "class MarkovModel(pychattr.channel_attribution._mixins.MarkovModelMixin)\n",
            " |  MarkovModel(path_feature, conversion_feature, null_feature=None, revenue_feature=None, cost_feature=None, separator='>>>', k_order=1, n_simulations=10000, max_steps=None, return_transition_probs=True, random_state=None, loops=True)\n",
            " |  \n",
            " |  Markov channel attribution model.\n",
            " |  \n",
            " |  Parameters\n",
            " |  ----------\n",
            " |  path_feature: string; required.\n",
            " |    The name of the feature containing the paths.\n",
            " |  \n",
            " |  conversion_feature: string; required.\n",
            " |    The name of the feature indicating whether the path resulted in a\n",
            " |    conversion.\n",
            " |  \n",
            " |    NOTE: When using Markov attribution, do not pre-aggregate\n",
            " |    conversions by path as this will effect the outcome of the\n",
            " |    simulation.\n",
            " |  \n",
            " |  null_feature: string; default=None; optional.\n",
            " |    The name of the feature indicating whether the path resulted in a\n",
            " |    non-conversion.\n",
            " |  \n",
            " |    NOTE: When using Markov attribution, do not pre-aggregate\n",
            " |    non-conversions by path as this will effect the outcome of the\n",
            " |    simulation.\n",
            " |  \n",
            " |  revenue_feature: string; default=None; optional.\n",
            " |    The name of the feature containing the revenue generated\n",
            " |    for each path.\n",
            " |  \n",
            " |    NOTE: The values contained within this feature\n",
            " |    must be numeric.\n",
            " |  \n",
            " |  cost_feature: string; default=None; optional.\n",
            " |    The name of the feature containing the cost incurred for\n",
            " |    each path.\n",
            " |  \n",
            " |    NOTE: The values contained within this feature must\n",
            " |    be numeric.\n",
            " |  \n",
            " |  separator: string; default=\">>>\"; required.\n",
            " |    The symbol used to separate the channels in each path.\n",
            " |  \n",
            " |  k_order : int; default=1.\n",
            " |    denotes the order, or \"memory\" of the Markov model.\n",
            " |  \n",
            " |  n_simulations : one of {int, None}; default=10000.\n",
            " |    total simulations from the transition matrix.\n",
            " |  \n",
            " |  max_steps : one of {int, None}; default=None.\n",
            " |    the maximum number of steps for a single simulated path.\n",
            " |  \n",
            " |  return_transition_probs : bool; required; default=True.\n",
            " |    whether to return the transition probabilities between\n",
            " |    channels and removal effects.\n",
            " |  \n",
            " |  random_state : one of {int, None}; optional; default=None.\n",
            " |    the seed used by the random number generator; ensures\n",
            " |    reproducibility between runs when specified.\n",
            " |  \n",
            " |  loops : bool; required; default=True.\n",
            " |    whether to estimate loops, i.e., going from state A\n",
            " |    to state A.\n",
            " |  \n",
            " |  Attributes\n",
            " |  ----------\n",
            " |  attribution_model_: The attribution model output.\n",
            " |  \n",
            " |  transition_matrix_: The transition probability matrix.\n",
            " |  \n",
            " |  removal_effects_: The removal effects for each channel.\n",
            " |  \n",
            " |  References\n",
            " |  ----------\n",
            " |  https://www.bizible.com/blog/multi-touch-attribution-full-debrief\n",
            " |  https://cran.r-project.org/web/packages/ChannelAttribution\n",
            " |  /ChannelAttribution.pdf\n",
            " |  \n",
            " |  Method resolution order:\n",
            " |      MarkovModel\n",
            " |      pychattr.channel_attribution._mixins.MarkovModelMixin\n",
            " |      pychattr.channel_attribution._mixins.AttributionModelBase\n",
            " |      builtins.object\n",
            " |  \n",
            " |  Methods defined here:\n",
            " |  \n",
            " |  __init__(self, path_feature, conversion_feature, null_feature=None, revenue_feature=None, cost_feature=None, separator='>>>', k_order=1, n_simulations=10000, max_steps=None, return_transition_probs=True, random_state=None, loops=True)\n",
            " |      Initialize self.  See help(type(self)) for accurate signature.\n",
            " |  \n",
            " |  fit(self, df)\n",
            " |      Parameters\n",
            " |      ----------\n",
            " |      df: pandas.DataFrame; required.\n",
            " |          The dataframe containing the path data to be modeled.\n",
            " |      \n",
            " |      Returns\n",
            " |      -------\n",
            " |      self: returns a fitted instance of self.\n",
            " |  \n",
            " |  ----------------------------------------------------------------------\n",
            " |  Data and other attributes defined here:\n",
            " |  \n",
            " |  __abstractmethods__ = frozenset()\n",
            " |  \n",
            " |  ----------------------------------------------------------------------\n",
            " |  Data descriptors inherited from pychattr.channel_attribution._mixins.AttributionModelBase:\n",
            " |  \n",
            " |  __dict__\n",
            " |      dictionary for instance variables (if defined)\n",
            " |  \n",
            " |  __weakref__\n",
            " |      list of weak references to the object (if defined)\n",
            "\n",
            "None\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Bxgk-9qhgzhT",
        "outputId": "594ce1c0-e559-4827-c294-f29dc754f4f0"
      },
      "source": [
        "mm1=MarkovModel(path_feature='conv_path',conversion_feature='conversion',revenue_feature='conversion_value',separator='>')\n",
        "mm1.fit(clean_data)"
      ],
      "execution_count": 141,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<pychattr.channel_attribution.markov.MarkovModel at 0x7f9f30cffd10>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 141
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VwzeFzexj0EY"
      },
      "source": [
        "removal_effect=mm1.removal_effects_"
      ],
      "execution_count": 142,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Y50SpIQCj2i1"
      },
      "source": [
        "markov_model=removal_effect.drop(['removal_effect'],axis=1)\n"
      ],
      "execution_count": 143,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JA5Zv4snjsgb"
      },
      "source": [
        "column_names=['channel_name','value_weightage']\n",
        "first_touch = pd.DataFrame(columns = column_names)\n",
        "last_touch = pd.DataFrame(columns = column_names)\n",
        "linear_touch = pd.DataFrame(columns = column_names)"
      ],
      "execution_count": 144,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lVLA33iRjlp8"
      },
      "source": [
        "first_touch['channel_name']=R['channel_name']\n",
        "first_touch['value_weightage']=R['first_touch_value']/R['total_conversion_value']\n",
        "\n",
        "last_touch['channel_name']=R['channel_name']\n",
        "last_touch['value_weightage']=R['last_touch_value']/R['total_conversion_value']\n",
        "\n",
        "linear_touch['channel_name']=R['channel_name']\n",
        "linear_touch['value_weightage']=R['linear_touch_value']/R['total_conversion_value']"
      ],
      "execution_count": 145,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "z3jYqFoHjorT"
      },
      "source": [
        "first_touch['value_weightage']=first_touch['value_weightage']/first_touch['value_weightage'].sum()\n",
        "last_touch['value_weightage']=last_touch['value_weightage']/last_touch['value_weightage'].sum()\n",
        "linear_touch['value_weightage']=linear_touch['value_weightage']/linear_touch['value_weightage'].sum()"
      ],
      "execution_count": 146,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "U5AweqXnURCz"
      },
      "source": [
        "markov_model['removal_effect_value']=markov_model['removal_effect_value']/markov_model['removal_effect_value'].sum()\n",
        "markov_model.rename(columns = {'removal_effect_value':'value_weightage'}, inplace = True)"
      ],
      "execution_count": 147,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_nbQB2JjD-oQ"
      },
      "source": [
        " \n",
        "#### Value Weightage: Percentage of revenue derieved from a particular channel "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 203
        },
        "id": "vZpPvOxiUo3M",
        "outputId": "f6f8e71b-d2d0-4eb6-d179-999324ab50df"
      },
      "source": [
        "first_touch"
      ],
      "execution_count": 148,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>channel_name</th>\n",
              "      <th>value_weightage</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Instagram</td>\n",
              "      <td>0.132381</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Online Display</td>\n",
              "      <td>0.208421</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Paid Search</td>\n",
              "      <td>0.239033</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Facebook</td>\n",
              "      <td>0.196553</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Online Video</td>\n",
              "      <td>0.223613</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     channel_name  value_weightage\n",
              "0       Instagram         0.132381\n",
              "1  Online Display         0.208421\n",
              "2     Paid Search         0.239033\n",
              "3        Facebook         0.196553\n",
              "4    Online Video         0.223613"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 148
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 463
        },
        "id": "I-tAQEGbnfSd",
        "outputId": "1db4954e-e78e-4c93-8169-dbf4b4972dc8"
      },
      "source": [
        "import matplotlib.pyplot as plt\n",
        "plt.figure(figsize=(10,7))\n",
        "plt.bar(first_touch['channel_name'],first_touch['value_weightage'])\n",
        "plt.xlabel(\"Channels\",fontsize=16)\n",
        "plt.ylabel(\"ROI (%)\",fontsize=16)\n",
        "plt.title('First Touch', fontweight='bold')\n",
        "plt.show()\n"
      ],
      "execution_count": 149,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 720x504 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 203
        },
        "id": "l3IK_XlFVI6S",
        "outputId": "bfa89f10-ac71-4138-8f87-ca8462061c08"
      },
      "source": [
        "linear_touch"
      ],
      "execution_count": 150,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>channel_name</th>\n",
              "      <th>value_weightage</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Instagram</td>\n",
              "      <td>0.128704</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Online Display</td>\n",
              "      <td>0.205142</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Paid Search</td>\n",
              "      <td>0.234821</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Facebook</td>\n",
              "      <td>0.198610</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Online Video</td>\n",
              "      <td>0.232723</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     channel_name  value_weightage\n",
              "0       Instagram         0.128704\n",
              "1  Online Display         0.205142\n",
              "2     Paid Search         0.234821\n",
              "3        Facebook         0.198610\n",
              "4    Online Video         0.232723"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 150
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 463
        },
        "id": "8AodWvlJnVu8",
        "outputId": "7a04b07c-a9cf-4036-9354-476971561f10"
      },
      "source": [
        "plt.figure(figsize=(10,7))\n",
        "plt.bar(linear_touch['channel_name'],linear_touch['value_weightage'])\n",
        "plt.xlabel(\"Channels\",fontsize=16)\n",
        "plt.ylabel(\"ROI (%)\",fontsize=16)\n",
        "plt.title('Linear Touch', fontweight='bold')\n",
        "plt.show()\n"
      ],
      "execution_count": 151,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 720x504 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 203
        },
        "id": "3UBsFVCq_Oq_",
        "outputId": "2de7a3ce-c696-4b85-d13d-c705e5469ef1"
      },
      "source": [
        "last_touch"
      ],
      "execution_count": 152,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>channel_name</th>\n",
              "      <th>value_weightage</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Instagram</td>\n",
              "      <td>0.127420</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Online Display</td>\n",
              "      <td>0.206457</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Paid Search</td>\n",
              "      <td>0.227732</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Facebook</td>\n",
              "      <td>0.201701</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Online Video</td>\n",
              "      <td>0.236690</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     channel_name  value_weightage\n",
              "0       Instagram         0.127420\n",
              "1  Online Display         0.206457\n",
              "2     Paid Search         0.227732\n",
              "3        Facebook         0.201701\n",
              "4    Online Video         0.236690"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 152
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 463
        },
        "id": "C_SHw8KZnPnE",
        "outputId": "0645cc98-b750-4861-d353-2b9f88afa918"
      },
      "source": [
        "plt.figure(figsize=(10,7))\n",
        "plt.bar(last_touch['channel_name'],last_touch['value_weightage'])\n",
        "plt.xlabel(\"Channels\",fontsize=16)\n",
        "plt.ylabel(\"ROI (%)\",fontsize=16)\n",
        "plt.title('Last Touch', fontweight='bold')\n",
        "plt.show()\n"
      ],
      "execution_count": 153,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 720x504 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 501
        },
        "id": "XnDhYt6_UQl5",
        "outputId": "fc266150-d49b-4e6d-ccb2-ff87aeea5d9e"
      },
      "source": [
        "import seaborn as sns\n",
        "fig = plt.figure(figsize = (14,8))\n",
        "sns.heatmap(matrix,annot=True)\n",
        "plt.xlabel(\"Channel From\",fontsize=14)\n",
        "plt.ylabel(\"Channel To\",fontsize=14)\n",
        "plt.show()"
      ],
      "execution_count": 154,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAzQAAAHkCAYAAADo02pxAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOzdd3hU1dbH8e+akBBAigGEEBAEAQULCliRooBKt2BHrIhergXQa69wr73ji1gAsSuoQECkgxQFFJDekTRKQpGezOz3jwwhBUjQJJOZ+X2eZx7nnLPPmXXGYWfWrH32MeccIiIiIiIiwcgT6ABERERERET+LiU0IiIiIiIStJTQiIiIiIhI0FJCIyIiIiIiQUsJjYiIiIiIBC0lNCIiIiIiErRKBToAKRDNrS1Br32tKwIdQsg70RMd6BBC3hPmDXQIYSFpX7lAhxDyPoreF+gQwsI3G3+wQMdwNOnb1hX698vIKnUDcr6q0IiIiIiISLEwsyvMbKWZrTGzR4/S5jozW2ZmS83s8/yOqQqNiIiIiEi48RV/xdnMIoBBQDsgAZhnZqOdc8uytakPPAZc7JzbbmYn5XdcVWhERERERKQ4nAescc6tc84dBL4EuuZqczcwyDm3HcA5tyW/gyqhEREREREJN85X6A8z62Vm87M9euV61ThgU7blBP+67BoADcxslpnNNbN8L8LVkDMREREREfnHnHNDgCH/8DClgPpAa6AmMMPMznTO7TjWDiIiIiIiEk58vkC8aiJQK9tyTf+67BKAX5xz6cB6M1tFZoIz72gH1ZAzEREREZEw45yv0B8FMA+ob2anmFkUcAMwOleb78mszmBmVcgcgrbuWAdVQiMiIiIiIkXOOZcB9AEmAMuBr51zS83seTPr4m82AUg1s2XAVOBh51zqsY6rIWciIiIiIuEmMEPOcM6NA8blWvd0tucO6Ot/FIgqNCIiIiIiErRUoRERERERCTcFu+YlKCihEREREREJNz5voCMoNBpyJiIiIiIiQUsVGhERERGRcBNCQ85UoRERERERkaClCo2IiIiISLgJ0LTNRUEJjYiIiIhImHEaciYiIiIiIhJ4qtCIiIiIiISbEBpypgqNiIiIiIgELVVoRERERETCja6hERERERERCTxVaEREREREwo3PG+gICo0SGhERERGR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FM65j4vhNT4o6tcQEREREckjhKZtVoVGRERERESClio0IiIiIiLhJoSuoVFCIyIiIiISbkIoodGQMxERERERCVqq0IiIiIiIhBnnQudGwarQiIiIiIhI0FKFRkREREQk3ITQNTRKaEREREREwo3uQyMiIiIiIhJ4qtCIiIiIiISbEBpypgqNiIiIiIgELVVoRERERETCTQhdQ6OERkREREQk3GjImYiIiIiISOCpQiMiIiIiEm5CaMiZKjQiIiIiIhK0VKEREREREQk3uoZGREREREQk8FShEREREREJNyFUoVFCIyIiIiISbjQpgIiIiIiISOCpQiMiIiIiEm5CaMiZKjQiIiIiIhK0VKEREREREQk3IXQNjRIaEREREZFwoyFnIiIiIiIigacKjYiIiIhIuAmhIWeq0IiIiIiISNBShSYIVChXN9AhhLSV59QOdAhhoWZE5UCHEPI+S/kl0CGEvJ9KlQ50CGFh5flxgQ4h5F01e0OgQ5BAC6FraJTQiIiIiIiEmxBKaDTkTEREREREioWZXWFmK81sjZk9eoTtt5nZVjNb6H/cld8xVaEREREREQk3zhX7S5pZBDAIaAckAPPMbLRzblmupl855/oU9Liq0IiIiIiISHE4D1jjnFvnnDsIfAl0/acHVUIjIiIiIhJufL5Cf5hZLzObn+3RK9erxgGbsi0n+Nfldo2ZLTazb82sVn6noiFnIiIiIiLyjznnhgBD/uFhxgBfOOcOmNk9wHDg0mPtoIRGRERERCTcBGaWs0Qge8Wlpn9dFudcarbFD4GX8zuoEhoRERERkXDjApLQzAPqm9kpZCYyNwA3ZW9gZrHOuWT/YhdgeX4HVUIjIiIiIiJFzjmXYWZ9gAlABPCxc26pmT0PzHfOjQbuN7MuQAaQBtyW33GV0IiIiIiIhJsA3VjTOTcOGJdr3dPZnj8GPHY8x9QsZyIiIiIiErRUoRERERERCTcBuLFmUVFCIyIiIiISbgI05KwoaMiZiIiIiIgELVVoRERERETCjSo0IiIiIiIigacKjYiIiIhIuAnMjTWLhBIaEREREZEw43yhM8uZhpyJiIiIiEjQUoVGRERERCTcaFIAERERERGRwFOFRkREREQk3ITQpACq0IiIiIiISNBShUZEREREJNyE0CxnSmhERERERMKNJgUQEREREREJPFVoRERERETC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\n",
            "text/plain": [
              "<Figure size 1008x576 with 2 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 203
        },
        "id": "9GAAjWdiUdTA",
        "outputId": "42e7d7b5-071c-4b05-ed6d-6e6b47af929b"
      },
      "source": [
        "removal_effect"
      ],
      "execution_count": 155,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>channel_name</th>\n",
              "      <th>removal_effect</th>\n",
              "      <th>removal_effect_value</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Instagram</td>\n",
              "      <td>0.3103</td>\n",
              "      <td>0.310868</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Online Display</td>\n",
              "      <td>0.1813</td>\n",
              "      <td>0.179455</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Paid Search</td>\n",
              "      <td>0.3595</td>\n",
              "      <td>0.358910</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Facebook</td>\n",
              "      <td>0.4614</td>\n",
              "      <td>0.461955</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Online Video</td>\n",
              "      <td>0.2489</td>\n",
              "      <td>0.249712</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     channel_name  removal_effect  removal_effect_value\n",
              "0       Instagram          0.3103              0.310868\n",
              "1  Online Display          0.1813              0.179455\n",
              "2     Paid Search          0.3595              0.358910\n",
              "3        Facebook          0.4614              0.461955\n",
              "4    Online Video          0.2489              0.249712"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 155
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 203
        },
        "id": "4tXoJYKTUVjV",
        "outputId": "a5326395-f781-455c-e46d-46569b245982"
      },
      "source": [
        "markov_model"
      ],
      "execution_count": 156,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>channel_name</th>\n",
              "      <th>value_weightage</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Instagram</td>\n",
              "      <td>0.199159</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Online Display</td>\n",
              "      <td>0.114969</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Paid Search</td>\n",
              "      <td>0.229938</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Facebook</td>\n",
              "      <td>0.295954</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Online Video</td>\n",
              "      <td>0.159980</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     channel_name  value_weightage\n",
              "0       Instagram         0.199159\n",
              "1  Online Display         0.114969\n",
              "2     Paid Search         0.229938\n",
              "3        Facebook         0.295954\n",
              "4    Online Video         0.159980"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 156
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 463
        },
        "id": "r5XsSPZRm3Pt",
        "outputId": "58ede9c9-09e7-4885-a29a-b7417855a859"
      },
      "source": [
        "plt.figure(figsize=(10,7))\n",
        "plt.bar(markov_model['channel_name'],markov_model['value_weightage'])\n",
        "plt.xlabel(\"Channels\",fontsize=16)\n",
        "plt.ylabel(\"ROI (%)\",fontsize=16)\n",
        "plt.title('Markov Chains', fontweight='bold')\n",
        "plt.show()\n"
      ],
      "execution_count": 157,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 720x504 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nESHxxHmFce-"
      },
      "source": [
        "def mainMenu():\n",
        "  print(\"Enter the amount you wish to spend on your campaign:\"+'\\033[0m',end=\"\")\n",
        "  amt=int(input())\n",
        "  print(\"Select the model befitted for your campaign\"+'\\033[0m')\n",
        "  print(\"1. First Touch \")\n",
        "  print(\"2. Last Touch \")\n",
        "  print(\"3. Linear Touch \")\n",
        "  print(\"4. Markov Chains \")\n",
        "  print(\"Enter the Option Number:\"+'\\033[0m', end=\"\" )\n",
        "  selection=int(input())\n",
        "  if selection==1:\n",
        "    first=first_touch.copy()\n",
        "    first['value_weightage'] = first['value_weightage'].apply(lambda x: x*amt)\n",
        "    first.rename(columns = {'value_weightage':'Amount to spend'}, inplace = True)\n",
        "    print(first)\n",
        "  if selection==2:\n",
        "    last=last_touch.copy()\n",
        "    last['value_weightage'] = last['value_weightage'].apply(lambda x: x*amt)\n",
        "    last.rename(columns = {'value_weightage':'Amount to spend'}, inplace = True)\n",
        "    print(last)\n",
        "  if selection==3:\n",
        "    linear=linear_touch.copy()\n",
        "    linear['value_weightage'] = linear['value_weightage'].apply(lambda x: x*amt)\n",
        "    linear.rename(columns = {'value_weightage':'Amount to spend'}, inplace = True)\n",
        "    print(linear)\n",
        "  if selection==4:\n",
        "    mm2=markov_model.copy()\n",
        "    mm2['value_weightage'] = mm2['value_weightage'].apply(lambda x: x*amt)\n",
        "    mm2.rename(columns = {'value_weightage':'Amount to spend'}, inplace = True)\n",
        "    print(mm2)"
      ],
      "execution_count": 158,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Yc6P0r22PYvY",
        "outputId": "f4719c57-dee2-4a67-c526-6cdf51414352"
      },
      "source": [
        "mainMenu()"
      ],
      "execution_count": 159,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Enter the amount you wish to spend on your campaign:\u001b[0m500000\n",
            "Select the model befitted for your campaign\u001b[0m\n",
            "1. First Touch \n",
            "2. Last Touch \n",
            "3. Linear Touch \n",
            "4. Markov Chains \n",
            "Enter the Option Number:\u001b[0m4\n",
            "     channel_name  Amount to spend\n",
            "0       Instagram     99579.687812\n",
            "1  Online Display     57484.475071\n",
            "2     Paid Search    114968.950141\n",
            "3        Facebook    147977.023616\n",
            "4    Online Video     79989.863360\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 542
        },
        "id": "SfcmSgnw_RFf",
        "outputId": "bbb43685-ba2c-4d64-ca1f-405dcc171710"
      },
      "source": [
        "a=pd.merge(first_touch,last_touch,on=\"channel_name\",how=\"inner\")\n",
        "a=a.rename(columns={\"value_weightage_x\":\"first_touch\",\"value_weightage_y\":\"last_touch\"})\n",
        "b=pd.merge(a,linear_touch,on=\"channel_name\",how=\"inner\")\n",
        "b=b.rename(columns={\"value_weightage\":\"linear_touch\"})\n",
        "c=pd.merge(b,markov_model,on=\"channel_name\",how=\"inner\")\n",
        "c=c.rename(columns={\"value_weightage\":\"markov_chain\"})\n",
        "c=pd.melt(c, id_vars=\"channel_name\")\n",
        "data = [dict(type = \"histogram\", histfunc=\"sum\",x = c.channel_name, y = c.value,transforms = [dict(type = \"groupby\", groups = c.variable)])]\n",
        "fig = dict({\"data\":data})\n",
        "pio.show(fig,validate=False)"
      ],
      "execution_count": 242,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "<html>\n",
              "<head><meta charset=\"utf-8\" /></head>\n",
              "<body>\n",
              "    <div>\n",
              "            <script src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG\"></script><script type=\"text/javascript\">if (window.MathJax) {MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}</script>\n",
              "                <script type=\"text/javascript\">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>\n",
              "        <script src=\"https://cdn.plot.ly/plotly-latest.min.js\"></script>    \n",
              "            <div id=\"8554fd1a-11f3-4d8e-8320-7afdf1817c07\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>\n",
              "            <script type=\"text/javascript\">\n",
              "                \n",
              "                    window.PLOTLYENV=window.PLOTLYENV || {};\n",
              "                    \n",
              "                if (document.getElementById(\"8554fd1a-11f3-4d8e-8320-7afdf1817c07\")) {\n",
              "                    Plotly.newPlot(\n",
              "                        '8554fd1a-11f3-4d8e-8320-7afdf1817c07',\n",
              "                        [{\"histfunc\": \"sum\", \"transforms\": [{\"groups\": [\"first_touch\", \"first_touch\", \"first_touch\", \"first_touch\", \"first_touch\", \"last_touch\", \"last_touch\", \"last_touch\", \"last_touch\", \"last_touch\", \"linear_touch\", \"linear_touch\", \"linear_touch\", \"linear_touch\", \"linear_touch\", \"markov_chain\", \"markov_chain\", \"markov_chain\", \"markov_chain\", \"markov_chain\"], \"type\": \"groupby\"}], \"type\": \"histogram\", \"x\": [\"Instagram\", \"Online Display\", \"Paid Search\", \"Facebook\", \"Online Video\", \"Instagram\", \"Online Display\", \"Paid Search\", \"Facebook\", \"Online Video\", \"Instagram\", \"Online Display\", \"Paid Search\", \"Facebook\", \"Online Video\", \"Instagram\", \"Online Display\", \"Paid Search\", \"Facebook\", \"Online Video\"], \"y\": [0.13238072598629147, 0.2084212360524869, 0.2390325476450335, 0.1965527781280069, 0.22361271218818118, 0.127420166154977, 0.2064566468684845, 0.22773183939139616, 0.2017010071440535, 0.23669034044108872, 0.12870399165624338, 0.20514152493222043, 0.23482126357203661, 0.1986097527833758, 0.2327234670561237, 0.1991593756239409, 0.11496895014104264, 0.22993790028208527, 0.29595404723264607, 0.15997972672028504]}],\n",
              "                        {},\n",
              "                        {\"responsive\": true}\n",
              "                    ).then(function(){\n",
              "                            \n",
              "var gd = document.getElementById('8554fd1a-11f3-4d8e-8320-7afdf1817c07');\n",
              "var x = new MutationObserver(function (mutations, observer) {{\n",
              "        var display = window.getComputedStyle(gd).display;\n",
              "        if (!display || display === 'none') {{\n",
              "            console.log([gd, 'removed!']);\n",
              "            Plotly.purge(gd);\n",
              "            observer.disconnect();\n",
              "        }}\n",
              "}});\n",
              "\n",
              "// Listen for the removal of the full notebook cells\n",
              "var notebookContainer = gd.closest('#notebook-container');\n",
              "if (notebookContainer) {{\n",
              "    x.observe(notebookContainer, {childList: true});\n",
              "}}\n",
              "\n",
              "// Listen for the clearing of the current output cell\n",
              "var outputEl = gd.closest('.output');\n",
              "if (outputEl) {{\n",
              "    x.observe(outputEl, {childList: true});\n",
              "}}\n",
              "\n",
              "                        })\n",
              "                };\n",
              "                \n",
              "            </script>\n",
              "        </div>\n",
              "</body>\n",
              "</html>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aWT1_zC5IAOf"
      },
      "source": [
        ""
      ],
      "execution_count": 229,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vH9K7IbQDEma"
      },
      "source": [
        ""
      ],
      "execution_count": 230,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nVqciCgwInvX"
      },
      "source": [
        ""
      ],
      "execution_count": 232,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QR-ah-buDFvE"
      },
      "source": [
        ""
      ],
      "execution_count": 234,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Bt5O7WSjI1ID"
      },
      "source": [
        ""
      ],
      "execution_count": 236,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Guw2EjqfFMwr"
      },
      "source": [
        ""
      ],
      "execution_count": 238,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 542
        },
        "id": "A1NnjfpnHnqV",
        "outputId": "7f2ac3d5-81b7-40a5-adff-136731b38dfd"
      },
      "source": [
        ""
      ],
      "execution_count": 241,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "<html>\n",
              "<head><meta charset=\"utf-8\" /></head>\n",
              "<body>\n",
              "    <div>\n",
              "            <script src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG\"></script><script type=\"text/javascript\">if (window.MathJax) {MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}</script>\n",
              "                <script type=\"text/javascript\">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>\n",
              "        <script src=\"https://cdn.plot.ly/plotly-latest.min.js\"></script>    \n",
              "            <div id=\"889b5fa0-689a-4a9c-a11f-cde4dcccc719\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>\n",
              "            <script type=\"text/javascript\">\n",
              "                \n",
              "                    window.PLOTLYENV=window.PLOTLYENV || {};\n",
              "                    \n",
              "                if (document.getElementById(\"889b5fa0-689a-4a9c-a11f-cde4dcccc719\")) {\n",
              "                    Plotly.newPlot(\n",
              "                        '889b5fa0-689a-4a9c-a11f-cde4dcccc719',\n",
              "                        [{\"histfunc\": \"sum\", \"transforms\": [{\"groups\": [\"first_touch\", \"first_touch\", \"first_touch\", \"first_touch\", \"first_touch\", \"last_touch\", \"last_touch\", \"last_touch\", \"last_touch\", \"last_touch\", \"linear_touch\", \"linear_touch\", \"linear_touch\", \"linear_touch\", \"linear_touch\", \"markov_chain\", \"markov_chain\", \"markov_chain\", \"markov_chain\", \"markov_chain\"], \"type\": \"groupby\"}], \"type\": \"histogram\", \"x\": [\"Instagram\", \"Online Display\", \"Paid Search\", \"Facebook\", \"Online Video\", \"Instagram\", \"Online Display\", \"Paid Search\", \"Facebook\", \"Online Video\", \"Instagram\", \"Online Display\", \"Paid Search\", \"Facebook\", \"Online Video\", \"Instagram\", \"Online Display\", \"Paid Search\", \"Facebook\", \"Online Video\"], \"y\": [0.13238072598629147, 0.2084212360524869, 0.2390325476450335, 0.1965527781280069, 0.22361271218818118, 0.127420166154977, 0.2064566468684845, 0.22773183939139616, 0.2017010071440535, 0.23669034044108872, 0.12870399165624338, 0.20514152493222043, 0.23482126357203661, 0.1986097527833758, 0.2327234670561237, 0.1991593756239409, 0.11496895014104264, 0.22993790028208527, 0.29595404723264607, 0.15997972672028504]}],\n",
              "                        {},\n",
              "                        {\"responsive\": true}\n",
              "                    ).then(function(){\n",
              "                            \n",
              "var gd = document.getElementById('889b5fa0-689a-4a9c-a11f-cde4dcccc719');\n",
              "var x = new MutationObserver(function (mutations, observer) {{\n",
              "        var display = window.getComputedStyle(gd).display;\n",
              "        if (!display || display === 'none') {{\n",
              "            console.log([gd, 'removed!']);\n",
              "            Plotly.purge(gd);\n",
              "            observer.disconnect();\n",
              "        }}\n",
              "}});\n",
              "\n",
              "// Listen for the removal of the full notebook cells\n",
              "var notebookContainer = gd.closest('#notebook-container');\n",
              "if (notebookContainer) {{\n",
              "    x.observe(notebookContainer, {childList: true});\n",
              "}}\n",
              "\n",
              "// Listen for the clearing of the current output cell\n",
              "var outputEl = gd.closest('.output');\n",
              "if (outputEl) {{\n",
              "    x.observe(outputEl, {childList: true});\n",
              "}}\n",
              "\n",
              "                        })\n",
              "                };\n",
              "                \n",
              "            </script>\n",
              "        </div>\n",
              "</body>\n",
              "</html>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3x_WpWMQDoif"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
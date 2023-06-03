# Protecting-User-Privacy-on-Social-Networks

This project aims to address the privacy risks associated with sharing personal information on social networking sites (SNS). It involves the development of an NLP-based tool that detects privacy-related information in messages or posts, allowing users to make informed decisions before sharing content. The tool utilizes machine learning algorithms, data mining techniques, and a comprehensive privacy database to accurately identify sensitive information, such as personal details, banking information, and location data.

Project Components:

Home.py: A basic GUI window that enables users to enter a tweet message and post it on their Twitter account. It utilizes the Tweepy library for user authentication and tweet posting. The GUI also incorporates the PIL library for image generation and the base64 library for encoding.

Rake.py: This script utilizes NLTK and CommonRegex libraries to detect the presence of personal information, such as phone numbers or email addresses, in a tweet. It returns a Boolean value of True if such information is found.

Send_tweet.py: This script uses the Tweepy library to post tweets on Twitter. It takes the tweet message and API credentials as inputs, ensuring seamless tweet delivery.

Twitter_streaming.py: This script leverages Tweepy to stream live tweets and save them in a text file. It employs OAuth for user authentication and tweet retrieval, and the resulting tweets are saved in a text file named "twitter_data.txt". These scripts are designed to be executed within the Spyder environment.

Project Execution:
To execute the project, follow these steps:

Open the Spyder environment and ensure all required libraries are installed.
Run the Home.py script to access the GUI window for entering and posting tweets.
Execute the Rake.py script to detect personal information in a tweet by providing the necessary NLTK and CommonRegex libraries.
Utilize the Send_tweet.py script to post tweets on Twitter by providing the tweet message and appropriate API credentials.
Run the Twitter_streaming.py script to stream live tweets and save them in a text file named "twitter_data.txt" using the Tweepy library.
Please note that proper configuration and authentication are essential for the successful execution of the project components.

Note: This README file provides an overview of the project and its components. For detailed implementation and usage instructions, refer to the individual script files and associated documentation.

# Smart-Eye
This work focuses on the detection of suspicious human activities from surveillance videos, using image processing and computer vision. Intelligent video surveillance is envisaged for monitoring various public and sensitive places, such as stations, airports, shopping centres, etc., in order to prevent terrorism, theft, accidents and other illicit behaviour.

The specific aim of the project is to detect acts of violence in real time, whether physical or involving weapons. The real-time notification system is designed to work as follows:

When an image is identified as violent, a counter is initialised at one. The next 30 images are then checked for violence.

A Telegram bot called "Smart Eye" receives predictions about suspicious activity. Based on these results, the bot offers commands to the user, such as "help" for assistance, "call the police" in an emergency, or "activate alert" to trigger an emergency notification.

The system operates in real time, ensuring continuous monitoring of suspicious activity. The results of the predictions are transmitted instantly to the Telegram bot, enabling it to react immediately.

Users can interact with the bot to obtain more information, request assistance or take emergency action depending on the situation detected.
The overall objective is to automatically detect and classify the types of actions in the videos, in particular violent behaviour. CNN models and an Inception V3 transfer learning algorithm were used to identify these violent events in real-time surveillance footage. The proposed networks demonstrate satisfactory recognition accuracy on reference datasets, showing their ability to learn distinctive motion features.

In short, this project aims to implement an automated system for detecting and alerting on suspicious behaviours in real-time surveillance videos, highlighting advances in the field of artificial intelligence and machine learning. This work has enabled the authors to gain significant experience in these fields, as well as skills in design and problem solving.

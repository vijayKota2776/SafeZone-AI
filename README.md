Project Overview

1.	Objective:
	• “femshield aims to enhance public safety for women by utilizing AI-powered surveillance cameras and a mobile app for real-time alerts.”
2.	Key Features:
	•	AI-Powered Surveillance: Cameras that detect unusual behavior and alert the user or authorities.
	•	Real-Time Alerts: Notifications sent to guardians and authorities based on detected threats.
	•	Route Tracking: Live tracking of the user’s route from location A to B.
	•	Battery Monitoring: Alerts if the device’s battery is running low.
	•	Escalation Alerts: A three-step alert system that notifies guardians, the user, and finally the police if travel is delayed.
3.	Technological Innovations:
	•	Behavior Detection Algorithms: Using AI to analyze video feeds in real-time.
	•	Mobile Application: A user-friendly interface for alerts and monitoring.
	•	Cloud-Based Data Storage: For storing user data and alert logs securely.
4.	User Flow:
	To explain how the core AI functionalities and alert system work for your SafeZone AI project, we can break it down into several key components:

1. Core AI Functionalities

a. Surveillance System

	•	AI-Powered Cameras: These cameras use computer vision algorithms to detect and recognize people, vehicles, and suspicious behavior (e.g., aggressive gestures, loitering).
	•	Behavior Detection: This involves analyzing the captured video feed in real-time to identify potentially threatening actions. Techniques like object detection and action recognition can be employed.

b. Data Processing and Analysis

	•	Real-Time Data Processing: The video feeds from cameras are processed using AI models (e.g., LLaMA or similar) to extract meaningful information.
	•	Event Triggering: If suspicious behavior is detected, it triggers an alert.

c. User Interface

	•	Mobile App: A mobile app allows users to interact with the system, receive alerts, and send emergency signals.
	•	Community Engagement: Users can report incidents or share information through the app.

2. Alert System Mechanism

The alert system can be broken down into three main stages, including conditions under which alerts are triggered.

a. Route Tracking and Delay Detection

	•	Real-Time Tracking: The app tracks the user’s location from point A to point B.
	•	Expected Travel Time Calculation: Based on distance and traffic conditions, the app calculates the expected travel time.
	•	Delay Detection: If the user deviates from the expected route or delays beyond a set threshold (e.g., 10 minutes), the alert system initiates.

b. Three-Step Alert Escalation

	1.	Initial Alert to Guardians:
	•	If a delay is detected, the app sends an alert to the user’s designated guardians with the current location and an “Emergency” notification.
	2.	User Notification:
	•	If the user does not respond to the guardian alert within 3 minutes, the app sends a second alert to the user, urging them to confirm their safety.
	3.	Police Notification:
	•	If the user still does not respond after another 3 minutes, the system escalates the alert to local authorities, providing real-time location data and information about the situation.

c. Battery Monitoring

	•	Battery Level Check: The app continuously monitors the device’s battery level.
	•	Alert for Low Battery: If the battery falls below a critical threshold (e.g., 20%), an alert is sent to guardians to inform them that the user may not be able to reach safety.

3. Flowchart

Here’s a simplified flowchart illustrating the process:

+-----------------+
|   Start Route   |
|  Tracking User  |
+-----------------+
        |
        v
+-----------------+
|   Calculate ETA |
+-----------------+
        |
        v
+----------------------------+
|  Delay Detected?           |
|  (User deviates from ETA)  |
+----------------------------+
       /      \
     Yes       No
      |         |
      v         |
+----------------------------+
|  Send Alert to Guardians   |
+----------------------------+
      |
      v
+----------------------------+
|  3-Minute Timeout?         |
|   (User does not respond)   |
+----------------------------+
       /       \
     Yes        No
      |          |
      v          |
+------------------------------+
|  Send Alert to User         |
+------------------------------+
      |
      v
+------------------------------+
|  3-Minute Timeout?          |
|  (User does not respond)     |
+------------------------------+
       /       \
     Yes        No
      |          |
      v          |
+------------------------------+
|  Notify Police               |
|  with Location Details       |
+------------------------------+
      |
      v
+-----------------+
|   Monitor Battery|
|   Levels         |
+-----------------+

Conclusion

This structure ensures that users have a comprehensive safety mechanism in place while traveling. The combination of real-time monitoring, behavior detection, and a multi-tier alert system can significantly enhance public safety for women in urban areas. 
5.	Implementation Methodologies:
	•	Agile Development: If you followed an Agile approach, mention the use of sprints and iterative development.
	•	User-Centered Design: Describe how user feedback shaped the features and interface.
6.	Challenges Faced:
	may challenges were we did not get free API for the same we could not compleat my app
7. ppt
8. name:
Om Sawant
Vijay Kota
Kinjal Gawali
Sneha Hande
   

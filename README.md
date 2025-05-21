Project Overview

1.	Objective:<br>
	• “femshield aims to enhance public safety for women by utilizing AI-powered surveillance cameras and a mobile app for real-time alerts.”<br>
2.	Key Features:<br>
	•	AI-Powered Surveillance: Cameras that detect unusual behavior and alert the user or authorities.<br>
	•	Real-Time Alerts: Notifications sent to guardians and authorities based on detected threats.<br>
	•	Route Tracking: Live tracking of the user’s route from location A to B.<br>
	•	Battery Monitoring: Alerts if the device’s battery is running low.<br>
	•	Escalation Alerts: A three-step alert system that notifies guardians, the user, and finally the police if travel is delayed.<br>
3.	Technological Innovations:<br>
	•	Behavior Detection Algorithms: Using AI to analyze video feeds in real-time.<br>
	•	Mobile Application: A user-friendly interface for alerts and monitoring.<br>
	•	Cloud-Based Data Storage: For storing user data and alert logs securely.<br>
4.	User Flow:<br>
	To explain how the core AI functionalities and alert system work for your SafeZone AI project, we can break it down into several key components:<br>

1. Core AI Functionalities<br>

a. Surveillance System<br>

	•	AI-Powered Cameras: These cameras use computer vision algorithms to detect and recognize people, vehicles, and suspicious behavior (e.g., aggressive gestures, loitering).<br>
	•	Behavior Detection: This involves analyzing the captured video feed in real-time to identify potentially threatening actions. Techniques like object detection and action recognition can be employed.<br>

b. Data Processing and Analysis<br>

	•	Real-Time Data Processing: The video feeds from cameras are processed using AI models (e.g., LLaMA or similar) to extract meaningful information.<br>
	•	Event Triggering: If suspicious behavior is detected, it triggers an alert.<br>

c. User Interface<br>

	•	Mobile App: A mobile app allows users to interact with the system, receive alerts, and send emergency signals.<br>
	•	Community Engagement: Users can report incidents or share information through the app.<br>

2. Alert System Mechanism<br>

The alert system can be broken down into three main stages, including conditions under which alerts are triggered.<br>

a. Route Tracking and Delay Detection<br>

	•	Real-Time Tracking: The app tracks the user’s location from point A to point B.<br>
	•	Expected Travel Time Calculation: Based on distance and traffic conditions, the app calculates the expected travel time.<br>
	•	Delay Detection: If the user deviates from the expected route or delays beyond a set threshold (e.g., 10 minutes), the alert system initiates.<br>

b. Three-Step Alert Escalation<br>

	1.	Initial Alert to Guardians:<br>
	•	If a delay is detected, the app sends an alert to the user’s designated guardians with the current location and an “Emergency” notification.<br>
	2.	User Notification:<br>
	•	If the user does not respond to the guardian alert within 3 minutes, the app sends a second alert to the user, urging them to confirm their safety.<br>
	3.	Police Notification:<br>
	•	If the user still does not respond after another 3 minutes, the system escalates the alert to local authorities, providing real-time location data and information about the situation.<br>

c. Battery Monitoring<br>

	•	Battery Level Check: The app continuously monitors the device’s battery level.<br>
	•	Alert for Low Battery: If the battery falls below a critical threshold (e.g., 20%), an alert is sent to guardians to inform them that the user may not be able to reach safety.<br>

3. Flowchart<br>

Here’s a simplified flowchart illustrating the process:<br>

+-----------------+<br>
|   Start Route   |<br>
|  Tracking User  |<br>
+-----------------+<br>
        |<br>
        v<br>
+-----------------+<br>
|   Calculate ETA |<br>
+-----------------+<br>
        |<br>
        v<br>
+----------------------------+<br>
|  Delay Detected?           |<br>
|  (User deviates from ETA)  |<br>
+----------------------------+<br>
       /      \<br>
     Yes       No<br>
      |         |<br>
      v         |<br>
+----------------------------+<br>
|  Send Alert to Guardians   |<br>
+----------------------------+<br>
      |<br>
      v<br>
+----------------------------+<br>
|  3-Minute Timeout?         |<br>
|   (User does not respond)   |<br>
+----------------------------+<br>
       /       \<br>
     Yes        No<br>
      |          |<br>
      v          |<br>
+------------------------------+<br>
|  Send Alert to User         |<br>
+------------------------------+<br>
      |<br>
      v<br>
+------------------------------+<br>
|  3-Minute Timeout?          |<br>
|  (User does not respond)     |<br>
+------------------------------+<br>
       /       \<br>
     Yes        No<br>
      |          |<br>
      v          |<br>
+------------------------------+<br>
|  Notify Police               |<br>
|  with Location Details       |<br>
+------------------------------+<br>
      |<br>
      v<br>
+-----------------+<br>
|   Monitor Battery|<br>
|   Levels         |<br>
+-----------------+<br>

Conclusion<br>

This structure ensures that users have a comprehensive safety mechanism in place while traveling. The combination of real-time monitoring, behavior detection, and a multi-tier alert system can significantly enhance public safety for women in urban areas. <br>
5.	Implementation Methodologies:<br>
	•	Agile Development: If you followed an Agile approach, mention the use of sprints and iterative development.<br>
	•	User-Centered Design: Describe how user feedback shaped the features and interface.<br>
6.	Challenges Faced:<br>
	may challenges were we did not get free API for the same we could not compleat my app<br>
7. ppt<br>
8. name:<br>
Om Sawant<br>
Vijay Kota<br>
Kinjal Gawali<br>
Sneha Hande<br>
   

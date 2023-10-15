## Inspiration
The inspiration behind PorchSentry came from the pressing issue of package theft, which is highly prevalent in residential porches. I initially wanted to create a solution that not only detects package thieves, but also actively protects user deliveries in a friendly and efficient way. I thought about the implementation of firehose spray, but I eventually went with a simple camera due to hardware limitations.

## What it does
PorchSentry is an innovative app that integrates with Wyze Security Cameras. It uses machine learning models based on TensorFlow and OpenCV to detect potential porch pirates attempting to steal packages. The app can distinguish between the primary user and malicious users, preventing unauthorized removal of packages.

## How we built it
PorchSentry was built using a combination of TensorFlow and OpenCV for the machine learning aspect. We integrated these technologies with the Wyze Security Camera system to provide real-time package theft detection and prevention.

## Challenges we ran into
1. **Training the Model:** Developing and training the machine learning model to accurately detect package thieves required extensive data collection and fine-tuning.
2. **Integration with Wyze Cameras:** Ensuring seamless integration with Wyze Security Cameras and real-time alerts was a technical challenge.
3. **User-Friendly Interface:** Easy-to-understand text that displays current housing threats live.

## Accomplishments that we're proud of
1. **Effective Package Protection:** PorchSentry successfully prevents unauthorized access to packages, enhancing the security of users' deliveries.
2. **Real-Time Detection:** The app provides real-time alerts and notifications, allowing users to respond quickly to potential theft attempts.
3. **Data Labeling:** Allows users to report successful and unsuccessful package protection and theft prevention attempts as a means to improve the algorithm.
4. **Cost-Reduction** Reduces the current cost of door alarm systems like Amazon Blink, Amazon Ring, Google Home Security, and Arlo per camera.

Blink: 110 dollars + 30 dollars per year basic plan
Ring: 180 dollars + 50 dollars per year basic plan
Arlo Home Security: 250 dollars + 60 dollars per year basic plan
Google Home Security: 400 dollars + 100 dollars per year basic plan

## What we learned
1. **Machine Learning Expertise:** We gained valuable experience in machine learning and computer vision, particularly in training models for object detection.
2. **Integration Challenges:** We learned how to integrate our technology with existing hardware, like Wyze Security Cameras, and overcome the associated challenges.
3. **Math** I learned how to differentiate and incorporate linear algebra into the computer detection model used in a camera especially with tennsorflow and ridge-regression... etc.

## What's next for PorchSentry
In the future, we plan to further improve and expand PorchSentry:
1. **Enhanced Detection:** Continuous refinement of the machine learning model to improve detection accuracy and reduce false alarms.
2. **Wider Camera Compatibility:** Expanding compatibility with various security camera systems to reach a broader user base.
3. **Community and Social Features:** Adding features to connect neighbors and communities, allowing them to share security information and alerts.
4. **Mobile Alerts:** Developing a mobile app for easy access to alerts and controls on the go.

PorchSentry is committed to providing effective solutions for package theft prevention while evolving its methods to meet the needs of users and enhance security.

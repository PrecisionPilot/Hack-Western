# Hack-Western
Hack Western 10 Submission

## 💡 Inspiration 🌍
Our inspiration stems from a deep commitment to inclusivity. Recognizing the challenges faced by disabled individuals in accessing the internet, our team set out to create a solution that empowers users to browse effortlessly using only one’s face. Our goal is to break down barriers and provide a seamless online experience for everyone.

## 🎙️ What Gazy does 🚀
Gazy revolutionizes web browsing by allowing users to navigate entirely with their face. Whether it's blinking to click, tilting to scroll, or even talking to type, Gazy provides a comprehensive and intuitive interface that caters specifically to the needs of disabled individuals. It opens up a world of possibilities, ensuring that browsing the internet becomes a more accessible and enjoyable experience.

## 💬 How we built Gazy 🛠️
The front-end was developed on React and the user authentication was built on Firebase. The backend was developed on Python, we harnessed the power of MediaPipe to implement real-time face detection and landmark recognition. To play audio, we utilized PyAudio, and we leveraged Google Cloud’s Speech to Text to convert voice commands to text. Lastly, PyGUI was used to craft the actual mouse movement, scrolling, clicking, and typing!

## 🚧 Challenges we ran into 🚧
Throughout this hackathon, we ran into a plethora of challenges. The main challenge proved to be iris tracking. The intricacies required to accurately track the movement of the iris and projecting that movement onto the 2D screen as mouse movement proved to be difficult. Additionally, identifying a dependable reference point for facial gestures presented its own set of challenges. Our team iteratively tested different scaling factors and points in order to optimize the result. Finally, during the development process, some of our teammates fell ill. However, overcoming these health challenges highlighted the resilience of our team members.

## 🌟 Accomplishments that we're proud of 🎉
We are proud of developing a fully deployed, functional product in only 36 hours. Our team worked cohesively leveraging each member’s strengths to streamline the development process. Specifically, our team takes pride in navigating the challenge of facial movement in innovative ways. By thinking outside the box, our team crafted solutions through comparing the delta x and y coordinates, and taking the tan to find the angle between the head and the y-axis. These innovative methods not only demonstrate our problem-solving skills, but also our persistence to our cause.

## 🚀 What we learned 📚
We learned a lot about OpenCV! Specifically, utilizing OpenCV in tangent with a variety of Python libraries and pretrained models to perform a variety of tasks on the user's face through the process of landmarking. Furthermore, our front-end developer learned to create a fully responsive website on React to complement our software.

## 💫 What's next for Gazy 🌟
Though fully functional, our mouse movement is a little janky, and the eye tracking is not fully complete. Our goal in the future is to smoothen out the movement of the mouse, projecting the user's gaze directly onto the screen and completely eliminating the need to move the mouse. Furthermore, we wish to implement voice activated commands to facilitate the process of navigating the app, and possibly an emergency alarm button for hospitals, in the case that patients are unable to move.

## 🌐 Best Domain Name from Domain.com
As a part of our project, we registered helpinghand.select using GoDaddy! You can also access it [here](https://www.helpinghand.select/).

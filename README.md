This repo was used as the project repository for the final project for *CMPSC 445: Applied Machine Learning in Data Science* at Penn State. Group project members included [Andrew Kuziel](https://www.linkedin.com/in/andrew-kuziel-371586153/), William Miller, [Jordan Sharkey](https://www.linkedin.com/in/jordan-sharkey-562a361b6/), and [Candace Todd](https://www.linkedin.com/in/candace-todd/).

The intent behind our project is to advance the cause of utilizing machine learning for safety and security in the real world. Specifically, we want to promote safety in the most vulnerable places, places that serve vulnerable populations but lack the resources to fully staff security personnel (such as schools and hospitals). Shootings have become a more prevalent problem in our nation’s recent history, and we wanted to create a product that would bring us closer to putting it in the past. To achieve this, we’ve developed a Convolutional Neural Network that will take in a photo and predict whether or not a gun is contained in that image. We hope that this project can be used as the building block for an algorithm that can be used to monitor real-time security camera footage. While our project only works on still pictures, we are hoping the principles used in the creation of the project can further our understanding, and other’s, so that we can begin to get closer to a solution to this problem.

The following ReadMe is from the original dataset owners:

---

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]
# Weapon detection datasets

An automatic weapon detection system can provide the early detection of potentially violent situations that is of 
paramount importance for citizens security. One way to prevent these situations is by detecting the presence of 
dangerous objects such as handguns and knives in surveillance videos. Deep Learning techniques based on Convolutional 
Neural Networks can be trained to detect this type of object.

The weapon detection task can be performed by different approaches of combining a region proposal technique with a 
classifier, or integrating both into one model. However, any deep learning model requires to learn a quality image 
dataset and an annotation according to the classification or detection tasks.

Weapon detection Open Data provides quality image datasets built for training Deep Learning models under the 
development of an automatic weapon detection system. Weapons datasets for image classification and object detection 
tasks are described and can be downloaded below. The public datasets are organized depending on the included objects 
in the dataset images and the target task.

You can read more information about these dataset in 
[Weapon detection Open Data](https://dasci.es/transferencia/open-data/24705/), and related works in 
[Weapon detection for security and video surveillance project](https://sci2s.ugr.es/weapons-detection).

Drive link [full dataset](https://drive.google.com/file/d/1Szc920DAh5kU8Qk38Doq0znEVR1QmTZS/view?usp=sharing).

### Direct link:

[Pistol classification](../master/Pistol%20classification)

[Pistol detection](../master/Pistol%20detection)

[Knife classification](../master/Knife%20classification)

[Knife_detection](../master/Knife_detection)

[Weapons and similar handled objects](../master/Weapons%20and%20similar%20handled%20objects)

### Contact

[***Fransco Pérez Hernandez***](https://www.linkedin.com/in/franciscoperezhernandez/)
- Personal email: fperezhernandez92@gmail.com
- Institutional email: fperezhernandez@ugr.es

[***Alberto Castillo Lamas***](https://www.linkedin.com/in/albertocastillolamas/)
- Personal email: alcasla90@gmail.com
- Institutional email: albertocl@ugr.es

### License

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

# hybrid-image-generation

Hybrid Image is an image that can be perceived in one of two different ways. The view depends on the viewing distance. It is based on how human beings process visual input. It is very commonly used trick for optical illusions.

A popular example of a hybrid image is shown below:

<img src="https://user-images.githubusercontent.com/53681666/76625043-d2de0500-650c-11ea-95b7-6312bf3629a0.jpg" alt="caption needed" width="400" height="300">

Looking at the picture from a short distance, one can see a sharp image of a man, with only a hint of blurry distortion hinting at the presence of an overlaid image. Viewed from a distance in which the fine detail blurs, the unmistakable face of a cat emerges.

Similarly, in the example I have taken 2 images - First of the KFC logo and second of the Macdonald's mascot. They are converted to their frequency domain and then a weighted frequency image is generated with certain proportions of each image. That newly generated image is now converted back to the spatial domain using inverse fourier transform to represent the combined image.

<img src="https://user-images.githubusercontent.com/53681666/76624781-50554580-650c-11ea-8d04-9ce71c9e3ed5.jpg" alt="caption needed" width="300" height="250">
<img src="https://user-images.githubusercontent.com/53681666/76624839-6bc05080-650c-11ea-95e1-eaf2c287aee8.jpg" alt="caption needed" width="320" height="250">

This is the combined image finally generated

<img src="https://user-images.githubusercontent.com/53681666/76626413-8516cc00-650f-11ea-8950-cd7b859fd053.jpg" alt="caption needed" width="300" height="250">

We can tweak the combination ratio to get one of the image as more prominent one than the other. If we remove the high frequencies of one of the images and combine with the low frequency of the other image we can get a exact hybrid image.

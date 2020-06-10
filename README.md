# Intelligent Olfactory Sensor

This personal research has been motivated by Phylira, an AI solution to create new fragrances developed by IBM researchers and Symrise, and the article about olfactory sensor technologies written by ETRI (Electronics and Telecommunications Trends).

There are various types of olfactory intelligence applications and the perfume and fragrances market is one of them. This project uses a Machine Learning technique for a olfactory sensor to digitize and distinguish the sense of smell. Since anything that smells fragrant releases VOCs into the air, CCS811, an ultra-low power digital gas sensor solution that senses a wide range of Total Volatile Organic Compounds (TVOCs), will be used as a main component of the sensor. Various scent samples will be collected and used for deep learning with TensorFlow. If the sensor successfully detects the smell and tells the difference between different samples, then actual perfume products will be used to test the sensor. Also, data from the samples will be visualized and represented on the S-Catcher web app, the online encyclopedia of perfume and fragrances.

## Technologies
- Olfactory sensor using Arduino Uno and CCS811
- Data analysis and visualization in Python using Pandas
- Deep Learning with TensorFlow
- Supervised Machine Learning algorithm: Support Vector Machine (SVM) Radial Basis Function (RBF) Kernel

## Fragrance Wheel and Scent Families
Every perfume and after shave is based on the different scent families. A scent family has distinctive characteristics and often individuals will gravitate toward one scent family over another when choosing personal fragrances. Scent families are broken up into four main categories:

- Floral

    Sweet and flowery such as roses, jasmine, lilies and peonies
- Oriental

    Rich, sensual, warm, sweet, and even a little spicy with interesting notes of cardamom, cinnamon, vanilla alongside of jasmine, orchid and orange blossom
- Woody

    Mysterious, captivating, wood-based smells like cedarwood, sandalwood, vetiver and amber
- Fresh

    Refreshing, zesty and vibrant smells usually comprised of citrus, water and green notes

## Fragrance Notes
The top notes of a fragrance are what you smell immediately after spraying your perfume, which forms the first impression of the fragrance. The middle, or heart, notes appear the tope notes have disappeared. Base notes are what is left at the end. It is the smell that people remember the most because it is the longest lasting. <br></br>
These different fragrance types denote the strength and how long they are likely to last once you have sprayed them. The more perfume oil with alcohol, the stronger the fragrance and the longer it will last.

- Eau de Parfum: 10-20% of perfume oil and last around 8 hours

    EDP is the strongest type of perfume and a popular choice with both perfume brands and customers
- Eau de Toilette: 5-15% of perfume oil and last somewhere between 4 and 7 hours

    EDT make a great first impression since they often have a quick burst of beautiful smells before fading
- Eau de Cologne: 2-4% of perfume oil and last perhaps around 2 to 3 hours
    
    EDC often used as a body splash to freshen up at regular intervals
- Eau Fraiche: 1-2% of perfume oil which is incredibly light and only last a couple of hours at best

    EF is great for creating a subtle, delicate fragrance


## References
- 10 Machine Learning Algorithms (https://www.dataquest.io/blog/top-10-machine-learning-algorithms-for-beginners/)
- Data Anaylsis using Pandas (https://www.geeksforgeeks.org/python-data-analysis-using-pandas/)
- Supervied ML Classification (https://builtin.com/data-science/supervised-machine-learning-classification)
- TensorLow for Beginners (https://www.datacamp.com/community/tutorials/tensorflow-tutorial)
- TensorFlow Customization (https://www.tensorflow.org/tutorials/customization/basics)
- TensorFlow Customition Docs (https://github.com/tensorflow/docs/blob/master/site/en/tutorials/customization/basics.ipynb)
- TensorFlow Model in Python (https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/export-model-python)

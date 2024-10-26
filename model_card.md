# Model Card

## Model Details
This model was developed for binary classification using a RandomForestClassifier. It is trained to predict if 
an individual's income exceeds $50,000 annually. This is based on demographic features from a Census Income Dataset 
donated in 1996 that includes 48842 instances and 14 features.

## Intended Use
This model is intended for skill building and learning purposes. It demonstrates classification techniques on 
demographic data and how ML models can be set up for pipeline automation.

## Training Data
This model utilizes a portion of the Census Income dataset that has a mix of demographic features like
age, sex, and race. A few columns, like 'occupation', include null values.

## Evaluation Data
The rest of the Census Income dataset was used for the evaluation data. 

## Metrics
The model's performance was evaluated with three main metrics:

- Precision: Measures the accuracy of positive predictions.
- Recall: Measures the ability to identify all positive instances.
- F1-score: The harmonic mean of precision and recall, balancing both metrics.

Overall performance:

Precision: 0.7269
Recall: 0.6172
F1-score: 0.6676

Class-based performance:

- By Work Class: Performance varied significantly. For instance, 'Self-emp-inc' class had an F1-score of 0.7721, while 
'Without-pay' had an F1-score of 1.0, indicating perfect predictions in this small subgroup.
- By Education Level: Individuals with higher education levels (e.g., Doctorate and Prof-school) had higher F1-scores 
(0.8402 and 0.9078, respectively), while lower education levels (e.g., 1st-4th) showed poor performance (F1-score of 0).
- By Marital Status and Relationship: Model performance varied based on these features, reflecting potential disparities 
in data representation for different marital statuses or family roles.

## Ethical Considerations
This model was developed with a limited amount of testing and older data. If the
model is used outside of it's intended purposes, it could provide inaccurate information.

## Caveats and Recommendations
The dataset was donated in 1996, and may not reflect current socio-economic trends. The model 
might not accurately predict current trends. Cross-validation on additional datasets
would be needed to improve the quality of the model. 
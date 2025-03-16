# **CodeOp Individual project**  

The dataset was downloaded in [Kaggle](https://www.kaggle.com/competitions/obesity-level-prediction-fall-2024/data) where the goal of the competition was to build a predictive model with the best accuracy score to predict the weight classes.  
However, I used this dataset for the *CodeOp* individual exam where the goal was to use a dataset(s) and get insights and be able to present how we deal with the dataset(s) to adress business questions.  
I chose this dataset because of the wide presence of missing values. Hence, I had to deal first with these missing values that cannot just be removed or just imputed using classical methods (using the average or the median).  

I used KNNImputer to impute the missing values and used its output also to help me understand the dataset.  
I used logistic regression to see if there were features that would individually help to discriminate a feature from another.  

My business questions were:  
- Is there a feature other than weight that is strong enough to discriminate a weight class? I found that "Age" was the only feature strong enough to help by itself to distinguish *Insufficient_Weight* from the other classes.  

- Is there a difference between males and females? I other words, if we separate the 2 gender, will we see a difference in term of feature weights? I found that "Age" in *Insufficient_weight* was actually impactful only in males. In other words, in this dataset males of *Insufficient_weight* are more likely to be younger than all the other classes and younger than the females *Insufficient_Weight*.  

- Is there a relationship between sncaking ("CAEC") and obesity? In this dataset, both *Insufficient_Weight* and *Normal_Weight* are snacking "sometimes" and "frequently" while the highest proportion of no snackers was present in *Overweight_Level_I*. Importantly, I found that these no snackers in *Overweight_Level_I* were more likely to be short males of average age (average of the entire dataset).  

In other words, using ML and traditional exploration methods, I was able to discriminate a small group of individuals (43) defined by 5 dimensions (5 features):  
- NObeyesdad: *Overweight_Level_I*;  
- Gender: mostly Male;  
- Age: average 21 years old;
- Height: average 1.62m
- CAEC (snacking): No  

I hope you will enjoy reading this analysis as much as I did when discovering these insights.  

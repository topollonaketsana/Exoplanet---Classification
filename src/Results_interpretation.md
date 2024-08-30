### From `src.ipynb` the results are found to be:

1. Accuracy:

- Logistic Regression: 98.38%

- Random Forest: 98.38%

- Both models have identical accuracy, which indicates that they are performing in similar way for overall.



2. Observations:


True Positives: 
- Logistic Regression correctly predicted more positives (907) compared to Random Forest (896).
- these are the planets that the model correctly classified as exoplanets.


True Negatives:
- The Random Forest model correctly predicted more negatives (986) compared to Logistic Regression (975). 
- The model successfully identified these as not being exoplanets



False Positives: 
- Random Forest has fewer false positives (9) than Logistic Regression (20)
- These represent the non-exoplanets that the model incorrectly classified as exoplanets

False Negatives:
- Logistic Regression has fewer false negatives (11) than Random Forest (22), 
-  These are actual exoplanets that the model failed to identify




3. Model Consistency

Both models show high precision, recall, and f1-scores, indicating that they are consistent in their predictions.
The confusion matrix reveals a slight trade-off between the two models: Random Forest is slightly better at minimizing false positives, while Logistic Regression is slightly better at minimizing false negatives.
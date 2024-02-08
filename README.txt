                                                     BRAIN STROKE PREDICTION


INTRODUCTION:
	
	Brain stroke prediction involves the application of predictive models to assess the likelihood of an individual experiencing a stroke, a critical medical condition where the blood supply to the brain is disrupted, leading to potential long-term disabilities or even death.By leveraging machine learning algorithms on relevant health data, such as age, average glucose level, BMI, gender, presence of hypertension, heart disease, marital status, work type, residence type, and smoking status, predictive models can be trained to identify patterns and associations that may indicate a higher risk of stroke.

GOAL:
	
	The goal of such predictive approaches is to contribute to personalized healthcare strategies, emphasizing proactive measures to reduce the incidence and impact of strokes on individuals and communities.

ATTRIBUTES:
	1) gender: "Male", "Female" or "Other"
	2) age: age of the patient
	3) hypertension: 0 if the patient doesn't have hypertension, 1 if the patient has hypertension
	4) heart_disease: 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease
	5) ever_married: "No" or "Yes"
	6) work_type: "children", "Govt_jov", "Never_worked", "Private" or "Self-employed"
	7) Residence_type: "Rural" or "Urban"
	8) avg_glucose_level: average glucose level in blood
	9) bmi: body mass index
	10) smoking_status: "formerly smoked", "never smoked", "smokes" or "Unknown"*
	11) stroke: 1 if the patient had a stroke or 0 if not

*Note: "Unknown" in smoking_status means that the information is unavailable for this patient


ALGORITHMS:

	Among KNN, Logistic Regression, Decision Tree, and Random Forest models, Random Forest achieved the highest accuracy of 98%, making it the most effective model for the given dataset.

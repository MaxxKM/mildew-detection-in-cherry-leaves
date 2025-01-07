# Mildew Detection in Cherry Leaves
- Live App Link: [https://powdery-mildew-detection-mkm-c29095774113.herokuapp.com]
(https://powdery-mildew-detection-mkm-c29095774113.herokuapp.com)

## Dataset Overview  
The dataset is sourced from Kaggle. We developed a hypothetical user story where predictive analytics can be applied to a real-world project in the workplace.  
The dataset consists of over 4,000 images captured from the client’s cherry crop fields. The images depict both healthy cherry leaves and those affected by powdery mildew, a fungal disease impacting many plant species. The cherry plantation is one of the company’s premium products, and there is significant concern about maintaining high product quality in the market.

## Business Requirements  
The cherry plantation at Farmy & Foods is dealing with powdery mildew on its cherry trees. Currently, detecting this disease involves manual verification, where an employee spends around 30 minutes per tree taking sample leaf images and visually inspecting whether the tree is healthy or infected with mildew. If mildew is detected, the employee must then apply a specific fungicide treatment, which takes an additional minute. Given the thousands of cherry trees spread across multiple farms, this manual process is not scalable.  

To improve efficiency, the IT team has proposed implementing an ML system that can instantly determine if a cherry tree is healthy or affected by mildew from an image of its leaves. Similar manual processes exist for other crops to detect pests, and if successful, this initiative could be expanded to all crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods from their plantations.

### Requirement 1  
The client is interested in visually distinguishing between healthy cherry leaves and those affected by powdery mildew.  

### Requirement 2  
The client is interested in predicting whether a cherry leaf is healthy or contains mildew.

## Hypothesis and Validation  
Powdery mildew-infected leaves exhibit a distinctive powdery white layer on the surface, which can be visually detected.  
The hypothesis is validated by collecting an image dataset from the client and creating an image montage comparing healthy and infected leaves.  
The hypothesis is further tested through average image analysis.

## Mapping Business Requirements to Data Visualizations and ML Tasks  

### Business Requirement 1  
The study should include an analysis of:  
- Average images and variability images for each class (healthy or powdery mildew).  
- Differences between the average healthy and average mildew-affected cherry leaves.  
- An image montage showcasing each class.  

### Business Requirement 2  
The ML system should predict whether a cherry leaf is healthy or contains mildew.  
The dashboard should feature an image montage and a prediction feature.

## ML Business Case  

### What are the business requirements?  
The client seeks a tool to accurately differentiate between healthy cherry leaves and those affected by mildew. Given that ML can effectively classify images, this need aligns well with ML capabilities.

### Can conventional data analysis address any of the business requirements?  
Requirement 1 can be addressed through traditional data analysis methods. However, Requirement 2 cannot be solved using conventional approaches, making ML necessary to tackle this challenge.

### Does the client need a dashboard or an API endpoint?  
The client requires a dashboard.

### What constitutes a successful project outcome for the client?  
The client should be able to visually differentiate between healthy and mildew-affected leaves and predict if a leaf is healthy or infected by mildew via an interactive dashboard.

### What are the model's inputs and intended outputs?  
The input is a cherry leaf image, and the output is a prediction indicating whether the leaf is healthy or contains mildew.

### Does the data suggest a particular model?  
The data points towards a binary classification model.

### What are the criteria for the performance goal of predictions?  
The client has agreed upon an accuracy goal of 97%, though the model has been trained to achieve 99%.

### How will the client benefit?  
By reducing manual inspection time, the client will be able to supply the market with higher-quality, mildew-free products. The ability to scale operations across farms will further enhance productivity and efficiency.

## Dashboard Design  
- A project summary page outlining the dataset and the client’s requirements.  
- A page summarizing the findings from the study on visually differentiating between healthy and mildew-affected cherry leaves.  
- A page with a link to download a set of cherry leaf images for live prediction (Kaggle repository).  
- An interactive User Interface featuring a file uploader widget, where users can upload multiple images. Each image will display along with a prediction statement indicating whether the cherry leaf is healthy or infected with mildew, along with associated probabilities.  
- A table summarizing the image names and prediction results, along with a download button to obtain this data.  
- A page detailing the project hypothesis and how it was validated throughout the project.  
- A technical page showcasing model performance metrics.

## Unfixed Bugs  
No current bugs as current, however there is a upcoming problem due to Heroku-20 stack becoming deprecated. This will
slowly cause bugs as time goes on and eventually no longer work.

Also the python version used (only compatible one with this project) is no longer supported meaning it could also
cause bugs in the future

## Deployment  

### Heroku  
- Live App Link: [https://powdery-mildew-detection-mkm.herokuapp.com/](https:/powdery-mildew-detection-mkm.herokuapp.com/)  
- Set the `runtime.txt` Python version to a currently supported Heroku-20 stack.  
- The project was deployed to Heroku using the following steps:  
  1. Log in to Heroku and create an app.  
  2. At the Deploy tab, select GitHub as the deployment method.  
  3. Select your repository name and click Search. Once found, click Connect.  
  4. Choose the branch to deploy, then click Deploy Branch.  
  5. The deployment process should proceed smoothly if all necessary files are functional. Click the "Open App" button at the top of the page to access your application.  
  6. If the slug size is too large, add large files not needed for the app to the `.slugignore` file.

## Main Data Analysis and Machine Learning Libraries  
- **numpy**: Used to convert images into arrays for analysis and ML training, calculating means and standard deviations.  
- **pandas**: Facilitates dataset manipulation, including saving prediction reports as dataframes.  
- **matplotlib**: Utilized for plotting images, including augmented and data images.  
- **seaborn**: Used to visualize image datasets, especially when plotting multiple axes and features.  
- **tensorflow**: The main ML framework for building, training, and validating the model.  
- **streamlit**: Used to build the interactive dashboard.  
- **keras**: Employed for image augmentation and ML model training.

## Credits  
- The code for data modeling, visualization, and ML model creation, training, and deployment was adapted from Code Institute lessons and walkthrough projects.  
- The dashboard and `README.md` file were constructed using provided templates.  


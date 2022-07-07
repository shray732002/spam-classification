# Spam-Classification (deployed on Heroku)

App link:- [My spam-classifier app](https://app-spam-classification.herokuapp.com/)

In this project i have made a simple app using flask and render template to it using html.

In this project you will get to know about major topics like:-
* Data preprocessing
* NLP(Natural language preprocessing)
* How to apply ML models and do parameter tuning of it to get better(accurate) results
* Pickling the model

### Steps from beginning(from making a model) to end(deploying it on heroku)

* Make a conda environment :- conda create -n {env_name}
* After creating environment you need to activate it :- conda activate {env_name}
* try to download each and every library you need in your project
* then use pip freeze command to collect name and version of libraries in your requirements.txt file pip freeze > requirements.txt
* Make a flask app and add a Procfile so that heroku app will know where it has to search for your app in your github repository
* Then just go to heroku app and deploy your model

### Screenshots
* Spam message:- 
 ![spam_message](https://github.com/shray732002/spam-classification/blob/main/screenshot/message-spam.png)
   * Result:-
    ![spam_result](https://github.com/shray732002/spam-classification/blob/main/screenshot/spam.png)
* Ham message:-
 ![ham_message](https://github.com/shray732002/spam-classification/blob/main/screenshot/message-notspam.png)  
   * Result:-
    ![ham_result](https://github.com/shray732002/spam-classification/blob/main/screenshot/notspam.png)

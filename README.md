# Digits Recognition App

Digits recognition app using:

* Python
* FastApi
* JavaScript
* Jinja2
* HTML

the model was trained on Kaggle using Pytorch lightning and transfer learning. The Kaggle notebook is linked inside the website.

The website uses HTML and javascript to paint on the canvas and then send the image to FastApi to recognize the digit.

This project was created to learn JavaScript, HTML, and FastAPI framework.

The website was deployed to Heroku.

Instructions to deploy:

*  Install docker
*  Install heroku cli
*  `heroku login`
*  `heroku create app $appName`
*  `heroku container:login`
*  `heroku container:push $containerName`
*  `heroku container:release $containerName`

Then you can go to your website.

For testing locally use:

* docker build --rm -t digit-app
* docker run -p 80:80 digit-app serve

then got to `localhost:80` in your browser
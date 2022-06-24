# Ecommerce Website

> A webapp for men's fashion.

## :hammer: Built With

- HTML, CSS
- Python, Django, PostgreSQL

### :computer: Setup
To get a local copy up and running follow these simple example steps.

##### Cloning the repository:  
 ```bash 
git clone https://github.com/blancc-page/week11-capstone-app/
```
##### Navigate into the folder and install requirements  
 ```bash 
cd week11-capstone-app 
```
##### Install and activate Virtual  
 ```bash 
python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations ecommerceApp
 ``` 
 Now Migrate  
 ```bash 
python manage.py migrate 
```
##### Run the application  
 ```bash 
python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  

## Behaviour Driven Development

> A user should be able to:

- sign in
- view items on sale
- add items to a cart
- view cart before purchase
- user can complete purchase

## :trollface: Authors

👤 **Moses Muta**

- GitHub: [@githubhandle](https://github.com/blancc-page)
- LinkedIn: [LinkedIn](<linkedIn link>)


## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

## :muscle: Show your support

    Please give a⭐️if you love this project.
    

## 📝 License

This project is [MIT](./MIT.md) licensed.
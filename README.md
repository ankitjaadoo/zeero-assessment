# Steps to run the Django Server

## Run the Unit tests
- `python manage.py test`

## Apply Migrations for recent changes
- `python manage.py makemigrations`
- `python manage.py migrate`

## Launch the server
- `python manage.py runserver`

# Deployment on AWS

- Install **AWS CLI** on your system **(Windows/Linux/Mac)** and use the following command to configure AWS setup in your IDE: `aws configure`, and provide the values for Key ID, Access Key, Region etc.

- Set up an EC2 instance with Ubuntu.

- Install required dependencies on this instance using the following commands:

`sudo apt update`
`sudo apt install python3-pip python3-venv nginx`

- Clone your project repository on to this instance. Also setup a virtual environment and install requirements:

`python -m venv venv`
`source venv/bin/activate`
`pip install -r requirements.txt`

- Install **Gunicorn** using the following command:

`pip install gunicorn`

- Configure **Gunicorn** as the WSGI server by creating the **gunicorn.service** file with contents given below inside **/etc/systemd/system**:

```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/countdown_timer
ExecStart=/home/ubuntu/countdown_timer/venv/bin/gunicorn --workers 3 countdown_timer.wsgi:application

[Install]
WantedBy=multi-user.target

```

- Create an **Nginx** server block inside **/etc/nginx/sites-available/countdown_timer** as given below:

```
server {
    listen 80;
    server_name your_domain_or_ip;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

```

- Enable the **Nginx** configuration to allow it to serve as a reverse proxy:

`sudo ln -s /etc/nginx/sites-available/countdown_timer /etc/nginx/sites-enabled`
`sudo nginx -t`
`sudo systemctl restart nginx`

### Access the application now by visiting the instance IP address in the browser.



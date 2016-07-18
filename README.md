# Recipes
Recipes website and app created with Django CMS.

## Create a service
Example
````
[Unit]
Description=simple python script

[Service]
Environment= MY_ENVIRONMENT_VAR =/path/to/file.config
WorkingDirectory=/path/to/script
ExecStart=/usr/bin/python script.py
Restart=always

[Install]
WantedBy=multi-user.target
````

Link to `/etc/systemd/system/`
````
ln -s /path/to/file/my_systemd_script.service /etc/systemd/system/my_systemd_script.service
````

Start the service
````
systemctl daemon-reload
systemctl enable my_systemd_script.service
systemctl start my_systemd_script.service
````

# Throught process Task A production went down: Find where I'm having problems in production

## Check if aplication ist realy down  systemctl status current service 
Ask whether it affected only one or more users
## CPU usage 
- ```top```
- ```free -a ```
- ```free -memory```
## Monitoring alert (Prometheus, Grafana, Dynatrace)
## look at the logs
- path to the logs /var/log
## check if the server is running (Apache)
- ```systemctl status httpd```
## check if the docker is running - docker ps , docker logs
- ```docker ps```
- ```docker logs <container_id>```
## check if the tomcat is running 
- ```ps aux | grep tomcat```
## check if the port is correct
- ```netstat -tulpn```
## I use commnad -  
- ```ping```
## Set up email notifications about application availability to be sent to our mailbox.
## If the application is deployed, a new release is made; if it crashes, a rollback to the original version is performed
## Verify that the application is working after the incident. 
## RCA- root cause analysis will be performed where the problem occurred


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
## check connection 
- ```ping```
### If the application is redeployed or Updated and than it crashed, a rollback can be performed to the previous version.
## Verify that the application is working after the incident. 

# Prevention 
## Set up email notifications about application availability. 
## RCA- root cause analysis will be performed where the problem occurred
## Monitoring alert (Prometheus, Grafana, Dynatrace)


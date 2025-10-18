FROM httpd:2.4

WORKDIR  /app_code

COPY ./index.html/ /usr/local/apache2/htdocs/
COPY ./script.js/  /usr/local/apache2/htdocs/
COPY ./style.css/  /usr/local/apache2/htdocs/
 
EXPOSE 80


#Commented
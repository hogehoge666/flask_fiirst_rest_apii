FROM nginx:latest

LABEL Name=todoapi-proxy Version=0.0.1

EXPOSE 8080

WORKDIR /etc/nginx/conf.d
ADD ./config ./

WORKDIR /usr/share/nginx/html
ADD ./statics ./

CMD ["nginx", "-g", "daemon off;"]
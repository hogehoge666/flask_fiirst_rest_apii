FROM nginx:latest

EXPOSE 8080

WORKDIR /etc/nginx/conf.d
ADD ./config ./

WORKDIR /usr/share/nginx/html
ADD ./statics ./

CMD ["nginx", "-g", "daemon off;"]
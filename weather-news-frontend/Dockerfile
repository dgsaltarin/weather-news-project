### BUILD ###
FROM node:14.17-alpine AS build

WORKDIR /dist/src/app

RUN npm cache clean --force

COPY . .

RUN npm install 

RUN npm run build --prod

### RUN ###

FROM nginx:latest AS ngi

COPY --from=build /dist/src/app/dist/weather-news-frontend /usr/share/nginx/html

COPY /nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

FROM node:16.14.2 as build

# Building the frontend
WORKDIR /app

COPY . .
RUN npm i 

RUN npm run build

# Copy the build content and host it in web server
FROM nginx:latest

COPY --from=build /app/build /etc/nginx/html


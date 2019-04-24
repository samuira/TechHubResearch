FROM node:alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN npm install -g @angular/cli
COPY . .
RUN npm install
RUN npm audit fix --force
RUN npm run build

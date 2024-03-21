FROM node:16.14.2 AS builder
# Set working directory
WORKDIR /frontend
# Copy all files from current directory to working dir in image
COPY . .

# install node modules and build assets
RUN npm install
EXPOSE 8080

# -----------------------
# SETTINGS FOR PRODUCTION
# -----------------------

# RUN npm install && npm run build

# FROM nginx:alpine

# WORKDIR /usr/share/nginx/html/

# RUN rm -rf ./*

# COPY --from=builder /frontend/dist .



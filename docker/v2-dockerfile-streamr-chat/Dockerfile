# @Author: Pizofreude
# 2nd Dockerfile Testrun
# -------------------------------------
# From the official Node image.
FROM node:alpine3.10

# Create app directory.
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the container.
COPY "./logger.js" "./logger.js"
COPY "./package.json" "./package.json"
COPY "./package-lock.json" "./package-lock.json"

# Install npm packages.
RUN npm i

# Define default values for the following environment variables.
ENV STREAMRPORT 2443
ENV DBPORT 4786

# Run the application.
CMD ["node", "logger.js"]
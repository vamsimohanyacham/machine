# Stage 1: Build the application
FROM node:18 AS build

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the entire project to the container
COPY . .

# Build the Vite project for production
RUN npm run build

# Stage 2: Serve the production build with Nginx
FROM nginx:alpine

# Copy the build output from the previous stage
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 3000 to access the app via HTTP
EXPOSE 3000

# Start nginx to serve the production build
CMD ["nginx", "-g", "daemon off;"]

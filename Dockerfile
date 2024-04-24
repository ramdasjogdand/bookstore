# Stage 1: Build Stage
FROM maven:3.8.4-openjdk-11 AS build
WORKDIR /app
COPY . .
RUN mvn clean install

# Stage 2: Deployment Stage
FROM tomcat:9.0.59-jre11 AS deploy
COPY --from=build /app/target/*.war /usr/local/tomcat/webapps/

# Expose the Tomcat port
EXPOSE 8080

# Command to run Tomcat
CMD ["catalina.sh", "run"]



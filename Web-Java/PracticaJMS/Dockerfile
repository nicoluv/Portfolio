FROM gradle:7.2.0-jdk11 AS build
COPY --chown=gradle:gradle . /home/gradle/src
WORKDIR /home/gradle/src
RUN gradle bootJar --no-daemon

FROM openjdk:11.0.12-jre-slim-buster

MAINTAINER Nicol Urena <20181669@ce.pucmm.edu.do>

ENV NOMBRE_APP = 'app_web'
ENV NAME_DB = practica4
ENV spring.datasource.username='sa'
ENV spring.datasource.password=''

VOLUME /tmp

EXPOSE 8080

COPY --from=build /home/gradle/src/build/libs/*.jar mi_app.jar

ENTRYPOINT ["java", "-jar", "mi_app.jar"]


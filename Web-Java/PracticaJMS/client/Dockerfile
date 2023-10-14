FROM gradle:7.2.0-jdk11 AS shadow
COPY --chown=gradle:gradle . /home/gradle/src
WORKDIR /home/gradle/src
RUN gradle shadowJar --no-daemon

FROM openjdk:11.0.12-jre-slim-buster

EXPOSE 61616

COPY --from=shadow /home/gradle/src/build/libs/*.jar client.jar

ENTRYPOINT ["java", "-jar", "client.jar"]
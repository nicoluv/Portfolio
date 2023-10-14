package com.progweb.practicajms.config;

import org.h2.tools.Server;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.sql.SQLException;

@Configuration
public class H2ServerConfiguration {

    @Value("${PORT_DATABASE}")
    private String PORT;

    @Bean
    public Server server() throws SQLException {
        Server.createWebServer("-trace", "-webPort", "0").start();
        return Server.createTcpServer("-tcpPort",PORT, "-tcpAllowOthers", "-tcpDaemon").start();
    }
}

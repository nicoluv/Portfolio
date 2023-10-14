package com.progweb.practicajms.config;

import com.progweb.practicajms.entidades.Sensor;
import com.progweb.practicajms.servicios.ServicioSensor;
import com.google.gson.Gson;
import org.apache.activemq.ActiveMQConnectionFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import javax.jms.*;

@Service
public class Consumidor {
    private ActiveMQConnectionFactory factory;
    private Connection connection;
    private Session session;
    private Topic topic;
    private MessageConsumer consumer;
    private String topicName;
    @Value( "${spring.activemq.broker-url}" )
    private String brokerUrl;

    @Autowired
    private ServicioSensor servicioSensor;


    /**
     *
     */
    public Consumidor() {
        this.topicName = "notificacion_sensores";
    }

    /**
     *
     * @throws JMSException
     */
    public void connect() throws JMSException {

        factory = new ActiveMQConnectionFactory("admin", "admin", brokerUrl);
        connection = factory.createConnection();

        connection.start();
        session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);

        topic = session.createTopic(topicName);
        consumer = session.createConsumer(topic);

        consumer.setMessageListener(message -> {
            try {
                TextMessage messageTexto = (TextMessage) message;
                Sensor sensor = new Gson().fromJson(messageTexto.getText(), Sensor.class);
                servicioSensor.saveSensor(sensor);

            }catch(Exception ex){
                ex.printStackTrace();
            }
        });
    }


    public void closeConnection() throws JMSException {
        connection.stop();
        connection.close();
    }
}

package progweb;

import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import org.apache.activemq.ActiveMQConnectionFactory;

import javax.jms.*;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Producer {
    JsonArray jsonArray = new JsonArray();
    JsonObject jsonMessage = new JsonObject();

    public Producer(){

    }

    public void sendMsg(String topicName, String instance) throws JMSException {

        ActiveMQConnectionFactory factory = new ActiveMQConnectionFactory("tcp://activemq:61616");

        Connection connection = factory.createConnection("admin", "admin");
        connection.start();

        Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);

        MessageProducer producer;

        Topic topic = session.createTopic(topicName);
        producer = session.createProducer(topic);

        double random1 = -400 + Math.random() * (400 + 400);
        double random2 = -400 + Math.random() * (400 + 400);

        double randomTemp = BigDecimal.valueOf(random1).setScale(2, RoundingMode.HALF_UP).doubleValue();
        double randomHum = BigDecimal.valueOf(random2).setScale(2, RoundingMode.HALF_UP).doubleValue();

        JsonObject jsonObject = new JsonObject();
        jsonObject.addProperty("fecha", new SimpleDateFormat("dd/MM/yyyy HH:mm:ss").format(new Date()));
        jsonObject.addProperty("idDispositivo", instance);
        jsonObject.addProperty("humedad", randomHum);
        jsonObject.addProperty("temperatura", randomTemp);

        jsonArray.add(jsonObject);
        jsonMessage.add("data", jsonArray);

        TextMessage msg = session.createTextMessage(jsonObject.toString());
        producer.send(msg);

        producer.close();
        session.close();
        connection.stop();
    }
}

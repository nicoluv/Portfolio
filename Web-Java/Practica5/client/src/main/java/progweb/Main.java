package progweb;

import org.apache.activemq.broker.BrokerService;

import javax.jms.JMSException;

public class Main {
    public static void main(String[] args) throws JMSException, InterruptedException {


        System.out.println("La practica de JMS se esta iniciando");
        try {
            BrokerService broker = new BrokerService();

            broker.addConnector("tcp://0.0.0.0:61616");


            broker.start();
        } catch (Exception ex) {
            ex.printStackTrace();
        }


        while (true) {
            Thread.sleep(44000);
            new Producer().sendMsg("notificacion_sensores", "1");
            System.out.println("enviando...");
            new Producer().sendMsg("notificacion_sensores", "2");
        }

    }



}

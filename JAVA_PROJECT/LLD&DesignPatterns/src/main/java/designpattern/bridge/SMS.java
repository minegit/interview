package designpattern.bridge;

public class SMS implements NotificationSender {

  public void sendNotification() {
    System.out.println("SMS SENT");

  }

}

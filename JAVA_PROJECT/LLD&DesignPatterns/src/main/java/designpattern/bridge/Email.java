package designpattern.bridge;

public class Email implements NotificationSender {

  public void sendNotification() {
    System.out.println("Email sent !!");

  }

}

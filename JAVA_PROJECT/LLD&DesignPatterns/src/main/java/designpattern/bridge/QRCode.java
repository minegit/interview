package designpattern.bridge;

public class QRCode extends Notification {

  public QRCode(NotificationSender notificationSender) {
    super(notificationSender);
  }

  @Override
  public void sendMessage() {
    notificationSender.sendNotification();

  }

}

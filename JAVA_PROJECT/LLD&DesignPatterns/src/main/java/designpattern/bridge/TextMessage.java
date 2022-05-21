package designpattern.bridge;

public class TextMessage extends Notification {

  public TextMessage(NotificationSender notificationSender) {
    super(notificationSender);
    // TODO Auto-generated constructor stub
  }

  @Override
  public void sendMessage() {
    notificationSender.sendNotification();

  }

}

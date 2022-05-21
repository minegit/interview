package designpattern;

import designpattern.bridge.Email;
import designpattern.bridge.QRCode;
import designpattern.bridge.SMS;
import designpattern.bridge.TextMessage;

public class MainBridge {
  public static void main(String[] args) {
    TextMessage tm = new TextMessage(new Email());
    tm.sendMessage();
    tm = new TextMessage(new SMS());
    tm.sendMessage();

    QRCode qr = new QRCode(new Email());
    qr.sendMessage();
    qr = new QRCode(new SMS());
    qr.sendMessage();
  }
}

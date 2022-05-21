package designpattern.adapter;

public class PenDrivePlayerImpl implements PenDrivePlayer {

  public void playInPenDrive(String file, String format, String from) {
    System.out.println("Playing in " + from + " :" + file + "." + format);

  }

}

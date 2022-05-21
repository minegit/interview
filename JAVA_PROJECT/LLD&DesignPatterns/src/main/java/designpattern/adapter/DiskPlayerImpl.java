package designpattern.adapter;

public class DiskPlayerImpl implements DiskPlayer {

  public void play(String fileName, String format) {
    System.out.println("Playing " + fileName + "." + format + " on DISK");

  }


}

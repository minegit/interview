package designpattern;

import designpattern.adapter.DiskPlayer;
import designpattern.adapter.MediaPlayerImpl;

public class CheckAdapter {
  public static void main(String[] args) {
    DiskPlayer dp = new MediaPlayerImpl();
    dp.play("mySng", "avi");
    dp.play("mysing1", "mp3");
  }
}

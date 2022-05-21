package designpattern.adapter;

public class MediaPlayerAdapter implements DiskPlayer {
  private PenDrivePlayer penDrivePlayer;

  public MediaPlayerAdapter() {
    penDrivePlayer = new PenDrivePlayerImpl();
  }

  public void play(String fileName, String format) {
    penDrivePlayer.playInPenDrive(fileName, format, "PEN DRIVE");

  }

}

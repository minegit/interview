package designpattern.adapter;

public class MediaPlayerImpl implements DiskPlayer {

  MediaPlayerAdapter mediaPlayerAdapter;
  DiskPlayer diskPlayer;
  public void play(String fileName, String format) {
   if(format.equals("avi")) {
     mediaPlayerAdapter = new MediaPlayerAdapter();
     mediaPlayerAdapter.play(fileName, format);
   }else {
     diskPlayer = new DiskPlayerImpl();
     diskPlayer.play(fileName, format);
   }

  }

}

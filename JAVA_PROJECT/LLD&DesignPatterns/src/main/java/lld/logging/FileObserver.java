package lld.logging;

public class FileObserver implements LogObserver {

  public void log(String message) {
    System.out.println("IN FILE : "+message);

  }

}

package lld.logging.observer;

public class ConsoleObserver implements LogObserver {

  public void log(String message) {
   System.out.println("CONSOLE : "+message);

  }

}

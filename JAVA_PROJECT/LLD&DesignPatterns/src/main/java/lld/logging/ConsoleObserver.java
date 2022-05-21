package lld.logging;

public class ConsoleObserver implements LogObserver {

  public void log(String message) {
   System.out.println("CONSOLE : "+message);

  }

}

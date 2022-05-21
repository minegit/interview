package lld.logging;

public class DebugLogger extends AbstractCustomLogger {


  public DebugLogger(int level) {
    this.level = level;
  }

  @Override
  protected void display(String message,LogSubject logSubject) {
    logSubject.notifyAll(level, "DEBUG:" + message);

  }

}

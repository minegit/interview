package lld.logging;

public class InfoLogger extends AbstractCustomLogger {


  public InfoLogger(int level) {
    this.level = level;
  }

  @Override
  protected void display(String message, LogSubject logSubject) {
    logSubject.notifyAll(level, "INFO : " + message);
  }

}

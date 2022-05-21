package lld.logging;

public class ErrorLogger extends AbstractCustomLogger {

  public ErrorLogger(int level) {
    this.level = level;
  }
  @Override
  protected void display(String message , LogSubject logSubject) {
    logSubject.notifyAll(level , "ERROR:"+message);

  }

}

package lld.logging;

public abstract class AbstractCustomLogger {
  int level;
  AbstractCustomLogger nextLogger;

  public void setNextLogger(AbstractCustomLogger nextLogger) {
    this.nextLogger = nextLogger;
  }

  protected abstract void display(String message, LogSubject logSubject);

  void logMessage(int level, String message, LogSubject logSubject) {
    if (this.level == level) {
      display(message, logSubject);
    }
    if (nextLogger != null) {
      nextLogger.logMessage(level, message, logSubject);
    }
  }
}

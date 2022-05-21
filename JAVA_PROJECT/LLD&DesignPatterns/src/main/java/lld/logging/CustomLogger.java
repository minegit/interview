package lld.logging;

import java.io.Serializable;

public class CustomLogger implements Serializable, Cloneable {
  /**
   * 
   */
  private static final long serialVersionUID = 4408814952585411552L;
  private volatile static CustomLogger customLogger;
  private volatile static AbstractCustomLogger chainOfLogger;
  private volatile static LogSubject logSubject;

  private CustomLogger() {
    if (customLogger != null) {
      throw new IllegalStateException("Object already created");
    }
  }

  public static CustomLogger getInstance() {
    if (customLogger == null) {
      synchronized (CustomLogger.class) {
        if (customLogger == null) {
          customLogger = new CustomLogger();
          chainOfLogger = CustomLogManager.buildChainOfLogger();
          logSubject  = CustomLogManager.buildLogSubject();
        }
      }
    }
    return customLogger;
  }
  
  private void createLog(int level, String message) {
    chainOfLogger.logMessage(level, message, logSubject);
  }
  
  public void info(String message) {
    createLog(1, message);
  }
  
  public void debug(String message) {
    createLog(2, message);
  }
  
  public void error(String message) {
    createLog(3, message);
  }
}

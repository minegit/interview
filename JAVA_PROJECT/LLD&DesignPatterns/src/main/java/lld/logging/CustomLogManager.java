package lld.logging;

public class CustomLogManager {
  protected static AbstractCustomLogger buildChainOfLogger() {
    AbstractCustomLogger infoLogger = new InfoLogger(1);
    AbstractCustomLogger debugLogger = new DebugLogger(2);
    AbstractCustomLogger errorLogger = new ErrorLogger(3);

    infoLogger.setNextLogger(debugLogger);
    debugLogger.setNextLogger(errorLogger);
    return infoLogger;
  }
  
  protected static LogSubject buildLogSubject() {
    ConsoleObserver consoleObserver = new ConsoleObserver();
    FileObserver fileObserver = new FileObserver();
    LogSubject  logSubject = new LogSubject();
    logSubject.addObserver(1, consoleObserver);
    logSubject.addObserver(2, consoleObserver);
    logSubject.addObserver(3, consoleObserver);
    logSubject.addObserver(3, fileObserver);
    
    return logSubject;
  }
}

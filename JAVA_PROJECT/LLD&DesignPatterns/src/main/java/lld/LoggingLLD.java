package lld;

import java.util.logging.Logger;
import lld.logging.CustomLogger;

public class LoggingLLD {
  public static void main(String[] args) {
    CustomLogger logger  = CustomLogger.getInstance();
    logger.info("IN INFO...");
    logger.debug("IN DEBUG...");
    logger.error("IN  ERROR...");
//    System.out.println("---------------------------");
//    Logger log = Logger.getLogger(Some.class.getName());
//    log.info("ACTUAL INFO...");
//    log.fine("ACTUAL fine");
//    log.finer("Actual finer");
  }
}
 
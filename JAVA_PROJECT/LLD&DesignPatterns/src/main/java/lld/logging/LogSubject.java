package lld.logging;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LogSubject {
  Map<Integer, List<LogObserver>> logObservers = new HashMap<Integer, List<LogObserver>>();

  void addObserver(int level, LogObserver logObserver) {
    List<LogObserver> listLogObserver =
        logObservers.getOrDefault(level, new ArrayList<LogObserver>());
    listLogObserver.add(logObserver);
    logObservers.put(level, listLogObserver);
  }
  
  void notifyAll(int level, String message) {
    List<LogObserver> listLogObserver = logObservers.getOrDefault(level, new ArrayList<LogObserver>());
    for(LogObserver logObserver : listLogObserver) {
      logObserver.log(message);
    }
  }
}

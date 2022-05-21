package tutorials.concurrency.WaitNotify;

import java.util.ArrayList;
import java.util.List;

public class CheckWaitNotify {
  public static void main(String[] args) throws InterruptedException {
    List<Integer> taskQ = new ArrayList<Integer>();
    int maxCapacity = 10;
    Thread producerThread = new Thread(new Producer(taskQ, maxCapacity), "PRODUCER");
    Thread consumerThread = new Thread(new Consumer(taskQ), "CONSUMER");
    producerThread.start();
    consumerThread.start();
  }
}

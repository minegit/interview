package tutorials.concurrency.WaitNotify;

import java.util.List;

public class Producer implements Runnable {
  private final List<Integer> taskQ;
  private final int maxCapacity;

  public Producer(List<Integer> taskQ, int maxCapacity) {
    this.maxCapacity = maxCapacity;
    this.taskQ = taskQ;
  }

  public void run() {
    int counter = 0;
    while (true) {
      try {
        produce(counter++);
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
    }
  }

  private void produce(int counter) throws InterruptedException {
    synchronized (taskQ) {
      while (taskQ.size() == maxCapacity) {
        System.out.println("Q is full " + Thread.currentThread().getName() + " with "
            + Thread.currentThread().getPriority() + " is waiting ..as size is " + taskQ.size());
        taskQ.wait();
      }
      Thread.sleep(1000);
      taskQ.add(counter);
      System.out.println("Produced with priority : " + Thread.currentThread().getPriority()
          + " value : " + counter);
      taskQ.notifyAll();
    }
  }
}

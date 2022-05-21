package tutorials.concurrency.WaitNotify;

import java.util.List;

public class Consumer implements Runnable {
  private final List<Integer> taskQ;

  public Consumer(List<Integer> sharedQ) {
    this.taskQ = sharedQ;
  }

  private void consume() throws InterruptedException {
    synchronized (taskQ) {
      while (taskQ.isEmpty()) {
        System.out.println("Q is empty " + Thread.currentThread().getName() + " with "
            + Thread.currentThread().getPriority() + " waiting as q is empty");
        taskQ.wait();
      }
      Thread.sleep(100);
      int poppedVal = taskQ.remove(0);
      System.out.println("Consumed with priority : " + Thread.currentThread().getPriority()
          + " value : " + +poppedVal);
      taskQ.notifyAll();
    }
  }

  public void run() {
    while (true) {
      try {
        consume();
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
    }
  }

}

package tutorials.concurrency.SemaphoreAndLocks;

import java.util.Date;
import java.util.concurrent.Semaphore;

public class PrinterQueueSemaphoreImpl implements PrinterQueue{
  private final Semaphore semaphore;

  public PrinterQueueSemaphoreImpl() {
    this.semaphore = new Semaphore(1);
  }

  public PrinterQueueSemaphoreImpl(int n) {
    this.semaphore = new Semaphore(n);
  }

  public void printJob(Object doc) {
    try {
      semaphore.acquire();
      Long duration = (long) (Math.random() * 10000);
      System.out.println(Thread.currentThread().getName() + ": PrintQueue: Printing a Job during "
          + (duration / 1000) + " seconds :: Time - " + new Date());
      Thread.sleep(duration);
    } catch (InterruptedException e) {
      e.printStackTrace();
    } finally {
      System.out.printf("%s: The document has been printed\n", Thread.currentThread().getName());
      semaphore.release();
    }
  }
}

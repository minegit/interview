package tutorials.concurrency.SemaphoreAndLocks;

import java.util.Date;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class PrinterQueueLockImpl implements PrinterQueue {
  private final Lock reentrantLock = new ReentrantLock();
  
  @Override
  public void printJob(Object object) {
    reentrantLock.lock();
    try {
      Long duration  = (long)(Math.random()*10000);
      System.out.println(Thread.currentThread().getName() + ": PrintQueue: Printing a Job during "
          + (duration / 1000) + " seconds :: Time - " + new Date());
      Thread.sleep(duration);
    } catch (InterruptedException e) {
      e.printStackTrace();
    }finally {
      System.out.printf("%s: The document has been printed\n", Thread.currentThread().getName());
      reentrantLock.unlock();
    }
    
  }

}

package tutorials.concurrency.SemaphoreAndLocks;

import java.util.Arrays;
import java.util.Date;
import java.util.concurrent.Semaphore;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class MultiplePrinterQueue implements PrinterQueue {
  private final Semaphore semaphore;
  private final Lock reentrantLock;
  private boolean freePrinters[];

  public MultiplePrinterQueue(int n) {
    this.semaphore = new Semaphore(n);
    this.reentrantLock = new ReentrantLock();
    freePrinters = new boolean[n];
    Arrays.fill(freePrinters, true);

  }

  @Override
  public void printJob(Object object) {
    int freePrinter = -1;
    try {
      semaphore.acquire();
      freePrinter = getFreePrinter();
      Long duration = (long) (Math.random() * 10000);
      System.out.println(Thread.currentThread().getName() + ": Printer " + freePrinter
          + " : Printing a Job during " + (duration / 1000) + " seconds :: Time - " + new Date());
      Thread.sleep(duration);
    } catch (InterruptedException e) {
      e.printStackTrace();
    } finally {
      System.out.printf("%s: The document has been printed\n", Thread.currentThread().getName());
      releasePrinter(freePrinter);
      semaphore.release();
    }
  }

  private void releasePrinter(int freePrinter) {
    reentrantLock.lock();
    freePrinters[freePrinter] = true;
    reentrantLock.unlock();
  }

  private int getFreePrinter() {
    int foundPrinter = -1;
    try {
      reentrantLock.lock();
      for (int i = 0; i < freePrinters.length; i++) {
        if (freePrinters[i]) {
          foundPrinter = i;
          freePrinters[i] = false;
          break;
        }
      }

    } catch (Exception e) {
      e.printStackTrace();
    } finally {
      reentrantLock.unlock();
    }

    return foundPrinter;
  }
}

package tutorials.concurrency.SemaphoreAndLocks;

public class PrintingJob implements Runnable {
  private PrinterQueue printerQueue;

  public PrintingJob(PrinterQueue pq) {
    printerQueue = pq;
  }

  @Override
  public void run() {
    System.out.printf("%s: Going to print a document\n", Thread.currentThread().getName());
    printerQueue.printJob(new Object());
  }

}

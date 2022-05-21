package tutorials.concurrency.SemaphoreAndLocks;

public class CheckSemaphoreAndLock {
  public static void main(String[] args) {
//    showSemaphoreImpl();
//    showLockImpl();
    showMultiplePrinterImpl();
  }

  private static void showSemaphoreImpl() {
    PrinterQueue printerQueue = new PrinterQueueSemaphoreImpl(3); // This show a printer can print only 3 pages at times.
    extracted(printerQueue);
  }

  private static void extracted(PrinterQueue printerQueue) {
    Thread thread[] = new Thread[10];
    for (int x = 0; x < 10; x++) {
      thread[x] = new Thread(new PrintingJob(printerQueue), "Thread-" + x);
    }
    for (int y = 0; y < 10; y++) {
      thread[y].start();
    }
  }
  private static void  showLockImpl() {
    PrinterQueue printerQueue = new PrinterQueueLockImpl();
    extracted(printerQueue);
  }
  private static void showMultiplePrinterImpl() {
    PrinterQueue printerQueue = new MultiplePrinterQueue(5);
    extracted(printerQueue);
  }
}

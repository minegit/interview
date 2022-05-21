package tutorials.concurrency.ThreadLocal;

import java.util.Date;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;

public class DemoTask implements Runnable {
  private static final AtomicInteger nextId = new AtomicInteger(0);
  private static final ThreadLocal<Integer> threadId = new ThreadLocal<Integer>() {
    @Override
    protected Integer initialValue() {
      return nextId.getAndIncrement();
    }
  };

  private static final ThreadLocal<Date> startDate = new ThreadLocal<Date>() {
    @Override
    protected Date initialValue() {
      return new Date();
    }
  };

  public int getThreadId() {
    return threadId.get();
  }

  @Override
  public void run() {
    System.out.printf("Starting Thread: %s : %s\n", getThreadId(), startDate.get());
    try {
      TimeUnit.SECONDS.sleep((int) Math.rint(Math.random() * 10));
    } catch (InterruptedException e) {
      e.printStackTrace();
    }
    System.out.printf("Thread Finished: %s : %s\n", getThreadId(), startDate.get());
  }

  public static void main(String[] args) throws InterruptedException {
    Thread d1= new Thread(new DemoTask(), "t1");
    Thread d2= new Thread(new DemoTask(), "t2");
    Thread d3= new Thread(new DemoTask(), "t3");
    d1.start();
    d2.start();
    d3.start();
    d1.join();
    d2.join();
    d3.join();
  }
}

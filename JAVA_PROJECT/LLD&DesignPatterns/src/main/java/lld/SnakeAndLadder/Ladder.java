package lld.SnakeAndLadder;

public class Ladder {
  private int head;
  private int tail;

  public Ladder(int head, int tail) {
    if (head >= tail) {
      System.out.println("HEAD CANNOT BE MORE THAN TAIL");
      return;
    }
    this.head = head;
    this.tail = tail;
  }

  public int getHead() {
    return head;
  }

  public void setHead(int head) {
    this.head = head;
  }

  public int getTail() {
    return tail;
  }

  public void setTail(int tail) {
    this.tail = tail;
  }


}

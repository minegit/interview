package lld.SnakeAndLadder;

public class Snake {
  private int head;
  private int tail;

  public Snake(int head, int tail) {
    if (head <= tail) {
      System.out.println("HEAD CANNOT BE LESS THAN TAIL");
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

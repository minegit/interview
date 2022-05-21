package lld.SnakeAndLadder;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;

public class Board {
  private int startPoint;
  private int endPoint;
  private Map<Integer, Integer> snakes;
  private Map<Integer, Integer> ladders;

  public Board(int startPoint, int endPoint) {
    this.startPoint = startPoint;
    this.endPoint = endPoint;
    this.snakes = new HashMap<Integer, Integer>();
    this.ladders = new HashMap<Integer, Integer>();
  }


  public int getStartPoint() {
    return startPoint;
  }


  public void setStartPoint(int startPoint) {
    this.startPoint = startPoint;
  }


  public int getEndPoint() {
    return endPoint;
  }


  public void setEndPoint(int endPoint) {
    this.endPoint = endPoint;
  }


  public Map<Integer, Integer> getSnakes() {
    return snakes;
  }


  public void setSnakes(Map<Integer, Integer> snakes) {
    this.snakes = snakes;
  }


  public Map<Integer, Integer> getLadders() {
    return ladders;
  }


  public void setLadders(Map<Integer, Integer> ladders) {
    this.ladders = ladders;
  }


  private boolean canSnakeBeAdded(Snake snake) {
    if (snake.getHead() > this.startPoint + 1 && snake.getHead() < this.endPoint
        && snake.getTail() >= this.startPoint && snake.getTail() < this.endPoint) {
      if (this.snakes.containsKey(snake.getHead())) {
        return false;
      }
      if (this.snakes.containsValue(snake.getHead())) {
        return false;
      }
      if(this.ladders.containsKey(snake.getHead()) || this.ladders.containsValue(snake.getHead())) {
        return false;
      }
    } else {
      return false;
    }
    return true;
  }

  private boolean canLadderBeAdded(Ladder ladder) {
    if (ladder.getHead() > this.startPoint + 1 && ladder.getHead() < this.endPoint
        && ladder.getTail() >= this.startPoint && ladder.getTail() < this.endPoint) {
      if (this.ladders.containsKey(ladder.getHead())) {
        return false;
      }
      if (this.ladders.containsValue(ladder.getHead())) {
        return false;
      }
      if(this.snakes.containsKey(ladder.getHead()) || this.snakes.containsKey(ladder.getTail())) {
        return false;
      }
    } else {
      return false;
    }
    return true;
  }

  public boolean addSnake(Snake snake) {
    if (this.canSnakeBeAdded(snake)) {
      this.snakes.put(snake.getHead(), snake.getTail());
      return true;
    }
    return false;
  }

  public boolean addLadder(Ladder ladder) {
    if (this.canLadderBeAdded(ladder)) {
      this.ladders.put(ladder.getHead(), ladder.getTail());
      return true;
    }
    return false;
  }

  public Board generateSnake(int count) {
    for (int x = 0; x < count;) {
      Random random = new Random();
      int snakehead = (random.nextInt((this.getEndPoint() - 1 - this.getStartPoint() + 50) + 1)
          + this.getStartPoint() + 50) % (this.getEndPoint());
      int snaketail =
          (random.nextInt((snakehead - this.getStartPoint()) + 1) + this.getStartPoint())
              % (snakehead);
      if (this.addSnake(new Snake(snakehead, snaketail))) {
        x++;
      }
    }
    return this;
  }

  public Board generateLadder(int count) {
    for (int x = 0; x < count;) {
      Random random = new Random();
      int ladderTail = (random.nextInt((this.getEndPoint() - 1 - this.getStartPoint() + 50) + 1)
          + this.getStartPoint() + 50) % (this.getEndPoint());
      int ladderHead =
          (random.nextInt((ladderTail - this.getStartPoint()) + 1) + this.getStartPoint())
              % (ladderTail);
      if (this.addLadder(new Ladder(ladderHead, ladderTail))) {
        x++;
      }
    }
    return this;
  }
}

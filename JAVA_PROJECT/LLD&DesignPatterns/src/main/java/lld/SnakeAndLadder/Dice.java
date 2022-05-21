package lld.SnakeAndLadder;

import java.util.Random;

public class Dice {
  private int numberOfDice;
  private int minNumber;
  private int maxNumber;

  public Dice(int numberOfDice) {
    super();
    this.numberOfDice = numberOfDice;
    this.setDiceLimits();
  }

  public Dice() {
    super();
    this.numberOfDice = 1;
    this.setDiceLimits();
  }

  private Dice setDiceLimits() {
    this.minNumber = this.numberOfDice;
    this.maxNumber = this.numberOfDice * 6;
    return this;
  }

  public int roll() {
    Random random = new Random();
    int randomInt = (random.nextInt((this.maxNumber - this.minNumber) + 1) + this.minNumber) % (this.maxNumber+1);
    return randomInt;
  }

}

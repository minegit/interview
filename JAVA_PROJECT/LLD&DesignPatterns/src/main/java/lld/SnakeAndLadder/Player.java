package lld.SnakeAndLadder;

import java.util.HashMap;
import java.util.Map;

public class Player {
  int numberOfPlayer;
  Map<Integer, Integer> playerPos;

  public Player(int numberOfPlayer) {
    this.numberOfPlayer = numberOfPlayer;
    playerPos = new HashMap<Integer, Integer>();
    for (int i = 1; i <= numberOfPlayer; i++) {
      playerPos.put(i, 1);
    }
  }

  public int getNumberOfPlayer() {
    return numberOfPlayer;
  }

  public void setNumberOfPlayer(int numberOfPlayer) {
    this.numberOfPlayer = numberOfPlayer;
  }

  public Map<Integer, Integer> getPlayerPos() {
    return playerPos;
  }

  public void setPlayerPos(Map<Integer, Integer> playerPos) {
    this.playerPos = playerPos;
  }


}

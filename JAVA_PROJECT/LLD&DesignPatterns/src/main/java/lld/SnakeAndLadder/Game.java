package lld.SnakeAndLadder;

import java.util.ArrayList;
import java.util.List;
import java.util.Map.Entry;

public class Game {
  private Board board;
  private Dice dice;
  private Player player;

  public Board getBoard() {
    return board;
  }

  public void setBoard(Board board) {
    this.board = board;
  }

  public Dice getDice() {
    return dice;
  }

  public void setDice(Dice dice) {
    this.dice = dice;
  }

  public Player getPlayer() {
    return player;
  }

  public void setPlayer(Player player) {
    this.player = player;
  }

  private void initBoard(int startPoint, int endPoint, int numberOfPlayer, int numberOfDice,
      int numberOfLadder, int numberOfSnakes) {
    Board board = new Board(startPoint, endPoint);
    board = board.generateLadder(numberOfLadder).generateSnake(numberOfSnakes);
    this.setBoard(board);
    this.initDice(numberOfDice);
    this.initPlayer(numberOfPlayer);
  }

  private void initDice(int numberOfDice) {
    Dice dice = new Dice(numberOfDice);
    this.dice = dice;
  }

  private void initPlayer(int numberOfPlayer) {
    Player player = new Player(numberOfPlayer);
    this.setPlayer(player);
  }

  public int throwDice(Dice dice, int count) {
    int diceVal = 0;
    for (int x = 1; x < count; x++) {
      int currVal = dice.roll();
      if (currVal != 6) {
        return diceVal + currVal;
      } else {
        diceVal += currVal;
      }
    }
    int currVal = dice.roll();
    if (currVal == 6) {
      return throwDice(dice, count);
    }
    return diceVal + currVal;

  }

  public static void main(String[] args) {
    int numberOfPlayer = 50;
    int numberOfDice = 1;
    Game game = new Game();
    game.initBoard(1, 100, numberOfPlayer, numberOfDice, 10, 10);
    List<Integer> winnerPlayer = new ArrayList<Integer>();


    while (true) {
      if (winnerPlayer.size() == numberOfPlayer - 1) {
        System.out.println("Game COMPLETED");
        for (int x = 0; x < winnerPlayer.size(); x++) {
          System.out.println("Pos : " + (x + 1) + " Player : " + winnerPlayer.get(x));
        }
        for(Entry<Integer, Integer> snake : game.getBoard().getSnakes().entrySet()) {
          System.out.println("SNAKE: "+ snake.getKey() +" ---> "+ snake.getValue());
        }
        for(Entry<Integer, Integer> snake : game.getBoard().getLadders().entrySet()) {
          System.out.println("Ladder: "+ snake.getKey() +" ---> "+ snake.getValue());
        }
        return;
      }
      for (int playerNo = 1; playerNo <= numberOfPlayer; playerNo++) {
        if (winnerPlayer.contains(playerNo)) {
          continue;
        }
        int currentPos = game.getPlayer().getPlayerPos().get(playerNo);
        int diceValue = game.throwDice(game.getDice(), 3);
        if ((currentPos + diceValue) > game.getBoard().getEndPoint()) {
          System.out.println("PLAYER : " + playerNo + " CURENTLY AT : "+currentPos+"INVALID MOVE- " + diceValue);
          continue;
        }
        if ((currentPos + diceValue) == game.getBoard().getEndPoint()) {
          System.out.println("PLAYER : " + playerNo + " CURENTLY AT : "+currentPos+ " WINNER- " + diceValue);
          winnerPlayer.add(playerNo);
          continue;
        }
        int nextPos = currentPos + diceValue;
        int upLadderPos = game.getBoard().getLadders().getOrDefault(nextPos, nextPos);
        if (upLadderPos != nextPos) {
          System.out.println("Player : " + playerNo + "  AT : "+currentPos+ " GOT : "+diceValue+" CLIMBING LADDER WENT TO : " + upLadderPos);
          game.getPlayer().getPlayerPos().put(playerNo, upLadderPos);
          continue;
        }
        int snakeBittenPos = game.getBoard().getSnakes().getOrDefault(nextPos, nextPos);
        if (snakeBittenPos != nextPos) {
          System.out.println("Player : " + playerNo + "  AT : "+currentPos+ " GOT : "+diceValue+ " Biting Snake  WENT TO : " + snakeBittenPos);
          game.getPlayer().getPlayerPos().put(playerNo, snakeBittenPos);
          continue;
        }
        game.getPlayer().getPlayerPos().put(playerNo, nextPos);
        System.out.println("Player : " + playerNo + "  AT : "+currentPos+ " GOT : " + diceValue + " Move to " + nextPos);

      }
    }
    
  }
}

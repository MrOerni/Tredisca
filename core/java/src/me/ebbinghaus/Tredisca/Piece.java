package me.ebbinghaus.Tredisca;

public abstract class Piece {
    boolean unmoved;
    boolean side; //true <=> white
    char icon;

    public abstract void move();

    public char getIcon() {
        return icon;
    }
}
/*
Nabil Arbouz
Algorithms Spring 2020
Stack Linked List Exercise
 */

class StackList {
    public static void main(String[] args) {
        System.out.println("Pushing values onto the stack");

        StackList testStack = new StackList(0);
        testStack.printStack();

        for(int i = 1; i <= 10; i++) {
            testStack.push(i);
            testStack.printStack();
        }

        System.out.println("-------------------------------");
        System.out.println("Popping values from the stack");
        for(int i = 0; i < 11; i++) {
            testStack.pop();
            System.out.print("The new stack is: ");
            testStack.printStack();
        }

        //Edge Cases
//        StackList edgeCaseStack = new StackList();
//        edgeCaseStack.pop(); //Test the pop of an empty stack
//
//        edgeCaseStack.push(1); //Push an item onto the empty stack
//        System.out.println("Pushing a node onto the top of the stack was successful.");
//
//        edgeCaseStack.push(-1); //Push a negative number onto the stack
//        edgeCaseStack.push("hello world"); //Pushing a string onto the stack will produce an error

    }

    Node head;
    Node top;
    int numOfNodes;

//    public StackList() {
//        this.head = null;
//        this.top = null;
//    }

    public StackList(int value) {
        Node newNode = new Node(value, null);
        numOfNodes += 1;
        this.head = newNode;
        this.top = newNode;
    }

    public void push(int val) {
        Node newNode = new Node(val, null);
        if (this.isNotEmpty()) {
            this.top.next = newNode;
        } else {
            this.head = newNode;
        }
        this.top = newNode;
        this.numOfNodes++;
    }

    public void pop() {
        if (this.isNotEmpty()) {
            if (numOfNodes > 1) {
                Node previousNode = null;
                Node currentNode = this.head;

                while (currentNode.getNext() != null) {
                    previousNode = currentNode;
                    currentNode = currentNode.getNext();
                }
                System.out.println("Popping " + currentNode.value + " from the stack");
                assert previousNode != null;
                previousNode.setNext(null);
            } else {
                System.out.println("Popping " + this.head.value + " from the stack");

                this.head = null;
                this.top = null;
            }
            numOfNodes--;
        } else {
            System.out.println("The stack is empty. Pop operation not available.");
        }
    }

    public void printStack() {
        Node currentNode = head;
        if (this.numOfNodes > 0) {
            while (currentNode != null) {
                System.out.print(currentNode.getValue() + " ");
                currentNode = currentNode.getNext();
            }
            System.out.print('\n');
        } else {
            System.out.println("The stack is empty");
        }
    }

    public boolean isNotEmpty() {
        return this.top != null;
    }

    private static class Node {
        private int value;
        private Node next;

        public Node(int value, Node nextNode) {
            this.value = value;
            this.next = nextNode;
        }

        public void setNext(Node newNext) {
            this.next = newNext;
        }

//        public void setValue(int newVal) {
//            this.value = newVal;
//        }

        public int getValue() {
            return this.value;
        }

        public Node getNext() {
            return this.next;
        }

    }
}
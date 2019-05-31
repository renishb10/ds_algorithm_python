class Stack {
  constructor() {
    this.items = [];
  }

  push(data) {
    if (data) {
      this.items.push(data);
    }
  }

  pop() {
    if (this.items.length <= 0) {
      throw new Error("Stack underflow");
    }
    const poppedItem = this.items.pop();
    console.log('pop: ', poppedItem);
    return poppedItem;
  }

  peek() {
    if (this.items.length <= 0) {
      throw new Error("Stack underflow");
    }
    console.log('peek: ', this.items[this.items.length - 1]);
  }

  size() {
    console.log('size: ',this.items.length);
  }

  display() {
    if (this.items.length <= 0) {
      throw new Error("Stack underflow");
    }

    const data = this.items.slice(0);
    data.reverse();
    data.forEach(item => {
      console.log(item);
    });
  }
}

const newStack = new Stack();
newStack.push(1);
newStack.push(2);
newStack.push(3);
newStack.push(4);
newStack.push(5);

newStack.display();

newStack.pop();

newStack.size();

newStack.display();
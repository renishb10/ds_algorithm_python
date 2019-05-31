class Queue {
  constructor() {
    this.items = [];
  }

  enqueue(item) {
    this.items.unshift(item);
  }

  dequeue() {
    if (this.items.length <= 0) {
      throw new Error("Queue Underflow");
    }
    const value = this.items.splice(0, 1);
    console.log('Dequeue',value)
    return value;
  }

  peek() {
    if (this.items.length <= 0) {
      throw new Error("Queue Underflow");
    }
    console.log('Peek',this.items[0]);
    return this.items[0];
  }

  size() {
    console.log('size',this.items.length);
    return this.items.length;
  }

  display() {
    if (this.items.length <= 0) {
      throw new Error("Queue Underflow");
    }

    this.items.forEach(item => {
      console.log(item);
    });
  }
}

const newQ = new Queue();
newQ.enqueue(1);
newQ.enqueue(2);
newQ.enqueue(3);
newQ.enqueue(4);
newQ.enqueue(5);

newQ.display();

newQ.dequeue();

newQ.size();

newQ.display();

class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class SList {
  constructor() {
    this.head = null;
    this.size = 0;
  }

  insert(data) {
    const newNode = new Node(data);

    // If list is empty
    if (this.head == null) {
      this.head = newNode;
    }
    else {
      // If list has some nodes already
      // Travel till end of the list
      let currentNode = this.head;
      while(currentNode.next) {
        currentNode = currentNode.next;
      }

      currentNode.next = newNode;
    }
  }

  insertAfter(data) {

  }

  remove(data) {
    if (!this.head) {
      console.log("List is Empty");
    }
    else {
      let currentNode = this.head;
      let prevNode = null;
      while(currentNode) {
        if (currentNode.data == data) {
          prevNode.next = currentNode.next;
          break;
        }

        prevNode = currentNode;
        currentNode = currentNode.next;
      }
    }
  }

  display() {
    if (this.head !== null) {
      let currentNode = this.head;
      while(currentNode) {
        console.log(currentNode.data);
        currentNode = currentNode.next;
      }
    }
    else {
      console.log("List is Empty");
    }
  }
}

const sList = new SList();
sList.insert(1);
sList.insert(2);
sList.insert(3);
sList.insert(4);

sList.display();
console.log('After Removing 3');
sList.remove(3);
sList.display();
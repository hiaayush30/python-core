# Object Types / Data Types
## the variables do not have any datatypes, the reference in the memory has a data type

- Number : 1234, 3.14, 3+4j, 0b101, Decimal(), Fraction()

- String : 'spam', "Bob's", b'a\x01c', u'sp\xc4m'

- List : [1,[2, 'three'], 4.5 ] , list(range(10))

- Tuple : (1,'spam', 4, 'U'), tuple('spam'), namedtuple

- Dictionary : {'food':'spam','taste':'yum'}, dict(hours=10)

- Set : set('abc'),{'a','b','c'}

- File : open('eggs.txt'), open(r'C:\ham.bin','wb')

- Boolean : True,False
- None : None
- Functions,modules,classes


- Advance : Decorators, Generators, Iterators, MetaProgramming

- In Python the garbage collection of numbers and strings are a little delayed

---
JavaScript's data types and their mutability!

Here's a quick rundown:

* **Primitive Data Types:** These are immutable, meaning their values cannot be changed directly after creation.

    * **String:** Represents textual data.
        ```javascript
        let message = "Hello";
        message = "World"; // `message` now holds a new string
        console.log(message); // Output: World
        ```
    * **Number:** Represents numeric values (integers and floating-point numbers).
        ```javascript
        let count = 10;
        count = count + 5; // `count` now holds a new number
        console.log(count); // Output: 15
        ```
    * **Boolean:** Represents logical values (`true` or `false`).
        ```javascript
        let isActive = true;
        isActive = false; // `isActive` now holds a new boolean
        console.log(isActive); // Output: false
        ```
    * **Undefined:** Represents a variable that has been declared but has not been assigned a value.
        ```javascript
        let notDefined;
        console.log(notDefined); // Output: undefined
        ```
    * **Null:** Represents the intentional absence of a value.
        ```javascript
        let emptyValue = null;
        console.log(emptyValue); // Output: null
        ```
    * **Symbol:** Represents a unique and immutable primitive value (introduced in ES6).
        ```javascript
        const sym1 = Symbol("description");
        const sym2 = Symbol("description");
        console.log(sym1 === sym2); // Output: false (symbols are unique)
        ```
    * **BigInt:** Represents integer values that are too large to be represented by the Number type (introduced in ES2020).
        ```javascript
        const largeNumber = 9007199254740991n;
        const anotherLarge = BigInt(9007199254740995);
        console.log(largeNumber + 1n); // Output: 9007199254740992n
        ```

* **Reference Data Types:** These are mutable, meaning their internal state can be changed after creation. Variables of these types hold references to the actual object in memory.

    * **Object:** A collection of key-value pairs.
        ```javascript
        let person = { name: "Alice", age: 30 };
        person.age = 31; // The object is modified
        console.log(person); // Output: { name: 'Alice', age: 31 }
        ```
    * **Array:** An ordered list of items.
        ```javascript
        let numbers = [1, 2, 3];
        numbers.push(4); // The array is modified
        console.log(numbers); // Output: [ 1, 2, 3, 4 ]
        ```
    * **Function:** A block of reusable code. While the function itself isn't typically thought of as being "mutated" in the same way as objects or arrays, its internal state (if it has any via closures or properties) can change.
        ```javascript
        function greet() {
          console.log("Hello!");
        }
        greet.message = "A property of the function";
        console.log(greet.message); // Output: A property of the function
        ```

In essence, when you modify a primitive, you're creating a new value. When you modify a reference type, you're changing the underlying data structure that the variable points to.

Let me know if you'd like a deeper dive into any of these!
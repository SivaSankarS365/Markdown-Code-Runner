

```markdown
# Test Markdown File

This is a test Markdown file to check the functionality of the script.
```

## C++ Code Example

<codeStart class="" />

```cpp
#include <iostream>

using namespace std;

int main() {
    cout << "Hello, World!" << endl;   
    return 0;
}
```            

                           
<codeEnd/>

## Same code but it will be skipped. Using skip tag.

<codeStart class="skip"/>

```cpp
#include <iostream>

using namespace std;

int main() {
    cout << "Hello, World!" << endl;   
    return 0;
}
```

<codeEnd/>

## C++ Code Example with Input from stdio (terminal), nocache to prevent caching

<codeStart class="nocache" />

```cpp
#include <iostream>

int main() {
    std::ios::sync_with_stdio(false); // Disable synchronization with C standard streams
    int num;
    std::cout << "Enter a number: ";
    std::cin >> num;
    std::cout << "You entered: " << num << std::endl;
    return 0;
}
```            

                           
<codeEnd/>

## C Code Example with predefined Input

<codeStart class="nocache" />

```c
#include <stdio.h>

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    printf("You entered: %d\n", num);
    return 0;
}
```            

<span style="color: #007ACC; font-weight: bold;">[INPUT]:</span>
```input                   
1000
```

                           
<codeEnd/>

## Python Code Example with Output

<codeStart class="" />

```py
import math

def calculate_circle_area(radius):
    return math.pi * radius * radius

radius = 5
area = calculate_circle_area(radius)
print(f"Area of circle with radius {radius} is {area}")
```            

                           
<codeEnd/>

## Python Code Example with Error

<codeStart class="" />

```py
import math

def calculate_circle_area(radius):
    return math.pi * radius * radius

radius = "five"
area = calculate_circle_area(radius)
print(f"Area of circle with radius {radius} is {area}")
```            

                           
<codeEnd/>

## Code Block with Multiple Outputs

<codeStart class="timeit nocache" />

```py
import time

def calculate_time():
    start_time = time.time()
    time.sleep(0.001)
    end_time = time.time()
    return end_time - start_time

time_taken = calculate_time()
print(f"Time taken: {time_taken} seconds")

time_taken = calculate_time()
print(f"Time taken: {time_taken} seconds")
```            

                           
<codeEnd/>

Note that the `hash` attribute in the `<codeStart>` tag is used to identify the code block and can be used to cache the output. The `class` attribute can be used to specify additional options such as `skip` or `timeit`.
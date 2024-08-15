

```markdown
# Test Markdown File

This is a test Markdown file to check the functionality of the script.
```

## C++ Code Example

<codeStart class="" hash="6cc9e5a3127ee757562a99f78fabfbdd54f9423a2ac7159f044600f15432acf4"/>

```cpp
#include <iostream>

using namespace std;

int main() {
    cout << "Hello, World!" << endl;   
    return 0;
}
```            

<span style="color:  #28A745; font-weight: bold;">[OUTPUT]:</span> <span style="font-size: small; color: #6A737D;">Time taken (ms): 516.81299
</span>
```output                    
Hello, World!

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

## C Code Example with Input from stdio (terminal), nocache to prevent caching

<codeStart class="nocache" hash="79b1fea382db681b71643418ac85b86cf5cc03bd00fdd698cb48b0c9bda0a0de"/>

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

<span style="color:  #28A745; font-weight: bold;">[OUTPUT]:</span> <span style="font-size: small; color: #6A737D;">Time taken (ms): 1218.65625
</span>
```output                    
Enter a number: You entered: 222

```

                           
<codeEnd/>

## C Code Example with predefined Input

<codeStart class="nocache" hash="cd90e5223462808ef8982ced6bf1f3cb466c7863a21e947e040ba7eceabfdf0f"/>

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

<span style="color:  #28A745; font-weight: bold;">[OUTPUT]:</span> <span style="font-size: small; color: #6A737D;">Time taken (ms): 237.25317
</span>
```output                    
Enter a number: You entered: 1000

```

                           
<codeEnd/>

## Python Code Example with Output

<codeStart class="" hash="3db728f8540ab3d082591b30b82a434a5499658822c56496dd0684af69033d1d"/>

```py
import math

def calculate_circle_area(radius):
    return math.pi * radius * radius

radius = 5
area = calculate_circle_area(radius)
print(f"Area of circle with radius {radius} is {area}")
```            

<span style="color:  #28A745; font-weight: bold;">[OUTPUT]:</span> <span style="font-size: small; color: #6A737D;">Time taken (ms): 33.86768
</span>
```output                    
Area of circle with radius 5 is 78.53981633974483

```

                           
<codeEnd/>

## Python Code Example with Error

<codeStart class="" hash="de5c7e5bc4a71fdc7225f43f9c1801cb627ced59d4ab5101130cb7b0e42409f4"/>

```py
import math

def calculate_circle_area(radius):
    return math.pi * radius * radius

radius = "five"
area = calculate_circle_area(radius)
print(f"Area of circle with radius {radius} is {area}")
```            

<span style="color: #D73A49; font-weight: bold;">[OUTPUT]:</span> <span style="font-size: small; color: #6A737D;">Time taken (ms): 28.05078
</span>
```output                    
No Output
```

<span style="color: #D73A49; font-weight: bold;">[ERROR]:</span>
</span>
```error                    
Traceback (most recent call last):
  File "/tmp/mdcoderunner/temp.py", line 7, in <module>
    area = calculate_circle_area(radius)
  File "/tmp/mdcoderunner/temp.py", line 4, in calculate_circle_area
    return math.pi * radius * radius
TypeError: can't multiply sequence by non-int of type 'float'

```

                           
<codeEnd/>

## Code Block with Multiple Outputs

<codeStart class="timeit nocache" hash="8965f08a226d88ca9815756d0ff302e6e267c449fa13d28c6938e57decbe83d3"/>

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

<span style="color:  #28A745; font-weight: bold;">[OUTPUT]:</span> <span style="font-size: small; color: #6A737D;">Time taken (ms): 23.38164
</span>
```output                    
Time taken: 0.0012569427490234375 seconds
Time taken: 0.0012540817260742188 seconds

```

<span style="color:  #28A745; font-weight: bold;">[TIMEIT-RESULTS (ms)]:</span>
```timeit
mean: 23.38164 +/- 4.34826
std: 2.17413
max: 28.84619
min: 21.81396
with a total of 10 runs
```

                           
<codeEnd/>

Note that the `hash` attribute in the `<codeStart>` tag is used to identify the code block and can be used to cache the output. The `class` attribute can be used to specify additional options such as `skip` or `timeit`.
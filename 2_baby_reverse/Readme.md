# 题目名称

baby_reverse

# Category

reverse

# Difficulty(1-4)

 2

# key words

- 简单异或
- ida中函数列表的识别

# Description

so easy!

# wp

拖进ida，可以看到关键函数在一个函数列表中

运行程序，可以发现有三个step，关键在第三个

其实主要就是把输入与两个key进行异或，exp放在下面

```c
#include <stdio.h>
#include <string.h>
int main()
{
    unsigned char magic[] = {234, 221, 153, 210, 224, 133, 174, 211, 194, 158, 147, 145, 163, 250, 223, 210, 192, 200, 224, 139, 153, 141, 231, 214, 255, 142, 199, 207, 146, 202, 246, 249, };
    unsigned char flag[100] = {0};
    unsigned char key2[] = "Excalibur";
    unsigned char key1[] = "Avalon";
    for(int i=0; i<32; i++){
        flag[31 - i] = magic[i];
    }
    for(int i=0; i<32; i++){
        flag[i] = flag[i] ^ key2[i%strlen(key2)];
    }
    for(int i=0; i<32; i++){
        magic[31 - i] = flag[i];
    }
    for(int i=0; i<32; i++){
        magic[i] = (~magic[i]) ^ key1[i%strlen(key1)];
    }
    for( int i=0; i<32; i++){
        printf("%c", magic[i]);
    }
}
```


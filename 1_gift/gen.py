import hashlib
import time
import os
import uuid
for i in range(1, 51):
    binaryPath = "../gift_" + str(uuid.uuid4())[:8] + ".exe"
    flagPath = binaryPath + ".flag"
    # 生成flag
    timeStamp = str(time.time())
    timeMD5 = str(hashlib.md5(timeStamp.encode()).hexdigest())
    flag = 'mssctf{' + timeMD5 + '}'
    flagFile = open(flagPath, 'w+')
    flagFile.write(flag)
    flagFile.close()
    # 生成binary
    challFile = open('gift.c', 'r')
    challContent = challFile.read()
    challFile.close()
    challContent = challContent.replace('mssctf{please_set_a_flag}',flag)
    destFlie = open('dest.c', 'w')
    destFlie.write(challContent)
    destFlie.close()
    commandLine = 'gcc dest.c -o ' + binaryPath
    print("start compile " + str(i))
    print('commandline : ' + commandLine)
    os.system(commandLine)
    commandLine = "strip " + binaryPath
    print('commandline : ' + commandLine)
    os.system(commandLine)
    print("finish")
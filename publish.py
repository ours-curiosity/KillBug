import os

def push():

    checkCommand = "pod spec lint CTKillBug.podspec --allow-warnings"
    pushCommand = "pod trunk push CTKillBug.podspec --allow-warnings --allow-warnings"
    checkRet = os.system(checkCommand)
    if checkRet != 0:
        print("校验出错，请检查spec文件是否配置正确")
        exit - 1
    else:
        pushRet = os.system(pushCommand)
        if pushRet != 0:
            print("上传失败！")
            exit - 1
        else:
            print("上传完成！！")
    return


if __name__ == "__main__":
	push()

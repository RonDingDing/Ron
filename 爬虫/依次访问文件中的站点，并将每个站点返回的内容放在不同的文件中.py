filename = "url.txt"


import urllib.request
import chardet

def main():
        i = 0

        with open(filename, "r") as file:
                urls = file.read().splitlines()
        for each_url in urls:
                response = urllib.request.urlopen(each_url)
                html = response.read()


                encode = chardet.detect(html)["encoding"]
                if encode == "GB2312":
                        encode = "GBK"

                i +=1

                filefuckname = "url_%d.txt" % i

                with open(filefuckname, "w", encoding=encode) as each_file:
                        each_file.write(html.decode(encode, "ignore"))
                        
if __name__ == "__main__":
        main()

# Gitbook ＆ Github 使用


### 產生公私鑰
```
cd ~/.ssh
ssh-keygen -t rsa -C "nicecoolwinter@gmail.com" -f id_rsa_nicecoolwinter
不用輸入任何密碼按 enter 就好


$ ls id_rsa_nicecoolwinter*
id_rsa_nicecoolwinter
id_rsa_nicecoolwinter.pub
```

### `將 id_rsa_nicecoolwinter.pub 放到 github setting`

### 設定 ~/.ssh/config
```sh
Host github.com-nicecoolwinter  // Host 名稱可以自取
HostName github.com
User git
IdentityFile ~/.ssh/id_rsa_nicecoolwinter
```

#GitBook


###ssh://git@`Hostname`/`github account`/`RepositoryName`.git
```
git clone ssh://git@github.com-nicecoolwinter/nicecoolwinter/note.git
```

`Makfile`
```
init:
	@gitbook init

serve:
	@gitbook serve

build:
	@gitbook build

clean:
	rm -fr _book

github:
	@ghp-import _book -p -n

```

### 產生 html

```
make build
```

### 發布 到 GitHub Pages
```
make github
```

###  網站
```
http://nicecoolwinter.github.io/note/
```



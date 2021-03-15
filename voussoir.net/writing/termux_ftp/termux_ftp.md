How to run an SSH, SFTP server from Termux
==========================================

With [Syncthing](https://f-droid.org/en/packages/com.nutomic.syncthingandroid/) in one hand and [Termux](https://f-droid.org/en/packages/com.termux/) in the other, you can do almost all of your pc-phone file transfer wirelessly. Here's how to serve SSH and SFTP from Android.

## "Almost all"

I have an LG K10 running Android 7 with an SD card inserted. I find that Termux isn't able to write to the SD card. The GitHub issues say that you can write to [one directory](https://github.com/termux/termux-app/issues/20), but you can't get general access. You'll have to stick to writing to the internal storage.

## Initial setup

1. Download and install [Termux](https://f-droid.org/en/packages/com.termux/).

2. Run `termux-setup-storage`, grant it permission, then reboot Termux. You can type `exit` or pull down the notification and press the Exit button.

3. You will find a new folder `~/storage` which contains some symlinks to various directories on the phone. Personally, I prefer to remove this with `rm -rf ~/storage` and then `ln -s /storage/emulated/0 ~/internal`, but this is not required.

4. Run `pkg install openssh`.

5. You will probably also want `pkg install vim`.

## Password auth

At this point I am following the official Termux Wiki page on [Remote Access](https://wiki.termux.com/wiki/Remote_Access), but I'll simplify the presentation:

1. Run `cat /data/data/com.termux/files/usr/etc/ssh/sshd_config` to confirm that the contents match the default as seen on the wiki:
  
  ```
  PrintMotd yes
  PasswordAuthentication yes
  Subsystem sftp /data/data/com.termux/files/usr/libexec/sftp-server
  ```

2. Run `passwd` to pick a password. I'll be switching to key-based authentication in a minute so I'm just going to pick `1` as my password. Of course, this password doesn't apply to your whole phone, just the termux emulator.

3. Run `sshd` to start the server.

4. You can run `ifconfig` within Termux to find your phone's local IP address, or, depending on your home router, you might be able to assign the phone a hostname from the admin panel.

  ![](https://voussoir-net.s3-us-west-1.amazonaws.com/writing/termux_ftp/lan_ip.png)

5. Open an SSH client on your PC. I'll be using [Putty](https://www.putty.org/).

6. Enter the phone's hostname or IP address, and choose 8022 for the port, and start the session.

  ![](https://voussoir-net.s3-us-west-1.amazonaws.com/writing/termux_ftp/putty_session.png)

7. Putty may warn you that it has never seen the server's fingerprint before, which is expected and you can accept it.

  ![](https://voussoir-net.s3-us-west-1.amazonaws.com/writing/termux_ftp/unfamiliar_fingerprint.png)

8. In Putty, the server will prompt you for a username. You may type anything your want, or even leave it blank and just hit Enter. Then it will ask you for the password you chose earlier.

  ![](https://voussoir-net.s3-us-west-1.amazonaws.com/writing/termux_ftp/ssh_success.png)

9. Congratulations! Try running a command like `ls`.

10. Open an FTP client on your PC. I'll be using [WinSCP](https://winscp.net/eng/download.php).

11. Enter the phone's hostname/IP and port. When I typed 8022 into the port field, WinSCP automatically changed the protocol selection from SFTP to WebDAV, so change it back to SFTP. You may enter anything you want for the username, but if you leave it blank then WinSCP will prompt you during the login process, so maybe you'd like to make something up. Also enter your password, then log in.

  ![](https://voussoir-net.s3-us-west-1.amazonaws.com/writing/termux_ftp/winscp_session.png)

  ![](https://voussoir-net.s3-us-west-1.amazonaws.com/writing/termux_ftp/ftp_success.png)

12. Congratulations! Try uploading some files to the phone.

## Keyfile auth

I assume you won't be leaving your phone's server on very long, or giving it an internet-facing port, so you can leave it in password auth mode if you want. But this is a great chance to get some practice with SSH keyfiles anyway, so keep reading.

1. When you downloaded Putty, you should have also gotten `puttygen.exe`. Open that program.

2. Leave the key type as RSA and press the Generate button to make a public/private keypair. You can use the comment field to give it a memorable name.

  ![](https://voussoir-net.s3-us-west-1.amazonaws.com/writing/termux_ftp/puttygen.png)

3. You may give the keypair a password, but you'll have to type this password every time you log in with Putty/WinSCP, which you may not want to do. So you can leave it blank. In a 'real-life' SSH situation, you can use a passworded keyfile to double your security; someone would have to steal your keyfile and know your password to log into your servers.

4. Use the "Save public key" and "Save private key" buttons to write your keyfiles to disk. You can pick any kind of name and file extension you want. I use a name like `voussoir.ssh.public` and `voussoir.ssh.private`. Do not close puttygen yet.

5. We need to teach the server to trust the public key we've created. In Putty, use vim to create a file called `~/.ssh/authorized_keys`.

  ![](https://voussoir-net.s3-us-west-1.amazonaws.com/writing/termux_ftp/authorized_keys1.png)

6. In the puttygen UI, the text box at the top has the text that needs to go into this file. You'll notice that the format of this text is `<key type> <base64> <comment>` where the key type is `ssh-rsa`, the base64 is the content of the publickey file you saved, and the comment is what you wrote earlier. To paste into vim over putty you may need to press Shift+Insert.

7. Save and quit with Esc + `:wq`.

  ![](https://voussoir-net.s3-us-west-1.amazonaws.com/writing/termux_ftp/authorized_keys2.png)

8. Also modify the `sshd_config` file to disable password authentication. `vim /data/data/com.termux/files/usr/etc/ssh/sshd_config`

  ![](https://voussoir-net.s3-us-west-1.amazonaws.com/writing/termux_ftp/sshd_config.png)

9. Close Putty and WinSCP. Stop the server with `pkill sshd` and run it again with `sshd`.

10. Open Putty again, and enter the hostname and port.

11. On the left menu, choose Connection > Data and put something in the username box so you won't get prompted during login.

  ![](https://voussoir-net.s3-us-west-1.amazonaws.com/writing/termux_ftp/putty_data.png)

12. Then choose Connection > SSH > Auth and browse for your private keyfile.

  ![](https://voussoir-net.s3-us-west-1.amazonaws.com/writing/termux_ftp/putty_auth.png)

13. Before pressing the Open button, you may want to go back to the main Session screen and click the Save button to store the configuration. Then click Open.

14. Congratulations!

15. Open WinSCP again, and enter the hostname and port and select SFTP. Put something in the username box.

16. Click the Advanced button and select SSH > Authentication. Browse for your private keyfile.

  ![](https://voussoir-net.s3-us-west-1.amazonaws.com/writing/termux_ftp/winscp_auth.png)

17. You may want to save the session configuration. Then click Login.

18. Congratulations!

## Homescreen shortcut

Now we'll put a shortcut on the homescreen to launch the server in a single tap.

1. Download and install [Termux:Widget](https://f-droid.org/en/packages/com.termux.widget).

2. Using the shell or WinSCP, create the folder `~/.shortcuts` and create an `.sh` file inside there. I'll call it `sshd_widget.sh`.

3. Here is the content of my script file:

  ```
  sshd
  echo SSH server running.
  echo press Enter to terminate.
  read continue
  pkill sshd
  ```

4. On your phone's homescreen, create a new shortcut widget from the Termux:Widget section. It will show you the files inside `~/.shortcuts`.

  ![](https://voussoir-net.s3-us-west-1.amazonaws.com/writing/termux_ftp/widget.png)

5. Congratulations!

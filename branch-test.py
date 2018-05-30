1,cat 查看文件内容
1.1, cat /etc/yum.conf >a.txt
1.2, cat -n xxx.txt
[root@paris b]# cat -n b.txt 
     1	a
     2	b
     3	c
     4	d

2,cd 目录切换：
2.1，cd -     切换到上次的目录路径下
[root@paris a]# cd /opt/rh/
[root@paris rh]# cd -
/tmp/a
[root@paris a]# pwd
/tmp/a
2.2，cd ..    切换到上级目录下
[root@paris a]# pwd
/tmp/a
[root@paris a]# cd ..
[root@paris tmp]# pwd
/tmp
2.3，cd   = cd -  切换到当前用户的家目录下
[chen@paris ~]$ cd /tmp/a
[chen@paris a]$ cd -
/home/chen
[chen@paris ~]$ cd 
[chen@paris ~]$ pwd
/home/chen

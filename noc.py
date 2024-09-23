import compile 
print("ran")
file = open("built.asm", "r")

strf = file.read()
file.close()
file = open("nocvm/mem.txt", "w")

file.write(strf)
file.close()

from subprocess import Popen, PIPE

cmd = r'nocvm\a.exe'
p = Popen(cmd, stdin=PIPE, stdout=None, stderr=None, universal_newlines=True)
stdout_text, stderr_text = p.communicate(input="1\n\n")

print("stdout: %r\nstderr: %r" % (stdout_text, stderr_text))
if p.returncode != 0:
    raise RuntimeError("%r failed, status code %d" % (cmd, p.returncode))

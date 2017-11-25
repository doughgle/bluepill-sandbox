first = True

class PtraceBreakpoint(gdb.Breakpoint):
    def stop(self):
        global first
        gdb.execute("return (long int) {}".format("0" if first else "-1"))
        first = False

PtraceBreakpoint("ptrace")

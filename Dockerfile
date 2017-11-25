FROM alpine:3.5
RUN apk add --no-cache gdb
COPY .gdbinit /root/.gdbinit
VOLUME /bluepill

#ENTRYPOINT ["gdb", "--eval-command=run"]

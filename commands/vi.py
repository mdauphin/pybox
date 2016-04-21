from icommand import icommand
import os
import curses


class Vi(icommand):
    def process(self,line):
        self.x = self.y = 0
        self.stdscr = curses.initscr()
        (self.height, self.width) = self.stdscr.getmaxyx()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(1)

        self.stdscr.addstr(0, 0, "Screen reso=%dx%d" % (self.height, self.width),
              curses.A_REVERSE)
        self.stdscr.refresh()

        while True:
            c = self.stdscr.getch()
            if c == 27: #curses.ascii.ESC:
                return self.quit()
            elif c == 9: #curses.ascii.BS:
                self.removechar()
            elif c == 10: #new line
                self.nextLine()
            else:
                self.putchar(c)

    def nextLine(self):
        if self.y <= self.height - 1:
            self.y += 1
            self.x = 0
        self.stdscr.setxy(self.y,self.x)
        self.stdscr.refresh()

    def removechar(self):
        if self.x > 0:
            self.x -= 1
        elif self.y > 0:
            self.x = self.width - 1
            self.y -= 1
        self.stdscr.addch(self.y,self.x,' ')

    def putchar(self,c):
        self.stdscr.addch(self.y,self.x,c)
        self.x += 1
        if self.x >= self.width:
            self.x = 0
            self.y += 1

    def quit(self):
        curses.nocbreak(); self.stdscr.keypad(0); curses.echo()
        curses.endwin()

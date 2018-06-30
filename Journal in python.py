# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 20:55:49 2018

@author: Anirban
"""

#Create a journal

import journal

def main():
    print_header()
    run_event_loop()

def print_header():
    print('----------------------------------')
    print('         JOURNAL  APP')
    print('-----------------------------------')
    print()
    print()
    
def run_event_loop():
    print('What do you want to do with your journal')
    cmd=None
    journal_name='default'
    journal_data=journal.load(journal_name)
    while cmd!='x':
        cmd = input('[L]ist entries , [A]dd an entry , E[x]it from the app : ').lower().strip()
        if cmd=='l':
            list_entries(journal_data)
        elif cmd=='a':
            add_entries(journal_data)
        elif cmd!='x':
            print("We Don't understand the Command {}".format(cmd))
            print('x')
    print("Well Done , Done with your App")      
    journal.save(journal_name , journal_data)
    
def list_entries(data):
    print('your journal entries are :')
    print('----------------------------')    
    entries= reversed(data)
    for index ,entry in enumerate(entries):
        print('Your {} entry is [{}]'.format(index+1,entry))
    
def add_entries(data):
    text =input('Type your entry , <enter> to exit : ')    
    #data.append(text)
    journal.add_entry(text,data)
main()
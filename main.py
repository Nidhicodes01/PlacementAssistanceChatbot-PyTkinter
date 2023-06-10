from tkinter import *
from tkinter import PhotoImage
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot=ChatBot('Bot')
trainer=ListTrainer(bot)
for files in os.listdir('data/'):
    data = open('data/'+ files, 'r', encoding='utf-8').readlines()
    trainer.train(data)
data=open('greetings.yml','r',encoding='utf-8').readlines()


def botReply():
    question=questionField.get()
    answer=bot.get_response(question)
    textarea.insert(END,'You: '+question+'\n')
    textarea.insert(END,'Bot: '+str(answer)+'\n')
    questionField.delete(0,END)


root = Tk()
root.wm_title('ChatBot Created by Nidhi')
root.configure(bg='Royal Blue1')
root.wm_geometry("600x670+100+30")
logoPic=PhotoImage(file='chatbot11.png')
logoPicLabel = Label(root, image=logoPic,bg='Royal Blue1')
logoPicLabel.pack(pady=10)
centerFrame=Frame(root)
centerFrame.pack()
scrollbar=Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

textarea=Text(centerFrame, font=('ariel',20,'bold'),height=10,yscrollcommand=scrollbar.set,wrap='word')
textarea.pack(side=LEFT)
scrollbar.configure(command=textarea.yview)

questionField=Entry(root,font=('Ariel',20,'bold'))
questionField.pack(pady=15,fill=X)
askPic=PhotoImage(file='ask.png')
askButton=Button(root,image=askPic,command=botReply)
askButton.pack()
root.mainloop()


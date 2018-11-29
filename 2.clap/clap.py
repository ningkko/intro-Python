# Clap.py
# Yanwan Zhu & Yining Hua
# Lab 2
# Printing out the five verses of the Scandanavian song

def main():
    list1 = ['clap', 'drum', 'tap', 'stamp', 'jump'];
    list2 = ['clapping', 'drumming', 'tapping', 'stampping', 'jumping']
    for n in range(5):
        print('I traveled over land and sea,I met a man who said to me');
        print('An old, old man who said to me,\n“Oh where do you come from?”\n“I belong to',
              list2[n],'land');
        print('To',list2[n],'land,',list2[n],'land,\nAnd if you can',list1[n],'like me');
        print('Then you can come to',list2[n],'land.');
        print('');
            
if __name__ == '__main__':
        main()             

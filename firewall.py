import re
import random

class firewall:

    def input(self,l):
        while 1:
            self.num = input('Desired number of rules? ')
            try:
                self.num = int(self.num)
                if self.num<1:
                    print('Number should be greater than 0')
                    continue
                elif self.num>l:
                    print('Max number of rules exceeded')
                    continue
                else:
                    break
            except ValueError:
                print('Enter the number please')

    def get_rules(self):
        f = open('rules.txt','r',encoding='utf-16')
        text = f.read()
        text = re.sub(" +", " ", text)
        rules = re.split(r"[\r\n]Name :", text)
        list =[]
        enabled = []
        direction = []
        policy = []
        self.input(len(rules))
        for x in range(int(self.num)):
            k = random.randint(0,len(rules))
            j = rules.pop(k)
            a = re.split(r'[\n]',j)
            for x in a:
                self.get_property(x,list,'DisplayName :')
                self.get_property(x,enabled,'Enabled :')
                self.get_property(x,direction,'Direction :')
                self.get_property(x,policy,'PolicyStoreSourceType :')
        print("\n{0} rules to select\n".format(self.num))
        print("Firewall rules:")
        for x in range(len(list)):
            print('\t{0} - {1}'.format(list[x],policy[x]))
        print("Inbound: {0}".format(str(direction.count("Inbound"))))
        print("Outbound: {0}\n".format(str(direction.count("Outbound"))))
        print("Enabled: {0}".format(str(enabled.count("True"))))
        print("Disabled: {0}".format(str(enabled.count("False"))))

    def get_property(self,str,list,name):
        if str.startswith(name):
            list.append(str[len(name)+1:])

x = firewall()
x.get_rules()
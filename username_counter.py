from operator import itemgetter

class Input:
    def string():
        return input("")
    def integer():
        return int(input(""))

class Oper(Input):
    def get_execution_count(self) -> int:
        self.execution_count:int = Input.integer()
        return self.execution_count
    def get_line_count(self) -> int:
        self.line_count:int = Input.integer()
        return self.line_count
    def get_tweeter_id(self) -> str:
        self.tweeter_id:str = Input.string()
        return self.tweeter_id
    def get_username_count(self, _list:list) -> tuple:
        self._list:dict = _list
        self.usernameList:list = list()
        self.returnUnameList:list = list()
        self._dict:dict = dict()
        for self.u_Data in self._list: self.usernameList.append(self.u_Data.split(" ")[0])
        for self.user in self.usernameList: self._dict.update({self.user:self.usernameList.count(self.user)})
        self.maxUnameCount:int =  max(self._dict.items(), key=itemgetter(1))[1]
        for self.key, self.value in self._dict.items():
            if self.value == self.maxUnameCount: self.returnUnameList.append(self.key)
        return (self.returnUnameList, self.maxUnameCount)
    def print_output_data(self, _list:list) -> None:
        self._list:list = _list
        print ("\n")
        for self.item in self._list: 
            self.item[0].sort()
            for self.user in self.item[0]:
                print (self.user+" "+str(self.item[1]))
        print ("\n")

def main() -> None:
    oper:Oper = Oper()
    op_List:list = list()
    execution_count:int = oper.get_execution_count()
    execution_loop_count:int = 1
    while execution_loop_count < execution_count+1:
        line_count:int = oper.get_line_count()
        line_loop_count:int = 1
        tweeter_id_list:list = list()
        while line_loop_count < line_count+1:
            tweeter_id:str = oper.get_tweeter_id()
            tweeter_id_list.append(tweeter_id)
            line_loop_count += 1
        op_List.append(oper.get_username_count(tweeter_id_list))
        execution_loop_count += 1
    oper.print_output_data(op_List)

if __name__ == '__main__':
    main()
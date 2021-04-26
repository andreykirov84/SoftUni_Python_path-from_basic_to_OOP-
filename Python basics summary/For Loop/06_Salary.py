globi = {
    'Facebook': 150,
    'Instagram': 100,
    'Reddit': 50,
}
enough_salary = True
tabs = int(input())
salary = int(input())
while enough_salary and not tabs == 0:
    open_tab = input()
    tabs -= 1
    if open_tab in globi.keys():
        globa = globi.get(open_tab)
        salary -= globa
    if salary <= 0:
        print('You have lost your salary.')
        enough_salary = False

if tabs == 0 and enough_salary:
    print(salary)



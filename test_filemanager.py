from Program import *
import shutil

# тест грязной функции, копируем файл
def test_copy():
    shutil.copyfile("instance.py", "instance_copy.py")
    assert 'instance_copy.py' in os.listdir()





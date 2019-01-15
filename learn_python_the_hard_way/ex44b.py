class Parent(object):
  def override(self):
    print("PARENT OVERRIDE!")


class Child(Parent):
  def override(self):
    print("CHILD override!")


p = Parent()
c = Child()

p.override()
c.override()

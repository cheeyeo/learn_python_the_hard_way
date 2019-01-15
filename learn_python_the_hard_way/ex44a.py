# Simple inheritance

class Parent(object):
  def implicit(self):
    print("PARENT implicit()")


class Child(Parent):
  pass

p = Parent()
c = Child()

p.implicit()
c.implicit()

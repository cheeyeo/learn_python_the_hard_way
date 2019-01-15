class Parent(object):
  def altered(self):
    print("PARENT altered!")


class Child(Parent):
  def altered(self):
    print("CHILD, before PARENT altered")
    super(Child, self).altered()
    print("CHILD, after PARENT altered")


p = Parent()
c = Child()

p.altered()
c.altered()

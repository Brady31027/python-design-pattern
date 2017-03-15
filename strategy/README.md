**Strategy** uses a context or an interface to encasulate a family of functions/algorithms.  
  
For a users, one only needs to access that interface/context to manipulate the corresponding concreate classes. 
  
E.g.  

<pre>  
class BaseClass{  
  function(){};  
}  

class DerivedClass1: BaseClass {
  function(){ print "class1 ";}  
}  

class DerivedClass2: BaseClass {  
  function() { print "class2"; }  
}  

class Context{  
  BaseClass strategy;  
  public Context( BaseClass strategy){  
    self.strategy = strategy;  
  }  
  public void function(){  
    strategy.function()
  }  
}  
</pre>
  
  
For user side:  
  
<pre>
int main() {  
  Context context;  
  context = new Context( new DerivedClass1());  
  context.function();  
  
  context = new Context( new DerivedClass2());  
  context.function();  
  
}
</pre>  
 

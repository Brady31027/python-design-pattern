For static languages such as C/C++, C#, and Java, we usually use **Singleton** pattern to ensure there is only one instance for a class.
However, for dynamic languages such as Python, we can't implement Singleton pattern. One reason is that we cannot hide the constructor.
<br/>
Basic Singleton implementation includes the following concept: <br/>
<br/>
* 1. Only one instance for a class <br/>
* 2. Hide the constructor -- make it **private** <br/>
* 3. Provide a **public** function to access the instance <br/>
<br/>
E.g.<br/>
<br/>
class Singleton() { <br/>
	private static Singleton ins = NULL; <br/>
	**private** Singleton(){ <br/>
		 // init data members <br/> 
	} <br/>
	**public** static Singleton getInstance() { <br/>
		if (ins == NULL) { <br/>
		ins = new Singleton();<br/>
		}<br/>
	return ins<br/>
	}<br/>
}

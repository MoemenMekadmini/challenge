#!/usr/bin/env python
# coding: utf-8

# ### Application: La structure récursive d'une fonction 
# 
# **Les structures conditionnelles nous permet de définier les fonctions à strcuture récursive.**
# 
# **Une fonction est dite `récursive` si, à un moment, elle s'auto-appelle.**     
# 
# **La fonction `somme_rec(n)`ci-dessous, qui retourne la somme des `n`premiers entiers, est une fonction récursive.**
# 
# **Exemple :**
# 
# **On considère la somme suivante :**
# 
# $$\sum_{i=0}^{n}i=n+(n-1)+(n-2)+\dots+2+1+0$$
# 
# **Pour effectuer le calcul de cette somme, on construit une fonction récursive `somme-rec`.**

# In[1]:


def somme_rec(n) :
    if n==1:
        return 1
    else:
        return n+somme_rec(n-1)
somme_rec(5)


# **Application :**
# 
# 
# 
# **Constituez une liste semaine contenant les 7 jours de la semaine.**
# 
# **En utilisant une boucle `while` écrivez une série d'instructions affichant les jours du week-end.** 

# In[2]:


list=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
i=0
while i<7:
    print("Saturday",",","Sunday")
    break

    
        

        


# **Exercice (8):** (synchrone) 
# 
# 1. Ecrire une fonction ``somme_rac(n)`` qui évalue la somme $S$ suivante :
# $$S=\sum_{i=0}^{n} \sqrt{1+i^2} $$
# 
# Tester pour $n=100$ et $n=200$.

# In[14]:


def somme_rac(n):
    return (1+n**2) **0.5
somme_rac(100)


    
    
    

    
    
    


# In[ ]:





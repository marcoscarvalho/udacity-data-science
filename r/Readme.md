# R
Link: https://www.r-project.org/
[R Basics Lesson in OMSCS Student Orientation](https://www.udacity.com/course/viewer#!/c-gt101/l-729069797/m-6789510772)

# Documentação R
[Quick R ](http://www.statmethods.net/)
[R Cookbook](http://www.cookbook-r.com/) 
[R-Bloggers](http://www.r-bloggers.com/)
[StackOverflow About R ](http://stackoverflow.com/tags/r/info)
[StackOverflow R FAQ ](http://stackoverflow.com/questions/tagged/r-faq%20)
[Google's R Style Guide ](https://google-styleguide.googlecode.com/svn/trunk/Rguide.xml)
[Jupyter and Conda for R](https://www.udacity.com/course/viewer#!/c-ud404/l-7826212765/m-9297122616)


# Download para Ubuntu
Brent Wagenseller, um estudante do Online Master of Science Computer Science (OMS CS) do Georgia Tech College of Computing (EUA), postou estas instruções na Piazza (agosto de 2016) para qualquer pessoa que esteja usando Ubuntu para executar R. 


Eu primeiro instalei R pouco menos de um ano atrás e parece que as instruções mudaram um pouco (não sei se você ainda precisa adicionar as chaves assinadas, foi necessário no ano passado, mas pode não ser agora). Além disso, você precisa escolher um mirror - eu escolhi 'lib.stat.cmu.edu/R/CRAN/', mas escolha um na lista de mirrors em https://cran.r-project.org. 
Não tenho certeza se mais alguém está usando o Ubuntu como sua máquina principal, mas se você estiver - aqui estão minhas instruções salvas (e muito resumidas).


Instruções para Instalação de R: https://cran.r-project.org


Para instalar R no Ubuntu, mude para o modo root e edite sources.list:
```
vi /etc/apt/sources.list
```

Agora, escolha um mirrore adicione isso ao final de sources.list (neste caso eu escolhi o mirror 'lib.stat.cmu.edu/R/CRAN/':


## Pacote para R
```
deb http://lib.stat.cmu.edu/R/CRAN/bin/linux/ubuntu xenial/
```
Observe que a versão pode mudar de acordo com a versão do Ubuntu; você pode simplesmente ir direto e ver as versões disponíveis (por exemplo, acessei http://lib.stat.cmu.edu/R/CRAN/bin/linux/ubuntu e vi esse xenial - o mais recente para o Ubuntu 16.04 - estava disponível)


Salve e saia de sources.list pressionando a tecla 'ESC' e digitando:
```
:wq!
```
Isso exigirá chaves assinadas específicas para serem adicionadas ao seu sistema; de acordo com as instruções de R, execute estes comandos:
```
gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9
gpg -a --export E084DAB9 | apt-key add -
```
Nota: eu sei que isso foi necessário em setembro de 2015, mas pode não ser agora.


Para instalar R:
```
apt-get install r-base r-base-dev libatlas3-base littler r-cran-getopt
```
Se você quiser instalar bibliotecas python:
```
apt-get install python-rpy python-rpy-doc python-rpy2
```
<!-- Declaring image and link variables here -->
[StartProject]: ./images/app.png
[RunServer]: ./images/django-startapp.png
[CodeSnippet]: ./images/code-snippet.png
[AppNaming]: ./images/naming.png
[BadCSS]: ./images/bad-css.png
[GoodCSS]: ./images/good-css.png

[Python]: https://www.python.org/
[PIP]: https://pip.pypa.io/en/stable/

# How did it go? 

## Experience
The overall experience for building this app was excellent and a lot of learning. I enjoyed every step; although some did have some issues or maybe were not clear enough, and did some serious learning on how to build a Microsoft Graph application and how to integrate it with OAuth with Azure Active Directory and many more things! 

## Process
The process for building the application was pretty straighforward. It was like building legos, but know how the legos work and understanding the implementation to be able to fix any issues that showed up along the way.

### Prerequisites
---

The prerequisites section was simple, easy to follow and understand. The prerequisites were:

> Have [**`Python 3.8.2`**][Python] or greater installed.

> Make sure your [**`Python 3.8.2`**][Python] interpreter has [PIP][PIP] installed.

> A personal **`Outlook`** account.

### Create the Django Dev Server and the Django App
---
The process was started by utilizing the interpreter's package manager [`pip`][PIP] which was used to install a series of _libraries_ for this application to properly work. 

The required _libraries_ are:

> `django==3.0.4`

> `requests_oauthlib==1.3.0`

> `pyyaml==5.3.1`

> `python-dateutil==2.8.1`

You can simply add the libraries by executing the following command:


    pip install [{library_name}=={version}]


Once this is ready, you can simply proceed to create the project by issuing the following command:


    django-admin startproject [project_name]

When the previous command was executed, the project tree was created.



![Image][StartProject]

Then you were requested start the app using the following command. Additionally, you can specify the port number if you wish.

    python manage.py runserver localhost:[port]

Then open your browser and check the `localhost (127.0.0.1)` using `port 8000`; or the port of your preference, you would see this site from the Django development server you were running in your local machine:

![Image][RunServer]

Once the development server is up and running, you can proceed to create the application. You can start by issuing the following command:

    python manage.py startapp [app_name]

This created the folder called 'tutorial' in the project tree.



Afterwards, we initialize the SQLite database by runnign the `migrate` command. 

    python manage.py migrate

This command will create all the tables needed for the server built-in functionalities logging. 

Once were done with this, you were expected to follow next steps in the tutorial documentation, adding methods, tweaking code, changing code and adding other code to the application to integrate it with Azure Active Directory and Microsoft Graph. 

<br>

## Difficulties
The only difficulty I experienced while doing this tutorial was to get the `app.css` file working. I apparently created it in the incorrect directory. 

This is how it looked when the file was not being loaded in the `layout.html` template.

![Image][BadCSS]

After fixing the directory issue and adding it to the correct hierarchy level, this is how it started to look. 

![Image][GoodCSS]

You may determine from the first image that the text box and the padding was off. It was not respecting what was declared in the `app.css` file at all. After fixing the problem, you can see in the second image how the padding is properly working and now the alert was not stuck to the top menu bar.

## Suggestions
> Some suggestions I would make for this tutorial in GitHub is to add the actual page link to the code snippets that were required to add, remove or modify code in the various Python files. This really gave off a bad user experience, as you would need to manually go back, go to the repository tree, browser the files, find the file and then look for the code snippet. For example, I noticed that usually you would see something like this:

![Image][CodeSnippet]

My suggestion for this would be:

+ Instead of adding the `:::code language ... id="CodeSnippetId":::` text, you could have added a simple redirection link to the file you needed the user to copy the code from. This would have made things a lot faster and also, you could have suggested something like: "Once you are in th document, you can use `CTRL + F` and look for the actual id which is `ABCD`. It was really not that intuitive at first. Once you understood what that was and how to look for it, it was simple. You could also just duplicate the tab and have an additional tab to browse the code, but it is still slower than simply having the ability to jumping directly to the file you needed to check. 

> Another thing I noticed is that sometimes it is assumed that this is only going to be looked at by experienced developers and you assume all the concepts will be known, which I think could be fixed by adding some link references in the words that might not be clear to less experienced developers. For example, understanding the Django project tree structure and how that works. I would suggest:

+ For people that are new to coding it may be hard to understand what `./directory/path/example` is. Maybe adding a short reference to a site that explains how directory hierarchy works would have been very appreciated for people with least experience. As well, people that are new to the Django project tree structure might find it a bit confusing. 

> Another thing that I found kind of confusing was the naming conventions for this application. There was a lot of times when the word `tutorial` was used. This can confuse many people. My suggestions would be: 
+ Instead of using an app name called `tutorial` you could have possibly used something like **DjangoDevServerTest** or **DjangoServerTest**. I think avoiding things like these can help the person understand exactly what they are doing, which in this case was setting up a _Django Development Server_. 
+ Instead of reusing the same `tutorial` name for the templates folder, you could have done something like `views` or `html pages` for instance. It was confusing because the application itself was called `tutorial` so sometimes it was hard to know which `tutorial` folder this was refering to. 

    ![Image][AppNaming]

# Conclusion
The overall experience was very intense, frustrating, fun, rewarding, ups and downs; just the typical developer stages while coding something that is new to him/her! I think this was very interesting, especially for me because I had never used Microsoft Graph before, I did used OAuth and OAuth2 in the past while I was in college, but it was also cool to be able to integrate that to Azure Active Directory. The process of documenting this learning document was also of much advantage, as it helped me to re-engage with Markdown (which I had kind of forgotten about) and also to use Git again. I did a lot of learning by reading the different methods that were used to build the authentication code blocks for the Django application as well as the Django development server itself. Understanding how the Django framework works alone was quite the read! I really enjoyed this process.
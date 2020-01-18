# Python: automatisation de configurations Cisco

<a href="https://www.casimages.com/i/20011805252325065016607769.png.html" target="_blank" title="Mon image"><img src="https://nsm09.casimages.com/img/2020/01/18//20011805252325065016607769.png" border="0" alt="Mon image" /></a>

Le but ce ce projet est d'automatiser des configurations sur du matériel Cisco avec Python et le protocole Telnet: 
* La créations automatique de Vlans et d'assignations de ports pour le Switch.
* La mise en place d'un rôle DHCP et du routage statique pour le Routeur. 

Pour ce faire on dispose de plusieurs scripts: 
* Le script principal administration_cisco.py demande dans un premier temps à l'utilisateur de choisir entre le Switch et le Routeur. Puis dans un deuxième temps une liste de tâches automatique lui sera proposé.
* Le script vlan.py va automatiquement créer 2 vlans: un vlan 11 pour le directeur et un vlan 12 pour une employés des Ressources Humaines.
* Le script port_switch.py va affecter deux ports aux vlans créer précédemment et configurer deux autres ports en mode trunk.
* Le script dhcp_routage_vlan.py va créer deux subinterfaces qui feront office de gateway pour chaque vlan ainsi que l'ajout d'un rôle DHCCP pour le Routeur.
* Le script routage_statique.py va créer un routage statique simple entre notre LAN et Internet


## Prérequis

* Un poste ou une machine virtuelle sous Linux disposant d'une version récente de Python version 3. Pour la rédaction des scripts Python on a utilisé le logiciel Visual Studio Code.
* Configurer une connexion Telnet pour permettre l'administration du Switch et du Routeur à distance.
* Une connaissance des commandes CLI Cisco.

## Etablir une connexion Telnet entre les équipements Cisco et le poste de travail sous Linux.

Dans un premier temps on va devoir manuellement configurer le Switch et le Routeur pour permettre une connexion à distance via notre machine sous Linux. Dans notre exemple on utilisera le Switch mais les commandes sont à une exceptions près les mêmes à faire sur le Routeur.

Switch>en
Switch#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Switch(config)#
interface vlan 1
Switch(config-if)#ip address 192.168.10.253 255.255.255.0
Switch(config-if)#no shut
%LINK-5-CHANGED: Interface Vlan1, changed state to up
%LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan1, changed state to up
Switch(config-if)#exit
Switch(config)#ip default-gateway 192.168.10.254
Switch(config)#exit


## Your first website

**GitHub Pages** is a free and easy way to create a website using the code that lives in your GitHub repositories. You can use GitHub Pages to build a portfolio of your work, create a personal website, or share a fun project that you coded with the world. GitHub Pages is automatically enabled in this repository, but when you create new repositories in the future, the steps to launch a GitHub Pages website will be slightly different.

[Learn more about GitHub Pages](https://pages.github.com/)

## Rename this repository to publish your site

We've already set-up a GitHub Pages website for you, based on your personal username. This repository is called `hello-world`, but you'll rename it to: `username.github.io`, to match your website's URL address. If the first part of the repository doesn’t exactly match your username, it won’t work, so make sure to get it right.

Let's get started! To update this repository’s name, click the `Settings` tab on this page. This will take you to your repository’s settings page. 

![repo-settings-image](https://user-images.githubusercontent.com/18093541/63130482-99e6ad80-bf88-11e9-99a1-d3cf1660b47e.png)

Under the **Repository Name** heading, type: `username.github.io`, where username is your username on GitHub. Then click **Rename**—and that’s it. When you’re done, click your repository name or browser’s back button to return to this page.

<img width="1039" alt="rename_screenshot" src="https://user-images.githubusercontent.com/18093541/63129466-956cc580-bf85-11e9-92d8-b028dd483fa5.png">

Once you click **Rename**, your website will automatically be published at: https://your-username.github.io/. The HTML file—called `index.html`—is rendered as the home page and you'll be making changes to this file in the next step.

Congratulations! You just launched your first GitHub Pages website. It's now live to share with the entire world

## Making your first edit

When you make any change to any file in your project, you’re making a **commit**. If you fix a typo, update a filename, or edit your code, you can add it to GitHub as a commit. Your commits represent your project’s entire history—and they’re all saved in your project’s repository.

With each commit, you have the opportunity to write a **commit message**, a short, meaningful comment describing the change you’re making to a file. So you always know exactly what changed, no matter when you return to a commit.

## Practice: Customize your first GitHub website by writing HTML code

Want to edit the site you just published? Let’s practice commits by introducing yourself in your `index.html` file. Don’t worry about getting it right the first time—you can always build on your introduction later.

Let’s start with this template:

```
<p>Hello World! I’m [username]. This is my website!</p>
```

To add your introduction, copy our template and click the edit pencil icon at the top right hand corner of the `index.html` file.

<img width="997" alt="edit-this-file" src="https://user-images.githubusercontent.com/18093541/63131820-0794d880-bf8d-11e9-8b3d-c096355e9389.png">


Delete this placeholder line:

```
<p>Welcome to your first GitHub Pages website!</p>
```

Then, paste the template to line 15 and fill in the blanks.

<img width="1032" alt="edit-githuboctocat-index" src="https://user-images.githubusercontent.com/18093541/63132339-c3a2d300-bf8e-11e9-8222-59c2702f6c42.png">


When you’re done, scroll down to the `Commit changes` section near the bottom of the edit page. Add a short message explaining your change, like "Add my introduction", then click `Commit changes`.


<img width="1030" alt="add-my-username" src="https://user-images.githubusercontent.com/18093541/63131801-efbd5480-bf8c-11e9-9806-89273f027d16.png">

Once you click `Commit changes`, your changes will automatically be published on your GitHub Pages website. Refresh the page to see your new changes live in action.

:tada: You just made your first commit! :tada:

## Extra Credit: Keep on building!

Change the placeholder Octocat gif on your GitHub Pages website by [creating your own personal Octocat emoji](https://myoctocat.com/build-your-octocat/) or [choose a different Octocat gif from our logo library here](https://octodex.github.com/). Add that image to line 12 of your `index.html` file, in place of the `<img src=` link.

Want to add even more code and fun styles to your GitHub Pages website? [Follow these instructions](https://github.com/github/personal-website) to build a fully-fledged static website.

![octocat](./images/create-octocat.png)

## Everything you need to know about GitHub

Getting started is the hardest part. If there’s anything you’d like to know as you get started with GitHub, try searching [GitHub Help](https://help.github.com). Our documentation has tutorials on everything from changing your repository settings to configuring GitHub from your command line.

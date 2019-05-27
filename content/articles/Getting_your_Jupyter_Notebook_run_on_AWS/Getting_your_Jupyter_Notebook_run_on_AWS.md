Title: Getting your Jupyter Notebook run on AWS
Date: 2019-04-21 7:25:50
Category: Blog
Tags: python, aws, EC2, jupyter notebook, cloud
Slug: Getting your Jupyter Notebook run on AWS

If you are just getting started with deep learning and you don’t have excess cash to spend on machines, it’s cost effective to use a…

----------

**Getting your Jupyter Notebook run on AWS**

![](https://cdn-images-1.medium.com/max/800/1*LFUeY_cJiwP4I50f0KWJAw.jpeg)


If you are just getting started with deep learning and you don’t have excess cash to spend on machines, it’s cost effective to use a cloud service. This tutorial discusses how to get a Jupyter Notebook running on AWS cloud service.
The first step is to register on [https://aws.amazon.com](https://aws.amazon.com/) and verify your account.

![](https://cdn-images-1.medium.com/max/800/1*q38SmbVKEtvYfmYOy1YTyg.png)


During my registration I couldn’t verify my account using my mobile phone so I had to contact AWS support. Once you have your account verified the next step is to visit [https://console.aws.amazon.com/ec2/v2/home](https://console.aws.amazon.com/ec2/v2/home)

![](https://cdn-images-1.medium.com/max/800/1*KEOu3sb_mYU6sUNpdDVDjw.png)


Choose your preferred region and then click on Launch Instance to start the provisioning of your first virtual machine in the cloud.
After clicking on Launch instance it will take you to a page where you select your Amazon Machine Image (AMI). This is the machine you will be working with. In this tutorial I will use Deep Learning AMI (ubuntu) since it doesn’t need any special configuration to start my deep learning.

![](https://cdn-images-1.medium.com/max/800/1*dhsv6WkW7dn_Um64tbt6AA.png)


After choosing your AMI the next page will allow you configure the hardware specifications of your machine.

![](https://cdn-images-1.medium.com/max/800/1*2BosKuwSoLU-yeskXpi_Qw.png)


For the purpose of this tutorial, I will choose p2.xlarge

![](https://cdn-images-1.medium.com/max/800/1*rXMG0MvGJiZ9DyUibABhGQ.png)


For GPU enabled deep learning p2.xlarge instance is powerful yet economical, only costing around $0.90 per hour of use (as of 2018). P2 instances provide up to 16 NVIDIA K80 GPUs, 64 vCPUs and 732 GiB of
host memory with a combined 192 GB of GPU memory, as shown in the screenshot above.
The next step is to configure the security group of the new instance to allow Jupyter Notebook. Create a custom TCP entry with address set to “localhost” and port set to “8888”.

![](https://cdn-images-1.medium.com/max/800/1*jTIjPVldKdGnSpzTXPVqZg.png)


This screenshot shows how I added a custom TCP entry

![](https://cdn-images-1.medium.com/max/800/1*5TzcUK1NNT_554PfUlHD-g.png)


Click on Review and launch.

![](https://cdn-images-1.medium.com/max/800/1*QwqDmxeniPWE4OUzx3Yi9g.png)


Clicking on Launch will take you to another page where you create and download a key pair for the newly created instance. Make sure your downloaded key pair (.pem) is in your working directory.

![](https://cdn-images-1.medium.com/max/800/1*kiH7yTDJrZvWORUOEs0RLA.png)


Click on Launch instances to launch your instances

![](https://cdn-images-1.medium.com/max/800/1*t6D2wNUG10xvXcS63SPzpg.png)


Now the instances are launched and running! 🕺🕺💃💃
Time to start running our Jupyter Notebook. Before we start running our Jupyter Notebook there are some things we have to take note of:

1. Your downloaded pair key (.pem file name)
2. Public DNS (IPv4)
![](https://cdn-images-1.medium.com/max/800/1*sD1g_m4L75D6NFXDDUhWNA.png)


Your Public DNS (IPv4) is highlighted in the picture.
Open your terminal, create your project directory using this command `mkdir deeplearning` and ****navigate into your created directory.

![](https://cdn-images-1.medium.com/max/800/1*Zexo-5g0aefAhMT5v3StFg.png)


Once you are in the project directory, run the following command:

    chmod 0400 <your .pem file name>
    ssh -L localhost:8888:localhost:8888 -i <your .pem file name> ubuntu@<Public DNS (IPv4)>

We have it all set up now.
So anytime you want to run your server, type the following command:

    ssh -L localhost:8888:localhost:8888 -i <your .pem file name> ubuntu@<Public DNS (IPv4)>
    jupyter notebook

After running the first command you should get an output similar to what is shown in the screenshot below

![](https://cdn-images-1.medium.com/max/800/1*RpfbmL3rz4tJlkXVezC5sQ.png)


then you run `jupyter notebook`to get your server running

![](https://cdn-images-1.medium.com/max/800/1*la1DYxhh4pZt6zHHYoq3Wg.png)


You can now access your Jupyter Notebook via your browser

![](https://cdn-images-1.medium.com/max/800/1*jZ_YWpxBcH3JO5GVUO4sbg.png)


jupyter notebook
**The next step is to upload your files and start building models.**
To upload files from my local machine to the AWS instance I will use a program called Secure Copy (SCP).
Run the following command to upload files with SCP:

    scp -i ~/deeplearning/<your .pem file name> ~/deeplearning/Cat_Dogs.zip  ubuntu@<Public DNS (IPv4)>:~/data/

This command will upload “Cat_Dogs.zip” in your ~/deeplearning/ directory to ~/data/ on Amazon instance.
We have successfully uploaded our file to our Amazon instance. We can now start building models.
**Happy Building !!**😀😀😀
I welcome feedback and constructive criticism. Thank you.


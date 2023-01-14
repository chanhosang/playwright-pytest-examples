# -*- mode: ruby -*-
# vi: set ft=ruby :
require 'yaml'
require 'etc'


$script = <<-'SCRIPT'
apt-get update -y
apt install -y python3-pip
ln -sf /usr/bin/python3 /usr/bin/python
apt install -y python-pytest
apt install -y gstreamer1.0-plugins-bad libenchant1c2a gstreamer1.0-libav
pip install pytest-playwright
PATH="$HOME/.local/bin:$PATH"
SCRIPT

Vagrant.configure("2") do |config|
    # https://app.vagrantup.com/peru/boxes/ubuntu-20.04-desktop-amd64
    config.vm.box = "peru/ubuntu-20.04-desktop-amd64"
    config.vm.box_version = "20230101.01"
	
	config.vm.provider "virtualbox" do |v|
	  # To start the guest machine in headless mode by default
      # due to some intermittent compatibility issue when starting in GUI mode on Windows 11 Pro
      v.gui = false 
	end


    # We don't want to generate new ssh keys because of bug in 1.8.5 Vagrant
    config.ssh.insert_key = false	
	
    config.vm.provision "shell", inline: $script
	
	config.vm.synced_folder ".", "/home/vagrant/src"
	
	# To should be installed by project
    #playwright install
end

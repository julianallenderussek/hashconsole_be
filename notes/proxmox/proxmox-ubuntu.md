https://www.reddit.com/r/Proxmox/comments/1058ko7/installing_tools_into_a_cloudinit_image/



```bash
cd /root
mkdir cloud-init-images
cd cloud-init-images/
wget https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img
sudo apt install libguestfs-tools -y
virt-customize -a ubuntu-22.04-minimal-cloudimg-amd64.img --install qemu-guest-agent,ncat,net-tools,bash-completion
mv ubuntu-22.04-minimal-cloudimg-amd64.img ubuntu-22.04-minimal-cloudimg-amd64.qcow2
qemu-img resize ubuntu-22.04-minimal-cloudimg-amd64.qcow2 20G
```




```bash
cd /root
mkdir cloud-init-images
cd cloud-init-images/
wget https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img
sudo apt install libguestfs-tools -y
virt-customize -a ubuntu-22.04-minimal-cloudimg-amd64.img --install qemu-guest-agent,ncat,net-tools,bash-completion
mv ubuntu-22.04-minimal-cloudimg-amd64.img ubuntu-22.04-minimal-cloudimg-amd64.qcow2
qemu-img resize ubuntu-22.04-minimal-cloudimg-amd64.qcow2 20G
```

From GUI:

Create a new VM 9000

On OS tab choose "Do not use any media"

On System tab enable qemu-agent

On Disk tab delete scsi0

```
sudo qm set 9000 --serial0 socket --vga serial0
qm importdisk 9000 /root/cloud-init-images/ubuntu-22.04-minimal-cloudimg-amd64.qcow2 local-lvm
```

From GUI:

On the hardware tab you now find an unused disk, select it and click edit and then enable Discard and SSD emulation (Advanced Options) if local-lvm is on a SSD.

Then go to Options -> Boot Options and enable scsi0 as boot device and move it at second position.

If you want, make a backup before converting to template, just in case.

Finally, right click and Convert to template


# MY HISTORY
```bash
  255  apt install guestfs-tools
  256  ls
  257  wget https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img
  258  sudo apt install libguestfs-tools -y
  259  apt install libguestfs-tools -y
  260  virt-customize -a ubuntu-22.04-minimal-cloudimg-amd64.img --install qemu-guest-agent,ncat,net-tools,bash-completion
  261  ls
  262  virt-customize -a jammy-server-cloudimg-amd64.img --install qemu-guest-agent,ncat,net-tools,bash-completion
  263  sudo qm set 900 --serial0 socket --vga serial0~
  264  qm set 900 --serial0 socket --vga serial0~
  265  qm set 900 --serial0 socket --vga serial0
  266  qm importdisk 900 /root/jammy-server-cloudimg-amd64.img local 
```

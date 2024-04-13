"""Setup up SFTP on a Ubuntu server. The node will boot the default operating system, which is typically a recent version of Ubuntu.
Setup log can be found at /local/repository/setup-<sftp-username>.log


Instructions:
- The setup requires the user to enter a username and password for the sftp server.
- Once the experiment is created, wait for the profile instance to start.
- Run the following command from the host where you want to download/upload files to the Cloudlab SFTP server:
    `sftp <sftp-user>@<CLOUDLAB-SERVER-IP>`

"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

pc.defineParameter(
    "sftpUsername", "Provide a username to setup SFTP on the node", portal.ParameterType.STRING, "sftpuser",
    longDescription="This username will be used by sshd to establish connection.")

pc.defineParameter(
    "sftpPassword", "Provide a password for the SFTP user", portal.ParameterType.STRING, "sftpuser",
    longDescription="This password will be used by sshd authenticate the connection.")

params = pc.bindParameters()
# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
 
# Add a raw PC to the request.
node = request.RawPC("node")

# Install and execute a script that is contained in the repository.
node.addService(pg.Execute(shell="sh", command="sudo /local/repository/start.sh {} {} > /local/repository/setup-{}.log 2>&1".format(params.sftpUsername, params.sftpPassword, params.sftpUsername)))

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)

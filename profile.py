"""Setup up SFTP for the cloudlab user. The node will boot the default operating system, which is typically a recent version of Ubuntu.
Setup log can be found at /local/repository/setup-<user>.log



Instructions:
- The setup requires the user to enter their Cloudlab user.
- Once the experiment is created, wait for the profile instance to start.
- Run the following command from the host where you want to download/upload files to your Cloudlab SFTP server:
    `sftp <cloudlab-user>@<CLOUDLAB-SERVER-IP>`

"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

pc.defineParameter(
    "sftpUser", "Provide your cloudlab username to setup SFTP on the node", portal.ParameterType.STRING, "root",
    longDescription="Provide your cloudlab username to setup SFTP on the node")

params = pc.bindParameters()
# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
 
# Add a raw PC to the request.
node = request.RawPC("node")

# Install and execute a script that is contained in the repository.
node.addService(pg.Execute(shell="sh", command="sudo /local/repository/start.sh {} > /local/repository/setup-{}.log 2>&1".format(params.sftpUser, params.sftpUser)))

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)

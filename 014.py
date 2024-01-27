from pyVim import connect
from pyVmomi import vim
import ssl
import argparse
 
def connect_vcenter(host, user, password):
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    ssl_context.verify_mode = ssl.CERT_NONE
 
    service_instance = connect.SmartConnect(host=host,
                                            user=user,
                                            pwd=password,
                                            sslContext=ssl_context)
    return service_instance
 
def find_entity_by_name(content, vimtype, name):
    container = content.viewManager.CreateContainerView(content.rootFolder, [vimtype], True)
    for entity in container.view:
        if entity.name == name:
            return entity
    return None
 
def create_vm(service_instance, cluster_name, vm_name, datastore_name, template_name, static_ip):
    content = service_instance.RetrieveContent()
 
    cluster = find_entity_by_name(content, vim.ClusterComputeResource, cluster_name)
    if not cluster:
        print(f"Cluster '{cluster_name}' not found")
        return
 
    datastore = find_entity_by_name(content, vim.Datastore, datastore_name)
    if not datastore:
        print(f"Datastore '{datastore_name}' not found")
        return
 
    template_vm = find_entity_by_name(content, vim.VirtualMachine, template_name)
    if not template_vm:
        print(f"Template VM '{template_name}' not found")
        return
 
    vm_folder = cluster.resourcePool
    clone_spec = vim.vm.CloneSpec(powerOn=False, template=False)
    clone_spec.location = vim.vm.RelocateSpec(datastore=datastore)
 
    customization_spec = vim.vm.customization.Specification()
    customization_spec.nicSettingMap = [
        vim.vm.customization.AdapterMapping(ip=vim.vm.customization.FixedIp(address=static_ip))
    ]
    clone_spec.customization = customization_spec
 
    task = template_vm.Clone(name=vm_name, folder=vm_folder, spec=clone_spec)
    print("Creating VM...")
 
    while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
        continue
 
    if task.info.state == vim.TaskInfo.State.success:
        print("VM created successfully!")
    else:
        print("Error creating VM:", task.info.error.msg)
 
    connect.Disconnect(service_instance)
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a VM in vCenter")
    parser.add_argument("--host", required=True, help="vCenter hostname or IP")
    parser.add_argument("--user", required=True, help="vCenter username")
    parser.add_argument("--password", required=True, help="vCenter password")
    parser.add_argument("--cluster", required=True, help="Cluster name")
    parser.add_argument("--vm-name", required=True, help="Name for the new VM")
    parser.add_argument("--datastore", required=True, help="Datastore name")
    parser.add_argument("--template", required=True, help="Template VM name")
    parser.add_argument("--static-ip", required=True, help="Static IP for the new VM")
 
    args = parser.parse_args()
 
    service_instance = connect_vcenter(args.host, args.user, args.password)
    create_vm(service_instance, args.cluster, args.vm_name, args.datastore, args.template, args.static_ip)

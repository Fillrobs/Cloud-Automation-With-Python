import ansible.runner
 
# Run Ansible playbook for deployment
runner = ansible.runner.Runner(
    module_name='shell',
    module_args='ls',
    pattern='all',
    forks=10
)
result = runner.run()
print(result)

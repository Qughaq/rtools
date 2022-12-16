import os

project_path = r'/Users/jrahmat/rprojects/voomDDA'

if __name__ == '__main__':
    count = 0
    library_set = set()
    for root, dirs, file_names in os.walk(project_path):
        for file_name in file_names:
            if file_name.endswith('.R') and not file_name.startswith('.'):
                refactored = False
                file_data = ''
                full_file_path = os.path.join(root, file_name)
                with open(full_file_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        if 'library(' in line:
                            line = line.replace(' ', '').replace('\n', '').replace('\t', '')
                            if line.startswith('library(') and line.endswith(')'):
                                line = line.replace('library(', '').replace(')', '')
                                library_set.add(line)
                        file_data += line

                if refactored:
                    with open(full_file_path, 'w', encoding='utf-8') as file:
                        file.write(file_data)

    print('')
    install_packages_command = 'install.packages(c("' + '", "'.join(library_set) \
                               + '", dependencies = TRUE))'
    print('1.terminal command for install.packages:')
    print(install_packages_command)

    print('')
    bio_pkgs = 'bio_pkgs <- c("' + '", "'.join(library_set) + '")'
    bioc_manager_install_command = 'BiocManager::install(' \
                                   + f'{bio_pkgs=}'.split('=')[0] \
                                   + ', dependencies = TRUE)'
    print('2.terminal command for BiocManager')
    print(bio_pkgs)
    print(bioc_manager_install_command)

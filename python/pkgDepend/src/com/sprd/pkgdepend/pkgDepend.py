#!/usr/bin/env python
# coding=utf-8
import os
import fnmatch
import codecs
import logging
import sys
import subprocess
from xml.etree import ElementTree
import sys   
from __builtin__ import list, str, filter
from apt.cache import Filter
from gtk._gtk import Item
from posix import chmod
from time import sleep
import xlwt
import random
import time

        

      
class PkgDependencyOperation:
    def __init__(self):
        pass
    
    def do_JDepend_Cmd(self, analyse_path):
        print "do_JDepend_Cmd analyse_path:",analyse_path,"-------------begin"
        
        pipe = subprocess.Popen('java jdepend.xmlui.JDepend -file report.xml %s' % analyse_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        #pipe = subprocess.Popen('java jdepend.xmlui.JDepend -file report.xml ~/workspace/sprdroid6.0_trunk/frameworks/base/', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        pipe.wait()
        
        print "do_JDepend_Cmd analyse_path:",analyse_path,"----output report.xml--------end"
        
    def dex2jar(self,path_include_dex):
        global originalDir
        print "dex2jar path:",path_include_dex,"--------------------begin"
        
        dex2jar_tool_path = "../../../../dex/dex2jar-0.0.9.8"
        if not os.path.exists(dex2jar_tool_path):
            print "dex2jar_tool_path not exist"
            exit(1)
        os.chdir(dex2jar_tool_path)
        
        pipe = subprocess.Popen('./dex2jar.sh %s' % path_include_dex, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        pipe.wait()

        os.chdir(originalDir)
        print "dex2jar path:",path_include_dex,"-------------------end"
        
    def get_jar_path(self, product_full_path):
        jar_path = None
        if os.path.exists( product_full_path ):
            floder_and_file = os.path.split(product_full_path)
            floder = floder_and_file[0]
            
            for path in os.listdir(floder):
                if "_dex2jar" in path:     
                    jar_path = floder + "/" + path
                    print "dex2jar produce: ", jar_path
                    return jar_path
        
        return jar_path
        
        
class Result:
    def __init__(self, pkg_path, pkg_name, dependon_name):
        self.pkg_path = pkg_path
        self.pkg_name = pkg_name
        self.dependon_name = dependon_name
        
class AnalysePathInfo:
    def __init__(self, src_path, product_path):
        self.src_path = src_path
        self.product_path = product_path
        
class PackageInfo:
    def __init__(self, packagename, dependon_name_list, dependon_count, usedby_name_list, usedby_count):
        self.packagename = packagename
        self.dependon_name_list = dependon_name_list
        self.dependon_count = dependon_count
        self.usedby_name_list = usedby_name_list
        self.usedby_count =  usedby_count
        
        
class PkgPathGitInfo: 
    def __init__(self, pkg_name, pkg_path, pkg_gitname):
        self.pkg_name = pkg_name
        self.pkg_path = pkg_path
        self.pkg_gitname = pkg_gitname

class ResultManager:
    def __init__(self):
        #self.pkg_path_pair_all = dict()
        #self.pkg_dependon_pair_all = dict()
        #self.pkg_usedBy_pair_all = dict()
        self.result_all = list()
        self.depend_all = dict()
        self.git_dependcy_all = dict()
        self.pkg_to_pathAndGitname_all = dict()
                
    def add_result(self, analyse_path, pkg_name, dependon_name):
        if( self.check_if_repeat(analyse_path, pkg_name, dependon_name) == True):
            print "add_pkg_dependon_pair,this is repeat "
            return False
        result = Result(analyse_path,pkg_name,dependon_name)
        self.result_all.append(result)
        return True

    def add_package_info(self, pathname, packagename, dependon, dependon_count, dependby, usedby_count):
        if self.depend_all.has_key(pathname):
            packagelist = self.depend_all[pathname]
        else:
            packagelist = list()
            self.depend_all.update({pathname: packagelist})
        
        packageInfo = PackageInfo(packagename, dependon, dependon_count, dependby, usedby_count);
        packagelist.append(packageInfo)

    def add_pkg_dependon_pair(self, pkg_name, dependon_name_list):
        self.pkg_dependon_pair_all[pkg_name] = dependon_name_list
        return True

    def add_pkg_usedBy_pair(self, pkg_name, usdBy_name_list):
        self.pkg_usedBy_pair_all[pkg_name] = usdBy_name_list
         
         
    def check_if_repeat(self, analyse_path, pkg_name, dependon_name):
        if len(self.result_all) != 0:
            for result_tmp in self.result_all:
                if analyse_path == result_tmp.pkg_path and pkg_name == result_tmp.pkg_name and dependon_name == result_tmp.dependon_name:
                    return True
        else:
            return False
    
    def print_xls_output(self, xls_filename):
        print "--------------print_xls_output begin---------------------"
        #define Workbook    
        wb = xlwt.Workbook(encoding='utf-8')
        self.create_sheet1_original(wb)
        #self.create_sheet1(wb)
        #pkgs_in_path = self.create_sheet2(wb)
        #self.create_sheet3(wb,pkgs_in_path)
        wb.save(xls_filename)
        print "--------------print_xls_output end---------------------"
        
    def create_sheet1_original(self, wb):
        print "--------------create_sheet1 begin---------------------"
        font = xlwt.Font() # Create the Font
        font.name = 'Times New Roman'
        font.bold = True
        font.italic = True
        style = xlwt.XFStyle() # Create the Style
        style.font = font # Apply the Font to the Style
        
        ws = wb.add_sheet('Sheet1-path-pkg-dependupon')
        
        ws.col(0).width = 13000
        ws.col(1).width = 6666
        ws.col(2).width = 5000
        ws.col(3).width = 12000
        ws.col(4).width = 5000
        ws.col(5).width = 12000
        ws.write(0, 0, "Path", style)
        ws.write(0, 1, "Package", style)
        ws.write(0, 2, "Dependupon count", style)
        ws.write(0, 3, "Dependupon", style)
        ws.write(0, 4, "UsedBy count", style)
        ws.write(0, 5, "UsedBy", style)

        i = 0
        for path, package_info_list in self.depend_all.items():
            for package_info in package_info_list:
                pkg = package_info.packagename
                dependupon_count = package_info.dependon_count
                pkg_dependon_list = package_info.dependon_name_list
                pkg_dependon_list_str = ""
                for  pkg_dependon in pkg_dependon_list:
                    pkg_dependon_list_str += "  " + pkg_dependon + "  \n"
                
                usdBy_count = package_info.usedby_count
                pkg_usedBy_list = package_info.usedby_name_list
                pkg_usedBy_list_str = ""
                for pkg_usedby in pkg_usedBy_list:
                        pkg_usedBy_list_str += "  " + pkg_usedby + "  \n"

            
                ws.write(i + 1, 0, path)
                ws.write(i + 1, 1, pkg)
                ws.write(i + 1, 2, dependupon_count)
                ws.write(i + 1, 3, pkg_dependon_list_str)
                ws.write(i + 1, 4, usdBy_count)
                ws.write(i + 1, 5, pkg_usedBy_list_str)
                i += 1
        print "--------------create_sheet1 end---------------------"


    def print_xml_output(self, xml_filename):
        print "**********************Pkg Dependency XML File begin**************************"
        print "xml_filename =  " , xml_filename
        
        self.remove_if_exist(xml_filename)

        # self.build_xml_file(xmlfilepath)
        xmlFile = DependencyXMLFile(xml_filename)
        xmlFile.write_xmlFile_title()
        xmlFile.write_JDepend_element_head()
                    
        depend_text = ""
        for result_tmp in self.result_all:
            depend_text += self.get_pkg_dependency_for_xml_item(result_tmp)
        xmlFile.write_xmlFile_content(depend_text)
   
   
        xmlFile.write_JDepend_element_tail()
        print "************************Pkg Dependency XML File end*******************"
        
    def get_pkg_dependency_for_xml_item(self, dependency):
        depend_text = "\t<item>\n"
        depend_text += "\t\t<package>%s</package>\n" % (dependency.pkg_name)
        depend_text += "\t\t<dependOnPkg>%s</dependOnPkg>\n" % (dependency.dependon_name)
        depend_text += "\t</item>\n"
        return depend_text

    def remove_if_exist(self, filename):
        try:
            os.remove(filename)
        except OSError:
            print "this file",filename,"no exist"
            
    def get_pkgPath(self, package_name):
        global project_path
        pkg_path = None
        #1. check whether package_name is in analyse_path,analyse_path is src path
        for result_tmp in self.result_all:
            if package_name == result_tmp.pkg_name and result_tmp.dependon_name <> None:
                #if package_name is static lib, we skip this progress
                if self.is_static_lib(package_name, result_tmp.pkg_path):
                    print "%s is static lib, we use process 4 (traverse dir tree)" % package_name
                    break
                else:
                    pkg_path = result_tmp.pkg_path
                    return pkg_path
          
        #2.check whether package_name is already in pkg_to_pathAndGitname_all
        if self.pkg_to_pathAndGitname_all.has_key(package_name):
            path_and_gitname = self.pkg_to_pathAndGitname_all[package_name]
            pkg_path = path_and_gitname[0]
            return pkg_path
        
        #3.sub pkg, eg, com.android.internal.telephony is a sub pkg of com.android.internal
        #  com.android.internal.telephony 's path is same as com.android.internal
        for pkg_tmp in self.pkg_to_pathAndGitname_all.keys():
            if pkg_tmp in package_name:
                path_and_gitname =  self.pkg_to_pathAndGitname_all[pkg_tmp]
                pkg_path = path_and_gitname[0]
                return pkg_path

        #4.find package_name 's path by traverse android dir tree
        pkg_path = self.get_pkg_path_by_traverse_dir(package_name, "java/")
        if pkg_path == None:
            pkg_path = self.get_pkg_path_by_traverse_dir(package_name, "src/")

        return pkg_path

    def get_gitname(self, package_name):
        global project_path
        path_and_gitname = list()
        
        #step1.special process
        git_name = self.special_process_for_get_gitname(package_name)
        if git_name <> None:
            return git_name

        #step2. normal process
        pkg_path = self.get_pkgPath(package_name)
        print "pkg_path", pkg_path

        git_name = self.get_gitname_from_pkgPath(pkg_path)

        if pkg_path <> None and project_path in pkg_path:
            pkg_path = pkg_path[pkg_path.index(project_path)+len(project_path) : ]
        
        path_and_gitname.append(pkg_path)
        path_and_gitname.append(git_name)
        self.pkg_to_pathAndGitname_all[package_name] = path_and_gitname

        return git_name
    
    #prefix maybe java/ ,eg: java/java/io, maybe src/, eg src/com/sprd/appbackup/service/
    def get_pkg_path_by_traverse_dir(self, package_name, prefix):
        global product_name
        pkg_path =  None
        if "." in package_name:
            package_var = package_name.replace(".", "/")
        # traverse android dir tree
        #i = 0
        root_path = project_path
        for root, dirs, files in os.walk(root_path):
            if "out/target" in root:
                print "we skip out/target"
                continue
            #print "******package_name:%s******** i :%d" % (package_name, i)
            #i += 1
            #print "root:", root, "  dirs:", dirs, "  files:", files
            for dir_tmp in dirs:
                compelte_path = os.path.join(root, dir_tmp)

                #package_var_new = "java/" + package_var
                package_var_new = prefix + package_var
                if package_var_new in compelte_path:
                    print "package_var", package_var, "compelte_path", compelte_path
                    pkg_path = compelte_path[0: compelte_path.index(package_var) ]
                    #print "we find %s in pkg_path:%s" % (package_name, pkg_path)
                    return pkg_path
    
    def is_static_lib(self, package_name, package_path):
        global project_path
        android_mk_path = package_path + "/" + "Android.mk"
        
        if os.path.exists(android_mk_path):
            fp_amk = open(android_mk_path, "r")
            
            #traverse line of file to find whether package_name is STATIC_JAVA_LIBRARIES 
            while True:
                line_in_file = fp_amk.readline()
                if "LOCAL_STATIC_JAVA_LIBRARIES" in line_in_file:
                    if package_name in line_in_file:
                        return True
                    elif "\\" in line_in_file: #eg LOCAL_STATIC_JAVA_LIBRARIES := com.android.services.telephony.common \
                        
                        while True:
                            line_in_file = fp_amk.readline()
                            if package_name in fp_amk.readline():
                                return True
                            elif "\\" not in line_in_file:
                                break

                
        else:
            print "android_mk_path not exist",  android_mk_path
    
    
    def get_gitdepency_all(self):
        for  result_tmp in self.result_all:
            git_dependcy_list = list()
            reason = result_tmp.pkg_name + "-->" + result_tmp.dependon_name
            pkg_git_name = self.get_gitname(result_tmp.pkg_name)
            dependon_git_name = self.get_gitname(result_tmp.dependon_name)

            if pkg_git_name == None:
                pkg_git_name = "None"
            if dependon_git_name ==  None:
                dependon_git_name = "None"

            git_dependcy_list.append(pkg_git_name)
            git_dependcy_list.append(dependon_git_name)
            print "reason:", reason,  "git_dependcy_list:", git_dependcy_list
            self.git_dependcy_all.update({reason:git_dependcy_list})
            
    def get_gitname_from_pkgPath(self, pkg_path):
        global originalDir
        global project_path
        git_name = None

        if pkg_path == None:
            return git_name
        
        #correct pkg_path, prevent pkg_path is not complete path 
        if not os.path.exists(pkg_path):
            pkg_path = project_path + "/" + pkg_path

        #1.change dir and do git remote cmd
        os.chdir(pkg_path)
        print "we change dir to %s" % pkg_path
        #sleep(1000)
        pipe = subprocess.Popen('git remote -v', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        results_of_gitcmd = pipe.stdout.readlines()
        pipe.wait()
        
        os.chdir(originalDir)
        #2.get git_path
        for linetmp in results_of_gitcmd:
            print "linetmp: %s" % linetmp
            index1 = linetmp.index("android/")
            index2 = linetmp.index("(fetch)")
            length = len("android/")
            print "linetmp[index1+length:index2]: %s" % linetmp[index1+length:index2]
            if index1 > 0 and index2 > index1:
                git_name = linetmp[index1+length:index2].strip()
                return git_name
        
        return git_name
            
    # java.* javax.*,android.*
    # we know where it is,and if use normal progress,it takes much time 
    # therefore, we directly get package 's git name 
    def special_process_for_get_gitname(self, package_name):
        git_name = None
        
        # pkg_to_pathAndGitname_all has already package_name's path and gitname
        # get it derectly 
        if self.pkg_to_pathAndGitname_all.has_key(package_name):
            print "pkg_to_pathAndGitname_all has already package_name's path and gitname", package_name
            package_info = self.pkg_to_pathAndGitname_all[package_name]
            git_name = package_info[1]
            return git_name
        
        #java.*   javax.*
        if package_name.startswith("java.") or package_name.startswith("javax."):
            git_name = self.add_known_path_and_gitname(package_name, "libcore/luni/src/main/java", "platform/libcore")
            return git_name
        
        #android.*
        if package_name.startswith("android.") and self.statisfy_other_conditions_for_android_prefix(package_name):
            git_name = self.add_known_path_and_gitname(package_name, "frameworks/base", "platform/frameworks/base")
            return git_name
        
        #junit.framework
        if "junit.framework" in package_name:
            git_name = self.add_known_path_and_gitname(package_name, "external/junit/src", "platform/external/junit")
            return git_name

        #com.thundersoft.secure
        if "com.thundersoft.secure" in package_name:
            git_name = self.add_known_path_and_gitname(package_name, "frameworks/base/secure/core", "platform/frameworks/base")
            return git_name
        
        if "com.sprd.internal.telephony" in package_name:
            git_name = self.add_known_path_and_gitname(package_name, "frameworks/base/core/java", "platform/frameworks/base")
            return git_name

        if "org.ccil.cowan.tagsoup" in package_name:
            git_name = self.add_known_path_and_gitname(package_name, "external/tagsoup/src", "platform/external/tagsoup")
            return git_name

        return git_name
        
    def print_xls_output_git(self, xls_filename_git):
        print "--------------print_xls_output_git begin---------------------"
        #define Workbook    
        wb = xlwt.Workbook(encoding='utf-8')
        self.create_sheet1_git(wb)
        #self.create_sheet1(wb)
        #pkgs_in_path = self.create_sheet2(wb)
        #self.create_sheet3(wb,pkgs_in_path)
        wb.save(xls_filename_git)
        print "--------------print_xls_output_git end---------------------"      
    
    def print_xml_output_git(self, xml_filename_git):
        print "**********************print_xml_output_git begin**************************"
        print "xml_filename_git =  " , xml_filename_git
        
        self.remove_if_exist(xml_filename_git)

        # self.build_xml_file(xmlfilepath)
        xmlFile = DependencyXMLFile(xml_filename_git)
        xmlFile.write_xmlFile_title()
        xmlFile.write_module_element_head()
                    
        git_depend_text = ""
        for reason,git_dependcy_list in self.git_dependcy_all.items():
            git_depend_text += self.get_git_dependency_for_xml_item(git_dependcy_list)
        xmlFile.write_xmlFile_content(git_depend_text)
   
   
        xmlFile.write_module_element_tail()
        print "************************print_xml_output_git end*******************"
    
    def create_sheet1_git(self, wb):
        print "--------------create_sheet1_git begin---------------------"
        font = xlwt.Font() # Create the Font
        font.name = 'Times New Roman'
        font.bold = True
        font.italic = True
        style = xlwt.XFStyle() # Create the Style
        style.font = font # Apply the Font to the Style
        
        ws = wb.add_sheet('Sheet1-reason-gitdependcy')
        
        ws.col(0).width = 13000
        ws.col(1).width = 13000
        ws.col(2).width = 13000
        ws.write(0, 0, "Reason", style)
        ws.write(0, 1, "PackageGitName", style)
        ws.write(0, 2, "DependOnPackageGitName", style)

        i = 0
        for reason, gitdependcy_list in self.git_dependcy_all.items():
            pkg_gitname = gitdependcy_list[0]
            dependon_gitname = gitdependcy_list[1]
            ws.write(i + 1, 0, reason)
            ws.write(i + 1, 1, pkg_gitname)
            ws.write(i + 1, 2, dependon_gitname)
            i += 1
        print "--------------create_sheet1_git end---------------------"
        
    def get_git_dependency_for_xml_item(self, git_dependcy_list):
        gitname = git_dependcy_list[0]
        dependon_gitname = git_dependcy_list[1]
        git_depend_text = "\t<item>\n"
        git_depend_text += "\t\t<gitname>%s</gitname>\n" % (gitname)
        git_depend_text += "\t\t<dependon_gitname>%s</dependon_gitname>\n" % (dependon_gitname)
        git_depend_text += "\t</item>\n"
        return git_depend_text
    
    def statisfy_other_conditions_for_android_prefix(self, package_name):
        return True
    
    def add_known_path_and_gitname(self, package_name, pkg_path_known, pkg_gitname_known):
        global project_path
        path_and_gitname = list()
        print "find known pkg-path-gitname---,pkg name is:", package_name
        
        pkg_path = os.path.join(project_path, pkg_path_known)
        git_name = pkg_gitname_known
        
        path_and_gitname.append(pkg_path)
        path_and_gitname.append(git_name)
        self.pkg_to_pathAndGitname_all[package_name] = path_and_gitname
        
        return git_name
    
    
class DependencyXMLFile:
    def __init__(self, xml_filename):
        self.xml_filename = xml_filename
    
    def write_xmlFile_content_head(self):
        self.append_content_2_file(self.xml_filename, self.get_xmlFile_content_head())
        
    def write_xmlFile_content(self, content):
        self.append_content_2_file(self.xml_filename, content)
        
    def write_xmlFile_content_tail(self):
        self.append_content_2_file(self.xml_filename, self.get_xmlFile_content_tail())
        
    def write_JDepend_element_head(self):
        JDepend_element_head = "<module name=" + '"JDepend' + '">\n'
        self.append_content_2_file(self.xml_filename, JDepend_element_head)
        
    def write_JDepend_element_tail(self):
        JDepend_element_tail = "</module>\n"
        self.append_content_2_file(self.xml_filename, JDepend_element_tail)

    def write_module_element_head(self):
        module_element_head = "<module name=" + '"GitDependcy' + '">\n'
        self.append_content_2_file(self.xml_filename, module_element_head)
        
    def write_module_element_tail(self):
        module_element_tail = "</module>\n"
        self.append_content_2_file(self.xml_filename, module_element_tail)
        
    # inner usage
    def write_xmlFile_title(self):
        self.append_content_2_file(self.xml_filename, self.get_xmlFile_title())

    # inner usage    
    def get_xmlFile_title(self):
        # title = "<?xml version=" + '"' + "1.0" + '"' + " encoding=" + '"' + "UTF-8" + '"?>\n'
        title = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
        print "title = %s" % (title)
        return title

    
    # inner usage    
    def get_xmlFile_content_tail(self):
        tail = "</module>\n"
        print "tail = %s" % (tail)
        return tail
    
     # inner usage
    def append_content_2_file(self, fileName, content):
        try:
            f = codecs.open(fileName, 'a', 'utf-8')
            f.write(content)
        except:
            print "error or exception occurred."
        finally:
            f.close()           


# define log class, to output all logs to file(myapp.log)
class log_helper:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename='myapp.log',
                        filemode='w')

class XMLParse:
    def __init__(self, result_manager):
        self.result_manager = result_manager
        
    def parse_pkgdepend_config_xml(self, xmlfilename):
        global project_path
        global product_name
        print "------parsing pkgdepend_config.xml ----------------------------begin:", xmlfilename
        
        #fullPath = path + "api_module_config.xml"
        tree = ElementTree.parse(xmlfilename)
        root = tree.getroot()
        print "root.tag:",root.tag
        compounds = root.findall("module")
        module_itemslist_pair_all = dict()
        for child in compounds:
            analyse_pathInfos = list()
            #logging.debug("parsing api_module_config.xml child.tag = %s" %child.tag)
            if child.tag == "module":
                if child.attrib.has_key("name") > 0:
                    module_name = child.attrib['name']     
                    subchild = child.getchildren()
                    #item elements
                    for item in subchild:
                        if item.attrib.has_key("srcpath"):
                            src_path = item.attrib["srcpath"]
                        #print " pkg_path" ,pkg_path
                        
                        product_path_element_all = item.findall("product_path")
                        if product_path_element_all <>None:
                            for product_path_element in product_path_element_all:
                                src_path = project_path + "/" + src_path
                                print "src_path" ,src_path
                                print "product_path_element.text:", product_path_element.text
                                product_path = "out/target/product/" + product_name + "/" + product_path_element.text
                                analyse_path_info = AnalysePathInfo(src_path, product_path)
                                analyse_pathInfos.append(analyse_path_info)
                        else:
                            print "item have no product_path_element"

                    module_itemslist_pair_all[module_name] = analyse_pathInfos
        print "-----parsing pkgdepend_config.xml  -----------------------------------end"
        return module_itemslist_pair_all
        
    
    def parse_JDepend_xml_result(self, path_info):

        analyse_path = path_info.src_path
        JDepend_xml_result_file = "report.xml"
        print "os.getcwd():",os.getcwd()
        
        tree = ElementTree.parse(JDepend_xml_result_file)
        root = tree.getroot()
        print "root.tag",root.tag,"---------root.attrib",root.attrib
        #sleep(1000)
        for pkgs in root.findall("Packages"):#mostly,there is only one Packages element
            for pkg in pkgs.findall("Package"):
                pkg_name = pkg.attrib["name"]
                print "pkg_name:",pkg_name,"   analyse_path:",analyse_path
                #self.result_manager.add_pkg_path_pair(pkg_name,analyse_path)
                dependon_name_list = self.parse_dependsUpon_element(analyse_path,pkg,pkg_name)
                dependon_count = len(dependon_name_list)
                
                usedby_name_list = self.parse_UsedBy_element(analyse_path,pkg,pkg_name)
                usedby_count = len(usedby_name_list)
                
                self.result_manager.add_package_info(analyse_path, pkg_name, dependon_name_list, dependon_count, usedby_name_list, usedby_count)

                  
    def parse_dependsUpon_element(self, analyse_path, pkg, pkg_name):
        pkgDependsUpon = pkg.find("DependsUpon")
        dependon_name_list = list()
        if pkgDependsUpon <> None:       
            for dependon in pkgDependsUpon.findall("Package"):
                dependon_name = dependon.text
                dependon_name_list.append(dependon_name)
                print "pkg_name:",pkg_name,"   dependon_name:",dependon_name    
                self.result_manager.add_result(analyse_path,pkg_name,dependon_name)             
        else:                
        #for key, values in self.result_manager.depend_all.items():
        #    for item in values:
        #        print key,item.packagename, item.dependon_name_list
            print "this packge:",pkg_name,"has no DependsUpon element"
        return dependon_name_list
            
    def parse_UsedBy_element(self, analyse_path, pkg, pkg_name):
        pkgUsedBy = pkg.find("UsedBy")
        usdBy_name_list = list()
        if pkgUsedBy <> None:
            for usedBy in pkgUsedBy.findall("Package"):
                usdBy_name = usedBy.text
                usdBy_name_list.append(usdBy_name)
                print "pkg_name:",pkg_name,"   usdBy_name:",usdBy_name
                self.result_manager.add_result(analyse_path, usdBy_name, pkg_name)
        else:
            #self.result_manager.add_result(analyse_path, usdBy_name, pkg_name)
            print "this packge:",pkg_name,"has no UsedBy element"
        return usdBy_name_list


if __name__ == '__main__':

    sys.setrecursionlimit(1000000)  # ������������Ϊһ����
    analyse_path = None  
    xls_filename = None
    xml_filename = None
    xls_filename_git = None
    xml_filename_git = None
    project_path = None
    product_name = None
    #project_path = "/home/user/workspace/sprdroid6.0_trunk/"

    originalDir = os.getcwd() # this var is used to change back to python dir
    if len (sys.argv) > 2:
        cmd = -1  # ready to accept cmd
        for option in (sys.argv[1:]):
            if cmd == -1:
                if option == "-p":  # the android root path which will be analysed by JDepend 
                    cmd = 1
                elif option == "-xls":
                    cmd = 2
                elif option == "-xml":
                    cmd = 3
                elif option == "-gxls":
                    cmd = 4
                elif option == "-gxml":
                    cmd = 5
                elif option == "-pn":#product name ,eg,sp7731g_1h10
                    cmd = 6
            else:
                if cmd == 1:
                    project_path = option
                elif cmd == 2:
                    xls_filename = option
                elif cmd == 3:
                    xml_filename = option
                elif cmd == 4:
                    xls_filename_git = option
                elif cmd == 5:
                    xml_filename_git = option
                elif cmd == 6:
                    product_name = option
                # ready for next cmd
                cmd = -1
         
    if project_path == None:
        print "the android root path which will be analysed by JDepend is none! Tell us the android root path"
        exit(-1)

    
    log = log_helper();
    result_manager = ResultManager()
    xmlParse = XMLParse(result_manager)
    pkgDepOps = PkgDependencyOperation()
   
    pkgdepend_config_xml = "pkgdepend_config.xml"
    module_pathInfolist_pair_all = xmlParse.parse_pkgdepend_config_xml(pkgdepend_config_xml)
    #for module,analyse_pathInfos in module_pathInfolist_pair_all.items():
    #    for path_info in analyse_pathInfos:
    #           print "module:", module, "    src_path:", path_info.src_path, "    product_path:", path_info.product_path

    for module,analyse_pathInfos in module_pathInfolist_pair_all.items():
 
        for path_info in analyse_pathInfos:
            print "module:", module, "    src_path:", path_info.src_path, "    product_path:", path_info.product_path
            product_full_path = project_path + path_info.product_path
            
            #use dex2jar tool ,make dex in android to regular jar 
            pkgDepOps.dex2jar(product_full_path)
            jar_path = pkgDepOps.get_jar_path(product_full_path)

            pkgDepOps.do_JDepend_Cmd(jar_path)                   

            xmlParse.parse_JDepend_xml_result(path_info)
     
    #sleep(1000)
    #output package dependcy to xls or xml file
    if xls_filename <>None:
        result_manager.print_xls_output(xls_filename)

    if xml_filename <>None:
        result_manager.print_xml_output(xml_filename)

    result_manager.get_gitdepency_all()
    print "we come to output git dependcy"
    if xls_filename_git <> None:
        result_manager.print_xls_output_git(xls_filename_git)
        
    if xml_filename_git <> None:
        result_manager.print_xml_output_git(xml_filename_git)    
    


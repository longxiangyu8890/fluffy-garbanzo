#!/usr/bin/env python
#coding=utf-8
import codecs
import logging
from xml.etree import ElementTree 
import sys
import os
from pty import CHILD
from time import sleep
import xlwt


#define log class, to output all logs to file(myapp.log)
class log_helper:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename='../../../../myapp.log',
                        filemode='w')

class Parser:
    def __init__(self, rootPath):
        self.rootPath = rootPath

#<item>
#<binary>applypatch</binary>
#<dependOn>libc.so</dependOn>
#</item>
    def parse_xml(self, pkgDependXMLFile):
        logging.debug("----------------------------parsing pkg_dependcy xml begin---------------------------")
        print "parsing xml begin"
        
        filename = "pkgdependcy.xml"

        fullpathfilename = self.rootPath + filename
        print "[parse_xml------fullpathfilename]: %s" %(fullpathfilename)
        print  os.path.exists(fullpathfilename)
        print "-------------------------------------"
        #sleep(1000)
        tree = ElementTree.parse(fullpathfilename)
        root = tree.getroot()
        print "root.tag:",root.tag
        for item_tmp in root.findall("item"):
            pkg_name = item_tmp.find("package").text
            dependon_pkg = item_tmp.find("dependOnPkg").text
            pkg_depend_pair = pkg_name + "->" + dependon_pkg
            pkgDependXMLFile.pkgdependlist.add(pkg_depend_pair)
        
        #print libDependXMLFile.libdependlist
        #for result in pkgDependXMLFile.pkgdependlist:
        #    print "[parse_xml------result]: %s" %(result)                         
        logging.debug("parsing xml end")
        print "----------------------------------parsing pkg_dependcy xml end----------------------------------"

    def parse_dependsUpon_element(self,pkg,pkg_name,pkgDependXMLFile):
        pkgDependsUpon = pkg.find("DependsUpon")
        if pkgDependsUpon <> None:
            for dependon in pkgDependsUpon.findall("Package"):
                dependon_name = dependon.text
                pkg_dependonPkg_pair = pkg_name + "-->" + dependon_name
                print "pkg_dependonPkg_pair:",pkg_dependonPkg_pair 
                pkgDependXMLFile.pkgdependlist.add(pkg_dependonPkg_pair)                      
        else:
            print "this packge:",pkg_name,"has no DependsUpon element"

    def parse_UsedBy_element(self,pkg,pkg_name,pkgDependXMLFile):
        pkgUsedBy = pkg.find("UsedBy")
        if pkgUsedBy <> None:
            for usedBy in pkgUsedBy.findall("Package"):
                usdBy_name = usedBy.text
                usedByPkg_pkg_pair = usdBy_name + "-->" + pkg_name
                print "usedByPkg_pkg_pair:",usedByPkg_pkg_pair
                pkgDependXMLFile.pkgdependlist.add(usedByPkg_pkg_pair)
        else:
            print "this packge:",pkg_name,"has no UsedBy element"

        
    
class Change:
    def __init__(self, lines, changetype, who):
        self.lines = lines              #type: Owner
        self.changetype = changetype
        self.who = who

class ChangeManager:
    def __init__(self):
        #list can do sort storage and output
        self.changes_all = list()
        
    def print_xls_output(self):
        xls_path = "compare_result_report.xls"
        wb = xlwt.Workbook(encoding='utf-8')
        self.create_sheet1(wb)
        wb.save(xls_path)


    def create_sheet1(self,wb):
        print "--------------create_sheet1 begin---------------------"
        font = xlwt.Font() # Create the Font
        font.name = 'Times New Roman'
        font.bold = True
        font.italic = True
        style = xlwt.XFStyle() # Create the Style
        style.font = font # Apply the Font to the Style
        
        ws = wb.add_sheet('Sheet1')
        
        ws.col(0).width = 5000
        ws.col(1).width = 6666
        ws.col(2).width = 13000

        ws.write(0, 0, "Num", style)
        ws.write(0, 1, "Change Tpye", style)
        ws.write(0, 2, "Change what", style)

        i = 0
        for change in self.changes_all:
            ws.write(i + 1, 0, change.lines, style)
            ws.write(i + 1, 1, change.changetype, style)
            ws.write(i + 1, 2, change.who, style)
            i += 1

    def add_change(self, lines, changetype, who):
        #self.changes_all.add(change)
        change = Change(lines, changetype, who)
        self.changes_all.append(change)
     

    def remove_if_exist(self, filename):
        try:
            os.remove(filename)
        except OSError:
            pass


class PkgDependXMLFile:
    def __init__(self, change_manager):
        self.change_manager = change_manager
        self.pkgdependlist= set()
    
    def compare(self, other):
        old = self.pkgdependlist
        new = other.pkgdependlist
        
        #print "[memberdef_define] %s comapring" %self.whose
        lines  = 0
        for item in old:
            if not item in new:
                lines = lines + 1
                self.change_manager.add_change(str(lines), "REMOVED_DEPEND", item)
            
        for item in new:
            if not item in old:
                print "[compare------item]: %s" %(item)
                lines = lines + 1
                self.change_manager.add_change(str(lines), "ADDED_DEPEND", item)

    
if __name__ == '__main__':
    if len (sys.argv) >= 2:
        cmd = -1  # ready to accept cmd
        for option in (sys.argv[1:]):
            if cmd == -1:
                cmd = 1
            else:
                if cmd == 1:
                    pass

    location_old = "../../../../xmldepend/old/"
    location_new = "../../../../xmldepend/new/"
    
    change_manager = ChangeManager()
    pkgDependXMLFile_old = PkgDependXMLFile(change_manager)
    pkgDependXMLFile_new = PkgDependXMLFile(change_manager)
    log = log_helper();

    #two files needed to compare 
    #parse old xml file.
    print "Begin to parse file xmldepend/old/pkgdependcy.xml"
    Parser(location_old).parse_xml(pkgDependXMLFile_old)
    #sleep(1000)
    #parse new xml file.
    print "Begin to parse file xmldepend/new/pkgdependcy.xm"
    Parser(location_new).parse_xml(pkgDependXMLFile_new)
    
    #compare two xml contents.
    pkgDependXMLFile_old.compare(pkgDependXMLFile_new)

    change_manager.print_xls_output()
    
    
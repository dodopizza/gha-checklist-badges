#!/usr/bin/env python3.8
import typing
import re
import os
import argparse
import urllib.parse

class Checklist:  

    def __init__(self, fname: str):
        self.fname = fname
        self.content = self.get_file_content()

    def get_name(self) -> str:
        return Checklist.get_name_from_fname(self.fname)

    def get_file_content(self) -> str:
        with open(self.fname, 'r') as f: 
            return f.read()

    def get_counters(self) -> (int, int, int):
        return Checklist.get_counters_from_content(self.content)

    @staticmethod
    def get_counters_from_content(content: str) -> (int, int, int):
        regex = r"- \[([ x])\] "
        matches = re.finditer(regex, content, re.MULTILINE)

        checked=int(0)
        unchecked=int(0)
        for _, match in enumerate(matches, start=1):
            if match.group(1) == 'x':
                checked+=1
                continue
            if match.group(1) == ' ':
                unchecked+=1
                continue

        return checked, unchecked, (checked + unchecked)
    
    @staticmethod
    def get_name_from_fname(fname: str) -> str:
        bn = os.path.basename(fname)
        return os.path.splitext(bn)[0]



class Badge:

    @staticmethod
    def new_common_badge_url(badge_name: str, badge_value: str, badge_color: str):
        return (
            "https://img.shields.io/badge/%s-%s-%s" % ( 
                urllib.parse.quote(badge_name.replace('-', '--'), safe=''), 
                urllib.parse.quote(badge_value, safe=''), 
                badge_color 
            )
        )

    @staticmethod
    def new_progress_badge_url(badge_name: str, total: int, passed: int ) -> str:
        progress = int(passed/total*100)
        color = "green" if (progress>=70) else "yellow" if (progress>=30) else "red"
        return Badge.new_common_badge_url(
            badge_name=badge_name,
            badge_value="%d%% %d/%d" % (
                progress,
                passed,
                total
            ),
            badge_color=color
        )

    @staticmethod
    def content_update_badge_url(content: str, badge_name: str, new_badge_url: str):
        regex = r"(\!\[%s\])\((.*?)\)" % badge_name
        subst = "\\1(%s)" % new_badge_url
        result = re.sub(regex, subst, content, 0, re.MULTILINE)
        finded = re.findall(regex, content, re.MULTILINE)
        if len(finded) > 0:
            return result
        else:
            return "![%s](%s) " % (badge_name, new_badge_url) + content


class ReadmeMD:

    def __init__(self, fname: str):
        self.fname = fname
        self.content = self.get_content()

    def get_content(self) -> str:
        return ReadmeMD.get_file_content(self.fname)

    def write_content(self, content: str):
        ReadmeMD.write_file_content(self.fname, content)

    @staticmethod
    def get_file_content(fname: str) -> str:
        with open(fname, 'r') as f: 
            return f.read()

    @staticmethod
    def write_file_content(fname, content: str):
        with open(fname, 'w') as f: 
            f.write(content)


def get_cli_args():
    parser = argparse.ArgumentParser(description='NFR')
    parser.add_argument('fnames', type=str, nargs='+', help='Checklist files')
    args = parser.parse_args()
    return args.fnames

def main():
    fnames = get_cli_args()
    readme = ReadmeMD('README.md')
    for fname in fnames:
        checklist = Checklist(fname)
        mdname = checklist.get_name()
        checked, _, total = checklist.get_counters()
        readme.write_content(
            content=Badge.content_update_badge_url(
                content=readme.content,
                badge_name=mdname,
                new_badge_url=Badge.new_progress_badge_url(
                    badge_name=mdname,
                    total=total,
                    passed=checked,
                )
            )
        )

if __name__== "__main__":
  main()

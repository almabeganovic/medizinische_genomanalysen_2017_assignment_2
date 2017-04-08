#! /usr/bin/env python3

import vcf

__author__ = 'Alma Beganovic'


class Assignment2:
    def __init__(self):
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)
        ### Open file and store file content in vcf variable
        self.vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24385.vcf", "r"))


    ## Sum of self.summ is calculated, and the number of self.summ is stored in count. Average = self.summ of all record.QUAL  / Number of all record.QUAL
    def get_average_quality_of_son(self):
        self.summ = 0
        self.count = 0
        for record in self.vcf:
            self.summ = self.summ + record.QUAL
            self.count +=1
        print("-average_quality_of_son")
        print(float(self.summ) / (self.count))


    ## Number of all record in self.vcf
    def get_total_number_of_variants_of_son(self):
        for record in self.vcf:
            self.count +=1
        print("-total nuber of variants of son:")
        print(self.count)


    ## This func search in header_lines of VCF Files  for line which bein with string "##source"
    ## Founded line will be split with character "/" and the first position will be printed out
    def get_variant_caller_of_vcf(self):
        for line in self.vcf._header_lines:
             if line.startswith("##source"):
                 print("-variant_caller_of_vcf")
                 print("-",str.split(line,'"')[1])

    ## This func search in header_lines of VCF Files  for line which bein with string "##reference=file://"
    ## Founded line will be split with character "/" and the sixth position will be printed out
    def get_human_reference_version(self):
        for line in self.vcf._header_lines:
             if line.startswith("##reference=file://"):
                 print("-human_reference_version")
                 print(str.split(line,'/')[6])

    ## This func count indels in VCF Files and the number of indels will be printed out
    def get_number_of_indels(self):
        self.vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24385.vcf", "r"))
        self.indels = 0
        for record in self.vcf:
            if record.is_indel:
                self.indels +=1
        print("-number_of_indels")
        print(self.indels)

    ## This func search for snp in VCF Files and if snp is true, then will be number of all snv with "True" Value printed out
    def get_number_of_snvs(self):
        self.vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24385.vcf", "r"))
        self.snv = 0
        for record in self.vcf:
            if record.is_snp:
              self.snv += 1
        print("-number_of_snv")
        print(self.snv)

    ## Print out summ of all num_het in VCF File
    def get_number_of_heterozygous_variants(self):
        self.vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24385.vcf", "r"))
        self.num_hets = 0
        for record in self.vcf:
            self.num_hets += record.num_het
        print("-number_of_hets")
        print(self.num_hets)


    def print_summary(self):

        print("All results:")

        self.get_average_quality_of_son();             # 1753.7782222395415
        self.get_total_number_of_variants_of_son();    # 38526
        self.get_variant_caller_of_vcf();              # tvc 4.5-1+0 (8ffe53a) - Torrent Variant Caller
        self.get_human_reference_version();            # hg19
        self.get_number_of_indels();                   # 1823
        self.get_number_of_snvs();                     # 36703
        self.get_number_of_heterozygous_variants();    # 23819


if __name__ == '__main__':
    print("Assignment 2")
    assignment1 = Assignment2()
    assignment1.print_summary()

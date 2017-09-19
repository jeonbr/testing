test_dic = {
    "app_revision": "e29dc02fe07039b69612a2895aee94507fe97563",
    "genome_assembly": {
        "fruitfly": "dm3",
        "human": "hg38",
        "rat": "rn4",
        "zebrafish": "zv9",
        "mouse": "mm10",
        "frog": "xenTro3",
        "pig": "susScr2",
        "nematode": "ce10"
    },
    "timestamp": "2017-09-05T13:29:37.765000",
    "src_version": {
        "pharmgkb": "20170905",
        "uniprot": "20170831",
        "umls": "20170508",
        "entrez": "20170902",
        "exac": "20160810",
        "ensembl": 90,
        "ucsc": "20170903",
        "refseq": "68",
        "netaffy": "na35",
        "cpdb": 32
    },
    "source": "genedoc_mygene_allspecies_20170905_simxuxc6",
    "available_fields": "http://mygene.info/metadata/fields",
    "stats": {
        "total_species": 21158,
        "total_ensembl_genes_mapped_to_entrez": 679091,
        "total_ensembl_only_genes": 997362,
        "total_entrez_genes": 18976826,
        "total_genes": 19974188,
        "total_ensembl_genes": 1676453
    },
    "taxonomy": {
        "fruitfly": 7227,
        "human": 9606,
        "rat": 10116,
        "zebrafish": 7955,
        "mouse": 10090,
        "frog": 8364,
        "pig": 9823,
        "thale-cress": 3702,
        "nematode": 6239
    }
}

myvariant_dic = {
    "_id": "chr1:g.35367G>A",
    "_version": 1,
    "cadd": {
        "_license": "http://goo.gl/bkpNhq",
        "alt": "A",
        "annotype": "NonCodingTranscript",
        "bstatistic": 994,
        "chmm": {
            "bivflnk": 0,
            "enh": 0,
            "enhbiv": 0,
            "het": 0,
            "quies": 1,
            "reprpc": 0,
            "reprpcwk": 0,
            "tssa": 0,
            "tssaflnk": 0,
            "tssbiv": 0,
            "tx": 0,
            "txflnk": 0,
            "txwk": 0,
            "znfrpts": 0
        },
        "chrom": 1,
        "consdetail": "non_coding_exon,nc",
        "consequence": "NONCODING_CHANGE",
        "consscore": 5,
        "cpg": 0.03,
        "dna": {
            "helt": -2.04,
            "mgw": 0.01,
            "prot": 1.54,
            "roll": -0.63
        },
        "encode": {
            "exp": 31.46,
            "h3k27ac": 23.44,
            "h3k4me1": 23.8,
            "h3k4me3": 8.6
        },
        "exon": "2/3",
        "fitcons": 0.577621,
        "gc": 0.48,
        "gene": {
            "cds": {
                "cdna_pos": 476,
                "rel_cdna_pos": 0.4
            },
            "feature_id": "ENST00000417324",
            "gene_id": "ENSG00000237613",
            "genename": "FAM138A"
        },
        "gerp": {
            "n": 1.29,
            "s": -0.558
        },
        "isknownvariant": "FALSE",
        "istv": "FALSE",
        "length": 0,
        "mapability": {
            "20bp": 0,
            "35bp": 0
        },
        "min_dist_tse": 122,
        "min_dist_tss": 707,
        "mutindex": 70,
        "phast_cons": {
            "mammalian": 0.003,
            "primate": 0.013,
            "vertebrate": 0.003
        },
        "phred": 3.726,
        "phylop": {
            "mammalian": -0.155,
            "primate": 0.151,
            "vertebrate": -0.128
        },
        "pos": 35367,
        "rawscore": 0.111068,
        "ref": "G",
        "scoresegdup": 0.99,
        "segway": "D",
        "type": "SNV"
    },
    "chrom": "1",
    "hg19": {
        "end": 35367,
        "start": 35367
    },
    "snpeff": {
        "_license": "http://snpeff.sourceforge.net/download.html",
        "ann": [
            {
                "distance_to_feature": "4864",
                "effect": "downstream_gene_variant",
                "feature_id": "NR_036051.1",
                "feature_type": "transcript",
                "gene_id": "MIR1302-2",
                "genename": "MIR1302-2",
                "hgvs_c": "n.*4864G>A",
                "putative_impact": "MODIFIER",
                "transcript_biotype": "pseudogene"
            },
            {
                "distance_to_feature": "4864",
                "effect": "downstream_gene_variant",
                "feature_id": "NR_036266.1",
                "feature_type": "transcript",
                "gene_id": "MIR1302-9",
                "genename": "MIR1302-9",
                "hgvs_c": "n.*4864G>A",
                "putative_impact": "MODIFIER",
                "transcript_biotype": "pseudogene"
            },
            {
                "distance_to_feature": "4864",
                "effect": "downstream_gene_variant",
                "feature_id": "NR_036267.1",
                "feature_type": "transcript",
                "gene_id": "MIR1302-10",
                "genename": "MIR1302-10",
                "hgvs_c": "n.*4864G>A",
                "putative_impact": "MODIFIER",
                "transcript_biotype": "pseudogene"
            },
            {
                "distance_to_feature": "4864",
                "effect": "downstream_gene_variant",
                "feature_id": "NR_036268.1",
                "feature_type": "transcript",
                "gene_id": "MIR1302-11",
                "genename": "MIR1302-11",
                "hgvs_c": "n.*4864G>A",
                "putative_impact": "MODIFIER",
                "transcript_biotype": "pseudogene"
            },
            {
                "effect": "non_coding_transcript_exon_variant",
                "feature_id": "NR_026818.1",
                "feature_type": "transcript",
                "gene_id": "FAM138A",
                "genename": "FAM138A",
                "hgvs_c": "n.476C>T",
                "putative_impact": "MODIFIER",
                "rank": "2",
                "total": "3",
                "transcript_biotype": "pseudogene"
            },
            {
                "effect": "non_coding_transcript_exon_variant",
                "feature_id": "NR_026820.1",
                "feature_type": "transcript",
                "gene_id": "FAM138F",
                "genename": "FAM138F",
                "hgvs_c": "n.476C>T",
                "putative_impact": "MODIFIER",
                "rank": "2",
                "total": "3",
                "transcript_biotype": "pseudogene"
            }
        ]
    },
    "vcf": {
        "alt": "A",
        "position": "35367",
        "ref": "G"
    }
}


def get_object(obj):
    if isinstance(obj, dict):
        result = {}
        for k, v in obj.items():
            if isinstance(v, dict):
                result[k] = get_object(v)
            elif isinstance(v, list):
                sub_result = []
                for i in v:
                    sub_result.append(get_object(i))
                result[k] = sub_result
            elif isinstance(v, int):
                result[k] = "Int"
            elif isinstance(v, str):
                result[k] = "Str"
            elif isinstance(v, float):
                result[k] = "Float"
        return result
    elif isinstance(obj, list):
        result = []
        for i in obj:
            result.append(get_object(i))
        return result
    elif isinstance(obj, int):
        return "Int"
    elif isinstance(obj, str):
        return "Str"
    elif isinstance(obj, float):
        return "Float"


def list_dedup(obj):
    if isinstance(obj, dict):
        result = {}
        for k, v in obj.items():
            if isinstance(v, dict):
                result[k] = list_dedup(v)
            elif isinstance(v, list):
                if v:
                    result[k] = v[:1]
                else:
                    result[k] = []
            else:
                result[k] = v
        return result
    elif isinstance(obj, list):
        if obj:
            return obj[:1]
        else:
            return []
    else:
        return obj


object_map_dedup = list_dedup(get_object(myvariant_dic))
# object_map = get_object(test_dic)
print(object_map_dedup)
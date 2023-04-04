%Commercial Use
can_use_commercially("BSD Zero Clause License").
can_use_commercially("Academic Free License v3.0").
can_use_commercially("GNU Affero General Public License v3.0").
can_use_commercially("Apache License 2.0").
can_use_commercially("Artistic License 2.0").
can_use_commercially("BSD 2-Clause \"Simplified\" License").
can_use_commercially("BSD 3-Clause Clear License").
can_use_commercially("BSD 3-Clause \"New\" or \"Revised\" License").
can_use_commercially("BSD 4-Clause \"Original\" or \"Old\" License").
can_use_commercially("Boost Software License 1.0").
can_use_commercially("Creative Commons Attribution 4.0 International").
can_use_commercially("Creative Commons Attribution Share Alike 4.0 International").
can_use_commercially("Creative Commons Zero v1.0 Universal").
can_use_commercially("CeCILL Free Software License Agreement v2.1").
can_use_commercially("CERN Open Hardware License Version 2 - Permissive").
can_use_commercially("CERN Open Hardware License Version 2 - Strongly Reciprocal").
can_use_commercially("CERN Open Hardware License Version 2 - Weakly Reciprocal").
can_use_commercially("Educational Community License v2.0").
can_use_commercially("Eclipse Public License 1.0").
can_use_commercially("Eclipse Public License 2.0").
can_use_commercially("European Union Public License 1.1").
can_use_commercially("European Union Public License 1.2").
can_use_commercially("GNU Free Documentation License v1.3").
can_use_commercially("GNU General Public License v2.0").
can_use_commercially("GNU General Public License v3.0").
can_use_commercially("ISC License").
can_use_commercially("GNU Lesser General Public License v2.1").
can_use_commercially("GNU Lesser General Public License v3.0").
can_use_commercially("LaTeX Project Public License v1.3c").
can_use_commercially("MIT No Attribution").
can_use_commercially("MIT License").
can_use_commercially("Mozilla Public License 2.0").
can_use_commercially("Microsoft Public License").
can_use_commercially("Microsoft Reciprocal License").
can_use_commercially("Mulan Permissive Software License, Version 2").
can_use_commercially("University of Illinois-NCSA Open Source License").
can_use_commercially("Open Data Commons Open Database License v1.0").
can_use_commercially("SIL Open Font License 1.1").
can_use_commercially("Open Software License 3.0").
can_use_commercially("PostgreSQL License").
can_use_commercially("The Unlicense").
can_use_commercially("Universal Permissive License v1.0").
can_use_commercially("Vim License").
can_use_commercially("Do What The F*ck You Want To Public License").
can_use_commercially("zlib License").

%Distribution
can_distribute("BSD Zero Clause License").
can_distribute("Academic Free License v3.0") :- condition(copyright_license_with_source_code).
can_distribute("GNU Affero General Public License v3.0") :- condition(disclose_source_code), condition(copyright_license_with_source_code), condition(copyright_license_with_binaries), condition(network_use_is_distribution).
can_distribute("Apache License 2.0") :- condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("Artistic License 2.0") :- condition(copyright_license_with_source_code),condition(copyright_license_with_binaries).
can_distribute("BSD 2-Clause \"Simplified\" License") :- condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("BSD 3-Clause Clear License") :- condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("BSD 3-Clause \"New\" or \"Revised\" License") :- condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("BSD 4-Clause \"Original\" or \"Old\" License") :- condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("Boost Software License 1.0") :- condition(copyright_license_with_source_code).
can_distribute("Creative Commons Attribution 4.0 International") :- condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("Creative Commons Attribution Share Alike 4.0 International") :- condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("Creative Commons Zero v1.0 Universal").
can_distribute("CeCILL Free Software License Agreement v2.1") :- condition(disclose_source_code), condition(copyright_license_with_source_code), condition(copyright_license_with_binaries), condition(network_use_is_distribution).
can_distribute("CERN Open Hardware License Version 2 - Permissive") :- condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("CERN Open Hardware License Version 2 - Strongly Reciprocal") :- condition(disclose_source_code), condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("CERN Open Hardware License Version 2 - Weakly Reciprocal") :- condition(disclose_source_code), condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("Educational Community License v2.0") :- condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("Eclipse Public License 1.0") :- condition(disclose_source_code), condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("Eclipse Public License 2.0") :- condition(disclose_source_code), condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("European Union Public License 1.1") :- condition(disclose_source_code), condition(copyright_license_with_source_code), condition(copyright_license_with_binaries), condition(network_use_is_distribution).
can_distribute("European Union Public License 1.2") :- condition(disclose_source_code), condition(copyright_license_with_source_code), condition(copyright_license_with_binaries), condition(network_use_is_distribution).
can_distribute("GNU Free Documentation License v1.3") :- condition(disclose_source_code), condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("GNU General Public License v2.0") :- condition(disclose_source_code), condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("GNU General Public License v3.0") :- condition(disclose_source_code), condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("ISC License") :- condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("GNU Lesser General Public License v2.1") :- condition(disclose_source_code), condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("GNU Lesser General Public License v3.0") :- condition(disclose_source_code), condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("LaTeX Project Public License v1.3c") :- condition(disclose_source_code), condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("MIT No Attribution").
can_distribute("MIT License") :- condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("Mozilla Public License 2.0") :- condition(disclose_source_code), condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("Microsoft Public License") :- condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("Microsoft Reciprocal License") :- condition(disclose_source_code), condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("Mulan Permissive Software License, Version 2") :- condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("University of Illinois-NCSA Open Source License") :-condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("Open Data Commons Open Database License v1.0") :- condition(disclose_source_code), condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("SIL Open Font License 1.1") :- condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("Open Software License 3.0") :- condition(disclose_source_code), condition(copyright_license_with_source_code), condition(copyright_license_with_binaries), condition(network_use_is_distribution).
can_distribute("PostgreSQL License") :- condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("The Unlicense").
can_distribute("Universal Permissive License v1.0") :- condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("Vim License") :- condition(disclose_source_code), condition(copyright_license_with_source_code), condition(copyright_license_with_binaries).
can_distribute("Do What The F*ck You Want To Public License").
can_distribute("zlib License") :- condition(copyright_license_with_source_code).

%Modification
can_modify("BSD Zero Clause License").
can_modify("Academic Free License v3.0") :- condition(document_changes).
can_modify("GNU Affero General Public License v3.0") :- condition(same_license), condition(document_changes).
can_modify("Apache License 2.0") :- condition(document_changes).
can_modify("Artistic License 2.0") :- condition(document_changes).
can_modify("BSD 2-Clause \"Simplified\" License").
can_modify("BSD 3-Clause Clear License").
can_modify("BSD 3-Clause \"New\" or \"Revised\" License").
can_modify("BSD 4-Clause \"Original\" or \"Old\" License").
can_modify("Boost Software License 1.0").
can_modify("Creative Commons Attribution 4.0 International") :- condition(document_changes).
can_modify("Creative Commons Attribution Share Alike 4.0 International") :- condition(same_license), condition(document_changes).
can_modify("Creative Commons Zero v1.0 Universal").
can_modify("CeCILL Free Software License Agreement v2.1") :- condition(same_license).
can_modify("CERN Open Hardware License Version 2 - Permissive") :- condition(document_changes).
can_modify("CERN Open Hardware License Version 2 - Strongly Reciprocal") :- condition(same_license), condition(document_changes).
can_modify("CERN Open Hardware License Version 2 - Weakly Reciprocal") :- condition(same_license_library), condition(document_changes).
can_modify("Educational Community License v2.0") :- condition(document_changes).
can_modify("Eclipse Public License 1.0") :- condition(same_license).
can_modify("Eclipse Public License 2.0") :- condition(same_license).
can_modify("European Union Public License 1.1") :- condition(same_license), condition(document_changes).
can_modify("European Union Public License 1.2") :- condition(same_license), condition(document_changes).
can_modify("GNU Free Documentation License v1.3") :- condition(same_license), condition(document_changes).
can_modify("GNU General Public License v2.0") :- condition(same_license), condition(document_changes).
can_modify("GNU General Public License v3.0") :- condition(same_license), condition(document_changes).
can_modify("ISC License").
can_modify("GNU Lesser General Public License v2.1") :- condition(same_license_library), condition(document_changes).
can_modify("GNU Lesser General Public License v3.0") :- condition(same_license_library), condition(document_changes).
can_modify("LaTeX Project Public License v1.3c") :- condition(document_changes).
can_modify("MIT No Attribution").
can_modify("MIT License").
can_modify("Mozilla Public License 2.0") :- condition(same_license_modded_files).
can_modify("Microsoft Public License").
can_modify("Microsoft Reciprocal License") :- condition(same_license_modded_files).
can_modify("Mulan Permissive Software License, Version 2").
can_modify("University of Illinois-NCSA Open Source License").
can_modify("Open Data Commons Open Database License v1.0") :- condition(same_license).
can_modify("SIL Open Font License 1.1") :- condition(same_license).
can_modify("Open Software License 3.0") :- condition(same_license), condition(document_changes).
can_modify("PostgreSQL License").
can_modify("The Unlicense").
can_modify("Universal Permissive License v1.0").
can_modify("Vim License") :- condition(same_license), condition(document_changes).
can_modify("Do What The F*ck You Want To Public License").
can_modify("zlib License") :- condition(document_changes).

%Patent Use
patent_use("Academic Free License v3.0").
patent_use("GNU Affero General Public License v3.0").
patent_use("Apache License 2.0").
patent_use("Artistic License 2.0").
patent_use("CeCILL Free Software License Agreement v2.1").
patent_use("CERN Open Hardware License Version 2 - Permissive").
patent_use("CERN Open Hardware License Version 2 - Strongly Reciprocal").
patent_use("CERN Open Hardware License Version 2 - Weakly Reciprocal").
patent_use("Educational Community License v2.0").
patent_use("Eclipse Public License 1.0").
patent_use("Eclipse Public License 2.0").
patent_use("European Union Public License 1.1").
patent_use("European Union Public License 1.2").
patent_use("GNU General Public License v3.0").
patent_use("GNU Lesser General Public License v3.0").
patent_use("Mozilla Public License 2.0").
patent_use("Microsoft Public License").
patent_use("Microsoft Reciprocal License").
patent_use("Mulan Permissive Software License, Version 2").
patent_use("Open Software License 3.0").
patent_use("Universal Permissive License v1.0").

%Private Use
can_use_privately("BSD Zero Clause License").
can_use_privately("Academic Free License v3.0").
can_use_privately("GNU Affero General Public License v3.0").
can_use_privately("Apache License 2.0").
can_use_privately("Artistic License 2.0").
can_use_privately("BSD 2-Clause \"Simplified\" License").
can_use_privately("BSD 3-Clause Clear License").
can_use_privately("BSD 3-Clause \"New\" or \"Revised\" License").
can_use_privately("BSD 4-Clause \"Original\" or \"Old\" License").
can_use_privately("Boost Software License 1.0").
can_use_privately("Creative Commons Attribution 4.0 International").
can_use_privately("Creative Commons Attribution Share Alike 4.0 International").
can_use_privately("Creative Commons Zero v1.0 Universal").
can_use_privately("CeCILL Free Software License Agreement v2.1").
can_use_privately("CERN Open Hardware License Version 2 - Permissive").
can_use_privately("CERN Open Hardware License Version 2 - Strongly Reciprocal").
can_use_privately("CERN Open Hardware License Version 2 - Weakly Reciprocal").
can_use_privately("Educational Community License v2.0").
can_use_privately("Eclipse Public License 1.0").
can_use_privately("Eclipse Public License 2.0").
can_use_privately("European Union Public License 1.1").
can_use_privately("European Union Public License 1.2").
can_use_privately("GNU Free Documentation License v1.3").
can_use_privately("GNU General Public License v2.0").
can_use_privately("GNU General Public License v3.0").
can_use_privately("ISC License").
can_use_privately("GNU Lesser General Public License v2.1").
can_use_privately("GNU Lesser General Public License v3.0").
can_use_privately("LaTeX Project Public License v1.3c").
can_use_privately("MIT No Attribution").
can_use_privately("MIT License").
can_use_privately("Mozilla Public License 2.0").
can_use_privately("Microsoft Public License").
can_use_privately("Microsoft Reciprocal License").
can_use_privately("Mulan Permissive Software License, Version 2").
can_use_privately("University of Illinois-NCSA Open Source License").
can_use_privately("Open Data Commons Open Database License v1.0").
can_use_privately("SIL Open Font License 1.1").
can_use_privately("Open Software License 3.0").
can_use_privately("PostgreSQL License").
can_use_privately("The Unlicense").
can_use_privately("Universal Permissive License v1.0").
can_use_privately("Vim License").
can_use_privately("Do What The F*ck You Want To Public License").
can_use_privately("zlib License").

%Patent Use Limitation
limitation_patent_use("BSD 3-Clause Clear License").
limitation_patent_use("Creative Commons Attribution 4.0 International").
limitation_patent_use("Creative Commons Attribution Share Alike 4.0 International").
limitation_patent_use("Creative Commons Zero v1.0 Universal").
limitation_patent_use("Open Data Commons Open Database License v1.0").

%Liability Limitation
limitation_liability("BSD Zero Clause License").
limitation_liability("Academic Free License v3.0").
limitation_liability("GNU Affero General Public License v3.0").
limitation_liability("Apache License 2.0").
limitation_liability("Artistic License 2.0").
limitation_liability("BSD 2-Clause \"Simplified\" License").
limitation_liability("BSD 3-Clause Clear License").
limitation_liability("BSD 3-Clause \"New\" or \"Revised\" License").
limitation_liability("BSD 4-Clause \"Original\" or \"Old\" License").
limitation_liability("Boost Software License 1.0").
limitation_liability("Creative Commons Attribution 4.0 International").
limitation_liability("Creative Commons Attribution Share Alike 4.0 International").
limitation_liability("Creative Commons Zero v1.0 Universal").
limitation_liability("CeCILL Free Software License Agreement v2.1").
limitation_liability("CERN Open Hardware License Version 2 - Permissive").
limitation_liability("CERN Open Hardware License Version 2 - Strongly Reciprocal").
limitation_liability("CERN Open Hardware License Version 2 - Weakly Reciprocal").
limitation_liability("Educational Community License v2.0").
limitation_liability("Eclipse Public License 1.0").
limitation_liability("Eclipse Public License 2.0").
limitation_liability("European Union Public License 1.1").
limitation_liability("European Union Public License 1.2").
limitation_liability("GNU Free Documentation License v1.3").
limitation_liability("GNU General Public License v2.0").
limitation_liability("GNU General Public License v3.0").
limitation_liability("ISC License").
limitation_liability("GNU Lesser General Public License v2.1").
limitation_liability("GNU Lesser General Public License v3.0").
limitation_liability("LaTeX Project Public License v1.3c").
limitation_liability("MIT No Attribution").
limitation_liability("MIT License").
limitation_liability("Mozilla Public License 2.0").
limitation_liability("Mulan Permissive Software License, Version 2").
limitation_liability("University of Illinois-NCSA Open Source License").
limitation_liability("Open Data Commons Open Database License v1.0").
limitation_liability("SIL Open Font License 1.1").
limitation_liability("Open Software License 3.0").
limitation_liability("PostgreSQL License").
limitation_liability("The Unlicense").
limitation_liability("Universal Permissive License v1.0").
limitation_liability("zlib License").

%Trademark Use Limitation
limitation_trademark_use("Academic Free License v3.0").
limitation_trademark_use("Apache License 2.0").
limitation_trademark_use("Artistic License 2.0").
limitation_trademark_use("Creative Commons Attribution 4.0 International").
limitation_trademark_use("Creative Commons Attribution Share Alike 4.0 International").
limitation_trademark_use("Creative Commons Zero v1.0 Universal").
limitation_trademark_use("Educational Community License v2.0").
limitation_trademark_use("European Union Public License 1.1").
limitation_trademark_use("European Union Public License 1.2").
limitation_trademark_use("Mozilla Public License 2.0").
limitation_trademark_use("Microsoft Public License").
limitation_trademark_use("Microsoft Reciprocal License").
limitation_trademark_use("Mulan Permissive Software License, Version 2").
limitation_trademark_use("Open Data Commons Open Database License v1.0").
limitation_trademark_use("Open Software License 3.0").

%Warranty Limitation
limitation_warranty("BSD Zero Clause License").
limitation_warranty("Academic Free License v3.0").
limitation_warranty("GNU Affero General Public License v3.0").
limitation_warranty("Apache License 2.0").
limitation_warranty("Artistic License 2.0").
limitation_warranty("BSD 2-Clause \"Simplified\" License").
limitation_warranty("BSD 3-Clause Clear License").
limitation_warranty("BSD 3-Clause \"New\" or \"Revised\" License").
limitation_warranty("BSD 4-Clause \"Original\" or \"Old\" License").
limitation_warranty("Boost Software License 1.0").
limitation_warranty("Creative Commons Attribution 4.0 International").
limitation_warranty("Creative Commons Attribution Share Alike 4.0 International").
limitation_warranty("Creative Commons Zero v1.0 Universal").
limitation_warranty("CeCILL Free Software License Agreement v2.1").
limitation_warranty("CERN Open Hardware License Version 2 - Permissive").
limitation_warranty("CERN Open Hardware License Version 2 - Strongly Reciprocal").
limitation_warranty("CERN Open Hardware License Version 2 - Weakly Reciprocal").
limitation_warranty("Educational Community License v2.0").
limitation_warranty("Eclipse Public License 1.0").
limitation_warranty("Eclipse Public License 2.0").
limitation_warranty("European Union Public License 1.1").
limitation_warranty("European Union Public License 1.2").
limitation_warranty("GNU Free Documentation License v1.3").
limitation_warranty("GNU General Public License v2.0").
limitation_warranty("GNU General Public License v3.0").
limitation_warranty("ISC License").
limitation_warranty("GNU Lesser General Public License v2.1").
limitation_warranty("GNU Lesser General Public License v3.0").
limitation_warranty("LaTeX Project Public License v1.3c").
limitation_warranty("MIT No Attribution").
limitation_warranty("MIT License").
limitation_warranty("Mozilla Public License 2.0").
limitation_warranty("Microsoft Public License").
limitation_warranty("Microsoft Reciprocal License").
limitation_warranty("Mulan Permissive Software License, Version 2").
limitation_warranty("University of Illinois-NCSA Open Source License").
limitation_warranty("Open Data Commons Open Database License v1.0").
limitation_warranty("SIL Open Font License 1.1").
limitation_warranty("Open Software License 3.0").
limitation_warranty("PostgreSQL License").
limitation_warranty("The Unlicense").
limitation_warranty("Universal Permissive License v1.0").
limitation_warranty("zlib License").

%Has Condition Disclose Source Code
has_condition("GNU Affero General Public License v3.0", disclose_source_code).
has_condition("CeCILL Free Software License Agreement v2.1", disclose_source_code).
has_condition("CERN Open Hardware License Version 2 - Strongly Reciprocal", disclose_source_code).
has_condition("CERN Open Hardware License Version 2 - Weakly Reciprocal", disclose_source_code).
has_condition("Eclipse Public License 1.0", disclose_source_code).
has_condition("Eclipse Public License 2.0", disclose_source_code).
has_condition("European Union Public License 1.1", disclose_source_code).
has_condition("European Union Public License 1.2", disclose_source_code).
has_condition("GNU Free Documentation License v1.3", disclose_source_code).
has_condition("GNU General Public License v2.0", disclose_source_code).
has_condition("GNU General Public License v3.0", disclose_source_code).
has_condition("GNU Lesser General Public License v2.1", disclose_source_code).
has_condition("GNU Lesser General Public License v3.0", disclose_source_code).
has_condition("LaTeX Project Public License v1.3c", disclose_source_code).
has_condition("Mozilla Public License 2.0", disclose_source_code).
has_condition("Microsoft Reciprocal License", disclose_source_code).
has_condition("Open Data Commons Open Database License v1.0", disclose_source_code).
has_condition("Open Software License 3.0", disclose_source_code).
has_condition("Vim License", disclose_source_code).

%Has Condition copyright_license_with_source_code
has_condition("Academic Free License v3.0", copyright_license_with_source_code).
has_condition("GNU Affero General Public License v3.0", copyright_license_with_source_code).
has_condition("Apache License 2.0", copyright_license_with_source_code).
has_condition("Artistic License 2.0", copyright_license_with_source_code).
has_condition("BSD 2-Clause \"Simplified\" License", copyright_license_with_source_code).
has_condition("BSD 3-Clause Clear License", copyright_license_with_source_code).
has_condition("BSD 3-Clause \"New\" or \"Revised\" License", copyright_license_with_source_code).
has_condition("BSD 4-Clause \"Original\" or \"Old\" License", copyright_license_with_source_code).
has_condition("Boost Software License 1.0", copyright_license_with_source_code).
has_condition("Creative Commons Attribution 4.0 International", copyright_license_with_source_code).
has_condition("Creative Commons Attribution Share Alike 4.0 International", copyright_license_with_source_code).
has_condition("CeCILL Free Software License Agreement v2.1", copyright_license_with_source_code).
has_condition("CERN Open Hardware License Version 2 - Permissive", copyright_license_with_source_code).
has_condition("CERN Open Hardware License Version 2 - Strongly Reciprocal", copyright_license_with_source_code).
has_condition("CERN Open Hardware License Version 2 - Weakly Reciprocal", copyright_license_with_source_code).
has_condition("Educational Community License v2.0", copyright_license_with_source_code).
has_condition("Eclipse Public License 1.0", copyright_license_with_source_code).
has_condition("Eclipse Public License 2.0", copyright_license_with_source_code).
has_condition("European Union Public License 1.1", copyright_license_with_source_code).
has_condition("European Union Public License 1.2", copyright_license_with_source_code).
has_condition("GNU Free Documentation License v1.3", copyright_license_with_source_code).
has_condition("GNU General Public License v2.0", copyright_license_with_source_code).
has_condition("GNU General Public License v3.0", copyright_license_with_source_code).
has_condition("ISC License", copyright_license_with_source_code).
has_condition("GNU Lesser General Public License v2.1", copyright_license_with_source_code).
has_condition("GNU Lesser General Public License v3.0", copyright_license_with_source_code).
has_condition("LaTeX Project Public License v1.3c", copyright_license_with_source_code).
has_condition("MIT License", copyright_license_with_source_code).
has_condition("Mozilla Public License 2.0", copyright_license_with_source_code).
has_condition("Microsoft Public License", copyright_license_with_source_code).
has_condition("Microsoft Reciprocal License", copyright_license_with_source_code).
has_condition("Mulan Permissive Software License, Version 2", copyright_license_with_source_code).
has_condition("University of Illinois-NCSA Open Source License", copyright_license_with_source_code).
has_condition("Open Data Commons Open Database License v1.0", copyright_license_with_source_code).
has_condition("SIL Open Font License 1.1", copyright_license_with_source_code).
has_condition("Open Software License 3.0", copyright_license_with_source_code).
has_condition("PostgreSQL License", copyright_license_with_source_code).
has_condition("Universal Permissive License v1.0", copyright_license_with_source_code).
has_condition("Vim License", copyright_license_with_source_code).
has_condition("zlib License", copyright_license_with_source_code).

%Has Condition copyright_license_with_binaries
has_condition("Academic Free License v3.0", copyright_license_with_binaries).
has_condition("GNU Affero General Public License v3.0", copyright_license_with_binaries).
has_condition("Apache License 2.0", copyright_license_with_binaries).
has_condition("Artistic License 2.0", copyright_license_with_binaries).
has_condition("BSD 2-Clause \"Simplified\" License", copyright_license_with_binaries).
has_condition("BSD 3-Clause Clear License", copyright_license_with_binaries).
has_condition("BSD 3-Clause \"New\" or \"Revised\" License", copyright_license_with_binaries).
has_condition("BSD 4-Clause \"Original\" or \"Old\" License", copyright_license_with_binaries).
has_condition("Creative Commons Attribution 4.0 International", copyright_license_with_binaries).
has_condition("Creative Commons Attribution Share Alike 4.0 International", copyright_license_with_binaries).
has_condition("CeCILL Free Software License Agreement v2.1", copyright_license_with_binaries).
has_condition("CERN Open Hardware License Version 2 - Permissive", copyright_license_with_binaries).
has_condition("CERN Open Hardware License Version 2 - Strongly Reciprocal", copyright_license_with_binaries).
has_condition("CERN Open Hardware License Version 2 - Weakly Reciprocal", copyright_license_with_binaries).
has_condition("Educational Community License v2.0", copyright_license_with_binaries).
has_condition("Eclipse Public License 1.0", copyright_license_with_binaries).
has_condition("Eclipse Public License 2.0", copyright_license_with_binaries).
has_condition("European Union Public License 1.1", copyright_license_with_binaries).
has_condition("European Union Public License 1.2", copyright_license_with_binaries).
has_condition("GNU Free Documentation License v1.3", copyright_license_with_binaries).
has_condition("GNU General Public License v2.0", copyright_license_with_binaries).
has_condition("GNU General Public License v3.0", copyright_license_with_binaries).
has_condition("ISC License", copyright_license_with_binaries).
has_condition("GNU Lesser General Public License v2.1", copyright_license_with_binaries).
has_condition("GNU Lesser General Public License v3.0", copyright_license_with_binaries).
has_condition("LaTeX Project Public License v1.3c", copyright_license_with_binaries).
has_condition("MIT License", copyright_license_with_binaries).
has_condition("Mozilla Public License 2.0", copyright_license_with_binaries).
has_condition("Microsoft Public License", copyright_license_with_binaries).
has_condition("Microsoft Reciprocal License", copyright_license_with_binaries).
has_condition("Mulan Permissive Software License, Version 2", copyright_license_with_binaries).
has_condition("University of Illinois-NCSA Open Source License", copyright_license_with_binaries).
has_condition("Open Data Commons Open Database License v1.0", copyright_license_with_binaries).
has_condition("SIL Open Font License 1.1", copyright_license_with_binaries).
has_condition("Open Software License 3.0", copyright_license_with_binaries).
has_condition("PostgreSQL License", copyright_license_with_binaries).
has_condition("Universal Permissive License v1.0", copyright_license_with_binaries).
has_condition("Vim License", copyright_license_with_binaries).

%Has condition network_use_is_distribution
has_condition("GNU Affero General Public License v3.0", network_use_is_distribution).
has_condition("CeCILL Free Software License Agreement v2.1", network_use_is_distribution).
has_condition("European Union Public License 1.1", network_use_is_distribution).
has_condition("European Union Public License 1.2", network_use_is_distribution).
has_condition("Open Software License 3.0", network_use_is_distribution).

%Has condition same_license
has_condition("GNU Affero General Public License v3.0", same_license).
has_condition("Creative Commons Attribution Share Alike 4.0 International", same_license).
has_condition("CeCILL Free Software License Agreement v2.1", same_license).
has_condition("CERN Open Hardware License Version 2 - Strongly Reciprocal", same_license).
has_condition("CERN Open Hardware License Version 2 - Weakly Reciprocal", same_license_library).
has_condition("Eclipse Public License 1.0", same_license).
has_condition("Eclipse Public License 2.0", same_license).
has_condition("European Union Public License 1.1", same_license).
has_condition("European Union Public License 1.2", same_license).
has_condition("GNU Free Documentation License v1.3", same_license).
has_condition("GNU General Public License v2.0", same_license).
has_condition("GNU General Public License v3.0", same_license).
has_condition("GNU Lesser General Public License v2.1", same_license_library).
has_condition("GNU Lesser General Public License v3.0", same_license_library).
has_condition("Mozilla Public License 2.0", same_license_modded_files).
has_condition("Microsoft Reciprocal License", same_license_modded_files).
has_condition("Open Data Commons Open Database License v1.0", same_license).
has_condition("SIL Open Font License 1.1", same_license).
has_condition("Open Software License 3.0", same_license).
has_condition("Vim License", same_license).

%Has condition document_changes
has_condition("Academic Free License v3.0", document_changes).
has_condition("GNU Affero General Public License v3.0", document_changes).
has_condition("Apache License 2.0", document_changes).
has_condition("Artistic License 2.0", document_changes).
has_condition("Creative Commons Attribution 4.0 International", document_changes).
has_condition("Creative Commons Attribution Share Alike 4.0 International", document_changes).
has_condition("CERN Open Hardware License Version 2 - Permissive", document_changes).
has_condition("CERN Open Hardware License Version 2 - Strongly Reciprocal", document_changes).
has_condition("CERN Open Hardware License Version 2 - Weakly Reciprocal", document_changes).
has_condition("Educational Community License v2.0", document_changes).
has_condition("European Union Public License 1.1", document_changes).
has_condition("European Union Public License 1.2", document_changes).
has_condition("GNU Free Documentation License v1.3", document_changes).
has_condition("GNU General Public License v2.0", document_changes).
has_condition("GNU General Public License v3.0", document_changes).
has_condition("GNU Lesser General Public License v2.1", document_changes).
has_condition("GNU Lesser General Public License v3.0", document_changes).
has_condition("LaTeX Project Public License v1.3c", document_changes).
has_condition("Open Software License 3.0", document_changes).
has_condition("Vim License", document_changes).

condition(none).

%All of the conditions
/*
condition(disclose_source_code).
condition(copyright_license_with_source_code).
condition(copyright_license_with_binaries).
condition(network_use_is_distribution).

condition(same_license).
condition(same_license_modded_files).
condition(same_license_library).
condition(document_changes).
*/

%Rules
permission(X, can_use_commercially) :- can_use_commercially(X).
permission(X, can_distribute) :- can_distribute(X).
permission(X, can_modify) :- can_modify(X).
permission(X, can_use_privately) :- can_use_privately(X).
permission(X, patent_use) :- patent_use(X).

conditions_before_distribution(X, disclose_source_code) :- has_condition(X, disclose_source_code).
conditions_before_distribution(X, copyright_license_with_source_code) :- has_condition(X, copyright_license_with_source_code).
conditions_before_distribution(X, copyright_license_with_binaries) :- has_condition(X, copyright_license_with_binaries).
conditions_before_distribution(X, network_use_is_distribution) :- has_condition(X, network_use_is_distribution).

conditions_before_modification(X, same_license) :- has_condition(X, same_license).
conditions_before_modification(X, same_license_modded_files) :- has_condition(X, same_license_modded_files).
conditions_before_modification(X, same_license_library) :- has_condition(X, same_license_library).
conditions_before_modification(X, document_changes) :- has_condition(X, document_changes).


limitation(X, liability) :- limitation_liability(X).
limitation(X, patent_use) :- limitation_patent_use(X).
limitation(X, warranty) :- limitation_warranty(X).
limitation(X, trademark_use) :- limitation_trademark_use(X).



license_a_permission(Y) :- license_a(X), permission(X, Y).
license_b_permission(Y) :- license_b(X), permission(X, Y).
license_a_condition(Y) :- license_a(X), has_condition(X, Y).
license_b_condition(Y) :- license_b(X), has_condition(X, Y).
license_a_conditions_before_distribution(Y) :- license_a(X), conditions_before_distribution(X, Y).
license_b_conditions_before_distribution(Y) :- license_b(X), conditions_before_distribution(X, Y).
license_a_conditions_before_modification(Y) :- license_a(X), conditions_before_modification(X, Y).
license_b_conditions_before_modification(Y) :- license_b(X), conditions_before_modification(X, Y).
license_a_limitation(Y) :- license_a(X), limitation(X, Y).
license_b_limitation(Y) :- license_b(X), limitation(X, Y).

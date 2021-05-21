%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-c
Version:        %{tl_version}
Release:        24
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0003:     texlive-licenses.tar.xz
Source0630:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bbding.tar.xz
Source0631:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bbding.doc.tar.xz
Source0633:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bbm-macros.tar.xz
Source0634:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bbm-macros.doc.tar.xz
Source0636:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bbm.tar.xz
Source0637:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bbm.doc.tar.xz
Source0638:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bbold.tar.xz
Source0639:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bbold.doc.tar.xz
Source0641:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bbold-type1.tar.xz
Source0642:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bbold-type1.doc.tar.xz
Source0643:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bchart.tar.xz
Source0644:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bchart.doc.tar.xz
Source0645:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bclogo.tar.xz
Source0646:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bclogo.doc.tar.xz
Source0647:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamer2thesis.tar.xz
Source0648:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamer2thesis.doc.tar.xz
Source0649:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beameraudience.tar.xz
Source0650:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beameraudience.doc.tar.xz
Source0651:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamerdarkthemes.tar.xz
Source0652:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamerdarkthemes.doc.tar.xz
Source0653:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamer-FUBerlin.doc.tar.xz
Source0654:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamerposter.tar.xz
Source0655:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamerposter.doc.tar.xz
Source0656:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamersubframe.tar.xz
Source0657:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamersubframe.doc.tar.xz
Source0659:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamerthemejltree.tar.xz
Source0660:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamerthemenirma.tar.xz
Source0661:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamerthemenirma.doc.tar.xz
Source0662:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamertheme-phnompenh.tar.xz
Source0663:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamertheme-phnompenh.doc.tar.xz
Source0664:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamertheme-upenn-bc.tar.xz
Source0665:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamertheme-upenn-bc.doc.tar.xz
Source0666:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamer.tar.xz
Source0667:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamer.doc.tar.xz
Source0677:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamer-tut-pt.doc.tar.xz
Source0678:     beebe-clean.tar.xz
Source0679:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/begingreek.tar.xz
Source0680:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/begingreek.doc.tar.xz
Source0682:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/begriff.tar.xz
Source0683:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/begriff.doc.tar.xz
Source0684:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/belleek.tar.xz
Source0685:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/belleek.doc.tar.xz
Source0687:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bengali.tar.xz
Source0688:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bengali.doc.tar.xz
Source0690:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bera.tar.xz
Source0691:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bera.doc.tar.xz
Source0692:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/berenisadf.tar.xz
Source0693:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/berenisadf.doc.tar.xz
Source0694:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/besjournals.tar.xz
Source0695:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/besjournals.doc.tar.xz
Source0696:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/betababel.tar.xz
Source0697:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/betababel.doc.tar.xz
Source0698:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beton.tar.xz
Source0699:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beton.doc.tar.xz
Source0701:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bewerbung.tar.xz
Source0702:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bewerbung.doc.tar.xz
Source0704:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bez123.tar.xz
Source0705:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bez123.doc.tar.xz
Source0707:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bezos.tar.xz
Source0708:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bezos.doc.tar.xz
Source0709:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bgreek.tar.xz
Source0710:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bgreek.doc.tar.xz
Source0711:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bgteubner.tar.xz
Source0712:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bgteubner.doc.tar.xz
Source0714:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bguq.tar.xz
Source0715:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bguq.doc.tar.xz
Source0717:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bhcexam.tar.xz
Source0718:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bhcexam.doc.tar.xz
Source0720:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibarts.tar.xz
Source0721:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibarts.doc.tar.xz
Source0726:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bib-fr.tar.xz
Source0727:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bib-fr.doc.tar.xz
Source0728:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibhtml.tar.xz
Source0729:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibhtml.doc.tar.xz
Source0730:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-anonymous.tar.xz
Source0731:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-anonymous.doc.tar.xz
Source0732:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-apa.tar.xz
Source0733:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-apa.doc.tar.xz
Source0734:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-bookinarticle.tar.xz
Source0735:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-bookinarticle.doc.tar.xz
Source0736:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-bwl.tar.xz
Source0737:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-bwl.doc.tar.xz
Source0738:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-caspervector.tar.xz
Source0739:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-caspervector.doc.tar.xz
Source0740:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-chem.tar.xz
Source0741:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-chem.doc.tar.xz
Source0742:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-chicago.tar.xz
Source0743:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-chicago.doc.tar.xz
Source0744:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-dw.tar.xz
Source0745:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-dw.doc.tar.xz
Source0746:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-fiwi.tar.xz
Source0747:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-fiwi.doc.tar.xz
Source0748:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-gost.tar.xz
Source0749:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-gost.doc.tar.xz
Source0750:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-historian.tar.xz
Source0751:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-historian.doc.tar.xz
Source0752:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-ieee.tar.xz
Source0753:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-ieee.doc.tar.xz
Source0754:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-juradiss.tar.xz
Source0755:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-juradiss.doc.tar.xz
Source0756:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-luh-ipw.tar.xz
Source0757:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-luh-ipw.doc.tar.xz
Source0758:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-manuscripts-philology.tar.xz
Source0759:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-manuscripts-philology.doc.tar.xz
Source0760:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-mla.tar.xz
Source0761:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-mla.doc.tar.xz
Source0762:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-multiple-dm.tar.xz
Source0763:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-multiple-dm.doc.tar.xz
Source0764:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-musuos.tar.xz
Source0765:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-musuos.doc.tar.xz
Source0766:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-nature.tar.xz
Source0767:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-nature.doc.tar.xz
Source0768:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-nejm.tar.xz
Source0769:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-nejm.doc.tar.xz
Source0770:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-opcit-booktitle.tar.xz
Source0771:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-opcit-booktitle.doc.tar.xz
Source0772:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-philosophy.tar.xz
Source0773:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-philosophy.doc.tar.xz
Source0775:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-phys.tar.xz
Source0776:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-phys.doc.tar.xz
Source0777:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-publist.tar.xz
Source0778:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-publist.doc.tar.xz
Source0779:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-realauthor.tar.xz
Source0780:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-realauthor.doc.tar.xz
Source0781:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-science.tar.xz
Source0782:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-science.doc.tar.xz
Source0783:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-source-division.tar.xz
Source0784:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-source-division.doc.tar.xz
Source0785:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-subseries.tar.xz
Source0786:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-subseries.doc.tar.xz
Source0787:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-swiss-legal.tar.xz
Source0788:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-swiss-legal.doc.tar.xz
Source0789:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex.tar.xz
Source0790:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex.doc.tar.xz
Source0791:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-trad.tar.xz
Source0792:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-trad.doc.tar.xz
Source0793:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-true-citepages-omit.tar.xz
Source0794:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-true-citepages-omit.doc.tar.xz
Source0795:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibleref-french.tar.xz
Source0796:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibleref-french.doc.tar.xz
Source0798:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibleref-german.tar.xz
Source0799:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibleref-german.doc.tar.xz
Source0800:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibleref-lds.tar.xz
Source0801:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibleref-lds.doc.tar.xz
Source0803:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibleref-mouth.tar.xz
Source0804:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibleref-mouth.doc.tar.xz
Source0806:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibleref-parse.tar.xz
Source0807:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibleref-parse.doc.tar.xz
Source0808:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibleref.tar.xz
Source0809:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibleref.doc.tar.xz
Source0811:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblist.tar.xz
Source0812:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblist.doc.tar.xz
Source0819:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibtopicprefix.tar.xz
Source0820:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibtopicprefix.doc.tar.xz
Source0822:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibtopic.tar.xz
Source0823:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibtopic.doc.tar.xz
Source0825:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibunits.tar.xz
Source0826:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibunits.doc.tar.xz
Source0828:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bidi-atbegshi.tar.xz
Source0829:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bidi-atbegshi.doc.tar.xz
Source0830:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bidicontour.tar.xz
Source0831:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bidicontour.doc.tar.xz
Source0832:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bidihl.tar.xz
Source0833:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bidihl.doc.tar.xz
Source0834:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bidipagegrid.tar.xz
Source0835:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bidipagegrid.doc.tar.xz
Source0836:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bidipresentation.tar.xz
Source0837:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bidipresentation.doc.tar.xz
Source0838:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bidishadowtext.tar.xz
Source0839:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bidishadowtext.doc.tar.xz
Source0840:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bidi.tar.xz
Source0841:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bidi.doc.tar.xz
Source0843:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bigfoot.tar.xz
Source0844:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bigfoot.doc.tar.xz
Source0846:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bigints.tar.xz
Source0847:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bigints.doc.tar.xz
Source0848:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/binomexp.tar.xz
Source0849:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/binomexp.doc.tar.xz
Source0851:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biocon.tar.xz
Source0852:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biocon.doc.tar.xz
Source0853:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bitelist.tar.xz
Source0854:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bitelist.doc.tar.xz
Source0856:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bizcard.tar.xz
Source0857:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bizcard.doc.tar.xz
Source7242:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamercolorthemeowl.tar.xz
Source7243:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamercolorthemeowl.doc.tar.xz
Source7245:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamertheme-detlevcm.tar.xz
Source7246:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamertheme-detlevcm.doc.tar.xz
Source7247:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamertheme-epyt.tar.xz
Source7248:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamertheme-epyt.doc.tar.xz
Source7249:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamertheme-metropolis.tar.xz
Source7250:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamertheme-metropolis.doc.tar.xz
Source7252:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamer-verona.tar.xz
Source7253:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamer-verona.doc.tar.xz
Source7254:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-abnt.tar.xz
Source7255:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-abnt.doc.tar.xz
Source7256:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-bookinother.tar.xz
Source7257:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-bookinother.doc.tar.xz
Source7258:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-iso690.tar.xz
Source7259:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-iso690.doc.tar.xz
Source7260:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-morenames.tar.xz
Source7261:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-morenames.doc.tar.xz
Source7262:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibletext.tar.xz
Source7263:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibletext.doc.tar.xz
Source7265:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibtexperllibs.doc.tar.xz
Source7267:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bitpattern.tar.xz
Source7268:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bitpattern.doc.tar.xz
Source7598:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bestpapers.tar.xz
Source7599:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bestpapers.doc.tar.xz
Source7600:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-claves.tar.xz
Source7601:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-claves.doc.tar.xz
Source7602:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-ijsra.tar.xz
Source7603:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-ijsra.doc.tar.xz
Source7604:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-lni.tar.xz
Source7605:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-lni.doc.tar.xz
Source7606:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-nottsclassic.tar.xz
Source7607:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-nottsclassic.doc.tar.xz
Source7650:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamerswitch.tar.xz
Source7651:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamerswitch.doc.tar.xz
Source7652:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beilstein.tar.xz
Source7653:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beilstein.doc.tar.xz
Source7654:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beuron.tar.xz
Source7655:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beuron.doc.tar.xz
Source7658:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-cheatsheet.doc.tar.xz
Source7659:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-enc.tar.xz
Source7660:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-enc.doc.tar.xz
Source7661:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-gb7714-2015.tar.xz
Source7662:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-gb7714-2015.doc.tar.xz
Source7663:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-oxref.tar.xz
Source7664:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-oxref.doc.tar.xz
Source7665:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-sbl.tar.xz
Source7666:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-sbl.doc.tar.xz
Source7667:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-shortfields.tar.xz
Source7668:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-shortfields.doc.tar.xz
Source7669:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/binarytree.tar.xz
Source7670:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/binarytree.doc.tar.xz
Source7671:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biochemistry-colors.tar.xz
Source7672:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biochemistry-colors.doc.tar.xz
Source7673:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biolett-bst.tar.xz
Source7674:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biolett-bst.doc.tar.xz
Source8078:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamertheme-cuerna.tar.xz
Source8079:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamertheme-cuerna.doc.tar.xz
Source8080:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamertheme-focus.tar.xz
Source8081:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamertheme-focus.doc.tar.xz
Source8082:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamertheme-saintpetersburg.tar.xz
Source8083:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/beamertheme-saintpetersburg.doc.tar.xz
Source8084:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bezierplot.tar.xz
Source8085:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bezierplot.doc.tar.xz
Source8086:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-archaeology.tar.xz
Source8087:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-archaeology.doc.tar.xz
Source8088:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-arthistory-bonn.tar.xz
Source8089:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-arthistory-bonn.doc.tar.xz
Source8090:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-socialscienceshuberlin.tar.xz
Source8091:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/biblatex-socialscienceshuberlin.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.


%package -n texlive-bbding
Provides:       tex-bbding = %{tl_version}
License:        LPPL
Summary:        A symbol (dingbat) font and LaTeX macros for its use
Version:        svn17186.1.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bbding10.tfm) = %{tl_version}, tex(Uding.fd) = %{tl_version}
Provides:       tex(bbding.sty) = %{tl_version}

%description -n texlive-bbding
A symbol font (distributed as Metafont source) that contains
many of the symbols of the Zapf dingbats set, together with an
NFSS interface for using the font. An Adobe Type 1 version of
the fonts is available in the niceframe fonts bundle.

%package -n texlive-bbding-doc
Summary:        Documentation for bbding
Version:        svn17186.1.01

Provides:       tex-bbding-doc
AutoReqProv:    No

%description -n texlive-bbding-doc
Documentation for bbding

%package -n texlive-bbm-macros
Provides:       tex-bbm-macros = %{tl_version}
License:        LPPL
Summary:        LaTeX support for "blackboard-style" cm fonts
Version:        svn17224.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bbm.sty) = %{tl_version}, tex(ubbm.fd) = %{tl_version}
Provides:       tex(ubbmss.fd) = %{tl_version}, tex(ubbmtt.fd) = %{tl_version}

%description -n texlive-bbm-macros
Provides LaTeX support for Blackboard variants of Computer
Modern fonts. Declares a font family bbm so you can in
principle write running text in blackboard bold, and lots of
math alphabets for using the fonts within maths.

%package -n texlive-bbm-macros-doc
Summary:        Documentation for bbm-macros
Version:        svn17224.0

Provides:       tex-bbm-macros-doc
AutoReqProv:    No

%description -n texlive-bbm-macros-doc
Documentation for bbm-macros

%package -n texlive-bbm
Provides:       tex-bbm = %{tl_version}
License:        Copyright only
Summary:        "Blackboard-style" cm fonts
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bbm10.tfm) = %{tl_version}, tex(bbm12.tfm) = %{tl_version}
Provides:       tex(bbm17.tfm) = %{tl_version}, tex(bbm5.tfm) = %{tl_version}
Provides:       tex(bbm6.tfm) = %{tl_version}, tex(bbm7.tfm) = %{tl_version}
Provides:       tex(bbm8.tfm) = %{tl_version}, tex(bbm9.tfm) = %{tl_version}
Provides:       tex(bbmb10.tfm) = %{tl_version}, tex(bbmbx10.tfm) = %{tl_version}
Provides:       tex(bbmbx12.tfm) = %{tl_version}, tex(bbmbx5.tfm) = %{tl_version}
Provides:       tex(bbmbx6.tfm) = %{tl_version}, tex(bbmbx7.tfm) = %{tl_version}
Provides:       tex(bbmbx8.tfm) = %{tl_version}, tex(bbmbx9.tfm) = %{tl_version}
Provides:       tex(bbmbxsl10.tfm) = %{tl_version}, tex(bbmdunh10.tfm) = %{tl_version}
Provides:       tex(bbmfib8.tfm) = %{tl_version}, tex(bbmfxib8.tfm) = %{tl_version}
Provides:       tex(bbmsl10.tfm) = %{tl_version}, tex(bbmsl12.tfm) = %{tl_version}
Provides:       tex(bbmsl8.tfm) = %{tl_version}, tex(bbmsl9.tfm) = %{tl_version}
Provides:       tex(bbmss10.tfm) = %{tl_version}, tex(bbmss12.tfm) = %{tl_version}
Provides:       tex(bbmss17.tfm) = %{tl_version}, tex(bbmss8.tfm) = %{tl_version}
Provides:       tex(bbmss9.tfm) = %{tl_version}, tex(bbmssbx10.tfm) = %{tl_version}
Provides:       tex(bbmssdc10.tfm) = %{tl_version}, tex(bbmssi10.tfm) = %{tl_version}
Provides:       tex(bbmssi12.tfm) = %{tl_version}, tex(bbmssi17.tfm) = %{tl_version}
Provides:       tex(bbmssi8.tfm) = %{tl_version}, tex(bbmssi9.tfm) = %{tl_version}
Provides:       tex(bbmssq8.tfm) = %{tl_version}, tex(bbmssqi8.tfm) = %{tl_version}
Provides:       tex(bbmtt10.tfm) = %{tl_version}, tex(bbmtt12.tfm) = %{tl_version}
Provides:       tex(bbmtt8.tfm) = %{tl_version}, tex(bbmtt9.tfm) = %{tl_version}

%description -n texlive-bbm
Blackboard variants of Computer Modern fonts. The fonts are
distributed as Metafont source (only); LaTeX support is
available with the bbm-macros package. The Sauter font package
has Metafont parameter source files for building the fonts at
more sizes than you could reasonably imagine. A sample of these
fonts appears in the blackboard bold sampler.

%package -n texlive-bbm-doc
Summary:        Documentation for bbm
Version:        svn15878.0

Provides:       tex-bbm-doc
AutoReqProv:    No

%description -n texlive-bbm-doc
Documentation for bbm

%package -n texlive-bbold
Provides:       tex-bbold = %{tl_version}
License:        BSD
Summary:        Sans serif blackboard bold
Version:        svn17187.1.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bbold10.tfm) = %{tl_version}, tex(bbold12.tfm) = %{tl_version}
Provides:       tex(bbold17.tfm) = %{tl_version}, tex(bbold5.tfm) = %{tl_version}
Provides:       tex(bbold6.tfm) = %{tl_version}, tex(bbold7.tfm) = %{tl_version}
Provides:       tex(bbold8.tfm) = %{tl_version}, tex(bbold9.tfm) = %{tl_version}
Provides:       tex(Ubbold.fd) = %{tl_version}, tex(bbold.sty) = %{tl_version}

%description -n texlive-bbold
A geometric sans serif blackboard bold font, for use in
mathematics; Metafont sources are provided, as well as macros
for use with LaTeX. The Sauter font package has Metafont
parameter source files for building the fonts at more sizes
than you could reasonably imagine. See the blackboard sampler
for a feel for the font's appearance.

%package -n texlive-bbold-doc
Summary:        Documentation for bbold
Version:        svn17187.1.01

Provides:       tex-bbold-doc
AutoReqProv:    No

%description -n texlive-bbold-doc
Documentation for bbold

%package -n texlive-bbold-type1
Provides:       tex-bbold-type1 = %{tl_version}
License:        Copyright only
Summary:        An Adobe Type 1 format version of the bbold font
Version:        svn33143.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(bbold.map) = %{tl_version}, tex(bbold10.pfb) = %{tl_version}
Provides:       tex(bbold5.pfb) = %{tl_version}, tex(bbold7.pfb) = %{tl_version}

%description -n texlive-bbold-type1
The files offer an Adobe Type 1 format version of the 5pt, 7pt
and 10pt versions of the bbold fonts. The distribution also
includes a map file, for use when incorporating the fonts into
TeX documents; the macros provided with the original Metafont
version of the font serve for the scaleable version, too. The
fonts were produced to be part of the TeX distribution from
Y&Y; they were generously donated to the TeX Users Group when
Y&Y closed its doors as a business.

%package -n texlive-bbold-type1-doc
Summary:        Documentation for bbold-type1
Version:        svn33143.0

Provides:       tex-bbold-type1-doc
AutoReqProv:    No

%description -n texlive-bbold-type1-doc
Documentation for bbold-type1

%package -n texlive-bchart
Provides:       tex-bchart = %{tl_version}
License:        MIT
Summary:        Draw simple bar charts in LaTeX
Version:        svn43928
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(bchart.sty) = %{tl_version}

%description -n texlive-bchart
The package provides horizontal bar charts, drawn using TikZ on
a numeric X-axis. The focus of the package is simplicity and
aesthetics.

%package -n texlive-bchart-doc
Summary:        Documentation for bchart
Version:        svn43928
Provides:       tex-bchart-doc
AutoReqProv:    No

%description -n texlive-bchart-doc
Documentation for bchart

%package -n texlive-bclogo
Provides:       tex-bclogo = %{tl_version}
License:        LPPL
Summary:        Creating colourful boxes with logos
Version:        svn39364

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(ifthen.sty), tex(graphicx.sty), tex(tikz.sty)
Requires:       tex(pst-blur.sty), tex(pstricks.sty), tex(pst-grad.sty), tex(pst-coil.sty)
Requires:       tex(ifpdf.sty)
Provides:       tex(bclogo.sty) = %{tl_version}

%description -n texlive-bclogo
The package facilitates the creation of colorful boxes with a
title and logo. It may use either tikz or PSTricks as graphics
engine.

%package -n texlive-bclogo-doc
Summary:        Documentation for bclogo
Version:        svn39364

Provides:       tex-bclogo-doc
AutoReqProv:    No

%description -n texlive-bclogo-doc
Documentation for bclogo

%package -n texlive-beamer2thesis
Provides:       tex-beamer2thesis = %{tl_version}
License:        LPPL
Summary:        Thesis presentations using beamer
Version:        svn27539.2.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifxetex.sty), tex(pifont.sty), tex(fontspec.sty), tex(xunicode.sty)
Requires:       tex(xltxtra.sty), tex(metalogo.sty), tex(xkeyval.sty), tex(polyglossia.sty)
Requires:       tex(inputenc.sty), tex(babel.sty)
Provides:       tex(beamercolorthemetorinoth.sty) = %{tl_version}
Provides:       tex(beamerfontthemetorinoth.sty) = %{tl_version}
Provides:       tex(beamerinnerthemetorinoth.sty) = %{tl_version}
Provides:       tex(beamerouterthemetorinoth.sty) = %{tl_version}
Provides:       tex(beamerthemeTorinoTh.sty) = %{tl_version}

%description -n texlive-beamer2thesis
The package specifies a beamer theme for presenting a thesis.

%package -n texlive-beamer2thesis-doc
Summary:        Documentation for beamer2thesis
Version:        svn27539.2.2

Provides:       tex-beamer2thesis-doc
AutoReqProv:    No

%description -n texlive-beamer2thesis-doc
Documentation for beamer2thesis

%package -n texlive-beameraudience
Provides:       tex-beameraudience = %{tl_version}
License:        LPPL
Summary:        Assembling beamer frames according to audience
Version:        svn23427.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty), tex(cprotect.sty), tex(ifthen.sty)
Provides:       tex(beameraudience.sty) = %{tl_version}

%description -n texlive-beameraudience
The Beamer Audience package provides macros to easily assemble
frames according to different audiences. It enables to pick up
the frames for a specific audience while leaving their order
according to a logical structure in the LaTeX source.

%package -n texlive-beameraudience-doc
Summary:        Documentation for beameraudience
Version:        svn23427.0.1

Provides:       tex-beameraudience-doc
AutoReqProv:    No

%description -n texlive-beameraudience-doc
Documentation for beameraudience

%package -n texlive-beamerdarkthemes
Provides:       tex-beamerdarkthemes = %{tl_version}
License:        LPPL 1.3
Summary:        Dark color themes for beamer
Version:        svn35101.0.4.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(beamercolorthemecormorant.sty) = %{tl_version}
Provides:       tex(beamercolorthemefrigatebird.sty) = %{tl_version}
Provides:       tex(beamercolorthememagpie.sty) = %{tl_version}

%description -n texlive-beamerdarkthemes
A package with three dark color themes for beamer, designed for
presentations with pictures and/or for bright rooms without
screen. These themes mix one dominant foreground colour and a
black background. Cormorant stands for green, frigatebird for
red and magpie for blue.

%package -n texlive-beamerdarkthemes-doc
Summary:        Documentation for beamerdarkthemes
Version:        svn35101.0.4.1

Provides:       tex-beamerdarkthemes-doc
AutoReqProv:    No

%description -n texlive-beamerdarkthemes-doc
Documentation for beamerdarkthemes

%package -n texlive-beamer-FUBerlin-doc
Summary:        Documentation for beamer-FUBerlin
Version:        svn38159.0.02b

Provides:       tex-beamer-FUBerlin-doc, tex-beamer-FUBerlin
Provides:       texlive-beamer-FUBerlin
AutoReqProv:    No

%description -n texlive-beamer-FUBerlin-doc
Documentation for beamer-FUBerlin

%package -n texlive-beamerposter
Provides:       tex-beamerposter = %{tl_version}
License:        LPPL
Summary:        Extend beamer and a0poster for custom sized posters
Version:        svn47508
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xkeyval.sty), tex(type1cm.sty), tex(fp.sty)
Provides:       tex(beamerposter.sty) = %{tl_version}

%description -n texlive-beamerposter
The package enables the user to use beamer style operations on
a canvas of the sizes provided by a0poster; font scaling is
available (using packages such as type1cm if necessary). In
addition, the package allows the user to benefit from the nice
colour box handling and alignment provided by the beamer class
(for example, with rounded corners and shadows). Good looking
posters may be created very rapidly. Features include: scalable
fonts using the fp and type1cm packages; posters in A-series
sizes, and custom sizes like double A0 are possible; still
applicable to custom beamer slides, e.g. 16:9 slides for a wide-
screen (i.e. 1.78 aspect ratio); orientation may be portrait or
landscape; a 'debug mode' is provided.

%package -n texlive-beamerposter-doc
Summary:        Documentation for beamerposter
Version:        svn47508
Provides:       tex-beamerposter-doc
AutoReqProv:    No

%description -n texlive-beamerposter-doc
Documentation for beamerposter

%package -n texlive-beamersubframe
Provides:       tex-beamersubframe = %{tl_version}
License:        LPPL
Summary:        Reorder frames in the PDF file
Version:        svn23510.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(verbatim.sty)
Provides:       tex(beamersubframe.sty) = %{tl_version}

%description -n texlive-beamersubframe
The package provides a method to reorder frames in the PDF file
without reordering the source. Its principal use is to embed or
append frames with details on some subject. The author
describes the package as "experimental".

%package -n texlive-beamersubframe-doc
Summary:        Documentation for beamersubframe
Version:        svn23510.0.2

Provides:       tex-beamersubframe-doc
AutoReqProv:    No

%description -n texlive-beamersubframe-doc
Documentation for beamersubframe

%package -n texlive-beamerthemejltree
Provides:       tex-beamerthemejltree = %{tl_version}
License:        GPL+
Summary:        Contributed beamer theme
Version:        svn21977.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(beamerthemeJLTree.sty) = %{tl_version}

%description -n texlive-beamerthemejltree
A theme for beamer presentations.

%package -n texlive-beamerthemenirma
Provides:       tex-beamerthemenirma = %{tl_version}
License:        LPPL
Summary:        A Beamer theme for academic presentations
Version:        svn20765.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(beamerbasethemes.sty), tex(pgf.sty)
Provides:       tex(beamerthemenirma.sty) = %{tl_version}

%description -n texlive-beamerthemenirma
The package developed for academic purposes. The distribution
includes nothing more than style file needed for preparing
presentations.

%package -n texlive-beamerthemenirma-doc
Summary:        Documentation for beamerthemenirma
Version:        svn20765.0.1

Provides:       tex-beamerthemenirma-doc
AutoReqProv:    No

%description -n texlive-beamerthemenirma-doc
Documentation for beamerthemenirma

%package -n texlive-beamertheme-phnompenh
Provides:       tex-beamertheme-phnompenh = %{tl_version}
Provides:       tex-beamerthemephnompenh = %{tl_version}
Provides:       beamerthemephnompenh = %{tl_version}
Obsoletes:      beamerthemephnompenh < 2016
License:        LPPL
Summary:        beamertheme-phnompenh package
Version:        svn39100

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(beamerthemePhnomPenh.sty) = %{tl_version}

%description -n texlive-beamertheme-phnompenh
beamertheme-phnompenh package

%package -n texlive-beamertheme-phnompenh-doc
Summary:        Documentation for beamertheme-phnompenh
Version:        svn39100

Provides:       tex-beamerthemephnompenh-doc, tex-beamertheme-phnompenh-doc
Provides:       beamerthemephnompenh-doc = %{tl_version}
Obsoletes:      beamerthemephnompenh-doc < 2016
AutoReqProv:    No

%description -n texlive-beamertheme-phnompenh-doc
Documentation for beamertheme-phnompenh

%package -n texlive-beamertheme-upenn-bc
Provides:       tex-beamertheme-upenn-bc = %{tl_version}
License:        LPPL
Summary:        Beamer themies for Boston College and the University of Pennsylvania
Version:        svn29937.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(beamercolorthemegoeagles.sty) = %{tl_version}
Provides:       tex(beamercolorthemepenn.sty) = %{tl_version}

%description -n texlive-beamertheme-upenn-bc
Beamer themes in the colors of the University of Pennsylvania,
USA, and Boston College, USA. Both were tested for the
presentation theme 'Warsaw. Please note that these color themes
are neither official nor exact! The colours are approximated
from the universities' style guidelines and websites, and
slightly modified where necessary to generate an appealing
look. The universities neither endorse, nor provide any support
for, these color themes. I give no warranty for the code.

%package -n texlive-beamertheme-upenn-bc-doc
Summary:        Documentation for beamertheme-upenn-bc
Version:        svn29937.1.0

Provides:       tex-beamertheme-upenn-bc-doc
AutoReqProv:    No

%description -n texlive-beamertheme-upenn-bc-doc
Documentation for beamertheme-upenn-bc

%package -n texlive-beamer
Provides:       tex-beamer = %{tl_version}
License:        LPPL 1.3
Summary:        A LaTeX class for producing presentations and slides
Version:        svn46705
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-pgf, tex-xcolor, tex(beamerbasemodes.sty), tex(ifpdf.sty)
Requires:       tex(ucs.sty), tex(inputenc.sty), tex(geometry.sty), tex(pgfcore.sty)
Requires:       tex(xxcolor.sty), tex(atbegshi.sty), tex(hyperref.sty), tex(beamerbasearticle.sty)
Requires:       tex(xcolor.sty), tex(amssymb.sty), tex(sansmathaccent.sty), tex(enumerate.sty)
Requires:       tex(keyval.sty), tex(beamerbasetwoscreens.sty)
Requires:       tex(beamerbasesection.sty), tex(beamerbasetoc.sty)
Requires:       tex(beamerbasetheorems.sty), tex(amsmath.sty)
Requires:       tex(amsthm.sty), tex(pgf.sty), tex(translator.sty)
Provides:       tex(beamericonarticle.tex) = %{tl_version}
Provides:       tex(beamericonbook.tex) = %{tl_version}, tex(beamer.cls) = %{tl_version}
Provides:       tex(beamerarticle.sty) = %{tl_version}, tex(beamerbasearticle.sty) = %{tl_version}
Provides:       tex(beamerbaseauxtemplates.sty) = %{tl_version}
Provides:       tex(beamerbaseboxes.sty) = %{tl_version}
Provides:       tex(beamerbasecolor.sty) = %{tl_version}
Provides:       tex(beamerbasecompatibility.sty) = %{tl_version}
Provides:       tex(beamerbasedecode.sty) = %{tl_version}
Provides:       tex(beamerbaseexercise.sty) = %{tl_version}
Provides:       tex(beamerbasefont.sty) = %{tl_version}, tex(beamerbaseframe.sty) = %{tl_version}
Provides:       tex(beamerbaseframecomponents.sty) = %{tl_version}
Provides:       tex(beamerbaseframesize.sty) = %{tl_version}
Provides:       tex(beamerbaselocalstructure.sty) = %{tl_version}
Provides:       tex(beamerbasemisc.sty) = %{tl_version}, tex(beamerbasemodes.sty) = %{tl_version}
Provides:       tex(beamerbasenavigation.sty) = %{tl_version}
Provides:       tex(beamerbasenotes.sty) = %{tl_version}
Provides:       tex(beamerbaseoptions.sty) = %{tl_version}
Provides:       tex(beamerbaseoverlay.sty) = %{tl_version}
Provides:       tex(beamerbasercs.sty) = %{tl_version}, tex(beamerbaserequires.sty) = %{tl_version}
Provides:       tex(beamerbasesection.sty) = %{tl_version}
Provides:       tex(beamerbasetemplates.sty) = %{tl_version}
Provides:       tex(beamerbasethemes.sty) = %{tl_version}
Provides:       tex(beamerbasetheorems.sty) = %{tl_version}
Provides:       tex(beamerbasetitle.sty) = %{tl_version}
Provides:       tex(beamerbasetoc.sty) = %{tl_version}, tex(beamerbasetranslator.sty) = %{tl_version}
Provides:       tex(beamerbasetwoscreens.sty) = %{tl_version}
Provides:       tex(beamerbaseverbatim.sty) = %{tl_version}
Provides:       tex(beamerfoils.sty) = %{tl_version}, tex(beamerprosper.sty) = %{tl_version}
Provides:       tex(beamerseminar.sty) = %{tl_version}, tex(beamertexpower.sty) = %{tl_version}
Provides:       tex(beamerexample-foils.tex) = %{tl_version}
Provides:       tex(beamerexample-prosper.tex) = %{tl_version}
Provides:       tex(beamerexample-seminar.tex) = %{tl_version}
Provides:       tex(beamerexample-texpower.tex) = %{tl_version}
Provides:       tex(multimedia.sty) = %{tl_version}, tex(multimediasymbols.sty) = %{tl_version}
Provides:       tex(xmpmulti.sty) = %{tl_version}, tex(beamercolorthemealbatross.sty) = %{tl_version}
Provides:       tex(beamercolorthemebeaver.sty) = %{tl_version}
Provides:       tex(beamercolorthemebeetle.sty) = %{tl_version}
Provides:       tex(beamercolorthemecrane.sty) = %{tl_version}
Provides:       tex(beamercolorthemedefault.sty) = %{tl_version}
Provides:       tex(beamercolorthemedolphin.sty) = %{tl_version}
Provides:       tex(beamercolorthemedove.sty) = %{tl_version}
Provides:       tex(beamercolorthemefly.sty) = %{tl_version}
Provides:       tex(beamercolorthemelily.sty) = %{tl_version}
Provides:       tex(beamercolorthememonarca.sty) = %{tl_version}
Provides:       tex(beamercolorthemeorchid.sty) = %{tl_version}
Provides:       tex(beamercolorthemerose.sty) = %{tl_version}
Provides:       tex(beamercolorthemeseagull.sty) = %{tl_version}
Provides:       tex(beamercolorthemeseahorse.sty) = %{tl_version}
Provides:       tex(beamercolorthemesidebartab.sty) = %{tl_version}
Provides:       tex(beamercolorthemespruce.sty) = %{tl_version}
Provides:       tex(beamercolorthemestructure.sty) = %{tl_version}
Provides:       tex(beamercolorthemewhale.sty) = %{tl_version}
Provides:       tex(beamercolorthemewolverine.sty) = %{tl_version}
Provides:       tex(beamerfontthemedefault.sty) = %{tl_version}
Provides:       tex(beamerfontthemeprofessionalfonts.sty) = %{tl_version}
Provides:       tex(beamerfontthemeserif.sty) = %{tl_version}
Provides:       tex(beamerfontthemestructurebold.sty) = %{tl_version}
Provides:       tex(beamerfontthemestructureitalicserif.sty) = %{tl_version}
Provides:       tex(beamerfontthemestructuresmallcapsserif.sty) = %{tl_version}
Provides:       tex(beamerinnerthemecircles.sty) = %{tl_version}
Provides:       tex(beamerinnerthemedefault.sty) = %{tl_version}
Provides:       tex(beamerinnerthemeinmargin.sty) = %{tl_version}
Provides:       tex(beamerinnerthemerectangles.sty) = %{tl_version}
Provides:       tex(beamerinnerthemerounded.sty) = %{tl_version}
Provides:       tex(beamerouterthemedefault.sty) = %{tl_version}
Provides:       tex(beamerouterthemeinfolines.sty) = %{tl_version}
Provides:       tex(beamerouterthememiniframes.sty) = %{tl_version}
Provides:       tex(beamerouterthemeshadow.sty) = %{tl_version}
Provides:       tex(beamerouterthemesidebar.sty) = %{tl_version}
Provides:       tex(beamerouterthemesmoothbars.sty) = %{tl_version}
Provides:       tex(beamerouterthemesmoothtree.sty) = %{tl_version}
Provides:       tex(beamerouterthemesplit.sty) = %{tl_version}
Provides:       tex(beamerouterthemetree.sty) = %{tl_version}
Provides:       tex(beamerthemeAnnArbor.sty) = %{tl_version}
Provides:       tex(beamerthemeAntibes.sty) = %{tl_version}
Provides:       tex(beamerthemeBergen.sty) = %{tl_version}
Provides:       tex(beamerthemeBerkeley.sty) = %{tl_version}
Provides:       tex(beamerthemeBerlin.sty) = %{tl_version}
Provides:       tex(beamerthemeBoadilla.sty) = %{tl_version}
Provides:       tex(beamerthemeCambridgeUS.sty) = %{tl_version}
Provides:       tex(beamerthemeCopenhagen.sty) = %{tl_version}
Provides:       tex(beamerthemeDarmstadt.sty) = %{tl_version}
Provides:       tex(beamerthemeDresden.sty) = %{tl_version}
Provides:       tex(beamerthemeEastLansing.sty) = %{tl_version}
Provides:       tex(beamerthemeFrankfurt.sty) = %{tl_version}
Provides:       tex(beamerthemeGoettingen.sty) = %{tl_version}
Provides:       tex(beamerthemeHannover.sty) = %{tl_version}
Provides:       tex(beamerthemeIlmenau.sty) = %{tl_version}
Provides:       tex(beamerthemeJuanLesPins.sty) = %{tl_version}
Provides:       tex(beamerthemeLuebeck.sty) = %{tl_version}
Provides:       tex(beamerthemeMadrid.sty) = %{tl_version}
Provides:       tex(beamerthemeMalmoe.sty) = %{tl_version}
Provides:       tex(beamerthemeMarburg.sty) = %{tl_version}
Provides:       tex(beamerthemeMontpellier.sty) = %{tl_version}
Provides:       tex(beamerthemePaloAlto.sty) = %{tl_version}
Provides:       tex(beamerthemePittsburgh.sty) = %{tl_version}
Provides:       tex(beamerthemeRochester.sty) = %{tl_version}
Provides:       tex(beamerthemeSingapore.sty) = %{tl_version}
Provides:       tex(beamerthemeSzeged.sty) = %{tl_version}
Provides:       tex(beamerthemeWarsaw.sty) = %{tl_version}
Provides:       tex(beamerthemeboxes.sty) = %{tl_version}
Provides:       tex(beamerthemedefault.sty) = %{tl_version}
Provides:       tex(beamerthemebars.sty) = %{tl_version}
Provides:       tex(beamerthemeclassic.sty) = %{tl_version}
Provides:       tex(beamerthemecompatibility.sty) = %{tl_version}
Provides:       tex(beamerthemelined.sty) = %{tl_version}
Provides:       tex(beamerthemeplain.sty) = %{tl_version}
Provides:       tex(beamerthemeshadow.sty) = %{tl_version}
Provides:       tex(beamerthemesidebar.sty) = %{tl_version}
Provides:       tex(beamerthemesplit.sty) = %{tl_version}
Provides:       tex(beamerthemetree.sty) = %{tl_version}
Provides:       tex(translator-language-mappings.tex) = %{tl_version}

%description -n texlive-beamer
The beamer LaTeX class can be used for producing slides. Its
functionality is similar to Prosper but does not need any
external programs and can directly produce a presentation using
pdflatex. Beamer uses pgf for pdf/ps independent graphics.
Frames are created using \frame{...}, and a frame can build
multiple slides through a simple notation for specifying
material for each slide within a frame. Beamer supports
bibliographies, appendicies and transitions. Short versions of
title, authors, institute can also be specified as optional
parameters. A \plainframe{} allows a picture, for example, to
fill the whole frame. Support figure and table environments,
transparency effects, a \transduration command, animation
commands, a pauses environment. Beamer also provides
compatibility with other packages like prosper. The package now
incorporates the functionality of the former translator
package, which is used for customising the package for use in
other language environments.

%package -n texlive-beamer-doc
Summary:        Documentation for beamer
Version:        svn46705
Provides:       tex-beamer-doc
AutoReqProv:    No
Requires:       tex-pgf-doc, tex-xcolor-doc

%description -n texlive-beamer-doc
Documentation for beamer

%package -n texlive-beamer-tut-pt-doc
Summary:        Documentation for beamer-tut-pt
Version:        svn15878.0

Provides:       tex-beamer-tut-pt-doc
AutoReqProv:    No

%description -n texlive-beamer-tut-pt-doc
Documentation for beamer-tut-pt

%package -n texlive-beebe
Provides:       tex-beebe = %{tl_version}
License:        LPPL
Summary:        A collection of bibliographies
Version:        svn46314
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(bibnames.sty) = %{tl_version}, tex(texnames.sty) = %{tl_version}
Provides:       tex(tugboat.def) = %{tl_version}

%description -n texlive-beebe
A collection of BibTeX bibliographies on TeX-related topics
(including, for example, spell-checking and SGML). Each
includes a LaTeX wrapper file to typeset the bibliography.

%package -n texlive-begingreek
Provides:       tex-begingreek = %{tl_version}
License:        LPPL 1.3
Summary:        Greek environment to be used with pdflatex only
Version:        svn36294.1.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(begingreek.sty) = %{tl_version}

%description -n texlive-begingreek
This simple package defines a greek environment to be used with
pdfLaTeX only, that accepts an optional Greek font family name
to type its contents with. A similar \greektxt command does a
similar action for shorter texts.

%package -n texlive-begingreek-doc
Summary:        Documentation for begingreek
Version:        svn36294.1.5

Provides:       tex-begingreek-doc
AutoReqProv:    No

%description -n texlive-begingreek-doc
Documentation for begingreek

%package -n texlive-begriff
Provides:       tex-begriff = %{tl_version}
License:        GPL+
Summary:        Typeset Begriffschrift
Version:        svn15878.1.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(begriff.sty) = %{tl_version}

%description -n texlive-begriff
The package defines maths mode commands for typesetting Frege's
Begriffschrift.

%package -n texlive-begriff-doc
Summary:        Documentation for begriff
Version:        svn15878.1.6

Provides:       tex-begriff-doc
AutoReqProv:    No

%description -n texlive-begriff-doc
Documentation for begriff

%package -n texlive-belleek
Provides:       tex-belleek = %{tl_version}
License:        Public Domain
Summary:        Free replacement for basic MathTime fonts
Version:        svn18651.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(belleek.map) = %{tl_version}, tex(blex.ttf) = %{tl_version}
Provides:       tex(blsy.ttf) = %{tl_version}, tex(rblmi.ttf) = %{tl_version}
Provides:       tex(blex.pfb) = %{tl_version}, tex(blsy.pfb) = %{tl_version}
Provides:       tex(rblmi.pfb) = %{tl_version}

%description -n texlive-belleek
This package replaces the original MathTime fonts, not MathTime-
Plus or MathTime Professional (the last being the only
currently available commercial bundle).

%package -n texlive-belleek-doc
Summary:        Documentation for belleek
Version:        svn18651.0

Provides:       tex-belleek-doc
AutoReqProv:    No

%description -n texlive-belleek-doc
Documentation for belleek

%package -n texlive-bengali
Provides:       tex-bengali = %{tl_version}
License:        LPPL
Summary:        Support for the Bengali language
Version:        svn20987.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bnr10.tfm) = %{tl_version}, tex(bnsl10.tfm) = %{tl_version}
Provides:       tex(xbnr10.tfm) = %{tl_version}, tex(xbnsl10.tfm) = %{tl_version}
Provides:       tex(beng.sty) = %{tl_version}, tex(ubn.fd) = %{tl_version}
Provides:       tex(ubnx.fd) = %{tl_version}

%description -n texlive-bengali
The package is based on Velthuis' transliteration scheme, with
extensions to deal with the Bengali letters that are not in
Devanagari. The package also supports Assamese.

%package -n texlive-bengali-doc
Summary:        Documentation for bengali
Version:        svn20987.0

Provides:       tex-bengali-doc
AutoReqProv:    No

%description -n texlive-bengali-doc
Documentation for bengali

%package -n texlive-bera
Provides:       tex-bera = %{tl_version}
License:        Bitstream vera
Summary:        Bera fonts
Version:        svn20031.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(fontenc.sty), tex(textcomp.sty), tex(berasans.sty), tex(keyval.sty)
Provides:       tex(bera.map) = %{tl_version}, tex(fveb8a.tfm) = %{tl_version}
Provides:       tex(fveb8c.tfm) = %{tl_version}, tex(fveb8r.tfm) = %{tl_version}
Provides:       tex(fveb8t.tfm) = %{tl_version}, tex(fvebo8c.tfm) = %{tl_version}
Provides:       tex(fvebo8r.tfm) = %{tl_version}, tex(fvebo8t.tfm) = %{tl_version}
Provides:       tex(fver8a.tfm) = %{tl_version}, tex(fver8c.tfm) = %{tl_version}
Provides:       tex(fver8r.tfm) = %{tl_version}, tex(fver8t.tfm) = %{tl_version}
Provides:       tex(fvero8c.tfm) = %{tl_version}, tex(fvero8r.tfm) = %{tl_version}
Provides:       tex(fvero8t.tfm) = %{tl_version}, tex(fvmb8a.tfm) = %{tl_version}
Provides:       tex(fvmb8c.tfm) = %{tl_version}, tex(fvmb8r.tfm) = %{tl_version}
Provides:       tex(fvmb8t.tfm) = %{tl_version}, tex(fvmbo8a.tfm) = %{tl_version}
Provides:       tex(fvmbo8c.tfm) = %{tl_version}, tex(fvmbo8r.tfm) = %{tl_version}
Provides:       tex(fvmbo8t.tfm) = %{tl_version}, tex(fvmr8a.tfm) = %{tl_version}
Provides:       tex(fvmr8c.tfm) = %{tl_version}, tex(fvmr8r.tfm) = %{tl_version}
Provides:       tex(fvmr8t.tfm) = %{tl_version}, tex(fvmro8a.tfm) = %{tl_version}
Provides:       tex(fvmro8c.tfm) = %{tl_version}, tex(fvmro8r.tfm) = %{tl_version}
Provides:       tex(fvmro8t.tfm) = %{tl_version}, tex(fvsb8a.tfm) = %{tl_version}
Provides:       tex(fvsb8c.tfm) = %{tl_version}, tex(fvsb8r.tfm) = %{tl_version}
Provides:       tex(fvsb8t.tfm) = %{tl_version}, tex(fvsbo8a.tfm) = %{tl_version}
Provides:       tex(fvsbo8c.tfm) = %{tl_version}, tex(fvsbo8r.tfm) = %{tl_version}
Provides:       tex(fvsbo8t.tfm) = %{tl_version}, tex(fvsr8a.tfm) = %{tl_version}
Provides:       tex(fvsr8c.tfm) = %{tl_version}, tex(fvsr8r.tfm) = %{tl_version}
Provides:       tex(fvsr8t.tfm) = %{tl_version}, tex(fvsro8a.tfm) = %{tl_version}
Provides:       tex(fvsro8c.tfm) = %{tl_version}, tex(fvsro8r.tfm) = %{tl_version}
Provides:       tex(fvsro8t.tfm) = %{tl_version}, tex(fveb8a.pfb) = %{tl_version}
Provides:       tex(fver8a.pfb) = %{tl_version}, tex(fvmb8a.pfb) = %{tl_version}
Provides:       tex(fvmbo8a.pfb) = %{tl_version}, tex(fvmr8a.pfb) = %{tl_version}
Provides:       tex(fvmro8a.pfb) = %{tl_version}, tex(fvsb8a.pfb) = %{tl_version}
Provides:       tex(fvsbo8a.pfb) = %{tl_version}, tex(fvsr8a.pfb) = %{tl_version}
Provides:       tex(fvsro8a.pfb) = %{tl_version}, tex(fveb8c.vf) = %{tl_version}
Provides:       tex(fveb8t.vf) = %{tl_version}, tex(fvebo8c.vf) = %{tl_version}
Provides:       tex(fvebo8t.vf) = %{tl_version}, tex(fver8c.vf) = %{tl_version}
Provides:       tex(fver8t.vf) = %{tl_version}, tex(fvero8c.vf) = %{tl_version}
Provides:       tex(fvero8t.vf) = %{tl_version}, tex(fvmb8c.vf) = %{tl_version}
Provides:       tex(fvmb8t.vf) = %{tl_version}, tex(fvmbo8c.vf) = %{tl_version}
Provides:       tex(fvmbo8t.vf) = %{tl_version}, tex(fvmr8c.vf) = %{tl_version}
Provides:       tex(fvmr8t.vf) = %{tl_version}, tex(fvmro8c.vf) = %{tl_version}
Provides:       tex(fvmro8t.vf) = %{tl_version}, tex(fvsb8c.vf) = %{tl_version}
Provides:       tex(fvsb8t.vf) = %{tl_version}, tex(fvsbo8c.vf) = %{tl_version}
Provides:       tex(fvsbo8t.vf) = %{tl_version}, tex(fvsr8c.vf) = %{tl_version}
Provides:       tex(fvsr8t.vf) = %{tl_version}, tex(fvsro8c.vf) = %{tl_version}
Provides:       tex(fvsro8t.vf) = %{tl_version}, tex(bera.sty) = %{tl_version}
Provides:       tex(beramono.sty) = %{tl_version}, tex(berasans.sty) = %{tl_version}
Provides:       tex(beraserif.sty) = %{tl_version}, tex(t1fve.fd) = %{tl_version}
Provides:       tex(t1fvm.fd) = %{tl_version}, tex(t1fvs.fd) = %{tl_version}
Provides:       tex(ts1fve.fd) = %{tl_version}, tex(ts1fvm.fd) = %{tl_version}
Provides:       tex(ts1fvs.fd) = %{tl_version}

%description -n texlive-bera
The package contains the Bera Type 1 fonts, and a zip archive
containing files to use the fonts with LaTeX. Bera is a set of
three font families: Bera Serif (a slab-serif Roman), Bera Sans
(a Frutiger descendant), and Bera Mono (monospaced/typewriter).
Support for use in LaTeX is also provided. The Bera family is a
repackaging, for use with TeX, of the Bitstream Vera family.

%package -n texlive-bera-doc
Summary:        Documentation for bera
Version:        svn20031.0

Provides:       tex-bera-doc
AutoReqProv:    No

%description -n texlive-bera-doc
Documentation for bera

%package -n texlive-berenisadf
Provides:       tex-berenisadf = %{tl_version}
License:        GPLv2+ and LPPL
Summary:        Berenis ADF fonts and TeX/LaTeX support
Version:        svn32215.1.004

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(xkeyval.sty), tex(nfssext-cfr.sty), tex(fontenc.sty), tex(textcomp.sty)
Provides:       tex(t1-ybd.enc) = %{tl_version}, tex(t1-ybd0.enc) = %{tl_version}
Provides:       tex(t1-ybd1.enc) = %{tl_version}, tex(t1-ybd2.enc) = %{tl_version}
Provides:       tex(t1-ybd2j.enc) = %{tl_version}, tex(t1-ybdj.enc) = %{tl_version}
Provides:       tex(texnansi-ybd.enc) = %{tl_version}, tex(texnansi-ybd0.enc) = %{tl_version}
Provides:       tex(texnansi-ybd1.enc) = %{tl_version}, tex(texnansi-ybd2.enc) = %{tl_version}
Provides:       tex(texnansi-ybd2j.enc) = %{tl_version}, tex(texnansi-ybdj.enc) = %{tl_version}
Provides:       tex(texnansx-ybd2jw.enc) = %{tl_version}
Provides:       tex(texnansx-ybd2w.enc) = %{tl_version}, tex(texnansx-ybdjw.enc) = %{tl_version}
Provides:       tex(texnansx-ybdw.enc) = %{tl_version}, tex(ts1-ybd.enc) = %{tl_version}
Provides:       tex(ts1-ybd0.enc) = %{tl_version}, tex(ts1-ybd1.enc) = %{tl_version}
Provides:       tex(ts1-ybd2.enc) = %{tl_version}, tex(ts1-ybd2j.enc) = %{tl_version}
Provides:       tex(ts1-ybdj.enc) = %{tl_version}, tex(ybd.map) = %{tl_version}
Provides:       tex(BerenisADFPro-Bold.otf) = %{tl_version}
Provides:       tex(BerenisADFPro-BoldItalic.otf) = %{tl_version}
Provides:       tex(BerenisADFPro-Italic.otf) = %{tl_version}
Provides:       tex(BerenisADFPro-Regular.otf) = %{tl_version}
Provides:       tex(BerenisADFProSC-Bold.otf) = %{tl_version}
Provides:       tex(BerenisADFProSC-BoldItalic.otf) = %{tl_version}
Provides:       tex(BerenisADFProSC-Italic.otf) = %{tl_version}
Provides:       tex(BerenisADFProSC-Regular.otf) = %{tl_version}
Provides:       tex(ybdb08c.tfm) = %{tl_version}, tex(ybdb08t.tfm) = %{tl_version}
Provides:       tex(ybdb08y.tfm) = %{tl_version}, tex(ybdb0c8c.tfm) = %{tl_version}
Provides:       tex(ybdb0c8t.tfm) = %{tl_version}, tex(ybdb0c8y.tfm) = %{tl_version}
Provides:       tex(ybdb0ci8c.tfm) = %{tl_version}, tex(ybdb0ci8t.tfm) = %{tl_version}
Provides:       tex(ybdb0ci8y.tfm) = %{tl_version}, tex(ybdb0i8c.tfm) = %{tl_version}
Provides:       tex(ybdb0i8t.tfm) = %{tl_version}, tex(ybdb0i8y.tfm) = %{tl_version}
Provides:       tex(ybdb18c.tfm) = %{tl_version}, tex(ybdb18t.tfm) = %{tl_version}
Provides:       tex(ybdb18y.tfm) = %{tl_version}, tex(ybdb1c8c.tfm) = %{tl_version}
Provides:       tex(ybdb1c8t.tfm) = %{tl_version}, tex(ybdb1c8y.tfm) = %{tl_version}
Provides:       tex(ybdb1ci8c.tfm) = %{tl_version}, tex(ybdb1ci8t.tfm) = %{tl_version}
Provides:       tex(ybdb1ci8y.tfm) = %{tl_version}, tex(ybdb1i8c.tfm) = %{tl_version}
Provides:       tex(ybdb1i8t.tfm) = %{tl_version}, tex(ybdb1i8y.tfm) = %{tl_version}
Provides:       tex(ybdb28c.tfm) = %{tl_version}, tex(ybdb28t.tfm) = %{tl_version}
Provides:       tex(ybdb28y.tfm) = %{tl_version}, tex(ybdb2c8c.tfm) = %{tl_version}
Provides:       tex(ybdb2c8t.tfm) = %{tl_version}, tex(ybdb2c8y.tfm) = %{tl_version}
Provides:       tex(ybdb2ci8c.tfm) = %{tl_version}, tex(ybdb2ci8t.tfm) = %{tl_version}
Provides:       tex(ybdb2ci8y.tfm) = %{tl_version}, tex(ybdb2cij8c.tfm) = %{tl_version}
Provides:       tex(ybdb2cij8t.tfm) = %{tl_version}, tex(ybdb2cij8y.tfm) = %{tl_version}
Provides:       tex(ybdb2cijw8y.tfm) = %{tl_version}, tex(ybdb2ciw8y.tfm) = %{tl_version}
Provides:       tex(ybdb2cj8c.tfm) = %{tl_version}, tex(ybdb2cj8t.tfm) = %{tl_version}
Provides:       tex(ybdb2cj8y.tfm) = %{tl_version}, tex(ybdb2cjw8y.tfm) = %{tl_version}
Provides:       tex(ybdb2cw8y.tfm) = %{tl_version}, tex(ybdb2i8c.tfm) = %{tl_version}
Provides:       tex(ybdb2i8t.tfm) = %{tl_version}, tex(ybdb2i8y.tfm) = %{tl_version}
Provides:       tex(ybdb2ij8c.tfm) = %{tl_version}, tex(ybdb2ij8t.tfm) = %{tl_version}
Provides:       tex(ybdb2ij8y.tfm) = %{tl_version}, tex(ybdb2ijw8y.tfm) = %{tl_version}
Provides:       tex(ybdb2iw8y.tfm) = %{tl_version}, tex(ybdb2j8c.tfm) = %{tl_version}
Provides:       tex(ybdb2j8t.tfm) = %{tl_version}, tex(ybdb2j8y.tfm) = %{tl_version}
Provides:       tex(ybdb2jw8y.tfm) = %{tl_version}, tex(ybdb2w8y.tfm) = %{tl_version}
Provides:       tex(ybdb8c.tfm) = %{tl_version}, tex(ybdb8t.tfm) = %{tl_version}
Provides:       tex(ybdb8y.tfm) = %{tl_version}, tex(ybdbc8c.tfm) = %{tl_version}
Provides:       tex(ybdbc8t.tfm) = %{tl_version}, tex(ybdbc8y.tfm) = %{tl_version}
Provides:       tex(ybdbci8c.tfm) = %{tl_version}, tex(ybdbci8t.tfm) = %{tl_version}
Provides:       tex(ybdbci8y.tfm) = %{tl_version}, tex(ybdbcij8c.tfm) = %{tl_version}
Provides:       tex(ybdbcij8t.tfm) = %{tl_version}, tex(ybdbcij8y.tfm) = %{tl_version}
Provides:       tex(ybdbcijw8y.tfm) = %{tl_version}, tex(ybdbciw8y.tfm) = %{tl_version}
Provides:       tex(ybdbcj8c.tfm) = %{tl_version}, tex(ybdbcj8t.tfm) = %{tl_version}
Provides:       tex(ybdbcj8y.tfm) = %{tl_version}, tex(ybdbcjw8y.tfm) = %{tl_version}
Provides:       tex(ybdbcw8y.tfm) = %{tl_version}, tex(ybdbi8c.tfm) = %{tl_version}
Provides:       tex(ybdbi8t.tfm) = %{tl_version}, tex(ybdbi8y.tfm) = %{tl_version}
Provides:       tex(ybdbij8c.tfm) = %{tl_version}, tex(ybdbij8t.tfm) = %{tl_version}
Provides:       tex(ybdbij8y.tfm) = %{tl_version}, tex(ybdbijw8y.tfm) = %{tl_version}
Provides:       tex(ybdbiw8y.tfm) = %{tl_version}, tex(ybdbj8c.tfm) = %{tl_version}
Provides:       tex(ybdbj8t.tfm) = %{tl_version}, tex(ybdbj8y.tfm) = %{tl_version}
Provides:       tex(ybdbjw8y.tfm) = %{tl_version}, tex(ybdbw8y.tfm) = %{tl_version}
Provides:       tex(ybdr08c.tfm) = %{tl_version}, tex(ybdr08t.tfm) = %{tl_version}
Provides:       tex(ybdr08y.tfm) = %{tl_version}, tex(ybdr0c8c.tfm) = %{tl_version}
Provides:       tex(ybdr0c8t.tfm) = %{tl_version}, tex(ybdr0c8y.tfm) = %{tl_version}
Provides:       tex(ybdr0ci8c.tfm) = %{tl_version}, tex(ybdr0ci8t.tfm) = %{tl_version}
Provides:       tex(ybdr0ci8y.tfm) = %{tl_version}, tex(ybdr0i8c.tfm) = %{tl_version}
Provides:       tex(ybdr0i8t.tfm) = %{tl_version}, tex(ybdr0i8y.tfm) = %{tl_version}
Provides:       tex(ybdr18c.tfm) = %{tl_version}, tex(ybdr18t.tfm) = %{tl_version}
Provides:       tex(ybdr18y.tfm) = %{tl_version}, tex(ybdr1c8c.tfm) = %{tl_version}
Provides:       tex(ybdr1c8t.tfm) = %{tl_version}, tex(ybdr1c8y.tfm) = %{tl_version}
Provides:       tex(ybdr1ci8c.tfm) = %{tl_version}, tex(ybdr1ci8t.tfm) = %{tl_version}
Provides:       tex(ybdr1ci8y.tfm) = %{tl_version}, tex(ybdr1i8c.tfm) = %{tl_version}
Provides:       tex(ybdr1i8t.tfm) = %{tl_version}, tex(ybdr1i8y.tfm) = %{tl_version}
Provides:       tex(ybdr28c.tfm) = %{tl_version}, tex(ybdr28t.tfm) = %{tl_version}
Provides:       tex(ybdr28y.tfm) = %{tl_version}, tex(ybdr2c8c.tfm) = %{tl_version}
Provides:       tex(ybdr2c8t.tfm) = %{tl_version}, tex(ybdr2c8y.tfm) = %{tl_version}
Provides:       tex(ybdr2ci8c.tfm) = %{tl_version}, tex(ybdr2ci8t.tfm) = %{tl_version}
Provides:       tex(ybdr2ci8y.tfm) = %{tl_version}, tex(ybdr2cij8c.tfm) = %{tl_version}
Provides:       tex(ybdr2cij8t.tfm) = %{tl_version}, tex(ybdr2cij8y.tfm) = %{tl_version}
Provides:       tex(ybdr2cijw8y.tfm) = %{tl_version}, tex(ybdr2ciw8y.tfm) = %{tl_version}
Provides:       tex(ybdr2cj8c.tfm) = %{tl_version}, tex(ybdr2cj8t.tfm) = %{tl_version}
Provides:       tex(ybdr2cj8y.tfm) = %{tl_version}, tex(ybdr2cjw8y.tfm) = %{tl_version}
Provides:       tex(ybdr2cw8y.tfm) = %{tl_version}, tex(ybdr2i8c.tfm) = %{tl_version}
Provides:       tex(ybdr2i8t.tfm) = %{tl_version}, tex(ybdr2i8y.tfm) = %{tl_version}
Provides:       tex(ybdr2ij8c.tfm) = %{tl_version}, tex(ybdr2ij8t.tfm) = %{tl_version}
Provides:       tex(ybdr2ij8y.tfm) = %{tl_version}, tex(ybdr2ijw8y.tfm) = %{tl_version}
Provides:       tex(ybdr2iw8y.tfm) = %{tl_version}, tex(ybdr2j8c.tfm) = %{tl_version}
Provides:       tex(ybdr2j8t.tfm) = %{tl_version}, tex(ybdr2j8y.tfm) = %{tl_version}
Provides:       tex(ybdr2jw8y.tfm) = %{tl_version}, tex(ybdr2w8y.tfm) = %{tl_version}
Provides:       tex(ybdr8c.tfm) = %{tl_version}, tex(ybdr8t.tfm) = %{tl_version}
Provides:       tex(ybdr8y.tfm) = %{tl_version}, tex(ybdrc8c.tfm) = %{tl_version}
Provides:       tex(ybdrc8t.tfm) = %{tl_version}, tex(ybdrc8y.tfm) = %{tl_version}
Provides:       tex(ybdrci8c.tfm) = %{tl_version}, tex(ybdrci8t.tfm) = %{tl_version}
Provides:       tex(ybdrci8y.tfm) = %{tl_version}, tex(ybdrcij8c.tfm) = %{tl_version}
Provides:       tex(ybdrcij8t.tfm) = %{tl_version}, tex(ybdrcij8y.tfm) = %{tl_version}
Provides:       tex(ybdrcijw8y.tfm) = %{tl_version}, tex(ybdrciw8y.tfm) = %{tl_version}
Provides:       tex(ybdrcj8c.tfm) = %{tl_version}, tex(ybdrcj8t.tfm) = %{tl_version}
Provides:       tex(ybdrcj8y.tfm) = %{tl_version}, tex(ybdrcjw8y.tfm) = %{tl_version}
Provides:       tex(ybdrcw8y.tfm) = %{tl_version}, tex(ybdri8c.tfm) = %{tl_version}
Provides:       tex(ybdri8t.tfm) = %{tl_version}, tex(ybdri8y.tfm) = %{tl_version}
Provides:       tex(ybdrij8c.tfm) = %{tl_version}, tex(ybdrij8t.tfm) = %{tl_version}
Provides:       tex(ybdrij8y.tfm) = %{tl_version}, tex(ybdrijw8y.tfm) = %{tl_version}
Provides:       tex(ybdriw8y.tfm) = %{tl_version}, tex(ybdrj8c.tfm) = %{tl_version}
Provides:       tex(ybdrj8t.tfm) = %{tl_version}, tex(ybdrj8y.tfm) = %{tl_version}
Provides:       tex(ybdrjw8y.tfm) = %{tl_version}, tex(ybdrw8y.tfm) = %{tl_version}
Provides:       tex(ybdb.pfb) = %{tl_version}, tex(ybdbc.pfb) = %{tl_version}
Provides:       tex(ybdbci.pfb) = %{tl_version}, tex(ybdbi.pfb) = %{tl_version}
Provides:       tex(ybdr.pfb) = %{tl_version}, tex(ybdrc.pfb) = %{tl_version}
Provides:       tex(ybdrci.pfb) = %{tl_version}, tex(ybdri.pfb) = %{tl_version}
Provides:       tex(berenis.sty) = %{tl_version}, tex(ly1ybd.fd) = %{tl_version}
Provides:       tex(ly1ybd0.fd) = %{tl_version}, tex(ly1ybd1.fd) = %{tl_version}
Provides:       tex(ly1ybd2.fd) = %{tl_version}, tex(ly1ybd2j.fd) = %{tl_version}
Provides:       tex(ly1ybd2jw.fd) = %{tl_version}, tex(ly1ybd2w.fd) = %{tl_version}
Provides:       tex(ly1ybdj.fd) = %{tl_version}, tex(ly1ybdjw.fd) = %{tl_version}
Provides:       tex(ly1ybdw.fd) = %{tl_version}, tex(t1ybd.fd) = %{tl_version}
Provides:       tex(t1ybd0.fd) = %{tl_version}, tex(t1ybd1.fd) = %{tl_version}
Provides:       tex(t1ybd2.fd) = %{tl_version}, tex(t1ybd2j.fd) = %{tl_version}
Provides:       tex(t1ybdj.fd) = %{tl_version}, tex(ts1ybd.fd) = %{tl_version}
Provides:       tex(ts1ybd0.fd) = %{tl_version}, tex(ts1ybd1.fd) = %{tl_version}
Provides:       tex(ts1ybd2.fd) = %{tl_version}, tex(ts1ybd2j.fd) = %{tl_version}
Provides:       tex(ts1ybdj.fd) = %{tl_version}

%description -n texlive-berenisadf
The bundle provides the BerenisADF Pro font collection, in
OpenType and PostScript Type 1 formats, together with support
files to use the fonts in TeXnANSI (LY1) and LaTeX standard T1
and TS1 encodings.

%package -n texlive-berenisadf-doc
Summary:        Documentation for berenisadf
Version:        svn32215.1.004

Provides:       tex-berenisadf-doc
AutoReqProv:    No

%description -n texlive-berenisadf-doc
Documentation for berenisadf

%package -n texlive-besjournals
Provides:       tex-besjournals = %{tl_version}
License:        LPPL
Summary:        besjournals package
Version:        svn45662
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

%description -n texlive-besjournals
besjournals package

%package -n texlive-besjournals-doc
Summary:        Documentation for besjournals
Version:        svn45662
Provides:       tex-besjournals-doc
AutoReqProv:    No

%description -n texlive-besjournals-doc
Documentation for besjournals

%package -n texlive-betababel
Provides:       tex-betababel = %{tl_version}
License:        LPPL
Summary:        Insert ancient greek text coded in Beta Code
Version:        svn15878.0.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(babel.sty), tex(teubner.sty)
Provides:       tex(betababel.sty) = %{tl_version}

%description -n texlive-betababel
The betababel package extends the babel polutonikogreek option
to provide a simple way to insert ancient Greek texts with
diacritical characters into your document using the commonly
used Beta Code transliteration. You can directly insert Beta
Code texts -- as they can be found at the Perseus project, for
example -- without modification.

%package -n texlive-betababel-doc
Summary:        Documentation for betababel
Version:        svn15878.0.5

Provides:       tex-betababel-doc
AutoReqProv:    No

%description -n texlive-betababel-doc
Documentation for betababel

%package -n texlive-beton
Provides:       tex-beton = %{tl_version}
License:        LPPL
Summary:        Use Concrete fonts
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(beton.sty) = %{tl_version}

%description -n texlive-beton
Typeset a LaTeX2e document with the Concrete fonts designed by
Don Knuth and used in his book "Concrete Mathematics".

%package -n texlive-beton-doc
Summary:        Documentation for beton
Version:        svn15878.0

Provides:       tex-beton-doc
AutoReqProv:    No

%description -n texlive-beton-doc
Documentation for beton

%package -n texlive-bewerbung
Provides:       tex-bewerbung = %{tl_version}
License:        LPPL 1.3
Summary:        Typesetting job application
Version:        svn37880.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(marvosym.sty), tex(geometry.sty), tex(datatool.sty), tex(eurosym.sty)
Requires:       tex(xspace.sty), tex(multicol.sty), tex(pdfpages.sty), tex(comment.sty)
Requires:       tex(xparse.sty), tex(longtable.sty), tex(booktabs.sty), tex(array.sty)
Requires:       tex(ragged2e.sty), tex(xcolor.sty), tex(fontspec.sty), tex(lastpage.sty)
Requires:       tex(ifthen.sty), tex(kvoptions.sty), tex(calc.sty), tex(etoolbox.sty)
Requires:       tex(ifpdf.sty), tex(ifluatex.sty), tex(ifxetex.sty), tex(csquotes.sty)
Provides:       tex(argetabelle.cls) = %{tl_version}, tex(bewerbung-cv-casual.sty) = %{tl_version}
Provides:       tex(bewerbung-cv-classic.sty) = %{tl_version}
Provides:       tex(bewerbung-cv-oldstyle.sty) = %{tl_version}
Provides:       tex(bewerbung-cv.sty) = %{tl_version}, tex(bewerbung.cls) = %{tl_version}
Provides:       tex(bewerbung.sty) = %{tl_version}

%description -n texlive-bewerbung
The package provides packages and classes for typesetting
applications with titlepage, letter, cv and additional
documents in just a single document. The data for the
application can be edited in a simple csv file.

%package -n texlive-bewerbung-doc
Summary:        Documentation for bewerbung
Version:        svn37880.1.1

Provides:       tex-bewerbung-doc
AutoReqProv:    No

%description -n texlive-bewerbung-doc
Documentation for bewerbung

%package -n texlive-bez123
Provides:       tex-bez123 = %{tl_version}
License:        LPPL 1.3
Summary:        Support for Bezier curves
Version:        svn15878.1.1b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bez123.sty) = %{tl_version}, tex(multiply.sty) = %{tl_version}

%description -n texlive-bez123
Provides additional facilities in a picture environment for
drawing linear, cubic, and rational quadratic Bezier curves
(standard LaTeX only offers non-rational quadratic splines).
Provides a package multiply that provides a command for
multiplication of a length without numerical overflow.

%package -n texlive-bez123-doc
Summary:        Documentation for bez123
Version:        svn15878.1.1b

Provides:       tex-bez123-doc
AutoReqProv:    No

%description -n texlive-bez123-doc
Documentation for bez123

%package -n texlive-bezos
Provides:       tex-bezos = %{tl_version}
License:        LPPL
Summary:        Packages by Javier Bezos
Version:        svn25507.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(soulutf8.sty), tex(keyval.sty)
Provides:       tex(accents.sty) = %{tl_version}, tex(arabicfront.sty) = %{tl_version}
Provides:       tex(babeltools.sty) = %{tl_version}, tex(checkend.sty) = %{tl_version}
Provides:       tex(dotlessi.sty) = %{tl_version}, tex(esindex.sty) = %{tl_version}
Provides:       tex(soulpos.sty) = %{tl_version}, tex(subdocs.sty) = %{tl_version}
Provides:       tex(tensind.sty) = %{tl_version}

%description -n texlive-bezos
A set of packages that provide: tools for maths accents; a tool
that changes page-numbering in frontmatter to arabic; tools for
dealing with some annoyances in babel; a tool for making end-
environment checking more meaningful; tensorial indexes;
support for multi-file documents; tools for easy entry of
Spanish index entries; dotless i's and j's for maths fonts; and
fancy underlining.

%package -n texlive-bezos-doc
Summary:        Documentation for bezos
Version:        svn25507.0

Provides:       tex-bezos-doc
AutoReqProv:    No

%description -n texlive-bezos-doc
Documentation for bezos

%package -n texlive-bgreek
Provides:       tex-bgreek = %{tl_version}
License:        LPPL
Summary:        Using Beccari's fonts in betacode for classical Greek
Version:        svn15878.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bgmc0500.tfm) = %{tl_version}, tex(bgmc0600.tfm) = %{tl_version}
Provides:       tex(bgmc0700.tfm) = %{tl_version}, tex(bgmc0800.tfm) = %{tl_version}
Provides:       tex(bgmc0900.tfm) = %{tl_version}, tex(bgmc1000.tfm) = %{tl_version}
Provides:       tex(bgmc1095.tfm) = %{tl_version}, tex(bgmc1200.tfm) = %{tl_version}
Provides:       tex(bgmc1440.tfm) = %{tl_version}, tex(bgmc1728.tfm) = %{tl_version}
Provides:       tex(bgmc2074.tfm) = %{tl_version}, tex(bgmc2488.tfm) = %{tl_version}
Provides:       tex(bgmn0500.tfm) = %{tl_version}, tex(bgmn0600.tfm) = %{tl_version}
Provides:       tex(bgmn0700.tfm) = %{tl_version}, tex(bgmn0800.tfm) = %{tl_version}
Provides:       tex(bgmn0900.tfm) = %{tl_version}, tex(bgmn1000.tfm) = %{tl_version}
Provides:       tex(bgmn1095.tfm) = %{tl_version}, tex(bgmn1200.tfm) = %{tl_version}
Provides:       tex(bgmn1440.tfm) = %{tl_version}, tex(bgmn1728.tfm) = %{tl_version}
Provides:       tex(bgmn2074.tfm) = %{tl_version}, tex(bgmn2488.tfm) = %{tl_version}
Provides:       tex(bgmo0500.tfm) = %{tl_version}, tex(bgmo0600.tfm) = %{tl_version}
Provides:       tex(bgmo0700.tfm) = %{tl_version}, tex(bgmo0800.tfm) = %{tl_version}
Provides:       tex(bgmo0900.tfm) = %{tl_version}, tex(bgmo1000.tfm) = %{tl_version}
Provides:       tex(bgmo1095.tfm) = %{tl_version}, tex(bgmo1200.tfm) = %{tl_version}
Provides:       tex(bgmo1440.tfm) = %{tl_version}, tex(bgmo1728.tfm) = %{tl_version}
Provides:       tex(bgmo2074.tfm) = %{tl_version}, tex(bgmo2488.tfm) = %{tl_version}
Provides:       tex(bgxc0500.tfm) = %{tl_version}, tex(bgxc0600.tfm) = %{tl_version}
Provides:       tex(bgxc0700.tfm) = %{tl_version}, tex(bgxc0800.tfm) = %{tl_version}
Provides:       tex(bgxc0900.tfm) = %{tl_version}, tex(bgxc1000.tfm) = %{tl_version}
Provides:       tex(bgxc1095.tfm) = %{tl_version}, tex(bgxc1200.tfm) = %{tl_version}
Provides:       tex(bgxc1440.tfm) = %{tl_version}, tex(bgxc1728.tfm) = %{tl_version}
Provides:       tex(bgxc2074.tfm) = %{tl_version}, tex(bgxc2488.tfm) = %{tl_version}
Provides:       tex(bgxn0500.tfm) = %{tl_version}, tex(bgxn0600.tfm) = %{tl_version}
Provides:       tex(bgxn0700.tfm) = %{tl_version}, tex(bgxn0800.tfm) = %{tl_version}
Provides:       tex(bgxn0900.tfm) = %{tl_version}, tex(bgxn1000.tfm) = %{tl_version}
Provides:       tex(bgxn1095.tfm) = %{tl_version}, tex(bgxn1200.tfm) = %{tl_version}
Provides:       tex(bgxn1440.tfm) = %{tl_version}, tex(bgxn1728.tfm) = %{tl_version}
Provides:       tex(bgxn2074.tfm) = %{tl_version}, tex(bgxn2488.tfm) = %{tl_version}
Provides:       tex(bgxo0500.tfm) = %{tl_version}, tex(bgxo0600.tfm) = %{tl_version}
Provides:       tex(bgxo0700.tfm) = %{tl_version}, tex(bgxo0800.tfm) = %{tl_version}
Provides:       tex(bgxo0900.tfm) = %{tl_version}, tex(bgxo1000.tfm) = %{tl_version}
Provides:       tex(bgxo1095.tfm) = %{tl_version}, tex(bgxo1200.tfm) = %{tl_version}
Provides:       tex(bgxo1440.tfm) = %{tl_version}, tex(bgxo1728.tfm) = %{tl_version}
Provides:       tex(bgxo2074.tfm) = %{tl_version}, tex(bgxo2488.tfm) = %{tl_version}
Provides:       tex(bqmc0500.tfm) = %{tl_version}, tex(bqmc0600.tfm) = %{tl_version}
Provides:       tex(bqmc0700.tfm) = %{tl_version}, tex(bqmc0800.tfm) = %{tl_version}
Provides:       tex(bqmc0900.tfm) = %{tl_version}, tex(bqmc1000.tfm) = %{tl_version}
Provides:       tex(bqmc1095.tfm) = %{tl_version}, tex(bqmc1200.tfm) = %{tl_version}
Provides:       tex(bqmc1440.tfm) = %{tl_version}, tex(bqmc1728.tfm) = %{tl_version}
Provides:       tex(bqmc2074.tfm) = %{tl_version}, tex(bqmc2488.tfm) = %{tl_version}
Provides:       tex(bqmn0500.tfm) = %{tl_version}, tex(bqmn0600.tfm) = %{tl_version}
Provides:       tex(bqmn0700.tfm) = %{tl_version}, tex(bqmn0800.tfm) = %{tl_version}
Provides:       tex(bqmn0900.tfm) = %{tl_version}, tex(bqmn1000.tfm) = %{tl_version}
Provides:       tex(bqmn1095.tfm) = %{tl_version}, tex(bqmn1200.tfm) = %{tl_version}
Provides:       tex(bqmn1440.tfm) = %{tl_version}, tex(bqmn1728.tfm) = %{tl_version}
Provides:       tex(bqmn2074.tfm) = %{tl_version}, tex(bqmn2488.tfm) = %{tl_version}
Provides:       tex(bqmo0500.tfm) = %{tl_version}, tex(bqmo0600.tfm) = %{tl_version}
Provides:       tex(bqmo0700.tfm) = %{tl_version}, tex(bqmo0800.tfm) = %{tl_version}
Provides:       tex(bqmo0900.tfm) = %{tl_version}, tex(bqmo1000.tfm) = %{tl_version}
Provides:       tex(bqmo1095.tfm) = %{tl_version}, tex(bqmo1200.tfm) = %{tl_version}
Provides:       tex(bqmo1440.tfm) = %{tl_version}, tex(bqmo1728.tfm) = %{tl_version}
Provides:       tex(bqmo2074.tfm) = %{tl_version}, tex(bqmo2488.tfm) = %{tl_version}
Provides:       tex(bqxc0500.tfm) = %{tl_version}, tex(bqxc0600.tfm) = %{tl_version}
Provides:       tex(bqxc0700.tfm) = %{tl_version}, tex(bqxc0800.tfm) = %{tl_version}
Provides:       tex(bqxc0900.tfm) = %{tl_version}, tex(bqxc1000.tfm) = %{tl_version}
Provides:       tex(bqxc1095.tfm) = %{tl_version}, tex(bqxc1200.tfm) = %{tl_version}
Provides:       tex(bqxc1440.tfm) = %{tl_version}, tex(bqxc1728.tfm) = %{tl_version}
Provides:       tex(bqxc2074.tfm) = %{tl_version}, tex(bqxc2488.tfm) = %{tl_version}
Provides:       tex(bqxn0500.tfm) = %{tl_version}, tex(bqxn0600.tfm) = %{tl_version}
Provides:       tex(bqxn0700.tfm) = %{tl_version}, tex(bqxn0800.tfm) = %{tl_version}
Provides:       tex(bqxn0900.tfm) = %{tl_version}, tex(bqxn1000.tfm) = %{tl_version}
Provides:       tex(bqxn1095.tfm) = %{tl_version}, tex(bqxn1200.tfm) = %{tl_version}
Provides:       tex(bqxn1440.tfm) = %{tl_version}, tex(bqxn1728.tfm) = %{tl_version}
Provides:       tex(bqxn2074.tfm) = %{tl_version}, tex(bqxn2488.tfm) = %{tl_version}
Provides:       tex(bqxo0500.tfm) = %{tl_version}, tex(bqxo0600.tfm) = %{tl_version}
Provides:       tex(bqxo0700.tfm) = %{tl_version}, tex(bqxo0800.tfm) = %{tl_version}
Provides:       tex(bqxo0900.tfm) = %{tl_version}, tex(bqxo1000.tfm) = %{tl_version}
Provides:       tex(bqxo1095.tfm) = %{tl_version}, tex(bqxo1200.tfm) = %{tl_version}
Provides:       tex(bqxo1440.tfm) = %{tl_version}, tex(bqxo1728.tfm) = %{tl_version}
Provides:       tex(bqxo2074.tfm) = %{tl_version}, tex(bqxo2488.tfm) = %{tl_version}
Provides:       tex(bgmc0500.vf) = %{tl_version}, tex(bgmc0600.vf) = %{tl_version}
Provides:       tex(bgmc0700.vf) = %{tl_version}, tex(bgmc0800.vf) = %{tl_version}
Provides:       tex(bgmc0900.vf) = %{tl_version}, tex(bgmc1000.vf) = %{tl_version}
Provides:       tex(bgmc1095.vf) = %{tl_version}, tex(bgmc1200.vf) = %{tl_version}
Provides:       tex(bgmc1440.vf) = %{tl_version}, tex(bgmc1728.vf) = %{tl_version}
Provides:       tex(bgmc2074.vf) = %{tl_version}, tex(bgmc2488.vf) = %{tl_version}
Provides:       tex(bgmn0500.vf) = %{tl_version}, tex(bgmn0600.vf) = %{tl_version}
Provides:       tex(bgmn0700.vf) = %{tl_version}, tex(bgmn0800.vf) = %{tl_version}
Provides:       tex(bgmn0900.vf) = %{tl_version}, tex(bgmn1000.vf) = %{tl_version}
Provides:       tex(bgmn1095.vf) = %{tl_version}, tex(bgmn1200.vf) = %{tl_version}
Provides:       tex(bgmn1440.vf) = %{tl_version}, tex(bgmn1728.vf) = %{tl_version}
Provides:       tex(bgmn2074.vf) = %{tl_version}, tex(bgmn2488.vf) = %{tl_version}
Provides:       tex(bgmo0500.vf) = %{tl_version}, tex(bgmo0600.vf) = %{tl_version}
Provides:       tex(bgmo0700.vf) = %{tl_version}, tex(bgmo0800.vf) = %{tl_version}
Provides:       tex(bgmo0900.vf) = %{tl_version}, tex(bgmo1000.vf) = %{tl_version}
Provides:       tex(bgmo1095.vf) = %{tl_version}, tex(bgmo1200.vf) = %{tl_version}
Provides:       tex(bgmo1440.vf) = %{tl_version}, tex(bgmo1728.vf) = %{tl_version}
Provides:       tex(bgmo2074.vf) = %{tl_version}, tex(bgmo2488.vf) = %{tl_version}
Provides:       tex(bgxc0500.vf) = %{tl_version}, tex(bgxc0600.vf) = %{tl_version}
Provides:       tex(bgxc0700.vf) = %{tl_version}, tex(bgxc0800.vf) = %{tl_version}
Provides:       tex(bgxc0900.vf) = %{tl_version}, tex(bgxc1000.vf) = %{tl_version}
Provides:       tex(bgxc1095.vf) = %{tl_version}, tex(bgxc1200.vf) = %{tl_version}
Provides:       tex(bgxc1440.vf) = %{tl_version}, tex(bgxc1728.vf) = %{tl_version}
Provides:       tex(bgxc2074.vf) = %{tl_version}, tex(bgxc2488.vf) = %{tl_version}
Provides:       tex(bgxn0500.vf) = %{tl_version}, tex(bgxn0600.vf) = %{tl_version}
Provides:       tex(bgxn0700.vf) = %{tl_version}, tex(bgxn0800.vf) = %{tl_version}
Provides:       tex(bgxn0900.vf) = %{tl_version}, tex(bgxn1000.vf) = %{tl_version}
Provides:       tex(bgxn1095.vf) = %{tl_version}, tex(bgxn1200.vf) = %{tl_version}
Provides:       tex(bgxn1440.vf) = %{tl_version}, tex(bgxn1728.vf) = %{tl_version}
Provides:       tex(bgxn2074.vf) = %{tl_version}, tex(bgxn2488.vf) = %{tl_version}
Provides:       tex(bgxo0500.vf) = %{tl_version}, tex(bgxo0600.vf) = %{tl_version}
Provides:       tex(bgxo0700.vf) = %{tl_version}, tex(bgxo0800.vf) = %{tl_version}
Provides:       tex(bgxo0900.vf) = %{tl_version}, tex(bgxo1000.vf) = %{tl_version}
Provides:       tex(bgxo1095.vf) = %{tl_version}, tex(bgxo1200.vf) = %{tl_version}
Provides:       tex(bgxo1440.vf) = %{tl_version}, tex(bgxo1728.vf) = %{tl_version}
Provides:       tex(bgxo2074.vf) = %{tl_version}, tex(bgxo2488.vf) = %{tl_version}
Provides:       tex(bqmc0500.vf) = %{tl_version}, tex(bqmc0600.vf) = %{tl_version}
Provides:       tex(bqmc0700.vf) = %{tl_version}, tex(bqmc0800.vf) = %{tl_version}
Provides:       tex(bqmc0900.vf) = %{tl_version}, tex(bqmc1000.vf) = %{tl_version}
Provides:       tex(bqmc1095.vf) = %{tl_version}, tex(bqmc1200.vf) = %{tl_version}
Provides:       tex(bqmc1440.vf) = %{tl_version}, tex(bqmc1728.vf) = %{tl_version}
Provides:       tex(bqmc2074.vf) = %{tl_version}, tex(bqmc2488.vf) = %{tl_version}
Provides:       tex(bqmn0500.vf) = %{tl_version}, tex(bqmn0600.vf) = %{tl_version}
Provides:       tex(bqmn0700.vf) = %{tl_version}, tex(bqmn0800.vf) = %{tl_version}
Provides:       tex(bqmn0900.vf) = %{tl_version}, tex(bqmn1000.vf) = %{tl_version}
Provides:       tex(bqmn1095.vf) = %{tl_version}, tex(bqmn1200.vf) = %{tl_version}
Provides:       tex(bqmn1440.vf) = %{tl_version}, tex(bqmn1728.vf) = %{tl_version}
Provides:       tex(bqmn2074.vf) = %{tl_version}, tex(bqmn2488.vf) = %{tl_version}
Provides:       tex(bqmo0500.vf) = %{tl_version}, tex(bqmo0600.vf) = %{tl_version}
Provides:       tex(bqmo0700.vf) = %{tl_version}, tex(bqmo0800.vf) = %{tl_version}
Provides:       tex(bqmo0900.vf) = %{tl_version}, tex(bqmo1000.vf) = %{tl_version}
Provides:       tex(bqmo1095.vf) = %{tl_version}, tex(bqmo1200.vf) = %{tl_version}
Provides:       tex(bqmo1440.vf) = %{tl_version}, tex(bqmo1728.vf) = %{tl_version}
Provides:       tex(bqmo2074.vf) = %{tl_version}, tex(bqmo2488.vf) = %{tl_version}
Provides:       tex(bqxc0500.vf) = %{tl_version}, tex(bqxc0600.vf) = %{tl_version}
Provides:       tex(bqxc0700.vf) = %{tl_version}, tex(bqxc0800.vf) = %{tl_version}
Provides:       tex(bqxc0900.vf) = %{tl_version}, tex(bqxc1000.vf) = %{tl_version}
Provides:       tex(bqxc1095.vf) = %{tl_version}, tex(bqxc1200.vf) = %{tl_version}
Provides:       tex(bqxc1440.vf) = %{tl_version}, tex(bqxc1728.vf) = %{tl_version}
Provides:       tex(bqxc2074.vf) = %{tl_version}, tex(bqxc2488.vf) = %{tl_version}
Provides:       tex(bqxn0500.vf) = %{tl_version}, tex(bqxn0600.vf) = %{tl_version}
Provides:       tex(bqxn0700.vf) = %{tl_version}, tex(bqxn0800.vf) = %{tl_version}
Provides:       tex(bqxn0900.vf) = %{tl_version}, tex(bqxn1000.vf) = %{tl_version}
Provides:       tex(bqxn1095.vf) = %{tl_version}, tex(bqxn1200.vf) = %{tl_version}
Provides:       tex(bqxn1440.vf) = %{tl_version}, tex(bqxn1728.vf) = %{tl_version}
Provides:       tex(bqxn2074.vf) = %{tl_version}, tex(bqxn2488.vf) = %{tl_version}
Provides:       tex(bqxo0500.vf) = %{tl_version}, tex(bqxo0600.vf) = %{tl_version}
Provides:       tex(bqxo0700.vf) = %{tl_version}, tex(bqxo0800.vf) = %{tl_version}
Provides:       tex(bqxo0900.vf) = %{tl_version}, tex(bqxo1000.vf) = %{tl_version}
Provides:       tex(bqxo1095.vf) = %{tl_version}, tex(bqxo1200.vf) = %{tl_version}
Provides:       tex(bqxo1440.vf) = %{tl_version}, tex(bqxo1728.vf) = %{tl_version}
Provides:       tex(bqxo2074.vf) = %{tl_version}, tex(bqxo2488.vf) = %{tl_version}
Provides:       tex(bcgcmr.fd) = %{tl_version}, tex(bcgenc.def) = %{tl_version}
Provides:       tex(bcglmr.fd) = %{tl_version}, tex(bcqcmr.fd) = %{tl_version}
Provides:       tex(bcqenc.def) = %{tl_version}, tex(bcqlmr.fd) = %{tl_version}
Provides:       tex(bgfonts.tex) = %{tl_version}, tex(bgreek.ldf) = %{tl_version}
Provides:       tex(bgreek.sty) = %{tl_version}, tex(ibygreek.ldf) = %{tl_version}

%description -n texlive-bgreek
This package implements a dialect of the Beta Code encoding
(TLG and Perseus Projects) for typesetting classical Greek
using Claudio Beccari's Greek Fonts. The package provides
virtual fonts, to reference Beccari's fonts in bgreek mode, and
support macros for use with LaTeX.

%package -n texlive-bgreek-doc
Summary:        Documentation for bgreek
Version:        svn15878.0.3

Provides:       tex-bgreek-doc
AutoReqProv:    No

%description -n texlive-bgreek-doc
Documentation for bgreek

%package -n texlive-bgteubner
Provides:       tex-bgteubner = %{tl_version}
License:        LPPL
Summary:        Class for producing books for the publisher "Teubner Verlag"
Version:        svn44205
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(fixltx2e.sty), tex(wasysym.sty), tex(amsmath.sty), tex(amsfonts.sty)
Requires:       tex(amssymb.sty), tex(booktabs.sty), tex(array.sty), tex(longtable.sty)
Requires:       tex(fontenc.sty), tex(mathptmx.sty), tex(helvet.sty), tex(courier.sty)
Requires:       tex(hfoldsty.sty), tex(textcomp.sty), tex(mathcomp.sty), tex(hhsubfigure.sty)
Requires:       tex(ragged2e.sty), tex(exscale.sty), tex(graphicx.sty), tex(color.sty)
Requires:       tex(framed.sty), tex(hhtensor.sty), tex(makeidx.sty), tex(mdwlist.sty)
Requires:       tex(paralist.sty), tex(ifthen.sty), tex(ifpdf.sty), tex(fixmath.sty)
Requires:       tex(babel.sty), tex(setspace.sty), tex(relsize.sty), tex(slantsc.sty)
Requires:       tex(ginpenc.sty), tex(warning.sty), tex(onlyamsmath.sty), tex(numprint.sty)
Requires:       tex(scrpage2.sty), tex(babelbib.sty), tex(fnbreak.sty), tex(subfloat.sty)
Requires:       tex(multicol.sty), tex(pdfcprot.sty), tex(verbatim.sty)
Provides:       tex(bgteubner.cls) = %{tl_version}, tex(hhfixme.sty) = %{tl_version}
Provides:       tex(hhsubfigure.sty) = %{tl_version}, tex(ptmxcomp.sty) = %{tl_version}

%description -n texlive-bgteubner
The bgteubner document class has been programmed by order of
the Teubner Verlag, Wiesbaden, Germany, to ensure that books of
this publisher have a unique layout. Unfortunately, most of the
documentation is only available in German. Since the document
class is intended to generate a unique layout, many things
(layout etc.) are fixed and cannot be altered by the user. If
you want to use the document class for another purpose than
publishing with the Teubner Verlag, this may arrise unwanted
restrictions (For instance, the document class provides only
two paper sizes: DIN A-5 and 17cm x 24cm; only two font
families are supported: Times and European Computer Modern).

%package -n texlive-bgteubner-doc
Summary:        Documentation for bgteubner
Version:        svn44205
Provides:       tex-bgteubner-doc
AutoReqProv:    No

%description -n texlive-bgteubner-doc
Documentation for bgteubner

%package -n texlive-bguq
Provides:       tex-bguq = %{tl_version}
License:        LPPL
Summary:        Improved quantifier stroke for Begriffsschrift packages
Version:        svn27401.0.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(ifthen.sty)
Provides:       tex(bguq.map) = %{tl_version}, tex(bguq10t04.tfm) = %{tl_version}
Provides:       tex(bguq10t05.tfm) = %{tl_version}, tex(bguq10t06.tfm) = %{tl_version}
Provides:       tex(bguq10t07.tfm) = %{tl_version}, tex(bguq10t08.tfm) = %{tl_version}
Provides:       tex(bguq10t09.tfm) = %{tl_version}, tex(bguq10t10.tfm) = %{tl_version}
Provides:       tex(bguq10t11.tfm) = %{tl_version}, tex(bguq10t12.tfm) = %{tl_version}
Provides:       tex(bguq10t04.pfb) = %{tl_version}, tex(bguq10t05.pfb) = %{tl_version}
Provides:       tex(bguq10t06.pfb) = %{tl_version}, tex(bguq10t07.pfb) = %{tl_version}
Provides:       tex(bguq10t08.pfb) = %{tl_version}, tex(bguq10t09.pfb) = %{tl_version}
Provides:       tex(bguq10t10.pfb) = %{tl_version}, tex(bguq10t11.pfb) = %{tl_version}
Provides:       tex(bguq10t12.pfb) = %{tl_version}, tex(Ubguq04.fd) = %{tl_version}
Provides:       tex(Ubguq05.fd) = %{tl_version}, tex(Ubguq06.fd) = %{tl_version}
Provides:       tex(Ubguq07.fd) = %{tl_version}, tex(Ubguq08.fd) = %{tl_version}
Provides:       tex(Ubguq09.fd) = %{tl_version}, tex(Ubguq10.fd) = %{tl_version}
Provides:       tex(Ubguq11.fd) = %{tl_version}, tex(Ubguq12.fd) = %{tl_version}
Provides:       tex(begriff-bguq.sty) = %{tl_version}, tex(bguq.cfg) = %{tl_version}
Provides:       tex(bguq.sty) = %{tl_version}

%description -n texlive-bguq
The font contains a single character: the Begriffsschrift
quantifier (in several sizes), as used to set the
Begriffsschrift (concept notation) of Frege. The font is not
intended for end users; instead it is expected that it will be
used by other packages which implement the Begriffsschrift. An
(unofficial) modified version of Josh Parsons' begriff is
included as an example of implementation.

%package -n texlive-bguq-doc
Summary:        Documentation for bguq
Version:        svn27401.0.4

Provides:       tex-bguq-doc
AutoReqProv:    No

%description -n texlive-bguq-doc
Documentation for bguq

%package -n texlive-bhcexam
Provides:       tex-bhcexam = %{tl_version}
License:        LPPL
Summary:        An exam class designed for Mathematics Teachers in China
Version:        svn39041

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifpdf.sty), tex(ifxetex.sty), tex(amsmath.sty), tex(amssymb.sty)
Requires:       tex(amsthm.sty), tex(bm.sty), tex(bbding.sty), tex(pifont.sty)
Requires:       tex(dsfont.sty), tex(mathtools.sty), tex(paralist.sty), tex(cases.sty)
Requires:       tex(tabularx.sty), tex(pstricks.sty), tex(pst-plot.sty), tex(xcolor.sty)
Requires:       tex(graphicx.sty), tex(geometry.sty)
Provides:       tex(BHCexam.cfg) = %{tl_version}, tex(BHCexam.cls) = %{tl_version}

%description -n texlive-bhcexam
The class based on the exam class, and is specially designed
for High School Mathematics Teachers in China.

%package -n texlive-bhcexam-doc
Summary:        Documentation for bhcexam
Version:        svn39041

Provides:       tex-bhcexam-doc
AutoReqProv:    No

%description -n texlive-bhcexam-doc
Documentation for bhcexam

%package -n texlive-bibarts
Provides:       tex-bibarts = %{tl_version}
License:        GPL+
Summary:        "Arts"-style bibliographical information
Version:        svn40096

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bibarts.sty) = %{tl_version}

%description -n texlive-bibarts
The bibarts package assists in making bibliographical lists in
the way that is common in the arts; it requires an auxiliary
program, for which source and a DOS executable are provided.
(Documentation is in German, though bibarts.sty does contain a
brief introduction in English, as a comment.)

%package -n texlive-bibarts-doc
Summary:        Documentation for bibarts
Version:        svn40096

Provides:       tex-bibarts-doc
AutoReqProv:    No

%description -n texlive-bibarts-doc
Documentation for bibarts

%package -n texlive-bib-fr
Provides:       tex-bib-fr = %{tl_version}
License:        LPPL
Summary:        French translation of classical BibTeX styles
Version:        svn15878.1.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-bib-fr
These files are French translations of the classical BibTeX
style files. The translations can easily be modified by simply
redefining FUNCTIONs named fr.*, at the beginning (lines 50-
150) of each file.

%package -n texlive-bib-fr-doc
Summary:        Documentation for bib-fr
Version:        svn15878.1.5

Provides:       tex-bib-fr-doc
AutoReqProv:    No

%description -n texlive-bib-fr-doc
Documentation for bib-fr

%package -n texlive-bibhtml
Provides:       tex-bibhtml = %{tl_version}
License:        GPL+
Summary:        BibTeX support for HTML files
Version:        svn31607.2.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-bibhtml
Bibhtml consists of a Perl script and a set of BibTeX style
files, which together allow you to output a bibliography as a
collection of HTML files. The references in the text are linked
directly to the corresponding bibliography entry, and if a URL
is defined in the entry within the BibTeX database file, then
the generated bibliography entry is linked to this. The package
provides three different style files derived from each of the
standard plain.bst and alpha.bst, as well as two style files
derived from abbrv.bst and unsrt.bst (i.e., eight in total).

%package -n texlive-bibhtml-doc
Summary:        Documentation for bibhtml
Version:        svn31607.2.0.2

Provides:       tex-bibhtml-doc
AutoReqProv:    No

%description -n texlive-bibhtml-doc
Documentation for bibhtml

%package -n texlive-biblatex-anonymous
Provides:       tex-biblatex-anonymous = %{tl_version}
License:        LPPL 1.3
Summary:        A tool to manage anonymous work with biblatex
Version:        svn45855
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(biblatex-anonymous.sty) = %{tl_version}

%description -n texlive-biblatex-anonymous
The package provides tools to help manage anonymous work with
biblatex. It will be useful, for example, in history or
classical philology.

%package -n texlive-biblatex-anonymous-doc
Summary:        Documentation for biblatex-anonymous
Version:        svn45855
Provides:       tex-biblatex-anonymous-doc
AutoReqProv:    No

%description -n texlive-biblatex-anonymous-doc
Documentation for biblatex-anonymous

%package -n texlive-biblatex-apa
Provides:       tex-biblatex-apa = %{tl_version}
License:        LPPL
Summary:        Biblatex citation and reference style for APA
Version:        svn47268
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       biber, tex(standard.bbx)
Provides:       tex(apa.bbx) = %{tl_version}, tex(apa.cbx) = %{tl_version}

%description -n texlive-biblatex-apa
This is a fairly complete biblatex style (citations and
references) for APA (American Psychological Association)
publications. It implements and automates most of the
guidelines in the APA 6th edition style guide for citations and
references with a few (documented) exceptions (which are mainly
currently impossible to automate in principle for any BibTeX-
backed system). An example document is also given which
typesets every citation and reference example in the APA 6th
edition style guide. This version of the package requires use
of biblatex v2.0 and biber v1.0 (at least).

%package -n texlive-biblatex-apa-doc
Summary:        Documentation for biblatex-apa
Version:        svn47268
Provides:       tex-biblatex-apa-doc
AutoReqProv:    No

%description -n texlive-biblatex-apa-doc
Documentation for biblatex-apa

%package -n texlive-biblatex-bookinarticle
Provides:       tex-biblatex-bookinarticle = %{tl_version}
License:        LPPL 1.3
Summary:        Manage book edited in article
Version:        svn40323

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(biblatex-bookinarticle.sty) = %{tl_version}

%description -n texlive-biblatex-bookinarticle
This package provides two new biblatex entry types:
@bookinarticle and @bookinincollection, to refer to a modern
edition of an old book, where this modern edition is provided
in a @article or in a @incollection.

%package -n texlive-biblatex-bookinarticle-doc
Summary:        Documentation for biblatex-bookinarticle
Version:        svn40323

Provides:       tex-biblatex-bookinarticle-doc
AutoReqProv:    No

%description -n texlive-biblatex-bookinarticle-doc
Documentation for biblatex-bookinarticle

%package -n texlive-biblatex-bwl
Provides:       tex-biblatex-bwl = %{tl_version}
License:        LPPL 1.3
Summary:        Biblatex citations for FU Berlin
Version:        svn26556.0.02

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(authoryear.bbx), tex(authoryear.cbx)
Provides:       tex(bwl-FU.bbx) = %{tl_version}, tex(bwl-FU.cbx) = %{tl_version}

%description -n texlive-biblatex-bwl
The bundle provides a set of biblatex implementations of
bibliography and citation styles for the Business
Administration Department of the Free University of Berlin.

%package -n texlive-biblatex-bwl-doc
Summary:        Documentation for biblatex-bwl
Version:        svn26556.0.02

Provides:       tex-biblatex-bwl-doc
AutoReqProv:    No

%description -n texlive-biblatex-bwl-doc
Documentation for biblatex-bwl

%package -n texlive-biblatex-caspervector
Provides:       tex-biblatex-caspervector = %{tl_version}
License:        LPPL 1.3
Summary:        A simple citation style for Chinese users
Version:        svn48122
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(numeric.bbx), tex(numeric-comp.cbx)
Provides:       tex(biblatex-caspervector-gbk.def) = %{tl_version}
Provides:       tex(biblatex-caspervector-utf8.def) = %{tl_version}
Provides:       tex(caspervector.bbx) = %{tl_version}, tex(caspervector.cbx) = %{tl_version}

%description -n texlive-biblatex-caspervector
The package provides a simple and easily extensible
biblography/citation style for Chinese LaTeX users, using
biblatex.

%package -n texlive-biblatex-caspervector-doc
Summary:        Documentation for biblatex-caspervector
Version:        svn48122
Provides:       tex-biblatex-caspervector-doc
AutoReqProv:    No

%description -n texlive-biblatex-caspervector-doc
Documentation for biblatex-caspervector

%package -n texlive-biblatex-chem
Provides:       tex-biblatex-chem = %{tl_version}
License:        LPPL 1.3
Summary:        A set of biblatex implementations of chemistry-related bibliography styles
Version:        svn46441
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(numeric-comp.bbx), tex(numeric-comp.cbx)
Provides:       tex(chem-acs.bbx) = %{tl_version}, tex(chem-acs.cbx) = %{tl_version}
Provides:       tex(chem-angew.bbx) = %{tl_version}, tex(chem-angew.cbx) = %{tl_version}
Provides:       tex(chem-biochem.bbx) = %{tl_version}, tex(chem-biochem.cbx) = %{tl_version}
Provides:       tex(chem-rsc.bbx) = %{tl_version}, tex(chem-rsc.cbx) = %{tl_version}

%description -n texlive-biblatex-chem
The bundle offers a set of styles to allow chemists to use
biblatex. The package has complete styles for: all ACS
journals; RSC journals using standard (Chem. Commun.) style;
and Angewandte Chem. style, (thus covering a wide range of
journals). A comprehensive set of examples of use is included.

%package -n texlive-biblatex-chem-doc
Summary:        Documentation for biblatex-chem
Version:        svn46441
Provides:       tex-biblatex-chem-doc
AutoReqProv:    No

%description -n texlive-biblatex-chem-doc
Documentation for biblatex-chem

%package -n texlive-biblatex-chicago
Provides:       tex-biblatex-chicago = %{tl_version}
License:        LPPL 1.3
Summary:        Chicago style files for biblatex
Version:        svn46331
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(etoolbox.sty), tex(biblatex.sty)
Provides:       tex(biblatex-chicago.sty) = %{tl_version}
Provides:       tex(chicago-authordate-trad.bbx) = %{tl_version}
Provides:       tex(chicago-authordate-trad.cbx) = %{tl_version}
Provides:       tex(chicago-authordate.bbx) = %{tl_version}
Provides:       tex(chicago-authordate.cbx) = %{tl_version}
Provides:       tex(chicago-authordate15.bbx) = %{tl_version}
Provides:       tex(chicago-authordate15.cbx) = %{tl_version}
Provides:       tex(chicago-notes.bbx) = %{tl_version}, tex(chicago-notes.cbx) = %{tl_version}
Provides:       tex(chicago-notes15.bbx) = %{tl_version}
Provides:       tex(chicago-notes15.cbx) = %{tl_version}

%description -n texlive-biblatex-chicago
This is a biblatex style that implements the Chicago 'author-
date' and 'notes with bibliography' style specifications given
in the Chicago Manual of Style, 16th edition (support for the
15th edition remains, but is 'strongly deprecated'). The style
implements entry types for citing audio-visual materials. The
package was previously known as biblatex-chicago-notes-df.

%package -n texlive-biblatex-chicago-doc
Summary:        Documentation for biblatex-chicago
Version:        svn46331
Provides:       tex-biblatex-chicago-doc
AutoReqProv:    No

%description -n texlive-biblatex-chicago-doc
Documentation for biblatex-chicago

%package -n texlive-biblatex-dw
Provides:       tex-biblatex-dw = %{tl_version}
License:        LPPL
Summary:        Humanities styles for biblatex
Version:        svn42649
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(authortitle-dw.bbx), tex(standard.bbx)
Provides:       tex(authortitle-dw.bbx) = %{tl_version}, tex(footnote-dw.bbx) = %{tl_version}
Provides:       tex(standard-dw.bbx) = %{tl_version}, tex(authortitle-dw.cbx) = %{tl_version}
Provides:       tex(footnote-dw.cbx) = %{tl_version}, tex(standard-dw.cbx) = %{tl_version}

%description -n texlive-biblatex-dw
A small collection of styles for the biblatex package. It was
designed for citations in the humanities and offers some
features that are not provided by the standard biblatex styles.
The styles are dependent on biblatex (at least version 0.9b)
and cannot be used without it. Eine kleine Sammlung von Stilen
fur das Paket biblatex. Es ist auf geisteswissenschaftliche
Zitierweise zugeschnitten und bietet einige Funktionen, die von
den Standard-Stilen von biblatex nicht direkt bereitgestellt
werden. Biblatex-dw baut vollstandig auf biblatex auf und kann
nicht ohne biblatex (mindestens in der Version 0.9b) verwendet
werden.

%package -n texlive-biblatex-dw-doc
Summary:        Documentation for biblatex-dw
Version:        svn42649
Provides:       tex-biblatex-dw-doc
AutoReqProv:    No

%description -n texlive-biblatex-dw-doc
Documentation for biblatex-dw

%package -n texlive-biblatex-fiwi
Provides:       tex-biblatex-fiwi = %{tl_version}
License:        LPPL 1.3
Summary:        Biblatex styles for use in German humanities
Version:        svn45876
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(standard.bbx), tex(fiwi.cbx)
Provides:       tex(fiwi-yearbeginning.bbx) = %{tl_version}
Provides:       tex(fiwi.bbx) = %{tl_version}, tex(fiwi.cbx) = %{tl_version}
Provides:       tex(fiwi2.bbx) = %{tl_version}, tex(fiwi2.cbx) = %{tl_version}

%description -n texlive-biblatex-fiwi
The package provides a collection of styles for biblatex
(version 1.7 is required, currently). It was designed for
citations in German Humanities, especially film studies, and
offers some features that are not provided by the standard
biblatex styles. The style is highly optimized for documents
written in German, and the main documentation is only available
in German.

%package -n texlive-biblatex-fiwi-doc
Summary:        Documentation for biblatex-fiwi
Version:        svn45876
Provides:       tex-biblatex-fiwi-doc
AutoReqProv:    No

%description -n texlive-biblatex-fiwi-doc
Documentation for biblatex-fiwi

%package -n texlive-biblatex-gost
Provides:       tex-biblatex-gost = %{tl_version}
License:        LPPL 1.3
Summary:        Biblatex support for GOST standard bibliographies
Version:        svn46709
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(gost-alphabetic.cbx), tex(alphabetic.cbx)
Requires:       tex(gost-authoryear.cbx), tex(gost-footnote.cbx)
Requires:       tex(gost-inline.cbx), tex(gost-numeric.cbx)
Requires:       tex(numeric-comp.cbx)
Provides:       tex(biblatex-gost.def) = %{tl_version}, tex(gost-alphabetic-min.bbx) = %{tl_version}
Provides:       tex(gost-alphabetic-min.cbx) = %{tl_version}
Provides:       tex(gost-alphabetic.bbx) = %{tl_version}
Provides:       tex(gost-alphabetic.cbx) = %{tl_version}
Provides:       tex(gost-authoryear-min.bbx) = %{tl_version}
Provides:       tex(gost-authoryear-min.cbx) = %{tl_version}
Provides:       tex(gost-authoryear.bbx) = %{tl_version}
Provides:       tex(gost-authoryear.cbx) = %{tl_version}
Provides:       tex(gost-footnote-min.bbx) = %{tl_version}
Provides:       tex(gost-footnote-min.cbx) = %{tl_version}
Provides:       tex(gost-footnote.bbx) = %{tl_version}, tex(gost-footnote.cbx) = %{tl_version}
Provides:       tex(gost-inline-min.bbx) = %{tl_version}
Provides:       tex(gost-inline-min.cbx) = %{tl_version}
Provides:       tex(gost-inline.bbx) = %{tl_version}, tex(gost-inline.cbx) = %{tl_version}
Provides:       tex(gost-numeric-min.bbx) = %{tl_version}
Provides:       tex(gost-numeric-min.cbx) = %{tl_version}
Provides:       tex(gost-numeric.bbx) = %{tl_version}, tex(gost-numeric.cbx) = %{tl_version}
Provides:       tex(gost-standard.bbx) = %{tl_version}

%description -n texlive-biblatex-gost
The package provides biblatex support for Russian bibliography
style GOST 7.0.5-2008

%package -n texlive-biblatex-gost-doc
Summary:        Documentation for biblatex-gost
Version:        svn46709
Provides:       tex-biblatex-gost-doc
AutoReqProv:    No

%description -n texlive-biblatex-gost-doc
Documentation for biblatex-gost

%package -n texlive-biblatex-historian
Provides:       tex-biblatex-historian = %{tl_version}
License:        LPPL
Summary:        A Biblatex style
Version:        svn19787.0.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(standard.bbx)
Provides:       tex(historian.bbx) = %{tl_version}, tex(historian.cbx) = %{tl_version}

%description -n texlive-biblatex-historian
A biblatex style, based on the Turabian Manual (a version of
Chicago).

%package -n texlive-biblatex-historian-doc
Summary:        Documentation for biblatex-historian
Version:        svn19787.0.4

Provides:       tex-biblatex-historian-doc
AutoReqProv:    No

%description -n texlive-biblatex-historian-doc
Documentation for biblatex-historian

%package -n texlive-biblatex-ieee
Provides:       tex-biblatex-ieee = %{tl_version}
License:        LPPL 1.3
Summary:        Ieee style files for biblatex
Version:        svn43620
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(alphabetic.cbx), tex(numeric-comp.bbx)
Requires:       tex(numeric-comp.cbx)
Provides:       tex(ieee-alphabetic.bbx) = %{tl_version}
Provides:       tex(ieee-alphabetic.cbx) = %{tl_version}
Provides:       tex(ieee.bbx) = %{tl_version}, tex(ieee.cbx) = %{tl_version}

%description -n texlive-biblatex-ieee
This is a biblatex style that implements the bibliography style
of the IEEE for biblatex. The implementation follows standard
biblatex conventions, and can be used simply by loading
biblatex with the appropriate option:
\usepackage[style=ieee]{biblatex} A demonstration database is
provided to show how to format input for the style.

%package -n texlive-biblatex-ieee-doc
Summary:        Documentation for biblatex-ieee
Version:        svn43620
Provides:       tex-biblatex-ieee-doc
AutoReqProv:    No

%description -n texlive-biblatex-ieee-doc
Documentation for biblatex-ieee

%package -n texlive-biblatex-juradiss
Provides:       tex-biblatex-juradiss = %{tl_version}
License:        LPPL
Summary:        Biblatex stylefiles for German law thesis
Version:        svn29252.0.1g

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(authortitle-dw.bbx), tex(authortitle-dw.cbx)
Provides:       tex(biblatex-juradiss.bbx) = %{tl_version}
Provides:       tex(biblatex-juradiss.cbx) = %{tl_version}

%description -n texlive-biblatex-juradiss
The package provides a style for use in typesetting a German
law thesis with LaTeX. The package (using biblatex) is based on
biblatex-dw and uses biber.

%package -n texlive-biblatex-juradiss-doc
Summary:        Documentation for biblatex-juradiss
Version:        svn29252.0.1g

Provides:       tex-biblatex-juradiss-doc
AutoReqProv:    No

%description -n texlive-biblatex-juradiss-doc
Documentation for biblatex-juradiss

%package -n texlive-biblatex-luh-ipw
Provides:       tex-biblatex-luh-ipw = %{tl_version}
License:        LPPL 1.3
Summary:        Biblatex styles for social sciences
Version:        svn32180.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(authoryear-icomp.bbx), tex(verbose-inote.bbx)
Requires:       tex(authoryear-icomp.cbx), tex(verbose-inote.cbx)
Provides:       tex(authoryear-luh-ipw.bbx) = %{tl_version}
Provides:       tex(standard-luh-ipw.bbx) = %{tl_version}
Provides:       tex(verbose-inote-luh-ipw.bbx) = %{tl_version}
Provides:       tex(authoryear-luh-ipw.cbx) = %{tl_version}
Provides:       tex(standard-luh-ipw.cbx) = %{tl_version}
Provides:       tex(verbose-inote-luh-ipw.cbx) = %{tl_version}

%description -n texlive-biblatex-luh-ipw
The bundle is a small collection of styles for biblatex. It was
designed for citations in the Humanities, following the
guidelines of style of the institutes for the social sciences
of the Leibniz University Hannover/LUH (especially the
Institute of Political Science). The bundle depends on biblatex
(version 1.1 at least) and cannot be used without it.

%package -n texlive-biblatex-luh-ipw-doc
Summary:        Documentation for biblatex-luh-ipw
Version:        svn32180.0.3

Provides:       tex-biblatex-luh-ipw-doc
AutoReqProv:    No

%description -n texlive-biblatex-luh-ipw-doc
Documentation for biblatex-luh-ipw

%package -n texlive-biblatex-manuscripts-philology
Provides:       tex-biblatex-manuscripts-philology = %{tl_version}
License:        LPPL 1.3
Summary:        Manage classical manuscripts with biblatex
Version:        svn45912
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(verbose.bbx)
Provides:       tex(manuscripts-noautoshorthand.bbx) = %{tl_version}
Provides:       tex(manuscripts-shared.bbx) = %{tl_version}
Provides:       tex(manuscripts.bbx) = %{tl_version}

%description -n texlive-biblatex-manuscripts-philology
The package adds a new entry type: @manuscript to manage
manuscript in classical philology, for example to prepare a
critical edition.

%package -n texlive-biblatex-manuscripts-philology-doc
Summary:        Documentation for biblatex-manuscripts-philology
Version:        svn45912
Provides:       tex-biblatex-manuscripts-philology-doc
AutoReqProv:    No

%description -n texlive-biblatex-manuscripts-philology-doc
Documentation for biblatex-manuscripts-philology

%package -n texlive-biblatex-mla
Provides:       tex-biblatex-mla = %{tl_version}
License:        LPPL
Summary:        MLA style files for biblatex
Version:        svn42445
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(standard.bbx)
Provides:       tex(mla.bbx) = %{tl_version}, tex(mla.cbx) = %{tl_version}

%description -n texlive-biblatex-mla
The package provides biblatex support for citations in the
format specified by the MLA handbook.

%package -n texlive-biblatex-mla-doc
Summary:        Documentation for biblatex-mla
Version:        svn42445
Provides:       tex-biblatex-mla-doc
AutoReqProv:    No

%description -n texlive-biblatex-mla-doc
Documentation for biblatex-mla

%package -n texlive-biblatex-multiple-dm
Provides:       tex-biblatex-multiple-dm = %{tl_version}
License:        LPPL 1.3
Summary:        Load multiple datamodels in biblatex
Version:        svn37081.1.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty), tex(etoolbox.sty)
Provides:       tex(biblatex-multiple-dm.sty) = %{tl_version}
Provides:       tex(multiple-dm.bbx) = %{tl_version}

%description -n texlive-biblatex-multiple-dm
The package adds the possibility to biblatex to load data
models from multiple sources.

%package -n texlive-biblatex-multiple-dm-doc
Summary:        Documentation for biblatex-multiple-dm
Version:        svn37081.1.0.1

Provides:       tex-biblatex-multiple-dm-doc
AutoReqProv:    No

%description -n texlive-biblatex-multiple-dm-doc
Documentation for biblatex-multiple-dm

%package -n texlive-biblatex-musuos
Provides:       tex-biblatex-musuos = %{tl_version}
License:        LPPL
Summary:        A biblatex style for citations in musuos.cls
Version:        svn24097.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(authortitle.bbx), tex(verbose-ibid.cbx)
Provides:       tex(musuos.bbx) = %{tl_version}, tex(musuos.cbx) = %{tl_version}

%description -n texlive-biblatex-musuos
The style is designed for use with the musuos class, but it
should be usable with other classes, too.

%package -n texlive-biblatex-musuos-doc
Summary:        Documentation for biblatex-musuos
Version:        svn24097.1.0

Provides:       tex-biblatex-musuos-doc
AutoReqProv:    No

%description -n texlive-biblatex-musuos-doc
Documentation for biblatex-musuos

%package -n texlive-biblatex-nature
Provides:       tex-biblatex-nature = %{tl_version}
License:        LPPL
Summary:        Biblatex support for Nature
Version:        svn43382
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(numeric-comp.bbx), tex(numeric-comp.cbx)
Provides:       tex(nature.bbx) = %{tl_version}, tex(nature.cbx) = %{tl_version}

%description -n texlive-biblatex-nature
The bundle offers styles that allow authors to use biblatex
when preparing papers for submission to the journal Nature.

%package -n texlive-biblatex-nature-doc
Summary:        Documentation for biblatex-nature
Version:        svn43382
Provides:       tex-biblatex-nature-doc
AutoReqProv:    No

%description -n texlive-biblatex-nature-doc
Documentation for biblatex-nature

%package -n texlive-biblatex-nejm
Provides:       tex-biblatex-nejm = %{tl_version}
License:        LPPL 1.3
Summary:        Biblatex style for the New England Journal of Medicine (NEJM)
Version:        svn24011.0.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(standard.bbx), tex(numeric-comp.cbx)
Provides:       tex(nejm.bbx) = %{tl_version}, tex(nejm.cbx) = %{tl_version}

%description -n texlive-biblatex-nejm
This is a biblatex numeric style based on the design of the New
England Journal of Medicine (NEJM).

%package -n texlive-biblatex-nejm-doc
Summary:        Documentation for biblatex-nejm
Version:        svn24011.0.4

Provides:       tex-biblatex-nejm-doc
AutoReqProv:    No

%description -n texlive-biblatex-nejm-doc
Documentation for biblatex-nejm

%package -n texlive-biblatex-opcit-booktitle
Provides:       tex-biblatex-opcit-booktitle = %{tl_version}
License:        LPPL 1.3
Summary:        Use op. cit. for the booktitle of a subentry
Version:        svn43621
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xpatch.sty)
Provides:       tex(biblatex-opcit-booktitle.sty) = %{tl_version}

%description -n texlive-biblatex-opcit-booktitle
The default citation styles verbose-trad1+; verbose-trad2 ;
verbose-trad3 use the op. cit. form in order to have shorter
reference when a title have been already cited. However, when
you cite two entries which share the same booktitle but not the
same title, the op. cit. mechanism does not work. This package
enables to obtain references like this: Author1, Title, in
Booktitle, Location, Publiser, Year, pages xxx Author2, Title2,
in Booktitle, op. cit, pages.

%package -n texlive-biblatex-opcit-booktitle-doc
Summary:        Documentation for biblatex-opcit-booktitle
Version:        svn43621
Provides:       tex-biblatex-opcit-booktitle-doc
AutoReqProv:    No

%description -n texlive-biblatex-opcit-booktitle-doc
Documentation for biblatex-opcit-booktitle

%package -n texlive-biblatex-philosophy
Provides:       tex-biblatex-philosophy = %{tl_version}
License:        LPPL 1.3
Summary:        Styles for using biblatex for work in philosophy
Version:        svn47283
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(authoryear.bbx), tex(authoryear-comp.cbx)
Requires:       tex(philosophy-classic.cbx), tex(standard.bbx)
Requires:       tex(authortitle.bbx), tex(verbose-trad2.cbx)
Provides:       tex(philosophy-classic.bbx) = %{tl_version}
Provides:       tex(philosophy-classic.cbx) = %{tl_version}
Provides:       tex(philosophy-modern.bbx) = %{tl_version}
Provides:       tex(philosophy-modern.cbx) = %{tl_version}
Provides:       tex(philosophy-standard.bbx) = %{tl_version}
Provides:       tex(philosophy-verbose.bbx) = %{tl_version}
Provides:       tex(philosophy-verbose.cbx) = %{tl_version}

%description -n texlive-biblatex-philosophy
The bundle offers two styles - philosophy-classic and
philosophy-modern - that facilitate the production of two
different kinds of bibliography, based on the authoryear style,
with options and features to manage the information about the
translation of foreign texts or their reprints. Though the
package's default settings are based on the conventions used in
Italian publications, these styles can be used with every
language recognized by babel, possibly with some simple
redefinitions.

%package -n texlive-biblatex-philosophy-doc
Summary:        Documentation for biblatex-philosophy
Version:        svn47283
Provides:       tex-biblatex-philosophy-doc
AutoReqProv:    No

%description -n texlive-biblatex-philosophy-doc
Documentation for biblatex-philosophy

%package -n texlive-biblatex-phys
Provides:       tex-biblatex-phys = %{tl_version}
License:        LPPL 1.3
Summary:        A biblatex implementation of the AIP and APS bibliography style
Version:        svn41922
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(numeric-comp.bbx), tex(numeric-comp.cbx)
Provides:       tex(phys.bbx) = %{tl_version}, tex(phys.cbx) = %{tl_version}

%description -n texlive-biblatex-phys
The biblatex-phys package provides an implementation of the
bibliography styles of both the AIP and the APS for biblatex.
This implementation follows standard biblatex conventions, and
can be used simply by loading biblatex with the appropriate
option: \usepackage[style=phys]{biblatex} A demonstration
database is provided to show how to format input for the style.
Style options are provided to cover the minor formatting
variations between the AIP and APS bibliography styles.

%package -n texlive-biblatex-phys-doc
Summary:        Documentation for biblatex-phys
Version:        svn41922
Provides:       tex-biblatex-phys-doc
AutoReqProv:    No

%description -n texlive-biblatex-phys-doc
Documentation for biblatex-phys

%package -n texlive-biblatex-publist
Provides:       tex-biblatex-publist = %{tl_version}
License:        LPPL 1.3
Summary:        BibLaTeX bibliography support for publication lists
Version:        svn47379
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(authoryear.bbx), tex(numeric.cbx)
Provides:       tex(publist.bbx) = %{tl_version}, tex(publist.cbx) = %{tl_version}

%description -n texlive-biblatex-publist
The package provides a BibLaTeX bibliography style file (*.bbx)
for publication lists. The style file draws on BibLaTeX's
authoryear style, but provides some extra features often
desired for publication lists, such as the omission of the
author's own name from author or editor data.

%package -n texlive-biblatex-publist-doc
Summary:        Documentation for biblatex-publist
Version:        svn47379
Provides:       tex-biblatex-publist-doc
AutoReqProv:    No

%description -n texlive-biblatex-publist-doc
Documentation for biblatex-publist

%package -n texlive-biblatex-realauthor
Provides:       tex-biblatex-realauthor = %{tl_version}
License:        LPPL 1.3
Summary:        Indicate the real author of a work
Version:        svn45865
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(verbose.bbx)
Provides:       tex(realauthor.bbx) = %{tl_version}

%description -n texlive-biblatex-realauthor
This package allows to use a new field "realauthor", which
indicates the real author of a work, when published in a
pseudepigraphic name.

%package -n texlive-biblatex-realauthor-doc
Summary:        Documentation for biblatex-realauthor
Version:        svn45865
Provides:       tex-biblatex-realauthor-doc
AutoReqProv:    No

%description -n texlive-biblatex-realauthor-doc
Documentation for biblatex-realauthor

%package -n texlive-biblatex-science
Provides:       tex-biblatex-science = %{tl_version}
License:        LPPL
Summary:        Biblatex implementation of the Science bibliography style
Version:        svn42147
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(numeric-comp.bbx), tex(numeric-comp.cbx)
Provides:       tex(science.bbx) = %{tl_version}, tex(science.cbx) = %{tl_version}

%description -n texlive-biblatex-science
The bundle offers styles that allow authors to use biblatex
when preparing papers for submission to the journal Science.

%package -n texlive-biblatex-science-doc
Summary:        Documentation for biblatex-science
Version:        svn42147
Provides:       tex-biblatex-science-doc
AutoReqProv:    No

%description -n texlive-biblatex-science-doc
Documentation for biblatex-science

%package -n texlive-biblatex-source-division
Provides:       tex-biblatex-source-division = %{tl_version}
License:        LPPL 1.3
Summary:        References by "division" in classical sources
Version:        svn45379
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xpatch.sty), tex(kvoptions.sty)
Provides:       tex(biblatex-source-division.sty) = %{tl_version}

%description -n texlive-biblatex-source-division
The package enables the user to make reference to "division
marks" (such as book, chapter, section), in the document being
referenced, in addition to the page-based references that
BibTeX-based citations have always had. The citation is made in
the same way as the LaTeX standard, but what's inside the
square brackets may include the "division" specification, as in
\cite[(<division spec.>)<page number>]{<document>}

%package -n texlive-biblatex-source-division-doc
Summary:        Documentation for biblatex-source-division
Version:        svn45379
Provides:       tex-biblatex-source-division-doc
AutoReqProv:    No

%description -n texlive-biblatex-source-division-doc
Documentation for biblatex-source-division

%package -n texlive-biblatex-subseries
Provides:       tex-biblatex-subseries = %{tl_version}
License:        LPPL 1.3
Summary:        Manages subseries with biblatex
Version:        svn43330
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(verbose.bbx)
Provides:       tex(subseries.bbx) = %{tl_version}

%description -n texlive-biblatex-subseries
Some publishers organize book series with subseries. In this
case, two numbers are associated with one volume: the number
inside the series and the number inside the subseries. That is
the case of the series Corpus Scriptorium Christianorum
Orientalium published by Peeters. This package provides new
fields to manage such system.

%package -n texlive-biblatex-subseries-doc
Summary:        Documentation for biblatex-subseries
Version:        svn43330
Provides:       tex-biblatex-subseries-doc
AutoReqProv:    No

%description -n texlive-biblatex-subseries-doc
Documentation for biblatex-subseries

%package -n texlive-biblatex-swiss-legal
Provides:       tex-biblatex-swiss-legal = %{tl_version}
License:        LPPL 1.3
Summary:        Bibliography and citation styles following Swiss legal practice
Version:        svn32750.1.1.2a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(biblatex-swiss-legal-base.cbx)
Provides:       tex(biblatex-swiss-legal-base.bbx) = %{tl_version}
Provides:       tex(biblatex-swiss-legal-base.cbx) = %{tl_version}
Provides:       tex(biblatex-swiss-legal-bibliography.bbx) = %{tl_version}
Provides:       tex(biblatex-swiss-legal-bibliography.cbx) = %{tl_version}
Provides:       tex(biblatex-swiss-legal-general.bbx) = %{tl_version}
Provides:       tex(biblatex-swiss-legal-general.cbx) = %{tl_version}
Provides:       tex(biblatex-swiss-legal-longarticle.bbx) = %{tl_version}
Provides:       tex(biblatex-swiss-legal-longarticle.cbx) = %{tl_version}
Provides:       tex(biblatex-swiss-legal-shortarticle.bbx) = %{tl_version}
Provides:       tex(biblatex-swiss-legal-shortarticle.cbx) = %{tl_version}

%description -n texlive-biblatex-swiss-legal
The package provides biblatex bibliography and citation styles
for documents written in accordance with Swiss legal citation
standards. Currently, the package is usable for French and
German documents.

%package -n texlive-biblatex-swiss-legal-doc
Summary:        Documentation for biblatex-swiss-legal
Version:        svn32750.1.1.2a

Provides:       tex-biblatex-swiss-legal-doc
AutoReqProv:    No

%description -n texlive-biblatex-swiss-legal-doc
Documentation for biblatex-swiss-legal

%package -n texlive-biblatex
Provides:       tex-biblatex = %{tl_version}
License:        LPPL
Summary:        Bibliographies in LaTeX using BibTeX for sorting only
Version:        svn46851
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(standard.bbx), tex(authoryear.bbx), tex(biblatex.sty), tex(etoolbox.sty)
Requires:       tex(keyval.sty), tex(logreq.sty), tex(ifthen.sty), tex(url.sty)
Requires:       tex(kvoptions.sty), tex(xstring.sty), tex(polyglossia.sty), tex(babel.sty)
Requires:       tex(csquotes.sty), tex(xpatch.sty), tex(authortitle.cbx)
Provides:       tex(alphabetic-verb.bbx) = %{tl_version}
Provides:       tex(alphabetic.bbx) = %{tl_version}, tex(authortitle-comp.bbx) = %{tl_version}
Provides:       tex(authortitle-ibid.bbx) = %{tl_version}
Provides:       tex(authortitle-icomp.bbx) = %{tl_version}
Provides:       tex(authortitle-tcomp.bbx) = %{tl_version}
Provides:       tex(authortitle-terse.bbx) = %{tl_version}
Provides:       tex(authortitle-ticomp.bbx) = %{tl_version}
Provides:       tex(authortitle.bbx) = %{tl_version}, tex(authoryear-comp.bbx) = %{tl_version}
Provides:       tex(authoryear-ibid.bbx) = %{tl_version}
Provides:       tex(authoryear-icomp.bbx) = %{tl_version}
Provides:       tex(authoryear.bbx) = %{tl_version}, tex(debug.bbx) = %{tl_version}
Provides:       tex(draft.bbx) = %{tl_version}, tex(numeric-comp.bbx) = %{tl_version}
Provides:       tex(numeric-verb.bbx) = %{tl_version}, tex(numeric.bbx) = %{tl_version}
Provides:       tex(reading.bbx) = %{tl_version}, tex(standard.bbx) = %{tl_version}
Provides:       tex(verbose-ibid.bbx) = %{tl_version}, tex(verbose-inote.bbx) = %{tl_version}
Provides:       tex(verbose-note.bbx) = %{tl_version}, tex(verbose-trad1.bbx) = %{tl_version}
Provides:       tex(verbose-trad2.bbx) = %{tl_version}, tex(verbose-trad3.bbx) = %{tl_version}
Provides:       tex(verbose.bbx) = %{tl_version}, tex(biblatex.cfg) = %{tl_version}
Provides:       tex(biblatex.def) = %{tl_version}, tex(biblatex.sty) = %{tl_version}
Provides:       tex(blx-bibtex.def) = %{tl_version}, tex(blx-compat.def) = %{tl_version}
Provides:       tex(blx-dm.def) = %{tl_version}, tex(blx-mcite.def) = %{tl_version}
Provides:       tex(blx-natbib.def) = %{tl_version}, tex(alphabetic-verb.cbx) = %{tl_version}
Provides:       tex(alphabetic.cbx) = %{tl_version}, tex(authortitle-comp.cbx) = %{tl_version}
Provides:       tex(authortitle-ibid.cbx) = %{tl_version}
Provides:       tex(authortitle-icomp.cbx) = %{tl_version}
Provides:       tex(authortitle-tcomp.cbx) = %{tl_version}
Provides:       tex(authortitle-terse.cbx) = %{tl_version}
Provides:       tex(authortitle-ticomp.cbx) = %{tl_version}
Provides:       tex(authortitle.cbx) = %{tl_version}, tex(authoryear-comp.cbx) = %{tl_version}
Provides:       tex(authoryear-ibid.cbx) = %{tl_version}
Provides:       tex(authoryear-icomp.cbx) = %{tl_version}
Provides:       tex(authoryear.cbx) = %{tl_version}, tex(debug.cbx) = %{tl_version}
Provides:       tex(draft.cbx) = %{tl_version}, tex(numeric-comp.cbx) = %{tl_version}
Provides:       tex(numeric-verb.cbx) = %{tl_version}, tex(numeric.cbx) = %{tl_version}
Provides:       tex(reading.cbx) = %{tl_version}, tex(verbose-ibid.cbx) = %{tl_version}
Provides:       tex(verbose-inote.cbx) = %{tl_version}, tex(verbose-note.cbx) = %{tl_version}
Provides:       tex(verbose-trad1.cbx) = %{tl_version}, tex(verbose-trad2.cbx) = %{tl_version}
Provides:       tex(verbose-trad3.cbx) = %{tl_version}, tex(verbose.cbx) = %{tl_version}

%description -n texlive-biblatex
Biblatex is a complete reimplementation of the bibliographic
facilities provided by LaTeX in conjunction with BibTeX. It
redesigns the way in which LaTeX interacts with BibTeX at a
fairly fundamental level. With biblatex, BibTeX is only used
(if it is used at all) to sort the bibliography and to generate
labels. Formatting of the bibliography is entirely controlled
by TeX macros (the BibTeX-based mechanism embeds some parts of
formatting in the BibTeX style file. Good working knowledge in
LaTeX should be sufficient to design new bibliography and
citation styles; nothing related to BibTeX's language is
needed. In fact, users need not remain bound to BibTeX for use
with biblatex: an alternative bibliography processor biblatex-
biber is available. Development of biblatex and biblatex-biber
is closely coupled; the present release of biblatex is designed
to work with biblatex-biber version 0.9.6. The package needs e-
TeX, and uses the author's etoolbox and logreq packages. For
users of biblatex-biber, version 0.9 is required (at least;
refer to the notes for the version of biblatex-biber that you
are using). Apart from the features unique to biblatex, the
package also incorporates core features of the following
packages: babelbib, bibtopic, bibunits, chapterbib, cite,
inlinebib, mcite and mciteplus, mlbib, multibib, splitbib.
Biblatex supports split bibliographies and multiple
bibliographies within one document, and separate lists of
bibliographic shorthands. Bibliographies may be subdivided into
parts (by chapter, by section, etc.) and/or segmented by topics
(by type, by keyword, etc.). Biblatex is fully localized and
can interface with the babel.

%package -n texlive-biblatex-doc
Summary:        Documentation for biblatex
Version:        svn46851
Provides:       tex-biblatex-doc
AutoReqProv:    No

%description -n texlive-biblatex-doc
Documentation for biblatex

%package -n texlive-biblatex-trad
Provides:       tex-biblatex-trad = %{tl_version}
License:        LPPL
Summary:        "Traditional" BibTeX styles with BibLaTeX
Version:        svn46668
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(standard.bbx), tex(numeric.cbx), tex(alphabetic.cbx)
Provides:       tex(trad-abbrv.bbx) = %{tl_version}, tex(trad-alpha.bbx) = %{tl_version}
Provides:       tex(trad-plain.bbx) = %{tl_version}, tex(trad-standard.bbx) = %{tl_version}
Provides:       tex(trad-unsrt.bbx) = %{tl_version}, tex(trad-abbrv.cbx) = %{tl_version}
Provides:       tex(trad-alpha.cbx) = %{tl_version}, tex(trad-plain.cbx) = %{tl_version}
Provides:       tex(trad-standard.cbx) = %{tl_version}, tex(trad-unsrt.cbx) = %{tl_version}

%description -n texlive-biblatex-trad
The bundle provides implementations of the "traditional" BibTeX
styles (plain, abbrev, unsrt and alpha) with BibLaTeX.

%package -n texlive-biblatex-trad-doc
Summary:        Documentation for biblatex-trad
Version:        svn46668
Provides:       tex-biblatex-trad-doc
AutoReqProv:    No

%description -n texlive-biblatex-trad-doc
Documentation for biblatex-trad

%package -n texlive-biblatex-true-citepages-omit
Provides:       tex-biblatex-true-citepages-omit = %{tl_version}
License:        LPPL 1.3
Summary:        Correction of some limitation of the citepages=omit option of biblatex styles
Version:        svn44653
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xstring.sty)
Provides:       tex(biblatex-true-citepages-omit.sty) = %{tl_version}

%description -n texlive-biblatex-true-citepages-omit
This package deals with a limitation of the citepages=omit
option of the verbose family of biblatex citestyles. The option
works when you \cite[xx]{key}, but not when you \cite[\pno~xx,
some text]{key}. The package corrects this problem.

%package -n texlive-biblatex-true-citepages-omit-doc
Summary:        Documentation for biblatex-true-citepages-omit
Version:        svn44653
Provides:       tex-biblatex-true-citepages-omit-doc
AutoReqProv:    No

%description -n texlive-biblatex-true-citepages-omit-doc
Documentation for biblatex-true-citepages-omit

%package -n texlive-bibleref-french
Provides:       tex-bibleref-french = %{tl_version}
License:        LPPL 1.3
Summary:        French translations for bibleref
Version:        svn35497.2.3.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(bibleref.sty), tex(etoolbox.sty)
Provides:       tex(bibleref-french.sty) = %{tl_version}

%description -n texlive-bibleref-french
The package provides translations and alternative typesetting
conventions for use of bibleref in French.

%package -n texlive-bibleref-french-doc
Summary:        Documentation for bibleref-french
Version:        svn35497.2.3.1

Provides:       tex-bibleref-french-doc
AutoReqProv:    No

%description -n texlive-bibleref-french-doc
Documentation for bibleref-french

%package -n texlive-bibleref-german
Provides:       tex-bibleref-german = %{tl_version}
License:        LPPL 1.3
Summary:        German adaptation of bibleref
Version:        svn21923.1.0a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(bibleref.sty), tex(etoolbox.sty)
Provides:       tex(bibleref-german.sty) = %{tl_version}

%description -n texlive-bibleref-german
The package provides translations and various formats for the
use of bibleref in German documents. The German naming of the
bible books complies with the 'Loccumer Richtlinien' (Locum
guidelines). In addition, the Vulgate (Latin bible) is
supported.

%package -n texlive-bibleref-german-doc
Summary:        Documentation for bibleref-german
Version:        svn21923.1.0a

Provides:       tex-bibleref-german-doc
AutoReqProv:    No

%description -n texlive-bibleref-german-doc
Documentation for bibleref-german

%package -n texlive-bibleref-lds
Provides:       tex-bibleref-lds = %{tl_version}
License:        LPPL 1.3
Summary:        Bible references, including those to the scriptures of the Church of Jesus Christ of Latter Day Saints
Version:        svn25526.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(bibleref-mouth.sty), tex(ifthen.sty)
Requires:       tex(hyperref.sty)
Provides:       tex(bibleref-lds.sty) = %{tl_version}

%description -n texlive-bibleref-lds
The package extends the bibleref-mouth package to support
references to the scriptures of The Church of Jesus Christ of
Latter-day Saints (LDS). The package requires bibleref-mouth to
run, and its reference syntax is the same as that of the parent
package.

%package -n texlive-bibleref-lds-doc
Summary:        Documentation for bibleref-lds
Version:        svn25526.1.0

Provides:       tex-bibleref-lds-doc
AutoReqProv:    No

%description -n texlive-bibleref-lds-doc
Documentation for bibleref-lds

%package -n texlive-bibleref-mouth
Provides:       tex-bibleref-mouth = %{tl_version}
License:        LPPL 1.3
Summary:        Consistent formatting of Bible references
Version:        svn25527.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fmtcount.sty), tex(hyperref.sty)
Provides:       tex(bibleref-mouth.sty) = %{tl_version}

%description -n texlive-bibleref-mouth
The package allows Bible references to be formatted in a
consistent way. It is similar to the bibleref package, except
that the formatting macros are all purely expandable -- that
is, they are all implemented in TeX's mouth. This means that
they can be used in any expandable context, such as an argument
to a \url command.

%package -n texlive-bibleref-mouth-doc
Summary:        Documentation for bibleref-mouth
Version:        svn25527.1.0

Provides:       tex-bibleref-mouth-doc
AutoReqProv:    No

%description -n texlive-bibleref-mouth-doc
Documentation for bibleref-mouth

%package -n texlive-bibleref-parse
Provides:       tex-bibleref-parse = %{tl_version}
License:        LPPL 1.3
Summary:        Specify Bible passages in human-readable format
Version:        svn22054.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty), tex(scrlfile.sty), tex(bibleref.sty)
Provides:       tex(bibleref-parse.sty) = %{tl_version}

%description -n texlive-bibleref-parse
The package parses Bible passages that are given in human
readable format. It accepts a wide variety of formats. This
allows for a simpler and more convenient interface to the
functionality of the bibleref package.

%package -n texlive-bibleref-parse-doc
Summary:        Documentation for bibleref-parse
Version:        svn22054.1.1

Provides:       tex-bibleref-parse-doc
AutoReqProv:    No

%description -n texlive-bibleref-parse-doc
Documentation for bibleref-parse

%package -n texlive-bibleref
Provides:       tex-bibleref = %{tl_version}
License:        LPPL 1.3
Summary:        Format bible citations
Version:        svn48319
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty), tex(fmtcount.sty), tex(amsgen.sty)
Provides:       tex(bibleref.sty) = %{tl_version}

%description -n texlive-bibleref
The bibleref package offers consistent formatting of references
to parts of the Christian bible, in a number of well-defined
formats.

%package -n texlive-bibleref-doc
Summary:        Documentation for bibleref
Version:        svn48319
Provides:       tex-bibleref-doc
AutoReqProv:    No

%description -n texlive-bibleref-doc
Documentation for bibleref

%package -n texlive-biblist
Provides:       tex-biblist = %{tl_version}
License:        GPL+
Summary:        Print a BibTeX database
Version:        svn17116.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(biblist.sty) = %{tl_version}

%description -n texlive-biblist
The package provides the means of listing an entire BibTeX
database, avoiding the potentially large (macro) impact
associated with \nocite{*}.

%package -n texlive-biblist-doc
Summary:        Documentation for biblist
Version:        svn17116.0

Provides:       tex-biblist-doc
AutoReqProv:    No

%description -n texlive-biblist-doc
Documentation for biblist

%package -n texlive-bibtopicprefix
Provides:       tex-bibtopicprefix = %{tl_version}
License:        LPPL
Summary:        Prefix references to bibliographies produced by bibtopic
Version:        svn15878.1.10

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(scrlfile.sty), tex(bibtopic.sty)
Provides:       tex(bibtopicprefix.sty) = %{tl_version}

%description -n texlive-bibtopicprefix
The package permits users to apply prefixes (fixed strings) to
references to entries in bibliographies produced by the
bibtopic package.

%package -n texlive-bibtopicprefix-doc
Summary:        Documentation for bibtopicprefix
Version:        svn15878.1.10

Provides:       tex-bibtopicprefix-doc
AutoReqProv:    No

%description -n texlive-bibtopicprefix-doc
Documentation for bibtopicprefix

%package -n texlive-bibtopic
Provides:       tex-bibtopic = %{tl_version}
License:        GPL+
Summary:        Include multiple bibliographies in a document
Version:        svn15878.1.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(bibtopic.sty) = %{tl_version}

%description -n texlive-bibtopic
The package allows the user to include several bibliographies
covering different 'topics' or bibliographic material into a
document (e.g., one bibliography for primary literature and one
for secondary literature). The package provides commands to
include either all references from a .bib file, only the
references actually cited or those not cited in your document.
The user has to construct a separate .bib file for each
bibliographic 'topic', each of which will be processed
separately by BibTeX. If you want to have bibliographies
specific to one part of a document, see the packages bibunits
or chapterbib.

%package -n texlive-bibtopic-doc
Summary:        Documentation for bibtopic
Version:        svn15878.1.1a

Provides:       tex-bibtopic-doc
AutoReqProv:    No

%description -n texlive-bibtopic-doc
Documentation for bibtopic

%package -n texlive-bibunits
Provides:       tex-bibunits = %{tl_version}
License:        LPPL
Summary:        Multiple bibliographies in one document
Version:        svn15878.2.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bibunits.sty) = %{tl_version}

%description -n texlive-bibunits
The package provide a mechanism to generate separate
bibliographies for different units (chapters, sections or
bibunit-environments) of a text. The package separates the
citations of each unit of text into a separate file to be
processed by BibTeX. The global bibliography section produced
by LaTeX may also appear in the document and citations can be
placed in both the local unit and the global bibliographies at
the same time. The package is compatible with koma-script and
with the babel French option frenchb.

%package -n texlive-bibunits-doc
Summary:        Documentation for bibunits
Version:        svn15878.2.2

Provides:       tex-bibunits-doc
AutoReqProv:    No

%description -n texlive-bibunits-doc
Documentation for bibunits

%package -n texlive-bidi-atbegshi
Provides:       tex-bidi-atbegshi = %{tl_version}
License:        LPPL 1.3
Summary:        Bidi-aware shipout macros
Version:        svn35154.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(atbegshi.sty)
Provides:       tex(bidi-atbegshi.sty) = %{tl_version}

%description -n texlive-bidi-atbegshi
The package adds some commands to the atbegshi package for
proper placement of background material in the left and right
corners of the output page, in both LTR and RTL modes. The
package only works with xelatex format and should be loaded
before the bidi package.

%package -n texlive-bidi-atbegshi-doc
Summary:        Documentation for bidi-atbegshi
Version:        svn35154.0.1

Provides:       tex-bidi-atbegshi-doc
AutoReqProv:    No

%description -n texlive-bidi-atbegshi-doc
Documentation for bidi-atbegshi

%package -n texlive-bidicontour
Provides:       tex-bidicontour = %{tl_version}
License:        LPPL 1.3
Summary:        Bidi-aware coloured contour around text
Version:        svn34631.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty), tex(trig.sty)
Provides:       tex(bidicontour.sty) = %{tl_version}

%description -n texlive-bidicontour
The package is a re-implementation of the contour package,
making it bidi-aware, and adding support of the xdvipdfmx (when
the outline option of the package is used).

%package -n texlive-bidicontour-doc
Summary:        Documentation for bidicontour
Version:        svn34631.0.2

Provides:       tex-bidicontour-doc
AutoReqProv:    No

%description -n texlive-bidicontour-doc
Documentation for bidicontour

%package -n texlive-bidihl
Provides:       tex-bidihl = %{tl_version}
License:        LPPL 1.3
Summary:        Experimental bidi-aware text highlighting
Version:        svn37795.0.1c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty)
Provides:       tex(bidihl.sty) = %{tl_version}

%description -n texlive-bidihl
Experimental bidi-aware text highlighting.

%package -n texlive-bidihl-doc
Summary:        Documentation for bidihl
Version:        svn37795.0.1c

Provides:       tex-bidihl-doc
AutoReqProv:    No

%description -n texlive-bidihl-doc
Documentation for bidihl

%package -n texlive-bidipagegrid
Provides:       tex-bidipagegrid = %{tl_version}
License:        LPPL 1.3
Summary:        Bidi-aware page grid in background
Version:        svn34632.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(atbegshi.sty), tex(kvoptions.sty)
Provides:       tex(bidipagegrid.sty) = %{tl_version}

%description -n texlive-bidipagegrid
The package is based on pagegrid.

%package -n texlive-bidipagegrid-doc
Summary:        Documentation for bidipagegrid
Version:        svn34632.0.2

Provides:       tex-bidipagegrid-doc
AutoReqProv:    No

%description -n texlive-bidipagegrid-doc
Documentation for bidipagegrid

%package -n texlive-bidipresentation
Provides:       tex-bidipresentation = %{tl_version}
License:        LPPL 1.3
Summary:        Experimental bidi presentation
Version:        svn35267.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(scrlfile.sty), tex(fancyhdr.sty), tex(ifthen.sty), tex(calc.sty)
Requires:       tex(keyval.sty), tex(geometry.sty), tex(hyperref.sty), tex(color.sty)
Requires:       tex(xecolor.sty)
Provides:       tex(bidiprescolors.cfg) = %{tl_version}, tex(bidipresentation.cls) = %{tl_version}

%description -n texlive-bidipresentation
A great portion of the code is borrowed from the texpower
bundle, with modifications to get things working properly in
both right to left and left to right modes.

%package -n texlive-bidipresentation-doc
Summary:        Documentation for bidipresentation
Version:        svn35267.0.3

Provides:       tex-bidipresentation-doc
AutoReqProv:    No

%description -n texlive-bidipresentation-doc
Documentation for bidipresentation

%package -n texlive-bidishadowtext
Provides:       tex-bidishadowtext = %{tl_version}
License:        LPPL 1.3
Summary:        Bidi-aware shadow text
Version:        svn34633.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty)
Provides:       tex(bidishadowtext.sty) = %{tl_version}

%description -n texlive-bidishadowtext
This package allows you to typeset Bidi-aware shadow text. It
is a re-implementation of the shadowtext package adding bidi
support.

%package -n texlive-bidishadowtext-doc
Summary:        Documentation for bidishadowtext
Version:        svn34633.0.1

Provides:       tex-bidishadowtext-doc
AutoReqProv:    No

%description -n texlive-bidishadowtext-doc
Documentation for bidishadowtext

%package -n texlive-bidi
Provides:       tex-bidi = %{tl_version}
License:        LPPL 1.3
Summary:        Bidirectional typesetting in plain TeX and LaTeX, using XeTeX engine
Version:        svn48397
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(iftex.sty), tex(zref-abspage.sty), tex(auxhook.sty), tex(ltxcmds.sty)
Requires:       tex(xkeyval.sty), tex(xcolor.sty), tex(showexpl.sty), tex(color.sty)
Requires:       tex(graphicx.sty), tex(ifthen.sty), tex(marvosym.sty), tex(url.sty)
Requires:       tex(hyperref.sty), tex(fancyhdr.sty), tex(bidituftesidenote.sty), tex(bidituftegeneralstructure.sty)
Requires:       tex(bidituftetitle.sty), tex(xifthen.sty)
Requires:       tex(ragged2e.sty), tex(geometry.sty), tex(changepage.sty), tex(chngpage.sty)
Requires:       tex(optparams.sty), tex(placeins.sty), tex(paralist.sty), tex(multicol.sty)
Requires:       tex(setspace.sty), tex(natbib.sty), tex(bibentry.sty), tex(titlesec.sty)
Requires:       tex(titletoc.sty)
Provides:       tex(adjmulticol-xetex-bidi.def) = %{tl_version}
Provides:       tex(algorithm2e-xetex-bidi.def) = %{tl_version}
Provides:       tex(amsart-xetex-bidi.def) = %{tl_version}
Provides:       tex(amsbook-xetex-bidi.def) = %{tl_version}
Provides:       tex(amsmath-xetex-bidi.def) = %{tl_version}
Provides:       tex(amstext-xetex-bidi.def) = %{tl_version}
Provides:       tex(amsthm-xetex-bidi.def) = %{tl_version}
Provides:       tex(array-xetex-bidi.def) = %{tl_version}
Provides:       tex(article-xetex-bidi.def) = %{tl_version}
Provides:       tex(artikel1-xetex-bidi.def) = %{tl_version}
Provides:       tex(artikel2-xetex-bidi.def) = %{tl_version}
Provides:       tex(artikel3-xetex-bidi.def) = %{tl_version}
Provides:       tex(arydshln-xetex-bidi.def) = %{tl_version}
Provides:       tex(bidi-longtable.sty) = %{tl_version}, tex(bidi.sty) = %{tl_version}
Provides:       tex(bidi.tex) = %{tl_version}, tex(bidi2in1.sty) = %{tl_version}
Provides:       tex(bidicode.sty) = %{tl_version}, tex(bidiftnxtra.sty) = %{tl_version}
Provides:       tex(bidimoderncv.cls) = %{tl_version}, tex(bidipoem.sty) = %{tl_version}
Provides:       tex(biditools.sty) = %{tl_version}, tex(biditufte-book.cls) = %{tl_version}
Provides:       tex(biditufte-handout.cls) = %{tl_version}
Provides:       tex(bidituftefloat.sty) = %{tl_version}, tex(bidituftegeneralstructure.sty) = %{tl_version}
Provides:       tex(bidituftehyperref.sty) = %{tl_version}
Provides:       tex(bidituftesidenote.sty) = %{tl_version}
Provides:       tex(bidituftetitle.sty) = %{tl_version}, tex(bidituftetoc.sty) = %{tl_version}
Provides:       tex(boek-xetex-bidi.def) = %{tl_version}
Provides:       tex(boek3-xetex-bidi.def) = %{tl_version}
Provides:       tex(book-xetex-bidi.def) = %{tl_version}
Provides:       tex(bookest-xetex-bidi.def) = %{tl_version}
Provides:       tex(breqn-xetex-bidi.def) = %{tl_version}
Provides:       tex(cals-xetex-bidi.def) = %{tl_version}
Provides:       tex(caption-xetex-bidi.def) = %{tl_version}
Provides:       tex(caption3-xetex-bidi.def) = %{tl_version}
Provides:       tex(color-xetex-bidi.def) = %{tl_version}
Provides:       tex(colortbl-xetex-bidi.def) = %{tl_version}
Provides:       tex(combine-xetex-bidi.def) = %{tl_version}
Provides:       tex(crop-xetex-bidi.def) = %{tl_version}
Provides:       tex(cuted-xetex-bidi.def) = %{tl_version}
Provides:       tex(cutwin-xetex-bidi.def) = %{tl_version}
Provides:       tex(cvthemebidicasual.sty) = %{tl_version}
Provides:       tex(cvthemebidiclassic.sty) = %{tl_version}
Provides:       tex(dblfnote-xetex-bidi.def) = %{tl_version}
Provides:       tex(draftwatermark-xetex-bidi.def) = %{tl_version}
Provides:       tex(empheq-xetex-bidi.def) = %{tl_version}
Provides:       tex(eso-pic-xetex-bidi.def) = %{tl_version}
Provides:       tex(extarticle-xetex-bidi.def) = %{tl_version}
Provides:       tex(extbook-xetex-bidi.def) = %{tl_version}
Provides:       tex(extletter-xetex-bidi.def) = %{tl_version}
Provides:       tex(extrafootnotefeatures-xetex-bidi.def) = %{tl_version}
Provides:       tex(extreport-xetex-bidi.def) = %{tl_version}
Provides:       tex(fancybox-xetex-bidi.def) = %{tl_version}
Provides:       tex(fancyhdr-xetex-bidi.def) = %{tl_version}
Provides:       tex(fix2col-xetex-bidi.def) = %{tl_version}
Provides:       tex(fleqn-xetex-bidi.def) = %{tl_version}
Provides:       tex(float-xetex-bidi.def) = %{tl_version}
Provides:       tex(floatrow-xetex-bidi.def) = %{tl_version}
Provides:       tex(flowfram-xetex-bidi.def) = %{tl_version}
Provides:       tex(footnote-xetex-bidi.def) = %{tl_version}
Provides:       tex(framed-xetex-bidi.def) = %{tl_version}
Provides:       tex(ftnright-xetex-bidi.def) = %{tl_version}
Provides:       tex(geometry-xetex-bidi.def) = %{tl_version}
Provides:       tex(graphicx-xetex-bidi.def) = %{tl_version}
Provides:       tex(hvfloat-xetex-bidi.def) = %{tl_version}
Provides:       tex(hyperref-xetex-bidi.def) = %{tl_version}
Provides:       tex(latex-xetex-bidi.def) = %{tl_version}
Provides:       tex(leqno-xetex-bidi.def) = %{tl_version}
Provides:       tex(letter-xetex-bidi.def) = %{tl_version}
Provides:       tex(lettrine-xetex-bidi.def) = %{tl_version}
Provides:       tex(listings-xetex-bidi.def) = %{tl_version}
Provides:       tex(loadingorder-xetex-bidi.def) = %{tl_version}
Provides:       tex(longtable-xetex-bidi.def) = %{tl_version}
Provides:       tex(mdframed-xetex-bidi.def) = %{tl_version}
Provides:       tex(memoir-xetex-bidi.def) = %{tl_version}
Provides:       tex(midfloat-xetex-bidi.def) = %{tl_version}
Provides:       tex(minitoc-xetex-bidi.def) = %{tl_version}
Provides:       tex(multicol-xetex-bidi.def) = %{tl_version}
Provides:       tex(multienum-xetex-bidi.def) = %{tl_version}
Provides:       tex(natbib-xetex-bidi.def) = %{tl_version}
Provides:       tex(newfloat-xetex-bidi.def) = %{tl_version}
Provides:       tex(ntheorem-hyper-xetex-bidi.def) = %{tl_version}
Provides:       tex(ntheorem-xetex-bidi.def) = %{tl_version}
Provides:       tex(pdfpages-xetex-bidi.def) = %{tl_version}
Provides:       tex(pgf-xetex-bidi.def) = %{tl_version}, tex(picinpar-xetex-bidi.def) = %{tl_version}
Provides:       tex(plain-xetex-bidi.def) = %{tl_version}
Provides:       tex(pstricks-xetex-bidi.def) = %{tl_version}
Provides:       tex(quotchap-xetex-bidi.def) = %{tl_version}
Provides:       tex(ragged2e-xetex-bidi.def) = %{tl_version}
Provides:       tex(rapport1-xetex-bidi.def) = %{tl_version}
Provides:       tex(rapport3-xetex-bidi.def) = %{tl_version}
Provides:       tex(refrep-xetex-bidi.def) = %{tl_version}
Provides:       tex(report-xetex-bidi.def) = %{tl_version}
Provides:       tex(rotating-xetex-bidi.def) = %{tl_version}
Provides:       tex(scrartcl-xetex-bidi.def) = %{tl_version}
Provides:       tex(scrbook-xetex-bidi.def) = %{tl_version}
Provides:       tex(scrlettr-xetex-bidi.def) = %{tl_version}
Provides:       tex(scrreprt-xetex-bidi.def) = %{tl_version}
Provides:       tex(sidecap-xetex-bidi.def) = %{tl_version}
Provides:       tex(stabular-xetex-bidi.def) = %{tl_version}
Provides:       tex(subfigure-xetex-bidi.def) = %{tl_version}
Provides:       tex(tabls-xetex-bidi.def) = %{tl_version}
Provides:       tex(tabularx-xetex-bidi.def) = %{tl_version}
Provides:       tex(tabulary-xetex-bidi.def) = %{tl_version}
Provides:       tex(tc-xetex-bidi.def) = %{tl_version}, tex(tikz-xetex-bidi.def) = %{tl_version}
Provides:       tex(titlesec-xetex-bidi.def) = %{tl_version}
Provides:       tex(titletoc-xetex-bidi.def) = %{tl_version}
Provides:       tex(tocbibind-xetex-bidi.def) = %{tl_version}
Provides:       tex(tocloft-xetex-bidi.def) = %{tl_version}
Provides:       tex(tocstyle-xetex-bidi.def) = %{tl_version}
Provides:       tex(todonotes-xetex-bidi.def) = %{tl_version}
Provides:       tex(wrapfig-xetex-bidi.def) = %{tl_version}
Provides:       tex(xcolor-xetex-bidi.def) = %{tl_version}
Provides:       tex(xltxtra-xetex-bidi.def) = %{tl_version}

%description -n texlive-bidi
A convenient interface for typesetting bidirectional texts with
plain TeX and LaTeX. The package includes adaptations for use
with many other commonly-used packages.

%package -n texlive-bidi-doc
Summary:        Documentation for bidi
Version:        svn48397
Provides:       tex-bidi-doc
AutoReqProv:    No

%description -n texlive-bidi-doc
Documentation for bidi

%package -n texlive-bigfoot
Provides:       tex-bigfoot = %{tl_version}
License:        GPLv2+
Summary:        Footnotes for critical editions
Version:        svn38248.2.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etex.sty), tex(manyfoot.sty), tex(perpage.sty)
Provides:       tex(bigfoot.sty) = %{tl_version}, tex(perpage.sty) = %{tl_version}
Provides:       tex(suffix.sty) = %{tl_version}

%description -n texlive-bigfoot
The package aims to provide a 'one-stop' solution to
requirements for footnotes. It offers: Multiple footnote
apparatus superior to that of manyfoot Footnotes can be
formatted in separate paragraphs, or be run into a single
paragraph (this choice may be selected per footnote series);
Things you might have expected (such as \verb-like material in
footnotes, and colour selections over page breaks) now work.
Note that the majority of the bigfoot package's interface is
identical to that of manyfoot; users should seek information
from that package's documentation. The bigfoot bundle also
provides the perpage and suffix packages.

%package -n texlive-bigfoot-doc
Summary:        Documentation for bigfoot
Version:        svn38248.2.1

Provides:       tex-bigfoot-doc
AutoReqProv:    No

%description -n texlive-bigfoot-doc
Documentation for bigfoot

%package -n texlive-bigints
Provides:       tex-bigints = %{tl_version}
License:        LPPL
Summary:        Writing big integrals
Version:        svn29803.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amsmath.sty)
Provides:       tex(bigints.sty) = %{tl_version}

%description -n texlive-bigints
The package provides facilities for drawing big integral signs
when needed. An example would be when the integrand is a
matrix.

%package -n texlive-bigints-doc
Summary:        Documentation for bigints
Version:        svn29803.0

Provides:       tex-bigints-doc
AutoReqProv:    No

%description -n texlive-bigints-doc
Documentation for bigints

%package -n texlive-binomexp
Provides:       tex-binomexp = %{tl_version}
License:        LPPL
Summary:        Calculate Pascal's triangle
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(ifthen.sty)
Provides:       tex(binomexp.sty) = %{tl_version}

%description -n texlive-binomexp
The package calculates and prints rows of Pascal's triangle. It
may be used: simply to print successive rows of the triangle,
or to print the rows inside an array or tabular.

%package -n texlive-binomexp-doc
Summary:        Documentation for binomexp
Version:        svn15878.1.0

Provides:       tex-binomexp-doc
AutoReqProv:    No

%description -n texlive-binomexp-doc
Documentation for binomexp

%package -n texlive-biocon
Provides:       tex-biocon = %{tl_version}
License:        GPL+
Summary:        Typesetting biological species names
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty), tex(ifthen.sty)
Provides:       tex(biocon-old.sty) = %{tl_version}, tex(biocon.sty) = %{tl_version}
Provides:       tex(biocon.sty) = %{tl_version}

%description -n texlive-biocon
The biocon--biological conventions--package aids the
typesetting of some biological conventions. At the moment, it
makes a good job of typesetting species names (and ranks below
the species level). A distinction is made between the Plant,
Fungi, Animalia and Bacteria kingdoms. There are default
settings for the way species names are typeset, but they can be
customized. Different default styles are used in different
situations.

%package -n texlive-biocon-doc
Summary:        Documentation for biocon
Version:        svn15878.0

Provides:       tex-biocon-doc
AutoReqProv:    No

%description -n texlive-biocon-doc
Documentation for biocon

%package -n texlive-bitelist
Provides:       tex-bitelist = %{tl_version}
License:        LPPL 1.3
Summary:        Split list, in TeX's mouth
Version:        svn25779.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bitedemo.tex) = %{tl_version}, tex(bitelist.sty) = %{tl_version}

%description -n texlive-bitelist
The package provides commands for "splitting" a token list at
the first occurrence of another (specified) token list. I.e.,
for given token lists s, t return b and the shortest a, such
that t = a s b. The package's mechanism differs from those of
packages providing similar features, in the following ways: the
method uses TeX's mechanism of reading delimited macro
parameters; splitting macros work by pure expansion, without
assignments; the operation is carried out in a single macro
call. A variant of the operation is provided, that retains
outer braces.

%package -n texlive-bitelist-doc
Summary:        Documentation for bitelist
Version:        svn25779.0.1

Provides:       tex-bitelist-doc
AutoReqProv:    No

%description -n texlive-bitelist-doc
Documentation for bitelist

%package -n texlive-bizcard
Provides:       tex-bizcard = %{tl_version}
License:        GPL+
Summary:        Typeset business cards
Version:        svn15878.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(geometry.sty)
Provides:       tex(bizcard.sty) = %{tl_version}

%description -n texlive-bizcard
This is an adaption for current LaTeX of a LaTeX 2.09 style by
Silvano Balemi. It produces cards at the normal US card size,
76.2mm x 50.8mm.

%package -n texlive-bizcard-doc
Summary:        Documentation for bizcard
Version:        svn15878.1.1

Provides:       tex-bizcard-doc
AutoReqProv:    No

%description -n texlive-bizcard-doc
Documentation for bizc

%package -n texlive-beamercolorthemeowl-doc
Provides:       tex-beamercolorthemeowl-doc = %{tl_version}
License:        LPPL
Summary:        doc files of beamercolorthemeowl
Version:        svn40105

AutoReqProv:    No

%description -n texlive-beamercolorthemeowl-doc
Documentation for beamercolorthemeowl

%package -n texlive-beamercolorthemeowl
Provides:       tex-beamercolorthemeowl = %{tl_version}
License:        LPPL
Summary:        A flexible beamer color theme to maximize visibility
Version:        svn40105

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(beamercolorthemeowl.sty) = %{tl_version}

%description -n texlive-beamercolorthemeowl
This package provides a flexible dark or light colour theme
designed for maximum readability in environments where most
themes fall flat. Main features: Dark color theme for
presenting in low-light conditions. Optional light color theme
for presenting in bright ambient light. Redefines color names
"red", "green", "blue", "yellow" to values that are visible
when displayed by certain projectors, particularly those with a
very bright green channel and dim red and blue channels. This
behaviour can be optionally disabled, with the provided colours
also available as "OwlRed", "OwlGreen", etc.

%package -n texlive-beamertheme-detlevcm-doc
Provides:       tex-beamertheme-detlevcm-doc = %{tl_version}
Provides:       tex-detlev-cm-doc = %{tl_version}, texlive-devlev-cm-doc = %{tl_version}
Obsoletes:      texlive-devlev-cm-doc < 2016
License:        GPL+
Summary:        doc files of beamertheme-detlevcm
Version:        svn39048

AutoReqProv:    No

%description -n texlive-beamertheme-detlevcm-doc
Documentation for beamertheme-detlevcm

%package -n texlive-beamertheme-detlevcm
Provides:       tex-beamertheme-detlevcm = %{tl_version}
Provides:       tex-detlev-cm = %{tl_version}, texlive-devlev-cm = %{tl_version}
Obsoletes:      texlive-devlev-cm < 2016
License:        GPL+
Summary:        A beamer theme designed for use in the University of Leeds
Version:        svn39048

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(beamerthemeDetlevCM.sty) = %{tl_version}
Provides:       tex(beamercolorthemeETII.sty) = %{tl_version}
Provides:       tex(beamerfontthemeDetlevCM.sty) = %{tl_version}
Provides:       tex(beamerouterthemeDetlevCM.sty) = %{tl_version}

%description -n texlive-beamertheme-detlevcm
The bundle provides a simple theme that has been used in the
author's department.

%package -n texlive-beamertheme-epyt-doc
Provides:       tex-beamertheme-epyt-doc = %{tl_version}
Provides:       texlive-epyt-doc = %{tl_version}, tex-epyt-doc = %{tl_version}
Obsoletes:      texlive-epyt-doc < 2016
License:        LPPL
Summary:        doc files of beamertheme-epyt
Version:        svn41404
AutoReqProv:    No

%description -n texlive-beamertheme-epyt-doc
Documentation for beamertheme-epyt

%package -n texlive-beamertheme-epyt
Provides:       tex-beamertheme-epyt = %{tl_version}, texlive-epyt = %{tl_version}
Provides:       tex-epyt = %{tl_version}
Obsoletes:      texlive-epyt < 2016
License:        LPPL
Summary:        A simple and clean theme for LaTeX beamer class
Version:        svn41404
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(beamerthemeepyt.sty) = %{tl_version}

%description -n texlive-beamertheme-epyt
This package provides a simple but nice theme for Beamer, with
the following features: simple structure: with page numbers at
footer, no head bar and side bar simple templates: displaying
theorems with traditional inline style simple colors: using
only several foreground and background colors

%package -n texlive-beamertheme-metropolis-doc
Provides:       tex-beamertheme-metropolis-doc = %{tl_version}
License:        CC-BY-SA
Summary:        doc files of beamertheme-metropolis
Version:        svn43031

%description -n texlive-beamertheme-metropolis-doc
Documentation for beamertheme-metropolis

%package -n texlive-beamertheme-metropolis
Provides:       tex-beamertheme-metropolis = %{tl_version}
License:        CC-BY-SA
Summary:        A modern LaTeX beamer theme
Version:        svn43031
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(beamer.cls), tex(tikz.sty), tex(etoolbox.sty), tex(ifxetex.sty)
Requires:       tex(pgfopts.sty), tex(calc.sty), tex(ifluatex.sty), texlive-fira
Provides:       tex(beamerfontthememetropolis.sty) = %{tl_version}
Provides:       tex(beamerinnerthememetropolis.sty) = %{tl_version}
Provides:       tex(beamercolorthememetropolis.sty) = %{tl_version}
Provides:       tex(beamerthememetropolis.sty) = %{tl_version}
Provides:       tex(pgfplotsthemetol.sty) = %{tl_version}
Provides:       tex(beamerouterthememetropolis.sty) = %{tl_version}

%description -n texlive-beamertheme-metropolis
The package provides a simple, modern Beamer theme for anyone
to use. It tries to minimize noise and maximize space for
content.

%package -n texlive-beamer-verona-doc
Provides:       tex-beamer-verona-doc = %{tl_version}
License:        LPPL
Summary:        doc files of beamer-verona
Version:        svn39180

AutoReqProv:    No

%description -n texlive-beamer-verona-doc
Documentation for beamer-verona

%package -n texlive-beamer-verona
Provides:       tex-beamer-verona = %{tl_version}
License:        LPPL
Summary:        A theme for the beamer class
Version:        svn39180

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(beamerthemeVerona.sty) = %{tl_version}

%description -n texlive-beamer-verona
This package provides the 'Verona' theme for the beamer class
by Till Tantau.

%package -n texlive-biblatex-abnt-doc
Provides:       tex-biblatex-abnt-doc = %{tl_version}
License:        LPPL
Summary:        doc files of biblatex-abnt
Version:        svn47291
AutoReqProv:    No

%description -n texlive-biblatex-abnt-doc
Documentation for biblatex-abnt

%package -n texlive-biblatex-abnt
Provides:       tex-biblatex-abnt = %{tl_version}
License:        LPPL
Summary:        BibLaTeX style for Brazil's ABNT rules
Version:        svn47291
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(abnt-numeric.bbx) = %{tl_version}, tex(abnt-numeric.cbx) = %{tl_version}
Provides:       tex(abnt.bbx) = %{tl_version}, tex(abnt.cbx) = %{tl_version}

%description -n texlive-biblatex-abnt
This package offers a BibLaTeX style for Brazil's ABNT
(Brazilian Association of Technical Norms) rules.

%package -n texlive-biblatex-bookinother-doc
Provides:       tex-biblatex-bookinother-doc = %{tl_version}
License:        LPPL
Summary:        doc files of biblatex-bookinother
Version:        svn45856
AutoReqProv:    No

%description -n texlive-biblatex-bookinother-doc
Documentation for biblatex-bookinother

%package -n texlive-biblatex-bookinother
Provides:       tex-biblatex-bookinother = %{tl_version}
License:        LPPL
Summary:        Manage book edited in other entry type
Version:        svn45856
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(bookinother.bbx) = %{tl_version}

%description -n texlive-biblatex-bookinother
This package provides new BibLaTeX entry types and fields for
book edited in other types, like for instance @bookinarticle.
It offers more types than the older package biblatex-
bookinarticle which it superseeds.

%package -n texlive-biblatex-iso690-doc
Provides:       tex-biblatex-iso690-doc = %{tl_version}
License:        GPLv3
Summary:        doc files of biblatex-iso690
Version:        svn44066
AutoReqProv:    No

%description -n texlive-biblatex-iso690-doc
Documentation for biblatex-iso690

%package -n texlive-biblatex-iso690
Provides:       tex-biblatex-iso690 = %{tl_version}
License:        GPLv3
Summary:        BibLaTeX style for ISO 690 standard
Version:        svn44066
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

%description -n texlive-biblatex-iso690
The package provides a bibliography and citation style which
conforms to the latest revision of the international standard
ISO 690:2010. The implementation follows BibLaTeX conventions
and requires biblatex >= 3.4 and biber >= 2.5.

%package -n texlive-biblatex-morenames-doc
Provides:       tex-biblatex-morenames-doc = %{tl_version}
License:        LPPL
Summary:        doc files of biblatex-morenames
Version:        svn43049
AutoReqProv:    No

%description -n texlive-biblatex-morenames-doc
Documentation for biblatex-morenames

%package -n texlive-biblatex-morenames
Provides:       tex-biblatex-morenames = %{tl_version}
License:        LPPL
Summary:        New names for standard BibLaTeX entry type
Version:        svn43049
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(morenames.bbx) = %{tl_version}

%description -n texlive-biblatex-morenames
This package adds new fields of "name" type to the standard
entry types of BibLaTeX. For example: maineditor, for a
@collection, means the editor of @mvcollection, and not the
editor of the @collection. bookineditor, for a @bookinbook,
means the editor of the entry, and not, as the standard editor
field, the editor of the volume in which the entry is
contained.

%package -n texlive-bibletext-doc
Provides:       tex-bibletext-doc = %{tl_version}
License:        MIT
Summary:        doc files of bibletext
Version:        svn45196
AutoReqProv:    No

%description -n texlive-bibletext-doc
Documentation for bibletext

%package -n texlive-bibletext
Provides:       tex-bibletext = %{tl_version}
License:        MIT
Summary:        Insert Bible passages by their reference
Version:        svn45196
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(bibletext.sty) = %{tl_version}

%description -n texlive-bibletext
The package allows to insert Bible texts in a document by
specifying references.

%package -n texlive-bibtexperllibs-doc
Provides:       tex-bibtexperllibs-doc = %{tl_version}
License:        GPL+ or Artistic
Summary:        doc files of bibtexperllibs
Version:        svn47520
AutoReqProv:    No

%description -n texlive-bibtexperllibs-doc
Documentation for bibtexperllibs

%package -n texlive-bibtexperllibs
Provides:       tex-bibtexperllibs = %{tl_version}
License:        GPL+ or Artistic
Summary:        BibTeX Perl Libraries
Version:        svn47520
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       perl(LaTeX::ToUnicode), perl(BibTeX::Parser)

%description -n texlive-bibtexperllibs
This package provides BibTeX related Perl libraries by Gerhard
Gossen, repacked by Boris Veytsman, for TeX Live and other TDS-
compliant distributions. The libraries are written in pure
Perl, so should work out of the box on any architecture. They
have been packaged here mostly for Boris Veytsman's BibTeX
suite, but can be used in any other Perl script.

%package -n texlive-bitpattern-doc
Provides:       tex-bitpattern-doc = %{tl_version}
License:        LPPL
Summary:        doc files of bitpattern
Version:        svn39073

AutoReqProv:    No

%description -n texlive-bitpattern-doc
Documentation for bitpattern

%package -n texlive-bitpattern
Provides:       tex-bitpattern = %{tl_version}
License:        LPPL
Summary:        Typeset bit pattern diagrams
Version:        svn39073

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bitpattern.sty) = %{tl_version}

%description -n texlive-bitpattern
A package to typeset bit pattern diagrams such as those used to
describe hardware, data format or protocols.


%package -n texlive-bestpapers-doc
Provides:       tex-bestpapers-doc = %{tl_version}
License:        Public Domain
Summary:        doc files of bestpapers
Version:        svn38708

AutoReqProv:    No

%description -n texlive-bestpapers-doc
Documentation for bestpapers-uptex

%package -n texlive-bestpapers
Provides:       tex-bestpapers = %{tl_version}
License:        Public Domain
Summary:        A BibTeX package to produce lists of authors' best papers
Version:        svn38708

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

%description -n texlive-bestpapers
Many people preparing their resumes find the requirement
"please list five (or six, or ten) papers authored by you". The
same requirement is often stated for reports prepared by
professional teams. The creation of such lists may be a
cumbersome task. Even more difficult is it to support such
lists over the time, when new papers are added. The BibTeX
style bestpapers.bst is intended to facilitate this task. It is
based on the idea that it is easier to score than to sort: We
can assign a score to a paper and then let the computer select
the papers with highest scores. This work was commissioned by
the Consumer Financial Protection Bureau, United States
Treasury. This package is in the public domain.

%package -n texlive-biblatex-claves
Provides:       tex-biblatex-claves = %{tl_version}
License:        LPPL
Summary:        A tool to manage claves of old litterature with BibLaTeX
Version:        svn43723
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(claves.bbx) = %{tl_version}

%description -n texlive-biblatex-claves
When studying antic and medieval literature, we may find many
different texts published with the same title, or, in contrary,
the same text published with different titles. To avoid
confusion, scholars have published claves, which are books
listing ancient texts, identifying them by an identifier -- a
number or a string of text. For example, for early
Christianity, we have the Bibliotheca Hagiographica Graeca, the
Clavis Apocryphorum Novi Testamenti and other claves. It could
be useful to print the identifier of a texts in one specific
clavis, or in many claves. The package allows us to create new
field for different claves, and to present all these fields in
a consistent way.

%package -n texlive-biblatex-claves-doc
Provides:       tex-biblatex-claves-doc = %{tl_version}
License:        LPPL
Summary:        doc files of biblatex-claves
Version:        svn43723
AutoReqProv:    No

%description -n texlive-biblatex-claves-doc
Documentation for biblatex-claves.

%package -n texlive-biblatex-ijsra
Provides:       tex-biblatex-ijsra = %{tl_version}
License:        LPPL
Summary:        BibLaTeX style for the International Journal of Student Research in Archaeology
Version:        svn41634
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(ijsra.bbx) = %{tl_version}, tex(ijsra.cbx) = %{tl_version}

%description -n texlive-biblatex-ijsra
BibLaTeX style used for the journal International Journal of
Student Research in Archaeology.

%package -n texlive-biblatex-ijsra-doc
Provides:       tex-biblatex-ijsra-doc = %{tl_version}
License:        LPPL
Summary:        doc files of biblatex-ijsra
Version:        svn41634
AutoReqProv:    No

%description -n texlive-biblatex-ijsra-doc
Documentation for biblatex-ijsra.

%package -n texlive-biblatex-lni
Provides:       tex-biblatex-lni = %{tl_version}
License:        LPPL
Summary:        LNI style for BibLaTeX
Version:        svn43032
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(LNI.bbx) = %{tl_version}, tex(LNI.cbx) = %{tl_version}

%description -n texlive-biblatex-lni
BibLaTeX style for the Lecture Notes in Informatics, which is
published by the Gesellschaft fur Informatik (GI e.V.).

%package -n texlive-biblatex-lni-doc
Provides:       tex-biblatex-lni-doc = %{tl_version}
License:        LPPL
Summary:        doc files of biblatex-lni
Version:        svn43032
AutoReqProv:    No

%description -n texlive-biblatex-lni-doc
Documentation for biblatex-lni.

%package -n texlive-biblatex-nottsclassic
Provides:       tex-biblatex-nottsclassic = %{tl_version}
License:        LPPL
Summary:        Citation style covering the citation and bibliography rules of the University of Nottingham
Version:        svn41596
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(nottsclassic.bbx) = %{tl_version}, tex(nottsclassic.cbx) = %{tl_version}

%description -n texlive-biblatex-nottsclassic
This citation-style covers the citation and bibliography rules
of the University of Nottingham.

%package -n texlive-biblatex-nottsclassic-doc
Provides:       tex-biblatex-nottsclassic-doc = %{tl_version}
License:        LPPL
Summary:        doc files of biblatex-nottsclassic
Version:        svn41596
AutoReqProv:    No

%description -n texlive-biblatex-nottsclassic-doc
Documentation for biblatex-nottsclassic.

%package -n texlive-beamerswitch
Summary:        Convenient mode selection in Beamer documents
Version:        svn46042
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(beamerswitch.cls) = %{tl_version}

%description -n texlive-beamerswitch
This class is a wrapper around the beamer class to make it
easier to use the same document to generate the different forms
of the presentation: the slides themselves, an abbreviated
slide set for transparencies or online reference, an n-up
handout version (various layouts are provided), and a
transcript or set of notes using the article class. The class
provides a variety of handout layouts, and allows the mode to
be chosen from the command line (without changing the document
itself).

%package -n texlive-beilstein
Summary:        Support for submissions to the "Beilstein Journal of Nanotechnology"
Version:        svn46503
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(beilstein.cls) = %{tl_version}

%description -n texlive-beilstein
The package provides a LaTeX class file and a BibTeX style file
in accordance with the requirements of submissions to the
``Beilstein Journal of Nanotechnology''. Although the files can
be used for any kind of document, they have only been designed
and tested to be suitable for submissions to the Beilstein
Journal of Nanotechnology.

%package -n texlive-beuron
Summary:        The script of the Beuronese art school
Version:        svn46374
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(beuron.map) = %{tl_version}, tex(Beuron-Regular.otf) = %{tl_version}
Provides:       tex(BeuronCondensed-Regular.otf) = %{tl_version}
Provides:       tex(BeuronExtended-Regular.otf) = %{tl_version}
Provides:       tex(beuron.tfm) = %{tl_version}, tex(beuronc.tfm) = %{tl_version}
Provides:       tex(beuronx.tfm) = %{tl_version}, tex(beuron.pfb) = %{tl_version}
Provides:       tex(beuronc.pfb) = %{tl_version}, tex(beuronx.pfb) = %{tl_version}
Provides:       tex(beuron.sty) = %{tl_version}, tex(t1beuron.fd) = %{tl_version}

%description -n texlive-beuron
This package provides the script used in the works of the
Beuron art school for use with TeX and LaTeX. It is a
monumental script consisting of capital letters only. The fonts
are provided as Metafont sources, in the Type1 and in the
OpenType format. The package includes suitable font selection
commands for use with LaTeX.

%package -n texlive-biblatex-cheatsheet-doc
Summary:        doc files of biblatex-cheatsheet
Version:        svn44685
License:        LPPL

%description -n texlive-biblatex-cheatsheet-doc
A BibLaTeX/Biber ‘cheat sheet’ which I wrote because I wanted
one to distribute to students, but couldn’t find an existing one.

%package -n texlive-biblatex-enc
Summary:        BibLaTeX style for the Ecole nationale des chartes (Paris)
Version:        svn44627
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(enc.bbx) = %{tl_version}, tex(enc.cbx) = %{tl_version}

%description -n texlive-biblatex-enc
This package provides a citation and bibliography style for use
with BibLaTeX. It conforms to the bibliographic standards used
at the Ecole nationale des chartes (Paris), and may be suitable
for a more general use in historical and philological works.
The package was initially derived from historische-zeitschrift,
with the necessary modifications.

%package -n texlive-biblatex-gb7714-2015
Summary:        A BibLaTeX implementation of the GBT7714-2015 bibliography style for Chinese users
Version:        svn48123
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(gb7714-2015.bbx) = %{tl_version}, tex(gb7714-2015.cbx) = %{tl_version}
Provides:       tex(gb7714-2015ay.bbx) = %{tl_version}, tex(gb7714-2015ay.cbx) = %{tl_version}

%description -n texlive-biblatex-gb7714-2015
This package provides an implementation of the GBT7714-2015
bibliography style. This implementation follows GBT7714-2015
standard and can be used by simply loading BibLaTeX with the
appropriate option. A demonstration database is provided to
show how to format input for the style.

%package -n texlive-biblatex-oxref
Summary:        BibLaTeX styles inspired by the Oxford Guide to Style
Version:        svn46852
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(oxnotes.bbx) = %{tl_version}, tex(oxnotes.cbx) = %{tl_version}
Provides:       tex(oxnotes.dbx) = %{tl_version}, tex(oxref.bbx) = %{tl_version}
Provides:       tex(oxyear.bbx) = %{tl_version}, tex(oxyear.cbx) = %{tl_version}
Provides:       tex(oxyear.dbx) = %{tl_version}

%description -n texlive-biblatex-oxref
This bundle provides two BibLaTeX styles that implement (many
of) the stipulations and examples provided by the 2014 New
Hart's Rules and the 2002 Oxford Guide to Style: oxnotes is a
style similar to the standard verbose, intended for use with
footnotes; oxyear is a style similar to the standard
authoryear, intended for use with parenthetical in-text
citations. It provides support for a wide variety of content
types, including manuscripts, audiovisual resources, social
media and legal references.

%package -n texlive-biblatex-sbl
Summary:        Society of Biblical Literature (SBL) style files for BibLaTeX
Version:        svn47825
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(biblatex-sbl.def) = %{tl_version}, tex(sbl-paper.sty) = %{tl_version}
Provides:       tex(sbl.bbx) = %{tl_version}, tex(sbl.cbx) = %{tl_version}
Provides:       tex(sbl.dbx) = %{tl_version}

%description -n texlive-biblatex-sbl
The package provides BibLaTeX support for citations in the
format specified by the second edition of the Society of
Biblical Literature (SBL) Handbook of Style. All example notes
and bibliography entries from the handbook are supported and
shown in an example file. A style file for writing SBL student
papers is also included.

%package -n texlive-biblatex-shortfields
Summary:        Use short forms of fields with BibLaTeX
Version:        svn45858
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(biblatex-shortfields.sty) = %{tl_version}

%description -n texlive-biblatex-shortfields
The BibLaTeX package provides shortseries and shortjournal
field, but the default styles don't use them. It also provides
a mechanism to print the equivalence between short forms of
fields and long fields (\printbiblist), but this mechanism does
not allow to mix between different type of short fields, for
example, between short forms of journal title and short forms
of series titles. This package provides a solution to these two
problems: If a shortjournal field is defined, it prints it
instead of the \journal field. If a shortseries field is
defined, it prints it instead of the \series field. It provides
a \printbibshortfields command to print a list of the sort
forms of the fields. This list also includes the claves defined
with the biblatex-claves package version 1.2 or later.

%package -n texlive-binarytree
Summary:        Drawing binary trees using TikZ
Version:        svn41777
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(binarytree.sty) = %{tl_version}

%description -n texlive-binarytree
This package provides an easy but flexible way to draw binary
trees using TikZ. A path specification and the setting of
various options determine the style for each edge of the tree.
There is support for the external library of TikZ which does
not affect externalization of the rest of the TikZ figures in
the document. There is an option to use automatic file naming:
useful if the trees are often moved around.

%package -n texlive-biochemistry-colors
Summary:        Colors used to display amino acids, nucleotides, sugars or atoms in biochemistry
Version:        svn43960
License:        LPPL and GPL+
Requires:       texlive-base texlive-kpathsea
Provides:       tex(Biochemistry-colors.sty) = %{tl_version}

%description -n texlive-biochemistry-colors
Biochemistry-colors.sty defines the standard colors of
biochemistry for use with the color package and the xcolor
package. xcolor is loaded by Biochemistry-colors.sty. Colors
include: Shapely-colors for amino acids and nucleotides. CPK-
Colors (Corey, Pauling and Koltun) of elements. Jmol-colors of
elements, important isotopes and structures. Glycopedia colors
for sugars.

%package -n texlive-biolett-bst
Summary:        A BibTeX style for the journal "Biology Letters"
Version:        svn42217
License:        LPPL
Requires:       texlive-base texlive-kpathsea

%description -n texlive-biolett-bst
This package provides a BibTeX style (.bst) file for the
journal "Biology Letters" published by the Royal Society. This
style was produced independently and hence has no formal
approval from the Royal Society.

%package -n texlive-beamertheme-cuerna
Summary:        A beamer theme with 4 colour palettes
Version:        svn42161
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(beamercolorthemeCuerna.sty) = %{tl_version}
Provides:       tex(beamercolorthemebluesimplex.sty) = %{tl_version}
Provides:       tex(beamercolorthemebrick.sty) = %{tl_version}
Provides:       tex(beamercolorthemelettuce.sty) = %{tl_version}
Provides:       tex(beamerinnerthemeCuerna.sty) = %{tl_version}
Provides:       tex(beamerouterthemeCuerna.sty) = %{tl_version}
Provides:       tex(beamerthemeCuerna.sty) = %{tl_version}

%description -n texlive-beamertheme-cuerna
The package contains a theme for Beamer which is referenced as
"Cuerna" inside beamer and has four basic colour themes. The
title page shows rectangles that represent the Fibonacci
sequence, and spiral is drawn on top of the rectangles. Besides
that the rest of the graphic elements in the slides are scarce
to keep it clean.

%package -n texlive-beamertheme-focus
Summary:        A minimalist presentation theme for LaTeX Beamer
Version:        svn48382
License:        GPLv3
Requires:       texlive-base texlive-kpathsea
Provides:       tex(beamercolorthemefocus.sty) = %{tl_version}
Provides:       tex(beamerfontthemefocus.sty) = %{tl_version}
Provides:       tex(beamerinnerthemefocus.sty) = %{tl_version}
Provides:       tex(beamerouterthemefocus.sty) = %{tl_version}
Provides:       tex(beamerthemefocus.sty) = %{tl_version}

%description -n texlive-beamertheme-focus
A presentation theme for LaTeX Beamer that aims at a clean and
minimalist design, so to minimize distractions and put the
focus directly on the content.

%package -n texlive-beamertheme-saintpetersburg
Summary:        A beamer theme that incorporates colours and fonts of Saint Petersburg State University
Version:        svn45877
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(beamercolorthemeSaintPetersburg.sty) = %{tl_version}
Provides:       tex(beamerfontthemeSaintPetersburg.sty) = %{tl_version}
Provides:       tex(beamerthemeSaintPetersburg.sty) = %{tl_version}

%description -n texlive-beamertheme-saintpetersburg
This minimalistic beamer theme incorporates Saint Petersburg
State University colours and fonts. It is suitable for both
presentations and posters.

%package -n texlive-bezierplot
Summary:        Approximate smooth function graphs with cubic bezier splines for use with TikZ or MetaPost
Version:        svn48259
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(bezierplot.sty) = %{tl_version}

%description -n texlive-bezierplot
This package consists of a Lua program as well as a (Lua)LaTeX
.sty file. Given a smooth function, bezierplot returns a smooth
bezier path written in TikZ notation (which also matches
MetaPost) that approximates the graph of the function. For
polynomial functions of degree [?] 3 and their inverses the
approximation is exact (up to numeric precision). bezierplot
also finds special points such as extreme points and inflection
points and reduces the number of used points.

%package -n texlive-biblatex-archaeology
Summary:        A collection of BibLaTeX styles for German prehistory
Version:        svn47989
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(UKenglish-aefkw.lbx) = %{tl_version}
Provides:       tex(UKenglish-archa.lbx) = %{tl_version}
Provides:       tex(UKenglish-archaeology.lbx) = %{tl_version}
Provides:       tex(UKenglish-dguf-alt.lbx) = %{tl_version}
Provides:       tex(UKenglish-dguf-apa.lbx) = %{tl_version}
Provides:       tex(UKenglish-eaz.lbx) = %{tl_version}, tex(UKenglish-foe.lbx) = %{tl_version}
Provides:       tex(UKenglish-jb-kreis-neuss.lbx) = %{tl_version}
Provides:       tex(UKenglish-karl.lbx) = %{tl_version}, tex(UKenglish-maja.lbx) = %{tl_version}
Provides:       tex(UKenglish-mpk.lbx) = %{tl_version}, tex(UKenglish-mpkoeaw.lbx) = %{tl_version}
Provides:       tex(UKenglish-offa.lbx) = %{tl_version}, tex(UKenglish-rgzm.lbx) = %{tl_version}
Provides:       tex(UKenglish-zaak.lbx) = %{tl_version}, tex(UKenglish-zaes.lbx) = %{tl_version}
Provides:       tex(USenglish-aefkw.lbx) = %{tl_version}
Provides:       tex(USenglish-archa.lbx) = %{tl_version}
Provides:       tex(USenglish-archaeology.lbx) = %{tl_version}
Provides:       tex(USenglish-dguf-alt.lbx) = %{tl_version}
Provides:       tex(USenglish-dguf-apa.lbx) = %{tl_version}
Provides:       tex(USenglish-eaz.lbx) = %{tl_version}, tex(USenglish-foe.lbx) = %{tl_version}
Provides:       tex(USenglish-jb-kreis-neuss.lbx) = %{tl_version}
Provides:       tex(USenglish-karl.lbx) = %{tl_version}, tex(USenglish-maja.lbx) = %{tl_version}
Provides:       tex(USenglish-mpk.lbx) = %{tl_version}, tex(USenglish-mpkoeaw.lbx) = %{tl_version}
Provides:       tex(USenglish-offa.lbx) = %{tl_version}, tex(USenglish-rgzm.lbx) = %{tl_version}
Provides:       tex(USenglish-zaak.lbx) = %{tl_version}, tex(USenglish-zaes.lbx) = %{tl_version}
Provides:       tex(aefkw.bbx) = %{tl_version}, tex(aefkw.cbx) = %{tl_version}
Provides:       tex(aefkw.dbx) = %{tl_version}, tex(afwl.bbx) = %{tl_version}
Provides:       tex(afwl.cbx) = %{tl_version}, tex(afwl.dbx) = %{tl_version}
Provides:       tex(american-aefkw.lbx) = %{tl_version}, tex(american-archa.lbx) = %{tl_version}
Provides:       tex(american-archaeology.lbx) = %{tl_version}
Provides:       tex(american-dguf-alt.lbx) = %{tl_version}
Provides:       tex(american-dguf-apa.lbx) = %{tl_version}
Provides:       tex(american-eaz.lbx) = %{tl_version}, tex(american-foe.lbx) = %{tl_version}
Provides:       tex(american-jb-kreis-neuss.lbx) = %{tl_version}
Provides:       tex(american-karl.lbx) = %{tl_version}, tex(american-maja.lbx) = %{tl_version}
Provides:       tex(american-mpk.lbx) = %{tl_version}, tex(american-mpkoeaw.lbx) = %{tl_version}
Provides:       tex(american-offa.lbx) = %{tl_version}, tex(american-rgzm.lbx) = %{tl_version}
Provides:       tex(american-zaak.lbx) = %{tl_version}, tex(american-zaes.lbx) = %{tl_version}
Provides:       tex(amit.bbx) = %{tl_version}, tex(amit.cbx) = %{tl_version}
Provides:       tex(amit.dbx) = %{tl_version}, tex(archa.bbx) = %{tl_version}
Provides:       tex(archa.cbx) = %{tl_version}, tex(archa.dbx) = %{tl_version}
Provides:       tex(australian-aefkw.lbx) = %{tl_version}
Provides:       tex(australian-archa.lbx) = %{tl_version}
Provides:       tex(australian-archaeology.lbx) = %{tl_version}
Provides:       tex(australian-dguf-alt.lbx) = %{tl_version}
Provides:       tex(australian-dguf-apa.lbx) = %{tl_version}
Provides:       tex(australian-eaz.lbx) = %{tl_version}, tex(australian-foe.lbx) = %{tl_version}
Provides:       tex(australian-jb-kreis-neuss.lbx) = %{tl_version}
Provides:       tex(australian-karl.lbx) = %{tl_version}
Provides:       tex(australian-maja.lbx) = %{tl_version}
Provides:       tex(australian-mpk.lbx) = %{tl_version}, tex(australian-mpkoeaw.lbx) = %{tl_version}
Provides:       tex(australian-offa.lbx) = %{tl_version}
Provides:       tex(australian-rgzm.lbx) = %{tl_version}
Provides:       tex(australian-zaak.lbx) = %{tl_version}
Provides:       tex(australian-zaes.lbx) = %{tl_version}
Provides:       tex(austrian-aefkw.lbx) = %{tl_version}, tex(austrian-archa.lbx) = %{tl_version}
Provides:       tex(austrian-archaeology.lbx) = %{tl_version}
Provides:       tex(austrian-dguf-alt.lbx) = %{tl_version}
Provides:       tex(austrian-dguf-apa.lbx) = %{tl_version}
Provides:       tex(austrian-eaz.lbx) = %{tl_version}, tex(austrian-foe.lbx) = %{tl_version}
Provides:       tex(austrian-jb-kreis-neuss.lbx) = %{tl_version}
Provides:       tex(austrian-karl.lbx) = %{tl_version}, tex(austrian-maja.lbx) = %{tl_version}
Provides:       tex(austrian-mpk.lbx) = %{tl_version}, tex(austrian-mpkoeaw.lbx) = %{tl_version}
Provides:       tex(austrian-offa.lbx) = %{tl_version}, tex(austrian-rgzm.lbx) = %{tl_version}
Provides:       tex(austrian-zaak.lbx) = %{tl_version}, tex(austrian-zaes.lbx) = %{tl_version}
Provides:       tex(authoryear-archaeology.bbx) = %{tl_version}
Provides:       tex(authoryear-archaeology.cbx) = %{tl_version}
Provides:       tex(authoryear-archaeology.dbx) = %{tl_version}
Provides:       tex(authoryear-comp-archaeology.bbx) = %{tl_version}
Provides:       tex(authoryear-comp-archaeology.cbx) = %{tl_version}
Provides:       tex(authoryear-comp-archaeology.dbx) = %{tl_version}
Provides:       tex(authoryear-ibid-archaeology.bbx) = %{tl_version}
Provides:       tex(authoryear-ibid-archaeology.cbx) = %{tl_version}
Provides:       tex(authoryear-ibid-archaeology.dbx) = %{tl_version}
Provides:       tex(authoryear-icomp-archaeology.bbx) = %{tl_version}
Provides:       tex(authoryear-icomp-archaeology.cbx) = %{tl_version}
Provides:       tex(authoryear-icomp-archaeology.dbx) = %{tl_version}
Provides:       tex(biblatex-archaeology.sty) = %{tl_version}
Provides:       tex(british-aefkw.lbx) = %{tl_version}, tex(british-archa.lbx) = %{tl_version}
Provides:       tex(british-archaeology.lbx) = %{tl_version}
Provides:       tex(british-dguf-alt.lbx) = %{tl_version}
Provides:       tex(british-dguf-apa.lbx) = %{tl_version}
Provides:       tex(british-eaz.lbx) = %{tl_version}, tex(british-foe.lbx) = %{tl_version}
Provides:       tex(british-jb-kreis-neuss.lbx) = %{tl_version}
Provides:       tex(british-karl.lbx) = %{tl_version}, tex(british-maja.lbx) = %{tl_version}
Provides:       tex(british-mpk.lbx) = %{tl_version}, tex(british-mpkoeaw.lbx) = %{tl_version}
Provides:       tex(british-offa.lbx) = %{tl_version}, tex(british-rgzm.lbx) = %{tl_version}
Provides:       tex(british-zaak.lbx) = %{tl_version}, tex(british-zaes.lbx) = %{tl_version}
Provides:       tex(canadian-aefkw.lbx) = %{tl_version}, tex(canadian-archa.lbx) = %{tl_version}
Provides:       tex(canadian-archaeology.lbx) = %{tl_version}
Provides:       tex(canadian-dguf-alt.lbx) = %{tl_version}
Provides:       tex(canadian-dguf-apa.lbx) = %{tl_version}
Provides:       tex(canadian-eaz.lbx) = %{tl_version}, tex(canadian-foe.lbx) = %{tl_version}
Provides:       tex(canadian-jb-kreis-neuss.lbx) = %{tl_version}
Provides:       tex(canadian-karl.lbx) = %{tl_version}, tex(canadian-maja.lbx) = %{tl_version}
Provides:       tex(canadian-mpk.lbx) = %{tl_version}, tex(canadian-mpkoeaw.lbx) = %{tl_version}
Provides:       tex(canadian-offa.lbx) = %{tl_version}, tex(canadian-rgzm.lbx) = %{tl_version}
Provides:       tex(canadian-zaak.lbx) = %{tl_version}, tex(canadian-zaes.lbx) = %{tl_version}
Provides:       tex(dguf-alt.bbx) = %{tl_version}, tex(dguf-alt.cbx) = %{tl_version}
Provides:       tex(dguf-alt.dbx) = %{tl_version}, tex(dguf-apa.bbx) = %{tl_version}
Provides:       tex(dguf-apa.cbx) = %{tl_version}, tex(dguf-apa.dbx) = %{tl_version}
Provides:       tex(dguf.bbx) = %{tl_version}, tex(dguf.cbx) = %{tl_version}
Provides:       tex(dguf.dbx) = %{tl_version}, tex(eaz-alt.bbx) = %{tl_version}
Provides:       tex(eaz-alt.cbx) = %{tl_version}, tex(eaz-alt.dbx) = %{tl_version}
Provides:       tex(eaz.bbx) = %{tl_version}, tex(eaz.cbx) = %{tl_version}
Provides:       tex(eaz.dbx) = %{tl_version}, tex(english-aefkw.lbx) = %{tl_version}
Provides:       tex(english-archa.lbx) = %{tl_version}, tex(english-archaeology.lbx) = %{tl_version}
Provides:       tex(english-dguf-alt.lbx) = %{tl_version}
Provides:       tex(english-dguf-apa.lbx) = %{tl_version}
Provides:       tex(english-eaz.lbx) = %{tl_version}, tex(english-foe.lbx) = %{tl_version}
Provides:       tex(english-jb-kreis-neuss.lbx) = %{tl_version}
Provides:       tex(english-karl.lbx) = %{tl_version}, tex(english-maja.lbx) = %{tl_version}
Provides:       tex(english-mpk.lbx) = %{tl_version}, tex(english-mpkoeaw.lbx) = %{tl_version}
Provides:       tex(english-offa.lbx) = %{tl_version}, tex(english-rgzm.lbx) = %{tl_version}
Provides:       tex(english-zaak.lbx) = %{tl_version}, tex(english-zaes.lbx) = %{tl_version}
Provides:       tex(foe.bbx) = %{tl_version}, tex(foe.cbx) = %{tl_version}
Provides:       tex(foe.dbx) = %{tl_version}, tex(german-aefkw.lbx) = %{tl_version}
Provides:       tex(german-archa.lbx) = %{tl_version}, tex(german-archaeology.lbx) = %{tl_version}
Provides:       tex(german-dguf-alt.lbx) = %{tl_version}
Provides:       tex(german-dguf-apa.lbx) = %{tl_version}
Provides:       tex(german-eaz.lbx) = %{tl_version}, tex(german-foe.lbx) = %{tl_version}
Provides:       tex(german-jb-kreis-neuss.lbx) = %{tl_version}
Provides:       tex(german-karl.lbx) = %{tl_version}, tex(german-maja.lbx) = %{tl_version}
Provides:       tex(german-mpk.lbx) = %{tl_version}, tex(german-mpkoeaw.lbx) = %{tl_version}
Provides:       tex(german-offa.lbx) = %{tl_version}, tex(german-rgzm.lbx) = %{tl_version}
Provides:       tex(german-zaak.lbx) = %{tl_version}, tex(german-zaes.lbx) = %{tl_version}
Provides:       tex(jb-halle.bbx) = %{tl_version}, tex(jb-halle.cbx) = %{tl_version}
Provides:       tex(jb-halle.dbx) = %{tl_version}, tex(jb-kreis-neuss.bbx) = %{tl_version}
Provides:       tex(jb-kreis-neuss.cbx) = %{tl_version}, tex(jb-kreis-neuss.dbx) = %{tl_version}
Provides:       tex(karl.bbx) = %{tl_version}, tex(karl.cbx) = %{tl_version}
Provides:       tex(karl.dbx) = %{tl_version}, tex(maja.bbx) = %{tl_version}
Provides:       tex(maja.cbx) = %{tl_version}, tex(maja.dbx) = %{tl_version}
Provides:       tex(mpk.bbx) = %{tl_version}, tex(mpk.cbx) = %{tl_version}
Provides:       tex(mpk.dbx) = %{tl_version}, tex(mpkoeaw.bbx) = %{tl_version}
Provides:       tex(mpkoeaw.cbx) = %{tl_version}, tex(mpkoeaw.dbx) = %{tl_version}
Provides:       tex(naustrian-aefkw.lbx) = %{tl_version}
Provides:       tex(naustrian-archa.lbx) = %{tl_version}
Provides:       tex(naustrian-archaeology.lbx) = %{tl_version}
Provides:       tex(naustrian-dguf-alt.lbx) = %{tl_version}
Provides:       tex(naustrian-dguf-apa.lbx) = %{tl_version}
Provides:       tex(naustrian-eaz.lbx) = %{tl_version}, tex(naustrian-foe.lbx) = %{tl_version}
Provides:       tex(naustrian-jb-kreis-neuss.lbx) = %{tl_version}
Provides:       tex(naustrian-karl.lbx) = %{tl_version}, tex(naustrian-maja.lbx) = %{tl_version}
Provides:       tex(naustrian-mpk.lbx) = %{tl_version}, tex(naustrian-mpkoeaw.lbx) = %{tl_version}
Provides:       tex(naustrian-offa.lbx) = %{tl_version}, tex(naustrian-rgzm.lbx) = %{tl_version}
Provides:       tex(naustrian-zaak.lbx) = %{tl_version}, tex(naustrian-zaes.lbx) = %{tl_version}
Provides:       tex(newzealand-aefkw.lbx) = %{tl_version}
Provides:       tex(newzealand-archa.lbx) = %{tl_version}
Provides:       tex(newzealand-archaeology.lbx) = %{tl_version}
Provides:       tex(newzealand-dguf-alt.lbx) = %{tl_version}
Provides:       tex(newzealand-dguf-apa.lbx) = %{tl_version}
Provides:       tex(newzealand-eaz.lbx) = %{tl_version}, tex(newzealand-foe.lbx) = %{tl_version}
Provides:       tex(newzealand-jb-kreis-neuss.lbx) = %{tl_version}
Provides:       tex(newzealand-karl.lbx) = %{tl_version}
Provides:       tex(newzealand-maja.lbx) = %{tl_version}
Provides:       tex(newzealand-mpk.lbx) = %{tl_version}, tex(newzealand-mpkoeaw.lbx) = %{tl_version}
Provides:       tex(newzealand-offa.lbx) = %{tl_version}
Provides:       tex(newzealand-rgzm.lbx) = %{tl_version}
Provides:       tex(newzealand-zaak.lbx) = %{tl_version}
Provides:       tex(newzealand-zaes.lbx) = %{tl_version}
Provides:       tex(ngerman-aefkw.lbx) = %{tl_version}, tex(ngerman-archa.lbx) = %{tl_version}
Provides:       tex(ngerman-archaeology.lbx) = %{tl_version}
Provides:       tex(ngerman-dguf-alt.lbx) = %{tl_version}
Provides:       tex(ngerman-dguf-apa.lbx) = %{tl_version}
Provides:       tex(ngerman-eaz.lbx) = %{tl_version}, tex(ngerman-foe.lbx) = %{tl_version}
Provides:       tex(ngerman-jb-kreis-neuss.lbx) = %{tl_version}
Provides:       tex(ngerman-karl.lbx) = %{tl_version}, tex(ngerman-maja.lbx) = %{tl_version}
Provides:       tex(ngerman-mpk.lbx) = %{tl_version}, tex(ngerman-mpkoeaw.lbx) = %{tl_version}
Provides:       tex(ngerman-offa.lbx) = %{tl_version}, tex(ngerman-rgzm.lbx) = %{tl_version}
Provides:       tex(ngerman-zaak.lbx) = %{tl_version}, tex(ngerman-zaes.lbx) = %{tl_version}
Provides:       tex(nnu.bbx) = %{tl_version}, tex(nnu.cbx) = %{tl_version}
Provides:       tex(nnu.dbx) = %{tl_version}, tex(nswissgerman-aefkw.lbx) = %{tl_version}
Provides:       tex(nswissgerman-archa.lbx) = %{tl_version}
Provides:       tex(nswissgerman-archaeology.lbx) = %{tl_version}
Provides:       tex(nswissgerman-dguf-alt.lbx) = %{tl_version}
Provides:       tex(nswissgerman-dguf-apa.lbx) = %{tl_version}
Provides:       tex(nswissgerman-eaz.lbx) = %{tl_version}
Provides:       tex(nswissgerman-foe.lbx) = %{tl_version}
Provides:       tex(nswissgerman-jb-kreis-neuss.lbx) = %{tl_version}
Provides:       tex(nswissgerman-karl.lbx) = %{tl_version}
Provides:       tex(nswissgerman-maja.lbx) = %{tl_version}
Provides:       tex(nswissgerman-mpk.lbx) = %{tl_version}
Provides:       tex(nswissgerman-mpkoeaw.lbx) = %{tl_version}
Provides:       tex(nswissgerman-offa.lbx) = %{tl_version}
Provides:       tex(nswissgerman-rgzm.lbx) = %{tl_version}
Provides:       tex(nswissgerman-zaak.lbx) = %{tl_version}
Provides:       tex(nswissgerman-zaes.lbx) = %{tl_version}
Provides:       tex(numeric-comp-archaeology.bbx) = %{tl_version}
Provides:       tex(numeric-comp-archaeology.cbx) = %{tl_version}
Provides:       tex(numeric-comp-archaeology.dbx) = %{tl_version}
Provides:       tex(offa.bbx) = %{tl_version}, tex(offa.cbx) = %{tl_version}
Provides:       tex(offa.dbx) = %{tl_version}, tex(rgk-inline.bbx) = %{tl_version}
Provides:       tex(rgk-inline.cbx) = %{tl_version}, tex(rgk-inline.dbx) = %{tl_version}
Provides:       tex(rgk-numeric.bbx) = %{tl_version}, tex(rgk-numeric.cbx) = %{tl_version}
Provides:       tex(rgk-numeric.dbx) = %{tl_version}, tex(rgk-verbose.bbx) = %{tl_version}
Provides:       tex(rgk-verbose.cbx) = %{tl_version}, tex(rgk-verbose.dbx) = %{tl_version}
Provides:       tex(rgzm-inline.bbx) = %{tl_version}, tex(rgzm-inline.cbx) = %{tl_version}
Provides:       tex(rgzm-inline.dbx) = %{tl_version}, tex(rgzm-numeric.bbx) = %{tl_version}
Provides:       tex(rgzm-numeric.cbx) = %{tl_version}, tex(rgzm-numeric.dbx) = %{tl_version}
Provides:       tex(rgzm-verbose.bbx) = %{tl_version}, tex(rgzm-verbose.cbx) = %{tl_version}
Provides:       tex(rgzm-verbose.dbx) = %{tl_version}, tex(swissgerman-aefkw.lbx) = %{tl_version}
Provides:       tex(swissgerman-archa.lbx) = %{tl_version}
Provides:       tex(swissgerman-archaeology.lbx) = %{tl_version}
Provides:       tex(swissgerman-dguf-alt.lbx) = %{tl_version}
Provides:       tex(swissgerman-dguf-apa.lbx) = %{tl_version}
Provides:       tex(swissgerman-eaz.lbx) = %{tl_version}
Provides:       tex(swissgerman-foe.lbx) = %{tl_version}
Provides:       tex(swissgerman-jb-kreis-neuss.lbx) = %{tl_version}
Provides:       tex(swissgerman-karl.lbx) = %{tl_version}
Provides:       tex(swissgerman-maja.lbx) = %{tl_version}
Provides:       tex(swissgerman-mpk.lbx) = %{tl_version}
Provides:       tex(swissgerman-mpkoeaw.lbx) = %{tl_version}
Provides:       tex(swissgerman-offa.lbx) = %{tl_version}
Provides:       tex(swissgerman-rgzm.lbx) = %{tl_version}
Provides:       tex(swissgerman-zaak.lbx) = %{tl_version}
Provides:       tex(swissgerman-zaes.lbx) = %{tl_version}
Provides:       tex(ufg-muenster-inline.bbx) = %{tl_version}
Provides:       tex(ufg-muenster-inline.cbx) = %{tl_version}
Provides:       tex(ufg-muenster-inline.dbx) = %{tl_version}
Provides:       tex(ufg-muenster-numeric.bbx) = %{tl_version}
Provides:       tex(ufg-muenster-numeric.cbx) = %{tl_version}
Provides:       tex(ufg-muenster-numeric.dbx) = %{tl_version}
Provides:       tex(ufg-muenster-verbose.bbx) = %{tl_version}
Provides:       tex(ufg-muenster-verbose.cbx) = %{tl_version}
Provides:       tex(ufg-muenster-verbose.dbx) = %{tl_version}
Provides:       tex(verbose-archaeology.bbx) = %{tl_version}
Provides:       tex(verbose-archaeology.cbx) = %{tl_version}
Provides:       tex(verbose-archaeology.dbx) = %{tl_version}
Provides:       tex(verbose-ibid-archaeology.bbx) = %{tl_version}
Provides:       tex(verbose-ibid-archaeology.cbx) = %{tl_version}
Provides:       tex(verbose-ibid-archaeology.dbx) = %{tl_version}
Provides:       tex(verbose-trad2note-archaeology.bbx) = %{tl_version}
Provides:       tex(verbose-trad2note-archaeology.cbx) = %{tl_version}
Provides:       tex(verbose-trad2note-archaeology.dbx) = %{tl_version}
Provides:       tex(volkskunde.bbx) = %{tl_version}, tex(volkskunde.cbx) = %{tl_version}
Provides:       tex(volkskunde.dbx) = %{tl_version}, tex(zaak.bbx) = %{tl_version}
Provides:       tex(zaak.cbx) = %{tl_version}, tex(zaak.dbx) = %{tl_version}
Provides:       tex(zaes.bbx) = %{tl_version}, tex(zaes.cbx) = %{tl_version}
Provides:       tex(zaes.dbx) = %{tl_version}

%description -n texlive-biblatex-archaeology
This package provides additional BibLaTeX styles for German
humanities. Its core purpose is to enable the referencing rules
of the Romisch-Germanische Komission, the department of
prehistory of the Deutsches Archaologisches Institut (German
Archaeological Institute), since these are referenced by most
guidelines in German prehistory and medieval archaeology and
serve as a kind of template. It contains verbose and
author-date styles as well.

%package -n texlive-biblatex-arthistory-bonn
Summary:        BibLaTeX citation style covers the citation and bibliography guidelines for art historians
Version:        svn46637
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(arthistory-bonn-english.lbx) = %{tl_version}
Provides:       tex(arthistory-bonn-german.lbx) = %{tl_version}
Provides:       tex(arthistory-bonn.bbx) = %{tl_version}
Provides:       tex(arthistory-bonn.cbx) = %{tl_version}
Provides:       tex(arthistory-bonn.dbx) = %{tl_version}

%description -n texlive-biblatex-arthistory-bonn
This citation style covers the citation and bibliography
guidelines of the Kunsthistorisches Institut der Universitat
Bonn for undergraduates. It introduces bibliography entry types
for catalogs and features a tabular bibliography, among other
things. Various options are available to change and adjust the
outcome according to one's own preferences. The style is
compatible with English and German.

%package -n texlive-biblatex-socialscienceshuberlin
Summary:        BibLaTeX-style for the social sciences at HU Berlin
Version:        svn47839
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(german-socialscienceshuberlin.lbx) = %{tl_version}
Provides:       tex(socialscienceshuberlin.bbx) = %{tl_version}
Provides:       tex(socialscienceshuberlin.cbx) = %{tl_version}

%description -n texlive-biblatex-socialscienceshuberlin
This is a BibLaTeX style for the social sciences at the
Humboldt-Universitat zu Berlin.

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD


install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names="arkandis/berenisadf"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}/%{_infodir}/
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*


%files -n texlive-bbding
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/bbding/
%{_texdir}/texmf-dist/fonts/tfm/public/bbding/
%{_texdir}/texmf-dist/tex/latex/bbding/

%files -n texlive-bbding-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/bbding/

%files -n texlive-bbm-macros
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/bbm-macros/

%files -n texlive-bbm-macros-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/bbm-macros/

%files -n texlive-bbm
%{_texdir}/texmf-dist/fonts/source/public/bbm/
%{_texdir}/texmf-dist/fonts/tfm/public/bbm/

%files -n texlive-bbm-doc
%{_texdir}/texmf-dist/doc/fonts/bbm/

%files -n texlive-bbold
%license bsd.txt
%{_texdir}/texmf-dist/fonts/source/public/bbold/
%{_texdir}/texmf-dist/fonts/tfm/public/bbold/
%{_texdir}/texmf-dist/tex/latex/bbold/

%files -n texlive-bbold-doc
%license bsd.txt
%{_texdir}/texmf-dist/doc/latex/bbold/

%files -n texlive-bbold-type1
%{_texdir}/texmf-dist/fonts/afm/public/bbold-type1/
%{_texdir}/texmf-dist/fonts/map/dvips/bbold-type1/
%{_texdir}/texmf-dist/fonts/type1/public/bbold-type1/

%files -n texlive-bbold-type1-doc
%{_texdir}/texmf-dist/doc/fonts/bbold-type1/

%files -n texlive-bchart
%{_texdir}/texmf-dist/tex/latex/bchart/

%files -n texlive-bchart-doc
%{_texdir}/texmf-dist/doc/latex/bchart/

%files -n texlive-bclogo
%license lppl1.txt
%{_texdir}/texmf-dist/metapost/bclogo/
%{_texdir}/texmf-dist/tex/latex/bclogo/

%files -n texlive-bclogo-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/bclogo/

%files -n texlive-beamer2thesis
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/beamer2thesis/

%files -n texlive-beamer2thesis-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/beamer2thesis/

%files -n texlive-beameraudience
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/beameraudience/

%files -n texlive-beameraudience-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/beameraudience/

%files -n texlive-beamerdarkthemes
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/beamerdarkthemes/

%files -n texlive-beamerdarkthemes-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/beamerdarkthemes/

%files -n texlive-beamer-FUBerlin-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/beamer-FUBerlin/

%files -n texlive-beamerposter
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/beamerposter/

%files -n texlive-beamerposter-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/beamerposter/

%files -n texlive-beamersubframe
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/beamersubframe/

%files -n texlive-beamersubframe-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/beamersubframe/

%files -n texlive-beamerthemejltree
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/beamerthemejltree/

%files -n texlive-beamerthemenirma
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/beamerthemenirma/

%files -n texlive-beamerthemenirma-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/beamerthemenirma/

%files -n texlive-beamertheme-phnompenh
%{_texdir}/texmf-dist/tex/latex/beamertheme-phnompenh/

%files -n texlive-beamertheme-phnompenh-doc
%{_texdir}/texmf-dist/doc/latex/beamertheme-phnompenh/

%files -n texlive-beamertheme-upenn-bc
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/beamertheme-upenn-bc/

%files -n texlive-beamertheme-upenn-bc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/beamertheme-upenn-bc/

%files -n texlive-beamer
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/beamer/

%files -n texlive-beamer-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/beamer/


%files -n texlive-beamer-tut-pt-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/beamer-tut-pt/

%files -n texlive-beebe
%{_texdir}/texmf-dist/bibtex/bib/beebe/
%{_texdir}/texmf-dist/bibtex/bst/beebe/
%{_texdir}/texmf-dist/tex/generic/beebe/

%files -n texlive-begingreek
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/begingreek/

%files -n texlive-begingreek-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/begingreek/

%files -n texlive-begriff
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/begriff/

%files -n texlive-begriff-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/begriff/

%files -n texlive-belleek
%license pd.txt
%{_texdir}/texmf-dist/fonts/map/dvips/belleek/
%{_texdir}/texmf-dist/fonts/truetype/public/belleek/
%{_texdir}/texmf-dist/fonts/type1/public/belleek/

%files -n texlive-belleek-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/fonts/belleek/

%files -n texlive-bengali
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/bengali/
%{_texdir}/texmf-dist/fonts/tfm/public/bengali/
%{_texdir}/texmf-dist/tex/latex/bengali/

%files -n texlive-bengali-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/bengali/

%files -n texlive-bera
%{_texdir}/texmf-dist/fonts/afm/public/bera/
%{_texdir}/texmf-dist/fonts/map/dvips/bera/
%{_texdir}/texmf-dist/fonts/tfm/public/bera/
%{_texdir}/texmf-dist/fonts/type1/public/bera/
%{_texdir}/texmf-dist/fonts/vf/public/bera/
%{_texdir}/texmf-dist/tex/latex/bera/

%files -n texlive-bera-doc
%{_texdir}/texmf-dist/doc/fonts/bera/

%files -n texlive-berenisadf
%{_datadir}/fonts/berenisadf
%{_texdir}/texmf-dist/fonts/afm/arkandis/berenisadf/
%{_texdir}/texmf-dist/fonts/enc/dvips/berenisadf/
%{_texdir}/texmf-dist/fonts/map/dvips/berenisadf/
%{_texdir}/texmf-dist/fonts/opentype/arkandis/berenisadf/
%{_texdir}/texmf-dist/fonts/tfm/arkandis/berenisadf/
%{_texdir}/texmf-dist/fonts/type1/arkandis/berenisadf/
%{_texdir}/texmf-dist/tex/latex/berenisadf/

%files -n texlive-berenisadf-doc
%{_texdir}/texmf-dist/doc/fonts/berenisadf/

%files -n texlive-besjournals
%{_texdir}/texmf-dist/bibtex/bst/besjournals/

%files -n texlive-besjournals-doc
%{_texdir}/texmf-dist/doc/bibtex/besjournals/

%files -n texlive-betababel
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/betababel/

%files -n texlive-betababel-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/betababel/

%files -n texlive-beton
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/beton/

%files -n texlive-beton-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/beton/

%files -n texlive-bewerbung
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/bewerbung/

%files -n texlive-bewerbung-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/bewerbung/

%files -n texlive-bez123
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/bez123/

%files -n texlive-bez123-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/bez123/

%files -n texlive-bezos
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/bezos/

%files -n texlive-bezos-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/bezos/

%files -n texlive-bgreek
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/tfm/public/bgreek/
%{_texdir}/texmf-dist/fonts/vf/public/bgreek/
%{_texdir}/texmf-dist/tex/latex/bgreek/

%files -n texlive-bgreek-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/bgreek/

%files -n texlive-bgteubner
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/bgteubner/
%{_texdir}/texmf-dist/makeindex/bgteubner/
%{_texdir}/texmf-dist/tex/latex/bgteubner/

%files -n texlive-bgteubner-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/bgteubner/

%files -n texlive-bguq
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/map/dvips/bguq/
%{_texdir}/texmf-dist/fonts/source/public/bguq/
%{_texdir}/texmf-dist/fonts/tfm/public/bguq/
%{_texdir}/texmf-dist/fonts/type1/public/bguq/
%{_texdir}/texmf-dist/tex/latex/bguq/

%files -n texlive-bguq-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/bguq/

%files -n texlive-bhcexam
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/bhcexam/

%files -n texlive-bhcexam-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/bhcexam/

%files -n texlive-bibarts
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/bibarts/

%files -n texlive-bibarts-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/bibarts/

%files -n texlive-bib-fr
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/bib-fr/

%files -n texlive-bib-fr-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/bibtex/bib-fr/

%files -n texlive-bibhtml
%license gpl.txt
%{_texdir}/texmf-dist/bibtex/bst/bibhtml/

%files -n texlive-bibhtml-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/bibtex/bibhtml/

%files -n texlive-biblatex-anonymous
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-anonymous/

%files -n texlive-biblatex-anonymous-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-anonymous/

%files -n texlive-biblatex-apa
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-apa/

%files -n texlive-biblatex-apa-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-apa/

%files -n texlive-biblatex-bookinarticle
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-bookinarticle/

%files -n texlive-biblatex-bookinarticle-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-bookinarticle/

%files -n texlive-biblatex-bwl
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-bwl/

%files -n texlive-biblatex-bwl-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-bwl/

%files -n texlive-biblatex-caspervector
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-caspervector/

%files -n texlive-biblatex-caspervector-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-caspervector/

%files -n texlive-biblatex-chem
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-chem/

%files -n texlive-biblatex-chem-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-chem/

%files -n texlive-biblatex-chicago
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-chicago/

%files -n texlive-biblatex-chicago-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-chicago/

%files -n texlive-biblatex-dw
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-dw/

%files -n texlive-biblatex-dw-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-dw/

%files -n texlive-biblatex-fiwi
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-fiwi/

%files -n texlive-biblatex-fiwi-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-fiwi/

%files -n texlive-biblatex-gost
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-gost/

%files -n texlive-biblatex-gost-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-gost/

%files -n texlive-biblatex-historian
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-historian/

%files -n texlive-biblatex-historian-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-historian/

%files -n texlive-biblatex-ieee
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-ieee/

%files -n texlive-biblatex-ieee-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-ieee/

%files -n texlive-biblatex-juradiss
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-juradiss/

%files -n texlive-biblatex-juradiss-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-juradiss/

%files -n texlive-biblatex-luh-ipw
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-luh-ipw/

%files -n texlive-biblatex-luh-ipw-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-luh-ipw/

%files -n texlive-biblatex-manuscripts-philology
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-manuscripts-philology/
%files -n texlive-biblatex-manuscripts-philology-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-manuscripts-philology/

%files -n texlive-biblatex-mla
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-mla/

%files -n texlive-biblatex-mla-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-mla/

%files -n texlive-biblatex-multiple-dm
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-multiple-dm/

%files -n texlive-biblatex-multiple-dm-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-multiple-dm/

%files -n texlive-biblatex-musuos
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-musuos/

%files -n texlive-biblatex-musuos-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-musuos/

%files -n texlive-biblatex-nature
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-nature/

%files -n texlive-biblatex-nature-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-nature/

%files -n texlive-biblatex-nejm
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-nejm/

%files -n texlive-biblatex-nejm-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-nejm/

%files -n texlive-biblatex-opcit-booktitle
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-opcit-booktitle/

%files -n texlive-biblatex-opcit-booktitle-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-opcit-booktitle/

%files -n texlive-biblatex-philosophy
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-philosophy/

%files -n texlive-biblatex-philosophy-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-philosophy/

%files -n texlive-biblatex-phys
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-phys/

%files -n texlive-biblatex-phys-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-phys/

%files -n texlive-biblatex-publist
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-publist/

%files -n texlive-biblatex-publist-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-publist/

%files -n texlive-biblatex-realauthor
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-realauthor/

%files -n texlive-biblatex-realauthor-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-realauthor/

%files -n texlive-biblatex-science
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-science/

%files -n texlive-biblatex-science-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-science/

%files -n texlive-biblatex-source-division
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-source-division/

%files -n texlive-biblatex-source-division-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-source-division/

%files -n texlive-biblatex-subseries
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-subseries/

%files -n texlive-biblatex-subseries-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-subseries/

%files -n texlive-biblatex-swiss-legal
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-swiss-legal/

%files -n texlive-biblatex-swiss-legal-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-swiss-legal/

%files -n texlive-biblatex
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bib/biblatex/
%{_texdir}/texmf-dist/bibtex/bst/biblatex/
%{_texdir}/texmf-dist/tex/latex/biblatex/

%files -n texlive-biblatex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/biblatex/

%files -n texlive-biblatex-trad
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-trad/

%files -n texlive-biblatex-trad-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-trad/

%files -n texlive-biblatex-true-citepages-omit
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-true-citepages-omit/

%files -n texlive-biblatex-true-citepages-omit-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-true-citepages-omit/

%files -n texlive-bibleref-french
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/bibleref-french/

%files -n texlive-bibleref-french-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/bibleref-french/

%files -n texlive-bibleref-german
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/bibleref-german/

%files -n texlive-bibleref-german-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/bibleref-german/

%files -n texlive-bibleref-lds
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/bibleref-lds/

%files -n texlive-bibleref-lds-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/bibleref-lds/

%files -n texlive-bibleref-mouth
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/bibleref-mouth/

%files -n texlive-bibleref-mouth-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/bibleref-mouth/

%files -n texlive-bibleref-parse
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/bibleref-parse/

%files -n texlive-bibleref-parse-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/bibleref-parse/

%files -n texlive-bibleref
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/bibleref/

%files -n texlive-bibleref-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/bibleref/

%files -n texlive-biblist
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/biblist/

%files -n texlive-biblist-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/biblist/

%files -n texlive-bibtopicprefix
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/bibtopicprefix/

%files -n texlive-bibtopicprefix-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/bibtopicprefix/

%files -n texlive-bibtopic
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/bibtopic/

%files -n texlive-bibtopic-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/bibtopic/

%files -n texlive-bibunits
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/bibunits/

%files -n texlive-bibunits-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/bibunits/

%files -n texlive-bidi-atbegshi
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/xelatex/bidi-atbegshi/

%files -n texlive-bidi-atbegshi-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/bidi-atbegshi/

%files -n texlive-bidicontour
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/xelatex/bidicontour/

%files -n texlive-bidicontour-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/bidicontour/

%files -n texlive-bidihl
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/xelatex/bidihl/

%files -n texlive-bidihl-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/bidihl/

%files -n texlive-bidipagegrid
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/xelatex/bidipagegrid/

%files -n texlive-bidipagegrid-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/bidipagegrid/

%files -n texlive-bidipresentation
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/xelatex/bidipresentation/

%files -n texlive-bidipresentation-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/bidipresentation/

%files -n texlive-bidishadowtext
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/xelatex/bidishadowtext/

%files -n texlive-bidishadowtext-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/bidishadowtext/

%files -n texlive-bidi
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/xelatex/bidi/

%files -n texlive-bidi-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/bidi/

%files -n texlive-bigfoot
%license gpl2.txt
%{_texdir}/texmf-dist/tex/latex/bigfoot/

%files -n texlive-bigfoot-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/latex/bigfoot/

%files -n texlive-bigints
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/bigints/

%files -n texlive-bigints-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/bigints/

%files -n texlive-binomexp
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/binomexp/

%files -n texlive-binomexp-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/binomexp/

%files -n texlive-biocon
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/biocon/

%files -n texlive-biocon-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/biocon/

%files -n texlive-bitelist
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/bitelist/

%files -n texlive-bitelist-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/bitelist/

%files -n texlive-bizcard
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/bizcard/

%files -n texlive-bizcard-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/bizcard/

%files -n texlive-beamercolorthemeowl-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/beamercolorthemeowl/

%files -n texlive-beamercolorthemeowl
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/beamercolorthemeowl/

%files -n texlive-beamertheme-detlevcm-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/beamertheme-detlevcm/

%files -n texlive-beamertheme-detlevcm
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/beamertheme-detlevcm/

%files -n texlive-beamertheme-epyt-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/beamertheme-epyt/

%files -n texlive-beamertheme-epyt
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/beamertheme-epyt/

%files -n texlive-beamertheme-metropolis-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/beamertheme-metropolis/

%files -n texlive-beamertheme-metropolis
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/beamertheme-metropolis/

%files -n texlive-beamer-verona-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/beamer-verona/

%files -n texlive-beamer-verona
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/beamer-verona/

%files -n texlive-biblatex-abnt-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-abnt/

%files -n texlive-biblatex-abnt
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-abnt/

%files -n texlive-biblatex-bookinother-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-bookinother/

%files -n texlive-biblatex-bookinother
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-bookinother/

%files -n texlive-biblatex-iso690-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-iso690/

%files -n texlive-biblatex-iso690
%license gpl3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-iso690/

%files -n texlive-biblatex-morenames-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-morenames/

%files -n texlive-biblatex-morenames
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-morenames/

%files -n texlive-bibletext-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/bibletext/

%files -n texlive-bibletext
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/bibletext/

%files -n texlive-bibtexperllibs-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/support/bibtexperllibs/

%files -n texlive-bibtexperllibs

%files -n texlive-bitpattern-doc
%license lppl.txt
%{_texdir}/texmf-dist/doc/latex/bitpattern/

%files -n texlive-bitpattern
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/bitpattern/

%files -n texlive-bestpapers-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/bibtex/bestpapers/

%files -n texlive-bestpapers
%license pd.txt
%{_texdir}/texmf-dist/bibtex/bst/bestpapers/

%files -n texlive-biblatex-claves
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-claves/

%files -n texlive-biblatex-claves-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-claves/

%files -n texlive-biblatex-ijsra
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-ijsra/

%files -n texlive-biblatex-ijsra-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-ijsra/

%files -n texlive-biblatex-lni
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-lni/

%files -n texlive-biblatex-lni-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-lni/

%files -n texlive-biblatex-nottsclassic
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-nottsclassic/

%files -n texlive-biblatex-nottsclassic-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/biblatex-nottsclassic/

%files -n texlive-beamerswitch
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/beamerswitch/
%{_texdir}/texmf-dist/tex/latex/beamerswitch/

%files -n texlive-beilstein
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/beilstein/
%{_texdir}/texmf-dist/bibtex/bst/beilstein/
%{_texdir}/texmf-dist/tex/latex/beilstein/

%files -n texlive-beuron
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/fonts/beuron/
%{_texdir}/texmf-dist/fonts/map/dvips/beuron/
%{_texdir}/texmf-dist/fonts/opentype/public/beuron/
%{_texdir}/texmf-dist/fonts/source/public/beuron/
%{_texdir}/texmf-dist/fonts/tfm/public/beuron/
%{_texdir}/texmf-dist/fonts/type1/public/beuron/
%{_texdir}/texmf-dist/tex/latex/beuron/

%files -n texlive-biblatex-cheatsheet-doc
%doc %{_texdir}/texmf-dist/doc/latex/biblatex-cheatsheet/

%files -n texlive-biblatex-enc
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/biblatex-enc/
%{_texdir}/texmf-dist/tex/latex/biblatex-enc/

%files -n texlive-biblatex-gb7714-2015
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/biblatex-gb7714-2015/
%{_texdir}/texmf-dist/tex/latex/biblatex-gb7714-2015/

%files -n texlive-biblatex-oxref
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/biblatex-oxref/
%{_texdir}/texmf-dist/tex/latex/biblatex-oxref/

%files -n texlive-biblatex-sbl
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/biblatex-sbl/
%{_texdir}/texmf-dist/makeindex/biblatex-sbl/
%{_texdir}/texmf-dist/tex/latex/biblatex-sbl/

%files -n texlive-biblatex-shortfields
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/biblatex-shortfields/
%{_texdir}/texmf-dist/tex/latex/biblatex-shortfields/

%files -n texlive-binarytree
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/binarytree/
%{_texdir}/texmf-dist/tex/latex/binarytree/

%files -n texlive-biochemistry-colors
%license lppl.txt gpl.txt
%doc %{_texdir}/texmf-dist/doc/latex/biochemistry-colors/
%{_texdir}/texmf-dist/tex/latex/biochemistry-colors/

%files -n texlive-biolett-bst
%license lppl1.txt
%doc %{_texdir}/texmf-dist/doc/bibtex/biolett-bst/
%{_texdir}/texmf-dist/bibtex/bst/biolett-bst/


%files -n texlive-beamertheme-cuerna
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/beamertheme-cuerna/
%doc %{_texdir}/texmf-dist/doc/latex/beamertheme-cuerna/

%files -n texlive-beamertheme-focus
%license gpl3.txt
%{_texdir}/texmf-dist/tex/latex/beamertheme-focus/
%doc %{_texdir}/texmf-dist/doc/latex/beamertheme-focus/

%files -n texlive-beamertheme-saintpetersburg
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/beamertheme-saintpetersburg/
%doc %{_texdir}/texmf-dist/doc/latex/beamertheme-saintpetersburg/

%files -n texlive-bezierplot
%license lppl.txt
%{_texdir}/texmf-dist/tex/lualatex/bezierplot/
%doc %{_texdir}/texmf-dist/doc/lualatex/bezierplot/

%files -n texlive-biblatex-archaeology
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-archaeology/
%doc %{_texdir}/texmf-dist/doc/latex/biblatex-archaeology/

%files -n texlive-biblatex-arthistory-bonn
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-arthistory-bonn/
%doc %{_texdir}/texmf-dist/doc/latex/biblatex-arthistory-bonn/

%files -n texlive-biblatex-socialscienceshuberlin
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/biblatex-socialscienceshuberlin/
%doc %{_texdir}/texmf-dist/doc/latex/biblatex-socialscienceshuberlin/


%changelog
* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init

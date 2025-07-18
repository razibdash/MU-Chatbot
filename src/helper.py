
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings


#load data from mu website
def get_mu_data():
    urls = [
    "https://www.metrouni.edu.bd/",
    "https://www.metrouni.edu.bd/sites/university/contact",
    "https://www.metrouni.edu.bd/sites/university/history",
    "https://www.metrouni.edu.bd/sites/university/vision-mission",
    "https://www.metrouni.edu.bd/sites/university/our-core-values",
    "https://www.metrouni.edu.bd/sites/university/accreditation-membership-collaboration",
    "https://www.metrouni.edu.bd/sites/university/convocation",
    "https://www.metrouni.edu.bd/sites/university/testimonial",
    "https://www.metrouni.edu.bd/sites/university/news",
    "https://www.metrouni.edu.bd/sites/university/event-calendar",
    "https://www.metrouni.edu.bd/sites/university/announcement",
    "https://www.metrouni.edu.bd/sites/leadership-and-management/advisors",
    "https://www.metrouni.edu.bd/sites/leadership-and-management/board-of-trustees",
    "https://www.metrouni.edu.bd/sites/leadership-and-management/syndicate",
    "https://www.metrouni.edu.bd/sites/leadership-and-management/academic-council",
    "https://www.metrouni.edu.bd/sites/leadership-and-management/senior-management-committee",
    "https://www.metrouni.edu.bd/sites/leadership-and-management/finance-committee",
    "https://www.metrouni.edu.bd/sites/leadership-and-management/exam-surveillance-committee",
    "https://www.metrouni.edu.bd/sites/leadership-and-management/admission-system-and-exam-review-committee",
    "https://www.metrouni.edu.bd/sites/leadership-and-management/teachers-selection-committee",
    "https://www.metrouni.edu.bd/sites/leadership-and-management/disciplinary-committee",
    "https://www.metrouni.edu.bd/sites/leadership-and-management/proctorial-committee",
    "https://www.metrouni.edu.bd/sites/leadership-and-management/anti-terrorism-committee",
    "https://www.metrouni.edu.bd/sites/leadership-and-management/anti-drug-committee",
    "https://www.metrouni.edu.bd/sites/leadership-and-management/sexual-abuse-and-harassment-prevention-committee",
    "https://www.metrouni.edu.bd/sites/leadership-and-management/anti-ragging-committee",
    "https://www.metrouni.edu.bd/sites/faculty-members/department-of-computer-science-engineering",
    "https://www.metrouni.edu.bd/sites/faculty-members/department-of-software-engineering",
    "https://www.metrouni.edu.bd/sites/faculty-members/department-of-electrical-electronic-engineering",
    "https://www.metrouni.edu.bd/sites/faculty-members/department-of-business-administration",
    "https://www.metrouni.edu.bd/sites/faculty-members/department-of-economics",
    "https://www.metrouni.edu.bd/sites/faculty-members/department-of-law-justice",
    "https://www.metrouni.edu.bd/sites/faculty-members/department-of-english",
    "https://www.metrouni.edu.bd/sites/office-administration/office-of-the-vice-chancellor",
    "https://www.metrouni.edu.bd/sites/office-administration/office-of-the-pro-vice-chancellor",
    "https://www.metrouni.edu.bd/sites/office-administration/office-of-the-treasurer",
    "https://www.metrouni.edu.bd/sites/office-administration/office-of-the-registrar",
    "https://www.metrouni.edu.bd/sites/office-administration/office-of-the-controller-of-examinations",
    "https://www.metrouni.edu.bd/sites/office-administration/library",
    "https://www.metrouni.edu.bd/sites/office-administration/it",
    "https://www.metrouni.edu.bd/sites/office-administration/admission",
    "https://www.metrouni.edu.bd/sites/office-administration/university-engineers-electrical-civil",
    "https://www.metrouni.edu.bd/sites/honours-programmes/bsc-in-computer-science-engineering",
    "https://www.metrouni.edu.bd/sites/honours-programmes/bsc-in-software-engineering",
    "https://www.metrouni.edu.bd/sites/honours-programmes/bsc-in-eee",
    "https://www.metrouni.edu.bd/sites/honours-programmes/b-sc-engg-in-ete",
    "https://www.metrouni.edu.bd/sites/honours-programmes/b-a-hons-in-english",
    "https://www.metrouni.edu.bd/sites/honours-programmes/bba",
    "https://www.metrouni.edu.bd/sites/honours-programmes/bss-in-economics",
    "https://www.metrouni.edu.bd/sites/honours-programmes/ll-b-hons",
    "https://www.metrouni.edu.bd/sites/masters-programmes/mba-regular",
    "https://www.metrouni.edu.bd/sites/masters-programmes/mba-general",
    "https://www.metrouni.edu.bd/sites/masters-programmes/m-a-in-english-preliminary-final",
    "https://www.metrouni.edu.bd/sites/masters-programmes/m-a-in-english-final",
    "https://www.metrouni.edu.bd/sites/masters-programmes/ll-m-1-year",
    "https://www.metrouni.edu.bd/sites/masters-programmes/ll-m-2-year",
    "https://www.metrouni.edu.bd/sites/masters-programmes/msc-in-mis",
    "https://www.metrouni.edu.bd/sites/masters-programmes/mss-in-economics",
    "https://www.metrouni.edu.bd/sites/short-programmes/android-application-development",
    "https://www.metrouni.edu.bd/sites/short-programmes/microcontroller-programming",
    "https://www.metrouni.edu.bd/sites/short-programmes/journalism-and-media-studies",
    "https://www.metrouni.edu.bd/sites/departments/computer-science-engineering",
    "https://www.metrouni.edu.bd/sites/departments/software-engineering",
    "https://www.metrouni.edu.bd/sites/departments/electrical-electronic-engineering",
    "https://www.metrouni.edu.bd/sites/departments/business-administration",
    "https://www.metrouni.edu.bd/sites/departments/economics",
    "https://www.metrouni.edu.bd/sites/departments/english",
    "https://www.metrouni.edu.bd/sites/departments/law-justice",
    "https://www.metrouni.edu.bd/sites/departments/journalism-and-media-studies-proposed",
    "https://www.metrouni.edu.bd/sites/academic-information/academic-policies",
    "https://www.metrouni.edu.bd/sites/academic-information/student-code-of-conduct",
    "https://www.metrouni.edu.bd/sites/academic-information/prospectus",
    "https://www.metrouni.edu.bd/sites/academic-information/examination",
    "https://www.metrouni.edu.bd/sites/academic-information/academic-calendar-summer-2025",
    "https://www.metrouni.edu.bd/sites/academic-information/payment-instruction",
    "https://www.metrouni.edu.bd/sites/academic-information/apply-for-certificate-and-transcript",
    "https://www.metrouni.edu.bd/sites/academic-information/online-forms",
    "https://www.metrouni.edu.bd/sites/admission/undergraduate",
    "https://www.metrouni.edu.bd/sites/admission/graduate",
    "https://www.metrouni.edu.bd/sites/admission/short-course",
    "https://www.metrouni.edu.bd/sites/admission/programme-fee-structure",
    "https://www.metrouni.edu.bd/sites/admission/online-admission-form",
    "https://www.metrouni.edu.bd/sites/admission/scholarship-aid",
    "https://www.metrouni.edu.bd/sites/admission/faq",
    "https://www.metrouni.edu.bd/sites/research/research-cell",
    "https://www.metrouni.edu.bd/sites/research/journal",
    "https://www.metrouni.edu.bd/sites/research/newsletter",
    "https://www.metrouni.edu.bd/sites/facilities/one-stop-service",
    "https://www.metrouni.edu.bd/sites/facilities/career-centre",
    "https://www.metrouni.edu.bd/sites/facilities/digital-campus",
    "https://www.metrouni.edu.bd/sites/facilities/library-faculity",
    "https://www.metrouni.edu.bd/sites/facilities/laboratory-resources",
    "https://www.metrouni.edu.bd/sites/facilities/cafeteria",
    "https://www.metrouni.edu.bd/sites/facilities/auditorium",
    "https://www.metrouni.edu.bd/sites/facilities/play-ground",
    "https://www.metrouni.edu.bd/sites/facilities/it-support-centre",
    "https://www.metrouni.edu.bd/sites/facilities/accommodation",
    "https://www.metrouni.edu.bd/sites/club-organisations/mu-sports-club",
    "https://www.metrouni.edu.bd/sites/club-organisations/mu-hult-prize",
    "https://www.metrouni.edu.bd/sites/club-organisations/mu-rover-scouts",
    "https://www.metrouni.edu.bd/sites/club-organisations/mu-karate-club",
    "https://www.metrouni.edu.bd/sites/club-organisations/mu-social-services-club",
    "https://www.metrouni.edu.bd/sites/club-organisations/mu-theater",
    "https://www.metrouni.edu.bd/sites/club-organisations/mu-cultural-club",
    "https://www.metrouni.edu.bd/sites/club-organisations/mu-debating-club",
    "https://www.metrouni.edu.bd/sites/club-organisations/mu-model-united-nation",
    "https://www.metrouni.edu.bd/sites/club-organisations/mu-cycling-association",
    "https://www.metrouni.edu.bd/sites/club-organisations/mu-photographic-society",
    "https://www.metrouni.edu.bd/sites/club-organisations/mu-robotics-club",
    "https://www.metrouni.edu.bd/sites/club-organisations/swe-innovators-forum",
    "https://www.metrouni.edu.bd/sites/club-organisations/mu-geography-astronomical-society-mugas",
    "https://www.metrouni.edu.bd/sites/iqac/mission-vision",
    "https://www.metrouni.edu.bd/sites/iqac/benefits",
    "https://www.metrouni.edu.bd/sites/iqac/expected-results",
    "https://www.metrouni.edu.bd/sites/iqac/management-team",
    "http://metrouni.edu.bd/sites/university/career",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/171",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/172",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/173",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/176",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/177",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/179",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/180",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/181",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/182",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/183",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/184",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/185",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/186",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/187",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/189",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/192",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/194",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/195",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/198",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/199",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/201",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/204",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/344",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/345",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/307",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/308",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/335",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/311",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/312",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/309",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/310",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-computer-science-engineering/383",

    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-software-engineering/212",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-software-engineering/213",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-software-engineering/214",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-software-engineering/215",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-software-engineering/216",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-software-engineering/219",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-software-engineering/317",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-software-engineering/341",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-software-engineering/397",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-software-engineering/390",

    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-electrical-electronic-engineering/219",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-electrical-electronic-engineering/220",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-electrical-electronic-engineering/226",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-electrical-electronic-engineering/228",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-electrical-electronic-engineering/313",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-electrical-electronic-engineering/315",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-electrical-electronic-engineering/316",

    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-business-administration/276",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-business-administration/277",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-business-administration/346",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-business-administration/280",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-business-administration/278",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-business-administration/279",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-business-administration/281",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-business-administration/282",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-business-administration/284",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-business-administration/286",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-business-administration/285",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-business-administration/287",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-business-administration/288",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-business-administration/302",
    "https://metrouni.edu.bd/sites/university/faculty-members/department-of-business-administration/303",

    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-economics/235",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-economics/236",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-economics/239",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-economics/301",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-economics/240",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-economics/241",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-economics/242",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-economics/243",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-economics/387",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-economics/244",

    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-law-justice/265",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-law-justice/266",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-law-justice/268",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-law-justice/269",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-law-justice/270",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-law-justice/271",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-law-justice/272",

    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-english/247",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-english/260",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-english/250",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-english/251",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-english/253",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-english/252",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-english/255",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-english/258",
    "https://www.metrouni.edu.bd/sites/university/faculty-members/department-of-english/261",



        ]

    loader = UnstructuredURLLoader(urls=urls)
    raw_docs = loader.load()
    return raw_docs


#Split the Data into Text Chunks
def text_split(mu_data):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    text_chunks=text_splitter.split_documents(mu_data)
    return text_chunks


#Download the Embeddings from Hugging Face
def download_hugging_face_embeddings():
    embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    return embeddings

embeddings = download_hugging_face_embeddings()
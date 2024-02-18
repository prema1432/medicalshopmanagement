from django.core.management.base import BaseCommand

from users.models import MedicalProductCategory

medical_product_categories = [
    {"name": "Pharmaceuticals",
     "description": "Medications and drugs used for therapeutic purposes, including prescription and over-the-counter medications."},
    {"name": "Medical Devices",
     "description": "Instruments, apparatuses, machines, implants, and other similar or related articles intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease."},
    {"name": "Diagnostic Equipment",
     "description": "Instruments and devices used to diagnose medical conditions, including imaging equipment, diagnostic tests, and laboratory equipment."},
    {"name": "Surgical Instruments",
     "description": "Tools and instruments used by surgeons during surgical procedures, including scalpels, forceps, retractors, and sutures."},
    {"name": "Orthopedic Supplies",
     "description": "Devices and equipment used in the treatment of musculoskeletal conditions and injuries, such as braces, splints, and orthopedic implants."},
    {"name": "Dental Products",
     "description": "Supplies and equipment used by dentists in the diagnosis, treatment, and prevention of oral diseases and conditions."},
    {"name": "Medical Consumables",
     "description": "Disposable medical supplies used in healthcare settings, including gloves, syringes, bandages, and dressings."},
    {"name": "Rehabilitation Equipment",
     "description": "Devices and equipment used in physical therapy and rehabilitation programs to improve mobility, strength, and function."},
    {"name": "Laboratory Supplies",
     "description": "Equipment, consumables, and reagents used in laboratory settings for research, testing, and analysis purposes."},
    {"name": "First Aid Supplies",
     "description": "Emergency supplies and equipment used to provide immediate care for injuries and illnesses."},
    {"name": "Veterinary Products",
     "description": "Medications, supplies, and equipment used in veterinary medicine for the diagnosis, treatment, and prevention of diseases in animals."},
    {"name": "Ophthalmic Supplies",
     "description": "Equipment, instruments, and supplies used in the diagnosis and treatment of eye conditions and diseases."},
    {"name": "Dermatological Products",
     "description": "Medications, creams, and ointments used in the diagnosis, treatment, and prevention of skin conditions and diseases."},
    {"name": "Respiratory Equipment",
     "description": "Devices and equipment used to assist with breathing and respiratory function, including oxygen tanks, nebulizers, and ventilators."},
    {"name": "Infusion and IV Supplies",
     "description": "Equipment and supplies used in intravenous therapy, including IV catheters, infusion pumps, and IV fluids."},
    {"name": "Home Health Care Products",
     "description": "Medical equipment and supplies designed for use in home healthcare settings, including home monitoring devices, mobility aids, and personal care products."},
    {"name": "Mobility Aids",
     "description": "Devices and equipment designed to assist individuals with mobility impairments, including wheelchairs, walkers, and canes."},
    {"name": "Patient Monitoring Devices",
     "description": "Devices used to monitor and track vital signs and physiological parameters in patients, including ECG monitors, pulse oximeters, and blood pressure monitors."},
    {"name": "Wound Care Products",
     "description": "Supplies and equipment used in the management and treatment of wounds, including wound dressings, bandages, and wound irrigation kits."},
    {"name": "Personal Protective Equipment (PPE)",
     "description": "Protective clothing, masks, gloves, and other equipment worn to protect healthcare workers and patients from exposure to infectious agents and hazardous materials."},
    {"name": "Healthcare Furniture",
     "description": "Furniture designed for use in healthcare settings, including hospital beds, examination tables, and medical chairs."},
    {"name": "Medical Imaging Equipment",
     "description": "Equipment used to create visual representations of the interior of the body for clinical analysis and medical intervention, including X-ray machines, MRI scanners, and ultrasound machines."},
    {"name": "Emergency Medical Supplies",
     "description": "Supplies and equipment used in emergency medical situations, including trauma kits, defibrillators, and emergency airway management devices."},
    {"name": "Sterilization Equipment",
     "description": "Equipment used to sterilize medical instruments and equipment to prevent the spread of infections, including autoclaves, sterilization pouches, and chemical sterilants."},
    {"name": "Blood Collection Supplies",
     "description": "Equipment and supplies used in the collection, processing, and storage of blood and blood products, including blood collection tubes, needles, and blood bags."},
    {"name": "Urology Supplies",
     "description": "Equipment and supplies used in the diagnosis and treatment of urinary tract disorders and conditions, including catheters, urinary drainage bags, and urodynamic testing equipment."},
    {"name": "Gynecological Products",
     "description": "Equipment, instruments, and supplies used in the diagnosis and treatment of gynecological conditions and diseases, including speculums, pap smear kits, and intrauterine devices (IUDs)."},
    {"name": "Enteral Feeding Supplies",
     "description": "Equipment and supplies used in enteral nutrition therapy to deliver nutrients directly into the gastrointestinal tract, including feeding tubes, syringes, and enteral feeding pumps."},
    {"name": "Medical Software and Apps",
     "description": "Software applications and mobile apps used in healthcare settings for patient management, electronic health records (EHR), medical imaging, and clinical decision support."},
    {"name": "Biomedical Engineering Equipment",
     "description": "Equipment used by biomedical engineers in the design, development, and maintenance of medical devices and healthcare systems, including CAD software, testing equipment, and prototyping tools."},
    {"name": "Healthcare IT Solutions",
     "description": "Information technology solutions and systems used in healthcare settings for data management, communication, and workflow optimization, including electronic medical records (EMR), health information exchange (HIE), and telemedicine platforms."},
    {"name": "Telemedicine Equipment",
     "description": "Equipment and technology used to facilitate remote medical consultations and telehealth services, including video conferencing systems, remote monitoring devices, and telemedicine carts."},
    {"name": "Assistive Technology Devices",
     "description": "Devices and equipment designed to assist individuals with disabilities in performing daily activities and tasks, including hearing aids, prosthetic limbs, and communication devices."},
    {"name": "Pharmacy Automation Systems",
     "description": "Automated systems and technology used in pharmacies to streamline medication dispensing, inventory management, and prescription processing, including automated pill dispensers, robotic dispensing systems, and pharmacy management software."},
    {"name": "Medical Books and References",
     "description": "Books, journals, and reference materials used by healthcare professionals for medical education, research, and clinical practice."},
    {"name": "Medical Training and Simulation Tools",
     "description": "Training aids, simulators, and educational tools used in medical training programs to teach and practice clinical skills, procedures, and techniques."},
]


class Command(BaseCommand):
    help = 'Generate medical product categories'

    def handle(self, *args, **options):
        existing_category_names = set(MedicalProductCategory.objects.values_list('name', flat=True))

        for category_data in medical_product_categories:
            category_name = category_data["name"]
            if category_name in existing_category_names:
                self.stdout.write(self.style.WARNING(f'Category "{category_name}" already exists. Skipping...'))
                continue

            category_description = category_data["description"]

            MedicalProductCategory.objects.create(name=category_name, description=category_description)
            self.stdout.write(self.style.SUCCESS(f'Created category "{category_name}"'))

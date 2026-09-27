/**
 * Doctor Bio Modal Handler & Multilingual Data
 * Supports DE, EN, RU, TR, AR
 * Updated with full CV data for:
 * - Dr. med. Kasim Fischer-Rahimov
 * - Dr. med. Tanyo B. Hristov
 * - Herr Habib Pirmoradi
 * - Herr Timur Khabibullin
 */
(function() {
  const doctorsData = {
    de: {
      labels: {
        qual: 'Facharzt & Akademischer Grad',
        exp: 'Beruflicher Werdegang & Erfahrung',
        focus: 'Klinische Schwerpunkte & Qualifikationen',
        close: 'Schließen'
      },
      doctors: {
        fischer: {
          name: 'Dr. med. Kasim Fischer-Rahimov',
          img: 'img/surgeon1.webp',
          role: 'Facharzt für Neurochirurgie · Praxisinhaber',
          degree: 'Promotion (Dr. med.) · Ärztlicher Weiterbilder',
          qual: 'Facharzt für Neurochirurgie (2006) · Zertifizierte Expertise in der Wirbelsäulenchirurgie · Zusatzbezeichnungen: Spezielle Schmerztherapie (2015), Psychosomatische Therapie (2015), Akupunktur · Niedergelassener Vertragsarzt & Weiterbildungsbefugter.',
          experience: [
            'Studium der Humanmedizin an der Staatlichen Medizinischen Universität Irkutsk & Staatliches Institut für Ärztefortbildung (1992–2000)',
            'Facharztausbildung für Neurochirurgie am Universitätsklinikum Jena und am Klinikum Meiningen GmbH (2003–2008)',
            'Facharzt für Neurochirurgie (2006)',
            'Funktion Oberarzt Neurochirurgie Köln Merheim (2009)',
            'Leitender Oberarzt Neurochirurgie MHO Osnabrück (2011)',
            'Chefarzt der Mikroneurochirurgie mbH Gensingen (2013)',
            'Zusatzbezeichnung Spezielle NCH-Schmerztherapie & Psychosomatische Therapie (2015)',
            'Gründung & Niederlassung in eigener Praxis für Neurochirurgie Mönchengladbach (2015)',
            'Promotion: Vergleich minimal-invasiver Operationsverfahren zur Fusion der Iliosakralgelenke – 4-Jahresresultate mit klinischen und radiologischen Befunden (2023)'
          ],
          focus: [
            'Minimalinvasive Wirbelsäulenchirurgie',
            'Mikrochirurgische Dekompression',
            'Bandscheibenendoprothetik (HWS & LWS)',
            'Spezielle Schmerztherapie',
            'ISG-Fusion & Facettengelenke',
            'Psychosomatische Grundversorgung'
          ]
        },
        hristov: {
          name: 'Dr. med. Tanyo B. Hristov',
          img: 'img/team_tanyo.webp',
          role: 'Facharzt für Neurochirurgie · Standortleiter',
          degree: 'Promotion (Dr. med., magna cum laude) · Facharzt für Neurochirurgie',
          qual: 'Facharzt für Neurochirurgie (Ärztekammer Nordrhein, 2016) · Basis-Zertifikat Wirbelsäulenchirurgie der DWG (2017) · Fachkunde Strahlenschutz & Fluoroskopie (2020) · Therapeut für funktionelle Medizin (2026).',
          experience: [
            'Studium der Humanmedizin an der Universität zu Köln (2003–2009), Approbation als Arzt (2010)',
            'Promotion am Institut für Anatomie der Uniklinik Köln (Note: magna cum laude, 2010)',
            'Weiterbildungsassistent an der Klinik für Neurochirurgie Köln-Merheim, Klinikum der Universität Witten-Herdecke (2010–2016)',
            'Neurophysiologie-Mentorship durch Prof. D. Debatisse, CHUV, Lausanne (2010–2011)',
            'Facharzt für Neurochirurgie, Ärztekammer Nordrhein (2016)',
            'Oberarzt für Wirbelsäulenchirurgie und Neurochirurgie, Rhein-Maas-Klinikum Würselen (Level I-Klinik der DWG, 2018)',
            'Leiter Wirbelsäulenchirurgie an der LVR-Klinik für Orthopädie Viersen (2018–2023)',
            'Operative neurochirurgische Tätigkeit in Düsseldorf, Clinic Bel Etage (2023–2025)',
            'Privatärztliche Praxis für Neurochirurgie in Köln / Gründung HRISTOV medical (seit 2024)',
            'Standortleiter der Praxis für Neurochirurgie Mönchengladbach'
          ],
          focus: [
            'Bandscheibenprothetik der HWS und LWS',
            'Bandscheibendegeneration sämtlicher Abschnitte',
            'Komplexe & instrumentierte Revisionschirurgie',
            'Minimalinvasive Zugänge (PLIF, MIS TLIF, ALIF, OLIF, XLIF)',
            'Degenerative & traumatische Deformitäten',
            'Chronische Schmerzsyndrome (SCS)',
            'ISG-Fusion & Beckenstabilisierung'
          ]
        },
        pirmoradi: {
          name: 'Herr Habib Pirmoradi',
          img: 'img/team_habib.webp',
          role: 'Neurochirurg AiW · Facharzt für Neurochirurgie',
          degree: 'Approbierter Arzt in Deutschland · Facharzt für Neurochirurgie',
          qual: 'Approbierter Arzt in Deutschland (Münster) · Facharzt für Neurochirurgie (Universität Isfahan, 2016) mit mehrjähriger chirurgischer Erfahrung · Über 800 eigenständig erfolgreich durchgeführte Operationen (Tumor- & Wirbelsäulenchirurgie) · Fachsprachprüfung Ärztekammer Nordrhein.',
          experience: [
            'Studium der Humanmedizin an der Universität Najafabad, Isfahan (1996–2003)',
            'Facharztausbildung in Neurochirurgie an der Universität Isfahan, Abschluss unter den besten 10 % (2012–2017)',
            'Facharzt für Neurochirurgie (2016)',
            'Facharzt für Neurochirurgie am Kowsar Krankenhaus, Sanandaj (Über 800 erfolgreiche Operationen, 2016–2022)',
            'Facharzt für Neurochirurgie am Milad Krankenhaus, Isfahan (Leitung komplexer neurochirurgischer Eingriffe, Tumor- und Wirbelsäulenchirurgie, 2023–2024)',
            'Fachsprachprüfung Ärztekammer Nord & Berufserlaubnis als Arzt in Deutschland (2025)',
            'Assistenzarzt Neurologie & Geriatrie im Elisabethkrankenhaus Recklinghausen (2025)',
            'Approbation als Arzt in Deutschland (Münster, 2026)',
            'Neurochirurg in Weiterbildung in der Praxis für Neurochirurgie Mönchengladbach'
          ],
          focus: [
            'Mikrochirurgie',
            'Wirbelsäulen- & Bandscheibenchirurgie',
            'Dekompression bei Spinalkanalstenose',
            'Instrumentierte Wirbelsäulenoperationen',
            'Hirntumoren & Rückenmarkstumoren',
            'Schädelchirurgie & Notfallversorgung'
          ]
        },
        khabibullin: {
          name: 'Herr Timur Khabibullin',
          img: 'img/team_timur.webp',
          role: 'Assistenzarzt Neurochirurgie',
          degree: 'Approbierter Arzt (Diplom mit Auszeichnung) · FSP Medizin C1',
          qual: 'Arzt mit klinischer Erfahrung in Radiologie, Chirurgie und klinischen Studien · Zusatzqualifikationen in Radiologie (2019) und Ultraschalldiagnostik (2024) · Berufserlaubnis Nordrhein-Westfalen.',
          experience: [
            'Studium der Humanmedizin an der Staatlichen Medizinuniversität Irkutsk (Diplom mit Auszeichnung, 2009–2015)',
            'Weiterbildung & Assistenzarzt für Chirurgie am Irkutsker Regionalklinikum (Allgemein-, Gefäß- und Notfallchirurgie, 2015–2017)',
            'Projektmanager für klinische Studien, Aktiengesellschaft "Farmasintez" (2017–2020)',
            'Tätigkeit und Weiterbildung in Radiologie (Röntgen-/CT-Diagnostik) am Klinischen Krankenhaus Irkutsk Nr. 1 (2019–2022)',
            'Berufliche Zusatzqualifikation Radiologie (2019) & Ultraschalldiagnostik (2024)',
            'Medizinischer Übersetzer & interkulturelle Fachkommunikation (2022–2024)',
            'Einarbeitung deutsches Gesundheitssystem, FSP-Medizin C1 & Berufserlaubnis NRW (2025)',
            'Assistenzarzt in der Praxis für Neurochirurgie Mönchengladbach'
          ],
          focus: [
            'Bildgebende Diagnostik (CT, MRT, Röntgen, Ultraschall)',
            'Neurochirurgische Patientenbetreuung & Verlaufskontrollen',
            'Konservative und interventionelle Wirbelsäulentherapie',
            'Interdisziplinäre Zusammenarbeit',
            'Mehrsprachige Betreuung (Deutsch, Russisch, Englisch, Französisch, Tadschikisch, Türkisch)'
          ]
        }
      }
    },
    en: {
      labels: {
        qual: 'Speciality & Academic Degree',
        exp: 'Professional Experience & Career',
        focus: 'Clinical Focus & Key Qualifications',
        close: 'Close'
      },
      doctors: {
        fischer: {
          name: 'Dr. med. Kasim Fischer-Rahimov',
          img: 'img/surgeon1.webp',
          role: 'Specialist in Neurosurgery · Practice Owner',
          degree: 'Doctorate (Dr. med.) · Medical Trainer',
          qual: 'Specialist in Neurosurgery (2006) · Certified expertise in spine surgery · Additional qualifications: Special Pain Therapy (2015), Psychosomatic Therapy (2015), Acupuncture · Established Panel Physician & Authorized Training Supervisor.',
          experience: [
            'Study of Human Medicine at Irkutsk State Medical University & State Institute for Postgraduate Medical Education (1992–2000)',
            'Specialist training in Neurosurgery at Jena University Hospital and Klinikum Meiningen GmbH (2003–2008)',
            'Specialist in Neurosurgery (2006)',
            'Senior Physician in Neurosurgery, Cologne Merheim (2009)',
            'Leading Senior Physician in Neurosurgery, MHO Osnabrück (2011)',
            'Chief Physician, Mikroneurochirurgie mbH Gensingen (2013)',
            'Additional qualifications in Special Pain Therapy & Psychosomatic Therapy (2015)',
            'Founded own Neurosurgery Practice in Mönchengladbach (2015)',
            'Doctoral thesis: Comparison of minimally invasive surgical procedures for fusion of the sacroiliac joints (2023)'
          ],
          focus: [
            'Minimally invasive spine surgery',
            'Microsurgical decompression',
            'Disc arthroplasty (cervical & lumbar)',
            'Specialized pain therapy',
            'SI joint fusion & facet denervation',
            'Psychosomatic basic care'
          ]
        },
        hristov: {
          name: 'Dr. med. Tanyo B. Hristov',
          img: 'img/team_tanyo.webp',
          role: 'Specialist in Neurosurgery · Location Director',
          degree: 'Doctorate (Dr. med., magna cum laude) · Specialist in Neurosurgery',
          qual: 'Specialist in Neurosurgery (Medical Chamber of North Rhine, 2016) · Basic Certificate in Spine Surgery of the DWG (2017) · Radiation Protection & Fluoroscopy (2020) · Certified Therapist for Functional Medicine (2026).',
          experience: [
            'Study of Human Medicine at the University of Cologne (2003–2009), Medical License (Approbation 2010)',
            'Doctoral graduation (Dr. med.) at the Institute of Anatomy, University Hospital Cologne (magna cum laude, 2010)',
            'Resident in Neurosurgery, Cologne-Merheim Hospital, Witten-Herdecke University (2010–2016)',
            'Neurophysiology Mentorship under Prof. D. Debatisse, CHUV Lausanne (2010–2011)',
            'Specialist in Neurosurgery, Medical Chamber North Rhine (2016)',
            'Senior Physician for Spine Surgery & Neurosurgery, Rhein-Maas-Klinikum Würselen (DWG Level I Clinic, 2018)',
            'Head of Spine Surgery, LVR Orthopedic Clinic Viersen (2018–2023)',
            'Consultant Neurosurgeon, Clinic Bel Etage Düsseldorf (2023–2025)',
            'Private Practice for Neurosurgery in Cologne / Founder of HRISTOV medical (since 2024)',
            'Location Director and Senior Neurosurgeon, Practice for Neurosurgery Mönchengladbach'
          ],
          focus: [
            'Artificial disc replacement (cervical & lumbar)',
            'Degenerative disc diseases of all spinal sections',
            'Complex & instrumented revision spinal surgery',
            'Minimally invasive approaches (PLIF, MIS TLIF, ALIF, OLIF, XLIF)',
            'Degenerative & traumatic deformities and instabilities',
            'Chronic pain management (Spinal Cord Stimulation - SCS)',
            'SI joint fusion & pelvic instrumentation'
          ]
        },
        pirmoradi: {
          name: 'Herr Habib Pirmoradi',
          img: 'img/team_habib.webp',
          role: 'Neurosurgery Resident (AiW) · Specialist in Neurosurgery',
          degree: 'Licensed Physician in Germany · Specialist in Neurosurgery',
          qual: 'Licensed physician in Germany (Approbation Münster) · Specialist in Neurosurgery with extensive surgical track record (Isfahan University, 2016) · Over 800 successfully performed neurosurgical procedures (spine, brain tumors, microsurgery) · Medical Language Examination Medical Chamber North Rhine.',
          experience: [
            'Study of Human Medicine at Najafabad University, Isfahan (1996–2003)',
            'Specialist training in Neurosurgery at Isfahan University, top 10% graduation (2012–2017)',
            'Specialist in Neurosurgery (2016)',
            'Specialist Neurosurgeon at Kowsar Hospital, Sanandaj (over 800 successful surgeries, 2016–2022)',
            'Lead Neurosurgeon at Milad Hospital, Isfahan (complex cranial & spinal surgery, 2023–2024)',
            'Medical Language Examination & Practice License in Germany (2025)',
            'Clinical physician in Neurology & Geriatrics, Elisabeth Hospital Recklinghausen (2025)',
            'Full medical license (Approbation Münster, 2026)',
            'Resident Neurosurgeon at Practice for Neurosurgery Mönchengladbach'
          ],
          focus: [
            'Microsurgery',
            'Spine & herniated disc surgery',
            'Spinal canal decompression',
            'Instrumented spinal fusion',
            'Brain and spinal cord tumors',
            'Cranial surgery & emergency care'
          ]
        },
        khabibullin: {
          name: 'Herr Timur Khabibullin',
          img: 'img/team_timur.webp',
          role: 'Assistant Physician',
          degree: 'Licensed Physician (Diploma with Honors) · FSP Medicine C1',
          qual: 'Physician with clinical experience in radiology, surgery and clinical trials · Additional qualifications in Radiology (2019) and Ultrasound (2024) · Medical license for North Rhine-Westphalia.',
          experience: [
            'Study of Human Medicine at Irkutsk State Medical University (Diploma with Honors, 2009–2015)',
            'Residency & Assistant Physician in Surgery, Irkutsk Regional Clinical Hospital (2015–2017)',
            'Project Manager for Clinical Trials, Pharmasyntez JSC (2017–2020)',
            'Residency and clinical radiology practice (X-Ray / CT Diagnostics), Irkutsk City Hospital No. 1 (2019–2022)',
            'Postgraduate qualifications in Radiology (2019) & Diagnostic Ultrasound (2024)',
            'Medical translation and international healthcare communication (2022–2024)',
            'German healthcare system integration, Medical Language C1 & License NRW (2025)',
            'Assistant Physician at Practice for Neurosurgery Mönchengladbach'
          ],
          focus: [
            'Diagnostic imaging (CT, MRI, X-ray, Ultrasound)',
            'Neurosurgical patient care & clinical monitoring',
            'Conservative spinal therapies',
            'Interdisciplinary case collaboration',
            'Multilingual care (German, Russian, English, French, Tajik, Turkish)'
          ]
        }
      }
    },
    ru: {
      labels: {
        qual: 'Специальность и учёная степень',
        exp: 'Профессиональный опыт и карьера',
        focus: 'Клинические направления и квалификации',
        close: 'Закрыть'
      },
      doctors: {
        fischer: {
          name: 'Д-р мед. Касим Фишер-Рахимов',
          img: 'img/surgeon1.webp',
          role: 'Врач-специалист по нейрохирургии · Владелец клиники',
          degree: 'Доктор медицинских наук (Dr. med.) · Врач-наставник',
          qual: 'Врач-специалист по нейрохирургии (2006) · Сертифицированный эксперт по хирургии позвоночника · Дополнительные квалификации: Специальная терапия боли (2015), Психосоматическая терапия (2015), Акупунктура · Практикующий врач-специалист и руководитель подготовки врачей.',
          experience: [
            'Обучение медицине в Иркутском государственном медицинском университете и институте усовершенствования врачей (1992–2000)',
            'Специализация по нейрохирургии в Университетской клинике Йены и Klinikum Meiningen GmbH (2003–2008)',
            'Врач-специалист по нейрохирургии (2006)',
            'Старший врач нейрохирургического отделения, Кёльн-Мерхайм (2009)',
            'Ведущий старший врач нейрохирургии, MHO Оснабрюк (2011)',
            'Главный врач микронейрохирургии mbH Гензинген (2013)',
            'Дополнительные квалификации: Специальная терапия боли & Психосоматическая терапия (2015)',
            'Основание собственной практики нейрохирургии в Мёнхенгладбахе (2015)',
            'Защита докторской диссертации (Promotion Dr. med.): Сравнение малоинвазивных методов стабилизации крестцово-подвздошных суставов (2023)'
          ],
          focus: [
            'Малоинвазивная хирургия позвоночника',
            'Микрохирургическая декомпрессия',
            'Эндопротезирование межпозвоночных дисков (шейный и поясничный отделы)',
            'Специализированная противоболевая терапия',
            'Стабилизация КПС и фасеточные суставы',
            'Психосоматическая медицина'
          ]
        },
        hristov: {
          name: 'Д-р мед. Танйо Б. Христов',
          img: 'img/team_tanyo.webp',
          role: 'Врач-нейрохирург · Руководитель филиала (Standortleiter)',
          degree: 'Доктор медицинских наук (Dr. med., magna cum laude)',
          qual: 'Врач-специалист по нейрохирургии (Врачебная палата Северного Рейна, 2016) · Сертификат спинального хирурга Немецкого общества позвоночника DWG (2017) · Радиационная безопасность и интраоперационная флюороскопия (2020) · Терапевт функциональной медицины (2026).',
          experience: [
            'Изучение лечебного дела в Кёльнском университете (2003–2009), врачебная апробация (2010)',
            'Защита докторской диссертации (Dr. med.) в Институте анатомии университетской клиники Кёльна (magna cum laude, 2010)',
            'Врач-резидент клиники нейрохирургии Кёльн-Мерхайм, Университет Виттен-Хердеке (2010–2016)',
            'Менторшип по нейрофизиологии у проф. Д. Дебатисса, CHUV Лозанна (2010–2011)',
            'Врач-специалист по нейрохирургии, Ärztekammer Nordrhein (2016)',
            'Старший врач спинальной хирургии и нейрохирургии, Rhein-Maas-Klinikum Вюрзелен (клиника DWG I уровня, 2018)',
            'Руководитель отделения хирургии позвоночника ортопедической клиники LVR Фирзен (2018–2023)',
            'Ведущий хирург-нейрохирург в Clinic Bel Etage Дюссельдорф (2023–2025)',
            'Частная практика нейрохирургии в Кёльне / основатель HRISTOV medical (с 2024)',
            'Руководитель филиала (Standortleiter) и ведущий нейрохирург клиники в Мёнхенгладбахе'
          ],
          focus: [
            'Эндопротезирование дисков шейного и поясничного отделов',
            'Дегенеративные поражения дисков всех отделов позвоночника',
            'Сложные ревизионные и реконструктивные операции',
            'Малоинвазивные доступы (PLIF, MIS TLIF, ALIF, OLIF, XLIF)',
            'Дегенеративные и посттравматические деформации',
            'Хронические болевые синдромы (стимуляция спинного мозга - SCS)',
            'Стабилизация крестцово-подвздошных суставов (КПС)'
          ]
        },
        pirmoradi: {
          name: 'Хабиб Пирморади',
          img: 'img/team_habib.webp',
          role: 'Врач-нейрохирург (AiW) · Специалист по нейрохирургии',
          degree: 'Апробированный врач в Германии · Врач-специалист по нейрохирургии',
          qual: 'Врач с государственной апробацией в Германии (Мюнстер) · Врач-специалист по нейрохирургии (Университет Исфахана, 2016) с многолетним опытом самостоятельной хирургической практики · Более 800 успешно проведенных нейрохирургических операций (опухоли, патологии позвоночника, микрохирургия) · Экзамен по медицинскому немецкому языку Ärztekammer Nordrhein.',
          experience: [
            'Обучение лечебному делу в Университете Наджафабада, Исфахан (1996–2003)',
            'Специализация и резидентура по нейрохирургии в Университете Исфахана, выпуск в числе лучших 10% курса (2012–2017)',
            'Врач-специалист по нейрохирургии (2016)',
            'Врач-нейрохирург госпиталя Ковсар, Санандадж (более 800 успешных операций, 2016–2022)',
            'Ведущий специалист-нейрохирург больницы Милад, Исфахан (руководство сложными нейрохирургическими вмешательствами, вертебрология и онкохирургия, 2023–2024)',
            'Сдача экзамена по медицинскому языку и получение разрешения на врачебную деятельность в Германии (2025)',
            'Клиническая практика в отделении неврологии и гериатрии госпиталя св. Елизаветы Реклингхаузен (2025)',
            'Государственная апробация врача в Германии (Мюнстер, 2026)',
            'Врач-нейрохирург клиники нейрохирургии в Мёнхенгладбахе'
          ],
          focus: [
            'Микрохирургия',
            'Хирургия позвоночника и межпозвоночных дисков',
            'Декомпрессия при стенозе позвоночного канала',
            'Инструментальная стабилизация позвоночника',
            'Опухоли головного и спинного мозга',
            'Черепно-мозговая хирургия и экстренная помощь'
          ]
        },
        khabibullin: {
          name: 'Тимур Хабибуллин',
          img: 'img/team_timur.webp',
          role: 'Врач-ассистент нейрохирургии',
          degree: 'Врач (диплом с отличием) · Медицинский языковой сертификат C1',
          qual: 'Врач с клиническим опытом в радиологии, хирургии и клинических исследованиях · Дополнительная квалификация по радиологии (2019) и УЗИ-диагностике (2024) · Врачебное разрешение на работу в земле Северный Рейн-Вестфалия.',
          experience: [
            'Обучение в Иркутском государственном медицинском университете (диплом с отличием, 2009–2015)',
            'Интернатура и работа врачом-хирургом Иркутского регионального клинического госпиталя (2015–2017)',
            'Руководитель проектов клинических исследований, АО «Фармасинтез» (2017–2020)',
            'Клиническая ординатура и работа врачом-рентгенологом (КТ/рентген-диагностика), ГКБ № 1 Иркутска (2019–2022)',
            'Дополнительная квалификация: Радиология (2019) и Ультразвуковая диагностика (2024)',
            'Медицинский перевод и специализированная терминология (2022–2024)',
            'Интеграция в систему здравоохранения Германии, сертификат FSP Medizin C1 & Berufserlaubnis NRW (2025)',
            'Врач-ассистент клиники нейрохирургии в Мёнхенгладбахе'
          ],
          focus: [
            'Лучевая диагностика (КТ, МРТ, рентген, УЗИ)',
            'Нейрохирургическое ведение и динамический контроль пациентов',
            'Консервативное лечение патологий позвоночника',
            'Междисциплинарное взаимодействие',
            'Многоязычный прием (русский, немецкий, английский, французский, таджикский, турецкий)'
          ]
        }
      }
    },
    tr: {
      labels: {
        qual: 'Uzmanlık & Akademik Unvan',
        exp: 'Mesleki Deneyim & Kariyer',
        focus: 'Klinik Odak Alanları & Nitelikler',
        close: 'Kapat'
      },
      doctors: {
        fischer: {
          name: 'Dr. med. Kasim Fischer-Rahimov',
          img: 'img/surgeon1.webp',
          role: 'Beyin ve Sinir Cerrahisi Uzmanı · Klinik Kurucusu',
          degree: 'Tıp Doktoru (Dr. med.) · Tıbbi Eğitmen',
          qual: 'Beyin ve Sinir Cerrahisi Uzmanı (2006) · Omurga cerrahisinde sertifikalı uzmanlık · Ek Nitelikler: Özel Ağrı Tedavisi (2015), Psikosomatik Tedavi (2015), Akupunktur · Anlaşmalı Klinik Hekimi ve Uzmanlık Eğiticisi.',
          experience: [
            'İrkutsk Devlet Tıp Üniversitesi ve Devlet Hekim Geliştirme Enstitüsü Tıp Eğitimi (1992–2000)',
            'Jena Üniversite Hastanesi ve Klinikum Meiningen GmbH Nöroşirürji Uzmanlık Eğitimi (2003–2008)',
            'Beyin ve Sinir Cerrahisi Uzmanı (2006)',
            'Köln Merheim Nöroşirürji Kıdemli Hekimi (2009)',
            'MHO Osnabrück Baş Kıdemli Hekimi (2011)',
            'Mikronöroşirürji mbH Gensingen Başhekimi (2013)',
            'Özel Ağrı Tedavisi ve Psikosomatik Tedavi Ek Uzmanlıkları (2015)',
            'Mönchengladbach Kendi Nöroşirürji Muayenehanesini Kurdu (2015)',
            'Doktora tezi (Dr. med.): Sakroiliak eklem füzyonunda minimal invaziv yöntemlerin karşılaştırılması (2023)'
          ],
          focus: [
            'Minimal invaziv omurga cerrahisi',
            'Mikrocerrahi dekompresyon',
            'Disk protezi uygulamaları (boyun ve bel)',
            'Özel ağrı tedavisi',
            'Sakroiliak eklem ve faset denervasyonu',
            'Psikosomatik temel bakım'
          ]
        },
        hristov: {
          name: 'Dr. med. Tanyo B. Hristov',
          img: 'img/team_tanyo.webp',
          role: 'Beyin ve Sinir Cerrahisi Uzmanı · Şube Yöneticisi',
          degree: 'Tıp Doktoru (Dr. med., magna cum laude) · Nöroşirürji Uzmanı',
          qual: 'Beyin ve Sinir Cerrahisi Uzmanı (Kuzey Ren Tabipler Odası, 2016) · DWG Omurga Cerrahisi Temel Sertifikası (2017) · Radyasyondan Korunma ve Floroskopi Uzmanlığı (2020) · Fonksiyonel Tıp Terapisti (2026).',
          experience: [
            'Köln Üniversitesi Tıp Fakültesi Eğitimi (2003–2009), Hekimlik Yetkisi / Approbation (2010)',
            'Köln Üniversitesi Anatomi Enstitüsü Tıp Doktorası / Dr. med. (magna cum laude derecesiyle, 2010)',
            'Witten-Herdecke Üniversitesi Köln-Merheim Nöroşirürji Kliniği Asistan Hekimi (2010–2016)',
            'Prof. D. Debatisse ile Nörofizyoloji Mentorluğu, CHUV Lozan (2010–2011)',
            'Nöroşirürji Uzmanlık Belgesi, Kuzey Ren Tabipler Odası (2016)',
            'Rhein-Maas-Klinikum Würselen Omurga Cerrahisi ve Nöroşirürji Kıdemli Hekimi (DWG Level I Klinik, 2018)',
            'LVR Viersen Ortopedi Kliniği Omurga Cerrahisi Bölüm Başkanı (2018–2023)',
            'Clinic Bel Etage Düsseldorf Nöroşirürji Operatör Hekimi (2023–2025)',
            'Köln Özel Nöroşirürji Muayenehanesi / HRISTOV medical Kurucusu (2024\'ten beri)',
            'Mönchengladbach Nöroşirürji Kliniği Şube Yöneticisi ve Kıdemli Uzmanı'
          ],
          focus: [
            'Boyun ve bel fıtıklarında disk protezi cerrahisi',
            'Omurganın dejeneratif disk hastalıkları',
            'Karmaşık ve enstrümante revizyon cerrahisi',
            'Minimal invaziv cerrahi yaklaşımlar (PLIF, MIS TLIF, ALIF, OLIF, XLIF)',
            'Dejeneratif ve travmatik deformiteler',
            'Kronik ağrı tedavisi (Omurilik Stimülasyonu - SCS)',
            'Sakroiliak eklem füzyonu ve pelvik stabilizasyon'
          ]
        },
        pirmoradi: {
          name: 'Habib Pirmoradi',
          img: 'img/team_habib.webp',
          role: 'Nöroşirürji Asistanı (AiW) · Beyin ve Sinir Cerrahisi Uzmanı',
          degree: 'Almanya Onaylı Hekim · Nöroşirürji Uzmanı',
          qual: 'Almanya resmi hekimlik lisansı (Münster Approbation) · Beyin ve Sinir Cerrahisi Uzmanı (İsfahan Üniversitesi, 2016) · 800\'ün üzerinde başarılı ameliyat tecrübesi (tümör ve omurga cerrahisi) · Kuzey Ren Tabipler Odası Tıbbi Dil Sınavı başarısı.',
          experience: [
            'Najafabad Üniversitesi Tıp Fakültesi Eğitimi, İsfahan (1996–2003)',
            'İsfahan Üniversitesi Nöroşirürji Uzmanlık Eğitimi, dönemin ilk %10\'luk derecesi (2012–2017)',
            'Beyin ve Sinir Cerrahisi Uzmanlığı (2016)',
            'Kowsar Hastanesi Nöroşirürji Uzman Hekimi, Sanandaj (800\'den fazla başarılı cerrahi, 2016–2022)',
            'Milad Hastanesi Nöroşirürji Uzmanlığı, İsfahan (kompleks tümör ve omurga cerrahisi yönetimi, 2023–2024)',
            'Almanya Tıbbi Dil Sınavı ve Çalışma İzni (2025)',
            'Elisabeth Hastanesi Recklinghausen Nöroloji ve Geriatri Kliniği Hekimliği (2025)',
            'Almanya Resmi Tıp Denkliği / Approbation (Münster, 2026)',
            'Mönchengladbach Nöroşirürji Kliniğinde Uzmanlık Eğitimi Alan Hekim'
          ],
          focus: [
            'Mikrocerrahi',
            'Omurga ve fıtık cerrahisi',
            'Spinal kanal darlığı dekompresyonu',
            'Enstrümante omurga cerrahisi',
            'Beyin ve omurilik tümörleri',
            'Kafatası cerrahisi ve acil nöroşirürji'
          ]
        },
        khabibullin: {
          name: 'Timur Khabibullin',
          img: 'img/team_timur.webp',
          role: 'Asistan Hekim · Nöroşirürji',
          degree: 'Hekim (Üstün Başarı Diploması) · Tıbbi Dil C1 Sertifikası',
          qual: 'Radyoloji, cerrahi ve klinik araştırmalarda klinik deneyimli hekim · Radyoloji (2019) ve Ultrasonografi (2024) ek uzmanlıkları · Kuzey Ren-Vestfalya çalışma izni.',
          experience: [
            'İrkutsk Devlet Tıp Üniversitesi Tıp Eğitimi (Üstün Başarı Diploması, 2009–2015)',
            'İrkutsk Bölge Klinik Hastanesi Cerrahi Uzmanlık Eğitimi ve Asistan Hekimliği (2015–2017)',
            'Pharmasyntez A.Ş. Klinik Araştırmalar Proje Yöneticisi (2017–2020)',
            'İrkutsk 1 Nolu Şehir Klinik Hastanesi Radyoloji Asistanlığı ve Hekimliği (Röntgen / BT, 2019–2022)',
            'Radyoloji (2019) ve Ultrason Tanı (2024) Mesleki Ek Uzmanlık Sertifikaları',
            'Tıbbi çeviri ve çok dilli hasta iletişimi (2022–2024)',
            'Alman sağlık sistemi entegrasyonu, FSP Medizin C1 & NRW Çalışma İzni (2025)',
            'Mönchengladbach Nöroşirürji Kliniği Asistan Hekimi'
          ],
          focus: [
            'Görüntüleme tanı yöntemleri (BT, MR, Röntgen, Ultrason)',
            'Nöroşirürji hasta takibi ve klinik kontroller',
            'Konservatif ve girişimsel omurga tedavileri',
            'Disiplinler arası tedavi koordinasyonu',
            'Çok dilli hasta hizmeti (Almanca, Rusça, İngilizce, Fransızca, Tacikçe, Türkçe)'
          ]
        }
      }
    },
    ar: {
      labels: {
        qual: 'التخصص والدرجة الأكاديمية',
        exp: 'الخبرة المهنية والمسار الوظيفي',
        focus: 'مجالات التركيز السريري والمؤهلات',
        close: 'إغلاق'
      },
      doctors: {
        fischer: {
          name: 'د. م. قاسم فيشر-رحيموف',
          img: 'img/surgeon1.webp',
          role: 'أخصائي جراحة الأعصاب · مؤسس العيادة',
          degree: 'دكتوراه في الطب (Dr. med.) · مشرف تدريب طبي',
          qual: 'أخصائي جراحة الأعصاب (2006) · خبرة معتمدة في جراحة العمود الفقري · مؤهلات إضافية: علاج الألم المتخصص (2015)، علاج نفسي جسمي (2015)، وخز بالإبر · طبيب تعاقدي معتمد ومشرف تدريب معتمد للأطباء.',
          experience: [
            'دراسة الطب البشري في جامعة إيركوتسك الطبية ومعهد الدراسات الطبية العليا (1992–2000)',
            'التدريب التخصصي في جراحة الأعصاب في مستشفى جامعة ينا ومستشفى ماينينغن (2003–2008)',
            'طبيب مختص في جراحة المخ والأعصاب (2006)',
            'طبيب أول لجراحة الأعصاب في كولونيا ميرهايم (2009)',
            'طبيب أول رئيسي لجراحة الأعصاب، MHO أوسنابروك (2011)',
            'رئيس أطباء جراحة الأعصاب المجهرية في غينسنغن (2013)',
            'تخصصات إضافية في علاج الألم العصبي المتخصص والعلاج النفسي الجسدي (2015)',
            'تأسيس عيادة جراحة الأعصاب الخاصة في مونشنغلادباخ (2015)',
            'أطروحة الدكتوراه: مقارنة الإجراءات الجراحية طفيفة التوغل لدمج المفصل العجزي الحرقفي (2023)'
          ],
          focus: [
            'جراحة العمود الفقري طفيفة التوغل',
            'تخفيف الضغط المجهري على الأعصاب',
            'استبدال الأقراص الغضروفية الصناعية (العنقية والقطنية)',
            'علاج الألم العصبي المتخصص',
            'تثبيت المفصل العجزي ومفاصل الفقرات',
            'الرعاية الطبية النفسية الجسدية'
          ]
        },
        hristov: {
          name: 'د. م. تانيو ب. هريستوف',
          img: 'img/team_tanyo.webp',
          role: 'أخصائي جراحة الأعصاب · مدير الفرع (Standortleiter)',
          degree: 'دكتوراه في الطب (Dr. med.، مرتبة الشرف العليا magna cum laude)',
          qual: 'أخصائي جراحة الأعصاب (نقابة أطباء شمال الراين، 2016) · الشهادة الأساسية في جراحة العمود الفقري من الجمعية الألمانية للعمود الفقري DWG (2017) · الوقاية من الإشعاع والتنظير التألقي (2020) · معالج معتمد للطب الوظيفي (2026).',
          experience: [
            'دراسة الطب البشري في جامعة كولونيا (2003–2009)، ترخيص مزاولة الطب الألماني (Approbation 2010)',
            'نيل درجة الدكتوراه في الطب (Dr. med.) من معهد التشريح بمستشفى جامعة كولونيا (بمرتبة magna cum laude، 2010)',
            'طبيب مقيم في عيادة جراحة الأعصاب بمستشفى كولونيا-ميرهايم، جامعة فيتن-هيرديكه (2010–2016)',
            'برنامج الإشراف في الفسيولوجيا العصبية مع البروفيسور د. ديباتيس، CHUV لوزان (2010–2011)',
            'شهادة الاختصاص في جراحة الأعصاب، نقابة أطباء شمال الراين (2016)',
            'طبيب أول لجراحة العمود الفقري وجراحة الأعصاب، مستشفى راين-ماس فيرزلن (مستشفى المستوى الأول DWG، 2018)',
            'رئيس قسم جراحة العمود الفقري في عيادة LVR لجراحة العظام في فيرزن (2018–2023)',
            'استشاري جراحة الأعصاب في عيادة Clinic Bel Etage بدوسلدورف (2023–2025)',
            'عيادة خاصة لجراحة الأعصاب في كولونيا / مؤسس HRISTOV medical (منذ 2024)',
            'مدير الفرع وكبير أخصائيي جراحة الأعصاب في مونشنغلادباخ'
          ],
          focus: [
            'استبدال الأقراص الغضروفية الصناعية للفقرات العنقية والقطنية',
            'تنكس الأقراص الغضروفية في جميع فقرات العمود الفقري',
            'الجراحات الترميمية المعقدة وإعادة العمليات الجراحية',
            'التقنيات طفيفة التوغل (PLIF, MIS TLIF, ALIF, OLIF, XLIF)',
            'تشوهات وعدم استقرار العمود الفقري التنكسية والرضية',
            'متلازمات الألم المزمن (تحفيز الحبل الشوكي - SCS)',
            'تثبيت المفصل العجزي الحرقفي واستقرار الحوض'
          ]
        },
        pirmoradi: {
          name: 'السيد حبيب بيرموراذي',
          img: 'img/team_habib.webp',
          role: 'طبيب مقيم جراحة الأعصاب (AiW) · أخصائي جراحة الأعصاب',
          degree: 'طبيب مرخص في ألمانيا · أخصائي جراحة المخ والأعصاب',
          qual: 'طبيب مرخص معتمد في ألمانيا (ترخيص مونستر Approbation) · أخصائي في جراحة المخ والأعصاب (جامعة أصفهان، 2016) مع سنوات عديدة من الممارسة الجراحية التخصصية · أكثر من 800 عملية جراحية عصبية ناجحة (جراحة الأورام، العمود الفقري، الجراحة المجهرية) · اجتياز اختبار اللغة الطبية التخصصية بنقابة أطباء شمال الراين.',
          experience: [
            'دراسة الطب البشري في جامعة نجف آباد، أصفهان (1996–2003)',
            'التدريب التخصصي والإقامة في جراحة الأعصاب بجامعة أصفهان، التخرج ضمن أفضل 10% (2012–2017)',
            'أخصائي جراحة المخ والأعصاب (2016)',
            'أخصائي جراحة الأعصاب بمستشفى كوثر، سنندج (أكثر من 800 عملية جراحية ناجحة، 2016–2022)',
            'استشاري جراحة الأعصاب بمستشفى ميلاد، أصفهان (إدارة جراحات الأورام والعمود الفقري المعقدة، 2023–2024)',
            'اجتياز امتحان اللغة الطبية وتصريح مزاولة المهنة في ألمانيا (2025)',
            'طبيب في قسم الأعصاب وطب الشيخوخة بمستشفى إليزابيث ريكلينغهاوزن (2025)',
            'ترخيص مزاولة المهنة الطبي الكامل في ألمانيا (مونستر، 2026)',
            'طبيب مقيم في جراحة الأعصاب في عيادة جراحة الأعصاب بمونشنغلادباخ'
          ],
          focus: [
            'الجراحة المجهرية الدقيقة',
            'جراحة العمود الفقري والانزلاق الغضروفي',
            'توسيع القناة الشوكية وتخفيف الضغط العصبي',
            'عمليات تثبيت واستقرار العمود الفقري',
            'أورام الدماغ والحبل الشوكي',
            'جراحة الجمجمة ورعاية الطوارئ'
          ]
        },
        khabibullin: {
          name: 'السيد تيمور خابيبولين',
          img: 'img/team_timur.webp',
          role: 'طبيب مساعد في جراحة الأعصاب',
          degree: 'طبيب مرخص (دبلوم مع مرتبة الشرف) · شهادة اللغة الطبية C1',
          qual: 'طبيب ذو خبرة سريرية في الأشعة والجراحة والتجارب السريرية · مؤهلات إضافية في الأشعة (2019) والموجات فوق الصوتية (2024) · تصريح مزاولة المهنة في ولاية شمال الراين-وستفاليا.',
          experience: [
            'دراسة الطب البشري في جامعة إيركوتسك الطبية الحكومية (دبلوم مع مرتبة الشرف، 2009–2015)',
            'طبيب مقيم في الجراحة بمستشفى إيركوتسك الإقليمي السريري (جراحة عامة، أوعية، طوارئ، 2015–2017)',
            'مدير مشاريع التجارب السريرية بشركة "فارما سينتيز" (2017–2020)',
            'ممارسة وتدريب في قسم الأشعة (فحوصات الأشعة المقطعية والسينية) بمستشفى إيركوتسك رقم 1 (2019–2022)',
            'تخصصات مهنية إضافية في الأشعة التشخيصية (2019) والموجات فوق الصوتية (2024)',
            'الترجمة الطبية والتواصل التخصصي متعدد اللغات (2022–2024)',
            'الاندماج في النظام الصحي الألماني، واجتياز امتحان FSP Medizin C1 وتصريح NRW (2025)',
            'طبيب مساعد في عيادة جراحة الأعصاب بمونشنغلادباخ'
          ],
          focus: [
            'التشخيص بالأشعة التصويرية (الأشعة المقطعية، الرنين المغناطيسي، السينية، السونار)',
            'المتابعة السريرية ورعاية مرضى جراحة الأعصاب والعمود الفقري',
            'العلاجات التحفظية والتداخلية للعمود الفقري',
            'التعاون والتنسيق الطبي متعدد التخصصات',
            'رعاية متعددة اللغات (الألمانية، الروسية، الإنجليزية، الفرنسية، الطاجيكية، التركية)'
          ]
        }
      }
    }
  };

  // Detect current language from html tag or path
  function getLang() {
    const htmlLang = document.documentElement.lang ? document.documentElement.lang.toLowerCase() : '';
    if (htmlLang.startsWith('en')) return 'en';
    if (htmlLang.startsWith('ru')) return 'ru';
    if (htmlLang.startsWith('tr')) return 'tr';
    if (htmlLang.startsWith('ar')) return 'ar';
    const path = window.location.pathname;
    if (path.includes('/en/')) return 'en';
    if (path.includes('/ru/')) return 'ru';
    if (path.includes('/tr/')) return 'tr';
    if (path.includes('/ar/')) return 'ar';
    return 'de';
  }

  window.openDoctorBio = function(docId) {
    const lang = getLang();
    const langData = doctorsData[lang] || doctorsData.de;
    const doc = langData.doctors[docId] || doctorsData.de.doctors[docId];
    if (!doc) return;

    const modal = document.getElementById('doctor-bio-modal');
    if (!modal) return;

    // Relative image path fix if inside subfolder
    const isSubfolder = window.location.pathname.includes('/en/') ||
                        window.location.pathname.includes('/ru/') ||
                        window.location.pathname.includes('/tr/') ||
                        window.location.pathname.includes('/ar/');
    const imgPrefix = isSubfolder ? '../' : '';

    // Update labels
    document.getElementById('doc-modal-lbl-qual').textContent = langData.labels.qual;
    document.getElementById('doc-modal-lbl-exp').textContent = langData.labels.exp;
    document.getElementById('doc-modal-lbl-focus').textContent = langData.labels.focus;
    document.getElementById('doc-modal-btn-close').textContent = langData.labels.close;

    // Populate doc details
    const imgEl = document.getElementById('doctor-modal-img');
    imgEl.src = imgPrefix + doc.img;
    imgEl.alt = doc.name;

    document.getElementById('doctor-modal-name').textContent = doc.name;
    document.getElementById('doctor-modal-role').textContent = doc.role;
    document.getElementById('doctor-modal-degree').textContent = doc.degree;
    document.getElementById('doctor-modal-qualifications').textContent = doc.qual;

    // Experience list
    const expList = document.getElementById('doctor-modal-experience');
    expList.innerHTML = '';
    doc.experience.forEach(function(item) {
      const li = document.createElement('li');
      li.textContent = item;
      expList.appendChild(li);
    });

    // Focus tags
    const focusContainer = document.getElementById('doctor-modal-focus');
    focusContainer.innerHTML = '';
    doc.focus.forEach(function(tag) {
      const span = document.createElement('span');
      span.className = 'doc-bio-tag';
      span.textContent = tag;
      focusContainer.appendChild(span);
    });

    // Show modal
    modal.classList.add('active');
    modal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  };

  window.closeDoctorBio = function() {
    const modal = document.getElementById('doctor-bio-modal');
    if (!modal) return;
    modal.classList.remove('active');
    modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  };

  // Close on Escape key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' || e.key === 'Esc') {
      window.closeDoctorBio();
    }
  });

  // Keyboard accessibility for doctor cards
  document.addEventListener('keydown', function(e) {
    if (e.target && e.target.classList && e.target.classList.contains('doctor-card-interactive')) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        e.target.click();
      }
    }
  });
})();

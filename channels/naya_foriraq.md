<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/cQFBfWzxi_twoemKTIE28fsIA2wlv5jDAbKq0NRGE7_mtpJrHCu2NuczNbSxN3NF57D539HIPWLzjJrDQQv5NHDgq44p2MipeLLiZfOUd5ruQP-t-HpytOZ1VQaHXeDpcPsuAZc7uDIF4LPM6W06m7-tCbL1ReqGQVGmb0tmhj9Nsw6B7eTjm34b5CuN2zF66l9cHWo_NB-7e2aVFI2ep8pAt_sta4_82FNr-tLlj7IP8Ea0r4K9ghSGtMbmiCe829MUJVXBt5LizRVmVM0CZkdKSHo8CNH3-_-k7bnyrzJROKg9oi5adtiOf4wF2WlxJ7QsBa9SDRs_htNwy_gnFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 265K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 09:36:27</div>
<hr>

<div class="tg-post" id="msg-92467">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇷
رئيس البرلمان الإيراني محمدباقر قاليباف:
الأمريكيون، الذين يتحدثون شيئًا مختلفًا في وسائل الإعلام، قد طرحوا مؤخرًا مقترحات من خلال وسيط. ولكن يجب أن يدركوا أن عصر إضاعة الوقت وإملاء المطالب من جانب واحد قد انتهى. وموقف الجمهورية الإسلامية الإيرانية واضح وثابت تمامًا. ولن يتم فتح مضيق هرمز إلا عندما يتم تحقيق الشروط السبعة التي وضعناها استنادًا إلى اتفاقية إسلام آباد.
بناءً على استراتيجية القوة والعقلانية، نحن لا ننفعِل ولا نُرهَب. نحن نقاتل ونتفاوض في الوقت نفسه. نحن موجودون بكل قوتنا في ساحة المعركة العسكرية وسنواجههم بمفاجآت جديدة، وفي الوقت نفسه، نستخدم أدوات الدبلوماسية لترسيخ تفوقنا في الساحة العسكرية وفرض حقوق الشعب الإيراني. لقد ذكرت مرارًا وتكرارًا أن الفائز في ساحة التفاوض هو من أعد نفسه للحرب.</div>
<div class="tg-footer">👁️ 66 · <a href="https://t.me/naya_foriraq/92467" target="_blank">📅 09:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92466">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇶
🇮🇷
هزة أرضية بقوة 3.6 ريختر تضرب الحدود الشمالية بين العراق وإيران.</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/naya_foriraq/92466" target="_blank">📅 09:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92465">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zy2oJdp_xa36MD4yjLbdSKiM8CS34PAZd_PoFBNHCu8-2LjjTwfabb2U96k-lApsUZ-kJLTO0o2upINflh-bKjXSG1T-vxUiD2bheS2-Z4PN05MrjwZZR5pJPE1pfZ4ytdIiqWmuuaQJU_FnFsjxG2MIQmM563iooLJ1TYr0q_186Z0KfaqHW56nMqYVu_DY_fyJbg9irZnMEOn1j0cwiWWW4sDsSwPbDSAcaTab2oh-GGFPIGsm-qebmo_RFztIlnId2HmATIsZH4VbSUxoLPrDtB8dmBwwDy_8DY6cV9DBOZma6SnGpadYSuZr8D75KZycHkWL7Vcf5VOrJfVl7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوة امنية تعتقل عدد من ناشطي المجتمع المدني العراقي   الاعتقال تم بناء على سحق العلمين الامريكي والصهيوني خلال احتفالية يوم السيادة في بغداد !</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/92465" target="_blank">📅 03:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92464">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">قوة امنية تعتقل عدد من ناشطي المجتمع المدني العراقي
الاعتقال تم بناء على سحق العلمين الامريكي والصهيوني خلال احتفالية يوم السيادة في بغداد !</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/92464" target="_blank">📅 02:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92463">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">▫️
‏الكويت تقرر سحب الجنسية الكويتية من 415 شخصاً وممن اكتسبها معهم عن طريق التبعية
عيل منو بقى بالكويت</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/92463" target="_blank">📅 01:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92462">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQwDGbdw7UAyZVx6DkfU2zTO9bWw9GG1Ow9XOOxP2mfjDPqSDH2z7EybJwkOhygvSJIRvUWq-3qEeUGytk2SciEMgn7nBTfPSI0nE3HahCs471uT0o7XdAWQkIKTEI6P_nTppmmiRSjqrIZy_u-FzeeSBzOF2hUNMmSeDET6ULyzeLdKenWCv4pD4kPrUgqkGsKE5I2fckBgBD747gN8WfZyiiUghgDl222OBSTxoRJfsODWB2GJYsEfPAsn_RSBm1z1_OQmLKrn51p6O7j8iqSLTtr_dCs8Bp3AvSDenqfZ4oVuV8krpJRrVQuekQZ9jgmVt3h2enaOONcpeHkAdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الرد اليمني وصل،هجوم صاروخي عكسي من اليمن يستهدف السعودية في ينبع واصابة عدد من  المواقع النفطية</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/92462" target="_blank">📅 01:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92461">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnKAoEklZ2PyXaFXxNUwv7PEwIU96oNa8VOJLQnBAo1wopxoAJ2fRYTe-McwLciaGHxcPPAraXFKMkRb5Wn9vSX1JTUKDo3f8Fi0dwC-uHM-yIqePcxGKvD8Xf2QT7aWGGmfe8bU3qpy3UfNpBC9h-JO9EGLT2jDYtXFhMaZEFlwJbnSpe5hxYxaJXIX9LyXE9EBg3CM-Il8Kw9M0_BJwyqTMqY1RVZO8giX3KHwQCx2dRCQpREVSv8zQmuZpQnwBEd4WoWNJqZ3kgziP2PkqagDZLbw-dwnGlVNno-QdKJ3dtmwQvcksS0S3LZS0404wJckA93mI0wMuLja6vTttw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القوات اليمنية المسلحة تستهدف الدمام شرق السعودية</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/92461" target="_blank">📅 01:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92460">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">القوات اليمنية المسلحة تستهدف الدمام شرق السعودية</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/92460" target="_blank">📅 01:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92459">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HP9-7RMjFgiQS18uJRlVFZ72ZwDMcC7FatSrTnVBqQ4j0XltGgcpoYXjATzvjz_vQ-oplAFSYSJE4eJY3Q4GLwlSaDDaAU2LxDlso8WzTH_7wQN8HjNsV_ZgJbwj4QbNoTRlDi15PhcytLoAVvjUBD3XzmewApTcJmX0rDt4pw6nUYL31QR48uJectWyOpmDam8J5sf63zHDh7dgWzxoRxUf2Dj3hsfecvaLDx-Xaoxmu8Xj-mcTFnG6NmRxiJbT6CGWvo6-uovM6KuLrvgPLcYDtVBaUCMhYcarupXjtSu23D4yRtyYze-jjLjR2pgQt3rmt-VpUJAYpvd4n5skyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
تداول ناشطون على مواقع التواصل الاجتماعي وثيقة تشير بمؤشرات امنية خطرة تخص والد مرشح حقيبة وزارة التخطيط و تؤكد انتماء الأخير لعصابات داعش الارهابية</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/92459" target="_blank">📅 00:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92458">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇸🇦
🇾🇪
غارات سعودية تستهدف محافظة عمران والعاصمة صنعاء</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/92458" target="_blank">📅 00:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92457">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab78e7a2b6.mp4?token=lDNanNd18TVyHx_cccRYzEqU_V4jjuOjWfjs9YNOuiBkRIps-YAMhNN0mqswig79Qi94hm-1aSTASjyRaPz2trOrTFwbBBdZVVNwYRkDzvpHnxrrsyQzJLN-K5sfi-3CgzSrz1Xj7io3l1GG2pewej1xJyyv82phZQDHI3PtwAtXWoRDKqxfEQ5npaBlQT7AmhBEUrwPxb_74V4dzvK2B4Ynl5Ar3wbqj3_e5Q2cpvl-FlJg0ER3KYQp9bU3_-zHiq8_FqQQxWmPAV6ag4RZYTFEEUxLg5gHzLEch-2jlA2o_OjzJkbtQQmobTqb-muUk6NN_6KtUcRR6zRrljn-yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab78e7a2b6.mp4?token=lDNanNd18TVyHx_cccRYzEqU_V4jjuOjWfjs9YNOuiBkRIps-YAMhNN0mqswig79Qi94hm-1aSTASjyRaPz2trOrTFwbBBdZVVNwYRkDzvpHnxrrsyQzJLN-K5sfi-3CgzSrz1Xj7io3l1GG2pewej1xJyyv82phZQDHI3PtwAtXWoRDKqxfEQ5npaBlQT7AmhBEUrwPxb_74V4dzvK2B4Ynl5Ar3wbqj3_e5Q2cpvl-FlJg0ER3KYQp9bU3_-zHiq8_FqQQxWmPAV6ag4RZYTFEEUxLg5gHzLEch-2jlA2o_OjzJkbtQQmobTqb-muUk6NN_6KtUcRR6zRrljn-yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: لدي قرار سأتخذه بشأن إيران. وسنتخذه بالطريقة السهلة أو الصعبة.
‏-لا يمكن لإيران أن تمتلك سلاحاً نووياً. بالمناسبة، كما تعلمون، تخلت إيران فعلياً عن أي خطط لامتلاك سلاح نووي.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/92457" target="_blank">📅 00:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92456">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇷🇺
🔻
خوفا من مسيرات روسيا
‏تقوم ولاية مكلنبورغ-فوربومرن الألمانية ببناء شبكة للكشف عن الطائرات بدون طيار على طول ساحل بحر البلطيق بأكمله، حيث من المقرر أن توفر مئات أجهزة الاستشعار السلبية بيانات في الوقت الفعلي للسلطات بحلول الربيع</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/92456" target="_blank">📅 00:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92455">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإعلام الحربي</strong></div>
<div class="tg-text">🔴
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/92455" target="_blank">📅 23:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92454">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇾🇪
بيان القوات المسلحة اليمنية بشأن تنفيذ عملية عسكرية نوعية استهدفت شركة أرامكو في عاصمة العدو السعودي الرياض وأدت إلى اشتعال النيران في المواقع المستهدفة   بيانٌ صادرٌ عن القواتِ المسلحةِ اليمنيةِ  بسمِ اللهِ الرحمنِ الرحيمِ قالَ تعالى: {فَمَنِ اعْتَدَى عَلَيْكُمْ…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/92454" target="_blank">📅 23:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92453">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇸🇦
تعليق الدراسة غداً الأحد في جيزان خوفا من هجمات القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/92453" target="_blank">📅 23:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92452">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇺🇸
🇮🇷
الاعلام الاميركي:
طرد دبلوماسيين إيرانيين من الولايات المتحدة بعد تجاهلهما أمر المغادرة.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/92452" target="_blank">📅 23:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92451">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjfoaLyUpULWISLPElz4N1kErVkR4q2YVmqhczat46cUpxnakOycvhO37g8OBDBpnWivvL9oGZ7g93eetME3xoA--rsEb67_DcKPHbf6XohcBtWD70ZWIX1_LcMsfg_pCoRPjBufhKKavBLWWIrKtRv_BGaZWimEUFiCfewdt_qdT3SlgynysTG6l2dunUXcax-VRu_0jr04izHBwJjvi_uCIzz4UyFWtrxPii3UcRPHF3V-GyybtKvQ1tFV_LcFjU1AKF69TiE7jNenbXfQY_Ar30_7o11ImbTUCE5ghVhj4R8JR74F9oOdRC6RWNjFsYU-QERqT8S7-h8cbeduKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الرئيس الايراني: ‏
اتخذت الحكومة نهجاً جديداً في إدارة هذه الظروف الاستثنائية. تمثلت خطة العدو في الأشهر الأخيرة في قطع شرايين البلاد الحيوية بهدف الضغط على الشعب الإيراني الكريم. وقد ازداد الضغط الاقتصادي، ولكن بفضل الله، وبدعم من الشعب، وبجهود زملائنا في الحكومة، لم نسمح للعدو بتحقيق أهدافه في الحرب الاقتصادية.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/92451" target="_blank">📅 22:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92449">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇾🇪
بيان القوات المسلحة اليمنية بشأن تنفيذ عملية عسكرية نوعية استهدفت شركة أرامكو في عاصمة العدو السعودي الرياض وأدت إلى اشتعال النيران في المواقع المستهدفة
بيانٌ صادرٌ عن القواتِ المسلحةِ اليمنيةِ
بسمِ اللهِ الرحمنِ الرحيمِ
قالَ تعالى: {فَمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ} صدقَ اللهُ العظيم
في إطارِ الردِّ على العدوانِ السعوديِّ على العاصمةِ صنعاءَ والمحافظاتِ الحرةِ والتي بلغت خلال 24 ساعة الماضية 60 غارة جوية وصاروخ ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد على بلدِنا 1410 غارة وصاروخ
نفذتِ القواتُ المسلحةُ اليمنيةُ عمليةً عسكريةً نوعيةً وذلك بعددٍ من الصواريخِ الباليستيةِ والطائراتِ المسيرةِ استهدفت شركةَ أرامكو في عاصمةِ العدوِّ السعوديِّ الرياضِ.
​وحققتِ العمليةُ هدفَها بنجاحٍ بفضلِ اللهِ
وكانتِ الإصاباتُ دقيقةً ومباشرةً وأدت إلى اشتعالِ النيرانِ في المواقعِ المستهدفةِ.
​إنَّ سفكَ دماءِ اليمنيينَ بهذا الإجرامِ وبهذه الوحشيةِ يُحَتِّمُ على القواتِ المسلحةِ ومعها كلُّ أحرارِ شعبِنا ضرورةَ اتخاذِ ما يلزمُ من خطواتٍ تصعيديةٍ وإجراءاتٍ رادعةٍ تؤكدُ للجميعِ أنَّ ثمنَ الاستهتارِ بدماءِ شعبِنا المؤمنِ سيكونُ كبيرًا وباهظًا وليدركَ العدوُّ المجرمُ أنَّ الاستمرارَ في سفكِ دماءِ شعبِنا سيكلفُه الكثيرَ.
مستمرونَ في فرضِ معادلةِ الحصارِ بالحصارِ والتصعيدِ بالتصعيدِ واستهدافِ التحشيداتِ التابعةِ للعدوِّ السعوديِّ حتى وقفِ العدوانِ وإنهاءِ الحصارِ عن بلدِنا العزيزِ
واللهُ حسبُنا ونعمَ الوكيلُ، نعمَ المولى ونعمَ النصيرُ.
عاشَ اليمنُ حراً عزيزاً مستقلاً،
والنصرُ لليمنِ ولكلِّ أحرارِ الأمةِ.
صنعاءُ، 22 ربيع الثاني 1448هـ
الموافقُ 3 أكتوبر 2026م.
صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/92449" target="_blank">📅 22:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92448">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇶
شركة ناقلات النفط العراقية:
تنفيذ عملية نقل مليوني برميل من النفط الخام العراقي بواسطة ناقلة عملاقة من نوع (VLCC) إلى خارج مضيق هرمز.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/92448" target="_blank">📅 22:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92447">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-text">🇮🇶
🇬🇧
العثور على جثة موظف هندي يعمل في شركة النفط البريطانية BP داخل أحد الفنادق في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/92447" target="_blank">📅 21:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92446">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e7e6594e.mp4?token=ct1fUcd3j8in0q-p5vkhKu-frKysX95n6g3Ct4-1hU7B4t-zU2-imV_PQVOS_GSZ73On7ySgTYfAciy3z2z1DcftOTfXEcrh38kXJ9FARsBXuoOQQ8Or33zJX6JXf0BmYAgn9_68BcuBuoyRdqWwMMYFG8XTMvh2V58ETc8IUlmJGJrxgD_MzYGmKx0FFUlEjH6Y27HgMNUeV4FkYtWpIScq0H-6z1XwAtswOjO1P25PCMXOoNj-_tcXMoyY5HRj7QNDMLX_Iwg6BMEDebmeSXdHIbbmuLUmXbzHGkUOvp0FWp_r553u0Fu5RigxXW_SUOSygersYaL8IEIVhcpMAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e7e6594e.mp4?token=ct1fUcd3j8in0q-p5vkhKu-frKysX95n6g3Ct4-1hU7B4t-zU2-imV_PQVOS_GSZ73On7ySgTYfAciy3z2z1DcftOTfXEcrh38kXJ9FARsBXuoOQQ8Or33zJX6JXf0BmYAgn9_68BcuBuoyRdqWwMMYFG8XTMvh2V58ETc8IUlmJGJrxgD_MzYGmKx0FFUlEjH6Y27HgMNUeV4FkYtWpIScq0H-6z1XwAtswOjO1P25PCMXOoNj-_tcXMoyY5HRj7QNDMLX_Iwg6BMEDebmeSXdHIbbmuLUmXbzHGkUOvp0FWp_r553u0Fu5RigxXW_SUOSygersYaL8IEIVhcpMAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
حريق كبير مجهول في حيفا المحتلة بالكيان الصهيوني.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/92446" target="_blank">📅 21:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92445">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1luZTxZT_jVU-hwUuYrlyS-t73PlEUlY01-vexN2H02BmzLDfUME7TVhggeq0HEPaPb7U2jad0sP4TpdFSzpYCWIxEu_b5LhYpVu9j0uvtMOlME8hKnzpIoGnGlCPfMxEsRfamJhDIrYJKTC0XACeqkFTXCfzZFpvpwK8y0TLbrCaPrpxO6r8vPtTXZZiUH3sWbkHkPx0NgSb5TpdPRv6L6ZJmXBvi9XaAbx4IIv_60d6cJi_tmw8PVtFoNBw9Rwb-_IpVPSexDzNxcV-Avi7jjGiL2E4WcF9Mkcr0A2TFcrUHpiROf5oyOUfmZ3PZaL_eCO048hfA_Si8p3A9H4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رئيس منظمة الطيران المدني الايراني: ستأنف رحلات الطيران بين إيران والعراق اعتبارًا من الغد، وذلك من خلال شركات الطيران الإيرانية والعراقية.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/92445" target="_blank">📅 20:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92444">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇷
رئيس منظمة الطيران المدني الايراني:
ستأنف رحلات الطيران بين إيران والعراق اعتبارًا من الغد، وذلك من خلال شركات الطيران الإيرانية والعراقية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/92444" target="_blank">📅 20:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92443">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 60 غارةً جويةً وصاروخاً استهدف بها الأعيان المدنية في محافظات صنعاء وصعدة وتعز وحجة ومأرب وذلك من خلال طائرات "F-15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف والعدوان الصاروخي من نجران.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد 1410 غارات جوية وصواريخ.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/92443" target="_blank">📅 20:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92442">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇬🇧
وزير دفاع بريطانيا:
سندرس الرد المناسب بعد التوصل لاستنتاجات مؤكدة في ما يتعلق بقاعدة فيرفورد.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/92442" target="_blank">📅 19:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92441">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
انفجار ناقلة نفط ثانية في مضيق هرمز بعد استهدافها بصاروخ من قبل بحرية الحرس ااثوري.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/92441" target="_blank">📅 19:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92440">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇱
مسؤول أمريكي:
إسرائيل حذرت ألمانيا من مخاطر على قواعد أمريكية خاصة قاعدتي سبانغدالم ورامشتاين.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/92440" target="_blank">📅 19:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92439">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇶
رسائل تصل للمواطنين في العراق:
مشتركينا الاعزّاء، نظراً لتوجيهات وزارة الإتصالات، غداَ سيتم قطع خدمة الإنترنت من المصدر مؤقتاً خلال أوقات الإمتحانات الوزارية من الساعة 6:30 صباحاً إلى 7:05 صباحاً، علماً بأن التوجيهات تشمل جميع الشركات المزودة لخدمات الإنترنت.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/92439" target="_blank">📅 18:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92438">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇶
اشتباکات مسلحة في قضاء كلار ضمن محافظة السليمانية شمالي العراق وإصابة عدة اشخاص كحصيلة اولية</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/92438" target="_blank">📅 18:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92437">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f9b9a634d.mp4?token=WFXQ4GStjsWPYAzU_WSYK1bH7QUB4hjXeTIajFpp22JEmQwDfAX-vX86JGQvdilcssUlTn5_fvxwTfm85m9m4PaBLRatxNUzToHyXpXQbXv6YEsa1sVu-3TVPUnKKITF7Z5JDjT4JpOa_YmZf2G7UlvdH2OT3WPb5QKWAQatQtYg9qYTgEewIRWoLGx_H2hht-qvJCuGDsy8nPMFwwq5gGTn8Kr_TRLpVLDrkGDsQBIomjkGx1rdHSGrD_ghSHBoIob2Ke09_3CPqxR57gQB316EL1QXYcCh5GgD0gamlI488G2VPuIHeoQ_e7h1NgTf5cUapT9dDM3rZKE_va2TlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f9b9a634d.mp4?token=WFXQ4GStjsWPYAzU_WSYK1bH7QUB4hjXeTIajFpp22JEmQwDfAX-vX86JGQvdilcssUlTn5_fvxwTfm85m9m4PaBLRatxNUzToHyXpXQbXv6YEsa1sVu-3TVPUnKKITF7Z5JDjT4JpOa_YmZf2G7UlvdH2OT3WPb5QKWAQatQtYg9qYTgEewIRWoLGx_H2hht-qvJCuGDsy8nPMFwwq5gGTn8Kr_TRLpVLDrkGDsQBIomjkGx1rdHSGrD_ghSHBoIob2Ke09_3CPqxR57gQB316EL1QXYcCh5GgD0gamlI488G2VPuIHeoQ_e7h1NgTf5cUapT9dDM3rZKE_va2TlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النظام السعودي يبدأ باخماد الحرائق في الرياض الناجمة عن ضربات القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/92437" target="_blank">📅 18:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92436">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce85fd1ad6.mp4?token=JzYVim7GbmwZ94FjsGFLhKs2MvsqZDU8K8bjd1RkF-YNW0-8VeMVMcz_Og3YigdOwoFnCxS00JTWBAEB-h8YqgLYrF30JJqaCNQw53cbrq76b1hlC-hCqxuFy49Egn9Gh1BmojKIEngpH4XBlGT1RDDYxZTi6atjRUw-kgwNqc_fYxDTBzn-8Y4YX9bKGBPK16kUeos4HLBtic0n-AIkiJ8IgLc2HmBf7GcNZj0DcDSJ05uHwRarI5zfznJIl14LwjwcJ3ez4eFpYLlu_tMDQfXaSM-hAT73YvCzhE_GilrO_nxCpvslMVs46vTlm7Wk5ExJgp3iVIVH4IuR3TyRKWRjsE13XCwVVfJxHBUi3jYzSbTeF0b2lqFXo6EPPXuatWa-Qqyo83LUNyb4W0eluqwqAdewmZZAND4t0EQI7cR9fCFvaC33UWp9ZnJ0J_Sw8YTKIt3HL_oHHNGFG2eHNFdjajqHPBSqih2lmR4j0bEk0j49khKIBNeMYMn4quBNVMmtmrSLTISivPaAi88IqB3Pxp4H82e-r08o7NDstO0hL4w61ajqq4-cD_ddWISd8ftU7Y5yhxtF9A4l8sr7w4DUu4dQU5-j3oKFc8h2WTbh6IN10BVrKtWdqhGmktmcA4L4TQIcQpjRwou1lkLTtBAcKmg7rwpKoPjNnbBknGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce85fd1ad6.mp4?token=JzYVim7GbmwZ94FjsGFLhKs2MvsqZDU8K8bjd1RkF-YNW0-8VeMVMcz_Og3YigdOwoFnCxS00JTWBAEB-h8YqgLYrF30JJqaCNQw53cbrq76b1hlC-hCqxuFy49Egn9Gh1BmojKIEngpH4XBlGT1RDDYxZTi6atjRUw-kgwNqc_fYxDTBzn-8Y4YX9bKGBPK16kUeos4HLBtic0n-AIkiJ8IgLc2HmBf7GcNZj0DcDSJ05uHwRarI5zfznJIl14LwjwcJ3ez4eFpYLlu_tMDQfXaSM-hAT73YvCzhE_GilrO_nxCpvslMVs46vTlm7Wk5ExJgp3iVIVH4IuR3TyRKWRjsE13XCwVVfJxHBUi3jYzSbTeF0b2lqFXo6EPPXuatWa-Qqyo83LUNyb4W0eluqwqAdewmZZAND4t0EQI7cR9fCFvaC33UWp9ZnJ0J_Sw8YTKIt3HL_oHHNGFG2eHNFdjajqHPBSqih2lmR4j0bEk0j49khKIBNeMYMn4quBNVMmtmrSLTISivPaAi88IqB3Pxp4H82e-r08o7NDstO0hL4w61ajqq4-cD_ddWISd8ftU7Y5yhxtF9A4l8sr7w4DUu4dQU5-j3oKFc8h2WTbh6IN10BVrKtWdqhGmktmcA4L4TQIcQpjRwou1lkLTtBAcKmg7rwpKoPjNnbBknGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السحب السوداء تغطي العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/92436" target="_blank">📅 18:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92435">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/564139a66e.mp4?token=srEXxv_KzMmxLrwwrHloLifvm3lEk2V6xdxstGTVeGA9Q3euvoiqzV6qSwAwu-n4mTqnAzCPi-x-yClZ93fs_q0Eepjd7XuuQpaZ6fBeB0TPYBIGT9Jmzu6ldeokG4_lFpIKZylVjPIiayevedTcjGO-YZ4DOJKjAKCZ8Y8TiD9lxjFIrAhY3kaOixJGRdAddVjZcq5U4Z3NmE8vi3g-R4wkR-KZSrZpxjwuR036BvHutxaxg_2crzHAS34XAddB7-GIuOs3Mzp99a_sn0XIarFpzY121naGFYJ7uuTJS38IrVMvrFq7qwLI1GtxLT59bYQtlXnW9qeihGPmyLoEyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/564139a66e.mp4?token=srEXxv_KzMmxLrwwrHloLifvm3lEk2V6xdxstGTVeGA9Q3euvoiqzV6qSwAwu-n4mTqnAzCPi-x-yClZ93fs_q0Eepjd7XuuQpaZ6fBeB0TPYBIGT9Jmzu6ldeokG4_lFpIKZylVjPIiayevedTcjGO-YZ4DOJKjAKCZ8Y8TiD9lxjFIrAhY3kaOixJGRdAddVjZcq5U4Z3NmE8vi3g-R4wkR-KZSrZpxjwuR036BvHutxaxg_2crzHAS34XAddB7-GIuOs3Mzp99a_sn0XIarFpzY121naGFYJ7uuTJS38IrVMvrFq7qwLI1GtxLT59bYQtlXnW9qeihGPmyLoEyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عودة الاحتجاجات في سوريا بسبب سوء الوضع المعيشي والمتظاهرين يقطعون الطرق لمنع صهاريج النفط من الخروج من دير الزور</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/92435" target="_blank">📅 17:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92434">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7164999ac.mp4?token=WnMiYh4-nutZz12MzMqHtzLr29x-OKH1gSA7ew0b8aYZSx7RMywEFk-aQytDxkByZjX5XOIiLrl7fWxMv4pBmMpMKROVJS19wgrTfaUQMCl12R-foTyarNCAAxx4FueKEjqSbdLpggGrPGTxdE24A8ni8KKrSTXkYfPvl1nQvGRXVcE2NrVim6gSyG5Uk0nOQHsSLx7QS-QBklLSR1jnnwHcOyy7Ry5WW3zOMdJC2Les8sJDemX_PYFxxFxKqXsHFwFVh8I3pmpD_X7a7cillsxaXxbMEkImhkZKcrdt-Zwa8M6vnV_PUsNegi7XONZIpd_KEEWSbAE5aZV2qcTfpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7164999ac.mp4?token=WnMiYh4-nutZz12MzMqHtzLr29x-OKH1gSA7ew0b8aYZSx7RMywEFk-aQytDxkByZjX5XOIiLrl7fWxMv4pBmMpMKROVJS19wgrTfaUQMCl12R-foTyarNCAAxx4FueKEjqSbdLpggGrPGTxdE24A8ni8KKrSTXkYfPvl1nQvGRXVcE2NrVim6gSyG5Uk0nOQHsSLx7QS-QBklLSR1jnnwHcOyy7Ry5WW3zOMdJC2Les8sJDemX_PYFxxFxKqXsHFwFVh8I3pmpD_X7a7cillsxaXxbMEkImhkZKcrdt-Zwa8M6vnV_PUsNegi7XONZIpd_KEEWSbAE5aZV2qcTfpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تدخل منطقة المساحين في مديرية الشمايتين بمحافظة تعز</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/92434" target="_blank">📅 17:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92433">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">إصابة شخصين نتيجة عدوان سعودي استهدف قسم الشرطة في مدينة صعدة اليمنية</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/92433" target="_blank">📅 17:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92432">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzv02zAAXhIOhGjHMgVSUgb4hIv2P-mu8nN2T46VCplLmZmmd6s6-Z4ZJPkuyMbMiPpklAaIe4_lLJ_ptdRfGABlbHYTNJmMOR2ptvlQHCz7gmuQRnWaAds3izAE4NeaRya5uFYthBhW8z1Fp82KZJnK9NXdfh4TBxpEOrmAvCEO7DYBrpHnifJWDCIIn-CFWC0I9VKrfiK2puKsBt8boSHNj1p1TqtbTvShDQqHw5wEMg2OI4uNxM2kivbJYI4vX5GpB_xOpQrtjOdrAH-UqJqvWYKR9PSk0hX746uySuupa5qyx71C4htx44nlwtI9c6cTFmxHkvUBz1hCCV_U_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العاصمة السعودية الرياض تحترق</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/92432" target="_blank">📅 16:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92431">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/567da1e998.mp4?token=AKDf1nfybtGQek9w3ZlSxOoOKV-qa8qcMHPv6sXgqucEheLVcFZ9y3mqEMwpT5FdHjRw0TGzWFmyIV6e1vpXQS75cjckCcvqsIIOSCLwEIEC-NyoIf65D8e98-3PVPe9-lxR_wRdLeke5kx13FFsp-7P7fvom_9RN-rQAGcPUE72nBLgamus_pq_pY9-hSEx0Ul7VFW_H5zAq17LfzwACtaAw-3j8LKlsZ3bF5J9ReHNNO9emHYYhEaH69vBt0tnwkYUEmCJL6_-BZTtOUiHoybrYADJu1XQgVkVCJWUCShlqJDmj26jwl1a8_MGzcR1U2GQAA-43SvN_qlZ5JwWcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/567da1e998.mp4?token=AKDf1nfybtGQek9w3ZlSxOoOKV-qa8qcMHPv6sXgqucEheLVcFZ9y3mqEMwpT5FdHjRw0TGzWFmyIV6e1vpXQS75cjckCcvqsIIOSCLwEIEC-NyoIf65D8e98-3PVPe9-lxR_wRdLeke5kx13FFsp-7P7fvom_9RN-rQAGcPUE72nBLgamus_pq_pY9-hSEx0Ul7VFW_H5zAq17LfzwACtaAw-3j8LKlsZ3bF5J9ReHNNO9emHYYhEaH69vBt0tnwkYUEmCJL6_-BZTtOUiHoybrYADJu1XQgVkVCJWUCShlqJDmj26jwl1a8_MGzcR1U2GQAA-43SvN_qlZ5JwWcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منشأت ارامكو تحترق</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/92431" target="_blank">📅 16:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92430">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52d0e3bdb.mp4?token=bEW4JcaLMOwk_VTT95cSe0qSdwTShdYAFT1WpqJNVrtxB5gEtQPFjdJbdccSvIKYJ4Fy6-VxArcw5xQ5JEWhL5jDBcZK5lhveKwCxgLb6LKU3R_FpBHDWu7buIjnoLL82gv0AzDD2FzbgcAhBIr1Oc7UtoOPn_8nK-HiwMc6KV0bNgTnm5glPNkOEX-SX7goUDs3rva_koLdaYv1rpX2Rgzf_zItr49szx5K0RpcK9_S0VDmgU3vesBivrcsw-JVLtaFL_OPFzjr7DF6YYJ4S7V-Bu-McB80hgqbZ9GJNOnYQR9ob6Y0wkYCeoG08lx93X9jWgp0gCRMoQRer5YemQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52d0e3bdb.mp4?token=bEW4JcaLMOwk_VTT95cSe0qSdwTShdYAFT1WpqJNVrtxB5gEtQPFjdJbdccSvIKYJ4Fy6-VxArcw5xQ5JEWhL5jDBcZK5lhveKwCxgLb6LKU3R_FpBHDWu7buIjnoLL82gv0AzDD2FzbgcAhBIr1Oc7UtoOPn_8nK-HiwMc6KV0bNgTnm5glPNkOEX-SX7goUDs3rva_koLdaYv1rpX2Rgzf_zItr49szx5K0RpcK9_S0VDmgU3vesBivrcsw-JVLtaFL_OPFzjr7DF6YYJ4S7V-Bu-McB80hgqbZ9GJNOnYQR9ob6Y0wkYCeoG08lx93X9jWgp0gCRMoQRer5YemQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منشأت ارامكو بعد هجوم القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/92430" target="_blank">📅 16:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92429">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2f30f9744.mp4?token=JtnjvVWcVf6B11C9CO4_YNkQzNUoKsk005GGSK4gIo7aVpswilrgZuVkivNJhEEk3Ip6jteCU6XLnI_8ijVeMfPa6k9AXhlJkbFY0Qg3QUKfMDJ_BEoOTh9dpoGZWW48frFSkAs7YhPXlFRfFUg2-nSKkrFtJuO06Xhr9GnMjadb5MpNa2nQD_AFNuKQYlc0hZpVW7etYf9f0UAMaacUa7ikBkKvcv2WnZeUHbPh2xgc_TKSUFKpgZ-8AdQge2Hg1uSvKlUQ2-cy8kkpSZfiiLXXsIwaqC3bPpDfpCtLYSBAjHp1Q6CqqfURQtTKT47MhMDS71LgNO5Fhx0HYi-bzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2f30f9744.mp4?token=JtnjvVWcVf6B11C9CO4_YNkQzNUoKsk005GGSK4gIo7aVpswilrgZuVkivNJhEEk3Ip6jteCU6XLnI_8ijVeMfPa6k9AXhlJkbFY0Qg3QUKfMDJ_BEoOTh9dpoGZWW48frFSkAs7YhPXlFRfFUg2-nSKkrFtJuO06Xhr9GnMjadb5MpNa2nQD_AFNuKQYlc0hZpVW7etYf9f0UAMaacUa7ikBkKvcv2WnZeUHbPh2xgc_TKSUFKpgZ-8AdQge2Hg1uSvKlUQ2-cy8kkpSZfiiLXXsIwaqC3bPpDfpCtLYSBAjHp1Q6CqqfURQtTKT47MhMDS71LgNO5Fhx0HYi-bzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من العاصمة السعودية الرياض بعد هجوم القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92429" target="_blank">📅 16:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92428">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd6222851.mp4?token=ZY0rz38eA2f4LItL-6V9CHFBAMZw7XpG5UfIde60E-vlvXxB7AAb8T2GlfX0gur2EiK-CVGXuvtTYA2LHzDncnnqMhOsslf_hRZzThLlE1Ir8JkhmNpclvpuUHoGzhJiFEMFp0smMzfAK4ovm2jyehCXGUNU9MTrNAHglBCJxvcEZ1CSx7gTedcEAy7XxJZUes1DaB0aCxaLiN5d23oL0BWqr3U_nij2rvgWB8uU_1q0cDt0Uy9IDY4uOdD1MDsWggPyJIxGD1gTTrTktE2oHvo9bqibgjIbwrmS5uG5FjA8smOaBYOPIoPnluvOzyVLMY5jhDDZtF4--APkQzwSig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd6222851.mp4?token=ZY0rz38eA2f4LItL-6V9CHFBAMZw7XpG5UfIde60E-vlvXxB7AAb8T2GlfX0gur2EiK-CVGXuvtTYA2LHzDncnnqMhOsslf_hRZzThLlE1Ir8JkhmNpclvpuUHoGzhJiFEMFp0smMzfAK4ovm2jyehCXGUNU9MTrNAHglBCJxvcEZ1CSx7gTedcEAy7XxJZUes1DaB0aCxaLiN5d23oL0BWqr3U_nij2rvgWB8uU_1q0cDt0Uy9IDY4uOdD1MDsWggPyJIxGD1gTTrTktE2oHvo9bqibgjIbwrmS5uG5FjA8smOaBYOPIoPnluvOzyVLMY5jhDDZtF4--APkQzwSig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من العاصمة السعودية الرياض بعد هجوم القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/92428" target="_blank">📅 16:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92426">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d3lttzcG0hPtqa0_H_t9wy0lBvNO58xof9UFCK9L-LjDOv8yrdK7U1Q0r7ZCLzECtRVhMpA1VEI9QLAlWex8mWgJcAuFdLE6i4b-CwlTpwJLx9ATjQ2Wb-34uqAkObQlHUEgPJgwHMIUmUEMVqroUDVw6TQJcj5dNQqC27GFz-Jc6PH5ynu9J5CcPNtbeyL5qyYkqrAshq2bCpnlH5wGJ2-gAYqF3QFksJgQ1XJnZ6B-SNy6PEheuXHLPrO6hcV9iJkhor84cbvakcWaoDPBF55f11ukgCd8Woj9Yy0QOefcF-lsN1iLaNAXrKu7oUkEyKODwcB9e5IAG1So7SZong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QtPjaKZHrixrae5V54WT9LleLITGn4vSmMQvEwSjBkPvixNyBGCbOaFoQBLRhWUI8xdFRpYhJ6LbQfmE98jjqsTUiZ_E_c9TKUSAxeItwr29k2bI8wngVf8AW3O10cx3-MW1MHVWLkWcpjwp6Sk-63HwPBTv2hMyBizULrJwysbmd0mIhxm2Hk-j42NKDUhP_b1muu9z8w-BuJrVNhdS0JrJ7IMs7560bi_iLkaIiMeSYqdl_LMMgauJLZKBujm1KG2aTu-ntJjWUKicE4LVke1iuuUR3oJ8ZF2FGlp5qzYViog-nAGERXPqtKzZ9ex5i_fQYFbc1z3GHcVHTDZ9kA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صور أقمار صناعية جديدة تُظهر اشتعال صهاريج الوقود وخزانات الضغط في مصفاة أرامكو في الرياض عقب ضربات القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/92426" target="_blank">📅 16:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92425">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انفجارات جديدة تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/92425" target="_blank">📅 16:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92424">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">جيش الاحتلال يعلن اصابة 8 جنود امس من لواء المدرعات السابع، بجروح نتيجة حادث سير عملياتي في جنوب لبنان حيث اصطدمت مركبتان ببعضهما بالقرب من بلدة رب ثلاثين ما ادى إلى نقل 6 من الجنود لتلقي العلاج الطبي في أحد المستشفيات وتم إبلاغ عائلاتهم.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/92424" target="_blank">📅 16:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92423">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">عضو المكتب السياسي لأنصار الله حزام الأسد: العاصمة بالعاصمة ومن كانت عاصمته من بترول لا يُشعل النار في عواصم الآخرين</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/92423" target="_blank">📅 16:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92422">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وزارة الصحة اليمنية: اضرار بمستشفى السبعين للأمومة جراء العدوان السعودي على العاصمة صنعاء</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/92422" target="_blank">📅 15:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92421">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgclSmCYcte82r9uUpLTr_kYwxkuWlTXkctO-m7HGJvfkvdosnULblgqQtZhGorBAkMOZ_864iBdlTxITDWdqXd1nnxqeWUSAhhHpuftHboya8sKq8_vG0Y5s6ATC0Y037cdXGApOT9ALI2QUiuJ3bjY-Lo00fQ10UyYhryVOFURm6azgBtytg4cqh0JBcybb43LNyTF-WPbXJcTLZuzP3t9z3ZvqBSqDtAULJvnMxFFidIkBQZYW29MFt-3DKkLRetRJOKRtWEaGxBgwVKiv3aTdGVNcfsMqFQy_f1tr1rUZCJ5CnB-LYDwoL8zHaFUiTm26xZWr3S40xnSieUx9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خفر السواحل الأمريكي: اختفاء طائرة إسعاف جوية كانت تقل 6 أشخاص قبالة سواحل مدينة "نانتاكيت" بولاية ماساتشوستس. وعمليات البحث جارية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/92421" target="_blank">📅 15:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92420">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">القوات المسلحة اليمنية تتقدم في عدة مديريات في مدينة تعز</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92420" target="_blank">📅 15:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92419">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اطلاقات صاروخية من العاصمة صنعاء باتجاه الاصول العسكرية والاقتصادية للعدو السعودي</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/92419" target="_blank">📅 15:23 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92418">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇶
🔻
الحشد الشعبي يطيح بعدد من كبار تجار المخدرات الدوليين في منفذ ربيعة الحدودي مع سوريا و
التفاصيل لاحقاً.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/92418" target="_blank">📅 15:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92417">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4VhrjmwQbv53p4Isdpl_In0g9fNuMPlUWcc5SHNOm8KSn4I0myMuXK8U2tSNUqn8OY4UPYgfB57ehF1tBThli26GZzuatl6ppQLwPUoA_gCuuRQV4f4IgvvDHhSewn8ViUFHO1dD_HsQIqpBWkhq4i9X8gjhm2OvQ4yWJoOzdjXIM-wDF1KgM45sM7BBGfgVXIc5wwDWcWx5Gn8aP-4FvMHGJe_nOsPq4sZuWLOwcNBjoADRJxcWeiszVJK8sYrwTYscSvjUFzNRgg4-Ntk1c0BQ6gjAC-gQlRbA3mXAb2mw53zN7VTgAhkZC8oiWik4g0YUc0XgMA9YDwqqS4kxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وكالة رويترز: شوهد عمود دخان كبير وألسنة نار بالقرب من منشأة تابعة لشركة أرامكو في الرياض</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/92417" target="_blank">📅 15:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92416">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انفجارات تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/92416" target="_blank">📅 15:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92415">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ممثل المرجعية الدينية العليا الشيخ عبد المهدي الكربلائي يعلن استعداد العتبة الحسينية المقدسة لتقديم العلاج المجاني للمرضى القادمين من فلسطين وتحمل تكاليف علاجهم ونقلهم</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/92415" target="_blank">📅 15:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92414">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وكالة رويترز: شوهد عمود دخان كبير وألسنة نار بالقرب من منشأة تابعة لشركة أرامكو في الرياض</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/92414" target="_blank">📅 15:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92413">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a5b43795.mp4?token=lX1ghUJtIw4NSaa-VzgyydMdozueMKTkxAi_mjCBIrpGWmOPUt6RY3ARxXdHFm_zf2KdMedB0FIK8itGoO0esha9aijlS9GnXY4F_vWNehqR5wl6sEu8MyT4-EZqmCB8RMikibFN_Wvl7NCIjbqzUMn6M1YrYk7CEOrr8H9UeZ2YgNHwDcyWPgribTyCIbm7inVbVz1u1mrbpRdkqaBRNBCdIVhSMgjPTBU9t7W56cD5WExaNJUodLrklBuA-LF3KDMi34AHhzdm2BaihIucmYX6u3Kx7S4rV22HDhwSYg9uOKhXSQgub1T-idmDKajaFbX3ZXp1dRqIH7v3MYun0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a5b43795.mp4?token=lX1ghUJtIw4NSaa-VzgyydMdozueMKTkxAi_mjCBIrpGWmOPUt6RY3ARxXdHFm_zf2KdMedB0FIK8itGoO0esha9aijlS9GnXY4F_vWNehqR5wl6sEu8MyT4-EZqmCB8RMikibFN_Wvl7NCIjbqzUMn6M1YrYk7CEOrr8H9UeZ2YgNHwDcyWPgribTyCIbm7inVbVz1u1mrbpRdkqaBRNBCdIVhSMgjPTBU9t7W56cD5WExaNJUodLrklBuA-LF3KDMi34AHhzdm2BaihIucmYX6u3Kx7S4rV22HDhwSYg9uOKhXSQgub1T-idmDKajaFbX3ZXp1dRqIH7v3MYun0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
توثيق يظهر إشتعال النيران في موقع نفطي أخر بالعاصمة السعودية الرياض بعد قصف صاروخي عنيف من قبل القوات المسلحة اليمنية صباح اليوم.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/92413" target="_blank">📅 14:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92412">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">القوات المسلحة اليمنية تتقدم في عدة مديريات في مدينة تعز</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/92412" target="_blank">📅 14:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92411">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f77d1d4ff.mp4?token=YPa_XXJ0QiDOxF-vVsYElX9uPOuXfiPAVa1Bo7Sl07ncwaOi14ubv6KK8c6lValOQGhh0LhzFjCUN7kxqh73e23kDb8UeS9xk_AnRc73MrcAEQCBsZjM5DrJjwv9iaVCZyve9a-n5HH82B4nP3QAjjIJPW9slR-YvZyjbtMfRu0eQT61twOMWahaLR-v9L9SbW6uqXrGbEdEdkINqsdHEDBksIgtNA1VrOipFdZK1LkI0rWwzY3t5OaiUomRt-aPpvTwhNw6q6GbiTDJu9NcGthArdnnYFk4fzgNscBsnCFQ0ToaEcfb8h2ENJ0qQIrzwOqzszJ4Pcc000xmnOOl3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f77d1d4ff.mp4?token=YPa_XXJ0QiDOxF-vVsYElX9uPOuXfiPAVa1Bo7Sl07ncwaOi14ubv6KK8c6lValOQGhh0LhzFjCUN7kxqh73e23kDb8UeS9xk_AnRc73MrcAEQCBsZjM5DrJjwv9iaVCZyve9a-n5HH82B4nP3QAjjIJPW9slR-YvZyjbtMfRu0eQT61twOMWahaLR-v9L9SbW6uqXrGbEdEdkINqsdHEDBksIgtNA1VrOipFdZK1LkI0rWwzY3t5OaiUomRt-aPpvTwhNw6q6GbiTDJu9NcGthArdnnYFk4fzgNscBsnCFQ0ToaEcfb8h2ENJ0qQIrzwOqzszJ4Pcc000xmnOOl3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان السعودي الاجرامي على العاصمة اليمنية الابية صنعاء</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92411" target="_blank">📅 14:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92410">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba88927483.mp4?token=gykmCR3uS-Pb1VYg2E9-5P97uecQvWP0t194YVm3hV5aIAcsVml8U6tU3QX2W5nXsgbAOOey5eIEmMQ347xlZJ5b4a8-nQ4qrXQZM1vTKXhUCESBDnghshsyje2TPC-kIa77IVc5B5KIIm80gUfse4GITamRuvWxs6wN4Yios9X3gIZNpnh9VHlzFzaLyG0wiN-sN-s-Fyv4GM2i2gU-sSGlI2zpTbaFBPXt3Z-l_YCMsyhax1zJprskETv4CuJ9PVLSUyqOBwzVDA1gvN76rns2BJBnI2g5wwObeAcP25GM1cIgwb2onNAbTrCijnLoNW1XAwz3kY8oldp0WS1ysg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba88927483.mp4?token=gykmCR3uS-Pb1VYg2E9-5P97uecQvWP0t194YVm3hV5aIAcsVml8U6tU3QX2W5nXsgbAOOey5eIEmMQ347xlZJ5b4a8-nQ4qrXQZM1vTKXhUCESBDnghshsyje2TPC-kIa77IVc5B5KIIm80gUfse4GITamRuvWxs6wN4Yios9X3gIZNpnh9VHlzFzaLyG0wiN-sN-s-Fyv4GM2i2gU-sSGlI2zpTbaFBPXt3Z-l_YCMsyhax1zJprskETv4CuJ9PVLSUyqOBwzVDA1gvN76rns2BJBnI2g5wwObeAcP25GM1cIgwb2onNAbTrCijnLoNW1XAwz3kY8oldp0WS1ysg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان السعودي الاجرامي على العاصمة اليمنية الابية صنعاء</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/92410" target="_blank">📅 14:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92408">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WHukE2iA4TRe6qalDXbvekXnTni2iwKmuXuTh9RrnmxgbgzZbFVeL_tvn_bIk27JzcqlU9Ra19dvsclrjG0PvCxwN4rVIrHxiTzF1kMbOhBOjI8Ski-g_pwVzrhkdxiOCQ98MHSwE1scXAX449w2Lw6UXCHIqUpOdilG1SLhpKeiKpeLX48JIXgQxAXjaMzCo3xDqj78aqHGPZwJsbvMaECZiWzpZxAoeT8454omW0pKXzQr4riJNBsje1t6D9-XqZCoVKhfI0vOGAsb77enwPGnNHgZjdnkNJva_VBQcl5JXZSLXbpDG2aHEfvev64yKXEWwOb2WDivWhMdYHxjlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Urv22ksZzz2acQYaWutZqCA15Cn_cc02kPs2I4VmZQwomQ_HESf8gaL444ESXSWFhUf_Eqqdbt7o1wc5batYwk4YYUhBACBSJ22QXYflAgSc_vzWNlNfQJx4vaI9JcNogwdDtmZMlC4pyYgGn_dkdNCvnUzAtyIz664OceUypARwAlr1g4ZET_0_ZR8X9TxliOC8M28Fei1F1RMOfmyw7dWDpnzJJOvfkh6SrFHX7xm3BMlNI_QQ26Iwh6fbU3thH_jxlSFDyMIEsVVD0MEljHtlwMxVKXuAFBeI9_ox27StDBEt1jvL4vgWYMPEElT-utckJMM8TSVy88iNPPGJcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">غارات جديدة على صنعاء</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/92408" target="_blank">📅 13:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92407">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">من العدوان على صنعاء</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/92407" target="_blank">📅 13:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92406">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25c05eae18.mp4?token=KlNCSDVa65SDDpHbmABk54jTe0dZ6JexebTltXDaDhMcnVzLVq6RGHngnOzLooOGzXCWoIKji_I95Gi3mq8PXJmzDMRTf18lXO3ReSSYL2b_ERJmjVxIsaoh7saW-dn9YdeU3sc0x9h2cmHnNsJ74wAVmJO4UhDx1jOJJ2oepv6iJzL0N8qWAvHjti2mf4yz6ikCFcJlhR3ySJWMl-R8P4yMPr-XtRhatPNVUq9IvVmN72rCXNARsGZDaCKk0urHbKdHhWnqjF-Bd_1umeKfAHlCMNJusMl1bUPlC8QBYiPkPG56QY9kPhr9Aj5Ou1tQofxbqnSaTJrZbhixbTn-_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25c05eae18.mp4?token=KlNCSDVa65SDDpHbmABk54jTe0dZ6JexebTltXDaDhMcnVzLVq6RGHngnOzLooOGzXCWoIKji_I95Gi3mq8PXJmzDMRTf18lXO3ReSSYL2b_ERJmjVxIsaoh7saW-dn9YdeU3sc0x9h2cmHnNsJ74wAVmJO4UhDx1jOJJ2oepv6iJzL0N8qWAvHjti2mf4yz6ikCFcJlhR3ySJWMl-R8P4yMPr-XtRhatPNVUq9IvVmN72rCXNARsGZDaCKk0urHbKdHhWnqjF-Bd_1umeKfAHlCMNJusMl1bUPlC8QBYiPkPG56QY9kPhr9Aj5Ou1tQofxbqnSaTJrZbhixbTn-_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اكثر من غارة على صنعاء وسط دعوات للهنود في الرياض لشحن هواتفهم والاستعداد</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/92406" target="_blank">📅 13:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92405">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9T57z1FasjXGi-Zo0BMMU0RtHB2Zv6EQSCGAZ323SxesiXImBi1skd2knbCD6QX9vmaaWtEOPHoRwvdWhRZBEz-35VhDJ86uEqloz73d2xLDK63c4E5x16svTpPBqlrNTq2iT0q7MAOiL_upDF-LsJieXz2ELE9if9f5tVoFAkXAHzQIxxhiEZc7Jiqsem5wQUrGtCJp6iFXm9AYSv8lGYYiO1jYV_K_aUyW2dACcDBneTdEXaQ4G49fKbDwiZgQY2VZkgZsbv82gAEg2Gx7ufd8ViDensNdxrsHarweANmQlcoW9zyZMUZsTM56UHBQ3WDFsh9WvkEi-Q6V6j3_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد اعمدة الدخان من صنعاء بعد العدوان السعودي</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/92405" target="_blank">📅 13:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92403">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jexMetbIdKDom5jjYIy4tJeHz15hA57nUyHb1DoxYeyR2aZ9EMH2QHNeqCRqWdOqX-QsXrf1e1Dl-_WtncU-Vtd2wEF95aMngZT8xU_iWqq13oFQ7ylDji9M4jvlNkWJL3wwj1BvBqpFWjFDzP6lUze_Tm2yj3qEBqNbIcg87-IbApDPePyXme0utfBmanFqctlhki8O9LqMgJ-co-hG2Kw9MBmalU7yTDJWJKIaQxAtSIyLyq6HBNbD_KCo4C_tBPuW7W_6Ao0xABCSXNc5BN8d6RjVGFuW_KQrCAVbwxsowsI8bXErdntbu8PX3NAfO_t8d9r0qlJEtDdbWRrx8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HoQbw4OosoArNHyNcToeilJ6BOqqjJwY-zHGIwauFUU6L_idxGjojdCF7Y_8nI4Mu172NNjzIFbTTLqdreX7RoOO6tYPfFbkq9e6cFc58EHuhEhafiJTtwKQONI2-4OLxWgNW14qh5ASCZgYlMB8eIgzWf8MdoyFD3_f0_UA1N1yz_xkJ0sETNc5T_ErRxxVAOeZ3zkO95YRG0WRkjvh84R-hEdtUJqtSE8bySAyq97lsqvC05C9njRzQPuqm-y_651cCO6DsxrHWgM_YVk-ZIDVWF4KoOS8qMFVfDP7menc9AONZ60gOdINRM4WIAl5KTpwIyNr4uAX1wOEPgdrbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من العدوان السعودي على العاصمة صنعاء</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/92403" target="_blank">📅 13:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92402">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRSzs8z5WOjK8ds5At-h2OKLB0mI1c7E8krhbH42W7W6xZgcRZ8iXQiSI4YGUYd1btFCrDSosceY1mc7kStL4FmmyIj4mB8SLJrRrWDggO7nWOF9b28kjP2mJeTD9BAIhV2aWYDOObueXvrYxYDSnXwQzvUWno3XVvcpHZ6A5_V6rQ6oMdnZMkWDkStEqk0VU95bd1dHMbUX9DixQPKTEz_OgOR_aPwLSSQcJKxZyGpfd0oR3blPHjolARPS4-39cAacXMaPVD2voGYqYu-XbQdOUezhbs-KIElJILd46FOhz6jhvQmrDfRdqv_JQ9lOX4ocV_6h8RAE7pSojHtGJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي على العاصمة اليمنية صنعاء.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/92402" target="_blank">📅 13:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92401">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي على العاصمة اليمنية صنعاء.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/92401" target="_blank">📅 13:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92400">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇾🇪
🇸🇦
القوات اليمنية تتمكن من أسر عدد من مرتزقة السعودية في جبهات محافظة تعز.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/92400" target="_blank">📅 13:27 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92399">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇷
وزارة الإستخبارات الإيرانية:
تم تحديد واعتقال أعضاء 4 شبكات منظمة، تتكون من 31 عنصراً من عملاء العدو الأمريكي والصهيوني في مدينة سيرجان بمحافظة كرمان.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92399" target="_blank">📅 13:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92398">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇸🇦
🇾🇪
انظروا إليها تحترق.. من الحرائق الواسعة وتصاعد أعمدة الدخان في مصفى آرامكو النفطي بالعاصمة السعودية الرياض بعد أن طاله الإستهداف الصاروخي على يد رجال أبوجبريل.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/92398" target="_blank">📅 12:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92397">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cad71f6a8.mp4?token=DYv0WA5wikvqoFK8BtwQwf8UwiCIVtNiDvIgqgoH_dTqUPzj2nb38xObUf8pu1FygRnP2lLvqZ1ozr7lwdX0DY8R83_IncZ7eyYSUIXZyCU0cG2XO1YLJvhkDKoRnNL9FciEW4qFP1jH5h0H88S1ltUOtlsTOjoRdyLKbkciuCfU_uP2jUkMLs-M3t2ILvRKdzmen8fCV5leQa0EvzUsXHDIXf6fN-akFNGqgk1yjexgFmaxm1TH0GRZyOoGqhBGrfBlPc6EiOutE5mvuLqjQFKa5rKk_vTKOjpXpKUAJHEJ0Nxg32E5cxOjjNqAPk1K8uhAtOoCiaPAUHTe45vQBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cad71f6a8.mp4?token=DYv0WA5wikvqoFK8BtwQwf8UwiCIVtNiDvIgqgoH_dTqUPzj2nb38xObUf8pu1FygRnP2lLvqZ1ozr7lwdX0DY8R83_IncZ7eyYSUIXZyCU0cG2XO1YLJvhkDKoRnNL9FciEW4qFP1jH5h0H88S1ltUOtlsTOjoRdyLKbkciuCfU_uP2jUkMLs-M3t2ILvRKdzmen8fCV5leQa0EvzUsXHDIXf6fN-akFNGqgk1yjexgFmaxm1TH0GRZyOoGqhBGrfBlPc6EiOutE5mvuLqjQFKa5rKk_vTKOjpXpKUAJHEJ0Nxg32E5cxOjjNqAPk1K8uhAtOoCiaPAUHTe45vQBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
من القصف الصاروخي للقوات المسلحة اليمنية على المصافي والمنشأت النفطية بالعاصمة السعودية الرياض.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/92397" target="_blank">📅 12:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92396">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/251473a77d.mp4?token=R5wyhtpJ5Kl2riGxExJ1eVkMygFX9WJNrLIFL-LliJrFsbmNEGI1ddHUOMJWEXrX9AD6GnRXDge24m-_cIKKe6Hx64x2vdMaE5kf2J3bkK7fXEaq8ZVIyCUX4Gd9ftBPgCzlObuLcpcVBOCLBeIcGLQuBmfIg4DArpFSb-qFdeoBYX_afCJG6cFhg1ng83RtvoWv5jlz5niOr9YDgOr5neVG8whK98WQR_HfRP7rQ7heqjN9Qw6tOCab93x8ZCHA2f_hgWXjeHp7IslByHXCTLK8vm_cddzuGqfQZLfCdUkScqOiZ9o1xJbrtxGipqvZtXLrnkETrVj60XoUdSIfQX9DBCXIIsQj6f1aPL0atnNcPV57LzD20Dqhn0gLWiBxf0AfEArgfdNeik_kvtgSjJlGxsDUBKKnMkAXwmvHSv5UALNo0D2yxrYeLA04xr1c_lh9De4n0d4BxtfiTEUxy2T3YJOpFxzACYHA2oPl43nqpUTjuAzDtURve_ZXIKY__FYOXjOVwK40gqDJ3CRai7ik6lAYlhwuPQHu2uA3IBveUkVzRkjTMn0UFM6nvaxr2ZEn1wN4ffJ1L16xhqGGc1TK3yvRMXcAvXs_u4mtIFZJmJc9FU3ow6AzpCbcLJK0XOxdrVBbUtJMkfbCGSXd4fTO_CpIymUTgLLnk0EJUqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/251473a77d.mp4?token=R5wyhtpJ5Kl2riGxExJ1eVkMygFX9WJNrLIFL-LliJrFsbmNEGI1ddHUOMJWEXrX9AD6GnRXDge24m-_cIKKe6Hx64x2vdMaE5kf2J3bkK7fXEaq8ZVIyCUX4Gd9ftBPgCzlObuLcpcVBOCLBeIcGLQuBmfIg4DArpFSb-qFdeoBYX_afCJG6cFhg1ng83RtvoWv5jlz5niOr9YDgOr5neVG8whK98WQR_HfRP7rQ7heqjN9Qw6tOCab93x8ZCHA2f_hgWXjeHp7IslByHXCTLK8vm_cddzuGqfQZLfCdUkScqOiZ9o1xJbrtxGipqvZtXLrnkETrVj60XoUdSIfQX9DBCXIIsQj6f1aPL0atnNcPV57LzD20Dqhn0gLWiBxf0AfEArgfdNeik_kvtgSjJlGxsDUBKKnMkAXwmvHSv5UALNo0D2yxrYeLA04xr1c_lh9De4n0d4BxtfiTEUxy2T3YJOpFxzACYHA2oPl43nqpUTjuAzDtURve_ZXIKY__FYOXjOVwK40gqDJ3CRai7ik6lAYlhwuPQHu2uA3IBveUkVzRkjTMn0UFM6nvaxr2ZEn1wN4ffJ1L16xhqGGc1TK3yvRMXcAvXs_u4mtIFZJmJc9FU3ow6AzpCbcLJK0XOxdrVBbUtJMkfbCGSXd4fTO_CpIymUTgLLnk0EJUqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
من القصف الصاروخي للقوات المسلحة اليمنية على المصافي والمنشأت النفطية بالعاصمة السعودية الرياض.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/92396" target="_blank">📅 12:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92394">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965605401f.mp4?token=gPCPFr2Xlo6gfuvb0O-jXuTFTw5Ysw_NR0MowN-6haJHsgYSAZRCaAdzSudlf8p3O8j8DpKfH_LP8nm3Cu57-1NctoMYoBXWaGPMi7mQ7UZLKnRlf3vLE5_tUZtqlMXsmKkxpQqVgd7BfcVvSLQFeLZ3Q8426PrCSMWWwfxV2Q_bmgjSTFXTrXPowKCIc1veEdtM-tvES6FNsnBoegTS_8YEsj3n3R_p5I69zH5g0LQ6rScN-cw4y4DrUwxq9h6ETv56eIQI2vwvzzr4ozAM5iRjILxOb7dMbGKqmp9wa9Mr85ntgAgK2xvkZj_Ilfw9-0lb8_2EgtPJn4ISg0MObQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965605401f.mp4?token=gPCPFr2Xlo6gfuvb0O-jXuTFTw5Ysw_NR0MowN-6haJHsgYSAZRCaAdzSudlf8p3O8j8DpKfH_LP8nm3Cu57-1NctoMYoBXWaGPMi7mQ7UZLKnRlf3vLE5_tUZtqlMXsmKkxpQqVgd7BfcVvSLQFeLZ3Q8426PrCSMWWwfxV2Q_bmgjSTFXTrXPowKCIc1veEdtM-tvES6FNsnBoegTS_8YEsj3n3R_p5I69zH5g0LQ6rScN-cw4y4DrUwxq9h6ETv56eIQI2vwvzzr4ozAM5iRjILxOb7dMbGKqmp9wa9Mr85ntgAgK2xvkZj_Ilfw9-0lb8_2EgtPJn4ISg0MObQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مصفاة النفط التابعة لشركة آرامكو بالعاصمة السعودية الرياض تحترق بنيران صواريخ أبناء اليمن.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/92394" target="_blank">📅 12:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92393">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇱
إعلام العدو:
فشل محاولة اغتيال علي العامودي خليفة السنوار المحتمل في غزة.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/92393" target="_blank">📅 12:09 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92392">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a76c3a62fc.mp4?token=uzf6C1GRgMiMtpmREhuFtwhJSV_-I3UQPSMU_lXHOgcGBJBM0fpi79nvq4i5PgvRTnFHJRb0TMLt92b4xmdDCkV7T9qyBMWSPekPaHvQ8H370kyNz0hS1v8QbWTre4Ty4QRAqFI96xIQrfHkxCSk32XmlCJ5dks08lwacDWA-cNrF9KBEGiUCwK7lV_xEvm49WwqKYxXhp_oavsQf-RweVvIJLFl4b5-yZJ-fN6KBPbEcjwEPCdqbn2EcxMZTb2ThMdLfPTdmSxbjS-rmLku67pXSyWqgv4Xbas_E-31eo6q4unN8JO-TkMBwM2iGQil_5DibAZCXcOMDVPtjv0vX4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a76c3a62fc.mp4?token=uzf6C1GRgMiMtpmREhuFtwhJSV_-I3UQPSMU_lXHOgcGBJBM0fpi79nvq4i5PgvRTnFHJRb0TMLt92b4xmdDCkV7T9qyBMWSPekPaHvQ8H370kyNz0hS1v8QbWTre4Ty4QRAqFI96xIQrfHkxCSk32XmlCJ5dks08lwacDWA-cNrF9KBEGiUCwK7lV_xEvm49WwqKYxXhp_oavsQf-RweVvIJLFl4b5-yZJ-fN6KBPbEcjwEPCdqbn2EcxMZTb2ThMdLfPTdmSxbjS-rmLku67pXSyWqgv4Xbas_E-31eo6q4unN8JO-TkMBwM2iGQil_5DibAZCXcOMDVPtjv0vX4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مصافي النفط في العاصمة السعودية الرياض تشهد تصاعد كثيف للدخان جراء الهجمات الصاروخية والطيران الإنقضاضي اليمني.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/92392" target="_blank">📅 11:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92391">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcb6959801.mp4?token=T08FMMRuMR5glv5hHEC0YnJLTp_bxqztdfb0TCf0Kxqd02YmY-vn9xDrI8Zo9NGh6dWM6r_jVQF1w_Wouc3I_QIlBJebuTUDNhq_8bIgoHuYkLIKzaCqtLadHD0SURBzdjIMFZ9UZblATjHKiXmCdwy3M9xyWTxinVxoN9nMUAtopdmjOuzOuwBp7wz752t3GN79tSoXpjkT1d0fU8ceqGYF7AT7iExehYBRYpboOHcLtM4VPpF78q26X_5gcQ1AV7FsFuQnut4JNuGdo2ztpLwwTkYZbnnK008EWruUsGn4JDdYPzWy4xjiCHlpZOeFp1BlkTFCtyAIqQf6n4eDaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcb6959801.mp4?token=T08FMMRuMR5glv5hHEC0YnJLTp_bxqztdfb0TCf0Kxqd02YmY-vn9xDrI8Zo9NGh6dWM6r_jVQF1w_Wouc3I_QIlBJebuTUDNhq_8bIgoHuYkLIKzaCqtLadHD0SURBzdjIMFZ9UZblATjHKiXmCdwy3M9xyWTxinVxoN9nMUAtopdmjOuzOuwBp7wz752t3GN79tSoXpjkT1d0fU8ceqGYF7AT7iExehYBRYpboOHcLtM4VPpF78q26X_5gcQ1AV7FsFuQnut4JNuGdo2ztpLwwTkYZbnnK008EWruUsGn4JDdYPzWy4xjiCHlpZOeFp1BlkTFCtyAIqQf6n4eDaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد تظهر دك مصافي النفط التابعة لشركة آرامكو في العاصمة السعودية الرياض من قبل رجال أبوجبريل، واعمدة الدخان تتصاعد من عدة نقاط.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/92391" target="_blank">📅 11:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92389">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njVoMxA3c2qiiP9JqYQB37-eIaryrSHCjfB2IBW3BrSvuusG_VxfBoMDaO14smegASFqRsX8I5rFbmVO9nHHFwq5mQwgYEkEHNpG_B87S9VcRGgzx8iSv_YRUu_sGsOaCoCJlD-uEjdXvkiAfYn-SGQ7YTkoiIiPTuLYpO2M3JXcvSP8YhEANCYKiArsqF2BaTvjx_z5Fir1cC7adXEZih5iKtOQi2Yn07hBgHa5BmaOBvt9Gr0aKUZxHzxHA2wqYSH0STkKCWH-NER2eEpBm5ZVUBa3V7b3IBdNoo6mO6yoW_9lOXEbfLyGnhYLxLrzhn-tw0maZl38oHnPg1BvBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Li8PzaHDlpkviKA_fv2pvggN3NzDW8n6bLgAVvHX1E2K_jYXQ7i8GfVZkQF8vTGIbdiyNQzHtA7eeAU_x7Fs1csp6hRmO_DJ51ZfJTlgpyonxnN6CxAg9G7HJCckpuakMzfFzzEkK-fl5HlJUa4XnpSZIw4Zz5qgD2sawVi12ELanzOZ1eNoxb8a1vEPA-HquwFhyG4GRcPXGAjGltnLzkiwBqTOT7ZIzws5IirWPm2f5-txpyz3rB8eztsIKBh37PqyiiBJMOdKuQY-NAqH-bQuW4duB9p5AN9gwkHDXvWy9CNs3k9h5lvmuxc9AyE9CEB-cnxeFObn2NTHyZP1TA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
سقوط طائرة استطلاع مسيرة من طراز "MQ-4C Triton" تابعة للبحرية الأمريكية على ضفة النهر في قاعدة "مايبورت" البحرية بولاية فلوريدا.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/92389" target="_blank">📅 11:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92388">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔻
السلطات الليتوانية: إغلاق مطار فيلنيوس وإقلاع طائرات للنيتو بعد رصد مسيرة قادمة من بيلاروسيا.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/92388" target="_blank">📅 11:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92387">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك خالد الدولي في الرياض.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/92387" target="_blank">📅 11:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92386">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgicUBZaGLu1s8PNlegP8uFQN1FFuWOy4WU41dP7XqRmpT9kN1yY6RaTRMFJImpSx3DtXFspX9gMZ9HjW2Rdk-gn0vJv5rHG2uCtXTT7P3k_2N24TNHlHsm5oC99khw0CoS4scjgrXvKZGVLB6BK8vSBmZQUmdsP_VK8d0BPYb_JcH87YpKmLLjoATN6331eUHpwpDsxPqpTNJqw5_bhkmRphqqMEj0wx5KSLUkd_WPHuIz5b-m1Pfjy-ycwAka2Oqls5M2s5heP5EP9vA1k0bYPVw92NQGCwUWYc09uWZ7Q-viLav1cGUuZ5Vygg0okEjAZzzTmhj50uFkzE6pinw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صواريخ تنطلق من صنعاء نحو المواقع السعودية</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/92386" target="_blank">📅 11:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92385">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGx_J7Vo9GqMa5O2CG0gzNbT8QNqzLjV7RbjQAG-gmmkmJgQ8exaeRDbRFsbmaSs2Ch2rCaBO_FhP73l6f3jO8nJxL48J8JCF_8GpMhKzGJ_Vehh8S3Kns6jm2RzI4Avs0hmOJOxZ8JZDQDFcusZ0gdVxKxBb0JaOMXoHZTlUAq6FLWcLNe06cHth2LIHgSaUQ_E8s_2tZLXHXZ1zjvOR1K7F97K0ml-5bO8c_MV5IuUzD2o5yHzxXazSLIhzkktzrPx2n_RY8WE6D3aIOJ9ShIvywKMW-RoJpm-NpRQczsbS__-YbD-C9jVLiBIhq9gWCrlDNJTGN_y_BBlc4Wa4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية بمطار الملك فهد في الدمام.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/92385" target="_blank">📅 10:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92384">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔻
السلطات الليتوانية:
إغلاق مطار فيلنيوس وإقلاع طائرات للنيتو بعد رصد مسيرة قادمة من بيلاروسيا.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/92384" target="_blank">📅 10:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92383">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك خالد الدولي في الرياض.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/92383" target="_blank">📅 08:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92382">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Crv5vdqd0_cjJ44d-P4Drl7KfsL90D4x2q142JndGoRZo8iHP2dQQjmD4rijr3A3pNeH6nthMAbodifX-tSQ2PuRJB7ND68QrcW1K7BP1bBzm9BhmBjaGMVqtEUUAwJ8PSjOE-Q6OH8ovGvGf5a9y6CHdiyV1en1ipAt9PGKOdO2luuUhVjRAKhmiRHAd0YBXnbbgmkYi5bDDulfsJ6w1bi2-0GfJWO-GZiv6VWthTEQd_pM92rpIeqoz2Ou-J7FTshwEJvEfsTurCf1IuiCsgKfSdw_Xm4VaMWDYPnnR5z-U_Vx3eRiXLX8cUppZ1noTfA7lBVNbpzZ4ABAq3vPxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك خالد الدولي في الرياض.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/92382" target="_blank">📅 08:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92381">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏ترمب: لم يعد لدى إيران سلاح جوي أو بحري، مسألة إيران ستنتهي مباشرة بعد الانتخابات</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/92381" target="_blank">📅 03:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92380">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jibScxVzW9KPaFO8WagOmSj94SYIpRxxe4bsEdZzpTg1woGHlVTFMH-QBVOHS7D_c__2oQ7xrZ3_hI_ewyjOAr8nlewwufLrw764Im9DIISE4RoKL9KGR4Ut6B2LFfg0CUwZyxdHJlsyhnbXyAo59eh9tIMbWxMkKE2r8TYra4POObAAzMHgBJb-LkHlHTTxcdqGLJ479FDbcTmeHihMblhr6bgUgZunIDN9OWH2cjQ_t24ptaiDxAdTsrPJbUJJ0gyhvVkwN7U9NJm6f72k_IqkGcEsxBBUtmdV811T5ZokV6sP6XjOgNkYY-5ZA9CCEDQND4vneWXZYab0yyTeCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحرس الثوري يستهدف  سفينة مخالفة على بعد 4 أميال بحرية شرق سلطنة عمان.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/92380" target="_blank">📅 02:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92379">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انفجارات في  منطقة عسير في السعودية نتيجة استهدافها بصواريخ بالستية</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/92379" target="_blank">📅 01:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92378">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇰🇵
جمهورية كوريا الشعبية العظمى تختبر صاروخ بالستي قبالة بحر اليابان</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/92378" target="_blank">📅 01:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92377">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1NI1LlU8PT217abnOA5CqCmksal-NGkePa6xEM9OU227RjicDwEbH7r2PqHl2qfXDLL-C5nP3mgVFTqqgP7f3PRyqKwJRcwQJ-_d0DGIolc98oC_zox-4ykmEoHc7SIzpn3QOdcSA6p6sIzzkrWrWUwyJ19BLKjkr4rT7JYQWUM8X9M9LPLUYdlfx2R5O3Or4WQ3Z8VWOR_dEE7HeXrfQG7so_dWVVmWCM1jHkV2-fR0sno0lvlSmrUvYMG4j21aXVjMdavNAQgCmLPSy2hzDisJ1B_PdgC3frlANGJTEMHE_2J8CEeNZBgVWs7LE-xYn-6KmtHiqdrk2t0RerlAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
الأمين العام لكتائب سيد الشهداء، الحاج أبو الاء الولائي:
اعتراف ادارة الشر الامريكية،
على لسان رئيسها الأبستيني، بحجم خسائرهم البشرية في العراق وتشبيه وجودهم هنا بـ (المستنقع والجحيم)، يؤكد بما لا يقبل الشك فاعلية عمليات المقاومة العراقية وقوتها ودقتها وبأسها، بعكس ما كانت تحاول أن تصوره بعض الاصوات، عبر الاستخفاف بها والتقليل من شأنها.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/92377" target="_blank">📅 00:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92376">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxrGccXmw7xsY-Z_sFm2CsBUBt5_kfpvFT9nbWExYSHsLyTkuXfRaLQFEVnMT5UbROCQuJi53RAcz8IHErJK5nbEskzpACNaY-nJlGRQ6y8F4PcM4D3yRKlWAt70pZd7410rq0hEWScKjAAZxROwvUWD8paMm-MPLDiPyPiuXjw2VB-MxbV2dZGbMV8yBXqI5_wey-po6BUoYFAWUEFbBcR_QkK2YsdRhRgZcJ-3FF4tO3r5K0cteqB3JyQAbliSrfYGuGYJ95XIGRehsmDVNnLXKAcWe8IoHWRj0eN5HWLj3qxJ6ZVX3sVq0CEITvEZGZcSFIhMgTE-9UshrAJXNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.   الرصد بتأريخ 1-10-2026</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/92376" target="_blank">📅 00:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92375">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇱
🇸🇾
الجيش الإسرائيلي يفرج عن أحد عناصر الأمن الداخلي السوري بعد احتجازه لأكثر من عشرين ساعة.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/92375" target="_blank">📅 23:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92374">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a23207838d.mp4?token=H360ibIftXdzG9_2Y_rNhM06zp63PjDuBkg3o8w7apPWzB-pH7Cc7XrVtwvxJCQjYb11BDtGuSi8lXlStKyzcKW6UVDz4FMi6KIe8O4DpWNaQXI--pJBcQupWi-0l8MSVsTH-zfwbPFz-cK06WbmgrWm10pN3SuV1HXsjW4IvtuKmuz34OdAR0TQz8uYK_oTWgNp_1swPCNcB-kVkNnHLIwITez8WyNNGpQbmcB57isnxmOq0qpBRX4sxymJbkcpQEz9_yXuvEMJEeJOhT0Gul4y1bJs38NoTngpd68L6kt-4Miz2tq6vt76gNunCXdui0feb0-21zo3PpsAiaZ5gzfBVu_rHnizOPYocwkIWOKjTiNwMqqCztov5nauuxO_LanLjRe4LzC0Tr2AMl1BhxE61YnJ6opxBd-jY9iQIoSkGsTUq47AZLCQ17BSvuXCa0sKl92ASDfU4E6IOasI_IgAcnmIOuGPMT-Squx7-k5Le7-31V08Fe46K7N3loRiHDHQuFxNZgMpKhN-QOdk12DEHcRCL4IMRyIvASz-KJjdPsRT10C5J2OgL_vBIjEHu4LLcJpOEIE3GUqhdwpGKvnx5TJCFLcfFecDdzWgfQyWsGNeEzVcPCiVaMdFlkENurjRo4UxFNTbUz4KxJwAa1nblALhC3sGDNbtlf6vuw4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a23207838d.mp4?token=H360ibIftXdzG9_2Y_rNhM06zp63PjDuBkg3o8w7apPWzB-pH7Cc7XrVtwvxJCQjYb11BDtGuSi8lXlStKyzcKW6UVDz4FMi6KIe8O4DpWNaQXI--pJBcQupWi-0l8MSVsTH-zfwbPFz-cK06WbmgrWm10pN3SuV1HXsjW4IvtuKmuz34OdAR0TQz8uYK_oTWgNp_1swPCNcB-kVkNnHLIwITez8WyNNGpQbmcB57isnxmOq0qpBRX4sxymJbkcpQEz9_yXuvEMJEeJOhT0Gul4y1bJs38NoTngpd68L6kt-4Miz2tq6vt76gNunCXdui0feb0-21zo3PpsAiaZ5gzfBVu_rHnizOPYocwkIWOKjTiNwMqqCztov5nauuxO_LanLjRe4LzC0Tr2AMl1BhxE61YnJ6opxBd-jY9iQIoSkGsTUq47AZLCQ17BSvuXCa0sKl92ASDfU4E6IOasI_IgAcnmIOuGPMT-Squx7-k5Le7-31V08Fe46K7N3loRiHDHQuFxNZgMpKhN-QOdk12DEHcRCL4IMRyIvASz-KJjdPsRT10C5J2OgL_vBIjEHu4LLcJpOEIE3GUqhdwpGKvnx5TJCFLcfFecDdzWgfQyWsGNeEzVcPCiVaMdFlkENurjRo4UxFNTbUz4KxJwAa1nblALhC3sGDNbtlf6vuw4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: إيران ليست في وضع جيد، وبمجرد انتهاء مسألة إيران سيعود النفط إلى أسعاره الطبيعية.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/92374" target="_blank">📅 23:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92373">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇬🇧
🇮🇷
‏
الشرطة البريطانية:
توجيه الاتهام إلى إيرانيَّين بالتخطيط لعمل إرهابي ضد الجالية اليهودية في مانشستر.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/92373" target="_blank">📅 23:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92372">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇺🇸
ترامب
: إيران ليست في وضع جيد، وبمجرد انتهاء مسألة إيران سيعود النفط إلى أسعاره الطبيعية.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/92372" target="_blank">📅 23:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92371">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rpqev0jtrT8GV-pVIDROsvWlVuOr_-98DVmFK2KsTtVrsmDo4UhtGMRelZoplEVWrKQNk70ROxiwfan-spWfOm3Hd81GJbRnedhq9ZZl8999QQBO8hHB0_Tkpg7bHtyzn6krDT1NNiP9b5PE6FTsxK8QPHOIwoKHPEG0aZDCBMXcESz2fMQPI2gbZhs10wPXOQ8x5qCIJ-wkHQmrE6eoBrYIUVPZxJxqIVPwY4hF1QqhHLKvrCecqT46whSEMMc-dv0HMZgUO3koVLmyZjbxzhgcmprohzl2q6v73hh3U3MYsqFblC5sdpgKhND1L1wVmnqApf8ac8IrkNDRd80Kfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
النائب العراقي محمد الخفاجي: كتاب مرسل إلى وزارة النقل العراقية يبلغهم بإجراءات الجانب الامريكي بشأن العقوبات.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/92371" target="_blank">📅 23:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92370">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔻
الاعلام الاميركي بخصوص قضية فلاي دبي:
عُمان منعت منفذ هجوم فلاي دبي من السفر بسبب آرائه المتطرفة.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/92370" target="_blank">📅 23:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92369">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnqm0ADjZim9lmTRFC4T5eD1T5joHXw2a73sByvSVoukuKKNN7UmPfEO1r_V7A8d_3LoMcytRm4I594L9U0wW6mmRItH5wbEu0QDmbfoelGfVvzPk7qK0J5jgVkN896Z6V75-__EixyM17UO3fXsdkjijM975zSnmt64PcyXMDRvgh__fMgdvIYj4SDJdRW-8pn9w1ko-o57FWuCwaMK6tY1K-nfKO2VvKzNnGkohZuaX_o2ymCLd3rBllwYF-h_WWA7M5KNQbhXlLhq0or0ZQSrdJgWoVf4XERuoo01d8GBgDU3mVoRkhnUAM-4N1aaS-K6sfAMaQKduUgLyhAV6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
رئاسة الوزراء العراقية: الاتفاق على السماح بتسيير 40 رحلة جوية يومياً من وإلى مطار النجف الأشرف الدولي لشركات الطيران الإيرانية باستثناء شركة ماهان.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/92369" target="_blank">📅 23:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92368">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإعلام الحربي</strong></div>
<div class="tg-text">🔴
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.
الرصد بتأريخ 1-10-2026</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/92368" target="_blank">📅 23:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92367">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇶
الميادين عن المقاومة الإسلامية في العراق:
رصدنا أمس 4 طلعات جوية للطيران الأميركي في أجواء العراق.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/92367" target="_blank">📅 23:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92366">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vj_ROeLwKYV-TEQKHgbffv3Me5nrD7IefIJmz8YvtWjKhzYejuKWiw8KiT0wEsV4oi3ciUGuQsBRq4Z0V8ByRj6rX_QB4V6AogkO4Qjmht50FXXxhL-8SRKHNxOAWUmwKI84PkYlFF3HyZnEno1G-33ovDXgyMBp3lcdVQiqjjVBPB4VXM-xVnqe8fy-DTTIXeJ8V_cyDD4uizL1qGPLvxf0X7922FJzj_Q-_Wat5yUJQDYx_DG6uvvdcAk2mS4yGAm784K8pGPvKHa3qn3Rrkr0Bd_V1-QjcctT_p7Hakm71_ith1wzN3RWHsSzXNEPeEKIyv4MZRIpz4jJFXjRUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
انفجارات عديدة في نجران نتيجة استهدافات مباشرة للقوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/92366" target="_blank">📅 22:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92365">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇸🇦
انفجارات عديدة في نجران نتيجة استهدافات مباشرة للقوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/92365" target="_blank">📅 22:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92364">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇷🇺
زلزال بقوة 6.2 درجة قبالة سواحل منطقة كامتشاتكا بجمهورية روسيا.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/92364" target="_blank">📅 22:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92363">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇶
🇷🇺
الخارجية الروسية:
نرحب بانسحاب القوات الأمريكية وقوات التحالف الدولي من العراق، نثق بقدرة العراق على مواجهة التحديات وتعزيز أمنه واستقراره عقب انتهاء الوجود العسكري الأجنبي، الجيش العراقي وقوات الأمن قادران على تعزيز القدرات الدفاعية وضمان الأمن القومي</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/92363" target="_blank">📅 21:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92362">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYVVgk4gBe-eR6A4GyMUlpvLrToc9iJYBbnbjq8NwCNpSSoOBF7TOWZpy6eu7vokNZeZgW0n7zfJq9RWJT7wc-zURD-Oel2u38ni2N1SOtaROfhZml424vjLAV7kkQhCL6KZ0XvvwJJ0unsPdT3AopEFHdovcaMSYNLvFbWalwapMnCDaOGxVWDw0tht6GAZgzw09plfeAVm19r_nSeGmUygSdJeZvj0LMbse5Bd9rHaV3Rn8O1uJyc7oWo-lhND3BB1Lahmpj5KufdlfKHoXMIS_CBJFjMcPq0jJZi6lr7AUtlQ6cHPHpMCGXCXGRrNAv3dzn0BQ-WTjjON_0Os2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
اسعار النفط تصل الى 102 دولارات للبرميل الواحد.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/92362" target="_blank">📅 21:50 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

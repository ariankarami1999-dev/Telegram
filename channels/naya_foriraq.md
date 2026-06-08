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
<img src="https://cdn4.telesco.pe/file/SxWGQ8aUqoXq7GWuNQ2FH0uR8mtAS546-6l3pTqyYUBIZHuaWFl4s93Hdgkb7Qsrb4XHoFvJt8H5i08BmQf-Qad4pH59szfkmJL3V0eqajM60J8bkFjIGoTVOE6fCXDGWBm_nVCFeOXqdcnelu3FbiMhNlNLe5UeldiIGNajx_PkpgPS2w8S2csFRYU8OTBYM0Co-lAM3Q2i5U94ta21flDGBL9azlq_F63gzGpqzIYZpJXZ-0ezZtr_jyQ3LEXY2HQAi1F3TEdHXl1MxJySM4bkYaWYkqClPHSyxouJyGK-tGaaxkpDrSHrCS3eAiIxjPkUX7iNei6nQkhcjvSZ_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 258K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 18:24:47</div>
<hr>

<div class="tg-post" id="msg-77779">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">كلمة للنتن ياهو بعد قليل</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/naya_foriraq/77779" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77778">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دك سفينة هندية بمسيرة قبالة بحر العرب</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/naya_foriraq/77778" target="_blank">📅 18:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77777">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxGBIaazsJhbay2y_FaM3_nxp2u1yW_NDx-Zl8SL498TU_2FVS5EZwtZTh9z0NJXoRjd2rzctCQ97RxNZvw-QsDzcWwNf_mZR0xifAuDCkPL_av2kH9NHPqIgBiYDT_WyKZvow3MYIzektHx1AatsXTtxdh15YzOjbxDvJnFWUkFWbiPrma0d9G1VwmNT69pTAEuVhmMyxN-b-SUQrugSA6z85wiprFb_usnclNY5YzIqPKhH5PB7Iwvu4IziX5qemsnsEgCqQsoKJMfc8a_3Qg1Y402WZUxGFj1tDh3Pl8SpVP-Zm6E3wz7y5DdjH7InNJIOxaNkJrNmnlwRa2z_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
لقد عطلنا معادلة وقف إطلاق النار على الورق وانتهاكاته المتكررة على أرض الواقع. طالما لم تكن لديك إرادة حقيقية لبناء الثقة، فسيكون رد إيران هو نفسه.</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/naya_foriraq/77777" target="_blank">📅 18:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77776">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏وزير الحرب الصهيوني: أي محاولة إيرانية للربط بين لبنان وإيران ستُواجه بقوة كبيرة</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/naya_foriraq/77776" target="_blank">📅 18:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77775">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏وزير الحرب الصهيوني: أي محاولة إيرانية للربط بين لبنان وإيران ستُواجه بقوة كبيرة</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/naya_foriraq/77775" target="_blank">📅 18:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77774">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🌟
القوات المسلحة اليمنية:
مشاهد من إطلاق دفعة صاروخية على أهداف حساسة للعدو الإسرائيلي في منطقة يافا بفلسطين المحتلة</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/naya_foriraq/77774" target="_blank">📅 18:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77773">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 04-06-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بصاروخٍ موجّه.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/naya_foriraq/77773" target="_blank">📅 18:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77772">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCdgCCLbyW4bJuUrt09BsNaz1tHJTT1wQBvuF6bxKSzqNdJI2JPuwT026c48-MwpW3_416A99hZXdGS5Es05NebQvF-gJkrU4eOgcBiUSkTEtWPBqhOy3eBO9Ok5f4HTDB5n3iODVhNdzHgpGddGiYnkCzLDWvY1zoYZlqZxHBrmD34vnZ4GOSENRz7fauwV0SQoaBGv4oV_A2RfPDJFTPxZyDBATxEBDiOAtRlHQC7SfWpdH26M7WfNYvT4HJ2bRAyRFW1GVNROQ2g4HT0rJ_RRDCgdsMldCyxvUAkwjYsGiY4Z0dRjNAFSNmTwEcMsK_zr6jq7HrD10bpNzSAuUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أمين المجلس الأعلى للأمن القومي
الايراني
:
إذا ارتكب التحالف الشيطاني أي خطأ، فستكون المنطقة جحيماً له
سبعة وأربعون عاماً ومئة يوم من المقاومة، من ساحة الحرب إلى ساحة المدينة، ومن ساحة المدينة إلى ساحة السياسة والدبلوماسية، غيّرت النظام الأمني العالمي.
ابحثوا عن التهديد الموثوق في مكان غير واشنطن وتل أبيب!
إذا عاد التحالف الشيطاني الصهيوني-الأمريكي وارتكب أي خطأ، فستكون المنطقة جحيماً له!
السلام على شهداء الضاحية</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/naya_foriraq/77772" target="_blank">📅 17:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77771">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">صافرات الانذار تدوي في المستوطنات الشمالية بعد هجوم صاروخي لحزب الله</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/naya_foriraq/77771" target="_blank">📅 17:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77770">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INTv7YtwOcYlUigktHT-884hvG9kcxCdae7Go7rw6qoFloYgiDn_khaeQTdH5U6E9Zs1wSLwR439kQXJlv6SdGHp45p1pj50-EdseYTRMkSouODTFmrT4IQHT2uDY_kKqPoKRT2j3x3xsGNwmuPl6nSoBTrtDtxvPe0UZJrdWRKhMzkA8WY-CFoJzywpoeb8JF-FRdXJ7lAX-BheXFFOv5kwcdZcRUFa6Trr6AD-jtSSwNR2BbXUDqay4Zz-rOlEMOLeOEievLIFGwEfZNnRDWu7iAkGiocpRATk2YcNp-wxC6QhdbMy7QJwF0qbuwmvzBIAO_zH1QBWowX0k3M1Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسيرة صهيونية تستهدف سيارة في محيط مركز الصليب الاحمر اللبناني عند مدخل صور الجنوبي.</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/naya_foriraq/77770" target="_blank">📅 17:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77769">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">صافرات الانذار تدوي في المستوطنات الشمالية بعد هجوم صاروخي لحزب الله</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/naya_foriraq/77769" target="_blank">📅 17:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77768">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سي إن إن عن مسؤول أمريكي:
لم نعترض اي صاروخ ايراني ليلا.. لا صحة لمزاعم إسرائيل بأن الولايات المتحدة اعترضت صواريخ باليستية إيرانية أطلقت باتجاه إسرائيل.</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/naya_foriraq/77768" target="_blank">📅 17:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77766">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وزارة الدفاع
السعودية:
صفارات الإنذار التي تم إطلاقها في وقت سابق من اليوم كانت احترازية نتيجة إطلاق صاروخ باليستي من اليمن اختفى بالقرب من الحدود، ولا تزال التحقيقات مستمرة لمعرفة تفاصيل هذا الإطلاق.</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/naya_foriraq/77766" target="_blank">📅 17:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77764">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YhHfo0XyQq-oP9sb_TX462i_WMQwTUPOeTdeeiLkQWQW889qHnAUcj6eyFS4B9HBJfxauCxQmemSe4a7nF70pEVCDJ9c5sT0H_PcaY-YbFhdVaCMHbizTQZwC008GawlJ0nzNjSEpPOdW1d2pzEJcVvYIV3hqz0IHyG65IvHdkn7gUocGWorNgp5zfWSoW8heE647v9Zh3XJX3pwHIOkCZJELdHTN0GDH6dBbIAMfQM9kKeqlVsfaJcTpDBhsC-fh5V65ePwK-prOlver-EU3N14_OB9DldrIJyAc73kjGryNPxv_MxfosPoK_1MK7AqIrjpFDKuOFN3gGEJlz1ALA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QIkCjK56JHukG0AGm0b4kNiWubvTVIkLUzh3zYUsajvDaZBiu5BYZeu8OP71TRNFCepwRiLh1pcBEm-ZvOTjyQkqNE6iYnsO2--ukHZxFkG0SU7JMZNebWPF_f9siP_vi7bJQCDftqgozW_HYG3ELbByBWi51oTEzyOrl0UgJtgYPhhQbiMBupeK_O_ozp9U3uFEKg6OyhDHwdqyErJnFJnhsRkj5e9tPHhBqA6mb_V23y89TG5wuIi2JCyJCzfCJrFMn_uROXmcdI6tf7HDKgtbHH5RaP-DtHut_c3Vyi5EjanXPnD9bwG0NoAyA_BquCaX99tqVjrZqSdFbmuaLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هيئة الإعلام والاتصالات العراقية تقرر وقف (برامج الجريمة) التي تتضمن استجواب المتهمين أو عرض تفاصيل الجرائم ومحاكاتها مؤكدة أن هذه البرامج تنتهك قرينة البراءة وتؤثر على سير العدالة وتشكل خطراً مجتمعياً وتربوياً</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/77764" target="_blank">📅 17:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77763">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اعلام العدو عن مصدر إسرائيلي:
المجلس الوزاري المصغر قرر وقف الهجمات على إيران واستمرار العملية العسكرية في جنوب لبنان</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/77763" target="_blank">📅 17:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77762">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🏴‍☠️
رئيس شعبة الاستخبارات العسكرية الإسرائيلية السابق "تامير هيمان": الرد الإيراني على استهداف الضاحية كان الاختبار الأول لقيادة مجتبى خامنئي، فقد أوفى بوعده بضرب "إسرائيل" بالإضافة إلى توجيه رسالة ثقة للشعب الإيراني.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/77762" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77761">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">📱
شركة "واتساب" تعلن إحباط حملة اختراق وهجمات تصيّد نُسبت لشركة السايبر الإسرائيلية "NSO"، والمنصة تتوجه إلى محكمة فدرالية بطلب لفرض عقوبات على الشركة الإسرائيلية.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/77761" target="_blank">📅 17:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77760">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🏴‍☠️
رئيس شعبة الاستخبارات العسكرية الإسرائيلية السابق "تامير هيمان":
الرد الإيراني على استهداف الضاحية كان الاختبار الأول لقيادة مجتبى خامنئي، فقد أوفى بوعده بضرب "إسرائيل" بالإضافة إلى توجيه رسالة ثقة للشعب الإيراني.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/77760" target="_blank">📅 17:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77759">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏الطيران المدني السوري: استئناف الحركة الجوية والعمليات التشغيلية في مطار دمشق الدولي</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/77759" target="_blank">📅 16:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77757">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو مهدي الجعفري</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqwhBFodsCz97cCCjnbION7tqgZDW6Qqrb-RZHLZdVvhD5GlEYDUFv3m0eRpekNaj_pjZ5jCGx2xGaSOF37HY9t4gWd3qK8nOLHh_IbESPNSH0HmO97xK7l9J29oe3eIhzOih1_ajBjrP28sXihglOX7083I-7YSbcqPTof__qUchj-GdFTG5YspWeCCUANyWl4KkWut8gLoG4cDL0bJ9v6_cMtTCSrOYWL8jwjhDe4pbq1Y-fZQaQ2xIhIlPlfbRXoCT1xmKOID17NCSsKrxZbMKpAFWb1Ks2PpJVR9QWebbNIXhR_hXVM8UQAQIc-7i0ocLSBo9dyVLoVYUqFRXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">في ضوء التطورات الأخيرة، نشير الى ما يلي:
أولاً: إنّ الأجواء العراقية تتعرض لانتهاكات متكررة من قبل الكيان الصهيوني الغاصب، في ظل غياب موقف عراقي رسمي واضح وحازم يرتقي إلى مستوى المسؤولية الوطنية، ويصون سيادة العراق التي لا تُحفظ بالبيانات والشعارات، بل بالمواقف العملية والإجراءات الرادعة.
ثانياً: من حقّ الشعب العراقي أن يسمع إدانة صريحة لا لبس فيها لكل انتهاك يستهدف سيادة بلده، وأن يشهد تحركاً جاداً يحفظ للدولة كرامتها وهيبتها ويؤكد احترام حدودها ومقدراتها الوطنية التي لا تصان بالتجاهل او (التغليس).
ثالثاً: نؤكد أننا في سرايا أولياء الدم على أتمّ الجهوزية والاستعداد، وأن جميع إمكاناتنا قائمة ومهيأة لاستئناف أعمالنا فوراً إذا ما أقدم الأمريكيون على التدخل أو المشاركة مجدداً في أي اعتداء أو تصعيد يستهدف بلدنا أو شعوب المنطقة.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/77757" target="_blank">📅 16:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77756">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">السفير الأمريكي في بيروت:
المنطقة التجريبية جنوبي لبنان ستكون مفتوحة لأبنائها تحت حماية الجيش ولن تتعرض لقصف إسرائيلي، كل ما يحصل في واشنطن يصب في صالح لبنان وإسرائيل ستنسحب وستعيد الأراضي والأسرى</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/77756" target="_blank">📅 16:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77755">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بريطانيا تنصح
بعدم السفر إلى
إسرائيل
تماما</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/77755" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77754">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اعلام العدو عن مسؤول إسرائيلي:
المعركة الكبرى القادمة مع الإدارة الأمريكية ستتركز حول مواصلة فصل الجبهات، ومنع الربط بين مفاوضات طهران-واشنطن وبين جبهة لبنان.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/77754" target="_blank">📅 16:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77753">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏
إذاعة جيش العدو:
غير واضح ما إذا كانت إسرائيل ستقبل بمعادلة "الضاحية والرد الإيراني".</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/77753" target="_blank">📅 16:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77752">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اعلام العدو عن مسؤول إسرائيلي: الجيش سيوقف إطلاق النار في إيران ولكن ليس في جنوب لبنان</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/77752" target="_blank">📅 16:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77751">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
الشركة الإيرانية للمطارات والملاحة الجوية:
عقب إصدار هيئة الطيران المدني إشعارًا رسميًا للطيران (NOTAM) يفيد بإغلاق المجال الجوي الغربي للبلاد، تم إلغاء جميع الرحلات الجوية من مطارات البلاد ولن تُسيّر حتى إشعار آخر.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/77751" target="_blank">📅 16:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77750">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نيويورك تايمز عن مسؤولين عسكريين إسرائيليين: نتنياهو أصدر تعليمات للجيش بوقف الاستعدادات لشن هجوم آخر على إيران</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/77750" target="_blank">📅 16:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77749">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">رئيس منظمة الطوارئ الايرانية:
14 اصابة بالعدوان الصهيوني على البلاد منهم من مدينة ماهشهر بمحافظة خوزستان، وواحد من طهران. لا يزال شخص واحد يتلقى العلاج في المستشفى، بينما غادر 14 مصابًا بعد تلقيهم الرعاية الطبية اللازمة.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/77749" target="_blank">📅 16:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77748">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اعلام العدو: تم رصد ثلاث عمليات إطلاق صواريخ أُطلقت من لبنان. تم اعتراض بعض الصواريخ وسقط صاروخ آخر بالقرب من قواتنا</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/77748" target="_blank">📅 16:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77747">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ايران تفرض معادلة مفادها
الضاحية بيروت امام قصف تل ابيب
اماً المعادلة التي فرضها عون هي عمل صحن كبة نية ..</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/77747" target="_blank">📅 16:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77746">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">الدفاعات الصهيونية تحاول التصدي للهجوم الصاروخي لحزب الله على مستوطنات الشمال</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/77746" target="_blank">📅 15:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77745">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اعلام العدو عن مسؤول إسرائيلي رفيع:
بناءً على طلب ترامب - إسرائيل توقف الهجمات على إيران. الهجمات في جنوب لبنان ستستمر في الأيام القادمة بكامل قوتها. سنقصف أيضًا الضاحية إذا استمرت الهجمات على مستوطناتنا ومواطنينا</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/77745" target="_blank">📅 15:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77744">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇺🇸
🏴‍☠️
السفير الاميركي في لبنان مدافعا عن اسرائيل:
هاجمت الضاحية بالامس بسبب ضربات الحزب باتجاه المستوطنات الشمالية.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/77744" target="_blank">📅 15:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77743">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مصدر أمريكي لـCBS:
الجيش الأمريكي لم يشارك في الهجمات على إيران، وترامب لم يأمر بأي عملية دعم للدفاع عن إسرائيل من هجمات الصواريخ الإيرانية.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/77743" target="_blank">📅 15:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77742">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58b316f312.mp4?token=lsAV3KmVAB3ED62K2r8XzMohOruWXha0TozZ20eD4RP15Ixuqpholh4o3d_B5MB0KW_8u9haHOkRIcdC0Fb1WvbVcc_UfkerWYp-2p_ABo1Xk-fNxLFX9e17diRsdKwKsdZvSBYU1n46B4aKAgeOGsPOR8elqOlnHSx6ncAmlzhCTagF-ghnPEXtpPcPuTY2GD94N5MZ_T_Pp9bwTDv5Xxcy5a7KMUGKfH0kISPv4xtKfny3joFTkmtPXsY0GVq8WOKUSPXQMtPOERPwuVf3zfQ5-JfhQ2Oh4cgsjpaoKjEhwWz6uDu1PxQVgjkLg9I4Q-JsKD1rmXibWyOsrj_e3oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58b316f312.mp4?token=lsAV3KmVAB3ED62K2r8XzMohOruWXha0TozZ20eD4RP15Ixuqpholh4o3d_B5MB0KW_8u9haHOkRIcdC0Fb1WvbVcc_UfkerWYp-2p_ABo1Xk-fNxLFX9e17diRsdKwKsdZvSBYU1n46B4aKAgeOGsPOR8elqOlnHSx6ncAmlzhCTagF-ghnPEXtpPcPuTY2GD94N5MZ_T_Pp9bwTDv5Xxcy5a7KMUGKfH0kISPv4xtKfny3joFTkmtPXsY0GVq8WOKUSPXQMtPOERPwuVf3zfQ5-JfhQ2Oh4cgsjpaoKjEhwWz6uDu1PxQVgjkLg9I4Q-JsKD1rmXibWyOsrj_e3oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اكثر من 5 صواريخ تدك مستوطنات الشمال</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/77742" target="_blank">📅 15:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77741">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">صفارات الإنذار تدوي في كريات شمونه ومحيطها بعد هجوم لحزب الله</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/77741" target="_blank">📅 15:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77740">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">صفارات الإنذار تدوي في كريات شمونه ومحيطها بعد هجوم لحزب الله</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/77740" target="_blank">📅 15:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77739">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">قائد الجيش الإيراني: نحذر بأن أي اعتداء من جانب إسرائيل تتحمل مسؤوليته الولايات المتحدة</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/77739" target="_blank">📅 15:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77738">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏اعلام العدو عن مصدر إسرائيلي: نتنياهو يقول إن الاتصال مع ترمب كان "توافقيا" بالمواقف</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/77738" target="_blank">📅 15:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77737">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇷
وكالة تسنيم:
معادلة جديدة لإيران.. إيران وافقت على وقف إطلاق النار بمعادلة جديدة وبشرط؛ حيث أعلنت إيران أنه في حال استمرار اعتداءات إسرائيل أو استمرار جرائم إسرائيل وأمريكا في لبنان، لن يقتصر الأمر على بيروت فقط بل حتى جنوب لبنان، وسيُستأنف الأمر مجدداً وسترد إيران برد أقوى.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/77737" target="_blank">📅 15:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77736">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDRDSd5-lEqomaNf0wDvAQJKpRXKLYMqsW-Qa4t2va0epDW5HelUtZ9eK5UTP8M987q3_dxZWKhKGYhQaAUAzqA1vVoNLOIJBfUC23kZGtzMVD75s0pve6jPwZNXly7GRgn66J1YJEkSu-9lf3sBv1ki0a3fI-o0vAHZ4dP01VdNbaJ_Joy3EipN_pmiHpft6ezPFPwkurYamsHfbfCHy2rWSih4h-V6-K0FNka1eTuUyVcd3Bhs9DQpnnlmtpChflVN3Ctha8aGYWK3E2mlyFUZs73cknGzYRTdV-HlrBZdShEx1EAMPtlzPr4c6vA2-8JRKTB7PozoK6A37AuXWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غارات صهيونية على جنوب لبنان</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/77736" target="_blank">📅 15:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77735">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سلطة الطيران المدني العراقي تعلن إعادة فتح الأجواء العراقية أمام الرحلات الجوية من وإلى جميع المطارات العراقية واستئناف الحركة الجوية فيها</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/77735" target="_blank">📅 15:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77734">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f58b1745.mp4?token=jFP1uW9JSXlG63p3mmHk3PV7Cl1H1wiwlvUQLRIfL7ajeggbznjnnSEU9nz632yHbzeLlUqC0qsEFVvNbafrjW5g0L70zSYBEhPy8oM2k4OrJM_4J-K7g0RbX6V8xLFt8iDuVJ7dXWCHYU-ylbtfZVknj923aJy2sugY_MxaEn8wDGV7cPfJiFkmahztYabFLoZNvxas_2Et3BjT-H4_T99rvMrCe-Pn-j7gtFUtSbNTdwjFevsIJO59rPYt1-eaS_ibxMWtlmcJcSBGCl64LB2nX30elqT22B67vEsMFfFZYSPHrUX1RQUQSO9ktrPID6ezfMwhJtfyHKZvOLo_ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f58b1745.mp4?token=jFP1uW9JSXlG63p3mmHk3PV7Cl1H1wiwlvUQLRIfL7ajeggbznjnnSEU9nz632yHbzeLlUqC0qsEFVvNbafrjW5g0L70zSYBEhPy8oM2k4OrJM_4J-K7g0RbX6V8xLFt8iDuVJ7dXWCHYU-ylbtfZVknj923aJy2sugY_MxaEn8wDGV7cPfJiFkmahztYabFLoZNvxas_2Et3BjT-H4_T99rvMrCe-Pn-j7gtFUtSbNTdwjFevsIJO59rPYt1-eaS_ibxMWtlmcJcSBGCl64LB2nX30elqT22B67vEsMFfFZYSPHrUX1RQUQSO9ktrPID6ezfMwhJtfyHKZvOLo_ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز اربيل</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/77734" target="_blank">📅 15:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77733">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">انفجارات تهز اربيل</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/77733" target="_blank">📅 15:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77732">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qU_LA3xYbMUBCmk3glOB1OM3AG64S21vYGzymfEHHPrw8RMtTtK-q53aOYSSr7eUELymhhnCLho3slILnMA-zvKVgxJ7kVWbxxDf65eW7l4cgRJDUb0IBGW7X0XcBbzZhXrBRnGAStTgROgpFGfFVrbYu38VQj6bd_DKeB443TIubxM6nYGMRNxR186FubbTu_DRvHKHejW3wtaivOuemQErd3SOwESyynRpzXWpsjNS10w929UvudinCvOQr9UTFSUNuNgyVYVr9i4iHG_6W3xczFcpwzW8oiLeAvTdTNETAWF5TFwCKkNcm0ixlJPq_RJ5KhCzp7mDfUrmvSTTAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة اماراتية تهبط في مطار مهرآباد الايراني بعد حصولها على تصريح خاص رغم ايقاف المطارات الايرانية منذ صباح اليوم.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/77732" target="_blank">📅 15:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77731">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇺🇸
🏴‍☠️
اتصال هاتفي بين ترامب والنتن ياهو</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/77731" target="_blank">📅 15:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77730">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1_dzMA70EzWRLBu8K13GdhuLfWEoQ30Hd6NGcGcAmvXDNoTcSxX_gb6PlF0Z5FMDmydUQVNNAVi6R03q6Uiz29n2uAKxEUE6vl27vkrAKvOsAgv9kC2RbheRvRqQTRlqcQ4qL1-eFMdX4WEc-qKGwCgVE4uEzGxKRnR7TjnuMtnnnr3jiEWytlvkxcRmNnWrmn6y0y2tFxA3TvX1q4HMF-zpIsmAMCebGyG9Oc7r2_ECstQPnQWI8edHOlLoBRKSSavDpR12pSMuSsZovJJS0XLK0MNHTAekWPzCda2TU7da-P3_Zq4odJaBXMfewVCO3o49ZksCG3hXcmtJy2edg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان:
أولويتنا هي الأمن القومي وسلامة الشعب. سندافع عن حقوق الأمة بكل حزم ولن نتراجع أمام أي تهديد. الدبلوماسية والدفاع هما ركيزتا القوة الوطنية؛ لم نتخلَّ عن ساحة المعركة ولا عن طاولة المفاوضات. بإذن الله، بالوحدة والعقلانية، ستجتاز إيران هذا الاختبار بشرف.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77730" target="_blank">📅 15:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77729">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سلطة الطيران المدني العراقي تعلن إعادة فتح الأجواء العراقية أمام الرحلات الجوية من وإلى جميع المطارات العراقية واستئناف الحركة الجوية فيها</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/77729" target="_blank">📅 15:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77728">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اعلام العدو:
يبدو أن: في ساعات المساء من المتوقع أن تعلن قيادة الجبهة الداخلية عن العودة إلى الروتين الكامل في الجبهة الداخلية</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/77728" target="_blank">📅 15:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77727">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اعلام العدو: كانت معادلة إسرائيل هي إطلاق حزب الله النار على الشمال - هجوم في الضاحية
تحاول إيران تغيير ذلك إلى هجوم في جنوب لبنان - هجوم إيراني على إسرائيل
الإيرانيون استجمعوا الشجاعة ويشعرون بالتفوق</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/77727" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77726">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇷
القيادة المركزية لمقر خاتم الأنبياء المركزي يعلن وقف عمليات القوات المسلحة
في أعقاب الاعتداءات والأعمال العدوانية التي نفذها الكيان الصهيوني في جنوب لبنان ومنطقة الضاحية، بدعم من الولايات المتحدة، قامت القوات المسلحة القوية التابعة للجمهورية الإسلامية الإيرانية، في إطار دعم الشعب اللبناني المظلوم، بتوجيه رد مؤلم لهذا الكيان.
ردٌّ كان ينبغي للكيان الصهيوني وحلفائه أن يستخلصوا منه العِبر والدروس.
وبناءً على ذلك، يُعلن وقف عمليات القوات المسلحة؛ مع التأكيد على أنه في حال استمرار الاعتداءات والأعمال العدوانية، بما في ذلك في جنوب لبنان، فإن إجراءات أشد وأقسى وأكثر حسمًا من السابق ستكون في الطريق.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/77726" target="_blank">📅 14:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77725">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">📰
أكسيوس عن مسؤول أمريكي:
واشنطن لم توافق على الضربات الإسرائيلية على إيران وأبلغت نتنياهو بضرورة إنهائها</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/77725" target="_blank">📅 14:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77724">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اعلام العدو:
إسرائيل والولايات المتحدة أرسلتا رسالة لإيران: لن تكون هناك هجمات أخرى إذا لم تطلق إيران النار مجددًا</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/77724" target="_blank">📅 14:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77723">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رئيس الوزراء البريطاني ‏ستارمر: على جميع الأطراف العودة إلى وقف النار، يجب منح المفاوضات بين أميركا وإيران فرصة للنجاح من أجل سلام دائم</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/77723" target="_blank">📅 14:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77722">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🏴‍☠️
🇺🇸
السفير الأميركي في لبنان:
إذا أوقف الحزب هجومه على إسرائيل فهي لن تستهدف الضاحية</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/77722" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77721">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🌟
النائب الأول لرئيس البرلمان العراقي يدعو الحكومة إلى وقف تحويل الأموال لإقليم كردستان لحين إجراء التسوية الكاملة للمستحقات</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/77721" target="_blank">📅 14:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77720">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🏴‍☠️
وزير التربية والتعليم الإسرائيلي:
استمرار تعطيل المدارس غدا الثلاثاء.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/77720" target="_blank">📅 14:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77719">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ما يسمى بـ"المدير العام للوكالة الدولية للطاقة الذرية رفائيل غروسي": المطلوب من إيران الوفاء بتعهداتها والامتناع عن النشاطات غير المشروعة</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/77719" target="_blank">📅 14:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77718">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">عضو الكابينت زئيف إلكين:
ترامب يريد الهدوء، لكنه يدرك أننا لن نقف مكتوفي الأيدي إذا واصلت إيران مهاجمتنا</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/77718" target="_blank">📅 14:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77717">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ff9HcZ1HdWyRXAZOdxOKwqmqmQsGuwFPdgH7Yj8YG4yr4h38j0t1NLbZ2qaMOnnoUoivQdCZ0sqs3Nyl1rj1k8oDutDValkWJ-KGSBm9G9HWlWRgn57IOSaUF6uoeejAdhK6b7oQcnysJxLSjrM54j0Fgi7UfSTTLh90Q06-sVgdkbqXoqKXr0k2U8cPzkYmVGo_vgQzMW9h7vPrhqScBPyY0-95_mOTgBWvWXPu06lwLY8-rbmfiOabef0x1BMstrwawP2D8JRgSpWCXGbluhJCcG2IzvDeakxAJqVeB7GwzdDIeYGpx0CJp4EVSvfFgNOHrziuwfaihMhwS1nYkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: يسعى كلا الجانبين، إسرائيل وإيران، إلى وقف فوري لإطلاق النار! المفاوضات النهائية بشأن "السلام" جارية، مع مراعاة احتمال عرقلة الجهل أو الغباء لها. سيظل الحصار قائمًا، وبكامل قوته وفعاليته، حتى يتم التوصل إلى "اتفاق نهائي". يجب أن تسير الأمور بسرعة.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/77717" target="_blank">📅 14:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77716">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">المتحدث باسم جيش العدو: النظام الإيراني يحمي وكلاءه في لبنان</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/77716" target="_blank">📅 14:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77715">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نقلا عن إعلام العدو ستجتمع الحكومة الصهيونية هذا المساء في الساعة التاسعة.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/77715" target="_blank">📅 13:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77714">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">حركة حماس:
نثمن عالياً الرد الإيراني واليمني على الكيان الصهيوني جرّاء جرائمه بحق لبنان وشعبه.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/77714" target="_blank">📅 13:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77713">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">إذاعة جيش العدو:
منذ حوالي الساعة 7:00 صباحًا، لا توجد معلومات عن هجمات أخرى نفذت في إيران خلال الست ساعات الماضية.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/77713" target="_blank">📅 13:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77712">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 04-06-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقة
أبابيل
انقضاضيّة.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/77712" target="_blank">📅 13:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77711">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38f3eaf5f3.mp4?token=j_-IRLVguDIFv0rWGruRTDoa4EWssCPZThlaGUF3_foMadculLl23QiXhUbL159hbfBQwNW9JUza5lenOOGPRu2Bub-4eS7yfIYYyRNYOQ2bMieh4QQTP9kUO6CA-V_n5YhXxeiuPBFLm1hQ2jfRFYPSGz_sojEGJ9j36AHYXqDrq5b4S-SmUHvwmazx9fDZfOjynewHw3HyWMfgUUXavlgTGbisD_3M9-731ixLdB8hUkijTgmprO68vTkoNppP9kuHX1qYDreeD5WKsSP96CWD103yT5DLtI4fbIrdza6_ecE76P5vBvfa7YTtmqNw7hcRZLQFZNfQtEVjINNz5IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38f3eaf5f3.mp4?token=j_-IRLVguDIFv0rWGruRTDoa4EWssCPZThlaGUF3_foMadculLl23QiXhUbL159hbfBQwNW9JUza5lenOOGPRu2Bub-4eS7yfIYYyRNYOQ2bMieh4QQTP9kUO6CA-V_n5YhXxeiuPBFLm1hQ2jfRFYPSGz_sojEGJ9j36AHYXqDrq5b4S-SmUHvwmazx9fDZfOjynewHw3HyWMfgUUXavlgTGbisD_3M9-731ixLdB8hUkijTgmprO68vTkoNppP9kuHX1qYDreeD5WKsSP96CWD103yT5DLtI4fbIrdza6_ecE76P5vBvfa7YTtmqNw7hcRZLQFZNfQtEVjINNz5IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لبنان لن يصبح لقمة سائغة للصهيونية أبدا وأبدا
الإمام الشهيد القائد علي الخامنئي</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/77711" target="_blank">📅 13:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77710">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دك سفينة هندية بمسيرة قبالة بحر العرب</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/77710" target="_blank">📅 13:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77709">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/77709" target="_blank">📅 13:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77708">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">المتحدث باسم مقر خاتم الانبياء:
- كما وعدنا، أثبتت القوات المسلحة الإيرانية الجبارة، بما فيها الحرس الثوري الإسلامي وجيش الجمهورية الإسلامية الإيرانية، أنها في ذروة استعداداتها الدفاعية والهجومية، تحركت بسرعة ودقة، مما جعل العدوين الأمريكي والصهيوني يندمان على ما فعلاه.
- في الموجة الجديدة من العمليات ضد أهداف مهمة وحساسة في الأراضي المحتلة، تلقى العدو ضربة قاضية من القوات الإيرانية الجبارة، حيث سددت ضربات قوية وموجهة وذكية ومدمرة.
- على أمريكا المجرمة والكيان الصهيوني الوحشي أن يعلما أن إيران قوية شامخة، وأن قوى المقاومة الشريفة في المنطقة ستصمد في وجه أي ظرف وأي تهديد، ولن تستسلم أبدًا للأعداء المهزومين، وإذا استمر العدوان والشر، فسيكون الرد أشد قسوة.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/77708" target="_blank">📅 13:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77707">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odxl-FBjdMCBjHadfg6jbG7vge90_6A5xVWKbQDGv9s1pGiJBajSDlEo06pTVckMuxdvz4WRGP9VkVDNhL0B0bOKwZb2Dz-Ir7z6ft70Pyf8HvQCBUwClrtT6ngbtUDzEEdEAfw7_20dNXoKWtb3l2MNW3m5RbWk67jmEJfLJg73Rh5qMxuiTZ9ceqwBL82jy1Ogybh_TxqCyjHFaMDt0rR5tYCdaQ-9SkLvoatExONb-iySouWAG96KD3BCc5Kd9h3073Q2m2ApsGCLwkie3kR9Po5NBVpswhp9IZUlaK-0eSRF6Gf_PD2XvIBYpC-Rw374Denqdh36EV4FXomy3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Bab Al mandab are close soon</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/77707" target="_blank">📅 13:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77706">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR2tKVcrR-J89lkK1yKZYjoQ4WM900BEER1Ec9CgoVZNBAUVlyU7Jn6GK5_bOPQ06VFmhT3gUgHL2V3_mdaJpCnpPiBQE402w4-OTBx7XHDIrkmg17G6_YGKVanftMp5fywATWkY3GMKmr6J3JrxU8U7sAOdoUi13j8RkQg3Dp5TL--OGalZht2vlXIoyGVcLnX5LI18YP1rZVzweFBy7NtBwdqswmbhZpn4VTuCLJcqdokikvck0D2slw8qujBWPxYW6p1dWTrxYNSHx1H9VkNL0OsUA_h0166OAZnF1mUaZZBvEqgZno0NbCBLFI2osDTGWddNRncxei1ku3-kDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
التخوف حاليا في ايران ودوائر القرار العسكري هو إذا ما قرر الجيش الكويتي الدخول بالحرب .</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/77706" target="_blank">📅 13:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77705">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇷
القائم بأعمال وزارة الدفاع الايرانية:
الكيان الصهيوني بات اليوم أقرب من أي وقت مضى إلى الأفول والانهيار، لن نتراجع لحظة واحدة عن مسار الدفاع عن مصالح البلاد وأمنها حتى معاقبة المعتدي</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/77705" target="_blank">📅 13:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77704">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60051ef060.mp4?token=Xt4oNXi-aXYLUyBFhjAYid1_NUgJNq6AWGb0xFYqqyBvkd2GqjG1f7nRCPp2797E4H5tIP4yd0R9eA9s5qkMtz7VUHIqH2Pcd_-vsHE0kcDz_vL9igN4qxVsY30CxOoU7XM00TsAZIlTjyOKgumaLA8SYLNL6gAH6CV0CKu1-mbJWIzLiYgD0VjeV1xgZHkgCAgvWCh4kwK0b4VHppRyymqZuxxXmZAA7WN8tLh7pz4bHxk1DzklDzzdgdi7uD5L2R723ZExiTcgSeiheeObQK9MY4NDJGbtUWiaBJLTOPMvUInzuQX9FO2ltFp9hk8MncldGk3amHrAcd3XvuNCLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60051ef060.mp4?token=Xt4oNXi-aXYLUyBFhjAYid1_NUgJNq6AWGb0xFYqqyBvkd2GqjG1f7nRCPp2797E4H5tIP4yd0R9eA9s5qkMtz7VUHIqH2Pcd_-vsHE0kcDz_vL9igN4qxVsY30CxOoU7XM00TsAZIlTjyOKgumaLA8SYLNL6gAH6CV0CKu1-mbJWIzLiYgD0VjeV1xgZHkgCAgvWCh4kwK0b4VHppRyymqZuxxXmZAA7WN8tLh7pz4bHxk1DzklDzzdgdi7uD5L2R723ZExiTcgSeiheeObQK9MY4NDJGbtUWiaBJLTOPMvUInzuQX9FO2ltFp9hk8MncldGk3amHrAcd3XvuNCLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">48 ساعة لم يطلق حزب الله اي صاروخ او مسيرة</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/77704" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77703">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تدمير طائرة مسيّرة معادية غرب طهران</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/77703" target="_blank">📅 13:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77702">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnPfX9udDqCXQN5-_BA93Wi-Vi2aTO4wi5TiyDqVVw5KMUJMWJ9BxKe0CcoXdbnxw_TyXNm6LDPrM3yJPIaJpaDZC92dgkreuihItPtzDSmnfpBau3OnQU4Sdw6R50njoAVzYV8jbscubMjJnlNhLn0TC3xzMkT8DSLB0__wH3L3dc8rIG_j90Vp14YU2nOhZJ8uryTqRZhmEcKlSZj0ESaxQuCYPLWTNQWJc92YoEmI2Gt4bmppzHc4WRNgRUBAlbhl66pSBkeWuoivcHqrUcRE_t5einQiBhLgi7EQVQpmSHZfQiwUP1FBnZ22F8GRSog1GD_r556tsW2GlC-zgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب : يجب وقف إطلاق النار فورا</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/77702" target="_blank">📅 13:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77701">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مسؤول أمني إيراني: تصريحات ترامب حول عدم مشاركة أميركا بالهجوم الصهيوني على إيران لا تتوافق مع الحقائق المعروفة</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/77701" target="_blank">📅 12:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77700">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مروحيات أردنية تحلق في اجواء شمال الأردن استعداداً للتصدي لاي مسيرات ايرانية تقترب من الأجواء وتحاول مهاجمة اسرائيل</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/77700" target="_blank">📅 12:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77699">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مسؤول أمني إيراني: تصريحات ترامب حول عدم مشاركة أميركا بالهجوم الصهيوني على إيران لا تتوافق مع الحقائق المعروفة</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/77699" target="_blank">📅 12:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77698">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">يبدو ان أخلاق العرب والمسلمين المبنية على نصرة المظلوم و الوقوف بوجه الحاكم الظالم فقط لدى ايران الصفوية وعراق الرافضة ولبنان شيعة جبل عامل وانصار الله في اليمن …</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/77698" target="_blank">📅 12:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77696">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">جيش العدو:
قد تنضم الجماعات الوكيلة في العراق إلى الحرب.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/77696" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77695">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🏴‍☠️
جيش العدو يوجّه تعليمات للصحفيين العسكريين: الاستعداد لعدة أيام من القتال على الأقل.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/77695" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77694">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚀
وكالة فارس:
إيران استخدمت في هجماتها الليلة الماضية على شمال الأراضي المحتلة صواريخ من الجيل الأخير من نوع خيبرشكن. تصل سرعة هذا النوع من الصواريخ الباليستية أثناء الغوص إلى حوالي 9 ماخ، مما يجعل تدميرها بواسطة أنظمة باهظة الثمن مثل نظام تاد وبيكان أمراً صعباً للغاية. تم استخدام مزيج من صواريخ عماد، قدر إف، وخيبرشكن في هجمات إيران يوم الاثنين.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/77694" target="_blank">📅 12:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77693">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🏴‍☠️
جيش العدو الصهيوني:
من
وجهة نظرنا نحن في استمرار لعملية زئير الأسد - في يومها الثاني والأربعين، بعد توقف دام شهرين. لدينا فرصة لتعزيز الإنجازات. ليس لدينا معادلات. الإيرانيون يحاولون تقييدنا بمعادلات - لكننا لن نسمح لهم بخلق واقع جديد في الشرق الأوسط، عندما تتاح فرص للهجوم في الضاحية في بيروت - ستُستغل هذه الفرص</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/77693" target="_blank">📅 12:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77692">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">شركة Wizz تعلن عن إلغاء جميع الرحلات إلى إسرائيل على الأقل حتى الغد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/77692" target="_blank">📅 12:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77691">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">إسقاط عدد من المسيرات الصهيونية في سماء طهران</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/77691" target="_blank">📅 12:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77690">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3T_UIcDi3goGbaSQxYPJ-Lujh_RLsjpZrpv_M5xbJ6JKwIz7pzg_Mc1O91LUXxRzQZABxkNUo8zO4RAuepOWMfAmaTM57zOqAn742eKoEyoJ0Sl1JcZoTwmmW80fruCTNhWp6fANxWoVzvh3TU_wkdMI5RQD8EMta_oZP5w1gp8BgDBjOrqi60-uNXMk9_oJ6jEXF6_uwC1bFLHTcGB9HMeVovlONr3_rpmtSfFacf_Wil3Zth3T0HGhBNfSrHJKZCK2X6Sqkm_OF2TAVQ2A7tJhXa9HHzSGIc-1_5desuAZaDtw2FjqLRaVlw6FNZzHtHymvHL6WN5cNvJnqjGgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إسقاط عدد من المسيرات الصهيونية في سماء طهران</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/77690" target="_blank">📅 12:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77689">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">"
⭐️
If you have a verified Telegram account with a blue checkmark, we kindly ask you, our esteemed subscriber, to support our channel by promoting the link and sharing updates on the channel."
في حالة تمتلك حساب تلغرام موثق بالعلامة الزرقاء نطلب منكم عزيزنا المشترك دعم رابط قناتنا بعمل تعزيز لغرض نشر حالات على القناة
⭐️
https://t.me/boost/naya_foriraq</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/77689" target="_blank">📅 12:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77688">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3c63c93fb.mp4?token=oq338G26J8JFUZZODnpwFju9qnQerRX9wrPndb9MjJAxmerapL4EAizQWuL-Y_CQwNxfpn8uP4s1R94Y5vy4v7XQb67NFAVXrZrTTRLywjIcbm6hWug4YFgexysZzUMnLmXjEfy2Hou_Kyib8kiPtiX-r_FeMRkGMqtgTk9nK0xL4bGQXDL8puveR-hTz5gEx4KKU2VuZ1WNuqU9XlKNWQk2m7Ojq0NqAQYnuuMaThmaHHH0Gx5Vx6gnNfRPBCnMhq1yN6KJ1OOXS0ZwErqImV9lltdjkLw8bsKCNb5fg8MzB11oLEVYH5P8cmxtrsWa0oiDmkiGV0d3aAVZrML-Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3c63c93fb.mp4?token=oq338G26J8JFUZZODnpwFju9qnQerRX9wrPndb9MjJAxmerapL4EAizQWuL-Y_CQwNxfpn8uP4s1R94Y5vy4v7XQb67NFAVXrZrTTRLywjIcbm6hWug4YFgexysZzUMnLmXjEfy2Hou_Kyib8kiPtiX-r_FeMRkGMqtgTk9nK0xL4bGQXDL8puveR-hTz5gEx4KKU2VuZ1WNuqU9XlKNWQk2m7Ojq0NqAQYnuuMaThmaHHH0Gx5Vx6gnNfRPBCnMhq1yN6KJ1OOXS0ZwErqImV9lltdjkLw8bsKCNb5fg8MzB11oLEVYH5P8cmxtrsWa0oiDmkiGV0d3aAVZrML-Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إسقاط عدد من المسيرات الصهيونية في سماء طهران</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/77688" target="_blank">📅 12:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77687">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">عدوان صهيوني على كرج وطهران</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/77687" target="_blank">📅 12:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77686">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الهند تنصح رعاياها بمغادرة إيران</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/77686" target="_blank">📅 11:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77685">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">إعلام العدو: ‏استهداف مطار شيراز</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/77685" target="_blank">📅 11:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77684">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">هجوم على نقطة تفتيش للباسيج في كبودهارهنك بمحافظة همدان غربي إيران.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/77684" target="_blank">📅 11:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77683">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">إسقاط مسيرة صهيونية في طهران</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/77683" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77681">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c3d2c5467.mp4?token=N3XbBoaT5J11LTUp28Al9dD24W88WruXu783h7z8tEDyp3LLt59RCvnnt3eTz0RH_hWvwSjceJyQq7lTknV9Pfnbbb3bBzKeQKW4TlrddYY_8o5XiqqamNue7iWi4qndHYGFj63gHWQJiOwGI6xVqdp2sc753jCexJFm7RvCXDE7NqVbV1vxV9GRX4uICLsRKlwjDxDWKt_548j5V8ff14HEVtFinywYDNbR_ANwgLiOODVc_mx1wQZxBupJoHZHmezO693RXa0J17XJU9izjqFZipW65AJnAvdLbNSZD-6NCZYH8GMq8YHdzbUFEjwjnfkPPYs5Z6nlhoVxmoalxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c3d2c5467.mp4?token=N3XbBoaT5J11LTUp28Al9dD24W88WruXu783h7z8tEDyp3LLt59RCvnnt3eTz0RH_hWvwSjceJyQq7lTknV9Pfnbbb3bBzKeQKW4TlrddYY_8o5XiqqamNue7iWi4qndHYGFj63gHWQJiOwGI6xVqdp2sc753jCexJFm7RvCXDE7NqVbV1vxV9GRX4uICLsRKlwjDxDWKt_548j5V8ff14HEVtFinywYDNbR_ANwgLiOODVc_mx1wQZxBupJoHZHmezO693RXa0J17XJU9izjqFZipW65AJnAvdLbNSZD-6NCZYH8GMq8YHdzbUFEjwjnfkPPYs5Z6nlhoVxmoalxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوي انفجارات في أصفهان</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/77681" target="_blank">📅 11:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77680">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تفعيل الدفاعات الجوية في طهران</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/77680" target="_blank">📅 11:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77679">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دوي انفجارات في أصفهان</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/77679" target="_blank">📅 11:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77678">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">إطلاق مسيرات من اليمن باتجاه الكيان المحتل</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/77678" target="_blank">📅 11:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77677">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">الدفاعات الصهيونية تسقط صاروخ إيراني في محيط قرية زبيدة بريف القنيطرة السورية</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/77677" target="_blank">📅 11:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77676">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79b3165a7b.mp4?token=s4phfFDbAxNh1TKcvYjtQvaHffmgwEVkQu3YZfvXLcPG0KK2ZyIQL8DoM7EmN_-BBwGy1nsKGUFGqfGEuv4WD9y4yPNsDSqaRgIIp4JuLBP5MrEgNRc_0EEV4jS572DvniG7DqYbMkwAEFvuPz9YE2qx8CveU4SqYcLm_kGu1NqWuZcEhT3JA4jT2mPioKrFHV4my8gVkRODKQRifXN9_q9hgJjQFiSXMSGiQHk5W2oPdHpWmncWeGDi82bUqJrEjnojwsLTFxR1O8HsZYe3EzBAsAWotPXbxs3x0_HW8wy5hSTpxTL77Rs0tUojVJtG1xLm690pJTpN3idxgtV3Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79b3165a7b.mp4?token=s4phfFDbAxNh1TKcvYjtQvaHffmgwEVkQu3YZfvXLcPG0KK2ZyIQL8DoM7EmN_-BBwGy1nsKGUFGqfGEuv4WD9y4yPNsDSqaRgIIp4JuLBP5MrEgNRc_0EEV4jS572DvniG7DqYbMkwAEFvuPz9YE2qx8CveU4SqYcLm_kGu1NqWuZcEhT3JA4jT2mPioKrFHV4my8gVkRODKQRifXN9_q9hgJjQFiSXMSGiQHk5W2oPdHpWmncWeGDi82bUqJrEjnojwsLTFxR1O8HsZYe3EzBAsAWotPXbxs3x0_HW8wy5hSTpxTL77Rs0tUojVJtG1xLm690pJTpN3idxgtV3Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوي انفجارات في أصفهان</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/77676" target="_blank">📅 11:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77675">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تفعيل الدفاعات الجوية في طهران</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/77675" target="_blank">📅 11:39 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

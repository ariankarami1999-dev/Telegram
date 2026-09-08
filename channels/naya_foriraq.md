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
<img src="https://cdn4.telesco.pe/file/aXLDrCXDXLMt8kjygfAojd2LN9q9lfAMvhxzhYmsGKhTXzrPbOcLFEo5eyxUqzVhzCHDHHZTbU_A1JSyZl5D58jgZ2HPnmWJh1UhXgGk_rICgk5eiO_3w3U1pfwhU_SsWIczn4FvvIqWyKGnyNM1eDnsqmtmwDWTKrZ7crv2az3wkH1RFBRpDj8UAOSbEdQPx3Z3fx8LytkqfHvmPPQhixd4hWXRaJNnobn6Uubmm8KJrS-wsoSzNZXB3hiA1IE7DlutvBBLwWX3aeplBY6aDtQUPfhshEVUGI4qLw8DJV8hrvgIwDwfK8JsTlKLNFkuR5zshNVw2_3jIRu5SP1CKw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 02:34:10</div>
<hr>

<div class="tg-post" id="msg-89842">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZPORxTAHBzMOGiRNQDSar7KtzkGmFnSd4T9Urm_UHi2TRg4XZ6rkMa6GYLVXBveZNowWwJdHcRFN7aQumTonvBTHhbuzE45oRP9c-g5VQ3M3xRjBdq63tgLzn07foqubAb0U_L1HjIhLK7e6uw5gT30JuP134uSBki4ajLOvF0Ey1mBA926Ihs4mvSoqS9Rr20lqDEPxfeN-2J6rfGkBAoc9hvXXmILHF8yPErSBc5AT464tu0k1_3i_LNthLSWDVtvXGiVmUTkb5E_5bI1mS016XFrN4IX04BqlE4IyN_69vOBpr1bLqjKk2kScpzD2xpOTnigIVtGoHXUyCR_qPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nb5Dutt-3QshDWUpqxZZslYQ27uERKDv_ML-zkKlSZsvAgwT_urbLx--gxr_VzJG0F6i6QYFrls521jj-JllvIHXG6YSZIoPVKwJh6-F0OXBFOzj-rMA0jy4e3zGSa846zB1NNa_cCnhbzj5hSKYoR2lHEIywNcrzU2fYx4uRmwiGfkaS2G1PNERCoAkniIeNYQjW6VOmePHobEqoxiIW-W3y2GxMVAKVuwMo4MGHqBg-SLmun6an6x9b4lhf-D9_HB6FC3htLWO4I8EMapWh_fCdK5MpB48znbnmYK6wQQWpLZDLZxTvjhh_Bu5StwFEzYlfTuT2VgkSLoUvxaQ8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عضو في هيئة المهندسين السعوديين يقدم شكوى لوزارة الخارجية السعودية بسبب قيام مسؤول سعودي رفيع في الخارجية السعودية بالطعن بعرض السفيرة العراقية في الرياض صفية سهيل التميمي ومطالبات لتدخل الجهات العراقية المختصة ومتابعة القضية بما يضمن حفظ مكانة السفيرة العراقية وكرامتها</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/naya_foriraq/89842" target="_blank">📅 02:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89841">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔻
مشاهد لإطلاق وابل من الصواريخ ذات الوقود الصلب والسائل على معاقل الشر الأمريكية، بما في ذلك القاعدة العسكرية الأردنية "الأزرق".</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/naya_foriraq/89841" target="_blank">📅 02:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89840">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔻
مصدر أمني من الحرس الثوري لنايا
شاركت بريطانيا و فرنسا بجانب امريكا وألمانيا واسرائيل بمحاولة صد الهجوم على الأردن ؛ انطلقت مقاتلات من قبرص قاعدة اكتوريا باتجاه الأردن لصد الهجوم .</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/naya_foriraq/89840" target="_blank">📅 02:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89839">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔻
مشاهد لإطلاق وابل من الصواريخ ذات الوقود الصلب والسائل على معاقل الشر الأمريكية، بما في ذلك القاعدة العسكرية الأردنية "الأزرق".</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/naya_foriraq/89839" target="_blank">📅 02:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89838">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLDFLG3b-ZYrGAxVP1DQe3vqVA1hOhDG2OQ2Ir7KtFTo0h6OxfohHCWotc8HgAn3K4lp7JwjMT6r9IkDPGxuKxUeeASwjSyRJ-BjQ12yWgGShj1qrih5W465UwEtBiDMHsMzbahY7hzto1WV9TQmwTNAZ9sH8ASwZdGf3FONeWRD454coMZQMA79FRx-DkPwEEAHL2jDL9H_PKjvSy6lrrE9_zSfX22Zdza0H2PQ9K4S9g_t1bv4fAulQS9vKHvx-FxrwQj_uS7MYzbc5MK_wLZQu1uSN_df9k5Cs9LfocuQplHzlEwn82PmEBY90UihZ9oL8u5veQcQ4v_igbYtrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Losing around 100 PAC-3 missiles will certainly cause serious concern and sleepless nights for the Trump administration, Israel, and the U.S. military, especially the soldiers stationed at U.S. bases.
Meanwhile, there is someone currently in Kyiv listening to mournful Shia religious lamentations.”</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/naya_foriraq/89838" target="_blank">📅 02:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89837">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">حدث امني بحري بالقرب من مضيق هرمز.</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/naya_foriraq/89837" target="_blank">📅 02:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89836">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حدث امني بحري بالقرب من مضيق هرمز.</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/naya_foriraq/89836" target="_blank">📅 02:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89835">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الحرس الثوري:  بسم الله الرحمن الرحيم "قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَ يَخْزِهِمْ وَ يَنصُرْكُمْ عَلَيْهِمْ وَ يَشْفِ صُدُورَ قَوْمٍ مُّؤْمِنِين"
🔹
أيها الشعب الإيراني الإسلامي الشجاع والنبيل؛ إن استمرار وجودكم في الميدان قد أرهق وأحبط…</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/naya_foriraq/89835" target="_blank">📅 02:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89834">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">الحرس الثوري:
بسم الله الرحمن الرحيم
"قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَ يَخْزِهِمْ وَ يَنصُرْكُمْ عَلَيْهِمْ وَ يَشْفِ صُدُورَ قَوْمٍ مُّؤْمِنِين"
🔹
أيها الشعب الإيراني الإسلامي الشجاع والنبيل؛
إن استمرار وجودكم في الميدان قد أرهق وأحبط العدو الأمريكي، ومقاومة وقوة أبنائكم الأبطال المقاتلين في مضيق هرمز قد أزعجت وأربكت قادة البيت الأبيض.
🔹
الجيش الإرهابي والمتجاوز الأمريكي، الذي مني بالهزيمة، هاجم بشكل يائس بعض السفن التجارية النفطية الإيرانية الإسلامية.
🔹
وبفضل عناية الله المتعال، وتحت رعاية الإمام المهدي (عج)، أروحنا فداه، وانتقامًا للهجوم الذي شنته أمريكا على ناقلات النفط الإيرانية، قام مقاتلو القوة الجوية التابعة لحرس الثورة الإسلامية بعملية "تأديب المعتدين" تحت شعار "يا حيدر الكرار"، حيث استهدفوا قاعدة الأزرق الأردنية بصواريخ ثقيلة.
🔹
في هذه العملية، التي تهدف إلى تأديب المعتدين، أصابت صواريخ باليستية صلبة وسائلة موقع صيانة وإصلاح، وموقع تجهيز وموقع استقرار طائرات مقاتلة من طراز F-35، وF-16، وF-15، بالإضافة إلى ملاجئ الطائرات، مما ألحق أضرارًا جسيمة بالعدو.
🔹
وفي مواجهة القوة البحرية البطلة والقوية التابعة لحرس الثورة الإسلامية في مضيق هرمز، لجأ العدو، من موضع الضعف والعجز، إلى حركات يائسة، وتلقى على الفور ردًا قاطعًا.
🔹
إن يقظة ومعركة المقاتلين في القوات المسلحة ضد العدو المعتدي يومًا بعد يوم، حتى يتوقف التعدي، قد أثمرت.
هذه المعركة القوية ستستمر.
"وَمَا النَّصْرُ إِلَّا مِنْ عِنْدِ اللَّهِ الْعَزِيزِ الْحَكِيمِ"</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/naya_foriraq/89834" target="_blank">📅 02:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89833">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مصدر إيراني لنايا   اصابة مباشرة لسفينة أمريكية في خليج فارس</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/89833" target="_blank">📅 01:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89829">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6f5c58e8d.mp4?token=CLaYBBcnHKxqQjQTzqBS2Jf4lDWEnjOZOEEsLhFw6shiOW49-Ld1zUKkAzYPgvagatiDfu7w49pJ3yoh_39Bd4Ye3brh4W8yC-Xilr11kvbFMPlnjy9vtP70nvBBF7CaUOAZDF2WeSB-3HkIOaLMaAQvQnH2xPR8aK1Yj46BITYNhl6ysI7YCzIe4nm32S9PwEqt6l-NA4jmDvqScAbOGECPptLPejyz-vpi2R_S30Tpkj2t03HWlBeCJj2rwStOKR6AibIe2hzJ9Il8BLse4Vaip2BS6VeXN2LA9ndH1WKEjwkrwd1Y5mLTylYFrvPQzu7UGW0sL5VsmR5CAmLo8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6f5c58e8d.mp4?token=CLaYBBcnHKxqQjQTzqBS2Jf4lDWEnjOZOEEsLhFw6shiOW49-Ld1zUKkAzYPgvagatiDfu7w49pJ3yoh_39Bd4Ye3brh4W8yC-Xilr11kvbFMPlnjy9vtP70nvBBF7CaUOAZDF2WeSB-3HkIOaLMaAQvQnH2xPR8aK1Yj46BITYNhl6ysI7YCzIe4nm32S9PwEqt6l-NA4jmDvqScAbOGECPptLPejyz-vpi2R_S30Tpkj2t03HWlBeCJj2rwStOKR6AibIe2hzJ9Il8BLse4Vaip2BS6VeXN2LA9ndH1WKEjwkrwd1Y5mLTylYFrvPQzu7UGW0sL5VsmR5CAmLo8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة سقوط المباشر للصواريخ الايرانية في قاعدة الازرق بالاردن</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/89829" target="_blank">📅 01:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89828">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مصدر اردني لنايا
تم نقل عدد كبير من الجنود الأمريكان الجرحى وهناك اصابات ميئوس منها باتجاه قاعدة درمشتاين في المانيا نتيجة اصابة قاعدة الأزرق والمفرق بالصواريخ الإيرانية ..</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/89828" target="_blank">📅 01:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89827">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f58a294cbc.mp4?token=SAhYuFkPp8QPOAh0c4wMWxRMG7iZKOu8-eBwzSdwqMUTU9VZxfI5KI0e94oPExod2REVbqauEFC6cYGOegSRHolEWLFu04LANdz5OiBm3QTtATIkTgLUdBpBd5gn7qb1jREmCjvWzIZZFbwmBkVZ4worr7IGFMmjOJLqzZzPK3W1LFhnFhb9MYUQL0X6PtoysiJJSy2axKBEPW8zf_8qPcfPXLqWrdEYn4291ybVNT9ZR510RFJt7rx-dWw3kSgP3MA04fxMJRx_1YGOPlZ7NWZgvRmwBf0qthd7mP3TZvWhS4ej9WkANu2G4QsGuYjmqNA3nEZqezTOZDKl9KxoGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f58a294cbc.mp4?token=SAhYuFkPp8QPOAh0c4wMWxRMG7iZKOu8-eBwzSdwqMUTU9VZxfI5KI0e94oPExod2REVbqauEFC6cYGOegSRHolEWLFu04LANdz5OiBm3QTtATIkTgLUdBpBd5gn7qb1jREmCjvWzIZZFbwmBkVZ4worr7IGFMmjOJLqzZzPK3W1LFhnFhb9MYUQL0X6PtoysiJJSy2axKBEPW8zf_8qPcfPXLqWrdEYn4291ybVNT9ZR510RFJt7rx-dWw3kSgP3MA04fxMJRx_1YGOPlZ7NWZgvRmwBf0qthd7mP3TZvWhS4ej9WkANu2G4QsGuYjmqNA3nEZqezTOZDKl9KxoGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نيويورك تايمز: جنود أمريكيون أصيبوا في إطلاق النار الإيراني باتجاه الأردن.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/89827" target="_blank">📅 01:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89826">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/89826" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">واحد معطب السرفة و واحد معطب الهمر
#شاركها</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/89826" target="_blank">📅 01:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89824">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8373741233.mp4?token=aNqsCpvoHoAEueMKAGAK5D9Ur2MpLGZBQPnyt8JQwaD4WbWThKZalbWYl-WPUycrYz6xFsXFn8jZFpyU9JkRKbI7j3oF0xtkUOymB3GPMc5TSBpPFUQoT9XmFXATpvegDm0SYKqQ3HIylvruDz-UM2R4n7DDEwBmFsKteYhUXrh3GfqYXGzJuO-gGr2nDFuMb-Ojx34zGlVLmsemYw-o_IDLhQ_AotjDIiFxX_dONhWbv78Vpr2SD6YBYafoc1osPpf-QMIkmUwgOzkS4Iw-EjBhAOdCLgz8jaP4k3e4hX1SveCKAVMDhY4vSDoc47bdPqzKp_LJaaSIv_RQO41pNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8373741233.mp4?token=aNqsCpvoHoAEueMKAGAK5D9Ur2MpLGZBQPnyt8JQwaD4WbWThKZalbWYl-WPUycrYz6xFsXFn8jZFpyU9JkRKbI7j3oF0xtkUOymB3GPMc5TSBpPFUQoT9XmFXATpvegDm0SYKqQ3HIylvruDz-UM2R4n7DDEwBmFsKteYhUXrh3GfqYXGzJuO-gGr2nDFuMb-Ojx34zGlVLmsemYw-o_IDLhQ_AotjDIiFxX_dONhWbv78Vpr2SD6YBYafoc1osPpf-QMIkmUwgOzkS4Iw-EjBhAOdCLgz8jaP4k3e4hX1SveCKAVMDhY4vSDoc47bdPqzKp_LJaaSIv_RQO41pNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/89824" target="_blank">📅 01:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89823">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الله أكبر  مصدر أردني لنايا: إصابات مباشرة للصواريخ الإيرانية داخل القواعد الأمريكية في الأردن؛ سقوط قتلى وجرحى بصفوف القوات الأمريكية.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/89823" target="_blank">📅 01:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89822">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">الله أكبر  مصدر أردني لنايا: إصابات مباشرة للصواريخ الإيرانية داخل القواعد الأمريكية في الأردن؛ سقوط قتلى وجرحى بصفوف القوات الأمريكية.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/89822" target="_blank">📅 01:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89820">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">الله أكبر  مصدر أردني لنايا: إصابات مباشرة للصواريخ الإيرانية داخل القواعد الأمريكية في الأردن؛ سقوط قتلى وجرحى بصفوف القوات الأمريكية.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/89820" target="_blank">📅 01:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89819">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/89819" target="_blank">📅 01:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89818">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7e8feb957.mp4?token=Doo6_2yzikeBz2AiOqDKnpacKFtBCLu0bvjwScb_3hKpo1OoD570MMqSjpGwXNijtXcnR_QQFd6CARcPI4ZCQ6g1fGoqb6Y0EsgJwhnINDN3ym5E8rX3tTcRBRccs7O2gC5plhexfIq7BjLfo6llliCClkJ9DZ9iPepAbD57H3mONem1eykPYiLJoIvGe_bJB8ie4S-fOa2iChmv3HEMJlTb1uJBPHSwMuliWGxKf3PKe5hUMsMfnrxHVQcXfxnekHmV1fjkVhyUnTbKmJ3qMrddI16ju2unZjkLwSkgmlDponMwtFLKcRGnrnuXN2ooYIKbvdseASGpFvZzb1jtcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7e8feb957.mp4?token=Doo6_2yzikeBz2AiOqDKnpacKFtBCLu0bvjwScb_3hKpo1OoD570MMqSjpGwXNijtXcnR_QQFd6CARcPI4ZCQ6g1fGoqb6Y0EsgJwhnINDN3ym5E8rX3tTcRBRccs7O2gC5plhexfIq7BjLfo6llliCClkJ9DZ9iPepAbD57H3mONem1eykPYiLJoIvGe_bJB8ie4S-fOa2iChmv3HEMJlTb1uJBPHSwMuliWGxKf3PKe5hUMsMfnrxHVQcXfxnekHmV1fjkVhyUnTbKmJ3qMrddI16ju2unZjkLwSkgmlDponMwtFLKcRGnrnuXN2ooYIKbvdseASGpFvZzb1jtcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد حصرية لنايا...  مشاهد أخرى من إطلاق رشقات إضافية باتجاه قواعد الاحتلال في المنطقة. https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/89818" target="_blank">📅 01:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89817">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الجيش الأمريكي: ‏أعلنت القيادة المركزية الأمريكية أن القوات الأمريكية دمرت خمس ناقلات نفط خام إيرانية في 8 سبتمبر/أيلول، وذلك بعد هجومين صاروخيين باليستيين شنهما الحرس الثوري الإيراني على سفينة حربية تابعة للبحرية الأمريكية خلال يومين. وقد نجت السفينة من الهجومين، ولم يُصب أي من أفراد القوات الأمريكية بأذى.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/89817" target="_blank">📅 01:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89814">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">الله اكبر
زاوية صفر مشاهد بعد قليل من إطلاق صاروخ باتجاه الأزرق</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/89814" target="_blank">📅 01:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89813">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">الله أكبر
مصدر أردني لنايا:
إصابات مباشرة للصواريخ الإيرانية داخل القواعد الأمريكية في الأردن؛ سقوط قتلى وجرحى بصفوف القوات الأمريكية.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/89813" target="_blank">📅 01:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89812">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55abf77586.mp4?token=oqq1ZC4_frEYOn2-TfawTiC1M3GG4RRMH_kY8Nu4uZMTNe9OjcBN5hVlceuEM_O4z2asxiMXS1ybbmQpRH9SqweslwgEdGDdNJNqObWkk99lKa-nYr8kuGiqQjIgB_XYKTi714n1PW7QSXk_rm-A8FnHyxEcEqEeKLtR_qkV_gJmnLc6x6dw3mSdmagJue5AcT-KyInFYzo9f1ojvK3qZBm92FeuEIlh031jKxQOSJohdETL-YoQWClO_r3UYosXtTXJ7jxnJ66FXLhIDe0c5piOvi_hci1xYg9BcXp3p2mWcJTAX63gKQCdsMwIc2fhw-D0sop7X5SLq2aJFxjuNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55abf77586.mp4?token=oqq1ZC4_frEYOn2-TfawTiC1M3GG4RRMH_kY8Nu4uZMTNe9OjcBN5hVlceuEM_O4z2asxiMXS1ybbmQpRH9SqweslwgEdGDdNJNqObWkk99lKa-nYr8kuGiqQjIgB_XYKTi714n1PW7QSXk_rm-A8FnHyxEcEqEeKLtR_qkV_gJmnLc6x6dw3mSdmagJue5AcT-KyInFYzo9f1ojvK3qZBm92FeuEIlh031jKxQOSJohdETL-YoQWClO_r3UYosXtTXJ7jxnJ66FXLhIDe0c5piOvi_hci1xYg9BcXp3p2mWcJTAX63gKQCdsMwIc2fhw-D0sop7X5SLq2aJFxjuNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محاولات
اعتراضات للصواريخ الايرانية فوق محافظة درعا السورية</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/89812" target="_blank">📅 01:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89811">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHl0Gxb7N1S_tGl2nH6qABnwpuMtOCbGU5XFHqyVdDDAnpYiPIPJFttA0exo2noEfwOll5q4SwfrhcXnmSgmocbYjRiRP0vMAqAl-YmJmCVg79yEwz-B764nAK9up0iCpLJxXgg76xZf-geeI1Fxw9YVU7TXZ3fAdAdRWX8QwoeaEJXTLyxhVhQfQvkvJONjoEhSuzi4_V-HXYyFfsESdRy57PUA_y5z_8srbvmK-1CxPkFy_3UUsNrjwiRnWs24NDf_qbI7WTcHGIC2RacY4pCvzJFs7IC5h4EYRfhpMAWokcjufCeouKtG7PKDuCH9paPOAGisLNPxay_qyN1qcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">النفط يشارف على عبور ال ١٠٠ دولار للبرميل الواحد</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/89811" target="_blank">📅 01:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89810">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a4cfc34c.mp4?token=pderhcOMSsmI8sFhgDxQJ2khwWijYvhKCV6tbwJGsA0bWIflq7l-0AKGUOiAJZz5jw68ZqaAmgPs_WKYVTzFz2Ss5hTVys50Y1_GbJwg1UlPMgWg3atCGcvCPqWbhURzfbLOb0SGGdKdMgv8d2G1LvPCkXtbRNp-qmf5p2xApBVfwmYtOTFasjBWC30Ik_Xqn-nPeiXtnxW_oZOcWylvgzMK7xojywX4i0TVb7X0VN9F3kDFow_ZD8lHg3bSF0fMw7-e83cAN6_8AAuZx2AJe2caKesZYKOrNsggXHmFZ7QeBZ9_dC6-EzM1JoSy8iUajIjJK0IZGvYaB9H8yx3nnrJBaT5BgCStmjJfIiYNNjOEkcd4thAgK2r9RujpsjwsXaKcTENulQlCMH8PDlayLbnqzYOazqCzj-3P118SveNQuQJxUU_l-SyDADyMxKxsyI6y0Zs1-sClZ6OdHsfX9-V_NzlvKlsFBgR7OCKAJ6PhUeo-E5mas2bCkKugFWh_rdEvEp5yK4ZGxORBp9dSdPuANuOFIuGAtBLwklz-wDaz6p4sJncfjuHiU_-T2L5Q872uRN55-J-qY-ZJUlWZk-KzRZmBE8LwijV3ZNBPxhWcOM3KgBJ69dS-8so1tucFD6XuSi7uAliDZMwdMbApYPFUrRLp85hJcPlYrheKvMM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a4cfc34c.mp4?token=pderhcOMSsmI8sFhgDxQJ2khwWijYvhKCV6tbwJGsA0bWIflq7l-0AKGUOiAJZz5jw68ZqaAmgPs_WKYVTzFz2Ss5hTVys50Y1_GbJwg1UlPMgWg3atCGcvCPqWbhURzfbLOb0SGGdKdMgv8d2G1LvPCkXtbRNp-qmf5p2xApBVfwmYtOTFasjBWC30Ik_Xqn-nPeiXtnxW_oZOcWylvgzMK7xojywX4i0TVb7X0VN9F3kDFow_ZD8lHg3bSF0fMw7-e83cAN6_8AAuZx2AJe2caKesZYKOrNsggXHmFZ7QeBZ9_dC6-EzM1JoSy8iUajIjJK0IZGvYaB9H8yx3nnrJBaT5BgCStmjJfIiYNNjOEkcd4thAgK2r9RujpsjwsXaKcTENulQlCMH8PDlayLbnqzYOazqCzj-3P118SveNQuQJxUU_l-SyDADyMxKxsyI6y0Zs1-sClZ6OdHsfX9-V_NzlvKlsFBgR7OCKAJ6PhUeo-E5mas2bCkKugFWh_rdEvEp5yK4ZGxORBp9dSdPuANuOFIuGAtBLwklz-wDaz6p4sJncfjuHiU_-T2L5Q872uRN55-J-qY-ZJUlWZk-KzRZmBE8LwijV3ZNBPxhWcOM3KgBJ69dS-8so1tucFD6XuSi7uAliDZMwdMbApYPFUrRLp85hJcPlYrheKvMM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انقضاض الصواريخ الإيرانية على القواعد الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/89810" target="_blank">📅 01:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89809">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejq5YAH148AX1cSDYe429Tlt-6OJ1u-KCqJs7CY1IzdxfvfhXylTUv3Nhs2Smav4DNtEHBnhaOPbwrDxgOHTQXqqSqr6MA1s-mCiLrYTrL60LTZjA6Vr2jnLC3yadJNp9zlN60Zh6PkuWmnU0FotPxnybttWE5bYdezA_-5F4NfcEVpYTnI740mHGg_lCCs-4kAXV8-A_1fJE24HF_vKojtNaAV9o66R0noaf-1EotQJzOCR_cYo35uQat8ZLjzWPx0DiIWqX78xbHRYZYPxHiX3SgTUs5vj5Ke-KzDLUtUEiCtYmewqns9fIC5hkkfZxkBcG7_pjhlh-EpuTby1Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">النفط يشارف على عبور ال ١٠٠ دولار للبرميل الواحد</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/89809" target="_blank">📅 01:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89808">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-text">🔻
شلیک موج جدید موشکی تا دقایقی دیگر .. چشمهایتان رو به آسمان باشد
@Naya_Press</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/89808" target="_blank">📅 01:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89807">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9c8f0a275.mp4?token=EhAQuoQaon0tQu17GMquLyXRpcABb_HLEw026nWvg9ki3Dc2MqeqkUycqFJ718UwXITyc74EUWZPas5c-yDow-R_F-ZH0c2eaNQmE0-m7nQZgLQBouX6QUEu-xkUaNyRLUezz0s3PM5Zz0Uzf6AlDUS54pRspd-aiwRkrF-5YivwbjaUAlFJr-oczQ-idNwHHPIbD5ICuuppWZR1MPPdXH7jmHTs2iWjNU32HjiKlPPeE4_11GREIlvvikvwKukXwFl9T0iMOgTFFmG4Zx1Nyb-iwZNeH3GUnBmkvpL0i9Lz2Pa8LhTQ9VjMJ667mjOJiQmYQzkiu6TiaEoyhpbfbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9c8f0a275.mp4?token=EhAQuoQaon0tQu17GMquLyXRpcABb_HLEw026nWvg9ki3Dc2MqeqkUycqFJ718UwXITyc74EUWZPas5c-yDow-R_F-ZH0c2eaNQmE0-m7nQZgLQBouX6QUEu-xkUaNyRLUezz0s3PM5Zz0Uzf6AlDUS54pRspd-aiwRkrF-5YivwbjaUAlFJr-oczQ-idNwHHPIbD5ICuuppWZR1MPPdXH7jmHTs2iWjNU32HjiKlPPeE4_11GREIlvvikvwKukXwFl9T0iMOgTFFmG4Zx1Nyb-iwZNeH3GUnBmkvpL0i9Lz2Pa8LhTQ9VjMJ667mjOJiQmYQzkiu6TiaEoyhpbfbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد حصرية لنايا...  لحظة اطلاق عدة رشقات صاروخية من الجمهورية الاسلامية الايرانية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/89807" target="_blank">📅 01:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89806">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-text">🔻
🔻
🔻
پاسخ فرزندان ایران همچنان ادامه دارد
..
@Naya_Press</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/89806" target="_blank">📅 01:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89805">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">الرد مستمر حتى اللحظة</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/89805" target="_blank">📅 01:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89804">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f647b1c5e6.mp4?token=rPFhZfT5kDfj47CTjlF-ca51HcI6H1R1TipcUazfT5vvE66kuXa5jv-2ZxQMubdOzn3DZ6y9rHGvcOVaP7EyTCJcYpz-0d6UgkT7VqaVlvSnlIRBVhuOyyESmnP2al5vMtB4RdRqQusPa-_4zGIzhTbzcMFB9EVt1MxaaBoGHNF9FOZkV2uvo9qpTZ1h0RM2qxb-d2hbaRAZDwdChWuB74HCIhCYa61V88hFN3FdQLgjSX1x9pw1MtkNG1N5P8nxls6HiGziFKRLJaVbc92R2UXcqS7fworfd7l3CyYE4eHv9nGrbC0BXu4EF4oAXzMv4gjpltZcP-YFhJYOWTNWhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f647b1c5e6.mp4?token=rPFhZfT5kDfj47CTjlF-ca51HcI6H1R1TipcUazfT5vvE66kuXa5jv-2ZxQMubdOzn3DZ6y9rHGvcOVaP7EyTCJcYpz-0d6UgkT7VqaVlvSnlIRBVhuOyyESmnP2al5vMtB4RdRqQusPa-_4zGIzhTbzcMFB9EVt1MxaaBoGHNF9FOZkV2uvo9qpTZ1h0RM2qxb-d2hbaRAZDwdChWuB74HCIhCYa61V88hFN3FdQLgjSX1x9pw1MtkNG1N5P8nxls6HiGziFKRLJaVbc92R2UXcqS7fworfd7l3CyYE4eHv9nGrbC0BXu4EF4oAXzMv4gjpltZcP-YFhJYOWTNWhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بارش موشکی بر سر تروریست‌های آمریکایی در اردن</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/89804" target="_blank">📅 01:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89803">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/665d19bf87.mp4?token=gDSSZYq7NDQcF-zw25PNAqP_7RikarZ8CKbe8FVefP5VQCdPgmYOQXMZz2CO9BHsgOct4VbTWRRz7xhEKp6kSGN0aPHWcRKFE64LdSTXq5_FQEMHbGtgmiC0Q3MNwyN6iojEc9OUPsqlqpGcg50GifBQMiWzub-TR2De67hc_g1_sphp6DTeecqXVlUuumhk833zHAwy8kgYXDsrlK21JX8duoFAzttHsJ053SFm7tOYTJ_SElrcX5EAyy2qpWuUHln36pCeJxoCCkY9YnsJB1f7THNeCSF9dAQZ34kE2psc6eZvB00G0zges13VzDzAEPObseQzt93qfWpbm-fuQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/665d19bf87.mp4?token=gDSSZYq7NDQcF-zw25PNAqP_7RikarZ8CKbe8FVefP5VQCdPgmYOQXMZz2CO9BHsgOct4VbTWRRz7xhEKp6kSGN0aPHWcRKFE64LdSTXq5_FQEMHbGtgmiC0Q3MNwyN6iojEc9OUPsqlqpGcg50GifBQMiWzub-TR2De67hc_g1_sphp6DTeecqXVlUuumhk833zHAwy8kgYXDsrlK21JX8duoFAzttHsJ053SFm7tOYTJ_SElrcX5EAyy2qpWuUHln36pCeJxoCCkY9YnsJB1f7THNeCSF9dAQZ34kE2psc6eZvB00G0zges13VzDzAEPObseQzt93qfWpbm-fuQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الهجوم الصاروخي العنف الذي دك القواعد الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/89803" target="_blank">📅 01:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89802">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d045fa19a.mp4?token=TZu0gtUiLmbxbaj1urAOfvDEXHji2_fobAeJtk_M14UPNuN1utjBAXVeYCR4821cFRyYDD1gZmxuVv2u-VaJPTvfVRqr8xKFtyMs3dXdQHLwI4PZBUdNvjwawnuEFtuQzQ8nQrzXQBA-kzkCSe8ggJEepAHkfqitFLGcYB836x0v67FuwsQLTXxdhHu9UF8rDdQtzsqwc-fUSG8BwRSg2J-zZ0CLMrEzB5ZgpcjkygQMpgEs0nUy0XquRT7Nf4AvAInS5tnjlZvJlvQlgx3IF7l9gdJRDyDVFVbC4hIwfTs1TPID9ft7AVsunaQ9p1IT_Kf72qsqOlX60_O07T7Rdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d045fa19a.mp4?token=TZu0gtUiLmbxbaj1urAOfvDEXHji2_fobAeJtk_M14UPNuN1utjBAXVeYCR4821cFRyYDD1gZmxuVv2u-VaJPTvfVRqr8xKFtyMs3dXdQHLwI4PZBUdNvjwawnuEFtuQzQ8nQrzXQBA-kzkCSe8ggJEepAHkfqitFLGcYB836x0v67FuwsQLTXxdhHu9UF8rDdQtzsqwc-fUSG8BwRSg2J-zZ0CLMrEzB5ZgpcjkygQMpgEs0nUy0XquRT7Nf4AvAInS5tnjlZvJlvQlgx3IF7l9gdJRDyDVFVbC4hIwfTs1TPID9ft7AVsunaQ9p1IT_Kf72qsqOlX60_O07T7Rdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الهجوم الصاروخي العنف الذي دك القواعد الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/89802" target="_blank">📅 01:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89801">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مصدر محلي لنايا
اكثر من ٥٠ عمليات إطلاق من منظومة الباترويت في قاعدة الأزرق</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/89801" target="_blank">📅 01:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89800">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مصدر محلي لنايا في الأردن
اغلب الصواريخ سقطت داخل القواعد العسكرية الأمريكية دون تسجيل اي عمليات اعتراض من قبل منظومات الدفاع الجوي</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/89800" target="_blank">📅 01:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89799">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تنويه
اصوات الانفجارات في سماء بعض المدن العراقية هي نتيجة انفصال جزء البوستر من الصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/89799" target="_blank">📅 01:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89797">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37c7079d38.mp4?token=axpwd6YEIk-zLvzuwdGWA98T5cU1XX8DMBw-YR1zIrKrsEVai3E_sXFsBaJsmPJ_18VQcd-Ez921LViz_wva3k-hydaenB3GIPK8XeCQW_ieko_c4Aazqy3iwjXom66v1GaAANsGnZAC4OZ8qBacUzpyUCD2XMaP8RTQeJY9NzmdbjJig-MV17dnXRxnbQFdYt8RlxVxhkww5dUpPO9HXu8X8w7G_dood9Y-w4UfrxyVAJavPbP_Pic-PSWNm1sSxWj9MCNXjqZCcMNkpCJH4zENRH8r_TsQpR6Nb-BJSDOyzITdmwFj29Q0uv32MxNmNQ_WF4_a5RgBj7B8CGsgXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37c7079d38.mp4?token=axpwd6YEIk-zLvzuwdGWA98T5cU1XX8DMBw-YR1zIrKrsEVai3E_sXFsBaJsmPJ_18VQcd-Ez921LViz_wva3k-hydaenB3GIPK8XeCQW_ieko_c4Aazqy3iwjXom66v1GaAANsGnZAC4OZ8qBacUzpyUCD2XMaP8RTQeJY9NzmdbjJig-MV17dnXRxnbQFdYt8RlxVxhkww5dUpPO9HXu8X8w7G_dood9Y-w4UfrxyVAJavPbP_Pic-PSWNm1sSxWj9MCNXjqZCcMNkpCJH4zENRH8r_TsQpR6Nb-BJSDOyzITdmwFj29Q0uv32MxNmNQ_WF4_a5RgBj7B8CGsgXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الرد الإيراني العنيف مستمر</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/89797" target="_blank">📅 01:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89796">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8c8dc2312.mp4?token=N1qthxl72e7WsJ-JhiZcVr-yGTb450gcO-ysRNO0kwz82O2ZRNCOZNsaAVQoAeZ3xXxhff9hbMiuoE01YGv1er8Vb-6x8Jn41W2uBekINWKE0QRTRrsIwleqfOVWNyA_XPWZ4xr9fvHv0tF_sErxew41_iAoKw4rtSSyIEmfKlUBUKXWz_7KfeqYETxf_BHL6IN4x3R_Ka6tUbR07e8t2AUjRr2eXiONHxaYu-HSXowSnQ1iZxX5l8FS7go9S9DuT4E3doZX8WXpxSKWO0UnEDT8QdTNDNbRUP7xfMBJkXf5AuH9x_iFu6bPVjo02OdHNomiwnS3uRwwXTBpFo7hRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8c8dc2312.mp4?token=N1qthxl72e7WsJ-JhiZcVr-yGTb450gcO-ysRNO0kwz82O2ZRNCOZNsaAVQoAeZ3xXxhff9hbMiuoE01YGv1er8Vb-6x8Jn41W2uBekINWKE0QRTRrsIwleqfOVWNyA_XPWZ4xr9fvHv0tF_sErxew41_iAoKw4rtSSyIEmfKlUBUKXWz_7KfeqYETxf_BHL6IN4x3R_Ka6tUbR07e8t2AUjRr2eXiONHxaYu-HSXowSnQ1iZxX5l8FS7go9S9DuT4E3doZX8WXpxSKWO0UnEDT8QdTNDNbRUP7xfMBJkXf5AuH9x_iFu6bPVjo02OdHNomiwnS3uRwwXTBpFo7hRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الرد الإيراني العنيف مستمر</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/89796" target="_blank">📅 01:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89795">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d100d8f3c2.mp4?token=KBObOWS50Pj23dRvFNPFMZ61IjOm_s2qrtap1wMfHDwqHgBOcyawlWvaUzcJ85plR1XTv4_k7k4hfedO-hOagAXIxRsxKlukgmxqTId3QWJo0-W_TwcsTUrVf-xwz5DMttSXsoOMzIwd49L11Z6Jhs3jsbCMq80wagLhO1cF5TUGqK7hnIgp8SWC7oQ4dHGtKY97xjho7o38H_T6TINRZ9KUVywcIOyhz8OKw7W3PtGzwuLRsMvCL1OmPFntYpyFKt_f_dFF6Rl_fP3UaVnvpiA5blpolJhEyiaOF2WZiBi027eGmm4P5iCxHE6zODn-VAG8bX3rz0VF9lm-3ByZUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d100d8f3c2.mp4?token=KBObOWS50Pj23dRvFNPFMZ61IjOm_s2qrtap1wMfHDwqHgBOcyawlWvaUzcJ85plR1XTv4_k7k4hfedO-hOagAXIxRsxKlukgmxqTId3QWJo0-W_TwcsTUrVf-xwz5DMttSXsoOMzIwd49L11Z6Jhs3jsbCMq80wagLhO1cF5TUGqK7hnIgp8SWC7oQ4dHGtKY97xjho7o38H_T6TINRZ9KUVywcIOyhz8OKw7W3PtGzwuLRsMvCL1OmPFntYpyFKt_f_dFF6Rl_fP3UaVnvpiA5blpolJhEyiaOF2WZiBi027eGmm4P5iCxHE6zODn-VAG8bX3rz0VF9lm-3ByZUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الرد الإيراني العنيف مستمر</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/89795" target="_blank">📅 01:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89794">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">شكرا للشعب الأردني المسلم المجاهد
على دعم الهجوم الإيراني من خلال التصوير وتحديد مواقع المجرمين في الأردن</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/89794" target="_blank">📅 01:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89793">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اسمها قاعدة الأزرق
موفق السلطي كان رجل مقاوم اردني شريف قاوم الكيان الصهيوني</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/89793" target="_blank">📅 01:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89792">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">يالثارات شهداء سيريك وميناب</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/89792" target="_blank">📅 01:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89791">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f5e96216.mp4?token=hOt1rU_kb4buSJMbhhDNEha-AZiZZzAQA8-O5ASr7rhMw5mt6sFcN4zlTdfFbAU5aDADvxFBmkBtq-hEyuqeSZuJAgNVwi8tyCh0hFWHvW_La6DH3XF_OS-_FSvREu58kAPkvoNlkSSU-KypO1CdeJzhrq_rGhn8YmwoxZk0kgKE-C6fCf6rY9U9n2GAfw_L_JqGFMZ2dfYulIQ7FFqBEupHmNXcs9tznTuWSfXZWmIhZVVMrZBcd9yP05Imz2GeqPLzWaMvBrM2_I3MCdB0xrSRlbjVJOI9KjhXrNiPZqMH34a7LcXrdGjLHeLX07wHQ4qnSWIHvDNFHqX34U2MyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f5e96216.mp4?token=hOt1rU_kb4buSJMbhhDNEha-AZiZZzAQA8-O5ASr7rhMw5mt6sFcN4zlTdfFbAU5aDADvxFBmkBtq-hEyuqeSZuJAgNVwi8tyCh0hFWHvW_La6DH3XF_OS-_FSvREu58kAPkvoNlkSSU-KypO1CdeJzhrq_rGhn8YmwoxZk0kgKE-C6fCf6rY9U9n2GAfw_L_JqGFMZ2dfYulIQ7FFqBEupHmNXcs9tznTuWSfXZWmIhZVVMrZBcd9yP05Imz2GeqPLzWaMvBrM2_I3MCdB0xrSRlbjVJOI9KjhXrNiPZqMH34a7LcXrdGjLHeLX07wHQ4qnSWIHvDNFHqX34U2MyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشقات جديدة</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/89791" target="_blank">📅 01:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89790">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f3509f88a.mp4?token=bHM4ZD_iEdrNLt3twuReXKedZxTcR5CIEx8Q0JyJkj-RHPOg-LMYF2gdK7MLfmJo909omhggjXH3oG6_6mv2rtFhag0p9LjzuO3jMmiai7QNL1oUOM2Hdjh1nDhlfUroVMnarc1a-Eb02Y1Wze_GV3mgiX7H2QCbDF-BFjaWkQdDRc5zXLbbbQV7slrPxin0xfIgFlNwD9SD41_ru90BtogNZhxzdW9xVlrjwkQg7S2hHm5nuXX46JSTK7UdFFZO7Pzx1L50r4W4jEGxpMNFsgEoAaS2ZDa4uOnroIGxtW3DDBi3CNtRMEJ4TErT65eQShUigpxipBeO51p_Ks1FLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f3509f88a.mp4?token=bHM4ZD_iEdrNLt3twuReXKedZxTcR5CIEx8Q0JyJkj-RHPOg-LMYF2gdK7MLfmJo909omhggjXH3oG6_6mv2rtFhag0p9LjzuO3jMmiai7QNL1oUOM2Hdjh1nDhlfUroVMnarc1a-Eb02Y1Wze_GV3mgiX7H2QCbDF-BFjaWkQdDRc5zXLbbbQV7slrPxin0xfIgFlNwD9SD41_ru90BtogNZhxzdW9xVlrjwkQg7S2hHm5nuXX46JSTK7UdFFZO7Pzx1L50r4W4jEGxpMNFsgEoAaS2ZDa4uOnroIGxtW3DDBi3CNtRMEJ4TErT65eQShUigpxipBeO51p_Ks1FLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/89790" target="_blank">📅 01:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89789">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f296b26a0.mp4?token=WkpphdroCOlxvymjgRxse3fWMX28x3gKBHUIhGecDnMIfaSpE2f4N5GcpWd41CnG-_LzjqJVaYHzEfe5UxUjT3sBWIwYMJSxK2F-Ozv_W06ExsTiq5VxFOi-eAPkELdE1vugMPt-cowaLy7CojB2VXULBFiXXVna_-vQGeWNxffxwnzulojitXakmRDp0QpyO8XBlEQQHUv85P0kWH_V3AuniGQlaqjVeIpSy8d2wRSPhw0LwTN0PJ-mL3wgYtzbIG9102hVlqzaATxuXKAh4Q5ugx8rw1mmFf060JFp1gKBHmYqN7BYKRE44GIHk7SDjgEqr3SzVYieyge-umm03w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f296b26a0.mp4?token=WkpphdroCOlxvymjgRxse3fWMX28x3gKBHUIhGecDnMIfaSpE2f4N5GcpWd41CnG-_LzjqJVaYHzEfe5UxUjT3sBWIwYMJSxK2F-Ozv_W06ExsTiq5VxFOi-eAPkELdE1vugMPt-cowaLy7CojB2VXULBFiXXVna_-vQGeWNxffxwnzulojitXakmRDp0QpyO8XBlEQQHUv85P0kWH_V3AuniGQlaqjVeIpSy8d2wRSPhw0LwTN0PJ-mL3wgYtzbIG9102hVlqzaATxuXKAh4Q5ugx8rw1mmFf060JFp1gKBHmYqN7BYKRE44GIHk7SDjgEqr3SzVYieyge-umm03w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الايراني تراوغ الدفاعات وتنهل على اهدافها بشكل مباشر في الاردن</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/89789" target="_blank">📅 01:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89787">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/508dc47b64.mp4?token=VkfqNPOPprpT1QO074iPq4s5xkrvA07SZlOyEWOonax_O3ALZiAyuNrWUgpjNFyy5434F2vefmJQz99Uv5hBm5uypJHxBhwIF_q15_agD6ss7wueXvnwYWTCOgE3f_JFwB2Cq0DfUGwnwiPTJL50QPZ9JwQQKSqvclJmxz2dJ1XEU8hY481YmUACFK2uaOYQ0zvaGRv4dabCCYyf22o-nPaaONFljwqqXKQ-01zR16gtTBrXoTMip8SA6VJAHNL9Plby6rf_hYEjDtOEDVZ7MXfdpndICN6HsFyONeOP1Y0BvBToAwKsF3yQWB2bgkKCKcCsJCQYjYI3WbX_gS8rXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/508dc47b64.mp4?token=VkfqNPOPprpT1QO074iPq4s5xkrvA07SZlOyEWOonax_O3ALZiAyuNrWUgpjNFyy5434F2vefmJQz99Uv5hBm5uypJHxBhwIF_q15_agD6ss7wueXvnwYWTCOgE3f_JFwB2Cq0DfUGwnwiPTJL50QPZ9JwQQKSqvclJmxz2dJ1XEU8hY481YmUACFK2uaOYQ0zvaGRv4dabCCYyf22o-nPaaONFljwqqXKQ-01zR16gtTBrXoTMip8SA6VJAHNL9Plby6rf_hYEjDtOEDVZ7MXfdpndICN6HsFyONeOP1Y0BvBToAwKsF3yQWB2bgkKCKcCsJCQYjYI3WbX_gS8rXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشقات جديدة</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/89787" target="_blank">📅 01:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89786">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49e52b0fac.mp4?token=YOoFuJ-u7-mSqhME9BVIdnb8pMhEfmQi90X18jIRyD4iV4uIfDI7XlYWdos57m6CaUoZ3mDqTjBjqbahubVDJNJmI-5XSKJxaYdAxLel74ZJZzgzOn6DPNXVDQPP06mIrEz2VGZWmOfR52cXZFw-zu5agXGqkIV0rEpr7ELnIu-u8sIRcmn2T0vsoRLTNMIar5P2AdvOzfCs_1HiY4RCYrUT5KucnxzC9ZdhGkLh8c_uDcJYpTHQKSab4kgjN0mYMYGX-egN4vpLYqciUhR1Tzw8Yo3f6waSwRqzLsRIm2gKHJqeeJeX5F7qbaBy1dRJqqDf-TF1hJOHd1gm_vahEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49e52b0fac.mp4?token=YOoFuJ-u7-mSqhME9BVIdnb8pMhEfmQi90X18jIRyD4iV4uIfDI7XlYWdos57m6CaUoZ3mDqTjBjqbahubVDJNJmI-5XSKJxaYdAxLel74ZJZzgzOn6DPNXVDQPP06mIrEz2VGZWmOfR52cXZFw-zu5agXGqkIV0rEpr7ELnIu-u8sIRcmn2T0vsoRLTNMIar5P2AdvOzfCs_1HiY4RCYrUT5KucnxzC9ZdhGkLh8c_uDcJYpTHQKSab4kgjN0mYMYGX-egN4vpLYqciUhR1Tzw8Yo3f6waSwRqzLsRIm2gKHJqeeJeX5F7qbaBy1dRJqqDf-TF1hJOHd1gm_vahEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/89786" target="_blank">📅 01:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89785">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/89785" target="_blank">📅 01:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89784">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مصدر إيراني
حرس الثورة استخدم قبل قليل صواريخ خيبر شكن</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/89784" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89783">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انفجارات تسمع بوضوح من ام الرشراش إيلات نتيجة الصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/89783" target="_blank">📅 01:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89782">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4c52f8bf8.mp4?token=hwkFynSkxN2ZF2lSXvq0KnHMnwBdq_7rmBzGvhPT-k3XmOh5bVp6Hi0lr3IqAqp2KXNogQthsF0Es6edydEukkPqx7oPaRlBHYsZm0bkI5PxzULVzHvLkoOOz21MWxw3eWOlnMhNdOExq187xCmujovGtCItkosCx8wwJuunSeadZG57Xy58BAITXxW6OVSL9dGeFm2_RSG_yX9r12tSjUKbBOLizNBePz7FVIrqbN2iOLHqVizLcrB2hCt7kKmsT0v9MnViCCJBSZVAT8tHmZvrq8U1wbNueZH0kwTY4JNoUeBwPWOJSv77btqE1QmIxOCb7Ro5MDLIW8mp1DuSZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4c52f8bf8.mp4?token=hwkFynSkxN2ZF2lSXvq0KnHMnwBdq_7rmBzGvhPT-k3XmOh5bVp6Hi0lr3IqAqp2KXNogQthsF0Es6edydEukkPqx7oPaRlBHYsZm0bkI5PxzULVzHvLkoOOz21MWxw3eWOlnMhNdOExq187xCmujovGtCItkosCx8wwJuunSeadZG57Xy58BAITXxW6OVSL9dGeFm2_RSG_yX9r12tSjUKbBOLizNBePz7FVIrqbN2iOLHqVizLcrB2hCt7kKmsT0v9MnViCCJBSZVAT8tHmZvrq8U1wbNueZH0kwTY4JNoUeBwPWOJSv77btqE1QmIxOCb7Ro5MDLIW8mp1DuSZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/89782" target="_blank">📅 01:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89781">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">يوم القيامة في الأردن بالمختصر</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/89781" target="_blank">📅 01:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89779">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1fb43c570.mp4?token=DG_2NbVLPSgOdUeKfykiW7zB407ibIgnXF8nerlId4e5PcmrmjbvSjCme6TcrIok28sVlXRBtSV_lJ3NMBt1F8C6pKmB5WtcS_Sk1WnZgTMoGKU76KOx1Ji3izOtU46vAt4b1ICQsBJf2e0i_fpZmsHNVfK_ZZHGIMjWQlZfqUraZ1GT3yf3oTpBb38Xr_N0CWSTSFmYe6f1MmJw0ajr_CqeFn2ToDdCJ8kRldZrcu95nE-plhUB6QLNYBprWlfAjh_v-8f3eAtAbOOz4OdMzs3Fv_UadiAorGC23sL8vWrMNCYl1-LTWWPye6MKqmwF4ZMs_k5JRqZlJRLD1XL9Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1fb43c570.mp4?token=DG_2NbVLPSgOdUeKfykiW7zB407ibIgnXF8nerlId4e5PcmrmjbvSjCme6TcrIok28sVlXRBtSV_lJ3NMBt1F8C6pKmB5WtcS_Sk1WnZgTMoGKU76KOx1Ji3izOtU46vAt4b1ICQsBJf2e0i_fpZmsHNVfK_ZZHGIMjWQlZfqUraZ1GT3yf3oTpBb38Xr_N0CWSTSFmYe6f1MmJw0ajr_CqeFn2ToDdCJ8kRldZrcu95nE-plhUB6QLNYBprWlfAjh_v-8f3eAtAbOOz4OdMzs3Fv_UadiAorGC23sL8vWrMNCYl1-LTWWPye6MKqmwF4ZMs_k5JRqZlJRLD1XL9Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ تنطلق نحو الأهداف الأمريكية</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/89779" target="_blank">📅 01:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89778">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtEpcWRxSIo2KsPR9g0pa0UDuU2JX6cL_s6v7QdyOW9wL35CkgewxJa-cm0xG-zoRafyoAeAk5vOeIrJFJTg6m8EKepMlMwTXkmJBv7iLf5vaDvVMRRjkIr2sCVP_aso5uYCb7ExAX2epF23Bhni3NL4NGz5gyWXw-hRdv_3w2WvRv-w8uwSjIrftCxJ6LvIUyPYhvELnS-F81LkdSYRZ3UBuYnRa5SyiI3moDSA0GcAN4PESrb7sxV-12TWVsOrbmQ0nvSZbWPmRMpWhQLgAVbTtiGtZK6vA4bzjTSfrIfULDDiI-53RHSoGAW57pRhypF_qtF5NBR5LqJmnx_fHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رشقة اخرى باتجاه دويلات الخليج الفارسي الان</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/89778" target="_blank">📅 01:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89777">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رشقة اخرى باتجاه دويلات الخليج الفارسي الان</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/89777" target="_blank">📅 01:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89776">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNnPs6_3DQEFLS8S4kQ3l4IHcWT-1zufOmHASgvwaUh293iZYOl5WG6R-2t_2Bi2AgwzE56C3fCUEXvG3BTGr2gWtgWNBnNrAhbUR0FM_XqL8YCV591a33kD44QZ-qTcSb709dW829qW-GQtPZ4z1UBtjbOHxD5pOwoER7xBPa0ZgMI1rg1rWEo-vGNywh016_nIJYzZNTyHrhhBNRocG01s8w59utykZ-nn4FcgksGw8-_tdSqBlZ454KkEsCAngblRKiFJDmHg_a16PraydNYMtoWL0qC-MKXNysS0ALrJw3ymwoo-phTJzEL5wSHO78q76IaIeHKZwhVHZvS4HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر   ايران دكت الأزرق والعقبة ب ٢٠ صاروخ</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/89776" target="_blank">📅 01:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89775">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">الله اكبر
ايران دكت الأزرق والعقبة ب ٢٠ صاروخ</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/89775" target="_blank">📅 01:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89774">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlkgXCKovEbc6Plm3-Btwbh-R5uFg0CzwidPDMaWya0dvXAx8j25OR9_rwmkJ-PW1QCbccOhHYH6DBCLSYNP1JRtJ0oD6TjiLTFpZzO_pMGfl81TlJuLt7IVskBxyVAhNR4mHS11YD5eMtBSm2fg8g9DJ7Bc4T5uc6r92J_cwpsgkMejAdieFhzapvVoTltxMOz9Ex5nr5Jbx2bGABMKACnNSHhwtWd2ozyEsvnEygXkS_aKSwaj8ltumz0COc47UWvaeF_XzQ3hMbRjRWfoCS4mVwTqHsW8Q7eF_2Ifzr0j7UUOzxtz46iEwTUywr5TpJql_ecgc-g5pxA1VoSDHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شخم زدن پایگاه‌های آمریکا در اردن</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/89774" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89773">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b42923dbac.mp4?token=apE58ZKFtFvbZsM4ntf1Ve_MU8ZEiCGX_fIedYJ4n2S0KOb9e26gCvzdhIqL3c4hp-hwNzNyKKNYqa_nDPVkmlEroK2Yky1ZLzcYEsTf50dnlmIkSveQqhEZcMUDNBojWjljUG3utKFPc5bTk4FBW3oLhr7yU5aXNTRO7HVQNVgiigHsy2UGKzwgJ0rZEHq6iEIlu97WoGpSuDDuE6cQzShN1m2iW5wDD67vxPunBG6EIGJVges8W-MB0wy4FcCsPmKOqu-M_acyOcNhw1H73HleJa_hJlk6S6iCsIR3jYtJT9IG7ZoqTnU7Q4DCjgAsCXUxNXtmXVkcgaMJTJWXzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b42923dbac.mp4?token=apE58ZKFtFvbZsM4ntf1Ve_MU8ZEiCGX_fIedYJ4n2S0KOb9e26gCvzdhIqL3c4hp-hwNzNyKKNYqa_nDPVkmlEroK2Yky1ZLzcYEsTf50dnlmIkSveQqhEZcMUDNBojWjljUG3utKFPc5bTk4FBW3oLhr7yU5aXNTRO7HVQNVgiigHsy2UGKzwgJ0rZEHq6iEIlu97WoGpSuDDuE6cQzShN1m2iW5wDD67vxPunBG6EIGJVges8W-MB0wy4FcCsPmKOqu-M_acyOcNhw1H73HleJa_hJlk6S6iCsIR3jYtJT9IG7ZoqTnU7Q4DCjgAsCXUxNXtmXVkcgaMJTJWXzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد حصرية لنايا...  لحظة اطلاق عدة رشقات صاروخية من الجمهورية الاسلامية الايرانية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/89773" target="_blank">📅 01:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89772">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d2b24a651.mp4?token=mmfjuivtCaBrwaue9F-5bdqrtKw-pw8fbnyiGA4VzinG7S9whfC8kYMsog66Vlf0dAQjgJ2XPOFStuszGGUSMT8cwjd_IY6JxTO57oSZC-i1GFi3eZivw9dYilCET8UtUMpfroxR6crl5-dN9caIVfMj-ghJp6q789_ZZUKPkeRC2n0e0x2XRzjVC2LI-vhXkf4GxhGYej_X2LW1IEl6_wa1TFCjB1DNfOcwr8rQGXdu3IF47jwF6ARD2EOV1ljl20fyZNPzIe66_UOzUx5_DWYMF84Lp3yss-VEcB3SI4dTh41OsjRI146ZVm8_w59SLtqN1GNUEtCVMENawgHoew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d2b24a651.mp4?token=mmfjuivtCaBrwaue9F-5bdqrtKw-pw8fbnyiGA4VzinG7S9whfC8kYMsog66Vlf0dAQjgJ2XPOFStuszGGUSMT8cwjd_IY6JxTO57oSZC-i1GFi3eZivw9dYilCET8UtUMpfroxR6crl5-dN9caIVfMj-ghJp6q789_ZZUKPkeRC2n0e0x2XRzjVC2LI-vhXkf4GxhGYej_X2LW1IEl6_wa1TFCjB1DNfOcwr8rQGXdu3IF47jwF6ARD2EOV1ljl20fyZNPzIe66_UOzUx5_DWYMF84Lp3yss-VEcB3SI4dTh41OsjRI146ZVm8_w59SLtqN1GNUEtCVMENawgHoew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اطلاقات جديدة من إيران نحو الاهداف والقواعد الأمريكية</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/89772" target="_blank">📅 01:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89771">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f211389571.mp4?token=AJLvGFDxwTQ32Mu1K_dZvSfqYHAqkenPemlYNDdQqp5v0YVVIuPbbnhiMVhEWmmMHDSPCN68XQQpWvv57vDql1SIsKh6zANIFK8c3gr6OE8tL0ONTKfZs4yiolb1PPGW8DA-IMxAWHoqme7L1uwYfE0v1i9m3mjk0STpxnlkx7cWcoM_mEdWZ6LABfDbcyuqK8QLZPgg97VaNRnKHo19DAYKpfdoRFnDejpXPRsQqG6E3oBVhB_ULlOYGp1sv3ylRoRPw-K7Ch7h0OJsJ1Y_eiepq9Y3SxnbHpiTjCXCLDVNeX4PTeFlNdgb1IA6SuPxrIZ9KH9ne5gW1sd7SbKvfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f211389571.mp4?token=AJLvGFDxwTQ32Mu1K_dZvSfqYHAqkenPemlYNDdQqp5v0YVVIuPbbnhiMVhEWmmMHDSPCN68XQQpWvv57vDql1SIsKh6zANIFK8c3gr6OE8tL0ONTKfZs4yiolb1PPGW8DA-IMxAWHoqme7L1uwYfE0v1i9m3mjk0STpxnlkx7cWcoM_mEdWZ6LABfDbcyuqK8QLZPgg97VaNRnKHo19DAYKpfdoRFnDejpXPRsQqG6E3oBVhB_ULlOYGp1sv3ylRoRPw-K7Ch7h0OJsJ1Y_eiepq9Y3SxnbHpiTjCXCLDVNeX4PTeFlNdgb1IA6SuPxrIZ9KH9ne5gW1sd7SbKvfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية تهين القواعد الأمريكية</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/89771" target="_blank">📅 01:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89770">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/89770" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/naya_foriraq/89770" target="_blank">📅 01:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89769">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">الله اكبر
سقوط مباشر بالعقبة</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/89769" target="_blank">📅 01:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89767">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b19aa63524.mp4?token=ZaNTnxzXrXrrVH9XD_Hj7YU7JjahM9TpWh5YkNyPFoYAvWVUH_FSVBolLDyZsH4l_Ob3-6QtIE7_-jB5zaBdBT3mO-ozv5uxUIZBafCANfCnrotrz8WxcPLFf7lZkzI1fktTB0fAx1__2q7xdPJQQZLuN9jUdXTD4l867uUGks_on608158VwzOfAxLwh7v74WnN_gD8c538vL1qhF3YIZI50eOX4HEqd_EIjXsQl2XfHL4x7vLSxslN9YsK3XijLA-lrjyeYiYTXhc-2BeQLcU9SeE60qaSw6RnXKBTsM5DROHvRXF5DLOwTLWH5LmoXVxOuyHIT29igDXDp-qm-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b19aa63524.mp4?token=ZaNTnxzXrXrrVH9XD_Hj7YU7JjahM9TpWh5YkNyPFoYAvWVUH_FSVBolLDyZsH4l_Ob3-6QtIE7_-jB5zaBdBT3mO-ozv5uxUIZBafCANfCnrotrz8WxcPLFf7lZkzI1fktTB0fAx1__2q7xdPJQQZLuN9jUdXTD4l867uUGks_on608158VwzOfAxLwh7v74WnN_gD8c538vL1qhF3YIZI50eOX4HEqd_EIjXsQl2XfHL4x7vLSxslN9YsK3XijLA-lrjyeYiYTXhc-2BeQLcU9SeE60qaSw6RnXKBTsM5DROHvRXF5DLOwTLWH5LmoXVxOuyHIT29igDXDp-qm-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اصابة مباشرة في قاعدة الاحتلال الاميركي</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/89767" target="_blank">📅 01:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89766">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">قاعدة الازرق في الاردن</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/89766" target="_blank">📅 01:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89765">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOP-XdOj2yRYERtNQJNqVb5EP_xEj9qFmKxyQFXmqIyHi_TIhZ3lDl6_TP2TojJB1UTxAo2gfL2qEmGapnyuI-7uR_L0QuaDkV-zHQ-u7AjYKK7O9ltOAoFs6DKRjhTsBv6xdb4RpK7wrXWyprplxFBlPt2TKFr5Iuv7KvJosf4NeIElkCoxII2zkmc_fvvl1w-9XKqt9yf2Yc3-1-fi_qx3_aZTG6Mfm0uplm8dZpG6fMKsJ7OvWS_v-LGgQBcH4MBkUAe6mavdv9RKWNPDZW3IrPLqvGM3S4LfvQMJk0F4eyuYZie6_1xKMWRvXv7dQxeGCp-zePU4BbZtqEtgQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
We cut the hand of US in Hormuz</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/89765" target="_blank">📅 01:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89764">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4839b061a.mp4?token=Zg9YbAlcs4u2MpkOIUC4K0F3k6Cc9brqPeNwSqBJiihWrcszbQbXp6jeWAr4c96HAu_RywLtChICFKIiyonqJU9UW61a7oOt_FhQI0rOdEwqt6o4lUc_Pshg0XmVTLqhbkGbo7zavgfUK4CTBOZq43RxmU9TxYUE6lq66mRhc95-AbBLxSQJEZaTbY2AwGJuIx6-Eh48i-1Dg3FhWVUr-B5xUlE2vIvVw1DNMcvw7kVoTc0dyOjzL4UQ0zL0HbBG0HYhi79oCYN8ImP-0GMe0ptyxfkVelW8hGpfVEPVSqRZIh9qvCNgMSxi5sn8Ab3uuFrBs7llCx9zAslaOaIpjhGm5EjYvw42KQmYD2t-Uq2Zlt_FgyjJcGw9TDnHObEq9LIE9SfLNT1jdhzJ6QGe3_O_2cfNNqkKrls7MWj5gkdMCqeFaepB-m2cQ9VUiu5mV9tQsUHlBNF_9SgDTVb_n8j8S03DUIqlrpHmxbZXi1vIvbpnYAvz6l--0DQXMmbZrdvd_8anpBM8BsKEC8CSaJr7EMlYxpb3rBQf2FFVkOxZtJZstfhgasNNCv7QyZN-y_7feaRS-WQ4hObeIUqvbHR1wWm8j3cEShN9GsGYxedm23uy7uuFTFhfijhqac8qEdp7ps0JW8TFseFfJKzQDXyZ7JSUdgYYlNwoUIabTBc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4839b061a.mp4?token=Zg9YbAlcs4u2MpkOIUC4K0F3k6Cc9brqPeNwSqBJiihWrcszbQbXp6jeWAr4c96HAu_RywLtChICFKIiyonqJU9UW61a7oOt_FhQI0rOdEwqt6o4lUc_Pshg0XmVTLqhbkGbo7zavgfUK4CTBOZq43RxmU9TxYUE6lq66mRhc95-AbBLxSQJEZaTbY2AwGJuIx6-Eh48i-1Dg3FhWVUr-B5xUlE2vIvVw1DNMcvw7kVoTc0dyOjzL4UQ0zL0HbBG0HYhi79oCYN8ImP-0GMe0ptyxfkVelW8hGpfVEPVSqRZIh9qvCNgMSxi5sn8Ab3uuFrBs7llCx9zAslaOaIpjhGm5EjYvw42KQmYD2t-Uq2Zlt_FgyjJcGw9TDnHObEq9LIE9SfLNT1jdhzJ6QGe3_O_2cfNNqkKrls7MWj5gkdMCqeFaepB-m2cQ9VUiu5mV9tQsUHlBNF_9SgDTVb_n8j8S03DUIqlrpHmxbZXi1vIvbpnYAvz6l--0DQXMmbZrdvd_8anpBM8BsKEC8CSaJr7EMlYxpb3rBQf2FFVkOxZtJZstfhgasNNCv7QyZN-y_7feaRS-WQ4hObeIUqvbHR1wWm8j3cEShN9GsGYxedm23uy7uuFTFhfijhqac8qEdp7ps0JW8TFseFfJKzQDXyZ7JSUdgYYlNwoUIabTBc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/naya_foriraq/89764" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89763">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81536a5aaf.mp4?token=kRYqddCMh4D9c7gnMF1DwYCVldgdEbvBBAE__BmGyckLyYp-5h2xK5cIUkbtHxx_jSYc9BvGGdeXWg5Xrj1aQLmRk9GiyF2rAayaYWxVbdS1w5lK1KpEEO9QO0pmr6mAf2g6t5uZTk_2A4YZHHuyJHqvLer9VtjBIxfpM8_5Hik7ZBrWj6niAcjHQ4U2_XKPZracRIXXhe0n8SRuybd5Geel5a8JUkCoc7Jw5Z8NWvScY0KM7boysP2XMJRGAkOAPQOa-4Ha2ZFwJuH8N-DACEC7jHUnf3A7LdxaE1oY3xgv9p-mXH5gxynx_k3HdjUXTUbodWYPn7wy7cceUGa1Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81536a5aaf.mp4?token=kRYqddCMh4D9c7gnMF1DwYCVldgdEbvBBAE__BmGyckLyYp-5h2xK5cIUkbtHxx_jSYc9BvGGdeXWg5Xrj1aQLmRk9GiyF2rAayaYWxVbdS1w5lK1KpEEO9QO0pmr6mAf2g6t5uZTk_2A4YZHHuyJHqvLer9VtjBIxfpM8_5Hik7ZBrWj6niAcjHQ4U2_XKPZracRIXXhe0n8SRuybd5Geel5a8JUkCoc7Jw5Z8NWvScY0KM7boysP2XMJRGAkOAPQOa-4Ha2ZFwJuH8N-DACEC7jHUnf3A7LdxaE1oY3xgv9p-mXH5gxynx_k3HdjUXTUbodWYPn7wy7cceUGa1Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قاعدة الأزرق في الزرقاء تحت رحمة صواريخ الحرس الثوري</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/89763" target="_blank">📅 01:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89762">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8edd87f15.mp4?token=KkRL5xyqvK_yL4IKyq9mEhFq-9kF_DnhJZBh6vexU3WKcSt29iqo9COpG7fCY9SSYTRx1b1ny5g9MPF3fk-lffRzvnhb51g17vNmo0X6foDaudZ3giV7PGNHmjDeU1D_tkBjKzxP-J3rnVe33Q7j71iraHX_taw_i3h7xYpHi-fZDdGAtlvkPULsOUJHMz_xOUxHmN2B-vHRI9xnTjxBSyKRh4XCKm2hdC6jepJ3JqSBVVQyuDYxa7VZUpho3R-FsSj-5Kox7YjT04LXNd7BzBOueN9vPqEKk-s-e8DOp-Nv6YjDMoXqoquBnm75x7AaMrhC1vdXGelTh6UmTkQTzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8edd87f15.mp4?token=KkRL5xyqvK_yL4IKyq9mEhFq-9kF_DnhJZBh6vexU3WKcSt29iqo9COpG7fCY9SSYTRx1b1ny5g9MPF3fk-lffRzvnhb51g17vNmo0X6foDaudZ3giV7PGNHmjDeU1D_tkBjKzxP-J3rnVe33Q7j71iraHX_taw_i3h7xYpHi-fZDdGAtlvkPULsOUJHMz_xOUxHmN2B-vHRI9xnTjxBSyKRh4XCKm2hdC6jepJ3JqSBVVQyuDYxa7VZUpho3R-FsSj-5Kox7YjT04LXNd7BzBOueN9vPqEKk-s-e8DOp-Nv6YjDMoXqoquBnm75x7AaMrhC1vdXGelTh6UmTkQTzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة اطلاق الصواريخ من عدة اماكن في الجمهورية الاسلامية الايرانية</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/89762" target="_blank">📅 01:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89761">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/89761" target="_blank">📅 01:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89760">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/89760" target="_blank">📅 01:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89759">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d6b878d2e.mp4?token=jUrkKGx9xYBBoeqsJM0XnNA0n5SArofHEYMjz9PoUAHf_xwCCqcVdvT-H_MSCgEZZaY-B26ba_oR99piBZYedM8vmztqekR5r1Kap-Y9RKqo2E4O5MLCESo0Ms5xlBFX6QNR6GjEZNekWNa7c-eszdZketyKijgm_Jnc_xzNFuFPi5c_d-fbVXzK_itQoPVx_3LioeERl0k9Wgy7CllTJfiYSPRGkKnWba-c7T5e87hQhxSSow0T0WS1WHPCfk7EMMOHmtZDL2zWd4uMvQYRrwVgdTSrq-XoPZ6vSxSXoIuQ27z59QIbVTLUVoPR_LxsJq93qx45je5Bj6rLhK67Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d6b878d2e.mp4?token=jUrkKGx9xYBBoeqsJM0XnNA0n5SArofHEYMjz9PoUAHf_xwCCqcVdvT-H_MSCgEZZaY-B26ba_oR99piBZYedM8vmztqekR5r1Kap-Y9RKqo2E4O5MLCESo0Ms5xlBFX6QNR6GjEZNekWNa7c-eszdZketyKijgm_Jnc_xzNFuFPi5c_d-fbVXzK_itQoPVx_3LioeERl0k9Wgy7CllTJfiYSPRGkKnWba-c7T5e87hQhxSSow0T0WS1WHPCfk7EMMOHmtZDL2zWd4uMvQYRrwVgdTSrq-XoPZ6vSxSXoIuQ27z59QIbVTLUVoPR_LxsJq93qx45je5Bj6rLhK67Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/89759" target="_blank">📅 01:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89758">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb880adca8.mp4?token=J85Pa-o93duO_DPypnDx08bv72EPQ4O-Afa89zxcKuEXb3nR1Tf6H2ppDxC1MI6Vk59WA9cMJLzV91dUn6_oW8us6PNc0UgdefUq6H9tF_fzVgp-9hxTHU-tNTolokMP46xaC3OSRlZiusHkPCg7riQ2w3sFkjqyvF2r60TLgnP3_Thb7k9TdwKXTYTq-o_zfutSOCkCJ9y6FbzCfAuZsrcWPMg1kN04oLr6XbXZ-l-1rpGnZg6rDSZVMlLjqsFufdWJai6UOGi4I0UfXkM2L0uccAD3uXOy5vDI2JgDQ7TpbTeEw0QbzG4kDjS_z05KhYeVY_U25YV6RBi_zyf7Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb880adca8.mp4?token=J85Pa-o93duO_DPypnDx08bv72EPQ4O-Afa89zxcKuEXb3nR1Tf6H2ppDxC1MI6Vk59WA9cMJLzV91dUn6_oW8us6PNc0UgdefUq6H9tF_fzVgp-9hxTHU-tNTolokMP46xaC3OSRlZiusHkPCg7riQ2w3sFkjqyvF2r60TLgnP3_Thb7k9TdwKXTYTq-o_zfutSOCkCJ9y6FbzCfAuZsrcWPMg1kN04oLr6XbXZ-l-1rpGnZg6rDSZVMlLjqsFufdWJai6UOGi4I0UfXkM2L0uccAD3uXOy5vDI2JgDQ7TpbTeEw0QbzG4kDjS_z05KhYeVY_U25YV6RBi_zyf7Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة اطلاق الصواريخ من عدة اماكن في الجمهورية الاسلامية الايرانية</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/89758" target="_blank">📅 01:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89757">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ایران اسلامی با کسی شوخی ندارد؛ پاسخ شدید و سخت خواهد بود</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/89757" target="_blank">📅 00:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89755">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbZxwFCi9PUt1ER-cgJdJjwfdlMrRiPTzKup3gc0azRZCRXlzVl70GEDPaCaletnFHtnn5__iAqUGPfu_VZezNS53KN38pc3Zs2HCepMs4zVJ4JbOaTBSBSkLDkxn8LXQoqNIBPDTHM-X_Ar_J8aDavXRNAzP9lJ7MP1l6_vG5hpeltgRS4u0JVKTfT9X8ARMzziiM_EDFCQiTEe0Be-JrrGcRdVHnedmxgkHUPPC5axJZOe4JBQvLaUyJ6qLmN9Aa6fgGgt3xne_mVQERPmfo4kr9-AUPRf-rKwarYO8mbZqH42RD9NHsHKXA57dsEqzM5V5a4tcGEEmQ49YDU-4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721dcb7629.mp4?token=biXVQcyKmS9Z8lPp794mBcZG5U24n_z8zY62_OEMUGpFe6lK82dBYs8RnJjAUH4ymJr-bXM-WNSZlPAlHE31j2GkG-hLOEJ_XfbADQB_lr9igouItOnO3VA1okqcl9rizkiSb4nIGpZXwbCYCQK2N-c__fx5--eYYC5ovktXNw5jmcnbAfHA4WbZbiEh2Gp2tdRtsTzwudN2HTpek0sGcEQVVC1_AJhzFEK5VE11j2MaO0-f2AIMCPUYcoHk0-yex8rGFQ-S9k4Vis3Khwzo_bELBiEz4Uwp6o8ZAG2GMTRohxEnTrG8aXNAovjL1ReeP0Zl0kCmp6zbwQhg4bAxcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721dcb7629.mp4?token=biXVQcyKmS9Z8lPp794mBcZG5U24n_z8zY62_OEMUGpFe6lK82dBYs8RnJjAUH4ymJr-bXM-WNSZlPAlHE31j2GkG-hLOEJ_XfbADQB_lr9igouItOnO3VA1okqcl9rizkiSb4nIGpZXwbCYCQK2N-c__fx5--eYYC5ovktXNw5jmcnbAfHA4WbZbiEh2Gp2tdRtsTzwudN2HTpek0sGcEQVVC1_AJhzFEK5VE11j2MaO0-f2AIMCPUYcoHk0-yex8rGFQ-S9k4Vis3Khwzo_bELBiEz4Uwp6o8ZAG2GMTRohxEnTrG8aXNAovjL1ReeP0Zl0kCmp6zbwQhg4bAxcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشرات الصواريخ من عدة نقاط في إيران</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/89755" target="_blank">📅 00:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89754">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انباء عن سماع دوي انفجارات في الاردن</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/89754" target="_blank">📅 00:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89753">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/89753" target="_blank">📅 00:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89752">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/407db53af4.mp4?token=XmqxrBn-vv7VY182KlzSbR9n1jHoDth6JC7OUJv8sCJ9wDPlBuBGCkCRJ95LLWr709g_E2UfQEXx6UR9YBKKPOWA4E2tcI1SuQ64ITAjvKl5bJ_32yUsKO0x0u7xhmD6PibgluFxG5oGG4m3FgfPiIvvhOvwaMib-wLjgOy5CUqwyAQIySt0ZrKV94EE37b1GQc7r6cj3-DIjW1B149X-CoabEV47giA8GGlt1-9SoJlDj5RfTOuqlJqYO7unSjVW-4tjbxkzFm9acbIutiPCLpRwHBAHZJUmgesUr27FazDD97THbtnbVCHoc41tabmiQmtH518TozGX1Wq6Vu_9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/407db53af4.mp4?token=XmqxrBn-vv7VY182KlzSbR9n1jHoDth6JC7OUJv8sCJ9wDPlBuBGCkCRJ95LLWr709g_E2UfQEXx6UR9YBKKPOWA4E2tcI1SuQ64ITAjvKl5bJ_32yUsKO0x0u7xhmD6PibgluFxG5oGG4m3FgfPiIvvhOvwaMib-wLjgOy5CUqwyAQIySt0ZrKV94EE37b1GQc7r6cj3-DIjW1B149X-CoabEV47giA8GGlt1-9SoJlDj5RfTOuqlJqYO7unSjVW-4tjbxkzFm9acbIutiPCLpRwHBAHZJUmgesUr27FazDD97THbtnbVCHoc41tabmiQmtH518TozGX1Wq6Vu_9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/89752" target="_blank">📅 00:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89751">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/naya_foriraq/89751" target="_blank">📅 00:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89749">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vto3c8bnm8oW464PlzKEdnyou2lVdEyqfVdGAwAWJEl_wygtuO5ou28G3cA0r3I_Mc_HEcozz6QPbjCeWSnQV8QfeOXI8UJTcX6eddJPPJsam1caSfqty2_2ll2V-V8ygSVQ0dcFEwIzYLb80nrXcE5UmxjztyDjxijiU9XNx_FxnQtA168S_fGhM2rwhg4S1aXLq8aETFEatWJOfW-3pNLGCkkIwnNFvw_U8saqRKu6oH-jB2mOTjs6kGQ5SFCuWrXUdStcoLUWQ8dIwY6KVSDmpB-OHej-WTFBUImsW0nO1PHLhiyNUXD9d7gzTlBc-D2XF09UZ8aH9nIrqErYjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5d408eed6.mp4?token=X4bJZInSUHg5jS1CyYkJaMegH7NczwABn4mu73E50nFVnvSLyIvK7gBiag7yy_k90MqlCQW8EVjw3iIWJVsueqS_9VHb3m1y_sx9MKPwNW0sEx0EtRjJRZskTVNoJUgTX9OD0wUl2-Ihxwx6QsyKOe39XPwVJ7Hht-TO6CaJHoZRJTpmxKMORZkhaY7479ry4U5N-G3yShZmDnOzAcdiP8eKyQWPFfp7kVYliNeOyGgXZBP_86nLrmiieu1K8vYxW_iGisUPvWugsqrt_XL1ixonqNV1E2ZH_QF42kVw3wWigMwnc0NpRfkyemL28QLBrrZrc-ZbbThMB8ukduQWoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5d408eed6.mp4?token=X4bJZInSUHg5jS1CyYkJaMegH7NczwABn4mu73E50nFVnvSLyIvK7gBiag7yy_k90MqlCQW8EVjw3iIWJVsueqS_9VHb3m1y_sx9MKPwNW0sEx0EtRjJRZskTVNoJUgTX9OD0wUl2-Ihxwx6QsyKOe39XPwVJ7Hht-TO6CaJHoZRJTpmxKMORZkhaY7479ry4U5N-G3yShZmDnOzAcdiP8eKyQWPFfp7kVYliNeOyGgXZBP_86nLrmiieu1K8vYxW_iGisUPvWugsqrt_XL1ixonqNV1E2ZH_QF42kVw3wWigMwnc0NpRfkyemL28QLBrrZrc-ZbbThMB8ukduQWoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشقات متعددة تنطلق صوب قواعد الاحتلال</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/89749" target="_blank">📅 00:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89748">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvDNHfFcdkvwmD4wL8AvZaZcL-o5FjkHQVpbe6mVefzh5aKfwxkdoygOubPXbDx6Rw-jCjaZGZh7LQ8pQfN6BMeFoTbc9F_rTm6BYV9QGbCAh0P5r6_YzDZ907xzZUloVzPxK78faKm2gL-ftKHIIUS7X9QFzQCu5Ja_EyqGSHdPcsBNPnOo5gGnBiWG5U4X2o7i3qSKAbKMAM5zXj9dYVcVdhW4g06En907ZbcFCL1tRw23piG7A3vjn0Z5m02hJlRXFgDooD5zLb3Hk1aSMdnX-nC5fg1w6HXQGQUWaLeJPtkuKsEb-0TjQ7oiUpzDytdj0bQBQn1h5q6LrD-fvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الصواريخ الايرانية في سمائها نحو قواعد العدو</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/naya_foriraq/89748" target="_blank">📅 00:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89747">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d94a6f42c.mp4?token=RVoZgwso6iKIoh7_MMZn8ofnKhdpZoOmvHhfdV4QfqWr1fVP0Ksjs0b4t_LL2cNqq4XMXYNWXedaX5PSLdW04w-Fubavm2xVYOgENwwiI2Ps4Q4xPDTOIk7ufMG6w0bGMOpQf_2bY6RpHF2XgaHoOODvAKLMrmdETFy5SEwsJcCmWzDHWeezZNZRhxL1tGIxFg2w0BDluQ4xPNpESD5QPrWjdAyumCDfK-mTbBDPhiXmBsz2uidgxM1-ziFAMYyourGTjthRHyS_e83kRSCCA0y5uSAJidoVPF2vH3gny0E9B5VdM0urFHrR9ZMpuwwuTuclrlp1ZTJB8KaGFMPsFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d94a6f42c.mp4?token=RVoZgwso6iKIoh7_MMZn8ofnKhdpZoOmvHhfdV4QfqWr1fVP0Ksjs0b4t_LL2cNqq4XMXYNWXedaX5PSLdW04w-Fubavm2xVYOgENwwiI2Ps4Q4xPDTOIk7ufMG6w0bGMOpQf_2bY6RpHF2XgaHoOODvAKLMrmdETFy5SEwsJcCmWzDHWeezZNZRhxL1tGIxFg2w0BDluQ4xPNpESD5QPrWjdAyumCDfK-mTbBDPhiXmBsz2uidgxM1-ziFAMYyourGTjthRHyS_e83kRSCCA0y5uSAJidoVPF2vH3gny0E9B5VdM0urFHrR9ZMpuwwuTuclrlp1ZTJB8KaGFMPsFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشقات اضافية تنطلق</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/89747" target="_blank">📅 00:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89742">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u-b2VD6CnLS0F4xDYyYRTKGibQcsxdisazpcXpftqLr6etV86UZOI_uKR3CZFVmuoLhUYue2WYrcdDbLOh0QqSVjdykKEd2TV0fVpfY2ZJxEqLxdZIl6pr4OyP3xcm1GNG3yNPbP0p2WdM5Me6FW2RU067ujNm1QCwQcp8hMQvdBDWwYg6qf2lkke2s7_QZf4RO8nN_FuiG5u9D6FNiiQccSyuyceBgdNwfGg67aJ_nSK7J-JSLkz-1zR3Fpz7d2R3U3ElgGDWrF_qxAWFbslRTcKC7jMt3-qV92fd9h2sgZtQhCJNU2HvT-KyHd6OlCISnsEGyrPHRMekJTNklAsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTJ5q0O2WCjd2WfN--nMf9j1Nlwju78AlI7YnVHCDzRX3hfC2LU9Czy9KRIxwvBtTe4evACtH5t783Sf5uS-lcwkSn16mX01oci8iCYOgUaprnF9EaC6iEjLkJF1QnVwRDMDLBv1I7m6y1zcWDYKUXVgCRfaWwOXpdcvLFbv6ML0ElyvYmU4pfqarSZY3YO6b38FkeNzq-EbBIFTUrMTe8vavau94h-u_mcFxzuLQKGPOR13lju7EDgoLwkvNs9ftSz21TtPPUTz5VgOOHAdTIVM1gykCnkrbEMwW6RJyfPBjMcxcYRSrypw6OoEE-ni6cZdaYnJ3l_YXpQ2vL2q0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TspfimdVCTlzITVf4M_jmJA7owir67Pv4VvxW50Ioze-pL8LwVnttiu2dYtsIzE-cQSiZ1BfqA-0kqgmnwuvsqNUve4N3w7S7FI19JTDInC04ZANFuUMlxbsrIUpG4BSQGudTt2IT5GKeKB5yY1kMHk6GaL0pvl-MKyNyxm9ivyU2pkRkxHDGKfyKZze_RlTbgoG_cU5Qiiwkzxik3p9TmjFGeT_T9MNacHflUucblfdL71W5YOYIVIjxjR519LNHoDGcny0X05EHCg3BL3lguOzEiwLwScEiszZ55CoKawsYJehhe3oGUS-wlcULp5V6xXGwYiCxQJLh9emO9-jSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد من سماء الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/naya_foriraq/89742" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89741">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رشقات اضافية تنطلق</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/naya_foriraq/89741" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89740">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/89740" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89739">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQH5puSgyXeJBzeP2YqYR3Qfwp_VUYrcxpe4NxrbUfJIQmjrWyRguty-y6toD8XtUoTcQXqyzqfJQ3XD2sZY2q7sKkycFIfTIUbuW2NlmzHlTG5d7aSlTFBx_Rtt4-8wgTak58i843ce8LXO8GUobontuLvf3rW5bH2_nwB9kPYGYKDNGHI1twH917OtC6rJWkYqKagQzQ17xLFRins6OOYW0QA1-c4UCJGvK7SytPUYaSE4WQXY6Peu5eD7jr1YxkA5FM3pYA6PjRBTgPna96UOR7MlZ-or5uaZDuXAdAlf8dJqHjfDqwSsiMxJRQ9oJ3gfYSZK-niIw1FU4JkjeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إطلاق صاروخ باليستي إيراني نحو مضيق هرمز</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/89739" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89738">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OO8Zu9KHL8MT98GNW7BWK4Tu6NURjJ_H9vidLOeFWAIUAjIiO3ZdFicwsI835jHw1WnKgT0bN33jImOEPpEZf_MTIzlZWfayLDVhx_b5gIEN6uQ6MGtpUHt5qoavNGruHlNjIsW5J0fOiV7BAxa8QXbeAqNGaNUa-VZ-mxKqhX92xNYq108tEjfivMTeDMYcz1pQU6Jk5zcEfP91qdIhqlbdoNWlIYAPROXm342k7je-oWaPUjS8mEBLHeX81hfIqfsngHclIRwDFVBUgtJNEMwiWnYepL6J5Qr88EyiqBE55c9UPClkhyjl2cIpw51JHfuW8ON6vpMFQUOdzPRRqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر  رشقة نحو الاهداف المعادية في مضيق هرمز</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/89738" target="_blank">📅 00:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89737">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انباء عن اطلاق صواريخ من إيران نحو اهداف معادية</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/89737" target="_blank">📅 00:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89736">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">انباء عن اطلاق صواريخ من إيران نحو اهداف معادية</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/89736" target="_blank">📅 00:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89735">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انباء متداولة استهداف ثالث لسفينة ايرانية قرب جاسك</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/89735" target="_blank">📅 00:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89734">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">كوريا الجنوبية ترتعب وتوضح:
إيران تعرب عن اهتمامها وتطلب توضيحات بشأن التقارير المتعلقة بتورط كوريا الجنوبية في مضيق هرمز، كوريا الجنوبية وفرنسا ناقشتا الأدوار في أمن مضيق هرمز، وليس نشر القوات.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/89734" target="_blank">📅 00:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89733">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي:
الضربات الأمريكية على أهداف إيرانية لا تزال مستمرة.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/89733" target="_blank">📅 00:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89732">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇷
تعرضت ناقلة نفط إيرانية تقع على بعد 4 أميال بحرية من جزيرة خارك لهجوم صاروخي من قبل القوات الأمريكية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/89732" target="_blank">📅 00:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89731">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
‏شنت إيران هجوماً جديداً على سفن البحرية الأمريكية يوم الاثنين، وهو هجوم لم يعترف به الجيش الأمريكي، وذلك بعد إطلاقها صواريخ باليستية على حاملة طائرات ومدمرة صواريخ موجهة خلال عطلة نهاية الأسبوع. لكن المسؤولين الأمريكيين يخشون أن تكون إيران تستخدم أسلحة أكثر تطوراً، ربما بمساعدة صينية أو روسية.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/89731" target="_blank">📅 00:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89730">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇷
تعرضت ناقلة نفط إيرانية تقع على بعد 4 أميال بحرية من جزيرة خارك لهجوم صاروخي من قبل القوات الأمريكية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/89730" target="_blank">📅 00:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89729">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مصدر إيراني لنايا
اصابة مباشرة لسفينة أمريكية في خليج فارس</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/89729" target="_blank">📅 00:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89728">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇺🇸
🇮🇷
‏
مسؤول أميركي:
استهداف ناقلات إيرانية ردا على هجمات على سفينة حربية أميركية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/89728" target="_blank">📅 00:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89727">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fskNSLgVRLFJafzUPYfCNoRpYJLTsVrM_PY8IR-nkyx307zUf3EcQ_VQ3oa7KgJ4Eg_wkiUzVf4ukTtkOk-38UfixnlLbja2hVXx6wE3UpidD4Pk3VFmjgcQagps9axZ1H_ZvRpIT9ZHwmXYhhY0xVyibeaq_-Wi4ZYJfWQbf6nPaEPfAWgE8AQR9UMDEhIf3wmDwBatE1p1oATfdwRjqBzD2FZW-eoKwTsSiiiX4jETHSMlGATCiWIo0nLifA2CiykS_H92QiCePhwjG8lTFsOncXtSzxIoufi0RXBo5ndTpDeqbhAG0q1R3npdfgpDG_HMMXL_jfP0NdhMR09dAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
إلى المواطنين والمقيمين والعاملين في البحرين و الكويت:  سيصدر إنذارٌ عاجلٌ قريبًا. يُرجى ترقّب البيان.  يتبع</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/89727" target="_blank">📅 23:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89726">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-oWQLGckJkBN2BqJVZYoSCtgFtpGuaiLT2KdiWtJcSsP3gcNvAfo9IA58JXLpyjotqTFGSEn-ML2uM-2NLOcYTW1r1dL7VxUA0-aYgDmTedN8enYypmKxNsU6WvxpTCKnCb78J983QjOvH1N-EzZxUgqTcd3eFL4S4UYEn4kBwOXDbxQEnZEzqe8eiPTx6U6WnAkDkx8dK6RB4xWMdwgaRMPkDbrs2DInpkCY8hxg1fMMQpHL4ipV4vWLpVxnuo6kj9mq0gBDybLlplSO__agFTm4UbC88zsJfmokxA7UQx-o0bXj5FHiPESf0UPjETFDiU8xHU06C50_7npDReOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
إلى المواطنين والمقيمين والعاملين في البحرين و الكويت:  سيصدر إنذارٌ عاجلٌ قريبًا. يُرجى ترقّب البيان.  يتبع</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/89726" target="_blank">📅 23:37 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

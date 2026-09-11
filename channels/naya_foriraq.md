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
<img src="https://cdn4.telesco.pe/file/L1wWB6kRB8LxsPNPvgswWKQVNorwrj6LNIs_dDMiGIG2dnmUSNHFj2gu2A-wMCgzY8M7A1Cs1uyQSFfiML8scUlTCakhdAjgW5d8qf0sVFrzElwYW5FaTeouzW1kzOW3x-G_rFqghye8J-iZIQ0CFK4xQN5GQ85RZ2Hi2UF53IiqlqsfhxZ37npqAtZgC06A9fwAlisq8UJ1rU5HuXytzdUFaeLcjKBnPJP3aBahXtKbcUTJ9_mkTgocH7QEe0T3Dds168KLIG5evINjPj0I7pVPtNYaCW3o3QcHufZ4WMGU4jGc_x3lr3yPWaET5JaHzi2-lLFLpKEY8Zc8sMD8mw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 15:07:06</div>
<hr>

<div class="tg-post" id="msg-90176">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اعلام العدو: المنظومة الدفاعية تتأهب بشكل استثنائي شمال ووسط البلاد</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/90176" target="_blank">📅 15:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90175">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0d1DPQZP-26MQYOatDWUg7jJUSoKiQ3DXraWOs381l2eg2eHT3VtWNDsG5W_9jTKjbY_r3Ifh7KvoI_EsZDBChFmhvRMcBHxwfeszgsOFqhujU7usY3stCnSdV6FNF51HoH0_iIOQmFfqM8SprlelLmckQosegGgnZfbUGnxGDm2YWHlBSa_Ak3m9bxn9RoCzCVDJPNVCvrJZj9ogWeYKKinH5s4gHW5xmOZVBS-L0rXRzkE1T2NbeDdCrEdvRtZss2JEMpdYLV2cvmRaW5kn9EhRDiB3XfC86Am1X4shXrc5L-vcP-6meUVo3YsmQU-Ln1GHD8DebKIIqgCXbIdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اسعار النفط تنخفض قليلا وتصل الى 104 دولار للبرميل بعد تقرير امريكي عن مساع لاتفاق مؤقت مع إيران بشأن مضيق هرمز.</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/naya_foriraq/90175" target="_blank">📅 15:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90174">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">القوات المسلحة اليمنية في باب المندب</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/naya_foriraq/90174" target="_blank">📅 14:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90173">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f399cdb5f0.mp4?token=lLgdOypK6JxorLKupsmYidL1zp3z8Vuw2VLDnGmPgGJ8v-TG7AgnhtKw_RcVlWrWY6LnMmy4O7pYUfwEOjAlpnw-5XkBwinEOhu6GuArD8r7rb_WAvZ7QoVETW2Jame6TkWWtIfmYwMGbJyUl5LdTyskfi8YoZ8x05BQk21_sJqAgeaobWAhQYaOcetv9m3UevxcBDlPI4LTLoPqQBLNOAnGKPLZR3tzJ4PcbH2LWlVczwGTVQHDLKx5hfOW9Sjg9nqjeMotZnOY5v_YKq5UC9H1BX2yDgOxoeXDuDHEaWsoukJRXz25neC3QI4nlswE4MR0cI-JSl-YOPh2ePeyfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f399cdb5f0.mp4?token=lLgdOypK6JxorLKupsmYidL1zp3z8Vuw2VLDnGmPgGJ8v-TG7AgnhtKw_RcVlWrWY6LnMmy4O7pYUfwEOjAlpnw-5XkBwinEOhu6GuArD8r7rb_WAvZ7QoVETW2Jame6TkWWtIfmYwMGbJyUl5LdTyskfi8YoZ8x05BQk21_sJqAgeaobWAhQYaOcetv9m3UevxcBDlPI4LTLoPqQBLNOAnGKPLZR3tzJ4PcbH2LWlVczwGTVQHDLKx5hfOW9Sjg9nqjeMotZnOY5v_YKq5UC9H1BX2yDgOxoeXDuDHEaWsoukJRXz25neC3QI4nlswE4MR0cI-JSl-YOPh2ePeyfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انصار الله يقضون ساعات مميزة في ميناء المخا بعد طرد مرتزقة السعودية منه</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/naya_foriraq/90173" target="_blank">📅 13:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90172">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQJlllDHCkWovB6CBRoOb_4PYWViAalgUER49pmREJs4EwGed9A1o8Cxm0Ty_QUL6iaU4uH_HU52dwd0bOtTBaAU29EkYyxNuLy-bIT6wkWOguKuFbPHvdj--s6NJL96UVcsyC62UAgmV7ShWO265yE2Nxob8gabXl-EXgCYP2DDCkEwFuBEzeb-wgOTHrKjTv7ATGkUv-sJuPBZwf0h1320p5AMYO83tox7jrNB4XuxvF4PzExhBHXhW1JQBd36mO97lOJ9UY0wMdeKxiuhEOSd5bXRTRJHi9OYq87-l4s4Ox8nYCKYPLLDvzUAaH72PC7sbNSQrmzZPqVTWwE47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو انصار الله حزام الاسد:
في سياق معادلة «التصعيد بالتصعيد»، فإن أي استهدافٍ للبنية التحتية أو المطارات أو الموانئ في المخا وذوباب وميون وغيرها من المناطق اليمنية، من قِبل نظام العدو السعودي، سيُقابَل بالمثل.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/90172" target="_blank">📅 13:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90171">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">الاعلام الاجنبي: انصار الله سيطروا على جزيرة ميون واستكملوا السيطرة على مضيق باب المندب.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/90171" target="_blank">📅 13:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90170">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇺🇦
انفجارات عنيفة تهز العاصمة الاوكرانية كييف</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/90170" target="_blank">📅 13:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90169">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔻
الرئيس التنفيذي لمطارات دبي بول غريفيث:
دبي تدرس نقل أجزاء من مطارها الجديد تحت الأرض، بما في ذلك تخزين الوقود، للحماية من الضربات المحتملة بالطائرات بدون طيار والصواريخ في أعقاب الحرب الإيرانية.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/90169" target="_blank">📅 13:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90168">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">القوات المسلحة اليمنية تستهدف تجمعات المرتزقة في رأس العارة بثلاث صواريخ باليستية</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/90168" target="_blank">📅 13:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90167">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مسؤول باكستاني لرويترز:
باكستان تحاول التزام الصمت في الصراع السعودي الحوثي الحالي لأن مصالح باكستان الخاصة كبيرة ولا تريد إفساد العلاقات مع إيران.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/90167" target="_blank">📅 12:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90166">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">عدوان سعودي على ميناء المخا</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/90166" target="_blank">📅 12:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90165">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇾🇪
بيان مرتقب للقوات المسلحة اليمنية للإعلان عن عملية عسكرية واسعة ونوعية.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/90165" target="_blank">📅 12:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90164">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/968111c504.mp4?token=ahYPnzxMx-ujhKJLdEpvBhU4VD6v37HyHGM9-iuavxv6Y5jSn_Xu3xeCviTLMGwJT_46hhPoHUFE-8oY9xzbsws4yH26Cl40meeGiBF1K2j5VCZmBoOx3ZmKAWx-YHS0SfCbsqSgkqpw9GG-cVKeWCvH_gqiahawYYZbflGDMwwd8G7BWh-kGSMsL8z8XFAPEZbvZk6OrvvDasMgkaT0onNHD_umijRxDVD2dq3l79BV9N4C8Lr-l4kW0-IHLdgB83FD4SSC_1o3MNzDwcGemZ8fADpM1d6VYJrKCN-O-s5OhSt39vDkYa5bNmJTs-gH9ZyuFWMl88_GZW6MTGsKeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/968111c504.mp4?token=ahYPnzxMx-ujhKJLdEpvBhU4VD6v37HyHGM9-iuavxv6Y5jSn_Xu3xeCviTLMGwJT_46hhPoHUFE-8oY9xzbsws4yH26Cl40meeGiBF1K2j5VCZmBoOx3ZmKAWx-YHS0SfCbsqSgkqpw9GG-cVKeWCvH_gqiahawYYZbflGDMwwd8G7BWh-kGSMsL8z8XFAPEZbvZk6OrvvDasMgkaT0onNHD_umijRxDVD2dq3l79BV9N4C8Lr-l4kW0-IHLdgB83FD4SSC_1o3MNzDwcGemZ8fADpM1d6VYJrKCN-O-s5OhSt39vDkYa5bNmJTs-gH9ZyuFWMl88_GZW6MTGsKeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الضربة الجوية التي استهدفت اوكار عصابات داعش الارهابية في وادي الشاي شمال غرب العراق.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/90164" target="_blank">📅 12:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90163">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇾🇪
🇸🇦
طيران العدو السعودي يشن غارتين على مطار المخا.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/90163" target="_blank">📅 11:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90162">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFOoceImzIZditsDtqfyHeNJHoySS4Z_0dSpDuYrHXhykSym09JCApsP0bTFHUPBKxbvkYwU6yrOoB6cO_KT1JglYS2cLhoNfmTVhUVlLQFatcvcw7WYq4NkgRL77MrdL-ss6b90pFjyjvGX6UT4e3L3_0Az5EqXk38CJCTVCCDqdfw-8vAnIa_lkaY-0oV_gz6MOCHKeTecGskKCmdKwySCDbyRklfdwWTXHxwVNnTdPJBwt29Oa5VIAKZXyzKcPiswD5YZJPx5Vycbk1R11o43GuSy9NoONiEM6r5ZZMXyw8k8GHSk3vGjFLfqvpwI7MHzcS272PEJ6zDjHRTquQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
رويترز: الحوثيون وصلوا إلى مدينة ذو باب الساحلية على مضيق باب المندب.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/90162" target="_blank">📅 11:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90161">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الاعلام الاجنبي: انصار الله سيطروا على جزيرة ميون واستكملوا السيطرة على مضيق باب المندب.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/90161" target="_blank">📅 11:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90160">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇾🇪
🇸🇦
بعد القصف اليمني الاخير امتد الدخان لاكثر من 100k عبر صحراء السعودية.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/90160" target="_blank">📅 11:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90159">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وكالة الطاقة الدولية:
من المتوقع أن يبلغ متوسط ​​إمدادات النفط العالمية 100.7 مليون برميل يوميًا في عام 2026، بانخفاض قدره 5.7 مليون برميل يوميًا عن عام 2025، وأقل بمقدار 1.3 مليون برميل يوميًا عن التوقعات السابقة، مخزونات النفط العالمية انخفضت 95 مليون برميل إضافية في أغسطس.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/90159" target="_blank">📅 11:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90158">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24fee932a6.mp4?token=lskUs5idFbT_PvsbsYWlnO9jA8c_9D_M-KFXzUybo4tngHAtN84kpdEOI2vWc1VVtwiAvsOcqKB4s-D04ED3LtYDQczB3vbmPK92aSSvEe4i6JWdLR6FlJ_mExu0f7CFXXOOwSznV6x45G_Q9Qnt6CWfqXQMdONBWsdjV3Fah9Yvq4jBl6dV4BGQ-gr2hxb8S9h261-zCF6pOVIdvMmyUsW0Qt00CIsfYW2gTdJKgIvMAT4Hpr6uEZw_wCUa5mky4I-huCVW67aL2qH-6p4ZlceguzVGTYLl2-lGARnaBUb_pSzVoDP0vkxcJ4VHD9sWfvPvcCRqLOrOUlpyyxa8tDmginZSSmJWax4ozJsh_K6LeqD03ZyhT4HrizOP5JP7TyDoWXkngtcniXRwf850iBNmEQfFVnq98sxGFEoK_cZh7guXiAX6okkWglx9_C4GVblOJ-lAm1lEIu-cPL8LKZw7rPRgLKj6W0hauFbxvdrZOWymlOnavOhR4nrQDYjUm4CNVwHxIyZQFGw-HRC1FdvyQw0-FatvpsbIxP5UzWnYdrjO44u--9PwexoCp2hGcZqvzY-LigFtBwkKDr5UmOafccF6WmvpLYbqSdq__UmCp9oPuGlKogFJsSPHWC4IbsBeru0UBvZfhPK_BUM3Epy8iNh6OaquTXpR8AyTMLs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24fee932a6.mp4?token=lskUs5idFbT_PvsbsYWlnO9jA8c_9D_M-KFXzUybo4tngHAtN84kpdEOI2vWc1VVtwiAvsOcqKB4s-D04ED3LtYDQczB3vbmPK92aSSvEe4i6JWdLR6FlJ_mExu0f7CFXXOOwSznV6x45G_Q9Qnt6CWfqXQMdONBWsdjV3Fah9Yvq4jBl6dV4BGQ-gr2hxb8S9h261-zCF6pOVIdvMmyUsW0Qt00CIsfYW2gTdJKgIvMAT4Hpr6uEZw_wCUa5mky4I-huCVW67aL2qH-6p4ZlceguzVGTYLl2-lGARnaBUb_pSzVoDP0vkxcJ4VHD9sWfvPvcCRqLOrOUlpyyxa8tDmginZSSmJWax4ozJsh_K6LeqD03ZyhT4HrizOP5JP7TyDoWXkngtcniXRwf850iBNmEQfFVnq98sxGFEoK_cZh7guXiAX6okkWglx9_C4GVblOJ-lAm1lEIu-cPL8LKZw7rPRgLKj6W0hauFbxvdrZOWymlOnavOhR4nrQDYjUm4CNVwHxIyZQFGw-HRC1FdvyQw0-FatvpsbIxP5UzWnYdrjO44u--9PwexoCp2hGcZqvzY-LigFtBwkKDr5UmOafccF6WmvpLYbqSdq__UmCp9oPuGlKogFJsSPHWC4IbsBeru0UBvZfhPK_BUM3Epy8iNh6OaquTXpR8AyTMLs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
بعد القصف اليمني الاخير امتد الدخان لاكثر من 100k عبر صحراء السعودية.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/90158" target="_blank">📅 11:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90157">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الاعلام الاجنبي:
انصار الله سيطروا على جزيرة ميون واستكملوا السيطرة على مضيق باب المندب.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/90157" target="_blank">📅 11:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90156">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/90156" target="_blank">📅 11:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90155">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAljRYBTqT9bKa6Iykzq67r2JK6QHw5X5nhpGS-wJE0hORib9I8nBO63NHHtpPEtrBdgGe5CZMCNisTSc8SZXODFTF2Kc-xpZNUN45ieHOvQL6HfNJdOjNFs97BCio1eSQO0O06Ssj_81ngkhhVKP25CQ3fPtKrHACkV-aYZeW7s_Bxrop8lddvZsnAlVqhT5PIUCDA2g2Iiz4TGWQM6A_X8JFlh3CgA7-4EAlqcd83yVlFRshYrOoXbUzu12MKvVH40ys5DsfPvWme2a09Pi0vUY-zm3syzSK-frysvlK2tjzj0ftVgCTrbyl5lFS6Ql4bPCBvXAXU4IYlg77lI8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
جمهورنا الكريم
...
🔻
لغرض التواصل معنا ونقل مشاكلكم وارسال الاخبار والمواد الصورية والفديوات ، سنكون على مدار الساعة معكم نجيبكم.
للمراسلة
@Nayaforiraq_bot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/90155" target="_blank">📅 11:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90154">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/324d248f2d.mp4?token=IjxuGE9qAj7GFmvnrW5XlD7rmga3mZTU77QiEnR8Q_MnQxqcUtPayu_9uINf9vJLouY0pw9nQ9NWWK3PQaBZYXvwtCyVZ85qrur9R_9J67znTG5kv2f0g7-g5fk6fB-aJOTu0bdIlpaBeczFmN5-0DXBftY7wODjA1RDF008bv_U5L3T92S2usWVCvhx-10Etmc9SotuM0mpFTWXgSg_IjF6GFEDu_ZtYKjwDa5jXku_dI8-ycAxd0LnbeWkBUWdmx4WmXFC-vRN3tspQPUQVhYH9mM3X01IQwm3n_8RAMLdbmiyG5YcEr1Xm-6QeRHpiaVV28JH1LwVvNtOBAGeHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/324d248f2d.mp4?token=IjxuGE9qAj7GFmvnrW5XlD7rmga3mZTU77QiEnR8Q_MnQxqcUtPayu_9uINf9vJLouY0pw9nQ9NWWK3PQaBZYXvwtCyVZ85qrur9R_9J67znTG5kv2f0g7-g5fk6fB-aJOTu0bdIlpaBeczFmN5-0DXBftY7wODjA1RDF008bv_U5L3T92S2usWVCvhx-10Etmc9SotuM0mpFTWXgSg_IjF6GFEDu_ZtYKjwDa5jXku_dI8-ycAxd0LnbeWkBUWdmx4WmXFC-vRN3tspQPUQVhYH9mM3X01IQwm3n_8RAMLdbmiyG5YcEr1Xm-6QeRHpiaVV28JH1LwVvNtOBAGeHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
انفجارات عنيفة تهز العاصمة الاوكرانية كييف</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/90154" target="_blank">📅 11:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90153">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇶🇦
🇺🇸
الاعلام الاميركي:
قطر  أكبر مُصدِّر للغاز الطبيعي المسال في العالم قبل الحرب - تجري الآن محادثات لشراء الغاز الطبيعي المسال الأمريكي بموجب عقود طويلة الأجل.
هذا تحول مذهل.
أدت الحرب الإيرانية إلى تعطيل اثنين من أصل 14 وحدة من وحدات الغاز الطبيعي المسال القطرية في رأس لفان (مدة الإصلاح من 3 إلى 5 سنوات، وخسارة في الإيرادات تبلغ حوالي 20 مليار دولار سنوياً)، كما أن مضيق هرمز شديد الخطورة على حركة ناقلات النفط المنتظمة.
النتيجة: انخفاض بنسبة 96% في الصادرات - 18 شحنة فقط تم شحنها في ستة أشهر مقابل 509 شحنة في نفس الفترة من العام السابق، بتكلفة تقدر بنحو 24 مليار دولار.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/90153" target="_blank">📅 09:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90152">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇺🇸
🇸🇦
سي ان ان: الولايات المتحدة توسع أنشطتها الاستخباراتية، مستهدفة دعم الحملة السعودية، ارسلنا أكثر من 100 مستشار عسكري أمريكي في السعودية.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90152" target="_blank">📅 09:22 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90151">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇾🇪
مصدر يمني:
تم أسر 2000 جندي من مرتزقة السعودية، مع عتادهم العسكري في جزيرة زقر وحنيش وميون على يد القوات اليمنية البطلة.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90151" target="_blank">📅 05:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90150">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33e117b174.mp4?token=wASShXabUKNsejrzRQeN-bLDvRCTScgQOelKmpUrP_HqsNvETfMQgxBbz5-FIBrDMyhyJU0Lq-5_yaSGS-J8sDTD5_YHv89EyYA2Ac3VHt-T9JIEbWS-HDO_YknGpN5nd28-qYyaLAbgCLkoPyi016CglxiKNHTpQsWN67G6hK8hWMb8BfEIxa1-DnGYZTGjmiVRQxdIirzfH1NNRfKpddo2kX8u8-s5beD3DWHtkXdzoETshliudeNvZJEjO7yTc5dEUQbe5VlPfTzYHqchakxK83UM-BRamGFkB5pLML29JcwoPe3CVWnP98paEBc81l7ExP3fEXyipWw-aLcuzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33e117b174.mp4?token=wASShXabUKNsejrzRQeN-bLDvRCTScgQOelKmpUrP_HqsNvETfMQgxBbz5-FIBrDMyhyJU0Lq-5_yaSGS-J8sDTD5_YHv89EyYA2Ac3VHt-T9JIEbWS-HDO_YknGpN5nd28-qYyaLAbgCLkoPyi016CglxiKNHTpQsWN67G6hK8hWMb8BfEIxa1-DnGYZTGjmiVRQxdIirzfH1NNRfKpddo2kX8u8-s5beD3DWHtkXdzoETshliudeNvZJEjO7yTc5dEUQbe5VlPfTzYHqchakxK83UM-BRamGFkB5pLML29JcwoPe3CVWnP98paEBc81l7ExP3fEXyipWw-aLcuzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
عقب تحريرها من مرتزقة السعودية..
القوات اليمنية تقوم بتأمين الأحياء والمحلات التجارية في مدينة المخا.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/90150" target="_blank">📅 05:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90149">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/510c41afc7.mp4?token=kcR7TW4s2F0u6nwfoFJd-7UzwaGdrYduP5jwIJkH7QOyYArVcXPEk4wIBi5QnXeSuBHGqKk8LNBismqQKHdiE_bTqV7xgF0waMQmwJkMnIY6qsXJ9qgEYi1wnlmkYE-O52mVsU6DKZ0A96IL1wHAQQEYlND-0ClmC86DR8cUHrRX791F9E4pjAvknNRJkUjIe5O2OItoBCqRWVlhQlwVPtP6XM6F5IRA1ej4m1M7-CxAet12nB_wggC8MBbAIShi88JJq9DRegMQk6E3ZnqZE42BICKFuFEEeXStvdwbH1R5YPst-Go1aELjqmMBbGo0SS_58kTUL6DkVd2ovOVcl2NrVSjFisNCoDLzpD5PzHSdI17XmS4i3IaafANlo8tzFSunBHj-G8-TZKdJ7kEnvJuqjhWzSZze-K0PCTiYSViOsLtt7EN3aiwDLWr5AxSAQtFPf2a7JvnqyOMG9bqi-AG_Nu0BcHjQYSM5Iknqho8rhxjKRG2um6nk5EsRLoHn95F6jcEpw0kQILrBk4aWCNvYi-9KGtdAFDWv3KWj3Nth_LnJwvEGxEgx4P73-1yahFPZMGizgi46s0Gw7JaZYzdNFlz5HUX-vA5812FBWRDps3gjAXf2-RGyJ8sTfgiMDfTyYfIWbRyeAvKUo4DKa4CU7lWuvcdOkPa3jtqZqes" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/510c41afc7.mp4?token=kcR7TW4s2F0u6nwfoFJd-7UzwaGdrYduP5jwIJkH7QOyYArVcXPEk4wIBi5QnXeSuBHGqKk8LNBismqQKHdiE_bTqV7xgF0waMQmwJkMnIY6qsXJ9qgEYi1wnlmkYE-O52mVsU6DKZ0A96IL1wHAQQEYlND-0ClmC86DR8cUHrRX791F9E4pjAvknNRJkUjIe5O2OItoBCqRWVlhQlwVPtP6XM6F5IRA1ej4m1M7-CxAet12nB_wggC8MBbAIShi88JJq9DRegMQk6E3ZnqZE42BICKFuFEEeXStvdwbH1R5YPst-Go1aELjqmMBbGo0SS_58kTUL6DkVd2ovOVcl2NrVSjFisNCoDLzpD5PzHSdI17XmS4i3IaafANlo8tzFSunBHj-G8-TZKdJ7kEnvJuqjhWzSZze-K0PCTiYSViOsLtt7EN3aiwDLWr5AxSAQtFPf2a7JvnqyOMG9bqi-AG_Nu0BcHjQYSM5Iknqho8rhxjKRG2um6nk5EsRLoHn95F6jcEpw0kQILrBk4aWCNvYi-9KGtdAFDWv3KWj3Nth_LnJwvEGxEgx4P73-1yahFPZMGizgi46s0Gw7JaZYzdNFlz5HUX-vA5812FBWRDps3gjAXf2-RGyJ8sTfgiMDfTyYfIWbRyeAvKUo4DKa4CU7lWuvcdOkPa3jtqZqes" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
إنهيار مبنى قيد الإنشاء قرب جسر الصرافية بالعاصمة بغداد، وأنباء عن مصرع 8 عمال كحصيلة اولية.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/90149" target="_blank">📅 04:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90148">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇾🇪
غنائم من مرتزقة السعودية في أيدي أبطال القوات اليمنية.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/90148" target="_blank">📅 03:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90147">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3fbe7e70.mp4?token=c-OM1JV1kjzEOkYArrHzg_OWp-51p7-DB2j8_uszR4UgK9j_7gEcnyq8tWlJc9QWyXDokuoBgShaBcRcXrLmgPFvpZxIpC2aBrLR74piTKZAmW61411UvpHvOxktdH95RInu7uiSO3czWjVGIso22Eqf1qCoqM9pHdlfniIPbujeMNsutqNZ85vNqDNNuk057yrxWOMQJ-3SA34jbMtH3Po6G28X-cJ_Ti-ZZ4v1sQ6q93dos_QTvrywywpBQfq93_J0mZAI15enmFJlgAzFwbnC0dgQPjLhhJ-UqJfmdtxtT3OSQheY6tAVpk8QJY_opNfbd7d-YFGbhqu82G5CCi_a4Md3vqFO6RujVQVsPrY0quo5f_EcUz5ncZU4fBRRkeQU3SRCvo3YRzpCxt7VQ9NAIfg59j_ODPJDAUpxlw93ukcS_1_fjzRafAx54n6bqbUSiy9ZUT-v_q1T-TcCVb6-rn2mK4YHpFgVNRXRgrWdlEmilu9RoWXKJzUMTe1IclNfW9lghom7xBnb9iavUT6IR4N0X2NOrwlLET4E6ZnS5A0gQ1I8Q8unADliajyCOuxuGBe5o_VQV40xnoeaO-1dIqxmsEaNtAWYop6dthSBKFpYCwFXFaHwcYwH3KYiCtwvtCh_SzNZ0pJJM9sVpZDA5jIyPYf7CXHp0DeUmoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3fbe7e70.mp4?token=c-OM1JV1kjzEOkYArrHzg_OWp-51p7-DB2j8_uszR4UgK9j_7gEcnyq8tWlJc9QWyXDokuoBgShaBcRcXrLmgPFvpZxIpC2aBrLR74piTKZAmW61411UvpHvOxktdH95RInu7uiSO3czWjVGIso22Eqf1qCoqM9pHdlfniIPbujeMNsutqNZ85vNqDNNuk057yrxWOMQJ-3SA34jbMtH3Po6G28X-cJ_Ti-ZZ4v1sQ6q93dos_QTvrywywpBQfq93_J0mZAI15enmFJlgAzFwbnC0dgQPjLhhJ-UqJfmdtxtT3OSQheY6tAVpk8QJY_opNfbd7d-YFGbhqu82G5CCi_a4Md3vqFO6RujVQVsPrY0quo5f_EcUz5ncZU4fBRRkeQU3SRCvo3YRzpCxt7VQ9NAIfg59j_ODPJDAUpxlw93ukcS_1_fjzRafAx54n6bqbUSiy9ZUT-v_q1T-TcCVb6-rn2mK4YHpFgVNRXRgrWdlEmilu9RoWXKJzUMTe1IclNfW9lghom7xBnb9iavUT6IR4N0X2NOrwlLET4E6ZnS5A0gQ1I8Q8unADliajyCOuxuGBe5o_VQV40xnoeaO-1dIqxmsEaNtAWYop6dthSBKFpYCwFXFaHwcYwH3KYiCtwvtCh_SzNZ0pJJM9sVpZDA5jIyPYf7CXHp0DeUmoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مشاهد مذلة لمرتزقة السعودية حيث مرتزقة الإمارات تمنعهم من دخول عدن عقب هروبهم من المناطق التي سيطرت عليها القوات اليمنية البطلة.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/90147" target="_blank">📅 03:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90146">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇾🇪
🇸🇦
‏الأرتال العسكرية المتبقية من مرتزقة السعودية تهرب من راس العارة بعد دكهم برشقات صاروخية من قبل القوات اليمنية.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/90146" target="_blank">📅 03:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90145">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44e27a0041.mp4?token=s39tC5zgq_766LoAvEthMVmGTVaXr1U3thcK9ILvyIzYYAMlQFI4uZibqul5416E7kYNd50S2hRnxweeksWLi7UtMLXi2NVJCjfEJQCkg4IdSG8lpDW33Ad_dyUrJ7a_hb4IBXOUFmu6WjhPt9ZDuf5koiAfn4gqqYqEeU__0Rmjuq4snGrSVI7MZAThmT_qCEt7bLXOHbjGJq7WZsOi5mEylMCD8w1gAoYFxaByboPMN2txoHHQHIKal74HMWYTWb3mjtxsMJdLJs_v9J6vxClaUbwxwJiRdQjf9RoHlG5nRyCgsBGXF8pQbPONAo0xysNNOS7ul-WD5nuVEkXsGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44e27a0041.mp4?token=s39tC5zgq_766LoAvEthMVmGTVaXr1U3thcK9ILvyIzYYAMlQFI4uZibqul5416E7kYNd50S2hRnxweeksWLi7UtMLXi2NVJCjfEJQCkg4IdSG8lpDW33Ad_dyUrJ7a_hb4IBXOUFmu6WjhPt9ZDuf5koiAfn4gqqYqEeU__0Rmjuq4snGrSVI7MZAThmT_qCEt7bLXOHbjGJq7WZsOi5mEylMCD8w1gAoYFxaByboPMN2txoHHQHIKal74HMWYTWb3mjtxsMJdLJs_v9J6vxClaUbwxwJiRdQjf9RoHlG5nRyCgsBGXF8pQbPONAo0xysNNOS7ul-WD5nuVEkXsGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:  ستنتهي حرب إيران مباشرة بعد الانتخابات النصفية الأمريكية.  الإيرانيون يواصلون القتال بصعوبة وهم في مأزق عميق.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/90145" target="_blank">📅 03:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90144">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8be127dc55.mp4?token=VZHG_SbZ6jpz4zqIX-SdGh_rvCTsx6JtVi7rqu2ZBPXUXTG4re678LQlypQlYyB_vs1pJvpubz6wpFHgtY1Po_Z7T5W7S-60UkSPLOyh0ky62x4SQTuycPUWRShvq3vYak0MPMf2Cpo4QBgvSTOARgOGqi2-5IjlRuium2ojePZe4Seo41zkZxMXGVoUtwgrQrCVLgJmjCfZh1-3aKCmMsX1BbhBdKtQl5VEtCyatnYWGhUN1xfsAL7Uc79b8HArbB8fu7gS_PwkvUeIrR1PLih2zEjt2cmXeE5h6jAyZnmrXz8FUJl5_w-JnIQKM-D-o9Wgz3NOikzXm7mldVTeI2OTTe6E9yuVgFFlMDU-9XKOEBVNWCdW7Wcw20VhTUsgPLjYzJ631je8os9l5H5euB8f-FIDMUib8pBFCRAuy_sGETDwW2n1tRncGQTZF0nfdTdVgRj1I-20auu9zlik-GakuuChP3vNK6ueXa_hhmzbvrIqhXqMrRNYhAGmA9HBzJTY4g1F9PCfZ7dPnFYERvQlP6zAfcvATMWNMmCLsSHmWTlbUM5tol8e95Vb6YbP0T1pGyrsp5jhbW9aYPVjAflZNX2yvIZWWWXSf6-xIJjjOQzc-Ehx9VznNRWMzahOW97erZyQkV_O1tusy0QGnaEisSWyQIIij1kma2yhTRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8be127dc55.mp4?token=VZHG_SbZ6jpz4zqIX-SdGh_rvCTsx6JtVi7rqu2ZBPXUXTG4re678LQlypQlYyB_vs1pJvpubz6wpFHgtY1Po_Z7T5W7S-60UkSPLOyh0ky62x4SQTuycPUWRShvq3vYak0MPMf2Cpo4QBgvSTOARgOGqi2-5IjlRuium2ojePZe4Seo41zkZxMXGVoUtwgrQrCVLgJmjCfZh1-3aKCmMsX1BbhBdKtQl5VEtCyatnYWGhUN1xfsAL7Uc79b8HArbB8fu7gS_PwkvUeIrR1PLih2zEjt2cmXeE5h6jAyZnmrXz8FUJl5_w-JnIQKM-D-o9Wgz3NOikzXm7mldVTeI2OTTe6E9yuVgFFlMDU-9XKOEBVNWCdW7Wcw20VhTUsgPLjYzJ631je8os9l5H5euB8f-FIDMUib8pBFCRAuy_sGETDwW2n1tRncGQTZF0nfdTdVgRj1I-20auu9zlik-GakuuChP3vNK6ueXa_hhmzbvrIqhXqMrRNYhAGmA9HBzJTY4g1F9PCfZ7dPnFYERvQlP6zAfcvATMWNMmCLsSHmWTlbUM5tol8e95Vb6YbP0T1pGyrsp5jhbW9aYPVjAflZNX2yvIZWWWXSf6-xIJjjOQzc-Ehx9VznNRWMzahOW97erZyQkV_O1tusy0QGnaEisSWyQIIij1kma2yhTRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
إستهداف صاروخي للقوات اليمنية على تحشدات مرتزقة السعودية في منطقة رأس العارة غربي محافظة لحج، يجبرهم على الهروب والإنسحاب.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/90144" target="_blank">📅 03:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90143">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44ae578a02.mp4?token=CQajoxSpNd0FkWLvwdtWIyJF_7ehwGT68z39I2m8-O17wKDewO6iz7AfiMl6i8-JQPumsy--eG6CMKO8jmwf8GQ8J_maoN2mQ5qygGeLq4bgR0AGRbPvNLb2xOo8eTSsPOlKKCyK01X4PQmTDURCrhEbYoAqG7VrW5OTMBYquFYc53QagGNtIYGV6A1qvSyaM58qUizJHZYDzc-0V1QFpw1u7yW4ZF4rOzr97fRyu7CyxdNyYwbToIUBOn6v04_sewQImfOItmRXjDIlIkejhMvDuqxeqMFoIu9HD8CPREi_mwK1aOKuu0iOYvqehXYrcjaqmCHnYreTddWF6cwOSZf7jZK10PHNbxselXhDwqvaARMb1wRDm_M93VgNW50oDJ48lsOcvrjOVpSX3ltmxikRSUMa0INkD7hSr-B4o9gI10Cw5wzGO-6fB-kDpFVPqzXdXuJ-ATNIKf_jbhrt_vt9ERXEV7SSFBLjxkHOGyTVdWgbiRiyNBJKHD1Haev3gmeSHGDprzo5CVKwnl8v5zyzAT779bOA3hGHs6qoc5ZxfnQAjRLa2BLwOmqTp2AjgTefRlaM4hWDFIatb_1XE8gcP2JR7oh0FUgAL_Ol8zVVaFqYI7_a29HmrgCbqP4XyAVd5baFihdth7ZCJDxW51t24Dq74fCbdVIm7_p0QtU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44ae578a02.mp4?token=CQajoxSpNd0FkWLvwdtWIyJF_7ehwGT68z39I2m8-O17wKDewO6iz7AfiMl6i8-JQPumsy--eG6CMKO8jmwf8GQ8J_maoN2mQ5qygGeLq4bgR0AGRbPvNLb2xOo8eTSsPOlKKCyK01X4PQmTDURCrhEbYoAqG7VrW5OTMBYquFYc53QagGNtIYGV6A1qvSyaM58qUizJHZYDzc-0V1QFpw1u7yW4ZF4rOzr97fRyu7CyxdNyYwbToIUBOn6v04_sewQImfOItmRXjDIlIkejhMvDuqxeqMFoIu9HD8CPREi_mwK1aOKuu0iOYvqehXYrcjaqmCHnYreTddWF6cwOSZf7jZK10PHNbxselXhDwqvaARMb1wRDm_M93VgNW50oDJ48lsOcvrjOVpSX3ltmxikRSUMa0INkD7hSr-B4o9gI10Cw5wzGO-6fB-kDpFVPqzXdXuJ-ATNIKf_jbhrt_vt9ERXEV7SSFBLjxkHOGyTVdWgbiRiyNBJKHD1Haev3gmeSHGDprzo5CVKwnl8v5zyzAT779bOA3hGHs6qoc5ZxfnQAjRLa2BLwOmqTp2AjgTefRlaM4hWDFIatb_1XE8gcP2JR7oh0FUgAL_Ol8zVVaFqYI7_a29HmrgCbqP4XyAVd5baFihdth7ZCJDxW51t24Dq74fCbdVIm7_p0QtU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
‏المراسلة: لو لم نتناول ملف إيران، لكنتم ستفوزون بسهولة في انتخابات التجديد النصفي. هل لديكم أي ندم؟
🇺🇸
‏ترامب: لا، أنا لا أؤمن بكلمة "الندم". يمكنك دائماً أن تشكك في نفسك قليلاً.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/90143" target="_blank">📅 02:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90142">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/702b942a90.mp4?token=cV0nHTCuqX2QchmJp90Z-DW_DAlxmCLAuZSedXp_XHEIr6CkXfOf12A5qytrN-u_yvOaeDODniTqQSMj0AiXp9wbAqWCEBibCtOf9AnkTTvuC-pg6RVE2wW4lcmxnF2Hxm7h0215IzFH0K5eB61l0lD-w0XxK6t-xDpjZK4BKhlAe8ksld1uDyALMjriu5CBrfuekX0OXs3hP2ILBQUN3inBafiG_QSkULUWXU5jKJGMxs8sOYHtbpky0aTQNVp5nvhVog3v73jycddncOk_hTl8qCKxcmPGWozdBSgVEUvT04o8XKwsO8cE0VnVPcPgjSGAwVeCsAkIe4C3ybriDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/702b942a90.mp4?token=cV0nHTCuqX2QchmJp90Z-DW_DAlxmCLAuZSedXp_XHEIr6CkXfOf12A5qytrN-u_yvOaeDODniTqQSMj0AiXp9wbAqWCEBibCtOf9AnkTTvuC-pg6RVE2wW4lcmxnF2Hxm7h0215IzFH0K5eB61l0lD-w0XxK6t-xDpjZK4BKhlAe8ksld1uDyALMjriu5CBrfuekX0OXs3hP2ILBQUN3inBafiG_QSkULUWXU5jKJGMxs8sOYHtbpky0aTQNVp5nvhVog3v73jycddncOk_hTl8qCKxcmPGWozdBSgVEUvT04o8XKwsO8cE0VnVPcPgjSGAwVeCsAkIe4C3ybriDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
‏المراسلة: كيف ستتمكن إيران من إطلاق الصواريخ إذا قمنا بتدميرها؟
🇺🇸
‏ترامب: بإمكانهم دائماً إطلاق الصواريخ. كان لديهم الكثير منها.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90142" target="_blank">📅 02:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90141">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc0c2b690f.mp4?token=iF5WR5worrGl4aSMjeCsdVK9mNh2Kn4rf61PxQ9f929jJ3xhxmRFuVaPpfiFXwJOzVNRNId-0xzHn88EfAm2CZia0JjV5AX3MHx8r37ZQewBQvKi8dtTQdG5Bep10SHhw3ATY2mdAMVkWcSm1HMIJVzwpWpUPIiRknFd1PYSaDi4nC5mJsCoVCxdSamuLpkIQ3MlhOwQFIqlqixnMsth7UdNd30BAGGrJnwT-BKtE0NQDihRY8BV2HWwgUrSVkGjGR-jEwrvwvTHZzpd_406JM3dWvai3Ni1YK_59kCWn9XZWUAlhkGr5-sQ1s7ddNJlwK0zDRhLhCTVx803Wv3C5mkUrRR9NcziCrZw6ztG82y_wqHRNlLXKzlojXMIuNw_JqxVvkhl90Y6jOhWoFhluHg-OTJ6-Uaj_VQ2ShHVoUy9rjImQdqGmFHL8KdiLIxjzZ1CxNp6NUj0oD-eByppeih9MIYmzkY6Bx8aS8pqfp11dwLE5X9NKXjqUppe_HZjJLKJvgpHgxJl3zvGGITce5vQDLTHK73mIx6sJ2b6BHyrj9BUFW9JK459SkYisEPej_v8QPeeaTN3wObH3BVxay6jqxUTTRi79Xhra4mpRqMVlLD4-zYMe6A2LIeLvbl2hLDNBs3pwaaMYo-bbRtUcUj9X_p3-47wJyeT9pdqrVc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc0c2b690f.mp4?token=iF5WR5worrGl4aSMjeCsdVK9mNh2Kn4rf61PxQ9f929jJ3xhxmRFuVaPpfiFXwJOzVNRNId-0xzHn88EfAm2CZia0JjV5AX3MHx8r37ZQewBQvKi8dtTQdG5Bep10SHhw3ATY2mdAMVkWcSm1HMIJVzwpWpUPIiRknFd1PYSaDi4nC5mJsCoVCxdSamuLpkIQ3MlhOwQFIqlqixnMsth7UdNd30BAGGrJnwT-BKtE0NQDihRY8BV2HWwgUrSVkGjGR-jEwrvwvTHZzpd_406JM3dWvai3Ni1YK_59kCWn9XZWUAlhkGr5-sQ1s7ddNJlwK0zDRhLhCTVx803Wv3C5mkUrRR9NcziCrZw6ztG82y_wqHRNlLXKzlojXMIuNw_JqxVvkhl90Y6jOhWoFhluHg-OTJ6-Uaj_VQ2ShHVoUy9rjImQdqGmFHL8KdiLIxjzZ1CxNp6NUj0oD-eByppeih9MIYmzkY6Bx8aS8pqfp11dwLE5X9NKXjqUppe_HZjJLKJvgpHgxJl3zvGGITce5vQDLTHK73mIx6sJ2b6BHyrj9BUFW9JK459SkYisEPej_v8QPeeaTN3wObH3BVxay6jqxUTTRi79Xhra4mpRqMVlLD4-zYMe6A2LIeLvbl2hLDNBs3pwaaMYo-bbRtUcUj9X_p3-47wJyeT9pdqrVc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: سنقوم بمعالجة الدين البالغ 40 تريليون دولار من خلال النمو الاقتصادي. نحن نحقق نموًا بوتيرة أسرع من أي وقت مضى.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/90141" target="_blank">📅 02:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90140">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b6fa3f0e.mp4?token=jFGBVTin1Q094EzoMtoJFfBzOkioKvaTz0dqFNk975rJcACsZGQcEPoIhadqk3WEyukDSAuVRuXw5k7rklN7ZmVF9Bs9puFsDVUEO1A5ly5mk9XU5DEvCXFt-B2BlyRYU3B6CRLijGa6pw-NnlowZMoFmTKw6k2x3RhrzeNPypZnfNIVUUtw3OOhWyIlX0c7zlGsXb767HKHRC9VjT-DGoSLm39yWwwCgjzQ9eRg8Im3rffqhc6zoD0vg-Zhhmed68LKGSB11Jnzn_TVyD_j9J8sxJZFLZJjix39uhdFGU68SBApNOc58TgI9wsVUVrBGlsmCWbdU6Gc9Al29gOiRzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b6fa3f0e.mp4?token=jFGBVTin1Q094EzoMtoJFfBzOkioKvaTz0dqFNk975rJcACsZGQcEPoIhadqk3WEyukDSAuVRuXw5k7rklN7ZmVF9Bs9puFsDVUEO1A5ly5mk9XU5DEvCXFt-B2BlyRYU3B6CRLijGa6pw-NnlowZMoFmTKw6k2x3RhrzeNPypZnfNIVUUtw3OOhWyIlX0c7zlGsXb767HKHRC9VjT-DGoSLm39yWwwCgjzQ9eRg8Im3rffqhc6zoD0vg-Zhhmed68LKGSB11Jnzn_TVyD_j9J8sxJZFLZJjix39uhdFGU68SBApNOc58TgI9wsVUVrBGlsmCWbdU6Gc9Al29gOiRzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏
ترامب:
سنقوم بمعالجة الدين البالغ 40 تريليون دولار من خلال النمو الاقتصادي. نحن نحقق نموًا بوتيرة أسرع من أي وقت مضى.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/90140" target="_blank">📅 02:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90139">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7S9JXCLEVLGMdPvV9bZ7I2eX2U0m5s4czgr0Wt2yIOTm51ga-bkbvQ_iP_xzsDB97BJgUatcpX0sAd3s4-8Um0LxsJrX_tay95XwHCpgoC3MbFHq30IYJ8YSI9z-XiAbGqfVgY93MqgocvwSlyui_bNlPDTCKolm15eKc9yOBeM_KIwzFYQNYPjCjqbVo18vdum5f_giSW5RcC3nZcz15et81RAXGPCNaZvw-uLGwaV-3u0lSFb1kVvugbe4hR3m3cwoBwrMwSBezS3B4lNlZSetTfiuFhVofqBPazqqsmv7KfiG-E__0Ujc2bqjDTTrjUwFjMFPyqjxZyiVigUag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
تؤكد الجمهورية الإسلامية الإيرانية موقفها المبدئي والثابت بشأن ضرورة احترام استقلال اليمن وسيادته الوطنية ووحدة أراضيه، وإنهاء الحصار غير الشرعي واللاإنساني المفروض على هذا البلد. ولا شك أن الأمن والاستقرار في غرب آسيا ومنطقة البحر الأحمر لن يتحققا دون احترام حقوق وكرامة الشعب اليمني العظيم.
لا يمكن فصل ما يحدث حالياً في اليمن عن تطورات عقدٍ مضى. فالشعب اليمني العظيم والنبيل، بوصفه ورثة حضارةٍ عريقةٍ ومشرقةٍ لطالما لعبت دوراً حاسماً ومشرّفاً في تاريخ المنطقة والعالم، له الحق في أن يعيش حياةً كريمةً، متحرراً من الضغوط والترهيب والحصار الوحشي، وأن تُحترم سيادته الوطنية وسلامة أراضيه احتراماً كاملاً.
تؤكد الجمهورية الإسلامية الإيرانية، مع تأكيدها على ضرورة الاهتمام بمصالح الأمة الإسلامية - خاصة في ظل الوضع الذي تواجه فيه منطقة غرب آسيا الشر والقمع والتوسع غير المسبوق للكيان الصهيوني بالتواطؤ مع الولايات المتحدة - على أن حل القضايا المتعلقة باليمن غير ممكن من خلال الحصار المستمر والعدوان العسكري.
تؤكد الجمهورية الإسلامية الإيرانية على ضرورة استئناف الحوار فوراً استناداً إلى خارطة الطريق المتفق عليها وتنفيذ بنودها، وهي مستعدة لأي نوع من الجهود في هذا الاتجاه.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/90139" target="_blank">📅 02:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90138">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72affd6b7d.mp4?token=mobpZhlOd7dhoKBnLeSERwyY7UiSk8GKo_sLqMSY0HlSX3t1fL9gbXdwl3zrcw6Z-DCCe5gd8Bp7ld0Ms4O7uyii1leBgxAxVYYda61AsVPlmUS0Y1RyGanBTfQ3KgysgL1bXbtqwBK3BtJS9P2JdUN_ulc3QWbZF4a4RpzkRGVRbP0ikloFLiw-eOUmq4uOTIoVqLbWjA5pwqkSvIEf4tGZTPy-sJXZlO5nHH6d_nTBYUHs7p27LT-MWCq5a6s_pr8PiazoGZ0NNjcYGv4d8LMbVqRqrap89YCCWDeSMD9VdLksSLAgzGsAl1s1rAi_GTdm83f05GBZKiHKs5dYxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72affd6b7d.mp4?token=mobpZhlOd7dhoKBnLeSERwyY7UiSk8GKo_sLqMSY0HlSX3t1fL9gbXdwl3zrcw6Z-DCCe5gd8Bp7ld0Ms4O7uyii1leBgxAxVYYda61AsVPlmUS0Y1RyGanBTfQ3KgysgL1bXbtqwBK3BtJS9P2JdUN_ulc3QWbZF4a4RpzkRGVRbP0ikloFLiw-eOUmq4uOTIoVqLbWjA5pwqkSvIEf4tGZTPy-sJXZlO5nHH6d_nTBYUHs7p27LT-MWCq5a6s_pr8PiazoGZ0NNjcYGv4d8LMbVqRqrap89YCCWDeSMD9VdLksSLAgzGsAl1s1rAi_GTdm83f05GBZKiHKs5dYxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
محاولات هروب مستمرة لمرتزقة السعودية وسط منعهم من دخول محافظتي عدن ولحج من قبل مرتزقة الإمارات.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90138" target="_blank">📅 02:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90135">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa53b820d.mp4?token=aAERqeVMTawcXRdb5lscC9hcJLCApx63aAfhURelHYNj5IrIqjP99jKMSYL7ohcn_vuaG0DHjIw49pkuVs9cD3_1IFs9iMtkHn0q3AaNCUx3Rc26bEUi4KChBxewq1Mqp-jgf5KSudyopHyYtcSx8Utqsl50smGPfM2gfPPIUBuBWXADPJZZTtL02gwkN8LZzcDrCfLyktx5EFfazcQatd01EX7UQf7aQ2UvzwsQWV4znnLB5UDmz0DnGv-YJaq2W_I5X1YTZtpBpPCKckQOVHFiieY2GM5kdBhDO1bsq68EjCENNZRS6HlDeoUtugQOURUKRFstnS-pCiUg1dzOtkUUKMsBD3iQ-pV2LaMdSRAPSWrn9DAnMtqHyshgTzMf4Va7x-FNx_mLSmEdf6edOhM1cvC_hGrd4muPFofLz29sjy52NDYWErDTlgnJp4DcF3Iv6AfCpDUXWDaOsw7sOoQmPYJpf7GwCL1JFNzAhL5YphKfxQspsulBA7gzJ8lIt2tNUDzY4EYJyyBdaJt5jyhn-9fATt1Z_E-Ur4sjX77TAdSnSF6aQQtGTFrZNzW3uM95X4PbzfC32IPsdcvGu9WX6pXOx6nPUtjzu7mAPdw3yW0fR9UxoQRsO1wVyRXI3lC7fbUvA7LnZSUARDLAV40WulynInJmYL96tpzsEPM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa53b820d.mp4?token=aAERqeVMTawcXRdb5lscC9hcJLCApx63aAfhURelHYNj5IrIqjP99jKMSYL7ohcn_vuaG0DHjIw49pkuVs9cD3_1IFs9iMtkHn0q3AaNCUx3Rc26bEUi4KChBxewq1Mqp-jgf5KSudyopHyYtcSx8Utqsl50smGPfM2gfPPIUBuBWXADPJZZTtL02gwkN8LZzcDrCfLyktx5EFfazcQatd01EX7UQf7aQ2UvzwsQWV4znnLB5UDmz0DnGv-YJaq2W_I5X1YTZtpBpPCKckQOVHFiieY2GM5kdBhDO1bsq68EjCENNZRS6HlDeoUtugQOURUKRFstnS-pCiUg1dzOtkUUKMsBD3iQ-pV2LaMdSRAPSWrn9DAnMtqHyshgTzMf4Va7x-FNx_mLSmEdf6edOhM1cvC_hGrd4muPFofLz29sjy52NDYWErDTlgnJp4DcF3Iv6AfCpDUXWDaOsw7sOoQmPYJpf7GwCL1JFNzAhL5YphKfxQspsulBA7gzJ8lIt2tNUDzY4EYJyyBdaJt5jyhn-9fATt1Z_E-Ur4sjX77TAdSnSF6aQQtGTFrZNzW3uM95X4PbzfC32IPsdcvGu9WX6pXOx6nPUtjzu7mAPdw3yW0fR9UxoQRsO1wVyRXI3lC7fbUvA7LnZSUARDLAV40WulynInJmYL96tpzsEPM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
مظلوم عبدي يعلن حل تنظيم قوات سوريا الديمقراطية.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/90135" target="_blank">📅 02:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90134">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9198c05ccf.mp4?token=uC1s1iQuynqmhw4fY0UUkIBBxqv9kLvw9i0W2cXG56UWJHpRjiwBatwKpZS156Um4vw59HJSN_LwwQ0AsFX3x6oqLWiOYvDnVRtmVmDeIDfdMdydMX8gO5tL-Wyeyb64AEz4PgpkW-NECYR5bhYIzCyK5pxnruAK1gWuB9Uek0iXEELq_gWdAxM-1WPKzuKlaASF8E--B-naAFBBATOaLjFnwbBPjDPZFGTy724pkxk7PKPL49pj5lU1GFC7nodAWrBs4YwXWuoSeklsu6A-zMymFTKVUQJHf0R7YFNi66yt6MIz2LJPxTjm6T--uC4_SDGHBmJhUVFhZ5MiwXvm6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9198c05ccf.mp4?token=uC1s1iQuynqmhw4fY0UUkIBBxqv9kLvw9i0W2cXG56UWJHpRjiwBatwKpZS156Um4vw59HJSN_LwwQ0AsFX3x6oqLWiOYvDnVRtmVmDeIDfdMdydMX8gO5tL-Wyeyb64AEz4PgpkW-NECYR5bhYIzCyK5pxnruAK1gWuB9Uek0iXEELq_gWdAxM-1WPKzuKlaASF8E--B-naAFBBATOaLjFnwbBPjDPZFGTy724pkxk7PKPL49pj5lU1GFC7nodAWrBs4YwXWuoSeklsu6A-zMymFTKVUQJHf0R7YFNi66yt6MIz2LJPxTjm6T--uC4_SDGHBmJhUVFhZ5MiwXvm6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
محاولات هروب مستمرة لمرتزقة السعودية وسط منعهم من دخول محافظتي عدن ولحج من قبل مرتزقة الإمارات.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/90134" target="_blank">📅 01:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90133">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gteO9ZACQU0XSoMAUTGdcryoz8UW_T3LGBPisVFIUr5j6ViB15VaQg9s48OFtu6aKRWxQx_w_wgvFuUPJruQ0h61eGD481Hc0vmcDwLlogha6LKQzsoRhVF6JA2s_F0aFa8RCbQ_Cnd2Jg4i7O1T8Ehb2NxUX-tuRecsE3y8ObSiLklHN6y5kvDDOWRpWI0HzsfNFRO8x5bvhX0juzhiS4MhsmmqKUA8_VFz7F8dlBtxplVLMeMcRpIcLKXSgzjlCulsiegigc7WOFUcYMK0bKQgotfpXJmfLRdR2ah2bliWwrkzOTpxL6-2XBVE2SKz3qPQ0r_cjaTfmBt5bSp1HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
النفط يلامس 110 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90133" target="_blank">📅 01:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90132">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇾🇪
الجيش اليمني يطلق عدة صواريخ نحو مواقع مرتزقة السعودية.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/90132" target="_blank">📅 01:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90131">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇱
اختفاء جندي من جيش الاحتلال الإسرائيلي على أحد شواطئ مدينة حيفا.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/90131" target="_blank">📅 01:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90130">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇾🇪
🇸🇦
عدة غارات ينفذها طيران العدو سعودي في المخا</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/90130" target="_blank">📅 00:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90129">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5DlEEKpaGm11Xv7vjWS1AyOBPRJ5z9r8qA3SEadh5AxrJJ-3IqnTRlVRIKA7RkrrShvNW4-5D6jkDC_Kg_7YULwT-ivlIZZk4mFQkxvdWOr8HTwVlceHEy89TKGcZHrnn4QT-LLVD8Nu0tHnTSGb5f7OfYEbt7KAkaXSl54PI3YlpHFMWQGAkqt6q_Jtqht-2yQp4AY4rUZnY1UiZBjMSFVj_XJgPscWZHef1SISrn6i84HQE2BK68gZiDpt2zeGC79yY_KNwzVcR6oHJxCTMA5ey7cbB8BYrqelcg90XrFuf-sUBHMTm4E-KYOnEjaZDwvi0YOAC1GS1PIcuZIlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف السفينة الثانية في مضيق هرمز واندلاع حرائق واسعة فيها.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/90129" target="_blank">📅 00:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90128">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnkdgQtqLqOlpt0MSoViwgJNVMSo15iuvf1VwhjRTdEOwoqNVJ8f29mEDimI30UqhOFcwrPzicIwYc7dD270ZE9PU0GohBpTLGmR8SRUY79qagDZS8ZVXh3U3Y0eteINxxTIP2pKhZPd6BH-Wo-pGhkD3RipppT5CEAXyWXLH51EvKRl0bSo1WjgR1UgjioffRuqxCaGz2n8Zuww8-aSIS84MzYlu9t0SNP3ygSICCkRF1yFCVjA2uUqLOsKiS73YIBvIlfX3dK-kN-ix_WtUCa-pgHLD2Iqvvyt84BJl6EsjPeoX11jlMhDtRWYzRkj9c0bDeNCJ6p6Q-C_HpVU-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
تجاوز متوسط ​​سعر الديزل الوطني في الولايات المتحدة 6 دولارات للجالون لأول مرة</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/90128" target="_blank">📅 23:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90127">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الله اكبر استهداف سفينة قرب بحر عمان</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/90127" target="_blank">📅 23:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90126">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الله اكبر
استهداف سفينة قرب بحر عمان</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/90126" target="_blank">📅 23:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90125">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTVgqHptcjorYUkko3YGiN1x5pp18ZfGDFvjX2cGSN_cPHMyUmOGfbR74CWZ32ELJuxHx12ybIHRvoj4vcVNipgzKVaovW8iT37e-DxHAzs-lggaDd0ATgth7zxILwaNkrrAHnNMZkQ0lUgYuUFwmMgQdc4StCL_sjvl2W37dYu7J9GB17PzqS8i_XZSk8ZZbHuSXYPSo_4WMuohqSHZ29MmknZ2agAJbj2ta3DHTqIvETGM37uBLjGz4PuUpXrjZGBJCW8s3kzrRE5ZfVDvVe7yQGMruMbbyFRus1LPn9o10HGrcr4dOTOPnQjVlLgm6teVCMSETZdgRgLQTCaKlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
قليلة التداول و تنشر لاول مرة " الشهيد الحي ابو الاء الولائي " زعيم كتائب سيد الشهداء العراقية من سجون الطاغية والاحتلال ؛ بتاريخ مشرف مقاوم مملوءة بالآباء الكريم والعزة النبيلة بوجه الظلم والذل</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/90125" target="_blank">📅 23:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90124">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇺🇸
🇸🇦
إعلام أمريكي: امريكا ترسل ١٠٠ مستشار عسكري للسعودية على الفور</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/90124" target="_blank">📅 23:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90123">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89269525c5.mp4?token=FgHuXfRQshsjtcxMm9o0T7E71O0-j0pkKzKYpn-VM493QeR93M4AZ_EGc-IhqYXHkhOHETio_G_5Y3t0OonWaqvttXijio-19BDbXfbWtTJI4Uqh_BnJag3ReQf7V8L2wVpQsMXyopolSR0EdHUsPlGykULT3K4lo1eB87gw0O3JYEmz_eHAOhWBL4tr5n8v4Kj6KSb1IcxAKb644RExdn6ZB-RDMrbuyCxfYEdQYgeCqKxkuIhBsJe6B7rlVbrv6rqyDUFEd2X05x0m3Dx7zxdpVHikM-Cbvqaq0L8PwVAqjNqHaD1UHXq9nNIcpiU-op-RjXtS0UzMUOdAbXb9sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89269525c5.mp4?token=FgHuXfRQshsjtcxMm9o0T7E71O0-j0pkKzKYpn-VM493QeR93M4AZ_EGc-IhqYXHkhOHETio_G_5Y3t0OonWaqvttXijio-19BDbXfbWtTJI4Uqh_BnJag3ReQf7V8L2wVpQsMXyopolSR0EdHUsPlGykULT3K4lo1eB87gw0O3JYEmz_eHAOhWBL4tr5n8v4Kj6KSb1IcxAKb644RExdn6ZB-RDMrbuyCxfYEdQYgeCqKxkuIhBsJe6B7rlVbrv6rqyDUFEd2X05x0m3Dx7zxdpVHikM-Cbvqaq0L8PwVAqjNqHaD1UHXq9nNIcpiU-op-RjXtS0UzMUOdAbXb9sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تفعيل الدفاعات الجوية في ارومية بمحافظة اذربيجان الغربية بالجمهورية الاسلامية.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/90123" target="_blank">📅 23:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90122">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇶
🇺🇸
وزارة الخزانة الأمريكية تعلن عن عقوبات جديدة ضد مسؤولون تنفيذيون في شركات عراقية.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/90122" target="_blank">📅 22:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90121">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf39a528ac.mp4?token=dIkT5DWGrCV-3256H_StXvLdXyECTLpa6EXqRR_DdrQtV9wSrFbevYOMn5sIsqLqyMc_faUkK3kLij3FCQWF_2exd0ebrEqkRXEmBB58dLYOUJ1D9oIpNi0uO9w3Da3oyZ69JvYzZs40UFuHzkLHt70uga7wC4cgsu1ZbqlZxXWQ6KWtm9hXuo_th61Xo0LFTW97eJYqfvdqa3yl6zlQRFnSlGO_Wk7oE1cysfj0brav5-VMyfERsc3yKJk8qjCnrqXLMut2EOW2hk1vCzKRjzEY-4PN34VN8oHF81vPnw3lAKS_-NB5ja0KCmqOwUXmW0mYv1rSKtl4E5EkAurfWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf39a528ac.mp4?token=dIkT5DWGrCV-3256H_StXvLdXyECTLpa6EXqRR_DdrQtV9wSrFbevYOMn5sIsqLqyMc_faUkK3kLij3FCQWF_2exd0ebrEqkRXEmBB58dLYOUJ1D9oIpNi0uO9w3Da3oyZ69JvYzZs40UFuHzkLHt70uga7wC4cgsu1ZbqlZxXWQ6KWtm9hXuo_th61Xo0LFTW97eJYqfvdqa3yl6zlQRFnSlGO_Wk7oE1cysfj0brav5-VMyfERsc3yKJk8qjCnrqXLMut2EOW2hk1vCzKRjzEY-4PN34VN8oHF81vPnw3lAKS_-NB5ja0KCmqOwUXmW0mYv1rSKtl4E5EkAurfWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اكثر من ثلاث انفجارات تطال ابها في السعودية</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/90121" target="_blank">📅 22:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90120">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2YR4MCPNRl-yFRM3C780brJr_bR1WBXoreJ7w8p9P0c-JRP6hN4ymFqJ5G3qJRE7Ha2snqPNVdGuUc3SrtbHZoY78C82s5OCHO0yjxxdwuuLKy3QV52PLWqT-5Q1eq_snKpCMcpfxuxicoN1QoUFpC9v2rvawqCuldSP6TNr4dzXSCB89UwDfcr1L4BQv1qstNTSaiQMIQj3MDErTZ0QSwIH_c20GQpYbaW5CiiANxak3g4GMNlVXLTRabbA5FcvidvePprtsErc1q252Taz6GwhQn20o7QBEi9ysY6eTQsJzM77sFrfS7K4jFKx_HrCaHRSgxk2_EgS7hkHK5yaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران اسعاف فوري سعودي ينطلق من الرياض باتجاه أبها لنقل جرحى مرتزقة العدوان</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/90120" target="_blank">📅 22:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90119">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رشقة اخرى نحو أبها</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/90119" target="_blank">📅 22:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90118">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رشقة اخرى نحو أبها</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/90118" target="_blank">📅 22:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90117">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/90117" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90117" target="_blank">📅 22:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90116">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رشقة اخرى نحو أبها</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/90116" target="_blank">📅 22:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90115">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/90115" target="_blank">📅 22:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90114">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رشقة من أنصار الله نحو خميس مشيط</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/90114" target="_blank">📅 22:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90113">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/90113" target="_blank">📅 22:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90111">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">انتحار جندي إسرائيلي</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/90111" target="_blank">📅 22:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90110">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇺🇸
🇸🇦
سي ان ان: الولايات المتحدة توسع أنشطتها الاستخباراتية، مستهدفة دعم الحملة السعودية، ارسلنا أكثر من 100 مستشار عسكري أمريكي في السعودية.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/90110" target="_blank">📅 22:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90109">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇺🇸
🇸🇦
سي ان ان:
الولايات المتحدة توسع أنشطتها الاستخباراتية، مستهدفة دعم الحملة السعودية، ارسلنا أكثر من 100 مستشار عسكري أمريكي في السعودية.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/90109" target="_blank">📅 22:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90108">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccmkeKVIyVVSTx_gCsMek_ONXuyShjXFIHVvNIlbZWTvCRZaZZSQoV6IX8elLG5YrtSjAgeWVSOIDmBmkoohmn9dEgl2Nf8shsFp3UaMqnH0OIcqXZg5WQPplSJLtfAqcZP_EWvctrFdEUEfE5EXgG5u6vi2shn77ZGcjrV8hVsyIiSoezt9MqaPxmjAYtBRTGAa8U20kVPXKnyhNYgaOJ-fuUI1R4yznhi06POXcA85UUZXoY5XY1CeKkIOi-ppNo9xHItrk_meIAybkSmj_1VoKDLZHi-ABr07a17ZLJ4BIZ0ffw4b1KEFLMLt6P2sXKPnwa0iAIZmSi9jXz3i1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسعار النفط تصل الى 107$ للبرميل الواحد</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/90108" target="_blank">📅 22:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90107">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇱
اعلام العدو يزعم ان صوت الانفجارات المسموعة ناتجة عن تفجيرات ضخمة لانفاق وذخائر.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/90107" target="_blank">📅 22:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90106">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">القوات المسلحة اليمنية في ميناء المخا</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90106" target="_blank">📅 22:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90105">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇶
🇺🇸
وزارة الخزانة الأمريكية
تعلن عن عقوبات جديدة ضد مسؤولون تنفيذيون في شركات عراقية.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/90105" target="_blank">📅 22:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90104">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇸
‏
مسؤول أمريكي:
بلغ متوسط ​​كمية النفط الإيراني أو المشتبه بانتمائه لإيران في المياه 110 ملايين برميل خلال الأسبوع الماضي، مقابل 180 مليون برميل قبل الحرب.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/90104" target="_blank">📅 22:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90103">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71c2af1239.mp4?token=On6djgpl9UTKHTrV8fh-9Fh-Gr6nghISTr__rY8HtJvtcf8ogprdHxbnOyaCdfyqM9k7wJETsh0UJjwhO0HVJy1nwmrgZtkGL34_E8E3eyrttNqU13tXsEeX3LE3-sYBpsoLglV6ESQ0xaWHcc8z-FcwPyARPdwXGpENpsF7B7b1URWHm1dz7txwagMNECxqfLyHrsNjAlI9z2Xigzb2Rq_lgt7Ov76NShRjzg2xuvs1HEoh6IXX8MyemvMtWsPJe1hofZnM-dlhTsai9Tf8k1rqD6Blv9i2L57x4ACOuYhT3TGtmW1V5WFgf04HT-S11gRlsnLk8agArNPETOUQkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71c2af1239.mp4?token=On6djgpl9UTKHTrV8fh-9Fh-Gr6nghISTr__rY8HtJvtcf8ogprdHxbnOyaCdfyqM9k7wJETsh0UJjwhO0HVJy1nwmrgZtkGL34_E8E3eyrttNqU13tXsEeX3LE3-sYBpsoLglV6ESQ0xaWHcc8z-FcwPyARPdwXGpENpsF7B7b1URWHm1dz7txwagMNECxqfLyHrsNjAlI9z2Xigzb2Rq_lgt7Ov76NShRjzg2xuvs1HEoh6IXX8MyemvMtWsPJe1hofZnM-dlhTsai9Tf8k1rqD6Blv9i2L57x4ACOuYhT3TGtmW1V5WFgf04HT-S11gRlsnLk8agArNPETOUQkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
انفجارات قوية في جنوب لبنان</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/90103" target="_blank">📅 21:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90102">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e0c86462.mp4?token=pAGzv5OecZJ86lW-8sSqVwuT8C-Fhic4_xGIs9pDQBog8cgFQwF8U8HHZPVKa_UcgqpFSiEy_s3dJwOPqJ6Rb-CG8xlqXGafL4XYTLq9wJWImCbAIchOzDqZW3VoJgTlNwylukMHonQIOhGmxiNUOpwxjRhVjEHSzpruqiAh-7UrjRyiXyXasNJLf3ufKagOdAbaAL5fEOXVHt4tGV5LQ7IxpXCx9V0UosZBg8-8_bEWtZQnhcn-Qe-4ACO053hkMblreaiWbcJrd1hHsChKMtkD-ROx-yJWvQhyK1StBk-GTtnfk0Y3STdB2gUL3Qzv8-7SCKQE6SwkzZnM3mWY2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e0c86462.mp4?token=pAGzv5OecZJ86lW-8sSqVwuT8C-Fhic4_xGIs9pDQBog8cgFQwF8U8HHZPVKa_UcgqpFSiEy_s3dJwOPqJ6Rb-CG8xlqXGafL4XYTLq9wJWImCbAIchOzDqZW3VoJgTlNwylukMHonQIOhGmxiNUOpwxjRhVjEHSzpruqiAh-7UrjRyiXyXasNJLf3ufKagOdAbaAL5fEOXVHt4tGV5LQ7IxpXCx9V0UosZBg8-8_bEWtZQnhcn-Qe-4ACO053hkMblreaiWbcJrd1hHsChKMtkD-ROx-yJWvQhyK1StBk-GTtnfk0Y3STdB2gUL3Qzv8-7SCKQE6SwkzZnM3mWY2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
انفجارات قوية في جنوب لبنان</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90102" target="_blank">📅 21:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90101">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏
🇺🇸
رصد نايا   غادرت اليوم عدة طائرات تابعة لقيادة العمليات الخاصة الأمريكية قاعدة ميلدنهال الجوية الملكية البريطانية، متجهةً على الأرجح نحو القيادة المركزية الأمريكية، مع العلم أنه لم يتم التأكد بعد من كونها وجهتها النهائية. وتشير بعض خطط الرحلات إلى توقفات…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/90101" target="_blank">📅 21:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90100">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">▫️
‏قررت الجزائر إغلاق مجالها الجوي أمام جميع طائرات الإمارات طائرة مدنية وعسكرية مسجلة اعتبارًا من 11 سبتمبر.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90100" target="_blank">📅 21:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90099">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/922f30bb9b.mp4?token=cABpnLSFVmSLeQZmwKT447vNvXQzGUyhAJ79B1_cDAfUfxyN-Z8te3b_kgsEcAJIpMbpeO_pZrVy5rdo0UKwd2dOoeNr4fBw73zs28-E8Cc4rIeeMURoDoDdltA0A6CTGYBHgVqS3GrjNNQfmAOFdWAp5Z3r8aHyPEhG1vaqrwYX-zHQy0X-MfA_XE1o-Vubfy7iCoiA9FZHALr6GLh3YwraX9duHhNqxyNC_zp4ogY_KU7vY3MI0YHtDWtGmOoCZmTKKeNtCgv4ykBOk4Ii4zKYLhs-BXx50BRh941zwMJh5iSls0Q1ksqGrDZekRPRBxDyYQ2bRKAsI-AXq1hQOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/922f30bb9b.mp4?token=cABpnLSFVmSLeQZmwKT447vNvXQzGUyhAJ79B1_cDAfUfxyN-Z8te3b_kgsEcAJIpMbpeO_pZrVy5rdo0UKwd2dOoeNr4fBw73zs28-E8Cc4rIeeMURoDoDdltA0A6CTGYBHgVqS3GrjNNQfmAOFdWAp5Z3r8aHyPEhG1vaqrwYX-zHQy0X-MfA_XE1o-Vubfy7iCoiA9FZHALr6GLh3YwraX9duHhNqxyNC_zp4ogY_KU7vY3MI0YHtDWtGmOoCZmTKKeNtCgv4ykBOk4Ii4zKYLhs-BXx50BRh941zwMJh5iSls0Q1ksqGrDZekRPRBxDyYQ2bRKAsI-AXq1hQOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
‏
نتنياهو
: دمّرنا قدرة إيران الفورية على إنتاج قنابل نووية مرتين وهي تحاول مرة أخرى</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/90099" target="_blank">📅 21:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90098">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇾🇪
مشاهد حطام طائرة الاستطلاع المسلح "كاريال" التابعة للعدو السعودي والتي استقطتها الدفاعات الجوية لحظة قيامها بأعمال عدائية في أجواء محافظة حجة - 10 سبتمبر 2026م</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/90098" target="_blank">📅 21:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90089">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y8PcnSeumYGdV8PyvjGFy9HjREMMaMg9p0wpo0I9-FxC8jK1mfhr8phsUlLDoOyoytzh0Gc596OI7iOs6FAhVgscnkz6gev1BFuVeLSJM1FMDmLk7rIrB54hnLbCnzgMG-x5YU_1vnkS2U-2VkkVe0rWpMYoL0p5NlaeXOCbmmWOVPWy1bJ8dT6A96ta8NRsiux2Kg4dRnevRfuBAixHdhFiwCZvkII9pX6h96UAE7ZSmd56kGrz6G3T-DLFbFd6L49XkekeAo-XCPcchE4u5UmSmtogkrxML-AaPqm8eqPZORJRCX2BA0R8UF9pDAED6vodeLOK3i8k2z_mzbjI8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l6Rb_NUFNYuRvUDrMkA0IMF7wThMS3Cb7uH1OBvIVot9xiNkBCCtOsbFxXZBOJb8m-ukn5ViTl3qdALQXKAkA8nT6fGB14CR98XmARRy88C01X0McduoXQznZzT3CCo4jBNRlfxr-ganIv5MNqNsu1a4thEqPOSarvxVYKC-1PO3RG15LmzRvR7CDi3bIiiWFef1aPuFIGqFrnbBhf4lAiz6t-Xp8nnhlDB2cEiFT4Ru1_3othb1bozeir03KfVZ7ydQ9C6nKykXzfclrUbDIBjCbASxu_61aE8YzrRtmnKDo9vinWTuhmoOxlyMi28W5yEQ2JnrHcCQXkNnx8pkTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C5oELaXHL5uHPfeTpYpjf_yXtwQnI0lbvvJN5kuJmgzIBraFlT1H9j2TCmiZ36grXDDMGqVKfVBUBw0wOgsyL1lTNtArbdEO57x1CNX4kW5_g6evTSv-2FCo3SfUtO6-Ip37J-xt9Wj5GcopXpJteIrpVAt86gKZqUgBsM7MloFxNScTGdiF0aVqlvaTZb3tXSyZgtlhZJrBGc8X6NU4DHiaPGGjRQYHH-vViOeMdo9ScRmzWA3LN8vfDhds4tX-SLArbBcCc4hOm09EyZ3Wqc6G9KDR0tDNG6I8tTVhk_cUV-rDhQkUBPkZA-CEHRUlr6aX5sZsJ43lUZklThFCeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hHLCOYShDi93ClSs4gEZO0vLbIgVy2r1GNmafRRGl3KFn9iRXNYdigLVFqZ3DUC_xPj5e7cMv0BBjLMg7b8R3urDuuAprkC_kMsxpnhuWgLmNGu_KC3P3T8Lx0P6E9PbjM2I7z3NL4kJ3YMjPHtFX8BueDQTjOI4fXdVus8Rcf1y3figbSTEzjJpnfwYoiVyW4hctGFWIPh3KA-9KXmJf0FSS_VdSBf4l8K_sfz48jWE7ME5h5-fZvJZIwvuT-ofbiVL6QHxB7ECh_L4iEKYJ3A0QS5STZdFDbJcD1doXNM4Fp3_9CGaR_5ZSUa8MPm-E1N3Qyp408GVlaT3ARPqyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNjeA1S9sP9MunGAB1XHCjsYmkOhFWI_u82f4mG-8NRFt8yOGELkhQL10MGK9peGI5DRCFGjXgN_HxlMuWTFnjw7CZg-6rAH5zLIw3SLLxDLTqUWslxPDseGYy99RHUcaScPwfrrvaDFUXuSSBI8jUL4yf_7k7Qkhasn6lYsyItlvy0Gtm2y_eySHa8vJPm0wWp0nypamcR7kqagkT9EsdVAXGd_st0P4FdwnrPWtrjd3IssiKX1lD2D44KRhdakOsrIIHVLZH5WRFgueOu2vYhB2PqvL36w8kJDw4KgPY0Na0Vq-TcdV7t-aeCUGHwknRMvIxcknRYeIhVben6Q4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KcTw_3makJaMK5S1oMa7YJNB1P9N1EVOatu4HoKavkUp6aSPayjfLVS4-z0PIDBA3zraX9ww9t-xVstxZZqMD_ne_L_y0GUoNBVoy_YkS9XnQbieuzOKXrgsLerC_82NtYjHykkhPCBjoJy5z5xg4EtOBeCqSjuxlIYUB_UOyT6ED5w8SXuO1Wc5Z14gw-FetpHO2IgRztLD6ZeK0FJqA43UUabewsxlhJAJ83iqK0bysvNEfP4fj7--6UDGeUeV8tYe5JxzUS7PVaINU44PKZl3yMHObWlAYmgAClMyxs7sYfvxxJMAmgB6qqAKYxsspB4nwuMamXzz8c8NAQkPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SAYbZbF3SkCW5daVWt9OtE9zcwKo4vURofUlI9RllPhYFoXBzFhoZKvkPXN5HaAC0R3yv2H4nSGOxj2ofMb8TV9xeKbfw7oiMuNagv515sBoxzAzDEG6ZLKS_64iWvB2IJsXkqIqeILY1L1176tpIkSEgHRSAuQv6UfYnJvpqlvcbTtQuZdpe-7Pjv-LoemsPOxSt3bJ5iLXcx_u1eUovdfnheLF0o7qJEZf_ZqRbqfwS-yRrRk-S2ohYWGGMUVxZXw8gBQzWSTcKo8pso3gmGBATeFx_7FWbpKgdhCF8FAJddyKP95nS1SUZIIqKpfWkOvNufQoDI5ZnSvB33hkkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IkiZ-NLzTw0uhkI5vY-kBF3OsK_kQHHMH4WmFOJqOrO023ZNRoXs62wfDZtkgnqM1EIZkq0-A4wYYP_o5M8yM8FahmxTuqPhV_j5MhFlKT-i6S1ZjvgVlP_C1Fm_IfI4cM0lAxWMq5f7oGR3efaJq8xYW79W72rxN8d-XLFNuC-v7Q2M7bUPOvHcAdtib6hJJyCPNAyhIyn-rTGbH8N8PchLlRpGssnypnigXJw_s_KQps8jw9-Y29EHw0im2Yeydrp73C1jdPL40EnQJhrnmbjO_ATazMzCQuktahP7x_HE2QZzkjCV-8dzqivaq6Y5wZGM_3hNIo0xxwHIkxIZpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UBuZfWsf-yXV2FzsTF6sK1cYEvOWFy3RuR-Uzp_jPwEPgpKcY_i8stYBebc4SU-IDmqL2JRpKDS99Qij0nKuZLiJGyX-QE5de6fuOb-YMUcrxqHgNuCiTo5Pyj4vU957-HAg2Sy7a2Fp1p1ezIzb8md7PvA6EyYQv3qj6Li1-luFgh_fgKUc-0va3NW-c49IlsZMYpoxnApO8GQQeJ6q1oAZVFnqnalNI2ZHcL7cZ-_MqMNfJ998w0OwiJ99pHWBN-UNRaNOkJS_yTimuZxQWk32BsTadp2zsyaZdPAMrR7KYTisIMIgCcbS80X5P3t3q7-WoGse4rP2OSyxeetNLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
صور من مشاهد حطام طائرة الاستطلاع المسلح "كاريال" التابعة للعدو السعودي والتي استقطتها الدفاعات الجوية لحظة قيامها بأعمال عدائية في أجواء محافظة حجة</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/90089" target="_blank">📅 20:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90088">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇺🇸
‏
ترمب
:  لم تتضرر أي طائرة عسكرية أميركية في الضربة الإيرانية على القاعدة الجوية في الأردن.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90088" target="_blank">📅 20:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90087">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5aee63c24.mp4?token=mGR1c96kbM8fA6RJCL7wJZelTk__1KpZ96JOoT68RySs3S4BGnuS_7TJEApl-YUUWDhL5gKy6Vb3qUlJKgsMyjyDmX8--0VnWZCWRC0IarF3fHbrGx6lDoFxRgwT3uePV6yQ8CdGFwAZIFgxK_G2oRPGDCepeo7fBZVZQJeEls3ljG132e5kTWEPrhSC3w0TwOmQeuLrhk-o5hTqLp0HqQ0nxlDnpIZpgXAW8mU8w4Zc_nVm0aKu_HML6ARZ_qgsx7fzHtJPWqqT1mkpz4HOyg1z3S7znS6h2c3wA6ZE1GBwj-dTZewkYBH4yQTlvOrkGvyrnkIASIdCzQLyNE5wxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5aee63c24.mp4?token=mGR1c96kbM8fA6RJCL7wJZelTk__1KpZ96JOoT68RySs3S4BGnuS_7TJEApl-YUUWDhL5gKy6Vb3qUlJKgsMyjyDmX8--0VnWZCWRC0IarF3fHbrGx6lDoFxRgwT3uePV6yQ8CdGFwAZIFgxK_G2oRPGDCepeo7fBZVZQJeEls3ljG132e5kTWEPrhSC3w0TwOmQeuLrhk-o5hTqLp0HqQ0nxlDnpIZpgXAW8mU8w4Zc_nVm0aKu_HML6ARZ_qgsx7fzHtJPWqqT1mkpz4HOyg1z3S7znS6h2c3wA6ZE1GBwj-dTZewkYBH4yQTlvOrkGvyrnkIASIdCzQLyNE5wxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🔻
بيان من القوات البحرية التابعة لحرس الثورة الإسلامية بشأن تدمير زورق مسير تابعة للجيش الإرهابي الأمريكي في مضيق هرمز
أيها الشعب الإيراني العظيم والمستنير؛ لقد أرسل الجيش الإرهابي والمتحرش الأمريكي، خلال الأيام الماضية، زورق مسير غير مأهول إلى مضيق هرمز، خوفًا من الاقتراب والمواجهة مع مقاتلي الإسلام الشجعان.
بمساعدة الله تعالى، تمكنت القوات البحرية التابعة لحرس الثورة الإسلامية من إصابة زورق مسير (غير مأهول) تابع للعدو، يحمل الرقم 5838، من طراز "سيل درون"، في مدخل المضيق الاستراتيجي هرمز، وأفشلت بذلك مهمته العدوانية.
تعلن القوات البحرية التابعة لحرس الثورة الإسلامية بكل حزم: أن مضيق هرمز مغلق وخاضع لسيطرتنا الذكية ومراقبتنا الاستخبارية، وأن أي وجود معادي في هذا المضيق الاستراتيجي سيتم استهدافه.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/90087" target="_blank">📅 20:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90086">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇶
المقاومة الاسلامية كتائب حزب الله:
بسم الله الرحمن الرحيم
​"وَمَا النَّصْرُ إِلاَّ مِنْ عِندِ اللّهِ الْعَزِيزِ الْحَكِيمِ"
نتوجه بأسمى آيات التهاني والتبريكات إلى الشعب اليمني الشقيق، وأبطاله في القوات المسلحة، ورجال أَنصار الله، بمناسبة الانتصار العظيم في طريق استعادة السيادة الوطنية لليمن الأبي، وتطهير أرضه من مرتزقة الكيان السعودي.
إن هذا الإنجاز الميداني في سوح المواجهة يمثل صفعة لمشاريع العدو الصهيوأمريكي وأذنابهم في المنطقة، وخسارة أخرى للنظام السعودي الإجرامي بقيادة محمد بن سلمان التي أنفق عشرات المليارات من الدولارات لإخضاع أهل اليمن الأعزة.
ولم يكن لهذا النصر أن يتحقق لولا الإيمان الراسخ، والتوكل المطلق على الله، والتمسك  بنهج العترة الطاهرة، إلى جانب الصمود الأسطوري والتضحيات الجسام التي قدمها أبناء اليمن الأحرار.
كتائب حزب الله</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/90086" target="_blank">📅 20:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90085">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷
‏
وول ستريت جورنال:
إيران تعاود إنتاج الصواريخ الباليستية.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/90085" target="_blank">📅 20:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90084">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skgfp4i6ApM-JifVmXZN4BD4wswQS-1LDimD6h2m7N_y7AkwRMv91JUyeBwnoNQMfuxkj8Bzy0KMF1iNnbi6JL_m_STU129hJeEVuntDkRTtPe1WKnRzi5O5PZKbMe6Q5k-ly3PuEY6LqgHMlIZjt7mMyr8IdRd7Jq4H63IYqMkPJ2EE76iCZXrclqO6zaY1zkUNLl5HHA5tTXA4HzfhqcoGOvvpXcFa9_CGgqEPMs-2_0Mb-2FHEeubZyvjBVjNCjIriYjxzeN8JSKhXbCobCDDO_8vK6z91NvLi-kK0lt-WktvaEaunixP54Zal_Ci3f-KuiV34EsW3odFvFHpMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف
: إليك جرعتك اليومية من "التوجيهات الاستباقية"، تحسّباً ألا تصلك أخبار من سلطات نظامك: إليك الترسانة التي سيستنزفونها والترتيب الدقيق لاستخدامها. تظاهرْ بأنك لا تدري ما سيحدث تالياً
😉
.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90084" target="_blank">📅 20:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90083">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhWzfSlpxDHKJN6Vsl9ZRtmYQmoge7Su1ZI_SNWkAgBPWsgW2tbfEEe93Rg2GkCfXHXRYBnw6PkwQaPuXRZyhkBJs_ayJWgrilqJ75hXaIU9414nID-HhZ2XExTjof23OSh0o1rEbAGx1Le0oU3ZH0Qlx6rZkBM7wHFhCPtvtlsNEBGVZMMwxKHDd8rXe918GJ_9BS0xAdNRy_P-RVane4fjUohrfeAQ8rGx3G8m0jO7khaKugq7rnwKPC5Qge5QbZzkRK7gO4KllRQtCN2fQhOh1qShBBBHlsBrwz9MJ6t49mq0gBBnuhvVVcL6tt-guZNdLmTgIVE4fok-5-FPOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
بعد ان ذاقو الويلات:
أميركا تضع مكافأة مالية لمن يُبلّغ عن بيع الجمهورية الإسلامية للطائرات المسيّرة.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90083" target="_blank">📅 20:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90082">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏
🇺🇸
رصد نايا
غادرت اليوم عدة طائرات تابعة لقيادة العمليات الخاصة الأمريكية قاعدة ميلدنهال الجوية الملكية البريطانية، متجهةً على الأرجح نحو القيادة المركزية الأمريكية، مع العلم أنه لم يتم التأكد بعد من كونها وجهتها النهائية. وتشير بعض خطط الرحلات إلى توقفات في مرسيليا بفرنسا وبافوس باليونان.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/90082" target="_blank">📅 19:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90081">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇾🇪
🇸🇦
الجيش اليمني:
شن طيران العدو السعودي خلال الـ24 ساعة الماضية 64 غارة جوية توزعت على محافظات تعز والحديدة ومأرب والجوف، من خلال طائرات نوع F15 وتايفون أقلعت من قاعدتي الملك فهد بالطائف والملك خالد بخميس مشيط، فيما تمكنت قواتنا المسلحة بفضل الله من التصدي لتشكيل قتالي قبل قليل في محافظة تعز وإجباره على المغادرة، وذلك باستهدافه بعدد من صواريخ أرض جو محلية الصنع.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90081" target="_blank">📅 19:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90080">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e493e9d419.mp4?token=qe7BqZzXY9vEKu29QUcK4YL32Tvo2KQRYZKA68eS0y9linmZHOzfTmduPw0mVJJrvAgezP6XNZ0pJNC6_ZadvGS4hI4hd_KSHlJWMaZ89uR5jE8ZIZAJRSh4YSyOW0tkjDIMXTlm3d5GFL-1BQzx5wzPEHzEY3G-G-dTPIPLP-a1g6CGc99Zm65HmDCnLAVKHXtaLvNSu3xUv8kz-ZDtpqFAzDdFbMIuIcJVJu68sXd3vmiHpXQKFs2hGjtl1CWSso3898xbQxrIOR2uAncNioHDE5A8RmP3GQVgdx7P6xSRS2peRHJMTpNJ4aFiKbngA2jnTJuYZ6gKPuiaGe3tDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e493e9d419.mp4?token=qe7BqZzXY9vEKu29QUcK4YL32Tvo2KQRYZKA68eS0y9linmZHOzfTmduPw0mVJJrvAgezP6XNZ0pJNC6_ZadvGS4hI4hd_KSHlJWMaZ89uR5jE8ZIZAJRSh4YSyOW0tkjDIMXTlm3d5GFL-1BQzx5wzPEHzEY3G-G-dTPIPLP-a1g6CGc99Zm65HmDCnLAVKHXtaLvNSu3xUv8kz-ZDtpqFAzDdFbMIuIcJVJu68sXd3vmiHpXQKFs2hGjtl1CWSso3898xbQxrIOR2uAncNioHDE5A8RmP3GQVgdx7P6xSRS2peRHJMTpNJ4aFiKbngA2jnTJuYZ6gKPuiaGe3tDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاقمار الصناعية تظهر اضرار كبيرة في خزانات التخزين في مصفاة جازان السعودية بعد الهجوم الصاروخي الذي شنه انصار الله</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90080" target="_blank">📅 19:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90079">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrB51pXmLfHVQ7KCQMCizh4pNHosGvoLG9OgEdzDzdSV02DH_Rcm5ISQmjjlUOm9zeYCGYwhJxh4XPJ-lW9wBYkKasMowUC9Aa5ZsI0ktSVQYC5VohGgoyHXfAqBq5qKvPYLeb0nBD_f1furzNmz-nCdk1NWod25JCLa1grJNtwmGU6XSQmqS9tZ6CuuODowKIF9-dtgMrkdTarlJQF5tjuSlpVxSrYJYrJkuHnzR8lV1iHLjrWX3hcqENJ2vi3vtjgMtfXOH3YFd8AHQN1sMwzuoVWFSfb5KCz4tON6KhUWa7m11IBHkE7R9KThixGpznDBI71_vBFxCkqimPPRXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسعار النفط تصل الى 107$ للبرميل الواحد</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/90079" target="_blank">📅 19:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90078">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fffef3ae.mp4?token=eujhnqjcsCPFhxj4P7B_ApQ66jOXuRy6a9qMUcsOCcrYn-g8mnQEznpheLC9L_BPSihKHRs464rlXW-d5gahUOqiNirOu2ldxTthC1PhJnK_yOAQvrhtWrmYE5alPbe3rkOP6Tly3fvpdZTflKz0npqb4oMwlIAHoCsBrpRu7LZyrTTYdowBehl-J2NW66-eeMdUT6T6J-b0SRDDRBrhnh2abwtPvRY7N3JEc63XRKglGx67u6Wb9Y0l5hEp_w4H9waRPweL4nHXAd-zzhjjmusg0XDAeKSi3p9RJwXM0egHwAxNLdUiQ0WZWZRnnPX6V6WSFUCIZpUvc4hjFLz-Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fffef3ae.mp4?token=eujhnqjcsCPFhxj4P7B_ApQ66jOXuRy6a9qMUcsOCcrYn-g8mnQEznpheLC9L_BPSihKHRs464rlXW-d5gahUOqiNirOu2ldxTthC1PhJnK_yOAQvrhtWrmYE5alPbe3rkOP6Tly3fvpdZTflKz0npqb4oMwlIAHoCsBrpRu7LZyrTTYdowBehl-J2NW66-eeMdUT6T6J-b0SRDDRBrhnh2abwtPvRY7N3JEc63XRKglGx67u6Wb9Y0l5hEp_w4H9waRPweL4nHXAd-zzhjjmusg0XDAeKSi3p9RJwXM0egHwAxNLdUiQ0WZWZRnnPX6V6WSFUCIZpUvc4hjFLz-Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#ترفيهي
مرتزقة السعودية يقومون ببيع اسلحتهم في عدن بعد فرارهم من جبهات الساحل الغربي.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/90078" target="_blank">📅 19:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90077">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">القوات المسلحة اليمنية في ميناء المخا</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/90077" target="_blank">📅 19:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90074">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gVMO2qxL9e8xdfGw6aYqZ1GQIdfsZPIFzUB2d6eTqcS3Cdb5s3EoCEvqI4PY7qy4GBtJT1fem3v5EMrFyHfegwgSNjtR7yIThG_oDqlvBIRzZ651sYSz2ImHNIJnq8Z9jmQjkTEw9Bu3oqMaXgJTfrif9VIF3ULXEia_ehfWFp6UVDWBKyaZzwzEWvRm0F1NuV5Z3nr1ZrwCdwlF6erS6L7oDLS3cTIA0vX6XmrGUP071_Ci65EYwMrt3ALRbr6MoWnpO7s6_9O2qwbpXM-3o1qoR8o3PqoHvH4URYCt1QOY9wzwAfvJj755zZvOuExNo4WjLs1rhF5JUkqN11N7Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YqAWYzMx73doZcUcbfPXrp10potCiL-U3y98j_L_n_-nkCALK3VSaB_SG2hEKWLVvyIPBsxLKPznv4x-BEm0q3efCVn53GdeVBvZhMWo9r7ZIH8pb2gNqa7GFENRFuLT6QEdoW6cY9ZiVQhZ6FLx5jdxCTZ6HTie2qJd6tPnO79x0Y9kNuQB9NCyL6DM0K4qePsDT5wyfKO-BUna1DJox-ustyjhd6LzuXerRDv9CorS5g35hobh44MXvTvbe6h2PG8P4_mMINNcxy54XKMbrzzqEen_Zz91_M3iDn8g7iRrLQEKGmTG1Klbky5fF_-acR9_AGRvJhN4m0cryxJ_jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vcFzYZm8NLOSQV4lzzpKaah0Jrdus5YeqUMdWTrnyT86K5w07OXucByZSYPxlKVaNyGicJqCYIrHGvizkhdjNcO3zn6Cv7NfHN2YvWw57OcEyE90iBK7FrHHc6XJbkhVdqochC8doeGBtIu5jw3mbqIotqo06SD4cMfI1_fMEh_Hy0qimMGIy23zMYkPFn-YDaKjzPzN7gV9FM6L1sEJmgmghX2a8xet-YAB5eiLuDIByhxJILOPkz9gWNipD1bAwBkdzT_Q8dYQSI3zGwPvw9nwI_E_nXrqIXb3nn6Py7ElO0ByNvGixSAoxuQ5jfwzHC07sFNscjDQxMhPj9plFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
🇾🇪
‏محافظ الحديدة يتفقد الأوضاع في حيس والخوخة بعد السيطرة عليها من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/90074" target="_blank">📅 19:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90073">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ميليشيا البيشمركة تعلن توحيد قواتها في محاولة لعدم خسارة الدعم الامريكي.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90073" target="_blank">📅 19:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90072">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed9003eba0.mp4?token=e4R-XlfTx7wzCAe840gaC63AEedoUTlbQ99okv5wKTKof0BN-L6644-culcdj1FfsMFbPHQtK93W_SJorh74o79IhvAMM9CNgdl794Lm5Mk9xwPuZjcLGbFQygcurTauIGGKZm2pVg_oLJZVHx22P9qALnNIyZ9_Bp2qMkD1WTqSH2DDf7Ex-EMBrINzyiHvCEJo__rqzM7ARK9zezskSm-OktLv4GRjG1bAF11slbLfGrLTvVOIVEpdnbspNX-VMk96U1N_ZMFvP9hY0IeyT9LEkF3biIVqxnp-xdW-Cu8KJVFsaNqCIlAF7LdScKaU23YwUdDVLEVB5akXpc2FmS3Typ6K6yrEHy_98q2SIpCQYH1oPvW02PbWylXBkfpsd2tvCF21Zj7pArAh954Zc2I6KdPpfKHaKKNrlTuETWQXhjZbgBOcleJSQxSiBHWy5QB5F_gxIZoTm7iOA_mygSI1tlo-xvV0luf1kostIWVXAcvBAYpgXbvEQ4_lX1tO-jRQOFT6bE8Mog3ITmfN0OOfOqOJsXlCVJJp-iAOx9C1hOzz6Z12iHhSEp9FYNLiR8WThDNkNaZne-c29hWPrWARlHmhB8QGynYZNw_mcP5p8porJ84dUJhcf4szukyCGbUo2jAwJVWeuXlY-CNV8g7yPpM288IGSgP1cQEqnfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed9003eba0.mp4?token=e4R-XlfTx7wzCAe840gaC63AEedoUTlbQ99okv5wKTKof0BN-L6644-culcdj1FfsMFbPHQtK93W_SJorh74o79IhvAMM9CNgdl794Lm5Mk9xwPuZjcLGbFQygcurTauIGGKZm2pVg_oLJZVHx22P9qALnNIyZ9_Bp2qMkD1WTqSH2DDf7Ex-EMBrINzyiHvCEJo__rqzM7ARK9zezskSm-OktLv4GRjG1bAF11slbLfGrLTvVOIVEpdnbspNX-VMk96U1N_ZMFvP9hY0IeyT9LEkF3biIVqxnp-xdW-Cu8KJVFsaNqCIlAF7LdScKaU23YwUdDVLEVB5akXpc2FmS3Typ6K6yrEHy_98q2SIpCQYH1oPvW02PbWylXBkfpsd2tvCF21Zj7pArAh954Zc2I6KdPpfKHaKKNrlTuETWQXhjZbgBOcleJSQxSiBHWy5QB5F_gxIZoTm7iOA_mygSI1tlo-xvV0luf1kostIWVXAcvBAYpgXbvEQ4_lX1tO-jRQOFT6bE8Mog3ITmfN0OOfOqOJsXlCVJJp-iAOx9C1hOzz6Z12iHhSEp9FYNLiR8WThDNkNaZne-c29hWPrWARlHmhB8QGynYZNw_mcP5p8porJ84dUJhcf4szukyCGbUo2jAwJVWeuXlY-CNV8g7yPpM288IGSgP1cQEqnfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية من داخل مدرج مطار المخا الدولي.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90072" target="_blank">📅 18:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90071">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">العدو السعودي يشن نحو 10 غارات على مديرية ذو باب.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/90071" target="_blank">📅 18:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90070">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">العدو السعودي يشن نحو 10 غارات على مديرية ذو باب.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/90070" target="_blank">📅 18:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90069">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">انفجارات تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/90069" target="_blank">📅 18:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90068">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇾🇪
🇾🇪
‏مركز تنسيق العمليات الإنسانية في اليمن يُبلغ جميع شركات الشحن العالمية بأن الملاحة في البحر الأحمر آمنة لجميع الشركات، باستثناء الحظر السابق على السفن السعودية.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90068" target="_blank">📅 18:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90067">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇾🇪
🇾🇪
‏
الاستاذ محمد عبدالسلام - الناطق الرسمي لانصار الله:
‏إن ما قامت به القوات المسلحة اليمنية في بعض المناطق الساحلية عملية وطنية في إطار فرض السيادة اليمنية، والتعامل مع التحديات والأطماع التي تهدد السلم الأهلي.
‏إن السلام الحقيقي والعادل والمشرف كان وسيبقى خيارنا الاستراتيجي، وأن على الجميع أن يدرك بأن خيار السلام مع اليمن هو الأقل كلفة والأقصر طريقا نحو إعادة تنظيم العلاقات وفق مبادئ حسن الجوار والاحترام المتبادل والمصالح المشتركة.
‏إننا نؤكد أن الجمهورية اليمنية ليست لديها أي مطامع في أي دولة من دول الجوار أو الدول العربية والإسلامية وغيرها من دول العالم، ولم تعتدي على أي دولة بل هي من تم الاعتداء عليها بما يتنافى مع الأخوة الإسلامية والعربية.
‏أما بشأن حرية الملاحة وحركة التجارة الدولية في البحر الأحمر وباب المندب فهي آمنة ومنتظمة، ولا داعي لأي قلق دولي حيالها، فليس عليها أي خطر من جهة اليمن، والعمليات الجارية حالياً هي محددة الأهداف وفق ما تم الإعلان عنه سابقا وتأتي في الإطار الدفاعي، ومتى ما توقف العدوان على اليمن وتم رفع الحصار عنه، فسوف تتوقف العمليات الحالية .</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/90067" target="_blank">📅 17:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90066">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f39dbddee2.mp4?token=KfgwbqNIyZnOWqujcSmPzFdt05YnFB6Zii1JFRW3TnDlVnjx1LgDZ1jYvmejLYM3ENQ3cAxgAW1M5bJDYtc8EATE348DdJZx8jV-p7bgxl1wRi-q8boswAdLHOTWGw1whEM_FWRDhm9bq6_hXyK38kvp_Mq8-Rz7M8UytBhoXYVp_Cg5TyAX6TsLEwRSwJJHd6IR2b1xfcX18tSKAJ1cB2-xdolImf3bOxkuMLawPrduWjSMwWkCv05WjgrU-QY9zP6IhW2l1qJPNajVitRyFdQC7RjyNvjMdvdcMQqh-EP0oN-JGehWqWYZG_Jx9UhvB6cB_OoYoeIPFaboeFVlzBmT7XEJi5V04rbtSp7izbAwhkfGfN7zCoJ4ojvaE8xHwAZ3WYHlKSW6AoRNKMdpp7mV6JvKdoPf7eZ1pCKjb72hUIXM4p6Dmh-PDSLRA1bYS_34pEEqkN53ehJ5ZxihGhJ3FFzVkBejt9cXYtvtjJKmHoCITqyowCa0WQJG_D7uJ-cErI5bOqOP0Tlyt4sfZaDhQXIj664VKsryuct4rOCRgCJusj8JxpyAW08v8pXS7agMXP7jfT5TvMSd-gBxs0JtC34Slf3cI4xUUlONnsp_nZvnX6OKFvizlWXWAOU1trHZB4VeuRMXzoYXVzb-a1V43x56BZ30nb3wBsCdF1c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f39dbddee2.mp4?token=KfgwbqNIyZnOWqujcSmPzFdt05YnFB6Zii1JFRW3TnDlVnjx1LgDZ1jYvmejLYM3ENQ3cAxgAW1M5bJDYtc8EATE348DdJZx8jV-p7bgxl1wRi-q8boswAdLHOTWGw1whEM_FWRDhm9bq6_hXyK38kvp_Mq8-Rz7M8UytBhoXYVp_Cg5TyAX6TsLEwRSwJJHd6IR2b1xfcX18tSKAJ1cB2-xdolImf3bOxkuMLawPrduWjSMwWkCv05WjgrU-QY9zP6IhW2l1qJPNajVitRyFdQC7RjyNvjMdvdcMQqh-EP0oN-JGehWqWYZG_Jx9UhvB6cB_OoYoeIPFaboeFVlzBmT7XEJi5V04rbtSp7izbAwhkfGfN7zCoJ4ojvaE8xHwAZ3WYHlKSW6AoRNKMdpp7mV6JvKdoPf7eZ1pCKjb72hUIXM4p6Dmh-PDSLRA1bYS_34pEEqkN53ehJ5ZxihGhJ3FFzVkBejt9cXYtvtjJKmHoCITqyowCa0WQJG_D7uJ-cErI5bOqOP0Tlyt4sfZaDhQXIj664VKsryuct4rOCRgCJusj8JxpyAW08v8pXS7agMXP7jfT5TvMSd-gBxs0JtC34Slf3cI4xUUlONnsp_nZvnX6OKFvizlWXWAOU1trHZB4VeuRMXzoYXVzb-a1V43x56BZ30nb3wBsCdF1c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتال مرتزقة السعودية الهاربين تتكدس امام عدن وسط رفض مرتزقة الامارات من ادخالهم</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/90066" target="_blank">📅 17:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90065">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a357cb919.mp4?token=A95aNhK_Q_EvHz0npVefaQbtg03l8AxdBAM0AbQdac6zu1ieuGbuhoIs7796IPeBiM6LlRnekvNIELDkd0J9qhELh-tav1eDiZdHw84oyqX5l5uAhj4Rs2qUJFeGZlXun4DxoJArLbgiBJtSwvl9mZik13r1JifcBMVytkJQ85EzRGaNj8ym4fhWs92u8XIXJtDGhl65rNFTVxlfIFdMTHlBh5sGSXvdHwad5t85DdId2NjgZIkIakMHWcXnAVoUHKpBPtvm_hMZ2jFmOIv_xCrzN2gIFmmlkTKn5EG-FgB2S-h_iNpuKlpQMN1XltXQdbU1dnRAYwJT1xz63ZtVs3RpyuD6ro3Jxb_Mm0-1YvrMc1DNsiDEOd-k95rdAj9UJmmUIDpFV9uBoVURqY__CMgQBKaUyZC3u9rdUeefAnNCl2bpSOvUkToXG3kM670a7_-Woz4JKVXS4Voh-X9jolWdHzRjc2_tM9tXBtY6SaWhnabScDM5FRp0nMuMXD7fnMlcaTk2gTwz45rl6s9M3g0EtjK0p-lNWXi8aRoW9Sap3te0ty-SIOhqqavcDqiSCacv3SxXHdD_Ow8nyWBUjLJ6ENc8_jlDZ59gK-ZmcUvoURQIbI4U49LOzm3ACVHEX48Nb-VcehNZrgJLy76EBtZDUbdZj5IMzwlBCLmVXD0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a357cb919.mp4?token=A95aNhK_Q_EvHz0npVefaQbtg03l8AxdBAM0AbQdac6zu1ieuGbuhoIs7796IPeBiM6LlRnekvNIELDkd0J9qhELh-tav1eDiZdHw84oyqX5l5uAhj4Rs2qUJFeGZlXun4DxoJArLbgiBJtSwvl9mZik13r1JifcBMVytkJQ85EzRGaNj8ym4fhWs92u8XIXJtDGhl65rNFTVxlfIFdMTHlBh5sGSXvdHwad5t85DdId2NjgZIkIakMHWcXnAVoUHKpBPtvm_hMZ2jFmOIv_xCrzN2gIFmmlkTKn5EG-FgB2S-h_iNpuKlpQMN1XltXQdbU1dnRAYwJT1xz63ZtVs3RpyuD6ro3Jxb_Mm0-1YvrMc1DNsiDEOd-k95rdAj9UJmmUIDpFV9uBoVURqY__CMgQBKaUyZC3u9rdUeefAnNCl2bpSOvUkToXG3kM670a7_-Woz4JKVXS4Voh-X9jolWdHzRjc2_tM9tXBtY6SaWhnabScDM5FRp0nMuMXD7fnMlcaTk2gTwz45rl6s9M3g0EtjK0p-lNWXi8aRoW9Sap3te0ty-SIOhqqavcDqiSCacv3SxXHdD_Ow8nyWBUjLJ6ENc8_jlDZ59gK-ZmcUvoURQIbI4U49LOzm3ACVHEX48Nb-VcehNZrgJLy76EBtZDUbdZj5IMzwlBCLmVXD0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تغتنم كميات كبيرة من الاسلحة كانت بحوزة مرتزقة السعودية في حيس</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/90065" target="_blank">📅 17:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90064">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">القوات المسلحة اليمنية تغتنم كميات كبيرة من الاسلحة كانت بحوزة مرتزقة السعودية في حيس</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/90064" target="_blank">📅 17:30 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

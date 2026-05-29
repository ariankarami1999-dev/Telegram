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
<img src="https://cdn4.telesco.pe/file/eXeeqTiPK8IBdrWK16jb5Y2xtAYsgPudittf2XxBqOX6b9BjRhDmvtojjSBXBwPs_YWgWV9ZXs5OddtetVwPJSEqwpUUFgHv4tvb5Xq92WaxX_sv0OzsotJnMMa4zYNp4kIhCH4ii4PtZ8LVw3o4gziF7NwjLt-8WAcDdSgtYqNJ32YT309CI1vvUpxgu17S5xdGdLnWrLP-r7EzOhQq8kWlK6aYWK5pbgwHQ3ncaN72OWvqlg8iD2O-wsDRH43pvX6zZgbLHcNyFOb1db3_PyuuZbJ9p06-hqyf1rOByVThc7tEl85eqM1gEq-OxmiHiuJca_i_epw9frRGEhWA9Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 251K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 05:59:39</div>
<hr>

<div class="tg-post" id="msg-76342">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">في خبر غير مهم
🌟
وزارة الخارجية العراقية تدين قصف قواعد الاحتلال الاميركي في الكويت التي انطلقت منها الصواريخ لضرب ايران.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/76342" target="_blank">📅 02:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76341">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🌟
فانس
: نقترب من نقطة تسمح لنا بالجلوس وحسم القضايا العالقة مع إيران لكن الأمر يتطلب إحراز تقدم إضافي.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/76341" target="_blank">📅 01:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76340">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f662ae4b77.mp4?token=Rp4pl5q-QifUhLwrGktmwSXDlE3sd3FjSyEnnwAFezlXzbXKTuIqhdViy2fJvNrZK0_11VI3OboFjbM_vgdD8cNVq1ENf88vZKa9g45h4zgQpicKmzRvFhjYGOn0kRYPBqu_W_t-TgqbqmcG00smyxs-g7cMGCovc19B-FDZDrKaEnKhQhUEWZzNumcn2qNPJRocoUrmYUaRjNLSvY7TpufymAMtLyckKdnFuo55AoRYv07TKRu-iub04bp-zUj_7dbtlLPHxrmisz_DMIDobGMQN1eLmKzLQFRtMlt17DUYJx9kHa4JOmxBaCqZ3ooNdf0Q3JDSTQLAY9oQNrSSpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f662ae4b77.mp4?token=Rp4pl5q-QifUhLwrGktmwSXDlE3sd3FjSyEnnwAFezlXzbXKTuIqhdViy2fJvNrZK0_11VI3OboFjbM_vgdD8cNVq1ENf88vZKa9g45h4zgQpicKmzRvFhjYGOn0kRYPBqu_W_t-TgqbqmcG00smyxs-g7cMGCovc19B-FDZDrKaEnKhQhUEWZzNumcn2qNPJRocoUrmYUaRjNLSvY7TpufymAMtLyckKdnFuo55AoRYv07TKRu-iub04bp-zUj_7dbtlLPHxrmisz_DMIDobGMQN1eLmKzLQFRtMlt17DUYJx9kHa4JOmxBaCqZ3ooNdf0Q3JDSTQLAY9oQNrSSpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
البيت الأبيض ينشر فيديو مع عبارة "هل أنت تستمع؟".</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76340" target="_blank">📅 01:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76339">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🌟
وزارة العدل الأمريكية:
توجيه 8 تهم للعراقي محمد باقر السعدي بسبب أنشطته مع كتائب حزب_الله والحرس الثوري، السعدي ضالع في 20 هجوما ومخططا ضد مصالح أمريكية وإسرائيلية بعضها على الأراضي الأمريكية.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76339" target="_blank">📅 00:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76338">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انفجار داخل مسبح يهز مدينة الزعفرانية جنوب العاصمة بغداد</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/76338" target="_blank">📅 00:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76337">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARNOklx14RfnVu_4Em2tbnUmYgEKVIHqDtfbkOpPEkmXftMWQuE7dac61ydcD6VMx6QfUjQrzNKDC6E_BPemei7MNXctYZxxQKZlKbBLaqeOmRbm0w6aO3pPp8OvuGO2R9LCjwUHdei18TD7nNIAjX651KINlbqjpLiusANzNyg09cVH7dRB_gTaj9y0qaAJo_XjMpRLE1IILP0Ikh19OiCNaKDxMJNiHFdhxCH8GkYJaCR59hDpf9Z4b6k-HfX6-uQZf1782adi5s7Hmhozs5il6BDLXaq8OFHqFPWTeQ_Ui5rMCqFxarICFwFhJTasNVuKpQq0qZYjPmtyqjipAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار داخل مسبح يهز مدينة الزعفرانية جنوب العاصمة بغداد</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/76337" target="_blank">📅 00:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76336">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">انفجار داخل مسبح يهز مدينة الزعفرانية جنوب العاصمة بغداد</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76336" target="_blank">📅 00:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76335">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKikjtojkkMl9Rf0mmlYXrUIOLFt5iJNIkXATcVF8ivw-yAJGTSOAXrY0aCfeAPmsSfJQMsx2JXRU-HjFwx4v30nXRamuWab3k4iOky87Qipx4AXLXOex_1z2Gao8IYdjyP8lI54cYyG2iOtkoZSYg23T8-WEdLuHquI-YquKfJR_Bh4IXjBE3YmAYPN3B_irZF17tEsmiNIjZnUlHDVADnycbxcEybG7Jef-AcNDEe5l9IZ2dzaIPkOMjMVwDyUii2Lb5YGjg7ptbyqRMbtSq2VHCwmxEMYYnqHH2CjLlzdVrYewDTL0jJ6WYelkFV5pU7oUi_lOaZNFnZV5KM1Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇬🇧
رصد نايا
تمارس القوات الجوية البريطانية نشاط لوجستي في سماء العراق حيث تم رصد طائرة شحن عملاقة " A400 “ بالتزامن مع وجود طائرة إرضاع جوي اخرى تؤمن الوقود للطيران الحربي ؛ يذكر ان السفير البريطاني في بغداد قد صرح لقناة عراقية ان العراق يتمتع بالسيادة ولا يوجد هناك احتلال</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/76335" target="_blank">📅 00:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76334">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇷
‏وكالة مهر: الدفاعات الجوية حاولت التصدي لطائرات معادية في بوشهر.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76334" target="_blank">📅 00:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76333">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇷
وكالة مهر: القوات المسلحة الإيرانية أطلقت نيراناً تحذيرية باتجاه 4 سفن مخالفة قرب مضيق هرمز.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76333" target="_blank">📅 00:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76332">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">صواريخ كروز من طراز ابو مهدي المهندس باتجاه سفن أمريكية في هرمز</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76332" target="_blank">📅 23:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76331">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🌟
🇷🇺
‏الخزانة الأميركية تصدر ترخيصا يسمح ببعض الصفقات مع شركة "لوك أويل" النفطية الروسية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/76331" target="_blank">📅 23:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76330">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🌟
🇷🇺
‏الخزانة الأميركية تصدر ترخيصا يسمح ببعض الصفقات مع شركة "لوك أويل" النفطية الروسية.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/76330" target="_blank">📅 23:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76329">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">أنباء عن انفجارات في هرمز</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/76329" target="_blank">📅 23:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76328">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639d01573a.mp4?token=PaDvLingfH_xCi5wMs3bXINK5tdv_0DXkylyJD2_rKctjzkm1wO6TJZ7Nt1MzjfkSEt_DYjeC7z0K3jQIiCpU8vATNCJMQt7F-6cJSiZbCh0wmWNbYew7o51GjgTLd_Yx5J-r1E4EVuiOsMUFLtdesV9PAvaQiKEkrjYItPXAVnmHthHCf1BkBNVQ_MLop8xxoKbHUbiBw9C1XUIskmV-gbNU8nUpDG0SzuUh16jpI1kXdvu8T_Qwji0d7sdfhSLDZQ1X2STOIRrT1ho95uqUyadD5AiCY2IdxRqZPhfros61RZVKsHWEvnHYB6l9f8FHRLVkKenWSpUFs2DVUWAu73cFiGzE5t9QelamQ2CzbMYjOFz12t404wjRiYhP7FNw_riEvoax64UxjpTKEPH0rzMtXyryLIJ90ryXGNg5V69rEXSPjnfeUInLld7uwkNm48iW5AKDO15t9jUiAnzR3uQ0MU76-RuyJ5fj0DNpUYN99c0j1JUGXa7lX6Bd7VFxiAhK9NLHnvBbOWYdEvLGJ9HG5MzvmQ1Ivpfum2DU5acQJZCOPcPBJE4d5z5YdxHKAc51anerfMXUMM8xN_m1yW7BgysmcfT1cMHVKXxpP5bW8MMMxWbNJFgiEiDWQFwoyBA1B8nYaW42_US2mJI4jFvomrcjCz6HzQLd9zFT-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639d01573a.mp4?token=PaDvLingfH_xCi5wMs3bXINK5tdv_0DXkylyJD2_rKctjzkm1wO6TJZ7Nt1MzjfkSEt_DYjeC7z0K3jQIiCpU8vATNCJMQt7F-6cJSiZbCh0wmWNbYew7o51GjgTLd_Yx5J-r1E4EVuiOsMUFLtdesV9PAvaQiKEkrjYItPXAVnmHthHCf1BkBNVQ_MLop8xxoKbHUbiBw9C1XUIskmV-gbNU8nUpDG0SzuUh16jpI1kXdvu8T_Qwji0d7sdfhSLDZQ1X2STOIRrT1ho95uqUyadD5AiCY2IdxRqZPhfros61RZVKsHWEvnHYB6l9f8FHRLVkKenWSpUFs2DVUWAu73cFiGzE5t9QelamQ2CzbMYjOFz12t404wjRiYhP7FNw_riEvoax64UxjpTKEPH0rzMtXyryLIJ90ryXGNg5V69rEXSPjnfeUInLld7uwkNm48iW5AKDO15t9jUiAnzR3uQ0MU76-RuyJ5fj0DNpUYN99c0j1JUGXa7lX6Bd7VFxiAhK9NLHnvBbOWYdEvLGJ9HG5MzvmQ1Ivpfum2DU5acQJZCOPcPBJE4d5z5YdxHKAc51anerfMXUMM8xN_m1yW7BgysmcfT1cMHVKXxpP5bW8MMMxWbNJFgiEiDWQFwoyBA1B8nYaW42_US2mJI4jFvomrcjCz6HzQLd9zFT-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية تصدي المقاومة الإسلامية بتاريخ 26-05-2026 أجهزة اتصالات تابعة لجيش العدو الإسرائيلي في موقع العاصي على الحدود اللبنانيّة الجنوبيّة بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/76328" target="_blank">📅 23:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76327">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">أنباء عن انفجارات في هرمز</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/76327" target="_blank">📅 23:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76326">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محرم 1 00_٠٦٤٢٥١</div>
  <div class="tg-doc-extra"><unknown></div>
</div>
<a href="https://t.me/naya_foriraq/76326" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">شبه لهم يا حسين
#شاركها</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76326" target="_blank">📅 22:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76325">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وَاللهِ لاَ أُعْطِيكُمْ بِيَدِي إِعْطَاءَ الذَّلِيلِ، وَلاَ أُقِرُّ إِقْرَارَ الْعَبِيدِ
وإنّ الدّعيّ بن الدّعيّ قد ركز بين اثنتَين؛ بين السّلة (والذّلّة، وهيهات منّا الذّلّة؛ يأبى الله لنا ذلك ورسوله والمؤمنون، وحجورٌ طابت وطهرت، وأُنوفٌ حميّة، ونفوسٌ أبيّة، من أن نؤثر طاعة اللئام على مصارع الكرام ..</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76325" target="_blank">📅 22:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76324">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو مهدي الجعفري</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9IhF_6AwK5Zwesgo4FhVFwsKFbL1xhi_33LDhqHfYpfpxJR_Yg-L5IwFAl3BNVcTufGrbaTb88vAC8Tn0v0cE7MCG4-voVYQbQgBEFeNAeky4MmtEIT_In1feA8_JWucDTnq0TQJXW2ENwzzpxU_hjyUekfLNAGc4njECj4e5bfEtHgGZxFHX-2d-BlMX9UcpW1r-DiW-7zlxxZBHDeB1JdcJ7BaokC5PuadluoLG8iouWFSPgG2pyajG491ZCEiI81J6FKmoXWE2w7mq8Vh0swftfAyY7aZ-v9L2wu-VhRCGeEnOk08tR8-Co6DhLb7N7YE-SccGXHflRunPmhmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المتحدث باسم "سرايا أولياء الدم" أبو مهدي الجعفري: لا تسليم للسلاح ولا حديث عن الطمأنينة قبل أن يرفع الظلم وينتهي الاحتلال عن العراق</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76324" target="_blank">📅 22:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76323">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو مهدي الجعفري</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZzVAlX97Td40-ypgTFsJNS_PjasRP69jy7Gm15Mn1Ix_-t052u-W-NUzZqperxu4tG0Y8vzCDD-Nc8Y8Zh-uHhbJHB2zE6_M341FDP9jN7SEtlmGpq9Y5dKVvI_SXH1DcBeKMojKOReNBotttFeFdHqt5mdUwx50-lNvDTKf1duIUoYgMvOvnUJo7oR8KjvErjLreKV7olPiicP6yrDTgTELh2CvUo1s8E5yYZKIT1saN9fdSO3WAyBJtYhjeQDhZntTwaCms02IcgDKn2qL2lktyb2MbHtEcOxq-F4HdIKwfQ_zuJHymWhlBtU3xNotNJkk5CwZM1XdxCo3WX9_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">كلُّ عامٍ والوطنُ بخير، ما دام فيه حُرّاسٌ ودماءُ شهداء ورجالٌ مستعدّون للتضحية.
لا تسليمَ للسلاح، ولا حديثَ عن الطمأنينة، قبل أن يُرفع الظلم وينتهي الاحتلال عن العراق.
في الحرب ينادوننا أبناءَ الأطايب، وفي السِّلم يتناسون أسماءَ الذين حموا الأرض.
فالأوطان لا يحرسها العابرون، وللمقاومة رجالٌ أوفياء يحمون العراق في كل ِّ المحن.
#موقفنا_ثايت
#قرارنا_مقاومة</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/76323" target="_blank">📅 22:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76322">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 23-05-2026
منصتيّ قبّة حديديّة تابعتين لجيش العدو الإسرائيلي في ثكنة راميم (هونين) بمحلّقتي
أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/76322" target="_blank">📅 22:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76321">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🌟
بيان صادر عن حزب الله ردًا على مزاعم العدو الإسرائيلي الكاذبة حول سدّ القرعون:
يواصل العدو الإسرائيلي سياسة الأكاذيب والتضليل لتبرير اعتداءاته المستمرة على لبنان وجرائمه بحق المدنيين والأطفال والمسعفين والإعلاميين، في انتهاك صارخ لكل القوانين والأعراف الدولية. واليوم يخرج علينا بمزاعم كاذبة واتهامات سخيفة لتبرير اعتدائه الخطير في محيط سدّ القرعون، الذي يُعد من أهم المنشآت والبنى التحتية المائية الحيوية والاستراتيجية في لبنان، ويشكّل مصدرًا أساسيًا للمياه والريّ والطاقة الكهربائية لعشرات المناطق اللبنانية، بما يمس مباشرة بأمن اللبنانيين.
إن ادعاء العدو حرصه على البنى التحتية اللبنانية وخيرات لبنان المائية والزراعية والكهربائية، وخوفه على الاقتصاد اللبناني، لن ينطلي على أحد. وإن سعيه لتحميل المقاومة مسؤولية الأزمات التي تسبب بها الاحتلال نفسه وعدوانه المستمر بدعم أميركي مفتوح ومباشر، ومحاولة تصوير المقاومة كأنها تعمل ضد المصلحة الوطنية اللبنانية، يندرجان في سياق التحريض الداخلي وإثارة الفتنة وبث الانقسامات بين اللبنانيين.
إن العدو الإسرائيلي، الذي دمّر خلال حروبه واعتداءاته المتكررة على لبنان الجسور والطرقات ومحطات الكهرباء والمياه والمرافئ والمنازل والمنشآت المدنية، ولا يزال يمارس يوميًا اعتداءاته بحق اللبنانيين وسيادة لبنان ومقدراته الوطنية، لا يمكن أن يدّعي حرصه عليها أو أن يكون حاميًا لها، بل يبقى التهديد الحقيقي والدائم لأمن لبنان واستقراره وبناه التحتية واقتصاده.
وإننا إذ نحذر من أن تكون هذه الادعاءات والذرائع المفبركة تمهيدًا لاعتداء إسرائيلي جديد يستهدف سد القرعون أو محيطه، أو يستهدف المنشآت المدنية والحيوية في لبنان، فإننا نضع هذه التهديدات برسم المجتمع الدولي والمؤسسات الحقوقية والإنسانية، التي باتت مطالبة بكسر صمتها إزاء الاعتداءات الإسرائيلية المتكررة على لبنان وبناه التحتية.
كما ندعو الدولة اللبنانية، بكل مؤسساتها، إلى دق جرس الإنذار وعدم الاكتفاء بالمشاهدة، والتحرك الفوري على المستويات الدبلوماسية والقانونية والإعلامية كافة، وتقديم شكوى عاجلة إلى الجهات الدولية المختصة، بما يضع المجتمع الدولي أمام مسؤوليته في لجم هذا العدو عن عدوانه وإجرامه بحق لبنان وشعبه.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/76321" target="_blank">📅 21:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76320">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇷
مصدر إيراني مُقرّب من فريق التفاوض: خلافًا لما تزعمه بعض المصادر الغربية من أن نص ما يُسمى "مذكرة التفاهم" بين إيران والولايات المتحدة قد تم الانتهاء منه، وأنه ينتظر فقط إعلان الطرفين، فهذا غير صحيح، ولم يتم الانتهاء من صياغة النص بعد. لم تُعلن إيران بعدُ…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76320" target="_blank">📅 21:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76319">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTyTvMetv0c7O3MbvLP0jIktyOQJLBiFfEbifChOjzZdlkAxlHCEvotfmw0cxIAZwrP-pdDa36QuNp7zWQx55HmM7Hr4jmk7tc6GkQbGy0K0ppqhakGzK-4EP41gNIiUsvxpc3N3AOl-GQbdj6tYsVlh1yXiBXct0BR3NlxUhhti-iQLx0sTNh2zG6rXJdDz2IIClpwHqB5SefIjdVOBQxNaFk54u7-XB57yc_x40t3ZokFdfDZVlNA-ZGLKfyDQvNMegkpN8a_xyaGCV4ySLgi4LpwITKtEzon1WUKQ6D4zQA4faNkExIpzBxY_Hodgn7-226jjQalsfJpVhRMFVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
🇮🇶
🇮🇶
اهتمام روسي إعلامي كبير بزيارة الحاج فالح الفياض رئيس هيئة الحشد الشعبي و السيد قاسم الاعرجي للعاصمة موسكو ..</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/76319" target="_blank">📅 21:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76318">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇺🇸
سي إن إن: ترامب يسعى للحصول على المشورة قبل الموافقة على الاتفاق مع إيران.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/76318" target="_blank">📅 21:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76317">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/76317" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سرايا أولياء الدم بالميدان
#شاركها</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/76317" target="_blank">📅 21:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76316">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بيان هام بعد قليل لا ابو مهدي الجعفري الناطق العسكري لسرايا اولياء الدم … لذلك نسترعي الانتباه</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/76316" target="_blank">📅 21:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76315">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⭐️
ذي أتلانتيك:
بدأ ترامب الحرب لأسباب شخصية، وليس استراتيجية واضحة، وهو الآن في طريقه للخسارة لتلك الأسباب الشخصية نفسها، حيث خدع نفسه فقط.
الرئيس الذي كان دائمًا ما يصف أسلافه بـ "الأغبياء" ويصف نفسه بـ "الذكي" تجاهل أن كل شخص من كارتر وريغان إلى بايدن كان حكيمًا بما يكفي لعدم بدء حرب كبيرة مع إيران.
ترامب طالب بـ "الاستسلام غير المشروط" لإيران، لكنه يتفاوض الآن على صفقة تلبي طلبات طهران أكثر من طلبات واشنطن.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/76315" target="_blank">📅 21:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76314">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KR0woLxSJ99URNS6-_A1s6H6SvIZDGqCg_NgC6SUuPySret4GgzZ8L7_0Ew8s1x18WGP3yWEJQqXk0YsL1boRXj7KtWXK_z4BYLoZtNCHM9rcTF_MYKG6XwjI7zkF2kGZiYVwrO9CZLn34H3B7_UV6QSN-K7G1yRfejDnpepMgMDEovkMGsWDayTwqq7uICVHVcOi5jVuF_l6LRpZ_ZT23FkuQMc_rNEFmlSH9hQcT4kX1nilqfP8TCSRJ-cKleXZgfogxdCR_ghayeNO4IYUSQJVQtZvrYxjPdpaKLf8hMOsZaU8tl8u3a4tqirsrrzaW46sRY3W_E2UFu1vxVhtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاول مرة بدر تخرج عن المألوف
🌟
المكتب السياسي لفيلق بدر ينشر عن تحديات التي تعرقل مضي العراق في مشروع التنمية بتفاصيل اكثر
اضغط هنا</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76314" target="_blank">📅 21:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76313">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇺🇸
مصادر أمريكية: نؤكد توصل الولايات المتحدة وإيران إلى مذكرة تفاهم بشأن مضيق هرمز والمفاوضات النووية.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76313" target="_blank">📅 20:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76312">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
25-05-2026
آليتين تابعتين لجيش العدو الإسرائيلي عند موقع رأس الناقورة البحري على الحدود اللبنانية الجنوبية بمحلّقتي أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76312" target="_blank">📅 20:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76311">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
تظاهر نحو 30 رئيس بلدية إسرائيلي أمام مبنى الأمم المتحدة احتجاجًا على القرار المشين بإدراج "إسرائيل" على القائمة السوداء بتهمة العنف الجنسي إلى جانب حركة حماس. وأوضح وفد من مركز بيريز الأكاديمي أن "هذا قرار معادٍ للسامية، ومنفصل عن الواقع، وغير أخلاقي.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76311" target="_blank">📅 20:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76310">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: بعد تقييم الوضع، تبقى سياسة الدفاع لقيادة الجبهة الداخلية دون تغيير، وستظل سارية المفعول حتى الساعة الثامنة مساءً من يوم الأحد الموافق 31 مايو 2026.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/76310" target="_blank">📅 20:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76309">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🏴‍☠️
‏إذاعة جيش العدو: شكوك بشأن نجاح عملية اغتيال علي الحسيني قائد وحدة الصواريخ في حزب الله</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76309" target="_blank">📅 20:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76308">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
بعد تقييم الوضع، تبقى سياسة الدفاع لقيادة الجبهة الداخلية دون تغيير، وستظل سارية المفعول حتى الساعة الثامنة مساءً من يوم الأحد الموافق 31 مايو 2026.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76308" target="_blank">📅 20:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76307">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني مسعود بزشكيان:
نحن لا نسعى لامتلاك أسلحة نووية، ولا نمارس الدبلوماسية بالإذلال؛ إن الاضطرابات في المنطقة سببها
إسرائيل
.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76307" target="_blank">📅 20:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76306">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed657d94fe.mp4?token=vZAhQ0p320DXs7Z-ukCTrDcWkeUOqOqPcdBYHkDb0e-9m_5y84P1so03pug9--y4sIfBdxmitV9n7Ywja2nLe_TxBebiAJO4bmDsauhq8QT8iFachd12rEAjK-cB4HoCckq3NJxlElrIMlHJtb5VyAg5g919GUcMxpwxZdHCxSelYTAWztXmN8Tnb_CkxFA8ERXPlrBc4hQ2ZljtAVNoCvjwIR5lgnTVy_OkcL6xHt32PGEfP3POavXMklJDCxgV1uvAghXIG-vHB0XSmYuZbRW5dmEO5d-BxFM1yJE7wframa24H8Np91Uqb6_0tRdBYp2HZEp8chyV_Dd_RwGZ7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed657d94fe.mp4?token=vZAhQ0p320DXs7Z-ukCTrDcWkeUOqOqPcdBYHkDb0e-9m_5y84P1so03pug9--y4sIfBdxmitV9n7Ywja2nLe_TxBebiAJO4bmDsauhq8QT8iFachd12rEAjK-cB4HoCckq3NJxlElrIMlHJtb5VyAg5g919GUcMxpwxZdHCxSelYTAWztXmN8Tnb_CkxFA8ERXPlrBc4hQ2ZljtAVNoCvjwIR5lgnTVy_OkcL6xHt32PGEfP3POavXMklJDCxgV1uvAghXIG-vHB0XSmYuZbRW5dmEO5d-BxFM1yJE7wframa24H8Np91Uqb6_0tRdBYp2HZEp8chyV_Dd_RwGZ7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
إعلام العدو:
انقطاع التيار الكهربائي في المطلة بعد إطلاق صواريخ من قبل حزب الله.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76306" target="_blank">📅 20:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76305">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇷
نائب وزير الخارجية الإيراني: لن نوقع على أي تفاهم لا ينسجم مع مصالحنا وسنرد على أي انتهاك لوقف إطلاق النار.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76305" target="_blank">📅 19:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76304">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⭐️
‏أكسيوس عن مسؤولين: اتفقت الولايات المتحدة وإيران على تمديد وقف إطلاق النار لمدة 60 يومًا وإطار المحادثات النووية، لكن ترامب يؤجل التوقيع شخصيًا. لقد طلب من الوسطاء بضعة أيام للتفكير في الأمر قبل اتخاذ قرار نهائي.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76304" target="_blank">📅 19:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76303">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
25-05-2026
خيمة تموضع لجنود جيش العدو الإسرائيلي في موقع حدب البستان على الحدود اللبنانية الجنوبية بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76303" target="_blank">📅 19:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76302">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c83ccef82c.mp4?token=Hgm_MdYwSY_IWA0oQ4aNh1qem9Ehw2EEad_zEUXS7PTmpd0qOeYp3VnEyacFpGyhwBigy6xEgta8zcg61b5mCu1zXtr0N2sa-wncf0TNjAJ9IoKkTeEDeI06tSEasIiFOAGM3SDyqI88Rm_2C3NU5DjzVx3bTt_h2lO8Bl1z2eJ917MUH5m3w9yxUVpFvTdAXY5g34maIjwrtgzh972Ks4NJ2_Hpm5GUIFRzxPNpFbsFq3xwd31qELCsUcS6diMUjIEGXp07Qt2OAzUdn_2gWqrfFb6tRHX6b0152rvIVemIs2Xds6BLorJMwbVhrbTeEAz44ijBVIg6oRL76i50xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c83ccef82c.mp4?token=Hgm_MdYwSY_IWA0oQ4aNh1qem9Ehw2EEad_zEUXS7PTmpd0qOeYp3VnEyacFpGyhwBigy6xEgta8zcg61b5mCu1zXtr0N2sa-wncf0TNjAJ9IoKkTeEDeI06tSEasIiFOAGM3SDyqI88Rm_2C3NU5DjzVx3bTt_h2lO8Bl1z2eJ917MUH5m3w9yxUVpFvTdAXY5g34maIjwrtgzh972Ks4NJ2_Hpm5GUIFRzxPNpFbsFq3xwd31qELCsUcS6diMUjIEGXp07Qt2OAzUdn_2gWqrfFb6tRHX6b0152rvIVemIs2Xds6BLorJMwbVhrbTeEAz44ijBVIg6oRL76i50xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
متظاهر حريدي في محاولة إنتحار رفضاً للإنضمام إلى الخدمة العسكرية ومن تحت عجلة يهتف "نموت ولن ننضم للخدمة".
😭</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76302" target="_blank">📅 19:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76301">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9421e16253.mp4?token=iBvfmaD_cHTHjOOkf_9s4giwdS9fM-TMFBT3VATHIGRGSvMxArmbEY5eVaF7sjvjybndrZMMd72U2Iik-ZWzZ4KuihvMIf84_fzko0htfwdWB8JeTI4T--vJcgwOYoNFv1Yhjg5VsC-TrjpGAVedm3-KNBWmqYUTaRSPY6S57xQCaPHFBiL6CVUfYIc-kdCBVywB7HBHKwnUXCGE4OoSFO_1gRPs6hDK5yonw8RStWvJjKz3KGNivIy3uNDwI_2x14poELbkVyEEqjWU6vRtYZH9G7dyukf0csBAY8o2OTfZSsQvXGtY4ktXskXGHr01jKAEGZg2V88Xd0wVKMxXZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9421e16253.mp4?token=iBvfmaD_cHTHjOOkf_9s4giwdS9fM-TMFBT3VATHIGRGSvMxArmbEY5eVaF7sjvjybndrZMMd72U2Iik-ZWzZ4KuihvMIf84_fzko0htfwdWB8JeTI4T--vJcgwOYoNFv1Yhjg5VsC-TrjpGAVedm3-KNBWmqYUTaRSPY6S57xQCaPHFBiL6CVUfYIc-kdCBVywB7HBHKwnUXCGE4OoSFO_1gRPs6hDK5yonw8RStWvJjKz3KGNivIy3uNDwI_2x14poELbkVyEEqjWU6vRtYZH9G7dyukf0csBAY8o2OTfZSsQvXGtY4ktXskXGHr01jKAEGZg2V88Xd0wVKMxXZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▫️
🇮🇶
🇮🇶
اهتمام روسي إعلامي كبير بزيارة الحاج فالح الفياض رئيس هيئة الحشد الشعبي و السيد قاسم الاعرجي للعاصمة موسكو ..</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/76301" target="_blank">📅 19:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76300">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47e2cac299.mp4?token=Cb2OThkGiGTRYDLMqQf1lSQ456T33JIzB0vMrNjABicJM6-Tq8fU-VHmfvCTVIzxLQ_JDG7dEfJyD0MQUBYa614PqGV8wP5B1JYT3aPDIaXad_Zq-7GeSFVJzsSDOSnQwKVQz1hW4Fs2eI4Gc2ZyUTHKXQLXjT7ShF0hNEIj5Z1dWxaJdY_emjzzxjZr7aFLb9swLaR0enArGlCzanuMR6CmKDo993sxFNCoP2L8BRiJ4E-tqdKS8RIpx49-YjHHT6iXoXk8KxX3yQ7ovCpdddvx7da-m37NgIevakJle0B5mUEu2PyxnaXjKohxWIEFHD0f5-F21LnHp1VP_5lP9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47e2cac299.mp4?token=Cb2OThkGiGTRYDLMqQf1lSQ456T33JIzB0vMrNjABicJM6-Tq8fU-VHmfvCTVIzxLQ_JDG7dEfJyD0MQUBYa614PqGV8wP5B1JYT3aPDIaXad_Zq-7GeSFVJzsSDOSnQwKVQz1hW4Fs2eI4Gc2ZyUTHKXQLXjT7ShF0hNEIj5Z1dWxaJdY_emjzzxjZr7aFLb9swLaR0enArGlCzanuMR6CmKDo993sxFNCoP2L8BRiJ4E-tqdKS8RIpx49-YjHHT6iXoXk8KxX3yQ7ovCpdddvx7da-m37NgIevakJle0B5mUEu2PyxnaXjKohxWIEFHD0f5-F21LnHp1VP_5lP9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
البيت الأبيض ينشر فيديو مع عبارة "هل أنت تستمع؟".</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76300" target="_blank">📅 18:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76299">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⭐️
إعلام العدو:
التقديرات هي أن المعركة القادمة مع إيران ستبدأ بمفاجأة تامة دون أي إنذار مسبق.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76299" target="_blank">📅 18:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76298">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🌟
حزب الله ينشر:
لِتَعلَم كلّ أمٍ عِبريّة...
תדע כל אם עברייה...</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76298" target="_blank">📅 18:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76297">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇺🇸
وزارة الخزانة الأمريكية تهدد سلطنة عُمان:
‏لن تتسامح حكومة الولايات المتحدة مع أي محاولة لفرض رسوم عبور في مضيق هرمز. وعلى سلطنة عُمان، على وجه الخصوص، أن تعلم أن وزارة الخزانة الأمريكية ستستهدف بقوة أي جهة متورطة - بشكل مباشر أو غير مباشر - في تسهيل فرض رسوم العبور، وسيتم معاقبة أي شريك متواطئ. يجب على جميع الدول رفض أي محاولات من جانب إيران لعرقلة حرية التجارة رفضًا قاطعًا.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76297" target="_blank">📅 18:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76296">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a977370897.mp4?token=oNr6uChliYwpoddlIVaRKuCBJgmNqVKw2Tox33NRF8Jmcpz4Pt6X1FsayekgZ1MeIRhNrd_L24pId4qfsU88rpzik4_OQh3jecIVOObomuXYlOkiuUt1z1RaL1ZSWwWhoMRHSkg8a91yeb3_2Sa28go5wW_RyWM6MhDMAGbuza_UkIgOPxnPEGlJrAejN81js8i87NdV-lN4vep5xoQZAY14h-r3BkakFa7sxX-QXa0Nph5h5VJTKach-TY889YqpCUJHKdsGRirGRpOz9Ol46leBTIfxajWeXeR3fcfdCo9JYbrw69nW85tSqZXHx-J2O35HYZKE2BUFKkkp6e_EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a977370897.mp4?token=oNr6uChliYwpoddlIVaRKuCBJgmNqVKw2Tox33NRF8Jmcpz4Pt6X1FsayekgZ1MeIRhNrd_L24pId4qfsU88rpzik4_OQh3jecIVOObomuXYlOkiuUt1z1RaL1ZSWwWhoMRHSkg8a91yeb3_2Sa28go5wW_RyWM6MhDMAGbuza_UkIgOPxnPEGlJrAejN81js8i87NdV-lN4vep5xoQZAY14h-r3BkakFa7sxX-QXa0Nph5h5VJTKach-TY889YqpCUJHKdsGRirGRpOz9Ol46leBTIfxajWeXeR3fcfdCo9JYbrw69nW85tSqZXHx-J2O35HYZKE2BUFKkkp6e_EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
إطلاق صواريخ إعتراضية شمال فلسطين المحتلة دون تفعيل صافرات الإنذار.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76296" target="_blank">📅 18:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76295">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">⭐️
‏
أكسيوس عن مسؤولين:
اتفقت الولايات المتحدة وإيران على تمديد وقف إطلاق النار لمدة 60 يومًا وإطار المحادثات النووية، لكن ترامب يؤجل التوقيع شخصيًا. لقد طلب من الوسطاء بضعة أيام للتفكير في الأمر قبل اتخاذ قرار نهائي.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76295" target="_blank">📅 17:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76294">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🏴‍☠️
🇺🇳
‏الكيان الصهيوني يعلن تعليق علاقاته مع الأمين العام للأمم المتحدة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76294" target="_blank">📅 17:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76293">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🏴‍☠️
نتن ياهو يوجه الجيش الاسرائيلي برفع نسبة السيطرة في قطاع غزة من 60% الى 70%</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76293" target="_blank">📅 17:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76292">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🏴‍☠️
نتن ياهو يوجه
الجيش الاسرائيلي
برفع نسبة السيطرة في قطاع غزة من 60% الى 70%</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76292" target="_blank">📅 17:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76291">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇶
أنصار الله الأوفياء الفصيل العراقي ؛ يعلن عن استهداف قيادي بالحركة على الأيادي الصهيو أمريكية في محافظة ميسان جنوبي العراق .</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76291" target="_blank">📅 17:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76290">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تنظيم داعش الارهابي يتبنى الانفجار الذي طال جهاز مكافحة الارهاب العراقي</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76290" target="_blank">📅 17:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76289">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇷
‏
التلفزيون الايراني:
بينما انتهكت أمريكا وقف إطلاق النار مرارًا وتكرارًا بمهاجمة الأراضي الايرانية خلال المفاوضات وفترة وقف إطلاق النار، يسعى جيش هذا البلد إلى إيجاد ذريعة لبدء حرب من خلال بناء رواية زائفة! سيكون رد إيران من خارج المنطقة. المفاوضات ما هي إلا خداع أمريكي جديد</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76289" target="_blank">📅 16:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76288">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🤺
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 19-05-2026
آلية هندسيّة تابعة لجيش العدو الإسرائيلي في مدينة الخيام جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/76288" target="_blank">📅 16:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76287">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hN25WyLr_Y7O7yv-ijMMLgKoRNGVjeEVm5YIpcBie6Nnq0wapi-36RrOV2H7qrOSxZxvVOqGU32QofGa544jxqSQBfH-sp5VXBWWmN3QNXzDwf3IGaFAI2LjdBn-CvlrfNUKFbjHAaY4vLNYvjXFlTrg-tjeszbjHPjZd4nWjvhWj2raY-RvLPxrlgfnl-JQYubvTl2y6lr0uauVrJSAQ26kdh5z6JVX5CEffVJSKa87arYbuVrrCfFbLRb2qCRWR-35fBGKcfKI3-hnQirsd0ifAe7U4YRZdvoqnpy0tg1Rpz3AxqQG2nyorZ20KTKZ1dAlRRwoH25hDAxfKWJnSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
وزير الخزانة الأمريكي:
سنمنع الطائرات الإيرانية من الهبوط في المطارات والتزود بالوقود وبيع التذاكر.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76287" target="_blank">📅 16:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76286">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وسائل اعلام تزعم:
إسلام أباد ستعرض يوم غد على واشنطن نقل اليورانيوم الإيراني إلى بكين تحت رقابة دولية.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76286" target="_blank">📅 16:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76285">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r08TeGoHRJV4wyPkwXihoJoDz1SKYnheW_778sVO5mwOi54AOArjds1bYWh84ic2mFsCaU-t06QWfY-dKqFFx8ie0assIqS-xRXZQ-AwJGd2E4KCuzNwbQSVt6QmyzVzw4Qcs0qPPeogAzaN_HI4OsrTNTFseoAiRFbLLmDE190f_QrjfWbMV4ZuXYSFP4pKjnw9Ti9TGatHu1bBkURBspP-O43BQy6FmjrwBNk4fW-_20nOVCMeKFYXpADF81vrIkh9R15k2hp4-5jEkPS0xmmuHmIwO8SvB21LPbxn82VDaEANt-utMeJsZx8hMxOMXV4U_jVBZWbawOkXCGfr0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قيادي في حزب تقدم يدعو لمقاطعة منتوجات المدعو بـ(ابو جنة) بسبب حلفه بـ"الامام علي"!</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/76285" target="_blank">📅 15:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76284">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26db9455a5.mp4?token=QDwXPBGMcXstlDknxPTX-gEMeWqnL_zfLDuQhEHWoOmYwHmjyf_kuTO4HiGj-pKpGo6WXPl6WHed93uu68V7ICdW0N9Q1w7_6zzdMk3U9XM30OVoJWleMVrDTbTDFX7tfS-YwtgOzGz-U0mp3KZWrutzJn9D8QgzsOjjgVRAM1DFBuHThxjkZNF2cVBI1riG0_tYkrXN-mySwHLCxPz88I9Elq3blnCYVhIZm3NKBM1Ds162D5CvxlI9ZfVCM_IfJWRjhKskbVOWr2-l8k1zeUz42YffAxyfjEmvLrnOzuonPhMTBEs8807JuF8kechg4NHsi94qf_Dl0jmq4XkRwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26db9455a5.mp4?token=QDwXPBGMcXstlDknxPTX-gEMeWqnL_zfLDuQhEHWoOmYwHmjyf_kuTO4HiGj-pKpGo6WXPl6WHed93uu68V7ICdW0N9Q1w7_6zzdMk3U9XM30OVoJWleMVrDTbTDFX7tfS-YwtgOzGz-U0mp3KZWrutzJn9D8QgzsOjjgVRAM1DFBuHThxjkZNF2cVBI1riG0_tYkrXN-mySwHLCxPz88I9Elq3blnCYVhIZm3NKBM1Ds162D5CvxlI9ZfVCM_IfJWRjhKskbVOWr2-l8k1zeUz42YffAxyfjEmvLrnOzuonPhMTBEs8807JuF8kechg4NHsi94qf_Dl0jmq4XkRwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
‏إذاعة جيش العدو: شكوك بشأن نجاح عملية اغتيال علي الحسيني قائد وحدة الصواريخ في حزب الله</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/76284" target="_blank">📅 14:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76283">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">إعلام العدو يدعي : اغتيال علي الحسيني مسؤول الصواريخ في فرقة الإمام الحسين</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76283" target="_blank">📅 14:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76282">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/704b0794ee.mp4?token=Vmg43E27RxutNB22bTzU6EmNfXQmTAKrTgLXJ-9zL4Df_-YO3B2ZYzUXEva-aqWj-n_PXeam5JYaDXkuY9dDahLn4ktUF6PbCcX207_qCq1UmRnsdJpZfP6mAu57H29UIfSm6OAf7x6jxfVlGekfECZ3HZRjaVxs1I2LKQNkytYQTKfaaaxXrAKjzlupeRHke8QxIruEaWooPxfruldT2ws1kM-OVDmJ-u7u9tbIA0ERbrWnaJVIQ1EHyHXPQK5U1avDo-BZhWCa_liljaC0anEgZg-tWJF9qxPf6ob74znzIIBqMWAw_xkcVyoq0WTTVtV2j-LMy5_7pwb-vYAX9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/704b0794ee.mp4?token=Vmg43E27RxutNB22bTzU6EmNfXQmTAKrTgLXJ-9zL4Df_-YO3B2ZYzUXEva-aqWj-n_PXeam5JYaDXkuY9dDahLn4ktUF6PbCcX207_qCq1UmRnsdJpZfP6mAu57H29UIfSm6OAf7x6jxfVlGekfECZ3HZRjaVxs1I2LKQNkytYQTKfaaaxXrAKjzlupeRHke8QxIruEaWooPxfruldT2ws1kM-OVDmJ-u7u9tbIA0ERbrWnaJVIQ1EHyHXPQK5U1avDo-BZhWCa_liljaC0anEgZg-tWJF9qxPf6ob74znzIIBqMWAw_xkcVyoq0WTTVtV2j-LMy5_7pwb-vYAX9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
أنصار الله الأوفياء الفصيل العراقي ؛ يعلن عن استهداف قيادي بالحركة على الأيادي الصهيو أمريكية في محافظة ميسان جنوبي العراق .</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/76282" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76281">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ضربة جوية قرب مطار بيروت</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76281" target="_blank">📅 14:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76280">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/406121fc42.mp4?token=CLXE3HGdclHgXYB_Wb0oydFTwTeiSDMPU5TVClu9aIi9dbF5n--U0MPZQVG9haaVLFn7M50X783Cmk9bsg7IXMT7WHWk4fmnTYeQjoly93_hK2KDggx1wHBfc8qo-zdkf1rbuZi-GGHHyqH3jJ6qXRi4Mhf5ER0HUrsZDql6yTii500qRiO4-ghpJiXO0s0dlSF4DhAz5QlQ2WhmSjRyqqf7frU_R_Vp9OeHxEHMgtnrh-UE84zySKmQTPi1pCUJ_4a9QKh6DoJoXTKPovFYNkOUT1MGlS9FNi_apypvhBPgFYi0JFoS_qz1rOiXhbfH8uPccIqVkNg0twjoi7MepA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/406121fc42.mp4?token=CLXE3HGdclHgXYB_Wb0oydFTwTeiSDMPU5TVClu9aIi9dbF5n--U0MPZQVG9haaVLFn7M50X783Cmk9bsg7IXMT7WHWk4fmnTYeQjoly93_hK2KDggx1wHBfc8qo-zdkf1rbuZi-GGHHyqH3jJ6qXRi4Mhf5ER0HUrsZDql6yTii500qRiO4-ghpJiXO0s0dlSF4DhAz5QlQ2WhmSjRyqqf7frU_R_Vp9OeHxEHMgtnrh-UE84zySKmQTPi1pCUJ_4a9QKh6DoJoXTKPovFYNkOUT1MGlS9FNi_apypvhBPgFYi0JFoS_qz1rOiXhbfH8uPccIqVkNg0twjoi7MepA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضربة جوية قرب مطار بيروت</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76280" target="_blank">📅 14:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76279">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ضربة جوية قرب مطار بيروت</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76279" target="_blank">📅 14:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76277">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇺🇸
جيش العدو الامريكي:
في الساعة 10:17 مساء بالتوقيت الشرقي يوم 27 مايو، أطلقت إيران صاروخا باليستيا باتجاه الكويت حدث هذا الانتهاك الصارخ لوقف إطلاق النار من قبل النظام الإيراني بعد ساعات من إطلاق القوات الإيرانية خمس طائرات بدون طيار هجومية أحادية الاتجاه تشكل تهديدا واضحا في مضيق هرمز وبالقرب منه</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76277" target="_blank">📅 14:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76276">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پیام_حضرت_آیت‌الله_سیّدمجتبیٰ_خامنه‌ای_رهبر_معظّم_انقلاب_اسلامی.pdf</div>
  <div class="tg-doc-extra">131.9 KB</div>
</div>
<a href="https://t.me/naya_foriraq/76276" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📖
متن کامل پیام حضرت آیت‌الله سیدمجتبی خامنه‌ای رهبر انقلاب اسلامی به‌مناسبت سالروز افتتاح اولین دوره مجلس شورای اسلامی و آغاز سومین سال فعالیت مجلس دوازدهم | ۷ خرداد ۱۴۰۵
🔗
https://farsi.khamenei.ir/news-content?id=62984
📲
@rahbar_enghelab_ir</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/76276" target="_blank">📅 14:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76275">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">#ترفيهي
الأمين العام لمجلس التعاون الخليجي: ندين بأشد العبارات استمرار الهجمات الإيرانية الغادرة على دولة الكويت
جا وتهديدات ترامب لعمان؟
😄</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76275" target="_blank">📅 13:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76274">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇺🇳
الأمم المتحدة:
معلومات تشير لأن غارات إسرائيلية بما فيها على صور والنبطية أدت لمقتل مدنيين بينهم نساء وأطفال.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76274" target="_blank">📅 13:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76273">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af565a9037.mp4?token=vuVZcH6Hoqw9mRsRIVC7GkL_9tddiXLPyVCPmeVkYmVnZ_QZiEFzsd7lf34Is1vjWB8bm-h6tCfRnmpikVO5DXxAb2ZcqahBPNeS-GB_4VhbJm6NtGDosjo6WI6WdwpQwq38bPD_UQVENH1PsX3AkIQV-jAutes7S9CmjYWKNCGQBE_766nbtb64gdgA4WnJMf0USku4mIbcgVDp6rzuydiFISSJ-bEN6AcMP8B9VdhpAWWWcBjXe13q7CosVYB4qEjxqje4iW-OzmChqjMPIBvy3APgPX-jqFLD2ZwoMDs-2ZHh9lN3fZJqxCYJk3_hQip9NANlMuTKR-ITen2Bbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af565a9037.mp4?token=vuVZcH6Hoqw9mRsRIVC7GkL_9tddiXLPyVCPmeVkYmVnZ_QZiEFzsd7lf34Is1vjWB8bm-h6tCfRnmpikVO5DXxAb2ZcqahBPNeS-GB_4VhbJm6NtGDosjo6WI6WdwpQwq38bPD_UQVENH1PsX3AkIQV-jAutes7S9CmjYWKNCGQBE_766nbtb64gdgA4WnJMf0USku4mIbcgVDp6rzuydiFISSJ-bEN6AcMP8B9VdhpAWWWcBjXe13q7CosVYB4qEjxqje4iW-OzmChqjMPIBvy3APgPX-jqFLD2ZwoMDs-2ZHh9lN3fZJqxCYJk3_hQip9NANlMuTKR-ITen2Bbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
‏
الشرطة السويسرية:
3 جرحى جراء هجوم بسكين في محطة قطارات بمدينة فينترتور.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/76273" target="_blank">📅 13:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76272">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇷
كلمة لقائد الثورة بعد قليل.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/76272" target="_blank">📅 13:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76271">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">📰
‏
رويترز:
تقارير للبنتاغون كشفت عن استهداف قوات أميركية عبر بيانات تحديد المواقع</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/76271" target="_blank">📅 13:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76270">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">📰
اكسيوس:
إدارة ترامب تعقد تدريبات عسكرية لاستعدادات محتملة في حالة حدوث فوضى في كوبا</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/76270" target="_blank">📅 13:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76269">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58cd922a9d.mp4?token=eSsd-svDZGD7EA2evDOdZIH7SUqKq7SzA3vEWenJ5aJOwB_nMTM3YGl3o3kG-0bBbh-aRZ4xTYUMobhM7bXp_CONE5_Hfj7FDz9Zr2ylvO5er952xqXyW3xf-WXavS9Eu1imnJwqTAIUkyPXdOtJpULK2lraF5ypPB8FHO1A0sKulnuiv7WpihLbtfdjWgI32tdGUvvoSOKRjHPB_VlmdpL8GWWYMea0c4K8c8dEYlHPikh9qARG1Q0_q0eoQcBH2TgQR7WnWFTNRl2v-jyAkHwXueqe_J1YJ3TSjBcDakXnaIgsRzwSytaTd-IprOKmb12YuCSlS9Gbjv-_xuLgyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58cd922a9d.mp4?token=eSsd-svDZGD7EA2evDOdZIH7SUqKq7SzA3vEWenJ5aJOwB_nMTM3YGl3o3kG-0bBbh-aRZ4xTYUMobhM7bXp_CONE5_Hfj7FDz9Zr2ylvO5er952xqXyW3xf-WXavS9Eu1imnJwqTAIUkyPXdOtJpULK2lraF5ypPB8FHO1A0sKulnuiv7WpihLbtfdjWgI32tdGUvvoSOKRjHPB_VlmdpL8GWWYMea0c4K8c8dEYlHPikh9qARG1Q0_q0eoQcBH2TgQR7WnWFTNRl2v-jyAkHwXueqe_J1YJ3TSjBcDakXnaIgsRzwSytaTd-IprOKmb12YuCSlS9Gbjv-_xuLgyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇸🇾
توغل اسرائيلي قرب تل الجلع بريف القنيطرة جنوب سوريا.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/76269" target="_blank">📅 12:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76268">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🏴‍☠️
دبابة ميركافا صهيونية تحترق بصواريخ حزب الله جنوب لبنان</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/76268" target="_blank">📅 12:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76267">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0HSHG-uvsuXF0FFE1FiFJ0a6mEgekSzJNEWZfQCyb-QHaPH8pCGKDj3DVqi5Xud4jKtePAhF_CC8YD_tgV9fcP0gLzNxHlvlPMRaX9IrDeNSpq5TA7ZVgrzu6_YfHXiWXGJXKWG3J05_99I9S5r80Ns-pWcFU-qD3L5angLJUpmwzlRTYpNztKQufPn00U12CTbabWRzk42o_1mJ51Cie3xOJn5ryW2H9rXGClRU0bC4CIPMzKsM5e12ETlCNFwzZ5lKivAFngVnNjEtd2K8hARZdNVCf71R3Y1LxPmyMHmi3-ksCnS1P9ORecDVLA862fLbmTZqa6bp4x3sfav1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
قناة العالم الفضائية تنعى مراسلها السوري "حسام زيدان"  شهيداً في غارة اسرائيلية على صيدا جنوب لبنان.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/76267" target="_blank">📅 12:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76266">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2pi2fjclkHm-LsXtz0J_J-aI6MJR03FKshLWNh_zU-Iyvt2rnYSqu0dvUJ9p0yKt_t-Rwot_kgLk7PYQ06UOwMBzGnOhSD70zddsXQBMXoEROTX1Xc-t8NFDCaeabjGBeCuLlgxBd5RUss_3O6Ux-RDTkD1sdSs6qr33k7T6j6Izd0RDdCuxJ3s5UOZsaxT5E3jMSYWsmhLaiRbAYuTO2-q9mHZJnnI-4SNauWO8kSW8qJWDlZRf6yrWldmkCup2QoERCXQYY0yWOO_7IlTNjbiS5rEg4RSNzAsDyX4qJnMDjDuDahuCyopr4-spWvOgQl7S2addRQMB4kR_QIZBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر يعلن انفكاك سرايا السلام عن التيار الشيعي الوطني والحاقها التحاقا تاما بالدولة.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/76266" target="_blank">📅 12:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76265">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏حدث أمني بحري في البحر الأسود</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/76265" target="_blank">📅 11:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76264">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏حدث أمني بحري في البحر الأسود</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/76264" target="_blank">📅 11:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76263">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال: تحطم طائرة خفيفة الوزن في "عيمك يزرعيل" (مرج ابن عامر) نتيجة خلل أثناء الهبوط</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/76263" target="_blank">📅 11:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76262">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏الخارجية الإيرانية: ندين الهجوم الأميركي على مناطق في بندر عباس فجر اليوم
أمريكا تواصل انتهاك وقف النار المبرم في 8 أبريل</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/76262" target="_blank">📅 11:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76261">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5918e5486f.mp4?token=oI8OSEVuOYeD0mVrs3O0R7hxBqrPeSaepv8TDImp6o7ZExaZ78zuSIX4u0jRNA-oM0uIfCZqvStPpdRSzR25hdV-mMRw4mQfsLs1wmNYQcKqix6XgS4uiVXkllrn7_zAesClgKgCCGAxQaKEvNpxPFHpYmoZjXeZY3uV36FY1GEvfneERsUMDkjxz-m0-EW0ywf_Z8j3tiYprw-BkqHIohvVlNqxzigBdJigLCmkihI6WQAMGniadDP_cs-daKscZaYl3oWpjPpKMLUpFF8ytDQVjJjDPokF2KB0LtOt6AZQgR3VwPL3AL0OTICu6fJR4ea2fBT8d2-702rZp-ryZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5918e5486f.mp4?token=oI8OSEVuOYeD0mVrs3O0R7hxBqrPeSaepv8TDImp6o7ZExaZ78zuSIX4u0jRNA-oM0uIfCZqvStPpdRSzR25hdV-mMRw4mQfsLs1wmNYQcKqix6XgS4uiVXkllrn7_zAesClgKgCCGAxQaKEvNpxPFHpYmoZjXeZY3uV36FY1GEvfneERsUMDkjxz-m0-EW0ywf_Z8j3tiYprw-BkqHIohvVlNqxzigBdJigLCmkihI6WQAMGniadDP_cs-daKscZaYl3oWpjPpKMLUpFF8ytDQVjJjDPokF2KB0LtOt6AZQgR3VwPL3AL0OTICu6fJR4ea2fBT8d2-702rZp-ryZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الحرس الثوري الإيراني ينشر مشاهد الرد على هجوم الجيش الأمريكي فجر اليوم على نقطة في ضواحي مطار بندر عباس.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/76261" target="_blank">📅 11:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76260">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⚽️
قرعة كأس آسيا تضع منتخب العراق الشبابي إلى جانب الإمارات وتايلاند وتركمانستان.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/76260" target="_blank">📅 10:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76259">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">📰
بلومبرج: رفع ترامب نسخة جديدة من دعواه القضائية التي تبلغ قيمتها 10 مليارات دولار بتهمة التشهير ضد صحيفة وول ستريت جورنال وشركتها الأم نيوز كورب، وذلك بسبب مقال حول علاقاته الوثيقة المزعومة بجيفري إبستين.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/76259" target="_blank">📅 09:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76258">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بوليتيكو: القوات والأسلحة الأمريكية جاهزة لمهاجمة كوبا، ولا ينقصها سوى الأمر النهائي من ترامب.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/76258" target="_blank">📅 09:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76257">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بيانات التداول: أسعار النفط العالمية ترتفع بنحو 4% صباح الخميس وسط توقعات باضطرابات في عبور ناقلات النفط عبر مضيق هرمز</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/76257" target="_blank">📅 08:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76256">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⭐️
دوي انفجارات عنيفة في الكويت نتيجة هجوم  صاروخي وطيران مسير،تفعيل الدفاعات الجوية الآن</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/76256" target="_blank">📅 06:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76255">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⭐️
دوي انفجارات عنيفة في الكويت نتيجة هجوم  صاروخي وطيران مسير،تفعيل الدفاعات الجوية الآن</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/76255" target="_blank">📅 06:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76254">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
🇮🇷
إن بي سي عن مسؤول أمريكي: هجمات "محدودة للغاية" و"دقيقة للغاية" قد نفذها الجيش الأمريكي بعد سلسلة من إطلاق الصواريخ والطائرات بدون طيار والقوارب الصغيرة من قبل الحرس الثوري الإيراني.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/76254" target="_blank">📅 04:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76253">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇸
🇮🇷
أكسيوس عن مسؤول أمريكي: أطلقت إيران أربع طائرات مسيرة هجومية أحادية الاتجاه تستهدف سفينة تابعة للبحرية الأمريكية وسفينة تجارية.  اعترضت القوات الأمريكية الطائرات المسيرة وضربت أيضًا وحدة أخرى إيرانية لإطلاق الطائرات المسيرة على الأرض قبل أن تتمكن من إطلاق…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/76253" target="_blank">📅 03:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76252">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">إعلام أمريكي : الولايات المتحدة نفذت عملية دفاعية في بندر عباس بإيران، مضيفاً أن "الولايات المتحدة ستتحرك لحماية مصالحها الإقليمية، وهذا لا يؤثر على وقف إطلاق النار".</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/76252" target="_blank">📅 03:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76251">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">إعلام إيراني : الأصوات التي سمعت في بندر عباس نتيجة تفعيل الدفاعات الجوية على اجسام مشبوهة</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/76251" target="_blank">📅 02:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76250">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">إعلام إيراني : الأصوات التي سمعت في بندر عباس نتيجة تفعيل الدفاعات الجوية على اجسام مشبوهة</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/76250" target="_blank">📅 02:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76249">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRtnJmU1Jbf4SxvIY2umD9gk3i9CAXspjAsNNpEuRdtSAk0KLvNUpNDAYsiNP57MeDDy3eMlxxmWpvwSiAbpVmVN0mEl-bgWOYnHF0SVradkwjTukyt4kd-zb9X0b64Vr-5hjllCBi6rsrisZZTbpvk53BJL1WmteqpDezjnYZZidQ6QUb56VS0TOPgE6hZimi-hqk1CrQzLeNYXsQU-TTQ3W1lpHziaTy7Hg9aEhIrFqUhvZywGyoqhFhQk2MyYk67ttzYCbTsev7zckIq62v19ZlmCZBHOnnUDlLiflraavLOZvbAZgyV1AyYH_GmefP4gwJSXF9a0Admc0yUQmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
وزارة خارجية كوريا الشمالية:
لن تتخلى كوريا الشمالية عن برنامجها النووي أبداً.
والبي زود خل يجي
...</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/76249" target="_blank">📅 01:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76248">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🌟
🌟
الجندية روتم ياناي التي قُتلت اليوم نتيجة إصابة طائرة مسيّرة مفخخة في شومِرا كانت من المفترض أن تسافر قريبًا في رحلة إلى تايلاند، لكن ذهبت سفرة الى الله.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/76248" target="_blank">📅 00:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76247">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dbfb4847d.mp4?token=p_sRzEiZLlM-Lf4zWNs3LFQSgS3MJp_M46FjaN3WFaNeD9Q_xDOhqb3mTxIQKu8v0ffJu8io_dHlSgmEp_xmtJ1L6dsMl62KRUdHgjhZa4irvuimc5xHE5sFabNA5cUq6vFh8oc_zwQ5bPt06AVtpR-pudDgGxKNm1mFgn1lP5HUl5c__QqZ9p45WWInwp043d4kRs3pu3lcubJszl1r9t6qQhXim-pd8CUv-L_1dec6ykmi3PRxFSD5BWfzy5XeBkUuwFxu6-3lTPl4l7L1tASpLYPoEb3jGft7M7u3kQqztssS2CZr2NF8xCJzxyuwnygO7M36KSUrI_VxFKNd4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dbfb4847d.mp4?token=p_sRzEiZLlM-Lf4zWNs3LFQSgS3MJp_M46FjaN3WFaNeD9Q_xDOhqb3mTxIQKu8v0ffJu8io_dHlSgmEp_xmtJ1L6dsMl62KRUdHgjhZa4irvuimc5xHE5sFabNA5cUq6vFh8oc_zwQ5bPt06AVtpR-pudDgGxKNm1mFgn1lP5HUl5c__QqZ9p45WWInwp043d4kRs3pu3lcubJszl1r9t6qQhXim-pd8CUv-L_1dec6ykmi3PRxFSD5BWfzy5XeBkUuwFxu6-3lTPl4l7L1tASpLYPoEb3jGft7M7u3kQqztssS2CZr2NF8xCJzxyuwnygO7M36KSUrI_VxFKNd4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
اشتباكات عنيفة في محافظة كركوك شمالي العراق بين القوات الامنية وعصابات داعsh اسفرت عن مقتل عدد من عناصر داعsh وتدمير عدة مضافات.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/76247" target="_blank">📅 00:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76246">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">هل قتل العراق العقل المدبر وأبرز مصنعي الأسلحة الكيماوية في داعش قبل يومين ؟!
ننتظر التأكيد الرسمي</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/76246" target="_blank">📅 00:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76245">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🌟
🌟
الجندية روتم ياناي التي قُتلت اليوم نتيجة إصابة طائرة مسيّرة مفخخة في شومِرا كانت من المفترض أن تسافر قريبًا في رحلة إلى تايلاند، لكن ذهبت سفرة الى الله.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/76245" target="_blank">📅 23:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76244">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAKGn4EjvEjQyYYUE9rV-kWcYgfVynyqqnlP19JVd3HW7nfYs6ITLAlCG_Bics9_EWDqYeZ-JuxilTgUA6myVRBl1Tz_E4momYzmdWA3-5VHU8IEBLM5RQV4AbpwEAbR0TVC-FrBlh5DCugCfwhyZrj1A1-6uvK4_gAYC4zYpz-Mk_t0HgjD5rZSNxUa5B6bA8jeJm_ypRtLydsvJsTf9RHi33LUNnyEzzjBtBpkNkRSfcF-jOy5-JSG4KvnE8nD6Hjyr2LYNsbX_qjBYKYmhBRFiDSOMPKdf0uEGsPQbegdjC7Je77tUPFoHO-ij466XWc9l2536flU5GrrG1ZH0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انباء اولية: قتيل و7 جرحى في شوميراه بعد هجوم مسير لحزب الله.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/76244" target="_blank">📅 23:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76243">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🌟
أُنقذ "ترامب" من الذبح خلال عيد الأضحى. اشترت السلطات البنغلاديشية جاموسًا أمهق نادرًا يزن 700 كيلوغرام، أطلق عليه السكان المحليون لقب "ترامب" نسبةً إلى خصلة شعره الشقراء الأمامية، التي تُذكّر بتسريحة شعر السياسي الأمريكي.
كان من المقرر ذبح الحيوان خلال عيد الأضحى، لكن الوضع استقطب اهتمامًا كبيرًا، إذ بدأ الناس بالتوافد لرؤية الجاموس غير المألوف. عندها قررت السلطات التدخل، فاشترت "ترامب" من مالكه، وأرسلته إلى حديقة حيوان دكا.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/76243" target="_blank">📅 22:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76242">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 23-05-2026 منصّة منظومة مضادة للمحلّقات تابعة لجيش العدو الإسرائيلي عند مرتفع الجرداح على الحدود اللبنانية الجنوبية بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/76242" target="_blank">📅 22:43 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

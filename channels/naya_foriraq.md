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
<img src="https://cdn4.telesco.pe/file/jqvikChziGgJF6MY_8xrfTdZWR78TfJ0GHJJzzSievrrH-2gF5pi9fvZiQK33FHU5woUv_goWzVOoEyPL7qaK8YvyuJHwu6doO_qbh5NsPppMbzf_pJRHYUJbJIGu4sJGipqzqs5PJms5TzKMIMynza3ILIPgVoT8WFHRpTXJBbYsh1MJ145Y8QUGm1GysarTQFiD0ATWE4TJnLaG5t221ySSDLKqgyrz0sInzfqSvCyswFN65UAJKQZjXnNXRCcDltCI-iUAzGJC7U_EaxV9L67QtjXFVbpu0TLDFKClF9ma6zcu7VW_LR0Kn_-i-x0HHZ7vRAeaC6onbVwyOGj7Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 264K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 05:04:34</div>
<hr>

<div class="tg-post" id="msg-93047">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
البنتاغون : سيتم بث إعدام مطلق النار في فورت هود رمياً بالرصاص في الولايات المتحدة على الهواء مباشرة</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/93047" target="_blank">📅 00:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93046">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a053f827f4.mp4?token=VoVCfkNzY81RrpaejV3h1-qTHZVZNdxcFYgJXa7XC54o8NLkmjMhowmY89u5AU50xDkXtwpDpKQGL5UPzqkoQF5iYc3BxqWGcFw8vo2f9Y-2tiwYyoic8wOBEiVJ2kc5C7dRwNTzr7_xetXoza_9-NfN12YFoR-kCOLjgBGdFw89nodcS3BG2hvCkOV5CbZU-R2QEqIuOB4N0JplbhpzFtBN2hfXDiPuPZbiH-C6-AUrR6w2JullwT8UMopLvEQaYNUxLB_lYedXrtgrSlBl5gp0yP8KtXfMs-zJBJtph_NqsGuqzdqB-d6acIt3hNM054hzr5Jio0nIN_xdCQWtWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a053f827f4.mp4?token=VoVCfkNzY81RrpaejV3h1-qTHZVZNdxcFYgJXa7XC54o8NLkmjMhowmY89u5AU50xDkXtwpDpKQGL5UPzqkoQF5iYc3BxqWGcFw8vo2f9Y-2tiwYyoic8wOBEiVJ2kc5C7dRwNTzr7_xetXoza_9-NfN12YFoR-kCOLjgBGdFw89nodcS3BG2hvCkOV5CbZU-R2QEqIuOB4N0JplbhpzFtBN2hfXDiPuPZbiH-C6-AUrR6w2JullwT8UMopLvEQaYNUxLB_lYedXrtgrSlBl5gp0yP8KtXfMs-zJBJtph_NqsGuqzdqB-d6acIt3hNM054hzr5Jio0nIN_xdCQWtWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد حصرية لنايا... لانطلاق الدفاعات الجوية السعودية من وسط مطار الملك خالد الدولي بعد استهدافه بصواريخ اليمنية.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/93046" target="_blank">📅 00:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93045">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b786078ca8.mp4?token=sC0jojLC5cttBVawG-Dia9ZPnwnYeKnRYsk-Oo8oVZv4xE8dC6dc20hmSDlKqTU8q19JicNqQvhMy0G08uIziElTAagywqS1Z0Rv5tKZxw4AMfY_WcTWrSss1hv4b651xzXgZx-Q4MkhyGhi1HJzHMqqzvTNCTgmmmbS3d0B1vN1_QGnxs4ozslIxtHsJCSpbLeLD8Kz2KsosJPsLhTr15G6M1F22pmtesQBn3OO_AU9ic8w5pRX7_yOUIvWzg1ibsfVneF7-Vl9raiJADq-i1dZXRCS2wdz78R4OvmnOeyw0pGNwNgUJfGjE4jFK2KMlSwwTAjv2VdGSEtF5DhM8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b786078ca8.mp4?token=sC0jojLC5cttBVawG-Dia9ZPnwnYeKnRYsk-Oo8oVZv4xE8dC6dc20hmSDlKqTU8q19JicNqQvhMy0G08uIziElTAagywqS1Z0Rv5tKZxw4AMfY_WcTWrSss1hv4b651xzXgZx-Q4MkhyGhi1HJzHMqqzvTNCTgmmmbS3d0B1vN1_QGnxs4ozslIxtHsJCSpbLeLD8Kz2KsosJPsLhTr15G6M1F22pmtesQBn3OO_AU9ic8w5pRX7_yOUIvWzg1ibsfVneF7-Vl9raiJADq-i1dZXRCS2wdz78R4OvmnOeyw0pGNwNgUJfGjE4jFK2KMlSwwTAjv2VdGSEtF5DhM8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة الهجوم اليمني على مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/93045" target="_blank">📅 00:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93044">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي
: وزارة الدفاع الأمريكية تضع خططًا جديدة لضربة محتملة ضد إيران في الوقت الذي يتردد فيه ترامب.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/93044" target="_blank">📅 00:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93043">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇫🇷
🇸🇦
رئيس الأركان الفرنسي:
لا نزال ندرس مع السعودية خيارات تتضمن وسائل عسكرية للمساعدة بحماية ميناء ينبع النفطي.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/93043" target="_blank">📅 00:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93042">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/93042" target="_blank">📅 00:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93041">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-KR2vy542XkGq8hkL3mL9OLdOOBlONFnkIdZ-14xp8jw2E2REf8gjgq2gzaJvaGhgFshaTKUWZcY3dVEfMOOsRQ8MkvEdke61jh5bgsUd8gzmUQtq2K_KX_8pZFqWA9AVEUbZFuOHEM-Ap4Si93uCBrFoLWeDwd4Dy8YMeyUnLhGB_AwPEKB7hu-RB66HL4hAnbIxOMAtyRKbZYSyhhtGsc4rIzblU1RylfXnCujTIXk6KB1SDnUmasTRyZqffIO32wPjJnPWbHh6rpv2JcBgpWmTMdTOLfPZq9PJH22YKUZ8ydYlo7zv3a94OfBkEs2NPZ7Shg2TK1GkPxi2mPNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇺🇸
🇮🇱
🇸🇦
🔻
أصدرت السفارة الأمريكية في القدس تنبيهاً أمنياً تحث فيه الأمريكيين في جميع أنحاء الشرق الأوسط على توخي الحذر الشديد، محذرةً من احتمال حدوث اضطرابات في الرحلات الجوية وتصاعد سريع في الأعمال العدائية بين السعودية " والحوثيين " ..</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/93041" target="_blank">📅 23:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93040">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8Qk-a_vldigB1ZpKt5Ea1lCFL0VLPuAbQSyz_-skGM_iBtHM875LMcyptshS8jM4gnDtaetIW9oda-AHPYqGaAhkFuZ9P6A_76QVCcNIN05Y8HPqrRkfC-j2Fh5FJqVaExxm50b6dOL4L5hppInrQiFdhmNHrLoR0PE9WIitGCLkepROVp3x5I4vhGlbX7av30hT_aQDOXajYn8j0tD-q3owpKYzrgF5ZgivDb61tpOjm89izQIrsxOmDf3NtQRKbnFGSlIf33rKw77TlzQUh4VqYy3RGyvffHOjS6jCRIckumeEH9Tlz2TOAIG6AnSv-VaTHD7y6OYYVmlzpmGuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
متداول
وثيقة تتضمن شمول رئيس هيئة الاستثمار العراقي بقيد جنائي ! الأمر الذي يطرح تسأل عن كيفية الموافقة عليه بمنصبه الحالي !</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/93040" target="_blank">📅 23:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93039">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWsMoga7GES3DCFYHv8ZcsN8Er-u5Ov31HJPAoGy35R6eMtX50szGNe13IK9-MFwoRGCgUBvkQBoapZEqoX5nSAVCR-zei1Ls05iApP-anghS2CKN1uKu_NXesz8bRQV6rEdGiQ5gVcEb4Gip5J9sipgmh3dFJOkSICBEcJ101Tc68_TJ296Id0LBlJ0zlYBIL7ICtItcF2WJwkBGDd_UTOVIGPugQc5tF16df-E4SCHlr9bbV7l3WCbChfexVxnfWpa--PBDk_oJ7rIgViNzybBS3xzJQoBy0HJXaKG4LiP775LLgcqmDMZp0lkQg-AhW7J33BnuCtqHwz_E7ce4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصوات انفجارات في صنعاء</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/93039" target="_blank">📅 23:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93038">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اصوات انفجارات في صنعاء</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/93038" target="_blank">📅 23:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93037">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxzKardN_-PJUFcMmOC_LJ2PIMrHGHPIgBkpAH4yXJiGYyNEoVW9KC7haLhscYnVOjWUOdJbbibRIWCl3Hb-_NIPMSoGivSN4rTdpcfkFoDz6ngsK57FrvAZjd6u-ogU_Blo2W2hYLhduiIZNaPjh6xAximz3FIuLXtd2qAjb2OjgB40Rr9suSaSAoOaCwD_W2SUMoKkKOWq_pcRty87ak2F7vDt5wjFxu5wH3rxFGTzPGCAOZvYxdoO3m4h5DyCeSbcMezACMpvQFaMo0HQT0_aPX1DJcTnO22sz6mK2MSmspvEr2gnnDaK9epDUsbfy4z9Ok8Lolj-pbKk0XJBnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
تحذير أمني جديد من السفارة الأمريكية في بغداد للمواطنين الأمريكيين في العراق</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/93037" target="_blank">📅 23:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93036">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L926QE9lYRT0yT2PDz9P8qbMSUWSpvgDstyLWXM_4sT4Gydt22kChtfGmCWiwVuMFER6Jl9pnmWHc_LhIaluTusOfY5OKlaLxH-1EDS5Plge2733t8ITIcaBCsL1YMCqNWNbs8mvVeUbk0uwvru35AMjielKmJ3jZYUhDwmRpv3atdPyTjJ25JK9_mJ26AKfGWUhp82SBZ89sS7cyXCrdjbkqh5LRz6x0_N7VeGTxpGRdHooz4473wEM_dvMeqFmj9w9q44fRX8dmn2O7etwNi-7bR-6XmO0xZI8AhEAoZLNJSTqfVaspDV1egW4zbCjF-Dfn1qsN9iC1QkidRaJvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
اندلاع نزاع عشائري في محافظة ميسان جنوبي العراق مقتل طفل واحد كحصيلة اولية.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/93036" target="_blank">📅 23:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93035">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
🇮🇱
السفارة الأمريكية في القدس تحذر المواطنين الأمريكيين الموجودين في إسرائيل:
يجب على المواطنين الأمريكيين الاستعداد لاحتمالية إلغاء الرحلات الجوية.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/93035" target="_blank">📅 23:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93034">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa770901e6.mp4?token=u3L2A1mWfChxsg3IUwT5bnwNVaPFZBeOlz96BSBJXif4L7Y79aFq2tzOAU745iKGVz5szyQllJ75-oYz2HJcDFZdxsesKrOYfChVg2g59NwrinTwG2KMSyNutunkfor8bwLmGmP29b5C0jM1fvOqFAnBd-N5UhofSX6SM6qTymz421cgtI3mqwyAVj0LVQWBvHuDD6tZOKTe9UgDhfVbG_JmM_6cvQPO1B4MSQt9uGatOekOY9BSiO5Rqe1w5X6Y6XkV7_Vn_fvXY2u2-n2GOBr47NVvDzma9_FumThqwep02Sq413TveUlNmSCAXMcgMqIb7D3XmRPVjGJRbEac3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa770901e6.mp4?token=u3L2A1mWfChxsg3IUwT5bnwNVaPFZBeOlz96BSBJXif4L7Y79aFq2tzOAU745iKGVz5szyQllJ75-oYz2HJcDFZdxsesKrOYfChVg2g59NwrinTwG2KMSyNutunkfor8bwLmGmP29b5C0jM1fvOqFAnBd-N5UhofSX6SM6qTymz421cgtI3mqwyAVj0LVQWBvHuDD6tZOKTe9UgDhfVbG_JmM_6cvQPO1B4MSQt9uGatOekOY9BSiO5Rqe1w5X6Y6XkV7_Vn_fvXY2u2-n2GOBr47NVvDzma9_FumThqwep02Sq413TveUlNmSCAXMcgMqIb7D3XmRPVjGJRbEac3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
توثيق قريب ومباشر للحظة استهداف احد مقرات الاحزاب المعارضة الايرانية في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/93034" target="_blank">📅 23:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93032">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c0ef9968e.mp4?token=ZzlEeayY7y9loR8WG0PiwN9Vp3N4f0YBnVgtjt2BdrR2c4Fby1E_-ok57K8tkkaJmy9n-dZalhqiYM5pYqpYQD3QC0dB7a5QBmmDErHY7m-IBOrMV_TJPM-YlaCcIOaA_kJUigIC5mN8-9j3OJv6nKbEx1X4wwO9Tdwg1Pl2M3WOpGoMH1LYe3M6HA8NDiFRLLQ97JhrgFDlvqd-HIwbep2oqtM4JNKiqiaBLHPCOmHOhqRGOUutFn5ShrRDm_2sVcgejD4xdgzKp1JTsFyRWJEKJK5UnxFD0Ej1ibHVWrdXRxi_G-URVL9ZPI7qxQ1YBenzl8DWHZD3TcYigkfJAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c0ef9968e.mp4?token=ZzlEeayY7y9loR8WG0PiwN9Vp3N4f0YBnVgtjt2BdrR2c4Fby1E_-ok57K8tkkaJmy9n-dZalhqiYM5pYqpYQD3QC0dB7a5QBmmDErHY7m-IBOrMV_TJPM-YlaCcIOaA_kJUigIC5mN8-9j3OJv6nKbEx1X4wwO9Tdwg1Pl2M3WOpGoMH1LYe3M6HA8NDiFRLLQ97JhrgFDlvqd-HIwbep2oqtM4JNKiqiaBLHPCOmHOhqRGOUutFn5ShrRDm_2sVcgejD4xdgzKp1JTsFyRWJEKJK5UnxFD0Ej1ibHVWrdXRxi_G-URVL9ZPI7qxQ1YBenzl8DWHZD3TcYigkfJAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من مقرات الاحزاب المعارضة في اربيل</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/93032" target="_blank">📅 23:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93031">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039ff7ebef.mp4?token=nPuq2aWZD-lccpSZ3v9DrKOiN3acpL21GBdPd9MNMlc5oc4G-CM7vvF_lmXAdum6-i5rrnxjaAw05zj7oa8zmBmnSvt20OJR9iNr4ktWuciWUwqYHBEdAvc14qtFbHUlx1BR0gq-JF1pyHZ06zbl4HzZ8DU1HCk2_tR76PFHYRzbg2NbSQzHJYTllaJcTr6VLmBw61alh0cZ0lNBBSJSwo8AGpfiRJ8jt2aGcfiVa7l-B7nEYXqF8-WaYRrkDsUnBap7K7SzAqU8lkzpFLvTeGBNp-9arBYgynEpB3qbtF4lHMeqfAhKjQ_7LYB9QD41ZXW6ME1x_nT0untP-_PY3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039ff7ebef.mp4?token=nPuq2aWZD-lccpSZ3v9DrKOiN3acpL21GBdPd9MNMlc5oc4G-CM7vvF_lmXAdum6-i5rrnxjaAw05zj7oa8zmBmnSvt20OJR9iNr4ktWuciWUwqYHBEdAvc14qtFbHUlx1BR0gq-JF1pyHZ06zbl4HzZ8DU1HCk2_tR76PFHYRzbg2NbSQzHJYTllaJcTr6VLmBw61alh0cZ0lNBBSJSwo8AGpfiRJ8jt2aGcfiVa7l-B7nEYXqF8-WaYRrkDsUnBap7K7SzAqU8lkzpFLvTeGBNp-9arBYgynEpB3qbtF4lHMeqfAhKjQ_7LYB9QD41ZXW6ME1x_nT0untP-_PY3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد قريبة للحظات الاولى لسقوط المباشر على احد مقرات الاحزاب الايرانية المعارضة في اربيل.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/93031" target="_blank">📅 23:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93030">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace48d1baf.mp4?token=KRGD3qA1c-zeC4BaZXTR3cgFNH0-J6nsvcsKO91cTBSKgcydrbOjVhM5K7SYpHbKWlghbfPz04wC4rN41zsWSNe3FP9Q7kn6tJID8L1kY7EJOqA9GKSqFWW9HTEId94AWy8axfbVod884_ZjNt9Xyvoapm-5Vd8AZcnosTcGb69EPkIy32shtiCF3eh6fG5CR9wlU2qH5W0lr_vFCvFyURQnrDWBqzlL32ClqhqGPrs7qmXlwCN49zxrEejT7FTsv6wuZZy6ZnjP1hwfWzDeIVrMpu-YqITpBwAH9sJUwarE3zksHcaTpbSMbLy9Ed_SZB4lTs5Ui1IQPIQifuAxvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace48d1baf.mp4?token=KRGD3qA1c-zeC4BaZXTR3cgFNH0-J6nsvcsKO91cTBSKgcydrbOjVhM5K7SYpHbKWlghbfPz04wC4rN41zsWSNe3FP9Q7kn6tJID8L1kY7EJOqA9GKSqFWW9HTEId94AWy8axfbVod884_ZjNt9Xyvoapm-5Vd8AZcnosTcGb69EPkIy32shtiCF3eh6fG5CR9wlU2qH5W0lr_vFCvFyURQnrDWBqzlL32ClqhqGPrs7qmXlwCN49zxrEejT7FTsv6wuZZy6ZnjP1hwfWzDeIVrMpu-YqITpBwAH9sJUwarE3zksHcaTpbSMbLy9Ed_SZB4lTs5Ui1IQPIQifuAxvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد من محاولات اسقاط الطارئات المسيرة المتجهة الى مقرات الاحزاب الايرانية في محافظة اربيل قبل ان تسقط على اهدافها بشكل مباشر.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/93030" target="_blank">📅 23:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93029">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bf39202dd.mp4?token=D6JTJ1LlW3kBl_44S6ZLIRkLGvJHorhe4nQvp2EsoDj4duzIaNWen7s8Gco9qSnnqnGcP7yrvMfwK4l3bPvc7UuvjI03-L03DRheg1OZpELk0I4ljpq4vhzhSqjR34ebpPVqoJfXSOLbiQP2PZyS-kV3N9F-hTamXqCU17qSJCKA6256YaZVNlQA4UzK9_CHJyPieAbc2lUub9eimss51ljr2uSsbc7fEDHQPnt8Xq-Ue8wuSs1NzF3CdR3_1jysqNS-nsgDrEKLtrjN1tqlD8375jTXVQutzzFWPIllIulD8uCqd3zdMjlym_Yhs9YbS_Yfr24kNPxrFB3ImVg9Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bf39202dd.mp4?token=D6JTJ1LlW3kBl_44S6ZLIRkLGvJHorhe4nQvp2EsoDj4duzIaNWen7s8Gco9qSnnqnGcP7yrvMfwK4l3bPvc7UuvjI03-L03DRheg1OZpELk0I4ljpq4vhzhSqjR34ebpPVqoJfXSOLbiQP2PZyS-kV3N9F-hTamXqCU17qSJCKA6256YaZVNlQA4UzK9_CHJyPieAbc2lUub9eimss51ljr2uSsbc7fEDHQPnt8Xq-Ue8wuSs1NzF3CdR3_1jysqNS-nsgDrEKLtrjN1tqlD8375jTXVQutzzFWPIllIulD8uCqd3zdMjlym_Yhs9YbS_Yfr24kNPxrFB3ImVg9Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرائق واسعة تطال مقرات المعارضة في اربيل.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/93029" target="_blank">📅 23:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93028">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db89739427.mp4?token=FTbPF2cu-rO_SehknHI0do-Kw38n6zTObHbO22dqyF27kBNNMRLdgG9kGWtqfAyYnUF0paEfPAZ1G7u1RKO05lwcdqx6ZS9Vc1A-Ugt22Wk33M9dYyIaN7yN_4DY4DXD_eP4095Q-Dd37Rv7CteEq2-DWL3BtSmDSCAITduryY-zKU-41S8LhGQJQ2wNh9xjb_pHMvqe9J6PWRPexPTeZ_ybNT_68EwS3imQhQoHTL4e0UAHydNZ_qSt1jkG5osc7Xkdl_RNgGHkLsMZ2IuR5SbRlCqPAiONZs8hpMtKnQhQ0CiSU6y_cR-3a4flkN8j-j_qYE5fzvW9_O_QtcqYyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db89739427.mp4?token=FTbPF2cu-rO_SehknHI0do-Kw38n6zTObHbO22dqyF27kBNNMRLdgG9kGWtqfAyYnUF0paEfPAZ1G7u1RKO05lwcdqx6ZS9Vc1A-Ugt22Wk33M9dYyIaN7yN_4DY4DXD_eP4095Q-Dd37Rv7CteEq2-DWL3BtSmDSCAITduryY-zKU-41S8LhGQJQ2wNh9xjb_pHMvqe9J6PWRPexPTeZ_ybNT_68EwS3imQhQoHTL4e0UAHydNZ_qSt1jkG5osc7Xkdl_RNgGHkLsMZ2IuR5SbRlCqPAiONZs8hpMtKnQhQ0CiSU6y_cR-3a4flkN8j-j_qYE5fzvW9_O_QtcqYyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد اخرى للحظات الاستهداف الت طالت مقرات الاحزاب الايراني المعارضة في اربيل.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/93028" target="_blank">📅 23:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93027">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f064a85ad2.mp4?token=nR-VxQ6fgZuKVluvIP7p_W9iYtZZ62bTyFMJPupA92Ln3CqEMVPGDHPMV1djj5Ai2ZBLxJBvntk4Bid6am5q4OHdS46_J-Bakj4cWPNayT16NMImCNdmrxTH6YIUinh0bzAa6GFKD14EpuTwTQH5uJlwq-4j1WHDlODtg5c2TrwVFVZat418IBGN3AQn45xbu4dHYtJzJCfi80IRfEVvslnASdpUqCqGIC7srr_IvHFslsxzz84PhjD2TevS9tr7LU3ykBbT5UDgB-sMWoL9wMSPQaEbvsyImqdemvzNuSJjAlMuItxJogVxx6EXmRN8G9s-jG_ciajNxil74leEBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f064a85ad2.mp4?token=nR-VxQ6fgZuKVluvIP7p_W9iYtZZ62bTyFMJPupA92Ln3CqEMVPGDHPMV1djj5Ai2ZBLxJBvntk4Bid6am5q4OHdS46_J-Bakj4cWPNayT16NMImCNdmrxTH6YIUinh0bzAa6GFKD14EpuTwTQH5uJlwq-4j1WHDlODtg5c2TrwVFVZat418IBGN3AQn45xbu4dHYtJzJCfi80IRfEVvslnASdpUqCqGIC7srr_IvHFslsxzz84PhjD2TevS9tr7LU3ykBbT5UDgB-sMWoL9wMSPQaEbvsyImqdemvzNuSJjAlMuItxJogVxx6EXmRN8G9s-jG_ciajNxil74leEBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
استهداف مباشر لمقرات الاحزاب المعارضة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/93027" target="_blank">📅 23:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93026">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30d8437636.mp4?token=STyJLIA0rKtk-5a33lyIIT84FNg5st_t48trhNY32JL2yJSxY5wbrNlcxaVAsv93D1JSKqRV5p1kTdzyCxORDmORoPGRnLsTr1YWX2Wtq-NCiNrfcFVIaaJ7koihr4eeLklhGVdQOu8tbRveGzNOnzFVD1qQql2bbZW6XqRqv7AMi2hmkVEoTZwXu_tA5NEJuVwheQb0zkPsI3KwIksOwe4lGE0XfefbGPOprP-HHhg0oott0ArW54UbElkJkVPMQRyPkm8izaLv_Tzf0AffzmYigDlNpnktK8iwVmtroIgzyxhURd1MTXvld5Q21UPITYDwjxxfRYuwfzoskjCQmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30d8437636.mp4?token=STyJLIA0rKtk-5a33lyIIT84FNg5st_t48trhNY32JL2yJSxY5wbrNlcxaVAsv93D1JSKqRV5p1kTdzyCxORDmORoPGRnLsTr1YWX2Wtq-NCiNrfcFVIaaJ7koihr4eeLklhGVdQOu8tbRveGzNOnzFVD1qQql2bbZW6XqRqv7AMi2hmkVEoTZwXu_tA5NEJuVwheQb0zkPsI3KwIksOwe4lGE0XfefbGPOprP-HHhg0oott0ArW54UbElkJkVPMQRyPkm8izaLv_Tzf0AffzmYigDlNpnktK8iwVmtroIgzyxhURd1MTXvld5Q21UPITYDwjxxfRYuwfzoskjCQmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
لحظة استهداف احد مقرات الاحزاب المعارضة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/93026" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93025">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9dbe316ea.mp4?token=eHuDyaslbRIGaF0Po-frDYWqcyggnE-qWXxGB3jjlRhgpgmiSyUY2PBTzhiENBsRtzn34oIl8rODJuiOodfb6h8EO3pezqJUZf9f4rjtCMVRUYD9cZFN5K2GuqWgEsWcrqFo36FDCfO5SEODXUHmph56IPLzhJxsmIcSD1scB1iu8adfoYb3F0IOCWk_zDzv6zGp2aEw-cLOVTiorTu6ElWh32ADiEdZXR3AbTo7kPwGJYLGBc_eWFnDDq6Zb9s81nLg_2VcvqYe5LUGjdwwyWRRC_EURuP_nenO_v44HG1wCL72OYJzF3FJr2JfwTA8Q_MS1miFKCYaqauatWP9bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9dbe316ea.mp4?token=eHuDyaslbRIGaF0Po-frDYWqcyggnE-qWXxGB3jjlRhgpgmiSyUY2PBTzhiENBsRtzn34oIl8rODJuiOodfb6h8EO3pezqJUZf9f4rjtCMVRUYD9cZFN5K2GuqWgEsWcrqFo36FDCfO5SEODXUHmph56IPLzhJxsmIcSD1scB1iu8adfoYb3F0IOCWk_zDzv6zGp2aEw-cLOVTiorTu6ElWh32ADiEdZXR3AbTo7kPwGJYLGBc_eWFnDDq6Zb9s81nLg_2VcvqYe5LUGjdwwyWRRC_EURuP_nenO_v44HG1wCL72OYJzF3FJr2JfwTA8Q_MS1miFKCYaqauatWP9bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انفجارات عنيفة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/93025" target="_blank">📅 22:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93024">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/391a0aa41d.mp4?token=HdD5waSLC6A0CSADxecFhQAt7kaeh8LjqncIlCP2kUECSDDLj7WYYA1gYNz23pCkmelXCOh60e3MKrfrdRZiqi_DLZpAHrJtr4RDVTHOpOnCC7UFgpeqHz4lqpKFVdR_9O-4uZLCYLZvViRX8EOHjY5204KYo6boJRNw0aPV2glkz_725tp2ltd_VwUmvIUzZe0BT6SMf4c-BW-SCJ3sSS8rbqcv1-e6yW2rupHDYNM9rHFf1FpMLcxy_cNVVZi_rUFS5gcguOR9cdIdlJn_925qAtbPFJfFSokS1S_ieOy7clQ3VHVS7oNQehLzNoAjKQZIzDs4F_gPai4jQXE7yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/391a0aa41d.mp4?token=HdD5waSLC6A0CSADxecFhQAt7kaeh8LjqncIlCP2kUECSDDLj7WYYA1gYNz23pCkmelXCOh60e3MKrfrdRZiqi_DLZpAHrJtr4RDVTHOpOnCC7UFgpeqHz4lqpKFVdR_9O-4uZLCYLZvViRX8EOHjY5204KYo6boJRNw0aPV2glkz_725tp2ltd_VwUmvIUzZe0BT6SMf4c-BW-SCJ3sSS8rbqcv1-e6yW2rupHDYNM9rHFf1FpMLcxy_cNVVZi_rUFS5gcguOR9cdIdlJn_925qAtbPFJfFSokS1S_ieOy7clQ3VHVS7oNQehLzNoAjKQZIzDs4F_gPai4jQXE7yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انفجارات عنيفة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/93024" target="_blank">📅 22:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93023">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الله اكبر
🇾🇪
اليمن تفرض حصار جوي على السعودية</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/93023" target="_blank">📅 22:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93022">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">السفارة الكندية في الرياض
: نحذر من احتمال فرض قيود على المجال الجوي واضطراب الرحلات الجوية في السعودية.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/93022" target="_blank">📅 22:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93021">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇬🇧
🇸🇦
بريطانيا تنصح الآن بعدم سفر أي شخص إلى الرياض، في المملكة العربية السعودية.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/93021" target="_blank">📅 22:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93020">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇶
حدث هام بعد قليل يخص الملف العراقي ..</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/93020" target="_blank">📅 22:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93019">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8NP5y4K3c-yWRgcVYNtOU4tGsnFc3LJweVDBGHm-t3ZAdGxL_JAqz2gQ-Wr6zOEQYxtPDH8wMm6x8qubEcnsXdWh1xmtNMP23evKZouaJ5oDJhv8DSG3tODmH7eDBSafRCbRjARgsT4-k8IKZL3kACTgG0uKcb7Loy2BrdO_L9IHdzFxrM8K6XqVpyybc32qZPWHCM_KkKuqVyiWoSFLk9h-cSV3p9YONATQor5Y9L7mk2nRFoGjEsAmPfY31ECPnyt1p3Ig-sp3MBTkHaukrrWfsey6dUNabKMr9fDIUmybwESqq34w3SMQ-Ho8b_6KMdsUT2SRuhgBLsdumnAzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.
يستمر العدو الأمريكي في انتهاكه الصارخ لسيادتنا الجوية، انطلاقا من قواعدهم في الأردن.
- طيران حربي نوع (F-35) عدد 1.
- طائرة تزود بالوقود (KC-135) عدد 2 .
- طائرات مسيّرة (MQ9) عدد 4 .
طائرة مسيّرة (MQ1) عدد 1.
طوال ساعات يوم الاربعاء 7-10-2026 .</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/93019" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93018">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WceYn54n7FbBtpCCZIVNCHdEupLmVu74XP83Bd2gRnXXAWnAtPGRgioDPn2PXsMO6Hzq4LfG7mq-aeAjxAv5Zt60QyXIdk3GQ7XQNIFbbC1TrbmqMXaDR8k8bD2MJ_7MMqGAnqPrlSpm1-YiEFRKYuOW1tZJMQsTiEgCM3-68DarV9YsunSDjOAgybvXFuaDjPklFRvA5C61M6oGaFew30Qm91ppr3pvVUX3K-9D1-KItEKvIvCQGfSvrE0I0l-jODzQsAWdYR3gp5mRYshMzV6B8WTWAmZLUGFG90Gaju968UjxZO1ZiooIWw5ueCa0_HJf9w8ZbiyaIl4L0WMWSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
🇮🇶
🔻
الحشد الشعبي يمثل العراق في موسكو
حضور د مهند العقابي مع وزير الاتصالات ورئيس خلية الاعلام الأمني في مؤتمر الإعلام والذكاء الصناعي بمشاركة ٧٠ دولة حول العالم</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/93018" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93017">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKMLh5eeulAVGOBizmHKsBQRDjEyt0G__AUPocbjSpUv55Qu8j8X8XqBLjDQTeXqIvtcgBspuKdc0r9NLtiClxQh3E9dVB3IdogH7YALTzfGLvvw0frNSU7jYetW_om_UyH3dD_GOTULUlX4vEUZJwPrykjuw0lGWIXofe816DB15HUu559kDO0tB3sgolnM2dFmQY0uo0FSsZ2RvwfqsFWhW_GItsGmORqb_6K8CufWjivF0V2AOP2iPORmBFN3Juf1-UJGjACg6Yd2i3ilKRQfEPr-hT_iNxDJ4fDoySjNahyxFF4nPytEjwzbYSvDdB1lutbv9IItVK3IzbFCPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
احد الجنود الصهاينة الذي قتل في جنوب لبنان اثر حادث عملياتي حسب وصفهم.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/93017" target="_blank">📅 21:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93016">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇷🇺
🇮🇷
بوتين
:  طلب من بزشكيان نقل أفضل التمنيات إلى المرشد الأعلى لإيران مجتبى خامنئي، روسيا مستعدة لفعل كل شيء لمساعدة إيران في تسوية الوضع الذي نشأ في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/93016" target="_blank">📅 21:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93015">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇶
ازدياد حدة التظاهرات في محافظة البصرة بعد القرار الأخير برفع سعر الصرف.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/93015" target="_blank">📅 21:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93014">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇶
مشاهد لطرد التحشيدات التابعة للعدو السعودي من مديرية الشمايتين بمحافظة تعز - 8 أكتوبر 2026م
.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/93014" target="_blank">📅 21:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93013">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇶
🔻
كتائب سيد الشهداء تحسم الجدل
لا تسليم للسلاح إلا بعدما يكون العراق سيد نفسه .
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/93013" target="_blank">📅 21:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93012">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 59 غارةً جويةً وصاروخاً استهدف بها العاصمة صنعاء ومحافظات الجوف وتعز ومأرب وحجة وصعدة والحديدة ولحج وريمة وإب والبيضاء من خلال طائرات "F-15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف والعدوان الصاروخي من نجران وخلفت شهداء وجرحى بينهم نساء وأطفال.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد على بلدِنا العزيز 1857 غارةً جويةً وصاروخاً.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/93012" target="_blank">📅 21:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93011">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇶
رئيس مجلس النواب العراقي: قرار تغيير سعر الصرف لا رجعة عنه.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/93011" target="_blank">📅 21:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93010">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇶
رئيس مجلس الوزراء العراقي أمام مجلس النواب: كانت أمامنا ثلاثة خيارات الأول الذهاب إلى الادّخار الإجباري وترك الموظف يعيش بالوعود والثاني توزيع الرواتب كل 45 يوماً والثالث الذهاب إلى الاقتراض وإغراق البلد بالديون وهو مثقل بها أصلاً، تسلّمتُ المهمة واقتصادنا…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/93010" target="_blank">📅 21:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93009">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇶
مجموعة من النواب يعلنون استضافة رئيس الوزراء ووزير المالية ومحافظ البنك المركزي لمناقشة تداعيات قرار تغيير سعر الصرف.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/93009" target="_blank">📅 21:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93008">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇷
قائد الثورة الإسلامية سماحة السيد مجتبى الخامنئي:
إن تركيز العدو الأمريكي الصهيوني المجرم وإصراره على ضرب مختلف مستويات الفرج، من أعلى المستويات إلى أدنى مستوياته، كشف عن أهمية هذه المؤسسة أكثر من أي وقت مضى. ومع ذلك، فإن هذا الجهد اليائس والهجمات الخبيثة على أركان النظام والأمن الاجتماعي، والتي لا مثيل لها في التاريخ، لم تثنِ قوات الفرج الباسلة عن أداء مهمتها قيد أنملة، بل واصلت، حتى في الشوارع والسيارات، أداء الدور والواجبات نفسها التي كانت تؤديها في مواقعها ومقراتها.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/93008" target="_blank">📅 20:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93007">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlovO9uenAWHE1U0HE4agnyUSlkyPM_nVyPsbIh3MsRubo0piAKIKJKJIgx6gqkX0_3vESz1L42wr4XVKlzcKwqQfIJQxN9sJH24_SDhFDosYkZ2eSAVtk5IDsEd8LHONFMMKaK3g2xBe_TlPYcnFqd2zXbkoICZ-C-ktaC9DBrtBjlORSuausF0qKzJZpQDPzTrBFHoR_IJJm-89ZSBNAgp9JoiQsVC8kdpTLuo1GbhpVXrVrjN15kyZmD9ZPUjPHe3HEK2gfgkAQiKni8CCdVvT-953_n7Oe9w4cHiWJBeec9mUVjsODqqGKzanLFw5YJpNWAQPsQyNwmyUpyriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
الشيخ اكرم الكعبي:
ندعو الإخوة في مجلس النواب والحكومة العراقية إلى النظر لهذه الاعتبارات، وتقديم أولوية مراعاة معيشة المواطن والعمل على خطط شفافة لإعادة الاستقرار في السوق بعيداً عن المهاترات السياسية.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/93007" target="_blank">📅 20:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93006">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feec5483db.mp4?token=eyy2kmKZCDM-GjIQrfeahbSFnY7S-fPMJ42Ky5TaEiB_BendRygSs6Nzx10YKDRVxzHhhiOwI-A0DFmTUbdNdZDZ6bi2c_fF7fQAWbhmPfYJvMUOkTWJ3NNnjP5IVLUxnBBUUQL5mAltHJn3Rfy6c5V8pxXI_9Cw6zel7dm-VFU2WrFu5B_igTYZKryp4FEmyBRPaVpGMfTIXKmXCu2F8D_CbGVigp3-6WfS25Fw5pdG9I-GWvRNKfCLbr_5IjHHEKLfepkNpwChto4Rb_hWyKMGmXKFpYrsPvvg1Hzcedo6SAUo77vvnwElWzGeQCngEmIQ0qM9IIG9L7UXpreMmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feec5483db.mp4?token=eyy2kmKZCDM-GjIQrfeahbSFnY7S-fPMJ42Ky5TaEiB_BendRygSs6Nzx10YKDRVxzHhhiOwI-A0DFmTUbdNdZDZ6bi2c_fF7fQAWbhmPfYJvMUOkTWJ3NNnjP5IVLUxnBBUUQL5mAltHJn3Rfy6c5V8pxXI_9Cw6zel7dm-VFU2WrFu5B_igTYZKryp4FEmyBRPaVpGMfTIXKmXCu2F8D_CbGVigp3-6WfS25Fw5pdG9I-GWvRNKfCLbr_5IjHHEKLfepkNpwChto4Rb_hWyKMGmXKFpYrsPvvg1Hzcedo6SAUo77vvnwElWzGeQCngEmIQ0qM9IIG9L7UXpreMmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
ازدياد حدة التظاهرات في محافظة البصرة بعد القرار الأخير برفع سعر الصرف.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/93006" target="_blank">📅 20:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93005">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97ff80a1b.mp4?token=pd-3GETEktg2jSxtrKFTNkbjM470yhnYmDtRebs3QM7akt5a6TKNbJ8JIHj8JwAlVf7yewALlRlZSJJrPg6S_oTRCAAS5cQGZl7mZ7vTyIV9D_husFkPDxLYp7kNOeVvhv63P-X3ErkmqdnbYjXq4IG2mMeIBhPAtOdDPMG08PzQP8wZOGesFVKEBuBEN46moSZMMcz0J5YhoCv6JA7YKMWw1yDq6J0UCDe6YL0YEh761BeyvVMe0zWBQCONLKeXHhYQL005Txk_aT8juv5g5lXXscnkkKjuLpLvxSfyOWoSU3FlxlI8Mr-Qu4D6iR6ZmpQyutmB4J_zTXoi0u7bYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97ff80a1b.mp4?token=pd-3GETEktg2jSxtrKFTNkbjM470yhnYmDtRebs3QM7akt5a6TKNbJ8JIHj8JwAlVf7yewALlRlZSJJrPg6S_oTRCAAS5cQGZl7mZ7vTyIV9D_husFkPDxLYp7kNOeVvhv63P-X3ErkmqdnbYjXq4IG2mMeIBhPAtOdDPMG08PzQP8wZOGesFVKEBuBEN46moSZMMcz0J5YhoCv6JA7YKMWw1yDq6J0UCDe6YL0YEh761BeyvVMe0zWBQCONLKeXHhYQL005Txk_aT8juv5g5lXXscnkkKjuLpLvxSfyOWoSU3FlxlI8Mr-Qu4D6iR6ZmpQyutmB4J_zTXoi0u7bYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مقيمة في السعودية تشتكي وتناشد بفتح المطارات السعودية بعد اغلاقها بسبب هجمات قوات المسلحة اليمنية ليتسنى لها العودة إلى بلدها بعد بقائها في السعودية لعدة أسابيع.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/93005" target="_blank">📅 20:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93002">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xvyd1LOq3Wr1n1qmfCK4tRNQAV1hpaGpfadfi-A_3NpVJaay_ZskD8_wBnaOSlW9IDwKwTnhjILpsI5Tbcyvi6JDc1nOtSksNqbB0IvcIiC37NaYh21gxP-Sbx9jS2AdYKiM342kd05TZa7TPqd5jxdHX-S6svH1FZRr5hpi1GGRNIeMoMgIMPdiAckBWzMzFzKJQuaj1pIF__I0cfoir0bY3_wrOky7CAQGtvEevVm9gU76W1Jj---4iVFPLKA5TvaTyPk8e_oM4CNzIQSTna9PxwxMnIl5xdrZoNIm-pjBFSlQ2VIfOt6zqjU--C5WT-CyWCbbBN_qmnm69oNOaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rH9mAKSnnCHxFpvrdLeKCCUXaQyG4mPh9m3myWFRQd0grFTV1zON2Dx53JleeVstPEDVoLhVsZM1bKFWNabqdX_VWlQKYmIFUKdHd4RvpHWxFObPoihDmD1LH1arKkF2qa7S_oP-krhZ6k_PiQDmQo3T6tNPLhGsicjZFJ_jmfB8BkV_5KADHj8fbAq4V2ntMqOKYJEBhpig659s3irC33xFGBT7i5vkEEbQPCJ_00OflQD1K6qWBEEwplk6cu3OToeJfSvDsDy3lBfusMJu058Xs_Srn44QWqdMhpwgYsx7lavWys9KoUNK6xKp_eUULIC5GzTvYyNjcQO6yPnFMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qOwlnbBG1LX6DNTRRiQ65ZguKvshHWEpH8XC9tBiQ1VjDD_p2fEquseuOqRb88pIji2dAlmLDraYDSnDiht8vq6a5j-h6hCZ0utsBjFIbKcCYXM9QViWoVWpoQKqlJT2IFtrs9QJXke5CJLl652lkZvIkQ7tQHzNpgx1QixO-XhcrKOldDoGnwkbo7JmgumKzqO5j00ap6BF7BUJT8gNE2guwF5TRjy911uQUfcBj50Pc2ZBtGp4tmpWEkr2ylp8xkncFh1wB59nFirwMF_K9oSq1M0tmUS4H0PEt4yR9VXEO5iEg5U-KdkUDY2l5JvwO5a4cSF5kWDlw-bhQQMsWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
مجموعة من النواب يعلنون استضافة رئيس الوزراء ووزير المالية ومحافظ البنك المركزي لمناقشة تداعيات قرار تغيير سعر الصرف.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/93002" target="_blank">📅 20:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93001">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/731963d562.mp4?token=u4_Iy5kl1jW5Fc-5AlcWv-BoUcVVsEtHE6RHgVS5lMIWqg_IGO5gyWOXz4aX7mm6P1F1Pc8W1oKjewHll0QgzgMIwjF3gklLVoYjaTdZ5Y_Ii2tGuG-CfJ-DOvQn9Kpew1DqhSEB1cPreeBdCymdoVUdAi94VbRi5HVSbgyOsW9UKBmQaxQX5_CAdtQuXD9gdGSAGOOQeIDDRPPAltEj27AkL4GwAvSc4ZS4EjAKV_YKWFKITokwEV78I-gMGYQzI7N904nT2iDJBu7-xobeU-IbjiExlSg4OMC6cmHygtZ3m6fk5apyWUtlA1lHbCH2ZdTAMtTbmf8lR8FY-uVsjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/731963d562.mp4?token=u4_Iy5kl1jW5Fc-5AlcWv-BoUcVVsEtHE6RHgVS5lMIWqg_IGO5gyWOXz4aX7mm6P1F1Pc8W1oKjewHll0QgzgMIwjF3gklLVoYjaTdZ5Y_Ii2tGuG-CfJ-DOvQn9Kpew1DqhSEB1cPreeBdCymdoVUdAi94VbRi5HVSbgyOsW9UKBmQaxQX5_CAdtQuXD9gdGSAGOOQeIDDRPPAltEj27AkL4GwAvSc4ZS4EjAKV_YKWFKITokwEV78I-gMGYQzI7N904nT2iDJBu7-xobeU-IbjiExlSg4OMC6cmHygtZ3m6fk5apyWUtlA1lHbCH2ZdTAMtTbmf8lR8FY-uVsjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مجموعة من النواب يعلنون استضافة رئيس الوزراء ووزير المالية ومحافظ البنك المركزي لمناقشة تداعيات قرار تغيير سعر الصرف.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/93001" target="_blank">📅 20:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93000">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇺🇸
🇸🇦
البعثة الأمريكية في السعودية تصدر تحذير امني لبعثتها خوفا من الهجمات اليمنية.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/93000" target="_blank">📅 20:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92999">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/db71UYgCrQ0BsEyqKN2z3JJ76HkZoYt6DmxT2CUgTjFARv9gIsOVsOaczNHJPHB9MWVHavN293gArf3D7V25-VYEZyjk6g-rLdNKcyDtO5qjLXrWHEf_UvhZ6n1Gg8MZEM9gjKoyUdVEy6VeS2RbsZfz_ulEdqgWH1oYnyYqyLSrCJolbysKdc8Az89tSQ6xjFwR4qhflCIS6k-HbDb1Oi23ZKtabTQrrrrCviJNsZFos9gHpap5EMBgoDcy69A3k9Wa5FfhmGXUFFgahGPYz5v8E6O8JUAgl56uLSME-sd2PoqwKSvcfStExxPahCyPEPGwZ68z0LIZ-zPG5p0w2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
المعاون العسكري لحركة النجباء الحاج عبد القادر الكربلائي:
فيا أنصار الله ورسوله والإسلام، إننا معكم ولن نتخلى عنكم.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/92999" target="_blank">📅 20:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92998">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqvMFLaXrXrIpPCK_NG2VcEasASuzPutGjX0p8HxVMfhMrgNkWIWaBnw59lNLOidAqDg5B3X4c0mzFLmeEogyurkE-H7qzjg-jhQI0TAx61UvvanJquIgv9QvRK_P2HoxsoMEJN5PxvgLT2PHVE2Z7vLZVdEh_9CBxd5VJ2j1HJ7kwud6paqy2Hlouu987wC0S3NhmCTFOfiAVVF7bXnnNUgxawcVT2JFg6sRwf2BQm_a5ITMQ6I-O-HXfQUWMYAVbWfXLvhX-Hy9SPH7EDQmUEhgBQEiEr1K3tt6vMYnO7dnu4sVwaMxlJ69fzldAQrCSalxyX0dKkYY6JT-R_ksQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: لن نشن هجومًا على إيران في أي وقت قبل الانتخابات النصفية، نحن نجري محادثات مثمرة مع إيران.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/92998" target="_blank">📅 19:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92997">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZkc0YYEzN5N7ak400nlzHIkcNlAdSMTq7SZDj9PTpwWEk_cul6EKeCI9kUPlqDQdsfpmIzYmQlVcGSQrD23M-ZZI-xEQG4sjTaLeOaP4xRFDo4G8nzM9JsO5GxYxJDrFegSYfKUse8F693Sfy0kvAwPkEXmnuUTDZkeTBHyAphmhW4RTHnuYe4WSz_PFSH6JCU2lgpgZxCJ6WAjwzVWCDpxIsupXm2jLp9Ffnl0rZ6vqIX7K2I7wMSF7f2xLE5qSADvvtJkH_GGNn1QmMCp_gwK4rsVYD1cQRpZzaOQw8wZ3vFVJmBK7ZSdhotV6_Zj2lZh_q6ZwPh5AC7p-xKNaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
: لن نشن هجومًا على إيران في أي وقت قبل الانتخابات النصفية، نحن نجري محادثات مثمرة مع إيران.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/92997" target="_blank">📅 19:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92996">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">تدمير طائرة في مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/92996" target="_blank">📅 19:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92995">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇶
‏
مستشار الأمن القومي العراقي:
العراق رفض طلبا من سوريا لإعادة آلاف الأشخاص المشتبه في انتمائهم إلى داعش، اجتماع عُقد مؤخرا بين سوريا والعراق وأميركا لبحث مصير سجناء داعش، العراق أعاد إلى سوريا نحو 50 محتجزا سوريا ثبت أنهم ليسوا أعضاء في داعش.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/92995" target="_blank">📅 19:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92994">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sv7iCY6xEnQJuqRNKDMQJbnKuEE7TQTsYE5kP3IOEeLpCMeunpxEV48a8kBjYXDHJ6S3XCD3cLQGezBynujM6TRkh73I40K0Ikl2xQBZEQlHmNZpJG6tGu5ss_ctTaGUAAkUHOa2OfMk1KuGjXJNy9nX7x2KMQaM7Lf8am3VEg4t8IqxeB9Gf2MbeWWXiNXP2Z3iSkpzr5AvU-_5Oj8jQTmtEy2eT1sMibDzkSGz4_4Ha_6qsD4lDUXPQOA-Rg6_djqjvlu7h6s6yGbaHSxjxtSgr399bg67JHaRSlgoMpxsMd-0LuEVysRJqJm5F0VcphUAkRlBTE8Y8shenN4DyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظة الهجوم اليمني على مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/92994" target="_blank">📅 19:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92993">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06b1ab0be6.mp4?token=DrC8uf5SEONthKkQv8w6g-AxkwZuC83z583uCeOvoaKx4WsWDLotvKyrIMTBmKAMvENkMx3U7MpuW7Lr8YxTzjTN9TDxXLbE-5WKSrel0yz24JhSWAUaMz7DHwHmRMvuD7qFxIJbd-X-03rCchVGC0bcGO2cOt3sIm0NfMMRyOBpR_TCNamg-qHg_sUwFdN_vD16IRgikcW4mtaqXV-C-qFPE-h5ytcc3hcyphbQf64XcJYlzuVtnig-6EEUOah3WVcd0I8bulmhxY6zK64tvSQj0Spx00EmTinkPC6ZUKjb2VB0m9lEddOG_1gjBCEcMSWXSOHXM5xim_vyTn8z8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06b1ab0be6.mp4?token=DrC8uf5SEONthKkQv8w6g-AxkwZuC83z583uCeOvoaKx4WsWDLotvKyrIMTBmKAMvENkMx3U7MpuW7Lr8YxTzjTN9TDxXLbE-5WKSrel0yz24JhSWAUaMz7DHwHmRMvuD7qFxIJbd-X-03rCchVGC0bcGO2cOt3sIm0NfMMRyOBpR_TCNamg-qHg_sUwFdN_vD16IRgikcW4mtaqXV-C-qFPE-h5ytcc3hcyphbQf64XcJYlzuVtnig-6EEUOah3WVcd0I8bulmhxY6zK64tvSQj0Spx00EmTinkPC6ZUKjb2VB0m9lEddOG_1gjBCEcMSWXSOHXM5xim_vyTn8z8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اشتباكات مسلحة بين يهود حريديم وقوات الامن اثناء تضاهراتهم في الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/92993" target="_blank">📅 19:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92992">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
استهدف قواتنا المسلحة مساء اليوم مطار الملك خالد بالرياض بصاروخين مجنحين، ومطار نجران بصاروخ باليستي، والقاعدة الجوية في خميس مشيط بصاروخ باليستي، وكانت الإصابات دقيقة ومباشرة بفضل الله، وأدت إلى تعطل حركة الملاحة في المطارين وإلحاق أضرار بهما وبالقاعدة الجوية.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/92992" target="_blank">📅 19:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92991">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔻
🇮🇷
اللواء وحيدي
: نذكر أن استراتيجيتنا في هذا المجال واضحة ومبدئية وغير قابلة للتغيير: أمن الخليج الفارسي ومضيق هرمز هو أمن داخلي وإقليمي، ولا يحق لأي قوة خارجية تهديده أو التواجد بشكل استعماري أو التدخل فيه. مضيق هرمز هو شريان الحياة للطاقة في العالم، والخط الأحمر الاستراتيجي لإيران الإسلامية، والحفاظ عليه هو الحفاظ على المصالح الوطنية وأمن الأمة وكرامة إيران.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/92991" target="_blank">📅 19:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92990">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انفجارات تهز مضيق هرمز: ناقلة نفط خام تعرضت للاستهداف بمقذوف أثناء عبورها المضيق.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92990" target="_blank">📅 18:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92989">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">😀
الخطوط الجوية الهندية تلغي رحلاتها من وإلى الرياض حتى 10 أكتوبر نظراً لتطورات الوضع في المنطقة.
المطار بالمطار</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/92989" target="_blank">📅 18:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92988">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e92d6aa9cc.mp4?token=oz35TEKU2x5hA1R2aQKLmkJev5NXgFu8nBnx8_6gGJRp3IFlLRduLymGaPqrNVRu0_0UQ9vtoEcPTkGGyHX9SE0UEm4SkZBoUrutOy4auDdSfEtbD1wYWNzgt359TSjdtQtIiuLwblDW-dZ7YHt_KQYDOJe_tzeBk-6Z1JXL5sbBv3dLDtTjcaWk3XXLia6Sif1vkouMYpHd6IKcratS-IM6-NwE9xdVr617GtI8EHyHpl3BFWp6FGqwWqzJ2sdZW-E-_Pb5VKWJHspbAlGxqnYohvCB_b6-NkeAqp3wG9JCgPc-aVpU3gO0CCtU1An3JaSfsuS0D2zAfZHT7L7ifg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e92d6aa9cc.mp4?token=oz35TEKU2x5hA1R2aQKLmkJev5NXgFu8nBnx8_6gGJRp3IFlLRduLymGaPqrNVRu0_0UQ9vtoEcPTkGGyHX9SE0UEm4SkZBoUrutOy4auDdSfEtbD1wYWNzgt359TSjdtQtIiuLwblDW-dZ7YHt_KQYDOJe_tzeBk-6Z1JXL5sbBv3dLDtTjcaWk3XXLia6Sif1vkouMYpHd6IKcratS-IM6-NwE9xdVr617GtI8EHyHpl3BFWp6FGqwWqzJ2sdZW-E-_Pb5VKWJHspbAlGxqnYohvCB_b6-NkeAqp3wG9JCgPc-aVpU3gO0CCtU1An3JaSfsuS0D2zAfZHT7L7ifg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتباكات بين الشرطة الصهيونية ويهود الحريديم في مدينة القدس المحتلة.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/92988" target="_blank">📅 18:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92987">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وزارة المواصلات الصهيونية تصدر تعليمات لشركات الطيران الأجنبية تُلزمها بإجراء فحص لأفراد الطاقم والجنسيات التي يحملونها، في كل رحلة إلى "إسرائيل" أو تعبر مجالها الجوي. ودخلت التعليمات حيز التنفيذ بشكل فوري.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/92987" target="_blank">📅 18:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92983">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BHxvEz3IDpj652J-ohq1S8opqMAqzBtxccUrygNk34-njIyZ3FATBKNPyIFC_NGqYe1cERJ_c3KXuWtx7ozXDN3_6iZw9vgUNholp0Jl4hfVHsGzoZA89Nx02lbxPk0fELTVmhUMDXaCYggyqDf-_cvtD1pln0-HUwtRHt1vmORIQH70czO8TBZtLLT7Bx0NtQtxypXFoA0-MShkqY_aAWkchQw64CrHrxZ_C7HHDBaXF3FUA9t0rmSh4d1J7KpYfTxtviFuW05OUilyEvTodkSuU3CfgwtwsJjtQZCmFcXOh-u18WZmrYyksnD-P7iZx4CRm1VhiHGFYAOqROtKBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZjlk5rDRstKgj3-6vjQIYeYh4enBJjtWQNcaXPn5PR5FsTyVVNpTt9NNNOwafQW30bbV7vo0OslzrhSCoVwTthOlBmUSB8WiIwR1X2_C1t6sXt7vBF2TG4MDL4SNOMSy160nYNFjT0admoD_TgGe55idrIMn_R_pd2G-aOJA7tLht1pT2RdOiXRtAzoyQT5wvP8YQcCpYmoa6xGEdqnAIew5EYWrwxJHZyIV4YsuNXvwjy-nJ_iAt0i8Ckrw5ZM6m9QlWc4Ho3IJkQzTUQHyB-upUlo7yHWWMCuZX4syItirKg2bboUAmOSai_MmbwW6WL-MLclhFOC8evglW3Vig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/479a877651.mp4?token=J89fOySF1TA8b-EkniSOaji8GSDmBulh9CpF-vUnbVevR2smzEEDCCosB8SYFUUOJDtc6F1AkHYM4damKrH0kbSYnEqmiXLGC-PWQOLx6LBqwweOj5bqItbrPgARZjtQfARGAIb8gM9vsMXRANDGIo_yU2D7lR9JtF3ZnUHRHl-IjEh2G0nDRQvGXorKcCfbIkNP18rFdN4XUSr9m5EdMybGPeTFy5Y6uYKwLyaex4f20O3l2APwjZZorqXRmm6CLu656lP--d0O_P1vyaegREWC5YgdPPU23TAdadg-LtGvQ3ZgKlKh25lEIk8iiyk_M8z-vYfmGF-Xf_wFWJTmbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/479a877651.mp4?token=J89fOySF1TA8b-EkniSOaji8GSDmBulh9CpF-vUnbVevR2smzEEDCCosB8SYFUUOJDtc6F1AkHYM4damKrH0kbSYnEqmiXLGC-PWQOLx6LBqwweOj5bqItbrPgARZjtQfARGAIb8gM9vsMXRANDGIo_yU2D7lR9JtF3ZnUHRHl-IjEh2G0nDRQvGXorKcCfbIkNP18rFdN4XUSr9m5EdMybGPeTFy5Y6uYKwLyaex4f20O3l2APwjZZorqXRmm6CLu656lP--d0O_P1vyaegREWC5YgdPPU23TAdadg-LtGvQ3ZgKlKh25lEIk8iiyk_M8z-vYfmGF-Xf_wFWJTmbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات اليمنية تدك منشأت ارامكو في بقيق</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92983" target="_blank">📅 18:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92982">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUSWUgtyv0II_p7u2vS3LT0jexS8xV9iRnv7bXTkCRdQqtrvPiKjuZGyBrjRhi_HGwA89ShRsGqcGzPBYWn7wrOfwXqNl0mwfX0UBhycPu-48i7Z8UB3-e3GSKwniGufUGGQKwJ8Buy82zBW7y1YJLhxzhdGIQpJjXukHi1_9j-mef1z4GDKvFjWHIOf0C7ucqUYvtYi1V7VJ4DqzO4YI0Jw5M3WxnSf8QBeDKwaPaiMgciLU0KKhShizyVC8ulN2zM_3MXTZXnDikeoIf3LUa-jetEGoKxPj1ijlmTwE9v0CQJxCpJHxv86h4elfxK6Yj304Eu2QThogHCILx8Oxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز مضيق هرمز: ناقلة نفط خام تعرضت للاستهداف بمقذوف أثناء عبورها المضيق.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/92982" target="_blank">📅 18:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92981">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇾🇪
التلفزيون اليمني:
العدو السعودي استهدف بغارتين باص نقل مواطنين ما أسفر عن شهداء وجرحى في طريق شرجب التربة.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/92981" target="_blank">📅 18:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92980">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c545f6ef23.mp4?token=I-eMKoBcWa0ZNA0nvfxDuFnXIdtEsvNBcVyvXnozMI-RrWw1BK4GD7-JAqGhy-gfa0EVKIVNYzWwTyUJa2Yl2AQ1Ytv_830iwlCmGMZ89UahaY6qyPX0ukVc13L2uvEFQGTIC5x9AQv9u5eC9oZpEJRF_7uYmcHhbqeMLWysA1vHqWZuBFPO2zsZN-drkpR1jrXg7bGJJlVizzzk1EyADDWYXJTV0eij3zebpm7DS_8F1O_MzZpuOxknWZxGXSD9vBw6ufJICtfebdNoSGqHiEn4Cy2pPe_0p0Yj_4n-Mk0YzB3SjlIx_alMtxJsE30wxEoNYj2WL_ungdL1QtjpPTeIMR0iyO4e3LSC0lbp039EY13EijIdIdznNQm_-RDWYq_zxxf4IEZDknd8SeLk7216h6_3wd85NrEhl3fN625KJ3C6EifemKWD345t3X12IacgbfBdOjtRPjXcOeir9igjjfFLX8rM3zOJMFsrE4ixGEizcxBXHOf12HcEKzYEbUP78aS386p8edHMc-3jejQ58kmK9cIsMQGPD2nWXYxYYHjkR34baaDfphomYo5xsXTKbDQ-De-CTwHUgq3mUd8Kp6xGJQIUQKFv1lv3GC850d8rUF4aq8POPtnOtX7kP_OCDrVaP8YAf9F_85RZjtLwUSMRZRQDvEhng_EMOeE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c545f6ef23.mp4?token=I-eMKoBcWa0ZNA0nvfxDuFnXIdtEsvNBcVyvXnozMI-RrWw1BK4GD7-JAqGhy-gfa0EVKIVNYzWwTyUJa2Yl2AQ1Ytv_830iwlCmGMZ89UahaY6qyPX0ukVc13L2uvEFQGTIC5x9AQv9u5eC9oZpEJRF_7uYmcHhbqeMLWysA1vHqWZuBFPO2zsZN-drkpR1jrXg7bGJJlVizzzk1EyADDWYXJTV0eij3zebpm7DS_8F1O_MzZpuOxknWZxGXSD9vBw6ufJICtfebdNoSGqHiEn4Cy2pPe_0p0Yj_4n-Mk0YzB3SjlIx_alMtxJsE30wxEoNYj2WL_ungdL1QtjpPTeIMR0iyO4e3LSC0lbp039EY13EijIdIdznNQm_-RDWYq_zxxf4IEZDknd8SeLk7216h6_3wd85NrEhl3fN625KJ3C6EifemKWD345t3X12IacgbfBdOjtRPjXcOeir9igjjfFLX8rM3zOJMFsrE4ixGEizcxBXHOf12HcEKzYEbUP78aS386p8edHMc-3jejQ58kmK9cIsMQGPD2nWXYxYYHjkR34baaDfphomYo5xsXTKbDQ-De-CTwHUgq3mUd8Kp6xGJQIUQKFv1lv3GC850d8rUF4aq8POPtnOtX7kP_OCDrVaP8YAf9F_85RZjtLwUSMRZRQDvEhng_EMOeE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الغاء عشرات الرحلات الجوية المتجهة إلى مطار الرياض بعد استهدافه من قبل القوات المسلحة اليمنية ولم يتبقَّ سوى عدد قليل من الرحلات.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92980" target="_blank">📅 17:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92979">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇾🇪
🇾🇪
السيد عبدالملك الحوثي:
-
بالأمس نصحنا القطري الذي بات يتبني العدوان السعودي على بلدنا سياسيا وإعلاميا، وهذا القدر من المشاركة مشاركة في الظلم على شعبنا
-
نحن بالأمس أشرنا إلى القطري بما فعله به السعودي، ونقول: نذكركم بحقائق أنتم عشتموها في واقعكم بعد مشاركتهم في العدوان على بلدنا مطلع العدوان عندما لم يقدّر لكم ذلك وقام بحملة كبيرة عليكم
-
النظام السعودي عمل على عزل قطر بشكل تام والمقاطعة السياسية والاقتصادية والترهيب العسكري وحرّض الآخرين عليه
-
النظام السعودي له أمل في تغيير النظام في قطر كما آل خليفة في البحرين
-
هل كان للنظام السعودي ما يبرر كل هذا ضد قطر، وأنتم تعرفون أن طموحاته تجاهكم سيئة للغاية إذا حظي بإذن أمريكي
-
قطر عملت إبان الأمير حمد على حل النزاعات إلى درجة الغيظ السعودي منها، والعودة الآن للتبعية للسعودي في السياسات الخارجية تراجع كبير جدا
-
ننصح القطري نصحا أخويا بمراجعة حساباته، وشعبنا في موقف مظلومية ويدافع عن حريته</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/92979" target="_blank">📅 17:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92977">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g2y7NTClO6ddarHJED7KkhxuY2ipAeg_EFjLy3u74SCAm84hbx9s7s2MkyrhdCP0xNjQKjYQRRDuBTyImFJd4a-d_XRmZkqmq-s5V14VGmINrWHxngfPusiwbwfdTm8gu3R4VyfkcyRY-OebILOAERzui6RHDR9sZKTgweyykl39Eyr3EjnmoH6h97hsw9uPS_HrJLWDbkseJGGIlTyP7S-ujZc2_6R-Lh_FS5fZVMrNAyfn6kedGItuiNJfx83jn53OroabKaKhLAKDqLO10w9ZkERmAZ7uTfynMBsSUTcxgBKjPKlVs8KhRKm162gMJnYps2NVkficgjsByMbRXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ibIKt1RERA2ZRKNy2-NMcvvtyqccfVUKGhTtNhg6wV694HhBTyQAJqZFDJ_DInI-foT2_W0icXLpSYM3tnZU3RWYYkNVbsodjwvoZh79e0mFJ6JZVq2GokdBKT8bE4TVR8zrTZ56g6KeO1zMp6bpWOAd2_xA31PdNO6sFlFdbYyCb-qQyn3gmHe0I0eOVW9lxnbrDORGGLU2j17QfxDOtXb2smpV2fMYgYmvuowDioVUEVuK_LKsmYI2Fsn7L53TbR9QrokvukADpMHnlngjmC3azPsMdimlY4CRn4AKhVx8NB5yGOQbdSvD4Qq5dkhGOfNYIkSI29euIS0_rbDlWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇱
قوات الاحتلال الإسرائيلي تسيطر على قرية جبة في وسط منطقة القنيطرة في سوريا بعد تسلل دبابات ومركبات عسكرية.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/92977" target="_blank">📅 17:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92976">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bde9df01ca.mp4?token=IMllopSMuhPicfXyZ876X-X3sRZPu6nRf4ouGk-SDQCxBd8duKd0viv9cV5uyydsDJg7iGT0mNCGMIgt46b2ibQjL4l3I2hXvmuWu9LEhYcUmX_LtVGSgaTLTj4Cq89mcZMHH9wWVFEqewF_WeaMo83rH2981JGUI7pNRlZURTFJc8s9CoAvGqjwdSnBwl7Lh2_U6ldD8VGzyHZa0rFvCxiW2DwPG3bxrVZdJbaA8fEOakR8DexrD24ukeyTLb8oM62vjxAq7Tvn4jem_90NZ6waPHkToOM_RpAVm1FzCwomPgF-T8DBeEP3ceARfK5R74XWINECjaLKbYdfzmh4pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bde9df01ca.mp4?token=IMllopSMuhPicfXyZ876X-X3sRZPu6nRf4ouGk-SDQCxBd8duKd0viv9cV5uyydsDJg7iGT0mNCGMIgt46b2ibQjL4l3I2hXvmuWu9LEhYcUmX_LtVGSgaTLTj4Cq89mcZMHH9wWVFEqewF_WeaMo83rH2981JGUI7pNRlZURTFJc8s9CoAvGqjwdSnBwl7Lh2_U6ldD8VGzyHZa0rFvCxiW2DwPG3bxrVZdJbaA8fEOakR8DexrD24ukeyTLb8oM62vjxAq7Tvn4jem_90NZ6waPHkToOM_RpAVm1FzCwomPgF-T8DBeEP3ceARfK5R74XWINECjaLKbYdfzmh4pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقفة احتجاجية في محافظة البصرة رفضاً لرفع سعر صرف الدولار والمطالبة بالتراجع عن القرار</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/92976" target="_blank">📅 17:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92975">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b86a06f11.mp4?token=tvXLGBr_kBfjWRfLlkzK1MXddOhvU2OjOVwPGFp5p7pdfnVMNreVNwNgX2jjrDPXqK2CCgM8VsRIx5VU5rybEWG7CqRUTynjbLDLe6Z2mXwIiAa9wKSPsuNsuwLmH7q0Df0TBz7ARp35MKcLWQ-9NiIgn9Zt0uH57wdJ8hC1KCji7rVDJAg0iWaP6aY8ZPdXrb7KNEgJETvNW4HkZhKGx1FFsEr4tp2glfA8TdOgmHT20vIpVePhrItlG7pwG1DQvTM0WA1SUkg8mHBaJKqHC5tJ7RlZNOOQxGkQYulcHI8mwevbYFERWzxTw4wto1grysiCO1XSzkqbKsP6Qh7qDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b86a06f11.mp4?token=tvXLGBr_kBfjWRfLlkzK1MXddOhvU2OjOVwPGFp5p7pdfnVMNreVNwNgX2jjrDPXqK2CCgM8VsRIx5VU5rybEWG7CqRUTynjbLDLe6Z2mXwIiAa9wKSPsuNsuwLmH7q0Df0TBz7ARp35MKcLWQ-9NiIgn9Zt0uH57wdJ8hC1KCji7rVDJAg0iWaP6aY8ZPdXrb7KNEgJETvNW4HkZhKGx1FFsEr4tp2glfA8TdOgmHT20vIpVePhrItlG7pwG1DQvTM0WA1SUkg8mHBaJKqHC5tJ7RlZNOOQxGkQYulcHI8mwevbYFERWzxTw4wto1grysiCO1XSzkqbKsP6Qh7qDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة الهجوم اليمني على مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/92975" target="_blank">📅 17:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92974">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fc6292df.mp4?token=EVDmozho_UvBAivqW8OTrHdyOWAp_ZKzgtt--llBCXldvMZR6pkj9d7N0ZiqENLtCLXAZ9jFcjY1eUk-J2S1Lx-UOeYGH8947zjlMM4GYRd25KE3kojJeDeKtkB3pMMaoGAUa6YOCldmJFuyPL_lTL7g55NtZSNvEaL0W9WWmmlrCRkNwy5MECF-NlHoo52R6vmYKq4SNewQ3Rs5_EJ1NYoUz6gAEcAGmb12S26b2UCDepvYghXbk38GPzhcW1srPQ16dgfM6Z-jTiflInqAg8HHjzvd0fKTMgWU-F3VjTzenzUIFGA4RV5dgKcJdQaTxpsgjEz13qReF-ABTsn48Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fc6292df.mp4?token=EVDmozho_UvBAivqW8OTrHdyOWAp_ZKzgtt--llBCXldvMZR6pkj9d7N0ZiqENLtCLXAZ9jFcjY1eUk-J2S1Lx-UOeYGH8947zjlMM4GYRd25KE3kojJeDeKtkB3pMMaoGAUa6YOCldmJFuyPL_lTL7g55NtZSNvEaL0W9WWmmlrCRkNwy5MECF-NlHoo52R6vmYKq4SNewQ3Rs5_EJ1NYoUz6gAEcAGmb12S26b2UCDepvYghXbk38GPzhcW1srPQ16dgfM6Z-jTiflInqAg8HHjzvd0fKTMgWU-F3VjTzenzUIFGA4RV5dgKcJdQaTxpsgjEz13qReF-ABTsn48Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ اليمنية تصول وتجول في سماء السعودية</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/92974" target="_blank">📅 17:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92973">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77c997f9f6.mp4?token=fIKrGSLQPfMTBv7YkZG0STLIBiKYk-6XRxkGcZNtfzDgAplYHodNrJ_9wobT8D2fv0ycXvdy7_woxHcn7waPP2faP3iDdMGtlU_SenZP77hLpqZnGtX8eagidn1HJQaC_mmVCXvbSPmch3e0yhSjHNH40IlSPg1CnZ6LDtyyxXQ-sCwqDLdSBsRtCE28upy0f8pNH5S7rDSPdqyiB3I3zag06vc_CVoZlosnkY0bfbE-hW6kpwlBUVCfX3a7nNlYlH6Nj1uE-3iixsQULdMP64X_1g-txxEA5VyYRBrjNshm_JO6QCDcLhBj7PVWlraMAjCCBUVgsyX-Z0PtsogCDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77c997f9f6.mp4?token=fIKrGSLQPfMTBv7YkZG0STLIBiKYk-6XRxkGcZNtfzDgAplYHodNrJ_9wobT8D2fv0ycXvdy7_woxHcn7waPP2faP3iDdMGtlU_SenZP77hLpqZnGtX8eagidn1HJQaC_mmVCXvbSPmch3e0yhSjHNH40IlSPg1CnZ6LDtyyxXQ-sCwqDLdSBsRtCE28upy0f8pNH5S7rDSPdqyiB3I3zag06vc_CVoZlosnkY0bfbE-hW6kpwlBUVCfX3a7nNlYlH6Nj1uE-3iixsQULdMP64X_1g-txxEA5VyYRBrjNshm_JO6QCDcLhBj7PVWlraMAjCCBUVgsyX-Z0PtsogCDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رصد عشرات الصواريخ اليمنية في سماء السعودية</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/92973" target="_blank">📅 17:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92972">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">السعودية تعلن عن اضرار جسيمة في عدد من المنشأت بسبب "سقوط شظايا".</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/92972" target="_blank">📅 17:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92971">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇱
اعلام العدو:
اصيب جنديان من الجيش الإسرائيلي إصابة خطيرة في حادث عملياتي في جنوب لبنان.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92971" target="_blank">📅 16:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92970">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مطار الرياض الدولي يشير الى الغاء الرحلات:
ننوه للمسافرين بضرورة التواصل مع الناقلات الجوية، والتحقق من حالة الرحلة قبل التوجه إلى المطار</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/92970" target="_blank">📅 16:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92969">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgewXXedLZM_pfjh22uXcN4wwPhT1WA50Us1PJMF4fQ4SpextIVSmen9jYCySvua9rF8xzE0EgoCiCY4vCB_OS9py6h9Uf74tZT_ZbmrbQFkCP2IbIXXZQc4MDQt7qksBKTRDqUMsDzdlMJxsOMJiA7IoMIUvoyuHfb-fVghXmNPf1eQT2y1zxs_j2XwbyuaXZH2wIC0bI_z3-DjIoy7gIxKstgn2aGuYyPeeLug6FKFWMpuS2OgUR1XpIjMuOaeuCxLD7ouluoTcnky1xfpsaT3YxTJ_XWEsmhnOnE0Uio6ZoE146LzMPkuvEs8ybeqJSpHW2sJMKGsK6-_MkeyhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسعاف جوي يتجه الى الرياض لنقل اصابات وقتلى بعد هجوم القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/92969" target="_blank">📅 16:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92968">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5b004cd58.mp4?token=LYe7b8rRKHHYxqqkq5IjOAfchruYs-n0y3QUANzWgcsnhKbnXews-3OgYcPDaOy3Tc_GOvxrTG2DXttWha7lyOwQgPK8t9aYfUQecSQYgGZq3bgXHn8Put-aZ27vaUPzdrPfWAEYA1F9vhoWQTIcY194P-jRcPdY1QD-7BsJKzqpuHp1lzPNXgJbKUhaL8f1q-fGAZ0_HhBDdHP3ioWIghScy7_U-laCy5jOcVFWPpUaV8MLw0XxiNccHqGL9_xtrgKfWHhZS123A3AC-dTE0gCXZxdi9AJVt-7XKPcv4mxbAZx4PfQtP4VYBj9Cw4jKIILYFgki7ganEiEI8WxMq4DB_qEP_mDD3qBjATHSueeB3LT73BOYwblUB_BLbL_K4CA7LzoqowX404vp6qvk8okdeNK9S0qSO4YXgokPJpMT4OqKM1Cdd7NDH0ObezjIeCBV4GGeghMnJjOXUzrtnn1IQoAlaZ2AVrh-3RYcpTJRxFcz2tEUcZNxigbVqtasVZ0rzbOO5s1wiF0wTwiVrVlD_Q9_7YFXmSkWAT7mnURezOj90j-1h4XO03OUjQVD55rZt8QgmsBVPGLkkhb-j5iTkPYRM8_g0UcnVWGo7xKOwxmSTo4s8BB0mqw62BwK1gMQda46xPOqIDH4wL4oIYYLw1lHbdsDn20MBMfiK4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5b004cd58.mp4?token=LYe7b8rRKHHYxqqkq5IjOAfchruYs-n0y3QUANzWgcsnhKbnXews-3OgYcPDaOy3Tc_GOvxrTG2DXttWha7lyOwQgPK8t9aYfUQecSQYgGZq3bgXHn8Put-aZ27vaUPzdrPfWAEYA1F9vhoWQTIcY194P-jRcPdY1QD-7BsJKzqpuHp1lzPNXgJbKUhaL8f1q-fGAZ0_HhBDdHP3ioWIghScy7_U-laCy5jOcVFWPpUaV8MLw0XxiNccHqGL9_xtrgKfWHhZS123A3AC-dTE0gCXZxdi9AJVt-7XKPcv4mxbAZx4PfQtP4VYBj9Cw4jKIILYFgki7ganEiEI8WxMq4DB_qEP_mDD3qBjATHSueeB3LT73BOYwblUB_BLbL_K4CA7LzoqowX404vp6qvk8okdeNK9S0qSO4YXgokPJpMT4OqKM1Cdd7NDH0ObezjIeCBV4GGeghMnJjOXUzrtnn1IQoAlaZ2AVrh-3RYcpTJRxFcz2tEUcZNxigbVqtasVZ0rzbOO5s1wiF0wTwiVrVlD_Q9_7YFXmSkWAT7mnURezOj90j-1h4XO03OUjQVD55rZt8QgmsBVPGLkkhb-j5iTkPYRM8_g0UcnVWGo7xKOwxmSTo4s8BB0mqw62BwK1gMQda46xPOqIDH4wL4oIYYLw1lHbdsDn20MBMfiK4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#ترفيهي
🇺🇸
وزير الخارجية الامريكي ماركو روبيو: لن نخرق أبدًا سيادة أي دولة.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/92968" target="_blank">📅 16:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92966">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VcE3MFEab0eRUYMF1Yc_ELuBNUYF_nTrevCMsfAePb149Og05wLO2BwXS7DYjf53TLYdV6FMrvlrFJRGI9YV3wKuvgeZgVRyfQhOmrVer275ulus8DRGZiE-Xlm-m_IzsTiSmjbHYdUkB-nag1RSPGQjHhGSg8Ojvhs0X2l6lOwX6xX4IHwMzwUbfHzXUTt-cuX71gxjQ8dZiMEOO-m6SZvcOU9-sJ2cHL8AZ_DH30_pzZY64exZETN4s0YdGnaO76ybBv9EboKlBli-VF_zxmqXfz3uKTOFf5yA9nWgdaOa2dVEAXjTHBHUO6BzKhJKT5VBSR8MLw5Tpf32MJ3Ybw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fn2cxOsM7gLH29p9SV-rBesm0ejrsGm8oe2Leewd4uu3eH9EBU1_9m32wktlfgAzSR43RBvxZZqS2rrRGsyS1jKIlxy98BWuvud5-ucnmEbifHsgI2iGKyRijlIEHIjEq4YkOZWdUmjG-Fcbbd90u82J4D2BhBLNPdIWaqtzZSOh2pk3UII57VUqoaXerqMdIW6eNJjeD3dkZb6-ajSzbkiXTJ5Nbm58aCjT4jUYxkhCX3LnYqiUUYVTUfFWJ9j87P88x1AGV5Lyr6N_vcVMY30cq0PPIYjUZfqFxwFXGAZqe0LJnAwMawrGS8oa7IVFz_enxIA0boeWcqs1RQ0jnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">القوات اليمنية تدك منشأت ارامكو في بقيق</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/92966" target="_blank">📅 16:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92965">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">القوات اليمنية تدك منشأت ارامكو في بقيق</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/92965" target="_blank">📅 16:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92964">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
تمكنت قواتنا المسلحة بفضل الله من استهداف مطار الملك خالد في الرياض بصاروخ باليستي ظهر اليوم وقد أصاب هدفه بنجاح وتسبب في حدوث أضرار وتعطيل الحركة الملاحية في المطار.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/92964" target="_blank">📅 16:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92963">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92963" target="_blank">📅 16:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92962">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/92962" target="_blank">📅 16:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92961">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6u_ntK-aX2D4luTByePDjyCmngiUBbmtndPNiWf-M0wUpJZgD7MH8CgVQIJ9VmAPBWtINScgDQUnKKys28Y0bSyplfmhNCMM_Ywz_-veDHkALpqupl53bAU3CAwC9UR7CjwcJtzuM6JOsnHRbddydR-puIheADNObEKhSHhNQN6eo0TPm3fVt9lKAHobM9gSm4iuBjiFfNRXI7VY7q7j22r9feujWbBm8O_inEEw40RTBfeTQM7Ry_-stLJe1EJDQ0s2VZaXYh_3MtUuXNr4l_y1Ag1AG9t6NzRrk7BSBPYeEq6dryhsXth2M1EcoOKuzKeZSGGOMmh6jX3GIA99w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ترفيهي  السعودية تزعم صد هجوم على الرياض</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/92961" target="_blank">📅 16:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92960">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">#
ترفيهي
السعودية تزعم صد هجوم على الرياض</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92960" target="_blank">📅 15:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92959">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9efb2a7c2.mp4?token=eUwJ9hdNIown3wsB4fHCXFEFqR-rI9G5x2J_UnA4WADxvs3lNNu7DT7yoC8tn8AtSdLUh59b1yYACfTjDHAkyUQFW11CCJmsMqPbq7iwYUKgXZaGJe_OC0qdHjtIHODZjcL-cOBM-pPgoPqlCXxiar4v8bn1EOk-gNdY65iqX2yYh_CzL7iVdt6fjELCtT81dj3I7qKuWNh9wB942MG53Gq9D5McngxeCRAUaQqtp3n-JxltVbX_ibXIsixg6WytuqchVGYVsuyDyDmN0r3NERxkJBEAvAxnRdON-1qhTV0aWSHzEZWBZrn7YQsFsEhxZo7dB71B4gnZTCsCAzcTDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9efb2a7c2.mp4?token=eUwJ9hdNIown3wsB4fHCXFEFqR-rI9G5x2J_UnA4WADxvs3lNNu7DT7yoC8tn8AtSdLUh59b1yYACfTjDHAkyUQFW11CCJmsMqPbq7iwYUKgXZaGJe_OC0qdHjtIHODZjcL-cOBM-pPgoPqlCXxiar4v8bn1EOk-gNdY65iqX2yYh_CzL7iVdt6fjELCtT81dj3I7qKuWNh9wB942MG53Gq9D5McngxeCRAUaQqtp3n-JxltVbX_ibXIsixg6WytuqchVGYVsuyDyDmN0r3NERxkJBEAvAxnRdON-1qhTV0aWSHzEZWBZrn7YQsFsEhxZo7dB71B4gnZTCsCAzcTDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تحرر جبل حبشي ومحيطه في تعز بالكامل</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/92959" target="_blank">📅 15:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92958">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇾🇪
🇾🇪
يحيى سريع:
القوات المسلحة اليمنية تحذر جميع الموظفين من الخبراء والمهندسين والعمال في جميع المنشآت النفطية السعودية من التواجد في الأماكن التي تمثل أهدافا لقواتنا حتى لا يعرضوا حياتهم للخطر سواء التي تم استهدافُها من قبل أو غيرها كما تجدد تحذيرها لشركات الملاحة الجوية في المجالات والمطارات والمسافرين والعاملين فيها التي تم الإعلان عنها سابقا.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/92958" target="_blank">📅 15:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92957">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2c7b71acb.mp4?token=HlVRHUBFf0pMTcLvevXgJ6oeJTD2x_dYB9STJ8NZGnQWmz7-eSFzYjf5J95V2K1qekbmN6jbYFaF1RuLHa3gohH43YjJoN_JRFh4zq_QTaW4NYQdfJ-ftR4Dws7QJ45OfmqqF0FvJ2st46MWg61uWl440GT5MPCF7sIMbpXZj4MUbTON_WcU6hGEY6ZpLPzbM9WxtnzVoD8dWbLKmLL2MMEW06NZMbkqQ-r9oXUvUAWVvxVB4-cINP4KcSid4-cRuNGpxkZmcieSe6_36QUkNqb73KRQL37RVYVOVksD81-JM4Ze9XBF6D_okBkotqj6fX3vxtW2c9O_8u5l9NWsBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2c7b71acb.mp4?token=HlVRHUBFf0pMTcLvevXgJ6oeJTD2x_dYB9STJ8NZGnQWmz7-eSFzYjf5J95V2K1qekbmN6jbYFaF1RuLHa3gohH43YjJoN_JRFh4zq_QTaW4NYQdfJ-ftR4Dws7QJ45OfmqqF0FvJ2st46MWg61uWl440GT5MPCF7sIMbpXZj4MUbTON_WcU6hGEY6ZpLPzbM9WxtnzVoD8dWbLKmLL2MMEW06NZMbkqQ-r9oXUvUAWVvxVB4-cINP4KcSid4-cRuNGpxkZmcieSe6_36QUkNqb73KRQL37RVYVOVksD81-JM4Ze9XBF6D_okBkotqj6fX3vxtW2c9O_8u5l9NWsBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة الهجوم اليمني على الرياض</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/92957" target="_blank">📅 15:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92955">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40a3604bca.mp4?token=SLtTAkepSA-3lV9kxdcZaCZ9fcMnDwzxs356HBpThwvhvm1gTp1Nbm2bArob56Pk-HqK3jh7KuoehTbEBq-bQ_hQBOhxSDsECopu4H6M5urT2knR6cXJm6_OpmztWWx7mP76cdeQm1JwGmMTF3C5ZONH7ItLXcHDIy7CRRFTYt_ERO-6LiK6RPU2ZZvtRRwwGE5S9BJeJPDk_KUMARrOhMqQ96jZBqxFo0esT8KDnMeOdCHii39OQRA6xz1grn1ykSlEbR89FpPQKxTysYkJbk1Mtrdihcx9_scfYDwfqIrVcf-V4OsJh3xPU4iTgGm5ZrstxjQLP9lJeVcUdAKLHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40a3604bca.mp4?token=SLtTAkepSA-3lV9kxdcZaCZ9fcMnDwzxs356HBpThwvhvm1gTp1Nbm2bArob56Pk-HqK3jh7KuoehTbEBq-bQ_hQBOhxSDsECopu4H6M5urT2knR6cXJm6_OpmztWWx7mP76cdeQm1JwGmMTF3C5ZONH7ItLXcHDIy7CRRFTYt_ERO-6LiK6RPU2ZZvtRRwwGE5S9BJeJPDk_KUMARrOhMqQ96jZBqxFo0esT8KDnMeOdCHii39OQRA6xz1grn1ykSlEbR89FpPQKxTysYkJbk1Mtrdihcx9_scfYDwfqIrVcf-V4OsJh3xPU4iTgGm5ZrstxjQLP9lJeVcUdAKLHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
لحظة الهجوم اليمني: مقيمين هنود يشاهدون الصاروخ اليمني وهو يتجه لدك مطار ال سعود في الرياض.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92955" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92954">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">لحظة دك مطار الرياض بصواريخ القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/92954" target="_blank">📅 15:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92953">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201a76143b.mp4?token=l_-YnaC-63qmszzfKt_pcwvEJCMgh1R7p4vi36U33WgAeG2jouyv88gopMFgjswOv8bmHrVZlLILVsS-dl2ASdHcyThDFaVxVRINefAjzelUbNmOQXOiCljRD6ND7G0zHc24oW8k0uSUJMS2yI6LBFqZNMjOcCuTQHoGm-Z3IWJO_03Mg2fLe2jSKTPIIYj2BxJr6gOES8wXG59sUua3gGx0xBqQvgE4EgIS080-YYZ008vQKB5GNswYwBv2Ibpl4eGYkh0qg9KxompUUSc6wU-YTGCcqZtsu6ODOO4LvrIkhW1cwLgXEGAtJcXw5vLsPqq7_2u5qMF7Yub8vrNaWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201a76143b.mp4?token=l_-YnaC-63qmszzfKt_pcwvEJCMgh1R7p4vi36U33WgAeG2jouyv88gopMFgjswOv8bmHrVZlLILVsS-dl2ASdHcyThDFaVxVRINefAjzelUbNmOQXOiCljRD6ND7G0zHc24oW8k0uSUJMS2yI6LBFqZNMjOcCuTQHoGm-Z3IWJO_03Mg2fLe2jSKTPIIYj2BxJr6gOES8wXG59sUua3gGx0xBqQvgE4EgIS080-YYZ008vQKB5GNswYwBv2Ibpl4eGYkh0qg9KxompUUSc6wU-YTGCcqZtsu6ODOO4LvrIkhW1cwLgXEGAtJcXw5vLsPqq7_2u5qMF7Yub8vrNaWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مطار الرياض يحترق بعد الهجوم اليماني</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/92953" target="_blank">📅 15:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92952">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9230f8f37d.mp4?token=HK3WvP8D_QlToR9MAuyEPBD5J0t6Tgv97QzKLRmeSKdOybar93jiMb2qBGCVAavAFnMsC2pFrRkU4ka1L_DJ432h82MMhry5MsbahJnMqGbGFFpritumCSljc465WbHZeer3ed1u2ZCvXS4udFS-biEsth0W5T1BwjSa5t5G7fY7bt6xkXwFwrgCvv-O52jKKnGCLzWZliujJ_oUOwawlBrqDzF7Jr8tHBjy25PASs9zmQ3HOexpv38diiSldtIMus_rtuu-sSlvKQ3a-LrNZubBrSrFWXADaprfW4aGQdNuXLVZCSYlaR_6Cb-ZgVDxPhKu-ovjFHAmi81Zb5_76Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9230f8f37d.mp4?token=HK3WvP8D_QlToR9MAuyEPBD5J0t6Tgv97QzKLRmeSKdOybar93jiMb2qBGCVAavAFnMsC2pFrRkU4ka1L_DJ432h82MMhry5MsbahJnMqGbGFFpritumCSljc465WbHZeer3ed1u2ZCvXS4udFS-biEsth0W5T1BwjSa5t5G7fY7bt6xkXwFwrgCvv-O52jKKnGCLzWZliujJ_oUOwawlBrqDzF7Jr8tHBjy25PASs9zmQ3HOexpv38diiSldtIMus_rtuu-sSlvKQ3a-LrNZubBrSrFWXADaprfW4aGQdNuXLVZCSYlaR_6Cb-ZgVDxPhKu-ovjFHAmi81Zb5_76Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/92952" target="_blank">📅 15:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92951">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7009ef3ba7.mp4?token=OTa848wC5wpPpYtxy_r7TnT8xZp4NTnxG1QnikMYcSDMSRJk8kJXRZ0gX1AZjCkvdyp6fIMIyyxi67k74kKTKhV_HZ8pvvnF3UqpkM3qdRcYfKGR3o-ljMOjB3kyhHVJ9mjtVktKHu3yws6TVm2PxTr1cVbL0YHIjKWm6kRIC2e1Yg_Zerztr4SzjeG9b0oSpru3d3pknjfT7D7PNRu-3IGlLE5TR62zFhUKi411_-TCxviUc7Rzu3jThtgfWdgkG_Me9nIA9adQs4TbK-EG6ItluOlgTHA06RC8crPv1jeHd6Pd4kUp7GM7w6zZQLVmjj821uaAQ7XpUkJo4IkKkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7009ef3ba7.mp4?token=OTa848wC5wpPpYtxy_r7TnT8xZp4NTnxG1QnikMYcSDMSRJk8kJXRZ0gX1AZjCkvdyp6fIMIyyxi67k74kKTKhV_HZ8pvvnF3UqpkM3qdRcYfKGR3o-ljMOjB3kyhHVJ9mjtVktKHu3yws6TVm2PxTr1cVbL0YHIjKWm6kRIC2e1Yg_Zerztr4SzjeG9b0oSpru3d3pknjfT7D7PNRu-3IGlLE5TR62zFhUKi411_-TCxviUc7Rzu3jThtgfWdgkG_Me9nIA9adQs4TbK-EG6ItluOlgTHA06RC8crPv1jeHd6Pd4kUp7GM7w6zZQLVmjj821uaAQ7XpUkJo4IkKkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مطار الرياض يحترق</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/92951" target="_blank">📅 15:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92950">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تصاعد اعمدة الدخان من الرياض</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/92950" target="_blank">📅 15:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92949">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">انفجارات تهز الرياض</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/92949" target="_blank">📅 15:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92948">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e4d22faab.mp4?token=eGuWnDBKJ3HIz4dfiRhdBkcHQxrDajFRcPpbS2p6CLFK-JuHzYQimYBUctK-PyGiYZDW_rf7IHrG4kw1qJ8CnQAJ_2BO9T4m_oTNPPyt5gC3Llm68u__cACM80sXJzwxRfpkIoSMZwh43KInEniiCfhFmsTpQItvA432xictILGYmsOSJpIUuavZZOAyvrCVmEcoG6UO26ieAioFh2SgBHCfbcDkWrcRSjMCfzbT2UM_gJeB6w8zGpY8GGTpEbdgsJx6OVRFD_hhLL1aqmRN3q9Xzhvoekzjl_f-4UemLMMaUa9jXvUT01_KAUR3dN5atVaPBuYyrbJihNZgvi8fRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e4d22faab.mp4?token=eGuWnDBKJ3HIz4dfiRhdBkcHQxrDajFRcPpbS2p6CLFK-JuHzYQimYBUctK-PyGiYZDW_rf7IHrG4kw1qJ8CnQAJ_2BO9T4m_oTNPPyt5gC3Llm68u__cACM80sXJzwxRfpkIoSMZwh43KInEniiCfhFmsTpQItvA432xictILGYmsOSJpIUuavZZOAyvrCVmEcoG6UO26ieAioFh2SgBHCfbcDkWrcRSjMCfzbT2UM_gJeB6w8zGpY8GGTpEbdgsJx6OVRFD_hhLL1aqmRN3q9Xzhvoekzjl_f-4UemLMMaUa9jXvUT01_KAUR3dN5atVaPBuYyrbJihNZgvi8fRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/92948" target="_blank">📅 15:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92947">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/92947" target="_blank">📅 15:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92946">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">محافظ البنك المركزي العراقي:
سعر الصرف الجديد ثابت ولا يمكن تغييره أبداً</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/92946" target="_blank">📅 15:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92945">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">الله اكبر
انفجارات عنيفة تهز الرياض الان</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/92945" target="_blank">📅 15:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92944">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmTOocpgn039bJwvmkYdgFZSKrs2nj6HoWMVxAsYPdDcZHerPedgWXb-_vh7iz0T2yem9tswmkNvTLQPYDDw_8qUdeha8cDWlYBsMFkxBzte9qOfhazbteFfUoDGz35q-wfOXb5tA4Plu5GkKLH102k0xIkR2I8PsxcyZ9tsbYaGza5jfVH9AGQdo7LpBbvOjJ-fzUtHEjl3XdWcGoI7JLAQnJ8DTKMwsZTN7axf5nlXJr2sDv46tWZmwASh9jPK5UouSw5czIcRqB7ybYhx7SwTGDsGKLH4CjD-FJEiSrFZP8r18Kmluznn-lpRI0KylMk_oIK_esJB9hIRXNIlhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عدوان سعودي يطال مطار الحديدة اليمني</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/92944" target="_blank">📅 14:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92943">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a46942fb8.mp4?token=AR80KJPP6mKza2l_a74xxSvtNEzphaDWATbFa8bL2r-DzrKuCIQcCqL94ZWYN9Jm1rxpQSXiUOL6d4OFHwAnTnjyYcYCQyXT4EyzEQ5uoF-X1_b9PTuloQTyNfGHGz6rNp31m0IQTYxbhjnk8_-P1kjPX3kfsguuzSgyuFxEmSuOpr7J7DT8_aqZq6nDFruNfHI4KcaIFhjUhEMSLmMrOIEeGBdH7iVd17G4leF78KZzEXASHMEXm_NmmexpWpoEgEhx8_U79i59g-Sy3hedb9LsloJSMycejR20ZX1i4xl5eDWUhMaT0FByZ2YoG03a0aaVDiIvOW-GDTrhxc9vKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a46942fb8.mp4?token=AR80KJPP6mKza2l_a74xxSvtNEzphaDWATbFa8bL2r-DzrKuCIQcCqL94ZWYN9Jm1rxpQSXiUOL6d4OFHwAnTnjyYcYCQyXT4EyzEQ5uoF-X1_b9PTuloQTyNfGHGz6rNp31m0IQTYxbhjnk8_-P1kjPX3kfsguuzSgyuFxEmSuOpr7J7DT8_aqZq6nDFruNfHI4KcaIFhjUhEMSLmMrOIEeGBdH7iVd17G4leF78KZzEXASHMEXm_NmmexpWpoEgEhx8_U79i59g-Sy3hedb9LsloJSMycejR20ZX1i4xl5eDWUhMaT0FByZ2YoG03a0aaVDiIvOW-GDTrhxc9vKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران العدو السعودي يستهدف منازل المواطنين في مدينة اليريم اليمنية</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/92943" target="_blank">📅 14:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92942">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">عدوان سعودي يطال مطار الحديدة اليمني</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/92942" target="_blank">📅 14:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92941">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">﴿كَمْ مِنْ فِئَةٍ قَلِيلَةٍ غَلَبَتْ فِئَةً كَثِيرَةً بِإِذْنِ اللَّهِ وَاللَّهُ مَعَ الصَّابِرِينَ﴾
🔻
معكم امريكا وبريطانيا وباكستان و تركيا واليونان وإيطاليا وألمانيا وفرنسا
🇾🇪
ومعنا الله و بندقية ابو الفضل طومر و الشعب اليمني و الأحرار في العالم .</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/92941" target="_blank">📅 14:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92940">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/92940" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/92940" target="_blank">📅 14:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92939">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇸🇦
🔻
مصدر محلي لنايا   اكثر من ١٠ انفجارات تهز العاصمة السعودية الرياض نتيجة هجمات أنصار الله في اليمن ..</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/92939" target="_blank">📅 14:25 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

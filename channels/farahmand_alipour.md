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
<img src="https://cdn4.telesco.pe/file/G1yguFHtk8vNXSAuAdBmBbfuaN7jTXYnxN1lwvANXL-S5CNCbPqvZOTisKlYgZ393raMwPFicou7xXIsj7CvFI6mDm2hhTAoUZ1A6uC_5IDl1cO-OfMkvKbkXo8Ztm8ei9WZEx39iAbfeVcNDXfKZGEVAk_SwfMSrz207YXNxbo7h91B3xAvxds7owsYdg2xU1cpFUIYyqVSmRrXyvAbKcmuA3d_CsgnoeS0LA5003FDDCevjRR3zu_t4wWWYTnkPpNV1oGaqjF1VI2qDv3XBDtHxJ3UeJLOX8ztiWaN06fK97qruLTjSty2Ku0Q3HISLEyNbh7Y_xD-9q6vJ11b5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 21:30:46</div>
<hr>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=rjByUsw67RfMsN3LvOUQHt00mVKiLy5KvbNz-jgqbV5-fUJRd6UXp4os45E84CwG_1nNvA2dARd0D9MvmrWJsn03UYlb2_0p89U4B_CeUQRvTXHOBQBPi5myK5UmKa2O41X0K-f1a9rDHyjZ0qPK2Jm3YlkAepQM29wAe0hFZhIQu1fCLgZ59r49Z_FiAtAVOQoQz5L959JhVgsQ5LSAROlR0mmDOcC_tdfw_QiZgYQBSgyu960HwIGSSNfIsuM6ZzHuTz_eJoqa70t_WjhSE6UqX2TihsWmm4ptmOR3-0sIKxwfCE8_whpggN-95DMMsEEAnwh99QB3QG1yqKEqWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=rjByUsw67RfMsN3LvOUQHt00mVKiLy5KvbNz-jgqbV5-fUJRd6UXp4os45E84CwG_1nNvA2dARd0D9MvmrWJsn03UYlb2_0p89U4B_CeUQRvTXHOBQBPi5myK5UmKa2O41X0K-f1a9rDHyjZ0qPK2Jm3YlkAepQM29wAe0hFZhIQu1fCLgZ59r49Z_FiAtAVOQoQz5L959JhVgsQ5LSAROlR0mmDOcC_tdfw_QiZgYQBSgyu960HwIGSSNfIsuM6ZzHuTz_eJoqa70t_WjhSE6UqX2TihsWmm4ptmOR3-0sIKxwfCE8_whpggN-95DMMsEEAnwh99QB3QG1yqKEqWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=NVTrVgvvOV3gyxNs7L_Cd6ybazM2sKzDHseO1GAyvbLxD96FhcXXZMUT31UXDucsY9yXRg9LseLy6L8MhY5s4ou2zzQETm-5stPla-uUzeePsLA7H9zl7D3yoWF4x-mUvPf0Lv9ze_5kTKuWRVnef-Om5rW1BvsmSvIedhPOh5yUiKOsUZl15Jw9mhCpl7gyDhoNOGUVWfa9Vrp6SeKXIPsNQU5uSh-ln16jP-KtNogz2GH7wyI8WTMZVrigYCiJeptTO6IwHYq7NB1cGw7fGuh2Lxd3benwamOBX8woVJxqAGJpgr8AeL57qrFDGTBeNem1qJYo9Pb6aMw6DuR7Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=NVTrVgvvOV3gyxNs7L_Cd6ybazM2sKzDHseO1GAyvbLxD96FhcXXZMUT31UXDucsY9yXRg9LseLy6L8MhY5s4ou2zzQETm-5stPla-uUzeePsLA7H9zl7D3yoWF4x-mUvPf0Lv9ze_5kTKuWRVnef-Om5rW1BvsmSvIedhPOh5yUiKOsUZl15Jw9mhCpl7gyDhoNOGUVWfa9Vrp6SeKXIPsNQU5uSh-ln16jP-KtNogz2GH7wyI8WTMZVrigYCiJeptTO6IwHYq7NB1cGw7fGuh2Lxd3benwamOBX8woVJxqAGJpgr8AeL57qrFDGTBeNem1qJYo9Pb6aMw6DuR7Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در میدان انقلاب تهران چه شعاری میدادن؟
نحن جنود الدین و العقیده / لبنان لن نترکها وحیده
ما سربازان دین و عقیده هستیم،
لبنان را تنها نمیگذاریم
(همون لبنانی که سفیر جمهوری اسلامی رو اخراج کرده و میگه این جنگ رو جمهوری اسلامی سر لبنان آوار کرده)
فردا که جنگ بشه میان میگن :
موضوع ایرانه! تجزیه ایرانه! برای خاکه!
رستم تهمتن و آرش و شاپور و…..!</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzvzQg1_t2hbOwZ8E7EaiomDRkRaPDZ04KwNq2whN0IfWA6xUzamD5XD3IGXfPuyfr6mQhy70-gAWJarEskaUpdlLr6Ch5v6aMKgIfFGCMj42oJIjp0N188y9jWuKPYor10CH0hTlXCWBhm38VxIKBqR8m3hyE4BOaJlnysMZPflzSSlmkYeAO7gYPkPwSguimGimPq7NST-GuIs-ZSf__xlgd2KrZVAu-vRnOhc4TYwbSXveBV0-jbppuA-m4I8BqunM89c6n9seNerh_cNL2FDDJQSAC7ccRu0-L5XJPx679vYWRWp7BbNEfw-a7do-ui4xtY7YAcTBlGy4Y3w-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aa1SUO_3erGCcGeODvn4X6O6Nn81h2Q_rsCh_Jvw7YwQ0ashMqAkztc1xj72AxFq4KbJlYzaOiRSj79amKdKk8Cj_iX2SmsY9x8H0QBXbb3b7q4qf4jTU23k31cDJy5W0a9vrV2yNSCWzwYWEki3DMMpOJqdqzgAKdWfCWO5Mn0b0ODDKc0e9qPfgdYw0Hy5WXUUggDFqOLB79KQONtiU7G-drjgqamt-KVKLzKv13H74vnaHeFvKHL90CKxf7PFdfg9g6xFynD96ZLchL_CaDOlnkEHtpiaE5kxixjHoSp8KkdoBD16GTE5vPMCECdaODE2SMYH1NW8v_IoTh_2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etJkcshiWs8rQ-v4V7DNLi15Au2s8gRTO0H8RhSch2JcFzBr0II7u0qw71xaAPTVChTndRR_ueX0zLdLYMso3l9T8nEdB9RiIMj4ekH0PurtxCSJBD5uprqfAUX3xZoJmG1Xx9vGfXoP1CBxCHoy8kfUWKhuK7ns8ccKvtRNYNsjN6Cha1kUuWqvSFatUo1shFBnxk7Vu8uH4GXKnpzTWR_tpqfADg1E4nFiqWUg_z9VHIQq0LL_OiUiSFtIAGFQr2O58rOQrdQMtg42ke7sxbXLrO_v1zxr1cN5Si4n-xX4hxOosQ5WvTp1lQn9P2wmkPOEnMOn347e8ppFoMP0Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،
وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.
منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!
یعنی از زمان هخامنشینیان این بخش
یهودی نشین بود! و ربطی به اسرائیل به عنوان یک کشور جدید نداشت!
دولت اردن نه تنها همه یهودیان رو اخراج کرد
بلکه ۵۸ کنیسه یهودیان رو هم با گذاشتن مین
منفجر کرد! فقط و فقط «یک کنیسه» رو نابود نکرد
که البته غارتش کردن و فضای داخلی اش رو نابود کردن ولی دیوارهای ساختمان سالم ماند!
۲۰ سال بعدش چه اتفاقی افتاد؟؟</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/5265" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWelbRb8XSFqxIrc_vTotVmbN2n4QPda70hcD3dfSHGMOYGKrSyYEzk_9Jws-Hz3Z8dTyNXMJZ0epkxcGZ2BUl5M7uoqV-faeL_O-7wh2WMxFP-dTIl9YGv-qE6BnqsaG4iIFsmxMMjAYTVzWAF07GsxNwiC30S1DzvF37kI2eDW6mS9ZHxErCltbSfdmQFlATje3UiNZQvuYDkPIKQYLWq25A4Zv2q0THv5Bq28Kng9z3KoXg1W_1NJC_oKPu_x2jjjPqAhbA3IHol0N6Was_JzGOIgPQgEvoGtvBmTR4PkZhdVzJUG-N1W0neNf1z2-LA_d13f6gTUVxkxUrD0fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GH68NWPUAfl87xVgUdOTn0HP4e7NotuhIylwY8d1A0BbSa0IHY_Nsuj-vgKIQsq9Gsuqrqt03zGKG-58XMXXePWVLuyRLpLH_K4Sv_WTZF40nRDOOMyf5YENUjmUXLw06f0XQo4yBz3xAseLiZtvhQcEhPjxmp4H0tNMTztUrwMLmO97_N4fj6kLAeD88A46uup82Cx_kXA_V7JulJg5MdOp9YRhsbMkVQ3gZF5tRdwCgq08oUqhB5vApteuwHLiNooIxCQ_AdFk4r9bxaZMW0F54bL31nfttuCg73K1kqy6vBk8TbJjb_KqK8eR951DLfGyLe6CJAOI3pn0qzLGiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJNChKs8UX-xwTz_nykgmipLJes__i3DWZqKtPaGjHicjYxD8SGlHekrG4AOHGSDZw2dwu6jkUBfTpaEzWRQ3goSKY0xQrAkSR5E77xtC-eLnkJlM85mLNYwsHIKh5Anab6mhU3L9OR4XO4C72HIrV3ZLFUgqw0WLc3kYVkCdQU9tL650gY4bepLFtMjmIiDpv81aKhozdAnT6-vWyvBAYKl7sMS1Aknub75YCHAW79ThPE7K-847a1Ut68QcJKFG0lfR3HMUQWfwHp1m5KqGqFrhM4xae5Kew_vttmavqZCLNbgkr6LgoCdyS-XldqrWrgvKxkXuhwy1c3v1-HZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITXA13_oTN4uV2FBVjfUB70-sG8QzriTPbq9LCSgZLFwYU0CfOZSuO99RiCi-KuFbITSgDKcgebqHaR8Ll8wrxloaZTQtvfAewGEQ6yLn5cz1O5Q_uZ_Ol2SBhyRN98JcSR1wttc01Q5LRWB9c2pDmx2nzWcHRO_PlE0GPBUis8rRi3f-CP2Xe6lzw0lx6og8TWqOE7d1HJTWP-dvEhJqa7iT3X_1wnIBAS8lXJx89v6I4W_PKA_hQZnrQSJDDMwRd8mL9SO4sHhFluTFBkDUNjveoFwDTfIAYBLHZ0fKUZQTYX5N5ISAsEAmmM6HuMInR_aTPXdwrzMVyjjLgNNYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=ui1YE3hFK3ltp9ixQdKAkoqUoAUGBFhIwe4hlAi9EK0mhQ6Ri0g-u5k2rP-FNmS2jVZRW2PjZe-icKoT5cxH-bI0cgaZoLflMAM0uH3n0kDyCl6EMdbMYdTWtusO_ONReYI_w08-7omhC_OVdLZfIRS0ehXJ4CbzcNmm3gQCdK5FIfbo3AzdLjAjzXx50w4USEbYkitR0K1F5vCyw1n-pcuVa5S5JS3BqrMra_5khTfNP3CqPlt4RD8RJ6OjNV_t5SV3WR7x-2Go3ZuslPgfnvd72e0LTpHd5YVzcTFEcU4TNZpeGiVCZSChtuaHgWj7T0Xb9G4tl75TYVlq90M0Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=ui1YE3hFK3ltp9ixQdKAkoqUoAUGBFhIwe4hlAi9EK0mhQ6Ri0g-u5k2rP-FNmS2jVZRW2PjZe-icKoT5cxH-bI0cgaZoLflMAM0uH3n0kDyCl6EMdbMYdTWtusO_ONReYI_w08-7omhC_OVdLZfIRS0ehXJ4CbzcNmm3gQCdK5FIfbo3AzdLjAjzXx50w4USEbYkitR0K1F5vCyw1n-pcuVa5S5JS3BqrMra_5khTfNP3CqPlt4RD8RJ6OjNV_t5SV3WR7x-2Go3ZuslPgfnvd72e0LTpHd5YVzcTFEcU4TNZpeGiVCZSChtuaHgWj7T0Xb9G4tl75TYVlq90M0Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5mSTAiHyMaE1tPBs1YQq3Bb9i9HqpRUS9WrC-DXUyBy8dAYmVw1z5hWcZvrel0TiUKf65b-CZemdVdg8mnDPk4YJfV8mamxaZFhKdMlZLbxhulyOdTB-RrTuB0zfhuUc7bDKtqd3JO6eU6cq3zeWpocFUhFV1VaaV7WHgciRoYp9uEDqaiMMuGciOl00WbeE64v3EOzB3aJAV4phy2nm0LV44hHwKEaVmXalXvJ033GWcMXAIAcZrds8BsMOVayrcX1xVfDcIWDwM27J4ItzjFzbR85bhIVt0pNSncZ8mdaRnYCGAo_oPB2dZoI0jCNVXuTp3q46dCeX1Se_Ow2IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OpDXtwlerrqaTW6TweJou17vaR-Y7JbhhRBc52SQKt6ja-BnRMNTYgq-GH0f77ICLA-gtxQNfTqHbRAZMoII25okY-gyMc0omQaJecdRNgc57hwCSUS1oFOl3CxitUQtHy4gN98jMBg31TnU51UzYD860PNJHOEwMCyiCV1bB2BSdG1GVIYyK8BgbmX_CA5g9H_TmLEZpZ8NrL7eYJsrkpBlR_EEFITSIvHEKcx0xE1Wa0NYx3HdRAWKYZCYyFUNangkeomruDGCjLbk1uSsX3mdINFynHZVOW_epm860ROxjcrE7GkxDt06PKYWXQ-aXinTjeKluA5SqGVaBvvi9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UlSCLkafqLOGjA90ur_0xp8S3dpMoUlGeehJgAy-FlRStnfGTxXQ000D_G5zbkUePKkjY51TH7WEpMtGFP7XYOwpZBIPWkz6ifcST1FRnCUG9WAWrCVa7BQKHphzLdSVLX7SQLi7EEhbt6l4TPrrkr4AIxR849keuaAxc4Z8025K2eMQbNTUswxBEJD80cVhQOXfgv9D7HulQ-Aqy3D38c4h98wlIb9eyRZU7hUnS86l_IOu6a4GVyuI4iyxTA5gd_dy95xqM1JumqUWPYCydNLDYBmCOmIB0iEPwP-1BtCK2H4eMM3lGXTQqXxVbUJSiP5Vqv0F169LT421NV9kKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flmsoJJ9lkcp98hsmgYyz1Cq4iH-1gUuYD5eC1-GUdE7_3SvX9P6uLsK5SduEske3uPgzk0fK9Mj6WFhMABIjSiku098T8aKjQColm16Y7UyYwpOS0vwrb9wmgEpxFaECHGS_CfjdOZJyP5uyLPHjzybu9JbU4WRQ6lC2_2PMn1OG0ORP3AhJEVwpKlL35Kza0jMipXb2RddSbbMLpIVw5HS4o0792UhitYBHrgtBLbQU1jqOQtUOJSNLNuRO7GZAfUtFfs7vf_S65OKBLQpcDNqviu2MKRTrp1zGt6qio-MgzZ_a-lgpdKzZHFi1iNWFZdB-3JsNOaOjLPzd_OJcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k1nyaWc_y_tHnytXZe9Xzxfneo6UDlI_VeZBZj42wnDYoVz4UpiPDLXwDqwickG9TfjpYR5vjfgMuSiMUuQBHcekoP41dW59-PnD4nEtaj6Mq4VQF6iOdW7T9785EyODkXtA4Xg7rFVaOLoYXEd8HU3a0F3Pm-X1fbp6ISjKobmZENjTT440azKiL2Hq5j6DOVHabI76HGWSyE7xlura2sU6SkVgb8jK7Ef8rMeW0KssSrI2T2ta3rsihD7SzH4gKrvXxkoy2NPxHq5h8MoFFaejWJRX8javc-mMpxniCl1DAmfI9fjniwY1b1fBCd8w-5WPUtJy1jyssom9NxIvWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XeXxdLrRNMz1usORlDK1iffYbnOKusK1UdrKaKSSacPSKONLcPP676WMgEG8feTQBh3FTTIab4vwfyeBeo4QBwnYlid9-ZrtSKPnIAaCBNd6cYLruyQ3TjvXrK_GE0j1Czdb03xhESpT22Covzbi3CQB1Y47o1jhP8TONk5-gXyB92E7GhqmVJqzpeB4e0wc5QaqYcYeJOl4s97nNZ_lYT8Cq3EKBg7pIfToAnb4-32o7-d4oV-ku1-PQM99_3xWdBHenbKQmsVgqVpPPbrROWxraP64sLY99yiQDEcwproE6AsQqrcLfVIkEgnV7qz-5yOr6lCrfGMg7PRtN9ZDOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhtJ2jYjj_8eiWbstmWo4cDW7WzZoXowYNP5dgg7P5DlDkEDOXVJ0O5M_XltkgtKihGV5pyMU0ATM21n1SybU8g6wz12OHHgMFs7ZqLqbOTwNbVXz7Mh_Tagd4-EP8Gh0Ruo4RtkgyAxuSUODOzw2TL3Q9LYY6TgTF1fPR4AIjWl6OUqcLW-aThKZpbR_NAvKPJR_VS3dvgsT2AZakmqVPBDyg_TDkz5aWSwCJkdnHkgcE8zVisriZ5DMvSfeEDdkHwwdMFLQQDjongX1-BvCVdsk53Lf--5pIW7T9aXRwe0IQZoIDsHCbBVsZdCNPikV_4jjgyxZe5xl1y_Tz7GEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l5ctTG4wQkKzMfWcMvAx5Alf5vkLuGNPFDf-UNYAnDrm_hRTBH1ftSdkah_-c_meAdamc59n96rd9qfu7r4_D06EFI7Gw_EBZkjOkugkdsx3ItsX0f4j51taWlj3uOuk4hrP9WeLXH9wZUObXy0mi6DpbYXp6S57LAcIMyCGmlL04CX-DtyJzUMiqHV7ASI31A3HHfVp4L7UM-KeMN2tK-_dEOwBwM8jnBuj7EJ-rw89e3J6vh95m-gZmnh9nGzfvAgiejmW_EFUDb29BK5sqQpfMvTTtQPdfQj_pubXnx06puYNQ8fqDPq1agzZnMHIbozTG4qnKhIfC1RaFHBnEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">و بعله! خامنه‌ای و پسرهاش
خیلی ساده زیست «بودن»!
فقط در زمان رهبری خامنه‌ای، برای خمینی مقبره‌ای ساخته شد که هیچ کدام
از اهرام فرعون‌های مصر،
حتی فرعون‌های مصر!
به این  هزینه و گرانبهایی ساخته نبودن و نیستن!
این فقط و فقط «یک قلم»! از ولخرجی
اینها از اموال ملت ایران بود!
در کشوری که هزاران مدرسه‌اش توالت نداره!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=k5XMzNxXoKxL5FjSE1ku02JvcZF9GXOO3EukrVWV_7z0qxK-zgbMrGAQuw242-7S6-YbnPE9aU_wKEu6JbWFxP2CHZER6xoincWc6t2hyWN5G-NDNxEH4GAaSiMhI78DDGcwpYhf2zQ0evVX-9_ss-g9PTSe0--Hi1T-81DXCKnd4XhsKnr6CKv-avhga3BQr3r5V0ZCuXYwrPc73Qh8JKOPK9S151A0M7lhyzO72QeaRKCjch1j-vDAHwZ2AboUqPTuDBA4M7wRAsID2HFvMWo_3sHd7bb3a7q-ZkYYzfG-W9lqc7PP_CY6EUIuKAohOJibVPCggfHIqqxd1hIdog7QAeGtqn_rPH6_qXwl1_b38hq3jceC94Ys2DIr6W5vQCb00xiBX6LKNnVEox6z4XY8Qn4w4CUUCcSxfD1hGhNjEtlJFWO0cKs_bZfdEAOg9GdFgI3nPIB0cfnq5M3JVcI4ZHXTe2YDPpoSZ-xw06rFDxC9ltFz48pbu6G6NDbRCGeLSuw7YqCcvsAxuW0YrEnflsW62Lq_0fPXMSaEZRUBY8ses6Q2sk2dr3Pe57ODjSyyqCgobWYJFuDV8nq0wOilRgKA_i5u0i_mv4k1knr9RodhKxnhT0rLGgW2oSMQSiy_rYBlhF6WKSMDITHe-6WykEUTqRYbd-KYVzsKpWk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=k5XMzNxXoKxL5FjSE1ku02JvcZF9GXOO3EukrVWV_7z0qxK-zgbMrGAQuw242-7S6-YbnPE9aU_wKEu6JbWFxP2CHZER6xoincWc6t2hyWN5G-NDNxEH4GAaSiMhI78DDGcwpYhf2zQ0evVX-9_ss-g9PTSe0--Hi1T-81DXCKnd4XhsKnr6CKv-avhga3BQr3r5V0ZCuXYwrPc73Qh8JKOPK9S151A0M7lhyzO72QeaRKCjch1j-vDAHwZ2AboUqPTuDBA4M7wRAsID2HFvMWo_3sHd7bb3a7q-ZkYYzfG-W9lqc7PP_CY6EUIuKAohOJibVPCggfHIqqxd1hIdog7QAeGtqn_rPH6_qXwl1_b38hq3jceC94Ys2DIr6W5vQCb00xiBX6LKNnVEox6z4XY8Qn4w4CUUCcSxfD1hGhNjEtlJFWO0cKs_bZfdEAOg9GdFgI3nPIB0cfnq5M3JVcI4ZHXTe2YDPpoSZ-xw06rFDxC9ltFz48pbu6G6NDbRCGeLSuw7YqCcvsAxuW0YrEnflsW62Lq_0fPXMSaEZRUBY8ses6Q2sk2dr3Pe57ODjSyyqCgobWYJFuDV8nq0wOilRgKA_i5u0i_mv4k1knr9RodhKxnhT0rLGgW2oSMQSiy_rYBlhF6WKSMDITHe-6WykEUTqRYbd-KYVzsKpWk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=Dl-7cMkRTl-QIuVzjTfcH8XjZn4NKvYe_nVvo5gxUNq5iWK1LtJjI_Sa3xUKkyo8zh-5G1oyONUHJeGyWeJ-z_MD68N0ltqbsSNGVDVkokr5x7HCyarZtKPay4iR5rWjL88CHcA_NP_kwgk-TAgXjp-Ai6vBZTdCbXN311n3CB6ldQ7QUla8Z_ojs8KVw-xdSiww5UxKYi8eVs0qIMBrds4rKyYRaA7SyJm7ENDBV9D2jjtlI4_SUiWjI5bUWAiAmrvPaGmI7F3hucwqSBOCxu_c4FzFCIJVbyHzQYlSEjQ-8MEBaXh6SQ_34Xc789CXcUh17w6mhmxoefWDAufeBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=Dl-7cMkRTl-QIuVzjTfcH8XjZn4NKvYe_nVvo5gxUNq5iWK1LtJjI_Sa3xUKkyo8zh-5G1oyONUHJeGyWeJ-z_MD68N0ltqbsSNGVDVkokr5x7HCyarZtKPay4iR5rWjL88CHcA_NP_kwgk-TAgXjp-Ai6vBZTdCbXN311n3CB6ldQ7QUla8Z_ojs8KVw-xdSiww5UxKYi8eVs0qIMBrds4rKyYRaA7SyJm7ENDBV9D2jjtlI4_SUiWjI5bUWAiAmrvPaGmI7F3hucwqSBOCxu_c4FzFCIJVbyHzQYlSEjQ-8MEBaXh6SQ_34Xc789CXcUh17w6mhmxoefWDAufeBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpN6EiadKQPvHB5CtZmWz6p-Fx8ChxmH3a42murIOPcC0tDGv9aIHW5Ix_rmeY9zEKlbjn1v92ZFhDXgTFpDAxwjz9k4HjBGL4oETPlfCxl0KBjVAPB__AowzsEDnTvrrpvJmlkE89tWQ1qbxVkpCMaiMaG_CIVFNMYoIYAzop0XH_2jyIJsKSiayyOZhJ5Rf_XqgUs5kaZpEz2xoFIaHQOsi36avZ4CXjO8v5aEfmNPlNyLd8eYFcjoMRICdnhYiQrycB8EGJDoulMK4pbMU5b0dfs1cakNcSaKvKqhD4Nbcr63_LkF96xKoga9NS7_7EqaGKljct4OenJzShLHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف گفته که اگر حملات اسرائیل
به لبنان ادامه پیدا کنه، در مقابل
اسرائیل خواهند ایستاد
‌ و «زنده باد دفاع از سرزمین مادری»!!
میخوان وارد جنگ بشن
برای دفاع از سرزمین مادری!
حزب‌الله برای چی وارد جنگ با اسرائیل شد؟
برای خونخواهی خامنه‌ای! که
هیچ ربطی به لبنان و سرزمین لبنان نداشت!
اینها فقط برای فرقه خودشون میجنگن!
نه ایران و نه لبنان!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بیانیه سفارت لبنان در واشنگتن در خصوص توافق
بر
سر
آتش‌بس
متقابل
:
حزب‌الله با پیشنهاد آمریکا برای توقف متقابل حملات موافقت کرده است؛ به این صورت که حملات اسرائیل به ضاحیه بیروت متوقف شود و در مقابل، حزب‌الله نیز حمله‌ای علیه اسرائیل انجام ندهد.
اسرائیل به ضاحیه در بیروت حمله نکنه
حزب‌الله به اسرائیل!
یعنی : اسرائیل می‌تونه به حملاتش در جنوب لبنان ادامه بده، اما حزب‌الله نمی‌تونه به اسرائیل حمله کنه !</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
ترامپ :
«من تماس بسیار سازنده‌ای با نتانیاهو داشتم.  هیچ نیروی نظامی به بیروت اعزام نخواهد شد و تمام نیروهایی که در راه بودند، همین حالا بازگردانده شده‌اند. همچنین، از طریق نمایندگان عالی‌رتبه، تماس بسیار خوبی با حزب‌الله داشتم و آن‌ها موافقت کردند که تمام تیراندازی‌ها متوقف شود؛ یعنی نه اسرائیل به آن‌ها حمله خواهد کرد و نه آن‌ها به اسرائیل حمله می‌کنند.»
🔺
ادعاهای ترامپ شبیه برخی ادعاهاش در خصوص ایرانه.
اساسا اسرائیل قصدی برای ارسال نیرو به بیروت نداشت! بلکه نیروهاش در جنوب لبنان هستن!
🔺
دوم : بر اساس قرارداد آتش‌بس اسرائیل قرار بود که به بیروت حمله نکنه! ولی داره حمله میکنه
و در نوشته ترامپ هم اشاره نشده
به حملات هوایی اسرائیل به بیروت!
گفته : نیروی زمینی به سمت بیروت نره و برگشت کرده و…!
گویی ترامپ دست اسرائیل رو باز کرده که به‌ حملات هوایی‌اش به بیروت ادامه بده و به پیشروی‌اش در جنوب لبنان ادامه بده.
همزمان گفته بله من مانع شدن‌ نیروی زمینی ارتش اسرائیل به بیروت بره!
🔺
سوم:  ترامپ گفته با نماینده های حزب‌الله در تماس بوده و… عجیبه! بعیده!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5245" target="_blank">📅 21:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrCqXLaAO33fPZPibyz8wdp2ahn1giDE86m_3XmSFEQch0Qc50_E89VQg93QIWUHmLETe7A4E3-7V6I0ARVykiUpta57RZoidgiIh2k9Nq_LbJZim5KVV6qbo8DslVOEKVyNCC0r8IH9_CwzNHdPfK0MBWsppuVT7lrI8L12eqrDQdZQ6J_2PmgATG8BLTnKAWltiZCfSdZcrPSTzlrSrcvjco8-kg55uNG0prKBzzp-O2xKt00HGbcadioZJB29_h86n8C6TaWr6A-GRs__lR5HIuWITfwflGCR9rsnT7um5wLE8_7NkaazlX3UUuUq5ygMcezNzgx5nPV8a1p8WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJadIQULv9Ki9dtv1cW149bxhRa-861iqmWnaQ-cNBt5UaUHwkLlgLDLUttsyJYk2drfjlsRuNEnG7ELocgRWgRPX9GLlz0ZkofWmYzQj-uZtm9-u6B4AaFxj_ZMzrqfsKZKt1KEXgdvVYwCnm3FqxH4hhhIRJgjsmemdvWvKd9u8xM05x_Qii0t-Y_21UpJlcekBsG-z0CYbUU-TRfgZ8qNzjWDHu8ZuS8ti6CM2by26rZvFOVlFdvnNYTu1_bEv4KxiZhQuA-Muwfqk2H6LIiBKp2nkc4kNRNHePZmOqapeubh1EtIDskSyIVBt7LD0iXiezivbpvIntZTZuPemA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnTsfA0wCY97t4zHLH2GG4Wvvcl3kG85ylLJJzncc1Ycn0Q-W_UQONQOK6JFMMqQMdpDKLN7X_nKiapChj2eSPi1hhsWT3rVaCM5Gjjbfpb6-anPHmDovbEKATcAIR8rOI4V-YJyRAsfvB_1FjWxFFmdbMu3SWGKwCzd0IJuMyf2VGjVq7cmf-xhSNx5FH5d1RnCCr4FI31H0cZATDWUWtvj7dwPainS2xg2XxCLd6_6ucPBqOb-7A334pZWn9g-dYmBE2z_oXpT_MCaS12_6anbgtrWuQ_b8y9ExHCJMIdjx2xsr7a-bbMH-ESlj9ExFQpuNsQdeOFqebZTYtgTMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFGE-NOtuSIxBOHU4KIZiX80fDBsti-Aqo0Gm3SQSitoI5W2HGkZXj_Fs41RUHiO6kFjtdNd5Hnb8Vjcp8mAKdF5-C6l6DUYdwHKP0WJwg6ASU0ATtSg11kSqJYZJhM6yXTyFjKGEmfSq1g9ntghxwUDPkjTIDxQxQ8875jlPuxFQz6IfeTfvmicWQqpXAJ-7xze9r1dp_OFpy5-x_qET_Za8yszBDzJx6fJJVnYvCZb61wvL6YYEu8WcGmJOiXuNT4Tsl-JD_V1yhbjn7H7PDoV08-ycbLS34-ynppentXHQgn7ixjl99AOtKAhjVwOmMY8kiHXgVg0fnRWdx1wZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIMpspnLLTQtcomT1SmUJChNAUcS1D7kRZwGjL3-W-370TXTiq2UpQxSuk9d9MLvwpegvcInQPXXfmZW1k-HHnbe71PZ-wD5q_duw984Sebm1GgBjZGCdfJcvy-DZpw4KCrDhSYcP0mpOpdsnDH1WSomzHT0fit28pXDQpqCXsFW3VyCmTc2qlcy66XbqXFZTEi-0FljYaTFeE_5GdSFSl3prZ8Zy07xJcqY8WeAsOyBxQG_chTcrmrRgmxt_clwUBBSbTSAX-EXJEP2HyepYMWLt07yKgq_C6Yh0oD73fHOu4dC_WIrmBKBojqA36TWPK0qKKCNaIm9uOKBERBLmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9ua2yy2em_r7FJcXrlxUY6iU3MtRhy1BcnY-IdADd0dKxRbiS2kdAg70iB_NJporKaI3S0UrWUNkpqeDThi-QMMwQr0E7BAsL_qbD53non37Kx1ue7Dp4uiyV2LSP7sQjWhVvUb97LAF4ULSCvcc1w5gWhlNyNK_V7BY1-avaAtSLsIwj0S9HYmGdcLr4K141jth9eYdKE6MXhLroeVTQGet4SRepJ80MThJxkJgOaal4IIaB5PTdHJTqrblh1SGCBBpuw8IIHhBKJV6NeogFOLn7eKu-o5JJ3_1zty8V7fDISoJORvhe8b-nBkN27uSVfK0Jee5Fn3Amqk5XklxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو دستور حمله به ضاحیه (بخش شیعه‌نشینِ بیروت) را صادر کرد.
🚨
بلافاصله پس از انتشار بیانیه نتانیاهو، پهپادهای اسرائیلی در ارتفاع پایین بر فراز ضاحیه به پرواز درآمدند و خیابان‌های خروجی این منطقه بند آمد؛ هزاران تن از ساکنان ضاحیه که پس از آتش‌بس نسبی به خانه‌های خود بازگشته بودند، دوباره در حال فرار از منطقه هستند.
🔺
نتانیاهو دیشب نیز در دستوری به ارتش اسرائیل خواستار  عمیق‌تر شدن و گسترده‌تر شدن عملیات زمینی ارتش اسرائیل شده بود.
باید دید واکنش جمهوری اسلامی چه خواهد بود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5236" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lvavz3C0YnoC38jpDYlyP5IHQlAJIouq9xYEiauK_mAfVuapAc9cQW-O3ZMTEhlkq8YgsCn3Dtp27ja6XGesvVtnZjJZ51uSllpm2XHU5XC12DhCLWCPSrQYM25K9yeYWsVika7jc1CcL6kxH4pex1IAFTaARwCUHef_4RW-muJWqmmhfM9FjfUUxvz0R5D6_H5EzOmhEz4TdPGp5OEkjPLkbAw-Sh5TRdq9Vd-noPV90Z0u-TWOVLkOYKFCQD4JYMj29u2eg8yxP-bHiGWP9IZwA9xmQ80kJaD0IrnsVk4gmhqbUW6mA-5TAY2sSEKRL4h-HFb9RwPRLvsjUlQvQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DG_rndxs8Ct5GgMVhYh5Irt2bHwrTHyjoJrgAuAmvrFExAQXpSBBG19gXlbrK4_RSeWVoZU0GzXyinwxWQRAocyblRK9wOuG-ckzu25iXbUTlRstvSJpGEwD9XgamFyzs39NuL_NDsSCQklJuKrdHZNCKl1l7HZal9Qe4Kp8JpNx5W4ARb-xVusdmazQ2SVadtfcPOj4oTX8mWNo22S_HQZj6tkkgpB8tEgmoGbaCZBQSBWgTRWHaU38NGpJ26yLw4VSocNnomPmRxTXQLDLrlNlmjD0ytpSLMzh1Vk9p_OaXHoVkGz-ICmwOANOnpc33esCz3QhVbkaiKNHp54Lvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=E_38Msq4IyZriidBa4n4Zo550aZwzKm2uNvLlrtJuq126zZAZG64p1RocOv5w2hpuO5dbmipfOZs6minfE7CksekegisnXShWPngSZ2nnYEVX0YrptwUtnxxsn1mBrAPMDRefW-U-kSpLzJUXd_GDbhQILIR3SnU_C6j8rkB-GWcEHZgKC7vVfFVWRMluEJS8VWZG_fxMJ07qutAQNWZT2iac7xNHqlKOUZakmLB60Jqdiu7wRbU35OFojrunhl3DsTOXrTggqnjNgY7eDSK5tOMsRhJ0QR5iYw6KHlVlSYOUIBj2lRr6_wig8v_jroEuHGjKAGUL7PAl4HRsptBKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=E_38Msq4IyZriidBa4n4Zo550aZwzKm2uNvLlrtJuq126zZAZG64p1RocOv5w2hpuO5dbmipfOZs6minfE7CksekegisnXShWPngSZ2nnYEVX0YrptwUtnxxsn1mBrAPMDRefW-U-kSpLzJUXd_GDbhQILIR3SnU_C6j8rkB-GWcEHZgKC7vVfFVWRMluEJS8VWZG_fxMJ07qutAQNWZT2iac7xNHqlKOUZakmLB60Jqdiu7wRbU35OFojrunhl3DsTOXrTggqnjNgY7eDSK5tOMsRhJ0QR5iYw6KHlVlSYOUIBj2lRr6_wig8v_jroEuHGjKAGUL7PAl4HRsptBKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bikur8vE8DkDrOQf7pH_7nxEFESi01u30bTzrcEk0HbeeSaz_89BjL7ullnAFcBzzGu08VOATT6QDPnqGg_X4v0HZ6eQP2Y-A0g_t2BP0eohWmalebQOmZ2lRlD2vcBUIBmE5MeGiLHlUdxDVswcplTMwbJ-O0sEFyzsYFXL7Kvy39G1V2mLXy-qdWD5IrMFfjyDeo_lAEescr6XosJDcXFISoawcAasmRNIhr1DmbPtUamdiFom6NggJR7IGKvfHXqFltjSb9D31Q_ZjEgTcVX4pKn4J90ocaBUo0V-FCRo1KZ_pe9KldQ3xoOSZF249mGfByZjwmuiSuVHaZoC1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=UZdN08gDJrxSeEmbzEgUef5QEPYmoWa8tzOR6E3hCugnu3ijST6dOXjG5Bhm2-Ba-HxAy4GnuA58grR9EHAid3bI1e6vbDys4AJm1LuohAP3BFQjLM0W8veLY0NL3x9SrxLDUh85GQCfeQA68c44QpNcQRsNnjWwfDDf_obvASgfYQd3bt-dt0XoKLeWPemqDFeVNdMRCgQgeSK50iQUDTPkfDCYSI26gkPV_psjSGByV-Wo9ytk299tRQDKhb24Y3levKHQx2E5T-yTgqZtk_0zZeSAWVW8JJD4mP8H4GXBDtlZ9ZQBHo6v2hXbafaEwZcSEsMyuQ4-n-oDLL9vcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=UZdN08gDJrxSeEmbzEgUef5QEPYmoWa8tzOR6E3hCugnu3ijST6dOXjG5Bhm2-Ba-HxAy4GnuA58grR9EHAid3bI1e6vbDys4AJm1LuohAP3BFQjLM0W8veLY0NL3x9SrxLDUh85GQCfeQA68c44QpNcQRsNnjWwfDDf_obvASgfYQd3bt-dt0XoKLeWPemqDFeVNdMRCgQgeSK50iQUDTPkfDCYSI26gkPV_psjSGByV-Wo9ytk299tRQDKhb24Y3levKHQx2E5T-yTgqZtk_0zZeSAWVW8JJD4mP8H4GXBDtlZ9ZQBHo6v2hXbafaEwZcSEsMyuQ4-n-oDLL9vcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=DMtfA6fdarmWRWhuEr2LX6SYWz8hcJaCiPKL1rE07Y5FOJUdMD2_22kuIG4JCKAu60YvrtWf18kXBvRQr9jvPN3yq22tfqUzfu73UGHX6HpNInaJauxXO4KgdK9u8RK3R6Ea33oWCvPgR2CT8MD3P2AeIrgGyOjUNSqujLYqoRctHiLO9p7mT03GkrrccGYt8XOUVlxpgAyAaK0T9DU1yFK-Ln56lulT1cEokGEwjAGEYGq1uoY34ImLKn3c7BrEm5N4twEGWd49gyKU9G2tD2wleE5h5Hb5_oo6PEs7R7p_J9LTHN4I2QlfnOCZeV4ui8tz1cCF6nxkksblJxRbqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=DMtfA6fdarmWRWhuEr2LX6SYWz8hcJaCiPKL1rE07Y5FOJUdMD2_22kuIG4JCKAu60YvrtWf18kXBvRQr9jvPN3yq22tfqUzfu73UGHX6HpNInaJauxXO4KgdK9u8RK3R6Ea33oWCvPgR2CT8MD3P2AeIrgGyOjUNSqujLYqoRctHiLO9p7mT03GkrrccGYt8XOUVlxpgAyAaK0T9DU1yFK-Ln56lulT1cEokGEwjAGEYGq1uoY34ImLKn3c7BrEm5N4twEGWd49gyKU9G2tD2wleE5h5Hb5_oo6PEs7R7p_J9LTHN4I2QlfnOCZeV4ui8tz1cCF6nxkksblJxRbqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbKn2XXWmzL2VW8rWUOV9DEfy-5NO0APxJwK5VuqFjMG6_ppDDH5ovsgB5d8pgxKkzBEVlJnvQvsvUNs189M1-pKIUPEzlVmtJdKs5S8o800uCoJESXgEFTTyudj9JwZXXhnTLzYNqnL9w0cxkAfNaLmRNMPlJ_i5ZgIik6beKGiNSGsgQSVVulgpVyBoMwMYvqgEzAEtcepup1KGbJuR7krQe5zQSUh9uIfFdtMjK4RsWWxcFvSUYfxPtEQWr8crAZvbSMGiJNpN4LJ5ST7eZVPcMxkahqmSHVsTQJ5S3xNLlwCe9MNN4Ks2YOwC2qo5O248iB8jG2CD6gDjsxcSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما
از دولت لبنان خواسته بودن
که برای آتش‌بس، مذاکره نکنه و…..!
به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره
(که بعد بگن دیدید، همون کشوری که به ما پول و اسلحه و….. میده، آتش‌بس رو هم آورد؟)
ولی الان می‌بینن جمهوری اسلامی توان چنین کاری رو نداره!
ترامپ اساسا داره لفتش میده و سرزمین‌های تحت کنترل حزب‌الله هم داره می‌افته دست اسرائیل پ یک میلیون نفرشون هم آواره شدن!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5227" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=h-bHKyh5-HacWczmXHhQyrHmfaUSTev9HSIrgcv6aYpGRhRU1b2sO8nZbEw6BsiFbwhqA-P4HqMP_lp2zJhkIiuEN0wwq9LEEzyuLSfAkB4agmcDBV2zHLMRUVb1UGvkR4GxHG54jzlf6dzatK-GqCtlBFtxrLvg1ppYRqiYY-1eGtCaMsF86I3v7etX9Lu2NPmTgVx3PapJXezLTMNAJTLTxy38v4Ky_shzP7-Mwq6e4tYH4DCuwCsLFcGwhKK4-mJU8nfpcsPDZEnZVq6pZdLiRxhkXmhHh26fKtQ8EsE71si4u586dCawQm-S3kGXAkcCkwYXWJtdW3w-ahrMfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=h-bHKyh5-HacWczmXHhQyrHmfaUSTev9HSIrgcv6aYpGRhRU1b2sO8nZbEw6BsiFbwhqA-P4HqMP_lp2zJhkIiuEN0wwq9LEEzyuLSfAkB4agmcDBV2zHLMRUVb1UGvkR4GxHG54jzlf6dzatK-GqCtlBFtxrLvg1ppYRqiYY-1eGtCaMsF86I3v7etX9Lu2NPmTgVx3PapJXezLTMNAJTLTxy38v4Ky_shzP7-Mwq6e4tYH4DCuwCsLFcGwhKK4-mJU8nfpcsPDZEnZVq6pZdLiRxhkXmhHh26fKtQ8EsE71si4u586dCawQm-S3kGXAkcCkwYXWJtdW3w-ahrMfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.
به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.،
مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!
یا شهر‌ نجف!
برخی از شهرها را اساسا به صورت شهرهای پادگانی عربی در وسط مناطق فارسی زبان و ایرانی ساختند،
پادگان شهرهایی چون : بصره و کوفه!
در قم اینقدر عرب ساکن کردند (از قبایل یمنی اشعری و از کوفه)  که برای چند قرن یک شهر با هویت عربی بود!
اصفهان اغلب یهودی بودند، یک شهر تجاری، عربها حتی بهش میگفتن دارالیهود
عربها شهر «جی» رو کنارش ساختند و اعراب رو ساکن اون کردن. تا نیمی از منطقه شهری اصفهان عرب باشه.
نیمی از قزوین، محلات عربی بود.
این حجم از استقرار قبایل عرب در قم، مرو، قزوین، اصفهان و… اغلب به خاطر قیام مردم در این شهرها علیه حکومت عربها و مسلمین بود. قیام های قم بسیار معروفه، اما اینقدر عرب ساکن قم کردند. که شهر برای قرن‌ها هویت عربی گرفت!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkwvwJkAtTwD8nCVlFn96U0K9hWhyucTtFOoBS64N4PJDwT8o2r11JjrXH8V0HODJ6OK7NychT_l8F9SE8no_cgHRsM-8wminOzKdDSsYE-YUVhuKOpfcHb_ruTu_dCQ5VJgz8T5farnU6R6BqJVPOzkZbqwdQq0szueNHxoDQmXiq640kRBbCgYSeTeMjcbDhajgWxI4lqO-hGfYapKbHd8moqCOZUBxHiejBe0HpXzsp8Q5PTItBKl1QJ5qOymj0hSZZfeC5NvMA17OzleRNk3geoHyXASpirEo2td3ddZBvucfBMWnerEPiC-Ez0Kmn_FpaCVFAHKZ_2Hm_NP3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqEE9gB_A19dxNTR44jegY_aH23SdBEqqmc_YAmrdsqBw_-BLF--oTHArDF6jTzteVNgloKwwWMaeZGwF1AE6hwTecfgr4tOEgRLCkqIKK_2ZYTE1HnO6PQXCxOyANvnng7WY8huBOyVBLNf-f-VRLjV1R0aVLxxLklR1Hury-yT4CJfBQqNJDV4nxrGX54_Bz2YCZQ4-dxHNTqeKDNyQAvRJL96RniMyi1cMxC38rIhKx6pW-HkHAM-7C94RsF4bYDaJvtW-HcnoKPCqDxaVCDJ6mmwdUJdAsf-hMWcVorW7i1jBUY2GZSJjFAEeRl_jCiw5Uuj4Pc399Q-ZtP_Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_U1pHnZfMv9WRzviiPCrE-n03-yDtACRK3iUjvUFFHcCq3nanEFbyyu8W-9RT_uAtNYegFH6MZRx_kn6sMmxfaiwgWHY0Bo5TRyrKnkYttUQp3hfC-ppeP1bW-yhIAgnJ5LA3AaqbzPtVfnkH-ZZ3lhvajeBxHUCu5t0AfOQfRgZMaWfvborERKSRweTIjl2nla6x8fiZKs7SLwSg504EbG5pMpUMXN1B-nFapE0l0AR4UMNzFkZ-zlJhfm4MJHcrPsPgcise3YeDkZn91MoweLvfuQS6ce95i-ocr8pdmkVlc3XdyUREBtyb9mPp34_zJNEBywntpgmM9wqPi1HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tABSfvlgB6XM7JznP3hdTaqmH4jjYV7MBi2_HYRBbu81gQ1YtJsVnJFw5OWf77dQ0Iq6FoR-vgSqM04JCeFjLRMF_8dfVK9vXorj61ny3aM4UBoZbeVhnh02y--Q7B5SkO_LfZXKWukP9jRxwHxHMzXoDzHHJD42LtiolzEKi2w-ek2L72xTb59vK1idSfFQ5tFhBmjUqGLr0XtYin4R3ADVJPAS9tgdJMwkkoUYFmVIaPn8B1VIaX6X5m4RiQZvq4lU7_IcgtF9vhYUu8KfbeltJCBqXzEmDP1Dd4mBNqG-dV44FrAYI8FS8ea9F8uY0GOJ2o9-3uecw9FcnlglxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DoEcuoVhVhBGtI3BLgcngiTmBUSweBx8Nh7Qo_7LJwImZnjv6_oWbXXHI_lsGDfcpJryjeaGoOwPAFSmy_uh6_2ITQQORRNSKEa34qyfg8uity6qoDzzUI78cWoqs1wHPleRlM80ys8hmkz56VkcTt3xXQxaE7jgt1WMiJL-Pg44dtKkS2sTjaqAvoSrJbvrbzo-elZn7pKJAcQliaJANdTTCiWLDvImkTwABAgy513zvh1eo6q1coHuDJ8QscLu3JtYrKeBNbIMUupiuMdF1vUMq7OlGB3tB304KiJhEaI3d_Ffskz7yPKGHxpa5spUY2ZweHrDyM33d6EnLFraAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتون رفته میخواستید برید
پشت سر خامنه‌ای در قدس نماز بخونید؟
که شما تاریخ خوندید نه؟
تاریخ جمال عبدالناصر و صدام و قذافی و بشار اسد رو لابد خونده بودید
که همین هوس‌ها رو داشتن!!!
و به همین نتایج هم رسیدن!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5219" target="_blank">📅 18:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5216">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-iEXfT8gnX-G35dA915PpOR-q_LAD-_M1LQc7qqMSRj2y8bFxWKDPedQf0bg7JbhH0URa3IycDII1WKkJTQ3KEjNy_-29wqqqzq4f1HJBlPb6YDxw7QyBiF-y0Zqw7u6iHF3NASERV5VX74Dl9uH-y6XnO5HBcvYcAU29TVhlS03hDCvjABch31NG5bBxwULPadS445fNW2ck7l-QGZsZTUzQi0Xj46JUkJa_nQSD19QM32g9k5MzbnedMoXnI0oZVukX6O_d-it0J5OUTNBCXWBh6stPZw4LjaZPejhiKPuwf7W68UJchQqQvkQiXd3fx-N6iyBRAf9Ggwy0IOeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F-oKI3Vnc2lBkcSHoJvne1krCEnxh8pmHzN8sbPiksShqW_pCqy54SwXXRwQ2RTRv19v8Gc7WnNAzvsjZrbQzEmsYMJd5msJa8GUEYryqaHvsa37PMrLxeou9VmX_l9GpQglfj2e1zKAmlHp5ejjVSIfmr7VfTk6wfp3i5volXYSK8hvoPmZvYCqdpqC4sCpaSewxX6f8Zog5AHAwdJAZ8btmqJ1d-vNY2yQco6jmC_mxGVzCfvoPLr6NdM7T7f0hHmfUcWJoVgQ0HjI19nmGiZWXOkaV87GXe6pwYkAxGOEzorJR6P5-msbl7NBLeq1yxt7ydhAdnVm_BPf_nraKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hGA59_xciXdEpyWzj-2xCQeH_rMEzZdM1ufRF0hevp5keanyyVzvRSCpSkOs26SslTUypd30rzGRGKPTYndshaSvk7BcWMoiGgUEWHBCNxgI7D_FnFoUT9NSNsneeGtoUfk4YMqegSs--er_uIICjeCxYO4Cly-l3Vm31kZQ-zUge0n6lmBHt1Hj2iigHavdfMNBVntLSYpicN5Ad7GO1DUyguFTScdhWD8z8-vChXxMBzCrZG6A9Yd6LLz1997BbGN7hoF-G1P_ZU7Ak6N8qa2nqhcQPZk5QgX2zAtmmTjBnZqP6GstaTVV8MEINoBkZoUZjQ0I8PMNGlTYn0_YSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=RbRh5AYDs1ru3vfQSnf19m6wHk9h6X87KrUtkMLYPgIDeEpxaaGzLrqHv3-VPRDFEC1P5j4tLpPawD3p5qkP_DvKvfrfX2YIKxxJFYz013L4lw5XAY35rbGlBDoVbu_EA4ivufvN2xq0vGFcdqsh7vbbPErQII4QnHBfyFs_BwuuhqkXAHJjPjXKySfKKuzB7Ut1eMnADFUpkjUCZ-1lVNrz_BzokOK8ydiDv4_LvjWUfjiadzjqUdd2lcK-gNTrXu9h9didhLzi8fy4n-S-TO6sUzt636EGUWjrsQPjr7jVPo6cnBgaXyi-O1zfKpgLOFxFiqxe8pbQgIIQjJ-LLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=RbRh5AYDs1ru3vfQSnf19m6wHk9h6X87KrUtkMLYPgIDeEpxaaGzLrqHv3-VPRDFEC1P5j4tLpPawD3p5qkP_DvKvfrfX2YIKxxJFYz013L4lw5XAY35rbGlBDoVbu_EA4ivufvN2xq0vGFcdqsh7vbbPErQII4QnHBfyFs_BwuuhqkXAHJjPjXKySfKKuzB7Ut1eMnADFUpkjUCZ-1lVNrz_BzokOK8ydiDv4_LvjWUfjiadzjqUdd2lcK-gNTrXu9h9didhLzi8fy4n-S-TO6sUzt636EGUWjrsQPjr7jVPo6cnBgaXyi-O1zfKpgLOFxFiqxe8pbQgIIQjJ-LLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=SnH7vO9Efko2mfEMqq8sjw6UQyQunMfiObl009llFmNGb0cXzUa0R-gkIPXXVlpnrgKMrZbeIVo790_GMu4wt6rIQ6rvvbI77fIYzG4MomGlH2trs4iTnr7HR_M5W2uVY7osZoXoPYz0PNpDn1JczyDjcMV6vw13UP_u5qfnjNbvsZcYIf5r__UqYiZfF8V01qyFUxZHcV00wXImhtkcGNyPFZ4lJnSBHeBZLWQ8k09sMDkwOaAr57Xyd3NROLIHxA8SoXU9622F3rrm3o9vwxwC9kPlLMgIk3ym-jgR1fDzjK9x8b88Zv1WlgNJ1taJNQuzkckw8v1m1q5hU8FywQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=SnH7vO9Efko2mfEMqq8sjw6UQyQunMfiObl009llFmNGb0cXzUa0R-gkIPXXVlpnrgKMrZbeIVo790_GMu4wt6rIQ6rvvbI77fIYzG4MomGlH2trs4iTnr7HR_M5W2uVY7osZoXoPYz0PNpDn1JczyDjcMV6vw13UP_u5qfnjNbvsZcYIf5r__UqYiZfF8V01qyFUxZHcV00wXImhtkcGNyPFZ4lJnSBHeBZLWQ8k09sMDkwOaAr57Xyd3NROLIHxA8SoXU9622F3rrm3o9vwxwC9kPlLMgIk3ym-jgR1fDzjK9x8b88Zv1WlgNJ1taJNQuzkckw8v1m1q5hU8FywQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=myBbyhZns-IiJ6Qzf4eqqgJHMfyWjj7ojydan-fHSjxA0st141EPrY7MQAbFuhJ1SFfpdxksZvFoscxOYROr-Cxxm3mhETTdYw74RqrQTHryDPF9NEX5Tt2BBjJ7TuKqLNl3S2kumUS3MRBWdndppyGM1msLOm6jGLtt_Vp9jI77vP1p0o0x7GCvSmYgluX65YhAkAyDvi9prd7iw_RoLgixyQ6TFgLJpteCso-mPdk01-F1yL92eouynFxhHhmzK348TfrZGprx1HCUcbhyg6xEpFC7ZhLIAE3SgLTSyc4jLGEKQ9ldEEjSRSALoPbNwypcqFkczA2cu-r4QZbNXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=myBbyhZns-IiJ6Qzf4eqqgJHMfyWjj7ojydan-fHSjxA0st141EPrY7MQAbFuhJ1SFfpdxksZvFoscxOYROr-Cxxm3mhETTdYw74RqrQTHryDPF9NEX5Tt2BBjJ7TuKqLNl3S2kumUS3MRBWdndppyGM1msLOm6jGLtt_Vp9jI77vP1p0o0x7GCvSmYgluX65YhAkAyDvi9prd7iw_RoLgixyQ6TFgLJpteCso-mPdk01-F1yL92eouynFxhHhmzK348TfrZGprx1HCUcbhyg6xEpFC7ZhLIAE3SgLTSyc4jLGEKQ9ldEEjSRSALoPbNwypcqFkczA2cu-r4QZbNXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbAo2KNeLz32zQBNnl7GfYisIR5UBUG5z2-I9Q9J43h64Y_Uo0aL_uF0IUvCY3sBvCVS9n-Lwxk9_2qVSRJ3yomPM4aGsQ7ERJT15LXZS5qRO3wAz6vYLFt82hQhXy_6wtudKX0Zu4hHfrhovk7b8LOyzQuNbqKW_0WglHXwwXD81leOY5zbCWbQLM7eMqUDpNObyAb-i5YYVRxrM3e0GpCMaXsB9O2Rxo1wo0SFBP9L-5bMiUVIXRY9acOH2Gegvw19z0XSZvJf3X3QfYv0P_se4DvqIQWUtWlZVMlL9e1j8K8yGBP7mbEJ8e3-xzAgiadETVSnZ28AauFkPrfWWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات و دعوا سر اینهاست!
خوش به حال آخوند که چون شمایانی رو داره! هر بلایی که سرتون ببره، آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی و کره‌شمالی رو نمی‌رفتید! راه
صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5212" target="_blank">📅 17:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZIyAgKfR5w1lpPerwcndNCe1STu_PTTV7fqHUsKaCv0JFz1sVGx-9cTQT8bTAjucTxRKaW53iCn9r8FsUQne3J_fymyAjDgpreplGsoINbPFLg0KRqJwL1Ryp5qwcKJO5DUR9D-QpssP3HF_QW33432NjnwKNFIIXR5uz1PxXH-8VsdZhEDaUDFmwbNMnRk4Dwae8pQ5mmeGkuh0tt0dhURfhdstD4H3Po15frq_WxXR3fCAoTRMh8QmuDtSqdJMxHBnrRsoZlMjxiZSkgjRNXplu-8y-hjg_AKFEni7xooHKC5QpLTeRdtnFWjm7k63nDBxnxUMfqa_6bKMU0J0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ  ۴۰ روزه به خاطر ایران اینترنشال بود و‌ دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های
ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های
جمهوری اسلامی  و ۴۷ سال آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات
هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات سر اینهاست!
خوش به حال  آخوند که چون شمایانی رو داره!
هر بلایی که سرتون ببره،
آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی
و کره شمالی رو نمی‌رفتید! راه صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5211" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZR_IhifOJSHsQ9IL8mC4vl3nD-rL1hvLA9Yg7cJ-YaUBCPew2gXsehCzVaqx67zSMPtKLkx8lK9GOPPkH8i4LRmPhtMQ7nXcfvCseCAbCk54dbNCI8virsjN2gH0jU2juGXSoUvd_Sq22TwCsnRPxA7pwZRX9rr4ERdgJgriWxA7bTkjxMIW6lwr2SmZoVVqYN5pBN8zAFtC02omVpOw4f9aYMJbL9p-glxJHuvncW28qrJxvl9fAqT7BIqWU9VRl7qWVCiIo5tWkVoWFQ038kMxx8WF1fTZyO-19f9szXL5rvk14UmnIQvy9peqEK2qM6o8ECTyDWMtXRg7XKFReA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUQruxBuHOHbnTjFPvZpE1YM-TkifqqP-r6gpQFyfCtcFpbICagdTNK688vSY1gn5dOZYLDVkba_VAZa_IaUDNrlNHdZlStNHdOqHcrB6O3u90_a9aW_K4pb19RxCJXp4LZEVC6cOVwfDkYct6wOnAteF6J0ly4zhR6FxKCLG_KQmoXbJzF0Q0VoIJvqvKoV0mg8b37Ks_MGbMqZ9hCVwlH5Gj9Rs4Z3ZsSAuNV3-i1Aoe7ZvzXy4pAzZd-mhiHZpOX60J1GmJAWgKp1dvfWhvgG7JlPGQATihv6zYp0A1gNyi2Qmq_7XqOZAcDueGZE1rvchC3lZS84ssSEz4KK-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=hkrUI80eNHkXCHOxAK13HX62LCSZs8VRxybmj-SvkMB3UdBcE3eHcbSrCfbUHgjTPsXpBUDgDfhGTU9RtsQm9OMTvfm8byGF25Sy_Pz8KatY-89fxikOeAeyLCaqbTAegfhikY1Msitco7H3UIMN_g3jUdhFMcCnHseG2Jglo8ysIagvfa6cfWe3-_My6FqX_kVU3lVqdB48lKguV6ZQDtM8OLAJYAkNWvJKmAjT6REXDCllXgJg6QQNiWArrLzYBBTKB_l74BMmA0Pi2GEV1j-VFKb7C6ThVtAgA3i4Kvxsl4J_8E8s5k121bK8U4TYRTC8tApIGtC38D67OXuj3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=hkrUI80eNHkXCHOxAK13HX62LCSZs8VRxybmj-SvkMB3UdBcE3eHcbSrCfbUHgjTPsXpBUDgDfhGTU9RtsQm9OMTvfm8byGF25Sy_Pz8KatY-89fxikOeAeyLCaqbTAegfhikY1Msitco7H3UIMN_g3jUdhFMcCnHseG2Jglo8ysIagvfa6cfWe3-_My6FqX_kVU3lVqdB48lKguV6ZQDtM8OLAJYAkNWvJKmAjT6REXDCllXgJg6QQNiWArrLzYBBTKB_l74BMmA0Pi2GEV1j-VFKb7C6ThVtAgA3i4Kvxsl4J_8E8s5k121bK8U4TYRTC8tApIGtC38D67OXuj3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=eRPZQrGxyjsaspm3J7N9Jo9z3NHjDBKqz0jQgjAZ1D5yW9moG1fS8fpThpl2XUFMGuTDYGnXFdwGgoBBgJybrKB7eyV0t04zQJIxqTNQfqJm6u8Rjvgf8DW4MPOfcj3KQsVNVD8zCIgji40fzESPFsWaQyHaNiZkI2-e_SooE4ZT6VxTVInqccEh2qLuXl9rY-4ameFNdzErLDcnFWfvmKCtKgkTUxQLtro2ul2ilPxzEROqZ-Zx4vBmbgZHRJ3mCD9EtWiqPMHTyGheDk-JGgXhx4NAVbcYzMm6ZLq6zWK4yENastRC42sOtlpnDegkYEd5DqVclvi77WLRug-mlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=eRPZQrGxyjsaspm3J7N9Jo9z3NHjDBKqz0jQgjAZ1D5yW9moG1fS8fpThpl2XUFMGuTDYGnXFdwGgoBBgJybrKB7eyV0t04zQJIxqTNQfqJm6u8Rjvgf8DW4MPOfcj3KQsVNVD8zCIgji40fzESPFsWaQyHaNiZkI2-e_SooE4ZT6VxTVInqccEh2qLuXl9rY-4ameFNdzErLDcnFWfvmKCtKgkTUxQLtro2ul2ilPxzEROqZ-Zx4vBmbgZHRJ3mCD9EtWiqPMHTyGheDk-JGgXhx4NAVbcYzMm6ZLq6zWK4yENastRC42sOtlpnDegkYEd5DqVclvi77WLRug-mlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2I2t0hZqfj5gI4f6-st581IMzhGydgboVbSOGdLtckatw9geXxB_8hc2DA_7fFWgcpn884Dci_qrXMnwNrBclKSTPANvC62_Hsa-NPPPHbWKZ7IJFoV1r9LtxYdps975p-2QPutcldytZfQ8IPYoKbeDZwZCC6mA9h9wiSBmNFJgTWgr-uBjj-MbiQrXyRGxF85fBMZfYaHWcyd6g0aDQX0MvH8Gmw3vBl7u7m1BLxBraYOGU4lrfvXMOgjJ1hLBnJpDJQrfsoiYLJOm4Us3i-MbvTlY6Fha68siQjZld3YDXrwPmY4p-4ox-KZLkUIsTj3Fz746hFfsAsJtRzKdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی با آب و تاب می‌گفت
به امارات حمله موشکی و پهپادی کرده،
حملاتی که ۹۵ درصدشون توسط
سیستم دفاعی امارات خنثی میشدن!
اما امارات در عوض پنهانی با جنگنده‌هاش
حمله می‌کرد و جمهوری اسلامی هیچ سیستم تدافعی نداشت!
یعنی اگه به ایران ۱۰۰ جنگنده، یا ۱۰۰ موشک حمله می‌کرد، میشه با اطمینان گفت ۹۹٪ ماموریتشون
رو انجام میدادن و اهدافشون رو میزدن!
کما اینکه اسرائیل ۸۵۰۰ سورتی پرواز در آسمان ایران انجام داد حتی یک هواپیماش آسیبی ندید.
آمریکا هم ۱۳ هزار سورتی پرواز انجام داد.
آمریکا همچنین ۱۰۰۰ موشک تاهاماک به ایران شلیک کرد، جمهوری اسلامی قادر نبود حتی جلوی یکی از اونها رو بگیره! یک در هزار رو هم‌ نتونست!
جنگ با امارات رو جمهوری اسلامی کلید زد
و هنوز هم کامل مشخص نشده چه آسیب‌هایی
ایران در این جنگ متحمل شده!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKb_dMKFfN-egepKtrssfwtvHn41ZFshlWDA5VqXvoXJbq8rMXtgpmFHZpN3BnbKYORqmFt08GsyrjKuaMz3pDOCSQNJ4v-8AeXmKqG-tJ87NKK3z9Lhcdm0VZ9knWynhPdFewqR4C9RnX05gUIYPUCiawyK-EXPPWLbSX3fm-Gh1iFh4USrBl9S9CgEPVg_4NsgkPpQ6wO0TCsr5AcFBT5oGvU2frMWddeyOHMS6WLeyuIC0CcIRA26ibflBjkEB375UMbF6YVTcpvKjYyN_rsq14Fk0C-UBXtd0reNvI5zXZuorLZ6nGuVdi0XC5SavcvfeIda49SsVWxE40Op7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oF2FVXREw2rC1MClqcTJLvUE-yOKfi1BKOl8p8WmZWNKbiV4AexSja3JjYqCKQNjdKucY1vMpebZ6VRdRal5ilaHCMQ7zYm-va-TnnPIEPaeDDHttCSTt8Kf7wtMwbcfsg2X91A9FQnuLHghLoTpj5GOTGlJsWYvtq98LvBHNedmhkuLRgKk_oaLYXRZGKU7xgUyxdU9gUsjpgLZLQLPcLYJhTMJx_inCQ3GYPJU5e82H_2PiRwX62YJlqjmnc8pJva1tGyCVWzw0XdIHbT79PdrrP3W_vR6XC4fVkZjqTOBpWFRlzmFNuY7rqJGBIqlMAYtX8y9057o7k7XlFXhOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grJB0YamdfOE3Woh-Y7kk4W6w_hO44cj9lHA-ep97dxJ6GsOtUQV-TsPSGFI8DZn5I33BuFo6VoM4s14u22QwrV0FKhRPkwZDcqdGGV6G0wZa5Jrro8qK9eq2jh6XC1cYNgcQo4YMQrcmwp1SNQRNGWJMgrWXOvNLIOoG_jJE5AkpemAEp6V61gNAlgOiXzgrr86BEWZZR-96h4yttfbLtq8uGogDIOf6dQAa2NLJcA9P7WlGlv6E1fZflJGf9vUsjOzD9mi8f1E-4Q2dheSZ-TbtLlOaprljZZlQJqYhffHyRRF4XrpZ5AiyC7dxxsY8_TEcP1AgZgUWP8Y-odVzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : برای اتخاذ تصمیم نهایی اکنون به اتاق وضعیت می‌روم.
«ایران باید موافقت کند که هرگز به سلاح یا بمب هسته‌ای دست نخواهد یافت.
تنگه هرمز باید فوراً باز شود؛ بدون دریافت هیچ‌گونه عوارض یا هزینه‌ای، و رفت‌وآمد کشتی‌ها در هر دو جهت به‌صورت آزاد و بدون محدودیت انجام گیرد.
تمام مین‌های دریایی (بمب‌ها)، در صورت وجود، باید از بین برده شوند. ما با استفاده از تجهیزات پیشرفته مین‌روب زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز باید فوراً هر مین باقی‌مانده را جمع‌آوری یا منفجر کند؛ البته تعداد آن‌ها زیاد نخواهد بود.
کشتی‌هایی که به دلیل محاصره دریایی بی‌سابقه و فوق‌العاده ما در تنگه متوقف شده‌اند ــ محاصره‌ای که اکنون لغو خواهد شد ــ می‌توانند روند بازگشت به خانه را آغاز کنند!
از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین دفن شده‌اند ــ زیر کوه‌هایی که تقریباً در نتیجه حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند ــ توسط ایالات متحده از زیر زمین بیرون آورده خواهند شد. (طبق توافق، تنها آمریکا و چین توانایی فنی انجام چنین کاری را دارند.)
این عملیات با هماهنگی نزدیک جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام خواهد شد و این مواد به طور کامل نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی میان طرف‌ها رد و بدل نخواهد شد.
در مورد سایر موضوعات ــ که اهمیت بسیار کمتری دارند ــ نیز توافق حاصل شده است.
اکنون برای اتخاذ تصمیم نهایی به اتاق وضعیت می‌روم.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lgcx1_4IvXE5-EaeXtvHRsy0O63ZbU-AsNwqByq9wgBi_LkK7GPPTcZrZGGI0V9MiLeqRrAAiTMT80tu_VJD1Z11XRI9hLwCtjTYradZ6V-ieyB2IAHMJzSdJEJxkT2Spv3KpcVd8sy9sLrRoiWJr3qWFUpf3VF0kiV9dZ9dcTBjcmWmyEeT3Lg5mrlVQsF_nT9tHXdz-bxOB8wytrB8gjnbih2XbAeif2ucH5KjA-DB8gZYOBMMG51eX0UB2s_ZUiBfp4A_dXO1mbXzcIyty9yAy9IjXEz2smX4B1gkTwLQZ7AKDy27yMs2YTX5Jib00hWEjSrTcpw4JBBA8Hpudg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PlBOAXKvskTdkMyzwHb9e3paTKQxOoXe1v4N4Ox4y9EVzju5dvC9Mo2OzPkmWrqCNGTEkUvnYrTqYvPzMgMHMHN2lZ1cdtQ-xvW0Gf7iPqYehzrOQW-hR6lzTABYBMrWhVomH77B3-gSxHhr4DTvzPAwu0NcXqQI5dGkXrtiArJsWOQdBiorm6c9x0xz2uha1QLsMTfaX77OdAaoLduxsqdQL_UW5mkdd1QcRLCR_kiLC7ynj37ri_4ft_v39zXswtVB7VOWktrqy160FsnAy80bPf9vl1N-t1OU41yw8XsoVeBThansoaBDb92WA8EXpGFCxzsZ99-j0oDDCI_sIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U8YlZS39cGol_3wit9cTpn3l1P6jELcx1IwATI5LylCB51MoeO2O3YZWvr60yMP-nztLBpVbfSpNtWLtzQSTUdvl_xxuBJtuBKLT7ebKDqSZQZKvEytTXehuIfOWPJAmLfANy2c3uvS-R1sJAX9EJwmVNexXxYLStoHyV01R7TgpYpBABEy_OsWSJtc5VZcRMKvPo2i93yp5LCp9p3uGFuvH6G3_QNDCK6sbnNtX1yPBg_lZcYU7xnOxcDfQbyaPyL9bvCUkS09tXkufLfh4i-3X_I5TYgN6wqcGTIazZ5hZs4sdzzrZ70LPj82hyzQczD0EakpiQbHVelRzP9tTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VGPDhJZ0Lk_-OjQVXCrx_SzLgQTpBetFzDCaiR7Jy0h9W4XGKESKL88JESFHmHFmysteXHqrXUTLf7I0Wfrf4xvytWYm-sQDqQLqPILPg9uSdQWPmGsxrUzcqUahYB1hhFjWEcPypiHO3K7y5oSWJM8HtCwRV_fqDXNDASAkeKd2thjN3B7V3btA2buVM7I2Lrk5kLG0AxU71SgxEmgQmEUPsI_pe9ewJapZGe0Ezh3vc24jwJu4Xp-duwwkiEGJ228aqTXCpNiUdzlWT3OkkFwepoXoUX1M05OPJx-hA4DGGQUl1mcb6FUTR1CmcmtHjfihlLGzLof4kO6hNXjtqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=tAxT3Thty0-keDWCDC36fdFYDd__7FufrjObnISagXMpD1RYPfxhPe9t49Uly0_kbCdpzEP74qefUHm0uf6rN3fMXKXYUQ0MdaDTgrRfPSL5i4m7WBWODUC5wygF-60UerI8vrA7PHULqJTUjxTHlkLKIvN9nbEnitGzhJRgvzOQYr3IqeMCzC2KjqrE58yiWKmpHFg441Kcr99fSePX6nuTQq6bRI4fNnuD4cO8X5EJrlkWLKlkTKkuupvgdv_Zea2_YrUSahKFTb756dw1HiZ_EtcJh10KyDGiD1SXJ4jRXR-sKU7_a3fNTY4OyHHK8TcM3UxMtZJ86IZwUFfYyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=tAxT3Thty0-keDWCDC36fdFYDd__7FufrjObnISagXMpD1RYPfxhPe9t49Uly0_kbCdpzEP74qefUHm0uf6rN3fMXKXYUQ0MdaDTgrRfPSL5i4m7WBWODUC5wygF-60UerI8vrA7PHULqJTUjxTHlkLKIvN9nbEnitGzhJRgvzOQYr3IqeMCzC2KjqrE58yiWKmpHFg441Kcr99fSePX6nuTQq6bRI4fNnuD4cO8X5EJrlkWLKlkTKkuupvgdv_Zea2_YrUSahKFTb756dw1HiZ_EtcJh10KyDGiD1SXJ4jRXR-sKU7_a3fNTY4OyHHK8TcM3UxMtZJ86IZwUFfYyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=LCH75ef8SLeJb-x1w1ktVRGzcZMgDpjV6H8sp2VKwvJUiCEM_oux60tfCQhO8qF3TxSLV33NjCU9S7xBhP9RNPKxS-tSoV-0MQHU2ngo0lbbs6TrcvKJ9qnAy_z0EMl_zhHJ1XVMbFWcDBAVHjVRkMLtSZGy4k2MTL9XtAzqRbMevN0nUUjgHn6_z3GOFsXMoSI_rfV6hDtYB9ONoRVMQPrJ6vXDOfqWwiPlS44DhoQ_RLyP8SihPseV6Tx6DwLk_rG41UYo-bP6qIZuoYjEoHOfOPs13bu2I28NHh9_T9Plo4UX5qq_pcJFvB56e5SmC-VPAMkEw__B8K2US4SVcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=LCH75ef8SLeJb-x1w1ktVRGzcZMgDpjV6H8sp2VKwvJUiCEM_oux60tfCQhO8qF3TxSLV33NjCU9S7xBhP9RNPKxS-tSoV-0MQHU2ngo0lbbs6TrcvKJ9qnAy_z0EMl_zhHJ1XVMbFWcDBAVHjVRkMLtSZGy4k2MTL9XtAzqRbMevN0nUUjgHn6_z3GOFsXMoSI_rfV6hDtYB9ONoRVMQPrJ6vXDOfqWwiPlS44DhoQ_RLyP8SihPseV6Tx6DwLk_rG41UYo-bP6qIZuoYjEoHOfOPs13bu2I28NHh9_T9Plo4UX5qq_pcJFvB56e5SmC-VPAMkEw__B8K2US4SVcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1yj9LTJxYgkzDaiY5foYzh5trokyFP9V8YE_BnJyb_EGv8olA-Zmdl0nMSIEpGpXdtc8WxXqWyg8wem79fv87hTDLeLY87skwqHYfj0ejp95D0ZA97fCQ38noATOsahbSb8bxohrQ2FR9LwdDVVQRXbT29Huty6ZNUsIK4RvTv0M6GKoyenxfxRY5irb_PHdsGXvL1CY9aGBA57_EhCr87brMFMH8qp-apTzBOi_jHS2bSoYKm6L2fCW7NTz9gXs1lmJzTymNOK13li0t1aByncSTiD6_gpznPPjdH3Li1h_U8RwZMGmgrbkPvpT0Gn4-kUn2RPMbSGvyFM-s8EDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/guO4AKaUoLBrkzCvDBg9-4MLLfv2tDl1rnj-BErTncz_kn2SjADFgPcA2S-Up52DS39fq9rzaBnGLh4stCaYhBNCVZmfClAwT_m33mSOyEOJ8FKwRbQu4sl3WTHKfCov5Y0N2_dYS7LWemAAqjkgbkTTmckpAW1mc7wQj6TOubaDvM4f8hIc_g2q7kgz0-rSPWt71L1ZK7-35PfWUc3FrOnNGXaZoWW2xOfInnSiDU8FkMAql9CAH4A0nhzUU2O8QJZ75N9qJ8lGJQ6v853XXdweZKZpu_Y_o6W20szrJblTIv9vUlUYF34GuecrurdD2WcThKMeKlVmnCtJ2vvkAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،
پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!
حتی زودتر از پیام‌ شهردار تهران!
حتی زودتر از پیام جوادی آملی :)
پوتین در پیامش نوشته بود :
«اطمینان دارم شما راه پدرتان
را با افتخار ادامه خواهید داد.»
پوتین راه پدر مجتبی خامنه‌ای رو دوست داره :)</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=RUT6cVEGVVpNTe8T4dsOFPKxGYPuqBwn1AYCmOUzcBb2X7b-_rrjqaNOwiobVn7xlGP05tVKGWzLmej0MWlqvjZMIXdITdFb6PAvvLCbn7-LPOQAowDg1A_YG2ebtbhrFO_iy8UnZ4CZNYc68BAX8joe3M86VINkdT5OndBMc5anWd9w20FrY27sD1YcIbInl2Gp-nxx5P9cBFTnfISxgPhbRWwKCuuXxWLW2k9UwAZNVUCgHRAMqYcGqYXIUsFUrhBMQV1iIVee-uihMoP1UFBegQF53C15FaHto-WzsGAZb-yY9PCOPYI2ghOxk84HElDLCf0-Y_tIuiaCbii8vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=RUT6cVEGVVpNTe8T4dsOFPKxGYPuqBwn1AYCmOUzcBb2X7b-_rrjqaNOwiobVn7xlGP05tVKGWzLmej0MWlqvjZMIXdITdFb6PAvvLCbn7-LPOQAowDg1A_YG2ebtbhrFO_iy8UnZ4CZNYc68BAX8joe3M86VINkdT5OndBMc5anWd9w20FrY27sD1YcIbInl2Gp-nxx5P9cBFTnfISxgPhbRWwKCuuXxWLW2k9UwAZNVUCgHRAMqYcGqYXIUsFUrhBMQV1iIVee-uihMoP1UFBegQF53C15FaHto-WzsGAZb-yY9PCOPYI2ghOxk84HElDLCf0-Y_tIuiaCbii8vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dy6LssCcS_nH04zTX3qXiWaYq2ypW69EvtLWV1XmJM4vxsehxe5vTo0C4hN159yicedu9pjHNmHU2bIUEEdrq3LgJ6xQEqVLScS-Nxma8hketLAO9g2Uy1l1uKxUM9Hvj0lJ10sUlfHCuzTaUiYoJAk5ZyyfWYYuVYjHBKjtWfdsDCFXy9UdRoB0aR0lUDhSUahH66qmbwYshrxQsRN1T_vGwcEQaadbms9SQMJSCh9QEtz9ChCOSenGOxiuroLtkbYthKcF5I2MJSkxgwYQjeuwAbtYJrj_K5xoJO158p-hU974Pk4WIfkNdU2T2QoHuNmoKspj_dX5tukugMnLbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏حالا که تشریف آوردید:
‏از ۵۷ کشور اسلامی، فقط ۸ دولت کشته شدن «ولی امر مسلمین» رو تسلیت گفتن و ۴۹ کشور سکوت کردن!
‏عراق، آذربایجان، تاجیکستان، پاکستان، لبنان، الجزایر، عمان و قطر تنها کشورهایی بودند که تسلیت گفتند.
‏بزرگان جهان اسلام چون‌: ترکیه، عربستان، اندونزی، مصر، مالزی،ازبکستان و… سکوت کردن!
‏تروریست‌های طالبان هم حمله رو محکوم کردن اما تسلیت نگفتن!
دولت فلسطین حتی حمله رو هم‌ محکوم نکرد! سکوت کامل!
فقط تروریست‌های حماس محکوم کردن و تسلیت گفتن!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5187">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های جمهوری اسلامی  از بستن تنگه هرمز خبر می‌دهند.
🚨
🚨
🚨
سخنگوی قرارگاه خاتم : به ۱۴ پایگاه نظامی آمریکا حمله کردیم و «صدها» ‌تن آمریکایی و اسرائیلی را کشته‌ایم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5186">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔺
شادی مردم ایران از شنیدن  خبر مرگ خامنه‌ای
🔺
بیانیه رسمی دولت اسرائیل تا دقایقی دیگر</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5185" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">حمله به بحرین
😅</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شاهکار جدید صدا و سیما  اینها رو باید تلوزیون‌های جهان در بخش سرگرمی نشون بدن</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5183" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">«دیشب مردم تهران در کوچه و خیابان  کل می‌کشیدن» مرسی از بابت این اعتراف و این مستند سازی از وضعیت تهران پس از انتشار خبر مرگ خامنه‌ای</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5182" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5181">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=ce33ogdkJha-xukNOi1r-D4gniN9iyzgp9iTLICunTi2S6Hc6S-hMjpaRGKJs_GIpu-8LXHoh0JErPdlbQ_dc94IB8tGdnQupo94V0VWCX4NiSDCLncDpbqf4Pd-_XT1uyRskRe36NYe0nRhM3K-eUmr4zA89K46Tvj40QaMrtiXAPko3xurlpJoqPqjlNNAUwJ5M8enotZmlsfN4WqVmKuJ3sE_JXLLMMvW-j-XXx7mQZ4zv_C_jRf8zx9xquSYDoAwrzBWDHpH_KKTK9rGBOw1Bfzx-j8w76qEJI1AKVfXqz3kgxFComoTJL-2YVhajJttk0JwS3_Uaw4glaEA0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=ce33ogdkJha-xukNOi1r-D4gniN9iyzgp9iTLICunTi2S6Hc6S-hMjpaRGKJs_GIpu-8LXHoh0JErPdlbQ_dc94IB8tGdnQupo94V0VWCX4NiSDCLncDpbqf4Pd-_XT1uyRskRe36NYe0nRhM3K-eUmr4zA89K46Tvj40QaMrtiXAPko3xurlpJoqPqjlNNAUwJ5M8enotZmlsfN4WqVmKuJ3sE_JXLLMMvW-j-XXx7mQZ4zv_C_jRf8zx9xquSYDoAwrzBWDHpH_KKTK9rGBOw1Bfzx-j8w76qEJI1AKVfXqz3kgxFComoTJL-2YVhajJttk0JwS3_Uaw4glaEA0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس پاکستان داره عزاداران خامنه‌ای رو با چوب میزنه  دیروز هم پلیس پاکستان ۶ تاشون رو کشت.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5181" target="_blank">📅 09:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بخش خبری ساعت ۱۴ شبکه یک و تکرار ادعای زدن ۳ جنگنده آمریکایی  در آسمان کویت و تکرار این سوال که چطور در آسمان ایران به این پهناوری نمی‌تونید ‌، در آسمان کویت تونستید؟؟</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5180" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فرماندار جم در استان بوشهر، می‌گوید که یک «پهپاد متخاصم» منهدم شده و وضعیت شهر به حالت عادی بازگشته است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5179" target="_blank">📅 00:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از شلیک موشک از منطقه جم بوشهر به سمت چند کشتی که در تلاش برای عبور از تنگه هرمز بودند.
گفته می‌شود در جریان این حملات موشکی که از سوی سپاه صورت گرفته، به سوی یک کشتی آمریکایی نیز شلیک شده.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5178" target="_blank">📅 23:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=O0DZ4lhVpRB4xZwv-MZwuYFk6NE8zqU1CY_pdqdyldTBz249FE3iovJZ1MJk76JFvL1KsNDl0N6uoU8mmO3N0l97EEr2E4l3UvhsS8ivjrAJ7znSdeeiCHitBTz8rINc40zpoMKamrKVGkOdz0f27vDXm9MzJcVTydId17IFHKUaWACuC2wdadGrvMtOWrl8qpiC1iqZbEAy4ciSeTn4NRVi_u4YujUA19bjlkAKF6i22EdYxKfDP_5I5iRYkbz2w5mVkqt5Czj6kPHbFM4f0k8Bz4oDHSE9YsQFczt6nDjSKzFo8us93eAqjcnJ16JxFBcLYeACK4jgI5AI7EQHWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=O0DZ4lhVpRB4xZwv-MZwuYFk6NE8zqU1CY_pdqdyldTBz249FE3iovJZ1MJk76JFvL1KsNDl0N6uoU8mmO3N0l97EEr2E4l3UvhsS8ivjrAJ7znSdeeiCHitBTz8rINc40zpoMKamrKVGkOdz0f27vDXm9MzJcVTydId17IFHKUaWACuC2wdadGrvMtOWrl8qpiC1iqZbEAy4ciSeTn4NRVi_u4YujUA19bjlkAKF6i22EdYxKfDP_5I5iRYkbz2w5mVkqt5Czj6kPHbFM4f0k8Bz4oDHSE9YsQFczt6nDjSKzFo8us93eAqjcnJ16JxFBcLYeACK4jgI5AI7EQHWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=aIv0BMcmgzgQyfWP9C1ohXc-og2wvwxREZaxqIdhqOObRYkNhwtmLzSa2Prs2vlipivbZtyfyP3UztV2ohTAHdctOgYe_CRCJzkW8Rgoa_CTwYOHxLZWpHtS0rYNBCOXgYqB63VzTO_GrLNAsIOyimLF7jk0__6qMUxDDBICjop3XEABiROAFVf02LsYKbCU5Sj6SxbGqOv0_d1_nXH-wo2KRvKUVvqUIPopEgFeN_egjSCzgmEzjMgkUH9D4Mqv4hNUz2xdpbH7KCBTC2PIbrgHaPSbnylRocDbj0fF5QJ2i9psLu_HPSlOwY3t830DV-wh5QEKLDVaV6G4DLmBGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=aIv0BMcmgzgQyfWP9C1ohXc-og2wvwxREZaxqIdhqOObRYkNhwtmLzSa2Prs2vlipivbZtyfyP3UztV2ohTAHdctOgYe_CRCJzkW8Rgoa_CTwYOHxLZWpHtS0rYNBCOXgYqB63VzTO_GrLNAsIOyimLF7jk0__6qMUxDDBICjop3XEABiROAFVf02LsYKbCU5Sj6SxbGqOv0_d1_nXH-wo2KRvKUVvqUIPopEgFeN_egjSCzgmEzjMgkUH9D4Mqv4hNUz2xdpbH7KCBTC2PIbrgHaPSbnylRocDbj0fF5QJ2i9psLu_HPSlOwY3t830DV-wh5QEKLDVaV6G4DLmBGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از ۹۰ روز صدا و‌سیمای جمهوری اسلامی می‌پرسه در حمله به بیت کیا کشته شدن؟
کمیل خجسته، برادرزاده منصوره خجسته باقرزاده، همسر علی خامنه‌ای، میگه  افراد خانواده خامنه‌ای که کشته شدند، همه در یک نقطه نبودن! در جاهای متفاوتی از منطقه بیت رهبری بودن که به همه اون جاها حمله شده.
این همون حمله‌ای است که پسر عبدالرحیم موسوی ،
رئیس ستاد کل نیروهای مسلح میگه ؛ ۳۰ روز گشتم و جسد رو پیدا نکردیم!
عجیبه در این حمله فقط مجتبی سالم مونده باشه!!
چرا خامنه‌ای در پناهگاه نبود
!؟</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5176" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
آمریکا و جمهوری اسلامی به یک توافق ۶۰ روزه رسیده‌اند تا آتش‌بس را تمدید کنند و مذاکرات درباره برنامه هسته‌ای را آغاز کنند.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5175" target="_blank">📅 19:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208f980645.mp4?token=g9R065lum1rLeT5acDMRd9dhOWy1e90mOiOIDrrqaBy8VV__7PXeN_8aos2jQNZxxfA1mYlHqew5anAiWf-wexHFSvaeKo7x3iVT1ZZRvfs6RkOWxrM4kk-AtpigGCnxfkb0fMkpo_iXnnLKjkEKntgyMoARa5gpghiJGUTrVPdq6sakbrMmaR5sG4s4UKgAudCEW14ftn6b1lIm-Hi8lzsW1-9_ZzgL44XIWsJZGrrAAj_ISqBjodAcbvQUUZk8ftuhG33YR1EPBwrcY9mT7Ar9vkwH2GcmgDbPbt01XlAE7qSHsg4DUzy6n5grSye1rVLZ2lBzzgUMd5YcRIrAPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f980645.mp4?token=g9R065lum1rLeT5acDMRd9dhOWy1e90mOiOIDrrqaBy8VV__7PXeN_8aos2jQNZxxfA1mYlHqew5anAiWf-wexHFSvaeKo7x3iVT1ZZRvfs6RkOWxrM4kk-AtpigGCnxfkb0fMkpo_iXnnLKjkEKntgyMoARa5gpghiJGUTrVPdq6sakbrMmaR5sG4s4UKgAudCEW14ftn6b1lIm-Hi8lzsW1-9_ZzgL44XIWsJZGrrAAj_ISqBjodAcbvQUUZk8ftuhG33YR1EPBwrcY9mT7Ar9vkwH2GcmgDbPbt01XlAE7qSHsg4DUzy6n5grSye1rVLZ2lBzzgUMd5YcRIrAPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش زدن ظریف :)
نوبت عراقچی هم میرسه!
این مسیر رو خیلی‌ها رفتن!
از منتظری و بنی‌صدر، تا موسوی،
خاتمی و روحانی، احمدی‌نژاد و…..</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5174" target="_blank">📅 19:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=iQvs5TnXTj1TnC-dlMVFIYZF6ArQDYyLOc1bnaxSqzfm_aVF5gFU0afDzDn-X-rYOUWU4YD0Vc8xZ-X7p9DVY9wddjuP2i3j8RV9z7zWLPO8tR7iUaQX-MUwe_wjb1BHVV0ZI1Tj4YAJjzKqsk2O_C3Uozwx6NWiB7zFy2lMlm9h143pA48Q0Gvzv0bua3DDSGFMMaov239ILL6X1F1utCkn0fiDY-rkVC-bEdC5eQpvsR8m-oRZ6cnWfHawztzv2eReitVKbnDEduzBpZazcDaYwNugfsprtUEgfkFueKliz67dTeHff3108BLoAhokPcN-qjFpaJ5428dW2Yk6Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=iQvs5TnXTj1TnC-dlMVFIYZF6ArQDYyLOc1bnaxSqzfm_aVF5gFU0afDzDn-X-rYOUWU4YD0Vc8xZ-X7p9DVY9wddjuP2i3j8RV9z7zWLPO8tR7iUaQX-MUwe_wjb1BHVV0ZI1Tj4YAJjzKqsk2O_C3Uozwx6NWiB7zFy2lMlm9h143pA48Q0Gvzv0bua3DDSGFMMaov239ILL6X1F1utCkn0fiDY-rkVC-bEdC5eQpvsR8m-oRZ6cnWfHawztzv2eReitVKbnDEduzBpZazcDaYwNugfsprtUEgfkFueKliz67dTeHff3108BLoAhokPcN-qjFpaJ5428dW2Yk6Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=Y_VwAhHiQPrypslzamaCWszoQVCtUwkX7lPPOCJ785z_IrN7uI-cdmygksUh508BNV-jUPq3jr-01EYFa8bMG7j4Sxxi2yoWryEaH9KPoQlL_kuohSA5_wlr9feK4DzIIVIrY_tb2nCheafPnbq6R-032eZK0Ngspk3EZcyhxMTwpl4t8VreAAVac6jtJ76CINqKmB_5HE4XxY0QN2OEQrRzA8cklLbPMx-ItxPIOwP3w8j8QDGGf-UIja8sq75Hd-et31wwmGaNqtFO0QiO8_qMzknpKXCQOdoqjikAhwLEh04yTdCYbBRgRbyZlXRitz9FnM9uAfVPn6MT4iqZJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=Y_VwAhHiQPrypslzamaCWszoQVCtUwkX7lPPOCJ785z_IrN7uI-cdmygksUh508BNV-jUPq3jr-01EYFa8bMG7j4Sxxi2yoWryEaH9KPoQlL_kuohSA5_wlr9feK4DzIIVIrY_tb2nCheafPnbq6R-032eZK0Ngspk3EZcyhxMTwpl4t8VreAAVac6jtJ76CINqKmB_5HE4XxY0QN2OEQrRzA8cklLbPMx-ItxPIOwP3w8j8QDGGf-UIja8sq75Hd-et31wwmGaNqtFO0QiO8_qMzknpKXCQOdoqjikAhwLEh04yTdCYbBRgRbyZlXRitz9FnM9uAfVPn6MT4iqZJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله هوایی اسرائیل به بیروت
🔺
آمریکا از دولت اسرائیل خواسته بود تا به بیروت حمله نکند
🔺
گفته می‌شود که در جریان این حمله، «علی الحسینی» مسئول ارشد موشکی حزب‌الله لبنان، که در واقع یک عراقی است از «فرقه الامام حسین» از گروه‌های نیابتی جمهوری اسلامی در عراق، کشته شد.
🔺
اسرائیل دیروز هم در حمله‌ای به غزه، فرمانده تازه منصوب شده برای «گردان‌های قسام» (نیروهای نظامی گروه تروریستی حماس) را حذف کرد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5172" target="_blank">📅 14:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">علی الحسینی‌ از فرماندهان ارشد و مسئول واحد موشکی «فرقة الإمام الحسین» حز‌ب‌الله عراق در حملات امروز اسراییل به لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5171" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5lf4HAYvPcETgv_diPc4Xd7T3-S7WZL4H5kEpROtaKTRvaN_pDtLU1S-BhLFjKJa_Gf1hZZO0ji-SAGdE5xodc_TyVgAze6phED-gSV3WawLxVtsfFyuwSmN2jewnlikpT3n3aneOHx1Dq88FiLFzNz0I8J-DEtZvEJ0xmooMWrSb8vbjr6FErMDmEEHnGD_3l1tvDHlgeqe6UziYsyUs1bBtfEz2OhlwzlBu1ii2j-rXG0dXrYaVdQeETZueTfbaE5Pmkmk2eRSgrpl-tK6su7ZfNL3l0xd6Jk0iebhTaGDCHAT2v2dm-3IGa-TeS9DnWnt3WLhmSg0_0K6zWgiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام:
ساعت ۱۰:۱۷ شب به وقت شرقی آمریکا [۵:۴۷ صبح ایران] روز ۲۷ مه،
ایران یک موشک بالستیک به سمت کویت شلیک کرد که توسط نیروهای کویتی با موفقیت رهگیری و منهدم شد. این
نقض فاحش آتش‌بس
توسط رژیم ایران، چند ساعت پس از آن رخ داد که نیروهای ایرانی پنج پهپاد انتحاری را به پرواز درآوردند که تهدیدی جدی در تنگه هرمز و اطراف آن ایجاد کرده بودند.
همه پهپادها توسط نیروهای آمریکایی با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنین از شلیک پهپاد ششم از یک مرکز کنترل زمینی ایرانی در بندرعباس جلوگیری کردند.
فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای همچنان هوشیار و با تدبیر عمل می‌کنند و به دفاع از نیروهای خود و منافع‌مان در برابر تجاوزات بی‌توجیه ایران ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5170" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=r1Va60-qFErx5ny5aXj71UOsqIrlzHhjIPZyBO9RbT4vzJczPIjzxA-WKFbSE7lAS7BMSKNJtsBGJd818xyovYLbPWgG-ln7u9WRxoRWiaKkvcXgSKvdk3jICYPNDlsQwPfJZa2u6DRGbeFeI7Fz3kR5NZABeakzMDRfNPNReGaEGp5srRXemzO1lDMRu9QumtdSS5yh9rajk0ANuslF6sbRrD9j0WA7pf-2Rxzn8OIfUeasJet9VDBLqMuz65Ur3ZWrjkIhakvvitDOmEimq357_k_q3pJmgkbXtoae65Iuzz2GqyqN5Gj8HFADgUKmC5RUFMJhGsUndZ8pRM5iRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=r1Va60-qFErx5ny5aXj71UOsqIrlzHhjIPZyBO9RbT4vzJczPIjzxA-WKFbSE7lAS7BMSKNJtsBGJd818xyovYLbPWgG-ln7u9WRxoRWiaKkvcXgSKvdk3jICYPNDlsQwPfJZa2u6DRGbeFeI7Fz3kR5NZABeakzMDRfNPNReGaEGp5srRXemzO1lDMRu9QumtdSS5yh9rajk0ANuslF6sbRrD9j0WA7pf-2Rxzn8OIfUeasJet9VDBLqMuz65Ur3ZWrjkIhakvvitDOmEimq357_k_q3pJmgkbXtoae65Iuzz2GqyqN5Gj8HFADgUKmC5RUFMJhGsUndZ8pRM5iRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmWEYZmfK-xos3t15Z2nmsbPazKsk9TTabyo3Cb9Wut52Yeo2_Ztl432CD8wIyO6jf568KFQdqewlTZvNxsBGVPyvD-TZgf6rd0EyRQ2mmMDMeQNDBY4M4j1uMSoXW2S79vM5b2DIklkYDHmDUlrXBnJYGwt9bnwnK73vdMHT3onPVI1ZAVJv4kmse0UqVnpMj0ZmXEnUFk0q1f_fpZHFp31Kgz_hC3hW7viWA_MuYyP0PWksr5YP-zz2JE0CPyvYLo2PputuL3Ld-_55kfoCUA57ZgUw6UnShJo9ETgUavrcQdFkaaSvhaOnl2RaluzgFbnaLdJZqYuk9zXo_SHHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=QWbxnz9I1pUCH8yEkDP0i7Ti9IGrJpxUXyk8OWvPTxAu_y4R49Qn3C72lxqaaXvFYxQanRA5PSpYyxxhBH49sUCnj9s9wNM36fLXPbbnhz5wDqz5AqdZT7eFIY0bD-wiWLbuGjXbrlkPzuMnax-8tA6HARjDjPUBbQw0X6_1mivEhoMfyn5tpdLBTxWf1nuPLvoojpDgpglpftIWSmp27m2iXna8BNETFc1Iktr1AqXaS_yFog_xSNU0UJd5WMuSyOCN1BOHx4eoYyl2aHrXNc57FDCWC7GMgYFNQY7u3aXTlGpv_EMpiJe8F4no5aHuWMXcrTuFvajfPgbhfk8bQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=QWbxnz9I1pUCH8yEkDP0i7Ti9IGrJpxUXyk8OWvPTxAu_y4R49Qn3C72lxqaaXvFYxQanRA5PSpYyxxhBH49sUCnj9s9wNM36fLXPbbnhz5wDqz5AqdZT7eFIY0bD-wiWLbuGjXbrlkPzuMnax-8tA6HARjDjPUBbQw0X6_1mivEhoMfyn5tpdLBTxWf1nuPLvoojpDgpglpftIWSmp27m2iXna8BNETFc1Iktr1AqXaS_yFog_xSNU0UJd5WMuSyOCN1BOHx4eoYyl2aHrXNc57FDCWC7GMgYFNQY7u3aXTlGpv_EMpiJe8F4no5aHuWMXcrTuFvajfPgbhfk8bQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !
جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،
انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره و مفهوم «شهروند»، دادگاه و وکیل و حقوق مدنی، پزشکی و بیمارستان مدرن، بروکراسی اداری، مفهوم حقوق فردی، مفهوم و ارزش آزادی بیان، مفهوم دولت و ملت، سرشماری و شناسنامه و داشتن فامیلی و..
صد مورد دیگه!
مسلمان‌ها در دنیای جدید چی داشتن؟ هیچی!
هیچی!! لباس سنتی بپوشیم بریم توی خیابون هاشون نماز بخونیم و بگیم خدای ما از خدای شما بزرگ‌تره!
با نخوت بگیم ما خیلی از شما بهتریم!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5167" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5166">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
سحرگاه امروز ارتش آمریکا به ‌منطقه‌ای در اطراف فرودگاه بندرعباس حمله کرد.
سپاه نیز در اطلاعیه‌ای اعلام کرده که در پاسخ به حمله آمریکا ، پایگاه هوایی مبدا این حمله را مورد هدف و حمله ‌قرار داده.
بیانیه سپاه اشاره‌ای به محل این پایگاه هوایی آمریکایی نکرده.
اما خبرهایی از فعالیت مقابله پدافند هوایی کویت در برابر حمله پهپادی منتشر شده.
🔺
برخی رسانه های حکومتی نوشته‌اند که یک نفتکش آمریکایی قصد عبور از تنگه هرمز داشت که مورد حمله سپاه قرار گرفت و در واکنش ارتش آمریکا دست به حمله‌ به اطراف فرودگاه بندرعباس زد که ظاهرا مبدا حملات بود،</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5166" target="_blank">📅 08:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biHIiS7xao6x-Ihx14sbG5TvPEqBzQ64tHOI2KWPn3zLP5YQensvG71N50zi3PV9cGgOTbgD5wtK5u4ePuc2G-JRBDn3jrlhIwsltfYPo0tujDPIIKAfRRH9orHu7r5HnkfrmfyZzeZREPwr93ClOzja0RZsX9VBWUe3_Mmd-Uny7qOO-e_ycfrLhFjG7nqKSDm0vydrxFQ7WAkhkVndBGNvM09Umd5lO-hl05WSvzA1VuBDUB7HaHbb7rLIPQKa8k11bGYx9J-KA6FGWUT4Il761bDmeFUNpwJ2sjFZ5-VQMHDxi9odIhlFS7vbJuCDqORxEFWrmn38czmnEWgZeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mz9z0e3REQKlmvtnDSeFXjKFVVFpzmGfedeywpj7pFS9NaUHatvxZ2H8ijHzFfCDwbEed-9bqOJlbqzPStwa_WMfEtX7ggOiBTNjHqCa_vQjBhjQ141JZUhIFM4QpFp_XOEqHR5ln8wYTctBH1Ucai7jVbqgbZp1jzPrg8FIZdklieNrj-VZ53F-KQUeuJpNC221NiFbxB_CpAV4kPZqDUCHEhrB_zfi273kXHpfId7vna2BN6YJquU4Z1APHHKwScxoiF02tAlnIjCnIrVqjYyPZ6az7yLtyfMK2VYWY6egXkUNICYDozPLWEOmAFRjUJKmyYFGC1b18Wb4j02aTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5-Mj_ap5Th935R2lvPlYIGc0sEBFtrqHOHEdeECCqhRBqDzzbRtopV2eTpL6lv8LmhbUi3m8FVo4GM4sYt2gp0xsThqLBXtlGDs8R6IyAy7fLjIvJWblRAujmbDRo-1e4simHO2zkntJrxDlsXIbybWo0bUbnCLxp4Lfr5wJuF5AaOrf5Abu6WG8_HvN2U9fT7mZyV7YmYYHq0ws2otzbjQvvtYWKCulAQq3_Wrc4nXd9iT8CM1WkC0EwZkCHt0zmojh-DBS8BKHbvNlnMBOVxlYGOWveUi59PrwjL6iLcC_JpJqhMaasA2rs3Ja5W4LfM4D3CbeK7D3rDpdYSaGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwU7TfFoQK1qlznirjRNLm3-5Hfk2TRwgk3xvgUDFN9YIvKJTGAJ6I1_mZYl8G1iAccnF9G-ygVcgmbMb4w8tLNR5IUxwc2ycqEnvchYzVEW4Jx8Mjl2f4STXH47xeA13FXeDbVCKYBsX5pZdsR7JOrjBzamdEmq3BjNQ-srHJaccazlr5khL9Z9BdImSESkyz4PtPbWtze7wSJg54k8mMSBFy8WkxJcTdEpi2AvAYvs7iAQgiNexX3S2HqCq_MSUad_2Ig68b2JhCMMUqi-WHy8MLd6VhqfPEFKag6P3iHsQLGk3m0NvHmXKu2ab40VDXiyFdO3ji4B2bf-cbxmdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPrBSNG5C_-iRAAYrUQMHGEPcJYQ8Y-6q5rAU-Gg4tDVOPLJlCSe4M_yPmbVeQsE2cxqjXoAs-Gkdyx64heaHoWJhwqw03tJl7ENuRQJi21pTPjY9OVBZTUw8XNaaQRLu34Wap-fObNEwY-KPFOCVt5T7_ChqE2_2YEEUvVzXhgZWcYPRCYjfilxEnatHBuizFmZ5Lp7-G9gWLQI5F9q2SnAg_TafNr4mRKpDJqnNtBeesa2b-FQbQc09ayoiao3J_2JkowrRMwRzr6h1zxjVPr--byIXN4k5GhTV-RsfqTnALF0C2qfZwGLUeEVSKBQ8PqWtZs3HPblC7kzMjPvGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o18tBUr1Xg1GAJ5x8Uktf5QzyFHHg12fsrXhb20BPsVjUgfq7clVN9XHhinH5i0WPZ7rVlmIcwjW7HgDgDCm6SFIQ6lnGL0DU6SMVG7WhJsb2MtsqD-9zoTMYavkFpGAV_IzpzeBI6LQfoVa8bCn8vSZ2UQAmKAaWaJLqiHzIL6WQcE0MfBGEjQbzXsll2BW4u7Tjt9OD8YZFTUJnTu0LZzlyVGkramfMBC8w5r5pzntH0004aiPg3Ii1C_1VEQM1edQyWyosYGbwamAu6rZ6ayd9YA_JQVEaQqp5Oz83eTsWuXmBEa1gAPwvHz6zSzg9T78TFWJ6XwVydOGnR8aYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeODqEknxmF0KcNdJYdXmHC-ju9OfhYNxRnmPHePtdB2YKf03fOtoQ04diF5h21nklxFzNwhSHCCV6RqUOYqArS0486rlGnZOJIwEiP98w1EoP134fDj3vKFx6bckvYnXbkmxBSe-ROBXk5EhArQsBEl8IzJEU0SgBwvDs7z5b3f47h9VyIcEv8IF4UUROUfz-1FaSGNXbtOwhM3YDKVraGrYEM6gef3bbAkpoUT0WuJKrtrIQiim5BsmHWj2woFpKWRYUQOJuzZJ6wM-5Ya8sHU9EqKYvcFJE45dJHnXQrQQogYdf924B4G6ODcUPoYHhyYFQFgeuBPZCn6HVCQsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHM_Na469jDm83E9-A6-eBb3YcW8ysvX_h9Hg7Cgk21IqHnVWdf0Mj3sLKAGVUxOu2mx6TIdmLm0HoFKettRZYRWNCd8OEUP0KCpWw3NGwWdCSlZSYUtPVMqyYYZdOTikIaNWFwbzZCrc63curXFCoY8ZLVkGsWwsUb5PhF8PATVaj9tt9XdLvmfvoufYyENxbdErOq5V2RQTUZdKl0ofKmrwn6yBNn5j0SqgkvmlnmprMkGSz_iE16N5_p5401EKJw_5VuaWcq48yChzt8R8tnCHrc0eHyvVyYp78O5svtDjpzesh_oS5kBMsbgrA6mzJMUAQrA9qXCATYvJ1KAVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

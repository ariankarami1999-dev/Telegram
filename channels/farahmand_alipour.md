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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 00:57:54</div>
<hr>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=uhppZHsKlj6yoLSHOLVOpveSirXVgJc2AIK6IYdyRxFTaecwZyCOeHs7zgA1I_V28khg1Ye9mLwilmjwWu5Tvt_1W_S-AIWuf3pDwdg5puP9JWApXWQvgGryAzIKoZTkb3599PqcSnJxtQfoshAiXGfUVC6hLUOudZ5G3risjkx6lupqIDRPawFlUNSjI11xV9LKYxwZ-N-YWYSfB8J4NU_VW8REuuiXHnEvQUC6GpwY_uQqvBpUi3zH90XaZ7jKVduc0P_ZgS-uUp-5rxJ2p6iXL90HAiUVGaIZLM7UKn7fjUPdIQ_NifbCLYGUmGxB8z_Y5wmo1Q1U0vi_0m3IpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=uhppZHsKlj6yoLSHOLVOpveSirXVgJc2AIK6IYdyRxFTaecwZyCOeHs7zgA1I_V28khg1Ye9mLwilmjwWu5Tvt_1W_S-AIWuf3pDwdg5puP9JWApXWQvgGryAzIKoZTkb3599PqcSnJxtQfoshAiXGfUVC6hLUOudZ5G3risjkx6lupqIDRPawFlUNSjI11xV9LKYxwZ-N-YWYSfB8J4NU_VW8REuuiXHnEvQUC6GpwY_uQqvBpUi3zH90XaZ7jKVduc0P_ZgS-uUp-5rxJ2p6iXL90HAiUVGaIZLM7UKn7fjUPdIQ_NifbCLYGUmGxB8z_Y5wmo1Q1U0vi_0m3IpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=rjByUsw67RfMsN3LvOUQHt00mVKiLy5KvbNz-jgqbV5-fUJRd6UXp4os45E84CwG_1nNvA2dARd0D9MvmrWJsn03UYlb2_0p89U4B_CeUQRvTXHOBQBPi5myK5UmKa2O41X0K-f1a9rDHyjZ0qPK2Jm3YlkAepQM29wAe0hFZhIQu1fCLgZ59r49Z_FiAtAVOQoQz5L959JhVgsQ5LSAROlR0mmDOcC_tdfw_QiZgYQBSgyu960HwIGSSNfIsuM6ZzHuTz_eJoqa70t_WjhSE6UqX2TihsWmm4ptmOR3-0sIKxwfCE8_whpggN-95DMMsEEAnwh99QB3QG1yqKEqWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=rjByUsw67RfMsN3LvOUQHt00mVKiLy5KvbNz-jgqbV5-fUJRd6UXp4os45E84CwG_1nNvA2dARd0D9MvmrWJsn03UYlb2_0p89U4B_CeUQRvTXHOBQBPi5myK5UmKa2O41X0K-f1a9rDHyjZ0qPK2Jm3YlkAepQM29wAe0hFZhIQu1fCLgZ59r49Z_FiAtAVOQoQz5L959JhVgsQ5LSAROlR0mmDOcC_tdfw_QiZgYQBSgyu960HwIGSSNfIsuM6ZzHuTz_eJoqa70t_WjhSE6UqX2TihsWmm4ptmOR3-0sIKxwfCE8_whpggN-95DMMsEEAnwh99QB3QG1yqKEqWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzvzQg1_t2hbOwZ8E7EaiomDRkRaPDZ04KwNq2whN0IfWA6xUzamD5XD3IGXfPuyfr6mQhy70-gAWJarEskaUpdlLr6Ch5v6aMKgIfFGCMj42oJIjp0N188y9jWuKPYor10CH0hTlXCWBhm38VxIKBqR8m3hyE4BOaJlnysMZPflzSSlmkYeAO7gYPkPwSguimGimPq7NST-GuIs-ZSf__xlgd2KrZVAu-vRnOhc4TYwbSXveBV0-jbppuA-m4I8BqunM89c6n9seNerh_cNL2FDDJQSAC7ccRu0-L5XJPx679vYWRWp7BbNEfw-a7do-ui4xtY7YAcTBlGy4Y3w-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aa1SUO_3erGCcGeODvn4X6O6Nn81h2Q_rsCh_Jvw7YwQ0ashMqAkztc1xj72AxFq4KbJlYzaOiRSj79amKdKk8Cj_iX2SmsY9x8H0QBXbb3b7q4qf4jTU23k31cDJy5W0a9vrV2yNSCWzwYWEki3DMMpOJqdqzgAKdWfCWO5Mn0b0ODDKc0e9qPfgdYw0Hy5WXUUggDFqOLB79KQONtiU7G-drjgqamt-KVKLzKv13H74vnaHeFvKHL90CKxf7PFdfg9g6xFynD96ZLchL_CaDOlnkEHtpiaE5kxixjHoSp8KkdoBD16GTE5vPMCECdaODE2SMYH1NW8v_IoTh_2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/5265" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWelbRb8XSFqxIrc_vTotVmbN2n4QPda70hcD3dfSHGMOYGKrSyYEzk_9Jws-Hz3Z8dTyNXMJZ0epkxcGZ2BUl5M7uoqV-faeL_O-7wh2WMxFP-dTIl9YGv-qE6BnqsaG4iIFsmxMMjAYTVzWAF07GsxNwiC30S1DzvF37kI2eDW6mS9ZHxErCltbSfdmQFlATje3UiNZQvuYDkPIKQYLWq25A4Zv2q0THv5Bq28Kng9z3KoXg1W_1NJC_oKPu_x2jjjPqAhbA3IHol0N6Was_JzGOIgPQgEvoGtvBmTR4PkZhdVzJUG-N1W0neNf1z2-LA_d13f6gTUVxkxUrD0fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GH68NWPUAfl87xVgUdOTn0HP4e7NotuhIylwY8d1A0BbSa0IHY_Nsuj-vgKIQsq9Gsuqrqt03zGKG-58XMXXePWVLuyRLpLH_K4Sv_WTZF40nRDOOMyf5YENUjmUXLw06f0XQo4yBz3xAseLiZtvhQcEhPjxmp4H0tNMTztUrwMLmO97_N4fj6kLAeD88A46uup82Cx_kXA_V7JulJg5MdOp9YRhsbMkVQ3gZF5tRdwCgq08oUqhB5vApteuwHLiNooIxCQ_AdFk4r9bxaZMW0F54bL31nfttuCg73K1kqy6vBk8TbJjb_KqK8eR951DLfGyLe6CJAOI3pn0qzLGiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJNChKs8UX-xwTz_nykgmipLJes__i3DWZqKtPaGjHicjYxD8SGlHekrG4AOHGSDZw2dwu6jkUBfTpaEzWRQ3goSKY0xQrAkSR5E77xtC-eLnkJlM85mLNYwsHIKh5Anab6mhU3L9OR4XO4C72HIrV3ZLFUgqw0WLc3kYVkCdQU9tL650gY4bepLFtMjmIiDpv81aKhozdAnT6-vWyvBAYKl7sMS1Aknub75YCHAW79ThPE7K-847a1Ut68QcJKFG0lfR3HMUQWfwHp1m5KqGqFrhM4xae5Kew_vttmavqZCLNbgkr6LgoCdyS-XldqrWrgvKxkXuhwy1c3v1-HZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITXA13_oTN4uV2FBVjfUB70-sG8QzriTPbq9LCSgZLFwYU0CfOZSuO99RiCi-KuFbITSgDKcgebqHaR8Ll8wrxloaZTQtvfAewGEQ6yLn5cz1O5Q_uZ_Ol2SBhyRN98JcSR1wttc01Q5LRWB9c2pDmx2nzWcHRO_PlE0GPBUis8rRi3f-CP2Xe6lzw0lx6og8TWqOE7d1HJTWP-dvEhJqa7iT3X_1wnIBAS8lXJx89v6I4W_PKA_hQZnrQSJDDMwRd8mL9SO4sHhFluTFBkDUNjveoFwDTfIAYBLHZ0fKUZQTYX5N5ISAsEAmmM6HuMInR_aTPXdwrzMVyjjLgNNYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5mSTAiHyMaE1tPBs1YQq3Bb9i9HqpRUS9WrC-DXUyBy8dAYmVw1z5hWcZvrel0TiUKf65b-CZemdVdg8mnDPk4YJfV8mamxaZFhKdMlZLbxhulyOdTB-RrTuB0zfhuUc7bDKtqd3JO6eU6cq3zeWpocFUhFV1VaaV7WHgciRoYp9uEDqaiMMuGciOl00WbeE64v3EOzB3aJAV4phy2nm0LV44hHwKEaVmXalXvJ033GWcMXAIAcZrds8BsMOVayrcX1xVfDcIWDwM27J4ItzjFzbR85bhIVt0pNSncZ8mdaRnYCGAo_oPB2dZoI0jCNVXuTp3q46dCeX1Se_Ow2IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flmsoJJ9lkcp98hsmgYyz1Cq4iH-1gUuYD5eC1-GUdE7_3SvX9P6uLsK5SduEske3uPgzk0fK9Mj6WFhMABIjSiku098T8aKjQColm16Y7UyYwpOS0vwrb9wmgEpxFaECHGS_CfjdOZJyP5uyLPHjzybu9JbU4WRQ6lC2_2PMn1OG0ORP3AhJEVwpKlL35Kza0jMipXb2RddSbbMLpIVw5HS4o0792UhitYBHrgtBLbQU1jqOQtUOJSNLNuRO7GZAfUtFfs7vf_S65OKBLQpcDNqviu2MKRTrp1zGt6qio-MgzZ_a-lgpdKzZHFi1iNWFZdB-3JsNOaOjLPzd_OJcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=k5XMzNxXoKxL5FjSE1ku02JvcZF9GXOO3EukrVWV_7z0qxK-zgbMrGAQuw242-7S6-YbnPE9aU_wKEu6JbWFxP2CHZER6xoincWc6t2hyWN5G-NDNxEH4GAaSiMhI78DDGcwpYhf2zQ0evVX-9_ss-g9PTSe0--Hi1T-81DXCKnd4XhsKnr6CKv-avhga3BQr3r5V0ZCuXYwrPc73Qh8JKOPK9S151A0M7lhyzO72QeaRKCjch1j-vDAHwZ2AboUqPTuDBA4M7wRAsID2HFvMWo_3sHd7bb3a7q-ZkYYzfG-W9lqc7PP_CY6EUIuKAohOJibVPCggfHIqqxd1hIdog7QAeGtqn_rPH6_qXwl1_b38hq3jceC94Ys2DIr6W5vQCb00xiBX6LKNnVEox6z4XY8Qn4w4CUUCcSxfD1hGhNjEtlJFWO0cKs_bZfdEAOg9GdFgI3nPIB0cfnq5M3JVcI4ZHXTe2YDPpoSZ-xw06rFDxC9ltFz48pbu6G6NDbRCGeLSuw7YqCcvsAxuW0YrEnflsW62Lq_0fPXMSaEZRUBY8ses6Q2sk2dr3Pe57ODjSyyqCgobWYJFuDV8nq0wOilRgKA_i5u0i_mv4k1knr9RodhKxnhT0rLGgW2oSMQSiy_rYBlhF6WKSMDITHe-6WykEUTqRYbd-KYVzsKpWk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=k5XMzNxXoKxL5FjSE1ku02JvcZF9GXOO3EukrVWV_7z0qxK-zgbMrGAQuw242-7S6-YbnPE9aU_wKEu6JbWFxP2CHZER6xoincWc6t2hyWN5G-NDNxEH4GAaSiMhI78DDGcwpYhf2zQ0evVX-9_ss-g9PTSe0--Hi1T-81DXCKnd4XhsKnr6CKv-avhga3BQr3r5V0ZCuXYwrPc73Qh8JKOPK9S151A0M7lhyzO72QeaRKCjch1j-vDAHwZ2AboUqPTuDBA4M7wRAsID2HFvMWo_3sHd7bb3a7q-ZkYYzfG-W9lqc7PP_CY6EUIuKAohOJibVPCggfHIqqxd1hIdog7QAeGtqn_rPH6_qXwl1_b38hq3jceC94Ys2DIr6W5vQCb00xiBX6LKNnVEox6z4XY8Qn4w4CUUCcSxfD1hGhNjEtlJFWO0cKs_bZfdEAOg9GdFgI3nPIB0cfnq5M3JVcI4ZHXTe2YDPpoSZ-xw06rFDxC9ltFz48pbu6G6NDbRCGeLSuw7YqCcvsAxuW0YrEnflsW62Lq_0fPXMSaEZRUBY8ses6Q2sk2dr3Pe57ODjSyyqCgobWYJFuDV8nq0wOilRgKA_i5u0i_mv4k1knr9RodhKxnhT0rLGgW2oSMQSiy_rYBlhF6WKSMDITHe-6WykEUTqRYbd-KYVzsKpWk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxgVLxBuF-C-fiVGgxuZITrFVcmXdgI0ipdto8acrJ_QT0QXxBketcE3V0qLbKDzKi-RaR3dHveTzTk4rSw0pK7yphnJbPX8I4Qp8tYwqjOnUtizBDEOmVRwY0x-vej7y5-gb8tXv2Uell88iiMO84yQ2XQGuapGI3jyDL8fdJ_Q19l1iD3XvjwixkZIVEp5Mo5A9nNrD_-GT4L_NlOseURmGUKDgw7vw2oiMC5FsprMFDYpLg55FHcvQJP-5ncFuPjeTWrZ7eTcvPvvTCG6ybHERPBEYzQv54kWn2GLwmW4XhFCC2lia7xM2O3-v7owENUgWMFefR-NVscvsWjNfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5245" target="_blank">📅 21:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uympb0ZO54zUYIxc1a_rBIBT8UzL_t2YTYE7I5oCm-pY1ssct4XCeHaQXC8JfZmdsmo9qED3Ar9J4RDkL1p1dB85nLdvuEoq4ZtyfadCebPnF8fZpypj6cUD_YeicTThcjnKJnJ1qt3ef0qzeeVLFBLTenm3kRId0AvQFfu1TjafA_tObyN_GKWnkZYOGp6Yt7ADcIy0R4m1hWLvbOtm6XJJcmKWgGR4WKPxH2BNpfLuvH27HvPYQNfdf1ItGfnWixwUsyXVMP0fFzGxmHN0zZSDbOPWWiAHqpz80j63ZhjrQ4axa9Q_5RaVDj7W_p21epjQYerKVvUVDQEK-qy_Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvO-N3-fcofV0j1i_ayulg97WtMDK-NBHsGsKw3DjGBr4--iH-yNNelnB7pHursk4Pli-ElnWNbSA_ABn0pspnX46_uVzTwk07pUO7Tgt6RTb7tRYIPahkdYt8EOU9C81yvZ3WUP0GCnLFDWZEVbdzwIXCDve1kHf7RQfAwUHy2tqNjBXtCFa-nquKOtLu-V-qYXNhrIsMqPu8CWTlAX14HeiQ-ND-XzqLeLqmfMr85KCBjPwUE3UG_xIqAtXhqXCfFtwTicNx5rc6cswT7wCl7XvKu54fyxDoC-eV__Wt6KYzDB1VY-MUU6_gGpAXjGhKXOeqRweBBL-LZQCjmhyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5hldfMVVXb7B02cTIWH8DZ-ezrTduwxyCK6ZXSdxWjtfsFTrmerBeqgXF76EMA1os-V2IsFM1pnP-87itja-SLDEyqnISNXV_eubicunsac8ARD7q0ocFR2aUnoOmd0kFBKBDj65LtRcMBgQHxEksHkSzJBC2nCoZHFUfvOQ51DCfSw7xuEfOZSH7KAQioxiFx_o8BY1As9n3wJXIz5XBOBL9aq09FHqEBRYV5JRP0V1P-xxPZk6zNRovEQw8kWdrsLu_HOVfD8wePk0WZnp8Oe9u10Zby2iCszpyBNcHaceeIty15UvzNeGqF3NoNTFWR_mguRlYvZeepvqnpNjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSzqDmRYBjnwflFn546bm_7C8dUPUXeJiTYl4QuIp3we828E6Oc8KXSDXhEovYSyFkxiCeiq5nD_84Tfjr8yLkyqtxkvgpAKA0MLTUeRxXFhJXT2kGfTWU17cOnQaeHnbuKquDB4Y073Qc-_u8J62uPXSKX3ZZKlgBZt2chgQiB3z-PpPN1UFDbuiFlOmEz7Oz79BppJXDVt0H4KsuuQnZKPGqhhKwPp3Ftcq7yPX_mO7VNvNkStrTHL_ksmhHzCOkAE2cFtjgrk4zfnW_5rjGzjhKAhZLscMYM-n-t27aStSp-eSjKq3fa4IQGA2Xytvosi2YQaH6-DmbAOM9tSPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzOj22pUs9ZCtEAj7XZ785fEoFoRoKdnSjGQoahrjsJW6m7muQ1_bT-Is6LXdV6E9Fhtr9v7AmcAGhkZKT1twrfxZwVhqs_IYqsFhO4Ys-xu76v1-8Pd_9bipDPlViePoAoAhjWmcLk3sPVVam5CapjFzywPHCqCpoglivzNfGkmCeIs0k1GlTMmjvRPuxWT-VVG4n0d51SEucbU6hoJkSaKUlDwcgOcxpoljkzJBkF3lL--IRvthB55SE9Fx5mgm8oihVk6IYu-ivzLxxIZYatSKZBdB1IBxa65lmiBDgyMSUeXv61PNImVGs5-5xzQxUPNsjb31zcsxHZTkT_4Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAJkSfZYKNbOc9tby7jNYbO_SvgYWMIWnquIBDo3WN_OAxlU83-rd9TWGY7tDIc5cRToTnm1G9xXITTvE7wqj2ctfGPe4eItsljBsQY6lq6qPQ_uEHvEGXTiYofQ_pUYC3wOEKov9QEQl3QWVJs2o056cFwBHjTQfIhcmL246kWb2qaElG6xV1dplUHtjBAeo3KpJ4O5Tl88kLZAYTcIGiadaOe3JSnnRFYsqmFsQEQktHAfw1KGuRXRAoziNQBo2NdgS23KUuoKADhodCe-fMe9LB8dvd6lKPKJgq2NNtMF9UPAl9CO1dFf06VJ0Uk6eRF812IsXHt5Ys8k-0Je7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو دستور حمله به ضاحیه (بخش شیعه‌نشینِ بیروت) را صادر کرد.
🚨
بلافاصله پس از انتشار بیانیه نتانیاهو، پهپادهای اسرائیلی در ارتفاع پایین بر فراز ضاحیه به پرواز درآمدند و خیابان‌های خروجی این منطقه بند آمد؛ هزاران تن از ساکنان ضاحیه که پس از آتش‌بس نسبی به خانه‌های خود بازگشته بودند، دوباره در حال فرار از منطقه هستند.
🔺
نتانیاهو دیشب نیز در دستوری به ارتش اسرائیل خواستار  عمیق‌تر شدن و گسترده‌تر شدن عملیات زمینی ارتش اسرائیل شده بود.
باید دید واکنش جمهوری اسلامی چه خواهد بود.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5236" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TsK5uTxBeZleOHR5IrLre17ba4E0Ij0RsO7FFURHD7UAlywPe_sYomovCbkMalYk7_tqcVVnAXsA2JDs5iumGXomarYrGewDQZgJQ-nt2qz8K6JLYz16WK176PZNH-2KpTM_HG2dHIqdkNAw773Ocw1eQqVzBhAQOZPoCGHaoDfJKwrUw2cuUUN1c6ltslNs4UajMSWeLWCl2fkoNGyGFUwHZL5vZKJVINErPC0Qeo04tSDFht13ygpYaJMymY4YSlnd8p3y_6wkJ-04UTToH7av53D1k5DsFyGebRV2OzIczeoeWs1ThSOExeozq6jYjpibvNrMd3IlOmrvbCKkAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KRUF28L3bTOAbdrxqaj4W8E6FEp3l4JKV5Mh1pcy1BoC3ENmRkv23iYPuAsXdcH4NIkQJlpaikh7cofmqjfwpk95hmADdqhXn8KyExzGsBGneGorxvWOdhkonRYKU0EeYIbm3J-2LrxLH9Fp6XINkpFnOOlhDLy_G8D1kjVngPgfbqFQGHpLZXQNqQ8K6ltao0J1NIZnPW7M8OcRD8L1BGJhOqWs-eAUXG2clpsJLUXxKAn5Tm5582Eg4S609PGImrMo3FU3KJm6mTiNy_Tp0OkN7wiyTPdeAf8RpNAHtgwhrl_-QQFoOA32687SUq-gn39iBvKJ1cf8f2H_Lq4XoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=TZsp7CdMyaLIW97AAUIdaqmyta0ohVGJl2pjMI6e_IOGn_9DUOrO6b0QaokndLjZ5KKdjqk6KCy8G-B8rPASYaN77R-zBN9TZBTn5v62zlJUstqCCQuvx3fJVCqzczCqeyKM3G1gReizceDt9jNj_PZDhlwO39NuIOXtlMSNLyg5nZwkxcMSlW8vpL9Qp-Mf8fKGo30jylXoOW53emz6qaYq7J58YonVZdqnOz-H_w4zI0wg1r7VZ0nUQlvC7eFsiQkVb71Jj0T6xQx5_eaiDQa_n37-IAqXvnpHeqN3cYfebvFnpAXQHpDkTtaUUxrSM547AVJLL5KLE6jKMq7FcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=TZsp7CdMyaLIW97AAUIdaqmyta0ohVGJl2pjMI6e_IOGn_9DUOrO6b0QaokndLjZ5KKdjqk6KCy8G-B8rPASYaN77R-zBN9TZBTn5v62zlJUstqCCQuvx3fJVCqzczCqeyKM3G1gReizceDt9jNj_PZDhlwO39NuIOXtlMSNLyg5nZwkxcMSlW8vpL9Qp-Mf8fKGo30jylXoOW53emz6qaYq7J58YonVZdqnOz-H_w4zI0wg1r7VZ0nUQlvC7eFsiQkVb71Jj0T6xQx5_eaiDQa_n37-IAqXvnpHeqN3cYfebvFnpAXQHpDkTtaUUxrSM547AVJLL5KLE6jKMq7FcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrvuV23UP9IPYvC_-x8GGwPtwy3dLvazKFaAFBVPsfd1BbWxT_GF6Hf9UfkIRG5RvbSkcPyYDMv0uCSMLPMwaSIvwFp-NaKoudELflIec2s0dpZwwFtT54KXagvfj8HcJunUPucIsuIbZDg8_o-w3TkZcgsGJkkKgmvmA3qlcJzpREWHgMM9NfMLIu2qULmZucuHDzU9ZeY-YnqWt08-EeHGkScuYISfo8EJZyxTKjCUvHUgRpZoPuo6GhyOA95vgFXNUeFhrBF2x9RxmNlzzS75mEAgrIg39Ex-6WJHqTQVvdTJn8LcvJpldR2uOqXkAzYFly4w4rmQgYjut0qZ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=cSqM8OHFGN776sgOZ4PhDP_rWkBi1VvcgQnruOG0RuyHRVbjiTeyUKrWUeXtQirenxvAnU_nm6uAdNZWBVUS3B6YnH_cvT1Gckahm9rNf4ftxBS3rVMosvXLEDcv126JP5y673JL_S6lQuHuD5Ow7d3Wt1OqG8R7kH4HiifFYOXy8JMO-Yej3q-3q95Zx8E2fmJE4zGkMHj0Hwk3XUKVRsp71wq5kCXnOHTert8piuEjytsRci8NQo7ueQPMaaDkYKByCRfLnf8SgOArBZ2aA3O_C6eKFd6-HAb5xEeOtz8abuYmtNtDHevC8THg-QjS8WE7wR6a77rH8X_PmYryfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=cSqM8OHFGN776sgOZ4PhDP_rWkBi1VvcgQnruOG0RuyHRVbjiTeyUKrWUeXtQirenxvAnU_nm6uAdNZWBVUS3B6YnH_cvT1Gckahm9rNf4ftxBS3rVMosvXLEDcv126JP5y673JL_S6lQuHuD5Ow7d3Wt1OqG8R7kH4HiifFYOXy8JMO-Yej3q-3q95Zx8E2fmJE4zGkMHj0Hwk3XUKVRsp71wq5kCXnOHTert8piuEjytsRci8NQo7ueQPMaaDkYKByCRfLnf8SgOArBZ2aA3O_C6eKFd6-HAb5xEeOtz8abuYmtNtDHevC8THg-QjS8WE7wR6a77rH8X_PmYryfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=QA-Q8-dPUr3w8EiXspIyaiidz-PkYGibBebSCCx60AOzAiCIDigVPWVsy2wJQkUDde36hnWJDTEQ2a1i_khXjYBSclwPSWq_EJRC6vmlmLhTvc0-93BTJcs3-_LBjkCsDlJsTXAOlrMntm5jqOph81Ake6JRB5giw6RTUo_Serjw48ER5VQOUEKYF90peD1ck3HtvKJcW1e68wr0D4cKmKPiJcfpGfMVBLsk13L_s0qjwbLEGVydMcfOFJRErcYFfpCSysb6Vtfsz3GMoHZl9l4SHxUk2v2PEVm4f9dGa_qgivIlId8WcmBaIWUNQeTtInTKeAokBkPIazU6n9S7mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=QA-Q8-dPUr3w8EiXspIyaiidz-PkYGibBebSCCx60AOzAiCIDigVPWVsy2wJQkUDde36hnWJDTEQ2a1i_khXjYBSclwPSWq_EJRC6vmlmLhTvc0-93BTJcs3-_LBjkCsDlJsTXAOlrMntm5jqOph81Ake6JRB5giw6RTUo_Serjw48ER5VQOUEKYF90peD1ck3HtvKJcW1e68wr0D4cKmKPiJcfpGfMVBLsk13L_s0qjwbLEGVydMcfOFJRErcYFfpCSysb6Vtfsz3GMoHZl9l4SHxUk2v2PEVm4f9dGa_qgivIlId8WcmBaIWUNQeTtInTKeAokBkPIazU6n9S7mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5Seoz-zagGysXCRX6_6PsE8Eq7F5lsEW8T4K5FrpCkHd0YI8BKJBdJ6n5mtVrgsPBtiPNYHoKYJylGk18b_jSVUULONb7sRW2415L6-iheBm0ijRrhjXAYBjnXShZMHDzyGh0crF7yoMI271WLbjJx73jbjw1tay3CM1-sxJEcRut5rtpDfsDpaQk1MPGJ3Hs3ipkS8jcxXvdRDqV9XV0Zq7zoIv4Q-J_kNZzdlsvPxtWvSVx7vGsB3l3bdOJ7slVe-4Gh1MIfAQEKPvgcfl1apTyHtQcOlmpxqsG58hCeP4BFjrHhszmjCfw9Ng_q1d1cS971MYUsDEircyM_jig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما
از دولت لبنان خواسته بودن
که برای آتش‌بس، مذاکره نکنه و…..!
به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره
(که بعد بگن دیدید، همون کشوری که به ما پول و اسلحه و….. میده، آتش‌بس رو هم آورد؟)
ولی الان می‌بینن جمهوری اسلامی توان چنین کاری رو نداره!
ترامپ اساسا داره لفتش میده و سرزمین‌های تحت کنترل حزب‌الله هم داره می‌افته دست اسرائیل پ یک میلیون نفرشون هم آواره شدن!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5227" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=MGneU_N3gwEiDrlwouBr7Qoo78lFXNu5YggHaYHSJg2KjF8CRqqK1tq3WsgR-ErOYRG1JkBHwBvLYKGN3kgUplaG_20Gnt9XTClLOOzwHqrdajVu1mVWcGzFM7xgUWCOjEVKc-A11jtZvPNLcePYopkF8Uy7RTnQ4KtY5ZSuqoUQNItzn79LtL1ABgnO_TGLjXvig7zlQl1QzWNP9F1rqUgUw32PVNSDGQRBePZTDJI3vJqlVzguVH8mYZ0yrq3CLuMXjqK2fPtFyeW-GcZ7p6NiieK0TuA22a-np1IGEtoltKFcMiFYOMqrLD64X-TdXQvCHBLrtQMHEzw2gAGMpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=MGneU_N3gwEiDrlwouBr7Qoo78lFXNu5YggHaYHSJg2KjF8CRqqK1tq3WsgR-ErOYRG1JkBHwBvLYKGN3kgUplaG_20Gnt9XTClLOOzwHqrdajVu1mVWcGzFM7xgUWCOjEVKc-A11jtZvPNLcePYopkF8Uy7RTnQ4KtY5ZSuqoUQNItzn79LtL1ABgnO_TGLjXvig7zlQl1QzWNP9F1rqUgUw32PVNSDGQRBePZTDJI3vJqlVzguVH8mYZ0yrq3CLuMXjqK2fPtFyeW-GcZ7p6NiieK0TuA22a-np1IGEtoltKFcMiFYOMqrLD64X-TdXQvCHBLrtQMHEzw2gAGMpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOb34ovep-xwjHjYcdzA7s57BHyPNHtTzuZBicuXferHw2UiF4MqcfdMM-mxwzDX6WANHM9eb8F5zJ0mMZrRtEyIASGwfvGiT6zO8rCm4eo44Xo8hZOfPtEZV7HslFQPz99Yxh3fSx9-X6bplqrD--vjy-VRAktlzDBN6S7N8oeaYexIHP_vauYtlhtpRYtp-OcSrVIi3xY9pLxphh5KH5tEpAqMgfIYavZB1Th2ueu4g648q4j8_r5RLH4ljgz4aYAkTAMgvi2_IB--qZlFD5K0ujhiOaC7OaFDQAlbtm4VD63NQhJKI6miz1aMuDzUSwFmsq2XRPdojd4C9IMh0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3Z3SAsEjCqjaBxip3rMQoxIlEaotQZSrzP-ECeO4jypLuLc0zxGHp_9_BCCjBWbSmTAN4IHe2Aex-VQZX8teerxZHZvD1ZURpgeiSyFyiX2JM2_GxmTqQfrsr-wtTW-oav670PEYVu_ignp7N5Mb_i712ebylfRupo-hORjNMJEmJEBvIC4agUpHmIqKgjDD39EFuMrtRlNy7zx5V-a4fjNZ62IU-NJMKweGVFy-lNBkI6OZ0QCDqMxGJGSfrWWwlFZN8pdmCw24s8kErG0a8n9-xUIMjNjPuJ2P0DXO-GVd246JsUGCNlGuj6BKnNx8nGypx9STKSO_DB6z4wdEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iz3Ed8a5fR3AAOHcaHBXNrP5KXIPsmQ7CmgbnjxYV7TQsiY-thtaoNgUAU6exKJF055IHJR2pQXFtBlMATXYn6Sh3tAdkeiH2a3mQRbj9R9gMoErDdqs6LpllxiylX8Jb8vLJYPQK-78y1Hf7FU016yxx0cXhaNoSPQcTja432Kg0EoLHpWLu8TdK5rPEnw9L44w4RFxoSiOcltTzgBMiD9kOJ5v8nGybvW8KobEhDm6yBVN-z-sNyrgMqdxOZwUEZ-E8uPwhjiYYyNIrXB0Ywp5Wd3QBXqGNh38LXDQJOpxm2RLkAK8bNWvrwFPUTrFoFq2zXzXKIq3ZEzXMm4Djg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gSM2uF5CJEoTCjrWed0WBJ3Wm-rdkNdCM6_DWU_nDrX0AQN09_-iOtJRtUxAB77OsCqXBoejUUr1BEaZqhH88lZ_NblFB3-aSyvI0-aNOoll33OsWE5M-sUu961r84KSIWZ1xnEWjyZm2crtPutR-3Mhq4RXaI6bCxUbnQB6HHS4T1NOBWANni4gTZ6B4kNFjNjLPqjSGNv0uyhjCgRy6a__qn7zTvmIJ3_dN2MIHwG48qj98hWzaOwNfbG-n49p0bz1P0sNpPqKBkmH2f9Y7gJQQQncmiHxVlPeOSYb7S2VqnRYaTfIbYLEkGFm3qPIbT1KwBOe9XOBiLrklKKAPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pvw3wyWRBQchBUbuSwjEut4l_EjE8_6iuhyak9KrzgLDlCRgtXrRQ5nqM-66QOTKbm2VBLZE0dJ1tCqXhBpwHnEGof3fywkis_6hdGDnyBBVY_eWk2FW7p_RpwjXIWRKa0Kjk6I7fmq3jg5VH9vaNtpPHXIPa2WkVruRt9ODueNgaEHQTEMNpxm-NXXRBs5-Mp-dutyO-HgDJ1Fg-zMOt5O7IAPuXbfkzTlXyNeacjXyDzdocczk3MHLkvY4nroqL1C1UN0ZWIwH5x3JA-owEmbR2zeIjPBqcQ47yzXlWcV8S8ZwdrIb7mFkRhlXNSo33NrpMD98LJlahvWzWLRKIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتون رفته میخواستید برید
پشت سر خامنه‌ای در قدس نماز بخونید؟
که شما تاریخ خوندید نه؟
تاریخ جمال عبدالناصر و صدام و قذافی و بشار اسد رو لابد خونده بودید
که همین هوس‌ها رو داشتن!!!
و به همین نتایج هم رسیدن!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5219" target="_blank">📅 18:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5216">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oqCkKIs0NYfpr_W8SGrWsfcTW8COJYfXHx4wPPWpoKpg4-WJ9gsTQGrSJvPqx2cKwUeqIhrxhzqCukDicKflzjHvd09zg1COPpbY3whgPvGQc3EbZtvlE1e6YoQ-aBoxxNGaaOg97ARyAARHPokzV20McfAUBocLJuBrwTcsiYElwKBVaLLQYQrHCofX_EQqMgX6Jkaz0QSI-J505XMxHN94lZRLgEHjsmYY1VIKVe-hY6vA_iwK84ns0P8RHkO-zsO-3DmfoxRUNda_ctxRIAgAPzX1uQD0ZJ27NlaBl5E16L-OKPEZP609mQPUOnl3Rl4g96LWclCs2JqsZDsTkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2TkS5cRnuexka-9W2xjjZ-dXVQf0roGQXBhmVw6zX0g_eFhmoDpo5WNKmscoAcY5pLtHSnebA8ToG7XEiMm-2wrbmUtY1hI7kYovKXyEKHK1HD_PIVW4QO5ixAY-8fgYzukNCutbKZIkhlIyyPaNGBIvORD5ihe8L8TSSEgYk6mkiJOHif4ojUCMGNkc88ev2c5S_U-Q5FpOISdbJs6zEDjSaJFbFOn11H-KxrHowhMXK7r1r9C7foVw0fcVOviDIcE-yIfeCtwt8Yjncbb4M32KVmsKFkOAdxsSl3HeGLauA2pVt9yHc_0UTYZXew1O2LDW7iSVW45xY2QYxyq-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KZLQuBH09Ek6lRRymdDrhmTHRWJVknY156JDyA_VLOmMSrcwUgcIoXSPLjCZUbIKH4yfU3k_1ZMUNtKklrscn_PA66ZFci2je6_pHzg3L1jT0BXWrOqJ6SmXoKp2-oL4k-Y-fUkkxFW1ukWlcnzcK9f3Q07ecFtAsDPo4mymS-JO2wUCh2OhJRI4rwd7SqDgOpgpyqrh20zVu0DTGlylmyhxsorwbza-5Dc4ope1RnMt9WRiKS51cBxenoIe8GX71rCvmgDK74fFuUgwB6GyJ_TTcvCu2q1UNHa5UhwlPW2OgYsrrLsaXse6x6DkdWKL1N3eo4DQfS-RQqOZEJpiNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=NuA-TtI25ixhpEcf4Ybb0prt9G5WiFofPogHHxOHJBYtzMvsCtyu0xAo3NQLLg2sCBknJoglKeXJEPNuI2Lcpi7M4vSuGO6f3mEA-zwrBnCHMU7unsSP4tdcuu1ZaliHYiMbgCxo2DBSHpltL-VB0PK5hVlcxy_jkfhXh1xsBU_bOsQ0871rxYcF_FVIOOj3CVdA6qIF5eRwncGL9rJeeKx-iYPddBxESxNSJGfLLubS68V8EVvdObCVIuxHKFUk62fb5EPZ713BN1SLCqpkJ_DhV02bSGgKPaa25_Amj1ra1P8bg9-jiw7ZhiHk3DQFNvuI9W5hVnB_erz906We-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=NuA-TtI25ixhpEcf4Ybb0prt9G5WiFofPogHHxOHJBYtzMvsCtyu0xAo3NQLLg2sCBknJoglKeXJEPNuI2Lcpi7M4vSuGO6f3mEA-zwrBnCHMU7unsSP4tdcuu1ZaliHYiMbgCxo2DBSHpltL-VB0PK5hVlcxy_jkfhXh1xsBU_bOsQ0871rxYcF_FVIOOj3CVdA6qIF5eRwncGL9rJeeKx-iYPddBxESxNSJGfLLubS68V8EVvdObCVIuxHKFUk62fb5EPZ713BN1SLCqpkJ_DhV02bSGgKPaa25_Amj1ra1P8bg9-jiw7ZhiHk3DQFNvuI9W5hVnB_erz906We-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=VFDJ7YdbvNy88auo4yB-vIFcY1Op8Y9e6tbzvTzYqp_UpXbxIeksuNkbO8esDf4inqe4wAdHKjz_vjfxRNXwipusM6MCvpzFiLOFv6QzRgfqT9UUI9i0CQJNvJBZbf6PjsNUIkq3Cv6emwsDdwZFPvxQ74ivQgi0clXAOXQDvzPtYt7xlMLW8OSw3HpYMHYsWSKQaD9h2TjEgZ2LPZD-Ch3y7g9eHUMDjliQMNF9gG5AUxFgGZf0TINHm-ajwWl4crVkApuPauujAO3E0a-4MHDBe-wGKvCyuCUOFf5SgmEih1jBYOFfxMlu17zdB0I_MC3LPvurkiPz9GTBJiVaKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=VFDJ7YdbvNy88auo4yB-vIFcY1Op8Y9e6tbzvTzYqp_UpXbxIeksuNkbO8esDf4inqe4wAdHKjz_vjfxRNXwipusM6MCvpzFiLOFv6QzRgfqT9UUI9i0CQJNvJBZbf6PjsNUIkq3Cv6emwsDdwZFPvxQ74ivQgi0clXAOXQDvzPtYt7xlMLW8OSw3HpYMHYsWSKQaD9h2TjEgZ2LPZD-Ch3y7g9eHUMDjliQMNF9gG5AUxFgGZf0TINHm-ajwWl4crVkApuPauujAO3E0a-4MHDBe-wGKvCyuCUOFf5SgmEih1jBYOFfxMlu17zdB0I_MC3LPvurkiPz9GTBJiVaKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=c71MBXQaV1d5bLkQpmcabG3ogk9hWXXtY4mNb42K6s4D5WhksSRMXv6v5WVE4Tf4xHABKajb2bDeJDW40egcG_R4a3KDHZ9iQibQvYwZVw5s_b_nr5TjinQKMQsttRBacrDNUKqz0l3O-faNL6dcH5-kq0uwuze8LrQTlTMxRnAXJ1ogGSNAxSi5dYPL9KmeT5Vih2nRrbp4godBOuqIIwlrVTdNu1wJDUzVzH8rYyQ5Kqjj0QlwwFDS7Mn1ibHLfg1bflXvKK9A6YZRbEfYO4vWXVPV6b5BBvQ4hJsyzmFicGTNvkb3a1DHaJjUktz_M8MRk992bU5E-UWgCax-Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=c71MBXQaV1d5bLkQpmcabG3ogk9hWXXtY4mNb42K6s4D5WhksSRMXv6v5WVE4Tf4xHABKajb2bDeJDW40egcG_R4a3KDHZ9iQibQvYwZVw5s_b_nr5TjinQKMQsttRBacrDNUKqz0l3O-faNL6dcH5-kq0uwuze8LrQTlTMxRnAXJ1ogGSNAxSi5dYPL9KmeT5Vih2nRrbp4godBOuqIIwlrVTdNu1wJDUzVzH8rYyQ5Kqjj0QlwwFDS7Mn1ibHLfg1bflXvKK9A6YZRbEfYO4vWXVPV6b5BBvQ4hJsyzmFicGTNvkb3a1DHaJjUktz_M8MRk992bU5E-UWgCax-Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSs9oLjok3mMYd2BJ6CMB2DUX4W73GWIEK6DXlusv2Rv2UGmDvCXZxc_Bwc1jz138zg4kHC9LdvrCDAAvmMLOdnGx0G3JczTE1l37rAljekTm3-4nrTF6wflgp3MrLKUz-UaV9xGo2pJshBhpufM7LLRys8Zfr9oQuY7fkTxlqQVo0wB-bLs36OLL6xN-LKOkRXUuPd0l4XJs4456yMUEs6Xi7oA_I-HxFDTY3afhlmk5zkfvK1JUWn7iG3QSinjRxhh8WvfgWJM5x3mW8V1AYmh406fWpZz5BHZtt705p0OCBevpfpuuq0rKRYGjS1cXVEt-k_2x8nhmkFiPjVHRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات و دعوا سر اینهاست!
خوش به حال آخوند که چون شمایانی رو داره! هر بلایی که سرتون ببره، آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی و کره‌شمالی رو نمی‌رفتید! راه
صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5212" target="_blank">📅 17:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4E0gYg0oCrv48MbaYvxBIPrXB-s86Z3WZ9ctGSNMc6EXIBss944zEq9pmFpmtF8jNuEtyJQYC_072u6UkSA9yjUEYE13pE0yZVaiYYyEmyWGeecpxb7SLyh9-xhibU-jlZd0cbZ_c48aS9YYFBNMvUCElMwbcsjxDdDS-BGawHnOo1lATZfaotafd-xVxKfgTwMoknB5UCkwSKDJIuD1h2LwTGNTeLgkJSE6RZoW6zvqHXuxVEqvSQyHRtf0CCyZyObaZiT0b7X1sJm0AO3r-qFfs9O2ABVyaAnGJ-biNZWBYilfNy5i7tqNr5j8LClQNCgIPRziLVYA0mU1EEjTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5211" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEzY7HT8wBGo9WSCY05vN5Z31WuYDNdoo9S7GnDYA1BsHApjnpZcciZRV4wSoy5880WlKgVOApNVYKtLil0n-rBErkcRgG8RNEkOB_EtpEZnOAlr6IFr2KnO7EAlgx3Q1czcEGJw7CfQQuaVqhytvJcaE5luCexQHsdwLLq4kK1Qnp1tjvcPeGPpJ4xw1L_sNSa3XyVQNz6duSDM6rVC9BolOrBHpL5u43Pwi4l2gkMq3mUCWw1ZLAKqUC164W0bMO0xPSf3DDYpA45D6e3IT_gK7bK3HnxDAwoWjjydJCI5HiBaY-9NWIIujH-QQYL3SeMCY6vjAynufwkAkdgJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnuwqyBoYySHDUIyhVW4XxMrVeAAT-SQisrAsh7Fs5xpDrE1y4aqBnPTLP5ioMKYW7bc0zpaGgoiSJV1kVLpEYd3EdiBfqp2S63WcnnSg1Lbj2jc8D2D3sCydjUH4xKk35Q1mDxv6RPAQFlyqz3dkYdvicMZIgswrHml1uqEdOIgKvMCdjhMhD0LAK_QeZkIw2SszoYzQXDPVY6OQjVIqhY5LtL86vD0KBBOXAN7QQGIs9wEwo8VPj9Q83tDFFmqVZUOtOGo99zJ-gtlkBFvKR9sTA1iPszACfLgkooE2fNAPnOwBpVDHndWwTCycBktI_CakENwI22n_nyKtMqjnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=H9I9YzkTSoDyMzuIwhDF7SI5EX-Zn8TF9bARh-BItvW-ZDXipnPnq-1fK6hsMfGx2erXBnFKxxeq_H5AWs3nEPWFffpUdnWgCXS_MFwQs9WObRjzWg_sB5p9hGk7arwFIXPv707oFeQrd41aUwOsjLSMLhM0_0EhuRCtCxUBGiTZPJfm5YuudT6N45oA3X6KPj5TEGUs3nONR1vlABuI1XI7m5bU16E9zw0J-E3TuZ8_ZOormnD86qHaO2K4GsChGJJZGDpFX1_xqBdxpuzLep61AG0RmBPtVvA4xK9lD83jAqhKDrCLUmva3lIryAkNgU6BrCp-uDjEvbq0kzwn_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=H9I9YzkTSoDyMzuIwhDF7SI5EX-Zn8TF9bARh-BItvW-ZDXipnPnq-1fK6hsMfGx2erXBnFKxxeq_H5AWs3nEPWFffpUdnWgCXS_MFwQs9WObRjzWg_sB5p9hGk7arwFIXPv707oFeQrd41aUwOsjLSMLhM0_0EhuRCtCxUBGiTZPJfm5YuudT6N45oA3X6KPj5TEGUs3nONR1vlABuI1XI7m5bU16E9zw0J-E3TuZ8_ZOormnD86qHaO2K4GsChGJJZGDpFX1_xqBdxpuzLep61AG0RmBPtVvA4xK9lD83jAqhKDrCLUmva3lIryAkNgU6BrCp-uDjEvbq0kzwn_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=f8Qm8amcdCJA3T0waocUaWMil-arOhJYK5bBPmLFr08070Qmf3ySIzS1kKinS-GhUHIOaE3G9k04Agb625FUt7eeDp5nj7GbIypo7YfjZwFqDUkZRKnn-Dbt3h6C2W4_QWzwomZRLDhYF4JP-CA-R89uB4iVrmM7U_5wrAzVFhVT7qvGIJ3Fw1iCioR9K9eJFc8qlmwYrWtfUpTs924k-U2qQw77GY0Zm-RNV-OQPdi9VV7pBgfXOG6Mwwg2GsG7pMvv4HnC8dYZHm2AZEN9oHhd5lsMKyUI_HDdNmX2GUpMFihhXc2L1sVGb-r7PnGA1itidpJtcShPdWORcFr1rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=f8Qm8amcdCJA3T0waocUaWMil-arOhJYK5bBPmLFr08070Qmf3ySIzS1kKinS-GhUHIOaE3G9k04Agb625FUt7eeDp5nj7GbIypo7YfjZwFqDUkZRKnn-Dbt3h6C2W4_QWzwomZRLDhYF4JP-CA-R89uB4iVrmM7U_5wrAzVFhVT7qvGIJ3Fw1iCioR9K9eJFc8qlmwYrWtfUpTs924k-U2qQw77GY0Zm-RNV-OQPdi9VV7pBgfXOG6Mwwg2GsG7pMvv4HnC8dYZHm2AZEN9oHhd5lsMKyUI_HDdNmX2GUpMFihhXc2L1sVGb-r7PnGA1itidpJtcShPdWORcFr1rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfbRYqKiFKBSLeRvgXr3hQuU1p9P_T40WyhXxUtc4xDxUZ0HjXaAR0Y2ny6gGAmzldM0-OzbD3zARMaGIYtt_HURODvXWpEnkhjtWL5loEIpTDWARag0JOO7C4UQh8MEjvl-OM_YMDXPh5T4LS2vn6P7mRPxYTGH60Rcv7hpjM42ETbDnri8IoCAnLI1t_jn7dopLxO0AEtYXNmeVtfhhUAbYaxeQn8lVkIjA8zcrYTnq1Kp0AuSZ13pthqE3D9t7BfR5mYavE2mPtZUBbPNOpPreNGyxkoj7MFtTvprfuHKq79KroxB_JRK1_GFUSj7hE4elLPnH6Ht9b-XhWf5eA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXfixRDcypFMdEariBTkg45nq1YXs6b7_lmO1ekUrE5A5CUR7IucqP5nbZrSSMoBw-r1Ub9bYR7ajBuFU794XRdqrtJ2uM0sjCPthE6vrLo0HRD30N2bNImTuCjL3fT9-w9jrO2c2GTcCkPS0uLLrFd-d_RJrLR54wkxRhj0DgNgzIgeoDnEh9iNWZbIqeQitNoN5_bsPoLT2DDtXT0UTdy5IiU-MEZsydvwQkuOZDnEt9iaX3MiimIRYbHglL3h1S8I_rxSSdgwcq5G-HvYDUvJq3WUdYJsT9RkJv9TTYuPTOq4eVDq60ALMn3iJquD6ESDg6z7p8uA2hzEBGGDjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSeim-fBiw1DEAk6U23WA0_LPxvOo0qlf4s4omWtb4fRHvvEiFxylT6eMVe58Q3uFKeUOyr4q1y5hboHhundZL4Ba9zFJWP5pg4vvpEfKTKj5zq0mOTHBtTejakBUJrNyooRM2DRNiLF8fZTQuESjFKFD5J6crcBrF3jOGbNBbBHzCIDwh6CjA7sWZr9Uj8pUiA10gKCbjlvDdcXogWU0Koke0FmnbSnpdlHk6eUAFKqamWIDVbuOqwIkdndBvSGInHezeY_lPAEBzAtSQ5tr88392efIELsiSRx_ydgWQ5bsKJx9zgxVHRsxLunIMTN_BJ_mc3hExdHc9mOtFJqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2a6fFzCTBYG03G66epXwc-C99QfjqNWluYy4b2fxqTyCQ0ctrK2W0U57Ey5EXlkGxizJAXORYFXgiopinNO6gmqjFngKhcyvtnjc94BiPZERXUPpvjd7DqDQiiLCIrwFx-d4XoQyhAm8bLfm0Yqu2s6Lz6MrwcjQW07jZjlyt030N4DK7saTwJrfQ1hyalJt5QcoKJwxtHYQn1ke6pshBXpCig-j9di9L8ki7omJ-f7akXmvz72HU5Rx06QLYTNNZ9OB0gtlowcfAbLFRF0r2Xsh8RMXbB5ocSmDP1b9akhl3rMWB42RxrSdFXN9BmKGdmrInOndSGZ8bnStSrsug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/COd7e6-20SX8a3XBWShKb3Eeb7yj_AKNMr5JFLfyogFVXnIqq26gbWKeF8cwrYwARqpe5RF6J_7VfD9BtWYD_YGqxlUb5YHatr9RpIBMGM6AX6dvV8d1BthMNJTQ5YqQrj_zqyzy5O4tB0Xs_8lGv5G6dudlpNWFrcA0cETHquZFBHMwmYslmiYXNT4ggbRv3jdeTzmROXPuU0ybfztnT78WRHsfKqEoKp9jYXmPriuNVEyzKZpg40ZaU_Up8cDytgd9RFjTtdWy1bwqN8Bb937TxQwHMpqZvAyCUTROennK95bidJb9XwRk_u2CEunTDpAenxIYhNhU8bswWtRrow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z7mX9PuE3KsnKMqEWyEiFfgBPqTv5jfzeVeyzMUi4apVEGCnQaOpvDaov3EN4-wvZL9TswgQKebjgntpp1paffDG2mjeSTJZPNxAmL4yOb_1oaktyp99ar5Ast7V9_PWUxvQvpTxh0uB02z0SJWUdchgGSQGIVo1BYshdIX2lsVvQYG3ymHH7zkmDiHaYGGr_fAxpwjALf9J2WZsFULIaZG7wiV84XOvRraKvrvXsfYHqxIC2vLD5WvJYGoNZaeJshjF7qdxRpK9002Ob4txm9LUeBjnAcMBBz_qgCTmDZ0o5BQhf5gA8i0P14Hg8MDAT8-eZLkIpEq717TRHYcfsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egDgncMbVbfgEmuemBz_t4N2o52zY28bJ-2HWv3mQq3LWAY4a16oUSk-2Zh958FxZG5HKy9or5kQ9bBuzexjjwfx1p6soR3yStR1A8cb2DR-2APuk5TH7Hup0HwEJ-DrwV8xL5pOCH-5AkJGaq4fJMKjkEtQoSX_OKdp90EZeiKt4YNIh_s4HltlOomwCPCXcoW1N0wP1685lRL26ESq-lnQ8eLvWrhNipDUGn1c4W3JBQ89DJyL8d7TOsoEeyxKy7YEuklfu7cUMD3MtuukdQ3MxFB3CT-WEKsg7WYCNeL4sjJG2_J0el00ser0RulwYUPxU9WR__rBuIm6XRCdZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGUfGQtl5D3j8R3PtDiOAjtgW7ZcNbGf0OXWyFzy-myevUtIa_YTQTzL4er7Qsn7XXOIXspKrhDNUgJ64-9rNzXsZsTxPmwwCGW2uFcy8AyR9Us0zUf3kpn2g0u7dJQX9EaL_HR2HnwpiRSoTp_qyA8XPgYsb7RPNYsj9Cs9ob0EdTP0KJSIoAtGyVVU71ahxBKZ130vyGprjtH8qBe0cjMmqRxd6T2a_x3ZFA0iCSDnYtKtYbqlmitv9qlSETCKPvUemuKbhsT8DsqueSwhwcoS9dm1LKD4TM-IKUr9EaJ-V-P2Y06Q1INDgidXUYf2Te50rYvBezOIuya6XSivZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=alw0xYreq-oM6IjLlFfOO3qIbUT7w60MSkGaUIef4tqUcETwZKvT32z-ywSX5ewmFmQ1oxRLXyVpt9-IeBr7pOLQwE3BPEfL5J4NYWJG_vEGNCf91YyEVfwyLBEyAEErp-ulCIdwUMm-wtVhpnlNqR6O6oPUP_v2q_rxu-kIdPVriT88BxyysFuIN3OUa1qyfWRqGm74q5iBr1c8xEUalDLuMTXEvqOhJggLxkyjHCla62jPe8d02kOehCeF7lU0PkgRMaHnavsbC7RUBacKuCcm4xjRhEF1ya8Q3l5w0WtG0UU1_tJayLbrOba2fxwyeVb7bKYL5Z7isucY8bQGjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=alw0xYreq-oM6IjLlFfOO3qIbUT7w60MSkGaUIef4tqUcETwZKvT32z-ywSX5ewmFmQ1oxRLXyVpt9-IeBr7pOLQwE3BPEfL5J4NYWJG_vEGNCf91YyEVfwyLBEyAEErp-ulCIdwUMm-wtVhpnlNqR6O6oPUP_v2q_rxu-kIdPVriT88BxyysFuIN3OUa1qyfWRqGm74q5iBr1c8xEUalDLuMTXEvqOhJggLxkyjHCla62jPe8d02kOehCeF7lU0PkgRMaHnavsbC7RUBacKuCcm4xjRhEF1ya8Q3l5w0WtG0UU1_tJayLbrOba2fxwyeVb7bKYL5Z7isucY8bQGjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=XvNjDYOto4t_e56RHj3Y-nBUy5DB4CXId0zFw5lqM9PuEIJERYHUW6GJmoC8SVkGMhaMLRtYyjiAicTm7L1DBbE2X_ULkkUMAVzEabnBKXAGLDRyDAiPLw_zG1wCuQelg3uf8PGoL_RzceXihevJn5wVRkacq72y55HLzCAJefU2_hkonv3QCNpGP1jR69PEA80FgKdO_vjq6H3U_UH45f3bHcXImvvnvq3TWohwhfCgFhymDZbP9En45ROn9ibSVPf_KNRkOHjEWG77PJMjAP0valGzOAATZ_tKNtgMx57mAsrIIgoP3esfnhASMvNerS4S5z7c0eWmUXtoTbq-2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=XvNjDYOto4t_e56RHj3Y-nBUy5DB4CXId0zFw5lqM9PuEIJERYHUW6GJmoC8SVkGMhaMLRtYyjiAicTm7L1DBbE2X_ULkkUMAVzEabnBKXAGLDRyDAiPLw_zG1wCuQelg3uf8PGoL_RzceXihevJn5wVRkacq72y55HLzCAJefU2_hkonv3QCNpGP1jR69PEA80FgKdO_vjq6H3U_UH45f3bHcXImvvnvq3TWohwhfCgFhymDZbP9En45ROn9ibSVPf_KNRkOHjEWG77PJMjAP0valGzOAATZ_tKNtgMx57mAsrIIgoP3esfnhASMvNerS4S5z7c0eWmUXtoTbq-2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dP-_E0LfvSt2-HHxAasn4dpOG0Mi27WGKaEBkKNrQAhl7JQ_BYzVzvY9jpurFQDXhwYTu1tw8nqmS9xeH1YHMDhmUK123lHBDXpc95YsPf81vExSVqNhOjeoBXCbwoAjFx2BI6AC1RFViqCZCvDqfZCmafn9b1o5s1CllPmSs-kZ5t96m3eW3g87V3UkDvIp-_FQ_2lkIshMG6QNwp8i1kTyl_GLgAavv7h61rmhk3FZZfFJYKiQgrJ5BjhzVx7iVXq4UgtFx6gZjOmUa4F3Qo-wCsgG4IymNE3FsbKuXHeO5psQH2f3h1618lN-2DCk1SiysAMkuKwLJQHF6rN4og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E0ngoB4gAsLmQrkQXkyFNazzJfFGiHMO6F2g_9CPkHmTe5tNSs09WSr67fZrqTio6JBO7KTubXfAV7v-97vTXQ-0k4Uz2dCOQS7yR0cl-_0T45FJHSb1bOP2MaBk1FJIUWbnu2EBBbz-3H_x_HwZ8e2EhZ1ASuReB0RzzVyr3ogBkKg77Do75OMhNIQPf56A6VFfgFb6ha7IlCOF4MCq4oURIi4J6QwzNdQP71g94HP4QkMQefPfYrQLmUcXVWo9vEBFsZvtbYRg4uYuZqwg_4Qa2AKkRMODK2Hu0WlC1ac_VLsdj0-W5A1ltsEneZwVnJ56UIG0mGWxIWT94SN-kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=lXhyyvvqWO5E8tIV4fbKoCftyLNg8LGoCgy7Y-yUYBxkJSqKVLfNYPxozBYDeSTt6rbOHkybncX5y4X0Rpm3BSu1etDUDKYRgQP3JSOogxoHiVOBm9MV6BlQKjP--k5mqp0DFI04Vkv3jsNkkqTcDb0xeiWQWV6pVWEwiIPZZ7gYgQrOeU756HWeg_et53JMDELj1i2iAoLxRGsv0RciXSHWxTAicFe_uGzVkKq1Pb6V5kOMJInhgjBeQwaMLwx5A7x0Y8KLnNhbvNja87i-fhjlK8fX5UHeCIzL9fTu-4LOjMDxZ2Msas3WLpr3vD_xe9nXuYudziwQmT2dQk3LMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=lXhyyvvqWO5E8tIV4fbKoCftyLNg8LGoCgy7Y-yUYBxkJSqKVLfNYPxozBYDeSTt6rbOHkybncX5y4X0Rpm3BSu1etDUDKYRgQP3JSOogxoHiVOBm9MV6BlQKjP--k5mqp0DFI04Vkv3jsNkkqTcDb0xeiWQWV6pVWEwiIPZZ7gYgQrOeU756HWeg_et53JMDELj1i2iAoLxRGsv0RciXSHWxTAicFe_uGzVkKq1Pb6V5kOMJInhgjBeQwaMLwx5A7x0Y8KLnNhbvNja87i-fhjlK8fX5UHeCIzL9fTu-4LOjMDxZ2Msas3WLpr3vD_xe9nXuYudziwQmT2dQk3LMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdj5oyi9CBMRSr48_h_nI50PSrnSJ8WmToMHz4hj5KpI6zrZmUrs0m9_59Y8v9ra1flzu67nLc4FS6dy2n5IaRUzvxQzZ7tgAVDYlrYrMSc9kw1kPeXhMN-O2FgIcWR2c6B7xVviYgHKtwsvenAhGz8fNxytoNum8aabM5BulkszybJVT6o3Mom5CBr9tcXPN_qcN5_RKxUIVAm6Xwx5m__XNwbbfKwP3Pc_otXLdUP_5FpuktRGzni45hVwSvSGsPhavLL-wwsILkBcurapPv0tHqQY2ta1-ldgSivDQp6PZMdKwlifyCkf7YDMO2S7VmpLOAy4VxWMZ0Yy155-eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏حالا که تشریف آوردید:
‏از ۵۷ کشور اسلامی، فقط ۸ دولت کشته شدن «ولی امر مسلمین» رو تسلیت گفتن و ۴۹ کشور سکوت کردن!
‏عراق، آذربایجان، تاجیکستان، پاکستان، لبنان، الجزایر، عمان و قطر تنها کشورهایی بودند که تسلیت گفتند.
‏بزرگان جهان اسلام چون‌: ترکیه، عربستان، اندونزی، مصر، مالزی،ازبکستان و… سکوت کردن!
‏تروریست‌های طالبان هم حمله رو محکوم کردن اما تسلیت نگفتن!
دولت فلسطین حتی حمله رو هم‌ محکوم نکرد! سکوت کامل!
فقط تروریست‌های حماس محکوم کردن و تسلیت گفتن!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5187">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های جمهوری اسلامی  از بستن تنگه هرمز خبر می‌دهند.
🚨
🚨
🚨
سخنگوی قرارگاه خاتم : به ۱۴ پایگاه نظامی آمریکا حمله کردیم و «صدها» ‌تن آمریکایی و اسرائیلی را کشته‌ایم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5186">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حمله به بحرین
😅</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شاهکار جدید صدا و سیما  اینها رو باید تلوزیون‌های جهان در بخش سرگرمی نشون بدن</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5183" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">«دیشب مردم تهران در کوچه و خیابان  کل می‌کشیدن» مرسی از بابت این اعتراف و این مستند سازی از وضعیت تهران پس از انتشار خبر مرگ خامنه‌ای</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5182" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5181">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=IfraHosUIEVmNY-KfMT0cJRgtRQ-aiL7D6dUrjP7kBmgelLnuoXD2_Bk8DNf-SvOEWFo8IYVFebTF7OZcuvtfg_x68rF9MwcaT87QwZ4CLUSpM7RpFp_tNT5om5_c8Bk4OTjGR72lwWIdv1DcAIvbLmzA6BECI19sdKEookT6i7t1QLFpQQUoY51FS85pSbYW2AUAsFoWvxkzE7Xei82d6ysXmJj6LoYfn3CW0IbEdytKW_H-Kbyriegqfc6Mlo7sKqGvNTg1Y__GXZHFWifo5EnDMfAQsInQ10JagpR5SKyc9agu1mZTkWze61nkgmLWvLq-rfAfC5dUNnpzTj-VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=IfraHosUIEVmNY-KfMT0cJRgtRQ-aiL7D6dUrjP7kBmgelLnuoXD2_Bk8DNf-SvOEWFo8IYVFebTF7OZcuvtfg_x68rF9MwcaT87QwZ4CLUSpM7RpFp_tNT5om5_c8Bk4OTjGR72lwWIdv1DcAIvbLmzA6BECI19sdKEookT6i7t1QLFpQQUoY51FS85pSbYW2AUAsFoWvxkzE7Xei82d6ysXmJj6LoYfn3CW0IbEdytKW_H-Kbyriegqfc6Mlo7sKqGvNTg1Y__GXZHFWifo5EnDMfAQsInQ10JagpR5SKyc9agu1mZTkWze61nkgmLWvLq-rfAfC5dUNnpzTj-VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس پاکستان داره عزاداران خامنه‌ای رو با چوب میزنه  دیروز هم پلیس پاکستان ۶ تاشون رو کشت.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5181" target="_blank">📅 09:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بخش خبری ساعت ۱۴ شبکه یک و تکرار ادعای زدن ۳ جنگنده آمریکایی  در آسمان کویت و تکرار این سوال که چطور در آسمان ایران به این پهناوری نمی‌تونید ‌، در آسمان کویت تونستید؟؟</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5180" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">فرماندار جم در استان بوشهر، می‌گوید که یک «پهپاد متخاصم» منهدم شده و وضعیت شهر به حالت عادی بازگشته است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5179" target="_blank">📅 00:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از شلیک موشک از منطقه جم بوشهر به سمت چند کشتی که در تلاش برای عبور از تنگه هرمز بودند.
گفته می‌شود در جریان این حملات موشکی که از سوی سپاه صورت گرفته، به سوی یک کشتی آمریکایی نیز شلیک شده.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5178" target="_blank">📅 23:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=SmsLMLpFld0X16CWww6bqv1jZ3vYgg71oemijmIgQtfHJa6BpufwWm95wqXsxagTGIP_x114PMbOQBgNMGjQJ9mtyfaM3GB9D7Ur6uFXgBmSZcWjSciUPVunyrpcRDh-QDPums4H6koIKxCHNAOYSSIVsSELzQKCX04bjZwOBF0FhIk2_VUgj6fYS6DqvFSsCRkkFYFILNmjh7tPjvEcRS5hCsbFVE-r7MTNXcpwXoS25lRPHnaGCGZ_1g0RI6tdfG2rF1-LDc5BdTBgPpeui-qU9Z4BPMOsahOwKXyYO_48cl1ELA3jbWNM-_008v9WEUFV1NgrtfQFhKjUU8ajQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=SmsLMLpFld0X16CWww6bqv1jZ3vYgg71oemijmIgQtfHJa6BpufwWm95wqXsxagTGIP_x114PMbOQBgNMGjQJ9mtyfaM3GB9D7Ur6uFXgBmSZcWjSciUPVunyrpcRDh-QDPums4H6koIKxCHNAOYSSIVsSELzQKCX04bjZwOBF0FhIk2_VUgj6fYS6DqvFSsCRkkFYFILNmjh7tPjvEcRS5hCsbFVE-r7MTNXcpwXoS25lRPHnaGCGZ_1g0RI6tdfG2rF1-LDc5BdTBgPpeui-qU9Z4BPMOsahOwKXyYO_48cl1ELA3jbWNM-_008v9WEUFV1NgrtfQFhKjUU8ajQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=qpTIHNzn_ZEh-vVyoYkxSGuyXVkN8LPF6r6Zm8iOky5rRIg05DqU7tPSS-9fxKKasSZlIadd9xzEQikhDAi0kfMkg9pBMRc6TNAyr_XXHp-VG-MvBU6jWFuz-hmLjkwLCE8a42kc-RnRuR8ntbOMreJc9wnodX2cfMdtVqIVV76g9SzpHrrl9hGvsxX1y7KGHVruLn9ojGYK3zP4oJ0YZIu2LIR8PlO2-NMo_J6BvZV4eeYoZBD3KR4IdGBg_3G51kAfFQ8bJXSr6vW-lEQf58vX1dhAfiUiokcYmKs6ARR-t83BZncbgczlsZ1ytNcSF_JdfZhV1iySdPN9wj0hvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=qpTIHNzn_ZEh-vVyoYkxSGuyXVkN8LPF6r6Zm8iOky5rRIg05DqU7tPSS-9fxKKasSZlIadd9xzEQikhDAi0kfMkg9pBMRc6TNAyr_XXHp-VG-MvBU6jWFuz-hmLjkwLCE8a42kc-RnRuR8ntbOMreJc9wnodX2cfMdtVqIVV76g9SzpHrrl9hGvsxX1y7KGHVruLn9ojGYK3zP4oJ0YZIu2LIR8PlO2-NMo_J6BvZV4eeYoZBD3KR4IdGBg_3G51kAfFQ8bJXSr6vW-lEQf58vX1dhAfiUiokcYmKs6ARR-t83BZncbgczlsZ1ytNcSF_JdfZhV1iySdPN9wj0hvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
آمریکا و جمهوری اسلامی به یک توافق ۶۰ روزه رسیده‌اند تا آتش‌بس را تمدید کنند و مذاکرات درباره برنامه هسته‌ای را آغاز کنند.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5175" target="_blank">📅 19:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208f980645.mp4?token=AI8SEOSnDgYIrmWmOMqC7eblkabQRnFr1gYk1UAFEfPe04ulbOgE2JvCFSSsHJbEquDYk0F7WbnY69kNMP7pBHqTcEHg04UEYv25-W9aByHstNXyZrnT8xuXvozZVWRaHMbPo--ZMqtsWAJRkjnAn8tWwc7HqCrpgUXSg7vzSruxhcAtdxEI_nW1Ncimy1zU_LbaJGbIwWLTuPPZsHy6_-fZqnIc48K9M2Lzc083X6GzAs9QR62c2djQ_i4UynyLgZ5Zpcp0u6b-JMoDL6Hcogty6qrfk6MkftfKBBl4hKx0oLPZ3-jDid9qi7JS3i2ZaUuYgNBG4utfX2NODdaxSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f980645.mp4?token=AI8SEOSnDgYIrmWmOMqC7eblkabQRnFr1gYk1UAFEfPe04ulbOgE2JvCFSSsHJbEquDYk0F7WbnY69kNMP7pBHqTcEHg04UEYv25-W9aByHstNXyZrnT8xuXvozZVWRaHMbPo--ZMqtsWAJRkjnAn8tWwc7HqCrpgUXSg7vzSruxhcAtdxEI_nW1Ncimy1zU_LbaJGbIwWLTuPPZsHy6_-fZqnIc48K9M2Lzc083X6GzAs9QR62c2djQ_i4UynyLgZ5Zpcp0u6b-JMoDL6Hcogty6qrfk6MkftfKBBl4hKx0oLPZ3-jDid9qi7JS3i2ZaUuYgNBG4utfX2NODdaxSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش زدن ظریف :)
نوبت عراقچی هم میرسه!
این مسیر رو خیلی‌ها رفتن!
از منتظری و بنی‌صدر، تا موسوی،
خاتمی و روحانی، احمدی‌نژاد و…..</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5174" target="_blank">📅 19:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=sOj0WzWHhfBF8q-EFZIUgHvnuCKOYqyh4RoXBX9DKskzw4IzpI_XBkBWdUiK5YcioAf83Oo0lyXe6jF7RqILTGWBnExWFDvbil7woEPrXNfiqL3HWFT7LZNm_Nj1enC6m6XlEoTwDacGuuej3_nMN7giKE5Cqxe0kFhn8ckSd_dUIF6_6BqC99pssK59olk3m07qSDbbwieXvZwboHDnwW-Dm5K5GCey5XypNKKwmz42WS5GjmWeF2KyjJTs0j_1bu9F7IL3C6HRbYeGJk2gCII58JN1HlP2KyC6XWSN0hMQQiJkUXXAjp-7jRCkgsmsFcx_O5BHSsPgZTHvrKjdew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=sOj0WzWHhfBF8q-EFZIUgHvnuCKOYqyh4RoXBX9DKskzw4IzpI_XBkBWdUiK5YcioAf83Oo0lyXe6jF7RqILTGWBnExWFDvbil7woEPrXNfiqL3HWFT7LZNm_Nj1enC6m6XlEoTwDacGuuej3_nMN7giKE5Cqxe0kFhn8ckSd_dUIF6_6BqC99pssK59olk3m07qSDbbwieXvZwboHDnwW-Dm5K5GCey5XypNKKwmz42WS5GjmWeF2KyjJTs0j_1bu9F7IL3C6HRbYeGJk2gCII58JN1HlP2KyC6XWSN0hMQQiJkUXXAjp-7jRCkgsmsFcx_O5BHSsPgZTHvrKjdew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=AsrFgpGtul1kjyHpYXEPtK0FMsMUcVXgANRkl3-8QTqQ52MgOFVumsY2ZXXR82QoOMy2kbBlB2QJlYbkB8yr6kSxzEr0rguCXo7X8NV_AIGEcAiw9kblV7SyCCF-FVdXxmWRwgblUqhzKr4ePQRyCe9nua6V307y6-LxfmRt5KKfxW_u1sEf_6dYm9CFNCfJIadApEU_SoiGTqh4rRzkP3k4LWxnqTFO-pUIm4FiLxPwUeVHUmNTCjWRIjU_xcckDMGRVm9-RIGVntaRhteq8BMNiVhgCJQMXKO68GJawavHtX-ZgDuCSVnU6rqZTmkVHw1_t8DaHU8UTFTz02fesQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=AsrFgpGtul1kjyHpYXEPtK0FMsMUcVXgANRkl3-8QTqQ52MgOFVumsY2ZXXR82QoOMy2kbBlB2QJlYbkB8yr6kSxzEr0rguCXo7X8NV_AIGEcAiw9kblV7SyCCF-FVdXxmWRwgblUqhzKr4ePQRyCe9nua6V307y6-LxfmRt5KKfxW_u1sEf_6dYm9CFNCfJIadApEU_SoiGTqh4rRzkP3k4LWxnqTFO-pUIm4FiLxPwUeVHUmNTCjWRIjU_xcckDMGRVm9-RIGVntaRhteq8BMNiVhgCJQMXKO68GJawavHtX-ZgDuCSVnU6rqZTmkVHw1_t8DaHU8UTFTz02fesQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله هوایی اسرائیل به بیروت
🔺
آمریکا از دولت اسرائیل خواسته بود تا به بیروت حمله نکند
🔺
گفته می‌شود که در جریان این حمله، «علی الحسینی» مسئول ارشد موشکی حزب‌الله لبنان، که در واقع یک عراقی است از «فرقه الامام حسین» از گروه‌های نیابتی جمهوری اسلامی در عراق، کشته شد.
🔺
اسرائیل دیروز هم در حمله‌ای به غزه، فرمانده تازه منصوب شده برای «گردان‌های قسام» (نیروهای نظامی گروه تروریستی حماس) را حذف کرد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5172" target="_blank">📅 14:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">علی الحسینی‌ از فرماندهان ارشد و مسئول واحد موشکی «فرقة الإمام الحسین» حز‌ب‌الله عراق در حملات امروز اسراییل به لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5171" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjKLgynl1OOoLGVkBq_NCpm1uJpcpvTD-bOGOz5nV5rp-G5c4BC0GEqhKh_WnI265E8MLX-EdV8aqDojLwpGb1-X-RaDKDYvZrp4EPg_UvSuPKg8rNnCMmjqMqg6uM910HQJDV2i1xCAqcGIvDOTFMucRfjLIYJlzRLTond8-jNzcTq0WxBFgDFvoYLJfK-LuT_LoNuTkiHEH9Ed4OCW0XNr7bV5kBVkPI3fNRKwrUXxfMWUxY4XYo6Stbaz2M73OINOumymIX4GOrQKMt3P2p6AHhlosJsnMODvVB0W0FLWROClWk0yEBkasjBkk-PQmABuW-yRYDsHN32FRhzFMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=UMyj5Qpi4kfF_TlKBLacKvguf4rfqYjkhnOsE9oe4ogwUQXuddmY4LQcrAvskPmZ-gt6i84n6pIUuPvQt-ffObw2gyOwMVvmhR4Fb8Qux3huD07cioPUQ-7ikVwJ_h-ZzQCHxTM3sZ3r5QbI3FrMVzFsOv0DobbfTIrU1ScOcChjxQNQEJOAvo6ybhX-eo6QqsGOSO6AaXIzDuZE4vfxk3GOFsib9fszJ3U7ZO3naFoDxF-fUJ4x9MLccsNCN_kYvE6zDNf1LaM-K3iazk9rBBGtWMzCj0btwv86vmlrmkhix6ceei1HwucuZKgS_tuKamz1mPsh8JvKNHZEz7KkIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=UMyj5Qpi4kfF_TlKBLacKvguf4rfqYjkhnOsE9oe4ogwUQXuddmY4LQcrAvskPmZ-gt6i84n6pIUuPvQt-ffObw2gyOwMVvmhR4Fb8Qux3huD07cioPUQ-7ikVwJ_h-ZzQCHxTM3sZ3r5QbI3FrMVzFsOv0DobbfTIrU1ScOcChjxQNQEJOAvo6ybhX-eo6QqsGOSO6AaXIzDuZE4vfxk3GOFsib9fszJ3U7ZO3naFoDxF-fUJ4x9MLccsNCN_kYvE6zDNf1LaM-K3iazk9rBBGtWMzCj0btwv86vmlrmkhix6ceei1HwucuZKgS_tuKamz1mPsh8JvKNHZEz7KkIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLhYDQru8E2jqLfOx5sE5RZSNXkHUy7fbOibPg-s_hTN7KDiQZrkCs3mUDrpmehDV0jjY2ArChoz1oesV8Bq7WfuxPsw-z22aVEiAdSFUJe3K7pAP1eEZVRZGFd3JiM_WgxTOUwJAW9zHBhXT6MoBuBe2ej_APAHwBBnVknclHAehvM3VZ3QvegWwPmrkGJh7AR93hXO2bu9Pbgqt6dNSSsvsMQ81AT1QYvW6p8mI5AMAICGY2rj43FRg5EH7YnuhkV-dS-gUcLlG7W9DfNJWE1S1vgM5J1hcgOMVH-OcUHvMlCcw5C4QuvNe5XwWJvP0e7an2U2PzQi4HVHODtwWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=Ty1KEMRZBSpi6jB9yyn4Lp2V-DbqkNGwXxsTQ08x4OkOXTV2kP32PXIQrARRFR27boH5HF5FPcJZXrz8CKs8gu6NVyqIRb_dvB5Y1dOpvY6a_v4secytUc1bxaLfj_wKmQ29HjsEHmI5FkGs3YvSPMTjTXXs7OfVstzES97bQbez8H86NtsRUZQ7NXlDWCXc-nmnjIKLyVCBT_1Bn4twnr7oDgGG3V4sDHhq-i7DLjtPdTb6RACqdSG3OAahaLCFdLfndPN8cHyFqnNLb_XpCTXaMg9iJftKrj7WWWrcq7rbjw8-DVOuo0AoJIO3uGh3AWTR9ug9oiWbtrYZ9OeNOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=Ty1KEMRZBSpi6jB9yyn4Lp2V-DbqkNGwXxsTQ08x4OkOXTV2kP32PXIQrARRFR27boH5HF5FPcJZXrz8CKs8gu6NVyqIRb_dvB5Y1dOpvY6a_v4secytUc1bxaLfj_wKmQ29HjsEHmI5FkGs3YvSPMTjTXXs7OfVstzES97bQbez8H86NtsRUZQ7NXlDWCXc-nmnjIKLyVCBT_1Bn4twnr7oDgGG3V4sDHhq-i7DLjtPdTb6RACqdSG3OAahaLCFdLfndPN8cHyFqnNLb_XpCTXaMg9iJftKrj7WWWrcq7rbjw8-DVOuo0AoJIO3uGh3AWTR9ug9oiWbtrYZ9OeNOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nl9CENY759G8oHhR_GPRLpcGIub-FWlWuTLspoHBtP1plQTcsGKFfSnRUJb3KBCZsctvHnZnvaHs1KTr9FRzhPU5V2i6ED3WfXyE4Jw3N8Oc5y8taXCyxkdAbQHodyiqrvpHZwtzpQfBJ_L7pftDH4eGV10dTgTaelx8dSVdFxaSGhDdKPHyww1ScnDXjWcxLSvSNebVMsXyM7o_akT6B4amN6cwXGGR-mDUtMagzsYvvUfNAFbZ7nB3bdk5ou1ANZaTdhPiucWmPsilswRlwHhCHFVoWLP5Zu2KNtyn1mdgszoO7OpDXjonUZbqNOMBvCk_KVplnBHzELqopiDTbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pppXlsj7GSWcp0mCQxOvh84cNldMsvsKvz6SfXPlX_xoyWWdy3VdZiDHmMwQ3ofJLUc1zaX4ht7CxTFM_24rMcURV3FVkINmjLRunBy1wIZq4xycdqlyvGtWYByTfywamWLWUII1xH2NqNKmvXt0iGNcgxyUAymhAuGC8beGUnGYXqLbwqO1HjkM4pcevahNYCfPD3YTkd0ik2mrPU11m4Oz4d9tp3b_IRFnc8u33t98jBV2ZxjChbiljR26CJK75cctvVcyPiBTIjnr0Ie1JFiMeXzZCoTzqxKDW9E081LlJGpPEEdk01shITxGhdYFwUzSow3S9_JRx5PY2nEmKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptpLJKyLl6uZDT09ly4V1A-Ew3xXY9a7KCxD-TRrAznFCHd9DD_Q5WfluSZbCCjLbIq5feFX8jGBTNnEJyKpfw_vjMSYAhmnLBV89hiJWd1aX76w7SCoM6GI4S5oar9j7sUdLHtiAGp9rItjGGQhIijGgKv-hB8iuaEhSM-0YAgNSVSJQ58DzocNpbWgbofgzqYLFKocfJ5z7eogjjN2srDhpDSz39pp5ogPA2MGzd0z86N1DTGjoIImhhzZYV9bMYDWcgh7egocCOKNSUCzmQh_Mrayu_n_yWGv9b1Tf9OL4CIfiE2s2PAXn0mdayzurMtwnpBVx9XQlX9BFSBI6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ty9hUIxFER7a7YvRhW51_ymTXTj4gwbViuBCuxQxVldrhC4im5CJA172Azdo8sGa1wROOFt3cpRWOE2-_TlWpTQl9y_ZUimpSaTdSw75YhgFriMb4dU38lzAgnmQz3m-_r3SSNLWpA_7xcyUnp2WXtNLj714XA7LPIxukO41H3mG4bMQEkqDY5wz0Gof7_zgJJML61CLmhO9axXs3fvBuSE5PRficKgONoPPaieDVe5P2bDmhOgWGZtttEYwyOQKStkQ91iYZQQjl9fvuHQ54-xhqAvoh8lWbp-ZQ2FDI98xHUl37mjKDdga6M_LiKNev3zfo_MdGibTYR7miExGbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUca0Fj2pLECygekdYzxRCz_8kV3F-92r4ZfvpVoNfFwQBIoToyobSbDeg3tMfekiIZb_X4x7lXj1vzeU30Db1NpBfHy8Sd53WSuZUzh043LC0a_ySih93Vi3FH_miCJGEIApjf8HN7vndSFY9-iUkqq0e-jFxUDl8rJ485X87maVMDJdFhnqOXYqob2hcN2Hd7uE_-bYuH5N74z7bMiGVjfNM_DSIG2-YpASB5lJR8Jx8ikz0SMFRylnHRPzopB_fEzCbjWrW_Aai03Kn__niRJj1gQIhT6c8FTlhkvI8F8dESx9k-MM_dYFDH1P4fRdoDB-6YeJgkxwsSrTDX4wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3XaaABnZ4RwiDOYfwLhBejAA_2St5Mm9-FunWELYHZWiYaeyiJElxRUjMhQESxmt7ygnJrOkvyhpz0_JkggF6EG4Mzi4QGQSMzztbJg6eOuJPgp6SB3v8hek7MMtbkDDkhVmIRY7zMUkN2VayLSIepWr7KhvSmDn4LTQbPaEp5KRIzBbOrp-3QmkibmA1MUslJxGBPDSt7NXWYpNctR3g7T9m5dg_SdjaNe_pTciL2Qwuw3JeMFQTHQTtFCzWqQHimxz6l4jI3-sC_iKNKX9_wGRx-3-_cumaAAmWLTDIAuqYlY-EXJ_1G4uUZByxZ4MQ-aYTcRTfrF9fcneiRM6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/YUoH69Vdj4udi-rPH0tDbJPYDXXM1ahcTRg09dYIwqgYE6tlC8hn1NgyoVjLB4ge8R928UTdVlBiaUNbpgXfdLPg5ThxgTPGXjFMpXamt3AfRdU5VGlVt9gV3qpA5tkKtOHErmVbbOIubJqZq0s5KU9xYRIF0sB7uNJif6q5J-RDJL4SAANK-V7y_gy94Uqi_n2JyeyHnsQrtDpFIdaOUY9x5HeSMHBd_iUt82yOYfVHNnrQnYVDvbYHh3tvOqUG6h_FWBXEfxaOE-iGQ_l3hQv2YzZnjdF6dP5mwse5a3tz-0LNJD7QPdyiupz9UxDBPqPSCvrSce7TPVgr-uSIig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.43M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 11:42:18</div>
<hr>

<div class="tg-post" id="msg-696848">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/935e9dafc7.mp4?token=pH_wt8LOJMaj6T4Mjjd0wtWgtcAsU8wjGiw4DtSRwg7B7m6rzPdXoEJXThAEX-tj_xWe3glF-75vYkVORWjWCb7IRK9UyGyHEYE-y1zQjwoZ1b3U9sX3MakqR6HU6n913Fro1qGWCN40URST72YQkua2TcVEgFH11gTReqA_z8gxLsVMsGLfItEIv6qRNz_Yw_3OhrkVxeooY0phZmeh5mPm7Deh72ZY2sRCs64t13un64AhOKE2lqAZTpn-hNENOiujaEZen-ilfjx3jwP_fGPVZTileQ7cKuslh-i33xvwvHAovwN4exEaH41g4DdHS8qrenhh6Ons0z-nHy_XHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/935e9dafc7.mp4?token=pH_wt8LOJMaj6T4Mjjd0wtWgtcAsU8wjGiw4DtSRwg7B7m6rzPdXoEJXThAEX-tj_xWe3glF-75vYkVORWjWCb7IRK9UyGyHEYE-y1zQjwoZ1b3U9sX3MakqR6HU6n913Fro1qGWCN40URST72YQkua2TcVEgFH11gTReqA_z8gxLsVMsGLfItEIv6qRNz_Yw_3OhrkVxeooY0phZmeh5mPm7Deh72ZY2sRCs64t13un64AhOKE2lqAZTpn-hNENOiujaEZen-ilfjx3jwP_fGPVZTileQ7cKuslh-i33xvwvHAovwN4exEaH41g4DdHS8qrenhh6Ons0z-nHy_XHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۹ اکتبر؛ روز توجه به لبخندهایی که پشت آن‌ها غمی پنهان است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12 · <a href="https://t.me/akhbarefori/696848" target="_blank">📅 11:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696847">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bee79ed0e.mp4?token=Pdex-GSWGh2aGOx9vQ-s1TTjDRJ3XmUNBT6Klj-j1TK6Ao1IYsGlvpP19sK6xb1N5CWd3saEHQQEMDWRn30RCKiw_-D-hR_bQLtZJnW9malHDXEdNRchqIHgaj_c-Zd5cXsfkCe5HM0wQHF1aY3ehcYozUtRjxb1mX38RnRtL0vT9U3MjJ3o9HNpGrUKlw0u6I9Laewdan5eWKrayD2MfZlYtrmCFF92LQ8RvedEk4tHvFe6iMMDBECDSFCEPdb21OmB7e8iIVBdtOqITbY_0lJQ5gM-98stQqeFOksbnaAOXCi1EWLA5mmvKmIA-umxvC8Gbvbx9gPBdEF9h8IK-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bee79ed0e.mp4?token=Pdex-GSWGh2aGOx9vQ-s1TTjDRJ3XmUNBT6Klj-j1TK6Ao1IYsGlvpP19sK6xb1N5CWd3saEHQQEMDWRn30RCKiw_-D-hR_bQLtZJnW9malHDXEdNRchqIHgaj_c-Zd5cXsfkCe5HM0wQHF1aY3ehcYozUtRjxb1mX38RnRtL0vT9U3MjJ3o9HNpGrUKlw0u6I9Laewdan5eWKrayD2MfZlYtrmCFF92LQ8RvedEk4tHvFe6iMMDBECDSFCEPdb21OmB7e8iIVBdtOqITbY_0lJQ5gM-98stQqeFOksbnaAOXCi1EWLA5mmvKmIA-umxvC8Gbvbx9gPBdEF9h8IK-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دردی که بالینا سال‌ها تحمل می‌کرد، در ۳۰ ثانیه از بین رفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/696847" target="_blank">📅 11:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696846">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNIDbhl7mbQAP99rgML5AdgnOhV8eMV-YOTBfFetqIUQyVBxyKEixkiqJ2WQxR9lUBjYtDUFDJ2kcpFP4BMFMmS4iYpOmrnx42hP_mS-V-zLqU2Nz_2aZ5S-PQkFNsl3MZbD3_l91T_GHdJJDbh69I0afKFHK6Gm_bnR_IYk31SIcVV7-VyChpM1sr_CRtTgE00K334Lzayjq-ruQ5mshxtwBJTQ9RFDlVRPEsGTKdokmsl1Qa3Kv5nHtYtASnCFiQNUld6xShCy1NlO15U23VRbCzaPTzTW5XqlQ1HoiuILVznPrHf5LJDNzNs9R9w-lws6lv31xm6eKlhk84GfyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تضمین ورود موقت خودروی سواری نصف ارزش گمرکی تعیین شد
🔹
معاون امور گمرکی گمرک جمهوری اسلامی ایران در بخشنامه‌ای به گمرکات اجرایی سراسر کشور، میزان تضمین مورد نیاز برای ورود موقت خودروی سواری را اعلام کرد.
🔹
بر اساس این بخشنامه و در راستای بند «ح» ماده یک و ماده ۱۰ قانون امور گمرکی، میزان تضمین ورود موقت خودروی سواری معادل نصف ارزش گمرکی خودرو به‌علاوه مجموع وجوه متعلقه تعیین شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/696846" target="_blank">📅 11:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696845">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
بارش باران در محورهای پنج استان | ترافیک جاده‌های کشور روان است
🔹
بارش پراکنده باران در برخی محورهای استان‌های آذربایجان غربی، آذربایجان شرقی، اردبیل، زنجان و گیلان گزارش شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/696845" target="_blank">📅 11:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696844">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
نیویورک‌تایمز: ایران به رقیب دشوارتری برای آمریکا تبدیل شده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/akhbarefori/696844" target="_blank">📅 11:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696842">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
طوفان سهمگین «سیمون» جنوب مکزیک را درنوردید
🔹
ویدئوهای منتشرشده نشان می‌دهد که سیلاب شدید خیابان‌ها و خودروها را در مناطق آسیب‌دیده به زیر آب برده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/akhbarefori/696842" target="_blank">📅 11:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696841">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بنزین در ایران مفته؟!
🔹
امروز بین شما مردم اومدیم و از شما پرسیدیم که به نظرتون قیمت بنزین کمه یا دستمزد‌ها میزانش پایینه؟
🔹
جزئیات را در این گزارش ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/696841" target="_blank">📅 11:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696840">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c12c246a.mp4?token=FoUFsDbuKF3kV8BJbw4mBmOvZc8K4nH5n-QjUPE0vPHq2Us1RrK4z26Ec-OsHu2wrw0ePa1_UIhkni6jg9EBoGOZNuR5VUNa8ReJfnL6ufl2idw04EjrxoE1dlE8gwcrmGOcugWCcna7qt0Cd7vn5AfpDWRyjRdpjcqPSmB3oPu8aTHxj3puTLAfaHdSLLbrVxQOpmtt1Jk_uMgERGwo1kqMwosPj9vf6N8GI5Vf4IsF231MLL_S4RqLssHyacCJnbb6jXmdEL3-RUDE586kenQ6SNjnYyyr_ZuoikEjbyYuRekOSrsClzI5jysGrWtfLTARZFv7s8n0Mt5zAvrHQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c12c246a.mp4?token=FoUFsDbuKF3kV8BJbw4mBmOvZc8K4nH5n-QjUPE0vPHq2Us1RrK4z26Ec-OsHu2wrw0ePa1_UIhkni6jg9EBoGOZNuR5VUNa8ReJfnL6ufl2idw04EjrxoE1dlE8gwcrmGOcugWCcna7qt0Cd7vn5AfpDWRyjRdpjcqPSmB3oPu8aTHxj3puTLAfaHdSLLbrVxQOpmtt1Jk_uMgERGwo1kqMwosPj9vf6N8GI5Vf4IsF231MLL_S4RqLssHyacCJnbb6jXmdEL3-RUDE586kenQ6SNjnYyyr_ZuoikEjbyYuRekOSrsClzI5jysGrWtfLTARZFv7s8n0Mt5zAvrHQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی زیبا از قلعه ضحاک، هشترود
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_sharghi</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/akhbarefori/696840" target="_blank">📅 11:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696839">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
عربستان: فرودگاه بین‌المللی ملک خالد ریاض هدف دو حمله یمنی‌ها قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/akhbarefori/696839" target="_blank">📅 11:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696838">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
عصبانیت تارتار از سرقت تلفن همراهش!
🔹
دست سارق موبایل رو قطع کنید!!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/akhbarefori/696838" target="_blank">📅 11:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696837">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d058d9b9f.mp4?token=hwyLzRZ--wPnXe1NIc5IF69YMpdMD-7Byxr347cQAsWCHPa8tv6_EQHz_nevtJxlwKQsTtTC6kOx7d59b2mb5IodRBF5uKEDo3Pw95swOfKSi_RGTRAdxKZGCXaHytR3Zh78VLOIvwjDc9ksE6v2ewoQBCYeeCXFnuXW6qYj5M_vuq2QzasGkWDh4WHWt07nhOYvzACU1ySv5F-gf0pnLL90zJ0gP9KJJONR15A8QwC0NyTZGr_KRaZ7vMkhEWMDgOWFONvQxkNQZUJUt51GKJx4Aj_LEjGW2LINkhUUySkdG_jRrN0-ZJB8yvXwky_C_qHUOBOUzKhauSuigxMZRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d058d9b9f.mp4?token=hwyLzRZ--wPnXe1NIc5IF69YMpdMD-7Byxr347cQAsWCHPa8tv6_EQHz_nevtJxlwKQsTtTC6kOx7d59b2mb5IodRBF5uKEDo3Pw95swOfKSi_RGTRAdxKZGCXaHytR3Zh78VLOIvwjDc9ksE6v2ewoQBCYeeCXFnuXW6qYj5M_vuq2QzasGkWDh4WHWt07nhOYvzACU1ySv5F-gf0pnLL90zJ0gP9KJJONR15A8QwC0NyTZGr_KRaZ7vMkhEWMDgOWFONvQxkNQZUJUt51GKJx4Aj_LEjGW2LINkhUUySkdG_jRrN0-ZJB8yvXwky_C_qHUOBOUzKhauSuigxMZRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تبریک تولد پوتین از طرف پزشکیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/akhbarefori/696837" target="_blank">📅 11:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696836">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
دعوا در کنسرت ساواش و مجروحیت بلاگر کرمانی
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/akhbarefori/696836" target="_blank">📅 11:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696835">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAOqcFneuQ18U_c5PAxkFRFMIaWPx7TFZ7bWupeBep25pZqWF_XcuMER6-Nk405RYpkbSbajMKgcvxd_QGKITT5vyEv0U7Fwv0TDUlEfJaHy3YpV9Eh0dSPYIED8Zi8hW_uIafHIIhK9YqfU7j3Fpp6e7Rie2l0FQgtySg7mNhbhInPXBBTt12JtaRFisT1K6PA7o6-VutoGcHwZmhYsTPlBuxDvj3WByqFNmApDaRTfiI7hYCK18_3p4UcAj3CCGouBf7YEByyvmv_BdtG_-aJ7r0Aw-qYil_bfXdEtjCRURv-eJO41qt2EQjJLsPpefmY0lfVUmneBeBIwu4AQMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار مدیرعامل منطقه آزاد مهران با سفیر عراق در ایران؛ مهران، محور شتاب‌بخشی به دیپلماسی اقتصادی و فرهنگی ایران و عراق
🔹
در دیدار مهدی رعیتی، مدیرعامل سازمان منطقه آزاد تجاری ـ صنعتی مهران با یاسر عبدالزهراء الحجاج، سفیر عراق در ایران، بر تسریع در اقدامات اجرایی برای ایجاد و راه‌اندازی منطقه آزاد مشترک «مهران–زرباطیه» و بهره‌گیری از ظرفیت‌های اقتصادی، فرهنگی و مردمی این مرز برای تعمیق روابط دو کشور تأکید شد.
🔹
در این نشست، منطقه آزاد مشترک «مهران–زرباطیه» به‌عنوان یکی از محورهای اصلی همکاری ایران و عراق مورد بررسی قرار گرفت و رعیتی با اشاره بر لزوم عبور از رایزنی‌های مشترک به سمت اقدامات اجرایی و عملیاتی گفت: توسعه همکاری‌های اقتصادی در مرز مهران می‌تواند زمینه‌ساز شکل‌گیری یک کریدور فعال و پایدار برای تجارت و سرمایه‌گذاری میان دو کشور باشد.
#مهران_فرصتی_برای_آینده
🌐
منطقه آزاد مهران |
Mehranfreezone.ir
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/akhbarefori/696835" target="_blank">📅 11:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696834">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d224775f7c.mp4?token=j38OS3lPQnGa8cWsDi8KOWy_JsdZ6FcKf6ejm0qO65aOxeVNBx10GQxHx5vVEQBfCivLY61cYeBq4DDnyzxQowktPVQwEhgmFckA7M1Eg5c1usoV3Rpr2Pl8Iox7kojsTJ7nduAVBy-I6Inm54Iixqt7Enh1MPCxd-KuuEhBnZxH1rB9DpkiXTfPENHaBsndwYIKEjou9rs6TCXQlhu1HsGj99rPbU4DMJGJcYgQXR-_-FesISYHEu87Vev8zOSO89ecmjhVoht7C64tAG5Z5LJsxc-gUhCpena1RHSK_rMoEqkCIvv0Ktalg7ezHLWTyj41dC-rm8mM0E9WbtiXCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d224775f7c.mp4?token=j38OS3lPQnGa8cWsDi8KOWy_JsdZ6FcKf6ejm0qO65aOxeVNBx10GQxHx5vVEQBfCivLY61cYeBq4DDnyzxQowktPVQwEhgmFckA7M1Eg5c1usoV3Rpr2Pl8Iox7kojsTJ7nduAVBy-I6Inm54Iixqt7Enh1MPCxd-KuuEhBnZxH1rB9DpkiXTfPENHaBsndwYIKEjou9rs6TCXQlhu1HsGj99rPbU4DMJGJcYgQXR-_-FesISYHEu87Vev8zOSO89ecmjhVoht7C64tAG5Z5LJsxc-gUhCpena1RHSK_rMoEqkCIvv0Ktalg7ezHLWTyj41dC-rm8mM0E9WbtiXCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۵ کد مخفی چت‌جی‌پی‌تی که خیلی به کار میاد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/akhbarefori/696834" target="_blank">📅 11:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696833">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
رئیس پلیس فتای فراجا: تجارت وام در فضای مجازی ممنوع است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/akhbarefori/696833" target="_blank">📅 11:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696832">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqGUAi8mUmi_TjJDPEQPwRaDJg-fNRLJ3h3kROB9apSduKIv2ZURXQP7f03BtmXS1Wo1yeAqimRzv__jPQmt8H0pLGRH8Da2kMcUIPfKBI7tyCnAH0k_d6VMPKHl2-48qz2PIMZ2-RTRa1VziRvwk0es7awfNfLi9Z5JDfapgvK_IzCsam5e1iZnYGsr3b7Xs4dut6zedmkmyKUa_1A7gitdGmhfU97ByMHo2gk0IcKvS4mIox3L8QcEGFWQ0CoMRniSRUTE5CMidKbPFMK5agn_2Je1bGgAbQfRECuD4TcUTubvuNpU1E_ri3odgtXZK0iOIG2M-Vegmgc1qRAZHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جالب است بدانید اسم پسر لیونل مسی «چیرو» (Ciro) شکل اسپانیایی نام «کوروش» محسوب می‌شود
🔹
البته علت انتخاب این نام ادای احترام به کوروش پادشاه ایرانی نبوده و فقط ریشه لغوی دو اسم یکسان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/696832" target="_blank">📅 11:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696830">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mULIJMylDvEXwRdSKyDOhc1ecpzUf28Gy_MXO9Frvb_pIsDwiO8m6CP5Q_9fjvexBRwVIP4E_aXSkTuKCQShgGEnuGMPeI36wCs66ytc07ognx_ftDnur-jlo6FQhAHxxcyI1kgdVU1AeqQ505bswoNNEidrGyGwn8VRGIZQt9VmA4bu8dgy3q4LgAMEOq3BTEvdwArYHK2-AfGvqQ2xbqalmVR0k7S8S_YDZOSJZsv4ATli5hTiuz50uqMCtIALPprVO4M9eVbaKNHpeVRi1eLu0I4nxfCAJfNsG7vq0notVSDednhkYyr9o9Q40sjydc8jPLjKHCvFCrCVRPFltw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8bfc80ae.mp4?token=osT7vFEqZYDO8C39WbftuifCGQS7QR1l-pO8rrT9KFr8l9wy-ZaPBQsWM5AdxMRy14ZT_m4MNa6lR7HjXLROPo_f9j710KKoNLxXnzAeFcrNSg9ISW4fOrBZlzkT4TPOcuxzy5pzMlwwaQypGXxK-2zHUMsUg4cUXjpCW_eiPavIqWTrHZ-kcPlAt7x3_ydteDloXZMLwHEyETrPy9vWu3Qn6uGLrT1kDH5yjeO7Y523VdJgezXp45nfHeadjRh4yI3gsnELAhpWJLX4AqqazDIwUDWOezw8xWDbc8iRRcz7aOa8k5H8q78dvrd_kIrUU_cju7kuReXeo4Vm2PAgpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8bfc80ae.mp4?token=osT7vFEqZYDO8C39WbftuifCGQS7QR1l-pO8rrT9KFr8l9wy-ZaPBQsWM5AdxMRy14ZT_m4MNa6lR7HjXLROPo_f9j710KKoNLxXnzAeFcrNSg9ISW4fOrBZlzkT4TPOcuxzy5pzMlwwaQypGXxK-2zHUMsUg4cUXjpCW_eiPavIqWTrHZ-kcPlAt7x3_ydteDloXZMLwHEyETrPy9vWu3Qn6uGLrT1kDH5yjeO7Y523VdJgezXp45nfHeadjRh4yI3gsnELAhpWJLX4AqqazDIwUDWOezw8xWDbc8iRRcz7aOa8k5H8q78dvrd_kIrUU_cju7kuReXeo4Vm2PAgpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
پست اینستاگرامی ایرج طهماسب در کنایه به امیرحسین قیاسی
🔹
قیاسی پیش‌تر از ایرج طهماسب عذرخواهی کرده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/696830" target="_blank">📅 10:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696829">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
آموزش‌وپرورش برگزاری آزمون‌های مؤسسه «ماز» را تعلیق کرد و هشدار داد: در صورت تداوم تخلفات، درباره ادامه فعالیت این مؤسسه تصمیم‌گیری خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/696829" target="_blank">📅 10:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696828">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90ee39992.mp4?token=lvt9PpiN0ykutxnmp22g-tZes_PTZxU2y8v10p0F0HESnR8WWrU4s9KWTqJN641ERIW_5wpFE7dDfLvy6tjgZyocdxeUHsxbjlGBpKa1tCp26hKK0DdgUrqghgO8-doJbBcMDSnaztVuO7iQ_Snsisl5cLfw7GM_iqtOBaogOV3ERzXyRl-f--f54doisOIHd7GIdnk8wuo5-RQSepU_ZnwltX5AhsOu9DCwX0-fIQLxFNcSEL8Qp99xRB4AIYccCWpZXtBubFTEd-5weW4PRm7q_6CYnBbtOuYn-TXZdEkG4eUcbOfS7LXTBexsAiJsF96Dfd5rCU199ZXfEiEV8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90ee39992.mp4?token=lvt9PpiN0ykutxnmp22g-tZes_PTZxU2y8v10p0F0HESnR8WWrU4s9KWTqJN641ERIW_5wpFE7dDfLvy6tjgZyocdxeUHsxbjlGBpKa1tCp26hKK0DdgUrqghgO8-doJbBcMDSnaztVuO7iQ_Snsisl5cLfw7GM_iqtOBaogOV3ERzXyRl-f--f54doisOIHd7GIdnk8wuo5-RQSepU_ZnwltX5AhsOu9DCwX0-fIQLxFNcSEL8Qp99xRB4AIYccCWpZXtBubFTEd-5weW4PRm7q_6CYnBbtOuYn-TXZdEkG4eUcbOfS7LXTBexsAiJsF96Dfd5rCU199ZXfEiEV8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باهنر: این ایرانی که صداوسیما نشان می‌‌دهد، کجاست که ما به آن پناهنده شویم؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/696828" target="_blank">📅 10:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696827">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کمیسیون بهداشت: در ایران مورد مشکوکی از طاعون ریوی گزارش نشده/ ۳ کشور کنترل‌های بهداشتی مرزی را تشدید کردند
فاطمه محمدبیگی، نایب‌رئیس کمیسیون بهداشت و درمان در
#گفتگو
با خبرفوری:
🔹
مقامات روسیه وضعیت اپیدمیولوژیک منطقه را پایدار اعلام کرده‌اند و تشخیص طاعون به معنای غیرقابل‌ درمان بودن بیماری نیست و درمان سریع می‌تواند مؤثر باشد.
🔹
تاکنون در ایران مورد مشکوکی از طاعون ریوی گزارش نشده و پروتکل‌های بهداشتی و پایش بیماری‌های تنفسی در دستور کار قرار خواهد گرفت.
🔹
قرقیزستان، تاجیکستان و ازبکستان در پی گزارش احتمال طاعون در روسیه، کنترل‌های بهداشتی و قرنطینه‌ای در مرزهای خود را تشدید کرده‌اند.
@TV_Fori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/696827" target="_blank">📅 10:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696826">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
در این فصل تا جایی که امکانش هست ماشین‌ها رو زیر درخت‌های بزرگ پارک نکنید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/696826" target="_blank">📅 10:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696823">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cdf4d6cfb.mp4?token=l2K0yoQpLrgUb0yjHVs43Fd5MO-dzP_bKGNpqrbpENhujNH5s9GaSgDUHIyDbrdStQVKsS95BJjfAlTU1-kcgm17EWVHn56gG3whbBGlPVQQykYOTFEqoO144i1HZ7CpnFuyNLxZcvrHMz1LQyWB_6qoRfIbLNN0zHulItqFaivVCuH-t8osINM4ANg6l6mhN-0xU2RmOurMWbft_2B7g-CMSeCh1e2kFC8EhhvNYNobqf4VIvzw0Pn3U6C9Q8XxC0NgXEat_KrjmBetps-0tCBElJ2qqab2Mjoh06Oc3tNDJpaLMUkS-yWMROOMNk8LmSTiUe1NkW9KYlpfmkfUMoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cdf4d6cfb.mp4?token=l2K0yoQpLrgUb0yjHVs43Fd5MO-dzP_bKGNpqrbpENhujNH5s9GaSgDUHIyDbrdStQVKsS95BJjfAlTU1-kcgm17EWVHn56gG3whbBGlPVQQykYOTFEqoO144i1HZ7CpnFuyNLxZcvrHMz1LQyWB_6qoRfIbLNN0zHulItqFaivVCuH-t8osINM4ANg6l6mhN-0xU2RmOurMWbft_2B7g-CMSeCh1e2kFC8EhhvNYNobqf4VIvzw0Pn3U6C9Q8XxC0NgXEat_KrjmBetps-0tCBElJ2qqab2Mjoh06Oc3tNDJpaLMUkS-yWMROOMNk8LmSTiUe1NkW9KYlpfmkfUMoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک بلاگر در اقدامی عجیب برای دیده‌شدن، یک مار را قورت داد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/696823" target="_blank">📅 10:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696822">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b08b03dadf.mp4?token=dc_ryYnAd-k-au2_SqjxsFCiVEzivNmWawTyaLZSl4oJ7A_8VcZiifHKZzarC5ZWJjdhqElVZBq2UdqTQgjD0XZoolUjiIP9sO-RffR3M8btGUd0hoUDy8Go9PUqc3ZNixPuDG2ZADqprHUjHu9ULWMEl8NMR07uuM5sRhn34quXhS3z3HOwuUNEhg5W_QtQVDKpC-JV2vD4TUpMGJi2_Ifc5wpDv99AhodiWDymVcq9HhKDV1PHNlp9wXSf3juBDoF9HcPZQrzmNweKr_RTBTqucX9Kpsm6o6WmU1rWvXQwwejVeSRQhU_gly-X8Dpq77M_3gBj2M32h3p4aChoUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b08b03dadf.mp4?token=dc_ryYnAd-k-au2_SqjxsFCiVEzivNmWawTyaLZSl4oJ7A_8VcZiifHKZzarC5ZWJjdhqElVZBq2UdqTQgjD0XZoolUjiIP9sO-RffR3M8btGUd0hoUDy8Go9PUqc3ZNixPuDG2ZADqprHUjHu9ULWMEl8NMR07uuM5sRhn34quXhS3z3HOwuUNEhg5W_QtQVDKpC-JV2vD4TUpMGJi2_Ifc5wpDv99AhodiWDymVcq9HhKDV1PHNlp9wXSf3juBDoF9HcPZQrzmNweKr_RTBTqucX9Kpsm6o6WmU1rWvXQwwejVeSRQhU_gly-X8Dpq77M_3gBj2M32h3p4aChoUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایده خلاقانه و ساده ساخت چراغ تزئینی؛ زیبا و چشم‌نواز برای دکور خانه
🌸
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/696822" target="_blank">📅 10:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696821">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d1694718d.mp4?token=MDjHCqqWz2zc3tDrzI_pHoGZPWoL6wGpTpZX72F_tiDKU3cK8Sc6A8CGGBZzPxXXwvq_mP9rwcHErBNpYs3maCH_VXjA8p2NMZchPhLC3kh7nUEPCIbZTF7NU_7j0fnZgT_EhCGOmuMONokXsJBOkMnknVTiBzwNu3rTr9eJ-KOuq9vCGlF9A3X_B0fiyKZ7VLH16wClRj27yJDMSSKPNL47Nw89WCQsBFEcUabcDSXDHrENUJLKPQp-6svIFz8NXfbr7fcFpN-_oJ39P3pBkFPSAWXRjfl-tTuxDFOGeX10d9yX6QE92g9fds19QRdqRzBn5EITL1MYbs1Zj4LKXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d1694718d.mp4?token=MDjHCqqWz2zc3tDrzI_pHoGZPWoL6wGpTpZX72F_tiDKU3cK8Sc6A8CGGBZzPxXXwvq_mP9rwcHErBNpYs3maCH_VXjA8p2NMZchPhLC3kh7nUEPCIbZTF7NU_7j0fnZgT_EhCGOmuMONokXsJBOkMnknVTiBzwNu3rTr9eJ-KOuq9vCGlF9A3X_B0fiyKZ7VLH16wClRj27yJDMSSKPNL47Nw89WCQsBFEcUabcDSXDHrENUJLKPQp-6svIFz8NXfbr7fcFpN-_oJ39P3pBkFPSAWXRjfl-tTuxDFOGeX10d9yX6QE92g9fds19QRdqRzBn5EITL1MYbs1Zj4LKXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله تند ممدانی به ترامپ پس از تیراندازی مأمور مهاجرت در نیویورک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/696821" target="_blank">📅 10:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696819">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwwYy1074h7c_NqUqLsofWoWvi08Wr9GqeTLnkshTU0FCX5iqSKz9yDw4_vz3uGXOx6MyRAk3j15FbT430YWrhPqrN7UX97YY_2Jk-6mcNdpEG0rF_v_l7mP7ioM-h_4-4AkwDavk9H23BpFgB_O1og-Jz_YPl4qKUJWeR-MOVYKchqdn9Ax-aJ7c_KPCXq0hz1y2Yfco-dh2TnDuDjISRhP-rxh8eYN7ysTVWHB9qzyL0a0j6w8peJfSiaztuXSCd69E11sZtconR8OooEy5b1C49L-08Oc4tgCA4L3GwzPT2dni2kkPCZBeH5VfWzJBHsF-KifW7ir9Z5HhyomhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e00fb408e1.mp4?token=f8zM59g_n9XDbqmOe9CMHQJt4fxvFFBaDqMvXTRxTwQcP9WLc8VEC3txa4WJOx0ytxs_N90zZgwqhz0-eVOS__dqUtUyZIs9OUg-m6NMrx45Dv2fsjHP152s5sEBZOIk3uyMsrgEzOOrDHWWh-VSA80yAY0tl3TH5xjqnLkyC-1UOIY0XCrLdCLBrUGqNF6_fSYRFiDGg4MeGS_k2ZyJMQtYYNwhhQyjl65xT1_NoNuylMoPxvzkTotLDiKzvHEhKNDsmkBdviBZnl16w3AFfdyET5Wa4xaeBwkmVkV_Zl5ljBzrVYXbSwBMmxoFRgl5xVDMtZSaktcKv0PkkhVPeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e00fb408e1.mp4?token=f8zM59g_n9XDbqmOe9CMHQJt4fxvFFBaDqMvXTRxTwQcP9WLc8VEC3txa4WJOx0ytxs_N90zZgwqhz0-eVOS__dqUtUyZIs9OUg-m6NMrx45Dv2fsjHP152s5sEBZOIk3uyMsrgEzOOrDHWWh-VSA80yAY0tl3TH5xjqnLkyC-1UOIY0XCrLdCLBrUGqNF6_fSYRFiDGg4MeGS_k2ZyJMQtYYNwhhQyjl65xT1_NoNuylMoPxvzkTotLDiKzvHEhKNDsmkBdviBZnl16w3AFfdyET5Wa4xaeBwkmVkV_Zl5ljBzrVYXbSwBMmxoFRgl5xVDMtZSaktcKv0PkkhVPeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطره‌ آرنولد شوارتزنگر از بیژن پاکزاد
🔹
بیژن پاکزاد طراح و تولیدکننده سرشناس ایرانی-آمریکایی لباس‌های مردانه و عطر و ادکلن بود. پوتین، ترامپ، اوباما و تام کروز از شاخص‌ترین مشتریان او بودند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/696819" target="_blank">📅 10:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696817">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7e5618e1c.mp4?token=BCgDs9eW8QjGfbnUlmZtA3aV6lNeknPDqG9Yw39wgxZeKvEJMd_KDT7G9TpQGOv-uvyD2ICA9ETIMrQWc8Gl-6siZWrPdo8hCclnhtGioZ8g_n4RbFglreuqVkBNTmrOeKRwUVqVZZCQnJP4dJkFJ1ZVDEZji-aY8n7cMZ-RSN9FkzkspNLRGILOdl7lbyJjcKrwkL57uDJQbEQJNq4Lo1fCsz9KeONvKFZKIpVh7LParwkrGuOMsZGKatT9DquwogVo1pB-al7o2IEhWR5S-ZeyMsx2Vi0vf9VfEwpq1ZuGnivnI7xCczlaTCiyJtF-_zeLsl8v_tmJrYJfRbxD7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7e5618e1c.mp4?token=BCgDs9eW8QjGfbnUlmZtA3aV6lNeknPDqG9Yw39wgxZeKvEJMd_KDT7G9TpQGOv-uvyD2ICA9ETIMrQWc8Gl-6siZWrPdo8hCclnhtGioZ8g_n4RbFglreuqVkBNTmrOeKRwUVqVZZCQnJP4dJkFJ1ZVDEZji-aY8n7cMZ-RSN9FkzkspNLRGILOdl7lbyJjcKrwkL57uDJQbEQJNq4Lo1fCsz9KeONvKFZKIpVh7LParwkrGuOMsZGKatT9DquwogVo1pB-al7o2IEhWR5S-ZeyMsx2Vi0vf9VfEwpq1ZuGnivnI7xCczlaTCiyJtF-_zeLsl8v_tmJrYJfRbxD7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شورش اعتراضی در نیویورک پس از تیراندازی مأمور مهاجرت به یک مرد
🔹
به‌دنبال تیراندازی یک مأمور اداره مهاجرت و گمرک آمریکا به مردی ۲۸ ساله در محله ماربل هیل نیویورک، گروهی از معترضان پنج‌شنبه‌ شب در محل حادثه و مقابل بیمارستان محل بستری او تجمع کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/696817" target="_blank">📅 10:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696816">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f429a7a6f.mp4?token=JAX-byDnFUANqAWtLHd-oaV1NaXdM_qVRVD8xcmMqswLqb33QJq8A8Qi6CV_6mqhOB2t8JZ84m7OapY4QA-6iSLcBhJmV9qpIDkh5ofy3R5ybpTHK6qnbjHaWa-nDdbdjaKufzBW3yLktwlb_QBvKqSSHkwl_g_QfHmFV6jdBMDeLGa4MaNmycr08cAniXUf4-xDDS7TvOFCDnBWODcu4kMvGo6VoOTetjI6Ksln1B6iD3hIyCer263OxI783QFIq-m37r7F3jL5YtdptJud3lVdCXy5KwFqmbEf1gx6FUU5alNceIkIjEriSrvmZX5KAz7qL70YtK2hqXCY0Ync3jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f429a7a6f.mp4?token=JAX-byDnFUANqAWtLHd-oaV1NaXdM_qVRVD8xcmMqswLqb33QJq8A8Qi6CV_6mqhOB2t8JZ84m7OapY4QA-6iSLcBhJmV9qpIDkh5ofy3R5ybpTHK6qnbjHaWa-nDdbdjaKufzBW3yLktwlb_QBvKqSSHkwl_g_QfHmFV6jdBMDeLGa4MaNmycr08cAniXUf4-xDDS7TvOFCDnBWODcu4kMvGo6VoOTetjI6Ksln1B6iD3hIyCer263OxI783QFIq-m37r7F3jL5YtdptJud3lVdCXy5KwFqmbEf1gx6FUU5alNceIkIjEriSrvmZX5KAz7qL70YtK2hqXCY0Ync3jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از آتش‌سوزی گسترده در تأسیسات نفتی «بقیق» عربستان در پی حمله موشکی یمنی‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/696816" target="_blank">📅 10:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696814">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
استرالیا به شهروندانش درباره احتمال بسته شدن حریم هوایی و لغو پروازها در عربستان سعودی هشدار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/696814" target="_blank">📅 10:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696813">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKDdkLDM5rOmYc---jeMbnl2BCVpJ-cDYUJ3eIdpcV7obMpKNEWt7lNAR48slAslkqqpQ1WkNzPhM48XONMlMeOnygZBB247O0MZ-4MyOwePm6fDOJRLHx7xOfo86bNEhjckcpbHTKL24jL10ALMdbq6ZuJSgcMvQRjyDMmz0Z3mYFHkjb-tC-_0HWvglrW1eBwG-oQYIpuTNKgAG-StBNg1GV6KpzYC812D_1yWy6-dWObySRgcVlvoJs5mLIygxqJIWah1w67yRAkPYQ9437Y9evJAgOebvOcgQHdUlf1XCGgGREBhgboa9wPL1XFGh0qyHg8EtGoXsjXDv5z0tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسجد نصیرالملک شیراز؛ شگفتی هنر و ظرافت معماری ایرانی
🔹
محمد میرزایی
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/696813" target="_blank">📅 10:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696812">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48e662ff15.mp4?token=A76Hw-5-EOKt8CWXeSMSHxUcaxpareCTWi05e7FHsS7-gjLwWnyRpdqu6DqW0TRYakhbKh1j1FVuxJfbZcG9pFznHtMPmFq6sfzkyO93GQGjJNKTDuGjijUj1CWl97_eYyyr1kRujV6QkxXP4uCzJJo13E06VIefniZbX2US427VA7cLMS5IOV5erMDIaPcfoTc55O_gClCC3zImbfQS-QY4p8_5ZjKbAq2Jl9Fcu6KEfxjsRC1edv_MOEIMVhd_DQUByjI8jW6njsaT-GflD5c1TgME_lhm4zUmpcUWIWYGPlA47tvGd8PCdwuu9QcU0M3Q6Tc1ElWyrQ1EI5l5JJpJ2_nIIP3-bRjStIgAUxrGu3BFZJ2-L26le0Q2gJZ1MTWyJ70lvLR-ohkXPxjkIaS27t0n3eOcTo0oa04MM15dpvH033WKI2KGeETjtFvw_dPggRC_5ihUrNGMYpnjJI5qmgR2S5F3Eo8XzAROYamtsUNQftVICUW0tzQV4cPJWBCcWCbHaNDazldj4spqbiVvuuzQM3UDtRjxC4dobGif5VCewFLcFZbq4q8yknZYeJVgsbbRlE615MM-AS1ULmQPUBfdyoxypxziS2xxGTmQDyO9ifwifC_AQyJN2Z6hWlNeYBleoWlYEzJm-E4mU01Gn7aeMzJwIvmmMaR4pWk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48e662ff15.mp4?token=A76Hw-5-EOKt8CWXeSMSHxUcaxpareCTWi05e7FHsS7-gjLwWnyRpdqu6DqW0TRYakhbKh1j1FVuxJfbZcG9pFznHtMPmFq6sfzkyO93GQGjJNKTDuGjijUj1CWl97_eYyyr1kRujV6QkxXP4uCzJJo13E06VIefniZbX2US427VA7cLMS5IOV5erMDIaPcfoTc55O_gClCC3zImbfQS-QY4p8_5ZjKbAq2Jl9Fcu6KEfxjsRC1edv_MOEIMVhd_DQUByjI8jW6njsaT-GflD5c1TgME_lhm4zUmpcUWIWYGPlA47tvGd8PCdwuu9QcU0M3Q6Tc1ElWyrQ1EI5l5JJpJ2_nIIP3-bRjStIgAUxrGu3BFZJ2-L26le0Q2gJZ1MTWyJ70lvLR-ohkXPxjkIaS27t0n3eOcTo0oa04MM15dpvH033WKI2KGeETjtFvw_dPggRC_5ihUrNGMYpnjJI5qmgR2S5F3Eo8XzAROYamtsUNQftVICUW0tzQV4cPJWBCcWCbHaNDazldj4spqbiVvuuzQM3UDtRjxC4dobGif5VCewFLcFZbq4q8yknZYeJVgsbbRlE615MM-AS1ULmQPUBfdyoxypxziS2xxGTmQDyO9ifwifC_AQyJN2Z6hWlNeYBleoWlYEzJm-E4mU01Gn7aeMzJwIvmmMaR4pWk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش در خارج؛
ترور در سیستان و بلوچستان
🔹
از نهم تا شانزدهم مهرماه سیستان و بلوچستان یکی از تلخ‌ترین ایام خودش رو تجربه کرد، تجربه‌هایی رو که نمونه‌های اون رو در زمان فعالیت عبدالمالک ریگی شاهد بودیم. اما این بار فعالیت‌های تروریستی در شرایط خاص‌تری داره انجام می‌شه!
🔹
جزئیات را در این گزارش ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/696812" target="_blank">📅 10:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696811">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
تکذیب شایعه فوت مهران رجبی
🔹
در روزهای گذشته شایعه‌ای درباره مرگ مهران رجبی در فضای مجازی منتشر و به‌ سرعت دست‌به‌دست شد؛ بررسی رسانه‌های داخلی نشان می‌دهد این ادعا صحت ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/696811" target="_blank">📅 09:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696810">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e1c51de4d.mp4?token=MjEapmV92iA4hka7E7-JfQJ7Hslth_9CatjQoFPL-_lwLEk8A82O5iGUocX3x8ZF6nLU2ZL77MAa3DK9ZfO0Hf72s4jrCGmm0wWCNcMs3CpwvkJsJf4NxhF_SSSnM8025_NuCC3zo5D9H8ZIYxSUqAa_34Pfu2TumvOm0ZzV5Kydh-I8IxXo1b6StC7M9Y7GIvwXsL5CHQlryNMgQECCRKN6lL9l7HBMVZl59jJti0GCC8bpohlWFM9_sOPSdUU-BfE1HXB_b6QEyBaX1t8Jw8AYHh8-olalr35THIyNbXzN1ucZytwMaduwAZD99r7lyFgYg8VEKjLtaizSD9cKXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e1c51de4d.mp4?token=MjEapmV92iA4hka7E7-JfQJ7Hslth_9CatjQoFPL-_lwLEk8A82O5iGUocX3x8ZF6nLU2ZL77MAa3DK9ZfO0Hf72s4jrCGmm0wWCNcMs3CpwvkJsJf4NxhF_SSSnM8025_NuCC3zo5D9H8ZIYxSUqAa_34Pfu2TumvOm0ZzV5Kydh-I8IxXo1b6StC7M9Y7GIvwXsL5CHQlryNMgQECCRKN6lL9l7HBMVZl59jJti0GCC8bpohlWFM9_sOPSdUU-BfE1HXB_b6QEyBaX1t8Jw8AYHh8-olalr35THIyNbXzN1ucZytwMaduwAZD99r7lyFgYg8VEKjLtaizSD9cKXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین آیفون تصویری ایران در دوره قاجار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/696810" target="_blank">📅 09:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696807">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7e2c521e1.mp4?token=VWEpTq7_RGYXjR514gSlmE4RFed9gsF0teyzWdsB9P9v6HGBgYWaOc3gQ8OTh6LW-6IQKomh5kxfkCbG9TpxsdzUIiwTKKyAqQTgjzXuRWx7ur_YsJpc5yLPgV782Zv2jZ4PpBjGtdcb51vOo1ZpBdMMVFl4yc3NAXeqScTKfhj9jZXDbp4nNjaHkkbyI4391PYLpRV04AD5QNtmYyLPqb5NvCcC9P7FqF_uTSirQNJtmBt31WzfOT_uTaLzgU2Eqw6EDSw09hMQmvOcZnY8E32zlsl1jP0pMSpY6JZ-VZQw-JlH26Jud7Mapwrg4ERCLUvdqHKik9nXTHV6WJW_vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7e2c521e1.mp4?token=VWEpTq7_RGYXjR514gSlmE4RFed9gsF0teyzWdsB9P9v6HGBgYWaOc3gQ8OTh6LW-6IQKomh5kxfkCbG9TpxsdzUIiwTKKyAqQTgjzXuRWx7ur_YsJpc5yLPgV782Zv2jZ4PpBjGtdcb51vOo1ZpBdMMVFl4yc3NAXeqScTKfhj9jZXDbp4nNjaHkkbyI4391PYLpRV04AD5QNtmYyLPqb5NvCcC9P7FqF_uTSirQNJtmBt31WzfOT_uTaLzgU2Eqw6EDSw09hMQmvOcZnY8E32zlsl1jP0pMSpY6JZ-VZQw-JlH26Jud7Mapwrg4ERCLUvdqHKik9nXTHV6WJW_vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات بی‌شرمانه روبیو، وزیر خارجه آمریکا علیه مردم ایران
🔹
هخامنشیان ۴۸۰ سال پیش از میلاد به یونان حمله کردند و آنجا را غارت کردند ریشه ایرانی‌ها به این غارتگران برمی‌گردد!
🔹
او در لفاظی‌اش علیه تاریخ کهن ایران به این واقعیت هیچ اشاره‌ای نکرد که ۴۰۰ سال است ایران به هیچ کشوری حمله نکرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/696807" target="_blank">📅 09:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696806">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای کانال ۱۲ اسرائیل: رئیس ستاد ارتش اسرائیل، بنا بر گزارش‌ها، دو روز پیش از مقام‌های آمریکایی مطلع شده که کاخ سفید و پنتاگون در آستانه یک حمله احتمالی گسترده آمریکا به ایران طی هفته‌های آینده، دستورالعمل‌هایی صادر کرده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/696806" target="_blank">📅 09:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696805">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eb1d4fa88.mp4?token=DxGxNnAwyo_cq9MmNruhDXKSXlP0mHrvvEBZLTffKvC2iEfwQ_uuKSqGmx1_XSoIZKLzISw4lP5cIPWpo3wNK-txoH2r3d37xyxnCrK746arwtcH-XgxOMHkW9XAadjkaEy531cJDmXYjNq9NIr9LdvGFjj1X8pTyuZDDWmQmwxL_l2oxNyd_40iSrHpx_2z0wjJxC2KHlA-x4KoErEJWnkRI-ysR4hxPfJZYyOog4A9uFq3SVf7vDxTCT5KMHYxkM99LLc_ToapQYGQCNPYGGZX7QBIp3-6nRX1gNVJARUzoJ347An6SQgx0S1u4JzXJiJk8X0X1WKNu0piTIEVonXT0Rbs4ARUNdfdJIKEu6-paHWRhD1V7zdGDQTbuzxaOwC1FFUhhxu6Kwk4jvrc5GwATcBQPbSvUpVyRcETCW67YThZLhF9UBw8oQxi4co1Zc7OCuooAG1PTnQiJnNA5G3dyOwfXrld5b8FyzBvyfBrM_h55GFWKulZJpJjNpTjukoOtxavqHDYusfVh2vwhLCY6Bpyse4ipWsI4pFPNPdFW2tiP7WtP0Pm8ZsTe1gggT9ItIIkAP6lNVWBhms_N_r4Diad9pk4pZU6ko_Z0WCrSEWSMLBExq2lMv4VsEzJA9LbxV2wDC3zkNQwXe2OUbKWGuTN8PwmSWD4JPecYuc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eb1d4fa88.mp4?token=DxGxNnAwyo_cq9MmNruhDXKSXlP0mHrvvEBZLTffKvC2iEfwQ_uuKSqGmx1_XSoIZKLzISw4lP5cIPWpo3wNK-txoH2r3d37xyxnCrK746arwtcH-XgxOMHkW9XAadjkaEy531cJDmXYjNq9NIr9LdvGFjj1X8pTyuZDDWmQmwxL_l2oxNyd_40iSrHpx_2z0wjJxC2KHlA-x4KoErEJWnkRI-ysR4hxPfJZYyOog4A9uFq3SVf7vDxTCT5KMHYxkM99LLc_ToapQYGQCNPYGGZX7QBIp3-6nRX1gNVJARUzoJ347An6SQgx0S1u4JzXJiJk8X0X1WKNu0piTIEVonXT0Rbs4ARUNdfdJIKEu6-paHWRhD1V7zdGDQTbuzxaOwC1FFUhhxu6Kwk4jvrc5GwATcBQPbSvUpVyRcETCW67YThZLhF9UBw8oQxi4co1Zc7OCuooAG1PTnQiJnNA5G3dyOwfXrld5b8FyzBvyfBrM_h55GFWKulZJpJjNpTjukoOtxavqHDYusfVh2vwhLCY6Bpyse4ipWsI4pFPNPdFW2tiP7WtP0Pm8ZsTe1gggT9ItIIkAP6lNVWBhms_N_r4Diad9pk4pZU6ko_Z0WCrSEWSMLBExq2lMv4VsEzJA9LbxV2wDC3zkNQwXe2OUbKWGuTN8PwmSWD4JPecYuc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری که گفته می‌شود مربوط به تست مین هوایی سپاه در یکی از جزایر ایرانی که برای جلوگیری از پیاده‌سازی نیرو توسط بالگرد کاربرد دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/696805" target="_blank">📅 09:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696804">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dafd53fcb7.mp4?token=nHxp5SdiJKPVX2MtQGi9rDz5acCAAFB_UbTflSdkw1rVjtnCrtOk0Jp5gUnpcG6Q3mmFzy5o35rijcWVhCKlwO-HLBqjaQqPna6hujX-w2xVAThTt_NuNSy6qKasG87zZ3C9YEZhUYk54NLY6iy6c6ppemspnT3WS6B26wI-c2MI1j3IWM8z2615_H_SW8rXE5xVq9CsMG_0SpXFwR4Ek4-bf5ySUGphk7lvfGHv9KOtCeDkP_kDI8Q9JnNH355QM7gg3PSFTi89itfZCvQrvSGpLhIY0AnO_LZjYeelmtxa41eeI1f_0aw5NeUAP65KV2gVVKfdFLAv5a-j7m7Z7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dafd53fcb7.mp4?token=nHxp5SdiJKPVX2MtQGi9rDz5acCAAFB_UbTflSdkw1rVjtnCrtOk0Jp5gUnpcG6Q3mmFzy5o35rijcWVhCKlwO-HLBqjaQqPna6hujX-w2xVAThTt_NuNSy6qKasG87zZ3C9YEZhUYk54NLY6iy6c6ppemspnT3WS6B26wI-c2MI1j3IWM8z2615_H_SW8rXE5xVq9CsMG_0SpXFwR4Ek4-bf5ySUGphk7lvfGHv9KOtCeDkP_kDI8Q9JnNH355QM7gg3PSFTi89itfZCvQrvSGpLhIY0AnO_LZjYeelmtxa41eeI1f_0aw5NeUAP65KV2gVVKfdFLAv5a-j7m7Z7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد وحشیانه پلیس با زنان در فرانسه مهد توحش...
🔹
این‌ها نه قصد براندازی داشتن و نه مخالفت با قانون، خواستار اجرا شدن حقوق ساده شهروندی هستن ... که این طور وحشيانه باهاشون برخورد میشه
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/696804" target="_blank">📅 09:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696798">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lEDzwvUpqatWsZzaTzFLecKVo0_OsWQrJHUTKC87XfxwRl095f4poHSpZYAwCqOcap7TJyhd9bQQeEJw8atEMW0znGK5HL5mtTJO2eDjDgUYP_IdpgZFJmXgibH6pi8CKx0CodR93kejlMBJZCvl6Nfyk90yroVPJqbrwo1ql2X6umUsWsDnpZVC-Vf6JnfBq3WvRFR9wui9m5nyhQZi87QeljsLNuRzrWcBYBvloVpLFISGA_6DR_YBYU1AzoaW_Pv3egYPRCqihPHRQ0QSCmFhlkusWC_m4__6NyCJ0DUl7wFZv8O1-5efjbP9sCflE7prA51bJmkJn9N8UYt9Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/otmazXHLljfhJPyRWHyV6zJhvz2Mebc1gTvU2yYUeKQ2ZvFbBIs4dBRSoG8iBQRQq-yMSx-PaIoHMWf1SfMz30ANpxQ7NFqiMKk5h61SRWM1m4_-9MoEYAl86cmeXK4wKSAVfv8BZHvXpOssfNdZyzgZk_ckuAiMMkqIXWfJKsvXWIm9iPdXsB42Sh_bzUKJ0_rzVNnFGGxdce9TiXbEX2u27BLEX9G4NB1b8eyUYsqFOmyED_CZ_5JXZBubLr6O8UQNXfz3GEeloJboRAv5KgwQgJE-h31e_WKhy3-L6yETKp6Yqybes3ePzANLdsBINI-MEXUML2qhpGDaWqNwIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PEeBQWGJgz7p1CqKqNVmT0Iat00wbKqtvkkKS7mmx5KaYNcY-gPN52bfU0jP0uAKyhZ_Jlt5OfibGH5SqqRGnBq92zjXEAYWRMHMqwNranExMnZNoYvGmFRIK0jvykNBATnrvxbHHJtksVLADtbpu54Pkbln56865MY2a2TIw_LRrjLV8f_KRM5b_brP4-Y40IrMpe2_MJknEtbOFzcpbygfUX8nu67MtbrAF4T_BHC98B_RpdTjs6nPHoUJFGJg8QKs3chXQigeWuQAcJ5ZvhXC9obu6iJ_v9mdMUElf708iCF6VZ-vD__UMnBskRrfTGnEmtxaDyipfbDeX1CHug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YwggR0rHZfH1a2e5ueRCIIeTfSEdmi1GC00Z7YJMv1LsejnF0qXEt1VFrfYjFcZeSzVU2WQVSqA3BDTYAQXVyywg5J3etN-YxHOdgz5Bg22RvnqSbOLyImSU1_Ptk5mBrbgWk-nrRaOoih7YpjrAEPHbcDQTjbsxCEYPGTAWkapNnoVEs3cDzJSksHq1NrislyWt5HrbVBRSuiZL7wkm6_NdNLXEr2jDiqViugdFOElCTf9PgcB3l4L9KpjJVJ-T2vxjO-BT2Oep3VoPv59JZ7G4CEs2kajSGoyDdVPx_socGVmYRRU29jtzT44jOxzB7v6mqJBaPZGPd3xnexxixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XTIgYML8rzZ_BvnkqxQej1CZbhQ1vOy8SNCQsvbTadgjXHqvjR-jUvLEm01jmfcEv5XlmuUCZCNdjPuLr-u5nf8u-jCXD-Qiz7K8iXVT5vF0FyvfXwxs1GDTLB4Qbsn2XUgJlWLwpituugdiYGWuLiuNHX1ieq3vHZenGlyh9SJP0G5OK6VUZ0pwmgSvArTvDjxc5CMKQq0TTZ_nw6CnyZ6ZXQTcwb7XxpoQhjIraq_uAMpI-RGJ09ywmvXyy2AYYBhqmFWBitzziyrxyck0EgjQazB_bqZleud04OpgnXmEBoou77rqMZU-dGRifc0H6ChZE3X91OH9nDiLlosYSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7c60OWPBOo8N-lqm98Hs0XFomJhhj0j4lutsJn9QHi9YACJMAugjmAVtgc5v7EZLTNQ9XtYjxUehTP7hnvy6dFUPkjKggSzU8GXixIeHhCblNUQXJqFj5_vDfSWqf71RjJu5YY2Ov97HKP7jeMXed9LicRrKOGcroeocjsouEcvqHZwMv1MQ1peLoojdb6ZrCTSaRPiXGehz6eKBRaoQ0I8PpE1LC1v6GrGVVQWOZLvLkeZ5xEmZNyTAgihgY3Qn_u0hXQSoMpuFH9qHRzcwhnyQQMzCrJh-h9FD1ouNm67LUY67u5QLGezDSJ9s29dalF7nyv0meyVATTqYx0sgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با
چند طعم متفاوت خیارشور در سراسر دنیا آشنا شوید
😍
🔹
فکر میکردی خیارشور این همه تنوع داشته باشه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/696798" target="_blank">📅 09:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696796">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم النور 4_ جلسه هجدهم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/696796" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه هجدهم؛ ظرف خلقت
🔹
اکنون در نور اسامی خداوند و ارتقای باور و یقین مومنان، سرعتِ کامروایی آن‌ها افزایش یافته و خیر الهی بر سرزمین‌ها جاری شده است.
🔹
اکنون بشر در نقطه‌ی گذر از ظلمت به نور است و به دوران جدیدی وارد می‌شود که رشد آگاهی و افزایش درک و هوش انسان بسیار چشمگیر است و عشق و آشتی هر روز نیکوتر می‌شود.
🔹
در نور نام‌های مبارک «اوَّلُ» و «آخِرُ» «ظَاهِرُ»‌ و «بَاطِنُ» پروردگار آگاه وجود انسان را در رتبه‌ای بالاتر وارد کرده و خلقتی نیکوتر برایش رقم می‌زند.
🔹
به میزانی که انسان در نور این نام‌های مبارک قرار گیرد، رتبه‌اش بالاتر رفته و اثربخشی او در جهان بیشتر می‌شود.
🔹
بر اساس سنت خلقت، با افزایش طلب انسان، باطن اتفاقات زندگی، ظاهر می شود که اول و آخر آن فراخ‌تر است.
🔹
با تابش نور این نام‌های مبارک، از قلب سالکین، تمامی طلسمات، جادوها و بندهای ظلمانی گسسته می‌شود و شرایط برای ظهور حق مهیا می‌گردد.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/696796" target="_blank">📅 09:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696794">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
افزایش عفونت‌های تنفسی همزمان با فصل سرما
فوق‌تخصص ریه کودکان:
🔹
هنوز با موج آنفلوآنزا مواجه نشده‌ایم. انتظار افزایش عفونت‌های تنفسی کودکان با ورود به فصل سرد سال را داریم که البته موضوع جدیدی نیست.
🔹
هر سرماخوردگی یا سرفه به معنای عفونت شدید ریوی نیست. از مصرف خودسرانه آنتی‌بیوتیک پرهیز شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/696794" target="_blank">📅 08:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696793">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
معاون نیروی دریایی سپاه: شناورهای متخلف در تنگه هرمز هر شب تنبیه می‌شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/696793" target="_blank">📅 08:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696792">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550eba849d.mp4?token=raADfBooa-j5QiM52hFumMG2Wapgxh3xb16_jQDns8IvqccA2lfPDLWKuO6QBLb3ewEtU8usuul8FUuRHAMTwyGUrUYImKcj_Xf1sbi3eh5x4-Ar24By9uNrVHjaUZoABjs5X5riZVxJwRcGRnTWddDavuwVqiMs-CJfag6HuoR9_1kvWKis_o7d9A5kqhqZToS8ZfLxnElyf9Sh9QGDzr6etTExQEw0cFVScqnU3H0lu1ONvSDvi-xm8rJr3SbmG__Et8ujYV8Nk-nSQEo4nRwUJbQ_hh4TPw-ehb60Jg2JFH2pRLgjELTKJwVAz5sQL9HNb0DHczkB4FLUdmANqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550eba849d.mp4?token=raADfBooa-j5QiM52hFumMG2Wapgxh3xb16_jQDns8IvqccA2lfPDLWKuO6QBLb3ewEtU8usuul8FUuRHAMTwyGUrUYImKcj_Xf1sbi3eh5x4-Ar24By9uNrVHjaUZoABjs5X5riZVxJwRcGRnTWddDavuwVqiMs-CJfag6HuoR9_1kvWKis_o7d9A5kqhqZToS8ZfLxnElyf9Sh9QGDzr6etTExQEw0cFVScqnU3H0lu1ONvSDvi-xm8rJr3SbmG__Et8ujYV8Nk-nSQEo4nRwUJbQ_hh4TPw-ehb60Jg2JFH2pRLgjELTKJwVAz5sQL9HNb0DHczkB4FLUdmANqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنکیک شکلاتی؛ صبحانه جذاب برای آخر هفته
مواد لازم:
🔹
آرد ۱ لیوان_ شیر ۱.۵ لیوان_ تخم مرغ ۲ عدد_ بیکینگ پودر ۱ ق م_ پودر کاکائو ۲ ق غ_ وانیل نوک ق م_ روغن ½ لیوان_ شکر ۱ لیوان
#آشپزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/696792" target="_blank">📅 08:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696791">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
ادعای وال‌استریت‌ژورنال: پنتاگون در حال بررسی ارسال تجهیزات و مهمات پدافند هوایی اضافی به پایگاه‌های خود در منطقه است
🔹
همزمان یک گروه ضربت ناو هواپیمابر و یک واحد اعزامی آمریکایی در راه خاورمیانه هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/696791" target="_blank">📅 08:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696789">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: پنتاگون طرح‌هایی برای بمباران شدید سه‌ روزه ایران آماده کرده است
🔹
اهداف شامل زرادخانه‌های موشکی و پهپادی، تأسیسات انرژی و مقرهای سپاه پاسداران است. ترامپ در ماه‌های اخیر ۵ طرح بزرگ را رد کرده.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/696789" target="_blank">📅 08:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696788">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
دولت فرانسه‌ در اطلاعیه ای، به شهروندان این کشور توصیه کرد از هرگونه سفر به عربستان خودداری کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/696788" target="_blank">📅 08:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696787">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53d003f8a1.mp4?token=j6i_RBMU26prX7TK5-PoAVqYXj70vzlS_FuyO86bb20acM3asZRE49NiF-4FHVu2dzNql2rVQ91epNHW3-srJZ-ovDmZRlHsSf6AoQhAcPpDKBKf5YO7rzrHQP--L6T3TXrN3BOa-NpmYqQtBf7gHFT4Kpj93GB-QcwSBVkI6zUbXc1DzFZaMcYFiMjP_60Ycp8UQ4mgoRvWpPC-E563EHflghbS9E4BtoGEzOlXCu2Ihpb3VyFaiZJTC6RhsBr-C1UWJACMLmDE8BEYufYwKzo4v3TumfKLCxk0-lun4wqIp3DU6_iPgkCoCOpnkpHrSQHwUx58u5gsrnEZhN_5Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53d003f8a1.mp4?token=j6i_RBMU26prX7TK5-PoAVqYXj70vzlS_FuyO86bb20acM3asZRE49NiF-4FHVu2dzNql2rVQ91epNHW3-srJZ-ovDmZRlHsSf6AoQhAcPpDKBKf5YO7rzrHQP--L6T3TXrN3BOa-NpmYqQtBf7gHFT4Kpj93GB-QcwSBVkI6zUbXc1DzFZaMcYFiMjP_60Ycp8UQ4mgoRvWpPC-E563EHflghbS9E4BtoGEzOlXCu2Ihpb3VyFaiZJTC6RhsBr-C1UWJACMLmDE8BEYufYwKzo4v3TumfKLCxk0-lun4wqIp3DU6_iPgkCoCOpnkpHrSQHwUx58u5gsrnEZhN_5Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از اصابت موشک‌های یمنی به مخازن سوخت یک پالایشگاه در عربستان
🔹
تصاویر ماهواره‌ای ثبت‌ شده توسط ماهواره «سنتینل-۲» نشان می‌دهد که مخازن سوخت در مجتمع بزرگ پالایش نفت و پتروشیمی شهر رابغ در عربستان آسیب دیده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/696787" target="_blank">📅 08:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696785">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
نیویورک تایمز به نقل از مقامات آمریکایی: ارتش در حال آماده‌سازی گزینه‌هایی برای ازسرگیری جنگ است، اما ترامپ همچنان در این باره تردید دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/696785" target="_blank">📅 08:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696784">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
نیویورک‌تایمز: شرکت‌های چینی برای عبور از تنگه هرمز به ایران هزینه پرداخت کرده‌اند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/696784" target="_blank">📅 08:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696783">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7iFjjWICq4hyEuZ7z_Drf9K0c5CMUzXGoLoMKSyJ-oYUFSYdXxWo_Vxv9KdqV3QqUrj1vmEX3VlWYnlXviY2tWA53tfP_zl4RzaWNgu-ciu12QXQD_aBMerNpR86Tgo3PThLjZt4ev8io26-FIzVmmpKN6hCUhnxhx24-2ZcvWspkQJM5K_frA0MvZV1nbWI0A3l9dEo24UNAInIAjdjBUWuXfCtkqIr7X7SqpSwqAXtzfvmWzvg7GdfE8aB6Lxl-PTwzHAS7-tawuBwTMJHeer-p0R1E8w0WGT4atWTkKuJsRBF7cbbUdiqquJUTXY4zH9MQIlB7gIxuf05Gf-vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با اعلام باشگاه تراکتور، علیرضا بیرانوند به دلیل مصاحبه بعد از بازی با استقلال از این تیم کنار گذاشته شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/696783" target="_blank">📅 08:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696782">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XG085OlUE4DhjygDXu2KLL0SqlwguyeAkVnFGcj9sHFyglWbgyT7hTP8TcCLXEuYBIhGVt-7qi95WuVGCNGTOUcbSDDqyJzEp4cVniRLpLmKeGrmXqK2t_jSZ6ZGpFHh6_q0aP1ptuTX31539iZvvu_JgJedNt9tCCu_EuJF87OJcs3tu3pqmzyotVCogW6uh_JacCAID5PBhlJWQBgr3BeCO-BlEmOZjaul7b_lNuC8oXrTbK4hrZrWJlByQQwTNgzMtSlIbX9tmsAsK6SvHvE_GVx7TF2t-uDOUm59b84p8cf-gk3uieZ_9EUcKPnTn1MaXBOrQArddvZNTNRLQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۱۷ مهر ماه
۲۷ ربیع‌الثانی ۱۴۴۸
۹ اکتبر ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/696782" target="_blank">📅 08:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696781">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b1c7cc7f.mp4?token=SBXjTW1u_YkdAgnq-NmFEZDJeYUyq1UA9hfVZEGsF86nNSx6jffqqg89FMrvEMijHWdL-pupNyGoEaJwYkpLeEJ295fstnNAQ9luJSuevl95cpZeESTbycPAre57r10iwuO2HomeKCIwUS9ODCBZ01bAlR5QHXAOUp15ec4uHU9PBPIjvR4kZ6v4yF2ydvZwA7tA8ayoijoGBcJm1Fs1i1e3pai0eLMEwIqlYJxxwaXWwqtNnraRppeMeljuNyvyRCfoY0T-hOdWOjz-D09dX-HZJ1aaZ_1D72SNrLWbYwANy80o6s8Tb5n3ifaQU6XUROySyG57iIzp5vXPtN3rMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b1c7cc7f.mp4?token=SBXjTW1u_YkdAgnq-NmFEZDJeYUyq1UA9hfVZEGsF86nNSx6jffqqg89FMrvEMijHWdL-pupNyGoEaJwYkpLeEJ295fstnNAQ9luJSuevl95cpZeESTbycPAre57r10iwuO2HomeKCIwUS9ODCBZ01bAlR5QHXAOUp15ec4uHU9PBPIjvR4kZ6v4yF2ydvZwA7tA8ayoijoGBcJm1Fs1i1e3pai0eLMEwIqlYJxxwaXWwqtNnraRppeMeljuNyvyRCfoY0T-hOdWOjz-D09dX-HZJ1aaZ_1D72SNrLWbYwANy80o6s8Tb5n3ifaQU6XUROySyG57iIzp5vXPtN3rMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🎥
#_این_کلیپ_را_حتما_ببینید
سلام و عرض ادب و احترام
💔
یک بچه نیازمند 2 ماهه ساکن روستا داریم که مبتلا به بیماری هیدروسفالی شده و نیاز به عمل جراحی داره،هزینه عمل جراحی160میلیون میشه ولی هزینه شو ندارن و بچه داره عذاب میکشه‌ و روز به روز سرش بزرگتر میشه و باید هر چه زودتر عمل بشه
😔
😔
🔹️
این بنده های خدا هیچ کس و کاری ندارن،امید شون اول به خدا و بعد به شماست تا کمک کنید،فکر کنید بچه خودتون هست هر چقدر که توانایی شو دارید کمک کنید و بفرستید به دوستان و آشنایان تا کمک کنن،خدا به مال و زندگی شما برکت بده
💳
شماره کارت
#رسمی
بنام قرارگاه شهدای گمنام(کلیک کنید کپی میشه)
5892107050067480
📌
جهت اطلاع و ارتباط با مدیر قرارگاه
@Hoseinfahmide313</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/696781" target="_blank">📅 00:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696780">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHo62uvjaiO5Kwg6l7xxUsDVAr4NG8W2cx3q9fYyUCIuNGQpIdDi4Gt9Zy6o2t53gA_Bf_YzKXirRHMLS4GX_BmXFo6OB6CKW-y29l09aIQIQD28lqE-PVX4s4EuEfOX8wNxppOV56c9ZfYtiSclJ74nJAz9X7XWB8w12tKLrwvVBV7abqjr-94fyOGnX7_6GL6BW-6Ebn-FolDWKUgWi-DQrW4Y_sLVty4jXhqdikbKRz9s6RUUUu9OxgemqeiNyr4zpoh_H0n9YDLpSEGdJ7WhE47boU1-YeY_21VxdvalUdXfCS5lKCAgqgs0sjhnvr1CGbZ5CJofbVtzPJ8KNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏁
استایل اسپرت، شیک و آماده برای هرجا!
🖤
اگه دنبال یه ست مردونه‌ای که هم
خوش‌استایل باشه، هم راحت
، ست
Motorsport
رو از دست نده!
🔥
👕
سوییشرت + شلوار؛ یک ست کامل برای استایل روزمره
✨
طراحی اسپرت و جذاب با رنگ مشکیِ همیشه‌مد
🧵
جنس پلی‌استر نرم و سبک
📏
فری‌سایز، مناسب
L و XL
🏃‍♂️
مناسب استفاده روزمره، دورهمی، پیاده‌روی و استایل اسپرت
💰
قیمت ویژه: ۱,۶۵۰,۰۰۰ تومان
💳
الان بخر، بعداً پرداخت کن!
🔥
امکان
پرداخت قسطی در ۴ قسط
برای خرید راحت‌تر
🔄
ضمانت تعویض ۳ روزه کالا
🖤
یه ست کاربردی که هم راحت می‌پوشیش، هم شیک دیده می‌شی!
https://memarket24.ir/product/fast/47547/180124/</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/696780" target="_blank">📅 00:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696778">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef79e239ad.mp4?token=eQX-tsZXPRflbjzfPWtecRa2my-_zJFK6md8GNhFjMekrxG_vHsupSRyaSKXgz4XbzbC2DZq7BD_XbYNgvWy11SsiUWHWUO7pyCMMqt2bCqpoL7QWXbGX8I9DjqQXiXsIpQF7GOMAcJabgJzkQkntoq5BX8diFak4YCTc1jtIaK6c8jSl_ZUX5_CTRIICpVuVy968H63wKjsAy5DtUlSojQAjzPj_P9rRHsJQU2wVEwV21FUbDiFhf4oTZy1Nm4xkn1TK16d00VC_GfqyXC6Tv-bfOy-Oi1fmZU_4Z01GGDVKQHGJ_sTH3rwkJBi3xYrrT6Idy01SKAJjx9zOJYaNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef79e239ad.mp4?token=eQX-tsZXPRflbjzfPWtecRa2my-_zJFK6md8GNhFjMekrxG_vHsupSRyaSKXgz4XbzbC2DZq7BD_XbYNgvWy11SsiUWHWUO7pyCMMqt2bCqpoL7QWXbGX8I9DjqQXiXsIpQF7GOMAcJabgJzkQkntoq5BX8diFak4YCTc1jtIaK6c8jSl_ZUX5_CTRIICpVuVy968H63wKjsAy5DtUlSojQAjzPj_P9rRHsJQU2wVEwV21FUbDiFhf4oTZy1Nm4xkn1TK16d00VC_GfqyXC6Tv-bfOy-Oi1fmZU_4Z01GGDVKQHGJ_sTH3rwkJBi3xYrrT6Idy01SKAJjx9zOJYaNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۶ دقیقه مطالعه قبل از خواب باعث کاهش استرس به میزان چشمگیری میشه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/696778" target="_blank">📅 00:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696777">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeR-rDVx0QJpUF9QH2y-plB6DVTthVX2R0oZiuwQwEqHROvKRne_D7clD7krf3uLeE6ehtytD-xZwLL3JvrpFjgf_Opu9LEgA87CfhFScArSAY_-TyVSjHdDK8tWPiHQys0qqJDGIW6_1MjibMur6AmCxy9O3IIlIpHrnHBqXuidNuK_gVtwx2Q15bnux80PqtyDhngPC5Uj8kFLEWxyWLDJKyzi-JVMyJNC0meB3XuDShzhLBqd-7v-AbXS20_37RAhQbwjmZkC7OjiJAMJC8zkP00OlXvUdqn3DejyjkafRAS1escM0OSoRf2FMbloVdexofoYVUCIhs5YuB-vVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طبق تصاویر منتشر شده، طی حمله یمن به فرودگاه بین‌المللی ریاض، دست‌کم ۳ هواپیما آسیب دیده‌اند
🔹
یک فروند، به طور کامل منهدم شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/696777" target="_blank">📅 00:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696776">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6883170c06.mp4?token=rbdOvZszcaYKi5wPs2dxMS3aqoGUL_p_Pew9TGeVyGx6tcSRDjGUPLK7MN2ia2Fi9w3DNvgYh0OLZ9V6k8qJ9sNtS4HSGjfyGvV70MiXoHzioSLySIdCqeuwtMB-R0PSFXu4OC1Doy-QNxy5s2_8WeOyikXmrvR8toh9uMVn2O5hOb271ZEHUqOmklG-FPyRF15j1P_qpRGMh7ZrKJlAc5pKCHeXVaZT62cLXis2hCVtkoBRwszW2PPSW8m5cV3DhXzagQ1sxkwTNNkvwMZvSn6tCvir1gzfLjIUO9tX_TvbKhRyGMxH2K0E7f4OJywSTsDxFySVga8nll1K3YqnlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6883170c06.mp4?token=rbdOvZszcaYKi5wPs2dxMS3aqoGUL_p_Pew9TGeVyGx6tcSRDjGUPLK7MN2ia2Fi9w3DNvgYh0OLZ9V6k8qJ9sNtS4HSGjfyGvV70MiXoHzioSLySIdCqeuwtMB-R0PSFXu4OC1Doy-QNxy5s2_8WeOyikXmrvR8toh9uMVn2O5hOb271ZEHUqOmklG-FPyRF15j1P_qpRGMh7ZrKJlAc5pKCHeXVaZT62cLXis2hCVtkoBRwszW2PPSW8m5cV3DhXzagQ1sxkwTNNkvwMZvSn6tCvir1gzfLjIUO9tX_TvbKhRyGMxH2K0E7f4OJywSTsDxFySVga8nll1K3YqnlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ملودی نوستالژیک گوشی‌های نوکیا؛ می‌دونستین این آهنگ ۹۲ سال قبل از اولین گوشی، ساخته شد!؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/696776" target="_blank">📅 00:18 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696775">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROSCVFn2M5xGk-3r88sh4VJsf_DwmbPxAa_AUbewgeHfoyF7SA6tqUlWUKMNIAlk5nhzXesycOSed9IAZ-w7sWkzHTFw2uS6K1qrVqnI7VyFnQRwhNw0YD5jpPcevMviVnDvr2x-He7G5jJmnN92lM707RWm0cpR6NwMdCjahH9XKPgPRds9ijG62wnS_pW-A-mjXx2-161NH_cVNOFxLSMP83GyV7SMDOsxc8lv54iFKAdq7WKyJqeSz6-WF4jgRn-8BBP7iMR2MFLkMieMOTkNbtkV9WgnuYJ_Yg_gL34kDw-6vaTA-xcqiYyaifXpz0tFAAbAQEVCICnYld5RLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت معنادار باراک راوید، خبرنگار آکسیوس
🔹
نگاهی به گذشته: در ژوئن ۲۰۲۵، پیش از عملیات «چکش نیمه‌شب»، کاخ سفید اعلام کرد که ترامپ «ظرف دو هفته» تصمیم خواهد گرفت که آیا آمریکا به جنگ اسرائیل علیه ایران می‌پیوندد یا نه.
🔹
اما زمانی که این اظهارات مطرح شد، ترامپ از قبل تصمیم گرفته بود به تأسیسات هسته‌ای ایران حمله کند.
🔹
در ۲۷ فوریه، کمتر از ۲۴ ساعت پیش از آغاز حملات آمریکا و اسرائیل علیه ایران، ترامپ ادعا کرد که هنوز درباره ورود به جنگ تصمیمی نگرفته است.
🔹
اما در واقع، او پیش‌تر تصمیم خود را گرفته و مجوز حملات را صادر کرده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/696775" target="_blank">📅 00:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696774">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
وکیلی: استیضاح عراقچی، بازی با مهره‌های محدودی است که هنوز در کشور حضور دارند
محمدعلی وکیلی، نماینده سابق مجلس در
#گفتگو
با خبرفوری:
🔹
استیضاح ابزار نظارتی مجلس است، اما استفاده از آن در زمان نامناسب و مطرح‌ شدن استیضاح‌های متعدد، این ابزار را لوث می‌کند، به‌ویژه در شرایط فعلی که وزیر امور خارجه در خط مقدم مذاکرات قرار دارد و استیضاح او یعنی بازی با مهره‌های محدودی که هنوز در کشور حضور دارند.
🔹
انتظار می‌رود آقای قالیباف با توجه به مسئولیتش در تیم مذاکره‌کننده و اشراف بر شرایط کشور، اجازه ندهد فضای مجلس و کارکرد نظارتی آن لوث شود و انگیزه مدیران اجرایی نیز از بین برود.
@TV_Fori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/696774" target="_blank">📅 00:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696772">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd532d101d.mp4?token=U5AGaNRISv4o0EbKBgeO5byt-Xd_hv9x1bGy6l5ossA_RgiMgAEen14VXlicTnHHbinE8i8d8ugqnIlS0eVUUfF5OMcI0J-B38pc727Q3WExO_fvckQUtFKhtP3HlBCZsnQghstF13Mi_WKbpTtaE4Y3S3zLpwLUBiwLKcCeSZ-Lr33moaqmUL2tvn148XjuWeyiiY8YzEYK4kf9dxMRzqdCeL2WuMXe-e4l7XL1bcVPR70PO5KGA71muo3IU7btXExGsL6k7q_EH5ku2gpQkE7a0zwMIXIG21jznurQd1Yx68pszzNaokLHLhQC3JwoQ7vatDYPDsQEyip24ZEpPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd532d101d.mp4?token=U5AGaNRISv4o0EbKBgeO5byt-Xd_hv9x1bGy6l5ossA_RgiMgAEen14VXlicTnHHbinE8i8d8ugqnIlS0eVUUfF5OMcI0J-B38pc727Q3WExO_fvckQUtFKhtP3HlBCZsnQghstF13Mi_WKbpTtaE4Y3S3zLpwLUBiwLKcCeSZ-Lr33moaqmUL2tvn148XjuWeyiiY8YzEYK4kf9dxMRzqdCeL2WuMXe-e4l7XL1bcVPR70PO5KGA71muo3IU7btXExGsL6k7q_EH5ku2gpQkE7a0zwMIXIG21jznurQd1Yx68pszzNaokLHLhQC3JwoQ7vatDYPDsQEyip24ZEpPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تازه‌ترین تصاویر از اعتراضات گسترده در خیابان‌های فرانسه  ‏
🔹
معترضان فرانسوی معتقدند بخش قابل‌توجهی از بودجه کشور به جای اختصاص به حوزه‌های آموزش و بازنشستگی، صرف هزینه‌های نظامی و ناتو می‌شود.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/696772" target="_blank">📅 00:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696771">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6jXd9jLoP6Nat_OorZBY5YiZV2p_243kUPUmuVNPaUCxe83X1frlYrVTNobXCdpx8jgPkYgOqmk9YWXAFeD8FV288sbI0HcePfY0UiL1mbBHy_9lQrMFknhZjR9raZ8vNvIbbMDWNYoqGw78j4tlmmxo9PP1is3PE13flitFR3KdSdFroS4vwDewTjO9N1JiF7668dUMEj1U10aaf8-sPbFmHyJdbmlDqk6V6pyc8LiV32Otljkf9OeQWNhvaZg-AmxlkHA6F6s0bQfetSPz70aa8lB1xIfWKA_pczu1Su8eBywIumNSwcxIzxVEP9DBE1cD6ah8W69bXA3IDNlJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر ژئوپلیتیک و امنیت ملی آمریکا: اسرائیل درست قبل از انتخابات میان‌دوره‌ای آمریکا به ایران حمله خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/696771" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696770">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpGIfznEg66AcMuV56sbhbj3jPUFEfEvpOLMBCzqoaYhpUhE9gWUTaw8c2f35_Pke_jK9AxauJuRlunGUxho2maNRfKimxdOta5j6YkDXF9hNCeAdVmSXZqBvYlXv9A8MrtXQzpEpK5ilk1cDw0iRoEYR6i0gGrvhzhVEeLnUmMLUdIm2rLO_mOkWyM7N4HOUF7fgveuG6eR-nGk1JWtlra-p3mv5QFNfYoQsEfCx9xdHh0JuClezrjQ2hDBb1hPCA5SrtF3FTpSdh8A4wTdqpJ7ViXPLrJi2duL5lRjNs7Mr1feCgYN5RXLxqGDoRg9G_msd537aR_RKR_gOLeNKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/696770" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696768">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/620d948bad.mp4?token=RFJCSS326be71enLN2ckxO7ctCC_Jyiqr1i6T_GzxYZTsC-hAMFcUkMZ-WPiBhw4_w_LBIGOJowK8ZScZT0QP3K07JRWctUkSXXL02iZBIyP0q7Bm2lhqswGOyK00BfQOhTIIvL7lcMLGmkKkoXlnIlCQAvBaRJ-LACkTziZW1FhbBuKqR_9hJB_d3B5m_DUmibZaPnPtGba671wxxeTI6xY0H2ii4J-wLHva-4bOuCoBRgU3O-aSF-b9UNqN1aV1H5ajrL9A8UZqbQ4rC7_rhDU5_P4O-xU1DEkVYAAn_wzWsGembv3D9fXuD-J9P4PIX-Y0Tpqyx8vio9E5s2ltr4XYPjf3I2aEEhkEzMxjx8TUKW_vo2-qSFRzDTZuDKipcFJLXGBqk7uWuZChQfdsTLnuIW3k9otzxlxZyrsBxEdTo9dsJvHjrtfMlWhqkjUnuuiuTbECv9zVYNCPGtVlDC_dFsZ-Uom89y8pt7wvKLK-2g2kyh2Zvte_NtuCWuk-se93Hoc3bcvg1T5rcSRoy5tG3gnAUFCN4_BAyJlF2IiPAU4VMi8lqyW2lAKyt-mOone-C3jkD4lCO5iarpMq2TVLePEcmGQopwMA6JnK_uPAiu9LWa5MxcNqSkTnW0LfKIesyUrxb7hf8Rk6YIHO_ihFuzP-8SdNnkijKUeqAo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/620d948bad.mp4?token=RFJCSS326be71enLN2ckxO7ctCC_Jyiqr1i6T_GzxYZTsC-hAMFcUkMZ-WPiBhw4_w_LBIGOJowK8ZScZT0QP3K07JRWctUkSXXL02iZBIyP0q7Bm2lhqswGOyK00BfQOhTIIvL7lcMLGmkKkoXlnIlCQAvBaRJ-LACkTziZW1FhbBuKqR_9hJB_d3B5m_DUmibZaPnPtGba671wxxeTI6xY0H2ii4J-wLHva-4bOuCoBRgU3O-aSF-b9UNqN1aV1H5ajrL9A8UZqbQ4rC7_rhDU5_P4O-xU1DEkVYAAn_wzWsGembv3D9fXuD-J9P4PIX-Y0Tpqyx8vio9E5s2ltr4XYPjf3I2aEEhkEzMxjx8TUKW_vo2-qSFRzDTZuDKipcFJLXGBqk7uWuZChQfdsTLnuIW3k9otzxlxZyrsBxEdTo9dsJvHjrtfMlWhqkjUnuuiuTbECv9zVYNCPGtVlDC_dFsZ-Uom89y8pt7wvKLK-2g2kyh2Zvte_NtuCWuk-se93Hoc3bcvg1T5rcSRoy5tG3gnAUFCN4_BAyJlF2IiPAU4VMi8lqyW2lAKyt-mOone-C3jkD4lCO5iarpMq2TVLePEcmGQopwMA6JnK_uPAiu9LWa5MxcNqSkTnW0LfKIesyUrxb7hf8Rk6YIHO_ihFuzP-8SdNnkijKUeqAo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خواب مجلس در روزهای سرنوشت‌ساز خزر! / هشدار درباره باز شدن پای بیگانگان به دریای شمال
مهدی خورسند، کارشناس مسائل اوراسیا:
🔹
در حالی که دولت بررسی کنوانسیون رژیم حقوقی دریای خزر را به مجلس واگذار کرده، تعطیلی و انفعال نمایندگان، منافع ملی ما را در این منطقه حساس به خطر انداخته است. اگر مجلس نتواند چارچوب حقوقی را به تصویب برساند، با بهانه‌جویی کشورهای دیگر، پای قدرت‌های بیگانه به خزر باز خواهد شد./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/696768" target="_blank">📅 23:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696767">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51421db204.mp4?token=ALQpfysu7Rg1_6PUaqQ3MIbgPcR5AsipP1gkFH7-HfbfynoSNEBYjokb1XLfvTbx-_FTjk8yBFpwYec0XzfSMaqCJe4e6xlD9hxwb209xohrHO9A5hzCz3HXHh1U5B4RN9_7q3Kq7wV0N47vqTVhTIlChujm_aBCUkCx1ZrAVL3F0l09z87NDbi2yzX7nFGDW6i6_pmxEey8VX427ogJflx-mh18Ryr0xD5d6CYJIzhronghmQywUJ_m26qzNUg40NJB7k-2t5LM1z_vNBF1LVdgd_fs_MgRoHIln0AtL0XSsXYQgzFvAWCDkek5pmKiBc_tPPLWY8jCeSfMbdbLpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51421db204.mp4?token=ALQpfysu7Rg1_6PUaqQ3MIbgPcR5AsipP1gkFH7-HfbfynoSNEBYjokb1XLfvTbx-_FTjk8yBFpwYec0XzfSMaqCJe4e6xlD9hxwb209xohrHO9A5hzCz3HXHh1U5B4RN9_7q3Kq7wV0N47vqTVhTIlChujm_aBCUkCx1ZrAVL3F0l09z87NDbi2yzX7nFGDW6i6_pmxEey8VX427ogJflx-mh18Ryr0xD5d6CYJIzhronghmQywUJ_m26qzNUg40NJB7k-2t5LM1z_vNBF1LVdgd_fs_MgRoHIln0AtL0XSsXYQgzFvAWCDkek5pmKiBc_tPPLWY8jCeSfMbdbLpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظات نفس‌گیر کادر درمان برای نجات بیمار در قائم‌شهر
🔹
‏خرابی آمبولانس در ورودی بیمارستان رازی قائمشهر مانع ادامه امدادرسانی نشد و یک پرستار هنگام انتقال بیمار روی تخت، عملیات احیا را ادامه داد.
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/696767" target="_blank">📅 23:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696766">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b81e58d9f.mp4?token=L8E_5xlGMZUKSvITR_4h3frnhTV5rJK8LtDVyzVDYfk10hnWRBgZKQwXT3Sxtw3TWNAXLmPiiZZPnOLgC8Ur8iMh9lTQRHYEUEaKBgtiH2MZtiVSqsENFjHxHCWUVUqT63BS6zegKk5_H4nzKPdfPBC4K9zXFXAaU4MVkRM1fmiL4Nz8dG-fFvsRzDDkHizuAVBhdIv7vweAiHC2PGDrPJRcnu57mFg5pZ-s_M-aGwNd2Oo2FlFa21h_nWiQOVlGx2pFcG8I3bOWDzWEBwfVxUnusvTLGFMTA-WPlOM0va-T1SWdT8M5WKoi7dxELFKXVNTArR792H-YudXMw-UhvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b81e58d9f.mp4?token=L8E_5xlGMZUKSvITR_4h3frnhTV5rJK8LtDVyzVDYfk10hnWRBgZKQwXT3Sxtw3TWNAXLmPiiZZPnOLgC8Ur8iMh9lTQRHYEUEaKBgtiH2MZtiVSqsENFjHxHCWUVUqT63BS6zegKk5_H4nzKPdfPBC4K9zXFXAaU4MVkRM1fmiL4Nz8dG-fFvsRzDDkHizuAVBhdIv7vweAiHC2PGDrPJRcnu57mFg5pZ-s_M-aGwNd2Oo2FlFa21h_nWiQOVlGx2pFcG8I3bOWDzWEBwfVxUnusvTLGFMTA-WPlOM0va-T1SWdT8M5WKoi7dxELFKXVNTArR792H-YudXMw-UhvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جولانی دورترین گل لیگ را زد
🔹
امیرحسین جولانی بازیکن تیم فولاد، در جریان بازی امروز تیمش از فاصله‌ای از زمین خودی توپ را وارد دروازۀ مس شهربابک کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/696766" target="_blank">📅 23:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696765">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/764ba72122.mp4?token=KRMDCeFpzmU2Fgd9r_d9KRayxcHImG6lnMnm9w8gOVuhyCePE2B0HHs-yCNowawZug3AIRgE9jbI7DXc5p9a4AWvY3WRw1AGxVRA6KyBjFPTSjUyaC2VXHxee2Ebvz8B18lLRIvyh_TzgoYgwJxsUlKdg_LzXjoDiXqLcurjAT5lqTxw1SqfjvuwRAthoJigmq1-lUfp2Zh9PuOIYmYWfezR80ALUu4dYrBWnd25xoyesWtiHdAtRG-T-6PnWmCKtBhbAYxEGhfOfwGubdVhOQ9blPgJp9OvwqJOuz10Jh5xb0deR4Rtgup6yPSuuSHeRWmdHhU7m-P167_Eog1mpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/764ba72122.mp4?token=KRMDCeFpzmU2Fgd9r_d9KRayxcHImG6lnMnm9w8gOVuhyCePE2B0HHs-yCNowawZug3AIRgE9jbI7DXc5p9a4AWvY3WRw1AGxVRA6KyBjFPTSjUyaC2VXHxee2Ebvz8B18lLRIvyh_TzgoYgwJxsUlKdg_LzXjoDiXqLcurjAT5lqTxw1SqfjvuwRAthoJigmq1-lUfp2Zh9PuOIYmYWfezR80ALUu4dYrBWnd25xoyesWtiHdAtRG-T-6PnWmCKtBhbAYxEGhfOfwGubdVhOQ9blPgJp9OvwqJOuz10Jh5xb0deR4Rtgup6yPSuuSHeRWmdHhU7m-P167_Eog1mpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طبق تصاویر منتشر شده، طی حمله یمن به فرودگاه بین‌المللی ریاض، دست‌کم ۳ هواپیما آسیب دیده‌اند
🔹
یک فروند، به طور کامل منهدم شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/696765" target="_blank">📅 23:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696755">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZxQj0_3UBKnR_gCTZffWxBhg7tLzM-lE8wSUSGdfmPdXHW81z9ecIYeVSPtf_4FnwlwMPri6_WvenqVL8sOsaMD1Gm0d_Uo0xXWLkXk0YtvST43QvhYaaGguYNvIWBGsbFkRfLqm3TzckR3qXIFHKoNqNg7ogOuuE7DF0MdtUn731iGpt8pe-uGqTbdoMQvqED_Itz7Y5xjVcQqmCFq7rfHuFgOubT-pHCTK4q2KJbIXMqKJmE93wzBq3vt-Sv80E3zzkiJVCWe3z0fbaijV2ePZGnP7eSzbE5SxUZlfDmggDnaL1YTV-9EeU7WO_bJaCA2XiMaOLGplrGC4hgzD7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YQGTZAVYt0afXugaibZCM83NH9NJsaVMILHUFVZMfsb2hz55QBV3rGkC7zh6KYD7VnJyJYF_zI85XnfrkhfEhK_N8mM8k-EEcCqArpMmLxTFu9zvGO4-qBPzaL_77He4plWp4r5xDcFJzjybrP7xqMDTej2KIGZobXmuR9iaTGEjLwpMgOwL-6Bf5DfGplph771KYy3ZaXQasRXQQd2s8GVQLnqmPKOQHks1dK1jAxm2NvCl4eZX01Y_LMyDMdiQJRYJTQBnH_F8hX2KVtqnlfrh2C6EjGY7O9UZ_NKwnaOnY2ocfaj7eku-qx0FrzXR9Izi6IjS5ViRPfRE9CnU-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cZPQFfa9P6P5h44whFwKIeQSsPIjR_ltXf_DPAGlegDAoxLts-vFh9XjKx-trQwiEh9Dgg7nq5B56MC1tAXIxL7BrPwsZfTBR_s4UWsst9zzlY0aHHbAdnXC9gAuvABe5r7YqeIpbAA-aBS94ZjhAfZ9_uWyhz3AOzlwNrsAwOrbf3kSnP5_0xk96ZpDKZIMVTtiTNggqCewPZBOYFT86Onl3zr4g88VgTXoOVc1NqoNsH6YuGnbW8k87XMAam3xlpWJiBKOIuymeDGMmRwToq6Yb4TOiuZi8Mt4uFX2NU-DERMqeHmOI6qTSrv1HDDLEsHTmnGD-blknGAPbaV7LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RZP5S8xPDwol0JPE9BA-i4_kIFK3LR0-SP9tCaKSANg0JJJk3exsqcaZUtNRe0by60bhKH6-6whxqzpB0avC_eGb2d_m02bTqcnvu8ZKYKU8CDJCPh3cB4Pv9aIqKpLNSi4cOmvLk4tppghXfw8p9aWMUkWv5IyeiDH4FQJLNwFlB48St7GBzXdb7q0cJYk3calz-5R5o6uC7tAdDAu6eCLHTlmtidJhch0KFOUqFnc-oiiDCpJeYb5JSftBW-eQz-Ys_hbSp8vzVz91exWLI5LzM4G25-C9y81g8okxlSt-dOp94L5hyJ_vPcpR3jMQQKrzeH3BSftqvLTTIVzOow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hLE2uaeF7JxgowXUUileBL7LDY0nPVBmcRYri1xSmH8gdMnvcfTA3DL5eLN8Jim09vAUEV38EIjdUVbc72AAXPOGsKViYYch62LPopJkTWMEfZ6vjXBaqwkU65LZlvF125NGll0geuiWlI-tk8ErVyK7bG87nE_HPnkUhGe0_Rpi9QOuphzxHKBzcnUA8L10hoQZ6VYyMJTAVuFcQtDpTXd1V9JJY5zZWmav254SiGFa_LCS1VXXLdalQk9sn22gruQpahm-rOTEHSemJyCVUgtDGD9Q_l_My4C65Cnk0qaiiWrxBuxGjzgcRdEiDCqB-1OVkgpjDqAePJYG5m5SeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S2x7OJ_rLteIyUrN66Sqred3y2Oy1MErLR9ElKL_UV-VFVPJV7xk08YDWmgXRXDqTYpey2CFzIIgt2JmY8i1quHz2Wd7X4uV1mc9rO96qThq2NQ9EaBbZB2CiSRXO0pvDCmEV2XvjNVbefzCeDg4Z-jj2b0W4aAuFlCbieZ7Jlv9MmNIJNJC9W9GFGu8gwsJEGT2wewJjYVnGYJwwLP8kpdgwuFQROMG_Gcnth3P2KeypjQSZyFO3lRG3j_Js5RXdo3jCqw-oIn-32v4pN9JRHctzww3dZEoSHtooSpNVU5R4r4tDwhnsV5fxdaWcmt2SSMJ_N1TtLGAWwBEP_3u5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/veHNBJyQCs3vxd7P7eTbnPVtEqPYTgbSghjIhtlaB-S6aeAxpNJZ7q7DKqikhdiZW1b7qkAQqTx7wPyq7gCRNTdN0gUOU9I3q5fcKtdSrTLFCaCnF8Enq3ASnI33YfO5-kRPvFkdv34FJDFy7W6j3cQ-sEXoZGoE6YCxHv6KHYU-B18eYXcTCEOV0cDyguN58j-3HsRI9_rop0FvSRs98ByHU9uCHEMBOKSTNzEYPliMPoO-iNiKjfnjwPV-NaogX4_XioLHGbVY_5eA8IZw8C67m6FTCO7G5dMUge3AuK_c9Q6tuqCbwNGdgCB2h0nKF8xqmcELMv7Y7WtsfK0i1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAwBG0zkuu4YS9SxQkUGvn2kUkdR9JDeUGD70REnCMgXVWy-h3yb0JnGIKrhDh6AyUvJwzQKJgs87bYkw3Oyx9ByMJ7-Lmy2QancrKpIXAl_3_4sKdSCBBwT7zsfXbPeKpfkXQVkDr94Nx2sG7rCeJTfPwxArT3H2ZRFpDYerBbJeaWcH65uhZ4hBAbk16RI3vnBEZ1jIhqN3mlVPoGoi71HgfDK6gpVE21ScybyghidLTQ6z-Z14psaYhcQtxxHTDlC4CI4FJ1YOWYwXRgeWn-p4OW6BXJkF1sSTCVM6jEmy7Avg_3j8CUYJo5p9JWiTZP8u1C2ZCSCo0QELFcI3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vwXHdQ2uWlCBb3e8otXJwCUlK7kjTBpc3JdTH8s_eix7zwJACsZjYtAH_t03hVbX5YEI5nEuOOdWYxklN9boK9QPlJxem-TUc5B5q_XGMeUSwo7Q4KYbVE_ERX8OHn_mQ3_dSbK7NcoIc7BMKWs9pV_Pi901j0W0iG3MYLYNavQHJe1PahLSTLwSN2tfDF6yb4KsKsPwhrdJVrJ9EEdxWVetHTGl48v-uSWO9VB5EqAPbLslQlb349v4BWedpQNU35waV8C1QeGhsi_GNTlnG_cU0JL7_x5AbcXNAktXvxUY3UT7F5AoOtwQyNZiHSzQPwgOdiJ9QpUGmCANh1f8xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQIucKq0VOdO9_Oi1a7BctZU-QadZeQz5vpr7ktWIULug2pxP3o2zW-MH05ILVvTJEGeblJlLu31X4H5aXQLaH44NyxTvSL8KQJU4ccOS4Wy5rUoBhffx4mZOGxErKAA5LDFu8RGpZCv6QtnVishR3vUrayScgRkcDlpShmxHgaPiffc5HFDzKF2_5NS8irhdXM7CPEOdk8W8v2fTJ9LJsI0bZ6JKcnaxRQ1jzW68LJXqAZ3_4k-ud4KQ9lRd2it-neQS4FbfIZ_6mJlSXeREE31c5pSAk_s2yxFQ1pfc0bNvytJTpc-vB62qGUjLE6AGYXC5qy6HAR1hkVp7ZpkfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راهنمای یونیسف برای استفاده ایمن کودکان از هوش مصنوعی
🔹
یونیسف برای استفاده ایمن کودکان از هوش مصنوعی، مجموعه‌ای از راهکارها برای والدین ارائه کرده است.
🔹
والدین باید AI را ابزار یادگیری بدانند، نه جایگزین تفکر مستقل؛ همچنین حریم خصوصی و میزان استفاده کودک را مدیریت کنند.
🔹
گفت‌وگوی مداوم با کودک، حفظ روابط واقعی و همکاری با مدرسه، به استفاده مسئولانه‌تر از AI کمک می‌کند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/696755" target="_blank">📅 23:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696754">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b21e8ddcf1.mp4?token=GyLkqvgmgipyx4sW9ueQtUoshAWFGLemxXmSz4MPIQH5_CWZfaxb4HabactXUW9S7FC9lNvQe-BYlkv2Y3PMC8Q7hGTMAw8-VbtTkJfbxahLABU7kgT8FZMEyD0iGrJfUxlsEcYO6k3Mz0rmhxeBlwISBkzXSI6pWXRIMrXDy_xF3SdSOEKfto5O9olbQfWV-KrVCVtHPDrRJR3hJ6y4am5u_75140sTWt-_TH7RAfPCXhBvsAC7kmrY9TbZLB7RjCI44z0JIMV2l1eM5Log2PR3W8qP6gIBOvpHCrdcONdMDXFQWwt3A_ynBP8C4GX6txuKj43axO3nhxXmrClX1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b21e8ddcf1.mp4?token=GyLkqvgmgipyx4sW9ueQtUoshAWFGLemxXmSz4MPIQH5_CWZfaxb4HabactXUW9S7FC9lNvQe-BYlkv2Y3PMC8Q7hGTMAw8-VbtTkJfbxahLABU7kgT8FZMEyD0iGrJfUxlsEcYO6k3Mz0rmhxeBlwISBkzXSI6pWXRIMrXDy_xF3SdSOEKfto5O9olbQfWV-KrVCVtHPDrRJR3hJ6y4am5u_75140sTWt-_TH7RAfPCXhBvsAC7kmrY9TbZLB7RjCI44z0JIMV2l1eM5Log2PR3W8qP6gIBOvpHCrdcONdMDXFQWwt3A_ynBP8C4GX6txuKj43axO3nhxXmrClX1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه شهادت نیروهای گردان پدافند لشکر ۳ حمزه سیدالشهداء (ع) سپاه در ارتفاعات شمال‌غرب کشور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/696754" target="_blank">📅 23:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696753">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Saram Bazare Mesgarhast ~ UpMusics.Com</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/akhbarefori/696753" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
آهنگ "سرم بازار مسگرهاست" که این روزها در فضای مجازی بسیار شنیده شده است، این اهنگ با هوش مصنوعی ساخته شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/696753" target="_blank">📅 23:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696745">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BXOxpj9ExSzXQZL-SIZINnj_nkYv70OyiUPNAb-ojA8DTT5R-pRtJsbF5jePFoYAaOT_lnzhcSDuwkNauGoZ_Cq-nxv_DrwLmCQfjOV9zeLeogsrU51i_0YpGK7vo_yWzO_JlFo068LfUGQyJMFOcxULJi1sd3W2P0RXA0Yf7-BetJ1d1LmpL9pnuGJtwcrx5qPJQHvCT0ptQln5XINl3PaTZfx2ASBy2O8erGIniZU5_luD9AE2i1WEY-mSAUg5WNnYrFOK8XUwdZUG5zKNTwtZKyXYDTaRLf5OfB_nHqHUvSH3nARGVIFK8HrES8_owuNIqN1I9cFbqhtEoURoTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E5vteG1iBNqasIt-V9JAKDmlqdeT_fHcGTm685jbG2lovQbpvJSB83qi1VgG9p2VNj_c8TKqyX4gDXZaeo8wY9Uhtt_NVtSyfMp64SXGA1IB33ytJMhY8E6bt6F3W49JZxiGPHGyJj-9LkIuTu-N0chiw-KOuEEvH98eE7QOY9pJa8Ng-TZapJzvWF9rjqp4Tyy0-SR_ex6BWjkmF0fpzq9tZ5EmUMyp0tLsboR5uck5NdATopbSfLGl4ho1vjjH-ExIWjiBem4VqlZAT4m20M1Rf8B0-iy0xQuZPcSJlVbp2ER1Gt6FQEPTzUqInQpPHqPLB_QYj57ER8R20Ekdag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tfK5RBV2QhaXDSylLjMkgyP5JrjbAu9K4sVx2J7FyfgymgBs1nBm8hIHzhXsO5cNVTQ7zZiudU0UXqz8RT2gC_TIFTevIrm0pLOyLLr0zIRGKWPay9yjuZ2QHcs90Y553U_tsI6Q59LpIho03dacKgnYn9c5c7TKs115ypVA6eX57rpL1Fnb2VGgZOoSdXUt1SgNdcgCcpz2wfXEsQZukJIdVhAh6SQ389t3KXDVy1XukL_dyl-vrdexzrOcf0ndmwVruw_FPNAXnnBFPk7yKkIptOEZaLDskx4qpZUo58VPFpXMvx1TH0BogjF1x8qFNePJqF3ScSfovYcVH2jHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RJuuGa5jv7Ce57OuQ9SdRE67YB4CWXmAe0Voim7rzqajwWBb7dolwxxWoLDs8Grqn4Z0rV3JGye61TxVolzPxo6iqBnY6-4kg0In-NP_dk2Q6dQO7MB9L5Eou-m488NbripR7SrxulGze33Xm1jyASxQV4elT4zZSQp9JwcWd6u7vIgWHlXfRHl9SmV0fqgGMG0MtVXrtygvDrHnTWZnjo7EDpjIxKaPuHbhL9DsS1bwQzBQDuLMAGSgTvLe4_ysNuUuKwWNgTAlbVFiqb6rVZW35y2Ft9-mmjO3vjPUqBxPemSyk7GAYFrLUHQpiEAzCQvFS31pedYtvN_TbZ5PxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iq5iMKbbmauY3pt8vAfNAV4EfgNn4OPIQCjmoOtySc9T46d29Ghof-hZ3uQcOdMN-xG66f1InReNnd771qMHOtJIFRdttOSTezO2Ydy17Hvm8poB_Cyb41bYgxnrxg-BlaC_53ckJ6S0bbKRAbUpaKTXCoMaFjW4pzzvyddWZyfJmU8KMbzueEJDM0V2Ti3AkD07zv5LqdnOFCD4IPJVE8L2DgjDmSlSHk_F0Ye_JkG1lV-6V04n7F0jVo30kk0KJYfeaSVB3DqKhX1vUkPzUaMPvPYan7ewaz2PcwLTJ9AmYLyXwGWtUtqUc9iZsvJIJEpfRjYUDn-wPqaMHNVhhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AABRKiKt2Ww-IRqygEBM8apYsbdyxXnVuSTqtc-X3wjgkSr5GKrXR6Pt07yHmIGGZEvgbrzWmVyyJeSIbSOcablZ0FgG_FoSROsch1pzuofdRgcHjNDS8FySxL_hk560aQOeQbVv3EJkxVZY9PCcrRX1UhNUhVZttofhPc0AkcYjDO66fDQxCkDRO-jRjqgygdI85iVPveVSv3hOomolc8UbzBCvVp-t1tyCgPgGXB4TmSs4M0oywysDd7fP_aqOVIs_ZfqnE8u963Dz6xR70LRY-cRo37UoiH2cVjdcvDqHbSYRAAIAZ6MpaQDG9UHwJGu87_KUFDVavZCv-ud9_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cf3chtz_OChdY11y61kE6gfsnmbSIh2tt6DVam22M1dOXMcabwZfRk2WdjCBYJaBY6Sy4TpAUIbCQwa3PQgUtI7SrGdQvy2-dGnuxeSdX-s0AMo3u7daJjSPYZr9ePZccqxw0KAWkblnVKAd6pDBxsn--99Qgm7FS_y3gltDdO300HZf_E-y5UewntR2sR5KA28yI5X33TBrYRXaeM7eS133lDz3_QmdB9Bk1vBHS43R_0ZndaRdf7yK_qktf9Xj2QqgYm4ntQJeJaBxJvFr9afZrABagdCdlZysHhZCfeLjLR-nQ5VaZno2GjY4_iIfFN3be96xepR9TdCOACjrZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vyu6lqGuJn1FAj-44S3cVw9NAT6TUVFlVLO8eYjjSTSfsn6g931PqGa6z0-06FtyPx8e90IYoKfvzN1oy4cZZggFjnmGBbgDQ-Q86MzUpVwMMxcZy7WkGwRq8YdaOLbKLIloub1PJeQ6w1OBemX_CgEJaUaP4Xjo0gShIeUbrcwB6-X-R-JL5Q3jNNmNXQaIWMGh4hDUOyoNpEwooCxiXsGJ3BuRrbhllOAGc_nlZA1PNebfKYdR0UH9MFDvI4NFkFbc04MtOSZ3hhR-ixQgdM1bw6ZtIRfB_-zzLA5Kv7ewj2XL747KCJ_Ql7mHIDK5ShelwuV714FGAXXec-M3Hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نزدیک‌ترین و مهم‌ترین گذرگاه‌های زمینی ایران
🔹
ایران در قلب منطقه ۷ مرز زمینی با کشورهای همسایه دارد؛ جاده‌هایی که شهرها، بازارها، مسافران و مسیرهای تجاری را به هم پیوند می‌دهند
@TV_Fori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/696745" target="_blank">📅 23:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696744">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEioi0zF6hT_f53bYPpAFxdI7sF6V-Ie280QIlxwVfNu-ewzALrFU60MCulIRlFkYAKxuZukV50X22_cpAE5dJxQVFUY2P4-2LjcvMi2kT8ssn1CjAKs6S6MAose8s3VpRmHgikhrA9eB6bhYFg0xGfoZSGrhNxH4xnYKbfn0lz4WHLbCtgNtH9D7Tz7E9I3T1eCDM017CVehplkrXFao3Toi3GhyJfEKmJNA87407zZ4rUBZ6bdiGrdTjlE4qiRq3RZubJKj4fRvNDcaUTVTGZXKrIwlOQ3X7aPT3SaVZcQdECvllI7Yl8JG3E6OJtXaLEFmGNUvEYFQbFDSdKfLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برت اریکسون: محمد بن سلمان مایه شرمساری است
🔹
عربستان سعودی بی‌دفاع است. فرودگاه‌ها دارند آزادانه و بدون مانع هدف حمله قرار می‌گیرند. زیرساخت‌های نفتی هم به‌ راحتی هدف قرار می‌گیرند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/696744" target="_blank">📅 23:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696743">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
نفتکش‌های متخلف روی مین‌های تنگۀ هرمز منفجر شدند
منابع موثق نظامی:
🔹
دقایقی پیش چند انفجار سنگین در معبر جنوبی تنگه هرمز رخ داد که ناشی از اصابت نفتکش‌های متخلف با مین‌های منتشره در منطقه از دریا می‌باشد./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/696743" target="_blank">📅 23:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696742">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLu3u8Z6xnPlcfWwy-Qj-mEOzSpJr5yCHTulw0g4gk3MAB7XYptlaEME1ZgR7nvTEBI7vPEXCbXj13MdH9Rat2z57hg9SsGv3GJqYhU9GBh8PEIpODUIPiSqq2V4CX98dOYTQ9NFsgjtztiF4rr_X1fYY64GQaV9kGz0UPZY4QwOfrC9cjkc6OZx-nhIDc9PoxXg6LmdI5aILkCq6dEJZvB2zRyP309qCDlEoCDWymkrPdPGqVWPrIESkAfWgzfe3eelJkGMwRldvT8lsH0SYwCXnlostINuekDGvIaI2CSrT6sSV85jAk2bHPSRg086KnqPOT6IOs_JDH4j57txJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استقبال سندیکای دارو از عرضه بلوکی شفا دارو؛
اختراعی: بخش خصوصی بهتر صنعت را اداره می‌کند
🔹
عرضه بلوکی شفادارو با استقبال سندیکای تولیدکنندگان مواد دارویی مواجه شد؛ فرامرز اختراعی با تأکید بر ضرورت واگذاری بنگاه‌های دارویی به بخش خصوصی، اعلام کرد که بخش خصوصی توان و چابکی بیشتری برای اداره این صنعت دارد و خصوصی‌سازی در صورت انتخاب خریدار دارای اهلیت و ایجاد فضای رقابتی، می‌تواند مسیر بهره‌وری و توسعه صنعت دارو را هموار کند./
متن کامل خبر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/696742" target="_blank">📅 23:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696741">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
سفارت آمریکا در اسرائیل: شهروندان باید برای احتمال لغو پروازها آماده باشند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/696741" target="_blank">📅 23:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696740">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
رویترز به نقل از رئیس ستاد ارتش فرانسه: پاریس در حال بررسی گزینه‌های نظامی و امنیتی متعددی برای تأمین حفاظت از بندر نفتی «ینبع» در عربستان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/696740" target="_blank">📅 23:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696739">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ادعای رویترز: حملات به نفتکش‌ها در تنگه هرمز به بالاترین سطح هفتگی از آغاز جنگ رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/696739" target="_blank">📅 23:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696738">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
ترامپ به حمله دوباره به ایران پیش از انتخابات فکر می‌کند؛ جنگ برای رأی؟ | پشت پرده بررسی حمله دوباره آمریکا به ایران
👇
khabarfoori.com/fa/tiny/news-3250780
🔹
سیاست جدید ایران در خلیج فارس؛ آغاز حملات شدید شبانه به نفتکش‌های متخلف | واکنش آمریکا چه خواهد بود؛ بشکه باروت منفجر می‌شود؟
👇
khabarfoori.com/fa/tiny/news-3250874
🔹
جزئیات دو عملیات تروریستی امروز در جنوب شرق کشور | از حمله به خودروی پلیس تا شلیک به مینی‌بوس ارتش
👇
khabarfoori.com/fa/tiny/news-3250857
🔹
حقوق بشر؛ ابزاری که بهانه سؤاستفاده سیاسی شد!
👇
khabarfoori.com/fa/tiny/news-3250902
🔹
چرا مردان پورن می‌بینند؟ پاسخ شاید آن چیزی نباشد که فکر می‌کنید
👇
khabarfoori.com/fa/tiny/news-3250703
🔹
صفحه ویژه اخبار جنجالی خبرفوری را اینجا کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/696738" target="_blank">📅 23:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696737">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYqOQSulgKqPEbRyylAgCrP1feKsh4GeHDnmOKZ6pZaYKWn6btTlulkXEUrwzhZGAIGa4hwfmbFWz5pha3u6cPJGSynfH9XHgDQSNR2sEAGK1rlJ9Da92EskaFLglf7MM0yR50NM8_FQZ3MO7u0tndlg5BRboQA4dKdRYy8MjybmoKCyaBP9JI0r7p6ZLcENApH_ok2JCrf8LJIsuS9dtWW7evhQ5DGBo-tDsR_gYhm6sBKJfoBhf0lad0AaAJHdz7cKxHdgmX8pwvIL5I4B72-Ih7cp7IWGkugybf5T2ywDQ2xKu8NhhkJQX2u_dgP4Oc8Reh2rYbxVu_OD6vNnKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ساعاتی پیش OpenAI با انتشار پیش‌نویس اثبات ۷۲۲ مساله‌ بسیار چالش‌برانگیز ریاضی توسط یکی از مدل‌های هوش‌مصنوعی داخلی‌اش جامعه علمی را در بهت و حیرت فرو برد
🔹
مساله‌هایی که بسیاری از آن‌ها برای چند دهه باز بودند و حل آن‌ها توسط ریاضی‌دانان بلافاصله به دریافت جایزه‌ فیلدز منتهی می‌شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/696737" target="_blank">📅 23:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696736">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddcbdcb298.mp4?token=F6hlN8Kr4m_lhZwYMWu6rAVRCrEHp6gcypG3EF1Hr8qGtB2lOOdZ-pwJc19LE7-WKqwGZuMve2SK-f_HLzhlk1U-8l6khZFAMTMd3jNryz-4p67lYE0ytAgV3pDiDa71Xk18EvkEix14SIfPbZPbM4hfRojEtf6PxcAfLssDFkRoE5TPODAr1KIjoH5vtCj5HO38LQNrviG9Fli-TuHMX12uT_f7KFi-Ff0a0FA3oqPu9cT2lxiSlsrKBH-9vZxNH5rAg35ecKA1HV9JXuULK4jn9Ho1_X5BzHBnyVOAx29VAWAPqLfjPil0Ln9RibMb0DTZ0jpV6hYuSyinK7IFlYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddcbdcb298.mp4?token=F6hlN8Kr4m_lhZwYMWu6rAVRCrEHp6gcypG3EF1Hr8qGtB2lOOdZ-pwJc19LE7-WKqwGZuMve2SK-f_HLzhlk1U-8l6khZFAMTMd3jNryz-4p67lYE0ytAgV3pDiDa71Xk18EvkEix14SIfPbZPbM4hfRojEtf6PxcAfLssDFkRoE5TPODAr1KIjoH5vtCj5HO38LQNrviG9Fli-TuHMX12uT_f7KFi-Ff0a0FA3oqPu9cT2lxiSlsrKBH-9vZxNH5rAg35ecKA1HV9JXuULK4jn9Ho1_X5BzHBnyVOAx29VAWAPqLfjPil0Ln9RibMb0DTZ0jpV6hYuSyinK7IFlYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا جای واکسن روی بازو می‌مونه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/696736" target="_blank">📅 23:17 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696735">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صد میدان 9- میدان نهم، ریاضت</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/696735" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
شرح صد میدان خواجه عبدالله انصاری
🔹
میدان نهم، ریاضت
🔹
ریاضت سختی‌‌ایست که به زندگی انسان ورود پیدا می‌کند تا در پایان نرمی‌ای را در نهاد انسان جای دهد.
🔹
ریاضت توسط افرادی که طلب پاکی دارند انتخاب خواهد شد.
🔹
اذکار منفی که شامل غیبت، ناسزا، اخبار منفی و از این قبیل می‌باشند؛ سرنوشت ما را بسیار تحت تاثیر قرار خواهند داد و اینها چیزی جز کلامات شیطانی نیستند.
🔹
پیش از آنکه جهان‌هستی شما را با سنگ آسیاب خود نرم کند، خودتان به جوانمردی و فتوت روی آورید.
ارکان ریاضت به سه صورت زیر هستند:
🔹
ریاضت افعال به حفظ به سه چیز است: اتباع علم _غذای حلال _دوام ورد
🔹
ریاضت اقوال به ضبط به سه چیز است: قرائت قرآن_ مداومت بر عذر_ نصیحت خَلق
🔹
ریاضت اخلاق به رفق به سه چیز است: فروتنی_ جوانمردی_ بردباری
#صد_میدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/696735" target="_blank">📅 23:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696734">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
کانادا هم نسبت به اعمال محدودیت‌های جدید در حریم هوایی در عربستان، به شهروندان خود هشدار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/696734" target="_blank">📅 23:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696732">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d26f81183.mp4?token=YJk3anzUnpX6E9zXwnbvK_0IoNpDlriebXngjIBKmDotv2ATVU5TjllSEONYnz-WAbSye7064mbCYqwWSRfYV1fEtuLIpD974mDTScWnZOfUo8xUwPN3jBAbOvzY8yiHAws9R0aUFfs5AQURmOZFxxtE_yk4hNycX2BLZzYvLpWwdDzqK9eIqG7bUTvZ-uZ7LlEcNZPsz05GcpBIzaRK5yzUcrIefHgQNZYdolSBLXoYNH_z-VPOo6_60_QaGCA4nYkI7PvJgQThKCqh2um7gfhC4g_jawD8ieTAS5T6GKMGGpXZ6VKjUta7pa3DK4V3iof8CYKVTKOASPZEsD57Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d26f81183.mp4?token=YJk3anzUnpX6E9zXwnbvK_0IoNpDlriebXngjIBKmDotv2ATVU5TjllSEONYnz-WAbSye7064mbCYqwWSRfYV1fEtuLIpD974mDTScWnZOfUo8xUwPN3jBAbOvzY8yiHAws9R0aUFfs5AQURmOZFxxtE_yk4hNycX2BLZzYvLpWwdDzqK9eIqG7bUTvZ-uZ7LlEcNZPsz05GcpBIzaRK5yzUcrIefHgQNZYdolSBLXoYNH_z-VPOo6_60_QaGCA4nYkI7PvJgQThKCqh2um7gfhC4g_jawD8ieTAS5T6GKMGGpXZ6VKjUta7pa3DK4V3iof8CYKVTKOASPZEsD57Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری دیگر از حملات پهپادی به مقرهای گروه‌های معارض جدایی‌طلب در اربیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/696732" target="_blank">📅 23:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696731">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db808e8502.mp4?token=PbDbBdF7NPvAjywvQfxwvVg0pkLbMelBy0F0d6ZaJhe82n7CQ0bhcWS0SwUC5E6Ena8Nk8dULsPh7GfUtux__xuOiyvu0n-88RnpAblWF1n4yWq-BXGTTRIjnILldfGF-CQutRPeRjV2-gvruUmAACkS81xWBRJt9Syrv64ISosEqv-rPYLcVsJ9ZZcoHRzoBy6JiRUCaMee0rzwYQT3JC3Q1S3O5ctLSANL5NxxTrEeP31GfifOTnoKkcJSOh-BO0zMqt3RHPKQ_zdFjOr7yKQ-EnWhsla6DrUfeJjuuy81TQTmDhQrITfANqVqVFGhMq-grJzXzmiaP63F6-eESQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db808e8502.mp4?token=PbDbBdF7NPvAjywvQfxwvVg0pkLbMelBy0F0d6ZaJhe82n7CQ0bhcWS0SwUC5E6Ena8Nk8dULsPh7GfUtux__xuOiyvu0n-88RnpAblWF1n4yWq-BXGTTRIjnILldfGF-CQutRPeRjV2-gvruUmAACkS81xWBRJt9Syrv64ISosEqv-rPYLcVsJ9ZZcoHRzoBy6JiRUCaMee0rzwYQT3JC3Q1S3O5ctLSANL5NxxTrEeP31GfifOTnoKkcJSOh-BO0zMqt3RHPKQ_zdFjOr7yKQ-EnWhsla6DrUfeJjuuy81TQTmDhQrITfANqVqVFGhMq-grJzXzmiaP63F6-eESQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع عراقی از شنیده‌ شدن صدای انفجار در مقر گروهک‌های تروریستی در اربیل خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/696731" target="_blank">📅 23:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696730">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
استیضاح عراقچی به هیئت رئیسه ارجاع نشده و فقط در سامانه ثبت شده است
عباس گودرزی، ناظر هیئت رئیسه مجلس در
#گفتگو
با خبرفوری:
🔹
دولت پس از دو سال فعالیت و با وجود فراز و نشیب‌های مختلف، باید نسبت به ترمیم کابینه اقدام کند، این کار به افزایش سرمایه اجتماعی دولت کمک می‌کند و وقفه‌ای در خدمات‌رسانی ایجاد نمی‌کند، زیرا رئیس‌جمهور می‌تواند بلافاصله گزینه‌های جدید را معرفی و مجلس با سرعت و دقت آن‌ها را بررسی کند.
🔹
استیضاح وزیر امور خارجه به هیئت رئیسه ارجاع نشده و صرفاً در سامانه ثبت شده است، در شرایط حساس دیپلماسی کشور، هیئت رئیسه باید با تدبیر و درایت مسیر را ترسیم کند.
🔹
استیضاح‌های متعددی در سامانه نمایندگان ثبت شده، اما وضعیت آن‌ها متفاوت است، برخی صرفاً در مرحله ثبت و امضا، برخی در مرحله بحث و بیان، و برخی ارجاع شده و در نوبت اجرا هستند.
@TV_Fori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/696730" target="_blank">📅 23:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696729">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
منابع عراقی از شنیده‌ شدن صدای انفجار در مقر گروهک‌های تروریستی در اربیل خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/696729" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696728">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_K_cWydbL-vw-aihbugHJ8lF7JUW3JQk7mk5vPArMs2RWQYdENiv-JPdEnb70I2YiURdpfik8KfYppW02IjdlvGCFtuwgQ0s6edFxZdmaMPsS2NXqa3bjuNQUPXoSrztPhc6BNrA9W4TBDukPw_z1Dbxf49OkHHm3kxO9USgOQtyA7wrKoiAi1ifp_iLbQm6t78U6jME1X4NH21Qq0EfgtmZxc28Vr2qS3ZZLr2rvPiC8_u5c_6jAtjDhwShVTPx0f2ydxEOAXbChfy37Cag9ivLqqEYM0em2tMUpQ4UwKySJSwBuna2J4EN44d2WSTca8KLbqScHpBfyzz185cNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ به حمله دوباره به ایران پیش از انتخابات فکر می‌کند؛ جنگ برای رأی؟ | پشت پرده بررسی حمله دوباره آمریکا به ایران
🔹
آتلانتیک گزارش داده‌ که کاخ سفید از پنتاگون خواسته است گزینه‌های حمله به اهدافی در ایران را بررسی کند؛ حملاتی که ممکن است حتی پیش از انتخابات میان‌دوره‌ای ۳ نوامبر انجام شوند. این موضوع در حالی مطرح شده که در چند هفته اخیر نوعی آرامش نسبی بر جبهه‌های جنگ حاکم شده است.
ترجمه این گزارش را در وبسایت خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3250780</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/696728" target="_blank">📅 22:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696727">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
پزشکیان در دیدار با پوتین: ما هیچ‌گاه میز مذاکره را ترک نکردیم
🔹
در حال حاضر مشغول جمع‌بندی پیشنهادها هستیم و پس از آماده شدن متن نهایی، آن را از طریق میانجی‌ها بررسی کرده و همه پیشنهادها را منتقل خواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/696727" target="_blank">📅 22:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696726">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28cb1d0a01.mp4?token=eeTqQudrnlV2TwJSnVqullhaIfBOBw1kjo1t4GhfTj66RUBJTLeFcy6NZeFhATSD0-Q6GH2Kv_cOyODTylNP66lEomdpan_zMIPgLcAYUsGjaJvuaRUAyago6M2TlV3-uk7q56AQXRVzecVPolXLa801lXwibrRVgmB6ztkV0E_GPP-LvUILypUkOsQ_7ysgw-Sg8Pe7O6tddgJFLZM5MNKAOao7dzKO_FZ5HRxHzDrKa8myZ1nH4VeqoOd_-CCfvWwzAj9oHK-yy_MBqpj_lZdq40U-HpLNSWtlQ_-MoPtRGwLyYhRE-lYGTUd37mU3IoN5MIM6PqppqpVn_KOo9jro6uK-08U6hM5tV_n53go4t9KmrihKrKiqPEoYPOp6rLEelUxb3uHDXBcLBv_gCRM8HtTegB36Unf7ZwSpUvMeyRs_z0N7uL4NU6CRr5orexaWUqkE2TRZ5D_w50kxAsv6RbaFXF4xLrUSmIfRdF8eo_6T6b0dt0m3dlkPOa78okno6HA816KylAdcUq27nxmOpJparkxThD7-AZ4P_cRV-9Qc6zxtnT0iJiyPFnemO37xHW6Hpml1xvYKRE4MBxOJ808QJDuOywil0nmgkE16WMFLDOnm0RGvol5O_GfqiN0hc_dK7-Fk1VReRJEywEhv325_KCLFkdUjbH0h9Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28cb1d0a01.mp4?token=eeTqQudrnlV2TwJSnVqullhaIfBOBw1kjo1t4GhfTj66RUBJTLeFcy6NZeFhATSD0-Q6GH2Kv_cOyODTylNP66lEomdpan_zMIPgLcAYUsGjaJvuaRUAyago6M2TlV3-uk7q56AQXRVzecVPolXLa801lXwibrRVgmB6ztkV0E_GPP-LvUILypUkOsQ_7ysgw-Sg8Pe7O6tddgJFLZM5MNKAOao7dzKO_FZ5HRxHzDrKa8myZ1nH4VeqoOd_-CCfvWwzAj9oHK-yy_MBqpj_lZdq40U-HpLNSWtlQ_-MoPtRGwLyYhRE-lYGTUd37mU3IoN5MIM6PqppqpVn_KOo9jro6uK-08U6hM5tV_n53go4t9KmrihKrKiqPEoYPOp6rLEelUxb3uHDXBcLBv_gCRM8HtTegB36Unf7ZwSpUvMeyRs_z0N7uL4NU6CRr5orexaWUqkE2TRZ5D_w50kxAsv6RbaFXF4xLrUSmIfRdF8eo_6T6b0dt0m3dlkPOa78okno6HA816KylAdcUq27nxmOpJparkxThD7-AZ4P_cRV-9Qc6zxtnT0iJiyPFnemO37xHW6Hpml1xvYKRE4MBxOJ808QJDuOywil0nmgkE16WMFLDOnm0RGvol5O_GfqiN0hc_dK7-Fk1VReRJEywEhv325_KCLFkdUjbH0h9Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عجیب‌ترین چیزهایی که از داخل بدن انسان پیدا کرده‌اند
😳
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/696726" target="_blank">📅 22:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696725">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
دولت انگلیس در تازه‌ترین بیانیه امنیتی خود، به شهروندان این کشور توصیه کرد از هرگونه سفر به مناطق کلیدی و شهرهای مهم عربستان خودداری کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/696725" target="_blank">📅 22:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696724">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
پزشکیان در دیدار با پوتین: با ادامۀ یک‌جانبه‌گرایی آمریکا دسترسی به صلح غیرممکن است
🔹
ما از شما به‌ دلیل موضع‌تان در مورد وضعیت منطقه تشکر می‌کنیم. روابط ایران و روسیه در تمام زمینه‌ها درحال گسترش است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/696724" target="_blank">📅 22:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696723">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
شهادت مامور فراجا در حملۀ تروریستی در فاریاب
🔹
سرگرد مهدی جمشیدی، از کارکنان نیروی انتظامی، دقایقی پیش در پی تیراندازی افراد مسلح ناشناس در مرکز شهر فاریاب، به شهادت رسید
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/696723" target="_blank">📅 22:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696722">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
پوتین در دیدار با پزشکیان: بهترین آرزوها را ازطرف من به آیت‌الله مجتبی خامنه‌ای منتقل کنید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/696722" target="_blank">📅 22:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696721">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
دولت انگلیس در تازه‌ترین بیانیه امنیتی خود، به شهروندان این کشور توصیه کرد از هرگونه سفر به مناطق کلیدی و شهرهای مهم عربستان خودداری کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/696721" target="_blank">📅 22:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696719">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
سخنگوی وزارت دفاع: تولیدات وزارت دفاع در سال اول دوره شهید نصیرزاده، ۸۰ درصد افزایش یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/696719" target="_blank">📅 22:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696718">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xln-wkxRigAWLPKHGsindA2IhmiDhcvq8X2HMdbVzgQ0_GhbDyf5XE5y2wqvtcEhztmc0rxq5XZFvrkfaZ95slb1L6Xtv3M6k1HRFmh6n_S-Vt71yj8dcnTBRuYEtopXZwU9y6rGbM3tP47kdLoy9_3Gb8LoKsWfpRlXHauJ4runilGB_xAuxQPtz0W-K-K9ivDlrWv6Tl59YPSDgJqsBV0_kTL7duXVhGDTfLuoA6M0q2u_HUCcSLM58Sfmfopj2M_ix-wTUs6Pz7QjKcudPlp9JTlZs_6lrEXVurv8GyZiA6FbUakFeB8Dl-PkYFqWQKHQm_GlCMnYiwZE-hJfDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کارنامه مالی هفته
🔹
در هفته‌ای که گذشت، بورس با رشد بیش از ۲.۸ درصدی بیشترین افزایش را میان بازارهای این جدول ثبت کرد و در مقابل، انس جهانی طلا ۰.۷۵ درصد کاهش داشت و سکه بهار آزادی بدون تغییر ماند.
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/696718" target="_blank">📅 22:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696717">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سخنگوی وزارت دفاع: تولیدات وزارت دفاع در سال اول دوره شهید نصیرزاده، ۸۰ درصد افزایش یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/696717" target="_blank">📅 22:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696716">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39c6f84fd8.mp4?token=S0b7BAsDh-MCsieverRlTtUZAqum0rY9qCl_jPcnvUCabggq0iATPt0ywdAC7LTUF5_OqnE4V8XEOZ5sBeCDb1E3hA7pFfGp13-2i9nVdKfa-2KNsq4wkSYR-f-yAzmibqtTypKo1hf_s6X2Miof_u14ZVwW0SWyZNMl_6I3Tey23ClS_oxneBCQ7Z2qWY1Dc7BQvHE94KTnfRxBSTS2drYILHQTF0qYSrhf-LFz_uK2XuE0FvzCVxD4EpZUQX1uo3opKtsoTZbQkUcdyEZ6tHkG-iV3bJW1xJ_W_V9UktTByEwBZE9wIwnyCkh7PHt9nJRCk3KSyvwKJ6TS2VsBjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39c6f84fd8.mp4?token=S0b7BAsDh-MCsieverRlTtUZAqum0rY9qCl_jPcnvUCabggq0iATPt0ywdAC7LTUF5_OqnE4V8XEOZ5sBeCDb1E3hA7pFfGp13-2i9nVdKfa-2KNsq4wkSYR-f-yAzmibqtTypKo1hf_s6X2Miof_u14ZVwW0SWyZNMl_6I3Tey23ClS_oxneBCQ7Z2qWY1Dc7BQvHE94KTnfRxBSTS2drYILHQTF0qYSrhf-LFz_uK2XuE0FvzCVxD4EpZUQX1uo3opKtsoTZbQkUcdyEZ6tHkG-iV3bJW1xJ_W_V9UktTByEwBZE9wIwnyCkh7PHt9nJRCk3KSyvwKJ6TS2VsBjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای وزیر جنگ آمریکا: ما قصد نداریم در ایران دولت‌سازی کنیم
🔹
همچنین نمی‌خواهیم شمار زیادی نیروی نظامی را در ایران مستقر کنیم و کنترل مناطق مختلف را در دست بگیریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/696716" target="_blank">📅 22:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696715">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
پارلمان اروپا با صدور قطعنامه‌ای ایران را به نقض حقوق بشر و خشونت علیه غیرنظامیان محکوم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/696715" target="_blank">📅 22:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696714">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5Vw2bLGI8u95BEZbdKxXf-xMNPWPvmkSb7Y4l6jsFVbf8cOsVQhj1KfpPTryWEwiG1QBPqbXkSc8UoUfhENQupC2qF035N_rkMVcvqiIYUMhiOQBi8ja64_aq8buCWWc3q5z0NS9jrDBu6b4gG6WQpWPG1xylkmanx-0Xc-UedqNfzeRgI4dH28Dbskz-XBtGq2zc099qU8rw3Q6otccSxyakl3D5aG-eWcqsg9p4caLXkwGq_mjbJX443BwUoEd7NJI1JvWrehtSXk2VQJ3W9mFAZNrsGbkgLjoBVTPH6O_xjuGI1ioCp1BbjlGnL6B2sy4OJXXcKfjVDDaO3aJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نایب‌رئیس هیات‌مدیره سندیکای مخابرات: صنعت ارتباطات کشور با وصله‌ پینه اداره می‌شود
🔹
فقدان توسعه زیرساخت‌های ارتباطی در یک دهه گذشته، سرکوب دستوری تعرفه‌ها و فشار مضاعف بر شبکه موبایل به دلیل تضعیف تدریجی اینترنت ثابت، شبکه ارتباطی ایران را در وضعیت بحرانی قرار داده است. بحرانی که به گفته فعالان این حوزه، دیگر به قطعی یا کندی اینترنت محدود نمی‌شود و مستقیما امنیت ملی و اقتصاد دیجیتال کشور را نشانه است.
🔹
به گزارش پیوست، فرامرز رستگار، دبیر و نایب‌رئیس هیات‌مدیره سندیکای صنعت مخابرات ایران، در گفت‌وگویی با بررسی دلایل افت شدید کیفیت اینترنت و چالش‌های اپراتورها، تصویر روشنی از وضعیت امروز و فردای صنعت فاوا (ICT) در ایران ارائه می‌دهد.
🔹
او معتقد است ریشه مشکلات شبکه نه در تحریم‌های بین‌المللی است و نه در کمبود ذاتی منابع مالی؛ و در حقیقت کج‌اندیشی در سیاست‌گذاری، سرکوب غیرمنطقی تعرفه‌ها و بی‌توجهی به اقتصاد ارتباطات، این صنعت را به لبه پرتگاه کشانده است./ پیوست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/696714" target="_blank">📅 22:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696713">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ادعای آکسیوس: آمریکا، اسرائیل را در جریان تدارکات برای احتمال آغاز عملیات علیه ایران ظرف سه هفته آینده، قرار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/696713" target="_blank">📅 22:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696712">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxDbY1FXg204zb7nlN3yRV82Lp_H7d9FhLS_b2KQoEfSdK9o2BiX5fVC-GkNz6AqIcOO98PFI7j8vtes8HwVweIAgy1-GVp0AAt7nMIHX0o_szwYeO3pPNii5fh-0myfhH_3uCx3uTCAlGHodMmyBw391MJxmoK_R17SvqJs20YU9UWX7Ob-gipgaq_uO00gbnhnT3mWYiDHsNaqX1ixXnQSFfcj2qK8HE_crY0H4ZzF4uJh9p0CfHN-nnOvlv9catAq4UI0ySsFjUFDxomXM2zBSH7dtc_rSSQGXyr80X9FhMtXrmizQxyfUtZcXjOuYRqeo7kgCR3fiLkZT7hbyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با چند تغییر ساده در تنظیمات، شارژدهی گوشی را دو برابر کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/696712" target="_blank">📅 22:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696711">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
رئیس اداره آموزش و پرورش کیش: تمامی مقاطع تحصیلی در کیش، از ۱۸ مهر به مدت یک هفته در قالب غیرحضوری فعالیت خواهند کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/696711" target="_blank">📅 22:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696710">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3LaDSwo_I5B_oT1YQcXY08hceSDOrC4kB8fFoM28yK7c8eBsf4OB1YTcOgw1yhFCYKzDYDe-klgGMAnG3Fl8l3FV0vJzz6IWl6PX_yWnXhig0CJj3P1IrJvCHnJRtzRTHhJf4sRrYc5K9Q3i1bEh_VbPn31LjhiVzlA9yOhfg4_271-hlPNA__s5HlhPC5lbtl93sxZ9OPFM9Y8LXpKumwEkNerawajMH0d3L1PJwjbILuX2RFgccYyZJiGjpUMfILvDOKilqdCmwhQ1VlBlohvucQRQM3P5iw7kGU760738hh7n7f_22zviU_ywUvlGrHRpOn9bgX0NB6wPfgx8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طوفان در تهران و وضعیت دریاچه چیتگر  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/696710" target="_blank">📅 22:08 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

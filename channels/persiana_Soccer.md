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
<img src="https://cdn4.telesco.pe/file/EU5c2yAGjUBlWox8KcvH719BvL-vjFYZQNAhIakn7AAq5HIIESIQ14X3JtrDHabn5MUrZmFP2Ih4jn_OnIUWroAlIA944hM19StBUUC16xcCq83NS9uz3_WV7XJyu-h6_4-I_OSZe1kr0f1H807Rfvo0kyDYGkK_RGEjYDBX14Jj2BM2P1x2dL67EIvzeTQGkeQ-_8ecNBSsISO0HWR3fWAygNbUzppnlKHMqwgKUqihvNsxLUrTeVJwMSyt-mecCY-BsVXdRO9BILqPmEfiGeTvbJSoq5LI_EACeEbdwrCESit2_AUK8B7k05npJKTkPvigpGnytCF7AWsyBdbpGw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 323K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 19:16:34</div>
<hr>

<div class="tg-post" id="msg-24474">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlU--fywcKBQougDMHneCF8p1u9upW9z71z0NpI51l-Q1AKKJbYYj6AmtkfOQARua7IFaUN8xBBOrjKqS9krY_3lNYissD-isN8ne6X9bGOC0qRfxuSzqPZnCLcZE9szX4SjmptZXbX6ODQwOJLcLGN_pOeHfcAQIuQJ7O7arMisNYv4NLlsjedxaeZvSlRIZ0Ff7ei0jFjpaGxBL06JBbB9WQqDFDDzsfUVFEdYFTetG0EQ9QDk8XdMifPITKFAb7gMG6UFPcq-X__dre1yavqFS0QOavptwiRpiDoDjKyG6UD5SocWnd-OAduBVNrFTGyC936e1z-C2At8k4JDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/persiana_Soccer/24474" target="_blank">📅 19:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24473">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0SGpEhvj3pA0QjvJPwWQtSdljBzk7o0mIgcNackYvZN_ANBNL0EiZZjMStPUmhl1vD5iWaK04KywXSI9KiQgdLJZLndo8mtMg774j4eUWlfq6xR44IPLIDfCtwNmTyx1jga4ewv3I4iCZy0gkkUfOHr0hSWQY0UD5kSn5KbG7ko-B2OwGobMWzNif47JRaIBhDOyCHHx4aNp9b_s17nr4daPnSLDXg8zPRJ1ZqQsYAFUbAhp0cSmQSzgJ_qsVxz02oGOZFISFbJoB84ZSMLnpzNB2aqdWuqb32vg_m3krA1ZSvL14RVCuFjGIr3cmeLYiQhYJuOBc7i1ehDXyed_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/persiana_Soccer/24473" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24472">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=t97c1llWse_8seqhPTcGZ9iKvh5un0YDVK0Rk1LEThbPDTrAyEbh1IgzYgJnijVCClt1AeJo9YSHEBfayiZd7fA3rt-U8h82XDPQpDX6tOgNtUBfmebaw1P9EfRJnUdLjNKrwozV2lRQ5NR5vvITzX-xeA3vRHEfjnH5PkopSBNUC1sZd021MZGZ3dHgpIaS1DxFKz8yhypa7pWMS2T5OClmxU2zVtc6cfHAsjuyMhX4VyhkEtduyaKSjmuKIOeRW2a3r5vuGclFwdhDbKLJZEAf59ncftG-_0XdF1TstSm2f-Es4JVWQwWzmHjVBV5TAS7iE_U3aGwjd1VsmZkbSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=t97c1llWse_8seqhPTcGZ9iKvh5un0YDVK0Rk1LEThbPDTrAyEbh1IgzYgJnijVCClt1AeJo9YSHEBfayiZd7fA3rt-U8h82XDPQpDX6tOgNtUBfmebaw1P9EfRJnUdLjNKrwozV2lRQ5NR5vvITzX-xeA3vRHEfjnH5PkopSBNUC1sZd021MZGZ3dHgpIaS1DxFKz8yhypa7pWMS2T5OClmxU2zVtc6cfHAsjuyMhX4VyhkEtduyaKSjmuKIOeRW2a3r5vuGclFwdhDbKLJZEAf59ncftG-_0XdF1TstSm2f-Es4JVWQwWzmHjVBV5TAS7iE_U3aGwjd1VsmZkbSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زلاتان و تیری هانری هم نتونستن جلو خودشون روبگیرن و تشویق جذاب نروژی‌ها رو انجام دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/persiana_Soccer/24472" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24471">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fqwCBfYfCGbQ2CNMUYa-K3lN1xZEozQ5e4T9U3TKYkLPRmoQHmD3sQqJTjhaxxthuDH3xiAUMU27qln_bTfcBPbV0WcWFIALFcsHItqT86ASRdFBptMwmSIBeIJAbbe5YOqjRXbnw0VwmS7POXV8sbmJ99J3K5rGSjQYyj3bUkXjcs6hD2rlT_mfvEb43p85eCHh3-FWtDCLPiAA8dRWFpYb8SSRcmmAs2Cv5W11Cncl3hPDnqRdi-QZt42ZDDHoLygyig2kIfKRL-geTkEJyZESm2m4ajx2tvECxNpVK6NKC7WvUdPHeBV-vUye51EBN7wLvV3w6fz8J_BqPRgvMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
با لنزبت، هیجان بازیهای جام جهانی رو چندین برابر کن
🎯
⛏️
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔣
0️⃣
0️⃣
1️⃣
برای هر واریز
🔝
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
💰
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از اولین واریز
📇
امتیاز وفاداری با انواع بونوس های روزانه مخصوص کاربران فعال لنزبت
🍀
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
G6
📱
@lenzbet_official
📱
https://www.lenzbet.cloud</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/persiana_Soccer/24471" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24470">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rzddh3S9A0gKM9d_5xrvTtgPkOhFIhW0NqkuqckpUDx5oA3yCSEPa-O4xU-uM_jJDZvFKjX00pQ_PF5cq5JhA-nTaqazCLPuAqieV8RWPdavUYsyi2lL5MwL_tax_OjEJlTerGEQwYbrvgcioCHRpu4IRmL3T9VtDMpGoO01PpIVXxPED7GtD2VgLv3XtS81mt3OiawRZsUdSGbmnGIznNujeQqQAjECF0vI--9qu-K9DkLlPgXdlBM3MLmceT5HZAty5g31G2v6EIDrA_f6VcG9XulXlYg4QxPVe2KPE_neHp9TgoqHKotV28JudU-kvRjzoxHLUBTSEljC0lUtTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇺🇸
فدراسیون فوتبال آمریکا در اقدامی جدید به فیفا نامه زده و گفته‌آماده‌ایم که رقابت های جام جهانی 2038 رو به تنهایی در آمریکا برگزار کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/persiana_Soccer/24470" target="_blank">📅 17:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24469">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTJPecoUXtUKZFl5nT0gP0Hr5Yi3GNSfXuOIM_onkA3mrYjGZxghDJTNt2jJNRG45QYlNATnVTQ_4o7OVhW5BAe8zvjWUW_OnWBd8JP2udf1VV73CLF_aL9jJPQSqCgpyo2NtRtUDjIwAkEZ7PohhGEwsfXhPYm0AHuKMVXzFkvcXA7rOtL5fEFCM0J1QFSdRXGE0aROjDe9vo35J7yeaxIHKRjKuZI7La8moL3LkONYXSxvWTRPGcCKZWAndSX17g6R0IMCRavVS_0VL9SgMSZNkpRPkIGUv4-QMlXudaMWkj1OdmY7ApgUIRVMPhpOFWfI7UXvUH6UCzwwYHA-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ گابریل پین دستیار فصل گذشته تیم سپاهان از طریق‌نماینده‌رسمی‌اش آمادگی خود را برای عقدقرارداد بااستقلال و اضافه شدن به کادرفنی سهراب‌بختیاری‌زاده اعلام کرده و علی تاجرنیا منتظر پاسخ نهایی سرمربی‌آبی‌ها دراین‌باره است. این مربی ایتالیا از سپاهان…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/24469" target="_blank">📅 17:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24468">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kbnnzt24GrTjoQjNMmcP-AAzOvgGfvU4zUeRcBsKlNdm7BrxToj5kfV7REotrF_W3_Nysd2TtqYDg9fOyTTeOTkPLBe6udTfsxDVtF9vpoI-n8m4p5j-UKJd-ZGTgR9IpD1WTrCUxxBXtxmU4vx3Lsu2VwRgSDJaHREkWkSZfvpj3czoLTm15aIe4xWOrPvEW8aDcIHB7GmFrRjrG2kOHbokg-x53NC6S5xhpz9UNV1dxvtn0aD0xtgocQLCsw8IaX2oI8BBXEwrd13tNLmnAmK5-jQRPIiLV4eWzDwAsqGA4y9Eu5fXYBOyAHkwoJAJKxPuNoyeUreSTtT5RvBjCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دخترخانوم پاکو خمز مربی سابق تراکتور در کنار خواهرش؛ بعداز اینکه نادیا گفته بود دوست داره به خاطر رونالدو پرتغال قهرمان جام جهانی بشه رسانه‌های‌اسپانیایی بهش حمله کرده‌بودن‌که‌گفته‌‌من‌‌فقط نظر شخصی خودم رو گفتم و حتی اگ در فینال پرتغال مقابل اسپانیا…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/24468" target="_blank">📅 16:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24467">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsGMifHXJV_0ZrtRNJ3rbkAmZr-ngSeE1zOuxU6vfNOkW-cV1L8hzjqf5rPBGwb1I1Kg4B_JjC1qoms47XPbNjhWsN2qYaPIKJvO0ClmpinhSWxlDlZtNz7zzmzWxG8wotI2kwcdNvJkO1zbOhw1nqu_hNkPbUbQrqRS2Cp7z4p8H8Nq6Uai96T_W1yqhmP-T3viTkFWQRQ6xVcEXoOv_Xlv0CSLw6h3UE3ZFDJWOG1nAEjUQo2EQmEvi4q2LgJxrFHEU6F8hujtwSfa7OYXmYpxjN5kS-c_pdH1EHVqGe0Q5jr0rlLZW73GClosOgXoEeyvSphlMbF4e0H4l_Qfvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛ باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/24467" target="_blank">📅 16:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24466">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7vx4BE_YWhYp-qqyioLFeqUj8GgJCHUy_YzzeyIdlxCl3ZsQEV7kMmCvlU-K-XEcszK6uiWeAdEVQ50SZFZ8Op7L-NZmOp2pOQvYSFd7RytCABrnmpJjHXskgXj6NTlcxeU6Up9moMsLme2tJDn2qJ23L7-x6dImAl-cTR-H69wGspkiwrS43T9L20EYvogwCTN2j9Rb1ylInsvN22EN4j5YvVAg3imdOZqqbbWHTtCeI0rkQXniQUme5F5P2z-hmpT7NbAnIzwOMIlN8yIxcZAiQCIWCKEeM_uwRQM6lD3baFHYAqer08ZEvFO0C-fgchhbIzUUWh0RJ_AS8HA1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جان سینا اسطوره کشتی کج جهان:
ظرف روز های آینده برای امضای یک قرارداد اسپانسرینگ مهم با همسرم به ایران و شهر زیبای شیراز سفر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/24466" target="_blank">📅 16:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24465">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKk7FD0gwumuwarwtXGYgoh-OyNcOKDM8CVOzSJDGtIqzSnznYLTVgNrbfAIcapfBSHqiQi35ojy1ZiSEy3IgwF-WMJdBaLtdHlw1IMysazewyfqibwOY0UGK8jsh8kXKmZmkwBVn-6cEUSTlByqtDtNcedPmkO_OmIfWq5d74jH6QQzmkI2cvT2lBl9e2hkfU-3ung5oIWuKbfccGnVQSC-ngi6ASblBZXwT1t76rEi3P92hjPv-uCR4GJvSqDjrwSvo2fRfnPCeNdsdWBVn0GuMgVwhu0FEmhCb6Jp_E7YkcYu2YUhghYtck3G20Nvqai5d8AbULWV3tB-UOfB2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌ برای‌دراگان‌اسکوچیچ بلیط گرفته و این‌سرمربی این‌هفته رسما وارد تهران میشه. قرارداد اسکوچیچ با تیم پرسپولیس دو ساله است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/24465" target="_blank">📅 15:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24464">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZhQR8zLAb06zPZjceI6rn8cGlFMcY-LZLJPltvns64eMiLa6cZOySGqzhnpcVOIazMSexACUAzWV2ZWdoKqMkxxXVWUlFUUNH3v1fy-nlZqZUYPd9wN9rnhlyuz32sKPJtRo13ZUnEeg0NIQ2NSLoY3jhCR4qHuATqxjJo0icH_YoBgpsXv4OZ_Wly7TAtdsy5EPTEdGa3Yl3FKxCBxrR7bA5c8T8khcIH0-lkkYDabrZfvLsOC5AauDWRmA8fzDziE2J9WLx7tTcr36JaV--P-JdYrbGYpdEV5szLCCBz1Iv3iK8caxnb_0o3pJiob2KIkx13_0UQ17YecLuxRDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ
: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن موقعیت مقابل آمریکا درجام‌جهانی 2022 و عدم‌صعود ایران به دور بعد، گرفتن کارت‌قرمزجلوی‌تیم سوریه و خراب کردن موقعیت ها مقابل قطر در جام ملت های 2023، قرار گرفتن باسن مبارک مهدی طارمی در خط آفساید و مردود شدن گلش مقابل بلژیک در جام جهانی 2026، خراب کردن پنالتی مقابل مصر در جام جهانی 2026 و کشاندن ایران به اما و اگر برای صعود به دور بعد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/24464" target="_blank">📅 15:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24463">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNTX46FQeGlwsJtCe-1cxbVYYqrDvHmc3yjZe87upnD-_IKDz2SGhP4QucuhxOlBXklAEk3EqxDX-2svTlJU0cOmMK1zhRKBCaPb4JgkbNWH-OmVGRPYbXuUinbCayZeUCnK8bVC_K4nLepn7LvTenlOkfkDAXYwjCv7N7CeMRbYU5lJDcBv2I7xqio9q-a0IF6xfgithKiklkPQxbFGBYU8SSp-sySonC4RZfdrOaRTrsZR8Jhh599zcnVjb-YfpkmUONpFHgK803u3B85Ll7zbjHdfpsgPqYEkrytbaRoduYclDvCpHhxA25BSdxH9F2zEjG_I2020TpQK40pc4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/24463" target="_blank">📅 15:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24462">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30dc88d38c.mp4?token=HNjWfMpwIuYeRpHM7VcT-ZAQc8flttrJ_SAF71c6TsTSvTmzMgeXp4fpk8mvN_WmHB6OX0BTHQbqsvnM4_ZKrnI2UVQOLkNM2DUpKhfRsLtkVnqTX-b2zGpgUIxTF85rGiy7QHeWO0zABNQ0pCJg7OL_kK-lWBxI2WkHVdcj9nhFbrbl1gBiOkEplqM1kzzbDv4V7Q-Inwoo4JXM1SzUSuojKeU6J7dqNkF84rI5oLEYRdzjWBNyD7XeZSB7X9NBxsjyS8_iPJ5Ob0qzA-Oa1Gni9EBV_BojHELVEBxGCmMVweJ9riaq2yUWEGXvHmh4zoS-8ssh_Acx-k1doy4njQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30dc88d38c.mp4?token=HNjWfMpwIuYeRpHM7VcT-ZAQc8flttrJ_SAF71c6TsTSvTmzMgeXp4fpk8mvN_WmHB6OX0BTHQbqsvnM4_ZKrnI2UVQOLkNM2DUpKhfRsLtkVnqTX-b2zGpgUIxTF85rGiy7QHeWO0zABNQ0pCJg7OL_kK-lWBxI2WkHVdcj9nhFbrbl1gBiOkEplqM1kzzbDv4V7Q-Inwoo4JXM1SzUSuojKeU6J7dqNkF84rI5oLEYRdzjWBNyD7XeZSB7X9NBxsjyS8_iPJ5Ob0qzA-Oa1Gni9EBV_BojHELVEBxGCmMVweJ9riaq2yUWEGXvHmh4zoS-8ssh_Acx-k1doy4njQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/24462" target="_blank">📅 15:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24461">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384d776b9f.mp4?token=nrW_ObZrjwX29wPAKyIvWFm9nYNon0YmlRCSxPFqfkgD_8MyBlgQC9uE2CehG4hTHwgaphc-AJZYXzIHLPVprJhRHCN-kHusOryq_ug5iyXzih1DeSjp5DoBi7XBxrmrJDwB3RMhkf73Aj77rSpL6GeEDIKKy-0aL327zDNvxAVR1Nrjc1OUYFaStZBor0IKh9D96lRAJrbT21LAL-ziXom5r6-YKhZAkhwsmzoVE5ms9WwtYMIM-LuaxxedCXMaeishxN8WTm29fGaCV2Lbwl1q8LSJtIS6Ecu9z6-weW9ORxsboJyXOu27-XyNLToOZX_U6oWyn-xIhuJn7d3ON1qRLrxXPhWAbou1lxS0xWWOPM75ugPeSD0mxhm2X1SynemyYcZycjp2OCkpreaMW3xYgZbk61-o30P4P9FO6mZOiH94CauFhDy_1HMxS3VZFPaxSdvRGV14J2oEap1DQJFO1WqqxS8yoBEeIB6eTso4WXqzSbeSUFQk-ooDnIL-3l3E7jU-5NmqiZGhVu-3Yja1i1bciXwWs0MH1IKJEO8lpl7T_IWoi9wYx-kWOtft5tbgjJESnDj0ZB611CYKtTSevZ7DxUOS22_PzsYB2egfjgXpDHD5s89LTjrZkaQkDQQH8v_2HAahLi0yd7eRmKGW0HTSsv7CQUuA5h37MNM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384d776b9f.mp4?token=nrW_ObZrjwX29wPAKyIvWFm9nYNon0YmlRCSxPFqfkgD_8MyBlgQC9uE2CehG4hTHwgaphc-AJZYXzIHLPVprJhRHCN-kHusOryq_ug5iyXzih1DeSjp5DoBi7XBxrmrJDwB3RMhkf73Aj77rSpL6GeEDIKKy-0aL327zDNvxAVR1Nrjc1OUYFaStZBor0IKh9D96lRAJrbT21LAL-ziXom5r6-YKhZAkhwsmzoVE5ms9WwtYMIM-LuaxxedCXMaeishxN8WTm29fGaCV2Lbwl1q8LSJtIS6Ecu9z6-weW9ORxsboJyXOu27-XyNLToOZX_U6oWyn-xIhuJn7d3ON1qRLrxXPhWAbou1lxS0xWWOPM75ugPeSD0mxhm2X1SynemyYcZycjp2OCkpreaMW3xYgZbk61-o30P4P9FO6mZOiH94CauFhDy_1HMxS3VZFPaxSdvRGV14J2oEap1DQJFO1WqqxS8yoBEeIB6eTso4WXqzSbeSUFQk-ooDnIL-3l3E7jU-5NmqiZGhVu-3Yja1i1bciXwWs0MH1IKJEO8lpl7T_IWoi9wYx-kWOtft5tbgjJESnDj0ZB611CYKtTSevZ7DxUOS22_PzsYB2egfjgXpDHD5s89LTjrZkaQkDQQH8v_2HAahLi0yd7eRmKGW0HTSsv7CQUuA5h37MNM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای دم صبی جواد خیابانی و پژمان راهبر از این صحبت های امیر قلعه نویی شروع شد که گفته خدا باماقهره. جوادخیابانی هم گفت این حرف قلعه نویی چرت و پرت بوده یعنی چه خدا با ما قهره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/24461" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24460">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346c907015.mp4?token=SA_4aGWbqzwwj7U3F2eqFoS5D1MhckgpYYu88AGGCTWSa3Wr6ysD2IVpo3JJfYS9MrFQxTuVRkEgvX5sDQRiLI-oGdLsP-8sgUPpu9z40V6Q64-_sPZS-UWGEfXBY6eMAfypE68wZc9bj2-XoZrL5t5nssW81XUF_8qhsjyMv999IJe5WY91_GChzIKv9sJrD0tR-C7DxbYxdMVgLfaAHk-P5NnhYsz3Wa5bSf61RBSVwAZNlEhRpW2fffG8hkrEIJZ8oLo3oAVThSYhRtr64eibsZJN93fpKwTs4D4Z8DKKEdiwrydOZ1kmQiC33lGF5ifFHnAkFCxJSvs3BzjnyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346c907015.mp4?token=SA_4aGWbqzwwj7U3F2eqFoS5D1MhckgpYYu88AGGCTWSa3Wr6ysD2IVpo3JJfYS9MrFQxTuVRkEgvX5sDQRiLI-oGdLsP-8sgUPpu9z40V6Q64-_sPZS-UWGEfXBY6eMAfypE68wZc9bj2-XoZrL5t5nssW81XUF_8qhsjyMv999IJe5WY91_GChzIKv9sJrD0tR-C7DxbYxdMVgLfaAHk-P5NnhYsz3Wa5bSf61RBSVwAZNlEhRpW2fffG8hkrEIJZ8oLo3oAVThSYhRtr64eibsZJN93fpKwTs4D4Z8DKKEdiwrydOZ1kmQiC33lGF5ifFHnAkFCxJSvs3BzjnyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
مسعود اوزیل هافبک‌ترک‌تبارسابق‌آلمان‌که فراتر از یک هافبک بود، مسعود درتیم‌های وردربرمن، رئال مادريد، آرسنال‌بازی‌کرد‌. اون درقهرمانی آلمان درجام جهانی 2014 هم حضور داشت، اوزیل در خاطراتش میگه وقتی که آلمان میبرد آلمانی بودم ولی وقتی‌که آلمان میباخت یک ترک مهاجر بودم، بهمین دلیل سال 2019 از تیم ملی آلمان خداحافظی کرد و در سال 2023 هم برای همیشه از فوتبال کناری گیری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/24460" target="_blank">📅 14:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24459">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVr-5_FidoL4XTdfSURIEHAXtTbSbYGj8vYv6t_GoZp_7gMwTQJXVYiPSxEZcbrq-jbhENGZIy5hf8G20fG0gPC2KcwcVDcdMMErpgeBkLvAZkIFJMRZCaC8noID7lGl4F2Bplws1M2Suq4w-WpBbrLKKQ2k2eePiAEsB4KrYIdSkMJp7mgDIk5t6WHg-3VM5yH3-0ekTfmH9o_W081bKKjVoaJR2yb6bf_hRgUnkOm8V2PpEEoSQsDoXtf0p4VvBaKEh--QUJ7Gf4jkpWB0_3GEOr6eADylQDzJaUFAYLkq7mrFFAoJOnPf7OXkl5Fp6o1p6Pr_A4G6lHqnf2833g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/24459" target="_blank">📅 14:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24458">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l41HJhKF6LnPSmcNwFJ0-rOUKYZeABfHDFoJU0PB_j7rtVEV3v0LOsO4i8QKgXh7w1UEf7iMsh0dkvRU-xxkT8roY7kNQTMtRCOji51F6qpPXjz8b2-5cjI4Q3whTGaaGnRIc0uq15nzmwTj4Feh64ALoDvwIjNMngYBL46X68FhbhanNC7A__jMMxwlFOPJJTzMaphNBv2MzTWOM1MreHMSk5j7vWLBWUfv5qAmq2j07rho0EsH29QIRpXCn3f_QvTaPSjFeiWenM9sc6v8yynv1FxrcYzzXMqUZwPhF3WUipJEx9q6hTVY1Q-1lh0yKi5Gm_pDs9iRCyQrVqZy_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برونا مندونسا مدل ترنس اعلام‌کرده که تقریباً دو سال رابطه پنهانی با یک بازیکن سابق تیم ملی برزیل داشته و اون‌هم برای رازداری 100 هزار دلار دریافت کرده که البته گفته بدلیل علاقه‌مم بوده این رازداری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/24458" target="_blank">📅 14:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24457">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/143e37e8ab.mp4?token=OA57Uhpisx01uSO72TmgsneCyVYAk-qWiXtXkBNvmlAQKyO6nbAdrJgEnOCuhgvalmIW_bNPT6AAh9vIFmsFOpFYrVMpGRMriJBpVx2FRMQ8U8MLNTDf5BG6YNbALDAUbZEPNlOBWeB5JPWOpCPqE6FeN7K3-RUFDe8VcqIhP5C_f3hunCsxTbtlOeQ3ksxSCAYeFQ_4qqhl4PUygjr_hpyUAoYl7-jZeSYu9MZYn1d2QdD8nTdHnVYEOG-A-1FskzZlhAE5CXONEmsXb_PydVEWJPdzD4pVpEJGVX3xlXEBnTqw98iL33B1O5WYbwvxX8nfY5RRp3vnTz9feggOJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/143e37e8ab.mp4?token=OA57Uhpisx01uSO72TmgsneCyVYAk-qWiXtXkBNvmlAQKyO6nbAdrJgEnOCuhgvalmIW_bNPT6AAh9vIFmsFOpFYrVMpGRMriJBpVx2FRMQ8U8MLNTDf5BG6YNbALDAUbZEPNlOBWeB5JPWOpCPqE6FeN7K3-RUFDe8VcqIhP5C_f3hunCsxTbtlOeQ3ksxSCAYeFQ_4qqhl4PUygjr_hpyUAoYl7-jZeSYu9MZYn1d2QdD8nTdHnVYEOG-A-1FskzZlhAE5CXONEmsXb_PydVEWJPdzD4pVpEJGVX3xlXEBnTqw98iL33B1O5WYbwvxX8nfY5RRp3vnTz9feggOJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/24457" target="_blank">📅 13:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24456">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVsEgcskMcZjVj4q8HerJRkiras4qcDmPj9NS5Wuxl4XtF1ntM7LskFvl7VzCoGnLm9OyPyl85igB6qjwfWfgxnSOCdIDz9d1wK7NDMVi5zZdGDq-B99lTGA3UXcBadsSbjnyMEm1xqudoLOV9UvSE4NxyNp02ZGWPqHYQ3lny7UmvWcFpSPGYZ6DlCkxK7cpY9tKbPQ-3IkJ9Z482kenuXrfK1XMRlDsM-q2ZdDij0asSKIy51v-cGtg4P7Ihf5oZnieZzKAKmWDhNbwCOSGiBZt5_Xd2xP8ouToYQwM86PSpAKJ2B31mi8VeLIiPFfcuTQw6WfaWe0W01fmzGPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/24456" target="_blank">📅 13:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24455">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUtu09Gcvr-XXvECxIY5S-qu9iT-cCQwvpzNAmeLaCyn1y5FsZJ5WXIM_EyX92xNh74cInSG8U4MhP41miiCvC54OnXLKbNim1mlJxX-Hdb97qqqmperGF7lPgZv3p5QYWhDJj7nQwUzNotz8DYdM815KAW3mAWZaq75rgu-uYgr90r8cy4Vq31XLb9uzr8JC9Hbvkv_EVJxR-Y2Ocyv3IWvSAS5k_zOjNSz1E70T5VBv9ipDmnbfe-SMixOF2TEp1JFt7JzYn8_cOGMBRthARYfSph3NNNWp4rvJcT7p9KwhQq-cVdi_RrM8sYzkDZKIf2Dff_u9m6_uYEAGMNH_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24455" target="_blank">📅 13:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24454">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qR9mMzi5qSaLMF9PdUiTmG2xTlr02eF5B7kbAd7v_XtQQDGFCtYlRd2EPz_KKSj9cC2oZZth7PnxvbVpQmq6hE5I9bifZCDPEQIbhuAxvgC5OKsVAaDQS-pPmuwjPZux_rc8NR1sxMwvLVzxteuKtCUlfLrRnRuef-l4xOM0ScSoWRx9Xvfb7P3WXjX0Eu3baH4x7nJYF_-OzogmCbCbgZ47oPmOlAJqNIOvIJ0bHaCNKBmBMudIL-LDLWALk0TjHoG4wakxxw_Ehf27x962ImXTqpmzPnZFZ-lL2kKHvnebMOOaNgElLVmRChhoDLU2e36msKycDuoLkugad64REg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24454" target="_blank">📅 12:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24453">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_GciaDBWBF8yKnGLqJ0LEDxlHCMu228rqShXe6QDcvos5CIXZEzHnIPhaVdoxk5v3DywkYpEqPXZGq_2QXWHSzBsZWdjL6u0v2Ie4EcGH1gJGOl2vYWQ0OspvGEPJvOUdt5MMLToQPGl5FGB5U3Yq0otx2sA_3cdZu95h6tRk4E7jhAJEJ3s3PRcVI8xdNDayBQwhV6Yjcbmp-Ad6bR45kpCN1t1gOd5zYh3cdwKUETqQ83t85dR1KyEgR9-uJEfwjA36u1IWMtr-sBn5TVIaqUmy1GJONHQVBf1-_sY_MJ3ViuV38_-UfILweKAiFg5psaDdvskhB-dJGXbPVfLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ ابوالفضل رزاق‌پور مدافع چپ 27 ساله فولاد خوزستان درآستانه‌جدایی از این تیم قرار گرفته است. همانطور که پیش‌تر نیز خبر دادیم رزاق پور مدنظر باشگاه پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24453" target="_blank">📅 12:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24452">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvd_VYhXptc6rOMRBFaERu_fG2iTvM7R1mFSGNDrt1ttj7yGai7mPoS62P6k2qz1swxBUPTkiCVvoSiUeE7nZe1StlK_b-JMJH0aNbLhcLm0PnDJQZDiVEYl2ToR5BZSw6dQUd9p275fTlT6w8snfz1E9a4008s0Y9j8dI9C87xdrRZRg9oboTgn5XJx8seVjFvEeqlMH93Ugsk5TeRjzf8qyq46fvWvXVA7fLXDTkXjczz9rC54maXVc0r_AVWQzmzbGR__ThNa01EDBibsHZb79H_LpQBZCLzxqqj3RP0XMqJPWyT_GVFyRU5ZpWg0-Vi7Hatr_cQYoI8hXNr8_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عذرخواهی رامین‌رضاییان ستاره استقلال از مردم ایران بعدازتوقف‌مقابل مصر: شرمندتون شدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24452" target="_blank">📅 12:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24450">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V12f2BdpS4D4FkCGuYkAIfXHRJC9WUdjZKHfM1OjuenfhIFNf72freQns5J31A53MrKpTLr8ZIMH8aUEsy6nqH8uBLLNsOPAVOPPpOuCGrRYuP2ik9622Xv6rrOMH2Ei4c2KwKAEjpCIWHN6WWVub7zAPGmChcUQZ3XzUFvTDENKFcyrPlM1BIEIxrnRXc0mbrDuhTnDIqYpCrxIJl19tKVATRLzNyxsjO1ZLsfdw5yoYGflEAeMqmuzSTayNpJZKfPfoWBFtoZS6V_jkld-x8nbRXOm_t4wKaRNZSJeiw9_bv8pgtTb8NFLSeqbT9DTepXb1s2pB-s5HeMMcrGlEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/thm8BtiyZ1Ud2gxucbnx8coPNxl9DLJlv_zKnLd7KWu-F8k0UWH1ngBm5uVf3wdWg2_eB1EEs7aAjZz7mJ8QzxDwQLFX4rpw6UrpDptLAAedmeuJdefVenTYEa1XtFze-OIUR12Ax__vM1FmclB0vd8v7DU7KlVWhYcC-T9_AJ86nWg2kXzlQRhUqRukh9HNjr9MVSTbSSye04VRnl9tMyOFGXKgrzca2kUI6fgv_GT6X3C2kRJFzKfXjN76uU2DCKgkurQ20WAdrGHES03rMNbpNWIbu-HhnYmaOevWKmiMMu7aQLyxKlyslr8VhGcenckFefHpwXmYJL351pg4gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24450" target="_blank">📅 11:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24449">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oU3E-Kdeu0E2Q-6-Kem5by-oYJkpfHjSG-LJaer3-APo-SlW49Y5Jr1mawNFKcYjsXHSMz69a-nPs78uAdQL9wQ8paLsVobxtWsgXKLCJtpLviInOEQVZ05dBnuuBta13jarnmPo9YoySDLHF052EMIXYxRgahIg2sE2XOVedzXrqKY1eghzbtxY4JBMBTdYWrNXDBQIbyfdZJE2EAlQcFyMwD8uyosyFD4GR0tFiEMvpNSgjHlFJ8MWuLv0p7KZkmEyNAeSWC809CN25y5D-EHl0UY9Ge_i3Kz3LSw566NMlsQ7B_4hH9ObSlERQX5JkcvgydPARSltdxdvVPcJCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی رسانه پرشیانا؛ با اعلام پیمان حدادی مدیرعامل باشگاه پرسپولیس اوسمار ویرا رسما از جمع سرخپوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24449" target="_blank">📅 11:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24448">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZ_5g2ixKZw4-8x-XIv7RGdxWZNLdD7lMBzIzCuVC-jv8GR4Z0nOxqK-09vzgrGVOgdVdGfLbnE0cknKEfZEXMdG2wyKtSwY7ZEAufXeSleMweQdnWMk2bpCe33dHFnBWuJ6Rq72UqkAidw0-XF3LfIujQ1cHTVv73M8K2ULQwRt0AlE5usAGtvl3D63gtyTW9yEMuZ96bSs9wIHFjBl91KjOg-pktXxVDMpEfs4l4dfE1f6POUMaUdeLsKmarDiAdVeX5Y5zvj2ahTWssB9oCiTuZ-W4laxuwNlFIqKHSQVJ8NBcLxhGmkPXbVkyodqAlcmhKO8658BqvpTf8nmLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
#تکمیلی؛یوسف مزرعه ستاره‌جوان فولاد به مدیران این تیم اعلام‌کرده که از استقلال آفر رسمی دریافت‌کرده و نمیخواد این‌فرصت‌رو از دست بده و ازباشگاه‌خواسته با فروش او به آبی‌ها موافقت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24448" target="_blank">📅 10:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24447">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=ufWXIkcxVCl242deZF-L8cQOdpg8fdueu6yhZc1FQje5XkLuq1J6upx3zZd1oO2nTNt1ParpbwV-_wKHGHqiH4OjB-O9lGCAsyn1WLuVLRhQQQ3Ae21CS6iPbyp6v-zT-1OinIBlLOzEK2kuspHfVGfsuOI7-jCNSZdltTt8j5Tqo9PW4GknfWdyOmLTqucjItuGBl27DNss-FLsU0QSkTEkja7VJw6Syg-Bg4JEIMWGcWXppv4XRNoXWJw1Y-mmMe-gGXkVo8-KGfCYDZOBzG4XndFfQWeXqG6yXN4uS8WRJ3NBRT93T_ZV-solShdosSydEVQhaIq-LF8IGoX2HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=ufWXIkcxVCl242deZF-L8cQOdpg8fdueu6yhZc1FQje5XkLuq1J6upx3zZd1oO2nTNt1ParpbwV-_wKHGHqiH4OjB-O9lGCAsyn1WLuVLRhQQQ3Ae21CS6iPbyp6v-zT-1OinIBlLOzEK2kuspHfVGfsuOI7-jCNSZdltTt8j5Tqo9PW4GknfWdyOmLTqucjItuGBl27DNss-FLsU0QSkTEkja7VJw6Syg-Bg4JEIMWGcWXppv4XRNoXWJw1Y-mmMe-gGXkVo8-KGfCYDZOBzG4XndFfQWeXqG6yXN4uS8WRJ3NBRT93T_ZV-solShdosSydEVQhaIq-LF8IGoX2HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای جوادخیابانی‌ و پژمان‌راهبر در ویژه برنامه زنده جام جهانی؛ حالا شماها دعواتون رو بکنید ما که میدونیم همش فیلمه که برنامتون بیشتر دیده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24447" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24446">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=mWVwD84Tg1iY6BHd-6PBMt0e8FJ2m5tdq8fcYlC8hZmHZi2WpQnPaY2QuYVnHm1MTs3ftTqdC-HJWkaCfbgHZC2_X7RUiGXi0unGKYSXRBXkd4qMrk9iSEPG17-1J517SZsiRbCXDEE5LJ0PB3OSO3GxESSe3eLe1UT3mZ5FGYkFbarmKfTedZNdlzaE5esmFn__3yuYh3GoscgmYabNsr4QWb7lQT74GrwRPoZCUglcx4obvG1b3ycWYrfTZ865ah6ed26ah_pqSwD4DB7eo_PArtkMzvX-t0qRDN5ylQ3k-LLp9TnVmL5EBfTHFGH26mGRBNEWD7QuHUxxN-nFQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=mWVwD84Tg1iY6BHd-6PBMt0e8FJ2m5tdq8fcYlC8hZmHZi2WpQnPaY2QuYVnHm1MTs3ftTqdC-HJWkaCfbgHZC2_X7RUiGXi0unGKYSXRBXkd4qMrk9iSEPG17-1J517SZsiRbCXDEE5LJ0PB3OSO3GxESSe3eLe1UT3mZ5FGYkFbarmKfTedZNdlzaE5esmFn__3yuYh3GoscgmYabNsr4QWb7lQT74GrwRPoZCUglcx4obvG1b3ycWYrfTZ865ah6ed26ah_pqSwD4DB7eo_PArtkMzvX-t0qRDN5ylQ3k-LLp9TnVmL5EBfTHFGH26mGRBNEWD7QuHUxxN-nFQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
رامین رضاییان بعنوان‌بهترین‌بازیکن دیدار امروز ایران - مصر انتخاب شد؛ رامین رضاییان نه‌تنها اولین فوتبالیست ایرانی‌ست که در دو جام جهانی گل زده، اولین سه‌گلهٔ ایران در تاریخ جام‌های جهانی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24446" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24445">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YViYcvOtFu9vN_-LU6-m_TTS2rHmJVkc6QBPo_-7cITD_Yf9o-KJH19q58-U5RLwIS8QW6dCL0RBTbu3HuURuOIH2c1-YGr2wuPEcUa_BkBcmT2_y9t7cscxlMBfxkwGPtcdDotguOzxIrt-oSsH-mZ3ifIn6pwcBzCYOC06Oz4rCqWSVu4z4A3PFyMfULWcQYh5CuIBvdTX6frqQ4BI8b2WPYMdXx_RHDBY65ZkNzSlRXS7UTx5BOjk43zMTZ1Av5Chk2DQh2ytxeGlrwgTEZ7TsECOsGcL2KdknKrf_9qTPoC7RgzUt4jzp7A_dlW7ywO833FjkF9FucsCvl-y-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود بسایت فیلترشکن خود را خاموش کنید
.
🌐
Link
🔜
MelBet1.net
🌐
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24445" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24444">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVVDoaQPmRqRtN06sfGihaNh7m2gFjpB5opUMKBS1v6UkUclVDj2JI9-NzjRWDuUN6vf8qHwW0fpGVJtizpZET1LnXAoIFRtxKRMpokHmMft9sfeamZ58HU-7q8zcI04HuWjy0JTcPlHhgCQGLgnA-1VN-yKxaBvr074Grn4HiJ1FQgg5E7IAvqXVlKYWosFnLXQqP1si6twxTfJgmdJlL8Ex_aro6ntogBUZc_SCymRv34fQ1J5TArGhEUZrKoW3b3C8U4BuT7X1HZLvhC1BKPd2U1hw2X41b80n3ATy3GgqM4WcqTZGU9MfMVkugXKXAQRWMxlgD2cE52Mtsd3gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24444" target="_blank">📅 10:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24443">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O46wgAR0xW0vzSvVLUdJEaAnJPEnEgku6uhFYuE9uGn79smareeFeVPKh159rboZH-bAmJNxPUPK1ZV-ixMZClrbzIojxmeQPlDFPNQ-2JuIU-uD6yfBQAb9L8qTUr3LD9fVuZVrVoqfctxv3sojVSxdotrG6AG6lJyUjfEyoNP0IYOr4wN_V5DvYjCRg4-qHjAeqWJQAOeT5MgRHBrUNkaobysT5-w6_8h9Smf9_SqgV2ThQa43N0ZI45wkhRC-iZcR3FXbOavZgwuZwh-l2TNxIamaApjRN_i_7YaGMNiuJRgAIEcsiCug0qGLexe5vOCI6ys-V3g84qkNxVPpZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ همان طور که سه روز پیش خبر دادیم؛ دراگان اسکوچیج سرمربی‌فصل آینده باشگاه پرسپولیس خواهد بود و به زودی برای انجام مراسم رونمایی به تهران‌خواهدآمد. اسکوچیچ پیش قرارداد داخلی خود را با سرخپوشان پایتخت امضا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24443" target="_blank">📅 09:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24442">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=PwT6hbzGA4ewS9g_jQqFhSuoNiBwCXcUyaZkXXUzcY06bmmlVXd0cCTo3jo_KhuzwShTZBxuJSGompUEmcCI8vHRtrjlLJkv5EegwNF-H-a1FF1Bi-CdJHDjlR_PMUaSub2Z2H4N_FKZTCwjsArbaGbsP7VNLSoZmzAF3SjvTUD23-bZR_T9qDcWmLeG07nY3ImYpGaEXbcCuEpmKaQX7w48_yvJb5XkittHQ5FHw710HDZvxY4kZnMvHBoZKQWif3uHXFgyDHnXi309gj2hHwxy_hIyQBb0EjesVZXkIK8EkU5J7Fu_X0KmcqsP20haU3UKn_o-ABn22wKNffqEdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=PwT6hbzGA4ewS9g_jQqFhSuoNiBwCXcUyaZkXXUzcY06bmmlVXd0cCTo3jo_KhuzwShTZBxuJSGompUEmcCI8vHRtrjlLJkv5EegwNF-H-a1FF1Bi-CdJHDjlR_PMUaSub2Z2H4N_FKZTCwjsArbaGbsP7VNLSoZmzAF3SjvTUD23-bZR_T9qDcWmLeG07nY3ImYpGaEXbcCuEpmKaQX7w48_yvJb5XkittHQ5FHw710HDZvxY4kZnMvHBoZKQWif3uHXFgyDHnXi309gj2hHwxy_hIyQBb0EjesVZXkIK8EkU5J7Fu_X0KmcqsP20haU3UKn_o-ABn22wKNffqEdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
امیر رولکس‌ازحرکت‌جدیدومخصوصش رونمایی کرد؛ اینبار دیگه فکر‌کنم گفت خودم که نمیفهمم چی میگم، اینام نمیفهمن ولش‌کنم بهتره، مسخرم نمیکنن. ضمن اینکه ژنرال درسه بازی‌جام‌جهانی روی نیمکت ایران شکست‌ناپذیرماند. رکوردی تاریخی برای او!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24442" target="_blank">📅 09:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24441">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24441" target="_blank">📅 09:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24440">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdd214fefc.mp4?token=lY8rGEE9L2qi_MHPjvyj0GftcUSW2uuT7e6o2s1snz5AXrDVREyxYBK9cL-O4V-FmX7I-YNEOq1-dzFXrgAc99m6PzJJeX3QuM51Gj33L_O1ge0iTbETHrDenzd-uR5feB1h_26G2y3JRFgtTQ5d4GtB0b1FiGvTgZBPeMk8JF3sXzvS04Oqw92IDQBYTP73mJ1W_I8ylaS_YLIqqQlL_5cWXgzj9M-c3GjZic0_-okPVSk2D115K-XDe7Eb98RTMsdZCkcaYKE7E2MZ6-qYyinXm0jOKM3prIF0DrqhMwmtgEO0HB2vMTpojPaBQQKw-P79MCtLSSlQgyi2yybEFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdd214fefc.mp4?token=lY8rGEE9L2qi_MHPjvyj0GftcUSW2uuT7e6o2s1snz5AXrDVREyxYBK9cL-O4V-FmX7I-YNEOq1-dzFXrgAc99m6PzJJeX3QuM51Gj33L_O1ge0iTbETHrDenzd-uR5feB1h_26G2y3JRFgtTQ5d4GtB0b1FiGvTgZBPeMk8JF3sXzvS04Oqw92IDQBYTP73mJ1W_I8ylaS_YLIqqQlL_5cWXgzj9M-c3GjZic0_-okPVSk2D115K-XDe7Eb98RTMsdZCkcaYKE7E2MZ6-qYyinXm0jOKM3prIF0DrqhMwmtgEO0HB2vMTpojPaBQQKw-P79MCtLSSlQgyi2yybEFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24440" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24439">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJ3CSipW_5EQwYSTHwdEth6X3MVlP2s_vdy6_cLXH1mKf0pB2rbzfTUyzaXkaiMYZ9LEo67edTfFSa7etk34KiolLNHEpss6dYibjKDvuwNeI3QNUA7wyf-hYvtIUQgRgAXeIoJpFN5daL2i84iFPxs5J9Cs3rjfUShHBAToU8bMPZT7UXQnsDR7vyQzCsGhZ6Zafsut5BWQE80rF7lN4IW_T9NDfM_bx9g0rzrRO9CsdOWfmD71HyNRJLxZhdGvldWCaFkZBTHbO-QgdMeivtbmBc3ckGKPbBBjkEWjfAYBJE9rWGp-Rn5aXvFh5MD9fMm8rUrJBhs793ZN0uRyQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24439" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24437">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24437" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24436">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-ceWgYAl_FH6_5utkCLCi8drLcC-3sLuiQeC6KZAAYcXavAAgt0riJet1v-QWTqFCXY5lJSeVlcy6qMcqN6PtyvkNIyuWk3DKXHTmAVPtGUSBi47sC-nYW_6mKNeW9NkKbDS8oZDH4lYJcmhRVRIornX6B_JVijvKJwXF8Hg3y745vj5MzqC6QlN08FNRNqQAQx9QhUchBh1dLyssX5yejMVvXdDGwZ4BO1FY1S0NLkwCoiRABEUVpLVVsTIQUtWTGzWQv_Pa7LJSyDurQE1wLW87H0ODuGSq1oQalEgikO_TKJjTlC_9jwYDTt4hLmZWjBInah5E2tpF6ecDSu0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول برترین تیم‌های سوم جام جهانی؛ شاگردان امیر قلعه نویی در رتبه ششم قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24436" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24435">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewyrcWge_7hvfETEIZg29KgBqMPdQ3f0rjjfFCC7ymHd-np-sN8EVRcQgp635fqJvGSMmPm_xLSJC-enweLui_B0KrgR_w8oBhJD4Ce_XK7tSqmDTV_Y4pqRRMg_GbMi1khVtEKIOz14LH_5wuHxQqOhlWGe7zn3dakpMNa_46RdWeksxLdfUsCSp62W46LPO1RJfUP8qy7TYUbrdPNTVBgIeoUsUSIEPXi9eT8oEZHxYtvK0aZzIvE_2PXMM5m0i8V7eagdDyWBblsqUZO9OXCYjIskWqvzu6rnwornQnaby3O90_uWExgoJRakNgTmctAl2tKYYDnnCUdMulBr6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته سوم جام جهانی 2026؛ مصر و بلژیک مقتدرانه راهی مرحله حذفی شدند. کار صعود ایران به مرحله بعدی به اما و اگر کشیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24435" target="_blank">📅 08:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24433">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZbNXvKSMndwdFnkJJiBqDpOLZX0fcXuogjMxaSHl547gQWkycyWfra8VLF7WAm1er62BOWC144Eiq505rQ0Bt2jrAi_RLdPfBEtdsCWQ-DWLJoH_9Kl7vnpwcCPIPP-WTw1RYAE6ok8SzrLvSZOf3-Uw9xHNBu96c64jGI2MQFbJOqPsH2YjU6CopqBrrSwH6l2e43O4UAJK_vqvSbClBl-EVJJ_2eru_RjVyUFDbcYb1dq0ushBqx2dOHy6T__BdQAgVfS6iLNOJogK61sfIq3kL3BumNpPioJrsBXt0PcUzzkSLvFV_hyVuL0K6MvhyT5hXrtUMn87lR31l0o0dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vn4vDyux5gVvwL13rfoLZPO9ZXL9X4s9v0RO65SbUj9FglX23ewFPCSR2sjjO5xOnBTi83AaefWIHu5lz3uk_LRa2IE10cBbQ__RUKmsYZNrINWL6j0Jg1xh3wQCIAMttX6uQObHrceXxST6QuWAUsQFZo4LPUdvjSbUyYvLLVtp3SAHcNVJ__Kesc5ipzxOFCGzx8yMSZKu8H_qNsokInVbHEBPzqNyeaXXkmYF4lSHOIbq8PdD1Ra0_GHSm_BJVy14GrZtol1ymrgKQuiuITOochDCJdDQtBBDxcsPqarH1S9b6TFHs-FWRhcGnvU2_TpzyGHpk7TUXMoVUXZ2Ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24433" target="_blank">📅 08:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24429">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Exgvtv8C0U25Q4G205F_sOnNUBdZzcQnfSoRUPEGCQ1KMc8dOM4_jMsYIGP5yyhotUcP1-uZapOJ_A9USjuKBPubF2pwN7qOLXdoyfL6ga9GatQNONy9AM3LcALlYLChbCqLBFS9-B6zNmuLaaPWAbvmBRTh6mr6vrGXzsn9j5xU_r2oI3pyNlywjrYewHFn_o2_NjA6Eh4CFqftaY8FkTSvsTwNhxb8bI2ciUW6rYElNF_aEmb0IIj5OcX816XF850P5obx2FeFRBB2hSOXKaFkLMyUB4uQbGV315tD4wl8he3-ZisiTsifpWHuXtf-CQ6BTB1wrH6dgawp3jTvEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛ از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24429" target="_blank">📅 05:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24428">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVjTH4lAS_MZm1ghiMkdw8DKjiWiJVXQ-RnAWYEZ3fn4D0O78WfFUhFHk4A-DEVua70gdD7La9hEhaRV8drZmHjN9U8FoU8zmg36dSL4ToAl6WmjrmSR-zoRFJbJxGUfwuR4SoHXiklBMDkrKOdknJDTJgProBS25jTpkgJV7vrTNH9ZuxZGO8qgyJiOX4LeWciYskw_fI3j_5pcBYENIwsNCGrUH2qnNDLj6rwG8u2WEfXyc7nSjYnvySAi_96KuUQsWh6vSWrdlRxQyjSru2ZqUUta-c3BZ0y5EhEhuYuimdy7xrQEfleFQyz7-x3LFrKdvkFx6dsF7Lo52dSlAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24428" target="_blank">📅 05:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24426">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-1Q6GaMmRaShQT3Z14BE8hzXJwN3dvvc9VC5hwCaxEXTQdUzJo_d0yve5DODwWOOCnZypbiYYhfEXNo8LYj2g8Fe-uk5CdU3H_jEl2OZm-K2dBFsZA-vB3wim3e5SZzxGuxkaV5PRRgsElR0JurpvnDv_wBz889_guxosrKwJF12iTHrmV_mfx3BJ0m0rv9qhu5LpcNhJbySO636V7PnDa-sBkphqZH6TMNVhrJEs1Ig-jLbrTW_JSwFghvqKBiOp8ppiGYKclk9yOujYc_ld0dwNUWFR47DxxNYbmlgWnDONYBRt4jjnakAY7Fqdu2xSazehBss7nC_8taXY0hbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WjyW20CH_9k6oYDIG4npGhj4H5m39dsPS6TEKeXtlaDg3AmNn2c_ODBI322PhayjXV_hi_8RyM5VIb1yp9rssdIcXtA_nS6KbcpB1L6ncl7lvLUkkujBfCCl-UocchSCo6TaBgzc08WOUTshD1Ndr0bGFKvc72Wz5g-M9KamWbSAgRh5DpUpAs-WHhhStPvhb1oUhwL0OktcdG7k1B-Iweht_m5roPg_F90_ebVBowDR5HrGre1WWA3pd4E4KofQmwe5Zv9KazZni9NOuMYNNCsh6WeVUZTUTwx5JNfXFd_b7RRTglMDAYPPx1JgoBP6fvBUmGiIoLsMCkL3PdBv5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇪🇬
عمر مرموش ستاره‌ تیم‌ملی مصر: ایران تیم خوبی داره بازی‌ های قبلیشون رو دیدیم اما ما اینجا هستیم که قاطعانه این‌بازیو ببریم و صدرنشین راهی مرحله بعد شویم. بنظرم بازی رو سه - هیچ میبریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24426" target="_blank">📅 05:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24425">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8RLyOLzCktzjK8oqEnNtXdjXVe1UnRd7XKc5avgnBJCZ0LcaAsX5mWxiejsHr-KXFweBgdFXum0AyMGbSjbwpgCMz1PuxZqw6SJ9Jnd3nsazPGl3XAO6ql8wA_EC8Ab5EDov15kQ5SP4_q0wdfM8CMy5Lo5QrUGmVL-jGORiE5HInZsD7Xr_Y_3_NXCExDX7O3gqSEveIRH5Qd7Pfi9BEKJPUPWp6NbG06pjWakhSA_8R-JpPqCnHSz6nFpM3Eyghb93QI_zaM6kRv_S5ei6EeGD9mzKyRY1JiD4NkUvsnG7xie4BJKKONfLgf5pnzB2k9k5ZYAvAnH0EmeMT8KVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌‌های‌رسانه‌پرشیانا
؛ ابوالفضل جلالی از دو باشگاه اماراتی الشارجه و الوحده پیشنهاد دریافت کرده و درصورتی که مدیریت باشگاه استقلال برای تمدید قرارداد اقدام نکنند لژیونر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24425" target="_blank">📅 04:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24424">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJ9-el9gZLjteZigJAGb8mF2bZl4-EN2soCz6qUZX7tCD8QlpfI95_uIN6RAckF9cBYen5COc66y8dN3u6-FwAd9KVhNZ7UzZsDEQORbzXcHlpJOSnqYbV4ctjx1IBgwRbkGL-OhjuRN4VFYSdXIy84BnecbfiMitEyVhhuE8kX1nw-lXR7G4jkAMWMlwNUH8b74X9oxq6aGzzKvPKvdr4-w7Dld0bIOV4Ho-sMYF_rB6apF_t59mpAxB2H0oBwHY-YGtUq6BC5vg-a63ve4vVP3EgTv7oeRl1ozJ5Rz18-_ypnpr5Dj0f0iZoUq6vKHKkI80UazEZPH84GcTUZZmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تورنمنت‌آسیایی؛شکست‌عجیب‌سرخپوشان مقابل جوانان چادرملو؛ فرصت‌آسیایی‌شدن‌از دست رفت. از بین چادرملو و گل‌گهر یکی راهی سطح دو میشوند.
🔴
پرسپولییس
1️⃣
-
2️⃣
چادرملو اردکان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24424" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24423">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e59cd1cdf5.mp4?token=cXvVbjkY1ex4MOP6qKcc8-DdtRB2gQviqtAxYw_Df1cwcsTirr09MqxB3BG7SP0tgNLmuaB7urhwr7yt5L8zhL_QyNj2tiP78Jykslt3-tSIKxskjNQvgOqqISaomOhDjaqLcIEbxhYciFSl07YYlutXXEm9zrhQtSFK5EJwDq6xkVEYQYITHn1DrUxl6uZOJvkd4X4ZWWG7W1Wp6Tx43Yxl8-aVgnO8tjgHkdJx5adCVhUmkP7hau6q7QUfpjvp_R7Mitq0PFd3g8KzGFdq7qnQajKg-8g_uucWQV0xEiyhKLLSTQZDlqZekna-qdlAKjUUEdlnsP1hZEEsSNrLYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e59cd1cdf5.mp4?token=cXvVbjkY1ex4MOP6qKcc8-DdtRB2gQviqtAxYw_Df1cwcsTirr09MqxB3BG7SP0tgNLmuaB7urhwr7yt5L8zhL_QyNj2tiP78Jykslt3-tSIKxskjNQvgOqqISaomOhDjaqLcIEbxhYciFSl07YYlutXXEm9zrhQtSFK5EJwDq6xkVEYQYITHn1DrUxl6uZOJvkd4X4ZWWG7W1Wp6Tx43Yxl8-aVgnO8tjgHkdJx5adCVhUmkP7hau6q7QUfpjvp_R7Mitq0PFd3g8KzGFdq7qnQajKg-8g_uucWQV0xEiyhKLLSTQZDlqZekna-qdlAKjUUEdlnsP1hZEEsSNrLYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
عارف غلامی بازیکن استقلال به این شکل جواب صحبت‌های مجری‌صداوسیما رو داد: آدم صندلی دزد از مفت بر هم مفت‌بر تره. اشاره به همون شعر شایع.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24423" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24422">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKRvqFU5Us4hoiCR6-hh83E4d03idk81CshF4PR9xuVdDGkE1UpdL-Y9-y4PVqPQn6o7lsKyJypQPJS5cwX7FY9rQYUEbaUGI5vqQUacZToZIRpwTt2QRHpIKNkizcWIyfMyAr74bdkhTj9Afcq3l5l1JmelkYsfY6Dl7KHSUZIwDTwxbxPsPx7TC1MtAD_cbv6KkcEwexYT9LT6pd_FWFxh4xudDXdzHh8giTBOTj8NHnQlnA1-aaMHhcjElh-vYAdQb7D6T5HtT6aZKtd7NXX9QG-YjMExl708n7GEjazj-2EyuWow4LD9XVcwqyxYPbYmoExlPPY6ieOJOiBrFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ایران - مصر | نبرد صعود
دو تمدن بزرگ، دو تاریخ کهن، یک میدان سرنوشت‌ساز…
این فقط یک بازی فوتبال نیست؛ جنگی برای بقا، افتخار و رسیدن به مرحله بعد است.
ایران اگر این بازی را ببرد، صعودش قطعی می‌شود؛ یعنی ۹۰ دقیقه تا یک جشن بزرگ ملی
🇮🇷
🎁
شرط رایگان ورزشی
💰
۲۶ میلیون تومان بونوس
🌍
فعالیت در ۴۹ کشور
📡
رسانه بین‌المللی
📺
پخش زنده بدون سانسور بازی داخل کانال تلگرام
📅
ششم تیر
⏰
ساعت ۶:۳۰ صبح
⚽
ایران vs مصر
صبح زود بیدار می‌شیم، چون بعضی بازی‌ها ارزش نخوابیدن دارن.
ایران برای صعود، ایران برای افتخار، ایران برای تاریخ
❤️
🇮🇷
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/24422" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24421">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUFDRTJ1UqqDiU0Jhz6A-NGGpnyoBhNdiiA7sEkKQ3kw9MXdbP_yAbxSEZVm35cIrP9V32dUoHjDqoJbDJUJGrBghf-DDLQ94v6RZtyOuyVNWmIxK_JaI_rw0dbtpJcmBE_xtIPj3B8WTTEIA_irPDv3qsGAJ7GitttQHogqweL_MBY_InEOMEWbv3Eugxn48O-hKXnnLt6eRFZgBwJ0ZN9v6PGqZw_CkEl8X0Emv0deKHS0MkJ4mwpYewEzoewoPRFVPrdB783AHjgtjm_Tg8P0cL5-qbNc-L_TDDRGJKFemkmPYz81A_3F-ebHoD3tBnLtDb2W4c-I_1h1D70wEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24421" target="_blank">📅 02:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24420">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=A69NuYIvH8jm2xM9BAOsTIg1EcJw1CcKyABqqqrIPKOURRlmWvvdGEgg-g_BeUjLLMF9r8uRXP_3-jDpZ_rIQtM8NZfg2e-MjSWGCRdajJnuz4CIQmVu9gU3yi1NzSGtN-bEtlZVekdvPBzh4L_QjX-LImVioNY7rNMRQ6C9fHP-ehIiRyeggjamNbJOSvZ7cRb23jFIWWOJxaNt3CN1vngV2omZptuBQyyR9bmNzP5LDITA2kj-pCCc-iTkHxSIT8Y2IEnpU8riFBCV20Q1zTwUjPe-6e3ITZVREo7sr8mss-Vv6xmd8uCWvQ1NDIaosedH6bBsMQE-YqSb0bpXsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=A69NuYIvH8jm2xM9BAOsTIg1EcJw1CcKyABqqqrIPKOURRlmWvvdGEgg-g_BeUjLLMF9r8uRXP_3-jDpZ_rIQtM8NZfg2e-MjSWGCRdajJnuz4CIQmVu9gU3yi1NzSGtN-bEtlZVekdvPBzh4L_QjX-LImVioNY7rNMRQ6C9fHP-ehIiRyeggjamNbJOSvZ7cRb23jFIWWOJxaNt3CN1vngV2omZptuBQyyR9bmNzP5LDITA2kj-pCCc-iTkHxSIT8Y2IEnpU8riFBCV20Q1zTwUjPe-6e3ITZVREo7sr8mss-Vv6xmd8uCWvQ1NDIaosedH6bBsMQE-YqSb0bpXsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24420" target="_blank">📅 01:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24419">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3k4AmPnqyjHnMF67TR9sLD5pZLm22MZy8qk8Qe9leXtY2piCmh3yR-OHwnb9s27NrpG9frQd7w47jRyKSD4_yfihFxzWQCudZ6MP6FoX2jGeZNvbnNW_hTTSZkr2Ho09heVU49CHA7IZTBbDJPDpYehcAmePcmU2SgjpSO6IEj138bZII1Ghbv--fbLGjzSdeCmWIw-bPmP4tcjmrHpd0FHvkCLf5doBHkfb90itUGIJIhdA-VPGMqx0DOTBRfmEG9LIZw3UnZV54fEGQ0hduqvHXyTEZyf6VPtMGrne1qRVwVU3YMxFadEiyL3CZGrYG6xW2xcxvBGcaU_D33s-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد پنج بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24419" target="_blank">📅 01:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24417">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7xTmByV3EjJK82NM-sn5xwzoq44kiP1cIQz50jYOMZwHTjKzr9cXehv7BZOB7kh_6Nju_edGY9PJvBYke_iqLUSBIaud2HQZAbQInsh2R-6Y70-MFsmUwqTKxPA-2VQi2SseJKVMWmI9PgMB9Z6daTHFYuNZu_8_A36an_tupDQ6T3ub66u8aKy-g1EQWO2CSY7DppOPXzOW5fgLD32R-I83uvU9iOiiYHhOyMKXoZEce-t2ivy4zGJOuo3ljvgqVb814i5I5OCqFyXp1D2AcV0SpDsuIy85ohfaPqxCtPGZSGtv7Z_mKScmOGfKQei4d5iR27GYxQC36v0aktqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛
از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24417" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24416">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toEFxQp-FWWtsfrINmvbfyeIfziADgtm4wccvKoVwMUl7B-ph5PVOLm5i0IoA7dJFRj-poP6raco8msEKlR_zfX5MgWol_quaYXtBQ15MMfT2DhDaoM8zub-l8n7YXuI3A4qG2sOWUUZtOre32r5D0p79xZvDKfkw1-Z-am0LBy_ySpP0VRilg_XlAciJUcgeaxBNrFZ90mlKIkcLCCnQu9R5LkZbDQenBiVgX3yoh5JYuag6lHIVJChhyeqfKrbE4OH_MuQdGR8PPr3usqDueyHGSFnbIOOfcjKNNFznyIXkKim7ZceLv_gvxEAnIQR5Ow8FAYJDldwPZ1Y-NGL1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌دیروز؛
از شکست تحقیرآمیز عراق مقابل سنگال تا برد فرانسه برابر نروژ در غیاب هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24416" target="_blank">📅 01:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24415">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmBH3Xs4KaZnaBZgRzvDO0Ag1UtVc77Z_LL0JyVrd1N_fUrU2SwTMkPjRgQABpXN6UNGTMlcRgN4i8zBRir0lB-A9zktYBU992nIt0IV_2iEkYpSLLj7x1P1jiLKcE-UTR8qxLvMJL7L-SPBHE7es9gTno-1sKM0iqSYxh8NNjIIVHHAETgbajKBGN0D6jFmSwTfGI46HJNfKo1ve7cmomerWgG3N_niFdHImhmTfCQvd6JPP56YcbJtzSSDals-I0Xp1IS57BJYKsEMCQ_CHCUAJBB99XWkT7h6-M4szH_UNEHF-EhZfKwQmmRzIoVUV5i50PLEEWXNpZVTQPBHLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هایلایتی از عملکرد فوق العاده ابراهیم بایش وینگر عراقی الریاض‌عربستان که تاسال 2026 با این باشگاه قرارداد داره اما‌باپرداخت 1.5 میلیون دلار درتابستان پیش‌رو بند فسخ قراردادش فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24415" target="_blank">📅 01:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24414">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24414" target="_blank">📅 01:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24413">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MS6n388599A6RPTuW3ogE0r5halU2-WfF9r4M74cuv70YrvEVo9wLtaLm3pstdMWJYnh9kGlnbymrJWBa9Db75Z9-Q2Q6tP5LLO7NzinPEAKjF4eb8QXpb50Mq5gjPt-j3_rXR67PUQ0H8Nf9rVfwR2UM36O7SVqyVaCWnIWD60B0QXm4yigVCtbTiso5Ht0qvVWxvqPsj9bhG7QI_h8hQhOt3YDlZZ2C6QyGnOUpsBzmxDMHRrq0rI1CXwJA77DsYZ-Rl6V2jyfKYkhMtgLGNk_A7iCD5GoUptq81NgWRYFcFrr-TJD3HKZZKT6k5LJa79ktYAcDWYp0PkoKOKwhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
علی‌تاجرنیا رئیس‌هیات‌مدیره آبی‌ها: وکلای ایتالیایی بهم قول دادند تاآخرهفته پنجره باز میشود. انشالله تو هفته آینده خبرهای خوبی خواهید شنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24413" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24412">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_nb1tynV_B_o2XoxOIv1svfy2YrliHl9IV50Vl6gvHz7oQM2bWUswWUryYuRvw0Is-UVgcIkKwg7s5Lrwr1z-bRuGLupAx60qJgnM-XLTF-Egkn-OPTog1Owp3y86OQYb68E5_i7pQ1cNaXmviuf9YKE4SvXw_QrJqADEw6atsjF4zY2SJUlJkuGZdoH0yRZVPWe_RESw2oTHMuwKqE_GMcEqzvTE7F7cvk67lgxtRG4ZfJNAhFhXOa9tmKKi0RnjD3dqhdlSBs3J_OGdEhNkYFhp3WsP2JoScoQ7bltXg0L2YocqrSRvk2eogtLVeS9nYGLjS9Kk9iq9YlcG2C-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله‌حذفی‌ رقابت‌های‌جام‌جهانی؛ داره کم‌کم جذاب‌وجذاب‌تر میشه این دوره از رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24412" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24410">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWEs0F7Ecf8uDVocN6TeOf_yvcrGpnIwO6HT3A1Z-wGOve38tu15k3t27S0xP_fl9ORgjuLeX7TScRcRiQoh5T_30UXPqhhZnZzjKl_YJio8hc5xXtBNbNt1HyGLqzw1WZnYwnk2eSkMQdLgruqNHWewyiQawXkXbLHJRzILrOn8mQjbnyd4WLB1WUvbqOMqIaUPhO44m7KHx64iTU82f-eOr8fOAuJ43VwcxcjwzUcMcwMsoqlWaAVVTeyrwu-HkQRVGrvAKgkq95LiPbPVxsslJf9mGqCn5yN4rNUi64gzRxhi35b5ZR5-pkxOt2gDePXnW5VTgIV1V7YpBGmu0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24410" target="_blank">📅 00:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24409">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDki8TYjZ_CF8GcqN5v53k-UOFGJv83OpPjbRBwWseh9Ads6U8qXM4tf13A9yEEQg0U27Dw21T2YkSmqhIc9YfUj-zP5DEt8i2zoKGgPsidyQMSoCvhmHmqg0CgneONUOvfRL_tstRNnmjfKsI8O5wTeSj74UzHVD5P6BPaq23mU0qycdQwMI2LZPHIdyYQRRAiJrYT10RINw22SY9xInkXhz04Z_0XMm2UXYkV_34mserRuxtgadZJid1u5SSwhtQ6cYqfqCHAN4PHdgFJ6ZKg7OrytYgLEQBOlagzPjJyOBtujMOCIcWhSqKQfdrZbHgo4s7SV5agpTJParllv-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد پنج بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24409" target="_blank">📅 00:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24408">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVhOfx-xMmnEy3cISQmaw9-zDq8Se2xvEIAJ4PdF9TtLI4o7zxVoJKTJ83vkefv-3aUJoHDsvPH9KAleliKZrhVxDw9shYyhQGUm2Y6rt4kHzUaq-xqhd0WC7IL-uBBi8ZrgRwmlweWE5QYxHxBrre2bw48wKOnV2PLWXBYrjgnSh_Wu7lRw493jL8dc8t4D87mMv_ff293i9b-ULysG52Y4eSzCfe_xNwpXFSUWLyMaVr04LXHnZwXCYZff9t12wmw_dz0UDdUHQvX9ZG306aFdgwZl19RsjY6LilpmWV6wxp-7ACaAIBzGb9usiI3qku2KcP2O9Lx0rMO5RJAtog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تمام مسیرهای احتمالی شاگردان امیر قلعه نویی در مرحله حذفی رقابت‌های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24408" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24407">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkeawvEBXGWYO047dMcCIZweKoH9h6qZfK0CjKqByOAM4surKvMpD31Yzbc4UYm6ceKj12Yhv2DS2oFjGs6NV2iP0uxO6BAf9DDq6w5DErXN3aAHc9uvJAbg9FL1jSMA0ZvtiEsSDU4eQdDb4a5i2P5M2NjCgveem9wN4u6p3DEo77UtZdAmI1xEknWvKc4poFl946w1FIRgRZDx2PdHuUZ_GKuN7ics3ZmW1G7Ie6SCprGT-ZySILi1hSEv34pbE-wfZcLZblY72HkQDQVwVZUN-d_7FcynIpbOhcT0N9KbF_86p07wdfusP0weQfUtx5rhi1oXO6S0ndFo3IwPJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24407" target="_blank">📅 00:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24406">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_HE2WgYc7yHtQx0hkppmH8-4nEEv_5wBhbbekBL-FkfLpU8ALXYD4zIL_vTZ4qXHkmFxjy8KT_PK5zvaf23mDbLhPT9U8nAsTFu0Pvd8YoOox-Qpk2eHtRjFymNaBwdib9_Dh_GWBDhDvI_TRETkxyBraeWPE552WfAa_-o4lgWZP4g2I3QoMg3UmX89L6OzDKJQYhR36fgvp4_PEhUlaEbcVdZ7zlQ9mQLX-_mPVSgoZi0YhQFTnEfT3jNRktzOlvwn9e9mdxj-M3kTDP4h6yBZJAXybDu3cFeDvhx-kGocczv_cl1Qm3mMb3tvSLMJfCS-p1zV5PH-wEQwEXU5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ این‌استوری‌جدید اوسمار ویرا مربوط به آخرین بازی اوروی نیمکت باشگاه پرسپولیسه. اوسمار به حدادی اعلام کرده با دریافت رقم توافق شده 900 هزاردلار فسخ خواهدکرد. ضمن‌اینکه نماینده اوسمار با باشگاه تراکتور مذاکرات مفصلی داشته…</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24406" target="_blank">📅 23:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24405">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec8965f3fd.mp4?token=FizWt7RRCxzCV2JkxoTZQJZjCJQ4uigiw6mXqImDh6hESowIDXDTWZr7LDzQq8H97mXGglwVG_bzOWa8QLIUNS2ohftnEq2KVepbqEgB28uKRGxVQCSabOhoDYkaDvP0nx2fXfIHE76meSlkqQny0-kU6eF0pBrux6Elw_aURFiyZVVaWfVYP6g8OJBa0yKknVZotewraR66mxTmQc5u6g3cWiW5cn-gw3t0d0ALaWqnWS-_KOzN6L8wQa5vIM8LNZ4ScBI-UZoo0KCWbB6142a97u-NbvGab1zvlfy4Eb_VXrNsKd8U6BBAgJdOtUpAuO8sxy3dmf9QHkU1Y08l_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec8965f3fd.mp4?token=FizWt7RRCxzCV2JkxoTZQJZjCJQ4uigiw6mXqImDh6hESowIDXDTWZr7LDzQq8H97mXGglwVG_bzOWa8QLIUNS2ohftnEq2KVepbqEgB28uKRGxVQCSabOhoDYkaDvP0nx2fXfIHE76meSlkqQny0-kU6eF0pBrux6Elw_aURFiyZVVaWfVYP6g8OJBa0yKknVZotewraR66mxTmQc5u6g3cWiW5cn-gw3t0d0ALaWqnWS-_KOzN6L8wQa5vIM8LNZ4ScBI-UZoo0KCWbB6142a97u-NbvGab1zvlfy4Eb_VXrNsKd8U6BBAgJdOtUpAuO8sxy3dmf9QHkU1Y08l_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تورنمنت‌آسیایی؛شکست‌عجیب‌سرخپوشان مقابل جوانان چادرملو؛ فرصت‌آسیایی‌شدن‌از دست رفت. از بین چادرملو و گل‌گهر یکی راهی سطح دو میشوند.
🔴
پرسپولییس
1️⃣
-
2️⃣
چادرملو اردکان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24405" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24404">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbVuZutNqFdgwO3dWP6u1h87cjnrOskGrtHwRQGFLzSn3RCMEDZMExzu0DpJGn7JjzjYSoZy2QWRRAaclrCD2MToadSLOsH3YHv34aGIHLeNo2RU6eL_a2ihW6TtMMJbVPzW6ZP5wO_dFqB4G-rOZoGhk8EdEplwxMlNwcVIUP0xvRV9dC3Fwp65mq_7dq6tP_ugKL7TJo4tFBYGQVixGi10kwuVAMJ9T6W8qP7C66D18cmltu4FHjCvz_7hne3dFhb86hVvqtt1ExTsMtwJeISwqY_OFeawuWRmrTpCCUeHUqoE461JCp9IX6pedJZZsb1oMXKS8KKbZUWhH0_5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گل اول چادرملو به پرسپولیس توسط سیروس صادقیان در دقیقه 57؛ بازی حالا یک بر یک شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24404" target="_blank">📅 23:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24403">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c65cc2b59.mp4?token=I8nXXTzU0TNEkcdmMDK0JBCTKqKlVF4v1tSkTDKZwu8Z0dmmYyZHr4M2fkEdeBQAa-6MBs8YoNmlPEOsd33vTm1kNdW5nZHLp_aZHFl14mquPRUrlUyyT0wI5kY1xZFNm4zzYLJl3Wz0wjUnsFZJGVQACRjyc4_xvanhDgESztW05rq6HzY96he18OKezKjaq5D-rbDT3h6tNww4FQC88LXfyHjDkGmarpiaMPxqQTa5pYrwgZLe3y8FHDAcM9iRxzkkuW-22c9Kx1JlnutuPjpyguRiKMqRKvn_IBzgQ6F75fy_-Lm6e5O-dzG4nm8elk1dc-rcfMuQn_FSv3Vp6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c65cc2b59.mp4?token=I8nXXTzU0TNEkcdmMDK0JBCTKqKlVF4v1tSkTDKZwu8Z0dmmYyZHr4M2fkEdeBQAa-6MBs8YoNmlPEOsd33vTm1kNdW5nZHLp_aZHFl14mquPRUrlUyyT0wI5kY1xZFNm4zzYLJl3Wz0wjUnsFZJGVQACRjyc4_xvanhDgESztW05rq6HzY96he18OKezKjaq5D-rbDT3h6tNww4FQC88LXfyHjDkGmarpiaMPxqQTa5pYrwgZLe3y8FHDAcM9iRxzkkuW-22c9Kx1JlnutuPjpyguRiKMqRKvn_IBzgQ6F75fy_-Lm6e5O-dzG4nm8elk1dc-rcfMuQn_FSv3Vp6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌جهانی ۲۰۲۶ رسماًبه‌پُر‌تماشاگرترین‌دوره تاریخ جام جهانی تبدیل‌شد. مجموع‌تماشاگران بازی‌های جام جهانی‌فقط در ۱۵ روز از ۳.۶ میلیون نفر عبور کرد. این عدد رکورد قبلی مربوط به جام جهانی ۱۹۹۴ آمریکا حدود ۳.۵ میلیون نفر رو شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24403" target="_blank">📅 22:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24402">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abdda890a5.mp4?token=mt3epmG4WG9gHLYUcmIsV3wQ8bYaCTHOwycxsTpcS-vFXn1MgiuL49CCKSzuF5zUjKwr0p0bxZharYuirU7shzoq08owkZ9h6oREEJJ2vOKABQ6xzGkhtqyYA9BHECZsl3WDQv_oAFeSlYGv00AogsGFlSJdWtuXcEEJPZOjOi1_g9bqRDhj3Phx5z1F1f7NdJtc8NOeUNp6MDruSvYXLurMAScSHunKuyMRZtro_uA--C3pRlIg2FPCgDiOiAR7bFOdAjRrR-NgHtKZGbYisfDQC3-QLhuUrF3Vwhj63YFx2igVdm8R_ovK5fcs7-9fcwnDVVfQMys1J0sZQeEGHW-SJwjZtY7ECOlfoLYvltdrakU4P8rF6Cq6SIYng3OPXVowrHpIA8th678LVLY9xLssb-Mh5l2S-jui85AtxBPYayHIGSQc8TM-DuWU0RysN0IdEAYtpmjUgMlS46jCEY0WPS73DHS2WsznnFd-RnwrxdqDgOlgfEIBYI_KL4glhERs2nxfNnFLWLuGB9WNaFyDLvWzfxlTqqXkHuKi3D6EoW9LF7N_HNvRhorwh1UHeUMbPe4U0l6H3xqmGbhh73CMsAXaJTd9cbFG8Jk_FZFANF91GRC_mYbsFI5Kgu92KxVfZm161wc6Uzf2zHX3jEMs959sKqnd3TWGsO3r1_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abdda890a5.mp4?token=mt3epmG4WG9gHLYUcmIsV3wQ8bYaCTHOwycxsTpcS-vFXn1MgiuL49CCKSzuF5zUjKwr0p0bxZharYuirU7shzoq08owkZ9h6oREEJJ2vOKABQ6xzGkhtqyYA9BHECZsl3WDQv_oAFeSlYGv00AogsGFlSJdWtuXcEEJPZOjOi1_g9bqRDhj3Phx5z1F1f7NdJtc8NOeUNp6MDruSvYXLurMAScSHunKuyMRZtro_uA--C3pRlIg2FPCgDiOiAR7bFOdAjRrR-NgHtKZGbYisfDQC3-QLhuUrF3Vwhj63YFx2igVdm8R_ovK5fcs7-9fcwnDVVfQMys1J0sZQeEGHW-SJwjZtY7ECOlfoLYvltdrakU4P8rF6Cq6SIYng3OPXVowrHpIA8th678LVLY9xLssb-Mh5l2S-jui85AtxBPYayHIGSQc8TM-DuWU0RysN0IdEAYtpmjUgMlS46jCEY0WPS73DHS2WsznnFd-RnwrxdqDgOlgfEIBYI_KL4glhERs2nxfNnFLWLuGB9WNaFyDLvWzfxlTqqXkHuKi3D6EoW9LF7N_HNvRhorwh1UHeUMbPe4U0l6H3xqmGbhh73CMsAXaJTd9cbFG8Jk_FZFANF91GRC_mYbsFI5Kgu92KxVfZm161wc6Uzf2zHX3jEMs959sKqnd3TWGsO3r1_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
#نقل‌وانتقالات|رسانه‌‌های عربستانی: عبدالرزاق حمدالله مهاجم کهنه‌کار مراکشی قصد داره در ژانویه قراردادش رو باالشباب‌فسخ‌کنه و از این تیم جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24402" target="_blank">📅 22:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24399">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28a6fd59e1.mp4?token=u5YF3WzkHep1ri_5CKatGB6VEKndBXQ78BqjT7hxc53CNDbW99KfpwPnYWm_xK9S9czI2qsGWu9tMOCxK9JZxaDVl6T1KaIUfRuPsAZtwkPXoF-Fz0w4tYUmsEsrOrzr6kMIHCYI2iuDnDZp-aYXiVR2_oPdIVjISBXRTntkI9lrPNvIWEWYIA71Cp6alq59iN4PkPEaTkk0JCYZyrFOt9khiaqyybAAw6oKdfCdZhrrAUYOSIDDeuoMPErUbJYpJEZ-FB2FtZJFeFhCgNGBAntJwnetmL6uf61TPwVzPppCWQhND2EJHLyF2zVjv3yK0D88TnqaVwXNw2xZ9jtz4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28a6fd59e1.mp4?token=u5YF3WzkHep1ri_5CKatGB6VEKndBXQ78BqjT7hxc53CNDbW99KfpwPnYWm_xK9S9czI2qsGWu9tMOCxK9JZxaDVl6T1KaIUfRuPsAZtwkPXoF-Fz0w4tYUmsEsrOrzr6kMIHCYI2iuDnDZp-aYXiVR2_oPdIVjISBXRTntkI9lrPNvIWEWYIA71Cp6alq59iN4PkPEaTkk0JCYZyrFOt9khiaqyybAAw6oKdfCdZhrrAUYOSIDDeuoMPErUbJYpJEZ-FB2FtZJFeFhCgNGBAntJwnetmL6uf61TPwVzPppCWQhND2EJHLyF2zVjv3yK0D88TnqaVwXNw2xZ9jtz4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به چادرملو اردکان توسط محمدامین‌کاظمیان دردقیقه 49 در تورنمنت آسیایی! این گل توسط داور بازی رد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24399" target="_blank">📅 21:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24398">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3569629639.mp4?token=BjmM7RjcIfE_ygQGUxyYkhWBMaa9janRGBtkF4YCq_gTQpEdHU05NUHonulnmMoMFWwYI5-Zh8TRT9FO7sjYQdAvEhoJq8686M5Ls4sYCZ1UtuohqtkldTqV1tq4XmnnKB9F77rW9xMvvMLP8gK-agRmRmhUukLOg2ddtKbjQIpdfId7dIgKj-q16tfUIK-zkHLLljCCcWpZuXjKHggZ8QgxEAJdjoT4mh5UQQTjOYF8TLFIZqTggaawJ1PHJhyAYdzuw96_1L-klO3t3leG1iS45C7q8tcUMRJb-koPO21RKJ9TEjbZ6uGJLrPwU6Insru4hpZVPwcvLPRCb-LwvVMt2l7SVZsItkRcErCIxB4lF2ji5TwdfVxHe70YxyYICNT5j668DEix4p5hOdMaNW2QxX6ugh-ll-QQUD5JsmHOOb2OBRKFIsZLOWzkpU4GW3Fscq2eFHvv9bpSW91jsmSg8fSi4dyE04wJ9tL_SFfCRhLabEqt6oHfWfSp2PwuxYsovis_kAdHEGKe85OiM3Z2uKRMndaKqAD-vhKAQosO7FcmB8vzaEMTdcJGe0mZctCo-j19nZ9LATtXqkDGpCfyasd2RJLGt-SrXmpJO2KbzQU8RtxDFJVBwt1QYnurVaSO5fu3esBXciqlzkg4ZICV_D0-fk0lEMYuL4lErFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3569629639.mp4?token=BjmM7RjcIfE_ygQGUxyYkhWBMaa9janRGBtkF4YCq_gTQpEdHU05NUHonulnmMoMFWwYI5-Zh8TRT9FO7sjYQdAvEhoJq8686M5Ls4sYCZ1UtuohqtkldTqV1tq4XmnnKB9F77rW9xMvvMLP8gK-agRmRmhUukLOg2ddtKbjQIpdfId7dIgKj-q16tfUIK-zkHLLljCCcWpZuXjKHggZ8QgxEAJdjoT4mh5UQQTjOYF8TLFIZqTggaawJ1PHJhyAYdzuw96_1L-klO3t3leG1iS45C7q8tcUMRJb-koPO21RKJ9TEjbZ6uGJLrPwU6Insru4hpZVPwcvLPRCb-LwvVMt2l7SVZsItkRcErCIxB4lF2ji5TwdfVxHe70YxyYICNT5j668DEix4p5hOdMaNW2QxX6ugh-ll-QQUD5JsmHOOb2OBRKFIsZLOWzkpU4GW3Fscq2eFHvv9bpSW91jsmSg8fSi4dyE04wJ9tL_SFfCRhLabEqt6oHfWfSp2PwuxYsovis_kAdHEGKe85OiM3Z2uKRMndaKqAD-vhKAQosO7FcmB8vzaEMTdcJGe0mZctCo-j19nZ9LATtXqkDGpCfyasd2RJLGt-SrXmpJO2KbzQU8RtxDFJVBwt1QYnurVaSO5fu3esBXciqlzkg4ZICV_D0-fk0lEMYuL4lErFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به چادرملو اردکان توسط محمدامین‌کاظمیان دردقیقه 49 در تورنمنت آسیایی! این گل توسط داور بازی رد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24398" target="_blank">📅 21:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24397">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o76LEf-dK-UlgmQofD_jeFIxFptqCijfpisJ-41MujeXycyHBra8ALS_y0HoSCfa1yFKtmU73lvXrwSTzGpcSLJrCupTc_PuyQ4Ucsa5ZB8ggEZBrhosu9Pvq9QEezWuNrnrIbebJAiyDI04st_58cgJ8fFJYVAVcvqEJ8JPWDPUd2jasrdIpeq39eny58glRanf-snAgXr8VBUIb3PazWL2by_fBQXBjRveXmPynmBSPOCD4qqoUGEJmsAtY01JTJqr2z3FoKwa6WDJxMi6AiL9MC_GXtFK5lvIq3dU4902nbz4_uMUQyvtv7cJPnn3Wc34fPyd5bGvPtz05jMcUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی والیبال ایران با ژاپن؛ ساعت 18:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24397" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24396">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=INTVj773AK2iCdR_BSu99-88F1Vs1UCd2SOEIu6fjCdLtXWbYvZMOvPf_oCS2eFvhAbUZ_J90jVYkjJ6gtcDhapa28heqLUroqDvRp5uYWngMgIUrmDd8sQmHzeSsVakuPfwPJmgiN-hLzSZKh2IjlQhllUgd44SSY05VFbey4o6OuLflL-4f0kCi-i__qktjvU0yKLzjrJtn7BFnNjrwXVvUzAzrMnuSLiBk7cqdC7IcsIEm6-knV1ISYXpSD60nyLcdwn87nQrBp7FXtNEFTn6s3qGCRnVMEu-SkYmU6qPRlkjfr8-EChcUMggkxEovmTkgVVNy8PgU8O9edYdPBH8dSHmO3CLGYbnKBlfRdJYhyGbXy_jDL27JDm1GYcKwXm4XWKV86Id233QLPeQ-4uMXoRv6yzaKJSysQ3mC-cYaD0H4a3OHUjWJkr3Nwb5EbXhpiTkmY8ztxd7hqEqtGUlHE6Bdv0HFd_w20XQcSqMYvvSEC6whnpFON3EcvogD9_t3Js2lep5jsV1uOgVWnxFeEZwg4AJMbsDOiWT2Qp7XIFFacKWx4vLJG4h-ru5Vu51oxxkJm4ig0YDWkV_kHgR1FaFrpTtYnXnzuHTQd4IMAbSW68O8FTxjXR33ZCCkFCkIxYAHPqIq7AukNfbEbIg3Li0KkiAnKVGGGXYqLs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=INTVj773AK2iCdR_BSu99-88F1Vs1UCd2SOEIu6fjCdLtXWbYvZMOvPf_oCS2eFvhAbUZ_J90jVYkjJ6gtcDhapa28heqLUroqDvRp5uYWngMgIUrmDd8sQmHzeSsVakuPfwPJmgiN-hLzSZKh2IjlQhllUgd44SSY05VFbey4o6OuLflL-4f0kCi-i__qktjvU0yKLzjrJtn7BFnNjrwXVvUzAzrMnuSLiBk7cqdC7IcsIEm6-knV1ISYXpSD60nyLcdwn87nQrBp7FXtNEFTn6s3qGCRnVMEu-SkYmU6qPRlkjfr8-EChcUMggkxEovmTkgVVNy8PgU8O9edYdPBH8dSHmO3CLGYbnKBlfRdJYhyGbXy_jDL27JDm1GYcKwXm4XWKV86Id233QLPeQ-4uMXoRv6yzaKJSysQ3mC-cYaD0H4a3OHUjWJkr3Nwb5EbXhpiTkmY8ztxd7hqEqtGUlHE6Bdv0HFd_w20XQcSqMYvvSEC6whnpFON3EcvogD9_t3Js2lep5jsV1uOgVWnxFeEZwg4AJMbsDOiWT2Qp7XIFFacKWx4vLJG4h-ru5Vu51oxxkJm4ig0YDWkV_kHgR1FaFrpTtYnXnzuHTQd4IMAbSW68O8FTxjXR33ZCCkFCkIxYAHPqIq7AukNfbEbIg3Li0KkiAnKVGGGXYqLs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل‌اول‌پرسپولیس به چادرملو توسط کاظمیان در دقیقه 28 در تورنمنت سه جانیه سطح دو آسیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24396" target="_blank">📅 21:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24395">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjHrxJ3_80i2oqLeNq7YmtiL8-qMy2Ky1QVE8TwmVLQ1GL0xSFU0Swhe8b40E_EfNi5bAuibwMek0aHtRCDbQlVQDtAlmU0-f3Kce5olCezPxf_WjFYhaesR8_2ycKFAhQanK45_Q-tvMZTSD6pC7Vq7xWwpMKy3utDgOpxZU_ynvRBSyNO18mvYfYOVOmlQYnAwdKd3PISekRPZoDmPrzPRysOPKe-IJMKmITVkpLoWSN8KKs0SZbfoQiGKs2p66-IX05dbzAtVwRUiUPkht9h8bvbiUdbIMjnYyP3t7Qv-VflN8c7snXFpajdx349iuN8U6ym-m0OdlbELww9XiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#نقل‌وانتقالات
|باشگاه آث‌میلان با پرداخت 50 میلیون‌یورو به‌PSGگونزالو راموس مهاجم 25 ساله این تیم رو به خدمت گرفت. قرارداد ستاره پرتغالی باروسونری تا سال 2031 اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24395" target="_blank">📅 20:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24394">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8XS-Unuq8838IbNzZWaKXNzqe2gwGNsfcP4Nz4C1SWJdYse6HvWrY_fPd2KIECpiKRr28yvFbe_A_-P9z8VTi6g0qOewuw0PkRR7_zz1j53Asb8ILCUQuxyiRS3T-rykuLvm15I9zehAijnrzPe62WRjzNqhHX9L3sz6mBP2sdpLsslbL78YvlGhiF_YtJ5fleeGf-fhNlProxuMTDu_f_-aP65l8eqXl8m2vA2oe076CZaJg4cUxI6Xc3Yb76LEZGqbHiXd30E85PksR5kAlA2QGXtEpcLHnIcR7jr380axKm4yCi89MnGywzNBgVEpNJ7EtRAX4PW6V_P-HnXZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24394" target="_blank">📅 20:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24392">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pipcfbEONtMtojyudBVTNtKEwtN4PqjJcJf5K5qPbS5_xQ6iqbGwzc3vT5zGUS-6gn2AWUQiG47UEKsepdB5emvhPUKP49JDut9B80mVRegd0WliouSZg8nsWEU3uurMrace_i81e3Y5EYeypZ8mGJ8IsKxq-TRFZa1cqMsW_ko6udAqNiVRgOrNOwPKA5VZ-CBSfJqrwTQOLrc_XbJw6DF-Dk8JWiRtZAxeDoJTLzhd_oCJ_lQLPrJ4HYouI3cYJUGUWkSFaJjOWIHT_AtGKpzM-ZTKYfRl_0T76kBGfxTMT-Ob550W0yvl9MroX8IS-xyF6GAs8DR02bpo0-i75w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SsCv6CwE7moZwYBJdLZyvcz6A3pOriTjn53aH4i0Yqv0GeeP3dQ14NEekCzzFEpI_gIWG1tNI84kx8fIOa_kUY_ue5j6-It6pNpepT19Y3kw10QJzOEs11mF7FiKr4HytLl9Cydn53JDfWyH8iU3DOjl4pF0PD3VKmoKm4rTfvck2VwY51TL6eup2o79MhOn98QXfUtecNO3gQUxgqUm1QwFcJ9WszMxRGkgezuIDTc1822XqmXENdi_pEDifiwdi0kuHsCEBwXhBeGi0mj_D4eGnclX3ugzmwbImlktG2oFr9KWAOo0Xs8Km7Yq7_7Vg8dsxb4z99B_ctqti_4owg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ناتالیا شادل مدل استرالیایی دوس‌دختر کنان ییلدیز بازیکن یوونتوس. این دو حدود سال ۲۰۲۵ با هم آشنا شدن و رابطه‌شون رو خیلی خصوصی و دور از رسانه نگه داشتند. ناتالیا مدل قدبلند با حدود ۱۸۲ سانتی‌متر هستش و قبلاً شایعه‌هایی درباره رابطه‌هاش با زنان وجود داشته‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24392" target="_blank">📅 20:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24391">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gfcm-FZHw6GgSFVv5nOuclLwTWh-WBwousbv04zLCYtkFScvfsW_9r_IiumkDetxMyHc3EmHp8Z3V4eUiLVuvrWHbBgYZkVmcjH0WGpuq-XYm0BLadFL5zuyikFrlGyOTtSP0zwWuKyFOYpCbW2jeG2wTs-TLMmWLd3zkJzOP3FGDhJxcS4lASTbKhkJ__meFu0bUK1ZbGDlQfRsCNUwDRIPeKN3dRgys_L4oMvYiBaprdcrfhl4dyyG9yjk55pdgWODNujzMdnYJO-zD5deOnrGAfOyVl8188dWBZ5svLcuHIg9uwKOBJdRTfNS8l7QhDPU8IFr5rnngD3Xqf0Eww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تورنمتت آسیایی؛ لیست بازیکنان کامل دو تیم چادر ملو اردکان
🆚
پرسپولیس برای دیدار امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24391" target="_blank">📅 19:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24390">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwvzCjc68wbgm3UJZXJHuj6LwqeCUp4z-TcYxU6bwS32wjMgN-TIZOxOh8bYq-kNKYoIjOKF4lloEv17pdrDTnKag29rEotun2cxU75mww2MiLDOjTR8_8uBRkVjmejtYn8UvspAHdMt7zJ78hV0j1Rqm8L4WqCH4CTxTs4hODPHubvJgUD5nvuf_BU9LNShJ4FMq0xjNQVa0YqZlc8dA1WgMz3rUm2Zvq-cwQgX7bda5zatT36tu-gIRz2Nfq_XMI9omaYiPb3XsZa_E5ZgPs7mceFSQ__rqH1FZSwR39bDPTDVTVnKqU-TJY6HYOvAAN9Tdhlz7auRELdHk5ElHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تورنمتت آسیایی؛ لیست بازیکنان کامل دو تیم چادر ملو اردکان
🆚
پرسپولیس برای دیدار امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24390" target="_blank">📅 19:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24389">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjKNFj0zQtGM3-5dcoKPDU9xu6ENKl51OJqAtke3ZtjWmm8XMwM2QhiQMBLS7zwkqk2mXl1VHRHxXvtTreyPbch__rdwzTkZ_0VjKu8bRA3WDYVdj0UXvnjEPWDHPNdVaPiZeieF7BYeuXO8GlobJvDCRg3ZP1QXrK2x1M9D93cOWJ5xRoHUhDgchtWP3wf_5ypT7L6vR3rU35GrhYBATUwTtLXjfh0Ny2v31R8AA_mXLPcm5xrmZxRmyHGKHF4I7Znx9FEgATtavZJBpvXMi4hKIZv8nUK4IkhiIC8_HdOmyubYIULna29AVPzlVFoPgCsbT6s-eqvukLTc0O-tuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب‌احتمالی‌پرسپولیس برای دیدار امروز برابر چادرملو اردکان در تورنمنت سهمیه آسیایی؛ 18:45
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24389" target="_blank">📅 19:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24388">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fI-n1ptXbN8PtVlUIKpbrhCyElQY9XDRcYhAXt3ZA8G-2zKgMh-k7ZygwASvGDvGr1yTgU1Gh-zEnKVei2IZz4OZSG5Sko3sKKhQEM0gg3pKkQIcon1toSXahO-I0OqOipYUQQExKIFMiEwH27cgSXE04P7bE5LdQYEWQCUGIuOotBuWHrZKD2T7mxX0ZX4s5LtbIRFyMxF3HEvvV4pIesJnG-iC1CJ529NGhfv6OgguquJC735FTvBB_MncLSr0erZtzTCylJP2T76gXuG3VR5itSrJcTjBuZN5ih8FX9C1eQpGspqfNmz0_Bg93Xtc7F5XQer_h3k5yReaQ3AbrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌اخباردریافتی‌پرشیانا؛علی تاجرنیا رئیس هیات‌مدیره‌تیم‌ استقلال صحبت‌هایی با مهدی هاشمی نسب پیشکسوت آبی‌ها انجام داده تا درصورت توافق بین دو طرف؛ هاشمی نسب بعنوان یکی از دستیاران سهراب بختیاری زاده به جمع آبی پوشان برگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24388" target="_blank">📅 19:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24387">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZX3JmNN_NI-POpCgf-bnZD2meNN3udXIXUrr6yhJgt05rzcnBqXMPp2G2QwItqXea8xpP5t4bPwx1hRb_ZNXYffs6Nw4fHFLIqjWQBO7DCR7ZOTZ5mjXBVzhEhsN-cmU9HmUzqmHPScNdTkzYEM51CxQ0dGpFvYOODxHPp7xDLv9mHHzBkguxuvqvModlUqbV0RjgBWqbZMHYQDxGsSpNXYjM8lKEewLceJY8H4bhCR7uz_3WXFykb0_gUoBNT1xuGlkqpNrEI-JpHh5YlDXyg_frHmCCyYLPeRxCizTX6h97N16HqxTfedxZavTj26d8W_N3G1Fs-yzh9VPbbhCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24387" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24386">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFMDlEAU8jXr6OYN_WaMzj69oVQxGkU3gLVhjU6WFFogDZLaBsgoqkoNknMPuFDycrm91JfTvRCexXNuxelZilHvq676KCRtChBwWPnQn7iMT5Z-q2NyGFR50CAUmLU8N8ZppEsh8leM75HNtt_D89L2TG-OUZC_-rxVJauuX5dvhDQn0ej5148DjyH1xD8iBvuyoiZTYWbbhmIpBSZD8VbhBwnBhDZRQ6_4wg4rYTS9FbKnn5q6mxM-m31ZflVv0hPuI5gIniGs4Ids_EGS-Ylf2GfpASchPhbwpKV3RgOoqkplORvlOftgLmX49VrZbK89sGSOTK5AXSG4Riv9Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24386" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24384">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrBzTNmZ3P06FncA6dwl4cxMtb6HgKYwApCoMa0SBPvrVH-HrqkBwkrU2AcXgKI7W6kN7aUkitOxCg_0LhqvL_xQfyLBEuHPn2AtbDgyX1ju6d838ZjRkZSFXFerDH454BLwEAhBSy4HCpIC1COOHAlv9pwi5RYASJ3n4KedI8Fjm6NxwlGhJATOp47mc1KhCUzFEhAf_AIP37-H-UD_-4p2Vu-XM9t9l-V6L9ExWAhHDaqaINbu6CQC_DSzpZgcISPbjCbS8n_aq-zLbGJ4ZLX3kAtek0rH0Hb97L_aKETrapZ9VyC-91Yswda4h9Mc703xHwA7xtDA1XPA6agkTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آخرین وضعیت تیم‌های صعود کننده و حذف‌ شده جام جهانی ۲۰۲۶
؛ تعدادی از تیم‌ها صعود خود بمرحله یک‌سی‌ودوم‌نهایی‌را قطعی کرده‌اند و برخی دیگر از گردونه رقابت‌ها کنار رفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24384" target="_blank">📅 18:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24383">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hoi8LfXT3j4dB5TlFGwEu9OgCk5zI796R4ozMEecSLJsQ6ERdtBZxh2Haq0Vo2k7EhBvjUVKfUUs3r_U47yTQLKc0aHSUuXD2Z1xFzrNv7dzbOhiVpvxXIDGg_Y81kxuSviKLKUd_bsbxYM2h0cHKtERJaKl3YvyliTuVKm1UbreJb7i1HXl3X1b36QJAoJqrewJxwSc627khIVaCEkXFajT8HoqrAgTkvwpmrhPo5d2KAPAnQ4dz7gH37c3uc0K5YOnfdvdPmSo3XXh-JpnVsv69BPVs1qgCNH4anGoIP5015FJjPV1KPJD_jQuUgip3jQWC_pKnRv0izyHMM0ZtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛
ترکیب تیم ملی والیبال ایران با ژاپن؛ ساعت 18:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24383" target="_blank">📅 18:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24382">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v74vj5vGtm9viIMZVmEMtGo3X-MeTwSO-VHn9exJ0z2wO5eX6XnlAilKx845CMa3ScCaB-io2EoPMVQ586Jq4DXfGOD-hlZhcAHuWeK6lO9WIv5D8XR-gnLUwnmXDYAxwc0KK5WwXKpndFytylwGQ3xzPcW96U2gKw4f-cpRyaIjF3yK-y46NwGb3bicEPKr4p_mugt7h1zaSipLIY_1agV8THdDJgRMt_rEDbOXmPMvsdqiHJ_rJyRzQ1NtaGcVeK7SZ8qbZrAV4P_nA4Z7Rl1O63fRh0qyxad24Qkk1nqyTHV0d4KMZaJRsghB7p8qF5L33mIo9BgSWU6x6TIZtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24382" target="_blank">📅 17:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24381">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjDFnov-R3nLY3klYwKsHU7o4iAr1bgJMd5Y4vcQacHUhkqWTNN-2D0jipRuWptv5HhW70oVvBzOfkAM168kc5kM3jM4CNVJpyBPC0QdUibsDCgbmTCfNcF6vkUXqsyPokrXgEJsT-hGl6WUE9-tUgzf1mVyVab0Tq7E9h3Xe-CUy5NTwdIWz6grRTHq_9_5h6poDRDeRv0Au5XcKn0o-5WuhHNxulRF4vayG189YViuknQxBeLEV8xlBGFdUmoo4gW4wzvDg61AaX9AQmB4doKE2Y8g8Iw6Q04J7y9_4lcdAFm6FUuqPmkSuGmMV58PSr4aP_f50FNsnmsPZK2Ivg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرچم‌حمایت‌ازهمجنسگراهابین‌پرچم‌ایران و مصر قرارگرفت؛ فرداصب قراره ورزشگاه رو از پر از پرچم های رنگین‌کمانی ببینیم. فیفا گفته هرکی از قوانین ما پیروی نکنه بین 250 تا یک میلیون دلار جریمه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24381" target="_blank">📅 17:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24380">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8IBiPUch7FTbEGqQ1hpzUzOntN_E0VE5AWHGj6BV-YI-aiztcCbPXcAYsa8-Lx1U2wCvwDo-WONxpudmHIcFBxcJJ9QQys3qRfL6q72sEHDVLolgfn9hCsn0MhrhAAQYE6NQIVH9iNVkslOAsuGE3Dvq1w9FUXCdqetEj_Hk09eYyYg8pmWr21Ff-OyPjo-XHyCnu_jp2oLCjgmGZMLzRjR9wRlP-yKvnBw-DuDuZ7dJlKnOfJ5Lk4O_xcPAEpn2fG4T0Kg79sJlqeKMOWHHgp57Pqc8OF37T5cxZxfvtqwCf9XTCvQlkHhoLpwyeeu1ALBAO_-zCrDkxuq5GBzEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24380" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24379">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9C-6-eyrzL1gqJ-5vrWDszkN1CxrsYriUbciSbj6Cu-DN77Qkbvksw2mkPfevOg-EIF4GkSlA8AutPrkQjDM_eoWnwM2Cfo8XCeTZk3emFRkZ2Mx2Dd97WmnHcroD1cU-JdJnB0KWN0KfC35UeBmC8CERCR14K5GSdIcNtqnA_JLbPlZRMWwmXEYpn7raoOq-9OEj6kaEa_L-2hAreb5UkXAG41mp9-00xpB945d-VfGVmUVtDfguGZnzF2EEjXRy5dOhxTqaLf5Ov43ziqucyCR_ohQ7HgSOWWSJKe1DaqCKPFrlHKdU3L5oM57wRkMbaMENozuzLqB-5HGJIPHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ داکنز نازون مهاجم 31 ساله تیم استقلال دربازی بامداد امروز مقابل تیم ملی مراکش این‌شلیک وحشتناک‌رو روانه دروازه مراکشی ها کرد که‌با سوپر واکنش استثنایی یاسین بونو مواجه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24379" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24378">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2f7b8fb9.mp4?token=dHzK4Nn2p83J5edL2InUtq5SOeMphnYUxkidyPgmtkCVrsi3uR8ocPUizlXPn1XqBQvQvQdqHq8iDwlxjQJeGOXes83OaIj1TTaFP9O2zsnZoKrXVblgcjBSOFGQqDjHs2WaM0qZ85j6oAlD9-7Az0UwGE1EACtpZLXu3X4mDngeldt4kV_8ysCsxTjBONJ60O30zwpVTGHAq9sElGD5GQqR3JdT3whslWC4qpWpIZ2FST5IUS2KNc1LUeXhjC-JcuIuF6eCY2t3UwpUXeBks4WBNH-bBqNWUdRktkrvNI95QJp4Ee6niJ8kgSzWOc3wYTdJXbmWmIR1qjHZYI7UzzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2f7b8fb9.mp4?token=dHzK4Nn2p83J5edL2InUtq5SOeMphnYUxkidyPgmtkCVrsi3uR8ocPUizlXPn1XqBQvQvQdqHq8iDwlxjQJeGOXes83OaIj1TTaFP9O2zsnZoKrXVblgcjBSOFGQqDjHs2WaM0qZ85j6oAlD9-7Az0UwGE1EACtpZLXu3X4mDngeldt4kV_8ysCsxTjBONJ60O30zwpVTGHAq9sElGD5GQqR3JdT3whslWC4qpWpIZ2FST5IUS2KNc1LUeXhjC-JcuIuF6eCY2t3UwpUXeBks4WBNH-bBqNWUdRktkrvNI95QJp4Ee6niJ8kgSzWOc3wYTdJXbmWmIR1qjHZYI7UzzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
توصیه جالب جواد خیابانی به محمد جواد حسین نژاد ستاره باشگاه‌ماخاچ‌قلعه: هیجوقت تنها نمون. همیشه مادرت رو همراه خودت داشته باش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24378" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24377">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WY0H0RMr0otnwYoStFbPoPbdzIsTx0vM1YDCCPZUZlheib4hE8I2YTxTYH5gZa1ZN9MH79G1pxiz7XBhD_XyeWhionx_wtJg-5UblRDdd49wVqPf9rZ0kT1iYBOcOngt3w9pO54p65hyUQ8hTh7znhqjp8ktvp_ft4GlOLVtjwR5naCO8vCxFSh2nMz1lZ2OC1s5uixV1FuGhP1lq87TvX1wjivB47p4250_wGRbQMzryCjonlfSPM2NxEIJZVRb1--30trc3y--VSH84bKJt-w_JfW-N1k6bX3RdorFst8ZQZWbbWGXHE-XD-gQO0lXEsBGxkqQeuVwPKS16xnxfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران
-
مصر
نمونده.
🇮🇷
⚽️
🇪🇬
⭐️
با پیش‌بینی این بازی، هم
۲ برابر
امتیاز
می‌گیری و هم وارد
قرعه‌کشی
iPhone 17
می‌شی.
📱
🔥
باجمع‌کردن‌امتیازاین بازی، یک قدم به برنده شدن موتور، توپ طلا، PS5، iPhone17  و ده‌ها جایزه‌ی هیجان‌انگیز دیگه نزدیک‌تر شو.
🛵
📱
🎮
فرصت‌رو از دست‌نده‌والان‌پیش‌بینیت رو ثبت کن
👇
🔗
روی «
لینک
» بزن!
@Snappofficial
🏆</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24377" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24376">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_b-N7HG98R6S-pat8G1M6r5qZ5A_DIguu5iTEY37px0R6yijDd1HILw6G08Lprv6GJGxqF0fUi5Xc3dH-HokKU45aGL6zAzbyE5cow9ksQmkmdCCJTuwQ0F7nMkqrH_KbG4dhwqeMDiqTEP6vRw42JxuDyKewT6Z3J6bpxJsHGdRB_nusZ403v9Py6SjU5TQyi1Tc1CXesAw6qHMxAxi9prMg9nOc-aXaNMaUCMmJ6swAKHLUC5fgff_l7TIK_rrWSsGv3EXd-6AOarBq_dnW1LcP585KjDFs0icv4Oz9ZbOkQp4tJFnZn3pOFZIxYwv8YyuoeWIqarZ5rafKcqYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی
؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛
باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24376" target="_blank">📅 15:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24375">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUESXpf8LXH1SicUxJQ9WrC4AzNrQ2NYsVA_Vo0INZDIijRW-mXBs5vH3kJKg37WKXYRtakbqkzBLvpUdQ_VQMQrBjS0dCEb2EP6arMdYkWjhCo-rXcJEPMUStlM-lP9KwPsaFwLNqs0NwUdqxK0f6gNn7aA1LD9COGR3oxidvUIPPaxLaKsruERM11K5ct_YqhDCw08a2j45_eDl5PT-4zomciGyjks29fWcN_UD013jElcdem0X7dG3NVvoTH-QQ0wTZyORvwlGeau4HK-qyNOaaNM5pZWnVJwEiIILR9MDwYbGOtNzXLWXCjSQZ16oqQm2sijsAWh4bHbP84vQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24375" target="_blank">📅 15:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24373">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNZsJ7_Dmu8ClNJOYXOlGVhpmWgLzoWQXdWFQEiyPGeJIrtUnSNqIPu24cheGmeSrb8xsnDARbh3-INiGgYxhfVkOTnnUZroo92d8FhcDIvl9kS7CLxhAC6tGi6SsQ-JaWI0fEx04E8N0aDWxs9ByVhy2WatcN7Xu-H7ELJmG5CDUGoGaYHtoLb-5wsg22vUFytFWHaKAMYb3QGVs8jQHGT5P8FjrwnHkVQJLYAhacSXXrlFQJsqCPXizj8SHbHX7GWZ5tIwIuU0ylfkpjVs4FtocpygzdWXho7qQ9n5rZAf6fW8QuoqmxOYNVbZ-kFGaLOGMd697t2NH6ujYX8Edg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=JX7-V4OLP1v47APx381u1eK7zKuzS2AgZw_C0w1LLdQIUlQPVizQwVpPpBnheTnXslhywqgueLlhI7tqnkNcmrh23t5limyGFsXGvbXYWBwMY7E8V54QtJu16gonnD4VF2SBfdxiIldWK0lc608gfB-ll17D2rEc0E6qjCHaA0sBK6A8JXmyjZWeuJ-z1_hUVwc76rkxkCQ-hXp3H9mvE3p6KhqZRV6kvRzOfLHB6Bw_ApAzom0mx2H4mKbIvz5SnLeZ-5ng5VbFNqXk3QQvC3SxuPrTuEurf6LlgTbdkTnZpyjcm0DecPHEPJT3H-z5aXLF5NtcpGzrg0BhWZrx5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=JX7-V4OLP1v47APx381u1eK7zKuzS2AgZw_C0w1LLdQIUlQPVizQwVpPpBnheTnXslhywqgueLlhI7tqnkNcmrh23t5limyGFsXGvbXYWBwMY7E8V54QtJu16gonnD4VF2SBfdxiIldWK0lc608gfB-ll17D2rEc0E6qjCHaA0sBK6A8JXmyjZWeuJ-z1_hUVwc76rkxkCQ-hXp3H9mvE3p6KhqZRV6kvRzOfLHB6Bw_ApAzom0mx2H4mKbIvz5SnLeZ-5ng5VbFNqXk3QQvC3SxuPrTuEurf6LlgTbdkTnZpyjcm0DecPHEPJT3H-z5aXLF5NtcpGzrg0BhWZrx5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سباستین بکاکس؛ سرمربی ۴۵ ساله اکوادور بعد از اینکه دیشب تونستن آلمانی‌ها رو شکست بدن و به مرحله بعد راه پیداکنن اینطوری از بین جمعیت همسرشو پیداکرد و از نرده ها بالا رفت تا بغلش کنه. البته صداوسیما این صحنه ماندگار که تیتر همه‌رسانه‌هاشده روکامل سانسور کرد تا یه وقت تحریک نشیم. برد اکوادور روی احتمال صعود ایران هم تاثیر گذاشته و ایران با مساوی جلوی مصر احتمال صعودش به عنوان تیم سوم فعلا از 90 درصد به 60 درصد رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24373" target="_blank">📅 15:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24372">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0edb018d7.mp4?token=nGixgz7zbs6E4dpzSefCixi9O4umO4pwxNXz4pP91PNrlV6l8tZucdHTREe2eDGqh5BBSzxUr8z-B_b3pKc9aNNMl3WhkmFmy8HFM_CkuqJ5jnvVbysPFGa_RTB-7_78_dg7b-QzkYePP2jwBmUXiAqZCIwuzaD4SXdfuDrMOEs0Lwc7dpf5KGK2RhKcFMmsQcbdIWlms1C2b7ULxaGSsuoffooKcFmLnabCPmU57N8q3RxuaU_Z5Qr9eTYC_NOx7Jva3DDVdQIyZbmH6JBwebeej_mQk2dgRxKAK3uQfAiSHTcPNp0KKvZrLcpEe1NypqhbBj8HgLOGxAhJsabgJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0edb018d7.mp4?token=nGixgz7zbs6E4dpzSefCixi9O4umO4pwxNXz4pP91PNrlV6l8tZucdHTREe2eDGqh5BBSzxUr8z-B_b3pKc9aNNMl3WhkmFmy8HFM_CkuqJ5jnvVbysPFGa_RTB-7_78_dg7b-QzkYePP2jwBmUXiAqZCIwuzaD4SXdfuDrMOEs0Lwc7dpf5KGK2RhKcFMmsQcbdIWlms1C2b7ULxaGSsuoffooKcFmLnabCPmU57N8q3RxuaU_Z5Qr9eTYC_NOx7Jva3DDVdQIyZbmH6JBwebeej_mQk2dgRxKAK3uQfAiSHTcPNp0KKvZrLcpEe1NypqhbBj8HgLOGxAhJsabgJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏰
بیدارموندن‌ساعت 3:30 صبح برای درس خوندن
🆚
بیدار موندن ساعت3:30برای بازیای جام‌جهانی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24372" target="_blank">📅 15:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24370">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PzDhqXBCk2sgqxwZSp_T40wgsqPIeMjiyuhYoZU4kfFAie41_hlG2eLUMW7E0KddmLp6rANEwwliFDLT3CkMci9nNtrPTgRAkRKTPaW63toODWMEUGAmsjHNfELv6xD4MH-07IBuJv4jPFvbCV9fd2uT3P4thM0jwmOc0SymXHRF5LorvJ5d2UNnQAo5H5H58Rdhqx2hBOroO0CTVJLsrQrz2jnDAyv14D4gt3FbuUC9rwRKhA81dTDzdGQhN8UFKDnsV_h4F4tnviSaqchPthqFpJPdJhN9kBL4uATB94mhjyI9MA52JanBl6p1LWD7I1lUfPjnJ0REOizSp3FQlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oNHlytU9h1IPq1JJLzGSY1nDca8v4CQ00YjjnEVkRhBHRGzdzwO9TDI5rYudwvsxfjb0v2b-GxH396HQEbIDmog1cojLXHHSrgRYJZ-k91advxaDTSG7Y_Ppu4TWYOFTKzB6LYTTEz6VB1mZw4YLav7LYsQN9UCuYZvhrjApggRyF31AOrwPsteWB70_RUgDGnuI3cm1GWiUTnw6vT0v3cnVJdeXG4AXPyj86gRjAo38pAkyLDl6a2OXp--TTFdDhp3KsL0ml1RdpjaVn4dXZNFtFSUvugvYwZvnsiXjDFp0SPr7BkELY8lkaF-XI1-nbiwIFBX0cOfFIvGdkqPrzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24370" target="_blank">📅 15:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24369">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCBqkvs98eqc7lXrz-uvMy6qu9z9pw7qVUmZKjIHNaiF6ZCmvfAdeRTjHBELKW6aV3RZDqLnQoKGpsSsEt_FNKBsTZhn9I_CCjWfEk5bS_mGDtY-xj_cepsUcCkQr0POFWAq4u0byewJi6HGWWKL54AVoD_It7fJPxfwUXUb0uRiFT2z8cwTcM_I_I3r14AzJfChaG1aJBbQ85l6S72j5Gc7MJoC-alnnMxPfy7Ebw_sbVdfrHgWiPrnNkLV-0iZFUB8XZcXTZOHlzQeDN0FHvWKZDHPCrMIG139Wyp9wfAAD5OKnJJoJu_96rXnbAuNFa3nKpmN5KCAh7iXTUeaTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال ۲۰۱۶ سمیر نصری که‌بصورت‌قرضی‌تو سویا بازی می‌کرد، برای درمان‌سرماخوردگی به یه کلینیک تولس‌آنجلس رفت و بهش سرم ویتامین وصل کردن. بعد از اینکه کلینیک عکسش رو برای تبلیغات منتشر کرد از اکانت توییترنصری چند توییت عجیب منتشر شد که ادعا می‌کرد علاوه بر سرم، «خدمات جنسی» هم بهش ارائه شده! توییت‌ها خیلی زود پاک شدن و نصری گفت‌اکانتش‌هک‌شده.بعضیا هم حدس می‌زدن کار دوست‌دخترش بوده؛ نصری امروز 39 ساله شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24369" target="_blank">📅 14:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24368">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ab6e00db3.mp4?token=HhPMbYryyzkSKcZmvi8wknGcOio2RM2qcTN6wpboZhAbnKcDTcRlWBRneldE5tUVxldtQdHnOPwSo252WtCm_0y44yZBEPJmtiFN7lCGmATXYDee3NAqDGS_fmBco2XGKwop6jP2tLb7UajW72VjKNC1LdUxCLTQPI7Y9MHHMNg5C0aaBU7XUiAhjcwwfVghfobVPG5x4icMWZpBV_l5xrKtLI8uj7c0NoRb-AOfDSq3rU1g0xBMcaIKrE8iwcoyVBORJiaYNKsMCz8S3bhrHIruH-2r_WNte4mqsJlKmSUfbyQP3mKkj-LETOST2WEHvtSJoyMZ_R2Io7vCT4Y5EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ab6e00db3.mp4?token=HhPMbYryyzkSKcZmvi8wknGcOio2RM2qcTN6wpboZhAbnKcDTcRlWBRneldE5tUVxldtQdHnOPwSo252WtCm_0y44yZBEPJmtiFN7lCGmATXYDee3NAqDGS_fmBco2XGKwop6jP2tLb7UajW72VjKNC1LdUxCLTQPI7Y9MHHMNg5C0aaBU7XUiAhjcwwfVghfobVPG5x4icMWZpBV_l5xrKtLI8uj7c0NoRb-AOfDSq3rU1g0xBMcaIKrE8iwcoyVBORJiaYNKsMCz8S3bhrHIruH-2r_WNte4mqsJlKmSUfbyQP3mKkj-LETOST2WEHvtSJoyMZ_R2Io7vCT4Y5EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیم‌های ملی ژاپن و برزیل بعد از اینکه از مرحله گروهی خود صعود کردن به همدیگه خوردند و این مصاف جذاب رو رقم بزنند مصافی که قبل ها در کارتون‌محبوب فوتبالیست‌ها پیش‌بینی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24368" target="_blank">📅 14:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24367">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=j3i5DH7iLFj_vT_lbrZ_PKBD--xSPQNJfNLbwlQs2gFYRa2ukXUEqSPRkeQoHoH_ZgA8A42mIfY3dQy9FFjOfhEhly0XzS9kPVuJ6VUPW9QzqczUahK8uXABj_kkciiKftPdlF1FaHb7mp7frvEsyYJjzIdfm9jpRfGXJFn3XGEMPi6UpUwl2cZonpN3Q6GpVfkbadzEIINU0F6yIEVvmHMGjk4O_GWrjQyeMsbn2rqVWjMIbsJL_w_2r98Ni2cc-1F1pic_8vbtnmZI3JhT1aTEtiRXEg0fMMhSJKcSFdHupx6d9pyJ4ITB1h2JbaZkEiATa4IGEHsVA7FKoGmvgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=j3i5DH7iLFj_vT_lbrZ_PKBD--xSPQNJfNLbwlQs2gFYRa2ukXUEqSPRkeQoHoH_ZgA8A42mIfY3dQy9FFjOfhEhly0XzS9kPVuJ6VUPW9QzqczUahK8uXABj_kkciiKftPdlF1FaHb7mp7frvEsyYJjzIdfm9jpRfGXJFn3XGEMPi6UpUwl2cZonpN3Q6GpVfkbadzEIINU0F6yIEVvmHMGjk4O_GWrjQyeMsbn2rqVWjMIbsJL_w_2r98Ni2cc-1F1pic_8vbtnmZI3JhT1aTEtiRXEg0fMMhSJKcSFdHupx6d9pyJ4ITB1h2JbaZkEiATa4IGEHsVA7FKoGmvgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه نویی درباره حضور پرچم‌های رنگین‌ کمانی‌وبرگزاری‌مراسم‌حمایت از جامعه LGBTQ در ورزشگاه سیاتل گفت: مااینجابرای فوتبال هستیم نه مسائل دیگر. تمرکزمابرروی مسابقه‌وکسب موفقیت است. درخصوص موضوعاتی که در دین ما ممنوع است و وجود ندارد، نمی‌خواهیم صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24367" target="_blank">📅 14:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24366">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLIUBRtHwTLDSSnF8b9MI84ilYfp54UYIX5Ls_hVCBGuUH479xwsD01AEFQNGLaRzPDmQIC9EM09Ol_avwMaqHUWGyTi8OMN_DUclJ4KZBIrqy_ZwbLGhEqX9DU2qter1QhfAy7oPjbrg4P05KQvv_kOjT6i7TtYqXJB5TlAT-zuRQZgDdjJ7pZPlvwUNR8q8pSiFM9W3qRB9FfMplDDJoqyTt4tdePaFNGqdGJ_CU--JWyCu51gnYJPcT9NM4ueCrUUSI3H37IOnbqROtB_IrKPU7-t08X2_aNuQZ7tL0SFfInloe0RHu1EUXwghdU1oNBApCnaC5vIaxxBBhJ9Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
دو پست کریس رونالدو و لئو مسی در ایستاگرام رکورد داران بیشترین لایک در جام جهانی شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24366" target="_blank">📅 13:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24365">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhpLuc31bQsLF3Vot5ZHRKD9_cnpzXBB1MGI5t9YQkVuuMaCOUh1VEzgv0MV3ZekraTQaUB6FNZiNEQ5vZ2OZJEBYOfVu81qyba4E7a-9woV3bHu3q_uKNsREVKIYgqFFyVx7lyBqHWxkreKzExYS6dW2rvq5xjxKd5CtOj8vuvGNzjLvp3_p5YIfGL0opts2kfAlzlDWrHrIMOQ4ELNdmIHTBpe1IJBy35KBZ-FaL91PIeeH-voTOKZonCE6EV18PuMhkzS7Ca92KtZLkjdp-dBcILO9JpZSiqOAUWqa1kTlkQQKdiMQG0Q2pbauLhllH-UUBNJhuGCPb8bMYvCNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇬
عمر مرموش ستاره‌ تیم‌ملی مصر:
ایران تیم خوبی داره بازی‌ های قبلیشون رو دیدیم اما ما اینجا هستیم که قاطعانه این‌بازیو ببریم و صدرنشین راهی مرحله بعد شویم. بنظرم بازی رو سه - هیچ میبریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24365" target="_blank">📅 13:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24364">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJ97xXSC8O2NvisDIuUbsOE44NhrwmUFCDIHF7w2PjvbIyrCWhfhmNDvXCdfX-aiOXKnKQZMV224965nggeRtiiSvADuOpcMAS4OXOzJw4N83EBgiZRAMvwSvYK00yTpdMw0swHaWB1ixDnwR9KKBe04NS_4OQGDz2ilnvzLGgS1qgGo92oJuluDYQoAVIlpOzkw1xXZTEgCbB3BbMaT8ScNl7Y2vuzqOicGo6o9AijVSdeRa675y3vNGq_uDmtVaZho-evD88rl21KcZowmQX5-5sEI4kN3viqdJgFF7keOFe_AR9kK4x331KO0VCBWFgYMCpN7V4PamPRqLvwcYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24364" target="_blank">📅 13:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24363">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThIZ6Ut4XeMAoEwDk1ReAY7qgdOX6Ow9RS_UaZRLnF-YYl3YdssdeQrfBvv4Rt-H46mk4i2SpjpWqpUVYBynNoc3Sbs_VyUaa-H0s1AVrcSM5wCXiCoGHK9FgjMM7VzQ6pitVVG7_AJSCUUOhCpWRPF3odMI4NLEcrwCBjOmjRjSRE06uwq2-cl-KVcTJUSKmzX88WKLMbGUxHF0gYsKBFMNxrcMe4p_-o3WK2RJ_3Ezi2d1Nlg2BsX8X80BRYZROV_RCCAbxE54LpR3elH8QGPpLw8WsTdO9h-uWF3-ML9WwcvqML73zg3FwdCtK36scDDR3KPV_MV93-qMf4ANAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24363" target="_blank">📅 12:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24362">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJ2wi60BaL8pxVOxl7pt1NYfOTGgQNMeoyOaeYs13m7G6UdXvAbn77OTpDqOYVSWyPBY1t8GLrS6G4uuilqftjwF_BfOMSVqD67NP267L8o_GnVs6wCgJFf38iPnYtQ_MFm4H_h_SiLGNSZb4vOdGuNGKZkTk-NyllPpIPi9t_QBCDBkcG9bEyxW_suuhckslo_9cHWIgDRpRaj2WzRZ40OKWy1e_hoi69zoOg7cFEzgaELru_QMquMIM9F7j8rcHTsTpB6nTjpuaKI8B3aOwldRtcmCil2eEMsHfxVB3sJv9H3F8tDix1LP_mZZgg-ppfvgZJy2dhqAuJydkvi4qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب‌احتمالی‌پرسپولیس برای دیدار امروز برابر چادرملو اردکان در تورنمنت سهمیه آسیایی؛ 18:45
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24362" target="_blank">📅 12:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24361">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Erlz4YymLCrwZ4M8jK6WMrVfSLACqav4dR_tOkhvCszxXBV4dObmExutjpmuyKUVkmkEBMyqUMJwEq3tpSFQE1H6qzwnxSGl6kc-HDoTrSF5cve7uH1crHe9qTQ7KwYRhCdbYMeSy-S32jeWC2-uc1VCTBMoCyUjzz4HZ-jJK-zNfYifub63HIh0SpsYQxpbrpA_GhB63ZeDJhYRCH6ESH4piazB3yL_rJMthfoGmo4RJJRyVVg8uuhakOx6ku1WkDNRwxluuG9NFpTyqub4kg1ERpK6rpiatFoAs8dsxqj4o65rgw2Mf8GlNf9tlseGQmRrKqQ2M2TksWoUFX00Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون درآستانه‌دیدار فرداصب با مصر بیانیه داده و گفته‌رژه‌همجنسگراها قبل بازی رنگ پرچم کرنر و پرچم‌های بین تماشاگرا و هرچیزی که مختص این موضوعه به ما ربطی نداره و به اجبار فیفاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24361" target="_blank">📅 12:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24360">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b03de0d7d.mp4?token=WfGAkrvSoFWqLQqTI1AlXPwAHnGNnnhUcWCOqO4hwdmz-fq8v17GJgX-SPwwUy0VOPS9Gm0ZNVDw4v36SEOAf62AD_YZ2BS_s2WkG_VP-mDJ0FYoVTeiPrRKeJzvLlIViH60uD_X8ShZaK4mnJLepowUhBFNnBAW8kaFhvSZmGGbRoUtle2G7D7SnewbP_aQ8iRukjOVes-noW8iT-d8sXcMgNYxSbEd7BzTALFtPnh43VsI5fqKjTAgXaAg5SD0jxIBiKDQxXlBJmTvE6JQZ_ckufwv9TA9Nw2IDjQohzsEASNd-5hm8I18tclUyAcSguNgJFFADS1_OfbOonNp8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b03de0d7d.mp4?token=WfGAkrvSoFWqLQqTI1AlXPwAHnGNnnhUcWCOqO4hwdmz-fq8v17GJgX-SPwwUy0VOPS9Gm0ZNVDw4v36SEOAf62AD_YZ2BS_s2WkG_VP-mDJ0FYoVTeiPrRKeJzvLlIViH60uD_X8ShZaK4mnJLepowUhBFNnBAW8kaFhvSZmGGbRoUtle2G7D7SnewbP_aQ8iRukjOVes-noW8iT-d8sXcMgNYxSbEd7BzTALFtPnh43VsI5fqKjTAgXaAg5SD0jxIBiKDQxXlBJmTvE6JQZ_ckufwv9TA9Nw2IDjQohzsEASNd-5hm8I18tclUyAcSguNgJFFADS1_OfbOonNp8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌هایی‌که‌کمترین‌درصدمالکیت رو درتمام تاریخ جام‌جهانی داشتن رو ببینید باحضور افتخاری ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24360" target="_blank">📅 12:21 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

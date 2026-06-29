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
<img src="https://cdn1.telesco.pe/file/PBR8H5M16ERMo2WctkxvkWLNc-ZjwXXHtfMD5IWphwszyal55kZNaYx6dWZT1SY5e990imYCzowOYHT5NfBYnw4OOdC4msWUf8c9-jbX4UHS7byaUzYxsg0iC_-Ly9PN7EV8YJmJQwrhcDNla76Gr3x3lFyirzOl0SDOPpTfzw4ReqrPujyxHlV8u3Z63KS225siIk2nFoniqNIj__l9geXea9ggwz0CMpnsqaAQ5lAmq48aBdjN6B9KYAOSqZTsOPDw99uNedyKFs9ByCRMygV7ODoQxiieLY6YFbJBP48XOIcR255GXxPl8skwKGZLfZ37kvXZUxSBWHg171pBKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 160K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 03:25:16</div>
<hr>

<div class="tg-post" id="msg-4126">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وسط ویدئو متوجه شدم اگر کانکشنتون با api ها خصوصا جمنای قطع میشه هی، می‌تونه مشکل از proxy-ip یا آیپی تمیزتون باشه
گفتم این نکته رو بهتون بگم</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/MatinSenPaii/4126" target="_blank">📅 01:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4125">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کمی ویدئو API بیشتر طول میکشه تا آماده بشه
صفر تا صد تمام API های هوش مصنوعی رو میگم بهتون
محتوا رو فدای سرعت نمی‌کنیـم
🥰</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/MatinSenPaii/4125" target="_blank">📅 21:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4120">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.8-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4120" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⭐
نسخه جدید WhiteDNS VPN 0.0.8 منتشر شد
میدونم آپدیت کردن این سرعت یکم برای هم شما هم من سخته. اما تونستم دقیق مورد رو پیدا کنم و فیکسش کن
ی
م.
ممنون از تمام دوستانی که نسخه‌های قبلی رو تست کردند و مشکلات رو گزارش دادند.
⛏
در این نسخه، مشکل لود شدن بعضی سرویس‌ها مثل یوتیوب و اینستاگرام برطرف شده و اتصال‌ها پایدارتر شده‌اند.
✍️
از همه شما بابت اختلال‌ها و مشکلاتی که در اتصال داشتیم صمیمانه عذرخواهی می‌کنیم. ممنون که همراه ما هستید و با گزارش‌هاتون کمک می‌کنید WhiteDNS بهتر بشه.
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/MatinSenPaii/4120" target="_blank">📅 18:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4119">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اگر نمی‌خواید این بلا سرتون بیاد و کس دیگه‌ای بفهمه ای ایران هستید از وی‌پی‌ان‌تون، از نسخه‌ی جدید WhiteDNS استفاده کنید</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/MatinSenPaii/4119" target="_blank">📅 18:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4118">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ولی GLM 5.2 واقعا عجیبه. قیمتش روی api تقریبا ۴-۵ برابر از Opus 4.8 کمتره
این چینیا چیکار کردن با آنتروپیک، خدا میدونه</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/MatinSenPaii/4118" target="_blank">📅 18:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4117">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">☠️
آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI
⚡️
لینک‌های استفاده شده توی ویدئو:  1-فقط گروک استفاده شد. ویدئو رو ببینید متوجه می‌شید: https://grok.com
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از هوش مصنوعی استفاده کنیم تا ابزارهای…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/4117" target="_blank">📅 11:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4116">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تمام سعیم رو می‌کنم که سری ویدئوهای AI، برای همه‌ی مردم مناسب باشه. تنها خواهشی که ازتون دارم اینه که نترسید، وقت بذارید، و ویدئوها رو ببینید و کار با این ابزارهای جدید رو یاد بگیرید
🥳
خیلیا که کمی از این فضا دور بودن، فکر  ما داریم راجب چه چیز خفنی حرف می‌زنیم و ...
در صورتی که شاید تفاوت درک و دانش ما از این زمینه با شما، صرفا دو سه روز کلنجار رفتن با ابزارهای مختلف باشه! همین.
به محض اینکه کم‌خوابی ۳۰-۴۰ ساعته‌م جبران شد ویدئو رو واستون ضبط می‌کنم
🤲</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/4116" target="_blank">📅 11:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4115">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GhA5pG-4gL7g5x9kfaQhW8yC8xWtUP1FXIK6IxcddFQzLTNAlOXjsbhbdQy8VXBdMghvSDxvxqOvGlAznHzAeXhwi4qQ0xgYual4kNiM6HTQvYR30Cvs9gS1SqNOEexfYa8BCsaB2NbMtMytCRE_KGX-zjMTKuR2C6APx1TQD-NChecRXJ222tQ6u-bJSpfGIiN2aXo7QFXyFJTudoUdREGIgNp3QXrNdftDgmEHkRk9TnNUpdX00q3QfQrYrs4lPSA8GfEzKv4AaDl-bxOxwR1jftVmGowxAuXEeIFI_45dWkq5YCwBJooJKppd_RdsZ506yS_v_sRtna-FQNN9oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت هم دقیقا شبیه همینه حتی قالب‌هاشون یکیه
😂
https://api.bluesminds.com/register?aff=drPB  ۱۰۰ دلار میده باز هم میگم مراقب باشید و توی پروژه‌ی حساس استفاده نکنید</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/4115" target="_blank">📅 11:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4112">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Tbz1ksNe-mCH1opV5Pj-DtpDSHox_pesKhZNdqrjkdg-_XlQnl-nGe9nRbhtFq9e6OP2DL9RrlSSoGvNbr9k3Pc25-QBPT7fsgB2B0TzBw9pyhDZ4CckXz_aB5cbVN71sCqo03SekkfO6NqA2xTOYnY6ysWxPSPJFNJxEOm-VMmHtMSVI8yJPmQ4DXF9_YY9L-C5sYtQ2BVmAn7eleTeVnLjoaH5rmGUnBSXR8sYgc3BFKRGmfkNpZLd-EC8tzM6odxj0AElAXbJY2UZ-NhgGe1q72wtwOIPMi-ZS1YqBFqf1eq5Gkm29x-yK-katePJA6gr0-80wilpdvGpRaEVUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NG9itTn9QFYXB6Loyju6bP99nn8ZoZR0xSjAf0YqkkjT_e0s4vJtTR-LRIv9Ep1lyb5mj5L35xHdAHKWQrMp7CMWRh8PdPUZ1bWJmkmf9ii4-_TcuQU9m6JtgTwy46Q0g0gIz3LZSidA9Uu_JukhsszYqnrPtKDMEyRrxRsSFQIE6R9jiUBuzuRIXtS3WBYgHBkdProvLIbfKh36YhSC2qWGUIMoOg153GNy1GUME1brsTDAkmRJhUjo0O7we6sl73mhYJSGrJjYxmf3AtUsQSqJyQT3eje_qc3YX1e8bylhw5-DOiAqKiRcAUY8KRUZWYVESixSACQOgzxmF5KK-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ugZJKP9Gvcv2mVzpmTZaJonb0QyqEru1ivI1pZui2S-NsxNE8f1DU6jjURv9bkqnE7NHrbMjsgZHbgXm0umwKo5gjJ55ltG1EelyMDcoYBFOu6odLNcNzUYCWYP2e9_zBEWQbsm4VLZHbgEnetdAKthwEE48Rc7POzLr0wmPKgCMd_fMSDRPE3n20DBHMO0wZkP3Wl_9-SOAlAS58xR2ay6pfHFrJtil3GViwhOQ6N5lOGfQfGH3j18W-LBrKjMTJuFYK10Yra2ls49m3sLTpteC7vpwku6gReUOa6eLRA28cKSD3NdNYExAatW5QORnlK-SOMjoSFrN-Q5RpcgC4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی واقعا داره پول میده به یوتوب که ایرانیا رو به دین مسیحیت دعوت کنه
این تیکه هم از یه فیلم بود. دوبله فارسی
😂
😂
وبسایتشون هم بامزه بود
https://daneh.online/four-spiritual-laws/</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4112" target="_blank">📅 08:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4110">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/doz4p1z4rjok_wei3F5KZ0-fN_0L10mDvp-TAQ5YDjgDYy0uxP9weJbILRSN77scqeJtTpL57vSrsdb4ZEG7AyDZGYVA8AylXNXvSiqsNRydyLqHIzTIt1qG6047gEpQ6WUkYYPxpH8bvJnjFM5gTXqLk1sTDaTcXBrQbu0iZt5lmP_kx3qjSAtl74drBy87Q8c-u-eRPAw8i3dF0XMZCveWDtbjnXxnXC-Dxg16OEt1Esf8fgBFbS5-u0KUq5cPx8Gu78cjRep4kulAmOC-vtV6rl1mW9CKAhz8ZgqBNMktIuXEDWuFSh6SlOS9WgEFZPMFavwJPpcx7kQ9LayvVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DKq1XrHvUWsUug9C_Nw_rYhREFhzZOdaalhmna9LecpyIafikj2tjTwCt85-4AclO-XQVmUrYD_L9UCkVr3wAyCFAzdOCJBup0GApxwKIJYMijI1rsHltA8dB1pllrAZzUtiPkXv0ZjoJCCqJ1nTdz8oa0NxfbnLQcK3LoEW58aghYTVnIW-zZKdB8U1WRbGAXQjL8iAbkkfVHVkpYVCfW7RNbt7Mn2RUZA3A08x9slw4o6Ok_bnq70Py7UfWQsTAsJ_eYuyvdt-FKTs5C2_q8266Hc6OsgjCUBWyGgevCUtKdSgEvE6UCAXtUg_ueRWY9bf0JJbj4wL4KmCan8rFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر حواستون به توکن‌های Hermes و ستاپ درستش نباشه، اتفاقای خوبی نمیفته:)) همه‌ی اینا برای یه تسک ساده. بهش گفتم برو نقدهای منفی راجب Berserk رو بخون و بهم بگو 10 دقیقه طول کشید و کلی توکن سوزوند با gemini-flash . اما در نهایت، نتیجه خلاصه و عالی و دقیق بود(حاوی…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4110" target="_blank">📅 04:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4108">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C9xDSSiE5ALsWabPDTC5gAzKYSJ_dmS5Erb-dQQ6CMmStje2iVsZYU-Y4EFMMhiyUtIgVfw-x3WJKY8QP_G9fUBACEv3Nbqy3q17FcsNpoyrGPO9fz-7fwKROOSBnBG6t0nPTbe2ur0REHF5TAkAJn7bga06rrMOIcNnfM5eoiUX02TNQ8WZjyucQLT_RtoOLrYN2cSCDSfbR4Er8mLi-hN_Jo5QBYCJbiUK4YZ2apLZemQSeHONT0e1Iovdi0qyENusRG9qWTbP228izlNpo_POxn2soNiYYCfuGka2SfxnsV9S_JSCN0G4-sC6sBjB7QaESnHuN2QRjwn0zv2imQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WpMus6mfrLVaTJKQ_6pkcwb4JqVVEW2FKlq-79Qq4P9uqwRaTfOAvOeI-o1yEmvhprCFeqpz4XnhwLAcsRP2ihuKBmF1TTK0NKtJgb02U0akRrhCo4uWT9xgV966aGcfLh9tl1fCo9KMlPv7wokPUthTGGXPSTslMYfcnGQBn40MDErSh7ydS_w985KktZrpY6taCR2HyW7ui7x32a6tnk8VyZm85EA1JKurKWx_LUc8SRN0_vqEU9oKaz_DTB23mRjlfvibKxgdDn9p91UrzUYcFv2yXMWzE1InAnyMbi5FNQS7Pzh-0__FhmX_6_d-xs8ctQ2_9CqoafWsO7SF4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر حواستون به توکن‌های Hermes و ستاپ درستش نباشه، اتفاقای خوبی نمیفته:))
همه‌ی اینا برای یه تسک ساده.
بهش گفتم برو نقدهای منفی راجب Berserk رو بخون و بهم بگو
10 دقیقه طول کشید و کلی توکن سوزوند با gemini-flash . اما در نهایت، نتیجه خلاصه و عالی و دقیق بود(حاوی اسپویل طبیعتا)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/4108" target="_blank">📅 04:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4107">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یکی از خفن‌ترین و کم‌هزینه‌ترین مدل‌هایی که می‌تونید ازش استفاده کنید برای ترجمه‌ی بسیار روون از انگلیسی به فارسی، مدل جمنای gemini-3.1-flash-lite هستش. روزانه 500 تا ریکوئست می‌تونید بزنید و 250K توکن هم داره. از aistudio.google.com هم می‌تونید بگیرید که…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/4107" target="_blank">📅 03:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4106">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یکی از خفن‌ترین و کم‌هزینه‌ترین مدل‌هایی که می‌تونید ازش استفاده کنید برای ترجمه‌ی بسیار روون از انگلیسی به فارسی، مدل جمنای gemini-3.1-flash-lite هستش. روزانه 500 تا ریکوئست می‌تونید بزنید و 250K توکن هم داره. از
aistudio.google.com
هم می‌تونید بگیرید که بسیار راحته و توی ویدئو بهتون یاد میدم. در کنار یه سری api و چیز میز دیگه</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/4106" target="_blank">📅 03:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4105">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رفقا اگر می‌خواید از نسخه‌ی دسکتاپ Hermes استفاده کنید، به نظرم یه دور Hermes رو با Keep Data حذف کنید و بعد، از اینستالر Desktop استفاده کنید. چون من دو بار روی دوتا سیستم مختلف تست کردم و اگر اول CLI نصب می‌شد، بعدا با Hermes Desktop میخواستم نسخه‌ی دسکتاپ رو بگیرم، به باگ‌های به شدت عجیب غریبی می‌خوردم و یه سری از بخش ها کلا به درستی نصب نشده بود. الان که دانلود کردم از
https://hermes-agent.nousresearch.com/
اینجا، اوکی شد</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4105" target="_blank">📅 01:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4104">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کار خفنی که پدرام امروز کرد این بودش که جلوی دی‌ان‌اس لیک رو گرفت کلا توی اپ WhiteDNS
اگر وصل نمیشید به اپ، حتما از Fronting IP استفاده کنید.
من که با سرعت بالا وصلم</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4104" target="_blank">📅 22:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4103">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🌎
سلام به همراه عزیز WhiteDNS
تغییرات جدیدی روی سرویس WhiteDNS VPN اعمال شده که از همین حالا در دسترس هستند:
✅
تمام کانکشن‌ها با دقت بالا از نظر DNS Leak بررسی و اعتبارسنجی می‌شوند.
✅
قوانین جدید پراکسی اضافه شده تا سایت‌های داخلی ایران به صورت مستقیم باز شوند و دیگر نیازی نباشد برای دسترسی به آن‌ها VPN را قطع کنید.
✅
تبلیغات از بسیاری از وب‌سایت‌ها حذف می‌شوند تا تجربه بهتری داشته باشید.
برای استفاده از این قابلیت‌ها نیازی به آپدیت اپلیکیشن نیست. کافی است یکی از کارهای زیر را انجام دهید:
• یک‌بار دیتای اپ WhiteDNS VPN را پاک کنید.
• یا اپلیکیشن را مجدداً نصب کنید.
• یا حداکثر تا ۳ ساعت صبر کنید تا تنظیمات جدید به صورت خودکار از سرور دریافت شوند.
ممنون از همگی.
🙏
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/4103" target="_blank">📅 22:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4102">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این 9router واقعا ۱۰۰-هیچ freellmapi رو میزنه. شاید کلا با همین بهتون آموزش دادم</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4102" target="_blank">📅 19:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4101">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یه گزینه هم داره به اسم disable ai
هرچی فیچر ai هست رو غیرفعال می‌کنه توی کل برنامه
اینم برای عزیزان دل مخالف ai
😂</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4101" target="_blank">📅 16:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4096">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rktgxvxOCiJLw61hk9I8EtmPcq3CEIgwPIqC4ADa6IOM-m0Nxd0XUfKQdlPdpp64dRGjw977vV6EEh3RIGLMD2qEMyNJPl93bfWfjLb5U1ztWkFh3lZCVlLVAVbPO6EHQehGP9sAad067zKgjkLkbAaarRDhjCmzdyGzLHKR5W01oH1m32ykluoqP7LwxAg8qH-dUhipMRW41oClDVK4i98aMVguHcMz5q1sPOH51d4aiPHdpJuzDpLIhiQZm0-UiHgD8AU57a2uXqEBmCeDmLgJwdcyvhMk-hg-lVKU4tyDqAppRPDm4JvUztqEoOy9zYqDA9hw2A0QZ9sqkhUEqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iH8zXQsUINytGBAzJWqM9Qxe3q6dJrwO4WcjQQfGwKu2pO6GNJY_7E_1-Oiqb2izaDCQd4f4hYC49_fNu8FNHhjFbnHZ47YZL2lWH3v5jyuXbYKmdcRY4OwiHPSKPRQjVst-GbG5278rzr3F0eBMVWm3NIPOo83IWQOoEwpyLi1dwwLHKrvgRgecTli15USm4KmY0Fesx_sKkcPSKW83gEgWrXLmqz5IDr2jI4MwqVGUp7sjpBZHqD5V55IGE3tmGDJbRe8_vIhfyvjvc832O4Tm-Ow1d8WpQHrfDmm3p8oB5theeN2kKjAfk28shaFPG4CYcFme7YNmZkJ9FM0ybw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DtI9_Z4XtYZXi42O_ZVi6LMozIGxlIlv_2fuMvw6acY-akmy_zecHrWjB3jqsWC5GwIQFLlxAGOJU9zobjZ5bERZ8JjTLRrkzx8HXnLlj1q3XL60gvhVunN--geh25GdD-50VvT_Jp-3HQ7xipxbAGmYghupPZ2RULCtIXuJF-rM4qTse4XCGHUxATBStyBNRZK2kT1y8CX3Bmf17ufTIaamUrqaaxZRyNq7FqkZI9jyfveoNivBYipV3aMAxwMalaiW5BylaAkh5ykAmVkwAq_Y7mYxNjRfIvoCYk41RsgM1VxOsPMWA_do8WRZw6oqP8lWPpPn_lcRC0HMqhMdxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tpCkF_0l498qKtCUGemB2bmv6TBoaaJaObjZ7i42hk_-qpH-tqA6SRxSTsPjjrKNGSeJpgTfIU5X8lX9u_WXqFuMLo12Fndg-auNPQQmZVMRY9xZJGUADpjJaaVWO9yGknmFgpMJHksCrgKVwYThemSSjoPPzHuVP-8TZImZXlaLpDx2zHsR4zvu6oDDzxS0SyhqrlppMjRWZHMrnklhUqqFLuXj4PMtpMCjgpz7lZU78hIKwrZDhkYXSDb1MeBs7luYwfqRM5uPooSWw9svt8vW5h5VeF4zNoJCwBk8-64hcQG71JwBHihfkcq2RB_W5EuxpzW9sF_29ebpC6oxAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cOegGdLg3LszNeANBP9-zy66Bsiwi7mspO40J4LewKP6O8m3CRxz13GXGveDLItmGSp-CMpLWYjVga2b2Egyhs4W2Zvo88RegtlLzx6jqg6kfsBfG1-sya0l0A0Sm-bwtQ6O0l8GlBPHxwdkSrziYDFyrtqtrxDQg0QZau1Pt1czg5IMZ1e71T766aKTPlRT24bFwY3F_DHqmqHcGIcpQxEZyWUeRMPUEj9veUe4r_axEbjUxmY0m_eDF7oKotPGMhuUZAWyJCcj8FlE8f6Nxf_370T8QW0E9yAp9fNOs1qtSoi-LzXMHpzSv8cdy74Unrw9rni4vFvmYpyQZn7zGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده. به شدت هم IDE سبک و خوبیه از اینجا می‌تونید اقدام کنید:…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4096" target="_blank">📅 16:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4095">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-poll">
<h4>📊 بچه‌ها آیا نیازه من یه ویدئوی کوچولو بگیرم واسه‌ی طرز استفاده از همه‌ی این ‌apiها؟</h4>
<ul>
<li>✓ آره. بلد نیستم👍</li>
<li>✓ نه نیازی نیست. بلدم👎</li>
<li>✓ رهگذرم. دیدن نتایج👋</li>
</ul>
</div>
<div class="tg-text">برای اینکه در عمل انجام شده قرار بگیرم یه وبسایت بالا آوردم، فعلا هدفم اینه که API های رایگانی که بچه ها میذارنو با اسم خودشون اینجا رفرنس بدم.   خودم اینقدر بوکمارک و هایلایت چک کردم که کچل شدم  در ادامه میخوام چیزایی که یاد میگیرمو همینجا داکیومنت کنم و…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4095" target="_blank">📅 15:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4093">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OMNKmmHLIzLMR_5S-tUdL_ZCWmG9h89Mv0hKNLBeiLlFgdqPGLfYwdJDtB9hb4Hdn7n9vJhHXYUp50FAPpih1Z95VZtitEpxVOAC_B-vtQ8ny_tvP0o3momyyWKbpmia3SWPNo7AvQVWDZexF81bV_tcj34-y810m8rfT_djeEt6nFKHpQuQ3q_mt6-wH55-1fw14cQZmrHHVBeMXx9ciUHh3ip89VygEqKp78z3ZXg52B0R5lt0f5mHkomRHvTaJXXs8nNVGqtN09cQRkCnNd8AKlc3O-zm52J2a5UDWb2hgk_KeTwrhgV4WeSTQxX6OKVvg1UgfwCVuHcjzV8SxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hODCGTu_VXE1_Ra0484-OMavN97esrk05fYA8D5kfjuJZuacgVW-aeJeMfQkqzmz0LzxwpC9kQSKPxbF-lu_9aOOZjym5DbwJH1MBzkUoVg_4eZPpxBYCMlFeSP4oBlvNUHG8lsLuOvMSzqlk2xnNUXU1oJU4cUBy_IbiLWNafbzXiur6RcAj0ep1iy5gYcsEfegV35kEUyMMo-bE3yrbik8dCFcnOsFWPhoWjPwgWMYiU54KngEPRH7tVUZPF68lUWJbUz-6zVBjfDgRBYpiAALdlk9Rv10KKRqGM1rp3A7To3LY1WroOqgWnhV2C3tWaMugwa2jF0ro5-qlak1BQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اونوقت واسه بوفه خوابگاه ما تو یه روز 30 نفر کارت به کارت میکردن حسابش مسدود میشد به خاطر تعداد تراکنش</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4093" target="_blank">📅 15:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4092">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ov498EG0EwZ62wTVqL9RLdidCGwg7CvlczeaiMl6Q3JD5qphezFUuYWxfbGWOrDMrStd-ZgRGWdUG6Pkzt4WTYwF6d5BV8I_c59bKoCAGrOvmfd3H7kU8j7Wy3Rzyf5UJFMg2vyNnkHvCQVo07QeUQ4wwUtFgUGPiXmh3lau56F8QnK33ZozLPuU1O3RfnjFs2CsBmbNwOiKpNbyu5YvPQ5vf4ncm9GloPGJlb9vlZae4avVhoA0DdYUBIP2eUdbdzyZUBiqAh4ILZAi-wiDqQX9lnyuCHs3UrUejGwAJS2buYgrldZZD-uybVWupL-YcAziNycTdvOANkKXamX4TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اینکه در عمل انجام شده قرار بگیرم یه وبسایت بالا آوردم، فعلا هدفم اینه که API های رایگانی که بچه ها میذارنو با اسم خودشون اینجا رفرنس بدم.
خودم اینقدر بوکمارک و هایلایت چک کردم که کچل شدم
در ادامه میخوام چیزایی که یاد میگیرمو همینجا داکیومنت کنم و یه رفرنس خوبی درست بشه
این لینکش، big pickle هم برام درستش کرد دستش درد نکنه:
https://ez-ai-access.yazdan.me/
✍️
Yazdan Fathali</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4092" target="_blank">📅 14:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4091">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">به قول یکی از بچه‌ها انقدر api رایگان پیدا کردیم که حالا نمیدونیم باهاش چیکار کنیم
😂
چندتا نکته:
1- اصلا از api های رایگان روی پروژه‌های خصوصی یا حساستون استفاده نکنید
2- هیچ اطلاعات حساسی بهش ندید
3- توی env پروژه‌تون، api key یا... نذارید مخصوصا api پولی کلاد یا gpt یا چیزی
4- حواستون باشه که به جز شرکت‌های معتبر(مثل خود شیائومی که mimo رو رایگان میده یه مدت)، به هیچکدوم از بقیه‌ی سایت‌هایی که api رایگان میدن اعتبار و اعتمادی نیست</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4091" target="_blank">📅 14:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4090">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nat32fMhQn2IlvAZsqybVP6Pg6kojrX3ZWWs0lzhMqz2ZtRWOrHtIJiLIXl2wilyGYWJgX2nAvelNKwxCIKgFUQnJWCUCTXtsgfy3TRIe7EP_GZSKLDSAUlfuKb3g_4Bv2ZHU_FQ1NvQ-SDzRtrlA8PwS0BMD37vVozaAicitZnUcsQ0EF7kt5hG3Ti_S_uFXpaNjF0BqFs5vzoWXezxk8QCMLifGBe6uSLTJuO2y3EU5bM2kHUszFeEKEqkGlDUS-G6Fyl4FTYp986_Y_zNQMAP9QzJl3-QOUiMESylpTryEqC9DbLSGb85OHTcdy5PYLckrTNWE2Iiu9lcdJEzxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سایت بامزه پیدا کردم تمام اخبار جهان رو با ai رصد میکنه. اوپن سورس هم هستش
خبرای ایران و آمریکا رو هم می‌زنه درجا وقتی موشک میزنن و اینها
این پروژه‌اش:
https://github.com/koala73/worldmonitor
اینم سایتش:
https://worldmonitor.app/</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4090" target="_blank">📅 13:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4089">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">در مورد بن شدن اخیر اکانت‌های کلاد، باید بگم که من ساعت و همه چیم روی ایرانه(Asia/Tehran) و یه کله هم باهاش فارسی حرف میزنم و حتی از چت‌های قبلیمون که شرایط تحریم و اینها رو براش توضیح دادم، توی تصمیماتش قشنگ لحاظ میکنه "توی ایران بودن"ِ من رو. پس فکر می‌کنم…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4089" target="_blank">📅 11:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4088">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L8XPKMkn-CT1Nwp8R9aeozkXeBI49laYkqb1IG0GN8LLJ5MLrGffdjte_pUf_PeZ4M8MAtdX3qthVLKc18CNPdO_-BcDoWEZ5J6u1NyoW31tlGz9vKyk9_b2ZQ2SaqKTvoWzYsTCELnL2gUdjKrBla2vTZ7YKXTgxQiMxM-KqRwoTEgA4-f8JAQ_UF9hab1ydHpKIT6lM_appCLPviiO0sXzDD_EDxxkRS-0R7TcJyGt45aRLTLgXHApasYrJXovU3yd8CwoDr_uVmQtQpdof-LawtFdjnVmKNzdT3Fj_wWUXEG0NBsPLK1nuIVnbQvQQjtC_LwBt2Xl8nisG_EIuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد بن شدن اخیر اکانت‌های کلاد، باید بگم که من ساعت و همه چیم روی ایرانه(Asia/Tehran) و یه کله هم باهاش فارسی حرف میزنم و حتی از چت‌های قبلیمون که شرایط تحریم و اینها رو براش توضیح دادم، توی تصمیماتش قشنگ لحاظ میکنه "توی ایران بودن"ِ من رو. پس فکر می‌کنم علت بن شدن دسته‌ای اکانت‌ها، چیز دیگه‌ای باشه. نه فارسی حرف زدن یا ایران و... .
به نظرم مشکل یا کارتی که باهاش پرداخت شده هست(که شاید کارت‌هایی که batch payment داشتن رو تشخیص داده و اکانت‌ها رو بن کرده)
یا اینکه علت دیگه‌ای داره. چون خود خارجی‌ها هم باهاش درگیرن توی ساب‌ردیت‌ها</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4088" target="_blank">📅 10:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4087">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پیشرفت ai واقعا گاهی اوقات ترسناک به نظر می‌رسه، اما من به شخصه باور دارم که نه جای متخصصینِ واقعی رو قراره بگیره، نه قراره اتفاق بدی برای زندگیمون بیفته(به جز افزایش قیمت رم
🤣
)
در کل، نباید نسبت بهش گارد گرفت. نباید هم نسبت بهش پذیرای 100 درصد بود که "آره ai خداست هرچی بگه درسته"
مخصوصا توی برنامه‌نویسی خیلی خیلی جنگ و دعوا هست و می‌بینم که کسایی که به خودشون میگن وایب کدر و کسایی که به خودشون نمی‌گن وایب کدر، هر روز توی سر و کله‌ی همدیگه می‌زنن. که خب صحبت طولانی‌ایه؛ اما
نه اونی که می‌گه نباید از ai زیاد استفاده بشه اشتباه می‌کنه
نه اونی که می‌گه کلا همه چیز رو باید سپرد دست ai
چون این دوتا دارن راجب دوتا شرایط و چیز کاملا متفاوت صحبت می‌کنن. و این وسط یه سری سؤتفاهم‌های بزرگی پیش اومده و هر دو دسته پیش همدیگه منفور شدن.
به نظرم با گذشت زمان، خودش درست میشه
بازار، خودشو پیش می‌بره و پیدا می‌کنه
و در نهایت، کار هر دو دسته هم مشخص میشه.
الان همگی توی قطار پیشرفت ai هستیم و صدای همدیگه رو نمی‌شنویم:) بهتره صبر کنیم ببینیم کجا می‌ایسته، یا لااقل سرعتش کمی کمتر می‌شه، اون زمان میشه بحث و استدلال کرد دقیق</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/4087" target="_blank">📅 01:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4085">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یادش به خیر یه زمانی مد شده بود می‌گفتن Prompt Engineering کنید قبل از اینکه با ai حرف بزنید و یه سریا دوره برگزار کردن کلی فروختن</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4085" target="_blank">📅 00:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4084">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/npbr3mUO1hWBlKTakvvafZ1FixBCtTIem3sObHX36GTEgVIKvVz7CWax2DXRy7Jyr93hnjXmMxyEj9eKWCGHCwIgFHk3uUKyF7ipvQu4zQWOGIdr7OPNbzi4tz8bXscJMUCqoL48iIUDXICvNipdnGzq6WBN0zfwdlp9YF9wqzfAY9kq5ddF_-No0x3sUq1WBSoW5_b67S6cwLzNbbMixm7w_KrbCos9zSXiNycBXbbZcQbD6r8MNaJ3sIB3iCzEOMYE3T85WaFc7TNlNAGFb2zOxKq6YT7nfwE1-TA6z3TGyQwncaJTGm758uKghkjOK427lLySph8WCsKNJuCGog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید اعتراف کنم وقتایی که حوصله‌ام نمیشه یه ویدئوی یوتوب رو ببینم یا وقت ندارم، میدم
جمنای
واسم خلاصه‌اش کنه
👌
attention span در حال غرق شدن</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4084" target="_blank">📅 23:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4083">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">الان Zed Code رو به جای Vs Code و Cursor نصب کردم، و اولین چیزی که چشممو گرفت حجم کمش بود. کلا 80 مگابایت بود:) ستاپ اولیه‌ی بسیار تمیز. می‌تونید اکثر ایجنت‌های معروف رو نصب کنید و تنظیمات رو هم از Cursor یا Vs Code ایمپورت کنید. تمام اسکتنشن‌هاشون رو هم می‌تونید…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/4083" target="_blank">📅 23:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4080">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IIlrU6kYDbTpVIadEutnobrEo7XOluQIRnmnljf3wsfoc4iGMjq1zzju_Dr1K-ClRB464oW3M3E89OKq7PocQJ5wCmHHFyCrDxfEeJShhVH431bscfLoogc-sUG93oUK6Bz-pG18VGu07GLloTLIYIqp6Cb440aCV4hSrmUCTtYy8_0Xvg5TekWzAM3EysxVtdokMnBn_TDO1h07YXvtWZdbl4L2NFa0glqsIP2pA9tvwSrYffOlkP_gUiRyCVzdK1abMXYzEWXA1jXCuLFCdhnzUOs6WUEn1K0quIf50Hc2ZqTPSkZhkzkuu1OXVhwhMsYkreSPh5nSMTiqmiX3AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kBBcRblc8JTWLdWjSNJjInRwPZYYJSdeMgEjq2QpvEQopWEfwJS28an_8m_WCK63rhJ1bygEyvTUa0rhKsxA5tmt_oHEhfJliC5utaoGz-tU6hsXGO4Q9jI5V1NILYIOQPCy1DPgI42X5d5C4oLtD9dT1j_1LlLIjISh2o8g9MkCOAK0DEAv96sEyU4O0ovqTTeDW_F33L6iEZijaI7RD9gWv_5ANNGifWIloSghiqq1JOEyX-btsz5kuM8Z-qUIIYSoSgYRwTYHTAkTBRWEl00DROWWuNi2oSVf-IoWrwA2G0MdjdJ65J0sMYJ1KeMPm6Hkqnl1IzoVZnuplBGw8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fS0JZvolOI_aVxgOKFxpL4Bst_C3vJJIy6INKsOnXdu29gmYpHn7ZzIRuFgV_bIDU-VPaH30v3QiQn2d18mBELLOVqGgrLRee9OJvVrExyHLMF5fvoYGYYklYrVYRAZD7nLPltcS27lu6DjDdZgZa0cUXbkg5BfX9cNn0fzIvf6vkGYpgQAzNl9DSnyz_tMytdM-TbKGEV24mSyQiiqUdnvwDncH_srs5hztPf16LO4tbiyI5QWoxBcgdMtFskXa18MMhY08nrAEJmFw6QKfxmbnJHYMl14z57YPf88jVvaQNSPAd7695wpLJp9WpbXsOoP3dbGmVJrafy4dr3wMag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الان Zed Code رو به جای Vs Code و Cursor نصب کردم، و اولین چیزی که چشممو گرفت حجم کمش بود. کلا 80 مگابایت بود:)
ستاپ اولیه‌ی بسیار تمیز. می‌تونید اکثر ایجنت‌های معروف رو نصب کنید و تنظیمات رو هم از Cursor یا Vs Code ایمپورت کنید. تمام اسکتنشن‌هاشون رو هم می‌تونید نصب کنید طبیعتا
محیط داحلش هم عاری از هر گونه حواس‌پرتی و به شدت سبکه. به سرعت تب Git رو بالا میاره و تا اینجا عالی بوده</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/4080" target="_blank">📅 22:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4079">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اپل تقریبا ۱۷-۱۸ درصد قیمت محصولاتش رو افزایش داده، اونوقت فروشگاه‌های وطنم نه تنها قیمت رو ۳۵-۴۰ درصد کشیدن بالا، بلکه سفارش در جریان تمام مشتری‌ها رو هم لغو کردن تا مجبور بشن برای قیمت جدید پول بدن. بله ایران درست خواهد شد
✉️</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4079" target="_blank">📅 21:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4078">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rd8ClEsbkp2Euu3h2z-wzrUL3bApL4fqOJdNyhyft_Z6kdI7K-ysWBujvN7PGpgzLVrazd7pFAWCXmQZEoJfgmD-yMuEcRartS-7DUf21tqMqSk0e2bzvdJXIxQyDltYSJLFkToLQp2PxrfdQVYpihlhz-06JWJAPwTzeLShyJ0BaH6om0Hro397pHurnbR6KEaTykyGM0jmRSN38OLKuBpmJ8fk54XcPGEFKr_Az4HVW8YbRw3W61bFcqMoTsL2NX4PzsnVY58ce8Xx5Y5O0zVwt51PQjDpO_EGg_137D91LMp4V8NUoTGuuSSXalwniN-qUk_fEwSN2SkkDv3CkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نفر توی ردیت، مدل GLM 5.2 رو روی سیستم خودش راه انداخته با ۴ تا RTX 3090 و 192 گیگ رم
😂
وزن Q2 مدل رو هم ران کرده که توضیح میدم چیه. همینطور با اینکه تقریبا از بیس‌ترینش استفاده کرده، گفته که GLM 5.2 داره کار کدنویسی و پلن و هرچی که نیاز دارم رو عالی انجام میده.
تأکید کرده که مدل توی کد زدن، پروسه‌نویسی و حتی کارهای طولانی و autonomous خیلی قوی عمل می‌کنه. و واقعا حس Frontier Model می‌ده.
حالا Q2 یعنی چی؟
حرف Q مخفف Quantization (کوانتایز) هست. یعنی وزن‌های مدل رو از دقت بالا (معمولاً ۱۶ بیت) به دقت خیلی پایین‌تر کاهش دادن تا:
حجم فایل خیلی کوچک‌تر بشه
حافظه (VRAM/RAM) خیلی کمتر مصرف کنه
سریع‌تر اجرا بشه
Q2 یعنی مدل به ۲ بیت کوانتایز شده.
این پایین‌ترین سطح کوانتایز رایج هست (از Q2 تا Q8 و حتی Q1 وجود داره).
همینطور طبق گفته‌ی خودش برقش هم خورشیدیه و هزینه‌ی برق نمیده
🔋
مشخصات سیستمش هم اینه:
۴ تا RTX 3090 (هر کدوم ۲۴ گیگ) که میشه ۹۶ گیگ VRAM
سی‌پی‌یو هم Ryzen 9 9900X
۱۹۲ گیگ رم DDR5 (Overclock شده روی ۵۶۰۰ مگاهرتز)
مادربرد MSI 840B (هرچند بهش گفتن برای این ستاپ ایدئال نیست، ولی خودش جواب داده که فعلا داره جواب می‌ده
😂
)
ایشالا قسمت ما هم بشه
پست اصلی:
https://www.reddit.com/r/ZaiGLM/s/Ew9JHC2XIA
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4078" target="_blank">📅 21:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4077">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fEs9Weqpjq-f1C_jGa0-nSL0EguPrEoPQ3I2FzAQvDgOWZ8-eoKcO0ycLdrmAaWsZA1lxWWf027_v2EXOIxvmr0TxMdbDme0SZveuE5pfWrXkHILCUD1W8dka3LvRDQeMxZzLga-h94s9neDt6IEv2zWQvkLiv6XIp3OY8O55DkBboGISxhU0QM9TuU78dG-5igYSXfK2xHiegMKlPFoF_kUxaaWH2du32TmjjULou4oJt4_UABgbw2yOueneq2dgxxhRqQcukD8DDmfJu22aItIyMV41KXkmSYITWCPFHdk7zmb7RXfuueoxf2SBa5FnwnapxwOQxSlgdaCeZpbpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده. به شدت هم IDE سبک و خوبیه از اینجا می‌تونید اقدام کنید:…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4077" target="_blank">📅 18:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4076">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l5-3a3shTAglZ9k48gs6KYQcbM7UC3d-U_I8a1d9jWq_ljvDnUNHnHPWLMCXc2vhL-D9tdM3EzhHCSClOIDgBDP41nYKZcDinGbbft3J-KTZ39GTpQHMbdcS3wMinqIyR6oeR0facqvX9DhbAkBI8B8fRgb7jkn3Id8NxRa-3qsZ2MYzO94hAxKYwTYXWy68VFUB4WU1SeWyJby89N4JBpPAv2g8n55okEbz32juVI3vZ9RYtQAYjZPiX6Mb-t_MzHvl5RY5o87o3ublkOcyH3xVVx4T4neiVIOpHLCrFbuB_qB-0l1uW8GQHrIqXZdFLKbnPj_Wj48t6I0i__5xyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده.
به شدت هم IDE سبک و خوبیه
از اینجا می‌تونید اقدام کنید:
https://zed.dev/education</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/MatinSenPaii/4076" target="_blank">📅 18:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4075">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/38b0a3b6de.webm?token=ZcFli2OSprxTzA8TgPPR_qBx8XAdFWaIQcVu4IICIFUbVqYoxVGI6jZISVGhC0uLDJrQqjcAnsYjtVEB67zFMPnNS7i5x9v9TNRQPySKAIMJpCGnvXyo5eUIUl44QI1rWZJcLRqx2bAXPGgwKVQ0pgCf6r09x-eX8w4ql7mLpo21CQdtCOq0HaALSuLaNrc-YFMykhJWoJPUrsDS8zIVCSOwo2bGQSvR9wfco3YAb-k84u1jPWLnwi76CRbmytCC-KMkvP7Uz9rGHKks-nogye61rBNWae6P7F3RCBvftBqH28AeeOm9IyylMoig8ofURznWoB5gLTaXZuUDMwyKfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/38b0a3b6de.webm?token=ZcFli2OSprxTzA8TgPPR_qBx8XAdFWaIQcVu4IICIFUbVqYoxVGI6jZISVGhC0uLDJrQqjcAnsYjtVEB67zFMPnNS7i5x9v9TNRQPySKAIMJpCGnvXyo5eUIUl44QI1rWZJcLRqx2bAXPGgwKVQ0pgCf6r09x-eX8w4ql7mLpo21CQdtCOq0HaALSuLaNrc-YFMykhJWoJPUrsDS8zIVCSOwo2bGQSvR9wfco3YAb-k84u1jPWLnwi76CRbmytCC-KMkvP7Uz9rGHKks-nogye61rBNWae6P7F3RCBvftBqH28AeeOm9IyylMoig8ofURznWoB5gLTaXZuUDMwyKfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/4075" target="_blank">📅 16:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4074">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دو ساعت برق رفت، گند خورد وسط کارام و تمرکزم و همه‌چی</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4074" target="_blank">📅 16:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4073">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/4073" target="_blank">📅 16:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4072">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lC4FD8xC8RqtCECB90uShpzdBaGedck7UXPmaRS7wU0X3Dxi-SFwNN57T0_pjyHQ2xCYpJ-UAhj9Bid7uvizngCi0Q9Wt3eC5IwcYFiK5uA_KlF1uM-g1dI8MMic3EvcS5zY8sKaJD-F9nidyLjElgiD6hYkWLLViCi6R9pTtHjujNFdQZMcTlRiG7Zf4Psu0so1YAxwnu3XXPNz-ZBS954R4hnAig_mdtmcHsQuQZw_FZV5xEq5VIJNoDHdXYdn4rf4O6YQOJco6i1bSvt9PuOqWoQu162kVL4grrDFPQUueOQkCltl8ZBnVx2kzQyCwpPUz-cTQTB-dnmMHeawmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس دیگه منتظرت نمی‌مونه — خودش یاد می‌گیره!
📱
قابلیت جدیدی که Hermes Agent اخیرا اضافه کرده، دستور  /learn  هست. به‌جای اینکه بشینید دستی یه SKILL.md بنویسید، یا خودش صرفا کورکورانه بنویسه و شما ندونید چه خبره، حالا می‌تونید فقط منابع رو نشونش بدید و خودش…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/4072" target="_blank">📅 13:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4071">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fKxsGbxzHVJmiP2hhTbNnl6mKeP6UE8b6phm2fF5mpshE_rKAG7CWswd-G2dy4gHordzXvYzsY1nPySoYScnr8ay7N1tvNC_nNK6wJdoB0WzJWM09RMAfDr0ZIzvslycDUOFSv_AtDu9Sbc48TwANw-Ruk1kXccanJ8_Q22io6ae8cDjkbOISLwh4f0YqLZcTctUqPJVJevGtN3y0juw03vl2LjmEexk5GB_OMZerSMvt9kal5Ohuo4kx4HqeR94Ag45yl7zSD1Oaj3799ieChJDC33CQyIWeTix8lHu2uZX-A1eNZ1252EPwfg-shc6mYxmFUvcG1_ZxY_-oR5hbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس دیگه منتظرت نمی‌مونه — خودش یاد می‌گیره!
📱
قابلیت جدیدی که Hermes Agent اخیرا اضافه کرده، دستور
/learn
هست.
به‌جای اینکه بشینید دستی یه
SKILL.md
بنویسید، یا خودش صرفا کورکورانه بنویسه و شما ندونید چه خبره، حالا می‌تونید فقط منابع رو نشونش بدید و خودش بقیه‌ش رو انجام بده.
🗃️
وقتی دستور /learn رو می‌زنید، ایجنت با ابزارهای خودش (read_file، search_files، web_extract) منبع رو می‌خونه، یه skill استاندارد می‌سازه و ذخیره می‌کنه — و روی همه‌جا یکسان کار می‌کنه.
چند تا مثال که بهتر متوجه بشید:
۱- /learn the auth flow in ~/projects/backend
کل منطق احراز هویت پروژه‌تون رو یاد می‌گیره؛ دفعه‌ی بعد برای پروژه‌ی بعدی، فقط صداش می‌زنید.
📞
۲- /learn
https://docs.someapi.com
مستندات یه API رو می‌بلعه و تبدیلش می‌کنه به یه مهارتِ آماده. مثلا من خودم سر API تلگرام و اینکه هی آپدیت میده و ai ها رسما نادون میشن سرش، این قضیه خیلی به دردم خورد
💻
۳- /learn my writing style at
https://example.blog.com
استایل نوشتن خودتون رو بهش یاد می‌دید که من روی این می‌خوام یه کم مانور بدم و قشنگ تستش کنم و نتیجه رو بهتون می‌گم:)
📚
🌍
نکته‌های باحالش:
• مهارت‌ها توی ~/.hermes/skills/ ذخیره و persistent می‌شن
• بارگذاری سه‌سطحیه؛ محتوای کامل skill فقط وقتی نیاز باشه لود می‌شه — توکن الکی نمی‌سوزه
• و اما مهم‌ترینش از نظر من: نمی‌خوای کورکورانه بنویسه؟ با write_approval: true توی تنظیماتش، هر skill رو قبل از ذخیره خودت تأیید کن! کنترل کامل=)
🛡
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4071" target="_blank">📅 12:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4070">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">از اینجا ببینید آموزش WhiteDNS VPN رو به همراه آموزش اسکنر اندروید من که پدی زحمتش رو کشید:
https://t.me/MatinSenPaii/3999</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4070" target="_blank">📅 10:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4069">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">↗️
تعداد کانکشن ها موفق WhiteDNS VPN به ۱۰،۰۰۰ کانکشن روزانه رسیده .
✍️
در حال حاظر تمرکز اصلی ما روی اضافه کردن وی‌پی‌ان به نسخه ورژن ویندوز، مک و لینوکس هستش.
✍️
مواردی گزارش DNS Leak توی کانکشن‌ها داشتیم. درحال آماده کردن سیستمی هستیم که علاوه بر تست‌های سرعت، امنیت و پایداری، تست DNS Leak  هم از کانفیگ ها گرفته بشه.
ممنون از همگی
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/4069" target="_blank">📅 10:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4068">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خب، من با کمک Hermes و API رایگان MiMo Pro 2.5 و API رایگان جمنای، تونستم یه ربات باحال بنویسم!  توی لپ تاپم کلیک میکنم روی یه اسکریپت .bat ، و رباتی که با mimo نوشتم، فید چندتا سایت اخبار ai که به صلاح‌دید خودش معتبر بودن و زرد نبودن رو، می‌خونه، با Gemini…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4068" target="_blank">📅 03:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4067">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WVEd_y2pp9_3i4lCOs4WyEwO5FQNei8pzOKJSaGOUec8xjhU7eLUt1NKzH_y2DN4ki8lo0eKXhfG0hptiKTUn4QS1Z2RUZe2G4s8UaHLAwYktGAQo8hao5NLV1ArVT89PlvbReL6huAs-IYlaiG94AQmdKemEOf-aCAfpNLvSt1GmFsN3rKYS94gwtEpoZMYRsQCRAUtJI7oAyNI4Rgx9CqwjJz5Mn4oBO61HUrqzcXbj3blqg9CLt87ICTqtrGojapvNWxWFC0wwxUy6qaFaLvZhaczC55WhmeScM8YLVzKCJawBbTcS6EJgxtR4hMs_KuFoDvvRFJlnH0jLMrffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا اگر از اسکنر من استفاده می‌کنید و مطمئن هستید که آیپیتون تمیزه، حتما تیک همه‌ی پورت‌ها رو بزنید برای اسکن. چون به چشم دارم میبینم یه سری آیپی تمیزها فقط روی یه سری پورت‌های خاص کار می‌کنن
آموزش اسکنر و اتصال رایگان به اینترنت ازاد با سیستم(ویندوز-مک-لینوکس):
https://youtu.be/JdNeZnclS-s
آموزش با گوشی اندروید:
https://www.youtube.com/watch?v=2otJfXgNWCM&t=70s</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4067" target="_blank">📅 03:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4066">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ai-news-bot-MatinSenPaii.zip</div>
  <div class="tg-doc-extra">50.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4066" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1- باید فایل .bat رو ادیت کنید و مسیر پوشه‌ی خودتون رو از فایل پایتون بهش بدید
2- من با venv و همه چیز گذاشتم که دردسر نصب یا ... نکشید
3- توی config.json هم باید api جمنای و توکن BotFather و آیدی عددی خودتون رو قرار بدید. توی این ویدئو اینها رو یاد دادم که چه شکلی بگیرید:
https://www.youtube.com/watch?v=7qYPK3dGoK4</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4066" target="_blank">📅 02:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4062">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qDA_2mv4R-a-3QeOyECgaerdpcLDcLIFrUFr6l0V3DFoAKfus-d335hdkK-m_ZZqgebx6p0g5Yr286ZQfkwMGlUkcVkjGW5BKbxaNHOwWkMQLXLxR4Znn3hA8-4hGPcd3nJg2cvfE-v1wTPbs2jW_gLfeLe-UHKjml-wqxslWrJrrdoYpWEuZ36pydQ_IW0MoHJRGkJKrlusfXLI3uX-3p5dbs_0pQcdM_5GNibT0pK3r2gVBqsnNLDJdZrDYvWxV3nm5nuWJEHb_APi8oQTSaClNmmYBzD8PLdWiqAlJt56HI_vQ8JDuLiY4U0Z4TWwY3GM4El_Bb5cZuSlRPgCGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mJfOYblzl1gMtcV90Nji2wM8dHfcfaEcTu_JO9gXZIWoKZR_7RauNRw7sjHt-KKqrNpkId79MluR5bAD43jAV6gclecWhBAIu_-RO7xo6GYVb5176R3i6c7XwzNZwHraYM7hGuW99TTZYhQ2g9oQSBSVZZ-9PR4PyV7yvVGKOK5h0DCHfqTyAVWaPQgBl59EJF7U6QbTpHmH8tus__z3AIve6WhYpqzKFQm8UncokOnLlh0C9V8kiBHlnlwWnMJ7U0uT29gTXSTVpJT3o4hHAeogcwrGe2L5YQgUxiJEsrGvtEv5uePsBCuIgzvW1xJHv_gDq9uuJbVYYVyPsNTWtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Fj-yzFYTgolXLaH-U7-3Uf7et0Jf0crlUJ0dxu6ZWbdEtGETW7mkBh2q0RQMXFdD866LI757Rzyu_BsyVvm37Ax37qiSi5mhN0KNK7fGl3cGsyZ2SwsTjwrkUwqVVfbM3aHfBYI3BfgrFHrka7pUs34cYdIxvM8XsRLi6G20jgusK74SRLwXPsFVkF5o213xm8GHZZBjBf841LJyc6JIT-HKV9jWnjBFaHU-WuYnlYw2rz20Jc26t6-bGGSccAiBnEpNJms-YZ70vxfgBrvXKYb0rOsVgEBkfbBKZrey2IJSyKncMZAUHpC-AWq4OuVMMyawHqqVMj09SDHMeLijow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rRUXRa-77JFRFCQF4_wspev7XW9VmxUNI7nh8uEy9L-OZzQUrM4NB6xFRtQ5T-23oPMolmTTNDVwMAbZhZkCVoaR9a6g6Sh7rTiwaNDbLSbrBYnZg7JOV6gJEK1whPxEW31RZFuntsf34UU7vuIlp76iVwE8PAMdrU5uzqiVNhU5hbDAPS5uvhZHUoEXtWSD3kxV2zwaPlVHwyofUkc0SOu-k-e9e6Ypw7UfJgqQwmeNVsztyJIbAYcckSAf50s8DnARs55Wawxayy0dVHhvkwomcrLfTuobZT4lESOBlXVBuRud9WY62tqWf476iQXMbWhBauMozJvkSglaudmZ6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب، من با کمک Hermes و API رایگان MiMo Pro 2.5 و API رایگان جمنای، تونستم یه ربات باحال بنویسم!
توی لپ تاپم کلیک میکنم روی یه اسکریپت .bat ، و رباتی که با mimo نوشتم، فید چندتا سایت اخبار ai که به صلاح‌دید خودش معتبر بودن و زرد نبودن رو، می‌خونه، با Gemini 3.5 flash lite ترجمه‌ی روون می‌کنه به فارسی، و توی ربات تلگرامم می‌فرسته پیوی من. که خب کار ساده‌ایه و بهتون ایده میدم چه شکلی می‌تونید پیچیده‌ترش هم بکنید!
الان، شروع می‌کنم فرآیندی که این اسکریپت خیلی ساده رو ساختم، بهتون توضیح می‌دم.
1- اولین کار، گرفتن API ها بود. از Nara Router تونستم 7 میلیون توکن رایگان روزانه بگیرم که اینجا گفتم چه شکلی:
https://t.me/MatinSenPaii/4061
و همینطور از
https://aistudio.google.com
هم یه api رایگان جمنای گرفتم. که مدلهای دیگه‌اش به درد نمیخورن از لحاظ لیمیت، ولی مدل Gemini 3.1 flash lite واقعا توی لیمیت‌ها خداست. 500 تا ریکوئست روزانه و 250 کا توکن که اصلا پر نمیشه. برای ترجمه عالیه. اما برای خود Hermes مناسب نیستش چون که TPM بالایی مصرف می‌کنه و Exceed میشه.
2- توی Hermes، از قسمت مدل‌ها،  Nara رو اضافه کردم. خودش اتوماتیک تشخیص داد و گفت کدوم مدلش رو می‌خوای؟ گفتم mimo pro 2.5(که در حال حاضر رایگانه توی Nara اما خب واقعا توکن مصرفیش هم بد نبود برای تسک من).
3- وارد چت Hermes شدم، و چیزی که می‌خواستم رو بهش گفتم. گفتم که می‌خوام یه ربات تلگرام بنویسی که هر بار رانش می‌کنم، آخرین اخبار ai رو با api جمنای بگیره، و حتما از مدل gemini-3.1-flash-lite استفاده کنه و عینا همین.(اگر نگید دقیقا یهو میره مدل 2.0 رو میذاره بدبخت میشید) و برام بفرسته.
5- سری اول ربات رو ساخت، و بعدش بهش گفتم یه سری قابلیت اضافه کنه. مثلا زمانش رو بگه که چقدر وقت پیش بوده یا فرمت بندی رو درست کنه. همینطور گفتم که برام یه اسکریپت ویندوزی بنویسه که هر بار کلیک کردم روش، این رو ران کنه( این شکلی راحتترم خودم)
6- همونطور که توی تصویر می‌بینید، خیلی تمیز برداشت خبر GPT 5.6 که واقعا هم سه ساعت پیش اومده بود رو پوشش داد، همینطور خبر های دیگه که یکی از نیازهای روزمره‌ی من رو برطرف کرد تا حدی. که یه دید کلی نسبت به اخبار ai روز داشته باشم. سورس کدش رو هم براتون پست می‌کنم که اگر دوست داشتید، تست کنید. هرچند چیز خاصی نیست؛ خودتون می‌تونید بهترش رو بنویسید
7- چطوری می‌تونید بیشتر درگیرش بشید؟
بیاید با همین "بات جمع‌آوری اخبار مربوط به ai" مثال بزنم.
شما می‌تونید این رو روی یه سرور لینوکسی ران کنید که 24/7 ران باشه و هر خبر جدیدی اومد، درجا بفرسته واستون. یا حتی ببریدش روی worker کلودفلر. و هر یه ساعت یه بار چک کنه، اگر خبر جدیدی اومده باشه واستون بفرسته
همینطور می‌تونید یه سیستم پست‌ساز نیمه خودکار بسازید برای تلگرام و بدید که پست بسازه برای چنلتون(و این وسط توسط خودتون یا یه agent هوش مصنوعی دیگه review بشه!)
خلاصه که راه برای درگیر شدن باهاش زیاده. کمی تایم بذارید، و کار با این ابزارهای جدید رو یاد بگیرید. من هم خودم اول یادگیری هستم طبیعتا:)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4062" target="_blank">📅 02:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4061">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u9TPfIu-nnjT1dsuZEQEZ83-RNADC85tQ72I7JnVOm2EzzFFK7kYDc4lYzSdkxruQ3iOHs-R8AuPiVTSFQ8t1fGWrsIFplItA_twfKWuNU9wO1AWYTzmAM-vTUMPOiWj0oqj93auL1qCU0Mgeth65UG05czuWeKgsGaVw5nLsQRf0NmZd9i5HVNTQb4lG4obfUEjBI_5jc4XDoINcELNcE_xNxrSgkwCI9Q4Sg3usdySjz6je32B_zYnh3-DZjAMaCQqHrdC2MEMOdKfdgy-ljpLqi9eHa6m1vkZrfYRTWpSDbWD3SIxQQDownFrIKwo_vSYA_6RadmD4oTl553Byw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه!
یه ربات خیلی کوچولو هم دارم می‌نویسم.
دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes
خوبی این سایته هم اینه که روزی 7 میلیون توکن رایگان از Mistral و MiMo Pro 2.5 میده و هر روز دوباره شارژ میشه. نوع API هم open-ai compatible هست. اینها رو بعدا توضیح میدم برای دوستانی که متوجه نمی‌شن پس نگران نباشید
از این لینک هم می‌تونید ثبت نام کنید داخلش:
https://router.bynara.id/register?ref=PJ6RZMDB
رفرالش هم چیز خاصی نداره فکر کنم، صرفا اگر بعدا خواستید شارژ کنید، وقتی با رفرال وارد شده باشید، توکن رایگان اضافه می‌گیرید</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4061" target="_blank">📅 01:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4060">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مدل پرچم‌دار GPT-5.6 Sol برای برنامه‌نویسی، امنیت سایبری و اجرای ایجنت‌های هوش مصنوعی بهینه شده و از قابلیت‌های جدیدی مانند «استدلال عمیق» و استفاده از چند ایجنت تخصصی برای حل مسائل پیچیده بهره می‌برد.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4060" target="_blank">📅 00:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4059">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">به قول یکی از بچه‌ها یه چرت می‌زنیم بیدار میشیم می‌بینیم ده تا هوش مصنوعی api رایگان دادن
😂
چون خیلی حجم مطالب زیاد شد این دو روز
به زودی دسته‌بندی می‌کنم و می‌ذارم
همینطور بهترین‌هاش رو(که زود گذر نیستن) ویدئو می‌کنم و یاد میدم</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4059" target="_blank">📅 00:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4058">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اگر مثل TTS اش بهش چندین تا لحن و دوبلور اضافه کنه هم عالی میشه. که اتوماتیک تشخیص بده و صدای دوبلور زن و مرد رو تفکیک کنه. که در ادامه به نظرم این کار رو انجام خواهد داد چون همین الانش هم برای بخش پادکست، اضافه‌اش کرده</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4058" target="_blank">📅 21:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4057">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">همین الان مدل رایگان Gemini Live Translate 3.5 رو روی یه ویدئوی یوتوب امتحان کردم و نتیجه خارق‌العاده بود! همزمان که صحبت می‌کنه، مثل مستندهای راز بقا(
😂
) دوبله میکنه و میگه و مینویسه تمام متن رو بدون اشکال تقریبا. دو سه ثانیه Delay داره، اما دقیق ترجمه می‌کنه…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4057" target="_blank">📅 21:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4056">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf6c81864a.mp4?token=na2rzal7di_MWyJOwFHPM3nmfODzr0ERD-4FG0dbGbh3PB8qv3oip_FlvA66OSeHoK5u8kIqPNXKQSfhHyzBx1z289GuwDzuT6nO-R8MB3XARSUL9tmnYPgc1j9WaFetkcx6PaPSP7ORfXd0a46DEWWf4qOePWGwH-EvFdMoa1TTyZgOA_wvWKIXJ7BpfSLJ2uPnxqB9itnK0fYw_R6X48GFzThpgpkqKHqoK4EGs8mYj4Pn6L65nV4Rt1-_d1auOblT3Rj7fmpZhgrUrenc3OSueVmuZsbZS0TuRkHtX7rhflxcuKRnvYeTZhHlWWJc9k_pk3gcJ6jUgNufq7kYt5w2SdWtMKKiM57NKMd99i4h_8t7hHI8LfS9fZcXy_BhczbfxNH2_JZPbVbCNGf1yQZ2zvPddYVAoPA0w1BrKBruptYC6CEESK_LPQisEmY5kz-0tmj6977tI1w4KKP3C3ST9zY76zQkGHktfFq_s0U5EwZ5u8O06b3ZVfI0-w5HBKlXRldPrxrSjNDi1tcJX_2IDAEAqyXp7JR3fxfM01MlTbTEYRzbEJHiiG0JVWUFjmDFTjNgU6-Be6HMHnbEh4FCtzMBMwjO6Dc1TRhmmUUvJRmeYM1JD9J8tYoEHwaTX_-3mbUEbCk5EsdA9Drix1wbz0-yVLSs1DMMYBtanew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf6c81864a.mp4?token=na2rzal7di_MWyJOwFHPM3nmfODzr0ERD-4FG0dbGbh3PB8qv3oip_FlvA66OSeHoK5u8kIqPNXKQSfhHyzBx1z289GuwDzuT6nO-R8MB3XARSUL9tmnYPgc1j9WaFetkcx6PaPSP7ORfXd0a46DEWWf4qOePWGwH-EvFdMoa1TTyZgOA_wvWKIXJ7BpfSLJ2uPnxqB9itnK0fYw_R6X48GFzThpgpkqKHqoK4EGs8mYj4Pn6L65nV4Rt1-_d1auOblT3Rj7fmpZhgrUrenc3OSueVmuZsbZS0TuRkHtX7rhflxcuKRnvYeTZhHlWWJc9k_pk3gcJ6jUgNufq7kYt5w2SdWtMKKiM57NKMd99i4h_8t7hHI8LfS9fZcXy_BhczbfxNH2_JZPbVbCNGf1yQZ2zvPddYVAoPA0w1BrKBruptYC6CEESK_LPQisEmY5kz-0tmj6977tI1w4KKP3C3ST9zY76zQkGHktfFq_s0U5EwZ5u8O06b3ZVfI0-w5HBKlXRldPrxrSjNDi1tcJX_2IDAEAqyXp7JR3fxfM01MlTbTEYRzbEJHiiG0JVWUFjmDFTjNgU6-Be6HMHnbEh4FCtzMBMwjO6Dc1TRhmmUUvJRmeYM1JD9J8tYoEHwaTX_-3mbUEbCk5EsdA9Drix1wbz0-yVLSs1DMMYBtanew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین الان مدل رایگان Gemini Live Translate 3.5 رو روی یه ویدئوی یوتوب امتحان کردم و نتیجه خارق‌العاده بود!
همزمان که صحبت می‌کنه، مثل مستندهای راز بقا(
😂
) دوبله میکنه و میگه و مینویسه تمام متن رو بدون اشکال تقریبا.
دو سه ثانیه Delay داره، اما دقیق ترجمه می‌کنه و خیلی جذاب بود حقیقتا. مخصوصا وقتی که بخواید با یه نفر که به زبان شما حرف نمی‌زنه، میت داشته باشید
از اینجا می‌تونید استفاده کنید:
https://aistudio.google.com/live?model=gemini-3.5-live-translate-preview</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/MatinSenPaii/4056" target="_blank">📅 21:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4055">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⚡
اگر برنامه‌نویس نیستید، API Key را بگیرید و بدون نیاز به ثبت‌نام وارد سایت زیر شوید:
https://B2n.ir/newapi
آدرس سرویس و کلید را وارد کنید و از مدل‌ها استفاده کنید.</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4055" target="_blank">📅 20:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4050">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کنار iran internet monitor باید یه کانال بالا بیاریم iran bank monitor که وضعیت بانکا رو رصد کنه
بانک ملی درست شده بود باز قطع شد</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/4050" target="_blank">📅 15:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4049">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XrUM28TFolUxriUwgNsgueVNlQ8dQID6xD3sXAKjzlZGMJaC5sMvM2JdDgQ8CFcH2LmqYxUsxMTsl-aPaffsSOu8nXK-GseJeHwbkanSMtHtG8gzaUhoAuWZB6kd5pcajhE6NIMPWZoULFhiixR1sCVMdAa61tfN2KSyCYXdNsFVKqJbjtH54iO2NLzVY11H3TTa2tbBB_1ngyhmBWj7ACaM4k2xXVgCa91sE5NDxTM0g4ahoc1QdOqdGkHjA7kuz53wpYdAwxzcqaU6VUpZD80_e4zWQt0KOJCcgLhXGN8SJvnKM9esGoxt_NrULjo0ub8R9jd65qhOZNgUrpxOgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویکی تجربه یکی از معدود گروه‌هایی بود که بدون هیچ وابستگی و فاند و رانتی، محیطی رو فراهم کرده بود که افراد نظر واقعیشون رو راجب شرکت‌های ایرانی بگن و نظر بدن.
سر همین خیلی از شرکت‌ها می‌گفتن که کامنت‌هایی که راجب ما گذاشتن رو پاک کن وگرنه شکایت می‌کنیم و فلانت می‌کنیم و... یا حتی می‌گفتن بهت پول میدیم، اما قبول نمی‌کرد.
و همینطور یکی از عواملی بودش که باعث شد آموزش‌های من به دست خیلیها برسن، چون همیشه مطالب رو share میکرد و با وجود هزینه‌های سرسام آور سرورهاش و شرایط سخت مالی، توی قطعی نت کنارمون بود.
و آخرین پست کانال تلگرامشون توی
تاریخ ۲۷ مارچ
(۹۰ روز پیش و اواسط جنگ) بود و همه نگران بودیم که نکنه اتفاقی واسه‌ی مالکش افتاده باشه یا دستگیر شده باشه.
و نتونسته دامنه
https://tajrobe.wiki
رو تمدید کنه. امروز دیدم که دامنه‌ی ویکی تجربه توسط ابرناک گرفته شده(احتمالا یکی از شرکت‌هایی که تهدیدش می‌کرد). و در عجبم از اینهمه بی‌شرفی، که میراث شخصی رو که مشخص نیست مرده یا زنده‌ست یا دستگیر شده یا... رو برداشته و اسم تمام اون پلتفرم رو گذاشته انتقام‌گیری.
امیدوارم که حال ویکی تجربه خوب باشه. دامنه و اینها کمترین اهمیت رو داره</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/MatinSenPaii/4049" target="_blank">📅 14:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4048">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/db2tNqxKd99kF7FDoaO26O3Ba1V9FxNUPycu-6x5lTO2xf2OqhA0LVgdpAbxpQo25Z9t_0DDM39TBGB-msUp3xNQ0Bk3KHz_jjGhXCfCmDbquGx9ISszDsmIvajHDIgSSR2luZZDYQ1M-3EhgLmOsSYG-6LdWB81hfPn5UNJAYn4-tkeWe6C6MOgY66ebf0NyLrx61jnLc7B4QRhZszKL4S2STwqJaC3n9sI2lfvNHjo8o7oZ9pRgHv4sDO-Xx2Eg7jlfRwE6iVr5FWWRDifZd3fwJtDFDdQwBEMRBa1Nn20cDKsn2vOS9OQZ4A6xRjnTkUVOfVryHamLj6DEOI3ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نزنید این حرف رو بچه‌ها. شما چیزی به من مدیون نیستید
❤️
همه‌اش لطفتونه
و ممنونم ازتون</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4048" target="_blank">📅 14:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4047">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Dastamo Begir</div>
  <div class="tg-doc-extra">MEZZO</div>
</div>
<a href="https://t.me/MatinSenPaii/4047" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4047" target="_blank">📅 14:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4046">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">این نت دیتاسنترا کی می‌خواد مثل آدم وصل بشه من نمی‌دونم.
فکر کنم جدی جدی کابلا رو بریدن الان نمی‌دونن کدومش مال کدومه</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4046" target="_blank">📅 13:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4045">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">موشک ملی‌شکن
🔥
@HexConfigs.npvt</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4045" target="_blank">📅 13:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4044">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l4QYrHlnbMjn4Pu32X6O7Zh3XXc7rwUWMKD2-KXxWRcnF9XACla6_Y5RvS-7gxLyYzLOCaN26OpMUmVKjwg7C_k11iVz-stA9SJZPslIyE4Z-ivS1N1Ip76Vb8xy-02onr_s3Q-6zGo1oJmtjrJZjAGluzcjDVNmM5sltCL4UCcRVYJ4Xlawzxb24a3GrQFgl79JMRvPiJyPYLV5Gtrl8jleRZo4sLlQymAEqsnZgUhce_tuqe9nmT7C0c7irDihgE_FrcVT7O1Cy32HrYTo5UiTVU1FIacXaEF4SIceR9zbQK3DGncRTtfMOE3OD41aGE3RNq36REYxQ01s7FrqwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4044" target="_blank">📅 13:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4043">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">این سایت هم دقیقا شبیه همینه حتی قالب‌هاشون یکیه
😂
https://api.bluesminds.com/register?aff=drPB
۱۰۰ دلار میده
باز هم میگم مراقب باشید و توی پروژه‌ی حساس استفاده نکنید</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4043" target="_blank">📅 13:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4042">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">چندتا نکته:
1- کاربرا توی ردیت گزارش دادن که برای استفاده از مدلهای anthropic زیاد به باگ می‌خورن و علت می‌تونه استفاده سایت از apiهای دزدی باشه. بهترین نتیجه رو با GLM میده
2- اگر از GLM استفاده می‌کنید هم، یا به ایجنت فول اکسس ندید(که .env) و اینهاتون رو نخونه، یا توی پروژه‌های حساس ازش استفاده نکنید</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4042" target="_blank">📅 12:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4041">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYKZQ2j_W2RnuFSA8JDkXE5nWHdkZTtj5SHtzXDKQp9YxVcWBqL70bdkGdPGYHGlU-ur_IbrMfFZdYWhKAVWijmUOGL-dARPndfTuUlXrfTJQ-MTNlsGcwV5FeOWr98sTTsK9W25Q_q7QIroBe4FNuWlwM1MPZiIisIMY7lreCeVpXsBDwV17UoXZ4rD0vBMgz0sthIzXsb1UolEjbSMPp8-u0EvQu7aYexZLskUrcPg9cCNkpiRMyFBzhpN_d_AQMt5r2FlhwW9xoYyUk2VDy7cL22i_hEQA6DVB-9QX-bYAvCogGWqvy5exX2tVoTiogKDM0DRdSQLBG4jmRdB-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایپی 188.114.97.6 دیگه سفید مطلق نیست و با ایپی های دیگه کلودفلر فرقی نداره. /// البته رو بیشتر نت ها به غیر ایرانسل کانکشن خاکستری نداریم و به راحتی میشه به کانفیگ های پشت کلودفلر وصل شد. برای ایرانسل (و بعضی نتهای دیگر در برخی مناطق) هم با استفاده از فرگمنت…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4041" target="_blank">📅 12:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4040">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gh8dCvVBILeHHq7Cu2mAqLhGjW3lUUSfZjdz9pHd6d5rdsYUxGx_vmbEMcohbLpMtUObcy82hic0NixkzSCrKYkR-7ohEV7ZIJjdU69JngcXzSv-CemLlOFHyNKIWZxV0UfS8M-3ech-2jaTkEtwUeAdiXJj4oT2rq-E4sdBB0_L4HR6teNJyUl3QMgF5XogwgMFnSfbqnpDjt4BtGybAEh4ktKHD3W7dPSEVUCdoSo9ykunIQNJvxtg26d8i8OjuuwZti3Mt2VuuKunanrsBAZitHSmjL7VaNzUOwmkyjDKFeV8JByPWAbl4qRo8dPiBWysuJWcRqkBGiZVvqwJjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارت 2: آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI  پارت 1: https://t.me/MatinSenPaii/4021  #MiMo</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4040" target="_blank">📅 07:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4039">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BO9jR72OYhZIiDxg9kvyRcb1nGd_GVdMyOHIVHo5B95SXPa1ESTr95GzEqTOd7mAQm9CrFEdbj6S1IRyz_eVvuBX9TxjPlGVUKJuASRIdd-1WK-Yg1GujrV13cn3RWJ7NI6Pf4UurxBMBec1tpF4p0Sr-jJerWHiS66y8_Q5Wn7O8qzT64kMKWvcs2GHcNdi7V2lLKCibkTg4Bq_Z6q6qWfHSqy63VeNuDGe7zYNzdM613-oswpTxqMJ12zzSZPtVzc2ZIQ4vEC4Gf0JFDkH5TQmEK5rFJxAqRrU7VPJteqhydPGyyQnyP_Z0OMEge-VBBjl-5XBsyAuzhDKap8skg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از GLM 5.2 استفاده کردم برای ساخت همین رباتی که توی این ویدئو ساختم با پرامپت یکسان، و نتیجه حقیقتا غافلگیرم کرد.  عملکرد GLM 5.2 واقعا همونطوری که میگفتن، کاملا نزدیک به Opus 4.8 بود. برتر نبود، ضعیف‌‌تر هم نبود( api رایگان گرفتم 150 دلار اینجا هم گفتم چطوری:…</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/4039" target="_blank">📅 01:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4037">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/McrzWpTXL9_UjxRHNzFPyAC7ASeoTT7gw5nfkPITlc4UtP6_1-wyj9qID0KDtpfnp3Rq0Gg6kG_Rbh32A6f_S1rhuKU-9BXUgrCAsaHEsIBk9q9Fdf22VLbFgoBix9f3H9WAa3TnyjBNrAOkbUzUsJFq0e68sO895y_F2wezUIkOcHXlGQ0F_gR3BpplMhJP0sKdtFbIlJ5vXpo3KY7qnB0CMX4CYGt1bX7WDrur20xLlKXnKozkAgBmJ_XEQ9aZtBoC0Mf8aOWssm8dQ5q6QuADcDt-bxDWFLpoD8QqDy1TLiZRuYW8KYtaMQzziyh3ZuOUd-sJdpFVDrXpGcwXxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از GLM 5.2 استفاده کردم برای ساخت همین رباتی که توی این ویدئو ساختم با پرامپت یکسان، و نتیجه حقیقتا غافلگیرم کرد.
عملکرد GLM 5.2 واقعا همونطوری که میگفتن، کاملا نزدیک به Opus 4.8 بود. برتر نبود، ضعیف‌‌تر هم نبود( api رایگان گرفتم 150 دلار اینجا هم گفتم چطوری:
https://t.me/MatinSenPaii/4023
)
این ربات تلگرامی که One Shot کرد، کلی چیز داشت که اصلا من بهش نگفته بودم اما چون صرفا فکر کرده بود که "منطقا" باید وجود داشته باشن، خودش نوشت. که خب هم خوبه هم بد.
و واقعا نتیجه 20 برابر خفن‌تر از باتی بود که با MiMo(که خب بنده خدا مدل رایگان بود) نوشتم توی ویدئو:
1- بعد از اینکه ویدئو رو میفرسته، خودش پاک می‌کنه( از روی دیسک )
2- به لیمیت Bot-API تلگرام اهمیت داد و محدودیت حجم 50 مگابایتی دیفالت(قابل تغییر در صورت ساخت local-tg-api شخصی) گذاشت.
3- کدها به شدت تمیز و مرتب و با structure درست نوشته شدن
4- خودش چندین بار همه‌ی فابلیت‌ها رو تست کرد و تا مطمئن نشد که هیچ مشکلی وجود نداره، تسک رو تموم نکرد.
5- بزرگترین تفاوتش با MiMo این بود که میمو صرفا تف کاری کرد که یه چیزی باشه که جواب بده. یعنی اصلا فکر نکرده بود که این قراره یوزر بیاد روش، روی سرور ران بشه، قابلیت سرچ کاربرا باید چطوری باشه، لیمیت داشته باشه حجم، و... . اما GLM کاملا فکر اینجاها رو کرده بود بدون اینکه بپرسه حتی
6- مهمتر از همه، یک بار فقط بهش گفتم و همه رو نوشت. نه گیر کرد، نه اشتباهی کرده بود.
حدودا 5 دلار مصرف کرد و حدود 140 کا توکن، که به نظرم ضریب دار حساب کرده خود AgentRouter برای GLM چون اونقدرا زیاد نبود کار، نهایتا 1 دلار باید مصرف میکرد برای همچین تسکی.</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/4037" target="_blank">📅 01:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4036">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">می‌خوام همین رباتی که توی ویدئو نوشتم رو، با GLM-5.2 و همین api رایگان agentrouter که گرفتم بنویسم ببینم چند دلار مصرف می‌کنه. با همون پرامپت و با Cline اکستنشن VsCode</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/4036" target="_blank">📅 00:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4034">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پارت 2: آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI  پارت 1: https://t.me/MatinSenPaii/4021  #MiMo</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/4034" target="_blank">📅 00:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4033">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پارت 2: آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI  پارت 1: https://t.me/MatinSenPaii/4021  #MiMo</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/MatinSenPaii/4033" target="_blank">📅 23:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4030">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h3OtbCaThgH6DhL0Wd3lMuApfTO8kqOsVzkNxbL5YAb7YlWx2zeuMpSOi6DfGQSgGUqFpWsGNqqaPK85_IYnW6Nn7bx2-lQcdhLUWJKlo5yt9taUUI5RxzVvdsX0CT0RA24CP1nDee6j-3iIp3QZhr02HGiC8FJvzMrSD8bZg5lLu7-1DOeg97iZY9CcHHQ5JxbMtUtjn1n4mTA4fJWwPlRDUSEFSNh1zj3186k9GDAFq3444_kPwr4UrRs_O6RCXyVyYYYde5q7IplKulOkQq8y0aNGP4-ejbuTasQMxDq0Yd8N2P4vT1WJM-Ur8LfReCEEsCyDa5PY_SrjSohGnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر براتون سؤاله که چرا OpenCode انقدر شبیه به MiMo هست، باید بگم که میمو خودش Fork اوپن کد هست و بر اساس اون ساخته شده
🧮</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/MatinSenPaii/4030" target="_blank">📅 23:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4029">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">واقعا یه سری آیپی‌های تمیز کلودفلر، سرعت آپلودشون خیلی خیلی بیشتره. الان که ویدئو رو آپلود کردم متوجه شدم قشنگ.
خوشحالم از پیشنهاد دوستان که تست سرعت آپلود به اسکنر اضافه شد توی ورژن آخر</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/4029" target="_blank">📅 22:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4028">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شدیدا حس میکنم یه چیزی اشکال داره راجبش ولی نمیتونم ثابت کنم
😂
۱۵۰ دلار آخه؟</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4028" target="_blank">📅 22:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4023">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K8DJvtOBDu44gj2BXZoomY8qVno87gK6Cfubv7v_EZbJLnM2h87YK9QzaXJHPYGbafO3FWXD0ipQVoXl1CzHyAqK02t7lkSW0i2-UichZzZ2qCnqXXc1NPUObVGetxwcMkzJTk5Se7GzPAFbL6-4J2ZWRHGGd55SyRDjVP1ssXKT0x1nOePFfILVvAtIfLJB43F_LnOPTS8Lla6MxLbKN-0sRpt7Vj18AYKTfzgUYK92CX3N5LLvGfLMdZTnQMrxoAxwGM9gmf9xrl7ggg9HnIOGhr2YfL8tL2_ewca-evM-tdVoMZQBCnIK_JY2hUJZlwNzR5haVO5AOHGadrHqiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AV4AHQYOKqTSbsMrxlCnaRxTv0Eo_KQKb1u2zSotX5GvLpNDLRd9jeALNzDCDYdwYgajZRbOE-7LyYYDQakyPuCzvluHDvmf0PFWVIIJxzbravzWmzg57S5l2OCXR4XSU3ReEeG1ztGVIffAZH36ElIsZfgLMcMy2g5uXfa9ByblRXWsz1Zng5HKdb3D8VtuwS3kTmDXP1tZiqyAeEcYrCf1YhpcELFYHACdSfSQzsrYOxvLIntqFrjaKsqQ_Cmb4GFROFKyA_TquRITRHh80W8eGPnZDAkX_oGX6XCNKfeSzoA-XhfXPC7fZA6wJ8O1boez1UYUtJVDXQ9RVBgoWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XtPi1c2Xf6JUAOXJ5gG0c1lyva5TowpuNt6kgX0j3qnfZL3aJ-KlquuU-TgZRu-tT2e7AWT9kRYxKQtdF1AcA8CFh3mIZBwVSCgiPhYYAj45IlTSnkHub9oYUtQnBPD1ZYRkME47gIj2Q94PwleoPEBVWrTETfWmEaP3bHzDbjjOwawhFhhCaPR53exDai0GwvJuKESSNQUhhrN5L3rOYMVKXE5VF8iBYdTCn6HmbuA7L1BSUGwv7GmXE9lAhcd2GLORJUTzgBfAOyF2-IeyeTAZOxal96KTIfd_T2qHNVQqCVlPPsYyfAqemZ054MNSEXWX62ls7UCBmrX_9uvQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nIuyuX7-_ffouB0M2vGJTkSJ0zBR1sxAt55lmjG6BFgzsWc7CSxJt4sLxPdQwIEcHpps3IqecfjDGXnZqTfmZiYp7RSvROoj-c6g6nCBL1Qxm6ZuWRqLMfiJNxbkYctgGep-7rN7Hhp35jRXHNe9_BweVq18n5hOPvOMJhoeZHRN27ho-GsCM4NxoI8oxHorwme55gz34ltyZEQqo7PJT-UNodcjcPYNnXsE9s4qc2mprjdf-6RwNrrtkX6FHM4AQnU_jYNMfAkLBAMxjLKKYugil_zroLY-QsiCkNbV1TcBf-Y1-Fs0vXD3lWK2-DygqS1wBNvi-ZkCwLgVo1AY1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p9MwsuLoRPI9UIt4fqfZaJjY58-Jyj0LrKEjITud78J3nVnD3e5mCYtM6hoSdYb9Fto2NPB82m4Y4YL0HyG1RMqjh_PRpl52X_fdn-c12j5sE8ezRdx9uo8M-OlHplhtqRNGFrIghQyRzCuVllKKRSuV1qqjwQ744AuFI5SmijUnNGHyXnwfPvIP_TYj-0KEt1WB5Qdy1qDS6OkEm9B5qhaC2mcPBynnMI_CcSM75QSn1Lwf6BJ71UPwpSFyWIAGOhklINaRDBJdhqOaEbmOWYHECTFwMx5xAu8i5Gnnpx0dRK5gR9zbj-i-AH7T3T1tJ_3FZi0oD7Sfsp9jmLMCJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این وبسایت، می‌تونید 150 دلار کردیت api برای مدل‌های
Claude Opus 4.8
Gpt 5.5
و غول چینی GLM 2.5
رو میده.
مهم: به این نکات توجه داشته باشید
https://t.me/MatinSenPaii/4042
منم الان 150 دلار رو گرفتم. با گیتهاب ثبت نام کردم ثبت نام عادی disable شده بود توسط ادمین.
برای موجودی بخش wallet رو چک نکنید. از منوی همبرگری سمت چپ، account settings رو بزنید، درست میشه طبق تصویر.
با تشکر از
شهریار
عزیز
فردا استفاده می‌کنم ببینم چطوره:) ایشالا که نبنده اکانت رو
من خودم با لینک رفرال ثبت نام کردم، فکر کنم ۱۰۰ دلار بیشتر بهتون میده(به جای ۵۰ دلار، ۱۵۰؟)؟ نمیدونم. این لینک رفرال منه اگه خواستید بزنید:
https://agentrouter.org/register?aff=PvaZ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/4023" target="_blank">📅 22:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4022">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پارت 2:
آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI
پارت 1:
https://t.me/MatinSenPaii/4021
#MiMo</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/4022" target="_blank">📅 21:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4021">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TvuWqJ1kKhbtZXPbaxxvmJaWwpqKXMFNVqLZFwcMHWcu6TV8Meenw7agBoDxFUQ9JUzmymkZMnIkkAtwdoX-t0sE7_jjBB8xW1ZYZXt__q5NXWIZLr6q9tRwHMonYqQKTADP2PVp78MXJhn13tBhL2oVrEBWHHu5Cd6ShWiTbDn2127DsNyIOzY7z9X2ZttlEKRCzxjIb5gUPr_M8ip1diABXgxB3ikDxzUzylv0_d5JU2e838bqfK8O4kIIW7Q3ZbRFQt7lXh0hgwDlIS1luFAZ4YeTbnoK4Gp7Jf9-dt1HoPAVK4kw8U8AcZD-JR2HrggCM3Xj8mMsAlf7BH1gEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI
⚡️
لینک‌های استفاده شده توی ویدئو:
1-فقط گروک استفاده شد. ویدئو رو ببینید متوجه می‌شید:
https://grok.com
⭐️
توی این ویدئو:
1- یاد میگیریم که چطوری از هوش مصنوعی استفاده کنیم تا ابزارهای مختلف رو نصب کنیم روی سیستم عاملمون
2- ابزار MiMo Code رو نصب می‌کنیم
3- کار باهاش رو یاد میگیریم و مود‌های مختلفش رو بررسی می‌کنیم
4- یه ربات تلگرام تیک‌تاک دانلودر وایب کد(5 دقیقه) و وایب دی‌باگ(50 دقیقه
😂
) می‌کنیم
🤎
اسپانسر ویدئو:
شمع‌های دست‌ساز لیرا:
https://t.me/liracandles
❤️
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگانه و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب
✉️
پارت 2(بخش پروژه‌ای که می‌سازیم):
https://t.me/MatinSenPaii/4022
💰
دونیت</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/MatinSenPaii/4021" target="_blank">📅 21:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4020">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">توی ویدئو از عمد وایب کد کردم صفر تا صد. و قشنگ می‌بینید که Vibe Debugging ده برابر Vibe Coding زمان می‌بره
😂
😂</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/4020" target="_blank">📅 20:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4019">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ویدئوی امروز راجب Mimo code شیائومیه. و با پلن رایگانش یه بات تیک‌تاک دانلودر تلگرامی می‌نویسیم با یه پنل مدیریت کوچولو، که خب چون یوتوب به شدت حساسه روی ربات‌های دانلودر، مجبورم اون بخشش که ربات رو می‌نویسم و باهاش از تیک‌تاک دانلود می‌کنم رو اینجا جداگونه آپلود کنم</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/MatinSenPaii/4019" target="_blank">📅 18:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4018">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هرمس — ایجنتی که با خودمون رشد می‌کنه
🎨
این Hermes Agent که دیروز راجبش صحبت می‌کردم، یه ایجنت(دستیار؟) هوش مصنوعی اوپن سورس هست که اواخر بهمن امسال منتشر شد(که ما هم بعدش نتمون قطع شد و از دنیا عقب موندیم برای همین من تازه کشفش کردم) و توی کمتر از چهار ماه…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/MatinSenPaii/4018" target="_blank">📅 16:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4017">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xb2Ibxq7biTlESNMNyigOMnlXuhTDp-Euypm7WwgvlpZKqamNIUBz9hqRvO_ABtPcgGa5Gu1KcTFi5fxEPtVzAyp8bHprHHku2TS4QfaH-EO-wh4HWTC4FVoTAHUOzpNDBZHYiXkqKepKaiy7-Y6fuarAjZmKN7Hll5eQ6MQE45jTW2nr4CGHoDAVj8u1r49exiDMbYQgi4Xmhl8oPWsjfslWC5ys6-AJSrrmn90y76Rgm0uZTji6rc0VolXIfIFF8swqq7mXWnNXCkIjNsd8Px9RYEzlDfs9aAzjtkRGTsYGPoXfm8c67eesnqYTRkn5nESrOjU4otegAEWgvjCuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من تازه فهمیدم میشه با توییتر پریمیوم از grok پریمیوم استفاده کرد. بازم دست اون عزیزی که به من پریمیوم هدیه داد درد نکنه
گروک بیلد رو دیدم، جالب بود
خوبیش اینه که وقتی رقابت زیاد میشه، 1- یا قیمت اشتراکا میاد پایینتر یا 2- کیفیت بهتر میشه و میره به سمت تسک‌های ایجنتیک سنگین رو خوب(و بهتر از رقبا) انجام دادن. تا اینجا Mimo و GLM و مدل‌های چینی، واقعا توی هزینه و... همه رو میزنن</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/4017" target="_blank">📅 16:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4016">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/frR3qby4xIIv1SocfB8FJyo8M7GgzjfgkfsCFRjLHXFdZEvdk7ljJ8u5hf5xYseB6gtmxOIsUdK-_aLXqudiAuifAZ8jZ9N_s0TuRPpYCidwOttyF-zDJfTwo6GKybMDt8vVoLIGOAEM1IzlTYzPW7BFTfo-vltIh0p63FcOTbWSSELf1qYQuygbRlxNXUeUxyruu87PCxOrQD3VO_w2H-ldsSRynEh6XWd8nzvZeKrx8CbnfdZbcW7vRX8cM0RBBuoC46I4MsXoqZtfusHRQ6DE3PuB9hiNvnSgA5Tpw3KVfCvbeaNT00uH-sDpErjJY9I3m-WhJ4878_7mfWxfVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس — ایجنتی که با خودمون رشد می‌کنه
🎨
این Hermes Agent که دیروز راجبش صحبت می‌کردم، یه ایجنت(دستیار؟) هوش مصنوعی اوپن سورس هست که اواخر بهمن امسال منتشر شد(که ما هم بعدش نتمون قطع شد و از دنیا عقب موندیم برای همین من تازه کشفش کردم) و توی کمتر از چهار ماه بیش از ۱۸۰ هزار star گیت‌هاب گرفت — یعنی سریع‌ترین رشد یه پروژه متن‌باز ایجنتی توی ۲۰۲۶. مجوزش هم MIT و کاملاً رایگانه.
تفاوتش با بقیه ایجنت‌ها اینه که نه صرفا یه دستیار کدنویسی تنهاست، نه یه wrapper ساده دور یه API. هرمس روی سرور/کامپیوتر تو زندگی می‌کنه، از هر تجربه‌ای یاد می‌گیره و هر روز کاربلدتر می‌شه.
مثلا دیشب که من بهش گفتم جدیدترین اخبار فیلم و سریال رو برام پیدا کن.
رفت که توی گوگل سرچ کنه، اما گوگل بلاکش کرد و نتونست.
به جاش از یه راه جایگزین استفاده کرد.
دفعه‌ی بعد، که اینجا پستش رو گذاشتم:
https://t.me/MatinSenPaii/4014
بهش گفتم که خب جدیدترین اخبار ai رو بیار
دیگه نرفت سراغ گوگل. چون یاد گرفته بود که گوگل روی آیپی من بلاک می‌کنه، برای همین مستقیم از ابزار جایگزینش استفاده کرد. که ما رو میرسونه به اولین و بهترین ویژگیش:
🤔
حلقه یادگیری بسته — قابلیت اصلی
این مهم‌ترین ویژگی هرمسه. بعد از هر اجرای task، هرمس یه لایه ارزیابی اضافه می‌کنه — نتیجه رو بررسی می‌کنه، الگوهای قابل استفاده رو استخراج می‌کنه و به صورت فایل‌های Skill ذخیره می‌کنه. دفعه بعد که مشکل مشابهی داشته باشی، به جای اینکه از صفر استدلال کنه، مستقیم از Skill آماده استفاده می‌کنه.
ادعای عملکردی‌شون هم اینه که ایجنت‌هایی با ۲۰+ Skill خودساخته، task‌های مشابه رو ۴۰٪ سریع‌تر (از نظر مصرف token و زمان) انجام می‌دن — که توسط TokenMix هم تایید شده.
📚
همه جا هست، با یه حافظه مشترک
تلگرام، دیسکورد، اسلک، واتساپ، سیگنال، ایمیل، CLI — یه ایجنت، یه حافظه، همه‌ی پلتفرم‌ها. به علاوه دو ماه پیش هم پشتیبانی از iMessage، WeChat و اندروید (از طریق Termux) اضافه شد.
💪
ابزارهای قدرتمند built-in
جستجوی وب، اتوماسیون مرورگر، vision، تولید تصویر، text-to-speech و استدلال چندمدله — همه از طریق یه اشتراک Nous Portal یا api ای که شما می‌دید بهش(اگر این قابلیبت‌ها رو داشته باشه مثلا جمنای) قابل دسترسه.
همینطور با Nous Portal، OpenRouter (بیش از ۲۰۰ مدل)، NovitaAI، NVIDIA NIM، Xiaomi MiMo، xAI/GLM، Kimi، OpenAI، Hugging Face یا endpoint شخصی خودت کار می‌کنه. با دستور hermes model بین مدل‌ها سوئیچ می‌کنی — بدون تغییر کد، بدون lock-in.
:
📆
زمان‌بندی طبیعی
زمان‌بندی با زبان طبیعی برای گزارش‌ها، بک‌آپ‌ها و briefingها — بدون نظارت، از طریق gateway اجرا می‌شه. یعنی می‌تونی بگی «هر صبح ساعت ۸ یه خلاصه از جدیدترین اخبار ai بفرست پیوی تلگرامم» و کار تمومه. مثل n8 n سر آدم کچل نمیشه.
🏆
اپ دسکتاپ (تازه اومده)
بیست روز پیش، Hermes Desktop به صورت public preview با نصب‌کننده‌ی native برای ویندوز، مک و لینوکس منتشر شد. اپ دسکتاپ از همون core مشترکه — config، API key، session، Skill و حافظه رو با CLI و gateway به اشتراک می‌ذاره. یه fork جدید نیست، فقط یه رابط گرافیکی روی همون ایجنته.
😎
حریم خصوصی و امنیت
تمام داده‌ها روی ماشین خودت می‌مونن. هیچ telemetry و trackingی نیست. از آپریل ۲۰۲۶ تا الان هیچ CVE عمومی‌ای برای هرمس گزارش نشده، و به صورت پیش‌فرض اسکن prompt injection و فیلتر credential هم داره.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/MatinSenPaii/4016" target="_blank">📅 15:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4015">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خب خب، دیروز فرصت نشد؛
امروز Hermes رو یه معرفی کامل می‌کنم</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/4015" target="_blank">📅 12:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4014">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W8OS6s3ZcIbdhZG7Lmr8pMCPHxw2n4_UsZBaZTxJn9W9N3hsqT0DN-chlkFTkTiKZXbp7eargc0x1-d0YA0J4_fuMd8mjIWZTOoo79i2bWq-IPU8y4771q_sCrRym5ohYxKmUZBk7Fem5EubURCE-lhaua6vBjyTRjLO_-eypeV5QPCJDb95XbSyZRtNA1WtdI7lVvQvDMVKvDD1zP0Gz0itdzo4sbaYKlXeEdVemgJXLXuES44_pt3wJXLMr3v7z6l0rOQOKwur9tUaiuwfSfYtP7uYHfbuj8OgDbr4Dei-V0Ecm6y8vvf6IaBPxTH2W5EVWpMXI2nOb7ickDzAbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ازش پرسیدم که تو می‌تونی چیکار کنی برای من؟ و این جوابیه که داد:  سوال خوبیه! من یه AI agent خط فرمانی هستم که روی Hermes Agent اجرا می‌شم، و اینا کارهاییه که می‌تونم انجام بدم:
🔧
سیستم و اتوماسیون اجرای دستورات shell، اسکریپت‌ها و پردازش‌های پس‌زمینه برنامه‌ریزی…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/4014" target="_blank">📅 02:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4013">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خلاصه‌سازی ترانسکریپت YouTube</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/4013" target="_blank">📅 00:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4012">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UVFvZbd8OruL7-w-N5Nox_SQGjEC8sWaBFXx8C1E1T9wRLrEk77_GZi6P8dPJSkQEnFMTTGcayVUkxuK3cmx4E2A66_3WqC3UQREz-lUCF2ELKKpnpCbieYTdoILd91uUxdin24P0r02qI0Sz_w6hfCxXlOYkjTKu5w5mZr21X00dMCVU7zneRnJm0kF8c4tiKfcE8DNI_RB1b7y9UYQsqQzph0q1yLXwU2T-szzkpPABASxDESlSvNV1c3cZ5NK5ALdkyxSiEuYMmeSpyOO35hwxuSEjSMkBv_n5Y0eIhVdjXWBmnA96YT-4UfdC9C_44vzQ4TbiIQiZS42_JeNkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ازش پرسیدم که تو می‌تونی چیکار کنی برای من؟ و این جوابیه که داد:
سوال خوبیه! من یه AI agent خط فرمانی هستم که روی Hermes Agent اجرا می‌شم، و اینا کارهاییه که می‌تونم انجام بدم:
🔧
سیستم و اتوماسیون
اجرای دستورات shell، اسکریپت‌ها و پردازش‌های پس‌زمینه
برنامه‌ریزی cron job برای وظایف تکراری
مدیریت فایل‌ها (خواندن، نوشتن، جستجو، ویرایش، patch)
💻
توسعه نرم‌افزار
ساختاردهی کامل پروژه، کدنویسی و ریفکتور
گردش کار PR (branch، commit، open، review، merge)
توسعه مبتنی بر تست، دیباگ، بررسی کد
ساخت و اجرای پروژه‌ها (Python، Node.js و غیره)
🌐
وب و تحقیق
مرور وب، scrape صفحات و جستجو
فراخوانی API، تعامل با GitHub، Airtable، Notion، Google Workspace
جستجوی مقالات علمی در arXiv
مانیتور کردن وبلاگ‌ها و فیدهای RSS
🎨
خلاقیت و مدیا
تولید ASCII art، دیاگرام‌های معماری، اینفوگرافیک
ساخت پروتوتایپ HTML، انیمیشن‌های p5.js
تحلیل تصویر، تبدیل متن به گفتار
خلاصه‌سازی ترانسکریپت YouTube
🤖
Agent های خودمختار
تفویض زیروظایف به subagent های پس‌زمینه برای کار موازی
راه‌اندازی Codex/Claude Code برای وظایف تخصصی کدنویسی
📋
بهره‌وری
حافظه پایدار (یادآوری ترجیحات بین session ها)
سیستم Skill (ذخیره workflow های قابل استفاده مجدد)
یادداشت‌برداری با Obsidian
کنترل خانه هوشمند (Philips Hue)</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/4012" target="_blank">📅 00:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4011">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خب بچه‌ها من با بدبختی تونستم با api رایگان این داداشمون https://t.me/MatinSenPaii/3990 ، مدل DeepSeek V4 Flash رو روی Hermes بالا بیارم. برای یه سلام، 17 هزارتا از 1 میلیون کانتکستش رو مصرف کرد
😂
بریم ببینیم چه می‌کنه</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/MatinSenPaii/4011" target="_blank">📅 00:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4010">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اپلیکیشنش متاسفانه پر از باگه اصلا Custom Url به درستی نمیگیره، سرچش بعضی وقتا خرابه و...
البته خودشون هم گفته بودن فاز تست هست هنوز
درود بر CLI</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/MatinSenPaii/4010" target="_blank">📅 00:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4008">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KjZzH3EZH_m2T9YttLsdxH1I5co74BUI5Ya1177y8sbrFyXwstlI2JE3OBLQbSi39nQx-pNSyRouiJRIyvKfl0hmgdU9n6pmTjoabOU2lpKOZ0V4Q9Z-4nnghJFugm8iqfMZZHc3KiSslUvaqjQfM6EVEJ_Elt2xN6iYQp5Ssglp7QhISYtjrO5XYffk7mELIAGkNQQnlK-tEF7CIrOKVYYHGYmy1O8pc-spx9f2-GLbeVn5EmdbdhhEJ7QU74c530QknoEsUyiD56Y8j4TkxXQG_UwNsmk-GzglxPULEmDVlLFyhi1PTYQ8_sepI57dkQQko9qInVlPqqQw6U1oGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tKXXJnh9tZFeDfH_aEzOVxuAs9LUIue-MXA1YAZHFLvRjJg_ZDNPBYyby4KH5wAXuJ8JXuvgAaZMfoU4kbTLj88R6Ja-bfUUHmkZKIx3PXq3rqcG7XlCqQEp33OEA2aklRf3zq3sautl0TgUf880H7iVZVCRGywXLuUBdaHnqz6w0Q0GBNsu1KyXU-iR0GtcZk5m8Jp66FEsG-F3UubA8xdOajDu9utPCSVJZdIkhQZY25KG3KVxwPwNN-VsADTHqJ5JWK2EmELbPQauVy-il2SFFd50kDOfOAfJKJEfFR0CXC_veKQdUK6QfMNW458GSy1xxz0VauqTNJoq0fTong.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها من با بدبختی تونستم با api رایگان این داداشمون
https://t.me/MatinSenPaii/3990
، مدل DeepSeek V4 Flash رو روی Hermes بالا بیارم. برای یه سلام، 17 هزارتا از 1 میلیون کانتکستش رو مصرف کرد
😂
بریم ببینیم چه می‌کنه</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/4008" target="_blank">📅 00:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4007">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حالا ای کاش قیمت سخت‌افزار پایین میومد یه کم
😢</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4007" target="_blank">📅 22:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4006">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vkJ_fGBnA7RBFFu1OfS2E2EI9TPkr45F2VqrGDthofYZTilX5L0ZoCeS0NuKCIrrfyr2LsxjCxqdDPY4fCjd5b8WzD4O-Y3odsqGpQ7xuLpu-BbkWUeTD2HHNHxjNYBbuzFvETepkn5oix3WIF8Q9ooCtHPuyxpJB-xv8Lx3gJrY7WYfDwPBwgoqYYiJa594wge1ArMMZ_t09_5Bt_kiW224Sz0BhzzARFLvqFWEsfKItBRC0G3RdWQ0PLWGR9g31LUaSzqe4PSP4vFvz5CYpszbJanW3w6WcmCumcYyOwf944rCRPpza0gOV62KwQhk0FwHxbQiO1h-cVGshhIZEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین تراشه هوش مصنوعی اختصاصی OpenAI با همکاری برادکام معرفی شد
شرکت OpenAI با همکاری برادکام از نخستین تراشه اختصاصی خود با نام Jalapeño  رونمایی کرد. این تراشه که از نوع ASIC است، به‌طور ویژه برای فرایند استنتاج و اجرای ابزارهای هوش مصنوعی مانند ChatGPT طراحی شده تا سرعت و پایداری خدمات را افزایش دهد و دسترسی کاربران را تسهیل کند. OpenAI می‌گوید فرایند طراحی این تراشه را طی ۹ ماه به پایان رسانده است.
خالق ChatGPT که پیش از این یکی از بزرگ‌ترین خریداران پردازنده‌های انویدیا بود، به‌دلیل رشد تقاضا تصمیم به توسعه پشته فناوری اختصاصی خود گرفته است. نمونه فیزیکی تراشه Jalapeño هم‌اکنون تحویل OpenAI شده و انتظار می‌رود استقرار اولیه این شتاب‌دهنده‌های هوش مصنوعی تا پایان سال ۲۰۲۶ آغاز شود تا زیرساختی کارآمدتر و ارزان‌تر برای آینده هوش مصنوعی فراهم شود.
✍️
دیجیاتو</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/4006" target="_blank">📅 22:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4003">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-armeabi-v7a-release.apk</div>
  <div class="tg-doc-extra">33.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4003" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بیلد کامل اندروید SenPai Scanner، با تشکر از
Hidden-Node
عزیز</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/MatinSenPaii/4003" target="_blank">📅 21:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4002">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">توییتر هم دیدم چند نفر گفته بودن اما گویا منطقه‌ایه</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/MatinSenPaii/4002" target="_blank">📅 19:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4001">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کانفیگای کلودفلر روی ایرانسل واقعا دارن بد کار می‌کنن</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/4001" target="_blank">📅 19:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4000">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GtIQ98TUr-IbxOaclHTRoUlxSJftcjGNiW8AoSek3nxKU1Hvdi9cmhg9i7X0pdkPDDZrPIMN03YTTtuXvBOqbkZDkB2mToM64NttzOTPO8OokKuouAA1uNSmz8o578YOUhYJszYlesq603GZJdh98qQMteglUWME1Tj8DdCLWjzcjQ6VEdubrAx7W28kJC9ortx4v1MO0S9mM6M6LiKxmZ2opIBHWeYihlkqP_uzldKQjkVnvR8Sz-4OdbmmSpuIS5mu8PX2oNs7jEhF_bzIejhNjNSGwM_1LKIzDeiy-DUrOD_cGcLqRqmak-rzsZJ94SghzTJSqKPn1qKYEGApoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس رو هم دارم نصب می‌کنم، به نظر خیلی چیز خفنی میاد. به زودی تست میکنم و ازش یه کم کار میکشم و نظرمو میگم</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/MatinSenPaii/4000" target="_blank">📅 19:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3999">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🛡
چطور آی‌پی اسکن بکنیم؟  یک آموزش براتون ساختیم تا بتونید با اپ SenPaiScanner روی گوشی اندرویدی خودتون آی‌پی های کلادفلر یا رنج های خودتون رو اسکن بکنید.</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/3999" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3998">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">34.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3998" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">به زودی نسخه یونیورسال هم ارسال میکنیم.</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/3998" target="_blank">📅 18:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3997">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🛡
چطور آی‌پی اسکن بکنیم؟
یک آموزش براتون ساختیم تا بتونید با اپ SenPaiScanner روی گوشی اندرویدی خودتون آی‌پی های کلادفلر یا رنج های خودتون رو اسکن بکنید.</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/3997" target="_blank">📅 18:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3996">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">برای دور زدن تحریم‌های اندروید استودیو، قبلا هزارتا پشتک وارو میزدیم. همزمان Shecan میزدیم و پروکسی و وی پی ان
🤣
اما الان با پروکسیفایر که وسطای این ویدئو
https://t.me/MatinSenPaii/3372
آموزش داده بودم، به راحتی هرچی نیاز داشتم با کانفیگ‌های کلودفلر دانلود کردم. با pdanet+ هم میتونید دور بزنید</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/3996" target="_blank">📅 18:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3995">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">برای یه کاری دارم اندروید استودیو نصب می‌کنم و از الان گریه‌ام گرفته
😭
خداحافظ جای خالی روی لپ تاپ</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/3995" target="_blank">📅 17:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3994">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یکی از دوستان، این رو گفت برای مشکل ابیوز کلودفلر:  برای حل مشکل بلاک شدن دامنه‌تون تو کلادفلر این کاری که میگم رو انجام بدید. برید توی dns records و گزینه export رو بزنین. اینطوری تمامی رکورد‌های dns ای که ساختین رو خروجی میگیره ازش و  دانلود میکنه براتون.…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/3994" target="_blank">📅 15:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-3993">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یکی از دوستان، این رو گفت برای مشکل ابیوز کلودفلر:
برای حل مشکل بلاک شدن دامنه‌تون تو کلادفلر این کاری که میگم رو انجام بدید.
برید توی dns records و گزینه export رو بزنین. اینطوری تمامی رکورد‌های dns ای که ساختین رو خروجی میگیره ازش و  دانلود میکنه براتون.
بعدش روی آیکن مربع (سمت چپ فیلد Name و آیکن سنجاق) بزنین تا همه رکورد‌ها رو  انتخاب کنه و بعد پاک کنین همه رو.
اینکارو که کردید برگردید توی قسمت overview  و روی Review on Blocked Content page → بزنین.
توی صفحه بعدی روی آیکن سه نقطه بزنین و گزینه Request Review رو بزنین و I have removed the content. رو انتخاب کنین و بعد روی Request review بزنین.
یکم بعدش باید آنبلاک بشه دامینتون.
هرموقع که آنبلاک شد برگردید تو قسمت Dns Records و روی گزینه Import بزنین و اون خروجی‌ای که دفعه قبلی اکسپورت کرده بودن رو این سری import کنین که راحت همه رکوردهاتون برگردن.
احتمالش زیاده که مشکلتون حل بشه و دامینتون برگرده.</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/3993" target="_blank">📅 15:32 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

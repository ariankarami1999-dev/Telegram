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
<img src="https://cdn1.telesco.pe/file/gnKh-KvUElndqeEQ4W07Mm-i79XeRrWG_UXb9GRT7SgLBZlUArXF4SrcAFxa7XzbH0P_5h0ZGhAEC6Hg9Ew1t9d3NMPfHg-udZN5KamM6Wv55NPcxO4q_0XOx4E4e-XxKJy9Q-RUOk110CV19GF9PjOmIMe1gDn77TP1IGzirmJzsNPoLKeiU61ymqJm_78ymIp01vem49QB1OJRfbC7EuOClZxr9KKTwjRqOn0NH11w5sh0qktNSAf_z0ZKDQd3wXPyZAtOb_x68dwm7exFKsKg3tcc4BOi5Oqy29DYzXy2SOmCVcvvipg8km4FA_Z1rtFbFBWVmq2mz2jx3eYCpw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 161K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 03:37:39</div>
<hr>

<div class="tg-post" id="msg-3654">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دوستان برای هیستریا، سرورهای AWS آمازون با این سرعت جوابگو هستن چیزی که من دیدم و دوستان گفتن و متأسفانه دیتاسنتر دیگه‌ای ندیدم که به این خوبی باشه. آمازون هم گرونه به شدت
پس از آموزشش فعلا منصرف شدم</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/MatinSenPaii/3654" target="_blank">📅 00:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3653">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شمع Iced latte</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/3653" target="_blank">📅 23:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3652">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/twpJDRfiYs197oIip4i6J9yT2HfrWES-56WtjgItufNjWR2wceJ5gjAh5PIexfD8Lg_Af1FAAbiHPdOkOhcJWK0P3s73KKxUjuPAK_V6CErwWc9OWSv6Jk4etrsea0nbX2Ab73wtI5ji1qmZJ8DEZTrBosSwDWV2yej0CcVWcEdveaOpMk2y6deJ5qnETG4uZLNagVdpoHBmGNEJrrMNnB-9Ul8XHPQ2km6z3FclL0FnjAPUn7ORvZmqHun2gwNf0nb07QxwiOFJuw9I5WSp3LnKDL2Fjo7YiH4e7CevxlgYiCh4CYK2TEyT5MyfJjtrf143MKPvHoLKjw4gnJN8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ارور EOF و 403 گرفتید یعنی گیتهاب هنوز روی اپراتورتون مشکل داره و این یعنی اسکنر نصب نمیشه(باید با وی‌پی‌ان بزنید). طبیعتا وقتی دستور senpaiscanner رو میزنید not found میده چون اصلا چیزی نصب نشده</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/3652" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3651">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux  دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/3651" target="_blank">📅 20:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3650">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KeWhf5oXYz82_-lPIXW38Gna09QLs1HHN_EyIswbxfnCuIWAw_z-4LfKfWPH_beqL_VGccN2zOY3QnOLWKQaVqG9HeA7UDlQeCy0ZgA5H92v7DI54qFvuOmpLDVRi_xSdd_WHtjdjizKVVKkWhAuoRRiAPJG_X0FXPRbt3ozC2lBewc9aW9LBH-TPPwJel0bHc3oYK1aBZEKGqLX2BebLlE96EmWt8svGHhPnyBW9ckzvXueKwjdQ9PHhRhFjd6cVNarR686C0G2GcsahRjWKC_SNfYAq-Ai2ReZUeX_iWNFsyXOVU7Nn-5enIC_-bzby_SfeQzCFeINI7bSvAnOKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر به این ارور خوردید، پروژه‌ی جدید بسازید. اگر باز هم نشد، با یه اکانت دیگه وارد بشید و مجدد تست کنید. توی این ویدئو
https://youtu.be/_aXy8wwyRG8
به همین ارور خوردم و این شکلی حل شد</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/3650" target="_blank">📅 19:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3649">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux  دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/3649" target="_blank">📅 19:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3648">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون متصل بشید</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/3648" target="_blank">📅 18:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3646">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ImftsYJP5C6pKVwrLym9gtiUah1EH2QUU5QzPCaEQ2TK_ByZ6jF-Q2jWKHh7zgSWoJBbYyxzXPiFwVELlyWC0GuX06bDpDMjxFCBXXff6geZfH7Z4sYvkhqfAQn4qjp8Fq1IpY124C1jEfnqYCdBsTlNM7upZS9uWVbtnzHX0P8dTOI9LTBMYqFzSHhhEg54Lkhkcruvbg5SUzREqufasTIxvmO7bhBtyDHJzigEFnoJHHZ7-0I-jXy6SIE80my1WEmcFJISDJJgtQc9CM_IbHcEX5BRYm0wAbaCPvXGpC4N5BLyqhBWfW3MVcWxi4ezMRBfnp6tOhIrCkyqo0jm6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VbxWc9xvDxyijlXLzNLucTmknsC5ojqTtj_nG7Y-gCwob2C0Z0KTbqobj_YmjDredSufHKjM5rMq6ZWwWDEP-Ckjiu_g73KnIgbmEyKte_oMHbkOu8CT7pL9Afp5PUM521rCn2jyXDr_QkhccNLC88VTZhIlTWmsvPiVpCXEYQOZndx3gw-2VJaYj8UyIO3-11lS0vtzUikG59fWpbQAR4snZF53xfMY8vbaJaKAgxLhHsDge4SwIl24i_6K-ZAg_25w_XazsvZjXU3cBX9uzAC6q1H9WIM3uEhu0RcKOV-eW6U0kBOtthvE1q-j0SfvB8sMfJJc8NLXKV5q5LRB7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux  دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/3646" target="_blank">📅 17:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3645">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V4-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">6.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3645" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لیست جدید 33 تایی از کانفیگ‌های Spoof که همه‌شون کار می‌کنن و خودم تستشون کردم</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/MatinSenPaii/3645" target="_blank">📅 17:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3644">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">base.apk</div>
  <div class="tg-doc-extra">11.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3644" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اپلیکیشن RSTA(که به زودی اوپن سورسش رو هم میسازن عزیزان)</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/3644" target="_blank">📅 17:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3643">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-on-Phone.txt</div>
  <div class="tg-doc-extra">350 B</div>
</div>
<a href="https://t.me/MatinSenPaii/3643" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دستورات اسکنر برای Termux</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/3643" target="_blank">📅 17:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3642">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux
دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون متصل بشید
⚡️
لینک سایت کلودفلر:
https://dash.cloudflare.com/
لینک پروژه‌ی  Edge برای ساخت کانفیگ رایگان:
https://github.com/cmliu/edgetunnel
فایل دستورات ترموکس:
https://t.me/MatinSenPaii/3643
پروژه رسول:
https://github.com/seramo/v2ray-config-modifier
نرم‌افزار RSTA Spoof هم اینجا:
https://t.me/rstasnispoof/2/1076
و
https://t.me/MatinSenPaii/3644
⭐️
توی این ویدئو این مراحل رو پیش میریم:
1- ساخت کانفیگ Edge(روزانه 6 گیگ رایگان با کلودفلر)
2- نصب و استفاده از Termux برای نصب اسکنر من و پیدا کردن آیپی تمیز
3- استفاده از اسکنر SenPai Scanner برای اسکن آیپی تمیز کلودفلر با استفاده از کانفیگ‌های Edge
4- استفاده از پروژه رسول برای انداختن آیپی تمیز به تعداد بالا پشت کانفیگ
5- استفاده از آیپی‌های تمیز توی Json  اسپوف و اتصال پرسرعت به اینترنت آزاد
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این متد نیاز به هیچ سرور و دانش شبکه‌ای نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
(با کیفیت بالاتر)
💰
دونیت</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/3642" target="_blank">📅 17:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3641">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vZGNJCgqxYwSnKIahONwA-W9mAT5NjoJZTdP6KjrP4meTJa5zYFm_0OnbiRotmTlifVkDL0dwCwe2BnxsG8xT0CjVuyusAzqmU5vx4N67cH6NkddFi8Y8klNTmc5lX0c7I9vC6lExwGB6jP65b0UEPDDtL3-cDRdG2JS2bOzgozkLbj9C12o6SNXZo1_B_542k6ubZMRaJt_ihk8xRe0UkIOBaWNMw3wmleN3huW4Po2elbWIZe5yXva-KmaufJuo8RNsDtkb-Td9d5trqhXsD-dD4lUGjUl2LKGQkLaLxCoLgaiAKhPww8v8vflif-xEkL-cdx3Y256zUAYrLbn0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ربات از
یـ‌ بـ‌ خـ
عزیز واقعا باحاله. یه نگاه بهش بندازید:
@iNewsSummaryBot</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/3641" target="_blank">📅 16:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3640">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تصمیم گرفتم یه آموزش صفر تا صد ضبط کنم برای عزیزای دلی که لپ تاپ ندارن و فقط یه گوشی اندرویدی دارن
از آموزش ساخت کانفیگ اسپوف گرفته(رایگان)
تا اجرای اسکنر روی ترموکس(سردرد)
و استفاده از اپلیکیشن اسپوفی که این دوستانمون ساختن
یه مقدار طولانی میشه اما دوست ندارم واقعا که بچه‌های اندروید کارشون لنگ بمونه</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/3640" target="_blank">📅 15:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3637">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hmsMsorES70-elLMFFZrNagihAtSSqOfHhJztTpwtX0fKH_W4nJ-KJ91StCZ5xNtUam3L6_qy815mW7N2QDYNGodHlnIcxYVnT1hT2FGvdagihyHkBzuLV30_BVWRpFb-P444WyCoqXjQqrCtJIpNf790G0gS1NQFOWjlJJ_sk1NFJAOi4od6yZ62v_uNfRpWZxqNYKBJnyxOo1gmtJVgz5m0DMO_l_qbCMADjMp-giZ2Kmwln_di_uFayj4ZqB6-XV2ZlXJ0dB8Un34x_L-e-7wmtuPnDIsZ-rsd8IViRt2rYp170IwPuijXKpAK4frtbkl-gDplRGUmMovCfki0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MF122oEu9UIUfVYk3wXt7Rjq3n6tTqkIB7YgfP50iFYcR2tJ4P_qFVnMCZeiCAaBkMCIBPQ06T2Iww0YMAliYr8PzVYK_vDFJzAp1G4QSpzfrOlxBthiFOLzWX8UfqSPXdr07HTHLQr9bf2d8tX4bGAoFHV8YhSlZ0EOeN-fDp0hoMhU8ZI1nom5LK2bl7T9csAGLCJckkH1oIX-ekvcRCYT1ceqxfk4Cg27vg77gXFHWfpCX1TkZ9J5CXxyRbIKRzVhHJO6IVTyruAC3xWM0vLhf4WKf9NOcIgCpoeRQbeJx2eMEdZLUxsU4wBbQC_Yv6P8yMj337bLrJ8UAq5ddw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز راجب اینکه چه شکلی می‌تونید کانفیگ اسپوف شخصی بسازید و روی گوشی چه شکلی برای Config-Json می‌تونید اسکن کنید با ترکیب اسکنر من و پروژه‌ی Shin، ویدئو داریم</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/MatinSenPaii/3637" target="_blank">📅 15:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3636">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">📱
اگر لینک ساب WhiteDNS رو میخواید از گیتهاب داشته باشید، این ریپو هر ۴۰ دقیقه با بهترین سرور ها آپدیت میشه
https://github.com/iampedii/whitedns-sub
لینک ساب برای Clash Party & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
@WhiteDNS</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/3636" target="_blank">📅 13:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3635">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">امروز راجب اینکه چه شکلی می‌تونید کانفیگ اسپوف شخصی بسازید و روی گوشی چه شکلی برای Config-Json می‌تونید اسکن کنید با ترکیب اسکنر من و پروژه‌ی Shin، ویدئو داریم</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/3635" target="_blank">📅 13:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3634">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2a4acd74d.mp4?token=k31n2Qp6YYDhwnH8Y_-3IUpYVx4QxvEN7WIPEk-Ykp1RBi5fiJyvidTXdj4Mrn0tSLVbiIfp8ZCVfA6T4nPrqluF5NI0jjk0BUJGTUcKdneyq7vyGR_5lqaPV6dmX_wM55nUh3dwyAtA_lKJW8OeSN7fCtWYm3BMcTEplu4_yb9S-fO8gYK0Z79fCuPFMnBAtr4gRG9m_o8Yoe2xaukYKnv0zDFCMcxdHkT70jeTOmXRDMlE5CM3ny81P1Z9Tw0om7saNr4yQ9cKnYMxGCIJafgA45cvL6LvKRX2uML3jRxv1el8Rjhh_6M8ldvdaioR_ZfiudKJUa2kQ1RzWyVPe5yCSko7mEzBJS6uJfIb9rhHcve-87kvg_D8inMfNl_6rZ6v5HFkzZUIHq3_b50dHqWhiqjGN_PA5Gzzo3Ye5Zmpt-uglciSkNIV2gmLI5YOVQ0iksQ46pUc2u3Zi_CZldHeB8XsZxdZXpsBJBIiAifA8m1n736xUWCXNN4fZRiCO2lbDzgZ8xo_g395EYifL5MDhI2sY-WwzJqpXBci6KCzAh-zPrZT-_7BzImWZnU7sw-ZiTt0GoG_hfjo1J-m5yf73Otwtf-FkWur3B3o9EcHtT1vUGpIhFSlSkMUq0xzlpszapJxqPKEElmJa-NTVyVEWSxUwFYAgI5lhJTPYX0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2a4acd74d.mp4?token=k31n2Qp6YYDhwnH8Y_-3IUpYVx4QxvEN7WIPEk-Ykp1RBi5fiJyvidTXdj4Mrn0tSLVbiIfp8ZCVfA6T4nPrqluF5NI0jjk0BUJGTUcKdneyq7vyGR_5lqaPV6dmX_wM55nUh3dwyAtA_lKJW8OeSN7fCtWYm3BMcTEplu4_yb9S-fO8gYK0Z79fCuPFMnBAtr4gRG9m_o8Yoe2xaukYKnv0zDFCMcxdHkT70jeTOmXRDMlE5CM3ny81P1Z9Tw0om7saNr4yQ9cKnYMxGCIJafgA45cvL6LvKRX2uML3jRxv1el8Rjhh_6M8ldvdaioR_ZfiudKJUa2kQ1RzWyVPe5yCSko7mEzBJS6uJfIb9rhHcve-87kvg_D8inMfNl_6rZ6v5HFkzZUIHq3_b50dHqWhiqjGN_PA5Gzzo3Ye5Zmpt-uglciSkNIV2gmLI5YOVQ0iksQ46pUc2u3Zi_CZldHeB8XsZxdZXpsBJBIiAifA8m1n736xUWCXNN4fZRiCO2lbDzgZ8xo_g395EYifL5MDhI2sY-WwzJqpXBci6KCzAh-zPrZT-_7BzImWZnU7sw-ZiTt0GoG_hfjo1J-m5yf73Otwtf-FkWur3B3o9EcHtT1vUGpIhFSlSkMUq0xzlpszapJxqPKEElmJa-NTVyVEWSxUwFYAgI5lhJTPYX0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از دوستان زحمت کشیده یه آموزش ضبط کرده واسه‌ی اسپوف روی موبایل. چک بکنید ببینید موفق می‌شید بسازید یا نه:
https://youtu.be/spTJKgafNV4</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/3634" target="_blank">📅 13:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3633">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H2ie0ZjYDthg5Xi1wJK4D6oPd8DAxIYsiuaen9sotemtS-eRdUomqOMizS6_Vlf9PkwgghcAWRfLuna_083MHGU9dN3M_yo2q_zIZuBpHDdC4Ywtehrzyp0VD9zJg_22alXVXwcjAt--uRWLD9UQEjeEmPfz_MjYG6VsoOP6Ni9dRODouxnfL4OKsZE6URmBee-An00K4rutIZyvA0bOGFpfeMmzaX_s6k8Ofxdqj0XT1dX6bpvTKosO-t-WetZklhOzwH6R4wU2PrbgZoMhkSlU86Nrh9P16_G9-jMzIuFokMBxHkNkqxJjpAev6-iUxwyTHWOUiAaWOr3tHjB40A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی  از این به بعد می‌توانید از سابسکریپشن WhiteDNS در اپلیکیشن‌های زیر استفاده کنید:  اندروید: FlClash آیفون: Clash Mi  با استفاده از این اپلیکیشن‌ها دیگر نیازی نیست تعداد زیادی کانفیگ را به‌صورت دستی وارد کنید.  ما در سرورهای WhiteDNS بخشی از…</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/3633" target="_blank">📅 13:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3632">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeHM5sHn9dmOiw0mG1kZnuIYZ283_CIKdQXhWs0ww4tSlkS1Xhj8HUS9ypH96dnJ5baG862DSDsqM4vp5xXXy1VgW8UNeGZuyMljoN8RRB4mvtriyZeEU3xZzucrjtCS85BdZZx8t4WVXOQW55OBOdNWtYt5hJbtBX1WLe4sJzsfnADlAnXdUgby33H5B4cs3Zd08m2dr9A98I7rQ5TBHy_xSI553pBBCgcAVRlKBee3uAsHgjjLOgDNRz3qLK6G-FjCN2SktYL-t8UZdhMQT5_hQScniLXiIuwbV_LSXCiGDKvYQ_5WKSpQjgDRx_fk6sIH87vNlU8JIx8SahiyHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی
از این به بعد می‌توانید از سابسکریپشن WhiteDNS در اپلیکیشن‌های زیر استفاده کنید:
اندروید: FlClash
آیفون: Clash Mi
با استفاده از این اپلیکیشن‌ها دیگر نیازی نیست تعداد زیادی کانفیگ را به‌صورت دستی وارد کنید.
ما در سرورهای WhiteDNS بخشی از کانفیگ‌ها را بررسی و فیلتر می‌کنیم. سپس اپلیکیشن موبایل به‌صورت خودکار از بین کانفیگ‌های باقی‌مانده، بهترین گزینه‌ها را انتخاب کرده و به آن‌ها متصل می‌شود.
لینک WhiteDNS Sub برای استفاده در این اپلیکیشن‌ها:
https://sub.whitedns.one/sub/mihomo.yaml
لیست سابسکریپشن ما هر ۱ ساعت یک‌بار به‌روزرسانی می‌شود.
دانلود FLClan برای اندروید، مک، لینوکس و ویندوز
https://flclash.cc/en/download
با تشکر
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/3632" target="_blank">📅 12:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3631">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">MITM-DomainFronting.json</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/MatinSenPaii/3631" target="_blank">📅 01:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3630">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BF2hfkCpEizhGm2qMaRO8zfbtqBeamVp_Q-VEOrXmO59ZLsOcxqPF3fa9S0OMJI6yfX8_grybuu6v3QyUZ0Lk4nvqUIryV7hbT-nCApIM--Ic9oiek2EDwhyblyNQdVgDkYKvFsQzUEmtt8obAjyYyqq_cF2V0uv6pfxGRZ1qFT1eJQNrT1ZfoSaH8nUNdqXuqUM2n3smdj9n2-EL3adqp9OWlmgZkhUIK5J5yTqANxqE7eLgMtAx2hhYLcBTAsgY0-8cC75d2lMBfLynT_9kXISRIiZb0Oqw0FQrG6exfJ2oJ6qsKr8bbMcF37Le40bci62FIaNCYJFbUGr2y7AZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب رفقا آموزش شکست خورد چیزی که می‌خواستم بهتون یاد بدم فعلا بسته هست و پولم حروم شد
😂
خوبه ساعتیه باز میشه خاموش کرد سعی میکنم اگر راه خوبی پیدا شد مجدد یاد بدم اینم بگم که paqet و gfk کار کردن روش که خب قبلا آموزشش رو دادم(ویدئو سوم و چهارم چنل) به راحتی…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/MatinSenPaii/3630" target="_blank">📅 01:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3629">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دو ساعت درگیر این بودم که چرا x-ui بالا نمیاد روی آروان، می‌خواستم یه آموزشی ضبط کنم واستون بعد دیدم ipv4 سرور با چیزی که سنایی به عنوان ipv4 شناسایی میکنه کلا متفاوته و من سعی داشتم آیپی‌ای که وجود نداشت رو باز کنم:| هیچ ایده‌ای ندارم که چرا این بلا رو آورده…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/MatinSenPaii/3629" target="_blank">📅 01:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3627">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aFW87jFDp2gPxVzitx7QPOqBLAeNXQYcxPIvNYP_4FRadeevcUVKrZGAVS3735Vz9OKmNEKT42TYFzZhz5jWcjMdfqfy_ZcvN4szfBwnyqBWFEp5LCTvOngFUQ3qQsx0j2qhlErBcC-UnkdDRJMhmkvrnxlIY5UkvICvRjQnSXhe7tuMoHqUGDREOYf-zQ_gPj3CbnXagzmUrdNm3QWnUwNv-oBJjWyAsSVA028d5HCS7YY6IDc3b1nqKVX--PxD6r9i0oMy61NqOtwrRNksf5vxpj7C5D_hi2dIZc05Us9PtdOUJXtGaT3ZwSv6-O_rIyOi0M5ldRpLNNWnEDjDhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Olh7o_rsqBZcVPd-3pDpxeNkaPTGM3hkuI6PNTaARWw57Pt2qL2G27cs-O5ZEFrcbDrfL1KwQ2B_nOY_pO-A6O9ellwTEdOyh4_dg2Bj_1SmqsaY7rjMq_wNnCYmxhE2YC_lAFwK-guqavbS0dZdHJYma277MDgd3pvlpCD63zdTxBhMJbOyLuJQ35OkXUN3COJe7ba0tyodrc8K-PMwBPGjCowPAN0QrBdhcFv-5coaXafjxQQSOKw0yHyKFE2SwpmT10R9I2gXWWAJwEjM_PCK8GO-phsHK5NLcqZBsLYNlG7X7rIagzu_2lkjAAuk3L4X1w3iXox_nz0l23Xa-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو ساعت درگیر این بودم که چرا x-ui بالا نمیاد روی آروان، می‌خواستم یه آموزشی ضبط کنم واستون
بعد دیدم ipv4 سرور با چیزی که سنایی به عنوان ipv4 شناسایی میکنه کلا متفاوته و من سعی داشتم آیپی‌ای که وجود نداشت رو باز کنم:| هیچ ایده‌ای ندارم که چرا این بلا رو آورده آروان سر سرورا اولین بار بود با همچین چیزی مواجه شدم.
و اینکه با سرور فروغش من تونستم به گیتهاب و اینا ریکوئست بزنم نت بین‌الملل داره. نمیدونم از کی وصل شده</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/MatinSenPaii/3627" target="_blank">📅 23:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3626">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gFjRD2UTmuDRyFnEit68evKKTJKragWo0hEIkdLqise26wXlNX9RufzcATbPBBQOvU0DFO_IA5uIuCo76X9tBdFQXcabGxc076Ugmqhw6UaCb4fd9BCGZhfYTdfxLYWVluCDNloCBYnNvlpfy1Fy_HmWBUb-PKr_qrXLbDaO9gjRTYbbaV_PQb54gzH3xA8A6uDm5QNFBWZha1xHHv3RO3hIvAP9Sa4czFCl9kuUMapdxvdAFD2O66cl9xRAH1BgJFh0iw6N6xmUfa8RtnGn-sU0mTX5zjsxUYvu36Tj5Uhy1kx25W3qKub1CpYGUnyhvlzQlqXHVyBgcpctKZ0P5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرسرعت‌ترین کانکشنی که میشه از یه سرور خارج داشت، Paqet مستقیم روی سرور ترکیه سه دلاری Yotta
😂
با paqctl
سم ران کردم روی سرور
با آموزش اولیه‌ام
هم روی ویندوز ران کردم</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/MatinSenPaii/3626" target="_blank">📅 19:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3625">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ShadowShare منبعی برای پیدا کردن سرورهای رایگان ss   vmess   trojan و...  وبسایت https://shadowsharing.com اندروید https://play.google.com/store/apps/details?id=com.v2cross.shadowshare ایفون https://apps.apple.com/cn/app/shadowshare/id1612647259
📍
آموزش استفاده…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/MatinSenPaii/3625" target="_blank">📅 17:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3621">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShadowProxy66</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mw4lCxFpThlaiKDlWVGIyNI49zr4yyb_kTmGQUqfXDBoz2G30Tdj6y0tcK-NuC4FEZQMi-41p2ptc9PrR1k3dGp326DmgYp1-mzsl7pu-L4wQ2hdMDazmMcPlNtDHN7M95aQKdJZNaLdbJvKPMRll06oKgH9WCgpX4LBzKiihl2_LfZDmLYftrsB1mLz1GsvFTemvVFj96Qj834ZAULsx_KdYdF_COWtdD-VSXKvtqY4FaJYghti1Xhy03Mo9ApG4wTtK9ydCqVkUxbogmgrFr4_xuEUFpFc0o4r25iBECXl3RaTaYx7ydVZKV9Oa_7sDZqedIO_odWu3za7y6yUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TGDuF5OJzAdHjNjXB-ch1tgeMozoi6d9-emAqjjKzSq-h8AgkIPSXRBQycTixLvf9goJLYUOXlnIwKzYl13dzx0WSQH2gHVYtmzcTxjIFeUQ30ekFc1slNV2y5MAONRbi8nIaOTNSmmpBZocivzgtEh_y-IEohXsaF8036g4Ze0letDUPVNz7PO_ybdEaorS_xRhjMVwWy-VM7-901OTsfRjLWAhgXZ9HH869ieDREf7YXRylzirIMWg9YOC_kXAicgMOwitUXYuQe0-xyxQSbHOTG8eodevOhXp4aUEer8BGQhmQLeQAQ7fGKephqdsRd6KJxVr4IQbVjtge2wnwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KiiIm_jW-7tIQ01wpsRmNsTCBAdf-jaTV_HtbfJPk-mr3wA3N-Pshcb4FjWGtutqZNUIaYfa5au8CDphPzUDt-oifO4wHv9FyzPhv-mrNd7JRCTTPLnUwePBs2Re0_yw3YViS9B_hv-lyBHnwLq9YOkL62wL4aKcgdAMZBxQ550ty5ccCG2eOIzZ76eed38rDn3au18LSm9ppzJDk3io0N5zV-VlY2aDaHGp1u65WTUIHiv_n4IXujyFWts2ulsoau6uCTWxXrtS1zTjVKcrdgMa1-d9R3gOXIoljRFa3bWerHw4HufEFf4pc3937RUp0due4C2Fm43kqCWM3U2nUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OmPym-_WXW92uZwFuKX2nn3qPS7eprapp8_HPvh2xvqpcVuW2eS_j58AKkiCFyKUuMdJA4CPWmQgVWll2b66m1qreZ1k_hcFkMLnTRxuQflLwMQBUVPymyCuLNHEUQzBT4zhmEGMOG-M5feyO2oBAMG7ZKH0vps0Rh6d8gBKb8Fs-pfzHMU4IzYKsZEi_rtHyCZeg2cEYJ3rAUwnZ5TkTyPjzp767QPcPwI1fXMg-5D2_aunrgdW07sI952xMGZ6VcIwzDFwIJCuVJt6giltb6E-XBejALp2Sn7SjjTfY2EfF0rMh-edHzZbJH1nV3rDX_T9k_YJVpMdb_RLFGAaPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ShadowShare
منبعی برای پیدا کردن سرورهای رایگان ss   vmess   trojan و...
وبسایت
https://shadowsharing.com
اندروید
https://play.google.com/store/apps/details?id=com.v2cross.shadowshare
ایفون
https://apps.apple.com/cn/app/shadowshare/id1612647259
📍
آموزش استفاده
(توجه داشته باشید کلاینت یا فیلترشکن نیست)
🌐
@ShadowProxy66</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/MatinSenPaii/3621" target="_blank">📅 16:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3620">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DRZ36RHltAn5U_y-Coh5pdpYFmVOXKgw9-jRJtvkb6DYyngVcLgThX1QtlXMo6asiSFRaKiRIQbrAPQA6DjMG7EXOKoCPzbvdIxM3fRl40HLCjjyvdcGVxWqJ5H9nnikpir_ppd6ALGv1ifdf8qLRKLXz3Q5uy9pTVMtQWQ7FqwqZ7BZ1Afotv42XN1O2-9B3IO4bNihLCfCMQcjVeRoeebVCf6IoYiwO4RNByqIGFXO9FFkXcHyAH7hJS7is7N3rc6tQolkV6GIANPoOd-8MBBuj6RRW02u4Asq7KdlaWtt0fVSrbTNQhQf10bqJW8xZxNGkTsr50DdOwu_iuIgAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/MatinSenPaii/3620" target="_blank">📅 12:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3619">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">من الان با این به Spoof وصلم:
{
"LISTEN_HOST": "0.0.0.0",
"LISTEN_PORT": 40443,
"CONNECT_IP": "104.17.89.5",
"CONNECT_PORT": 443,
"FAKE_SNI": "www.speedtest.net"
}
به جای connect ip، میتونید هر آیپی وایت کلودفلری که از اسکنر(
https://t.me/MatinSenPaii/3598
) به دست میارید رو قرار بدید</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/MatinSenPaii/3619" target="_blank">📅 12:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3618">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اگر می‌خواید گیم بازی کنید، می‌تونید از این کانفیگ‌های هیستریای مسیر سفید استفاده کنید: hysteria2://Masir_Sefid@18.159.104.97:443?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/MatinSenPaii/3618" target="_blank">📅 10:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3617">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HxyWxeLaz00jexq7UUcrABPRgW1E3e5qJjyBsFsFtiohp6Q9Hk5Hf_vOy67WG7pkvxKVG3hEniqtRuFozFgnrY-DxuvGRgTOd2dfrfLRl3UjZtCfgS9FZLStYUTj3WaaMW3IGptdYNk2blSZZUXk3zREvMTQVftUg5I48PojWoHkwFk7-w8gOKughH2HI75-trkKM7NrhsGQdXZWkWZXMNmZsymoqzCtcb8_CUeBBZGfJlNKjEILGo-x070ppWacdurnvTxPHU7aL6temM71z1TxxT6h2tse6F-_aTjjWyymoBRpc_qcaBHWDfQGpQNBTWd-fNjKGgYkXAVAmO8hbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر می‌خواید گیم بازی کنید، می‌تونید از این کانفیگ‌های هیستریای مسیر سفید استفاده کنید:
hysteria2://Masir_Sefid@18.159.104.97:443?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:444?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:8880?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:1040?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:4040?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:54040?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
این هم لینک سابش:
https://raw.githubusercontent.com/masir-sefid/Sub/main/@Masir_Sefid.txt
این هم کانالشون:
https://t.me/Masir_Sefid
من با همین کانفیگ‌ها توی کالاف پینگ ۶۰ و گنشین پینگ ۱۰۰ دارم و راحت می‌تونم بازی کنم.
کانفیگ هیستریا هم آموزش ساختش روی یوتوب هست، باز اگر لازم بود یه آموزش ضبط می‌‌کنم واستون. اما نیاز به سرور داره</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/MatinSenPaii/3617" target="_blank">📅 10:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3616">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBUgc-7IZuYyXGSB_F-Y1F9qSJ-2KlAhgxJWPsvsOM-2qN1T57-rj9IQ_mxXhSuqfywQXrv_Q3oGHRHBQxQaGqA8F8R6uPBACUHvOJ54rkz0kCIJUCfMuoh0R-Jz2AgsyswJYynMw8p0laJ02rLn5AjeZk7tc7R3vwUgKNKeKhNdxTdo3gzyDFQU177zp7ZtHX0F9j7tHabWsBCXeHwHgxHkfGXm1SK2u0WESyghDehlSsP8_38doQ-cqg51W-jd1mlHadyugCfAoYpeR0cZEp7tbNM02NmkfS1kVvyudVcM3Nc0m-p6k9qHUCitNOAFd2nSlo778aSvlHok8kh5yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش تبدیل کانفیگ به آی‌پی سفید
از این به بعد برای تبدیل کانفیگ، آی‌پی‌های خودتان استفاده می‌شود.
@WhiteDNS_Installer_bot
مراحل کار:
1. وارد ربات شوید.
2. روی گزینه «تبدیل کانفیگ با آی‌پی سفید» بزنید.
3. کانفیگ V2Ray خود را ارسال کنید.
فرمت‌های پشتیبانی‌شده:
VLESS
VMess
Trojan
بعد از تایید کانفیگ، ربات از شما لیست آی‌پی‌ها را می‌خواهد.
می‌توانید آی‌پی‌ها را به این شکل بفرستید:
8.8.8.8
104.18.1.1:8443
یا با کاما:
1.1.1.1, 8.8.8.8, 104.18.1.1:8443
نکته مهم:
اگر پورت وارد نکنید، پورت پیش‌فرض 443 استفاده می‌شود.
اگر آی‌پی را همراه پورت بفرستید، همان پورت استفاده می‌شود.
مثال:
1.1.1.1
→  پورت 443
1.1.1.1:2053
→  پورت 2053
در پایان، ربات فایل کانفیگ جدید را برای شما ارسال می‌کند که host و port آن با آی‌پی‌های ارسالی خودتان جایگزین شده است.
@WhiteDNS</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/MatinSenPaii/3616" target="_blank">📅 03:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3615">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ErUytrOol-oS8ULKQOxptzjrmIgcmYB0tYHoFaE3dzdQjvz2L-9PwJ-5A1L48g3dBJTtvsAaavbK6i2X9GzAE4RlwYgineUlqMMN3Kmec9N4VYHonXVitVaxNCikJ4zVkFTlGoCdc0qlISft-IRntAeOH94nEYfqnsY_KaJZSvfx4n6ilb8PATPQSgqZoOePmwg5OuBTz5ot4bGgHpVbaCncEBIFfNJAfkT8PE-9wadOGpzQP2mwR_VNm9tcUxSvS5CzciKqrG2HEk1z6UCundIVwIMT_dMh9ilzTPIVDQnHsMCW76CbmMrN8Ukq7oi6CvB6nWCOiYhGTnn-9q_l1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کانفیگ کاستوم دارید(ساب نرمال)، آیپی تمیز رو باید اینجا جای address قرار بدید</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/MatinSenPaii/3615" target="_blank">📅 02:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3614">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑇𝑎ℎ𝑎</strong></div>
<div class="tg-text">https://t.me/MatinSenPaii/3613
خوبیش اینه با این روش میشه رفت و کانفیگ BPB ساخت
برا دوستانی که کلودفلر براشون بالا نمیاد یا نمیتونن وارد سایت اتومیک میل بشن
همه چیز با همین نت بدون نیاز به فیلترشکن کامل انجام میشه
بینظیرید شما
نخبه های ایران.</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/MatinSenPaii/3614" target="_blank">📅 02:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3613">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MITM-DomainFronting.json</div>
  <div class="tg-doc-extra">9.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3613" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">☠️
(اندروید و ویندوز) رفع تحریم سرویس‌های گوگل از جمله میت، جیمیل و درایو بر روی تمامی اینترنت‌ها به صورت نامحدود  این ویدئو، مقدمه‌ی اون روشیه که برای یوتوب گفتم و ویدئوی اون هم پشت این ضبط میکنم و قرار میدم خدمتتون.  لینک داخلی ویدئو: https://up.theazizi…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/MatinSenPaii/3613" target="_blank">📅 01:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3612">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iKoXRlwgAdsIbCBw6VobLN3sOtnIkZL6YwuemH3ZLZRkjwiH2Vq27xhB46rEFpWYDremk3RRi5AkB1-9X8eTTc2BIWEiQcH89QF0PPRbpPdZaRLcupdBCpT-oNgsDwPVWiC-AJbjacwrqjGAABngQKaRu3D8AvRfZBauPtKOLTq1LOQPxIB36LtmW9CXqmJSVUExBlE_uxxfy18SNlZ6q4IvAEAXFr9jZK1liNd81S5Hu0Zu94IIvq1EjIbh1YyDxg9_SxDr5Qyu53397zUxzYzC2Dyn6x51br9K07NB_M5do3nYQ8PTlL8ovILsgQc18EJWxOGBXOWcE2_1sMqWrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیستریا هم روی اینترنت من باز شد</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/MatinSenPaii/3612" target="_blank">📅 01:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3611">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Mr Lou _ Ey Iran | مستر لو _ ای ایران (Rock Mr Lou Version)</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/MatinSenPaii/3611" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/MatinSenPaii/3611" target="_blank">📅 00:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3610">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دوستان اگر از Undefined در نمیاد،
1- صفحه رو رفرش کنید
2- حداقل نیم ساعت صبر کنید
3- اگر نشد، پروژه‌ی Worker جدید بسازید و دوباره مراحل رو انجام بدید</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/MatinSenPaii/3610" target="_blank">📅 00:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3609">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3609" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3608">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/MatinSenPaii/3608" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3607">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/MatinSenPaii/3607" target="_blank">📅 23:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3606">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uJ0nW2fWDs-l_yUyssOYKUYm64I8Q28n-BjSNtfuXiMVJ9fUEg3Y53d_RUpL0hAZvFXpyD0IniFWOxQXmzv4l_DOY-lXQdDCvb2LT1CmhBjTw_Nmo4yS2cAKT4mqIvUfx3N9Gt4ibrjJ0q1fjDPS6xUkj7IuSGNdrDEwvEIGTkDSvB7lOl3yxZnOH6RdIntARx7-pU6Y2oKyXhoImxAaChKSX83ZpvbPttBpIiLrpg48pCDTa8f0LBWhc-_rhkXeobbOOxe9hIrtPJv8jiNYWgrg3Qa63lZ1abVcMX8vBskyVrK8khAKyHXGwQ1iqyc8jXg5Lm4LK_mbLrkTwCtX3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای SNI Spoofing
SNI =
www.speedtest.net
IP =
104.17.148.22
✍️
Kharabam</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/MatinSenPaii/3606" target="_blank">📅 23:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3605">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/MatinSenPaii/3605" target="_blank">📅 22:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3598">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">31.8 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3598" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ورژن 0.5.0 اسکنر
راهنمای نسخه ها</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/MatinSenPaii/3598" target="_blank">📅 22:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3597">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر:
https://t.me/MatinSenPaii/3598
پنل BPB روی گیتهاب:
https://github.com/bia-pain-bache/BPB-Worker-Panel
پروژه اسکنر روی گیتهاب:
https://github.com/MatinSenPai/SenPaiScanner
پروژه رسول:
https://github.com/seramo/v2ray-config-modifier
⭐️
توی این ویدئو این مراحل رو پیش میریم:
1- ساخت پنل BPB ورژن جدید
2- رفع مشکل پینگ -1 کانفیگ‌های آپدیت جدید و درست کردن تنظیمات کلودفلر برای کار کردن پنل
3- استفاده از اسکنر SenPai Scanner برای اسکن آیپی تمیز کلودفلر با استفاده از کانفیگ‌های Worker
4- استفاده از پروژه رسول برای انداختن آیپی تمیز به تعداد بالا پشت کانفیگ
5- توضیح حجم مصرفی و استفاده از این روش روی کلاینت‌های متفاوت
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این متد نیاز هیچ سرور و دانش شبکه‌ای نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/MatinSenPaii/3597" target="_blank">📅 21:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3596">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">جریان اسکن از اول طراحی شد تا هم راحت‌تر باشه، هم نتایج رو همون لحظه ببینید و واستون Save بشه. همینطور یه الگوریتم کوچولو برای اسکن پیاده‌سازی شد برای تشخیص همسایه‌ها، و روند تست و سرعت دانلود بهبود پیدا کرد.  https://github.com/MatinSenPai/SenPaiScanner/…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/MatinSenPaii/3596" target="_blank">📅 19:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3595">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">جریان اسکن از اول طراحی شد تا هم راحت‌تر باشه، هم نتایج رو همون لحظه ببینید و واستون Save بشه. همینطور یه الگوریتم کوچولو برای اسکن پیاده‌سازی شد برای تشخیص همسایه‌ها، و روند تست و سرعت دانلود بهبود پیدا کرد.
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.5.0</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/MatinSenPaii/3595" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3594">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-7lfz2D3dsmS87Qs7tYc8jL8fV2CX4fmUFCdm99-6PxhHPT5eLpeHFTqMrGWTm6p_1dKAbLkaL2H3pRS5jlLgsA8NQNk330WUooMo2-z1BA-9b8qbEZG4W8UZSVMt4eUf7x0r75V07WtMJLJzXnEPYforMKoO_d-Dd_j-yWqDrkXwZ8JWLO_N6FmEajnRWTzsbEeERaDsxi5L7vw_teadR7leR7ByYJG72gGEGfSgNmRzci7jafuBGwPLCggzkoxgRfCFlUyGcblmpNfvtG_F6N6r8EeMVYMRReFosW5PHT4-YrKmG92MLvad5DNsSlzfmIkQ8WHyuwFc2h6_AdEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😊
آموزش V2Ray از صفر تا صد | نصب پنل، ساخت Inbound و Cloudflare Clean IP روی سرور شخصی
در این ویدیو نحوه نصب و راه‌اندازی پنل V2Ray روی سرور را به صورت کامل آموزش می‌دهیم. همچنین با نحوه ایجاد Inbound، مدیریت کاربران، استفاده از IPهای تمیز Cloudflare و اتصال کانفیگ‌ها از طریق اپلیکیشن WhiteDNS آشنا خواهید شد.
سرفصل‌های آموزش:
✅
نصب و راه‌اندازی پنل V2Ray
✅
ایجاد و مدیریت Inboundها
✅
ساخت و مدیریت کاربران
✅
آشنایی با تنظیمات مهم پنل
✅
استفاده از IPهای تمیز Cloudflare
✅
آموزش پیدا کردن و تست Cloudflare Clean IP
✅
آموزش استفاده از اپلیکیشن WhiteDNS برای قرار دادن کانفیگ‌های V2Ray پشت IPهای Cloudflare
✅
افزایش پایداری و کیفیت اتصال با WhiteDNS
✅
تست و بررسی عملکرد کانکشن‌ها
✅
نکات امنیتی و بهینه‌سازی تنظیمات
😊
لینک تماشا در یوتیوب
https://www.youtube.com/watch?v=vVjqNQBUGIc&feature=youtu.be
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور
🎬
کانال یوتیوب WhiteDNS</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/MatinSenPaii/3594" target="_blank">📅 17:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3592">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اینترنت دیتاسنترها هم برگشت بالاخره؟</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/MatinSenPaii/3592" target="_blank">📅 17:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3591">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏دوستان می‌دونستید که این روشن/خاموش شدن Wifi ویندوزتون باگ نیست؟! به‌خاطر فیلترینگ شدید فایروال‌های ایرانه
🤦🏻‍♀️
دلیل و راه‌حلش:
تست اتصال مایکروسافت (NCSI) که فیچر ویندوز ۱۰ به بعده بلاک می‌شه؛ به زبان ساده، به‌خاطر فیلترینگ، ویندوز فکر می‌کنه اینترنت قطع شده و برای همین هی وای‌فای رو خاموش/روشن می‌کنه تا اتصال برقرار شه.
راه غیرفعال کردنش:
۱. همزمان کلید Windows + R رو فشار بده (کلید ویندوز همون لوگو ویندوز روی کیبورد)
۲. توی کادر Run که باز شد، بنویس regedit و اینتر رو بزن.
۳. برو این مسیر:
HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\NlaSvc\\Parameters\\Internet
۴. روی EnableActiveProbing دابل‌کلیک و بعدش Value رو ۰ کن.
۵. سیستم رو ری‌استارت کن و تمام.
دیگه این فیچر غیرفعال می‌شه و VPNتون قطع نمی‌شه :(
البته تا وقتی که غیرفعاله حتی اگه اینترنت قطع باشه، همیشه «Connected» نشون می‌ده.
✍️
گیک‌زهرا</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/MatinSenPaii/3591" target="_blank">📅 16:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3590">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dx8Y7tisovwXt9GLg4jlPrHdA6Vj4JblIYpFcEdfHiuG-FxV08LBwpogR6aZbjgk-r7KLdh3OAcGZqBz7-W49aSH2Qi_KXod3sYwu3L6xjgt6qSEmK3qc_XqTue4JaWJDWZtnC3XUjyjw_IlB9EE03D9jaDPmLkmfj1J0WzSyIP0MMUZpGrjYYQ0CZUhpOJZ4p9U4uZ6-9oXQOibLYI_7zj7IVgCx_99OVPNIlSZeDlqhqkQBBvkb9fNBa9lOLTOujT0BbPiDwaFMHGWuoha6AGre8ERNPubWHK8sLogy_pHtJC6jhP_6EsEygD_xe8_ryLXPq5DzD9yVM6gCBd9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه به این علت باید حتما اسکنر رو توی لیست سفید آنتی ویروس قرار بدید. ویندوز دقیقا این بلا رو سر BPB Wizard هم آورده بود یادمه</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/MatinSenPaii/3590" target="_blank">📅 10:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3589">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">متشکرم از دوتا دوست عزیزی که 105 و 3 دلار دونیت کردن. من تازه ولت رو چک کردم
❤️
مقدارش مهم نیست. کم یا زیادش یه اندازه ارزشمنده و کمک بسیار بزرگیه به من. ازتون ممنونم</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/MatinSenPaii/3589" target="_blank">📅 09:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3588">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.4.0</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/MatinSenPaii/3588" target="_blank">📅 09:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3587">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مشکل bpb هم به کمک دوستان حل شد</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/MatinSenPaii/3587" target="_blank">📅 07:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3586">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fidCs918LvjyxeVfwmfdWLb5mnL02FDOUYpz8YPJOGRUAUw5P9BX3XiVHV_5cD8ZjESQ2_4zw05i2vNoG8WIUtU6UEKtoPazen6-HDYtV3vMhTM6WB8i7-blhNO-wqKF9meAdCbO-7M9SNfvCqIbhZEq9sp8No56waZicSBKqKaaTOHijQLuoK0ruxhlYklauhmxSLhJ09kROFZXN3U7NRRaxpBwC1Nr5fCSnFDLa0t22tPf_ArSVIUXRSKwbycA7dFL1ZJ-Hvc51CrzxMm3Qjs-KDWtw86yGUUPb7ZTw-K9HYGChbc1UCQJ-IvXAyjnGFskywHcLuyXNls5-4h6oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکل bpb هم به کمک دوستان حل شد</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/MatinSenPaii/3586" target="_blank">📅 07:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3585">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YYGGzvs2oJiuyShOAfkDaufZeiL6K3QPR14mTZaXv02n0GrtnFY5lOxGlYruZw2itnQzbTgGkHLM0IxFBkT0TMaMyALl1CyrUW82_ofhFdkD_uAkSDZIClcILqA3IwA9W5ngMjiik79FM9zQlpDgvbQ5sN7NtOuIFF39eipRFZ9-e2lCxkHRfKFxQqfWPpRauqf1mhHwiRm2dLTWAW-ToDRsYx8k50pHRiWKRSzLQtF-Mkuday72IwWv3bXinGZFuVmgvROFiFMJiCA1hY2dF3PULwLcIS_9vNEubsDS542grElGSLWxMEefB3Kx-J3bI3yMeXbDBBMu2luXL9ZAWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگار که عملکرد اوکی شد بالاخره. چندتا دیگه از دوستان هم گفتن
نسخه‌ی اندروید و دارای ui درست و حسابی به احتمال زیاد منتشر نمیکنم چون خیلی درگیری و کار و درس دارم، اما سعی میکنم روش کار کنم با contributerها. فعلا تمرکز روی درست بودن عملکرد بود که حل شد
برای همین prهای فعلی هم reject میشن همه. تا ببینم تست چطور بوده تا به اینجا</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/MatinSenPaii/3585" target="_blank">📅 07:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3578">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">31.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3578" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">V0.4.0</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/MatinSenPaii/3578" target="_blank">📅 06:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3577">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RPdhAqG20SbXStVNvxhtraHP2MIXmXoOk98Z3ZMcAJMVh1nTKUPBQ9V3HUIMeLRszoN6hqfkNWtb7iLWvmn8mpRbdTnpgdPpdsB7rizvvP9r7S52ufdrixpbIkB9Qye0gf1MGJfVXlP6294IyvOhMaR9Y_aU8Arljq00ccfZCWU7zrVyUleeK1jx4g54V0rzrImcbU0lnHtcttgpCKIRooG5fJftGWwseDxUkjcPtc2Dju0sgZBndOyWGaBm6SBvbMJ2A3OzycFPPP0nNoDAZt6qR5PqXiHREiCXPFyFsbEaLALRPhcGOBvssnNMS2mPW_ji7Gr5yj02orFka9-b2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب، فکر کنم یک بار برای همیشه مشکل آیپی تمیز فیک حل شد.
و ممنون میشم تست کنید و بازخوردتون رو بگید. تا اگر مشکلی داره برطرف بشه و بره برای ریلیز</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/MatinSenPaii/3577" target="_blank">📅 06:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3576">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V3IFXC9h1G7fjlGWz8UKt66LA5elOqmf2KdxQxg_H6t1z2PapYh9A1-7yORQUUD3F87Qhy2zTG86tiI4qrIOzLqDjcM_mYPEgfNnOby_94e-DXcgIUc3t62jSLz4MXWRILqjyCz70VB6bwP5eiB09Iy9Hgofo8KqBXGnMeTxGSZmB1thT_7w7lgDdr2OwfpfsxVIVQUtNcLOWDM31XVa5ERliQnitPiYGYE4xxti6n5xShUyyXFFih4DkBmGvdITcqNEKA-_eAsfv8XvblIkp3UXYTQzD6OYIikZkM_ctum6HCalJPuTJZJhTo_29V9DZx9hmBhFidK4ye8msAaOlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پترنیها گویا روی یه متد جدید کار میکنه که به راحتی می‌تونه فیلترینگ الان رو با یه استراتژی جدید دور بزنه.
منتظریم ببینیم تصمیمش این میشه که الآن منتشر کنه، یا بعدا</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/MatinSenPaii/3576" target="_blank">📅 04:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3575">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">دوستان، اگر پیامتون توی دایرکت سین میشه به این معنی نیست که من دیدم و جواب ندادم
🙏
من میزنم بیاد پایین، همه سین میشه
روزانه بالای ۶۰۰-۷۰۰ تا پیام هست و من نمیرسم متأسفانه جواب همه رو بدم</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/MatinSenPaii/3575" target="_blank">📅 03:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3574">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oIuodNwL_Ez-8fG1ZFM1M1txZ-L6lCAVwdXjihGoSgAXZkilxWYw22Tp-tXD500i2w1hetfPvSAU4lsyaByU1w-82VtA2PjPCjAGcXeRZPboBVdeCdzeNgsY7DlVDwQ23lumUMKzFYD1Y-u6iPfMuZC2kE4R_smoeRyLJWwlal9oXohq1kRabhzPp5_k8wd4HsNzAdTIuFcH28HbHYieywWHybcL7NKeu3IbEZaHzG2DpFibEBbMCUc12aBBfKuOTnXxEG8P6kzxik8R_QA_eDv5PdVSbO-x9zwqQjcSkiCaQGgym3ri_yqgXmmI7W7vNBX5_fWynC2E-Kv3DyOmpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشتراک 20 دلاری Cursor اصلا نمی‌ارزید. خیلی خیلی خیلی زود تموم شد با اینکه از مدل‌هایی مثل Opus هم استفاده نکردم
اکثرا gpt 5.3 بود یه کم هم Sonnet
افتضاح زود تموم شدش</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/MatinSenPaii/3574" target="_blank">📅 03:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3573">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مشغول حل کردن مشکل رو اعصاب آیپی healthy فیک هستم. خدا رو شکر یه سیمکارت پیدا کردم که روش دقیقا همین مشکل رو داره</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/MatinSenPaii/3573" target="_blank">📅 03:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3572">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iNFtZh8dOFjfbt7Ax4xNFkFnivjbVsauOh83lRcGTYueVuuL_jugCT6y20PvoFc-sMjhtEc05r3wbQmfQD2JwRhi5gzMKz6HUXUjIe9SmZvhWWhjdnYHqDA3JPgh6SBncikUPWcelC7vjofEW0kRhcwbFe82i14JPqKaCtWZbirK1Awuf_rA-L8zKtNgEwYtiBHSAJZUq1E2j7ZIVIh9WZcy13qCblM1WffOQ7R4Aj6NS61uIhOEe0Z6eAMJyMJ5O4XasrJWH9NilGs5Vp_8NnTnSpN5xWjCdcW4vjaqRruJkk2iYskI5Q5kOv15q2qm62n9HpuSBfLxKs8Sj8OzBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی یه اینترنت عادی هم این شکلیه نسبت. یعنی تعداد آیپی‌های سالم کمه و همین هم شانسیه چون range ها به صورت رندوم انتخاب میشن. حداقل 200 هزارتا اسکن کنید</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/MatinSenPaii/3572" target="_blank">📅 20:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3571">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">V4-Spoof-Configs-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/MatinSenPaii/3571" target="_blank">📅 20:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3570">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اسکنر همچنان مشکل داره متاسفانه روی اینترنت‌های دارای اختلال. دارم روش کار می‌کنم</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/MatinSenPaii/3570" target="_blank">📅 20:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3569">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V4-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">6.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3569" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">V3-Spoof-Configs-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/MatinSenPaii/3569" target="_blank">📅 20:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3568">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ورژن 3 منتشر شد https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.3.0</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/MatinSenPaii/3568" target="_blank">📅 19:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3567">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اگر اکانت جدید می‌خواید بسازید، از BPB استفاده نکنید فعلا. با این آموزش، edge tunnel بسازید:
https://www.youtube.com/watch?v=svYBcv4bSzo&t=618s</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/MatinSenPaii/3567" target="_blank">📅 19:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3566">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ورژن 3 منتشر شد
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.3.0</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/MatinSenPaii/3566" target="_blank">📅 19:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3565">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b9eSlMfksT9dosY0Xdp7TU34vt_D8MSqMopDmw4w7-2IcFiXrcLvBkkYAd6gFd_diQ6pKWkYj3CFgLiiOWYrujImdVNaMiAuPP-txi271cLWult_eyRIXmnysWbLCyTOthbbVZnUx7gskYAx0e6r6mkD4ASgCJa8YHeEN9tr62AcEQiF_-_fGEZtx8eP7pAIOdFHVjEZLzAV6cIv39NTy5GV4OrxFeh8HvnKshtQy_fnhv4q7tmP8Gle7x9GeUMS130P6qKXaEcwPHZDbrBFbQ5d1HpYTgkSceamJH7CDIZGgkzuW_LKC7Jl_MJv7jiXaytE2SAVnnHDILXGasqu-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به لطف دوست عزیزمون abolix، به اسکنر هسته‌ی xray اضافه شد که دیگه پینگ فیک نگیرید. همینطور دارم باگ‌هاش رو می‌گیرم که بتونید راحت استفاده کنید</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/MatinSenPaii/3565" target="_blank">📅 19:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3564">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">به لطف دوست عزیزمون abolix، به اسکنر هسته‌ی xray اضافه شد که دیگه پینگ فیک نگیرید. همینطور دارم باگ‌هاش رو می‌گیرم که بتونید راحت استفاده کنید</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/MatinSenPaii/3564" target="_blank">📅 18:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3563">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dY-Tj7t1gVg3eNpyVWVb-ZsS15i1cWD0Pzt4TzuoUh1z1GH4PmM_h3eF1ZrMh-wEgp4FNtllt6HZ_y6T7WNI4teikq408vS5QDS82V6fSpiIVzB0p-8Fv9PT7paWg-PDUJ3bwc7HfePTMtqvysP1I4ApJCpuYhjPMr59vw0jkte0CJhXDb_d5fQLuqa5KTPIdcoSbWKFslCqFHCWiGjIelRmSL9a8yZ9Nhe7GEbkXwBazToptVT1EyKgtx90IJaG2j59Uz_E_G6s-yotvKg4c34DCfnLA3nupxD2_Kwzfp_Viw0k9lm2CTFUlTrfCYtD95DCp5NqF4CUKoOQ-MrXeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">BPB - Edge - VahidFarid
فقط Edge داره کار میکنه. هر سه هم روی یک اکانت</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/MatinSenPaii/3563" target="_blank">📅 17:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3562">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خب انگار مشکل از BPB بودش. چون الان edge tunnel بالا آوردم کار کرد اما bpb دوتا بالا آوردم روش کار نکرد</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/MatinSenPaii/3562" target="_blank">📅 16:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3561">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">امروز به دوتا نتیجه‌ی مهم رسیدم:
1- روی یه سری از اپراتورها، اسکنر نتایج فیک میده
2- پنل BPB ممکنه از اول تا آخرش ستاپش درست باشه، اما در نهایت کانفیگا کار نکنن. که دارم سر در میارم علتش چیه. فرای از اپراتور این شکلیه. یعنی با یه vpn دیگه هم ازشون پینگ میگیرم پینگ ندارن با اینکه tcping میدن</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/MatinSenPaii/3561" target="_blank">📅 16:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3560">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">همچنان از
@Whitedns_Installer_bot
می‌تونید کانفیگ رایگان دریافت کنید. تا الان 21 هزار نفر دریافت کردن دیروز و حدود 5000 نفر، حجمشون رو تموم کردن(که امروز دوباره شارژ میشه). به زودی مقدار حجم روزانه هم افزایش پیدا می‌کنه</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/MatinSenPaii/3560" target="_blank">📅 13:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3559">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یه آموزش کوچولو داریم امروز</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/MatinSenPaii/3559" target="_blank">📅 12:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3555">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SNfpgQfmcCnQILbuWfSozSDlUVq6Jpt8x29k2s_RLresqseKj4-zXijNYP_Z8USH-1MW26DVzwDfo8S1rDxI08q49mfpd6KUbOgzZex8mXePdLKDAV8vq2-fHx2Rsg4fz33_1WPpEHHhwNbkzlY7331Xmd9aB7XcARnmDb33XaYzF61mhN2eUXNLnEtNrzK54LGSeBzBaI3XjdWx565JmNEzbWOqRPwXsu9XITI3D51AgvO6MJhRQDa_DFalzaksd06X3vAIKK4GVcmYXNOyE3GtuQoI3HUk8OVAMjzj6ZnUgtyUndvJOU3Pmnu-oFaJIspmBD775UQtgl1WuwCP-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Mno2Q883efbNkASPwixidCEtt89Z643EPauud3NyzeTcOCM95xEAjFOAXi3o-cXF0c9NN542IUliN9DccYpxZbG9KlKUuoL3WSdVTPtr3hJJlezB-kJCR0Oa_GTmpFea8MSjmYy8E5_iLvj9eykG1VbGqL4rxvcx1XvvbPyhVl_dD2ddcovJi8BSz_zQNNA-ni_jExtoXkgj_9B5FE_gc8RVOvkWZBoDSKGSr4LM5hNAeOYJ7JGFJa9HQ8yk7CA14zv9YKkVz8qB_gRBAXYx_weLornEUtpO_q33UfOBxmT8ShsiavYOGnJKMfFeVHA4Tgb0YEVKcE8t648vstzE_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DPH-jp2ReAygE9P04-YXrSgKHsb6GaynHTASsdsduUctj7uquXfzw9uxK53loBJpO4ob0AtOIfRGoaXccSGVYgm6JxJMTg87AhO7LEk-22ZsorrG1COyW6OfeJK-T8dE_-p4iaIMT4rbd2woojQQ6pTSuDwDflZaYjDOvGpNLt3_5jSa0kGmvor88MZtTJrF5JSf0qSf06OqQZSiz2-vCnCImT8gX2lbL-sc4u-9VFBFP4UCj_bpqOxxIl3qH-SN3x0IGkB5v6ZqKmF8UshqHdiex5hSWPi7bpCpk5Yi_fp69lE6P9gSBoMsbX_VyW7XmSj-q8uTz-JJiLLskfeoFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P6WqIUT4G9T9kKsaB81bT3R2hxs92hXq9u8oV502_QToTHLaQOGUMgVc-ag_haz3GZfxfWedI9Qgdlfz1I5vki4DYjHf55Z0zIX_5iuuM4qJsY1uo_oD1Ppz4M8H_KaQiVUMn0r7KmeN-__TB_CYWvnV92D_aoAWxyjru-EkAmOr1Z8c254xDZYcMALnkSJPRbFWj00TdCDXFi6LP0w88yDQVVt45ngtcfEUQ_Mums8zlnnZGXX2dY8sEFEpsibk3bPitCHvv60wTMeOSKhFuOcdQ6hceFISOx6te2evDSPbCeTB0VFThXSUCoGhVz4JQntMrmnxNCQDahtHYNMy6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاری که خودم کردم:
1- صد هزارتا زدم بره برای اسکن با ورژن جدید سنپای‌اسکنر. با 200 تا worker کلا 10 دقیقه طول کشید
2- برای من 4 تا آیپی پیدا کرد
3- آیپی‌ها رو با این پروژه‌:
https://t.me/MatinSenPaii/3554
بازنویسی کردم روی کانفیگ پنل BPB(هرچند خودش داره اما این شکلی راحتتره)
(صفر تا صد ساخت BPB رایگان)
4- کپی پیست به v2rayN و ادامه ماجرا
سرعت آپلودا هم اوکی شده الان راحت اندازه دانلودم میگیرم</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/MatinSenPaii/3555" target="_blank">📅 09:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3554">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اشکالاتی که فرموده بودید رفع شد. پروژه با هوش مصنوعی نوشته شده و تمرکز بر سادگی و استفاده‌ی راحت مردمه. اگر اشکالی دارید توی استفاده باهاش بفرمایید و issue ثبت کنید یا اگر خواستید، pr بزنید و مشارکت کنید.
باز هم عرض میکنم خدمتتون که این اولین تجربه‌ی من از اوپن سورس هست و اگر اشکالی به وجود اومد در آینده، پیشاپیش عذرخواهی می‌کنم. سعی می‌کنم که یاد بگیرم و نیاز فعلی رو خوب پوشش بدم و همینطور پروژه رو هم در بهترین حالت ممکن maintain کنم</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/MatinSenPaii/3554" target="_blank">📅 04:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3547">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">7.3 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3547" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">راهنمای ورژن‌ها
تغییرات و بهبود‌ها:
- رفع کامل LOSS% اشتباه روی شبکه‌های محدود و DPI (مشکل اصلی کاربران). حالا تایم‌اوت بین Dial، TLS و HTTP به‌درستی تقسیم می‌شه و پکت‌لاس فیک کاملاً برطرف شد.
- ذخیره خودکار IPهای سالم بعد از Quick Scan و کپی در کلیپ‌بورد با زدن دکمه C
- خروجی فقط شامل IPهای سالم (بدون IPهای مرده)
- فرمت txt حالا ساده: فقط یک IP در هر خط( از
https://t.me/MatinSenPaii/3543
برای بازنویسی کانفیگ استفاده کنید)
- پیش‌فرض‌های هوشمندتر برای شبکه‌های محدود (تایم‌اوت ۵ ثانیه، دانلود ۶۴KB)
- کاهش تخصیص حافظه و فشار GC
- حذف IPهای تکراری در اسکن
- اسکریپت نصب یک‌خطی (شامل آپدیت و Termux برای اندروید)
- بهینه‌سازی منو و تمیزکاری کد
ممنون از همه Contributorها:
ProArash
،
M-logique
،
Mralimoh
،
Hoot-Code
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/MatinSenPaii/3547" target="_blank">📅 03:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3545">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mqvtktGDA8763DLb7QdVSMSJXjcxcNgWHF-GocHhIxdJth6k5SL7RIUKvZKr5CgeUog0UueJSP8HlnMyNqPrzhEQ2yrD0gVNeSdkUB5sHxO46vk0_4TNJp4Wgb4oSiFz3SUCUnHhIgWvwWzwrVDTUcblnxtFoGWlvBKYkJcmRq3TiKiE8ZujNggCwe_DDXEW8XOCWTcCHb9TYK0QZer83R3zS9gavjRGnBmdBwG8DLm7KCtTcU6PIUrYTrfiuHpj5IKTw_PcRwYlSanSNdgk0w9ex6OOBdzWqU7xWDSgb36PlOLmXKq5ZwmmqAECxfn6V2FNR3Zw8ADTgsXuwTJdTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o5z2VMTiYOIRhI6v7FJidxhjW89VIEsLlVAqn0tt2kI_hmKFhhB48XkbeAMIqnlnf8gNm-nZUD3M_mHEBUJS8LtAgRo_YQjU_7QorbTnhzGr4gZmBYWPfdDGe5XgmMr1VAEr36fTQ1Y4wYogKNobulMwk3kgpxo5ReVoOUUkzzoCqMkMTc0QIRB5P72yMhQmGnPDxSxPBR0dwiKoY5JtMRJwCO3hrtakQL3Awcj09fO0kUshc9QbYRz7fQW2asmgT9190dz2ALDLqRtY8JkQuuUTSQ1Re9At4Bkssto8-3Zo4fBlu45REU45pY75-9A3IFiyiKmUKXLawBIdY5tRcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توی آپدیت جدید اسکنر، آیپی‌ای که Healthy هست واقعا بهتون پینگ میده!
همینطور با زدن دکمه‌ی c روی کیبوردتون توی تست لایو، میتونید این آیپی‌ها رو کپی کنید.
یک سری دوستان عزیز متخصص هم برای تست بهتر، روی پروژه pr زدن که دستشون درد نکنه واقعا.
تا دقایقی دیگه منتشر می‌کنم
همینطور که توی تصویر می‌بینید، یک آیپی به من healthy داده شده و همون داره واسم کار می‌کنه با سرعت عالی</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/MatinSenPaii/3545" target="_blank">📅 03:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3543">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TEhXbpyLr5zpt8CRbew3MAoTNrI9wfSO8bJbn4Xn5Kn-WHLfOnmjzDey1TjZiC53JIwyKIE2Uzj0pmWh_aNm9FAhQQ8O9kkwrSCi3AGvij8XnGWci4kNOcVId5RSdBTl88MolWL_nzYuLK9eIqz4Wdsws82FZO232FAhCUdT9wcXqke-OpEDVVdMBOgJhh-2JpaXm-KoHyczmApk5b09CcPPbSkLumvXGtbDg1xHHrWQaCdyQp2dvMbeqh6DRx3-rRrtbPm0rfqGsWvvDGFjw3JrfBZKcFkUjCDBCTbdqJ4lV6ATiHgIP3giL-3kPBC80q4IxJGnQN5k157a1Dxt0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازنویسی یک کانفیگ تکراری با آیپی تمیز‌های متفاوت!
با این پروژه‌ی رسول عزیز می‌تونید این کار رو به سادگی انجام بدید:
https://github.com/seramo/v2ray-config-modifier/
این هم نسخه تحت وب ساده‌اش بدون نیاز به نصب:
https://seramo.github.io/v2ray-config-modifier/
برای حمایت از سازنده، روی گیتهاب بهش استار بدید اگر دوست داشتید</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/MatinSenPaii/3543" target="_blank">📅 03:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3542">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKn-UdJFUdQxnLfpoo5CjPMN-19ANBRzivWLypWATPGjXHV7n7AReRpISkbWdz_LMlYecotyAer99hn6SwnP7ghqzKGN0Dw3xDWNU1Er0OthDweWdb2nGu_XfAwyA82oTJ0-sGJF7zbjWH3xq_rlWhYucgc0GtsBc4h6GFnx301JKqi6-HrWF3CpfzjDGkqaiz6AtmqvV1jPsQamkntECUo3bAWf5O6Eukz2RdKxNyp_-lIv7eSMR9S7jYbhYblP8zakhe7oxQWOhaByBJ5OX-cNPWlE41v059VdiJNP1jnzWr-jWEwOkHPNvy75v6RHwDiYAOoKfj0Y7tuHBJCZQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با شرایط امروز اینترنت، دسترسی به کانفیگ ها برای برخی اپراتور ها امکان پذیر است و برای برخی نه. ولی راه حلی هست که امکان داره کانفیگ هایی که سالم هستند ولی پینگ نمیدهند رو هم به کار بندازید.
با امکان جدید ربات
@Whitedns_Installer_bot
میتونید کانفیگ V2Ray خودتون رو ارسال کنید و اون رو تبدیل به کانفیگ هایی پشت آی‌پی های سفید بکنید.
وارد ربات بشید، روی «تبدیل کانفیگ با آی‌پی سفید» کلیک کنید و سپس کانفیگ V2Ray خودتون رو بفرستید.
تشکر
تیم WhiteDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/MatinSenPaii/3542" target="_blank">📅 01:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3541">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دوستان، ترجیحا همه‌ی پورت‌های توی پنل bpb رو باز کنید. چه tls چه non-tls</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/MatinSenPaii/3541" target="_blank">📅 01:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3540">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دوستان، ترجیحا همه‌ی پورت‌های توی پنل bpb رو باز کنید. چه tls چه non-tls</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/MatinSenPaii/3540" target="_blank">📅 01:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3539">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خیلی باگ‌ها پروژه داره و تا الان نزدیک به ۱۰ تا issue ثبت شده و دوتا pull request
دمتون گرم. همه رو اوکیش می‌کنم تا صبح
❤️</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/MatinSenPaii/3539" target="_blank">📅 00:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3538">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NbQaX5UhPKoYP86DV8w598Zz6GVZwE9Bya02cvTiC0E4s9WKrsB0TU-jeGuJ0Ez8aJlkjc-EPM2e3wBlzBxL4_0qrlO7HMV5tv0nAwYryrVwTkHkdvPct-PjmywV1Ukqopi2K6QfOWDlm2nWUZsBsU8SXroX6f221qPzHUcUK0k_575ujTJXYZZRXzKuYnqj0WiqlWEnYLo5rUE8xnHHk9mkJtkwXBreo1UPpxQ6w1w7znfXxFINAdSlI9oKDA_cvhEWI6DxXtn7UAYFnAiMWiCNgUtpskHSRWDDr5Ea8QDMfQvinlUTiQNuC2vur4jsHBo7keC2jlc2U-eh83wc4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اکثرا جوابای خوبی گرفتن از اسکنر. باعث خوشحالیه و خوشحال‌تر میشم که دوستان متخصص issue ثبت کنن یا contribute کنن
🙏</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/MatinSenPaii/3538" target="_blank">📅 23:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3537">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">عدد سمت چپ اینجا 104.16.90.120 در واقع آیپی ما هستش عدد 2053 هم پورت ما هستش. ابتدا بزنید روی گزینه‌ی ویرایش کانفیگ، و بعدش آیپی تمیز‌هایی که توی کانال‌ها می‌بینید رو، به جای عدد حال حاضر آیپی قرار بدید. پورت رو دست نزنید.</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/MatinSenPaii/3537" target="_blank">📅 23:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3536">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hIBWoa3aWqQrF-ertmX-NTjr_EC6admdBmYJJ7gbAW87I1y7_CwO7kpPmmRYHskOSswn26j5Alz5OOagWciEv7w5udFbXFOO8y-g6wNaw4SFdXqhwEA-FSWJ2s0d1dS9DKzdDaqe5m844qpPKZ5GyYPdX2Ncj_r3gcdvLfQEXSuVDIeDDxcIE2EXt-bzpm5ILsZ9WUZDncOYC7sBi_JLCvShu229lsFhC_v-tjajA2qLH0yPM_C1uSShiX7W_vsDidcchhTGNw0T-X4RGcSS1hccstqX1w4EZaqJeeYb8GdilQgVXvuRmb2P1ue-_eZtvTenheGT6u5S0a9GSDknBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اکثرا جوابای خوبی گرفتن از اسکنر. باعث خوشحالیه
و خوشحال‌تر میشم که دوستان متخصص issue ثبت کنن یا contribute کنن
🙏</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/MatinSenPaii/3536" target="_blank">📅 22:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3535">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vadb5TKtA1acWr9qmw7CpMdM73t0LL8b3V2kbAjPzqwgtcxEiuZ9HiZZMNw8HpKI5STywk19SimCKfDEbevzVXeMLo7kqSHE2EB9CQg7MAezizMtXX1WZX4gfmMKr2bKpUue4udhfSFwq32DYJvkI8pZzSZU6N2hEgk9VAgB2QsnfUt3IA-x-rs5JG3E2PapLWgn42XOVRRmWYliskb12Ho9eMtOgUwq1duuCzFc6DSff_ZX4cWzYogymE9SLZPtM3fmYYaA8yb4A8yMPOKNmZuzTRchwT7S2KZF_X-U6vvGWzFI8H0TF8aHplhelVtKa43qKzOAiYQKNsAe_pb1_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌ها کاملا رندوم اسکن می‌شن. برای همین باید تعداد رو خیلی بالاتر در نظر بگیرید. حداقل ۱۰۰ هزار</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/MatinSenPaii/3535" target="_blank">📅 22:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3534">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">این اولین تجربه‌ی واقعی من از اوپن سورسه پس اگر کم و کاستی داره، ببخشید. صرفا این پروژه رو زدم که نیاز خودم رو برطرف کنه اما دوست داشتم پابلیک باشه و یه پایه‌ای باشه که از ایراد‌هایی که روش گرفته میشه، دانش برنامه‌نویسی و شبکه‌ام رو هم ارتقا بدم
❤️
امیدوارم که این پروژه‌ی کوچولو به دردتون بخوره
به شخصه از اسکنرهای پیچیده‌ای که هزارتا مقدار داره داخلش و نه میشه به عموم توضیح داد نه میشه به راحتی ازشون استفاده کرد، خسته شدم. نیاز داشتم یه اسکنر داشته باشم که به صورت رندوم، به تعداد دلخواه آیپی اسکن کنه و تست کارکرد بگیره ازشون</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/MatinSenPaii/3534" target="_blank">📅 21:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3527">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">7.3 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3527" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">راهنمای نسخه‌ها:
🪟
ویندوز (Windows)
senpaiscanner-windows-amd64.exe
مناسب برای:
سیستم‌های ویندوزی ۶۴ بیتی (بیشتر لپ‌تاپ‌ها و کامپیوترهای امروزی با پردازنده‌های Intel یا AMD).
senpaiscanner-windows-336.exe
(یا همان
windows-386.exe
)
مناسب برای:
سیستم‌های ویندوزی قدیمی ۳۲ بیتی.
🍏
مک‌بوک / اپل (macOS / Darwin)
senpaiscanner-darwin-arm64
مناسب برای:
مک‌بوک‌ها و آی‌مک‌های جدید با تراشه‌های اختصاصی اپل (
M1, M2, M3
و جدیدتر).
senpaiscanner-darwin-amd64
مناسب برای:
مک‌بوک‌ها و کامپیوترهای قدیمی‌تر اپل که پردازنده
Intel
دارند.
🐧
لینوکس (Linux)
senpaiscanner-linux-amd64
مناسب برای:
توزیع‌های لینوکس ۶۴ بیتی روی کامپیوترها و سرورهای استاندارد (Intel/AMD).
senpaiscanner-linux-arm64
مناسب برای:
مینی‌کامپیوترها (مثل رزبری پای ۴ و ۵)، سرورهای ابری ARM، یا لینوکس‌های نصب‌شده روی مک‌های M1/M2.
senpaiscanner-linux-386
مناسب برای:
سیستم‌ها یا سرورهای بسیار قدیمی لینوکس با ساختار ۳۲ بیتی.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/MatinSenPaii/3527" target="_blank">📅 21:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3526">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jzkYF3jpIHnMiQcuaj_fTfhANikncjKPE1B_QSdTTsDlwGqShGaSadPuvFCt7IMO93CUaOxmCZbuJevh8obgglBddZAVnFgCUeYwLp7_XH_SBMVJjxUHm7B7oXa5czYFzY0dsUfQfwa-nlbSS0I9nzkml7TQawnlAlStStfZhKJvXHN_JBQRKZJDbPUmbAhTksSo1Rj9MK_bair5TsOPc-z0oiOp4lvXupVWk-NRSByjuPdk27SGYmZ-2eI8N26D9ItktFDA-2RRbYq-Naq4Ou2aySWy5hjkGUFD1aYvvRbQMGVTZaJ5yifYGOysxQgwW0ZRjGs2VAHdJcqUdxogxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
پروژه‌ی
SenPai Scanner
— اسکنر IPهای Cloudflare
چی کار می‌کنه؟
از شبکه‌ات چند هزار IP از محدوده‌های رسمی Cloudflare رو تست می‌کنه، سریع‌ترین و سالم‌ترین‌ها رو پیدا می‌کنه تا توی کانفیگ V2Ray / Xray / Trojan بذاری.
چطور اجرا می‌شه؟
فقط فایل مخصوص سیستم عاملت رو دانلود کن و اجرا کن.
۴ حالت اصلی:
⚙️
Quick Scan
— سریع: تعداد IP، تعداد worker و timeout رو انتخاب می‌کنی و اسکن شروع می‌شه (پیش‌فرض: حالت HTTP + تست واقعی داده)
⚙️
Custom Scan
— کامل: تعداد IP، پورت، محدوده CIDR، فیلتر دیتاسنتر (مثل FRA)، حالت tcp/tls/http، خروجی CSV/JSON/TXT
⚙️
Test IPs
— لیست IPهای خودت رو از فایل
ips.txt
عمیق‌تر تست می‌کنه
⚙️
Discover Colos
— می‌فهمی از شبکه‌ات به کدوم دیتاسنترهای Cloudflare دسترسی داری
چی اندازه می‌گیره؟
- تأخیر (latency) و jitter
- درصد packet loss
- در حالت HTTP: تأیید Cloudflare + شناسایی colo (مثل FRA، AMS)
- یک نمونه دانلود کوچک — تا گول IPی که «وصل می‌شه ولی داده نمی‌ده» رو نخوریم
نکته مهم:
این یه ابزار
پروکسی نیست
— فقط IPهای خوب رو پیدا می‌کنه. تست نهایی هنوز با همون کانفیگ واقعی‌ات روی Xray/V2Ray هست.
---
🎄
پلتفرم‌ها:
Linux · macOS · Windows
🔗
لینک پروژه:
https://github.com/MatinSenPai/SenPaiScanner
دانلود فایل‌ها از گیتهاب:
https://github.com/MatinSenPai/SenPaiScanner/releases
دانلود فایلها از تلگرام:
https://t.me/MatinSenPaii/3526</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/MatinSenPaii/3526" target="_blank">📅 21:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3524">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cgNlFKl4OSPd8XkLjfNoziQw49gNZyP2Kuc5-CwOfcgMP6OQ9vdbAVfulBgT5h18hMhPPly2_JQpTlfH9GcufnpPxdmQa8XlRegOelDFfF2RJjP68bEo-oF3t0SMKGb46W2zyf7UNIQ9XmwBCAXZOTFALWvSNmEWlVTlMzgK2ipyvGz0WsQg958uLSGflHwZoTbMTESAwmcvAIxHSBCxl9QqAweC38YyoV5FfvW2OkaKxNjNH4IXLYLB7SM10HJYsDe4jJHMj78e6whcgzrUROdfg4WpIs3dCx2RYdp6jYVh8DNXDRXcEYFMVq8tIONTqiostXVTTTBuhaWaPvWP1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nEtHoAIA5b-gAtnjPXjFwIDYn0DjIzqd0PVpeheYFY_r7_6OQ32D7-KH_ku8qXFl9n5247ACqn6_jFCY1F8nI23AWrDhFGuMrBNhyiLgfIGeKRk2607tGGJZbAcXMGwgBJa4XmInZfjxt9Un6jisFLXkPm-Jbb9UXYTaWuwQlMyU-p64qSXbJwZJczIZeH_R6nTZZx5sUxMDCLaufUEiS_fBsdTsu4dkJYsQ8kV6tiLE4KZcdwDlU6j8AZPUif2GcQB_9GwMHxwBwaT3Jy-ZkzWcyEIjxE-qI-MrxHF2TS-uGzkH5u_x2-isfBs0qWagvW8zJDlRvu-yr9jjRqprZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اولین آیپی ای که اسکنر پیدا کرد و داره کار میکنه
مبارکه</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/MatinSenPaii/3524" target="_blank">📅 20:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3523">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آیپی تمیز مخابرات 69.84.182.49</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/MatinSenPaii/3523" target="_blank">📅 19:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3522">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hPupxk-CHX5AVs--03QDKp8jhgpWAMVDHiE0xY0p-UccoPQCCNj4PIXSnPXnLCGzusPwzCif3sAmkw7XtD2XX8Obn04xrd8ZhlEVBr0-mEWT9YNN2LCJDRHWJJCyWUfVUWYIlb8kQ8U94jwZBuJfv90i1UpvdjW50UHScTUa9oj7lpHlBM5YmH3TEq2NDIwuGiXiDb0G_Rpz2vYFiWpDil6vpg5-eLX1gISTk74ddJYZTATr_cOECU9KT7NeEGHbHFdSmUp4YflO6qZfOvqC1sr3TO_fSwVcIWHf5J0ZzId92zl7smTYLx8SbgifdQ8hubKXQY4-BlfneMVuWPDAqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عدد سمت چپ اینجا 104.16.90.120 در واقع آیپی ما هستش عدد 2053 هم پورت ما هستش. ابتدا بزنید روی گزینه‌ی ویرایش کانفیگ، و بعدش آیپی تمیز‌هایی که توی کانال‌ها می‌بینید رو، به جای عدد حال حاضر آیپی قرار بدید. پورت رو دست نزنید.</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/MatinSenPaii/3522" target="_blank">📅 18:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3521">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fP7NHvCA72dd3dKaf4CzVIuSh-a0OVh8CW3I37l_0tha6eAQi0kT50unHuSJ9uJPt1lBA2EGvVGfAx7il6T-3z31dHSbmxsZ1bkVt-0zfVRTxmyVCb3FPtVTREz-iBJJ2xuU-IvF5WXeCBDgytiG2hST4PatYATQWlWRW93jZMjiI7VV5R6mUK_mxio9KdAmAD0QwUqv7vR2ZWc8U6Wgbp7MTymfnukk6vbvVB3eBh0q0baiSUWTbpeHgUJBsWRJ0bY_u03BLO31etE5_bHZ4-u2ciV20tXClEbTvsWsPsodqz_kTqzWEBt4VCglNnSe0N526vnKdp24e_sVg91yuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی تمیز مخابرات 69.84.182.49</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/MatinSenPaii/3521" target="_blank">📅 18:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3520">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آیپی تمیز مخابرات
69.84.182.49</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/MatinSenPaii/3520" target="_blank">📅 17:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3515">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">v2rayNG_2.1.8-fdroid_universal (1).apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3515" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آپدیت آخر V2rayNG fdroid
🔴
🔴
🔴
دوستان برای اتصال به کانفیگ های بات از این اپ استفاده کنید.
@WhiteDNS_Installer_Bot
@WhiteDNS</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/MatinSenPaii/3515" target="_blank">📅 15:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3506">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZpArhtTcqvImMZN2uEM_JvIJPndCRXpPcfVVN0_R8FmJXzwPHJFE5_VIhTAfVGxJOMYkj1VypBSh67F2vrIVSwcle_t_CNVILQIDwys_yx6OSLVTDZenxXqHi0LcSsUNT4DhZOFv84YzIG2BtEMjMlY0f4IgTeOpRJkHI8kY0I2s64hdTFk1Eyi8DUDwg5dcPL97roZH5FP_3lphhoHxNju1GjHB4F_0K8tZpfFM8mP55zfPUsq2xsPcDlK-0Ule1deKKbOmzZ0S08HP9NdyFJzVMJzSi0pfSG78-pjB1GMmrXrCjW3MzMhl5I5LFeK0FY74byEuVwyjMsBaOIvGvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rQY4Kcudj7PrYEWSVa15HEiFGKb02RJ69p_Vc-ajWWbEBJ-HlpngyQfNI8xwXlDax8lZ0icwaShX01tsh9lEHHco2Pp9ebSN7k4bcrtza2kD0-4bp9nfIwToUxtCHW8rWdj9V0ExQbU-Z-oDndaNdGBpTPSOY8UtVYZj4RQqqczKuLyfW52gyA3idHd_krJQlsPtbzubIVUwilosofSjkfTotKt0RsonVP4J6e53zaIWGYBNMcXz2ENlMH4HXhzJd_mJWysCIwvVUbqDORhJhO2Sz7mfb-s67kdrb7z9tmGyddUxxoKlTdzhxRN5VJ_-QKqb9L2Z8y2bOk8aFx595w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aixL0tiaBR2d8s-jNduXtnSj-KUrTr0kP4c5-oQePHMEXwbJst7cUhRxlxdB5aypxP_iCeTrsjRLZ9KLDxlob09WL1oVPmPLhES1EOjODivk2pTkqEy3cRPAGL8VkZtTaNE2TLf-aH10rCP1VvQy3JLqKjnFbb6dNIRT-WLeVK29NKOJ0jANTFpCuUrI-j-BE6EJMI0iUdrDoFfz1OnlRXFK7gpAp6yMpVPS63UwF0CorpdrjDrVl7MekK52kahyLb9DlhrHxF7fPkM2ZvbnFgqHz3En-9iTXbP_gQ8-BuvGBPJnoaIC9CcdosVrvQ6maG_mY41GwczCzy7aJVeC6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EGEIdDZsf2pQ4SgOZX8nJzTgoJ2ya2q0RJyzej_Z3n9nD460G1xrWd6qfREMlfpLzGW48-hZ1H9ZObZ1RFMmShqYgdKVz1kRkKGHOPEtrAKDZzyiuLbPHgJrnO3CqopDrj_MeO68l6_3iKstBs5KSCor7VgPDQ3ivBo5HjDNyWRQdh8fUUdMe2qzHiShnzBfh5Nfg72fbVQahkJ7Bda9NJYOZdiZwNsfjHEtegcziWzVN8CKbZEV4DbLQ-qaxi5ExhMA27ikxZCAodyIS4eWq4BzrXUQqz-XVnz8N65puEXKlZI_vfoZl3cEsPFY8OPSsA_XIiDMM6WFxOxe1M4ZFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VXdDSawbRrioBkjTQWYdfV6jMsITwxRZ1duiNGv1XChS4fNcYFYD3ZKLz-BRUcMavw9xVpLhLgg-9fAL_96Je-oVSFmL4oDhXJ2mplViQus4_Q14Ri6CivAjmlPcVjDMM89fIYwIOwNKqM3v-QeI2LQYlZ0t6_WwWQW9tvqkTZraTkZj2xDyPxUaIX4sCONeWBBMNtIOCvHG2olzBT7HRQDRzDSm9NST0bztvVHO5Wr6JmKFyemC8i9xTWK6L2-iueoYv-gvmHqpPCqF1E6Ak9SmaPIuf8HHsguhowJYV5KZxfncvfZpeoWH7kQFhUarCGdgebZnokSVukDhZ6CEvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FzQzi3rLdRpktpKB9ik5Ku6C6XW-bpEV5X1KaAeNWgPe1EamHXGlRMDKFna_bWhyf2k57YDsWLXFg2gkEmmzC84Hgp3fM5zq6JGqPFno0bLW0IUB2zV-E6fiaSJ2w5MX_IDUvjlu4bk_IsPeqvqUUVFF8iIZJJ7wFocKOOiAR-FUz5ICzc9NQngx82Ww2MnO6a37dFhP_YjS3cXgBDZCAPQH8GfDtdmhcVTDcZ6Khxmn8PNsQwig2avq1HijIMn_uFzaAh2GsJ-BQW9BuMgBiKOyIauqCVBSVR-Nlp6D3sHj0a9RWImHixmYAweYZe0t0vtja4tO9S4VoT7hsey-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U7a4hYukUj0c9oBTeQcEFwuaXCAH7H23gzsWnJ33yLhDI_dkSUnGJpwCubqoNB6a7b2zOjrwpBlSZWzjq8pUeubIVt12f8U3Ut9PWULJveveff1-bJW3Fuo5j5LnO9NMu-Ij7dMu6DK5DuD9NgirAuFeBlWmtSzsPNfHtO7DoEi09OgCPtc1cutdtUcBE-9mWwKBaVwryqo8xNaYytPNJxIixYOmX_fPM-MGEfFL19ZJS_DV2AQSuFpxjGIVs8Wzo6UXtrdI6ZyZ7dGzPXmq-H5Ly5eIZd0noIpdisY3Gv0-dGQTF-fwcISwbgN3TXeBQWHyvq-D8_gm2s-J79oU-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Nw9aan2q_RT9qcBFIXnFSWAt_qQdvb4hukUJi7IOzx0QbT2pwNb7YSDLAMC59nQkx7n_sYusMQLaIkFmxzVQPOgzzzU7ute07-FPj3WyvtHBijT66vvQIiqh4zcCXCGXFPNK32dRF8IJ1xmXWtTIxAxIiLhuGgDRCst2Bmg79wUhOBJXZIO7qAh5hM_Mvk4GnZt2dOO9nULqLZM59OpjMdYWzsgKb2D8gkPR5YHl5MnYKLmfToXBLbOlwnP_qcSO2uxAcwgWLXv-BkBeZIc3yYQN_XocXaN4yBhZYfuUHGmjmzfaETCTNgevECjsPHwY6Nr725tfb6djV3pi0ob2vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l3dtIMAf_qIsDhYxXe4UwFCKguo6-qOuV70hcKZ2aDSS25wx5mkU1enLAQTHzN2oJR3SzIeL8ZZk69CjDurAfntcqUCMHXbASdQITjJ4kF8W8696R028XZ-UuqsbKtlsxAzFebcR0CK0cYBYjnJOyVnaqO_8-qFK1r6nCiKM7YJPuEolYx-ANWo528f3W9oF2BuWYHcFgEstbfsPanCqAEHBMnfqY3QBRPEgamdPE6Yp-Ty3G41-sFT1RevaEaZpF4UUpIi0TgoO6SgMWri10eDMubVH-upIo_1Z7ZsMGp95TVMR2_u3vCccwsLO8BQn8PROxL_WJcHF00txYxS_sA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش قدم به قدم اتصال به کانفیگ های بات
نکته
از آپدیت آخر  V2rayNG استفاده کنید
@WhiteDNS</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/MatinSenPaii/3506" target="_blank">📅 15:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3505">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QC6oDM1nl0WG1izMjAFrJAuVeOFQ1lIAAAFY7zQLM8MHLFsPb3MLTV04Q9xFQxUm0MdsPPlVOe485JLBcDZRXQo6qQ58913s8IKAAcPn_UG6vUHKbnviBxJuJCfl8JbCwp6NzrtLXYlRytOZBZmkSDEwbcedOR5aA8YFjIH10P77V5fP7pq3bovk9rkGoA-9Yaa7gpPy0G3ZkD-P0lzfuLuEmYAKqdy1ObCF5IV7LGH1915TL-iuqdeBrLnpwFmhv1dL73aZz7sVVQpHunk-giXwLXqsdBmUgUMcmJwK_HyfGOzz722LbFT9GH0k5wzPXd6XpS9jCYnptztshuWXcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.
@WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر بشه و پایداری بهتری داشته باشید.
بعد از عادی شدن شرایط، تعداد خروجی‌ها کمتر و بهینه‌تر میشه.
⏳
همچنین بعد از ۲۴ ساعت می‌تونید دوباره درخواست جدید ثبت کنید و کانفیگ جدید بگیرید.
ممنون از حمایتتون
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/MatinSenPaii/3505" target="_blank">📅 15:04 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

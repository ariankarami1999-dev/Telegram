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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 23:41:19</div>
<hr>

<div class="tg-post" id="msg-3653">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شمع Iced latte</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/MatinSenPaii/3653" target="_blank">📅 23:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3652">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/twpJDRfiYs197oIip4i6J9yT2HfrWES-56WtjgItufNjWR2wceJ5gjAh5PIexfD8Lg_Af1FAAbiHPdOkOhcJWK0P3s73KKxUjuPAK_V6CErwWc9OWSv6Jk4etrsea0nbX2Ab73wtI5ji1qmZJ8DEZTrBosSwDWV2yej0CcVWcEdveaOpMk2y6deJ5qnETG4uZLNagVdpoHBmGNEJrrMNnB-9Ul8XHPQ2km6z3FclL0FnjAPUn7ORvZmqHun2gwNf0nb07QxwiOFJuw9I5WSp3LnKDL2Fjo7YiH4e7CevxlgYiCh4CYK2TEyT5MyfJjtrf143MKPvHoLKjw4gnJN8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ارور EOF و 403 گرفتید یعنی گیتهاب هنوز روی اپراتورتون مشکل داره و این یعنی اسکنر نصب نمیشه(باید با وی‌پی‌ان بزنید). طبیعتا وقتی دستور senpaiscanner رو میزنید not found میده چون اصلا چیزی نصب نشده</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/MatinSenPaii/3652" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3651">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux  دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/3651" target="_blank">📅 20:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3650">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KeWhf5oXYz82_-lPIXW38Gna09QLs1HHN_EyIswbxfnCuIWAw_z-4LfKfWPH_beqL_VGccN2zOY3QnOLWKQaVqG9HeA7UDlQeCy0ZgA5H92v7DI54qFvuOmpLDVRi_xSdd_WHtjdjizKVVKkWhAuoRRiAPJG_X0FXPRbt3ozC2lBewc9aW9LBH-TPPwJel0bHc3oYK1aBZEKGqLX2BebLlE96EmWt8svGHhPnyBW9ckzvXueKwjdQ9PHhRhFjd6cVNarR686C0G2GcsahRjWKC_SNfYAq-Ai2ReZUeX_iWNFsyXOVU7Nn-5enIC_-bzby_SfeQzCFeINI7bSvAnOKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر به این ارور خوردید، پروژه‌ی جدید بسازید. اگر باز هم نشد، با یه اکانت دیگه وارد بشید و مجدد تست کنید. توی این ویدئو
https://youtu.be/_aXy8wwyRG8
به همین ارور خوردم و این شکلی حل شد</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/3650" target="_blank">📅 19:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3649">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux  دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/3649" target="_blank">📅 19:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3648">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون متصل بشید</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/3648" target="_blank">📅 18:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3646">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ImftsYJP5C6pKVwrLym9gtiUah1EH2QUU5QzPCaEQ2TK_ByZ6jF-Q2jWKHh7zgSWoJBbYyxzXPiFwVELlyWC0GuX06bDpDMjxFCBXXff6geZfH7Z4sYvkhqfAQn4qjp8Fq1IpY124C1jEfnqYCdBsTlNM7upZS9uWVbtnzHX0P8dTOI9LTBMYqFzSHhhEg54Lkhkcruvbg5SUzREqufasTIxvmO7bhBtyDHJzigEFnoJHHZ7-0I-jXy6SIE80my1WEmcFJISDJJgtQc9CM_IbHcEX5BRYm0wAbaCPvXGpC4N5BLyqhBWfW3MVcWxi4ezMRBfnp6tOhIrCkyqo0jm6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VbxWc9xvDxyijlXLzNLucTmknsC5ojqTtj_nG7Y-gCwob2C0Z0KTbqobj_YmjDredSufHKjM5rMq6ZWwWDEP-Ckjiu_g73KnIgbmEyKte_oMHbkOu8CT7pL9Afp5PUM521rCn2jyXDr_QkhccNLC88VTZhIlTWmsvPiVpCXEYQOZndx3gw-2VJaYj8UyIO3-11lS0vtzUikG59fWpbQAR4snZF53xfMY8vbaJaKAgxLhHsDge4SwIl24i_6K-ZAg_25w_XazsvZjXU3cBX9uzAC6q1H9WIM3uEhu0RcKOV-eW6U0kBOtthvE1q-j0SfvB8sMfJJc8NLXKV5q5LRB7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux  دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/3646" target="_blank">📅 17:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3645">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/MatinSenPaii/3645" target="_blank">📅 17:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3644">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">base.apk</div>
  <div class="tg-doc-extra">11.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3644" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اپلیکیشن RSTA(که به زودی اوپن سورسش رو هم میسازن عزیزان)</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/3644" target="_blank">📅 17:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3643">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-on-Phone.txt</div>
  <div class="tg-doc-extra">350 B</div>
</div>
<a href="https://t.me/MatinSenPaii/3643" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دستورات اسکنر برای Termux</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/3643" target="_blank">📅 17:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3642">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/3642" target="_blank">📅 17:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3641">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vZGNJCgqxYwSnKIahONwA-W9mAT5NjoJZTdP6KjrP4meTJa5zYFm_0OnbiRotmTlifVkDL0dwCwe2BnxsG8xT0CjVuyusAzqmU5vx4N67cH6NkddFi8Y8klNTmc5lX0c7I9vC6lExwGB6jP65b0UEPDDtL3-cDRdG2JS2bOzgozkLbj9C12o6SNXZo1_B_542k6ubZMRaJt_ihk8xRe0UkIOBaWNMw3wmleN3huW4Po2elbWIZe5yXva-KmaufJuo8RNsDtkb-Td9d5trqhXsD-dD4lUGjUl2LKGQkLaLxCoLgaiAKhPww8v8vflif-xEkL-cdx3Y256zUAYrLbn0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ربات از
یـ‌ بـ‌ خـ
عزیز واقعا باحاله. یه نگاه بهش بندازید:
@iNewsSummaryBot</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/3641" target="_blank">📅 16:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3640">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تصمیم گرفتم یه آموزش صفر تا صد ضبط کنم برای عزیزای دلی که لپ تاپ ندارن و فقط یه گوشی اندرویدی دارن
از آموزش ساخت کانفیگ اسپوف گرفته(رایگان)
تا اجرای اسکنر روی ترموکس(سردرد)
و استفاده از اپلیکیشن اسپوفی که این دوستانمون ساختن
یه مقدار طولانی میشه اما دوست ندارم واقعا که بچه‌های اندروید کارشون لنگ بمونه</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/3640" target="_blank">📅 15:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3637">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hmsMsorES70-elLMFFZrNagihAtSSqOfHhJztTpwtX0fKH_W4nJ-KJ91StCZ5xNtUam3L6_qy815mW7N2QDYNGodHlnIcxYVnT1hT2FGvdagihyHkBzuLV30_BVWRpFb-P444WyCoqXjQqrCtJIpNf790G0gS1NQFOWjlJJ_sk1NFJAOi4od6yZ62v_uNfRpWZxqNYKBJnyxOo1gmtJVgz5m0DMO_l_qbCMADjMp-giZ2Kmwln_di_uFayj4ZqB6-XV2ZlXJ0dB8Un34x_L-e-7wmtuPnDIsZ-rsd8IViRt2rYp170IwPuijXKpAK4frtbkl-gDplRGUmMovCfki0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MF122oEu9UIUfVYk3wXt7Rjq3n6tTqkIB7YgfP50iFYcR2tJ4P_qFVnMCZeiCAaBkMCIBPQ06T2Iww0YMAliYr8PzVYK_vDFJzAp1G4QSpzfrOlxBthiFOLzWX8UfqSPXdr07HTHLQr9bf2d8tX4bGAoFHV8YhSlZ0EOeN-fDp0hoMhU8ZI1nom5LK2bl7T9csAGLCJckkH1oIX-ekvcRCYT1ceqxfk4Cg27vg77gXFHWfpCX1TkZ9J5CXxyRbIKRzVhHJO6IVTyruAC3xWM0vLhf4WKf9NOcIgCpoeRQbeJx2eMEdZLUxsU4wBbQC_Yv6P8yMj337bLrJ8UAq5ddw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز راجب اینکه چه شکلی می‌تونید کانفیگ اسپوف شخصی بسازید و روی گوشی چه شکلی برای Config-Json می‌تونید اسکن کنید با ترکیب اسکنر من و پروژه‌ی Shin، ویدئو داریم</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/3637" target="_blank">📅 15:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3636">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">📱
اگر لینک ساب WhiteDNS رو میخواید از گیتهاب داشته باشید، این ریپو هر ۴۰ دقیقه با بهترین سرور ها آپدیت میشه
https://github.com/iampedii/whitedns-sub
لینک ساب برای Clash Party & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
@WhiteDNS</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/3636" target="_blank">📅 13:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3635">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">امروز راجب اینکه چه شکلی می‌تونید کانفیگ اسپوف شخصی بسازید و روی گوشی چه شکلی برای Config-Json می‌تونید اسکن کنید با ترکیب اسکنر من و پروژه‌ی Shin، ویدئو داریم</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/3635" target="_blank">📅 13:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3634">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2a4acd74d.mp4?token=k31n2Qp6YYDhwnH8Y_-3IUpYVx4QxvEN7WIPEk-Ykp1RBi5fiJyvidTXdj4Mrn0tSLVbiIfp8ZCVfA6T4nPrqluF5NI0jjk0BUJGTUcKdneyq7vyGR_5lqaPV6dmX_wM55nUh3dwyAtA_lKJW8OeSN7fCtWYm3BMcTEplu4_yb9S-fO8gYK0Z79fCuPFMnBAtr4gRG9m_o8Yoe2xaukYKnv0zDFCMcxdHkT70jeTOmXRDMlE5CM3ny81P1Z9Tw0om7saNr4yQ9cKnYMxGCIJafgA45cvL6LvKRX2uML3jRxv1el8Rjhh_6M8ldvdaioR_ZfiudKJUa2kQ1RzWyVPe5yCSko7mEzBJS6uJfIb9rhHcve-87kvg_D8inMfNl_6rZ6v5HFkzZUIHq3_b50dHqWhiqjGN_PA5Gzzo3Ye5Zmpt-uglciSkNIV2gmLI5YOVQ0iksQ46pUc2u3Zi_CZldHeB8XsZxdZXpsBJBIiAifA8m1n736xUWCXNN4fZRiCO2lbDzgZ8xo_g395EYifL5MDhI2sY-WwzJqpXBci6KCzAh-zPrZT-_7BzImWZnU7sw-ZiTt0GoG_hfjo1J-m5yf73Otwtf-FkWur3B3o9EcHtT1vUGpIhFSlSkMUq0xzlpszapJxqPKEElmJa-NTVyVEWSxUwFYAgI5lhJTPYX0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2a4acd74d.mp4?token=k31n2Qp6YYDhwnH8Y_-3IUpYVx4QxvEN7WIPEk-Ykp1RBi5fiJyvidTXdj4Mrn0tSLVbiIfp8ZCVfA6T4nPrqluF5NI0jjk0BUJGTUcKdneyq7vyGR_5lqaPV6dmX_wM55nUh3dwyAtA_lKJW8OeSN7fCtWYm3BMcTEplu4_yb9S-fO8gYK0Z79fCuPFMnBAtr4gRG9m_o8Yoe2xaukYKnv0zDFCMcxdHkT70jeTOmXRDMlE5CM3ny81P1Z9Tw0om7saNr4yQ9cKnYMxGCIJafgA45cvL6LvKRX2uML3jRxv1el8Rjhh_6M8ldvdaioR_ZfiudKJUa2kQ1RzWyVPe5yCSko7mEzBJS6uJfIb9rhHcve-87kvg_D8inMfNl_6rZ6v5HFkzZUIHq3_b50dHqWhiqjGN_PA5Gzzo3Ye5Zmpt-uglciSkNIV2gmLI5YOVQ0iksQ46pUc2u3Zi_CZldHeB8XsZxdZXpsBJBIiAifA8m1n736xUWCXNN4fZRiCO2lbDzgZ8xo_g395EYifL5MDhI2sY-WwzJqpXBci6KCzAh-zPrZT-_7BzImWZnU7sw-ZiTt0GoG_hfjo1J-m5yf73Otwtf-FkWur3B3o9EcHtT1vUGpIhFSlSkMUq0xzlpszapJxqPKEElmJa-NTVyVEWSxUwFYAgI5lhJTPYX0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از دوستان زحمت کشیده یه آموزش ضبط کرده واسه‌ی اسپوف روی موبایل. چک بکنید ببینید موفق می‌شید بسازید یا نه:
https://youtu.be/spTJKgafNV4</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/3634" target="_blank">📅 13:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3633">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H2ie0ZjYDthg5Xi1wJK4D6oPd8DAxIYsiuaen9sotemtS-eRdUomqOMizS6_Vlf9PkwgghcAWRfLuna_083MHGU9dN3M_yo2q_zIZuBpHDdC4Ywtehrzyp0VD9zJg_22alXVXwcjAt--uRWLD9UQEjeEmPfz_MjYG6VsoOP6Ni9dRODouxnfL4OKsZE6URmBee-An00K4rutIZyvA0bOGFpfeMmzaX_s6k8Ofxdqj0XT1dX6bpvTKosO-t-WetZklhOzwH6R4wU2PrbgZoMhkSlU86Nrh9P16_G9-jMzIuFokMBxHkNkqxJjpAev6-iUxwyTHWOUiAaWOr3tHjB40A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی  از این به بعد می‌توانید از سابسکریپشن WhiteDNS در اپلیکیشن‌های زیر استفاده کنید:  اندروید: FlClash آیفون: Clash Mi  با استفاده از این اپلیکیشن‌ها دیگر نیازی نیست تعداد زیادی کانفیگ را به‌صورت دستی وارد کنید.  ما در سرورهای WhiteDNS بخشی از…</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/3633" target="_blank">📅 13:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3632">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/3632" target="_blank">📅 12:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3631">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">MITM-DomainFronting.json</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/MatinSenPaii/3631" target="_blank">📅 01:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3630">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IWnuGZYf3gu2NB5LrF9JBzDCuLefj8ZpV40nB0z0kikX3tOOy6P1rKrLVHCKDNK8Wc5ESNuhcCBD2cvybVsOCBEQqzG8GTQYOW3vqpFoT4FtYf2BCnswdnJlHBnQBMrJOLkBXXNx4u1xc9HoBSsBVj7nLjdw2-y82LyhtbFjtu2hUASS1gMu94UXlDV8wjR3g-pxBBI3nurd1rmP3wSlYmjH_c0RREONnGEnIG4n88stMu7OoOC2md-MMamNFNlbHbz4yQjY9X-RMEPu2hWyw_J5vaTGYTCWX9Nq6IMkuBzKi2u5CTluRH7v1KzBCFwcVwSRQkreyuOu-1jILZ75yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب رفقا آموزش شکست خورد چیزی که می‌خواستم بهتون یاد بدم فعلا بسته هست و پولم حروم شد
😂
خوبه ساعتیه باز میشه خاموش کرد سعی میکنم اگر راه خوبی پیدا شد مجدد یاد بدم اینم بگم که paqet و gfk کار کردن روش که خب قبلا آموزشش رو دادم(ویدئو سوم و چهارم چنل) به راحتی…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/MatinSenPaii/3630" target="_blank">📅 01:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3629">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دو ساعت درگیر این بودم که چرا x-ui بالا نمیاد روی آروان، می‌خواستم یه آموزشی ضبط کنم واستون بعد دیدم ipv4 سرور با چیزی که سنایی به عنوان ipv4 شناسایی میکنه کلا متفاوته و من سعی داشتم آیپی‌ای که وجود نداشت رو باز کنم:| هیچ ایده‌ای ندارم که چرا این بلا رو آورده…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/MatinSenPaii/3629" target="_blank">📅 01:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3627">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aFW87jFDp2gPxVzitx7QPOqBLAeNXQYcxPIvNYP_4FRadeevcUVKrZGAVS3735Vz9OKmNEKT42TYFzZhz5jWcjMdfqfy_ZcvN4szfBwnyqBWFEp5LCTvOngFUQ3qQsx0j2qhlErBcC-UnkdDRJMhmkvrnxlIY5UkvICvRjQnSXhe7tuMoHqUGDREOYf-zQ_gPj3CbnXagzmUrdNm3QWnUwNv-oBJjWyAsSVA028d5HCS7YY6IDc3b1nqKVX--PxD6r9i0oMy61NqOtwrRNksf5vxpj7C5D_hi2dIZc05Us9PtdOUJXtGaT3ZwSv6-O_rIyOi0M5ldRpLNNWnEDjDhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Olh7o_rsqBZcVPd-3pDpxeNkaPTGM3hkuI6PNTaARWw57Pt2qL2G27cs-O5ZEFrcbDrfL1KwQ2B_nOY_pO-A6O9ellwTEdOyh4_dg2Bj_1SmqsaY7rjMq_wNnCYmxhE2YC_lAFwK-guqavbS0dZdHJYma277MDgd3pvlpCD63zdTxBhMJbOyLuJQ35OkXUN3COJe7ba0tyodrc8K-PMwBPGjCowPAN0QrBdhcFv-5coaXafjxQQSOKw0yHyKFE2SwpmT10R9I2gXWWAJwEjM_PCK8GO-phsHK5NLcqZBsLYNlG7X7rIagzu_2lkjAAuk3L4X1w3iXox_nz0l23Xa-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو ساعت درگیر این بودم که چرا x-ui بالا نمیاد روی آروان، می‌خواستم یه آموزشی ضبط کنم واستون
بعد دیدم ipv4 سرور با چیزی که سنایی به عنوان ipv4 شناسایی میکنه کلا متفاوته و من سعی داشتم آیپی‌ای که وجود نداشت رو باز کنم:| هیچ ایده‌ای ندارم که چرا این بلا رو آورده آروان سر سرورا اولین بار بود با همچین چیزی مواجه شدم.
و اینکه با سرور فروغش من تونستم به گیتهاب و اینا ریکوئست بزنم نت بین‌الملل داره. نمیدونم از کی وصل شده</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/MatinSenPaii/3627" target="_blank">📅 23:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3626">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gFjRD2UTmuDRyFnEit68evKKTJKragWo0hEIkdLqise26wXlNX9RufzcATbPBBQOvU0DFO_IA5uIuCo76X9tBdFQXcabGxc076Ugmqhw6UaCb4fd9BCGZhfYTdfxLYWVluCDNloCBYnNvlpfy1Fy_HmWBUb-PKr_qrXLbDaO9gjRTYbbaV_PQb54gzH3xA8A6uDm5QNFBWZha1xHHv3RO3hIvAP9Sa4czFCl9kuUMapdxvdAFD2O66cl9xRAH1BgJFh0iw6N6xmUfa8RtnGn-sU0mTX5zjsxUYvu36Tj5Uhy1kx25W3qKub1CpYGUnyhvlzQlqXHVyBgcpctKZ0P5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرسرعت‌ترین کانکشنی که میشه از یه سرور خارج داشت، Paqet مستقیم روی سرور ترکیه سه دلاری Yotta
😂
با paqctl
سم ران کردم روی سرور
با آموزش اولیه‌ام
هم روی ویندوز ران کردم</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/MatinSenPaii/3626" target="_blank">📅 19:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3625">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ShadowShare منبعی برای پیدا کردن سرورهای رایگان ss   vmess   trojan و...  وبسایت https://shadowsharing.com اندروید https://play.google.com/store/apps/details?id=com.v2cross.shadowshare ایفون https://apps.apple.com/cn/app/shadowshare/id1612647259
📍
آموزش استفاده…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/MatinSenPaii/3625" target="_blank">📅 17:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3621">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/MatinSenPaii/3621" target="_blank">📅 16:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3620">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DRZ36RHltAn5U_y-Coh5pdpYFmVOXKgw9-jRJtvkb6DYyngVcLgThX1QtlXMo6asiSFRaKiRIQbrAPQA6DjMG7EXOKoCPzbvdIxM3fRl40HLCjjyvdcGVxWqJ5H9nnikpir_ppd6ALGv1ifdf8qLRKLXz3Q5uy9pTVMtQWQ7FqwqZ7BZ1Afotv42XN1O2-9B3IO4bNihLCfCMQcjVeRoeebVCf6IoYiwO4RNByqIGFXO9FFkXcHyAH7hJS7is7N3rc6tQolkV6GIANPoOd-8MBBuj6RRW02u4Asq7KdlaWtt0fVSrbTNQhQf10bqJW8xZxNGkTsr50DdOwu_iuIgAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/MatinSenPaii/3620" target="_blank">📅 12:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3619">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/MatinSenPaii/3619" target="_blank">📅 12:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3618">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اگر می‌خواید گیم بازی کنید، می‌تونید از این کانفیگ‌های هیستریای مسیر سفید استفاده کنید: hysteria2://Masir_Sefid@18.159.104.97:443?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/MatinSenPaii/3618" target="_blank">📅 10:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3617">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 63K · <a href="https://t.me/MatinSenPaii/3617" target="_blank">📅 10:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3616">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7jViwzM9_0pqLip7Wrx_T02PP7YkSM7Ra8eZV4IRPnZZI0Y6Xz7m_I1H-pH0ZmFGwMbdo86PD_LMIwB5JTayIA0JtWkzQtciYJajJy5JZ1qGtMcbekrQhnZ2DSF6sQpYDKbg3KnQEOQfkJbxT9Tqqvsyd66Gzh1oOQfMb2crtx2KC_5C-49sTsFSF5_lr908hrEi3NDanQtNvJHjbt3ggffacaY_B716R8uD5eStlhg1Qu3G0Ly_WqJSbV2gGW-8CZIWb5xFRvk1jNBs5tM6TNmEDFo7Iv_lRYYeJkPAnM4VyMnLfj6gUTb3VG-4aIqAp2ZF_sC4UAQxem8LILuHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/MatinSenPaii/3616" target="_blank">📅 03:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3615">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K3MgjLPmNWOxqdMp3sbJRb6WlRiZXe3QXsm8QBGTzdnUgF_xiNmEtloitNLwv5__DGMCIEtGSkUJb1wtTEotZgeZaNCbTYcymiYOKT8x2-aFso4ZUazSliyKyl9TndiJNwyG3kxrDnV4P893uM6HbuQdP3Ojfv38V6IUz5aA3BYbV0dkNipHh0kYwTG37Y3PlM9dWuEwZlgs5-UXSpio9eZJkYzdqkJL9IZQ-6ChmwezG2kXso_Z6M2lpYMMipaNv10b1c6sO3J5inJLKgCvS__rxwISb6DYI2izpzxZbVm6D0uqfCcAkeXO-A5qeXqoHipp0-MdFELFKsKvodX9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کانفیگ کاستوم دارید(ساب نرمال)، آیپی تمیز رو باید اینجا جای address قرار بدید</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/MatinSenPaii/3615" target="_blank">📅 02:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3614">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑇𝑎ℎ𝑎</strong></div>
<div class="tg-text">https://t.me/MatinSenPaii/3613
خوبیش اینه با این روش میشه رفت و کانفیگ BPB ساخت
برا دوستانی که کلودفلر براشون بالا نمیاد یا نمیتونن وارد سایت اتومیک میل بشن
همه چیز با همین نت بدون نیاز به فیلترشکن کامل انجام میشه
بینظیرید شما
نخبه های ایران.</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/MatinSenPaii/3614" target="_blank">📅 02:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3613">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/MatinSenPaii/3613" target="_blank">📅 01:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3612">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JAySzL06XtFKfY-9O3Lr766UzqATqmB-V3zp9strI7Y0l52Whay8eHFID55q5rZ_NvxBm6tbkf99Ps_NDkOsaEyw-zQ7uqaZ-Vvcg3I9qM9PozSK1lJU1u7Cyty86j3uTYyfMAzJeoNMOZiOxBLA2LaKsINZCTwKtlgkg6ifA72mBWIK8-wGO16rwq55PgBD-75xQ4SK-cgcRr7G9GNCp-V8tFeSdt-IedAjX3I7lYTrK_JeakEgKnYAtVY9KlC25FzOWfRjcCJyyJQwUVHhrUAdTr3IfhX9TOMhLiA5TC83_QORTo5eL8it4j5vPmLMJECgtUXO1zzi2x6j_QWEcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیستریا هم روی اینترنت من باز شد</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/MatinSenPaii/3612" target="_blank">📅 01:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3611">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Mr Lou _ Ey Iran | مستر لو _ ای ایران (Rock Mr Lou Version)</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/MatinSenPaii/3611" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/MatinSenPaii/3611" target="_blank">📅 00:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3610">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دوستان اگر از Undefined در نمیاد،
1- صفحه رو رفرش کنید
2- حداقل نیم ساعت صبر کنید
3- اگر نشد، پروژه‌ی Worker جدید بسازید و دوباره مراحل رو انجام بدید</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/MatinSenPaii/3610" target="_blank">📅 00:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3609">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3609" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3608">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/MatinSenPaii/3608" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3607">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/MatinSenPaii/3607" target="_blank">📅 23:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3606">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uJ0nW2fWDs-l_yUyssOYKUYm64I8Q28n-BjSNtfuXiMVJ9fUEg3Y53d_RUpL0hAZvFXpyD0IniFWOxQXmzv4l_DOY-lXQdDCvb2LT1CmhBjTw_Nmo4yS2cAKT4mqIvUfx3N9Gt4ibrjJ0q1fjDPS6xUkj7IuSGNdrDEwvEIGTkDSvB7lOl3yxZnOH6RdIntARx7-pU6Y2oKyXhoImxAaChKSX83ZpvbPttBpIiLrpg48pCDTa8f0LBWhc-_rhkXeobbOOxe9hIrtPJv8jiNYWgrg3Qa63lZ1abVcMX8vBskyVrK8khAKyHXGwQ1iqyc8jXg5Lm4LK_mbLrkTwCtX3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای SNI Spoofing
SNI =
www.speedtest.net
IP =
104.17.148.22
✍️
Kharabam</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/MatinSenPaii/3606" target="_blank">📅 23:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3605">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/MatinSenPaii/3605" target="_blank">📅 22:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3598">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/MatinSenPaii/3598" target="_blank">📅 22:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3597">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/MatinSenPaii/3597" target="_blank">📅 21:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3596">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">جریان اسکن از اول طراحی شد تا هم راحت‌تر باشه، هم نتایج رو همون لحظه ببینید و واستون Save بشه. همینطور یه الگوریتم کوچولو برای اسکن پیاده‌سازی شد برای تشخیص همسایه‌ها، و روند تست و سرعت دانلود بهبود پیدا کرد.  https://github.com/MatinSenPai/SenPaiScanner/…</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/MatinSenPaii/3596" target="_blank">📅 19:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3595">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">جریان اسکن از اول طراحی شد تا هم راحت‌تر باشه، هم نتایج رو همون لحظه ببینید و واستون Save بشه. همینطور یه الگوریتم کوچولو برای اسکن پیاده‌سازی شد برای تشخیص همسایه‌ها، و روند تست و سرعت دانلود بهبود پیدا کرد.
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.5.0</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/MatinSenPaii/3595" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3594">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/3594" target="_blank">📅 17:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3592">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اینترنت دیتاسنترها هم برگشت بالاخره؟</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/MatinSenPaii/3592" target="_blank">📅 17:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3591">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 61K · <a href="https://t.me/MatinSenPaii/3591" target="_blank">📅 16:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3590">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dx8Y7tisovwXt9GLg4jlPrHdA6Vj4JblIYpFcEdfHiuG-FxV08LBwpogR6aZbjgk-r7KLdh3OAcGZqBz7-W49aSH2Qi_KXod3sYwu3L6xjgt6qSEmK3qc_XqTue4JaWJDWZtnC3XUjyjw_IlB9EE03D9jaDPmLkmfj1J0WzSyIP0MMUZpGrjYYQ0CZUhpOJZ4p9U4uZ6-9oXQOibLYI_7zj7IVgCx_99OVPNIlSZeDlqhqkQBBvkb9fNBa9lOLTOujT0BbPiDwaFMHGWuoha6AGre8ERNPubWHK8sLogy_pHtJC6jhP_6EsEygD_xe8_ryLXPq5DzD9yVM6gCBd9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه به این علت باید حتما اسکنر رو توی لیست سفید آنتی ویروس قرار بدید. ویندوز دقیقا این بلا رو سر BPB Wizard هم آورده بود یادمه</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/MatinSenPaii/3590" target="_blank">📅 10:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3589">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">متشکرم از دوتا دوست عزیزی که 105 و 3 دلار دونیت کردن. من تازه ولت رو چک کردم
❤️
مقدارش مهم نیست. کم یا زیادش یه اندازه ارزشمنده و کمک بسیار بزرگیه به من. ازتون ممنونم</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/MatinSenPaii/3589" target="_blank">📅 09:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3588">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.4.0</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/MatinSenPaii/3588" target="_blank">📅 09:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3587">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مشکل bpb هم به کمک دوستان حل شد</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/MatinSenPaii/3587" target="_blank">📅 07:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3586">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fidCs918LvjyxeVfwmfdWLb5mnL02FDOUYpz8YPJOGRUAUw5P9BX3XiVHV_5cD8ZjESQ2_4zw05i2vNoG8WIUtU6UEKtoPazen6-HDYtV3vMhTM6WB8i7-blhNO-wqKF9meAdCbO-7M9SNfvCqIbhZEq9sp8No56waZicSBKqKaaTOHijQLuoK0ruxhlYklauhmxSLhJ09kROFZXN3U7NRRaxpBwC1Nr5fCSnFDLa0t22tPf_ArSVIUXRSKwbycA7dFL1ZJ-Hvc51CrzxMm3Qjs-KDWtw86yGUUPb7ZTw-K9HYGChbc1UCQJ-IvXAyjnGFskywHcLuyXNls5-4h6oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکل bpb هم به کمک دوستان حل شد</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/MatinSenPaii/3586" target="_blank">📅 07:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3585">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YYGGzvs2oJiuyShOAfkDaufZeiL6K3QPR14mTZaXv02n0GrtnFY5lOxGlYruZw2itnQzbTgGkHLM0IxFBkT0TMaMyALl1CyrUW82_ofhFdkD_uAkSDZIClcILqA3IwA9W5ngMjiik79FM9zQlpDgvbQ5sN7NtOuIFF39eipRFZ9-e2lCxkHRfKFxQqfWPpRauqf1mhHwiRm2dLTWAW-ToDRsYx8k50pHRiWKRSzLQtF-Mkuday72IwWv3bXinGZFuVmgvROFiFMJiCA1hY2dF3PULwLcIS_9vNEubsDS542grElGSLWxMEefB3Kx-J3bI3yMeXbDBBMu2luXL9ZAWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگار که عملکرد اوکی شد بالاخره. چندتا دیگه از دوستان هم گفتن
نسخه‌ی اندروید و دارای ui درست و حسابی به احتمال زیاد منتشر نمیکنم چون خیلی درگیری و کار و درس دارم، اما سعی میکنم روش کار کنم با contributerها. فعلا تمرکز روی درست بودن عملکرد بود که حل شد
برای همین prهای فعلی هم reject میشن همه. تا ببینم تست چطور بوده تا به اینجا</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/MatinSenPaii/3585" target="_blank">📅 07:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3578">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">31.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3578" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">V0.4.0</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/MatinSenPaii/3578" target="_blank">📅 06:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3577">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RPdhAqG20SbXStVNvxhtraHP2MIXmXoOk98Z3ZMcAJMVh1nTKUPBQ9V3HUIMeLRszoN6hqfkNWtb7iLWvmn8mpRbdTnpgdPpdsB7rizvvP9r7S52ufdrixpbIkB9Qye0gf1MGJfVXlP6294IyvOhMaR9Y_aU8Arljq00ccfZCWU7zrVyUleeK1jx4g54V0rzrImcbU0lnHtcttgpCKIRooG5fJftGWwseDxUkjcPtc2Dju0sgZBndOyWGaBm6SBvbMJ2A3OzycFPPP0nNoDAZt6qR5PqXiHREiCXPFyFsbEaLALRPhcGOBvssnNMS2mPW_ji7Gr5yj02orFka9-b2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب، فکر کنم یک بار برای همیشه مشکل آیپی تمیز فیک حل شد.
و ممنون میشم تست کنید و بازخوردتون رو بگید. تا اگر مشکلی داره برطرف بشه و بره برای ریلیز</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/MatinSenPaii/3577" target="_blank">📅 06:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3576">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V3IFXC9h1G7fjlGWz8UKt66LA5elOqmf2KdxQxg_H6t1z2PapYh9A1-7yORQUUD3F87Qhy2zTG86tiI4qrIOzLqDjcM_mYPEgfNnOby_94e-DXcgIUc3t62jSLz4MXWRILqjyCz70VB6bwP5eiB09Iy9Hgofo8KqBXGnMeTxGSZmB1thT_7w7lgDdr2OwfpfsxVIVQUtNcLOWDM31XVa5ERliQnitPiYGYE4xxti6n5xShUyyXFFih4DkBmGvdITcqNEKA-_eAsfv8XvblIkp3UXYTQzD6OYIikZkM_ctum6HCalJPuTJZJhTo_29V9DZx9hmBhFidK4ye8msAaOlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پترنیها گویا روی یه متد جدید کار میکنه که به راحتی می‌تونه فیلترینگ الان رو با یه استراتژی جدید دور بزنه.
منتظریم ببینیم تصمیمش این میشه که الآن منتشر کنه، یا بعدا</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/MatinSenPaii/3576" target="_blank">📅 04:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3575">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">دوستان، اگر پیامتون توی دایرکت سین میشه به این معنی نیست که من دیدم و جواب ندادم
🙏
من میزنم بیاد پایین، همه سین میشه
روزانه بالای ۶۰۰-۷۰۰ تا پیام هست و من نمیرسم متأسفانه جواب همه رو بدم</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/MatinSenPaii/3575" target="_blank">📅 03:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3574">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bOS6KmSFK20hRbMoCZ5QaVJyrh4015StfT7a5BIqf094I-NG7YrXNDuqFLK57vwon7bE396JOUo8hHWm7l9aslKe8mQwi1fOacAlOpIAFeDKoC6D2pi2Q4xio_4muvzPkue8nDXhVn1opwvtAaUBTr71RZKQi6A3XuztLvVOZN8H1FMUrQTnHKQHWvpg__5BZj3Jl_uXXwYlvnWvhguaJlngF55hOr9LjEwNZjdelZHfudy7QSh9i1ySm86H_7xhqFzN9u3axW64dz4RynwVu8wb30CjYvzMIiNNuVJg08KNG72p4Vm08Dcd1Tgk8_knQD9cF7DXrce5c_MWNcTYIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشتراک 20 دلاری Cursor اصلا نمی‌ارزید. خیلی خیلی خیلی زود تموم شد با اینکه از مدل‌هایی مثل Opus هم استفاده نکردم
اکثرا gpt 5.3 بود یه کم هم Sonnet
افتضاح زود تموم شدش</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/MatinSenPaii/3574" target="_blank">📅 03:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3573">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مشغول حل کردن مشکل رو اعصاب آیپی healthy فیک هستم. خدا رو شکر یه سیمکارت پیدا کردم که روش دقیقا همین مشکل رو داره</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/MatinSenPaii/3573" target="_blank">📅 03:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3572">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iNFtZh8dOFjfbt7Ax4xNFkFnivjbVsauOh83lRcGTYueVuuL_jugCT6y20PvoFc-sMjhtEc05r3wbQmfQD2JwRhi5gzMKz6HUXUjIe9SmZvhWWhjdnYHqDA3JPgh6SBncikUPWcelC7vjofEW0kRhcwbFe82i14JPqKaCtWZbirK1Awuf_rA-L8zKtNgEwYtiBHSAJZUq1E2j7ZIVIh9WZcy13qCblM1WffOQ7R4Aj6NS61uIhOEe0Z6eAMJyMJ5O4XasrJWH9NilGs5Vp_8NnTnSpN5xWjCdcW4vjaqRruJkk2iYskI5Q5kOv15q2qm62n9HpuSBfLxKs8Sj8OzBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی یه اینترنت عادی هم این شکلیه نسبت. یعنی تعداد آیپی‌های سالم کمه و همین هم شانسیه چون range ها به صورت رندوم انتخاب میشن. حداقل 200 هزارتا اسکن کنید</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/MatinSenPaii/3572" target="_blank">📅 20:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3571">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">V4-Spoof-Configs-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/MatinSenPaii/3571" target="_blank">📅 20:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3570">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اسکنر همچنان مشکل داره متاسفانه روی اینترنت‌های دارای اختلال. دارم روش کار می‌کنم</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/MatinSenPaii/3570" target="_blank">📅 20:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3569">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V4-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">6.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3569" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">V3-Spoof-Configs-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/MatinSenPaii/3569" target="_blank">📅 20:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3568">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ورژن 3 منتشر شد https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.3.0</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/MatinSenPaii/3568" target="_blank">📅 19:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3567">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اگر اکانت جدید می‌خواید بسازید، از BPB استفاده نکنید فعلا. با این آموزش، edge tunnel بسازید:
https://www.youtube.com/watch?v=svYBcv4bSzo&t=618s</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/MatinSenPaii/3567" target="_blank">📅 19:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3566">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ورژن 3 منتشر شد
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.3.0</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/MatinSenPaii/3566" target="_blank">📅 19:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3565">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b9eSlMfksT9dosY0Xdp7TU34vt_D8MSqMopDmw4w7-2IcFiXrcLvBkkYAd6gFd_diQ6pKWkYj3CFgLiiOWYrujImdVNaMiAuPP-txi271cLWult_eyRIXmnysWbLCyTOthbbVZnUx7gskYAx0e6r6mkD4ASgCJa8YHeEN9tr62AcEQiF_-_fGEZtx8eP7pAIOdFHVjEZLzAV6cIv39NTy5GV4OrxFeh8HvnKshtQy_fnhv4q7tmP8Gle7x9GeUMS130P6qKXaEcwPHZDbrBFbQ5d1HpYTgkSceamJH7CDIZGgkzuW_LKC7Jl_MJv7jiXaytE2SAVnnHDILXGasqu-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به لطف دوست عزیزمون abolix، به اسکنر هسته‌ی xray اضافه شد که دیگه پینگ فیک نگیرید. همینطور دارم باگ‌هاش رو می‌گیرم که بتونید راحت استفاده کنید</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/MatinSenPaii/3565" target="_blank">📅 19:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3564">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">به لطف دوست عزیزمون abolix، به اسکنر هسته‌ی xray اضافه شد که دیگه پینگ فیک نگیرید. همینطور دارم باگ‌هاش رو می‌گیرم که بتونید راحت استفاده کنید</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/MatinSenPaii/3564" target="_blank">📅 18:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3563">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dY-Tj7t1gVg3eNpyVWVb-ZsS15i1cWD0Pzt4TzuoUh1z1GH4PmM_h3eF1ZrMh-wEgp4FNtllt6HZ_y6T7WNI4teikq408vS5QDS82V6fSpiIVzB0p-8Fv9PT7paWg-PDUJ3bwc7HfePTMtqvysP1I4ApJCpuYhjPMr59vw0jkte0CJhXDb_d5fQLuqa5KTPIdcoSbWKFslCqFHCWiGjIelRmSL9a8yZ9Nhe7GEbkXwBazToptVT1EyKgtx90IJaG2j59Uz_E_G6s-yotvKg4c34DCfnLA3nupxD2_Kwzfp_Viw0k9lm2CTFUlTrfCYtD95DCp5NqF4CUKoOQ-MrXeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">BPB - Edge - VahidFarid
فقط Edge داره کار میکنه. هر سه هم روی یک اکانت</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/MatinSenPaii/3563" target="_blank">📅 17:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3562">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خب انگار مشکل از BPB بودش. چون الان edge tunnel بالا آوردم کار کرد اما bpb دوتا بالا آوردم روش کار نکرد</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/MatinSenPaii/3562" target="_blank">📅 16:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3561">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">امروز به دوتا نتیجه‌ی مهم رسیدم:
1- روی یه سری از اپراتورها، اسکنر نتایج فیک میده
2- پنل BPB ممکنه از اول تا آخرش ستاپش درست باشه، اما در نهایت کانفیگا کار نکنن. که دارم سر در میارم علتش چیه. فرای از اپراتور این شکلیه. یعنی با یه vpn دیگه هم ازشون پینگ میگیرم پینگ ندارن با اینکه tcping میدن</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/MatinSenPaii/3561" target="_blank">📅 16:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3560">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">همچنان از
@Whitedns_Installer_bot
می‌تونید کانفیگ رایگان دریافت کنید. تا الان 21 هزار نفر دریافت کردن دیروز و حدود 5000 نفر، حجمشون رو تموم کردن(که امروز دوباره شارژ میشه). به زودی مقدار حجم روزانه هم افزایش پیدا می‌کنه</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/MatinSenPaii/3560" target="_blank">📅 13:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3559">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یه آموزش کوچولو داریم امروز</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/MatinSenPaii/3559" target="_blank">📅 12:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3555">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/MatinSenPaii/3555" target="_blank">📅 09:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3554">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اشکالاتی که فرموده بودید رفع شد. پروژه با هوش مصنوعی نوشته شده و تمرکز بر سادگی و استفاده‌ی راحت مردمه. اگر اشکالی دارید توی استفاده باهاش بفرمایید و issue ثبت کنید یا اگر خواستید، pr بزنید و مشارکت کنید.
باز هم عرض میکنم خدمتتون که این اولین تجربه‌ی من از اوپن سورس هست و اگر اشکالی به وجود اومد در آینده، پیشاپیش عذرخواهی می‌کنم. سعی می‌کنم که یاد بگیرم و نیاز فعلی رو خوب پوشش بدم و همینطور پروژه رو هم در بهترین حالت ممکن maintain کنم</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/MatinSenPaii/3554" target="_blank">📅 04:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3547">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/MatinSenPaii/3547" target="_blank">📅 03:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3545">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sqdB2UGzCNgKWxs0E0NSXGCvF96ZDfM9SVGnEf6gziUkHilT-CttS2C4YW0Sf74piDlEbbTFXgVkY-kIM84rW1_9l-2Zalv19rz4AauK75vgR82ivUOFyLjHrhpHUoWTdMZfnmfqRXgzPXsHDOqe-D1FHmTgFbz21JlBERtThcVkJrvYoeZOC2jJeH4VH5F33c0Ae326t-tX3IRVao2A7TQTe4ZjD8cl08biBucTSFXxk4l4ROC3ucn0eEWPKs1eGGYEuEva51FazWg_TIe3Q9AS8Rw6AeWG-xDB6WO9gsTxDAmyLCCwg9Ihp6yCntr0x61QkqXKnFJzk0zyE3s4ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vaz6QC3_CfKWsStVtIx3Bt1agvObQ0mSchA7vtXHmYRLb1NgsXTzvjMufBWIFWS5VPa8FBuy8CM9Hn-LKU3enBCwP__cQ9TA8ZgfQrytMHNLOOfYcc7wq_IrVSzsGYJqgUgMbWiDCEjTrBPtzGScZLouKquLE2dp9mjph5DRR0YeatdNWOaggQ2oFlI9JjFhdvs4DV-SsnA7K1xqlXNGuGaU4nJ3dZ2VmRwgXvmIor3qmLUqMVmNHVd-e1VaOLeN-K4nCZg1k3w59hRFw84VzAxvdSnxSWkooz-PEEEKM5vgl1rtWOIdhQyxQEbLSQEJLFHrRl__xqq7XcKY6oJRKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توی آپدیت جدید اسکنر، آیپی‌ای که Healthy هست واقعا بهتون پینگ میده!
همینطور با زدن دکمه‌ی c روی کیبوردتون توی تست لایو، میتونید این آیپی‌ها رو کپی کنید.
یک سری دوستان عزیز متخصص هم برای تست بهتر، روی پروژه pr زدن که دستشون درد نکنه واقعا.
تا دقایقی دیگه منتشر می‌کنم
همینطور که توی تصویر می‌بینید، یک آیپی به من healthy داده شده و همون داره واسم کار می‌کنه با سرعت عالی</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/MatinSenPaii/3545" target="_blank">📅 03:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3543">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LuSRc0NqHH9SEJDLU42UngS0fo0MLYibEaVcRfxUca0IooOcaJ3Cze17N8BVYAoWchSB_U2v06V3bKJOCSqnVlJddBGBOEY6gBTCs_5U-CLCtFFkxB2HFlBU0yE3QSSJ5XOIgPgjX4vq-OEmTMNl72mGNw4AH0phm0xugNczcooDxRMdVd5cw7V5N04Gk3iitNmaW9X5-YYpLV2M1_wORXDCL8YZHvYWtcWll781-quzVBkgtFhd1RTA1rIYhIl8VPRgCjEkKB8Lenj7AncajxcUa_rWc9o5nYCoy4HrRW0BjJymTA2Ojsfjf8UE9aaeaV4NL6pfEXmhFK57O0alcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازنویسی یک کانفیگ تکراری با آیپی تمیز‌های متفاوت!
با این پروژه‌ی رسول عزیز می‌تونید این کار رو به سادگی انجام بدید:
https://github.com/seramo/v2ray-config-modifier/
این هم نسخه تحت وب ساده‌اش بدون نیاز به نصب:
https://seramo.github.io/v2ray-config-modifier/
برای حمایت از سازنده، روی گیتهاب بهش استار بدید اگر دوست داشتید</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/MatinSenPaii/3543" target="_blank">📅 03:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3542">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYTs6J9q8JACFOKlppB-vTMG9t_YunyNewa115gaTyEcL78fSRmY7ZZBJVOguA0jwK3WCjyocmIboJ9PgH0-RTWcBm_ejO5SPCn-IoVV3FOaC5Gi9m_oOX5dCffcLrzyP39AsG8OUS5psO5TJVtxBl2caEFqKl868SvF6YQtzIrwc0Rr-fKPZc1A9lws1fORFiZG5B04A5MUJ1GpufYRVF8nYDwUfMI52CrOwz0AYHZByybUsXI8-3SogHKMvMumbjC1aaYfb7LqnLMDJfpE3fwxDUSo3shS-NDo0IKMe7LOibLuXWxsYqzMy_o1_J4hVWzra1n_HpkNeJqoNBA5gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با شرایط امروز اینترنت، دسترسی به کانفیگ ها برای برخی اپراتور ها امکان پذیر است و برای برخی نه. ولی راه حلی هست که امکان داره کانفیگ هایی که سالم هستند ولی پینگ نمیدهند رو هم به کار بندازید.
با امکان جدید ربات
@Whitedns_Installer_bot
میتونید کانفیگ V2Ray خودتون رو ارسال کنید و اون رو تبدیل به کانفیگ هایی پشت آی‌پی های سفید بکنید.
وارد ربات بشید، روی «تبدیل کانفیگ با آی‌پی سفید» کلیک کنید و سپس کانفیگ V2Ray خودتون رو بفرستید.
تشکر
تیم WhiteDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/MatinSenPaii/3542" target="_blank">📅 01:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3541">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دوستان، ترجیحا همه‌ی پورت‌های توی پنل bpb رو باز کنید. چه tls چه non-tls</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/MatinSenPaii/3541" target="_blank">📅 01:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3540">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دوستان، ترجیحا همه‌ی پورت‌های توی پنل bpb رو باز کنید. چه tls چه non-tls</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/MatinSenPaii/3540" target="_blank">📅 01:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3539">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خیلی باگ‌ها پروژه داره و تا الان نزدیک به ۱۰ تا issue ثبت شده و دوتا pull request
دمتون گرم. همه رو اوکیش می‌کنم تا صبح
❤️</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/MatinSenPaii/3539" target="_blank">📅 00:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3538">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KSKigpYJioKBkxId-1ECrq79_xjQvsQ77iQZoQpf22VKE3xY0u3Umz0EcrrvZ1HEi8nTFcBhSsIaMmJ2vH7ne-6AvQ5_FDdF8KVIxrygVyyyz8hl_DwMt5VNWqnGUeAffLdaNYyxaMjl8_6hJu_IJLer5Q1ZZY0R971EpuZAHikuQX74V3cuCC65KdG0-nac_4W15r-e456mo-zQje5hzEtpK1YE7VsLHSjrLTWphmRosS6YOved2hB3-caXVJVeqf002HqYukd9DWSq27G_jXLJivEQPXWECWRvYRKYYsZ-rVfx5GRIolf7XKshd6eos_FOX9xnIFKpZ8gwUgTxMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اکثرا جوابای خوبی گرفتن از اسکنر. باعث خوشحالیه و خوشحال‌تر میشم که دوستان متخصص issue ثبت کنن یا contribute کنن
🙏</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/MatinSenPaii/3538" target="_blank">📅 23:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3537">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">عدد سمت چپ اینجا 104.16.90.120 در واقع آیپی ما هستش عدد 2053 هم پورت ما هستش. ابتدا بزنید روی گزینه‌ی ویرایش کانفیگ، و بعدش آیپی تمیز‌هایی که توی کانال‌ها می‌بینید رو، به جای عدد حال حاضر آیپی قرار بدید. پورت رو دست نزنید.</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/MatinSenPaii/3537" target="_blank">📅 23:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3536">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hSQj4L6pCNs0WaI1VhY6dGqszSCNWz8eWhXNZDu-FILu_B-_nMnPABKmKYwqWzWbgY9LNtGO-dpb03M9gwkZ4nWTvq0fHzxh9L-D09K7UoQfnP0ESKSXAng72ORTNVuZWO4A-ZPBjVyqXd4nZi2O0m_WSHH69XHuLcSDAIXzyMH8obb-eyddPCVHAqCAlefBuUYGNzAa8k1eHZg6-tYLwNsDVzXF2Ol2FD1E3Z1kEmV0XZTQ6R114M_BlQ3t-UQxqNNV5l9nABv6XwZmTG5EeTKMuQ7SyJqdyuZ2JU-wMUVuhZbtq1L4rX3olEaP6wM61LSpV63HH9XeEAVS_gK19w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اکثرا جوابای خوبی گرفتن از اسکنر. باعث خوشحالیه
و خوشحال‌تر میشم که دوستان متخصص issue ثبت کنن یا contribute کنن
🙏</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/MatinSenPaii/3536" target="_blank">📅 22:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3535">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pQuA_vTsm8CgNILNpnc1ZHtoFYyKalq2dOlfmx1rO_c0iG5jQ3nfOxr42taUiKQj1jPquwCyKCL3JznO1U_JI6nCCSMZSH6PCpxZtX8RIodHpZZkL0dmv3yjihTzIVzSGnkvSUOPjIiruTVIp1y69w4HmcepSWEYeOfh3FZ4g6QYJGuyVFQRXygGdtax_0a973L5XvJt-6zCBNAa3RDCK14ZrCohUIBsojGfckO9kHoub7NoTuEgRmsTfIbkSQofZkw45HWiiOEKhcqDSLLR6euxJPwP4iGDaPkRqXH3hDRjehAv1g8QP_hA5gWHbJpSq4dYTCYdSyHv3vnVsCJ4Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌ها کاملا رندوم اسکن می‌شن. برای همین باید تعداد رو خیلی بالاتر در نظر بگیرید. حداقل ۱۰۰ هزار</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/MatinSenPaii/3535" target="_blank">📅 22:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3534">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">این اولین تجربه‌ی واقعی من از اوپن سورسه پس اگر کم و کاستی داره، ببخشید. صرفا این پروژه رو زدم که نیاز خودم رو برطرف کنه اما دوست داشتم پابلیک باشه و یه پایه‌ای باشه که از ایراد‌هایی که روش گرفته میشه، دانش برنامه‌نویسی و شبکه‌ام رو هم ارتقا بدم
❤️
امیدوارم که این پروژه‌ی کوچولو به دردتون بخوره
به شخصه از اسکنرهای پیچیده‌ای که هزارتا مقدار داره داخلش و نه میشه به عموم توضیح داد نه میشه به راحتی ازشون استفاده کرد، خسته شدم. نیاز داشتم یه اسکنر داشته باشم که به صورت رندوم، به تعداد دلخواه آیپی اسکن کنه و تست کارکرد بگیره ازشون</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/MatinSenPaii/3534" target="_blank">📅 21:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3527">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/MatinSenPaii/3527" target="_blank">📅 21:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3526">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U2tD7FBo9AGDVrIm_1rLykms4jORX3ByjX01ZqS_uyES2pJngiEQlWarj-r8NRmybzyUHDNPYJEaXWAAKIuqPc6vhlzMsA_Jh159ia498jYwKDwCM5e6BXf3g4D0Cg5doAYVPLjRWbq3YgsDIagtqEShnKqKqP2RinmtRcb3MdvYQ-MsbCrdJ_tZAjeGcV28zdqbfNzZUNwD8y5F26VXAlb9s6bVVOHXfdIvoL_hQva_JXGP4Cr9owf6MhCwzctZEgSjWKc1_U_Qc4FOwr-8fPpXAx8P53y0yvpTscip6jwTXTZUFIAH1e5OQN_sRgf_HkzcAJNMVhAabZmUlYuK6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/MatinSenPaii/3526" target="_blank">📅 21:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3524">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IXvfwXo2xDIS0m0StzSi8fhqrf4HeLxoHWr1Zuo8v7aevefes9RwT6UHjGplX5dTCzN1qHfaD87zg3IFJNzqKu3GWvaPCUfQd4KldAKAhlAvrmwPA9f5Hvt1UskmS9LUlh9mmMu1H1pmI_oY8XK7cpOhL24ErfvEZJ_3nBPLVbMpMZmeIzlO_v_zEq4aQ4dX0gR2pLQ8KeJVHEUR2f2-RSWMePYBT2j9hRJyXhKFtoOFnwgcTSdbIfF-oeRmHA3D73isA_6EVqXiI2gr56TMn18gmsEdvGll1NzPshrXVY2DEDq3o7POyIsvRWdnQUJk5YDwJuUcxTayP-8znS6tcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NsDrh6HJC-ZYrvVmO9uCYUuk0DWvQK_vXj3B1X-s26wPn-e3kNl71BusEgJwD_k_-I2W4bH90OGscahQrzLhdUxff3BmwI8hkBFUzwt2rJcSdN2qTdlNDYG-wBm2DEIfJ4_X_W6dIxUdP3r0PW-3fLShmSPQilkDoBJVTgP6A6davk8a3MG4dn6FX1DlUQcXN4Bm9Wztyc_1aMjrzdUkOD-Cl7Li_BTy1cIvZjywJdhfdm00ZIMe9-lbEZd991KVIMvx3OH2CSQICTTNUw3pECQCnneUrz5jrdT4SlCvaaTYq7IRJTGacxWoTxajQiWICrRprDdJn1fGl9GRxE-6sQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اولین آیپی ای که اسکنر پیدا کرد و داره کار میکنه
مبارکه</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/MatinSenPaii/3524" target="_blank">📅 20:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3523">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آیپی تمیز مخابرات 69.84.182.49</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/MatinSenPaii/3523" target="_blank">📅 19:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3522">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XleLFu_mbZkKxmN000jSUQ9cn4z7QD8lvLkc7NmvvQ9XsdHW8aBbfXQ4m4hXzaToCkQ9tgtHighU1aXkb4qUgsVe1e5P_GRrCj44_-8i58TzjoBkp2_LwUAsiOMbGKHhCww-9wnJdG0AhuNvbTdbOqRDTRaXEdgNENktoX0_GEFKCFW6l8HdSCqm3SFQ2y1gd8R_3oi4JwEJREp1iVtIF2oPdC7JT5HSlwR5gopo2aZKh2Leh4KOrL4QkXz5WMkwF3MrPEwG1JGgF2O0OZmOKGkWIEnL_24Bipq1ndOph4m60QTaZif4vpS5qGhbw6qE-8ZZxTG5LeMAkoUMAb4Fvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عدد سمت چپ اینجا 104.16.90.120 در واقع آیپی ما هستش عدد 2053 هم پورت ما هستش. ابتدا بزنید روی گزینه‌ی ویرایش کانفیگ، و بعدش آیپی تمیز‌هایی که توی کانال‌ها می‌بینید رو، به جای عدد حال حاضر آیپی قرار بدید. پورت رو دست نزنید.</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/MatinSenPaii/3522" target="_blank">📅 18:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3521">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dTGzwEUeTddEU6Xvrg7MZ-rS6TcdlIoSuBmnCibhVzsCCDPY1qxhSivvYQ9ogGR-0kM95QTdsikEnfFb6vShFwwBOEdNYBBdaVFTovzb54KDVfUc-ImhcM3ov-bqzYTbPpsDyAgX87_K5QfCs_mfP2Cv0NJsq30oAWBh-aKAZ91nm_ZyaL3XT0Q-iUYPISlYYDOFhkA7vVy8B7Wz-4p9bN8eZ-QMvOflIM0j_Ypojl3IA9hZ4hMr1UeyY-Aom2QJMA8D52GpwcryBwqp0JyhR_vFP0bw8_WnVQfVAL0y_1ke2Rwg4Pa1HIV6JJ8bt5Kqn3Vd4MhDK7JSBmkSI5V28g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی تمیز مخابرات 69.84.182.49</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/MatinSenPaii/3521" target="_blank">📅 18:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3520">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آیپی تمیز مخابرات
69.84.182.49</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/MatinSenPaii/3520" target="_blank">📅 17:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3515">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/MatinSenPaii/3515" target="_blank">📅 15:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3506">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fVBvAjZw7PAZeXlwjKR17o0jziW2dksVTh6OWyLGYNocA0_fB-WrC9lKtdKRdisGa2uLDTbn1kHRXn5PBir6-LRyVpNZrqmvRdIddpuP78m_WnTuS0ppsBPXP2kHyo3gQbxvdAIn-LI4UJ471vXAQLNwTgOr6_feTyKx4nd8sXWXcIZkfDVIhbJPjVYu1m5nQNL9N6pevrF8Ev-riipP60Uo56OjFc0gEpnyTBBMHP4StDia3SS0jKyEM4Zd37UzT1dRYshT31U3G1hesKrmfe5AXw4NXuRYKEZyTKgh6whZJLZwMNDHiT7atDzhUnjZ48jJ1ABHizJUDDcj2C8rzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZA9wxSiSQnNM_nFE2ItFd2Qhs10saPkB7jbM5MkzxtFx42gbLNxmRZMjrg0KMqJ6FCqvbZm2KfUoqxiAYumV16QzXt8Oapd1kMBnN9cZNOPQm3kNWNT1j7GJkVa2mPxj-90WtWQeryRa7XYLWOu6sEwXnE-RMPZnjCg7xOUDZZ1hbs8duk5uGtsQuqwOeF0ab0HIirfOjhi83qiiLA_Sb_F5ozstRCEy7sx7n-iIp58PjkSIgOw_TIFHazPwNS7UQHydXOlQkpJECZ-lk5UI2stMXBg1rQRllSkqFMFfNSf0Keu9AIFpZx515uj2QqzvL1DwFbDaSmkuQjNORcnTMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CnUAuLRsTrIpkRINTH7TAQdDR9y4fHD9uVUFgApCqoo59b0ebjOb8YX6jzceEl7V_1i-hwYu_DWM0zQJIZKfL9AXdRu_2k3F2vowfG2g0C1kipZthj2Mqos1BM__Ma82z1Q_F4-WEDh3zgoYgIuDAEIdSWfmic1W9z2AP_6GrWImseZX9zX7PmHB2obhm2ANYmn5WsYzG79x6LxRc0NLdAOLApKiTe743y7WGK6pC3J5XVCMH7vEQKtTL6BCdJHHxrkVGhKV9wQ66VMd9yIeDPmy8fhNtZCPrCUGoz3Af-KRhxlcpftu6b7NMD9v8bNbKiVLpGs_TgyQ0CaLdiNAHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DIQ6LQ9D2xg5nNRX1_XvmRocAj4Vw-_F2kj1kNPZjwnrBqeRfFAus5eGcK6YBZEXKB-HuHfx5N42vQJs15lGXteAphreSvDEfY-BWdo6qazn91SYZGfsvIgIbLFLHWfIGP8_HX3MG0M3G9Qyl9w0dPsR4-HBekNaEcEqV3OGU9XL_5uc16BGqAKv0VxPTNWp8r3v6mkaqpCBKvNWjoWamH_FG-GjUtU60HtPHlyT4p1MstAf7LAPYaz5hEettt2wmEfcx_aZLDo8NGPkXkbp6Ex8Geb56_CatFOWrr-t9WPPy05Ahevrn_ZBuL9JfOeTYzIQlD8qo5f6EBj2Q_w3zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gEbFje6fZevTOnE_VeUiqsIbQe0wVvGtRRiOnZKv3oazF6omy1Zun9mxmVF5LwqOuP9wQMBxJazz1NrIHqiIJn5tvX4pcoVxF0G1Kew5rINBCf4k6r1WzgLzJYLxDdJVu6p_g9BopjqwxREGSyLrMcsX-Pn2blKU23IZZ6olndm_tGFgLXtvXtdU5SNLE1gQx_2l-7d7OTijnWWILWu1uO0W2-07vft4Qeyb0P2x7F7ky8PRsDGXCPHtbtIpO0zIJm1lRUxQG7Rx65fsc0q7kLkHuyefTk65zuvSCVWf9RxnMnEjBrDYsbUKlD6zXSDY6aX8nnfL3Nnhv9QAQWN0yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qEkKg5ZH4B6spSAY4KNjQiqvujS0JGl4BEEh6x32_BHbeTd2rc-fki28pjdJ58mQyiYsfWtS6pOUxxF8BuTVP-qTzeFvnuyuoDTPEqOW9dnsgaEe42VFRv-hnIMiZBLHhM1IWaWsuhan1afeuHgkoJJwmXhmYOyYYRqx1cNktrQ2EreC0CBei8i60w6pehfB3Joy_vFNWS1vz5PSFYn5j4ZrgPxLF0dfjNgg8fOYa1xES4sc-1NfKrKBBbE1qOpJiuO6uL57J3oBkaCNK9vQaRZ41zaN3rT20WJfSm-fBC6PHUdkEbshWTadImAdl1e87zqxoXK6aYGxeRi1vH6J6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lTRruApbkkTADGYDm3IiHlIAeyHg9_yHxyHVVji2jBHfPxxeWt5ZV-qIc6pZCcC2hNwKz1RGV6_UEAmvDfUbVsvuAQZ-S_Oo_0iHxnzUIErgtGxEMg5Gj_ygLx8KJnD3s45Pc9J59u1pbSl1zA-9HYjfcCwyzVhMJgPb6n5C0fc3ytVRZssmu0oO_fg32EWW3KyWZeI8HKsLlFxbYoNdyNPdZbr5YGSDeDVNcnJJl2sAIKmQYmA8FQDBxQXaxm5P55lE0MqXbamJ7hnggMYPDhg9ZtNSoyE3xaJLklr4CoM2wLiedeQ3uizMFcyhIHsVbXwuWYzuGiKDxYBicZAvMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FPa6Doa-wBdShdydZF1g3B5Siglm806qSM7hgqDrmFi6IoaeAUUI1QmkXzMkufbQT-4iZG42nvOye7IMvEYP_dYmWXOYZOr1VAzcd4POiJJI9aLvoknMN0YG0jgUgTm2nToqJMPIZOBS9ACufSVR6MTeTMi0iAjLdnjreqLsoyTp6oueu_npVyP5jotp25mIA3ukrIN4TvCZSkvM5gH1GLtoT9mCyv3kv1l7bx1EAABGXVk9mLJ8pHmzpMhFKL0Q8ET8DujQTQLOVQVqW8gkFTwRZRNEHwkXDOQ3U87iDv-FDNbEwMlXDJthATAd-bczh6e_AyT_ewTyg7yWZkxdCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OOazz_0VuotPEZa_2HvbLQZkGphr8hQAMwPpTY7uYj1jwKGxPcChjWk5cVSEW65iuQtsHMpoxVs2DBk3zx21655aLckYx1Ia98ceZVtQHUeKSq7uz0ULUUR9I_-HCa4uzFHwLcM-IiwnS0ayWY4YJkT7U2v3j4d4oPfOZHQK_H1gytKYvRBVwffS418K46Gx8tT3Ey1lAhejzO7LHUV015JG2DvRMiPoegWDS_YNvyso9PKOUGQuGKB5PFCwd5Oac7TyR6BqUdL12O08TTzw33V6l2ZQWHryi_puCbKhYpyo1nVyez_ZiTF9itzhOUVJ4cNz9TtFGqdgEoZJu8p7SQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش قدم به قدم اتصال به کانفیگ های بات
نکته
از آپدیت آخر  V2rayNG استفاده کنید
@WhiteDNS</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/MatinSenPaii/3506" target="_blank">📅 15:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3505">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZ17_eHSj0ogy-y8rrgutIyRYSPuoLLLBGf4Z1uPc0QTnqNJdx7M3zJlwrHpW5iN6d6YeOiFrExpQ48NVJy7dekMpB1RsEqx0PKK6_fK3U33ORECD79Qx4cqGH16e66RnPZgbFXKG0dVD2d1yS3in06zqIdAwsvzzTtKQjlFUTfOG8Dnhgl9RWRr4hjDDnPXjRGdCE492As9-1CmSfzV5PKx_QssCpk5I8iKlMzAk9FNsG33nsI_mQo0qfwY4OVKcV3gYvKgatYvD5Nk4MoWnZREaG5ZNClaD65m5Sy9Y1qqfwmX0v4LAt3CJsGCi511vPnG02j31fJ4yaBENmqUNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/MatinSenPaii/3505" target="_blank">📅 15:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3504">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دوستان ربات تحت بار و فشار زیادیه. کمی صبر کنید پدرام داره روش کار می‌کنه یه کم دیگه مجدد واستون قرار میدم</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/MatinSenPaii/3504" target="_blank">📅 14:09 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn1.telesco.pe/file/XI5Y2sjaKL13BreaJtNrdGy3ua9KegB8lE54AWIVOmgj33mhRRTDWYsrdYlW4mXq59qNbpIzzKeo4MBL5jS5aKMkJhjeUEHMrYZJyXVe6SKJ1ONIOZ3gmNDs_QLp5pCu9f88lNUG71AJuF6i7TuyR9Bs0CtjOCyvmbeZcg6MHD1HSkEuaComxlUa8Hn7JBeCq5RpXcCp3Frkrej8_aMl3HSw9kWZDgmZREWf7Pz4HkYac-nRPF2LCvJmq25Uo9_TsnlacHPKR-FPnm_74sJ6wpC18ZOTzToudAzKC_OpjlZNLRyQalY9l0P9LYK_oJ60Og_pHLVS1vIV-acjEetkwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 93.3K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 02:28:21</div>
<hr>

<div class="tg-post" id="msg-2332">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VZ4oOnFwIpIn0AR7vukwtfsxM-QE8EU6MfDEeb4MhoVx04zEToGLpiNo8zM6g81tX9j0ujphbCQ3LG5UkUuPDkZzvRuW9ywCegUMilN38CUqkDjLbfo3NYPRS1lGOZTPYi1BWJ2DvE75Y2Snn4AtxMnFzT2mg_11m5WXRIP6asy2G49HAkIYykUtdHMK0umHsCeHip-yXwdy8cr-MGfHHRGb8OVFZMkN0MrdRRadii7L4QjqXKtXB8wE_4emKOLsUXiSparnRhs8Ppz5tqNA98nUIpnM3MoUU-WepispYIISFGjIq2WPAamVC07dsRqI07inFn5w0wslMYq6GFYwGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون فرهنگی مجلس: امروز پیامرسان‌های داخلی گوی رقابت را از پیامرسان‌های خارجی گرفتند.
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/ircfspace/2332" target="_blank">📅 19:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2331">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ck60UB4b7T6EYcwKwFwXlZHIGWU4r6uBLof5b0VpSP2DfKdxmGHWjLHdEeCU_la5TjQkLydzTlumcq7Ac1Rmua854l8uxZVaGT7g6YcUikl2s7w-iaQH_DUDX94gxnAgSGo8m5NmhW4tC2DLQ-jdsOyGr-7m2vb7RDB2qgj1-T_aiMHSqnUxEdy3F7XoePSYLU7fC1jJI3CjxsISN0XJ8sgztoZbP4Imu047CxGZ4yca2zZyo770dTpkejyb4ZNP6c-Tspt7kdd0pkzPXuMU7hsfuLXOA03IT4IkbVxlvGYae3a5VMDdWafDREPPjUB0giGYVVNjlzWpIwOKJ8kqLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷۵ روز از قطع اینترنت گذشت؛ همزمان درآمد یک کانال فروش فیلترشکن از ۱ میلیون دلار گذشت!
©
mosi115
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/ircfspace/2331" target="_blank">📅 19:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2330">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AxUQvMV_R5pInb2Cy-8Fkt-P_L9gtrYbB_L7aJVGds0yI380mJVuB2VVKPgN7pNqMUuemqBvIX4ibpHSLrvN2H_JPaXv69cI3LMHw00tDC9uNNl7n1FQBFhO7a9bW8hxEw8nneNDavbjLpyVWv1cFE9mJ8sLMg6dhkKLQVa6S75fIl9pL98tcZutEl4SOxxD18U7mDifQozhqp8Eg7hBqJoUQsGuZnZv45LtWB4W0fiIa3R-f6No43c0g5qnUMrC7JxSYPDUw7YzCXGzDs20CcWo4FIaXsJh2PCb2O2tgWENvRz7KIVbxPPZ1LFE-Xbk4LzNvBzUgD75RQ4q8-am2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میاد مرحله‌ی جدیدی از
#اینترنت_طبقاتی
شروع شده؛ دیگه خجالت هم نمیکشن. قدم به قدم دسترسی برخی افراد و کسب و کارها وصل میشه، تا عموم مردم به عصر بدون اینترنت و بدون هوش مصنوعی برگردن.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/ircfspace/2330" target="_blank">📅 19:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2329">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سی‌ان‌ان در گزارشی نوشته
#اینترنت_طبقاتی
در ایران خشم و نارضایتی عمومی رو شعله‌ور کرده و به نمادی از نابرابری ساختاری در جمهوری اسلامی تبدیل شده ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/ircfspace/2329" target="_blank">📅 19:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2328">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">قوه قضائیه در یک کشور مردم سالار آنجایی که حقوق مردم با تصمیمات دولت یا نهادهای امنیتی نقض می‌شود واکنش نشان میدهد. در ایران رئیس این قوه نه تنها حق مردم در دسترسی به اینترنت و کسب و کار مردم برایش مهم نبوده، بلکه چندبار شاکی شده چرا اینترنت پرو را سختگیرانه نداده‌اید!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/ircfspace/2328" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2327">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=gIqNe2inN9eH3livRUTsXSX8-EvWOIuoikwo7OBxYdQ57CbaA44UUolXiTYdwk0n0WLFJdPX3quWkcCVB8yA1Fdv081j7eUIMsvNpdMDgfRWwiUmRuZCwGneHL85dLBsW-lkiwJBrwR2ey648PYcOoFVnxjCnpYly47nogd-CBV1kVb6yGB1NtvUPkX3YoAMaIbD8351zJWJwYtbuP2FD0gv2kmjoOj9yCo5CsI1vrR29pXYlvsl8spsTeEowvsS8aM5fUj3solSDGXgSMyoIwaeJExrGCppdnfB-bgiykedNnYrTKMN58hhppy8iPlLwIIc6wsXKeDr3693I5IUBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=gIqNe2inN9eH3livRUTsXSX8-EvWOIuoikwo7OBxYdQ57CbaA44UUolXiTYdwk0n0WLFJdPX3quWkcCVB8yA1Fdv081j7eUIMsvNpdMDgfRWwiUmRuZCwGneHL85dLBsW-lkiwJBrwR2ey648PYcOoFVnxjCnpYly47nogd-CBV1kVb6yGB1NtvUPkX3YoAMaIbD8351zJWJwYtbuP2FD0gv2kmjoOj9yCo5CsI1vrR29pXYlvsl8spsTeEowvsS8aM5fUj3solSDGXgSMyoIwaeJExrGCppdnfB-bgiykedNnYrTKMN58hhppy8iPlLwIIc6wsXKeDr3693I5IUBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر هکر بودین و میخواستین بانکهای جمهوری اسلامی رو هک کنین، سرورتون رو کجا میذاشتین؟
علی کیافی‌فر، متخصص امنیت اطلاعات: در جنگ دوازده‌روزه، نوبیتکس، بانک پاسارگاد، بانک سپه و بانک مرکزی از داخل خود ایران هک شدند. مثلاً نوبیتکس توسط یک سرور زامبی واقع در یک مدرسه‌ی علمیه خواهران قم هک شد.
قطع اینترنت امنیت رو کمتر میکنه و نه بیشتر. سیستم‌ها نمی‌تونن آپدیت امنیتی بگیرن، سرتیفیکیت‌ها expire میشن، ابزارهای دفاعی (فایروال، آنتی‌ویروس) از کار می‌افتن و هکرها (داخلی یا خارجی) راحت‌تر کار می‌کنن، چون نظارت و لاگ‌گیری مختل میشه.
©
farhad_mottaghi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/ircfspace/2327" target="_blank">📅 19:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2326">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lXhE1KlVsO-YCVsaqg6QZByC_z2e4ZqJko9HckA18iblY5ULkiK1n68iEGrLpB4Ifh-NaV7l9vU1V8X-MRG1mc34ZPNmoqpjk-m2vg93QSJ09kkt14M-ZiKxFh5jcQfpE3Ft1US8Pn4OhK4Gg4A3fldgw9Py0xSeLeKDeT9AgSYI9qMn4F0rTY74M8e9lJvsUz8HQIPjoSP9cEIVmCFHhwe8qICDc17eyS5QhFza4aGTkML60unOmBl7n1gLY1hMSIOEwDvV-icgYSNwCBPAkHm-DTwEBz2N36hkjYnz2LQ7l4ARlwMUPv1wl8NbJ5rKnbxbvf9pHUrMJ5Yg9hHX7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آگهی یک دفتر پیشخوان دولت برای فروش
#اینترنت_پرو
©
mamlekate
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/ircfspace/2326" target="_blank">📅 19:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2324">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tCqrL3xG4M8-CeMRrXNNTuILQqKh6KV48OiBWub6s9XJhs5A5NgEBDC2b-UOBp5ubdDEUoUfSRBdBLPsMH67HFm5mH-Pt2rJPisqd1tUYrYYguOugsMjdAofanQFVkuC53PODaAZ4K9HSSVjL_qWkuuqstWjE_YjRPQ0_UTxXMZMS9Wb_tCdBv9AmrPP5u1zk0gXIWXFR3Cjeig2W3FcgZO_t3K50FXpvTphsBRVQ43EVIoDygb9rLXRkCY5X8ZH8QSvr45HMZV0nATKMYC0SEYLWd1yxgM0pWp8RFnwxApGkLeiRcemG1T64NeZ3wZTRtQtAB7661Wh05uNiSvMrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا دسترسی آزاد به اینترنت در متن سخنرانی‌های رییس‌جمهور و هیات دولت برقرار شده!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/ircfspace/2324" target="_blank">📅 10:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2323">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تعداد کاربران اینترنت پرو کمتر از نیم‌میلیون نفر است!
تا امروز یک اپراتور با ارسال بیش از ۴ میلیون پیامک، برای بیش از ۴۵۰ هزار سیمکارت،
#اینترنت_پرو
فعال کرده و اپراتور دیگر با ارسال بیش از ۵۰۰ هزار پیامک، حدود ۴۰ هزار کاربر پرو فعال دارد.
©
aghplt
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/ircfspace/2323" target="_blank">📅 08:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2322">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qVozktRdO_TY3lnbHxq7cJKk7TWpKRp-1TOP9tNu9TGEA5j_z-LCyjF6vWZljxoAYh7qMpPHqg7kIfe7q6t8J_Ksa_qmXBzbCdH5AAoPjQBBDrhw1qJelQAoHYGChbkXQNtmAVcjLVx8fCxzHBsC2Kwt4CzwBWF3glLHEpsBO-bUTQ6gxGGw7wSwmq6ObsZ61xFFMWENHunNEhZp9TQBFOjAg5gfi608dOg5gbpjbYbsjnx2t83NoVpN4_tQe1TtFux4jxGP8cOzU9C3YDsBDD8o05hCj0xhtAagNMo7vC5rNv78LzCfjqaT9111nM3Wklumk5FPmY7ociu97nHRzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن مهندسان نفت برای دریافت
#اینترنت_پرو
واجد شرایط شد.
۷۵ روزه اینترنت رو به بهانه امنیت به روی میلیون‌ها ایرانی بستن و هرکی که کار و زندگیش به اینترنت وابسته بود به خاک سیاه نشوندن، تا
#اینترنت_طبقاتی
رو اجرا کنن. مدیونین اگر فکر کنین کیسه دوختن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/ircfspace/2322" target="_blank">📅 08:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2321">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بدتر از قطعی اینترنت فکر اینه که سالها درس خوندی، دکتر و مهندس و محقق و پژوهشگر شدی، بعد واسه کار علمی دسترسی به اینترنت بین‌الملل نداری؛ اونوقت حمید رسایی با حول و حوش دو کلاس سواد برات تصمیم میگیره تو اینترنت نداشته باشی، تازه خودشم تو ایکس وله!!!
©
NiHa_Mehr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/ircfspace/2321" target="_blank">📅 08:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2320">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RLL3cefIL6JavyzxNSVBC6NvIkMMcer_VHe5v08diEtOhHrOP7ryOOI0J59haXBgbTxIeSIhmKgNj0gQrK5Fa2aHTCVOHZuOVgZZCUXmZ4sltf69h8t8Wcxgo96ggxWXwvpPoPhq8rsNxypCnvvOpHeM54ehhtj5duHLT0WW0cKH7Br4NUoE7-q-1eEr3LWuuXnALjoytPLKFbvV9QYQD4WG-0OAMTOB9MQnMlx9fJDyCmXwfUUvjCvyDo2mmDO00jfwKcrxknmuDgQ0kZ0Tzy5cRWdG3z01CWiOEIceY0ZZ_oCflxZc_Fg2F5Cr8RY0NRkpElehcjvLCgVjY93hfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس قوای سه‌گانه کشور در واقع ۴تان، که یکیشون به نام
#قوه_عاقله
نه توان قانون‌گذاری داره، نه زور اجرای قوانین رو، و نه در جایگاه قضاوته. مهم اینه که قوه عاقله قصه ما با
#اینترنت_طبقاتی
مخالفه و قراره نقش اپوزیسیون داخلی رو در این مضحکه بازی کنه!
©
nimaclick
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/ircfspace/2320" target="_blank">📅 18:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2319">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r1ticOSwByWs7rC90ANNfX5EcC-ZQO9KuD80iGABH_rmc0MNmtTsV_KobcKe1iEnrGK9sMi30SCCsbF_LsJVR0ayl76b22uHIYIPVfNkI1Pyr4CAH_m64p9vzMKxRo5ChkeUupXIwWzk3XocTBzDFmpoul3wftCIaaB83-hmuwQf1wpsbsL1jsabCLycqF7OCrosqkT2wJUILwv_0u-Jm3U-vkcyuIQoLRZ05mav4vYoB1-tjcpeh872L_jtQDqfICJm25yU-9tTR9WryVzRPhsOc590qy2OlQMzpnwboeyram9jxfzHH9rSznbEHfteBEqoKNktneUl7ABQL0fuIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پای
#اینترنت_پرو
به اتحادیه صنف اغذیه‌فروشان و مواد غذایی باز شد و حالا با ارائه پروانه کسب و کارت ملی میتونن از
#اینترنت_طبقاتی
استفاده کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/ircfspace/2319" target="_blank">📅 17:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2318">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lGK6oUcD8EhLGBBwMq3wqRMNbWl_i9NGuvpBzAfoqOAF0uNI6FIFlMLwtKvoBIvENcpA5mUmqkdzmKusg5pCvQb1VPvKr4mDW7skIGX_a5ZTnA379LLUtYqOL9PRAldaA8kDjSGEUMX0TUeydHVpdkzOpyu2HTjk6rtoWgUTaAD4G88feWJqHXsmBHaYoXCOTOTZUwuE4lMkCdr-exZSROtiZ4ioKKWo6zRJphvirO76RnLEv1vPfG8TfC685V7YnSp9HEW7QyXbJUKp2JOZ9k-3sBzbcx17bcYCeTThX_qnhjwjCuYPi-GobDbUI489774R4GFCzbeRV4ut_Q5iGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان TunnelX برای زمانی ساخته شده که کاربر نمیخواد تمام ترافیک در سیستم‌عامل ویندوز از VPN عبور کنه. با این برنامه میشه فقط برنامه‌هایی مثل مرورگر، تلگرام، ابزارهای توسعه یا برنامه‌های مشخص دیگه رو وارد تانل کرد و بقیه ترافیک سیستم رو روی اینترنت عادی نگه داشت.
👉
github.com/MaxiFan/TunnelX/releases/latest
💡
t.me/PersianGithubMirror/4816
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/ircfspace/2318" target="_blank">📅 16:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2316">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FAVgo1OtjhF8Z2hHfYB1Ra4JYW6Wd4RH3fyRgGiP_gdAuePLqELVvJT59PoryN2VATl_fTw16QFYT2atJcEfzSVetwVvL1UF09cX8j5G6u_Eiy7rhpg8vARP7P8cAgsd2N7efA41ZHNIYg2n0Tdh7EVem_2YztcWixnOrBoFIPz1i1CpKsOS5wnt6QQ1d67rysX_qtVTKWhETNHrHKg74JlXI3DSJerwQOEMuPhvKolXChh7_rmAx7k2gdMp7AcF2o6uwkb97uQprSq_LtH3FA5oUe6y_ocy3Z8X8bq3js0BK-fwEBRwEfczYuDTMveX5Af1RNGB_YbzpASpfinqGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر اینترنت غزه، اوکراین یا هرجایی که حمایت از آن برای حامی‌نماهای حقوق بشر "ویترین اخلاقی" داشته باشد فقط ۷ روز قطع میشد، دنیا را روی سرشان خراب می‌کردند؛ اما اینترنت ایران ۷۴ روز است عملاً قطع شده و آب از آب تکان نخورده است.
فکر می‌کنید اتفاق خاصی افتاده؟ خیر.
ضریب دسترسی واقعی به اینترنت آزاد در ایران به گواه نت‌بلاکس به حدود ۲ درصد رسیده؛ میلیون‌ها انسان نه ۷ روز، بلکه ۷۴ روز عملاً در یک زندان دیجیتال گروگان گرفته شده‌اند و همزمان که جمهوری اسلامی در پشت پرده به سرکوب، بازداشت و اعدام مشغول است، آشغالی به نام "اینترنت پرو" را به‌عنوان راه‌حل به مردم می‌فروشد، که عقیم‌سازی عمدی دسترسی آزاد به اطلاعات و نقض آشکار حقوق انسانی و حریم خصوصی شهروندان است.
ظاهراً برای جهان مدعی آزادی، فقط آن دسته از رنج‌هایی دیده می‌شوند که موضع‌گیری برایش هزینه‌ای نداشته باشد، یا چشم‌های مردمانش رنگی باشد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2316" target="_blank">📅 10:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2315">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qxxj7BG6LKik1RAd_5hAVIsVBTqMq7iEJKTmj1e7nlPtiofnkUzhiEIhGSHL3B6ZirpVYLGMbwj6CYbz3yxIX5M1CcAnjf7NEQpb_8w-pHHkdt7KzYO_fYLqPV2tulhBQAuuBpHs3LshkLiDK4wmim1HgYsG4x3O0e25aDfLYALm6gs8ygFS_bpGVY7IN-DghL5a6_l2KsqivRLUe1-ZvdtC6iNlHK239bJuLUZAJbxYD9nmkAnvuNMyPerHO7aBNM1UPSaInmdM91czepZebJ23daLseyxKDi-W6XyCNa0BnvvWzYSq05J99t9KL75u-1U7y-OgJ_HMl8jS0uWn3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در روز ۷۴م از قطع سراسری اینترنت هستیم.
وزیر قطع‌ارتباطات گفته "در تلاش برای برقراری اینترنت بین‌الملل در اسرع وقت هستیم".
نتیجه عملکرد و تلاش ۷۴ روز اخیر این فرد از خروجی عملکرد یه مترسک داخل مزرعه هم کمتر بوده و جالبه با اینکه از بی‌خاصیتی خودش آگاهه، حتی بصورت نمادین دست به استعفا نزده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/ircfspace/2315" target="_blank">📅 08:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2314">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t1l_Is0flM0wWigbFjl3TDrCzydwDWjFy0w3NpVPCtWIc6MCl_TIMsc3jUYsjtRZp-cfEfp0H1zbT-uXSGq72LVxO3xW4g1_zl0oJKGK3aRQruU7v2eOBTh955hdxV_u2euWmm1JgHc6sOSYwNXu3Vi-ElPUdgiB0w38Tfhkt6MXS6faNGgqmSKKIhrVmrUjuZ9hDn9gG2mO5wqyonD3wBNzGM_mC-Qhzw9AWberP8yvFp_JDHedY_Lws16lfTvsYiIeH5qFlKkKHbaJQyeyk1uLfqwPmzM4Xf50oGtgBvriWGaX2xdf99ik2qNG7Y-mKlgkNv6fGbvJysHhtKCSdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه روندی که نشان می‌دهد تصمیم‌گیری درباره اینترنت و سطح دسترسی کاربران عملاً از دولت خارج شده، وزیر بهداشت برای رفع محدودیت دسترسی به پایگاه علمی «پاب‌مد» مستقیماً به رئیس مرکز ملی فضای مجازی نامه نوشت؛ اقدامی که بار دیگر نقش کمرنگ وزارت ارتباطات در سیاست‌گذاری اینترنت را پررنگ کرده است. /شرق
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/ircfspace/2314" target="_blank">📅 08:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2312">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s6KHJ9aDSz2hqd2zLA3XWslJkIHfpDzblFAAKNxxbJPYNT0TreBBRcgTnh-tKxSCmWRXZ6UScPgymfVAWer_T5DpkO8Ro3P7WrJ72xcluq-rZD4TNX6ntTYNT4G5TTncHVWbZ2jGfj9hUZY_UjBYXcniNCTSYt55erjt3KU3x0YPeh0PCqZMJ9Z1aufiatLCziRiMwfJFcCIFTZ3PYfoZj9XkqwwHKx6tCzDQE9dq6k8ZmXkqY9SciU07mTcuRBowJpAVDwBe2BbMzmlqB777IAo3fLiF9TQzcG3iMuuZsLWKXQEh4OB5DXoflu0dy_qNCC8SD0wGL_zukvAoAgNuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت AIO Downloader یه ابزار متن‌باز و کاربردی برای دانلود فایل و محتوا از سرویس‌هایی مثل یوتیوب، گیت‌هاب، اینستاگرام، ایکس، تلگرام، گوگل‌پلی، تیک‌تاک، پینترست، ساندکلود و ... هست، که فرایند دانلود رو از طریق GitHub Actions انجام میده.
این ابزار طوری طراحی شده که در شرایط محدودیت شدید اینترنت و وایت‌لیست فعلی بتونه بسیاری از فایل‌ها و لینک‌ها رو دریافت کنه، بدون اینکه نیاز باشه سیستم یا سرور شخصی برای دانلود داشته باشین.
با توجه به اینکه این پروژه به GitHub Actions متکیه، بهتره برای استفاده ازش از اکانت اصلی گیت‌هاب استفاده نکنین و ترجیحاً یک اکانت جداگانه بسازین.
👉
github.com/ProAlit/aio-downloader
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/ircfspace/2312" target="_blank">📅 08:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2311">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LIAAab0gt3D8eluyiARBHqKyzudSYRN1QUMUtHcoZhsAE_VVgyXHaihqcvQhC0rS1uH10BhGyyHAxGY9cX-NBj4_gD1bKV1pcbTkvwK_utvy729cPULQ5AbSR-kZKApPaz8KWjO9c1QPIGkOrsPNb87KgSpSmdVyxxd_DUOiBea_jRQx84Bec8620fa1b0qI6cE6X2FbEx2wtkn4ie5pS5LGhJC87uHOdvewvAEN2F4S5MH7Tt69ueAc1ragHrocagoEiWk-Qtua9JDaYJtHS4zwj3ftBFd68ZI9V6H5vd8tHPvfr-c7BVJNhGDxjWyai3okaGeGTSw6Uuk5xBuWGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پیامرسان_بومی
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/ircfspace/2311" target="_blank">📅 21:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2310">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YQaZ6SuVRhqUP6xxPfuo6nQbfnrvVWG3C-07ktniURsQbyg40F9V2mjhysKYgChn9syuLdy0dNBlxtKCpgERdSr6K-wuV-atEwHgK6uNBcWyko3bpowtdamOk1wZb2ISKgE3xthCgyeDUR5fBP0meI-LDPmGTmYv5lhQ_c09L51GmC-pwhoKCkFbuisDz2xR9RgHkhuSilL1d0g9OAd7myXfp4oc5YyzAxekKt68wI8H2PKlkCBJLvwDL4_m2lZ5OjguA77kW-daZvbEKnk-oJXDVTtnv07g8gX7zdV9_qGLgmJvHP9cAJWZDX5gtJa-iqZFwf_XerRdmff21DsPdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه رودربایستی رو کنار گذاشتن و بدون ثبت‌نام و بدون احرازهویت، بابت پیوستن به پویش جان‌فدا ازت تقدیر میکنن
😁
کی به کیه؛ اگر آمارش به ۳۰۰ میلیون برسه هم تعجب نمی‌کنم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/ircfspace/2310" target="_blank">📅 21:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2309">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تا الان توی هیچ پستی نگفتم که به پروژه‌هام دونیت کنین، چون حس خوبی به مطرح کردنش نداشتم؛ ولی شرایط همینطور پیش بره احتمالا سر چهارراه نشسته باشم
😂
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/ircfspace/2309" target="_blank">📅 21:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2308">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">قبل از شروع جنگ و قطعی اینترنت درخواست فیبر نوری دادم و حالا اومدن نصب و فعالش کردن.
با تشکر از شاتل بابت سرویس خوبشون؛ در واقع قبل از نصب اینترنت نداشتم، ولی الان با سرعت خیلی بیشتری اینترنت ندارم.
©
itsmralii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2308" target="_blank">📅 11:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2307">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pq4aET_hIObr7AObCsHQGMCxkZdRFv4ivt2tO0oYM8g7oasCpzqNrjpc2KhxfYXucabzm2ZacozmDEBNSpWcx4NvDvm6wGXyixh6CzSaIz9lJxvvGMDW6V57w2sYJkFpa76MqvNIEMDnZffGNW-fNdPZRib2qP1Iqs9gDdpysC79aldyvNZt-sZwzwLKTMg8WtWnXT1FsTXzXJ6pCFtuFYvPUBTF1nxXjDhIbosWGJZ-di9QaMuiqbHCr1YCDpVElgFACCZTM3Z5WqT5lGTsqS_nKOkH9pGJBp36mNrZ9JCaVVw7W3P5l8kFsstrXjD4i_JWU4sSiyH8LgYTYDMFRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور از وزیر ارتباطات بابت هیچ و پوچ قدردانی میکنه، بعدش همون وزیر از رئیس‌جمهور قدردانی میکنه، بعدترش همین بدردنخورها دسته‌جمعی از مردم قدردانی میکنن؛ اما تهش می‌بینی ۷۳ روزه که اینترنت قطع هست!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2307" target="_blank">📅 08:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2306">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/wBf8HISANeFUBhARcJD6YN9T2-WIaDPdCH9O-jnU0mCo0yMTrc4VLTvUXxsjKKwn8xqtSTEyDtWnl1bnUsEDf37qS6CS3Jdz0MPF0_rjUBgHzNim_C4XenVmkTqwf0zK8KSRANSOoHBUisRfHibM2yuq0zl7iL75gGYzT1ddczx5MNShc7EXB-jvAUTCBkx_EMIUNNv_RgBZD0qhzFKUmqihCmrhvdL7S0y1wd96n_OSWtqFbX5294THgfsnNdfLyV0Ma7QACJUHO8QWznlMtgWVNwhS5BgPWfYdrizx8APTOld9Ke8QeT3ebdmlHtDD_e-MrgFfHR7k8ep1Y7rJ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteDNS یک کلاینت متن‌باز و رایگان برای اندرویده، که امکان اتصال از طریق DNS Tunnel رو با دو حالت Proxy و VPN فراهم می‌کنه. این برنامه با تکیه بر MasterDNS و StormDNS طراحی شده و میتونه بدون نیاز به تنظیمات پیچیده، ارتباط رو از طریق تانل DNS برقرار کنه.
👉
github.com/iampedii/WhiteDNS/releases/latest
💡
t.me/PersianGithubMirror/4637
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2306" target="_blank">📅 16:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2304">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j4GqRbw77Ut4SzyZ4HJQ9lnTO8zafx0YvH8PYm6XPwxAByddnhB82EvxYxVJJrlDbeRDBpyaCx_BvP63w0eSEBWIy3b7fN_8XxanFBAPjbp81aOBalUbT3ktY10JLFGDnyR-Kpp0enbM6cZxWl8fcysn19ZN01Qzx2g97r0TgrInmflK31ad7Nr_sYb6TrtOuLrvpCpTn292R7F8ua3AdBP4l27bIWxZH62zSFZ3WtHdIfumxQxFP7NDK_iBeDHGZR2sUeCgXhicnlUTylXEoacPIE2D5CPjGInDXUkfhkcu5vqjK76IsVLTHb3ubD6M36OPzP1Endmp5PNJEsqjzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز که نت‌بلاکس عدد روزهای قطع سراسری اینترنت در ایران رو اعلام می‌کنه، یه عده میگن "خب شمردن که کاری نداره، خودمونم بلدیم".
ولی مسئله فقط شمردن نیست؛ مسئله اینه که نباید این قضیه عادی‌سازی و فراموش بشه. اگر فکر می‌کنیم راه مؤثرتری برای اثرگذاری وجود داره، خوبه؛ ولی سوال اینجاست که چرا تماشا می‌کنیم؟
۷۲ روز گذشته و هیچ اقدام جدی‌ای برای کمک جهت اتصال آزاد به اینترنت انجام نشده، کسب‌وکارها نابود شدن، آدم‌ها شغلشون رو از دست دادن و سفره خیلی از خانواده‌ها کوچیک‌تر شده. مردم برای یک اتصال معمولی باید میلیون‌ها تومان از جیب خودشون هزینه کنن و در عین حال بخش بزرگی از نهادها و جوامع حقوق بشری نسبت به تداوم قطع اینترنت، سرکوب، دستگیری‌ها و اعدام‌ها سکوت رو ترجیح میدن.
در فضایی که همه‌چیز خیلی سریع به حاشیه میره، استمرار در اطلاع‌رسانی خودش یک کار مهمه و همین گزارش‌های روزانه امثال نت‌بلاکس حداقل باعث میشه موضوع قطع اینترنت در ایران کامل از توجه‌ها خارج نشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2304" target="_blank">📅 12:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2303">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">این هفت کابل اینترنت جهانی در خلیج فارس رو اگه قطع کنید خیلی خوبه، اونا هم مثل ما اینترنت نداشته باشن، بلکه دکان‌های حقوق حشری صداشون برای اونا دربیاد و یه نگاهی هم اینور بندازن و دل ما هم خنک بشه!
قطع کنید.
©
ehsan_369
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/ircfspace/2303" target="_blank">📅 12:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2302">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jlPO4JiKaQveHzDeCR_pTJ_8DbF9EOxywV4Avs_YR1aTxRn5Tue3-SdULlRFHkvNmzTJWJapscS-n0D1efaxCLeZnkwdOJiJv1xovAwiY5raFXgoOHD88g3xBwUX7iXUtOId5U7OXQ1K7JD4Om6NteWBulSmT9fqUT7A1sc9MeKcrAmi184S2T8o6_usCPvYBKMdS1OcXIq5X7yiQ8EbcCLoGtRE0Um6cbQrdEdW41Hs2dMbIxqdo_OxOEl59t2mrgoKufCA_ndzRaYUnNxZGQ3Pm_sEWq9-rXEafhSNA1oIPzYi9qJHPdJTungVsnRhad-E1CHSdMDnk4228vRgPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم نوشته تنگه هرمز فقط مسیر نفت و کشتی نیست؛ بخش بزرگی از اینترنت و تبادلات مالی دنیا هم از کابل‌های زیردریا رد میشه، که از اونجا عبور می‌کنن. پیشنهاد داده ایران از این مسیر پول و کنترل بیشتری بگیره؛ یعنی برای عبور کابل‌ها مجوز و هزینه تعیین بشه، شرکت‌های بزرگی مثل متا و مایکروسافت مجبور بشن تحت قوانین ایران کار کنن و تعمیر کابل‌ها هم فقط دست شرکت‌های داخلی باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2302" target="_blank">📅 12:17 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2301">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VLr7soMdCXld3Xn4oLIYmKgZX7evcc_Oab1jCFO2PowylzylmBOgX9ReHatRpG68iOLdVQvWE-VJ1ZGXqkDWAPSU4Xr6pOsmNu1CY40pQWL7-i-nlz4F4S6svjOB9tTLV8C6fCMf_mM5WzcyrVYCYH8cNl2T68OzhjWysV5k4F8Ls31lIhph83H6IyJeaWSs06NAZ6gV1x9y03a0Iv2FLyIzsIf8upvfCIGibR20MfX3r15hAeEj5SmESj84WSBae-vTjO1WTZTo7e39iiUYBmbdH72S6lt2hQ_GklaTjB1tc4VyNuh0kpnGdQafsqUZWXo-eAaLfJurlsrxOoM2JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران وارد هفتادودومین روز خود شده و هیچ نشانه‌ای از بازگشت گسترده اینترنت دیده نمی‌شود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/ircfspace/2301" target="_blank">📅 12:07 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2300">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JYkZN-dc3Ro1_PBFromZVzRYQwMx-EsldaPtOBcW2kwtCU-YU1zaY_pLcEKaUV11UWxhaOnbalA6fpSv6E64fLAmQmGhInXQ5HEHWEN9hI-nwxAV6yVTFFGoG2w3-y9w04fXU-4x-XJoSgcbVkghuK5Uafk8bbb3deXFiZ6G6YalDGoJLTIhOMousB1wrRFzUdFDNvs0jAbKsuBraRCWpDl1GWKAs4A68xmgOGrkvgzOEvRAIKCiaf1tlJkwjmYPTv5qjwcIhoh-_AFDrHYyS7P9XiExitgVY8igCXSkcn6zKIIl9TxWPucajW9Vc3415W80d5fy0hRR5Fzn7u2J_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۳ از اپ متن‌باز و رایگان TeleMirror برای "دریافت آخرین مطالب کانال‌های تلگرام در شرایط محدودیت شدید اینترنت" برای ویندوز، لینوکس و مک منتشر شد.
در این نسخه نمایش پست‌ها بهینه‌تر شده و مشکلات مربوط به کش تا حد زیادی برطرف شده، بخش تنظیمات به برنامه اضافه شده و امکان بازگشت به تنظیمات پیشفرض فراهم اومده. لیست کانال‌های پیشفرض افزایش پیدا کرده و علاوه بر نسخه Lite، یک حالت Normal اضافه شده که تلاش می‌کنه در صورت امکان تصاویر فیلترشده رو هم نمایش بده.
این برنامه فیلترشکن نیست و بر پایه دسترسی‌های فعلی وایت‌لیست اینترنت عمل می‌کنه، بنابراین ممکنه روی برخی از اینترنت‌ها قابل استفاده نباشه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4599
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2300" target="_blank">📅 18:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2299">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">افغانستان تست خدمات اینترنت 5G رو در کابل استارت زده، عراق تلگرام رو رفع فیلتر کرده؛ اما جمهوری اسلامی تا دقیقه ۹۰ درحال آزار و اذیت میلیون‌ها ایرانیه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2299" target="_blank">📅 17:52 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2298">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oj0RhlR3fh1cjHHZTHGItnL5L4YfVG2EZif55zgYfp6AaSWdtydcGI2fqDFFb_UFKHtgoMKMq8PzC14Z5Lw1x71_Yc4oHHKel5isA-x7QB7SYkhNZNP2NO-ZioNjrQeqWHvuOo4FWB0jbuIlflaSFWxTH9MjU5pcAhbn_U0h1fqVZk86qfV5a_fF9cdRUrvl3JWq5NNiQxLOb9u2g8zVx8IWFtSKrcsYjfLxpcVlZrBQPkwDYQ4W1hZ1g8tFqPENcCrt7E2LdJhgROCpxSCiDw3iyrJx1EjulPjQ7YPX-X8SIGPNKa5KlgamhpQOOJs17Cimurwum6zUzLpb8K9WrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی خاک بر سرتون (پیامرسان‌های بومی) که با اینهمه حمایت و در میدانی بدون رقیبِ جدی هم عرضه ندارین کیفیت خدمات دهی، پشتیبانی و توان زیرساختیتون رو ارتقا بدین و بعداز اینهمه سال سابقه، آدم نمیتونه ۸ مگ فیلم ارسال کنه.
بعد از خودروسازی، باید شماها رو هم دومین فرزند لوس و بی‌خاصیت کسب و کارهای داخلی دونست!
©
kamran_falahati
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2298" target="_blank">📅 17:48 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2297">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">جمهوری اسلامی ۷۱ روز هست که اینترنت رو به روی مردم خودش بسته!
روح‌الله مومن‌نسب (تئوریسین بارداری با ۲ گیگ اینترنت) گفته شرایط اینترنت به هیچ وجه نباید به روال گذشته برگرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2297" target="_blank">📅 17:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2296">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dkPONS6sf4OPUBC9r8D2pSmsHsCX4Ps5ScnuzIfQNRrkcpOI8FxbImxqgr_ogATxn6I9_dUhlq3jy8NVWSphJ9j4JOI_z1OVho1Yrb3gQ6cqm5m4IyeeIxeUEgrx9evOtRcWixdLW4dD2_7NIpmDghUKBm3ZtCLZ6In-0kRm3JEQvFiduTB9Lj4YBMfzB-uXCT1s-RRKSYhRY9FUxKqXjFNO0JZ8fUm032cANWHU2Miyk_1uYS0nCVnw54eQHUvH_OJIT5ZZSni_q6yBqRj_94Pr2gCtXa3cj6pnT1LwfX2GgSDXmUXrOCVOisikXTbs5sXNxCC2ilg8iXQTHFd1ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان Pigeon یه فورک از پروژه تله‌میرور برای macOS هست، که از طریق اون میشه بدون نیاز به فیلترشکن یا لاگین در حساب، به محتوای کانال‌های عمومی تلگرام دسترسی پیدا کرد.
👉
github.com/MaroMushii/Pigeon/releases/latest
💡
t.me/PersianGithubMirror/4500
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2296" target="_blank">📅 17:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2295">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g6DmXDqj46La_MXNLUO6AFoMLy7kyZYXY-DkaCZJwKXlLeVHsdozZgPMirLbycBd-UKI1J5EJUHQOvwgPTxpgj0tNVfIQk1GvYQNvEVL-F_wftUt6SuU21THmmQFTiQc3MLB-usfqQMQSfRrm4JDo1ia6NdK7MSyEYHGCSyLNSoqL1lVTXzZm6Lx8bkyBae3D6jp6t_jQFOKxopZPpX2Gi2KcGeafliVzJ5DOkzU0cS4W4Ielapu8WV3SuZ_xpVWkuFRgEsVSuPPTE1Q9fcNzVmRtprCLLH3QIrWpqLhb_XVIbn4mVcTcQaSQHmkHazkLQMaPfYf595lWu1xL8GP8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Youtube Sandbox با استفاده از GitHub Actions بهمون اجازه میده که فقط با ارسال لینک یوتیوب توی کامیت‌مسیج، فایل ویدیوی موردنظرمون رو توی فولدر Downloads (داخل مخزن) ذخیره کنیم.
👉
github.com/iphoenixon/youtube-sandbox
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2295" target="_blank">📅 17:36 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2294">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lc5x5CBjWkfPkeb7nUbKWvbVFDeLX2tPMWvcSwUf894hwOcoMPWWdlCCJYeZjs_vZe6LAMsCQArOLY6wJ2jw2cH2hCE3bC2K788iberTZsQj_cv2s_NggStSixnr-NtbyQKx_M9WoV48QgyifBra4pmqpWJxx4MBHZMbWTT2yWFhS_K5U7O3wKRVq0kZFU2j41P7h65H6vs9Cs0_sW6MKEvAhI7tqI7NaALLMqDXfITIswKFQjLEdkjc9hm0DDNvkTQ1ILV3Mibi7gLth2hKPGXGWEPVdCZ40nYKYksZHrw7P4oaRiS-4byi3J1zYXGG07F2LS1lMiUNb5V3zZrb8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه گوگل براتون باز میشه و در وایت‌لیست اینترنتتون قرار داره، می‌تونین خیلی راحت با نصب این کلاینت اپن‌سورس به گوگل درایو در اندروید دسترسی داشته باشین.
👉
github.com/aleskxyz/Round-Sync/releases/latest
💡
t.me/PersianGithubMirror/4489
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2294" target="_blank">📅 17:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2293">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kLT60C6-J6LAZJT920JLx7HXKLMMG5C88iPU8OpLuLdr0kupsIw8M9B_HFkl8qoGLZi_VEu4KZlZSqoy83Fm5robA_VmLCJRSRH4SVj_-AV9ULSJTNkmgXC0usValrnTiF-kp3X0K42fjX5QhcIQc3afwCvGnJcJIz3jW6Yt-q4CYKMhLapfE9GczHwKm5t5XWQZ-_9iZiFGVriBmPYcStThoajIGxkH5P1hIvVM_8Pj48bCHrb706tcS3F3hwKRxC9jSMeTsoUVXjbCGCNbVYZCE5IWzOSdF-gD64O0rFAHW-49JqpoFchh2CbwOk7apZ2oGJcLzn0PW5TUL3_LVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید کلاینت ZedSecure از طریق گوگل‌پلی در دسترس قرار گرفت.
در بروزرسانی جدید این‌برنامه پشتیبانی از پروتکل DNSTT اضافه شده، هسته ایکس‌ری رو بروزرسانی کردن، بخش تنظیمات تکمیل‌تر شده و یک‌سری از مشکلات برطرف شدن.
👉
play.google.com/store/apps/details?id=com.zedsecure.vpn
💡
t.me/PersianGithubMirror/4496
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2293" target="_blank">📅 17:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2292">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">۷۰ روز است که جمهوری اسلامی با قطع سراسری اینترنت، میلیون‌ها انسان را عملاً گروگان گرفته است.
این یک اختلال اینترنتی نیست؛ حمله‌ای مستقیم به زندگی مردم است. کسب‌وکارها نابود شده‌اند، معیشت خانواده‌ها آسیب دیده و ارتباط مردم با جهان قطع شده است.
در سایه همین خاموشی، بازداشت، سرکوب و اعدام ادامه دارد؛ بی‌آنکه صدای قربانیان شنیده شود.
اما بخش بزرگی از جامعه جهانی همچنان ترجیح می‌دهد چشمش را بر این فجایع ببندد؛ چون واکنش نشان دادن هزینه دارد و سکوت، ساده‌تر است.
For 70 days, the Islamic Republic has effectively held millions of people hostage through a nationwide internet shutdown.
This is not an internet disruption; it is a direct attack on people’s lives. Businesses have been destroyed, families’ livelihoods have been harmed, and people’s connection to the world has been cut off.
Under the cover of this blackout, arrests, repression, and executions continue while the voices of the victims go unheard.
Yet a large part of the international community still chooses to turn a blind eye to these atrocities, because taking a stand comes with a cost — and silence is easier.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2292" target="_blank">📅 16:29 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2291">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">قطع طولانی اینترنت تحقیر اکثریت بزرگی از افراد کشور، یک‌جا و باهم است. اما این بین، گروهی که شغلشان به‌هرشکل به اینترنت وابسته است، تحقیری عمیقتر و نفس‌گیرتر را تجربه می‌کنند. با آن‌ها طوری رفتار شده که گویا شغلشان "مهم" نيست. حرمت ندارند و می‌شود با زندگی‌، زحمات، اهداف، آینده و برنامه‌هایشان بازی کرد.
©
DevYara
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2291" target="_blank">📅 16:19 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2289">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بر اساس گزارش جاب‌ویژن با عنوان "تاثیر جنگ بر بازار کار"، محدودیت در دسترسی به ابزارهای اینترنتی موجب اختلال یا کاهش فعالیت در بخش قابل توجهی از گروه‌های شغلی وابسته به اینترنت شده و بیشترین کاهش فرصت‌های شغلی در گروه شغلی دیجیتال مارکتینگ و سئو (۸۳ درصد)، طراحی گرافیک (۸۲ درصد) و ترجمه و تولید محتوا (۷۹ درصد) ثبت شده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2289" target="_blank">📅 12:07 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2288">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YFeGQAXFhZpivbL9YyeXQHCWiridz3ZD4fl9ae5iGoC7VFZT1tZnTRCP0l6YfgIF-2MqQgF8xz1rz7rE__Sn-a5hPP7IqemotIBhvt0cF-aqD5BXzrwGm2stvj2NM-Wv2LNZvn-hoUQiWe3nWpS6S50qHr8iEPJQH5mjfkya2y2x3pxPusD9iOGAG_bh3hJ_erssiODSKKB9FUTXhCPUTWNETH_-jAsGs0oKwpm4INc3_WJh7Q9EO2zJ3Cjg6eYtZGxAuVihgl_EgoanYkcRVjwXOqJ_ZXF00DAJjv6PyifVM0YX_0COeT_H-XfxaanCqzGTrk5wqyEocfNP-SYsRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی شاکی است که چرا با وجود اینکه که پول داده، تیک آبی اکانتش حذف شده و ...
در همین حال میلیون‌ها ایرانی پول اینترنت دادند، اما بیش از دو ماه است که یک شبکه داخلی که فاصله زیادی با مفهوم اینترنت دارد بهشون تحویل داده میشه و از دسترسی به هزاران سایت و سرویس محروم شدند. سانسور اینه!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2288" target="_blank">📅 12:02 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2287">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وحید فرید، کارشناس اینترنت گفت: ما تجربه قطعی اینترنت را در دولت‌هایی داشتیم که به ظاهر حامی اینترنت بودند. خود پروژه شبکه ملی اطلاعات یک قدم به سمت ناامنی دیجیتال است. کسب‌وکاری که اینترنت می‌گیرد از نظر مردم رانتی است و روی حقوق مردم پا گذاشته. حاکمیت با قطع اینترنت به جامعه سیگنال ناامنی می‌دهد. /کارزار
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2287" target="_blank">📅 11:58 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2286">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سمیه توحیدلو، عضو انجمن جامعه‌شناسی ایران، قطع اینترنت را از منظر اجتماعی خطرناک توصیف کرد و گفت: در زمینه قطع اینترنت حاکمیت هزینه-فایده انجام نداده و متوجه نیست چه میزان خشم تولید می‌کند. آنچه در این وضعیت تشدید می‌شود، شکاف دیجیتال و محرومیت نسبی و شکاف حاکمیت-ملت است. /کارزار
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2286" target="_blank">📅 11:37 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2285">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cjw5JS9p1QzyQ3YZrplYux6IVfTJXkkukEGuV5hO6mjsOt2y6dVYVAvS1XMns3A0MqRakHDSw7MlRNdjGdyZCUmYrlb2gHNl1Ga9ruNKMYjoHJE4N1S96xc42jpAJS9OTA7L_I75kdPMC_q4G_um87e471BN7uMbp2jrHRC_boUaPLsaQ5kN_3c8qCpPE_4akaXpzdyQQxC9ysA8hDLLlhVYddtWHmBmd5xlHaeksjU1opg-w7BpojbrGUrXpQ7liMBZOWDES78POFrHJVI9BTSjCVcbGMvLntbdOMWqzV5g77aCzG-WC80A8voP1xnp7GKWlFNWSs4JXYeYeDdL0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای شرایط فعلی اینترنت ایران که روش‌های عمومی دورزدن فیلترینگ عملاً کارایی ندارن و اسکمرها و کلاهبردارها زیاد شدن، مدتیه یه مارکت‌پلیس برای خرید و فروش کانفیگ راه‌اندازی شده تا خریدارها و فروشنده‌ها در یک بستر متمرکز و نسبتا شفاف با هم ارتباط بگیرن.
طبق توضیح تیم دیفیکس، خودشون فروشنده نیستن و تمرکزشون همچنان روی ارائه و توسعه سرویس رایگانه. این بخش صرفاً برای وصل کردن فروشنده‌ها و خریدارها از طریق این فیلترشکن و حذف واسطه‌ها ایجاد شده و فعلاً هم برای تراکنش‌های رمزارزی مرتبط با ایران کارمزدی دریافت نمیشه.
در این سیستم، مبلغ پرداختی نگه داشته میشه و برای مدتی بعد از تحویل آزاد میشه، کاربران میتونن به فروشنده‌ها امتیاز بدن و تجربشون رو ثبت کنن و کانفیگ‌ها هم بصورت رمزنگاری‌شده تحویل داده میشن. البته محدودیت‌ها خرید بصورت رمزارز رو دشوار کرده، اما افراد خارج از کشور میتونن برای خانواده یا آشنایانشون داخل ایران خرید انجام بدن و فایل کانفیگ رو براشون بفرستن.
👉
market.defyxvpn.com
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2285" target="_blank">📅 11:26 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2284">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=ZOsmOqnpCi7xbbrcL-7Z1lRfkd22Q5PL4iP1pc2Hs-UVsxAyzxs-mnh_sZ8a-vD-0ElJQZjXqBZZ-Wb8wBKld2xsD97Sn-5VE3bUig-lyyrAnQ3MUh4506Ncuu7Z5v77xUzB6-7XrI4Q8h2-IcBWjmSGdaytkxgk-cKY_iD2q_nfiaJW39GLRso9R6dcK1-y9vPE-3ySCtoOzLkqE2zfiqPrDRz9WtBQM-jQStrhiFayT0nNsXq-PhCaFCqB2ERKMgHk1i4-THmm1jKTAz1IVIGZ2UUB5VgQ1BpZ3vI-SVw_Y3haFDqI4MOqwdFqtRVJ5PTuYJ2TEvPEEgmT-mtSZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=ZOsmOqnpCi7xbbrcL-7Z1lRfkd22Q5PL4iP1pc2Hs-UVsxAyzxs-mnh_sZ8a-vD-0ElJQZjXqBZZ-Wb8wBKld2xsD97Sn-5VE3bUig-lyyrAnQ3MUh4506Ncuu7Z5v77xUzB6-7XrI4Q8h2-IcBWjmSGdaytkxgk-cKY_iD2q_nfiaJW39GLRso9R6dcK1-y9vPE-3ySCtoOzLkqE2zfiqPrDRz9WtBQM-jQStrhiFayT0nNsXq-PhCaFCqB2ERKMgHk1i4-THmm1jKTAz1IVIGZ2UUB5VgQ1BpZ3vI-SVw_Y3haFDqI4MOqwdFqtRVJ5PTuYJ2TEvPEEgmT-mtSZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبقه اشراف و طبقه رعایا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2284" target="_blank">📅 11:01 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2283">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وارد روز شصت‌ونهم شدیم. میلیون‌ها نفر رو با قطع سراسری اینترنت گروگان گرفتن و بازداشت‌ها و اعدام‌ها در سایه خاموشی دیجیتال ادامه داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2283" target="_blank">📅 08:16 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2282">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/piUvwdjDPt-CSxSu22EHl2HeMpBSSVJMZl2upi-w0gTZ3ul84jDxrPO1OlAnnpFSkSgw1gn6tJkcfTsiy7k09PNmqqgcakylTQiZL3PL-vf1XX1crY6gGEsMtP_Y9rxR5hLGAO4Yoi33HsQ0GWJQ0NMgAjmgOjlGONmtVbmZfrtTzNUwnRmdjG7D1R96jzjQrwLV4EmwQNvyvU97-jofSGJjJSp5sEmmr4GtIBi7VaUrINm5re5FnPmE13sBBQAnnk882812IIvGwSgzYBCCMffD_10noc_-z5sds826G9CVEbeJF8MknMP3sDuZ6qGMiKrIrfhrWjMlZuu8Xo5nAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آپدیت جدید از اپ theFeed امکان فراخوانی محتوای کانال‌های عمومی دلخواه فراهم شده و پشتیبانی از اندرویدهای قدیمی‌تر، حل مشکل رندر نکردن نظرسنجی‌ها و ...، بخشی از تغییرات جدید هستن.
👉
github.com/sartoopjj/thefeed/releases/latest
💡
t.me/PersianGithubMirror/4273
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2282" target="_blank">📅 18:20 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2281">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qYya4ZsQaYXhYBAbieId7THjN7rPMnih4YhvO87o5Sbjavoo2ZxrBM7on1CGoqt0YghH-5JIMygtLj3ZR-CSKkEeVXQ08VIdcsD10QQBtSA6FvHitlTV9-jhi0yTaSRtJtfSMTEWExrDN7-ztPnr7rMFNKPSu2lVegvfGPYo0OEW2v9tHVfwuVrymDXfnPbw8NlJRDlT9LhvyX5g6j1mYY4GapAAF1jNEP8yV8SwIidsMxPA6i_AuYtaydZ3JemaCKleWxj7J-dlc-Hs1Gb0wxQu_gssdASalgFv6dbqDWlZzICxiwuSRQvMZvaTEkze64ohWqBp7C0cElTBut3EVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای آسیب پذیری اخیر کرنل (
Copy Fail
) فارغ از اینکه آسیب پذیر هستید یا نه، آپدیت کردید یا نه و کدوم لینوکس و چه ورژنی هستید، همین دوتا دستور رو واسه محکم کاری بزنید و تمام:
echo "install algif_aead /bin/false" > /etc/modprobe.d/disable-algif.conf
rmmod algif_aead 2>/dev/null
ریبوت لازم نداره، ضرری هم نداره؛ چون به صورت معمول شما به این ماژول کرنل نیازی ندارید.
©
tiosus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2281" target="_blank">📅 18:11 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2280">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">قطع اینترنت به بهانه امنیت ادعای مزخرفی است.
پشت پرده اینترنت پرو و سود حاصل از این رانت در جیب “ستاداجرایی فرمان امام” و “بنیاد تعاون سپاه” می‌رود.
حدود ۹۰٪ سهام همراه اول در اختیار شرکت مخابرات ایران است و مهم‌ترین سهام‌دار مخابرات هم “کنسرسیوم اعتماد مبین” است. این کنسرسیوم متشکل از “گروه توسعه اقتصادی تدبیر” وابسته به ستاد اجرایی فرمان امام و “شرکت سرمایه‌گذاری مهر اقتصاد ایرانیان” وابسته بنیاد تعاون سپاه است.
در واقع گردانندگان اصلی این مجموعه و به نوعی مخابرات و همراه اول دو نهاد ستاد اجرایی فرمان امام و بنیاد تعاون سپاه هستند.
©
yasharsoltani
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2280" target="_blank">📅 09:22 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2279">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">۶۸ روزه اینترنت بصورت سراسری قطع شده و در همین تاریکی دیجیتال، بازداشت‌ها و اعدام‌ها ادامه دارن.
قطع اینترنت فقط خاموش کردن ارتباط نیست؛ پنهان کردن حقیقته، اما خون با هیچی پاک نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2279" target="_blank">📅 08:21 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2278">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EQlBZguaJqGyc9e1M9ZpkS8TcDkjiL_9-HOMJKR_9EZ3D_-FxGTRWje5vk6-nP0o3kpMQsfKxrSpGwWOWLzw86lQ797DeS3EVg3LTG-IrXlY-TP_9a79mNhgntNQzuqA15BBgtF7CaPIY7YSzLB5ds_BhZNkubSUNDcT01JoWagxKB92EBY2QjhOtrxi_heK46Cb5KyY0_HHqUqPIiOooBvxKXSfqO_kmFKAiFBP-pn4IiduRN4qczTez4P3ZtIsm5vfsTLS-l1HKmRQRpGRFZwY2nqRPXzsW0LqQs5bMj19e5XnJyD_sQ83d__AlOCtRQbDtoxQKsqlT_3qdUbUDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۲ از اپ متن‌باز و رایگان TeleMirror برای دریافت آخرین مطالب کانال‌های تلگرام در شرایط محدودیت شدید اینترنت منتشر شد.
در این‌نسخه بیلد لینوکس و مک هم در کنار ویندوز اضافه شده، برنامه چندزبانه شده و یه سری از مشکلات برطرف شدن.
این برنامه فیلترشکن نیست و به وایت‌لیست فعلی اینترنت متکیه، بنابراین ممکنه روی یکسری از اینترنت‌ها کار نکنه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4295
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2278" target="_blank">📅 20:49 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2277">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cYGs5axO96ZJDNIzOs-tcg_PzIaNUP7P33cAWBczkz1nPmCvsEMR1E6onT27xquT6PK4l7TVUjlgaUgQS5a-1JCUQz0s7sTbha6UZyDV0E8BPe3deh5WxXzCIrWJqqH5q92WBSq7CMepA5cdDfZ26JX2u1x4W26UPik_VFQhxgGZcOWIehhcOb15iC_he-V0NZ-tymuVUZ0aMXKYQB-ZpECec-a7kqgT5TlM1sEy6mqxgGdcKQTrV_TXyNws-OWZIeheJQK4CW4ur7w_a0ENsM_at2jbNZysV53G7hTA7Nvi3OQSP6aBDYNx2v2fOTGUgfr8l8g6VczOenjd9cJQXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک آسیب‌پذیری بسیار خطرناک در هسته لینوکس با نام Copy Fail (CVE-2026-31431) شناسایی شده، که به کاربر عادی (حتی بدون دسترسی sudo) اجازه میده تا کد مخرب رو مستقیماً در حافظه (RAM) فایل‌های سیستمی تزریق کنه، بدون اینکه تغییری روی دیسک ثبت بشه؛ به همین دلیل بسیاری از ابزارهای امنیتی قادر به شناسایی اون نیستن.
این حمله به سادگی و با پایداری بالا اجرا میشه، میتونه برای فرار از کانتینرها (Docker / Kubernetes) استفاده بشه و تقریباً تمام نسخه‌های لینوکس از سال ۲۰۱۷ به بعد (Kernel 4.14+) رو تحت تأثیر قرار میده.
اگرچه با توجه به وضعیت فعلی اینترنت در ایران بروزرسانی کار دشواری هست، اما توصیه میشه در سریعترین زمان ممکن سیستم خودتون بروزرسانی کرده و وصله‌های امنیتی هسته رو نصب کنین.
©
Bamdad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2277" target="_blank">📅 17:02 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2276">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WFbnjHGqwREB5mbUBcFVLvBK0Z02B9K0aVeNXAWnq99YRiZ1oMbyTX3QtxcBSGqltQhmpKbeDxiG1xozP6t4RYfHSapvVIZbsu7j-qChymMIc0t7Lnm06sZROB6TozO1rQvCpmT-WTpLSYSIQytpYdYYRvo7U4qMpZAqBMmt3Vv07_MxIcKWsbpHvChJxQKlyz9RHb3VF5wxc_dWgPVUD4UCtJ0MhFcwHrV4rpLVt7LXi0cFgh9g517YBMyU-hBaJetBdga2kuJuOQD79MtN6jBnWicks4JhbhveSmgilm3cAsKjpoiLT4GpK6nZz5isBr8RnAwy97eZKoGh4k1kMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل آموزش ساخت فیلترشکن شخصی به کمک گوگل و کلودفلر از طریق متد MHR-CFW منتشر شد. اخیرا یک کاربر فورک جدیدی از این پروژه رو به زبان GO بازنویسی کرده که مشکل سرعت پایین، لود نشدن برخی از ویدئوهای یوتیوب و همینطور یکسری از خطاهارو برطرف کرده.
👉
github.com/ThisIsDara/mhr-cfw-go
💡
t.me/ircfspace/2259
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2276" target="_blank">📅 16:49 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2275">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">توی خبرها دیدم که دستیار ویژه وزیر کشور گفته "محدودیت‌های اینترنت احتمالا تا ۴۵ روز دیگه رفع میشن"؛ بنابراین بنظر میرسه باید خودمون رو برای کابوس ۱۱۰ روز قطع اینترنت آماده کنیم!
😐
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2275" target="_blank">📅 16:42 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2274">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VS2dYmRlQ2bNHN9bFImwsWJ6t1xOlxr31AujqmVzlJR7X0x2tRz9BC8WcM-meLNv7rBweSFqYgF4gZzOp9INnwnHBuBvrHEadOQ-ohGdgvwAZ3CnTdYMKBc7dRb8CvqXZ_rcvjqykD8tOl6HzOMjSSI0Ssw3r6oy3wvuCYeeBo68fA87FOsCuojJlkoTX-bsucl7TrAhqTsexYTeHTaI-DZeviu-sDxjtEah5HpKHFtSms18qSxeCctECSy1vVH6XK3vmeUV0YOE0JYPVFsbg9Q-tRZd2dmPcj_54ck_MOaEdykKCpx9YZBk5eyFwcngPJfjMADuxkJO2fImsNeE8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز خبری در رابطه با قطع اینترنت سفید خبرنگاران توسط ایرانسل منتشر شد، که روابط عمومی این اپراتور گفته نقشی در این ماجرا نداشته و "هرگونه قطع احتمالی دسترسی متفاوت برخی کاربران به اینترنت، لازم است از نهادهای تصمیم‌گیر پیگیری شود".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/ircfspace/2274" target="_blank">📅 16:38 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2273">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QmkWlXhB4q9xyMd7Osxqo6CtH7rloJBF9rSqmu8e6x1CPQ_sSpFeUviXztmb_E7-yzsoaXK7OnrVNVFWAVGnuT9OybyXfU0TeaSiGDcCwdeZFAk47HD3tjGeYoyRUdon7_xHDoKyM1acoUhqOzHenuKycUWCK_UV_1u7WfFujpZgxw-pOeJbd7QVRP7xSoyuLxeeIyVIhZ2ozVJd0I9qEtU_w3UdqVbfhtQRL1_Qnh7aHwFCax99tI_xItdWooWl90o-tPdCciYHULlMnd6MREUN6pmLoP9AkUGRC6R9gAArv_rD5HxQTwzFycVv2WoS6U57zjiukJOuDXkDNuNnPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع اینترنت در ایران اکنون وارد روز ۶۷م شده است. اقدام به سانسور دیجیتال، پرده‌ای از سکوت بر افزایش گزارش‌ها از اعدام‌ها می‌افکند و قربانیان را از دیده‌شدن، پاسخ‌گویی و حق ابتدایی شنیده‌شدن محروم می‌کند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2273" target="_blank">📅 12:26 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2272">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">توسعه‌دهنده اپ SlipNet متاسفانه از توقف توسعه این اپ کاربردی خبر داده و در بخشی از توضیحاتش در مورد علت این تصمیم، نوشته که "توسعه ابزار آزاد، رایگان است اما بی‌هزینه نیست. متأسفانه در جامعه نرم‌افزاری ما، فرهنگ Donation هنوز جایگاه خود را پیدا نکرده است. از سوی دیگر، جنگیدن همزمان در دو جبهه (فیلترینگ از یک سو و خشم و کامنت‌های تند برخی کاربران در روزهای اختلال شبکه از سوی دیگر) توان ادامه مسیر را از من سلب کرد".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2272" target="_blank">📅 12:22 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2271">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کاربران میگن ابلاغیه‌های مشابهی رو از قوه قضائیه با موضوع "پرداخت وجه و تسویه اقساط"
دریافت کردن
، که توسط "نوآوران پرداخت مجازی ایرانیان"، یعنی نام تجاری دیجی‌پی (زیرمجموعه دیجی‌کالا) ارسال شده.
با توجه به اینکه ثبت اظهارنامه آنلاین از طریق سامانه عدل‌ایران امکان پذیره، احتمالا تعداد نفراتی که پیام‌های مشابهی گرفتن اندک نباشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2271" target="_blank">📅 22:24 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2269">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jqr1BSrQ42rDe_rU8F8bYutPH5GgdCc1XqpVunN4GsXfk_5YN2Hdd9aUeea6UaUTGRYbp3rFCJzFgvHLZTXfSx4FgPHq-zfLNQCWkrkXjHAiHKZCl0sz-3CifAfmuGb-5EPvI9tvsOfuP5Dkve5OyatvWN0kixZwvSErHIh7mbwDhHe-keeiBXbUApJeUaIjTNykHmhMUZHCRdHQ_-xCWyRrWQKwPb55WEJMQCPTCMYPMZy6NtuPxxQwx0wOVhzAtNqlqngIb0-7bSzEtAOeCYdeNB3Da-d-OsySE9s9a1VZGZE9wzpOUTDuBY7p98vvR_w0N6gikZ2s5rW1pnk23w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبری که امروز در مورد "ثبت رکورد ژاپن در رابطه با سرعت اینترنت" در صفحات مختلف منتشر شده، مربوط به حدود ۹ ماه قبل هست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2269" target="_blank">📅 22:15 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2268">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/br26d--PRJ70W0Bttb9tdNxYrHZeBCMOfLlvF7UtMO1d0pGCDPVUFqFr8AnovbK3HuaMICdScAAUDnWoTYwy3CYdDrAXwKO70kku1if-rOnHHzqpCpiaPPH_27jF4bs7DgtorUFW-ewbu8VQjnUBMHuk47hKKf6X2FfWJqtKVRmeq9bnJQ_BNJ_16VnRgjCR8vEIVOnBlp2SHGvXZWCBJ2xQMa1SJIm1-2PAo2Eyq42rL9F3bmI-XqpmLP5HtJ5sZQVo_SJlp0xnz37dk0TIjwvR4nmH6o-rK9gCVnra5m3IhYeG91Iga_1CS78aFo8Mce5L5qg145I-RjfEGvYF8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیجی‌کالا خیلی اوقات در رابطه با خسارت‌هایی که بصورت مستقیم و غیرمستقیم به مشتریان و تامین‌کنندگان وارد میکنه پاسخگو نیست، اما در شرایط جنگی از طرف سرویس دیجی‌پی بخاطر ۲۰ روز تاخیر در پرداخت قسط اظهارنامه قضائی میفرسته؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2268" target="_blank">📅 21:57 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2267">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mdgdMV8RlvG7QtkhCzWhqz6KboWUbAeFg10I19Wuq7DCIoEnmnfBvxMUrUfyDAeet3pNDRllire0DBqf-4wgP5gWlipdalPNMnHJoybm7gyDFATVDqbqGLBXMSkyG4u2eGoF8nac-b4shCbCOvsDhysHq_SP_Re_sytzI0beB5RjhKxQpvoh1-Y3uAIAhOOURy5eSk5ZBxj97q4JRIX2MDQOq5HhfZMwNY9R4Hg_7Qg96GEePHtZmc5FvHPJKzYFNRQL68bMYkPOM4vfWv8vqcZFssUtDDRaisVKmkldK5XGU8OYsiZ5gI-IUywA1H-XH0AlA6UfHvSNW5_D0rETfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ TeleMirror یه تلاش آزمایشی برای دریافت آخرین مطالب کانال تلگرام خودم و سایر کانال‌های موردنظر در شرایط محدودیت شدید اینترنته، که سعی می‌کنه با چند روش مختلف پست‌ها رو بگیره و نمایش بده.
این برنامه رایگان و متن‌بازه و فعلا می‌تونه برای دنبال کردن اخبار تلگرامی بدون نیاز به فیلترشکن، یه گزینه موقت و کاربردی واسه دسکتاپ باشه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4128
۱. این برنامه رو برای کانال خودم نوشتم که در لیست بصورت دیفالت وجود داره، ولی هرکی میتونه سایر کانال‌های موردنظرش رو وارد کنه
۲. برای اینکه ریت‌لیمیت نخورین پست‌هارو برای مدت کوتاهی کش میکنه، که با هربار مراجعه یک درخواست به سمت تلگرام ارسال نشه
۳. به وایت‌لیست فعلی اینترنت متکی هست و فیلترشکن نیست. ممکنه روی بعضی از اپراتورها جواب نده، یا خیلی زود از کار بندازنش
۴. برنامه دیتارو از کانال‌های پابلیک میگیره و به هیچ اطلاعات شخصی‌ای واسه تلگرام نیاز نداره
۵. در حال حاضر نسخه ویندوزش رو منتشر کردم، اما اگر بازخوردها مثبت باشه برای مک و لینوکس هم ارائه میشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2267" target="_blank">📅 19:53 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2266">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">در شصت و ششمین روز از قطع سراسری اینترنت هستیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2266" target="_blank">📅 08:59 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2265">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tjSzFUOQeZkRUjSTKBaTZCsx0FQDp8DnfrobP4iRuubZOeKbK_DGAk05AEjLIPTn-z65sgjS1D1jj7rsupo7pA5kvOujj17aMWLowZJbNgoTTf55qY4ZQSsfNz1PbP727cRftnYHiOKYhHWFIy65Kj8oWLR7XeqaqDbDBXabKLYFFWHW6K3p17MqK1QYcBEYLbYqSJwMymmR1N_eec4abFCjXa9Oudvw_WNPZ2atsHbxNIW_n09FtYuGsFNlx2uaPoZZBZKK6NwL0FWNNosUqFG-cMUuycsyHz7XK4wPPCczI_LpBtMQCFgWDZInJMp_T8amaMQKcPRf77PzXiwwNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی‌بی‌سی در گزارشی گفته که شبکه‌ای مخفی در حال قاچاق تجهیزات اینترنت ماهواره‌ای استارلینک به داخل ایرانه، تا کاربران بتونن محدودیت‌های شدید اینترنت رو دور بزنن.
در این گزارش اومده که افرادی در خارج از کشور این دستگاه‌ها رو تهیه کرده و بصورت پنهانی وارد ایران می‌کنن، تا دسترسی به اینترنت آزاد فراهم بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2265" target="_blank">📅 08:53 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2264">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">انجمن فین‌تک در بیانیه خود استدلال کرد که رویکرد ایجاد اینترنت طبقاتی، گره‌ای از مشکلات زیرساختی باز نمی‌کند و در عوض، اعتماد عمومی و پیکره اقتصاد دیجیتال را با آسیبهای جبران‌ناپذیری مواجه خواهد ساخت.
این انجمن از نهادهای تصمیم‌گیر، به ویژه وزارت ارتباطات و شورای عالی فضای مجازی، خواسته که به جای تعریف طرح‌های تبعیض‌آمیز، بر بازگرداندن کیفیت به کل شبکه اینترنت کشور و صیانت از حقوق کاربران تمرکز کنند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2264" target="_blank">📅 08:51 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2263">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R-wMGw9f9-A9UgMUiMyBGAuZK2nrPl82QKm6ZeGBHOdTNn8Ss01MOTCrjrbwRqek9VgyaFcE2sCA3jWd9CUAptc1cUvIBrGq205x1wMlXo9EYIeYgaBs91thCvf1-EK_FRtyDCw2pAIeq9kVS6OND9XQy_CpCFfwl-if_3vFzblc1Jb4EWNqZ7wZ6Py1S3c5yAa3GY_s_FNPWu3HMxrRrlEjkdpCfvvZ9t8V5gy0ESs_fyOvY5XSIyGG1l3QVjnRl53pGUc9jv0-dAEVmXMTxPFIRsWrKvf6CPZQr1doEf83-bLNIrdE1SOZyX8h6-QtqPlJNk51o9mQKC59CZYsVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: داده‌ها نشان می‌دهند که قطع اینترنت در ایران وارد شصت‌وپنجمین روز خود شده؛ این در حالی است که نگرانی‌ها درباره وضعیت حقوق بشر در کشور رو به افزایش است.
از طرف دیگر دسترسی گزینشی و سطح‌بندی‌شده برای عده‌ای خاص برقرار است، اما عموم مردم همچنان از ارتباط با جهان خارج محروم هستند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2263" target="_blank">📅 11:13 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2262">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بلومبرگ در گزارشی نوشته که قطع طولانی‌مدت اینترنت در ایران دو پیامد اصلی داشته؛ از یک‌سو توازن قدرت رو به نفع نهادهای امنیتی و نظامی تغییر داده و نقش اونها رو در مدیریت امور کشور پررنگ‌تر کرده، و از سوی دیگه فشار قابل‌توجهی بر اقتصاد و زندگی روزمره مردم وارد کرده. در این شرایط، دسترسی محدود به اینترنت نه‌تنها ارتباطات و جریان اطلاعات رو مختل کرده، بلکه کسب‌وکارهای آنلاین، تجارت و خدمات وابسته به شبکه رو با رکود جدی مواجه کرده.
برآوردها در این گزارش نشون میده زیان اقتصادی این وضعیت فقط به تعطیلی مستقیم کسب‌وکارهای دیجیتال محدود نمیشه؛ اگرچه این بخش به‌تنهایی روزانه ده‌ها میلیون دلار خسارت ایجاد می‌کنه، اما با در نظر گرفتن اثرات گسترده‌تر مثل اختلال در زنجیره تأمین، پرداخت‌ها، تبلیغات و کاهش بهره‌وری، مجموع خسارت‌ها میتونه تا حدود ۸۰ میلیون دلار در روز برسه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2262" target="_blank">📅 08:37 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2261">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">روز شصت و چهارم از قطع سراسری اینترنت.
لعنت بر جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2261" target="_blank">📅 08:35 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2260">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کاربران شبکه‌های اجتماعی از جان باختن حسام علاءالدین، شهروند ۴۰ ساله که گفته می‌شود «به‌دلیل داشتن اینترنت ماهواره‌ای استارلینک» بازداشت شده بود، خبر می‌دهند.
بنا بر گزارش‌ها، او که پدر دو دختر بود در اثر شکنجه در بازداشت جان باخته و پیکر بی‌جانش را به خانواده‌اش تحویل داده‌اند.
©
indypersian
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2260" target="_blank">📅 19:31 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2259">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نحوه ساخت فیلترشکن شخصی رایگان به کمک گوگل و کلودفلر، از طریق متد MHR-CFW ...
📽
youtu.be/L3lJZrAqqUQ
💡
github.com/denuitt1/mhr-cfw
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/ircfspace/2259" target="_blank">📅 19:22 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2258">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GtyYoCsEU3Kng0Xsc_IcXiicAVV5EGgrwH-c5G3klscknYc2duFbG1UqGHIAr685EP7CpuGXp1FouE8PxQL0wKSpKuLP3M_L-yfOiigVhrPoQbq0lFcJTzJsdzBA8UqRoBpjeJ9jVA14Ft64esWhz74BjhyepGVyIlhiNQxatyaBu0uTstwbdS1MHHEEPoVRpwE3R97wFUXO_M_0WCMCoSSnEXsWzJtKR7DXDYd3T6kDG_KPSGjKesFF-8zXaa9aWU4pXlbnEJTGHVFvE7eYTVNBeZXhATrwRK7xt2r6olQUjsGEstgRAuhorcH37OWd5qUrBeCDLE1lg8WVSnKvJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با روز شصت‌وسوم از قطع سراسری اینترنت در ایران، گزارش عملکرد سه‌ماهه اول سال ۲۰۲۶ شرکت Meta Platforms منتشر شد، که بر اساس اون تعداد کاربران فعال روزانه این شرکت به حدود ۳.۵۶ میلیارد نفر رسیده و نسبت به سه‌ماهه قبل حدود ۲۰ میلیون نفر کاهش نشون میده؛ هرچند این شاخص در مقایسه با مدت مشابه سال گذشته همچنان رشد داشته.
متا اعلام کرده این افت فصلی عمدتاً به دلیل اختلالات اینترنت در ایران و همچنین محدودیت دسترسی به واتس‌اپ در روسیه بوده. البته در پی انتشار این گزارش، سهام متا با واکنش منفی بازار مواجه شده و در معاملات حدود ۷ تا ۱۰ درصد کاهش یافته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2258" target="_blank">📅 19:13 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2257">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بعد از ۲ ماه قطع سراسری اینترنت و شدت‌گرفتن تعطیلی‌ها و تعدیل نیروها، پایه حقوق وزارت کار بنابر مصوبه شورای عالی کار ۱۶ میلیون و ۶۲۵ هزار تومن تعیین شد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2257" target="_blank">📅 17:39 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2256">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انجمن صنفی روزنامه‌نگاران در
موضع‌گیری
خودش نسبت به اینترنت طبقاتی و حق دسترسی به اینترنت آزاد حرف‌های درستی مطرح کرده، اما خبرنگاران جزو اولین اقشاری بودن که به اینترنت سفید (یکی از
سطوح
بالای اینترنت طبقاتی) دسترسی پیدا کردن!
واسه همین این بیانیه بیشتر شبیه یک موضع‌گیری تشریفاتی به نظر میرسه، تا یک مطالبه جدی و فراگیر. اگر رسانه‌ها واقعاً به این حق عمومی باور دارن، اولین قدم میتونه شفافیت و انتشار فهرست کامل خبرنگارانشون همراه با وضعیت دریافت یا عدم دریافت سیمکارت سفید باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2256" target="_blank">📅 17:33 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2255">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HVHUZvuH0uXn3y7xPmoMZ590wNnOwC0lXiTqb_3Z7CkYaaHS1nDF_b2rWqzpVSKIOcLClEwm1M3EexonBU4pdl6FP2-IuKiuxwPVd7W4WoJ1c4lCE9kBbr41f6IvUaNHX2wAsDa4B0hRW8l7l2ek8GJevgOFGbDxLnxSFZcTW8T0AtQUASPMq9SqHlQFwc0QxPT6Yl7ZEd8uF7z2abHhjVuzVMw87ddMZeKbeOuo9Kt8-Y142R0i8H6zZebMFCy_tH06jkOaqq5CGsGiumWup60O5dsoDh3NZL4nSWzDrRxDdk6SGy52QVVYHLau1g8tKQ7A0aQSq_py8qwuetV84A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن صنفی روزنامه‌نگاران استان تهران با صدور بیانیه‌ای تأکید کرد: دسترسی به اینترنت آزاد، باکیفیت و همگانی یک امر تشریفاتی و لوکس نیست، بلکه حق عمومی است و دولت‌ها موظف به تأمین آن برای همه شهروندان هستند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2255" target="_blank">📅 17:27 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2254">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/appJv0Z_G9y-JNN2KHRqcvmTR1BOk9CDhv-OrocME4pXpcD32ClooIpNgly0nBhsw9_yPnQgLBjWADRc1aaWowXamcQLUObms8YAEz_9P9yOZpUTornbXagK4cDSj6Ml9FyurmtlfGloVgG9jzD2X-LLkSAo0z3PWPqQvSUooDDIrF4bip6hDttYvx30Ti2sSHcRSifmw8yTGBsZ7xoxB42icvuL4AhBSnCo2CZ3OH2s8K50I6IUJo_cTgs6FoIVgCPhwkzdxPMUmGBaIPLM3r-gxJeXE0GQW3Y4FgLN3uBKMSvDbWVnAxaXM5RgK5TlSjq8Pzy5_4sxVTUztVDguw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایفون در بروزرسانی جدید اپ اندروید Conduit گزینه Personal Pairing رو اضافه کرده، که میشه یک لینک اختصاصی دریافت و با دوستان یا خانواده به اشتراک گذاشت.
این لینک رو باید در داخل اپ سایفون از طریق بخش Pairing URL وارد کرد، تا مستقیما به ایستگاه کاندوئیت کاربر موردنظر متصل بشه.
البته با توجه به قطع سراسری اینترنت، فعلا سایفون بصورت عادی برای کاربران ایرانی قابل استفاده نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2254" target="_blank">📅 17:15 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2253">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c8H1ArANeLOnCLj-gta33qgSAEo17mA47Cfx2l3XSu48GhoDhpJcPWqx1VA1ZwyaOvXl7Dxl3_C54cbhKzLcXD8ifObFE8k4KF-MktOYSTfZwuOrlKTtDKrHeoyfGnK7X_gG3HsGXkLYzlidg-UoKNxsgxsybJNwfsMGBatoEIwUHwtebyS1cmw6Fsq891EEuAapJ3oTxFJ-Pp_exxD1dWRt-trlhE18GEVSnMz2J0hDM0S3dLP7Fh236nJHjodXJO0LGZY3EerHsG_d-wV6EyTC-5Gt8ckKwHNpJO0u2qQQReQ1FeklIYtfkGc_bdO8ctUU_kD2YK4b8X66eeQDNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش تازه سازمان گزارشگران بدون مرز نشان می‌دهد ایران همچنان یکی از سرکوبگرترین کشورهای جهان برای روزنامه‌نگاران و رسانه‌هاست. جمهوری اسلامی در میان ۱۸۰ کشور، در رتبه ۱۷۷ قرار گرفته است.
©
dw_persian
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2253" target="_blank">📅 17:03 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2252">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">روز شصت و دوم از قطع سراسری اینترنت در ایران!
میلیاردها تومن پول داره توی زمین VPNها میچرخه که بخش زیادیش میره توی جیب جمهوری اسلامی و حامیانش. شیرینی همین پول‌ها باعث تداوم قطع اینترنت بین‌الملل و تمرکز روی اینترنت طبقاتی شده.
جمهوری اسلامی ده‌ها هزار نفر معترض رو در دی‌ماه قتل‌عام کرد. یادتون باشه بخشی از همین پول‌ها که بابت
#اینترنت_پرو
هزینه می‌کنین، قراره خرج گلوله و سرکوب مردم بشه!
©
Maroon
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2252" target="_blank">📅 08:35 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2251">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/esxQZ9uGjPRryNoe76EDziOTUJEsU-w6i3RW31Eet_y-i1MX-FGyUPmxnHXGdNCZ-yw6Xa4NQBOmHAVCiTPw5mMXghJIYXjHtHY6n5EneMbr9SMu9ZPSvWzJux9me8sRYMNqTh7dl7U9DBUrB-KKrimw5ZV9M8elwbXrcXXWlMIXE7jSZ0CxcpPEW74bGQiK_4yTWTiNBadZ1Tu82eb4uwCxCJCSgTz0maIjx7_iSGwLqmDiUSBOK9Z0LlOcq_MTP_T4mYBEM9b5z2GCJE8TdwVAP3rIXh8f8cJ0V9ocNU69uWqD4LPm1CAIQWAor6TwwW2QG30X27wb-kObgBUuhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلیمی، یکی از نمایندگان مجلس گفته: رئیس جمهور و وزیر ارتباطات مطرح کردند که ما مخالف اینترنت پرو هستیم؛ پس چه کسی این تصمیم را گرفته؟ رئیس جمهور بورکینافاسو و وزیر ارتباطات افغانستان این تصمیم را گرفته‌اند؟ رئیس شورای عالی امنیت ملی، رئیس‌جمهور است و باید در این زمینه که می‌گوید ما مخالف هستیم پاسخ دهد. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2251" target="_blank">📅 18:05 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2250">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F1aEM5EMnQUI1GRFSOC_4rIVWSgSfQzjPn71853Njwl8SsMnjbx0UWcFJd9bBXQfGA39Bbx6cY9geYnf9IUVJGrnDFDB2besSeCJdN1ILJoYiqs4kcdkx9MfDyFySg229R3J-jQiSky98teIsjrHi6tu8f70JsxLfDgFidLzbBEiHxK5ukhqu27gu4LxNQq1XG8pD7vvLPnfJG-ne9Y4lanOoGNqkg2YLj0dPnVgM_ZhiBf1HbldmvCJh-dXtjcUERnb4tBB24OVcD8BOP6FIBHLjMYJx4ZVss44Ijy3rwIpfoMo93qLgTZjxGgkdjIDZXN9aqX126Capo170vD0Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت ما را به عصر حجر می‌برد!
انجمن تجارت الکترونیک در بیانیه‌ای اعلام کرده که قطع گسترده و طولانی‌مدت اینترنت در ایران دیگر قابل توجیه با ادعای «امنیت» نیست. این انجمن با اشاره به بیش از ۱۰۰ روز قطعی در یک سال و بیش از ۶۰ روز قطع پیوسته اخیر، تأکید کرده که این سیاست‌ها نه‌تنها امنیت ایجاد نکرده، بلکه اقتصاد دیجیتال را تضعیف و جامعه را با آسیب‌های جدی روبه‌رو کرده است.
در این بیانیه آمده که حتی در دوره‌های قطع کامل اینترنت، حملات سایبری مهمی رخ داده و این موضوع ادعای ضرورت این محدودیت‌ها را زیر سؤال می‌برد. همچنین هشدار داده شده که گسترش «اینترنت طبقاتی» به معنای تبدیل یک حق پایه به امتیازی محدود برای گروهی خاص است و شکاف اجتماعی را عمیق‌تر می‌کند.
به گفته این انجمن، مسئله تنها دسترسی به اینترنت نیست، بلکه حق دسترسی به اطلاعات، ارتباط و حضور در جهان امروز است؛ حقوقی که با ادامه این سیاست‌ها نادیده گرفته می‌شود و هزینه آن را مستقیماً مردم می‌پردازند.
©
filterbaan
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2250" target="_blank">📅 17:46 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2249">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NyOjjennwUcA_LQm9wj36XGVm1axqTQla25JbfwoQQOCUmG5ht_667TnAgtC8_dloV5NX5q4XS6B5RAQZbJnVR8B-HhPCOrWznGcBzz9tSnGNz3xbe2BGfRqBlyZS8RfSREgyIkJpCGRNAkMXXK1hQ8Y9p_CfPHFbxwYlYuqA_r1oZDTlEF6TdhIFTwDk3agYmu2Lb1udXGFWmbNlkq5ZaU20adkuirOCde5DuB8VMSRc9GbQpMHeAmP9KaqXNPZ7eBejj6B1caO_6K0BtagJsgTwfIJC7tn6uxg-uCA_xdAnZ4ilft0aO7F5lFgNsg03jt1mRc3v3vjpMyfcAC6HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو نسخه جدید CFScanner، دامنه‌ها آپدیت شدن و هسته ایکس‌ری به نسخه جدید ارتقا پیدا کرده. یه قابلیت هم اضافه شده که می‌تونی خودت دامنه‌ای که برای Fronting می‌خوای رو انتخاب کنی. همینطور پشتیبانی از Xray توی اسکریپت bash اضافه شده و نسخه Xray تو بخش پایتون بروز شده، تا همه‌چی هماهنگ‌تر و روون‌تر کار کنه.
👉
github.com/MortezaBashsiz/CFScanner/releases
💡
t.me/PersianGithubMirror/3624
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2249" target="_blank">📅 17:28 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2248">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yu8jXOZglNpOHPebzTBsJSlxMJj9bpj95uZnJ0QVqL-nILXmMkp2Z_mfmWjh-unfi0LFTTuJyH9w-qGffzeQGwNcVLQKy03OO_yYlcSiHqeXxjOLmq_SXEOAmO1t0kq-SN-kDZcwIFMASuxE1BvnG0wh9OpeVTV6Aqi7DOjqf0B90ALex0VtpWlkJ8eq5OHYGMs6xPPFC89Ka7m3SXkFPraU__EWf0H-wRz-v13D-piD9jHoyX2mDJ78XsfL5lyp7ww3x0DCG1JG2KM7DWM7pQTguONmFRt2sOHLsYU8ineWzQZozX2fc76PsdWESAfgNzqRac--J0J72IzfdKkfJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن علمی روان‌پزشکان ایران اعلام کرد "اینترنت بخشی ضروری از زندگی امروز است و محدودیت یا دسترسی نابرابر به آن افزایش فشار روانی، احساس بی‌عدالتی و کاهش اعتماد عمومی را در پی خواهد داشت".
©
shima23972921
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2248" target="_blank">📅 17:08 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2247">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">روز شصت و یکم از قطع سراسری اینترنت در ایران.
لعنت بر جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2247" target="_blank">📅 08:48 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2246">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NcjlhXpvVgAO0omuvjcSSqbZwuRJekLr-jHHshGr8Vl0IvsdOvps335v4M9ZXQIYe-dtMckG5jjx2ZhtiB0DSf4dc2DokcpX5q2cbfPE9wSdPoL6OmCOui6_8jQ0QBJL0cgfRfQQ91Hx9P-FkVm4TTrBdHJp2L_QAqAQPvJUtm7aLIu6ACymX5pW_dd4eZsiflRFONRAnsjJfm9w9tX6i0BRTOUFa0PubSI-BkW0U7OqPGmDXo1i3J_m_Y-3m0YJBDpYltFvcc7z8ruwnGX1UiGvxgaCd3r2ri77qSVlmi-XMGDGusKSoxhlFPCTjZscHuzwhAlXARmbq7nq97aHJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به واحدهای قضایی دادگستری نامه زدن که میتونین از
#اینترنت_پرو
برای انجام امور جاری و تخصصی استفاده کنین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2246" target="_blank">📅 08:41 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2245">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">هیچ‌کس از هزاران فرد دارای معلولیت که از طریق اینستا آنلاین‌شاپ و درآمد داشتن حرف نمی‌زنه. قشری که نه حمایت دولتی دارن، نه جایی تو فضای شهری و نه سهمی از استخدام‌ها‌.
©
Mtherofcatsings
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2245" target="_blank">📅 18:35 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2244">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اینکه می‌گویند قطعی اینترنت «روزانه ۵۰ میلیون دلار» ضرر دارد، یک مغلطه است؛ این عدد فقط نوک کوه یخِ خسارت‌هاست. ضرر واقعی در نابودی  کسب‌وکارهاست، خصوصاً کسب‌وکارهای کوچک و استارتاپ‌هایی که شکل‌گیری‌شان سال‌ها زمان و هزینه برده. با هر قطعی، بخشی از این اکوسیستم از بین می‌رود.
از آن بدتر، این خسارت متوقف نمی‌شود؛ وقتی درآمد افراد قطع شود، اثرش به کل اقتصاد سرایت می‌کند و یک زنجیره از رکود ایجاد می‌شود. بنابراین مسئله «۵۰ میلیون دلار در روز» نیست؛ واقعیت این است که قطعی اینترنت، در مقیاس میلیاردها دلار به اقتصاد کشور ضربه می‌زند.
©
hiddify_com
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2244" target="_blank">📅 18:33 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2243">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رکورد ثبت رزومه در جاب‌ویژن شکست و بیشتر از ۳۱۸ هزار رزومه در یک روز در این پلتفرم ارسال شده. این مسئله نشانه‌ای جدی از تعدیل گسترده در بازار کار و تقاضای انفجاری کاریابی در پی اونه. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2243" target="_blank">📅 18:28 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2242">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XvjLb-YbVZJN0qdMQzBTW-kgByL6bzC0gcspM0h8CoEk-qwqlE6WXrsa27jaf2luyr9ph07dGQhuZfJ7UXxRxFdMPryKORqItO60F9CQN9fatp9gj35AmHdaLyvQhWMZQIfxw7OTzqiyIbQyBlPasvtq0xB7BSWlx4t1jRlVhc6qT5BaFs-YdLW2uVXdF_BjxaPv8Aop7FCH6peyi6WcZ5Pd7kVgjRtxpsgHZNEHb__QQT3ef_zNOerisNEgi0HZK1FnZDSWWSR7CdZ3ucaZ-wktZWdF23mZkL_QciCxZ1eyxt_L9dYRlTZ0OVOoqV6KkRw49UBcJ1mSF6MhwU-ceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی وزیر قطع‌ارتباطات رو از برق بکشه!
۶۰ روزه اینترنت بصورت سراسری قطعه و بازار
#اینترنت_پرو
داغه، مشخص نیست هاشمی در مورد کدوم تلاش حرف میزنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2242" target="_blank">📅 18:22 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2241">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hZPN954elYabE38gx0R7nncyW0ot879So-vxsrJawRfA_lc-pny6A9PzZOcBEeaXQaUpnMzdbpFr1rS_ZgVICiF85kYN1Ekl9Z7Pu3MF-pYSBLgXfO3oPKOK281iyE9CA6LmY8wgdBInhBSspZzoAixpX7tVfyist2jvssP9AmxMso2o5uj604QC2cCREzO_Zsvob0AJVDUNimmW0qKZ6XS6fVnggPRnAhp5_aSGYFOocq3YuLa9X6CqWOb-OtDhq5AyloviPrBAnvxRN5_VqPCcLpD6NpGTIF5gDVQvaVu4V8_RIguvFaqkLtBrY1NKl4a8olmMW9HnQ9X5Q-fRLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد روز ۶۰م از قطع سراسری اینترنت در ایران شدیم.
وقتشه اسم وزارت ارتباطات رو به وزارت پست، تلگراف و چاپار (به جز پیجر) تغییر بدن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2241" target="_blank">📅 08:58 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2240">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">به بهانه‌ی امنیت اینترنت را بستند و حالا گروه گروه پول زور می‌گیرند و باز می‌کنند.
این یک تلاش برای خرد کردن یک ملت به دسته های کوچک است که راحت تر خفه کنند، بیشتر تجسس کنند و مردم را آلوده‌ی بازی کنند تا دیگر حق‌شان را طلب نکنند، وگرنه امتیازات یکی پس از دیگری قطع می‌شوند.
©
souzangar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2240" target="_blank">📅 18:12 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2239">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پیام‌نرسان "بله" خیلی عالیه، پیام که میفرستی باید بعدش اس‌ام‌اس هم بفرستی که بله رو چک کنه؛ چون اصلا چیزی تحت عنوان نوتیفیکیشن نداره‌.
©
aboIfazI
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2239" target="_blank">📅 18:08 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2238">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mm2ThgZRT_uCvbkovuVAP0R09XsfeFTfAZAt0rjvEOOUIDQ-XkEcqCTI1MEfOr583Qd7AH84PiACiSSYCEYoXjM-51Sfh6DOhJLMZ8SdsdkJzAMts_tu_BbMbCYp-N6siDsfKv_0NV9CF6cFQVLv_aBvG-sbgerZ-KrFSVCI_9WFm1i5BPDZrdr9MQJCb0ikom5s4Z10_ZkmwUNajabtFHFFXmv5boA7F1pYGEDjpP35rtKOZxVVmWqQsRblSEdGGZbClSTuDD8MR90OJW0LFCG2j9F_ZL9mGzMfLShiaocY27FMMXCQHdWvzwJ1kDu1khyR0KqA3pNB1M4NtunEcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت
#اینترنت_پرو
در بازار سیاه حدود ۱۰ میلیون هست. مافیای
#اینترنت_طبقاتی
لطف میکنه ۵ عدد اشتراک رو بصورت عمده به قیمت هر عدد ۵ میلیون تومان (یعنی نصف قیمت) عرضه می‌کنه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/ircfspace/2238" target="_blank">📅 17:59 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2237">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R45PJsuqQwau3KliDE-KVFQjPlMRKOebqOcD06_8ZZUlQJuaytHZvm8CU-CP90rc3JBwRmG87qH6ph87y4JoY9PJYwwVR2LC3Xee0Daj4o-3RhMgDGXabkc-7DMbac1ZRiswRDMsJrAE1NTIx7mJfCPXUdbCqM1OMjt_QT7YLIIUZ0TyhThGRYpQxuR6CfpbwsgtDlrjQHX36lpt7j2IEE6_BjlFUALCGqUqogqoT20LD6lJrRD9vZbBfx4dLjxk_yYVZX2RROqs4f3Jk62l0tjLhmXgU5dLNuIBvytwaS573zeq1_7iuUw7bO-bYIR9sMb8DcsIP-d3A2bxwIoO3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت حدود ۲ ماهه اینترنت رو بصورت سراسری قطع کرده تا طرح
#اینترنت_طبقاتی
رو جا بندازه. بعدشم با کیسه دوختن برای مردمی که دنبال حق طبیعیشون هستن، یه بازار سیاه برای فروش آیپی رانتی و
#اینترنت_پرو
راه انداختن.
قبل از اینکه روش تازه‌تری مثل «پرو-پرو» برای خالی‌کردن جیب ملت پیدا کنن، چندین کانال مختلف دارن هماهنگ (حتی توی رنج قیمت) همین اینترنت سفید رو به مردم میفروشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2237" target="_blank">📅 09:17 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2236">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">در آپدیت جدید theFeed مشکل نمایش بعضی پست‌ها به شکل نظرسنجی برطرف شده، باگ هنگ کردن اپلیکیشن رفع شده و امکان اشتراک کلاینت روی شبکه اضافه شده.
پروژه دفید یه راهکار مبتنی بر DNS برای دسترسی به محتوای کانال‌های تلگرام توی شرایط فیلترینگ شدید اینترنت و مواقعی هست که همه مسیرهای معمول بسته میشن، اما DNS هنوز قابل استفاده می‌مونه. ایده اصلی اینه که بدون نیاز به اتصال مستقیم به تلگرام، بتونی آخرین پیام کانال‌هارو دریافت کنی.
سمت سرور (خارج از ایران) به تلگرام وصل میشه و پیام‌هارو می‌خونه، بعد اونهارو بصورت پاسخ‌های DNS از نوع TXT و به شکل رمزنگاری‌شده در اختیار کلاینت قرار میده. سمت کاربر، کلاینت با تعداد محدودی کوئری DNS میتونه این داده‌ها رو بازیابی کنه. طراحی سیستم طوریه که مصرف کوئری پایین بمونه و در عین حال در برابر محدودیت‌ها و فیلترینگ مقاوم باشه.
برای اینکه ترافیک قابل شناسایی نباشه، از تکنیک‌های مختلف ضد DPI مثل padding تصادفی، تغییر اندازه بلاک‌ها و پخش کردن کوئری‌ها بین resolverهای مختلف استفاده شده. کل ارتباط رمزنگاری‌شده هست و هر درخواست بصورت مستقل پردازش میشه، تا ردگیری سخت‌تر بشه.
کلاینت یه رابط وب داره که امکاناتش فراتر از فقط خوندن پیام‌هاست. امکان جستجو بین پیام‌ها، کپی گرفتن از چند پیام، نمایش لینک‌ها، ریپلای‌ها و تا حدی نظرسنجی‌ها اضافه شده. اگر سمت سرور اجازه داده شده باشه، حتی می‌تونی پیام ارسال کنی یا کانال‌ها رو مدیریت کنی.
یکی از تغییرات مهم نسخه‌های اخیر، اضافه شدن بانک Resolver مشترکه؛ یعنی دیگه هر کانفیگ لیست جدا نداره و همه resolverها یکجا نگهداری و امتیازدهی میشن، برنامه هم بصورت دوره‌ای اونها رو بررسی می‌کنه تا بهترین‌ها استفاده بشن. یه اسکنر داخلی هم داره که می‌تونه رنج‌های IP رو بررسی کنه و resolverهای سالم پیدا کنه.
👉
github.com/sartoopjj/thefeed/releases/latest
💡
t.me/PersianGithubMirror/3393
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2236" target="_blank">📅 09:01 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2235">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u7NNpTxbC24YzOCdGKlIuxG9bLn_Lalr9gibd5IqZAj77iGliyS1Fc2s3W09so1nb0sfeT4so5EH_-kSQUrcVH7XlpPM8DVvbQxyK05i8Qt6a_SaNUj6L6OxV8wuy4AABWHrF3kpK-QBrPvA2lna89eRXal78IrB2T9oIvpSDRN9-vvvaK37hDFg67MIQNJSrHlZbvt_p74x2xEMVtk-MDe-LrrnlqEFWBlWLvo61744iEtbMIOqazCZdLeSfx9baxNEDJ4EsQGA72KXKirAMzxWt43iTn7xOyvuQs_ReQUPf5soj3B1ERFK1CWfEMyUBPW54I0yutfRdV1Ekjb-Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Loole یک ابزار مدرن برای مدیریت تانل SOCKS5 در سیستم‌عامل macOS هست، که برای عبور از محدودیت‌های شبکه طراحی شده و با استفاده از Google Drive و روش MasterHttpRelay، یک مسیر ارتباطی پایدار و کمتر قابل‌شناسایی ایجاد می‌کنه.
فرآیند راه‌اندازی بجای درگیری با مراحل پیچیده و زمان‌بر، از طریق یک ویزارد ساده انجام میشه که کاربر رو قدم‌به‌قدم هدایت می‌کنه و حتی بخش‌های حساس مثل تنظیمات Google Cloud رو با راهنمایی دقیق و لینک‌های مستقیم پوشش میده.
👉
github.com/g3ntrix/Loole/releases/latest
💡
t.me/PersianGithubMirror/3455
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2235" target="_blank">📅 08:52 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2234">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">من تحقیق کردم، چون اینترنت پرو گیگی ۴۰ هزار تومنه، دیگه برا جاسوس نمیصرفه جاسوسی کنه. اینجوری امنیت تامین میشه. ایول.
©
SMoslemi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2234" target="_blank">📅 08:40 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2233">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یه تشکر هم از بچه‌های سوپر اپلیکیشن روبیکا بکنیم. واقعا ساختن برنامه‌ای که فیلتر نیست، ولی از اونایی که فیلترن ضعیفتر و کندتر کار میکنه کار آسونی نیست.
©
danyydrinkwater
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2233" target="_blank">📅 08:39 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2232">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/STa2hgjmuBLpSgE1yLuy-YS8nrZpenECdK23Gu3PIPKY2hG0pfjQCOb4B_draPMoCUr25sWA83vutQSEqCr1NTSsxfPSp70eASHxHhV3bXH7aLuL5ni2amVnp-CiZ74D35Ls5cic0TAUd7Kmhf_DluwL73Ph0FI5jnyR7bDgoj6nPDit9M7LuSUw-xX_s_SPbziXe0rg_mbHXTQuzyw-EDWBe9qj_ZkJsChukDv-N2aMN9zV5CAkZV7dfcCC6sj9O92hC7K9mWPV-E60yb1Qfz405r639n5BKHib_yLnkIicPGUc61XazdLgTKZwqBJ8cLOSm3aOx_sgJdhaJUpeLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۹ روز با قطع اینترنت مارو از جهان جدا کردن؛ به اسم امنیت!
بعدش اینترنت رو سهمیه‌بندی کردن و گذاشتن پشت باجه فروش.
اسم این دکان‌بازار امنیته؟ یا رسمی‌کردن نابرابری؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2232" target="_blank">📅 08:36 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2231">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GB0blfcIazzkIRcIAlXAvHd6XPYch3BTaIENM81hhcYD3_Lsw7Mi5FEIC5ghA7gPF_XpwjSKoZml1mKVkXy8u_c01zlMYGUhS6hSIkQK5XwUA8e203wMvVjtAAOyvcNhquTzpfp1V_0RIOtq-0W7XFXvl7lP37qmnlLA1HwTn61nL7YLyEZi_r__0_pZSzySAm9cP6W3zWrEud_yNIUk2RYT9xEASBZB1p8r9g0hbzSLbSItpbnqAfYdu_PhQT0iq8OB6Dly-N0uzixGMz3Jx-puwpKMsAxYGmcQoO9c48jRlpuSnmg-HeyOSA0OP6OfClcaPl0nNA1FZHIkizbrNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبقات مختلف
#اینترنت_طبقاتی
©
mamlekate
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2231" target="_blank">📅 19:03 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2230">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دولت همچنان بر مخالفت خود با «اینترنت طبقاتی» تأکید می‌کند، اما بررسی‌ها از چند منبع نشان می‌دهد طرحی که امروز با نام اینترنت پرو شناخته می‌شود، نه‌تنها به تصویب نهادهای بالادستی رسیده، بلکه اجرای آن به‌طور مشخص به دستگاه‌های مربوطه از‌جمله به مرکز ملی فضای مجازی سپرده شده است. /شرق
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2230" target="_blank">📅 18:28 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2229">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DeSk90OtsfsOpkPrchuRsVEASZC4MV_jsF-_W9C6ODOq-7B44omGbPbBZkI-_GUfWIMrrw9P5JX_po2WiJ67wrB_Ma8uJ05giYxRYM1CAOqcVCbPSQY0urFYBAZRv4YwD5NDZIeRzf4NWhp71xz71aYVfvP1QiDFky787AYLKqrfrwpTtflNO9mBK3FX8EcRlRwJA8tAHGDO4nkCZWzJMXv1K2xcU1B8_mrMTyHZBTgDLF0DcqAxlZiNSWj3y8I7QYkt5FOwdoNaVbx3U0XGitQ2FlA8Aund9EjRBxy2ZaSBHeX1zHkcAUt2vT9xWxVZriWELmRBeBbH5vwo4igRdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا جمهوری اسلامی یه بخش زیادی از بودجه پدافند غیرعاملش رو‌ هزینه خرید لایک از پاکستان کرده. باقر و عباس هر مهملی میگن ده‌هاهزار پاکستانی براشون لایک می‌ریزند. قبل از پروژه لایک‌ریزی صفحه بزرگواران سوت و‌ کور بود.
©
SGhasseminejad
حدود دو هزار حساب Amplifierهای پست‌های قالیباف رو بررسی کردیم، که همه‌ی دیتا و لوکیشن‌ها رو اینجا منتشر می‌کنیم:
۱- بیشتر این حساب‌ها از کشورهای ایران، پاکستان، آلمان و یمن هستند.
۲- پنجاه و دو درصد این حساب‌ها بعد از هفت اکتبر ساخته شدند.
۳- سی و دو درصد این حساب‌ها رفتار بات گونه دارند و انسان پشت این حساب‌ها نیست.
👉
github.com/goldenowlosint/Islamic-Republic-Influence-Networks/blob/main/Data/Ghalibaf.json
©
sabber_dev
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2229" target="_blank">📅 18:13 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2228">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">قطع اینترنت، روشن‌ترین رفراندوم است. فقط حکومتی حاضر می‌شود میلیون‌ها نفر را با قطع اینترنت بی‌کار، هزاران کسب‌وکار را تعطیل و میلیاردها دلار خسارت به مردم بزند که یقین دارد طرفدارانش در اقلیت محض هستند.
قطع اینترنت ۹۰ میلیون مردم ایران، بزرگ‌ترین گروگان‌گیری تاریخ است.
©
SharifiZarchi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2228" target="_blank">📅 18:06 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2227">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d8g2tzQVAm1J3c6Q0vcOJEZJvWWQEiu-Zm30jdu1vq7w7hvcGCbmWUn4j4vp0HuMDwUjc0gJWHWetQEw0gRhnZv4gyhXCCwkYYL2QBUivuHuK4YAQltZ-rOAsx0ZGjIVjnsdzzMby73AJh0QhGxVRnAwa-OX5NaNQKSfQAuCO3O0RobbqrkW5mZilkeb8aHgdOXhDvWhbZopPmj6HEKSGkmM8U3FCtGob33aaV5Ai-puGtlJDWOhvmN5Cgg5hSHuUc9irL46XoDyg9FdlBQp-VUxNHKnkS9FcH3tkT810mDDzSK6uD-5vEM1XA1_lu58_K_mX1HP-t4M23jKO-aXcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز اطلاع‌رسانی فرماندهی انتظامی تهران بزرگ از پلمب ۳ واحد صنفی در شمال غرب تهران خبر داد. بر اساس این اطلاعیه، دلیل پلمب این سه واحد صنفی "استفاده غیرمجاز از تجهیزات اینترنت ماهواره‌ای" عنوان شده است.
©
dw_persian
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/ircfspace/2227" target="_blank">📅 18:05 · 06 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

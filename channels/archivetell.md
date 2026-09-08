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
<img src="https://cdn4.telesco.pe/file/dcUbWKMkVQHykVUoQ9iP4byhSZTMQXJWumjFnJMTeT6dUSHtuQQBbf1WoDEY6rDMeTHxqm5EL4_XCQlujv2C0CZi120JJEeoeXJYSzc93XXyw2-XLF2DfeAcE4iEeRTUcpaGdsazTwB6HuLGm7QeHj-RHJSpjyaKUgVaLP55eDdJGugR62wC_zDya2wmOZkxv3fXwPYWa7pUaBY18wvWMv9ckNYFs7kaBiUajf7uoWLy0U_OJmgHRJ3f5q__tHZBNpOx56y-u6gk6q-CW3JIgDLT9_MJSMnCMfJ9sW9DRp3HSo0xdp0ScWh-a7aE_0TZobVTktia7GsEM6roVIK-Kw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 08:58:33</div>
<hr>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbZLC7PFYfyfTk2Kg1XEZ8AXlz8Vm2DjXpoMvXjYMdGVkSWp6mgR0bcnJmm4ABypAWHA4q_wT81gc_d72pmwgZU8426ef2xg4f7_BfYo2LOWcpn4_S3PmuoakWQxwKbYqTzNFjrmJK7aobp2vrHMgtX9daPQ9MLOB-TDYcy1PKtbnuM2uyv2kIgk6NwosymxumZuNhA66MeXU3gs1fS5K1s33QmK2fCtQRk0si2U0XgwH-R8c-GbOy4Qeh5T5O0cW3P5jJHRySHRZ5QzfEyb3SMy76poFWc3GfAzGmN5_Lvkl7tSh-4L8CR2uOggJ8BLWvF6OKIcN_KJ-KRp9WUiWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت
یا کاملا رایگان باشه یا فریمیوم
با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم
اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 812 · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h9TSZyNRuNFWT0aB69Q86r5UzdNZq7obLp-jpo1yq0mxgpRdIopD10y5W8_P14nn6UdRhx2QjuePFih1MXhPzKhiMyH-lklUXwKZ2kn3MuWEnHC-AIcqt-5dTRDIDN09WrjnlUNrlZoOtapiMYBnvvXbnEZCMPcqmqtJqTU5NIIPVP0CExCKFI2I2gngCpNfnWx7WRryISPjLtMDq9S6uZJBA4B51DbwpNtdSflV5Jc1M6LWvrNNfsF2QFXMznsVEg3Lw0xOj6LoUm6xPJ9aNla8QmPfyy2rxTeFA8yHzVl9fCikl-XAreb5efDkiOtgVaoUpFgiKjcN6NJyJpZFqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yje1WbdNm9QTwjC1R7KZYP5LhRpEF-DOD-WsbSKk1tWjG7v3mncuLCKFM9sWynwEkhtqFg_mDysFSQVu3D_jsbs7Ld9533AFAl-AXVsl24iDzdYBEgGHNpYCWRF3xROqNo5_GrgShz1KvAe-lct-aBJRxhSCNsX2U90A6uAk5yP1VrmqjxGON3I0u8BzU9PPCyDJMF1QDAVsWGCsLJ14EJ4pq8WDnq3ZekieoJVKcW_QO4T9KimMJWs-O4JQO6_CR7o1KVF9yB4Kntoudxv3NFEvDqOfBzZaj95gk39RywtkoDtrcPJtuyFHO4-4mUB-LNDdwFqCSq4C-ZLdPfvjHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📌
مدل GPT-6 Astra بازم یه حرکت دیگه ثبت کرد؛
بازی Portal رو تو 23 ساعت و 43 دقیقه تموم کرد!
مدل به طور خودکار شخصیت رو کنترل می‌کرد به طوریکه هوش مصنوعی یه تصمیم می‌گرفت، بازی متوقف می‌شد. GPT-6 Astra با استفاده از تصاویر، موقعیت شخصیت و زاویه دید دوربین، تصمیم می‌گرفت که چه اقدامی انجام بده. بعضی وقتا هم تصمیم گیری هاش تا چند دقیقه هم طول می‌کشید، اما در هر صورت تونست بازی رو به پایان برسونه.
🔥
این کارو آقای "cozyblaze" با کمک اشتراک ۲۰۰ دلاری Codex Pro انجام داد.
🔗
سورس پروژه
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 977 · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLsf9iZPxtGCscBdZrrOuEMVAJU1O6oz3_DC4t8k7GQjKbiWITq8tB54Q70KixyYfaokChBa7sElwEfTD-hkSLTIEUnpjX3Iyq8tMlW_tXMteF6TfEpdD8yvWFt34kCKnep1fouVOov7CvyvHHY9XAzZ7u-K7qvC8hslX6ThYNqUVriCaKMJ6aPDUoXAZPqsEefYTuleIIUCGDxzAFXDlRio292j1a_2eq5Ob2UEY8umK8WhLqn4H4Zp8EPEQgwW0qZcd2gVrYr5dy9-ivby4v4Sy5R98jtzz37XHgnEfYypIcp_ygk0pJ6r9v5Srv12ApXewuRViNzSj2iCkdTP-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعبه‌ابزار همه‌کاره برای برنامه‌نویس‌ها با DevToys
💼
اگه خسته شدید از بس برای کارهای روزمره (مثل تبدیل JSON به YAML، تست RegEx یا دکود کردن JWT) مجبور شدید سایت‌های مختلف رو باز کنید،
DevToys
دقیقاً چاقوی سوئیسی شماست!
👍
🔧
بیش از ۳۰ ابزار کاربردی:
انواع کانورترها، انکودر/دکودرها (JWT، Base64، QR)، فرمترهای کد، هش‌ساز و فشرده‌ساز عکس.
📄
تشخیص هوشمند کلیپ‌بورد:
به محض کپی کردن متن، خودش می‌فهمه چیه و ابزار مناسبش رو پیشنهاد میده!
🛡
کاملاً آفلاین و امن:
تمام کارها روی سیستم خودتون انجام میشه و دیتای حساسی سمت سایت‌های ناشناس نمیره.
➕
پشتیبانی از اکستنشن:
میتونید ابزارهای دلخواهتون رو هم بهش اضافه کنید.
📌
لینک مخزن گیت‌هاب پروژه
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 951 · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=VjQdNg1jmmVDTvO-sVmY4rQKOS1p1vV4lIvfuZfR9GcFZiTzvUXUbZRpDbCQUjgREAa3KLWm3gEc7iUhOSYhJ9T3iqMtW4GJ7SlbYTVRqYNpaOKzLIysCVBz14q6X7rUhAdB-_ddw-q_CTY_srxK76yU8mykoghCkXafJLJfSbW3fIfYurNsOO4HkdGjvbYDEgiAJAD5JbrqkhGLzEBQi0d8xVipXsJGRruQwmTpugMmKKAc_R9uorV27w8rzYky3zNs477usUf2kRv38S4cCNSNxz1CevLUvip22xwi3fMOMJnIbP750WGbMLj-URxyyaZ7cOPGkIgabMcYYntsFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786d6d3a9a.mp4?token=VjQdNg1jmmVDTvO-sVmY4rQKOS1p1vV4lIvfuZfR9GcFZiTzvUXUbZRpDbCQUjgREAa3KLWm3gEc7iUhOSYhJ9T3iqMtW4GJ7SlbYTVRqYNpaOKzLIysCVBz14q6X7rUhAdB-_ddw-q_CTY_srxK76yU8mykoghCkXafJLJfSbW3fIfYurNsOO4HkdGjvbYDEgiAJAD5JbrqkhGLzEBQi0d8xVipXsJGRruQwmTpugMmKKAc_R9uorV27w8rzYky3zNs477usUf2kRv38S4cCNSNxz1CevLUvip22xwi3fMOMJnIbP750WGbMLj-URxyyaZ7cOPGkIgabMcYYntsFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم 7 برنده خوش شانسمون
🎉
:
1.
@reza1629
2.
@mhti9
3.
@KIING_ZOG
4.
@Gogogrugo
5.
ＮＯＢＯＤＹ
( 6641463426 )
6.
@an_Y008
7.
@AshenOne2077
برای دریافت جایزه به دایرکت مراجعه کنید
✅
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/ArchiveTell/7670" target="_blank">📅 20:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7669">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/ArchiveTell/7669" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7668">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🥇
رکوردشکنی دوباره از GPT 6 Astra
خبر رسیده که GPT-6 Astra تونسته تمام ۴۸ مرحله بازی «I'm Not A Robot» سایت
Neal.fun
رو بدون غلط رد کنه ، خیلیا جوری جو دادن که انگار آخرالزمان امنیت سایبری رسیده!
😂
طبق معمول، ته این هایپ‌های رسانه‌ای خبری نیست. کپچاهای تصویری سال‌هاست که عملاً مرخص هستن و حتی مدل‌های پارسال هم با یه پردازش تصویر ساده دورشون می‌زدن.
سیستم‌های امنیتی واقعی وب الان با تحلیل رفتار موس، کوکی‌ها و الگوی کلیک کار می‌کنن، نه با ۴ تا عکس چراغ راهنمایی و خط‌کشی خیابون
😁
تست کن ببین رباتی یا نه ؟!
🧐
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7668" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7667">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0RbxgJGdmq2VXJOpssmcTwcVoh4UG3rDMPEUrUdhy7l6E_l86jwLrmUhcuCC9X3Xgf-w-IWmAfCBQx7kLoriXDGN4Z-2gJjVHwZuX7kQKBazTY1nUsjj3Cg00cgQmsQam1sX6XxanJ-pJpB9_jn27W9XS8e668tm2Fqt608kAxaNNpR1GBgJTnJNoX27ZcyfisywmzPL5jvuHmke_xIn_U0p4FVjB-84v9OxYPwINQhSHBlTPerzTeWwguisFd-P1g6y_Y6KOaLNTY0Py0zAw-wckg8yRIUWEBt59q8-epncv5ObIpVzsu4Y5oICDvGJBrrlnzZd8L_lhjWOGYaSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جداسازی صدای خواننده از موزیک با هوش مصنوعی؛ تمیز و بدون دردسر!
🎤
🎧
بچه‌ها اگه دنبال ساختن نسخه کارائوکه هستید یا می‌خواید صدای خواننده رو برای ریمیکس بردارید، ابزار آنلاین
AI Vocal Remover
دقیقاً همون چیزیه که لازم دارید! با استفاده از مدل‌های صوتی AI، وکال و ساز رو در چند ثانیه مثل آب خوردن از هم سوا می‌کنه.
✅
🔺
پشتیبانی از انواع فرمت‌ها:
هم فایل صوتی (MP3، WAV، FLAC، M4A و...) و هم فایل‌های ویدیویی (MP4، WebM) رو به راحتی قبول می‌کنه.
🔺
بدون نیاز به ثبت‌نام و کاملاً رایگان:
پردازش تماماً در کلاود انجام میشه، قبل دانلود می‌تونید آنلاین پیش‌نمایش رو گوش بدید و تا یک ساعت خروجی MP3 یا WAV بگیرید.
🔺
کیفیت و دقت بالا:
تفکیک دقیق لایه‌های صدا بدون نویز و افت کیفیت محسوس سازها.
💡
نکته:
برای آهنگسازها، تدوین‌گرهای ویدیو و یوتیوبرها برای برداشتن کپی‌رایت یا ساخت بیت‌های بی‌کلام، این ابزار سریع‌ترین میانبر بدون نصب نرم‌افزارهای سنگینه!
🔗
آدرس ابزار
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7667" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7666">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvPTIelRZWh2oy1lZTrd6MIh1HoTjbGcYveqskFgly3PPZWv8CNOJlVuMziJURHF1Y7ouiyobIvNArQAkaXc5nOgm8GhYOUZrlgbJEFDc8i9eyj2TDDV2QDMWYAMz2oi0MYF4ea8AamaCdMSIxuy_jAp2_xvo8LX76Rq3r6PBheGIvMZ9egXSBxxo1X1eXlx_uc1O8qrLKIVhCL3iyUvZqn1gRmDsDKuPi2MBxMXq8yYtXZMqwUyhBh618YaIJ97yClOTOypCfgllO7FCzCwo7vyvAUA2lTq4Yy4-yj-xgvdS9eXC9wft-_hpEClwV0GdINm2rHqyWfwGHVWace0IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل گوشی اندرویدی به یک کامپیوتر دسکتاپ کامل با Android DEX!
🖥
📱
اگه از قابلیت محدود سامسونگ دکس خسته شدید یا گوشیتون اصلاً DeX نداره، این ابزار خوراکتونه! نرم‌افزار
Android DEX
با ترکیب جادویی ADB و موتور قدرتمند scrcpy، گوشی اندرویدی شما رو به یک سیستم‌عامل دسکتاپ واقعی با پنجره‌های شناور و کنترل کامل تبدیل می‌کنه.
🚀
🔺
تجربه دسکتاپ چندپنجره‌ای:
اجرای اپلیکیشن‌های اندروید در پنجره‌های تغییر سایزپذیر روی ویندوز، مک و لینوکس با اتصال باسیم یا بی‌سیم (Wi-Fi).
🔺
خوراک گیمرهای موبایل:
کی‌مپینگ حرفه‌ای کیبورد و ماوس، شبیه‌ساز جوی‌استیک WASD، قفل دید ۳۶۰ درجه شوتر (FPS Mouse Lock) و حتی شبیه‌سازی ژیروسکوپ!
🔺
دور زدن شناسایی امولاتور (No Ban):
چون بازی‌ها مستقیماً روی سخت‌افزار واقعی گوشی اجرا میشن، آنتی‌چیت بازی‌ها شما رو شبیه‌ساز تشخیص نمیده و بن نمی‌شید.
🔺
امکانات یکپارچه سیستم:
مدیریت اعلان‌ها، پخش صدا، انتقال فایل با درگ‌اند‌دراپ، رکورد صفحه و تعریف پروفایل‌های اختصاصی برای هر بازی.
💡
نحوه راه‌اندازی:
فقط کافیه گزینه USB Debugging (یا Wireless Debugging) رو توی Developer Options گوشیتون روشن کنید و برنامه رو اجرا کنید؛ بدون نیاز به روت!
🔗
گیت‌هاب پروژه
🔗
سایت پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/7666" target="_blank">📅 14:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7665">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vv48cb_ALYSoPYvYff4Jh01DtdQ7hZ66_vslV3Zsql4yQCiwlN_G8zmuM4Nk_UNRbomaiTr8pDWbJ-bNgvjvHvwQx74WDnG9R682SH_PrWEIC_BM8FnUaVWAcjuRQGs3dTv3EPt4VhlKpMFNubHKF1olddSVU_fgfl3cFX-KD9xnFDqzxP0J5X2w1w0fS_p-FQopNzlgTf1a_CU9-DbjTheBxfSTh_iOJm3y07HpqLAMMlsmardgkxrxkypOH1R8gP3EShVH6QIsHpuYCJz-J7YGvzLipIadByWUJ3UoclYPJvghpL1DpCD9-Q1W5tk5eI5CDcWVefnNxobNA_5WvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معدن مقالات و دیتای آکادمیک اروپا؛ گنجینه‌ای که کمتر کسی می‌شناسه!
🎓
بچه‌ها اگه دنبال مقاله‌های خاص، دیتاست‌های خفن یا پژوهش‌های پروژه‌های اروپایی هستید که جای دیگه پیدا نمیشن، پلتفرم
OpenAIRE Explore
دقیقاً خوراکتونه! یه پایگاه عظیم با بیش از ۱۳۰ میلیون دیتای علمی دسته‌بندی‌شده و رایگان.
✨
🆓
🔺
آرشیو عظیم ۱۳۰ میلیونی:
دسترسی مستقیم به مقالات اوپن‌اکسس، دیتاست‌ها و حتی سورس‌کدهای پژوهشی پروژه‌های اروپایی.
🔺
بدون لاگین و کاملاً رایگان:
بدون دردسر ثبت‌نام، پی‌وال یا محدودیت دانلود، مستقیم به منابع معتبر دسترسی دارید.
🔺
ردیابی شبکه‌ای پژوهش‌ها:
می‌تونید خروجی‌های مختلف یک پروژه (مثلاً مقاله + دیتای خام + کد نرم‌افزاری) رو به‌صورت متصل به هم پیدا کنید.
💡
نکته طلایی:
برای پژوهشگرها، متخصصان هوش مصنوعی که دنبال دیتاست‌های تمیز و رسمی اروپا هستن، یا کسایی که دارن روی مقالات بین‌رشته‌ای کار می‌کنن، این ابزار مثل یک میانبر تمام‌عیار عمل می‌کنه!
🔗
وب‌سایت رسمی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/ArchiveTell/7665" target="_blank">📅 14:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7664">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJ6GoA2cMWIqswuJj0_5bXr3XRPuUe_qOdu7c1Yi9K3MRMuXxXFZM9qygVtTgu8IieeoO_kbWaOeJmN0NEGupyMGNO74T9isj2lfY9OHYUCaHZ8i1YL5VycgwUBMI2RTdq_iX_Nn7s4zfBre7zsoYVoLqBl0jbCwuMvyl7rSCma4zwP20JM6SBfgDmcIXVRc2vVzdq6zNcFiymCU04CLQ4BISSR-zUVBiEeWWOhkyFpx3-rzzVJTsxV9LL6ua6rCaQwmpDpMsHAoolD9EHWjTkuSA_E20M1M-tJWaRGefm1hJDK3nnH0uuMGby6Z4Ls4XYNWMvv0EKqTQyyqGPk-Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیبورد «شریک جرم»؛ قبل از ارسال پیام حواست به جریمه و حَبسش باشه!
🚨
بچه‌ها براتون یه پروژه به شدت سمی و دارک آوردم! این کیبورد اندرویدی اسمش «Соучастник» (هم‌دست / شریک جرم) هست و کارش اینه که موقع تایپ، متنتون رو آنالیز می‌کنه و آنلاین بهتون می‌گه ممکنه بابت این پیام چقدر جریمه بشید یا چند سال برید آب‌خنک بخورید!
😁
🔺
کاملاً لوکال و آفلاین:
نیازی به اینترنت نداره و داده‌ها از گوشی خارج نمیشن؛ با llama.cpp مدل جمع‌وجور Qwen3.5-0.8B رو آفلاین روی گوشی اجرا می‌کنه.
🔺
سیستم دوسطحی سریع:
اول با یه دیکشنری سریع کلمات حساس رو بررسی می‌کنه و بعد مدل هوش مصنوعی جرم یا تخلف بودن متن رو می‌سنجه.
🔺
پروژه کاملاً اوپن‌سورس:
کد و نحوه کارکردش روی گیت‌هاب قرار گرفته و برای گیک‌هایی که می‌خوان اجرای مدل سبک LLM داخل اپلیکیشن‌های اندرویدی رو یاد بگیرن عالیه.
💡
نکته:
هرچند قوانینش بر اساس مواد قانونی روسیه تنظیم شده، ولی معماری استفاده از مدل‌های فوق‌سبک لوکال برای پردازش آنی متن موقع تایپ، ایده به شدت خفن و قابل شخصی‌سازیه!
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/ArchiveTell/7664" target="_blank">📅 14:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7662">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgbYqWEpGVeRlEGwmPleCnih6-v7VtIZcTyQSjo7gcNK_NhnmW1HAxClYDXdOAXy6lcoZPEGLLZ849phuWuehI7cZMvCW_3ETPMdnFz-UgrjVz_lCfHcnRBwyoYkUDUgG7XL68OcgMJVbj6NKFX5HNsVA8tEKA7_cKfecpzxaLG-WT1jfqAZG5o3bwwYJdfKeimIZq53soIqTwosXoAqXVK0ATuCM-ZlDjOtGASi3jVGHhcKiRmOh-SkuClIRMbiLwXrsVzRhRuag18wDyHuWNNATHcGm5CH2UIPMZ9ce22snkzFm9W0_ETceRz38HvD8JS4gjOhWP5gGwBRK17TAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طراحی و ساخت اپلیکیشن با M3E Canvas
🛠
📱
پلتفرم
M3E Canvas
یه پلتفرم اوپن‌سورس و جدیده که بهتون اجازه می‌ده با درگ‌اند‌دراپ و کمک هوش مصنوعی، برای اندروید و وب رابط کاربری بسازید.
🔺
طراحی سریع:
المان‌های آماده رو می‌چینید، رنگ و فونت رو شخصی‌سازی می‌کنید و همونجا تو مرورگر تست می‌گیرید.
🔺
تولید پرامپت جادویی:
جذاب‌ترین ویژگیش اینه که در نهایت از طراحی شما، یه پرامپت دقیق می‌سازه که می‌تونید مستقیم بدید به ابزارهایی مثل Claude Code یا Codex تا براتون تمیز و بی‌نقص کدنویسیش کنن!
📌
لینک دانلود / گیت‌هاب پروژه
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7659">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه
ArchiveTel
رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد
این ربات
رو استارت کنید
2️⃣
در چنل ربات جوین بشید
3️⃣
با آیپی خوب ترجیحا آمریکا وارد دکمه بشید تا سایت باز بشه و دکمه وریفای رو بزنید
‼️
نکته :
در هر گوشی فقط 1 بار میشه اگه میخواید با یک گوشی تعداد بیشتری بزنید باید هربار کلون های تلگرام رو نصب کنید  ، هر 5 رفرال برابر با 1 اکانت هست ، تمامی کریدیت های جمع شده تبدیل به اکانت میشه و قرعه کشی میشه و لینک فعال‌سازی به شما داده میشه
‼️
شرایط : حتما باید در چنل آرشیوتل عضو باشید
تاریخ برگزاری ، فردا دوشنبه ساعت 20
🚀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIAmkdmNS6wWi6mE-P0xD5l8JZ2KMibSkdnJwji0i4fInrjbpHanfc7ks8YQYPvLgjtjnTwpyEojZ45aC3pdIZaf8Odm4K_yTLwuC9N34swoYqD-oUR0QcNzMMDFwfgjIrWlPjMaUgMCJ_h7XfNID5tY55Z7ZXSjXpMSvRg2OiLjIcj2w4JGQ1d7fgZKDu8uiupLVDOQr6jmGEB_-qNoP8yt5GKshqU9GzLfKOmP-LY7k4sCvS0nrJS4C-4zxXn6ZmHZqvUiwGkltIPAz94rfC41bF9QKbk-eJDNSwhwNtSUaJmlGWYdv6O7xNBD82O99_rf23DW1kyrAmkJ3Xuuow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API هوش مصنوعی ها
💥
🆓
DeepSeek-V4-Flash-Vision-Exp | DeepSeek-V4-Flash-0731 | Qwen3.8-Flash-Next
✅
این سایت ثبت نامش کمی آزاردهنده هست بخاطر UI بدی که داره ، باید با گیتهاب لاگین کنید بعدش میره تو داشبورد و به ایمیلتون کد میفرسته و اون کد رو توی مراحل وریفای وارد کنید ( شماره تلفن لازم نیست ) حالا بگردید عقب و از سایت API دریافت کنید
✅
هر روز این سایت 1 PTS بهتون میده که معادل 10 دلار هست و خیلی زیاده برای این مدل ها
🚀
محدودیت هم هست 20 درخواست در دقیقه
‼️
📌
Base URL :
https://developer.amd.com.cn/radeon/api/v1
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL : https://api.b.ai/v1
📌
Model ID : deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید …</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfIr4GdDFzZonsk3V8whrROBu98wYQPwi-5CHuWgfYVhUXMFR8lRxVaXykEndb-MuuGy4SrXT4z6lJZHgdq2GkVOqfCO-FH6p5BQjj6oOYgZbMmA_YVUeQUOvYQL1lw7C_K50dNqlhHzJM6HnfbuQCWYIVmP8jMANZJauEYOGgvUr-66Fqk0pnsR1wban2ccnmUK9ULXtNz6TyhlobiwufmP_xG9wG7V2REp_RsSLvlXJCatYd2q2y96YHcsgZCL86eEGzyfoiIlX_SnIyDLl1SADK3Xq4U8Fj0GRB7bktc0xwTXmIyQGvpP2QwXrydW3F4obUraFE1qFVosl-jbnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به هوش منصوعی های محبوب
💥
🆓
Opus 5 | GLM 5.3 Flash | Deepseek V4 Flash | GLM 5.3 Flash
✅
4 میلیون توکن میده که میتونید استفاده کنید از API هر روز هم ۱ میلیون توکن میده برای opus 5 ( حد مصرف روزانه هر مدل ۱ میلیون توکن هست )
📌
Base URL :
https://helyxai.space/v1
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMY1NKyKVS6DGpFifVDi6QAS5VejKanas-Bt1wuKHny75n-XICBN4DWCwhoyz_jSGKzUEeOZE7FqnjiYtVvTCC5noJF8xG8zSDui_Ems-VUaFJ2le5_7uG5RxojrL62jznxwFNju4lWkNXh0TsM60fok2mApFDC4wBhgnlaXSx1rDrvYGLoQ3NaoT4iy0k8vaSXRi2_SU1ZvlcsnMRm7trslPK5knLLV2gePgzgSsftELlW0ZzIIbWKH4pVZt53J6NXP9RY3uE_xUAQteLrFbgGLy5Z2Zqj9b31_Rg8kakgAKXks1eQBIG23zQqlmG400W0VGBnUM3G2bVhMhudaxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏
اینم لیست مزایایی که داره:
‏• جمنای: ۱ سال رایگان
‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه
‏• جت‌برینز: ۵ سال استفاده از تمام ‌IDE⁩ها
‏• گیت‌هاب: پکیج کامل توسعه‌دهندگان
‏• آفیس ۳۶۵: نسخه کامل ورد، اکسل، پاورپوینت و تیمز
‏• فیگما: نسخه حرفه‌ای مادام‌العمر
‏• نوشن: اکانت پرمیوم مادام‌العمر
‏
برای دیدن آموزش کلیک کن
✅
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CI_ZJf0nX_YQ6Bi98gE95YLfRS_CmCj3gmDXNBfN3PamJJgepS6_y5oZLUQSSw4TZui0sMTGFskfETjjox7g4bz5WjZh-F452Cq61VIj4UZXPJn_5KEhPs7Qia572A_dBhRNH2z4be9LXshrR41Rdu2utu8TUIKPZzzt5PH6DphYNVF6fcFVGg89gUjQmCGWm6Gf4P_hcNZfH9gUdid8bfYx38NPvGr9n2nxsnPn7QkHuYnq_Gl4sKVdYewpuD4ww1Dctq867ktyYtzUFjPRg2n7t9oFqcppTZHE9SSfUZxnk1hOkB9iARCMjDXn0_reF-91IslI6COSliQruKb1XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
داستان GPT-6 چیه؟ انقلاب هوش مصنوعی یا فقط شوآف تبلیغاتی؟
🤔
این روزها همه جا پر شده از اخبار رکوردشکنی GPT-6 Astra و نمره عجیب ۹۹.۹٪ در بنچمارک ARC-AGI-3.
طبق بررسی‌هایی که کردم، این نتیجه تو شرایط کاملاً ایزوله و خاص ثبت شده و توسط منابع مستقل تایید نشده.
قیمت‌گذاریش هم به شدت نجومیه؛ هر یک میلیون توکن ورودی ۱۰ دلار، و خروجی ۵۰ دلارِ ناقابل
😁
(مقایسه کنین با جمینای ۳.۸ که ۳.۷۵ دلاره)
در ازای این هزینه سرسام‌آور، وقتی در کل حساب کنید، برتری خاصی نسبت به رقبای خودش مثل Fable 5 نداره.
یکی از معدود بنچمارک‌هایی که هنوز اشباع نشده و به نظرم بهترین معیار برای ارزیابی مدل‌هاست، بنچمارک Humanity's Last Exam عه
تو این تست، عسترا نمره ۵۷٪ رو ثبت کرده؛ در حالی که Fable 5 با قیمتی مشابه و حتی پایین تر، نمره‌ش نزدیک به ۵۸٪ عه
🔥
با دیدن همین آمار میشه گفت OpenAI با این Gimmick های تبلیغاتی، رسماً داره به شعور کاربراش توهین می‌کنه
😐
من حتی کاربرشم نیستم ولی باز به شعورم توهین شد
#طهلیل_ai
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4TGpd7Qxo0fx6hqgIrR6mEiQKC9UN-dNywOExLzPt4mssDj5bCMv7lnZjV5MaWJSvVD5p9Rm-dg7w2Q-iRsT8a7tSW4hFEs5l2gLSGeufNJS6MVod0s9su3jJUePqQO6zJyWAbpUxzsrC6RRA-IoFJ7cpAkCll7FslmD2QOImJmSlDaBzaUuM2LoeNvJbW8TtY88VSVHs9HNe8graadwYlrXgFT4xJJlbJQSecaI8B48Y0K-MCGkyKYNV5o8CZXHEwfZIOvMqZN50cm8A8X8jzZbJ3EYZzu3kDGatN0hhrJPkcSEkujlS_RMMGzZDzwKCwPqsHGnzqlDVheMWTL3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Free 2k$ model GPT
💵
📌
Base URL:
https://vip.9aws.net/v1
📌
API KEY: sk-g926rIr0SG7pfoD4WextkZwRRAgFOwYZDsG5hnDr8mL2ZH9d
📌
Models:
gpt-5.5
gpt-5.6-sol
gpt-6-astra
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuN-c9nv_FweZOttgsOfPTQEuQq0iH_ko3ZkMbnVvrCYMTIBtqdFKaVVvAsKW1M8WwJ6Zu8VOTPIX4rqL3r_xqSo67SQ01pWm1odQ2YlOs_z_5kIOXthv3_cylt07hagFJ6pd65vuJg9k_UcDRGTB0LkbWRzkRiURrsTJJ_BDxb8Xz_igHWaPfpEzX4mFVVWYCpIY7fX9ddBh5KBaK6492du3TXUFK9_9wWYNRILTy5q_Y3YRl2oeoUGa9roDyLXGPLHmSpcWEWoqsBtwbZbuNeWzCCKV6ftClpQZC1eAosY1NjUjpqQKc6IOMrity1YHRveCuXJ0G0CaNsE6dqp1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی آزمایشی رایگان به مدل‌های پیشرفته هوش مصنوعی
💥
🆓
Opus 5 | GPT 6 Astra
✅
سایت ClickUp فقط یک ابزار مدیریت پروژه نیست؛ ClickUp Brain حالا امکان استفاده از مدل‌های مختلف هوش مصنوعی را در محیط کاری ClickUp فراهم می‌کند. طبق مستندات رسمی، مدل‌های OpenAI، Claude و Gemini در Brain قابل انتخاب هستند و می‌توان بین مدل‌ها حتی در یک گفت‌وگو جابه‌جا شد.
🚀
🎁
سهمیه رایگان
در پلن Free Forever، نسخه آزمایشی Brain شامل ۲۵ استفاده برای هر Workspace تا ۱۰ نفر است. در Workspace های بیش از ۱۰ نفر، این مقدار ۵۰ استفاده است.
✨
⚠️
این سهمیه ریست نمی‌شود و پس از مصرف، برای استفاده گسترده‌تر باید پلن/افزونه پولی تهیه شود.
🤖
حالت Agent هم دارد؟ بله!
دارای دو نوع Agent است:
• Super Agents برای انجام کارهای چندمرحله‌ای، تحقیق، کار با اطلاعات
Workspace و اجرای workflow ها
• Autopilot Agents برای انجام خودکار اقدامات بر اساس trigger و شرایط مشخص
💡
علاوه بر چت معمولی، Brain می‌تواند روی فایل‌ها و اطلاعات Workspace کار کند، جست‌وجو و تحقیق انجام دهد و حتی Task، Doc، گزارش، اسلاید و موارد دیگر ایجاد کند.
🔗
لینک وب سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQ4JhCxNxOCdOfShuPbEglvbczLQkvTDN8Z0_ufxpkwM1auGYyBC92mzhl_RZn_kYV7eIqg5aFhCFvy8dfhHlLQBjuxC8csxFDcZH6SShmnM6tKktkJkYUtpzZv7EDzmf7PYU3p7iyfrv-XcSxfeTkP2AU8WmMukmhsezdNm-EO3kTFfLsEf7XNnGKV4RnB0X6gvNoOcZ6eDbh0MURrrHOoSB8v1IOLimdbkjIclMKwW3WEytDWjzNnzig21uNl5iYD0i416BhFzyLmkHoCuMMBJtk6iPBEUPcUVolNP8snwrnKZebbEu_IV37npvbC2PCXvaed_9QMN6qGDNXcwYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های هوش منصوعی
🚀
🆓
Opus 5 | Grok 4.6 | Deepseek V4 Flash
✅
برید تو سایت زیر ثبت نام کنید و موقع گرفتن api باید گروه Free رو انتخاب کنید از این گروه این سه مدل بالا رو تست کردم جواب دادن ، بقیه چیزای خوبش کار نکردن این مدل ها رایگان هستن و کریدیت نمی‌خوان
✅
📌
Base URL :
https://kiosapi.com/v1
اینم کلید خودمه اگه دوست داشتید میتونید تست کنید ریت لیمیتش رو نمیدونم
📌
Keys :
sk-ZoCd9hc91if9INutCoTC6zA0wJ2pbrd9a75GQJTyj5V4gIup
🔗
https://kiosapi.com
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvS2eRqNif9BQBP4iIk-YH5uuvS4opCfhnXcqqOWLurySaYpa-YRrHzZjm_-0tt04hd0fZwTcefq5dVVWlVjS2JnM4oelxy9QW2yxbMed10nbf6MV-a3E2N3j98-MEqL8lYP5OjEEytV2g_hPczniPvAqVBKQfTqmrcUHEGR3q4LgGn8VpjMXKDRMjI6y7oc4zWi323xOVm0F3_LG1nhpHF7klJLDl8sNydJXWV27I171SGIReqq0lt5lFGUofxyeaxqbmcuHx-fqNUvaEV9zG7i99Hvs6YoDS22dyT0-5LJks23z2S5-m9tHx1gbuS1XiynNu4cC3QnRX6gVB53-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5000
دلار
😎
📌
Base URL :
https://vip.9aws.net/v1
📌
Keys : sk-faNuu4uK9WqIYAiXjdmYxeX6PI1Z5wNLzCsIXKbKVQ67W1rG
📌
Model ID : claude-opus-5
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUn7z0emmwdd1w40xOnpqsg8CerzeyRFnGyAJXfg3ymC1NJ-DOC0SYjR5FmyeRClqSULHMvyIBjJxlog3gyTeFACixbg0GAyhP_BN7yp2IFSW4vUV161tGuuIWbLlB0rsQ2i9vSDNHbRqVdtwclOeN7MaLnUavDxC7_r6MfmPvnLK1e7LNZBV2SobFFeQl57-fWVldEJA-w44nzFcl-cJsYWO9HG2_1T8HYrYoxqzDempX-Bz99y597uE1-4Ds5SfxC5PJSl_0a-veH3r8XElmD6oBNEaK3ouC878VpONH7uSKIa5rlK8NfwYf3Ew-LRhlBwX6rvQcyGYIVk0dLc-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ساخت وبسایت ۱۰۰٪ رایگان، فقط با یک کلیک!
​سایت شخصی یا پورتفولیو می‌خوای اما حوصله خرید هاست و دردسر کانفیگ رو نداری؟ این پلتفرم اوپن‌سورس رو دقیقاً برای همین ساختم.
​
🔥
چرا ZeroWeb؟
​
💰
بدون هزینه هاست: کاملاً رایگان و مادام‌العمر روی سرورهای کلودفلر.
​
🤖
مدیریت با تلگرام: پیام‌های فرم تماس سایت مستقیم میاد تو تلگرامت و همونجا جواب میدی میاد تو سایت.
​
⚡️
نصب با یک کلیک: فقط روی deploy.bat دابل‌کلیک کن، تو ۱ دقیقه سایتت بالاست.
​کدها و آموزش کاملش رو تو گیت‌هاب گذاشتم. همین الان دانلود کن و سایتت رو بساز
👇
​
🔗
https://github.com/faithsaly5-stack/ZeroWeb
​
⭐️
خوشتون اومد استار بدین
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItfERMCg9Q-8M8wAlq1pksxYlH_0X1MYgw99zHrOeSyb5KrfvBLPw9Ty2wEhh6x2lu4XQo7Hk--t3XWdTkqmJwkg3-kqjCQwSLClxNT2z72efkHnORhUCso_AvDBKO3zcVfZvcCAXtMYzKXDT_0miPSbmzD1iGQ41TiANf1BeNu_d5_bKWrfORXAcH14eamEJAnrp7m7l3NYNeoxBPak6lCoCw_ObQ8spgNmBAa_ZrvbDbIV-mEfpNX7Ow8Y6Zw7FRSWvme9TRh9j4ShxruI5Q56-mlA4q-T1nZCcVlCI1P__9rhgeiYgzzrTUgdhWmzekxoRwssTtdUfKYPYn1Udw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM-5.3-Flash به صورت رایگان
💥
🆓
شرکت z.ai کمپین Global Build رو تو اپلیکیشن ZCode راه انداخته — از ۳ تا ۱۸ سپتامبر
🌎
⏰
دسترسی روزانه: ۱۰ ساعت ،  به وقت تهران: ۱۸:۳۰ تا ۰۴:۳۰
👑
کاربران Coding Plan: هر روز، تمام ۱۵ روز، رایگان و کامل
🥚
کاربران جدید…</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7645">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hE5QZ__FdPZS4w5jm4FEuuyyKSKLPHpTR-_aASsln15RRgBke6mpI_7LMmiVJ0GnkSoiXWjQJJNJrxVcXu42n5Sh9Q6qCZV6YbljnB4ox2U6iM8jVEZ-cQjgskz1zN17Y_aQnIP0tTq3pfcQ9rHjal3zhZQdP82q75D2d17RnXiS4U5IXySVAZMccGxCocM7kF-K2A-HMwn6ZKx1cl3Od-GUTZIhEjvtCbWvcj14s5wmw-iG-pQCmtYl-WZPDhpCti1kTIpQGXGHPCq_oOLZw8EdiBhJyD_x82er7f9l-jjTUK4YH148_TxlNtY6MkBQJQlOQ0p-7q5H8_wySIMgvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1,000 دلار
😎
💵
📌
Keys :
sk-ByTi6xCfB7Pt1N8Hp9z7VdsRwGIMM5pdnh4CsorUfflysvbq
📌
Base URL :
https://tabitoken.com/v1
📌
Model ID :
claude-opus-5
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHc5_PXOWTk1WFNAvm-rnYOe_mzTSG3XsDGEwqJZjYofMJkwz3PNnZUwm_iIVvPAqyoEr_Q8Pmt6G3scKiFsAw53asVbu-oPkLPo5aHfNTFLKUAD089YBZFDwq-EuSUO07IBksp7JufD0OmyKbSgSHS9yueTBSxYqGgAV4GjnxajIeJXHWqFmQFDruiNRYmbc9CHM1UEBsMQJuvY6VkGpzqt7Kay7LA8Q-BkY3V_e44KYPmjxj20YV7WuNlXTCQSEpGhl6U3ZlieGkjOQjNiJYwGF3md0yaomOCRdTC41Zsq3GZgSU40ohE79He2tUn_AvzkZRDrFQ6UIWsxy6_sUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqYwZudtAW0SsuWH3sCdWlcF968EG252ysN9RfRaUouc1KndcL4Mmng3MXQWb3ve5fKQ0lqAAuiCjy5bzjGfLjR4H7CHfidouKMIemC5y5MTP469WoHmkSmv3kQsWMVT4wygsAzDkHNRfmKMDuKvbezrV-gl5FZI_AW3yCemXJwzRVP9B0pWx1UdG2rdcDfXqkgw4XRW0fcIP9hXiJgU6jpMXdhl_2VlKS_tSFTbYW8EH2DuIXPBhy4Gag6hst8HjNbsEqJMQouRQBFdSKmZ4IE8QhgztL2tgasQTiTGsXzcaKjw4LaYYHFtjUQnDXAIJpMSp7dBpEfJQTGVxzYndQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت هم به دلایل نامعلومی میاد API مدل های Fable 5.1 و GPT 6 Astra رو میده ایشالا که خیره
📌
Base URL :
https://api.experientiallabs.ai/v1
ماهانه 5 دلار میده و همچنین فکرکنم Fable و Astra کلا رایگانه
تست کردم اوکی بود
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XA5Z2AWqbAv5SZjSPq3qLf0mipNaGonJ42RK4e2erw5tQ9UfM-LFGX2J65OZ6T5_D5Fyzia8-8MyxNfozvR_4Q_ftEiw_szh9Kb6s-U4Yc-pF-Ssx0D0KZh-EiihvYFef4XeRy3B--BGcCegY0qscb4BmDcE-KtWnJoJFgp0RMESYINdG9DztXV4HXecX9i6l4ipZbCYZnurFGvJtCBuTb5Z2SdWxPoepUCFChg20zdM66yB9QJRswDEhJc-s8pvcKu8U3CT8LnVkL9Jd7NrtdJz7n7xba-4ic_jJpgUJbSyG1PI43B2BPWVgG3WHiQOpgm4Zj_fLNpKwTLGse1SIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=dr22yErDY8VuQlwEnx5mz4FX3Juc0OPTDnleO5q1__y67JL3qmAE5L1-pzrAAZuo9hNPdQgti4i2Y6b8EQsKNddPmVdWxy7ZN6J40AyUB9chFH3NUrhx0AcaEWNVlzVtLDz8sB0n3owM3QiWpXL4UFB0W5XxtdlSnbrBgZ9LQDeXd2vBUZtpBN-dr6V5O59-gOxFBnu75V0RqhKUmIdH0qNcCU8VK1DL-Y3wA9dHfOOQFWcz5vjmyQDRy7gQg9-Fi-uanxLyx1muTJn_XwQE-3H68xsfI3hNhCE6gpzMQ1YuZ3uKuTz0ixguKwJ_URQmyC6jUHVk8jHyJm0GxJcRYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=dr22yErDY8VuQlwEnx5mz4FX3Juc0OPTDnleO5q1__y67JL3qmAE5L1-pzrAAZuo9hNPdQgti4i2Y6b8EQsKNddPmVdWxy7ZN6J40AyUB9chFH3NUrhx0AcaEWNVlzVtLDz8sB0n3owM3QiWpXL4UFB0W5XxtdlSnbrBgZ9LQDeXd2vBUZtpBN-dr6V5O59-gOxFBnu75V0RqhKUmIdH0qNcCU8VK1DL-Y3wA9dHfOOQFWcz5vjmyQDRy7gQg9-Fi-uanxLyx1muTJn_XwQE-3H68xsfI3hNhCE6gpzMQ1YuZ3uKuTz0ixguKwJ_URQmyC6jUHVk8jHyJm0GxJcRYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هوش مصنوعی حالا می‌تونه با YouTube کار کنه!
یک قابلیت جدید به نام youtube-skills به ایجنت‌های هوش مصنوعی اجازه می‌ده فراتر از باز کردن ساده‌ی ویدیوها، مستقیماً با محتوای YouTube کار کنن.
🤖
🚀
قابلیت‌های اصلی:
🔺
استخراج ترنسکریپت کامل ویدیو همراه با تایم‌کدهای دقیق
🔺
جست‌وجوی ویدیو بر اساس موضوع و پیمایش کانال‌ها
🔺
دسترسی به ویدیوهای جدید و محتوای پلی‌لیست‌ها
🔺
دانلود زیرنویس‌ها
🔺
پردازش گسترده‌ی محتوا؛ از جمع‌آوری ترنسکریپت‌های یک کانال یا پلی‌لیست گرفته تا تحلیل چندین ویدیو
🔺
امکان انجام تحقیقات عمیق با بررسی هم‌زمان چند ویدیو درباره یک موضوع
📊
یعنی ایجنت می‌تونه ویدیوهای مختلف رو جمع‌آوری کنه، متن اون‌ها رو استخراج کنه و برای تحقیق و تحلیل از محتوای YouTube استفاده کنه.
⚡️
مناسب برای ساخت AI Agent، تحقیق، جمع‌آوری اطلاعات و تحلیل خودکار محتوای YouTube.
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtwkKJorSTRza-Ulh9VbK9HWR8H1BrOxXSQnO-n8QwrkqKrG1w68e9iMdV_hTgVC8XkAv-jP-v_Skc_oBWKrTRAhTiqW-6bptv7yBwfn2BBZfP1jAdDXZHgyCs7Nyc5zW4aDRFah7pQp3NAtAU1uKWiJR-ka8Zkflaq8QBWISqqZTdkHGAbTbj7l6cziGEMtJZehsx27zeFP5yha7xbQr9WO08ob3hOIYpdpMZ8pJuZkpL1LGQODY_QK0rHGqqSI4XQgaV_DdmsNaobfWCL998AaDQFyKXhBFjjrLulDSvLfI2mCenCoIeQRgi8aRX3cIqz3TYi7_uUjW62ffT16JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">200 دلار برای دسترسی به مدل‌های هوش مصنوعی محبوب
💥
🆓
Kimi K3 | Deepseek V4 Pro | Deepseek V4 Flash | Sonnet 4.6 | Haiku 4.5 | GPT OSS 120B
✅
کافیه با جیمیل ثبت نام کنید و یک کلید API دریافت کنید تا 100 دلار دریافت کنید
✅
📌
Base URL :
https://api.you.com/v1
📌
Example Model ID :
kimi-k3
حالا برید بخش تکمیل پروفایل و یک ایمیل با دامنه ناشناخته وارد کنید
مثلا تمپ میل
سپس 100 دلار اضافه دریافت کنید
😎
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎯
چالشی بزرگ برای وایب کدر ها به همراه جایزه
اون لحظه‌ای که به یه دایره چرخان خیره شدی و منتظر جواب هوش مصنوعی موندی؟ Commons میگه این وضعیت روزانه
۳۰ میلیون ساعت
از وقت آدم‌ها رو می‌بلعه و حالا با پول جدی می‌خواد حلش کنه.
😎
💵
🎮
چالش چیه؟
به‌جای یه پروژه‌ی کلی «چیزی با AI بساز»، این‌بار هدف مشخصه: زمان انتظار برای پاسخ هوش مصنوعی رو به یه تجربه‌ی سرگرم‌کننده تبدیل کن. یه بازی کوچیک، یه تجسم تعاملی، یا هر ایده‌ی تازه‌ای که به ذهنت می‌رسه.
🚀
⚖️
داوری روی زیبایی کد نیست؛ روی کیفیت خود تجربه‌ی انتظار، اصالت ایده، ارتباطش با AI، قابلیت استفاده‌ی دوباره و کیفیت اجرا تمرکز داره.
💰
جوایز:
🥇
نفر اول → 20000$
🥈
نفر دوم → 8000$
🥉
نفر سوم → 4000$
🏅
رتبه‌های ۴ تا ۱۹ → هرکدوم 500$
🔐
+ 20000$ جدا برای بخش ویژه
📌
مراحل شرکت:
ثبت‌نام تو
commonsmade.com
← بخش Hackathons ← Join the hackathon ← ساخت پروژه تو بخش Code ← وقتی آماده شد Publish کن و تو Hackathons ارسالش کن
✅
🗓
مهلت: ۱۷ سپتامبر | کاملا رایگان
اگه مدت‌هاست دنبال بهونه‌ای برای یه پروژه‌ی وایب کدینگ بودی، این هم خلاصه‌ی مشخص داره، هم جای خالی تو نمونه‌کارت رو پر می‌کنه، هم یه جایزه‌ی جدیه
✨
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7635">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcxYDuFdYTf-K5bkHkDQnEYyYCx3ZN1RFLtsiNSkUoTxXBBUyCbgl2x-T9JO8SeCNjNPtPazz2XQhPlKZ0OeyXRaST00EP68a8OJ8NsgfZW7M-jfIGJ5Rx9XcbN95x1FHyP97p2dEzmsLqaFKaKV_0_gIOxODf4o95xDvv5xSe-KdPe0_peZU5w6e6O0dp2hNxv9RYMJcU5eNAa10THyZySLpK_BfRF4osa2GohySlXx15O7nIw0I5H6MsB26AJOHY7h7ALjaSym3D7Ml3aKEZUjORHRjh9jfhm2sBIZN2vm1jl27clmlga7juhjIISCwJEUVWiAkIMY4STM3wVTtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM-5.3-Flash به صورت رایگان
💥
🆓
شرکت
z.ai
کمپین Global Build رو تو اپلیکیشن ZCode راه انداخته — از ۳ تا ۱۸ سپتامبر
🌎
⏰
دسترسی روزانه:
۱۰ ساعت ،  به وقت تهران: ۱۸:۳۰ تا ۰۴:۳۰
👑
کاربران Coding Plan:
هر روز، تمام ۱۵ روز، رایگان و کامل
🥚
کاربران جدید عادی
: یک‌بار ۱۰۰ میلیون توکن رایگان موقع ثبت‌نام (تا پایان کمپین باید مصرف بشه ، با اکانت جدید ثبت نام کنید )
⚠️
توکن‌های رایگان فقط داخل خود اپ ZCode کار می‌کنن، نه از طریق API.
🔗
لینک سایت
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=V1KKDVn1lEkJO6dZYBi8pVdjJBqSVcY_4ZTtmrP0LpdnJIdJDvnt68AMyrFSwMR7JVWfHCatNw5CGaJId96OPfITYKnZKGx8uAs5TjhMQcqr2zPvoqwWe3AgTpbf-fStd0ec5pmlWmoU7Y5Hso_1Kb3roX0e9P_a9Qs28o6II7E3poimLQpIL8OX-lMifXCT6fy1I4tiqkImh2zcwjZZEq5S1jGh880fOm1OpSAedBoPuIhHi5ld-4DV94OAMMAkrVyh5L6dHiHFtEAa1FDfilwJizKqbS-lvylp4_RKIuUhnofhCSgknQG20txmRba7ati4rpgfGYCPy4QG8nydTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=V1KKDVn1lEkJO6dZYBi8pVdjJBqSVcY_4ZTtmrP0LpdnJIdJDvnt68AMyrFSwMR7JVWfHCatNw5CGaJId96OPfITYKnZKGx8uAs5TjhMQcqr2zPvoqwWe3AgTpbf-fStd0ec5pmlWmoU7Y5Hso_1Kb3roX0e9P_a9Qs28o6II7E3poimLQpIL8OX-lMifXCT6fy1I4tiqkImh2zcwjZZEq5S1jGh880fOm1OpSAedBoPuIhHi5ld-4DV94OAMMAkrVyh5L6dHiHFtEAa1FDfilwJizKqbS-lvylp4_RKIuUhnofhCSgknQG20txmRba7ati4rpgfGYCPy4QG8nydTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌍
Pythia — رادار زنده جهان برای هوش مصنوعی
ابزاری متن‌باز که وضعیت لحظه‌ای کل دنیا رو جمع می‌کنه و بهت میگه احتمالاً چه اتفاقی قراره بیفته
🛰
🔺
بیش از ۴۰ منبع خبری و اطلاعاتی رو هم‌زمان رصد می‌کنه (اخبار، درگیری، بلایای طبیعی، هشدار آب‌وهوا و...)
🔺
پیش‌بینی از فردا تا یک سال آینده
🔺
کاملاً رایگان، روی سیستم خودت اجرا میشه — بدون اینترنت، بدون سرویس ابری
🔗
لینک گیت‌هاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=SyvC1yesoU3Y2k9cxacVCOIgdjRU0CjZhSs-t0N6QeHLfkttUikHdvclf3f9dt07V6uJfLl_lfWIajxLCiiNH21ia-0Nz_5eov_E3-wxH6ETGGo9NffB9-COI2wJG-vXKRTiAz7uh274UL8iSzyQOXQ0RO-zXfAhUcTIPNnTJYZZAUTdlN9vZjyEVF2d95x-cZwvSOH5NF_rRyII6a72a01QJ46HjHn_1ZrGt_XTn1l7JW9vRHeF_E2CAsaiR6geX2zT7GmSo3Lrfjv6hEZdsIGMzIfK9BpAELXGu8gH_upCfTevuPULu4C2GqJ60Im1eF21duBZb7oomAjtpRPU9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=SyvC1yesoU3Y2k9cxacVCOIgdjRU0CjZhSs-t0N6QeHLfkttUikHdvclf3f9dt07V6uJfLl_lfWIajxLCiiNH21ia-0Nz_5eov_E3-wxH6ETGGo9NffB9-COI2wJG-vXKRTiAz7uh274UL8iSzyQOXQ0RO-zXfAhUcTIPNnTJYZZAUTdlN9vZjyEVF2d95x-cZwvSOH5NF_rRyII6a72a01QJ46HjHn_1ZrGt_XTn1l7JW9vRHeF_E2CAsaiR6geX2zT7GmSo3Lrfjv6hEZdsIGMzIfK9BpAELXGu8gH_upCfTevuPULu4C2GqJ60Im1eF21duBZb7oomAjtpRPU9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
شرکت Anthropic ابزار رسمی بررسی محتوای Claude رو منتشر کرده
راهی برای فهمیدن اینکه یه فایل با Claude ساخته یا ویرایش شده — مستقیم تو مرورگر، بدون آپلود
🔒
📎
دنبال یه نشونه امضاشده (C2PA Content Credential) می‌گرده که Claude موقع تولید عکس، ویدیو یا صدا داخلش می‌ذاره.
🖼
فرمت‌ها: عکس، ویدیو و صدا (تا ۱۰۰ مگابایت)
⚠️
محدودیت‌ها:
🔺
فقط نشونه Claude رو تشخیص میده، نه هوش‌مصنوعی‌های دیگه
🔺
نتیجه «پیدا نشد» یعنی نامشخص، نه «قطعاً انسانی» — این نشونه با ادیت یا اسکرین‌شات پاک میشه
🔺
هیچ اطلاعاتی درباره سازنده فایل نشون نمیده
🔗
لینک ابزار
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=HUbqcurK9-cSzzJVUxlXlIbdQl5JO1QUnW1zDRXmjyfLO-L7KRfD3SIW6Z_xgPbn2eMvUORH2qeczlNWXIg3VMRyTzZBgvTLahhMVsz32UlYt6Yj20sHqw2HsltxXLL_eWsTxzWFR8TUB5X01kwnU5PRzrttZvyz2Saueo5RVcWbkA3Ra8G4qK5dwp_5Uih6Rp9cHgTm3BXd3RRxi9ZXouqW3Mo0zGnNLn1DCeC9hN8Tr7ABp_RtSAdcOH2n2iNygmYclzlWoaqiW1KdVRaoCV_ahI0xQD-W_FncRRykiCgHu-LKTBPXCZP3aWmjDwDarFZ3hhUf-bUQnb2zjWpzeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=HUbqcurK9-cSzzJVUxlXlIbdQl5JO1QUnW1zDRXmjyfLO-L7KRfD3SIW6Z_xgPbn2eMvUORH2qeczlNWXIg3VMRyTzZBgvTLahhMVsz32UlYt6Yj20sHqw2HsltxXLL_eWsTxzWFR8TUB5X01kwnU5PRzrttZvyz2Saueo5RVcWbkA3Ra8G4qK5dwp_5Uih6Rp9cHgTm3BXd3RRxi9ZXouqW3Mo0zGnNLn1DCeC9hN8Tr7ABp_RtSAdcOH2n2iNygmYclzlWoaqiW1KdVRaoCV_ahI0xQD-W_FncRRykiCgHu-LKTBPXCZP3aWmjDwDarFZ3hhUf-bUQnb2zjWpzeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساخت رایگان ویدیو با مدل قدرتمند Seedance 2.5
🎬
🆓
خبر خوب برای علاقه‌مندان به هوش مصنوعی! سایت Dola مدل Seedance 2.5 رو به خودش اضافه کرده و حالا می‌تونید هر روز به‌صورت رایگان با این مدل ویدیوهای جذاب بسازید و لذت ببرید.
🍸
🎉
✨
ویژگی‌ها:
🔺
تولید ویدیو به صورت…</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7631">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mixJUaHgPLqeu8ZR6Vpx_T22Oly3_39kL2HujK3AHqq18lx0495tDb580QeEE8vZqJ1ikAMXM3CYpBcB_GjmC24RW_QhqIAQRjiKs9NFJJhVoT6o4xaJqSbcvru_cwaWkPeOJVKYw0Aibnj7qTpUvcQ7AsRHxw_xYzKOggl5RirUPxGCh2IUS1BHLZNFPoVDl3rVPvt0hICqgAnUyUkHbb_V_tt7NFWy682lL_DjIAtyZyPnRTf4--fG0Gbhb1c53tKWkro6g9PLqDxKvO2cVERMqD_g4rUDCZvocy-Qpn64QA6QInpXYy_nm0r2IkzEK_hKFsiG6h4mxQz6HWDQ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن API رایگان GLM-5.3 از طریق TokenRouter
💥
🆓
بدون کارت اعتباری، مستقیم قابل اتصال به اپ، چت‌بات، اسکریپت یا هر ابزار هوش مصنوعی دیگه‌ای
🤖
📌
راه‌اندازی:
1️⃣
ثبت‌نام یا ورود به حساب TokenRouter
2️⃣
ساخت API Key
3️⃣
تنظیم Base URL:
https://api.tokenrouter.com/v1
4️⃣
انتخاب مدل:
z-ai/glm-5.3-free
⚠️
نکته :
به دلیل رایگان بودن ، مدل کمی کند هست و باید در ساعات خلوت استفاده کنید ، محدودیت و ریت لیمیتی اعلام نشده ، این پیشنهاد به مدت محدود در دسترس هست
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=Mo_xncwS12hAONLiQ9lmrIYza21MN0DCs502SvlkcpfBUxkViSRX3Yy_PiMUe9fgpyzn_m066wHPq6DdTYWCqbjfhOJ3i_cUMzajPGBZcSrU4x7338w5qjpwdEVPboA2OutLuQvMkYxlHK2kUYiniIsBk_5PvRb_B-OhP3s5S4eKHn1t-x74CKmxJtUEI7CHY1j97VK0M-p0NGL6DsAE5fmGws0R0bTlP-LJqydTLBCqrvuMA3tPiYx4oeg0SC8q1BzlFi2rkJcRm4K0DsCTu2SkfzwLuFtvtaB45p3FBvAi5EhFVM_3jpwnjbqaF7_CnRznsvWBKxW0O64hc4eTvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=Mo_xncwS12hAONLiQ9lmrIYza21MN0DCs502SvlkcpfBUxkViSRX3Yy_PiMUe9fgpyzn_m066wHPq6DdTYWCqbjfhOJ3i_cUMzajPGBZcSrU4x7338w5qjpwdEVPboA2OutLuQvMkYxlHK2kUYiniIsBk_5PvRb_B-OhP3s5S4eKHn1t-x74CKmxJtUEI7CHY1j97VK0M-p0NGL6DsAE5fmGws0R0bTlP-LJqydTLBCqrvuMA3tPiYx4oeg0SC8q1BzlFi2rkJcRm4K0DsCTu2SkfzwLuFtvtaB45p3FBvAi5EhFVM_3jpwnjbqaF7_CnRznsvWBKxW0O64hc4eTvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثر های شگفت انگیزی که تا الان توسط GPT 6 Astra خلق شدن
🚀
✨
🔗
منبع اول
🔗
منبع دوم
🔗
منبع سوم
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7623" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7622">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3_rhSM-mOPzMGyhMKKulK1I_h8UsBpXPjnCyZS2bqeJPgz32Gu3ohuaYmmxZZpufLpw1i9NbOCtEsMU7Vp2JlYN3Wc_hYhPfqD1y_Yi2MC6-dcta_Di5IUFKwRGD_ZhBztjvkcAsARL7C-ILgVIZbE1-D2MFKCwv_B_h6krAKIFtUA5EisVgqr--p7isEPG6f-g0PhXEkGKGcJ2b7MluYeuoP8er5hyPZFj596A8MWAYMX7cmyyBA1Mgyq3BnOHN6yBpGAnyGobL5PFr9lLgMn_QfWB2Cw9toQ-5zGfpdzqzCB6GeraZq93evvcWMZ8nYOzfLhSpwOIJ8uracDAcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
کتابخانه پرامپت YouMind
بیش از ۳۰٬۰۰۰ پرامپت آماده برای هوش مصنوعی
100% رایگان و هر روز آپدیت می‌شه
⏱
📦
چی توش هست؟
🖼
پرامپت تصویر (+۳۲ هزار)
🎬
پرامپت ویدیو (+۹ هزار)
🌐
پرامپت طراحی صفحه وب
⚡️
بر اساس مدل‌های داغ:
GPT Image 2 · Nano Banana Pro · Seedance · Gemini · Grok Imagine
🗂
دسته‌بندی حرفه‌ای بر اساس سبک، کاربرد و موضوع (پرتره، انیمه، سینمایی، سفر، اکشن و...)
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7620">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2hOTTJd49xMV3pkc8xi4YthsPj8mozYW4Jb55LL51XgKNYiVLNBm7XtT78-hQG_482Vwd3nwBrz1Qv5DJjrLKdA8bnj-j95q1MWbsNcHkxFPEXDZUH290F5Nkb9zpYS62Q_mUS_A1QCvJLUEFR3p_72Gj5kbr0ooh8ClMDu8IZTaLAcwyG0kU8d6F8wDWWDc0Illd3XZXOu6Su_YI2rqmwhtUIDhhJAQLNeTVjoGbOQzf3NSHBNNI-UgpHZc_89AFV3JbBFDpMsIZUfM9_RJ77yroDyh1jJV3Z7qeLy1pO6b-J-TOEGuKFJkdNe0ulra6EGpw9HnEKPDbP165Y8lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5.1 2 days Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=claude-fable-5.1-high
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0imk3tCvl7TDVXjyT34j8XSsMd9lij0tEMYGEIWuNMSVTc5ATjTWyycrbLtnIY8-wwwpYkErAA7mhI-JGRpWVczre86nNcVw6xL1V27vvoNd6J5P8BO57GQxZsF4_qM5Yia_i7PVx0ilH_mNinayxIT6Ls3dE_9dERujT4-5JhdS6nKze7RGIg696PkG-su31Lb7iZIwADuHUhnp8z-Sf22C6sZqJ5GTnK9KVD6gRQiwiGAkJ_vtYdJW2HhN-UWQeGCaAUZ9g7tixi5M8yFZYl285chHxVoImIwxR5QkALO6De33ak7VgFKeNTJTOa0Vau3NLRXkQ2qcP40YbLpNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
خبر خوب برای برنامه‌نویس‌ها و علاقه‌مندان به AI!
مدل‌های قدرتمند GLM 5.3 Flash و DeepSeek V4 Flash الان به‌صورت کاملاً رایگان
🎁
داخل IDE چندعامله‌ی Verdent در دسترس هستن — بدون نیاز به کلید API جداگانه یا اشتراک مدل!
❌
🛠
روش استفاده:
1️⃣
برو به سایت
Verdent.ai
2️⃣
نسخه IDE رو دانلود کن
3️⃣
وارد شو و از GLM 5.3 Flash یا DeepSeek V4 Flash به رایگان استفاده کن
⚠️
نکته مهم:
این دسترسی رایگان دائمی نیست! محدودیت مصرف ۵ ساعته و هفتگی داره پس قبل از شروع یه پروژه‌ی طولانی، حتماً سقف باقی‌مونده رو چک کن
📊
⏳
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7614" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7613">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcYKwZ9Nl5ZFZuE4VXmTPb0C4vzjwoVxrt6IQ9fbAnAeaioZlZTBe-u0JVKEYyrrfPk8vql2iho1bO1J9WS-08RBiIFoZCCEfRtP9rWMWXCxJVawX4HOBQt25SyOcmdFk_BbJ8yaQ_AKGEqPN_O3BdIzar-WzmbvF_Qo_d2NBL26-qxepj4VtA2e7RJw-jnMpdTNUwpZlyqfWNQS2HSe20Z0OMOx_7Jm_odDm4377Jo3yPpZWZNVyv6j162MqhFMCeBzFcZH8-2aOwpKxa51UJXbVocAy3PF_Z7SpCvesF6xfFNZpMIIXLLhK_t2ryKIUIVjlajfWVeo3JRx92Wl7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه
سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت، Prisma، Supabase، و اتوماسیون‌های ClawHub (اسلک، دیسکورد، نوشن)
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7611">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">10000 دلار کریدیت رایگان Fable 5.1
💥
🆓
🔺
Base URL: https://syntro.up.railway.app/v1
🔺
Model ID: claude-fable-5.1
🔺
API Key: sk-pHXhquluKg5xOejYuGxaFkrZbgArNB7kX9HtvekqCwA64pWc
✈️
@ArchiveTell | #API</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7611" target="_blank">📅 14:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7610">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kT0TYXUh3a2EyFyMbvNdk5dAGtkDHPlceAsX753j_1SVf9I1a-OKwdLEreHAKPXNK-oZeZv_xhLcRcB1LNUR86VBLNg35ops0K7in7yBDN1ccGv_y7-QYA7xLuOgsc7-Wa61EYqrqfCwNIuA0baGyDLYXJfG6FAJngzu0RevM4te590tcHa41HZkO3NvdwHPKrKJ7YDyHtJBISQ1cyonADvCHvbk8yPqqW3LwQFIzJCQFlrWxPKuX3yJCcRCt3Yr5uYiFQJC9gXY7sedUunPdSU1qHxMkE1a37M22e963DQpDRqAvWK-sBG9n-f6LhDcBtGgXlOyYMziLxlsDqw97w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10000 دلار کریدیت رایگان Fable 5.1
💥
🆓
🔺
Base URL:
https://syntro.up.railway.app/v1
🔺
Model ID:
claude-fable-5.1
🔺
API Key:
sk-pHXhquluKg5xOejYuGxaFkrZbgArNB7kX9HtvekqCwA64pWc
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7609">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">Free Deepseek 2.5 Billion Tokens
🌊
Base URL:
api.pkay.fun/v1
Endpoint:
https://api.pkay.fun/v1/chat/completions
Key: pkay_f38d9bbbfdaea88a190f415eb007ef2ffb74bed33961c366
Model: deepseek-v4-flash
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQxjtQrlxndCh3nTBMr0lus9-I542auh2ko79bVWr9iHRYSl7tIlSpEblNmjAmfphKyTfhBtZrU-UIVk5R_ICBPYqywPY7hC7KIRuPr-20v2CYdo5o_egwg-4lQjqJeqjuguH1e_oCoKiuFrMRtA4cTzqua2STLgjDgxZDfCmU_dc1b2ZRjJCnqaOl_6mXZ0TaqgBwqzdLFtcCGEqtD2642iCWfVC4AWkSVepbJhNVKtsXVSdB90nlTnfUuPhBLWhib_kubCdahLMtP8hcDAVPnhF6u8z3QLX7AHr3u02wMCuBKZbss2lngiPf_4zcNQnR7htayw33YA3R-b0Y34gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل Gemini 3.8 Flash در برخی موارد از Opus 5 پیشی گرفت - با قیمت 0.75 دلار برای هر میلیون توکن
شرکت گوگل، سومین مدل Flash را در عرض شش هفته منتشر کرد. Gemini 3.8 Flash برای برنامه‌نویسی، کار با ابزارها و سیستم‌های عامل مستقل طراحی شده است.
بر اساس تست‌های گوگل، نتایج به این صورت است:
⚡️
Terminal-bench 2.1: 89.4%
در مقابل 89.1% برای Opus 5
⚡️
Finance Agent v2: 61.4%
در مقابل 58.6% برای Opus 5 و 53.8% برای GPT‑5.6 Sol
⚡️
HLE-Verified: 54.9%
در مقابل 54.4% برای Opus 5
⚡️
پردازش ویدیوهای طولانی: 87.8%
در مقابل 75.4% برای Opus 5
اما این مدل در همه زمینه‌ها از مدل‌های پیشرو پیشی نگرفته است:
⚡️
DeepSWE v1.1: 71%
در مقابل 74% برای Opus 5
⚡️
Terminal-bench 4.0: 19.1%
در مقابل 51.8%
⚡️
OSWorld 2.0: 59%
در مقابل 75.4%
به عبارت دیگر، این مدل "جایگزین Opus" نیست، بلکه یک مدل سریع و ارزان است که در برخی وظایف به مدل‌های پیشرو نزدیک شده است، اما در کارهای پیچیده و تست‌های جامع سیستم عامل، عملکرد ضعیف‌تری دارد.
قیمت این مدل تا پایان سال 2026 ثابت باقی می‌ماند: 0.75 دلار برای هر میلیون توکن ورودی و 3.75 دلار برای هر میلیون توکن خروجی. پس از آن، قیمت دو برابر خواهد شد.
همزمان، گوگل مدل Gemini 3.8 Flash Cyber را برای جستجو و رفع آسیب‌پذیری‌ها معرفی کرد. این مدل در CWE-Bench امتیاز 47.2% را کسب کرد، در حالی که مدل پیشرو امتیاز 47.8% را کسب کرده است. دسترسی عمومی به این مدل وجود ندارد: نسخه Cyber فقط به متخصصان امنیت تأیید شده از طریق برنامه Fairwind ارائه می‌شود.
در حال حاضر، این نتایج توسط خود گوگل ارائه شده است. هنوز هیچ تست مستقل از این مدل جدید انجام نشده است.
⚡️
جزئیات بیشتر:
Google
⚡️
بنچمارکش داخل سایت
https://artificialanalysis.ai/models
اومده
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7604">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGTQaDocUydQpHNseilhUv2I98jWc98IlOrpBzdXv-UEz2JEDwMufybVfvMX6jUDsM431G65i4Dp-aUANLoPpAWxVS2Q5IEVbXQuDGOqkVwqYLVS4EVJaXbhuqnJg48KknAhTA81XvFxdoe2FiC_dsD_AjYHCODMsvbDX7HSS-q5d09hyBEIW_YdmEqCXn1-1FFnywiHxZz807YzPw0RDp77rnW9DQ_uWYsqStBzKOQ5TYor8gJW-fxj5iCGwgn7a2_H5lhSFZGFC0lGDrDCDih51UrBanAQTSqVIYB3Lt6gQ36hzF0-4yokvR3RCQBnq80hthVGmq5v1XO2QpKY3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5hkfa8MPK9yiDVWkqGo6e_ffE027zOZAxIibuKbb4LfjgaTt12oaresL4vmvtAypiXjMTzewMirvGypUd6AMjoctSI6gNEKZ7NCK5bWzecY09tD41j-f7EUUIeRUv5L-KIl_tj-DUpynlyo_u3lj0EeybVLc7NCsDxwaimM09nR1JQIoe3-EV3aVJnzVCK1Jz_D9ubs8AnxD6lO9y1bpYOFBP2fuqu8PbmAR65DBocENP__eQdMhB7dYLniNGHUu5f2411HzrqJr4qulIUsOsWc8ZmjwssGjHJQ2NGiHaF1z7DLUpf5NK1J1UzKdl4tkh7btjHEUWRJTNsIe4QkvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNof-0PtLF3_dYg7tW-z7znCq6RUUyc7vUWvqlwffzqNq8qY7oJLsy5zKeGPN4Udm6uZWAY-S24pPx2fjk_wbp8S7kqng9-O2PNvKrZ6O7BRVUV_B0LZY5JFEQVrYhvRFkHy80LsdTgW3DMiCOT9xHwvwgYjQZML0w8KxGLIZ1GtCQScy0lzuiM05Z2Y3imQnCApRAWD5EZIeqG9USSlncvkAiqjzeBeFszoRZ9Nd5L6epQXN-5gKHkFpOBwfLqtNhXzq0jpxkoYjoTHzkDkJ0aWTZ0pILMqojjVzAz5AmMlLX3SXVF3F-XmCdbFzl1F2SIW-33Iamf_ycJylJK_9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ریپوی ArasClient پابلیک شد!
بالاخره سورس کامل کلاینت روی گیت‌هاب عمومی شد
✅
🔗
گیت‌هاب:
github.com/ArasTey/ArasClient
📥
دانلود مستقیم:
github.com/ArasTey/ArasClient/releases
فایل arm64-v8a برای اکثر گوشی‌ها
✅
فایل universal برای بقیه دستگاه‌ها
⭐️
اگه خوشتون اومد یه Star یادتون نره — برای ادامه مسیر خیلی انگیزه میده
❤️
━━━━━━━━━━━━━━━
چرا ArasClient؟
چون کار چند تا اپ رو یکجا می‌کنه:
⚡️
اسمارت کانکت
یه دکمه: همه سرورها همزمان پینگ می‌گیرن و سریع‌ترین وصل می‌شه
🔃
سورت سراسری
بعد از هر تست، سریع‌ترین کانفیگ از هر سابی بالای لیست قرار می‌گیره
🔓
فرمت اختصاصی .arasc
ک
انفیگ‌هات رو تو یه فایل رمزنگاری‌شده امن ذخیره و به اشتراک بذار
حالت Protected: طرف فقط می‌تونه وصل شه و پینگ بگیره — نه آدرس، نه URI، نه اشتراک‌گذاری مجدد
📊
اطلاعات ساب
حجم مصرفی، حجم کل و زمان باقی‌مونده ساب مستقیم از لینک ساب خونده می‌شه و بالای کانفیگ‌ها نمایش داده می‌شه
📣
اعلانات ساب
پیام‌های سازنده ساب خودکار نمایش داده می‌شه
🏳️
پرچم کشور
کنار هر کانفیگ پرچم کشور سرورش (از روی IP واقعی سرور تشخیص داده می‌شه)
📊
آمار اتصال
تایم اتصال، آپلود و دانلود لحظه‌ای + آمار کلی در تنظیمات
🛡️
همه پروتکل‌ها
VLESS • VMess • Trojan • Shadowsocks • Hysteria2 • WireGuard و…
💎
پر-اپ پروکسی، روتینگ کامل، بکاپ و رستور، تم روشن و تاریک
━━━━━━━━━━━━━━━
🔒
ویژگی‌ای که هیچ کلاینتی نداره:
کانفیگ‌هات رو با پسورد به دوستات بده — اونا فقط می‌تونن وصل شن و پینگ بگیرن. نه می‌تونن آدرس سرور رو ببینن، نه کپی کنن، نه برای کسی بفرستن. مخصوص فروشنده‌ها و ادمین‌ها
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvROliqY8A9qDG5KRKyz0yaBxyAwerGNJZsjUtDHK-62hbw6aCH4BuPEjI36v-rpjRLBKZpOzpu92KTrDaBu8tBWf_axh1nW10PRaOJaRnfAFUNRLJcgri6hR499YQwGhcMXfq0XnsH6RdWvXY5OPw56W4vT59h0VmtFjiGEyyIONvxakD-R8IbSKRim3ZVL4CvxxXSJ_nxcWQWUA-ebHau_bUU3F5TDDMGBAr9GmKjPhdpVKMJqLCufrUXMINuOfbzNaandIIasJ_Cf_i7Yjzoho86Lw61cA58QCiO9tV-GeYCOxO2bBcH1lNOe7ouXJp-H207UkerPVTedu6hsYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧑‍🎓
✨
OpenMAIC — کلاس درس تعاملی با هوش مصنوعی
هوش مصنوعی داره تبدیل به یه دانشگاه آنلاین کامل میشه!
OpenMAIC
یه پلتفرم متن‌باز برای ساخت دوره‌های آموزشی تعاملیه — شبیه NotebookLM، ولی با کلاس درس مجازی واقعی
📚
📤
چیکار کن؟
یه موضوع، فایل PDF، اسلاید، صوت یا ویدیو آپلود کن، سیستم خودکار می‌سازه:
✍️
ساختار منطقی دوره + اسلایدهای آماده
🔤
آزمون، تمرین و سیستم تصحیح خودکار
🔬
شبیه‌سازی، مینی‌گیم و مدل‌های سه‌بعدی
👨‍🏫
معلم‌ها و همکلاسی‌های هوش مصنوعی برای بحث گروهی
🎙
سخنرانی صداگذاری‌شده + تخته‌ی هوشمند با نمودار تعاملی
📦
خروجی:
فایل
.pptx
یا
.html
قابل ویرایش
🔌
سازگار با:
ChatGPT، Claude، Gemini، DeepSeek و مدل‌های محلی (لوکال) هم پشتیبانی میشه
⭐️
۲۰.۷ هزار ستاره روی گیت‌هاب
— پروژه‌ی فعال و پرطرفدار
🔗
لینک سایت
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMeev1_wC-9NXkZ9NAPRTGInkzsNVLiTMghUpd-p8SkQAD6E_Ea92l7A06_YF2pmqwqwGdCeOLtiS687RQG-G21L2D37VwLwwo2PsAzVszWPh3cYAU87unmXSIG1_OfgoqJzQaX6-9z0o55kuk_8azqGBFiH4FuPlFXqFxl5qpXmswpox0zrnppF2di6vPmQnxOelORzJgFS-KlFzElgSFEOQCdCZqFD-h3Vst8QPLU00pJjDv3u_t8t5T3LC0QnZcNrYjtziRzTgJWw4Uk6VfQSu0mmQIVJeHIHgOeRLyjxQvPaILXqFKUtP9OyF8d61ZVhcPDoUXnP3gGrB8ezwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
✨
۵ ویدیوی رایگان روزانه با MiniMax H3 Max — بدون ثبت‌نام!
با این سایت میتونی این مدل ساخت ویدیو رو به صورت رایگان امتحان کنید
🔥
✨
ویژگی های کلیدی :
🔺
روزی ۵ بار تولید ویدیو، کاملاً رایگان
🔺
هر کلیپ ۵ ثانیه، کیفیت 768p
🔺
صدای طبیعی همزمان‌شده
🔺
متن و عکس به ویدیو
🔺
فریم اول و آخر بده، مدل حرکت وسطش رو بسازه
🔺
نسبت تصویر: 16:9 | 9:16 | 1:1 و...
بدون نیاز به اکانت برای ۵ تای رایگان روزانه — با لاگین هم ۵ تای دیگه اضافه می‌گیری (تا ۱۵ ثانیه‌ای)
💡
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u38UwwxOL2ns6GM2FKIZGIUYYI5FiYdvqRAqbmszAAsBb4gkyJi2qkputWjc231pRGoaMdpVSugd6Eqf2ia_lAmN9W1ZNCG_MMLuGB7J1ky2x9OZAeN5XmrJpdKjuh96fm1mRoCY5lgW58X_3Rgd1RMIkKlCKXUaGL9W84QPXoruTC8dvELQNTYPLBo5htrOpqm91WlNjxm2lcAtx523g5lmjh6g_P3zWobiCDNpsGM9SOupKN34VQjiURAPVAfa2qL0r4I0yihAKkSFdyxdzM5w-iksDY9gXt-wJyIElPhd-gWHGnZpB7EV7LCv0B4foKC0vKD8FPsV08e2llQEdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔧
✨
دانلود کامل گفتگوهای Claude با یک کلیک!
معرفی
Discussion Downloader
— یک اکستنشن ساده و سبک برای Chrome که گفتگوهاتو با
claude.ai
به فرمت
Markdown
ذخیره می‌کنه
📝
📥
چیکار می‌کنه؟
کل گفتگو رو استخراج می‌کنه — همراه با:
👤
مشخص بودن نویسنده هر پیام
🖥
بلوک‌های کد سالم و دست‌نخورده
✍️
لیست‌ها و جدول‌ها با فرمت درست
🏷
هدر YAML با متادیتا (عنوان، لینک، مدل، تاریخ)
⚙️
چطور کار می‌کنه؟
برخلاف روش‌های معمولی، داده‌ها رو مستقیم از API داخلی
claude.ai
می‌گیره، نه از روی صفحه! چون توی گفتگوهای طولانی پیام‌های قدیمی از DOM حذف میشن و روش‌های عادی نتیجه‌ی ناقص میدن
🎯
🔒
حریم خصوصی در اولویت:
✅
فقط دسترسی
activeTab
و
scripting
✅
بدون آنالیتیکس، بدون تله‌متری
✅
هیچ داده‌ای از مرورگرت خارج نمیشه
✅
رایگان و اوپن سورس
⚠️
محدودیت‌ها:
🔺
فقط شاخه‌ی فعال گفتگو صادر میشه
🔺
آرتیفکت‌ها و بخش thinking صادر نمیشن
🔺
رابط کاربری فقط روسیه
🔺
نصب دستی (unpacked) — توی Chrome Web Store نیست
🔗
لینک مخزن در گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgQ_bGRO1eazAiKYNU-YoVTfkzo4yXjxqTb2UIopS50oZtMUxlkLToxeYBcGO5kMtzmk35JqBAZRdZU-anSucpmBZK3z6ncNMAdTfoFfNJWmIkGji7IzFgyLNVFPoFRhdhpjhQkNKxUWV8SjBkPH0IrcFxneLTcJ2WLWXdgOvuBqooxq5mX2g9eL8UzshO2b1tGVcD99_5EKKzQ4gOiQKuopddfVxl6FJOGqJpUBeGEovvQdM3_pqQGrTJUznqnMQDbN03Hy5MXYL5T5tutq6vUOrn4q9qboawFG9lYuQEhOy-1R7UCLFbYgLgwq_NUFwV4UMsXc-T24crRJjbQiTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦆
✨
حریم خصوصیتو با هوش مصنوعی معامله نکن!
با
Duck.ai
بدون ثبت‌نام، بدون اکانت، بدون هیچ دردسری به قدرتمندترین ابزارهای هوش مصنوعی دسترسی داری
💥
🆓
💬
چت و وب‌سرچ با GPT 5.6 Luna
🎨
ساخت عکس با GPT Image 2
🔊
ویس چت با هوش مصنوعی
سؤال بپرس، جستجو کن، تحقیق کن، عکس بساز —  همه‌چیز رایگان و خصوصی، بدون اینکه ردی از هویتت جایی بمونه
🥸
🔒
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DADGpQVcc4BbOYRo8ScESZOjqopWpWp2hCYPCMvvY692jn1zOWfrYeNmxsShJPL-3Dv1l-R2QdhzfXP9PS4Oioz_psZgjCHlGH-KZ6FpqTZ0X5BmGqgf3ZAbL51j2o1zb_Y2Gv4i6Dp1uP-nBg2oJz4FDHjtkyIrLbQgfVnQsfw1W1TkoIlxn6VRNiU-kSYEZZOzbU7oxBKXB52UE57k8LHxNE2ozw4sNHgGeZBKIkasOyr80J8hFIh0xyTOtu6MM9OJZw6hv0BwmfthMO2Cwq8QBjPD5eonr3W6b0LQj_o02Jsy4bAd5vaTyTyo3jsXdod8WaxzVs6lGBXmWjoD3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Hy4 Preview: رقیب جدید GLM-5.3 و Kimi K3
شرکت تنسنت، مدل جدیدی از خانواده Hy را منتشر کرده است که قبلاً با نام Hunyuan شناخته می‌شد. این بار، برخلاف روال قبلی، مدل به صورت عمومی منتشر شده است، وزن‌های آن در دسترس قرار گرفته و به سرویس‌های محبوب اضافه شده است.
اطلاعات کلیدی:
🟢
770 میلیارد پارامتر، با 49 میلیارد پارامتر فعال به صورت همزمان
🟢
ظرفیت پردازش متن: 1 میلیون توکن
🟢
حداکثر طول پاسخ: 64 هزار توکن
تمرکز اصلی این مدل بر روی وظایف پیچیده و طولانی است: کار با کدهای بزرگ، تحلیل چندین سند، نمونه‌سازی بازی‌ها و تحقیقات علمی و غیره.
در یک آزمایش کور، شرکت تنسنت 203 وظیفه مهندسی را به 163 متخصص ارائه داد. نتایج به این صورت بود:
1. Hy4 Preview – 2.99 ( از 4 )
2. Kimi K3 – 2.94
3. GLM-5.3 – 2.92
این مدل در تست‌های منتشر شده نشان می‌دهد یکی از قوی‌ترین مدل‌های متن‌باز موجود است.
نکته جالب دیگر این است که این مدل به طور جزئی در فرآیند توسعه خود نیز نقش داشته است. این مدل نقاط ضعف در عملکرد خود را شناسایی کرده، پیشنهادهای بهینه‌سازی ارائه داده، آزمایش‌ها را انجام داده و به افزایش 31.8 درصدی سرعت پردازش کمک کرده است.
نحوه تست:
>
WorkBuddy
– به صورت رایگان در دو هفته اول پس از انتشار
>
CodeBuddy
– دوره رایگان دو هفته‌ای، با تمرکز بیشتر بر روی کد
>
OpenCode Go
– مدل به اشتراک اضافه شده است
>
Hugging Face
و
GitHub
– وزن‌های مدل برای اجرای محلی در دسترس هستند
برخی مشکلات شناخته شده وجود دارد: مدل گاهی اوقات بیش از حد طول می‌کشد و نتایج نهایی را دوباره بررسی می‌کند. به همین دلیل، این مدل در حال حاضر یک نسخه آزمایشی است و نه نسخه نهایی Hy4.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKk-IdXuyFwwdgTZDFNxCDNMg1QUJkgCJciSNSVvgaGb82wzVCarVU4RROpiuspyTYUz7bFK2cjjNSk4JJgIgYio6_2vPpO7gK-RSkoTSGFSDWwyxvowTtjrqlMMbLzb_OX8RPJbJFG5AT4LujEcaJAnlMQuoRpYj6LAKfuHePXvooR4kZxSpnqYL4u0VFO27fP9JMnUybcHGsuvGCnOdUXx2ZxfcSM9UBemduVrUCTNSwYeKGY9TkSK_EYUN-wulWsp8VpuCNUMNWRrMRWyFEMldpYPcE7AKKPCbSOx3Bgu_rolEhA6aQj1SjyiBmm8YfCJ4H_-wjQj3f1H_uovwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تبدیل PDFهای قطور فارسی به متن تمیز برای هوش مصنوعی!
نرم‌افزار ویندوزی و رایگان
PDF2MD Studio
. با این ابزار، PDFهای ۱۰۰۰ صفحه‌ای رو به متن استاندارد مارک‌داون تبدیل کنید.
فقط در ۳ قدم ساده:
1️⃣
تبدیل هوشمند:
PDF رو بکشید تو برنامه تا به عکس‌های سبک و باکیفیت تبدیل بشه.
2️⃣
استخراج متن:
عکس‌ها رو تو Google Drive آپلود و با Google Docs باز کنید (بهترین OCR رایگان فارسی).
3️⃣
تمیزکاری نهایی:
متن خامِ گوگل رو دوباره بندازید تو برنامه. نرم‌افزار تمام خطوط و نیم‌فاصله‌ها رو مرتب می‌کنه و یک فایل فوق‌العاده تمیز میده!
حالا این متن رو بدید به AI تا براتون خلاصه کنه یا تست امتحانی بسازه!
😍
🤔
پردازش امن روی سیستم شما
🤔
بدون نیاز به اشتراک پولی
🤔
اصلاح خودکار باگ‌های تایپوگرافی
دانلود رایگان از گیت‌هاب
(ستاره
⭐️
یادتون نره):
🔗
دانلود نرم‌افزار PDF2MD Studio
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cns_q289YvM0Nur87J6J2_p1b67Ye59b4-920jn1T10QAQZseKdob2RR4I9fpBnCkoqYRGkDVH7vXYdm3uaAdrDz0uzChTSailmhl7zr82tk_ehHhcUrDRCKVJUTfdHNcFDyI7oA2Was_xgMi1BKTYDzKcyY2bo6xa8alSzpTfMYHUkxlCxalVZJuJ-dyjWexJuxhHl52yet0jiRv_RsDrMK8BRIY06CbpbtnnSAnYffOON3N9EijEk_gRH2PxOs0iTZc8Sh9kVTnSUM4Aktt9zqXSFUYioGiH_pLynO5kNRkAjFZtmI2tCQgdwW8T1JwFHxgUN8ZJ_p8lhPQD0zQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100
د
لار برای دسترسی به API بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدمت یکساله )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
25 دلار
و شخص دریافت کننده
100
دلار
دریافت می‌کند!
همچنین 20 دلار پاداش روزانه
🎉
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q--KTpyvxop-aGlOdMLc4n9UJ3ut2fpTOrpMUamlZ4ZE7NIvRWyj-RpmAMztOtMJRApxV6QiR4Dx_auY05C02999lKPG7JKdbQPs0n5rfvH6dPYKCLa6WxutzEwRIy_O8VtkLg3Eq7ZMtW7iRjrHvKBeXFB2X9eedhmmbjvHv9tYN69Vqbe7pgaMJVGAsCgdD24luyDOW4yzLT5p-QKeMNjdSEy3-ECJCwHPBc9iTWR_paXEZHJ5YWZoLdpuwp-CRlDQm8F7_pIMBVFVV3VBNjuDOoWR847e4D2jwmgk5nlOo7dSbv6yjcTRpXKbwipPZYUtFmHk-uqqkLo-nkleQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت 10000 کریدیت رایگان سایت Genspark
💥
🆓
با این روش میتونید داخل این سایت برای مدل های زیر و دها مدل قدرتمند دیگر 10K کریدیت ۱ ماهه معادل ۲۵ دلار دریافت کنید
💵
😎
Opus 5 | Fable 5 | GPT 5.6 Sol | GLM 5.3 | Kimi k3 | Grok 4.6 | Deepseek V4 | Nano banana 2 | Seedance 2.5 | GPT image 2 | Gemini 3.1 flash TTS
✅
❗️
نکات مهم :
چت متنی در این سایت نامحدود هست ، محیط وب سایت یک محیط دارای Agent هست ، همچنین می‌توانید از این سایت API بگیرید ، همچنین این سایت یک نسخه cli هم داره
برای دیدن آموزش کلیک کنید
✅
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_c9SbZH7C8HPlGsvDm2NhzKIaOGq8cMC7TMef0ypzlShOs0-TPAe901QyiMQrG9onP05JI_0JL7Psa67tGox-YCZziW6YdNbXWRpn-RLhRuAtsxlsvk8BcV2916OSQ84cDiUT45Lae8a1DOf70wd9oYa3NrKXLucoOXpteFucF-OpSTJUEXeJ62yhJE5hhkMCClKyBYunVJ-vPueDANX-X3vu438XMDaTPh14dqY-MMz6D9U3gfcs8SYV55M09YzS9PckyCpaJRDIYtYnr7xCxGRLSLxw0iEKHuF1xn4KRQdHZDsRdz-bfB9S96iFslkgGE6OVKwp1WLzXc2CvLuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
ساخت تصویر با هوش مصنوعی؛ رایگان و بدون ثبت‌نام!
🔺
بدونه اکانت و کارت بانکی
🔺
بدونه کردیت و واترمارک
🔺
بدونه هیچگونه سانسور
🔺
تا رزولوشن 1024×1024
🔺
چندین سایز تصویر
🚀
فقط وارد سایت شو، پرامپتت رو بنویس، فرمت رو انتخاب کن و تصویر رو دانلود کن
⚠️
مدل دقیق استفاده‌شده مشخص نیست و محدودیت رسمی روزانه هم اعلام نشده؛ ممکنه در ترافیک بالا با صف یا محدودیت مواجه بشی.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=HEvrUdbdrxik2Vf8z-FOe5ngKYeGeO26Put1mOWwlyYfQJoAlB_BOUwCJSHPC_CrtmvU5HoFcgc1JGfqfSg-eX65Cw0SKgW87liHUCabQJ7u2FGxgFXv7dvwelkyf43FIDiTtTduccc-aP2qzec3BZ8tTdfjbvHYAl0Vdd-hnFxo1uVX4xPw6no37s1snLNzx_Tlop5olXAZZUnHXnhR8JW8z3QpIqjnbOuIUPxdWkramLBLbMeeVDTwLoGaMfpHxTouHdfJQbGO8JkViQ4aUAU6HvsM-Pk4KINmT3jZDY-8MlHjvRDefA7FtStpUYzQf2k_a4xX1PpOgXEUERpjSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=HEvrUdbdrxik2Vf8z-FOe5ngKYeGeO26Put1mOWwlyYfQJoAlB_BOUwCJSHPC_CrtmvU5HoFcgc1JGfqfSg-eX65Cw0SKgW87liHUCabQJ7u2FGxgFXv7dvwelkyf43FIDiTtTduccc-aP2qzec3BZ8tTdfjbvHYAl0Vdd-hnFxo1uVX4xPw6no37s1snLNzx_Tlop5olXAZZUnHXnhR8JW8z3QpIqjnbOuIUPxdWkramLBLbMeeVDTwLoGaMfpHxTouHdfJQbGO8JkViQ4aUAU6HvsM-Pk4KINmT3jZDY-8MlHjvRDefA7FtStpUYzQf2k_a4xX1PpOgXEUERpjSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدها ابزار متن‌باز و رایگان، همه توی یه جا
💥
🆓
سرویس NoSignups یه دایرکتوریِ از جایگزین‌های متن‌باز و رایگان ابزارایی مثل فتوشاپ، کپ‌کات و فیگما رو جمع کرده — همشون هم به‌صورت آنلاین توی مرورگر کار می‌کنن.
✅
🔺
بدون ثبت‌نام، بدون نیاز به کارت بانکی
🔺
توی کاتالوگ، ابزار برای برنامه‌نویسی، کار با متن، عکس، ویدیو، موزیک و خیلی موارد دیگه هست
🔺
همه‌ی ابزارا کاملاً رایگانن
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOhYRlhqcgLo3bfqvj7EN9vq1z_MLeGpE2e3m9hHOnsPAlXkce9y-_9KC9r2gvAr1CPUexRvMimdrC_JQU4BbEGhtzZmmzEFx1AObln4dW0uXmgcPRwymAs02woNC4J9nDSR-gvl5IL20TwwxYTIcSnEc2mv5cmed1UzKCNIXiO_37jFXQsMDp9N9nqCH2panM_ym-k_fOyFHllhY3BGreTy1V1Ba5rsm1WHNriYliuBoXuGm9Oeu0DiT4x5l9cFHnT3nAfLzZVq5FtOOPqvT9b2EDaKsbNcvwwfIJ0FkfM_erNAw5fjwBC72y7cet8xmFFmOsZBg67AxVySxor15Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجموعه رایگان ابزارهای تشخیص محتوای جعلی و تولیدشده با AI
🔍
سایت
forensics.media
یه سری ابزار مرورگرمحور برای بررسی عکس، صوت و فایله که کاملاً روی دستگاه خودت اجرا می‌شه — هیچی آپلود نمی‌شه
🛡
✨
چیزایی که می‌تونی باهاش چک کنی:
📷
تصویر:
تشخیص ادیت و اسپلایس (ELA)، متادیتای عکس (مکان، دستگاه، تاریخ)، تشخیص تولیدشده با GAN یا دیفیوژن (Midjourney، Stable Diffusion)، واترمارک نامرئی، SynthID گوگل، کلون/کپی‌-مووِ بخشی از عکس، و متن مخفی داخل پیکسل‌ها
🎧
صوت:
اسپکتروگرام، تشخیص موزیک ساخته‌شده با AI، فینگرپرینت صوتی، ENF (برای فهمیدن منطقه ضبط از روی هوم برق شهری)، و تاریخچه‌ی فشرده‌سازی
📁
فایل:
هش SHA-256 برای اثبات دست‌نخوردگی فایل
⚠️
نکته‌ی مهم:
هر کدوم از این ابزارا فقط یه سیگنال جدا رو می‌سنجن، پس هیچ‌کدوم به‌تنهایی حکم قطعی نیست. برای اطمینان واقعی باید چند سیگنال رو کنار هم دید
🔗
لینک وبسایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=Yr3FfLkTlWbwTTB9RPyYUhmz_IwjU0pipK9FvYujjdSSGw5EJ5iOabMlGKuM6Kr0hD3jlp6FIqK1Jra9eUjy5xBy7QrIjZAlBoIAXxA31v_39DFsKaPq5DJhEgYnRPv2nW6gjTdBC3oQRlJV3QcB14WK_Wmpr4hDV6ucW2sglzcmsdrJnDJ06Aa0a67o29i_MkyFIBcM9kwuVOviekd0U04M7T5KR3_tepU5vqQLSl5_z2TqbRWv5t1lrflT0aYriLgb7EVIIk153DMGIr5J-lGKMQtbQNc3SdYTSqnATT4ZgvpXIQdla1TD2sLQCTmJATNxUa3add2A-lvQdHLl9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=Yr3FfLkTlWbwTTB9RPyYUhmz_IwjU0pipK9FvYujjdSSGw5EJ5iOabMlGKuM6Kr0hD3jlp6FIqK1Jra9eUjy5xBy7QrIjZAlBoIAXxA31v_39DFsKaPq5DJhEgYnRPv2nW6gjTdBC3oQRlJV3QcB14WK_Wmpr4hDV6ucW2sglzcmsdrJnDJ06Aa0a67o29i_MkyFIBcM9kwuVOviekd0U04M7T5KR3_tepU5vqQLSl5_z2TqbRWv5t1lrflT0aYriLgb7EVIIk153DMGIr5J-lGKMQtbQNc3SdYTSqnATT4ZgvpXIQdla1TD2sLQCTmJATNxUa3add2A-lvQdHLl9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوی ترین ابزار افزایش کیفیت ویدیو رایگان
💥
🆓
🎬
هیچی نصب نمی‌کنی — فقط فایلو بنداز توی مرورگر
✨
خروجی با کیفیت 2K یا 4K، هر کدوم بخوای
🔍
جزئیات ریز هم تمیز و شفاف پردازش می‌شن
🎁
کاملاً رایگان — نه واترمارک، نه حتی ثبت‌نام
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_sRae9knZ63AvJn36KmOAeRdRr9HpRGsRuSZsErgVTOTG_rUheERX0-3q40Ae-LCSPfhk_DNJ9V8aQ8t45OnXpRX36QOZW6VW16bzYDiuCuu01AgF7h0wkONQP1PBwLuTclBxhv9tzNj6r60rx5nnq2tNz7XbtD0S4OQ8aRSRCtaM_hsrYDRctDcw1GYmBcJfyu7qltK5YkCTDeu92411T2djTS5Beg-tT3heW-MQ6is1FTso0SXi_M1UZihUIbWdqN7Xci0LMO7QmVbGwhde_Nldrhw51cdgrLtM7_t-LJKY-wGo4UspefZHh4-QWN3G7tcb6xz9dPPGdZXzDzFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به API مدل های رایگان
💥
🆓
مدل MiniMax M3 و چند مدل دیگه از طریق Ollama Cloud به‌صورت رایگان قابل استفاده‌ان ( با محدودیت روزانه و هفتگی
⌛
)
1️⃣
وارد سایت
Ollama
بشو و اکانت کلود بساز
2️⃣
با گوگل یا جی‌سوییت لاگین کن
3️⃣
از داشبورد اکانتت یک API Key بساز
4️⃣
کلید رو به 9Router یا هر سرویس مشابه دیگه اضافه کن
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uv81pk14zbW4VyyHqNhhiVft0uv8nQoHybv5gzYxjy-h2e3Q8a1O2lz970wYxpvs-NsIaIb0tIdexlPTAk0Efd0z-M0zbwkq548Zm4HLQjLNRyfvV5gktXF-ir3ksZTF5Mnjsiu6TjMDdi3iGhfJl9OX_2VmqqqBpyWzsPwbfXKDupUHyOQAvPQcSTD1OwygYuF_sdT3FWH3QzwN07i_MW8DZS098i8KqqUyuAvZMkzAzw3MAHGePto5rSn2WwLMOk7xxpaoqK65piJiG-K502Eg4BwzpH_0Bnvxdx-rpYdqIaZc2_youqkpQBeCRx6xFiwMpaTEXhU_FUJCijJvBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
DeepSeek Harness Studio
رابط گرافیکی ویندوزی برای DeepSeek Harness
🤔
بدون نیاز به ترمینال یا Node.js!
🤔
نصب خودکار در اولین اجرا
🤔
وب UI رسمی داخل برنامه
🤔
پشتیبانی از پروکسی داخلی
💎
https://github.com/ScannerVpn/DeepSeekHarnessGui
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K31KEftgELS2BAFq0a7k3O_IFij2W7moGrSxcWXT1R09awpS88_X6Y4Jj6QrZNx6lnUfpDBCfGkkpKobvYdQ9TT4ivlteVuujr6QNq9Fc4nJlFD1ch1JtX83g1pYsLWy2IXPiSoz5BTSq0ypA_AftKo8lic6JqOwj3Q85ladjZ9JVPltUEpoPYp60NqZywrycW30wo0m7Eq0R_n3I23GzuEeF15sg41z0EwwXNkgINXX8sezxwxi2-NJL8NqyJ1unQwF8w2EtT2i3BSXJxxy2b783ih7xtdi4BQtKDpTxOYNL_ETsvehQGjKsfp9nzgHEfk7UGQL86h-oZfWX5xKgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hq7mOODTq02zDllTr57WtywcaaAqQreWQFrAaCCOhnbTLBfZj2_bGH_ftocfXvKKxlmL8bpl2ujpCFOH18PefhNGvFw37PG4lQ7qm4HI95e-RpAf7fnolq6ShisGyYI54Msoj4CHUd-DHJ2uEn7Y41UgqqWj_PmU4tu7bS1eQxee7kUMhJPKR-cj1WIsDg4v7rC90zdplBnKng2uEwyCT-HnZgFDSxyBzYoCqo308MWg3OtodXYYOsOBQpsAF_bQyOlBAEq6yIfLbWyWpavXUwb068AMw-7jBPPLouIdhwbJ4yRqu1-Oz0QLYtC8-uLY47UTKdx_udI9SHzE0HkJQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kIjdgDYirGXnmpulADBGj0Mu4PBnMAxHklAK4-kW1YVFSuR3OuM5MT3gyR1AyL2CAuuZHMAp3EjqoKkPtaKrrNOSCim483fXgJJKaw8ykNZ_6D4fbaanUSfc90NbMPcg8BE4IpXvkN9iEo5sJ6IOmEYmVGqsiuV6l4wCDa8iKuZtkHAr4-KLc9_WLBCLyHE07EN-C0Ujxc_ASbHj5SDxLVxALWXRyxPKyrlNwBQ3N2pq6bZ79-xp6fhYCOvjCWgO_qCcxqyqEXgOdYzxuZjm1oo78rhK2lCwM1yoHLq0MOG-1skx96TTMHoE7thxNjVC32M3_mpfq9Tdmgg6iJCBwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fg7cJ0LgXUBUvEpA4jSZqiklXyd194q55t0SCYILBgNkm-eF9rc11pawZkVFkwE3hFZO3bLpfMZtkEGWyYHRdDgB5PqbxOU1eHVIEytcWn7Q4anQmeQBnVm4Be7WJLavdr7lKQJ93gItIG396895rQP5EdImhBHDMjW3oJhVd-3eNwv4GbRx9Lw290byHWmr8jM7lKBXKJ1FjQI5XX8WHmQKl_YH5P6O_tGJjtNA1YhhgYyEM0YaNM7gkoj3Teivo2chcAvtN6JFrMr1hzWmFsAWbAg1IMv2Q7jBmePjtwRGjW7reuei6wSyc_u6PRAnxX1lecmwGQbfAS4FgGj7jA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🛍
خرید اکانت
Windscribe
با کریپتو از طریق
Build a Plan
اگر قصد دارید اشتراک
Windscribe
تهیه کنید، می‌توانید از بخش
Build a Plan
پلن دلخواه خودتان را بسازید
⚡️
کافی است مقدار دیتای موردنیاز و مدت اشتراک را انتخاب کنید، سپس در مرحله پرداخت گزینه
Crypto
را انتخاب کرده و پرداخت را با ارز دیجیتال انجام دهید
🪙
🔵
انعطاف‌پذیر و اقتصادی
🔵
امکان انتخاب لوکیشن‌های دلخواه
🔵
پرداخت با ارزهای دیجیتال
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRVJDVoxQKfGCfxkkOzjvdk3aFiW1jSZPya-eYPT7MLn-4BSh4NxQUASS45OD92EB0mdBNthU7QD7K86DXl9mTqimW70_7vNzVP4wTdVwEpC5p6BXBVZj3DfdYVAm6SpFy4KbWjamqiD9iqNh7LIrWVDYXWReE3RHEnN_b2xPzhHx69glFmpXyq07DJZhPVrsbl586gQ4FWlfKPL_pfr2K9UXrhz23Sn48QnpJmnCCNKrx2kUU9aYZoXqyydQsA8grPHmcNetAh4FBxFSxfecEfsE8dECvIvOfDuQ_a8AtR5lSrR3slRx_kq6eqOzGL3A4Gt-MiNlbSNZpTdlUnsKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!
‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون
‌GLM-5.3 Flash⁩
محصول شرکت چینی
‌Z.ai
⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی تست واقعی با ‌Cline⁩، هر دو مدل از پس باگ بر اومدن، اما Ox Alpha با مصرف یک سوم توکن و سرعتی خیره‌کننده‌، برنده بی‌‌چون ‌و چرای میدان شد
😎
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">عکس‌های داغونت رو تبدیل به شاهکار کن
✨
دیگه لازم نیست از عکس‌های بی‌کیفیت بگذری! نورون InvSR رو پیدا کردیم که هر پیکسل رو زنده می‌کنه، بهش عمق و جزئیات واقعی اضافه می‌کنه.
🔥
📦
نصب لوکال از
گیت‌هاب
🖥
آنلاین رو
Hugging Face
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">Avast SecureLine VPN
4KAX6F-Q7LM6J-5LCJ6E
3N7RAW-SG38HJ-5LCJ7W
BJS8N3-NNAVTJ-5LCJZJ
J3BSAR-XJZR32-5LCJME
VUYR9T-JZ5GBJ-5LCJVN
23RWWJ-SEAQGJ-5LCJTN
GFU46H-QA2CDJ-5LCJBE
7SKUU3-S97Y42-5LCJD6
UENGEB-Y9NGA2-5LCJEE
EBF8PY-8CPH82-5LCJ6J
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5bQ3B87hxxpMW9jnyK_PvxeQXIHg_qX4dcnTdAr6bZxdjqRQ3SizAAwzMfMdOxS2xiR6LrNVPz0vHZdNRa2R3selFQypHk-AdPR2ZLYIHQ_Jv3zMqRA-fXEsf30bmsiFCC_ZLc5uPKE3_mvvVuplVvzZ9TIUUdnOu-Y3dsbSuutZMQfUFaOKgle7uAccLbJ09CCXfho4GLkTtJnVU44UO4Eo6n3w4RWEvJ5JKFDmKAoMh-o4DGCOq8G1IuweEQLePnKp58vHM485rXoyYKfEq9iuaX9hvGhyXqcxEc0JB4eg2j7MKCZnZOFihjNYbV4UyGjIQFgXSisXc3Ryl8Yug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب
قدیمی داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
100 دلار
و شخص دریافت کننده
175 دلار
دریافت می‌کند!
فقط در کلاینت های گفته شده در Docs میتوان API را استفاده کرد
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lw8HNZJv1Z3FmASeZRBiiE33cc4-D2LONg5FeWhalLZeXUxJ0vJhtZoPpJCUX9BoTvdNCxvSqa9FxNne_EzXfGBWPI6MABX0578xSXQhHfAWSQ021iyS86CpX_bZmtqEEsLWSYHW4jwFr6M8vQ3MwDCcAzDCxtJArSMW_gTdFmHakwOL9jgB831zSaIvlz9DcC83Z8W8Qv6EUh7jWiR8uJ-q5YQlf58i0N8PZUfj21g4ld6f40o3yl7pFNbpM6HCZBWhFY3VojLK6pM0nk8WryWQC1Z5K2LNOi-llDbCJem-3sFLpLJ9M9lqkxzLib6d8-BBRsc-OEiS0YyuqwsLIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌های قدرتمند MiniMax M3 و M2.7 به مدت ۱۴ روز کاملاً رایگان و نامحدود روی GMI Cloud در دسترسه
⚠️
⚡️
📌
از
۲۴
اوت تا
۶
سپتامبر
🔥
همراه با
Speech 2.8
و
Music 3.0
🪧
دسترسی از طریق
API
خود
GMI
یا
OpenRouter
💎
بدون محدودیت استفاده
⛓
Link
🔝
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqzLj6aI4T2bpmFYc9YzYUo5_T7nguWTmZHuWQ3_N7x1NMKUeqM5S26Wku-IRSNWJR6mdnid7oWJihFcfwjaiMJM3V8_9I2l1RbYrmCQqu-EUfGQ5qGwvosbNr66xCgHILD1abpL1gAkssaFYduC_jtv-ZINhdpWY5RnDHZQgaobq-Fc9_j8KcC1VVZc-ycLSeBgqeE2pQ_UPej3xyn91PqsNmf5aR0b-O6W9ncopVAqKv2vcSA3UUXdPMKV-pkBq2fAeF8sZdnnc3-GzUP0Dbk9uA4gOQg2UF9AkGHnNRGSkzwnzNpHZN5CF9R5RN7vchibcNQ655VRkm4jnbplHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API بسیاری از مدل ها مانند
💥
🆓
:
Gemini 3.7 Flash | Gemini 3.5 | Flash-Lite | Gemini 3.6 Flash | GPT-OSS 20B | NVIDIA Nemotron | Nano 9B V2 | NVIDIA Nemotron | Nano 12B V2 VL | Ling 3.0 Flash | North Mini Code
✅
📌
Base URL :
http://aihubmix.com/v1
🔗
لینک ثبت نام در سایت
🔗
لیست مدل های رایگان
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyrvxLN9RaRGDkrp_PcPcHF7D4i6Xos31ZfgB8UYpcncmGfhA6R9PCSkmvjRSgS1z0hLx8CbN-CmbhIYt7MKeDKfccW45VtCqWLw7HKmhq52M0IyCCX4Yw8cEO7vFSPlA7NpzvFfHeVIGO8PCtPryIQWKgwejE_78wLZweAlyWrn8uTtPrCVt6SdUzp4tG3KT2OPPoIqhOAL0iRyg8K9JOBzcx-oHQboCarMIqOMemXmwvj7CAwdX4eJMGRDVEl7j_6E-Kk-97M3HhHLEb_4g_bk1ryFeC4rWvb8xf1LbwbGX4CB1fxiwTVxmbzZQu_fxSJp4u5Z7w4-9ZKwyzAZXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به برترین مدل های ساخت ویدیو
💥
🆓
Seedance 2.5 | Kling V3 | Minimax H3 | Seedance 2 | Seedance 2 fast | Happy Horser | Kling V3 Omni | Kling O1 | Q3 Pro Video | Q2 Pro Video
✅
با این سایت 1000 عدد کریدیت معادل 10 دلار برای دسترسی به مدل های بالا دریافت میکنید
🚀
✨
مراحل فعال‌سازی :
1️⃣
وارد
این سایت
بشید
2️⃣
پلن رایگان رو انتخاب کنید
3️⃣
با اکانت گیتهاب یا گوگل ثبت نام کنید
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL : https://api.b.ai/v1
📌
Model ID : deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید …</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_5jThJ27YoLIAaMsHWooR5J2_gv6FwC8Iwxbj9tMi9MZSoY4oHLkYSn4xIs7ZBHpYqqN4C_g-fIa-GSwNd4E_-BlTLNGrkaX-qBXQg0ZBHNiD_4uqDnfZTNQUo2TCN3mMpmvAknlkUDfE6bcmYvm5pf4lVgMlfBwOjZcetw4PA8bFRYECZtFrlCCOQofhpcOSHDZgIaZaDs9I3j63iEBkKiWKccvNYsOE6xxVbKtlbFnzz3zkDiL67-aUZ-g86s6sb3rBG6T49Y7dq3Fdjs1G0fqMOQfCnP4v3hMD2m6vNpRWLNygb81A1os1V8YOvdgYcf7bdnPRFiQtQGSzMdsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی رایگان به GLM 5.3
شرکت
Z.ai
یک اپ دسکتاپ جدید به اسم AutoClaw معرفی کرده که یه دستیار هوش مصنوعی agentic است — یعنی می‌تونه به‌جای تو روی فایل‌ها، مرورگر، برنامه‌های آفیس و حتی پیام‌رسان‌هایی مثل تلگرام و واتساپ کار کنه.
😎
🎁
هدیه ثبت‌نام:
کاربران جدید ۲۶,۰۰۰ اعتبار (معادل تقریبی ۲۰ دلار) می‌گیرن که تا ۳۰ روز اعتبار داره و می‌تونی باهاش مدل پرچمدار جدید GLM-5.3 و همچنین DeepSeek رو امتحان کنی
✨
مراحل دریافت:
1️⃣
برو به
autoclaw.z.ai
2️⃣
نسخه دسکتاپ رو دانلود کن (macOS یا Windows، نصب کمتر از ۱ دقیقه)
3️⃣
با ایمیل ثبت‌نام و وارد شو
4️⃣
۲۶,۰۰۰ اعتباری که داخل پلتفرم منتظرته رو فعال کن
⌛
زمان محدوده، هر لحظه ممکنه تموم بشه — الان ثبت‌نام کن!
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کانفیگ amneziavpn
[Interface]
PrivateKey = YM8CabYhib72x4z1G3Tv6YPTzkN1EgieYgzRAiEOXGA=
Address = 10.0.0.3/32
DNS = 1.1.1.1,8.8.8.8
MTU = 1280
Jc = 8
Jmin = 74
Jmax = 195
S1 = 115
S2 = 80
S3 = 44
S4 = 21
H1 = 220741314
H2 = 689752078
H3 = 1491205382
H4 = 2102461473
[Peer]
PublicKey = MF3gfbfjik3PoBeXrASElNP8OOXDlalC1ZCmLfqUuSo=
PresharedKey = 5AUecEnESNGx35D0nM1REFG1HAGtUuLTxlzhUHDhkSM=
AllowedIPs = 0.0.0.0/0
Endpoint = 65.109.215.18:51820
PersistentKeepalive = 15
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWWOdGZ0-eY65FwGZTfeKofNiIjse_TDGmxZ1TSEByOXyOkXs2pS7ADMz0ImoeeXMxc7EdwkoxOWfQXJehNm_VQjIAwfMk1kNHjgy-PNAJO_gK8A_inMW9gATBXwbvy9Yenl0aNXNCRHRxKOrwgZN8mM5J0YCCHLzbnKqAijZEMqfH4ktvk69RgZh25O_xErmbV7mPTtWT4J2vhJkuuiZVmzKJL0T9hKP5--NL_KL6gOcnLY9aoDTMTsS-NM46qQZFEWeBVRZ9fkmCA5G3VTmsnOENbDJvioYJ7IqW1YDb7CTRv_498k2ROf0c0rGiMKKEAJiZpTrIZZhQ4FYD70cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)
همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟
پروژه «روح‌گرام» یک یوزربات فوق‌پیشرفته و اوپن‌سورس با اتصال به Google Gemini هست که مستقیماً روی اکانت تلگرام شخصی شما سوار میشه و رفتارهای یک انسان واقعی رو شبیه‌سازی می‌کنه!
🔥
قابلیت‌های خفن روح‌گرام:
⭐
کدهای رمزی و نامحسوس (Stealth):
با کدهای ۳ رقمی مثل 777 یا 666 کنترل میشه و دستورات بلافاصله بعد از ارسال پاک میشن تا هیچ‌کس نفهمه!
⚡
شبیه‌ساز واقعی تایپ و خوانش:
🌹
قبل از جواب دادن، اول به اندازه طول پیام «مکث خواندن» می‌کنه، بعد علامت ...typing رو فعال می‌کنه و با سرعت دست انسان تایپ می‌کنه!
🎭
تغییر آنی شخصیت
🎲
با یه دستور ساده لحنش رو عوض کنید.
دریافت و استفاده از پروژه از گیت هاب:
https://github.com/faithsaly5-stack/GhostGram
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=N_RQJVIf1DhgWOPWi3KcWFxKtL6nTTo-wSCsY0CY0fELz15D-vpMcsroB7sx_e6DdXpZwlINYTHafrUECmKbRLfvQ2g6OWA5hOPtvr8P8mMvasCyQ-B73Nr_QG6eDKJIJtaJap_M5bPNBLFzD82fULVQt4KNQLeAsy5cSwAlW438aAFvi9QSwhYDhtnGeGa13iJf3wUqCzvwm0gty5-0Rv_sswcROVwh9VLSeMW6qfY9egnVfVLEpEnW7Kcv8mcR0ANy22tnoMUphnhVdpWsKq9nRtaPzHjdWi69w9K7kxtKqBggeERKYQYyx7dPzSM6HJeK-qpz4aJP9MXoVYuxWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=N_RQJVIf1DhgWOPWi3KcWFxKtL6nTTo-wSCsY0CY0fELz15D-vpMcsroB7sx_e6DdXpZwlINYTHafrUECmKbRLfvQ2g6OWA5hOPtvr8P8mMvasCyQ-B73Nr_QG6eDKJIJtaJap_M5bPNBLFzD82fULVQt4KNQLeAsy5cSwAlW438aAFvi9QSwhYDhtnGeGa13iJf3wUqCzvwm0gty5-0Rv_sswcROVwh9VLSeMW6qfY9egnVfVLEpEnW7Kcv8mcR0ANy22tnoMUphnhVdpWsKq9nRtaPzHjdWi69w9K7kxtKqBggeERKYQYyx7dPzSM6HJeK-qpz4aJP9MXoVYuxWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡
مدل‌های غول‌پیکر روی سیستم گیمینگ خودت!
محققان دانشگاه‌های UC Berkeley و MIT سورس‌کد سیستمی به نام FreeToken رو منتشر کردن که مدل‌های بزرگ MoE رو بدون کوانتیزاسیون شدید، روی سخت‌افزار معمولی اجرا می‌کنه. سیستم به‌صورت هوشمند محاسبات رو بین GPU، CPU و RAM توزیع می‌کنه.
💻
📊
نتایج کلیدی:
🔺
مدل Qwen3.6 35B روی لپ‌تاپ با RTX 4060 8GB تا ۳۹ توکن بر ثانیه
🔺
مدل DeepSeek-V4-Flash 284B روی RTX 5090: ۲۲ تا ۲۵ توکن بر ثانیه
🔺
حتی مدل ۷۵۳ میلیاردی GLM-5.2 روی یک GPU ورک‌استیشن قابل اجراست
✨
ویژگی‌های دیگه:
🔺
پشتیبانی از ۲۰+ مدل باز MoE با فرمت‌های مختلف کوانتیزاسیون
🔺
یک API سازگار با Anthropic/OpenAI برای اتصال به Claude Code، Codex و ابزارهای مشابه
🔺
نصب یک‌کلیکی با GUI برای ویندوز و لینوکس، بدون نیاز به تبدیل GGUF
🔺
متن‌باز و رایگان با لایسنس Apache 2.0
🔗
لینک مخزن گیتهاب
🔗
لینک وب‌سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=hYBm5WBucBcocasOBvrS0EzSB2HjOEKB79tN_gwsJVyGcuaS6dwKEqAQn0dHEdCQdCkuB2X2fSQvfcIbvTCCiqktTIDuHMO-MHyxJ_nNUAVMj3xqMazdkBGjiv1y9cyw1_jPqYeijhO-GI3dv8zDjZ58WZoETjcV0hprHnmkhaZakIKpDtebF2okAlTsor0ypuZLU9cuTNddnG7LtOPtTdA7YbL1rLtPYT-saZUWzfMkTQ2uf-ZZVyWWphBop1GiSxEwAzujhSOOx0xduqSKZNp8bkGmpVuins-cle4CEK41RqLg_ryD9afCw-MqlkgfeGUuF-ZRyf-TijoMole2gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=hYBm5WBucBcocasOBvrS0EzSB2HjOEKB79tN_gwsJVyGcuaS6dwKEqAQn0dHEdCQdCkuB2X2fSQvfcIbvTCCiqktTIDuHMO-MHyxJ_nNUAVMj3xqMazdkBGjiv1y9cyw1_jPqYeijhO-GI3dv8zDjZ58WZoETjcV0hprHnmkhaZakIKpDtebF2okAlTsor0ypuZLU9cuTNddnG7LtOPtTdA7YbL1rLtPYT-saZUWzfMkTQ2uf-ZZVyWWphBop1GiSxEwAzujhSOOx0xduqSKZNp8bkGmpVuins-cle4CEK41RqLg_ryD9afCw-MqlkgfeGUuF-ZRyf-TijoMole2gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت خروجی 0x Alpha و fable 5 در یک نگاه
👀
تو کل سطح اینترنت واقعا اتفاق های خیره کننده ای با این مدل رقم خورده
🔥
➡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7548">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCVRDeg7DXDNDUk7ODN5H-VkSPcBs2RnzibZLWbEJhBTNY7tFCKIN2CgOK0VjRbtdPabS4jcC8tqfyO9pypv-eU2n5z7NdudwnzeERM2Ua_eS6Hvjd_jhOoYcJdlWX57MZwgyQPIf1oLNWglggle495qQBBsA9sUO25eh7Y5B53X4Wf2x3AhFSt6Hoy4fH3Y059O7mlGyAcORAJ5VTh84W6Z4meUAaxVXXuUBGRxyrkNY7nNaPm5BTHmCiFjyh3oFP7vH44VdfKTUNiOmbe3rIalNNO7CmXyRhrnTwMZrwqmvgrO-zm8vK_eg2b1XGwLKNbJJweu0NQQwBb9JMyQ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔬
دانشمند هوش مصنوعی که خودش مقاله می‌نویسه
یک پوشه از داده خام رو بهش می‌دی، یه جهت تحقیقاتی مشخص می‌کنی، و سیستم از فرضیه‌سازی تا مقاله‌ی نهایی PDF رو خودش انجام می‌ده.
🧪
✨
ویژگی‌ها:
🔺
کار با هر فرمتی: تصویر، صدا، ویدیو، اسکن سه‌بعدی، جدول، فرمول
🔺
درک مستقیم داده‌ی خام علمی، بدون تبدیل انسانی به جدول
🔺
سه مرحله: فرضیه‌سازی → آزمایش با کد واقعی → نگارش مقاله با DOI معتبر
🔺
اعتبارسنجی داخلی: هر عدد باید از خروجی واقعی کد تأیید بشه
🔺
سه روش اجرا: دسکتاپ، CLI، ماژول ادغام با ایجنت‌ها
🔺
پشتیبانی از Windows، macOS، Linux
🔗
لینک وب‌سایت
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7547">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRuBVQEqYQFXhtGzZaq3DgvrIZws6oyk5_0Dp1cSociguQn3Q-6HnKvoID6Fmy_EgLLVDmIbCwFI3xLsBcivDYuTcmtRi0ZxoS6ikotFkyLCG1LXR13SFXuAcdFTblnVs4v7aJGRqOOuLi61Qk-ukpvVv5ZbgMgd1ijva8iXMEd7RgUv7FxB7daTCtD7rvWzcokKwasF_-4wiIGz9vPCWIw4cqswSaJ8REfMXApl1iJgAhfaa78Xa66EiOU3in4GCJNhlFYP9arjWcqlhIHP2SCejHX4fBL2yAYM3Sm2NEd52s-9yAUPA9imwYrFSKvun0KfVvH8iOXlk9ouOsCALg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جدا کردن صدا و موسیقی با یک کلیک
یک ابزار آنلاین رایگان مبتنی بر هوش مصنوعی Demucs که صدای خواننده رو از موسیقی پس‌زمینه جدا می‌کنه. کافیه فایل صوتی رو آپلود کنی.
🎶
✨
ویژگی‌ها:
🔺
آپلود فایل محلی با فرمت‌های مختلف
🔺
جدا کردن خودکار صدای خواننده از موسیقی
🔺
پیش‌نمایش آنلاین قبل از دانلود
🔺
دانلود جداگانه‌ی تِرَک صدا و موسیقی
🔺
بدون نیاز به ثبت‌نام یا حساب کاربری
مناسب برای موزیسین‌ها، خواننده‌ها، تولیدکننده‌های محتوا و ادیتورهای صوتی که سریع نیاز به جدا کردن استم دارن.
✅
🔗
لینک ورود به سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRLuHbBQ77FFdBrwiw_hocrGMmdpK7f7TSe3AMtZaoOCNXJ-Azrxgv8-0wanvMZoMQpPBPkfaTvRvcYKiLxbdfIdsjInVr5O3v2UhKFqxFwwJpU2LDk3wKuy15weMaWee-ZCMBBuUjwhp2msoo3FeEzPku5aejFASqgxKEJbG7HtTNAwkkiXSqoD5vy_ocFaaTx5KOeSQIbLQ1nZVQgjQN6IRlXZcYuYiwrWqpgZh8yZFOR3ww2-pzEesh-j5Fjo9N-bXlDGgDbhWYnxsP5o3F3T8qp5mP__RZWHH9zzxHvrrDLz18FFxFNOtDY0K1b-Vcog3YwIhm4CIMHq_f3LgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 دلار برای استفاده از API مدل های هوش منصوعی زیر
😎
🆓
Opus 5 | GPT 5.6 Sol
✅
در سایت زیر با ایمیل یا اکانت گیتهاب ثبت نام کنید
( ابتدا کپچای سایت رو تکمیل کنید )
سپس کلید خود را بسازید
✅
📌
Base URL :
https://true-sota.com/v1
📌
Model ID :
claude-opus-5
|
gpt-5.6-sol
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">DeepSeek V4 Pro
| MiniMax M3
♾
♾
♾
♾
♾
ApiKey
—
sk-dc9d4b7df36ba555-rcaq9e-2790fa25
Model
—
am/deepseek-v4-pro
/
am/deepseek-v4-flash
/
am/minimax-m3
URL
:
https://anymodel.org
♾
♾
♾
♾
♾
Free
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7544" target="_blank">📅 21:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7543">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به
هرمس
اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7542" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7541">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">5 میلیون توکن برای استفاده از GLM
💥
🆓
به مدت 5 روز هروز 3 میلیون توکن برای GLM 5.3 و 2 میلیون توکن برای GLM 5 Turbo برای کاربران جدید در اپیکیشن Zcode
✨
مراحل دریافت :
1️⃣
وارد سایت z.ai بشید و با اکانت جدید ثبت نام کنید
2️⃣
برنامه Zcode رو دانلود کنید…</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=OjzBTX5KL6FYm9rPjnGIlJU3lRDEUGsLSOqX6kVAn3X1B7Q6UKYOeI9XqChPSIGih143QvWJGgsl8im8mL2E8PD4GD-DRDdLCv0CoxZw1OynhhCzsXACqFwiRHU9MtPZzzhTRU_O1f-dc1oIJA5VMRLlReJjSHsmj7QTdGo7ToZu5qrBaDgNcyonc9UIi_ezfqy0uUggfc7iDtZqm_1ATDDDjUqqH-EqGvGgOxDrOl5-LVxjVOdC8qNEgZVLmT5HVzf0dZ8LB-U2n0kRiWNS86v7b8XAfIiH3f5FnTuUjKI4RzLnsKYZuWU0Ka_7wmzUqEf_zeWxgWgfABDH5ttHpiNSDRXPiDp6XxiTa_glbI9bUYaxmQsJ3p1KxKpAjReu6bIL9VJ5vY4us2-7F1ElsuMUo_rTB1lRTC1KrZ71iujmjj9mUhuZ-JIp8WX_DjUir9A_CjsKZCbNIe3WOCg_8UBOmmmLoa8vmVLxIVP9pYYNHHLtOUmcCbKZ1YIZJtFlEC8nV67BcV_0No1DFwRk8ksTguwIpTMDoycYNkcn7g1BsVnvzX3mBhVTkYQGt-17VG9R0tQf2gF4_UBlRg1f4qN2B2z6IOOt9I5yTOQIwlo2eGEZK0nm1EDrnLi-yDNNu0k_h2mwNDbJ-v1HxWdBtvXY7cvtur5UFlSsKdKvXQ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=OjzBTX5KL6FYm9rPjnGIlJU3lRDEUGsLSOqX6kVAn3X1B7Q6UKYOeI9XqChPSIGih143QvWJGgsl8im8mL2E8PD4GD-DRDdLCv0CoxZw1OynhhCzsXACqFwiRHU9MtPZzzhTRU_O1f-dc1oIJA5VMRLlReJjSHsmj7QTdGo7ToZu5qrBaDgNcyonc9UIi_ezfqy0uUggfc7iDtZqm_1ATDDDjUqqH-EqGvGgOxDrOl5-LVxjVOdC8qNEgZVLmT5HVzf0dZ8LB-U2n0kRiWNS86v7b8XAfIiH3f5FnTuUjKI4RzLnsKYZuWU0Ka_7wmzUqEf_zeWxgWgfABDH5ttHpiNSDRXPiDp6XxiTa_glbI9bUYaxmQsJ3p1KxKpAjReu6bIL9VJ5vY4us2-7F1ElsuMUo_rTB1lRTC1KrZ71iujmjj9mUhuZ-JIp8WX_DjUir9A_CjsKZCbNIe3WOCg_8UBOmmmLoa8vmVLxIVP9pYYNHHLtOUmcCbKZ1YIZJtFlEC8nV67BcV_0No1DFwRk8ksTguwIpTMDoycYNkcn7g1BsVnvzX3mBhVTkYQGt-17VG9R0tQf2gF4_UBlRg1f4qN2B2z6IOOt9I5yTOQIwlo2eGEZK0nm1EDrnLi-yDNNu0k_h2mwNDbJ-v1HxWdBtvXY7cvtur5UFlSsKdKvXQ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
استودیوی هوش مصنوعی که خودش کارگردانی می‌کنه!
اپیکیشن MiniMax Design یک اپلیکیشن مستقل برای ویندوز و مک‌ هست . کافیه ایده‌ت رو توضیح بدی، هوش مصنوعی خودش برنامه‌ریزی، اجرا، کنترل کیفیت و نهایی‌سازی پروژه رو انجام می‌ده.
✅
✨
ویژگی‌ها:
🎬
ساخت تیزر تبلیغاتی، گرافیک، بنر، محتوای کاربرساخته (UGC) و انیمیشن
🧩
ادغام فیلم‌نامه، استوری‌بورد، ویدیو، تصویر، صدا و ادیتور در یک فضای کاری واحد
🔌
دسترسی به پلاگین‌ها و مهارت‌های تخصصی متعدد
📂
امکان وارد کردن فایل‌های محلی و اتصال به سرویس‌های خارجی از طریق API
💰
بعد از ثبت‌نام، ۳۰۰۰ کردیت رایگان اولیه به کاربر داده می‌شه
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7540" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

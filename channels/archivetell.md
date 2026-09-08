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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 13:27:39</div>
<hr>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JefVfhcxDBzK5O0278mrGXAv9XycRkQkCS_9GXyKCL0VoVe6EgCIxj5LsA6TvT-4voNaM65Aib1p8U0zDcZJg6hzTH6-do6-lnf7L68Y9lJBlD2ONCd8JJ-dPnDHihVwUGrhumvLMxUxCqlgf4zDSd7qnX6KQfcszu8jxBKGi00VNlG03gbn9lXWwAkZ_lLxMSppxr-dgyVdIHuwt4eJ3M3Xp3zUkhsjTbwZPIi7Oojuyntntk7PtkyqtkJixyXw8Br2tsawSZ_tMAOSLvb-BK0I1QsZbBJmXhGymgHkLNZiHKU5ENHoOG-DLNv8Cyb3nkauOaygNUA56WQm4yRUZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توکن‌های نامحدود برای Claude Code با شاهکار مهندسان اسپاتیفای!
🚀
🧠
پلتفرم
Portal
مثل یک مدیر هوشمند عمل می‌کنه و با واگذاری وظایف ساده به مدل‌های ارزان‌تر، تا ۹۰٪ در مصرف منابع و توکن‌های هوش مصنوعی شما صرفه‌جویی می‌کنه!
🔥
🔺
تندخوانی با Gemini (bulk-reader):
فایل‌های حجیم و چند هزار خطی توسط Gemini 2.5 Flash آنالیز شده و فقط یه خلاصه مفید به Claude تحویل داده میشه.
🔺
کدنویس روتین (code-writer):
تولید کدهای استاندارد، تست‌ها و تنظیمات خسته‌کننده به مدل‌های کم‌هزینه سپرده میشه.
🔺
تمرکز روی کارهای حیاتی:
با این روش، Claude فقط درگیر کارهای پیچیده و استدلالی (مثل رفع باگ و طراحی معماری) میشه.
💡
در
نتیجه:
یک ترکیب هوشمندانه از چند مدل AI که باعث میشه هزینه‌های شما ۹۰ درصد کاهش پیدا کنه و خیالتون از بابت محدودیت توکن‌ها راحت باشه!
🔗
لینک دسترسی و پروژه
✈️
@ArchiveTell
|
#TOOLS
#AI</div>
<div class="tg-footer">👁️ 891 · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7677">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7677" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7676">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/ArchiveTell/7676" target="_blank">📅 00:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7673">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/7673" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7672">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/ArchiveTell/7672" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7671">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/7671" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7670">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/ArchiveTell/7670" target="_blank">📅 20:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7669">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/7669" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7668">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7668" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7667">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7667" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7666">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7666" target="_blank">📅 14:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7665">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/7665" target="_blank">📅 14:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7664">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7664" target="_blank">📅 14:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7662">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7659">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktSbTnPG7jQliAGSuveTjpGqyZkHnPekMgZ6RrbmEscM-H0JGNbYcgxTxGgDCLoBRcVKhWc8BTBs7TKgQBpNjdSvT0tPn_hUzjRA5sowG8_yEohP9aQ0MngaEAojq1vmiORW8DvT3bKvpSvHLOyayfJUl8MChXsXZxIy5u0kYZJNmdRmL3OWQSawU9TrJDUnKMtDOe66tlXVIVfr4erP8GfPZc7HwBaqDboYv3jgDLJUfVtSct9j7uF2svV-ZS66B5y59eIESyo3nn5XmaJZyvwrih5588uvT5tqQ3GdrbWYghtOiJpU00rE8gni_cozwMl5XcSDr3utt_sOr5p-PA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atEe967GOSkyVzBoDjTvO0sseoRN6HvOzF-xqBZz2ZauUPsRXlv02Ut5kOMPq73updKbUPGrQ746YWNADBU2oH8wQ4mnBCJ_rlT1zopn5TqL8mcazBowq0eIq2GRn0DErNMr806uIuqcRqv58zqgW_znyUzsocK73Um3KtrZsmd5TzhOKYS_1AnA2HBkMggsNnFjDlkdeutFZAUou9QQAAulUxIYl5JEvRXDXlyVOQplSYdfor0SNQiD2SPgC3PB_AfcuD0QYV1LlybMyYpWLMpIsngL-BMJntfYkiGZycPXdwIp2MP1u9hi0CxXJ2VOg_A3jtOB3S5sJCGcWx-mug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPy2LzxLfFh1VbQfKB-KfUoYs3Mi_ookmf3HZ-v2sGOfd7U037GPjHhD_hNg6sTRJGUw8248ZENuLUh4z2yerizjutTeCcPpkFhINZo5_KIFz96cPT1UzG6pi3bv9wMJLIIzBzGdId7f_jhTj7u6X-SB76Dz1DeJoiSqdx8l2EcBmXxHbzcox0NpXfSkfSdBk2g5BZlZ-D2z6yvv6wSnLaRQYAPgdkedtObJsVaxiInbLJd1H7DAz1NvIgkUrcYTM2iTRibZEq6DC44Bdqs0zGBWi-MUwFFW5oeAZQSpscQHvCjXXe5J6dxs7cA0wQBdosWeuGCncE7SYDEbRgZkag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpF1YnHhLTssq1na0EiVV8YyRHndXCA7S-qEf8ZNYA-1GkdMwzF3CFwAB3HItyrGdniFLzmFiEqrhl_2b9-TPbEsGG6YLyrczPU1LGlBmKkoqs0AVEM4n9fUHa8NInPqVANO4QJ7w_SZ-heHg-mVXxKknbufNv2JaOckfwouCZfIfdHfvtZB_ixaXDU8HKyx5QrY4kdo6MXuvmSC2geedWeZTBmrlOUdH7enIg5I_k1NgLaR10AAtgp6QSiMXtR2be5IWt96X_NUK6ECZJlC5zK86f4Yjlvd1lsC-KtHcymV6nHRZgfr1XWBU0ZxfQ0PngWB0mkupJBpnJGsLlb7oA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGtWoF94IKAveN1jDh4qqxrjsuPVi7SwTsG8rYGeVO5WKm1HoRb1rlRxRVenTWGqh13tgwtn6IRB9pTGWoWzX929Z5YMz3QuVW4yz3Gc3J7dMRF_-DUueVPWLD93w-IxY5RwV2mSQbgqU9jBS-CNdt6rOMEYBhDBjAFLdNr9DmmCPIDH-iaLE07yQGKgYZuP9zbUxSMqT-JihZV-RpcaLQOmaW5gM5DDfyNgsdDACXkLYmIVvEaElpW6LH7bh8EhsIheLa1Jo32R_XpwOVj2mGvhe84G67FPyWZ_qdOF94eTuDcEYBRXGNKz1jdGORfJs4gIo9xW-YvHdptJnZN0eQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7645">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkol-YBgSRhkyVYMieNfEN8l9cdknn5stDN341QNC95KajJqsGaEiBdvQw3dUhieSz40v3zijeMgxKnCOPs2Subp3x6r86TdC6x4KWOtMsar8M5290kzk_cDG0SlbBYsrgRv6YwT4oJu11txTL54NlmelziZ1vjWpd7G1tSyw19Es3RseI0QkSAt7sOd_K_VncDBOqsAA-dvzn-MFHqKxjz8S2Yk5ndxkcMTJN2AOXKHUXCxFoCrtaBpt0KUAno2k2DCsVlwApMpA-A-T_x5yJ1f2fJH5Faj8O5qNBscHg3A4EKYXpGNvqhjaGfjJYV5nPirp4MQbfL_59aQwLp6vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXMWvp0J3sR3UH2J_s-FhsqZYZ0osoV-scrD4bqlkQRDLG0Qc1WQrmCgpRdfxil06GvbzYQAcH-j5DMoD6B37DD32V4e9b5IwagGhu3vs6-sB-tAx9E8fROGJY07ajq91kYdECU9quv_Bi1T0KqPatK3brXjOQykohyH5ANtEVb1MgqrBpA2t48tZ1kT3YKi1_4yFC3HL91MaviyXMLxpyQj-JPtXIoY1CL9KwvUG6_nTUc3_sS9DmYF1l8vnS8g03FefkQOTC5D2SEFI1uD0NxpFXTuymYN0S6pTStkll4_pRNmCzLhQ5dr1-mACbkSD1IdDHf1nYmAO1vKmD8oJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XA5Z2AWqbAv5SZjSPq3qLf0mipNaGonJ42RK4e2erw5tQ9UfM-LFGX2J65OZ6T5_D5Fyzia8-8MyxNfozvR_4Q_ftEiw_szh9Kb6s-U4Yc-pF-Ssx0D0KZh-EiihvYFef4XeRy3B--BGcCegY0qscb4BmDcE-KtWnJoJFgp0RMESYINdG9DztXV4HXecX9i6l4ipZbCYZnurFGvJtCBuTb5Z2SdWxPoepUCFChg20zdM66yB9QJRswDEhJc-s8pvcKu8U3CT8LnVkL9Jd7NrtdJz7n7xba-4ic_jJpgUJbSyG1PI43B2BPWVgG3WHiQOpgm4Zj_fLNpKwTLGse1SIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HF657wXDtHB21Mbj-WSyL-pm2lhfg-0i63pc8s5w65Xv6mm5PGRpd5f-mQuHCWx1zKoEjPWPaAxvC547u01QRGw0bIU0epvxXQL0MfJIM87YNVgizU-kuIiHvXvBnOdhX-tvlIX8SVSnPefNcMd0EetZkQSsgZT8L_mZLerEPExO6BdDdy_boY3UaE-bJzkS5XBHLiVL9LQQgZA_3WPADZYWAVe7KM8ppqc5n42Tel3ws7pwzzRIGR4OUDpwK74jq7Csd_BsfegEBG0xu-uTk-EQsHsg0q7uUcu2X-CsWZlzpPZUAUjq3VACuPZfg2axR9akKq_EtSSnCoBEc8vqXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7635">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=JQ74eQyfUwch7VYTlfVm-rMe-HnoC5PEBc6p9dw8vxc8jy9GU6ur7W1UKs3x121U5L9vJFrJbblF8PSCfC9jdfjNnakgRxvqqsxkCJHV1ftBo7IonXvYjgv5wLZZ9o6vBvB1a1CNdO9Il9ReeyMf1twbeSfh2brOc7QyPawHLaWxfykvajkJcVbehSJtMdIIbiUpbVovYgPgvyVYFJPPa9s7lX6xjulqhbrk8jXpkzZMH_NFmNtCR2lDOuk6hzjbb2KpaJXyrqulz-LeF2rhRgaeY2c7ao99mOvrDo9jW6HXMeCMDmnOh-suDO0pk25Hm_alRaNn8Gu_HrWU9JNzAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=JQ74eQyfUwch7VYTlfVm-rMe-HnoC5PEBc6p9dw8vxc8jy9GU6ur7W1UKs3x121U5L9vJFrJbblF8PSCfC9jdfjNnakgRxvqqsxkCJHV1ftBo7IonXvYjgv5wLZZ9o6vBvB1a1CNdO9Il9ReeyMf1twbeSfh2brOc7QyPawHLaWxfykvajkJcVbehSJtMdIIbiUpbVovYgPgvyVYFJPPa9s7lX6xjulqhbrk8jXpkzZMH_NFmNtCR2lDOuk6hzjbb2KpaJXyrqulz-LeF2rhRgaeY2c7ao99mOvrDo9jW6HXMeCMDmnOh-suDO0pk25Hm_alRaNn8Gu_HrWU9JNzAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7631">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4fUUw2jUabDKZapC8ZQS8uqyRS7XZroyPvpo0zgQ5l_gswWlkivAiOqWQ2sPgzk5Bfei0La-tjfCHfWgnB7OGR6ijNOMCttQxNybvvlKkcbJRD6ylCxCao4TT8vwK1r70KwsjN-Cau36UjH4F-qhyLqNd9XojjvffTJsw4-KvtgeJB_o8ciOvtgXVeD5VNM_Br_E6iFj3ZXCqBAOhnTQbEGejqlLPekODEImRovXan70JzF-ELo0QOYRrNIFhFmK6dWoksHkkV1nZ6hoJKLQ4NF3H6DHOT9u3cFcwrZ3Hj7MMJEaN004B3cdO-0a-aGPHD_sDvqVSocH7c2brPXZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=oBgo2iQLuoI9QwsUZmHWQ4NdFVxjWpV6PCu_FfIsjpGKTcO-Xw2TCmOQ3GXln2F0QCCgFDeE_X8t2VEwo45x5l4nTF_TW2sjia9DSb24yGmTJSp1gItqVLzIv3tzNQAyzQOVCpjJ5WPxvCHhll6I1CLGKLhUD21Ka_6KlR58pK2rEwUMoo9G3BQsTpoLfddZhAsiuLj9DhHpsb0dxNBf4gi2KQ9x_-Vfi0zPrx8ANzrCziXbzT_496qrkulnmesMwoZQ7Nf3xAcscsFX5CZQFYM4gtryi0xLppT5XONQT_1wkJj756AVgKa6kKTHbOj6zcZO-swf5bniMYCDSdtHXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=oBgo2iQLuoI9QwsUZmHWQ4NdFVxjWpV6PCu_FfIsjpGKTcO-Xw2TCmOQ3GXln2F0QCCgFDeE_X8t2VEwo45x5l4nTF_TW2sjia9DSb24yGmTJSp1gItqVLzIv3tzNQAyzQOVCpjJ5WPxvCHhll6I1CLGKLhUD21Ka_6KlR58pK2rEwUMoo9G3BQsTpoLfddZhAsiuLj9DhHpsb0dxNBf4gi2KQ9x_-Vfi0zPrx8ANzrCziXbzT_496qrkulnmesMwoZQ7Nf3xAcscsFX5CZQFYM4gtryi0xLppT5XONQT_1wkJj756AVgKa6kKTHbOj6zcZO-swf5bniMYCDSdtHXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Olz2RLRB3EbKh02Jzh1Fwrw9RFxSmA2cp3aXPrpiLZnIKYtSjVaonqXSuXNyDSKYeeZN-0bFy3IM5kqFrUY9tzDSwYtb991yYNYgNr3KpfFV8n3iXvstYqo1Bf1IcqK-B-TvIhsIy-z2lyB_JmtQ-I6njpVoXthxjlo0v5LDpQqoLMT-iLWMPYD9oWD1Orbbid3kIyx1ZVxUweTLvZvsFr94llj7SCO6Tcr6TpYs8c7_MBdecqrA5hzGsrjhADfzONOMXp5LJfdfTUCirEjkNkdkERq1taE17EUjTb8OtaZpux9F1q6grjMfUv-mFAcLq0pTXgXZDUerpD4qPu3s2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7620">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2hOTTJd49xMV3pkc8xi4YthsPj8mozYW4Jb55LL51XgKNYiVLNBm7XtT78-hQG_482Vwd3nwBrz1Qv5DJjrLKdA8bnj-j95q1MWbsNcHkxFPEXDZUH290F5Nkb9zpYS62Q_mUS_A1QCvJLUEFR3p_72Gj5kbr0ooh8ClMDu8IZTaLAcwyG0kU8d6F8wDWWDc0Illd3XZXOu6Su_YI2rqmwhtUIDhhJAQLNeTVjoGbOQzf3NSHBNNI-UgpHZc_89AFV3JbBFDpMsIZUfM9_RJ77yroDyh1jJV3Z7qeLy1pO6b-J-TOEGuKFJkdNe0ulra6EGpw9HnEKPDbP165Y8lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5.1 2 days Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=claude-fable-5.1-high
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Um6Zi0cTFTbFnslgvXwViKgtkuFTPUvJGgbSs29xCxZPrNliawTkCwI88Goa48HhEN_tTaXLodUvjPwF05BwMV5ZFzQfAw6_IWpbxYeuY75jSuJ2JMx-uyYB-YfsHKA8PfGl0gdxfOY8yTgeLYN5Ct9PuBfJT7UA7ydHK-EWAwJklHnCymmVSg7aqbrWJIBg2LvZnCSXHHOoCnM1wlPKhKEnau_7itn46FyDOetxAlBFw7aMvVAgGNA3wGyqEmZMmf2JywEvGHd9E6zTXNN_KW4FlleulZnXqDLr1KtZ4U6FHB7HLK4iqgsjducPJAxg_P31Kf2x1UuuuUk5K89tTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7614" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7613">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7xnQqznGeMlm93qBXsDMPTjwn21b6kQXO59vGtcsVRMFmNH8FXjB3AyHbbCA2eKwntPYLORXV3xbSHCPc2eQUgaYXFHCecwHaGGkh5yYR1QmMYggfrCFzGon2_4II_uzEnm-Z2ZrPt1CvAlgl8Y34Etx2bfik4Q3lRoFhAeS8aAo3jZJDbCGmajBOeUGGM40Bfy9QGp_i5lxGxsijAsvPah4O-ndWpy8N49Gt-CEuYYq0MwwFEFyWw7S-dPE1sJqEMdJJngWTla0a2_G0l4pM8piVpxn_tb5g4RkSAcgauMJkQE8zSLtp6rO5pDYqF94qj_2HEeC7I9RqtXC_vjbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7611">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7611" target="_blank">📅 14:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7610">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObbJTujCVT57Ja1E-Rlc4bUr3M783TIrJHk5jIPkwNvUnum1Wa5UqLFWnAeoYGZlGg0R3BAtLfav1StGbKPC5-fVudcB34p5GtCYEwoLRnNhib3pUHe4tRUCcT23QnFLVmBO6IEtbVyzIIyMMK4PzB8T0pCFaOLjnbL-FuYsXUwfN3g3genKgWDMUf1H7Tg2I_vHzGu10it4T1NxGw8kY_phUNOKNQzGSWGuem7u_Of0DxXHQj_ysPi2FU6LQ__t5OeoajnQ_Hc7qv9jKvKCwT65v-X8OAdPvzN186YK0oaYdL_2tnEu5gFX4QfmN1tnorDkD0hkOl9Z2qWL7jD4Lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7609">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t75FSNH2VAf6tOHdGsHPTnXPIhj0NR0BVHd1f7-NVLNEPcrueWegx8y9CgtHubNJ5VSffWFzxNWdPVn9sqmXDIWMsAf62UlH9HOTesnPXf6d65KD3zn8EMa-tBmCdgbBn-F2EXt7bEaI8xKniD0t4VTn12LoRXpy4OO9B-QmvbdYOS9jP9A8xYz_uv5yw4PGqN5gQDSNYX0ZFs32A3NM2UHnAT7ecR9D-iwAOX_Br-uFt_jhsFZnc9Dyu9djaGiRpsLKaAy5pXAqAUIeq-ftVaW99o6Bv3F7gR_6cfEIx4v3w-kkd3aSgVZ63dPcSq0NDRzoiTLQKR-K4IX6YOL_xA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7604">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zc5yeYwN7DSUxmYSmJbLWrWdH_2y3Up_g5Pa2Sa-J9G7oE3L2_y0Yr21reJuP-1uQu-n5nUyJW9gtxrzwrezBsm_2tpFmuTrYlDPSamBbz80WccHTm5AJ-I8Pd5ZZeF20GyIulYmKMP0kgW4gj5nBJ1HYHshgkawG4T2uOlekSaThjOtUssHIMNr7CQTtMbDGWNbrrQOIPmObZ8ABc4SWOUSyEuJQNQYhISDufmdtpq_hgAQMkdqGke6esT-nNlJTMZteuvBVYBUnwH_LgwPVoDkFzDDWS8bVnBCXDXg_eOz1B4mhn9SFTkJ5fU7RGy5FFofV_BYuxENCDd-RnH7Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5wwxc3wySVFMNh_KlrfE19hSllGV6xUYk4tD8mLzZEgmEZthAfH0Dkq7bTih74FHu9Ky2jx2i11_V1ie7gDjPEJoUq7gn0auNfIB7zhQ64pNY2bQpuIcJ0FQQT6GZ91DSLW85yZGpOR_76d3yEU4Fvv8GMUX9bq4DX3AM1KRy70lOSd-NAJhyZxeDMXAXlqVaB9jEbjOUtTgsSx9sD4au0VfCkH0dzOdhuekApERZe-NvScjHRieM6zFmv_ynduH-46x1xF98eVXATR10593wgcjGzEnZ8p5WRoFiLqxdETbyMYGctddRZrg_3FLxTEvfXjYgtdnL3BkVy-QvQVkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1x9hL4tmaTVh9WueZx4vBnn0J-IVzHpsR-J6JFGTlbQh2N0ccXcPkknsVx0VjVV_UOgDg7BkG7HsHiBsU4fEYZYTnHqEIbxC7rhpFg9mhDwv2ptMfRJ8efDBfDx8Gdua_e5nuEUaE-dvW9o2PWaztYoAQp1cfoS6IiUpS1Mv_TMVyrnhqXxyy5mI4QNnBb0TFz-nXPAxRER0cLVLTXgJu69_6OeEpOm94EL1S4dLj_fLO4y236OYMltrGPv5FagrA9EbI-6XOhDG6oFB4rBqc55LpxfPt8iVqOC4J2y4tWBvTIz_wlrsMhidRy4oBPhqxX0xd1pA6QB-Jijwnu6Wg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4UVY6aCyjkwjcbfKBKnsgAKuP4qQmYAoLzOlNq4m57BLWOxBRVrkQiUFFm7YjrSmNHnEA1jkaunEU71oFBj23G7vPh6NXgqGx5TnV-virkzf6eTJ4i6DDNi20oFO6aCh_eyGaIEcjdGNuvUke5IfdtnaKvQpoVr346iptaUgLyd4OM0zrv2Koj6hoC2FobIWer8WkZbB0Nk-z5mVUHI8tfgcB9RNEKGg-d9Yrm96kd2WSeUZjtHI4EHQreFUy4ppukfpySd-aiZhcyNReGsOfaEo50bUj5AHdmMh8vchK4yEbVuHb1nqwiIMfb2Er1U3c9hrOBv16kTziVWwG3JAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLrqS7RcWrgJL_qbFCAE8ogKv_LslTeAnH_bboDZ6kf2jfaxi1hJfeMR3F4nbBoPEiB2eEYvp0Nb01Y8-foBnje55NVrph608tYTO5m3WZgk0WZJ9rbmNKcZmyaGKO6kP15xx3tPdIp_lb6UJ1K8LiOFjjpk-tTX06ak4g47fbxuAO97934U3jeuyUADC1fWDg3gz9PdGs70DWZQ2KRzdrXUg_9O-UOBUiKnXOh7XAqx3wFxXjl4igqlJ65mn0RRhCCKgQ_dVDliPamFWzvjMXmbRGN3WV280-UplcmzfL2nCvWX8s7uPzgwKO3bwpkV0meK2Oy6Ob0HOFMQVHtYRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRbmfV4Mb8Y2Q9ywHksisbht2K7lUt8AUd4eAaRJF_5FaFOr4yVwJUHUwDXUi9qv_rJ51u_HpzpbKRkXNnczLpeMUVQ0l7__HH5uRrbo_NZne90l6tbidGD6cRV0ymmp29Z6zrK8pLqxhc-bFv9cFwFFZ_E8dtCEZAGQ1siJgDAswsEc96zhKzryEGG04Cs5MciqbN7sxj47r6NzrQBrisyEtJC7_PBLGB7Gk-xplNYt1_vFsPP4uIA4NFY0qzcNieggRkvrVeul9BvRZN-oLB3gF1axUPiiOTf1KplII-yZI3m-GaWbRGszFtXfm9iLItAmamOigs9dZ9J0a-8P7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLZaReGujXvpf5NhrENkr5kCic2KwwYAoMzbfsp3Xdiyi4GHGSOIIKwoYRG-bEe2E-lcgZjcAz90yViy_YW3--xcKdrpm4ddM-K59FL5aGI_j5CRZQ4IQxxFECHbxkPp2iZCL4GA6dqZMmjH0LQ6nOUwaeQlyPSTFuVtY7jxi0jtHpyCdqfanzbtsJNmOwuC-prQlqAydINZZydxErDbuWDemRxj8jCjT0lHJ7vYtPMCzRT7KTbYFnp8cp82FO_rv2ZJ4LARQDNfI0pCidqy9r9pMyHL_erhjlGRjXwx0QtAnQJ32DaoHB5qk79dl2ILDZYStx6Y9BBi9FT3v8Zh4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAr5uvrDi6eKGtS0gZFUIODsXz4YIm67ZatGC2qQDzy1oTvBb8m00yEFe3yGpxEyekiUVE564yzwYvqXUIYrBar2P84njwLNf4pSZKslEByEmLdg1rluv7NoSxIKRu1KoTkdNwAnaxykaZAOq_oHxl5OR0HoFtY4io5U41Qz3WCb-g8H3huArdS9BxXZr4l0grp1K3PVTRMyZJqOL1i7iqsrIwRVSEbHQpqlP1Kk-lMjl819WQ4X_1g_NkLbOnTekkxRTL1ewz0AJTE-p2KlTv-3f8lfloHb_YonwR4Hz0Cm41kvoCUsbN8fspJQHqkVeu3IW5q81Z-qBTQ3GF-U0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDYWLFP5g9Bq-kcWmSK5i6Yy1b0IWKrxMD5Sfsvh2fXfq7g2XdMyBkpUdRACw58xEexqE-GiEEKjUkWh1L9Uzhn7uYV-U639I43KuJU7IR3JIz8mnAIJDUZAf-D0_CrDjUvlAQF3R1x_y4cp16lItiR3MsomD8jK4_7Lki6K8VNCXLIl8Vmpm_IDamG3jrsPu8PjrrSf7A7pBBitUQFeUhRFA1rZQg4-YPwqYytCX5NraSu4J6pOLVOKhiXtbvFSExIeSvdCD9LSTbuKJUOFFJNuXZ0c5_pF-SifjBQQiWi60OcaByL7H2LFwqo0szttLZNNi5uWmi6siusTjd2zVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjle_3fSk07of9yZA6t1ueQMU49i8FLZKmdSUm4uc1GS0edkyHBSDqLdMhW31lX57qkT7D9LocsSCiQ9GiF-0th9HvA_DKwpBKGgEFq1Du76gSmCWlHTYtSBTcIuBrl7cbKDi_I9aY2JxPfV1CFYsZneRJ-qV-J3DUDZxDVH6IsWKfUyccl7Wd3fkd1JrgkHqXhXslAqABy4ha26KBJGltij5fX-t48S8vWH0d1mwk6yLL3Zz-zgArGtfT9Y8jbwjblNjBVEUho-uWDucxW6Wba2dP7u9iTm_omKOf6ckzVU6wap70ZoQEKXQ0POKwVBJiHOnDAgApDtsjh_tfqNHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dku_MOBsgDxEfvbJTm-MzYQRH0OkxNjiWhIEPd9v9uBTLGgej9-HwnSyWg_e_QZLTxE1_9Irzd3KpQny3GGbDXdRNcc9pjbwRJo9qh8ikcodf6OcpMLNh-Wcl09WLp90d4-UdLBkY0kDHoCFWPdYFm7bCLHcD1xGtPMQqTFTZMz32wVo63N5y46jxaXGjuXyHzOoFOjvBeLOAyb-OvbDoZjYgy3fmoM7jSXF0hiDMdNLu7cmQoJnxF39zf_iT4yKTDgs2Cgvchbx6IQFCOlNPfjrhcfQ0mPavpMkKDNz5-gGicPYednGzKdW2kvCnPTMcAcYZ6LAbI19F5P-JdVhcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=HfT1I5amQHeURTOB24TJQqAANEEVu25wzzZ7ZcPvkp0vXo7A3rQsMw9GEuI6Qo8VZdAsOCPZ-ZXvhZiwzJnoAAeNkPSOnVao3BxYEjbJcqb6WU2cHWLYjHG6h64eGLhs5WeBVhYdYfjxcuGqBVAiU4yG2_0qFwUdP6uZx1EY6ovcS_yrYWsnO4e-UCObxM7x2ImqJRj_6xkAOHRLMMPnBnR1vE6vp6uuLkPOykStVJHcE4GJgMEXoRUqLu2qtppSMUIWbwo-vSMlTla1k_zhvbwJc5FBSCjR2r7p1WCKcKnIzO8ZL0bqZW1Vv8BJQ61EIdTQqyykOpjiyPFREPOJmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=HfT1I5amQHeURTOB24TJQqAANEEVu25wzzZ7ZcPvkp0vXo7A3rQsMw9GEuI6Qo8VZdAsOCPZ-ZXvhZiwzJnoAAeNkPSOnVao3BxYEjbJcqb6WU2cHWLYjHG6h64eGLhs5WeBVhYdYfjxcuGqBVAiU4yG2_0qFwUdP6uZx1EY6ovcS_yrYWsnO4e-UCObxM7x2ImqJRj_6xkAOHRLMMPnBnR1vE6vp6uuLkPOykStVJHcE4GJgMEXoRUqLu2qtppSMUIWbwo-vSMlTla1k_zhvbwJc5FBSCjR2r7p1WCKcKnIzO8ZL0bqZW1Vv8BJQ61EIdTQqyykOpjiyPFREPOJmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHPMifiVoHaXUq2He3V2yIgQpudQDeuolAo_1A3XjqCMGeCGHnUzWynoLoBpTDtJG1vWUcH35aVdy4F9Q8lQqmOnoes7V5n_9bOjQqzw-jaS7u59-uTH1ibWi1ZeVf1DAzevxrUUf9yPbvXkX3zdzSPf55lUZxNgO8Jqck6K2E2XHSHu4En5rNCBYWFsgTCPsXidVaWcCKudo307K2W1ErQUUVY9HSxwUaRG5Dq7xs5rzKMcuZk2xGpHSX0xY-madLSXFoue3fGUE_xvwcCs_bUpUoekBgHdU67pvpZWBpfnmFnFEnnuj6k-JuFdanrM9OGXJNG5FqN0DgaQ0f8g9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=hd7j5eCFQTRci7BhcqcaGooJ0KRQDh0c5d4QU3Jc1O3IGd2-nBCVSPM4hProQjnYDRq_CM60pD__9KxhQQRZBol4irD0Dj_H1gWQ7YIgNbyK-rekju9HwgsPgAahrSJnsedfQKSpwFPQT7VtXSHKll8dSQ1JkqeZyMeKVNo1LENb1t8MLV6Uz92E5kwOJyVetRfxUq2IFnNT1Wvw9AJPzSZjy170H3DoToaEhS6sIwlambcwQBxSG_j0SBy-LM22r_ETOs_jONg_1qq3IyUi4Zq3DyqJFP2PItOFsBVAEvYcg6jA3E-f5wpNshRnOJgcJ2QOzBwUBg8tsMLzpIPqvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=hd7j5eCFQTRci7BhcqcaGooJ0KRQDh0c5d4QU3Jc1O3IGd2-nBCVSPM4hProQjnYDRq_CM60pD__9KxhQQRZBol4irD0Dj_H1gWQ7YIgNbyK-rekju9HwgsPgAahrSJnsedfQKSpwFPQT7VtXSHKll8dSQ1JkqeZyMeKVNo1LENb1t8MLV6Uz92E5kwOJyVetRfxUq2IFnNT1Wvw9AJPzSZjy170H3DoToaEhS6sIwlambcwQBxSG_j0SBy-LM22r_ETOs_jONg_1qq3IyUi4Zq3DyqJFP2PItOFsBVAEvYcg6jA3E-f5wpNshRnOJgcJ2QOzBwUBg8tsMLzpIPqvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Exz43hsjNTq5zKm1FI4hQiliau_EDuTE6ODcHGMeRpopHQ3Zm530Hhv-NhNY-aR-3jH7L1U10gWcQx4CegmmYS58kIwL2NM6qpp5AprPI6mx5RZBOeD2KmzHq0RwuO_pVT9P3lBj9F5k36JqjiMYLHgvNzjiXQ-k18WI2aoVe47iqH20SH6gRhRHE4VBJtBMWBsWemIO8ejZ0nybl3UnItXG__2yJc33165RyLTtfRa3TBGJfhaUT3-DA4pAwTOLIWs-9m8p_MS2lBnWwvQzK6JJPn81HLFETL4w99ToICuhvGLU94ROhLDZYv2RlgdIceRD7NDyrqB8WGxvnRdpjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFffKD9cUYzyFwdN9dbkKu4fdIPPgA1UKy8L1P0FZC4LvCwV3LLlXkeVL8pgmJpgdBV0w9_oXP7Cj13Upq-H4NUzxBEcHMa1cQafxKNWKlghEaSD_tXdHKMc6d_j-Te5JnHYgLbNfLDHa_EEabj0fF_ufCQdd93bAR8G0m3wqySoj7PUiW_Vw2EHV09ofixA1j4AsthtB-h6KT3GYRB0ufN16vUiwp_qRz7vTsCO8IcWh3alG54Q84e_U7B3rX7dp954837vC04YvmEcRUitIl78DTQcoqgC6UWNcr89hvfJDGtaTD3jSDm6ca6b6DdKSHSoOCpBJU12zk7v4yp-EQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CThIx4iOQT4REr6XTWVFMtxPM5XOcmnBaA0F60_qY4yPSfNl9AsJ5_w37kAz8SWeaUmagq9TS_2df5Kdj62fXo8mUaI8DsrlG1i7Ua-5H1jU81OSu4RdfIHHhOoqiwLQBgYEgfojF3QyIQPb0qIfqamkaIAYPj0KbAyDqiYBUonIcxRTItQWEY0x5xtInvYe7VJRqupX8gUOVdeC0JrDPk_tadAVygnxJoqmYHeDHVDMw_zcGpxA2czBKS2NhWrvBqpALlE1yhzkNs0v6KuG4UUCBOiV_lYJ1hGVwG4mXpFJQ6kjkHx8MVZ73qQ0mXPYbkxOzaEwEAG8KLsJgPc2DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fd310T84fHM1xQyDyx1ITIyylb60S2KNCIaPZy_tU3C5Sg8oDETbi_43eHrJfBu9MaQXiMcjyf-4DN-qmdMnKanGkfMlOpL1trOhk1xSqVSHZCY9QZglywkS2eRpKu3RTk2DQiKPZqkwWQlupycfA2gwUTjz9RX4sEzSic2lCH7ZKucBXfblOrrnRgJrGUt-yJSo91RlY9ZI6EJPkXIlJ33z4n0q3VGXSwNMKAsU4RxpCGokmr1rz6RHQyLwh8jYw-zEIzr6Wj8uSurlvWXIG8SPLvrd3Q_0zfc7kulF7h95WHlw5FETRvS5OIu0hhMHE1aDDhpVPttc8GdHggtcIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S6CMBnLKHkpI9dcaBmyIl58ZVVPFtPGrpJ2UPiWydDYhOGrwLjPKJRvUYiqB6IU5xmT4KWvXA5ooAz9K4e01g0ttYtCnW5LEgQORDBrivDrXkUxAai7HOWtsTndR8j7vio4XrjIntY83MxpD82HFcmE5R98urErkliLY2x4Lnc_Rb_BMN1yBuSvD8yUZyPtOVicpqkYnZ3Q3e-1tr2-B74RawJ9TJkCWcr9I42_lMqFnT1sKN9oe6abW6-ZC-VlHvmr3KZnC-77EyHQP6mkhk5z9tVCe5IERq9ZkcSwnDHE8pV81XgHW_WUvZU5RmM9IsXbSYth_Va-RKSogEXZwuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PIu2k5FtWnajRVZiVVJ4u-feX74nr_ue2kXQmS0yNqJCyySqawuK-WbSQP7eQtrgDJipx8XRSUzmJpO9-YwASanqiv3myeTNw7cVll4o5RaiH7JfLM0qAy3T_xnb79pzT1AtCgDRqvXToOYP_geUQW8qLA2NJOcQ7ygag2UspL7Dvz_xncQ732WLPrb0k0LSskAOd-6kj6WgRSG28ccmHhba4Ne3YAWZ7YclxMu_xYh1ykJFFOUuc8C9TO3E4iO5QSmG9LasRmRVM5rxg0Ymqh8VGThHMO5F6m0wU3Q76tqDrNXdw1FuBJB7Z7xQQLldk59298wIbUJx9qQM0dWtyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bcthw2Eu32-TD9MnWYAAwUjW1kdPBczVkNx-A6rAuVFdKYDTXFvfCDJCy6EK88fOsMVA8Knw6v1TVuWNM-gEvzkKurf_Bagb56bnJoFDtt7pAcWzIRRFobO390-4ZUyH3Q-pyccuPCRP8t2OwMGLQ_Fc2rJzbCyjaDaOLQZaaUofd54nsMgRD6pF9PmZqVKO-teV3wIviM15eY3lDNg4paW3C0Qvn0u85FijswDXBU7kSpyPJZ7-7zyBT4EA9IX4XbMjK2ZFx1eCMhp7DZucYxRgqZiKq-tsr-uFQD8QMgYZiG-Jb6Nkk6cxwtfAIfSfB4RfI6uRGQN04y9SNMPHBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBkfGt94HT22myeD0F0SyB8UjAAchzFlzR-h3KBD7loQBL4gJIkvRQKHCMEcqIp6MWphTjhY-mZMFLSf699sP9jCT6FenFCfMD0osKbxwT6nhNLt0aHyTlOxMXUKXuhT1ITS-tCH6IzFyEZyjIxufbP9yYFUsa02jpvp2Pm_f8ta2GvjiMedjogvI6V4jf2q0n_LFdDXsXpQ0CzE7df080_U7QqqO000hdFYnEBtVNN-xpdxadoAgoSzxIFIhxi1Ron9pKInwFdNXfnjhrspwFRm280bAKjhVPvudw2dUTp2itb4Qdd7tPiURSh94ZDlkfFdDzF02UwYCCpTvvYyIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoacIiL4Tu3NDm7GTR5Od6xKNu196EKBeymEFMWX5BtkV3kTl7m6JoOiSlytRA5wsxOZ7glk1rOIbSf97-h3qZzqhotoVgUPlndb6tBxhCfuuOWgRfNJKR_PrehD15cwwWJUHyK-cEfAyuev-k09FW5EAms8F6P79dN4hVlCqyuox9qfJ6q4HZTEvSW7GiiQbnAT-U3-JXbiO43mQPOWsgetU8-zDR0DGcmRV_KCCKyZ3333PouoO96nfvXogF3l_Yfdb8SUsHYSrBwViPu1VuFozSxlixLM8M9Vj18-Hw-VTabOjwyL408HkPCHf75uuEVHfhxFD3pBhtfeNY9y4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsdQVi97C9cAnmmbJ0S44lt0QeSA9Ji6Ryt8CVkG1E2XmEO1TE3QVXHYuBkSeTnD1DxxZ75ncE-2B91npMLC8jRDrHm13Y5Y9vwVe-Dx19OFUjdmOG1ypdMLWX3KLWqI_afyJ2fsEqQ96U3uR5_6suLfMSfoopTqiOmCe4WW2DSOKRc7fWPZuN4hJSZTZPdipBxBAOZrMrRrC8ZsRbgJoGr5QW4-z9TxsmJgUMZFiJXtexqUGuNGJtHpKWq5dGDa8wk9P_k9nrscyJM_Y5F2WMsmb2xwBUoFrz66O1VCswue46hSenuYv0YgqvZUfL4w8_rNmMGsaCZW-21fVtdk7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsSqQXv0ZruBdhLVtKSDm2sWKtFQgvBZFzX_OFsYwiexfhCqDUFFm_xxo6xRlimqvO9ZtspE6XweAR4pkJchTzG_Xv_vL24E4LPJ6x249gTRr4uztVK9ec-R8OT8ysQnX9Er8fi9ErtqAR2unFjBOpGebhmaXyEp3qG6Qz4Qoo5Jvz8O2x-oom8lDR-PYrpCQZYN4h9kcHrIMIJe-qsA5dnWTc0YGZYdUKULuQGxNpCr5tjwZKR_89zBpZKUTmRYBnQ-9zoBQlgeHCoYYWS6YsoAWfWrPJkbxKNRrz3yoVkXXS9GEeoQb8ix7yw5ysBz9pYnpDlTwSgLHDvjHdZfWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bk2-Q9wIGSftTq_9b60GXNF71H1yJ3dQyxKqP38aRR_SPhU84yGS20vtxuUfr8SxJKzluP5h1mHEic7UJZ8CeQQj2PA5vrrizBSHcm7oG54W1LKSWJpo0iSFlT6xXOHZJ0cBb52obVG8Pjten34z54mUFP9yhMclmwylbUvMn_82jUuc-SJ-1K73L7okJM-KXIo8NJslovv1ICRliaOuMzV8rGl33WnN0FIlrckK-Bcl0fjIqHP15aLRMtiY8HgprI9avsBSHHRsmhxtKFuOidCDuVMnKri43ArB5BUH7q2XDqXKb-7wLAdlO87sZNEIN4bGD-tXdq42yXDVekaxVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrNpzrbk3vmgky909gjaVfav3P9nl-Z6dEAn0ACtoahbqjIWcBaXvayCxeMnrgwOvsLWzk1KcOSV9aaHBqi77cin36Z4k3-cYbQ9f_P1Ji9z96IpKSEgSFb-pdODNG3eD4giO3nAsF2ZgoZTROAucf3pYy1GE4LrbjJ93L-dGu83EbtmFTCwuemAdTg8UJ7br3Myoy4NLQYM7Jg1FRvqhuc2nC-cLs6Bv15djPI9m9XyLfKZOe5rNOdnlOWHrqFeu-hVukg38Kedt9scUMcyKC-Baypc2X_VxZNU4KP3TnML5tv-kYF2DuIkYZqQCG7gMprLbJ2WiD3I3DHBcV5x7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=bRDAjN6Ep1xuF3w_OXUDvi95oEyDD5D5BRAkgKNdSaIXQqvYsoFkII4TZaJeyuzP3alVY096OZWST8xf1MQ0OiPZzPNvpr2lPwctakpYTnZhWVD-NmpJTaJvgJGr_h7AyigVawLHKcqGNyLP5Fg-csb7_Kg7vgrcDEIvzTbltsatGNpkIwex6ENuyhKbjHhaJpmr9pDnI1Eo6UcfLf72btfbL74X13LPbxjalP8VcJEwqpZBdpgCHkIz5fYekVZgRZs1mjgShEhxNjyk2mrwgc_XoJst_jZK7MlCDPBgepUyKGlCk0gXM7gTddyLrCNMwqlXZhJqNijY-WOsjjpiCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=bRDAjN6Ep1xuF3w_OXUDvi95oEyDD5D5BRAkgKNdSaIXQqvYsoFkII4TZaJeyuzP3alVY096OZWST8xf1MQ0OiPZzPNvpr2lPwctakpYTnZhWVD-NmpJTaJvgJGr_h7AyigVawLHKcqGNyLP5Fg-csb7_Kg7vgrcDEIvzTbltsatGNpkIwex6ENuyhKbjHhaJpmr9pDnI1Eo6UcfLf72btfbL74X13LPbxjalP8VcJEwqpZBdpgCHkIz5fYekVZgRZs1mjgShEhxNjyk2mrwgc_XoJst_jZK7MlCDPBgepUyKGlCk0gXM7gTddyLrCNMwqlXZhJqNijY-WOsjjpiCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=sWMpw_oymL6FxTFVTfUrTnQPFNo80RUqQCC-Lh5to41AMM3wL2dT4hGAv1FDCZopjYrKb35iMBTXxU-Otd33BajLBKNcuPEx0PrgiQHdFoej3SSPRtVIRfli7hbt5Z309cMRNPjdcZnGTtXfiZTK16lItRhHEBF4kj81zTD18sLoEdMZrX6yPKXFg3sJWj8bzKy-IREqt9TZqy98Hk6TFUiXJfhXWipJ4QvM0VIdtm76_7eFArKpClz5iMp4GDEDrXu56Gn0WWw3yb6Lc2aBCS4Gy2AbNz79OX3DX8TluMeY2hNQCUnWMVVnQocqepdeSR5MZEkmh40E_MErwPttXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=sWMpw_oymL6FxTFVTfUrTnQPFNo80RUqQCC-Lh5to41AMM3wL2dT4hGAv1FDCZopjYrKb35iMBTXxU-Otd33BajLBKNcuPEx0PrgiQHdFoej3SSPRtVIRfli7hbt5Z309cMRNPjdcZnGTtXfiZTK16lItRhHEBF4kj81zTD18sLoEdMZrX6yPKXFg3sJWj8bzKy-IREqt9TZqy98Hk6TFUiXJfhXWipJ4QvM0VIdtm76_7eFArKpClz5iMp4GDEDrXu56Gn0WWw3yb6Lc2aBCS4Gy2AbNz79OX3DX8TluMeY2hNQCUnWMVVnQocqepdeSR5MZEkmh40E_MErwPttXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJuWYp1kHyHQQpCA7oa5vwXLeWzemEEgX_L_G3OhbiCJ-RyemiraJZFJe68dbJlvoJvBTt15EMg-Jbcjf1y1P5jy0YfyTX-7_p6ztH9D1c5uSr0jY7uNp4CuzQs83Tn0ucDDcw6p3xwb78P7KJuzyG3swhuZucwGqxAcScJ1yoAMkeS2vXHSb-9GRrpl10yv0iJFrFxAWEkmQzVNcXollYooprbJ1CWuAQxD-1ooXepaDv0i20elp-EgOS6e040xmniJoCOjhFFu5eJ_VU7TYQtCVr9XqzksjyOGnRTVQ43KBmF383O3NMnUvkNqc4h9XK0M2Z9LY2ChsVtnDasuuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzkI4grdhLrer2RYdWnGY3xeK04xnGnXowtE1TI4yy0S3gYYGVpPTvWGMd5ik-gY09vSrFsITweV6Yitp8yLSKM4arR9K-vFf7yM3oBdX4N7AvtI0ZapV8_GXmiKZJGWo4prs5c5wat3RjfqjORyCyra2v7FsgqXi7iU12LbyETTfl0SH6148LnYcUnNmdnkYM9BiWlur8hvmndK557f-NkF8xup8ICPfoCLQtxBXBbby99YLIIaLTC2zqUzpw55x8vj6hgdnVc3SLkaDNxFI_VG9tJc4oS-KdI-zrg5G_5wI8-M4MKh2TpeptmJzy5TzatfYgeEdv0d4tEJtFqlig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u87aSGrjWM_sicmxArM6xly6oBoX2teaIRxeu_1HVs-hTKdU_j-uR-tqN30-o8wh5FpnFey8Ej3jbpymqwKiN4d8loo9Wz_hyzlm7k6eq6k9u20OJ77_TI_pr9P896-_rFr-I4ZwP816rmgoB4Ft3wXHp-nHQGrxkFblY4OJIKpreej5ALTpcp5Bto1sF5wXHtLxiJHFQm7i59TljDHj16T7bWDiJ1HjZFGDyTpFlvX5jVG8EwCTOKtkxnq6qh7_Vn5XU_wo4iCdCKEk8h7gGyjavflab_MLDorHQfUUmBG8cu7Ss1KovnOH4dIlkpEsGR_qcV6blaybOsc4LDA-UQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

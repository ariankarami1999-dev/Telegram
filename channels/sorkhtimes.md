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
<img src="https://cdn4.telesco.pe/file/R4cG55bvEK71P-oQekMq-zdWofyGSkDZdo3LGi83uw7ajDCbh0GkWCAP5t5SR4yNwVL9dv59w3epXLOpwvXDAjiI3f-n7wKC05_a7LN76KmKeiAbH4bALT2GIIXcE5HLfSEeuIbOY2cAEtrTjq4u0E-701v7Yi1fqv9ENin8LJVmsdQKROFf4q9pJAYZ_8TD4yBAZbzv13wD7kqQGIXiafRcCDtMy1NoxuTFOpfM_5bV-m0yaAkLVMCGC8k7C7QRCLvT4WOxmjdPo6xYnpgrMs-S59s1Qu-5C8gFjF06TJqNi8fZJTpYGe-HLSmTbPo7lIwX2oADQg44VW-VFJnJcA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.7K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 05:59:39</div>
<hr>

<div class="tg-post" id="msg-132403">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAU23BU1T1paPqS5gz396QtAWU2fQ2QeSYVxeNwFYp0LSTyDlc8_oqA94DEGunkfDP-TgiJo5TQmy2608MCOL13dT6pwpnfwiIJhKKmqEPa7M12P7sxP4tJlROK7bnHEwmWnp3A9RihfJvRD3zKMXg2MzyXJQrrZSKINyYjadfXGngEzyB-nyBOJH3vFXNZVaWzm08R588dMm6Ttk8v2caV4yOmYgZqV7Ozi_KLmmgE6YONMz3Xfk9KpHwOUFp94yF3jjqWLReAmWsSeXjfgbt_79fE43DxZIwt2oWGXHF2Amdsxg8_EW8AqqmhrtOenFYJCwu0Wsc_jfFmHT0U0cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🤐
دیدار ششم از فینال کنفرانس غرب رو بین دوتیم سن‌آنتونیو اسپرز
📀
و اوکلاهاما تاندر
🆗
رو در سایت اسپورت نود با آپشن‌های متنوع پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/132403" target="_blank">📅 01:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132402">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
خودمون رو گول نزنیم ، بازیکن خارجی با کیفیت نمیاد تو کشوری بازی کنه که ۴۰ روز جنگ رو پشت سر گذاشته و هنوز هم هر لحظه امکان متلاشی شدن آتش بس و آغاز مجدد جنگ در اون وجود داره
🔺
اما آیا این اتفاق و این جنگ باید بهانه ای برای انجام نقل و انتقالات ضعیف برای ما باشه؟ نه به هیچ وجه ، جنگ پیش اومده ، پنجره بسته استقلال و مشکلات مالی سپاهان  باید باعث شه که ما به سراغ بازیکنان جوون و تراز اول داخلی بریم
🔺
امثال دانیال ایری ، مسعود محبی ، فرهان جعفری ، مهدی گودرزی ، پوریا شهرآبادی ، بهرام گودرزی ، پوریا لطیفی فر ، کسری طاهری ، جوون های سپاهان مثل لیموچی و حزباوی و کلی تلنت دیگه تو بازار داخلی وجود داره
🔺
حتی لژیونر هایی مثل محمد مهدی زارع و امثال الهیار صیادمنش که جام جهانی رو از دست دادن و نمیخوان جام ملت ها رو از دست بدن هم میتونن جزو گزینه های باشگاه باشن
🔺
این پنجره بهترین فرصت برای پوست اندازی و جذب بازیکنان جوون و تلنت لیگ هست چون رقبای متمولی مثل سپاهان و استقلال در بازار حضور ندارند و پرسپولیس و بانک شهر در جنگ ۴۰ روزه دچار مشکل مالی نشدند و اکنون وقت خودنمایی پرسپولیس در پنجره نقل و انتقالاتی است تا سال بعد با شایستگی و بدون حرف و‌ حدیث به قهرمانی برسیم و به لیگ نخبگان بریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/SorkhTimes/132402" target="_blank">📅 00:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132401">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47978b8339.mp4?token=JXrQZzr8pvbJAUYJQ2YVkY0ZfU4dZNO2bJyXgPcAdf-aoKB1mahT9YEd7m17wxOb_pzIeptK7GYQfjScFJgTcUViceaS1GfcRBtErYxh5BYHzn2oKt3vw5Sjaze4kZlz230WBRZqdm2l407edZtEu4UXa5kyrxRxctshqhOzTFwC-9PAq6JgKEn2o66zptX9rKYTce79kaurs1-9pwYMaz-S5Z0nzI3VsY_jUH-r-VBqFXEPqtiWA4vGByL15tDLaFfhLE-zaFzFppnz3ncqJ5sO2XGeO72vN5cZsuh5n-x9_MeWzrU0QBfRiwhlx6kT20ZGTDtgnEolaftxDn6CXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47978b8339.mp4?token=JXrQZzr8pvbJAUYJQ2YVkY0ZfU4dZNO2bJyXgPcAdf-aoKB1mahT9YEd7m17wxOb_pzIeptK7GYQfjScFJgTcUViceaS1GfcRBtErYxh5BYHzn2oKt3vw5Sjaze4kZlz230WBRZqdm2l407edZtEu4UXa5kyrxRxctshqhOzTFwC-9PAq6JgKEn2o66zptX9rKYTce79kaurs1-9pwYMaz-S5Z0nzI3VsY_jUH-r-VBqFXEPqtiWA4vGByL15tDLaFfhLE-zaFzFppnz3ncqJ5sO2XGeO72vN5cZsuh5n-x9_MeWzrU0QBfRiwhlx6kT20ZGTDtgnEolaftxDn6CXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مجری صداوسیما:
◻️
آقای حدادی چه گیری دادی که باید حتما در آسیا حضور داشته باشید؟ حتی اگر CAS رأی بدهد و امتیازات تراکتور و استقلال کسر شود و سپاهان هم مجوز حرفه‌ای نگیرد، پرسپولیس به آسیا نمی‌رود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SorkhTimes/132401" target="_blank">📅 00:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132400">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
از بین شهریار مغانلو و علی علیپور؛ یکنفر از لیست نهایی تیم ملی برای جام جهانی 2026 خط خواهد خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SorkhTimes/132400" target="_blank">📅 23:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132399">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kt6k0u4mcGavcYfdj_nWkmq8N9VvCEnNi8ftYhWCJkNaVnvbqHC9Jy4Wvg0lIp8S2QK6bUX6Z11I2e9mXXFU16V50U5mil0-6hQySCYuc9GU2Hpa_vg6DDczbpbqPC8sIG2N5b_I42ukmp-a-VTVvIvJuavZU_-qJnLJjaTVkZyRO5-IThQ8KfkZzvu2EuR8HifZDm8wE8kR3mp_uZna9AC8dczLnjXzvkzqXyAgCExIxZpm-FYjIZtvJQxGxoYhO_oZdSZ1cAvYOAIsQtC01vZCj7NEJKtroATTxkqT5JLuqoOAOR9KxR_CTaYFpCaZo_aq9RC8c5DvefHft5r8Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیمان حدادی:
اگر با سروش رفیعی و میلاد محمدی برخورد نکنیم، توهین به بقیه است. به هیچ بازیکنی اجازه ندادیم که سر تمرین نیاید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SorkhTimes/132399" target="_blank">📅 23:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132398">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‼️
فداحسین مالکی، عضو کمیسیون امنیت ملی مجلس:
🔺
بیشتر پیشنهادات ایران در مذاکرات پذیرفته شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SorkhTimes/132398" target="_blank">📅 22:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132396">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❗️
سی‌ان‌ان : ترامپ تو تلاشه قبل از تایید توافق با ایران، مشورت بگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SorkhTimes/132396" target="_blank">📅 21:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132395">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6vx4ZmgHA_58JyXV2-b1vUJxIMVn9xXjkcQDD_Yve3-aCWSKhBTBSUZR-HrWhBE3Pq5YBPk9UqO1N4tDoLSy7KEcsndKT9L8V_nKApOoapoWqjRQhycGSE6pP9z81bUViA8IVpzs02Sqp7B-swmiPLpi2qSgO82yDDDsewQcoq8lVlb0xNvl2Irnn56kJ_8hjAEeWPg9kMWjeFlOFfXnDa3V5ymvPRxx9MIM3AOAhGjuGoqnqazHLUBSLu29Mcf4fb81NMze-GmgdCanF6pMIiIk-ef5UkvTDVffTLu9kLrsZUqgAt5kccmYZBNFJ6mMBxPetYH8SoimE9Rko5M7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کیت‌های ایران و هم‌گروه‌هایش در جام‌جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/132395" target="_blank">📅 21:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132394">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
*یک مقام آمریکایی به الجزیره:*  ما تأیید می‌کنیم که ایالات متحده و ایران به یک یادداشت تفاهم در مورد تنگه هرمز و مذاکرات هسته‌ای دست یافته‌اند.
🔴
توافق بر سر یادداشت تفاهم با ایران در انتظار تأیید رئیس‌جمهور ترامپ است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SorkhTimes/132394" target="_blank">📅 21:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132393">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/divG9Sme6fybUrVc77zyf2w65wtD-bUGp4Xc5oqFDNoIedQX-owSRPcAZqIhZEfqYgw9ZZi8iKtXkDtuzOYybbfxnlRbw4MfBB4wcwYRvDYGZzrR-XGti-1mzEWqKNSYJ6pEqeLOVF5KPgmBwlqh03ac0LZoFr2RkUgFc-JbUN3xpBTIXqsSPlL42x8MT0stbs6BcvvLXtr1qk_jHFK2G_jPk5AFClholuMHtZQrIJZlw03crq9PZtpTI8bldSGDinvenqfvbczcalOilhtCACHT9Ii2TQI_-MrJtzVAL-h66eLY1EibkWiegnZil75-lGP1-PXuPQi7oqmpaJrPuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کشور های دارای سریع ترین اینترنت موبایل در جهان
❌
ایران اصلا حتی تو لیست هم نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/132393" target="_blank">📅 21:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132391">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
ادعای العربیه به نقل از یک منبع دیپلماتیک :
🔻
توافق بین واشنگتن و تهران در دو مرحله خواهد بود
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SorkhTimes/132391" target="_blank">📅 20:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132390">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrsaaEUFXOGMxwNohxlm0uBrGnKtkPV7hoYnMiHgqKJqQ8Ds9I-A-koozm-IqI7wvQ1eS4y_8JBQUhkdqn8iQK-FSiT2tIA2yfiBGGZV_SJ8gMMNgjdxwmaBfTOFqW0GkzYS5Gu_U7X8-_Md7k_ZM1UcdsRqhd2ChdfMBFFZGbAHu4oa_HAgn2ExusN3a1pmRpLTU5asXyFVEFuoRWeG5Ec-peDC_hRDUd80wuXoE6ut2YnXyQfi-_Logqqbf_CjZMuNFoeHkjeelfzqMYDbrfHZiOEl7x1NRnYQgIeU2EHlwQgssQAIWrKDH5xNNB6KzLhEtI7OAVnYpkKMgao5NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
مسابقات گرنداسلم رولان‌گاروس رو با بالاترین ضرایب در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/132390" target="_blank">📅 20:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132389">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fp6ta-HU8tONgkX6gH3v_aJpHUM0XuujqUhHPJVObACXUtH2tFQU9SNb9tGazW3n_CAcjnYR7EST26xN0mGfHsBlAQkqgYVd6LW2LREKF9kZBTdGdy2u2BUCs5Szn_dGPAVW2U9x-Xvx-UhdESFMBL0VpxpXPVOU6b64-SEacMaWlp8peqdNUO-zcKt0FKDSBfxOxHs4MxCKQoRPp2enIrvqyb6LfsHJS9FJv1uhstNs_6Y4uVHicNutJsrorG4VP7nQjcwvLfekUQUUnHGM7r0W0b9mETZ88tc4iu7-B3CxR1uBbi36PBvEpTY6PHa1LC2-D1daf2hSl87rbWcRhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ادعای العربیه به نقل از یک منبع دیپلماتیک :
🔻
توافق بین واشنگتن و تهران در دو مرحله خواهد بود
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SorkhTimes/132389" target="_blank">📅 20:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132388">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
مبلغ رضایت نامه آریا یوسفی از سوی باشگاه اصفهانی ۲۰۰ میلیارد اعلام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/132388" target="_blank">📅 19:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132387">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">⁉️
⁉️
نت بلاکس: سه ماه پیش در چنین روزی Iran دسترسی به اینترنت جهانی را قطع کرد. در حالی که اتصال اکنون تا حد زیادی بازگشته است، شاخص‌ها نشان می‌دهند که کاربران هنوز با فیلترینگ شدید مواجه‌اند، مشابه دوره موقت بین اعتراضات ژانویه و آغاز جنگ.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/132387" target="_blank">📅 19:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132385">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
✅
خروجی ها احتمالی پرسپولیس:
🔺
میلاد سرلک
🔺
امین کاظمیان
🔺
مرتضی پورعلی گنجی
🔺
میلاد محمدی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🔺
سروش رفیعی
🔺
یاسین سلمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/132385" target="_blank">📅 18:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132384">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/132384" target="_blank">📅 18:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132383">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
✅
خروجی ها احتمالی پرسپولیس:
🔺
میلاد سرلک
🔺
امین کاظمیان
🔺
مرتضی پورعلی گنجی
🔺
میلاد محمدی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🔺
سروش رفیعی
🔺
یاسین سلمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/132383" target="_blank">📅 18:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132382">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
طبق گزارش Axios، این توافق شامل موارد زیر خواهد بود:
🔴
دسترسی بدون محدودیت از طریق تنگه هرمز بدون عوارض یا مداخله از سوی ایران.
🔴
محاصره دریایی آمریکا نیز برداشته خواهد شد، اما متناسب با بازگشت حمل و نقل از طریق تنگه هرمز خواهد بود.
🔴
تعهد ایران به عدم دنبال…</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/132382" target="_blank">📅 18:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132381">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/132381" target="_blank">📅 18:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132380">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
✅
خروجی ها احتمالی پرسپولیس:
🔺
میلاد سرلک
🔺
امین کاظمیان
🔺
مرتضی پورعلی گنجی
🔺
میلاد محمدی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🔺
سروش رفیعی
🔺
یاسین سلمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SorkhTimes/132380" target="_blank">📅 17:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132379">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SorkhTimes/132379" target="_blank">📅 17:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132378">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
🔴
🔴
و تمام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/132378" target="_blank">📅 17:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132377">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
🔴
🔴
و تمام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/132377" target="_blank">📅 17:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132375">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">💬
🎙
🔴
عبدالصمد ابراهیمی، کارشناس حقوقی:
🗣
شکایت پرسپولیس از فدراسیون و سازمان لیگ زمان بر است و رای بیرانوند قبل از جام جهانی صادر نمی‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/132375" target="_blank">📅 17:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132374">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
✅
خروجی ها احتمالی پرسپولیس:
🔺
میلاد سرلک
🔺
امین کاظمیان
🔺
مرتضی پورعلی گنجی
🔺
میلاد محمدی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🔺
سروش رفیعی
🔺
یاسین سلمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/132374" target="_blank">📅 17:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132373">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8sy2rLLGw0dqdd6KKhJxVGCDuecPMBiFY0GM8DR-w5sIlwp4YdivKDJy_AlMZp5LCAo5GU-SUKkoYNNOnN_VG8jCAvVSoffCI-2-bqxOzutZ_4GaSdfaOd-_J6LRg7eHStXY1oBRW8xTXGboFhFxlhxO-T3ypoHVdsB6Svm__whnqpA6pE4vvjZhMDGfLwy9-fGo26kXLBGZGdzWX7Q_XqH5Y6OhTG3KC1CaMo6kNezBvoyRepscp_9TCI4Rm51bc4vVHptjdqshgTLlbkHG23_PKfK_tqkGHQCIJ7U826haq_tBhUjFRU5mm91D4Z3WeJnc_Lvh7cD6-J6MtT6wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚡️
هر مسابقه یک فرصت، هر انتخاب یک هیجان!
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/132373" target="_blank">📅 15:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132372">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
فارس: هنوز جام‌جهانی شروع نشده اورونوف از دو تیم روسی روبین‌کازان و دینامو مخاچ‌قلعه پیشنهاد دریافت کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/132372" target="_blank">📅 15:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132371">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
مهدی طارمی - شجاع خلیل زاده - دانیال اسماعیلی فر و احسان حاج صفی تا این لحظه به دلیل خدمت در سپاه ، احتمال صدور ویزا واسشون پایینه و به جام جهانی نمیرن ، البته فدراسیون درحال رایزنیه ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SorkhTimes/132371" target="_blank">📅 15:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132370">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
سپاهان به بازیکناش اعلام کرده فصل آینده با کمبود بودجه روبه‌روئه و احتمال فروش چند ستاره این تیم بالاست؛
🔴
پرسپولیس و استقلال هم می‌خوان از این فرصت استفاده کنن و برای جذب بازیکنای کلیدی سپاهان وارد عمل بشن...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/132370" target="_blank">📅 14:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132369">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTA-9FoEC8_ZW2ND_pxq4i7yAlhgvcOjsupxHUodgbL89Z2Q3N0RYW1zBtQ6RtT5131zuJB9HRB1bigiejjUlyOEZQTBxOImijPW5Q56qigvMWmAQTfWS84wwYsCHEiRpOf2reffA_Xq2vfXncd8_b5-_M1MG3E5peDBVneUQVSWK5vOxS_McsSy94_VbjbFypRmlvunoOJDc6Lz-GBT7c2jJLcwIhzR1QW7RbcL5RaAbXCzvPRq44RANrzaAuCt5eqFGa8hqsOn4OD-gZqlMWGoxx3dWX4tkwKpPiE2ql7RFY-K5MEJV1r3jTodd2aDp42DlZF1ChyoXNkscovFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
نت بلاکس: سه ماه پیش در چنین روزی Iran دسترسی به اینترنت جهانی
را قطع کرد. در حالی که اتصال اکنون تا حد زیادی بازگشته است، شاخص‌ها نشان می‌دهند که کاربران هنوز با فیلترینگ شدید مواجه‌اند، مشابه دوره موقت بین اعتراضات ژانویه و آغاز جنگ.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/132369" target="_blank">📅 14:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132368">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
فعلا تلاش‌ها برای بازگشت سردار آزمون به تیم ملی جواب نداده.
🔴
سردار حاضره پست عذرخواهی رو منتشر کنه. قلعه‌نویی هم گفته هر طور شده سردار با هر تبصره‌ای که هست به تیم اضافه بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/132368" target="_blank">📅 13:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132367">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🎙
‼️
پیمان حدادی:
‼️
🔴
برای بازی با ملوان به دادگاه CAS شکایت کردیم، سپاهان و گل‌گهر هم قرار بود شکایت کنند. امیدواریم سه امتیاز این بازی را بگیریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/132367" target="_blank">📅 12:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132366">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎙
پیمان حدادی:
🔴
ما هم می‌گوییم استقلال نباید معرفی شود؛ در حالی که نماینده پلی‌آف در آسیا نداریم؛ بعد از جام جهانی در کنار لیگ حتی می‌شود جام حذفی هم برگزار کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/132366" target="_blank">📅 12:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132365">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🎙
پیمان حدادی مدیرعامل باشگاه پرسپولیس:
🔴
با چند بازیکن وارد مذاکره شده ایم اما هنوز از آیین نامه نقل و انتقالات برای فصل آینده خبری نداریم. نمی‌دانیم بازیکن خارجی می‌توانیم جدی کنیم یا خیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/132365" target="_blank">📅 12:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132364">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrH-zCseqXYvPsZoNYfJ3OVT0eimwa04jsgfa6_PV_Qd1A5m3KQiCOYkpKAHSw-hWWOK6FB3E9x2Yls7gWU9YVLK2zZ2QlwifCJlnv0dVi8SbJqBAJIQnH8f3UxCINQ9jgAsYmel0b9S63fu9rh5oPx4DoOrNowV8AmzfCyhI_EoZcJhnhSHmnmjblwngKJerjpZA8hM8vOkNr9w-Y_ftH3gIWsWq0c_SAyNfbddtpwkX9lt0CR6MzcPqnQn_rREOIUkJRQLRVjYfS1MnGc4Hmr4ONTgXKvNwSGHCSaWRubMQESaC1L8Jz5AntqSe7Ot8Z10FpCUlxY5XxJwTltfOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#روز_شمار_جام‌جهانی2026
⚽️
14 روز تا شروع بزرگ‌ترین و هیجان‌ انگیزترین رقابت فوتبال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/132364" target="_blank">📅 11:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132363">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">#فوری_مهم
🚨
🚨
گویا سپاه امروز پایگاه آمریکا در کویت مورد هدف قرار داده بخاطر حملات دیشب آمریکا به بندر عباس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/132363" target="_blank">📅 11:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132362">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❗️
نت بلاکس: به نظر روند بازگشایی اینترنت ایران متوقف شده و در حال اعمال محدودیت‌های بیشتر برای جلوگیری از دانلود و استفاده از VPNها هستند!
🔸
کماکان هیچ اخباری مبنی بر اتصال کامل اینترنت دیتاسنترها وجود ندارد که مشخصاً برای جلوگیری از گسترش تانل‌ها و VPNها…</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/132362" target="_blank">📅 11:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132359">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❗️
خبرآنلاین: سردار آزمون حتی با دستور رئیس‌جمهور هم دیگه نمیتونه به جام‌جهانی بره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/132359" target="_blank">📅 09:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132358">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⭕
تلاش بیهوده برای رفتن به آسیا یعنی حماقت اون هم زمانی که حقمون نیست که به آسیا رفتن فکر کنیم
✅
باید بپذیریم که اگه شرایط جدول برعکس بود و ما صدر جدول بودیم و لیگ نیمه به اتمام می‌رسید حق خودمون میدونستم که به عنوان سهمیه ایران برای لیگ نخبگان معرفی شویم
✅
نه به cas فکر کنیم نه به تلاش بی ثمر. Cas تا بخواهد به پرونده رسیدگی کند سه فصل لیگ نخبگان سپری شده.
✅
برای فصل بعد برنامه ریزی کنید. تیم را بسازید‌ ریشه ای و بدون بازیکن سالاری...
✅
پس بکوبیم و دوباره بسازیم.
فرصت ها را از دست ندهید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/132358" target="_blank">📅 09:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132357">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzaN84p1mV9_UrCLZ4KHhHdcXBmMbO-pSxNRQF8WiGQdZkzGXI-rrjZFvGpLWdlh6TQ-dlZw_y3NjgXbrJZ50YtdZO4OE54KIyyL6v3ZqWgAD1PHpqHbhEfQiyfRCGTUKMCEYZ7QGQGi3KBiwdod26OfR2_2uob-_1zDc_rT7o_CDSHKztY0a-CfiWrdU8LWh5VPF-UQc0203jmYg1W1vjsRdlhEXs4THJvrLhOLGUC2osGBUfjeg2uYCSrad8M4cAUEW8mLFAY-f5DYnQoRUE05BwC83BXz6UoRZH6441BmlKxULn5FqmpjMx4vXtbu2kCl_GALEbZZw5LYNWEwAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اوسمار برنامه ویژه‌ای واسه پایین آوردن میانگین سنی تیم داره و باید با اکثر بازیکنای بالای ۳۰ سال خداحافظی کنیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/132357" target="_blank">📅 09:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132356">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
تسنیم: ساعاتی پیش یک نفتکش آمریکایی با خاموش کردن سیستم راداری خود قصد عبور از تنگه هرمز را داشت که با اقدام سریع و قاطع نیروی دریایی سپاه و شلیک به سمت آن، مجبور به توقف و بازگشت شد.
🚫
در مقابل، ارتش تروریستی آمریکا به زمین سوخته‌ای در اطراف بندرعباس شلیک کرده‌اند که صدای انفجارها مربوط به این ماجرا بوده است؛ این شلیک هیچ خسارت جانی یا مالی به همراه نداشته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/132356" target="_blank">📅 09:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132355">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WX7cXhMUlAtUpvwpO9Yynezt4-ciyLwUlToBnMWbfCALDlQd4qz9BEEH6vXgjt-V3cgP-qPPkaTPTBjOuFK2VjI0N2_AewZt9o_CpuFlT3cXE_NR0oEnki8leFSEDHUwx_4wR6b8WV1YbkeonyfaFpg8YyXHCXF7tvgtWgKnkmNmAL-HbGTDkAzSUhdlrQhQd9kzzVyd78W85EWxfcZjZsT3EDxM1ouYllRMARJgscohaNpkrjO_TMzUDyztGzjgv4_3JwsD44ptbS_EOVBHgouYpgWE6rCnc3yUwGKM8v4MiDwxTYs3_f28clHGrx9MRLGhYUteL9-8YIE6qVVPRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
مسابقات گرنداسلم رولان‌گاروس رو با بالاترین ضرایب در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/132355" target="_blank">📅 01:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132354">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
رضا درویش:
صحبتی برای حضور در هیأت مدیره پرسپولیس با من نشده است.
🔺
در ورزش بهتر است هر فرد پس از چند سال فعالیت، مدتی استراحت کند. همان‌طور که یک پزشک پس از انجام جراحی‌های متعدد نیاز به استراحت دارد.
🔺
فعلا ترجیح می‌دهم دور از فضای اجرایی باشم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/132354" target="_blank">📅 01:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132352">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
گوگل پلی رفع فیلتر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/132352" target="_blank">📅 00:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132351">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
خرید بزرگ پرسپولیس از اصفهان میاد./مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/132351" target="_blank">📅 00:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132350">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❗️
نت بلاکس: به نظر روند بازگشایی اینترنت ایران متوقف شده و در حال اعمال محدودیت‌های بیشتر برای جلوگیری از دانلود و استفاده از VPNها هستند!
🔸
کماکان هیچ اخباری مبنی بر اتصال کامل اینترنت دیتاسنترها وجود ندارد که مشخصاً برای جلوگیری از گسترش تانل‌ها و VPNها…</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/132350" target="_blank">📅 00:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132348">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
ترامپ
🔴
کنترل پول اونا دست ماعه و وقتی اونا کار درستی انجام بدن و چیزی که میخوایمو بهمون بدن ما هم پولشونو بهشون میدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/132348" target="_blank">📅 22:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132347">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❗️
نت بلاکس: به نظر روند بازگشایی اینترنت ایران متوقف شده و در حال اعمال محدودیت‌های بیشتر برای جلوگیری از دانلود و استفاده از VPNها هستند!
🔸
کماکان هیچ اخباری مبنی بر اتصال کامل اینترنت دیتاسنترها وجود ندارد که مشخصاً برای جلوگیری از گسترش تانل‌ها و VPNها…</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/132347" target="_blank">📅 22:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132346">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
بودجه سپاهان برای فصل آینده مشخص شد
⏺
باشگاه سپاهان بودجه 500 میلیارد تومانی برای فصل آینده خواهد داشت و به هیچ عنوان تصمیم ندارد از این سقف بالاتر برود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/132346" target="_blank">📅 22:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132345">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
🚨
حمله وزیر ارتباطات به مخالفان اتصال اینترنت:
❌
واقعا شرم اور است بعضیا نمیخوان اینترنت وصل بشه، اینها فکر میکنن اینترنت تو دوتا پیام‌رسان خلاصه میشه اما اینطور نیست
❌
من و دکتر پزشکیان با قدرت جلو میریم تا بهترین اینترنت رو در اختیار مردم که حقشون هست بزاریم…</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/132345" target="_blank">📅 22:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132344">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❗️
🔴
ترامپ:
✅
به درخواست نخست وزیر و فرمانده ارتش پاکستان، به ایران فرصت کوتاهی خواهیم داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/132344" target="_blank">📅 22:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132343">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
بودجه سپاهان برای فصل آینده مشخص شد
⏺
باشگاه سپاهان بودجه 500 میلیارد تومانی برای فصل آینده خواهد داشت و به هیچ عنوان تصمیم ندارد از این سقف بالاتر برود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/132343" target="_blank">📅 21:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132342">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
الان به نظر میاد خودشون دنبال توافقن. فکر نمی‌کنم حق انتخاب زیادی داشته باشن  اینترنتشون تازه دوباره وصل شده، اقتصادشون هم داغونه، تورم هم خیلی بالاست!  شاید مجبور بشیم برگردیم و کار رو یک‌سره کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/132342" target="_blank">📅 21:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132340">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
بودجه سپاهان برای فصل آینده مشخص شد
⏺
باشگاه سپاهان بودجه 500 میلیارد تومانی برای فصل آینده خواهد داشت و به هیچ عنوان تصمیم ندارد از این سقف بالاتر برود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/132340" target="_blank">📅 21:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132338">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
❌
مرتضی کرمانی مقدم:اعلام قهرمان؟ اگر دست من بود می‌گفتم همه تیم‌ها به لیگ پایین‌تر سقوط کنند. مگر کیفیت مسابقات امسال بالا بود که حالا منتظر ادامه آن باشیم؟ به معنای واقعی کلمه هیچ تیمی مدعی قهرمانی نیست و از این به بعد حتی اگر مسابقات برگزار شود بعید است کیفیت آن تغییری کرده باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/132338" target="_blank">📅 21:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132337">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqJXmu6GwC26_G8fDFCxNSnh-8vlmdCk-Fob03ebyRT9aYFpsPSPwjb35GUJp6qSQqnJyk-ahHzI_skSLMHgW8BR6OmC1h_3-ikgbrRxHXFcDLGpklKBW6oM4tc39qTH4vITSftxP9-BoFN17m-jEbWWApTQ0sCr_uJEKeTfnyYY_-ourPt3aO9rRM3Vjwdui5lyM0QM_yzqNDNKErzJNVrnuczEsiNiDjL8EQPfuZI7Ck9hCyq7_1Ga-G5r7szV3DKnBIefo-Vq5DUZO3EwuQKDFzQwkj6WWUMOiuJk6i3D35WAmp5AhEVz2-l6WMCtIr13i-CIGwnUGtcGrExdzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
فینال لیگ‌کنفرانس اروپا
[
کریستال‌پالاس
⚽️
-
⚽️
رایووایکانو
]
⏰
امشب ساعت ۲۲:۳۰
🔗
این دیدار هیجان‌انگیز رو در سایت اسپورت نود با بالاترین ضرایب پیش‌‌بینی کنید.
🎁
بونوس ویژه ثبت‌نام برای کاربران جدید، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/132337" target="_blank">📅 21:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132336">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
باکیچ و تجربه متفاوت در پرسپولیس
◽️
سایت‌ها و رسانه‌های فوتبالی مرتبط با کشورهای حوزه بالکان در مطالب منتشرشده درباره باکیچ، روی سابقه بین‌المللی این بازیکن تأکید کرده‌اند؛ هافبکی که سابقه بازی در لیگ‌های پرتغال، ایتالیا و یونان را در کارنامه دارد و سال‌ها در فوتبال اروپا حضور داشته است.
◽️
رسانه‌های این منطقه همچنین حضور باکیچ در پرسپولیس را اتفاقی قابل‌توجه برای فوتبال مونته‌نگرو توصیف کرده‌اند و معتقدند بازی در یکی از پرهوادارترین تیم‌های آسیا می‌تواند تجربه متفاوتی برای این بازیکن باشد.
‼️
نظر شما درباره باکیچ چیست؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SorkhTimes/132336" target="_blank">📅 21:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132335">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
اوسمار کراش زده رو آریا و لیموچی و حزباوی و باشگاه در تلاشه برای جذب شون راهی پیدا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/132335" target="_blank">📅 21:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132333">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
#فوری | ترامپ:
🔻
ایران می‌خواهد توافقی منعقد کند و ما با آن توافق می‌کنیم یا به ماموریت پایان می‌دهیم
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/132333" target="_blank">📅 20:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132331">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b15265d538.mp4?token=JeVnrUysOQUXlSLk32duNdSRmfmtMovof9CKmVSUhzdoKC9UVzjrEr1tRWPAkMaN-u54WrbSKs2zveLxQpqDmqKeLib33nWIO2tCSdvQPrl1JwYkIbADfzc1SOnH2eId6mJtyctx0R6YtjoFSgIt6Q8sh-3rO8X0NKygl6KL8AnwFuQvO52-ch5vJmZg19R2ik-3iJpOpKUKgJ6qlT85jWGKQ2I7AnmkFQ6EZn1PGE8N9VpXvI_dS1eXCffxo6T-t8ZqTNBY2vAoksZa2qZ2ektqcaL1CxIz8Igmy-oNoAMRKLLRL53JGmbupx9yy2xjJ4ZTTF4praNFWaJ3zcopSg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b15265d538.mp4?token=JeVnrUysOQUXlSLk32duNdSRmfmtMovof9CKmVSUhzdoKC9UVzjrEr1tRWPAkMaN-u54WrbSKs2zveLxQpqDmqKeLib33nWIO2tCSdvQPrl1JwYkIbADfzc1SOnH2eId6mJtyctx0R6YtjoFSgIt6Q8sh-3rO8X0NKygl6KL8AnwFuQvO52-ch5vJmZg19R2ik-3iJpOpKUKgJ6qlT85jWGKQ2I7AnmkFQ6EZn1PGE8N9VpXvI_dS1eXCffxo6T-t8ZqTNBY2vAoksZa2qZ2ektqcaL1CxIz8Igmy-oNoAMRKLLRL53JGmbupx9yy2xjJ4ZTTF4praNFWaJ3zcopSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
#فوری
| ترامپ:
🔻
ایران می‌خواهد توافقی منعقد کند و ما با آن توافق می‌کنیم یا به ماموریت پایان می‌دهیم
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SorkhTimes/132331" target="_blank">📅 20:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132329">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🔴
🇭🇺
❌
قرارداد دنیل گرا بزودی با پرسپولیس فسخ خواهد شد.  این تصمیم توسط اوسمار به هیئت مدیره باشگاه پرسپولیس گفته شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/132329" target="_blank">📅 19:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132328">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ns5DgxGYme7NeIC6j29pNXeZEC9lS4WUflkRgXYBEBUvNWlUR7DGSH12rlDaKIfE4VCtXSjpMQsu4IyjMkva6rFBWlFyi1sF8e6FMh0MXHgAZjdzMeds-lvKJyT4Iwoc8X_qHHKmwizoP7OKWZ4lctIHNA-jF7lTkxn6LXrE79Zzixevq_9KgiKwvx_Ik5bIV3T9Pp6HEDsdTynVqQV7jz3WTJZ_LZ-7IWASp7QqLJSOVbDdJEdWqBZoVaxlPLIFRQ4tZxly7sEVEcupk_Eh4a9GtzLrSP3mRGi_Ru5JDl--qrJjQm2LcC4H8Qlo2KadmQDzUY5LXwA3gG6MuBJJ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇭🇺
❌
قرارداد دنیل گرا بزودی با پرسپولیس فسخ خواهد شد.
این تصمیم توسط اوسمار به هیئت مدیره باشگاه پرسپولیس گفته شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/132328" target="_blank">📅 19:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132327">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
حدادی : تا پایان فصل خلیلی سرپرست تیمه/با اوسمار در ارتباطم و گفته برمیگردم/اوسمار لیست خروج نداده/برای برگزاری لیگ جلسه گذاشتیم که بعضیا گفتن پول غذا نداریم و لیگ رو کنسل کنید/در نیم فصل دوم اوسمار نتایج خوبی نگرفت ولی دلیلش حواشی درون تیمی بود و فنی نبود…</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SorkhTimes/132327" target="_blank">📅 18:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132326">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✅
سپاهان به بازیکناش اعلام کرده فصل آینده با کمبود بودجه روبه‌روئه و احتمال فروش چند ستاره این تیم بالاست؛
🔴
پرسپولیس و استقلال هم می‌خوان از این فرصت استفاده کنن و برای جذب بازیکنای کلیدی سپاهان وارد عمل بشن...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/132326" target="_blank">📅 18:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132325">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
‼️
واعظی، مدیر رسانه‌ای استقلال: تیم ششم جدول نباید دنبال رفتن به لیگ نخبگان باشد. آن‌ها حتی در جام حذفی هم نیستند. ما حتی شانس قهرمانی در جام حذفی هم داریم. پرسپولیس فقط فرافکنی می‌کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/132325" target="_blank">📅 18:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132324">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎙
🔴
پیمان حدادی، مدیرعامل پرسپولیس درباره اتفاقات چند ماه اخیر حول باشگاه:
۱۲باشگاه به صورت کتبی گفتند بازی‌ها برگزار نشود!
بازی‌ها باید کامل برگزار شود و در همین اردیبهشت هم می‌توانستند برگزار کنند.
امیدوارم نمایندگان ایران براساس جدول پایانی و پس از ۳۰هفته، معرفی شوند
در پرونده بیرانوند علاوه بر منافع ملی باید منافع هواداران پرسپولیس هم در نظر گرفته شود،برای بازی با ملوان به دادگاه CAS شکایت کردیم.
به هیچ بازیکنی اجازه ندادیم که سر تمرین نیاید پرداختی‌های پرسپولیس نسبت به بقیه تیم‌ها بیشتر است.
نمی‌دانیم آیین نامه نقل و انتقالات برای فصل بعد چگونه است، برخی می‌گویند می‌توانید بازیکن خارجی بگیرید برخی می‌گویند نمی‌توانید یا ممکن است دوباره سقف قرارداد تعیین کنند.
کمیته اجرایی AFC پانزدهم اردیبهشت جلسه دارد و ممکن است سهمیه فوتبال ایران ۱+۲ شود
درحال حاضر محسن خلیلی با حفظ سمت، وظایف پیروانی را انجام می‌دهد، نام وحید امیری و کمال کامیابی‌نیا برای سرپرستی تیم مطرح نشده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/132324" target="_blank">📅 17:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132322">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
‼️
واعظی، مدیر رسانه‌ای استقلال: تیم ششم جدول نباید دنبال رفتن به لیگ نخبگان باشد. آن‌ها حتی در جام حذفی هم نیستند. ما حتی شانس قهرمانی در جام حذفی هم داریم. پرسپولیس فقط فرافکنی می‌کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/132322" target="_blank">📅 16:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132320">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
‼️
واعظی، مدیر رسانه‌ای استقلال: تیم ششم جدول نباید دنبال رفتن به لیگ نخبگان باشد. آن‌ها حتی در جام حذفی هم نیستند. ما حتی شانس قهرمانی در جام حذفی هم داریم. پرسپولیس فقط فرافکنی می‌کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/132320" target="_blank">📅 15:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132319">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
‼️
واعظی، مدیر رسانه‌ای استقلال: طبق قانون، صدرنشین باید به لیگ نخبگان برود. حتی اگر ما هم نرویم، پرسپولیس که رده ششم جدول است، کجای کار است که اعتراض می‌کند؟ تراکتور، گل‌گهر، سپاهان و چادرملو حق اعتراض دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/132319" target="_blank">📅 15:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132318">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
پیشنهاد رسمی باشگاه پرسپولیس به رئیس سازمان لیگ: حالا که‌مجوز حرفه‌ای باشگاه سپاهان صادر نشه استقلال و تراکتور رو به لیگ نخبگان آسیا بفرستید و ما رو هم به سطح دو لیگ قهرمانان آسیا.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SorkhTimes/132318" target="_blank">📅 15:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132317">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">#اختصاصی_سرخ_تایمز
🔴
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس هنوز باشگاه وارد نقل و انتقالات نشده و منتظر اوسمار هستند!
♦️
لیموچی و هر اسمی که به گوشتون خورده در حال حاضر هیچکدوم شون صحت ندارن و تا این لحظه باشگاه هیچ مذاکره ای با گزینه ای نداشته به بازار گرمی ها توجهی نکنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/132317" target="_blank">📅 15:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132316">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
🔴
شنیدم اقای کشوری فرد گفته هیچ باشگاهی جز پرسپولیس و مدیرعاملش اعتراضی نسبت به عدم برگزاری لیگ نداره…!حالا که یک فرد دلسوز داخل باشگاه هست که برای احقاق حق باشگاه میجنگه و پاپس نمیکشه اقایان بی تابی میکنن و تاب سربلندی پرسپولیس رو ندارن.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/132316" target="_blank">📅 15:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132315">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
🔴
شنیدم اقای کشوری فرد گفته هیچ باشگاهی جز پرسپولیس و مدیرعاملش اعتراضی نسبت به عدم برگزاری لیگ نداره…!حالا که یک فرد دلسوز داخل باشگاه هست که برای احقاق حق باشگاه میجنگه و پاپس نمیکشه اقایان بی تابی میکنن و تاب سربلندی پرسپولیس رو ندارن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/132315" target="_blank">📅 15:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132314">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
وزیر ارتباطات: اهتمام رئیس‌جمهور به بازگشایی اینترنت و احیای ثبات ارتباطی، نشانه‌ای روشن از عقلانیت و ایستادن در کنار مردم است. ملت ایران شایسته ارتباط آزاد، آینده‌ای روشن و اقتصادی پویا است .
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/132314" target="_blank">📅 15:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132313">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
محمد حسین صادقی: در پرسپولیس بدشانس بودم
🔺
وقتی بازیکنی به پرسپولیس می‌آید، طبیعتاً نیاز به زمان دارد تا خودش را با تیم هماهنگ کند و به ترکیب اصلی برسد. واقعیت این است که در چند برهه زمانی از این فصل، آماده قرار گرفتن در ترکیب ثابت بودم، ولی مصدوم شدم. …</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/132313" target="_blank">📅 14:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132312">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
وزیر ارتباطات: اهتمام رئیس‌جمهور به بازگشایی اینترنت و احیای ثبات ارتباطی، نشانه‌ای روشن از عقلانیت و ایستادن در کنار مردم است. ملت ایران شایسته ارتباط آزاد، آینده‌ای روشن و اقتصادی پویا است .
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/132312" target="_blank">📅 14:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132310">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
حالا که مسئولان باشگاه پرسپولیس خواستار برقراری #عدالت برای دادن سهمیه آسیایی شدند زمان این رسیده ما هواداران سنگ تمام را برای باشگاه عزیزمان بگذاریم
◽️
در تصویری که منتشر کردیم خواستار رسیدن سهمیه آسیایی به باشگاه عزیزمان پرسپولیس شده‌ایم و کمپینی به راه…</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SorkhTimes/132310" target="_blank">📅 14:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132309">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6bKlIJ1gk3W-V7r22lYIp7Q11JqXi7PUrpyaeuuqn0LK40S8zAv9Zq12uM5An19UrzPcZp7rCrmGdZf2fJXCdg9ex9qoiM1ES796y5FiCTXMdwLN8Dgueu7Zyeur1IblZrhVoYDN4_rAJE4Dfwb7MF66R-bpEQhAcrYrdWcfvLeyS0RerCk_gT0L0cp1CD2Q5VIapRNrB7o7JTuaOCdxUn5IupLtqXPGX7AmU_dY38K0Tc0qmp-bYCDWd620igZkRp0hlf4YM4oL0KX0z09mLN7A-SaAcRo5X-o2RjBvDhVFjfItMBj6wZe_BoVYhWk2WPkIHhgmTXQwyMCTcU3Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حالا که مسئولان باشگاه پرسپولیس خواستار برقراری
#عدالت
برای دادن سهمیه آسیایی شدند زمان این رسیده ما هواداران سنگ تمام را برای باشگاه عزیزمان بگذاریم
◽️
در تصویری که منتشر کردیم خواستار رسیدن سهمیه آسیایی به باشگاه عزیزمان پرسپولیس شده‌ایم و کمپینی به راه انداختیم
◽️
از تمامی دوستانی که در این حوزه فعالیت دارند از کانال یک‌نفره تا کانال و پیج میلیون نفری خواستار نشر دادن این کمپین و تصویر بالا هستیم
#پرسپولیس_آسیایی
#سهمیه_آسیایی_حق_پرسپولیس_است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SorkhTimes/132309" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132308">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdOrEy-OQcLPzRU9Pydh7NbHN19Jc5GfyIhcNaJOP6N3ZGQk5dhHnWLffoOnQdV0WEXt4R-CaKwpCs4Bkt8JktANHTDvzP8MX9z14WbuENBPsVa-QfDkazC-FCrDHR6eHH5iKDBGALgfrr084P72Tw9VMvLY9APgh1Mtlqkjy8YPYBFJz77qPklIIX4lGZmLDQpH2XBuKvOp9YVXfZk7NjOOt2ziXsu3HuFIAQdKZrXaSqDDP5VK4c_CPQLqT7C3Ce012epFG1S3MteM2yKwdIsc6z2KM5NQbfxB3wdSnaDglHrSy59GbDY_JYbq74eBbiZBvyHu5XxbTClSuMgajQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚡️
هر مسابقه یک فرصت، هر انتخاب یک هیجان!
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
بونوس خوش‌آمدگویی
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران جدید، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SorkhTimes/132308" target="_blank">📅 14:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132307">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
درخواست پرسپولیس از CAS
2 امتیاز استقلال و تراکتور را کم کنید
❌
پرسپولیسی‌ها سال گذشته پس از اینکه کمیته انضباطی فدراسیون فوتبال، باشگاه ملوان را در دیدار با استقلال و تراکتور به دلیل استفاده از یک بازیکن غیر مجاز (سینا خادم پور) بازنده اعلام کرده بود، از ملوان شکایت کردند و خواستار اجرای همین قانون برای خود شدند اما این شکایت در کمیته انضباطی و استیناف رد شد.
❌
باشگاه پرسپولیس اکنون و در شرایطی که قرار است نمایندگان ایران در آسیا براساس جایگاه‌شان در جدول مشخص شود، از دادگاه CAS درخواست کرده تا زمان رسیدگی به این پرونده و اعلام رای نهایی، به دلیل شرایط خاص موجود دستور توقف رای کمیته انضباطی صادر و فعلا تا مشخص شدن تکلیف پرونده پرسپولیس، 2 امتیاز داده شده به استقلال و تراکتور کسر شود.
❌
شنیده ها حاکی از آن است که دادگاه CAS نیز در این باره از فدراسیون فوتبال استعلام گرفته تا بعد از آن درباره درخواست پرسپولیس تصمیم بگیرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/132307" target="_blank">📅 14:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132306">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUHtab0rfNVhCiv719x1oXmDZJ_7QRUdqYp382-hib0nEV-tjl8nUT4-WrrNgWXIuHyZ9AdgDG51JHdC_83c9PiyNf5HDqShH7-fpdJgLWCb06f3_ydSMruM764IQoURi-pc8Zgc2C5vLVLqWpyNfMohAF6kpoQZJsWvrudck-Rb5Py3cyvV2J_wTruPBlzEo3AlIqB51QAZiaPaIULg8VoPFJSla-RJZ1ok6ZAXIzUX2dbWa1vDPiKM_xF97PuGt_97tYMDQUNxJO-a96ztOxCPa9Mhfs1Y9mqj-SWlTcZsU4zh6M9vAvZsPGjRMVHk2hWrg-b0gmJBiiiORwBxhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🟢
یک فروشنده در تیخوانا مکزیک، برچسبی با تصویر تیم ملی فوتبال ایران را نشان می‌دهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/132306" target="_blank">📅 13:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132304">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
وزیر ارتباطات: اهتمام رئیس‌جمهور به بازگشایی اینترنت و احیای ثبات ارتباطی، نشانه‌ای روشن از عقلانیت و ایستادن در کنار مردم است.
ملت ایران شایسته ارتباط آزاد، آینده‌ای روشن و اقتصادی پویا است .
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/132304" target="_blank">📅 13:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132303">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
سردار آزمون به زودی با انتشار یک پیام عذرخواهی به تیم ملی بازخواهد گشت.  #خبرنگار_فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/132303" target="_blank">📅 12:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132302">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
ایسنا: مهدی لیموچی در آستانه پیوستن به پرسپولیس قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/132302" target="_blank">📅 12:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132301">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
طبق برخی خبرهای ضدونقیض؛ تندورهای حکومت فشار زیادی آوردن تا مجددا اینترنت بسته بشه و هر لحظه امکان داره این اتفاق بیفته. اگه کاری مهمی دارید سریعتر انجام بدید. چون هیچی قابل پیش بینی نیست.
✅
هنوزم بسیاری از آی پی ها فیلتره و اینترنت اختلال زیادی داره.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/132301" target="_blank">📅 12:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132300">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
باشگاه با یک بازیکن از سپاهان به توافق نهایی رسیده و این بازیکن داره فشار میاره که با این تیم فسخ کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/132300" target="_blank">📅 12:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132299">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
علت کندی شبکه اتصال زیاد است به مرور پایدار میشه
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/132299" target="_blank">📅 11:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132298">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
مهدی هاشم نژاد وینگر ۲۴ساله تراکتور:فکر می‌کنم خط خوردن من ترور شخصیتی بود. دوستانم در تیم ملی گفتند که خط خوردن من برای آن‌ها باورکردنی نیست.بعد از مصدومیت قلی زاده همه فکر می کردند فیکس باشم اما دعوت هم نشدم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/132298" target="_blank">📅 11:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132297">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
مدیران باشگاه پرسپولیس در روزهای گذشته با ایجنت پوریا شهرآبادی ، مهاجم جوان گلگهر جلساتی برگذار کردند و خواهان شرایط جذب این بازیکن شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SorkhTimes/132297" target="_blank">📅 11:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132296">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
شهاب زاهدی که به تازگی بازیکن آزاد شده؛ تمایل دارد به پرسپولیس بازگردد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/132296" target="_blank">📅 11:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132295">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
✅
مهدی لیموچی در آستانه پیوستن به پرسپولیس قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/132295" target="_blank">📅 11:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132294">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
نماینده محمد امین حزباوی امروز پیشنهاد مالی‌ مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/132294" target="_blank">📅 11:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132293">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🟡
فسخ لیموچی با سپاهان؟
▫️
به احتمال فراوان مهدی لیموچی به دلیل عدم گرفتن دستمزد خود در سپاهان با این تیم فسخ خواهد کرد و مقصد احتمالی وی پرسپولیس خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SorkhTimes/132293" target="_blank">📅 11:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132292">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUloY3JXyLqWsHwITOmOd6PuUSbnN69mYv1Im3fa_hUhE6w73Y0mT8TXLtOKw8y84dD4SFwkkWz5pZMubrFgUsPMfa51PIgylNQ6WqsVuvMlnXH1auMo8-BWGtNkEMoesVfytqIHBtPWX6suCrz4QdM4jn7FOX5mcTBZmQ4_kF1MDJCy81fbUC7qSoKWfEgeoWeqmhXfiawmmwhIW4BBERq5HlrxQHg-8H1p_1kKeIJuJfV4dgbkkj4UjhlRWD38_ag1E0KR7s8l6WdRYoE0a9yB9-DR2EyptkSAv7qV_O-6ONb-p3hu1iFv9kv6txCPPitSfjXzYjQSOTgx3_h9qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهاب زاهدی که به تازگی بازیکن آزاد شده؛ تمایل دارد به پرسپولیس بازگردد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/132292" target="_blank">📅 09:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132291">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇷
🇮🇷
جهانبخش نزدیک به یک‌ماه است که مصدوم است!
⚪️
مصدومیت علیرضا جهانبخش فعلا مرتفع نشده و این بازیکن فعلا امکان همراهی تیم ملی را ندارد. این در حالی است که 23 روز از مصدومیت جهانبخش سپری شده اما این بازیکن همچنان شرایط تمرین ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SorkhTimes/132291" target="_blank">📅 09:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132289">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLV1ZUN0RRsMEEcWwIF4GWG5BqcsSOCtfKWBGyTHsNSNGGdw8PLIgaE-9XBBa9_kwbliKZ_VlM0r3soIX168cEZPfMKhxzLKiKgrL-C9CIhCjaKQ-pUDfj0YLTqRZSAhToq__Dba5gRrx3gnM6D2LLfqH8ckTNSSIKqwPbOnWSjdFxOZ-VzcoAqN_KlyLVlAQi8JOn_xb9FdvN0wYYxllUwCNNWKAscDLmqIbKrumHMFiz9DVZfs6-pIuaIsJ6wfHkJiTBNHHtGGFcNvPaSNXKvm-NzgyJBVDnCvY6cufKaSXHygUWfhmao5KJ_9J8H4N71bgMe_FuzZE00M2yWfCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت فعال شد!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد سایت وینکوبت شوید:
👇
🟣
ywincob.com
🟣
ywincob.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/132289" target="_blank">📅 01:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132288">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‼️
کارشناس صدا و سیما : وصل شدن اینترنت متوقف میشه و دستور رییس جمهور اجرا نمیشه چون خلاف دیوان عالیه.
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/132288" target="_blank">📅 01:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132286">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b15265d538.mp4?token=QZ7geW6yb3CGN6y5VETrcHotyZv7Icqgbk27fFqeiLk4UFF7d3ivTxhxj19TE6DczsCGbCbMBMoap1um8amIrZ6B-MVaMlMEgBIgJh7HfuLHVNhvRt7St9Sol7qFRGo-xfIWvkqosepTB8NAILeFF1OtXbHZncFi2Idz7LCubdg4EhiNjoi6IH8eyQLr8Z1E_fW57gK9DXZT1gNCmLCzg8OvjGE3PjkzC81_6D_QHn3OK9DggMK_1A1CxHQLey7LPAEkzvaQVV12RN7YF_jf_GtpQRBODpBt0ieS2jCPbptVa6Yq-YuZunCZTxyupQcY6DQxPXXgTZTB32_ZEpWGBA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b15265d538.mp4?token=QZ7geW6yb3CGN6y5VETrcHotyZv7Icqgbk27fFqeiLk4UFF7d3ivTxhxj19TE6DczsCGbCbMBMoap1um8amIrZ6B-MVaMlMEgBIgJh7HfuLHVNhvRt7St9Sol7qFRGo-xfIWvkqosepTB8NAILeFF1OtXbHZncFi2Idz7LCubdg4EhiNjoi6IH8eyQLr8Z1E_fW57gK9DXZT1gNCmLCzg8OvjGE3PjkzC81_6D_QHn3OK9DggMK_1A1CxHQLey7LPAEkzvaQVV12RN7YF_jf_GtpQRBODpBt0ieS2jCPbptVa6Yq-YuZunCZTxyupQcY6DQxPXXgTZTB32_ZEpWGBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
#فوری
| نورالدین الدغیر خبرنگار الجزیره در تهران:
🔻
همه چیز انجام شده، چیزی باقی نمانده جز امضای توافق
‼️
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/132286" target="_blank">📅 01:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132285">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEROmU9tyJLl1aFZvLzNmOPzTh4fsatoWtcfyry43N4TiBabftX1Uh4W3hnZbhiZul6JWNbIproxF5WhNxSFifnbLieL6PuikHR0vILVVaIoD7dXHmvBoohMpOWVIghLKAEQ9NG0mVCmZD3KjcSpLOSR9QQykVUtFwfIdhS7KWJ5fIwoXdahwS4CDjxcdqD_8y3v8BRk-TwoYmdxzNbqkTV-gJeNcYAxvqRQd8C02ugpxbM6-NFCgkRBtjXZSA_uCFRRn-XhrxvOu9Tnqjho4RBYYy9eY_tnZja3VIdRrFWcBoeZGTgV07WJGmtT53yAZtqzhNfcRxGoWKvaITLgmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
🔺
فیفا اوکی داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/132285" target="_blank">📅 00:59 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

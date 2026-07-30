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
<img src="https://cdn4.telesco.pe/file/OB3V9RBtyPHvAqPbX6k92l7-IkSaFIn9ijdQ9NP9Fotewy81E7i4WmSj6J1HPqD91hWC2zXaYCKrFKgvgzxLfgyHry38f1oqbYLVEPaqpnkJDq24jyUej9vRSWXPQgjGAW1xLBuxfQBlFo8RIDfg6LAhwym9Lzq-sC2H7lEpcytNrbLx7g7u65CRhBgC6anfgiV2SqPGsx0t5mq0vDCgIXNfc3Twk78_Zpa1DPISIQtoY-GnMRPdD_M1WWspK21kIrwL8se_yC9d_nNdKMglmSYx4npicesNOateq9k-y8NubTsTHqDdpoF1ZVn6gSYrIHscWMJty6fxU8nXhrkuIw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 10:58:31</div>
<hr>

<div class="tg-post" id="msg-137030">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🫥
🫥
با موندن امیررضا رفیعی پرسپولیس میتونه 5 بازیکن جدید در پست های دیگه بگیره
🔴
دفاع وسط
🔴
دفاع چپ
🔴
هافبک بازیساز
🔴
مهاجم
🔴
دفاع راست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/SorkhTimes/137030" target="_blank">📅 10:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137029">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
پیوستن پورعلی‌گنجی به الطلبه صحت ندارد
⚠️
⚠️
ساعتی پیش برخی رسانه‌ها از پیوستن مرتضی پورعلی‌گنجی، مدافع پرسپولیس، به تیم الطلبه عراق خبر دادند اما پیگیری‌های خبرنگار فارس نشان می‌دهد این خبر صحت ندارد.
⚠️
⚠️
پورعلی‌گنجی هیچ قراردادی با باشگاه الطلبه عراق امضا…</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/SorkhTimes/137029" target="_blank">📅 09:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137028">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
تمام راه‌های ارتباطی به جنوب، فرودگاه، پل‌ها، راه آهن و... دارن دونه دونه نابود میشن! آمریکا بدون هدف کاریو نمی کنه. یه سناریو بزرگ و احتمالا حمله زمینی پشتشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SorkhTimes/137028" target="_blank">📅 09:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137027">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⚡️
⚡️
امیررضا رفیعی قرارداد جدیدی را امضا خواهد کرد
🔻
🔻
رفیعی یک سال دیگر با پرسپولیس قرارداد دارد مشکلی برای همراهی این تیم نخواهد داشت اما احتمالا با تمدید قرارداد در جمع شاگردان مهدی تارتار حضور خواهد داشت و زیر نظر حسین اینانلو کار خود را دنبال خواهد کرد.…</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/SorkhTimes/137027" target="_blank">📅 09:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137026">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🫥
🫥
🫥
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SorkhTimes/137026" target="_blank">📅 09:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137025">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
رفیعی ماندنی شد
🔄
امیررضا رفیعی گلر جوان پرسپولیس ماندنی شد و به ارودی ترکیه ملحق می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SorkhTimes/137025" target="_blank">📅 09:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137024">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
رفیعی ماندنی شد
🔄
امیررضا رفیعی گلر جوان پرسپولیس ماندنی شد و به ارودی ترکیه ملحق می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/137024" target="_blank">📅 08:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137023">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toPQA_r3cSjHxgtkMwSAncsfvEt_987yRkBaHwWYO8e6co8_ObuxUp5YhtCpjqt6rYXud52AwJj86SqN5G1XdjJ__hyI8ifD51mCnSkm30FPtqRAMl7GCgm14K0hxNUhuLorsC9g0ujYCzMnaWRKJzXVwPXtiH4ACWt_sfYm8xdh5-RLqMz2Pwu-dvdeeASCLzXkBhlszyWruiQAi0eCnGQ3snHuz0PSDBnCRtuDEgk0HvghlNMW-oNSPaXjxmYPH5q8CYqWr692Z10aqgY1h6DES749u1Lnj4vABi6nXUr4QNEboECERiMIIoDaJhacIPbhg7sg-qH7Bq9d5Qe9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/137023" target="_blank">📅 08:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137022">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwZBVBAAPatRFo12_rgS0jf353mM5TwYSlI_6FJMeUwDMRgTPt5pyEfavQJAN8Y1OorNMr_RtQwx05QMeE4bRJHNE3egHOi5-25-mBOKnhqeLSPBIGmcKN1h3JCjznS5N0bmyGt0dCgD7j_Q7c1bm9zWia2Fz9OpCnpf3aJoEIP2j5mQckFi_ZcJWCsaxiN-I1b6oy0jQeCijE0TFut2DFpsKKH8veq3QuByY5IY7213u4Zw9hRYIY0t5Yz2_NAcy_sN9An72WVKHtxp9JPeybLLWheyFAOfWMNyNSf__4jRgbRsubRUZU4aBwybM_Kr0yMbUJDn1NMt-mM30hVmCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏐
اوج
هیجان و جذابیت با لیگ ملت‌های والیبال همراه با
اسپورت نود
🏐
پنجشنبه ساعت ۱۰:۳۰
[
ایتالیا
🇮🇹
🆚
🇺🇸
آمریکا
]
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
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/137022" target="_blank">📅 01:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137021">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-VmDaQOCgr7_1K49nNInRGWtNy8tWbD0PBxXwDBhTO0vfpVZGKLFllFzEK2Va2ZoK6AiyudATxkOC-x3YASV6Cn1CBNEzs4TzdOHMF5xJ73tyw8MYRCU3L677grzL2ohK2qEsc9nt_aVkd-BJ8_R4qfX_AqfkmVeY_b_t9jzpdughuAfu9UnOkfLC9qZadd0NtM7mgE8ltgYWguWAs-bcsC8JoXvJJfSqptF0yByEOz3YSb4ODERAKRqsyH5qPpJvKLCEK1098ZwLW4QgIG-ixglITdYzmvpu6n6TcLJfXwpWV-i_RZ1m-9RoAEQCsUCeaiLGAst-szlqb9XkEFrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
رفیعی ماندنی شد
🔄
امیررضا رفیعی گلر جوان پرسپولیس ماندنی شد و به ارودی ترکیه ملحق می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/137021" target="_blank">📅 00:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137020">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❤️
❤️
❤️
❤️
❤️</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/137020" target="_blank">📅 00:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137019">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⚡️
⚡️
پوریا لطیفی فر با نخستین تمرین، آمادگیش رو نشون داد طوری که خیلی ها جا خوردند. کلا هافبک با انرژی و دونده ای است که شاید بخشی از این خلا بازیساز رو بتونه پر کند
⚡️
⚡️
مهدی‌طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/137019" target="_blank">📅 23:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137018">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
تراکتور از جذب قربانی منصرف شده و کناری گیری کرد /فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/137018" target="_blank">📅 23:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137017">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🫥
🫥
🫥
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/137017" target="_blank">📅 23:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137016">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
فرهیختگان: اولویت های تارتار در پست‌های مختلف
✔️
گلر: گوهری
✔️
دفاع راست: محرمی
✔️
دفاع وسط: افسرده
✔️
دفاع چپ: رزاق‌پور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/137016" target="_blank">📅 23:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137015">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔽
مرتضی پورعلی گنجی با باشگاه پرسپولیس   به توافق رسید و قراردادش امروز فسخ میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/137015" target="_blank">📅 23:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137014">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔄
🔄
🔄
آنا: محمد قربانی با رضایت نامه 200 میلیارد تومنی به تراکتور سازی تبریز پیوست
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/137014" target="_blank">📅 23:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137013">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/137013" target="_blank">📅 23:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137012">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
دنیل گرا در تمرین امروز هم حضور نداشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/137012" target="_blank">📅 22:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137011">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
شهاب زندی مدیرعامل نساجی:  با استقلال درحال مذاکره‌ایم، با توجه به بسته بودن پنجره شون اگه بر سر مباحث مالی به توافق برسیم این دو بازیکن آینده‌دار نیم‌فصل راهی استقلال میشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/137011" target="_blank">📅 22:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137010">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⚠️
⚠️
⚠️
مدیرعامل باشگاه گل گهر سیرجان :
⚠️
⚠️
امیر جعفری مدافع چپ مدنظر باشگاه پرسپولیس قرار دارد اما تا این ثانیه به صورت رسمی با ما مکاتبات نشده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/137010" target="_blank">📅 22:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137009">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
دنیل گرا ۶ هفته از میادین دوره و ممکنه باشگاه باهاش فسخ کنه/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/137009" target="_blank">📅 22:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137008">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4994f708ed.mp4?token=ie1NGtPCUKqUh7_XFrY9ZLOc9v-KxcMryRlxtq6D3DYJWuTtdMYwGg86iffUZini6FHj0mKi722m3-3m1h5-L9pkbnv5T3AtrgqVzsR-GY-c7npvyjo3cs8rDeWRm8vkhrI2pH4KTw7_eKdYniR3RD8n9LLeo5L5ovyMFXPP4KsWeY-JPAl9bat_MM4tZxYb3FZqAHJ1DYNXyTu3ZJOubWxnETo7qoUuK5OCdff0Gm0ifvXnbFpnSqSAPzezkzg0_owdwfRNN-g0qt6kV7-OaTCGIDt6erRutMd8yX9XW-7sW7wP0AKYxySaHOaOiVjamNLnLlz8SZuAsa_ITJ_Buw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4994f708ed.mp4?token=ie1NGtPCUKqUh7_XFrY9ZLOc9v-KxcMryRlxtq6D3DYJWuTtdMYwGg86iffUZini6FHj0mKi722m3-3m1h5-L9pkbnv5T3AtrgqVzsR-GY-c7npvyjo3cs8rDeWRm8vkhrI2pH4KTw7_eKdYniR3RD8n9LLeo5L5ovyMFXPP4KsWeY-JPAl9bat_MM4tZxYb3FZqAHJ1DYNXyTu3ZJOubWxnETo7qoUuK5OCdff0Gm0ifvXnbFpnSqSAPzezkzg0_owdwfRNN-g0qt6kV7-OaTCGIDt6erRutMd8yX9XW-7sW7wP0AKYxySaHOaOiVjamNLnLlz8SZuAsa_ITJ_Buw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
تمرین سخت امروز شماره
1⃣
🧤
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/137008" target="_blank">📅 22:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137007">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
🔴
تارتار همچنان ولکن گل‌گهر نیست
✅
شایعات؛ باشگاه به دنبال امیر جعفری مدافع چپ گلگهر!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/137007" target="_blank">📅 21:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137006">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mGJy4HnY27iWelaU6IHhlOW_-Kdoy84XDZuy_FBYn5om9i4eCLMSwLNnaDnzkwLnFPGzCGl9xuOufIvhYnPJcg1KPOp1bLtM0_wapq5Bf9gU-WEg_nmw82EyZj-Qhv4RXju0YVUE3nhmgjJWSDaGGQGKKDIxwWLkVJBsDK7zFvqtrh9dQUs0h7WiqA4pIaZpkUa2kiZrzSEZ4mk2WX_RgG2VdWNlM_xnAiCSAvHMLay6Rtpw8_PaB90akrSv5XmZGwM9swoKW5pFa9IaoyBLsjy6iPJ4H6AkEMKC_iNDA9nslPXPVdMXSeMORqrnp2kQbxBYXF0C08Cav-Q-Db-QuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
شنیده میشه پرسپولیس دوباره رفته سراغ مسعود محبی و با پیشنهاد جدید دنبال جذب این بازیکن
🔹
محبی هنوز هیچ قراردادی با تیم روسی نبسته و امکانش جذبش هنوزم هست همه چیز بستگی به نوع مذاکرات و پیشنهاد مدیران تیم داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/137006" target="_blank">📅 21:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137005">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
یاسین سلمانی ۲۰ دقیقه اخر بازی دیروز اومد زمین همه جا حضور داشت چه حمله چه دفاع
🗣
🗣
پاس گلشم روی یک ارسال تمیز شکل گرفت. با وجود اینکه جلوی چادرملو هم بهترین بازیکن زمین بود نکته عجیب اینکه چرا رسانه‌ها اصرار دارند مازاد بشه.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/137005" target="_blank">📅 21:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137004">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoI7sm-o36eGeYgsmQaGNfBnmEHr_O2bqY1wG91tqtfJPQ7aRSyX3fiByzcu8E-T0pLhzReT2SKOkQrv3IxrNGiuWp5hM5IeS1Da_pyDfi7zbTMbEize3H5WvJ-MokaHdSmjKyPfOSGd9gKwQ2iVJ5tr3GERjqJUznEzjtpm-Noymd-BQHQqW0WwpUTNoFtW2bOcB5n75sl60U5DDYUXOUHgYoWr9dzXCUJroXhVgBeD4Rqg6i6cRIlB5dwXEOM9WvBRP3FWyPL4kwt1-QS8N_8yeP9xVS7p7ZOcaCp3zjYIpzQoPR7xukSy8df5vEsMDqLQYy5_VaJIO3woV89-OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نگاهی به ۶ بازیکن ارزشمند لیگ برتر در سایت ترانسفر مارکت با حضور سه بازیکن از پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/137004" target="_blank">📅 21:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137003">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAf0Wux1by9VbKJuKJSbI6KB_4wcGkzQvXYah5TP_705eRcjZ1xzJlCBDYAH3OHy5UR7y8U2hULwM9QPxVUlhnyNMSPSEoVAOBeXqdp_ftlggZFng9xyKa4xS9IRDMgnTdhjNCbi0qo37cPdvNxdWPJE2XRKVHdXSKCHQyStGuZ2iO120Jup35Gkfhff6BNUDJQowSBoIgcJibJm7omTFCtF5OCKpxXod3p7JOCR4v5LH0nBMMFR_GtOIEZ2OpU8nwnPvY_t6ZOO2LoR5RPm2nJhQX0bF-nr5E-lfsxY5CrZ0VAgeJvRZ8YfT9GswljXtAOcOIvYocZ2L28wz2TzGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
زیر و رو شدن چهره پرسپولیس پس از گذشت 2 سال
🟪
🟪
از ترکیب فیکس پرسپولیس مقابل مس رفسنجان در روز قهرمانی، تنها حسین کنعانی و استون اورونوف در این تیم باقی مانده اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/137003" target="_blank">📅 21:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137002">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🫥
🫥
🫥
تارتار امیدواره بیفوما و محمدحسین صادقی رو دوباره احیا کنه. بیفوما بعد از یه فصل ضعیف، تو بازی دوستانه اخیر گل زد و حالا فرصت داره خودش رو ثابت کنه. صادقی هم که فصل قبل فرصت کمی برای بازی پیدا کرد، امیدواره با اعتماد تارتار بیشتر بهش بازی برسه.
🌀
🌀
از…</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/137002" target="_blank">📅 20:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137001">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_ygm_0-lhb2BrpF5d8Lfvs-pR-4vcfRGKrmn99v62_lIJFLv7BqDk_KG_guhvPc99w06OfKbZ_4_AvGQ38ehvFTMLK80aOIhnbgXSSH5oJeBCfLUL08siFNz0gjo6EcxUDClHOahLqKtDrrBSU5MrqWOaFNNJ_7aJtMJbnfEBD5wAIFtrDA7OabgkzxnxnY7Rd8DVuXuk81CQitqOXcFBvuylNosMdZtUYUN1rAv_keFrTwr1wOaAIwqkzYrlplahts405OphVN_3Kj4Ywq0YHC4g9ePJ7FNPJlyKQExRZ588k4PYkNkfJ83LawMsbnFcAwOmeh8ONVB7ua2tDS9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
اوج
هیجان مرحله برگشت مقدماتی لیگ قهرمانان اروپا همراه با
اسپورت نود
🇪🇺
شبی پرهیجان در مسیر رسیدن به لیگ قهرمانان؛ تیم‌ها برای یک گام دیگر به سوی مرحله بعدی به میدان می‌روند.
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
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/137001" target="_blank">📅 20:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137000">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cc30274f9.mp4?token=AdOMMIRd0I8YRoABDThdnwl4MeZfqCGqF33O4rLwqcBD6FzPNP6k5dA-1OV0uLFm1kRD2hl1-h_0kF4JMQuYQsvCBKHT_379lfTVavxB4dRRdWVJLL99w8qqYiKjCENuLUbq_5K_NDxQi4WygHVVSL6ZjNjoGqX0H-qIqt1scKU1cUKmknzWPMYuL8cwG6v_3g85pkjGx-73RwCOKWIUNUoQL25T6pEi7dS0pgt52vlYPvM0k53ftBa98E0TqlK3gIHojy9downy7BSpL4-lGuvPzhtqf-eU9MNMdDd-Cjm5QvU2y7lRXz0ZH6W-eZvH8Mx0-gJ7-xEEBkQ_7whBTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cc30274f9.mp4?token=AdOMMIRd0I8YRoABDThdnwl4MeZfqCGqF33O4rLwqcBD6FzPNP6k5dA-1OV0uLFm1kRD2hl1-h_0kF4JMQuYQsvCBKHT_379lfTVavxB4dRRdWVJLL99w8qqYiKjCENuLUbq_5K_NDxQi4WygHVVSL6ZjNjoGqX0H-qIqt1scKU1cUKmknzWPMYuL8cwG6v_3g85pkjGx-73RwCOKWIUNUoQL25T6pEi7dS0pgt52vlYPvM0k53ftBa98E0TqlK3gIHojy9downy7BSpL4-lGuvPzhtqf-eU9MNMdDd-Cjm5QvU2y7lRXz0ZH6W-eZvH8Mx0-gJ7-xEEBkQ_7whBTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
امین کاظمیان در حالی اولین بازی خود با پیراهن گل‌گهر را تجربه می‌کند که شماره ۱۰ گل‌گهر را بر تن کرده که نام تیکدری بر پشت پیراهن اوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/137000" target="_blank">📅 20:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136999">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⬇
⬇
بازگشت جنگ اعصاب به فوتبال
🔴
فوری - جواد نکونام به لیگ برتر برگشت
🤝
جواد نکونام پس از ساعت‌های طولانی مذاکره با باشگاه پیکان، به توافق نهایی با خودروسازان رسید تا پس از یک وقفه، دوباره به لیگ برتر برگردد و هدایت این تیم را برعهده بگیرد.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/136999" target="_blank">📅 20:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136998">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbOufIO2BmBu0qhVVk1ljmerM-gi-dP46FfOrwZbeF5ng-x_-TBf5UaUEIhiCu7UWZZGahbIxH22RqYi__b1YcHAJDi7MV9SqzrsIRQB4KkvlAPpnHCARfahV-gFcwBjnxKIZjEtS8weFAU5ELQ_LPUMhSadgPkLmo394IsYHgypwRHOqYx-AC3c-TvXN4tUgMmRWAUOInOV9sxc3pd5G1QtkucTLzfPiZwMKM-0B902pUY2Gz7pn1BtGgyJjY2H-sAHsLSA4fNMZfP9frjdn8Wa55oC-BifsVv1oLnVDV04xlVGZ6L_xnljKnJ-7sLWanFohyXOr6gyksiciiklwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
در عربستان پول پارو کرد!
🇸🇦
کریستیانو رونالدو از زمان پیوستن به تیم النصر، مبلغ شگفت‌انگیز 625 میلیون یورو به عنوان حقوق و پاداش کسب کرده است.
😇
فوق ستاره پرتغالی در کمتر از چهار سال، ثروتی بی‌سابقه به دست آورده و او را به فوتبالیستی تبدیل کرد که بیشترین میزان درآمد را از قراردادهای خود در تاریخ این ورزش داشته است.
🟡
حقوق پایه (۳.۵ سال): ۵۹۵ میلیون یورو
🟡
پاداش برای ۱۲۹ گل: ۱۱ میلیون یورو
🟡
پاداش برای ۲۳ پاس گل: ۱ میلیون یورو
🟡
دو جایزه بهترین گلزن لیگ: ۸.۵ میلیون یورو
🟡
پاداش قهرمانی در لیگ: ۸.۵ میلیون یورو
⚡️
مجموع درآمد: تقریباً ۶۲۵ میلیون یورو
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/136998" target="_blank">📅 19:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136997">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SY7UggLxaUoznlwiF9LAUXZZRmEz0sVquo__1B7kOhOQbMTcKsXiwtnBhfA60TDR7CqHuS9aU2kOKm4SACXYRp1o9hyX3VhamXKj3DD_BB-L60YPzgn8ap_NdUngh--guul1EnreqNAHHOW9uVLirIUeEPfKaJz87v-795tyaaNbcW1jny4kaJWjPkuyzPQHgysNbZ85gZxDv0EJEXwqF0-G0fd2Jgdcj84KbK6ei9dVKeBW1l3Xm3x3jhcQu4L0JWLPzgCAFAGpHWF7fEimGv6tGLksIInSabeNoMP2MuBJLwlhs1hPyhU1vs1pzPLsjYrpFLEBZlzMymhFjZ-Y1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👤
ممد مهتی امشب به اردوی پرسپولیس اضافه میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/136997" target="_blank">📅 19:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136996">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🌀
🌀
تارتار تو پست های دروازبان، دفاع راست ، دفاع چپ و دفاع وسط بازیکن میخواد/ فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/136996" target="_blank">📅 18:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136995">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⚡️
تارتار: حداقل به 4 خرید دیگر لازم داریم (دفاع چپ،دفاع میانی،گلر و مهاجم ) بازیکن می‌خوایم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/136995" target="_blank">📅 18:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136994">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✔️
✔️
میرشاد ماجدی، رئیس هیئت فوتبال تهران:
◻️
مسئولیت استادیوم‌های تهران با من نیست. ورزشگاه‌های دستگردی و شهرقدس برای لیگ آماده هستند، اما درباره آزادی هنوز تصمیمی اعلام نشده است. زمان شروع مسابقات مشخص نیست و به وضعیت جنگ بستگی دارد.برگزاری منظم مسابقات،…</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/136994" target="_blank">📅 18:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136993">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⚡️
⚡️
پوریا لطیفی فر با نخستین تمرین، آمادگیش رو نشون داد طوری که خیلی ها جا خوردند. کلا هافبک با انرژی و دونده ای است که شاید بخشی از این خلا بازیساز رو بتونه پر کند
⚡️
⚡️
مهدی‌طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/136993" target="_blank">📅 18:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136992">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⚡️
⚡️
فوری/ دونالد ترامپ: در پاسخ به حملاتی که سپاه پاسداران به اردن کرده، ما ایران را به شدت مورد حمله قرار خواهیم داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/136992" target="_blank">📅 16:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136991">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⚡️
ترامپ: اگر توافق نشود، پل‌ها را ظرف دو ساعت و نیروگاه‌ها را در یک روز از بین می‌برم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/136991" target="_blank">📅 15:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136990">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔻
گل های محمدمهدی محبی خرید و ستاره جدید پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/136990" target="_blank">📅 15:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136988">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
🔴
🔴
باشگاه پرسپولیس با مبلغ ۵۰ میلیارد با وحید امیری تمدید کرده و حالا با توجه به جدایی و بدون اینکه بازی کنه، ۲۸ میلیارد میگیره و توافق می‌کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/136988" target="_blank">📅 15:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136987">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/136987" target="_blank">📅 15:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136986">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/136986" target="_blank">📅 15:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136985">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
🔴
🔴
🔴
توجه به پیوستن محمدرضا اخباری، احتمال بازگشت امیر رفیعی قوت گرفته است. برخلاف اخبار منتشره، باشگاه پرسپولیس، با احمد گوهری و سایر دروازه بان هایی که نام آن ها مطرح است مذاکره ای نداشته
🔴
رفیعی به مدیران پرسپولیس اعلام کرد توافقی جدا شود و باشگاه به او…</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/136985" target="_blank">📅 15:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136984">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
🔴
پوریا لطیفی فر ستاره 22 ساله تیم‌گل‌گهر با عقد قرار دادی چهار ساله رسما به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/136984" target="_blank">📅 15:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136983">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">💠
💠
💠
✅
پرونده ایری و طاهری به حدی جنجالی و پرحاشیه شده که مدیران پرسپولیس فعلا هیچ رغبتی به توضیح ندارند
🌀
🌀
عصبانیت هواداران هم مزید بر علت شده تا برخی از مدیران ترجیح دهند اظهارنظری نداشته باشند.
🌀
🌀
وضعیت به گونه ای است که حتی جذب محبی هم موجب ارامش هواداران…</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/136983" target="_blank">📅 14:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136982">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
امیر روستایی مهاجم سابق پرسپولیس به سترة بحرین پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/136982" target="_blank">📅 14:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136981">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
شهاب زندی مدیرعامل نساجی:  با استقلال درحال مذاکره‌ایم، با توجه به بسته بودن پنجره شون اگه بر سر مباحث مالی به توافق برسیم این دو بازیکن آینده‌دار نیم‌فصل راهی استقلال میشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/136981" target="_blank">📅 14:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136980">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFsUwDyLa28WZVXBV8B1PphIT-QyToBFtay6k5OWaBXGouvqOTM6U0hof9McLvZaSoubsj9x0pYf-Gx6PMemBEOcU2-7QbpMAbs1zmJJpFgtZUHMlxMU78KfqorJhiP77lCG3pMWCsL64OAytxsaXjZkeXR69l71kISyxj__Lxt9y31MLaVM5H7h86nHA9das9W9AQz0I887BdBkNlhpxs5_zyAovMTz8MVPMmxqkX_z0m8NEq22en-hoZvuVgrYV3pNEMBoKSRuBS7gz-cugmLqWxnRmWfaBUqy4S04yfoX4IFjCFmdrr2_vBI37WvoqlQytvDSnoIhQFcgcd08YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرحله حذفی لیگ ملت‌های والیبال از راه رسید!
🔴
نبردی حساس و تماشایی بین ترکیه و اسلوونی در پیش است؛ جایی که هر دو تیم با تکیه بر قدرت سرویس، دفاع روی تور و بازی تیمی، برای کسب برتری و نزدیک‌تر شدن به هدف خود به میدان می‌روند. دیداری که می‌تواند با رقابتی نزدیک و ست‌های نفس‌گیر همراه باشد.
🏐
اوج هیجان همراه با وینکوبت، چهارشنبه ساعت ۱۰:۳۰ دوتیم ترکیه
🇹🇷
-
🇸🇮
اسلوونی به مصاف یکدیگر می‌روند.
🔗
برای پیش‌بینی بازی‌های لیگ‌ملت‌های والیبال با بیشترین آپشن ممکن همین حالا وارد ربات مینی‌اپ وینکوبت بشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/136980" target="_blank">📅 13:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136979">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
علی بازگشا، سخنگوی باشگاه پرسپولیس: «اینکه پیشنهادی آمده بی‌اطلاعم، اما ما می‌خواهیم اورونوف و سرگیف را حفظ کنیم.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/136979" target="_blank">📅 11:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136978">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔄
🔄
باشگاه نساجی: دانیال ایری و کسری طاهری رو دیگر به پرسپولیس نمیدیم. بانک شهر ما رو سرکار گذاشت. اگه با استقلال توافق کنیم اونارو به استقلال میفروشیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/136978" target="_blank">📅 11:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136977">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
✅
کسری طاهری رسما توسط نساجی رونمایی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/136977" target="_blank">📅 11:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136976">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">💢
💢
قرعه نه سخت نه آسون گیرمون اومده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/136976" target="_blank">📅 10:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136975">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">💠
💠
💠
تارتار دوست دارد در ابتدای شخصیت گل نخوردن را به تیمش منتقل کند که حریفان به راحتی دروازه تیمش را باز نکنند.
⚠️
⚠️
تارتار در مسابقات مختلف خطاب به شاگردانش تاکید کرده نباید به هیچ وجه گل بخورند چون وقتی تیمی گل نخورد شخصیت پیدا می کند همانطور که تیمی که…</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/136975" target="_blank">📅 10:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136974">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🗣
🚨
شیوخ ابوظبی اعلام کردن دیگه ایرانی‌ها جایی توی این شهر ندارن و محمد قربانی هم به این دلیل از الوحده کنار گذاشته شده / هفت ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/136974" target="_blank">📅 10:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136973">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
خالد در آستانه بازگشت به پرسپولیس
🔴
❌
مدیران باشگاه پرسپولیس بعد از منتفی شدن حضور محمدرضا اخباری در این تیم برای تقویت دروازه خود به دنبال جذب محمدرضا خالدآبادی گلر سابق استقلال و فعلی شمس آذر قزوین رفته اند
🔴
خالدآبادی سابقه عضویت در آکادمی پرسپولیس را…</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/136973" target="_blank">📅 10:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136972">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
محمدمهدی محبی احتمالا وارث شماره ۱۰ پرسپولیس خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/136972" target="_blank">📅 09:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136971">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBs3tpSdQzxMB_yeCOEeL6iLoFQOCGWuBDVoCzj1DAxjWpzUwodBNCm35m-BpMI8y5hnXHNM5p5Ux0DVc4ev4dEiL8_374gN5Px9KuCOnqcUndi7O19vnBWxfmGbxe9uRc4s7xMJYQBFAOz6SXf3CjLfy55-ZOj4i8W2MPPT_HKcXhA_zrkemgWmBAKe5gr969nC6JsE-jlyG6yriLTeBFH0dhIEaQq8zneLgSLOOQBoJcD3xQa9Ftnc10CjPj5SYKA6a0AAu8An-QZg80Nadn9tskm3hPGNCEoJ0LIclBKuaL6VBjijEXAd4-DYM-C1MUMKwK6jURSNmtDI3KnhTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خبرنگار ورزش سه حاضر در تمرینات تیم در ترکیه: اسکواد سرخپوشان همچنان ناقص است و احساس نیاز در پستهای دفاع مرکزی، دفاع راست، دفاع چپ، هافبک بازیساز، مهاجم و البته دروازه‌بان ذخیره احساس می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/136971" target="_blank">📅 09:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136970">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✖️
✅
سه گزینه نهایی مهدی تارتار برای جذب هافبک بازیساز مشخص شدند:
🔄
⏺
1_ فرهان جعفری از ملوان
🔻
2_ مهدی گودرزی از خیبر
🔻
3_ مهدی نجفی از پیکان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/136970" target="_blank">📅 09:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136969">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✖️
✅
سه گزینه نهایی مهدی تارتار برای جذب هافبک بازیساز مشخص شدند:
🔄
⏺
1_ فرهان جعفری از ملوان
🔻
2_ مهدی گودرزی از خیبر
🔻
3_ مهدی نجفی از پیکان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/136969" target="_blank">📅 09:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136968">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🗣
🚨
شیوخ ابوظبی اعلام کردن دیگه ایرانی‌ها جایی توی این شهر ندارن و محمد قربانی هم به این دلیل از الوحده کنار گذاشته شده / هفت ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/136968" target="_blank">📅 08:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136967">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIsDz090ZxJn8dtLg-lcnLM78xSDs6Lx3tNZbftnAbpB_o58P0ykjnN7LsbpUIQO098EYy9BAm2zvctkkPbpbY-spe2qjvzuH9bD0qgcwYdFGfcOG-8gSoxOGrjyORwGGWtUFpKrqCF5lPbZOiA7tDjat07b_QWsj-ZUw3P1XX1E7fdEiM5rDT6V6edu0OgMw0gRsspOFFE1qTvLxWyzrqowYMNZZH6k7dz2OktbPjGT1bHxk7qenWG__ET284BfmC7fA2tqhAQ4kY0f0bG2aP7YOlrZ7CCy0T_ONLUB_aKwhCDydVqn6y6bo7fb6ReyjiVgDOMieu-XkrOwJjDf4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/136967" target="_blank">📅 08:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136966">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBurtmWz0pJzP2etxcfPTdiFRGt2K72OHmIpDszCXgRx2rQ4MQ5-U53m_NvoFljx69W0-jcQZCIrg6zixGJ_NB2xpCYBVuW3rU1jCLb-s0U2pSRSPzyubbiB9lPg8R5WwJtiWI6X8TPr0ZDLWfxFXOYrTbwilVBkpSMeKG2YsvCZ6v8OCN8OHBxzwVmJSGG2RXCZmAL2pt6DlY-MI6f_Dlt3mYLjbvJ-dhEfGwDLr4hXxmsrAYoqrV4sI-vRiQv1PyqNB6edJJKY_DqENbwm0DNgiVKLKbbxXf91a8X8F8sYfxjm968c5S8quAbzThf4N70NJDGlcQnxJ-pZFF4Uug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرحله حذفی لیگ ملت‌های والیبال از راه رسید!
🔴
نبردی حساس و تماشایی بین ترکیه و اسلوونی در پیش است؛ جایی که هر دو تیم با تکیه بر قدرت سرویس، دفاع روی تور و بازی تیمی، برای کسب برتری و نزدیک‌تر شدن به هدف خود به میدان می‌روند. دیداری که می‌تواند با رقابتی نزدیک و ست‌های نفس‌گیر همراه باشد.
🏐
اوج هیجان همراه با وینکوبت، چهارشنبه ساعت ۱۰:۳۰ دوتیم ترکیه
🇹🇷
-
🇸🇮
اسلوونی به مصاف یکدیگر می‌روند.
🔗
برای پیش‌بینی بازی‌های لیگ‌ملت‌های والیبال با بیشترین آپشن ممکن همین حالا وارد ربات مینی‌اپ وینکوبت بشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/136966" target="_blank">📅 01:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136965">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⚡️
⚡️
قرارداد دنیل گرا با پرسپولیس ۶۵۰ هزار دلار است و این بازیکن اعلام کرده تنها در شرایطی حاضر به فسخ قرارداد خواهد شد که کل مبلغ قرارداد فصل آینده‌اش را بگیرد. گرا در مدت زمان حضور کوتاهش در پرسپولیس به اندازه‌ای ضعیف ظاهر شده که نه تنها باشگاه‌های لیگ برتری،…</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/136965" target="_blank">📅 00:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136964">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⚡️
⚡️
فوووووووووری
⏺
باشگاه خیبر خرم آباد رضایت نامه مهدی گودرزی رو 70 میلیارد تومن اعلام کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/136964" target="_blank">📅 00:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136963">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⚡️
⚡️
شنیده ها: با درخواست مهدی تارتار؛ باشگاه پرسپولیس فردا برای جذب مهدی گودرزی اقدام خواهد کرد
🔹
پ.ن: گویا خیبر هم مشکلی با جدایی گودرزی نداره و به دنبال درامدزایی ازشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/136963" target="_blank">📅 00:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136962">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⚡️
فوری از مهر
🔻
برخی از دلال سعی در فرو کردن قربانی به پرسپولیس دارن ولی تارتار گفته من چهار تا هافبک دفاعی دارم و نیاز به این بازیکن ندارم
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/136962" target="_blank">📅 00:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136961">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
شنیده ها :معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن باقی مونده.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/136961" target="_blank">📅 00:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136960">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🌀
🌀
🌀
اظهارات کنایه‌آمیز محسن خلیلی: تیم‌های دیگر هم دلسوز بازیکن گرفتن پرسپولیس هستن. برای جذب هر بازیکن تیم حقوقی ما بررسی می‌کنه تا محروم نشیم.
📎
📎
📎
خبرهای خوبی درباره انتقال یک بازیکن می‌رسه.
🤔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/136960" target="_blank">📅 00:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136959">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGOVUHzAbJFMYvnhQYjTK_HP7FewGHtl1k5BnE9J0H-wJ1pta5pGRWeUpit-AOfy8nJ-cKkqsRW8A569U6RWVsAVRRdxbh3tOmfYmi47XHzRksjZ8gKT2RyFqT2Xi5Jp8QM79QbF90u3QJZTpnEwOjN6_jPEmru7KhajL9v6wI3Nx6aoa_b9XXRkGDYLGmS7x3Fzpoeys4MSRaZTDQLX7WRlCYPVwhmgLZDWKYTw4aSXbx-kCeGXdzu-nQJVTVSmM7dLptZZns5RVC8wTs6zCaT1r0-2IO2cBb6HyrubbdaqOmxwJwaCX3YTLyaq_jPxqKc15PbZ5haZPerlm473cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
📸
سرخ‌ها در مسیر آمادگی؛ تصاویری از تمرین امروز تیم با حضور لطیفی فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/136959" target="_blank">📅 22:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136958">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
🔴
🔴
دو خبر از قدوسی
🔴
امیررضا رفیعی به احتمال زیاد در جمع سرخپوشان ماندگار خواهد شد
🔴
🔴
تراکتور مشتری دانیال ایری و کسری طاهری شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/136958" target="_blank">📅 22:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136957">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xn5t7_3oE-Cm3ujBS1HYlRiMxwb0LkPSW7R2c-Vxtmz_7UgaVZEsiXnSuVDfS4lg9BefXmZINdzO-L48EtPb3aieFJsfNUhBXMZnYlhRBNLEIusCWl1-w2yamlEhGZa-gHsjFIRSJKdPAdtFfObegf3Uf2qp3A869Z3WcIteZGELRFdY-388XRqTFkhDctCfxXI1zj8m3T4zy8nd6t3BO6P07MXzLV0pDkt4FT1otrwFaWszgMxVxvJOZZ8eJO2lK4pKe9bRV-DPdCOexVrQoqjNgRfW7Hp44Z4ybYAWAzWrt3kOiq7QPlbgzI8DCcoO7DR0VTlLZJif3_uQ0pxrhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
آلانیا اسپور حریف تدارکاتی بعدی پرسپولیس در ترکیه
▶️
با اعلام باشگاه پرسپولیس، شاگردان تارتار، روز پنج‌شنبه در دومین بازی تدارکاتی خود از اردوی آماده سازی پیش فصل در ترکیه، به مصاف تیم آلانیا اسپور خواهند رفت که خود را آماده فصل جدید رقابت‌های سوپر لیگ ترکیه می‌کنند. این چهارمین بازی دوستانه پرسپولیس در فصل جدید تمرینات خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/136957" target="_blank">📅 22:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136956">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⚡️
⚡️
خوش‌آمدگویی پرسپولیسی‌ها به محبی
🟪
🟪
کنعانی‌: بازیکنان جدید باید بدانند به چه تیمی آمده‌اند. خوشحالم محبی به این تیم بزرگ آمده و امیدوارم لژیونر شود.
🟪
🟪
علیپور: در جریان بودم که محبی چقدر دوست داشت به پرسپولیس بیاید؛ به او تبریک می‌گویم
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/136956" target="_blank">📅 22:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136955">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🏅
قرارداد سه ساله پرسپولیس با محمدمهدی محبی
🔴
محمدمهدی محبی، وینگر راست و لژیونر فوتبال ایران، به‌زودی با حضور در اردوی ترکیه، تمرینات خود را با پرسپولیس آغاز خواهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/136955" target="_blank">📅 22:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136954">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❗️
❗️
محسن خلیلی معاون تیم پرسپولیس: دیشب با یک مدافع جوان قرارداد بستیم. با یک مدافع چپ نیز درحال مذاکره هستیم. با یک دروازه بان نیز به توافق کامل رسیدیم و به زودی ایشان به ساختمان باشگاه مراجعه خواهد کرد و قراردادش رو امضا میکند.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/136954" target="_blank">📅 22:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136953">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
🔴
🔴
تارتار: حداقل ۴ بازیکن دیگه نیاز داریم تا کامل بشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/136953" target="_blank">📅 22:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136952">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
🔴
🔴
تارتار: حداقل ۴ بازیکن دیگه نیاز داریم تا کامل بشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/136952" target="_blank">📅 22:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136951">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⚽️
بیژن طاهری: مهم ترین دغدغه ما امروز جام قهرمانی لیگ برتر در فصل گذشتش، از سازمان لیگ خواهش میکنم جام قهرمانی رو به استقلال بده چون ما صدرنشین بودیم و حق ماست
😅
😅
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136951" target="_blank">📅 22:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136950">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⚡️
۸ خرید پرسپولیس در این فصل راضی هستید   پ.ن البته هنوز ی دفاع چپ و هافبک بازیساز و گلر دوم به شدت نیازه و جاش خالیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/136950" target="_blank">📅 22:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136949">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOEn9XRxR9SP78I4_ohePunBZb6CytnkCteKcGgZiD7E1KTcedvcpdTi8mhvk_uD1yIDaQ0DZUpx2JG1wWboVL_JnbCvlvZFJXVOp7O2BWFkao_9AMoDCig4banVEYnVRkwrwdctG1FcfJSXiz0R142Zy6rxDe6bni2Zxl6h_faV0MRiJJJJde7IQr4UtwEPPie9-7MlYabK6dx50RPpK-NXMUk_2gW0bJdixkw02qphsEzBGpfXHJBfnRmKHv4YbQ9iy9lvQpk0rkg1bT78o3ltO2d2dmxU2PhDoOvU3CAtOT71giQ7xj0V0LQg0ZOVHrFxld54FapPuh7-juUfwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
✅
کسری طاهری رسما توسط نساجی رونمایی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/136949" target="_blank">📅 21:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136948">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
🌹
رسمی؛ دانیال ایری به نساجی مازندران پیوست  پ.ن.... و همه سرکار بودیم و از کسی بخاری بلند نشد برای جذبش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/136948" target="_blank">📅 21:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136947">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✔️
✔️
میرشاد ماجدی، رئیس هیئت فوتبال تهران:
◻️
مسئولیت استادیوم‌های تهران با من نیست. ورزشگاه‌های دستگردی و شهرقدس برای لیگ آماده هستند، اما درباره آزادی هنوز تصمیمی اعلام نشده است. زمان شروع مسابقات مشخص نیست و به وضعیت جنگ بستگی دارد.برگزاری منظم مسابقات، نشانه ایستادگی در برابر تجاوز است. ورزشگاه تختی تهران بعید است به لیگ برسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136947" target="_blank">📅 20:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136946">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEVdf3PWNYaetn_zYWnFGlZzs2O35_Cr6lr1cZx8H49UQL1C1rVFi4CiSa-E3z4kq5iXEbmCrx2GmnKwZ548YTTHU_9SnBPF3DAYfSTBBAY9YNquH8qRmlYcYEnAY8viS4h6OZqgKzh_tR85GO5OJUMWoCfUvc2pL87upMz6mXAnBJ5CCRd1JJ-g-pv-hpH7ne2qhVSvFeNYMQAy3adABqeU7ByM0YoIkAPRsa9ZpnAfOaBK4vItcrW4cwMH1oOnVy3UQf6lcTn2omULgO-L7o25pIrWtVAnePv62-Wi-MOIocsKgcKWB9s3FDmfBDBREw0rYFE53Bj6g2A7Z30Q1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
⚠️
امید عالیشاه به ذوب‌آهن پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/136946" target="_blank">📅 20:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136945">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaI4oyPhNW6-2jPA5YeGZpZtuxezY3RcrzKZ_NJGVnCwFDBhVyhESQ1KGZvhbZL1BLKJ2oTa8B6CG4qtXUWecRoMlPbbPsKVK6RiE2P8J4AkQPlYTGo0bPNCcChN36fNXhXBtwSJ2BGk2_zo4Ta2XxsMPJdZ7Gp5c28aw_XTHxEZZKgf0seKxb2YhrHN7zgIy5gwAlzRWv3Ljq48MZncRNAdsRWFB5fU7KlWBswB_nmLreVjcmf3oprfEmMttZjM2qakxNEg_e6-TvVSKmg0-cNTird-c220a2XQ2xdMTgeMpru2a8w5dUkffXDN868pj8Qto43VKyBp_OfigSP6YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🌹
رسمی؛ دانیال ایری به نساجی مازندران پیوست
پ.ن.... و همه سرکار بودیم و از کسی بخاری بلند نشد برای جذبش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/136945" target="_blank">📅 20:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136944">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HB8F8W1iXqYXXbd862x7487cNERAaIIzdh63NexepV2iaGLJP-sE3EYRguAWq6JgTSCAonnhGyc2oiRmR28O2bZ5XFmMyVkkd1lR1Tg_J7Y5kAiuF4mGE_SiSScHv4FW4HNrQWMi7VRYtKbXmt3ZEhAbICjlGyTowWWAvubvN_QUNC357Y2C6yeKqnx_VSZEypR6BGTvKHThEZt1qbDu7GNbmsuvNh7qO69PzkJ7x7tIDZ9vOMlzo1syMu7-DAYkdUv9sPfRwh2X53fuRefC3X0Pvg5eee9QTLSsUHGDh9qzFrSoWsXCPy2AIGvHCLY_HCGfRaa44pdOZh4-1kzxCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
امشب خبری از شانس نیست؛ اینجا فقط جسارت، تمرکز و یک تصمیم به‌موقع برنده را مشخص می‌کند…
🎾
امشب یا فیلس دوباره قدرتش را به رخ می‌کشد یا جودار انتقام باخت در تور بارسلونا را خواهد گرفت.
🎾
Fils -
🎾
Jodar
1⃣
هر گیم می‌تواند جریان بازی را زیر و رو کند.
2⃣
هر بریک‌پوینت می‌تواند معادلات را به هم بزند.
3⃣
و فقط کسانی که زودتر تصمیم می‌گیرند، از بهترین ضرایب استفاده می‌کنند.
📌
مسابقه را فقط تماشا نکن؛ از هر امتیازش فرصت بساز:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/136944" target="_blank">📅 20:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136943">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔵
🇮🇷
باشگاه نساجی مازندران انتشار این ویدیو از دانیال ایری مدافع جدید این تیم رسما رونمایی کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/136943" target="_blank">📅 20:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136942">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=YS5nY3ztmCoypapeh7NfD_fxn0g-TUfJ1cF581eIzY86h3oeO_kBYO1GIHlHw7JW-EfrPxYuHRWQ-OHqZn3WTftFvsL7dinL9Sp8-rwggUJbeFPyfPPV8dBCJAOcDbAMuLcqS0uehGHwpMtPC1dLZkcZwZT_GeeJu_Nq5By3GC-H7wclM50wukfzQRR72fuhcGQuxrnzvS-MXHkbDU5gJ9IC6W87MzzEeEJQlfj6IGJ2rm-DwUnwnHX41NjUiIXdf66z-23wz8b46PpknMe86zJxsp_6wJnme7-yzgNtJb6QQ651S_Ub7TXgRfp9agqSA3-rsyVcS4Vt4TcHM4P0Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=YS5nY3ztmCoypapeh7NfD_fxn0g-TUfJ1cF581eIzY86h3oeO_kBYO1GIHlHw7JW-EfrPxYuHRWQ-OHqZn3WTftFvsL7dinL9Sp8-rwggUJbeFPyfPPV8dBCJAOcDbAMuLcqS0uehGHwpMtPC1dLZkcZwZT_GeeJu_Nq5By3GC-H7wclM50wukfzQRR72fuhcGQuxrnzvS-MXHkbDU5gJ9IC6W87MzzEeEJQlfj6IGJ2rm-DwUnwnHX41NjUiIXdf66z-23wz8b46PpknMe86zJxsp_6wJnme7-yzgNtJb6QQ651S_Ub7TXgRfp9agqSA3-rsyVcS4Vt4TcHM4P0Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇷
باشگاه نساجی مازندران انتشار این ویدیو از دانیال ایری مدافع جدید این تیم رسما رونمایی کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/136942" target="_blank">📅 20:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136941">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">#شفاف_سازی
⛔️
در خصوص محمد قربانی خیلی هوادارا میگن بخاطر اینکه تراکتور تقویت نشه ما باید جذبش میکردیم، اما بودن خدابنده لو،باکیچ،پورعلی و لطیفی فر به هیچ وجه قابل توجیه نیست جذب قربانی
🔴
البته باشگاه قبل از جذب پورعلی و لطیفی فر برای محمد قربانی نامه زده…</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/136941" target="_blank">📅 19:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136940">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCfe7l-YsIZhLKruyQPBQd80lQ8Yg5OG1wU0BrtCq5OvNz3_xWJwRzEmF9P9e5hLzRiahIAgt3E14OxVglNNTTaEe2TN3yomXm5CM3EAxTp9CfyJqswaixqmH6-dDTZQ4JdbpFuioMEwDBZSQVbXzQOwP089VdojbJyn5OLtwY6-qzeYeyKsdT96scvbM3YxPpnX8eORPiNY7KI1hnMnqb6bQyqTip1y1kVDfEDegVTMfkT5wnIR9lEFtXWRul050Pz8Yi2lzJOO_A5nmMUi7Y5RrBmF9IfkkltmyVezNO8K0vCLmJ6obyvtf1DInkzytRviIqxEDNASTXdO5ahauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
درصورت عدم جذب دفاع چپ، از همایی فرد برای دفاع چپ استفاده میشه
😕
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/136940" target="_blank">📅 19:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136939">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⚡️
⚡️
#مهم | ادعای جدید ترامپ:
🔻
ایران در حال حاضر با ما در ارتباط است تا به توافقی برسیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/136939" target="_blank">📅 19:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136938">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnNAhqPAoJhEq-rvjkkWeCueAm5Ave96Y_2FguvINd5Y_gCN2HPpy34ghaWKuAlNrt6FvPqEVdbTTBAWXXWEJMYy1vloAvNo04MuZ9zybe8SgLbQS9Zc87Ye0XHewPwXtV4088qRMd2gU48tMzLByfpfhL_eOM-upMt1kCkjYUWa3aid4UznbpC3_eGoDlAlD3QGtlau9w9eoUcl_YhMoByCW6n0tDuGjKgX_6sb7aBCGQ0WoZ2UjpgYdLJyZlBmZJeGM_iQMJUOoulr5EtNIqvhamW-Bs217QXCl4jFOcNQjq20h-ie8Z65RcsJmIS-gnW9BFHUnq5yZ5jsc1-Kmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
۸ خرید پرسپولیس در این فصل راضی هستید
پ.ن البته هنوز ی دفاع چپ و هافبک بازیساز و گلر دوم به شدت نیازه و جاش خالیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/136938" target="_blank">📅 19:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136937">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🏅
قرارداد سه ساله پرسپولیس با محمدمهدی محبی
🔴
محمدمهدی محبی، وینگر راست و لژیونر فوتبال ایران، به‌زودی با حضور در اردوی ترکیه، تمرینات خود را با پرسپولیس آغاز خواهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/136937" target="_blank">📅 19:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136936">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c4177448.mp4?token=un_8ksBW_23NrexWl0W1uaQwyTno4f-XuWwjxS2OUrWYPyksE4UuiPv4-mLrDwVhvTFSzM6DVCVTIctR6NTHFyo95wSdNkm9MT7_8IR_ZJrHN3P6_a1U4mxKeVNJ5_ikKMsNz1GAlotAHT3_YnZNqnhZ5a3UZxmmu3ZRqhix4xv1YWFMHsMOEwm1ZXn1y6CeBrV9mbhoXBxD47NuvXcOAemyka7hCvuZlRv6avyzl3LHRKBGpTKGEZWNliqEo8yY2sfMCMehvTJsOK_Gj9v_1fkv5-DzOnbQwx3LMXGbpV4CMjV2dvvR1sE3AYABsLTeTkENeLSEiQE8jHrKI8-BOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c4177448.mp4?token=un_8ksBW_23NrexWl0W1uaQwyTno4f-XuWwjxS2OUrWYPyksE4UuiPv4-mLrDwVhvTFSzM6DVCVTIctR6NTHFyo95wSdNkm9MT7_8IR_ZJrHN3P6_a1U4mxKeVNJ5_ikKMsNz1GAlotAHT3_YnZNqnhZ5a3UZxmmu3ZRqhix4xv1YWFMHsMOEwm1ZXn1y6CeBrV9mbhoXBxD47NuvXcOAemyka7hCvuZlRv6avyzl3LHRKBGpTKGEZWNliqEo8yY2sfMCMehvTJsOK_Gj9v_1fkv5-DzOnbQwx3LMXGbpV4CMjV2dvvR1sE3AYABsLTeTkENeLSEiQE8jHrKI8-BOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
بیژن طاهری: مهم ترین دغدغه ما امروز جام قهرمانی لیگ برتر در فصل گذشتش، از سازمان لیگ خواهش میکنم جام قهرمانی رو به استقلال بده چون ما صدرنشین بودیم و حق ماست
😅
😅
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/136936" target="_blank">📅 18:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136935">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZufqot9bKAlvptzBECkGlDQTyMsaesRyhd3XlWLcBHAhdhDjHUXmujFnXZE8gz6bqm-HslWWrbTnBFbOSmHdCcOKFSA7IbIUzkJ6VhmmthoEyIEyLi9Xx5TOYBDJHaN-9KxVEL4q8knSpyX_sb4a01wdE1Hzx1p9kiLV3jxYxo9dsfKBZl2VuwlZ8k-DqhGfiCJBuLMnf7puVnTs_UVEZbbkmr9mAV6n_r-wksmjc8Q2V0o5QOxD1UuHW8vRreUS99AYzxkp_MCxkJRsVg8fVxYfD_RCCm46L-6Ouf-AITbp2vTONKUpStpTocSt4lm8fiHBH8110y57fd1lolOIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
قرارداد سه ساله پرسپولیس با محمدمهدی محبی
🔴
محمدمهدی محبی، وینگر راست و لژیونر فوتبال ایران، به‌زودی با حضور در اردوی ترکیه، تمرینات خود را با پرسپولیس آغاز خواهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/136935" target="_blank">📅 18:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136934">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
❌
❌
حریفان پرسپولیس در نیم فصل اول:
✔️
هفته اول: شمس‌آذر
✔️
هفته دوم: اس‌خوزستان
✔️
هفته سوم: تراکتور
✔️
هفته چهارم: ملوان
✔️
هفته پنجم: استقلال(میهمانیم)
✔️
هفته ششم: ذوب‌آهن
✔️
هفته هفتم: خیبر
✔️
هفته هشتم: صنعت نفت
✔️
هفته نهم: مس شهر بابک
✔️
هفته دهم: فولاد…</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/136934" target="_blank">📅 18:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136933">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🏅
قرارداد سه ساله پرسپولیس با محمدمهدی محبی
🔴
محمدمهدی محبی، وینگر راست و لژیونر فوتبال ایران، به‌زودی با حضور در اردوی ترکیه، تمرینات خود را با پرسپولیس آغاز خواهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/136933" target="_blank">📅 17:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136932">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKl6y7mOqldujl8dbkmJShtZVheoUO3W6ek3pYCIjIzzlNPeIWMi8sZgi1BdIPqYvGhTiiFDe-Z5pM_7PwWz2kw-oNPvazLed6m8ay1hK_SCy6FofQL-8TtxjR4LwTG9_ie6k2L9OrppIpYfI8ZpMH8SZrM-W02tZCiMhvhIKHRPmks7S8RoXTpGH7dAWNMzIXnHRNGa1PTfvhEyzxwycMyOpGaams029JY64GOIMQh-T-VtcbLLyk0lCCsvcsDLeRVHZNYPON-ZMWkggQsqU8_DwWnHW9LuEyq-y83TLsioS-gAvivzDbVYNWgoTHcgm-zvsIRfD4TXyYRkJ77xhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی
⚽
💥
حدادی منتظر پاسخ محمد مهدی محبی؛توافق با کلبا انجام شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/136932" target="_blank">📅 17:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136929">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
❌
❌
حریفان پرسپولیس در نیم فصل اول:
✔️
هفته اول: شمس‌آذر
✔️
هفته دوم: اس‌خوزستان
✔️
هفته سوم: تراکتور
✔️
هفته چهارم: ملوان
✔️
هفته پنجم: استقلال(میهمانیم)
✔️
هفته ششم: ذوب‌آهن
✔️
هفته هفتم: خیبر
✔️
هفته هشتم: صنعت نفت
✔️
هفته نهم: مس شهر بابک
✔️
هفته دهم: فولاد…</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/136929" target="_blank">📅 17:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136928">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⚡️
⚡️
آغاز شد پخش زنده از شبکه ورزش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/136928" target="_blank">📅 17:09 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

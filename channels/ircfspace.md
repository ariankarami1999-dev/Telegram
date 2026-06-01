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
<img src="https://cdn1.telesco.pe/file/MtF01J1Yp4u9dpmlVqOLkrtJFCx_EifpNUMLydSC1d7EuwX-houH1j5BjKLfM9OTyFygljyxw9628zQmTy-DTJDcAePvQbC2K_3SKyv6hRks74Ml6VFQ_QGxgUSVT1OhSeWC9eBuOM2kNoYDmk7jyXGKE5iSFgVcPi_TwmBn2OLRU_3C41sr2xrVuQny5W2MMV0Kspv9A8IKr-fwKuOWE_wxxtf0w192mRwl4fk17NIjJcuJ-lwI5V5uQtvMvRqn6-XUzjuGtedy-CFZ4u_DxiN3i5ErlKuxvEFxt2SwHrZAgk8p6DZ1z06xFRoGYwyWCCSTkVjXvrz0eXmOEb_W2Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97.8K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 07:45:52</div>
<hr>

<div class="tg-post" id="msg-2410">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وضعیت قطع اینترنت طوری شده که همدستان فیلترچی که روزی روزگاری با هم عکس یادگاری میگرفتن هم به شکایت رسیدن.
یک سیستم فاسد همیشه به سمت فساد بیشتر میل میکنه؛ در ادبیات فنی بهش میگن فیدبک مثبت. یعنی سیستم هی فساد خودش رو تشدید میکنه و در این مسیر بیشتر و بیشتر از آگاهی تهی میشه.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/ircfspace/2410" target="_blank">📅 19:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2409">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/irqZJiyws0ywU6S8rj5CNDnJt-BJ-kfS66uKsWtLWPN3H-soHRvszZjlCgSst0F5rkDcn-5goNX4mnQ7Us6RVX6OCx-Sasf6zg0jWZ19R-bcoPpxj9UxREcj7Vl17ys1AT3SKtd9rDhulblkwVbb3BMhKnzozTv-6VEB9H4pnwOhMDZGsWg0sfENi9IAhXyLR-VHqGxl8jD2pSC6pCN5FAXvDjqF_jfXVwuZYLu0mez33Dcn-LKPh1dJtAyC_YYxMqPibpE_s3d1p0KsM_Ex8ZjeU6jhMIsreDhbTVqon1qLPpY3F3p_QDbuH06DKJfrIf5MQlzzVNXaziUnm1wPAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صالح اسکندری، عضو مؤسس و عضو شورای مرکزی شریان، در خبرگزاری فارس کمپینی با عنوان «گزینه قطع داوطلبانه دسترسی به اینترنت بین‌الملل را فعال کنید» راه‌اندازی کرده است. این کمپین طی پنج روز گذشته تنها حدود ۳۴۰ حامی جذب کرده است.
در حالی که میلیون‌ها ایرانی برای کار، آموزش و ارتباطات به اینترنت جهانی وابسته‌اند، ترویج ایده قطع اینترنت بین‌الملل بیشتر از آنکه همسو با نیاز مردم باشد، نشان‌دهنده فاصله طراحان چنین طرح‌هایی با واقعیت زندگی شهروندان است.
©
alirezaer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/ircfspace/2409" target="_blank">📅 19:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2408">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V7ZNupi2eWwEBjfJMIkFmRdocrdUns75HDj-EE292SrbVhvvrnqQbC7QdJYzUD5DtGoDH48cSFrRYLq1XyTvP2rbYNbGKO_8XXbefcBedjJKet24A8vLG0emgDj08oxgpiizclTnd2JppTQXGG3hUvCK6_LuL0MIGGuRYzQkh_qnI9jFEcEUaiA7JdKkdr02z4Tw-8KcFzb_BkLu9bn5ICbEAMskAv23mc5g21e23M6X_uuN8WI8DPdEUvnGnpkm8jjZCljPf292Y3nw0kbY2pqR4l89ciX9fZSr3E0LhGbUsTNfl_LJiI3bHVBEFdMny_ftoWOs12PFFNel02AsFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ SenPai Scanner یک ابزار متن‌باز برای پیدا کردن IPهای مناسب کلودفلر در ویندوز، لینوکس و مک هست، که با تست عمیق از بین هزاران آیپی مربوط به محدوده‌های رسمی، اون‌هایی رو پیدا می‌کنه که هم پایدارتر هستن و هم کمترین تأخیر و مشکل ارتباطی رو دارن؛ تا بشه در کانفیگ‌های واقعی ازشون استفاده کرد.
👉
github.com/MatinSenPai/SenPaiScanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/ircfspace/2408" target="_blank">📅 12:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2407">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cu56ck9QYAEdm5NTrlDeZlNwUeJbBgOAwY3kAfFJzpmMzg921rpihmgGd7sH-FH5ZsrBOXQlhwuyWFoSZjK_at94ZkqTsQ2KEYE7vhqg9-h0r1ICSw7V1W_2MxUZ1Z4sv9aWZbIaOsz15cXdLuyfatFlDgdDF-iZksxx4O8u8cZ44ZCnFEmCcw9fqoqgGgOxV_Ysxfhkil0I6AkcNZNOBM8uFcHvexS7hyMr4u-XSB82axBJoP7siLKh_UyUTYdXq8UGLuVLMsAumXbLy8c3VMjvgimLSECpZd8LwOoyR5mkDFs7XRomuZrcyaKgUd78NyV-4EpMEjWALUfIOOpcpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ SpoofGUI یک نسخه گرافیکی برای SNI-Spoofing در ویندوز هست، که از هسته‌های Xray و Sing-box برای مدیریت ترافیک خروجی استفاده می‌کنه. این ابزار در اصل برای اجرای یک مکانیزم محلی SNI Spoofing طراحی شده که به کمک اون می‌تونه مسیر ارتباطی بعضی از درخواست‌هارو به شکل کنترل‌شده دستکاری کنه.
در این برنامه کاربر می‌تونه فرآیند SNI Spoofing رو فعال یا متوقف کنه و وضعیت اتصال‌هارو به صورت زنده ببینه. همچنین امکان مدیریت چندین پروفایل مختلف برای Spoofing وجود داره، که در هرکدوم میشه تنظیماتی مثل آدرس و پورت اتصال، IP مقصد و حتی SNI جعلی رو تعریف کرد و در نهایت بین اون‌ها سوییچ کرد.
👉
github.com/ZethRise/SpoofGUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/ircfspace/2407" target="_blank">📅 12:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2406">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OBxTD-RSHrNsSCKIfY9MhyWhK9hn9iTEu8ztPN_Z6EQhEVZhyZBFX8SAqch6_8LUlsfxBr8Hzbdn0nY_NJH8-DjxKoj8C9ioOCBkvyZBRYskb95UOjoxmawhjMmhDkuPrwzO4XkdlE9b6Qhe4ZQbSJd1rmyMrOhOQWs8xnS-EQbU1zKNqBGjxTffrslPPpNyttEn5HPbtLfsULDZAyePKkNwpOqb3wCwVO5ymcSCcHvG_2MhSfToTM61gwvfKwO-YM3kMZc5iD7zcSeSor_VAMmuODaaLfK6_2unp1y9pULBvaHBM7_rKhbb9wJ8B3WIn_OjGZJ6cIByYDmF2lyU3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر CrimsonCF یک وب‌اپ برای اسکن سریع IPهای کلودفلر هست، که آیپی‌هارو با L4 TCP Handshake روی لوکال تست می‌کنه و خروجی‌های آماده برای Xray, sing-box, Clash میسازه ...
👉
github.com/amir0zx/CrimsonCF/blob/main/README.fa.md
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/ircfspace/2406" target="_blank">📅 12:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2405">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mtkpzRet6XYkBwIvZQx4vWyar-rTz4nm6cTI2c17itLU1YyEm9SkNrTyrLnmfCD84rR3trPrLyvY-UsnTy2R0XBGhxoTdFAPrEVSxRajKCo6qjLoqKGQLhZl4pi8AcsT_KpUAPziVV2E2PHanTCuK8oZzrj8Q_kizlDJc9rX82b6Tl7ddhI_BD_HDGtIo0fxKM0tboXIU7gi0in3EdcD8zkU4gJV4bDFkD3cdLCRQSJ6FMwK7DIpUvvuo4bYyY8AAixiQA3_gy6I47moD3u98Iz7hhk8gcg9oC4SdRR8flfL80wzUWYV1xrEQzerA95SQvkbBX0erG_mdvekyG47OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتماد به نفس اگه اپلیکیشن بود
©
mansheyeh
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2405" target="_blank">📅 10:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2404">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اینترنت صرفا برای توقف روزشمار نت‌بلاکس وصل شده، یا هدفتون برقراری ارتباط بوده؟
چون با هرکی صحبت می‌کنم تقریبا ارتباط پایدار نداره ...
©
ArashNalchegar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2404" target="_blank">📅 19:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2403">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اینترنت در ایران آزاد و عادی نشده. بیشتر مسیرهای خارجی یا بسته‌اند یا نیمه‌بازند. فقط بعضی مقاصد و مسیرهای خاص اجازه عبور دارند. همین باعث شده فیلترشکن‌های معمولی خوب کار نکنند.
در این میون بعضی از افرادی که دامنه‌ها و مسیرهای سفیدشده دارند، دسترسی می‌فروشند. نتیجه‌اش هم شده اینترنت نابرابر، رانتی و پر از راه‌حل‌های موقت. انگار که درب ساختمون رو کمی باز گذاشته باشن که هوا بیاد، اما اجازه ندن کسی ازش رد بشه.
برای همینه که گوشیتون ممکنه نشون بده که اینترنت دارید، حتی شاید اولش سایت یا اپ مورد نظر رو باز کنه یا بهش واکنش نشون بده، اما در عمل از اینترنت خبری نیست.
©
nimaclick
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2403" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2402">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تقریبا اکثر IPهای خارجی خاکستری هستند، یعنی در هر کانکشن شما مجاز هستید حداکثر ۶ پکت به سمت سرور خارجی بفرستید؛ این محدودیت به شدت سختگیرانه است و تقریبا هیچ سرویسی نمیتواند با این محدودیت کار کند. به طور مثال برای کانکشن‌های Https صرفا میتوان یک ریسپانس ساده Http را دریافت کرد و  شما حتی نمی‌توانید درخواست دیگری بفرستید.
برای بعضی از IPهای خارجی خاکستری مثل IPهای CDNها و ...، SNIهای محدودی سفید شده، یعنی اگر شما یک درخواست TLS با یک SNI سفید به یک IP خاکستری ارسال کنید، آن کانکشن سفید میشود و می‌توانید به صورت نامحدود پکت ارسال کنید! به طور مثال با اینکه الان تمام IPهای کلودفلر خاکستری هستند، ولی اگر شما یک درخواست با SNI سفیدی مثل
www.speedtest.net
ارسال کنید، کانکشن سفید شده و محدودیت ۶ پکت برداشته میشود.
در حال حاضر SNIهای سفید به صورت وایت‌لیست بسیار محدود هستند. با وجود میلیون‌ها وبسایت میتوان گفت عملا اینترنت همچنان قطع است و صرفا دسترسی به سرویسهای خاصی امکان پذیر است. حکومت برای بهبود کیفیت اینترنت مجبور است بسیاری از دامنه‌ها را بدون بررسی دقیق به لیست وایت‌لیست اضافه کند؛ به طور مثال الان تمام دامنه‌هایی که در لیست نیم‌بها ثبت شده‌اند همگی سفید هستند. نکته‌ی قابل تامل این است که اکثر این دامنه‌ها را فیلترشکن فروشها ثبت کرده‌اند (زیرا قبلا شما می‌توانستید صرفا با بالا آوردن یک وبسایت فیک و ثبت درخواست، دامنه خود را در لیست نیم‌بها ثبت کنید). بنابراین فیلترشکن فروش هایی که دامنه‌شان را در لیست نیم‌بها ثبت کرده‌اند حالا دارند سود خوبی به جیب می‌زنند.
این سیاست‌های بستن و وایت‌لیست کردن اینترنت موجب رانت و فساد زیادی شده و شک نکنید که خشم خدا را در بر خواهد داشت.
تکنیک SNI Spoofing باعث میشود که یک SNI فیک توسط فایروال دیده شود و کانکشن سفید شود و محدودیت ۶ پکت ارسال برداشته شود. روش اولی که منتشر شد اکنون در بسیاری از نت‌ها بسته شده (یعنی فایروال SNI اصلی را می‌بیند)، ولی طبق گزارشات همچنان بر روی ایرانسل و بسیاری از مناطق حاشیه‌ای برقرار است. روش دیگری که آن را Plan B نامیده‌ام، دیروز (با تشکر از دوستانی که نکات فنی خوبی را متذکر شدند و باعث جرقه ایده جدید شدند) با موفقیت تست شد، ولی به ۳ دلیل فعلا قصد انتشار ندارم؛ اول اینکه بسیاری از فیلترشکن‌های رایگان اکنون وصل میشوند (به طور مثال سایفون به راحتی با فستلی وصل میشود)، دوم اینکه همانطور که گفتم روش اول همچنان بر روی ایرانسل و بسیاری از مناطق فعال است، و سوم اینکه بسیاری از سرویس‌ها مثل اینستاگرام، واتس‌اپ، یوتیوب و ... به طور مستقیم با MITM در دسترس هستند.
©
patterniha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2402" target="_blank">📅 19:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2401">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اینترنت در یکی از بحرانی‌ترین وضعیت‌های خود قرار دارد!
اکنون وضعیت اینترنت در کشور به یکی از عجیب‌ترین و ناپایدارترین حالت‌های خود رسیده است. در حالی که بخشی از اینترنت بین‌الملل برای کاربران خانگی و شخصی برقرار شده، اینترنت دیتاسنترها که بخش اصلی زیرساخت کشور و میزبان بسیاری از سرویس‌ها هستند همچنان با اختلال و قطعی گسترده مواجه است. همزمان بسیاری از VPNها از کار افتاده‌اند و شرایط اتصال نسبت به زمانی که اینترنت کاملاً ملی شده بود، برای بخش زیادی از کاربران حتی دشوارتر و بی‌ثبات‌تر شده است.
کاهش شدید پهنای باند و افت محسوس کیفیت اتصال باعث شده دسترسی به سرویس‌های خارجی و حتی داخلی با اختلال و کندی همراه باشد. از سوی دیگر، گزارش‌هایی از بروز مشکل در گواهی SSL برخی سایت‌های مهم و حتی سرویس‌های دولتی منتشر شده؛ موضوعی که می‌تواند امنیت اطلاعات کاربران را تحت تأثیر قرار دهد. همان‌طور که قطع اینترنت فوری انجام شد، وصل شدن آن هم می‌تواند فوری باشد؛ اما فعلاً روند بازگشت به‌شکل قطره‌چکانی پیش می‌رود و همچنان بخش زیادی از کاربران و سرویس‌ها درگیر محدودیت‌ها هستند.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2401" target="_blank">📅 19:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2400">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">توی یک لحظه دسترسی مردم رو قطع میکنن، بعد میخوان به همون فیلترنت سابق برگردونن میگن این روند تدریجیه!
مشت‌مشت خاک بر سرتون.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2400" target="_blank">📅 15:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2399">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vhWPRXcdUKv9hBwg7UYM0XN63nuRC658H9R9b37usE1cCjb6kyxe9RYGUU9qe9emL4Rooe4zjybEgIlPedpLP0plFfS9G1HUiScN5LA-NH21z6HcrR5JjNKh9K1UNAhll2WAv0VNb3WlodXeXfKsSRoDTdUjawa02uIv60b4R2vsXNkkbgRyMEj3ReusIDVJ1x71eqi-C_4dqD7eeZxsTZ27dTVftniMFv20aYZbh9ISYUq9KbPzxbuDdyffPHGwsU6x5O4UdMVR531e9aFR45DoZZDnlYY1tzOtw2tmIGxpo0dL9U2MaHfNoFkUTakIg5USEDLv8UqVUElsJV3C4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جدیدترین بروزرسانی از فیلترشکن رایگان و متن‌باز
#دیفیکس
فرایند دریافت کانفیگ از API بهبود داده شده، متد CDN Fronting رو به‌همراه اسکنر داخلی به بخش روش‌های اتصال اضطراری در قسمت ترجیحات اضافه کردن و همچنین روی بهبود عملکرد، افزایش پایداری و رفع چندین مشکل گزارش‌شده در نسخه‌های اندروید، آیفون و ویندوز تمرکز داشتن.
👉
defyxvpn.com/download
💡
t.me/PersianGithubMirror/5676
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2399" target="_blank">📅 10:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2398">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZqS_2i94112e2gfjxTZl0wM000s7XCp0KFc_daqYbDDYaJrWQAGSk37Wzs1XCOLNTQKyAmnTqtm15tx2uUhyjYswqVgOZ0lBBq7uNnzrwwggD_MgRMOlY2Jv-FqEPwsAZVdSZpAdKo9jDPfOVOrFWFZRgrpkn-YGbizzIyD3dhDW3TjaaFYYmpDYamZTjj0Vf03f8hQdl6c2P3wyiBULgueQswt1_3EJjRFdapFd6o3EqKYx_tTr_WHxFO9_OmpqxbyCQ5eh_o320J1NhxtIuqYDQ8_R81JQIcbp0oD9kSEx-gCubmRk2CwDvsD0mNCXyHreWFA0W7xSDfMWQb1WQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در بروزرسانی جدید از کلاینت NexaTunnel امکان پشتیبانی از کانفیگ‌‌های Xray در کنار Stormdns, SSH over VPN, WhiteDNS برای iOS فراهم شده.
👉
apps.apple.com/us/app/nexatunnel/id6766783641
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2398" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2397">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رئیس کمیسیون تحول، نوآوری و بهره‌وری اتاق بازرگانی تهران گفت: خسارتی که کسب و کار‌ها و به‌ویژه فعالان حوزه اقتصاد دیجیتال در این مدت متحمل شدند، اصلا قابل جبران نیست. /ایلنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2397" target="_blank">📅 19:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2396">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">این اینترنتی که وصل شده داره نمی‌اینترنته ...
©
okhtapoos80
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2396" target="_blank">📅 19:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2395">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ikUHtZ1uJMEkwDikGvSzozq2fH5BQx3VUGvduMnzEZQt10wFQW6WwB9uDVw1VJUCbYI6bpoMBzHI65N5-Z-PzmviCLrCejtogFyFXg65pGd9W2rP-VTgskGj6vqt91LgACg9mTU3RmPSvKgv3bBE7Bx1iEoPtHgDlJV9BVaF4tdRpWFW_Ih-VIZgAiRW1-pF89enNo-r1FUSSr7ZwtX47M-n1nOeM-0E9Q_BmTqhTh_1N0H49WuzgOD9HTztEvadVSJ6j41ePuCLaeF1byVQ7bVmg-1dROZ8BbtINJ73OWoQaFu9R9W4FG7XOAPDqVAsalDc3qHua24uKISPPPElOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمانی که اینترنت در ایران قطع بود و تیم رسول جلیلی موفق به مسدودسازی Signature وارپ شد، اپ رسمی کلودفلر بروزرسانی جدیدی داد که حتی رابط کاربریشم تغییر کرد. آپدیت جدید این برنامه الان روی بعضی از سرویس‌دهنده‌ها داره کار میکنه، هرچند امیدی نیست که در محدودیت‌های شدید بعدی دووم بیاره.
برنامه‌هایی مثل Oblivion که بر پایه وارپ کار میکنن هم تا زمانی‌که هسته‌های وارپ‌پلاس یا وی‌وارپ بروزرسانی نشن، کار خاصی ازشون برنمیاد.
👉
one.one.one.one
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/ircfspace/2395" target="_blank">📅 08:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2394">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بعد از وصل فیلترنت یا همون اختلال‌نت، اکثر VPNهای متن‌باز و رایگان دارن به روند آپدیت‌های منظم خودشون برمیگردن. تجربه قطع کامل اینترنت در ایران احتمالا به ابتکار عمل بعضیاشون کمک کنه، تا بتونن در شرایط سخت بعدی کمک بیشتری انجام بدن. به مرور سعی می‌کنم بروزرسانی‌های جدیدشون رو اطلاع‌رسانی کنم.
👉
t.me/PersianGithubMirror
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2394" target="_blank">📅 08:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2393">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دسترسی به اپ‌استور و گوگل‌پلی روی خیلی از سرویس‌دهنده‌های اینترنت باز شده. احتمالا خیلی‌هاتون دیگه حتی حوصله وب‌گردی رو نداشته باشین، ولی توصیه می‌کنم وقت بذارین و حتما برنامه‌ها و دیوایس‌هاتون رو بروزرسانی کنین. حتی سایت‌هایی که دارین (از جمله مواردی که با وردپرس بالا اومدن) نیاز به آپدیت‌های فوری دارن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2393" target="_blank">📅 08:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2392">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بعد از ۸۸ روز قطعی کامل اینترنت، جمهوری اسلامی اینترنت رو وصل کرد. فقط یه مشکل ریز داره: فیلترینگ انقدر لایه‌لایه و سنگین شده که عملا فیلترنت ۲x پلاس رو باز کردن، نه اینترنت رو، و همین فیلترنت پراختلال رو به اسم بازگشت اینترنت دارن به عنوان دستاورد دولت تبلیغ می‌کنن.
بماند که جمهوری اسلامی میگه اینترنت به وضعیت قبل از دی ماه برگشته، ولی ترافیک شبکه حدود ۴۰-۵۰ درصد کمتر از  قبل از کشتار دی هست.
©
AManafii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/ircfspace/2392" target="_blank">📅 08:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2390">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عدد ۸۸ برای چینی‌ها نماد خوش‌شانسیه، برای موزیسین‌ها نماد پیانو، برای فیلم‌بازها نماد سفر در زمان…
ولی برای ایرانی‌ها، یادآور اعتراضات سراسری سال ۸۸ بود و حالا ۸۸ روز قطع سراسری اینترنت و خاموشی‌ دیجیتال!
جمهوری اسلامی اصلاح‌پذیر نیست و بین اونها و ما دریایی از خون فاصله هست.
از فرصت استفاده کنین و دیوایس‌ها و برنامه‌هایی که دارین رو بروزرسانی کنین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/ircfspace/2390" target="_blank">📅 21:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2389">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lBVnq_Cb0DtW9NejAgWuBUuMP-YfIJ4ma5D9I60zvUqH4CstQVnlcbZTOTsDkakFTp2o9vSb4Vp1GHkLW0mZkgTemP-8xBM6yE6cKaPPy5Lwi_uzMl4MVcB3rNdat_UACe8sSYDrJAM2btqAxT68H25U-za4LDLmkXmUahwX4FW4bVo5wh3RBHuA-U_BRAQoas_78syzAu0dDEo3q0kz0FcqlQkx4BrhufgyOUgTPyfPgovyEcZmsm4fxNQkmTCKwoSBrRjHk93kUcLOpR2jVQm4EvLR9ZK2JxZu7qvA2NyHP0DT-VO4x4OxMiYknsPWKoDgClPwplAq3dkmBGS6Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس تایید کرده که میزان دسترسی به اینترنت در ایران افزایش قابل توجهی پیدا کرده و به ۸۶ درصد رسیده؛ هرچند فیلترینگ به قوت خودش باقیه ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/ircfspace/2389" target="_blank">📅 21:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2388">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b9h5MPQT98IWRIQ9Sx-dgqgEP_KZxntMZ6yep61OKyKZ1Ud_qyDPOoclo4yzPVOKkHvsJy4D2pz_4IcY369y9-TYSWnTDU6C2XRRTD8aHlu9JmunmfGD5BZOEfdMCunO-LPPsXo79SkZOYYQBZmQcxhQYEydsBN6DSgfjUaQSUHjd0jwGIM2I30xBNc3qtsCT96mkkxOVH8NS0csJrCPJneEjHG4UfxsmHiLZ8V3b1UeYFPgPs_hYkzLUaVtmevmtMJ-LYTnP8JTyrTI82mcNfoL5L4mQFO6XgBkabLSgkbAolL8VNHOLaxxY91cB7VuLq5UshqWlcr4vG2fbmDHow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اینکه از وضعیت این روزهای اتصال نسبی اینترنت در ایران آگاه شوید، لطفاً نگاهی به این نمودار زمانی جامع بیندازید. ایران هنوز راه درازی در پیش دارد تا به همان سطحی از ترافیک بازگردد که قبل از ۸ ژانویه داشت.
©
nimaclick, DougMadory
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/ircfspace/2388" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2387">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bMXh8t00V41UqYYF5nD4vAeRcswF1JlG1ypE0b-ssuJrK9UXiFPIsCL59VxSXvewAGrHKT0uVirx4Kj71074uZsy0V3ZLDvj89B0loOxvlOSH85XrfR-ATYrIFBxiJ5FwLUh8kkXug3iM5eXipt1DmUuutL1kS2RKCZPzeBFt_oG8FD6aOSTyiKcjRNGOP1CyjQOuKwyjRoQwqGV-xA7yjnQqC_N440GE26OYlvLeHt8_5rjH1ASK6r1y7uhjmZo8sqlZ9dwgKQfWkK7EQ-fl5IDtBaGFml7tZ_d3u82uZCwBL2RRig_Djkgvxg_B_YQq52fQToCP8caFBEoqLkKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه‌ای از تلگرام اندروید که از طریق سایت APKPure منتشر شده، ظاهراً یک نسخه دستکاری‌شده و آلوده بوده و محقق‌ها متوجه شدن APK مربوط به نسخه ۱۲.۶.۵ امضای دیجیتال متفاوتی نسبت به نسخه رسمی تلگرام داره، که داخل اون کدی با نام DataCollector قرار داده شده و میتونه پیام‌ها، مخاطبین، فایل‌های رسانه‌ای، موقعیت مکانی و اطلاعات دیگر کاربر رو جمع‌آوری کنه. گفتن این نسخه به سرور مشکوکی در هنگ‌کنگ متصل می‌شده و داده‌ها رو به یکسری API ارسال می‌کرده!
©
vpnreviews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/ircfspace/2387" target="_blank">📅 17:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2386">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بازگشت اینترنت به وضعیت قبل از دی ۱۴۰۴ را با ذوق و شوق تیتر زده‌اند، انگار فتح‌الفتوح کرده‌اند.
کدام اینترنت؟ همان اینترنت ناقصی که UDP و QUIC و IPv6 رویش عملاً بسته بود؟ همان اینترنتی که نصف سرویس‌های مدرن دنیا باهاش درست کار نمی‌کرد؟ همان اینترنتی که برای هر کار ساده باید ده جور VPN و تونل و کلک می‌زدی؟
اسم این چیزی که شما تحویل مردم دادید «اینترنت» نیست؛ این یک شبکه دستکاری‌شده، محدود و مهندسی‌شده ا‌ست که هر روز بخشی از استانداردهای جهانی‌اش را قطع کرده‌اید. بعد تازه اگر همین شورای جدید واقعاً قدرت تصمیم‌گیری داشته باشد و فردا یک نهاد دیگر همه چیز را دوباره برنگرداند!
این‌همه خسارت به زندگی و کار مردم زدید، حالا برگشت به وضعیت نیمه‌خراب قبلی را هم دارید مثل دستاورد ملی قالب می‌کنید.
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/ircfspace/2386" target="_blank">📅 17:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2385">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rvZafwYauD-aKGeLhA8mXTFgTMw2NkQ5asW4hlYpDtBH_oSFJWEK6S3xslzD4MqwD45qcjWW6qbYi4G3lbaICyL3KKOcDWcTxXK22TAsyKlk0dPNisHItNFAgSxVifyijAZ9BxSZJSg1H9TfmempnZ87t24KyO5JKckbVFHIzbj1SIH-35q-2iNA1XMSxS6RtlTUGGlxPo3HptT37xTiqGy7fn09Ixk36gGOq4djwEy5Di-UBbrc8PXgYPcC8MZ772fD123ACDCUBt0349hEzRaKw3KGqtZqESoMB6oPPkt2y9FAKG8y-jzMfBDeyt-_XmVLUw7z-tJeAdvXNxgLrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ فردی که در دیوان عدالت اداری نسبت به اتصال اینترنت بین‌الملل دست به شکایت زده‌اند، کامیار ثقفی، رضا تقی‌پور، رسول جلیلی و محمدحسن انتظاری بوده‌اند. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2385" target="_blank">📅 17:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2384">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tsw2O9b8WYOSsaKaMSRwS6oN2ynwF5D2hHlhdoaAPYyXv10IaAF-lttHJTpYEu3YT-D4ka9olyOm6AGQGap410j9salM5gnRNx1dWhVgC0sdk1GhjRniSJttwsUfZlupIQtNSheMKO-MyFZ7egRTD2l4-c_jpClaj3SwnYs6Nlta_PMLgz0JGysUIQjgERyyi0jtJQwymx1yXedJ5myvG8X9cBD40Uvc6MbF1fzfw9NL09rgEUaxg8yPtk6DUHHX5jA1_D3HplzS9z9PXNd0tTfSu2OPIPV3kM7BIJ6ovzy1ZsG5qn3NBEPwYb0ExRrrZaO4I6KJERDoj7ioMZ3qOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: داده‌های زنده نشان می‌دهند که در روز هشتاد و هشتم از قطع سراسری اینترنت در ایران، اتصال تا حدی درحال بازگشت است. البته هنوز مشخص نیست که این بازگشت اتصال پایدار خواهد ماند، یا خیر.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2384" target="_blank">📅 17:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2383">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دیوان عدالت اداری به مصوبه تشکیل ستاد ویژه ساماندهی و راهبری فضای مجازی کشور ایراد گرفته و گفته مصوبات و تصمیماتشون تا زمان رسیدگی به شکایات، قابل ترتیب‌اثر نیست.
فعلا اون نمایشی که پزشکیان و هاشمی واسه وصل فیلترنت اجرا کردن به دیوار خورد و شرایط روی ملانت باقی می‌مونه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2383" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2382">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rk21PLjz5t0GK3Uf4uiz2T8Jdl-ADbAmLcEN-zcoo5ElQSNxjF6pdW_0NVoMlplbaBL-1nkF8q72i1r0CfB2JVUGjQTrGIh1w4JAIM_YycAvhzqOA92nu4xExYospgOvDpu36c6otJoZ9-UsyrsPOQDleUTQs4r_vLhzq-5diHLVR7z_AC5voikRp7iTVc21Az5cnyxP-yvhQivUMPd4KCoRZdlwQZ8KzrhmKtHiQClSDAxnx-GpxOKgoTwnz3V2KgMpOKKV5P2AKh0_Hq3SQqhkt08xU4emNR0tYo-KyvZ92psdOBfUoxptjdFg-e_di7RaVtDV3NIFmDSXWstOSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها نوشتن که مسعود پزشکیان مصوبه بازگشایی اینترنت رو امضا کرده و بعد از ۸۷ روز، بزودی فرایند اتصال مردم به شرایط پیش از کشتار دی‌ماه برمیگرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2382" target="_blank">📅 23:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2381">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/edEdefbUPbuP05exWH5J4KiaaVKeXrzd6gs_EJAz0rpzaKp1jqeeHkMz1zsUOUveWq6lS-KOvnTmk3kyN7FPouMgaJan7d7zIyXubKuuyOkWZ8s0vWhE0IogKyHP5QKRt-OTG1XmP8SCXiTPDWgWM2xiso2exo09jZubRicoxBk-dUzy8ugkXizk6NP6P6x7ioUdpbxPBOU7-gresX9Gpm-l6YHBG9jyC2iDMT7-m-JxZFS7zc0lj8oC7LDHgVnAYgWhbFS8xXHgHFpa33kgVdx5UBgAMt2-lZ30Vql2vaFdOse54e3LMwOT71KzhsUaOk2g6aFMBjdQpIbXil6BHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: اکنون هشتاد و هفتمین روز متوالی قطع سراسری اینترنت در ایران است؛ محدودیتی که بیش از ۲۰۶۴ ساعت ادامه داشته. این اقدام هرگونه شفافیت درباره اعدام‌ها را از بین برده و به شرایط غیرانسانی و بلاتکلیفی روزمره‌ای که منتقدان زندانی، مخالفان و حتی گردشگران بازداشت‌شده با آن روبه‌رو هستند، دامن زده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2381" target="_blank">📅 11:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2380">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/enQO3yiiDT_tvHpR9L6hw5ZnxN-bnIMX85Q0Qe6Z8NwMC10MmAjWaO9TGOOPZtM9fmpsi0qxg3XsggjtwCnp7S4kNcFvtyhrqcSB9OiwbrZiqJlGyT7IUJ-ggc9-OW3aSSvdbUhH_ueJIjRPQFzWf3S3N8ok3nt6jzp3Qi8_i-PnKQHu6BbJF3GLxFHMCBGMw9TI6JmL0gRQiQ5cHz-lATvdliC4QYZBn3GPYaghG1ZMSo-ZZzYgkZyd88OXruT-kiS3bzWk8-rUQGqQOO1TGTMnMqD8JWAB2e80j1vS8DqTrQE8DU1JMZJ6YS4D3-ruKJCsXjmGpXLZWW1cqfmdQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی آپدیت جدید از اپ متن‌باز و رایگان
#شیروخورشید
کار خاصی نیاز نیست بکنید! حالت اتصال رو روی CDN FRONTING بذارید، اگر قبلا آی‌پی و SNI ست کرده بودین، پاک کنین؛ بعد روی اتصال بزنین و برای مدتی صبر کنید تا نرم‌افزار خودش آی‌پی تمیز پیدا کنه و وصلتون کنه!
👉
github.com/shirokhorshid/shirokhorshid-android/releases/latest
💡
t.me/PersianGithubMirror/5515
©
yebekhe
آیا این برنامه امنه؟ قبلا
اینجا
توضیح دادم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/ircfspace/2380" target="_blank">📅 17:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2378">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مامانم دچار آلزایمره، از وقتی اینترنت قطع شده و نتونستیم ویدیوکال کنیم، فراموش کرده من ایران نیستم، فکر می‌کنه باهاش قهرم و نمیرم دیدنش.
©
MaryamA89323145
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/ircfspace/2378" target="_blank">📅 08:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2377">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U1fZif7GBKaByzmUtVpgFMFHdoRPE_hE0UOVEmN0lUtPSqemeQGO4xrvAopX6uL8J8XcWxIgY-canYMr7zhD7KkslFVvWaTnj2tXKfk_fpHNK0MEa-xWdsFTz9KO2ZoWHLqH_a076JUcdSSLBREqLad6KcjQI7ObbK1bpLRtEFVRQynh6nXXupGtX5CGyKzise1UMXfLdz1dRvulIX-NEB3M3_iiiXfE4qepvlCl_9GJH9Qg1odaXVROoikjaCf4HIYd51FlBBDjMHlxAYOmaLtfUsAjNNjAkUSbKwy2LF5QA_i0dQgtz3sziLqVviZ4Jn911vJLxYBwse5m07_plA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع سراسری اینترنت در ایران به روز ۸۶م رسیده و همزمان توجه رسانه‌های جریان اصلی به این موضوع داره کمتر میشه. انگار دنیا معمولاً به رنج و فاجعه‌های طولانی عادت می‌کنه؛ مخصوصاً وقتی قربانی‌ها صدایی برای دیده شدن نداشته باشن.
Iran’s nationwide internet shutdown has now reached its 86th day, while mainstream media attention to the issue continues to fade. It seems the world gradually gets used to prolonged suffering and ongoing disasters — especially when the victims have no voice powerful enough to keep themselves visible.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2377" target="_blank">📅 08:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2376">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a874f4f669.mp4?token=rw2xE3eND52nBOtZVre0Yz_U7JgE6eu3IX7mlGfqQCd_sdjAPz0bgDdUL8JNRL4oVPovCO28QrFHF-uselNHT1ONqoYSCMuV4gLkDdZ_dVZ9_XqdRt21_h14x5--k6JBmHrr2zdUsKtOa04au5i2RP4SQ4gwHP1tTL9LlLFObVOLbDmK8qDMnrtPS0H8Mi3g7OdY8WfQPbzG5-lLLuP0cMRL8J7rZYlu5bPW2ZHroot1_ylh3xLTTTA-YSo3nIyJ-1oLRrp89-No-4uLy3QKFU8NJmnv47ioZvDJyiikFIbTgM_2kZPFkWVYnCLQAEsaPzUddsmpU000zBL7-ZlbSg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a874f4f669.mp4?token=rw2xE3eND52nBOtZVre0Yz_U7JgE6eu3IX7mlGfqQCd_sdjAPz0bgDdUL8JNRL4oVPovCO28QrFHF-uselNHT1ONqoYSCMuV4gLkDdZ_dVZ9_XqdRt21_h14x5--k6JBmHrr2zdUsKtOa04au5i2RP4SQ4gwHP1tTL9LlLFObVOLbDmK8qDMnrtPS0H8Mi3g7OdY8WfQPbzG5-lLLuP0cMRL8J7rZYlu5bPW2ZHroot1_ylh3xLTTTA-YSo3nIyJ-1oLRrp89-No-4uLy3QKFU8NJmnv47ioZvDJyiikFIbTgM_2kZPFkWVYnCLQAEsaPzUddsmpU000zBL7-ZlbSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم خداروشكر كه الحمدالله، وگرنه والا به خدا
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2376" target="_blank">📅 08:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2375">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رئیس کمیسیون تولید سازمان نظام صنفی رایانه‌ای استان تهران با انتقاد از تداوم محدودیت اینترنت گفت: پیام‌رسان‌ها و پلتفرم‌های داخلی هنوز نتوانسته‌اند نیاز کسب‌وکارها را تامین کنند و مشکلات فنی و محدودیت‌های ارتباطی همچنان پابرجاست.
حسین ریاضی اضافه کرد: راه‌اندازی اینترنت پرو و اینترنت ویژه برای برخی گروه‌ها، نشان می‌دهد که خود سیاست‌گذاران هم پذیرفته‌اند محدودیت‌های فعلی، فعالیت شرکت‌ها و کسب‌وکارها را مختل کرده است.
او با اشاره به آثار طولانی‌مدت اختلال اینترنت بر فضای کسب‌وکار افزود: ماه‌هاست درباره آسیب‌های ناشی از محدودیت اینترنت صحبت می‌شود اما هنوز مشکل به شکل اساسی حل نشده است. در عین حال، ایجاد این محدودیت برای اینترنت باعث حساسیت و نارضایتی گسترده در جامعه شده و بسیاری این وضعیت را تبعیض‌آمیز می‌دانند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2375" target="_blank">📅 08:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2374">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AQa_i_s4VtCPyvICHd1Pch7v3W4Gh5aOLXuTFbW5hyYbrbsoPifvaDAGhq8vc61Y8NGHU2NbQwXzSgemhl558hIJvrYo9b0IsqnxNkCtxTzqffm32sol7Uwv8TlkX4t2NDJGTw1f6bolLW4rsXWo9AsWQ1U_6X6dpViwWXMq9BEUlT8Sw7y6Ve1_KzrPIJTE9odQnr08T2ONGpbCvFbZ71X7-d41qJU4_dyMwj3OP56VJtQGSRjp59YPzOnOwLW0bKDlo1TvTThdVUBejvSQm4P0ZrTBvb9jOX2KJlwt1AKJMlgJLHYcN-djg-L6whpN4-IPJSY3kegiX9vj2EJHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸۵ روز از قطع سراسری اینترنت در ایران گذشت!
قطع اینترنت در ایران، یک پروژه چندوجهی است. قطع شده تا بین "هواداران پهلوی" و "پهلوی" فاصله ایجاد شود و همزمان عده‌ای بتوانند روایت جعلی بسازند.
صدبار دیگر ایران بمباران شود، نظام با بمباران تغییر نمی‌کند؛ چیزی که جمهوری اسلامی را ساقط می‌کند، آن مردمی هستند که شعار دادند "این آخرین نبرده، پهلوی برمی‌گرده" ...
با تمام دشمنی‌ها، سرنوشت محتوم ایران محقق خواهد شد.
©
AmirHadiAnvari
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2374" target="_blank">📅 08:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2373">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ezDCmwjrWZPh_l_GusQ4U2hVA-imMGZO6jVg_O7sg4C9XI34c-RDUk_fxjGqqiOtb26W60z3Knoh-phzevk4t8j9YhckFl-KkpPQJR7tAtnWHCdE55MLUyh3OMWlkQ8K47cjZo48ZQzfU23CZQ4ZkSt6JgHZ7c6NmPiuRky13rdDiTtZOzxrL-YeUtds0kJmpVazgJVESHVqMoFI94R4tXManHyUzRbvltkP9O3qBmQrNIyMVSahYLPv1YVZRtwNv4NNVVQFW679UIqpuC0nIU8Z623xQZ53ZnNin1uh6xmPV-rvtAOFHOp6x0Lfjmjf_ZiMj4dFLqWN6EsK42iJZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طی یک عملیات بین‌المللی، سرویس VPN موسوم به First VPN که توسط مجرمان سایبری، گروه‌های باج‌افزاری و هکرها استفاده میشد، از کار افتاده. در این عملیات بیش از ۳۳ سرور توقیف شده، دامنه‌ها و سرویس‌های Onion بسته شدن و یک مظنون در اوکراین هم بازجویی شده.
مقامات میگن این VPN در تقریباً تمام پرونده‌های بزرگ سایبری یوروپل دیده شده بود و برخلاف ادعای بدون لاگ بودن، نیروهای امنیتی به دیتابیس و اطلاعات کاربرانش دسترسی پیدا کردن و هزاران کاربر شناسایی شدن.
©
eurojust
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2373" target="_blank">📅 08:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2372">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">جمعی از سازمان‌های مردم‌نهاد و فعالان حوزه حقوق کودک، با انتشار بیانیه‌ای نسبت به تداوم محدودسازی و طبقاتی‌سازی اینترنت در ایران هشدار دادند و آن را عاملی در تشدید نابرابری آموزشی و اجتماعی، به‌ویژه برای کودکان و نوجوانان دانستند.
در این بیانیه که به امضای ۱۹ نهاد رسیده، تاکید شده دسترسی آزاد و برابر به اینترنت، بخشی از حقوق بنیادین شهروندان، به‌ویژه در حوزه آموزش، دسترسی به اطلاعات و رشد فردی است. این بیانیه، با اشاره به تعهدات بین‌المللی ایران از جمله پیمان‌نامه حقوق کودک، محدودسازی اینترنت را در تضاد با این تعهدات دانسته و همچنین با اشاره به نقش اینترنت در آموزش و معیشت خانوارها، تاکید می‌کند که اختلال در دسترسی بر شرایط اقتصادی و امنیت روانی خانواده‌ها نیز اثرگذار است.
©
hra_news
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2372" target="_blank">📅 19:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2371">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aRxzydoi3tiAJ85XfIvqY9-PfwDVfek0fFqjVcFthCvSsucOgUoSiQjEikuz0XjRXpnmz44oO11f87Cv9C29CAFZsy3Nfa6-7rTuhuGXY3nkdLtAHpeKGcB6LpgxySOVaicn98OhkdgZU9LzRbMFzzNkFI_UseJKVNZS66TKVRuBPTwIvw7W7eA4SU4cjPhzkF4cK8yQnOTC5CrErVXBWzj2bBymcbXOoElMhOYYYDxnLnkKJu_pwzpKeMTma7wt1KCkNdtbs6KXhnSN9LyVCUKQKnpy4Oq1s2cIraAYxyjUo8zugoL_7IAayYAeADjvHXacu8fKFJzII1E-J7TcqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران با ورود به روز هشتاد و چهارم، از ۲ هزار ساعت عبور کرد. هر ساعتی که می‌گذرد، شکاف‌های اجتماعی و اقتصادی عمیق‌تر می‌شوند؛ به‌طوری‌که هرگونه ارتباط با دنیای خارج به جایگاه، تبعیت و امتیاز وابسته شده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2371" target="_blank">📅 19:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2370">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خیلی راحت آمارسازی میکنن و میگن ۹۰ درصد مردم با قطع اینترنت مشکلی ندارن؛ به همون راحتی که احتمالا قراره تعداد ثبت‌نامی‌های سامانه
#جانفدا
از کل جمعیت ایران بیشتر بشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/ircfspace/2370" target="_blank">📅 20:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2369">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کسانی که قبلاً کانفیگ می‌خریدن، الان ترجیح میدن دیگه نخرن، دلیلش هم تکراری شدن خبرهاست. دنبال کردن مجازی دیگه اون‌قدر براشون ارزش نداره که بخوان بابت هر گیگش خدا تومن پول بدن.
از اون طرف، کسایی هم که سیم‌کارت پرو گرفتن، خیلی‌هاشون توی کسب‌وکار خودشون موندن. چون درسته اونها اینترنت دارن، ولی دیگه کسی نیست که بخواد تبلیغشون رو بخونه. تقریبا اون چرخه‌ای که باید بین محتوا، دیده شدن و فروش می‌چرخید، به بن بست خورده و کل سیستم رو از کار انداخته.
©
NR2OH
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/ircfspace/2369" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2368">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lAySFkdxy9N8CJvglq9ZdG-PC3j-nBtmd8_fkWurUwJl2oSCNVf3JfiF95YCtHOmqjqru_hqB6KcqBZ23yMRB7RdE8EhmUKdQbmjHeMA2oM866DpPiZG7C9nSR3Q-y8A3UT_dE2fvVP1PimhXdEgXC0G1YKgP720AhbIfY32NjMsuH03St8wSOtWc1TFUPbcwBfvl4p75reLHEL9t4fp9q1eCx9z564w-LzHJjDVdHIzo8ZTsmAyu58liWGxtjXHIEy1ga4mfw69Hpd5sx4y4eUiaTA4GYJiw-vcJtiyq2lzPqTVtZxFaHbeQXaubxOACXTAgIwmrjYztkcbdMntng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا فرزانگان، اقتصاددان حوزه خاورمیانه در دانشگاه فیلیپس ماربورگ آلمان، گفته است حدود ۱۰ میلیون شغل در ایران به‌طور مستقیم یا غیرمستقیم به اقتصاد دیجیتال وابسته هستند.
او به وال‌استریت ژورنال گفته محدودیت گسترده اینترنت باعث کاهش بهره‌وری، تضعیف اعتماد کسب‌وکارها و افزایش نابرابری می‌شود؛ زیرا در چنین شرایطی تنها کاربران ثروتمندتر یا افرادی که به ارتباطات بهتر دسترسی دارند، می‌توانند اتصال پایدار و قابل اتکا داشته باشند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2368" target="_blank">📅 20:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2367">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f2ctLpS5pd-v-oTDzCXI-5dnG5IENG0CDettdnJXQZTE4iNYl2RXanPAb1IbBQdVf_L_DTGr-XD_7PWZ12kpCXn-9DgtaTFDRWksGzv-ddTknSuYLiLJWyJKzMZL_SIfJChsMJBzrfmYrGXbHqaKfofQs2PZj5lhrfJ9tL1Av4GhtP7gk9gyJfFIlXyIHHwCguRg6KiOjYbFB2OltnZ6bx4zwQteKW-w7eyS9Mqd9b2X2vgdXRdxQvZF3pa-ZhvGlKUkA_7fE2YTHohjBTV66obJ-WZj82XXMZmm2oOv4QPnmDsv8KE3K-6Fh0s42riY-xRIPGCrAa7nVFNtjRunQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زارع‌پور، وزیر قطع‌ارتباطات دولت قبل گفته "جمع‌بندی رئیسی این بود که اینترنت به خاطر هیچ‌چیز نباید قطع بشه"، ولی یادش رفته که رئیسی با ۶ کلاس سواد حتی جمع و تفریقشم افتضاح بود.
جهت یادآوری واسه
#قوه_عاقله
، اینستاگرام و واتس‌اپ توی دولت سیزدهم فیلتر شدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2367" target="_blank">📅 20:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2366">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یزدی‌خواه، نماینده طویله مجلس گفته "در شرایط فعلی تصمیمی برای بازگشایی اینترنت جهانی وجود ندارد" و "با قطع اینترنت، کسب‌وکارهای مردم از جهت ارتباطات بانکی، خرید و فروش و بسیاری از سایت‌ها همچنان در حال خدمت‌رسانی هستند و مردم مشکل عمده‌ای ندارند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2366" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2365">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VUfLIW-OR0lL87yzeBeq6KA4_kJn9SCOeARmRPsgOFnCVefoHt-PJ060PIA2SBCbmFf18PAcn30RrCkVyHzet50SusTRB20J23bhkvVv7rqcuslPZLYtVF_fugEfeaH7iNMDXSX_j4vUYiy9zV8myoUDhpEMiEIaSKcfwXSVFK4zq75XLjRZaMjQo_S9OmwREkntJW3g8KfuRozGeFvo7Gt_pGEqeW8Wi7pw4bVdLUZ_lSSGLWNnmRlW3W-LQZ8qkZxBk9h6alr_XSuYePDMATvi0ZOxcIC1diMSmjvKBw5VXps5cpeYrZ6CH07nGinWW7cvdd9triqqpdXp4J5nXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه عاقله در همراهی با سایر قوا، قطع سراسری اینترنت در ایران رو به روز هشتاد و سوم کشوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2365" target="_blank">📅 08:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2364">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گیت‌هاب گفته دستگاه یکی از کارمنداش از طریق یک افزونه آلوده VS Code هک شده و مهاجم تونسته به تعدادی از ریپازیتوری‌های داخلی خود GitHub دسترسی پیدا کنه و اطلاعاتشون رو خارج کنه.
فعلاً میگن شواهدی از دسترسی به ریپوهای کاربران یا داده‌های مشتری‌ها پیدا نکردن و موضوع فقط مربوط به ریپوهای داخلی خود گیت‌هابه. البته دارن لاگ‌ها و میزان دسترسی مهاجم رو بررسی می‌کنن و گفتن بعد از کامل شدن تحقیقات، گزارش کامل منتشر میشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2364" target="_blank">📅 08:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2363">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">عضو هیأت رئیسه مجلس: تصمیمات مربوط به اتصال اینترنت فقط با امضای رئیس‌جمهور انجام می‌شود؛ تشکیل ستادها نمایشی است.
این هم خبری دیگر درباره اینکه مسعود پزشکیان نه‌تنها مخالف قطع اینترنت نیست، بلکه در ساختار سرکوب و محدودسازی اینترنت کاملاً همراه و همسو با حاکمیت عمل می‌کند؛ تمام نمایش‌های رسانه‌ای درباره «بی‌اختیاری دولت» فقط برای فریب افکار عمومی بود.
©
alirezaer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2363" target="_blank">📅 08:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2362">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nqiP5iAIy-4g5VaaSilcS1_V-CvYK2o2zbJjyaK6CgBKfaSIgSeF4WEIsOuFKu5LxLxn-2HOD4iu50NoIer7w_AGeIoge_rHktThVShF-AYUffWnamx4je01jb6x9ABhzvMKS6ozwPQ_GiXSPAgL239v-3Z8ssbNFoV2TiTmQOz50pCpd1FI7iwnRZbuMoaGJdUxi2iC9XquqSgmt2eGTs0iDafRqJdbvBTIa_2LdQnlDY0pFss5ITa6_D2xIiOyJLH0rkUhyXKV30-BAVwrTV8mYHvPxogW6ba7f_Df47-dBv4bJgg5bSh1jCbOpYXuWdW1vlpIDBYcwaGFvh4GCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار نشون میده در ۳ ماه گذشته یک پاکسازی طبقاتی دیجیتال در ایران رخ داده. در این مدت سهم اندروید از ترافیک اینترنت ۲۵٪ افت و آیفون ۱۸۰٪ رشد داشته. این به معنی خروج میلیون‌ها کاربر طبقه متوسط و پایین از فضای آنلاینه. اونی که آیفون داره (احتمالا) از پس هزینه کانفیگ یا اینترنت پرو برمیاد، اونی که نداره، اونقدر دغدغه مالی مختلف داره که عطای اینترنت رو به لقاش می‌بخشه.
©
arashzd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2362" target="_blank">📅 08:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2361">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a69mcuGjGOZN6DRgBBpZqRWPMeCooY-HHc0BvOxLx9kdV5uVyKzosrOufkR4x3B4H3-5T8Zfl3XCzImi9CkvNXBXSgiXpFA1OrZ2qjbLqBj-sBCjqBraZoG6PVdFl6ZKWibABfM06iRbNwKGck7iSHvPXjGmlkxNJVwt70R19EbyCgTILDCaqI0n27BWRBT4k7ppENTNdKqas8_vNCsSgBzEYKU4TFTqhDkuVqP8jYAxrIJzmM_LkTmJKDBdjwoeyr0DfvlCWbdDruRV-94TFavQ43MRwwcjXTM8Fr1TZfVxEXkjfVeqGmpAhkUgtr6yCVvKSaC6KuPp934oYl3XHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتاد و دومین روز از قطع سراسری اینترنت!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2361" target="_blank">📅 09:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2360">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">قطع اینترنت به خاطر تأمین امنیت، یک دروغ بزرگ است
گفته شده قطع اینترنت به خاطر تأمین امنیت زیرساختی، نرم‌افزاری و سخت‌افزاری است تا کمتر مورد حمله‌های سایبری قرار بگیریم، در حالی که این یک دروغ بزرگ است. حمله‌های سایبری و ناامنی زیرساخت هیچ ارتباطی به قطع اینترنت ندارد. متخصصان به این‌گونه دلیل‌تراشی‌ها پوزخند می‌زنند. البته نه به این معنا که زیرساخت مخابراتی ما یا زیرساخت شبکه ملی اطلاعات ما در حال حاضر امن است؛ نه، ناامنی وجود دارد، اما قطع اینترنت کمکی به تأمین امنیت زیرساخت نمی‌کند، بلکه لطمه بسیار جدی‌تری هم به امنیت زیرساخت می‌زند.
در همین مدت دو ماه و نیم گذشته ده‌ها آپدیت امنیتی برای باگ‌های «زیرو دی» یا اصطلاحاً باگ‌های روز صفر داده شده است. این‌ها باگ‌هایی هستند که می‌توانند دسترسی بسیار بالایی برای هکرها ایجاد کنند؛ روی گوشی‌های مردم، روی مودم‌ها، روی شبکه‌های صنعتی داخلی. این‌ها هیچ‌کدام آپدیت‌ها را نگرفته‌اند. آپدیت‌های ضروری‌ای که حتی یک روز به تعویق انداختنشان گاهی باعث ایجاد ناامنی می‌شود، الان بیشتر از دو ماه و نیم است که دریافت نشده‌اند و ما با یک بمب ساعتی در ناامنی زیرساخت شبکه کشور مواجهیم.
من فکر می‌کنم وقتی بحث امنیت مطرح می‌شود، بیشتر از اینکه منظور امنیت شبکه و زیرساخت باشد، منظورشان کنترل افکار عمومی و جریان آزاد اطلاعات است. اگر با این چارچوب امنیت را فهم کنیم، بنظر می‌رسد حق با این آقایان است؛ قطع اینترنت قطعاً باعث جلوگیری از جریان آزاد اطلاعات می‌شود. دلیل اینترنت پرو هم اتفاقاً همین است. اینترنت پرو نهایتاً شاید به یک یا دو میلیون نفر ارائه شود. یک یا دو میلیون نفر با ۵۰ یا ۶۰ میلیون کاربر فعال ایرانی خیلی متفاوت است و باعث می‌شود جلوی جریان آزاد اطلاعات گرفته شود و در واقع کنترل افکار عمومی و کنترل جامعه راحت‌تر شود.
چطور اینستاگرام یک پلتفرم آمریکایی است و ممکن است لوکیشن و اطلاعات مردم را در اختیار مثلاً نهادهای امنیتی آمریکا بگذارد، اما سیستم‌عامل اندروید که متعلق به گوگل است، نمی‌تواند چنین کاری کند؟ اساساً منطقی که مطرح شده، پر از اشکال است. وقتی شما اینترنت را قطع می‌کنید، عملاً یعنی تمام زیرساخت‌های رشد و توسعه یک جامعه را متوقف می‌کنید. به یک معنا، ما با این مسیر داریم گام‌به‌گام به عصر حجری نزدیک می‌شویم که در آن از فناوری اثری نبوده.
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2360" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2359">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">امروز هشتاد و یکمین روزیه که اینترنت ایران بصورت سراسری قطع شده، ولی پروپاگاندای حکومت بدون لگ داره کار می‌کنه.
امروز هشتاد و یکمین روزیه که جمهوری اسلامی داره
#روز_ارتباطات
رو با قطع اینترنت جشن می‌گیره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/ircfspace/2359" target="_blank">📅 08:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2358">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HUynSc6IW0aGQ0RisGyY6RzhfCbJ2EfaaVef8ZMJ-szBRP91edQwcmMCcKP0ZEKKyggf8CxzzBtUbgTVdiTOfKz0-o7o58FgXe64shVM-GSgLUByTQRtb9xdtZ4QCMufXjf9olydRVRvXwwYeIM-zoI7tgSjgak6xOKkdV0FuB6eVgzUd6qftXcRqr1rjzDhn8MeQ-ulLNmKTqBlBT_w3vOfWT_cS1zLo8sDE1a8F-iAETsSow1F48fXPeqyhZ-PzTfd-qFy-Vz2NZP9SnsjHRZP6SFReg813_Fqt5pQ_JuT9B-2o3vkQlLEUEm7KCzPFxhoc4eJ-3EQyRMJY08jDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در بروزرسانی جدید از اپ Network Checker برای اندروید، ویندوز و لینوکس، قابلیت اسکنر آیپی Akamai (جهت استفاده در اپ
#شیروخورشید
) اضافه شده.
👉
github.com/mirarr-app/network-checker/releases/latest
💡
t.me/PersianGithubMirror/5227
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/ircfspace/2358" target="_blank">📅 08:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2357">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/El8sjAs-QbI7RZBndjLAr0BXKAg7oYXywNYZclNArlC8TbUhhmsyqbNX_7kxriF3nNJPmUBuBgmz5rlPMe0amA1EnR4VhNdzjEHN_rhrXyHGwnDE-J0COsIaLGVZHG-vVwahALuHSBvRkV986u5ydKRj_49kWb2Yl9ugFbXVMB6tvGYDMlNvDcShUSp2_S8qFLtKbCY-BuXocG5gi4IZ_3AFauRXY_2QZADMTJOVhgis8DYXrEME65bDOUsypnBKofCsBomQZ0XGBPnmKXWSxwNdUaBkVxvu7hBtbP3rMzCu6fQk9NMjRZWpQGGmd-myMMyezxuBr20iixpFhoh_uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ NexaTunnel یک کلاینت رایگان برای مدیریت تانل‌های StormDNS در iOS هست، که به شما اجازه میده کانفیگ‌های مختلف رو وارد و مدیریت کنین، وضعیت اتصال و ترافیک رو بصورت زنده ببینین، DNS Resolverها رو تست کنین و خیلی راحت بین پروفایل‌های مختلف سوییچ کنین.
این برنامه با رابط کاربری ساده طراحی شده تا بتونین وضعیت تانل، سرعت دانلود و آپلود، پینگ، IP عمومی و سلامت اتصال رو بطور لحظه‌ای بررسی کنین و مدیریت بهتری روی اتصال‌هاتون داشته باشین.
👉
apps.apple.com/us/app/nexatunnel/id6766783641
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2357" target="_blank">📅 08:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2355">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">توصیه اکید من اینه که برای وصل شدن به اینترنت سعی نکنید از سرویسهای ایرانی (خصوصا سرویسهای متصل به نهادهای امنیتی) که شمارو قبلا احراز هویت هم کردن، سو استفاده کنید.
به هیچ وجه حتی برای امتحان کردن هم ارزش ریسک کردن نداره. و به هیچ وجه هم روشهای مربوطه رو معرفی یا پروموت نکنید! اگر کردید بهتره همین الان پاکش کنید. از سر دلسوزی میگم، بچه‌هایی که از چندسال پیش در ایکس فعال بودن میدونن دارم در مورد چی حرف میزنم.
©
aleskxyz
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2355" target="_blank">📅 20:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2354">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aXcgu_RNv2oLsNQSpO8Mgq-T9hJ8SejxNriMYA2XqvKZTTPWouNM-enaGUkhFILmhM4IWrbQFymyPOH-O7dwUYlUnbTyCtL614JlKzui_wxwDmou6P2HOTiMTIFXLS5Hk-9iCkQIKgfDYK7G1Vz910kF6mypAp7vqesfgIeuWZU2bJ4t1a_QHsZmKobIYU4WksoPt1EQlMf3GNgTaJxqZcNylP0lW95WvJoQn2LCq0VZ3k-FQAcMrRcbaHGpJ4HBlQ6OzF4Kv6n7eVQRH_e9ZpqMLsP8n1p1UgN3rsCpHTkz_m31GCdz9jx-i8qcBlbgtU97FYhKCC5SYt3qs2lyfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما در انجمن تجارت الکترونیک تهران تجربه واقعی کسب‌وکارها در زمان اختلالات ارتباطی را مستند کردیم. از میان ۹۴۴ کسب‌وکاری که به نظرسنجی پاسخ دادند، بیش از ۸۰٪ اعلام کردند در زمان قطعی اینترنت، فروششان بیش از ۵۰٪ افت کرده است.
اما یک نکته مهم‌تر در داده‌ها وجود دارد: حدود ۳۳٪ کسب‌وکارها گفته‌اند در زمان بحران، «پیامک» مهم‌ترین ابزار ارتباط با مشتری برای ادامه فعالیت آنهاست. پیامک در زمان اختلال اینترنت، یکی از آخرین مسیرهای باقیمانده برای حفظ ارتباط، اطلاع‌رسانی، پشتیبانی و فروش است.
حالا تصور کنید پیامک هم قطع شود. بیش از نیمی از کسب‌وکارها گفته‌اند با قطعی پیامک، افت فروش جدی (بیش از ۳۰ درصد) خواهند داشت. پیامک بخشی از زیرساخت تداوم اقتصاد دیجیتال است؛ نه یک سرویس فرعی.
©
NimaQazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2354" target="_blank">📅 20:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2353">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p1wo4krPUZZNAj07Hh4WjAdt5Fqz0MdOH7-2tC5qGE0eb6LPC2IlNrphAhVp0KJ7V1Woy6oIyl6LVYTlvejvxH9TZj6JjqBRpLK5x90l59_AHFgg-Y9d7IqlPHFb8wquFVmR3cxxWlas4y3p8lqtF6cPq6fr8fW-D1j-VjUBqVumPWLNhQPKPFPOjW8bPSjSLTCJfvWpmtOd0w3QEH0vPxkWQcudFDfVj52SkoXzntd27KEHS_ulkdmGYll5SO5b5ljSmxrIchMB83CRpunHdwdBp6MMQl8kGIcA1WwnWSesq11qxG5GLgwvpCnyvyvncHvFI653dFE7sRD5AlztGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید به افتخار وزارت قطع‌ارتباطات ایستاده
شاشید
!
آیندگان در کتب درسی از تمامی دست‌اندرکاران فیلترینگ و وزارتخونه‌ای که اسمش ارتباطات بود اما ۸۰ روز متولی قطع‌ارتباطات شدن، بعنوان
#قصاب_اینترنت
یاد خواهند کرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2353" target="_blank">📅 16:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2352">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J16t0P9uFXfXVtZwznYzo6JETG2knZvrVLjIEUZsOGv3Dff9TCBapYcphI9KmgllN9H2aaNYAXGDAkq8fcs92WipaqrX1coVWhXtVihF6QkVKaYYkHNFQYNTRzuvM1DxHWsmVGiOloy2ruz4aPbjFWtvW1oepmwPADA8zx2S0tM5N5d428QReQhrMvMe-QL6mdWuV-zkyL6X8kQHsOc25FQM9CILHuM4q_G85ooFWcp1F_DvPTKCRqU29tKE86swEZDDnjgu3vOENdic6uxisBbcfvlXcWo40kBmAlom8Ds00KQwdWSkbf5A-cRx4pb0FHPd1HGrzTL3PK-PirccsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستار هاشمی از پایداری شبکه ملی اطلاعات در دوران جنگ تمجید کرد و گفت: شبکه ملی اطلاعات کارکردهای متفاوتی دارد. در شرایط جنگ شاهد پایداری شبکه داخلی کشور بودیم تا ارتباط بین مردم قطع نشود و خدمات مورد نیاز مردم ارائه شود.
وزیر ارتباطات افزود: در دولت چهاردهم نشان دادیم شبکه ملی اطلاعات ورای یک شعار در میدان عمل کار می‌کند. این اتفاق بی‌نظیر و شاید در دنیا کم‌نظیر است. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2352" target="_blank">📅 16:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2351">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b6FsPceZwiqLn33cR2Lr0lj3g1Vd1kwPCIQrE2mcWHmYnbS7h9d5vIAZAzYmGhVPpoj72LqgBXalmcAjZtDhciTGsUlyo2IDwHZV1x7f-Wf1XIficZIrQWVg-BGgsYOi07QRG1RPS9Egx31pspgUu39-Y7zhq_gZnIWrC81hJ4wcI5Fn00BefDe8J8iSwmLptRmMwh2W5iXFfUfI9yL_ArbxyZLFdRwF_7xlVt-IgA6LZVtuHJWPjXaNMjQmFntNtDWWI9U1XO2aMJbIFgkrRVQT55DlNbR9BctUSqkJffZLlKIKEakfJin64fmFg72VRJHBq9w7fIgM9K-wLMvNEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ اندروید
#چشم_عقاب
نه فقط یه خبرخوان، بلکه یه راه آفلاین برای دسترسی آزاد به اطلاعاته، که بدون اینترنت، بدون VPN و حتی بدون داشتن مجوز اینترنت روی گوشی، خبرها و اطلاعات رو مستقیما از ماهواره روی دستگاه شما میاره.
کافیه کانالش رو روی فرکانس 10762/27500V ماهواره ترکمن‌عالم باز کنین و دوربین گوشی رو سمت کدهای QR که روی صفحه نمایش داده میشن بگیرید، تا اپ در چند ثانیه اطلاعات رو بخونه و روی گوشی ذخیره کنه.
اپ فقط به دوربین دسترسی داره تا QR Codeها رو اسکن کنه و هیچ عکس یا ویدئویی ذخیره یا ارسال نمی‌کنه. تمام محتواهایی که دریافت می‌کنین، قبل از پخش با امضای رمزنگاری‌شده Ed25519 تأیید میشن تا اپ فقط اطلاعات واقعی و معتبر رو قبول کنه.
👉
play.google.com/store/apps/details?id=com.filtershekanha.cheshmoghab
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/ircfspace/2351" target="_blank">📅 10:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2350">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">باورم نمیشه قطع اینترنت به ۸۰ روز رسیده!
وقتی حکومتی برای حفظ خودش حاضر میشه یک کشور رو وارد خاموشی دیجیتال کنه، یعنی مردم هیچ اولویتی براش ندارن؛ وگرنه امروز وضعیت اینترنت، اقتصاد، مهاجرت، ناامیدی و زندگی روزمره‌ی مردم این نبود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2350" target="_blank">📅 09:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2349">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ONSzp8y6HgEF2BLwuAvPrpHcRDGV3Hkvh3ZiZs7FXtndt-ToaaiyJFoTUyGEuzUxo4hd0guO684vY8TLy4cfGw6noNXtxra0cQGZdm-mw9ywHoBONeH2qktR2UDiYzcH1XhIznT3eZ2CRxWRzIP6y7jkCAVw3g6oa_vWLvjPDl21DEKHpMFrUqXdyA3r7QNc6fsKknlOB6INRWm3m17FOM5cLnlZ91ry_ec7t6mlQELVGU2DNphy1xqmHVV3VaI7bsPMQSojEVYFLf_W0ePlbIykkALIFpGI-XM1JJ94NkEJkD2-E_9BYgVwVRCoO62qXJbYyiKOsDomAza-w9AfEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان بعد از ۷۹ روز قطع سراسری اینترنت در ایران، روز جهانی ارتباطات رو تبریک گفت!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/ircfspace/2349" target="_blank">📅 21:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2348">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AnM4gNiCHp5MVe2HiwC6AcO3f7KI4nd4YzBpaAYUkj1zeRIpJgirscjzCk5OjRPB1PiAo5GRC6cllLBuqCNHfjA1sZ2NxHyLOVbCz4k6f27gKtmnS0a7WJPvm_M_WlZAmitYzgp3rz-rTTLDff7AFaPhgsOh7_iH7Q2xfKzsGoy_Gdm1KLcBC9Df_QMFpoyt1YoHLc9IvlElZWzsL1Sr-uYlgYmrV0A738JYZkyOtJUnRnju_WmNEehzQYVD71Rfel5QYT3ryrjTVCWv1EGUaAo_GTOIG5nfoJ5t3A_cIVV5MMAVBvRwAoNIxcPCSlzmFbOOjQBXXmMltsMhmUxBEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیمکارت‌های بدون فیلتر، حفره‌ی جاسوسی برای مسئولان!
در رابطه با قطع سراسری اینترنت به بهانه امنیت و اعطای
#سیمکارت_سفید
، سیتنا در مطلبی نوشته: طبق منطق فنی، وقتی با سیمکارت سفید و بدون فیلترشکن به اینستاگرام، واتس‌اپ یا سایر پلتفرم‌های خارجی وصل می‌شوید، هیچ لایه واسطه‌ای برای مخفی‌سازی وجود ندارد. یعنی دقیقاً در همان لحظه‌ای که یک مقام مسئول درحال چک کردن دایرکت‌های خود است، اپلیکیشن‌ها لوکیشن دقیق او را با کمترین خطا رصد می‌کنند. اگر نفوذ و ردیابی، خط قرمز امنیت ملی است، پس چطور با دسترسی‌های ویژه، عملاً موقعیت مکانی لحظه‌به‌لحظه خود را تقدیم سرورهای خارجی می‌کنند؟
تناقض وقتی اوج می‌گیرد که می‌بینیم مردم عادی برای اتصال به همان شبکه‌ها، مجبورند از کانفیگ و پروکسی استفاده کنند. این ابزارها با وجود تمام دردسرهایشان، حداقل یک لایه پوششی ایجاد می‌کنند که لوکیشن واقعی کاربر را تغییر می‌دهد. اینجاست که بوی یک تجارت کثیف بلند می‌شود!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/ircfspace/2348" target="_blank">📅 08:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2347">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اینترنت برای عده‌ای خاص، محدودیت و خفقان برای بقیه مردم
امروز هفتاد و نهمین روزیه که جمهوری اسلامی اینترنت رو به روی مردم خودش بسته، تا زیر سایه‌ی خاموشی دیجیتال، سرکوب، اعدام و پروپاگاندای خودش رو پیش ببره.
چندماه هست که هزاران کسب‌وکار اینترنتی لطمه دیدن یا نابود شدن، اقتصاد ضربه‌ی سنگینی خورده، تعدیل نیرو و تعطیلی‌ها بیشتر شده و مردم حتی برای ساده‌ترین ارتباطات روزمره هم با مشکل مواجهن. با اینحال هنوز هم بهانه‌ی امنیت رو تکرار می‌کنن!
این قطعی تکان‌دهنده معلوم نیست قراره چندروز یا چندماه دیگه ادامه پیدا کنه؛ اما همزمان جمهوری اسلامی با پروژه‌ی اینترنت‌پرو هم جیب خودش رو پر می‌کنه و هم به رفتارهای متناقضش ادامه میده؛ یعنی اینترنت آزاد برای عده‌ای خاص، محدودیت و خفقان برای بقیه مردم.
در این بین، عده‌ای در شبکه‌های اجتماعی تلاش می‌کنن با فضاسازی‌های ساختگی یا حتی ری‌اکشن‌های فیک، تصویری غیرواقعی و عادی از وضعیت کشور به دنیا نشون بدن؛ رفتاری که علاوه بر نبود بلوغ فکری و ناتوانی در درک عمق بحران و رنج واقعی مردم، برای خیلی‌ها نشانه‌ی هم‌پیالگی با ساختار سرکوب یا فعالیت‌های سازمان‌یافته‌ی سایبریه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2347" target="_blank">📅 08:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2346">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C16EgdMeJ22NJYy31jHGnDDnBqz7Lo5_yIjNQLTh55SHVh9vTx6B6LeA_ESYsG2GEGpojtAG6q-FlGuBbgjz4ZcyAs4rbQ3XbS9ySFUPvMGwxDtG2TAYLZV4-p3kKTEWF_Px60ii-XRO0ed-ys4ivpc7GDWTpRpkfwIWoWIQfLyu8I9Htv1OIPOQO-zHXsKzs35FXdRCaFW8Aq10g4Dli7ndroVFEz2yD3Z2hTA-C29RrnIwHS-LfITGPFYC8L-0Z6uSsdB4oi6fPElKE2WrA-Fapq9wirtADPJyD5XC3m423cYwHMbih1dYB5NzL3AxXT2CSrurRER-T6ySl-Jy-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱۶ از فیلترشکن
#MahsaNG
برای گوشی‌های اندروید در دسترس قرار گرفت.
در این آپدیت هسته‌های MasterDNS، GooseRelay و FlowDriver اضافه شدن، قابلیت CDN-Fronting سایفون تعبیه شده که میتونه شانس اتصال رو در برخی محدودیت‌های شدید شبکه افزایش بده، امکان وارد کردن دستی HTTP Type لحاظ شده، یه سری از مشکلات رفع شدن و اسکنر DNS حالا IPهارو بصورت تصادفی بررسی می‌کنه تا نتایج بهتری ارائه بده.
👉
github.com/GFW-knocker/MahsaNG/releases/latest
💡
t.me/PersianGithubMirror/5051
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/ircfspace/2346" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2345">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اپ
#شیروخورشید
بعنوان یک فورک از اپ رسمی سایفون بصورت متن‌باز ارائه شده و توسط گیت‌هاب اکشنز بیلد میشه.
آپدیت جدید این برنامه تونسته دسترسی هزاران نفر به اینترنت رو در محدودیت‌های شدید فعلی فراهم کنه و همونطور که انتظار می‌رفت، افرادی سعی کردن برنامه رو به حاشیه ببرن و برای کاربران نگرانی ایجاد کنن.
علاوه بر متن‌باز بودن پروژه و امکان بررسی کامل سورس و روند بیلد، متخصصین حوزه امنیت و افراد فنی آشنا با ساختار این نوع ابزارها امکان تحلیل دقیق رفتار، ترافیک و عملکرد برنامه رو دارن؛ نه اینکه صرفاً بر اساس برداشت‌های سطحی، حدس و گمان یا خروجی‌های بدون اعتبار AI، درباره چنین پروژه‌هایی قضاوت بشه.
در رابطه با تفاوت این روش با MITM هم توضیحاتی از طرف توسعه‌دهنده برنامه منتشر شده که پیشنهاد میشه مطالعه کنین.
روش کار کلاینت شیر و خورشید کلا متفاوت هست و اصلا MitM انجام نمیده، که نیازی به سرتیفیکیت داشته باشه! دلیل اون روش این بوده که بیرون هسته سایفون میخواستن ترافیک رو در v2ray تغییر بدن، پس باید از سرتیفیکیت خودشون استفاده میکردن (که در صورت بی احتیاطی نا امن هم میتونست باشه). در شیر و خورشید تغییر تنظیمات SNI و ... که روی ترافیک ایجاد میشه در خود هسته سایفون اضافه شده. در واقع اگه کد رو بررسی کنین میبینید این قابلیت Domain Fronting چیزی هست که خود سایفون در نظر گرفته بود، ولی تنظیمات و قابلیت تغییر درستی رو برای فیلترنت امروز ایران در نظر نگرفته بودن، که الان در شیروخورشید اضافه شده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/ircfspace/2345" target="_blank">📅 23:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2344">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fm19o5LScWAagQZ__wMqQpzbYJQOkGTWdNjsFDFRgpI7wXoV26uDA0ek9LBKPj_c8C6CpudSh95YxrhFAWS3YkI01MbQ6JClHmkf2NO1hC4s6Fw-SpbiHhEaEj7W8OV59C6Q4qltqQreLOxysxxyVc3sWc5wdpqFOdrkCzNMFqM5kF8_m0nz8fb4eHroWZv4UZRrdpazutdpturipALyz48Uy4rUjyRj1HZpwuy4qRZljK9FKpnuiEVefSCE4mMW3LWABsVqZIBAQJd8C0L4pMqkz0tm6NpQwACwgeIyZWfTLt2PahiTaMxGEMA2EJS4UsEZxnCVFLD0_GD6UyFkEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتن هرچی که تهش Hub داشته فیلتر کردن؛ حتی گیت‌هاب.
قوه عاقله‌س دیگه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/ircfspace/2344" target="_blank">📅 09:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2343">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rap0b_icEN0uYzzWf-gfPDETSZ0xRY2PFZzErkpSf_KfPTCBtugdZfpNAYTPI3_-AJK6w4Pw32KSI673fanbeUkjMC0_lgiGAtgBN129xEIF4N2-tfeSmK8Dg_ZrteE1qSdHk3jEAEyso0fSxKpml-P-hl3o_QlnvjPvDiUoi16ktbYhyLkfuhB3GaE9ylPz9RerwSjgGlljecKtRClbgh8pGPMp-basr7EodjTflwpv1EJD_fsg-PbYWzS0VZdurQYehNEONZiSg3j85Pz4rGZaIstbgirq3uUbbstInlZtDf1If6fGkmP7XO7_7omOK7rE-vPJTnBgz06971Wlgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان TunnelForge یک کلاینت L2TP برای اندروید هست، که از امکاناتی مثل حالت VPN برای کل دستگاه، حالت پروکسی با پشتیبانی از پروتکل‌های HTTP و SOCKS5، مسیریابی، پشتیبانی از چندین پروفایل همراه با ذخیره‌سازی اطلاعات لاگین، بررسی وضعیت اتصال، امکان استفاده از DNS سفارشی و تنظیم مقدار MTU برخورداره.
👉
github.com/evokelektrique/tunnel-forge/releases/latest
💡
t.me/PersianGithubMirror/5008
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/ircfspace/2343" target="_blank">📅 09:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2342">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FoiX1tX5NuJxEJaxjkStf3ZMyQ44xvdGFXB_2R5WuVsqpTNIXn-XTl8rjwg5Wr55yuB_pzu2RbUfovChj2RUTGTJXBBBCKJh-lAgI7v4z1rFdH3ZVUq4AAS7qxR3aZFlcEKIjtWmMgNkAlfwjR04XIuwMzNDk6dA6XExpDsSWlTrLU9iQ_2-HvxSRUJYADxD9j_a-8VN0bPDBjMmAIQTj1W5ISLb6IV3ElL1xF9b-lpg-tPx4LWoC6awcLbSPkxXsJoqQz7vTD3B9k9STXmEPlOePathvdl_W5EpmU4IQKc99ZRH8NiCRnTpyE2gXpQLHQ30hVwhTBd2Z37NueZc7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آسیب‌پذیری جدید به اسم YellowKey در سیستم‌عامل ویندوز پیدا شده که توی بعضی شرایط میشه BitLocker ویندوز ۱۱ رو با یه فلش USB دور زد؛ البته فقط وقتی مهاجم به خود دستگاه دسترسی فیزیکی داشته باشه. برای کمتر شدن ریسک بهتره ویندوز و BIOS آپدیت باشن، سیستم کامل Shutdown بشه نه Sleep، و برای BitLocker رمز یا PIN قبل از بوت فعال بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2342" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2341">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JURh4C50HXuz7t5bMl3yOCQVCVzqyZ-E-GRPIvs6RUtjTsbyL-9x2AhIteT6oyEC0miBw2n6yxy_VLjQcLf_i9uxGXj8SYuHv6mWaAmC8bbLVSEuPkN452STDlcxPH3e-uSuqnPLYvP4zWG8cTQt4sLsrDTZ78PF8jmg3bYR-r88KycbS9g95QMy7FnbayuCJHqXxYusJetLNLd-fuyXu6SY4CGgOteNwnFzdDEcOt-BiIYwn_0QXDCDcJwXd1xr6b-4CFMD5Dd9yR8C1quVp_5VeBZbmC7N4ERsxMVbCyP_F0ZXNSviXJL09UIuYPFXb5xCqBn6phjsZAsBDh0h7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استارلینک مینی به ۲۰۰ دلار رسیده که فعلا اشتراکش هم رایگانه. کنترل اینترنت با اینترنت پرو و قیمت‌های کذایی یه توهم زودگذر هست!
©
imanraisii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2341" target="_blank">📅 08:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2340">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IZ2IVWtqshDzmvsEXn6AugNlrFH0lD0H5xrM7jBBH2NM3WRpDblZhPLGRFVIVifMr46QrPQdf2vcep70HkOzJi8fDHKQY9lYje5LDmkykAL-1VZk4Tr71XABjNEI98QDvHJHg_ggHjtOSscKGcZVJeT9AQP3qdFBKnAEjdKr5LLYnOC1xEmCmaIrhFMQY9-dr8bCbwdUqz2jAkrdNMgU1INMPdg7wCSb3sHNWpGCpK-3mvfcuiC6WQhtpaUWo87aVhSI9tfVQ86nqUFYdtB2gpTLT-dHE1Hirq8SM5aja8PW6Zc5L9Cgg6TPaIXUCYJkEWddiTWWlzvXv9rDF2ca-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در هفتاد و هشتمین روز از قطع سراسری اینترنت، از جدیدترین روش ترکیبی عبور از فیلترینگ با ذکر "لعنت بر جمهوری اسلامی" رونمایی شد.
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2340" target="_blank">📅 08:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2339">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lcnpr8C6Cj3CaUP9paXbg6R-_VKRKaoqNEBIAbmYyyS5PGqKQHstLQxOlDHOV5CdU-bHV5O5pz49-xr238HBXG4_IWDhhbjW0b7Hq1d8ZWTB4nUByEOkiUR8S6Upgsl_gA9-BLpb1kw3iJiKtBb7gtUCfFmcvr14IX1hrk7fDxhhNzql6zJpIpVsS5g_rU4dO81fTgzX9IZDpiOuW7JClXucOqzsghd3tRNfHFRYp7oU525p5-VysxVRJC5YJwS_LWnItweUq79OyZlJPKfukv2nHZ0UA4oDeQ5aQqLn2iFsn0SoQPo8cJShmU9u7ukrpBkxIzPZijkVfBqP20wWGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتگ از تبعیض بگو!
اینترنت غزه که قطع میشه، اتحادیه بین‌المللی مخابرات میاد محکومش می‌کنه، ولی وقتی که اینترنت ایران برای نزدیک ۳ ماه قطع میشه، سکوت مطلق! ۱۰ ساله در مورد ایران توییت نزده!
©
markpash
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2339" target="_blank">📅 08:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2338">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AzDUmICdstueZg6b52-jksnlI1GMsBmRn6iXIL_2tWN5opHlsr7AgsOGlPXT_RwW8tRBxjj5NI0hKsjEABEseQRA2sfUOqJ-FqNBhXIfPQnttBNg2C_ipBzNsWOluVTnGLZ_Acwz1LnntlKx8oGamuCYyK9N1-FaTzplUHNzIB9dVfCeoSzkVaRf2ck0SHuNTrj5FCM2WdQOnteTdiUaZJriaAcAiGKhJQoJkUyLJ9D41Vmiv982iAl2BNyCBXxLnnmeEo4I-qShAvPJrNuohdzAYAc2_ZMUwcBGX0GbpDJE1864qJBJNYdID7HcBjArFc7aO6T8hUhYf7tYycBhaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد حساب این الاغ [توی ایکس] بسته میشه، داد میزنه که آزادی بیان نیست...
©
AminSabeti
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2338" target="_blank">📅 08:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2337">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تقابل اینترنت و امنیت یه دروغ بزرگه. مردم نه‌تنها  دسترسی به اینترنت رو به امنیت کذایی شما ترجیح میدن، بلکه هر چیز دیگری که خلاف ترجیحات شما باشه رو هم به انتخاب و تصمیم شما ترجیح میدن. شما هیچوقت جسارت برگزاری همه‌پرسی در هیچ موضوعی رو ندارید.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2337" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2336">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ستاد فضای مجازی با مدیریت دکتر عارف در اولین روز کاری برای افزایش رفاه مردم و تحقق وعده‌های دولت وفاق ملی، گیت‌هابو فیلتر کرد.
©
pey_74
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2336" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2335">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KxQigmvkB57oYzg-DPHhgZQOheSeurTs81QDm98OBfh71z9Bu3F5vhP0iSpv1ZRoGNp61jguaV71fdPHKNJcoD6TzCfd6LjpR3xn0MvUz3huNtD-pDAuC8_d_lbExt-QOi7B6Y5iVoOuwIGdfVYGWonGHHMSd4puosTTXesvLSZpSOU81njMcd4-hNcDQuyqQv0gZzkdem2OJjB9C10xVeltlMpuPvb2OGWtP787aS_ydT2CbhIcyLCE6Ec2TSfMNqRPul8EjmbRVWc3VkOEtwaJl1rt3tuGXpnSGVgkueRO_LrPsNA1qcVUoMMh5SWPyHM4622XP-ghlIaN2J3aKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش
MITM
در آپدیت جدید از اپ اندروید
#شیروخورشید
گنجونده شده و می‌تونین بدون دردسر ازش استفاده کنین.
برای استفاده بعد از نصب یا بروزرسانی، باید وارد Options، سپس More Options و بخش Connection Protocol شده و CDN Fronting رو انتخاب کنین.
همینطور در قسمت CDN edge IPs اگر IPهای وایت‌لیست شده
Akamai
رو بذارید، سرعت اتصال بهتر میشه.
👉
github.com/shirokhorshid/shirokhorshid-android/releases/latest
💡
t.me/PersianGithubMirror/4954
©
PawnToPromotion, mahdavi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/ircfspace/2335" target="_blank">📅 16:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2334">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نحوه اتصال رایگان و نامحدود به اینترنت آزاد با متد ترکیبی MITM + Psiphon
👉
github.com/patterniha/MITM-DomainFronting
©
patterniha, MatinSenPaii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/ircfspace/2334" target="_blank">📅 16:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2333">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">روز هفتاد و ششم از قطع اینترنت.
معاون دفتر پزشکیان گفته "درصورت برگزاری همه‌پرسی، مردم امنیت را به اینترنت ترجیح می‌دهند".
وقتی گفته میشه هدف از قطع سراسری اینترنت و خاموشی دیجیتال مسئله امنیت نیست، دقیقا مطرح شدن همین اراجیفه که به جای نظر مردم به افکار عمومی تحمیل میکنن.
زمان زیادی از کشتار دی‌ماه نگذشته. به جای این چیز خوریا، بهتره یه همه‌پرسی بذارن تا وضعیت مشروعیت جمهوری اسلامی دستشون بیاد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2333" target="_blank">📅 09:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2332">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tKfZLjYOh1AgIPLBPDwUAmhN2a7XvEHuBceKTSVZaMEWlEPDm7wb4OtxUmnSLy4Q9mSeHNZGz2-fIp6so9n-3-ias-gltpekH5zqtmQBb8WtlTtRfCSZ5m8ZxRKYA0i6ixc2VTtoN3bN1lWBGlW3vgbE8wAq3Lk9BZ03spuLM1KfcomE0p1O4KL7weg7wD56vppyBL3VWZ2LbFj7jntG-9sQ7AkaNujI7MB42pF5fficU_cx6_qHOWPsjiHZQSG_Hzjtc3mIcXKTFLxsipKhVKToELx4w87koPzUazuSSfqpRDBS-BrQhXzkvRoNtkWOr11G07DdFV-pKvSF9T0Tpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون فرهنگی مجلس: امروز پیامرسان‌های داخلی گوی رقابت را از پیامرسان‌های خارجی گرفتند.
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2332" target="_blank">📅 19:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2331">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kfo0hGLxSf7GZmTSrWD76E4WXOA0xHjYRc8xXpiN69ltU0Xohx5R3JW9kSETG3dSwBXE-or9uu1bht8ODmxv7ruXwgilFPDo8l8gkYjQsEXQPXDuSLkFPwQX0EPm7Q-0eCxIiEohRGrkzgdev_RSf8H2dO7-LmAeGAnrPch3YOzVlUPdr2erVDChmjwqLElUaEOxb-KjeGASerQW_gbT0CuVtd8adYJ_zeb8nkHcYRBHA4PtiDT44ddKLJx8oUziKKSbAfdaBRIiHjz-XhfYcJ_sCS0UeyhIdJEZXkm7Sl8R-RVmNCFgjI17koFWYQWBNqQ8xk4-pEIzWRJgs4N5IA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2331" target="_blank">📅 19:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2330">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ORii2XFub5q_FdMBLssYNF6_gvkbx_uvBMd0auAvAOpSDTPl56U6zTcSFFQRTvCjdfqQYa2ANjvGbnoSgj0q2MNWOYFFp2W64lCalVDJrJf5U6ThPX8zKdLm23PMbd8HC48BeMG-hQAwiOyfEqzLnRl5i2H5yW7GGUNk90FE4Ei_DP6xL_vwqyAEd74x8UJgpp6X-CY-FQ7byhm6icJeDQB8umMo-m8mzTxd54CdnPT6S1gkQCnQKHXvLSe7pgtEXwOPAwd4oP2o36-D5CDpAMoslE8oByRKz9HdHeWlUST5XINCYq-Qh-_q_JlEMFP3R_9-uM5bw1oRBZ9cmXhjXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2330" target="_blank">📅 19:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2329">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2329" target="_blank">📅 19:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2328">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2328" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2327">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=vKLKXV7Oox0GwQCBdF__C72RboXqOWxf3Qa7ttUEvanQv64zHFwqRpJiUAPuehjvGPbzMLrtm3UL0ftEiQNpmAa8O4gLI6HR83lJAPlb5V1RPMMvsJ6Ohlce8GPlfF6hU2lcRYGy4WvPlRrbAjoDbeasFV2kt7pAEHieCcPOgiVRhtwJu-awOe9vLYx8ICaPSb5NmaH_32yDaO_G0sMt1z8G64JGyIYCR3EkuzYtbIH5ez_-7K7Lix6WYcnLzGfE6u0CA01BjNxoSWbS1qSlLs200ZTEY4Mjnc7WoMQe4VOyKYcd5sXBFcFkRPr2mNXc1uqWDc_QcmX6rJ_SgVxaCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=vKLKXV7Oox0GwQCBdF__C72RboXqOWxf3Qa7ttUEvanQv64zHFwqRpJiUAPuehjvGPbzMLrtm3UL0ftEiQNpmAa8O4gLI6HR83lJAPlb5V1RPMMvsJ6Ohlce8GPlfF6hU2lcRYGy4WvPlRrbAjoDbeasFV2kt7pAEHieCcPOgiVRhtwJu-awOe9vLYx8ICaPSb5NmaH_32yDaO_G0sMt1z8G64JGyIYCR3EkuzYtbIH5ez_-7K7Lix6WYcnLzGfE6u0CA01BjNxoSWbS1qSlLs200ZTEY4Mjnc7WoMQe4VOyKYcd5sXBFcFkRPr2mNXc1uqWDc_QcmX6rJ_SgVxaCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2327" target="_blank">📅 19:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2326">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KPj8PIQwF0XjqXvkvR7yo7cQLZ_6TcWOHydjQIUE5z6-_XpHPOaimkuigF5rqq3XtkVrX5heft99ZnxbjJ5JhRfNNnx-_RMRRqC3-lnBXXRX1xqVvKdWCbd3VqIDS2vHsPv4YUBcCOIEWGpr4pDMzFAoKFsY6oxVH2AqBX2M4_dgNFSfcdRazzs5H8FfdzfDN_yF-A5z0YzHI64DYj0RvW8Av7pB8_J1zq2vS79T6b-Ud0fbkU-QjsEhlCdeOc9KCMMQHqG0hn3B8hOvYBgC7PfZ9WSr9BbCW8Hhv7mc-O81sDncDXu2USMDbSKY7yoOqVDyv5yTYjOhUZMG15ltNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2326" target="_blank">📅 19:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2324">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gZvAasyvKCwew-Op0Wg8FmKbAFsLqgLhJTNXd8ro0XJ7GZOlLtJo6PEEkPDxQTdeZrCJ8rg4UjZ8m8M8Otee5fQ2z77sHq-xEM2J9W-23cEFxhSmlwbSNRX32MBKGmlxTNFcVttqbyxxB8WAs2jY2cny0Au5prFJBA09ekTUDHG-6GoLsPmzrew74XONBiD1i8ySAZAB-Pg2QGypr38OUdH3fdx0HGI8tQUrmu_hRvQbEblomw9vFKjofhA0HDqNyXcHrMeY5zpxG0dNZnO_tIKVClDD-1g_pqFHz-U3g-HlhyqPunz1U5y37RZprn__nTz8tiiVmn7LMefO5beoKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا دسترسی آزاد به اینترنت در متن سخنرانی‌های رییس‌جمهور و هیات دولت برقرار شده!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2324" target="_blank">📅 10:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2323">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2323" target="_blank">📅 08:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2322">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZClBjMx3dPG3yypzkSFuyqNOiRAYJ4ehMOXgYjDs1d-JFm6tGNsTozJlaYzFHQ9ExnOOFcc-ggi9eU0G2uFaHikjrDxVULahBRA2TuuFC33P72t7m45_xTpADZJBUe3UOSkf3fK2EnM_Ibthj2OiR-oQ1mcKupMgkRfQcwArkV7zoidOkegQBQVABtOnD6yCT_joNf9eeIdtuRh2xFLRXhAo0VZpRXllg7v-DN_IUvKk-ITsBT7gs5LouPICX5V_ACWO-hBLrk_qS3rpguqlQ6JroIA2POu9T2RdgyTWejHh_NPKCEriIgJVWD7l2WgrhdhRzc4f7KAf1jejeGtH_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2322" target="_blank">📅 08:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2321">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2321" target="_blank">📅 08:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2320">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HFMHeoZuSOhPbRsjZTZpXXORXpycQtAQG6JnQRzy5pzU6Q42PM1b_lWoMP0LsRRnnKKUbFQSmePZug-KPIm4a0Q4RzoqrYYTGqwKEbPV_EEIjcJPEQmK5GrsbirJAuCLV3K3WKS3UUue2Vsg44y9T2OVqb-29UPqE6zQDxOd30NkIdeaOfKGWyqgYGqape6CpDY8gTMZ-PdU8SJ0zWwiXPg4nHlo25UKdd7jMp5bkPE2_EuVWEZ1sFr0noR6kzIpLXErtIR_2FJEUvADdN10cc2pzHZrCP3nphy2Whm-y4u4kBhvlBvw7KK-WjOAvBzyU7Q5t7oiNpVAi97LAhBTBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2320" target="_blank">📅 18:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2319">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H_hpgQHfwByCU13jvXoeI5dJAR5vu7Rq3YlEQi0OeqK2B28fMOBPIXBod9b-0k4XN7QiCAjqi4dRbLa1ecfXXx69rfgEKdNAWBK-U0ZD40FiMepmkTHciMlsCNBhl65B7SVuJ2zdDSn57Ed89WwGZlmxApDkzpK26FF7j0PruyisrTwdQXWFQew1DkYZz2KEgcJkSewK9r_J-6Pihldj7moXJ6sg_9hltw8PeOtYmXkiaSuJ-1M0ooMRsV9BrDwZ46526_HruXG0NT-fdfwutwTtEHpJlDrtd305AgK7mCYNIc1Jndwfn_MrSDnVDpP7pt6olP1i6pw80dqy5EBWJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2319" target="_blank">📅 17:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2318">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L-77bqfPDn9dejfkx7L9RAbVN1UXIGxtTJiwwtd92xZS_44gt0Svf3qh82-DTgvm7MmD4cIZxq5U_Or9qDeC0iK7NnqLsbgVCYZk9IaytHmNESQDIB-o0X__fX5nhT-7SGU8fEHRFfC_2K3O6XXQrNuyekIS9nwr9AtWOBC-dgbHA9qdSMGUKtNvkQQ_417dNBQJnGSnk3y0KGWw-nAJ4YmOZRHDG9TmgI7RLbmVlojKyO8GE4a-NmZzXpk2IE_RX8fuZUn7DKAix_ZLfzMTLZOnsuPsr6lgQHiEpZYNgU_udg--BKxxiafgiJeIZKHecsZqpKZ15mJ61lMSksmktA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35K · <a href="https://t.me/ircfspace/2318" target="_blank">📅 16:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2316">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VIhz70kcqL6TNL0p-kIcEDWllpjS2NToDrgFlIzzGxtRno6Z05WDhS9QmDD6JTl22qLDk8ezp5tLievw3lDoVQrtSl6qAyXzMps-sAOzCyYq6aOzxv3hyjpg4Kwi9pGqvaUkz2Azb7Y-iq4x-Vjk4Azg9oeI8y3VIqvN2kWe2Rre6zVSMTMa9Hy1QK_361jzlrn4rdDxUVCvVImFbtF0mKSKj6K778TsWdrnKa2vysVuFwNtoL-szJg_USRiUuDGFAZNW55NB96TuBTjTuo-K8u_CYnFelTIZiG2kzgMK1AhyL--BQU8ugukF6rrDY-7JJtqwrby6RkRnoGNjkrt3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/ircfspace/2316" target="_blank">📅 10:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2315">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XuHS9HquwX7Y4Wl4AxEDLBimoaDH4ninAaZs-1-o-Gpygtqz8Y6yoVITcUnFQm_mMgEwJ22FKcCVmnMu2J4_B7zu-8uDsPS2zIRU6gCIcYi8ibvIhGroAV7vzGkcsQUMFpjPzQrT61TfYMhhGCiSX409LJAS0RGC2P09xmcbSaMIMroWoBfnZxQMKqC0ZG5uZN198ONV3DPxLOwobyeVDXz7x0lHkVl_c3y8vs6rQBEKKEfUKbDjFYST2p_dNlhmTsqjvE4CYyHSF26_knP1o2ajYFAFtaP7ODuEyp1brEO6UzvP4OadtmColKflXAXU1hmwtuRpbuVnYyXMDJlzng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2315" target="_blank">📅 08:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2314">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/syrCjUCrPgkdhFjK5CqbrfN3CuC9YZ3d8Z6AdtbBJNql1n2mxVGgUYcXVfSBDbto3ZnGF3LhrFTc3maE7Y6qn20lT5q8tELx-FrWlqhim3HZ2coS4fiNs6PA5b0ZjMMKeukfCCbykq5gTMvA3UrtNHLGoNxCGu98le6mcRP9rtF0Rhzf_EEjMvFROTlr8Atk2IsWk_5dPdEW7vhn9ztT7hCSqpKRGKINjwCIBJf6FqItCytMuEodWGEmecgbzGlYO9OXhwHzNU5nRYGjJ_vGEVmAjli92-cCDfIbuc2t2bh3K_BcGdoyZIN1u271zML5-bIjk_EGKUNuIx2vSorShw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه روندی که نشان می‌دهد تصمیم‌گیری درباره اینترنت و سطح دسترسی کاربران عملاً از دولت خارج شده، وزیر بهداشت برای رفع محدودیت دسترسی به پایگاه علمی «پاب‌مد» مستقیماً به رئیس مرکز ملی فضای مجازی نامه نوشت؛ اقدامی که بار دیگر نقش کمرنگ وزارت ارتباطات در سیاست‌گذاری اینترنت را پررنگ کرده است. /شرق
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2314" target="_blank">📅 08:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2312">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S9Qb9Dfg8sMp8sgzbsS1MQkiSETlNIPCqYibgugO067Bt7avBZzGJqFzfY4eVOD-_3NXMbQesloGamKhlrd82ttzIrZk-4Ogec0ySWJTjvgqFwopBuUBdVC33XAuwlHSq9GGptm_Gzr1Yak7HI7YPiy1Rft5wrGh3Ka4sxl-2qT58GlmxiNvwLFRxApJkPsyqwzqs5hRECFi2hHM_fMdORY3efnYzcROVhni1_wv8_nqZKav5E5PM7oDi3JCswtJ7sZNJxGncegKsPUeV8Up_l_wJCCTGEPbRMKx-7DyTKOMpAFzuzDaSwBUBhhueGuxfrQ3D-cDDgO7YmxSFa3Sfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2312" target="_blank">📅 08:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2311">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U_XwuT5zOUQH5q28fOuyOypX-cY3VCAmPJ35a0jN7QVNg8NlnVBIyS52xPq0dPcLUNtR2nEnz_oHnM-jhebmrh4IhujlGlRuvq-RfcmjnLVcaqDuGmTuGbnIAaSk6NqEw8k5Q_lypdIywwUlTdZkCKYVi9U3FkZCwFBcfeNIovMnVEwIsQ5Qw0pkZArTyJq5QuB02zTSAnWimSIrXQwyleqt4uQlOq2xnHtzNo-5bL7l5tv_HqvDx60REocPWbHJeyQ64iAFYBdaJ87v2t9-VXvfkwJ4MOkBWpbLzEL22WrrpZ-CyNIYAw5HH1lGswcs2_d0cHVb_UDL6aSCvmbnxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پیامرسان_بومی
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2311" target="_blank">📅 21:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2310">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GQUmTkpAd39YbM2k9z1iRhqTncwqzGXQmZwf-fxe_IS9JaV7QnS3A0beHdUn5Tia2HuZ7ZLUg9cY_QygzvSViIuSg7eBpT8AQf8wha3Fn8CuZBABp07UdnfrYaniw2iUjnG3HcdmMiKiQR0dgl7e61P0HNW4KHcSleBFoAyZ6rSeuIMw1CNMQcNqDL5T-U1lO8xUOsQvl4SMii4JiioYUXJtGFIhtKLqZGWzCdQLWEgvAdthe0U28J7iVQxTozRxDp_CxC_u1x5NwzGqnli1fcFSR38iBiJX9PT4Ca3RNZSV_gEDDd3MUIdvTs9riwNMvEJfjgBWuIjiZaB6JEYxIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2310" target="_blank">📅 21:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2309">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تا الان توی هیچ پستی نگفتم که به پروژه‌هام دونیت کنین، چون حس خوبی به مطرح کردنش نداشتم؛ ولی شرایط همینطور پیش بره احتمالا سر چهارراه نشسته باشم
😂
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2309" target="_blank">📅 21:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2308">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2308" target="_blank">📅 11:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2307">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZtTSzJnWYeAMblZJ7SqWN0p0FsVS8x_ILW9qFRm00uQAt4QTpyVUvmD5fvg_FUyFRTIcIluQTrhfc4gV3V8sWwrb5YweB0qX5zLRX96EdzLK6mDCgigM799C13dVsqZcNhR1y1lFlj-RNgz24GfLXnjS-DHBqvYGwNdv4_5u0yJLwN2E08GsWpJJ3jwBD-kgWFkMs_N0Ts3TVow_ZIzkMkDn1FG2GBmjV_MuVUbCmyI5WujjxLL5sdb43LR1mcB_XEQIMd3OgELL5q6aW_vW1mwQN9oX01DlWTiujDQZMxItlN-bzcyGW7o5VjumygTE_bv-YDUcBwfD0sQfkz4r-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور از وزیر ارتباطات بابت هیچ و پوچ قدردانی میکنه، بعدش همون وزیر از رئیس‌جمهور قدردانی میکنه، بعدترش همین بدردنخورها دسته‌جمعی از مردم قدردانی میکنن؛ اما تهش می‌بینی ۷۳ روزه که اینترنت قطع هست!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/ircfspace/2307" target="_blank">📅 08:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2306">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jKBeL-3WwSsZf7K_qpkn1L8jKUMeiW8TRp08bWzN6oL6J4L5r_Y5wpi8TW_dgWG4roIajUdsXvz1Y-8hXALD4oN5vtOgl1y0Km9gdVoHwCdgpujXc5yeiBPUM-AQ5T4XrGJp5LUAk7YA7ocDSKX3FsOKkaa7j-6NC38oMMVsx0547IKQBp2GCfDNMft1FU96jycmfOLZJb84ybWYyp4jzPc4Bb0Iyv-_8KkwroBRu4ATZEeWuRF5ZBGq33WgHDLbEYdVy8C7kuW9tiiw306sfwEo1nUKTRsnp-ux1gMyyLZ7eWnQzLOEy6rm0cXHrXqbjGYSI3LvGkoBH5qHJIbF7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2306" target="_blank">📅 16:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2304">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dphhWTUzbnjXrwwY8jTRI8hENBdgvcZpaFoyYuIAEOZ28IuKpVG8ZPQ5OoQLfiqr9ssWBcqwZuvLm0D3qkqBgDDqOCg8cIHb0sz6MWhsNoefJ8br6I6JPX3MrdqXrZIZHCHu3ia2BzoyJyTi2uQdyVr8HsnIfEhXf1e-laBJXeRO_kkXJq1v69vliDbwUDr33rh96SdLtUs-zx8KSNZ4loY5kjJAAyRlOHwMs64egJdrfH70xF-5mFrRBwk2zn58z92_YWJJZaMRmoSU1Z52gc9volC4bcPh_2WpezSixBkZ4JeN1JLByIxG4FpBMws9LE9fVp6JQ3FlKMGSu42ECA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2304" target="_blank">📅 12:30 · 20 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

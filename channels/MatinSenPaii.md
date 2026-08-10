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
<img src="https://cdn1.telesco.pe/file/cQz-Q_p8xGteX3TCf1LbjiBySuwUnvkP780ibRZ54SXMuRBHjqb2IGMB0RVxBPPiG-WjBpcmCgm3VG1pxr6OZGncfHybzvbYxmP5baofmEONtIKXPsWfEr0TiFPNQxqEDkpcKnsYpgX9oU8vrvBNTngm2cwPvl8FDOwOcPjqvJKJGWcr7nuMNihwf1rEpMJNnmWNoTzx6an1J0ekEg1RGLaX_CAiTFNBCC609VFLOpyjlVXI0pcDyJEzE2cKYKXWy5XN-J1jqOnBQWYfYfST2yeJXVy-U0ja1-VhOQ-eUCi1VIS-qGIDE379XUA_d7RhtZ3dicbx_TI8vod3vcQAzQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 23:37:40</div>
<hr>

<div class="tg-post" id="msg-4892">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شاید بپرسید پس چه کاری؟
حالا برنامه‌نویسی آره یا نه؟
باید بگم که نمی‌دونم حقیقتا. تخصصش رو ندارم واقعا که بتونم تحلیل کنم
و به نظرم باید ببینیم AI به کجا میرسه
اما یادگیری رو متوقف نکنید حداقل. به قول جادی، یه چیزی یاد بگیرید(هرچند جادی میگه ai، استخدام برنامه‌نویس‌های تازه کار رو replace نمیکنه که به شدت مخالفم در حال حاضر. به نظرم تا حد زیادی نیروی برنامه‌نویسی کم شده و فقط متخصص‌ها یا کسایی که واقعا علاقه دارن یا ایده‌های طلایی داشتن باقی موندن. حیطه‌ی برنامه‌نویسی هم مهمه)
اما خب حواستون به حرف‌های غیرمنطقی و امیدهای واهی هم باشه.
و سعی کنید خودتون تصمیم بگیرید. و توصیه می‌کنم حتما علاوه بر مهارت‌های نرم‌افزاری و پشت سیستمی، یکی دوتا مهارت فیزیکی بیرون از خونه هم یاد بگیرید
❤️
نه تنها وضعیت دنیا معلوم نیست، بلکه وضعیت ایران صد پله بدتر معلوم نیست</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/MatinSenPaii/4892" target="_blank">📅 23:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MRdJh7GAlWILj7cydzebow6mUTk8gND5QpmTc5IZuTB-QzTuJQpDrSEtqWj7iwCunqFgYFFZSmmW2YsnNsQZN1YhSLvxIJLBbKMMmGc0lv2OkbrxYGRMOwMsrU_bl5TxMJ2bgBkKwIfD5yfgDAmnxsnwfNVPZu2aMGe9nV55KRz-fcfBAXIxIf2fMTULq7aJXpgbVbOlYF1kvsuS245s3W-ffrFU5_wjCIlQvPAV6vj8cqgEMyZkJbaaRwT7kF00IR5qDyWEAPN55oYYes0ROiDItI5l1KCxVMTyy8UfAw_USCj25HaJm15V6LIA2sFPs7XcYqW22snm80e7gvbCnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">21 سال تجربه توی گرافیک دیزاین، UI/UX و Product Design دارم، الان هم که چند سالیه با AI سر و کله می‌زنم.
از زیر پله تا شرکت‌های اروپایی و امریکایی رزومه دارم.
سن‌ام هم دور از این 35 نیست.
بدترین زمان برای ورود به UI/UX عه، قبل AI شانس زیادی نداشتید، الان که اصلا شانسی ندارید!
✍️
Diego JR</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/MatinSenPaii/4891" target="_blank">📅 23:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/biHbcGbqVE0hU7lXS23mHL6SFEOOG14-HWtCITQpz7RkW44xzcPZGHj5QsHrG9fip7PvEyRFwQY4Vsq3tr2kdXHLy8MMFE-EIXPdWYrlY_IbSlaW6Tqdxtdz3ZUQA3WRpMWP0Jh8wLXC3HMIY8JZNGrkNlShvNeRLY4OtsJRd4PoMyzrqvXti5dnqzX_OgHx8aQqkNgZRRECwZ2wraM6jX8fZSHyCLzKnczQ9QJihQVY8gixs_MYNjuGkFdJIiFPW99uLO3fG7nxE2eWuSwNU5GbACAI26AYbkIg8KbYjUgFNSoqHpMuEv6dDjcGY2pxg7jDBXFdjinsUwVGoJ5DPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز نشستم با Hermes و WinDirStats سیستم رو یه کم پاکسازی کردم</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/MatinSenPaii/4890" target="_blank">📅 20:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کاملا موافقم و به نظرم هیچکسی "عقب" نیست
با کلا یکی دو هفته می‌تونید به ایجنت‌های جدید و api هایی که هست و... مسلط بشید اصلا نیاز به تلاش خاصی نداره</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/MatinSenPaii/4889" target="_blank">📅 17:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">به نظر من کسایی که هنوز نرفتن سمت هوش مصنوعی آنچنان ضرری نکردن، چون الان استاندارد خاصی نداریم هر شرکتی چهار تا Agent برای خودش راه انداخته و داره باهاش پروژه هاشو جلو می‌بره ابزار های هوش مصنوعی یه دو سه سال دیگه پخته می‌شن و شرکتا یه همگرایی به سمت یه استانداردی می‌کنن اون موقع دیگه یادگیری هوش مصنوعی اجباری می‌شه، ولی اگه هنوزم کسی نرفته باشه سمتش با یکی دو هفته شایدم کمتر بتونه تمام ابزار های ترند (نه استاندارد چون چیزی هنوز استاندارد نشده) رو یاد بگیره
عجیبی ماجرا اینجاست یهویی یه ابزاری چیزی میاد توی یه ماه 50 هزار تا ستاره گیتهاب می‌گیره بعدش فراموش می‌شه و یه چیز جدید تر می‌اد!
@Linuxor</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/MatinSenPaii/4888" target="_blank">📅 17:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4887">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">نمی‌دونم واقعا یه سریا، کی می‌خوان بزرگ بشن
کی می‌خوان به بلوغ برسن</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/MatinSenPaii/4887" target="_blank">📅 16:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4886">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">«الو بابا این پسره منو اذیت کرد بگو سایتشو بزنن فیلتر کنن.»
خیلی سایتای فیلم و سریال و انیمه و... همینه وضعیتشون.
تازه من دورادور در ارتباط بودم در جریان یه بخش کوچیکیش هستم فقط</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/MatinSenPaii/4886" target="_blank">📅 16:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4885">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">با ابلاغ مصوبه جدید هیئت دولت، مسدودسازی و اعمال محدودیت برای پلتفرم‌های آنلاین از سوی دستگاه‌های اجرایی ممنوع شد. از این پس، تعلیق فعالیت سکوهای مجازی تنها با تأیید رئیس‌جمهور امکان‌پذیر است و مسئولانی که خارج از این چارچوب عمل کنند، ملزم به جبران خسارت‌های مالی وارده خواهند بود.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/MatinSenPaii/4885" target="_blank">📅 16:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c92W6Kr_U-VLY-ZihB9r6uQ1wmUX-3RUq1tslCyd7nVQ2IBy30qBHX91oWTRspI88OfRzYiOvMvJ5iV1ir0Xxa-gdbaE3f4YGvEAE1oaT1FObo23_DIuz4-euf7cwHdc6D_L0IRtqCuQVAyr41m6rZiQdA7HCCoR2lLR9WB6nZytLm_pYPXvhS1LgcSTssn0AwJSC_OcpmdphGRF9b8cBcVLvLZi-2IPOClaijk4sn-aLFQM37RPshsuabrOuj2ZUWweRqSAHpUyFjd11yG9qj4WKW5DAYJLBGVca2wDKY3nswJv3ZdDMP7ml6crKiiiFeAqJPClbE_nQZEn6zg_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Free Movie هم بامزست. دو نفر می‌تونن با همدیگه، رایگان فیلم و سریال ببینن
https://freemovieir.github.io
هر فیلم و سریالی بخواید، لینک مستقیم دانلودش رو می‌زنید اینجا  و Room میسازید و می‌بینید.
در واقع استریم نمیشه. Time Code کنترل میشه و چیز باحالیه</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/MatinSenPaii/4884" target="_blank">📅 16:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4883">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">دوستان، یه توضیح مهم درباره پروژه X4G که توی ویدیوی بالا معرفی کردیم:
بعد از انتشار ویدیو متوجه شدیم که به نظر می‌رسه بخش قابل توجهی از پروژه X4G از پروژه RVG گرفته شده، بدون اینکه اعتبار مناسبی به سازنده اصلی داده شده باشه.
🔗
پروژه اصلی
(لطفا برای حمایت استار بدید)
https://github.com/arvin341az-glitch/RVG
✍️
برای اینکه از سمت WhiteDNS حق و اعتبار سازنده اصلی تا جای ممکن رعایت بشه، این کارها رو انجام می‌دیم:
- اسم RVG رو به عنوان ویدیو اضافه می‌کنیم.
- توضیح مربوط به این موضوع رو در کامنت‌های ویدیو پین می‌کنیم.
- لینک گیت‌هاب داخل توضیحات ویدیو رو به ریپوی اصلی RVG تغییر می‌دیم.
این جور اتفاق‌ها متأسفانه توی دنیای Open Source پیش میاد. ما قبل از ساخت ویدیو با هیچ‌کدوم از توسعه‌دهنده‌های این پروژه‌ها در ارتباط نبودیم و طبیعتاً تشخیص اینکه یک پروژه از پروژه دیگه کپی شده، همیشه از قبل ممکن نیست.
ممنون از دوستانی که این موضوع رو به ما اطلاع دادن.
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/MatinSenPaii/4883" target="_blank">📅 15:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=YJUYdbGw_iynk5635yw6pWe5fBkYtennzKCjJSmi-yuwvOBP7CqTvhdATuoTAesEWpYlXw1QxhuFYMbBf-LAUUWrXrgAfLcbbB-pAL3SY8unrpnlKdCiPibuM4LPwlPo_DoGmahjhHLXI8nDJjfnxx8uG2egBKbkIcdORDAtWdMnijFqQxnMoADTwiIDt-acG1g37OYRglJnxLUA5btGPR59UWVuCr16QlOZ_my5EF3ydVp-F4Z2xIbonxoH220g_9sNJ4lLDHJnSqZxGSoSOcKjJaYL9xHafdxQSiB2MB4E1kmBqP6kRHYtFaMUgcK113nbbam2tEQ7F4-MjGzBqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=YJUYdbGw_iynk5635yw6pWe5fBkYtennzKCjJSmi-yuwvOBP7CqTvhdATuoTAesEWpYlXw1QxhuFYMbBf-LAUUWrXrgAfLcbbB-pAL3SY8unrpnlKdCiPibuM4LPwlPo_DoGmahjhHLXI8nDJjfnxx8uG2egBKbkIcdORDAtWdMnijFqQxnMoADTwiIDt-acG1g37OYRglJnxLUA5btGPR59UWVuCr16QlOZ_my5EF3ydVp-F4Z2xIbonxoH220g_9sNJ4lLDHJnSqZxGSoSOcKjJaYL9xHafdxQSiB2MB4E1kmBqP6kRHYtFaMUgcK113nbbam2tEQ7F4-MjGzBqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش ساخت فیلترشکن رایگان X4G + پنل شخصی
این پنل تقریبا شبیه به سرویس BPB هستش اما روی بستر سرویس Railway اجرا میشه و سرعت و امنیت بسیار خوبی داره.
🔗
تماشا در یوتیوب
https://youtu.be/8G7xioYZqPQ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/MatinSenPaii/4882" target="_blank">📅 14:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فلفل چت یک پیامرسان متن باز سلف هاست هست که روی سرورهای قوی تا ضعیف قابل اجراست قابلیت های هر پیام رسانی رو داره:  - چت های شخصی و ایجاد گروه ها - تنظیمات پیشرفته پنل کاربری - پنل ادمین با دسترسی و کنترل تمام قابلیت های اپ  نصبش ساده ست و با یک کامند انجام…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/MatinSenPaii/4881" target="_blank">📅 13:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromZethRise</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A_70SQLABQbY3oNpgFW6Q8mM8OYOHMHSZ_ksQzHwQAmvsmb4UkY3F17hBffu9c8ZojsrPjamr5foAJSe3eWuUsT9hHLhOIgh76_p5LrpXZSeX1GOjYjZA0tfQcc4xqIB0iWuJPlecwR9rRIJi9LC9cBuAClsrBEtLH_e6NaUUn94InQ0LE_QP6ZJ2PLxPhQW1KB9RjKvubPBRbm1Tg9mtlmtQjYVkrOZI2Ag7y0Iovvxb33H10LEfH_kW4-wTKh_jGesx-2dsmKqUPTHMkH2c7bidLsJixDJFG3muTRw2HNHi5gJXBHzc2ZMjwI4RC5wf4rhIbn1B8fP0TtGO7w3Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلفل چت یک پیامرسان متن باز سلف هاست هست که روی سرورهای قوی تا ضعیف قابل اجراست
قابلیت های هر پیام رسانی رو داره:
- چت های شخصی و ایجاد گروه ها
- تنظیمات پیشرفته پنل کاربری
- پنل ادمین با دسترسی و کنترل تمام قابلیت های اپ
نصبش ساده ست و با یک کامند انجام میشه:
curl -sL https://git.diastom.xyz/ZethRise/FelFelChat/-/raw/master/install.sh | bash
و سپس با کامند
felfel
در ترمینال سرور میتونید اون رو مدیریت کنید!
درحال حاضر فلفل چت ممکنه مشکلاتی در UI داشته باشه و همچنین در backend چون نسخه اولشه (v1.0) پس اگر به مشکلی برخوردید توی ریپازیتوری issue باز کنید!
👩‍💻
Git Self-Hosted Repo
📱
X Profile
🚀
Developed By
Zeth</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/MatinSenPaii/4880" target="_blank">📅 13:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4879">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دو تا از دوستای خوبم امروز همراهم اومدن و اذیتشون کردم و کلی تجهیزات گرفتیم
🥰
🥰
به زودی خبرهای خوبی در راهه</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4879" target="_blank">📅 18:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔵
WhiteVPN Desktop — نسخه ۱.۰.۱۴
🔧
رفع اشکال آیکون نوار وظیفه (taskbar)
در نسخه‌های اخیر، منوی راست‌کلیک روی آیکون کار نمی‌کرد و امکان بستن برنامه از آنجا وجود نداشت — تنها راه، Task Manager بود.
مشکل از حلقه‌ای بود که پیام‌های آیکون را می‌خواند و روی رشتهٔ (thread) اشتباهی اجرا می‌شد.
اگر نسخهٔ ۱.۰.۱۲ یا ۱.۰.۱۳ را نصب کرده‌اید، این به‌روزرسانی را حتما داشته باشید
📥
دانلود:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.14
@whitedns</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/MatinSenPaii/4878" target="_blank">📅 08:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4877">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(Dᵢₐₙₐ🍓)</strong></div>
<div class="tg-text">📚
آموزش اسکن Resolver و استفاده در WhiteDNS (cottendns)
اگه دنبال یه Resolver مناسب و پایدار برای راه‌اندازی WhiteDNS هستی، توی این آموزش قدم‌به‌قدم نحوه اسکن و پیدا کردن IPهای مناسب با Clean IP Finder و استفاده از اون‌ها در CottonDNS رو توضیح دادیم.
⚡️
🔍
کاربردها:
• اسکن و پیدا کردن ریزالور های مناسب
• بررسی پایداری و سرعت Resolverها
• استفاده در WhiteDNS
• بهبود کیفیت و پایداری اتصال
📥
دانلود ابزارها:
🔹
Clean IP Finder v1.3.6
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/1.3.6
🔹
WhiteDNS v1.6.0
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚡️
ابزارها رو دانلود کن و طبق آموزش پیش برو.
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/4877" target="_blank">📅 08:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4876">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
امروز اومدیم با یک
#آموزش
کوتاه از کلاینت/اپلیکیشن incy
🔥
داخل ویدیو به چه چیز هایی اشاره شده؟
. ایمپورت کردن کانفیگ ها
. وصل شدن اتوماتیک
. تغییر dns داخل اپلیکیشن
. تنظیمات مربوط به تست پینگ(مشکل پینگ فیک کانفیگ ها رو رفع میکنه)
. وصل شدن به پروکسی لوکال(باگ کانکتینگ تلگرام رفع میشه با این روش)
🔛
خلاصه:در قسمت dns از quad9 مقدار گفته شده استفاده کنید،تایم اوت کانفیگ رو بالای ۶ ثانیه بزارید در صورت باگ تلگرام از قسمت پروکسی استفاده کنید.
دانلود اپلیکیشن اندروید
دانلود اپلیکیشن ios
دانلود اپلیکیشن ویندوز
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/MatinSenPaii/4876" target="_blank">📅 19:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4875">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TGmsec6byJUcNHVYTtHV12HK2APo0_BCBFLknG488ma5_b5CUzzmW4FRo-Z3QcFok4GtDulv-vD7AOBJ8Ggy7IKb1xV1tk6nenUAdPOZqJOllBvmQtL5S4dvRnM8fr7aFqwbOSdBNByXWUIDMYPEeg5m6-mil3wYKPbgdkHUsLcMjnTANs_3mMe9ddSaXjK1K4N7NgYE9WTS0NfuPaV7-XcLBPvYYZQe9KVcxQYcaMNwXpP8PhIEc__S8bKJU36W72XmAH2JZ5ph-Utql34FEtjTYXO8kugdJ6W6fYE3LeCV5O2-kyaoN71VnpBRnqes-OduF_hJbl8HZjEV8VCYkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مغز دوم و هوشمند برای ایجنت‌های هوش مصنوعی؛ پروژه‌ی متن‌باز Synapse
🧠
حتماً دیدید هوش مصنوعی‌ها بعد از یه مدت حرفاتون رو فراموش می‌کنن یا اطلاعات قدیمی و جدید رو با هم قاطی می‌کنن. پروژه متن‌باز سیناپس، مثل یه سیستم‌عامل حافظه‌ی طولانی‌مدت عمل می‌کنه که روی دیتابیس محلی SQLite سیستم خودتون بالا میاد. این ابزار فکت‌های مکالمات شما رو استخراج می‌کنه و فکت‌های متغیر (مثل شغل یا محل زندگی) رو به شناسه‌های مشخص وصل می‌کنه تا با تغییر اون‌ها، مقادیر جدید بدون قاطی کردن جایگزین قبلی‌ها بشن. سیناپس اطلاعات قدیمی رو کمرنگ می‌کنه، تداخل‌ها رو رفع می‌کنه و به صورت خودکار مانع ذخیره پسوردها و توکن‌ها می‌شه
👍
این پروژه به صورت سرور MCP ارائه شده؛ یعنی می‌تونید اون رو مستقیم به ابزارهایی مثل Claude Code، ادیتور Zed یا Cursor وصل کنید تا یه حافظه واقعی و تحت کنترل خودتون داشته باشید. سیستم بازیابی حافظه‌ی ساینپس ترکیبی از سرچ معنایی، متنی و فاکتورهای زمانیه که همراه با هر حافظه، یه شاخص میزان اعتماد (Trust Qualifier) هم به ایجنت می‌ده تا بدونه اون فکت چقدر معتبره.
که به نظرم یکی از مهمترین قابلیت‌هاش هست.
با سیناپس، ایجنت هوش مصنوعی شما به مرور زمان با بازخوردهاتون هوشمندتر می‌شه و تمام داده‌ها هم کاملاً آفلاین دست خودتون باقی می‌مونه
✌️
🔗
لینک ریپوزیتوری پروژه:
https://github.com/Danialsamadi/synapse
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4875" target="_blank">📅 18:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aevZ1Bk7_IUF1kq1ZVwH9hkhrKqnDyIg_yPqVsJhWFevKIyT4SHKDEUCf3-Q2nTN83baQNoPP0tBEBMZzcVcI5MkYhpCvWi-gVwAfjWZw4jUGaiizaImxHtEGb8kEZou57fqvVFdSV_e8kMN5kqWj1dsYjtNDC_MLPp-L1uK33Jvkk3ITJi1N2mYb7ZWK03bVoZErcXniWF5i1N-DLP19lGdh_vGFnOoI1Cc4EHj0Yfnp--6Vj70gNsI03o8SsRu0JhQqtJVK3caO9_S61JfK2X7j32EPFTnnHn_y5uUVhUfLSgAbetUDVkzgCJjExeJN67zZOpU96ojbtjdusQGnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاملا درسته این صحبت.
به محتوای ویدئو کاری ندارم، اما خندیدن به اینکه "آموزش «چگونه وایرال بشیم» خودش 60 تا دونه ویو خورده، هر هر" قطعا از کوته‌نظریه
و صحبت این دوستمون کاملا درسته.
اون شخص داره این ویدئو رو برای یه دسته‌ی بسیار کوچیکی درست می‌کنه، و کد تقلب نیست که بگی نگاه کن خودش نتونسته:)</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4874" target="_blank">📅 11:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نسخه‌ی جدید Grok-Build هم اومده که زیاد چیز خاصی اضافه نشده، همون بهش نپردازیم بهتره فعلا</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4873" target="_blank">📅 23:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Zvdm5mk4Ct3CTyrz4oCWM5RAu035w7ZFXz1sxPN9RTq64NvwgRWwjehC8hF8qN8TmxjRsD5gw2czuLK33-2DUdbYEo80ijF9qvtqX-ts3TkdZR_XR6R8E-oFz3aV5o37HAA3pX-WXODBHUXEkSh7ZVfn0Hwy6Z_2rNt69TArM1TpEGvOqYFbB7DnOVjjx_3Ar9qDK66vIq7YYFc5qsM8VBJXN23-u1Udh-0ftFYoiETQtZ5cytjLLLDtgEtw3exscBZd22c_VGqn4rOEar3_t3kYicS4Y1sbKA4xdXCuRV3pBe957WiGL_V7UQ1gl69A2j1LCJM98u2MpKw65LeZlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JzeJxiQo-l_9rjxNzpHcK9qLTDvTWQpNR4_tRkNYAEqWTMwjbFJC4Z9ZvP7aPQK_eJjgaR2wL0R5Jwssdpmdz15E-e84JTVuUrewDSePSxyObUoH52Mcd1zeChXy_BQ7l-fAxMtnLs0BBxiYe6buKul01d8c3vcWlVLhPO_la0s8uUCcFRVvb5gPLOjr03lZSuzbKL3SJLM8rHkgSN9qHR2Z2VO-vRLqmSeG3Sl8QdFxAmSjAb9Ude_ON3Cx83x-ujkL57JLgNa5eI4XsG4D7Y7UtT9YUow9PhNQRqjk_wZ8k-MGmNRW8PNLjppvYoY9nWl5F8OO0uCmK7zbyaC7VA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دسترسی رایگان 14 روزه به تمام مدل های zed code
ادیتور Zed اشتراک ۱۴ روزه Pro خودش رو به همراه ۲۰ دلار اعتبار رایگان ارائه میده!
​مراحل دریافت: وارد سایت بشید تیک Free trial پلن پرو رو بزنید
zed.dev/pricing
با اکانت گیتهاب ( قدمت حداقل 30 روز ) لاگین کنید
✍️
CypherDeveloper</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4871" target="_blank">📅 23:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یه مدل‌های خفنی در راهن که باید وقت کنم بشینم راجبشون بنویسم</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4870" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انقدر اخبار جدید از AI میاد زود زود که به قول یکی از بچه‌های توییتر نیاز به گزارشگر فوتبال داریم دیگه تولید محتوا کافی نیست</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4869" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4868">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yz3sqHSoTJG0UDvdlHwx8GAo6tvOfr9A-14ncGcQxr-LS-rRbwoU3Bvr55OwaRq0RdT6Ulm8vEGbzQx6kWJQFH9MQ2UputKEeSoWTSctZrlCPAfMBDjpaWKAEaC4QAV54XGvy2fIuN0H198FsPXTPNvduqRfOOVNi7eHvb0PpQk_M3XoLVMZs1P9qWZL8V1tT-4tvKeMJFYqes6B7mn_avj2pWL_riAGK29Thu7_b9HS5DUqxNR2kuGuxKMbNrO0OzTHp5WgZV0I25B8WeQ6ksLdJC1CKL93-4CjqzUHMSYK75ygyOJ2GMAXeBCxs6-SqzcaaDIabKwOTKGupHjzpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین اپلیکیشنی که برای نوشتن چیز میزایی که توی ذهنم میان استفاده کردم، TickTick هست. ساده، راحت، بین گوشی و سیستم هم سینک میشه می‌تونید توی گوشی به عنوان ویجت هم اد کنید. خیلی هم سبکه در عین مدرن بودن و چشم‌نواز بودن طراحیش، هیچ چیز غیرضروری‌ای نداره. پلن رایگانش هم از کافی، یه چیزی اونور تره</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4868" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4867">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مارک زاکرچیزبرگر هم muse coder داده که تستش میکنم. سرگیجه گرفتیم از بس بین ایجنتا چرخیدیم.
اما جدی مدل‌هاش قیمتشون عالیه اگه بنچمارکا درست باشن</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4867" target="_blank">📅 05:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4866">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4866" target="_blank">📅 05:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4865">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=oHM6FB7Jru07cZSApK0LmZl7LyTuk28T6mQvy7K7v3rAcBWGLkJj1i4wmnc3P3GM1lHy8RUfLUz79Qnc4faaHjBv_7C0o7UOortvYBSg7AMQP6GDu0-NJ43sKfUr2NYMgYKQfLk0KI2Lw4vgLPBmXZSOveqTnvPspEoMMqewpOvyNnXEK4xI0b_WT0WjdLMl8EsQLMkIzLw3T5ufIRW4_mHHKzB3bBGiLHsMW48F_tNvdOKVjNFeRNgZz0va9SOelKWGn7XENJuf2APRcj9fOSRMIEmhkiKA_2JZ5cDZUsp8grK2tni5sXbRT6Q9nO028wx0SVTOLW5Q5oJip14Yvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=oHM6FB7Jru07cZSApK0LmZl7LyTuk28T6mQvy7K7v3rAcBWGLkJj1i4wmnc3P3GM1lHy8RUfLUz79Qnc4faaHjBv_7C0o7UOortvYBSg7AMQP6GDu0-NJ43sKfUr2NYMgYKQfLk0KI2Lw4vgLPBmXZSOveqTnvPspEoMMqewpOvyNnXEK4xI0b_WT0WjdLMl8EsQLMkIzLw3T5ufIRW4_mHHKzB3bBGiLHsMW48F_tNvdOKVjNFeRNgZz0va9SOelKWGn7XENJuf2APRcj9fOSRMIEmhkiKA_2JZ5cDZUsp8grK2tni5sXbRT6Q9nO028wx0SVTOLW5Q5oJip14Yvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش فیلترشکن رایگان و امن با استفاده از متد های MITM و Serverless
مشاهده در یوتیوب
https://youtu.be/VYfQePhgEUU</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4865" target="_blank">📅 01:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4864">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یکی از دوستام برای رفع لیمیت اوپن کد روی 9Router، حذف و نصبش می‌کنه و درست می‌شه.
به زودی واسش یه اسکریپت می‌نویسیم که این مشکل حل بشه</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4864" target="_blank">📅 19:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4863">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=tZ12AFd01TSh4z0TrShZSJahRekVWOjDGvQkI-xdsZvlOD6uI9rs468Dp_XRTX4G9_5WQAK_qseNpMP5hIUWx4N9A_p8ubdJ_pWb-kIklgPOOcCq_weqQV3HpqjgtNjw2OLsYoXWzw-Q9lqAXP-cRWKTAp_ggu8u_yNNRF_R-w075ph8y941XYR3a4UfiUuZvHImWdwT8XNhsRYrNZRCLQPHACA9GHk171VEGteUq5Oi0XSCwRO2I0AsdvRAknDpyHn81o1eSPAYUtBOFR5sXxAIutibGVhQI6vF8NMk9rmgI9K0gbOmyowalUYp3EGNB4I7KzKUuAI4gpwR5rh1lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=tZ12AFd01TSh4z0TrShZSJahRekVWOjDGvQkI-xdsZvlOD6uI9rs468Dp_XRTX4G9_5WQAK_qseNpMP5hIUWx4N9A_p8ubdJ_pWb-kIklgPOOcCq_weqQV3HpqjgtNjw2OLsYoXWzw-Q9lqAXP-cRWKTAp_ggu8u_yNNRF_R-w075ph8y941XYR3a4UfiUuZvHImWdwT8XNhsRYrNZRCLQPHACA9GHk171VEGteUq5Oi0XSCwRO2I0AsdvRAknDpyHn81o1eSPAYUtBOFR5sXxAIutibGVhQI6vF8NMk9rmgI9K0gbOmyowalUYp3EGNB4I7KzKUuAI4gpwR5rh1lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/4863" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4862">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A8PE2DM3Zq-adENPjg9psMb-9OwlbNlP1jhSe_xKutLt2Acgg5NgUuMqOTc9it_oNe4eYKqW3nIREFsStistxdkpX27lqLOS9HLy_BRHBPKnB0O7YFD86JbRXQ5sixmkqWGRgqdaDGh_Hrn83y-T6lO2OAdGL2BUa4FWvA5A6zX6UzRqKo3fJq8diWwNeXHoRcBlbxFaJ5GH5G15xx14xwuu-PqSqvqMy5_JI5bZvQPiFPNuBuuOdCjfoBwsQvAeLp6uNmyXPd7v_RZuPiZtNquOI6YUWsryPvSCdawlLafs1_JjGGT9DPpkigse2CXKw7Qozvp4i7YxrdrJmfrijw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه جوری ما رو دعوت کرده به سان فرانسیسکو، انگار حالا ما میریم
😏
😏</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4862" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4861">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">Matin SenPai
pinned «
خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید: https://t.me/Editor_MatinSenPai شرایط کامل توضیح داده شده
❤️
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4861" target="_blank">📅 21:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4860">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اگر وسط آپدیت کرش کرد، یک بار دیگه باید re-deploy کنید</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4860" target="_blank">📅 19:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4859">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4859" target="_blank">📅 19:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4858">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">«بعدش هم روشن شو»</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4858" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4856">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i9J9c44NNyFhYEbkJ5XnyPdPs0xwcjrNnN7doVL6oUKXorFVOxO-B8rQZeiRh7Wbz5kEiDrmjjpMunUHNe6w_WOrqLJc0LgMS7EQfaI2FaihsAZU7qSlKuGn0jUosSyWljU-8lTt1gU5OuBDrbMsgggTUjLzD9V1Ow3APwhzAJARlS8HOoAPMAEnG16vxqZSzN3EKqMYWK6_DYZw3tr0I4jOJFOY7pWZvy2foctXQfhH8LuWragLwxNVfJUrrBexDffTCBHcBh1EPEVrXoUTJk5H_7VAvx_sQJEbAqhZAmSAL1YY_VjcS788-5bThqMlWXXfkCCYWfiO7hOma1gyFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rUayzKiAwGzQWbMXsgDcIrccexxZ4M5W66rtlLHI-aVn-FfqYiuka4JOsEAnUIk_rlmOoX-zza0rLR6GWVnt-jdXlZwek2JHlWEyfy9n0gbCH8SmFjwogCtP390CzDP9Hhq6L8K5xmsLtu_VeUOcIuafHBeSbPgg_vKRtOILGTxrsBwa17MZhn7tDoAIAVAub_WeT2QTMx66RCd_SKUtyWXSXSK1o6NR8j3SmpFM2lgGzqmWvNwMYK8sq3xbyk9Kz_w6gnttQEoVBPdEat8t6p5YdR_NiX73suXTCHZ8pZdYQbXGSLgcVZXEigr13HmOgwP3-qSJRyMkV3GkhlIXsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">متین الان که هرمس اپدیت داده
چطوری ربات تلگرامیشو اپدیت کنیم رو railway؟</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4856" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4855">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SNgxUC7J4SIqF0u92YRhqjtvb84x_KsSTMfjRDJ4AymxlO9QgqS7l0tylHP4bhbr7Hr3GHh9hGchmBGsrfXwcP41bhc67PzbLjsoldCO7sjyJxUtWx1Is6yNhJ4fz3lJZcZHTThlAjDmcxUOapc9soc4rQTtM_D_3-qKGwdLw8k7rqt4Ht7RSghnCqTp6Ai0ORHMklbsVdZ2faZRaR_hH0puukmnOymrB5twARd7VlVJDj8o6tP73bQjFLuV1D1MkxISSJ8E6eqjHQUX0dSoV55_BGtVyC8oLHu0TnuH2AeNMUJNzinD254QC7412d42zb3AotflQ-YYHidJw_bTTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت بزرگ Hermes، ایجنتِ دوست‌داشتنی ما، نسخه v0.20.0 منتشر شد!
📊
این نسخه که بهش "The Herald Release" می‌گن، کلی قابلیت باحال مثل ارتباط صوتی زنده، سرچ با منبع معتبر، وب‌هووک، اتصال ایجنت به ایجنت و بهبودهای شدید پرفورمنسی داره
🩰
تغییرات و ویژگی‌های اصلی این آپدیت:
1- گفتگوی صوتی زنده (Talk to Hermes): پشتیبانی از استریم صوتی زنده با قابلیت قطع کردن حرف ایجنت (Interruption) و کلیدواژه‌ای که باهاش بیدار میشه (Wake-phrase).
🎙
2- منابع و استنادات دقیق (Cited sources): توی کارهای پژوهشی تمام ادعاها رو با منابع واقعی و مستندات و سیستم راستی‌آزمایی (Fact-check) لینک می‌کنه.
📚
3- وب‌هووک‌های خروجی (Outbound webhooks): فرستادن اطلاعات و رویدادهای چرخه‌ی حیات ایجنت به HTTP Endpoint‌های خودتون به صورت امضا شده و امن.
🔗
4- ارتباط ایجنت به ایجنت (Agent to agent): پشتیبانی از پلاگین R2A v1.0 برای شناسایی و واگذاری کارها بین ایجنت‌های مختلف.
🤖
5- سرعت به‌شدت بالاتر (Faster everywhere): سرعت لود اولین توکن (First-token) تا ۸۰٪ کاهش پیدا کرده و پرفورمنس اپ دسکتاپ به ۶۰ فریم رسیده.
⚡️
6- پلتفرم دسکتاپ: قابلیت پیش‌نمایش زنده آرتیفکت‌ها، کیت توسعه پلاگین (Plugin SDK) به همراه تسک‌بورد Kanban و پنجره دسترسی سریع به دسکتاپ اضافه شدن.
💻
7- تاییدهای هوشمند (Smart approvals): پیشنهاد تایید دستورات ترمینال بر اساس تاریخچه استفاده و قطع‌کننده هوشمند برای لوپ‌های ریجکت شدن متوالی.
🛡
8- قدرت‌نمایی در CLI: اضافه شدن ابزارهای اسکن پروژه، مهاجرت ساده و اجرای مستقیم کدهای شل.
🛠
9- هدایت بهتر ایجنت وسط اجرای کار: قابلیت اصلاح مسیر و دادن دستور به ایجنت وسط کار بدون اینکه پیشرفت قبلیش خراب بشه. نسخه‌ی قدرتمندتر Steer که داشتیمش
🧭
10- ابزارهای خودترمیم: توانایی خواندن خروجی‌های نصفه‌کاره ترمینال، تشخیص خودکار خطاها و بالا رفتن محدودیت تعداد تلاش‌ها.
🧹
11- اتصالات جدید: هماهنگی کامل با پلتفرم‌ها و مدل‌های خفن جدید مثل Buzz, GPT-5.6, Claude Opus 5, Gemini 3.1 Pro, Grok-4.5 و  Vercel AI Gateway و رفع باگ‌هایی که داشتن
12- قابلیت‌های جانبی: پسورد Vault داخلی، فشرده‌سازی خودکار سشن‌ها، لوکال عربی، فایروال و مقاوم‌سازی امنیتی روی ویندوز اضافه شدن
🌐
این دستور رو توی ترمینال بزنید، آپدیت میشه:
hermes update
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4855" target="_blank">📅 18:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4854">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کانفیگای کلودفلر من هر 5-6 دقیقه، 1 دقیقه قطع می‌شن نمی‌دونم چرا</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4854" target="_blank">📅 17:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4853">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">راستی این ویس با میکروفون گوشی ضبط شده و با هوش مصنوعی رایگان Enhance شده و به زودی AI اش رو بهتون معرفی می‌کنم
🥰
https://t.me/Editor_MatinSenPai/3</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4853" target="_blank">📅 16:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4852">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید:
https://t.me/Editor_MatinSenPai
شرایط کامل توضیح داده شده
❤️</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4852" target="_blank">📅 16:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4851">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sV3A5G8wtSFlDkn5WEJPQ1ChlQajnMZ84wbRNZWhs4fNbbDJumOaWHqaILNlb76qsn72e9MfdjdFDMQgR9NcTpndCoX1-OjmBWpGYkRvvwmEAjvcgoZlAQBk6KLZoMQdIrsPcFdI7CduWMjBhuyO15m1OLDkXKOM6Vy_on_tLurLofFXzdkJqHkYLYfFJ52CJQDUBo_kOXjO6nZYoP8H9SUeTFE_ex1UmZF9O8hn7WOa6QUfYvFaKrZzdCeG6cSgpxFMZBfY54wz3MZgYmnMEW-pfhH0Ik_mZnrKANivjgC5_GZAu2kAT98LxOJJyG2n_0QDHbfzs4FKDyUxsGVmBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این اپ INCY که امیرپارسا بهم معرفی کرد خیلی خوبه
دم برادران روس گرم</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4851" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4850">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست  https://t.me/RasadAIOfficial و برای خودم هم جالبه کلا به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4850" target="_blank">📅 16:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4849">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست
https://t.me/RasadAIOfficial
و برای خودم هم جالبه کلا
به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4849" target="_blank">📅 16:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4846">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T0YF4I9D5UmXBBdzrBkGruyItNDMdPIEd7LkUjFG_7qq5PVUX0N-S-XRUKIucSl8PIC6wKppP-PWWvVPu8oactiYgC4fMXqykCrQi0ruNDyOn0p2TZxdkyzOPMapLte76oZAzGzC5Wd_AryK5pKPu5-H_sOE2g5u65Iw4VOuaQv4NI8XqCduDQFHG7Rl_9NFo5teQmq1pENLO0CymNuYolmYl-0CSd4OWATnmKIs1XmPG9TMalRUFjh2dilDQb7m7fLmAOamaUkMwa9WDx3yuVO89HGn5qAeSBcw-5apvVfh8Az7kj8Pyzwozbdu3kdW-OOfOqYWDTrACE7l9L2t9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EQ7bMVWs1NHPvIAvefK1q1oFo-QgVPzHmTIIP6700Axp8d-stEVd6T5PDoAOcW_mIbmOtaZ3gpCNv9YFHqEDshACkNK9-CVPPw6OSB3OeRxgn4_rxtwVzUmSgml9NX9-OSfxEShj2OqFhqB6QnbrHHwFBnGEre4sm40ZqeSmKdwNg3G8slBlzVXr1R9ppD_77cVCGV2cXyeTrByhzKp66cHAPoXoZD3DAwL9tycTR6KZ3Vw8PQZctuSfwI-pqLFUsD4cFyp07f2PZ5Qo6t__XoNOCa3LoyGYDegDrn5Y8_lweznSdbj656k7NBW5gbwswXBepDHt3NxqZr-xAqYDCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/chLgcC5LqS2Mw0VBJVBkIbp3Ub7Mfh8UhO_womASW0JBggrADwCGZZcrPS4a1odMST6MqTe5PYXjqDWvYO-yQ0fHjo8l_Bf_hyXT1jpygI7muQtpPGJG9N0Hb9n8oZ_sDRlY4LNnI3jHQ6_xfNqlxSyTajTVXAyAgiixAk7VL_YSAvjzamy5jL1wWJ0AI6-90qnIGk04WgN21_NJHn9h_Pn6FHyQscyU9qKY3GM5X7LCsInz14sE6bkaSildgwWKt3q1W7ZsIzD1I7Rjzf5uVLgOo-mqQsX41G0flA0HFfRxfLYyNGluF-GH9hsDpXc_VryCBgOId1Nfx_Zk-dGJfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به نظرم برای رفع دائمی مشکل هرمس با Antigravity یا مدلهای دیگه، از اونجایی که گوگل داره به پرامپت اولیه سرک می‌کشه، بهتره ما هم هوشمندانه عمل کنیم.
وقتی متن خاص اول رو تشخیص داده، متن خاص دوم رو هم تشخیص میده اگه هممون همون یه کار رو انجام بدیم.
پس چیکار کردم؟
این پرامپت رو نوشتم و بهش دادم:
توی
soul.md
هسته‌ات، برو و تمام چیزی که نوشته شده رو به یه لحن دیگه متفاوت باز نویسی کن. محتوا همون باشه، اما کلمات و چینششون تغییر کنه
و بوم! جمنای دوباره فعال شد روی آنتی گرویتی</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4846" target="_blank">📅 08:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4845">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">انگار نتیجه‌ی کارآگاه بازیا درست بود این هم راه حل آنتی گرویتی روی هرمس، با تشکر از سهیل و Moh جان: https://x.com/i/status/2084572159016382738</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4845" target="_blank">📅 08:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4844">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uIIF7jActDkh9_TRsJti-yz2M1YjAP1QD1fDcvo_2UP0UfsqE954ygEPTOAFxFjeipCBsaqVBYg208pzwn27rHIVxkq5hDi_0bUAwZiBNB9JIjemqNOmhd0kBLA7J-U_PAoh7KBAf1EeYa4sngUP8eHgEQuixFju5FWiXjYrOqQwA52OqGbBehWXD25CyL9c5k5plnuDOobyxyyHGrlA-u57T8lfYXbnvLd6AP4mGGsk00iGgO2RL08boUi5iNFig2tmcpfb-4faKk7Sd9hVHY89db0HD2sOYrRC9DwThMVcnEpZbfEvYOZ0n08YpKs4mBSyWISVTXbIYOn3_i7QjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم مسئله از خود پرامپت سیستمی هرمسه چون درجا ارور نمیده قشنگ ۱۰ ثانیه طول میکشه. میره فکر می‌کنه و برمیگرده</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4844" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4843">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X06SK48rpE3wVIGocHul6v0zdOQIYGkrytHmMYPyBcVBiP2YdsxPf2WNjH5jZ0n2TtMGfCUbrGp-ved5FnykvD1plYeHdhxFN_4R9KzJsldwKmFJ2SSMfBbWGMtpwE6iooBHNLE_ICq7CR5vwoXoxAXmzT9d8Jiqz8Q1oy-htIW2SG9QXmi91_yyGmof3kQ-dBTIHxVIf4qn8gmS57erDQeCtjKYvyuoF7-x5gVPdFUq39PM6V6_ec4Y0vt8F94TPeowgyc0d38mbKNzCzze4IPUtLcstJx_LZxx-6naEVlDkwg25J--YeFLNHgpO8YPWtG7txz7aniF8QsAsS-GtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلا درخواست‌هایی که "Hermes" توش باشه رو رد میکنه</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4843" target="_blank">📅 07:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4842">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router جالبه که روی هرمس هست فقط جای دیگه ازش استفاده میکنم مشکلی نداره در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4842" target="_blank">📅 07:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4841">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qyS12M9E6eR7gdAE_e3FjdKrmiBqvl696LJwbzoi7dX6AaKnOXyfW-19WY5ec2nL5nOW9uyZBI7pcplZU5AAnSiYtm9Psbcn19RvrUJQMZL9eTbZaCqOV3Zk8cFE89gY4pl3YekIBzCtyeOyCVcqdhu7YXUDIicxnhQx5ID8VENHpCufdQ6JwpzaqrylvUWbH4wpnwltUu8APzzfc1R_hhGVUVW4OS6o2J4-8L6M7StJpnwl7GqG4FRgQvPkck2N8MV6hN9-nTnwfEVEPnYSmAY7xlE-vB9XzJCbA-uA7PL_j6Run0DfQcJpNjACQczSDEYS6OPP60d2Q5_quozssA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router
جالبه که روی هرمس هست فقط
جای دیگه ازش استفاده میکنم مشکلی نداره
در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4841" target="_blank">📅 03:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4840">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AmfUpuNmmIof-H_b_gUMxXkzQaFepEunti3MMjTPKDA7KEj8zFSE42_ASVuLqEuPxBLpdUeiZI9DpFmgn8sExNg_SzhJTuxRA_5S8zp6XFG2NWS_ob0qQSoiFOqhtoFFcKNZu64UeMv0Vl0dKtI3drAgk91CwRMk5d7qepDB4LP_94ZcNVFt6aNmVFqEdOrfUrJTZr1q-xFApBdbEb6m6rHfwteQFmk_LGpnG0SXcwywoUYd3ENl6LT1pyrfbvvpP-Wlsfx9RDrmlFPz8QljhH8sytf0kMDj_olzmq9SFbh7aS2K604d03X4h7_UYLXL7PSPHEE1rEYxzJ2XPBKq1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچها اگه از pomodorus استفاده میکنید</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4840" target="_blank">📅 00:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4839">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رفقا ما داشتیم خریدهامون رو به دانش‌آموزهای بی‌بضاعت سیستان‌وبلوچستانی تحویل میدادیم که یکی از همکارامون گفت یه خانواده‌ای هستن که چند ماهه وضعیت خیلی خطرناک و بدی دارن.
بهشون سر زدیم، دیدیم کولرشون چندماهه که سوخته و شبا موقع خواب میرن تو حیاط و پشت‌بام می‌خوابن، اواخر هم فهمیدیم بخاطر گرمای زیاد، یخچالشون هم خراب شده. بیشتر پیگیری کردیم فهمیدیم خیلی وقته که وضعیتشون این‌شکلیه و کسی بهشون توجه نکرده.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4839" target="_blank">📅 00:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4838">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">به زودی قراره یه چالش(چالش هم نه) ادیت بذارم، و ادیتور بگیرم
خوشحال میشم که اگر دوست داشتید، داخلش شرکت کنید
اطلاعات لازم رو می‌ذارم تا فردا</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4838" target="_blank">📅 00:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4836">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WYIWQe72JkFXGm7z1w63LJTtxQPoAYj-Oje0c84qA7kUxfzVtzLhF1ueZYMK1ywPVWU4_u9OjLQN0jYY8ZxGHSA3UDpHcY2DVh_AThvCjysMdigKIAZRuPujexnDbNi9xXC7NB4KIVrp-sh4BA18svGDJgSV9POsn41t1TiEr-t5uk_lBZ6xK5g_4HUzMbhd4aSdVq-FNROYABzaXqc3PG1UlI30xrYbDI4ul2im4Az41rLjK5FrWcYEzP9zbk14p3tQWMyUjbFaCW5vzljPM_6pXKZ_rYnoB7Rn_P-k0fs26BAxelZ0U0LB3SaC2fg0K_7bxFNJ3_py5UUF6U2fxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از چیزایی که راجب کامیونیتی فارسی باحاله و دوست دارم، اینه که زیاد توی کامنت‌ها با هم در ارتباطیم. کامیونیتی خارجی، این شکلیه که ویدئوی تکنیکال می‌ذارن، 60 کا ویو میخوره اما کلا 25 تا کامنت میگیره. یوتوبره اون 25 تا کامنت رو حتی لایک هم نمیکنه. اما کامیونیتی…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4836" target="_blank">📅 21:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4835">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AAPFyEmGtfgzMRN4lgCFx0xdpTRFjOi5btHifliWMdE_zQ62jgzBmHlPEQJMSb4qoTA69rhl6u9eEqEJJblj3hfXPIy_oNQfxS8PzbikBcKbxbJbL8usLyIovYsDMJMJnMXXE0vtBds2VgDMPmLX4Iajx9PKXU4f_SfUN0eJSUcbaiW6PIWlmLi1OUlAM0Z_yL-oAPF_jQgInzR6Wy5OmADUCng99c6BHUCocW_D2NT4pt9_W0lq6kkLKF6h1eGnCmW5Z-dvrPGKTSGAmhNsG2H4qzbi0bSbaXmz82q6M8V-6YW7l-1YCqFF-RO76vJE384nyPlISDPS2YzrIRCZ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایگزین متن باز Fonto، رایگان، تحت وب
دیگه برای استوریاتون پول اشتراک ندید
😁
و اگر دوست داشتید، از بالا(علامت قلب) به سازنده دونیت کنید تا لایسنس تجاری بخره و فونت‌های خفن‌تر واستون بذاره.
لینک پروژه:
https://github.com/FontWoW/FontWoW.github.io
لینک سایت:
https://fontwow.github.io</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/4835" target="_blank">📅 20:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4834">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">و به هیچ وجه، به هیچ وجه روی کانفیگ VPS نذارید.
فقط روی ورکر و کانفیگای رایگان
چون به سرعت از طرف دیتاسنتر ابیوز می‌خورید</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4834" target="_blank">📅 19:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4832">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jh3Ig-LJ4PQTopdcccPi4jzmaRo2NwI1AmL-px_DEAtVQAJTMtwlb2eET8A7D0dRcu1QOzcrLefs9762BMxkhniaVq9fChW0GPvH28fEdFS2R8NfjJc6ZQUr2tjD2Qw2YHYMQaBYyVsIFtJhl3vy0l8rI2wNshdmJaJ7O70XbhSX-EjZTpDvwkeDm5FuN6_65UT9pRMu1-TOKeNaviRiThvugKaBtpKzfi3UlH0jNt1x5OIpk686O3BzrFk6-Bub24OvfzNomeLCMSSDLRxqkX5FJGCD-vlLGTrb8Q7k1Bjl-P8gIasCjtwzj3gnwYjRPRuH1V2uZgZsovlADXX-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l9MH1Q7clc4DPsHeCV3_NTq02X_miI7iu59PFS0KiWYiYaD-1ypSusNgXUCNnRRL4d3w2Ke8-zos2hntlBR94ThCndDkS2wVeGPbHG0jaFxfZBQFsYJPTs2Y8GcgGszwxrAQvTuxXvnwx4k75hes7hRPCyVGAApTYdP3YoB5gLKC5Mh4JYIsywc5iZ9dkdbwD_aUEEQQQP0d4JXmBxMmiUywKhAVmo_HoMKO1Mr8L8iDduoD-ot20bedgHxtNaXjsSoU_y-28L7m9sajQBxMvtI8shqOYgY1GSwGpblAfNIT8aX59D0J2u0QjoVpafMowcAp48H4ixbIpohiMr7adw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4832" target="_blank">📅 19:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4831">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/glyP4sqsDvYAHBlu_Gw8UE5ul7ieFcC5ehm306CKZAIn0aZb2BdI77MMXvLlGJpGb0mhYe2QXptEnKCx5QOyXh63-JF4z8hDim41a5Xj3JmOFqc5mZ0HhAfzJ7-k-eT-UE8-8nY0EncrtLbsQm1dJ24Hie0pxHyM6HGz5eDtKc1rWiXa_F-n_p3cTvuYdSdBr_pLxBLnqA5PfXeP6bOl2SezGY_mXwG2AZe-aRY4LgOc6i6l-oEZC2RhYTmku84EF-IoQFSP2nGZuVzbP6u4HLDPAAXdozAcLGIYJ-FE9XR6s_4eahyLAoj8xEk2Juucwm4-GS8KfSe8AVpaNwjKsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید: https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4831" target="_blank">📅 18:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4830">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید:
https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4830" target="_blank">📅 18:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4829">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خیلیا ایمیل دادن پرسیدن با چه شرکتی کار کنیم
ببینید شرکت‌های ایرانی همشون یه افتضاحی به بار آوردن. یا چنل پروندن یا..
من هم شرکتی که واقعا کارش درست باشه نمیشناسم. ولی خب متأسفانه وقتی مجبور باشیم، چه میشه کرد
الان خدا رو شکر دوستم واسم نقد میکنه از خارج از کشور و میفرسته و دمش گرم</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4829" target="_blank">📅 18:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4827">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UrkqHlgY0XrWQ7JrMpM1HPV4mYyN0jFzds48u4sYJR97qxg3v4tY4oXdX8SqihUmeg9UZVZFz0cEMxz8COXO_73rWddvR66PGX213EUasenc6MwZSTN1iMFou-4lc09iVk9ydbQODuU1suPF1andcUs_yjutQYulyAEm2eC6jmd-XonCLnw8NSmjFC6BWKbYcYYcZtYEEBDcpBXKGDBRUaLasm9wts_HeHV3l3FXWzVoxK7wbhwjBaQ8cN6RDMemvhPFkZKZ0AIlzpFoUMkWJex-UeWVrTVaXY4HRsDw2rnm-ksLIinKNAShB9dSt0oidYuV9oY0Lzq9DLhNisnVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cJ7W5rmrSXz8rB4Kly-cezgd7_xNXWDY0iQsEsUI8BV3FgYbcUB4ICIRHNL1GiN9uqlM4uTQkISI875QtYVvL9LtNuBYkoVwaKLMRB-_mPVrTCg2r8SZoyyyAwCmDhVguZBWT-wwVN7WPxae9rMOIRO5xhoOyg7U83RPzBeOHWuQi7IMxUYcv2xnooEcUEic5lP_v61rso7lKCn2uiR2X82IrdvQk2UgfIaJjyVTXPjXO5lh_0D8EHu1U8Zh8eulTjx0iQJgkCdlPRkb3Qz_--t8qHxJmkqX5bAGRV2dA1Pjh-E3dQK17Nd0KiuPja1-sLlunWmpcO7d1AHu4A_Tcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادش به خیر. زمانی که من یه میلیون تومن هم برام نجات دهنده بود، یوبر این شکلی جوابمو داد و هنوز هم اون سه تومن مال 7 ماه پیش اونجاست:)
تازه اونم با قانونی که یهویی گذاشتن.
همون روز ادسنسم رو قطع کردم و کلا حسابشونو از اکانتم حذف کردم.
هیچوقت با همچین شرکت‌هایی کار نکنید</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4827" target="_blank">📅 16:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4826">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPavel Durov(Pavel Durov)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kj12Z6JQ2_1DEbP8qymZEGOt-F3i80mkPmB67cTm0DbgDDshF3FPdA8AUZ16t0pAO7SsRdOBBd3woZlbGF_Ok9maPP0wSLEhI6KxkVAVuj-U0CqwO9FepJvm4pdFRsa9oHM1pV57sKnvlliqNxqagJ54dnYIvZjGnDRx_gl464oA1Awh0_eBFMdANW8Z3BFnjunHjXjEVJQhLuSUnMrfSh3s1YnTtTs98eJuxQE6M3eapscMny4GObmF1fsdCg5bip68JbqULSOSMsTa1C6-2I7zdkRS3yQB1skK4VUWTOo0OOioWINE_uETgfluo2Az-lT-zCTWuBIRdtAhSs1cvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
The 2026 International Olympiad in
Artificial Intelligence
starts today.
As a token of support for those who will reinvent our civilization, we'll issue
🏆
240
exclusive
Intelligence Cups
to the winners.
💵
We guarantee minimum buyback prices ($
1,000
per
Gold Cup
, etc.), but the cups' limited supply may make them worth much more on the secondary market.
Good luck, AI coders!
🍀</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4826" target="_blank">📅 15:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4825">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOVcbfLYkBUXky-tMoffs8IMdbBcusEX3baETEH-8qhs9CX2WNJkvPeg2WFCtQ-w1702jSomZIAN9obi9Wxy1crjRMtgj3D-MK_JAM_6Cz4IAxVfY3CzYw_Vl-_hBJKzSehgxG0K2Sa693XJHmYIVojGkbY_FqRLSctHa79_50PX0SccLJCxI8d7YJTtRHHdAY3lEqdntJlnjmT7UuY9puB45br8vVEofGdoNVrmPlYCdv_vBHXaQ-6H_Nq1-PUkUPjPaBLFAZGM_x9K2vahb1dDq6f0jpC7NOZhfqJsTAEr9q0b7kWFviVkU_vgTf6LJNtnNH2RVncBDqV2jUTrMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر روی گوشی VPN دارید، دیگر لازم نیست برای لپ‌تاپ هم VPN جداگانه تهیه یا تنظیم کنید.
ریپو
Relay
یک ابزاریه که با اسکن یک QR Code، اینترنت گوشی به همراه VPN فعال روی آن را به‌سرعت روی ویندوز به اشتراک می‌گذارد.
اگر زیاد بین گوشی و لپ‌تاپ جابه‌جا می‌شوید یا نمی‌خواهید روی ویندوز VPN جداگانه تنظیم کنید، این پروژه می‌تواند گزینه‌ی کاربردی‌ باشد.
https://github.com/Mahdi-mortazavi/relay
⁠
@RepoFA</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4825" target="_blank">📅 15:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4824">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VtI3ZQdryplXKRXBLUhScNEOPrvSsoLyZqePdkb8oT3byQzkZsnJdZfo56el3T1fRz6L2TwE_uODxg76rBY_pD_kfuJcKPuo7B7oiP3Rmz0-cZAvDhpSTLXCVSUiXmHUuC5kiMFqBbSB-dxLosC9V2QSgoYM9B16tauNAyk7-g4Keb90FCk0nNtw_Z3-pA2neyxMvfMPBHXLEfGflY04bbxJRQydc9uEaLHbsHFjlQhynWKwv9nu2FjH8LPYMVT-F220itptxgjVSSfN2aaBVJL9f10A9Rx0ofo_L3j_PD6E-Ry7aCzAPg0DeQriW9bEzD2zCEBjCYEkEZHHVgjHdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقااا من رندوم برداشتم از گوگل
برای این ویدئو
اصلا هیچی از F1 نمیدونم
😂
😂</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4824" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4823">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=oSQ1kKMoa-v9dcZN-xPWFjG1Jfcu-mRdx2FJ3d7p7mTyFWP-OyFLb5vNTk2L6R1z1n22fndW9idhgukS8-P0lstthmPkWpmskU--XjKnuHXSohvHLBuhaEyQPGXIagcCVaRlyCQdfnVG0ub1KnL8vj4fc8n6wSf95k3Loh_zoE1OyD3qf4gLsvBYZdd9yubS3CfgB8LfHxdqxFoSGIodKbw7reRzwu0XnZeudwm4OFtjKyrpqnmvGJx7xmZ5lS9UxJWUO3PU8eqYGC7PSaf-_Ju5z-OX6OGs3Kow6mVQbV0qmbEVDPzERBXHGGvMFEdCRJglrcuk27o8b3qf_0twUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=oSQ1kKMoa-v9dcZN-xPWFjG1Jfcu-mRdx2FJ3d7p7mTyFWP-OyFLb5vNTk2L6R1z1n22fndW9idhgukS8-P0lstthmPkWpmskU--XjKnuHXSohvHLBuhaEyQPGXIagcCVaRlyCQdfnVG0ub1KnL8vj4fc8n6wSf95k3Loh_zoE1OyD3qf4gLsvBYZdd9yubS3CfgB8LfHxdqxFoSGIodKbw7reRzwu0XnZeudwm4OFtjKyrpqnmvGJx7xmZ5lS9UxJWUO3PU8eqYGC7PSaf-_Ju5z-OX6OGs3Kow6mVQbV0qmbEVDPzERBXHGGvMFEdCRJglrcuk27o8b3qf_0twUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
درود به همه رفقا...
آموزش
سا
خت کانفیگ Amnezia VPN(وارپ)
• صبرکنید ای پی ها رو لود کنه
• بعد یکی انتخاب کنید
• تیک فعال سازی پارامترهای امنزیا 1.5 حتما بزنید
• بزنید روی ساخت کانفیگ Amneziawg
• دانلود کنید وارد کنید داخل Amnezia VPN
• میتونیدم کانفیگو کپی کنید + بزنید بعد insert بزنید کانفیگ اضافه بشه
💡
نکته:روی تمام اپراتور ها متصله هست.
لینک ابزار(ساخت کانفیگ):
👇
https://darknessshade.github.io/Amnezia-VPN-Config/
دانلود اپلیکیشن ios
دانلود اپلیکیشن اندروید
@xsfilterrnet
👑
@ConfigWireguard
✅</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4823" target="_blank">📅 08:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4822">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L3PhNuomRRivyQ_jo-fcSYNy_m9sJTJPFbxbVLM0VeXT8y1bgYGC8ZCn9tUi4Q3_6In1S2qm8sdi_ts2Ov44WtTImh_HW4JytH_xeLfCOQZoGDJ4SmT5qhF6T6yN3OWquE-ORyBb4yEtcrLhI8un0ZlSvhCBg3yoA-RR_fBc0BV9t7bldb7M8xIvQwdbtzBhYwRZ56e0AVvpmkbxHupWEuwTrqLgxVRFeQyrKFj-CjGBFXr3holztGCTw_YuvJH68cN3YUy_Rjw0r4UkX8eyBy4Gb3XwdU_wMU3TDxyBcqkhcG6xZJ_ulukCGCpEiamCE6_AF94rPzzX9iw1_XE57g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4822" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4821">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JWlaf4WcWeOwBq-c4AfYU3PBN2dvEOf5slz2om90VHJfAn2mVPjDJ6DD5HNGPHSeuyVRkRbRArw1EQUUGU3KLFDEFW3Nxo2mvT_ZlIWxjlCpNzkVIvW95yOQN439lo5vnS2vMwL8qbBwcT6EVkWCkJM7E0G0WNQQ0wAzqaWQPvdohKP-UpBC9TWPid8sU3Es8DtX5givsFBV-cBBr1PhOS8ONAv0B3weYVUCRtN3aPsXOEX8zeZmrrRsDJ9JmDgZt-YGRwnbMJld-9PGVBQn6pdC4o_4C6qCcBu2qwR3UgdkQ64gXOhEy5PQ2k19lWLEFUUjc998pHZqK63FLStmQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)
بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.
مهم‌ترین تغییرات:
🖥
یک GUI کامل دسکتاپ برای Windows، Linux و macOS
📱
اندروید از نو بازطراحی شده؛ Kotlin + Jetpack Compose + Material 3، پشتیبانی از اندروید 7 به بالا، APK جدا برای ARM64/ARM32/Universal
⚡️
دیگه لازم نیست منتظر پایان اسکن بمونید — هر وقت IP سبز کافی پیدا شد، متوقفش کنید و فقط از همون‌ها تست سرعت بگیرید!
📋
امکان کپی نتایج (همه IPهای سبز، ۲۰ تای برتر یا یک endpoint خاص) حتی وقتی اسکن هنوز در حال اجراست
🔎
اسکن همسایه (Neighbor Scan) دیگه اختیاریه و به‌صورت پیش‌فرض خاموشه
🌐
تشخیص ISP و ASN چندمرحله‌ای با چند منبع (Cloudflare، IPWhois، IPinfo، Team Cymru + دیتابیس داخلی رنج‌های ایران)
🛡
اعتبارسنجی واقعی کانفیگ‌ها با هسته Xray؛ پشتیبانی از VLESS، Trojan و VMess
📦
خروجی مستقیم به IP:Port خام، Share URL، Base64 Subscription، Sing-box JSON و Clash YAML
🧠
موتور اسکن بهتر: الگوریتم weighted-random برای رنج‌های Cloudflare، جلوگیری از IP تکراری، پشتیبانی چندپورتی، خواندن ورودی از IP/CSV/CIDR
جزئیات کامل و دانلود:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.0.0</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4821" target="_blank">📅 02:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4820">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hallelujah</div>
  <div class="tg-doc-extra">Leonard Cohen</div>
</div>
<a href="https://t.me/MatinSenPaii/4820" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">00:21</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4820" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4819">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه. همینطور قابلیت ip fronting هم داره و سرعتش…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4819" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4818">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⛏
۲ نکته برای بهبود سرعت WhiteVPN
۱. بعد از اتصال روی دکم
ه اتصال مجدد
کلیک کنید تا به سرور جدید وصل بشید.
۲. همچنین میتونید به صورت دستی تمام سرور هارو پینگ بگیرید و به بهترین سور به انتخاب خودتون وصل بشید.
آموزش تصویری</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4818" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4813">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.6 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4813" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4813" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4812">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxXGxASy6jGoEnT7RCWsYu6cSbRI0mp2eQiB9feyAqOYldAzi4x-7yR7Q_JV0FBA9j8bQnLddgSQPaXVnnC9CFlFr-TDXzg4k1gvr4pdTGBfJumflSxLv4czLxiR0lKeIBUMYowdptfqaYfcnQIkc-5r4-MBDsle97QeIu5heuSMp2D7_0ALwRp2MoeWR4_v-1eFwcFgLSgTvBtGyxAOh-UGLa8Vj2dR2z2mXvB6u5Nz5JskIR9-cPEZiy0PAbbFVNZGYn6iu8eZU4OF56dkmRBVLNqKOfRNS-745TH6L-vGIn-ExCFns9Ds5_fE2L_LRWc-E58uoRUc8Q-lpDy3YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت WhiteVPN 1.2.0
✍️
تمرکز این نسخه فقط روی اتصال
سریع‌تر و پایدارتر بوده است.
امکانات و بهبودهای جدید:
•  شروع اتصال سریع‌تر
•  انتخاب هوشمند بهترین سرور
•  جابه‌جایی خودکار در صورت اختلال سرور
•  کاهش خطا و نیاز به چندبار زدن دکمه اتصال
•  بهبود Real Delay Test
•  رفع مشکل متوقف‌شدن اتصال در مرحله شروع
هیچ تنظیم خاصی لازم نیست؛ فقط برنامه را به‌روزرسانی کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4812" target="_blank">📅 11:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4811">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k3yoywtlHD2XlaZfKOhUemec4DT-b3NKnU7rbkJZqY9G-xqvG8awgHM253qWpACaUQZYPePL8xNyO6gsYSkeypgZe3_FZZAieJ3HSpCmaeK2vKcgTYaV31vSaL_Ek-1gozf3VxOwj3z9jSHXrkRqgUdnYfVvvseZLHkVTL1KSRyuQuzqbIA9t0xnNj8umc2vz7VMf5gbrPpYJfdD0YOnOG_8G0eF_if9isBw570aa5WibEGxdUs-wYuaX5GnJlhkXSRrlPuPgRCdc1Y7kABYvq_uem-2Kax3pcIyDxAlnLUGN0rqZDFFFNhKx8wp2vjYlkV662tMdTdLw8uNRxZ-Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه پرومو رایگانش تموم شد:)</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4811" target="_blank">📅 10:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4810">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gIrL_rhbFSRdJty8rloawTSS679fbK9LHyios50GxrJHUnlWtlmIXCFnURxp0yjOrbIuQYkb2oepN5eCkPjaESdK7t0nBacRHAMSD51NQiDOut1f9P4Dc-hZtZzih_VxKQbwLSaEKgy40tQkGAz4ZFVZI9QqdosrDDJ7MZreiAwIkJ421hBb37FNzbGgNseUQleu-wEAljaJz7EyArn8IT9tMIMQXa8xSxEfsMIq8Dq8m2Y5iJcZncfOKLzgKyTZvzi0q_HA0UIElJ8f05bN7MLmdqv0p64TuPDW8iCRdET47DkRNMxYxYBkNSu2FRvn4qTgpRI5dV7oRI1ljkW0rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان بیشتر مدل‌های دنیا وارد «منطقه کشتار DeepSeek» شدن.
یعنی مدل‌هایی که توانایی‌شون کمتره و قیمت‌شون بالاست، دیگه رقابت سختی دارن و ممکنه کم‌کم کنار برن.
✍️
Ali</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4810" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4809">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4809" target="_blank">📅 06:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4808">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سرعت آپلودش هم عالیه.
قابلیت‌هایی توش پیاده‌سازی شده که از همیشه استیبل‌تر بشه</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4808" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4806">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PtncbOg1_hKWy7yrjcqtdMS6GJFSC0_jYNP73BZq8F5Pp44QduWKkVf2-lVeGNKykYikdqkymhTZWBUcv2TAXyePfwLoJcuzYcgTWKl93iIBsC810_7xq7lYwvshTcRYpdkIpaNe50dgykzDdXxNQaWHddYnM95mf_8KFCRpgjdtGVSz1l3alX_PKY9KIPbSxfj5AUgX4OmYt25NYRSIDYT_XYjcExDidAL12QrNRr6yP3vThFapMAMZssGnEZpccTO1eyn0gFZg13pw0TfKwRjJrKRVm4_56O11Ydlis2A0GUbP4RX5W68oFVu8UB1PuU2I58s6ZjS7pxot1T8kSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FnecnY8RRrKONULAgJhD54wECcsQnXI2EyNd_s9L4f4WSq-fKDTNXzOks1yvXgoXfknquGV66EFj66wCwVBIX_YowdZ2x8rUuxt0xhm2b_FsG5lmh9X9Bvzx-ttSISbFNnS_rrHDV-LxkC5Pg3iE0SNilF1JBTRExdrr_u4cI0Tyh7Es0n6SqbnlHA_1VCHnLeQ032EixoT1JTsbkGWXFTwEY0l9qBVcYNl9nhau3Rio_WXDLvb5mD8QnDWfQTUtOhN-N882T2w16kVnpLMHvyDLyAscz_1IPNbcRaj-ji4eU8zAPlAaesc70maw4FHGpTuooDwn8ZdWnzzPCKww6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون
اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه.
همینطور قابلیت ip fronting هم داره
و سرعتش عالیه(حداکثر سرعتی که اینترنتم میده)
دم بچه‌های WhiteDNS گرم واقعا
❤️
🔥</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4806" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4805">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دقیقا این اتفاق برای منم افتاده بود و سه ساعت داشتم میگشتم ببینم کجا پروکسی روشنه که بدون وی‌پی‌ان داره آلمان نشون میده
🫩
🫩
روانیمون کردن</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4805" target="_blank">📅 05:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4804">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Qwen-3.8-preview.html</div>
  <div class="tg-doc-extra">44.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایلی که الان با Qwen رایگان ساختم</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4804" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4803">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Kimi-K3.html</div>
  <div class="tg-doc-extra">41.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4803" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایل 4 میلیونی‌ای که توی ویدئو ساختم</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4803" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4802">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4802" target="_blank">📅 04:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4800">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q5fyOMAnePcrBOxldOKHO54tV_G5rUtDsx2h3h6aUiHpgqt_ReHjfuJVlIjmy1EP2_b7b6RGvrG0Hl79-OSnFwU0ca-WD2-C9Q4Ev9J-P38T8TnKbF2zosPgB9M4v_w-XGLUjClhkF-Tetqj_7enPpVl4by-mjFOEN4rvyH7C1CGezyD6I2434XkP7GAv5Uh9sEEhI9DcGtg0lJ9Pneuv_0m6gRpI88eDz8bn71bRkSCutP3sQk7WvSulwnpIss4-VOGGtL0RVzrxHhWAGu6ZquxlhTRNZXXnFgN1bHwMZGCB0HiHzVjez4qwPV90NtmOoUufvcY6I4Z8n91GC19mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XcO2wNnO5jIrePryZ23RnpITbkJLJd20IZYBR6kxYtjjUx-xXOl0kRkmENEb8Y8b3lddujcjCABFYMLFcHbm_TauzgDm01B3Bf5_jAOQswn5Wg8Jfg-htbdYvkut43-B6nGUIIjJn-eciXAoEDUavt5cMCR9AR8leC2ElSOtqhO22UcdMIEYYA-3QkakDYHdXVFAG-3O6raGFl9IVHKZZOCEJqk2xViuerYl9i-fE1W9QIK--qYrL1sL8IZf9LyGWq-iAFtM7_OjWQssBfyNPQM6ajk2W8Ao9lRYVf_OHOEqvwUIzaQzGaEr6JGhTiA0U-KeftH0AFZnrtYDpxqsYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4800" target="_blank">📅 04:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4799">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UfgZYRjC5zoGTC34-dUdjDNU2cGDYGG3kiWe--MmcDf-ymoZwNhrO0wrfW47cX9YbsCkGTQH9tfhZXwcOpuYygTPzMbeZWxfLu5j6pgZMXn1b2cxh6LIPywYaLjSSHxPjrHssTJtPFXx8h0qjocF3lj37HiLs0xvw3UR5Tvi3fuXhKVcxfH9-Q2qHEgMtcSqLBndT4kKe-VQ2IirKrvPX65uGR8gps5lP3yXKlQLN5hOtavY-gQ5CXH2talzsvfUV6bFmCxuzLJM3-mosmINFfUnyjOotml3IbZAg0FhpQZTMxaQDl6kz1W_eFp9ly9Jj4mCXs1IPphSWJxLJbN1xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان توی
infron.ai
میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.
ممنون از confesious عزیز بابت معرفی.
فعلا دارم باهاش کار میکنم ببینم چه شکلیه
تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4799" target="_blank">📅 03:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4798">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4798" target="_blank">📅 02:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4797">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت
تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4797" target="_blank">📅 01:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4796">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-poll">
<h4>📊 از گوشه کنار زیاد میشنوم اینترنت دچار اختلال شده. مال شما چطوره؟</h4>
<ul>
<li>✓ به زور به تلگرام وصلم⚠️</li>
<li>✓ اینترنتم کند تر شده🔴</li>
<li>✓ فرقی نکرده✅</li>
<li>✓ ایران نیستم👌دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4796" target="_blank">📅 01:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4795">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خدا رو شکر توی قطعی نت دستاوردهای بزرگی داشتیم و اپراتورها از وی‌پی‌ان فروش‌ها ضریب دادن رو یاد گرفتن
😑</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4795" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4794">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ggu06VLhNxQnIQ9smkAYk7BJxo8pVWHnKG1OHCR23x7UrnIgqb6wx7g9dubmjeqIvcWCOKabXVBfkmDuApigpQ63Xg2Tft_eb3KJWRxi2RDpx9mXg_KXhWz3SOPwl4VtmXCR9TNpWCObYdNM33U3cyTxq-LGtSQkCOLnr42XLXDR_GnQU5oru1dOMJbZ7OUraJaSBdlyLZ_MGbYmsapaiy2vhB9-uFbFo6WebXNa13tL2owCGu4xVTpUFJo4xqIWCL0-rL7TIuLNlmbnrR1mtA2HoQkBUDcQhU2natfRlUZMFHl52hbftoftOyGGiLHZUixBQT5BuAT8bNMCFP6Q2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4794" target="_blank">📅 00:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4793">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4793" target="_blank">📅 00:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4792">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgX8yt1mH0KmOSitMbDYvfbav0AYHu1rtN2MqxRGhXlHL9sxbMGQi8DkfsiB2yZuUr4RuIM24FXBJNLY_wdhUr6RJYZJyarb_kDuVehhZ62Qdqb5hAUdPEi5q26fZ5P2z_NjcMCiWuHgo6n7q267v8bPxzn1upcsHcc9Xb2lmqEx3nlOKx3whqdbfHNuW59SNOsuTFhQqxHqJlstbR0zPCE32LiZsaiFCeOUmBAlHEGgUvdw0ek9Faq02_e23IksNzMyR4ZDCdCT3kRTU39ZbMii4lD7skQbqXN89YPAPcWg0NQP7TogZviKkko3OzndoSW9EgCQPDEW6h4wy_zqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4792" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4791">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">به نظرم یه تماس بگیریم باهاشون</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4791" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4790">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج 205.252.xxx.xxx داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4790" target="_blank">📅 00:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4788">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AwsLUVhJP__QvQ02yev1BAzVl3JdoRd08lSNw7UQ5tsA6eDvgkGH0Kwfjbz6Uyo-igHTaK1HGz2NM8bAkeAYMikdQSJ1WPMpjuo5s9M2NHejJFJBRzK3NkTDA8EDiAO0phSGpUOVBxXTo3jZo0Q4aKWmY4b1Bk8MYacp2u_qrs2FdQ2Cw_bgASewKncJ0bWpkhCWT6aQpfRT5HiJjfFFBwDp-ekeyv3gWWIswfad6s2GUfrdMJO5h3DDJuf5HI6gyfc4bQecizvmP0n6R-Y35daywnLYFkK9-1rNyzb2hfhAYPi734SG7Eli0YeGnLoFS87bNz4H84e8icIoyp4pHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jx4vDWmO50OyxgIL9Ef5PCM2C9w2_TCDgcKMHRY_3U8v2CYhZEKX2tUlzXQVs6fCbq-dIL5ZprYUioh2OyDW-VRrpGxdYYko4nmrNFBcenWiEh5GFU8TBhcn2WAzTalmNMMp-JoWAZ9_EWPkD3BFXucw7tnnSXY_UterCVe9_mudtDRGRWGeZq5zXzb2-OmMtMCQt4aB7mtqSY1z9JZsokeC-vbci5Fj3eugE_HeVHLKTZ-ZD-yF51cumpdklh5BaGIX4cwioLkO8F7yLvICgIa6anyO3lbYMOGqLojMZWs8Nwwj4VhP25Vfep38qo88gAZ4CG8yeDYMJt6sKNMzAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج
205.252.xxx.xxx
داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل قبل محدوده 80 90 بود الان 140 160 ، درنهایت این وضعیت nat کردن اینترنت در ایران داره به یک روال عادی تبدیل میشه که جای تاسف دارد</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4788" target="_blank">📅 00:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4787">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o5Bi8OZO3sJwf6ZSKXtSzQishEjlDrJ8BYzxEUSMu6bRGEUOliGbLr5TaLmKmeQOPYtIfR4ubJ4HgAPD37cMzwxjfMIpokEiD5-i_UXZMElQHj7ILeyWvz3qBpNaBDx-92sgBiUVXjVlbroQDo6JKFM7XJuWRKmLJq2OsSs8tYj2NBAeJPhZbepEAubkLI61EcVS2VuOGZWKzSqTr_UVWDlvZBkMhTXa5i6XoWKDWAJKteC0FVEsmJ_vEzlPPnGFCgPDilv33gf0Mg2N_vjQP21EulDb7AeqCH6fyw20cgZ4RWebUB91qbcQFmpNJex0VMimA0OTZrZcOuY3RUz-eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فریم‌ورک Science One گوگل
💡
گوگل یه فریم‌ورک تحقیقاتی خودمختار و «قابل‌تأیید» معرفی کرده با Chain-of-Evidence — یعنی مدل فقط نتیجه رو نمی‌گه، بلکه زنجیره‌ی شواهد رو هم ارائه می‌ده تا کارش قابل راستی‌آزمایی باشه. قدم خوبی به سمت تحقیق و توسعه "کم‌خطا‌تر" با AI
🔗
https://research.google/blog/science-one-framework-a-verifiable-autonomous-research-framework-via-chain-of-evidence/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4787" target="_blank">📅 22:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4785">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TPut4DU33btiLHgJ3xm4ekQsjsj7gKMY1lhuIUcPadUXhddQB1HrO58GAUz6tPoKhv629_QqoyU0NOAnLyOvjCS8R6j93Ax11PDzso_FS4zqeEvcnKeKwpqd1IO4jD5qophfj5gyFlEWCaHQc5VglbzMfVPz4JdcpeGZejyVlmK1RwBLnx_IiUCNwUBFP6fxcXSqDdqYynqIt-sLiDOZo3aZLN3WWxdzs_O5FuCU1NX-Glz_a7mCbVQCy6oBNcUdDuBhkpKgyOMOTes-QPsGlfepGKnYJCj71pbQqHXMAZBSKtEQGkKa6ERzbpwwj5hWrEwrwnQjNl_pFijnNXm8rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J25pDMrCgtG6e2Szx0a1yBCNuWIh__Wp4JBd1OCTlTY4fSkjDRYWo4RoseuBSVtKNBHhZOqstXUEaOJ8N7V9v5G1YPA_NkzmF31cBty7L2hYnLIvJ3fKP3k5-GeU_EA9j7RCl8C5nT9cDdOM1NZv-_1TJMK_4QAQYcqlpvmTNud-UHCrT8cpHSg9UqvpD7pwewAwt1Xx0xheuGHnJVBQw11-DXc1C8f_29pJvX_TAVsS9pthTfa0rBX5MRqeN5cu_3t5vSU5XX9w8Nx8OTw5EXjubzSRnVJnG7Yq2nMKhakkksNJhDIUy2BSWTpfw9Tmwnc-5it8HAcOlUnSoVPtyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی: https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو: 1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4785" target="_blank">📅 21:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4784">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/4784" target="_blank">📅 18:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4783">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">برق رفت
🥀</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4783" target="_blank">📅 18:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4782">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">این پرامپت‌های ساخت بازی سه بعدی واقعا به درد نخورن(توی سنجش قدرت واقعی مدل) اما از طرفی اعتیاد آورن. هرچی میرسه زیر دستم پرامپت ویدئو آخری رو بهش میدم ببینم چیکار میکنه
😂</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/4782" target="_blank">📅 18:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4781">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی: https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو: 1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/4781" target="_blank">📅 18:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4780">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سلام رفقا
ما به رسم هر سال، نزدیک مدارس که می‌شه پول جمع می‌کنیم و واسه بچه‌های سیستان‌وبلوچستانی که بخاطر وضعیت بد مالی نمی‌تونن ادامه تحصیل کنن کیف‌کفش و لوازم مورد نیاز واسه یک‌سال تحصیلی رو می‌خریم و بهشون میدیم.</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/4780" target="_blank">📅 17:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4779">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">با پنج دلار ویزا کارت خریدم، ایشالا که کلاهبرداری نیست
😂
اگه خرید کردم و اوکی بود بهتون میگم. برای Claude که حقیقتا جرأت نمی‌کنم</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/4779" target="_blank">📅 08:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4778">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یه هارنس چندنفره برای اجرا کردن Agent‌ها. یعنی چند نفر می‌تونن همزمان روی یه تیم از Agent‌ها کار کنن — یه جور VS Code مولتی‌پلیر ولی برای اجرا و مدیریت agent
👍
🔗
https://github.com/yc-software/qm
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/4778" target="_blank">📅 01:17 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

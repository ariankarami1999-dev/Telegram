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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 10:20:45</div>
<hr>

<div class="tg-post" id="msg-4897">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/MatinSenPaii/4897" target="_blank">📅 01:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4896">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا
جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/MatinSenPaii/4896" target="_blank">📅 01:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">مهم
⚠️
WhiteVpn Desktop
دوستانی که میپرسند اگر ما کانفیگ های ساب خود whitedns را تست میگیریم و بهترین را پیدا میکنیم . چطور ذخیره کنیم که همیشه داشته باشیم . ؟
شما با این روشی که من توی ویدیو نشون میدم میتونید راحت این کارو بکنید. , و همیشه اون کانفیگ را دارید
یادتون باشه که توی subscription باید حتما manual را انتخاب کنید تا ببینید
🔥
@whitedns</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/MatinSenPaii/4895" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">Building_Applications_with_AI_Agents_Designing_and_Michael_Albada.pdf</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/MatinSenPaii/4894" target="_blank">📅 00:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4892">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شاید بپرسید پس چه کاری؟
حالا برنامه‌نویسی آره یا نه؟
باید بگم که نمی‌دونم حقیقتا. تخصصش رو ندارم واقعا که بتونم تحلیل کنم
و به نظرم باید ببینیم AI به کجا میرسه
اما یادگیری رو متوقف نکنید حداقل. به قول جادی، یه چیزی یاد بگیرید(هرچند جادی میگه ai، استخدام برنامه‌نویس‌های تازه کار رو replace نمیکنه که به شدت مخالفم در حال حاضر. به نظرم تا حد زیادی نیروی برنامه‌نویسی کم شده و فقط متخصص‌ها یا کسایی که واقعا علاقه دارن یا ایده‌های طلایی داشتن باقی موندن. حیطه‌ی برنامه‌نویسی هم مهمه)
اما خب حواستون به حرف‌های غیرمنطقی و امیدهای واهی هم باشه.
و سعی کنید خودتون تصمیم بگیرید. و توصیه می‌کنم حتما علاوه بر مهارت‌های نرم‌افزاری و پشت سیستمی، یکی دوتا مهارت فیزیکی بیرون از خونه هم یاد بگیرید
❤️
نه تنها وضعیت دنیا معلوم نیست، بلکه وضعیت ایران صد پله بدتر معلوم نیست</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/MatinSenPaii/4892" target="_blank">📅 23:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MRdJh7GAlWILj7cydzebow6mUTk8gND5QpmTc5IZuTB-QzTuJQpDrSEtqWj7iwCunqFgYFFZSmmW2YsnNsQZN1YhSLvxIJLBbKMMmGc0lv2OkbrxYGRMOwMsrU_bl5TxMJ2bgBkKwIfD5yfgDAmnxsnwfNVPZu2aMGe9nV55KRz-fcfBAXIxIf2fMTULq7aJXpgbVbOlYF1kvsuS245s3W-ffrFU5_wjCIlQvPAV6vj8cqgEMyZkJbaaRwT7kF00IR5qDyWEAPN55oYYes0ROiDItI5l1KCxVMTyy8UfAw_USCj25HaJm15V6LIA2sFPs7XcYqW22snm80e7gvbCnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">21 سال تجربه توی گرافیک دیزاین، UI/UX و Product Design دارم، الان هم که چند سالیه با AI سر و کله می‌زنم.
از زیر پله تا شرکت‌های اروپایی و امریکایی رزومه دارم.
سن‌ام هم دور از این 35 نیست.
بدترین زمان برای ورود به UI/UX عه، قبل AI شانس زیادی نداشتید، الان که اصلا شانسی ندارید!
✍️
Diego JR</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/MatinSenPaii/4891" target="_blank">📅 23:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/biHbcGbqVE0hU7lXS23mHL6SFEOOG14-HWtCITQpz7RkW44xzcPZGHj5QsHrG9fip7PvEyRFwQY4Vsq3tr2kdXHLy8MMFE-EIXPdWYrlY_IbSlaW6Tqdxtdz3ZUQA3WRpMWP0Jh8wLXC3HMIY8JZNGrkNlShvNeRLY4OtsJRd4PoMyzrqvXti5dnqzX_OgHx8aQqkNgZRRECwZ2wraM6jX8fZSHyCLzKnczQ9QJihQVY8gixs_MYNjuGkFdJIiFPW99uLO3fG7nxE2eWuSwNU5GbACAI26AYbkIg8KbYjUgFNSoqHpMuEv6dDjcGY2pxg7jDBXFdjinsUwVGoJ5DPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز نشستم با Hermes و WinDirStats سیستم رو یه کم پاکسازی کردم</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/MatinSenPaii/4890" target="_blank">📅 20:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کاملا موافقم و به نظرم هیچکسی "عقب" نیست
با کلا یکی دو هفته می‌تونید به ایجنت‌های جدید و api هایی که هست و... مسلط بشید اصلا نیاز به تلاش خاصی نداره</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/4889" target="_blank">📅 17:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">به نظر من کسایی که هنوز نرفتن سمت هوش مصنوعی آنچنان ضرری نکردن، چون الان استاندارد خاصی نداریم هر شرکتی چهار تا Agent برای خودش راه انداخته و داره باهاش پروژه هاشو جلو می‌بره ابزار های هوش مصنوعی یه دو سه سال دیگه پخته می‌شن و شرکتا یه همگرایی به سمت یه استانداردی می‌کنن اون موقع دیگه یادگیری هوش مصنوعی اجباری می‌شه، ولی اگه هنوزم کسی نرفته باشه سمتش با یکی دو هفته شایدم کمتر بتونه تمام ابزار های ترند (نه استاندارد چون چیزی هنوز استاندارد نشده) رو یاد بگیره
عجیبی ماجرا اینجاست یهویی یه ابزاری چیزی میاد توی یه ماه 50 هزار تا ستاره گیتهاب می‌گیره بعدش فراموش می‌شه و یه چیز جدید تر می‌اد!
@Linuxor</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4888" target="_blank">📅 17:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4887">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نمی‌دونم واقعا یه سریا، کی می‌خوان بزرگ بشن
کی می‌خوان به بلوغ برسن</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/4887" target="_blank">📅 16:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4886">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">«الو بابا این پسره منو اذیت کرد بگو سایتشو بزنن فیلتر کنن.»
خیلی سایتای فیلم و سریال و انیمه و... همینه وضعیتشون.
تازه من دورادور در ارتباط بودم در جریان یه بخش کوچیکیش هستم فقط</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/4886" target="_blank">📅 16:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4885">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">با ابلاغ مصوبه جدید هیئت دولت، مسدودسازی و اعمال محدودیت برای پلتفرم‌های آنلاین از سوی دستگاه‌های اجرایی ممنوع شد. از این پس، تعلیق فعالیت سکوهای مجازی تنها با تأیید رئیس‌جمهور امکان‌پذیر است و مسئولانی که خارج از این چارچوب عمل کنند، ملزم به جبران خسارت‌های مالی وارده خواهند بود.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/4885" target="_blank">📅 16:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c92W6Kr_U-VLY-ZihB9r6uQ1wmUX-3RUq1tslCyd7nVQ2IBy30qBHX91oWTRspI88OfRzYiOvMvJ5iV1ir0Xxa-gdbaE3f4YGvEAE1oaT1FObo23_DIuz4-euf7cwHdc6D_L0IRtqCuQVAyr41m6rZiQdA7HCCoR2lLR9WB6nZytLm_pYPXvhS1LgcSTssn0AwJSC_OcpmdphGRF9b8cBcVLvLZi-2IPOClaijk4sn-aLFQM37RPshsuabrOuj2ZUWweRqSAHpUyFjd11yG9qj4WKW5DAYJLBGVca2wDKY3nswJv3ZdDMP7ml6crKiiiFeAqJPClbE_nQZEn6zg_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Free Movie هم بامزست. دو نفر می‌تونن با همدیگه، رایگان فیلم و سریال ببینن
https://freemovieir.github.io
هر فیلم و سریالی بخواید، لینک مستقیم دانلودش رو می‌زنید اینجا  و Room میسازید و می‌بینید.
در واقع استریم نمیشه. Time Code کنترل میشه و چیز باحالیه</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/4884" target="_blank">📅 16:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4883">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/MatinSenPaii/4883" target="_blank">📅 15:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/MatinSenPaii/4882" target="_blank">📅 14:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فلفل چت یک پیامرسان متن باز سلف هاست هست که روی سرورهای قوی تا ضعیف قابل اجراست قابلیت های هر پیام رسانی رو داره:  - چت های شخصی و ایجاد گروه ها - تنظیمات پیشرفته پنل کاربری - پنل ادمین با دسترسی و کنترل تمام قابلیت های اپ  نصبش ساده ست و با یک کامند انجام…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/4881" target="_blank">📅 13:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/4880" target="_blank">📅 13:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4879">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دو تا از دوستای خوبم امروز همراهم اومدن و اذیتشون کردم و کلی تجهیزات گرفتیم
🥰
🥰
به زودی خبرهای خوبی در راهه</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4879" target="_blank">📅 18:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/4878" target="_blank">📅 08:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4877">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/MatinSenPaii/4877" target="_blank">📅 08:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4876">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/MatinSenPaii/4876" target="_blank">📅 19:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4875">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4875" target="_blank">📅 18:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/exTrpSLmXdNV903COulIdVpZk7EUxcy_LGS5lsMQwGvTgc8ghkS3P_HRxCbee0M5zxBHimqussgameVjKfEQHNsOfZ7RY6AV7G9EvUezEzOOBbnJjLvO4XBd1ZLngrdV9wTglbDBHtFrTdXkka_oEykqjYijg5k1zeW81OJm8IqkRgs8B9wU7J_J0uKFmagoIkzSxw9JKhJ01XqbXfHD-Gl4Zr9F54fxwCylrmOx1TqZOScyAfuoWwvVveuoVCMP_DzOSW0j8zJ4c6Zrob_CkpM7fdN-kSE15oivJYolTyWhqWCKCOT9Dnh5NVuSTzIZYAK7GU4DMgah26fFVYU4EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاملا درسته این صحبت.
به محتوای ویدئو کاری ندارم، اما خندیدن به اینکه "آموزش «چگونه وایرال بشیم» خودش 60 تا دونه ویو خورده، هر هر" قطعا از کوته‌نظریه
و صحبت این دوستمون کاملا درسته.
اون شخص داره این ویدئو رو برای یه دسته‌ی بسیار کوچیکی درست می‌کنه، و کد تقلب نیست که بگی نگاه کن خودش نتونسته:)</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4874" target="_blank">📅 11:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نسخه‌ی جدید Grok-Build هم اومده که زیاد چیز خاصی اضافه نشده، همون بهش نپردازیم بهتره فعلا</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4873" target="_blank">📅 23:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4871" target="_blank">📅 23:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یه مدل‌های خفنی در راهن که باید وقت کنم بشینم راجبشون بنویسم</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4870" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">انقدر اخبار جدید از AI میاد زود زود که به قول یکی از بچه‌های توییتر نیاز به گزارشگر فوتبال داریم دیگه تولید محتوا کافی نیست</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4869" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4868">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yz3sqHSoTJG0UDvdlHwx8GAo6tvOfr9A-14ncGcQxr-LS-rRbwoU3Bvr55OwaRq0RdT6Ulm8vEGbzQx6kWJQFH9MQ2UputKEeSoWTSctZrlCPAfMBDjpaWKAEaC4QAV54XGvy2fIuN0H198FsPXTPNvduqRfOOVNi7eHvb0PpQk_M3XoLVMZs1P9qWZL8V1tT-4tvKeMJFYqes6B7mn_avj2pWL_riAGK29Thu7_b9HS5DUqxNR2kuGuxKMbNrO0OzTHp5WgZV0I25B8WeQ6ksLdJC1CKL93-4CjqzUHMSYK75ygyOJ2GMAXeBCxs6-SqzcaaDIabKwOTKGupHjzpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین اپلیکیشنی که برای نوشتن چیز میزایی که توی ذهنم میان استفاده کردم، TickTick هست. ساده، راحت، بین گوشی و سیستم هم سینک میشه می‌تونید توی گوشی به عنوان ویجت هم اد کنید. خیلی هم سبکه در عین مدرن بودن و چشم‌نواز بودن طراحیش، هیچ چیز غیرضروری‌ای نداره. پلن رایگانش هم از کافی، یه چیزی اونور تره</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4868" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4867">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مارک زاکرچیزبرگر هم muse coder داده که تستش میکنم. سرگیجه گرفتیم از بس بین ایجنتا چرخیدیم.
اما جدی مدل‌هاش قیمتشون عالیه اگه بنچمارکا درست باشن</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4867" target="_blank">📅 05:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4866">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/4866" target="_blank">📅 05:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4865">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=JuM_6m5WvoVGDtpf6znjdLYcptSPgkBbgUvysg_LIKeaBspEdNi56dIY1HNSWuZQd1Rp_ndNYvLzY7h-4cuk1QXfkNSpdOQY3eHbeomRAHF1cfB6lv1ljDHBzgggQ6ovxTke55SnCEXYWXGS5Bw8Mcg2b0PG6fEeE9MVWIpadhiO3s1bR4hJUFMqUtD0Lq6TonqhY0I0dLHDdADzg31I47jkdGnGJ1OVrQoLnbY9ySLu0Juj2mZvg3GUgkERUfakzPFzeWh8cW_8fxWA33h8Vr7xllXYnUzB6COsjf3pFCmDlm2qdpcBrLiOswppeGpRF1rQJJh0UNrZzN3byxPYnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=JuM_6m5WvoVGDtpf6znjdLYcptSPgkBbgUvysg_LIKeaBspEdNi56dIY1HNSWuZQd1Rp_ndNYvLzY7h-4cuk1QXfkNSpdOQY3eHbeomRAHF1cfB6lv1ljDHBzgggQ6ovxTke55SnCEXYWXGS5Bw8Mcg2b0PG6fEeE9MVWIpadhiO3s1bR4hJUFMqUtD0Lq6TonqhY0I0dLHDdADzg31I47jkdGnGJ1OVrQoLnbY9ySLu0Juj2mZvg3GUgkERUfakzPFzeWh8cW_8fxWA33h8Vr7xllXYnUzB6COsjf3pFCmDlm2qdpcBrLiOswppeGpRF1rQJJh0UNrZzN3byxPYnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش فیلترشکن رایگان و امن با استفاده از متد های MITM و Serverless
مشاهده در یوتیوب
https://youtu.be/VYfQePhgEUU</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4865" target="_blank">📅 01:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4864">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یکی از دوستام برای رفع لیمیت اوپن کد روی 9Router، حذف و نصبش می‌کنه و درست می‌شه.
به زودی واسش یه اسکریپت می‌نویسیم که این مشکل حل بشه</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4864" target="_blank">📅 19:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4863">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=tZ12AFd01TSh4z0TrShZSJahRekVWOjDGvQkI-xdsZvlOD6uI9rs468Dp_XRTX4G9_5WQAK_qseNpMP5hIUWx4N9A_p8ubdJ_pWb-kIklgPOOcCq_weqQV3HpqjgtNjw2OLsYoXWzw-Q9lqAXP-cRWKTAp_ggu8u_yNNRF_R-w075ph8y941XYR3a4UfiUuZvHImWdwT8XNhsRYrNZRCLQPHACA9GHk171VEGteUq5Oi0XSCwRO2I0AsdvRAknDpyHn81o1eSPAYUtBOFR5sXxAIutibGVhQI6vF8NMk9rmgI9K0gbOmyowalUYp3EGNB4I7KzKUuAI4gpwR5rh1lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=tZ12AFd01TSh4z0TrShZSJahRekVWOjDGvQkI-xdsZvlOD6uI9rs468Dp_XRTX4G9_5WQAK_qseNpMP5hIUWx4N9A_p8ubdJ_pWb-kIklgPOOcCq_weqQV3HpqjgtNjw2OLsYoXWzw-Q9lqAXP-cRWKTAp_ggu8u_yNNRF_R-w075ph8y941XYR3a4UfiUuZvHImWdwT8XNhsRYrNZRCLQPHACA9GHk171VEGteUq5Oi0XSCwRO2I0AsdvRAknDpyHn81o1eSPAYUtBOFR5sXxAIutibGVhQI6vF8NMk9rmgI9K0gbOmyowalUYp3EGNB4I7KzKUuAI4gpwR5rh1lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4863" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4862">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A8PE2DM3Zq-adENPjg9psMb-9OwlbNlP1jhSe_xKutLt2Acgg5NgUuMqOTc9it_oNe4eYKqW3nIREFsStistxdkpX27lqLOS9HLy_BRHBPKnB0O7YFD86JbRXQ5sixmkqWGRgqdaDGh_Hrn83y-T6lO2OAdGL2BUa4FWvA5A6zX6UzRqKo3fJq8diWwNeXHoRcBlbxFaJ5GH5G15xx14xwuu-PqSqvqMy5_JI5bZvQPiFPNuBuuOdCjfoBwsQvAeLp6uNmyXPd7v_RZuPiZtNquOI6YUWsryPvSCdawlLafs1_JjGGT9DPpkigse2CXKw7Qozvp4i7YxrdrJmfrijw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه جوری ما رو دعوت کرده به سان فرانسیسکو، انگار حالا ما میریم
😏
😏</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/4862" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4861">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">Matin SenPai
pinned «
خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید: https://t.me/Editor_MatinSenPai شرایط کامل توضیح داده شده
❤️
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4861" target="_blank">📅 21:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4860">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اگر وسط آپدیت کرش کرد، یک بار دیگه باید re-deploy کنید</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4860" target="_blank">📅 19:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4859">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4859" target="_blank">📅 19:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4858">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">«بعدش هم روشن شو»</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4858" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4856">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i9J9c44NNyFhYEbkJ5XnyPdPs0xwcjrNnN7doVL6oUKXorFVOxO-B8rQZeiRh7Wbz5kEiDrmjjpMunUHNe6w_WOrqLJc0LgMS7EQfaI2FaihsAZU7qSlKuGn0jUosSyWljU-8lTt1gU5OuBDrbMsgggTUjLzD9V1Ow3APwhzAJARlS8HOoAPMAEnG16vxqZSzN3EKqMYWK6_DYZw3tr0I4jOJFOY7pWZvy2foctXQfhH8LuWragLwxNVfJUrrBexDffTCBHcBh1EPEVrXoUTJk5H_7VAvx_sQJEbAqhZAmSAL1YY_VjcS788-5bThqMlWXXfkCCYWfiO7hOma1gyFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rUayzKiAwGzQWbMXsgDcIrccexxZ4M5W66rtlLHI-aVn-FfqYiuka4JOsEAnUIk_rlmOoX-zza0rLR6GWVnt-jdXlZwek2JHlWEyfy9n0gbCH8SmFjwogCtP390CzDP9Hhq6L8K5xmsLtu_VeUOcIuafHBeSbPgg_vKRtOILGTxrsBwa17MZhn7tDoAIAVAub_WeT2QTMx66RCd_SKUtyWXSXSK1o6NR8j3SmpFM2lgGzqmWvNwMYK8sq3xbyk9Kz_w6gnttQEoVBPdEat8t6p5YdR_NiX73suXTCHZ8pZdYQbXGSLgcVZXEigr13HmOgwP3-qSJRyMkV3GkhlIXsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">متین الان که هرمس اپدیت داده
چطوری ربات تلگرامیشو اپدیت کنیم رو railway؟</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4856" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4855">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4855" target="_blank">📅 18:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4854">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کانفیگای کلودفلر من هر 5-6 دقیقه، 1 دقیقه قطع می‌شن نمی‌دونم چرا</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4854" target="_blank">📅 17:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4853">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">راستی این ویس با میکروفون گوشی ضبط شده و با هوش مصنوعی رایگان Enhance شده و به زودی AI اش رو بهتون معرفی می‌کنم
🥰
https://t.me/Editor_MatinSenPai/3</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4853" target="_blank">📅 16:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4852">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید:
https://t.me/Editor_MatinSenPai
شرایط کامل توضیح داده شده
❤️</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4852" target="_blank">📅 16:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4851">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sV3A5G8wtSFlDkn5WEJPQ1ChlQajnMZ84wbRNZWhs4fNbbDJumOaWHqaILNlb76qsn72e9MfdjdFDMQgR9NcTpndCoX1-OjmBWpGYkRvvwmEAjvcgoZlAQBk6KLZoMQdIrsPcFdI7CduWMjBhuyO15m1OLDkXKOM6Vy_on_tLurLofFXzdkJqHkYLYfFJ52CJQDUBo_kOXjO6nZYoP8H9SUeTFE_ex1UmZF9O8hn7WOa6QUfYvFaKrZzdCeG6cSgpxFMZBfY54wz3MZgYmnMEW-pfhH0Ik_mZnrKANivjgC5_GZAu2kAT98LxOJJyG2n_0QDHbfzs4FKDyUxsGVmBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این اپ INCY که امیرپارسا بهم معرفی کرد خیلی خوبه
دم برادران روس گرم</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4851" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4850">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست  https://t.me/RasadAIOfficial و برای خودم هم جالبه کلا به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4850" target="_blank">📅 16:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4849">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست
https://t.me/RasadAIOfficial
و برای خودم هم جالبه کلا
به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4849" target="_blank">📅 16:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4846">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gBy5GY00zKSqkdubhe3NnfNiDthWtpB_3-hvaqXSvP0EKDeEL1B2zYmoVQuVe_ee0_hPbWvYkYXAVPiDMdXPp389_EPu_06Xvy1OctRUXbtU1gmgY84USLEe8T-9dn4d2fKorMW4wtuqayvxhKSF7gbIBa_6Q9980HXHURsri_10s_DaMnGsmP7KcWJpGABSw52YKIeQROZ6t3zVFN3my_HNy1yEQ8ES6egK_LPu5Qh6gnLdhreiozcjChyGxfFoGCAdi71xUFlunlwxdxIWI5Gp95q8ryFtk3B4xwZayLcesQDH5WeoWwxB0Py8h1ulRNrW6CU2kjxyjftafI7-ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PF8D_CW8sIJJibC2mllAXxeEhUAvOaCXCRESrgNS99D_9czMzp8IEUKAr_-69kfbUMaJEaOvM7pS4Z-WFeG6h44aSulHnSOTDSmT3fjYCpK6ZAm3b6IxxQbtvCZ-7ikgvXjR9JCESSfLjQ-cJ86MLLoLsXqR7sbcIzXDhN87J2UDYEqwKOMjC3kIxnBJZYf3u3xvJivcyd5tKykLA64Iotk-HcoXDxksgCpL2usPo0opKj_cdKI4Ooz2lP80h-ifVK4EONcnWO7JhQkBbdWC6IMBZS2ygClsrPTRFgTDsQsC15nWjhQQbJlRerg6IPCkBRnrEMYIGkqPCnERBwy0Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dC3dkwLgUifg1KP_OU1slJTjts20BZy2hs4bvfms0y5L83nkRQA1qaCc7qPMAHYij8DdCshj6Wv4VDn2v0Difl6e9Jzs2SbqpHaYvnppuUddpIfEeznCQ_33e37sbe4RHH3qF9NFy14H-4FBYJUB9N6iLPrmh3_2P8naiPepnffqdwVT0PnlWtIuWgYMDaPjp9q8suRcyOnm81rne-n3W8fowjPtW5sKUjgSdUOcUiWy6Nw-g3_kcn9xchz5NBQUz6OQPT1NpjpSu0q7qdMdZhpJp_C4kajTSVyY4rCI3XhBQ0zLjDMiysnpAhCEdul6XZAHrmZF8lgTT47pnIT_EQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به نظرم برای رفع دائمی مشکل هرمس با Antigravity یا مدلهای دیگه، از اونجایی که گوگل داره به پرامپت اولیه سرک می‌کشه، بهتره ما هم هوشمندانه عمل کنیم.
وقتی متن خاص اول رو تشخیص داده، متن خاص دوم رو هم تشخیص میده اگه هممون همون یه کار رو انجام بدیم.
پس چیکار کردم؟
این پرامپت رو نوشتم و بهش دادم:
توی
soul.md
هسته‌ات، برو و تمام چیزی که نوشته شده رو به یه لحن دیگه متفاوت باز نویسی کن. محتوا همون باشه، اما کلمات و چینششون تغییر کنه
و بوم! جمنای دوباره فعال شد روی آنتی گرویتی</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4846" target="_blank">📅 08:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4845">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انگار نتیجه‌ی کارآگاه بازیا درست بود این هم راه حل آنتی گرویتی روی هرمس، با تشکر از سهیل و Moh جان: https://x.com/i/status/2084572159016382738</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4845" target="_blank">📅 08:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4844">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KxCLfmCClxlIXY7LjVkMGN_dNeAdsUzXQUnr3RKoBYDQOhDJU6tuvwcX3GhiOzoBa84gQmNMMAXKK8pCPqQIMy1eSQd0iImZkAh3nxQMl4s0AiSF0mGUBEcKkLK6nmuVOxKz6sjeIpO-Ss2c93h-xAXjnMmACvkXRqPD6-zRPQ_DlceQioAdGHsC1dWzde60CLfuPIFIJ_8mr8eh2Pa7AZcifBJdAdBKz0OLfFecpYDV1ruj6DheO-JiUw5FY90OwO27wkChrVmn7K25p0M4WtrhoiKYku58e3zbssJ4L1SFIuOPJsLBw495_OArXj_OmbGPpkP2_zhZC_VqxKPMMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم مسئله از خود پرامپت سیستمی هرمسه چون درجا ارور نمیده قشنگ ۱۰ ثانیه طول میکشه. میره فکر می‌کنه و برمیگرده</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4844" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4843">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QuOs7aFTgsuHp_Wpc5zzGzKZmnD3IbtxP2wIOq9Rqbc3bENS7HHRTaTY1IJP5KhVq3GvMbPrFltwVPOJ4Xte2K2owd42BkLhrtiLyN1xSC33atACM5J3GkmhlVMX9De1al5CIq9wYsee8tAkbXZl8DEWUJx9I2rn9LaE9pki6_r6yZ4HswMUXoxkXfpPh40owf5qZm4ajS6Sq4EVObGVmw2axStxk7r3q8AzLOEilFR1nBW1LNLF4TFq9NJvdFEV20kDlmkvmdRkOFujm1wRd4vlknLmVmPQZv6sce2SzMo6WibcMq3mYDisxC98jTWmc1zGkNJN5S7TivxEkBU8Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلا درخواست‌هایی که "Hermes" توش باشه رو رد میکنه</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4843" target="_blank">📅 07:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4842">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router جالبه که روی هرمس هست فقط جای دیگه ازش استفاده میکنم مشکلی نداره در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4842" target="_blank">📅 07:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4841">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y3Y8gg-dHqrSmmo9NW6eeN_L-dxNh5s4vKEodwxCZsz48eaQK6MmdOCrGz44EtbQdqo9CQWnXekGEZu3Kls-QDtrP99usFFnDsO2Nynmdhmc-2sax7Zpb7hj8jQ2xE90WwLimYuPypKEcKypsPfIANEkGqU0aoWKYUPOTbt-9wHZ6VksmPHYrLIMNh_ppQwMpvX_qc9LKD0fUkDB756a5yJE2c4r3OZhfjzRTj-pTY1uSgYIbJtFz6dqA8vztws8tE7sT40m8s118TYriBbs_KFJfDb7hEaaOR8KQWRgGkjXFEpuZxFP2HkEk_RWbaq2c6xF2mwU6_g_EAXte5GnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router
جالبه که روی هرمس هست فقط
جای دیگه ازش استفاده میکنم مشکلی نداره
در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4841" target="_blank">📅 03:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4840">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/scId3ly3TlzW9irG21imN7wDtisK9HQjA6C_3ZmbrRIVkQzSz8J25vCnp3Eg-9dn2wh1y52m7S3vaYrcwXDICFkzQL0wEJZDgIACSqCUZQ_xgI3BRZQcDAbEMqaujhAPohzObaAULCmI3YBtEf57FSpPTLGrTQUsauKGVrTORsQiI-GEoV-XCYrKDYsBkTReU9nuSz-OdunofjgdUvkW7DE_q85EoZ88PKtAy3QEibcg1sbdAcGuK026WoLfx-j8sDFhjbkNuoTewURzXeGy8_e4c0g908J8lZjnqgyQR8qcWPU1Qj3t7_3cb0DyXR-81pcmMqs9A_YADuEsJzdhlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچها اگه از pomodorus استفاده میکنید</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4840" target="_blank">📅 00:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4839">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رفقا ما داشتیم خریدهامون رو به دانش‌آموزهای بی‌بضاعت سیستان‌وبلوچستانی تحویل میدادیم که یکی از همکارامون گفت یه خانواده‌ای هستن که چند ماهه وضعیت خیلی خطرناک و بدی دارن.
بهشون سر زدیم، دیدیم کولرشون چندماهه که سوخته و شبا موقع خواب میرن تو حیاط و پشت‌بام می‌خوابن، اواخر هم فهمیدیم بخاطر گرمای زیاد، یخچالشون هم خراب شده. بیشتر پیگیری کردیم فهمیدیم خیلی وقته که وضعیتشون این‌شکلیه و کسی بهشون توجه نکرده.</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4839" target="_blank">📅 00:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4838">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">به زودی قراره یه چالش(چالش هم نه) ادیت بذارم، و ادیتور بگیرم
خوشحال میشم که اگر دوست داشتید، داخلش شرکت کنید
اطلاعات لازم رو می‌ذارم تا فردا</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4838" target="_blank">📅 00:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4836">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WYIWQe72JkFXGm7z1w63LJTtxQPoAYj-Oje0c84qA7kUxfzVtzLhF1ueZYMK1ywPVWU4_u9OjLQN0jYY8ZxGHSA3UDpHcY2DVh_AThvCjysMdigKIAZRuPujexnDbNi9xXC7NB4KIVrp-sh4BA18svGDJgSV9POsn41t1TiEr-t5uk_lBZ6xK5g_4HUzMbhd4aSdVq-FNROYABzaXqc3PG1UlI30xrYbDI4ul2im4Az41rLjK5FrWcYEzP9zbk14p3tQWMyUjbFaCW5vzljPM_6pXKZ_rYnoB7Rn_P-k0fs26BAxelZ0U0LB3SaC2fg0K_7bxFNJ3_py5UUF6U2fxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از چیزایی که راجب کامیونیتی فارسی باحاله و دوست دارم، اینه که زیاد توی کامنت‌ها با هم در ارتباطیم. کامیونیتی خارجی، این شکلیه که ویدئوی تکنیکال می‌ذارن، 60 کا ویو میخوره اما کلا 25 تا کامنت میگیره. یوتوبره اون 25 تا کامنت رو حتی لایک هم نمیکنه. اما کامیونیتی…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4836" target="_blank">📅 21:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4835">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AAPFyEmGtfgzMRN4lgCFx0xdpTRFjOi5btHifliWMdE_zQ62jgzBmHlPEQJMSb4qoTA69rhl6u9eEqEJJblj3hfXPIy_oNQfxS8PzbikBcKbxbJbL8usLyIovYsDMJMJnMXXE0vtBds2VgDMPmLX4Iajx9PKXU4f_SfUN0eJSUcbaiW6PIWlmLi1OUlAM0Z_yL-oAPF_jQgInzR6Wy5OmADUCng99c6BHUCocW_D2NT4pt9_W0lq6kkLKF6h1eGnCmW5Z-dvrPGKTSGAmhNsG2H4qzbi0bSbaXmz82q6M8V-6YW7l-1YCqFF-RO76vJE384nyPlISDPS2YzrIRCZ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایگزین متن باز Fonto، رایگان، تحت وب
دیگه برای استوریاتون پول اشتراک ندید
😁
و اگر دوست داشتید، از بالا(علامت قلب) به سازنده دونیت کنید تا لایسنس تجاری بخره و فونت‌های خفن‌تر واستون بذاره.
لینک پروژه:
https://github.com/FontWoW/FontWoW.github.io
لینک سایت:
https://fontwow.github.io</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/MatinSenPaii/4835" target="_blank">📅 20:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4834">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">و به هیچ وجه، به هیچ وجه روی کانفیگ VPS نذارید.
فقط روی ورکر و کانفیگای رایگان
چون به سرعت از طرف دیتاسنتر ابیوز می‌خورید</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4834" target="_blank">📅 19:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4832">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jh3Ig-LJ4PQTopdcccPi4jzmaRo2NwI1AmL-px_DEAtVQAJTMtwlb2eET8A7D0dRcu1QOzcrLefs9762BMxkhniaVq9fChW0GPvH28fEdFS2R8NfjJc6ZQUr2tjD2Qw2YHYMQaBYyVsIFtJhl3vy0l8rI2wNshdmJaJ7O70XbhSX-EjZTpDvwkeDm5FuN6_65UT9pRMu1-TOKeNaviRiThvugKaBtpKzfi3UlH0jNt1x5OIpk686O3BzrFk6-Bub24OvfzNomeLCMSSDLRxqkX5FJGCD-vlLGTrb8Q7k1Bjl-P8gIasCjtwzj3gnwYjRPRuH1V2uZgZsovlADXX-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l9MH1Q7clc4DPsHeCV3_NTq02X_miI7iu59PFS0KiWYiYaD-1ypSusNgXUCNnRRL4d3w2Ke8-zos2hntlBR94ThCndDkS2wVeGPbHG0jaFxfZBQFsYJPTs2Y8GcgGszwxrAQvTuxXvnwx4k75hes7hRPCyVGAApTYdP3YoB5gLKC5Mh4JYIsywc5iZ9dkdbwD_aUEEQQQP0d4JXmBxMmiUywKhAVmo_HoMKO1Mr8L8iDduoD-ot20bedgHxtNaXjsSoU_y-28L7m9sajQBxMvtI8shqOYgY1GSwGpblAfNIT8aX59D0J2u0QjoVpafMowcAp48H4ixbIpohiMr7adw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4832" target="_blank">📅 19:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4831">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/glyP4sqsDvYAHBlu_Gw8UE5ul7ieFcC5ehm306CKZAIn0aZb2BdI77MMXvLlGJpGb0mhYe2QXptEnKCx5QOyXh63-JF4z8hDim41a5Xj3JmOFqc5mZ0HhAfzJ7-k-eT-UE8-8nY0EncrtLbsQm1dJ24Hie0pxHyM6HGz5eDtKc1rWiXa_F-n_p3cTvuYdSdBr_pLxBLnqA5PfXeP6bOl2SezGY_mXwG2AZe-aRY4LgOc6i6l-oEZC2RhYTmku84EF-IoQFSP2nGZuVzbP6u4HLDPAAXdozAcLGIYJ-FE9XR6s_4eahyLAoj8xEk2Juucwm4-GS8KfSe8AVpaNwjKsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید: https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4831" target="_blank">📅 18:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4830">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید:
https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4830" target="_blank">📅 18:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4829">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خیلیا ایمیل دادن پرسیدن با چه شرکتی کار کنیم
ببینید شرکت‌های ایرانی همشون یه افتضاحی به بار آوردن. یا چنل پروندن یا..
من هم شرکتی که واقعا کارش درست باشه نمیشناسم. ولی خب متأسفانه وقتی مجبور باشیم، چه میشه کرد
الان خدا رو شکر دوستم واسم نقد میکنه از خارج از کشور و میفرسته و دمش گرم</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4829" target="_blank">📅 18:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4827">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UrkqHlgY0XrWQ7JrMpM1HPV4mYyN0jFzds48u4sYJR97qxg3v4tY4oXdX8SqihUmeg9UZVZFz0cEMxz8COXO_73rWddvR66PGX213EUasenc6MwZSTN1iMFou-4lc09iVk9ydbQODuU1suPF1andcUs_yjutQYulyAEm2eC6jmd-XonCLnw8NSmjFC6BWKbYcYYcZtYEEBDcpBXKGDBRUaLasm9wts_HeHV3l3FXWzVoxK7wbhwjBaQ8cN6RDMemvhPFkZKZ0AIlzpFoUMkWJex-UeWVrTVaXY4HRsDw2rnm-ksLIinKNAShB9dSt0oidYuV9oY0Lzq9DLhNisnVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cJ7W5rmrSXz8rB4Kly-cezgd7_xNXWDY0iQsEsUI8BV3FgYbcUB4ICIRHNL1GiN9uqlM4uTQkISI875QtYVvL9LtNuBYkoVwaKLMRB-_mPVrTCg2r8SZoyyyAwCmDhVguZBWT-wwVN7WPxae9rMOIRO5xhoOyg7U83RPzBeOHWuQi7IMxUYcv2xnooEcUEic5lP_v61rso7lKCn2uiR2X82IrdvQk2UgfIaJjyVTXPjXO5lh_0D8EHu1U8Zh8eulTjx0iQJgkCdlPRkb3Qz_--t8qHxJmkqX5bAGRV2dA1Pjh-E3dQK17Nd0KiuPja1-sLlunWmpcO7d1AHu4A_Tcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادش به خیر. زمانی که من یه میلیون تومن هم برام نجات دهنده بود، یوبر این شکلی جوابمو داد و هنوز هم اون سه تومن مال 7 ماه پیش اونجاست:)
تازه اونم با قانونی که یهویی گذاشتن.
همون روز ادسنسم رو قطع کردم و کلا حسابشونو از اکانتم حذف کردم.
هیچوقت با همچین شرکت‌هایی کار نکنید</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4827" target="_blank">📅 16:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4826">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4826" target="_blank">📅 15:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4825">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4825" target="_blank">📅 15:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4824">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VtI3ZQdryplXKRXBLUhScNEOPrvSsoLyZqePdkb8oT3byQzkZsnJdZfo56el3T1fRz6L2TwE_uODxg76rBY_pD_kfuJcKPuo7B7oiP3Rmz0-cZAvDhpSTLXCVSUiXmHUuC5kiMFqBbSB-dxLosC9V2QSgoYM9B16tauNAyk7-g4Keb90FCk0nNtw_Z3-pA2neyxMvfMPBHXLEfGflY04bbxJRQydc9uEaLHbsHFjlQhynWKwv9nu2FjH8LPYMVT-F220itptxgjVSSfN2aaBVJL9f10A9Rx0ofo_L3j_PD6E-Ry7aCzAPg0DeQriW9bEzD2zCEBjCYEkEZHHVgjHdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقااا من رندوم برداشتم از گوگل
برای این ویدئو
اصلا هیچی از F1 نمیدونم
😂
😂</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4824" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4823">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=RQwuloGlC94LLGSPwpT8YHcyNBC21Wsxo04hsMLIQBSoinnJJxYZy-sprSQlTbZLsI4LKKSSQOgvYHu7hgHFKMd7OBKKAJXPGLN60UFZMj7V3JMoWK7LGG1JgSYY8yS_TUUFriJg8bLOBI5EkJ500Dy6ZfeviLMxe1TH7rNTEOhtWTis_RMDaj0cAMF8Jsvu1e8-Q6vPoZxOMRgJOCWKdqjmWScIYkGs1d24_3NQpGPuumjCl-sZycfS2V2NGMfKxCflGhMfqsQkMTmr__jXE9H9GGX9iPVElqVBL_t1F6mhvwW4ntCT7lnePSFJa_zn5EDCJswhZvcv_V__-j0vVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=RQwuloGlC94LLGSPwpT8YHcyNBC21Wsxo04hsMLIQBSoinnJJxYZy-sprSQlTbZLsI4LKKSSQOgvYHu7hgHFKMd7OBKKAJXPGLN60UFZMj7V3JMoWK7LGG1JgSYY8yS_TUUFriJg8bLOBI5EkJ500Dy6ZfeviLMxe1TH7rNTEOhtWTis_RMDaj0cAMF8Jsvu1e8-Q6vPoZxOMRgJOCWKdqjmWScIYkGs1d24_3NQpGPuumjCl-sZycfS2V2NGMfKxCflGhMfqsQkMTmr__jXE9H9GGX9iPVElqVBL_t1F6mhvwW4ntCT7lnePSFJa_zn5EDCJswhZvcv_V__-j0vVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/4823" target="_blank">📅 08:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4822">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PCHNMlinw7k_7aJrPnsOSNf0DUqaTs7TpYj_1xDIBnECGz2bNywo8H9ysIv8sRwBTw6MJbOtQBvXdfKWKKB3v1sbz7152aD2Fe7KBv6W38zgnlETKZot9fRi7c7B6t5C0w9BdEEFBW79CqwWfJ1yp-wVmhwIJhexCbu6NXiZTfTiKof_AtsPPl1cTA5H38T9N14rOVtcsyCytKNElynZppOKzg5Ldq6GphJzH5fejj5r4g3kIy_SnlQRUcfpLD2Wgxl39tYb3hGIXUBhvAJ4lCcuvGhExmmtEJ5yHZBLqVkZ1z0ZmqckqHlzgzyHDd_OHxGcl0e6VKgJenAR03oPAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4822" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4821">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JqiuI3mhaZmKc77dz0bUNKZ1iEqth6jx50TY3zQ64Z81thkmADVI6UnPuth2-Gf0u6d-1AHaiZVo98j8x20Ub-wlSLBwKibH-Ea6lgtWKF7WuALkjiALJ40Ii-Y_h4mBiDW2NcbmpUOdFzUd9x7Ffdl_IP-RiO050QBpKgjizN4IR8LKKGUlVKx6BjRd1wcDq1qjzMJJuA7c9cBFYxoTvMrTXk9WaJ6mjZoTVDwkBTe8MnAg9kx3rpvPCjWpKdNorHpm-cEG1sc2ver7q0Wi6UjWuUPnYsBQ5WaKIJ3ektcrQK23zgVVC92C9UjQGMtGRuMEJgXqNEH_0vwSrjSQGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4821" target="_blank">📅 02:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4820">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hallelujah</div>
  <div class="tg-doc-extra">Leonard Cohen</div>
</div>
<a href="https://t.me/MatinSenPaii/4820" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">00:21</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4820" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4819">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه. همینطور قابلیت ip fronting هم داره و سرعتش…</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4819" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4818">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⛏
۲ نکته برای بهبود سرعت WhiteVPN
۱. بعد از اتصال روی دکم
ه اتصال مجدد
کلیک کنید تا به سرور جدید وصل بشید.
۲. همچنین میتونید به صورت دستی تمام سرور هارو پینگ بگیرید و به بهترین سور به انتخاب خودتون وصل بشید.
آموزش تصویری</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4818" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4813">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.6 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4813" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4813" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4812">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4812" target="_blank">📅 11:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4811">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k3yoywtlHD2XlaZfKOhUemec4DT-b3NKnU7rbkJZqY9G-xqvG8awgHM253qWpACaUQZYPePL8xNyO6gsYSkeypgZe3_FZZAieJ3HSpCmaeK2vKcgTYaV31vSaL_Ek-1gozf3VxOwj3z9jSHXrkRqgUdnYfVvvseZLHkVTL1KSRyuQuzqbIA9t0xnNj8umc2vz7VMf5gbrPpYJfdD0YOnOG_8G0eF_if9isBw570aa5WibEGxdUs-wYuaX5GnJlhkXSRrlPuPgRCdc1Y7kABYvq_uem-2Kax3pcIyDxAlnLUGN0rqZDFFFNhKx8wp2vjYlkV662tMdTdLw8uNRxZ-Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه پرومو رایگانش تموم شد:)</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4811" target="_blank">📅 10:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4810">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NRiRYAu_YYYK50En4HKycvsqr43BnRhDlS-vjA_4ThCRyGd5dJW35TJ2EmTEanQd_Joiii6f5EreaDuL89q3wdc1DBnF70WDXH17RAHLmdkDifWvoiwEoFuQbUI1dhz-ftCowgCaBZDbs3IwAyudNBylEbNgO_7UGWl3KCRLCTzsChaiox52XfBhHs_8MWfBBbdpHVsMIR7X4_M1myqavVd2OjalUlarYssogoBFkAdEsvr4xTNMTMKC6lIB9PYVUZPpIrsoxIMD6VvpuvjxKPFWTX8LF7mWokcoBB9JZRdQSOaersHLvf2hmjjjIupoJnML9oe1tP5004oapWiC2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان بیشتر مدل‌های دنیا وارد «منطقه کشتار DeepSeek» شدن.
یعنی مدل‌هایی که توانایی‌شون کمتره و قیمت‌شون بالاست، دیگه رقابت سختی دارن و ممکنه کم‌کم کنار برن.
✍️
Ali</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4810" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4809">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4809" target="_blank">📅 06:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4808">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سرعت آپلودش هم عالیه.
قابلیت‌هایی توش پیاده‌سازی شده که از همیشه استیبل‌تر بشه</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4808" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4806">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e-yovgbrDiJuWcKdUMfJ4YZa8O4M0AaFRM803gHW_qmpLWg-CcptgI5l9DQ5AUah-xqQRgzyYEdSjz5oRTWXRvWTdPrUOl3608eUvSRSHNAZUw9ou-wpJmaSNJOM3-z18bfIg51vW8mAHUsfCIACC89TUEeKNxl5ZTxGYW51T7tdLG4UZYpBAfvzbjXRwpOp9cuhQyKFVtemLpJvVw10B2Qloe3BRU-ylZKy9pXDWlMhhiHmjSrw6YSFKd2jlvKpSknm-bQr0VA3Ja_ONtxy-NZlrp0iYmcqAh5o9EytnsnfVY8GS0n-Xi23ufy0Lqbr8IQi9bOEqZ483SCas48tLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T-rxWgu7LJrvqCDPZ4_JDRkq8jkRt4O6YgVPe9BddOTeT4FCwGwOlnxYGA9x_tcg1mMmDiAVWglHZKo19jE209dpeyepPYPH-XX8-3hPajD4SaYyPAYOgeiCa5M_cg7JtDelSw2Xd_m7FieAalMhxSWmkAnb245tXBsbTnNu1utJdKL-pJRAB4mJ4VxLwLydwBnDxMxZ35KQaYhnB0O0kT5eydIJxFiixCkgmc9HYJw5kbbbkDA4L9P9UWmMhqCuTdL_zbUndp2hd867aS8k3lIu4OGc5_Ezb-ScU2ajnmlA9SbIIb6qna_VCvQ_dyQ0BvupCzrqrs0NxowggaMIiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون
اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه.
همینطور قابلیت ip fronting هم داره
و سرعتش عالیه(حداکثر سرعتی که اینترنتم میده)
دم بچه‌های WhiteDNS گرم واقعا
❤️
🔥</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4806" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4805">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دقیقا این اتفاق برای منم افتاده بود و سه ساعت داشتم میگشتم ببینم کجا پروکسی روشنه که بدون وی‌پی‌ان داره آلمان نشون میده
🫩
🫩
روانیمون کردن</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4805" target="_blank">📅 05:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4804">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Qwen-3.8-preview.html</div>
  <div class="tg-doc-extra">44.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایلی که الان با Qwen رایگان ساختم</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4804" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4803">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Kimi-K3.html</div>
  <div class="tg-doc-extra">41.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4803" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایل 4 میلیونی‌ای که توی ویدئو ساختم</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4803" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4802">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4802" target="_blank">📅 04:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4800">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tL-f-TsGzqkhjyje8yD5J9KlyfL4LGbXnw0TdakuAxrb-oOt47Vcv83grZ8utvGEegkvzcf3401Ak52EhTJsDWwwHYzeViYvPy3orCl0BPFLJOFD0VvelN8H1jzxEev2yWruS5Y9Q2UGMiRREfjVIiy4T6lxgo0qtlx0zpJaueUAZVNC_VNGKi8I8o6YnCXnbVRwt_3YMbY29X7I71HyatrAs85sTpeT7Oe4SA_o6JYBeo8i3Vp20zGsnj_ZStpajLip8zt26j2OADuDt5DczP4sq9q0QXHpw_SzMfnPDcouzDkfj2opQWD5bgoY8rW9tIO8wGVvu3fae_aWkcvYIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lWCIGgnewWbbp4rvWxmBj43BZfT_ZFsxiVohIsOrs6a8IT-S-OhMbg0HlKBcpjvJOyrj_Jj78YhS6BqsFxay0Wq0AtexYJTOPtyjDe_woEbXLWkdYUokFnFBco2CUd70af7wVgwZiLeuQbQMV7qnrX88v_pcqhzYEPFuIlwXStcsyPeP506S1-GzfLdc2uK1dMuotoHzRAIn2ZHO6NqeA6QaTpQnTaTyUfjFow-ZvDqrYQxZ35YFAp_FC0nzsl-eVQF-Mrl00T19rcqKAOGKw_LzDmRn3ylcRshFif32PplPTk88sq_hmO1Ow6BS27091duw4zAumiiWLpC36UUfKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4800" target="_blank">📅 04:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4799">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RYc9E6YvQ01GKirzohvd6NOfYNv4Ynh-t1OubNyynopYdG-qq5-57kxft4ZsN4IMFpFoLKYB2CWI4wC0a3dLj1rf0yj4favTtopj8MPWugYUszE8Fm8ipxqsoe4tZPT1IaFGHA65ttSuGFVq3Uj6GKI4DLNk0UmVeURarl4HnvV67WM474nuu8eihqbM-z3xBft5eQ92vwwD130AP60U5LspBOHHYmvbFki7sJUNRhl-FprXpMshM3veeBvhLKapnUZLMSvaLPEy1wG2jsORmf03UUZ8O-BSgpyBPvF-MwQPfKA3j2E3M6G7OGXcgX0T4cooylLSsdKhPscdje-HbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان توی
infron.ai
میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.
ممنون از confesious عزیز بابت معرفی.
فعلا دارم باهاش کار میکنم ببینم چه شکلیه
تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4799" target="_blank">📅 03:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4798">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4798" target="_blank">📅 02:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4797">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت
تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4797" target="_blank">📅 01:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4796">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-poll">
<h4>📊 از گوشه کنار زیاد میشنوم اینترنت دچار اختلال شده. مال شما چطوره؟</h4>
<ul>
<li>✓ به زور به تلگرام وصلم⚠️</li>
<li>✓ اینترنتم کند تر شده🔴</li>
<li>✓ فرقی نکرده✅</li>
<li>✓ ایران نیستم👌دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4796" target="_blank">📅 01:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4795">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خدا رو شکر توی قطعی نت دستاوردهای بزرگی داشتیم و اپراتورها از وی‌پی‌ان فروش‌ها ضریب دادن رو یاد گرفتن
😑</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4795" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4794">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SIFBylrEpULj9eeJqPXAU-envLHV5MoEHJTxZGT4bCS5qzVGGHYQuVJ-4XQ3FYgolhuX0kr5DdVQJpQSCK-0EVrQ4sIxF95NP9PaqIzhgn8SojXZGMboeBPH4DPpwjipWIFhHbiYkQ9igkd3gUR77gklQfSE4AUi3n0RPK5vkys3seH2QINGZAGsBHJU2kdIKHMYCihThDXxkJcE6sd1ylumm7XZT2hA1RCLSemYsQTI3KNFMmy_AKnu1LLwSSX7q2UBSu-FQh1KfnOiZex-Q4kHWmLaoeq-xamiMW15s2TYOmWDZVqsffo3qw6VqQ-qqQtSCB2dpjZy9_cyZoLtdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4794" target="_blank">📅 00:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4793">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4793" target="_blank">📅 00:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4792">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhsNTxMLq7eDm62ataFD7aK3wZ9R4W7S9CgczUf8Cb3r-mUfzCq4G5iWgbILR7U6dYYpyh6Y66WPhTVMhUBYnB5t4KKj-XYNxybIZXq-Leyk6eOWuPawNKVS9ru-kSpClLTy5N5caC1Cue-wiQmqTNDeZes9Wy1DVUkRgn5n63F4FQ2MsyIBXuojb_FCDKqvm2grgQqkkmaKoQR2FmFckV9ZUITB2Jkf-be-V96Eae1xZan1h_-DRK5VYeNOder52lNX60aF-xex8vP6f4tbPXjSY7GKP57gT9A3cVsw-1mxzYyiK6NiWeBo7afC6tKK1vvS6dDnKZ5CsgAbbjaUsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4792" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4791">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">به نظرم یه تماس بگیریم باهاشون</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4791" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4790">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج 205.252.xxx.xxx داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4790" target="_blank">📅 00:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4788">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UAxtNmEW8fxI8gDuI-egqf3cH42JvUyrDxqtS5ec3128xNyPVt-zfZ4ber_bCNSP_icR7ZKYyHGWQHsLKUnxKrGpfIvvz8lMuVUgWYaxBjiM3Fk0dDUXkSAtQEx2KZ4i3tw-0xyV-NyNQrpeIe5YtETzRTsUVJXRCzARbC5O6RSxCVmLCYDjBTkCo_-Cd7fx_gERlzaviSKHXzYWxyne2BCXA7saP0qJYEkUN9L0gzxlMxkwTw4lL-2rjRw0eY5Q8D1Pmd406v06L2CMfiGOxU_7i8EogiVfbcyCS7l1fqWYn4uWFoqtXuxl1yVSN0QeLQnAim21zsQiDx0UMvcIWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jx4vDWmO50OyxgIL9Ef5PCM2C9w2_TCDgcKMHRY_3U8v2CYhZEKX2tUlzXQVs6fCbq-dIL5ZprYUioh2OyDW-VRrpGxdYYko4nmrNFBcenWiEh5GFU8TBhcn2WAzTalmNMMp-JoWAZ9_EWPkD3BFXucw7tnnSXY_UterCVe9_mudtDRGRWGeZq5zXzb2-OmMtMCQt4aB7mtqSY1z9JZsokeC-vbci5Fj3eugE_HeVHLKTZ-ZD-yF51cumpdklh5BaGIX4cwioLkO8F7yLvICgIa6anyO3lbYMOGqLojMZWs8Nwwj4VhP25Vfep38qo88gAZ4CG8yeDYMJt6sKNMzAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج
205.252.xxx.xxx
داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل قبل محدوده 80 90 بود الان 140 160 ، درنهایت این وضعیت nat کردن اینترنت در ایران داره به یک روال عادی تبدیل میشه که جای تاسف دارد</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4788" target="_blank">📅 00:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4787">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o5Bi8OZO3sJwf6ZSKXtSzQishEjlDrJ8BYzxEUSMu6bRGEUOliGbLr5TaLmKmeQOPYtIfR4ubJ4HgAPD37cMzwxjfMIpokEiD5-i_UXZMElQHj7ILeyWvz3qBpNaBDx-92sgBiUVXjVlbroQDo6JKFM7XJuWRKmLJq2OsSs8tYj2NBAeJPhZbepEAubkLI61EcVS2VuOGZWKzSqTr_UVWDlvZBkMhTXa5i6XoWKDWAJKteC0FVEsmJ_vEzlPPnGFCgPDilv33gf0Mg2N_vjQP21EulDb7AeqCH6fyw20cgZ4RWebUB91qbcQFmpNJex0VMimA0OTZrZcOuY3RUz-eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فریم‌ورک Science One گوگل
💡
گوگل یه فریم‌ورک تحقیقاتی خودمختار و «قابل‌تأیید» معرفی کرده با Chain-of-Evidence — یعنی مدل فقط نتیجه رو نمی‌گه، بلکه زنجیره‌ی شواهد رو هم ارائه می‌ده تا کارش قابل راستی‌آزمایی باشه. قدم خوبی به سمت تحقیق و توسعه "کم‌خطا‌تر" با AI
🔗
https://research.google/blog/science-one-framework-a-verifiable-autonomous-research-framework-via-chain-of-evidence/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4787" target="_blank">📅 22:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4785">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4785" target="_blank">📅 21:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4784">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/4784" target="_blank">📅 18:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4783">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">برق رفت
🥀</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4783" target="_blank">📅 18:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4782">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">این پرامپت‌های ساخت بازی سه بعدی واقعا به درد نخورن(توی سنجش قدرت واقعی مدل) اما از طرفی اعتیاد آورن. هرچی میرسه زیر دستم پرامپت ویدئو آخری رو بهش میدم ببینم چیکار میکنه
😂</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4782" target="_blank">📅 18:04 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

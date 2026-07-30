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
<img src="https://cdn1.telesco.pe/file/m3N26jRdNK7oYAJdpZfdVpPR0GC9giGnJVidlMLnfeLzgN0gR4Pfy6fsFqP0BFVH-EUZngp34CMa6KFL4MVN9CEGGHrsW9AsHtL1AkhGJzJ2PIQFGOoiXvkO4v7a2SjO1BPEAM7flYkga2zTNveCmDcZzJtKkigoJGDiYWpQ4hz6x0j0Exd4yix1iHp5TDftYK8Bsb0e4fSnkZBnnP0nf_ExRdFeMNliiGXB-FPGYVV49MbEAyW3w0qylwFv8KBZrlEPqgrGOYAG7TeJ1Anb1yWUO3fKuFFlMtC6HhBnorQQOQX5QnWMfyaf7f71K9vsz7hA2WorL4GlXgR_GggP-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97.6K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 10:58:31</div>
<hr>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته توسعه زیرساخت‌های ارتباطی کشور حتی در شرایط جنگ تحمیلی سوم متوقف نشد!
انگار نه انگار ۸۸ روز اینترنت کل کشور رو بصورت سراسری قطع کرده بودن و بعد از مثلا وصل شدنش، اختلال‌ها در ملانت ادامه داره ...
برای راهپیمایی اربعین هم در ۱۰۰ نقطه اینترنت رایگان درنظر گرفتن و پولشم که با افزایش ضریب و هزینه‌ها، از جیب مردم پرداخت میشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EUOdeT6TAoTmLhxdpsRUZFNfiqGIly71NDZwCD5huB7DJmtLwulrObIGuk5q-g1gtib3uO046kteBKx8JNoChNrqgyZZLWp3dgHgoIFMcjtx5wNqeEDbuB4MzLwfdUmwaUTQMhqvE7eUdtYrxp0o9xCEL-AWNzwHEE89g3kaoLX_UphCSfeaUjBghlzjeV9EymAYlpfaWuAya7bnJ3oUILu_-y-fNJWrVGmF4OvleQiDAe91I7Jf5E-80veIqhSmZB3DViGVtSiDYI1oN6wsTIwCGQ-PwJxxsnOcfk4TaNd7hp_71cbaxbuj9okkOF37ghINOj7ixFvpkzTR4G2kwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZDTu9iNe64_nCc5FJFhiQ_urdkUkXqE_U0QtB6PbPRMkXDt5Vzybk6AJGhoppkekW_oz09Od86lxiT9HMAz0Z0WZbf08FNkprwU8VTLGnZIuBC3I2mUBW9A_4FJr8SvsFFJaZj_x1s_5Etv7nBD6Git_7jHvcYUGXyrfm4QaB5Fm89tdyiQqm7lRe0kxOPJ7RD_fAMJmHMAVN9cj8a0aKOvptNp10iBi2rsa8PwPbrsmYrMpdSw4_kmOgiPV58D38VxiOcXKquHK3-LLzfX0PAZIslDR3r9SLYDtw0Joo9ngnF8YnXziRL3ouxd1n6f1ALQtn-DTxGdtYbEODVaWDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g8CcP5VAevXaxMyNdk5I4Nmk3SDItTp0jEvrKaissv7xmII8WnH83jjBQGkAfzu4gbHZ_bTdswh9QMLnOO6BLZRXEPAPVJx6pvGGiTtTwO0I_iEZBhfc7f8fX6wzYs6pSh-O7Q0cKZ23O5GstabNaI-MG448jA6aF9vLfVBFVR3xc5MFiafzXLvqsEzCjT5QOJqY_H-P2ExKQoochZkbeY-ancMiq-IT9xCGc7lxhGR3vWAUDXI80QnrbVH_YQdc7b3BjRTn-yl2FpFZLdLmY05zrA_bNn4_qowry2g-lFteXUfGhk9xui7DJf40BwPz-22nKQ-AwFT9S5Sg5JAarg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ AetherST Tunnel یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که با ترکیب هسته Aether و SOCKS5 مبتنی بر HEV، امکان اتصال از طریق پروتکل‌های MASQUE، WireGuard و Gool رو فراهم میکنه.
👉
github.com/immaghzbad/AetherST/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IgOWHwqZgR6jifBLcR9Y7oV6glMTC51uRxVu7_d1U-6ok_iRcFoZoQYjLnSw4Gyudtg8KVrUjTwXHf4QrlRSjktIiljLiKTJgBCIr_TS4GQoxMOjzUqBzpDoB48PFSxEoHo7Ok7GnCaIPvwyPE6mtpEqx_JzBhfT0LBybkDE-qATVJ9txBgh6n_Gaa67_gmYe-YEucaI47JGUG6c-3yxCpDVy7eRQJP10-VtPxPrxmXAhQ2rnWTBTjrDh_jgXGjZabr4UrAe8p_2p8wN9nOncX12RegWQrvPoWfVawEekVMJ3toot2IExn5MTg2Rj9Va6x3Y01yNMwi-kuuF-7e45w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از چندروز آینده بخش جدیدی از قانون هوش مصنوعی اتحادیه اروپا (AI Act) اجرایی می‌شود که شرکت‌ها را ملزم می‌کند در موارد مشخص، استفاده از هوش مصنوعی را به‌صورت شفاف اعلام کنند. بر اساس این مقررات، اگر محتوایی مانند تصویر، ویدئو، صدا یا متن با هوش مصنوعی تولید یا به‌گونه‌ای دستکاری شده باشد که بتواند کاربران را درباره واقعی بودن آن گمراه کند، باید برچسب مناسب داشته باشد.
همچنین چت‌بات‌ها باید به کاربران اطلاع دهند که در حال تعامل با یک سیستم هوش مصنوعی هستند و محتوای تولیدشده نیز باید دارای نشانه‌های فنی قابل تشخیص برای سامانه‌های دیگر باشد. البته استفاده‌های ساده مانند اصلاح املایی یا ویرایش‌های جزئی معمولاً مشمول این الزام نیستند.
در صورت نقض این الزامات شفافیت، شرکت‌ها ممکن است با جریمه‌ای تا ۱۵ میلیون یورو یا ۳ درصد از گردش مالی سالانه جهانی مواجه شوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/crMbQqrSsZR9-Dw3yPyzxU-FdsIy0BM0uQO74OpZCSmzosquffd-_VtJ5o8Vta48lh9FKmBgqvSrqkFCgn2wIL9QZWxuqGDAYdSEq_zfaLp9lQO4o6PuMHwPnOE-Is2VezItA-bmwAH81lqt8Azf3y722zw4eyVLU1-Cf8ArTsAoRmkrRRNxyNB5Fq-BWfdz3WZ1JUjMULjE9m1UYxBZs4vRm9CTp2D0F4S-GiLFOXEMvbMfYElCNMFXbN6Pn5Qmonh5YBKqlDN0ow3SMWtG4ymNGYTnRkUNE5L_3nRKBlOYOu2Xfj1qcWN5TjtuTSNsmGnNVXrvYgt3eClosKse1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسپرسکی از فعالیت تازه گروه هکری تحت حمایت حکومت ایران به نام Nimbus Manticore خبر داده، که با نام‌های Mirage Kitten، Smoke Sandstorm و UNC1549 نیز شناخته می‌شود.
این گروه در حملات جدید خود از یک Backdoor ناشناخته ویندوزی به نام NightLedger و دو ابزار Tunnel با نام‌های BridgeHead و ArcBridge استفاده کرده، که قادر است اطلاعات‌ سیستم و شبکه را جمع‌آوری کند، فرمان اجرا کند، فایل‌ها را سرقت یا حذف کند، Processها را شناسایی کرده و از صفحه‌نمایش Screenshot بگیرد.
بخش نگران‌کننده‌تر، ابزارهای BridgeHead و ArcBridge هستند؛ این بدافزارها سیستم آلوده را به یک Relay مخفی تبدیل می‌کنند تا مهاجم بتواند ترافیک خود را از داخل شبکه قربانی عبور دهد و به سایر سامانه‌های داخلی دسترسی پیدا کند.
روش نفوذ اولیه هنوز مشخص نشده، اما این گروه سابقه استفاده از پیشنهادهای شغلی جعلی و صفحات تقلبی استخدام و ویدئوکنفرانس را دارد.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فیلترشکن
#دیفیکس
در نسخه ۵.۸، هسته وی‌وارپ رو بروزرسانی کرده و میتونه به دورزدن فیلترینگ از طریق متد مسک روی بعضی از اپراتورها مثل همراه‌اول و مخابرات کمک کنه. همینطور مشکلی که باعث میشد فرایند اتصال در همون ثانیه‌های اول با شکست مواجه بشه، در این‌آپدیت برطرف شده.
👉
defyxvpn.com/download
💡
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LrHf3RCHYxwFWfQuMFWcrdJvsa2uS_tSx9iDc9kHMNOWAz8Ln0WiP-u3hP1hoh7S0pjxVI4DJ8c_mV8DtwZBZ0Zk4zgaipoOJhN1ufSIzm97Xv0zy9kek1KeXze9_55ouS2DsmCSEBH8AEMDejIrCDvZ7WQt9N4ROTT6H8ukpRYIeZgJwkZ7plG4hkn_JA4UGqy7T01VDrAxjAmVvvEy-1q9ARrJ4E4tC77WJU4z-1v-NXuyfF82x9-SW_X-ErKr4H0WRl4-7OGz0pDnwvPg4HnH3h-h8tmfHM_TJ1k2DYZ1nW603uG13VHjHUppU-QCCQJ98N1s04sqzfDU5UrkUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ
#Aether
یک فیلترشکن متن‌باز و رایگان بر پایه هسته Aether هست، که برای اندروید (AetherMobile) و ویندوز (AetherDesktop) ارائه شده و از پروتکل‌های مسک، وایرگارد و گول و حالت‌های اسکن مختلف پشتیبانی می‌کنه.
اتصال مجدد خودکار، انتخاب و تغییر خودکار پروتکل درصورت شکست اتصال، برخورداری از حالت نویز، امکان تنظیم MTU و Keepalive و همینطور Split Tunneling، بخشی از امکانات این برنامه هستن.
👉
github.com/QW-AI-Code/Aether/releases
👉
github.com/QW-AI-Code/Aether_Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NhLP316H1NAlMKr967f-cudqg-_PFLtAb8CjTg9UcZcpgzHo0hsl5pmO6q6Y1_6Xcls0N6JyaU6Ts3_1n7q6g1Bq0m9e9Do0LwLZ6uyRVJmMZi1wJIwzEHK6sctPxuh7c_Gux4qtAiWKZxqdzEVoZfkr65dUXMXuX74SFPoITIHfMk7Ia2pyoTLas7cFKBfrKPEHrOBmeGjbbQpeAw-x_jVzAYkyLsWpuAU6miraHV8ZbYbClPQblYwgOLpqexFG0l_imHVL-4PZLLzeJkFulo3y3fYtxxOAu3HdBwkda304Spl3pB_MZwv-isKEG8pcQZqBbpj1OQ-WOuWHrXooYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HLD8mdBIvpMVt095oxAnItLzib3HumXxRXQImuR9o3xqrLQ2bdpisSZgdNQdqcTUOag050HPfC5sBAnq95wtrj_elvxblsuzAAalhPj0O6POdkfLd9WHvic8s2Qd-N9K-fpqLKx-WpAoErLzi425UA5kuMstNJE4sMeGaY0BWWORs8SQ7RtgtFByidgoMOqFpLaUeS5K5PFoJd_AZkJeBLn73wv0wC_6sGth-UyqWWfc0MtptsSJA1qGcrsmikAsrx9oMoIQQsj1wmriGe7-eYM-TC71_Gz7VMsYlfIGmSvmSjWVCEjMiOSveyHA9l7xgiG0QBCkxz2HBueVOUapOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b6RS3eK4cEBdfz6GRsLyl6LhNxjdI7Lfbyad8HxPHiK5maGZK_UEegNjZa8PB0k6wYJJ5iqHkNTHR0EWObWfK6_BwcHytBELlpDD31KgoYJq39d4ZuT0_2fZYa1LGmH01xQxaZsjhAYs8rZ7jiSOG9nKuLs_1FgLJ_tdGJsvbLSuZ3oUCR5vOw-ngrtofk3GZ4PDoWGMvugudtMGrJ3uwhssWDaZ8MbobGzqJV0mpsd4xwiHxr-CWN3H21Fjz5yLyKzoxfceF3cVQIJfOZag_930ktWnNwhVADJn66-l0mCuiN52uNHgxSos86xZ3kG9TPZs88zl6suUnXMamYyOTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/geReZXxP7YaMzCCLZhSiWQgpZUmIpKGv2Ab7ZizZ0M7w1Q9swCw_b_D79M-A__-POP5eOCBVDkIl_Av6yDzJrqefFHAlar25pBcyEV8D_sPvUbdGs8ny3JbpdCM7exoVDFKwSrtAaoXLaZ1qsmD87ggkEcrg7jVt6WTpqlbjXEHxQK086v7N9NmHLlsiLEnAc_n8JJLoNJNUpJMDvUdtLdx4X6bG34Lry1kY0giVaQyzZaBv6hpz95M0pEisJxKZ4eHhhIEiLjUZKKeLQk7LKmBoSN3lalupzm5Ht7d9Yy2h1B7rMLxjKvEZRl5xvBAJFgFGV-9dtUMBX2B2EewTeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E6f_gr7HffbuO89n0g6wwgkubT_X2iH-xCwp_57LUq_IXYsp4ylDqn8vkTG6ShNt_UTge0MuOhTOEEUI6C98JJROEEOdbAhRlnfXqwuVCHuIifAiP-05nqIuHSDbGEuaPzQoj8j7fDMIK8j1ABUu0xZ7Na5MVZOkoBm_rZr6XC_gmzeFJypzM3zC_xIqKrNugqgQclZb4qwRqHbvk9OVJbIw_8eFctRTZ8_8Iyy3y3ro6EmCn-GiDkt-_sx0UxPQhS7c5FkNGI0wd4jwmjsWHh7i5UJezrwou8dj8VjMAASnjjrAU_lHSSdaHk4x2e2KNv1_phkhGZC2X1-ZYh43pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kr4t2TRegL080kHg40FYqliK5h4nBLydfvW2bOlSvZa-7qRdP4Ne8ZbVEZ5l1i8QPqzM-LFkVABoZRR2WcP-ZOf8Vbw_TARqFWNhUOdT3JNJ2YOcbZs6hYzDHF1g6ahrd2qJES-fnD27fHzRwKxdPiZInDu2Sh86nfmhilaYUPaksvfAU0NoYI1fQ-HSmqe-3_8wdT7qjKmpsx2W_JSzR_o9ZKAPNVQKWk8zPz0p6pCZIp35MUAH_-uyfNRedRjM1Nv0MqBgSEvWFNg6PTlm0doiuKu0cLUqriphLqByMERVfwloQOUFrB1gCjw8I9sihqMq_ZRRmko1yg6N-7HNug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VMF3QEhdDCQRvHyW1-KJXK6n2Guhu3SXhGSQI8MLpH9uQxs1kRfk2ysVI6hnqwWkuBltSJS5BxfCXIbPxOpnWJeAP27AHmU0Ohsf6a_UHT1MKo6aj_nRP8C2lTp6mr8swWLoDBxBCq87bqizAAFyBEfH3TtHBc3Ff_Tbkv1YWAHrCCvwoD0xQpAY60NiJW-usKhCEAf0oMN6wIUHfmI99HWFJ915cJF6OxNPWbYNoNlDhWXVipE8OzYtVtTyETkLuxA_klOSiEd8LD-TiyIHUwFzKez0cHAmju1RhUtbSxqMnimH5V3ilElw9YNc8kF07Q5O1nPCb-SD7p4PC89ASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pDOrdEvUsxlSMYZyJPdZrUZwuD0eIGJ_ZetxAaK2s0s_1M7hxJbSsntPf4OqcTrEBanysUEXKkpzSK8wJiLlHSFJ7d9z6VxKs9B_wX6bpFwW7t2wExjlpBfhAzUuashsZwusWOKywS9tcFLJCzho0tV6IcmUBMz8U6OCpVkLNeDx9PBoiOeTJwnSYIH3njGU5mBMLchYFhhcJZpMD45lBBYlh2fnGcjkmhN5m35LAj0wv2rOaJ0j-ifE0vVkqBZTslAGH1BTgF5uGT1tut0xJeXstbbN9-Fz4K3ONhvgLQy_OzvMPsy2gw4mMp9-1wkIj2YKnhF_nrMICZTylvNUFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KSeuOvmLDytD3U8GvWfhDxc6WTRPi4VZyR8Nad5Q06hN7Ad83duDh7uMa800z5X_rZl85gbucHJdvuP-slrpWdq-CIalRmt93YSbzgM7ipeQfiGWN5oWzJdcGV80YbxBUP9_Rv1_cedhqRCC9q8mjQZXy48jJBDOIX1b4Qx_vnSNTUOf_4zXW5rirHjY8_XSEbbRMZm79HXdsbl-3r1ciKHWnYpN0Lga4prLbRxLidmkKHRVLhxlK7SnhBmC9trtVPH_Pg4x5Qujci9lBD_R3asoSczEMWmBWYtcgOOaHT5E52ZJknPvHzhcNS0M14_sukeRCRUIX6lVL09Ld6ec6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cZZEqxCUreXVo6IwL1gjrx54TNdA7Cb101zn0ZgyqTTM-C_EERXLMmTH1fJjPZWoAR-PH0qYYzJVRYG7Tc7TUXy65ZmQgvmFRu9SooP5wrXObEIl-I2l_lvxAsAyGL_amwKdcOWknnbZnqSHwGH7NeURMPVegMjleGE_4eqg7cIZue39VrBfO620WNWxQYLGbO3hx3TdMLU4GVGvSUfUbqRhIKZOuYATGqgx4OOTLRY7-jQmnPh9lavNuRwprfNMvNlwC2qE-7jVfZ1V6ruftPxdFQ3R7mzFkdK_rpL-LaOpkszkrWzKGRe9M-Lpm3yJ9ADtlsGlprUnL2uzp0_nwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن Aethery برای اندروید یکساعت قبل به ورژن جدید از هسته Aether بروزرسانی کرده. اپ Aether-GUI برای ویندوز هم کمی عقب‌تره و ۳ روز قبل بروزرسانی کردنش؛ البته احتمالا بزودی براش آپدیت جدیدی ارائه میدن.
👉
github.com/ZethRise/Aethery/releases
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lr8e3u0cd1RZVut0mqcSmuQc0WH9dGiqovWn-h5UhqytW9FJUwCykHpwo8XdJ0PIsRenqtMlcHAdGfzaPzZhx1n1XKyz4gsFjxS1rTYcF4eWJFyXKwq9HchZvl6XiENe8sJX2gjyGBati7-Z3234hGUsAGxUGgy2y6hhKY7NgVgwBGoAPImOSD3VQIeU2fgxglazNmHMZ1kNQLnTL8HdcQelQtU_fFjZOFm1GvFXPg9IOX0zEpLkLD00Tk2K-kBd_4XvbsFc4DfLzZrRixV6c8GeJdtYksU-udEzcjQwquE9QDpawSFaVEz1ObyIRFyxQJ-aaEXU9hDpeaSqyDXfvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۳ از پروژه متن‌باز و رایگان Aether منتشر شده و مهمترین تغییرش اضافه شدن حالت اسکن Ironclad هست. برخلاف حالت‌های قبلی که فقط بررسی می‌کردن یک اندپوینت در دسترسه یا نه، این حالت قبل از اینکه به یه سرور اعتماد کنه، یک تانل واقعی برقرار می‌کنه و یک درخواست HTTP از داخل اون عبور میده تا مطمئن بشه اتصال کار می‌کنه. البته این روش زمان بیشتری می‌بره، اما در عوض احتمال وصل شدن به اندپوینت‌های خراب یا ناپایدار رو تا حد زیادی از بین می‌بره.
توی این آپدیت روند اتصال مجدد هم هوشمندتر شده؛ اگر ارتباط MASQUE یا WireGuard قطع بشه، Aether دیگه برای دور زدن فیلترینگ مستقیم سراغ اسکن کامل همه اندپوینت‌ها نمیره. اول همون اندپوینتی که چند لحظه قبل روی اون متصل بوده رو دوباره امتحان می‌کنه و فقط اگر از دسترس خارج شده باشه، اسکن جدید رو شروع می‌کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پژوهشگران امنیتی Insikt Group وابسته به Recorded Future از شناسایی یک کارزار جاسوسی جدید خبر داده‌اند که با استفاده از بدافزار MarkiRAT، کاربران ایرانی را هدف قرار می‌دهد. این عملیات به گروهی با شناسه TAG-182 نسبت داده شده و طبق ارزیابی پژوهشگران، ایرانیان داخل کشور، مخالفان جمهوری اسلامی و فعالان مدنی مرتبط با جنبش‌های ضدحکومتی مقیم اروپا و آمریکای شمالی از اهداف اصلی آن هستند.
مهاجمان برای توزیع بدافزار، نسخه‌های آلوده برنامه‌هایی را منتشر کرده‌اند که برای کاربران ایرانی کاربردی یا جذاب به نظر می‌رسند. از جمله آنها می‌توان به فیلترشکن Pis2ray VPN، نسخه‌ای جعلی از Star VPN، برنامه‌های YESHICA، YEPlayer و YEMPlayer و همچنین یک وب‌سایت جعلی با هویت Starlink اشاره کرد.
بدافزار مذکور پس از اجرا می‌تواند اطلاعات سیستم، فایل‌ها و داده‌های مرورگر را جمع‌آوری کند، اسکرین‌شات بگیرد، دستورات مهاجم را اجرا کرده و ارتباط خود را با سرور فرماندهی و کنترل (C2) حفظ کند. پژوهشگران همچنین زیرساخت‌های جدیدی را شناسایی کرده‌اند که نشان می‌دهد این کارزار همچنان فعال است و احتمال ادامه فعالیت آن وجود دارد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sTGWtEMa5dMzwbFzZEz8DjW07Zd4cgbXT-6uxI5wrcv49xSbL9usoopKNS54ciJgOTuYrKhHUSjyHreIlT4X-lwuYjs0BnuO8LbYdQqGxSTKOl18w5i5zWQAqClhHH4-1C-a8eSh5NOgJqKWW3T_Pii00FD4Hg-riFvW1O24ug4Q7kvvm3hFkl2q1k7HpEuK2UQiXQX8ab6oGeWtbsOQJBLhklAJ1QY1yh1YLwI0-zeuVVYtZK5a20qSLSUvevw8tEI4BKtj6tif3ePBj6o43yDL_toHzc_8gxhqyq5UJVbSUVGcU3sGshha362pXLn9BtJw0qkwRWiegU8Ckwe2mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران امنیتی از شناسایی یک زنجیره آسیب‌پذیری جدید با نام wp2shell در هسته وردپرس خبر دادن، که می‌تونه به مهاجمان اجازه بده بدون نیاز به احراز هویت و حتی بدون نصب هیچ افزونه‌ای، کد دلخواهشون رو روی سرور اجرا کنن.
بدلیل شدت این آسیب‌پذیری، جزئیات فنی و کد اکسپلویت فعلاً منتشر نشده تا مدیران سایت‌ها فرصت کافی برای بروزرسانی داشته باشن. این مشکل در نسخه ۷.۰.۲ وردپرس برطرف شده و برای بسیاری از سایت‌ها بصورت خودکار در دسترس قرار گرفته.
©
slcyber
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VcKzX2iPN4kZIb9Ms0V-wOay5m0hwVvty3eGTXkfyQjbeiSfykRxUdhtnybTnXFSArzORzgj80TjiwtW7pTnQ4qPahT3TAD8tNMB-j9aCKhJKrwfV4x9s7NkB8eLbJvzRn1VfRPiYIeOF70Ikcb-lB4j_HomouYyV31VaV-CLEWxzRqS-Jg2GC_EqkQlk7JWZQnsi7Pb9WYI7moMOsG57Qt7WUG04O3P7IX-YlBMzgltuFQ8O14NMJLPJTn4kiGVhxWtzKxSPq3ejFtYMXlgdf7Q_ipRvMGGTWcv3QEv1lLVUjuVTpiLbIqWpSuvBwyxqG4SIVmSrmFqsIXU8kLvOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F-4JIfCwahmd2pBWi_RNN51Bx4Uajhbm6vi8flsbiVzXVk9ZZfNg0BSF4FnB57HA9MnbIoc8IcOx4n43CoJuOTfhGDII44xxSaVqeVAAklCCciD8ag-lLsU08fJBGJMFbR77XPQTaF409_thtN4CHohxY5KVatoe-178_OD2H18xfTIopSGKeKMpa8Is1cVxSfPUqj_Np1jvI3uVXBDzGfMhIw9to_7oCRFs1NLIjlQdYx0BWUG-kJfK5FYOEJn6y-gijn730JwcUqHhCcjoR7D6ZpOudxN_MQqTsd4dX2ys-lN39BXHuRFKLC-V24edCBfnxdhOqE9dFCCA2mvZaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ dicodePing یه کلاینت متن‌باز و رایگان برای اندروید و ویندوزه، که مدیریت و اتصال به کانفیگ‌های مبتنی بر ایکس‌ری رو راحت‌تر می‌کنه. این برنامه از مدیریت سابسکریپشن‌ها پشتیبانی می‌کنه، می‌تونه بصورت خودکار بهترین سرور رو بر اساس latency، jitter و سلامت اتصال انتخاب کنه، از حالت TUN/VPN پشتیبانی می‌کنه، آمار لحظه‌ای اتصال رو نمایش میده و امکان تعریف دامنه‌ها و برنامه‌های خارج از تانل رو هم در اختیارتون قرار میده.
👉
github.com/mcodersir/dicodePing/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پژوهشگران دانشگاه میشیگان، دانشگاه نیومکزیکو و مؤسسه فناوری دهلی، ۲۸۱ وی‌پی‌ان رایگان اندرویدی با بیش از ۲.۴ میلیارد نصب رو بررسی کردن و به این نتیجه رسیدن که بخش زیادی از این برنامه‌ها برخلاف ادعاهاشون، امنیت و حریم خصوصی کاربران رو به‌خوبی حفظ نمی‌کنن. توی این بررسی مشخص شد ۶۱ اپلیکیشن بخشی از اطلاعات رو بدون رمزنگاری ارسال می‌کنن، ۲۹ مورد دچار نشت ترافیک یا DNS هستن و بیش از ۸۰ درصدشون هم با سرویس‌های تبلیغاتی و رهگیری در ارتباطن. علاوه بر این، خیلی از اونها هنوز از تنظیمات امنیتی ضعیف یا روش‌های رمزنگاری قدیمی استفاده می‌کنن.
اما نگران‌کننده‌ترین بخش گزارش مربوط به ۵ وی‌پی‌ان بود که فایل تنظیمات اتصال رو از طریق HTTP و بدون رمزنگاری دریافت می‌کردن. این ضعف میتونه به مهاجمی که روی یک شبکه عمومی مثل Wi-Fi رایگان حضور داره اجازه بده تا اتصال VPN رو به سرور خودش هدایت کنه و تمام ترافیک کاربر رو بدون اینکه متوجه بشه زیر نظر بگیره. به گفته پژوهشگران، ۲ مورد از این برنامه‌ها این مشکل رو برطرف کردن، اما BambooVPN، Free VPN و 101 VPN همچنان در برابر این حمله آسیب‌پذیرن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OSGncemB6hoGZtnGUkuP9U1TzGtY9GQ1Fp9KFJ3Nz8XjN4MfzTphj5ALiOTAhEzQ32a-Ij2T9_SqIt52XmvFBbxxb22YX3ZJKFXcoX7Xex52lFZ2nTpnYivjJkcGuAxytu-oQ_FlLqyuxBGOig1XQkKnaVC5Qfif7FtcIsl9Q9NDtwZhq_yGyHooaDEkVtBlXPkN4DG5md2UJIxHTBxCeA65--0dAh_GRBdUj-n_nCXMIwXbZU419SqdsZyx1d5z_iM5yy0QQ2vmmuKbmdput_zRVJ5roWUIUJg2kZx9cf9n7YIYsOCkL9k3bKaY5JK1qdyCJmtwwL4IuPWUvzz3jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aethery یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که بر پایه هسته Aether ارائه شده.
👉
github.com/ZethRise/Aethery/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fkjHTrkb9n49z8vK6Cr46QOBDLECZ-ZmPsk7pziEMsFaBO5QPR6V7viviIIkvZzqCDnnAsBFOHnCYVooGQZl_Dll-OVOc5W9pas5AVIgDJdWkvmuRUOc9Ovu7pBBqbLUx72vilNIVqKMFdD-VcD5VK6kDbpez3xnGpvZTYlt0iuY_hNAE0-ZiLfREC7WysPZRKI6uAXLp1Ht5sM2yn62IU9Qo2KIRN5gWv1rIvvAL2xD9LvOlxaHFhnIhQYplGMAjCJdCDiD5XWcE_Shl5DeD9Ivk5sKI7mEZVY27D1oF49p8zMsZtkbUCNDNW8_Y579OdoQgf-pZfTmwpY8ZkfGsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت رسمی Sing-box برای سیستم‌عامل ویندوز بصورت پیش‌ازانتشار عرضه شده و طبق اعلام توسعه‌دهنده‌ش، همون تجربه‌ای رو ارائه میده که پیش‌تر در نسخه macOS در دسترس بود.
👉
github.com/SagerNet/sing-box/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hCtVTAs6tZ7AqKcwwafgi2ErrcTY6_F7WCPGqI2d5i6ppOf8KDhctlKBaN5HEw3jbcXC1A7qX9mZFZw5AtsTK-vxuU4lOcOBMADpjG67HmPWQFkrvovX_ChD5EpdlAB7r5lapg07ZiHJG_T4psuzMb0zIY-dSWdFeUYlOBV5EARjiiSWvQmTRCjLNmVqAlL4H1ZQ8EA_mfzkULc6ALqiTa5-YGfaNpBpFPddiDVbAe83BPEpcK2FUKToQfsetkC-w6EZTEWzipyNeyyRY6E6ekujJFF4isRQUnN3S859GUDtwyJEObYy8PFWQG2spASP-yi0Md_NF_L0A9eflD169w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aether-GUI یه واسط گرافیکی برای هسته Aether جهت دسترسی به اینترنت آزاد و دور زدن فیلترینگ هست، که دردسر سر و کله زدن با محیط ترمینال رو برای کاربران سیستم‌عامل ویندوز حذف میکنه.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nAiZJwvFi49UYshykSeLWSyykm8KfcaebWLqUd99Nbot5MHyu8Vrwsavy6FdbjaZCTUsfXg-oeQbw-PUGaLVho800G4Z5f7kDjIYDnnjuEEGBtJsvH9x1LxNsM97efc6mqSg4q5q7RlucaqVma9hCOsm_wbYOfQ6W-jWKS6gUoK1MYfMwBf4bwKHaG_9EF4Xldf6uydP7HLIbYP65NiSRb1V45jdK6tT1CVl_TzZN0lxNoPuLLIVXUZx9t1ROjoOjgsReruY9iR1PClhVwbodOlNRNTqy9IctHVyDue0_GOxRygXx_IdYOD22-C88tF_navSGI7cQjEukXAcpxOhHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت در بروزرسانی امنیتی جولای، بزرگترین بسته اصلاحات امنیتی تاریخ خودش رو منتشر کرد؛ بسته‌ای که ۶۲۲ آسیب‌پذیری منحصربه‌فرد رو در Windows، Office، SharePoint، SQL Server، Exchange، Defender و سایر محصولات این شرکت برطرف می‌کنه.
اهمیت این بروزرسانی صرفاً در تعداد خیره‌کننده آسیب‌پذیری‌ها نیست؛ دست‌کم دو Zero-Day Vulnerability پیش از انتشار Patchها، عملاً در حملات سایبری مورد Exploit قرار گرفته بودن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fu6YUvxBescadmgzBL-s7Snf8oeXWXg-cDJgyboR4NVEJ1HfHz2_tdHd71gZhjuELGacYIoAxvFQKEq7avRR1Cu8Vfie7PAjyJL4ljhcVi0J0W-hxvnV-wUXLT46Xml4E0YB3DTpcUIGZG6Mh0Gw6SHDsD23qlzkICzYshiyAjwWtYvwrtl2dsbQzbszYH95oRpLnHOgpmhtpxs2BiKhLxvf2x3utGTIVFGYx7RhAamJex16fyhL7YkpW0utMqB5ma50sHDO_3ukK2TH1q33Y1gvytYJh7PpoUb0Ssitqz_Gs71_Dh7cKLtJIj3i3VNwMgHVaUQe6_pudlPnYpcu4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Aether یک ابزار متن‌باز و رایگان برای دسترسی به اینترنت آزاد و عبور از محدودیت‌های شبکه هست، که با تمرکز روی سرعت، پایداری و مقاومت در برابر فیلترینگ توسعه داده شده. این پروژه با ترکیب وایرگارد، MASQUE و WARP-in-WARP، ترافیک رو تا حد زیادی شبیه ارتباطات عادی نشون میده و به همین دلیل روی شبکه‌هایی که از DPI و روش‌های پیشرفته فیلترینگ استفاده می‌کنن میتونه عملکرد خوبی داشته باشه.
یکی از قابلیت‌های کاربردی Aether اینه که خودش بصورت خودکار اندپوینت‌های تمیز رو اسکن و بهترین گزینه رو انتخاب می‌کنه؛ بنابراین نیازی نیست که تنظیمات رو بصورت دستی انجام بدین. بطور پیشفرض هم از HTTP/3 استفاده می‌کنه، اما اگر شبکه‌ای QUIC یا HTTP/3 رو محدود کرده باشن، میتونه اون رو روی HTTP/2 قرار بده تا سازگاری بیشتری داشته باشه.
این پروژه روی ویندوز، لینوکس، مک و اندروید (از طریق Termux) قابل استفاده هست و توسعه‌دهنده‌ش اعلام کرده که بزودی قصد داره هسته Aether رو با زدن Pull Request در فیلترشکن‌های ابلیویون و دیفیکس ادغام کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rVcOV1jTQxp0akUEgk7lqJHuMtbI78TFYcIHFT8LxNlxOqxCx47WGRcosb7b4CpTGlh5o__bNjNug7AlCiM3uIJgE-tq-Y1YBA1nrauP7h6NqenX6hR3J50OcgTtD0M_WPjwR9CEyeTlNvWKwqE__6uQpPnreoAOQfC-BVIK9B-ivdUpWLhR1uwyaD2RHkl-siPOo9E3IZiCF3nQY87RsHpmcWYT5bBp0-8l8x9QQVPDI8DTOFQRpndWOc8mF6n-QKiN7vLRnYV0dMiW-JWKIWOccrYwYt_UMXulDan0gUS33m7_SMKB-MFVs8hmsdMEuk6I-ELehOHf1hE_N4U4nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دامین
t.me
که بدلیل تحریم‌های وزارت خزانه‌داری امریکا مسدود شده بود، مجدد فعال شد.
©
Linuxmaster14
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نزدیک به ۵ ماه مجلس تعطیل بود، آب از آب تکون نخورد. ۱۵ ماه وزارت قطع‌ارتباطات هم تعطیل بشه، وضع اینترنت بدتر از این نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pv3hAFv5vqfN8beb-vTN-z_KSmFK5E_giwG_GIVjiAM6TbMsmaGE9LSPO7t6dFB-6zoBO-aURdMk48REYmeTA9az0D8ViTvTNRwK--W-ugQfmKnfxaEmPYGh40QNdegVpdrGDbfOp_g_ToWi9Y0VBctIdRHCRK00ZM_kc0b1dLeuiUeUFjY_X4xZ8yCS8YyfNn2-phOto8iRxlq2NSa4PEQrRrOpIVkVucw1IVujiH82Kk_PYhk5Oxi4yW3RBKJvRzzGN-uVE1inyw4WT-PtAV5WzJoK6UYMdzXG73TPucNpwxrhJ72Xd1Xcs6pue1WfU9aLW0BOV0A7LrCy4Z93dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به یکی از شرکت‌هایی که API می‌دهند مشاوره مارکتینگ می‌دادم. چند راهکار برای کاهش هزینه جذب مشتری یا CAC گفتم، ولی تاکید داشتند که باید API‌ رایگان هم بدهند. پرسیدم چرا؟‌ خیلی راحت گفت: چون رایگان است، طبق شرایط Privacy & Policy تمام پرامپت‌ها و داده‌ها و خروجی را می‌خوانیم و ذخیره می‌کنیم. فکر کردم شوخی می‌کنند. بعدا دیدم نه. جدی است.
(...)
مواظب باشید، لااقل اطلاعات حسابداری و مالی و مارکتینگ و اکسل فروش و لیست مشتریانتان را به این API رایگان‌ها یا این سرویس‌های هوش مصنوعی حتی پولی که در ایران هست، نمی‌گویم ندهید، می‌گویم دقت کنید.
©
AdelTalebi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sVLBsqIJP2bTB9IXxCuFlGyY9wvEddteTPXkJDJ1nlucp14HWV4lqxeMSNnk5M1sKSevfmVFD89cRexhnOfVnwNsLsyMpM-Z8h_NtKlxGGxGmmen0ceVX9ADebLZzxoA82i3iPOLlzFnNPPVo7u4FDulqugEXSNL8fx48CO_3R6UnkKGCf0v26KFbIc4LuNsAE5yIVw1D2JQ8exHLp-IU1X3nvvbRiYlffGRsjhSxzHmrreVgGYw7hthHQLF1zJOljSLAzEzgwl43FNQQr6TqqmWcZhtjeYyj5X5dwIZFECuYksFDJGfbgyn63MA0h_Ogn0mtizDKZZMnPNy0Nh9lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروتون در
یک مقاله
جنجالی ادعا کرده ویندوز دارای شناسه‌ای پنهان به نام GlobalDeviceId (GDID) هست که میتونه یک نصب ویندوز رو بصورت پایدار شناسایی کنه. به گفته این شرکت، این شناسه حتی در برخی شرایط با وجود استفاده از VPN هم میتونه برای مرتبط کردن فعالیت‌های یک دستگاه به کار بره و حذف یا تغییر اون برای کاربران ساده نیست.
پروتون با استناد به یک پرونده قضایی معتقده مایکروسافت درباره وجود و نحوه استفاده از این شناسه شفافیت کافی نداره و به همین دلیل از عبارت "ویندوز یک جاسوس‌افزار است" برای انتقاد از سیاست‌های حریم خصوصیشون استفاده کرده. البته این عنوان بیشتر یک موضع انتقادیه و نه یک نتیجه‌گیری فنی قطعی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2487">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بانک ملی اطلاعیه زده که "کلیه خدمات بانکی و مالی این بانک شامل همراه بانک و اینترنت بانک مجددا فعال شده"، اما ایسنا نوشته "اعلام بازگشت خدمات بانکی به شرایط عادی، لزوما به معنای پایان مشکلات برای همه مشتریان نیست و گزارش‌هایی از تراکنش‌های ناتمام، کسر وجه و اعلام زمان انتظار تا ۳۰ روز کاری برای تعیین تکلیف، نشان می‌دهد بخشی از کاربران همچنان با پیامدهای اختلالات اخیر دست‌وپنجه نرم می‌کنند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">طبق گزارش‌ها اینترنت در برخی نقاط کشور از ساعات گذشته با اختلال و کاهش سرعت همراه شده و دسترسی به برخی سرویس‌های آنلاین با مشکل مواجه است. همچنین گزارش‌هایی از قطعی‌های مقطعی و افزایش خطا در اتصال به خدمات اینترنتی به گوش می‌رسد.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/inIsrULFN6PiTLjvz-z50x5FqlUpnXWgrPUIOj_VtBN7vUjRdm4R05kAApidgGlqvg7f0HMNLp8LzS4C0eB_6o7Gp7nTogqdHGLBU837OeZnaZXQFa-ulG78wuROyQcnHdPmNp8OHypEEBIR_FaZKOurDpdKBoDSNBDXJ92xfcHKsPxMEEleo_raMHwhnqnG6Nl_VpGVCi64-oiMRi-_ci8P4m8pp8Sdq8V4HFe7mNawGip2sfisnHl49oBJWLOyf2R2YBPKpAI6a-VQIYPet3pQkqonvGNiUZes03EXkFKZ5D3Vx6sur5syF4awnHFfOaAuzTOAdai09gl9EsGcQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pyDrlG-2n8QDghJSAQ1tvz4_MUWsn7u6UVDRMfKKhWl-sJEZpMcR0NJgghxA6Ed8VojrtFsZs9q55kWEmRgDGjpJEZZyQThripIIxrZHhv8r4EySzZAjZMn3OWq1yUWXm78mtvk2uS6-10QeF-54AK1qnOFsx-XN8OjDR0ABeUOW48tV8nYPUE8_YPNVLco9NDGDv7ggZ2M_v0zJMZUyKy_a7GAml-NbZndujqoImKjmuJdGtUgmbKG4J0vRxPVeUX0f7A4ZBFRsOtJKIjP7R__d2ZJiwAPNd5aQG06CXjFOfCewEdITPrR0NCqIJj8q2-OCuwZtxRruFtapkzI2Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل زئوس یه ابزار متن‌باز برای ساخت فیلترشکن رایگان روی بستر ورکر کلودفلر هست، که امکاناتی مثل آیپی و لوکیشن ثابت، دریافت خودکار آی‌پی تمیز، لینک ساب و QR Code اختصاصی، فرگمنت، شبیه‌سازی فینگرپرینت، بکاپ‌گیری و ... رو بصورت یکجا در اختیارتون میذاره.
👉
github.com/IR-NETLIFY/zeus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2483">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ILmRnaQoquytVzRytmZNCj-2Un427I0EHyoNRRpG3_aQ3eHYkIWFHqitnwEr1P290lhgq6LR_sIpv7QuOYnYKbBd9r9I9C_-nBVOuZhnMA81Um2UBTmHkoxsq2-IRbuPvx8-1CASwa1lA2iOCjfZO05LPsZ-g1WQsMNdEQe9JwsE6KKJirP_d1i1WudUsQaSZJB4AQ72HZOyGNlYspmG5Wt-u4acn5GyLyRqVmgrYxNUl9Ouh6LNHryN5hpC2bea_NfKBM89hfERCzdFWfkGI5ZfX7l99mBhgt7HWjcO-iSOOdHULunx74m84MyQQZceZNBlrMjVyfLtIfFozcxIJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت یک آسیب‌پذیری روز صفر در Microsoft Defender با نام RoguePlanet رو برطرف کرده که می‌تونست به مهاجم اجازه بده تا با سوءاستفاده از یک نقص Race Condition، سطح دسترسی خودش رو تا SYSTEM بالا ببره. این مشکل با شناسه CVE-2026-50656 ثبت شده بود و حتی روی ویندوز ۱۰ و ۱۱ کاملاً آپدیت‌شده هم قابل سوءاستفاده بود.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2483" target="_blank">📅 08:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2482">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b0xOaDZJhP4GDC4ZcI8JBMjT4mq3UyYAa5oFEGo-f7fmw8GOgin6D3Tkp2DTqp2DG7K-u6nXT6UbkoxLLR9HrQCi2rn1rJtWii6baUz8YqUGGyhY9pQcoNh0lc2MkzQ6eS8Qu6PreNMynJCWjKAzHi4D_v3Cm98VJOLKSg_A3tEI82B2t0xjQ5vPdHemsg2vs713B7aoBc_UymEYYgvQycNtAv_-EWQSYr7u2gM52SokyYnEdCiFfE4YcoAqDXJanmCiYGUUi_PqOhGyYeh3XHz6ew3CDa0w9E97K6iyLoo9cUoVgTgCRtDv8-FK4qaIpC8rfJRXBAq59yclaQrViQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت اندروید NipoVPN که برای اتصال به هسته این پروژه و مخفی کردن درخواست‌های HTTP داخل ترافیک عادی وب طراحی شده، حالا روی گوگل‌پلی در دسترس قرار گرفته.
👉
play.google.com/store/apps/details?id=net.sudoer.nipo
💡
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2482" target="_blank">📅 08:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r2rhz_8Hh20TsSK1ID_Lgrhdz12laXYUTIsRlr5AXokmePx6NM3Ghti0zTSb7ZDhnU3pqDCGWjFYHXT68WxQo-5fkvTDAq07Y43cl_VGm0FOqc7i2y9BYLEBxnxf9x2ex5SDAmqpBMHTq7UXa4hjnu_73iqyR8pJ1nHN6dTaamCzdgcq7OtmFNNc6LdrHGqvU7ofsbAASrO5LlKWNWKEoYoYm_drIwxTN6H1Gdiq9HYFB0H4PeHrYAyS7lIxAIu_Dtt4aNPApCo3qQO_FDnHwDmNgeD0ytc32HeyKnNhonnTVU0svFoLIFpSz-HRVGJHngI3EvziVgYb63fAlSdteA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار BG Scan یک اسکنر متن‌باز و رایگان برای پیدا کردن و اعتبارسنجی سرویس‌های شبکه هست، که اجازه میده چند مرحله اسکن رو به هم وصل کنین و عملاً خروجی یک مرحله رو بطور مستقیم وارد مرحله بعد کنین تا فرآیندهای پیچیده راحت‌تر انجام بشن.
این ابزار از پروتکل‌های مختلفی مثل ICMP، TCP، HTTP، TLS، DNS، DNSTT، Slipstream و Xray پشتیبانی می‌کنه و علاوه بر اسکن، امکان اعتبارسنجی و مدیریت نتایج رو در اختیارتون میذاره.
👉
github.com/MohsenBg/bgscan/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2481" target="_blank">📅 08:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2480">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PFeQHil_wrdr1miwQH2psoE9oYPDpQeTzd5eBnfPj-ZCBWXIcxL-WGZELnILeH07o9ym4ajUZYU_IV_R5EleEfpd3Mxl8m8t45Rv3T5cerAsmmPHi4damQlGtjaINJvPyTQZyd0VcJvmCyA1wINP3fFvnTgq3u9eIZOh0LKid-6R-qmVTBHgZlRMXqpTVwpwV40b1d7B2en-C7rXrWJzSTafvU-AsCRMurqTrSG-aV6L4hFAUWCosgzlk-Snu1aXG9C40OjuvFc10Hgdh7Z9iho2PVUZPXUeLQc3Kd92lZz7cQ8CRNOWhkNqprGnudGHLBzOXt_BBOyVL3ddDWcKlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاوه یه ابزار برای اسکن، استخراج و اشتراک‌گذاری کانفیگ‌های فیلترشکن هست، که کار پیدا کردن کانفیگ‌های سالم و به‌روز رو راحت‌تر می‌کنه. این وب‌اپ میتونه چندین کانال تلگرام رو همزمان اسکن کنه، کانفیگ‌هارو بصورت خودکار استخراج کنه و در نهایت یه لینک سابسکریپشن بهتون بده تا مستقیم داخل کلاینت‌هایی مثل v2rayNG، v2rayN، Hiddify, Streisand, v2box و ... وارد کنین.
توی کاوه می‌تونین کانفیگ‌های خودتون رو با بقیه به اشتراک بذارین. علاوه بر این، حذف خودکار کانفیگ‌های منقضی و امکان رأی دادن به کانفیگ‌ها و منابع از جمله قابلیت‌های این ابزار رایگان هستن.
👉
kaveh.yebekhe.workers.dev
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/ircfspace/2480" target="_blank">📅 08:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2479">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sc4wJ_M5DXfTM8z3Oh5LzL9FWTHfvv4xU3LIZGkBOWacuy3x9HXLjiEU9vQLabUow2zE6llFZxH62O_lj2QVi-bsMSkkknGVYY0F_X3kC3lcMNHIEBxXNUwbRRrjq_jDgcMo8P6oWUtZsVk49ru9TEzVqn2wZkIwSySkSDgTHc4hxb34Oo4meAwQ6fl1n7vyeRZYgMi3lxySqNtjYP_zhaVl7IwkJ4ZbdSj6yykkUNJJRBgduTqBRzeLmTp-1UlL-LKOfvIiAVgIqd_I61VouIKmmTIzaKe93qxjrcR0U_mHc_NEuJkVe6hiOuHrIAHVnovxTd3AykfHo-KoTdaTtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ابزار MTProxyMax آپدیت جدیدی منتشر شده که توی اون از بهینه‌سازی‌هایی مثل BBRv3 استفاده شده تا عملکرد سرورها بهتر بشه و مصرف حافظه هم روی VPSهای ضعیف‌تر کاهش پیدا کنه. همینطور در این ابزار که برای مدیریت پروکسی‌های MTProto تلگرام روی سرور شخصی هست، قابلیت‌های جدیدی برای مقابله با DPI و اسکنرهای شناسایی پروکسی اضافه کردن تا شناسایی و مسدود شدن سرورها سخت‌تر بشه.
👉
github.com/SamNet-dev/MTProxyMax/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cepoft0Pm0tPnsR7VxZAihyjt97yXMgPFdIBHaZjzGF97hBEshbp0c_tQJFqYdJQx8s4PRn_hbBSALa9hGKsUEr59eD4H4L5qPuVD91LJ9tkQ1GbdMJ8pZ0W2y-YxzFpeXtrPvXzGt-oewV6IG_4C3um7vhHR-fMC8fiIhkCIIdw5OWargs1opIFsA9khe52RbbrHinvbYA8AfC_ssqM1-bIdgl1niCAzZl1v2KzmR4BoaPiUGFeiin2GaxLHKhYWpvny7thfmco25-on8juoUjKIssoMx2-Y_x_bhvfN2xukk8ypFpXRkpDgFVRdTf49Yjsighze78_jC8AVPBBXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.
این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده، اما چون جلوی سانسور و دستکاری DNS رو می‌گیره، در شبکه‌هایی که فیلترینگ از این روش استفاده می‌کنن می‌تونه باعث دسترسی به سایت‌های مسدودشده بشه. علاوه بر این، رمزنگاری درخواست‌های DNS تا حدی از کاربران در برابر حملات فیشینگ و برخی بدافزارها هم محافظت می‌کنه.
اینترا توسط Jigsaw (تیم نوآوری گوگل) توسعه داده میشه و سورس اون بصورت متن‌باز روی گیت‌هاب منتشر شده. این اپ از طریق گوگل‌پلی در دسترسه و برای استفاده ازش فقط کافیه یکبار فعالش کنین، تا در پس‌زمینه کار خودش رو انجام بده.
👉
play.google.com/store/apps/details?id=app.intra
💡
github.com/Jigsaw-Code/Intra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2478" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2477">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WM721HbzbDb_zlUx4gQI8P-GlaIApmpDSUlqblI0nxL6ADpxgdTo1ibXS7H6FbJxqCsp3RsV6xGI2EkPm5Qri4LCKuB26d3NULxv1MlHaXDsH8rcJ_wVSVZuoSrGCbfWmzVta9sPf1ep3hshv3yqZC_isxm47ZIKDwkNrSxXRcZRgSu8X-JTt9nz6ueOBL9s4xFmk8vbCUjrXZA_V6cacmLQ6OyG-Hg5w2GxrLiRWXaRCEkgn1nZZEv7ZH2sIigga1zaosUSGxr9Tvt5S1t_nnj1B1bRi2c4N5bCTqi_XBA8vpVRSwqEeulThshGAqmEzuAMNzBg-_kVi9nP-ZIKCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محققان Datadog میگن مهاجمان با استفاده از بیش از ۵۰ حساب قدیمی و غیرفعال گیت‌هاب و توکن‌های دسترسی (PAT) افشاشده، از طریق API گیت‌هاب در حال جمع‌آوری اطلاعات سازمان‌ها هستن تا برای حملات بعدی آماده بشن و ساختار داخلی، اعضا و ریپازیتوری‌های اونهارو شناسایی کنن.
توی بعضی موارد هم تونستن ریپازیتوری‌های خصوصی رو کلون کنن. به گفته Datadog، چون این کارها با حساب‌های واقعی و API رسمی گیت‌هاب انجام میشه، تشخیصش از فعالیت عادی توسعه‌دهنده‌ها کار راحتی نیست.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2477" target="_blank">📅 07:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2476">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qL9jdHt0cGILnIDi5bPR-pcGcEhxewcviDm4N-uu2qcIehRFHl0jTOIUQfQh9LA9MY0tKetUezzGELSLd5oTIW8qScXskIZxaLA_QH42dT-9TIZxv7PPHbv4AErqdJetcsaqbmtXYqXsNhsLWWLhR0RAvwO5k0dmmrOuaV2s9IVdaj04rLlOMbFum-wCZk5Nlox_DrVd7sNBbdjcLtTB1lLN171h87iCaUCuNz12Oo3_bCw6HYdrgK17_rwes38WjsQ9d3IMq6tp3PrCKS9WtE-AbTd1ogEFbB3qYNYrkg-efhQZbeVrrhZDcDiafteCBM6h18SP-VTH_WExLn8EBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک سنتوناس، مدیر ارشد فناوری شرکت CrowdStrike میگه خیلی‌ها دارن روی این تمرکز می‌کنن که "کدوم مدل هوش مصنوعی خطرناک‌تره"، در حالی که تهدید اصلی جای دیگه‌ هست. مشکل واقعی اینه که هکرها حالا با کمک هوش مصنوعی می‌تونن آسیب‌پذیری‌های قدیمی و جدید رو ظرف چند ساعت، و بزودی شاید در چند دقیقه، پیدا و سوء استفاده کنن.
به گفته او، هوش مصنوعی بیشتر از اینکه باگ‌های کاملاً جدید کشف کنه، باعث شده هکرها بتونن تعداد زیادی ضعف امنیتی شناخته‌شده رو خیلی سریع به همدیگه وصل کنن و ازشون برای نفوذ استفاده کنن. یعنی اگر سازمانی هنوز وصله‌های امنیتی رو نصب نکرده باشه، حالا خیلی راحت‌تر از قبل هدف حمله قرار می‌گیره. هوش مصنوعی لزوماً حمله‌های جدید خلق نکرده، ولی سرعت و مقیاس سوء استفاده از ضعف‌های امنیتی موجود رو چند برابر کرده و همین بزرگترین تهدید امروز امنیت سایبریه. /اکسیوس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/ircfspace/2476" target="_blank">📅 07:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2475">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pOypD16xcNUrRgkQdyQTkufwOzV5WN8ZIGQy6KnTiMhHxJf-ZmX0M1JahPcWJw3I80Vf37b6zuT1DYmPXZ83uiHZtNNd8WsPp812JoNMzsjfiKawBXMqEgO3EtN3mrWjrssnL4_qbbOY_WGU9yMnSt1zzazSASz2kfOe4q5NMbqYItQFlPo92a2xCXd2DuidFB5nLBKtc6bTPvbtDumxaXVvDLw_C0mhYfAVzTcxw-HwlqI_-WO80RSbNDzWxme6ugLAnBgBkXHAaLGCpJgMnrCmAveJlKFFguOXxOBk3oBB84ztCduXPt3UID7B7rwiZTIAyVV2Iymn4cOe_PROPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ GRoute یک کلاینت متن‌باز و رایگان بر پایه هسته ایکس‌ری هست، که امکان استفاده از پروتکل‌هایی مثل VLESS، VMess، Trojan و Shadowsocks رو در کنار ترنسپورت‌های مختلفی مانند REALITY، TLS، WebSocket، gRPC و XHTTP برای دیوایس‌های اندرویدی فراهم می‌کنه.
این برنامه از قابلیت‌هایی مثل اضافه‌کردن کانفیگ وارپ، مدیریت لینک‌های ساب با بروزرسانی خودکار، مسیریابی تفکیکی، پروکسی برای برنامه‌های انتخابی، فرگمنت، Sniffing، نمایش لاگ‌های Xray، اسکنر آیپی تمیز کلودفلر، امکان تست کیفیت اینترنت، بررسی پینگ واقعی، تاریخچه مصرف دیتا و ... برخورداره.
👉
github.com/SuOracle/GRoute/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2475" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2474">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آموزش راه‌اندازی پروکسی تلگرام بر روی سرور شخصی ...
📽
youtu.be/pyvB6VSPhwg?t=176
💡
github.com/SamNet-dev/MTProxyMax
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/ircfspace/2474" target="_blank">📅 08:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2473">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HUCNOYUBCio0VpfXNFxBXpcJAXQXI74svCiPgPKUdmngqSD-KLkfEbFeKR2tJXOaUK0PK9xSL1cqdIB_3VQznxCnRPjyPgb03v3-x4rIF8QLVeUaLafXgV11-I_SxbIyA0s8ZKL1Rrs165nRI1lMKNprrpZjXwEdjtcenJCCjOyb9QMvSq2KnhffdJ_7esrUdzTHIf-ztxHY6cmaunNYdfqFfw5thuk3fSjNHfeYFetCWWD9oF_ghjz4ZAjNTvLFTTKuaPCx6uk8V6M4yAI3_k8Zqn62TMAzapImw7OzlYxVzPaamuu4f2e-JdeLtSHvid876WVotl9Mu0PGHTpJ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر سیمرغ یک ابزار متن‌باز و رایگانه که برای پیدا کردن آیپی‌های تمیز کلودفلر در اندروید و ویندوز ساخته شده. این برنامه میتونه آیپی تکی، رنج‌های CIDR، رنج‌های دستی و لیست‌های آماده ISP رو اسکن کنه و بهترین‌هارو بر اساس سرعت و تأخیر بصورت رتبه‌بندی‌شده برگردونه.
👉
https://github.com/rezakhosh78/SIMORGH-Scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2473" target="_blank">📅 07:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2472">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gb5DkTy8xd-_ObmS9l4Ms-QZ_wQ9Dl7vc0vcG4SG9UcbPsodTXpv8uYylweVX9PgH69GzfRhK4Z4JLUBGs4cemBFEh8VdseGLh597SAj4N_CFsqDy6yu01-H-r5xzN1CO4LZZKo0k6yu3VWgNP3Dqcp5BZ8Ns23l3S1nHyT9ZCUnFN9TJNpNkqF8C959phekx-MjwEI5Mi8-WmaTvPQWJp7vz-qI3cC-dhR1zUR0M-XsS5bGydvJ_z43f4IdC-OHaHDqw_Cwh2sR_Y9TTtpZC0lEfzzT1RaDqeAF19fGBiFcduS29pMuM8PL4k13FKHDpSWJjxGsYaTn9QBIxanORA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر Asha یک اپ متن‌باز و رایگان برای اندرویده، که با تمرکز روی پیدا کردن آیپی‌های تمیز و پایدار کلودفلر ساخته شده و کمک می‌کنه سریعترین و مناسب‌ترین آیپی‌هارو متناسب با شرایط شبکه پیدا کنین.
حالت‌های مختلف اسکن، بررسی لیست دلخواه آیپی، شناسایی دیتاسنترهای قابل دسترس کلودفلر، امکان تست سرعت واقعی از طریق پروکسی و استخراج هوشمند آیپی از وبسایت‌های پشت کلودفلر، از جمله امکانات این اسکنر هستن.
👉
github.com/ashanews9776-eng/asha_scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2472" target="_blank">📅 07:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2471">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نسخه ۱۷ از اپ
#MahsaNG
منتشر شد و توی این نسخه هسته سایفون بصورت ویژه برای شرایط اینترنت ایران بهینه شده. همینطور امکان ساخت، وارد کردن، خروجی گرفتن و اشتراک‌گذاری کانفیگ‌های
psiphon://
هم اضافه شده و یک اسکنر IP جدید برای CDN Fronting طراحی شده تا پیدا کردن آی‌پی‌های مناسب راحت‌تر انجام بشه.
امکانات جدیدی هم به خود برنامه اضافه شده؛ مثل دریافت کانفیگ‌های ایکس‌ری از طریق نوتیفیکیشن گوگل، قابلیت زنجیره کردن دو کانفیگ و حذف کانفیگ‌هایی که موقع تست پینگ توی ساب فعلی پاسخی دریافت نمی‌کنن. رابط کاربری بطور کامل بازطراحی شده و جابجایی بین ساب‌ها با کشیدن صفحه به چپ و راست انجام میشه، مدیریت ساب‌های بزرگ بهتر شده، شماره کانفیگ در حال تست نمایش داده میشه و از این به بعد خود اپ می‌تونه اعلان‌ها، اخبار و بروزرسانی‌های پروژه رو مستقیم به کاربر نمایش بده.
توی این نسخه مشکلات مربوط به اتصال مجدد و کرش سایفون، ایرادهای ویجت، باگ‌های CDN Fronting، کرش نسخه ARMv7، بازیابی نشدن رمز عبور HTTP، وارد کردن لینک ساب در بعضی شرایط و چندین مشکل دیگه هم برطرف شده، تا تجربه استفاده از این فیلترشکن پایدارتر و روان‌تر باشه.
👉
github.com/GFW-knocker/MahsaNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/ircfspace/2471" target="_blank">📅 07:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2470">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یکی از نکات جالب اختلال ادامه‌دار خدمات بانکی اینه که هنوز چک کردن موجودی از اینترنت‌بانک با مشکل مواجهه، ولی پرداخت قسط با قدرت کار میکنه. در کل هرچیزی میخوای از حسابت برداری، به خاطر هک به مشکل خورده، اما هرچیزی میخوای بذاری، میگیره
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/ircfspace/2470" target="_blank">📅 07:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2469">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مخابرات قیمت اینترنت ثابت را سوسکی بیش از ۵۰ درصد افزایش داده و آن را به بدترین شیوه در محدود کردن کاربران و تغییر ویژگی بسته‌ها انجام داده است. مثلا اینترنت ۱۶ مگابیت قیمتش ثابت مانده اما در سرویس سه ماهه، بیش از ۱۰۰ گیگ از ترافیک آن کاسته شده (۳۶۰ گیگ به ۲۵۵ گیگ).
حالا شما اگر بخواهید تقریبا ترافیک همین بسته را که تا ابتدای سال عرضه می شد بگیرید بایستی ۱۰۰ گیگ ترافیک بخرید که قیمت آن بیش از ۲۰۰ هزار تومان است و در واقع همان کلاس ۱۶ مگ سه ماهه با ۳۶۰ گیگ از ۳۰۰ هزار به ۵۰۰ هزار تومان تغییر کرده است. انتخابها هم محدودتره و برای ۱۶ مگ یا همان ۲۵۵ گیگ را باید بگیرید (و بعدا ترافیک جدا بخرید) یا انتخاب دیگر ۸۸۲ گیگ است که قیمتش بیش از ۳ برابر است!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/ircfspace/2469" target="_blank">📅 07:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2468">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oIIJdLHu_iHcEhLW3JMVKFhS0zDtmIdW9ahGSLlHdgzwpogg9bHwwQZFMqO05zI1Yxqrxvhk9wOWserJEV1RxGBeYwxzJYrMO1kmQNcim9MtRZC_EuHuKElPFuwWayPtA-x-pzMZCjVwD5Lsjups-0dTIfnMpB4_c6oWCnIdPzHJSQzh2wDq7Tf88ZndB--H8uPwriZaA3_Ia-d00EJ6sJv18NpW_QwWXETkj7IbeQ4oiDkQ9npP9zaTRzEXf-OdtG0iLKhKWHddc57Nohd3TExvgRh8tT8vCM3clefosytVdM2pJY_D122hpH1T_T8-7cDQfY5F9CUaEMr5U1Q48w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات (که به تازگی بابت عملکرد درخشان وزارتخونه در دوران جنگ ازش تقدیر کردن) گفته "لازم است با وزارت نیرو برای خارج شدن سایت‌های ارتباطی از اولویت قطع برق تفاهم شود".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/ircfspace/2468" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2467">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گزارش تحقیقاتی
HalcyonAi
نشون میده شرکت
ابرناک
(مالک جدید دامین ویکی‌تجربه) مستقر در تهران تحت پوشش یک شرکت آمریکایی به اسم Cloudzy مشغول ارائه زیرساخت فنی به هکرهای حکومتی کره شمالی، چین، روسیه، ایران و چند کشور دیگه‌ست. زیرساخت این شرکت برای ۹۰ روز زیر ذره‌بین کارشناس‌ها میره و مشخص می‌شه نه تنها گروه‌های هکری حکومتی، بلکه گروه‌های باج‌افزاری از جمله شرکت تحریم‌شده اسرائیلی Candiru جزو مشتری‌های این شرکتن و بین ۴۰ تا ۶۰ زیرساخت‌هاش به فعالیت‌های مخرب و مجرمانه سایبری اختصاص داره.
آدرس خارج از ایران این شرکت (که قبلا اسمش Router Hosting بوده) به دو کشور قبرس و آمریکا منتهی میشه. نشانی آمریکا به یک مرکز خرید در ایالت وایومینگ می‌رسه که آدرسش با بیش از دو هزار شرکت دیگه مشترکه. ثبت‌کننده کلادزی در آمریکا شرکتیه به اسم Cloud Peak Law که تخصصش ثبت شرکت ناشناسه.
گزارش تاکید کرده بعیده مدیران کلادزی یا همون ابرناک ندونن که بیش از نیمی از زیرساخت شبکه‌شون داره برای کارهای مجرمانه استفاده میشه. این شرکت در واقع به عنوان command-and-control provider به هکرها فعالیت میکنه و برای استفاده ازش فقط داشتن آدرس ایمیل و رمزارز کافیه. ابرناک در ایران در سال ۹۹ با نام «آلان فن آوری ابری» ثبت شده. دانش بنیانه، بسیار هم فعاله و در حال حاضر ۳۴ فرصت شغلی باز در سایت جابینجا داره. مدیر این شرکت محمد حنان نوذری به رویترز گفته فقط ۲ درصد از زیرساخت‌هاشون در اشغال فعالیت‌های مخربه. همینطور گفته نباید چاقو فروش رو مسئول خلاف مشتری دونست.
دور از انتظار نیست اگر اسم این شرکت و عوامل اصلیش رو توی فهرست تحریم‌های آینده ببینیم. ابرناک حساب‌های توییتر، اینستاگرام و لینکدین خودش رو غیرفعال کرده. نکته آخر اینکه غلامعباس نوذری که در شرکت ابرناک شریک محمد حنان (احتمالا پدرش) هست، دیپلمات ایران در نیوزلند بوده. حنان هم در پروفایل لینکدینش به تحصیلات در نیوزلند و در پروفایل کوچ‌سرفینگ به ۱۵ سال زندگی در این کشور اشاره کرده.
©
arashzd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/ircfspace/2467" target="_blank">📅 08:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2466">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X3inBr35J4jou9SJtbcy39Nxwf3LBqycDgtHpkwVp9UTqYCx7_ZG7Ci3aGvwGs1QOgeJhhUC6-tPqkjNXpk9EMWsLhRZqMqVIJBYhVOFDAyu-Fax8HUgxXeibeaXBPwk00SyKXlaB7SGL1iKBGERLs5M7aJyvNmVRf-Hgty0ArAhShdYq7f_ovzGT58BhPmDOs-DfAcmTwOVDfxD0tztHMAB5OqEjBz-42EAp-88RVti37OGoOMxm-7Xhz0LmTdFPizTSuMpJIIazv_IUx5GSNdCadv7pN3vBmLmMQDeOt6A-ImZsd-qbvz2nBqmo6nv518_S6vIc9CAOlbqKLpyhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران از رتبه‌بندی جهانی اسپیدتست حذف شده. شاید فکر کنید چون دیگه حتی ته جدوله، رتبه بدترین اینترنت هم توصیف مناسبی نیست، یا دیگه زیر ۰ و منفی جوابگو نیست.
نه، چون چیزی که داره ارائه میشه اسمش اینترنت نیست!
👉
speedtest.net/global-index
©
Mehrdadlinux
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2466" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2465">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VdK8PhIDIlCS-9wt0ks-RkQVaNO-MFoezQvendwraFXiDecNrzgNx0YN-hb6doZmGNrbn6ZLh8gDk4gBQs5fSP1Dvc0D1fZWV9tG5Uje_nQoHIefDDdZBiN6Ez8tDQi1zMkE4I2asu4MKgZ5I-_IENHC_2pQs4_CC24taQnqBJ7zP08mKb8RJ0PrhSJviuub0HimOIQvlCvVDxJv1mXguEri1gy0t4hyo_hwEE2Oi0ZWuravj_niASUCJwrWsz-HfRxxGVxBsnKQCNlk5mn8X_VBqsvlvqAq_UMXWEVI_2uJHO1IVkYqZq9RcKW2cQEgDRpToa8jC8ghV-cIQ6gXJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این چندروز احتمالا در مورد اکانت ویکی‌تجربه و سرنوشت نامشخصی که برای مالک ناشناسش رقم خورده چیزهایی شنیده باشین. متاسفانه دامینشون رو در ایام جنگ و قطع سراسری اینترنت نتونستن تمدید کنن. بعدش این دامین توسط ابرناک ثبت شده و با یک پیام مسخره و کینه‌توزانه، صفحات سایت تغییر پیدا کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/ircfspace/2465" target="_blank">📅 08:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2464">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dusARTlkrgr5ulXIth6gOEZwkQkQtY4ViZvZYQdWwuMedMzaPMLycs5YkeuSzjw5zIz4FCaVLqyWsEKPZi52eLxAYdVSqjWe9GAS_vRxp8X9nS2Uh_URdqEtRbXcDulUttQiFtvtNKD27fkm84myDFu3F9ZbVz7yFcoSMBQkAk0BSDrVfmYwBElGPFiRvpUVKbnEi626vaHf5vvOFemp0D5eHBP3FFRwOjEl3nU3-e5MjPJcLknfDE1AXUVFMyLQee-ADtkzUvnzfrx_E-QfDTBBubPAz2r4x78hEdrnWOZFVBfPLoL8sTTopKhVMqAbxndn6U7MA8cOw8GZb9v4LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از
#لینوکس
استفاده می‌کنین، فیلترشکن دیفیکس در جدیدترین بروزرسانی خودش پشتیبانی از این سیستم‌عامل رو اضافه کرده.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2464" target="_blank">📅 12:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2463">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pwsFkWHbPVVVymi77WcwqnZEDbtog52NijI4F2TBYoKDhvzuzBeOFX4Q8OCB3TW5gq8GdQmSUBz7-XK0hI1eriMgD1s-GPUf6d4mJJemmZQ4AfoudjHOMVjU6Gk0dBEuhLhxtxwUYrxYeMZaJP5UcGNYGYEPomW6G9mOoukSWOVDBZBj67ElA_iq901GUJmKwhqGl5LBQhvIFFIaF8amTRKoJYvEPx_NhmelGgw7dmpLdD9wKOCLqI-QubINmLPi-kWEcy6qm9Da4EIO3-T4noB6gtJCkPznJKnAk8olMoiiHnahbgAx9u3aMu8Dfh_z0UoP2Tm-ryz5CAxz5ytflQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ RedCloud VPN یک کلاینت متن‌باز و رایگان برای ویندوز و اندروید هست، که با استفاده از هسته Xray توسعه داده شده و امکان اتصال از طریق کانفیگ‌های VLESS، VMess، Trojan و Shadowsocks رو فراهم می‌کنه.
این برنامه تمام ترافیک دستگاه رو از طریق تانل‌های رمزنگاری‌شده هدایت می‌کنه، از قابلیت اسکن و سنجش همزمان IPهای کلودفلر هنگام اتصال بهره می‌بره و همچنین با استفاده از قابلیت Sniffing، ترافیک HTTP، TLS و QUIC رو شناسایی می‌کنه تا عملکرد اتصال بهبود پیدا کنه.
👉
github.com/Devtahas/RedCloud-windows/releases
👉
github.com/Devtahas/RedCloud-Android/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2463" target="_blank">📅 07:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2462">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بانک ملی از اختلال مجدد در خدمات کارتی خودش واسه ساعت ۲۲ تا ۲۴ روز جمعه خبر داده بود، که گزارش کاربران نشون میده این اختلال در روز شنبه هم همچنان وجود داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2462" target="_blank">📅 07:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2461">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">الان خرید کردن با کارت بانکی مثل دستشویی رفتن شده. اول باید چک کنی آب وصله، بعد کارتو بکنی؛ وگرنه ممکنه گیر کنی.
©
shokhmatic
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/ircfspace/2461" target="_blank">📅 18:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2460">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">در حالی که با اعلام شرکت خدمات انفورماتیک اختلال خدمات کارت محور بانک‌های کشور برطرف شده‌اند، بررسی‌های کاربران نشان می‌دهد که همچنان بخشی از اختلال‌ها در خدمات‌دهی بانک‌ها برجاست. اغلب اختلال‌های موجود در بستر نرم‌افزارها و همراه‌ بانک‌ها برجاست و این موضوع کاربران را در برطرف کردن نیازها روزمره دچار مشکل کرده است. /ایسنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/ircfspace/2460" target="_blank">📅 18:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2459">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fyAuorCdfAjtbUVsLCVGGHoYXsZmRzs-2T8_FXqW8f9A8Fe3xg8F7Hu4ubeMi6LRbjcE0ARWc_KSdeNoj6z8CPmNitMWhiF8Gjk3vRWnLgxbXd29oEhv_tHAhMycy2YNQs_CFfUmbiEXqXhUYbxdVdpsQBEP5XzirOydx4yy9MeB0Ovv0GQNo80HAymhTCOvJaTZ3HLXW7DUc3pfpXKtAbAIYgxYUReno4wyQgyx8hlmipdya2jbTlZQ7HISZ9qyBz7W1zu3i0KLVEMdF6HIEibOq_iH-N-Wy5ABGX0vZwnZ3qPl2l8M4WFy8frE5yKM8TNE5MLkWLiP-sV3S00XIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیسیون اقتصادی مجلس طی نشستی با ستار هاشمی، وزیر ارتباطات و فناوری اطلاعات، از عملکرد این وزارتخانه در دوران جنگ تقدیر کرد. /دیجیاتو
بابت تقدیر یه کاسه دادن دست وزیر قطع‌ارتباطات؛ اما بابت ۸۸ روز
ریدن
به اینترنت باید یه لگن بهش تقدیم میشد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/ircfspace/2459" target="_blank">📅 20:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2458">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است". /iranintl
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/ircfspace/2458" target="_blank">📅 16:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2456">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اختلال خدمات بانک ملی بعد از چندروز نه‌تنها برطرف نشده، بلکه این اختلال فقط محدود به همین بانک نمیشه و خیلی‌هارو گرفتار کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/ircfspace/2456" target="_blank">📅 13:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2455">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">جنگ شد، اینترنت رو بستن، تنگه رو بستن، آتش‌بس شد، توافق کردن، تنگه رو باز کردن، اینترنت رو بصورت تدریجی برگردوندن، گشایش شد، مسابقات جام جهانی سر رسید یا هر نمایش و کوفت دیگه‌ای؛ ۸۸ روز قطع سراسری اینترنت، سرکوب، اعدام، زندان، شکنجه و کشتار ده‌ها هزار نفر معترض دی‌ماه رو به فراموشی نمی‌سپریم.
خون‌هایی که روی این خاک ریخته شد و نسلی که هزینه آزادی رو با جون خودش پرداخت، از حافظه ما حذف نمیشن. بین ما و شما دریایی از خون فاصله هست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/ircfspace/2455" target="_blank">📅 09:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2454">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JcXvyf3jmbDwNajU0u9kt37v0sF66aLlloqcVWN6XlTdth4xHm5l9iWLFJny3fYj3rQ-cetLtCu0T9iK0vYIEIvwwKik0Yac1NyyOrTURF4puZhX7nWXz1jerpM23Z9al0uBeXMKuD0pXw-W9XyYZ3NXZK0RaE1uLKyJ-0myAhU21fVZh34pF1jf9vqe_xXsNARCZrkOB2_4T0Kb61WMiGeJEMLBMhc84MpAPUcjrphgUyDYdJIacUXKVpg7F2V42AQfnAbHZPYBWcdkjbBWFjFdFjacVEElADwGN4hIg5xHpfUD7bzGjQYi7Ur-tGSYV7YMCJ_sVFlF7qVUFkkVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل V2X یک ابزار مدیریت اشتراک سبک و متن‌باز برای VLESS روی WebSocket + TLS هست، که به شما اجازه میده با دیپلوی پروژه روی سرویس‌هایی مثل Render، Railway یا DockFly، برای خودتون و خانوادتون اشتراک اختصاصی با قابلیت بروزرسانی خودکار ایجاد کنین.
این پنل امکاناتی مثل مدیریت کاربران و کانفیگ‌ها، تعیین حجم و تاریخ انقضا، نمایش آمار مصرف، مدیریت IPها، اسکنر داخلی و ارسال گزارش و هشدار به تلگرام رو در اختیار شما قرار میده.
👉
github.com/SulgX/SulgX-Panel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/ircfspace/2454" target="_blank">📅 09:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2453">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FiSfyZWbG0-69f_vOv8HXUdLQ5vpIqhEqXZHEGG1l1vmLCEBcRkWi1_JAJ-3J8d2pJbsoHym3EQ3TCom3q-Q8ZrlLxpHko5dqq6wawoCAWh44l0phy7zo-6SV-XcxFQYWqki1a9YnjevjLxmXKcbWz22LSEgL8Y7M1IhUO46Wceb0jmoWLJnXdUFzhzM-xg9JJ7eURu_4Cm7x6tJbMczPjHtTxM5Mcbiw5VdmBt5VvPs43rZTaQGS5nCtzNHAb1v77rwTah9wAK3UUkZl-cWPdxOxhmEi-4669iemuZp2pwAh1wd99SkGH3PulVCn7pVkak2V09fYlqCA-KubeVTGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از کاربران ایرانی به نام MrArrow دو مشکل مرتبط با فرگمنت در v2rayNG رو برطرف کرده، که از نسخه ۲.۲.۵ به بعد این اپ اندروید در دسترس هستن.
این کاربر توضیح داده که "چون تو شرایط فعلی اینترنت ایران Fragment نوع
tlshello
روی خیلی از اپراتورها دیگه مثل قبل جواب نمیده و بین حالت‌های مختلف،
1-1
معمولاً عملکرد بهتری داره و حتی با مقادیر پایین Length و Interval هم میتونه از فیلترینگ مبتنی بر SNI عبور کنه، یه سری مشکل در برنامه وجود داشت".
مشکل اول این بود که با وجود اینکه هسته Xray از Fragment نوع
1-1
پشتیبانی می‌کرد، اصلاً گزینه‌ای برای انتخابش توی رابط کاربری v2rayNG وجود نداشت. مشکل دوم هم این بود که v2rayNG عملاً فقط
tlshello
رو استفاده می‌کرد. یعنی حتی اگر توی تنظیمات نوع دیگه‌ای از Fragment انتخاب میکردی، موقع اجرای کانفیگ دوباره مقدارش به
tlshello
تغییر می‌کرد و انتخاب کاربر نادیده گرفته میشد.
👉
github.com/2dust/v2rayNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2453" target="_blank">📅 09:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2452">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GwIFFPTr2NBMIxK_CR0FfEXXePfnmXV7mj8oUZRXiBrJXA6x3qIQLPrmW8sacVEZaVm3HwUJAj_Ys7tm5St4z7ZZXV_GYXXWwUz1snr9IZL1igE62iqiOF8Y6a0_YeUIHNEOJ94-vda4WFJNub6fTcJJfkSITHxnz2wX8uqNW05HZ8kwB2-hqtZVHl36AuF2ZR6_uExC8d-e7OcpSdGHG9GHwcOTAqJZ6ykY2mAgEBNqj_pa52jtPslgbRgyGn2nsGrb9shc5cijLgNmskRTtYsBj04WRSCbtYlR90I-F2oeDo08GfbM-1wH1x44dK9qM0WQPS1V2ngA6aIAswsjfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکت اندروید F-Droid (که کاربران میتونن بدون وابستگی به گوگل‌پلی، اپلیکیشن‌های آزاد و متن‌باز رو ازش دریافت و نصب کنن) هشدار داده که گوگل قراره از سپتامبر ۲۰۲۶ قوانین جدیدی رو روی اندروید اعمال کنه.
طبق این ادعا، توسعه‌دهندگان برای اینکه برنامه‌هاشون روی دستگاه‌های اندرویدی قابل نصب باشه باید در گوگل ثبت‌نام کنن، هزینه بپردازن، مدارک هویتی ارائه بدن و اطلاعات مربوط به برنامه‌ها در اختیار گوگل قرار بگیره.
منتقدان میگن این تغییر میتونه نصب برنامه‌های مستقل، پروژه‌های متن‌باز، نرم‌افزارهای شخصی و حتی برنامه‌هایی که خارج از گوگل‌پلی منتشر میشن رو با محدودیت جدی روبرو کنه. به همین دلیل F-Droid و برخی فعالان حوزه آزادی نرم‌افزار معتقدن اندروید بتدریج از یک پلتفرم باز فاصله میگیره و کنترل بیشتری روی اینکه چه نرم‌افزاری روی گوشی کاربران نصب بشه، در اختیار گوگل قرار میگیره. به همین خاطر کمپینی با عنوان Keep Android Open راه افتاده تا کاربران و توسعه‌دهندگان نسبت به این تغییرات آگاه بشن و به اون اعتراض کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/ircfspace/2452" target="_blank">📅 08:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2451">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کاربران میگن "ظاهرا" دسترسی دیتاسنترهای داخلی به اینترنت داره برقرار میشه. فکر کنم هنوز از اون زمانبندی که نامسئولان قطع‌ارتباطات گفته بودن "بازگشت اینترنت درحال تکمیل شدنه" چند دقیقه باقیمونده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2451" target="_blank">📅 08:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2450">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Og1mQ3jwJLqxUwcrCHkQ5clbCVckhOvfxteALxtYSDzZouRaUn82qF_BcoCKEpZHzaUKOlwL2mq9Ltf_0XqoW4kQv7mI0vtw_ZRk-8z9Sqj2baJwy2D0cLhmj5oz7kJxhmSIRwxWISXOWhq_Jgu9nVS6w7dFIF2ySAhBaEHywzdSb-ZHrB68wPNym1enwW078WG62gorR1q_-RZuQODtEioOt-ieKNgkHt2PfA1F54Ft8R64LYNCDRbZE1XyjK9FpsVW8cRFlJsrazsoobN3-wLc2wBcTHmGIW3hM7d8Jzx0wDlyew2RdPOhdwXJ_6FBTAvdCzYmM0W23_eiX0brAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما تنگه را مفت ندادیم، زندگی یک ملت را مفت دادیم. سال‌هاست حرص و ناکارآمدی‌تان را «سیاست‌گذاری» نامیدید، ماشین قراضه را ده برابر فروختید و گفتید حمایت از تولیدملی، اینترنت را خفه کردید و گفتید «مدیریت»، فقر را گردن تحریم انداختید در حالی که رانت و انحصار رگ‌های مردم را بریده بود. جوانی را به مهاجرت، کسب‌وکار را به «تاب‌آوری»، آینده را به سکوت فروختید. اگر چیزی واقعاً مفت رفته، نه تنگه هرمز، نه یک وجب خاک؛ عمر مردم، آرزوهایشان و فردای سوخته‌شان بوده. این صورت‌حساب واقعی است.
©
rassssoo
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2450" target="_blank">📅 08:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2449">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">این اختلال GPS بخصوص در مناطق مرکزی شهر تهران برای چیست؟
داداش طرف اومد نقطه زنی کرد و رفت و تمام شد. الان GPS رو مختل کردید که چی بشه؟ ملت اونجا سرگردون و گم بشن؟
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2449" target="_blank">📅 08:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2448">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fgt1VFtvToh-9UO42ZOUY5l2wygngKQ24ucP7GwUdtlfRF3qPKosRvjeWmr4G-oAyKJc-RbWSkRQtReHknm-jGyGynV-CK_UrY-riGL5tQ1GbUKT7pZBUL3XeIsikV6JupaG4MSnZkZSEaCDKurv8zOMGmSw5IkJwwdFXSDLatRvcAzOdgSwpCDzGScJJyYsT0cfJ-cJXhwE-JhadEpN0_tLJF_k_QbPADK3jd7awMqrxIevKR7x-SuCamPet2oH-lW2XR7uZ8OQ7f75qfi-7tiqkXt02kdyxvRda27ofpa70wajFsUzAjiCyKNAeUHfF2ELlGL2nnPjYj09Wv_lgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه CandyTunnel یک ابزار متن‌باز و رایگان برای ایجاد تانل روی سرورهای لینوکسی هست، که با استفاده از تکنیک‌هایی مثل تغییر و پنهان‌سازی آدرس IP، رمزنگاری ترافیک، بازیابی بسته‌های ازدست‌رفته و روش‌های مختلف عبور از فیلترینگ، تلاش می‌کنه ارتباط کاربران رو شبیه ترافیک عادی شبکه جلوه بده.
این ابزار از پروتکل‌های انتقال مختلفی مثل UDP، ICMP، Proto58، TCP، QUIC، IPIP و GRE پشتیبانی می‌کنه.
👉
github.com/AmiRCandy/CandyTunnel/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2448" target="_blank">📅 08:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2447">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d3eIQYWq2kiJXKMe_8et-uBJXyHIUtGZVekVHQ-ku8LRLe6F5tks9Q7dtbLBMvtehzcJkdqsJcYeqPSt9AXm7GfeQkFw7O8hPtJ9eeVzGo77RozGreDTKRSgY96CBh523F-2hrIxnbNgVCKOnhdOmR78lPTVdEzVnv-g33AAwyNTysR0KXhJCGQwcijZFqJZA4Frpu7uNKWfFIlZoI9L8UaUwOpW7de5u24963jFCUuepwOQW0MQmnO1jk2ZswcIBcLt0Cp8M-XHrxpFCRyYYv0dvTGhRMOXl9HdRj-3hU0x6UF0-UECVWlnEUM4tmRIsTNZAl_wVP-xTiJ1DoKRow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار Config Converter یک وب‌اپلیکیشن متن‌باز هست، که ۳ ابزار پرکاربرد مبدل V2Ray، مبدل WireGuard و مبدل Clash/Sing-box رو در یک محیط یکپارچه گردآوری کرده.
این ابزار امکان دریافت مستقیم کانفیگ‌ها از لینک‌های سابسکریپشن رو فراهم می‌کنه و ورودی‌های Raw، Base64 و JSON رو با تشخیص خودکار فرمت، پشتیبانی کرده. همینطور کاربران میتونن بصورت گروهی آی‌پی، دامنه یا پورت تمامی کانفیگ‌هارو ویرایش بزنن.
👉
darknessshade.github.io/Config-Converter
💡
github.com/DarknessShade/Config-Converter
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2447" target="_blank">📅 08:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2446">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QiWmNAyis6G4sRYRxRJzKn-auk_WqjMJ9Z4WEwt208k0zjc3-LePtIab_789v4yb7HnavOIvvnl3cghTK3TH-F4nTyNu8-I_9F7gh-ficyY3nnYYiGgUndIlIfcMTso-La2X3cAhQ7MZPf07otCSSvzFUWzZaxmcwZIJrH1bTxWYEGfBsovJ7LOGAY-tVdcCPctqzopY4h7RREFgtB9zx4Rx_zTCInrAmzj4i5jd6Q7x4RaR9K9U0AZw9ZyiiKEcU7icrLYT13MkWf33kKYqhNwtZj1Pa-wVFWShVWWAnXw3qLFFxYctsMAZQ4ACxZ4trAC5TPT-GpPS6CV2ZEtFcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان بازرسی کل کشور از توقف اینترنت پرو خبر داده و گفته اپراتورها اقدام به ثبت‌نام گروه‌هایی از جمله وکلا، مدیران و اعضای هیئت‌مدیره شرکت‌ها برای دریافت اینترنت با شرایط ویژه کرده بودند. در اجرای این طرح، هماهنگی‌های لازم با رگولاتوری و وزارت ارتباطات به‌طور کامل انجام نشده یا در برخی موارد محل اختلاف بوده. بنابراین مقرر شده از ادامه اجرای بخش‌های دارای اشکال جلوگیری بشه و مبالغ اضافی دریافت‌شده از مردم رو بهشون برگردونن. /فارس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/ircfspace/2446" target="_blank">📅 18:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2445">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dQqmgdTXAO9DBwOieLR8OYC_YPpopXQmI4L8pgqtvf6Gtj5Y1DZfbeB1lIjbuOejH2a01we5lEhyykl1vIUI9KIhB0hRroLa49IjsSGyc9SrX3h9iBRBRXUitzhcrQofQwSHZjI5AG9vom6UMxXwpzq0Uxx60orBUhECfmCWb5S1V68U_ZvMe7kB4NaNFldmNbADL3jDse8sOz9WQOXJSLoc9Clh_nFvx19-IYgu_WC9EJBl638u6XmcBbd6Yq7A_0Z4VewgrkGYT0QDSxmGGXaoPPuE6EwhEA5_QEOqdxrrGUCrwJhSo1rv09oEIzYtYic0_zieaa_YGMnVERijUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه NipoVPN یه ابزار پروکسی سبک و قدرتمنده که درخواست‌های واقعی HTTP رو بین ترافیک عادی وب مخفی می‌کنه. این پروژه با معماری Agent-Server کار می‌کنه؛ یعنی برای استفاده ازش، اول باید هسته رو روی یه سرور راه‌اندازی کنین و بعد کلاینت‌ها به اون وصل بشن. در حال حاضر هم کلاینت رسمی اندرویدش به‌صورت متن‌باز و رایگان منتشر شده.
👉
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/ircfspace/2445" target="_blank">📅 08:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2444">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/npznqvpzVCfhOQE7NL54bbPGyF7hObui3Pxw2pnOJcPTLfdMc-cyyugnzoPJ22Vcahhtfn0yVIufkjnXMrUUmOUFmqLpqvc__HxWnMv604LBEkrp_0kjfsg0QVCMBdEuom3GKjOdNKNqN5HCCqiwVIFgD8On0SBJesO8lhcjaJ3xR_2NNcKTP0OE6p7QJtBWy7bwCPaqFTT_cBIsxcM86HQKgiVRkLoZw_TQCUMNEU2MICwARqaRqTtEKI9PvVtSmafR9hdZN7COleeVKnfcyYyWBF00BcujDRbvBMMKUXaCEgPS8zTcZvbW4QMY9YjOarkETjSTmzOl6eATU5ktSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ InviZible Pro در بروزرسانی‌های اخیر نسخه بتا، با اضافه کردن Tor Snowflake و پشتیبانی از پل‌های DNSTT، قابلیت‌های ضد سانسور خودش رو برای عبور از محدودیت‌های اینترنت گسترش داده ...
👉
github.com/Gedsh/InviZible/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/ircfspace/2444" target="_blank">📅 08:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2443">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پاول دورف، مدیرعامل تلگرام در واکنش به محدودسازی استفاده از شبکه‌های اجتماعی برای افراد زیر ۱۶ سال در بریتانیا گفته: این ممنوعیت فقط اونهارو بیشتر در معرض خطر قرار میده و کودکان به استفاده از VPNها روی میارن، که در نتیجه به محتوای غیرقانونی و به‌مراتب خطرناک‌تری دسترسی پیدا می‌کنن. برای مثال هم به استفاده بالای فیلترشکن در روسیه و ایران اشاره کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/ircfspace/2443" target="_blank">📅 08:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2442">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">از میان ۴ بانکی که اختلال برایشان پیش آمده، ۳ بانک در بستر ایران‌اکسس فعالیت می‌کنند و دسترسی مستقیم به اینترنت ندارند. یعنی هیچ ارتباطی بین آن اختلال‌ها و وصل شدن اینترنت نیست.
©
emirhussein_rz
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2442" target="_blank">📅 08:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2441">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R_3E9LpKfzv23vJtL7iNnRXtJerwsYXVyH-Lz4x8QylEn_WaibqRakgOJGQ2X-zo1LPr5V44n0ko155ezIz5QpVaPKq7tbTF7-IrP2vOvjZlvREqChN8Mgm7vdTdeGofKpBxjTWgikGdbbdPu4qFqq_Zi7uaE6H9wV-HWorZw63eXr26L0wK9DRpaARZfRX5y3uDbqGEPw0jhJBncO2jBqLTBXOwCr0QSa0SfrfQBkTKCgvQri03DyV6pIi5Ok8B3iZg6Rgvvym88RlHn-zUIK1_Ae_CMn7y3IcErYY5sHpD1wM8KTiyku6gXQ9r313r0Lq77xLPFilZbK5iIry4Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویروس زارع‌پور به هندوستان رسید؟
دولت هند اعلام کرد که دسترسی به تلگرام رو در هند تا اول تیر مسدود کرده، چون از این پلتفرم برای کلاهبرداری از داوطلبان شرکت‌کننده در آزمون ورودی پزشکی استفاده شده. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2441" target="_blank">📅 08:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2440">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XpbYD27u2kDfQHNGEMW-2QCBaCzpJNCBtZiNTKymHDVKizzOD05ndS8HRg8T4eg8qzVh1Xp3GmubFgOCPGI8tz6Tgs5Y-W42OMFK45DtEElncnPokkFninaIl4c-goU9R4hiyl2QcMzj5IMPRBeGS4zNKFs5VmKz2qCj-0Qdv6L8sZMtuqll5hwedG3t4DRcfxjkTYTIzQSgG6psYlGbdrUdrTX3DtzWpUnwtARZZussMN-Ogho0YboGI5wJX1ZDutmToZ1geLcChZzpn1B95FP3PaiemJ5gor-YN4_3Tkq6bN2j-iSf_X8ykhLu9xH1-cbtcd7-pIJVNqmDYBcivA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ سیمرغ یک کلاینت VPN متن‌باز و رایگان برای اندروید هست، که با پشتیبانی از کانفیگ‌های XRAY، پروفایل‌های NipoVPN و موتور اختصاصی MSP، تلاش می‌کنه بهترین مسیر اتصال رو با کمترین پیچیدگی در اختیار کاربر قرار بده.
اسکن هوشمند آیپی، انتخاب خودکار کانفیگ سالم، پشتیبانی از کانفیگ‌های ServerLess، پروکسی محلی، ذخیره IPهای تمیز، بررسی سلامت کانفیگ‌ها و ... از جمله امکانات این برنامه هستند.
👉
github.com/rezakhosh78/SIMORGH/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/ircfspace/2440" target="_blank">📅 20:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2439">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">با وجود ادعای رفع مشکل قطعی و اختلال در خدمات ۴ بانک بزرگ دولتی، این اختلال‌ها برای سومین روز متوالی ادامه دارد. نیما اکبرپور، کارشناس فناوری، معتقد است طولانی شدن روند بازیابی، نشان‌دهنده ناکارآمدی سامانه‌های پشتیبان است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/ircfspace/2439" target="_blank">📅 19:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2438">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/672c6641f0.mp4?token=muB6E4-ZDRpq-HWNSe0NBsy2TcPyY0SD6sENhw9rGRzAHRx58WBURwby63L6V7UISGX6WzN3ewxpMDRGj56Cfrb_Z62vkJbrcQKPzu18xIIe5LIlwZfUP7VYsXOMghfqFSz3FaiuUWf0gOEidwCJpkLMXnq5WltbCS6e0JCYoaogXyJmPmeHDiOctrdR8ASp-6ZUwLpgUTVajjJk3nY42H1BkaFoNBgdcTGsJWi4ppZDG1HUssiLX_GbtcAoL73bHCnoPVT3U6jgIU-yg6LoN9-Z3B_EZX0KHAhxFOlx-z1aWubTX6Ec76llg5s6yV2DP9ggh78lYRx9-dbYdar0hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/672c6641f0.mp4?token=muB6E4-ZDRpq-HWNSe0NBsy2TcPyY0SD6sENhw9rGRzAHRx58WBURwby63L6V7UISGX6WzN3ewxpMDRGj56Cfrb_Z62vkJbrcQKPzu18xIIe5LIlwZfUP7VYsXOMghfqFSz3FaiuUWf0gOEidwCJpkLMXnq5WltbCS6e0JCYoaogXyJmPmeHDiOctrdR8ASp-6ZUwLpgUTVajjJk3nY42H1BkaFoNBgdcTGsJWi4ppZDG1HUssiLX_GbtcAoL73bHCnoPVT3U6jgIU-yg6LoN9-Z3B_EZX0KHAhxFOlx-z1aWubTX6Ec76llg5s6yV2DP9ggh78lYRx9-dbYdar0hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانفینگ
😄
©
miladiels
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/ircfspace/2438" target="_blank">📅 19:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2437">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">در پی تجمع مخالفان توافق ایران و آمریکا، خبرهایی از اختلال در
#ملانت
و پیامرسان‌های رانتی منتشر شد. خواهشاً اینترانت ملی رو قطع نکنین؛ عده‌ای اگر مدت کوتاهی از پروپاگاندا و خوراک تبلیغاتی حکومت محروم بشن، ممکنه ناخواسته شروع کنن به فکر کردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/ircfspace/2437" target="_blank">📅 08:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2436">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فاجعه یعنی اینکه اول حمله سایبری رو تکذیب کردن، اما بعدش بصورت رسمی تایید شد. الانم نشت اطلاعات مشتریان رو تکذیب کردن، احتمالا چون قبلا هرچی بوده و نبوده پابلیک شده!
شورای هماهنگی بانک‌های دولتی، اعلام کرد: به پیرو اختلال پیش‌آمده در سامانه‌های ۴ بانک ملی، تجارت، صادرات و توسعه صادرات، تیم‌های فنی بلافاصله پس از شناسایی نشانه‌های غیرعادی، اقدامات پیشگیرانه و حفاظتی لازم را برای صیانت از داده‌های مشتریان و زیرساخت‌های بانکی کشور به اجرا گذاشتند. بررسی‌ها نشان می‌دهد حمله سایبری محدود به چهار بانک بوده و هیچ نشت اطلاعاتی رخ نداده است./ انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/ircfspace/2436" target="_blank">📅 23:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2435">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ایرانسل و همراه‌اول با گذاشتن ضریب روی بسته‌های بین‌الملل قشنگ
عَنِ
دزدی رو در آوردن. گِل بگیرن در اون وزارت ارتباطات و سازمان حمایت از مصرف‌کننده رو، که دزدی اینقدر راحت و علنی شده. البته چیز دیگه‌ای هم نباید انتظار داشت، یه مشت دزد دور هم جمع شدین!
©
Mohsen_935
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/ircfspace/2435" target="_blank">📅 17:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2434">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ju1lyEE4ApLkOSoX_FAOEKYACFQNkp5nSQk3nAi9GM9uLPegVAsR4BgbnpCh5wZDNfXEiLwwMV95U0Y5xNLWeC_qlooUKIylzq8ScuyMS20JXn0pdTHfoN3vXVHJEdmUNvGwYYb4XLpp_tnD_t1BhLAksaOUMNXnWPguj7c-6b-B8hCOVOfJ6xFNCfkUGgZKzBBZQFzPHCxEe65m2hxmp0fSTHAaZf_r5OPaiqXzw2DeiGD9vGoxzAYTEXn2FnbItw6tD6a9BSSaPGc2BEPYsT0S-hS26UdLu_XnxXIDwX0GW2wg3k0bQ521fOfZ3ozx4AMDbJRdAtl1YFR4-GL4wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به دنبال بروز مشکل در ارائه خدمات بانک‌های ملی، صادرات، تجارت و توسعه صادرات از صبح امروز، پیگیری‌ها نشان می‌دهد عامل اختلال بروز مشکلات زیرساختی در شرکت ملی خدمات انفورماتیک بوده و ارتباطی با حمله سایبری ندارد.
البته تاکنون زمان دقیقی برای رفع کامل اختلال اعلام نشده است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/ircfspace/2434" target="_blank">📅 17:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2433">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IFyawuYKp-z58W5ZdQ6-IuU92mYllupoRghX4wM_ZDQhTY8CQjJ5yPbNViaUmVU_X41eRmGKJJtlt9OyJX7pIdvW9VClbkM9aeVduKs-JTzsOidZxhgyshTaJqgCHWvhh3r9mhuEgdQvFDHz1mPJ27mHb-HzC9-x5qmFzUym0HSoDIZFhVADTO0gIVR4YK_RDdvdzMjVw8h5tig5OWHWU3Pbjl8QJyDBLRNP3f-WqMQfWe-K6Ie49D6CsOHkHGZDEuL7IetcTEvCQwA3Oiwok6oeODnBi3EDNdnsWAd8uZkD-IyjJXbZjOnEchoPOdHnsSca_yGD9i834nTLYo7V3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اعلام کرد پس از دریافت گزارشی درباره فعالیت ده‌ها کانال یوتیوب مرتبط با اشخاص و نهادهای تحریم‌شده ایرانی، علیه برخی از حساب‌های ناقض سیاست‌های خود اقدام اجرایی انجام داده است. این شرکت جزئیاتی درباره تعداد کانال‌های مشمول این اقدام یا نوع محدودیت اعمال‌شده منتشر نکرده است. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/ircfspace/2433" target="_blank">📅 17:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2432">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jLo-BQI4CpfiSEBtBcmAWB47sV1wIpAlZwXgjGk9AybsWW_D2RxcumwdbUXbRayOnYSO2aHkkKoAq3wB3Jioot-IbYdYHP4kFBzaAJYtWpNvqyToEy2MLJtm5PPBvfIoBADijvVlXMXrLHIsT9yAukIhIKXYbCFnYZXc_e7sH6OttcaARXSkGgDezf_UzlwoQfXvrvblajBoPnIqrGVJjKlfoi3qaJeVLPM9_bkXwbXaf00WXTRUqSsTDIraNd4Yd7mgBXjHdK6GlpwLk-Ak2K0F4fcz7t4m6mf5mGO4xLhQLCAMGiYvFZU4NkQzmRbTG7LnxOooK7j91PbfkxJ1SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستار هاشمی، وزیر قطع‌ارتباطات اعلام کرد پیش از بازگشایی اینترنت حجم ترافیک استارلینک با کل ترافیک اینترنت کشور برابری می‌کرد. او همچنین طرح وایت‌لیست اینترنت را برای جمعیت ۹۰ میلیونی ایران غیرعملی و غیرقابل اجرا دانست و گفت به آنکه ایده‌اش را مطرح کرده بود گفتم ماستت را بخور. /یورونیوز
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/ircfspace/2432" target="_blank">📅 08:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2430">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B5L1Nhsupj128GWSAb5RdCvXiYa_Ol122-HuwEtLLsmu_ajlAQgSHmmJ2iKO9KtiXAmnslw--tmTHHhnSPKzoXA7xAtuVzwAB5P2PNmVfFwL2f5PO1bTkPjzAo3Y06tp3Cy5_cxZ8pid1LPpiYLuVkT1aQu3PDDAOE9ZYYkLU0m6P9oGS1TI0qk07_N_1c1Uj3KJ38njeoIQK13gJNcM5wd9ENR-rK0Nxx0C99iRB_2bsFM0eAioG77DZr5Nr_viuVNe0J6EWWp88zgZZQsvtxgafcBwyPuXUxpk4s5sPMcsCRkuVPdTMxcDvyVaxUzVgwITLT_BNU-BfWur67rmhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌دنبال توافق‌نامه‌ای که در اردیبهشت میان شرکت ارتباطات زیرساخت ایران و آذربایجان برای توسعه ترانزیت داده و زیرساخت ارتباطی به امضا رسید، بخشی از داده‌های ترافیک اینترنت ایران به اپراتور Delta Telecom در آذربایجان منتقل شد.
داده‌های موجود نشان می‌دهد که آذربایجان در مدتی کوتاه از رده چهل‌وچهارم مصرف ChatGPT در جهان به رده سوم رسیده، که انتقال ترافیک اینترنت ایران از مسیر یک اپراتور آذربایجانی این اتفاق را رقم زده است. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/ircfspace/2430" target="_blank">📅 07:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2429">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور گفته "نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه".
از اونجایی که دولت کلاً هیچ‌کاره هست، نگرانیم بیشتر شد!
😒
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/ircfspace/2429" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2428">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a9WDQ8871KZtWGpK6bGh2yWUvyFGbyJg-g46jog5iWkw5rNIPj2gP7ymIWKzw_xYgEVZbiESIpDTK-gPJbmLcE5OmrevjxStqjSC1GCO1YuOxhgJ4-V3eh7-QzJrI4-0pBLO9WvLd4kPlczzfyNlGPY5tz-ZVA5AP8S4Go9gJ5ry7f69mzkDI-7caYuijlLjo7AboyW_ovcMWmk8dODQVwS3mHPnADIEk3HxAb4il9ihqI5cot2ldR4nmBGth5Oi3eIbn5oUTT8tVrB6Cb4CboAZBeXjg2vNPd_qQqCafx_v5134pfwKWiwCMKherdg3EwDcuHzfAlqT3hb-X5_ZJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آپدیت جدید از فیلترشکن متن‌باز و رایگان pyWarp که برای ویندوز، لینوکس و مک ارائه شده، ۹ مسیر اتصال به وارپ (با انتخاب گزینه Auto در Protocol) چک میشه و در نهایت اگر اتصال امکان‌پذیر باشه، بهترین رو انتخاب میکنه.
👉
github.com/saeedmasoudie/pywarp/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/ircfspace/2428" target="_blank">📅 08:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2427">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">هنوز موشک‌ها توی آسمونن و به زمین اصابت نکردن، پهنای باند رو کاهش دادن و گزارش کاربران از کندی اینترنت و افزایش اختلال‌ها حکایت داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/ircfspace/2427" target="_blank">📅 23:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2426">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بعد از ۸۸ روز قطع سراسری اینترنت و برگشتن دسترسی‌ها، هنوز اوضاع اینترنت به قبل از دی‌ماه برنگشته که دوباره دارن واسه همدیگه خط و نشون می‌کشن. انگار باید خودمون رو برای یه قطع سراسری دیگه آماده کنیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/ircfspace/2426" target="_blank">📅 20:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2425">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SYOYcvyvXZusRYj1iAZAn1ABhR219EXdm-jN8w2Stal9AqOPtqPnOtLJqp8crbDlKxzgG5CnKSjOxrkgCny5cFTjHc_SUKBx67ueAidrk1CeLCo2c3kjuuvfKxLgCsfhbNoAxSexyiZhD982vGPvJjDM_Jhg9GcFU4-m4BrYDRBggW0NDHlDPe4g9KJ_003GsUuWlRg2it219MqQMDtyBfx2_Ez6bhPu5WIfJdy0Mhtfvy1O9ve0YLr4gZIZ6yoBzDXGe6LwZ1YkdUqqBs6j76ypsoLlwtk2bUjZmIn1MkKQhSg7wjj23brkDZ7SYUDPLO62TqxW92xgdOqCo3vkLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه
#نهان
یک راهکار متن‌باز مبتنی بر Workers کلودفلر هست، که امکان راه‌اندازی کانفیگ رایگان Vless و Trojan رو بدون نیاز به سرور مجازی فراهم می‌کنه. این اسکریپت از داشبورد مدیریتی، امکان پشتیبانی از چند کاربر، ربات تلگرام، قابلیت مخفی‌سازی ترافیک و قابلیت تغییر آیپی تمیز از داخل پنل برخورداره.
👉
github.com/itsyebekhe/nahan/blob/main/README_FA.md
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/ircfspace/2425" target="_blank">📅 08:01 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

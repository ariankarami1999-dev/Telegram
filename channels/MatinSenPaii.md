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
<img src="https://cdn1.telesco.pe/file/Hz4oJlR8e3gmp7oYoJdjv-6DbveYqoewpENbCoNg4hevBWFrllOMR9NfVFJEC6eLPztRyTsrPLurr7cmHADis55CPSOgSjkrKCX4OlqzBjCMA_YnQVBq6w4mu0mA6WlgAdIVLY1kdSdDiBY2u_Xaj1E_knoCMPoiJMICsMisP-QnZHYn_eS6phbKMITtXckMYKYIceSWTiE1ACrIFBni3FxtNePDY-pSmWd59XUcjCPGXBmOFE7d3Oo52ymbXAsGQjZle7-UZW5FMLor_HAGVLKVVnqwEVC1RH7rEH-Hs3BYKmaAketkBFYz7nL9rvOmGh8Y9FAsKyDVIH4HKiyN5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 161K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 13:44:06</div>
<hr>

<div class="tg-post" id="msg-3946">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">✍️
دوستان برای جلوگیری از هرگونه سردرگمی، ما در حال حاضر سه اپلیکیشن مختلف داریم:
🛡
۱. WhiteDNS Application
این اپلیکیشن بر پایه‌ی MasterDNS ساخته شده و مخصوص زمان‌هایی است که فیلترینگ و اختلالات اینترنت خیلی شدید می‌شود.
در شرایط عادی فعلاً کاربرد خاصی برای استفاده روزمره ندارد.
🛡
۲. WhiteDNS VPN
این یک اپلیکیشن ساده‌ی VPN برای کاربران اندروید است.
اگر فقط می‌خواهید راحت وصل شوید، این گزینه برای شماست.
🛡
۳. WhiteDNS BPB
این اپلیکیشن برای ساخت و راه‌اندازی BPB روی گوشی اندروید است.
یعنی بیشتر برای کسانی است که می‌خواهند خودشان یک پنل BPB بسازند و مدیریت کنند.
🛡
۴. WhiteDNS Installer Bot
آیدی بات:
@WhiteDNS_installer_bot
در این بات می‌توانید کارهای زیر را انجام دهید:
• نصب MasterDNS Server
• دریافت لیست IPهای سفید Cloudflare
• دریافت کانفیگ رایگان VLESS
• تبدیل کانفیگ‌های خودتان به کانفیگ‌هایی که پشت IPهای سفید Cloudflare قرار می‌گیرند
🛡
۵. WhiteDNS Installer Wizard
لینک گیت‌هاب:
https://github.com/iampedii/WhiteDNS-Wizard
این ابزار برای کانفیگ خودکار سرور شخصی شما استفاده می‌شود.
با استفاده از آن می‌توانید سرور خودتان را همراه با پنل شخصی 3X-UI راه‌اندازی و تنظیم کنید.
❤️
یک نکته مهم:
اینکه اسم برند ما WhiteDNS است، به این معنی نیست که همه‌ی سرویس‌ها و اپلیکیشن‌هایی که می‌سازیم حتماً بر پایه DNS هستند.
ما از اسم WhiteDNS به عنوان نام برند استفاده می‌کنیم، اما راهکارهایی که ارائه می‌دهیم می‌توانند VPN، BPB، MasterDNS یا تکنولوژی‌های دیگر باشند.
@WhiteDNS
🌎</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/MatinSenPaii/3946" target="_blank">📅 12:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3944">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i7B5u3k5yLazl6UHWvufDblX7FPmxLeXYMbrfLWOQgv4s6ZOZF7wO0gG-PgDVto8ngrpqUtz6fsYglZ0Lkf0IhWznewqArxsuk6g12p3BJrR0vFTnyKCZOhpmq9ut6GorLoRHJx-WiQBgrZyGvx0slDfIXo-VNUnfAljdSmmY27JY2YW_oG1R1K_LikwK2cIqUQDFRrvDDpV9a6WqtBeiWwL-TlYbdZn-CXc8h7Bo5LGl9DSHJ6HRlY-BNwzzyVYWm9tpEiF7FO_Uy-w8cquOQUfsQKF980d-7I5BlIb2o9J2nmWev-98a_TNzB1qfTZPRn2hL3JV9NIzDgUognA_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kzsyoRBbNnweKvyD-ibxV3RfbIHPWiAdZiJoqpANnr7yJC_rcGnWzD-WmEL2XwioU40JV3YgNMRzBbTi9QSHmtVHA4Ak2wgiF_rpg0WW3uGEZKGO_pdbxlA8py61RLyhwQnHsnExKr8DcOmo_qXXtPdEPQPT_XTvqq1ZVsm5nvMKxVeXy_O3xeIftqkIs3ZNqKUkM4gOxHHYHNV43ejFL6_5rtoWKmr62E1L-lZMtiI5nVORtRwI1LDaj9QAy95yJPIyF3ionnWdV20_xfGrcg9DMq4ast19sMppws6O2txaasoKmFGyYSoQlrsImDWPn-E_uVnVd8qtrYZAEQ91yA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی از بچه‌ها اینو واسم فرستاد و گفت گویا V2box، به صورت آزمایشی SNI-Spoof آورده. یه تست بکنید ببینم داستان چیه:)</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/3944" target="_blank">📅 00:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3943">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">دوستان عزیز
❤️
در چند روز گذشته متوجه شدیم که بعضی افراد و کانال‌ها، به جای همکاری و ساختن، مسیر تخریب و سوءاستفاده را انتخاب کرده‌اند.
این افراد که ظاهراً در فضای اینترنت آزاد و کانال‌های مشابه فعالیت می‌کنند، برای جذب مخاطب بیشتر حاضرند هر کاری انجام دهند؛ حتی اگر نتیجه‌ی کارشان آسیب‌زدن به پروژه‌هایی باشد که با زحمت و هدف کمک به کاربران ساخته شده‌اند.
چند روز پیش اپلیکیشن WhiteDNS VPN را معرفی کردیم؛ اپلیکیشنی که هدفش این است کاربران بدون نیاز به تنظیمات پیچیده، فقط با زدن یک دکمه به بهترین کانفیگ‌های آماده و تست‌شده‌ی ما وصل شوند.
اما متأسفانه برخی کانال‌ها شروع کرده‌اند به استخراج کانفیگ‌های داخل اپلیکیشن و انتشار آن‌ها خارج از برنامه.
دوست عزیز، اگر مسئله فقط بستن مسیر دسترسی شما بود، ما ده‌ها راه برای رمزنگاری، تغییر مدل درخواست‌ها و محدود کردن این رفتارها بلد بودیم. اما شرایط اینترنت آزاد و محدودیت‌هایی که کاربران با آن درگیرند باعث شده ما تا حد ممکن ساده، باز و قابل استفاده طراحی کنیم.
مشکل اینجاست که همین رفتارهای مخرب در گذشته به پروژه‌های خوب و ارزشمندی مثل Slipnet ضربه زد. وقتی هر ابزار مفیدی به جای حمایت، هدف استخراج، کپی و سوءاستفاده قرار بگیرد، در نهایت انگیزه و امکان ادامه دادن از بین می‌رود.
واقعاً هدف چیست؟ آن کانفیگی که با زحمت استخراج می‌کنید، همان چیزی است که بخش زیادی از آن در لینک‌های ساب ما هم وجود دارد. چیزی که روزانه هزاران نفر را متصل نگه می‌دارد فقط یک لیست کانفیگ نیست؛ پشت آن اسکنرها، تست سرعت، بررسی مداوم، فیلتر کردن کانفیگ‌های خراب و یک سیستم کامل قرار دارد.
ما این ابزارها را در مدت کوتاهی، با انرژی و فشار زیاد ساختیم تا به کاربران کمک کنیم. لطفاً به جای تخریب، کپی‌برداری و گرفتن انگیزه‌ی تیم، سازنده باشید.
ما از نقد، همکاری و حتی پیشنهادهای جدی استقبال می‌کنیم؛ اما سوءاستفاده از ابزارهایی که برای کمک عمومی ساخته شده‌اند، نه کمکی به اینترنت آزاد می‌کند و نه به کاربران.
اجازه بدهید این مسیر ادامه پیدا کند.
✍️
@WhiteDNS</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/3943" target="_blank">📅 23:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3942">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">این پست سگاروی عزیز رو بخونید، و اگر دوست داشتید همکاری کنید:
https://t.me/AiSegaro/120</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/3942" target="_blank">📅 18:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3941">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-text">تیم داشته باشم، دوست دارم از خودِ شما کمک بگیرم. اگر دانشجو یا دانش‌آموز هستید و مهارت ترجمه دارید، این می‌تواند یک
کار نیمه‌وقت منعطف
برای شما باشد تا در ازای کمک به ترجمه و ادیت، درآمد کسب کنید. آیا این مدل همکاری برایتان جذاب است؟
هدف من این است:
سریع‌تر به محتوای آموزشی مورد نظرتان برسید.
هزینه‌ها برای هر نفر ناچیز باشد (پول یک قهوه!).
بالاترین کیفیتِ ممکن (ترجمه انسانی) را تحویل بگیرید.
یک زنجیره همکاری برای دوستانی که دنبال کار نیمه‌وقت هستند ایجاد کنیم.
هر پیشنهادی در مورد نحوه قیمت‌گذاری، فرمت‌ها و اجرای بهتر دارید، در کامنت‌ها بنویسید.
من تک‌تک نظرات شما را می‌خوانم تا بهترین مدل را برای شروع استارت بزنیم.
این فرصتی است که با هم یک کتابخانه آموزشیِ قدرتمند بسازیم!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/3941" target="_blank">📅 18:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3940">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1scCm01Gi1tbRfNWw17Q82538al6xvdDIUiBMAxXnFCndfBGPJwuqoihYeXhEfcOROWGjaGgPCZavRXtL3YZ4Los7H0WLsKPOoMn4GozjzT62Kg8_8h-e_zuVobpPy9LkY-mp_GkSu3NxKAFxyKHe5Fpnp0r-3WanjkQxgeqflPmKepYFGNymrSmEGUJu8I2e88pAWSx_KG8Oq6cV-_zRZJPFpc5ZBu4eW-zlyJ8_MPj8XpoCJWJkyoZjZRh667MZ8YKfdFvU4bOagVX_51-qFFSn1-Y1ojl-BwutOUSB66_t8Qb4YeGGUAOyoiWa4SeL2V7WJxnVIiX9zOsopIHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به همگی، یک پیشنهاد ویژه برای دسترسی بهتر به محتوای آموزشی!
همان‌طور که می‌دانید، درخواست برای ترجمه و زیرنویس کردن ویدیوهای یوتیوب، یودمی و کورسرا زیاد است. از آنجایی که کیفیت و دقت برای من خط قرمز است، فرآیند آماده‌سازی ویدیوها (ساخت زیرنویس، ترجمه دقیق و ادیت) بسیار زمان‌بر است.
برای حل این چالش، قصد دارم یک
«کانال مستقل»
برای مدیریت درخواست‌های شما راه‌اندازی کنم تا با مدل
«مشارکت جمعی» (Crowdfunding)
، ویدیوها را به صورت عمومی و با کیفیت بالا آماده کنیم. در این مدل، به جای اینکه یک نفر هزینه کامل را بدهد، با مشارکت چند نفر، ویدیو برای همه آزاد می‌شود.
اما قبل از شروع، می‌خواهم «شما» تصمیم‌گیرنده باشید.
برای اینکه این سیستم عادلانه و دقیق باشد، دوست دارم در مورد جزئیات زیر در کامنت‌ها با هم صحبت کنیم:
مدل هزینه‌کرد:
به نظرتان چه مبلغی برای «مشارکت جمعی» منطقی است؟ (پیشنهاد شما برای ویدیوهای زیر یک ساعت و بالای یک ساعت چیست؟)
فرمت خروجی:
ترجیح می‌دهید فایل زیرنویس (SRT) را جداگانه دریافت کنید یا ویدیویِ چسبیده شده (Hardsub) که آماده پخش است؟
یک فرصت برای شما:
اگر تعداد درخواست‌ها زیاد شود و نیاز به</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/3940" target="_blank">📅 18:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3939">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tmNTGq2leyfFwjVadQhvfoE1NIahuRqEbSh00zS6Tqp-EhP3CBpnZWh86iGR-YuCq8zYRf-hSLoF9jmV1IRgO6woZYWBJUmMYlRwbSHjYNGuizcpR1OtVHq9xgDlocTMKyG1GxyEfhibWhZyPERvOGq0TOnPLhFeoyfkVhuGqP-n5AtAGnMdQEQCOJQcpI1aZkEBWVzbGlrc2fKdh2dRqYMfTZwQB44-CGJnlrGdg00LNTIXqTo3jhGtSof-ap97m6K8hYoAh6CjsOPFR5lnSvWD7ETy9_CZVTTghrloFKR-onpS4RKUu6JrsGvI5YXx9uVRmjcrcgyyPkbBPtOfww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی از دوستان این مشکل رو داشتن که تلگرام واسشون باز می‌شد، هیچی دیگه باز نمی‌شد. یا یوتوب و ... باز نمی‌شد   مشکل احتمالا از کلاینتتونه و dns اش. باید تشریف ببرید توی تنظیمات v2rayng و Domestic DNSرو از چیزی که هست، به 9.9.9.9 و یا 9.9.9.12 تغییر بدید. همینطور…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/3939" target="_blank">📅 17:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3938">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ku0-M5nsfsHfL3ldENvqIN9oYwjgSpFxqYb3UzAjk8CAqDA1c4D0-6Q839CUIReC_MHWrihzu-lL9FP407AGsj6Y3xaCAozC5u2NyiJwCBw2awDfCVdjYKPuju7oL4SlE2IWaX-IziTgO4Yda9k2cXimyIaEsuW2NC58y4upKu0C8v5ol1fo8mDG7Atq35dcaeEg8kGMznO60ss4HlWlhkOdjXunkUcSzMul5RureDnVOPwKaID380eAw_iboMj6ON1A96Bf-rSVLVeyo7MTqz__IGvLJBKxE7SljjEVD9HO9tQD6bl-z2ZJBOToqD92FlK4hWqaC-8NFVuEIQlIkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
بدون دانش برنامه‌نویسی و کاملا رایگان، اپلیکیشن اندروید بساز! (فعلا اپلیکیشن ساده
😁
)
⚡️
لینک‌های استفاده شده توی ویدئو:
1- خود AiStudio گوگل:
https://aistudio.google.com
2- پرامپت ساز ریک:
https://chatgpt.com/g/g-6a319e2a22648191836468df375a3763-prmpt-sz-ndrwyd
⭐️
توی این ویدئو:
1- بهتون نشون میدم که چطوری می‌تونید از یه پرامپت ساده، یه اپلیکیشن ساده با تم دلخواه تحویل بگیرید
📲
2- توی مرورگر، Emulator اندروید بالا میاریم و با اپلیکیشنمون کار می‌کنیم
🏆
3- و در نهایت، اپلیکیشن رو مستقیم روی گوشیمون نصب می‌کنیم!
📱
🤎
اسپانسر ویدئو:
خانه EB، خیریه حمایت از کودکان مبتلا به ای‌بی و بیماران پروانه‌ای:
https://ebhome.ngo
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگانه و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/3938" target="_blank">📅 11:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3937">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ویدئوش آخرای ادیتشه
🔋
می‌ذارم تا ظهر</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/3937" target="_blank">📅 10:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3934">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J6ufsDENeHaD10C-jgmNCKgzGvaLSYCVGASmIpVJVZEFjno79Rnf8ozzhivmYDQYVeGNjXZAVVZn3EpR8QD8eXJe3GRkRclrsEv4E1-2nzGvIEAsaK_Hac4l-bjNqh1ioIriflJ8xkiPjuaUi4o2r5n1Zh3wAwzj2oNC1V9n3EQW28PmeYBmd3oOlfjcKmhoyy1VbsJdvcub-2m-o5AKAc0g8rgryZLqjPy7GHSAThNRVErB0cdMyaai6DUBycaTsWL1VrqcvrtfpRDkynzD571qGOmYOBL72nk-Ywt-18ygaenSfAyPpYiqEcAhsVXUn_RL_oLhCAd3zv3saOkfKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l8xdAhn-uUJXG2e4ggwVADNMETcTjX-c4BkKu71f5vk7z6YV7VNOvWkrrvGD3TsWbksXHF03S3KTPki_Z7wSHHa59Z1aoWBV9V6YTYo7ogfNqYhM4Oj6v6a0wlzcnCyLUxt4nbiiZ335_eqS0yBAnPkH5lajaOY2qeHvYJXtwwP-ITJJ3ylPjhQzmhciiRIIpTA6pk-2TM5ZixpXGDbz63v7UuFTE3_BnoZ1FMiBUPh5Anwaxyh70RFNMztETZZXXo67TCN-nx0tibvfAoW17njay8f3h7yTnV3RPXF9_q0-cYpPLDGTG2-BUrjNnFNzAomA4G6cun5Db1UZNcz2Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a_CkLxjN8Jmk_fZbi7xXy4yCptFXMBHDBkMpiKPaCkDNbe4eqnxZtFkZRtt8gqnC1bJb9R8NkXVoI87UhYDphWywEDNh3nvL0uZWR_Vnz3RJC7Q9rY2OBfK212BccocRFmxqqmjbCyYzmg7qa4xPLYp1b4xy1RthGR-DQGaZCketVCT_LVofgXj_9D2S8YEGt_Rt-bpWjcOvcp-ZGYTiZv3IKSFVkuGiHzM5TAr8fVx2AEJfM6qJH0o5D6Agn1PK3RsGZ_3umpuF34hXc_1yFnxYSIX-G8MJlX7jDqmW7RfZdddfcc16V-W3UsI_wldOkEEG6ktVXSNOsKagYcWP1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه اپلیکیشن مسخره‌ی اندروید با AI گوگل نوشتم مجانی، توی بیست دقیقه
ویدئوش رو ضبط کردم که به شما هم یاد بدم. اصلا چیز خفنی نیست اما خب بامزست</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/3934" target="_blank">📅 23:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3933">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">میگن Cursor یه چیزی ساخته که SpaceX اومده 60 میلیارد دلار خریدتش
نمی‌دونم چقدر حقیقت داره این حرف اما سرمایه‌گذاری خوبی انجام داده. به زودی CLI کدنویسی grok رو شاهد باشیم احتمالا</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/3933" target="_blank">📅 21:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3932">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آموزش کوتاه استفاده از :
WhiteDns BPB  1.1.0
📱
📡</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/3932" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3931">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ورژن 0.0.3 خیلی بهتر شده رفقا. حدودا بعد از 20 الی 30 ثانیه وصل میشه روی همه‌ی اپراتورها و سرعتش هم عالیه
منتها می‌تونید از خود Wizard استفاده کنید و بسازید برای خودتون</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/3931" target="_blank">📅 18:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3926">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.3-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3926" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/3926" target="_blank">📅 18:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3925">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/3925" target="_blank">📅 17:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3922">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cX5GCMbAY5wNJm-CZVrGROSEqNDYmBZEAGT1WnlHj2bBJ-kWa9MYsINr4AQnhIJtzVPWN2mJKvi7BpNy6Ua8If6kmJUN0hba_Sr4dLEj0wu1kNQTEX2ustFtSdI16sn0GvtSbfTAPqkAQQIpG9EIbVYvFsWio0TiprZMZeuguJEB0xR2VevspM9gsvTML0yF_piS4RwSW09Xq96TQP-6Av-1I7mLzF7H9FLwxjrqfNqGgoZw1GU3jcxK5Sbwf9Tc5qseGrpcW2MlQumJOvWU8-Jx9kEXA41fbf-S-6nTR107Srd8Z4pjbnYe5VTyvWMiOBWeSSC3EOcYZVx_Nz_nVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lo9ts2Lc9j45ZYHrZCK7GJw47Rr8Fl8C8vPQ9qboUtUSdolFrGZ4h3JqTMcbvhygo3PZr5UtWsjddPTfkTP7FIJ-RM9RE9u_HItfRc-SRzDJhV26pWQ4PsgtlcfHh4KnFmiIzY1hMhyNvZSB7J11ofrHVFq1pYLVyoFhJae77muP-gUQhRosl_3P9lS93fN0GkpRo6Br9oLKqD8wkFxY5LC5LptX2_tnSmivJds6iYY9x0k7BO7t8rg3WLHOI7pA9MzjgO5tCQnSA505GKRyQ-af3tBa7mAwDoz6RqHmfqup0EIlfhVeJg9MJ9TF_fG4-RdhgTYgXNWA-D7AnvWEpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/svev4wSBU8Kf5dcSbQvEOuIXMXwJOzccM4IXtmncEHZ_TVh5Vpk7jceo2D0hDKoAfKiI_g3vC4MV_2Yxp74J_cNk2QAGjHlJimHkix7neQikq3yQh046Msl9_-XAishJ14p1AhFB2PkUwA84PtomEC2Aev0D6VN8qbkfXA2SPQVBQxJnq_a_iEErBlCBqas0h0CDJ6HTPtY-25QIwoqtXAVWVw6_ssqEriaOOYfT_R-MjPHQdyB3uMdz6jUlYXFKQsAaQsIZoQt3V_2OafX1lVLi-_ESscbDH46eYzKxqEQyFkkWeGzl4d3NPsZ_cbbAx7RiEKqsZTCxco8fB5mqxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بالاخره قابلیت ضبط صفحه نمایش به همراه دوربین سلفی، به اندروید 17 اضافه شد و دیگه نیازی نیست این کارو با نرم‌افزارهای مجزا یا تیک‌تاک و... انجام بدیم. کلی قابلیت باحال هم برای گوشی‌های تاشو اضافه شده؛ از جمله foldable gaming(که توی تصویر دوم می‌بینید) و ارتقای مولتی تسکینگ
اطلاعات کامل تغییرات:
https://blog.google/products-and-platforms/platforms/android/android-17-features/</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/3922" target="_blank">📅 15:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3921">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">برق داره دوباره نوسان میکنه
اگه سیستم داشتم به جای لپ تاپ، از صبح تا الان 15 بار خاموش شده بود
فکر کنم باز می‌خوان قطع کنن اه</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/3921" target="_blank">📅 15:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3920">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">😂
😂
😂</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/3920" target="_blank">📅 14:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3919">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ugj-PuYQJ0UA3SQQsFR5Cg08Y2h3pWCx1KiN5FLgOo5-wqRNhYJQwr1Y6mz86sJ1eRw1sHLgI0RFpRNmtVaGLr5JDHqBc0rASUVCV8zy-f3fYQT6qqDRItb24S1kNAi4uXb-CcvUo8qbVdFJebokFsB1wg93bAsRBC9rB4jvZIh6J6vJN7w4w8ktTcY4X0Olm4ryiqecZ9TPpvnQSEQUtoO0WrNlsDIsE1EFMx7thzzoPinYKssDjMnpTf8Udp5lTkzCHlCDii1atpfH2DlF9ZLL1NGFC9tk6Py1je5JOgJxdBLSM0vDWIieNfaO0NXR38ISKpBkqeQ9AOBjMgT8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭
😭</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/3919" target="_blank">📅 14:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3918">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fumJ4RqGTeurTuZpQrOxjknN7cRY8XQX8kRcuEzdnAHxlZKilK_HfmKLKkV_CiVXoPtT6OdUz42FtNS1ORwWn_NcF2fQhbMEgrmMvrdYh8YPEqUyIpA8LS5NkuQO-c4aVBMpmGHf4T4C1U8EKvSmzRmZQhyf2J50_BGRyEPQf1JezIyQs7-Odly2i4nA3f_zmf6J-YIVNS6DESxPv0LKgy5fX3cnJXc3lbrQintUqlwLthMpzUfpJ4jDlhmdWCUYiSBOpfUdiIlRxIKknu3pbzK01VTb5sJ3-ilZEb5DwWQ08OAK5I1t9nwz6vqnctLqtnoEdulxQtE9UsUZiwz_YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیدات کردم مهدی جان
🥳</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/3918" target="_blank">📅 14:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3917">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QRRfPu5GL2A1qoPddETTJ6hg6vQWBeB9OKPuXKzOuvVwrgrKG_zw0NcRScsKMrrdGIw4yXXTtyYfuH4Fr12A0EppFUpXaohqGOjygJBPe5-Sb7yyZBgassWx7nQ7Yb0BU4c32KvsvVqdYZ7B2D6qXTNOebGprBZorjbwV-d1j_2rp0HR3EOfMAlCXy9BXrTTvjeH_dXJwvG4irxuPjetkJyxkycVZ3lUeC5Gw3YQmspUP8DKUsxAqZ2NdoQc983PXu6RzCJemtTz6NhjKKLPCLF2vKu2q6qzueO30yDGVGT4hZkwdpwoF0Wzs58fL9McsV-XIOZtW863ota9yLlwEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندتا از بچه‌ها تفریحشون اینه برن وارد پنلی که من توی هر ویدئو میسازم بشن و پسووردش رو عوض کنن و برای خودشون لینک ساب بسازن استفاده کنن
😂</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/3917" target="_blank">📅 13:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3916">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/3916" target="_blank">📅 12:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XDdEIYy2H0zhtXGiwdP2CTEFfdvZO1_uKHYPk7RBNKvdPg3gp_oiqPvOEmuSY2uCzr00gOYgQoDHcOy9tEBA1PNgrRr5uBa7REZPaRm2tOI5KExT0jmXzfVdruKSvMQ2SRPor-i0TsaGDA0yNJAHErc3Bfy3CFTSbvrGzV9E5vFybYJcjVvWCwkagKvhNABwgcx_t1GZSdqUMMvNuX_DiNl76-vBFyFH955YNfMLxCm2NGtZS9w1Sej9ZUcPCLKrZ-c1Or_9wTiHaLVXumglkrEnZamc-pEiCGUbtFuMVkWM5TW1EfqB-0G2RIIVeHsI9LV_B7CkKHhNAFO9sFZZoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/MatinSenPaii/3915" target="_blank">📅 05:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3913">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/3913" target="_blank">📅 03:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3912">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">من که عددی نیستم والا نمیدونم وحید آنلاین و اینا چطوری هندل میکنن که آیدی خودشونم گذاشتن
😫</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/3912" target="_blank">📅 01:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3911">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/3911" target="_blank">📅 00:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3910">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3910" target="_blank">📅 00:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3909">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا من داخل این پست میخوام توضیح بدم این بکاپ ها و این ip به چه درد میخوره؟
ببینید قبلا یعنی تا چند روز پیش شما تو ایرانسل اسکن میزدید واسه ip اینا ۱۰۰ تا میداد برای مثال ولی الان هر  چی میزنید ۵ تا به زور بهتون میده و ip اصلی که
188.114.97.6
میشد که ملت روش وصل بودن رو بستن
❗️
یعنی ip ها کلا رفت تو دیوار کاملا خاکستری شد
اینجا (patterniha) بهش اشاره کرد:
https://t.me/patt_channel_x/68
بعد حالا همه ip ها واسه همه جواب نمیده باید ببرید پشت gpt با یه سری ip محدود برای sni spoof استفاده کنید.
جدا از اون میتونید تست کنید این لیست ip ها رو که واسه شما وایت باشن و مستقیم بتونید داخل پنل های bpb و نهان و... استفاده کنید
🫰
ip:
103.160.204.34
185.193.30.94
45.8.211.57
199.181.197.1
159.112.235.52
170.114.45.239
104.17.21.111
104.24.200.94
188.114.97.6
آموزش ساخت پنل bpb
آموزش sni spoof
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/3909" target="_blank">📅 00:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3908">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X1pzikcrusefI_2uw19ogaCDDZFZmSbbf6_mStfNGEJXGK2l6qrUK-5vig-7O0RdA_biiUEtq1hY_aLF15XrQFq9fewj_gaNd75Okx9oSwDQXYMJ4AofGjzy1ZFQR65opCX7jPDXq4MGnAzzmgLixsYnNfUTqD14ppCu1siN2Tq10tqJl1HNdqF5iVUinEc1hd-3z28xFZAaaqGK08cBB5ryT4LxL8qnE5-LHrzxJGGcayiXtdpeshA0QeuB8d5g6s8Y7E-Awci-SdWhr04KByUCtzys3WTF3rO2dwfSdH1hAXtm2tm3Lc7fb4RgDQz8N_iIUKEK3C90DvFyZMTDxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/MatinSenPaii/3908" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3907">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">متشکرم از بچه‌هایی که دونیت می‌کنن. چه کسایی که استارز می‌زنید، چه کسایی که به ولت‌ها دونیت می‌کنید، همه باارزشه.
من دسترسیم به ولتم قطع شده بود و مجددا وصل شد الان، دیدم دوتا از دوستان 3 و 20 دلار بیت‌کوین دونیت کرده بودن. ممنونم ازتون
❤️</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/3907" target="_blank">📅 20:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3906">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/MatinSenPaii/3906" target="_blank">📅 19:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3905">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر:
https://dash.cloudflare.com/
لینک پروژه‌ی نهان:
https://github.com/itsyebekhe/nahan
لینک اسکنر:
https://github.com/MatinSenPai/SenPaiScanner
لینک ربات ProxyIP یـ‌بـ‌خـ:
t.me/nahanproxyipbot
لینک ویدئوی اندروید:
https://youtu.be/2otJfXgNWCM
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش ساخت پنل نهان
2- اتصال به ربات تلگرام و api کلودفلر
3- ساخت کاربر و مدیریتشون
4- رفع مشکل وارد نشدن ساب در  V2rayNG و ارور 1031 و 1101
5- اسکن آیپی تمیز با اسکنر SenPaiScanner
6- پیدا کردن و تنظیم ProxyIP بر اساس کشور یا بر اساس سرعت اتصال(توی ویدئو نشون دادم چقدر سرعتم بالا رفت برای دانلود)
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره
با تشکر از
YeBeKHe
عزیز
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
(نسخه باکیفیت‌تر)
💰
دونیت</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/MatinSenPaii/3905" target="_blank">📅 19:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3904">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">داریم تستش می‌کنیم این رو، و خارق‌العادست. دم ویسپر و پدی و بچه‌ها گرم واقعا توی ۱ دقیقه پنل BPB ساخته شد واسم و الان دارم پیام میدم باهاش</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/3904" target="_blank">📅 19:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3903">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-BPB-v1.1.0.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3903" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">معرفی نسخه اولیه WhiteDNS BPB
نسخه اولیه اپلیکیشن WhiteDNS BPB منتشر شد.
این برنامه برای کسانی ساخته شده که می‌خواهند پنل BPB خودشان را راحت‌تر روی Cloudflare راه‌اندازی و مدیریت کنند، بدون اینکه لازم باشد همه مراحل را دستی و پیچیده انجام بدهند.
با این اپ می‌توانید:
✅
به حساب Cloudflare خود وصل شوید
✅
پنل BPB جدید بسازید
✅
پنل‌های ساخته‌شده را داخل خود اپ ببینید و مدیریت کنید
✅
پنل BPB را با مرورگر داخلی اپ باز کنید
✅
لینک‌های سابسکریپشن مختلف پنل را ببینید
✅
سابسکریپشن‌ها را کپی یا مستقیم وارد بخش VPN کنید
✅
کانفیگ‌ها را تست کنید
✅
از داخل اپ به VPN وصل شوید
✅
لاگ‌ها و وضعیت اتصال را بررسی کنید
در این نسخه تلاش شده همه چیز ساده و مرحله‌به‌مرحله باشد؛ از اتصال Cloudflare گرفته تا ساخت پنل، گرفتن سابسکریپشن و اتصال VPN.
اپلیکیشن هنوز در نسخه اولیه است، پس ممکن است در بعضی دستگاه‌ها یا شرایط خاص نیاز به بهبود داشته باشد. اگر مشکلی دیدید یا پیشنهادی داشتید، خوشحال می‌شویم گزارش کنید تا نسخه‌های بعدی بهتر و کامل‌تر شوند.
WhiteDNS BPB v1.0.0
@WhiteDNS</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/3903" target="_blank">📅 19:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3902">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">توی NPV tunnel هیچکدوم از مشکلاتی که داخل MahsaNG داشتم رو ندارم. احتمالا به خاطر dns‌هاش هست اما خود V2rayNG و Mahsa و V2rayN خیلی اذیت کردن این چند وقت سر BPB خلاصه یه تست بکنید</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/MatinSenPaii/3902" target="_blank">📅 17:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3901">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">توی NPV tunnel هیچکدوم از مشکلاتی که داخل MahsaNG داشتم رو ندارم. احتمالا به خاطر dns‌هاش هست اما خود V2rayNG و Mahsa و V2rayN خیلی اذیت کردن این چند وقت سر BPB
خلاصه یه تست بکنید</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/3901" target="_blank">📅 17:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3900">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مقامات هند، تلگرام را تا 22 ژوئن در این کشور مسدود کردند.</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/MatinSenPaii/3900" target="_blank">📅 15:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3897">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qF_ybvDwNo3oGlEvSy7v9SJwAO48bOhafyiGM2BKdKZ5tGnog4mQ3F6PZ05k_cPay4SfrbEv9VLPJL9-n25O3vCg9QHDTzITY3PEkSeLCbhTH_fWT5hqtx9j2DNekOCoCgx88KfBE7r0kF-dW8rCKDegvl_5hHcPFDc-AUM1f92s-myd605y5DIMZkyH1qDlsHmQ8qyOHYMh04A_mpwHvkH625wMGo64_FbUvHy1XlJt7cEBz2M575Q8Mwn4pTprLYVBLPvmx2-LxfG4GlE9DKpN5pMtwzuF9FUH5wvzjCqfZntz-mQUkUXyYrF-AN1Hba1omw1Ixp7Qlif1woYTRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v186YLRC4TPCLtQafp8ryJhgkzXwvijGETd6KTkSWgiRLU6irnEsOlhqnox2yO4Fi0SwIXscqEvZ0XUocLQEy_9PgiSFwqZkXtJpWt5iwyZiKWEbepT4JO-D-2n0h_WVvkM71C-44Yx-AILKDYwfYIeHJnDiHKDF8IGBHHkQs1-FlUm2xUjvS5sFP1WxitfSsj0KxTcJEZSw_p9NDz-D062OLVyueoRuTXpBRayfmRvytWc86fxnQOat4WbzB1W1REHo6aEkYfZ7_MQc-V08I2OBNey5bjQXlOorD0vuGZFLsUIPrBaCw0TT5peamUQOZ1Tzs3XBJifUJEtl8gGCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fkjh-KfGFWRktRurPDVA9v-UwZq2qtU3JVoPw952CaMj5SUa6U4U-THF1MmSkz0Gc3QBdQco-GamKTCzEDP3sgc7uk5ou1Wcs4hXjJN6EW9E1FCZndA3F5xKLV7ApS2d935WU4AYWV6HoRZlHOmXJJAJkaIu_SZnay90Srt0PfB2TNw26bQCmfBbsybPk0R5HOI7wW_4VIwgn7GHH6mylbg_Pxu6l0ZCnykwdfA2tcZA7hwsGT0InNCEjsDUdIWo-IcqN3jckn6FqczlvwBSqAYi60IFpb5Ghn6wNWXaLcBE8LBJodgUJY_Xyg1LozT2aaPYKgGgSOnVUzzNpd3gig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بعد میگن چرا کامنت‌ها رو جواب نمیدی
چون 90 درصدشون جواب توی ویدئو هست، اما ویدئو رو کامل ندیدن
✉️
مثلا اینا کامنت‌های ویدئو BPB هست</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3897" target="_blank">📅 12:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3894">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F4vSZk8CCKaoGnT2bSj6oX6op1OICMxaWiFVNNHVma930oF-rHVLenhVRbKZpcdR1cx1UF5KYBYxyhb3CuC6oNqq8JIenU3zTCq3qwaurh87TxITvvdmqAJM88uAhZdwKT4HwXFJ1QpXwHIsKczekAYUDOrWvBh4kp-6ol3aN7PWniAgRPRwK01_ZhakSTy-EYydouanr_hhz4yPM2J8pMcJW8diinPGLy2kVz46c_H5TOlYns5E8ecgdWAgJPHpAEiN0XuPNaXNAmOLqc8XjG84TfJq74tIdEbxbMbh0BJhp8UinI9zo81B7mlAy61lRkLOV67JjjFqwVrP6i7WLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d9_WbLb-Q5rn7NzJe2BAhGA5eacr5eUlfW7UulTY_FKRVY5N_F82a8-pQ9ROcxKXmOl0NQzQiovdJbqIitX05Q6EguVNwtVMI5_za8O8jtbT-T_ZJxKJdUkdVCFYUKJCITX7oXa4cMBBHID8ZhpC9xMTfyhAnpKrQ30lsYDzycj3ZPi17XYmZKOV7W38wXC8EONVjQAExMKXYojqHPKSE0IJoIUZNqaUEkM4gOtTZrOea5NBCcPQxwDVWOwxMqQH_TRTiMBRi0JMw2pGsCrJaD_1llNx0QDkfILdckjjn21dS__JINWPzXFyOeBfOkpNvVgiYysYHhnzn1G5sDi6Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PDUwlLL_VpB6fVB-nE_UoTexe-jZjrBsO2GTjDV7p9eQAfrdk6M_vJ9bzG8V1eIpyKUhX5fD9qCN5JTB_KKaarqS5y30vqmLZLEhht0W0Gw7OU3WF0M58kDbLoHloRG9sMIpKHQzpdtqtCCoyHSxR5DBFg7iWjdF1jdZfMgVRXVfIBbOwHMLr8adL_XFC30D19oNxyAuj0VQjcqmnxyie3p6fzWYsXq1ufKxh-Tb7pHwNP6KEvGjofQzksioeY9ZwzT2RPcXFyq-wbQASA55usCK0-zfCUQLv1S-Am3MiJE5u7kOsOKdQWI501KQENqFJ7SSjc2VPss_WHGbM7K-bQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا با WhiteDNS BPB هر کاربر اندروید می‌تواند تنها با گوشی خودش، پنل اختصاصی خود را راه‌اندازی و استفاده کند.</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/3894" target="_blank">📅 11:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3893">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">از دو روز پیش، دیدم که سرعت آپلود کانفیگ‌های مستقیم پشت کلودفلر روی یه سری اپراتورا توی منطقه‌ی ما به شدت افت کرده.
و بعد که چک کردم، متوجه شدم سرعت آپلود خود اینترنت خام کمه و زیر 1 مگابیت، و مشکل از کانفیگا هم نیست.
پیر شدیم برای یه اینترنت خوب</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/MatinSenPaii/3893" target="_blank">📅 09:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3892">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">شمع iced blueberry
🫐</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/MatinSenPaii/3892" target="_blank">📅 16:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3891">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0t9YNI9t209WMdqjcGZlqbulIkQqjh0spCsC5VJaWPxBV_occEhA_zgm3e9zMRsGpgAcFRCfYrqGX7zCG5XmEquGEKFsRbYqjqPcp55TZlGWr7WBP2C-wkSgnRcd3UhXglnoSK6at--E6vXTA8KiCe5ROMk83HsWHaxosw_PjBtXTvWkM4ssaaD5FB74mNmeetPXbi96OXg4bmfqa6xfMpziLrYRcyRMgPoJSvLIAFDSpNwdZDF6CqkXDnr-eBPnpa_Q4YatPsVMhIaa0zqnpsaj6znGp2t0mJNs-uhpFilRWkkg7bH554Um1dI9ngwUsraP0-4U157ef4WqkT_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
جدا از همه چی رفقا این ابزار رو خودم قبلا ساختم این ابزار چیه؟
این ابزار کارش اینه که شما لینک ساب بدید کانفیگ میده با فرمت های مختلف و همچنین این که کانفیگ بدید بهتون ساب میده یه سری آپدیت ها براش میدم تا بتونید مستقیم تو اپلیکیشن ها استفاده کنید ولی فعلا داشته باشید و ازش استفاده کنید.
لینک ابزار:
✅
https://xsparvin.github.io/Abzar/
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/3891" target="_blank">📅 13:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3890">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EEbf6G6Ty9Dm9ar4ihP3LkXRCLO3pVP0JS2nUlXdk7VMXQosE0QSC8isFicYFAucRRAN4vFS-7ICZZZ9I4jieaew1ddpHEjGYrPjYAvU7GW7wOQvXgTf8gRuugMskFXxQADvDVzgBVPHS3-zRqsZCnW9ucD0q6zWh_u4MSdidBteun19nDyJb9ZGWbubNwGzXOnEZjCIImeFrzG3jhLjgXb0_BXI9wNyaZNR3xrzHs6eSVtAPHdJ6nJ3Ln3IEEETtAIrl3BiWSNyO4RcJAomgGMHB8cFFh2Vmh4HdiEhYMoGzbe_MAmyubqEjfUUKp5GA5PRnY3rpDnddpNdotD-8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اول که ممنون از لطفتون و بازخورداتون، دوم اینکه اسکنر حجم زیادی میخوره حواستون به این نکته باشه
🧐</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/3890" target="_blank">📅 10:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3888">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mll3z0KDUE7f4IOU8H7qwJ7W-u4eMLVY_Ry-ToRdLT1jQEKPM9Zh9PD-FGvON1CFwYeQfbhbj2bU0ca8SN9rQvAW0zIN1mqWU3rF4uKGrIhulJxQrSD71r6xalC-EFQfbz8l-2RAw0s9cqrbZTO9sbDEbDcn3kuppDCYkdZtgxPNcv2sZg8y7m2Aw-NZ7v6bSaZW9ZP9N_7AaCbJPIc45vw4OYUTJZCXKQFhb8Ho6lBkcnzneURbIlB3OX7VkbN-zP6uS4BwUBBtZSwYoeEl6BbNHQUsO9Ks_-Cok3of_VmEM6pwk-mWq1oXAfOq0egWL4l4bJybkiOs3i9cJk8DAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uCVsiTRiBI8uOS2jSzkLjj-oIgAOl5vejhL5HdgB9P156uu_ruki4sQCv-IsXV_7xRTXaxDdFW02x_BxCSGp42d92_1eQYxld0FRyl84MRN9Ni666ERHb8pJZeeH8N4gT1P81fLw3wLnBWcS1a_gV5zElISKMlBVBI6N2XlStKSVAbQ0hXYcaLX5U-b9vPcgli_loigZcs343Fsn92NT0fqa2sf5L7WoF5JqNpGAORr7iY0Edoc6vAQQUYWugrtu3b7zwBZPjZiPDtdmk4go_WDao49ERhPM2ht-pDNYL4OCX2NqOkCGc_Tt1_hf9AYbyK08YY_4sWPZBo7Vv7K90g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور: @nahanproxyipbot</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/3888" target="_blank">📅 10:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3887">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XjJGtNDXZMmzChr-JEyHZDAodtZdxzQZwvfnoZ9bKyz7_jtYVeYZYyHoQ-_ai3H28HYJ-0ocCnNb_9AHzaPwHlAdqOoK5XB2zoLSYaz_0ZaHt5zh5f6ZfcMe4tWO9SDeohHPGmcNkoQwGjC2n0UxqlJJIXwbZQOWyqJxh5mmLggUE1QhMNxeUp5L97FV1wdgrrQZOL8oEx26lwVH9s7OMUlDf4IyfcMiSfyVKdewWkug4jJXfWYZ02Ki1PoUsR53PLHYerTcrQZMpMTIYpvEMFVTUiK9zCkbXBIARAzvzWi5PY4AgQteII2S43ktoSQFkp4LT5JJmkg2WZa6FEwPKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور:
@nahanproxyipbot</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/3887" target="_blank">📅 10:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3886">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خب قیمت دلار اومده 165
انگار جدی جدی توافق(که نه، تفاهم) شده</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/3886" target="_blank">📅 09:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3885">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VUVe8vcp4PyOtNV7AvjDq5J-13jBCm1mhJ-WyUiGS1eM08D6e8qRXlikFwTaY7599DBEwdFxWYk_8cl4YiBQsh45CK7ra-WHLzbEkrd2B1eXQCOOrKybY-1pzBtNQWKaaquG4FnLAAkC37tKuG7VDjYb6RiaLfLbvBUUPT1oX-iW6wm6H-5tdN4sF-gvikNKvrBBe3AzDjYXx_1usSAIG3L5591_KvPUq9BJfQAIShx7FMwO-LQDkaCyYN3FJXmWOmNgNinbj-CTriJUMxGQGfkeg_bNOvv43QMwkDefqIUMVdMShKRcy-iXGtyvBJSWUlnIsa6zrn6JJ5aVWL0efw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پروژه‌ی جالب دیدم به اسم SurfSense، که بهش می‌گن جایگزین اوپن سورس NotebookLM
📞
اگه از NotebookLM میاید، باید بگم که SurfSense همون کارو می‌کنه؛ صرفا با کنترل کامل دست خودتون. خلاصه بخوام بگم، یه agent تحقیقاتی اوپن‌سورس و با تمرکز روی حریم خصوصیه که شبیه به کار NotebookLM رو انجام میده.
👍
مزایا نسبت به NotebookLM:
• اتصال به ۲۵+ منبع: گوگل درایو، Notion، Slack، YouTube، GitHub و افزونه‌ی مرورگر برای ذخیره‌ی هر صفحه‌ای (حتی پشت لاگین)
• آزادی انتخاب مدل: ۱۰۰+ مدل از طریق LiteLLM، یا اجرای کاملاً لوکال با Ollama و vLLM
• بدون محدودیت داده: هیچ سقفی روی تعداد منبع و نوت‌بوک نیست، و دیتا روی سرور(یا سیستم) خودت می‌مونه
• جستجوی بهتر: RAG دومرحله‌ای در برابر سرچ تک‌مرحله‌ای NotebookLM
• قابلیت‌های تیمی جالب: به شما رول‌های Owner/Admin/Editor/Viewer میده + چت و کامنت و...
• تولید پادکستا بدون محدودیته
😭
معایب:
• نصبش هلو برو توی گلو نیست واقعا. رو اعصابه — باید با dependency، API key و فایل‌های Env کلنجار برید
• هنوز کاملاً production-ready نیست و در حال توسعه‌ی فعاله
• باید خودت میزبانی و نگهداری کنی؛ طبیعتا که راحتی NotebookLM رو نداره
#️⃣
جمع‌بندی:
صادقانه بگم، NotebookLM همچنان ساده‌تر و آماده‌تره ولی کاملاً بسته‌ست. SurfSense سخت‌تر راه میفته ولی دیتا و انتخاب مدل کاملاً دست خودته. اگه با self-hosting و سرور هم بخواید پیش برید، به درد بخورترینه.
🔗
ریپوی اصلی:
github.com/MODSetter/SurfSense
آدرس خود وبسایتش برای دانلود مستقیم نرم‌افزار:
https://www.surfsense.com/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/3885" target="_blank">📅 08:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3884">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/MatinSenPaii/3884" target="_blank">📅 21:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3883">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/MatinSenPaii/3883" target="_blank">📅 19:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3882">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gu_Ky1aUJlgGGlqoHb0szV5PlcPj2tUpgyVzxdVHyovNzUm1XvYnQhd-C_vSLljuTccqoFrncVycqsoxR4daTah8v-CfXI562OmvJncVwlGJsbIc0eFmDuxcG_Jbd96CxeWfLSx7pNTFXZO9b12mqwwnp1VYeO4rLma4UNnfNwhqj3aVrN6aekzA8Lr8saZd1oW4RDyvdCgC1o0XB3nzpwhN-V4FKsIlCyWpXVvxnR1B5XduwmQeqNXVKFpM3b0etam-VEYah0J9cQwtxaPHwgKfiYxbYacNfK4kVq3l36OYw5BdWUvvpLZCUCKiQ244Xjr2YHaRJ_jR7JK7xxoQzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این ارور رو برای اسکنر یا هر پروژه‌ی دیگه‌ای می‌گیرید، ترموکس رو از گیتهاب نصب کنید؛ درست میشه
https://github.com/termux/termux-app/releases</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/MatinSenPaii/3882" target="_blank">📅 18:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3881">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kTJlknIn-l8JHZx_EvAX0nPhQzX7yPcaUtROx0Rv3hBYAKuU8366SknJAnLCa8FKfMbvu9kEqGQo4PrG0FV5Eicqfn-p_6d4gOK-SqsZItIXPm5jzJjl5m-yV_3RFhzGR7M8ezXqLN4c0DKVabiq9io2ntCebbLaM48Yg7xWiqRU9uQuLBhEmPo6-Dz2GQpTxfVi6Kuwk87VkhxqOWMK-u091Vwk9Fjk5-cQ0vG9nw8Yz2VZgH9BXjc9hu2-pYoyGiuDmb0OrL5Lm8kBgeDqrVeH79SQZmaQTX6TPwlcKgPN6kpeXPnzQIvXU7MbH_z5TiCYFjHWwNU46ZhUlO5RqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الان خودم با سرعت عالی وصلم روی ایرانسل. ۲۰ ثانیه طول کشید حدودا، منتها ممکنه تا چند دقیقه طول بکشه. ولی وقتی وصل بشه دیگه کانکت می‌مونه و قطعی نداره</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/MatinSenPaii/3881" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3876">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.2-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3876" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه جدید اپ WhiteDNS VPN آماده شده.
در این نسخه
• سرعت اتصال بهتر شده
• مشکل داغ شدن گوشی رفع شده
• اپ همانقدر ساده مانده و فقط شما باید دکمه اتصال رو بزنید
متاسفانه باید نسخه قدیم رو پاک کنید و این ورژن رو از اول نصب کنید. این مشکل از ورژن بعدی نخواهد بود.
ممنون
🔥
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/3876" target="_blank">📅 15:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3875">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WF34PD6da-2xT-sEPLWD_gXNszfgMhD00VAg2-XZECiq89NQPQEwbwuxqOeJ_l4oIy9987_gSAknsAxraElXg48EA5EsHWLYja8_DiLBCzyyjeCAOfJPMvohpurIFQTTq9V5w2J6cdec8NzFWAigujRoQQxZLzx70-zyvPlOfwPU8sFI1yi80_VIqkfkhEm9706QM-hQLz6MTLuCJVsAKqMk6X7vfh2iILjxojCItzWWt1cqGoLFXsEbvtfedTAfC_dYzc5IGDQ_s-V9SH71ZCUeTXV8XVscxJFcN2Ld5tEoBFGjuLUyvJyX71vXLirUVYpj_NVIJFtmg0Cme_r38Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکرشو نمی‌کردم یه روزی قالب وردپرس رو هم بگن بیاید اقساطی بخرید</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/MatinSenPaii/3875" target="_blank">📅 13:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3874">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خب دوستان به نظر من اشتباه کردم و فونت وزیر متن هستش. مسئله اینجا بود که از من پرسید، گفتش چه ترکیبی بزنم؟ چندتا داشت، یکیش فونت مربع+یکان‌بخ بود. منم زدم همین و بعد دیدم اصلا پولیه. اما الان انگار وزیر متن انتخاب کرده
نکته اینجاست که چرا اصلا فونت‌های پولی و غیررایگان باید بهشون اشاره کنه یا دروغ بگه
🤔</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/MatinSenPaii/3874" target="_blank">📅 12:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3872">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ws_D8Bl4P4EXHpW2YMRkbtMqd6IRigSHogKk0D9kKG4DMU91AjsaYmBQZ5_pANRbyRuutI1J7M64WM_Dzukq0Vt8uXeqF8rmJaJ2cc23I48LfmVgf0h3RVBm2QF_1pHxBYXu5u5ab2K52xwehir0-z192vYZ5M-ESV81Jutr4V4hZAltdiyVtVEM5iExzWqTR_ixAUCjgI6xVtAyPkq17o18iK0e4qmoJ7RvYw6Lp3LNVWW1BY47ntJAo0yyc-QbETgm3XsLqkXoNeUIK6wolIKZsRy-KeN1Vg99e_k8r9S-SkVjP8EplNkDH5yZhUv8IyZVsZC2OxuUItm7agnjsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iRQehWK9LIoSHKl8zsS6yr08vNdlAVG2aRygn_UxEj8l9NnVOWxK0OJgevdvGA6z677gbtKYUZtNTbrh3K79S7L2yG2gtJkOp2aTxzA-4g8vaRpMqAv5yTboyOvSuZ6bmXLf6kBXrBcIpaxnhjRc2OR2j70QEZyloIKdDORQbHTSzsy-OQw2IzAodyO_FGqvg0nUUZ1C12gyxExJNLdOIwY69pi0NXl_QrP-_VPGGkfqsPEGUOJlolOmkvobQTuK6BfOy75I44iiEghXnrN-rDxXQLcWJjTlG6JKcyefyGobvVAwzgcQBeQ4j0uiUlCGKV-z_IB_KfVilMhDdagEXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم کپی‌رایت برای کلاد شوخی‌ای بیش نیست. اون از قابلیت اکستنشنش که کل UI و المنت‌های صفحه وب رو درجا کپی میکرد، اینم از این</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/3872" target="_blank">📅 11:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3871">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gjeV9xDeZkUJUNdX1k0ukfNKQkKuwnZeamr5Xt4wzIPlYVyN7mEy5G7ZJC1Nv2kWtqi8YgQDOWTmj6_FgM16C8M-Sw9ZOLwW65EAI87dDiPtHNe20brBIFj05g9KIcUaxLsLvOvPhxQO_yDg1oDV6iApXxSCSgROhQ1gXwozaIOFhIVuBg1kXlgnkPKRjYQgV-VKydUvmn_9FnuqmwEx2DTP5EjSbyLOon5TAQb42rMZ61dY-u5gaVDJXuPbvw1VWg1sMiBP4Sp0KKjacKtjRm8ztGr9caQHbE8GDk7y9c6o6wwO0soZfcESzDrLn35ZhlxegKKaj_VcJcJpm4GA6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این حد بگم که رفت فونت پولی ۵۹۹ هزار تومنی رو نمی‌دونم از کجا پیدا کرد و گذاشت توی پروژه
🤣
🤣
🤣
اصلا یه کار عجیبی کرد</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/MatinSenPaii/3871" target="_blank">📅 10:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3870">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">در این حد بگم که رفت فونت پولی ۵۹۹ هزار تومنی رو نمی‌دونم از کجا پیدا کرد و گذاشت توی پروژه
🤣
🤣
🤣
اصلا یه کار عجیبی کرد</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/MatinSenPaii/3870" target="_blank">📅 10:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3869">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">من منتظرم که شرایطم استیبل بشه، حدودا ۶-۷ تا ایده‌ی خوب یادداشت کردم هم راجب AI و برنامه‌نویسی هم واسه اینترنت آزاد که واستون ویدئوش رو بسازم</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/MatinSenPaii/3869" target="_blank">📅 10:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3868">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">من منتظرم که شرایطم استیبل بشه، حدودا ۶-۷ تا ایده‌ی خوب یادداشت کردم هم راجب AI و برنامه‌نویسی هم واسه اینترنت آزاد که واستون ویدئوش رو بسازم</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3868" target="_blank">📅 10:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3867">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏
بدافزارهایی که با ترساندن هوش مصنوعی پنهان می‌مانند!
تصور کنید یک سارق بعد از دزدی، یادداشتی آنقدر وحشتناک جلوی در خانه بگذارد که مامور پلیس بعد از خواندنش، با خود بگوید «بیخیال…» و اصلاً بازرسی را ادامه ندهد! پژوهشگران متوجه شده‌اند در موج تازه‌ای از حملات نرم‌افزاری، هکرها از ترفندی مشابه برای فریب دادن هوش مصنوعی استفاده می‌کنند؛ آن‌ها بدافزارهایی می‌سازند که بخشی از متن‌شان طوری نوشته شده که هوش مصنوعی از بررسی هرچه بیشتر صرف نظر می‌کند!
ابزارهای هوش مصنوعی کنونی، ترمزهایی از پیش تعریف‌شده دارند. برای مثال اگر از آن‌ها راجع به نحوه‌ی ساخت «بدافزار»، «تسلیحات شیمیایی» یا «تسلیحات اتمی» سوال کنید، فوراً ترمزشان کشیده می‌شود و از پاسخ دادن طفره می‌روند. حالا هکرها متوجه شده‌اند که با افزودن این نوع از متون ممنوعه به بدافزارها یا نرم‌افزارهای معتبری که آلوده شده‌اند، می‌توان فرایند بررسی امنیتی کدها از سوی هوش مصنوعی را هم مختل کرد.
به زبان ساده، مهاجم سعی دارد کاری کند که ابزار امنیتی وقتی به بدافزار می‌رسد، به‌جای بررسی دقیق کدها با خود بگوید: «من اصلاً اجازه ندارم این را تحلیل کنم» و از آن رد شود.
﻿
این نوع حمله نشانه‌ای است از ورود به مرحله تازه‌ای در امنیت سایبری؛ مهاجمان دیگر فقط انسان‌ها را فریب نمی‌دهند، بلکه رفتار هوش مصنوعی هم هدف قرار می‌گیرد و ترفندها در گذر زمان فقط پیچیده‌تر و خلاقانه‌تر خواهند شد.
✍️
NooshDaroo</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/MatinSenPaii/3867" target="_blank">📅 08:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3866">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pudLIljxgMCAmsLesQwITGYmWD61bBg5LWS1sy17AJeHsY-xshpC9a9eH4DUmppP7vnBr-yhyi6E5b6UVqdQL09CsVK1Y6NvjbJKWa2N-ZPx-KaLJitemL8_z3YcY49E_7Dq4eCxLIETJYRiHWfkp_kkcCWSYfU3mmEaRD-7PGl_LSo5x3d-YgQ25OrciRQdfW8rsW5wDsCCXQp79c6BNY1JK19c0AVMyQQ8ewx_Wnnu5CAb3-4m_yxzqqKOfMKmJunieDIucvKS5NsKguhxvz0HmMCSk18t9pLKEWQeuu2LJwWw6r-xRpSTJfT5qSWNmkel0vhX-X73mLJdLoBTvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید دفید قراره قابلیت چت با رمزنگاری e2e داشته باشه؛
باهاش میشه ارتباط امن با خارج و داخل ایران داشت.
کل این قابلیت با ریزالور ها کار‌ میکنه تا توی فیلترینگ و قطعی شدید هم وصل بمونه.
طبق تست های من یک‌ سرور متوسط با ۸ گیگ رم و ۴ کور سی‌پی‌یو میتونه تا ۵ هزار کاربر انلاین رو هندل کنه!
اینجوری کار میکنه که هر کاربر یک اکانت رندم واسش ساخته میشه که توی سرور های مختلف ادرس اکانتش ثابت هست؛
ادرس اکانت شامل ۲۰ حرف انگلیسیه که هرکی این رو داشه باشه میتونه بهتون پیام بده.
(سیستم اکانتینگش تقریبا شکل شبکه اتریوم هست، یعنی‌یک seed دارید که با اون یک اکانت ساخته میشه)
کلاینت هر ۱۵ ثانیه به سرور هایی که بهش وصل هست درخواست میده و پیام های جدید رو میگیره و تقریبا برای ارسال یک پیام چند کلمه ای باید حدود ۴‌ کوئری دی ان اس کوچیک‌به سرور بفرسته!
واسه اینکه به سرور ها فشار نیاد محدودیت های سختگیرانه گذاشتم، ولی همه این محدودیت ها توی سرور قابل تنظیم هست و اگر سرور شخصی راه بندازید میتونید محدودیت هارو کمتر کنید.
https://x.com/i/status/2065531715041239193</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/3866" target="_blank">📅 01:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3865">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uPkHgYcqmViS9RHcAAnFLhk82nc4P2MQ2_j3UaAGP-y0Iqqa_5CWq6UBOsUL7eh4mfio7L_fmv_SM3B7EQwkBVExV6k4R6xKl3qkaquEH3ZFz2JUA7niKa4lbNRnoAM7BgfpmM3NF4-Pgu1gRKeJ5kRNEpRIOGEc0h5cSg_4CKjcksZdHgoWMHwqCCpF2X1Yuf5FcAoHe_Ol1rczJi2c6-qaaHzrwXNplmwvpM0Aw5dOsw2ztAu-xQwLyQ1Cjxl10w5j-rfn9tvZcdy9xbI_XvGHGo1eMlo9rp9X0cvEsqhrKWu3zyYVN1Ov5Q6AanLAdga91vyb6fpTUDn57mH9Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا به هیچ وجه روی کانفیگ Websocket معمولی سرور شخصیتون نباید اسکنر ران کنید. فقط روی Workerهاتون انجام بدید که ارزشی ندارن و ابیوز هم نمی‌خورن</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/3865" target="_blank">📅 19:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3864">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">برای اندروید و ترموکس، کسایی که مشکل دارن طبق این آموزش دوستمون برن</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/MatinSenPaii/3864" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3863">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">برقا باز شروع کردن به رفتن؟ خیلی دیدم امروز توییتر وسط کد و گیم و ادیت و... برقشون رفته بود</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3863" target="_blank">📅 17:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3862">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مرحله اول  همه بخش مرحله یک  رو کپی و توی ترموکس بذار
pkg update && pkg upgrade -y
pkg install golang git -y</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/MatinSenPaii/3862" target="_blank">📅 15:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3861">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دیسلایک فیک میزنن انقد خوشحال میشم پولشونو میریزن جوب
😂
(توی یه ثانیه یهو ۱۸۰ تا اومد)</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/MatinSenPaii/3861" target="_blank">📅 14:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3860">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نمیدونم این کانالای تلگرامی چه گیری روی ری‌اکشن دارن
میگن ری‌اکشن بزنین انرژی بگیریم. انگار از ری‌اکشن برق تولید می‌کنن
عقل ندارن راحتن به خدا</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/MatinSenPaii/3860" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3859">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دیسلایک فیک میزنن انقد خوشحال میشم
پولشونو میریزن جوب
😂
(توی یه ثانیه یهو ۱۸۰ تا اومد)</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/MatinSenPaii/3859" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3856">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tTMc-CwcDvHfK4V1jBAOiJcyhTt4Mm7QR5y0ELKhpSrPUqrXykrYOoqoaAAM82sMSwzt4qUr06BATfNi3jRqVOsOCZ105DFRgaEOgSLBwK491tbNBX_KmvTnAqyH08mY5P5PeyvwWkiNOyeSSziVQ_a87if44EoEZpXCoB1aqlMwyBRgZiuE6r3HqcKam9-4sWwjJcjdVNC8ZufV_602hBroGH1WosoV2QTMpGTCsXwL4Xlx8eh6CkIUpp0MUO-5RFBeof53wrW-axFMM8zPMSXGugyPP6MbuQpRyUBYsEIxcF3xVILz523YySQ5ROHbS81Anz_1wXA_wbb4A6jibw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FdogK-WS3fd47E38MZvi_UlDbzYngnq-Rrtl_RXzqztIhUXPcJR4jFnGhRqcxFofdgKRu5nroecUMsNLam0lz5EU334XssYGes4dlGBxrgazidP_ASEDdV-gp9tGObuZbUXA6odMyejffcRZcFOUxAkibxZnIvAgoh9-ri9MQ6POm9XlNxGjbuLk8vc5vCw4iSa5DD23OYHFJ2szu0w5Jbqsl4kAJuS7ZtwZM9gM26AD2sZfAs-QzCAyt23Pp75CxkxQ2q9hZ9vFRqxvRbxMHsTslpKl1jzEvvNZ4OeNekYvDBosoR1UANh-QTt9O2V8VUFysh_JlMGnb-HU0TZixA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YprbNT0h8bCSc_rFyOLQRtNGNu8FOVniVJcOvYxZnDd-iYGhUEMrDNGltw5pOuBVVcLxGZttkLxPt4S3xno_LQOxHd0U1TjDmxs2iAShTULaU2FT7ILkfiPInCBLawNVYS-0zyFUW3Sz07DNdPOfI923LBZrIDwe6q3qCvp4ybP_Rp-OBLgqdrRVg3sneXLn1yozbnln_vqJ46W9rBUxFLtr1-s6tDywjfcZL6qSPYQdRqb45J8CEmcRXUEbWa8Oe4tk9X2RCxeQ2_mWx_OK9Jez3qX0d73ADSS3PLQoEj4enPsmC8DfLW7Q4uS1xQfPnzNS8cydK-os5b29ktOa7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن 0.7.1 از SenPaiScanner منتشر شد
✉️
😏
پروتکل‌های جدید
: پشتیبانی از
Shadowsocks
و
VMess
اضافه شد — هر دو از فاز ۱ اسکن تا فاز ۲ xray کاملا کار می‌کنن.
🧮
خروجی چندفرمتی
: با زدن
e
بعد از فاز ۲ می‌تونید نتایج رو به سه فرمت صادر کنید:
1- لیست Subscription
2- Sing-Box JSON
3- Clash YAML
🔥
تنظیمات سرعت
: فیلتر حداقل سرعت، تست سرعت آپلود، آدرس سرعت‌سنج دلخواه، و سایز sample قابل تنظیم.
🤖
ذخیره تنظیمات
: تنظیمات اسکن ذخیره می‌شن و گزینه «retry last scan» هم اضافه شد.
📚
پشتیبانی از CIDR
: حالا می‌تونید توی
ips.txt
، مستقیم رنج‌های
/13
و... بنویسید.
📱
اولین نسخه پیش‌نمایش
اپ اندروید
با Kotlin و Jetpack Compose اضافه شد. معماری MVVM، تم‌بندی کامل، و ساخت خودکار APK از طریق CI/CD(هرچند CI/CD باید روش کار بشه هنوز).
لینک دانلود آخرین نسخه:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.7.1</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/MatinSenPaii/3856" target="_blank">📅 13:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3855">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دوستان، این شکلی میتونید به من پیام بدید:
https://t.me/MatinSenPaii?direct
اما از اونجایی که دایرکت به شدت شلوغه، و من پیامها رو اسکرول می‌کنم پایین، ممکنه گاهی اوقات زده باشه سین شده، اما من نخوندم در واقع</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/MatinSenPaii/3855" target="_blank">📅 12:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3854">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حقیقتا MiMo اگر پلن پولی بده، خودم اولین مشتریش هستم. توی تسک‌های متوسط Backend شاهکار کرد امروز
هم توی سرعت
هم توی دقت</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/MatinSenPaii/3854" target="_blank">📅 12:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3853">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">هم پشتیبانی از Trojan و Vmess و Shadowsocks اضافه شده
هم تشخیص ISP
هم تست آپلود و شخصی‌سازی تست دانلود
هم WebSocket(که بهتره On بذارید)
هم هسته رو به کلی بازنویسی کردم
و این به کوشش دوستان عزیز برنامه‌نویس دیگه هم بودش که اسمشون توی Release note میاد و contributer پروژه هستن. من شاید 20 درصد از این 10 هزار خط کد که اضافه شد توی این ورژن رو نوشته بودم</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/MatinSenPaii/3853" target="_blank">📅 12:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3851">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fxjqnARdFcwrWmwQRV5JpXN93ntGCKH6u5RzbSmTKzDkHPSB31PrBgf6kowGJ5fdiG0x8mBtTFYo9DfXwtfKoxswawpmYAwYU6ichKrhMCfXhtzcSORY_ThoWlQFL3O9Bh9wFqt2HMcTAj9ZrbxjQFOEeApwt9FhsjnbQmTxygZY_FEwQ17ilH0XFzRHoouNfJc52YbQP-kWezkLDxwcxrRR-X48pfGWLHXi72vgWNQLvHytt_t1DTFQCRJ5jnzG8sRt-ta85rnhBEj3rkSDrtSWXwwNPJiIyHhRdxWl2vyTVFmItqAdZyxRU-ykes0AG8IOKqCvcWNkIqjp3y0pVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J97PDDccEdKLR4aEi_d3MIW8hu48tH5KCOZYJ4RyCFzT-9huM9D4PiYoEJbvGNvvOqT1fa5GMHt81kbb1YIyAfTPIlbnDJGurP8AzQmsRwTelpqhTmJb93LoqCq_zt3QN0QJ0XTPwUG0g6sQJjMOLReRDMM_dmmMdWF7L6Ea5jdw1yhRYxrZv8Qf4rZvo-k0wbvm9guiiX-ZkuAogQ-_2-8gz46smgpdmWCyaVbiQK6XdXPT-73ScOYbFL8xUnhzxZKn65-fYyu_Xnh5X2RGi-glhZ39aRGyf83jBNLfWPEhohcpCw8EiO4d8_Xm6vrvz0NlXXQfAoiD_2XESRpwog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بازخوردهای خوبی گرفت این ورژن که باعث خوشحالیه
❤️</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/3851" target="_blank">📅 11:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3850">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kKNf20FRsEK8g6-U7Xb0-xgmvQiRFD11W3StwEd964jA4R_s1ZKFT_ua6DvMn6JygLdEPkAsyg6e3k-k7eJdBhsmo2-x-UC-k4YcwJzta7DuxEsJHDfVTODa_O2jz4rCpgypkW6rijv_LwjEyrPBi33LKDps1FO-CkXAemZcHk9Kvfee38cYljz81_XYOUORIPL4uPj3yURPMu0lXMW7kQwizWUZpFCNWwxldAttkWg014iYqjs3tD6UhdSonEF8Hg8_dILvT6iSB6Fs6Wxp9SjDBor3fsEVFcYtAStQAJjBGNgoHL0ye_LGaqmTLOHkfAilMF5uZhHaLUaugHtYiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازخوردهای خوبی گرفت این ورژن که باعث خوشحالیه
❤️</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/3850" target="_blank">📅 11:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3849">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/3849" target="_blank">📅 11:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3848">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BmkCBw-rzSrz-AYCClScHAb9vhHa7zSAMnotQywDWf-M92MPXqO7LSGJBUmocd_-AYri0b-1BFbqHIxRFQhEjaplE85_LU4FWBz_0cQvjtuUjBAqTsdCFm4fZjW__aSkkeHqimPILwRJoCkm1I7PL0ochBsJcmSQRBe7wqUfFd4uu7Ebbzw5xRljn6MCzhFus2q7gdrHvFvLSnz5VPWpvw8pb30GbHu1fReTdQ3h5DnHoE1u9bQLlxVQrvjrZEaeg3wAk9fb-X8pR0CKoe3KThINA5I6vi0LI15im_zTBWwWts5OjzHeANwPssF8gbyxuDc0hMolAuxcAoc39kWFtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان خوب، لطف کرد و هسته‌ی اندروید و تمام چیزی که برای ورژن اندروید نیاز داریم اد کرده، صرفا منتظرم که خود اسکنر عملکردش به بهترین سطح برسه، اون موقع نسخه‌ی اندروید هم بیلد میگیرم</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/3848" target="_blank">📅 11:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3847">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نکته‌ی خنده‌دار اینجاست که دولت آمریکا دستور داده دسترسی به این مدل‌ها برای هر فرد غیرآمریکایی (foreign national) — حتی داخل آمریکا و حتی کارکنان غیرآمریکایی آنتروپیک — مسدود بشه!!  آنتروپیک اعلام کرده که چک کردن ملیت کاربران به صورت عملی ممکن نیست، بنابراین…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/3847" target="_blank">📅 11:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3846">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/3846" target="_blank">📅 11:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3845">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/3845" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3838">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">32 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3838" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خب، دوستای من هستید یه تست از اسکنر ورژن 0.7.0 بگیرید؟</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/MatinSenPaii/3838" target="_blank">📅 11:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3837">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خب، دوستای من
هستید یه تست از اسکنر ورژن 0.7.0 بگیرید؟</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/3837" target="_blank">📅 10:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3836">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HBCcsho9T9kPbwBACDVfOQb98963i1yHXaXxic4eHSTzOy1bKZJ4rtGMiYICa8RTxI70XNr9iBclvswhEOASBVXQs1Ng89DL6h3MPxcBCx-hHSYgtIt8lZdWhOM3d-Yvzkq4LpD53AC5N9oW1tLvh421n2b-QX_fD8rjLh4BLz8COn5iFg_Ip74_6-vrNas76g1AeriWpOTUBCy1tesNV5K8gFsX2U0ZP-HH51bGWfaitV_ihAcRSYj3DB6wBMc3JYBZOITSa_cYR82iDF2SMrPM0HptFnNZ0IE943NvzhEwIVjTzpWWXRLGlfhPDCAXthHpDM_i49eITu_G0SRG_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لپ تاپ اوکی شده الان اومدم تست کردم MiMo رو و خوشگله یه تست پرفورمنسی بریم باهاش روی SenPaiScanner</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/3836" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3835">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hwaJ50_NsGEye1DJ3-UiaGjVj579dvn1ZIckqHdwmDLXVYn2EacTKaV1WztXdv4NgU9t_BzWgdkZmWPH6FzqXaSlnwTPoBfAg9NCAwZaAqhR24KM0ZnoP1kCLgltC_Iva5Noc-mdZtq1fO9PBcaacKbTDnTzZZ2MjvKZ7HLd8_BL0MatTh2bUDOcXw-nofLK_KQ7qxCtNvzcMNpu8aOobhhBoR_x9waN1eQM0DcB6aqNilwMwGldpYRiS0S2C5rER56wmikawXD3lSgkkQ_MkAMkHA_viaGyvaoeBihkyoomTW2nieBV5T3_EwidgA3Xdl3mpEs1chAFfc-yq5IYog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد  توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش فورک OpenCode هست!).  خلاصه‌ی ماجرا: تیم…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/3835" target="_blank">📅 10:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3834">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">برگام! آنتروپیک به دستور دولت آمریکا و دلایل امنیت ملی، دسترسی به مدل Fable 5 رو برای همه‌ی کاربرا مسدود کرد!!</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/MatinSenPaii/3834" target="_blank">📅 09:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3833">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lUc0DDE6A5WRSe2xM4dRPcTcgeqyFjIoWJNHeY7VoQz8ZBLizMCzXrtOGH8aAJgMvY2lCn4EQ5nj2ykxA2GUzCFjd58VuMQSQ7A6ZG-SNcb4CVJV-OCPvIxLoWfwgQ6pg8WVD8zT4O8YDpRLvUcByAJGsmRqbL_hKStykF-aGSWzapuAPudwsCdXPIda6ZJDZbeaN-BKr52edHRRlXz6sopBEPtoTW05CReNaTtkbs6X9uOjP2_AqFP_TalFxVVZu60S6nANMMuRQHlErhz1VEI_qFXe6ecCF_Iiu_7NUvCvzD-Ex0A42hJOSXE4tQ13Nu8NuAghvSyrbGzDNb6U7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام! آنتروپیک به دستور دولت آمریکا و دلایل امنیت ملی، دسترسی به مدل Fable 5 رو برای همه‌ی کاربرا مسدود کرد!!</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/MatinSenPaii/3833" target="_blank">📅 09:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3832">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">این سایت رو یکی از دوستان معرفی کرد برای دامنه‌ی رایگان، یه امتحان کنید http://l53.net/</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/MatinSenPaii/3832" target="_blank">📅 02:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3831">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FXXE6QJrRya78igF32dRx_JR-5aFxU2_SY6cAHx8mJ7EmDu3xarz8Hs5VyYLs8nKwq4amXk5rdmavpJW7Lf5l6eV7bBgQvZXBlPKNjhi_x6lIxOsyDjM8w3_d7rv4tWBve_DKo8U8gFJwo7xpqVfGLqUXvVFP0Ar1cjireJJAByfvA4IU0NIh9kkRzDI_Py1XC3QpgSwRs9OoWEQ6PAa0qZIGk4BZ7_AB5rhOpTASSbLrVzrKecmCtlb90UD-S0rypZs2P0C10bVbHNxy1G7I_mm4_mitYvgDsuZ8TRddwfRNtbXBQobQ4SUGxcQMZwCpsJFaY3-139eNOlB2mfvPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت رو یکی از دوستان معرفی کرد برای دامنه‌ی رایگان، یه امتحان کنید
http://l53.net/</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/MatinSenPaii/3831" target="_blank">📅 01:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3830">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">من شرایط ضبط نداشتم دوستان. یه مشکلی هم برای لپ تاپم پیش اومده که باید بدم تعمیر و ممکنه کلا مادربوردش بسوزه اگه روشن کنم ترجیح میدم ریسک نکنم چون دیگه پول ندارم بخرم
😂
تعمیر شد، آموزش‌هایی که قول داده بودم رو ضبط می‌کنم</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/MatinSenPaii/3830" target="_blank">📅 01:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3829">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWireguard Configᵛᵖⁿ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=vMJtTwqLazRDtKlupNdIwHCfMUQuoGGcl7XhcOdfYn4UdxLi2HZTbDR-F3DlTjNa1c7_EGkeJxICayrJLmh2XNVDcTo5nwJZjwcJrXjSkDYxe_CQYQ6K11TwL6HFhji1cacgSvzpMLnWtna0hNocryoqkh1Paqbq7_yncZB9NowUDAkpfWorkGuRwOw3MPwUHyjmvPAN6q3BWmBRwlCOWNHTMP9olodlthqL2RlMF9ZeItY4xy4QSdCwPw5IuM4-0eZ2FunGXWDixmVp10fo7qtq97gQ0ni3-RDFpLhGhSjXof8SzYmOeprHtSgw87ceON-LMcxucG4R0Up4z2U7aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=vMJtTwqLazRDtKlupNdIwHCfMUQuoGGcl7XhcOdfYn4UdxLi2HZTbDR-F3DlTjNa1c7_EGkeJxICayrJLmh2XNVDcTo5nwJZjwcJrXjSkDYxe_CQYQ6K11TwL6HFhji1cacgSvzpMLnWtna0hNocryoqkh1Paqbq7_yncZB9NowUDAkpfWorkGuRwOw3MPwUHyjmvPAN6q3BWmBRwlCOWNHTMP9olodlthqL2RlMF9ZeItY4xy4QSdCwPw5IuM4-0eZ2FunGXWDixmVp10fo7qtq97gQ0ni3-RDFpLhGhSjXof8SzYmOeprHtSgw87ceON-LMcxucG4R0Up4z2U7aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سا
خت کانفیگ Amnezia VPN
• صبرکنید ای پی ها رو لود کنه
• بعد یکی انتخاب کنید
• تیک فعال سازی پارامترهای امنزیا 1.5 حتما بزنید
• بزنید روی ساخت کانفیگ Amneziawg
• دانلود کنید وارد کنید داخل Amnezia VPN
• میتونیدم کانفیگو کپی کنید + بزنید بعد insert بزنید کانفیگ اضافه بشه
🟡
فعلا روی ایرانسل
💯
جوابه(همراه اول ،مخابرات،سامانعلی)
📍
ای پی جدید هم اضافه می‌کنم
https://darknessshade.github.io/Amnezia-VPN-Config/
@ConfigWireguard</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/MatinSenPaii/3829" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3828">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کلا فکر کنم ساعت از ۱۲ میگذره دکمه‌ی بمبارونشون روی سیریک گیر می‌کنه</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/MatinSenPaii/3828" target="_blank">📅 00:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3827">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BYIMhXvYjAIEo-yCuRD0vaOIFwJ-vIJtZGGY4pXN3OpMiC1WYBSwB_KgeagZLkolx31KE_Jqx2ZbRjVlnF1E5yFrvnv0-bTAQF2PcyBtXErqFkTsnrBuhZ-JnA2nopgEGo4Efj614yik9pCetubOy2_6XjW1eUAla5RFRLeQo8uTuMP90izZRStHskwmyqSVVzVVjKb2bm9M7OEOm1zlPrdsrkruLhqdsydKRNN8mXo5Lijgrz-3vt9OWnBbWqTmpLNfOwAjlLj7LiC8XTkkoKGMGjwLlOGPYxEA7imgH9nHrplIv3uangznKtypJY0H_VaSNR3k398CzXtKh-968Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد  توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش فورک OpenCode هست!).  خلاصه‌ی ماجرا: تیم…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/MatinSenPaii/3827" target="_blank">📅 00:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3825">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اگر مشکل باز نشدن توییتر با پنل BPB دارید، همونطور که توی
ویدئوی تنظیماتش
یاد دادم، NAT64 یا ProxyIP ست کنید. اگر باز هم نشد، صرفا کانفیگتون رو عوض کنید با چندتا کانفیگ تست کنید، درست میشه.
proxy chain هم صد درصد درستش می‌کنه.</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/MatinSenPaii/3825" target="_blank">📅 21:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3824">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lgjjmuxgpzUPvNmtdxs498qT_omXX6nZB9baPhmKMlWvH8VOnlBq9uGPzDFTuDyZ6TPaiviRlDSPEuVNPOG-RbuoL-pfKfdSQuP1amYQdrjY2lhGZyiJ4RFWTN7d3ycveEvszRajnYon7b16M9KjhF9qZVrbZLhzwLjFY7CN5uRufv2JHtWnMQBp0LwQBOqmK4Q1Ch9xqwgZ06I3iF9VQ4o-sSEwSu1iLxVs2ZeRbcSzSllgR5xOB9PbLmuD2y98zQb4wbHkVHhV6QdUDcQqAyJLa_SUbYb_J3sRx5eZ3t8t9fjriSjys2Oazy2Umo584nAS_UB-r5LwjEjsard78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد
توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش
فورک OpenCode
هست!).
خلاصه‌ی ماجرا: تیم MiMo شیائومی به‌تازگی، دو روز پیش (۱۰ ژوئن ۲۰۲۶) نسخه‌ی
v0.1.0
از یه
AI coding agent اوپن‌سورس
با لایسنس MIT منتشر کرده که توی ترمینال کار می‌کنه و برای پروژه‌های پیچیده و
long-horizon
(بیش از ۲۰۰ مرحله) ساخته شده. این ابزار فقط کد نمی‌نویسه؛ می‌تونه دستور اجرا کنه، با Git کار کنه و در طول جلسات مختلف، درک عمیقی از پروژه‌ت رو حفظ کنه.
از اون‌جا که نسخه v0.1.0 هست، طبیعتاً یه پروژه‌ی اولیه و اکتشافیه — ولی معماری‌ش جدی و قابل‌بررسیه.
ویژگی‌های جذابش:
۱. حافظه ماندگار (Persistent Memory):
برخلاف ابزارهای فعلی که فقط به context window مدل تکیه می‌کنن، اینجا یه subagent جداگانه (به اسم checkpoint-writer) توی پس‌زمینه کار می‌کنه و تصمیم‌ها و پیشرفت رو لحظه‌به‌لحظه ثبت می‌کنه. حافظه روی
SQLite FTS5
(جست‌وجوی full-text) ذخیره می‌شه و توی فایل‌هایی مثل
MEMORY.md
،
checkpoint.md
و
tasks/<id>/progress.md
نگه‌داری می‌شه. وقتی context پر می‌شه، خودش از روی آخرین checkpoint بازسازیش می‌کنه؛ یعنی دیگه نیازی نیست پروژه رو از اول یاد بگیره.
۲. ویژگی Dream و Distill (خودتکاملی):
دستور
/dream
به راحتی جلسات اخیر رو اسکن می‌کنه، دانش مهم رو به حافظه پروژه منتقل می‌کنه و موارد قدیمی رو حذف می‌کنه. دستور
/distill
هم کارهای تکراری رو پیدا می‌کنه و تبدیلشون می‌کنه به skill یا command قابل‌استفاده مجدد. هر چی بیشتر کار کنی، بهتر «پروژه‌ی شما رو می‌شناسه».
۳. قابلیت Max Mode (آزمایشی):
چند راه‌حل موازی تولید می‌کنه (best-of-N) و با یه مدل داور بهترین رو انتخاب می‌کنه. که با
experimental.maxMode
توی فایل کانفیگ می‌تونید فعالش کنید.
۴. قابلیت Goal Mode:
با دستور
/goal
یه شرط توقف تعیین می‌کنی؛ وقتی agent می‌خواد متوقف بشه، یه
مدل داور مستقل
چک می‌کنه که واقعاً شرط برآورده شده یا نه — در نتیجه جلوی توقف زودهنگام و خوش‌بینانه رو می‌گیره.
۵. ویژگی Compose Mode:
با زدن کلید Tab فعال می‌شه و یه workflow ساختاریافته برای توسعه مبتنی بر spec ارائه می‌ده — با skillهای داخلی برای planning، اجرا، code review، TDD، دیباگ و merge. کل چرخه از spec تا کد نهایی.
۶. ورودی صوتی، Git و Multimodal:
ورودی صوتی real-time با
/voice
(بر پایه MiMo ASR و TenVAD، مخصوص کاربران لاگین‌شده)؛ مستقیم با Git پروژه‌ت کار می‌کنه و multimodal هم هست.
۷. سازگار با Claude Code:
authentication، skillها، MCP serverها و دستورهای قبلی رو توی یه مرحله import می‌کنه از پروژه‌ای که داشتید با Claude می‌زدید.
۸. انعطاف‌پذیری مدل:
MiMo Auto به‌صورت
رایگان(1 میلیون توکن اگز اشتباه نکنم) برای مدت محدود
و بدون کانفیگ در دسترسه، ولی خودش هم از هر API سازگار با OpenAI و prov/erهایی مثل Anthropic، DeepSeek، Kimi و GLM هم پشتیبانی می‌کنه — یعنی vendor lock-in نداریم.
نتیجه؟
طبق ادعای شیائومی، توی بنچمارک‌های SWE-Bench Pro و Terminal Bench 2 (به‌ترتیب ۶۲٪ و ۷۳٪)، با همون مدل پایه حدوداً
۵ درصد
از Claude Code جلوتره(که هنوز بعید میدونم. به چینی‌ها اعتماد ندارم). اما می‌گن تفاوت واقعی‌ش جایی خودش رو نشون می‌ده که کار طولانی و چندمرحله‌ای باشه — نه «له کردن»، ولی برتری معناداری توی long-horizon.
نحوه استفاده (خیلی ساده):
۱. نصب یک‌خطی (Mac/Linux):
curl -fsSL https://mimo.xiaomi.com/install | bash
(بهترین تجربه با iTerm یا ترمینال VSCode)
ویندوز:
npm install -g @mimo-ai/cli
۲. اولین اجرا:
خودش راهنمایی می‌کنه — MiMo Auto (رایگان) رو انتخاب می‌کنیم، با حساب شیائومی لاگین می‌کنیم، از Claude Code Import می‌کنیم تنظیمات و... رو، یا خودمون می‌سازیم.
۳.
می‌ریم تو پروژه و کار رو بهش می‌سپریم (با زدن Tab بین agentهای build / plan / compose سوییچ می‌کنیم).
لینک‌ها:
- گیت‌هاب:
github.com/XiaomiMiMo/MiMo-Code
- سایت:
mimo.xiaomi.com/en/mimocode
- بلاگ فنی (درباره long-horizon):
mimo.xiaomi.com/en/blog/mimo-code-long-horizon
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/MatinSenPaii/3824" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3819">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RzG4dMPI8wXQED4EixlBPwSXByK4-UFOJom2e71b6sIq12opmuwYIpwTyAbacekJUVs6BylpdiEAXCm03QChcaxB1lRg97maO7B81uFU_LNFI67YbUu5k5j_dL8p7kTUpXz1USQE7g6wwYZ4DJCWG5YmeerLTFO9mIZHRvK-GRl4_CVOuCmMFpkUyup0y0YV-ELE5yABxgfSI_sRbvZ1ECHCICZ_1tXsqIK95Qa8rMNL63kbQLlrFeFNcoOh1Tsm51tQcMcCwUwbD8qFfV4qNU2BIouWvXDdreJVFXq9WJc6Ubj_XQ8nurkzN7VhQuUqvoerptQKr_btbUaSnk6OIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از ChatGPT بپرسید که
یه عدد بین ۱ تا ۱۰۰ انتخاب کن
بهتون به احتمال زیاد میگه 73! علتش رو هم از خودش پرسیدم:
وقتی کسی می‌گوید «یه عدد بین ۱ تا ۱۰۰ انتخاب کن»، من واقعاً عدد تصادفی تولید نمی‌کنم؛ بیشتر یک عدد دلخواه را انتخاب می‌کنم. بعضی عددها مثل ۷۳، ۳۷، ۴۲ یا ۶۹ به خاطر الگوهای آماری و داده‌های آموزشی بیشتر از بقیه به ذهن مدل می‌آیند.
جالب اینجاست که در آزمایش‌ها، وقتی از انسان‌ها می‌خواهند یک عدد «تصادفی» بین ۱ تا ۱۰۰ بگویند، عدد ۳۷ بیش از حد انتظار انتخاب می‌شود. مغز آدم‌ها از اعداد خیلی گرد (مثل ۵۰) فرار می‌کند و به سمت اعدادی می‌رود که «تصادفی‌تر به نظر می‌رسند». من هم تا حدی همین سوگیری را دارم.
پس اگر چند نفر قبلاً همین سؤال را پرسیده باشند، کاملاً ممکن است من دوباره ۷۳ را گفته باشم
امروز توی توییتر اینو دیده بودم و واسم جالب بود علتش</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/MatinSenPaii/3819" target="_blank">📅 15:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3818">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jhqTTtK5s3U8t2_9KaCAdG4KEXr8rcWna72K-MyPkPZJJye8G_M69alM0Fb7cRHf2A47KiyjTVvymRhtdqSlJaTsGu5D1G1gDWUQbzRk3qQGQLZDrTBBlGfUeB68ZvDXhPoBaN4M2DlOZGZXZm24kJcx1jwS94hnP0e4LP20aTvKykg_K7Hrvy9NyzNuKuplDR0uGayppzTlbhxZyXJOL8G_uIVNMDRBgZCWv_NBoIzi9h92H-yQmToPnXIp3dV9IxOQKxrR7iB20pELC4ereYAq489MOzoM7R4oo6DUYqNI9W28cZfd-NRqO-llTHYuDCwvzfXLrbFoGzWr7Oh0gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار باحال آنلاین پیدا کردم: یه عکس می‌دی بهش، بهت گرادینت میده با کلی تنظیمات.
برای وقتایی که دنبال یه بک‌گراند یا پلت رنگی هماهنگ با یه تصویری، عالیه.
تو مرورگر کار می‌کنه و رایگانه
👇
photogradient.com
‎
✍️
Reza</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/MatinSenPaii/3818" target="_blank">📅 14:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3817">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا
ابزاری که امروز معرفی میکنم...
داخل این سایت میتونید تمام ip های مربوط و بنا بر نت خودتون چه برای ورکر و کلودفلر یا شیر و خورشید اسکن کنید
❗️
ویژگی ها:
💡
اسکن راحت و سریع و دقیق
رابطه کاربری خوب برا همه سیستم ها
داشتن ip بیشتر cdn ها
لینک سایت:
✅
https://cdn-scanner-pro.vercel.app/
توسعه دهنده
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/3817" target="_blank">📅 12:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3816">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2658a29175.mp4?token=AB97TweclElDQ0migKHRsXBwqSVoAfZHRNEVH8feqZRl7iOXNfmuxBxm7gEy5ohKjz4qgX-Evmf9n0Tm4zFRMq9bftPMYVZNl-2gpcPiuoUIgVbwLz0ZlL0RIw98gujUqPQIoUrz4SYezjhg90uKyw6o0v-cShZ7Sj4pgQ45Mwsmi91j1_lfSob3CopJTb4x0pGfL8gnK-71FVZbNVpS9UZPJBlugS9PJXd5xZ4kEm4wjTd0l6JCKeHV2eQKL_EXGqYQlIrgdRSZG3pzo_4OWIiUEBE-wzoS5Wu_e_MuLzoviuzGLsL-UgRnBzRiwjCOtSvKkiZf9xCvUPk7q7hp-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2658a29175.mp4?token=AB97TweclElDQ0migKHRsXBwqSVoAfZHRNEVH8feqZRl7iOXNfmuxBxm7gEy5ohKjz4qgX-Evmf9n0Tm4zFRMq9bftPMYVZNl-2gpcPiuoUIgVbwLz0ZlL0RIw98gujUqPQIoUrz4SYezjhg90uKyw6o0v-cShZ7Sj4pgQ45Mwsmi91j1_lfSob3CopJTb4x0pGfL8gnK-71FVZbNVpS9UZPJBlugS9PJXd5xZ4kEm4wjTd0l6JCKeHV2eQKL_EXGqYQlIrgdRSZG3pzo_4OWIiUEBE-wzoS5Wu_e_MuLzoviuzGLsL-UgRnBzRiwjCOtSvKkiZf9xCvUPk7q7hp-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیگما یه اکستنشن کروم منتشر کرده(فعلا برای کاربرای پلن پرو) که با رفتن توی اکثر وبسایت‌ها، می‌تونید با یه کلیک، تمام اون صفحه‌ی وبسایت رو به شکل فایل قابل ادیت فیگما دریافت کنید.
برام جالبه که سر بحث کپی‌رایت و اینا کسی بهش چیزی نگفته هنوز
😁
اما خب گویا هنوز با چنگ و دندون قصد دارن نگه دارن اکوسیستم فیگما رو بعد از اون سقوط سنگین سر Claude Design
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/MatinSenPaii/3816" target="_blank">📅 11:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3815">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏این روزا اسم Agent Harness رو زیاد میشنویم، ولی بیاید ببینیم واقعا چیه و به چه درد میخوره!  همونطور که میدونیم context window مدل‌ها محدوده و اگه به صورت کارآمد ازش استفاده نشه، خیلی سریع پر میشه و مدل مجبوره برای ادامه، یک دور summarization انجام بده.  بعد…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/MatinSenPaii/3815" target="_blank">📅 10:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3814">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IIeSYIitMw6p1Pr1LQ_wD6yjiiSHFeqO1I_l3JYVxmAD41S4WnHHN6pbMopa_rM24YrTrfVxdUheWGjsyHYlSNdmvkfxehXGv4Qua8byY01AfpVmLsXvgni7r0gJxp3IBeR3IWDE-fzKAFyZ5hqYoZhaVKm6qha4Ngei-1u_xPwVCliwPOJ2i-URourWRVEbdEc9XA2mXzlP3My4wK0mYE0kh2-aajOBskzF7B8tdKI5GhPpRMi8WRBybbCy4XNjLDujBeKcH1EN0VCYEDc0IvQAuZ_S9W3AnwLrLvoMeFpfeAiscN3jyZWl4LfL2ilfAehfISp3XDF7gG5Lgz5fXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏این روزا اسم Agent Harness رو زیاد میشنویم، ولی بیاید ببینیم واقعا چیه و به چه درد میخوره!
همونطور که میدونیم context window مدل‌ها محدوده و اگه به صورت کارآمد ازش استفاده نشه، خیلی سریع پر میشه و مدل مجبوره برای ادامه، یک دور summarization انجام بده.
بعد از چند دور summarize کردن، نهایتا بخشی از دیتای مهم از بین میره و تسک به صورت کامل انجام نمیشه! پس اومدیم یک سری تکنیک پیاده کردیم مثل تقسیم کار بین sub-agentها تا از پر شدن سریع کانتکس اصلی جلوگیری کنیم.
بعد این ایده مطرح شد که بیایم هدف نهایی (PRD) رو تعریف کنیم و اون رو به تعداد زیادی sub-task تقسیم کنیم، بعد مدل رو در یک loop بندازیم که با هر بار اجرا، یک context و یک prompt جدید داشته باشه و بعد از هر iteration چک کنیم که تسک به صورت کامل انجام شده، و در غیر اینصورت چرخه رو دوباره تکرار کنیم!
در واقع به جای اینکه برای اتمام تسک به مدل اعتماد کنیم، ما در یک لایه بالاتر این رو validate میکنیم و اجینتِ تنبل رو harness می‌کنیم :))
✍️
Amir</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/MatinSenPaii/3814" target="_blank">📅 09:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3813">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FyHAIZv98FXMmdJRJB5DQ1Tw7LXHdiwI_yybtE_sfJQrBC_KwWXWM5029HG0zZodhRjCGQF-s2ZlDXnjIFgXS7aMerkAdgy5AMzbq86UxSYuRww5bdfg3oOK7IT7uFbF3hQvgPIa8_yd3rzai2KrqpaO5Y16ofeHRlaISvYdoLTZWGlZJXeZ14wAAcpCIMYtVvT2p9YyTG49Nlals5V-lYIFSFevEfKaM1HoNLxAomiAk-Z-IshT9y6XadPKXuVGB0f_JexvIqOeUQ48gbVs-zAIYt533gGFUGJosOLIUbUmn3CbTvjN7ZRq-eEVuB0_nGK5GLOQlR51HeRWW0wiFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله شما می‌تونید دامنه و سرور خارج رو از سایت‌های ایرانی هم بخرید، اما چندتا نکته وجود داره:
۱- احراز هویت سایت‌های ایرانی کلا جالب نیست و خب این ریسک رو باید در نظر داشته باشید
۲- توی شرایط قطعی، فروش دامنه و سرور همه‌ی این سایت‌ها میره روی هوا
۳- شاید عجیب باشه شما اگر از سایت‌هایی مثل netlen و با کریپتو خرید کنی دامین+سرور رو، شاید ۸۰۰ هزار تومن(با کارمزد و همه‌چیش) پات بیفته. اما همین دوتا رو از سایت ایرانی بخری زیر 1 تومن نیست</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/MatinSenPaii/3813" target="_blank">📅 07:01 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

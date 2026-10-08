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
<img src="https://cdn1.telesco.pe/file/ohI3TyLOooGsifbWymmLPmItoN6a48cYAjQNru9uK5WzehODluKK7Vz5djf_4-zZS3dd6gKFnxsR5bCLoDEkN6T3jaZgMI0B3kqgDkZro724K2nKpx_CoFe_iPTG1OWwJrjG0WxaAixiqXgWNDL0KcneJrJ5Y70ZmVbbFzAuDNW8nku4gDNQhPZg-DDXdsKXIKOvKTOuS0Zy-xxP5LIy-OHgeXMXgR11WjegeI1Oo72Kh-pI0emQm8rEM1pLoxlLvYT4INsUQGFt4GqpZN0lvCbiS-QiE3DVloe7mmDZHdpTi5TwHYHwBheRhXuqadjtlHs5O0nSBe8YnS_tIMgL9Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.9K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 20:10:43</div>
<hr>

<div class="tg-post" id="msg-2658">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fx6BtJ2025ybVafJI-O2imMV6dg_A09-eawm1P8KtfGJqEq9I7TsxRiRCX9iEy6MTg9isfWFklLOdLTqb7WF9_EnG96qw6zDNOdU6yQoY654UqjAVxN8tpYjmRA9nzpEHJlTTngKoUWD2d17fbk8NILd9oqaYHf44NpBbDlLVRTnEFDOVF4RiLitaoPXAh5vML3g5a9fiInZ8lwVblWfBb1Ei1TUuRX6AiFYNujD6aIH1MPJB1AW6Th4XC0ajhbueqX8F4a4nli2qvwk0G0dDrUyEZWBdaw1pY5OGV93SoV-9WJYH83EB8FLmuPb1b-hHsyIPjmnoe4YGmA2ySOSSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروه Void Verge مدعی شده با توجه به تغییراتی که دارن توی شبکه ایجاد می‌کنن، اختلال‌هایی که روی اینترنت و همینطور اتصال VPNها دیده میشه و مهمتر از همه خبرهایی که به گوش میرسه،
شبکه زیرساخت برای قطع خیلی از پروتکل‌ها آماده شده و فقط منتظر مجوز برای اجراست
!
روش‌های مبتنی بر کلودفلر، ایکس‌ری، سایفون، DNS و حتی تور جزو روش‌های اصلی اتصال فعلی هستن که فینگرپرینت شدن. تجربه جنگ‌های اخیر هم نشون داده روش‌هایی که عمومی شدن، زودتر شناسایی و مسدود میشن.
این گروه معتقده در چنین شرایطی به جز استارلینک که البته دسترسی بهش محدودیت‌ها و چالش‌های خاص داره، به مرور باید پروتکل‌های ناشناخته و ایده‌محور جای روش‌های اتصال فعلی رو بگیرن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/ircfspace/2658" target="_blank">📅 07:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2657">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gcTUiTgmjn6_tWtC56TdpsRRvEZXxuiQxuEtoSd89zRIUCKN3Y0xlZvlH0YHYZu5g1fClYITkY0m4AdyLEjRRqnTW1e1MCynPst1GTrST0boqy6LIHwylLcP_jppwGW-PXCTIyZvtcxPYZHf5r_zF4p1RiLSibJZzpca2HvyGvoEreyHseBJp1AMd0mVBhYC8wShXPIGcFEf2DaguL5pheKhUiWML90eDVnDQCvGNAjVp_xmL-0KeTF6oXLJqWsQvEa5ILcIAaQdkA0suiTNDkUdmHev1L0eUCBX2qo-7Nig_1ISaESBohuiR5fmTYATlK3R_woCKnPFgUUOmHOSkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت متن‌باز و رایگان ZedSecure آپدیت جدیدی برای اندروید، ویندوز، لینوکس، مک و NixOS منتشر کرده. در این کلاینت از هسته‌هایی مثل سینگ‌باکس، ایکس‌ری، اسلیپ‌نت و شیروخورشید پشتیبانی میشه و در کنار پروتکل‌های DNS، امکان استفاده از OpenConnect (سیسکو)، IKEv2، OpenVPN و AmneziaWG فراهم شده.
همینطور OpenConnect روی دسکتاپ بصورت VPN سیستمی قابل استفاده هست و امکان اجرای زنجیره‌ای روش‌های اتصال مختلف اضافه شده؛ مثلاً میشه سایفون، تور یا SSH رو از طریق یک کانفیگ Xray اجرا کرد. روی اندروید هم قوانین مسیریابی میتونن بر اساس نوع شبکه (مثل وای‌فای، دیتای موبایل یا اترنت) تنظیم بشن و با تعویض شبکه، بصورت خودکار تغییر کنن.
👉
github.com/CluvexStudio/ZedSecure/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/ircfspace/2657" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2656">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rG2YckQjBjt5tKZjskMR8T87-iJgYrn4PSsUs_4tesONgvB1i3XXQfTmqpTx0zikyVXvZYvcBqpCosrCIzFv48W1bHAOTdBM_uYsf1OANRc3PTvZEDiWMZZ3BXESCrE6vbyRxvPJuMnIYJd3kw0I1O8PkVGnKLRP2Rkt5wtQ15l9ueraNZ03jqZelAqMEqqiRP_WjJrVYOOSLEhqtrlH87hieaRESRfFu6JyguYk0WU87hm8TC8G79B3f5k9Po7FbKM5ncbcqkEd1z9dgIUhtROGfaTX7CQ5YCmD7pzAlPAXxm7SXgtFMh5p8KOsZrSuR9eyNwTNEuONwvVxxF7rig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس داده‌های رادار کلودفلر، از ۱۲ مهر یک ناهنجاری ترافیکی در ایران ثبت شده که همچنان ادامه داره. ترافیک اینترنت بعد از شروع این اختلال بطور محسوسی کاهش پیدا کرده و حوالی بامداد ۱۴ مهر به پایین‌ترین سطح خودش در این بازه رسیده، هرچند بعد از اون کمی بهبود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/ircfspace/2656" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2655">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JZYJ_FBu-nqRzPzDiS_zbCuydac_0qHwOMLjkyxRU6tbZkL2tvy-JMJM7pMhgMcmyDgRA8nFYQZux9BwSKF0laNfo-nVtNOdLSiHjtik7nMFRvl6jFOEclQVYs7k4xQaDvsZFRFbKBe5vnH71A3Z4XFwthASi2G0TkWWKy-jqOoGK_SEuqTnnhzdoD7R1QtqExjHI6qxFSfRwYScEoRwTNNG7nMt3sYALWuNo5-BclEHgvraD7GuvutdY0DvM4VVnMHgVpNk5hY3JPPjP09X6Rb9CL5c4osFoWBr16W_JxnYSu_wj5m4cHZi7VmwEuR1mtTOHEQI5VEtbsvUXBSGYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه جمهوری اسلامی در واکنش به سرکوب اعتراض‌های دانش‌آموزی در فرانسه، سفیر اون کشور در تهران رو احضار کرده!
با در نظر گرفتن کشتار ده‌ها هزار نفر معترض دی‌ماه و ۸۸ روز قطع سراسری اینترنت در ایران، ممکنه فکر کنین طنز باشه، ولی منبع خبر تسنیم بود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/ircfspace/2655" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2654">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gQf9t16aR75P-UZWodcQnW5aCd0jxP44Teb86dwpqhDjfq3d0IdzpgKVjnY_TA-zXS7APD5GkIqQbNJIIJOlijuJt7spJS8VHU265TFaAI8NwzZzdVZu4zfozRkAXuC4633rC6zuwc2Vt7Fl9SA8IsqqWWQR4TkcfjcskRkg-5lrvj8FRznsoKOMV85YPY8yVDY2seLraoFwOp4dOfkHvm0Q6tSII_8Jv9EaKIu2bsn7qMvWVzoYsefwL3EzwfRWSfdKaXpxqPjkPMzTcK57q3UdZw1CTgM9EybLx4wPVXKb4xoewoWecNLz4peC1QARoRlL8vs7uLZt8rHqzjuJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از اسکنر متن‌باز و رایگان SenPai Scanner برای ویندوز، لینوکس، مک و اندروید منتشر شد، که توی این آپدیت قابلیت Anti-DPI اضافه شده و با تکه‌تکه کردن ClientHello (مشابه چیزی که در PattNG انجام میشه) امکان دور زدن بعضی از محدودیت‌های DPI رو فراهم می‌کنه.
حالت Gentle هم برای اینترنت‌هایی که وسط اسکن آیپی‌های تمیز کلودفلر قطع میشن اضافه شده و حالا می‌تونین آیپی، رنج یا دامنه رو مستقیماً وارد کنید و اسکن رو از فاز دوم ادامه بدید. امکان ذخیره اسکن و ادامه دادن اون بعد از قطعی هم اضافه شده.
👉
github.com/MatinSenPai/SenPaiScanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/ircfspace/2654" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2653">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شستا ۱۰۰ درصد سهام رایتل و ۵ کرسی مدیریتی این شرکت را به مزایده گذاشت. قیمت پایه واگذاری ۱۳۰ هزار میلیارد تومان تعیین شده که با نرخ امروز دلار آزاد، تقریبا معادل ۴۸۳ میلیون دلار است. فروش به‌صورت نقدی و از طریق مزایده دومرحله‌ای انجام می‌شود.
©
stup360
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/ircfspace/2653" target="_blank">📅 19:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2652">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fRtJJ1sc6VnFUA4I2o12aZTO3LivfmQ0tfD7ajuoPjMmXXHEiRtnwgXx_eWO7GCEhCw464SM6Me8WARiVbZv0nwfNV4aKbFygCG0KdUgTz0_LPMwOqM9ZOLDcw-rgxFFd8jN4Z1W1Zw7JKV-23twlxbIgrnERZscZYovruczh8H9tRRB9rgb2Jm-jdS2LZBksVImZ5sF6TwZuwSLFNQ5w1CcOSHGQrsiE6u6J92QwCTLimrnDhYdZLzNbNoP7iqKJkcSxfelLS5rt4i8oTGXvKyfI3kDRIQDWq-rg7jy10Z4QgmfPBOi96HQquX_1SD5U8-rCy4YGl4EpViKhy2a-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پترنیها در تحلیل وضعیت فیلترینگ ایران، جمع‌بندی روش‌های فعلی اتصال به اینترنت آزاد از طریق کلودفلر روی فایروال همراه اول و ایرانسل رو منتشر کرده.
بر اساس این جمع‌بندی، روی فایروال همراه اول میشه برای اتصال به CDN یا Worker از روش ECH با یک IP مناسب استفاده کرد. استفاده از IPv6 هم یکی دیگه از روش‌های فعلیه که بسته به فیلتر بودن یا نبودن دامنه، تنظیمات متفاوتی برای finalMask داره. برای WARP هم میشه از متد WARP-in-WARP در اتر روی IPv6 استفاده کرد و با اسکن، IP مناسب رو پیدا کرد.
روی فایروال ایرانسل، برای CDN و Worker میشه از متد F&F استفاده کرد که نیاز به تنظیمات مشخصی برای finalMask، cipherSuites و فینگرپرینت داره. WARP هم روی این فایروال قابل استفاده هست و محدودیتی برای نوع IP وجود نداره. علاوه بر این، روش MASQUE/H2 با اسکن IP و تنظیمات مشخصی برای فینگرپرینت و finalMask می‌تونه برای اتصال به کلودفلر از طریق هسته اتر مورد استفاده قرار بگیره.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2651">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/faXX3nwNjbnth2qfggENBVfYT5W1frQiEQip3yRExpxkMP3b-Mhe9FiAUHzzAw6KJ59sI7bRJEnKmp5-VuwsHk2TF4ucSUgYme2hnQ-Tvi9gsfWjfaHUnqO_gw5AiN-qvaVpP3lKiytUXm0CgeTyubbweflcuLHlC2ICh1ukQTfOB7ivALzVIXQn3jq_QbCw05tAfcfEcJ_IMUga4y8CM4PfWxiebj3-zwsFTCbGA4PtsBk5kB5oyyfl34CvDPuEFhecWPQl90QfRkpdwgZVXhcVLgvgX2Ly5lcj-ZYD4Lm8RVL6b8us-hWVyXXsoOZbTiGQ0ZD0HfddUx217gv6aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن دیفیکس توی جدیدترین بروزرسانی خودش قابلیت تانل‌کردن کل سیستم رو بصورت آزمایشی برای ویندوز و لینوکس اضافه کرده.
در این بروزرسانی عملکرد کلی تانل بهبود پیدا کرده، مشکل نمایش پرچم کشور محل اتصال رفع شده و چند ایراد جزئی برطرف شدن. این نسخه درحال حاضر روی گیت‌هاب و گوگل‌پلی منتشر شده و بروزرسانی مایکروسافت‌استور و اپل‌استور هم بعد از تکمیل ریویو، در دسترس عموم قرار می‌گیرن.
👉
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2650">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZsrKFKI84HOMUE2uXDaZmkADLjGna-3ut40CBxqrH9HPMHpx7uv2DoWEGDFXQAQV4Q0-iQRRRnUz0A2cfrTkcyW9dACwem_UxJd9CKV3j0vLNx1kFpxXi6CfuaMs9ky4lVlHmnUdcEZkqAbM1J0G70-3vIMLR9zh7Nwz7pWl-hH3gSH9rI50AuqWtmg0CMstrlHu88J5Q7ND-pjbyuCndFdg-bNGtbYzan_8cx2WtgSigS4ZopwSGRI-JwdCR7zntgJrZjTj23kMSK4bWargA9_G52DhjtKY4l5jMXkGEiLSoyQr8lwBgzEgghmZi-_GHpNcd3_bVj_8Mqd4DXvY6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای "قطع اینترنت کل کشور فرانسه به‌دلیل اعتراضات دانش‌آموزی" فیک‌نیوزه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/ircfspace/2650" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2649">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RBBU3d24E7eBRoO0csm1oKg2PAdzdQloMDZgR9EjP9Crl664TGLaGy5wbc8d2HE3aqoFTZdL6KjLuNMUrfZBsHcKKWuuikFURqrLXWQtJO34RzuwvPTuKLozD9yh9es2ilXHXrnmEOvWJkK38fMAEHOE-qiIJyndkgyDUNWnnWQk8fNNXoCPhIF44MWepdoGsWxW7sltqSX11r4Q_95Sgg2S4zSxVVK0lqPGKGUPLizV5xHutuSNWq3RyfCDBdQ17ttCPgvEH_-rhR0BoIHLF4YYDQECSqrljpJyOFDUyfZx3hz3jS8tVkWvT0f4KZjyyKU_D8unhMGQkrJl0KwKBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در جریان اعتراضات دی‌ماه تونست با جمینگ و GPS spoofing روی
استارلینک
اختلال ایجاد کنه و حتی تو بعضی مناطق کیفیت اتصال رو به‌شدت پایین بیاره، اما اینکه بتونه استارلینک رو کلاً از کار بندازه، دور از واقعیته!
اسناد ITU نشون میدن که با وجود این اختلالات، ترمینال‌های استارلینک همچنان تونستن به اینترنت بین‌المللی وصل بشن. حتی راهکارهایی که SpaceX برای مقابله با این اختلالات اعمال کرد، باعث شده سرویس در بعضی مناطق دوباره پایدارتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/ircfspace/2649" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2648">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qa61Ng2J1o-LIuG0x7OCCRXofejYgtVEmZv0cYNdc0nQVtE963Eca-Zg-6t-wOUxlPOr_8NzZWAyIjhilMYbDjWF0E44jbsMHOXfdJXLfRaPW3SKR_LoRiXdD489vzwkEITxXp7Bm_5JpTIUMeZCdg3MD9ek2URXY0oOu-75NFmRYrIIVNk9Ti-zNbkmurIdU5OqD604krpVHr5J4HaKDYtwNO5kc7p7kRdTTCI8LVbGDydQRBN26pPE8iMT5fCkbpBGuanY5mJo-gOso1bLhh0dyrRm2aUHki7fgtdqsEG3ZUHyYlNJNVlQekNEAjbQGdlLsZ57wqJ_SR_ht51aaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا: هر سایتی که اقدام به اعلام قیمت‌های کاذب ارز کند، باید بداند که برخورد قضایی و پلیسی با آن به‌طور جدی انجام خواهد شد. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/ircfspace/2648" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2647">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WLlTPzdhV1ZeYLVXdZMH89TeLvECAwyti7WLYP8p2QU7cUxjUa9Sifi2fJGD5FksgGZumT1RVD8mPc6MNneowkEGGKhYurI0wQqLhGCFze8QCBia5WK0XPEJ-KBTxcrKUsdPxdlMc4oNbikIeTOMfJkcoD_IoVFmyTDVwWeReM28V94WMEY5UsL-GXmgeU1Dr1fDuTQIb3_uxaXnvPSkExRLTZjSl1E2eYSItWBSJk1x4Ok3aVEPJ6wD0wlprmHsUSOGnwCN35YuXqDUBM83PKMpWvMca5p0UoxgaLQmRzFOl0Q2hrAD1ctnbTq8awq21NYCad5sQ-LOOEqQbRSs_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید از فیلترشکن متن‌باز و رایگان Aether-GUI با آپدیت هسته اتر به جدیدترین نسخه و اضافه‌شدن متدهای اتصال سایفون، تور و مسک‌این‌مسک برای ویندوز، لینوکس و مک در دسترس قرار گرفت.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/ircfspace/2647" target="_blank">📅 17:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2646">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cEFRE2xrQjsjd5fZq7EHco55q_qcJHfe6K3d-S1ahyEXf7wNKYjeNSppuy4dJwdquxuABTMX6PdcVqy8knbb_NyoLbgZGjpq_niFt6vX82UHVzRuwcD2GeG7KGdeR4YbLz5wDjXx-4fiUfgkfQ1rP_vRRn46sVIkp5FQMxTZYKlbS9F6cnXh7HgpeW9Ov0tmQawGZHcy7hqEnarfxxBAsDlTuD5k9ucQEVlD9Lrepe0BOxN_OKE4leFTBvqOlGc4GCqOmAsS1ir1BUi2fQXFPDN5pIBn_KvcbZxxQ8rucNuL0fOcL4TJfxBEC893Eh0X4hlwrVfV9Cc4_9hYOc1f3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مرکز ملی فضای مجازی گفت: ایران برای اولین بار توانست با موفقیت پایانه‌های استارلینک را در جریانات دی‌ماه سال گذشته از کار بیندازد. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2645">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S-crmhv1lG4H7jBuMB6tdPMkf2ER1YHTMNuKsEwaTaPq8eemnE-2wieruLEwVoh7CE9TGrKxE9OLfq9z9WkXBvw50zYufi2fcbNJ98CxWzfjtCC2DfUcsj6DCSgn_tLyT9h0yZ1nF_dtkQlmR4thK4g3uoOOYYX4ElSoFUhRN0lw5bGq1canlkKoxp0cdRCUgyv9g2mIWJ8vVs0-jKv8n-RVzkXOE908Hxuq0eZtmRQ1SrFEr13ifd1M5c_64yDFyC4FjcYxSzCveRwwclVgJSjowF90FvOnyWdjJtwJChJdSWVmErqbsZJGImJHeJi7AJp_LwDfjCqruPnzU-cynw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زومیت در گزارشی نوشته که در حال حاضر دو راه رایج برای دانلود فیلترشکن JumpJump وجود داره، که یکی از گوگل‌پلی و دیگری در گروه‌های تلگرامی هست؛ اما بررسی کارشناس‌های امنیت سایبری نشون میده هر کدوم از این جامپ‌جامپ‌هارو دانلود کرده باشین باز هم در خطر هستین. فقط خطر یکی بیشتر و اون یکی کمتره!
جامپ‌جامپی که از گوگل‌پلی دانلود نشده احتمالا یک فیلترشکن دستکاری‌شده هست و به نظر می‌رسه این فایل یک exploit یا آسیب‌پذیری قابل سوءاستفاده داره که می‌تونه دسترسی root در اندروید بگیره و رد پای دولت‌ها در نسخه دستکاری شده دیده میشه.
حتی اگر نسخه کرک‌شده رو دانلود نکرده باشین، بازم برنامه اصلی دسترسی‌های نامتعارفی از دستگاه می‌گیره که نشون‌دهنده ناامن بودن این فیلترشکنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2644">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lCWhfa3iXBqS-bZPkntonQ31JXo7xCr29krKuGare6joWPlt_Js_6WlpcyjZBdwxnGqRWoHw5e_OoXzEgJEsLQgx4MEf9XIQ1cgbOeMYDWtgOwEg7VjJ3leOT4Chmuskq7kn1QyvBnUFONy-RpNMPfQ1mLHxCA2Uot-otn4YWKQJttcByuhpHQdX-w5IKD90nK2ilRQ-0BEFkjvXerezGYjQK1BbGDyJ4Xg9TUagUDM6Mp5PDt7VLYsJLNuZaT84BLWnobtW0Z0ksK5RBamldxKh5JyJ0VlKLBv1v4fGqQID7fYK8lkOT65eQ0JrAToF43Vz5BkCc_Ek6vs6Fb3v_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از اپ سایفون چندروزه روی اپل‌استور در دسترس قرار گرفته.
👉
apps.apple.com/us/app/psiphon-vpn-secure-access/id1276263909
💡
play.google.com/store/apps/details?id=com.psiphon3
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2643">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lGqMrxMqQMCBwnI0bFPTTCt-Vf5XflV74Be_frAEr_wQsejLGWabksRg_xXk-phnbIBH4Ec2ZOAK88ufOwhNN6R_5vz_Cl9KLbDw4dXjwsliIY2qltBQzdSjrxbAuW7qpRbxAIfT3zBD9gBbEnpxorxaCnRjQ_21YN1e06r1UQ4InOjRxjWJVXcXQ-MDUxMG7U8MoBCmAvuX8uyqReAQwm7h1yS6q9VTgYbuZWJU0eo-8LgfmHN4jrMRpuYRQoUcM2PacLGmDmsDfS_cfwDlopLbejPuFn9whPqCK-qiArMGGUIuw3D18TB7GE698tTD5nIX6WfYGjRM7FlZs2silw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق آمار رادار کلودفلر، از ۲ روز گذشته ترافیک ایران به کلودفلر به شدت کمتر شده. اکثر کانفیگ‌ها و اتصالات به کلودفلر مثل وبسوکت و xHttp مختل شدن، فرگمنت روی همراه اول و مخابرات بسته شده و روی ایرانسل ضعیف کار میکنه؛ همینطور پروتکل UDP به سمت کلودفلر کلاً بلاک شده و اکثر رنج آیپی‌های هتزنر و OVH از بیخ بلاک شدن.
©
mahsanet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2642">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AXIfUvS946GGkA1GYCyrT0JkmnQpl0RSFrr1zqwDISQ8Jr0ng8El3b57H8iC2lLcdITJMKhbxPTW62FZrcm-Jjhi7xRNh9Cc5T8S9-8DLn5iwqhkCxiUQsNeQf0f20TegK198Z0yDwqt1VS4azRFiViDo20ip8S__ph2iwHM_ukBYwekSUqCm_DThGOJgr6KQqKS3u0J7rCQqD2P2lNcnJpvHeB-lWo1fQ_8vrKHojZf0BKQlbghmzGysoRefBwXFSLVJ5RJDv6G6KVxmkgN2w8tvuM_vgobsLtl7KMTCOX9yAUW8uvDqAgW-nT-6BvT3phaJJX5YtkUP8o4RL-OTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نحوه استفاده از برنامه‌های PattN و PattNG برای دورزدن فیلترینگ
📽
youtube.com/watch?v=CnEQipAJ2hE
💡
t.me/ircf_toolbox/25
©
𝐀𝐥𝐢
👉
github.com/patterniha/PattNG/releases
👉
github.com/patterniha/PattN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2640">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CxI5NMCWNJ4O4z2RCYohl5HoDVcjIXfLEbpCtgBJ-iLaCyRQqsZGdA_wAsgUVNUTPrUdd8YH9agyU4RGuHxu_50EzonRsNaGYpaw3ktaOeqPMLP_2yzWU96wyEruiflyTN7GD2qbnr0LhzQY-QFIYfYoACRFygtuQLK8UrA745iiRv2qBinsYDql2Uf8DMw89ROawzAuihR9ZhagdSp6dS_m19AxfIfrLt2_e2kFvFf1allOZKUS9T1TWuM_oRjZy6X7AGLHiCHGUWEpNQ7qJqW0do5viSVX_w1n3zhRl_U9nr37XlyGA829o0sYqVOSGMuujpa_n2Ywnngin69r-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید از هسته Aether مشکل برگشت آیپی ایران در متد اتصال Gool رو برطرف کرده و محدودیت اخیر دریافت کلید وارپ و مسک رو روی بعضی از اینترنت‌ها دور زده.
اگه H2 روی سرویس دهنده‌هایی نظیر ایرانسل به هردلیلی ایراد داشت، میتونین طبق داکیومنت از فلگ فرگمنت استفاده کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2639">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hFpyMs6O4bHxxEtqbIl8ULxcyOBdXnlSzW0Rn94Zdqo347uPd9Emffytsw57bNkPSWHlOeuUns1JiKUzrSOhdqmFW_xGYKEJx-q4JoakSu93CKy2_u2I0UqvplfTAayE5nCT0aOVmsS6KWixJcWu3xiRI-1wPNuUcF_bzQcJLg8IFrjE59K5oIEoSRw9xlxzaETaxjO84TtkOYf2paPVh41EuGCsqksSMEXl9ezw2BcfEG4kV6d5UpAZszcMEg9GJ-8M1kmoi9wcEVDkhrOYqS4vfKYjXzEvwN8gtMBY8tyyE95gMUp7ujE4FDfmirH10Z_uMqWGB4pnZDw0MmW3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱۸ از فیلترشکن اندرویدی MahsaNG منتشر شده و توی این نسخه هسته Xray مهسا آپدیت شده و پشتیبانی از پروتکل MASQUE رو اضافه کردن.
برای وایرگارد و مسک حالا یک اسکنر IP اختصاصی در دسترسه که از نویز و پورت پشتیبانی می‌کنه و میشه کانفیگ‌های این دو پروتکل رو با کلید Auto ساخت. امکان بکاپ از کانفیگ‌های شخصی، صفحه پروکسی تلگرام برای کپی و تست سریع پروکسی‌ها و بهبود Fragment و حالت Auto هم اضافه شدن.
چند نویز جدید برای عبور از فیلترینگ UDP، کانفیگ‌های جدید یوتیوب و پشتیبانی از Cipher Suite برای افزایش سرعت آپلود در متدهای پترنیها به این نسخه اضافه شده. FinalMask حالا روی پروتکل‌های جدید MASQUE و Hysteria در دسترسه و علاوه بر رفع یک سری از مشکلات، ابزار زنجیره‌ساز کانفیگ هم از Fragment، Hysteria و MASQUE پشتیبانی می‌کنه.
👉
github.com/GFW-knocker/MahsaNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2638">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tp8gcyNC0o55NUL-iPs4nrRmRkYu4ysGBa2ZRJ0hj1gEF5X4Sd4L16M3VTmPIoQ64Rk4AgbcP5A-nMLXkTaPc3yy_ukz9P3Ecc_qp6NPDbJf5vKDPy6RItL7nIe6-e1gY3iToZ9HZoRnDlavx7oyYJ-w8CMrypB6B-QdLkZiDZ5CO98qLgFPjIroSmwpBVALgadPPefUbCPUUw2vwuXuwiMeT3dtkhs7QnwuoaEoUji_o69nA8WcHo9CqVf07_uSqPW7btm6kfzFgQGGCUo4_lcKRI7yajbWhPK9O12Q2qXoIb_1ov3ZYUoph2nUVFWBU_HpOzizE168tYZ8lfKSWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپل از نسخه iOS ۱۸.۱ قابلیتی گذاشته که اگه آیفون ۷۲ ساعت آنلاک نشه، خودش ری‌استارت میشه. این کار باعث میشه اطلاعات گوشی دوباره وارد حالت محافظت‌شده‌تری بشه و ابزارهای فورنزیک مثل GrayKey سخت‌تر بتونن قفل گوشی رو باز کنن.
حالا شرکت Magnet Forensics که سازنده GrayKey هست، ظاهراً راهی پیدا کرده که قبل از این ری‌استارت خودکار، گوشی رو در همون وضعیت نگه داره تا مأموران بتونن فرصت بیشتری برای استخراج اطلاعات داشته باشن. این قابلیت با نام GrayKey Preserve و همچنین Evidence Preservation Mode معرفی شده. البته فعلاً این موضوع بر اساس یک ویدیوی تبلیغاتی لو رفته از شرکت مطرح شده و جزئیات فنی روش منتشر نشده. در واقع جنگ بین اپل و ابزارهای بازکردن قفل گوشی همچنان ادامه داره.
ناگفته نمونه مأموران توی ایران برای باز کردن قفل گوشی بازداشت‌شده‌ها، نیازی به GrayKey و این ابزارها ندارن؛ زور و تهدید راه ساده‌تر و دم‌دست‌تریه واسشون!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2637">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پروژه Nexora یک پنل برای مدیریت چندسروری VPN هست، که تا ۲۵ کاربر و ۱ نود رو بدون نیاز به لایسنس و با تمام امکانات پنل در اختیارتون میذاره و میتونه برای مصارف شخصی یا گروه دوستان یا خانواده قابل استفاده باشه.
نکسورا مدیریت کاربران، نودها، اشتراک‌ها و پروتکل‌ها رو از داخل یک پنل انجام میده و از پروتکل‌هایی مثل VLESS با REALITY، XHTTP و Encryption، VMess، Trojan، Shadowsocks، Hysteria2، TUIC، AnyTLS، Naive، ShadowTLS، Snell، Mieru، MTProxy و SSH پشتیبانی می‌کنه؛ در کنارش پروتکل‌های کلاسیک VPN مثل OpenVPN، OpenConnect و WireGuard هم قابل استفاده هستن.
از قابلیت‌های دیگه Nexora میشه به تانل بین نودها، پشتیبانی از CDN و چند آدرس برای هر نود، همگام‌سازی بدون نیاز به ری‌استارت، Rule-set برای مدیریت ترافیک، مسدودسازی تورنت، محدودیت دستگاه بر اساس HWID و انجام عملیات گروهی روی کاربران اشاره کرد.
برای مدیریت و نگهداری پنل هم امکاناتی مثل احراز هویت دوعاملی، بکاپ رمزنگاری‌شده، بروزرسانی خودکار و Webhook در نظر گرفته شده، امکان مهاجرت از پنل‌هایی مثل S-UI، 3X-UI، X-UI، Marzban، PasarGuard، Hiddify، Marzneshin و Remnawave رو داره و از زبان‌های انگلیسی، فارسی، روسی و چینی پشتیبانی می‌کنه.
👉
github.com/nexora-vpn/panel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2635">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eJatGOBTtl7yHftj0Xgl0RTBMwdHYKHhTmScfDaZBvoVicnOr365yoHog4iz4dMWVbp6iApM3TLXBg8sYwWVXGgfR5WT3uLq_WI9CQ65pdI2zsd1gBOgauotVCTendo3tgL2GVab-oF96be1qNE2L51tMxSUh3AokAi2toTsbfUusw7cJkB3J4ZXAEk9TuF3NERMbd04wewq0Xt-u2UaJeMbQSANWTQEOlyUQZGdriLZXAwaJHXkiAzM2UxR2QS5hAV1tZb2zHl4VWg0e95W3N2LgQNKLmzgTUck_gAnr9K8tXpzqEI2DwyQ_PrQ03eIycmhw5iN5AXu-wOZJQT4RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب رسمی مایکروسافت در ایکس با بیش از ۱۳ میلیون دنبال‌کننده هک شد و مهاجما از اون برای تبلیغ یک رمزارز جعلی با نام $Clippy استفاده کردن.
هنوز مشخص نیست چطور به حساب دسترسی پیدا کردن و تحقیقات ادامه داره. مایکروسافت هم اعلام کرده هیچ ارتباطی با این رمزارز نداره و پیگیر اقدامات قانونیه.
©
theverge
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hu-iSzpqq_rKhO29EejDxwRu0OVGDwqafRs-Oxcm_GqmX9C4q4BP0lF8c6Fc2p8HuIR-wCTFwRmAdgrksNmmFWRA0p9nNoi_aHgvcNgquIMSXYey6871orKb-VJyJ2QH3T5fWY5h5DWKQeFud6wfNFGumPUd7KdOFwoh9MrMMIqeJ7TPdJjHdl2Xy028hefi-9ecHsX7Or3DADKs_BDmBP_EgEZypUB04LjCbC5713Gf9HaIuV5Fy7bi8fkC6UabSiruzgdjs5dAuIGJemjoO_yUg3CH3eHo8TTvnFRx-rKBqjV9zlwOtY8uMJ-5_SHuMD0c8RihpJ541WX4mak2tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OVTLFIX7XYYFySgnh9V0xFimi8kB7uI1JtUIFWSTp7PVP8s-jOk8c5kpm476ejN31jXdCglJ_8Xnc7sNN6KxKgj85PZsuAtrpHFGVwD5li7Qxgks_IN52QfD-QstaOHX84TwigJkwIZQXvseyXDyulpcGQfEeDFzijxIx4Etry3CHYkN-as2l4eDyQ8nza2YXZu3DaG_V6DAYrmHNdcWd-H7ksmRbw-bG96tQlKDGoRgCTt_WOzwb_v82p9FqqD6TvYXGLrdfsfvGDp14vrEoVRBvbuCK2AKyWRnjcVxUyOa8V4S9-zfCUaaqcg27E1Hv47ao1p2QB8liDg8gTYQ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه از TeamViewer استفاده می‌کنین، چند آسیب‌پذیری امنیتی با شدت بالا پیدا شده که در بعضی شرایط می‌تونه به مهاجم اجازه دسترسی غیرمجاز و حتی اجرای کد روی سیستم رو بده، که مهمترین مورد CVE-2026-92370 با امتیاز ۸.۸ هست.
فعلاً TeamViewer گفته شواهدی از سوءاستفاده فعال یا انتشار کد اکسپلویت عمومی برای این آسیب‌پذیری‌ها ندیده، اما در نسخه ۱۵.۸۲ این مشکلات رو برطرف کردن و لازمه آپدیت کنید.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fx6cVx8GM54gjAJW5HFOkncg0Xi2PjF8ddJa4l8zt5WTNdwN-FP_GAnYuc_OIxcPMf5ijm3E85kmBjdub_85K23xm835fDHSgYeoupZeACCdV6J02GLkbXPKG_HySwPTP_myhpaohra6xkgdNOtr5w0dSwZ_OMfBjXa4mhFDYGNW7fvW8EXFQSNfUewbQTQ7fFiU6vWMX0HhWz3tv1ucObRVnE3ZaZHvv5LnGszIqh--P9dw9D4_pHHNai5fikooEAp5MvUlSNCnsxHOPEaOmbzHfzyhmzdH1YTZ6eR8yG_05D9WFKc0zT46ulCL4FXXBlwVq9qNOvUlaKesLggxwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ج.ا در سال ۲۰۲۶ رسیده به راهکار ماه‌های پایانی حکومت قذافی در برخورد با مخالفان: قطع سراسری برق!
©
ArminSoleimany
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2631">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KaeajPMhbHgXMmAqEt19Vnkn5ipaKl4XgONvbWo9O372mGBb6l9pf6XiXlAW5Dgd87vnzQkDY4tzkKVGSu4k_NkjmhK5ZHqDY8hrI71SA9B8V1x3Zq7LjrJw7cTLHgzn_LjxBg8gWgw4qRwaBuNkXXFlVsSe3W4k29xp0kozJwmtcQE-Yt3xnCClaYWUFGc4A0D-sVgmg7anbXzLsXHR_WG-CmTrkD9JwhwSvVH-nfHQI44MkML3vaYdxGYXCwSFUR1LLyQ2XOMhN9gotMtEolb-vz1G9j9oBIJiizzDOCs5e9uQUuu-ETYDqDmu8hhUbC9i63sr7vVjX7DjxHRuGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتیجه این و اون خبر چند وقت پیش در مورد تغییر شرایط استفاده letsencrypt می‌شه گواهی ریشه داخلی و پایان بازی. از مسائل فنی اجرایی صرف نظر کنیم، بحث‌های مهمی باقی است: «حریم شخصی» و «امنیت».
در کشوری که با مداخله در پیامک احراز هویت ۲ مرحله‌ای حساب کاربری مردم رو تصاحب می‌کنند و پاسخگویی هم در نبود قانون و ضمانت اجرایی نیست، امکان جعل گواهی برای شنود به خصوص برای موارد بدون SSL pin هست.
©
Hamed
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oY3BiJtMdFF7BW-3oMHsLhDCHdSRdi9UENT4UjBbwZaZyPt20MuCtDuuJ7OgKW25hiRcddscN3vffxX76cpDoY7GuoWSwc8jJuvi_ot4YIRaQ5P88LtIRAKIiJiI971_flzuLY1pAaDa5afUTQYkJim87lid2B9KGedyOl3rAMJMRV8wO_3Ig8IcFiaWkRdZfReNzDUgndQ77Sd_t5BG6yZxRt5FAQ4Nl30myTMl3nbtp_PJ67Flk5RglD_Ri7B1VGGjJzFv4sexuMGy9KTS_Qitr2K55fDPh5_SOe_rViFZo4YwEBrFH_ab8pE5PRomeY1nbptgYPZjC8CND-6xJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهکارشون برای مدیریت قیمت تتر چی بود؟
نمودار قیمت رو غیرفعال کردن!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2629">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کاربران در چند روز اخیر قطعی، ایران‌اکسس شدن و اختلال مضاعفی رو در اینترنت تلفن‌همراه و ثابت گزارش کردن و میگن آشغال‌نت چندروزه که شدیدا اسهال گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YQP8lKfCvmVs1ezXj0LN_hnyJsC8wTdae6gMIyQ-pfUV-CrZa5mV3TxOGwgVUDsV1P0oB_WsjGNHisHSpVWVOqsI8LOpbqqdcarxqRt-0K1Z9Lf7b7CEo2fzRI07oICNzu2_KdWnGZ_y2B92EkN5lVflRNfTkiLo5LvUv2TTXRolzwHPTA2joOnnFtl_4JgKrXBg48OWDzaeGbh4SbfJ5peGZv4lXN2e6ieIw-utThmElMO0ppHFgaqDajxhRkMGS_YxpIwgOqWScoswhWb1Ps00nTX2H76F43fX_L0ijfFcXrIzoru3qqL31X98YS_T3oTOWXoh7rxkh_P82nvWNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Group-IB، یک بدافزار ویندوزی به اسم HEAVYGRAM شناسایی شده که از تلگرام بعنوان کانال ارتباطی و کنترل (C2) استفاده می‌کنه. این بدافزار از پاییز ۲۰۲۳ برای هدف گرفتن روزنامه‌نگارها، مخالفان و منتقدان جمهوری اسلامی استفاده شده و می‌تونه از راه دور روی سیستم قربانی دستور اجرا کنه، فایل و اطلاعات بدزده و حتی از صفحه‌نمایش اسکرین‌شات بگیره.
نکته جالبش اینه که مهاجم به‌جای سرور C2 معمولی، از بات‌ها، اکانت‌ها و گروه‌های تلگرام برای کنترل بدافزار و خارج کردن اطلاعات استفاده می‌کنه. Group-IB در گزارشش ۲۹ نمونه جدید از این بدافزار و ابزارهای مرتبطش پیدا کرده و با اطمینان متوسط این فعالیت رو به گروه حنظله نسبت داده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2627">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اتفاقات امروز و تصمیمات هوشمندانه‌ای که برای مدیریت اقتصادی کشور گرفته میشه، کله هممون رو خراب کرده احتمالا.
ساتوشی می‌تونست وایت‌پیپر بیت‌کوین رو خیلی کوتاه‌تر بنویسه: دست به دست هم دهیم و دستگاه چاپ پول رو در
ماتحت
بانک‌های مرکزی فرو کنیم.
حالا تقاضا رو سرکوب کن، حساب‌هارو ببند یا سلطان فلان و بیسار رو اعدام کن، این باتلاقیه که خودتون درست کردید، توش دست و پا می‌زنید و ازش خلاصی نیست. این وسط، عمر ما هم رفت سر ایدئولوژی شما.
©
GrizzlyBTCloverr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2626">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NxmD3OVD4VQ8CpfPYYRtdcJ8XPHmhf2LtDnLoL_qM4ocrSuDtoZxzuNzS5O3kf7q9Y22JqdAefOvJfg8A22M9oae5mCxPFAhoiz264TklVupBVONELc83qLWb6AohIwuVneoHjxhDxIq9G09trdm3KQ0gKxw7eDFHTrDgA0K6F1OEaAnEDcyA3WIwOFc94CcIEMQBusOQI3PvE-pTP1gm-DertFiHcV08WV88TuANdn_Z1QxEZzPti_vDt5kloHaCBUfRA9uXMokhMhlcCGGUJnkT90V-oOIF5iIrRF2vRHdz3uQZOSE6xpMsGZpnnBtVWbRoS99kvMzTOkZrEvIgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از دیوار چنین پیامکی گرفتین، ازش بی‌تفاوت رد نشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iSmBUi73aQTpwZ_jurXgIOabPG7MkOJTdbzUlfnrg8TC63aOTyBzwqT_CUZ940MWK1G0UFod429cAM964zJZcsanLVMBIAYXsuU7aNi1vzkdI_ld2VAJBLH9Mpkd2kYH1v-cN_1w9IPI2QF9lvxCzkGJaRhN_EOFL99wTLBBe4kczGSwaR5NFwQN4DfPRnR8LGOC-GJV9nl4M9UMJpVssPhcg6Pz72VToEdQVjcVlJFZ3uW-pOq8LQ_ELTX81pwtcyaXLn2Vjxk9u8w-wl5Wu8bnRrADCQqrD78xByfjgVpx-Q8Iw_0mqMFV6vvea946wjHnSKaHoQcveY35AM6MHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرامه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2623">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مجموعه‌ای در حدود ۷۵۰ هزار رکورد از اطلاعات مرتبط با کاربران صرافی ارز دیجیتال والکس مربوط به سال‌های ۱۳۹۷ تا ۱۴۰۱، در فهرست فروشندگان بانک‌های اطلاعاتی غیرمجاز مشاهده شده.
این داده‌ها شامل اطلاعات هویتی مانند نام، نام خانوادگی، شماره ملی، تاریخ تولد، شماره تلفن، آدرس، ایمیل، اطلاعات مرتبط با احراز هویت و همچنین اطلاعات مالی از جمله شماره کارت بانکی، شماره شبا، اطلاعات صاحب حساب، آدرس و موجودی کیف‌پول‌های رمزارزی و سایر اطلاعات مرتبط با کاربران است.
افشای این اطلاعات می‌تواند زمینه‌ساز فیشینگ هدفمند، کلاهبرداری مالی، مهندسی اجتماعی و سوءاستفاده از اطلاعات هویتی و بانکی کاربران شود. به کاربران توصیه می‌شود در صورت فعال بودن کارت، برای تعویض آن اقدام کنند، نسبت به تماس‌ها، پیام‌ها و لینک‌های مشکوک هوشیار باشند و از ارائه اطلاعات شخصی خود به افراد ناشناس خودداری کنند.
©
leakfarsi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J6J3JHxdnvlxs9T3mj78q3EW0qGTVDnKHjtU7c5dgpjO_eYpXeMcLmO6PWPUx-h-EA_ZjOqJo2MFkOqmWPtHPLQyco4_hq8BR10LZgxlcnBgxpuwf3QOQIEjmTuqdJnB82so5i21-nEOUYzvKnMUExc_YUFP-t3RlQInLtf7ayRSww90wuwW6YpGhWnbBHCeHBmSR6Xoo4L5Sr2Zib1b6v0TNvWSJmcijIoScGC9o8V-hM7vlQO9g9zgaEYbNZ8vLfb92pONGq-K1-mylqmo_Zf-kyBURt6E5h2oxHHi1AlbARoCPX4HgjN9KK8E-vEsymxmYLkmc2IROjWi8OCBIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر قطع‌ارتباطات گفته "فراگیری استارلینک میخ آخر را بر تابوت حکمرانی فضای مجازی می‌کوبد".
۸۸ روز اینترنت رو قطع کردین و نگران حکمرانی فضای مجازی هستین؟ بابت ده‌ها هزار خونی که ریخته شد، باید منتظر کوبیدن میخ آخر بر تابوت ج.ا باشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/chLcQS1IEf79q7Spzvz7dSjyA_9pUZ77gxfEb43OxM_vCoBqZ1979pwPJ8YWWAJhFhVf3fwuKDANOB4jr6IQwbxrrfJNq4nVkSpel5YTPfuHRZEfmoOh7lA32YxKGisteZ7p8P3GrRejAZt4kxYFQ1yeSmSySnGpq9WG4jrfiAvoa-MZ71qO-WIjdqh2eSr9ToIGfim0_bmlmERM_BhnOBnl311RBx77gmyiwApZ2domuC-kT1MUW1v8gN7vXILPaoq_Q_0igumSQDPHfDV6z1hlPbtP8RRDFM_Y7IZcS5leJQnybbYINUU0HFM_YNbAEVbCAEZqu4PA1G4u3F7BCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی با ابلاغ یک بخشنامه‌ی رسمی، ارائه‌ی هرگونه تسهیلات بانکی برای خرید طلا، ارز و انواع رمزارز را بطور کامل ممنوع اعلام کرد.
این بخشنامه بر ممنوعیت مطلق پرداخت تسهیلات، چه بصورت مستقیم و چه غیرمستقیم، تأکید کرده و مقررات یادشده شامل پرداخت وام از طریق شعب بانکی یا بسترهای دیجیتال برای خرید طلا، ارزهای خارجی نظیر دلار، رمزارزها و همچنین فعالیت در سکوهای مبادلاتی مرتبط با دارایی‌های دیجیتال می‌شود. /تسنیم
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uCemhO8Kf_d5wIAGEQ2-NlwIUK8GKQ3qogDElX6N-_dV5p9lXr8EFXjEvvnbzBnJznyVHblPy5-TNPiQRyl0eOyasKWy35XzTKML8CoscyaLCTZPBZXFTpSTydI_iwqJuji21zSNZhZZuL-YOcpHT9JUwLSxqtg0lbnyy7ODIlcCkM9eALJxYigBKz_GU-VR9mLc4MS-yRE12S7BfXzhlTDVV858ueimgvU3vNSQnE6R8V6Lsf-xzjdKIRr1PKmaWB_wX2fY3kj6vvFVh_CMCCVV4MxnEH2Dn8BnUD3twLxXJhMEd3S7yWm4CjXczsrrJJV7-XZjUqam1VWunJoZjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت تتر به تازگی اعلام کرد "به مسدودسازی نزدیک به ۵۵۰ میلیون دلار دارایی مرتبط با بانک مرکزی جمهوری اسلامی و شبکه‌های تحریم‌شده کمک کرده".
الانم با عبور دلار از ۲۵۵ هزار تومان، صرافی‌های رمزارز (با دستور مراجع) معاملات تتر رو از ساعت ۲۱ تا ۹ صبح روز بعد متوقف کردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">هم خبر تحریم ساخت ایمیل برای ایرانی‌ها توسط گوگل قدیمیه، هم خبر مسدود کردن ۶۰ اکانت مرتبط با صداوسیما توسط گوگل.
فعلاً اون لجنی که توشیم هیچ تغییر جدیدی نکرده
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iTW_lmz-O5QSJAiJYsjCVI_H9cboGV85VhOXeO6deingdWm0vEbH6ELR-tyoPVTGresJHbggiHXSDkbSBa1FjTj_-Ea78tW8VHQpxksM1fc80mdr8TOvJk1o5yjK5SdLFHOsN5m3pJecE4nUganZNVHiZDu5erH539cvn4PIMj6xLlfEMs3KgKziDy7w6tahnmkG5J-D9cy6vpTRz8Lu40NuXNXheXnSr2GUJORJKcjmFDCRZh_0idKSXLi85IFLeI_lNpxLXVBtc3b80mGPOe2jv90IUZ_55FwW261u-ebGody_aMy1Lyl2q3H82Uio_C9NTnKR1xWI9EF7vDx-cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ sushTun یک کلاینت متن‌باز و رایگان برای هسته ایکس‌ری هست، که از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard پشتیبانی می‌کنه و تمام ترافیک سیستم رو از طریق تانل ایکس‌ری عبور میده.
یکی از بخش‌های کاربردی این‌برنامه که برای ویندوز، لینوکس و مک ارائه شده، مسیریابی هوشمنده؛ تا بتونین مشخص کنین ترافیک ایران، روسیه، چین، تبلیغات و دامنه‌ها یا IPهای دلخواه از تانل عبور نکنن. امکان تنظیم DNS، فرگمنت برای TLS، Multiplexing و چند قابلیت دیگه هم وجود داره. حالت کم‌مصرف هم اجازه میده ترافیک‌های پس‌زمینه سیستم مثل Telemetry و آپدیت‌ها مستقیماً به اینترنت وصل بشن و از پروکسی عبور نکنن.
👉
github.com/soroushdeimi/sushTun/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vdFXPfukdX6DEnZNQLlPN8GaKZYZJRraOT_8SR4n7NY8pZqhOm2Ul22h8iKmNxRi5077BvPdtEjnXg_WoWjajM6QQYftiTshGMzYO1SIHISSfMPcgZuPB5OEuUGlf1ffSgv7p_V1O0-kEESYgOo8pNnbVAamXrCeSCVwlYOYzyg8bKb2mskAg2p1UvsxCGsH8mz4F3QxkegROpAxJ8Zj8HVKZi2LlCnZtwtGKa-Ue7Bl4ot8xd5jROKJnHYwaPMMqZU8fPQT12N3OAzndFprcaN2LR8HsdaFJ6hvejGefxv_hx6uX2c0nyzLe-uW5f2V7siTIdbk-4MgEEEmV_fP-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت Satelite یک اپ پروکسی متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که می‌تونه بین هسته‌‌های sing-box، Xray و mihomo سوییچ کنه.
از وارد کردن انواع سابسکریپشن و کانفیگ گرفته، تا Rule-based Routing، پراکسی‌چین، DNS هوشمند، System Proxy و TUN رو پوشش میده و یکی از قابلیت‌های جالبش، حالت Multi-Core هست که اجازه میده چند هسته همزمان کنار هم کار کنن؛ مثلاً سینگ‌باکس هسته اصلی باشه و بعضی پروتکل‌ها رو به ایکس‌ری یا mihomo بسپره.
انتخاب هوشمند نودها، تست تأخیر و IP خروجی، مدیریت DNS و Hosts، تشخیص اتوماتیک پروسه‌ها و اجرای دائمی در System Tray هم از دیگر امکاناتشه.
👉
github.com/zn0wii/satelite-proxy/releases
💡
github.com/zn0wii/satelite-one/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cvkSTT2pqhsf6ZclUzOdZchB1Fq0UEtM2PzkF3AZRS-FCEQdYYT1d0Y5n_yA7iE2OBIZgt56JXSp7gcIEI5XdzAIUHRIMiECxvS7hbsIEacCCO9rYqKEkMUNYI5bIksBgxVwICoLUvZnnaJ00BXiXHocDBOEj4wPC3SrCHGGoBCC32HcT2s6rNyzmqzDMFOSFwFBMf9krF1KjNzyqDu8iNRmGkuCz191YtwPGoszskoJi9abdk1nPi2tOvAqKARpHQC3tr0DSeW9oeI6mFqznnPTUSVQdpIRmy0bYRNXSD12lD4CylqcRGksqPTajKcBBfMKHaNSiHBLHEEXSuH3Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی فقط دسترسی به شبکه‌های اجتماعی را محدود نمی‌کند؛ محتوای حساب‌های شخصی را هم زیر کنترل می‌برد.
شماری از کاربران با انتشار پرچم حکومت نوشته‌اند که درباره فعالیت‌های «غیرمجاز» توجیه شده و تعهد داده‌اند در چارچوب قوانین جمهوری اسلامی فعالیت کنند. پیش‌تر، انتشار لوگوی پلیس فتا در صفحات اینفلوئنسرها و کسب‌وکارها نشانه توقیف یا محدودسازی آن‌ها بود. حالا انتشار این تعهدنامه‌ها، نگرانی از تبدیل حساب‌های شخصی به محل نمایش اطاعت را بیشتر می‌کند؛ جایی که مخاطب نمی‌داند آنچه می‌خواند، انتخاب صاحب حساب است یا حاصل فشار بر او.
©
filterbaan
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">معاون سازمان تنظیم مقررات و ارتباطات رادیویی گفته "حجم‌خوری نداریم و بخشی از ابهامات و برداشت‌های کاربران درباره نحوه محاسبه میزان مصرف ترافیک اینترنت، به وضعیت ثبت اطلاعات محتوای داخلی در سامانه تعرفه ترجیحی مربوط می‌شود".
خلاصه: حجم خوری ندارن، ولی باقی چیزارو قول نمیدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BcWfBuOlHvecj3yQPyHdQRmzTKDgjZrXVmbOy8DU2Hwt264hJS-tNXqhMhNvyslSa9VFdgyVwomUOPjjPpeMqee8LXJYrkFqiCR8MTLNn1W2EaxIhasiVDGONH3rUty6U80xk-2LO964xgEdfz6WN0qAgtyGD7htT5hqlaQcUsEJ_teZg2cRxp1BqFZX7lH97HOD1OFnF75B0cON_Pdujvl8YMIAFS8Zy2QJBXcH4jclSUg-MSoYIA9sxaPexvpQ3P_ypD_iFM7LlFibqvIAPK--_R0Efy2GNwQVYAVhvHGQULl8jfVgdXUyvbNxQFeV4NZ3FGzH5JlKuBu9BHWwVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Qrator Radar، شبکه همراه اول با شناسه AS197207 در ساعت ۱۳ روز ۲۹ شهریور، بطور ناگهانی ۱۹۰ پیشوند شبکه رو اعلام کرد که باعث ایجاد ۱۰٬۸۶۵ تداخل مسیریابی با ۱٬۵۲۴ شبکه در ۱۰۰ کشور شد.
این رخداد که بعنوان BGP Hijack ثبت شده، در ۲ مرحله اتفاق افتاد؛ مرحله اول حدود ۸ دقیقه و مرحله دوم حدود ۱۵ دقیقه طول کشید و حداکثر انتشار اون به ۱۰۰ درصد رسید.
وقوع BGP Hijack میتونه باعث قطع دسترسی، انحراف ترافیک، اختلال گسترده و در بعضی شرایط شنود یا دستکاری ارتباطات بشه!
البته در این‌مورد مشخص نیست که بصورت عمدی بوده، یا خطای فنی ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بانک مرکزی نصب «گواهی ریشه داخلی» روی دستگاه مشتریان را یکی از راه‌های ادامه خدمات بانکی مطرح کرده است!
اما مسئله فقط رفع هشدار اینترنت‌بانک نیست؛ اگر این اعتماد در سطح کل دستگاه ایجاد شود، می‌تواند فراتر از سایت بانک اثر بگذارد و در شرایط مشخص، زمینه رهگیری ارتباطات رمزگذاری‌شده را فراهم کند.
مرورگر زمانی گواهی یک سایت را معتبر می‌داند که زنجیره آن به یک مرجع ریشه مورد اعتماد برسد. اگر کاربر یک ریشه داخلی را به سیستم‌عامل اضافه کند، دستگاه ممکن است گواهی‌های دیگری را هم که همان مرجع صادر کرده معتبر بشناسد.
خطر زمانی ایجاد می‌شود که آن مرجع برای یک سایت گواهی جعلی صادر کند و مهاجم نیز بتواند در مسیر ترافیک قرار بگیرد. در چنین شرایطی، مرورگر می‌تواند بدون هشدار معمول به واسطه اعتماد کند و حمله «مرد میانی» امکان رمزگشایی ارتباط را فراهم کند.
نصب گواهی ریشه به‌تنهایی به معنای شنود نیست؛ مسئله اصلی دامنه اختیاری است که به آن مرجع داده می‌شود.
البته راه کم‌خطرتر وجود دارد؛ اپ بانک می‌تواند فقط برای سرویس‌ها و دامنه‌های خودش به یک مرجع داخلی اعتماد کند، بدون تغییر فهرست اعتماد کل دستگاه.
پرسش اصلی طرح بانک مرکزی همین است: برای حل اختلال خدمات بانکی، چرا باید اعتماد یک مرجع تازه احتمالا به ارتباطات خارج از بانک هم گسترش پیدا کند؟
©
raaznet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dVfGXcGOAL_bPu08fpFqN6XyxCmZ6RFW4FaUv22tbQ_P3batvgklrRgCcqkxDnCXLKFT1IBJzQciiF_WcfiIXXReuzkFqscFR0g25JgbNw01p0aYtG37vwllSF7F7mUbFGK5OPB-OkUPqpV9xmniKla9Wg8wV1ZajWgHGAKDXrF6sNjdcIxJyp1asH76f5d3cco1kr0ZTaT_cQmw-jy_exzYOprsFLDW9KQ2clUdCkkyfN8_eln8xZDhIYWLKrUDJlf41tscPKqXRw2JgOTDE7SGKM-8Pe4T_Srq_rdQC_x_va8RO0rgN_IqAJ5e_Tc4QOxgqjTbxyq3aUDdtUX8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراقب این نوع هک باشید!
یه صفحه جعلی شبیه Cloudflare میگه برای تأیید ربات نبودن، Win + R رو باز کن و Ctrl + V بزن.
چون شبیه تأییدیه‌های معمول کلودفلره، ممکنه طبق عادت انجامش بدید، اما در واقع دارید یه دستور مخرب رو اجرا می‌کنید.
©
milad_joodi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hSYlJyffWGBxgwKF3yUe_Do8b2DMtUwc5VkHD8j8DkrnVPRB6fdzt9cdPyi4VDNdWxR86HQepo3s49lvibdcoMQTQRgZWjvXOhwCe1WkyMirjcipkgtA5H9W77T4qo88VpclUQ79tjbZTKkyuFGkZa4Ur6vq0QfRMX3jYKxayJC03RqhXDEU1G6YYgseUCrSjNJGQyRMZ0IiLukPEoGBsZhDTgoLUWXUaz3I1IcWAOdz7RwMyMY9iM02IqCrMDUINe921sE8onmMcBDuwCS-r4sIqZH0wZHa1IU2zbZIuc5oisV3PPRmjeNhyHVDnkJsMZ8OHg29gfhzXQqv3aEWsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زپتون یه موتور شبکه‌ی جدید، متن‌باز و بدون وابستگیه که با Zig نوشته شده و برای کار با رابط‌های TUN طراحی شده. ایده‌اش اینه که ترافیکی رو که سیستم‌عامل وارد TUN می‌کنه، مدیریت کنه و اون رو به ارتباط‌های TCP، UDP و ICMP تبدیل کنه؛ بعد هم ترافیک رو مستقیم یا از طریق SOCKS5 در اختیار برنامه‌ی دیگه‌ای قرار بده.
پروژه Zeptun امکاناتی مثل پشتیبانی همزمان از IPv4 و IPv6، NAT، مدیریت DNS، مسیریابی خودکار، فوروارد ICMP و پردازش چندصفی TUN رو داره و برای Linux، Android، Windows، macOS، iOS و FreeBSD ساخته شده. طبق بنچمارکی که روی یک رانر گیت‌هاب گرفته شده، زپتون عملکرد بهتری نسبت به Sing-box، Hev و Tun2socks داشته.
این مدل هسته‌های مستقل، می‌تونه برای پروژه‌هایی که نمیخوان تمام شبکه و TUN خودشون رو به هسته‌هایی مثل سینگ‌باکس وابسته کنن جالب باشه؛ مخصوصاً با توجه به اینکه استفاده و توزیع کدهای پروژه‌های دیگه می‌تونه الزامات لایسنس و کپی‌رایت خودش رو برای توسعه‌دهندگان داشته باشه.
👉
github.com/Noisemux/zeptun
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aVmfcsqXwMOOpJOD-ETJiF0xzf38vehrhIkkSp7IlVlfg35nuKMbOBTj-GCpiviL3534JQypNA9PGO6h6xZM9jQzy2Ltj1Y2jgKmzdLV3tDMZLPBag8afojy9gHpqd0DQyGTJIwvrVfg7PueTQdLc3xIKRsgf0ncQKHJK3XCoAYkMXfAPw0T4N0eJ322z9vy-TrOm_Kdu-UiEcB82oW-LKoKjmkAbvO4MBsqIT4p-aYfQm_MDY2SdHJ9ae8THxu6ENhEI-s7rJ3ltGj0R1SEHyFfuplJZxqMlkXvg1S61_HVtb8SvUvtlAEOPKlITojylyxWj12vYesdLZLPh_DVag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای، چه گوگولی
😄
فرمودن "مجلس بدلیل پایین بودن کیفیت دسترسی، با افزایش قیمت اینترنت مخالفه و انتظار داریم وزیر ارتباطات از حقوق مردم و افزایش سرعت و کیفیت اینترنت دفاع کنه".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LCA_slq9Yp3pfhEnhKCyD-MIe4KSijM-kXFMfkPnNVy8e1IqlfvtZH0rPg4Sb33DLreT6TCjuYra37C5TYVbCCrtH8j0dyo32IMlzUcDbpqpXa0TX6HnsgMdlpSMF8fyy14rVJkAYt8jtNDvVQFj0H9PRgjPZLyDR7k7DJvPp8LGSs9YTl0_J8RpGBQQVeR6vF0bbn2mn9YBbVDqwGU2n9czhnBegy9TV2JIZR1G-Gutg5GDwW2q_JHhiQbjf6RdS1IjXcwNNII7FPyIq-8KYDmZanW4Hqyu28kDBPbE6GlTEuUb7EHEeDyA9qQ4YrVRklcDrlgZCuayLfxfUIGaqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت Google Flow Helper برای اجرا از طریق افزونه مرورگر Tampermonkey ساخته شده و کمک می‌کنه محدودیت‌های دسترسی به Google Flow برای کاربران ایرانی دور زده بشه.
این اسکریپت درخواست‌های داخلی Google Flow رو زیر نظر می‌گیره و وقتی به پاسخ مربوط به تنظیمات و محدودیت‌های سرویس میرسه، یه فلگ مشخص رو پیدا می‌کنه و مقدارش رو از false به true تغییر میده. بعد پاسخ اصلاح‌شده رو به خود رابط Flow تحویل میده؛ در نتیجه فرانت‌اند تصور می‌کنه اون قابلیت برای کاربر فعال شده و محدودیت مربوطه رو اعمال نمی‌کنه.
این ابزار VPN یا فیلترشکن نیست و خودش محدودیت شبکه یا فیلترینگ اینترنت ایران رو دور نمیزنه. آدرس
flow.google.com
باید از اینترنت شما قابل دسترس باشه. این اسکریپت بیشتر برای مرحله بعده؛ یعنی وقتی به Google Flow دسترسی دارید اما خود سرویس بخاطر محدودیت منطقه‌ای یا تنظیمات سمت کلاینت اجازه استفاده از سرویس رو نمیده.
👉
github.com/maanimeisam/Google-Flow-Helper
💡
telegra.ph/Google-Flow-Helper-09-20
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WNo8-C3eSBAnmGuViHS5O35aesVNmJWbj_EwbYG8Icc04DBTo08falal4j7Jr__9TxeB8C4pRGjuodQDZoCMy7ZdhlV6p8Uwd0GQVYOHziPmCMpXkRK2Tk_7mNTsRzBWDPADc-Gu7hTuCeXihqmKERAF-0NcYtkQNFvs1PLA_BQUwSWzI17JxH7PfkR3JTRKitElAX8zAShOSk_FC3u6WSOm_63BcZAHosrUJiVI2MM0L6_7LMxwT-IBbXGujeIOITkcLzBOlCU5WPyIxMU1MlPj6njiN6YMzTx7Mg5zZ3NszRZWGEXstPazdoObcpbTFw9RlxXHLYq91Lp23Lk7pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیقی از TechRadar روی نزدیک به ۴,۸۰۰ اپ VPN اندروید و iOS انجام شده که نشون میده تعداد زیادی از VPNهای موجود در گوگل‌پلی و اپ‌استور، اطلاعات شفاف و قابل‌اعتمادی درباره سازنده و سیاست‌های حریم خصوصی‌شون ارائه نمی‌کنن.
در این بررسی، ۳,۳۹۲ VPN اندروید و ۱,۳۸۷ VPN آیفون بررسی شدن. فقط ۶۱.۴ درصد از VPNهای iOS و ۴۰.۸ درصد از VPNهای اندروید تونستن تمام بررسی‌های اصلی اعتبارسنجی رو پاس کنن. بعضی از این اپ‌ها از آدرس‌های رایگان Gmail، سایت‌های ناقص یا غیرقابل‌اعتماد و سیاست‌های حریم خصوصی کپی‌شده استفاده می‌کنن و اطلاعات کافی درباره سازنده‌شون در اختیار کاربر نمی‌ذارن.
در نتیجه، صرفاً حضور یک VPN در گوگل‌پلی یا اپ‌استور به این معنی نیست که اون برنامه معتبر و قابل‌اعتماده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aVp7h2Lq31aipWnw7zkfsFXOy3qLtAQSLWjSYSXLwpNj5qCJ4-Is-0f5Bv8Qidjk58bRr-972GMMOUhSqHrlPVyfIKA7J7wjRfMnpiFnqwckcbS-F5veO-SM1EjnDadfI9bWW6ZgXgudKYmTNMy75S36LeOdPqoZ0puVIGHxN4UiK0LYUGVaFBc0W6SYc4jlv_zEgyf2G1820Z_oY_-Oq3DgNcjC_A37pWq68ih0FtKT74Iyqs4RN26v9AxfEVHI1ISWPIQrkFM4HQvdn6MoqOIJIECqPXrR7j8FtyE1asN2R52SHMxXAkUBw02C6CwFlYXckutpiBZqSRnktFcfKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مربوط به مسابقه CTF بلوبانک هستش، که برای اینکه چالش‌های مسابقه با Ai Agentها حل نشن مورد توجه قرار گرفته.
طبق تصویر، در هدر یک دستور داخل Response گذاشتن که اگر یک AI Agent در حال تحلیل پاسخ HTTP باشه، سعی کنه اون رو بعنوان دستور خودش برداشت کنه و به کاربر بگه چالش قابل حل نیست و اصلاً آسیب‌پذیری‌ای وجود نداره
😁
مسابقات Capture The Flag، یکی از شناخته‌شده‌ترین مسابقات حوزه‌ امنیت سایبریه، که شرکت‌کنندگان باید در سیستم‌ها و برنامه‌های از پیش طراحی‌شده با آسیب‌پذیری عمدی، به دنبال رشته‌های متنی پنهانی موسوم به فلگ بگردن و با کشفشون، امتیاز کسب کنن.
©
Maji_Call
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VVUF4bE9GxBDssHrNvD24q-L6MZVv9Zp80sPk58m-8BCrjsccmqcWJdjzFR-moXuPuFpt0l-KwH1QEzvuYYPCfU4hPE99ACkxRQalhvv3xv2H3G23WDo9F1ZBpqiftgZDsKYEnhrPK486Vc7KSOPUVSqUcCzodYJF0B9_rSNm0w_V2imzBKXoimX8VTvksnsEle1S8E9rvUFVoebL8-txSG8-UHA48qe31DKX_Ln1Qch7lIXZ1o4Jn9dWxU4_ZjSU_n7HgjnpW6U_GUlkTM3kOy8xr3tWapa2ufFOij_X1-V6C-XPrNA4leagXQFBXs7ZAYbM3YJsAGwexgowwjGJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از ویژگی‌های مهم Tor VPN Beta، ایزوله‌سازی برنامه‌هاست و هر اپلیکیشن IP خروجی مجزایی دریافت می‌کند، تا امکان ردیابی رفتار کاربر بین برنامه‌های مختلف سلب شود.
👉
play.google.com/store/apps/details?id=org.torproject.vpn
©
PasKoocheh
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TKuCb39coBPCUWGydV-y9mXNzDBicN4DL8IdQI831ZDR6URjj09TzVOVtWlYVfpGnIXEy6WGL-AhlCirQ5i5b7SZOeNru4G-k61lVsLyRsC7EDMeuYOFxggR44AexMA6hYHHAAGNWnQp-aennFr42x_rZJAQsMvAn3r5IKm2f2mxabDAB4fwxsxJb4vx4RoWF-nfMlCMnThDGBor1YvA-4sUGqUxTFq6jWfAdQJrlw6-rRO8mfFf7PIeGerF2rCp2TgK-mPEd0jqmyaBXccdffHhzu_T8JtSJiMxeKX-5e70aWVvbKUf0vlo-3pBi9sH0VnEmlgEUEhybLQbHPmsIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپی میکنید حداقل اسمش رو تغییر بدید :)
تصویر مربوط به نسخه وب ایتا هست.
©
Ralireza11
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ایران در جدیدترین گزارش اسپیدتست نه در رتبه‌بندی اینترنت موبایل و نه اینترنت ثابت حضور ندارد.
تا ماه گذشته، ایران فقط از رتبه‌بندی اینترنت موبایل حذف شده بود و در بخش اینترنت ثابت با رتبه ۱۴۰ جهان قرار داشت؛ اما حالا در گزارش جدید، رتبه ایران در هر دو بخش حذف شده است.
©
itiransite
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UuKPDkqWhotZn-eZbUH8K1YV4xBy6x71lhn7J0TF604xpMqKpHWFI1EhAj8VBDvzhVBYk74ZuVIXOv2j-6ii_1qzPmn96t5rmL-HApemOr-KUcS9UDCPaGGAIEd0Hzpudd3fCKT4iptAkAO46zTy3QFNX5AM76GgCrTjKrBfAEhnqPNaFgNgMPeKiGmrgwJRXrkJEkPVMAgacxwL2gcerkuBORkt3DBAgW7wqwvrcAzWOa09-RFvEo-0cYuGyovByYvT-0Sy1kiY5k3n7qhZX6K8rTLdQe23OiGD8BXbb5LZ3MgyvH5mOY9eeodRIFI1Tw8NONHd0WZ9yA4F6F9XuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ju2Re1-zBxBqsXyivSn_iL1omp2lPzUpcuBRAhZlTP05-S1cG4azaC9bjksXCUpplqVxu2bDTMtP2MUbZnK8GhFVlE5q8BAt8YILLLO6MtgX14IyYN6glhUQ9gKOj5FcT-ssT9J-2l8bp5An7TpAQqE2YEl8WitzrWIZYi_CkqRccmk29LIFYjxB0wxy0q88z9-o38lbaSNS0AUAZRGLlfy3YHkTrXSEhllmJHAERjQzXxHDY0-ecdLOJkuqb73QWl4uZibtpH-ZYRaTC4bisIliZp1yZBOYZ2kZIkELnLNLakGa_VsXN5jhlnHwnIO7PFyF5RtC-cGzQ-JA4MdNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی خبرها
دیدم
که ساکنان روستایی در منطقه فتح‌پور هند، در اعتراض به کیفیت پایین و ناپایدار اینترنت و خدمات تماس تلفنی در منطقه، یکی از کارکنان شرکت مخابراتی رو به یک دکل 5G بستن.
امیدوارم برای وزارت قطع‌ارتباطات پندآموز باشه!
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h0JmRMRzGFivh4BOIXRf20XCGFdol-rYEM7mA7eE9MEMFGtPNsubdOf1etoEko6rwccvs830Qpi3KdgpHwim5Mc8qdQqyVUxqLInvR2Ydp1Poh8043SCMgYh--gcAweSvdu77kEzwEAtigCctuEU7vnQmaqo-0aIg_P5Jn2PjoAjEB_XH66fMzaa15G8ZEfYJE7Po2bIXM-9NEU0y8GxM3pd94Bt1yu59-RhyPz_gd-d-q4AE8gSrbuRQE4dCceke9atEwzuwKRMletrQNqobQRr__ZGMllfJrFb-iBlbBRKQSVnEMLvO__46pkyaYdrz9VgiWQf-aJiWBjjAiDu9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jx1cE57SH_TeefknDIaS7IbiRK9Ak5NAb_fQ0m5vS35Giv_N6L8qaGxgxihwiSY0xGXdArXDh_8VOTuKYCIrzEHZo0Gd0aoU0Nh9Aihi_S7iwBinxA9YWHVaR365qevi6GVhoMa5KA8a4smi22Jq2uJPKwaypB4UMHODKHmVb5VKTx58FEGwZMzYErDbx5xMhyY3m1gpvrNuy8ich_xMr5nvkrTVLfQJbNkQ4zKVA6jLcMySIZvRulBC6XBHOpGlSzpczTVyGIeSPR6vdzkf3Ew3F6-a0mi9KbJ9tolr-TAMQ1B6TX8AWk0ekR8uq-0BFf51jJuabfRIxd2qyXCjng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether منتشر شده و این بار Tor هم بهش اضافه کردن. حالا می‌تونین از تور بصورت اتصال مستقیم، اتصال Tor از طریق وارپ و حالت معکوس استفاده کنین. پل‌های Tor هم بصورت خودکار از BridgeDB گرفته میشن و Aether می‌تونه پل‌هایی مثل Snowflake و WebTunnel رو امتحان کنه.
یه قابلیت جالب دیگه MASQUE-in-MASQUE هست، که در واقع دو لایه‌ی مسک رو پشت سرهم برقرار می‌کنه. این حالت باعث میشه برای خروجی، رنج آی‌پی متفاوتی نسبت به یک اتصال MASQUE معمولی داشته باشین و توی این حالت دیگه آیپی ایران رو از کلودفلر نمی‌گیرین و رفتار اتصال تا حدی شبیه متد Gool میشه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IS2Qsbn1w0TZaruk4MJvpAcXSwZ8bIESRMr8m-0QtIdW_TxHicvleeYabDaWtvrhp10rt_swxYLcf3bVIspb4WDIVPs4NtYm5M9DSG6tMQeDHBjfntXLigkgemKJp8xYbLzvsVAdvMcSPbVUbgNR-rUoBywl_LaMPY08jzBh861HQU5LdIudtOVDyS_onXg_-yJpNhFAKtySSqo5xTeZ7ovznODa0w49-UKvYesJwfCgV0sRF7yCVk9tyEoOzGlr0S1YYpvF05UqAOKuO6qZEjAoESiI-42B0H0YwaoI9IrsAaWyrX13oudprFz3oTKWPxbHcZsS6bcf0n5RlcO66w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک، شرکت سازنده Claude، در گزارش تازه‌ای درباره سوءاستفاده از مدل‌های هوش مصنوعی، چندین عملیات مرتبط با ایران را بررسی کرده است. در این گزارش، ۴ عملیات مستقیماً به جمهوری اسلامی نسبت داده شده و مواردی هم به سازمان مجاهدین خلق و یک عملیات فیشینگ علیه کاربران ایرانی مربوط بوده است.
در یکی از موارد، یک مجموعه مرتبط با جمهوری اسلامی طی یک سال اطلاعات ۶٬۳۸۸ ایرانی را جمع‌آوری و پروفایل کرده و برای این کار ۱۵۵٬۲۱۶ توییت را تحلیل کرده است. در عملیاتی دیگر، بیش از ۵۰۰ کانال برای جمع‌آوری اطلاعات افراد داخل ایران بررسی و ۵۱٬۹۴۴ پیام برای ساخت پروفایل‌های روان‌شناختی تحلیل شده است.
استفاده از کلاود به تولید محتوای تبلیغاتی محدود نبوده و از آن برای جعل هویت، پروفایل‌سازی، توسعه ابزارهای نظارتی و حتی ساخت بدافزار و ابزارهای فیشینگ استفاده شده است.
©
RaazNet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WquB7-FncHNFNlsak99OsVZvr_jgYiy1IZs9kl8kNvxUzHFb20OvUSGcoxdjiZQr8RTJpr_bqRIRhWlE3Vl37j8_I2k1aG71r9cXystOCBektAudvRmurH-X2pBnzTs7K3hmf4rLVYAjO_V0Js5xHowxz8RNrH_Lvhpm-PpBIi5coge1-wGQcB0qQJChOsWqi6JPV_ZMtIJufJzcmjU_BqB1z4jy3W0yGLwMscmcPQd6TaFhXzxoX9cS8_blmoOP282xh9ExcxY8yWxc66Ypuolwlr5pVtceq-gF9PEgAIeZkedMx7d5w77hnSi4TFjj0NKHOk75u3lzBJ9QwS35_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون علمی رئیس‌جمهور گفته "۸۳ درصد رتبه‌های برتر کنکور در ایران مانده‌اند. این موضوع نشان می‌دهد بخش قابل توجهی از استعدادهای برتر کشور در داخل فعالیت می‌کنند".
البته نگفته ۸۸ روز اینترنت رو قطع کردیم، هزاران نفر رو در خیابون کشتیم و خیلی از همون‌هایی که کشته یا سرکوب شدن، از استعدادهای برتر همین کشور بودن.
نگفته راه خروج از کشور رو برای خیلی‌ها سخت‌تر و پرهزینه‌تر کردیم، عوارض خروج گذاشتیم، ارزش ریال رو در برابر دلار به پایین‌ترین سطح ممکن رسوندیم و انقدر محدودیت‌های مختلف ایجاد کردیم که بخش قابل توجهی از آدم‌ها اصلاً امکان رفتن پیدا نکنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GKctFD8TLqgva6CzWmkrdreCB9Ubjh0Dzix3kqG_fjD6wRMKEXn2oCvS1sQoIix30E1snnhvyM5ErvMLFAcCb4SMXDXV3YI2ylgFFgSsyQ_DBmcgexiUEieBq-ADeXtCxoM_qxnBknSVrzxv2ARo9JflXrXcIqT0mOl7nW7JFyw9OMJC7BpykPuI26QEzSF6Kh9jeB-z1R2N6Vk4bxoGzXldGXngcUnpBQAQDGQMU7QlErwoltQtnEihMx987OPvTv_sa6CIrekE1pTYg0sb4ItkfZ6AEA3KnKkjIIfEA--cxcGweqICUGUmP-6UAj07sEL4RZqEMwmRvC0W5Ifalg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اسم JumpJump قبلاً چندین بار در گزارش‌ها بعنوان یک اپ ناامن و مشکوک مطرح شده بود. بنابراین اگر از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hAO8E2aXf1W1eI0Leu8RhtCNrfE65w0vipCa6HvvCD96N0a57sKXEXZuGR6PS-4mVtrzCvJ3DLLTAMa82_qs6gAVQTng3ZRuiZ1IOjmszR17MVdhFht4a9XbbwXYlJg6mq3KKvW9D5pjJl-upNu56UK3mTXGau8s-Wk3ARuB6_qqN8FaxtozD8HHKEJibnOsiP-B37pRFeBvh_-Vh8EMvkuprrUhn1fVDj1PydH-Ywodio64PlkOlotEiV8e9ZIPXeyTPkpT3brg5IEF9cnvWu2zH8Rt_RK959brHAeYs3QS46t7QDXyXfW1hwH2VkP6aAWIfEKR92QZStY9hfd-LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qEp83MlLhcNupGXi1VI5eCELgB4EFb6dX39VPbEBS5KMWYsYFsoXdWrG548YzfiaQvQskKTh6vtjy6m0BQHMatCYju0ECtgidxj2PuEynz6g4EZvpk99nCunMcAhwJgKrFuEBFhcljQuCkXKRESF30hTkGYsazqOvaHfcpTaQ6SJUAeXUbwZEjfR3orWskWa0SHZXSkl5cBbo65D3JH0lu_Q9tL0rEwXOUl6Ao1vsS1ocGoQOtU3uRb8oibPd5oQRWLDEgyNJKaN7QTkVp6wubmUwtbD2vBCAsQclOQOlfSXmTYs2cmQgdxGX8JERDYn-A2lAkzM06Qom8Kc_fhTNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از مدت‌ها وقفه، بالاخره فیلترشکن Oblivion به مسیر توسعه برگشت.
در این نسخه که برای اندروید منتشر شده، هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
👉
play.google.com/store/apps/details?id=org.bepass.oblivion
💡
github.com/bepass-org/oblivion/releases/latest
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/afk30p7DQ1J8oTjlertoZRSCvk9rqXofTAoiUaAjYm2aSmRYtrGe0lgjaV1eEAZgKEJcNbIIaKwTfgu24OR_0IDtxxShZj1FDR5K-ODwDh2OBlFYIBzOtsTXOcx9GRfmDl1k8ciaaKhX1gL7FUpynL-Xl_O4hQF1sbpncfXU7iAuTx8cq7xIYT1i88l1PNhABvgNCZqr8qInqHpiuoQPEjvwWfvN-lw4pqsZe-WOK3jWoaRWjO_y-V3WN8r_AEOQghyBclYOcK4N4p_56gjUncs-ndbG1WfQ1D3yaB201JlWFzDzmCMedQVp2CzjXTvHOhnAGvuHjAFV0zjiQCjVYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل یک آسیب‌پذیری روز صفر با شناسه CVE-2026-85046 را در موتور V8 کروم تأیید کرده و هشدار داده که هکرها از آن در حملات واقعی سوءاستفاده می‌کنند.
این نقص ممکن است با هدایت کاربر به یک صفحه آلوده فعال شود و مهاجمان را قادر به اجرای کد مخرب، سرقت اطلاعات یا از کار انداختن مرورگر کند.
لازم است پس از به‌روزرسانی، مرورگر را حتماً دوباره راه‌اندازی کنید.
/فیلتربان
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/It307HkzE9Klq-z096qHakE3pHBkImt9euepPp2cigKbp5-RAkEFtcLRZ8HuvsL-Dwtvt0GtxOCVdi6vZJM0pM1mS60ubA-SrYg3Xy2JJTx9mTglmInHHukPNfYEWe8GJbDZOfnY4R4V7FjX114cwo6yDxQCuZqfn1wRNepGeHfeQx8DSkzdcwc06FnsHtcPx3PQUz-YV2GLCao5gko0Tr9_w47pOseloiftQmplt1meyEiIhfZ1PWviOArRUKDT60zq490O2alomUApUJ-hUrGxIx2b4SpEccCz_qBDXzeGVFfstnvMVh6RLDyt6pf71ZZ09b8WHiht9hSoWZrsLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیفیکس اعلام کرده که این فیلترشکن توسط تیم امنیت
پس‌کوچه
مورد ممیزی امنیتی قرار گرفته و تیم توسعه درحال بررسی نتایج و کار روی چندین بروزرسانی کوچک و بزرگه، تا در کنار حفظ عملکرد و تجربه کاربری، کیفیت و امنیت برنامه رو بیشتر بهبود بده.
این تیم گفته ممیزی‌های مستقل و همکاری بین تیم‌های امنیت و توسعه، یکی از بهترین راه‌ها برای ساختن نرم‌افزارهای امن‌تر و قابل‌اعتمادتره. هدف این فرآیند، شناسایی و برطرف کردن مشکلات پیش از سوءاستفاده احتمالیه و انتشار خبر این ممیزی هم بخشی از شفافیتی محسوب میشه که به‌گفته دیفیکس، کاربرانش در چین، روسیه، ایران و ... که با فیلترینگ دست‌وپنجه نرم می‌کنن، باید ازش مطلع باشن.
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CuJq-wXmYPqAVXo15TXK_1aaqcHMfgmDaoo_VaSfIf1GTiOOa2MdqyV_u-WxEYke5E4ZQSrrb_ZGdTO8MzAIOaLkJ3pQ7UnyGnbYcBajaoYnVj0KZ6B9iClYujwFdyyOlAea9QpD3NxusMIcx1IoYaWVQVx6GfSbdY_0EO0nw1H_iLS2qFtm2YtV0GxZCZP46Ei-uJifjBttDKoCefbBCjc5ZG8Nem0KguVNFmFPHuOoVRZn8B9GUwc2q0mhVKtLrPg4X0NZsZHbmamGEPjWWptVXJPg52jLfzAd7Tj5gtkcM4TdrntMQbM5kC601Uz47gEVUcmpiK97-kVsNTLbZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/myXl9vKw0VPbB3DYAAou4ocxzpx6ZIeO9WJJmlVomgM3gDOzB3mkkm0fur4LHN1R9cwtikhzzfFatePAvmdBocY1o-pZP53pl64IiSwPwJs39djsmAjiBKEb9iXRtI9SAKGKRXUB62jAvU5nYxCDzsz_KjfcmBV4SDxilAxE6UXvQt3ZfmbHYITsbjatQHjQsdmn7l2vaB0HSVTN4sNtIwyN_hY4BJMHhtuRAuzjykdrVdfjAdiXrNjmMi-uExZEurRLdtF4-Rwx5TBYm3bKwMsb1gDeCI1qvT_ZAJ1xYkKw2xx2B8bPt41bhoJl0JQQrJUVyNqHqH5uKYozkNLQng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سم جدید
😃
☠️
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VgUC5PrESYLpIq2MU1H2BF3wkagb8_-zy8GYPMtNfwuWnoG4Drg5R5vKc-GLQb0h7MH0hzyRMOiihuh4XtvKMNPM15rHXUY6TQikBMow56LAKz7l5uXDKJCbdDY6Vp0eCwpC4kIkY1l2bI9OcUFsDJRfhtWS1Wxni-OcHj2vI-tYpvZ3Do0qau7R09Oz8MvVzU88DL4yYXZunnCxBYPhNOA7YyZwd0rQIC_j4RbV9ebfluw5LRUU9r5qNsh6i3HhvmeSXXDl30lyc7tNEeElsi3GL21R3M5iChIcdXXnzSwENMrUhfreudQEavltZC3nDX7CmrlNrqbvLS9XSqt55g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات معتقده "قیمت
#ملانت
به اندازه سایر کالاها گرون نشده" و احتمالا باید بیشتر از این دستشون رو توی جیب ملت فرو کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U04-lwXUw99N_18ben2W0rv_rI4knSJH6cTcuOIK1Us-itM-vxZQdrJgAiYF-HFJdviiLzX3NdIS9gwUkXzHVBqCbQHkFk_Sr6GvwMAOkLRigNL0ql3h0YD_IgD6_RNJUa8qpI5J2Iq0xUHs_U3JiNhbVwRyp6vECQJpVHBAyUgAMYzNISvOVGGJQTqghRh8RsFJ3vnGUxOQN1HQtH8IiyZEX2P-4K4c49TK0QOqYv-y1_eFzPldukTVCaqayemZmwkn7j0zHh49uBAio72IiGEGTGB1pue-FQJneNIjLw3C9DpUoHbFko587dqE_5dO_fMk-wpACSt5Bd6m_Bx5jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واحد امنیت تیم پس‌کوچه در ماه‌های اخیر حرکت حمایتی قشنگی‌رو شروع کرده و اپ‌های VPN متن‌باز (که در ایران مورد استقبال قرار گرفتن) رو تحت ممیزی امنیتی قرار میده.
طبق آماری که دارم گزارش این ممیزی‌ها تا الان بصورت محرمانه برای ۷ فرد یا تیم توسعه فرستاده شده. اکثر این اپ‌ها درحال کار روی بروزرسانی‌های جدیدشون هستن و بیشتر از نصفشون آپدیت‌های کوچک و بزرگ داشتن.
این‌قضیه تقریبا برای توسعه‌دهنده‌ها و جامعه‌ی هدف برد-برد هست. اون فیلترشکن‌هایی هم که نسبت به مشکلات گزارش‌شده بی‌اعتنا باشن، به مرور از چرخه اطلاع‌رسانی و توصیه به افراد کنار گذاشته میشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MGB8idA-AiWEXpbkrqZblTOd-LumTIPDaSq-BaOJPpCnymkE5RN0j_8upvEDktFtqC3u_xGE83P-vVhHyIwXG_TTsZ5whqoQiMrpM0pYtwq4CtmbQ39NX0sR-04V7h9yZ_uIAFcIAxKd8LxZhCV1am15K6TR1LU_lDHqUDjMwmSmFDiuLHuMlqg6Zm6HSblbAJtQEcnJMQz_Ke7Bp5t2tO2I1N_FPnwwqq1VJM6-nJwCkJ40Vls2_ndMO8eeFhEYQKZCuL-_EiAqyz-FVllpEA6lcDuwqBlqyqOava925wgWh-Uy5UcHppux56vOMhUv_s6mQt2sXHWz-nuFITpWfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cztZF2uZ7V1EfziSioWrzJn9rXd42KS77rZfgBstKeKGrYNlM1ufTfPjeEQvMP8PG5yCylKlj1u5huNNBT7x1UnCjH61KQtb-Q4XPXWMkliGTEigJ-FtbzH7M7_lE_yjazqh0WXjxU5ABfZ36pE4Mw68iHR5YSxffChn1bIyuZmOsfkAzRQwELm3qLQF3wMbKHoSEjwAP2Jl_xn4cF_03Kv1v1rNuw31CnqubAKLvKiEqN8jXVnHLTVJR1djYjSz28o7MhRFqGMR2cToG7a750q0CpE8ri39FHddUEIY50snJRGGy8BEe815-hI-OCWTGJhqr6_PNRpV6QKwEBbkZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nUbdZ-VN0Z6tkbezygaEOtGQOdMZAV_TiZyvC7TPt6nBaIut9BOPsaa8BxemKnIOMnsgON0vBOB0YQVfNypYkvjey_m6K1fX8v26ZJG3NJpWFZspgnPqmBMtM6ZNE40CLrhtMqCb0Mc4Pn-MYiw7ZeHDaVe3n9PB2gW1l2Q_IKmusmkpBLLjuy0dS9ddJzJJPXBfz8c2xbrpeAabw015FBaiRHGZ9gWQIykfv384Kbx93kGZb5ITflrLRIsxj_LiFpG4bUa9FbsR3aWgAcaXXHM8qRlIEG7s66GfPugXLaR6DAbiVqMNicHuOOpsfuoppbX4tGniNatOj0D5sfT1MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسپین یه ابزار رایگان و متن‌باز برای ویندوز، مک، لینوکس و رزبری‌پای هست، که دستگاهتون رو به یک هات‌اسپات مجهز به VPN تبدیل می‌کنه تا بتونین فیلترشکن رو با همه دستگاه‌های خونه به اشتراک بذارین.
کافیه لینک VLESS، VMess، Trojan، Shadowsocks یا Hysteria2 خودتون رو وارد کنید، تا ترافیک دستگاه‌هایی که به Wifi کاسپین وصل میشن، از تانل Xray رد بشه؛ بدون اینکه لازم باشه روی تک‌تک دستگاه‌ها VPN یا پروکسی نصب کنین. درضمن اگه تانل قطع بشه، کاسپین دسترسی اینترنت دستگاه‌های متصل رو قطع می‌کنه.
👉
github.com/Iman/caspian/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u4BP3aWiOIqa4pOS0Qjsrdx_0R7O6BnVHOWm1DYbD8CaE6mPGLFncwNuQT4k6lZif_tyyMnIzz4NShs0gY8st4UdODC4h1bjRCf5KoIwdEj3SYAHjwp7y9fEYAdVuJ3wLt-XYwtHMOIlqB7EX4fGLkYWMcyG7ZNJY7d6ReQjhlOYW0qzfKBULF1PEiwkzh9AY3W2CK8x4_STNN5uLZn-Sv69U4DRtxsijczMbPfG1miNzcXZbB2OIBUTczNAS3j5_TP0YeNfYdXCFkthhx0QP5G6cr4ML9Kbx2Ydt5KyDFXPtC64n6JRcSmploj-j9-Gkg8d0pHwVT1O0Rj13VVEWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Misga یک پیامک‌خوان متن‌باز و رایگان برای اندروید هست، که به شما اجازه میده پیامک‌های اسپم، تبلیغاتی و کلاهبرداری رو بصورت دلخواه فیلتر و مدیریت کنین.
این برنامه چند فیلتر داخلی برای اسپم‌ها و کلاهبرداری‌های رایج داره که می‌تونید نگهشون دارید، تغییر بدید یا کلاً حذف کنید و فیلترهای خودتون رو از صفر بسازید. با Filter Studio هم می‌تونید با Regex یا متن ساده، قانون‌های جدید تعریف کنین و حتی از هوش مصنوعی برای ساخت الگوی فیلتر کمک بگیرین.
👉
github.com/mirarr-app/Misga/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lzkaFQN4wAZUvFdqD8SRT4Wg7Fk1bq-NG4B7fm-RFx5vbepMPwOahDEO1XrXikEFe8AJAHP_KvUES8JAFEE7KiJpQBIt4f0G_QHYlsTyNwYhdRYQ86taEA-qGPKh3gYPvYVGgVfEATtWOJnwADO9d94BgxPzQpwFF68LlJfC9zrwbca_iRAg5fwcX1JGuEReY4enH3biZ_z3cyM7minnuVHPxJaS-MfvG6wDFyLxc81byXxlCqOpn-VXGtd9rJvZjjLNatz-rCq1A3mLAGVGpGIB2Jaw753UPBeBGswEqzMuILczq_Byww89Vs18bm7a_s56jBeaUExzl50AGZp0Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند آسیب‌پذیری بحرانی در RouterOS پیدا شده که بعضی از اونها در قالب زنجیره‌ای به اسم MikroTrick در حملات واقعی هم مورد سوءاستفاده قرار گرفتن و می‌تونن در شرایطی دسترسی کامل به روتر بدن.
از طرفی Shadowserver در اسکن اخیرش بیش از ۱۲۲ هزار MikroTik با SSH باز روی اینترنت پیدا کرده که حدود ۳ هزار موردش مربوط به ایرانه. این عدد لزوماً به معنی آسیب‌پذیر بودن همه این دستگاه‌ها نیست، ولی نشون میده تعداد قابل‌توجهی از روترها مستقیماً از اینترنت قابل دسترسیه.
اگه MikroTik دارید، حتماً RouterOS رو هرچه سریع‌تر آپدیت کنید و بعدش لاگ‌ها، یوزرها، Scriptها و سرویس‌های ناشناس رو بررسی کنین. SSH و WebFig هم بهتره مستقیماً روی اینترنت باز نباشن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cf4Bfw4o4vNhutLMp-mEHEmUk8x6RUCyydr_aMmG7pk5cqH_sqravvFGUz6h1t39JijTHv4XctWMz3Vftu9Z4RZ7cz9rUo_lIcAXIH82OhL3L4SUUMgjb2gMk-4q97ofj8vbP-zlSgBObxWuwhnr1aHp2bGICBGKoQuGyljVkAteHNfBM_0z_wc3NDvd_O3zooRlFXZSG0B3xzkTNFKc6eyq7wfWbaGbu2P9LKJuuF8bcaERzulMPXfW1a5m2_cTGghZilTAJ9seRY3jT1z4gqzuT3AvYOJKe5u_AvVYsZEj5f2A0djpUVVgpJFitn6nw_Qkjr-Nt0dg0F0h2z45Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه یکی از زیردامنه‌های gov[.]ir به افراد دارای مدرک فوق‌دیپلم یا پایین‌تر اجازه ورود نمیده و حتما باید لیسانس داشته باشین
😁
©
SePeHr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B0bo4-Ais_kbXJXh5CWVAhMfpkrdeeGyOe0oFtsN8kFDt54tkn-sjL2hZfx4oqfZSuErf4McN4TdRb76nK5l8TrHOHXyuQb0GIqrnXCRnGE85eONPwYfu8sUAOSvUQrgZxYw0FhiSL-lwgcTgsBu9-sFXYdHaaoE4IXl7C8OC3loUHxXBjuCJxmuc72a8afAn7QJ01a9J6SVf6cSUDwq_HmqzJi7GyWCMQWvdrUc0xhCzXh6Q2uJFQ18UhU-oyZD7LzOvA3zLO0BZUM4W0NgKdQ-30AN09ina2WmC1mYagZi41ugKQ5Sq6lGNoD4f3aSlHdwIxxKgW-qfNOy8zuBGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن متن‌باز و رایگان دیفیکس اطلاع‌رسانی کرده که امکان تغییر زبان رو در گزینه Diagnostics & Experiments مربوط به بخش "ترجیحات" این‌برنامه قرار داده و حالا کاربرانی که به چینی، روسی و فارسی صحبت می‌کنن، می‌تونن DefyxVPN رو به زبان مورد نظرشون تغییر بدن.
البته این‌بروزرسانی بصورت آزمایشی از طریق گیت‌هاب در دسترسه و بزودی از طریق استور هم در دسترس قرار می‌گیره.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ایسنا خبر داده که
#قوه_عاقله
بخشنامه مربوط به "ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها" رو لغو کرد.
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">حکومت در حال تهیه لیست IP کاربران و در قدم اول مشتریان دیتاسنترها است.
در این طرح شماره موبایل + شماره ملی + آیپی به هم وصل می‌شوند و بدون ثبت آیپی در سامانه شاهکار، دسترسی به اینترنت ممکن نیست!
نقض حریم خصوصی کاربران و حق ناشناس ماندن در اینترنت با قدرت در حال اجراست.
©
souzangar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H7ftylTcrS-qsDEMzq60pChwxGQjfTCx5fpdz_uw83mCO-E-Z4TgyZmd7j6p9m8IwgYoEiGhNt5V2AkunPYVuXXCsiCJBFtFcBfiGlD3Tw9EZemN1dqrmM8mK5cMNgcOUaQzWtjN83L8VHqppHFavlCAdozXcX8WPqvQyOpTSCd38LY59UeGAWMZnAIU8SOcrO0827qYa_5AvRATXklm5E_DMyz5ehuzz75P-navQQMxXni8ZNVGwHjfzRFLZXrM5DsVg3iqqH8ij_r2RBYbUB0HzMKpPo_Guy0yk5t-SB1NWoNMu-SpoUqGCyT2f2QjdhG7ViUksSu-hrNOdjs3IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether با تمرکز روی بهبود سرعت و عملکرد منتشر شده و مهمترین تغییر، فیکس شدن مشکل سرعت MASQUE روی HTTP/2 هست، که حالا با اصلاح پنجره Flow Control، مسیر ارسال، فریم‌بندی پکت‌ها و MTU داخلی، باید در شرایط مختلف عملکرد بهتری داشته باشه.
از طرف دیگه، محدودیتی که بخاطر بافر دریافت TCP در Netstack روی همه ترنسپورت‌ها وجود داشت برطرف شده و این بافر حالا بزرگتره. ضمن اینکه می‌تونین مقدار بافر دریافت و ارسال رو بصورت دستی تنظیم کنین. البته برای WARP-in-WARP چندین دستور جدید هم اضافه شده، که اجازه میده اندپوینت‌های مختلف رو بصورت دستی مشخص کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c9jUtPhUovsTsKhD7Qef2EwE_uzV6ETEqKyvxoyQg0gaJWOF46bVJgoDVgP5f5mmenmZqgg8d9UvZPBvf0KLrvGvb7tXc2tuXvMFShVgOpJcVdq-phgrwj0POApEFYt_5oZubXPKWZ7xNgVBSiBWdHtdwBipGYEMw-KU2q88-_gf20hUN4vi2FbmpctkViBW-Dcjn3COyop-1aNVlwivVX_EFu_yLCTPLK1cF8iTYrUwqbbeE0xSTZHyyQSkiJvO15UxjbSnAIYZn3OXW6PaKxv77FEXBZGuyowCRgrzsn3qzpIvSLeW1GjNyxNJ5FU5JjfCAE2g-U-8MazzDh-L5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ljkie2bku2ttFjwBVlAJHVTdjHtHaW7PNWjmBnWiP2Chkh1cxn7uJeQ5yqfQman3OVDB9BJesIPdQ-Ki6Ezy-JHjqkhI7eJj8iOcG5pXYxTO7aelehKGQsvMouabtUDY7y75doVaUcaXITQnkMrp_Knq6PsSfT5dqsEFYTS3Bx9TbaKIWg5GICYNYNvI6hsF0eEoSPVeuftC38GdgmJGIcm4Dif3H7qtgKcjIb7lsJGDkn0fxC3DH7qNJlc2U8P8KJ2IZC3-w2mHUBm-iyLygx6E1A_NTzZq-JepEfK5eYrp_3soFgzxWHvqtA5Psiy_PIsjm-iixqWYok3JogSj9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه باگ توی واتس‌اپ اندروید پیدا شده که روی بعضی گوشی‌ها می‌تونه اجازه بده بدون باز کردن قفل گوشی، به گالری و عکس‌های شخصی دسترسی پیدا بشه. این کار نه هک پیچیده‌ای میخواد و نه دانش فنی؛ فقط فرد باید گوشی رو در اختیار داشته باشه.
ماجرا از طریق تماس ویدیویی واتس‌اپ و گزینه‌های Meta AI انجام میشه و روی گوشی‌هایی مثل Pixel 6 Pro و Oppo K13 جواب داده، اما مثلاً Galaxy S25 Ultra جلوی این دسترسی رو می‌گیره.
©
notebookcheck
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">معاون سیاسی دفتر رئیس‌جمهور گفته "پزشکیان معتقده دوره محدودیت و فیلترینگ گذشته و اینترنت طبقاتی و فروش فیلترشکن به هیچ وجه قابل قبول نیست".
حالا حدس بزنین رئیس‌جمهور و رئیس شورای عالی فضای مجازی کیه؟
جواب درسته؛ مسعود پزشکیان
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NcMi52xgPopzjAwKKU7Lv6GA3efGl9RiadTJcVFyKmoyA2wbkwP-Bd04ro27pwZBo6LSpJoPg3hEOydz-4hz00SRnyZa5sJDDsXnhUVAP74GCkOdUe0zOKMGPe7wOoUrDUo56DSWw3bCnpB3fHlFcoUztnwP4eUP6oWnzdPjCoegpGRy9dqu6Q1ZyYl4lj42VNV2ufVAFsvF-mat-LT9N9c99x_kUEH2hHM-h7SmuoJlQf--gaow2MLqby-8AQQb4iRH5qEnw_HxzSNT60p-uSzB6CqpUGrQEUbDogvcQpVhWrltK6gvYe1DLZk-3juRq6BIHOG2AVuif8g13GFqHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Echoes یه ابزار متن‌باز و رایگان برای کارهای شبکه و توسعه هست، که چندین ابزار کاربردی رو یکجا در اختیارمون میذاره. از جمله امکاناتش میشه به پینگ، اسکن پورت، اتصال SSH به سرورها، بررسی اطلاعات DNS، WHOIS و IP/GeoIP، ارسال درخواست‌های HTTP و مدیریت DNSهای کلودفلر اشاره کرد. همچنین امکان بررسی وضعیت سرورها از نقاط مختلف دنیا و مانیتور کردن آپ‌تایم اونهارو داره.
👉
github.com/SinaXhpm/Echoes/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ETi6w7jhlQSgW3CUDrM37g4xTjwFKHnb-0rW_pNv8cC00wPwPgzov9BSkr8VM5CIdcW3RyI8DgTLGR1hgv6kBtuJ0zOzPJVjYjaVd5OLto8cbMGEAnyRa4XtM0qzK97Qe6UWY9LESkhT-MPABMYe5LVOB_buAWgIq5znmQa5S7Vhs9WX_hkg7OaIU-i0FeXDqA0ovMWKCIjwStFDjfWDn9RANCT2RaTbBcFk6RQGXa_Pas6X_yptP9Cgv1D2bnJIveyhilR20AiId4_Kyspffq5bOpO-BxFJPLisk4iHmNfiTaXn2-Z6lV_mxguOK6_bkwTKR5piUTXjOe7hzxo44w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بانک مهر ایران!
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uko5zKB3YuS-3oFsgQ8cIGvjnVKByLVLEc8WWy2_l1RCS9rGn_7Sqs6uhNVcZilb_6ofHTkuK6gm8v26tXKtCOu1Th44GL9yM9p2phB5UGxzl2QoOteswTgdeWP-cZCqoKogkWHFIHfMr-WfSfWq3JNKnpzQ-zW_gzEAd_Pe_I5izk1OxXaoPzx7T3FS2Fjnad6JNJ_1KO5UoDPYu5Rb8JhZ4FPMeQoEglEB1yGPEzPik0ceW_bFmhvGdxAz4PDk1u0nMKTOyyPL02VFVeFUb7oCGHVaCtoaFIAZOjRDwPC_UG6uvnvj9Z2MYzcU2epfbrveRgyhgZanWVEthhO9aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که بانک مسکن داره، ستودنیه!
کاربران پیش از نصب نسخه اپلیکیشن همراه بانک لازم است، ابتدا هش نسخه دانلود شده از سایت بانک یا سایر منابع را با استفاده از الگوریتم استاندارد MD5 به یکی از طرق معمول محاسبه نموده و مقدار بدست آمده را با هش زیر، مقایسه و در صورت یکسان بودن مقادیر از اصالت و یکپارچگی نسخه دانلود شده، اطمینان حاصل و سپس نسبت به نصب نسخه اقدام نمایند.
©
alirazzazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p11CU4YgPF6PyC_ocPAq8oeTyOHuT0mNmT7uBSttdhKuSV-o6Yk0HAPOhCE-g55thYEVxjl0IEh0nHO0dNUNKyhZYZTQQX4iXU9cY22fNNaAIRaBf9ghVPSrxxQ2oGxp6yv-E4pWt4Tj-xlTPmkHs1WkYkdT9CHcapMC6x9WBQUHObQcmYOQVD6HgVUue1ZrV-eRCfD3zVqlrXgY68uyiBLe7vOk1NnTCwDpD_xbiJLSe4rSpngLcsqP1nQpKSuDuHucnTpIN4EUKO5rL3zipZeuLfFq9kVXgAGmb47NuLbZ5FLhPx5K7_kqx_SBghn3BGprkopiNQfwipM1SkKgYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دستور پیگیری فوری
#ترافیک‌خواری
اپراتورها به کجا رسید؟
چندبرابر پول اینترنت میدیم، چندبرابر هزینه VPN میشه؛ تهشم آشغال‌نت تحویل می‌گیریم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/InpjtD-d4jwrrC1mlnZqzQs-G5nwY83-5_AvaO5TvsYKuxdAr_lEfJExVY0b092A757HEyMua3z6myvesc9hhNG0y_Gne4jnZj0EyxKv2DsPJTPsfIA7V2weWXJ9cqYzcqGYLPKtpjg2xrw1DDdEt0t9nF9KYbq2ScofE4gDj2UGWB7wxGO-yEAPxo9MBwD4lI0QWuDysljZxxB-MCzyR1709k0F1L7E3EN_-SepFr52XeP4eKiq7umYUkKLoUgSiwk3wPfh1ddVnpGsTElrdbwv_O0UA46TDeyGn_XhMU1bgu6Fs26KXEZNfpOHfdagZr8dR3-iNXqcbt_Z3ap89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پانتگنوس یه ابزار متن‌باز و رایگانه که برای پژوهش و بررسی‌های امنیتی روی فایل‌های کانفیگ VPN و پروکسی ساخته شده. این ابزار بصورت خط فرمان و نسخه تحت وب در دسترسه و می‌تونه فایل‌های رمزنگاری‌شده با فرمت‌های اختصاصی بعضی کلاینت‌های اندروید و دسکتاپ رو بررسی و اطلاعات قابل خوندن مثل مشخصات سرور و تنظیمات کانفیگ رو از داخلشون استخراج کنه.
ابزار Pantegnos از فرمت‌های مختلفی مثل SlipNet، HTTP Injector، DarkTunnel، NapsternetV، NetMod و Happ Proxy پشتیبانی می‌کنه و برای تحلیل و بررسی کانفیگ‌هایی که توسط بعضی کانال‌ها و منابع مشکوک منتشر میشن، می‌تونه مفید باشه.
👉
github.com/FrontierTM/Pantegnos/releases
💡
frontiertm.github.io/Pantegnos
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YgDHp3kizrmZ5e5HDw-K1jmKuWx-448DRIRxqPN9mrhB0kiXxnZzBucYbQaFdA3VciC8KY2LXOCM8KelZ1WhmAlPqJk43Fqx3zrulaXS28p78HxchvI8pz744X7soV6E0HaCOSWykW3aMWawKdSm493-AOYiSMGzcCPb89x9rClVOsNGuGYsESBGqIHl78njh0Mf7hggVmOwp-NiFqVcCpavxoRI_1ZzBMnPQESwhRqENZvvTHw736DBxbTm1nvHIbYqI4qB3DTj-BrRr-E8nNAd7ksZV_ieinJwN0wO9aOWjJS-tvHXhtxqUMabfwFP4K0lOWW-brP3m5Rb8vc4Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپیس‌ایکس می‌خواد Starlink Mobile رو به یک رقیب جدی برای اپراتورهای موبایل تبدیل کنه. این شرکت در گزارش مالی جدیدش اعلام کرده قصد داره سرویس اتصال مستقیم گوشی به ماهواره رو گسترش بده و در کنار شبکه ماهواره‌ای، از زیرساخت‌های زمینی هم برای ارائه خدمات موبایل استفاده کنه.
©
satellitetoday
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iBa-WYp9pfStrm0aa29DSKgxocwzwCttQa70VIZUkQGV4lGuw4Lm5tDeDguCsL0bGVu8kpZmt07mCSFEyh8ZLgkPVTpHXRxcynVUTdJlJDK90-Xp2AoXjkXMX1cRBzN-4uWKe0gVqg_k21d2iYCLbrwzN51v8yprnPYq8TeOiCevcz-MBartSsDUtwNIqfqMPDP9GsbGfeh-6oiX6nhZqdAFkzXvrQj4047XMlctKsA2mMdKAFxxlJ9AFBjm4B-dVwa7fHs_6hDjw9v1uI09p9f_aqRBIbrG3Sd98KGOpVYlTmrVwN-bw0QyS2dT_FhsFrK14CUzAp-EvteRqqqWgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vkRc5pqGobj9dadcRy9WpdusbjS5tDazVTrhdEStzDNNGw4Um0Ewqb_fwc-0YOXypg4V607urvnNkoDIpYNckfHpKVy98bIxycU8vljw3SdHGJ-nGkbxPmrCaAyNVJK7E7OgXtXY2V5tM7w9OsTdy5TgHs8nRwlBFZygg7U_Qoyh7p9QPUySCWN-EAmYytscHCO0RkHVxVa-7VaIWx0vNso8ErI_Zt_347vQ9K0ptO-Sd7Eof81oRZWBo8tiGqHycB2f5PsBNRwfRTXGAskAPZoayfMOD4zbpzrbWhSMGQUFYT6dlDrt3RNVA4LI17W2sTRyIU1-BH_OLgX35zQApg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام داره روی یک نوع WEB Proxy جدید کار می‌کنه که ترافیک معمول MTProxy رو از طریق یک WebView داخلی و روی HTTPS یا WebSocket منتقل می‌کنه. در سمت سرور هم این ارتباط‌ها دوباره از هم جدا میشن و هرکدوم به یک MTProxy معمولی وصل میشن.
این روش به سیستم‌عامل خاصی وابسته نیست و نکته جالب اینه که دامنه این WEB Proxy مثل یه سایت HTTPS معمولی دیده میشه و فقط درخواست‌هایی که اطلاعات مخصوص پروکسی رو داشته باشن، صفحه واسط (Bridge Page) مربوط به پروکسی رو دریافت می‌کنن.
👉
github.com/telegramdesktop/tproxy-server
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DC8-GT2XkT7ZMJ2-sGiqxAw4LRd9saiS4UN6PG2F4JeqE82xhvIKDXqYSpWlOtftU5ruk8Ys5RCxQhnhF1EyEW_pX05O1-VaFDIGZj9QUA4lc1HxGQqrrY3LseZtFjR3BWowU6qbNQAddj9DqJP1G55LaUQ4nfhejMKMowluVMU14I51_lmfU5cdQ-3ALqVv0MN7lGqNrBwFdvO9Dv_Xj1h7RB55dKXaVOAsQqARBhWYJDEzg0H_vlALTEywdpg3IhEPEXQe1bCRX2GWFyIhlKIjfv1yaCxOTT5In-x8SzxNEowm-MGIB5SoWTr7SbT6m4-U2P3LRuHxPz66K8-42A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدهای نسخه دسکتاپ از تلگرام نشانه‌هایی از یک پروکسی آزمایشی جدید با نام WEB مشاهده کردن، که از WebView و ارتباطات مبتنی بر HTTPS/WebSocket استفاده می‌کنه. این قابلیت هنوز در حال توسعه هست و مشخص نیست نسخه نهایی اون دقیقاً با چه معماری و مشخصاتی منتشر بشه.
©
telelakel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SRayvzPxIyXkXpfOpMoyji5dN4LK6NBebM53PglhH3uuTapf0d4eZqjZN5vhuPLvN8TH4oKbmZk8txn8ZPremIoPHW73fRVyRiz9_xiqpO_jIPVSOy-juNO5N1RtzYi62aKSNVxC9XpksLP-Ly1cGHx9BQtA2C5iNcNqmerhBoieCDjVwfIG21zcqIcfMZ7Rd05FV29nDQoNu7wR7Vho-_c2eBwYZXrQ1ObstZYkrBD5uZlp-kIr6nzJtD4QYhfSQdaB0zGGhyuQKB8jIxaLB7cu-4wHAgEC8HGirDtM0WQsWGS4c7-z1lnsANHZ1S85e-iLVr9C_tHVqhYhxDgcWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا با همکاری سازمان ETSI یک استاندارد امنیتی جدید برای VPNها با نام EN 304 620 معرفی کرده که در چارچوب قانون Cyber Resilience Act قرار می‌گیره. بر اساس این استاندارد، VPNهایی که در بازار اروپا عرضه میشن باید حداقل استانداردهای مشخصی در زمینه رمزنگاری، احراز هویت، مدیریت کلیدها و مقابله با آسیب‌پذیری‌های امنیتی داشته باشن و این موارد هم قابل بررسی و ممیزی باشه.
البته این مقررات به معنی ممنوعیت VPN یا محدود کردن دسترسی به اونها نیست؛ هدفشون اینه که VPNهای ناامن و بی‌کیفیت از بازار کنار گذاشته بشن و سطح امنیت سرویس‌های موجود بالاتر بره.
شرکت‌هایی مثل NordVPN، Surfshark، Cisco، Google، Palo Alto Networks و Airbus هم در تدوین این الزامات مشارکت داشتن. از طرف دیگه، ارائه‌دهندگان VPN باید آسیب‌پذیری‌های جدی و فعال رو سریع‌تر گزارش و برطرف کنن.
در نهایت، اتحادیه اروپا میخواد حداقل سطح امنیت محصولات دیجیتال، از جمله VPNهارو در بازار خودش بالا ببره و اجرای کامل الزامات این قانون تا پایان ۲۰۲۷ دنبال میشه.
©
techradar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XZPLj5gWtRGSiApCE_K1faXLSNCj_o1waTf4KeQxIqSXd3zuP1wD1UTtqoIULtkjX-AcQQLeAOKMG2nqDFEyKHkFjhUWad_Yo6ytcvt8ze3DTvY05-6NFe-N6xnXLFb16d3G96wEIufxI7fXZPzPxBTrenh0DHJZwVTq5rQePilPn_yVkFFbObObTmCIhK6SsBjHgHDgBIbL-N2z8XLUr0Q_NNTOCIZnbvoI5V_c59GPjmmmK2keYeMayNzCrqgRRT3e6VcXQd4OMRv55aNoR3y0qGr5FAcSUBAw-9a4W-YMcTcQ775QEf4LhW-6sMbL6hbTXfTdgD2dgwNvniY98w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم پس‌کوچه با بررسی نسخه اندروید فیلترشکن Line VPN که تا الان بیش از یک میلیون بار از گوگل‌پلی دانلود شده، ۶ ایراد امنیتی مهم در بخش‌های مختلف اون پیدا کرده، که در سطح بالا ارزیابی میشن.
مشکل اصلی و مشترک در تمام این موارد یک چیزه، که اپلیکیشن در چند نقطه حساس نمی‌تونه با اطمینان تشخیص بده آیا اطلاعاتی که دریافت می‌کنه واقعاً از سرور مورد اعتماد اومدن یا نه، و آیا هویتی که برای اتصال استفاده می‌کنه فقط در اختیار یک کاربر مجاز قرار داره یا خیر.
پس‌کوچه این وی‌پی‌ان رو بیش از اینکه سپر باشه، به ریسک امنیتی تشبیه کرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JfX9ytRt6u0SkOaOqdU2M-3kK4nDr884N83CNWQBSbdi1REB-M9GRM6LqXx7XTHuiqmqePpyoUuX-kMgaCNN8otanK8yEN8oj8AG5Rp4jhRQGkbwQL6rVNE8ong6JLV-VEPbKrJee1wZuV19-ij9EV-sSlLVREvmjIis61d3HfC4I9miTisUfS09RgrCRPHPVE39QJdoWjceNmLH4BcwNfcdviacUtS26gh_GQ3iFSxZ7OKwBjXnoR1qCmaoHBjgCNsJcN2c5FytUpkMaoBLNv_sM8wQpdoOGjTpUZHDc2lNOUQ-Bzs-5BZjrgssMgk0D-iqXQ50SMvdyt2_NfvpEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ایرانسل و همراه‌اول فکر کنم یه بسته رو به چند نفر میفروشن.
©
ali__m___i
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ظاهراً پلتفرم شنوتو، میزبان هزاران پادکست ایرانی، توسط کارگروه تعیین مصادیق مجرمانه فیلتر شده است. طبق قانون شش نفر از اعضای این کارگروه ۱۲ نفره از طرف دولت هستند. دولتی که در «ستادش» اعلام کرد دیگر هیچ پلتفرمی بدون تأیید رئیس‌جمهور فیلتر نمی‌شود!
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j1yaB4QwUFFK5OnpZfcprzIYU77203jThNFwZKwUhQWTJUw-UD2olIk-lAtEDLhfxuD6ijfB4mER7MVQ23n0HaoUST6DSnUEy0z-_hL3bSBwgv2v-4yRXSQaae7-44gVRWPPsZ_xz3H3irhBqG7E9SCKl4pe_fj0S7AyuspnnqjCWalT99YwDD8n9g3x-f_OlkGWl6IypZruXUVmA6Dq1K0saY4rmgsbJWiIkeDZrOln8DKlTdjxd294PIGuZ-t7Ey0rIvXCI5ByCs3_YwhgpnyhJs5dPwNwrctBH2REo3OfsAy_YAUb2jWdraOHR1lq7D_kWr76XcCoxoP70VwmiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران شرکت امنیتی Socket شبکه‌ای متشکل از ۷۳۷ افزونه رایگان VPN رو در فروشگاه Chrome شناسایی کردن که عمدتاً کاربران روسی‌زبان رو هدف قرار می‌دادن. این افزونه‌ها در مجموع ۷۵٬۴۸۶ بار نصب شده بودن و ۲۷۴ مورد از اونها با جعل نام و هویت ۶۶ سرویس معتبر از جمله Proton VPN، NordVPN، Surfshark، ExpressVPN، CyberGhost، Windscribe، TunnelBear و Cloudflare
1.1.1.1
منتشر شده بودن.
بخش عمده افزونه‌ها پس از اتصال، تمام ترافیک مرورگر رو از طریق سرورهای SOCKS5 تحت کنترل یک زیرساخت ناشناس عبور می‌دادن. در نتیجه، گردانندگان این زیرساخت می‌تونستن مقصدهای بازدیدشده، IP کاربر، اطلاعات SNI و داده‌هایی رو که بدون رمزنگاری HTTPS ارسال میشن مشاهده کنن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IcKjhrBXu3VVfaEJz1JA2HSp8pQaPFJPT1kM02nEhlZDRHq6qQpGCpiK0ysjOOinoUaffjw_578GedjEzNt1_7wB5ZsJDa5TgEvl5Oqqe9foOqRaVqpGkLS1RZeer_ZXGgR-a5XBjySt0Qfa7S91qZZ1zVZVdSFLm8RdBYGnvHdGOJvqFFdHwXeTWI58k0SOCNIjMTRWfHjJgOnrrPhyHPzM7TnihhhgDZjHnN8diRTsHmKKfL6y49zcJ2YJpZA1fdbCqH6WGN7OsUUfVMzfQpF6cOFd5sTe483B9Im9UAleYyJfraQK5Iu913MkGPOl-cRdGnZLKCwPx13HqE2fwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteVPN یک VPN متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که بر پایه‌ی هسته‌ی Mihomo ساخته شده.
این برنامه با پشتیبانی از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard، امکان اتصال از طریق سابسکریپشن یا اضافه‌کردن دستی سرورها رو فراهم می‌کنه.
👉
github.com/WhiteDNS/WhiteVPN/releases
💡
github.com/WhiteDNS/WhiteVPN-Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">قوه عاقله برای بار نمیدونم چندم دامنه
workers.dev
مربوط به کلودفلر رو فیلتر کرد و مشخص نیست بازم از فیلتر دربیاد یا نه. بهرحال "در سر عقل باید"، اما 404 مشاهده شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اینترنت همین الانش هم طبقاتیه، چون هزینه بسته‌های اینترنت رو اونقدر بالا بردن که دیگه خریدشون در حد توانمون نیست!
©
Kiyas
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

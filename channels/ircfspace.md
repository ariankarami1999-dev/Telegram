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
<img src="https://cdn1.telesco.pe/file/tJWsWpJKIiU8dlSk-mlf-kZDd7pknfvBuAY2KLHigDY07kdObqExgM8BFAWEWm0eCqHCzgGv4MG9bV0xJSquvrGjMi15M1Oszv1OG_RlbulIJLgrOuvXZ33qtHzF02yPqLjxfPFg7f91CdcfyckXkYSZobDTYTizzBHDz9mfdg-Bg639C1UnThxvO9eOe-AjdhD90hp3QA8jktUINVgKCEUmUrKGgwe-RzIp_f1xrEaMg5PKdwJopxyrTXbA5UqBsHbpnHokmuTocjRva5aB4L_9_lTBPYaOdsq7Kjhn2Iz8MiDFllTm34NOMnper7XzmnF3pH7zh_U9sJsAOCp6aQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.9K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 11:42:18</div>
<hr>

<div class="tg-post" id="msg-2658">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o6YLnvvZUBChGHvVV5jwJfnlfkcjjyYw94Nz3SUap9aHiHUJJNg2EfSItdZuYaDWzE6kF4oubLf3uLxocv5vG6cpca7ydvzifgQzFa9pk3-HSbSGpKwImhBouozpH1_r5jO1poXHvWxE2QH_XH_J68d8lYAFJbXPyNFeSeC-3fn2iLpseMigFEzgB7MdHsWBqCIQX1NMjdFYFAzwankxNsB4KHkSUFRlhe_Di7WlyHizaR7aS_9Ope7HqEtE9xFjSjD_vLCSeDb9jz8p7RV-ojJT3r2TzOAg6NqrqV27dvvlX4puVrqtqTa2ikiUUkrE50K9q5aGHumVBUYXL5eUYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/ircfspace/2658" target="_blank">📅 07:51 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/ircfspace/2657" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/ircfspace/2656" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/ircfspace/2655" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/ircfspace/2654" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/ircfspace/2653" target="_blank">📅 19:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2652">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X4FGYzdMhQXVZYQJSxd-btDQ1E6JITaDkT-XsgrUI-axJmUTD5OEqYcl3u2ixS6rpd0WxVMCHUf4Cfr4xK_KE1p2tTMDDsvQcoQC5kISplMXAB5PAkf1aY41LEI5Mm8JamrIn2Xh1rglAyaYfv5dnDzyw7fch1vfDFxhgvlRd-wqn3y9N1IU5OEjJGdAEnFg4mTKlhVbv23VUrVmea4vJbz64j59IOu4c7wg2biGWYKO8U6fF9lrfQyCqmutP-DTcZlt14MTR_6KQMQ1O1wTfYyVkoGi_7xCo4QaV2RYCOTalVgS12gjjE9MGJlxQXKf186GHCJJkIW-CyspSODSrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2651">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TFrumZ0JJ0KqRUrMgEE6OWPCgAlCwGW3M8ZscU-SH9e45u3xojotbZiviU-mk3CXWEEOTDEwZox8sa1wHzxHrzzJSvPhkioiBlivUsgkP_6zfhb9t7N6reSVK7pgyH2ysZ7M3DwJ1OVgkf6SNYuXKz-KF36RGnP6sJHb1YwZ1Cnf9T1uwSCUDg6f_P667wkp5tLh7NSCbteQ3zJC7BhAXUgnpBDbCvC9g1HtK21V6cvGETjS6g9y7lhdUTGKuwYY-b3vA-SFi3Fr1ILt8ItJEK0YsbK-laveRRhyjuWN3LhhHT8n-OatXjbcBJBhqiEv1d-s4_5T0PmXqoCtYqieFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/ircfspace/2650" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/ircfspace/2649" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/ircfspace/2648" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/ircfspace/2647" target="_blank">📅 17:41 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2644">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bt8ldL0IV0H-pWpwN9tLvGKNu0-1A0-WIXXpBYvp_js0Ds1Iii9WoC9R-htlIHRgLNjXIMfIJvl73DhfHmhcqtwgmFKpDMFnoc6zreUOnJoWedr77yw3TXrYOEbyEsczj_DQi7sSGDSsT0LkoZsdsXwiD_mhbebpQM9NuCYyljCm_AemEwnulnH9OVi48L8mSCsCuDWOgDxYjBLCdzkic5u4HU_VCzDhsaTfE-4gW4sIdPaKQMJGtbEpJLLncH8Y4EujVVGIdwzYV1aOsTeynTf8UYmfWFbtRmVlYbhOidQjnpW7VxS-wcuZ39WRo4tjDUf3CNlwiCdZIZ6NFa9QIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2643">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QSy_U_JDQ5rhFJ0A6QjJR-PeItf5wx0868bNetSJ5qcmLPCNc2L1Q-OF_JLUqi2_cs8pctk4QDaWuhEXWIRzx5Z4LnRrFdd4dHGgmtAoznHiaxzAaMTpRuMBcJfSuGVft_TwU1Tf4OAowXQA-mTxgPj_QuqSsIla1TvtwQOMp7HNqVPrYZ7B3Gn12uyr7TXEBkjmP5i8901ArPesmAtdoU-DEBHJ8HHlSWzF-AxrnhgqkpETK2mtjVrqq0IbTPChWo4a5qZYXnjeqsE46aqb9qx4e87B3bKAfpOP5MubMMK9h1DKWzyL5zYY3Sg3UENX2rGKxzvDEEHBDbCymFp0AQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 69K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2642">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t5NzWos-ZXql7iw-oqb3wzG4X_qahkchz37HQUpXQnTnKbhSRjlYyMSljxQq0hV7BMVPpNGKCaR2jNzi4oLN5syFtlIyx-R4ocf34IDJlMO2F2UDONVUHkpL9ZQ_IqLceaxdMRpQdHo2p0l8T2nuFOsCDawZ0SW9C2Bw2DCPdpGxMkjaJu3nNeEpA4tnTMhn_qBlg0_FUws5BwwDcA5OP6zN59t3yU_TnvAnfO9RpGvuL3eeQP-e1lzliIf169C1Dm8aoii5mrDjTMJaPIWHPf80B2xomzNxIlvZghJ-fEkN_iuAd1AKNcRNboQqzQuRNB5nex07F0aSfhK1OKipcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2640">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kb8fWLw9UjE-8865Yu8odesclNAakI8bBa2hDAoWpwG-zhrgfStf2Xc7yAOWNwa0HsFnGyXRXFn3cpUk7oUIzEHvA2fRMlvlSB6CW65pLKccrmGeLx9Lgi4rLi7qMvb6jcHv_w7lty99g8sd5UUY5IKd8sYniJWfy7Dt576CDHP943pmPDevMX5uSj85bgqHUTrOrs0P0oJlsvnkkPXIHuV7ohcdhGl6yfZ-BE7_AdA6_OhTR2VMfJKKUbOlKb7adm99icAWLxVoJGfwNSLieLi1nXtMnap8jnOApdwINih1vzmZ3irXu2E3c27WRroEDNLMGBw26IKbaUlcH5wSDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2639">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kj17UR2XMovm7KV3T75iVncCYDr77qlEuaHHIj3CpX77qgIpw9EXCo_eXFN4abw3ooPZkmWCndHoBsK_RPH1KBJ2araY5Lq1agYiTKiwU5_upW3keP4Q_-mtpiSa3AJZ9OGM72JbJGroIn1oI9-wZSpS-LBQdkF11uKdXj9rfq5-XpHnggBZPnrcrLoYRsNpVFE6n25mBD9-C4wGGTrPAJDa1LExK15bSwa0f3Jb40meZf4kPo0R-XbE8yQziPnqaWRNGWWWuO7fAzbldfMw2cTNJiA1D8umQpG708vO2wJMYtc6w-3T4kieWoILxVaOtn1vz0JWY_YHBL85gHuAsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 39K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EA5edg9LQuWC7vNlBrb6gWi9kFsvTj6_ItRN7HasiAgeh-6-_u78vu7NzXJ08T0NtGgudE08DGCA0-63BidNk2VN8IjpnS5qY1q6pEm-pfJmPFvMbxEUxPmSNS_Ud_6aQoDdvA3LhaT59yKb2J13qTsppgoqXJYuu-w1WtsyRP6XSVA5b4J0o64hP_xxaAC7khJ51lFOLp-yQwkv9bLqX_cxURN7HNYnBO8sRXHIMbwLrA3hZCYBbHOuTt8foB6ADNyf7NJsJJJxZ1gj-ZHzAjDdj8v7HoUfSMDCs0hNKe0xDg47hpwt7FwbWTI-WMxHbU_m7n6ik2nhRJu1cuLWAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dMtlYFtYpS4NlfQ7F65jYdLRz0cfiOQh9TeJMmfx-VPESsdvCc6wi44rigVeVBUDLU1sXuxddVU4yTLWu9nf6DCPYawbnMNNuLsj-qO6ZJrh9scy8q2QyqbgiqCQwTtGCaolSSuoY8vhZVJZyxpF6mcrBKY8exhqC1N_SNQpO3zNYlaoE34uxGF4pZdjLmiFP4hzX4NDl3YmlSVSy0Mn6jQn7_szajCHtJC_GUEB1BJbKYx-JOmm7Pdomok3lfLzvFhG7_CdKsp5ucwhUem80Q2nloAafuibfsB97DF4CnPZDz3O0kNE1uP0-WuquhEBTS0awXeNQIw_KqHQCXEb2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TQ2WTYCPCQYllim4kAvZps6dYyt12Crp9xkZYQleFytRPSNiXDLcSC67KWwJ63AntKrsfHbmqFAiWNX8l_r1T29uxywBBvLuWhd7K77rIiXsLn25LpNLjLxxyRNk_6wGCc_cE8Aq2gLcXYtv1oxI6WtdZue5BrrplVgkUm2gXng_SGQxWg3jVkDzExkuwCszvkQwCTfwri0la0SZhIMhEzw3KClwNVshhrM-GNItJqXQoba-6-rSn7n207w4dPPpwfRpVudIPbaAQOlflDkFga2DxRj1AMQT7KsxZH2feNqIbx31iUdTamWxop0pE68B_yvRkncJXMm9qJ7UoGxXJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bec0PaVrcpcndbT-HlZ89ShLNeo56FUqJ5QcI6oAV6VahylSQuYihdlrFAndsXybSVLXYUS0h9ikflxDjuJDlLlfYeCRDjhBENxSYBZF6iXKt6Ul2vnWNEFYX2jKTXC8Cf_GkII8OwkSHboeggGvJRk0C7-fE1KJxdrbdR6SlvhFWHFVeAfwCQk1mXI0vR_LbKvu9Lfnp2azAt2pfR996PfzexkqQ1ct0j_X_VJ0mp9ThzMTd158hCyxqdLDxQNOD_8GETwyUEJ47aPpwmHGLNlEKxrTWd2jCighMaSuUTZka4qFyQjGRybs02Jf0AbASEjU86UuDmdYFP0h_HK0xA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d7WTiguwY-VymMCHs22VCaXikz-1O5jNrfkZzDcO6mOfhAzSJjv8Z7hvlBGRWrzL5G6OON5NAWAQ4t_imT88439hApbz_g6dWybsvNbmGg89utq3xPR3oypgAdXu1rjMRXyCBTSnDLKbmp0NoANRcwbht_EHJkIlF1Lb-ce-EAdQ2rdH0MIaRFd-q9WukfvHM9PFoWFpvGZg5QwY80R71Wp8KaHC8S9BJhaBzzSeM-_Davkbh86ZOBhU8iiBirmUiM_jNVNcH6grS2xxi5NZJ61ydjg723W0psTQADzgerwzN1efPSz63X2olqAM46YcMhO2B1qChK7cwnqfEr9z7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aZNA5tQUetCxWFuLShWpI1vxQAdnN6jRYtkOjlKINB5Zm6jPvyEUP9-KNGwn9igEz6GkSB-yPuIXiFpayA2y5ZkMdgG9KNNpxNhU01PPaHbyhluwNKMh70Z7ISA6gkpAVZ8UaSzevPXpC3Y-wOUZRD8zoa_W5COvfM62cVxax_BECf44ktgNE67xmrkkCjKwFR_kmyj6lYL-4Hx_dTvghWJ38G8HnLOJskVfiUDbcypA8zZMp5ZVUmztULx8sNqtpiWlqfO-Qx6JzMSWPBye2tkG1L_bi4aBMC0OrcWBZ9rCCxo0v0bnqOX-9-F5gXea31E_MzzeFHxKOqS7xg613w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CpvMnDf4KZ-JaraLnD1xsz51sgssUmMvwOL9PUjXiRPa_NW5GHLIY0eYA5rKasmbZZsKVrpuSczspfeqyt2GFWQu6KMifiv4TpoghzZd9PVFX_NFx450uPB0qqXQVpA0sauP0TWQ3q0gplPRZml7bsFpYJ-AuU3j1qYEjrFmAuHQB3vE26xBsiu0FUa4bbt1aQAPjo_Fe-rMEGKaJLw32o5EzWQ-EOOBeBAOTlM5Qf8jTuRBC5Gg6ArBNW9XvIJIBG1QLlzHMdjzioJE17svdHB5N6tiVaf5px5Gziuoxuguzm8qpcoZxEg5oL3Tdfq9IGUmwxMPddtu2-I-WqcnWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DqGTmrVM_86I2rpxqLt-lOYTyWa-D3R_ew-nDsvCiepgq9V8KIqvSR_2Htr7fP7LduiVHprZwzuCkeyM5-1TEAxe7v3YH13RFDwa7S90CUs0rSQu2KXDkNht6c14WgMJxpyGQ4WuYAqVAKt-D0Klw3PtyF-Br0vIH1xxBItu6PZEyoyyoKs9Lc085M6Srbxwz5NFeAlQ268s0W_jg8cizGDKL42heYIFCA5kBwhcIm37jTQuW3-Gnpt9x9Qklrz8VCIctLUKVLNKjUmZZbaFlgs_19jYbb8yTVESl035Emi2I2A4LNkTe-EQ81BTCEfsIqjF7Sui2TPpA-gVmzzuVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mGkX82o1LKPosG5vqZbjCh2j2duRu-SXUqinT3-Yr6inZLBJaHSqSdspq6QLb6huE75MY6sUcnEjYLdGD1llESszQdUkWRu8n4nbRPSwgYfGHIg6m6VtCj0-D7BA2P75a5jiw8kqQeRCloPjmd0tYz1zuJVI3LYhKcJbJ0VC81q_aMsRoRMG3v6CG88GxULW_KaV-zkglf8G3A8Us2kbKaAE9b3YzChlAcFJcgwp3G2nJDSEQbfLyE7n8kjuFlaqS6FJPLLgpVBo8iFgjkCMEeCiO_GSRI7dHZBd0s7Oili-9WNO_PJqJZnui9eYSCL3zoGQ2i3Qk4q1bV5cx7FUoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D8w02RTaPuekFEGQRSIYVfBnFgQTm6rzHnQwgkwz6Ji1CD4O17SZR2dNRkyy_Hw0I4riyYOl73RKO9bG-NX2oOfucYXoxu1wu0d-V3fQLaIjfs4G6PKsjsLjXnw2BZcTgZJSkipA9FeOzwD6HNWGOVmuR7TE1zpnk4ELl8I1wfroruU43OQa8qYfEfhDDrb5NyRBzaEV5yIa28xJ6gT5oMXnHWUZmFbrZHP9GU7DKhO4WUo-tX1LSje7nyyNTWBgD28sxhDlTDm1xlhOcDKZ3ocFb7YXxYA2elZMqmJRjWKjZvg0lQzPr89I0KkRQuQplXAIPQif4pTeNIZLuTd8aQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dGTeabzr6tuycL-vVE1kZm0lw4FYOEXnu1oTtTumW5pgC5ZfnH9Xki7nL-F-V_2nvGDjYFBDDMWsblgMg8csPkiFAg3V_tCh0IT6JN86e-nOzJ_wAP_xhROJz-M9tw9N6i_lh-TozplketvAqvD8TZ6jqwIc_ttmxsC1eq-NoUlnV2uoHeput5BK31kJl4vCa3lWl8imObmjr0Uxog64lvFToI1tMeF7ikitJ0m9pAz2KKwwNBtZBCXc2nRh1AiPNzqvYOCZFKXnoCJDpt33VIa7oXqM8v0KvE4v3SYXa0_mpgGI5kBz0_MKhMP6COrXWOvHWeqw5ZezwTYGBv1E6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fl3XSPk32p6CYo3x2Rwvhqjeg23tSM1-u_7KWpAo3q90CV2CdgbxKh7fKi-BM0XB4mwE5O6YbSoXV5kToi7ta-9qrV1UqNWEwC1ZNzgKBcR-23TuJm4c2a-ad_2xfukBuiTm40fnMDOewTwJ3N2DXy3PCZSkNT5d9OHKE4UUt8agbMu2VvhmIA5DmgNtjjHAIqJSj2JTQXZc3f8vphIIyaEZRmiHluwrLYP4jRHRTdwThXeVW7TJuIzwcVrObV5b9RIuCWK0waD4ML1zV9NdSE0pJj3VIPOlyDGcX6c-KwYwkCgu_c5e8cTgL4uV08xmE5QtO2cHEqJrT2LK_IBIYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BUzLmcCUt6qz4OFlPXI0-auy3M6oAmkSzKwffsCoI4V_ne8YncYcN2RYOfYszb1x6ID6d-AxcmzG5jHjXRqXr_6lq1bPihGZOgZxkFW2b5WaiR4Gh2kd3kGD7xYvsoi_RX7lifFOtanKyLMFh6EFDycD3oOZFxprIT5xiQb6pKFDQjgtWU98hizC6gq80GF7rKXtGANw1JGZKhX8pNJGfPQIiu6LnrNs52zE6t9vaJueFyGRKufvwvk7sKJ06HnuuRLv82WhSSWN5O4FwNm7xfEqkxyZzkTBvVo6mL7MbQZqI_crxeqH3eaAAh3TiK-EBQARxTRr9zRoS-scqBFGDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cfz5qOg2GyMEFt7D1H5P3hhijF3RZH_FX_4_6qMydySE8tUAMxVLbruVxlucgRKHimBf-JOjBQtAxpkVwMdoC9Svs6BVqOSK9ytXzFSHU1fRqfWfg2jTIcJ8cCtb-y2Z3p2AJ733fVm106w8amTTBG0tUpseCkALpdiNmqwWN3XIIXDEW44KBM1NY5Y24urERz0piz54eoVlLoyAFAgxflZgXXeiQDVfmqKI4OV-yLXRDcFUvwQNg0bwLePvggCiTaZ0g5sAqeA0j5vyYf7WZzsZjneIFfjkpjNgAxiImnSIJGFwiTSKSTCeZQcwn_RdL0TWxZnQkbB0jgFyBfyYlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tyUNE0c2d2DrY5fRe0vLQn-VtdHeMNqFKrVrs1Lgn6_TeTGi2QqBTeNmJQ9fy3DibmhQUXfVtFXdLJLC-IIUMO1eJFVVsPICFtKtZMqYaXokoCtkTcAbRw5hy_Nvj2q-TbCFc0hrk0hktmNBVOYAWFfPR27SECQhYgcDpxN-kBEgBx_jjbxK_C722jNfnn0qOpUrHPVueBwNomrriN701nP0xWjp0J_mBIWvhmYepBM9JhOruz7n1WAHNBcmja89WTVTxCMiS_JTtl9YyML4O9iY4EKzfB_r5ETb6LKMeWbznQeHwcsuFNGFoMB4HyhJYppVsZMSPMmLMaPHlYRGmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DUkrCVw5Gs4JVLBF06vtht4X_vNCgWQ2_I0Ix6FxfToGo269wpyKCdjK4tCT6FGkekNC1KuTH5Q6OruXFtcZ8-GBSD5IioHrceO3OQZcOAqab60-Xn9sOwn4FhyA2YvFbgZV7GU85VcBMI27JXWUjaY78ObsrjHN-9nOoNR9rWthCsYf5JcvV0eTDTSaNevVLQxJLsdpYxj-y3EcwEq1bmBg1j8oCJymhO3OV6Xga1A_m8E51o-bgLGugdLU8ZJXRE11YA-F9aFW--ieRLjQRP8CJ3YnmhBwrQilDngQgUVE2kyJVRW3WUekdCWZ0Vf7TBxtVswORVrU2J22SKYqHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S9eBaEqEmz87s8WHDSFGID711v6bJnP2hcL3dSlWP1fuMwIiJNJaTDr7ZEmCtgeEDeGvClMCPxtcjQNbaRNQbIoBvhA8mYTw5X4LrtNwv6CaV1dVncDJICGao9UmvE3n595AgwhPagD-McgFLS9JFMjT8ASNmHx98nukDyzj1Bbo0LQ857mbByBurEKAH_yuYZMBSDewM6unpWAibxpK2lbBfQUiSvj5kypUD2I7LobgF5pJOzdaIRypLG2pajgIji832-5YeZgzQrR1V80Lc7iLIYoaMnmKmDD9iEay7lWGvnvQwHdIhYrVAC0CkDW3WvhmqE4kJjmz-tMLS3cw5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q5Uf7HCBHnmtBwVhelQfFgoTy3VNY5hcBrkOYbZEJ0QiMCJ_luu7wnG6ybCwVcSSN4NbTVxS9TqyJcaQY9sIrpFjrCJhRlCTxv1CJaTlWsS0iRdQfnxuAuBaS6tKGandGlu4grvWSwptsh-Pez7tl3G4b-49hGLCCdcraCyMCUCR0TDKzNfDcbQAVa2c1C6KrRv_W0__vWYeO5scjJ9ym1pREyQWPTk9XT3i2Ntef943T0PTilMXN5mq8ggbmmFpcsUuA6F3QPvvWAs3i5SSZc1Pn4-q37s7tM5li_WdgZd57tCaRhKFL8F8AAWGF2Ig1CjOLOkoWUc-bIt7Ilj7sA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d_rIrhcSKahYa0T1pidHcs4phSqjQLoF2Nk2U9rsq18hV1WOkCKbmWjokl2ogjWvYQJnKdFVod0au4WUVX1E59fQDqf623HZSlmnPOynj9AM7-wf4FbuHL6cduPSgqOMZVfBaKtpFFkG8TfMMEJkw7P9VghI222k3HQF5KtkoL5MWP0t0hHcYk-n__8ZCcfJRoFPwc9wyudBQhpCX5CVOP4xGok9WgUyzP9bpeKqlyLFbssWiSxaJHj_dExfXjSe4VRjpRAWqZ2slA_kihGGEUjXkpF0r-U9m7Rxnx-RS9ecrybVld4SLwRcjft-BdDfG02gXP_0nHMoMP-UIIN0Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iybRReCyY_6c2rR4RrPXlMw-H00v8oxH8cWNVooxBckzVZfny4FKK0efuZe1ohSKt-3Y3jYfr-LNCKJKWsGUppESJ-YJjjJpdY2M8aoSIqu3nfQKVU6MhLp7AfiFXHSZ_gbLJcBrYoascaFyHqJCrYuPk68mwQUe8ajiVzFo8PHrgv6ckahcnBsOgu5q_IFR59si51kis4WTpqHROFz3-8L0kOIrw0eJVolpq-yV5nLZoQtF6E0ehuGjRI2bSHvL81Rh6B-FS9EM2ZeCIU7TqqYe4eJCY4347hL6_wWq7CQ8R7gb23xa_eLv6LKj0N3FFq7Zdy1UTpQKoM5O26n80Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B8SIOau0MFOo7YrMLZ_OQxJvyyuLTJGuQCf6JfJRAZO9Ftmwh8fOloaW2F98YTVvPWFErdecYL2BEOu1ehe3262zZj_kiLhqbu2gjrw5edOrfBK8DUZy2Gg-CyHP3twSasKCntBFzLiyhs8oHViEq2S43o05ukY7x1qdQuGXWMsCqr8tbSHTF8sGV2kq0ld8gvPlxCV_PjcLwHN5Nkfyrg47CWHi21-NN0fKH33HU8QG3Lr1lno8TVEJcKQ3-IwSx9CrRCk3LzPVAalE2E_Ui4XQ-_mEGzMEc78sWvG2CebbxzVNm9M12ihOfwizsDOHSb-EBJiYc_bfoPe9Sb17Sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VTPDQrDEto4XiEm5wmT7NUQuvS4_Ztu1QPOebD3yl8l9vl1Vh7BkLB7b3M17cVSY1_3GKoHArGdom2PP1in21eDLNAmE4U4ah2oMroD4o7BFsTlXKvrHJxM1a0SGMChhXfNex2eDUW8PdoB14NApZx_BBJAjp_Txgiqe9r3P1M24QmNmVdtL8lF6UspCyOOz-DVjNbIJfpkpsSlXZhQL_BXgFZLufcKD9ThZFwh_jw37WYZruICVKKQzH1gjFhUrTaV7-MMD0miaZQ6nIBVSHNYapAG8TZ3LCwHiGtn-8tcayigZtMttIM_OcVaFlzmmJeeuuZo_IgbfLH5UfbOo9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e8AT5W68WmNGyvHQYxTuMr5lZZvW5fF-D2NGfV5QyHPl0YInqgUPibciVqpXdgNEI4eUUX-BaBoKth57ELMIDdAqDhC-lFSIlAPAzFI5gLAwV2_dGUQj5GJkJP1MEQQPKZvsGb9xLfJ6tmhYFMf2c2YQNeuTjBGOanokGWXebYbex-9pmp0UbHaBWprtFHYMG93BXEQAgUAKgFgA9R4qEy07aank--jf1LrCbB090ZBFJ7j0cubLyaVB6ql1PBsTR3Oa83Xeg-zIUHKSM7146al-mp-XDFPacFxHfBZ7i1N_J4PpGtW0EFRbakTOrZaHbyWycZSkdp00jGEBHlmuyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XAM14KpxYDfbf_WCeQNdcUk_jnJPCEXuxZLxVpsuoa-ILrMaU-1-YqOSa_hG_UKd2mT-QdIMi37QPBOQlxxQqyJSwWAttyTg2OfgXP3yiXtrAZpS1qbNpNwzhYsTADQK9v1rV5RTkCY6x2Wpw2ZbGP66uj-P_XWMtliJu4ynTVXrf99J7tgTtACz4O9qVtUh6dseJbbwOhUeWGf1j5J0tJsRKqdqZgP07q3DceCE4baLDq7ebN_Pk0yZtj3ukUBrQpRKOBxBPcL9iJKzs4dWopcY3ubttoxCh2RGKTB_Z7uYGGQmzgL0eTZJE9zknzfGqrr0fiuzzfG_Lr4YtWW3fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XdDwfEO3mBx-X9N6Sz5zv-eP8Fwp5amrGmXsJVIYeBpwLw70qbcuHVtPPfT_Abt-WoIY4CgLqFO3llJIIpStf71Cgc09dZNZYJQ43ww0SHB61NCuuWvjQ3LU0ZoO3rzM78blf9O7SJVR5xICwdFS5DpnugL8_QKs-37f09Rt6ycXkKsd_ef4sKMxo5f_Db_euJs3EGUybNSUZsAsB860MCB-ieROZTQOgkAoL9MYPcMZGnOVYEi78eT9iE2eUw1RjQ66n5D7PchHuusjny_entasLdExc2taDScwxK53SFQFKLAMdkZOvUS6w4kM0NQCB9DIdHVWJBe7HQcN_Wf6EA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iqxBNnWKfQpM39YRnNL9XLFRdrPmHY-k7yOXzONcSKTMCy1HxE2fFHJHDkxpNZiRKIni0hL3l7F7TzAjz88ZmUY8Ps0gis4TEfdMt5onw_mvKkCrMUYEht5p2gC7WBYkWRakIRbvHU-HadbvuKhqhqMPrbLWpYPUYLGxdGX1kVDv8O1l_Mc5k0c1DfIsh066rT9OvExjkkYpWBuKA8OyW-232MBLL0TdQErDEJqejsd5JMy0QTu6R1t_aZ11FGsOf-15bZFEPobSP6upzSAAwMs0BF7-faqyQx390mDWLGxW_PKM2YSpQFp94fFu0iRkHVnbpWHtDTiIAstPCEX9zQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sgp3FWiUyBoK55eAqWMftCDWfW3Z7MIW22nFpZxmq30dEg5pS7tQX89BqsYxAQam3v51Ogee0w5-BXkGnvPqrJyEBQZ72J0slrgYU1guLP1f29y7cqAYlTwIJ4I7THGZ1rhtGM6M_ARCjNdZqvFD19ZtWl0aJ3on0kBSXnctHUHnteE9Hr1YIxwt2CYLrjOoJnlMRO3i0Ga2KJvRt5Q4LOqjbxYiOh3zggCaHfK3y_qmuVJ2eYVW84mcAHDabrFNm030UK1AJ7MrN81ZRi-rUQXSldM9ucKxeC1So3sf3MZwA4fgPqMBeNMsjr7ECxjyJhW1tDN4jraI0WDyQGLbrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cW5KBGIiCcABDwozcNxsppbNYYxw02UXcjAedJVFg9HLMaehTiRrp6L_MARRwDADCu_nTruECZkfk3JvclJgIEHuNA5-2i7kxXtPBZ-Xth00RjfxNCK5eErmaGQDYfXX61RsFXzPijjvidm63iv1KhFboKRUvUuYTTM7csPI4iCXKdqDXY07Sd4PvPTaMxy1RyuVYvTr6qWKBFh6GXQpBFcvveLw2IyzKy_B_oa0ujhfCAK6ZA6ALHFN9ndZnqrCScHgnzDC1N9Z6MveSE9Yiv16UAX6IWPh90JXjNNqGOZTK-m9yUl3NJKGePI2PFoEl4l83JrE2HhKv-2nfEQJtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vsJMQ2C0B6wiHATkdthP-A0rd4TyNvcTwSoVMvF3LSpc-K0zNxu8LlRise0T9GbVy04kKihCFw6B5H3Q-GEfmKOqevBBgob5cYriWKtQaKTU2pMaIOZt6RPA421LKw9tpTKQVSbyE4MHEGdWRtuhk7GSTrEmuaCGHgI1eWD3zfCQTzNjrHuMBnuGxs4K_8aOZwpVrPvXC1MygEJRuVG1_UR4dXBDBeCULBAQTQdSTRaEIIxpVNw9ktv1k1WRoz0vzqEo9iAFUC3SDJu-QZsbT7tPdlpBnPkjYWih5WluQQ-k3ZulIhkiUcsLWDhVN3yQCMNfQt0LLzg3Y5dGnXFKiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HheJNgIeoa8pvucqlliW2ajjsymzMFKcC-pDbSfjXQEG_k1IdzmiipCUfhXmt_JZb6PN9EfiPQM3gZNWaMetuj183XJNQPAjT2b1fLc3boCrrl733vVo05B-1P0jD_r19CsNYYEvA_jVdJeqaBquya3RCy66UEBcjyGdNgPQSAZs8BsV0WN57HmAwfvEA7BERTQUWVMhvGXSqHowc0C5qN36v40FTYLYu41XS7hsHPI56B2bpM7y908MMqAntsieXUBma7II16gmetqNFF1VDR6oB74yD1i1KGnzizeAAPkFTbOLmfgr1-tb7sBR_LdITUYOC96wC11jXHLDGfPi5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QhmQoBbHg-Lf1T_O-kxVtgbuOZHIk5USSV1bXgiJ2JLvo10AtC5vNx65mUIo176J8ge3RhRe4CSeMY67ClAmtRqGlPn5L26mLRN5ab6dqP8mL1s-YY9PL6M7gC2fG3QdjmqOrg3rmOPFM0N-Tsav9qz756V6b5Y11VOZFWPVHhQ3h21__R7CEKfilxR_nVr0PPLAYLARcReP9-emCZXzi0FfFoNMZ148or-E0QJ3vf-AyHjeCYBPgsketcUqDES4CGNKo_MlkrNzQReZtYYSiW2pUzfV8ydcjPILstP4xQQQ8ggBNtCj2IKMsBWUKni-ILzn8fHLRruKPQkwULAbMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O7ropxhxnxHE_DkO3PXHdEYvnVwUslcCMXt_56hL5h8akp4Re71wF8YJxelXO3gYyyYWw1fC7Adt5QmEs5SbSTPLQoDT_Rs7woP1G2tXhMoCLh6cjsRDQLUYvBMUcII0LAZzQbeqWXu2vuLB-IB6HNaMBXy6M-NBmFRGEmfHnd56fWw2iMKfg87Z0jmDXStSzHbxE0_1rHCOcxEkrGsiDSNcjS1amVxzZdiGpKknygqfbdMBCF7fdFmVMMcGgRKVYHA3S_HG-WNZXP5uGMOKS7XVTydLTB266jrdimutdVxud1hBY16CATMB_089xMbOs5yKw5ryWKxJ1sRZDhaywQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UeXXeC9nX3XFb01hjCOHCUxn8CbfBJSk8OWjm63ZSZbJ-XlgmgQ924i-AdSxDMcVbgJWRmGKuzVzgL-kG6x2kAPb13b_IQ77KbqkZgHSqsQC7-Ndscq-8ywY5WJrMZVtt9cS_bHNj915eStGtBJkNcJszNfda7pl6ELLGRSoy-VRbwh8O2mnb2yVNuQbTDFepq8lPfg6ghhKBjR4ppIzvBHA2ReIiPc2G8pCfWKynM-ocQGgJTB6JLyt_Ol8H6fSRn4sViShNG7i22HWDKgv_3l3tDK04osjxRi7_weylgB5JkHxTHBeKuez3AFoZ_HQBzgHK1MJ4DIQwj7DQ2X3mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E7A1ZqtA6b6aFV5GTZZGzQ_9r2IwDfPXB3XzpbI6mgF-uWOfxlzld8c42D_c_yjuzJWCby6mxB-WQlDp_v_l_SGJNt2YXLj5Od2UxVd_G_lPCp78lR4WfyQszCeqC-v-jqjCW_PjdfDV8UE2dIT7PMsPmKlewBJsp9TyqVVMfOQmqt9ikPFPf5BB1FGCYtCVmmMAzoZnYBWih3pfxEEk16E-roNiE5UR5FiA5fhE8S6QeEwVMVPq4R9bWl7qeweOTqx-eXBhc0N8n2nMM7Gp5J39Ow5k2VPP-7jFhfcggz0idLNXIaHxZZCFRsLKCbmYKiuhEZPmu6NsZOU7vnshFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QsyW-1SA3ME4ThSm2zlN79wfUTBL9Nc8xX99SgZOBY9_ZxL2106Sq7Sv9jWHGt2Yh2mr750vCQVJjDS-zYwSWD8FQqaDZ7X0_szy4hQyt-sZGh4atjABllQNT3exB9DQvS2JmegKASVtj0_1jgGiISdl3YHXFuX-w6RASlAWIeXQsFObUKtVBx0bOINSiDyrG5h6lLAMx4QWdTf5fHI-mCIJHFkAZw2whwzE3WclpK72HoGdenOdCCIjO2B1N4RwdFbmkUI4IFQp4-7RbtVgifvKcNw_jivLjMr7c0a1Ta4cwtBCOet8k8zP6Z_rIsQoglznnScRmFd24uBlGJJ0sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vdNgq1dikNkW9qELoXNGXLyw8zUlDokv5Bq56iSTQYdiGgiWnNq79h1ZpMi_Z1AjRRzGEzmNed-C2l5u33RNJK7dZXNNHJujrMC6MTxFqbC_eG4kAtyCHYErFfIZCCHv-bFEoyIfu3jEj1mtfLl4eKzYHeSa_-crWUJ1DMo7cYBqANtWBXHVTFotIxOvDi4EkO36fh9uTPPTkSBQwqBIlpC18qSDhQKbLMd9g72txH9idlx5YI5TUTgCJaciNsvo4O9dRppuu68GFDja1XNnz1E_ZHYqtE1SNQvTh0VzNh4zlQook1qgbx7tOYn2PaECYax7m1Zt7SBCa9hihyTOrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BHgPteA_-O_vQVC4o3VEyMDq2cyUUoyWw5J3Y6J4hU58rh28jfnxeO1Wwm7hCV9k9llYEmJvh4gs2L8gkbiUVsrhAkmlLXce-iZiTkwQUVgxopYsLF-a0zVcSMFOMoyelKxNftYzCEhKTtjwItZDCh0NL3mMeek40ucxxURdVsNVd5OVU_zc8GZo9XhatpPM6RvjXYE_UvhvhhxrszGRiFgoW3ILl_USDYbsrbnSFNytaL9rOEU_idGJy3T4OZPMh_trgj49AsGlq0PnSF5jPs22O1ZA4ZWCg-LoxIxkVBCfZMXTg6MrL9z9v8Y5SdxSPP86v9TmgRvli8AdpQvhsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z7UNzeSOnrjtQq4jZ8TPw8VFi3LASSJ6C3z60EXPXYAw_97cexruKf354uTI210K6neqo3qtpBcv9JhpHGimt9NMwiiZQ9kbvL57JkANwtDPkpjjgW63ZhyRfbIRhlQ-05-SVZBevZ9pOcizLVQxTgx_BXjlA-2FIQniNdK9BLGGhlfIteKXtyiSZf9hSUooE_sxs-Zrl6Xaf59d1TBXoMKB8ENAm-SQgyxpYLQblBX0ZG6RJp3Cd89xfhGVQuLKRwGMs_u69k0ZbC_Xc4BEm4T6oB44yaWQT6E-Qmv6XWgjSdLV0-Xo9wW7xwAlBpstGbBAc8OGvsJV3FsqtD2oug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nb7YWfvZB-Ghm0KR8sCxieHLuSrtZQFKfiT95Sgw-8ZKbAVRnJ6f7wtehZLzAvLsrsuOo7Qu_Atz81sGovrt9rWF9ZTwyR9tO9DYKt66efs0M1Y7eIKAdAWbiR-wYZhizlxKUekGZFuN10WesjSFkZDpZ0ISnXWZrbPEe8wpbyIaFc_VZg38m9bjrPv36nwi9Ki9ZaoA2RODt0JqwLd-L3pj9RhcW5pGxXYiyuHnyyx5zuilLuou5y2-_OXpaq0SXZsfGoo3yDbKYWw6bUfKxwsnaeyCauffEL3kXT95xpxBEt8gWyNxfaifFn-mTpMuJAnqYT2M_PGhL-MiwxkqwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P20wUhpdBMrG-P7UFAQLKw_yCR0V7jGlSqnwXRD_3tq6tq1KIOSWEJ7JCLzPXjdrt0csQdoqo779J0GS0U4a8AkC1on6FS1xzb-1eQYNDCIPtWPlEtfdjUAwwufcpQaIg_MA2G2PkBNrEmcTMyVI665hlw0QHUpTCpuIQqEPf4ZFiNkq0SZJEzHMGbZjN04RoBwESkQbtx47VCQsLOLBoDCifBmNCuGVp4Nj36G9RfdfwkLnlU79CsndldwdD4pFXAJtxZ8JcTbcqfERQQ6_LANAaEb1vLKkGlE4NC6YrO67N19oI6cUljVXQ8FkF9zKE4R96y9GBPiaHenpWlVDIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hp9hY4OnRXKQsok1q4IdU8s2jz1WgXyzyOtgNu2sVYWO8ujEN_Ear4SlMScCQQhuqN2y7NZv7u40YLF64JQDBt_s0bAx7Bn-p7kM9ULK8-1ZtGjfYqsPX1VOd27egQS6UMEq9ZGjQmWd5CX_QU-FjvnntKdMS1ULuLCVpr2QSvneArCGdPQ8QbXuUnQdDeXD2G6P8kR6dNw70h9COP7b6x0IzlS_R96NJE9lBylp0FPuojbL785VTAaxk6mjnaWzEMVn_WR4vF8Nhsa9pwefHPDM7XLCZSUP2CZmOhFV6nSJhIj8JFvpbP47O_rf37t40m7_w9uXX6bvAYPSgx7SxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XKLStHMcEBjuWLovqqXXn9qUucFHIxlkCwnakY-AQzNAIfiEb16enrZGbC8IlGqne9OGH6NoJbMBnz1ENwnD4kGjPWr4j4hbwbOw7VvUOot3TmV-UqZpQS-0fBKujPDyXtAZJ_IfVHXk2ulCAEVJhyTwiTa_8hzGx9519xUaCgb08_ywUXDJzcpJccwwBS-xVxibVVHTkYDWZPhPRhlITB_ZV07wz8A-vKSTay0l2jXY7u-zVcmU4jZ-lpc2l8E9uoq5gldTbhYdcMhuBWgisnesxD1FXmkYkuH_5U6esiPRXr7TXGw8WYXUGRxEGF35Zf-Kp17-CsIqvZ22uwIv8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b6qhaQUXzQB-LmowGE99tCxxYp3_S7EWZOqGbruWU02S6ktLE4pV4a-5ISqkuK9u2QARYJljDU5SFw-izqd0JngCM_3kGZ-oFPngBFX4tTMdKwZAROq_aBBQFQSRIsuRZHxP5ZQv_CE8I5c6ctReiUTZMCIPGI5TO1Zn9jzLhrLEEDeQjFGGX-SsnoU0g-HrgIXupC78oLsUeZVY2ZXw8mIVuDdwVaEa6g3vW6hGUSDVr88gv7e0G0tRrxrEEZiW9-DsupV9cVQlLnkG9NFrWRpcJxm3KuFbwB0ZhGez5IkOng-xudBn0xW1FN1SDOTVT4QIV713Ew6xpCxWkNujNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KLsqHkBYjJnaxGDaArNamyNvWuK57JBYyz7Llg6lQTA5MV2HBtke1iGaFZzA-GRYrgK5PPaAByMYefhjD1SwQDzkQuoZffgjypzK02Vu65R0GfFUD280s5LvxzohCtwYT_6-CCC6T9Wzgia3yKBXJB4sEEEgo1dDWyyZiePEfcPTqvxdRThJAMo6hSGiJSazeFuE8yB8xcyO0Vskt7WQh1x6sPBG7ViRuuFhJulv7svAze2tHjamYtKrKI13LhOqIQmn4xESDzVZ5FoecBPfiqEhdCqpEuClfasua0bO4qre5KDPfYQfZVx1OQpjltT1YMhj_t8ci2DQDXEFZHthTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YyXczKAP1wBvl55olRYUfY0SZAO-2oT4112CEVBIDhcjMsFnRk8pk0m2rXY1o2yU0Ly8w4CE5zg8tSnUxzHIQz2Gb3Yh3fQRe3RysFiMoufOyygtBCDuorqDiorhWbnIFyTVJX2DBXORxgAAyA7R9O5yeXtLEOF6dFWdDLZhAQ8YBKZT5UTvC1xYf8dq_WY8AU1Q7xjn1iyL_-daCeZ6VKGr4k1ks4ElKELjfkxby83Z9fzukLUbXqfgP2ihGBOeDvgPuN_7Jrj0vswvje0gelt7BUVTcPviGaLzh3aRO1JlzKYZvVLFsxnmkzARJbHJUqA8e13U8Yc3-8mm37d9lA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CUP0df5Gt-PeD3vG_gIKxFlt7i360jSAyjNC816z8EJWMe8Je3nZH0g-hdUYlI_HZJw6Hqhwxmw0fOWPVaFOYePW61ddjeoDbESBjq_ygieZ0COlT1TxjZ7cfwF0Rm-tppfvr7Sh2cXH4ZbKp0iyhuUeHzOhU4zqDZ0qukLtZJQg4mL2-Y20YuJXJvCbqah1_6XZYs207KVhPJMdugf6tpiyPe5x9zNlOXq6iBRhc4ehrbpIQ3cwtVjzBdd25D5KfMxrh9vZLlnqY5dp47sRyw-mbD4Q_YSe7RboVat2xs14FT5BjGtr8NaTL9UC-StlVrudPpDMMy5Tn7rYuhMIww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Thfn3shvj0pXFKRAEPjlpdoPcivPPOBFYjCNLrOCTzHn7ughlR3mFKfBjcfwdYvvi9YsFjpI_5qvGsfmeTVegA1T244J6QlEcjJ22dTih8T3UWNlSywpdjft-6skwV0dquAdf727xv8aNp-1LCrf-nuclyNH_gKdTCGCv3Asje_rudCHTPLlvoDUiMuceMXJ8krrMwhp81ssY4UuWWVd37n524vmK8AigRQFMERsTz_L16x0KETwy0Idk-t9DhxKo_cFd9azCSvaBwn0geylAwvNuVkx_uHfUEpJPWNvDNdgaOHc-1lOyHzNO1X8LvFu_fZKg-NFu6AgEilzUA4LcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NiKxJIUs9CDCXGwe6q4WN6FYTqmBDudKSb5UZpqbZshJXFdiQcrQ2ONspgIAUuwv1xIGj4bzQfupFHcPNDjJ-7bIFMUAHSng3eGav2uo4xVMJ_zhcCNtx4lx2gmzWcpqty528FJ405jxqnm8CYfEoC4qHKav8kqodEkyjAfmB8MD1M1nmFwSqzTeThag5FhWMuOgyVV2YCMJIpzvwkHoscNwsrErv8xbgXet5xcCWfDYJTsVHAvc_uxJAdQc4i4j8SGyI3pl-w7G6Z3lBBzAsMIR0koDW_gAMeINgmLEItbQOu_W_bqOB0Ets36WrnhMMFVW9RWkdv89LAzAwJIylA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tvWS3CMYrINNSs5novKy5Ja7--g9WPg1DIb-A7NQDKhTywL4XdpU0tRMBHTpOUrgYZIXbobhGTfCSrwMRc8k2SEYtf5lPLDKQbGFT23dd9Azz5UQPOP4L6UGhR2-YPsgWh6q0wqkruHFEJ1dQCI0F6zerOPGJftNKgqdFMwfz4NS4vwPwq_V6r0BmWLrFOXv6qKV5XK1kwTXYawvfNw9tytMLOjnSIUIsuJU3A_QqUKz6rsnajSUgc2cR3_OTQRIthEIi6NbLiBYgWZEFueBGBPxkNHbsuJVcKK0VbS5aruLy7KIes3VM3OjS4Ury_ZnH_O_JE31xnAMdjuFKt_0pQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ECCgqf_aHbwYElRUgk6MQqb8DHy2Ur7sExkRlRrJMNfI-pxujnEGzZQ9CdNX0ru5_W6Sc8gTqro-NvrmBuoTqLqdDKaa_3zrsZzdMv_lJWi6NyOmE6QtgJAN8uv9upPCdf5iCo75bKJYlHkqttLCKUzJDsZAcBQICuGuEN8NKJdlL7pNPqZa5c77ZPyBy9ji6mJaHtOUMgco-gFZU1BBh70iC5Nmvp3LQ4ggsr7fvtmhBoeWL7QH69FALn2drThKqjoI9O6ITayVkMwP4WiBKOoxO3Dp-JrnICET14Ijjkj7ds7r_UyK9sGT4NO763bRVwouIt68sP3xIIXn2uqmLQ.jpg" alt="photo" loading="lazy"/></div>
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

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
<img src="https://cdn1.telesco.pe/file/XbDwSblYMuQQsjKKg31NrzBsbg3eWU498qYi9u7ZkJu-_BHMYoz4LvfwSEi2OtE2fVh3QDAiIh3FFlhfwlc2PVy5Y6TYzNNmXmtL2yWNxHpe1e0NmoN1b6412VcUiJbW4N0CYDDLR-GkfR6RJ1EQX0sCxuhxcDsvqyhtuDIqcvEDLY6q8iH4bScDZrG9qIF8tc31O9FNIOHWtxg_zdSaf15ItXJe6056hTwt8TJqK9IyN7VpNnghKNekmDSJFKJ18wnaeAPLNxpnBL-f3skwSpbwawEcWP9v-c_kglARMQDoJeWkSVZWg1MCS3vtBhXNfG-nTl9lR5MSG2hdG9j1Fg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.2K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 11:50:28</div>
<hr>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YWU2N53VOp93E1jLbBbg1OyZsfF7y-c5fkRpMzjEw6KviSBmYgSGY_6bSDAHEajlW1tVw6QJGjVeXa9uohjJEKZ7VQRGBysDMjSETJAx--yWgogF6zAvvUD7QJbW1bGr6M9x9fXE7-4qUYctftSx8l0j7zrMC_SrvAwg9qpFEDC7Ug6hU5Nilvelpuq1ozeio8vfFQ-kmzuU8RjfguW5piPWmVNSNnMxxnQydGu7iHf--3w-ZjPvNWRUFhlQt11__PCyAz2XfJvXIWKb9uCFjhTnBZizJ1c2EPeaBqEh_CaVroFocFcUhDbvB3pGoFc8NEcgfqosFScxv5WG7v_hTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j96c-s9ZKg0QeOs8QC6fGAPYzj-l_qAiyA8WYMBWAZc7L7AYYKt5gQguHR_uKGgnhkkI0YZNDd3dOvgjIcPxKLkEPk54QoFwMZ8dmViiGGxA99Lo71TB5SAO3bFDptV6bxrLQoge2dtIgR3MGZcVgImvATAHqOV3YnZp9C98xWCdxpHvDk-eHRp07JrWyyK-VHHrVHd82OGygyhKLaPMEUd5FquQ4cQ31y7Y2aBRwidUn8vlpyzCvLNJ1nlscIFh5HG5uAJJBIc5FsBMjsnaTRpXRZdq8A_6S2Ld2iIfe6sRYlN0agTvMvGFWCbIGK3vAD0zdy3BzWDMRD5yIvXIrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K-QHF5T3KA3aENXfHfy7zg9oCTCLwPrjIWw_LkA7gnU61d2GqQDYKIBlDs7dDmZzVLw2NxlNPHaBbM8X7kuqBWNlMvjroGwRpp2OkA6r8vu1ZJRca2KjzIeog0wFG7l10Z2LiicNz9mM0cDjf_vP55g7NpAf5FIpYOqSUgjA5MmfSJJzd1UxIWSvRbktQilgWYX0nHKLhLgS2Rh9mi-q9DwPDA2r8Mn0QKvJKOXblei50_XQW0KVY1NEf_DEcm1qwmH1_sfXGC9-XvUpoRQH9lKb7TSQwvgfFKmO0aS_ybH1Wl5JWNYPSIiP-59dSpOzHxcO8Av7NiGWzqTv59KXog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UjlfuQBm9RzmIIbevxkG9oiAzETS4VVNg-7ioHgWS8U1l5LzArvDEoSEjfigk8RuZjRZ-f_5hEbWe93RVt3vFZ7zaljlJNNWBjgUeHRW06DXe26Qev8yora1myYpMkyCMU_k31NxQS4v0B_dmILJp05m2aqV-Uv4Un9fVeIx8YdF5gjVbt-4cVcWMiLAli8SnK6xMWCO4eTOWKSnq0ywQgeptDn_-ALIO0vY2vsxquJXOu9dQMr3A1JG3OVTKfEh3nNz1Rj7kfQsHzF8YGIFUNmxcmdgm21LAoFQatTuM9yO6DHJKptztutwyX0mX6Nvc9WmbPKgMz-OmSBfCq9jGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vDxfV3EvOiT1kRp141bS8YnxUud3jjomN4lM47EnwSW_LStADtCW-aCnXIXSZB9G0LrlHsqnBtiIAMeI0vb6bjDXRDZ5ZLCChY2LMMVT3Dpl2VQLLGnyBZuYPS-ccfs9JBfWloc95lHRpUczvFMzOVZ1ptiYS2epsHuvxiMqyPwx0CPXiA_iX-58JSpCAoYeD-ORJMsPASqEUHG_8RErYLXhTizE_IrQVdk-O2d1empDjTw4vttzi4yf0PmAEM3LQircH5dEV9HP_Q5JjWXq4m2mFnjd9cjXHPjoupr35RG4m1A9xLj94qqt1FBQz17P4_4fsiAoGd_AyFU3oL2eeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YkBod4tIgaxf4GCVExXDKeP-vBDgR452PHE8cZc3CSHq0GX8Dj-scjTCek7CIZb3uVfu-q111PBLval0NkRwgF96uqiqXiqOW3PvIOYO39mUKDY52hxHWw03En1JBKCF2vfphuUTBEtgs69wOfkQeGh1oMAuX1URXYm6U9awHo2n7oneVoU3e7HAl8zPCtkd6UpBpobesdm9JVCdjU-SuZnhl-Cxa9-EMxIBtlYck60UHcL6YrA2Alu6yY9duN0LOxJZi4BCTe17r-YAAPJpoKF2bywFUK-d710dJk7I3Mque7k1ZomVmLpw14hOepyzcreTPeECQ5UHJ29gOOc0wg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YzvQ0lZxnaCF3QE-tHSfvneI1Gfng_QGM1fHXcV29CGJN-HDvgPRqbxZnPZM8obMVbqpc1RwYTWJPMufCNiu5BSyGBB-41fjw1R5_1uUJfcg6XzwdgOceiNVeT8_qyfTqJyEbhKjJoT-Z5lkprZmMBf7kX07FEOuA1KiLIRSUy1Q1DPEkaIeUWYl83dLLuUT2KSovoSQCy4mmmQ4UmkFB2nr9jJAkyJKcBBPwE993_F2GV6UeXI4WgKhbggE5A03XpHfsEfB4IWco0BJ-eLvpxYkpmQ2Hbe13u7HoSAx3AAsa6F7FZ9HA9V_OYwV8lLAfGHYwygE-kQxLqSwRQ1rPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Svc5BeBGUSapWmaRilYwhoWxdXRKdjxYbsHCbKODIDjU7Rs17iXfLcot7Ni4_oJvsFLzOH2TTQUKTfVbqWGh57FF7UcfG4VOxbXBGI2BHM_1C38v5zgNHPsAo5i7fDSPuaILLO78VyQp-IW0LZGjU_9DqsrZV3IQ-66r1nn3qpdR5pp7lPH6PJ2EOW07hZsgFbHZ3auCY6SsB5FdO9VK_04MCH3X7zzjK9rq40LX_k0--uph_JqW47w23zi-Usi0wsq9TLZH1IbOP-T0LQAcJzbTlONOtrBVvEtx5-XWcDYB_fmVuZvWF2f7el4L8BXB1_rPXBr4QZz_6qS_gAHKEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rVI8MG5oOlw3zuTTkNuMpdM0mEuHdUZCBF428M4QXXkJdixuQahg8ZYYt-UgFMkxHwwLpZLY_kvT_Hr_prK4GgmCSs6zbMA3HpBR8mBnY_5Rl1PAlF9ol6IHER_-lE8DZTnJzEB3CgOZ9llMkhhZJ1DgWM-cJNbLk04KCc_DyuzXWk545Jfl0SPajs34-eRgiYE0xD3uBq9-TI1WbckzDdDmWSKfxsZg11zO4JM8JEkqF6MWqmDVGPpiB9Ky0OBh3LyLI9HDVLHIZeUEXn3_B0BbRjZUqI7O5z-EZQKThxSedF27Hu6HtqbN3G-QH-E-z7-sljBjeUBT2SZFpCKF0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IvQIeBfJGo6iZRVE9OupL4sMb_MaIAGC7Id--cO748CaIZHFn3Hp7Q1GakzVXwZKQBtA7Q2Pyk_XeO2aUVM2SwS0wgZYB6hKH5nq8ACKEM42I0yRZSkbOuiYiT_PMUGnkPOH0I-QIf7aJqK0aAY5ukJZ80bE5YVerNL8AiJG6VO8NBlc7axPoXGKgBfkjzyusipNeV0asWygy5FgzvRrhiWvew_h_K2yRgfTy6LiStksfq0Frt5txKvleLK-6mrTacTOTFiyA0UnQhSrBLneRZZebbDpWcaJ4wX_F1bmtDUmmAb0UDqu38myqDyqHKDaBCOCBypvmfoMHKvib1fTng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oinJtYUscymjAeBygxWHIRKE-0IFFL5m56i4cydV2Fb0TXsgA6pBNln0F6v9OYbKycWjs0wDYXbVuZIP6Z-_oee50Ubf8AVMf5sClnNiOI2ukQ9YSvFDjN6frQo-j_AbFWgdDKdFfn3zjiSNTs8b4ejW1IJhcHQdjIemQr4KXN0lOBlss7xFxeghtJEluiOqZzHvLy91DAw1da1FuPqE48YUr4FMWwxfrROrNJikGeyN8H_zngDvdTT_sbSY6PjeOGmprlKZKxnv3XHZmEdy5t72FYmagrZ-Zcdos-8fyoZvxqsTAQKkLp7nDH9KGHnRq9Pm3S7nrs0i60Ys9Q-2MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dg38aIu7f7pLjrOV3S-aakKoStRijSHeSRs8pNpnn3jgGCcHDwG_8h-Rtnk5SD_t1X7ZRLl6Px1e3ySYCa7MBCt6GPaG93XyC2crAXiE8c1Zl2_jxC97b9Z8jx8oBpwsAVmnLBJo1j1sC-Z6HrU4qaPNjUtQq17dmh47nU3paa16E6_x2Y0f9V2czI6M701THql9d-nQj0xhl2XN417a_vgK1pTDYGox2KJo07zyCcdEoGQZIKojADZqnu4lO6PlKa-WOJUNHfO1IfqVvMCndRuOkWLPT3R6jSZxyirw2aPSeVWLCuHyCDl3b2JCHFjaqDU59RediGhtD0VyHVBsXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q8g331xKwW6yEFQKZgTG2xwBlltpRnMFx2hv888ST67Y3l0gjS0oS3lJmZvR8IQf6mRaB9wPyZgtq3Ex7CkOPGxCIcrFQlkHrLq5TSWV9Vmk-tQGxX7zmMwfysq3IblLljq4mIGl0BpZn2Aa3QGFa4b2JYbQsgOXQaJlHGuNHX3jUQbvMYG2XWAVDgjEyU4b9a4seVTSsM01boJuXXsxN5aD8fmfI-tCBmQkJD0FMeHIPMsapZI9_jlNcPH-nUSiccvrnN3jXYjyj7A1Qt8hd3jcf7seKkIMgz5WD7ZUHVBvWl3GEmoi-orJEAelvJ9mBM8uS9eV9EnMCU-vONNZwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N63_LgTAec2jZ3itC12zbFCbkfnPx_-tek-BdkegUAsT54wgDrFBvIJVkWjoSa0fz4ASxCz6GOyWGqGQiL4wIgrU0wEI0uq3gHVqlPFs0HNM_9vGCa2K1DYHRIGlfJThVgBOdUlFXZdOMjlZ7Tmci8Vvk8_TrD6LfYpMZ0vKZrydbVMHAIiHzk4aEaoCpXFqSor3Z2IBxNA4igXDwwIu5qWIJqVqaR-d_m-_s8PqGI6y_s_Re3_d_-uU7GoZb2ZofB3KFMh03nHtaLf5EMpx0z1UZ7KyHxHPVV88MeD6cKhB6rZQaUtiDh_VdoPicobKKrCxWpsyeItdRGZvgmFfng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fsKK9t-CUmyeCukN_51HR23DNeH-GVaikDz8FysFvnnuTKBTqxmuh_x-b4rc5GUfkl6iszOtJJHVxWvk9N4IsWzZZaejgpXQ_C5W5IF5D49woOUO0OkS6iiqluzjSv4FAOJHgd8P5PD0k2AeVIdB6N6U7-TTzjUDMp_eR0iilE4fcFp_aG7EeS6af4VDvtm_clzdGNoIWqyr__5mr02grMXBQI0ECOH6w_aLdvG4TexsEagL-_5XN_jp9bJApXUxwO0djaFn-FcOQghEmW8J9DQ8LmGYz1VPR5y5QA9Ag_HFHtVQtxukOfXvAS2LPMyJxI3ix9G8C5ufJTSS4XAxAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/URjnpQhs46mUUv3V8CrhiuStzm8OWju4aAfffdGtniJohMkNDZ70ZbFZsedDJCnz06hQdIxl5sdNEEft4ja1hE6s_V1CDbeTj9QsUzop_bG0Dwet8G2Igm7NfmvwmEReGW0tzkxqjmpN9KSH_m5jyaomULDGTF20iLk6Y3yoMgpo3qNlQvYMS2TSMX8ov5xw0dOug9xLnVP1SCuTzVaDtvnJuPjlu_7S3yi4wPpVYULb7augSO0h4t0FmGRPO2OWd491mPKonMDKzkVc5c9HQZiapeqJnHgsGx2p2cfRAJ1nCMULNuWtiFQE5MH1nSNECNWbii_MimunrtaFgjozWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tzsa7D9eNIT-VkuBkLkCok-Cy-TFGP5X7zZ60On9TJAhw1pWsRxqTDxHTvaI6vwc_J_sfQRChd9pWkLVoQHoSbbr-zr6nh8SRAmUI0V3JTa06JMlQ-ybTuEYAzs4HSSrXf3M3xaD4NwFeQfgCDg7M0zqMlPv3nlVh8VKQ7Kxiut4Nx0yncqEHn7XrC20gpQ2Px40zIL3dJGnNQSloAd6yZWY9GYIt3gWYJA0LJI0lBqPV1cdM6wszqgEODKJKyQHDIfgSCd8uWp0G3yZbYW5risCIuojLpQfDmXoFR2Mfa4b7XwdjdT7sdW6PqaQLJoenuL2N6mpufR67Ooj8WFq5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZMQDDkJQqvJE5QZ2fQZVGIYhknoj3fp65xpEyZawRIeRkbyXsGcqGF8baA_ol62f_qjPYaJqTLh4PjV80Ya4Ac-9XlzZ_u27e0FYrxb0taRZ_NCTc3nYgEGKN81q_-7_r0nY_fTeM9Y-cMErP7y1-1iaqLL96pafYnloF9HbmNdB7J6ByI_Wd-paejDACxB5MSEUBCNt5ZZ48oWFtv5lXLDRF9kuMXqqWawVzKg-bemtCMMdmwcQ2_oaUGTGYQeXleR_S66Fg9zabtEkYdKkk4AREk-9X2T34iqhpPQjxJ85Jtwl7TVqQ746VqeNZDNUuKW3nBC952DBx-Oh-kAwbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pUqcKjAnb81UoLGGI7Rp1yLh82oFzmfqjH9r1nrTWf6xHDq27oP-wWQ3O8qNjDWVAG28n4z7lYM6s9gtkx2fyVPSTmXOK6rGcmlnFWBeHeOg3Bx-72hendpJvS6VXRhv8PSafPXvgEJ7DKgyZi3VARROCegVM4LUqvrgzsaYlghp94ft7r5ei4ja_MFn87D1ew4LgDhtA4XFvBTOcR9jQE2rZN-pq3LwIvizCgK75401iZnsORgCVcO30OjbpDvDRQOkXwKUQxUPoaa_9k311DDf_CcIsEvhDZMX0WjXfIcnFMpvfRq8B2BLguxb804R5Ak8RtmjCkqNpU0T312BtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VAD97OfYZZA9hlY0cgWZujFym0d0gzb7rz1QiHjber2SPlXEwOUS8m_Wq-OhSsrNk5j0KxpE-R7vUlaSi8u_vYPKv6Dlj2vanHUekTozAhHlMfRXGTRW8rFpbGU2ifkZwJfY3Rj1ntKOxK-w7vEAkLxXCGNCae96K6ZSjcsSthPoVBj0ddeVU23d6Spn_wiV6TzlkTMAV2rhWI_snhMK3tQSHmYuqZA572qBtBuOSb8uvAYM6XwPDqNxxJ5O1eWsKu4BatL4HXUcIKqoWtPiNT_bVWHKv-KnZJGSHBOo6NcMWM7mAmfvL2lC-86-OAHoYDv3qDNGWzagjimkEPjd7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sAo6CVUBwdpaZxauD2G5dKOWQrZpPKiCphWN98hHvduuBKGnvACXIeBeAFabxnziC-5wRfemiSWA3xGWx1oiAE5TGoP4gRErNxW89hdr6Z3rbMy_JCuVrlIxgBxq8FBa3phY4CDNG1YZwSEIWrjgIbIcZPwdFdEH2DscWPFKv-YU6cHGEr3NKIHgMQyqb7yokhCbYVcV1JyDt7MgfIZQxZqVqiRACNWzpmOwmOTz_R_Q43VhX4G_oPaFZcZ6-chQ7X4IJvbtHbdkMdpt0C83A72oJpNZ5Ws-hewKyRh8F8D5KO3kMGc5j8B4P2HztobNfZJm_p942KmGuNjLpqWXkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cOssEa5LUEEqnIgDt-WSaLbf7EdojxC6vYXbLcimfO6EjYzeQvhYmUakBTKLY09RIwJG8Htk6QAS0UPExalNYCTEe61UcQXzakGnvKmPHGUfib0XsjZZIup13wg3Fas20xCjXY5aMIFFuFoGaVql1lwVRn0PwqhnMm9gFCBN9daliIXUROHZi-7TZtorGT3jntClanT-VxElQ-FJqeOG0LNWEJjS5w4_9TqeLeebrvx_QFChK2Y0nmYfXIvbW0MDrs5KnpmJDCzyi2lLyz1fbeq9PDp5J_udKbS_5h2b3h60wRjeRo_jFk-JgQ-V8X-dbc4UAsi4LasHfELq4lXOuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qdIUu_XVdcbOFsF-dsbuvTAhn9uBBPqcM23EG81Amoxm15kRj81Z-OpZQaHyFx6wU9Nh111W53UfVSUoHOuBmq7jvUUc3oLXgbDxA0UMx97BB63V1d7-ZBLJZCkP7AD5rMD_3lHj_TwX0S9Qy_Ni0EGLEaXWYTExc0EAGAZ8KFUQKyVxFJ1GEuO31bh_3sSFGQqVY-dS5DDBVEzAwsg6HtXTYJ5MoUBuBdNhdGjGybz3ejr2Gy2Z_vSfGozMqgnpExki56LRHlmiVcUqMBrlVODGSptlFGz-x_SCZrcKzYCPFLGUSnXFJVtEkqvF2hwfog9QNlsT3DHhnXel3V6Q6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Om3NLHmsG8vdahRkPqaTDRa09zcmqEnVtfu6ZNMWKqxc5wwULBgp1aWIyc4DHqI0v8iucaDxAcjHfDl92IWSxclvTaFUDYE58OnJoq4muvrQ2xytp1VwBUkzYOKmksRm_FRmsgUZ5JH9okb-EmESx4xEV8O37rFeJqgY5TKsH4e5hV9LPFnMaN04aW2uGu0ln2JUfoPX6A1ZU7Hmaix7b5BXNB2qcdfIQk1mNs6OtonZ-wqTNbWW9F5ZqI0VAm7kHcNK86XUSJdjI6bM0llFPNbxtuVahwzorh7tEbjNmJUYyvvLDR6PakLoKzU6v7G7y9udPVymtHIKzwLCHEWHfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oaWJ2MyEeh_XhcfaRrhYanLDypQPwF2PbgZBxQO2jKxKxMlY1uQuwTMFXYstz9H2tD24u5GZXNORPO0lQ1tHMBMFOJd7uYLYL27svPeV7zauQgshAO0IfERqaGHxllCALG9chhZfGWpqQ4t5CUtGFJf71MJ6c_6O0Sm10WHLRlxtJX-p7DwwD_om964MQZ6s6tqjfbTL2ocs8zHDwqRrpyJsmwf9i0AzFKrrCsSOxQnxfDucVxgOxxzdAI8yPKxz_WBevOrdvLov4jmLv28hdE6XKvYll2t891XLwMsUEB8i5aSwlFSjK4NpTsu3jtRzdhuhunYRx9I7bgR01URi4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aJIxlDBlcMm8ju67PrSqE8BIwyBTZVI0fHgj8QLl-axWpoiB-chRb_KYdFwzYe1vuiUIwK47Y7IJ5mTYtwBuTRiag9PFsRynzBZfFYUKoss7tW1XKpzupXWVP_5BkVWIJaLWIQV5RsuO3lDMypeln2NvV7IuoNk7X81o_PZEeH7rw67KfBD6KiNzck2V73BwXA7NlT4z9YKEkfhtRKfYwHc5TK6oP0ElfbyOnBIM_D03rNDWxO218LTarHY-TRE58ifnjsN7mlskCK7gQAPBknKB0IRMdROMxUebpw7bcJOVK3TM6heShM50STEA45XwjyXCD5LeU4GWRbx8N018wA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZM3hEoKkH4Il9RSs8_nfCpAfLsztR0WgC83g41IKn2OPc_SM-YMw2iW8f9tYqGppiTguLYYZKWBq071YKbrwQy5EtUl9HRT0X16r-VDq-OZNb_-OOZ4dcQRBs6PdHZbMImVYAhZe4Mo1kql5w6_IfFSM1IeQRjnIBClLvL3GIvrZLiwjPM2UszETVvjSbwZcLz4FhUrg9h2QNtFiTAUmG3WHbQUUkNg2k4tSp2N6xdkIhOB9TRSbsPS0VrA9PiLfKOfo8r5WqL81DadQXGcHVJc5l8tescgYJCUh0Hndl1d72_qdsrcaNq11pVNXxv0seTyvrNJ4UmpgUsuPGuXRKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cwoHyd02ZRhXHlRF4EUuAfFdwZl20F1XcshHp9rCC971jxqpnIXXiEXtf9AyHzNeIkNdXQ2xRRvBR6kpUZbjRafmdw5cWfR7feb8DX6wMHDFlYy1-nHqaT_2qh4qYNjUQuqOkG90q6fUHJDlhnGxOVH75dgBNFlMXBJs4Nr3b_aG-cpl9FbzcJQ9pdeKSx4u5QMlEJOjtzTTYCupJCNSUJdIc51prYscFU_gsXDpz8wp-cmI9WXZ36DJpVX8vq3RZ3v7BTUmHznMmlAkpLLi0ugXCboPdhg79ipG1qSIHNWDeNoz9zsn8CPLvo6MaYJ5V425rdm3eyebbfOILcMvSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H46MeSKoD7AuG-uPrZRUbii0uvmYUEWmqOIl3W_h_f2VXBdk8ZzV0DGh_uxfXoJg0oZvNz4ThRxfElMnKOQMjQS7VLpxnLqDMnG6u4WHKRxl5K63vIaQaU4D03h_KrQFSw2ChBE_nhlle2ch3drIOoax9ChdRW8_0hpU4upiYj1Xc3gM8Bp7aZDF0D78ZZaY_1BRKRdf_FjJiwq14k7G3IpBoUo_cvsKWMtZydM6mJgPlQSr1relapejHEaPHQwIoA2G3kbXQ1k8lWgxjPKHBBxb2Tvgiymgl3qsM9dC4nMaYbbgc49_XtGVCHgyK16Gp0wGdKEVy59X22Gec-EAQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vqia2tMLw9iZgPCQJD2pjXlNJIzdUVNNiVhqAxdaTQYaHfsDbQR4obYY5V-gQCbcMFRlfhtLV6veLO5-_Vz8MS8wb5_wxhpy8wid6zcAYO6TDzgHjx6cMdJNeNd7fCyNAP5oV5qKO_f4uX8oFg6SvxrzU9Wnwi85Q5CERJRD3n75ztN9rnnuqhjiElPodj4D-3iFEIEShOv2nPZu9n1Q9yjFoI8VuJ5AUA_aj5xAQIr9Vz_23rK7ojrVuccfyvReXgQlVu5AkqMA9BBD6ssKjD-jSpxpkoUM8wmEyJuLAtJ37-0xNcemsi-Jq2_1KdiWTi2aiSiHrJbYOvg395dYJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PSMHBUuMu-g4Xr9DGGZ-K1ZvwlfKaTGCisBe47Cf6LJkRUy0VyZI7-ZyG_-KW0jLVlj-M-YjUhIcY4Xvs_A0Z762-h2FbicfButiqKyZEZHKzJJzs1vQx_pMuQAYm58iOkmoAlfRbQEMCD1p0LnvT6VY-vbjmh2ZiUWg62_QBaJlvcxpYS_pMsRJftrYEiaUfEGY63YvQFNrnbiyPJvFYYcmtOMLVsWwiQ71zF_yM1lqaoM5gBnSG6yRKKDFpMCDTQ9jbb8m-I74SK-mcZXY0QXWqH32WjroMCzJmBkdZ9hQmJGuGEtIzy8Xm0l4TYSHy7kkUIVLOKs4sYWaRXOZHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KFB9BqM0F9svD3FDMUVCYpjIeq632OmcJtXx6X0NQ73QY8LHftD0OXET1vCSb3dP40ftmUvq3V8M-elvgY4o-athHtJW9OVZ5OdXvifaN8trJGImV5S2Vfdqa7TXc1PLTUWbhpuhcPSV8rJTJ8m-qnlr4GLubvcRshTsI7IfqkaGXJPmpQgKuiuMtFoznpzHxCwxrvHXTJljrNcDNobnDPvBLvD9dBvtl93bwxpNRB1n1XYwMyqGKPhRoT4zgDxjkSaDyqOQ52qiRdqgbwi_W9BQhJZMSSnEzfBMzDrkRddkPuZxdx8Z7he0tsAWnIfiBoWgqlNzcWO3bn8jQppdIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/phJQenAb8ehp5SafWYvBF-l-ZXH-nNj717Zz3qP2dEBpIi90upvQKjwJohiAP-gcWcmTye_IDJPfXuMWdfTujNFwBrDVbjC97qfplySzMVTnlwio9TPqrLMoJOB5zZx3Y9BZeSd0ngWqzupTdM7IyhPFBaZpkjKyteFmD_f2Hk7yWI4lFthtbHrWw94-iSk3bH5YEeAU7gDDqkjTvCU76-JnXxpKlEbhTnlPom2DO2ab-WkD7EpejGgvJwLN72PzknSzVfn84N7zWwCyFAdOiQZSciemKiwDOT2l1TRYXjWN5cU_e21rJHygYhmBoJ3ZzZjABWyyipZLc0KOn9SGKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EikqXya_JLIgcRsHFGo2yK8zQyTLIjPlS48kutz-XfEyUyr9KrM_IBjSF9z3mwA4YMFqBSHzX75XOr_XqNe3VVBGT6wMG0wggin9fbLzg9C_vodRmZ6j2lFkJC0iKC8G7shlEXAPPR3dR0Sdd05FMBm8uKeB9xGcoBaowtNYDkzWNzdQLDOy5MzhIyjx7bwDdy3LPNsVhf80vRjF86wuyqKR8-ZD6ch-XZ0RCDwaY0HaMq-LOOYX8-zFfEncClpcmhJueanCcZzI80oaPeN-zPD0IJtbbSQRImWS6XS8rkBtHdZcZpKmYJ1EdN3ZLPAg6zcyzxmotVdXFItQremKGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JF-OXm8L3LMUaP0gxUEvnRVBeaicQzAX3OYTCbNKKSn26la8d80MC4Ka3kbePivVbjpVcO6nFGEzhRUdJRWgXeN03wt4WH_VEXCA2l6kX9MMhzX5aG4mp3K2DAcGyVSOCmW56XWN7SM7laZta46-DXdRmvETqCNdOEnYMe1ZYoiinYoAxHjX7HZrB3iLjuCER5cFWWNGRVERvpGzjQyHEZ4lst5BpQhxBHNuhJ18qU_FseJa2Byg3mgvjxsM84F-Z3JTQkWJxS1U5dT0rAdwj6wKibwYdkS4OB_OQdCSYUMW8cNzjtmTtY2yqeBOtw0rae3Lsa7ePTX9jDvRmeXQHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VLEfVIPrBYzZdHOsuCAN9eeVeRXJUGY6aYK1fHiMebldMB9IzEVhPHc6k1v60EZDkA-36p07jxxhHcsMQSqouDDdXkIyOlecjbrbQ-JDHZ0fpLTSBBBPLJXXzdZZXx_XXL7DSsW3HI1ARQAZmlMr7JGpqsln6cBWgHu_qzI-xqjtFdYi7nI2AW-Mq7KzCd3vDTNoBmfhHtxyP-w7l9DHEzgF5evQ_704zZyjNWB2jwqRz1n0oyJXGfD7YYm0HkRsF0XoHVOjRVxregHSw7bDwQhafVzpUzxAtTLRugBc7Ff0p0viv_L5O2I0uWyi-MN8kVjN-RYPnf_koFjtVwANgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pu7Jr88UXU492OWvdyk9OBx9dQFDmaTmqvxTipiSMCZMmKL31wGYVGVHuWJsMntkz7ek5ZODCvDPR22amJqZqHRsKEKTKqD0IBn_LqWIqDgOSgc4HLhmIYPs-Pf_Coa1wPw9fb-l3XGkSSkykQgctRUvp1Su6-qRsiGa1fxBCZUOZwyRVfHIyCuI4Ae0FelDQbjqh6j_GxN8hW7t5az0ZGSSDT01gJDmtMKsclAIpG3F_BOLWy_MDRSIx7lWNhUN5O3nYdeAYIqaa1zbJe6S1aEWL9agP-Kr1pkvcqzgRw0zS5cHDo1J_3184YvhyYAOuXva-jhJeBePVX9GZiPKkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 49K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jOfXm3xv_gDKWIVazage4gDstAxDjUZ7jCHVMOpxMnPPixnE2jYiNisF5U6tpsk_bAiE4cf691I2i_J8ESaMP8DZNYJfe1aR2PrgEaSSmJfkiPowxHcGQ-C-2AZWx5yB-QQY99j8DqjR6QnhjdPVGSNHT6q1zt5hAXLbtigBSo2T6WPLCRsxIf-lcd0cy-f6KYe3qS0Vz1OdAUeZCky1wMOIEfxdq6mj5nVNSJA_UDrQjmvQgGim7pozfiPUUCU1tQXuTDy4BpJxZmiaBV7Zl77wOzhK6WaJfBHJbBTGwgk2MYKBoQq-bM1DFXDllbkXILglrjODqVIy3NZphuUTug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اینترنت ایران باید به لیست شکنجه‌های تاریخ بشر اضافه بشه ...
©
thepanue
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=AdymU5JBm9M2qd5hpEDw8hI33u---KTLBACe2bPYF5GHgvW0XU61PtWy0A6trNbIcP4S1DYZrHteQJHnP6T6tnsu9vk-AWywzOzFTijKUNuc4XSuMofYRJUwnxhFKDy_dAxTJb9CnoVC74r1bXAh_NCqYrfRo84Su2yE2bzLKFAzwDf6_9LVC0R6eox456jrGZAkifHGt3_xQwzM3RFJBx7v-zY_06c2gEenIwPPolb7Ev76JMKzALjbYWUgq5Zs9LnIcWhpDx-lA6mN-WYVnT0R_C_TQw-n2pUHbPFv7598J5MtIWopyMECffFUMg8-kCJLrxp7FBgIw_e4RVG_fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=AdymU5JBm9M2qd5hpEDw8hI33u---KTLBACe2bPYF5GHgvW0XU61PtWy0A6trNbIcP4S1DYZrHteQJHnP6T6tnsu9vk-AWywzOzFTijKUNuc4XSuMofYRJUwnxhFKDy_dAxTJb9CnoVC74r1bXAh_NCqYrfRo84Su2yE2bzLKFAzwDf6_9LVC0R6eox456jrGZAkifHGt3_xQwzM3RFJBx7v-zY_06c2gEenIwPPolb7Ev76JMKzALjbYWUgq5Zs9LnIcWhpDx-lA6mN-WYVnT0R_C_TQw-n2pUHbPFv7598J5MtIWopyMECffFUMg8-kCJLrxp7FBgIw_e4RVG_fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lydBTcsfD0tAW1LHEuZV4adqWF2h-5SiZQZR0HpfYefyZt8khJ0hVhHeoaFA-lXsOegsSi0KyxS2w8Rcjmz3gqli_n56ai8w2ENp-0juTM49ku1s0nxu2Qrk-EYKnvfkmCZ5YhKMYfT84ZqpZaeCOLM9nEmaRgizQWm2DwXrldPh-oZ4HAc4Oe42NmEsRLqUqufaxUWVSe9IBoOpa37ApRD6hfeK6ViE-ZyUXeXSQ89D_wqoH6jBbWfUH2pTj1mMSJT69tbZ99xwC6YrHlz6IqyTSTvpf4LLHqNz1z-QMTH3HjGtDwJ6ilA5wUXACOuYQIv7KrOuv2vaTjalJ2httQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IqzINXtaCJDGpfH6pgmv43TMW70UQavpi2BHdvXkcCfA9SpT6ZBvTp4bV43-81y2USJWjHFAOecXdRfasIT6SONNx1UcWBvCmx4f9jMkHMyu6qneVnA9WIFCo3h3XaMnBeNsgLvLvAC-dMX7sJzupdlWY2fKpS9xjkItTpm0NSxInFaw4odg1LjRGEzbCGJkbI7HHmI4RYqor9tE_CvkFv9QAGUz3Oh9nEveccsQq8_imlNsLiypdW6NHrOJ0Q5LNyAskp1J_kxsFU4tYmxy5li4t-hFtymPiyw40FgooiXkAOQ-PlyX6Zwshc1mclzbbn_desO5cXQS_UG2_9Wi9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/USEVWbXMpJdMBeZ6MXYgHsG2iTjBhzXVAsZrqNawBIlJje3kEdyFoOn56Igt720fOy9fgRAZYfKf2oLvN-63VQ3gilNwxqu7x2cWGxmpalEa_hA49OKyB91dMl1zgei3cLBMuBOqrnMLeLM7636aZJCBMoFINH9_AsaS1VwHxH70_u-SZmcfXqnFYK-2oybcwFbWkQlbbIjKan-P_0ymK9f55G4riVvCgUOUaSoXygirI5SEdyqom-iNb_x7t1i2X6MwwyOkSKoSk7P5VYyKZRhgpTp4REw7iFTWGiYwbfY4qN4_oTaOBttC75HdiyQao2hmO7Ts9T4-61nP5k7cHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CwqclaXlC2T_WsC8ZnL53lPvGfBkqQyuO2QlIQy4GOin9M0enX-ejglO-HmBbhRpUg02UJ_e5ugreDjHjleVOfud0QeKQZQjjlJknLamq8HJjPHp2e6jdeRuxJXd1iIBRUOhlcRJiy-ZvZy26sE7p4fTinlMGqpI2EWqST2V48lAlEoiaTC5po39-SZJ-26LkSTF9ig7yQ_nHvChAHeXLx7vvgFz82_yCLN1RFcnnsPkw_tea6SpTV3F0mDLxKODA0VWGC_uXuLEErkGa4P8kYg060cCvn3LBnH2Xb9Kc6xdXa1ODgr656B5ukL_LzklDfw-nUmDg961G-HLUBBnEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OCRLsDwFEQgT9xWXzqsKvC6r_cinR2f_h-Dz7OtZz6thaFsSaX5LbPaB3alaPjhlenWRhv_TBJ7R59NyXF88GO8U0cbEvsNygBO8mOqCU7tBA9yLujg3Brq3o9dy5OMy0mQS7UNtqwT88K8ZFZxnePFGrM4w_t7nCJEBxq1OBchfPYhMXeZtPTw_P8s0w07sUV9nw2AJKKk7cSxeM34sHLNovoDGVpB-vURMvJlozK4TyiF8i-uXvcq3YNneNxmFK--zsXzOtFiIZ-6BeerXseYSgIuOGqW-zHcHzNTUJ--UJQz7tDVjzJHbk_-cz8JMBIuHLhVAoKSMqhVAnepJyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l-rfNlBewgHUvA7wu-1sfPKyDtXgeYKMOlvCasDkpzGjYCBk9-3lefI1mNLRRQmv2pv7fRIWNtI4wfBCUAtdnh19Ux1u_EwKNtIVFwvO_chKug483TC3gUGWIIXaVcMot6aVHlilMHieuyCASTepeduh9SyJwAb8faoa1O2X8_iNdwEzY3ReBjrpgpWsN1VbznhGT05UUbbBhF0Gi9mr-BIVKf9-xMfkZaeWpb-hGwY9iTkHGuVBgCK3qjAdCcVCSQv88HE_phQ3Yt5BmPJfHrLIla1XVtL3BZnspByyMn_wvXesu_YYHPEaqagmgrCPJX8k7ypHnDVy7IFW-YGqqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aJN-CKFrdRy1ABU6VFcRSQ8fv9tbpuqY4-9SlmJURTV8EgjoQFdrTvWDeeFYtuCSM7-gQHPj06S7qQEXYv-E1t0BxIhJ2WegKGSKvayvaWamydY4sh5VEPW5mt-hiOVzGGxvAUp_K6ZHkMw7HHF2PakCdWAbd944b_sMFJw-i4FVwkAs-TxBwDA2W6fE5NvUD-dECbLcSSs4eP29h0azWAIzbbXkXYHW4bGQ968FvzOMhJUhRctTBZFApvAru-GswTedLsZorKXlJj1c_WNqt1w6r-Etwxw-I5IcraJzG-fLHHBF9OyZRzlPCwUaCAynkyiCz95fIccLqvP6Rl2r3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J_jJn1keNipRl5tB6n7DjyYVv5oSoOAnkJ2xu-rN_L5z3sD4Nn-YqIrPpzIUCOJdV0CYq5VMDZdbnWv5uWl-yI_0i6aRV_9Iji-W-lhCdeBg_JVaZVgVA2jaohSQDFaiHHNIENJVURsecdyVOu66Ow0YhirHj4a4nUeWxuk7xNkLgTYt1xt407SM9aPbWPiQEvOIjdNBtYGFgaAfvy6ToCavtxXe6jq9bu8-lsPAGrFuvU-uW8LXBIYct6juiVnIKNTmuhuSx5F6-iV-lS2pLlHMr8yz-Z-oaKN1VEYSrSnQwYddOxM6_fT0HBBvMcMmSRUaU-nN5BWXQmXqNr36fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">چند پورت مهم مانند پورت ٢٢ از سمت زیرساخت بر روی آیپی‌های ایران به سمت شبکه بین‌الملل محدود شده است.
همچنین شواهد و بررسی‌ها نشان می‌دهند که ارتباطات زیرساخت برای ایجاد یک قطعی گسترده در حالت آماده‌باش می‌باشد.
©
manageit
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UAxG-nS-MFr-ZGsAkgwZh6jwz0zKVVmJtQCjgZXa627DuB_3sdmJmUukX46FP8yRDMY2JfzjeP6HeIjwD1cBX9-f685BwRX9IJFWkgGNnHnjjOCFv7eJf6r1Mw1oykWf-CmwGyS87t3kwDeLys2fsPCEdY7ECC9KeXJYkvcx_1Me20VyNu7gl1aLp6EO2yZNgPxRllZsjR5uBpDwZ6hru8xiNb5ioTYE1MHw0UqsxLszi_s7KA690Tja_6yv8HmbToXmLIKuPfWGbaBcVDwiUpoCB0SaGMs0sTrJOb_DzDyxwYbY8r8y9US8KZgeMAqIREt3Gy5IsZoLW-msi63y3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">چرا کسی از این موضوع که "سیمکارتایی که استفاده نمیکنی رو واگذار میکنن، در حالی که طرف با اون خط اکانت تلگرام داره و چتاشو شخص جدید میتونه بخونه" چیزی نمیگه؟
©
shara77miaa
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hi516tBDqrc_ynj5e3pcBULjq54Qebawf8OFPJS1hmNku8x2jQj1FvWHP8eRqmJ-Dz5Ab61BgscrVQumk8COQmNz76RdlAqttbqH7Je-2Hm1epfe5m5jYMR7Y3sZXj4M_wQrY0NFz7x3V_PQGxqWqqfZKEttv5u0qPXGlja1-fh_pdQzPzJZNzFkcz3tj_icXpY68NnlI3MQxOZIRqpBzRXmHeLE_0dZTKvm-3afYiwAuFnF7ffdpvWXhUB2svRc3W38Ek-Est5msR48wXMNtwccBaEfnIUhocpIPxpG6xnIG0cbtKo3uaEtwLOgKlv0DWUxTv7_oGeHH2uytreOzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jIcPxOT7zwUJvae3BGwYTLVHuVokShNaxTiF_94ukBnIgkGPM68jR25CISvbBDWvKcM_W5TBfpaTHS91PXXxqU5LVKzZxSXbgjsuIDKAik9kwY2dNR2JCEWotvSriuBhcbMfzs9mBmWbudnD5KICoHr2sOH5xSlKSVT8ELvAAcKs3vcGoEjfDH9MssmhJu0VGTcMfjsxH-vso33PmORkYO0dA0i6DoSQXY86CTLOStI-BYhHXvcuUyJ5sd_pLZSlxQeGKO0RLFJ8biX12gxzYrHo5MA9GOeGLZ4T3TKdy5NcPeWK2EYAZxC39X3BedhWqoYu-jibt_e3RTp7Lagu9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی و با چه مجوزی تصمیم گرفت ضریب بسته‌های اینترنت بین‌الملل رو بدون اطلاع‌رسانی تغییر بده؟
قبلاً ۵ گیگ اینترنت میخریدیم = ۱۰ گیگ داخلی بود! و فقط پول ۵ گیگ رو میدادیم. الان پول ۱۰ گیگ رو می‌گیرن!!! فقط نصف اینترنت بین‌الملل میتونی استفاده کنی! بی سر و صدا دزدی میکنن با عوض کردن مدل درامدی!
غرامت قطعی‌های ماه‌ها اینترنت هم هنوز پرداخت نشده. این دزدی سازمان‌یافته‌ست که با حمایت وزارت پست و تلگراف اجرایی شده !
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aqzyRpHEmpi4GE7xnk71axDu79v-CcLO-665KBdtQnOre_NeCZVOIjlyzvNm1wc7CrwySBIUR2Gj2ZYSnO93Zk5IlGQ2QpX5_YJCa7mPdC5JQ84YJP9uPCqcj1Co2Xsd22Fv_s0KTfs9YRUzEo6rHVBDIV4mwd1vvRPSyuk2JkFoHhpXFM9t8I9pJqjAuWT0AdbAop4VY2ZPASn8LXeBIhKQHEZwywb8RTWNhIdc1ogj_v_1RBROAIE8BKfbuLWZo2rJb2upilSkIB-citzWHpZMQ1Vn06JZmAHXqzRSwKNXe57QmaJPXLsiVFAOS2yR-QqO7zt4gMRWA47THVbUsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aerial یه رادیوی متن‌باز و رایگان برای اندروید هست، که باهاش می‌تونین بدون نیاز به ثبت‌نام یا استفاده از فیلترشکن، به ایستگاه‌های رادیویی مختلف گوش کنین.
👉
github.com/shapeshed/aerial/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NPKt_V6eKZx7IyaF2d6TXCm8xaBhqM4xtkGmAbKL8-oEiHssywoY6muHVkL4iu4LMVl6kOnYW7uKVO2uWOKyn459KIpGrmUo4zT7D4flns8F1cAkg-oKLIOyCBIDsRgFWOOpuAnDCYnLU-kKfx3l2u11igEU9Y1dPsuj7LxmYCbAZBxSFhChwyJDwXJF1zOAyDXztveC1pp2iIDrrIgr2mYdp5oyclBXvDScKGgA_bEjCzaIbEcSKsis5QhAJrOBjiMhgxLBhROZT-S_SRVjLw7z6ydluEWKZmNZtWf0bAIHUu4ws6OoWdrxWNnBBzusxoKXXbD__JJGQVS9G7gScQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZUzY7KH2RtbNnSRd8-u08l3iRTcA7yWA6p-gJuRcQFAwkMAZSNFfdqnOUpAPj-SzW0sEYc0pUYSrsY-Gx1QAkhIFVcvdY0DPoFXEwjLOkJfCenC3jPCCxsRbCaSnR8Rg6DPKCDueOacsU8uQjLJfpnxtvi1Oi2WE83zm56WKHbtHmWb8IcBkh7YNCW_hYYrAFnIkpNicc9MTvhHCYVfMePeFB5ZQXe7vZaJXtA5yHmypxcoPDM3XO6hL6zIqhhV6lJccM6RZk9sudGTm7ziM2KATw76JSq20u_jk50Xtne4smGhyMYGvd5j0IDJeo67BiWPbhqRnhJRaEQshUxRMiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از راه‌ها مخفی‌کردن صورت مسئله، اینه که چندهفته پیام خطا نمایش بدی!
©
AmirMahdi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YHVxETwmcFMEtTIekX0rzhLf59thy2y7NEv6DBhvJhjNqsErv-o5J1XMJ-vAjjEx96jqeUvQbMF0U2lMqm1ZeDeHuzN44pXsSYiibp6CKKtqQhQKZyHhFkCufl6kV8cDH8ASyxcNWZ7w9FlHlHTY8krc-SEfJ0iQlhPdXa_cW41ssXsAL2UqFX_G4dPE4Uaq8mf-ktzEP7LzPVpG1MO6pSupyvEtuF7HjhYON_cuciMoMB1jQOem_sbi8udT0u1bG7Pp7wCTVN_FZPdoPEt4TtUHKuD10-AvshTwlWdfezEbRFTH5jPhULero63lGUl2B8C5jaLstymjFq9kPl5dfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GExxmoeYlexo2UoTy0KBASyOLkdH3a6mA6RB-DuJ70c89hbYKgCmMmbH5Xty_FfP38AgfEKrVVbrU2hO26MzyJF0UUyXLeGKI0u1nQ2cnlez5Ux32iaeI7k28y2McUspOyCImzT5r0XS9HdRNEVQ_CAE9mxDAq9GSnSxybZBhhM_hYLDePhS5a4TofMVlk55Hjlk5qhDkRP95zlZpSUByGkBDeL46m_GKU7E9ycAkp5mv-JmXrC4pDmciVihfEU1ue3z4oA_NKRORAcNz7mkRSxKLfXOaNKcnZOp37797Qj5ixmgr1p0vLgNp2eBNhiFCZrkAd4fYJvz_M_ADVTBfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 65K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ضریب اعمالی به اینصورته که شما اگر ۲۷۰ گیگ اینترنت داخلی دانلود کنید، ۱۰۰ گیگ حجم از بسته بین المللتون کم میشه.
این کار کلاهبرداری خواهد بود، اگر حداقل یکی از حالت‌های زیر اتفاق بیفته:
۱. اپراتور موقع فروش به شما حجم ترافیک داخلی رو نمایش بده.
۲. این اتفاق برعکس بیفته، یعنی شما وقتی ۳۷ گیگ دانلود کنی، از حجمت ۱۰۰ گیگ کم بشه.
ولی هیچ کدوم از این دوتا اتفاق نمی‌افته.
متن دقیقش اینه: هر گیگابایت ترافیک بین‌الملل معادل ۲.۷ گیگابایت، ترافیک داخلی است. به عنوان مثال سرویس دارای ۱۰۰ گیگابایت ترافیک بین‌الملل، معادل ۲۷۰ گیگابایت ترافیک داخلی است.
مساله اصلی اینه که
این تصویر
و وایرال شدن این قضیه، شاید بیشتر بخاطر ویو گرفتن بوده نه انتقاد یا اعتراض. ما میدونیم که انتقاد اصلی، انتقاد به گران‌تر شدن و بی کیفیت‌تر شدن اینترنته؛ و همیشه هم این اعتراض رو داریم و در موردش بحث کردیم. اما انتشار این خبر که مبنای درستی نداره، صرفا قدرت تکذیب اپراتورها رو در مورد مسائل مهمتر بیشتر میکنه.
باید اضافه کنم این ضریب ۲.۷ اینترنت داخل،
در آینده میتونه بهونه‌ای باشه تا بی‌کیفیتی سرویس رو توجیه کنن! ا
ما فعلا در قالب یک هدیه، کادو پیچ شده و به ما تحویل دادنش.
©
Taha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی ۱ به ۲.۷ هست؛ یعنی اگر ۱ گیگ خریداری کرده باشین می‌تونین برای استفاده از سایت‌های داخلی به میزان ۲.۷ گیگ مصرف کنین.
اما چیزی که کاربران میگن دقیقا برعکس همینه و جالبه!
چند نمونه از پیام‌ها:
- اپراتورها درحال شعبده‌بازی هستن
- ایرانسل و همراه اول ضریب دارن، اما هنوز از رایتل ندیدم
- من مصرفم در یکماه طبق آماری که خودم دارم حدود ۵۰ گیگ بود، ولی ۲۵۰ گیگ رفت توی پاچه‌م
- بسته‌های اینترنت با سرعت چند برابر تموم میشن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پیام‌های زیادی در این چندروز داشتم که میگفتن اپراتورها ضریب جدیدی لحاظ کردن و مصرف اینترنت بین‌الملل رو چندبرابر محاسبه می‌کنن.
یکی از پیام‌ها اینه که "امروز با پشتیبانی آسیاتک تماس گرفته بودم بابت اینکه یک فایل ۵۰ گیگابایتی دانلود کردم و اونا بیشتر از ۱۰۰ گیگ از حجم اصلی من کم کردن. پشتیبانی بهم گفت که اینترنت بین‌الملل با ضریب حساب میشه و همه اپراتورها این مصوبه براشون اومده".
توی خبرهای رسمی چنین چیزی ندیدم، ولی اگر اطلاعات دقیقی دارین می‌تونین برام بفرستین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YDrA8hrjckTk4f13_bAw768tWKVtFHFdoy2LVLOrCMIWibGrq1u_vbdr-nBbxgO3ydrOImnZH89R-bigDqP9EDD6YW_8wUyAzs0-9h3nD-1g1S_J4NdN0oQ02eJnvDOpjNjPHdFGTnnMYInD2CZexm92Nwg6WA3r8Le6nfVychaGwwq2MNrS5qZX9AH66An7ifP6UPuV5LIAsZONH-BSa55ALgtp1c8qyPg3ouNHpr1Bz05iNocmfxDecB6HJvVfHJ650_OcQOl2-nqKUrRv7ctbi5RmZTltxpp9JXluyLYKb3bH-rXvAlne2B7svCBBvSdE55AW3foobnNe9SPmvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ‌کس این چنین به ستیز با مردم برنخاسته بود ...
©
sadroddinfallah
بروزرسانی: تعدادی از کاربران میگن متن داخل تصویر گمراه‌کننده هست، که درست هم میگن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OsX71AXp78e8th8JwuoVXZEDCfqJyKVyGQtHsET_kjW9ptwC8ZDIs6alWjRpuBsNYIRckBlFnhpGxaabYEEu0sYbjoHReziMgAZaG1PFaOs8Q86MKInr2krN05zVwE-J3kf6gXHdfW6D5-fWOkSiK69Agc46-5gOaGeS7RpMZ9gaHwQxY4bs7wUWqyg3xHxfWwxtbJ4bDHGzbA4Rt3QJUUDoZ7EynfwzxpoLGDQhZKJty787hWJk8zE7-EctktiM0dHlbslD4XLITjfg-n4Tph8Z9SP25cExOD189CCLltfvvxb4r7SvZlu6g3EwkGizGr0H2L3ziEhhby9EtE0Dsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هسته Aether یه آپدیت جدید داده، که امکان پشتیبانی از Zero Trust و تعریف قوانین مسیریابی، مهمترین تغییراتش هستن.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eFyBaizB32VvbFXZamjRFXZFTK9OdJM6DDf13QxxV07lHonF_WI_jaeMvYMD-WMY_n7zHo8gwSabsHcttf8zOxn7Oi8gFYFxXepfT1NLPsyZ1zS-QCQn7520pjDjl3oS3H21l11NZ4gwfp1xS64tk3xA731HLiE3ZfXGaihbXoRMhPLYoTeGbYsY7Gsec_MHhugyi3RScSOyafUj4LhE_SpDWQCYIDniq4SfczIxyV45P9ODq4tSreAID4CmpABvYfSOhkBiXn1hwPO0iF37ermBWI_QNzsvkof8OFByXIcloPc0VBRG-zJyVlSaLA_Qh_BRhm1kR_msGEZAQRt8_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از فیلترشکن بگذر برای اندروید در گوگل‌پلی قرار گرفت. همینطور می‌تونین نسخه ویندوز اون رو از صفحه گیت‌هاب و نسخه آیفون رو از تست‌فلایت دریافت کنین.
در این‌آپدیت هسته ایکس‌ری به جدیدترین نسخه بروزرسانی شده و روی افزایش پایداری اتصال، بهبود عملکرد کلی و افزایش سرعت برنامه کار کردن.
👉
play.google.com/store/apps/details?id=cloud.begzar.begzar
💡
github.com/Begzar/BegzarApp/releases
💡
testflight.apple.com/join/cRSCr51a
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IqyszBlPd-ULkvy7Y1j6fLFNLa8pL9IoDmmx5rQ47yqiigoc7IFKomNWeAVGxazKXC17fW-vznDfDRgXE0wkIHAVWPeimo5HCGgHkh7z1r4gIRxpg_KejXzgdWvv2h-6KWrHJgjCh29MSVlMikIb6jbBKx-9589T7UXi60PWzHIiH2E9jO4LjHeGA3twUyfmfTNYBhuJgrE0C6tnMArraDeXMozh6W-ITQF5OYcwCUUcVbnxq6HG4F852JGX3rkLMJe8nX2-x87erreYGTooSovFK6ZnmZeprbqsTaT_CabvH6JxnRH6xhPoBqPJVvsDpB68qKFekkbJRXlwAGU79Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SfKK2qu_WUwmaoE1H3oC9XhtcPCgrUn1rsoNjMHOeyL1hViv-Jfh87DH0qOzsVQSzV3Oy8IYTKwMnJk32ZmXUodDvDXqSr4Be7o3ckOU2akltz-ZrUxgPesI4wMSok6PTNyKrUvqVijNRYOZZojrLz1B8sBqMsetdS0T_5NEu6BX6O8GG3EFmbwpg8b10Nqka91FWGEEiOLkqlCbHLaFYcy1HZP-I4jEmfa_IxlhjXgWs_ycsPRKGreIGZwgoLYPMwQbf_mcAGexGcKdSazAjaajPXgCZpfZc5Yq-dyu16xNplBPDFbRpJVhzvnpzrfm1yWXobMoPLnNK0z6DJLlYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HWzRNnpCV0fjxuOvoyI6LnW1P5RgR4-3WaocXMORuHmKScKc0TiSMpk_-uggYE0b3sBTrjnrJH1qJIRUS7sAlSvZntbVXAuyYUUkeJ1z2d0Agu9ntNxkZx4fE-A2VyPAuu9dBGRgq84QSSezFEjXywk0iuMm6XiX50J7OgNCwdhO3Vnph6nRP1dqeifWOh616oZyl126l1u21Q45owAoVF0YXTqVH8IIxkJdrbuo9jR777LJjZRrR2GXso74doLrn5-LU8ia4NVgXD_HpqmEL6ROYbqdjH30Qlyf5AxkTS9lM2OAjqUDvn9TKYgq6QyBgjO3DChDI8t9GN0ZJUxRQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oAVMrzR21EA2cNmUY6pRByaT1Y8xwAoeLhGS8YhgR48qEoRh2t5yIa2BKyuhl5FSaJRGwf7q_OnXtWqZhN5dcZAyECs6bKTp-ZPqqS-ixHxNqxtdgasz2UlUQPde3BU32oOZS0xGegstyTgBVumUeSpGuUmL7nNg17cSczMUMAXul8wiLq1YVOfp9S7UD3MtGQfHO9B33IqYs3YhbCYLBQ4dioEwi5UzRno7MG9ALOvfU_GS1_AirCENMCPytEVrPDUZDxMzZdF_Sd_S7Lic8yKooYF6e3Xw5HNu-4bH4pOOWog9HemodHjDMfw60bljAzLPFX8rraV5sS9zxbXomg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mz4BhbNAL437iZ4v5X2w7bdEn62CCjchuIJuDNYqKMPab9vgF-rGs9k1NiAev8NNWNRYxoLSsh7nu1_mYpPSHl6621JJV4hT9THy2WtTClWZCGk9eDBOTG7SFFPjUZN72zhhdn4PV5ANzcbB5t_VA0xqrDDKY7xqFQNmTL-Uoccf-7Z62bW-xL59cgO3F8JiC2zzxe7PqncG9K9C3-OMWGpyE8dx4tzJrvv6tjSxzZOruzf36GE2OtT_rukGMHyc7H-wHSDcIPq5IKuOhbARo-mhHRtfEeepzj8gWk5Dw-PcVlUpK_QlbOFo3M6Wgg_QxKje0ObfBZpvFIj0nxdkEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F5WajLrtJnynKy1mtXgN63HBI4O828-uGyN8Q0YXta6iw_6obP9kGvUbGN6R5z65LOMC-pQkd8mzmROgEN43gfsh6oE7c8Lc94ukSn5Z3W_-UU9kGIvHvCAIvSWWggF7GMP8ZapQ-IApQYZ1rkv2EyPxHsDtIwNcOUXaFFCQwCIT3ors_drHog-pNrz55vobArWOYa6E2MyO-l0oW94gVQ2bUjTXnKK7H3W-sB1O-x-bJtjXhbiBA-SCLzsPCN16iDwjhayMuQ38nCilwu2ztgay5raR4-BkTw853Ucn0QBMnfFPNpu-uU_ahJK0MgOcoeJyDO3Lw9dZjoUpt2Uinw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iBcxSQWOTGJO495qmtpyppQImTFaFxgzqc-xusP6baaJvkqKtsORcjIdk6Ah7SZK9VuBqzLeaqFs8GXjXMM71zeAJvr1nuwpmazYpuMA_hOabZn1tjQM9Fqdh9cPmHafT84nCxXuT9jPWhYyPQXN7h_yj3NB4OvOmpY0X8Pnh-30PhYyFWNUqRQI8Sooy9T-3QA_8DbEC2wkMttQZ9hzI2RpynVRBbBZWTHGpjnGf9n47cNWT6yteNIGVLTKCe7zC8I3eL9I0FyTTqVpK6g14kg_C4Gv6DEi8xKArtDGyW1tqdMDaMzdwFhfjGZFoT7cA-rJrl9HpTDbDmVetoIKTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/psf23f-2DSOjNOa8XLb_HvxFrXs3y9pgdi5fOb4t_4EXR5yK9m2QURDEW4xRGAtDo_qNGMFbj5LiOgXrgFES-QyiitKYg-2rOUYK-AI4_KjhkG08dm1dpIGqHAGswbmJ30d8kq7dRUTh9uMXGRyz10w50hJwugJZNUAN5lHFTRAfOe3h7fDYLIDFfLRo4_EyYMuRIbDNFZX-epdO_a5WXy7isvFBNTQ9BINqwsg6J2mzmxHjCFGmLqLxMdsPiT0PbJQLUSprzDTcKWSzW0KOSDoTCO-e4bPA61KNM9tLO4a8nTb0VDuwl7Qx6VQZFhiACQuavUnMI8F-g84vbUhJPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rNlXu0qyTNcsl0cwSh1uCvfaGONmW3N33DK_kh-mPZeyU6aIqVff60XvSV0qjD-orEaQeTCFS5f384XiOHYggU5JCVXokLO57QewO-CV2cWEhTs-RcERL2MvucNXrJfzIDmgCT1UiY54wVWqpp2T7CVnnA3j6bRuzO-_AC8YJnQpllOx8fpAZpnTEKXUqoSz4GuNmYZpM6W-4lZM3RBryAK_M_M6-0htfLFurCos0vOkh31FjjbwJYJ2XE75KXnDBS1ngZBqVID7U7WdMMpMbr6Rxe1C2eE7Y7WeHywpOsepcitGjYcRrBppGOjqY3Meeuh6ZZ_rbFTEkELixkdwWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UjEEOVKz6R31MItkRtqENKAt9aUuPCa_OcSVbIB2UcRTsjifh6qQWtG9UURcurZ-aFwg7BeM33-g-Rn5gcafzmy7y9vGHMCJHxaCn6__axJfDITmFEzlyu43vEkS2GfrteRfGX21Gclj-gewIAQlEkI9bMOfbJOZvywZ_wzh00hKVgxREkX6uUY3bYnDCjFAFf2RLhA8KRG1Ih72X7R2GJ0c70kekwson_qU32rn7TsFIVuPao5LQ8jq6nd0iGCFFefgac5ufMIZ50S7vORZIoh22-6blUggSaO-wowoTixIKRZBbp17Ck5tFMH8KKJUZJyLqNNFkpaK_wiW8Kxgkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CF6b3PBnlV43AJXwpWSM0g8EP5LHZ_xwJ8wtGrVronBolpWPKvz_pWCFEVQvgMLPli_dR7HJclbJ29MUTuvi2Ab3HWsf0Ct-2dA6ZmxZ5hOWgdcCUkKVEGYV9kx9zYYXIynZZO2t4VHRLEBaTB-SRGvwzrjTDJRcqZXtDL64bkpFKzH4hIzrAhpw9YYxdrVY6QiEn7g5XNfupiZEBnZbnejCZA-WV2wEAGiQ05LflYoDH55wiKud-f_ms_iMMaTgg06WqGoCwy6QAEPn66tCCeh3sRjKphhWQsDvaNUJgZZbYcCteRbzcOtfYNJt4Xxpa7k_z2XmYdwDJWiIFHoosA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aMI67XTUtQuDZ0gXyaFajzIueXOqE2SDtOxpjFdEFuPe-aD1rVm2lz2cDNeGcpNxsG7Tq2mzuVt5_nTdfo8_Rnd9LCxL2gaegHfRme1Oa8gOqmL5HQSbl2tah8_yUMCpbAtmyG8FGw98fQz6ApofP7a5S8gRcCMqXfK3rbGYF4v2V-Jf6209zYFgY3Axr6Mm_7Szdk-NptH-H2YGSkW-KstMif3Vf81EUBa5kuLGZNuHoiGQuXTZJ01Z_T8U1iST3PsJOGrqWWXZqfsZa6EcQ8CwL4ao9tbqwXtcLz49bA1gEz6xKuMlEIfG00i7SI4dVkyTL0fUeviLCR2KiDCKcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jUneWWuZyiHK6LA2aaw_X0T2cHCy2FGgKoGWDH35-chUkbABK-5rNBlEQXze-GbP1XphN2Hxmc3IQ_1ka2oHfvtIHuXuzjUKyniyVlmBv8aJ7MiZkYOPfptYM3-jmTXZjCXsu22xhUzmHk5u-aA_q3gekJAVq9G5D9q_jw5QnzyEtf76lo6aVE2PY3s9i3Tp8koHKiAb9irOZIFRiUkAmpeNJDste9xag0g8q1iWaRzwsVx3Gg8QPV2Gsu5wG_W65YCV3Cl8zYczZhiBUBMyevDOceHRBt7q2JQCXHz34fFnOHfKNVXptgJmTX3Ma4-L1wGMgONe6c7xD0VElC-Uig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FdnP3P-SLN8sAZKf5YoS1kcUL5F7RNmmeFN-0gJphcKK5J-w1xQCt2KkilQD1OUZy8Wp8BhnrfnrEEGZf493xk5ILdz8WMflY1A068hVowTfZgWfO2ovtOpdxuhVfafID8B4Gj1dGwwzJ2iVqsVLcOOzM0BLrNPIKBOL7AYWJ0lg9p9E-rDNo7dOGf2GUvkpqf5E80H1LEqrQNoaEw0NqweUQ23bEhKkd5ZayZqKk_OOiAQgWvchi10v3p6kRheWDCyFn7esW_mYh3fnKXGwi2xRn1gnuf8xXo3DGAzT7MQ_rCKIQne-wvU1zkVwPcVfqOStbRorNGDIVCJz6dUXHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v3LudB1P_KCA-CiZ27Arih1PQM3Mi0gxjousxl-JS4pHVdvZhAeSiy0tjmre68Nk6uQUn8He_7YDorHfyczqw-xNwM051HL4BC3yYOLk0W_5TJmq-WST19BZeYRSORzcob6wQ2MZhwS2ztGUT8oTV7qTbqmDa3Rq1N6Lp3Kr9z32UbYajnyVKb9D7BUteyV3RGh2H-aVoLVxkcCVyPq7Dq6g0r_XKTc_1ouXyC4b39CZymkcY-Zqae33hdvL0EycO6QYPmVnsRg2bdo3asy5g-uqhlDi-rbXCWSi83jWPg-vqqA-iesiEGs6tezvquUq05U8N5CvvMOaPcg9cAUZEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QoXgPlt0SH2X8hM8zMdS4y5CZ9Ps6f7S8nH5KDOXCjIEOTxoiXfYk77bDMwOCXyYLMujBrl7CWq1a03smL5INucW8avB3Gdv-N58qYKKYKEm2ka__7IoCYYeNe_xPqLqdNkM1zjJ-fsGV3x1BLNWOvvWplBOXOA2byrCyQLks0c1yWDcCAFv9JmIDt6akAnCATVngy3TqYW8oLz9UsdFlOD4fGTdWEam9wghZXmjc91XbjAwRp02S2VTjLngv7coluSlfcfSit2ptOsEMegQdYwyjuTPLn0Mo4iALo4OQM4TwTW7yRe1NLi8vOlRmZQvsT1RHaVFdKndVcHVAd3j-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eP4A0hDA46QDr0aF01WpDVBbM398ySIC-gzTGq8jPxHnUGxJmwr22d7vVChTAlWQYSPSQVIYZMWrTpO-Xc4Mk0Etzu9rQ8KByT8oBUdFmQrv_8IIUb7LQsSuW5ZzXyxtVYLUXpjMiSQA24el1xfInKCkuABhpMBlkyCSWk7oNt4nUjCX7I6OKPICRt3imqlJp2GSn8KjcpiS4vPRH2QUWszhk3oL3vPp6u_hm9fHTVYGlfq5JZVy-gPOQVDegR-3l8CzEkDEnH8T7A994ajv0_jw5iQzWl6ZK2_duWeipFPpIG8btnSde01y07a5Y6R5HugSZN7EgFJPcslGmaiDGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FpRrmSTKsEgbOtrbYSzn3Jn1OdoLa6vj4DkmkghMUsc7dX741vBA-RkLv-BUV7wXJsiQWUnSpB_A4c_8NxTDdHmzASGWqhKwWZ83CFsuIY3DHknUfdzIaKwdwqkQIG1mvHxC7F73Mcme5BvIMvSN8GHIo8gw0dVVsygIuJuBM5OKFqcEP2-WTmOQ1L5VMEMbeS_epnxF5n6YZrd8HTOM72krvUxI0HOwEe15RMGoiCgH5sfNJshpRv3aGTienshzduZ9bnRBQjVzmMRtQoY9xn07RFKSx_pdbJhVTWGmIhuDxZBMxVOQcPVPWqU_z64Q_zwcceijvlRnEJsx4QYxXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

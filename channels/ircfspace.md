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
<img src="https://cdn1.telesco.pe/file/gG-CUMncPHSm_i8BFsV6xJgCuGkJ2eH4hJU9_4qDivRAfcJlYwCh4n2-KxksZGsFZVJLa-9Cc6VjAess_f7Bf5SYjkFTdoGQJb0zAohe0j3MY-QIPXz_03vC88_9igyHMfre_Zgk5xv_ZpLgcWjnZZKdp2NOg2hBhTX6VwfgDW1MJ1rFK_GCE3hKXpkZmt24kqeXJAYFjw3viFwuDE1r7RtzA-BOwescNFCL9jFD38-6dvF_wUxCI7GX-EDfsTquAqWxqCS4b1guCG94zu_YccFxgS0DWV4nHWitwLp5f62fOxG7Zr_dGLwlX_RJFbeSKmK3nGU6HhoQxg9SWXf29g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.2K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 23:22:57</div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bqbjBQlKXqKO7ZOfE0dBK42zEMfL7Ef8M6z-iofEjDPNpfnJuhJuwYhmkelJd1PTdZO40T8781-1rkdyqCDVDOSPHklRym1H6omrzx5d5ZStFsTCuKD_F3XOIlHL8KmdrRAeVpXoHdUpV_nzmAds8_LHiDLpOy8sy_fnOQwthhtTOlYSuPBD5RWR39nEPiushQLsDVThJ0QdhrWNyO3LyG-jorPwmyi0SD8vHFMbJMdpG7cotGiLwxHb7ZOVYc-_OtEsds1M3jz_AZvzDxa63pZNLrwbehQAQ4c9nZjxzNuyHUsTVHpHNsmekH0T4DU64gHFHIV0rci7BkD3lFMLag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r9IT4gGjjdCkq9ApINNI32fbQ5W8oCIj1nvXYi4pFj-Bx8sFmrTifR0kpoChCZN_cODB-hIw4VXpTPYlxK7U-hreb4oUy3PiYIq9e8QEB8it7zcKfOIHhZynjSsumoO0h0BZb2wmTGCN45Y8F0mwo6V8hKtQivyreQBFEsqDkPF9CX4WmEzqPrbMtYcxQBqUkqLdDx9Bla35hMNa0JmG9Mrq9Ox6NYx3YDv5Wy1s7AFx-6SPeizxtq-NthI5uHvuKJizXWIiH_1susSh1zXlGrXTW8-MxD5ZAYoh6PFrlPLtBwlqM_IXsXjZLh5HXIG33cG_A-MSkLvYx3g-Z3G6Qg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SshzZGXO0Hhrg0FWnc4U6HUvmX-KM-EN2M9J3pl12em1UFopZBVm3URUTtSSO2c8vY8TYbFhgUmP4M_9nMkvXgi-LR8SlP1bKSggBzV0TN9ax4r1Tj5haHm67up3Epai_ugu0i0AmkKAPmR0LvV1YMG4WqtGMHJachnSSQLtGP4bNmowm4ONv6ihxqc4wRDgIgUonvtXZmWGfM9xbyrXcZVDerE_LD6MFWnK0veOECR1BMpPYeUGOXt2y-xXqz8POgv0SbIBtNhxjdlhL2s_e6sHqVnsMQCWEUdURQLmE_cBG8HZcshI1f_s2yzVbT015GO_7c_RlRaGRKQFRg6zbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dz8ug2y2OnfpiKfdDtQ92KfJ8qhQiwqcYSaB9KsTxZvTB0d1YBaP312I_wljxDmkOaPblhF929Ps6_mk1icqt67T7-17HjYE7k52d76VdImCSyDos77ClpZtH3IpnNXF8BHgWwBqOU_nQ0-ZFYstq1xOl8Wzav59ODhG3HGj34PpbhNMmjhP-KLc7DjPEpC0AK0zMrRT17zOdp3iqF1AotatUU--HtvKtCBcXuLgmJ5q2oGAcSoaWOuhhJRYvIm2grBGjcPX_IiS2NSrf7Bpg004bZSHgf4GEU-gmja1kE-9D9gSQRPN_kzpUrspQLxaF8jpvH6Zu-TONK6A_Gcp5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qtNPn4tucpb_4f-_86IiABUCPLnTwU3_vkTyswkYJG921tjyujA6YPD17Ug7QF54ldVhhWoo5BmyRycoVGV9ogqdTYSYyhCNunWTF6C9wv_v-XRvG5DQb9kCjVIBw3e6JZtIn11cbkQgtJbn3NuJkSZiYCAMqVotuXJGwABWB6870HZ0qSgrNR9TScZRDyragByH8s9tQhmE2PvfR1gbFANX5TKqOkp-n8opWeNaqRy_vCKGgkl-0oyQ-8_C-XFIKrmYF_PRHSmLjZ-dUm-4jgXmThqMwt5yZUa4fxqbcsfk-Eo1aD9iJglf_SfDJgokiCs3dyboTJRaffeVTy9ibQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K1Dp-COWjMxCRZeppLvxTouZSgXu720GX1vkrGE816Uz11VftT5NjltYZwCSCJqK4KZhr3LWbOrNa70JPJuff_LDok1BiEqsyS-HErkYfcDNWojmaRt-4LmVXEc5_ptskgoFNWd3r9W6aAhPV0eyYYYYltVMliDMfoiYc1942BeyG-zLEIUrhyOKHPIEoO7d9Mm-JCTZEMgcGBUuTkSlsm2I5e0SD5HJHupXcYbOfUfC0-XDkqU9UernZ9wr1ALlHHHnlGnnlaUz3eKA0BeKXQkXiDrQVMECWrOeZDRyV5Ab6wHxF86l3WmUK_-GOeJTiIfXTM836vSmO9rfqir3fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E6ZpmtBhu27v854I-a2HB7w1_4bb-fxzp-eEjMAzhOwIUjbVOlKl4ZSllMZCns3q3sPNXU8jXgE5guKE_DvvUohwdd498tw5JDATxbQNC-xRgvqe0kOKeRvISN6qbQQubuu5YVIXU2Xc7CzdzLlR3NwR44Vk9D0MyBEny4JmHhp9JPI6JMh5OM6bHr9KXOJrCkEFAJibu8ZQ2F34_nDt0fZSuoE4buyhIbxWc48aBNEy3xZ0Jr2JFX_WcFRtpqF79o_LFA4l0XpQeaOXTs_Ri8vIUNT-dzCE5VpmSFRg0QZPmeeNsEinLvA6C3KSz68J6D9fgE72c1a-VewIxrOBzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mjeJoeLESC-OFrYdQhYw6CsfuhVWDuiV_5JdsAcz6mx6Ms7bdiD2Cfhu6xMHjH9-hdB1woYy-72fPE0_Z21US814OXqRL5VlsAQVhlG-zLzX7bHrqLpfbJv86Yi-BF47Y-28v_0YTryoJ24KY1CHCo-5xXCIM_8lQYvUbhgc76lpvzIJxpxLdnL1cTkoLCbezKMn0QOuQWmSs6awW5hJrTbqHMFOMU8oFmy4ok1s6B98Ox97A2g2UYpRr2ANd4Ygh2dx2q5OiR4VR186GUF5jVNMPSgZ0pR09ZyHP8ZrFMq6HJxrbFJAMs_EHag2Hply2LIW7e5V-_x6K5At7DIvZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VWlglPWYfdaNZh7jNYw50KlzkPW5_qqUev6dg85HrYwQsBoWWFML6g_OjgU3y9BKUF3F9PKRtKDKm9yz6ICKntwOO1zNzyrA2YogFgUgkMhVo95t8RT3MM3q7BqKycTk1L0tmFcAH1-Fu7k2aK3VCzP2_V1kDM8kFXgClv_41K9ChxS9IFzxnbOZ65nBYZa2q7FwlE8hYvaQ8GsUENdsRMvdHVzU9vCWui0sqzfPdMWamOCsBTxVwsDUw5HdM7atPNBDKKiNcptrmv1bhPKelxwv6FMliqmGZ3efIhmLmpApafMe5aIEW2e9XaFXVnJDusMHcMZGE84rvO3ioz7i7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VlkPwMK6MrOPcIJ_vVK6Z7R5vExiAelnKiiCAvaCtveNvIWQ4FO9RZzc1wVFcsFCBcod3BJAykEpOAkyZwTlF33ML1jtUfWYVM1LCbVM3ioo0_EP2LWHC4FhUwSOSMo6-fYCN0HOngXyBnpoi1gqLgqxnZV_O8bSftLAci8JEkCeLlryT-lChsyVXKn2lQMFr-m3L7EMVo0CmvwaH7BvN7D01crRmhjv91GJBUTLs6BblpRzAkUMarSU31YWVlcFW93RtV9s7lar4PGrI4YJVYYgIcn9z6ax723qd2ZtbWypECgT_-_PbWQIF80iIt2JPAK2y6h00VpQ9ooit7M0kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r3Sj3Vwe68NkJBuPEH252J7YhgFAy-rOh5gaAEfpcejrwaW7gJDzzNMKa9mVB7uO-pgsD0_2ogBlztbkpoKRdVlCXkO_8kYuuMBKhpiO8K9krNpLEyIB3qUEMGx23-G57woJ0iy9V35dv0E4kO9JoKlsj-0-gU6xsa9IsHgY6RPXXktPMTfv3s_aSjv3aAjrFkJ4PNj_OqB1lXUskjJNoIt1wCV6EwkarUzxQj4mfjHAH2waGWornBP5bhANx4mtK-qJkZ2hrRp78XPMMw6MvktovIhq9KlK-6zyrztA7VjmJlvjV9B_Ya37TkLsKKyo-6pCCvupxvzdYv_yBEM7EQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ii4iitKlCR3Eb50v4bmxbr2CaMMLQijtw1m9bYPzbThRv7b-0Dp5Zlubdoy2LIF0p-ptB7QlNAp-psGaO5EvEHDtonZjo5XozTi0ZoIp6jvnM0gbVPgqPhck-YO7UMkBq9cNDu32VvVl-kDwCDB_aJotS67o9uwO9eBwnlWyaa2kulECMAN5PYca_zrMesx9W63ViaUwIq2wIC91JsPqitJM-4yhfJ8lbOej79HvoQiDSmvck8qrW5oFdYnLctNJnBBF9rT9hgd-mXKa38zRKBNF9urK_QL_LiZgJhKRqU_n9lR0UVb85gwkwAmIZDfA7soR-Or7zS6HPqtKDHRPsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 41K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 41K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=SEoTZDjrRVBMPXJAdVqQnZs4kPUTCL9D2469Ap7UObrrF7IHD-TD-R6zaKQXUF4uqgMlnB0BmJDdhRjgEJeI2lmATbYEI1F6ZO-_R_0Mybjp7SsX3aPpGM5kxFk5kMqYdmKq3XDjNDCbJ3YicmX0DJ0fFp7xUU02HGx3PLsvu5rD0IPo23bvafwIZXg5GWP9SdKT9sC7DuuY-keTDf-K8TDK6kkE2GTN7njGCZxMsmWQQ82tULfPNBNyoal-nakHOjbloAcQps6s4R-RVpY14PDaKEOQfNzRBgqYCl_a_1tTgX0Xb2vBAo3aT3TvB1kfj15Ts1LrehNjgI-2sNFORQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=SEoTZDjrRVBMPXJAdVqQnZs4kPUTCL9D2469Ap7UObrrF7IHD-TD-R6zaKQXUF4uqgMlnB0BmJDdhRjgEJeI2lmATbYEI1F6ZO-_R_0Mybjp7SsX3aPpGM5kxFk5kMqYdmKq3XDjNDCbJ3YicmX0DJ0fFp7xUU02HGx3PLsvu5rD0IPo23bvafwIZXg5GWP9SdKT9sC7DuuY-keTDf-K8TDK6kkE2GTN7njGCZxMsmWQQ82tULfPNBNyoal-nakHOjbloAcQps6s4R-RVpY14PDaKEOQfNzRBgqYCl_a_1tTgX0Xb2vBAo3aT3TvB1kfj15Ts1LrehNjgI-2sNFORQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 54K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TmXMfKpu8RLRL0-ZivSj8N-WDgHuA5eDdilrT2BXnyluGWzKPFUATwBPDuR-UMhh4hmauL8mtpuTUQFljAdCPgAf-mdHSQ2DNXocG1_G015ws1XiuKmhr3X1SJA12E5NlSd9J031Px4ZzrURLZUWpxJ9Cjoy4nUGF51dwRojBZwWeNFVLGuaQIWVg6bMgLW7-9MFNdOZQPCfUl8tLkWSQCTGC1is2CtJORo_E6qWrKzeF_MLSft0_ARH6J6dHbROkYfBDIfPA4BvfrQxCjDXHzxG9eNP1C8LdIJz_a4jsI1pz01HIlmojzgoNcdYeV2xn4Jzk1GZfZf9ojdW1mTjBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WTxll-XWrS0vY1tHJKDotxsjZx5WcbBELKPu9zeppOFz719guYZkhtmcSCCWQi3Cza5JrzOZ9qYC8QPsKDW0aEl2wZMQzLoLPXQ9aJnWWWZxtsIzJmrp1b3svaLcs3fbk6KFyeoPT0I0X56I_-iTbcePeDGk4bTp5azato4nIntNbc3mqZQ_EmJ55Rd9rOmnXlQpeXpS9PZr_hV7SOFMvhU4QvYaF1UHNwJb5E7FbAq7G3ODMpCYk0ZjgiAzJnpHjqgNbHP8i1DaI-nvmVNRoP1uiSC4KTkboWQul3LJgMauex3zKvyer2G1GfH0v3JI5v1rnoPdVmPwY0eYayzBvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZHm_F0FpuFzoE0TcWzww440oBu1zrmXJbCX5G-eN3y8px8YMIb6xj0KkKjKj8m0nroCFArQjO9m5hyHMjCD0boEejPAaak5v2GBf9WJFU_a5pvY6zfN0c7a4d12MQ6VMuDpkinAIkuC1JCXR2cKSimSkljw39H6_R48dMsDD0-AfyrslEvDcqE6VYJKDH8RsinPjooTv7VwH-ymbBpcYeQ2FFrsDEIpeKyCU4jcVQ3dlOYaWEmsTUl6doMXUTUs_CgLFk7eBUnmqJpDe0GuflMv6Og1J5V8Z7POJLb7S9Jx_8YN1lPE2Gf1GsBQNsC00v31_Q7UIM1wlDm7xC8Wf-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/umiG5d_3qGVlLEKTLsUsJVmgQiVIwHy-u5_PRuKQymnp3WngkXNonJJihEinxBOrRM20aY4Fdjs-r5oFa_jQAGin1yUW_aOhGIk7w3dRIq5fmq2mJjddjNWQiTNLRAQl6-B5WpgrQulAuPJUJjlpsrrArhs5Ik0Zh7eWwdqS_rGpEpCs6FKMPqUbhwmnHWRP7zcU-Zq9DDB3XBdrSGlsARSebyfwSVGN3q87pCtJdFMGjOqM8M5hJN3B-F-5WGqmnDvkyD_JDAUYnKjXTJLvfNS19GlaHs1B481WEfbxzEUs2g4X33axOIdB4_J3-G1kIeED7bHaHXddSz9kkfS34A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kb3xyBlDzwtL250dmvyMcHIV7dPN4uwwSHE5z3wE27ljju0gLMKa972sWvs9CMRF1lduo6n8ZwteXh4y30W5N3ei23mGZzbUj19g1B07RVaVhsCHqoJGTy4D07gipdpoPf8mhAArKBmwRphvdO54zOQVD_t9-5-fX3voVHOZSLMYgXuUC7ajO0_TxNsVVhdwFL9ybCs0I86DonkDhXy1cQTTgE2R-wLVnklr5jubr9D1yNH8U3gQpKSX1aqv4G8CnG7OLLTKJTY6muQ57iE9e9fOzsYUK3UUEBzOBELzm-8DbNee52cL8IpD2BzENu2EReB0PsFtHaiyOXr2lc7H6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RLdlwR5owtHWvj0hWDAOHlKSftcCq_NrXbZNfniqipENbJr_DYFYL9vKQY23vnKoyirjPzk1o7AFFoQsZNPNiojA5-MgNbuOx9Oa6V16GJ3dfq34zBL61G-VdLv7icodh6bLt7XVhxmbwRrwOharQT41uDgruMYHQB00u8IpgXZRE1nXjgvzX21ZUAyYWbJ0iE3FvQv6JPHtXc5t9rUcapF0r9OzJmBrLJ5aiEn02b8ZyrTBywKXEdI0Bel2Oq5yXv0fp6Lp7OVs3OU5OWuJJWYqqQkAoYFw6VvbqUOg7dN_p3GIAMo7ZWKrqWScyqMBVEU4pEK7cLLL2SO1DtW-fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JOroYx1aMxmVBs1t27ncvCSxP73K-K1qF-wCWPjoh2PVjdPVDB5qphi5o2LYYEgUKzzbgRdDuYobh1QqtJRpkRH5K_Qy4OBOrJxim-7uGFhPE7JRgOVqk7Pc-FKscITOu8xycLMNV-RhaHY3a0r4ToHGopsvUVxuatFE9XOo8AeC9OYd21SjH5SkJRENXTqPgCnmxtvXk36XVR7W-lhcYoS-x2GcIKcmNCxBQvNbaet1ceU_rygdW1D62SfDxFXF6T_t3Kf9GAKHi0f2vSmPKbvSXiZIvuI6LDPNNKcomBhCJ_7xNxWIADN8pOBQzLpt8ZAZa6bbzNLxFZQTIOaFiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rfeFf77wbmH5epJP8qurNG5Qs-DlTTOXzkPrvXezlEcOxNV7RBbenBF7QUfXqZiJBjjdiK4Aw1swcIeO1dRqbLV_kPGXDl3T3gAdq4FFRbzp1YrFBsPhCyazUBz5v69eQS49CHa_6h9hCbgLoMAfThTT6D9zT7XAl98hO3ocJEmrFLpHqswuzZHlUiOly80AUdwxKDqN7eORboAHkB7M2oj0KLcdXi3pG8w5FUsdMXN0bw2VvdZUVYxcgNtjwqfyeJrEgtoVtqMdoIOMzmRebtoInV8j23E7LBBxXP7meLc0yD0DsyZlRIxJ1luk_QKSXdBQR3EWAQe0CjTHjpLAXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Oa80LSqa_BFAl0iTNyQR-89sArSGUrY3xt5TVacMdBNwhhph-rmi4t1l2DkvwpgobyHCzTgOwaYy9RT4T0po8YkYRWt-DBSQ8Jr4XuPf0kWAxoykET_i7Nzq6rar7RsHnoesiinkq25ByfUbGiQb8rjAh9AlmSbHF4_BawPItZHk8csVm8NO97_sHpvd00RknAqK8HXon70eEU8P3YUH-C8_h5fl7yiSkz2_Y4NqCr3fYWeWwwfkJvDykMW9sus_oacRhXza73BMO749pUVyRe4HSXnyFT_rsPbQcVSyZCAsrA5PMj-BlCx8Yob7so3FNN8HLylz-495ZGx4vZobRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IkN5z4nEQet4fFzcGmfBk3v8FLsYyCXQnl9aD7yPUG3qYiw-MJGZUKVn7tUxkZKwL6DWrB47fwUTZJF0h1X-27Lbj5k_yIRoQXPiqnqXWUBsTK57uVt2Csh_a_VAPpdysRxReI7BNmDAwUjP_M8_9lPX5hvaxSyvkihZNe0wqyahlqU-k-Gy6bBp4OFckqQ36p_p5QbttGWNTZfTUn2hvkQwkvdmA0DjSn41ZJwO5ExJ7HvymxZAW7MsRUkdV0w3DlnI03cpmhoxLxKRzWuOqM5-MYNfbs3d7rd2aphv1xVEqv65Dl-Lk0LC-aC_DNuphlJbtCpgJqMfFDoHui-2kw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gh0qAqjtghMXygbmx7MXxWCBoqcTYTX2UIP2cVLSpyz8LyDCaOLtyR_a48VrC101qIPCaLgsQaMyi4Qd1_87OoKKSlaYxVmRxSuLw7rbQjlpbbxRau1bxRUqT04eWyUDLxPy-YrAK8BnSKus0TqpSLz-JtekXGxRlJzda80gk31r_bw1HanSP3BhQahk6W99g4b9HdaBvCRB9x1Yz3BFIEZyu2ZjJg9Tq_jsrqjeFyWHvdCzvZpQ5hD20Zawi1ZvcKJk4UEeQ7sRE7TyURe-pKinahVAJDX-VWBkQt3BrUeqjMounr_NZxKAWy9DTcJ2a8nbpjPf_D4C9VwuWDB9gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BcgvxBijJXEVvJMj7iMX7tMBvdtycm8-vvtm2gMLeXaxntinEXdHX-lEgqHVa2rMxkQGTkkdNrM3Vn6M3F3DBRELWd2aladLaMvqrKctKaoapaZJsWKZa9_7Cp2W1yWlZnK7-eKqO-xq5Rrq7x3VDdq8u2w5cBBASoYdUYrQmEg3OyU15QlNNlKQutWrMGi98z13MJK_USTwFXpegX6_wZ8fbXCO8tNJjzRSiS7IhW848LWB5YMQEAQrpJ8zu1Oz2TTYwVVxzn70nIifK0poaPcPL3nIiqo7ZAyvLhoQQtf_ML0SFDp5Z0hY-sYzAd-nSzRy8wkTOV9GDTCiRefvKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iOCnT-EroYmzjXIOYyMFw1DY5LoIIllAhUhwHkTfK7S8awKbER6xCNw2V8FkkmUIJ5f4oyvlQvYhe0Z85-0uP9O1Tbx1KFnyNbWOQ4Skk1nGUzwf3sX7G-acL_4d1dJE4DaoaRH7QiNWanR4UgxLfYLfn7JYu_znEDLx1VrFZm7sI87Gi7CO8mC1g11YBtjetZxUsCdK1y3fRkMDtLPqTDG6FCHOqjZggUZhfGomH5d0yRcP2d3zaQVTzae0kQ0xRxq562uKp3RaEkruZf00g3v0544Qs9gcVNbZatJsaNsafHqLYb4bU7rlkK_3G-lq7Qu9G7K_xxRBomWNtdL1og.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gb_-LH7Km5VLwimZifrQ_vk3LUUgxBLXwru9pwd06Iyoz0btZsBcLAFVR_weWUXDGQcgRpriSHuZdVKGyMnbPwCvfEe_p1CIU6EcHAA7w9g8yvjZGqKsb-lKII7rviCSGogZb5oDGtmBkXkpLY7BnvxwuB9TELTkTSYaFFtCIR5N8PYUthBX5k_lPV_ciahYHPY-EB5src4FlZla0JQQoMHbv3MEgu1CjR4CCn5p0QisfDEzuzN8v95bXWG-SQjPjSx28KpM-om8kfJllSib5KQTCCHqSp20sXok1ezfKOcX782ou3rrBIP68RKT5seTQQtopm9Ls-cHR710Htektg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O4fzEL2wA19lOTrGliTCHS0XeGJlcYWzeFVjOBeAm3gWDycxDuafbtWBUvAfpytlsq1yzCGGjvAVMHS77_w7E-vFLF2YTcTIF_Z7M5I1RvBa7_DSYgYAW9tEccwIgh7m8mzjjH9HcOtUMaTm2mjHCBUEv3HMSO5ptxwLYZDviwNkg8o9LIeF7chi6faPzRd_iil2T-fHtWCkD_g7RZZLvWCrxIwxQjXL_GVV5ZQ6Su1MNXqxl89FkdudmYyhZqcz75IAqQGubXiyr8mJEOOgH2jeeNOLF15Cjklh9IJPy2NAlubQ5a3a9tj9BvK4Q90LWxr3eo7P3kWptciDFKN5WA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pTBDyKIEEchu7cfDSsgbOvn-5DKxOJbBnUEZXGGFSyiB215UAhCzpUDXw2q2zIKJDq7vzUSGTX6SE9Xo7cRm81YxeAXtGF_RflHvj9OqqhQ4nVe7hXX2O2LcTIS0pOLLxh3qKUpN53MveLYg70HBpBnjB3aOf0fDZQ6XQKAYh9MHkaPhffWKRXULs4orR1TxOSKmSbudD-kFai3OuZX4cNBKyZUdhIASZqQJWGLYLpo7ZpqOF_lZ7qV48m7vkrnGX2aUfwfpskH_C4cBhUqfHhFNIQhTGSXPBireRCl1RVluEiHnBsgPe-cvApCkAQ7QviqKcZIvdI1cekFFLW6z-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UFj8UluveH3Kroz5jXNIvjswD34RKy7zet7Qep0ax91dV7fSc2xWHLCjUKOlfWiN_X4cnqdOm_KDxeXEMfOqc4_igyojxaxZfsn0xKdSBo6AqNgjNmHj3dG_4lzX_0mfPCItjq_2w0doRfExilkYJJ1iUANd4k-e7Ljd_KFZ0Z23BM4-IYoKPmkxhRxTeADmFTdJqWbQPs_J4tkBiRidfUUiqkrFYTX8LIJJbm67USQ8GLsHbVCn4gypX7SB3efDdA2jQzUBmuQb6EQFtGrrSLEP0CpDp3hvXc1jUqYkHtbjc_DCfyPT1bAdYw0P1MPcu8I4dGdQ73CNbVrq3Z19Nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ThTLk9xJBK9yKVJhK2ca73Cys44LhNhSJsFRav2jWpsQ02i2ryVAnKADR-8UkwRHZgqFIKjOoi_VYqR271q1ma1FRwsSS7wNj_vTTXU-QVlYw5Wde8tbv3m9fLXUvxJpporwB51Y_TY6SsbLqWVmYkMM9JypdVsYeUUPDf2-9kW3q8RKifEYppuX111yJGklUWyVCFKQdyLHdgupZDDMtEcHnqOR2Dg-AnXFYwtU3kpnOGQq77_UWFwQ9Sll_m6w6BQvJkEYD_Eq9oMKGlfYGB8GjnsoQ_oiXNsIwif35ssfanx6xjShF6K2MVrBZ3C1htK4q-n2FkL-8qTC_IeVdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SS7h5IWIhvR1f8A7mXOVyb5fy8b4FBJ5sxvIn08w1164OqjuJ6UrQ2vUHe7MenObYgXA1eT5cMA3Hzx_yk6OLyF5yaw7bvBtraxPwfev2YC4tg_ujWFHAeAgZos2AltG9F9EH9vVhItoTLMWg32Ej3ccaXCFmITm0ps8mu4my5UahOy2AYAF92OforUQ2STaq0-5eHZy61QwG-44nSrrkqcKHnZ59qYmNQ1dH3IUpsiXeZgdHPtOvuCF5YE_8FF5UmL8xEw27SRS2ls3LIOj6c1Pb6RExsaSCRtkBgfNTupyaPgtVV0A49hFN5Gf-izftQxFKiaw99YrvUkwejRQOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z2NO9CGL8tsGezwhmR9N0FvpCePW79eLG4s5qDHnbg3g6T6QyxLSII5GbDi4qehSUAP_vqbaTtqXOZExuab5fLr4dhMQHBleuyaFl4fubB1k-pfLcjwM2-3-qXI5HQIZOdPgV1kO5sWKOWsYXIh1bwje0mo18A5n-VvUQwoyalCmj2KWZnm_vyTCOdxQKBJ3KIM5HZs27PAYSry897sFEKGOAOFgHkHGUN7OC0SVxRsQViW5tFEQBJzcA1_6kqTnaGwnfbbkbKZp1Dq0DpCIZ8pB10aELf0B3SbvsOfLOyMRcKq5zluNZz5aOD10vYmStJIQZHT4lVHJ2gfa3HfYrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dRtiSvqNvR3l8suqXL27T00t9bgRo2R5Xw6t_jWYwBEV2P0AYJ-h3pUkNbm8QS79njpDShu8fD0p7-Qct0UvEJxAqwnFQE9SuZdQF77_TihGpyvZ6dgiHM1F5UVKIEom16EVO-V5QjsR9Kw4sOV_mLeVSGjHBa9NxL-_sIgqqIUfMmXOwRfQfZ0Oq32M3QZG4_nLbLUcDf7qFdogXLFgCld7p3zk2om-VqBNFHYdanREMR57j4XXLHfh7Ue0YlITgHJ44fptZ-GsBZM2Mt-J15tXsMv1TYcn_YRjpKo9vwcPTsfQTXLBl49XAket9gQzC2FtC1eo_FJnTNenRmcsuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Oy2B_k3Qg_cW7UjBF6y_in1ahRZtQ9C-SGXA9U4DPYOectuPrR3tZtlgCzYFa9SUsKtPY2i-shpoo15pF6RWnp722D736J_cGOxayeVfTNuXWKh60FjbClUWiz5Y2hnmhk_L0j1IGhxEu6zTKgt-Q8kGZM179PYSO0Dk9C0-CNxIXZg-wdwXjwZDkTlNsoF1Xjc8p5DK1-fPzc3U7mQyA1AgwJp32bkY-3nYqeieUV1_pwgGZePinunoP9pElf2mj84MqMkjeucZ6ZTaalYD0tV2pXqbRmLGGp_SyRP6rJZ5Ft0C4MW08DGHgElw93M09CiQuiqjbzkUQXdYokv6Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ucw7z4z1P-DMR4KtU6UZbgQCT1fMexPGxcRBCvNv4pGOIVrTaiLCMaBNFfSNXPTV4ufPIxzO1aWyqDcqksnGh-FB7lP0W9dIjK0_EMoDKUtPz_i7XWGMaYUA0X4UonKXXkScAF4phHUVMLTtzRU4TQDX-MGRZItNyvdaOaS1uvciMo8ekMD5iUFEhQAUjX9Hm6XpuxM5XTA2KKsgIT4NV7Fvf7aw-_KxuSPoua_Lw8bnezkUUnMmJ1jfKNr4JUWNlj4cTQta-wvoyxscYcz3g8hb482vafdnDBzY1pu6yF3Jtd_EyEluOdwhNrWM3CcZLm9ReUN7hiZ2s6MYsZf2rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tV9TJG7hk0YBxGSkuWlK2po2nY6KXYLqJyPtypaxwW7rpNm5oTjKXR398u5gyb_Ff6zdwVxudtP8FrbS2pIGIMzkXJdn4RPvqGHqNkY412PYh14rWJvjG4BCDn0jav9xbrvX513FQouaxGnp4TRvopNMSCdW0OC6Wh7hkjrhQy48f3twF2gzxyaIg25qVJUyN6gXr8DCjMU152jAtaciSke7BNApXbN_QoAHXBk095mlk1zcUhujwl46_HulWkfivpJPNLqI_9FYHHwUsE2JWmZAAXQRivfIYTXgXCIVlAbPNV4SR10uVMLfg40sUXfBVT5MpjdPsxy07XOugHwI0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KqmuWdX5KSQ2OOkJeRjYAUn1GnMLAl1gDE7EsOjrG35PAtdsSfeD-RQeb9rWAL_eRqsvCPrToXpzWJrDhOhMh2zlFvXB1KDzKhORVo3JCwyRlF7vbCy3yEx6ncjmJD4J5UJ8y6Bg1P0vLnLc2L7L6Nel3-TUHAW4a0ohAEAS7WgjbN_NwaiU_pMOrHdxo-KJQbxECqD-929Z8snuqmpmlvdEnfIftAybSb5NJgOWMDdd1QmZoVI9LW6oyZ-sMGqHUaYgYfsUZUUOPbXgHrxcZUffn26ERKPVzpko79mZlL8KaSkrOm82Fuh30EuKxPiTj95r5uHYVtPWj5y2dAgB-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C8zl8to4ZSNh67sZViit49JA1BLY2mfguSVul6SBgd-b-PRbVlRNimYGQ8Ds203cZoqh_9Bku14uY1t608Q6hdhYbDRFg7WRUWIO3wyHWODlbS0xt1kEXQ227M9DLwxSocEOSz0HfqaANYm1CamUXg8MoDLj5CSHYMwohrHHPY9orV7W81taP61NkQplReI5k4bb0tMh5imR-ps6wHeU039uxFySZS_MOIbgYTQjPA6alqZ5_8mchYgWQ4bIf5kBGrGotESHSkZEu59anSbzx0-NOskkPzQ0nxQRfmgABaQjWBNxQCAYPlg1F-o_7aMZjwbErk3aDfz_8o2mIkClOA.jpg" alt="photo" loading="lazy"/></div>
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

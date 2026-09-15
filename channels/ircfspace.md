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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 15:26:15</div>
<hr>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J73elsIxi0l0dCjADTqMW8HixpBbkd_BEEVGgjQgbTj3awGoFo1OT5-2h8nx_wquOkY5Xsm5KlAs4k4CZzDolpywFd5uk__igq2WuapSlB5NVcOjthaBOBlzmA2Qawsx3JnutWjHJ7hhLavrML_TmLHO9yQIyrA6J7esjUgtMHA1uYKNl6cOyFXmF7Mf17AIqqM1PGaUqDCaFIYQlA4IcrgzUtIgrYeqQf6SyLPPPU1QqkatXT3eq_Xt60DOZJDa0QM38jXxG4rg2GhDgT0eTx-9aGOgy8WdJQEx_hydUaqLIc4duTBaXX0Z9x_BTGAIonoJRkVG7Ufzmr2nWo_v8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oSzJDGiR2rm1FpXpkWmO9d_CQ27FyQkxJ7OHxJFnYWIfbnOzeGaaGuJcyZ2VkLv_G1WZcwDETer11BntFDlQVFboIPrRBRZ7GnXny5aUDbrjhsfa6FBMT41VLmN-dVk1tNzDwe1G0ntuWzT33cODElr5dPpeI2Pjaed074wn5sCp7BGuTb817caMGHiRtxC_ncfble-vv6FXEkKeB_EwKIjVgBvPvA2WPjcTOvPGGqnwOGOCV3MuV-QWNGZxKEdgLZBONRlAIPvwc8SnrRaVwrVyS8g4gbKPBzszRNy5fM-vpeLPJ-5pc6ZNbAbRS-D9ob1_aKrkWjPkyuobYTDI9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HcJI4BZ59ZOL-MITokRSi0EKNTxLFX3emVAxMkfPIZbYEDeE7SLYMB81x-v8GJVgb7QY4_zSI36g5i-vaI9bXjFPkUQw48ksKX1GhxTvUbisFfZeOdZBVuBaSVVNyMs4MWthfAOBrOEdLar_aqOZMDvZbexX5ojlc09MkJdYnHuL9zAupXWc-eyDxVi7BnV3lC5W5uNWBMoHOQOgLnf6gYzz9blY8XUe9ONzvzA6fq8S4R6_-7hOcBe1Qz5F-VSzgUxskMd9SZDUs5LCjjN6897abB-5GprfEDjUCZFfOZBlSYdK4I-q_goD_ACN1bcQjjSrdadSdByIbPjvmlwtYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JBtM1MWwEGLpA0wUqaL9D-vNDKVAUv0a3KygVIOM2OQBvT0_dNr3Dln5OHHf6IWMKwiJiKe3F2SSzGF6X4ASkXMQOCDQQQ1q13S76P7fbuYptxxwf2U5AzJoB_uCdpEPNdvaWky1T9Z6aOQwbgk4YPyA24F61IjumzoSyeSf64fdmoPQaoGx51LQ1sR7Rzc0BnyNlJA08IfT1PvGGMtl_V4WPQu2inNO9YO9NJUwMa8Ls7-q2A5vZ7q7pMgB7a2QP1hWYP1EP9aRd_7aEOf3mSWj4BNPxQoMqKMKOjzye2HRHASOaJpGntvO9AGtb3tyChpG-4_-B9CT0wHI5nBN1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DuKiM9ynp1kw3E0tIJx6yMK9Fl86o4lgI_nm1auLZWbVzds5vHE1LjZK3yYAyGTU9o1wy2wPL-97ZAMTxnDz3FW8ineP1ZmTLly6Qia8NmLl1uN7SOSjsq4utbkUsEvGIX8mZzv0pAw2HU2lWIULVU5-PRKjTP_q2KbQ1SO_AHm17ONaKKT9u_PfdgotIEuY2rY1hV3OU_opRB1LMgQX8XGk_95HSudFhkZwn-I2hFHqlj7SLwmvrSuwcsj1MMXZC-mijw99igLbJfQlGKSHVIcUjblfnN6wo_YW88KH9yXHsbRXWZzWIufWTWE64UxzPlwHiAQR0U0y-BqFGFqkag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FbjIsPZYeCpwMCx7OXDUnnIFhh3bFB_0OpyH1nN-xE8TjbUbZucahSE3Zv4sXvpzp9hH60FV0TzUhK4yhyI4w3MHXeorUFo6adOT8h8EebyqJ2Ew_EzzPbmZXW2Eyo2Eotx37Bdu49rd7zf2sSnqi-INYJRtSeBcnRZTtuKGn_t9YKO5l85OGBvccSpoV62C3oEKM7ESHS4HCZwMWwa2I4sIFHhiVnniwvtEYoTIlbYm3XFTx-ZtSlQAkwfxTftUma1ejdtqN7laE6cmK0EbmEMz1LRL2IItMSH9iS3h1cJriurtQDvr_9y-0N3iXCZAsMEQ7-RzlvTebPMdldPzng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pqYo5dpqkVqhEXYWSRFzGDcjko8asYbE6E1nZ4yfWBwDQfj37ym5TL3TV1B-Z3keTydypgBDIYp0asHecd5Ksy-J7cvElDAgGUiUE-JRfWE2YSvSYQTmUyITWslDAPPEm8cY6WUCO5KSV7yrWa7SnFqaK2wbZ8BZO_G8pALOgxBaRVKP5eXWnMrTSVW_ngAcIddk5X3KuiVHen2oj4nDZvxhv6IDwy6Z_qJepESd-WZI99PQovuVtxUNUX_iLgJj_usyzDvXe4XeTCLoKgfYrZNdYElUGKhooDGfX1kEU6uTUd82mUqwN2gdo3a3dgsDXWLlgJiKnY1hdftxrhruZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EeT3LqXdAjnyFURjOQor7nNOI5fGyjM93BeW4HI3Xa--Wl0SDXJd0onVjFnZEOsEFA0dAJTn_9PzOghnn_glk9yzWRixg2xZPSNtmO6wySWJ1FaKznzRzh1GJ1DxJWLk4prS66kXtJWcH-IXWb_clla4t5R-jlR-Psj2mjImdLQuIXK98ocVpOz66Cx1BO3N0aenEjkYLB_HiQ7VLWMyJt_4rbOvsfU3MrkJNcM4DRHvcO43uxJNoo-yMeDCiGzPV8BeytUqImkSesVKOcRvm7N5jNzxDtj4uusMKZYqi6yPa9TlerM-1XbSdXPSrZCxmIQOTLzXDKC0IPSbSad73A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NPiABCyezq6V0nvrECfbZeMCiKzDCxJGHQhhHoSz_50f8ftPmfy-SvOKZkM9r2zDEM6fY14QoP0eyKBsXN3rRRhWdABaviXx1AkIMMRq4DA_NiMFSHEB5dj62mCSI2-IhEwOKklFDKZztYPrbZ4gkeqy5u-vYa3BpxU6ptbGOVkPmaeqbkm10VTsPhVHwBzU-_52NJ78oLnBpCJGHueYItpnihiOLnYZCvRnqYl7WYhQ3fONAbc9BxFPQyO2gBaVce_Jw--Wy_BA4Pp_xMbn_EYa03SIM3NMNOpcCcdjMgafAM3P4-RTE9R36hcDoQXLRVy0ccmCrsXspz-KFmJfzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pTJ_jKIetvxL4LCHbnZUjFyz3K3aDPMY9g--zqffZw57SG4zc1LKPeudAzUa9O_SzsTaHZ0agIXc9MBmhNZepRIFKgWMmClS1dXzQy8HQaqm1-yWUZo0X0Mr72HY2HyZ121CsObwgmlXC-UEEaBDwnVjWG5PZaiwIlIy_6qbxHjw48leAAs1mqR2mTVWjP4tnSGEjVzhKXbleH_cwFILhrWzNEf8bBOc1GuxHeZN2UwkyUMrNa8_LS_90US1yMgSMG3nwlRpDbF0XX_4H58Efzo85iCjAwALTUrj_9MDtb17GeHupFLLLQEdFxztPmFkN7hlRBnffy-VqxlBv0ET6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FIFUx9hyj2wqEaXKQh-TMM9w7DvWyc6igeo2deFlFHp7tJMDDKNR-Dq8SbBuzFE5pHo1Z4WXYYC49LqL6IhIGCmKYHMlgMXUn94CtdROmWymEPvfcNdQa-egACBFD8XQe50TIg_TX5793DjAOs4cBJFv0b_nMmfbr6IN8ePA13u5ZszTER7t6-HuaKDcOaCc28iCqNITAughTQbFrZLNAv7Oznm9uPLkh9VoIYl8Yr6awCsv0MEY8dsU_HbesUYn9x5U9hgXAp2DUT8O-EDJ4VVtrdsgtTr8Kxui2IiAWxcxM31CGaQC_ILIN7lMB8fXVqAv9hJ_IM1ikwQCuuXaEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UiwVTSodt41JEUpGzt-MW54zyZdUEj6EYxedQU6k6pfdu9LqKKui2Dc6ifX6X5y_Wl1rQiT0U5aJBnvXMwKdu7PFkSmEdJVKXYteYLBp4KHRsNWrL31Dv59ivGPtReTflgkw27Rd0iAJzED66gTa2FfO-Vht-4p6FK8y2SMKt3wzUvCoggAHVPLSOXsBwq-eiBl-jIBUAq-MeQbNX_CLXp6ls4ehNlVjSg9B1QEyN6P5Kn7zs8sKLISzS2AdSSBUsEvnoELTdiRlZLEEDAq8VqOzoQC_GoUZ9aMvo92XSfFoEJP9vSrBI6aQiV5-EPDi8OoSvX7aIVGeX3-NjbhzWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/je7CpPavDs829a2bMbwdRaURx8nhWaZ55cVj3A8820p9E2l_542bVTqT3FtyWJmKWtRIeBTd_dNTYZGd3mMNgJf3_eW7yQMWEBbT5j-dKiPFvLT3CDT13ApWkB_rve3yuFA6XBldfckXst8MBic0mjIrV1eqM-j_ZQzEWlwz4rKEZRahS_dYS4k5RBp1JBeuj1ausbLDyalmrRMVhjKh0fi592Hqh_cBFpAuXMd0kmfDReVmMXazAGcRp-kRO85b-IgCP4VfxriiszQXDkGloszhDOSMqlJjWTK8z2WIdyqfx6r7MZ2pHtIJCyfUw2sVmbhV7sDYmGK9Dub5m5QLUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bByx535SXUz4UUe5eBKc9kMbVzpAbucxrh3xmnx-3dTd4LIAYg0-VFPZ9qqhF9cihXqrrjs_FzKU8QzvE8bdpSG9L-qR7LufB0QVhIJ2to8ctlxmm-kKFbtbIM04jrB34O0Drqm0jjLFLU-tlbKQ26TjQR_ysYl-tLr6auOdLsRu2YBKyQ4uWL_3AbofCt0kP3FTwhvCF8MzWY3TK-8gauAuVFbuhjJCRUf7P6JvEu2EK94oJwP2tcA_vT93PDcjB3R9qgVRJ7eCv-LdfUSuJw7sbAgwfp4lHK4OsIl_PWFQQViotIyS0JRwwdLcrjua0_yGCuadQWDbFys4k1z59Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WWDZzka-Q_cdaOfbG2OvkECe1E5iZiDQ0_UNDxYFax3jUqW2_xexMxqDXSdjWu1wrbxTILGfdFVhZ13gCqVwdnzULTl60s9NfER-R2lCFcT0QzkSIRR0MacwYVblEgbJkIwvh90qrCpG03e8g1FPHM5n1Mh_Nv30JF8dvZKrKA9vhp7aTJ9bQNgw9dWKVP52A_TTFxHIo0AGAYjvyS7K1xnOI2uWPSwmXlJyIyJFeY6UWb3FIQ0ehqVI93eb3mPYZL6yV3o4Wdz6p8CwHvM_Q8Fz-3aYpAaU0M8uL8gvHixyU_aJGP1ghiOURXymTEhDYNPrOeKgdF0sapNuOL44bA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PoV_HGo3Hz7MypPCQfbhyHe3OUGmzHf464v27LlpJhFzgTLh-eeH0LETW8iTENHaT7ACZuK3gZVWAj_d_Z_4jizwwenX8T_DaZajS-gOXN1LB2R_8HUMkVTmnoQrrZ4E35KTkIewlTR3z1NzOCLzIMuJUKIGzv_GdORct4sJMFYi0LEvqAd8mWHuoQSkoFyII-lrxhocmqV47DjfNaOllS0Dtzg0oCh7skNhjKFFgMv_r-ghjlHkQif3WQUMNYy_f8u78ck0xST4BrAhFCd7GT56C7nlSiF7dvffFYy2Wg8YwBA-Ku9fQDgjADItkhrge9kLeIEIvNk1NVU_2SyIqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zff2GY7kAhmwpGY0oN8p0mWSlKnMSTPCR7_qS3XhuXIVHuqJcfZbIj1WFr5XLZ7EKLgv9kyXa0aOVjDvcNkn5_jGIetmt41N3t6EhCedLCmWvEUcAU9H5s00hU-hr2Ws73fAOWeGqXMOYUvga3_ztf7R8R4QvhlZgzHv7s54kPv255zWWYw1xaaE_TcFEiz8hF8mC3Z1BhMw1SNeZj_ab88C_LeY-g-akegpQtUtcuueGEPNGGvwi6ckQXd_mlaVAv72H6vLDFNy8ZBb4IdHmNI-YCTYeWtZr5srVwy7oAHtHN6ZLLmuEEzgSh0KMsloiwVT54Q1sPTM15syLH7dpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T4oA2IXfHmQIQkOjgpPAjQ7bGhPBBun9JYmFAFrAgu-IedDP_jHFyi_LfzMWvQdOPAezgLkgg6uQXY7PvfJJj4jRTzTGX3qzr8oBviZaAZJ0bG1INTaXSa7wpztitYFh4KVHSoJPXp1W_QE9pyN58QuOkAPYjPJdzaZFwFbBICyEcAZTh--T3RR3TndcgYYFD1e5nnRq0y0bolMzvk0VsQTV1DJW1bhTfbCVcFJUvTMTQBHpTB8w-r-Db23bZlzsyz3If45Nd9_YGyr6Tcy-FQUU9G6au83dIotElZS_v1TIpUqX4VvyeXIo_6U7Dx-rZ99a726t-9qvVhRIuiaW9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DO-JGn7Wjzv_42eew_aE02LsBUaNrkkTTdQOzYXOa8NucEtXvBfR6av9iHlDew_tw0USZoI5n8ATSyz4BpzLD8-tUZNoPRdCGdvIQSt1Al0eepj5E0mBg-_Dz-MKxU4pXS6IOJFiG8t85AarAsNewjUHuyCPSqSwOnQ_ZiJtURTnH_ClZSfLozqYBJxJAb0INTKzLkGuZMCoSRCj43W8y1wVyUxcdmSIZAqXrzd5EFgalPLWhbs1BkTYfaQefWNqX8kiYsjsUrv2W47WfFduVqCERtb8K1o6znI40ibVkxth_ObYO_LQ82dKtPQjvDM18zIxinsbCNoBl4wJ74BS3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AUiPhxmKqTgx0C0-JKPUDhThYtsc-t5X9mKVixo6CDJHKM3FqS58DKyMaBQ_Vk2J9bqeKNU-erMN-YqB00nZdDGfgolkemaaHCfp_-G8KXtd4MO4M0_yzEjjIAom0EapvsjDqvy_fRUWCR9sYDkUumohZBrt-CR0s82nAjd81F3iNmMBvoVX4ajhRkzdvmOHELCcDNRGMd0qtLkeiiF1lT3ZBq29HO-rc5I54hK_J8PGQQMlLxzFIci0V8CKX0Kw2l-ujZjaa4jQMiqvlZwKQ9EI5oDtBsaUewzbqt2JLH-D9vppJhtrO9rUmJneV1OE5rbGZY1K3ihBW_57K31vqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/skVce3ZfQwxmWbHmxNx7_2vj2rVmUK-Toh7XM9-17YSc4cl5DfdvXKucHuzjiXKMbx_HtBS693K1fUvdcuD0c8NwxMdCiBchkc_v5K-tUYNQQDODjHcskInlxj6Wdq6qKji0nvUm9LCw-NOBDVcHovZenRou86-vz5Jno9-Z4JSKF68S6S2N_H-j3b85kj4-lyCakGiwsgZYqwraIR0EzmCrlC1ilQ1CwwxR0BliBsrCxCkhJE3VDlWUSYvQnVavCUpF8w68__k0R6RsCXnvPRcDMfgU3VLZH1DEPZBjLrQSXI9qye775R5rtFxbvagZsLQj8_JAxHqOVcacd2Op5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Iz9XoygfWp0jPIamEpZNC4lMCmX9W0VnL8cmS3zOy3TsUpXofxYPhJTCyWUaF0ho-mnnOaUSSZljsVRs4JHQtLAEeQ-idRNHH0uMNdGWWJIVR31kKClJWdVtV-ZmGYIVHoAiD5YjypKwm-_MMmPAXf_dyCrXBunuC_HM_EdZFNXhX-iNs2eECPeEPyg_kZH10iVgLpAgyxGaq2XhXOz1ErnaTiFUHfjqly_W-aIH3DlqBZSAysMkaCBx8W4G2AuL_J-ZzAXLBw2nsTd8Rydu7HaMJnclrHoPPG8KnPIHNpnxo7jlYsJ4a8GpZd2bN8RYi-cgYf3mnSCdP3nJRtcvHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gJ4T54GpywyUAijvm1jUuXDXByzgCsL0jC2tx1W390ejZAqpnJk0q7pjkZHviWPsvYzqWnBnxpSzZRyLz7FmCUgiCWOcQ51WmqPSnisIOmeAUCW0_Vz2LQ-0qfiFlKOeULlmJjqrK0jzhEJF9dwZ2kzmozxCVcfkgGmgb4oMq9Xl11GJYhGUddd1rlWuoLjzKqS5fCmcWYmjMlspOGj8yHMbALshDsUlZJcuWWJ6KDJ3yhQoelBzpXtKhFUXNgbGx_GozCVKWsrBVP46fmjSEc2xY1FaTcQ3l8wZUwyxfvdRUoshm9PE-ZZ9BkrMv5i8fCAli8ReFs14fz2tE3kMsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VmwsxrW-Z2GUEc0qnWlX0w740Sz8NUfMWH5ABYbo6IIWE26XVFRFysDs4V0GAWYTTTeoMbcP3WsnW4DIm8K7HwI0BnE1j1PC1whcMLUFAWRAeNlgsc5YUgmEH1rKyh8JUDXcdSWtGnNo4Nmmz0e0-NzKdjQ0liKtTKA9wfjwGrw5GUtlWOIG_aZXgD1Jmkt1liKHJd2oOwJPzlrMdX7L2d7IPBqr0y0vsAwO_aHRxxPvpJn7uuqpm8-aUrEGTDuBaTtA6Zs7LQ8UkpvBYS68imqVdgJVuMZheKCOpjX3wdOqd8d3ndmwnn6MebFSJgl7WM23uR8btaEsQ4Rcz1IQJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q94Q3PMpkQPRVV8c3lXOklNpfW340f55XfYILzV8gvbXSdBxdDI8xFO9u3atZW56yBxIrmkPSQNvFWyYKGbj7roaw9Kj9Lf8iBxT8DF1HH3W0eU7teMC4JBYAmWizVztZPY1zaeZ_U-19YaV3bC1_ZOrRgry8x74vJ9ybKOXdoWKElFLl_FlRuTGbXpCmzpFNZvGzz-T84qY75FoQp4tu3nRf1YYo3IXKJlcDxDwWgRZ6KENV-lfQeLJloKveX6hudjCSK1hAGORNErESLM6-1ZUpfGV0-nf796cbJy3B-PwoJHs4TmMqbi0DYmvpivJ7GhgHIrbFNLfCz9it5mXiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c5Ih-Voq3KYxBhsi16vXvjQCjLv8ObYKL2iQsl3q2jMsCdX3flGHe9dSRtCLBhjzOiC1snxvdPkRq6wcyilJYZJMkGLLcAog3IY6u_hmGXFFPp2QBjsSwluGCBGwXkH8cvsONSaG1D0vlDnfct9imJ7wfSpnnD7WnCWB-96K3RtFg13QaW4XqIy1NfUlc57uYDDvK28SWVVtc_M7KI8T8hsAG9q7GZ2EdXBAEVg0iv00V4HvsqL-DULZaq5Xi-ulnvaT67-pMf_ELx4_peEbWFvj4KZ9cGqdWXM6N_BYYTys9HWG6Me-Erqg3eUeL8HFuIT8AtrWXrQZRYn2WnEC_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ms0gzfOuHQwy-Ey0DlDXjYyIh4KrCc5isXBvdFTUWTn1rdTmB8sG4ejT0oiHTqHNvf8z13ypS5viI9Kl7H3XoJHxvYwN2qFK6nMefTeq7PCdlblPoM_cK6A34xG8ZcR42JTC8pFdFbW0q5DyhsVbEOl796q8QYh_TTseuGwzDEGFDuW-KuRyIR7IhC49Eoe8nwPuf1delxYYXdnj6TkTjdAbT93Todhe4h1nGek_elzKjWqwT5mxbtpVmwHOVyfdKPo4hNIvKhoERA9eEZgin6_0WizjxyptRHi6D0G3mPRtzZbkXQbq8_UXXlEfGJj2P0nOPn_nq0GmlBZw2bLcCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BbokUx66cPHcMUvl8nUkaq26rpvTzP9CFF1fQWptv24Hs_piuRJP-4_tJCBCRJQg6CVNSYf19DQzd49k33UM36OIIiCr-UFvld8v5OoCaNkGdBOd1JP4OBsATFztVhF6AsMoxHGNjFDKSnUWabNlbyCOqCfBYR2ILI9fiwaLtG7Osoo9SsrylJTQFTI1S_jyXzrlN9ElVYlZwMRFp-QXhl0KTR1qYPYpt0SgyaIU_ayqS83c3HuDLpSamwu9sjt5S1lzIhv8f-431HT_FYao6PiYfTY_7Yceeju7Dz2boXgAqlmBqIbBoaKh5whRGO7yQYd8jleDcEKxzAr0BVyciQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HeXranec7Oc8VNcIGpiJ4VkLhjyf6-I9RwR24QCajbA9zMzyzeN7cQeKUX9twU1qFQNlSKt68dTDhllqop0KsJhdnrgbpuMUuJEt4iI4VR05aR2jGqnU0lZNgBUAaZBRnft3oumhwAJfbpvZJ0Bd5Cf_6CAzS_8CjgWRoGHv5ib6W-hDeTGO8sVsBFx98IU7ORZbBZteRktqUD9fXhpgQlT3Fv0pPb4MBF1bgTVX3M_91NeyPagWcldklE-EG8OwHIYzq0UrLehUoJ3klRZiEqFI7JcGMX3sXfKmFie2a0-RSKB0glgFN3Eh12cBsv9l2dDo9C8i8UM02_aRG4UxEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RbFCm7hom4DBG0PwdaZQqFEFrYPadMcIq_Aq7CgokQ5ZD_8PtXXAn0qPP9UbotGpqU5oS8dXdG9D_olJAmmjQJWhKFr07VTbrl4BFyYbiF05MH_RQWA9Apc2UYNT0qFott20JAS50OAJRJKl7Hys_nkci7NRN4U8R7jjFK_bhHG3WQZINUh5yxYXRhj3nWGtpWfw8Mgtx8zq-9l2ZnKd2ogV3xSKFegal2ZaAFOwitauroFAfLuZqcpI0HOMISLFKwUP79kM6BxRB34IHxleeztjOCoyAU7pqhumATTqNvIsADfyu07x3X7aeBqf2Jhc9EFt08v8QyE0LTdmMDFwDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MVQqqKRRzDitTzi1z7NpOv56KBMxhYHgXGQ5Qm6F5vAndI0fKTDDklNXpvOTs6RzMKLHo_qR9GAkjWaCvLcEnrZIEdQp2pJSCS9iLAlExSz5j9BZ0BVzkdzxQkNMl2pzxBN551tPfMOyIp5JY7teyUrtPh9Frk75iayRo1LbLtcPZegI6lQgN9AuNQJVUC4lGMNnVayPTvxKulIjSRlL0MG9Cjn3oSEi9QS5pzjM8A0TPTpxmh4mdh03xcye8TCksY-IAb-6oTwLiz4tzzHU-5L8KM7HVhhiOumrfiLKqXoVnsrckWS4eHV3PqP39f71lJmlxRfqXmK1LuBm0VQ_nQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cBhP6WoNAdj5bT5crBRE7UT-2KXo20qUq5l5czyp1ChJue71SyWqXFLRmXP_N_X0JlYRuhHra8TBZblG1Jjk6FCB-gGDhUJeNLjM8AO4VzJjJLomg6WR5nIFA4x_Khb8XOf8pM5wixU6GnnpnLgICIxVBLxUI4peH-V2DCDcqwrkM-NXIi8AMe84xFTFEbksnY2q8K2ozYHYrkruHXO80ga1IOV8Z2WZgGum4uH0EzhC04OR2dRBbDxxk6stc9M3anskehyUhcG_CM9bq9xc_-yvgq8C2MuYPGl3qsbVVRQpTGrlGw2BY31OXZQz3-mxPJD_ApYFyJ6Icbk9Q-Hwag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AfyNtEPxzmFX2tMgVwaV4m-ZJVXQVqWcIHfk_ZE8oAbQG1vVBWvlGlmsEnEbWAmKBNVvQxRU2yr1XWDUVZFO0RSWn_vxDDjXznDp8J4C2g0H4LBwZMXG5nbKWCkf0-JEH-RzQPMmFAyAWf3L_Kjx-E3g1JFW8P6A2a9g91wMhkaPyMYGisuOiw5JaBTcZCjAzsbqUmJcx0wPEQ_ThvDYLW0h6OzfOvGZbQ9B7AVFUMqM54tDfkid3bEeoszS5vMhu____W_cyjMyQaWkMvfd85Fc8pivCB8BCUYDbhql1tP2gmmNHLhue3NGff6kaa47Q6cgoc1pzm32kjIa3KCKqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e9HEO1r9cHENmX8LeY1wLv6BsArnnZ19NEFkQeQLeUajs2P2HMpAC3hRnzhdMNUMZ1kpqdKhqMdVWeKctB3r5IJxQg08lPJUvQ6jCklCh5Cq9HO0V3UVv8zGuGGwZ_sd370oD9N0VwmVxHx_p7rmHL3PBSrRNgU93HjsbslK0Pm-7cd84nJEIWz718RqEPd2-_KCdSYoUstAtCHtdq2QvZN3UPi65PcDehs8C-EPzVx7InldfHBHrekSNM5ZuP2otD5UEFqCItuX4so6aBBBhV0i23_V89pcZVNpUT078RVOWkvmzKcSyVTJ19LU02a9nWU8vSZY2q-bRDr0wvGScg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 63K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cZ6aS_mU1edhQ5qG4zD2Y0rzqY-D7NnO8xPQkfPZvhyWOqcKHnA_ytwTzHgewRruMVoAEJPW-b-lhad3wSbaT8a-Bz0M1ArkLuZResDjlL30rLI37jC3MqnnWm3aLu5OOY1P89ZMAWvA0L9zdQ-zNp8aXM7VXhbUVFf3Wj-rOx7H5P48x6FgMNvoDgQseEvRkTDZhHty8zWZE6C-N16-Pi5GsuuUQyTFeip-s9Y2rwvz2VLRASsvutHWKj_DuqV8NmCDiNlsBBS7-VFFnZ_whSGT_5VUGYYF-JkmC-8Mkk1qif7ATGnweKF6FUXJvj-FH1eT_KYyhAboIBL0MQsJkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/feYxw7x7HlSyn2HGy8V-zJYxxs4IQkS14yeMto3zzGki9Nb4smJ-0JisPPrzJQjsEDXWFNKeyrxi1jsNYWr02lmTcR4jUFlBY4hanRKMdYNbTHEK7HelD5KljMe3pHM6Hp3SNq7pNyRrSOCF50nLpNdmx5GM87hYE-dOSLvvkfUr1E6fe8htdix7GWuzg4v0w0Kl1J04p0AuhFUefcto9iXgWG0aoRaS3A1w6BEv0-VTT5QdxpE2hoyeI7RCKBhQKLpnDaILhk4eydwzc5IrdJdqFybqLP3-Fh2DiVuHVDEDozVbp582yiTutcbaMXlZLV3YZtM5LiXbLJUHh54U4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vvGlvNZBk-hl6T8ZKJsrBTug91xOAGIjLIHZZsT_anFUPhwVHuGEHt5nEA_YcmGmpscP-XUhBbEnMU48-wwn_9IInSNUSr3dLGEXJmIfH_m2pcT6f7s-BSmwXl6UHjWG3YFEfuDFCMmmOdv4CY_kacjqn2Bpzf7RGfn1exXYcYyeeXu5kbplBnCfbgkdNKqcsu1JA1hUTWQdf0yyv1KYt6uEnocQ965Enth-8_q96AKJ9_26TqbqeBD1Gymf_tueRgEHFWbyC1qlOAZy3wKYUxICzPNxxLE7kQNt0udp7B7E1Bzgmd1rv08y7QjrVY1JO8zWWyx-rH8A2NFlql79MQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GB4wce6GCjPHG-VKiyneAsxarjBsCIOImNppPPM3homm3zbbiDfQjRnoncoHbzx1eLRfLh2ew0EvMbKlHYJgQNg3RyKjmAzzVRc0Dv2ippyZ_ME3k9Wo2h6E-4mXEx73Q3Un3m0MpapP9_uNQ7bDiaPIbqrhUUmKhsW39szrijpFDwvVQN1BiK62WIeokz8aib7vjUPbiP-fRJlFTHrV016LYMf0XJ9iL4Yhqrhf5OYJnTNbepiiMdlr4qc_YLzQfoCPK2-jeVzIqh15uozr2RrNu7MWskScCgcyYOyDolG2Z6yqITWgIsfoetp244zly4C8ZaHKH9t7BJaAEMSuBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TI6tqSpnS6ASA-vTTTpLmPhu8Axd3USCeUCZ1lKrfsWP0Fvcx3m-QtN0J7-vL8FU0n2i870pVXZx-aTzWsVaqkdR64VDMYfyZ3Y7jtzVHrCRiDfUAtJchezLa1mCPTEWWWHHC06ZCCs8SV2Zd9-3P0JLqXnVWRl9K02h24oesp0BSlqOQ0ZWRf0HRA_BgUhqwrozxRsT7r88GznaT9zR0iFr5ulKR_e2-eJD4sDgiV0xHFvf0rrR2uwOXYndQSBEeepQ-qpwlVT_XymoeynHp4vRqh7KFhwnvoorgRnDTptoYpLoRjNKg6pB9GuQqUWAMmCRM9sqoPGGuCbMezB7jQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mhmYQ4fpeAnpzw4Ue5kN3xu0K_0FghOk7taBaR7FyUa-tPe29QW60xf-iuYlPQdDae3Fzfduel1r9KGJsRdZ0NP9zmxTo1pFIxKZNWENaY_d21BLo14JppOr1vmagROITKLmqIjBIe8086JFBhPWCbG9fWoGErhiKyEYVrPwDbb_eMh-NOvM9Qb13amJ41U5f-3QSQTAgMeJGdJ6BkRHU1vKmDO42B963zULuHQrppUO7g5x_HXwWHzBYUeP0M1Cydm_mfqmjcVK6O3_ky62jOLx2gA3P33l72byaqs9I1p_3imf4VsBCF4gKfo_HgtMSaTDmxbQw33eLb0ggXtHOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/THynLvmA1GoOlFCbwMq-2GIZZKVdnSpjNRVp0NW2LYWSCVJuafhlFhrkcaHMfG3IGd2dPWq8xrTDwx-C9pZC_gmZnzsQN-X393_TMhvzQbObblYr8zLfGARSEhSkPneFjNYfrzLeLAflgSMjXOf4rvv7VlQWJN7wV--Mtj0hSxL8vLrsHCBPBK43XiY7i3XwPagGFjvt2JMIhqW1gVHt3kYHOVJb3Q1XoaA5LT7eQFfwI6XJkXZWE44g8afO1UPtUh8kXpw-X_izeLmSTda8XB887kxHHoeAkw53IMsQ-TXhui1fJoKjImSXzhfIBfpN0wAhKiS4lqk-F8VQv4XO5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fjQIJAhz4yl3TXUyWj4FLKQxdI5WGvxw0jBzS7wC31kTTQcb7zm4vi05NeQaL3Tq7_sJJiOKh9KA8-7ZaRU-xxmDZE1LAun-w7q_EoWsyjlgr_QZ9AYnyzWByT883_BHLYDoG5EYMWTuatLviC9v5nzD3KuAbqSTotLbTKkHWSVhmnwf0oiLErMjrzTkDIT5GpJJRqWOOR4TP_vADvjsp2XQxPkZwJBz_LgRM0SEqhkJq_rYntmpSxdF0tkvH_oC_MIkFvo4BkAooJWynNQ4XjkxS9Dnncvkah-WVWFgEdO0oGobgdlsPlFeGalsJgtDvhWOWRx7U6-mVEliDxNY5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hnOUilEjrbZKXoO4jES9m81k9u7u5yAZMPEyhCeWP_uQMk_fOkPdOoUdHEdNMgoxJcV2vI6YVPD90tK3B1CMP6kTurnyJtoZjgx1ksw6u_Wa1tceILDCQv7mZmwtbqF1udJJ_V7tDruxlr6HOg8dgADBelZ1ggr-1biD951vG4bbk5RG9eG4S6yGBw1MPxMWo8IcyTaJWJIIG8Whg_6pQkMzFN6LkXWsZDPu3A9ZHah6YmSmHxJ1fCVGPCkWLTG-mqeuXTNvzcrZwoGWEv97ca4Qkc5SXeL6fWbZCMpOeYy3i13wRXTfvVdhEuE_FR1ova_XeygIX_JaAzkEckc7XA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZWnhlCMPMZxdnnZTiixzMB0E1VKuB-xLc2ZqdNwvJ28H1ooywWiB-oPaVt_YyCi7u-DpmCsvg_7klaqCjP7M_rmaUsvjFpRjAqAU7NeBhlUD6rXbAbg19HEVj9GEZmObWsxzs8wTPl8yWTru_PgKksiW-fBqVZCrlc3g2HI5QtylsDyhppm6AEH0HLfHg6N8FMXVqfMiDlhuId2OPBvZ60LU1dLBvOZi7euCZCPlBMQmpfTxGI90QXM3QedhMEzDjxuV25-p_XwJKnYHBxfoH7LopDYuA7TwqchWQT965LWf7yO1MvVu4g5FojSm-S29CnbEAd9y01Z6dHb4md7fPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sXCnD-Rz6SPBz6l__g1Awwb8r03pzi9LVhlEI7FxWrQd7jFQedoEDMwp4Hcf80STPjQsy3zCUTwLRIP6t1f_orzyx77KCQ2PsGxncnlhNl5C1ARG9XhNHnl7ebJXIBnQoXRoaIU8wDjqEHbArcd3VMYMnPeUMC6EhXHdpjbdKXeBEvPVdeZggSLXfNUO7qUlzsBsQW2wsSNCctU3rX8o1z_Uj_nt7t82cKOz_oQavA1TjjczT4u6lggn-s0P_1wQsO47MBDMBFsjFKn15yymXCYcClEquyKVET-Hm3RGmUJ-eAl88w6-PznL5buKAKQqbYFx4_4ySMdVK5WUu0VFrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z0QxRd2i2NDRsyc4_QoVn5u6hqgB9yGwAgVLu5_5HQEWkPnqHwThhf8CP-alEEBjXtv73L2CA-8fW1sIN7NqmxROCoSEIogqPnMI1Gnn-VnGSKBOqHttNV_XuY4YmMHhpyakec7Tcm62fJTF0EtT_HCKIGhLh3kjDO7KppXPxZ3B1B0fKcxkk1UXtEsY9MKRwBuYTJBoF_Zh7aQL1pBQKEJpf3Tws7h-PdUyLS2JwC9dv59HWxx1uZRxEOHN7PLd-7wymfmgGrkecxGlLQPNOB64a3SZhgGcx5BhldMKlYcdWfKlwBtkWbTnMsJ4kzD9GEhnyVbK5K0slMxPbSsf9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t4I6wq5MoQ82kWcbJOAdeJ7hmZyCMK9M_RSoqxVECmxG1HynRKE-CWU0Mo5ikU7QDKCJFp2FphpDyUTDHDwzdRoGMnxqvmku8_ysNbUteCpQH4HOw5TQac9uW5QLUtHgeO4HpA3FLlfibEdyAflaDmHpOCFunw6E_SMkoox1Bv4v1PZ7X6vJwPQiNH-kvb_kxwp0gZktFWg1dcpRkFWY9FBW4dPophGgVDFFthQc92jl1Zt8AgzuYkzAcCUAaXjsUew69kdKPeimgw0ASjO_gL9cDlzZBRTLpM-lc_aMZyh_bjFd0WKaIb_jDa_ir1w0zH4SyBctkEGjDz5sxNqIRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sc-W6bMOmBXg4jKlsM7gDBcffGSv6ojSDtYqD0p5n3o8aMNdT7zaqBwOMvWalS7HkyOq4E-H7EIAJsjMnp8xLDdH9pO9Bb4vboDS23roIubtB-NV2sUhxhFWjcl0J13LLfy2K7iqjti2Szm-G-b7XHKrpknLk_QfqIiEdmlW7N_9chqmZBl0U9hKnd2tEVRR71QQEXb9KQwHmmrEV1GbsvU3E-vwBB-_z7sgQ5tYxUCHkIXvjN-E_pFisDJwkN_kcFT6wDgGQFRM8kz35Pm2H_zhW7FyYlhPba3EPShtmbY2AMeQHMxSbJfpXVoUJPBRLWNCn6p7H14uXJ9KS4IcDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bVf18U3pF8Qv72feUKjLXgCZ83Tc5x0fIC46K0rwA77QjNgZID03vGux3-qcCAMNTC0SKFltk1jXP9pwoVcrJU2VhKgqXgi_Z64HmuY7MrUt1K8WHbZ4WnpDuohrV2ZiFiuWxFestcyXiTcUQJnjOoSuWsp1TmpDM0Bc13sDb60vqe1KZSeoAk7ri_UQN5Osh3eAIhbRnxY-8gkMwsmY1My3-lys0Yhy-o7r1nTrCGiKkovU5Akj5B1FCLgYKZNof7dUoYHz8dUCA1qzUmKy7CbuQ7yjSoyXbbG4OAWzLbI9bPi59ssUHS89J_7wRwkFASK_CKTeGYM4eQefXl_99Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JWS2dymEJK1wcrYSAJxN0gHmf_1cXXgIBpDpJsASdNTBSxU-gewuCe1-6ZRhBZMw1O9jOtzJlWt3kKomOYyvCtEWKAB5X9I26GSdBWF-yzeWQOHtkFuWwNeqlLBJkazgej1OPElVAXj_9T2gvYNJdWReJNI7RDdG8Pr99ttNzZdYlIZd0vYjM7NwHb-5wbe78ERDMlPam2fO3WWf9-dNJ-q3j-2aaJL_l0MGNKvF3qQN4bwYX6CsVt2qIOQCHz-NTko4WHQNG82mjcY7iiCSZIHZvcc5MkmsOshwQZ9fa8433Hq8rdOMsN1p2MufUEZPacL9Z_Rr8IoRPwRVEOhM7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rcnYbyip3hsS_ZR5z5WSFkJ65_7TyXusZT20KHxzzRy8BqnwaXedwveUM9KMXFrWlQnnKs4MJhi1U5OcvFl2gujSMSUeUkMqEjmg6IUT3lr84SjmMtpqG7WkPmwBwMVsVuJCJs7eGkd_IruLOriYQG-e6_Sf5U-3v5k-JZFPPwyu95X8tjoVMPBWpShYAaq6bQ7p6OVKnmn9j9Z7fg0Gl0GAwNCEmP_PEnzHKJse_F2unyhZXrwExZWY2SkUTwNyduRQq6I12ckPb-N-5AE9CoByyU9-scTiH4NXdl_RJbaXlOo9yN8xVPAHOcCFrhk_1Fepyt3VLM1Tb_ERBZvXVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pLdEw_VS9PEdpO0p2itPtLZycb9OIDYqlC0JCN0g8Yseji0zzEPVGGxADtEsBQi9LppROibtl2rprsFP_NPJcjpde5zvRbimGIlzWByU8yHLQAd0w2YapotMj5XVQQIRruRoM2buM2wW-k90kVlsbo7I8cMsNBVY1GT05DYfLG52_XnmcyTi59jO3Dt9hMcUgCQgs4SXY-qMEPSe0cRQiLqacR5frOHfIgjYNXHWzShSy531Grcn-tknhe9oWvFP-je7A7qeD0mBn5GtKMYKpsJjFQAI_cmv0-cyJ6MntRH8gzX4rETtKPLSqQblPX3SPqRgsoO-FCgSCnqJw2fsYw.jpg" alt="photo" loading="lazy"/></div>
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

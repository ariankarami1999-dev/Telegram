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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 23:40:59</div>
<hr>

<div class="tg-post" id="msg-2662">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p_RWCuj9obwv7y0DelOvgdZwq1o6-vapoHbd4VIgmFS9iAXIAdDtCVoB9Hbyp1rS1_dq-QoxwyZaEOl1yA_RXuVR923CjOcA58qp3yu7fsft2hRzRjlp5y4uRVoZ7-fsfd70e0e_1y9_t8ran1Lb0tj1q-b_IjJ-LpPP96gwNRhrA0woPbajlQxMfkBDF4ovD-enkXTEXR4G6LMlbNd5rq29OPJO4Pl8uFQVzVFu4nFhALelARcquxjANJ31BsUOBPPcjvgUgygF7pjEj3KCwXc2vpXS3Ht6T6UdE-vZcNc07eI1lWYSff24DUqqccBmzMKoWTdiPCwIzKiji-Q7Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل NoRoot VPN یه ابزار متن‌باز و رایگان برای راه‌اندازی کانفیگ VLESS/XHTTP روی هاست‌های اشتراکی معمولیه، که فقط با PHP کار می‌کنه و برای نصب و راه‌اندازی به دسترسی روت، SSH یا باز کردن پورت عمومی نیاز نداره.
این پنل از هسته واقعی ایکس‌ری استفاده می‌کنه و ترافیک رو از طریق یه اندپوینت PHP عبور میده تا حتی روی هاست‌های محدود هم بشه با هزینه کم کانفیگ VPN ساخت و مدیریت کرد. اگرچه باید سراغ هاست خارج از ایران برین، اما این روش به معنای ناشناس‌بودن یا تضمین امنیت و حریم خصوصی نیست؛ پس بهتره برای مصارف شخصی و محدود ازش استفاده کنین و مراقب اطلاعات هویتی، آی‌پی و ردپاهایی باشین که ممکنه از طریق هاست یا سرویس‌دهنده قابل شناسایی باشن.
👉
github.com/mr-r0ot/NoRootVpn-Panel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/ircfspace/2662" target="_blank">📅 15:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2660">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ct7aH8l1RBNWDFAIvTDka-SH-vj48GVrYx9wYqJiwjPWpPB3jS5uGBcpk05qD5rQiKPfL0gjrHydXtq72GmkJs6bBDQOuxT4m2XX5UoPI0nnj4t6lOD8pfQYm9mGDuKHXuYAeH_zpj1WVKa1V34WqgGR3zdRexLfgOlaz9E3hFwC0d2qZlmOI7hODTdqy7eRdgKKpXwP71eqfnHuWXV5bEYforUeHRxFylrFlsHOKOM_U0RrIZGh6E2Z0hJqYlMgZ4VP6MM4nKFtn9x7Jg3f8lnSiJCqkrKS1CwbzL6TwT4muz66x6CofcCBRFWZBE_kENPOHJmD931MPfJojKOxrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس‌کوچه در مورد Jet VPN که بیش از یک میلیون بار از گوگل‌پلی دانلود شده، گفته معماری این فیلترشکن دارای آسیب‌پذیری‌های امنیتی، با شدت بالاست!
این گروه قبلا در مورد خطرات استفاده از JumpJump هم به دفعات هشدار داده بود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/ircfspace/2660" target="_blank">📅 15:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2659">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a2kIG8vZrAEiX0rntnzka_W8uFRZTjhFNRD4rKm97IiqLdW76_egguaTs7xoasfvN7uC5gm4sujjz50JxGZyJoxbDKt6xjVEnyw7xfsJwAhEMoYGEok78xZzTfTL3hv1pVXZ0QtGojnOKt1syEr4GWP4gIytFVG6OhgVdl4PXyxtajCCldkoBw55Sq8zZ8gXaJzfjXT0zPX8M8TJ3SpYC23OIQjRXqaPW63L-sWrIznEpoQxhYypbaTeZJMr5j8Lz1JUhU6e3hH11QcGkJD37GEBoAUajHzuOZXvC40UDW8hXbEvS5siVbUeuHUjNXD_pMRts2ZYF7WuqmhwYIurDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاونت توسعه بازرگانی وزارت صمت در نامه‌ای به پلتفرم‌های خرید و فروش آنلاین طلا، از آنها خواست اطلاعات کاربران و میزان طلای تعهدشده به کاربران را به‌صورت کامل و صحیح، در قالب لوح فشرده (CD) به این وزارتخانه ارسال کنند.
در شرایطی که شرکت‌ها برای حفاظت از داده‌های کاربران و زیرساخت‌های خود هزینه می‌کنند، مشخص نیست اطلاعات کاربران پس از انتقال روی CD چگونه محافظت خواهد شد؟ /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/ircfspace/2659" target="_blank">📅 14:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2658">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/ircfspace/2658" target="_blank">📅 07:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2657">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fs28wpSKX0HJY8Iwoz_2oz0ej1Mhp5Om5DXgzmTXNsYZHn4KbHYA8biTeSAeHz8sX_K94JjrZGGseeqh7AIKxuXtr6BAOWqSwZJNWczVxngfWoATUy12Unh-O34Bd8yjtKeG42d4Pq3Rxq6iQ1kxdkSQ_ZDI88wMI85HauGHCtQl_nmHafwvhwjyuicKWjq6stfYGdJM0FQee12KGq5axtQcZpEuZ9z4ZTwhCExusKbvfOCrQR96xplMi-jLG3vHZmgnUuESLpfFqIAL9KnmBha_y1MMDq5OOfaVFywKIu04xliFSpaWZWUWk_wOWAJomo3CPUtakQrSPdNV377rog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/ircfspace/2657" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2656">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oMY6zo8Kz-rFzRXMygZlbGqpXeW0ToDJ49vAgOhV9HqNC9OXHYBMzMgPFTrGfG0zwXUhZakgR0CPI7kpYvd_tP2rMsGhXKgZoFm2fq_PRhqfxaT-jMT6tukERLIqQz4pGxPnyMZNbHcgOrDjhU583Xe-VAzTEXocaCnmz4XKwOEo3IwH0fzPtGFNn6rIprDe7n6vx2NNOTEiEfCU9iPLyxjfue_CFmkXKfxBJQYfEok1wadgHixBLiTUuMKX9vse4YLO1FPc11VdNEwq5chKJ88RgddSSTJiEplWljiXeh-izexOm6NNxakFAja1azf92wrvZchYRyyLHk5HK2zd9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس داده‌های رادار کلودفلر، از ۱۲ مهر یک ناهنجاری ترافیکی در ایران ثبت شده که همچنان ادامه داره. ترافیک اینترنت بعد از شروع این اختلال بطور محسوسی کاهش پیدا کرده و حوالی بامداد ۱۴ مهر به پایین‌ترین سطح خودش در این بازه رسیده، هرچند بعد از اون کمی بهبود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/ircfspace/2656" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2655">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GBvCGJHhYW56-ojKOeG1Co0ckJap8e1kam0tNUjBTQKEtLYh5jQ2SzJdtJgqeCmcncCO9aqW9h3lsrCbX8WMwB-J6ImthI-hgPvuv5KF60cAhPIISDxoEMSKWXw3Unl-g4OXHR3mGXV2eOVa6QQhguSPDzGLbBp_kkUIt1fUCSHPUfJJJSMvygpRMBEI9-cZOzCsYHDe4IEVuz2m8apoHjRIAl_gQ-FJglSZwxTEqKToUdWqmV-9rjyla4qV2Q7Dxddfap6fbpU4_3HQyQqYQDIb7uZBuNQmCPxIDwZMmGxR7rwoieSE7b57ihwO-mqb9TlsDqoRuqpOTMtN7USvIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه جمهوری اسلامی در واکنش به سرکوب اعتراض‌های دانش‌آموزی در فرانسه، سفیر اون کشور در تهران رو احضار کرده!
با در نظر گرفتن کشتار ده‌ها هزار نفر معترض دی‌ماه و ۸۸ روز قطع سراسری اینترنت در ایران، ممکنه فکر کنین طنز باشه، ولی منبع خبر تسنیم بود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/ircfspace/2655" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2654">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mNRjqBpc7UjaqrO2r2wZi1LtxogwlMD8lk0gLzknSGIU-J-8RVXtGH2RWt6Abm994C0thHK-cjnyagZ5K8HF-Aa1kd6sv23-ZgpZGE0SY_X515i6MFzeH7QfwF_wiUY7AymzX8LnGHokz_ysrVBdLmm8Dwy9yJVVFVfkZ_-dPeoRLgLodtdQruNrc77pER4Hi5ru04iPDRHRk8LeS7WiU3PbZ5FdM0ITjNjCeprDB0xddb79s6ml7c3Ssq1g150hicctgR95Pj39qMML1CgOMmOv-tt_Zr1FlSlqOKPrNMyVF9-dVtGpPQwJozzEIdNt4CDdIruWvLAN08DGWhx_VA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/ircfspace/2654" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2653">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/ircfspace/2653" target="_blank">📅 19:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2652">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l46lvLiInYyHteWSRq4MTpZoJzoWtUJZRFpuWM9xCFlDQHLHsbTxPlqNfcR2qERv4W9RO5i9T0MtoRaXOOwfSXclwZ9XtWl6qp4y6Qw5Y_Rf2T7UZ_zMR4WntWiYp84aCXW3MrxpYOTjqSFn2ViNVE4aOXUajvPKEPhvzVvgWm8wLuUS2h6UGhhMFjgDvTDu_XyG_fncC61wE0gHaitqBlJTzzM95FFIj7pyxGhEMYSSm7P8-TfVvzUj9J-3yFzTrqfNJT-akt8B6xeB21RAIJry9sXBrWkWc1z9FxMy6ek5lNmXu0bXwNp_thGr0aAjJCIyQ-Arife3twZHyl_8QQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2651">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cel2lUYfQXhNLgBN6NYwhtSznJvSaLEcL2lOKREbdG2QY2InvL95Sa23LD9ld9JeiXhq6DLnuH6h_hRPO5EdHJqoi0vJQSmWex0hAeofFKu-QTVb28ifE3_nGWQnIQPSOL5phqc0TOw7zeHL4kMUOKJRUjEf7t2FkveOKFTTIWlds44CQa7jOde_RZ12PiXJ-HUQcGKUDWdK3YATrM0Nps4UkeeyaxeEvc2cW9Zhp67jdeSD7pX5S7Y8HFAaVZi77CmiH2HCAndr43L8UgCkuWwJpw6PK0yg-bPSdWuHtasElAP0CgXHboucBFo8-HrMGQicbXAdIIFfaYdFtyTvKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2650">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XIoGuxV1M5mRI4rkBMcLe7ktauCe6uXOjQ0moXC_iEch7RIgwJ5g7yS2J31iD6oBhimJvEfkSVbNzormnxG-P7T2sGkVlvmgxiGvzXmtofTsn8AsBePaWfHhAZK-5ZsTe7e-PK5LuGJ4REEPmW-pYsDFaqhOf--0TEFHEBimM8QEJs7aV3m8KzV7eP4n5f4WMD_8PBgw44t6hYLotFDwyFuu-DEdJqA9Pe_ISXSYwcejQq0Bkj_RsWxFUl4LGV7pt79VuArAMpqRpyMC31sTHEqgiMCWbJdMffLGAPsYiASbC-cN5ujV_P8tblXrGcxia_4itRpOFjTHpvwBND1QfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای "قطع اینترنت کل کشور فرانسه به‌دلیل اعتراضات دانش‌آموزی" فیک‌نیوزه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/ircfspace/2650" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2649">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YD6qDQcC4veOvblRJs_fGPCWql4wBQ0AQ4BcOnyYEbXxdFOKo-A_4gxnFakHgmXHMVnS_OZhbwEiQJYLw6fMQXZus8xb6Q_P67GkYyendMRcqCpeYah0tOCeWMP0gHDRykuqdzOnTAjBYkctk5UjwafuEsTEQUGXGqbjdxbxnx99b4hGtaOH7vM1LUUYhU5sKHOczlo78knLGYgJ8AuO5enF9VSb4HdcMqwJvfwmA4RQCWHcI6Q3QoJvA_lpIeAyfC7ZJC-rp0PcJy-aY0IcYneiL9f23vCU0aH-wON9pbfZ9NSwTG_x0-8Pj1Cu1V_ahu0Ll0lpAfnlhytlwIsoaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/ircfspace/2649" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2648">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vGsCa5uhoKbMylW2hjnzHwXXTsFB7QmA0i90sfDyo76TB8zViERR571icHoAzc--F-oZdRUL-NhB4IGHG8UCp_3qZwAnCqzYfJhoaLvXGwQAj3MehtsoCTXWxXcfaeuGHXfu_dPDohphfJjkHrXcmI6cazRR5o8uP1pJMCw7TT3KgMx8XR8FcN-nW_oAFbaI3lEh_VvB4ueQQmqqIl_pWQaPJdr6Hr8CxTHSLOCUflD4410YFCWaApxvn6YqBTVTxxsFdTetK4-eGrcgLxnZxig_1z4Z9gTT9S-GUujkf7zLSD4dHvSP_NXVJOzJGEnyMSQyHzc2apUJ3N6E0-LgNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا: هر سایتی که اقدام به اعلام قیمت‌های کاذب ارز کند، باید بداند که برخورد قضایی و پلیسی با آن به‌طور جدی انجام خواهد شد. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/ircfspace/2648" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2647">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YXlijyKbJ1zcJ3DBt4qcBX6S2McjAka2b7U8EbznAbFBS8PgIUXFOQpnbSFp9PXZaqybK3HIiN_h4djVaNHRKQ55OM5EF8aBKCzndEeA1OqEYwvfKFV8WdtNyPM4x13Hy39ZLYlYQFOWV4puVQwx-4Ay4pNC2PMz8fnTFfb3bvYo64E5HCg3F07zuYRIjppDCPfu98yWguFLtKc71B5By0pQGXb2l4RR44vdMwSSvOi3OaGYpJljtUEixhs2dYqL8eF9SKPW2MnX2YPL3qYjvgvtA0AuZER5iUr86p7jK_k9zOOQW950jJPtmOwtiOZ-5Ju9QrlYBPFDflLL0k3pdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/ircfspace/2647" target="_blank">📅 17:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2646">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BwkvSrHCn7x_QT9ENKPUL4TkP-fVxQ_mBLbxcvObYL-hhbFSQPfoOpjrp8xZUpi-jxmMwjpN6W8ifMlBCiT-cGe_ftEnc88jWRi0iK1GrnoLDpEPsmgLSfFyzvnUKMDsL87WxBlp3KE2xgWO0vavp_eNgyvaSzCan4Ykqcf7bTTW9vgxU6sLUKaH0va1z2Wvd7wGeIVwW2fAGLcAX24J6_kpK7WRQ9y6sk3X6gZ7RBdOXXd6F_qV_-z1GwEWYojWv-eaaQoZlf76p2lFg_pla5zRKfAI9F4f4Ctdeh6cmFxrNUzfL7JQAb7wgSDz1Mnm8ETiu-w1GkHk2ZVXiuEgMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مرکز ملی فضای مجازی گفت: ایران برای اولین بار توانست با موفقیت پایانه‌های استارلینک را در جریانات دی‌ماه سال گذشته از کار بیندازد. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2645">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ILJJF2tZqe7MVW1jWanwmC2VdWzdCXxiY8it90TDxHgEQikkNg513TIcLHzv-CEHkuKjT5oVpoW7CbstYdVmpyXtQj9YdYANRFGHtLNOiMNbwySwf3aI2gQiUrSBGtc7BFRSs2VzgSPaDPdIeoqAG81G9g-WWmTaazKRaBFPSbjDrfhsOG7MUQaz70pwasgtb8thW7Fgp_h9n1O5TVEndfOkdi6xoO-ac_Ccsu1FfGXKjaQM4Z4Fyi_WS0BoLOazXBKsn8DAex_nku4bLAosLR7fzL36YkluIgvQ5p_OyEpz3nhAW6Z6_Md2WzF3l2V6yNCbcUSrqnp8PlM20tfj9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2644">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rQkuX8ATC0Gxh8Tmvr4EJ5gHqy--skTkQ5bLvwBTGMqQBTMGgqAZByMGN96ZN_L3CsB5omgWo5aLE4SR2hnOvL9mF3UKAojw6UevEuWAEXKuZgjItDKoz0_T5R7sZLgtHx4RUlNWBmlfe7QHIuxdJXDzIJCPw-ZVMkEhUzDlTKjqrgE2nd0tCHaEkacWBYrQ72Q4rhsjWkWbnatvnBQGcboxEQ_03PrgfOpJpeRZMOWhrUCTywEgI7fRGWhD6J31UtXZePP0rTXiwZG3V3Ch2W5KyzUY64b_rNOiCrM3g9juI3_1tI-t8_dPZjGEp7lg-uhCCvz8Pho2COHByqming.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2643">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fc_IISalUWcTbkOIWUdKEirYYUtKVLFXa-vHS01jt5YhgoPhf1PUNsxSux6lAF0l0jgU_jhXB5ppA_v-5PTffkjzFAQM2c5M04Y1YclvwBT7vsAVlOf5uiSGaEdksMH9t4fSoTrzM1yU8a3rMDyrFLlzMLtKDBxIKDZYuFqpoVwSTzm68hP6bfPjh7b9f6dv4V5Xr-yTMaBN2nwQ5sqyS9GuiN1MDfle1ddWN24Y8089v2kbVGNWxE8joO4lZCQtfB0T0sfIFVJvD5qDq0sdyq2mdAfWiyG8vbBSSbq7oh6EE1XCj_NoRNFAepEQwXIVZ3CpI0FziaLg-1XL6TIB8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2642">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fh5UMIlIJpeWX00Lmq-5IK117UtbQfYbZXNluiasxCb7y3gt_ugsEQ6BcdPzYZBZxkeC2AwbeUoYtfpHGJpQ2f8oq2eIuJoqmOczHheTH0VjqkLjE8VTZlvrK9Y211c9DsN0fhggzBR5aDUCoU9cyA23p45DoVIYvwZniapIPT_iYvV3BtDRn8q-MmocN7hMtEiVFoQNarqzhr6aMgs9XBAOKIMxo_z-u_ZKavYyCBKlijYFmAMwYBrRpCQ6zOH40wU1kCoJVtnfXTnI-51wGvM1l8rEaahX_xVe-D9iXMRF0xiawF3gXzZK30J0cCKxIqnxZsHjsSo6pCgChx6CZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2640">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JDscEOK5wlKx3IPeBAhjcUDSZDy1z48MbhktWKwhqL1aQ1m2udGfLUIeMcIAtKARHhT6ttbdjQyDU-faLp-pTebPmPzAEO_Ca4VBhPyk4R45GVn6lFblCc_kOSLSkti40ylqwc8fxNzvXjIvpaFlBErGsnUPD_eBtX15p1bdVnNrcFsZ3ThKPudaQd-vSRAcO0VIo3JajOPCa0VMS4atWqTIymn04Fqz7E30CKvOwG9j8OJfxM3Ac7lO2SgwpbbBv6Hardz2SGfZlh4mUblT7dp0qTRDJU8S8DCT4VfSkXbt37BrNflVbk_u5JK6ziHaADyWSBEkwXmeHhOgZJXLDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2639">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2638">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sH_HiTFsPxAdjB85OyDfCJrcSpat2D4T8VQIU0ciquIPbwLlsQLfzx7L0Dze_z4F8t-Toif6oFtkNojXxW5WhFM9gX52AGCaXJgNnRdsBQ3SSgePhJOEaFeErAWQ0OGW0FU9bDlNFh1Rs6TDUqihSPah-gvR_EY7FMQxSVifcW54Pzi-3RPEe6We_X3NLtxmVD5mjJ4dWmMqsZbFkAKKu5_Vl5TQeJtkNw5GokNKHlAt9T8jMKyWsho7nkXRfZvnHjj0hZQMj2Jic6ogVqaq8xxf6Q9tlNBSsZPd_HgnfzdClmgVNPDaJYb-3no-xOEUlCSshpbjKFZ2eiZv566RoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2637">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2635">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i9IwB1KafOy-3JM14qng_H7V1afv-ANHhCh-MEz0wbDaiRSBKIdueUTI93UH12emAcWlRncUR-OnUquPx9KUvVIqlD_j5DVj_S3LxRfLXXRxLxCHCFuVHZvptgOY2-jk_nJlhe83SJz09qQZZB_leh7K7bYcTt37s1pXyMo-Db1EJoTp2tWPudOj3TRW157iZHHtEllu4NeBiEjbICcCCQTB9H0NAph9--Ci8QZknOuus_y3Qq5TO7rpWRmnLfGHsQ3P903Ex2kq8sYxLEdSklsGYfIqdBp0iqmxs2tki9Nzb9Z1fg_OpS-lypNa4s1uTrxcoQqq6NJTIp9AimQPqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zsk6Uu578YKHWt1xiM3xSzgVCVvjJiu7gUcok82uasv1lCLnxeqRBb2_LXJYO1UnTeeJrCejVDdmncr2AG3rhY6ielAi2tfTK83LlUgZ5Aerl8nKNdVGjylNxhEEcOsLC3k0SlBfxZV6jqM9gqDfKtCrhGHapzfU2kZV38KDZ7t_XeTQ41PPtni_ki7YLStFs8IBXDgxGmczbZMS9BNFEYtJpe5yDf3JsIBGSp1SVoU_TrHkydscOzPeQtqRMlX1wbkeIuKbHGL33hjzvuY8k2LKcBMwUaFVcpvRoPdwdLbYVifwuL6jALJOoItsiZ0EJL2RYE_93vhgmQsBFiDSWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/US7YIuMOoGD_E1pMFurhnkWfnfBsxV57jhh0b8J8V6We2XpjPtrwSmf2kP7XqBrKfHWJ1dw_QA6i36VWd5-sia7N6Fapa4pXd78xKD0Fdr-xg5pD9cbmKqUTM82kp4RsUVYVDh03p0ph0D_YcFTuUsMjmWcNN6TW91nLiG7Q3JqYMFSQqkpCA5sEue7dWY7EKf5m9Y4q-xl0Ua5xbUsWjXayLjmlweUPjs4dTugu2nT-MlGG7B1_IT7hd1sMi_NTgdJbZb8IhahkKoQyykAkQt2ZB96d-9H35UuYFa8ndXCelzzt_r54d0FM5UXNoxLtFLzeZJg7KNtubqffC2ao2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pgW7tNjrqqCJjWnb_oXXAvUM8e1hw822tnTDP7-vSd034Tcom2RvruLXK_aBqFR8P1OWc5G-qrtGSMjqDNGbDy6VoQix-w6wZ23x1OpmvjzXx7ftBUUDX2q1MkGI4lxj0KNc2aQ7dD-89UWSB8c8AZlKQRvQe4Vy3EbXgHTOeSCSQ-A0IosQPA1z4NSuaUNitbabgDhSymGcTZNVEEjGM-Rv_DM60O1L1VLstr_BRb916aVAiyUMgo-9HGUPsvEJNJyXkFrKL_S3MZ-32emOE4-sCEB4MDlCLI6FXm2vOv4LTxXgivFb5pAFB_BnC_NzhQmoei5ZIOxM4CGvM_jcKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2631">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fZoEymRyyFejzQvOWEjcHCLa9PjOmywbFw_lGAsc84aEwMXfCZNfkQEYHYEpcb-YcTd45O3eG4BMSLfPe5O1y6jZfjGrW56eR6ni45mOq-R6thJcIMFUEdewpCwlyjoslzoREB2oXv45rg36nG0QSCpSThh04z9xDhbqkRl5cAj2GmYnkp8af9tbeE3ksXffXcerXliSgRfUbvmSwANJbQKW4OXcSOnCGhs-J-zpaLyvoXS7WrJBpSWuuxyQ3la5_VtYjX7LyXZLiTB54FQTuJWJ564TJMgKen7gqGqYkvDgtuLLcYrlDvT1VurWTpjD4p9n4_r3Ky-BrC9KpzUHmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GdQI-JtWKqeYn2NDXrbiMhsquvCoTMK99n5VzAQT4QOPKY0nJIdLqsz28USixziPFB2C0O-_yJOwNqIhLA-nO3EOh5zP4_EKk1k1-Vvszb78ptqbYpBHRgcqJJF_Ja8W3zQ7Xv_WSZ8EoAJmmvkgtFo-XD8Mst0ucoHg_VnGX6xjCCGzLXOFNmNZMcHhVfQyac8hfhiEV8ZeTfOw-WmWC_6gf-q5jVIKSMwtY7vriNFLV7esz9CETuHM7WR56RrGGLIxTLa0WMjnNkl3pZqJ5gLlCltuUr1oxrn9XMRVMRZtea_SoYTPgcYZB4hYX-rQl7zOhMYkIV15iSaM63KC0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2629">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کاربران در چند روز اخیر قطعی، ایران‌اکسس شدن و اختلال مضاعفی رو در اینترنت تلفن‌همراه و ثابت گزارش کردن و میگن آشغال‌نت چندروزه که شدیدا اسهال گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vfQBqznfzLwA7y1o02R9MAsRUMAQ2iTwowFaS-p67pUVSiysNUa1XM7Vhvgh3pk5V1iOgkLNp7vcOYkmU7U8CTQzGfSmBgyiNG7UoIEMwhPSDOYHClSWkwatXVwl0p82FW_Ea_g0JX-oDfkuVlF7hykryLm344o3VNygT2kgOSU822bQqRkK-jdNlBTMaU2LOQzxwbNSE0utymlQlbkMvdOBXWrZCvJpRhjYAPeaihwjQYoylVCYLocASODd7KVzNbX7lvYdTWNc5lS0u1L4eJUJ0X_K4A4ijl1TSSJfq4xe5ltNosyMqP21txinhPUJj4a1PUodom3CfIoBuNeGRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Group-IB، یک بدافزار ویندوزی به اسم HEAVYGRAM شناسایی شده که از تلگرام بعنوان کانال ارتباطی و کنترل (C2) استفاده می‌کنه. این بدافزار از پاییز ۲۰۲۳ برای هدف گرفتن روزنامه‌نگارها، مخالفان و منتقدان جمهوری اسلامی استفاده شده و می‌تونه از راه دور روی سیستم قربانی دستور اجرا کنه، فایل و اطلاعات بدزده و حتی از صفحه‌نمایش اسکرین‌شات بگیره.
نکته جالبش اینه که مهاجم به‌جای سرور C2 معمولی، از بات‌ها، اکانت‌ها و گروه‌های تلگرام برای کنترل بدافزار و خارج کردن اطلاعات استفاده می‌کنه. Group-IB در گزارشش ۲۹ نمونه جدید از این بدافزار و ابزارهای مرتبطش پیدا کرده و با اطمینان متوسط این فعالیت رو به گروه حنظله نسبت داده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2627">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2626">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OjmvbZFNhP3JJdJ001f3Jd60E8MmkIPBW2lfvvzGtNM1_mDiaEQjP6Ih1NXiNpbjc2Vlj62m96jpUNIHCnXadP4LFZ_QEPk7W9YMrnXrDqHZvKY_j9Gckyc6cgqQ3_4uU10u1vpV1xbErBbBQW72u9lENwDvUseQSky_eDDZmiw29ComK0FMqrGVKwPT1LHbDDrYXUWl8iF-AJeyPgfv2aO1MTI9992qAUZlydPzg__Qk5TabH2tdj-OzwprYT1G09afhKST8XiMgzaLCuZAqXNdDJWe-tC5BjwSTT1_B6deuDJ2yymVrtgHtdAsX55ebArdILtyNkIQsLVQDm6zeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از دیوار چنین پیامکی گرفتین، ازش بی‌تفاوت رد نشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VR-jbHf_2KbFjJYMRgM4as3AD3BXMEdDXrHP3UCjbfh7sSslsKseZ-S1CdpufkIhXFzOB9kKrnIMbKc_UmwXaU3VYg4R8q4Fsu6qghbsNbcDblLGekeA8UE9Fhbi3qGULLBSZX9-7RC8URehRojgt7QTi5hl-lVYb01TiAUlA8FSnLc1P7yqctbaXCCLygFNDB-d6TDoB0-9k4dJIzmajGle2yyL-_ypUSgSf89Wn3KyhTHmgQTspM9v7kgtej1xQudTRK99rx9PQcH5nFJgWFYmNwlY1CzyDCElf-McA5HK2ZsmmJ-XFsWMQ87G3zCPH5lFLmbKDovwO8ElX9vOng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرامه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2623">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pN0vM3CB1N6DORWPvjwq2OFDPYKINx1gMw7XBKU8GjyAf1U95DrUFucdwM8PrkwxioUjG0d_KgFki3RJuHnPZ4dtaGoovm1nmV_9Ql0v7kKkhlw4T69neHVZpkDl72bseaWMIn8s3piXIDNMR2w7zKaxwYGIvAcqMs40ibMcOFnJfKoDh7k1a9ymWEQACl0ipkfEm-4pjzMDy0KNj4GlFLES_LD01gbE6hdWnU-kRxn4yvSBj9dp5gOmbWe8-8gKm3x-WDpxEcHsnS2NvqS7qxUCjsuIvD8KJ20ybLxn8_8_OpXTMSgKycHjkLfinBpIQtkAezr7jiSTeryt7ok8tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر قطع‌ارتباطات گفته "فراگیری استارلینک میخ آخر را بر تابوت حکمرانی فضای مجازی می‌کوبد".
۸۸ روز اینترنت رو قطع کردین و نگران حکمرانی فضای مجازی هستین؟ بابت ده‌ها هزار خونی که ریخته شد، باید منتظر کوبیدن میخ آخر بر تابوت ج.ا باشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IVnUO0mQoNUoobExwD_6ZZQeJCdImiBZQlreu0D0_JsmUwJvgrNdCNXgkmO4_wvQuIbKjx8dj4K4NzKcBq-CAXPohyTIpPDJ10fmOlqpppLqHZSL9ydbEmC84_dKgMMfDX2AcYx8dLci3hbn1TPRbNZhmqMBVHYn0w0B3MMd44frIwcHKb4n03MJy-FAfEDTsq7XBf23lWK4dQ1K_0AQJZoFS-f1RZ7lo0IT8mbpqSoBTVtfi5QKyuneBofr92jLIEbdD_zBxhu3oG64hSt7FMSmsyUWCZg5Ksylvn0fgsEHcZM3SjwIPo9WNidsX0suCsRPobl2OddNd6jEjns5_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی با ابلاغ یک بخشنامه‌ی رسمی، ارائه‌ی هرگونه تسهیلات بانکی برای خرید طلا، ارز و انواع رمزارز را بطور کامل ممنوع اعلام کرد.
این بخشنامه بر ممنوعیت مطلق پرداخت تسهیلات، چه بصورت مستقیم و چه غیرمستقیم، تأکید کرده و مقررات یادشده شامل پرداخت وام از طریق شعب بانکی یا بسترهای دیجیتال برای خرید طلا، ارزهای خارجی نظیر دلار، رمزارزها و همچنین فعالیت در سکوهای مبادلاتی مرتبط با دارایی‌های دیجیتال می‌شود. /تسنیم
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RjcuZROGsldwi_ElDQrydgOJAn3dC727DwHML-Kql-wJY5ozhNvKVEYcNvo2HADnZwKzsIMqi-GNQNf6bVTIx5IW59hEUFy6CwxZ9zA2BQhxC2fpzFO9oN21jGFwHCMSTaaneyww0t1lBJYdlBkKkEJGKWChggPftJ0LmwV300sRVDdy3ws2MH3NLtoBhJTQj9w6spuGmWx_HMYitXfvwmR6TZoxRSf9lI-YK6SLCs2poxXFcByZdBWymHdfrBq4priowVdiEWHQKrd_Q7llcc-x3wuCNOX50p9zdjF_94JKSqpr_pOJiNBf6L554wh4JoSGmqX_JiXuzIVJagDSBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت تتر به تازگی اعلام کرد "به مسدودسازی نزدیک به ۵۵۰ میلیون دلار دارایی مرتبط با بانک مرکزی جمهوری اسلامی و شبکه‌های تحریم‌شده کمک کرده".
الانم با عبور دلار از ۲۵۵ هزار تومان، صرافی‌های رمزارز (با دستور مراجع) معاملات تتر رو از ساعت ۲۱ تا ۹ صبح روز بعد متوقف کردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aVTvJj_1e9mM6Ewf1xuHhZZcrgLVDtBx78gV5EjcqecjHy8rTsiAOPlykn7kjMyaTiL7jmfCpxNSsSBdejUpQ5S8r7p39eEqGaq9fQPdDAhvso6U-P6mesGWhDsy3yQ551PApLwOjNlAA-IAw7cHNyT9q_6rvev3qvD1br4oQU9pJGYMHrwddSKAWCq94JnuQhD5ON_qHTnQXX_8tnKjRpMg4LUyKlhxW1c8qaxQJe_jFsvMN0RjRxflkonFnpH_G768-7Iwcf1OfyVAdeICJgFq0Wz3mrzgXv--nEcv9O_hNYy3G-cOgGzlUb0fUoFrW5NWzst9GWzShUkNf84gdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YXyvr_DrF48LrvxS3vxEQFsCn72o_hP3vOfL7UtysAf8M53HaTUMLPvtPSQKASkg5UkeaVAeywNq8vcDQ3f88Gm5WVWqxyo3XJdLKqNxUvpU48o_LQiV7qL68Dn1U47zAjaMEaGqY7oYvUXXORXGvAemGaXEpjk4s_QHMxc5glXh5XSDqeHPU_TmycxtrBSZ8EP8K96dz7ToKu-OirqvJCAOJyWqTUNdUW0vYRYtEPwqAVPnPdEMxyCz5WZrY8FVXYAoKSMVLhdbVngnOASKVtliCbuq4uuONft9sOAzRSrwUicuwX0I3IcLQOJaREkWJlit9Tcjnn4e_JtG4oRxtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YihXgTqiHd3ztwd1gSWMBcXZRdhkIy468HsHmSdxv29271-mKO6E5PT3_MNx8KOEE7XlBEQBiey-m8L7cNv2qodaxckflL5szHx_iEc_9rmx3mSfM9ggIYS929HJ0jhb6w58piLGnUKazlxhnykIRG26wu_2_DYEj5U6VnnO1G8BAy6AcG4b71epQzpyxsFwyDZakueiBORMDCOgxtqTZZLNlPzoV-WgKIw8h7ttAm5MY7GT0ruzFaG0lNZVKh9nHDE46hR34nvhU5UE4idzaSKAWyfO4bJd5v_r_AMj4X1xjXzqDT6MK2zAbUOWLx02P5APR-IuVOEy_Oz9LmuwwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">معاون سازمان تنظیم مقررات و ارتباطات رادیویی گفته "حجم‌خوری نداریم و بخشی از ابهامات و برداشت‌های کاربران درباره نحوه محاسبه میزان مصرف ترافیک اینترنت، به وضعیت ثبت اطلاعات محتوای داخلی در سامانه تعرفه ترجیحی مربوط می‌شود".
خلاصه: حجم خوری ندارن، ولی باقی چیزارو قول نمیدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b6K1jtte9-Cu67kYXm29f_2GEKCSU_Y32g9hFhYk-uF27Je3SENbTUhEvC9mLk7IkIIH7pJBat0ul2B-AFK3hD-gAHH-3WMOHwADyA1C4r6RLY-KPR8uA_eXNHfb4nmXYCNch7cQNS2XQVLazA81uG6vkWh23Ita6lKH8q-pw_K7E0ORrC-hcne5ILDG9ShpiMUJ8DdT0kpu7m0a_Cjf38v2nuIcjKXVyiRS4_Q2x11RhEAlG94b9RWKacF_fgc-YkAeOMCq1SBFBnwiKpOPYN9LFOklHOTANxRkJH47kxJAKeBWiaZJpBv7AItRroqGvrkViagWG6LV9n_kKGHRFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BDQ67oOfUl2kPQKyIVz3q0I-Tw8jXCYZHDVHPgpmVJFs7OuGjY2R0gYpwMmhC36dINFazKQZpgrlBfSOcVeruMwewKVlnOxu38GzqnaAQvq_njVElrhdlT9t5fr_avrq_ExS1MR32f6ujwIuk6M4wiRv4Q4I8ig4fZla-S-kUlIlVPnuOSnY_OtnoB2-5UeZICCaQWIBewGlyp3hRqIsaE1GzKX8OX_qebM2D3g0KZA1s47ch-NrO1pg2BCapaYmgTjmXXKP6dD5qChjIAs6gJJlO6fPhEYEVPmTFq3fF-W7bof7ZQzPc4Ir0Fxh_2Jr7z6pJ2hlx-yqp00dIcdGxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lzw9jv4Ml6Q-CNqZAsAQpITr6kiTe0DlrfznYgIJq3_En-4nL2o_ZeMA-XEVluLlzJ9KBWmC2vKe601Nq4vl27TXGBnFqroIcf7ic8HL568iYQrjw-VYk6KXyngeWHmmSyqyDz8w5FpkMrwa6S3GjqINZGeu5SjU_kDDVtWvbckGHyGsp72BmmrBSaNl9X_GoLjh_u-TI8Gn0_3LwDkWJ11mZ2CRfbOpmo-3mGQueM3IbXDGcQnsiH5LJGPl63-FmRLr433iEYybdMNR2aLm-tStNatdNJNfT389pjeoyJsXgGZFv-K5AMZELfiRk789xoI21Rtb5w6DY1GpYKo75w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n9ZsDcHgrl6QZRLQrAiAAeGLN0raxxIUd8FcR-hOaJ_XGpghOvfq4Rqjy_HqaHK_9RSCVPXXmio6Q2-pLaduLnqCseNoMs5gDVGYed1t3hVDOS4aO3qB2J8_Mb9Buy_ikBv9ncWo4DJo1WdoBqLaN1ouPOyqt3Bh6RQZomKtvqgzpToO8biTlRBHZzkRa87ECXkFuvKzeItfS7YFrefLJa95udPeff8G4nR7mhxgg5WUKaEkBH1EL5bog-0J5sS7X2v9VM0k4wokKxjJ93BDh3Hu9p2pPgDmsVR5uNWa2e0BDzwq5BOfXWb_egAlvTpqb5mJv0S0EMIuXVG6AzLOWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rjOzuzwOgfxtCMnMQiRw72W8fFGQlXeXel_U28kIdxHyBIw_HlueKYAZnEnYJMEXuQ7S8Akj4kE7YSGSQzd-_40ksjAM40mZkZmkvkquEd4gHsP87V-p6Gqa-alMXTFGiEYYp5YHSaoMauaqL9lT8XBxm_WE4mRhy02UykQCTARa85CnNPvUlHPluyfVRMepBUxmm2igsTuslLYYVK52YoDD6BFBQhmIG8r4znGjY0wjRfr3P8LiyKiDgqM1PIPlFOQUjgljgWgsiGBnEuchcelVg-i0eXNg4zFKC4MRR0BILOmRWf-d9z3jcuDdmumC8lKk2LrhgCm8Uivloq1BBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BcI5pMzfRV25d292g2tgrdt4gkwGJrXWWwYqIPyuVEDQ6QK0g5k6BA9s2AYLO67D_GZWSXpUQpBm1C8rJN1TP8nd1PybpM_kLE8TccDR-T6hKlqzmlBIhsWfI-jQLYsHSysLzS-ZSUd4-E4xkmeWKQFrRc_XxNktFXhRtzy6tQn1UDR2S-O8nynPpiRu6PTTjJX5GXjlTj_lQVdZknQQzLAQj6MULhvq5KnN1pqembOS_S1QfKNlxHt6B6BWJpo7TMrc9jozcbaj8OewsnIAWr-NHKRJY-rPcEQaZHkY-7KS6TAQrJxtCwltRq3S-bSbPxdLl2ZZV1F6aTpw3addoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U_5P_YWXinoxaWqAL7ECgheE1CCSLH2bnAUn7ujMOvEP4CK9KSSDOkAZlR9Zo9OiGydSsqoLHEaYc-aBIB73apuG-b49G9hvDIoqHydD_4lgK5nfYNruIxF5wDSJIJr6wgGks_aS_Dt7bQReID9rMQBlEDFYG9YEL3IGZuVWutZY94Edo83qGI5NGmjcqMCChVJCA6VPtbVEtP_VWcpTmCt8VqWe5mJ3RI63DSLCej4EIE0d7oscdMPIk1HoomnaaHUG8joh3wT5iV71G7Ct4A1KjDq1NdrQI0sia3v7td_U51fbQp6tZ1BiBqxUjQfO26d0t2IFHLoVDXRnsTaV0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T3evmJQs3oYpkHD0sA5BpVvBP8rqncAYIc_U0SL7xXFuzZUfV2YGDjOnSpoL34Wb3lUo7mI2NGU5LO4stPF4Th5hlnaR50SsHzhhTN0HtYylHciLo5j1UkAnQs8HXIH9LAO8-_a-Ijkwk4kq-kFoojO-6f5C2gueuZlDEdixwjtgiTzpsORkUZXxbEx-Sp_mqj4jG10rR7O05cWbFWjMzvw927rdRXXaf9hbSw6yTy4G6-gIM5QcUPleYFtCgeLF7df2Lq_cPyoXmUwHmYGHBE7rVWU-J3o8twHFZkmPdYoLtywwEecIxyk7vftn4eKgicMdLyvvG6gIkUA0o-irQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q98X8QCOxu29zf4oS6DQjbV-eJhJJyJv-U65bGm2EFY7d9QPLiOLRD5JGrJ8mkiYKYYDsjtr8oByFC6-9NgYrHJ_perQQQDZue2s-9DcnlNIq8ei5iYsmwy0oeiBJqdm0Dvv71v367QuPPoizSrXgLDAD-O6mrRJAmUe0LTnrpXYqA2sG3vrVsKT5-7NHt2rqW_98E6OeWfHk49m9O2iR3PzwQ9L5CGyE3wSTokR9AAH4AKHvADZVy5ypnOev3mXqX52oFyFtU-dArEhaxjqDjY977Zc0Y7I1dvB5sKoWFSi-DdAWo5mmrnv2z0WokP50e3TswGbtETy7jnv6FhkXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LUo-pmfVoVlWz14iKus8hUhwtiBmtu_ZC9nJYhlz8E7T0VdCxKJgeE3kikUT4EpDBGpHpiY80MTJMHAF5odADitv3oftswMUlVtebGYWowwF0FBdNSZIyL0TrDLYOgjKHhYJ9KBqNm_ktG3I5fRmeJjBHcx7_7mXqKVixV56CXiElb9yYZn7NCSADe-lNmaDn9HqA6Txo1_wSnOnN9DCKBm0V0rJRib0JGT9GeGvmKQruBVqzH7GHXpbmfmWSxQxZVDD73DqltCkJpnA7hUma5-cH3dP4WDg7NRrOhCVOIwVBUmX5x7TE4JppWiEWHPWwVXchusft-4JiEQk_-RFSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ajy8XbIt-2KPTV-8Hi5kDhnw2mClWAXPLNlUIFEair4cflqjSmaZLtXrAw_fUbm6plkocbbzHH0GzSPrewU5Tti9w8VGWm0-NT63tYZc_2xU2DXn0tScQhuX-kXGW_66-GWIeaS7Pwos0Zu-vg7crC88yInOOODMCDsIwrjAy68Sag0DFu9yyoSaSSLRe-Xkv4WkMY9VQVDYCvJehbxdK5aZd5Vrgb-kQJhaNQDQiXjw4Zylf-X0pBgUQTzbs78n9B2dLZTortHlije2P8VAeZ3R363dC9ivwby5HFK-OsGf2lZ9UQTlDUjlacJ-2JEZjU7B27w8GQQdtUErA8GU3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CDucbvRVGEYn1-bJjIemJLPQCc9hQfsTKlcgdTT-oX2_4XgXE3Yaq5f5bBYpZUOGIs1FvOasnGSWwtbdHy3kfvL6JJnGy8Nvg4-XPPl_ILckP3-cC9zWSHkCplHC-s00uNWSt7z2ug6pzcCNWk5I8pW2P0Z7FiIaAJH3t17sL-svq2X_SLC_KT2ySrGISoVCKKFNSdlmFKTUV4jmLVbimbT6eX34IAFt_JD0YQLQlDFPoIzZROigWdOM9FhjJ3Z85TlaE_2rrDbZeBWvnUDDcV5-HfJcYbvhFSTMiqTJtFYRV8tzYWqXwZcvRnYTx8tVB8CEh5ZK9-vdQTF3j3uXTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L05ig8LxfP6rCTATi0QlBHkhiUQPfVpELLSuIUZtOFu4VQg3mSX8HHnL2uEfAC6BwFfAQEJDm7Q0V4ji7GMa9dr-jVnJJabK-abFKnKawR7l8SUQPVjDQTkAlqXTyi3Zrw1EKslskW-TCzbie9AZ6JTtlDqDmtCJwAPV1HPxwBuEHfoc3zlKSUJFtstQT8n2LeSEpEwWSS6uSvZDtgjHiDN3v9JKqVe0BFRWEHVO_pQubR8Pagt1LrcQn8U1XHzcC64crjjJ2cvxC-XxZlqzNMwytGknqIqsuJ84GLiPkuqIkvSoRThn5EQKtoENJvEChumCZG6Foxy2racK97yZ1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M2yRrpwyq5G2VVQsmculYZzBgB0cPhh-Xau6whoav3BhiNygp5NCrEA5aVlBUpU2PvEAjLo2Is1BWAf4VLMRaEBWlyrXULg7oWb6i--KEDP0B4u7jpflrwxiPfdbeH8Feig5uNm12IjBPNVwIuV96adUkdjI7rBtnjLRjLUZbAE1PX29ammH3gUxKQN4FtHkWSguLp_h3bAJKHOcFpxU6oCR1fvpNi1f6vOrKopUC2Kvt9RiMg5CF4v2LPYvsepk5RhxNtW8PkT8R4xbub9JWrQROQfoZBCX1gSdnw5z1oY_ghEi7dGNUwn2wVglagwsffuZLjx760GwYrlQV_EYGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u56-sxPZNWkN4EV6qIcCW8U_YSoMdNP3i98mdSfgAK54Hk44yHysBlF6s1qwtcdbGMonjn7Z84jndxqHKMOCWdgphPi3W9__pGXaniV-udQIstVlaPEQ3ICi5NoUrPHmb9RiUuFxaCsJ6MIMGnoVyLvYSCOxDDTHHmWaMlYHBbFusg57PEf5x6vEBcwy6H4LVTazaHAUYdueySswaw9Wf1K3Y1t12tcaacK134zA2LUirJW5slbCnK49RQVf79CL88RkEYav6OokWi5GqtgWqAKM-ls2Feqo44UMKRNoaSf3sXcsDa-_NRrvp-pdCxO9LSJkCL0aaPxhMH5HpNLrfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HSNijif2lJY2wZ27PA0XaJeISb2zf6wfk_IFiWCXVOgm-Zn2EcgmG97BV6-itewaFN--Zx1rgpPYcB1JX-yzh7QveplLvsXa88il276cbsSmsj_AqqsDsiWpvwyoGjnDlM9d1PS_DKZe5yWI9pOXVdNImI03iY8tUtRX8kXibmpcVQEKfez8k74S0TcAiAmiNE1EfMkWF4hSt35AMxeH7k8dK8lZvNVX2V7z88azJamBUs4iQu-Sf5ZDoMlGloZ6X9xFi0pgwD-8HuvVuxUHnQgIHuB9v0WPTK9xesD7EJ-AxRN4ItGQfUjR8kx5E06z_WnFE_GR3Q85Zw7Q5zgf4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cw09l29jXoESxYjKkdlhmvjfCmfze2n7a5s2sWkgfpb4nYU4CG5R095gFv6ja02xUIXimc9AazueR5JUqoFqJWPp1TdnLREjZcxTmNyfxCLYKIlYQUOxy46HW9myGc2g8OWC3zGgyhD0DSY8fCsGYjIm8_iH0LYOTtBm3KLkharnJhrSKFFS_uIZIQiwBLmEql8lCI2f9r32ZxmBkx5ngfHNOhCKTOma1cVgjNGR2Sc4jq6T5KOzIPaQl4U8BjaeX2Xt-5hwHuoZMP_qYny6vj6l38oShVWud9Ra28FYYL1xUOErxrlzmBvHmC8we4TEiNBavojFlHZLMKHK_iiSwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uhvWh_LMxYGU83Y0Pdm0eYHKsU7S2A7HJNoYIQm-GEViRZxAVbZjbZGPmFcuvLgI_1otYLC46q9vpNqDdkSMh7-QLjz-tO_LXGlkKX_qiwPhLFn5btSwtWflJ72MvPYCNlCQEKbgs5_7mElySh1OjoCx13WdoWNO1whnW3lYiqKsNyQg1aEgdnW-6pJci1vr7PgUO4GbnzV5DNb_-a4OT3rX4opnkK-BL1vdIojalxnH6thEkxgqfFcmlYGZQ8OhkcbZ7RVRZFB3Z6aZb-fnrzsab4wDB2cyfIqx4iegWJlfmOkDLeIovTZBqi6FzQp_X1XXH8m-A7AYgw6xf4xBgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CChrgHZUcxgraBvRp64ndcW5nBmvQUaM4dursSPztpr3WWrCMLzl7n0wJIEk9p6NqrnkdUWFWU3vpWnnlM1GJCiB493f_-iI-QQL0WCV3aPmRb3pzItK22PuscqwykMCH9yNAtvOerhcgta6hv36hk1BT4dreACW8515XqP7f1UO39gjZd3_RtaawHbH2a32INAo8M60SsdlJtYKFaeuPRPNDBYfI-zhHjkx8OGuqHnpzv3_XhSOWGnrLsYcmpjF27RUAUo-mNzHCLiNAvll0uHKHLrHZoDI8BKdOdKqazuhnlZrKhLx0JasW8-twglOA2urpmwBOjz7qp0ndyZnGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lqh7YRrcIJZBRklx7G4xAEKuhdObCuNMgXStZsH2lLfv7PNNrYmYScZUUmg1kQV4SBm2mDr3UwPbooMCoCVjFT8twQsCHZy4Sdh9GnFBAHPXuQCE1aBfOPcq4H4jStfCn04Xd7S-mN5NmqIo5jJySOkOGMbJEL3GmAR0D5mKlJOFD5VS9egPyn3b93_OHUBAQUrpXGUYcNXEfIfW1yqqr1WafeLQ6A6Vj2gGXPwIKILplQpjDvj8EGLefMdKIByxSJ5mDyEKTuPHql6ShqgDQkeoPxYbpF9KFYP4ueQIH8-pYPnnxQ1SXgSM2-kv7H2YBhrErDgySnHQJISqwmBvTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cVlvXRCF91d9yIr1uACgwPH3WtDZPASXJl2mZTJJ6ectqBg4rVj-Kq5YrsAh4TJOv6FxCS7kIWMzUO6Z7aYgMpm08OObjRPAFooyxqYeZ4ixmH_t6Hl-7_wnLVmziWIIw1kcTJwqtdilyGdWsyZ-fXgUmJoFslFCTE0HW8Yk6uDxjbXCwZNupLelR5fi5wUVpvMFuWO-a9n4dl3sLwdEEwuPi2rlYFhpKb1GYk4OiNoMD239wz9DU3raJ5iKvLZgB7_JJXUgUNNsAMBrJFLkgrOlDt5UBVH9MrhvBZCo8K4Yv9GRddpNlvLO7LQ8T8Z1M7A5Afock-sxaX4Cw_Rjbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ultd3DyOquavY3a4tUsc5iIzeZYB9s0ljtxCkA8RJXQIJnaH8g5Ek-nO5gH9z0Rum93LpS22Lb-AyTumvtIAZcbVhom2hzTlflltv01aIb9tNczlK-n5RPAnmTi-g4lYnrJ8olW6NtiFKEVCrIz9huOdBsd_Vgyt1pMT8CYhclopDHoR0YbYKde8tU3Cj2bXzfgpnsZaOk3QnEU5E4GovVWr3T0hKK4mnsL-0Qp59Qrbc2Wivk5Q9MK5bEVV5-N3goCSIds0BKwaPEYMg473wT2BgXB0dFDdMjbUm1YTAUQ3nnnceVfl40I6-bqaEL7hhw1hO6aC4_te4KamIUqwwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hFtZmw5BYogis0ys8GAG3-4sVteFN4dNG5BSsBy8TTmhPfl8r6ZmW1VhmsJlhzhDBWEUx9hC95BOT9a1YHAf6jlb-SsIGxyDXLTCaTuq1CbS2rJmeufJhVXjW5SOr2qE74oxI2N9iDffUzbmPNKzJpNFjfaF1xDkdhPB0eUOarNNH88JVm__NJIEPQLqeK9bg4Jx4gM1xZ8C6t8-3GMcSOXfUzxS43xifdtG9aIyKp5JLsOWpEsyuB_dTI97XDNZH_4NuiimMCfJoBEMiDYpdX0OwGrjbvC8M02zPFbVCkcVQkOP__ry15bEPuBdMXNjrVvMTMmiFNPQi6qvw4Zudg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qfn0KPVzVp-ryKsuID-vy_Xmto4YMvhjdUkmFBLQTCFUc0zZ4Fn3ABVoGdgQnTqTf1gSxWDS_2zHejQ8uvlLuxIr54c9h0ZOJKYk2h1j687mgSQhx-6OFPdZVVZJIgA58TDXUde-M3-25B2VChny-YOKIMri3hKM9c0tqlxBR6srC2b-vF5-dVTA8D88Z32hEJIIQl_l0fJ1-oR-4pkss5p3NsW0T7lJgcpara1yriuyo8MMN_PvQnHkyqZSNkihqocKPyy5I_AsYjcaSXtC-pmG85SAsi673uzuZ9-UCtUWNsCzbNWnpohRoBwRZH-7nB5SPuQHidV8C_17kwGxrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eIkWU7PeDn-A6Ch-MCZ7nMYAOjv_PxbHNPhM-bpORWRrVhbz2zDTWMOZQ1acagwR2GKB0pLZZr7wYyg14jkEwmTRBwQBbc-9aIYcC9-rxNHyCbNE6rssw03MzCBoTGbGKyemw47z7vQMCk3cbN5rQ5nKAWHZ8rnBdbmFdC930EsgQ7Tw0LEe2DiTwdktlD7kkOPB7KeZuZsx6_5OM3BTxLdrA-WSoZcxRF6wV34B5EJV7RzU0R7-buI9Q573KnqHxGZ1C2RIOEwrVH2Su49P1jU2GNOQHN5QewcBp85mkUNLZxzw7XzbyP9p8-mwLoaqiypV_fHCAiyxr627Wsht1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dxz32axqXINTu25Zpd7bStAms2GZEX0j6X8xAKPWbITXA6SSnvNJinFMvybFsMTim6uGt2jI9r1LZQuShHH0wP5bkuRx1pHUTkYKRgtSiB4ty_pmZgYd6CP518Y6SY4bcqdikzxXv6h3QLEbktIKLYYBANEwGoO0QQ5MHHEmfcFLWV0I6rrgYRQL5Tabk6oGW_N2Rw1R3Z0b6ZG2aAeEJ_ATkxYuybOV5Uma45O7UT6_-QvwAzX8XsYN0a48WAYxk7XlwSZeKpVX3h1g4CRt5GjQ8sUZnhbxHjL3-5e1RrKzCjH9OnhVg2HMwYTkQdgEWCDDGT-LH35Q5Zh6Z-xtCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tBnRV-6VSX44efJNonfism6xXJl_BnxLdfR-BlpkQQ_-Biq8KO3O94jG2jCdGbP7EuybVpngXYVB3rQfNiYvGKhb-aWaOvoGOSEWXx_SVRSbxg5ZHQ5f4BJ8PKnRrArxpAvmPDh3pqeIhQcc7eRK8inMI_C6FlxueTNMebXKH-hzc7Wrq-SL-r4Zcm1efhhclObUH3n3iwhRox4U1Ot7N_ZeNzYbTZ8SwEKffoWXeWp8d81GNSJWfmwc7xdULj3Xdfz4mSW5-0Mr6kKOpCQKJLmIBpO_DtZ7gdubUKqPVwsfEKG2qfTsJ3P8H19k2ZfKuQ4PXyabGqEFt0UipXGWKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mZbRzIg2zpdLR2W7LjpCdDul7Y-4fkToFfHWOBLnLdaxPEzNP8-bM_Ro5FiyQVsTqbE3bOMIqM9jODyI9_YR7iMQGzRSfyGR6WFIeu8ZkB-Lxw1xd-Msud56ZvP_b7DOcfSTQ2rX-J4dZwQOK8xxj2p0R0jDVBrf6VXjNfafWAcWKX-JcUf-1zutLxVRe5jb0rWO19Muendeu3w4ciI8eu6axZAHpJR6wo76KE63Z0Fh1qTHhidYq5Y2yNJTrpSOvzhFdQKn2292cPECU5N2fIPyv75zAnA0Cmf4L1DyreHL__KnoiuwsXtWkFMauXC9GuMUPYRIUbODGYtzeA_3Vw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fIsJ1HJTmsxQNb1AYIAz1EDexctxJ7lSuykBVEC6Y2LN1H-EuU5rdA0bdZbl66d93rfN6O0oxtPMN07aQ7F3SkBJA9AvL6nGSU7W4o6Yxt5XYbrpz5BEOuY3SiKeX8S8U1oqvK0azY96M7rG2OnGn1MN56UAzhl3glkn01aS3TNtzPC_hzxT26tO3nRa8BBDOiogumRSAM3zx687DH6D35OgtAFT7AgT9kaT9f60RipLgbVt_MXkkhJBhpUn5PU06dhONMPdYDm-I19hWEf2Y8cnTV4paAWKUB20BBrFFWZwHZZkDVoKMvPvXxYTVJdmIoCrP0Q__tXiVxu9bBdxzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rigcHPZ3w2qJDkdO-AWjm9f9zGdPIm7BzSOGEDAPlJMd0SXDk_-Z5rS7zLmv67J_Jf4kX93yhywOnMXyM6YpgKtDcdec2iob0PAevCv6ktvUjX1QDIZbj52DBlFHhNqh4HabWf3XGBIAtZCKiUwmstvOvi_xRd8q9zT_VubKoL8wgsGO8DZsCE2JHCGv8Sar_4zsjvtGPOh0ejCOf_Tsn65WU7Mjs2qsTjKo9iv5hdGLDFHIgnGW8sN_CLvpvEPuEa2jbju6pETJWdvZ5AHKaJB0oN8YIHpKCwNFmssERNjvMg6gb7cIBo_DgnAp1xyp0IM2lX5NVOQyeqCoS6xz1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mcla2UVSuJyXvRJRX8t2NpEBCeknsOltCy1dYrlopMyp-6p0tT_ozWmPunmkhVEkJERxfZPKdZN667fgDViRNfAFlYOtSWDmUBedklWxfvHabCDsezc1gRTM87fGfSnfusil4eTeIS5_FqzrWZVD9V0pYViJqdM0zN-Rp-yjMFq4CZ45TWx8tO0c5Gd9utSr7yopMk_l4VvfwynqYLalSVZZXizI2JEZA-7yxmv9djSNvVVwcLkyL399Mpe3iPnCz-8hPS4ViebbTsgZwl7FmZtApDPDGIOtdttOTKCzPn1OSjTvVOxMkvO7Ujh7jXJD-2hfbbj1bfn8xMs9ts_bzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cNGQf2NLf9mYBHl7rjWoGxNzpq2RqwZFLbdQrQIzEJEJFC8V2_6hSZCNjwjQlyuUpGofhtYxCQX5j5wMhy_L9xACMFAk5afrLh-BaPz0fd0PQzVEOstpm_H10NHjIvz71vIqXpe_aDeEegFx_ThGaby0S2I9hFHfCMX6oUU4Q8yeV5Y92LGOYN9b9IYHZeB5FSn9wZvPBKi0AS8mZZBofiMpCsyNnIitwZqKpSnumVXSr368xHFJjGpBE6nbSBd7_XxHLtvckmXY4Hh83E5u72Ou-jEZLtXU6DHYeZ6aFQWbfaMW1Frb-f81RiXq-J6Ob-2HGq-Bh3wPLByCE-0KqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jnV5ziuaigeJfIO-faDR8wQJfTa6Zwc21yvctdk6EdYTPiQkDTusWaSMKJQauryojkRWH9eIFRmynyIzjD6CTWDM8HUphre-Cz3gww7jcMo3z7FdLKg10cnkpa2s5cQNbM9yiMmZGVj8NdwWnjHUPF04Y1rs0q4deopFGyB9EE8S2KWY-WGoZhRwyfIXBKGgzDoPfXVMjX6EhQkmhKOt3YtACpcjXNPOr7oHUn2HYTrTGjMsldVo6G-J5yMdUf7pbhDdPtV6B1i1o6YdVOPBwPhvsiwUwKz1Tj9V8sIx-Xrl5vojZEMG7hB7QXlfZLAjypT9fpSUPbVrCw7akMWNHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iUUyEQVpRsU5mw0pN24AShLNw3OyUcdcetaeHn50SwC0lDo1bZlFuy-Gle7F9cg0t05mDgoAD9HmwNPOg6oNJtQyuHhoQ5Ufa6bqFmirNMyYU_oMmPEsJSRNjGhYPGJ3Gd7kvqDIhazbVpY6V0QhVv2mgKtZZXfPTay8q6IovkUx2hs-koo2k_xzsKY0uUfytFzIIiwW55-gB-NWRk7ULvQS3-ZTfp1PmsM99XSF3d0yfoobXWe-50PZwl6bIyq_0dCddNZxBpQE7y9KguOivKhnWtZoJdC2TbPOnCiAZyuQPo6pdWdK_PTcq6vTj5XXey9RbaHQUkhJRFWa38kLHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XWFDsyklAhvSqO8vKu_WyCq96UFyjcTWMsiN-yANQzGLcMGNL7l2WPxNkiUtWjRLF42RDj8jBrsQNZwzdZBU_v4EFl1LBzfYAv9miZRDZV7nOOQoSpEHANu8q0KDx2A8TFhxS-0bv-IbXYuQx8vEkY5xaNWGQwA-soNAsZO2ESZo_VkD282OovVvYUBu04Vju5Z4IOTKXzYXLzPz7iElygKhLk9-tuBs23C4zzzc6et35ad6uybG7peGoUutjwIUyKgKXRSG-dPZsfgRfHD-G5r9sf0wnNz1Di0AxAwhvEFtByokGmcP1EaMnW7rqFbMz_3_wW3lvbQL2fnQb_NnTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lPjzD4uzDCMyX5GC-llThH4UOaW24XsFjRDqqMEPTZ7hVvePt0oavzIL8V_OIIH-jhHoEjcmAhza2uTKjGtxCtws3xMAo1TX8foygaHSGaRaIK50JILGJfBYU82Ulx7NzIpfVn6lVcU5RIgjKsMYJnCWHMebaKXhBBaPAwp_LqNnEnqI7DX5Usf6-Kxa8eRxTEPIethNo1K3OwtZJT8FwZcXnCmUJbnDR8abWkz8yYfhPLJvHm3PTZ1u7igh3tArjj0fUh-8zzx0Ah-kZo3q5--VsO0vCvpluNDwIMzBGCVMWMZ-uLqAq6Lh7m_jKS-Oo3K0gakOJi3IAA51L7DRog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sVHCLrWnLb8MreM4h7wG2PnfZkmfbYT75FdDJABF9n23S-vMFFGwzvnZmoyz8Bnl-eqaNInT9-gYQ7pP2jRLwKzaPcRKp9CzLgH1cuuFLb2_GPbgP-GbllyY3CVDCpDTv7djOUD77UgRL63CRaITcNmT8l3U_v0SroJIns2nUD_OKtUXPA6L4WoM3b1868xq4Bbm_VmYK_Id4nTsyoXUK_DUACrMTo3grnxn4Tzb4-G2Rw3SBV9cmdT45DU2KOOhGOvCj-AENirZNQxjzbt7LougGu4x0a6xn2XgpbPvCd04AF5_2WUdgUcMCHuGDvpevQsaX7S5UPRSUuaeMAGtTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZS77req-ePRbT0DC9CGVtxbE26FeYtwEP9Wl8cbmr16yoDGekpueI2JF0EEneVmLE-gmc2g2_sjxkrLQUXIqhy8Qqp32HnNhbJisDV2ndF1iliDQbLSQWWWLpJ2EtywLOBaJD5yWUBHxMtpnx90zBLfOdLdQXf4gko0p_Og8MabgQY9EjjifG479uu90MRYXdDkvHtuGh5LukkjIrGLCObmxgl5ixxXt9g2DBzKmwEFQmoCoBwjx8SsDuuwuJS-BDp7TRLRzUErzsED6uG5bcN56WrsW5S8rHo4rnHcq_EefuY_2wTWrHZWnksW3-3oq5dBYgvVjhu3esoPirY9Taw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QXB6TKh6oHSHHLJaL9QlIeEI8NFQmrt3sLgf6AE7PADGWkiy9QDe6syaelXllh4pFjcfDN0r1v9QPGPrMTLSijC6sxBxly8hXfil4hgr5B1nXjJVVVCVCh9r7MI99ATZfF0igZWGjvuugDLKNhF33NThEvGHJNw12FYBlD0qR8_Oqz6KHxXWv860m_Ydsf7j0dNsahbRiGaLKBfhr-ewtVr06jc0iSbAyfd2A04A7_oOwL-MqP5OhdxcxElMtPZDEyEb7VFKWsCCD6lPUFtmlRycM0OD2cROclgO1EnfZ6ejX1bsFyH8oj9ZDpP6vzYdw1T4FagRWFiY276cHSaMgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hilo50XKByaF_2hfZwvNoyloV2fQS1rJMmOqmfZ6214lVWx7C16Ob3Vd5SaCPk6OT46Sy2Y7s9x5K6hBFLeHaJLHaVM7Bvuq-vfupQKxNrIFDnzyUgQSkM8nO3_spVYJ7u30DvC5CKvHaruGexkcvNu6MKPqUXhFOCDGQOwqQyxIPxUXAvjrkvHZzzDemw7HaTqaBF1UT8WF8Z7a9u6jB6oBJU_mtcR9qx538J2tXpOL0MkeqSS9XZ24FWRy_XWcMBRsEnbsVJUkazEgb1R9ruK8gUq8wSTnmq7VVXuDKPsp6Zfx_7tbgXgVBNf4jIOebjZulcShEdjafMedKpTK3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ztbs7-sKSMmwHdJPJhdbxzc5PY62HQSmzqoweQwNtAul4g0sCXpnefaZYBYqKd-Wt6seQYMLG7FKGMyWKoRHSacPwYNoq0WiJGe619O7XF9gmi5MPDzEe-pSvzzSJbYWENwH1YVCmdzfn0Hb3Ysf0q9a6i8Ev8iGdrG55N3dL0gRr_MnTuMa6Qo7BQgWe7yZucc6kIqDyiLyzL_ueLPyiV1v_3PULoFkUS45ooX1FCp80Fcf9NzYCkHj4RbdISf6Siq3HztUnSTGgQNUrnMbT76xbhwkVWSW0TgaPIgfbo14r46WqGIF8TrJKL6QbjTzT4eOKNpNCV9v97NVw9KhOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CgyFDv-DPX-ZZUT3CjhBQl_rjcM9yKe9lOj9ctPztmUVsUq_XDc8bXpaHBwxL_QRn9WP7K30iQYSVxitzoO9RUA6U9LcBbX8_oaRFZeaQg1bP8qdNdz8Cgm1S91w2GSmAi-aTXfysBhMWQqlYlgYZCxvEiRWCS1VuY5U7cxdU34YILIcczvtX9FY68nxKo3Omc15sHdK1I2UVFovW3sKswubUzkOu5Qu0th9Dcqo-BZOHFqjpoFvvsFLA1qp92sovBk1QKcUP6jFVOqOjK9KWFtY5f6G0k5L025IWhU97SS3wu27T05rZkieNRe2o36zH665a2AgFKIdTojdfmNwMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b_IsDL91PIC92AhBRFvvBIyJ2Ns-Y8bWj4LLihEW9do_MRl6bpaIH47LKiUQVLqgEooiRTzpVxne4KXDTvBIqZ-cRp0PLVsFcUpqX939N_zfsDGiyOM7eSFU7a8KfcipGSNta0BQQ9e1EfGRChwUDbp3j3f-0z4Rc8MDNBrB6sJMS08X227yz-8vLNPpcLRKWrSs8wH2HnKh9veOjQ6QH_E0OpdysCIeZfXLMZNtbn6yrfcU8nXheNn32V7w4M3g6tuUV_Wzpal_7MUIDlRD62yxYK-GsrcAbblI6C2ZDrV83bttr2l6lWcP3DUC0OCGi3aJwYwZizWftO_71dN77g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aoVCQZ2hKiBiC1L_n6h5BfijtIaZRwquMnhp7YeR_0HAYrecnA3nL2y-e5byqaVMdV3fxuwfxdtb1W61Y4gMuZrVNXSOdqtMIdhWKLokP_WGGBCTjQVCmeiQtqb0hzTFmQku_k3TVLmn0WzVUSI7kArpTIHfTrLYFY9_o_BdFeyMImwKrfJcNJGE-kTFcfTL2N62OvU8gtl9xwwuUaa324t4GFTHGCsL-ahEozvgsuA6cMTDsDtaoL9ERaeudNe0WsqLgubLKqcZRylhVh6KkX4d25vDJDZ7VJOeU2O6NJd2KgXyObNFdKgAp_95r1rO-dX0hz0k7cw5L0RSS62hZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KSP8AFixWX0JFiP1hnynbtHwII3wnDbEhqqQh8Ymowvfo-NVK25WBwnC8CMHYHXetLeNxG2ruGRYo_F4ID1C9OPkCnNCNPf-_ugGtGffzHtq7ew2B0DlPnOCxppii-g2QysClU5GI8myg26hrlJ5JpO73Rtem52BWyJ85xh0rlN_LTf91POZkMMc2_BnQZNAu-zw9gwZoeb9Itxa-ezn31M7gb8eANPuSEeFZgIsXnP7NnAWpDh2kCfakGycRk51dFLOQBp-TZfrEL5dnCM6l6Q7CP8sbYnnNJ6rsu4Vu-OxTm2HoMYUnc9crybrtRkjI7DvP9A4qYScDTI8WP-vFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qa03QmbKm_wlqM9BWKyudu7tB_Y5NlS4NfgnJrj4XFAys4J3skU6SV8Raqkm-mBhJmmRO-fnfZRqt46DuRa9rb6JSy-nHdZHE71RSC3wvHJN-1C8zFPFiQtgPJf0bhXhTevMkatQsYEKmVLDyNmQlmgTKkyAq_u8rA0xXQMcICwovmwYbcvwox6OyliRteeJ-4hxdF0HDOTuGZF-8r7owe4pVN5meU9EK1JXMhem2B6Fie8dmNOztoNXgOrNWW7jg6boR7b3fuQiH-37EArrsXgcTcJVhKmMQbnMaUjwjV8A0kHCIV19eNepw6G64isgC_BhWv-LkUPLjdQcZFnTHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/terh9zo12HMSdXwR73TZh_xd9sQwLtPvlYKvr32jucnkMTJ_prQJdFNL_V55PF71ESn73bPbt-gPlSFwiSp-9FliWwIJ22KshbO7O17DYRrlP-tmaNkHsfWfdDEjiPOwz8nSFqm-O-Sym4NXUS0FFEw6SixI1zf2OCpAeISChglo3-9f-c8zpGgGA70dpQm8pwHoOf40_emjvN1VIIX930NPf-c0apReXYMoTP6doNvQCNYQcr8GHelh8-AG0Ohhs0DWHy1dcnEh7BMwY-TvVPshJGelFxFLRM-hz2FbzOKANMyM_rCtTfw74lUzcUPPWMbk9ADi7EV88bYlU2ag3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 51K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

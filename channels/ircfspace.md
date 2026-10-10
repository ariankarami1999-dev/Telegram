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
<p>@ircfspace • 👥 97K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 03:38:05</div>
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
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/ircfspace/2662" target="_blank">📅 15:16 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2660" target="_blank">📅 15:03 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/ircfspace/2659" target="_blank">📅 14:56 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 53K · <a href="https://t.me/ircfspace/2658" target="_blank">📅 07:51 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/ircfspace/2657" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/ircfspace/2656" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/ircfspace/2655" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/ircfspace/2654" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/ircfspace/2653" target="_blank">📅 19:38 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2650" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2649" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/ircfspace/2648" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/ircfspace/2647" target="_blank">📅 17:41 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C08UdnibxmXSp9zB1YtvVWGnCySElM9V4I4RpPCqNnl9tU36jv2Kqhj8b1E8N62lTEM_4dh1kggGURrHGbvvAuh8Q4O_O9bT54nnDDYu12B3-X70W0B3yGhhr6AbnJRiP2xvi1YU3HeMrT5M96GEcGa04AjSCtT9tIZH9jKIj-fXylmPI-5fUlMbdl27mJtMJbD6H7Ush0jaTa6xs2EsQ2IVGxSRFTXA_YuzIjhR08R83rmDBgoRY8h_Q_UnwcN4rwZ8rspaGxZTv09NpMpgyDvLLhMY_9H2pTH4MiKWs_VAFGBdfQHg7wZvRyEl-nJQUVZK-f8af4UlID6PCBBxcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mj71Kh-8-VVTyMuZ2b8WZ5-Eop-bUkAMD9Pt9Jf7z8H_-ZzqZ0QWDhYnIOSvHfkniC6SP7HQ6oWzhlr88baX5LRdjZjwdtoQuDlfVz8_K6yaKYO68D-mcygJI-tUln86XRdYCMWFBqmPs6OGPvHToJv9_hGtvaMi47imwPBksRm8OUshIm5PWOqIiPyeEotr5L1WQ6xCwTrVWdqLK-qg65U-JeRATK_3U3LQdflPwbBfW5XVj15JeWxd1j5DSmtD-P8i8MAJinYW08caJabeDENE0bJbXHAA8IPaHEt_MBqmBnpfFvFWuzmkhEgmLgXZkzhtTNyyxQ-30vQ6IPK_zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L_E2JDU03kWcfSkhbpXtdF3wK6twsWrueCPM4qW79QtgejoPXsc4_cKaip_64qUSDfagNfhLEZmMKnzN5LB7jAKkSrgvcsR2gU4FydJjXfrM3_wY6P3S6W78pzjmskklK03t90G7m4jA9wXmGACHlEbLt-Nzhr3MbRNNy9GTdOfnXDIOwM-32LznQ2pI21-xUiUGllVGLnh_8a3p8sdb9dsssxyj1F-AwiYBqFn-6TCfMhii6gf8B3Rx4pAppnxZgJY5ZowtV1rD1NWiOGc8stPtNzXM_JMXMMN5p3U1rzMlWnQwaTItnPPVUB99Y9zrczyDgHC5TLrhP2RNf5hQ5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FDOcIcd4bGgYP9QRohCq9dHtHPXrG_qnIMqU_UxKwoj_lB1qcfUCPJOfKbcXSeCnZVyiQLLnuGRSTSgjWC7pjJPNPB6NAouqyznLvuMSdIrUfytSuPIMI-wdg6VGV4RVtb_iVT8PE8mqAwz4AtuXXYfMilAz0K3SYw1zYBD0eUD33mALlm_PtpP5Q2xDPTOS3qos3DFkYmQshmlV1JDPXj87aopR1sQj7gzzXS0I4HjlCdUzAx9mc-FdQb7zR0K1Rt5FMVbZdTsHIsiwpP7a8uNBjAtt50S40C5UJ6kpQMoznFCz9706esaPQ5YgBYXgHvYO_5Zdb_BG6ZwKCTFgPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W4FxCtL7enuYVqW9RdZioVjFpzZPyHi8gbeocwYbZzEGh7w7ihGEitLyg2hcl4UPSDLrlXJEs-xXJr4rV0cUPAk3KL4LbgQzQ-4ttKw0BaItNrlE2G3IE14vzpWxy01jdGv70AllbUY8Vf-niHKr0KwK0cltTTUxaD0QJ4SXb4bcMUs5-hJ2QN72kvSXK0ZVdIY0OGwr8PNF1Yq-NqI2vjV7fUtVMlwqax6BMGyVJ0iekB2uSmLF2T3tfhuiG_MQEEnZCE13ydRGL92DEE7cqJoJxGP8ctlM_r0gJMe-elCy6wHoZF9Uiel0RVSFDq8RpzVvPAO1BtOtOuZoXHr1ZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kTAk0PP7SlqNTJCTtGBgO0voJs1zA1efYlM0Ok7cB1d6n7FJpNQ9gH8Zab4w-qxEysuHCza0zP0QVQVMYVf-vWHD4lC5Rgz0lY8rIOFLRQ3NFgyFOG4k1e3-T2vSduok8fcM0QhpLh04WyXtxRedflHhQF2gbnlBXmK-a7q98eNJ8OwhP7zPM6cL82lULbcG2twJd3t-8VMpCQ1R16G03AMJ8wiSHenVOtbEwclwAft0eJ9zIy31UL4KGq5H0CrEdyokGc_NYVl02vzvj-L2wMG-_87CINHLqTQPVHIEBan2ELYHwlYGi1973d1TwiGoC4MUqTyaQ4_GhQVidOVN5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AuyhkG4uOmjtOJQtITbM46CgL55-85Or5Ubwi98_Sinm3ML-YTTlDSVm2U9JjRM7bYvM8VTG5ItpJVeJf7dGW2ikBjbgRE1IqOumDnZq8lP67Vd4ttfiXNviemQmx4By6qXp8LavdGeIqBjJxbg2QS_O3Gwtbifm0xLb3CzrOjuhnc9btB2UeWZqGiqn3MUUR9HBDsaiNU69fnJIL3ncwpx3aem9zk6arzkjczQL1Hdye3P89xoS8Z66Dkkda70drq8fQerERBFmz8-Al2dZG6gRlzq6KpcD1Psy5zwJxB5-StbLcS_BKM46Tf64emZOS1-NCMOVDtOPN6pT0Ci9Jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nv2AHLQxoBa2ZIRm7_E96UU2o08YtN0jgDBzFYlgQKS0Qv-9xm8tCap7McEIvhGUseIj9ohqG9PyIwEaUf9uQo456pr_ww9dTa0wMTfyIxl_ecXbggHszmcfKiFZHKjA4uPx70_dkTOy2jDjdVjs68AyFWD1jrJEHVHtcphGPrXXKCdXmcMo8x3y907uzDa4GhuDmd9ZXSgBYw3WHnzoY9UKDGXrCVEaOX5ctBWusmyxRVTMAlrjFzYuPvzKz3YD58-pjolnCGsX1xqbAk5tDGURYjmxMFpJPMj-hbfNsWWLQ58rnN8s35agzFTWqB2EcoKwLXK5WQnD9f5797Y5qg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/StBwI8hcdis0RJWZZJPupE2A8lS1_WvLqrLVjvjDko9nUgNYVXcZfZGw_fjyP9yfBF3meSTkOzWv8iPgoMTNct14erfQYYweuoNidylIIDEjQQyktdE2SFo5rek4v-h7VnmDx5rbzuczZSdIiI1kDgxSUh7w_dgz6SNlDQkr2FBV9zRD_EGDRcOM1DvqfomEDRb2_UAk7Xz8EUlYmbm79lZ4fnet8N5l7PIjS2j2EJw2NjdB1HQzL655YDovqjfFsSKbjBnuahHcZMHTer4qNnlgegX-p_at3BZSQ9URcXmrmJKN-3b33Sp5RXO2RNwwAr4NufP6xmPthtYyNwFhWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YHXVTN-K152hY3NUV2tIXB3CzcpQHzGYzv_3Ib42CL0dsfE1FMC3WRlGkxV-TMD4KuuRKNomEQQCj3hN6fk-MenjJnIXWmx_mROzM69l5XCGgs7jUg6hglJtUw0CSSThOIs5PViyYiXkBRg94u1LcFG_2Ps7XXCBL0a6rGyMSb6skFfyUeCdSMF8wuJAWjuSfjM5NxUMmTo4cQ1vxPONiFVKeuJW-DZQNxEbsaJETR02gaztAz7DNPXnDQN5WUqTSJfwfdcN2xLomvxPw1SazrD1BkozycYVEH0FGpNbJyVy9gVTEWdvlHAWYz5Z7p81G_vhEVJDHcRkEqXZfSkHxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bCkoRPxR2XKmOPPvmtHuNK6HDpZgpQ2BUxrIsqenDRQXcga37mpDdhiwvjJpFEwvKG_RDALap4jGKZfFiI-DVd3Mme9xmRv6SlkNoBgijElmOaxy7R4XwUB4cj2G5J53RUYSXSeG9nMKZSXUTEUwzhR7jMwNvl6cNVlhlOYRDKLNDHgMPZjIa-uzGE_T3RUfkkB18rw4I-43V806cYJwByTRDnAlgZoW3QwqAZcS0UqGq86YSWchDYNTT5nym8hOT3bXGn_jtuQCPLXkiCIe3Kbro0D2bGXmE3P6L9Zp9ln_W3DgHaWweIgXOuA194BOMSwVD43hosW60hOLX8qWGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k1lpbusQNgaOp1jimsSTGcYhQ9Et-hTlqiiwJg-u2csajqdSX9HYKtsigFHSyYkGCB68kxEgjV_h_6Vh57pf5dT8sEWv4OA23Am9FLNvb7IBiZq0wS2JkANDLJuSJExG35FJUkP2tk96qGcuAoRjG1EVdKH4_M4C49iz8oWbLXyG3HQbmHsGeWsitop8m6iUb7ECcxp7-96G8OJ_Ku273OAuVBYMRjwqBNiDin1_Ml-Z0K6lkafJmMeLwWKjNSFBkx6op_GUhNoCAYavhYNzFYtbWsnxQez8vCMrNI-kD8aX4LH2TU4wmxCtEftkE1x-Q24blcMN1POlEB2wIVwWVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KaD8gpJRtjLFC2S8q8HgqAurI8I3wKhF57vb0Gq_8mlc7sasZ_cGPHu7w-R-dL4kCMyhlIMoYOJfWccd6gw8ugsrAQN0maa_2oDVLk6aUBAn0R-6XT08SobTInODmsf5C4XpQHZKvosKVfcO_GY0i9DfKmGgBuKcz9-mMcKovn6HISq7ff6pon1ZALA46uoJbx4iWiRmaz4ox_LgDrCBU4LqyNU3-_l7pTbHW8AHHvifeE5_y4blxWyIAWMUxVkj4rCWRLrDMm3SeTUj_qrczi5zDNzC8gu4n-xVgygkLE8MsXFSVN_lRGQJMYIqtYi25qwdwdDPP_XQP3MwsjRd6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OAYw7IqJbebVZzsa-XmXG5B4Yolsy_y33i1vlJ1PwY0LmDgIRjlCoxG1r32quQDu2dup7LOd5qnu1404pqgTurI6iiQHPoMJQmlRPcy53n1YiOfLixzCgJjcgke53_1YJO77W6iuFAdd2SlS14sh3PyFxdKEql7SZMiVRRZ2pecnKFMkaIGHDmhU9oRC9hOHY91Q8f3buGMaFTt_y9rkLdxxqtpdzHzB--35eVQyPVJr_IpIHFGmnexS2TxYv3RulnCWTyaKZbNZL_QHOAgPaqKNBqz450JaO4Mz5PYEB3MUZuSeDXAnpuLihrkdspzehGUoaxUarLaNhvurnc0B4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q03QA7v-kBzNZ84jrCR5KbxRYBlKU7n2l9yxsLKdYdhiHwbttYkAKR7G4OWY9NhMF79cues4hdGuKchky22YmyL2v8jTx1CBQqIHUaluADUZ2rSiAMwXIVq_JnW1LbcHpQ7CuyVkPqDpDVcj8y_2GA-IFlYkPDuPJkyDG0Mho31IGbMc7jH-JCI0NMioCNq1r-UKbDCnjkZA0HaOZmuo_T4oN3drQRggLlBX0F9Fb92XqJ_jR98ACmxO2Nl9EC9Ce-TtMEw3wZ1rE-Pyz0E63ZZZqox-NCwRCbxJclA-x4RS5ZFll7tm3tAZasjp0M0m-8lnrL0KuFFJ7d4GnewJGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h1vsokS5E93izSeMaEsgcZWAdhFOHbjNdtA7GCE_d6Hdr7HMpF8CS5y7AgI1bFRppMj7R_miPouCQy60e9_Pq15vcteyQ59vEqYbTVVxSfCaHCgtV6rxXYu-8-kez4QVSppE56XQxyvKP6u1Q0p64LwITpJtqfEH59u88JPHNdbjN9G-XkiAnQntM9xwa9DdGpP7fVc0IzbjDe4CSnYsPr2fI3MXCPJQOtxPZ33uoNhRdkQ4IpYOcoeQTfutsIqwCSfXprD9ioHmpCCtHKAlCzczh6MTdYAXaEXj0thkqfA_aqqK4NOeNIdKrhPbBZVgae2_x45KVlNtZeT-7F9MMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gNQnNMb3sbkHzCucPzrtWL1ySrX0spdTgWXYLNd-BLNi5_s4U1xw25Qn5X6T3OkFFXZxw8wd9WIQrzHuJUbHwARFeen2_HCPEWdageGCg1Pp7g2-1jPcs3AUpSoMZcFvUI9eFBRiOTz7P2gnW9SS3Z-RgzK97zMk8jP8Q92c62NLhBKCJ9MKDr331nM8BBMmLrXFW_8ZIhHsdtVVzeb-eRX14cGcMGbzkoe3sMCth99dvZ7862cbJy3L5XGnCU3jccTszJ8eBT9LgqpqQ_M-UytL3rxcCbsbiIUkQyPrUPIljIR-zZJnnAnbNw0cR5LLld6h0q7zfDqgEETYesn3ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kpPjeNLsotOKSYOoIrlGcFr4KYGF-U3mY2PUQ5W3oN3QM4ewoPt4mZcbIisoUUml1qQSVc6am4R-P3cqR6a0M30NmYtkZ0dFtxpkuEirMZ-jLuNb_y03wZVHu-0ztvheOklcElugKHAttKiZ-oZcHAUJCE-7xNUdZFzSy746PRlfW0xLEjFKf-ZqPUWV-MqvribTrC7zlj9cbzxepuckZ89MS6IjjKEe2i2Ot4jx9IVxaqEIMf86sviOlhgZW8bXGBA9uhevH9nxP71PW9v58mIHb5cfsHsNKkzi__xQ_7DjGaR8MB-E1m9GdkbE33eVXo5Lmd_lEZ6_UJbjXrmaNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tpaQWlegRu_yK27qe-vAlZBwQprU3mBV9F8zsfCinyky2FfBZaIiksCq_kj-JnmEdklXQD0lKF8GiKCYWzpNZhqkmLVERmvgDP-QUQAENuhrQGERSlj3bk0bjR3dwNCCICedM5L5BPtXHcELvHhICXJFOm0n34iLfi7sk5oeIu7iax1ybP6t0WSJwvDNq73Xl1gX0ylkZ8JpofRQr3qlKhtyiFgUK0N1ob3tLNFnoSatTbxyk2XGvbDyQH79CWlnFiAtTR26T0HS2mXr_pAa7I2kvw0OE4VJxCZFphMrHmfIRaKZcjOfqHgPpr2v350oMKT5fjajwwv6ufCM2K8ngA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nbkE9wwmo4QFjcvhlG0D18OzdTZvPqDC4dW_KzHKsNCmw-Gapt5fNoAA7tmTRtET_UYLL9zOqILBQLOyg7gjEfU1J5maLzeAMyVo4iyrrS1S0vXg0RzfnpS3UWGPw7rxMLkVwLzObCfxJl5xPoM-T1uloxmILSGoMbiZTpHW7xqNCfdyLA8Lj8sShvrwknCdaKuBIU9I6Z7dEIuhZDq2gugO7Y2tJCBWNRm8cl-UHkmBQeZ8mD4Ft0HHATCbbEJI0AUF3LM2HCupqZ5rAE93_wD1b8XMzagFcv2N4_os3VwRz1mcdWqxZV3CGOIE5UuhH8yLmfR2fXsWUrHn-FLXLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sTrGLSc9by_SemVRzEk_g4dliDkAjn8rgHj0hN_eA6Kn1IsJ7Xft4p6Am9Gbh0fLXD0mWtJ-BGpstAmG4beXOufV0qyOM3DdzEWKcD68CAMNNz3T16vt3r7zmlUYqcHDb579fz93HWw9ofMPs12hbjq25lCAbPi9M45lJgrK9q9N2bI-tKg-KOI2RgjqC0NQxpAVI_FS2xurOV8AjNDmcbEhbIck21Mprk90FrDahdN08_7w6i54UeqZlrA_ZwAP7YQIMhQKAQO7xeeayq227zHy5PDU3AIqagentY0v-QB5kL8x1ov9vGfroGgGAjsN9_hV8Hld1uMO3jTv12EETA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VQ6VZC63AbaB0b1ADpJYRwuo2dR1SR6-LTS6IYGvowV2c4hyhXxFKoh0wrfPaUwxQb5U_Yp-QdMaFqYCwF0Z3CbHU6LEEazyPzYHE5UqPT0n0qQO7VT1g1FnSTmsrsEgpIo4gGjChzL0h204wrIsB2hmMD6k3FtG_LfdhNjpwIcikpynje1YBSlao7r7c3RjyF8xmFiKIySYpk9sxExxMUmywunhhKmlaF8H7DqqHGIbQpt4rZrONa9Ph_ReneFaZVmooWCqJbk8B2nAM0Vq3TmTZNplivDreYD8aab7yOGQmfj6qAOHrybknNR9YnDKliN_tRDAwKdzUb-PMTGVdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PdtWFvmiqO88nYTGQfpXFHdyRo-EOexjJU77bpnxZu0SDqbyENc0d1NAuxldY2wl7i2gX2U-xl74cz-FAACD0wS3euiabMN0LqTqsb7EmLq1w_SlIqWwZDy3YkIZOFWurt_SvKrekGJtgpRWhWVUCkliWm0D4nXAngwTCaIWa5fN_QiP1NNQmAlL2tXMnGG7ib1XYUVunMyVw98D_DP5aqQ2Dk2RK0w6IxRyUtDcFM3YkYnbHdjL1wRasDOF4TMTH-PIsFfpX3iAoJvibAzyF6tAGpTYCq6MDhOOE9O2vA-E4WonSb64LlwiOrfad97l-_kaPTtZJxT1R2zTsisYQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fsExjhwbmPzz60X_CG05_FeMmm1F_0YHFFDxdeCj-5Rgxa2tm-I7B7Y6rhScRs0Rbk-d1pkUczFg-9-mCepcQ9jZhfaxMS0pEgQrClMcRJJ5E2K-sLjoGqlSK2Uzg-uToQafXvBeu4Vol6p1fU6w0JspQLXTV-jiFwODH0aUBTzznLJyElAaXGBnd6IKZNCOue-oQwl_v88zouP03EXtqNEt4kNtbg1Fngpq_0eBdZkYVpvCBR1bOylFRk_nClj_t9xs9qB3HOMwPhUOF5RrwlDeZXMqkl4FvfHy81_ANNXeRRVsoei1I_y-gPrr2lmX4_pnoCLymdZEnuMFe9wFBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/onhidafWxwaZXy5fEvg-P6t2p9n4jzEzKQ1332F7is5Phv3HHbBosFOkLBPKSLpPaxlMcx1vX1nldMxgSV57oMW6h88xKQF_cqhq8OtwI9Vb1AtzbnxSp8n3TXvFloHnDzN4UWru1B6ItfHlwvDmaswUAxryG6HbyCJLqC2aHobhDAyVmYTIunH81fawtSnLZgcrXxmy-hY_f9Ih71yUtrZ_frIKOpi-0atsdICKlYs9ZKcu4JgwDVaPdIMpcN2tXF2t_fjmroT1Xf_kdsRN3wE6f1PfemttsyI5WEcVfhj6oT_s6dQN9tPFbfkpIkyCwvZ38Mba4VzPHxrbYH5Z_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bxVXnycna8zV2ZJWf7E_SmWrXA9hFA9dRxANW12GVI95m4y6-FZWvxXQQMwCG5Tmb9RAwF6e-eMr5XpHhgts-YPR7SiYzmIWpCtYEZxaap8lKj8JJ_9H8Sfb7vZd5as6W1Yb2yPS2cVM3zaLS2yXSlhi5WT1k-9dW5rnc3w96R3xdrwnm_NvUbvJ4VM_GL0ryRo0LN5F5bTen1R6PefrRK1o55C4zN_wMQhljFxo-u1Xia3HeVr-3ry2RvEIYqF2ejBudfLlwfV2298HrAGTEDUyYWkHwiFw9HkUD-ZRnl_dSo-Nn_5qxtZTLD2GOsnO7tsZruVRP-uhmqrvg7zT9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/icIZS_fVN_F57wMlQ1FA1Q90LJgua_cdooe5oE5oyDxezK2gWv3ghOzzWWNmL-JC1QM7WgHmFRa2YWl0U9ypzUdYXRvITomZXCY_ERfesbwVEjROSqbVQOERAMYH84i9xScV5672TlkL7Tm7T5ls-6PjA2YJj-plLdxQg_Lj9oX_HnGPvMvAGa8LWzPFJTi85T7qY1bdX2hZASiOA9nYI0u6FWANvz6ixyX_ajZZat2HLRyIx6J11-f6WHPsJDLlhHnUxSJfUCRwqR4flIJt3EbWHsoAtCEyZHFnN-3VmgAIhAHGFOlQjcLtvrfgOqKqRMKvCZLZhz2ygEgSEEgLdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iAXaqYicgPZ1Zjv1NoNAUIwkN5CHqDpbuf1buFtpWFhIMVpnlkjO_oTjiAemDa9J7WCIbEydSWVJzmxbsGnI0DnQ-I6pXP6vryyG_4BB0FJuzhtXnUbRVeULL4mw5jOL_AlzeTvbPY2ll3YgP_fBrZ3uP-Z-dCGmidoH76tVLGUTyuh2r1FhWi4vycFGwAGgZzembiAWp8ipbedLWuMW7NcGpa4dmRW__Bi8EfovDQEQHGFYmowFvsHPHYJAscsm3eIyF-oMQ-9aVcuF-YkbpKB83DKKI3IF3oazhwOwn3X-RdY-Gor8MHTtL71oEw_uJnYrp_-vppYws0HShYcbJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C_Hd2uslxkPkaL9g_3TiddCcB7b2ZyYp7MII_xaecPcsECC2BYiCS3OSeFSmrcF078dNzd3pZdh_A8u0Oi4iuhc7nbDKvnfr7C9CjClUh5O0lw5DGgepFg61FuCKAOkcCzMxSjgDB8UBVK-CIZlBaZSFCzDoLQ_Ny9fqEvT2QnwPtqlZEyhSxfa_9RFwVMcGkS-AXFQf27BaXHEha40LtH6DPMJC2tkmPSRLkVj6hP_AM3qfrHmnJaiXQAWq3vFa3i14MOr-b9_v0Sxkf89woqg64-0W3rNB-m22aV-ditcITkjtLFrhGfvBb91pjKb7gW4p9as2sbHyVn1SOf5SOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vnj5-FMMBts2TQ53b0LG8JCVmU4rk-YV4d6KlDcAexq7Nmf1CDQAHX300n1Ki3XD5Z24UXbJqPzNre16OHXM8PrDpLiTQrn9NvMx-drd_h3CnwX6zJDHpJxfAeQbKOvYYdzN2gNEleuCxHyGhfio2BCLy2qP5jXcL58VEMXKRwUi4LGZvwhSEwUcLt9HrhVroNzTgHh03wGrRXA1dLb_Ocx_UGkxctIP4V3ATk__sZLsAcIDrrc5vPiWILs80ZqOHyh28y0bHGbkznrnnDS9trWwk0Pin38MpjOSB9nmdRcR0shnoPveeU9kLg92l0VHLOo0Zrrd5W90sfo5Fp3zAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZM-BcQzIXWsAyOOTwGoUDmK8PUVNU9-CezH06MZ79dV--9un1BTRg7qNUlVNnIacB2y2lGC7t2fmKTSiTVG_dm1rquULSGiJR_x7B_izahUTHJQeLbwGik0hXNwvZKplg1fxUExDAG41Wof4vys2kIerLYPRP0MN-mReTd23th9yX2lhuBQQFQRnxKMoWre8rGn2MJNTy0-AMF0BnQ85lgF42C5Vi1Jp1eHIgwbUMjZJP02c9SPLBcGQ5ZveMkPTTozM5A_7gAueb2J96rkwUHJm5Hk37CwhZtgEC4svNANPsFgYvQ7uL5n95uJ8DecOC3GtsSw7ZR7MGTucBsFyfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uFuXHZW0KmWN8BKxMflKoiPrnYSDIKSFG1domUoVd6lRxkX7edIDnGjbLUT6I18v75hHtPKssSkzNCIWt4314mVaiCiaTsQwNZhesNYxlXsfcjGWIHOyMHYpfHZM5JUr6t93v4aS5QNEnr04FeQTu2quDavDUrZaBfHMcuPk3WlAXce4Ba6qci3fiUhscKtKoOM7fFKLOnQRBlx_Lv9X0pymeeKkr3NRN7A7PWcvWBcd3M8PrOOjCkHdIQIdMPreylPYKLa7s86JrsbWQR9CHOXe8zRksju2G3u94G3whGt0pIY6-x55Rb6v_5KyrevJReQRUu7yJrBBTMLM1gVOKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iRr6a1Soq9mums8mNntzKohsKo4tatvtTLhCoKfCBzJU9AfvFq6KChjPgMyXAobdVXt6WDygKyQMyQiUY1Ln6L8ZtgZPASMc2SNLGaj9mdRFOhXYS1YEOmZK6kqCNDrD7BC4DBQObSadAEd6c8Q026oAFLRXkf3Sz1FZAuyXRlVISMmduE44hf5QaNqnMemn1Dimv2lA2f1OYVQxw3-7m1y6eI0n-hWk_MDJ8Q8hTFsue8Oup8i1F9L9T5dC9equvdSzYlgw8srpiJmRqfqgybCjnbaSreRTDnaROqWlvjcIDiYrDTTjCSg3vzW1CQeJvqT2SBTe6id0dFwsCA0p4w.jpg" alt="photo" loading="lazy"/></div>
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

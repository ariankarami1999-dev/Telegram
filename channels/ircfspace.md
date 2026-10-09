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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 18:54:21</div>
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
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/ircfspace/2662" target="_blank">📅 15:16 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/ircfspace/2660" target="_blank">📅 15:03 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/ircfspace/2659" target="_blank">📅 14:56 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/ircfspace/2658" target="_blank">📅 07:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2657">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/ircfspace/2657" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2656">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rG2YckQjBjt5tKZjskMR8T87-iJgYrn4PSsUs_4tesONgvB1i3XXQfTmqpTx0zikyVXvZYvcBqpCosrCIzFv48W1bHAOTdBM_uYsf1OANRc3PTvZEDiWMZZ3BXESCrE6vbyRxvPJuMnIYJd3kw0I1O8PkVGnKLRP2Rkt5wtQ15l9ueraNZ03jqZelAqMEqqiRP_WjJrVYOOSLEhqtrlH87hieaRESRfFu6JyguYk0WU87hm8TC8G79B3f5k9Po7FbKM5ncbcqkEd1z9dgIUhtROGfaTX7CQ5YCmD7pzAlPAXxm7SXgtFMh5p8KOsZrSuR9eyNwTNEuONwvVxxF7rig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس داده‌های رادار کلودفلر، از ۱۲ مهر یک ناهنجاری ترافیکی در ایران ثبت شده که همچنان ادامه داره. ترافیک اینترنت بعد از شروع این اختلال بطور محسوسی کاهش پیدا کرده و حوالی بامداد ۱۴ مهر به پایین‌ترین سطح خودش در این بازه رسیده، هرچند بعد از اون کمی بهبود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/ircfspace/2656" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2655">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/ircfspace/2655" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2654">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/ircfspace/2654" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/ircfspace/2653" target="_blank">📅 19:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2652">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2651">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/ircfspace/2650" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2649" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/ircfspace/2648" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/ircfspace/2647" target="_blank">📅 17:41 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2644">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2643">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2642">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2640">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MCIj1u3kc0wcwc2P0Oj3rP3Ex_b3OK0hNIfRysNym_rojhDkJH4116_RmqqkJQgxFixJ9e2cdFwcZyLVTlokA2MIRNLNoxHYa_oJANU7MztS_2gqjE3hvs8GTr_bKTVGtFbliq-iqJJib4bwntigA1s2U9tP_n69mKmFuBghlXYDTDNwtv5YQWXBEw151-gb-NY2DqC_4Zn-ktY2q3hUTGy2WD6QbNiEZlK-Z9iQlzdTAN_hFDHAckLw-pJG8StFiM6K2LKzx8MysDUeZHL1sOHuSqMn9SN0NtAzZAE9QCLOBgTsqvYidBECis5FtlOMMoF6PDhUAp0k1PtvPjYbpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 39K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JTpfxwcCQAvjdAKX6CLzBwTMSpbOJfp3d29TznCL7tBO_eT4s-h5Beq8_KQdBysixlAOVhfLyhpjf43HUwzqq1qxdE61fVApa1tIENKrbwxF7usIFK8GSEv90zoFm0YkR8ZsWTQzNMlgxxYetYEoKm_eNBEK5pkhSu0xunREcqLn0N9TKz0xcIcOiB8JQzdaqz8VbRAF7PetHtZxn8XwWIkTEtB-eeskGHHZHvwRU2fRms2JD_QDq8qzm9MCkI5jlfVK5qAsyLQK5p-VytHzC6n0bkKSCAUjmJllXhLzsNJa5p8YgVB9HVGreGK-nXzYowyrGvaZzBKRoIj7DU6gsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rH3zJ_n2gKLjKcSA48La7OArXIxLekRXdw8lwkniHoxp9KR8CsUxPcAgUGMJj6QSYTIzzvQXKScz7CNLeprwGxDHsqrKLchD2VrrdYYdBwGxvxms2ixS5NjttILiHnnEBDpmp3y3qnUE6lKfzJovfME6iYnLxi-iAgkO2B9_EY9akqP7izBT7w3GwEZ_V6VDVBSd2GsSGk0Wui0-ymOto9Ma1G1sGuYCkw_zOWt4ysUp3GnXwczoOwzmWBhmhCQc7S13tFxeQ2_ssGVW1u8MTReRzcKGX0uSGNy29bi_4XQ5nTk0K7YpwShfqO5mG06vzPUcNAMmZFzymx3QnDRePQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qefjEuqXfgH_vyCAshcIP7n5J7JL7CbfoFrF74oH_xNV5GaBf2y9vYD1cqFOwO_0kb7jMXc__MAPE1azeiz5P21M-SIswRuMoDXBK3Akz9NhRtOXeIN6c-l6MFekLASmfjmYVrK_Qed-HhSsb-sG5Fqfb5rqq8QZ6rLFbhXEZi6DjvD9qVXB86M3LsbHv0X3k6s_60l74I238pYcc5HIGumHoR4QkwwjUwOssCGz3Ts5LtTP93PpQtF_uRYT6Jt8nbCVa05Uzoclp_d32KdckqX9SPw5Lu5HN01OJl5NM487hY2_lkHnZNhJBO46VexQsc23CaQwm61sGA_miPY2cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lkFSM4r0_gipj58AN9g0LQHFthzqN6cXcbwNSQeiFsIWlcjSCGT0Kr6oKYvlD1ol1vJUwr2aLAVxfvCXamiLlkETxklJhilymLpt_VNyqERuAdjdQVRWvmbf6612sm1sd_d_PyQFAJa1YrsxQ1Pv3-CPZqAo6Gh0Cf9JPWlvz6I1DpLjmsjaFX7jj--LKNhz-C0frNARv99Fy-uQxt2G0cTBJTO8tC_q2xFvyDNAvKDHuTEdGOeLKc--yNitPpKxEojxZvqG5vexU_bbAJ4_5L1dLcKtjlfECheuSYlChk4n0bmP58x53dyl9Dott7NuFME1045zPtN-kWuqw-pn3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nvEjZUnQlkYBpOXdONV9WkFjzUF7P9IuW50CglzP2aYnWOuuSF6JjG5ToFyYgG-lDTnVu5PYLWcUanfq9pbRepi65VXfFN6Gt9yiYGCCF2Z579nJ5fmKgUv5cQR1rhUMeIMQARuQWKqRs3zoJOZaYBjzpqj1AMXwRJ1H5_5E24R4C6YzJIkjOjNPHUTVEPDCP05H2O37aFw1kQgNCEnq3-zMdwPawcVVyBlaV7-APaPIyAvmyjnit2VEsMF1QAKkUt2tZUnKXGeCryDg43mXRLxwn_LmBIxK7nl1t-85iba7vvxD8gk4sJzi2Atcziy0lRYvYx8yiYHxrDF0cknv4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/An_QXFt_TYUCv6cKnzUW0AUXndgUe_PBe3Dzo0MoIu8YGlu2cuHRrwmF0SRKmmVYel3h3b9vqQqovZMpTRtz3PNZCQpY0RjgGDJFelRd0zokTb-Gyk0h-p1odPga48KcKhLW2lvC-2Ku_aZGTw_m1l0OdIpyhAmTO8TreFy3HUrCxLJXSGD-_MCqiLs-KaMRiD4QRQVuTquG7UaVKDWm17UYAVDGZCIWV3FpnJSG9rezTbbFqKkFEc2PsRZWm_HrHvxbXLEqkY8LMS_4wkPT4dgglbw3e-9Dz6gfixA2VNkYaqyl88qYO13nIE69tPC9U2JZ3dKfhqixxVNmJgDehg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pHbu0RjxrOh1foHt8OpQs8fqHC6fdmu0-EmTSGaNZDjLU5QnQ3qbsEjAuYc5HX5HJ1WR0cdYnTo3OTAcHpnYVGZhi-chVy5Zj4tFGzaNlXS_3pA3vuscSl4TpmCtR7dZhWTCOeHJDkIWo05FjyRCKPKho7trLAg20KneF8J9yF4KyzqjjYYOqut4lT0rqPoKZ1cnSS1e3stTKrwvfY1bwa764gP0Kin-KqXiAR1bjy4cVaARbwnNvohKgmaPUi4zVa9j5YKgGZQhd564Z9MZvAsMv1S7GssMxLuZorXg8JZXSNYXVGlLzZC0O6RDqUXl7JcCIJ_ONv9X3qfo6BcksQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l9z2KBpskWKaYDW3cJwdoG_7rMf93dIeFqW_H_DRz8AemjHhhc4677yp6r-w69fK1NrEDD64NC4jVxDhXrI-7tIzSTY2wqpCJu3yj94ACtJiRIfx_Dnfd1NIqn2-SfWbSrmxIL5fo8gozmC4aaQoz0kJ78PV27CEjAgsneIIMj0Y3mrRWbWaNvYPGaITn-7o43aoDaw2n8aDRi1hnJOV3wVBNMgNi3wAwtvGscI5ICJoEBHFEhtvMHuljtS2OmJn5KfVVeej_paY8X7PeZSP3AlcAEgIvjYvi_hAm0XAjaceqDGXzcMyduoExLXiRQyQ9pqI2cgWzyE7Q5vEZPRR_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CIpgG-n3im6Mvsd7Jz2223AplF1YzOCw56YFY5VOl7k5R4UuncJs9Qy_fQEZCpLl4mp6Yc-YIyILqFf9mMbyySYhjkVjX5NnW1Kpttd3-7v-A_L2_WQlNyxia1CTEV1g43qaS7BlsDiRRLcItT9Wpj5nZQjs_TaVhSgIxmeGLaf0jqWU9OowW5nU8-4MdjbS6l5fE-1WZfj4C9vBmZ3JTbGJi3yoETSD4gonbrlWtFmK0Vs7uoAG44LpP3fgLzIEpN75adtTx70GZSckcx2ryOA-NXQfiKbD-jvTqCHLfFApen4pWp8IJeByKbKHJXVsTpje2p-DHv3O8RqAicuDig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RBJZJoR9X8Ch3ZqnITtErXlcZhFtUBCkiZW5oYEBJFtZ2rlhQSEkXOerL1MeNbMQ-oPJK32OGfDkvKj-yajkQp8QM3CJtAs4SXn1W5bAw1Q1LHT4cAnG09u5a7upHbvA2WLaFgsFvEZD8Q8oXTmfuVrQO27luSSzBd6DlzZSWEryp_JHtKKnBQGXnMS6WmZ178QvAS7ATlUE_PTdctdMg5deMpoprMaeA-rpB6zUQSMj6qcgrAmEHFzetKoBjUKe7_0Jn3E38mrH5j9ilYqn1BLh2OBK_5icSJm2gLsfZGA99i_GrcGEYdmLS2S04MBd6g2aqCVebvFPBuFB2EUgBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LONcSkbCmmbPxBwsgUSUNOGkKcr6vl25ki7MzV3LCRKaTxlypYtF74NKHU3Sp8vRe_SekuuKQoxnPEdYxTPTs-YnQtMy7Mb0kenQGaRHgW51Xdw6F3SDIPpcBzcsZk1Kwt0gwAlutaV9gXde3QxfdMYcd6MorB39h4xbvfp5Nd-TkMBxjWoC9dUms5pKpKP8kt3e34wzTfQpZ-egrRxyOn2h6t1XTBzY6Tut3PrUgJH74NdHUbk86KhOyyGjDZB5206ksKg8r69wJuLCgJ6FnsbY0qkauAy8WX6jRDod9xcryKTTlEyEzfSkZKM5ygDd9mAZi7L33IpU1ELlPMPqew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H3IbdWbz_PHUJ_tnRps75TOhGKfpazH8igqqAOsl1GJHX9CKT3rRR3Lo0WFnsIahAJdqmShHs7RfZTJTsYUUOFl_4Y5zh3_9M0vnClBLVdCvVbDPTlv3n8k-by-BUxzpM9kGRkiiDExVfwpWhU5rXqWZd5W0Y25910yeyc8m4tGIH4WpdvBS8fzVSxgWbCx-pC72T93ltuH34DFpzhpI0qFZbGgeNinfdK4MZP8Dd5tfEIhJxNB2SVVfoQ31MRNUCQMGDGb0n97FKNA_vpEpShkb0GZlKvP097uoJbYw1msOtstNT5kveEbRU79otB0a6MV3QPXCmlyZNK38EP4FGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F_niuPadnhkXcbS_6FHpeyhODWR3X-x6DdhEnj6OwZZLRBW73yy1B_nuMMvwqt24jf5DFbLM-jybMxBI284WdW_TiaJNDrYexJF_5zLaV9nMLsAb_U9j6tLK7JiE-pBp_WmWhMY0jcQGa_2cQSb03dLmMCes3MbHEY7S7MtHlD6VzGUBMfMe4hdOV1q6YMTbIwK7WF_Rr9gcb_J9UedILqNytLISNkQvJziYaVb36noMSr6RSmdTq4Xdp7M1boytHqNUXQmOLAGrECvxqEk07eilU9odsSTqOpofwF20L41hjpDajJRj1SJFNRrMgdpz-HhJ6UvLTNuQ4LTVuvWEPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e0oqteDGWBWhAnk4wu3PZTdo1n4czB-9wHQ8X5oGB5oKqkijFWhqGNRRAGFQDR3DfoTvD0iG49nrkk1CwDMhU8UZ_cLpWC1dAa0B7VD_n98ctPz4nzvp3Wd2A1BRdWcyrIeMsxxNrCbOUGoWgw5cgzn090SBKODc8BrgI4iGBDBsp9G5dHLsnhRqI2bkllvrqSMb-EmzDb6f1xVtZGCNio28j-ERRbFO7KWWXkIWIgENcp8709vNH1pXVLrUpHgmJjyAFjSQLUW-5p-aA7dZ9YrAT-5sklxa9whw5RHoz23vf0IlxCRiJ81_pCFec_64RUJJhngsWcny4NBccL2LCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dgKz7iZdKZvRFv5AvfQY8Xt-AA24G-pvZK2Ch-jlHFaGSoDSEyr8sr_XwU-tHogSsy6mEdLcOgH2FM2feQL2J9KJ7NlBZrIXeF-G5KfrgV2SZ8JbBzJtINqqZPJ0oRXexNWM5Yqr1DjR8FYdRwHr_7iOSHlR2X8IW4HresIEKOw8kra4yMyniQYAw6wXj1BXdTjbl6MY9ikK22xmBbNrjnEUKlRRQtVnUPR3eZ_WJZ9HsAPVxiOd_sg9JWtJ8sMSXst5kbN39KfP5NRYbybd_8GUc7N615wyPdto8NKnvzwJUNVkME1smHTbCptyVzLNZRUJCuQt7UfgA5WVzglgzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C33BNaelfZQ2bRqKjratFaU6jqVEfST9SuY9Nf1tBKKGDjdlWQkypiLgdmwDJUE6jXThu17-axi-TOcRFusAvBvywzNZlRQ55NGF6-Q2999hJjwXriTydIZsTnr88MzKqn438Pg8KUUKyCo8BJVIIJFaP6lyJnvSqqg7StKtd197Fi-q8PtCM4dXOl66PgmdLtySENXz5jWQ3JpOaV6FEyD3O0hMIkN6A8ODzb_f7fQsy7pVNDKipOeSzEzN6qFvDEOhn7AhXoQgyG_O5J2eTdXkwNHroSGKVWLOYqEzmS0VjUxjOGAzYDbIxDus8bYxYrYBhh-E3Kejkj_M_fuSbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bYWApfewUZAzhUj6PRxuUSxGIbqPrSZSXQWAZyYubHbeqsHA9KjBD7keeHYUPNdr6hkdE342SZe9n3LBVt_MX6RPantBp1ImsGdo4OAvI5bi2LQbsa7sCgpAPdn5QttpVQUutWrWO4GJfC0C15IrUl8CjoWXqdTttqOsiAPiJa-DWy8bnymScNqnwRm8TfB0aYR9gMUKfFuEbBLMuPNRZrslelBncmMjBNhvQaZUobL_E_rmj0X3UEjspybhdesaSpMGkD5UhCsEOOE8ZzfANvzpFqnJLtnhqkbN_9vDuT-cajbFMFyUo0kbA2CJ4ULYzRUeYXMzKHntXlDo16lu3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TPjrxDOkpEpYYHrzWYJStrT3b36uhN4g0xHHwkHcoRelJrTX86NF2z4u8hESOT48URpxLEtmySsa3gcA4P94ZvaebUZ00j3oXuPXArfAbStqMkLuxd3SUMGjIC7nmBz9oGYYudXthTMG33lG8ZNPgjvTTw5p5T1cHdAvntQrj0jDiRzqXTkIsDf92zKRjByBNWn1gvDLpOz92wLokxT_c76tWeMrGCY3bbXwf-BCnA9CVVGVrTl19wmqPL3mMG7OGAh92JPRQi2GVXig49J4q5VCYC3kWGmFleUIF1fm1FsOCmuMi-OJzlim9_eiIDZzhHe8VZqPuZHh7k4vSOkDHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X4xpi_3cCZU7V0vCAW_g7y5GrumNvUSIeAFXpkpSeEp048uK2SZspkzBY1eA-glY5vktthnkBqUWQeJilK40_ysO7gpzo13dyghmyc_8ih-JE8GjJ6KFahLteujZKblH3vZ9WP3LS3ECZhvvlPJeSr__DWVQqhBjtDkSxOMW9Tq5UBKK5zxcCYyTWAU0BVuLtwXhRjcDogx5747zpWAhssh9sXXLVByRTAF5V88eE2VwS4mGk3leCPNUUo9uKW9qvEbxul8o6BsRomXg-205XldnAiQZ2h1Hj61BoR-7HGMpM1-iBBrgJqihiybxcwGplmrOs-5lRQPAtmQnCH-G5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 89K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gzl0w6wez-aYDsvhgau8IydOPEjYpc1i0m-BujOfpv1wUT3xl_neKxbcYGjndWCB2EIrLKU8cwkw7JmCRbEKRyl00NyzmA3PByQbVfXVIVWJXEwhgThcswjwSdZUf3PI4_YArLTkydNx0puO-mRQeVNaFnRRYOrt23UkYL88zt4oLrA5QSuhcllear3gad9b-1RJkboyD56JA1AF-ezNNXM-09YLR7if1lrvY0VbaXuNiCCdLSB7RaqzOYDritMnyRZOyoPqcGc-563xH8_3VWIRhkplkBnE9frxcG0DyPRrlkk2JoZMe5jlzzovWxxc_-53L5PcUIIhfqY88NOdOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xn08vC8DRrq9f54tc-lkw5wagAmpAxzvKEAqmK_biXNAkK4UCNZptdCxC6YkXAd-Lvkp9WRhbPestziCsGLQfdLcI62DIGiI_WXymC3s7WqG70ccJzN09CsMkOenxgQtEsM_HPWq22bDwYx31MNg06rL7pUEfz0izYhtzLzj7mKp-FLH3Fqh6mpVFqfX6pjAY2enqVitFIK97eu1u06CMC9M2fcoNmaduxUOKea5uJE-uBsLqSopyDjdtkDPt4zUjuRLqcVC6DpgmA6OONyZhU3IrtB_amqUcwxicN9SRW8yKA9EAZwrK7t6A0aTT-Vz_YYn33kXb3TVNQx_2HV_gQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ohoSjddkfiS3HOamrcdR5ITPweMAUw24OZqa7HYVx7UMLFNz8kFKM2mDJB0LfQk9MrUiYoWtS4POVbbQgHv2-kJzdPfn6v3rc4pdVM4bale-q-V1DH4ECcZltN_TbOu3iae2MuacYo0bYUkk9z8kEwHKH9jJ4kydThy9SpOvIF6IlO22O3a6Ess3n9SsQXN4NRe3OnK-YYqlF9jMG7rbl_hfk-sQfj_mfk8NOYAY2XCglYIEofNX3ny9_yz4EhO48h3F11KK-7EwTdO36B3oBmEDpiRLbmf0MzfmJxZG6ru0YfuFLrqLgk8T_w0m7rE9CxoW24DOwGrjXTtJeqYdHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rPT0ODN7bimueV6qjo8rCYcrs3h9SEDLpMGTN3BzxJocH8HRnB0nOGyvL1wfY64IelA87Azv9fROIZXRswEPDx347YQCN5-Np1CBtXdCYZue0IBCT25KV6pAz7JltJ7m_LPRinZceBZTgaVGrGXKr0BLEquVO6zcGngoYswSB4Wil7khGNY0fJLTBOiivMrqOGLms_NA2w3qBY7ldBn5acTsRgdUcTxPBL1rPlo3z9xjeAGmZ9qlu_ZRvQJFbg0Fuq6qrn430i3GIWGY3qWYvGXxiNttweVBaw-HD9_Qa4NFOs1JAcq9aLBJla3_u1OQd3s4VZNMg-0gftkpEqifOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aiQZR6LNPLCKtoC40ULw-k3i_xzjdwufz0RQJxB2CZUdqCl4NLz6a1KvPHo-ve9d5nJtOrrpIoAHQINwiGK3zj8KreExXiEFGJOeeIY967gMotWyb6yGdQGZz1mlQD86mwvZedPQ4b8s-_ckIJsrRghRCKKN_bQWpezvyUBUqT4Bpl4yCmpeYZ9iHcdk1uNdgkxfZmJdANKXSo4u5t00gtf6zsw3xT2OPN7mnfD8S09P3ckinRsxBmJzZI2lXVIMO7X-bwf5N1wTevlxHF2QDidkYQ1R-au3Xs3XN1e1MRscTu4uEjZpYa-FbOXC-0Z5qaUJ4hnMk-q4dDAxHlgNRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T36nJ1ZhPeNnkOFs8PkCz_O74wdpw1CA1yboszywGGBfixhP6KGVkiyA4HT8e_k-hWSyr0jd2jMAsAWL3FkAY7yYBAqjTx7Bop9JsoofiTawhIrnA1L7iP7HjpNsmtte1SwBFoOw-7hwWPNj63HsNRdW03NOF_RD7v00i5vKovwiKdWALqdIgC4bCg4Xd5DAqQzrp2Nd4LZsixE8eC1k5oD3ctj-unplgHasAqpgvsZTBio-KRP8rEPfnJWjDFTEutj6mx7HKF5tPVlRRLxHWzaDWVC7T3LrgfetTGv24cKT_lZU7nmT3C_thJHDQA7GQgfAiWJXT-YFz0AgKWPxjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WrpKMBAf9IQg_p-kHrJSbkCryLmjFIaDawuyyS3lKPVUv5HCRODo7jeIXCC3__XnUNeZkJjCHLLxBB7ujFN6HgACBTIOHKxEF4UbsqmH6pFtP1QKuxn8UPTXoPKh97JlX02JVuGCHPkGYzshLc_SlrWaKieK5N6ycIgrvekrmMAd0QC7RG1tTcrcZ0B9cyJqJIu3tHUhs_wu33WntGOVmpEgoG3Y4BeSjQMxtQrx09W0M8yKWvsEuUVV5WWynat1UZXrTOjjaCHZY53mmgdZ63eBRK-Z-RJZqPzEZVArW4F_qHjgD3nnO_rKsN1fK0BiAZWdtJb0e9q4K0BducFQpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oExo8Q6VaDzssMw7SVeGCgXedsdVcX45zdyrtCuNWh92IRMHAnfb4Vq4yQpp70GkG1eMjHlnnP-uL3UdGaZvdbyHgRZJHOQucYfdyjUybpEMsT5r1ZBTbAxRE9EE-8msrgCmNCY0REoN-KK2LgaJE53WWAkkwm9qHBoyNAaNXOh3O7OT27Z-zfUhcYgY6317UzcLRfe1NXtTg6yK4wwdRRjPNGkWZxA5wESu4xMZAm2GlWtAbM6fe-daOB27tRbUUIAgvKvZDWlM5qRmF0GgEXXJwBQ37VYQHAxVbggpi535PZquUlRh1g8M0kInZ6okQL8_IYohANHsEJvpbe8xQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RSUnc0MF0tQFeSVh8k6wt90zmLtCtL5IzddIxGp-zgCU6n30XD3qYxypBN-wJq3fUYxOvSLHI070bWsbVwn4gQqjgp1xV19DOrPMBDHfwyMWh41jU4GTvVwYLuE2vlSyZDWtj4-XbysDb2bpw_XSe0G76ruYNChbHDhueQJ6-m5Lf7XadDEgu2kOXGT8PPApS932I8U1uvBZvRFNgEvdt6KzXSiP9mz2_e9Tx-2qcWwIYJ1aqLB9fmYYKavRZf3ZkcXH8ILBwX6YIgbwm4SftQp2y_xYmOQUAO0U5c8BgQGQJnClV7GrIgUOprAW_3efSD3o0OcXAlaNn4CJm7P0Uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aIS3KJS8mZKkPgVMmOumj_mqRVVAJYwLfsfdzXCuC51aVnR3cCWL474i6lWWM120biemTn_sP6XX4GTeOyWUwFaYfueVJEUDG4FcvWolcS3xy6Z2WSEOIBhBRuEW9VSHX_SBBCkehoFKKvm0RxU_zmt99fcLEDBN5oXHwhcRK4b3qad4KLR3Wr2Vpklt4pqEjGYEsoWBDUxAkgUQO6ZJxruWeXeFxLZ0HwDrIfgN5NpsI4PeI5ZDtRQAKdeSMrhd69q9thvCurVOeUOf2zFr3KIymMqxDNscACESQjYsUDIp8cNGuTGjSuI-y7ONbCZdWEvi6esJ7Ilb-SHCjop7wQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BAw42Tzr3oweN9zi1Tz-6epv-eflfBiIs-CAQo7qLczhmmXWza3gMVEfg8JjOj9mwhA_en3W-9QjinmyJjRAa209jBORszsDeMw4jAQmcq293nc52BVHYxeVfqmx3KPR2MTWxsM8V-RG-kUeTqLVZZN29cFKfXU8ng8h0_PRPawYcFfNZfw64Yy-6V1ijv3zlDnZhAO27j6Hv6RbChQC8znckYK_e9SUz-Gsurkg6tzuYlES_XblEB_Xf40nS0FobJyGgAvbfKPk41-TtMUP7wfBK-9DuGhRFJ-NZf9l3mKMJyzGfnkST8O8MyyyPoBwI56D_SdnRY3HmYIOY_m2_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uIXKGwsg5ELujt7FCHOnD9W5_JVdrkcP5JKXnOoKuOHx61hjB_mVMxGvzvEc4xh-_sprOjr_YJtRcdm-ljepjmE7JMFBXXULVx8xx-Xym2BIaKjz04rJObq2jnNQVo7NSam9Jmk8-UVNQoEy91UUEmSJKuubR89AdKoSytFn0l1-b9EQsjOqXDyIEK9NCUKkVhLyld39XfdCUmvlj7Rkc29-83v0ZYoNu6E9Jo2VIbmZuB37leIAgqr3J9TqDRyBSb910qnrSQYjcPyuP8SoaQhsqGwo_q64E88WZ0sbW3CrDGqHVcxu0T9_--AUKtEYMTX_H2FcKgvVLFPa41u2Yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KD880FEKfDtVaGemcepYMlw9yeOhxp3kZVk2fde5tLeFl0GSxTVsbBer8akf8A_w0R-ZuW0yQL5tnEb0XC77ruVG_Yp8kKDwoDMNUO_eI6QIxMkhyptqAn1uZtR9oGEfxhjlfHyLMpJ8H4Du4HlFf61kkgHbq9PO_m5Du14AIZt9fwCoYa1CaPtzc8GOTw4-IAPtKVEMsVxDZ-LSYwWlQyCqTH9IKwmHtunT02vZNvnqM-iwycN-jsswXb0ZhGxAsDEFbapvhTb4cGAS-g59ujSFzWbVu2DhW6Ex_LFsisGdDVCgFYaxc2froOOffGGA9sxHU2lYdq3SLIoKWy8LXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fzixGXSwKZopSjBgk1NzK6SlW1_4BVBjEG7pwPaANc61nEnUh_OlG2S0hKrvJ58cX_sr6AwwUOBa--VR7mn6YBTzNqpa_uecKqib4O0OfEtIq1mgBCTKI7JTdfBoDqY0pNwrpjc7EeCuGgh2HBWs6SU-VCLHFra86ZFcp4NWlBX4ZilytKwLowY62zgKfkWjAL86pUxAYS9m-YLptPU-rUUS8blVVQSZmelF7-3m8foH6nVowhpqd3B-ISEtSdTVlKU__2a2csz9eK3y6WeSzpg_sUWMQFbe5P1ZxuMDaP0GuI03-6dc_52nCZ1ncK4BlYBiGZZe6apZOWEt6wVH9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HR5-aqQHzRohlQFmEm6KqYngjWIc1S0ldhYt30wPLmoQmnxTA3wcDm66GRUfTJ6ay_DeaN81ZhMxaotpA02HUQLlVT4dsM1i9RS36egq6MW5Vqsp1ck50D4Sn1-H3_j-F7lL3nHx1VrcAenGBOJHUEx8o8cUy5PU1neMkhe4QRuVI4uQjPaewyp6HtF32hn-z6uB1SuyaLFndYyyxbcojt3ZxXnVBsfi1IltVz1QjidYLhfE4h-goVZ6IkJDdLwxu5B0k0lRPkUHsCZ9vjLGW-uGy7uqRFziuaVPrfzEINsqAvcfBOfei09SIVewWlkfK6ZjGdBDyfIpbpioCV9bwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Moslv8PgGun1tehA8qAW-DPGoNyNTt2djAvpdKcg6HweG1ltE6k1FR-dakofJP3Fbyu-kY9BISC02K7Mqyl9HoLx-teyHAvfLYrfYfgXQN7ieqbl-drq-RqRukQLhGZjRqRIAPPYO9FW8eZD6gzTPBvnQuMuRkOXkkOmPjyq42QUGYuNcK7UWYX5XwNKrynWzwEEfdyFqQo9Ldjmq_x70u79z4_ooRU5d4gTqst1KeNgzbKr1KvbiiolGhtV0gmg2Px12rSx4wDeBVzl-WhBBAHqRE1I6udbgL0jYn_9PZmLlqMzTrg-cqmwEiJyUxxQjsr2Ka4nIgIfTjhZ1YO1aQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gZSNT1q-luiyfnbiydbmtXN5Yk_BVOWqvBhAg1w6HcJvuy69R-aBAEl6J0LHfZe3DBtp-LsXpucUw0kcPabaVuIc5ohpdeAS7FxXQ-TN-g36VnoMDCxekCtxf4k2kgO2Z-B8sGu7vdQfrZOhRaEhJYmJTQEHKOAIHvowfx_2MTis_yU9JltYGPl23097z1urlgke7PaF-VW5tjRZYulTCeszFwNhkD33hkgvKccj-JnvRfAdX5uLKDTm58rUDDuA2g5UetprPVpw9z8ST5RN0p25VSS3YSEsAFCSys8z5-msOv_aoij7_CHiJMSVIH-m5tJwNDxLHpVN7xAlslBnmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j1MmAqetUqbjgHRovBDn9l_9MlUt21K3DUOPATbN5WnuC_s4MPC--17U96veZr69n_feqOL7lT-IqpO482E-tgLkBuZOxV1OsAyfmZ52AWZyG51rA_TuiIRH6VzJCRQO1MNaaWUmJPngDAl2QntDfW2hkQcWF8J_0Lq7MehRmHtCpzuLMbRw3C-p5O2Mkduv_gaMXlCgkkHw5l6nGq4cJqtrZ8OLS9aegMPE9sAtn6BFm8BTDQRO4F8-tfANFiqOU5OqpnhRKnHjJDdv-_F6dzcL5Y9Wl5I6z1D8ldQWtETHft3k2YLDsGo9f8VzPeuXZVhN5hmLMfat6SobNJH3oA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lOk50fZP0ocGMj8BkQh_AJRIdYr2jV8fNv1YF5dzmP6GoZa4uhA-3KsCG9WmhjIEjdIVCH2RLaR15w6YcGVvpIlbvoMECvsXFnfmxCeDPClO5apokYO0m7sVzyuu-kKat8QN1GIek5sX6QyUwYyx69JIyBQtJEKYNtu__6u6A7ix5mR5zyAhBJ1APcJk77uYjZQKeUe4VS8GiSkO7EPLkvkvrS1dvWNtvJjJzDp49ANnITtcuV3RbJMFdr4vR7kiAcM_c6fE3YbdnlCyzPrTLQMdRKQpjB_HUDtriPPcCuoQz7bvePiekpHFUo_AOdKvMI8J5cwkzYvTOhZsptxrLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f_C1oirJWYXN80KqcI-vvJQk-OoUFBcOkOIOeuAouonf2IPn7ZdImpXSEEEGU-utTtw7FLGmU6o8qIVzf9LwwAFmyAksYjk8i1tFUZWLuzucaLKlomqEh76KKXmAPDfGt8cv4L60TROWZd13rJ2iAuKmgD-RQte3uBd-PJe3mK7JBdsBS-pJaCsF_c5wJ26fyjajLddVcWRPTVXH4NWYvtydeTJSbJCf8m2WuFGc_GTF5_DdrSWvSgBKvJJVsD_8KO0jkRWtLaY6PoEjJRehqRUYqc73V43Vbgc3WFCEcE570HW-cf9km6eeFnUZiv10umJPR8PMcobY6x3bzroj4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eaYSXvYHwvqck2eczCxkvFYnkSDVOR0D03bNX8S1W1P24fgdSdihmPBdbyEgF-oZD9j2ayccqRCixk4rJG1WifXX2JrKHPog8sejMxUm9jzMyMy82_Snt9F79x545u8vsFCnvjwq3AbBCphrWGw2od-rFfH4ITgKbqpEXUrCZzHkREi0iRVXWYxlXlZCotdiTS9Rt-efsxuVJgvnEuKxq3CxJ460d-IRmH-Uc5tujM9bvRjWEbi64XdI9VTiYRp-xYkmwBSq32kE1WjAdtEP2G_e1ftpl1sZE08-FcVV97nMqcWAwUJVbNawtFwmrNp5z6jCVM0oSOx8DfUgkukxoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bcPjv3vnZkVC8GPhU8uM05uEJe9_2IZdgEB7BkKxxY7Q9zu6SXWvSj145Su-39Ky_NMZnWabqG255TMSTRWEfW-5o4omOXnWhG8AszG26kZNDaV-3dVLjwTuAbUBzHO3maU_fSdvGoVcRj5TlnlNXgeaAU5Poi5B-nu1CFuXU__dFHdnUwhZ5aAr_qcTcU7AtOR_O-7Fx-ZYNToXu6c6cFwto8t3Zp5X6SRahKj-uLWg45VRsYy-gH-PmkdTeEczGEcL4FWoVcP_AxyuMCfu8Jy-24jhLcILK-Wt-ssi9bu8709gNzuCiP34NKmEaRfjZjNc9vyzMOSRsfjp9fNhmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aW_vDljGT2Yyo4C-0f2ufJtmm5NoCoI2YuwP6tAj6qLR6gAlrYI-XrgTQuqo25YI9-OV7w7rFzRyVbpB38NmAjO_tSm2NKOgeNm3kyFfpvyFnLEfrwAxRlw__67Id6lM5fQBaVE9qAJki1ddbTlS6rYHqg-sQW1YRVi0c6KeyVucp-BGPORSItKYHG2D8vJOSuJHQnHpI0PCOwMe18WXhKT_FaC09egMyfG48euFjAoUq-zoL-U4ELIckJqgZQZs4ZXoYDFW8KRxKAcFjT8xNw7U30_lpokNkkSpeXzzMPKbi_n5-v9gFfmJ-PJOhmQrV9uAi8v5sIv8EVaRRiWweQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VznYRQw7L3dC3bA3vyW0sz0IiKg08yHVD0UA3BdMd_7Rhyqr-lN-nyKmDDBCGv8RjG2_sL8qUj_QcHhfcnn1DTCXgBvBNKQxZbqt5JxZK3epA9DPi7K2IYFh0OFlzVgSXUrPn2SDt9V3ybGpf0apZkK16E0_YNkAiHcYaG5-nOI1frDhMqY34t2bjMVxadhtbPiWtyw8FDOsgYMcW-cvQz8ylEwzKfSad55a8sPdrYXhdUws7mYar1GJPxuBYbYi7cF5qRne7fU9aBDSQkwsrChIIpUfmSZanPigKl6DVx1DsCC66COac_kFXry0NfiXB26GBy7hdRjPo4KciMuapA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RuDr5JhHbRXWdGgti66iLTQ2QxJkHoK0pYcMnOw2FN90UFs2jDH4Y7rCEyxUTOQFn_4QirZQ7h_pX6IXNpr1fqBGXt44v1dnPHjmDhCuS2EJFq6_2dkWD6e-yQ-vBDgajh3QZFt4RjUW2g2a3Jl_Y03UsxeBLTW2LgP0wRj-hLGZbh_C7tXvAd6auRplWDgyAiLtkjQ_31p5yJe8m02_QKisHWE8p_J8UnZ0CWe_26ZCviKHzLj66XeFLUjy8HEme3eQfEkGN-AOBfqiKnAjfxJVkfs-Q1ylwpzPDYvBJ-yrTcVKp8jRY47ghNLccxI1_cdzYa9yl7ttbqRSoozuOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hBB_8Hmi5n4OPpVzNLBX77thADGjrDKabWHRSKFGs_uTK7gkXLMLDWeGCa0I9izzQhOh5Lc_WMS_zqBW7QpheuY73pvBqD7zHi9lxUJ89usyI0fTV-2KoO8MyDlr6moSTHXQZNnV1cGOas4xlkJm8yAQbgU1O8NrEtcp5kncUl72aBtWO-EQkAcHW6SkkveLRXing4944jTzD-VlEy-c8ByyJyTk6P8489uGlA9gqvACfSMGFjt44SKWxaDlUcC52FrM1ozwo3WUxP1tjQ1uuqASwFHa-9g4Z_wWijpejfWOJYgwQaP3t-h_rDzw4tsjbxOT7kZmmZ0TVWKqYYRH7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z2RbfDP-wnWGJ2Lk72hJoHs76i4rWEo0e8SABdDx3pyBBL5MMVfccWGp6D20Ul0am-Ek1532Puv_PIXRL8f7GmJVbjfKH9iEBGhM2nBtj-IQnN4Gc4x_LR41_zaP0hsQ9hwKmRbDUcFhRLXKG8ZBPSRIGufvOQDG2Q6uKoJxPEbzjDOYeQj8_NWnVt4dEVRNBKRavdZQE-tXrvS52Sbag-41jAaikpDNRZ6Z5vWd8se1CRwg3JDLcmhtNdm0YiBZu-HFx5HqBoT3ayJhkOrPiWABENxJcaA84JKaDn1sm03tVnB4KdFJQMUB84sTDcKG6oc_qArpvxtofB9uLInnig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UPn7Wl4g7BGLhPSrT57ujGX3-PQF0oo1C9qnBerzNBpxy_KBGVyPk7l44pHzv3m6Bo3XjIY6xYbB0saIdbHVM-_H7pwf8tfxz75lzSp1sKe0ClcxqZ6PqmkUXt3GIaIMedeumOMqsNkbeKx1xfYyYTby4CWLF_aHULYO3_ERYJpqAfCLux8BEIxcrBi522q4zvr9axkWtBCcKPUV6QjQs7EmT7_lg0ucvCqTuLgIXHi_8pkL8Y6TCs_H0gni9V547mfbFy2cOcMi0z4X_uokcT0t9lyCpDROf8nYo6CcueyoWX3RUUOTv1L4lQQnWkKVJX-HWISJvPA198SipQQ7zA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/if1AiP77oAQshyj8Iy9u6UYlA-gySmejxx3vzGl9NHbstbs3IylZJ49DkZCsvQm4SW4tErjGaoeij_FywOLDi_040royyNm5tv3nrn55zlgCOd2fOWMWp80VgWBTVXv5BDknsBXWOHjLl4bGevXSVHaJtqHlsTCpboHrfp3jDuYKQLWdwzTXK8Kubbpemgw_OLioamD02R2QefmUVn-YwJILf07dJ4cWHUzHBm4yARKojvQlVGoWpt08R2YmBqsu4tGTibNH1qbdW2sPCQUXnyt6KfMLjnOB1oIbAKR5iRO-2Okn490BMCaX-8o7ZHewTi0nyD7IXD9EnGOSgOId3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lZfFXGiMxNvh2HZQoahIpGIrrkTmIqFqQ-qP7LfTDOV0QUqfsLHeKV7DJ-nHW-1n8pYMmt8Z5B0VPlwbeqCzv9WihnP2UDJRwVNllhgZohmkbZrca9Qo5K9YLHOCrCiVK4-C7zdUitpNoG7oiadg2Xyfl03km6jAloGO5X308d4uGkXccvXuF8uBwN32hwNEzgGIRYLAabdBMrVmwUVGQNFqvzoP4CdAV4gIO05T__8oMQVvLj4m_4zH221ozaIwvKDxXLSF0rT_1G_PmVU_cD_chvjp3nJSLjKL2Tpk15pKorL3Ly0UYPEEQWYaDMHp7EaxdF3o5kD3jbLYSibxqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m4tPFU0MRfOnlHzX1OXYNb1NuGQqN1t74EbfglgvKlIZmrJRUGuhzewGeQqSsWweO8fX54_ZDrkwJINUD426r1gdKi-LiS8H8sorA-E0HQf-0WytDIUnqayn7XTrpvHwxlT5DY46ovrW2AX-_naQFvaA_Z-4xsB6xNc7xN2Y7pzGLa7So2mzzWcy7wcBUoM_M-kkxnNNLZtkPjDhECs3O2YX1i1GZhVA0gvW3ktXRTVGG-EBMqa3v3qHpqTx-K27YHN0G6vh-rB04sv6zkygzQebzQy0pdYgYPKrJs-9pdZzf-HWvMOf48CElQAdo7epQ8Lml2X_L0DtkgLS-GAIug.jpg" alt="photo" loading="lazy"/></div>
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

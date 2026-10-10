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
<img src="https://cdn1.telesco.pe/file/Cc9yR4o4Y3p1KHmSb6wEEWWwCNxrHzJRxVH-J2bc5-z6LWo3BHYWotUabgovLZyxZBRysM6BetHu06bJS3OCHcJHlouyf7kNfl2wsxqvKat0OnRaaLdrqHP-Jadd6fC7RN5gfLJArpUzkKHuW6mO-L0KNAysvNTRpFXpWnmHN_LNYUr7tpmvh6swyT17JgpFusfVlnnCcpZ4KrsTciySW9RgbbHqmRLykWK8xlXUmpU0Lo6fPQgBIL2NLv_h6K_Li8QDkhHEM2LUS849RBsGfCOl5mcL9CEfhCa8Fspy0iWg_KtN5_bbJ7wW0ljtexG4LW8_lv3U3uoQ0FoJsZLd8w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 16:17:25</div>
<hr>

<div class="tg-post" id="msg-2662">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pEF0JpuwqvFPEDbkvpP2AbIC2iQKxNdh28hxFcRgWyw_4byo9zIOeJBw21OG-DmsSbTFd_PdKR3ixlIyh9XkgG9ByEGw-KQIMbuYXOe3cQG1Vuc6Ic4RtZ1AqZdJ0KW1rI4Epgv8XEzdyvE-O7MO_ZpEpT6LqF871Xc65ra8mZ0-OORF2s5wE88t-rYkwS0xASOjhsFVg95P1QJtd9vysY3UljfXfGVLjfoSivlhx7LLbUuNgCAP4NG-ulhWeywYRPvr-Zbh1fA3ssjyqSckDPMKdlngxnkFBJ3ZSSe1D5nwLYPh_kSKrnHVc4zHIckO5o-o2oXjiugVLf912wuLqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/ircfspace/2662" target="_blank">📅 15:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2660">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qFE12FgQlv8qEAitp7F7GX2oAPQe1wjoLM2_l3C4HYrzRK_kAj7Q0vxsT3NP5NRUvDJECqQzADVIuCDhueRRes5eYXDLuRnwz9XMEfgOdrfgKyecY1R8Sto9WQ5cusW21IzwrRDjzr5yb0XL5PKAVI3FwQZkPBfdwschYVQA8nrwXDc1NiCptGgZT9B2C-7_iNRT2OKtLcQlsEvAtZkiiCELZcME8QSy0QWI4HSWlVjyw3cpXYSnWfzevOECiJ-wD0F2NwbzsfSzaC3JiR0C72E4L1QD9LvQBJDsvxAgknoerXSJvAWbrU0uMhkwFKAfAiQdh3FcjRyKPHMFsv-7rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس‌کوچه در مورد Jet VPN که بیش از یک میلیون بار از گوگل‌پلی دانلود شده، گفته معماری این فیلترشکن دارای آسیب‌پذیری‌های امنیتی، با شدت بالاست!
این گروه قبلا در مورد خطرات استفاده از JumpJump هم به دفعات هشدار داده بود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/ircfspace/2660" target="_blank">📅 15:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2659">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dn4xHGjt2XmyEPAfkcmkPYp6IkxligdNDwh61GCq1Ai64X615si84tn4R1Ran7kuAhuyCPknVrVAVcUXZb4HrvxwUX8SAqnLLjurKSgHbCGKcybGJuuWwGSxCvqeM5zhos0GXFFm-HA6T1UEhlFtdBCOEhoTUvCOK2pzwFog_ckO9wZSARO_wmT6IGwMaZqPxpGktPHWvz_kk1v1N6SuYNIw5eyfJeZwez1PbxkRH4VgP0326YWcpESIJ4QTodg-duotyO3giEhBpNzJmIkKTJKy6tUXlRUKn6zQ0oB3UOO9igVhkXh548sg76vZmjYWuAGYKDyyBRt-i9I9JPOraQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاونت توسعه بازرگانی وزارت صمت در نامه‌ای به پلتفرم‌های خرید و فروش آنلاین طلا، از آنها خواست اطلاعات کاربران و میزان طلای تعهدشده به کاربران را به‌صورت کامل و صحیح، در قالب لوح فشرده (CD) به این وزارتخانه ارسال کنند.
در شرایطی که شرکت‌ها برای حفاظت از داده‌های کاربران و زیرساخت‌های خود هزینه می‌کنند، مشخص نیست اطلاعات کاربران پس از انتقال روی CD چگونه محافظت خواهد شد؟ /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/ircfspace/2659" target="_blank">📅 14:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2658">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZXXA1czwGaxqgFi8FFVmojACC4qds9smOGxI4LyLZEgaAGbVoaDuVZfi88NAP1qtKHSr3UNOWrTcEj3XUhx0Kuvv0WPIt_lV4ZfGntg4EfRj6iKi7-sMBYnJf3e68lrfNVE_H70IVjNJ0lQtUrFsfjD-CbTVtbTwLtpfaY1VjO4i3xMp2v1XJGtZDZTem5pAsGu3fdwib5gfw2hSHKfLHftgRiWyKWulNevtHPQTB7YDMepnuq8_3dKF48Ak33eajZM0plomt1bRfdKoviXktkV5jV2onnSBB_5F_848-U1-3lsGiantnIERd-vkmvomXUUGLupYvSXP-lOw565gww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/ircfspace/2658" target="_blank">📅 07:51 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2657" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/ircfspace/2656" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/ircfspace/2655" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/ircfspace/2654" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/ircfspace/2653" target="_blank">📅 19:38 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2650" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2649" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/ircfspace/2648" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2647" target="_blank">📅 17:41 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2645">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RWDh3b5bc-nlp5QKpBEzg97xnW3zROqrOJ_u298jEkimzCWuOY2n4LVrDgaxL0Wk6a0R9NpwhThZDUQL57ff827rHtPDeAJdFooEBdLOi7Yu3QRwREycD7q2CEhJ9bpRZFlDDXvP0cCKVvVTNk1u0VqsCplUz9TBvo7lft50lAwsM6kRc-QkI6dvwA_zLbHiHcHihTwMuyNiULTudu_bZs-ZtKcXucMWMHtnYkam0s4hJEne7W575x8XJ52dXyrTrNfTRBdDHe7RrH4qfOBii_qtSYZ7rIa9uLZlHCSCUmx28FFHho6u8tfPLoROtbL3iyotOwcQbf32O4JUUpJNmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2640">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VQSvGvNmbQLv5q-E4WGobTCyuaCJb82oSK6Aes5kwUsdHydZoEDhuU6sX90HpT9Gs38RNpDNcfcg8P5Ged5X-feoB0kbBFoDHRQwnzo6ZbwSmgDd3TwNs1oIRuHBIPSHThPBKmIoH6Ts384kGD6Vg5Pj1Cy6ruSb98b0PvU5Ys2aIAHaXn8VzmQ0gn_rk1IVy4S_KKn0UeY6GPulVEAP_ZhZE98P2lRrVTdBRy9WsLIk00zZA-HHfMS6w6g0eHYwg8h1cpL6KpFakYrWbB9rtPHziwacoUPUjItF15twZ9Sj8nSFQ7dYJUARVANn_XGfemRV7ERwVTH30HCrPS80ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2639">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RviOFP53c9p6ROiVFBdEKs7L1mGZY5FEGlabqGCM-eAxrxu7BKLH0dC6UVuxgVs-qMPfkQq3MdNETlmQgmWtdMrKX7Jh2JTfn-_t3eupqYuxyHlu6Eap-ro7xV0K7SdcrC3ODJDDS-KRH9c8u95WgJFvMpe12gIu8qNMNUEG5f3n7rpDVV6isg5T-wuqEJ_6IajSO-lQy2-MZFfi95UEqpuM6tytFGyY5mEF50UQEt5G7k92NEj27Vw3Djw7l76JMswA7VvdkVfgWFB5NBRIhKDanUEHKDtixy7PWAjwQLuvYIplpJBo2oqLf7oh9Y1YCHu15cJ6Ebce_7YIupF6Ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2638">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cPUInI775RfEptn2XycHTcbDt3tDACOjyfvQz9fisC6jY-9t9dfZgXmWXKQySWnrYSVJLTDvnEhn-lH82iojZqGZPgY7bpdTtmjWmF010d-kh-WnlhPTOFsj6hzviv0OkKlXLrjKN3Q6lfO04pASm-DvoVhA06ndUadpPySUBsF6_15b0IkiApmevfqhBByH6Mw0vo8JhpLxYm8CVqLBQowZ42TDn_swZ6XnbDDNjJpxHJX7sbjaZ-ImRQA_1YVwNonq9RECxxrb8SY8k3BhQNTot8bVT5CvTKPA_aM-fKZLuA8w7mKgEuLLfURqV0mdLJKSga6mkpHS6pTvKwx-pg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cfkX9tou9sJ71eZWE3Nfnkdr5eJ0WPnhoVmAaZH8mb710c9jZSW67BBLOtusprqEq3kigdCsBATJLLhfQ_h06S24kcUUnzt8Hqi26IO7br2BWx83_6sr54ackuVVdfjJJNIzvkxh6_AmpOHAhIB4XD9XaBd8ZZaG4rzYA9JTw_9LSXYkk3GlrkOAhbuWS7ngDpisKLFxWp5OLSeK6K_qn7drfDwu9D1zDtZDKBbceXOk9iFZO3MxS-lrBRtUkpJQdxj_qVplBu_MT3lJrvWZdwcsc1Cueh6a-Pwe3vphtAN9xZWEdc7X2Y7cfdECRNIHyau7HUviorp_2mMH2jQgMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N2Z2P42_4GNcc_bU3ItDL-2cULizXFgRBN-yVpLKdxY7IjJdGnQER1sijj5AFguuWqRCrjxcvr3t8ppENqRrt0mnld2q3kptKBdBtONAcvh7iWLGuq4K7BYtC6QURWUWS-9aMRUDp4dnUupJCVC5N_rl4AErszmVQIwNpQAe5bomzSW9mks7dS-7qIECELedOa8uI18hKRAExmaqocLF1yJoHUA24WVj848WjA7j10s85v4EKLk7UuEAKbeRh4bNfKDWdgCedZzXHS2lij4BzAI4UtpIqBN6ugjHuHQhrsDrm5lUpvBaIK2GH4jYDpivN-aPwXLERtxwR-gKnNRKAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aoMjW2-NnbexGp_RQmWFWNYUeER-oh5G12e7Lac1EoqHnUEjA_DuwQ70xNEJpgte9yrwVMe7IrTRVMcG1w6E-SWaFNw8kHGUZHJMAXsPCwRZn9n6cg4PmPNMjnfxwEvPympEIB_FsFO90fSD-MZtZ3WmoFGRy1rZTYE522hUJBlHGjvdfTSuaIkXTahh24JxPGCGQ9Pt2N8tndIPGNP3iw2SIE0CVSB3-9b38BhJRjwNQWZD6asdttCzn3ZYl2yzB_RFkgZi3cqJGZATMv_6Rj3-0yDl_L3Xh0iRJFM3jwQaA42hJaLsI2UW1Dhs_XvOdiGV5cGKhkvYzozMvRNPtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UVfCaJOO_LfRfnZJRYp4JcXGKu2OKSDKc7z0RrlpnZp-GQoGzqNBxTYxyHlI4C5DEyYqKaEKqvOuGBg0_QG1dNONfCvYBZ3t1k2-NGegrkGjVc4EJTtrKNgpfkxBeM-MQlPR016VE2GqBg8lMhjUwcXJA86roFW-DAExeYUCQyS59ckD43cr6-v7fM8Cbz-YhXL631lHXN_7qCFt4TsKxfUVaOSudz5R2Qc6TN-b0Fjg5zjVroDQmyfEU--uYrwdhXeuxTssdM4KumYwRrsWiQwmX6h6H42BodPI7_f5xKVjn-Y-VN0lI7vC8K84LWFdbVVdg7TPmpCIQnG8P_n6yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KfO-Lmh0LA6dfHXZ-kpSZm7YB0Ai4xsoaCmFjvCHJyFhFDT-n7RVf0SYfAbtHrQ7Yh8nzTYHMpGC59OVYPpRg2AMNb5E7APSE2DS0KsSxaDyBR1FGtzl2g3gdL3xbHojR6p1xPqU0vWfKoNQXMupn2--DmUEBsoDfvk6gd15Isq-SQhBOQcXEhqakdGBinBt-wCVcp1h69bqH-0gb_9bVBbOB1dSvo--jyNAwP1L-Tu7KFXERg3mg5eo3MCjdqdpog2zeqq9IgIfQowheKpYkMmiOY7Cd1KUnIakV1_0BPi7FyieFSrHyt7iDLMcEsDNJtHh4S6ZICRWqB4lz9ykaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mEYIfSM4DFMGdydtHii0D9fhOZ4l0YwqrGPB6CtGWE1QaifSGv3SBIzfY-iUco5V0cUCScr1ab6-g8XMUQJnJFPab15aGrjFow6B3VmXvRXwVaP6_56zpawj5fKZtb4u0Fw_q62FCSxCTGsQ6nnAyx0zenwUvpjSb9uhzxCYIiuMcxzNJaOh776sYXDv6l7jWnIQjUx2RDloxoL8WxNA09bST4qOfTQ2rFygCro9KRbi6s5RTGWVQfN76dpFDv59Y2X_bSc3LFJ9LYyAqxdZVJPSq_JV7eCr9Bo7VD_5BLxo16T0RU2qmTM7nGqpklJRViZQd2OwNLWn4hFoAxgXDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MCdHo6iFaENd-c7ZKlCFpcx7R7GzZ4veGEv6bQ202qfdRpoEOZstvNpRMtVupx9-Lh9MOOmglC6DMtj4neqUZwwTX13PxC1MUQiOypSe5YnlApt4ddWnDRVsyJJse1aXNqh_r8ZPRjFgY7dsaDJIhSTu8vQlDswNoGJmyQYYMlNUwmNJpl5jIcU0V6ilkWTNA7IN_jpjk7jb5HV2cYvhDXuMZOcpcvrhtnbOCYq9PHCLfMfkl9SNRtt9YIkROIleQllRhwN6wZ8OBGVZmRLuAonjPx9pXECOKS5_8wWn0EdJD6gPZN9jcruUpAq-QSih6JwUre3YRa5WG6d-cTkulw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Group-IB، یک بدافزار ویندوزی به اسم HEAVYGRAM شناسایی شده که از تلگرام بعنوان کانال ارتباطی و کنترل (C2) استفاده می‌کنه. این بدافزار از پاییز ۲۰۲۳ برای هدف گرفتن روزنامه‌نگارها، مخالفان و منتقدان جمهوری اسلامی استفاده شده و می‌تونه از راه دور روی سیستم قربانی دستور اجرا کنه، فایل و اطلاعات بدزده و حتی از صفحه‌نمایش اسکرین‌شات بگیره.
نکته جالبش اینه که مهاجم به‌جای سرور C2 معمولی، از بات‌ها، اکانت‌ها و گروه‌های تلگرام برای کنترل بدافزار و خارج کردن اطلاعات استفاده می‌کنه. Group-IB در گزارشش ۲۹ نمونه جدید از این بدافزار و ابزارهای مرتبطش پیدا کرده و با اطمینان متوسط این فعالیت رو به گروه حنظله نسبت داده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DsLEUWFg684GUOfRev7ROD91KGaOrMr_bNdwBbXK09CznT7NkP2ItOjARYHMGUp36-g4g5uiG02W818CIeaJNrFTVgj5cri9_MtUgTQnAtJ9m1NwcVt1QlwOp7EsN62oEtQt0Pa7lJyszrwEzVdY4V6X8S1muCoDnb3F1LWaNH-D9MFQBBKZClJire9YGibcQeoPcGSVk884I--8VJ7aV7QDaXDmDMomwhjZDaAXJW0EQw_DB87z9gKMKaipIwFkvwucOWXvVB-EyvE-yTer9jNzuNiClvjPnRNjTGkanvHqbs5UuW54cBa57XvE28yWwHYGIPyNeC-egZYJ49LKvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AB6eHE17uixZYjxfbDsIasLkO_xpK2D7GnAPIcPyRQEpcNANqiEE1JxETHW0kUR5sgsxTM0KcBOCXhCsV2uAA7E42r8xlTp4B1G0KdZWPxiWd1jMtmnPkKQhd6XyXFMk0N7jRzZMVkB1MJHOWG-agg2KtYNfZeQomKURquxnKCaRsHU2osTk22NSiLRP_If1HokZ4CwTOcktpH9K7zKfUjJoPK62Z9UhNP30ALILmnoQ1W2_SkBIzdB7GmZSnFCvF1XpW4wAQFuazoq4zY6Lqo8pnekBSjZ6zVxbbvLuRpujHB4OPQSgomftr635_xs-2iF0pZm0BVqx8Jqz6nDo8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرامه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vA79wrkH9GFXsqKHBdM4Eu_eAHYKBCFU4km7hIJOHX6C3-W8UVXspjkoySIA8mr0v8hP9qrtzQz2DWy_men8LkNIJg4g9IeLFi5DJHTq-xi1rll9xbQvseVssoREnLHXq_bZPumRmZBkCl2YgDdjjO0oQ3tR55tYkeZkUS3FaOv75g8fiNKWeUXpZB53Af1ban3PrA8nR7QpXmJN_JjYXC0E3vKMqh-9iquTu664m-ELoFf3dWgSlsC1S7zTG70SHGdYi0SQUCfv5i7874t4a8F_YeBl4fYJs8gc0YEky9H9cwt-5lU0k2qBcgAQtCecmmbtPUiNgtBsiIOuGHtL-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dUJ2aUikJbmlybpT3g3Z8rzFNp0lkvLfn_N7IvRurC5vbzJI7WXRhfLqTz377UzZT1JdC3N9oEfqjTcfEkrY3ncZRXVF7DSBCZ9ujKz8yMuiUvCgyaL9a5bdHYDxYvJime2J8t7zfrzqdj-gzUC8p9MyZXWc1ADj_wknOyz1lr9xPzcDWZ6vWLwiOxKYnjVcVE2Ap7vvf-77CLwESiyU82csb0YgCAPOfRJcB6huX8OKRk_iiwx4lObRbRAWPjnuZgS2HCKGz4hUlrsnF_7ulz0u00-8I4agh16F2yp5Gmn_CZWCBtiaEJzkBMyI43TSTGliWwog28IDadK8xHVvog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pgUHElhX8Gg-XIXM0wN72pQKodMXwQlim-1DdiE6DFvJhOWJe5Srg2jnuztkVlwGFveZ2d28mVtCe1z1zopzJ3gP2J_raJ0OgGkZ1lq4HFSk80mMNBAh9Eesxx6_oIhPS-UOL15XDkHl8DVWZFjl_1jN_cEvkL9QYNl7JcdqziYirBL8ThUIcCOFnpSQRSxqV5OY8dhuBQsCJ3rLKe2_9WubIlmCMXrun42_2VdAHGe5vyG1853NTrB6C9J2VsFVsvsZDNn9pNL0ousQotmvzNy5gD_HY25CdG7rC3XAcuFXaXD0RxedNPLY_qxwc5vWmLGii12NEU-ZlZXkarzlxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت تتر به تازگی اعلام کرد "به مسدودسازی نزدیک به ۵۵۰ میلیون دلار دارایی مرتبط با بانک مرکزی جمهوری اسلامی و شبکه‌های تحریم‌شده کمک کرده".
الانم با عبور دلار از ۲۵۵ هزار تومان، صرافی‌های رمزارز (با دستور مراجع) معاملات تتر رو از ساعت ۲۱ تا ۹ صبح روز بعد متوقف کردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E6NZLg5AOZ0WLgYaXIntw2hxJOS5OdRVUAgtcfjZ05Hd11-mjXdSmw7acldQO8k9quDVYAOQmH1oK1FTAHh4IwIWZe8AmZ_bi7L1LG4hIhMoqFJ7gEETSSjdguGWSygbBI1_Q6Go9yjiVsyRt9NDFojb948vIU01fZcStUw1fBnpaQf6dTxA9clhAKNKB3EJini4neFM2cVaLYFhN-qWKQ-qKltsCjInj9QO5Mf11XqZS_VlZGHUcTK-l6dMq_34dhxpZ7lW7DC6s5FCqMqnIKfcFvaOCFgZbK68EE3OAxFFjXLM-RD0Y2aDI3y5aUj4ZoB0YE5Klm5Fbt7snvHpQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WVhJVJARtp7fLzd-MVwT_EeGUCBO0Vux0iXiIH3i6-IPDFmmwS3OD6vw7lcBoMmpt0OjMXPsbOKEgDELVuxB3g0GfB8ZlJBiA7OruEoXC0xhroql-07ZlobYAOHt5B3X1ZNJcT6ReTA_8uqvhp71OHDEXBTXVFkmK_v8nHpxqi8aUUdpnqqS0osGHQ-ODSJImabGfKzlycooxBPq0uKWXHWZGzznaXRqZd4nwOvADAsRd5YZWyWN3ltldStwYsNbmqAX1oFUaIw_EmW2lBelpPQIcIN7rUM8eXxhxemctj3FEiEr0rBj-qTodWY7zeOZKJ22cjgGXcpW0THKOBLp6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GPHenv2Oph66-DxLtaMyk3Cg_SbxD_67_9nPgEtFoStGr6PPmtq1_M4geIBR1dzRUrlXld7p7RvN09NLRheIFEIKxRK-_1yfgNdRuM0WpCf_CRwPt_fG4WOMWpcT72UhDT7FhO1J0l364n8RYHNxeWA6rcvWNzPW8gXO22YRURpszOoTaNyMHBLKSHk6_rTNn8A8Z9TGDjQgkdMg3uSEVPLmd9wuDJc-L9WlpXOykRiuYD_DP79Jh1lY6yfkoZ2T2iL0VRR6JgNU_N0oCs2VTnuTPiXsLp5JiGMqlLeXNcEO5tD1uZLF7NEOeMsxiDhdAy97qV1BUwziYH3ehWWQxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sLNmq1cGHtmlVr4_ThWCS6Xa1Apc_TgcxHLuN2Gr0inFdSDYTN0x0slZsaSYmCZ7T1wkTNICBD-fFMlFPvWZBTxg4IxiZGOMvQIjvWNhMaCY3141KfNt-qgdTR-RsTnNDybJKkSlgKwZr2l8UIKrcm3_GYEdXRJbfGal9V2TXW2m1gncR3yQqrFDycpFeddieR5IzWYdbF4g-UIeCBiwWeNawYVVtak9OuVht6BG3xYdTfvMt8l9xDeORwjbx06kkeV3c0ADJpsqeoyV00OAIIYqriNoY4X1HPb3y2lgk-JMn11G3oyQyPHmwGXYHCEWnd2QmTgUGFjCXKnQ5ItyuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cflWqEtlt5tXBjWwkxp-Ox-rmCyEANqaaMYezOyGedoNlxaCY7M2DFbGCtF-w8xo7IaE1RYm1tTEIEFQpsASdr7bknIirBK0V7KcWW8QB2EnYOSKdsEDBQHxiGosGXMZgX5DPm9awWU-LBmsOGIizlA_sBf-vgC7oKp96usBl0KmXWh8C4LV6mlM5gim0bvoSi58_fXW7ok8HrR4pLa2OB9qyaalQa9uclvDNgUf_IPAQaKGW8Zcjswgz4PwizUagOoT_Y_Bl33OsiyWrbv2btkiAOc4C6dmlxdxtw1HqtgD1yUpLWW-fqN3qsn0eA1qmChIlkCPXMRqSAJppuF1ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PMvQci9WzREGLa3Lfy5eiaWru3vUjTSVMegSnGR1h8KnBOe5INorBUAo2ZLzRq0y4ROXH1g4_6BIapPjMnre5kHKSVMRDwjG7e5in1pRiMccToa1gfTX7C0J5_EBoM61W0NyJz-HqLRONSPK1yK7Odb2gpePUM_5r_tDniAj83WP6qCsdNaHLysBRXIdddMLqSwRgJJKBVc_dtDX7BeqG2EzjMP_sgYFw1b889Os-MGtJ7Einn2VC7COb4FAbbVNq4IsNuSS8VVkRyDQMz0vHfR14zjQIvjlnRoG7rYzNBrHXHngf_Itl17LMf8uRWNqyKwyqT7ze8o9SylkuO22lQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F46Lx-sYiWGjfivTwC_F16Ll3G_SgPVNHsaOz6vK8q0ykyo2-6wHHYiMExOLnt8AegFEWrccmHUIgEmtPyaMM58wUjhHnNoku5wUxcuuvrVngpaA122SJP9tf_cqDvdujIYzzFZe3Ct3ZkotV5lyBF9VEHtzEDLX6Oit9gcykGumYFyaVoPwkyTJEN4n8v-Em3MolYBfZrj7CEKVZwVlmtjzPQKBAcfx3QPwBMH3Tw9PDCtdk3jqXrIT-9l3XK7dqW2bCu9shPlANcFgOhBEovqdF1UJl_EwVPARQ2_aHVdxK1wQRvUBjGrWH68jor5t-BbpDN5cgNHAtzPA2-AjPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F16Mrk10m0-tqNUucszX-ANBTvgnOWTAiwOkQqJQk_4HpQxHR_eXm3rXCRez4W1OOfII2G18NshBmP4DETtQpwHXV4JjdbpmJz4qDVD5XfGu56yUA258Fwb9sjlyWG8vmgFKQVdth5aSPv5XxtQbB8kuvTV6J64f1UBagsTn9mDUVVqOTEb4c1Hl4zAcsi_GZvb8nqDCqenOcUQXn4bJ5ebje-ncgXMIViuyJq5OrUezdlf15BZ5v3H98t_yDE-wC5g1uE8zJicKqrq4yC2UZRCjijMm6lIKZBC4VZI6r9Rp8pbUEuLy9nnKFLbNYw-LncPu8Orm9PfJNCU792UAiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D5Tuwzb7MVQ5QcsJBr24Z1fl4_ZTfjcEk68YyZc7JMHXsxDOLu17IXfgPRxcAieHjR1OiUjsmC-71C8oBX1B6mJt3Unm_mI6ZoTi8jVSCkysiMA9smuF-Kkq_-Y9WOWhbUdG9BjsvH4lV5G5yUEl08TDgp7AfzMQt-h3MRNZWoDJXCbNLQpcZve_wv7URxtVCP-g_EQnvJWNZ_e6r8qFBk1pmTCB1mnIUmn2NxhIw5k5vFyTfWywBg59Dxw-SDrZ1y4qp1087z9vG962MLHBiqPoADE2uG2EapTZFHsv2zD0s49X8-oIAyhgKpXMxe6IviPkNCB5jSWOSEdMO_5hiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z7srocOZk5kr-sYSzamWUz0HoSh6sCv6jTKHfMsJcaJt67Cubdv55qiaJJiatB_0fsVRfxztMRGynYjanCdMoVxOkQJb9uyfIksYqFqmQ4sS9QytpClCKYU13Ws2mO-fVZHZGqK0wlcFN93ccx9IOG0CrHsqNTQ50U_tni3v5AGk8KJVFsxUS7-HEEzu9FZnv3C7ZGoBDzhUakiFlXtghRr639qVsu9Oi1nhcOV7R6k72bwvEw1WBHbjo9Po_SOdXf38cXAjMQDs_PIS0krCiqcwarVYs15Us3DN33VoTqYKGj-LUk0Kx_4plDnCCNuPF__d7LC2pQtbmLlloiw7ww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IAE2xUeWD4wDAkq7GRkUXGTf-UEv6HtFPzSS0Fm5dEeXnrnNS9Silf9d4fIJpcZ5o1W2dwGEB-GHggsmnAmH-BiqHgGUElM7-IDw5AclUPnwsecfmqMHTig_M9SK3w8xNnYSWXuwaAzoQK9fGGfl3USewPSCn4d_xYuTpUuh7RbjALHQaFSwZYWtjrcLtBiix6SdrguZWCLqs5WdmiO-8v6zlsk-nLH-koc-FK5Kk3q8XOkEnpIp--g1HdudkdT8D-vyyX04DVHrXibmFgpJfsWkdOgoLf1brc__80UbP0h8enj9dLjFyjUGWWFy20capHTpnf-ZGK1LJGmY1wRNMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SVvENkpkQpKxssk10iU8DO_3g6T0jZVV_cmpFCtMuNnftkqZbyboY4c0IlowjR69twTzfTgectBosjcG9l-PAy0AKbg9DA5ZCfGRI2SLsi5xGlG5qD8MoIXjgXGSPPk-_tgVdsh3wB9HTNPXlNzvgumVS3OwoZ-3TKpxd4K_W1pAvQkseatDHYKWiYAcd8QObQEHwv1o0tr8JcF7gpFE2mOwW7rVjZjc2K4a67vPKc4ZG60IJc2mD-UXKN5QM_1saRidOdDmp2A_N2wEe_XwxdpGKA2xj0enkPjqvoYlWQ9SaAmg-v_apDwNrMwksUCGBbO4xToCXG02kuapTAbdSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ikkdo_8FC_h_5OxFyOf6s9GdawGmhuW0k0XnonYucsO9gcnHe7bYrt3MF-05kFi4pjSOCHIDUHVPvUrw3KdRmkOpDwPDObxF7rIY0SVFZpdVNvNRI-0Kz6za5n3Rg4bEw1zy5lF84TLVxtv70_nVlEE-9Lq_9gUEZC_j_6W1XN1WW11r58BuhxU6TYzkdVlZLVc1TKrXTUQcHBCOTOmIM5xUhLk0GPL_w59_NJ0OCeJOC15qswJCONzKMXpwsEGMmkF_3Siz4chTKDvU8TczdAhLykoozYqdPoMJVBZCgg97PoSbxIxSsBlErfCOleaHYOsoUgRf0z3YD7GwaZnfMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AgH-OJSbGGl3LrjAONUvva8HUA9gyb9w1sLqr_v_ILo_v-Xs9Bdigk9uuoAjqfxyXxywUSrMLUvWRbSlARQgPlJ9jn_ePOvR8CdCjtHcQUde8gKwoD_pZJw7tjkk8TdphTU0awaNyQHtnFQxSrUlVU35bvk2sXCwqdTua6ygl0D_d3h1lhLWpOMcvdALvMY2cGyVYgkMb6mnOBaV18QODO3KdMck6zXTlddzwve-KV8AMrgY3YMkqERpQOzwsT6T9YmJjoj-ve3kkdBNYa9kE89bKslR5-wX6fhHjwLh4LdS40WVrBeK-60_DAuW-kHHXx9A7B-JyEcMvH3kFxwWZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g_Nt57Pa5FWkaj6F2lWeTWI5MolCbbzXzTzGvIE3sPfzUszDUWcypwK0ZKKc_ea5YK85LbP4pTKmu47EuOolhfMLilW6HKfTm4Hug-VKuPo1l7ZUZbOpJ4XD5SXQ7rrAMhtNOZ6mnnzpi3C_sdWoraEGRGFeXUDc4u3z4UeEwoZPbjmJeNN_7ASGKvUOEu7sI_HvZTC5CXiUJCJmtLRyCGc7gfTy8KQHs11K7aMLzHso6y3aBlagv9ddKbBYCpR1J9RtNHTNBCo4-XhFc_8KUJyA_5gWm3BXnlL5eXXHsT-eaeP3KfHq5RTX-e1SDW_V4-EUvvng8g6FQeo5W0yrUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nHFOIB5WO8KCL7B3WLxQOcBIhG2NXzV0gCmFfbT8FNCU3mCC2i6sgEGCzhZVWD0YoViYjri4wqoN-_o8XOOaSX1FdJ9sQ_l0Fm9r2953EOpOXN8iAM-GGqQJrQo2TaXksocTSQJKsROxsBf-fkE2jxuahTc7w_cqIMG0YA9CAK_O7UtXjjFBKGKA2WddU0nX7TLELL-_J9cTsoL_UIVUBA8putpeeLe2lahL4aifp61TiaXiS880C7uXQKvgWVPTeAvLp5qiQVGG4Ksg_P_4IsPUQQIhA8YMgCNXMa3C-MSB2d5GweuoPUyDSRQPpjQdPGAYxDECguoB-S-1c2Vg5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gsyFPjIpDjHyeaSqcyzB1O95r-9gOnMGY3gaBwLqrpy0OUa5hum9koCZ_JU-6tapNiIsmXBD-HOWwIdhS8GPFgp5l6J1-Y1pl65NMqtKQboJGChIs4QgSgfnCzKtieU8kKWsc0sjVJspFNz45ihqszNXaNwD5RzMSUoVmBUt1knyOUfJfjWt7OL5dXPWYK-PQlPmut7iWcZXUfEpsDj6BjH6IUX3DablhDZPWm4ipz3Hh9MKe9ewA-5KNYAaVXLiVtJ1sjRUamgx09valct5YYzoqgGn-rlrr3zZI9RVEDxi050FQKz_TXzd714UhA40CNuYahhp5JlhSO6oTOdb7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NM1G5e57nrGa82GkCjj_-pjbYl3G1sqwgRb98ne6KNh2jcmsLX-tuHqvYpVspdDp0Oq0BxxugIo1Bq7wk3Ey0ra9KC1eF3QZ4z_1w7CbexllGuVjlMi9aw_5HxGHWT9aW36hcB58TJzsbteqRVjexS-QsLc3Wc4wtbjpyJXgFM-G3Y_RKp8X2UPNw2KOMAEPlOMocYREG28mBjp54fLnQpcHz_N081_glMQradEMehnVP5TPqJlK4sNp7oB7MQ8RwxRj9dANiapmUwUrdMg2LC2syO_D-bPRQWtzOh5BcrKwu3_lUmhUpJHiCuGeKvAqiYh5kRaEoDISVN7eCHvOGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HxLPQtv4AMe3waNWEledBFCmphd6f8imxFa9TEEqEPpEsb6YwmfjvGwVhIPAr8_nApgGbCvPjcCuNKN8V7vTKACMpbY38z04jck24-o__PJRDeBo36L9t1ftpaA4ujl1kCju0czpjZAx6f4mk7WMDV_WrX9a4t6FisVLRnmD8G2ta7jW0a4MOk3Ndj7sW32S-eBCj-exrnbGOB1LWLbkOpZTUKdaw6T_V9IN6aFL8ElcYZhEk3uFcuvvEu1EYhWA9QkgFlAz1NiyBx3fWePB-a_60MqH6e-hRq48CG97uP7dIwsnweTJEJJkGn8DrthMlLlc-1_Z5Ddq2jo1UraGnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/joNOzSQTlfTGHs9r453QQ1ZkSMJJSt7OhMxieT8zyUUNb6fhtGuMOVPF2XXbyegiPEINdUuk3ERj6eMQmQBgvKLDMTn8bKFbn2eFoQjiQIA7QRmIwHTAGlAxPHNsplHd81Vao9Su-y6R5FQkon-tVWCo-fsnLVMv-Zo98pl_OefeDQuUSjfDWcz45M2m-tFHj3HwOq3y8Uh-1Q_fn9a6miABB01_7jpJobqz0HdTk_1ZqbbsZpDvEpQy2P3UxI6yLGineUnJfbwCqKf8cewInS0_yTmOmC5NVQWb_GCrSzTCVL84IZcUP5Qz1ntA0aiOLm0WgGCqHZnLhD8EM4R6Zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i7-vi0yxB_ZTnQiXjxVyVEStzEAKKSHcBOzcBnJPFs-FAJq0X1QdRywU954uOE0HRuuw5kb4tY-K_evfABMaQAX2pcMvOCzHD4p0ZSn-iP25Fte2NQ_5Qbx5Ppm7cYWbrVf1Q6r5mXqN3ymrFHoePhG46cGvqWJdh-80iglO4wG9VmMPPCJm6FsOVH9LCfaAmF3b5_bJQcNYdrjalCdxViwORVOcGysyQ4bcLEv6fahRVbNuT39rPEGiew6ahWdsV5SdRR1z81nQoXMZbYRqEb9kKygouBPizXV9cPcsk5f-udDVAcWmRswBXNNFx7aJfwAUmHNFaR2bg70Qz1TfyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f1yeHup3cRj66mnnmquri0KcL5QyJJPtHFNYyiFlzAz8lwHzmPMOeVdCkRmxkTHUTcsgLSYm-G6a5v_84UVJaODhqwHBlw0talp0xDWik7DpvEojfgmaeQXU6TQAy9WbSXsfmP-AfrQRSOcIWVbT4xM5L4XRpMmPoYV5xC8mDrm6ZUTag-fawtPvSUbWly4fFuqjo_vglX2gG-qqpzbKuQCXZgZpul_7xXzgA6iweIcMBdloOIK1xKOkNQzz5FkMAA4iAPkW7NodZwACUs5zLTma3CxmhxDNBFIU92B8x5fzro_JYyPE8bMKpee9w_uq8CVfleq7oO8XBR7ntXQgtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZzCqmfuYXt2uHQohSZmw2jhYRdEyuV6VA97o5j7Uii1-Gqw4WPUb96dbkE_q8oVXyim8GnK1ECfUX_8o25JB9lZ3zWosY6Siyd5r-GlGyzIU0pQBe930M4he-Rwnlbg5soEubuAHD-N1TBSf6jU8XbD6WKQyIW556LmwoyjxFmzbBUCn1KPilvyi4ePo4QkErghqvIJZNUMV9zvD5I8b00dlEj-4fGtnDyNutXVUMFtvbqXOPO95fXnEiyGXQ8d3DTh1iPINqPtuHcffhon4wlzThjZ41QlCb3Larrl68YOLDbVSjU1kjmUY31sD12fZVhT15N1e6EllTUnB6jjfWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aOZ9Sd5FiaqPpOI-gXzdwmnoYCULSxSwoislKdIXm5WI190Eq_moingpCvy2sdztor8ED-Wc30jwDs8fifq7zWw2ZJP_GD7cwBTnch4WnVhQgm8e8M_umkel8ADGEITQHLAJv_8YBlYsfBKcVerKTsepYDpGUiKgmQZ2EpGJFivqTL-YI2sCENffM2y91BayhxBmcxyoSB9sWwqCnqSxzqq069LwvH9HngiRm4JOxoj3b6gCZFALFXY27gSKIvlzcQ65-zjSEnaBp9XDsTxi8wiPH_eqHgH4ImsipYJmZT4bMjDLG03TE9lydX7TZh8E7b3CL817ebGt2cug3tP-kw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GaGLvqJ_5MKRfMFV0AgKIeWAf7wyeRGOQB0QZ1JkN4UUcaxA904eiInsCHM2tW6z_WFj92sMaOIlYRgqY9dFIxk6J3w7KMkxZSwYFU8IXnG0MO8i7Z2PNXQB2F2fvqcOqtnubkIIiifwMZ8vfl4agDev148m4niMEcRU5DX0W6meK8i_ognG1VJg19_4EM0hx_GrrYR59wIgZ7adjgAxU6dMR6shANcF2bmEtOlxZdFG6MVu8FK0CpzEnUWiHdaqnGTKqVrc3U2IiCmSHgOkc_XnOf-usA3oB3iI8F-hFyzQLaKgrJTMewLNf3Oh0mv3Ab_Gl0IQoPMMrEMmwbjmBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r4G9Ue6gOqtLBL68c_13iXx2zABBondTahd50rZx8wMrRjVvfUTzAQoZUr8G_8pjnUTTVAMY4Jl3hC9_dR5SRpEserdmVeWEjq5hHKwORxZPbEN4DYUmk4xy-rlefqfEqI0hQMUZU3cAFQFVXWK9s080P6TZ0Hxz_7pV1M7L9psnT2vvLNzWcRiwfvy73JRNrZK0A8bvOxqcUA0HTP4ENkVq_ZWKfIxvsi6EdC8y8CkLTE_3GlG9hDS59NtHljJ-pWhz0mtU11ZN_dcee-nkATBvhY0XKziKLcIqKP_ReJvNu0yL7xsdNtQJcCW5oV8NWxqYoi6doxIS5mSX9RnEjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vNnybgUsDBY-2GiFT3EqBgbDTp2x4xcRVvpVREVaAkWvbsteFVwMunqkzgpnhlKtzRkpsvMjCfS03vVfCXoRzNpWs2hBEZ1v2hv_Ur2Ehoppzvs0N5HGT6v3CtArJWsiCOoMO3OTTau1z-wsRFFiER5lbZS2tSp_t5-PwroWDxvbLjHgI3MPEA-jletX1WBTM3GwIAF0ZqncdlJgAXjbOIaEMrQrUCKWwjWqWejRkIrTtm_xUlXDTOshZVaWl85krvV4rYMZ7FuGYS4kTbbnnIBEo0jLDKvDXKfO7MI1f3nQU_LUVmsbIRf4br0ePrylz0jUZj4DnMGPw8HNL52_ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pdQhbphuFFC3F2um6MlC9jbU6qkqcOHMPT0MWiKw4z6TRy8hWOdJKsHX04FfDwGaFihzF16Ycz4c4pvwrWYPu4i_phTwEYYwHgb_7E5oifRD9g09rds_K8cqiMfb67IGE3zFw2FAmEs-ot1XLxhp1d9uuXB5K3nG1_cn-2ODMRPf9z9MmG7x-F6CW0ZLKDq_p3fZktDDTxovdbl5hv3WcO7bve6P-bsGp9IRaWzMRdroWz6gAKfLf6VoOQwwCBhHGD1Q7oG77P_a9XRYVqmYizx5_FFdRQEPDZbdiaHMTBh2pFGzj_ng-0xWw5DSvbeUGZaw2fRvZDKG5_bkuEJAMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dxX6JxYewtJgXYlIKrPIWdG3yT33NxL7QjnvfQwH-DDfB-9aJjPd01YQ7sEHH0FGTTLEGo8nDkq9X2OMsmgkhvUD3fvPpIzY0K9B15mFZu0JLkDepxoTHWJrZhNkfbY-ZK0tl9lx19_JtFtL-dBC2pC7v412jq_8H15NZsS9MiMz3pNMxyGK24WNAwnJKclW_QWlgnj_eTQyUEaQGXy8NkZwC0ajs3rsG0-CyL8ArXBduZlCNHcjXI9e2ssMb96-pqwQ3-ecJFGbCAxoo_VxkZ1QnEdjW0eJcEg2M2bz3UtMPziwtf_q7QjBHpw9-pVklijp0CE02Kaa-S61wk_1Fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vvfL6tzDB_OW_qZvRSHhBmFipcj9ag4JfrIkrh-JHq3cQPvNDw2wg9BFk_PGEuPBa8oEUiV7cWpUxE_pAUOB9en4cXdVon8LqLwJYXy2ZDQ5Z2AIBesF1KS3AbhzxnpsEg_VL91ENIZTwgfKySYidWi0yaDmDaI-gs1PN3HbkULyaWsqVe0UQa0t054aKtnnS7K0V7fs-CupofgrE74vWUet4WkI14V9NW-aqBVMbj2sofUWvdJS88QdzfQJiXMoFzVPgdy4O6FirPUPgwXMNl9bcesErXJratVtitknuPPZDmtPgaEPRxtbbbIh_AXq-cT8yDEyvHrx06tmv7nDWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X8_SFUWyzgHh-lIpUgEA1P23h3rgEtUC6fgz8zYmFsCiHskhNdlRIVUqmucrWUyGULYa6UFXjODv0TJhZ7Rg3rZjEXjkLJCTRZW1oXsvuDx_lEZk9fWQmjiIxqbEaX1SkFd4zqrZFb0-9By0nHaN6RhBQ_9wnKX8v2Z9DP4_Y7Z3BWomqY8BtG5aeWqiqSfgVgwpPi946gSZcJLINbQwnSltzqxxYxNkBF2dgNgDlJUtMP27KjUrlRtBN9U2sCHurWG4d_OUyfrB_DRxPhpYq0ieUBL_bk4j7Zpx29-_7vBfvcQC7Y013k-kP39g6h1K1jRpSnBx3bzKMIcTjKFeIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G8pWBltjp0GdHJtZy5mTV6Me7yzRarOyVAkRRR6BNYRjiIrRQDdsPNbcU-HlD9STGeSNev9MpIU1Q2H3lnwuPk0I9C9uM2WJH53u_x9J8Qtno5AxHFsieYbGVGRSmMo75NcgdHwAFxSD_ZU8bpkWIYYhQouKLI8dxcBZCF7nVN9AkiAKJCIHg53Gs2EyvEGw9Wd-Jrz0AJV8EezYkhKOEJh3wzRtp8fKjBTCPbtXTc9LYc8hG3CmxSJJYKaquWTYY7qtnIGH97oHCmTdMrNyMAsv_qYN-YW26OIsMaMbMmh8pqFc0hmvH3ZebhcrQtThTi_avw8pfRZaDWgvkkQasw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sSgMh8D0LimMUoalElXXjAu3dwzj_9KNb2lqbKYoQGEl7Lck6ixX3Zg2IT0WsyoUATcc2zD8XbmIoRPmt1CyQYOLO6SVOaI_vneNYRHyikEW9xbYfMDHMhEz0x4f79kKAtqG3fMHLBFonLESbL339jU80Ct4FMTnwQXYeB-GCQe6WMrYUzicN4788yIIyFT2Vyq7qDVjsPM0aRQIRdyPivqhe6GfA420qXN7IaPyueqFk4WqeOa9Xznq4nLqccnTY3RLHcLib8o__M0f6V6elotbfJ2jY1P6Bim-zBBpsOR_p8MC_9NKhdiPDZlEOxcfNKH8fv44NIOydu3nrxfhtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IAQiJ3FLCAHrGZy0UJFOzHflUkebRSiZdkbouZYfdYQDY16dFJJo8glDIjgOI7_9-sc5QpE3yBzSZPXhN0qX6ffegH_sYZaLwwUC5HSwdSNZCauPW76-hSuLbqRD610_vCgjyGKMdjC5uxSjsZ0Z3sUaLdTKbIuJoVOD73jk0xPM2l6bki7lhJ7H5OF_Qa27AEDcadPbo1pI6M7L6QS5RhanJRpykSb8NuKHFfu39gbGH95WRGZM6X2Kioz_zDORlCpcrvsjZMHFwH4Ikj-EfsMFLBeFtuKqTyEc5-c4l-OHZ0zLaTeFKny3GPHavpLJ5i33dlWclfokTVvUTRthJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pOjJFGkbt4mOpp6PXV2hVjw6tR0RILxS4EJ_S99qhs9hO56SFyC3cxqBMTdr69UpXdscDsBgGx3Zt2skxOwcNtcgIkhqVPf1S3TU6nRwwrTbUxlr_4x1hFXSXVibStoURlA4Z5kMP6e5qMTbesZ1gzVPLg3RKX9kZeIu7Ex_CBy5PryJUx_Dde4XIrriv2KJEkZUoFpuET5rK-snmpziem5VmXfVAt693yCbIxeT-ApNGFedc03GaV0Usqqb0YtE4Iq2oEZgb7W7xeQf7GX1LJm32vXvwDlhlYOFyvTyr6qn7hQ0fIXz0sPBY_FxlWxf9kF-bAyPzip0kPu0DEdHZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mzXjvv50Lv1SleFArkJWbr6cY9Mlee0SnDtopq6cp7FSdznnOIWp4FLLtp1lpbD6Xtsmn-w6gmeJMmqP0ljWKgb8Id5503FoGNPnx0FAbB6gkfiH_iIo7zYjkEpkN9A3RWe_aKrS94gw9Xnd7-bRoGhTlxm9qhcE19uBlLli3oD3bPo4dmxIfUZqA9kNInFE8RYBiIKl3by9viVIJ4FX1g0r97eZezzQNfl9CV2BI_VjW4_t_jHKXMavj4yr0WqyJx_IXvhGNiTnkXiB7z-9gnqQkfPXbh-WLcXpLHsBaZu8-kAvjEiEpGuE9h_Fs34cCKj1RmyABrmQnj2hj8hlKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/npmWzd88x7kUlY-H5n_UBz6cf4KeDr4796Twh8OAPFOuFOO-Bl9g8bMjtXCiGToT8bQ8bAHoYvoLrab7sJbDL9Az7VhpqDLlhwxxiQpTDZaJv7HZCaO1gXev4OLtozu__CRL_cKj25K7b2UOwIMNTHug6hV3N3oswI8uilQGwul29UdsC8bhcg5pzGUDeVCGf15U_UgbASaui5GdabVCRnK3szcsFbUJOmohnJGmEqezZ0KGGhH-3_fU1wK-t6RqAXiMipquEAoomd74PGKVHTCqTojpbF6CSInnjRi20dw3hIIzqz1qeyThoHD_9jNidSt37iLl0P4GebrHYnQYQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eBmQzCx8KviIXqv5mSMqJmCywLfRV_DOon1yTOQcwaa8PZbyD0mwoEyla0oTHIdYEYofQLhHMrzreE-Fp35swPUnscHokGRqz-qFXqYsX66vvechma9uwF7hmFNSlz6aFomxMJ0P7d76z3KcmtdrwL2DxU3ktpzZG9r5KU-XQHDjHdRIltiiFVvfdtzcQn0E-hs0tUbxruTUb0eWrGminnaYP8G6Ehkx8iKplxnfU--wekK_tNhgPy_JwF4ixZIOQ_MHPYDZvNuouTNS-Dyj-Z-NSHRbW068xy7RGwLAu3VOzc9i2tu1yAKvLBNyL-RzHuTnOPafpPZdiDf4dLRW2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qixK9_Tu7nC6AyftI0L_D4UgGzzncH0vL_-O6aUOD3f6e3wv5pB1Y0CGHoOT3QRiBJYv7sVttsYZW56zeR_nRquyH2ly7l4gCYrlqeozY-NrNgnGRlhAKJmDd7Hq1Eb78rDoiGUjBpNBAFwFxWUAbso5NMcDBEoHczxiKIi-pwTMgC9WIUs0s7WW85fJlC2VL57D2jfO240R8siBAxoI7K-vn9Q1km8nYLD7TyU6_GC3_G4D7yUejLl-F0YZTA8zgSLeg4pFX92b2YbsHPsf-raZz4dOGlXMdFNJfWCu3Oju_S4NPyQ9tHiHNPYUNApFRH_Ntx_KIMuCbtP-AFIcOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KuIWBSQD9YP7MwWbrOAEbq1xFbrCXzfyVi_XgC6D0C7h2AbzLInY8tUrdbm27-BxHPg44-xL2j4r5IbfKHZrZtbZXGluTIG7IlxJe-3447KYxFLEuyiwZrTXGwS8O-BpJbKAGF8eLhvGsFW4CDV3vkR8BhsEr8OzQ93vmA6dEyQmSGPPQnCpWZT3uQAvu7zfhjLEV_VnqiSjVrkkpimJfqXsH-8JOjWIOHsW5zDlYSG5fYAtaHVzm_Q_LiMAQfP9k8Pa5BcK1lOytNW3eavV1B_m7ifwsptNIlyMpPX_ARjikjT0CJ3RV1gU_rjR_9rlab_Iq8qaoLcnBzkeecjsPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NBpsEqcKGQtvCk4Vu4Of2qOHvFNi8PI7IZ-5oji4eRon12L6jsNBBRb_I-fvrK9-A9BZC02yfteiINTJ3reYWJLGrOX9H5UUhlGpOlGoxddYtbEP2_xVqDea5GpCf2gJTo17LG3Hv-s8njiH6B-Rf-4FpC4sZvXXp1f-kxMJB29knhzE_GG0XgyFqQLeN3OiZdx_Q6xvszSbyCnEnQ1vymZUzpQcdqFOXrMKHx-dFvUWHx6g2rEkPUBHNtuUDUDodTMqJWk4q-opX-n1bNPNZqQmRS_7QwSuldPNHU00kBBPCMuPF1gfE6dC-2KKWfe-lc6JAVdjatTC-EV30oOWTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vwpq0JBbUkDFBfuixSO_U54GGY1rqK_rVEkkyXJ_yZdk8ykcSn20oqlzFJBgm9mwzbN-SyNEstngaO7OrJw7srT-tvgYxnhN-SfpVMHVeQ5pFh-L_Jk22Kc1rDvKj3oztjpL6WBxh142-ub6FXrlLFHUrh8SFLjYoisivglVFZEQP-0dLdyDsdLHl8VpBIrtBIAGICLz109H7WlULtL60AZmYgPgYaPSzlE6X1rgdrC3HZz217EkI5PKcQJz4zU3SOrSexcJQla7BoSpH__4THmSi9GGGec66KGXsyVp75yahHqajNYFPz4bBZ3eaQuih2qKdQjusGt0kcVzH6TLmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cuIcsnYXBZ9otYL8q0yVyoJZAxf0QCaQk45qgX2gP6PLg0qmj5EfKmNcqtuUPAjWahVnVZ1hVZluX3fj7O4Amv7c8PJu5qCzFRSCsa7WgquS6B8eACpTuSU-KF1YcRKkXgN0KJaO4EWwkA1Dhlc_CQKNzRY_TwSGEh3-zWKHcquKTJHJXRKOOsG1mX3fv4owi6zkTYW25PscwgkpgOkC8igZWJtnf5V_TcqsKeeqnKgCT2icfKNl8ASnoDKPtdAoaJoq0mBk_gY5az7WwSyACYIXnqhG_rmhOjlTv30_pJpptJMGk-7KWbEZAhGqlK2kiSp2d0WuRT8vA1CY_sRsdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DM580eNNJUjnUrN1J8_uSBqSQnBr9W9cD24DQEpGqhq4htr3oOTokEWQ-E9P1o7-kaIf8Er1Lj6-xAJ5s6fdP_waZVLuRcm0jnHHchuqnlNLwkzsJDAKR1G6-3WuruWE-J4otdK5RIQd1TJ8d2MfVXw3VuTrQ-at-WVZF7UrPttbyjhxZyHTUwfpFWnCaXNHpEhJ5Qxcit74uArFXZkGgd-UwUdT0ja2hS_xVRtnf5GjRyrX4qTelNAHgyCQNhup7RWRrIwEDOCOL8sIl77ZOj8-U6rn59J0ByqOD1VkpKs_KUnKouQF2ijU0m7tNlYGb6HcqxsXLk8qMb9VF1H3BQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sDBBIG6illrWDwnCKBoXzDc0p5Q_JEuYSZHZdQPTYexXeT8tCTOe0RvJCOADUWbjnJkGhLjfv0wI74F3AH7ImJVhkn_183l3DnPtSfMt7H2bVXSOXbjhKeymzFT5LpphTiU0Hx0GBE7N1egnUWeTJbBNByvPpn7VFTzZ4uCCtBvjfiaCSekQLVCEJ2EJdmL_mT4op4NhSgGlllKsmZQS2yBikmMTijCnt6mWcOZZym3H7ub5CI2SYqUyvZFD23JpZWwgjuQ2WmHKaz9XfcwA8CzsEHmeKjsv4Kru-vbDma0cgTKMh1PUvpT2ZQ_xpXZdML8El94KXkE1VO0PIKJ0mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EYTCATtaWMhp_B_WS-9YDh8uT_0Uv4GBvS6_TRbNKxUr8wub0_9niZRyQS5F6X5gXRxc2YtN3yJNIIKMncSOpCG_OX6Swq8e1LmcvNa8sNB7XallSSVfBYEnUvmCckC5KOnfIlCuJsHeNyFYrs9Sl-EvJdHhPlY9eIVqjn-EzwEV2fAUESYlcn3iTzdFE69zJwQMrSIxM8N0BehpkCT0QNU_nJT8mqgxBfwiar7fUolK6PpPJfsWs_Qexodg_MN1uBu8QaKLiSeBpA0X12kFiwtpBMavdeI6h1zIP93ftMG7dTtyE7qDQfNks8MMQDJ3qMYqL_BdLOCbzrBSiKY0jA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bcOuSS9nJsMRy1FwXGLc9pu2vlZp4Q1GWTjQpL1ezqPyj8Z3wWUFmfhg1bR5x0dZ8hcke8ewVaKJAmnBH9fDa1PgKPMdrTgrdsS7ix1Tu4NE2nCcccSWqJ5Y6fxOT3cxeN2IfnNiUqCOT8HavZSfF-S5PQ94B4BGHcBfqKm5uxm8VGwy9tAFfcwk0SxJJQH12z8fI9riuau7GjFEVIj2wc0a_GKS-YMcNJncHGV5eR0BUtUjZstTh5HvMzf4m-kWiH_jTLsziZkb-0Aj6E70xtU1-PVM_MaQPwEkgW8M8dsywH6zmXPG6VLJp0EAqzWTqShbGztm0gEOYCA_5zuJ6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nj2NIw4Jzrr3LOUu-vP8IHNucQqIhCLEYgBdxsEyaKD-8A5T38ErpUDOnSI1cxMc5OHbTAZl-nTtAkSJyn-6IsHDqKoOaVlMB4NbhzUEG9KZTWGfyam9UyP9NXdUP9-2iAPWa1oCS0q0wkDVg5wqmKUNU1FXRXjIIe0r4R40nRCtssYfHxFXGdPnjQKyzI7dPqWxVacoy0bdlSGDfKeRmR82_pzD6If7adNZlzIgdRSh5WIw0gt7CVETQldiFJuz-2JEUo5A79_Kah5uhg3wZCTW8dRFKeQ5CSeSCdkiXl_0oQy18NYqB0ZHzgv0fYamNVCBqwfRn0fopmVZEgB-Ew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oarxTLjbkxfkqdMesa63luyysdPpdXXJACsv_f5CwkEr_Azqk-ieI39DmslPIPiivHVfvMkvpzCr0Fo5Rb6B2F0Of9pXicu1Tt2nbUuHKEeFUrfKjT0EOXDqBYJuDP-ytF-T4Rl6zCgnsRxkAQ7X9oiY-JHjjrbBiamj46xGcCgHcAyvwLmWHTo6bKMhWvd1R7FIx1GusS5pwie26f-tmZ7rKz-wXmPtNIl5vlRfibbGC_FCzO4EDb6cTpm9vkGkmfwQUgQZ1sUUnv_6_mFbBTTGny3PH_2WxoeW4cIUAJlL4ZkWsznythcmgrfoSdsXdY8l_ulx1unS9IZM2JEs_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u511fbI5IiDKzyMxZvCO-S47f0AOfqXJU0VlGHwDV4CGNYuSoByoFxPEv5pj49eLBfk2IQ_fSPnOpY2y0U9rrV9VLMtZO8_u5pXACPtUtN8UUloQgwvxh64LlDkDj3l57oA2h0S0wn3dEUJMjP2JZZLREgHm7xPjbc8Njj_VkdiqtWxMY-zEjG9xd5IqZ3xqnrBRR0O0Aado3pHrNGw2lD03Aj2p83T-9Ic_2mwY857MOD-D77pH3Jiz85NrAQnkG8K98EMioSwi2ATsx40nKsKU3tgFtyi9-_8iwQhTi6AOwuEYq-7Si0sA9VT_F1nhyjoidQ9M-91IiYXVjNlaWg.jpg" alt="photo" loading="lazy"/></div>
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

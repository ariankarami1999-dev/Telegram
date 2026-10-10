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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 21:02:44</div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/ircfspace/2662" target="_blank">📅 15:16 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2660" target="_blank">📅 15:03 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/ircfspace/2659" target="_blank">📅 14:56 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 55K · <a href="https://t.me/ircfspace/2658" target="_blank">📅 07:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2657">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kdGn4l3jBYkSrai0qvkZzu9ezZ190EpcNzWDUhlus4UjoPX4Ye1NhW9RytYRxR9aw3CGZu8lRD3Z-gsyLHu7ziG_NK7TxVfTcD468XVthmgE40PHKai6vyOuqbUwsOE2NpqkeFRKXMoyLbzoJr9si149KX04G9MPzbUOdq2NNaljZXLks5bzfunUfzYG5atYzdCh17FM8ym0KCB7hOT9uH1_KWdLReUB9Wq3RUnj_SfDsLSxXt07lAd7O9JE6M3aCky2e9Gl7F8vkfHbhLPKs7GPASUsRaH-h4P4krubgiU48xIge6uYo83VLC5_7ks12ptgEj8hYOJMiAJNY5QZ8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/ircfspace/2657" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2656">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MkrYf776dUwYtDaluTcZXd9BC94nHdq6nX-tjFJnLGZOB60x4i2bykQOd-d9XbLxFbV_GOXQt5ku3KZxtRmKVAq2GhPhUk_sBzTngrOVjaKiigbgPepCWq19yprRqiE1ejHOtL16t2OlIWm8WXKpvduN3b7Gj9RjUC4ri1AemQ6ma199pGhz4kmZxBLhk-lkw4bptu1100WJAF0QUrzorqgvhFmZlEJ5aWAD-IbPSLz-qRiO8rCqwKm47PIYYWOdazv8bOVjhJZcFE9HFE9pfXUWziwRl0p5rieCGmaMtm0K28mZxjrWaFfGXvA4reepcKHp8d3qE0WvZuZ0_0Ik6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس داده‌های رادار کلودفلر، از ۱۲ مهر یک ناهنجاری ترافیکی در ایران ثبت شده که همچنان ادامه داره. ترافیک اینترنت بعد از شروع این اختلال بطور محسوسی کاهش پیدا کرده و حوالی بامداد ۱۴ مهر به پایین‌ترین سطح خودش در این بازه رسیده، هرچند بعد از اون کمی بهبود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2656" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2655">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H1BMeek4DUSIONrKLir2-xngXM_rKQfvVy9xEBsZC-v1NGdSPHuDZYYSDKuzXXz1EHWzE8VfzlbotWcehRJ5qc7suWXsMMi3taPcCTGeN6aJNAcmA5bcHDcWMt_IcDiX835ndmUklDdP_aW6Y1QtMr-oDR3GZCPUUur_Q3a_ZDtWLxBjMrzpv_MmFU-yZo5jPcOJAsOp1qu5DkJuniWmPP9XXiQcBlrVj3IHtQd4_Yy6Tf5nCZHYdR2hdH8f17jHvx1-ABkX5Y8uh9PRhtUoaAOOtmyvB0rDOl0dtj4jP2i60G53KBu5hp6iMYoxba8H35Kv2w3rTfPk9JfFWdyqhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه جمهوری اسلامی در واکنش به سرکوب اعتراض‌های دانش‌آموزی در فرانسه، سفیر اون کشور در تهران رو احضار کرده!
با در نظر گرفتن کشتار ده‌ها هزار نفر معترض دی‌ماه و ۸۸ روز قطع سراسری اینترنت در ایران، ممکنه فکر کنین طنز باشه، ولی منبع خبر تسنیم بود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/ircfspace/2655" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2654">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rNfldJSMD9ArhkkzUcfFAmuWwF0waW_mYffix6B8QIqlIyTiUnwQPHmnkYQeN_J1iWDkv1c97AQO6eUS91YRMe82G2ooo5z2W6RWK49HJ2_agBRmVMfDj6LSHzSfP8VOzLt5gfyNaatIA6JdGC7fWAUnBJdCu7aC2gV_EMrwcTUf_XrUPAGWVdot5ltWTiEDxeYvW69BoPh-Bm_lYQUlozW7VgE64TEfrvrseujUgS_3-ThDnV93iNlE4EHw_oipaYzjT9r84XpTTXs8NIURfDHlCuWkvj1ChnvwbjmygWWwCO4TDGT1YP1SXrybYDYUiL2fPqCHOcKglFOIbn9m2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/ircfspace/2654" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/ircfspace/2653" target="_blank">📅 19:38 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2650">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BnuMEFlKoMUigWhW1cJykFFSd0oAzPEy6EZERI7KkLK_qh5p-eXqBItjj-WpIQc0qWxCWGJ1ZZ8sT7nac_GmxatuvKgTMPZd8S7h9rDRCWb6CKkGL_zb5AWnEv3Y22wE9MlDGINSg8zwbzpx13vTWUQiILfQ5kXzStS_zAyOjtFBjXhuhAMwVSfgbctV8XWCciQ3QGRgHyKkloEosdQtzyYjiG5PJ4vBLRGpcde-q7lO2KSXmiwEYgbfGjw0my1zX6WPb74wBKvvHvPovCbtUB89wW7HhLsCrerezD4B-3sAJsf0-16MSbvdvhzQPpHYceHy_Ye-Akr9AJyZfZ2N3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/asqvgCRsM83YVqKgAkDviCTArpDxR9ihUudxkCWXgP_Dm086vtd5olRhEoHS0RRhvFUKSiQr4vMd6BV0ML0ELNnWfRLT_cU5AfDi1JJhth-M3Fkdf4T5CM6YsjGCLGeyFjPeVpS54giyx-WDUXqdY3FOWVDgf-oYKfiFmHrGSj0leJ8lO6PJ6BKUWeNLTu08s6EPhsoqs6ogTY-XrEcXnisyIg3KKeB3nCrATEw2cnC59e5LGK0hFcOksl8GtPVyWxcQd3GwM8HwOfRgmX7gMfojmCopb2x7zA7yXBNhXxldXQfhwSgBkTf2sUb5q5a70hYBkdR7N1oa0yqyahmZ3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2649" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2648">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iy8L1Jvujo2b8wDzBKteNwhwteHVOq6ax3-1JKbBxiiwWGipaf5vAZOb1YusY8AOC4rfi-CtDabMKur41AGXvfZ2u2igsay4R2ZLIjnJ2L7Xs-bzHjmAsZBB6icaUucaVUlAzSxn6v4k3Xk_hQ0rz39UCcOnmAggsQyciVkVNxRKHSaLgoFBRZUqB0zu0Q2bgPj10UvQ1jCrpgvnkY2baTGnPWs43W2GVzPorE6IEgTF7ROeVqV76UGoJ-WNO0npu5ZhuIcE9shYAXQOkr2vg1Oa_SZm5SLcgeqrorH0WqGkh1OX-y2nrGaOPoWT8VxQZ0Tyn2KD-yde5XlztLQvoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YWyVa0ODXdHPaWj6N0uFB1EoAJqmC0E4NQbChR8orkmvjDYb4mAyYD72SGYnEauwnl4WIELh_WVZvBKFr86Mulb_fqgUeBBC-SWLBcQDfAMz0qt7bL_4i3oejeyFPmw2TJF5nZ54moWYi20KrfDqC03UwMsoJJhmYWsVQ-CPUDTb_ZQfF3QUqLBuUptRRUC1Ujc_1td7iL-39G7ev-58DaoyBlagnFrp6xyfWKEQVbRNN-dSM7Tkt1Z8u5Pv8r9X7cQzveWEuW0Y4cK0ghPotW0DYzBc_KXdhWJGj4MO10wNSvYAcDM8XuYc1W4cRdQTKHSwY2-4129KYOBiGw-0_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/ircfspace/2647" target="_blank">📅 17:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2646">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LukarzJdcf4k1Oie8BTDxpmGPBJyju1uZNJtD7tev6-N-wadnsiwtu0Ayjjmo0KqdBKtBAlzClRM9oZQlLMpQiTkWTAqR5t45FaBSufzNXWJzjSah527uRg92NfPg4-oEJYt7wZJuxx0TGLXbxrtJuTWUxTiyku0fxL-vvP5o9_Ah2hajzLra_a0g-aojH8CQiEfTpl6Q-dF8DYEJizmxbzyiM4zvSS-mu4iUvaUCzC1vvRUQlpOl3N7RRzd3vYe_6oi-x9f7_kT4SB7raDkNEJ3uEACVjRykkTgunQSggxvgLMt3R4HvUm5tQLYwzn5-iN709n6Kaj4PFHxNgadqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مرکز ملی فضای مجازی گفت: ایران برای اولین بار توانست با موفقیت پایانه‌های استارلینک را در جریانات دی‌ماه سال گذشته از کار بیندازد. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mVv_ax5NhZzhZz1O6H6N4VL21k0KMLdKXKlpaf3EyOOsGXxSRsrJsRvJI9PuZNw4AOw5Vu22Ws57pocvGNaEydSU5fyxnY3bJqhtboN2qiBuBDQSuBJtq1mM_OSXCTTIAJ8bbIF3_yC0Rp_Z-JWut9KPTPNTtYP093x-dI7WTXJoG52yYAc2mwsBin1cymbSZcjOQr0q6lNIFpPoJMgWwGz7NO-Iffsm-J_EsznDLLiH063lzuF8hV1YkS-EO2hCBvw3bNPHNAKHBB7Wq0t-JwXJcnF7tDVOfXc1O1UAhda5qCQOsSY3lmZEaAvvMURu20kCx004w8PrnXeL7VJvhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qUL_vYFCZOM4sqVuG96O049arA-IajKmoBVmYY0PlvXWIKT-9ZqMEf1x2g6EoZyi8a3--sCSH2PgnTgy0HoBPKS3Q1RKVpcUcmMdwQBqhMmuedElt-imWTd7GMw0jvmuI02PGIdp7DVr2fk6pk__ka8IFcw06fJv8EbUnwSzmS8WXMFSGraPdyF2rtk9gwStG1qkRMn0BEQAMINngSrag72a3fBDmbLU-iT70D0ayZBhxPagkGg7s0VarFJZGKMa-wiWd0XOwD1QdUQPvdbq7ApXR0IEH17o4lqfDv8EynFvhU9QH9r8Jo7aY8gDo97TkEyuWB9ZvKuokh0rvl5L7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tQpSDqCf9BjQFLmAscnPQLLMT1_796DWwnvg2wAAySKQ8FHXr_4DhTsbKd4oP22EuzBnadzR91SvsLkzQKOZjbHq5k1WuUUNf_0Dk7F5ak_GTD810ffdsLS7xC-_xmIZZMNm8yA8FC2nDgzq4K11sZQRp8K80t8r7ai_EVVm-ewe4DBYriHQRAmbA3Bbm2bwu7zPbzmgjONZmAZrclct4HEuIt1LYcUn6XjqedWgtsqzAgTpfMK_3l-L7JYHw0Zgk5y3MfIS4sBcR4hPCccTgkFpLK38eHVQ_LmlvI8VhliPtfnqeMNLOQhyI_MGJDDyf_8o3lxqq5FLVDvP9Zjx7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ae7W9V05oNmsh2HN5eUdfraXalcOcp-5WiHZyMRlFeb75rxrNJpNqV4RbP4PTGHREILzKL0UeN5ynwqbL-9MWPQ2T_hWB7NpkOd8Pz6tA1_x6Dr7G1l3dM-L-U1bpAbotbeiL9fjudrJ6NIYQA1-ir6mBu5rdKKVanN7tB8DtWwFvBpWgB7SoIKqtUzGrO-Yj35vqa3XHuQW-86kknW4a-4yQXXtwMLj877TSTVf4Yn4vZP1UI1dRgThqdx2idvEoRREllbyiiTS71yHJS4yqaNOfqGVOH7opejQRleQiF7CbLKvWeLviTSi0xopfC2couZMBfhG9u_RyQ9LbP657A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c0iHqSIcPZ8BEhVHcHnyBIlxeZ9e8CXN6KQPvcVYTUuHnPV14hp_E9DGHG6qOK0QCo0DbbamSCGPhAWDXSwhg0ctalvPDPm5AQ51FBCFgmOrxTbwadXG03i7pj22c_GWUZ8SePiHofVAiGfVWDggglpwRX6GkVRyU9-l38m0c1UCllKDDR-2Vqp-7d0kEJE-Qr4tsqds1W6m3E4LcNPhSSBm5_HuOTSRBSOiGiffh_u0GLLcxxZWU-dxetfFFhd58XYPvsY83T1WlU0j_m0ehk_GBgnIMn3oSDmfcRIAYT9CeKv9PH744yTjtrP1a7fjTS6Gq9kjFVFXmCDDR9S2jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bKgcjJMdhTv2r9XLj1LTb4qmbkZZO5gByET5MdC7G1FEhDSyoTaB1rcn0XY9xFguoZy6kQAzQPGYRZkrR2wxHVN0cdmxWL5r7iDsK9JcewYl9jdTUk8g6htrIIFGGjcNTkxzsaLtHelzpBZS-7VBRyXaEB9Sj7soP56SM43qetQV7XsYckiANNt1bVMMs0BOv2b_nr7cKhqPpC1hUbibjvuecpZEmItYAy6MbEYD5PDJX0coewArgWWjQueB0T_CKxM8LFeZqm_Qy59Sja9wozhEhVJy6Lc_whEBWVF8rJEj_3eWy8CEFhpQKWQsrz-PFOIroFQuaSxgeJ9zWakReA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N6jfqDsFN4RgPwj7zca3pvUL7u29RZy14IZVhTOFOYobyDZ4HGvsdLm_nsdRzbRKw6g9gCI_J4BkwaIp3IG1qREJ650UfKDwL47P7Q7C5l_HMMjiwfYT0LfYz9ZW4gavtoRNVb75Y3_vrfC_LY2WKyg__TXiG1KwrbBO-zpHawHKWpUzs9YF3v6g32xBEXClT3lrJoT4-1jMNs2gGD3D7Yh5hpiOZXfp7GGPV2DDiNV3D4l5LAzv173npxPIUZMrzrL_dYglLFMixU-2wLCQuXgAuo5G7zAE6Zb8dc4Kb4I_6Pw7qjTcl6vjq5kDXDyFQUvGWlHR9FiNjFUfftdOvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lee3yCSfE6HLkuzIOGZVXnFPGZPbuMhKk9z_X9XRsXlaKaNzGlDyWpDmI0LhXRhde3z5niLfzi0y46k61cf8V4AqQvgb1BQ9J6bChPwKVjqn86BZA03nhGuC7rLW6sZ6qyiWiCtOCJpLzq5-rFY7NFIBlTWDItJVSNGJp5WcInDVj8bhYzkERvROP8W9-6mIoeqc4gu1YgpE6MgYa-VUa12ePcgsjlvn7tvrckvGovE_D-fU_zyUgMTYU0s4362MVUANp1ZAyIaNtflIGCLhCIYdhPPfC-Fvzk3kbGWr12qwwo5DI9AKqvyXvRezCdHbqQBOtERJnbap7KgAJs8TwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NhJmsiHOf7hNp0XOPyCpUcPMeWgNeAHCM2qJat7RqG0LUabrskkmGAiF5KzMWzlO32G9cyDIzdgfJ6x3G7zudfYvHAhW1VeZHuWf_G17FH3NvLEtaX1P0cH4ll93cb6p1HRvgQv7nfB7sHS3U9eyzSfkZvyMah6H5hNyA7PcObblnhtbXhqDikpVCosp0K6uDBsB71DpQwO84oMk7isXnYC087chy7M3En2lYAgKNayxG-ou2YVn8VZ6Vkj9IeP5-LDWee8jK1f3-7bXkbtQfUW9zqO2FrmmUVINScCva70Bdy9ybvzx-ah9JYvw52_QlVr-tQ1lm_j6frMpxcC2PA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RpA_WRvfxKm8ZO8athQDJGIp-LGKeeXRgl2FAEfJXGHmf6Own5HoauajWmS-gUWE2a82AIHx5Kj8KkSAACgsy1H67F-dFKnO7Of3a4Wks8lqwPlbyXM0eDtpz2RaSYN0ky84l7PXlG4DjY9C8iBIhByNbso8FMnoFnKdWgq7_N6g37HnrXKfOclkWgaY5GNBsXCnw1i9IlOaWX8KhgX-UBUPime3IE26r4OV21oyWQTjg9h8HXjRv8KFYkQt00XSNI4sfVO2yPZbhf-DwqEUYLXt2G9bwD8WyVd2yKpdc-rCZo0Raz-GGnNEJ2KKP-KG8hyHLFyUOzqc4Li9foNhkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e8Rz68gqXIc9vXiQLebg8VyD-APzYopsvF2sW4IZI4WrXzhfQksv8gKhHBRx_lWoBrzPGgWhVDk5E-KS0lmf-bA7gjz101hmlMrImJJFPycJpIvpG5BQZDkfdgeJn-C8qfxQ9Uf2IJBeDfK313DdtB_0IWwS6YOt0wEblhtbtWj1r93ugzpYUawYHoXSGov-PlKVs7spaQS0Pk3HIlYPKvbLjQUEkrNP4nhKKq5uIzar-s_DuBHgVH9uMdcuX3JeTryu5R_XisJP_Rr6OM2s1Jz2O0BvSgj98o3Hx7eUBOrDQ1R4OfpKHaXPZQQcuNMBkNA2Jak18_w0wsa5lMFyQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bcpi6X19p0z-S9A64o7_HJ36032bqrmbavzm7ru38YzLI_HiSBKL8z7ZqoQHv9uoP9nY063E4yhQnIv_m9ERsaA_4nO8LSQSL4vOHUaEMsyNboyZBH1353G8xLVbFr_qw07Am1H1HKhfpvvv-Xpdml8Ew2ZBF5H5lw-XLTned-m57a4yYnDfvA4dcAEuOcsBjmn7sseJQVPhSfGz_G-X8NtpQ4klS-HxEolSw7V2dK8onc5sqX4gg0jAmw6tGUPGEl_NaIwu-A6Q26UUSc8QALpKlRJtJqZUa0W3dfeL3BDRxeytAS4a24OWqIRJMmae-8OjE-_aO2TUGKez-1rRlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FnFfyjI2IxvGwVrhdRBiYee5AQ6ew9Bb0KkPLU0pFoYF8se_g0OMAFRUocV-RFyVsBoliB26zDCm-gyMWX2IODXpCTg_b12zVt7o7Wm3x37WYyDU1etZhjU3XYQtSRfd-2FkfKwUxS9RMwvzUnXtBU6vK9PvLO7jROMJ1B0k_sHEYJ8H9kJMmMbIuIP9EpqvkHE9Uqi6fMq240PoDep8MmeoA2YXXxs5YtgYPyi4kVAvTRlSUPAFxRruqnbw567kMfq0xDjwJPbOjdBNjS53zxxVR3NNKKsxfAJzHTCaAgk9a6_BLjHG4F4VqnRvPg30u_S11UYacHH1n2QaLvkt6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hybUWQVFrzeTcS2S00Qm6_WZuiY8p0zqwknmmrkgEmjIelYV3vgdQ1gtCNwjpHV0egs1MULnMQO3-JdkUiS9KdEjj0WyqKPPie0Q-P8PPupyICoPxO7kkj1EhfzY8IWyPMl_vd_MH2q0Sk5Qv_71ggcCD0Wqg4MpT8nowLb25Q6SY6W_l7Ut7nEDCAwjZluduPmmEkJklsB25Q02anPth4GAZSvVbNXvJklzkzEl6ak8Wkw2vi9mCCEv_3R4iWtLxlyT_kTzZzJ3IyMMn5Evd34Rn-8qj4M6kVCgKWdRPhCWACHfsTcA67fl-vPDA5cj_5a7Y_eZ3pnFSJTojwmzJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O0TVaNVEWaCVdTAKjn8arFg8ovhYQi2mjKX3RuDrANneg4X6881LYDmRn1DU8JBzztJqNo8F6aOwOoS--e2mUJew1SeAg6J5r9jWh7aGBZXMv2RT_-JKi1_ERCJ8fLKnBjWp-qN5mkcHijKoVcndDPijmqknC4QZ_DmpMKXOYs3vLwO4wDIwyS7y7NUx5cIcmHARRvasGofYyZvwPv9zCR5yRz2syVoHjBKN38E_7LH7fm-Y1Vw_0XlUrkXV0xoC6_kd5ir902UlosMWWZCcBEDrMyXCO4el7FmjaRHTvcC0i_TZK9BtWXmv4nIRfTBjkW1uuQDgtYjEVkznnQWAXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PxIM7YuALXEOGKLUOWhw4aOnk0bDAan8hjD1iDdlSGGyPktW_UsLXx2RfzZNnAZzKsD2MAhUPpE4A5KsCb1ZMUGV9-HkVGEMXaBofzMyaGHRRT1HLqaGb3_zH-KfdcOaDVDmv9z8hdFLeEoV2hK0NAc1DbpjOklrKX7zXcIGgVBMaO0qPZoHhx2WzPaYY854UDBWDKTSGvZjUIZwX7PsRMI7hYhg_hQhNUu8yKa9WrBbeCOkA-JuRilTmwEQ0QSKb6AvBeFDdPBv2As373dp0Hj97MjqfZQ1ypRcs1EqmI716Sa9qyhOD9xtPavZMlhg_BisRBiOvt9MZJ4VxijAXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lngxccg9CRTxQ5FGvlEL_IswQS-tvwJvQl8OTujNSLB7zRifGgq5Lwwr2iuqhH-e-31dqY1OJfy_G9qjTznd2FYtddozC7QcKHv8EV6rNbqFY-iBnLThAD6Voxa0bXI31pFe_wZhgiltwhAsOf3HxTCH9qmi3vQkDPSAVnd8yh7yStipYYHF9mMiZaLxd-K22Aen5IikuayPUfjbn1nYjBe9Hnix8AxD6R8uUFi5UUGY8CbZXAqUVAr_H_2RWh67n19OrBESfqdtTeI9Wy1WkTEB182hjvRfZDmMu4GT6xLfpofj230EQ9ooKBuzUWXN4hp3yahMIzheQtAvTRn3kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/en0rn0YzjuLFjTuld33Bs972KtrAuakW_WnDbLwPWycpnP6BzcWE_znmX8E03iOgYDq2pZbRg4h8NPr2dliFdXxQ7qzIcOmCFd564mJ0mwZTx8016McpqnFiAzCf63Swd_Vl6rQ1kOGsB7KkEonB51Xos4X874VO7YDoMXQSXSzzxPF8inxPU2SuReVttO-pAZSz6BZrZCWgvMx1tdd8RUPB81hVk-9TdR3sXSionciKfVUjV-6qOae3h7jdqbCOa6zkPucAFyR4oXKxBO-c9D9F8ha1Py4ucKpVavGbm_8zu7QOsqcjEXpkwEY3qdZu7mE-6jyfwF_jZkYJu26yeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mchOAysZJIFXBs3E1I0MawfW8c9nlj3FRQTR5EWbnJ_F3f-5BPKTYQqGnUn3mrCp4m68gjL2RhDZiDbOM4EJuZXo1NavMd5sfYYhldOGduXpX86qsJXvmE46gnQ5AtIpnsSPn7UoHkCunVwyiolUOhEXFfU4-chkItoZ_7ZA7WUZep_VP5P41DKNHv0dLcwdanLxERCWpYRy5ybHQR67EOs2o5fgad34d18CThWmTqdQMwHnGPf1MoJ9bX0Ne0g9HD7qtXmrgNeWJkUINAkXLIRmKH-W7we7wvPwrFCgT49xv8fZSBpaFfZMBuxKjUC_TgNJihNx0ZtR1ycSWcuMhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dp18IQ4nbxnP5CYLctZNBQF0QC6L8mWmuRzq-X3w3i04StG6VZn9_dgkgdapA3qKEZUKCHwMpfbk5NUT-WwCAZnu-LH-SpbefN5AA4kSWcZhVVRimYH9Ccp2uV3yzdB4ekWlmYMyOLJrddyM1IHkvHHr_Xihne5lmtv9n6-CjGNPly9-vzCl4ILL5nO1CimBGQagUMtbDEFUIFUvcj832B5uG3WRoWbd_HqQsJtoKB_Xm_n-ELY2zg9RanK0lPzE1AMxPf5G0zeNw-tJH5-hAVRfCH_ENV-ASO5UcvAczTzlKm9NyPBkzZ9RS30am8xqFiR1XzWvQB1DK7TshTmZng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HqfLqmPOaAUXRBOxZN1h_rv1EUZAYQnHkJtGoMPmRTn8R8fpkqN9ZTxQmNoNM0rcgRWdsAr_6B-gZE2U4h353xJXBlotta93VbvP376jMF-kkmm2yzEr6x72jIkLzZlrmjlB6YVAUZ1TO1k2aewW-awNOE3Oi6B5PaqucJ1uNuf63_SKrOhFs0RKgIJD9pDTK5xwMt16zFaNdKnLeRu9kQ9QmjRRSDwG412-FLiVBYbzJNDzAFXYhISLec4biSu1jcyMtHRup1HFO6fX0m7itefpzN9XBrHvT0cq-lPrtukciAuTdOZCKeMzJAE9i-0Dzc17CL-atmXhHNHTngyNIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a44Zqaj6Q9ScUNP1ILzKofzwkLLnJJLzaAzjyW-M9eHNQyuNpsOtBZQ6rE5szrQnVdQCjbJ4PDAikd7bLAXz8_XwXAVTr681eHXo_zTN_WdtqxWR9KYspRps229eyIqeMdJZ1jgn2mPpsJZFJ1Byhj4A16p3qT9TMCy_jHS5uEqSlv8JUiqnuNr5e_iAWpjKTvct54B4csPhhbscVKn5zCNNRmZ_WBS6zoxqdVjT4ASAiHKcUcVSbbWs_M7C2dFE0Qz_H3hbkHkc_c0vNzFkWvO420G9_GBDLZiJdCaD5YRUE8MdLXjstQaY2Xi7gzNBU-hDufp1ngsK_ZJQ0dZhRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cOsKMAL64s6MdkRRV9g9fFetubLUhcbL9KOrShklP4ZtzurUVligwNcoWsMuGdO-IZdRpvtc_pVg-p6z-Jb3pYWe56bAzwJS0Kq-mC1m_ve7tkLc57cyOUlR_H33jpSiyM6RkDzRipQqqjQvllDAI3a9iNHtBTPyyWTi6XWIBkd6zrzLw3BHG96dKnrvKbluz6fNZ5KHqLUFBeHS4FThcTGgIbjrogNESG-jsFJ2-XppvvTA-nO5XnO4_buEKGvdkzmq0hxGbinlJ4yBEbEP_fB2aAivkJUiov57uSGiQm7suWGIl9V-SVkyNocBiTZkH25nQmjANXKsdceKL4DYCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PW6P51VWurn2E3ZfEMtV4BN9tRWAfvHluJptHGJrsbTNaJ-TweHawrPiGy1IiUTL-ptitL66VpE_AKooxcHdgtIOZ7MC222cUfgUDuUE0APfACZFg47SHRwCoqAMAtKzfq_j_6KvuwJH9-FfR40DTBnC013fMhVL0ipHkoKO1UaY7-GNZr4CT2Hqj_ax3kn8Sg7AvPlYLqU33t8YRcgRBlu0ZxcR_98UHp53WacgIAmSPWD5qUpe1jkPr0wt450YRV3CBwlVgxafmGVfFi82K-QFjQFeBrX0hXtVcG-1yEJHRlGvYjL7WYRe4Q-D5C6pky_pwHG_3eTr9Nzv2EfVPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AqrT-PMjMgOzxxwwu6Wx6tKDOkzBN1awTn8CB3UsWHz2SSilbxxWB8-8EA3ngEBuW2F815WuM5igXIgHtCJNiQriTwr4QsuC7GPC0_5O-S5YiWIElMcvnsZnwiZWt4pL2LAuu8CTnRhnwPQEZL2klKgFWm_XGLFhnmbcyuQl7qPxLjCFxO-M9LtK2uqClhWnw6G5Dy1owr0V7RX1AuHrHmmHvjDBk_xYsdQppLp1YZaVslRdZLW_EmUSIwtYgiaHweps-6bu9srVjfHh5IgZlKx9x5wotCbr7SVAM8LBkcpAdrTDADT7lHYQnvaMNo3N8QD7wvzO5RuhXEo71JVcCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g5WqTEKTJFh_ZS1lBinZy9qCXdghfW4deIV9w1IOCzzSyXLVgOHOWQY6QyE-N-SKPJLOnCRV2VYBT1PAeavX8Yc7vNDeq-2cPStCwO6gYqF0XZbQqg337d_OraKShz2F-PXoU7NIm-wKbvYA309tP5Dg9zwAgvFfaM56lwbDrrbTFGh8VE_pP_ZNfMPfgrr5A3kjPP4NK1dTn_cH-HbRT-PLEfPYsQ-26-4jBnqbYgHkgZ1Taat6nqr-NcpQKGGpJwSfz9eIhM5zoOfTmaSoiyNFqkKNWCuWDvW-fApKkUYPTfZzqnd6N8MnGfGVX2xbKvFJjorQ-pwZ-MFVdM4G2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XZ-nGOTePCarQ7h0h7hpV8CQUic0I-2BR5JFrADH6ilO461i2oGaVrWuaZSgN4l24Cvw1Ex0qq-ZWpV7kK8ybF4K4h_dTwDCvq5SFYrDbmEY1stOt75ff1RHZUziInq5wtZ60tqbG5cwSnNqIONQujQAX-6rJ2X03m4dOfhPeuczQVwTf-FEovhh9RTGiHH2GAv8edC27nPdC45zyvfwGuXitCBHDN6UssbbGSXlYpmdAIcAIezpj5DH0SH-gDdpcGfc2kVdlaLoVo2YdNeLYIS9VvK4gkz3RlPluroDD70udPMGaIXNQ3KcfJ3xbW-tIKbZzqJMMacjC48T9q0UQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hao5F_I1YcKYVVjggexoqt18qcTRfzWOqGWJooqkHHYsPKbptugGWxnfOVvW-fYxRfGdlEez6t9VTPyC51nobSbGbhzFDOTipcUPulCqf1cYlmfFVXfITOGFLKJ4uoBIN05so51Bl0e7NVdoijUju6gUqICDe60FADR-dDmVy6C-1v6eWLElzPWE1H9HF0ksvVkYgG0xK1uGP04sXrrottvKQgNhMVN7ArEyTN-QP2cizrKFW1G-ybXuVFWVQPFo3mSQM0xafSRyJETdb5jOvrQOsKupWCcDpovv27gXVJZnouKRTHf32uyJyr--lDL2iBjBzfzoSP3zlxG2Su8ENg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ifxxGQEbgPvF48L04OiiKhu5ezG6qio3kIE-UKgjkpX9jl_QqEY7Xi_ZpR4-Kk64WLW1syeVHQVgJvkRAHmGxnpSKWy0w2ge8Td-LtK-dYNMpMStbUxic3Z1JCJCyULpvdHTkhipeIi_D2FSoPXgkn1G6zUs3ou6NNrqU931I3h3i0UigaMyWjZ2bLaOPo-EWBTxRuolAUbfKX4b2O7-1UXTNBcNFKrK5TiX1QejadcrPOv7qzp7Cj7DsZi6NssQpvCIP9TgTckmuxu0JivH9GoVvgQwZDLaBCDmxmqS0Tb0nYXi6_xY1JtXwfq29azbNdORhLR9F5fS2-QKiqVZEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oRbVkdQpJD8VyOEgsO4c2Gs4va7TodlDkgu_W5Gd1Gc5wCBq6_U34Gil94xsC2fHXChw3a5dZo7qLD2k3ml9dB-91cQLXy9cJmqvvSkUQZ34O1U34aBOFzTTO-8B1-_NdmvmvrY0wiVKJY4zX9SH1JwNbLD5aN9iyuqaMBQFpu-g1wfC819Wfq0_kIZTW6IVccteR0JCf8q1SMKU7laQRzVZhjxRlygOjrY2i2H5jz38PEMCPgnBswiiL3rxs3UZGA1U_aqzupZgrMRJGyLQEh04-yVxDd5s4GuVuRVTlmKipGFSj0WJ0SiiPXP2s5XYONTSsLCWonOlxDRBMpsacw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V6PZXsFnvtXqIH4KhOHBK0UvL8QqHw4IUFeJjZwkUtHz9cVnnTiHEb4p6eqg0rgy-6X40Pbv9SYptwpu27K3sME8vB-VW5PJP0wwPNS3t4bgJyQLan30j4zloyi51iYXLzOV2BrYYGbkCH_X2Z-HQ802PQyhwGM1JF_T4PJ5a-VougXVN8uKIT5223L-SthNlBAvQv2V6jppllfUa6g5o_HKn98xrh6Z6Q2gBD7g1Hedm-zys7asNm5RhiD2-krDhsD8AxZCAm3vhXH-CWg7DuyZVGrjbdaApHJX68eghHTxV6f_rX_7UWpOxup4Rm-DS5-OE1E6hrO1Xyb-f8C4tg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cFh7wtzE54GjQWF7Y_BnXq-UDErgj4ixfQ44P415a5YXbsR_10Tox7f_YSaPxoU0o9scaGtDfRys8x92pzqvqvm_4Aw8I7zCjKnZmdbptg8U0ACuxSQIOgqoQL7RgXNVW7TZWXaqmprUsmC0FtGYR2Tu9no9kTyrKKivtPLsvIvHblagrwemsibUVuGnEDhEBYLCelGrEjF0pKuJS3TfRh8di7b14mEmkBH4CkMYXmotpYneMJqI0UHj_srg2DCSDPaedGWgE181CFDCNd9ZCQi-Kf1xTG5QPh4nMkBbkyMx6wGDC2D_TqcOgrozvTTtrOZuReQgzV7MwN8zjuVd6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oftKz-Er7DiutG-jMzWacXd0vxJOpDU9eaR0I36lpiHoK2dK1mwzIzyDw8YVKxoWD3U7bYgtsKuDLETu_SrBU42IfA7t9xg_kRi-uve9g1XmjUMhv3YK-WdLLdxdO7jS9acGN2bNdDd5Vf_T31b1rYu1l__wQrIDtMMx8JBB-osNQdlcSP6L2bW5jb1Ep10vhMjdDd4Wigzzx5xvps3H7bnxnF8vEjZz2M4bPZAe9zRQrY9Zc0Vs94kP2Tfsnf99JbuE9V2sMFQjiV4IHXAGehpfiXPGvm1fRmBYFQJluOY4klVJiqsRTm6Yip8dlnSdG7Y7qYIGxg7femdQYijf8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k_g9GMQKm61dR4Tts7WN0jZcCtBVZMD82ltLEVnz41Lx-sVqxE1cIni62PC3oghoFQ3iZFtehfv0U-yZbaEwPW3H_yhdN7EChsLic2ZCfzY5C3NpNRlqLKNmaJa79KfywktZrfbcQ_NI4jJtcjWQh7VeMZw4GKlGmZY01VSmu110GWVby2hFoHJwrl-knQKQVdaIXl3WhQuICJ2XOG1ZkSH2jSC4M8jnT0SNVC8gDmvcN0IVA9lK4bTHYQww03LFCKEX4PGSlFSjqc4fuaI7p3m3dA4lr78hy6L4RIdGuIVwxMPANDTRd3Z_Eh9sZBgo6fDzKi7jq5Xj7qz2IvYMog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KXttyoRSj2xAxxHn3AaXxsQnzTE2T8cnMU134iH6Bp9dR_KgGRWf0mAWjPtdnFtDDyqM_ZbkEd03yWMOUNwA_UAXDXTip4oc8eD9tbsYD7uFWttWYu8oIAo8xonggAcZHU9-OHAz6R78FIH3GnYSv3wNBvxpil-WOPAz-F08hMFzrZfde4FaYR0hnEizTDG2UBzAHjp8zfbS0I_FTy8tYfjGqsry7ENVgq3J0yz4qLgcwBZXhx66zlnWScRBcxtmc_z_pUBBnNQtfhVVEa2HjaJRlPfXDWwBqXSrY2b0g1u9r7f7D7G9C2cpNiw2PgHZ7ICsnF-nUGeRAEK5bwIO8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nDl-O2pBcJbuFk3BLYs52f7ptVNHNSCpd6zPMh9S9w34RFHY3KyfLUeF4jaYKNcsjAwGDKWJHnPblSaA05LDOzYdFSOzRucCtK9hWu5riWtlmJ64KXr2lctQ-H_FwIYv0Rdi17IlXzcDGanPCcpyylJkzjmvZDIIFrpFU0uG1ks_MK3_8bMlCi2Q94OXghlAcRL6p0r1izEGy3-P3GYuW-MJiZeDoTwYkTA6lQUw44sXbP7nC87NrXXzD3_ytOzO2lQWZ6QJT6J2oYGh9Bl70E1fP5v-QqZaffaDVyok0lt-a3mC1I-E9XyIh7CbO0WViiCBVEluvQUPOUaAHGcfdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JhD445S5I4kBy57q6Iuu9TkqrZKGsGZhbaZptW6OnE-QLMOEFeQHcn1dqk4BHQPpKaV_0ySyNVuOM4K5y-lUv_LlhiHJd8hAcVzIcFBHQ5fIC3xTLcZUEyt_RLDX2bzQGGcYjFx3I_6-JuI9N1d0tms8li7HTotruWipXwyHuYtm8IXN9E9XCZFEP56iMT8v2QL0mQLMjs0gMwvveUWjxtQCmLN-gjmkTyescvSK0W3Kf1qfAXwhdnqRTr0KLNR1U1DUBkhkEQlcLPqbebqYC0C7U2o0SfFd19wn-6egbK5dkTxhP3dGNcMqU7DVI4wAkp7vCgkn5xkPO6YjDyyz3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ov5oAwkoYBfwnCADintpsxxHCo4A0Opjbw2M_D-ZdNpXbpzkOwN2aF8fzOo5BeNV5hzQ7DFXZD5818Ky5dyFKu53kar_AmxdKzthA5K7usTfNo1z9oSvuMzrr1dsAUDpSKvsNoV9qRSy5z2WZoGK-nXMFj62kuK995W99Q6D-E_BD5MFbpXkyMv9Iu8nEdlJrez-ULWDwkw2m7rAqX6uKzN92Xj2Y_Jje8D7t_ciAC_jMmY0FJLRueb9aHyPP_o6tP3QPrnr391vVvJsvjmR1aw3uGw0kpkz56qhtGpWTTppyukSWWNvOiPOhC6tpfKwhOJtBY9lZ6XOb4YiI-buoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H8cdKCJS5gyo7M_CS_W_f3EeI8lz14GyrtFzg3KtLgdkLPM3oodlHaLtqvFHBnCrZhh0KWP1qY12GGuqGKXnrl4pVbdQERYRrVOWrtptVsa_5vr1DvXH8t3Pn_oRm_by-7lkAVAnX3Tm3-pB_hnkNY4d6g7MXsQo74aHZucG78ko8lEQzNJNaRrmslDl8npqqybID3Jznb1ICpCLbLzJAZkhk6mphBTu8mSSSTsCVpieCfxgi6I3_GSRutrfV9qeAix8tJu-H_iPRlwPnSZQ81WH-rKT7-08ntGhqdamQGHY37qIi_HJyYwy_qam3a-UOKKTQlD_hJ4Aw-phOfz_4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XMpUKk73F7xUHV9RzzE3A-FNQzYNXbtaSoqwMDNmbkJwKgQby7_cV9cGx5bJfTmP2CM2fPWknv31hX2H4-H-aHtHu253JDSKltkr8jdPao4VIrKjqGhw3K_pI9JM7WqC3PnsibCaXaBQj4tjyxy1kPk-QJ5FztGK6uxBM34M3rB7ia6a0KLFSQE-OxayTaldQn2VcBzbOry5dJWB-ps4w-q6eVrXsfVQtnlrS8UNedFeFQFh9Q5kXrlmUk1-CjMYY7cg5aKXPuhZpTj-1BQI_8Q-jyuwy6y-KKL1jNPufardwOJQvBk0hGCBOtADh2gSD4WTgfzuQWNSUShXFDKgXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qPbRKBcP03sCxo26lQdxDx0KFUa5avz-1NEiiCwe5CmSCD3Z2kjB_YqBUSsU5vnFbOhauqIQdyoTk8tQVYD1u4Umhgv-m72dZTQT-IxeWhbfXt-YnCZtcJ9DS68tHDZJM6jlN1Bhm812y5qucNK8_WOzIwcLGr_yvQG_vr7xf83za1JPvnXyrNlBPuHBx4LABfFvz4NMDYs30TAvcdT1UATPgZ6s1NeTjUmzse-Y1h8Hc0tqjXFS_hzzpVCgoi-Q4Xj3FDyEEurF5ok9T_zM6_fJGRDH2kGpYQcwQPIKN6HAnqkRHLR1IwQFOYt2cAHM0ycDltHQrhAPIcFhsZhYiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vo14Nx16JjMHNTH_H6ZafLZhidkZO-mzyg7tg5TcLLI1lNSQu00NZ3kcJ45ls5Xz0bhgFQgBCLnqs_6FP77JVr2P0Tm9rykvgy-i6vc6f6PizSxxYPXxZjfwJsbXiVY9xoGeSIkRIIjWd7DsulilsqvloB0uxttJv8xJFoWGIzOKXrtvH5zb9tI2T0MbU7CiZt0oGbKwMlZd_y1Z7Ln1ZwWbyI8rYBC24NNke-KWIcZ6gUQjE8ZNOcgaREy4iSUq_rSlyZY21G_8RYZhCSusGjmk_6bb8mBDEeVCGejTU4IHp9L6t0hUrNlc_hhlnF8PgYWvUFzQwBbEdDGImarqEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hOoJRe5AUdnIQBlE3nGnWR7_h4Tfne3RIZfIaFJSxCFFiipidK1Zgv4rOj-TcXqP4Z8P5t7MZjT4Nksshk3X06IekdoOliv0HiDVFiHaJKm86dOEjl-gzEZtTR5cLv0optAww_xphG3sajJb3nZ4OQactIteHIU2TWZnPXyKmhevGI1u225aY9IsoDlheQ91eG3A883U00jxzmPMHwHZzIJfyXUQpNhuV3l51QrhvOrCzfu81OgWxiO-FSOsH2uZSRE8IqdQ48hbBBBKfadu88UEaQU4Bfht2gaodz412AKWibN5INW_LnxCmvUqKwMRLT445a2C1LmJfT7dgALYZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DpKy0B_dKHpILAAdd-Rd40T_9QTEDPKnzLSwazi9jZkIMTnetrvBwfIl1pC3CuKPV_aQTkK8WLYUMk1_iXbeLq2O97twQkxxmwQTB9eJttuzp_NOfEtIvx9sL5Gormk3sGGpu-G2oqhHdvMS7qbhU5mJFWpDaYEnfhp5Ii6YgGcaFx5rpdko4067fX6CA_-9bSJaNKm8LGq-kI7r3tYfbLDff-kPsXzwY-jtzqvgWTm9k10TTe73NhFUqaYizWxyHZ7Tjk7-Kp85Wc8dvOILGJVH_s5S0FYYR7136gSc8Vtmf7ETF-MaIn_fxXv4a27vcqw6eQVJvKf9t4EoNspEEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tGuHxonnhWR-uxfigRYNzvU8CZ14XfrX_8iM5rQF4FC4amS3xNLq9thSt-akw0iC3An19WFsyzxfcPAsBYgeAo7qLD-7BtFcW8Rc2aE0SN6RUzt3OOG8rtw8VXnEiL5T2IbFKZsvipkkRSY5zwblYQqNq4y-r1PN-yl_cRaGWFwWyzDMLkTDQMDlwn-MED190dIH7LU8qfQPQZYW7wDqynxc_l96_tCp1K65IyiCUSFUNDGsvN0202wq0cLuHvs6_OtHUo5Cz3xA6eP_IClplu6YVlaG8lbvgIOdwoYB_ICk2iGao4TtZTPDqHCHGL2VgodyK2dg8K-xmFhT4CJrcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NSZBaR-PtXiSI36aipYdpWtLrSpe3cd0adYdUMvMx3Kpa6PAeJprJUlIkHgeDheII8SAhnwYi6D0O6tmS9bAj4VzCRXb2zKKR6pCKXA-76QeEm90wv_jxUShyivSpPR0ispzPJfLBZxjU77wZR9u_M8GfmNfD9kuJc5xlexUikAIig0-SPBkFpGUemHtimzoiKdH0Qu8ny4kFA4LFl1guA37MIOqRc6eImUy-rNfi6r0RWCrcG0pCBrpbdxLs79NQBWk2RNWxuB_BUsv66zQ3ipJgCsuNmYdxcRmBrnb87cJz01A4iFrSmCW7Eg5CaytTEnyX1y6vmNlF3F5lUGEkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uVU9sn-EBLxiKk3M6vB0-8JvoLtgv1znMXybTNoBMdIf_EzexArOfvBwCZlquezNHq0qhbhwBcGMKVqh0HyCrArUP54CbJzJs8WUXAYXXMvSrRwQJnF60gfgvEk3Nam-IYYhC3w1s6CyfGVLe6rmJvDUbzi79Q0sjA7FuF1e7IPADAv_QcTsY3DIjX10Dl8WNNKQmkYXlR5T1qz-trgBKexo2bmeG27iHtFP0rna8iDnLCugkD0tqE7w5IbjRXpJYUV8sFkMJaYHkzdwMptgPYpYXb692i_pdHhLcYncthlWueY3ci0Qu_zI4LtbT3XJ6CBtPghNhJ-wokGrOisgqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zp3ShfQbQs5ucKDov-oY07NOYUReuAJf44o7JU75-o9qoL9Zql1P-GK4s8uMZmLsxxAqfQIe2WoSeCIAwBYSMg7LNwmIsAAagw8eknbKgDsLlFqMiPWwWwbP3-68kxKjgRAMZok6PJNunTrjAw5qwnIjVbzWw6qermPzooXQoUyoAZaoSJ0MaBkbv0VZ4vIEkkX0rAf2uIVFAsAhgSJpTGnp0nls_vsHNcikDtCympw2712bTEV1GD2W4cQ7FG7uybs4ZzrgzvS5onQwliQh_Lo7xCqNVY38FKqsfDoEUPEIxyuKAty8IjyDupYBm4YzJrMZnKcwvuwXc_wrUyzD3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZN3MKGBtzpAcySGFZKsCj6shhVzbl_sIX55QTfDGUQfl-MZJ4p5AT2Jfz82RMB-Z7d5HI7yyu32a7bHai2YfWFVhxf7N_EPW65Bxa5TE3XJ8La6j1FMY0vyKw8i0HkvppmGP6L2sEjg9dq7cGm79FL3d8wn2esCMZg_muLG6l-Axwi5a3d14xeIsI6QvyBk0GdfFMh9QRIckN3d2Io7KbPb58Ze5eRMVl1CFm-eerrUTtkjHxez6BHfpxgFVfo0Zy_cP2elwUPqDxBEBx2lCWACcKqTuuJe7mj92FcVzJD9DejkcabNXWT7ZvUtG6o460KlpTFjGq09Ya_7Y4dE7dw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OtPW5nMhFr3izXzA5JwHe1rFpyyCguIrgEHz5PYMhVS17kzzASeM3ubGrhTUvAe6u6_yy789dRNBrvDiSm4aTGvB9u5owop6hb7aspFglb6_CZht56zf06bvliaGzLAXyZZ_QhAcRjVAa4ejSiinii0WFyj3X3UJJqpaIUCwGy0cjWfO3Bu3NXpgSYMPxSX0vDOt2DAR06HpVwcEiYDZ-Ndoy-hsKMmWMIgaJ_pOc-guR_9a4TwfbdwVTc0AEqE3FT0-EzC31dJ6mqCr-eAqi8vao2NhbdHD16yXAST_hUgPWBtrqjoR6NSuD-oWriIR1IKsnOMLHdlPtoZkQBy8Pw.jpg" alt="photo" loading="lazy"/></div>
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

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
<img src="https://cdn1.telesco.pe/file/hJfdyJvnV9ESewA6m6U_zUBipn821GOEBdhcqTcn3WpqvuKKqfbvwdpAAASZ-7vRizvb8Uyy6rU7yu5HzmGWOO33Ri39tiZ8xzErhNGGs8h4eAROW2EGNpYdTFATeCUy0-iqP9w7wzTCR24aoYOIQJ5ykXMp2KhZZy1OFONuIEINJil26SrIGB6v8vp2quF_ShQsUUnuPJUEYh2qHTxujIKd7f3Sbdq1RVuQrZ_VfYWOlmXappUKFqqP-JmuQafJem9wCpX3wEyw9iVKlqXb4WDr6vaRQIKH9JPiz_b2MGRJuxZR-eKRvaL33MroDIPLcpV69orywpU6Uj0F5lK_Cg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.3K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 05:45:24</div>
<hr>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gaMIom31u98RNmYjIcfqBjPjLGLg3K2IkA4dGlEM4gFgfEgYrxC9VMMf7YJ4Pnyr1RXeY2Y_4YihsDO6vBVOmaWRS2bHPUQl2rhZ1NIS3MweEWIzbK4NJXRF0MwsA5bjj86vwYwqfbRcph0lwBwwLsuNYmjhx2gpT53103c1IlehB0NENnEjwNWLy_-y_SgEMSchzlAbSVT99IdxXwBF43VxIzU-NHyNa9dQmQYw3fenuVywmahxyXRjkL0QQD5izVsvFkvXrmZiJihpaOV_qxGuGF1U-a9vHwOggIW8giy8j2ASqgiFuutgtJzxygfaPegVr8AIVjlv0BmmHjdVaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EGE1LJ4dOlid15TLMffs1wAiH_uGLWgZw7EObk8AgGIE3CUd7vZA7ADv1wdFtJdQm4ITtxlAkyHMxFUvp29IAPniT6HCZvrrivDRwH8Om7Wu22VuIRUk7WAmKt1n2CECuKLe_diir6URRyfF2TbX5-vpYpOzZ7tzBWOepEoBO8t697j7szh04-_IKOqUE7M_6katY0gniQGvGYat_cQGg2GXQ6aRURsudb_29oMWJpYRQkw90k50NxkS7vv03aqwueF-_veRJ8Uh3zpLi6intO_T_xoTEn8xPvVlJCIUYWkc1SIyiKYhDIYcsRuu9hDaIjh7k9QO7E87wqA_O84PZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G-IDVZRKfc9DoAkjQAaGHLlXL8iay0C280dg0jnPLEUZU_r3SLKYO1H9_0QloLh1RrZPPx09CRh7yR1KRTI7ahgWE-PT2VvqDk_dABAnQ5aZ5FJduUwB1D_YgNUNb6nkSSNS24QiI81SpjQVXbvnXpUKX7o-5w_2gL5KmnGSn1NkzlWw1Up4kBCLeQe08HG5sSEuBDvjD2SzcqD9GfrnMqbuF0PqKyE3UDydQeDqGBYD6kg9upobpvIoWFhpFg77TMlrU7CsyQzvNkAqaQsP-J9abFPhudHo5mtuP0HPHk7nzrUEiOWnXVkAs5zFoSvGZ8WG_UFEzM_O0RwI17HAew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vtBGLB_HRkfMny4GX3mrV_zfpu2dTNtK9GuY5aBK_cFvxT9uISJ7KpZA6xuaIqXfDzbYFEy53FPgTansqaM4jJs5NiMRSpSsMiZCIVK7AHJeWf-KUeSkdTa8Mzi9s0yalNq7sIrX4SyWR-LiSG40c0N3WwmY1ztETEAEKf7lXwtQsH9gvArVn1aAIX7EIRjPX_ikV46osJ67QUl0Wi90QLx4g50dgiieSvpAcFH9sDCwvy67oujPOyoJ-fzPKQxFVbC1odWizKysheFl8q8PXFTeR33s8dNJMceJfakFe83cMCduLL7kYq3pDOHAsdtcTU94PSZp-JbLKfNu5bBJaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ok4YAQuDx7M-qX8COctZTBttUX0THu9yRQVWFRAep2zQx60DLjFcB4Z4UUK6HYh7qBITzJP1qbbjicNUk_xMEk7AlexyDQsVi_dw7H4YpxxIRKh9AtlVUP3HcT9BNFsdm9f8K_xL5sG-Xq76ZhZdN4QQ00wLTNAgOF8ktF6QgkDw9YDYiALQe-jf6WJSNtA7vHUJM-5bZhWp6cv34QS7jQIh64vEgFqh61HAYahfaVynQUzFIgOlWXXl_EIePLRNSOggGJjmG5K5ATJqeS6a3WRNdTJNb9BWmdHyFw6XSlfgkTXSMZBCCmHskHQwVJpDWacoGBOBV62tlxPWR9JiYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IMfH2FlPDkzPXXTorqegoy984UYBiRXRAxcKZIHiRS2fkbFfGUyO_zjfr70u1cR1TvpP3dZJ290WG2gyccOoY-CuDVWYkjIBgekSXmCkY5_swgTvk3hICtxw1_eoWvnOKFYNvW7RyBvgICcrfZUOmmziJvO2UAx6cpwEY8_mk5fAn_gG28qSs96CFSKltDWT40y3PrkJtraoIFl9_mKUSiLC-vt-YYwKdawOvcKAY6m3m_hCTwQwRnxyZG9eFIVK5VAm498MxTKVq5aa9PcaG_L7K1UFx_uuyQBTW_o_T-mfdZp8cOwAv5Xg_lfTd9CzpjIWirZ1QHVeopAUzNcE3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nuku5-s8nohjYwu2qiGPOl6iQiapvakkkBUIdKmEZq89-5S8odnQ3tN7pffyHe4IuBH1d989c0qN9waGCQqXa5WgTBVhsOYtj-P-OfXrfZ_06wFNH8NxcFVbyMFutdbVUeAXsjuckBs0-o4D7tHnKY6ALuYbKghnkHWnrh9h8sAbUCx00PQ1hZMPHCpcycqkWi1naaJ4e7_3POLwqZlUOyfbNgQms4DwJD5AbYDyelSpQdber48PCAEA5cmFPzN5NRB8aCWXZ0GdG_FyN2qOIqDfdPg1DxReEXdngxo4LeQniBMjYDiK7Y1ZU7fybf7fbCZwtvfSbTnBJj57nUAniQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TQbpUy-fWzcpnqXYXsVzNBPsFGrztCUMu3uDduAXRcBgMjy0j5kZo0FHcbaD520wFs1hjbBKYwtlnimri-KFwQlnotaIl1Nxtviv1mJUHy3XgLuPc0f9uFSLvbm1Qtuoq9UX_I-nzxI5T4JJvksY691UKDrX9x2zj2DVkmQY6pI2to5eqqOQGJI_bI1_FrU7O9hW5Q8XbnjNX7eADbCb0YjHiJXSuvaXKFiUx9LlaICN-cIJX24HYP_bQYutI-oIBfBKvT5f73y1BVPEZWY91d-5XEpb3CvT3KJdqJi3LoJ6kijvfG_5H1q9_Nq8PUlIfLwN8mhW2ktEzhe9vm8liQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lxbIiR5RpePy6b-Y6xxdahaAoNd4jyOowyT7y_x-ssQZDc6rgcbkq89UYtDnTA-speyVXMmBw95qtwhuNWyAyyzm0gpShGX89txEIST1Qzx5yafYFiVzI-lgiLD-WQ7aEyaXHGSj0ksjsgKEIqcLJF4OVNnkiStVosLwkQTf2OD_-M9-Z1FZ3rBVr1h91HPv7tyQYqwLWtJv7ju5Y1NRrcpC5ft5Lk6BGU5-KcGRUnIzIiCcLAa3ESRIyNzOvm0GQCNONGzkDWIZdgNLrb-UcR1tEzmrYF_KSB52gAZuizqi0O19EGv4mXYp33_4FMWlsEU6Gd0Ho0Co5wP-riOu4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZUeCCGhqair9_YnMf1j8zsvBpkZy6oJ8tQYwovCZDIgkNC_DdJPdgkNpeT5jAz9NUFp-zdO3hG_AtVLDDsqC4B0tZBviBlLTGKlgeDI_tcdKMZsWDuMIQqNeQZ7vYDzzaq9U1m9IWhxiIawIAm2I_IZBpNmlyx5mRPFqihlPo1fr9bQ0d4e5rdygikZ_k9yAMkQpg20gnYqL9DwT8XlV-dpnIMCA35H5aRYTKpInLgfsByvhWM52HA0hX3brCcVuWZz36-xWjFEYam1VJcGZVQHYDPSSu0NiUSEUIcCNQBoyCYrbn-3PoyXi_6tETJfrAdNOR-oBTejPQBdukEDY7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dGr4MiIymZoWs2ET80cYI9XS8HeBoHF5-y_BkFAh_iS7cW_37mFnSBw9nHqTPKBYVi0gTFCwNFqWKo3rOwcwzq8HyyKATBinQoVLXxfCXKs7uovqFhOmq19dNXVs5PQhbAS9IU6do5_ts3JD6KFUMg5gMMYWDoSM-V2wzfzFiv528HDEX9O2zRI8ihVWxytMSwvqioQux6TZpsogK4gfqTJSG2CW1Hq3InKOQk-8LlwFxL5t4Ltg-ugU15_2iR2zEX_Fu6tpFgNkU7y_3_4edjPr7DVfuZH8r82j4av32OvdpR7QDZK12j-5kjshrcqzbWNS-qNgg5Ittx2U0uu7og.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QpEt8fA0vktyx3avyA_IU0epD_gaSd5OFloHIahKgO4KnvVkux2XNzTAMatd60A1Zi8_5t1RIcYmqyYVdfChiahJq0yicLftg835tjsbV8thApb-IXjBTL2J7AYWAwy3be0ulAhTDUJT5xtX0uQ0yFgkUHMVnPRE1djNqTO6_qI7iVHVtvtHlWo1cAOUJoxyr8fZFPVTzk5omvYxNbTceqbZeqI8GM6aUK9hO79ZwDB1I68jxwjwrgNYShCh19yKFppVJV4XnEsH5N49eSPoUbUeqI4_eLT-P_b9yY_Q5LV6QyCkXCIeWDOqstHJ2VmV6QlGbmJk1xP3a2Gyg6KfuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bwJ-AVHYC1ypiU4zX5uHrgvUVKJQPIitQ7p2cS_tQM3NJ7yDWsc01_WTyEI7GuccYQ78ZweinNZbyu5gctwgc1x168cTGXE2Hd60mJ3T4M1mQX5p_ltwPBBDi282mEDRmR2gSy5OiOn4lfZy8U55KHL4md3vHlu0Kj7xyC-WG7DgIKV7RTG3tyAwllSZOcwBZ_014RFF3NdDrSBju8uP8NSX7784H8-D90eyXlQRMzcrPSGUlVTItcV-3QjmaQDftCSAVnfZsPzhZgXXTYx8tkkJvdSQr-H50Z9xVLQ5bMA7jYdfMXdI749-4N6h-B4v247ulxseWf3YmiIlRAoOrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J7hZZm6EokYMWNFFGPhRiEa-wRnwxFz0LC78NXDhGZ8Qcl2OjpiE81u7QLXcGnwq0qsMUpkdcYHsTvKEEtSYYEDEQ8c07eT7KVDy9JBEfsiYs-2-N9L2qm1GqLS1dB78KxinpXTG4hb8pEWlwc3eaQmelTekBsUbdwuM-Uun5QoZbxfgpPj4wgylIz5mI1pUtnULb-zZMX2gVuGS-pDSybJTMAmWEY1cEWK07F15CUdpCp4JdEV_YVHweqmu5bC-wy1dW-Le-HNU-994v0XGZjr4E7N78SN9rwVO22O90iCM1Lj4XGIPmyI8ajP1eXhPWQMRTtUvmEsq8_EBff8Y7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gWXeVhbvt3VeTJE6CVeQY_kX2dHkGsRRxmo00urGIOLdl4a7aypd4OOmwpAXGvcxLh3O3lQJRDJRDf8IxCzUzIkrliIeO23Gef9Mt_2YAnr3xmyM2JVLELY9zZ3tCglUdhlmWN4hCR9p3URIMe9pddqRiX9RTdZ9WsRkWx1czscoVOJWLRSR3DQo8Obq-xXY6PSd8lAdoLlIs07v3x8o97BuFQnoj7EkEPcfbKHp5nKd4bHVqAj1Nn15ZtiMsdKkA-yZ_GEwoMhiX0RTnjACWF6yXQaCEn0zXvQKAJ4iiFEKkIV-VLs-aEnhoS9FXuJi4Jj31WWd2G34hcHWVLyChQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cQw5RH8-F9zyjIwThLymRDUZ8s01Bb4HkEycuNRlhLEgkFDKwSIIIi_5d8R04DLllJzNzEEa36IgzTgJdvhGOO1bWL9sxq5f4G1yDnTGVIUNQGfpQS2etYDogqbRXm1v6AActHb-X9gSvrJhdlsnQRAQvHnpIAhrEP_RU_w9EZWN82OgUWC5M0gBLnff9F1rX9H0zp6ADW6daxW0_IuoZIOlCmxQRfbxonZ6ylR20pHmG7amM9g_iBwa9bgR7fouxuw_mEnZW-Wb2PJ1o5mke9pSZ-cJY74XKL0iDq00MaSeqeP0JGbNWutvx_kEwnYg5RJ_flfKbJMiu-_O1j43xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DNBFs7cFQ-4A66qJ5Pg3HyrjTowpyzmNY0NcfnwO2OkLNB7ocAUUpSURMfkhsHEZtS3qY7wS_aQ5_RK0uCHEorIQ6E_2AHtuWXLOrIHvU98JO0Gvi-R7WJ0eUOkgihzGK_9f_CEXBR2-dtPVWKqVGbw1Q20hqfFp28qk-g3jWtR2LlT5ii-2pLez9lW8GO2JyZTUaD3Gb3-G0xd1qWwtEWu44dFF-_opmvheSnKrwvqTkxYf_2xxGmoJ6KQvWw761aQbu6xGDr0ZbZuWn9Ow3icF7czl0UBWjUvaL48L3bE1p07HwNw9q1CkKFDf9yEz5LOuMGbW7FoToz_K11GmGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aYLY_PgECSDqHSIe6_tmtc1KLEU_iQPDYNkJEcbbVS1oLi3GfakggQBSe_a9-un67v4lThxhVuqRtwddEzpXvYkalZHT5cA9w6hYDLUpwkE13h3l5wUPU8Mq6_g9LMDhjOgiDo8uih_Ci3tpl6LM9v25j3YgDVjsQco5XnkQRqJqG4h8vtQCqyBOLDQbGG9ULe2_gJtFFLgMefoLtTUbj1O3Loucp0ml1mow1bFLBY7fKm-T4Wdi70AHYH15IbT_VAqG51tiF7AUUADes_idlETtwasuCLtyUEzDk61SDcrfN0fb2rlj60e7jMvqkhdCK_B1sNjRKpOqJYyBBeSRzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OS9IU7GtQ0C9Uw_x17dI7YFa34cp-Vwa2UQZAJ1Kb43VDR-jOlIY1iNO2hdB5NEN-1gZ0sEAbXnL-3tBRXOK62DvzXfT3-MC4ys1i3GMnMggJNxUTT-N0ZKTPCv9HMMYwjJ9jRmZZml989mBTj7ilzJ4MQ-YeJa5lEc7d3ZaVXQoVViXSaDhAnExuwXWlvm5Cm-2QHdycKyBqiNFXTc5XQIsFSyo3W1pUpwrIaW5UlAwUkvb6z8ifLm9PVshytS8OQ8iWmhD7TpoYk0laqruPC-E-bXq-uHwAe9w8doUJHQ3-aQWzWHGIvbOM-BO6hjtq-sNee32C8ojbLxVYA-lyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pSK-ZptPn5BiFtF0VvbPvHk287gFy88gaJyFgpyMOxOmBMn-z--cM13_KV9n6x2Wfrcj9Zkvu7xYmKhXeU2ndsxjFCmwtm2i_T2amYwDl9hX0Sbp11XpgWTx-6jKd5PSAvRZwl2v4w2AvikD2rDdZkOiqOY7wtdvGnrLzbwnSNIoN8NNNcO7ANSzan6MtrjQ1FTaayVXpmeZ-9ffuGZWCYkFr2aqMomYdjj-uXlVvddjR2MGS_vnYbjEKmENQibEl2m7oS4cpZutFY-6rF8hGsxkc2KtqnSbSQKqHsGfOMw4ymXJfCGHPKEFmEL4LqhPXZFJ-2HLDcp_Ra0nEKtnSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZYjE45t2CIXj3aVcLjI5Nhg04gp0impha63c4BM_xmSDhukPkeEKKfL6XJyY0T9ruzM1zalFMvYnIBhcbJKEuEJxpkkmOhsuNIjHhutsrJxW-7J_HiNP-gg74I7WkTb8aFEUvPVXtzeG_Kpk0S42ps_LTKu_vyt5fa2Vzm-ugkscZs1E8LDFqRtEFdD34B4YKfAlJbTns0_FDWUyx00L53bpb4l6vnuD4z3hyPnGM8e68Ie_HMITk5HKHZqaQfQusH3QhP3vesKCi7uO-rtW15WvDwSKOAv7wgClQmD-iCe_r9SDhKYvcwYyKXxm3qq5kpi3UzmOmnZeqL_W7AvqOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aukKDbYTFOixPD4NGUJROjpfdpz-GGmCn4clXCtwIgT3lnqXCM-ELm1i30C7NNA3-N7bk72yod7g-Jmp6BiECU_1vAYBm0vCPzgj7QmdMdlKv_8qBrTg5fft1_O4k9T_lTJ16L0UtzdZiuwT1_ePggvd9tQvjGt4TB7KnafBbVhI9qndzC5A2x5w-hEs3TOsiutLkPxXI34lb4QKlTePb5xSlJlEic-SnJey9bixdUaMPgLWodKZWo6EleymWyQTvF5Xzegiaqkg0_xMBP7abg2C6tIz8XZswm6SShd-0S-uJQXmRaIip13o1fgTXg88WjPNUy7v4jGh09oyDQ-B6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JJlCWbzxT7J5c3Ol9gzHrguMVcR0fdypS0VsljnKquzf4AP477tzYswRMW-pgTgsczMFKnEjlYOmXxuTP0J_a9R6vknw20nZIVoGTIq-Et6JjHGAiiwk2cqJEzTFOMGoDpjsUEaRnXA-dTP7Ea0V5SNdavOUcROVihC19TUECkqwZsyW-JMFSsavOepG7lsgAuGOv24qNbK0c7kA2fpaJLyhdpZyh37omxQalqKoWoOWXtoTpNwkLvfw7jBE8rvikUjryCihXgv--oMYdRaRDW5gRUktXZAbzBPm9GVRw8WjU5C02yP3LJpPQULxjlHg5RRVMLx6nwc7jtC5aK22FQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IVpSq796ILcVwS0UBEe4qa2sP1HiojLDGsEDv45UZa95Iyi6C84tf8Yuk4y5TEOsWfrSXC2z7AWZiPoAlyh8a-jGJvsQdBOxgIzIp5XdowL29IMYyYE6wT7re2M8P1IJtDdpDLB8__A7XC17N5whmaTCtX5Gt8n52KKWZCdj66YbNMkUJ5NVQ_-RTJRQPoXtr2MuNrW0bbKaPIrWxghFoyVvZJJKSg96-FoVYNsQHsjIc4lD-KgXkBIeuaFVN47xc5asWvBuLeH2nmDJxJlTC1x1gEzZyd429mdgrt5Y0ykSoVqOLu1d31MFjNnBFRmuAhwMdrsbXsoNMJlXDNYYWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kTvHezJjJ65-hb8cLbHXgA_VOfoaHHdryCbfwbHfnKrifLJ5RWGa3LI6faO3G0tnYVQupeBKCIic1Jin6RYTPcjXdp0WgsI8zoKYnEz5GbUiAz7PhFLUC4nFwp1pACeuZaR6kq96vsC7Gg26JHz6N9Cgp_yHqc7kasYKCW-ezw8WwRrRnZwB-OevwpgjHrv5Ex0F9gN20Q-vKFW8rIeBnGERJD6lw-JfSfbNiucjt7G-ku9N8YsISX9sePFp1mrVUeUulVzD_7qTQ1DjavkKhKMm-6h4Pze4tRjXzPVnJBdV5HYz4FyVuVxWbBojUOlS8V-O-II1bbjha6tlkQmEoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/octr0t-29guEsWwRYuCR0Owruy4UCl6R_2NDtsPiqzXzVXWLQ3aNth2_WUzFowWR3F7gPbHA2O3X0eJtlsq1lbj7TgTY1_9BaZXp96NkB6QF7o4uWngQgmwGHQvlrDdM4hf2SqdfAe2E0XOuiOMBH7pWmpD9FWzvQb0HRr8aEfJhqq-qw5WL7HoF_tcaoXxceH6GV3wcDzOXX3HylwjbGWkrFlfCn2s3JWABUOXwSSXWYkhaTAYqX9b6K_3iYVz58WjiuhrGjpfApeH52oQf5Xv3PnQ52eI8VvR8mtxVB34f31eq7vvRdxxJyLumrCaXdrOO3l0RuGNELdI2H_OlCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W3pc1hDy-RAaZW_s3CSXb_e3dgwpXi16f14waKrNvsgFf2xqzqlABTuIXN35KB9Mq7Iv5BTcxdJ7ziXCaYjOXvAQdBr_YSQhMouc_f08_ZT4KauXjw6RnEHUlD6l371DX8xI95hQ7B96U9bFajCkrLepc0zgV0gO02wEiDgqJRosoSdsXfxS98AGgXQHiqwmqDouLR3zAI-lbPFlZUllsKhIL5dcjFplq-gjXiPR5hFk7Bqw8UAfQiCbou7OcxWLvSFyo2GEY-d3ch5E7LagC_T-eFWAR2cnghHMJY-On4FJFrldilkc4kpOUzSIhl8bg0nYIY2VxIRLnDqWxPaycg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ujQqrh_Izsx17zw4ZGc7ZMvD7P2C6yxgRx3PKTkVBVn1st7vKd1O_V0riTcht8j8WIzWEwdvquvodzFgYw1xgDoMX2NdiwFjUeTwRoVTayy9SVsVXLS3RM4aW4RWJ7hpoWsvgbhc5bU8c5PK0rheZqy7ol_go8D6mJu6FGoGDt33DUkFcQKrc6fgcp4l8EYpCa03sUT3hQILdBTxNJ3IZ3deE-IkJ9tzX0EPSy_8Oz7pN2YRux9aA5dJVd7mZOHnyqjH-M98HdirqSesa05uaBttjcBNP4W7-_towkIeVfoXCh5KUH98KxONa9StK46zghlSDk-Di3MpaXDm-pZhwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RYJBA2v8_97hOi6j-N4tTyHy4tvShXDkOns-93DC4Tp9vS6w39wDKXgYs7LnLwansuHmUrKhGQDDq26OHyiiUMi5DcnJ3JBjsPU_hE65b0tT-aMinJfFhzpbQ0A0gAd4nkI0FPQRL3ljBk-Xtw-AST06gokGCtsjaY0ADxcyq2WB5b1Zb79XCIvPZqqzQLN2kQyhMEi2MNsrtZWP2ph-Y6iPS8OuJlWIV9uP52TRehSiHaWEQglKhrvfuEKEcznazjrlUSfdjSqMmBzsn_VsIXwK18R5GYexzKMTn50usk4FQMeXxWfTHlf8tfUsLGYj8KiABU0on4kPQFBZRFt_GQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IO-N6vX0ABHrZlLLMWIxCy0vHsU3aXPV3JZG1k6L8l58OcYJUS8OAv4SMroIRNsXSjaeGJba4_D17iufJKFvY4DJgJ2ZOrP-X2vzDu-qbHY50O6jOWtQpiyyqfFuaTQFRLu_V20B-8Z3QmENiX_cMY4HW6bREQlTeoZA8Ncz_PmFKhHjb55WD8MMVnKIH2jRwnXw6CjVzePGs2gXsazv5zsfF2-mAXtCMbbiFOciTrpLlcwOfRpDC2UeuXviPYEcOW_qI0KRTzXJ_ozpR1DMQtxS64Eqv5gq-5Ob9iPwmhfYHEGl3We8llUdN5hJN_ORFgduhfLEJlt7K39khWAE6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SY18jxyE7yvfyjyZ0QzABjO75FMhFOv2dMSR9O7xj76Sa6kdjDbYiz0Jn2lxIObx_MngOlkp2sZ07c2vnBqI7DfbkeItXCZYrDZVywxYhYKHBOozGEZEki3B2lagMAUjAzqcwE6qcMFD083anCWIzxcYQkYly9r55coZ-aCP9Ph87urJMt0wkONqJl4rrG4av4suEEip9emQTemCMjWblB-WQoqLgGxETzucZFvtbmY5vorKBIsnDycHqxc_zOXSb4VIZBqJJCEtthEnuQDOsAWe5yu6NVTSNEE7wANDKoz43wzre5Lc4n2lWSdkvtZW7gW6r7KCk7SdzMebiyuEoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dEG5-LcX8ZJVCJFowo2AKMS_qIhLO7BBAriLkTX1Qnlig4V6k85rU6dO8iNXArqo9frpwt_n_ezCloiqjbXvuzAMjy1LBJnWEvZnOnuF9seazv7lZTae1TJxXOT9lvIBdftm0jEYcQb-whUaNPgrFeNB76fnnvYETxTUCJVfcSh5VV6a9UQx8Lxet7fRNXVfpeqNwnioLUfRtL6tvr5KG4Hue2ZnRo1-paRb3Adzhq8UqQsJGYGImxZ8qnw3h2ktei91gw7FgwxIEZ0Gt0Q5x4whUeagiKt5d3LnWgoEwS-zbKd8sOfVq4T3GaFiI4HYOqFwNWdl5yjV4LolmHkndw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jiVz5bxtTBs3ToYKIz44zQu5F9O3_XCqgJI4_BudI_qrsQACtvONWWj1NYQhCPtSJ4a6GFKsnDJnBeEezjvHzsb1mttLFwcymuL_QypqVcGXmnAzpq--ycCvjZyzmjceoZ9zQshU0SRk8dlglYaepOnBcIYHGgaSoWjndAO9F2rr-fx-bxZNJpmmFwM2-Dk5UesFU0_sbf9J44IbqMzfjTKWPMtMn3mTrW5fE1dAuiCj9nnICZLL8pI0MmCDl7Ey1Y-sRTbB7r5XDfNjI5VEdTIuHXMgwjkE2xR69pcqygN2GnHH9G64F6UqKCaFSy3w8kfH64eVrMAGzqtqttvM4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wb8nEtVvZWOOgf0dSUZY3UG6xDsWnqQ3Zf5hHePFvIVC76vJw1pUzJ6WwogCEN0FWQwASG493_F1qBEdzGkkG2iQK2quqnqU2uCB93t2Ngmk6hM07zdQ6cfGM0K4XAiZAwjtl_OMsXRC6XKDS6fRnEC10eqvvjlcNMFvgFwAu-MpcEAOFL1F_nfbY0GWnG2hirAcIzl1_Wmv0HyrYWcseZAvVnclOeZky1iiqihRVtbYwXxE-NDjmQltr5jrH6FMa_mNYeMJI6biIF8MGb28l8Nz-56WPKpH53fGJ7xQhmm1T4EmBIBgZP_vCY8moQv9dta7JwCP0IO7DAQ1hjqLiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DfF4KS30FETWpCuel-RoVmtGXbB9LCb7TDgyYRK0J8lR9tfHJEwFHvSxjKHkEIFLp6SebqBcDQEPlYly7QeZI35UIjwam3Z5_Rf7G8IjEhg1DzA9ndV5boKQ6p45FhBnNzlzXEUS0Wm4XCfWot_cWVobtvttpWYaiK8j2AufabgAk2h5CwjhbQ2MzdJDrJTjpAJOb4O4KnWLXn9LGacWjBcmusYG7zMe1611hkfwFcBZya5DUb8ik2B0iDpcY_WtPgbn1llhl3uGro_ZgCudDr_3R6IkZR_2EOxBBwnGgHdLbQLhUHGOnMq0-kZFfmFyuGsIb-2_0344fwPsj8JT-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 49K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=GmxDIwDaYZ-Rqdpj_CNe9xN5WPTwmXDkeARB_VP7ydEwU9MHwGg76Z8c8qUH1ey-gSMryne7wDtkXHk8ycriwyFxhg3nKhK2hVHmiAvdw-AXJXQO6nqOt9RMNI3PP3ADhWZl_H3s1C1pDLxmMYtnj_7bgXWAIiHQe5Coy7RWA3_6vH8UJMa0yO8fC_zkbc-gleNEiTzJJRY7rbKVmuXszWW6KNnObl5YDBbXanM1l4X4h-YgCPLvmh4RXGOC73IVpEKK_perZp5Oeam7wlTeZavlj0HBZierrHY11MrApKXwH3oV8N50HxZFZ-Ar3zdM-1kwvFUKcDmYRfWIvuyndA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=GmxDIwDaYZ-Rqdpj_CNe9xN5WPTwmXDkeARB_VP7ydEwU9MHwGg76Z8c8qUH1ey-gSMryne7wDtkXHk8ycriwyFxhg3nKhK2hVHmiAvdw-AXJXQO6nqOt9RMNI3PP3ADhWZl_H3s1C1pDLxmMYtnj_7bgXWAIiHQe5Coy7RWA3_6vH8UJMa0yO8fC_zkbc-gleNEiTzJJRY7rbKVmuXszWW6KNnObl5YDBbXanM1l4X4h-YgCPLvmh4RXGOC73IVpEKK_perZp5Oeam7wlTeZavlj0HBZierrHY11MrApKXwH3oV8N50HxZFZ-Ar3zdM-1kwvFUKcDmYRfWIvuyndA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WiLOk1_R299QwWENGdtuEBXwG5Z7PbFrR_EyeGWo0_Yf6gBsT2T5rUYj7GLt3gfSAeD3_5Hy7VhVRLC_M5lQEQ6jkqSq-gRnKF2ojXfSA74aXxnLM7gTe2SWyXtiDbvd_IQUsiDViVKTSXXiPbbyWs32I1pE_NhfMrBAD_vFYvcBBKZQ1jtYVZC639EVo4jsw4nY_vksY_L-T9-Y0pOOCLABq6VpGW9py27MzS9KZgPC-FSW0o52yjtkaLSGyi6AjnDus9cyg9mQ4ZzeT0rR0QVIWeV9UkzkfoZOD72FroAevN5bhYvv1wvKrlXVTU0pEQpqeRgxNoT2y5bgvDI5UA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UKali9rikcghXhtEcN18nH_gqqeJwEonz4jM_Gkig1KzBSFMaPQTse6ZztAOInr8-ZkL10zfCRTigKane6hXxsNM52NunyAxDP8ty3wySt8M8Au6lLvjW-waehtS8n-9PxzOrMY0RX-VtcQ4JqR18qP0y1ca8md9C1dKXVIGAEfSRMK0gLWBh7cJo4cQ1FBfRoV2LMl0d5ACvpz1MiLu91XTiHb5TJhWBoYlB2MocZ1IUF6b7QAas-Hi1js-67PyKFsut1ul5EkmjZlQXcB3fvGnYrY17OKYOXfdz9yide66HuJ9bu1wlYugk6mrcLHumLrIX6ua0hy_qVt7d0mdfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iSl5QNcgv6YQqP7L0UCsnZDG5tKEA0ynYbHInfNT5d5G1uJqGksQvsNLNF0GaY10EY5KiUXuj4Eri1ixc2QBA3yu6sqTWHK9TmdXSrM9vcFPCdIHR-6pnLW87kdt7nCvQJZF-8SgBdHqPo7KOCGvdBEDqZwbBC0tOJY-k-WrU-quUuJ-xB1N5P0qDJl5cBkycU0bmWdQXWawj1M_0L350BcAv0erC0TaVR-mfB2dlzcx8_2N3sN5kJt9PJt7Xf0Lh2OmfbGdq4KOE5Nn3T6vzsIzFRep1gZU6wePJc83MV_7dvXAP_gKEmRjNNwOuqecXeeG15ozcPMdRt2YkiQbpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pSP-YhJEkWtDrALra84FUC4dp2DTEE8_bIKTiZPN0rmojEkE8eYDVq7UaLWLZ8YnTw2p0i3Y-DzsywBoJo4xIYoEZyD-061gkU6m0L7inHPQV11VnSUzO1kQkcRig52WApre9hVxBUSNhKwr2lKJR7fGEy4kTKAHK1GEh2B-EsbepFzscnLAWxaABLCz-bKGVCkl1CoQQQi3nH8qo0eqa72r4uzfRNaLf_YpMGLXrkX1XPQRku4Bih6989BbJ3egOfW9jqQb3Hk7wU1oY2xDc2Y7lSq-4hLWphcnhOz7ru5PmeOQ5-yY9T5rSqWw0wIE0-mC16WFUbZ9Ken-rJJ7hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SlZcdOqr2SiKw9YLeGGu2lT-QoiY-bxWT7Fv9UOmTRxmbbxbWxEVRxnO8uDWRjFVB8HyROG85ZA0cC-HbLNkpvrCNg-ydpqobQrRv8Rq9YbqYEE039ts8frED16GsAycVbjEDZ1eMCIdhaVqi6fvvbnl_HEb_FOUuMd-aNXnDWDx_5BUhQXLH8l0r5e8OijvJtDeEDNiyE47Vibkn05P7WJZWX5fOECac1Gm0A7OySh4G3wrQv4JNFPWs34vFs9t3TWoQyN5mi1hAHO0f-Qgl_pkpR4K8NU3ChOyMCxZLoPW3zI4ei0Mmu98vOyXAcerXwW_9b-_1HCMqon6Os3Hhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nPmpvLcw9M46D0X2oBzqXP7lYteq8GOcs3mHkt-JYsUkpqPF9qwDiJhsLLAxyGCFnUUKA0QUBgAf6jLwMLkKJsftLIRKRiPdsph5caDadfZrdWPTdXyCaoiAf95BfV4OfHWgtcBC0sv78a3H-OH-C7uK5fd2aS7h_wlxPVCy-VNQLD9-uzBPnCEdf7TxQYS288u0INPO2ap6mtP5Uwl1tUx6ZJOtOOymeyIjOSapSnboF7mLAD4dVMaxxT7ozfes3OQn9xwTFQJWQBgR6cnYRDNO7YnKRiTlRjwvY-b6fHSbcDByHQ-Ys-ncRvapkFmLTVqeo-Yr2nZZqKCl3DQ3Ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/knX3EYfqDLoQt00WKgxiYqqzMd_AwnbVubEwofAndzOF9GUFseqWUaoe6yvzg-3LtvQ-EHkgaf7asoLlHK80gsfR-ieeaf8qHoQr4gegPOfUvDrq3FSYEs7WgEV4u_OjITQ2Dro-rRvBlEbHzTO5m_VNsFblEqaX23KzDuGPhbbhJiLy15AE7Y9q-JByt5T5dy7dwa6Pt_m4uJXvt9_Tp_pxt4sN4LrU84gLOyQzAeiLd8PVUWSUxvmZlEv5fBNXe5opWvzmmgHC3vPQegvr_VIAfO8yJz26cc8jkH4PIyosekmlmtyMn41Mkp_Z_PDSu4im4lIvYOnBGEo2ZUTLjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YCp9zXn5X7kNtSdLn8fnaMNr4okR0wb8YaLuHYAfuAoFI2HwHwHmjAIL62UicGfJWnWTbJYYsCjEANF5qd5KDsfr0hBHx7t3KDhCJ-rLX_t_KaKcn9rF5C0gbFIME9KrU0mKAcMpTwA2osu7DJBCv0SspJHeD-lkEyAK0q4NTUtE2U8-k6Pov8d4VIjQVKQtxn-qmuIOFIsi39oatyvAFJfaZ1Hb1_s-lDeKAoWJ-P-QWWBd7IL9HoIwHqVjj4XVt02UyhaO2aTJKoppdtwu6Zb5jMQwS9C3-BjaM2_Cnkdy6hUQY1-4ygUFH93I8M9VVn0qlx5grdw06a1-zn44RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GBOj3oSEU1rVcIB9TmKrOSS4lijwR5R37Ho1tMtKGM3TsfJJdMJvjWhtg-kEtdfeU8m_tckvi-Bv8k24Vk-OIjYmOKJe4KGYRmEUWAk6wn6gUa2OmdOcrZ0lrHv5ZM805h7z74Cxry0Rn9jyYcS4aUCkTXQxaXyKtT4p4I8r7KzXdqIRXqBlQ04bzZTd_3d2J45RUIFyOGOp2J50jewWZLPTXkf4kGgJKcfiSgE7VpqU4xk_3RulycNoHdqCnnXXr6QOwiXOkE9vVYXvdJ7fDDpumYoHuZRahI2Jtylvz7Lzcqq6WmHbAH-KMsDbEuMNxokuY2JIawmNBBiDPrtJfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t5aHafNTJ7DlIJ_ZZmnZesIqmE_bZp76tQ0YzRQ9tLSkaQ4JjhjXC-hKaojK6c8mHE1QXLuY6Uw4FuVl8S2WJrUhy1g3teUOEqBItCmz1LpXseeSgmhNY0GmrLZ3H0wEzTuy6v8TavE_dOtT6zJqdoG72x0NAmIKOyviYpghf1KTj3O659XZ4U--gSeCbhec1guKbY5wfjfomqOfc8zQ5AwZcr_c93-RzbKD7r-8sM8F1vfnd_-243-dcxqHoS7NvTfNnEJJtB_77_89MqniN7_Pa-X_Gc8pYbojk1sYPrVmeFoL0AVxWv4OgyrLTywLgOubMlM_-4Nk76IV5vVRew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QiHj0ffcnUWX4_zrA8EJ8EOnQm-AtsLSwu6XLx_fHIRB3-KJp1_R7_ayi49dEQ8bBeNOSLgIx8b9BQrkC4cszhy0xmYHM4jaTh8my2as77gTGFCslatWp0rHf7k2vwbND6TNy7W1_TuAY7PAUYLvPQI_kWP_h-BsCphurPfmGqpymVYzxIwB6QbrbarSEevNOif30SmA4UwXT0UGUGy-xAYPBkVtDf1vJGVca7vbcWrLv22FFTqoLRI_SABBnlEbWq7pRXB1PAw3maU0EKazJpTq_0-cm7XDo0UF5oHJ-O__zpIMDO11oZpwd4lI59p3WvP92EVs_E8--A8pznhX8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FMeHxTRZ0X0Ob9WwtUp6Nj9VXcXJATW_JB7fFkxZq2AKGxvLUM68fkpN6IYEJYSAO6F76qjtEn1Y3NyFYjhf_NaqF4dThj3oY2QtB-sErzHVlnJl3TCvPCoqlck1_9muOmGnkd0WMpJyjseID-z2gcnfEWCJhXS_CyTAmD-1qqGhc2IghNLrlVcFM4q7-dZK5wQS7niwNi5AMRLN8ZnWYMKj35yOqK4dpcLej7Sie1kBlDp49CFAOQp88awYqPUaxv5Uv7xALSP6SdRfRdhupr-tAbdvF9lH9t7q8sr-3Ryc5IGGQZZ69qikmLKTibWAp_-nMRNCYZipV7nsn4IvCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pVzpxPCOoIcyPZH5Enjf_auxWjN537InN7zLK0u-uBU9lIchSFMFLl3bKBDNxShmiltqZ_UxQIt6aaOAquLSBEb8QiAK3SfKP2c-YHaaooiAqGlJSttqNhRjzP-Oq1dV9vWUgO4w2vX8zw_HfPR96Qp8ELzzfYoyc3TzL2HrX_svp0P3pi2WILA1AFvCfjMAny4a8X2D6SKFwiyTdUsidm7h8VmCB4KPSbAIIkhPyAWvogIi-EWLzyPCO8lsOe7jvTO9-OQBovr9ih7LzR1VGx8_I6VeSxpQn2LFe1PnM9pI3OejibYJOr-9bYKz1rPUxf1NO12vW3jM2eaS8K8UZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M9QxonBfvmfFznrDkElAq5EEV4vXlwVM4mSaikS7rLTRAy7NRYvnKN4ujVgRujcwLAE9HlvDjilLJg57SohPi8N7QrR0asHpq0pwnDZzPnIoC6LjLHXei-aADLrgV5jJyB49av-6BuXIVzogPG_y8sbPhadGeO0MHEx5O66YXgfgmUJGxC9vtaa6Sm2QAyfYqwdXaRCwZo3900Ocie07RIYMBG578G6R6eEqTlC_6CTs0Gyjh79aI2o2pAdI0IoK6Jz6H9n2FbXVHG7mQNB39EH2Kziyf45qKBFLxQ5EOzBv8vgUosx4k4_JjQERkuWIy2e4wasrCE3wdZRjnsUN9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qlvgvIAwWtw_-MGVCvvySLV-9ndfUzo5bF-M3SecLmbD2i8gZaP-owHq-_bSbHaQgksrkHnbUcEf-1FN_FrWiXCskXVy6ZCPzCp5Rzjyv4nuBTkWkOyN9Nqns6W1jAJGSLmvHZa50W69TRzO_Ok3qaMP0dbpiUzHSQ6tib4v-wc0M1qox7l-aOj0JkzWt8tfIMnA9VgcWlB1VfwUmmI3oxrfTWaoxzJDH0CwaSsSB1yaxyu27zS7u6dwI5i0_YBHTjweHbPCWu2IQxtAehqx3keyE7sM34VepCKezZ-QhY7ET6XZc-5qPZoEa-Q1OiPHOpqzWCqsBOsBqujru6aR_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uhsb_JujQYDYhm56TxeHlRucbRTv1JEQNmLHQcP4Y_EIEz3AYeHf3_H4q-ducHYHdS3Iq6AW70sNXZGlX774mXrHRpsFUWYWIxB1LACESl6V4r6joC45kk6Pevi40CWUCXKTkr9Z0Pzvkp2mMQs_0kJOPpCbwU7dzAJ3zTXuBLbvG6g0IlncrCXjq1toy-k0IZ5ti4b0qVzW16oSv_yn_8tFQN7A5aSuNqiMRiatbadDMHCzC2WOBR8AWFZaBTbpuReflU6Z_1XRIyMynIz-_cqMQPOuYF2zQVT3SfyLhed9e2hkxrNCv9kQauzFHRToeyr4ai4__tQAOJWvIIaYkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o5gg1ogxcmsBFddvXuu3TJ891Bj5QFTzO8p8Zxy-x74vlQtFq5EY27wTOS8GhHZY07R7C8cZcRKxW97yDgIxdcaaIkGstw7ADSHx5EES-eqHxQ5QrgYaQcoVrzHTl0RR0wZYohWpAKk8Q8DwxvAgzKZqNaBPghGr5ieFAVaHA9BlOZxAVR7XXnxMdKtZOX1KUeE0WOVpO9QQbxMv3s2D8TvuaVjaaayCBOidtPGKJeVv4zggymr074C_vUvUJtoIM0-qKhdQvyl_58AWTHHbkuhhpTuWMD8nJlaM80Uy3mimoJ5U-9lUcwKo-Ng9Wsv7XVihHM7acMqcwkH9S6De9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SYu7u8wIJVGtOHEOpqRv9tXSTQ1Qpxf1lO6-Lv2HhfLZS5m5Kbdj7TuolO6mvL-bGhGN5m8PlUL4yBzKlu9Qz2B5si3q5VE0RtMgZLg0q56tqpO9YJxoDlQi7DyvVh7WfF73q5NAss6pDBetenogiqdLmMiUowl3r3rY5YH68LW2mLCjY9TdDqfUrHpUp3BAN4gni3cjq1jeTX3En7FFiCrDePiQqFWyUFrZ7G9uAVr67NUUstJZOxXri2Ejb9qOSbPGPihC2YM-WQGSHQQIfa-F95b_0PKQfGvMXC6YXQ2BwBgAptf__2xTb1kKrejs5Cn89fcxF6m8IOdmvODuWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cu61COhFzKAXJQAxJuA0lqQbmN1yVqiar1_RNd25iYhVVDrHUetistM56AiNw-fQpB89o-i2rYelC7OPtsTFX_0doo9v6mBiPI0sUqBhXGu11uQ9B32kbJJdlZGSYkeE1z6hI8W78u-T4neiwgY0ESVinzlbMO1EYPQi85YwreejszPVb591v_dvhs5hzYuT2zFgNc33MYvSNbA-_P-SNL5bjhEjG__fd0aWrZaoRptSoLBsRB31E0yc_LoE4YJ2JoW9H0d-xMib0N6C0UPbOtIrjnMB2tDIkznIfMOXsqbLoonNFDrotacCgSSsvoX2wY6em-A1zpJ_vAStSclH_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h8KkTUJsx7Yg8vfexneBnyJzeoQaXafGNbFtxh8FsBegdBC93Jt-gxNdsAvYZyYFWgIXFhqFcL9enDNqlMTaQVXcw-f_-W62dAyvgTS57g_fzpHgbqZf2rldcDEtfQG8TIn8Hh9VaQKM9QOn0KJyQrx6c6VdNgAaeLVh9n0VDqVUboW_DBBxcnhJDABWj6PHFkt8U79SQr4FQOxeEPEgFwjwBMOLl4H2FDcnPzHeaO4u7WwFxZrHavpxFuyNjVeZIUVuby3lMqa8LSmOTeQzhDNDDkwpwNkqPsvCq8d5aSOh_PpzEKLHVC-jvSLgleWxHTJLSTTlVZq3cgbYEZfkWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J_ynqvmH7pav-86rkWPX5k7kcQpzX3GjFkoRL8mm6npyMGfPiSYZ2vE_OAa4fxIJWq0VBlZg3ksu87OaHMe8_PrUpGz6czFZhOekCo3oOj2uC7Q6CmNTkR32NpBwEmTmfSCvvgWp3IRmKcv7OXiFkBrrRBTNxtFivBObl39d5oMPsNo5pdTBm7pJXs5ajPwYTCq62LzM6weKdsr86-pouYqQn2Qajwsi9HSEdPxRjm8rKG3w1xX5ctQ1UmZ2ZJDFs7gL0bDQA5akEgC9P1C4Qr4mctdEnF0cSRZW802qccaaVD72bbFLHCyiBRYs0c0XcSOEalwvrTsH8hEZZjYgNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OUjLNaJh3AOZSsZk-m3cwUpa6yQaN8IPOynHw_Vg7185zID7GR27amzwvT1S2iNfNeBJWeMUbItREFR5jALQvndOf9mtW3akvvHTqdnMDpy3dHHWKfHEK6Br_S_SPa1Sv5mMqPP_kdmrLasWwwXrtFur2HGjdKni-nWxuVxuLCc2OvzYypow9drS7qneSBoP0a0osDgpdi0wMk_pV-Ig24kbK9cxB4TlwGz94Rsyxm_kV0TDxU8Oyyu7HUemPxnyhG9IHh097xAQK39RoymCiEuUFezp58cHlHrzWn3I4--jvZisFUcvW-zXRUsIzAwShxbTw8UKgB7fHME_E5IX8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/afDZblF6pMGfqe08rzrwB5Jo44ENYL8zYhcJP8LMgsyGBIR681jKNgHiajfgT9twL0MyE4noE_Hboynt-83_PE2vP2O2qjgqjl6VLiEDnnXGzn_nOvobIGPeGMU5d50Kggxom-d5Xx1RxshD6N4mg0QOjORIz47dfxufgK-ophiEald4SwnWI_ToIKf6Gw6vqKXDy6UWdjvVmgrj5eJtEL1GEhfBggpAhYKPYs_LGrfSW4-oR54XNNiGZkp-XAXk2KQTM8rOaWcvI6jV-1bovHyROIGcOHjCumiAaOSEmhWjjOmsXC9KRwZMsGfAAalsuxawvkGSHEli1-GqZaUeZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RbDpyHPqELlQ21Asmriwf8D0JXT8nsEuT5FP8kNlKCKTqglVFOcF4lJUi2v3_i6BTfsPibxT5s4r0rzQWto-Y6JIe_l4Kw1kKWxFiFpQ3Yimm722Gvc2Sl4wr7QXpFfld6C_-vR4sHynCJF3FWOk2frlkHmnwlqhc1lRwVrg0LI8ecCcAMYHg8HWLyQLHVaS0SAXBgPG7DPrIVDzVlplMHQbdYEsvIOn_Q-e-AHuoSgDTqRmYE3uACDJip0ZGfdQyPvE1uCglkr51xU2yDr3RO5JjmRMll54BhzUsdk8f1LiVFNTeO6eQsyC6wS7AUjgan4GTmX5SG5dO-Lvrl1pcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VxCp6GnxhHpzKmnNCtF_g-Rjgh9MnSGj1MW4eYHH9J43usy-aF9o9ofpjPUPdynDbMqBR2nP3288Zgs5-cgxogLTanIAIUYZ6BSio8kx_zvjxQw8n2FYiJ7vexP0wUbG9rWBAufrIM1HX7xj9HcK8vFFXsTbIXVmPAzj4OMrKElDz_Jp1R_Sqmy83lXGeqO74INX2kOdR-UzffhMCxJYQ_5WQIEU8b_I7rYj0rjvAyqaQIl7tk577LGV-s1sEVKK0UXGow_F4TeBlFiWUzyNuBo6E_ttDPZY1C1LLt-pIOZHfewIHxDdlGk-FNk_RQ7E-C13km8N8kQlXFN1uq7MHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p-my2BBlpXytcu_MprRjmEZp-dL1J2u4UrMJqnJ3juEI0bFDg7Qo9gwl3xz81YxBHzYbPBndPU27e_nE14aBx2Y6_fPg1CB5mEo1CiUlH-Sgh8_5DR1dCtnS7Y_D5E-N3nlcwGl3hAbyuN5cD0oo-eJ5p01cvozsgGBotLEaK3lRBh6hkWhOuBcmEDKmLqw-JhnXRv4-fXI2iedDfxMvboDTGbzl_KgXcwnMb-t1EqQJoGclSvBLXWXfwYmkyd0_qHLroNcxjt6wuRySEc_Suo4U0q39MeZ5LXxMQA0qiJ-4EaDz3aV4WAr00TGMVv5gYqTzurbGLNbI_32kDkDj4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UfQsa9Fl_O8xkjrVXTREncsxnsNiqGW_7yAVwE9HAo6k3V1FBgMEo1f3bIJ1Nzt7hf0E-jaM6OxFbcs7qVrPeuqYp1IUfRmpllAJXCPEWErQwm4yJv-AgYUSDk5yGgTPFjaa7bbWv_LBCq8PVwmUqpObFAaUWm1Ta3CChrEJgv9vshPevqMnaOyqZ1TinaVWrog-VEQktYHgfs5DOxfsJs0EUBtH16aj_GOA0drjtQbg2rGvuWGh6tppu0iBBfWvkkiPhW05PBgqZcT1gviEox5BNfXJ-Cn1GxK4ddreV1xN40hGGgFu-678Whum9wwodqXYjjhMenP6ba0Updr_1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hFT7RThfxdZg_nrIPzdUHKb1PEIiKIBWiyGM8JaUmybZ-51AdG37XExypOJ-KuHxA5JwggCb4C4iZUJq4182Fom0DzpPwnubJSQa1RHzTvfFcw1il88fbdQe-kgBakKQ7s5Jx7IhEI8Zn3szsp6iSzrl4nCE3XO3sEQz6IIMhYSbPXD5BFZDu3jOuwc2vEOppQIJ3Gx2rrmDBlgy2WcFyA4VsBFOQ7FFhs_O80GesPO3EVMinYOkEl7tmQoR_RlHOTq5ZDucoJxywghD-Vn1t6a07d5jp9Qk8BVAJtWl2pL59esdZPT7bgp1Buqyb4b656CGuMZXTDeDFV-x_wdDEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BwThptWRh99L3mdKQsknzAYD1mlpC7dPdIIBg1A9VHtcQsaDP1iD5qI_5KX2oYnGmMlbyjpvgbvR2lstqHs664UKoYjxRJnFfbOMazZoPeDYs1tqMmi2FdWZapE4JkPpOf9x0DaBaLO8OroEWdpgJBbnny6yCe41e3ytlQJGIGHwhplvTCGn5c0L-rTbKZcwwo8feTXf2ZAeUo2b_23h4YV31sptuc8djg3CqvePPcapO1A7rxyG9M5oUdRLaED45933KBvvQkI3gFPdetutarsw-hKau1ViShbgbIhBi6R0nhNRDni1iP8ZQAY4cDkHJInSPcHhMbSxO_cetlyAwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dTgMcVWL5e0WTK8EENAfOIWcdSK3DU30pjs9-GZx16c8EQKc40rRccXWreBf9cFAJlitPjylMtLaxHMYFEVU3CWjZhkgoWZBax6bJwuDMIZ6AkzpiGrxmRgFPaf-tIfxm1BLkguwJOHz1kLJ0xYKIj-TtbzLqBFwc64dY-X_sUctk8pwpyzlsUW5z2vkEswCOpX9i0HzxgafYskOzLwXqcopAJylThEvblW3vRX_UQt0mgu1jCUKkZtB8xFDSh5VbPGg9SWudHzGz5wfv7e95ocZ43wj_C2zda_y0i3XtUKSF_vUck9ATsNyoUFBADNieG7K3gO15Hsuho4SkpGUwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HWdqmNiPxtLLhFpOabx6KoEcFuc8YjD1C3z5Ni_Z7Y-qkEhkzSsX_-3u2qVkAgWrzE6T2GDE5kmyU8niRizC4y3m_Mr08oMaG-lIeMK7tKte2MJ7Ainm-8IA9U81RYHvymIlvqzkJSyj8LGBwCjP_2pthmLjAcaadcbdIOKIyZHOVSsLti7vhyNoj2RhJD8QY16Unfu0m9101Xhb7v3Ayh1hdV8kW0RPyw0qRWoFQb0g4sWWzsHfKgP3mUD7Cv3G9NFh-RjAQ4LLR2WGPgw265zvRdsA7-Ujkk7k2SLeLL2CwHWtrIBdeWd5iMRYOFQEJJWw9DvGHAavy9yYE-3Kyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DInPYZrq_z_l07ohfFQwlESJlDed7acW7abhPI3nazvz6vNRSiY6pLYzMAJVvtYvHpo9c_ueQoCNq-yiZsys68sGAo_wuguvatzTH8ERpJ_JHuitnq8aF7ZG-yJjl3ZiU64EQJlvWxuH2Ek_3hIJmYAWHBsEELX7vaTrxStS58a2cyPv9bK0vt7kIXh-lV5bw6ljVNieNhZa5KBQFcvlIpA3z_nMp-WD4vBmkfCAjI9JzOfe6YpiQiyx9z5OKpPgMGwSw4Rw-DeAlN5ozlzdYdXvfXpxXxCm5dma-wLhX0gXb_lryX8CkqtW9IeRoe6mhURakd9Kp_ErjGdofDTQeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iVKFK0QNyvTAu5OvFEhlbKe1jlL-VrvDLnvVZ2KiEp0abtoNJBV1J5jBGMNgXAAVZimN-y_gnTHKfTyIQQewy1_B7PpUauBwrz3SfFRonkIAgvloeWAv4xj8K4Ch8g_-f20kvC60kS9C4ZiNB8MugUxoTXX6OtUZnyKASvCqMVmWXoUiB-9G2j2RZrMOUwNCFjJq3PdSm4tFS4_pIYCi8oWOsbAQJEd5v5S3GbM-6mulgiTuZWGIJiYb0Z5uTCfG_mLado8CREMtpMCDDrF5Sao5GZppR5LozN7D9-PCgk97u1XZEXomrScJ9SrQdXrgzu0nbzi7RBuSG35AAWsiwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bBI_uualBnHXrMQ7hdJ2wfv3EnyhioyEOh6Bpr6IxfFTNwBQseCfJmiEMY_tXlduVU49lelzLZ-CVcCZ7vFmAqYcTCqXDpvjA1-VOwIPezfKgGlw01tGj4UQSOt6uOMX1cKTpd1VQS3JJpegz8v4-17SpLJK672nfvwGC_5dIvyxSlkKNcBrwM0z0FM7xeXFy7VNQXMHRyQe_12uEuQRhaPRsb2AU4oy-7a6ggW1AR77ZjNLdpzcwroEbclYeDR9kZXPQYIghG5M84Gpz9YM2Dh9xJV24gLatpGR58YgNC7ietcmpigCXR3bMaEcsgVgO5agfnx3kUla556Ov4Ndkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aVJeMQZkgGRXFVnvvGZazHaZ9s4aKyhDiV0tpny8XcQFs6W_TeFQgK9ZvbHipbigedG563aH_zjW1S3c4Gv9_v7fbMoUH_yXah0g_UMRwmITTKIV1d_1PUq4nGNMV0-6eV3dnnnbG32z_3-PbNdXW9dlWlJAiQFB3qa_XYGHVKROPRyyCcqBX9sRTsi-POKLjatfJAp3c-0VFeJ0-hBk9SmxjbKYPZBQ38xV6Qz-q7JLNx4I_tq3JX6SoNLBNSSH2NLpoRqnLjPp4hgbW1FQaaQ4e26yeakLe-aU-8f6eUO-tf6A04Zwad1NEqGPAsjhk4kEMVi9DHM0m5Wy3e0WmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KhIwXqOppfJdcpLPy-5cMto458hp55S-PSVM_8uuIX4uzq85-qjFuHVyDgLn-6iipYsDtjX6OSr0L3gTYBUy2TTG_Aqx9-G85Qxfcef9asfIRFMdm32nTO8_ovFloKUC6PWSQgTZzj7AQmK0fQeZmp7HgVVMW92xp6zvpUibHuBbvuQXp2TRO1txFtNkUc2e-Xr2hV3RNPRhwPFd5TMaEJ-ftQN30k_1BoUrQZSo8cjqFvYO_g3aeIQEaVw4DTXzWTxwZxYjiAbEJPq47XgyBuuFOsGT6qRSRCSeeORxQj1JLYN6zF3lMESvsu9896Cb3Ly2X_l6zwu5LBHmStBqVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dkS9sOOnuO68wefsnTebvO68gFE7F-vUpO8IuUByZSgjjS83A69MOJ6iJpST2t7CT0xNrSqpYr5R7ATsDmLhyJo4EZq6WhOhZ32iyk-NFyedfp9XoY8orr54RbTPOXS-kqKvPqAjGs1rkaVqYmjb8PJyJbjRPrfn_Am5GT18OvVOvUusz5sqO8LWOLUvw42CLhHKcsZS5Wry5evENGKb01dD4XTObfr0TZZPEFrMx0wnLlxhD2IHaJBSuJAkp00wlphhQ25SwNch-E5uJlb8UDQpsTG2JQIIpYRMQYG936rw4nuWU3pVJYwZQlLCLqB5ndGoe7zIfCCubqkeKsINCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LoOwRCKoQc9yDjmOeWbe1NZwvJO8YbnsfRbKmqzRtwIQejdTDETCv0tw_gFKH5A8YdW7jQWsfEgArp9TstRqT7WBEngvLxeG8r4j5Eru4edxGofPBAUqT6QHst3UESe8OsijGYeDAPHqrfqHYBN88lZ7IuIqUzAMKyQNTm4nE-Bv0rkvo81TByqB1vNCeJqIZwTt21OiGEJCntoMy_PKSGKYyDcS_ZTtX_iDmRHIqkBtQx-JXFOdL2vF662lGhTTHWi_f6kUH0Sxnjg08P2y5iHY0M6YJ0OxR2vPxWAP1Zz6FLAOgHyT6vv58kxYMPatcN6n59SVUeJsG1zU89V21Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L1Ye-Cb84lGfwEXQaP3brISZjkANY_yYmXoHSE3Bio6uqO4ctfD3UY5UO_FRo39zDeMqwtIQmJvjNj7v2N0KchnZ-OTi4DuqvkobRCLZ0Sn-GfVMgUWNUfUm0b5oS6Ojb3Hmnl5Sj5P3TWP3m9FiN-EuQBjVhqwtY-THEyKmT2Dwz96i6pepHjUybaNSeqwmQ5eiA0mLd0BT-wSOZWr5PE2r2cmGfrpw0P1xuZlgHfYEC2Qd0IoHZ3HyxP9PBIVepxmwos_wASzJFqUSTJv9lHsKjZVZBSA1McDDEhA5X0H3jI-FOUOWXEZAJTQzqV8CLUp5DmYXM7OEwZslEDxa2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ dicodePing یه کلاینت متن‌باز و رایگان برای اندروید و ویندوزه، که مدیریت و اتصال به کانفیگ‌های مبتنی بر ایکس‌ری رو راحت‌تر می‌کنه. این برنامه از مدیریت سابسکریپشن‌ها پشتیبانی می‌کنه، می‌تونه بصورت خودکار بهترین سرور رو بر اساس latency، jitter و سلامت اتصال انتخاب کنه، از حالت TUN/VPN پشتیبانی می‌کنه، آمار لحظه‌ای اتصال رو نمایش میده و امکان تعریف دامنه‌ها و برنامه‌های خارج از تانل رو هم در اختیارتون قرار میده.
👉
github.com/mcodersir/dicodePing/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پژوهشگران دانشگاه میشیگان، دانشگاه نیومکزیکو و مؤسسه فناوری دهلی، ۲۸۱ وی‌پی‌ان رایگان اندرویدی با بیش از ۲.۴ میلیارد نصب رو بررسی کردن و به این نتیجه رسیدن که بخش زیادی از این برنامه‌ها برخلاف ادعاهاشون، امنیت و حریم خصوصی کاربران رو به‌خوبی حفظ نمی‌کنن. توی این بررسی مشخص شد ۶۱ اپلیکیشن بخشی از اطلاعات رو بدون رمزنگاری ارسال می‌کنن، ۲۹ مورد دچار نشت ترافیک یا DNS هستن و بیش از ۸۰ درصدشون هم با سرویس‌های تبلیغاتی و رهگیری در ارتباطن. علاوه بر این، خیلی از اونها هنوز از تنظیمات امنیتی ضعیف یا روش‌های رمزنگاری قدیمی استفاده می‌کنن.
اما نگران‌کننده‌ترین بخش گزارش مربوط به ۵ وی‌پی‌ان بود که فایل تنظیمات اتصال رو از طریق HTTP و بدون رمزنگاری دریافت می‌کردن. این ضعف میتونه به مهاجمی که روی یک شبکه عمومی مثل Wi-Fi رایگان حضور داره اجازه بده تا اتصال VPN رو به سرور خودش هدایت کنه و تمام ترافیک کاربر رو بدون اینکه متوجه بشه زیر نظر بگیره. به گفته پژوهشگران، ۲ مورد از این برنامه‌ها این مشکل رو برطرف کردن، اما BambooVPN، Free VPN و 101 VPN همچنان در برابر این حمله آسیب‌پذیرن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

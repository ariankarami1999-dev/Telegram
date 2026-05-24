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
<img src="https://cdn4.telesco.pe/file/aQK5tnMMF8zRpzGEvUDSLaf9u8hlIPjuDaulWfYFM9a4bDy2kbxBlGTSCiEzGLMQuMJOBHjaFCYCScQ8Reb48XS9iEcGKUILJdx-gJYkKZqwKTkYgr-sc-wr5cS3GeB0VDWRUaFJBHLvqacvK6XE1TbAO_SFhJpHtNQJMUyczdp5JIa8C6YHNmcUDzsBItkIg52RvAnya1dM4GZzr3nH5JE0LI80OVQuDU3RO7rT-3365Bfo64gbMJcMHLEtdaOP2RsvMKYfiJH0ngE4ubUtHg2Q0eI1lkWgWnDk3A7ApgjbW18Ge_7544UXsU9aNCS6k0iq9ThMyeMzQXOSc0fxZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.89M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 19:26:08</div>
<hr>

<div class="tg-post" id="msg-653870">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5722bf4152.mp4?token=RzNRX-NWKJXQdNOZGyoG6ShoAXRtukxnwPp3BLp7drmzFtf2AqJJgwE06PbW8zfHVkuQhg65dyqKjJyx8e9nUrTmB19jQxUWP6J9rLvK2zMd32oKK7zNMLiUs7q2p21gOPpXTmFH4_KMbbNXByUbFuW6QVqSRyJVCJtmoR5qLeLP_htEhtr0NVtw85lI2iqjxfgLxd8Vclb_KUXujva3f4hPmLM2f9pav69TjfQRfVTnj689V1Hj9bzBMpJAsTIMn-XwkQyZ4iKRpk8OPcCF0IWyH3Fwi56DpDWOg5S-spmT6ql3RUpvU-NcmFETRnvzLo46P1zICPSoGY4ADMql4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5722bf4152.mp4?token=RzNRX-NWKJXQdNOZGyoG6ShoAXRtukxnwPp3BLp7drmzFtf2AqJJgwE06PbW8zfHVkuQhg65dyqKjJyx8e9nUrTmB19jQxUWP6J9rLvK2zMd32oKK7zNMLiUs7q2p21gOPpXTmFH4_KMbbNXByUbFuW6QVqSRyJVCJtmoR5qLeLP_htEhtr0NVtw85lI2iqjxfgLxd8Vclb_KUXujva3f4hPmLM2f9pav69TjfQRfVTnj689V1Hj9bzBMpJAsTIMn-XwkQyZ4iKRpk8OPcCF0IWyH3Fwi56DpDWOg5S-spmT6ql3RUpvU-NcmFETRnvzLo46P1zICPSoGY4ADMql4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جواب نظامی به یک سوال دیپلماتیک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/akhbarefori/653870" target="_blank">📅 19:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653869">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/go-gVBVw1WZshos8mry6rdJPj3gBeVZa36uV4ozzT2K99mAyoI--Bu3upVmuW-CMn2xK9kRWHENumQCATi5ET8Onc0JUeCEKhwZKt_Cr71SP5Oj-sqWCFJiU-8quenIkNr83phv3hensy8c6kuGxNWiDqbcGy-uUZaYq7YHLidcD3PoxDjMAHZelxV9FqijNozAm00PKQAyleO3cybcVv1AYESdS3D8wKa1tL8W4kRA-lAGqoQ7O9d_ySWm3LbnlxLSRX42elNjZ9ZmzOenZ-hskAPC5JyKl1WiKUINrQLfUq_AH27yf17-KBPPEVy0mjX9mwoyj1_BxgZ8uEUy07Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ابتکار بزرگ
#بیمه_البرز
برای تحقق شعار سال با بیمه‌های زندگی پروژه‌محور
بیمه البرز در راستای تحقق شعار سال «اقتصاد مقاومتی در سایه وحدت ملی و امنیت ملی» و با هدف ایفای نقش موثر در فرآیند بازسازی و توسعه اقتصاد ملی و تقویت اقتصاد خانواده پس از جنگ تحمیلی ۴۰ روزه، اجرای بیمه‌های زندگی پروژه‌محور را به‌صورت ویژه در دستور کار قرار داد.
مشروح خبر:
https://alborzinsurance.ir/PublicBlogDetail/5035</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/akhbarefori/653869" target="_blank">📅 19:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653867">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
المیادین: بخشی از توافق ایران و آمریکا، بر اساس طرح چین است
🔹
شبکه خبری المیادین جزئیاتی درباره توافق احتمالی ایران و آمریکا منتشر کرد.
🔹
به گفته این منابع، توافق ایران و آمریکا شامل بندهای مورد توافق در طرح ابتکاری چین است.
🔹
طرح چین شامل ۵ بند بود که در ۳۱ مارس پاکستان در جریان آن قرار گرفت تا یک طرح ابتکاری مشترک را تشکیل دهد.
🔹
این منابع با اشاره به اینکه تفاهم‌نامه کنونی در بند چهارم طرح ابتکاری مشترک چین و پاکستان قرار می‌گیرد، تصریح کردند: بند چهارم این طرح، توسعه و امنیت را به هم پیوند می‌دهد و شامل ۵ مورد است:
🔹
اول؛ توقف کامل جنگ و درگیری نظامی و تضمین عدم از سرگیری آن.
🔹
دوم؛ بازگشایی تنگه هرمز از دو طرف و خروج تجهیزات نظامی آمریکا از اقیانوس هند.
🔹
سوم؛ آزاد کردن بخشی از پول‌های مسدود شده ایران.
🔹
چهارم؛ لغو بخشی از تحریم‌های یک‌جانبه اعمال شده بر بخش انرژی ایران.
🔹
پنجم؛ عبور محموله‌های انرژی کشورها از طریق هرمز، از جمله ایران.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/akhbarefori/653867" target="_blank">📅 18:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653866">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivGEwMWLx5pmfmckgL0bvsYxxLZtMJyUNE9fz5Wfh0xHf0Vy-rQbimxidVnpQQC6ZGSwG4EYODQPRHZrnc1K8Etush2LZv-7MLTmGMq8-YYIyIK3_n0xzJF6OlkzP1dPBNwLSHHb3hqoDFlGyiK0dCxKGNmyie_h98NXV1SK4zRpA7Yf-_5bLoPwQryegeiBftQ_re9Sd7mih7pO25jZCV6cO9W4M_cyIy8bo9btu4A4mNQvrTZy1zz2_ECF8Sf3lHa88b79Y02k0dNKEPuC1h-TpVv5Oa8jw3sGjNO_9X5tex86_05sPEd0M5OVV_eMm22YgwCMVFyUvKiwBbLKug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حبابی به نام «توافق ۳۰ روزه»/ به این دلایل توافق ایران و آمریکا سر نمی گیرد
🔹
برخی مفاد مطرح شده در توافق احتمالی دارای ابهام هستند و تضمینی برای اجرای آنها وجود ندارد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3217596</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/akhbarefori/653866" target="_blank">📅 18:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653865">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
پیشنهادات جدید شورایی‌ها برای رایگان شدن مترو و اتوبوس/ بلیت رایگان برای دهک‌های ۱ تا ۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/akhbarefori/653865" target="_blank">📅 18:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653864">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjX2G8tJ6ayGFvNZ_qwHrpz7exLuWD9H1QjOSty4yKlO4nonwJUXifwMa3giafwtgxh9kNf6QeAkbIuFr1MeDrMCMySceXmZdmV30bBDo2FIzPzMGnTQIzVfvKbWASFJSgWzD-1DxEM8kILuoBNqwpiamJQpvy4znTBtqUw7iSegvrHV4H-BSrTB4Gz61tG2QpVPB3NEPCHsUXvaagjId0uJyiTBF0Vd7VZc0sakHSYB_z6pehpySAz0IXxFEMaAbjO3tbHV9YekAK0LxKnXcPpehdLM0C69RrIWXPdFKbuZD-2ZXDmG321UvfvgIYcXkpN0RqBCFbbsBSl_WguySw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: اقدام تروریستی در راه آهن کویته را محکوم می‌کنیم
🔹
سخنگوی وزارت خارجه: این اقدام تروریستی به جان‌باختن و مجروح شدن تعداد زیادی از شهروندان پاکستانی منجر شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/akhbarefori/653864" target="_blank">📅 18:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653863">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YB3tWFnPlHC5XFG3vGvMxPI78E1q3UBMpyE7zFsYvaa3OWATRjEqApgn23QTb4_BtkJt48_wS5uzm_yrNuQHuKaYest1aHgTgtD4QOL2craqzKdQEaqDZ5tzQ3kJpZGdoDWe-q7rbXFbE3KVho0nXC5mz0ny2zFK7-jeWr0lsTxQbXBnJlj5ZcCtsY_tqWzWyql2ayOAOMfDAp5pUHnjczCGQLrDmlxeOdRgntO5jwj3usjOeSjVo2K6OWwRsKlUkm46oW_glQZLNxU63sQWH_X_kYyzTMecypMnQkZDkPKGjU3vV_hQa8H85Q8FRrFoYzKBmpWjKDRLeMXEwxp35g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب آبادی: برخی کشورها بعد از دستور دیوان بین‌المللی دادگستری، کالاهای مرتبط با امور نظامی به رژیم صهیونسیتی داده اند
🔹
معاون وزیر خارجه: تعهد به پیشگیری از نسل کشی در کنوانسیون ۱۹۴۸ تعهد واقعی است؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/akhbarefori/653863" target="_blank">📅 18:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653862">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNwmJMZOZiskmtAH9gOKEaTeL0R5LH7kd3VwE2xclI6nCUMHRsunTDA8RexVOJMWFu8OaD5jtwhFfVA1k8SXNhk9MtjN7RvRcbFXDZgwPwmi1-GfAaF2gnlESdb_DgRM-Ixi3koDbbgAg_SGiIBSH2g1sUeQlCqKXFX3xEpuMJufI8WkTUn0neeUIC49YyCbUV8tu-5saSecc9TxWdjz9KeXCUilkgpUeMaSU1EN-uRUcOa0CvJGSa7vnWyROSLXW8zEWVi0fiwzHly7QiEQ0L8oINVoWetQz3icdlIG59jtFwsiDYCEi56fv7IapOroq8lmoYHwSoxsCMurkCeEvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید نتانیاهو کودک کش با عکس ترامپ: ایران هرگز سلاح هسته‌ای نخواهد داشت
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/akhbarefori/653862" target="_blank">📅 18:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653861">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
حجت‌الاسلام اژه‌ای: وحدت رکن اساسی مقابله با دشمن است
🔹
رئیس قوه قضاییه در حاشیه مراسم بزرگداشت شهدای جنگ تحمیلی سوم:
🔹
در هر سه رکن «خیابان»، «میدان» و «دیپلماسی» باید به مؤلفه و عنصر «وحدت» توجه ویژه کنیم و در هر سه عرصه‌ مذکور، دشمن و حیله‌ها و مکاید او را بشناسیم
🔹
قطعاً ملت متحد و منسجم ما و همه مسئولان و کارگزاران، دست از مبازه با استکبار و ایادی او برنخواهند داشت و ما اعلام می‌داریم که «تا آخر ایستاده‌ایم»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/akhbarefori/653861" target="_blank">📅 18:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653860">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5-RWG7ajSYRgSLVEZv8BGC__YNu2Y5OE_LksONkTQH9rCxqa7R3BzRAvx_wvevYbZ737gMyKn7gEo36pZB1tN8vL2TaQ-S6C_imGuAjSkygNzt4beF55IIfsjdHTzwl1W4I5-b9GIRjHtAIHnqnyzSFP7UnuDqk-eUWVtLI6ukmrpNI68zXv-JfcgtwQxW_yBpk0NYvMgQ5jfnUmHE6h1OVG7l-ZgEWEKBg69T13RldG3s2iRuNqPA2aoEHiVJm7BFc2_Ef-1SpPCW0FJik094uBlnsmSvEtQFEYU2GfpdIbNrnhiH-y2c9YKU6GchUNwqZDaPyE41OO0wT6STknQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتایج مهم جنگ رمضان از نگاه تحلیلگر و استاد دانشگاه تهران
🔹
حسن احمدیان: خروجی‌های راهبردی جنگ علیه ایران:
🔹
کاهش نفوذ اسرائیل و اثرگذاری آن بر واشنگتن و سیاست‌های آمریکا.
🔹
کاهش گرایش به عادی ‌سازی روابط در منطقه و فشار برای انجام آن.
🔹
کاهش انگیزه‌های جنگ علیه ایران در واشنگتن، به دلیل گیر کردن و دشوار شدن اقدام نظامی.
🔹
کاهش ارزش حضور نظامی آمریکا، به‌ویژه پایگاه‌هایش در نزدیکی ایران.
🔹
کاهش نقش امارات در اقتصاد و بخش مالی ایران.
🔹
افزایش انسجام و هماهنگی میان اعضای محور مقاومت.
🔹
افزایش ارزش و اهمیت منطقه‌ای ایران در مقابله با گسترش نفوذ اسرائیل.
🔹
شکل‌گیری نشانه‌هایی از توافق‌های احتمالی درباره امنیت جمعی در منطقه.
🔹
و مهمترین دستاورد همچنان این است: کاهش مداوم وابستگی کشورهای منطقه به آمریکا از نظر امنیتی و راهبردی؛ روندی که از چند سال پیش آغاز شده و جنگ علیه ایران آن را سرعت بخشیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/akhbarefori/653860" target="_blank">📅 17:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653859">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPsgMwd4WZDRXC4bzwB0EOj4UeLVi-5uTPZrGfLVTz1IQ3v3Bq8OzFWB-_NNklcTlHTBFK8QEY3J83wM20SuEi3tXNP5uzHAbqTgKOxogMAxjoJSXOYU5ysiAd2tBN4vOm_36frhzrvE_WMyWSiy6kx3UQIKEAJitBC9e9dUvsk3hmA0QqhzaQ17Ux9Q29OCvz_KA9xAyM9tlErMNTjFJ-UPY6bVj9lGjadxv9XLwlH3x2j8ASoEZVgTEz_5bEBP9j9bCubSufkYiurdwPiv3C4jwQXgs96VXGiemJ0op7Moc7oGw51fXi2ttfOjnS4kx3MjS4FJPE47NN64L6qe8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یوفوها، بشقاب‌پرنده‌ها و پرده‌های دود | چرا واشنگتن شیفته موجودات فضایی است؟
🔹
در سال‌های اخیر، موضوع بشقاب‌پرنده‌ها و موجودات فرازمینی از حاشیه فرهنگ عامه به قلب سیاست آمریکا راه پیدا کرده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3217529</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/akhbarefori/653859" target="_blank">📅 17:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653858">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
دو بند از توافق احتمالی آمریکا و ایران به نقل ار فاکس نیوز:
🔹
نیروهای آمریکایی به مدت ۳۰ روز در مجاورت ایران خواهند ماند.
🔹
به عنوان بخشی از این توافق، ایران معافیت از تحریم‌های نفتی دریافت خواهد کرد. همچنین میلیاردها دلار از دارایی‌ها و پول‌های مسدود شده ایران آزاد خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/akhbarefori/653858" target="_blank">📅 17:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653857">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75595ea0fa.mov?token=mwwQjBjD5kzqmNe30KGygdP1hiYgFMTtL2M_ouyvJb-EkQ-OiNHSEhTdrEgFMFzDDa5ERTpUJ5YJzREyw-Ix9uqXs4MsYLx4iq4umiMNqLZvI6-b65vl6qQxyw7mlMg2osvCRQEGdjb8y2sMdXfqDRvqkxCxYK_2X-T5nafSDtB_d2RyWBEXzWvuQ8eLwfCr4ree_DsrgtIFD4XGgrR9yksbjrvk9RPkEnR4kiyLdgjfsMb2pU3L4eW0ve5yYDnXtDj1c7IR-zg38OjtC8ALC8xtuRZkHTnh91uLXszpZbCaj97wT3_YoAz5BIzszeHhh2V5LXltaF0N7aV6rmTsQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75595ea0fa.mov?token=mwwQjBjD5kzqmNe30KGygdP1hiYgFMTtL2M_ouyvJb-EkQ-OiNHSEhTdrEgFMFzDDa5ERTpUJ5YJzREyw-Ix9uqXs4MsYLx4iq4umiMNqLZvI6-b65vl6qQxyw7mlMg2osvCRQEGdjb8y2sMdXfqDRvqkxCxYK_2X-T5nafSDtB_d2RyWBEXzWvuQ8eLwfCr4ree_DsrgtIFD4XGgrR9yksbjrvk9RPkEnR4kiyLdgjfsMb2pU3L4eW0ve5yYDnXtDj1c7IR-zg38OjtC8ALC8xtuRZkHTnh91uLXszpZbCaj97wT3_YoAz5BIzszeHhh2V5LXltaF0N7aV6rmTsQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر رضایی: فرماندهان آمریکایی فهمیده‌اند که باز کردن تنگه هرمز دالان سیاه و تاریکی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/akhbarefori/653857" target="_blank">📅 17:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653856">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
آماده‌سازی‌ ناوگان‌ جدید به‌منظور شکستن محاصره نوار غزه
🔹
رئیس کمیته بین‌المللی شکستن محاصره غزه: آماده‌سازی‌ها برای راه‌اندازی ناوگان‌ جدید به‌منظور شکستن محاصره نوار غزه آغاز شد. متوقف‌کردن یا رهگیری ناوگان‌ها از سوی رژیم صهیونیستی نمی‌تواند به موج همبستگی با نوار غزه را پایان دهند و تا زمانی که محاصره این منطقه ادامه داشته باشد، این تلاش‌ها متوقف نخواهد شد.
🔹
رژیم صهیونیستی هفته گذشته موجی دیگر از کشتی های ناوگان صمود را توقیف و فعالان سرنشین این کشتی ها از ۴۰ کشور را بازداشت کرد.
🔹
این فعالان پس از آزادی از آزار و شکنجه خود توسط صهیونیست‌ها خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/akhbarefori/653856" target="_blank">📅 17:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653855">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ترامپ از کدام خبر خوب صحبت می‌کند؟
🔹
ترامپ بعد از آنکه تمام اهداف اولیه‌اش از جنگ شکست خورده به ای‌بی‌سی نیوز گفته است:«من نمی‌توانم در مورد این توافق صحبت کنم؛ کاملاً به من بستگی دارد و اگر خبری باشد، فقط خبر خوب خواهد بود. من توافق بد نمی‌کنم.»
🔹
قرار بود حاکمیت ایران نابود شود حالا ناچار شده در مورد حاکمیت ایران بر هرمز پای میز مذاکره بنشیند.
🔹
همچنین قرار بود نفت ایران را غارت کند حالا باید در مورد پس دادن دارایی‌های بلوکه شده صحبت کند.
🔹
قرار بود تمدن ایران را نابود کند ناچار شده است به مذاکره با همین مهد تمدن تن بدهد.
🔹
اخبار خوب مورد ادعای ترامپ در گفت‌وگو با NBC را بیشتر لیست کنیم یا بس است؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/akhbarefori/653855" target="_blank">📅 17:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653854">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
‌ سرلشکر رضایی: اگر دشمن به تنگۀ هرمز حمله کند، ما محاصرۀ دریایی را می‌شکنیم و ممکن است از NPT خارج شویم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/akhbarefori/653854" target="_blank">📅 17:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653853">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0088317db7.mp4?token=P-MwBr_36ayH-nUKBvQF863DrI26S5rpnl54sS_7-wru_A8BeqyuHnjX7OqpcU2hzwca8byj5Fq67wffl25HP_Ov6PMGx9S3xtBbTKl-e37entPsCsy1Y0QAaV0ASRqeIbQjqTVV84sxjmAVzeplJIdaMQaoOL2xsLVh4L9kRaqDvLAB0DVuCU_71HCoJwUj8UtQypx26eY6DJPkL9W6uNmN6Ahe1RujPOKvjmx8rSrNzcbvO8Vn3Q4IkrjSm5zCeenlS0Mxlt7V2DC5HQcq8Oha6ea2Zo2PsiTC6YcLJyqYXR3LilkHUiIZgu6kw10qlbds3YgJGcTP6oktQFabxIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0088317db7.mp4?token=P-MwBr_36ayH-nUKBvQF863DrI26S5rpnl54sS_7-wru_A8BeqyuHnjX7OqpcU2hzwca8byj5Fq67wffl25HP_Ov6PMGx9S3xtBbTKl-e37entPsCsy1Y0QAaV0ASRqeIbQjqTVV84sxjmAVzeplJIdaMQaoOL2xsLVh4L9kRaqDvLAB0DVuCU_71HCoJwUj8UtQypx26eY6DJPkL9W6uNmN6Ahe1RujPOKvjmx8rSrNzcbvO8Vn3Q4IkrjSm5zCeenlS0Mxlt7V2DC5HQcq8Oha6ea2Zo2PsiTC6YcLJyqYXR3LilkHUiIZgu6kw10qlbds3YgJGcTP6oktQFabxIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: خروج از ان‌پی‌تی؛ می‌تواند تهدید راهبردی در دست ایران باشد
🔹
رضایی در گرامیداشت شهدای جنگ تحمیلی سوم: یکی از گزینه‌های راهبردی و هشدارآمیز ایران در صورت تداوم این روند، احتمال خروج از معاهده «ان‌پی‌تی» (NPT) است که پیامدهای سهمگینی برای طرف مقابل خواهد داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/akhbarefori/653853" target="_blank">📅 17:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653852">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ایران بساط سواستفاده دشمن را از تنگه هرمز برخواهد چید
🔹
پیام فرمانده قرارگاه مرکزی خاتم الانبیا(ص) بمناسبت آیین گرامیداشت شهدای جنگ رمضان: در این مراسم شکوهمند که بر تداوم مقاومت و پایداری و هوشیاری و هوشمندی برابر دشمن امریکایی صهیونی تأکید دارد، با تأسی از رهبر عزیزمان، ایران اسلامی با شکر عملی نعمت، منطقه خلیج فارس را ایمن خواهد کرد و بساط سوءاستفاده‌های دشمن را از این آبراه برخواهد چید و آسایش و پیشرفت را به نفع همه ملت‌های منطقه رقم خواهد زد.
🔹
به دشمنان هشدار می‌دهیم که برنامه‌ها و راهبردهای رهبر انقلاب برای مدیریت خلیج فارس و تنگه هرمز، آینده منطقه و نظم جدید منطقه‌ای و جهانی را در سایه راهبرد «ایران قوی» تضمین می‌کند، که بیگانگان هیچ جایگاهی در آن ندارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/akhbarefori/653852" target="_blank">📅 17:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653851">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c518857418.mp4?token=ol0Pywhf8UMGj-XkF4-FnoqDuQr3S0slbAJW4n2WPCXVTd4x0HmAf_oBw8hbqn9mQcORbvtB7o_OW_naEcVviuTqTHPIilPWrmE-jzDO-REvI5NT-_85zp2oYjBjWfrvQHvKZLRmjqi3qqc12w-G57cJoMcsS-lAMeFwg88Onywz42E3G557vIuRUGQu5Wv6jO-mUeEy00byMv1cr1AaPXZwxOXER656FfNi2MoBrpItbtLAMDzi8frOSAIB039YvJOy3WhQvGgAlzyldw5zFebdHFhwuq7BmtlJP5hOFyFsHcqYirJMXOeB4PvudicqVFgrxKJ_szz7lstozMLmDijz6TFLHE4x0rOyIh3NgFsTZIMKp-jLCOD10xmTqBOX2T6Tb75q-v59oK5bKEjRAirqKuwA-1mweldy7aD0i8Np6fOG5tWy9SzN0fiXRjAexEv9BdoiCFDvITdQHJRCZyR3z9K9YwOOGz4t3s19hUEYj5GGlmk408lOVHX4KICzg62VQsOzo5msjf9LwC9R62GTdczATMYRbATIw-I5tMx0KeRZf_OPTWlWYxj5nS5lVOC4zghj-2kBTjXXHEn3pYmFnRQXQ-nNv9D6CCHXfmEjRCJKeaN2WwIBs2MQoc-ZeAM2h3GCSf9_d0xxJbY3fSCsKL9HT6gI18awyaa3udg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c518857418.mp4?token=ol0Pywhf8UMGj-XkF4-FnoqDuQr3S0slbAJW4n2WPCXVTd4x0HmAf_oBw8hbqn9mQcORbvtB7o_OW_naEcVviuTqTHPIilPWrmE-jzDO-REvI5NT-_85zp2oYjBjWfrvQHvKZLRmjqi3qqc12w-G57cJoMcsS-lAMeFwg88Onywz42E3G557vIuRUGQu5Wv6jO-mUeEy00byMv1cr1AaPXZwxOXER656FfNi2MoBrpItbtLAMDzi8frOSAIB039YvJOy3WhQvGgAlzyldw5zFebdHFhwuq7BmtlJP5hOFyFsHcqYirJMXOeB4PvudicqVFgrxKJ_szz7lstozMLmDijz6TFLHE4x0rOyIh3NgFsTZIMKp-jLCOD10xmTqBOX2T6Tb75q-v59oK5bKEjRAirqKuwA-1mweldy7aD0i8Np6fOG5tWy9SzN0fiXRjAexEv9BdoiCFDvITdQHJRCZyR3z9K9YwOOGz4t3s19hUEYj5GGlmk408lOVHX4KICzg62VQsOzo5msjf9LwC9R62GTdczATMYRbATIw-I5tMx0KeRZf_OPTWlWYxj5nS5lVOC4zghj-2kBTjXXHEn3pYmFnRQXQ-nNv9D6CCHXfmEjRCJKeaN2WwIBs2MQoc-ZeAM2h3GCSf9_d0xxJbY3fSCsKL9HT6gI18awyaa3udg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: متجاوزان در دام راهبردی تنگه هرمز گرفتار شدند
🔹
بررسی تصمیم‌گیری‌های ارتش آمریکا نشان می‌دهد که آن‌ها نبرد ۴۰ روزه اخیر را تنها برای چهار تا پنج روز و در بدبینانه‌ترین حالت برای ۱۵ روز طراحی کرده و متناسب با همین بازه زمانی نیرو گسیل داشته بودند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/akhbarefori/653851" target="_blank">📅 17:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653850">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee39774246.mp4?token=SMVKNKaUEQSOgQfzctWtB-e9MB7c5fYB_NULGDHnRMI15O-JIWcHLJTUWPj_NPqPS2K4H8xNAHjgruq1_htc1UbFb8VzXxG640JNgy7fma-2cM5fSPeoa_c6q6DsPf6Zr71uJGGa-FhfYhaPHCPco2Zi4I83pif676MM9h8sXB5je0qh7drPZIX7z_XiWDpVpVqzT-h65oMexV5TAYG77UnXU9cYz5GnhA5OhwzhB1w6wRwRe891w6EyWC66JqcsqsZvllfEjnUevoZJ9Ae7VGGiT3i7T1A9xQ45tI22UMaxKQNMlvi9rJO4oTQbZvZ1jlV7aJwqfq0CNXS50Fvajg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee39774246.mp4?token=SMVKNKaUEQSOgQfzctWtB-e9MB7c5fYB_NULGDHnRMI15O-JIWcHLJTUWPj_NPqPS2K4H8xNAHjgruq1_htc1UbFb8VzXxG640JNgy7fma-2cM5fSPeoa_c6q6DsPf6Zr71uJGGa-FhfYhaPHCPco2Zi4I83pif676MM9h8sXB5je0qh7drPZIX7z_XiWDpVpVqzT-h65oMexV5TAYG77UnXU9cYz5GnhA5OhwzhB1w6wRwRe891w6EyWC66JqcsqsZvllfEjnUevoZJ9Ae7VGGiT3i7T1A9xQ45tI22UMaxKQNMlvi9rJO4oTQbZvZ1jlV7aJwqfq0CNXS50Fvajg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: ممکن است از ان پی تی خارج شویم، راهی را که آمدید برگردید
🔹
اگر محاصره ادامه داشته باشد آن را می‌شکنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/akhbarefori/653850" target="_blank">📅 17:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653849">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed16233809.mp4?token=cZh3UXIQct4vWqJbr0yyg7_vkRVZtujUp251j_gjl2F_4LPzkezmiLew_kGWkzQQ4PvJk3dlrNzKWZqj2jHcc2z0AcVmwGFAMXqO2zDRsjT93AvM8TK_FA2e8G0c6DqCIBDiNo5iJw3kz1meJ52SDEUEMvRE9qiFvBlsZRHsFf8EwWt5arhqsvUi3WZXp4Das_e92RFGQK7YW5e9ANPfXrcGL27G5uBRbLNL_VAffvDec0aYcAotWTJd7yTQXbpWrnYT-LD8UYV91pXK0MUslzCzRfRCMVjdpLIvjWGFi60VpCZ-9UBveZRgVTmx88aytiJPASva5dQBbU2jmiXgcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed16233809.mp4?token=cZh3UXIQct4vWqJbr0yyg7_vkRVZtujUp251j_gjl2F_4LPzkezmiLew_kGWkzQQ4PvJk3dlrNzKWZqj2jHcc2z0AcVmwGFAMXqO2zDRsjT93AvM8TK_FA2e8G0c6DqCIBDiNo5iJw3kz1meJ52SDEUEMvRE9qiFvBlsZRHsFf8EwWt5arhqsvUi3WZXp4Das_e92RFGQK7YW5e9ANPfXrcGL27G5uBRbLNL_VAffvDec0aYcAotWTJd7yTQXbpWrnYT-LD8UYV91pXK0MUslzCzRfRCMVjdpLIvjWGFi60VpCZ-9UBveZRgVTmx88aytiJPASva5dQBbU2jmiXgcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش امیر سیاری معاون هماهنگ‌کننده ارتش به اجرایی شدن توافق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/akhbarefori/653849" target="_blank">📅 17:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653848">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d37bf7f5f0.mp4?token=vWpA118a3c7Y7PifKjH8-n9FGXyivvbi56M6J3UUDJRxyJsjY9GouNCyjK2AFjvPB9Isvtg06jpT0RSuvo4caz2zGNusg-hWkqMGTd2iOFGoSDUgdNwHxp-bnv-VhbyGhiF1dOLTeodO60CwkS2q-GH-jGSMRJvjyjHJ1hi3NZyRT-aIgPn5nuXxR6WDRxLeu7BYCfhsXK-uGNIP2YowkkmFWMWqeM7Wz_OHubxurmPIQMFgZdYjA5iLV3orxQrfcbdUtAavNiuUi7yfTX72Yl_r2YGyUFiAVvCeshE9BUAJO-APB2E9W3epiDblDnPVbUSTV4sihNz3OQKdm02Wpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d37bf7f5f0.mp4?token=vWpA118a3c7Y7PifKjH8-n9FGXyivvbi56M6J3UUDJRxyJsjY9GouNCyjK2AFjvPB9Isvtg06jpT0RSuvo4caz2zGNusg-hWkqMGTd2iOFGoSDUgdNwHxp-bnv-VhbyGhiF1dOLTeodO60CwkS2q-GH-jGSMRJvjyjHJ1hi3NZyRT-aIgPn5nuXxR6WDRxLeu7BYCfhsXK-uGNIP2YowkkmFWMWqeM7Wz_OHubxurmPIQMFgZdYjA5iLV3orxQrfcbdUtAavNiuUi7yfTX72Yl_r2YGyUFiAVvCeshE9BUAJO-APB2E9W3epiDblDnPVbUSTV4sihNz3OQKdm02Wpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتی از کشف لاشه پهپاد متلاشی شده اربیتر که در آسمان هرمزگان درحال جاسوسی بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/akhbarefori/653848" target="_blank">📅 17:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653847">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
محسن رضایی: برای اولین بار بعد از جنگ جهانی دوم ابرقدرتی آمریکا دوباره فرو ریخت
🔹
آمریکا بعد از جنگ رمضان دیگر به آن آمریکای سابق برنخواهد گشت و ما افول آمریکا در خاورمیانه رقم زدیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/akhbarefori/653847" target="_blank">📅 16:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653846">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1242bf8da9.mp4?token=bJUSj60D_NOvcZdtMHU8cQR3luVJYvJXZJNDMF9tHAw6pviI0ypHEkdMCoM5KExrDJoqBHmj3g5ochLtczRTjEAeTM0NJwxm9pL5eBCiLVCgPw0dMVYFkRHM2QKeFOLZ3Kb7Awxk_C-lMUyLrKfqcaIgPuh601VOauRe4DBuEv9h7COeWc4O5DpJ2xi2oIhkIXFbsoILwPGTaREGNZ3B_VRSGFFfcfQAK3rRz1ZwYbzpiZUhU55YdsljGpoKKGtb_0yQYiGULdAnxeS7hIWZQtHj98Xp7L_vyjr6qfdgrB5VbTs2mkA3OMXof-jwkV2rLT76-M4V2KwdwW-luXzhFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1242bf8da9.mp4?token=bJUSj60D_NOvcZdtMHU8cQR3luVJYvJXZJNDMF9tHAw6pviI0ypHEkdMCoM5KExrDJoqBHmj3g5ochLtczRTjEAeTM0NJwxm9pL5eBCiLVCgPw0dMVYFkRHM2QKeFOLZ3Kb7Awxk_C-lMUyLrKfqcaIgPuh601VOauRe4DBuEv9h7COeWc4O5DpJ2xi2oIhkIXFbsoILwPGTaREGNZ3B_VRSGFFfcfQAK3rRz1ZwYbzpiZUhU55YdsljGpoKKGtb_0yQYiGULdAnxeS7hIWZQtHj98Xp7L_vyjr6qfdgrB5VbTs2mkA3OMXof-jwkV2rLT76-M4V2KwdwW-luXzhFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار محسن رضایی: دست ما روی ماشه است
🔹
کاری می‌کنیم که امنیت کشور در ۵۰ سال آینده تامین شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/akhbarefori/653846" target="_blank">📅 16:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653845">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
امیر سیاری: در صورت تجاوز مجدد قطعا آمادگی وجود دارد
🔹
رئیس ستاد و معاون هماهنگ‌کننده ارتش: روش ما این است که راه شهدا را ادامه می‌دهیم. اگر فرمانده‌ای شهید شود فرمانده بعدی جای او را پر می‌کند؛ ما الحمدالله فرمانده لایقی که بتواند صحنه ها را کنترل کند زیاد داریم.
🔹
توان نظامی ایران بستگی به اراده مردم دارد، وقتی مردم در صحنه هستند همه توان‌ها وجود دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/akhbarefori/653845" target="_blank">📅 16:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653844">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
گرانی قیمت دارو به تغییرات نرخ ارز و تورم عمومی کشور باز می‌گردد
🔹
وزیر بهداشت و درمان در جلسه نظارتی مجلس: گرانی قیمت دارو به تغییرات نرخ ارز و تورم عمومی کشور باز می‌گردد و تلاش داریم این گرانی‌ها را از طریق بیمه‌ها پوشش دهیم.
🔹
راهکار اصلی این است که بتوانیم تمامی افزایش قیمت‌های دارویی را در قالب بیمه، پوشش بدهیم تا فشار مضاعفی بر مردم وارد نشود.
🔹
علی نیکزاد نایب رئیس مجلس: سازمان برنامه و بودجه اعلام می‌کند ارز ۲۸ هزار و ۵۰۰ تومانی حذف نشده، بنابراین دارویی که با این نرخ ارز وارد می‌شود نباید سه تا پنج برابر افزایش قیمت داشته باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/653844" target="_blank">📅 16:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653843">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79a4d45548.mp4?token=kaL004qMcGdOVr-LHahqAzev06PolDLi47hzG2hIFygyCgn6cmvycrd48mRhaDqE6kkVQj0MSkjtIh9vNrEoDtzuMHcqR_GYkjDKMWzp6JQtqHKY_TSUkEGjp2XWrwPldK7zLtIoPdeZgO5Cf5EFERGjB8hT4mmTOZf8iosx1QA0yWohovBZYkg57RwaEVm-4B7O6e20gCWKHp_grHBi0CKWvblEHFH20-i6fJJEdMvlLLCC4g8GLKxSzXAfMvxkRMZCs9hj-MtWx_LY7u09eSoexHju88t-UzB6kgUZzzMNMJSpqHkBvK_3rsAyiSE8KM_e-bSzv2hvT0jNVC2CEjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79a4d45548.mp4?token=kaL004qMcGdOVr-LHahqAzev06PolDLi47hzG2hIFygyCgn6cmvycrd48mRhaDqE6kkVQj0MSkjtIh9vNrEoDtzuMHcqR_GYkjDKMWzp6JQtqHKY_TSUkEGjp2XWrwPldK7zLtIoPdeZgO5Cf5EFERGjB8hT4mmTOZf8iosx1QA0yWohovBZYkg57RwaEVm-4B7O6e20gCWKHp_grHBi0CKWvblEHFH20-i6fJJEdMvlLLCC4g8GLKxSzXAfMvxkRMZCs9hj-MtWx_LY7u09eSoexHju88t-UzB6kgUZzzMNMJSpqHkBvK_3rsAyiSE8KM_e-bSzv2hvT0jNVC2CEjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتی عکس محور از زندگی رهبر شهید
🔹
حضور فرزندان رهبر شهید در جبهه های جنگ
🔹
آقا گفت فرزندانم شهید یا جانباز بشوند عیبی ندارد، مراقب باشید اسیر نشوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/akhbarefori/653843" target="_blank">📅 16:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653842">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895f9c57c4.mp4?token=Ts3Gihl0GsdPvnZLVKhMBRVu1qXF4V9dVOCPhrK81yW9pz_HSiswwSGbYaOsNB-hW9JxxbRAKW5uHCZ9pe1SZxTqylhzSebuSC78x6ae3mLoTF8_HV8bbzLoti3a5W2kvKcN_CjxJ-jMo95QBTToKJIVXfE9tsS1BjB7z-1Zg83T6sU0MYsp9nh3hKjOJk9Qe3TBuNdHBHanUJFid4jupUgqMFAGn5Lt1mlTxj8TLWuJuJO4h72jKgEqC5x1miQi6wwLqT-BVLdsEuYTOlp-y2LLM7Nzm8K8t5tQOsyOi3TPcxAB_eLi8pxdfsH5KYgT_ZsKV56hBJnC7o2zHddVaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895f9c57c4.mp4?token=Ts3Gihl0GsdPvnZLVKhMBRVu1qXF4V9dVOCPhrK81yW9pz_HSiswwSGbYaOsNB-hW9JxxbRAKW5uHCZ9pe1SZxTqylhzSebuSC78x6ae3mLoTF8_HV8bbzLoti3a5W2kvKcN_CjxJ-jMo95QBTToKJIVXfE9tsS1BjB7z-1Zg83T6sU0MYsp9nh3hKjOJk9Qe3TBuNdHBHanUJFid4jupUgqMFAGn5Lt1mlTxj8TLWuJuJO4h72jKgEqC5x1miQi6wwLqT-BVLdsEuYTOlp-y2LLM7Nzm8K8t5tQOsyOi3TPcxAB_eLi8pxdfsH5KYgT_ZsKV56hBJnC7o2zHddVaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور فرمانده قرارگاه خاتم الانبیا در مراسم بزرگداشت شهدای جنگ تحمیلی/ سرلشکر عبداللهی: با سلاح‌های بومی، دشمن را شکست دادیم
🔹
در شرایط جنگی هستیم و تمامی نیروهای مسلح در آمادگی کامل به سر می‌برند که با هر دشمنی و در هر سطحی مقابله کنند. نیروهای مسلح ما به پشتوانه مردم قابلیت رزم در هر جنگی با دشمنان را دارند. امروز ما باید در عرصه‌های اقتصادی، اجتماعی و ... آمادگی داشته باشیم و نیاز به ابتکار و نوآوری و خلاقیت داریم.
🔹
همانطور که در چند جنگ اخیر متکی به ابزار خودمان بودیم و با ساخته‌های بومی خودمان با دشمنان جنگیدیم. اکنون نیز باید در تمام عرصه‌ها آماده باشیم و به موفقیت برسیم.
🔹
ملت ما ملتی پرتوان، پراراده و هوشمند است و این حضور را در میدان نشان دادن است.
🔹
پیروزی ملت ایران بر دشمنان، معجزه الهی بود و هر آن چیزی که ملت ایران گرفت به واسطه اراده ملت بود. آن چیزی که قبل از این جنگ بود و آن چیزی که بعد از این جنگ است، حتما دنیای متفاوتی است و حتما عزت و افتخار ملت ایران زبانزد همه دنیا هست و بیشتر هم خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/akhbarefori/653842" target="_blank">📅 16:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653837">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TLg2MzVicFYxtcOctXBkpToNmQdtbJRAdH5rBRuxd7z8YB3y2fQLBE7gRwN2y9QnkIxM_4QguH3bLWVfJux3VqXkkMmN5D2IAVX6y1bIqi1XPrSI6vEglNJH4oNT73fsLRKdcQWevfQhu427gi8nKNZcd1bM1pC6uF-OoyYLQiMb2tbwKUIdci8LI5SG3RRb2w9pxCNCbW-OtblS8_XMCmzY2ZPzUEQko2rY_hNf1S1kLrl2b4MR-xMu_MCcWkGbZUGnlUy-l0BshPJyke3bfK1eIW9OEDPyZYwz26gHjjM0k1eNULtgnkXqlelkzQnTablICTvyjekzfFLabJfdxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tEY-QzDnyEYROuyMDd4pfe_j1m4x-OSMOtNxdcbhAvGo8X6jRni3_u5-ZFfhewYzODxdcRN9o17mMxIZMc81BMZUO0ovQOIPdf1FsqTFWmtaELTVU4etCf2R-82Gr8NklOLJPPNKNq4_teS6AvaxoVwmWQBk0QLE8vWBCLEii4_9hFZBUMl1mUNoGH64XDc5al8kxX7_G_iYhao9XfGrP7C0jX6WpBlcwrAK6IUIA2voG5NUH7O-MJ_Yw8eWh31GMRy6DcGi31io3db00If5Fgm7ZjRxrEH5H3z_7wmLLSzVFrGab6cN2kTOpVFT55huW6BQTR7BL7G1Ae_ihWt5fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TnlqG_ImDOv5-8qtaRupCawCXEEHTpYiYqk1DeCSUst1Q5PomGW6h2nWu9HUysr7EtvFEE560RNbg3cCgmp2ws3oW_e4DMIR4YBSimBLqTuXV2T3x9FXnDG8eB2J5L1uVshlX4lKTJF-2IkwsYD-1LfqonpoA8S_7tQb3pSokseRGPIJBluAHbBF5FNrdhy4XpwEex24UH1B6eyEPYJ8dtlMdqxDA-ic1TNPgzWjs0j0mOFiibV1MsUNUBzbuUQo0bHEbehdcwLUza5RKs16oreRbV8ob936xD4sgzJnHnQazKAtz9TMk8hZ41eoNQLFC7eSkjMkaetDQHgFUbVA6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DrKdV3KWP1busc8Irq6sTfCx18vgJ7wnb5rcPoyWGGPWKBS_d9M5hOl8yjGJYfPefkwBzsqrLU1qkgLKjn2mWmrlapU879Muc5k6LP-gZhY3ZA-lqB-t4XsabLDKq1LSBp02cHywrZ2xah3rmwFiWkLH_xRl_ZRMdxW5JiqyBy8SrQ8pKkMBkZwqdHkC6UDyWF9Rz_1cr3yHhnTSVNRdLykwV_p-oHWFoW8pF9DIe0oIe3mopCR-ou5tTeqfgOcXy7EdqPY2l37aaZYTO1SFyqO6O1AtuK-HXhBp7oOs5Avt6KaLSfnBjJnwNmJW19tZVB1GdPXzRjMfyL40jDdK2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GVL9_0M7ph8UrHI0bWzKw1TBgwg52sKdUKnMW8XS6OhiOftNZ47Hx74HvG2LJBBoIMdss8z17wFdXS2JlqF4dz72FHJ3Z4lJaeD5f1fv2ILoyKrILWdgpCrBb354K-VPpb739ijmd1ibrM3u85JPxLbb16DRsO4hs7DxEz1ibmYm_QVHUrW8OKMIoL-MYcCvUoSIzz0SjaiHW1jGe0KVHUjGKGB4RkTvgl6AQcA_ZPc3095kQixZotwRGlGikaVfjoq1OcXFeYfBj6xOQ1G2vcHFhzxsDlz0JGWITY6VMbOyFEU64ZxuCyVyuNsUAJh6BjNTB1SbFUQGS2zMqEUJRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۴ انیمیشن جدید برای دو زبانه شدن بچه‌ها
🔹
۴ انیمیشن جدید که بدون کلاس و معلم، کودکان ۳ تا ۸ ساله را دو زبانه می‌کنند.
🔹
لهجه اصیل، جملات شمرده و واژگان کاربردی در انتظار شماست. در این اسلایدها ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/akhbarefori/653837" target="_blank">📅 16:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653836">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j49D7kHoOCw-WyK8RE9Sp2nrq6aqQ9ovZTUQjfDXBCHxDHjXRR_AhDcIM2WXj90hRABQspartkCnyn29r9Oj9J0kTz6tA5FOj8KDiKvYVx_IkFBoqYx3OryJBhEX3TbZZ5JyjhfogVPUS98lJtus1iieN-TI6_9qD-E8EmeIHQeCZVuxH2BrngtHr3a0hHx-VTYZvZd9dc8NT90vdYVo59JxlbfvypcbmTBGQKBLfwUBjTmSgj2uStDKENncuhH62FS5v5uVGv_-3_mexlxd00kAht6FR_V4XYxrLikwccE6ttAAw1IRKd96SWTZwdvqNgiwk9A5O9YSQm4ma7kqXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ناترازی مالی در صنعت برق ایران به نقطۀ بحرانی رسید
🔹
بر اساس گزارش حسابرسی صورت‌های مالی شرکت توانیر، متوسط قیمت فروش برق در سال ۱۴۰۳ برابر با ۵۳۵۸ ریال به ازای هر کیلووات‌ ساعت بوده، در حالی که قیمت تمام‌ شده واقعی ۷۸۲۴ ریال است.
🔹
این شکاف ۲۴۶۶ ریالی، یعنی دولت برق را نزدیک به نصف هزینه واقعی به مصرف‌کنندگان می‌فروشد. این اختلاف قیمت، انباشت بدهی دولت به صنعت برق را به همراه داشته است.
🔹
برآوردها حاکی از بدهی بالغ بر ۲۰۰ هزار میلیارد تومانی دولت به زنجیرۀ صنعت برق است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/akhbarefori/653836" target="_blank">📅 16:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653834">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0YzoRR4I1fKQMNXSk3c9b4Z7NKcHpu52DlxwT9gt0FEDw9Nm0xaKTzd1EtLhaaWlGCXGU810AAgiVcK4PUDFVYmlkiy0W2Hqtlnb8lo5lCo_Z6PS9VhjipGHnaolto8aJx9eUqorPhawgjrmuw8Yla4EObwPxXx6jJCNHb0rW98qgLVt5CvepMwljEiTra5ZyJfqayHQWkqd3xLrane8PZ1ZS9ILDpJBBwVzrJ972lhN8nzddndzy6gsbdDCRda9G9_yxBHSjmG2LUTLjws_ZulKVMc-5sA9fCct4B_wMov1gVrIg5DEADWEGGCOQAji6GWF3znKVGU0skKA5ekmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7386a3c1.mp4?token=JCYfuBy9hVHY9ieyoqrMwvAYHwQBsdnzqW4kbMBa8OwsFi44HjHJA3y7_Zx1KmaKy7n-g8vomrDBWbJ2d0keP1GUoJIXCJnTjnQOupppwussgbW3QJ4XJXfqh9KaZuW1L_yPJ6SnSPGWjuZtE9W9LIc1MgQj_dzJ5aN7A1XAXXQ_NwMz2DSTHA8GyyhmJ-L5QrtId4EkJzXVpAFyPzuUyaKy1kX31IhcI-KC7pL2CknJ7OcO_86zSLnvRoNxmj1lj9QXFWHP0CXlOKwPwD7fch9lZmYEjEsYMEShwqk1mtwI5WecOo2fQkkR_gRwC5lMKZ0YXnukIfSfPNeR00hojw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7386a3c1.mp4?token=JCYfuBy9hVHY9ieyoqrMwvAYHwQBsdnzqW4kbMBa8OwsFi44HjHJA3y7_Zx1KmaKy7n-g8vomrDBWbJ2d0keP1GUoJIXCJnTjnQOupppwussgbW3QJ4XJXfqh9KaZuW1L_yPJ6SnSPGWjuZtE9W9LIc1MgQj_dzJ5aN7A1XAXXQ_NwMz2DSTHA8GyyhmJ-L5QrtId4EkJzXVpAFyPzuUyaKy1kX31IhcI-KC7pL2CknJ7OcO_86zSLnvRoNxmj1lj9QXFWHP0CXlOKwPwD7fch9lZmYEjEsYMEShwqk1mtwI5WecOo2fQkkR_gRwC5lMKZ0YXnukIfSfPNeR00hojw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات هوایی رژیم صهیونیستی به محله «المسلخ» در شهرک «النبطیه» در جنوب لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/akhbarefori/653834" target="_blank">📅 16:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653833">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31ad66245e.mp4?token=oZYdSsnS0saQ5cL6gukL_PbBVMOFbZvNNfsH2rjf9deMSeYelPmRYkLTP6CPH-jJnwbWk76KV7ehpHilaxvPmZJQLctKcaFd-TGnZ-iYRrzKthRj5CoWhGU8Eo6bSDCBd632JZkqRlgl7zj-48ANVU5xNoBwRFY7q9yhUxXe35nDKyWbmbEXosec2ruc3JMZMCaXExf3BxC5RwViSl1n-BrFAMGWaiO7jL4FKIlTsVdjnIOPO0TJ2aAVp3Dt-K5oP2FcP_JVU2U-X99F9oBwTpXxiIT_Slwq_sTNQ408yfEfoAFr4uIyiN-eaLTbHdU6u2zKkCHPr-0-2z1Q4rqdC0E0oTV1986c-2nPK9UysbWZybNDGFX7VVftRQ-St6Ad1v3JTTEpzATfKvv7rZ3Tt5NHs-MNGAmiKt0oHZ4RN26cKf4WYWigl52ao-cphwj7owZz2MAxukir9N5nqQT2-jFduqv56PsZPlGfIBunvMCUEODX3yxZF7OHHJTaqmJ1gVw5EAVVV4Hx5jpXaJNjV9dSZn0vVcRem2Lmkq2--1mCZxG3RaEZ25GRmVXWppjIuXU5aVxc76eKVKwAPyYwg0fLL7yyIfU2H2SBryZXXdQ46fjVKqZL9YurxHTNg0RdZPaXMqdgZ4zcApEQxA6jfXahiNQxqbCrBac2_wZE4mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31ad66245e.mp4?token=oZYdSsnS0saQ5cL6gukL_PbBVMOFbZvNNfsH2rjf9deMSeYelPmRYkLTP6CPH-jJnwbWk76KV7ehpHilaxvPmZJQLctKcaFd-TGnZ-iYRrzKthRj5CoWhGU8Eo6bSDCBd632JZkqRlgl7zj-48ANVU5xNoBwRFY7q9yhUxXe35nDKyWbmbEXosec2ruc3JMZMCaXExf3BxC5RwViSl1n-BrFAMGWaiO7jL4FKIlTsVdjnIOPO0TJ2aAVp3Dt-K5oP2FcP_JVU2U-X99F9oBwTpXxiIT_Slwq_sTNQ408yfEfoAFr4uIyiN-eaLTbHdU6u2zKkCHPr-0-2z1Q4rqdC0E0oTV1986c-2nPK9UysbWZybNDGFX7VVftRQ-St6Ad1v3JTTEpzATfKvv7rZ3Tt5NHs-MNGAmiKt0oHZ4RN26cKf4WYWigl52ao-cphwj7owZz2MAxukir9N5nqQT2-jFduqv56PsZPlGfIBunvMCUEODX3yxZF7OHHJTaqmJ1gVw5EAVVV4Hx5jpXaJNjV9dSZn0vVcRem2Lmkq2--1mCZxG3RaEZ25GRmVXWppjIuXU5aVxc76eKVKwAPyYwg0fLL7yyIfU2H2SBryZXXdQ46fjVKqZL9YurxHTNg0RdZPaXMqdgZ4zcApEQxA6jfXahiNQxqbCrBac2_wZE4mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر شهید «زید ماهیگیر لارکی» صیادی که طی حملات تروریست‌های آمریکایی به قایق‌های صیادی در تنگه هرمز به فیض شهادت نائل آمده بود، در جزیره لارک تشییع و به خاک سپرده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/akhbarefori/653833" target="_blank">📅 16:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653832">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YScYIy9EDBhHHagSFwVcpT8Xt5O377zgTMb4rvhfD6Tcf_JRPagjUPtWYt_jqdlhx-2dotImhqWSPp0qsWWxVHT8lGvX7zOLdSABlMvyuc2-Hui5IncBsqJlJDJgtJjUfdbz4amacjelKjIZTFDJvEdncJwTrTWFLiuDXUuBdJb5MYsalyGc14yAwEjEg9USNY65elEpWssBv7dr27DO6QqVRApZpfSIBKv9b5BBw0xbYcBmE6172d38gXyL1pksDxvcwMSOqhswJempkUWHn5O3XY2wyTcRMXQR--8t3jkefEDGBS-ZOIDUicBHX19CdT512vpQpisxCCQyX07vVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تلگراف: آمریکا نیمی از موشک‌های پدافندی خود را برای دفاع از اسرائیل در برابر ایران از دست داده است
🔹
بر اساس ارزیابی‌های پنتاگون، آمریکا در جریان جنگ ایران، تقریباً نیمی از موجودی موشک‌های رهگیر سامانه پدافندی تاد را شلیک کرده است.
🔹
آمریکا علاوه بر شلیک حدود ۲۰۰ موشک تاد، بیش از ۱۰۰ موشک رهگیر از انواع استاندارد-۳ (SM-۳) و استاندارد-۶ (SM-۶) را هم مصرف کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/akhbarefori/653832" target="_blank">📅 16:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653831">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۸ هزار شرکت در ایران منحل شدند!
اعظم قویدل، سخنگوی سازمان ثبت اسناد و املاک کشور در
#گفتگو
با خبرفوری:
🔹
تعداد ۷۷ هزارو ۹۸۷ شرکت در سال ۱۴۰۴ در ادارات ثبت شرکت‌ها و موسسات غیرتجاری به ثبت رسیده است و ۷ هزار و ۹۵۴ شرکت نیز منحل شده است.
🔹
در سال ۱۴۰۴ تعداد اظهارنامه‌های اختراعات ۱۱ هزار و ۱۱۶ فقره و تعداد اختراعات ثبت شده هزار و ۲۵۸ فقره بوده است.
🔹
علایم تجاری ثبت شده ۲۴ هزار و ۵۵۸ فقره و طرح‌های صنعتی ثبت شده ۱۳۲۸ فقره بوده است.
🔹
بعد از اجرای قانون الزام یعنی از ۳ تیرماه ۱۴۰۳ تاکنون بیش از ۹ میلیون و ۳۰۰ هزار فقره سند مالکیت حدنگار سبزرنگ ثبت شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/akhbarefori/653831" target="_blank">📅 16:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653830">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
دستور اجازه قصاص قاتل خبرنگار ایرنا صادر شد/ پرونده در اجرای احکام است
🔹
وکیل مدافع اولیای دم «منصوره قدیری‌جاوید»، خبرنگار که آبان ماه ۱۴۰۳ به قتل رسید گفت: قوه قضاییه دستور استیذان اجرای حکم قصاص متهم پرونده را صادر کرده است و باید فعلا برای اجرای حکم منتظر ماند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/akhbarefori/653830" target="_blank">📅 15:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653829">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJGiD58QIoBZyQLa9yXGpaEZ7K0EkmnhXPWbZbb3stoF5Gd8S0FyO60DKdqEs2PhIDaiLMdtUed95WAymSNyE3tH4czDrEjbkDnoSs8isdrOL_wu94AV8L3QU93jmqVLjlq0oBqFrsJxeOYtZ34vEe4e7IfZaMQIo69tJkZ2MmKivy_amxPA4hif5evnziIOkTy9QZJbaiCaEklklmUSNvWi1vvHRHGoQGsmQ8dWa_IhAb0XTsE-aqfxsD44yavD1RS06RuQpYtDVv82kNnzQOEbndooqp-vR98i9g_I4ZvzwBT1trNlKZWv_iSLUciesTJ6ybwscV_1DBIzGmpn3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیرکل سازمان ملل از شکست کنفرانس ان.پی.تی ابراز ناامیدی کرد
🔹
به دنبال شکست کنفرانس بازنگری پیمان منع گسترش سلاح‌های هسته‌ای که به مدت ۴ هفته در نیویورک برگزار شد، آنتونیو گوترش از این موضوع ابراز تاسف کرد.
🔹
استفان دوجاریک، سخنگوی سازمان ملل در بیانیه‌ای گفت که گوترش «از مشارکت صمیمانه و معنادار کشورهای عضو استقبال می‌کند»، اما ابراز تأسف کرد که کنفرانس بازنگری «کمبودهایی داشت، به ویژه در زمانی که با چنین چالش‌های مبرمی که امنیت بین‌المللی را تهدید می‌کنند، روبرو هستیم.»
🔹
در ادامه این بیانیه آمده است که رئیس سازمان ملل از کشورها خواست «تا از تمام مسیرهای موجود گفت‌وگو، دیپلماسی و مذاکره به طور کامل استفاده کنند تا تنش‌ها را کاهش دهند، خطرات هسته‌ای را پایین بیاورند و در نهایت تهدید هسته‌ای را از بین ببرند.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/akhbarefori/653829" target="_blank">📅 15:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653828">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcegVCKamGXW-OahZSFyP_J30xdZGNC_uc7uQk68SUzoWxj0LSJ6LMKzf4M6fEzezIW-RhYxlPJBwIuryI03BUDQPDzKgOqjP5sI4BorXM61op9y2FGuh5U8PCLTP5jWK3_V1djp5YcUr1HQbS_2-K-H5dbAHVCnjBCaiwbDzv24u3nV-uwvE1UOz35EzOfdvQ7Frt03WVL76tj1MVynJGQQv2qySGOj2jLb7jiCOSsH4_uEnOy-8c857H9uPd1fvjfhRCyxHbkC4SNCmirBgFrXlQePlmkwtGA5rJfrj1s6dwq703UcVvrXyGGkBqvXIbq8UqyaFxgOVwW7IEdUhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دغدغه رهبرانقلاب برروی دیوارنگاره میدان انقلاب تهران: با افزایش جمعیت به ایران جان بده
از جدیدترین طرح دیوارنگاره میدان انقلاب تهران پس از پیام اخیررهبرانقلاب به مناسب روز ملی جمعیت با شعار "به ایران جان بده" رونمایی شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/akhbarefori/653828" target="_blank">📅 15:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653827">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2ce1f123c.mp4?token=lOvlLSeN0jIJkZqVhmo7PHF2H5q8Ix9Zc-LoPDXjV23l20f9QtgGVnLsFMJChjQ7JJJbtv3X0xIr-A6suEdArYopcmLivGz42QjmIP5YIgvR22T1sQhj15toeABOGcii2HV-bmwENUS0rVAcfAggwnQuc3K3oLf_0y5QZgzE4UGVu1shZi9ZS0772GlpGONqF2huQDPMLnzNcRFqvWj2xO_m538JasWiSPPCAzlvYOgZYvuOd6bPavt9IsYD7VM3ydGBLXs_8uTAMPTGWQrh95eBYOTax3iC_UFM0OJDUmISgDpyyO9Lif-Ek1aqtds-xK9PB0UTALSKMi-En6xJJbuXxx9fSUxyIbwHbhIFWPgzoM2Gce6WXR5Y3iJbUXy-et0vsR1yEIKdL7LND2iUAdK7YKUD3r-bCYqKvQx7C4qrcwkoU8ZREBtasVc_dyYovwHAVEnDnR3iogbC7JfoBacAmHGycBzL6C_d9TMF9v3Bv0PKm0gXjWlxwtMJcl4bvjtD7pzvzI6YJAq9xb3knMmKgLPpTWWESHLoK8Wsbn5BOTjGepjDE5Cmv_YuWaJQRn9GFaJqxWMvxtBQSyEk3dOuwXlsACjtxMkb7rgYo75ca4LJFgGcE0uU1wGTcNYT7i5cwpK6HpwLA5FG6DrYrxAVp_DE2aEaeg629hKLWxE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2ce1f123c.mp4?token=lOvlLSeN0jIJkZqVhmo7PHF2H5q8Ix9Zc-LoPDXjV23l20f9QtgGVnLsFMJChjQ7JJJbtv3X0xIr-A6suEdArYopcmLivGz42QjmIP5YIgvR22T1sQhj15toeABOGcii2HV-bmwENUS0rVAcfAggwnQuc3K3oLf_0y5QZgzE4UGVu1shZi9ZS0772GlpGONqF2huQDPMLnzNcRFqvWj2xO_m538JasWiSPPCAzlvYOgZYvuOd6bPavt9IsYD7VM3ydGBLXs_8uTAMPTGWQrh95eBYOTax3iC_UFM0OJDUmISgDpyyO9Lif-Ek1aqtds-xK9PB0UTALSKMi-En6xJJbuXxx9fSUxyIbwHbhIFWPgzoM2Gce6WXR5Y3iJbUXy-et0vsR1yEIKdL7LND2iUAdK7YKUD3r-bCYqKvQx7C4qrcwkoU8ZREBtasVc_dyYovwHAVEnDnR3iogbC7JfoBacAmHGycBzL6C_d9TMF9v3Bv0PKm0gXjWlxwtMJcl4bvjtD7pzvzI6YJAq9xb3knMmKgLPpTWWESHLoK8Wsbn5BOTjGepjDE5Cmv_YuWaJQRn9GFaJqxWMvxtBQSyEk3dOuwXlsACjtxMkb7rgYo75ca4LJFgGcE0uU1wGTcNYT7i5cwpK6HpwLA5FG6DrYrxAVp_DE2aEaeg629hKLWxE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پلو تخم‌مرغ وارد منوی رستوران‌ها شد!
🔹
منوی رستوران‌ها به حدی عجیب و قریب و نجومی شد که با دیدنش برق از سرتان می‌پرد!
🔹
باورتان می‌شود که برخی غذاها پرسی ۷ میلیون تومان است! در این ویدئو ببینید
@Tv_Fori</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/akhbarefori/653827" target="_blank">📅 15:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653826">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b32b509d2d.mp4?token=Erdaw3vTaeDBZd-RnFIVAtk2G7Bjvzy22W-xO33Ja6Iv3GiusuC9lAqNsjHyl0LicRl-WJyoQOcg1BTWuAI3_Px93aQE9NPMU4fhdI3mNiEfA5UAczMf7Umn2uUE1V79AdXpteqLNsNxgySUReL0vmYQOzjueRIS-FKzYCCremGTgXZJNZNxHcmpIZT0kFHe-DsEqe6C_f_7TfwoIcpkiIWOhHf50bu2CzTU07ZcHR8F4W_2e5IQg7vBJA3ld5EBL_FzS-ooFMtVLw8358K0LTVf1PhQgOASh5zqZd9H8XBi42NYAVQ7WVx14Iypv_84iHr_wB2PAC-9ImHH65V82y6fd8uM2JQpKN4Oe5-4DpB559Y5Q0vNxyZOIZ61xb_EvXUi_gB-ZMYOrb24F66LGjtyuy82PyCfZEkOw-aRHOGU1SLCpw6g7uKZhKYQkdEa4jQeF31AuwlsV8vWktiZu3b3Ei9em533I5-nCRl09vLJZq6wbIFXqvpGDBQivYnA23695qj8sObwk-k481cJqDU2EPo-0f1L9mUg2LMfh9PiSpeFVdtE8b_FHaPpacrVT2iC5oANMqr34-89DcFBVWrP-DFkzJGmIYauM37fc-hxbKxDpQQmkscD88W5iP0KU4LkszidGoNXC6KeNi0TlRif-gqzf6eDqANQ3WEiK30" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b32b509d2d.mp4?token=Erdaw3vTaeDBZd-RnFIVAtk2G7Bjvzy22W-xO33Ja6Iv3GiusuC9lAqNsjHyl0LicRl-WJyoQOcg1BTWuAI3_Px93aQE9NPMU4fhdI3mNiEfA5UAczMf7Umn2uUE1V79AdXpteqLNsNxgySUReL0vmYQOzjueRIS-FKzYCCremGTgXZJNZNxHcmpIZT0kFHe-DsEqe6C_f_7TfwoIcpkiIWOhHf50bu2CzTU07ZcHR8F4W_2e5IQg7vBJA3ld5EBL_FzS-ooFMtVLw8358K0LTVf1PhQgOASh5zqZd9H8XBi42NYAVQ7WVx14Iypv_84iHr_wB2PAC-9ImHH65V82y6fd8uM2JQpKN4Oe5-4DpB559Y5Q0vNxyZOIZ61xb_EvXUi_gB-ZMYOrb24F66LGjtyuy82PyCfZEkOw-aRHOGU1SLCpw6g7uKZhKYQkdEa4jQeF31AuwlsV8vWktiZu3b3Ei9em533I5-nCRl09vLJZq6wbIFXqvpGDBQivYnA23695qj8sObwk-k481cJqDU2EPo-0f1L9mUg2LMfh9PiSpeFVdtE8b_FHaPpacrVT2iC5oANMqr34-89DcFBVWrP-DFkzJGmIYauM37fc-hxbKxDpQQmkscD88W5iP0KU4LkszidGoNXC6KeNi0TlRif-gqzf6eDqANQ3WEiK30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهار گرانی با بهره‌گیری از سازوکارهای تخصصی محور اصلی سخنان معاون اول رئیس جمهور در ستاد هماهنگی اقتصادی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/akhbarefori/653826" target="_blank">📅 15:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653825">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به افزایش قیمت‌ کتاب، رفتار خرید شما چه تغییری کرده است؟</h4>
<ul>
<li>✓ خرید کتاب فیزیکی کمتر | جایگزین با نسخه‌های الکترونیک و صوتی</li>
<li>✓ خرید کتاب فیزیکی کمتر | جایگزین با کتابخانه‌های عمومی</li>
<li>✓ خرید کتاب فیزیکی کمتر | جایگزین با امانت گرفتن از دوستان</li>
<li>✓ خرید کتاب فیزیکی کمتر | بدون جایگزین و کاهش میزان مطالعه</li>
<li>✓ بدون تغییر در خرید کتاب فیزیکی | کم کردن از هزینه‌های دیگرم</li>
</ul>
</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/akhbarefori/653825" target="_blank">📅 15:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653824">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyylrXFvdKjQv60rjjxvPUIudYohufW0P1yQCU9PSmTSEaGd4rBQVMPXnSXEtgw9Yid160G3S2UkkEuo7j7KFL492GQt8FSreqYFxPuPIv9i19KK_xZ1tgWM7NOJYHHRLvzEc0UpkcS40UV_bvsSSbaJbblfzs1XpMMgItCAa4sC82ErJTjeH8zavX5bkOi1yCrDzT_ZS4n6PIR2xFuLjqOhINWnvbPtuwB0o8nd2TBYoA9Z7vgV4WiQlr0owkOCCCrnBGF7W7A_y9HsTJ5wkWGwJSFw-AtCYXJH4Y2gLhVU01R4SA7zPsDoopa53wjqz-2afV3_YJE4uu7FbuEQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گوگل محدودیت دیرینه را برداشت
🔹
گوگل امکان تغییر آدرس ایمیل اصلی را ایجاد کرد. حالا دیگر لازم نیست به خاطر آدرس‌های نامناسب دوران نوجوانی، اکانت جدید بسازید یا از شر ایمیل‌های قدیمی خلاص شوید.
🔹
بر اساس اعلام گوگل، هر کاربر سالانه فقط یک بار اجازه تغییر آدرس دارد. اما نکته مهم، آدرس قبلی آزاد نمی‌شود و همچنان به اکانت شما متصل می‌ماند تا ایمیل‌های ارسالی به آن، کماکان به دستتان برسد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/akhbarefori/653824" target="_blank">📅 15:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653823">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64d2538a96.mp4?token=tBQv58rzmqeawMHl4MDg7Qh249vAQz4I9q6Xcyz2Zvj9lWLKrWbhhyGpeL2j0102NJleVMP1BhxP62PvSI8qmNMzhoGrVJzI6NqPtoAS5Jg_-lbPakYR1FDPJdS-gO5Nqu2LJTlQunGgbcBeji4Cdk1Je8MogHrIVHeoKT9mkwNEspRo1yYXdUqBoJU7tUvecjNvSv0QBmNTuzG5KthrSN6CipklXOlfbQrIxxC924h0kXzTsrQ_mkw002rNanpWvrXUZF_PNYT0bhkg-Ys4gLMNNaxo6rxzeC30uzBVnt6oVR7osIgh_igpFVlUm5M33RXy6q-E_0BY8Vzh_upo6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64d2538a96.mp4?token=tBQv58rzmqeawMHl4MDg7Qh249vAQz4I9q6Xcyz2Zvj9lWLKrWbhhyGpeL2j0102NJleVMP1BhxP62PvSI8qmNMzhoGrVJzI6NqPtoAS5Jg_-lbPakYR1FDPJdS-gO5Nqu2LJTlQunGgbcBeji4Cdk1Je8MogHrIVHeoKT9mkwNEspRo1yYXdUqBoJU7tUvecjNvSv0QBmNTuzG5KthrSN6CipklXOlfbQrIxxC924h0kXzTsrQ_mkw002rNanpWvrXUZF_PNYT0bhkg-Ys4gLMNNaxo6rxzeC30uzBVnt6oVR7osIgh_igpFVlUm5M33RXy6q-E_0BY8Vzh_upo6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر نیرو: برق مشترکانی که با دولت برای مصرف بهینه همکاری نکنند، قطع خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/akhbarefori/653823" target="_blank">📅 15:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653822">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
بحرین ۹ نفر را به اتهام همکاری با ایران به حبس ابد محکوم کرد
🔹
دادگاهی در این بحرین ۹ متهم را به حبس ابد و ۲ نفر دیگر را به ۳ سال زندان محکوم کرد. اتهام این افراد همکاری با سپاه پاسداران برای انجام اقداماتی بوده که دادگاه آن‌ها را «اعمال خصمانه و تروریستی» علیه بحرین توصیف کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/akhbarefori/653822" target="_blank">📅 14:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653821">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cV5dUtqWz4M0-kLUAu1hKFyMQA_6iShWhciGxvKuslfBDVpoEpweXZsOInO3pDlWlssHEc9jUCIC5lueVT9Tt2hJ-f-1nRI7HjwPdHHhK3tGcSByzyYQ8AcjhWWk6CWAXjpO2TJVp2HqQD68_73jBPBPYwbh93QlYywGjg-Y-xwVEqt00br6IaXh_9r5S7xSG9LobPp69x__MXf_SqHflkm5I0WwjqPoC5uSf47Geksh6s2NXNTSJ-QXD6z4LSuJXiqr6Wur1BTSSDsMcENszn8OCXI-odlx9AnauQpbd9CqgUZ4Z2yWvuaJGPoIo69AxH885N3eDGCDxkOmSLh-HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابهام در مسیر توافق؛ روایت‌سازی واشنگتن و واقعیت مذاکرات
🔹
در حالی که موجی از اخبار درباره احتمال توافق منتشر شده، بررسی واقعیت‌های سیاسی و میدانی نشان می‌دهد حتی در صورت دستیابی به توافق اولیه، مسیر رسیدن به یک توافق پایدار پیچیده است.
🔹
ناظران سیاسی بر این باورند که حتی در صورت اعلام توافق، آنچه شکل خواهد گرفت صرفاً یک «توافق موقت» خواهد بود؛ توافقی شکننده که بسیاری از مسائل اصلی و اختلافات بنیادین در آن حل‌وفصل نشده و به مراحل بعدی مذاکرات موکول می‌شود. همین مسئله موجب شده تا در ارزیابی تحولات، احتیاط و پرهیز از خوش‌بینی زودهنگام به یک ضرورت راهبردی تبدیل شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/653821" target="_blank">📅 14:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653820">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نقدعلی: مجلس پلمب شده است!
محمدتقی نقدعلی، عضو کمیسیون حقوقی و قضایی مجلس در
#گفتگو
با خبرفوری:
🔹
مجلس سه ماه است که در تعطیلی مطلق به سر می برد؛ مجلس پلمب شده است.
🔹
نمایندگان از محتوای مذاکرات به معنای واقعی بی‌خبر هستند.
🔹
ما مجلسیان از اینکه روند مذاکرات به سود یا ضرر ملت ایران است، اطلاعی نداریم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/akhbarefori/653820" target="_blank">📅 14:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653819">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
سفر تیم امنیتی عراق به تهران
🔹
قاسم الاعرجی، مشاور امنیت ملی عراق، روز یکشنبه اعلام کرد که یک هیئت امنیتی مشترک عالی‌رتبه از بغداد و اربیل به تهران سفر خواهد کرد.
🔹
این هیئت قرار است تحت نظر کمیته عالی امنیت عراق و ایران پیرامون توافق‌نامه امنیت مرزی ۲۰۲۳ و حفاظت مشترک از مرزها و گسترش همکاری‌های امنیتی تشکیل جلسه دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/akhbarefori/653819" target="_blank">📅 14:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653818">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVG2t31usf-apuDcr4m7rkeZZw0EOELch4T8nLJjIxklseVTjiro75nNr8AJHQykPBX3S9wdpAS0sKTrT30sk6eYZGDGZkUUU3xbL5qH6bPZfa0alBrU8JYVfdq1JTb6R366PXCTaDBOwSNBemB0eD5wmxJqxmqgHWNSx4P9f_3y2x8oCzUW9yRBXZrhFtZxm4EQv013Z5LlJf593ypsafISMxW0Yems-_DiDemw1D-_JwSlBPOEJQnS2EfT4YfmkuT4xUAAoGRReR4k842xZixrl0S8gjefoJRt1jJn-PxI04RrIY7gh0grkXRTniuDEK7xhGJfwUMeEoI_1hCPQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنان ضد ایرانی کمیسیون اروپا: هرمز باید باز شود
🔹
رئیس کمیسیون اروپا اورسلا فون درلاین، از «پیشرفت» رایزنی‌ها بین واشنگتن و تهران استقبال کرد و به طرح ادعاهایی علیه برنامه هسته‌ای و نفوذ منطقه‌ای ایران پرداخت.
🔹
او در شبکه ایکس (توئیتر سابق) نوشت: «من از پیشرفت به سوی توافق بین ایالات متحده و ایران استقبال می‌کنم. ما به توافقی نیاز داریم که واقعاً از شدت درگیری‌ها بکاهد، تنگه هرمز را بازگشایی کند و آزادی کامل ناوبری را تضمین کند.»
🔹
فون درلاین گفت: «ایران نباید اجازه توسعه سلاح هسته‌ای را داشته باشد. همچنین باید به اقدامات بی‌ثبات‌کننده خود در منطقه، چه مستقیم و چه از طریق نیروهای نیابتی، و همچنین حملات ناموجه و مکرر خود به همسایگانش پایان دهد.»
🔹
این مقام ارشد غربی تصریح کرد: «اروپا به همکاری با شرکای بین‌المللی خود ادامه خواهد داد تا از این فرصت برای یک راه‌حل دیپلماتیک پایدار استفاده کند و از سرایت این درگیری، به‌ویژه به زنجیره‌های تأمین و قیمت انرژی، جلوگیری کند.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/akhbarefori/653818" target="_blank">📅 14:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653817">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87c364b394.mp4?token=FxdFHe_Ekea_Qp8WWY1kdPwZCzRo7-xiiEySwU-3OgIjodGLqIic82ZHRyG3t3ThFMnMTZLPbzP7fAOGn7zl8tWNeWutJdw2q8wK794nR6TybMB8APQjNIH66BgcWVl7ue22bBvcIzv-ZtzrlQ-JFkRL_j5kPtOhnW_VwDxhgEPTUtjs2xvUCNCcYehwHC1q1oDg2QXqrPxU8hw14eSBOMjvf_RveBmhOGekZtteFsbQr7xFgF4N_xYKwZsCUZ2BCimZzE5ZyMThniQqTMdeL5qOgvBwliXacyFd2ACprMIAZwxFEix1ovkRePikfRgRSqCX97S7gSbWMxUWqUWLBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87c364b394.mp4?token=FxdFHe_Ekea_Qp8WWY1kdPwZCzRo7-xiiEySwU-3OgIjodGLqIic82ZHRyG3t3ThFMnMTZLPbzP7fAOGn7zl8tWNeWutJdw2q8wK794nR6TybMB8APQjNIH66BgcWVl7ue22bBvcIzv-ZtzrlQ-JFkRL_j5kPtOhnW_VwDxhgEPTUtjs2xvUCNCcYehwHC1q1oDg2QXqrPxU8hw14eSBOMjvf_RveBmhOGekZtteFsbQr7xFgF4N_xYKwZsCUZ2BCimZzE5ZyMThniQqTMdeL5qOgvBwliXacyFd2ACprMIAZwxFEix1ovkRePikfRgRSqCX97S7gSbWMxUWqUWLBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: اولویت دولت معیشت مردم است
🔹
از مردم بابت صرفه‌جویی در مصرف انزژی تشکر می‌کنم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/akhbarefori/653817" target="_blank">📅 14:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653816">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bddb0791d8.mp4?token=LYfDlfffnVoAz_SxXXnh4_MaNOQci-87Qwk6Iw8skG_1uANszrFcnkXH9XMsQpSX3geUv0jQ6ff5EJRdYhA4QPzM50gAsEPBxPGVXSAxlb3mUvay7V3bk_1dPB9GNcevkL5vPX76BFzaBXwjq0mbV2UbAdikATjgOT86v90QG1AM6R4-2EsPzfGObdEl4bSf1-LxSUD9bo35jXVJ3V4v3kGAnqaOAEOh89ssoN1IsBVD6OBM6ehVgFPpVIu9RfMlwfnxMBoMm3sYtY3iwfQD0-568Ofik4EaYhl9uXKjCXx97Pin7njJnpn6K2zO3efG6TATSO35Agl20cp8LKk1_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bddb0791d8.mp4?token=LYfDlfffnVoAz_SxXXnh4_MaNOQci-87Qwk6Iw8skG_1uANszrFcnkXH9XMsQpSX3geUv0jQ6ff5EJRdYhA4QPzM50gAsEPBxPGVXSAxlb3mUvay7V3bk_1dPB9GNcevkL5vPX76BFzaBXwjq0mbV2UbAdikATjgOT86v90QG1AM6R4-2EsPzfGObdEl4bSf1-LxSUD9bo35jXVJ3V4v3kGAnqaOAEOh89ssoN1IsBVD6OBM6ehVgFPpVIu9RfMlwfnxMBoMm3sYtY3iwfQD0-568Ofik4EaYhl9uXKjCXx97Pin7njJnpn6K2zO3efG6TATSO35Agl20cp8LKk1_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کمبودِ ۷ مهمات کلیدی و عقب‌نشینی ترامپ از جنگ ایران
🔹
شبکه الجزیره در تحلیلی درباره کاهش ذخایر تسلیحاتی آمریکا در جنگ با ایران نوشت، کمبود در ۷ نوع مهمات کلیدی ارتش ایالات متحده از دلایل عقب‌نشینی ترامپ از ادامه جنگ با ایران است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/akhbarefori/653816" target="_blank">📅 14:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653815">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
هدف قرار دادن پهپاد صهیونی بر فراز هرمزگان
🔹
این پهپاد صهیونی، که کاربری جاسوسی و شناسایی داشت، با شلیک پدافند ارتش سرنگون شد.
🔹
پهپاد اربیتر رادار گریز است و با سامانه ویژه‌ای هدف قرار گرفت که مشخصات آن را مسئولان منطقه عملیاتی پدافند جنوب شرق کشور، مستقر در بندرعباس اعلام نمی‌کنند و می‌گویند، با این سامانه، هیچ پهپاد رادارگریزی نمی‌تواند به آسمان منطقه ماموریت، از خلیج فارس و جزایر تا سراسر منطقه جنوب و جنوب شرق کشور نفوذ کند.
🔹
لاشه پهپاد متلاشی شده اربیتر هم با همکاری ناوگروه دریابانی فراجای هرمزگان کشف شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/akhbarefori/653815" target="_blank">📅 14:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653814">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ما سوم خردادی هستیم
🔹
محمد زعیم زاده، سردبیر فرهیختگان نوشت:
🔹
بعد از نادر هر وقت جنگی در ایران در گرفت بخشی از این خاک جدا شد، گاهی حتی بدون جنگ خاک دادیم مثل ماجرای بحرين. اولین بار که این خط شکسته شد در ماجرای آزادسازی خرمشهر بود. ۳خرداد ۶۱ کمر صدام شکست، حباب توهماتش ترکید، اعتماد به نفس به ما برگشت، ایران حفظ شد و این خط تا امروز ادامه دارد. ما سوم خردادی هستیم.
🔹
در اسناد و مکتوبات فتح خرمشهر هر چه بیشتر گشتم یک گزاره برایم قطعی‌تر شد. بعد از لطف خدا و رهبری امام اگر بخواهیم حماسه خرمشهر را تحلیل کنیم و از یک قهرمان مسجل نام ببریم به حسن باقری می‌سیم. نابغه‌ای که هر چه در احوالاتش غور می‌کنی بیش‌تر شیفته‌اش می‌شوی. عقلانیت شجاعت، کاریزما خستگی ناپذیری، عاطفه ... همه یک جا جمع است.
🔹
سردار دل‌ها درباره او می‌گوید باقری، بهشتی جبهه‌ها بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/akhbarefori/653814" target="_blank">📅 13:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653813">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyW82HeZNzfEwGoU61VSZQ1_ea2l5LGhmHSAmDR3TGhpnwaV_uLe0vYV6cHhT1AEaJraajjCECdtKPlmPMmur5paJEhXGHOUsgANZ5M9LjPLXl2RW9ciSHNbqsmA1Q4kQMR_9Lr-Z6eloImbmTROVXTVbQEQoboAdKx36lPUIHGevQTwhqe6i-2N6N8m6ABjADaoSoLvyTGYQBo7c_HD3A2Pbwvpnc6wqqZ5fWBLpG93JDLHkArkmaww3oh_j0m7yIWIADs6qs603O7Ki4Vq_NndmbSazxY_Ps6KxINaYL9csy6CCklSrxfec0svMhpCjBGEcBBhqgd7FHCjs73qSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تایمز اسرائیل: واشنگتن و تل‌آویو به هدف خود در قبال ایران نرسیدند
🔹
یک رسانه صهیونیستی، از بین بردن توان هسته‌ای ایران را مهمترین هدف آمریکا و رژیم صهیونیستی از جنگ علیه تهران عنوان کرد که در رسیدن به آن ناکام مانده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/akhbarefori/653813" target="_blank">📅 13:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653812">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaSp36185GMKycG8NVLdeJptoJbuO4nwWHGza0V2xuWYAWyriLNQsdmKGiqkLv8is4fXGKyXlrDU00I25q2TS13PNFk76OxD7YASdCh5-eIx1QZIiWWue4qJbdpV0gLW_QnhqHfxWfKV4osYrlqQuY8iSCeDfENtbaIdYVtlTm_l870Whs6ulW1zZx9pCSKJA0ZDNvV9_Up-uIeae2cVd8vL0ve9zGy_5f-UWkwk_TjQs_sniiwEH_uZwYG6rg7QAfo23Vg7BZLsmpYrMPI2WhYPbaHcQ66C3nXgvXQUwxhV0oi9zzBYv2sKnf9hlHivdJp2GT9Of_w1v-uKBlpCRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شروط انگلیس برای «توافق آمریکا و ایران»!
🔹
نخست‌وزیر انگلیس کی‌یر استارمر با بیان اینکه «از پیشرفت به سوی توافق بین ایالات متحده و ایران استقبال می‌کنم»، به تشریح شروط مدنظر خود برای این توافق پرداخت.
🔹
نخست‌وزیر انگلیس با انتشار یک پیام در شبکه ایکس (توئیتر سابق) نوشت: «من از پیشرفت به سوی توافق بین ایالات متحده و ایران استقبال می‌کنم.»
🔹
استارمر بلافاصله بعد از این جمله گفت: «ما باید شاهد توافقی باشیم که به درگیری (جنگ) پایان دهد و تنگه هرمز را با آزادی بی‌قید و شرط و نامحدود دریانوردی بازگشایی کند. بسیار مهم است که هرگز به ایران اجازه داده نشود سلاح هسته‌ای تولید کند.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/akhbarefori/653812" target="_blank">📅 13:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653811">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkhATDg0N1VynO2YdNtIuasKxu_La2OSIjZhQxB77y3qidPxIVAYhuYize0xOMC4pgsmbSxt5Wld01vyZc2X2FUxw7GJp16S-77WrffqcNqcH3ZB36NOSxnEiPlvioez9Wlu_TjKAvGAnVvNDEFGnhq3h7VShlZj5a8HRj7uQSN-2PDCCgUe_Wp2ci6PnbsjJD8z8nFteK-9EDclfhoIFoIZeTLrdhhRK0db_b8E0t1SF_PCV6BJB9XhvizhdRDNLXLCao1ibc9DnM1gXdLXaURGSeiwDGx9E-uLa05iOA3R_CrWwVR_YDK__FjOU4LdKzOgNJRWGuRahcJhF3r1rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات مبلغ و شرایط پرداخت وام ازدواج در سال جدید
🔹
بانک مرکزی: به هر یک از زوجین که تاریخ عقد آن‌ها واجد شرایط قانونی باشد، مبلغ ۳۰۰ میلیون تومان تسهیلات قرض‌الحسنه ازدواج تعلق می‌گیرد.
🔹
اگر سن زوج (مرد) زیر ۲۵ سال و سن زوجه (زن) زیر ۲۳ سال باشد، مبلغ این وام برای هر یک از آن‌ها به ۳۵۰ میلیون تومان افزایش خواهد یافت.
🔹
باز پرداخت این تسهیلات برای تمامی زوجین ۱۲۰ ماهه و با کارمزد چهار درصد است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/akhbarefori/653811" target="_blank">📅 13:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653810">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9c68dac0.mp4?token=WGR28CrPuxlFmHuLPAOyekYRAqggjhZ8zgq-8lgXuwCy3Ii57EDHDbUnRe8zlBCu_RVBd1qcj-SAlPpYDjn_iFq1FNb6UzPUNCOEQvST-t9reRnqsR1JEmXnHWJ-ijFzWvEihOmNOYVjiVC0Z5g0CUvNpsiQ4_ZfuYsQlEfRSTZXlGREr3bhlaBS8hC4J98c3cfpGonMlxWXh4fgsuTS5mBm9GNSF3oQ_eZzKHEnYFe61BX6OEemloUebocExOFQ8hImwOeTj3_BkHnpI6Im65EZU5prMXzE1YlO2aOgZ85ntYqHnIabmziADHwAP-vwZL-Is2iS6PHXwnAXNLAE4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9c68dac0.mp4?token=WGR28CrPuxlFmHuLPAOyekYRAqggjhZ8zgq-8lgXuwCy3Ii57EDHDbUnRe8zlBCu_RVBd1qcj-SAlPpYDjn_iFq1FNb6UzPUNCOEQvST-t9reRnqsR1JEmXnHWJ-ijFzWvEihOmNOYVjiVC0Z5g0CUvNpsiQ4_ZfuYsQlEfRSTZXlGREr3bhlaBS8hC4J98c3cfpGonMlxWXh4fgsuTS5mBm9GNSF3oQ_eZzKHEnYFe61BX6OEemloUebocExOFQ8hImwOeTj3_BkHnpI6Im65EZU5prMXzE1YlO2aOgZ85ntYqHnIabmziADHwAP-vwZL-Is2iS6PHXwnAXNLAE4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس جمهور در نشستی با رئیس و جمعی از مدیران رسانه ملی از پوشش و روایت جنگ اخیر قدردانی کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/akhbarefori/653810" target="_blank">📅 13:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653809">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSrZCK3N7g3wg9ZAU_fEwhGvrbmZkn2oAfbr3rJzyqbiAleA-ElyZXdeVlcPB9P8vB_GthsA1e-uvsl10vrtpU42R_v5wxw0Yfu9IBCxl9nXLptlVJ4mD1mg9LYEcTBROiVQfNDYe_7pbiv7cv0LdxTmgg85SkVKdg_mN0bRB-loxp7zsKhjU40jg_SiAui9REg7VK-V94IB0kfFdOTwMl5cr-9oMxrlC7Ojl2Q5fuIGIMXX91dB7LUrnBoDVRrFlNuFiIArRGcBnkcxonXMgw57Yh8LSICl2NiHLD1PgeRU9v1Pim0P2pPX_t5zcXgCNtjvEmlNliPLnaBttyD-Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خنثی‌سازی مهمات عمل نکرده در اطراف نیروگاه اتمی بوشهر
🔹
عملیات کنترل‌شده خنثی‌سازی مهمات عمل‌نکرده حملات باند تبهکار آمریکایی - صهیونی در اطراف نیروگاه اتمی بوشهر در دست اجراست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/akhbarefori/653809" target="_blank">📅 13:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653808">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxiBGG0BTcLrAhxBfRialvJqL6tmFKOgX4I_qtJn4ZRlcndbv_AIq2pDd3wNFBuairLhtuyzjxoVeOoky9rHp3lI2ltvvKK7yt3qb_mTYi1ojNB2ZYi_G79SLBhe2wOHMIW10WXXyRFkcrWTTA8udlQCjBEpvL3BL6NBjUeLnrPibc3xrp3zzTVH40TPG8kk2cpgqBQjjrKfVvAWp7FE4nJI8z037N8E1IlSk0AA64kWAsDbgglaYogQi1ghUDe4Arm6ghsRcrCYzLfq5OLBvv4sF_BNsWD4EHk-IaTXclqd5vS2s7u6hXQs1ROqYg8BhQLfiKKZKCnFJIgIjCjy-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش فوری ویلا مدرن در چمستان (بهدشت )
- اطلاعات بیشتر و ارتباط با ما وارد لینک زیر شوید :
https://ble.ir/vila_aghsat
🏕️
ویلا مدرن نوساز
،داخل شهرک
🔥
✅
متراژ زمین ۲۰۰متر
✅
متراژ بنا ۲۰۰ متر
✅
۳ خوابه (مستر)
✅
روف گاردن با ویوی ابدی جنگل
✅
معاوضه با خودرو ،طلا،دلار و...
✅️
دارای سند تکبرگ
✅️
⭐
اقساط بدون بهره
⭐
قیمت :۵ میلیارد کلید تحویل
-برای اطلاعات بیشتر و ارتباط با ما وارد لینک زیر شوید :
https://ble.ir/vila_aghsat</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/akhbarefori/653808" target="_blank">📅 13:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653807">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eD42XK-i-1NaiJWFKzoFstBaLdSQ66l1VQh8SmLqh46Cc8EKuNsp99Ne4Fy_Facomynk4wn079o-_iO5vfpp-7aTJ8ScWVkQgPg2blSeUG-IqkIEdxgZWwrG8nlt3iXWK8Wez-qeYOVdcevv9FC-T8mJ93VCtr_MlbYZvq8ci48wG94ktGiRtfKOcNGVyK69yMTLW6JIxdetUj-jIv9ksr4A9GC59XmjUwdg6wKreq3eO5G15-AydZ-vjWqWYvcsMunLXTDlhRWGYrcXSCLRe3dbQ7ZiIRt88-Ll2PBPcvAIrlLQnkvFRLgyObDDxRj9npVc1AahavRBfZ6eDr2Mmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حال نامساعد «دارو» در پساجنگ؛ «کمبود» و «گرانی» با هم آمده‌اند!
🔹
چندی قبل یکی از نمایندگان مجلس، مدعی شده بود که بین کمبود یا گرانی دارو؛ می بایست یک گزینه را انتخاب کنیم. اما، باید گفت که در شرایط کنونی، بیماران با هر دو گزینه دست و پنجه نرم می کنند.
🔹
حالا کار به جایی رسیده که مجلس شورای اسلامی برای بررسی کمبودها و گرانی دارو، تشکیل جلسه مجازی داده و قرار است در این نشست، وزیر بهداشت هم باشد و به حرف های نمایندگان گوش دهد و برای آنها؛ پاسخ قانع کننده داشته باشد. هرچند که روز گذشته شاهد تشکیل جلسه کمیته تدابیر ویژه دارویی در وزارت بهداشت بودیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/akhbarefori/653807" target="_blank">📅 12:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653806">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3zNwaOUKgc0ZrlH-O3e2cqiYZwTQSHbCQWDGPokwjtk2BpncxSiXfAK4EfhRgbtTUDLv_fftx2Dq4qDEL11ydnhetWTQ7s5iM0A5V7yc1AGE9nIoRtUMteSqx1tvw2CGp3D5RtEcOeAVQKf0B9uAEjUM4d6WPqA4EXPCKmgkMyvLxczMAyHFMm7FvawitEPKILmpcMyaVwKOpj7VlLhKwKyT7Pff9AJaUNJC0UGczxyhV14cR-5JD7bxDtSlirNJ5CRVJ72OxugCOKv42n0TFLnd2U5XVvYR4gzrvEYM0u_CIwmeNuyVfPHqDV3-MvvBs0K_EHvS0asGpQydU2wUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه ۱۴ رژیم صهیونیستی گزارش داد که بنیامین نتانیاهو به وزرای کابینه صهیونیستی دستور داده است که از صحبت درباره توافق احتمالی میان تهران و واشنگتن خودداری کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/akhbarefori/653806" target="_blank">📅 12:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653805">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
نقش حاج قاسم از آزادسازی خرمشهر تا مبارزه با رژیم صهیونیستی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/akhbarefori/653805" target="_blank">📅 12:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653804">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAVNM1DNIYazqEGSovJxUGg--Rtp_fw0s4_xXwyndyaLRyxC8inVsxgsI8kFZrTGxamIKkhseLWBpX8Cct5Z08cH52QjShAOm83O_o4D-xE4lzJQiBgKt-sASbpjlvbX8xW6Fd_R43wHXJGMGF2ZgaoJLLE412Ne40gEhPZJAMa1EWuBkCbDqgjXey8p3Csfr1Jshj3j8BXoTuQogk6IeukdT4CbxJ0XpK9ich7T66BlXGgD3VK90ct83B46FGC_xS1Q7Bv3HibyClU29LNgoJUUU3KNYSZQOFP5gSBcf8AtL7SfuvhPdvy91baDjctshP02L_U87j8Wz1WWIhlFGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اژه‌ای: امروز حفظ وحدت ملی بخشی از امنیت ملی محسوب می‌شود
🔹
رئیس قوه قضائیه به مناسبت سوم خرداد:
🔹
سوم خرداد، تنها سالروز آزادسازی یک شهر نیست؛ بلکه یادآور مفهوم «وحدت» ، « خودباوری و مقاومت» به عنوان یکی از مهمترین مفاهیم راهبردی در تاریخ معاصر ایران است.
🔹
تجربه دفاع مقدس ها نشان می‌دهد که دشمنان ایران هر زمان احساس کنند جامعه دچار شکاف و چنددستگی شده، فشار‌ها را افزایش می‌دهند. در مقابل، هر زمان ملت ایران در کنار یکدیگر قرار گرفته‌اند، امکان عبور از بحران‌ها  نیز فراهم شده است.
🔹
امروز حفظ وحدت ملی تنها یک توصیه اخلاقی یا سیاسی نیست، بلکه بخشی از امنیت ملی کشور محسوب می‌شود.
🔹
در سه جنگ تحمیلی ۸ ساله، ۱۲ روزه و ۴۰ روزه، خرمشهرها را فتح کردیم و باز هم به مدد الهی فتح خواهیم کرد؛ مشروط به آنکه در مدار ولایتمداری بمانیم و انسجام و اتحاد ملی خود را تقویت کنیم و روحیه خودباوری را از دست ندهیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/akhbarefori/653804" target="_blank">📅 11:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653803">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s65TFKkXbWHJkFhukbCnbVd-Vdhf34mm2zEt_GmxuYLahY9YFi5F__fyA4BwqXugbeRv3PoLwmxh3m-4Q9eE0cIYEblBJs-cEdACzEe95ppGKo8Y9vzFHj-XYml9U45XTw_8hE0zUxmI7MeSbRp901wPLMv9pPDu3bJjv-gBFsvfZ7BdQ2yl46Oxne2StjAjcefW24LTVu2TDZxj1NE53bg7dqQWZsEOGlMSBZRPKM0a2vf4Okrz6kRvdY9kEz388bDsqFZc2tcR2yAeYrNKyowB6GXRBaPg17aWJSzfoj9LKyPKc1YSFD_T7JRArpX0tapAt_XreOFXsU_52k1LYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵۰۰ واحد تولیدی تهران در جنگ تحمیلی سوم آسیب دیدند
🔹
استاندار تهران: بیش از ۵۰۰ واحد تولیدی در سطح استان تهران در بمباران‌های رژیم صهیونیستی و آمریکا دچار خسارت ۱۰ تا ۱۰۰ درصدی شده‌اند.
🔹
در مجموع حمایت خوبی از ظرفیت‌های استانی انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/akhbarefori/653803" target="_blank">📅 11:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653802">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_M1SMLqEHhB-ATUC6u0RokIKSG3konHAV2gxO8gacyJGOOX-443g3F7PwtpjzikHSlETmhZ_SMLSa8MRT4uRw8Q0NSqGeuFV5xkEtwmfUWK_V_4hK2wAlc75bxi022Z2PKJ-L4uc3WrJimhh6RUQfkTuvRMRITSpnKYgrVqAJYuFSzkN0xZSQGiLWoclhzYbMsbHSg5D8LXJ9MRjE-LeL4L27-5xap0RiKg9UdTL2pCGmZi9iXEpqXd0jHmtfTSMhqo7Wsz9F_EvFZeR_HCFLJZtYa8SYg6ffolJFnVR35WtSX8209IcAyw68FqcrfG8qEHRSnurf90CrqSE3BLqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار منطقه غرب آسیا رویترز به نقل از یک منبع ارشد ایرانی گزارش داد که تهران تحویل ذخایر اورانیوم غنای بالای خود را نپذیرفته است
🔹
طبق این گزارش به نقل از منبع ناشناس مذکور، موضوع هسته‌ای، بخشی از توافق اولیه نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/akhbarefori/653802" target="_blank">📅 11:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653801">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
وزیر راه و شهرسازی: تسهیلات آسیب‌دیدگان جنگ در کمتر از ۳ روز پرداخت شد
🔹
تسهیلات مربوط به واحدهای خسارت‌دیده در کمتر از سه روز پرداخت شد و روند تامین سرپناه موقت و بازسازی مناطق آسیب‌دیده ادامه دارد.
🔹
جنگ اخیر زندگی مردم را در بیش از ۴۰۰ نقطه شهری و روستایی تحت تاثیر قرار داد و رسیدگی به وضعیت خانوارهای آسیب‌دیده در اولویت قرار گرفت.
🔹
عمل به تعهدات باقی‌مانده در حوزه مسکن، توسعه ابزارهای نوین تامین مالی، استفاده از ظرفیت بازار سرمایه و تقویت تسهیلات خرید و ساخت مسکن از برنامه‌های اصلی دولت در سال جاری است.
🔹
اجرای طرح مسکن استیجاری برای حمایت از اقشار کم‌درآمد و مدیریت بازار اجاره نیز از دیگر برنامه‌های در حال اجرا در بخش مسکن اعلام شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/akhbarefori/653801" target="_blank">📅 11:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653800">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
پزشکیان: هیچ تصمیمی بدون اذن رهبری گرفته نخواهد شد
🔹
رئیس‌جمهور در نشست با مدیران سازمان صداوسیما: هیچ تصمیمی خارج از چارچوب شورای‌عالی امنیت ملی و بدون هماهنگی و اذن مقام معظم رهبری اتخاذ نخواهد شد.
🔹
هنگامی که تصمیمی در حوزۀ دیپلماسی اتخاذ می‌شود، همۀ دستگاه‌ها، تریبون‌ها و جریان‌ها باید از آن حمایت کنند تا صدایی واحد و منسجم از ایران به جهان مخابره شود.
🔹
امروز صداوسیما باید منادی وحدت و انسجام ملی باشد. اگر همه باهم، در چارچوب منویات رهبر معظم انقلاب حرکت کنیم و انسجام ملی را حفظ نماییم، دشمنان هرگز به اهداف خود علیه کشور دست نخواهند یافت.
🔹
نمی‌توان هر فرد یا جریانی صرفاً بر مبنای سلیقۀ شخصی خود، نسخه‌ای متفاوت برای کشور ارائه دهد؛ چراکه ادارۀ کشور مستلزم تصمیم واحد و تبعیت جمعی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/653800" target="_blank">📅 10:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653799">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
فارس: پیش‌نویس توافق فاقد هرگونه تعهد هسته‌ای ایران است
🔹
در پاسخ به این ابهام‌آفرینی‌ها، منابع آگاه از روند مذاکرات تأکید کردند که در پیش‌نویس توافق احتمالی ایران و آمریکا هیچ بندی دربارهٔ تعهدات هسته‌ای ایران گنجانده نشده و تمام مسائل مرتبط با برنامهٔ هسته‌ای به مذاکرات ۶۰ روزه پس‌از امضای توافق موکول شده است.
🔹
برخلاف آنچه برخی رسانه‌ها تلاش دارند القا کنند، ایران در این توافق هیچ تعهدی برای واگذاری ذخایر هسته‌ای، خروج تجهیزات، تعطیلی تأسیسات یا حتی تعهد به نساختن بمب هسته‌ای وجود ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/akhbarefori/653799" target="_blank">📅 10:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653798">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
اسقاط تحریم نفتی ایران شامل پتروشیمی و مشتقات آن نیز خواهد شد
🔹
شنیده‌ها از جزئیات تفاهم اولیه «احتمالی»، میان ایران و آمریکا حاکی است که واشنگتن متعهد خواهد شد در طول دوره مذاکرات، تحریم‌های نفتی ایران را به حالت اسقاط (Waive) درآورد؛ اقدامی که به ایران امکان می‌دهد در این بازه زمانی، نفت خود را بدون محدودیت‌های ناشی از تحریم به فروش برساند.
🔹
اسقاط تحریم نفتی شامل پتروشیمی و مشتقات آن نیز خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/akhbarefori/653798" target="_blank">📅 10:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653796">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6904fa420a.mp4?token=NfdzAvFJIvMippSU3dKizm9gQpd-C14mqhdqEBAGrpmk1HLUjhJ7CsJDmwuy2t_TrTHUsvwhJRbyKy0VsiWQfdcqswXXP9WRii_U1SCNG1Hl6XyhXalQLDHsabr8-33rgqybYL3jElWhDsWtCeI6b8JPWKUmEe8hwQpmrF-24K12jMugvvgZ9wc6ebifSYFBA-PRwYHwtnY0q5vH_F1wE_DRTLtmpGtChH2Nu2yYwpiZUpSGRRO22EQU8gVGPPju4QjDl6aZ1lwHclTcRo1pm_PFlqlGEcLxZdzyWbPEoer1SiGbQvedyyfeJ_XUlfOczySXBN-0Su608fIomrgkdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6904fa420a.mp4?token=NfdzAvFJIvMippSU3dKizm9gQpd-C14mqhdqEBAGrpmk1HLUjhJ7CsJDmwuy2t_TrTHUsvwhJRbyKy0VsiWQfdcqswXXP9WRii_U1SCNG1Hl6XyhXalQLDHsabr8-33rgqybYL3jElWhDsWtCeI6b8JPWKUmEe8hwQpmrF-24K12jMugvvgZ9wc6ebifSYFBA-PRwYHwtnY0q5vH_F1wE_DRTLtmpGtChH2Nu2yYwpiZUpSGRRO22EQU8gVGPPju4QjDl6aZ1lwHclTcRo1pm_PFlqlGEcLxZdzyWbPEoer1SiGbQvedyyfeJ_XUlfOczySXBN-0Su608fIomrgkdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امیر مجتبی جعفری، مشاور فرمانده کل ارتش: همان‌طور که هشت سال دفاع مقدس، این مملکت را از نظر حمله نظامی به مدت ۴۰ سال بیمه کرد، ان‌شاءالله داستان جنگ سوم نیز این مملکت را به مدت ۴۰۰ سال بیمه خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/akhbarefori/653796" target="_blank">📅 10:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653795">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
قالیباف: امروز سربازان رهبر شهید انقلاب دنیا را متحیر کرده‌اند
🔹
امروز نیز سربازان رهبر رشید انقلاب که در مکتب امام شهید خود پرورش یافته‌اند دنیا را متحیر و مبهوت از رشادت‌های خود کرده‌اند و یاد سرداران فتح خرمشهر عزیز را زنده نگاه داشته‌اند
🔹
جوانانی که یادآور خرازی‌ها، همت‌ها، باقری‌ها، باکری‌ها، سلیمانی‌ها و هزاران قهرمان دیگر این وطن هستند. جوانانی که برآمده از دل ملت هستند و خواهران و برادران خود در خیابان را در میدان نبرد نمایندگی می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/akhbarefori/653795" target="_blank">📅 10:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653794">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
بخشی از دارایی‌های بلوکه شده ایران باید در گام اول آزاد شود
🔹
شنیده‌ها از جزئیات تفاهم اولیه «احتمالی» میان ایران و آمریکا حاکیست که در صورتی که این تفاهم‌نامه مورد توافق قرار گیرد، بخشی از دارایی‌های بلوکه شده ایران باید در گام اول آزاد شود.
🔹
با توجه به تجربیات بد پیشین ایران از نقض‌عهدهای طرف مقابل در آزادسازی اموال، ایران تاکید کرده است که هرگونه تفاهم اولیه (MOU) منوط به آزادسازی حداقل بخشی از این دارایی‌ها به نحوی است که کشورمان بتواند به آن دسترسی داشته باشد.
🔹
شنیده‌ها حاکیست که آمریکا در هفته‌های گذشته تلاش می‌کرد آزادسازی این دارایی‌ها را به توافق نهایی احتمالی در موضوع هسته‌ای گره بزند، اما ایران تأکید کرده است که دست‌کم بخشی از آن در همان ابتدای اعلام تفاهم باید آزاد شود. ضمن آنکه سازوکار آزادسازی بخش دیگر نیز باید در طول روند مذاکرات مشخص باشد.
🔹
درصورتی که آمریکایی‌ها مجدداً مانع آزادسازی شوند، ایران در مذاکرات آتی تجدیدنظر خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/akhbarefori/653794" target="_blank">📅 10:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653793">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUlHbhPcnp3DHeJT5VgPll6jPKHMA1x1ULeckZIWMXp8vikReFkm-ef2bwAJN1Sdfduw1YwdVD0SSVsLvN1ODD62nrw5-dHjHMlPWL8LsfDjFrz7OxFk2FBD2IDC2tVCaeS4UD7phyJ6L3KT-j-xNWTNTbk-m9bocGx_C17j4DFKv42fHz-MwTGGoGUnvHqJdlyoxRaWuUuiuKW6eSrxK0sAZ10Swgo2k4S7YnH7iIuKFmeUYkzk1h7hynhWPeMdD0E20ljm2uGzf2LSi8SE4Zp6K9HJo6bbRz9v2Gs5QNfkpaVITLZBRtAy8QO9BMTDgE47W9r9mGsOcdxRwXSTpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنگ خطر خروج متقاضیان از نهضت ملی مسکن؛ ضرورت افزایش ۲ برابری وام
🔹
محمدمنان رئیسی، نایب رئیس کمیسیون عمران مجلس، با اشاره به افزایش هزینه ساخت هر متر مسکن به ۴۰ میلیون تومان، در نامه‌ای به رئیس‌جمهور خواستار افزایش ۲ برابری وام نهضت ملی مسکن شد.
🔹
کارشناسان بازار مسکن تأکید دارند که امروز بخش قابل توجهی از مستأجران بیش از نیمی از درآمد ماهانه خود را صرف هزینه اجاره می‌کنند و این مسئله ضرورت اتخاذ تصمیمات فوری و عملیاتی از سوی دولت را دوچندان کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/akhbarefori/653793" target="_blank">📅 10:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653792">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa13283cdb.mp4?token=bZ-ysJYuShTqKgh0pwohXLKUjU8s4O5xMFG5UM_5fNS49cuN2OxJ8FkKytWRYhmlOuP3MHWt5CLIyQ8orDowXaXk6Yl6ntRXz_y3nR2-_Dj6FohXHbIPOmZurdHQA1RA5XnvsmnmUz_mOFM9yRtWIngN_L7Nck8YPxwYTTJjcqYzSB5VF6h252bclJ8HF57fmiG0s-80763sUUEf43ZllYVdXhwsFZ58cSAEyjT4Ujk25zIO0vUAXTfvvZ3atP0y_KoB8WBT_Ptw_vO8-JZVXpnjfoPfB9ySHrLOPwhl6AzKubKUkLNyPZ55YpPjXKra7TJd62IspHIggCzVdglJUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa13283cdb.mp4?token=bZ-ysJYuShTqKgh0pwohXLKUjU8s4O5xMFG5UM_5fNS49cuN2OxJ8FkKytWRYhmlOuP3MHWt5CLIyQ8orDowXaXk6Yl6ntRXz_y3nR2-_Dj6FohXHbIPOmZurdHQA1RA5XnvsmnmUz_mOFM9yRtWIngN_L7Nck8YPxwYTTJjcqYzSB5VF6h252bclJ8HF57fmiG0s-80763sUUEf43ZllYVdXhwsFZ58cSAEyjT4Ujk25zIO0vUAXTfvvZ3atP0y_KoB8WBT_Ptw_vO8-JZVXpnjfoPfB9ySHrLOPwhl6AzKubKUkLNyPZ55YpPjXKra7TJd62IspHIggCzVdglJUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر میراث فرهنگی: هنوز ابعاد شکست دشمن برای مردم باز نشده است/ وقایع دشت مهیار مهمترین شکست دشمن در چهار دهه گذشته است/ دشمن با همه تجهیزات و ژنرالهای نظامی جمع شد که عملیات سری انجام داده و اعلام پیروزی کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/akhbarefori/653792" target="_blank">📅 09:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653791">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcis60KyGo3cnMK29F_dBgfs9ZlAH7ih-grLYg46TGuMjOk1-ObZhypjGmmWYdigiTaI3NfrramhcFoYWvoxrGAKlCIeff1yZH4iswS9gT6jkOdRQjnea_bOwMrJ6MvCJhpNnzkkQ1LN2F8VK2NWbqJggPM9rn1NiuoZ2g58XL31ctGnr43WYGAHlvaTpBjT9xYGbQvIBPEIEnkQ1nteSUQDVHOB5Zp6PuQx9-v2rhRZtt5twuve-2z-nZIMGb-9g7RAVtzSfsZC9qi4oqQp352-5DPTVrk8_10mUpLQ06Y7rL06PDUze-plxiymvCbIgk9Pq0eJ6SVSoIsvV3T_gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸۰ درصد مردم ایران خواهان دریافت عوارض از تنگه هرمز هستند
🔹
نتایج جدیدترین نظرسنجی انجام شده توسط یک مرکز افکارسنجی معتبر، ۸۰ درصد مردم ایران معتقدند که حتی به قیمت طولانی‌شدن جنگ، ایران نباید از دریافت عوارض در تنگه هرمز چشم‌پوشی کند.
🔹
این افکار سنجی ابتدای اردیبهشت ماه و به صورت کشوری با جامعه آماری ۱۲۰۰ نفر کشوری انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/akhbarefori/653791" target="_blank">📅 09:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653790">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7c8027743.mp4?token=Di6EHsbd7Jcx1lTtBhHwVZ_mTjKtDNIte84ZrQ3B3hDOh5Tm9XctiI1fn3QPy7XCyJyUh-iGlfCS50cKtz6WxHrpShykgV7u1zQmsTfmX7hsytCu801ylkCT51vdkean45HoruexXF8q8bRsvUwO7UdqfhOJW7y_gWCtHfvZgwIkkQDMm07olYmRPo05ZRCwuf1Vz8w9m-DCDw4Mf_8UvjdbI3MYqJOODNkROOPblzZEKK4V1IS4gOBkTZanA_xf__fBDmp0fX26kLZWI7ZEmmPlu5gznUkUtPbsD6Uk-opP5nJA8Y80wK-EQN7INFLTgB6UF3i57Vr3TC0pfNrt1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7c8027743.mp4?token=Di6EHsbd7Jcx1lTtBhHwVZ_mTjKtDNIte84ZrQ3B3hDOh5Tm9XctiI1fn3QPy7XCyJyUh-iGlfCS50cKtz6WxHrpShykgV7u1zQmsTfmX7hsytCu801ylkCT51vdkean45HoruexXF8q8bRsvUwO7UdqfhOJW7y_gWCtHfvZgwIkkQDMm07olYmRPo05ZRCwuf1Vz8w9m-DCDw4Mf_8UvjdbI3MYqJOODNkROOPblzZEKK4V1IS4gOBkTZanA_xf__fBDmp0fX26kLZWI7ZEmmPlu5gznUkUtPbsD6Uk-opP5nJA8Y80wK-EQN7INFLTgB6UF3i57Vr3TC0pfNrt1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو حاوی تصاویر دلخراش
🔹
حمله شهرک‌نشینان صهیونیست به زمین یک مرد فلسطینی در جنوب الخلیل در کرانه باختری رود اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/akhbarefori/653790" target="_blank">📅 09:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653789">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-Ua9TtF3KqGDKqLVNk5BfGcWadKgRg6O9qPyZxDftRW3BRW5PzBH75Oq5665FVZAZXbwhXGjSyt0teV0FEwgUHRBBfNdCw6ztsA5Fb6JUvvrMYgXbZfAOD5NHj53MVJzv2rLJ5pqdsGXSHsvRyHdgTuRdoOkI65z9mm31nQEpHq4DQXfJp9spWbmWho4sYsowQTPYRUluz375xWqxn8YUDJSO1ww58HjYL9jjv__KmDrMm9o5AoX2DZ9WzkTcMTlXzVeib1jzKXcdGiKAmnZvux055JSlTtBOACh_C3Qv_xuqlbeT17NW31wsM3z1fmlVPHRMB6MPBocn4h6_Yn8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸۰ درصد مردم ایران خواهان دریافت عوارض از تنگه هرمز هستند
🔹
نتایج جدیدترین نظرسنجی انجام شده توسط یک مرکز افکارسنجی معتبر، ۸۰ درصد مردم ایران معتقدند که حتی به قیمت طولانی‌شدن جنگ، ایران نباید از دریافت عوارض در تنگه هرمز چشم‌پوشی کند.
🔹
این افکار سنجی ابتدای اردیبهشت ماه و به صورت کشوری با جامعه آماری ۱۲۰۰ نفر کشوری انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/653789" target="_blank">📅 09:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653788">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d739060b7.mp4?token=aJ_4YEmv1QyHhjPtgxJwrn4n9JUSABuEI6t8a5HK1TqeGurcqNbyhRxP4_xC9HHg_sqSWaczM3It2Kxs4eI2w5gBpBumsiVw6K81M9GYoUV_it3MTKawkAIyRIb71at4hDwIQUBd95VM_gJ0-Yl4s0sVWmftNwFKONpGxnIHBkI3Z68_tHBv2S9PzykFqZHuhupmhigh_HkjrqCOFWnX0WeTn-plpz-WpnPP1w0Fly7YxePI5tMF_UFgC9fsUN_3XdVlcbJl16hnXUwh0Suo3NzqLmzlnaUqdk2IharRuB-QnfeBLUALRnjT3BD74kWL7X0vlk7Aa12UoOB9o290qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d739060b7.mp4?token=aJ_4YEmv1QyHhjPtgxJwrn4n9JUSABuEI6t8a5HK1TqeGurcqNbyhRxP4_xC9HHg_sqSWaczM3It2Kxs4eI2w5gBpBumsiVw6K81M9GYoUV_it3MTKawkAIyRIb71at4hDwIQUBd95VM_gJ0-Yl4s0sVWmftNwFKONpGxnIHBkI3Z68_tHBv2S9PzykFqZHuhupmhigh_HkjrqCOFWnX0WeTn-plpz-WpnPP1w0Fly7YxePI5tMF_UFgC9fsUN_3XdVlcbJl16hnXUwh0Suo3NzqLmzlnaUqdk2IharRuB-QnfeBLUALRnjT3BD74kWL7X0vlk7Aa12UoOB9o290qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صالحی امیری وزیر گردشگری: دشمن با همکاری سرویس‌های امنیتی و ژنرال‌های نظامی قصد داشت یک عملیات سری و بزرگ را در ایران انجام دهد و پیروزی اعلام کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/akhbarefori/653788" target="_blank">📅 09:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653787">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmE6nujnqJCb_WkLqfF0xGzK-233Hk6SqbNBUzp0Y2fIGdQsRvpmI4ekSM3ESVPsb_zdMKpeXLMOGSVoRrDh0SIZmhThPTZmkzkCDIu8Bp4wDfFv2B_cHUt509amVdLa6RZnJtD06tdP5GIiUlGnAIshr8GPqWhWzMNPeEgbT0wUNsYOfzNwkVd8qznvTDtWXeWi6QRaf8gl3wGR52UGtA6CNyUx2SV3WD-C1Zxs5klf46TWF5n0qmmF9MJy_7_eUsa-K4vDfwfYhUHEOwaVFmIuRHUcW_lxQrCEzteG5O5Bms-YQJYO2f2G8l_UJvpvuvtf0q9NsA8oaN0ZWhJ8jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خرمشهر، شهر خون و قیام آزاد شد
🔹
خرمشهر در عملیات بیت المقدس در سال ۱۳۶۱ پس از ۵۷۸ روز اشغال به دست رژیم بعث عراق به همت رزمندگان اسلام آزاد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/akhbarefori/653787" target="_blank">📅 09:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653786">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJb0nWd-70cV9Pv0lhDSyBCtwPLtFfaspgkA-X34q1MH2SzrZc2QaJkk-JpgG3iA7qoj1drwPfOdyDp8U2qPxiY15cDK-Md7JZdS8oG_JOckKIs6BOC-yzFi7Ic2mFv-64gHM8R4YzMEnselZ3MjBmgjqgK5nBBZlLf1FCIz5DrCZgd-K1OyxtEsJCaA-4B19xZNf-T7dpTXa5N3oriuJNz2iAodqCaPyMIVB527AL9yz-D4orAOfUoEQdb9gEgK6fFuLMZMliOg2grdne1j1AK2nMBUKgggDqallzdiiBc6aecp4E5JYngo_ZQ-XNWpmcxzFwLsHqQvvtms1eK9eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقام دولت اوباما: جنگ آمریکا ایران را مسئول کنترل تنگه هرمز کرد
🔹
یک مقام پیشین دولت آمریکا با انتقاد از سیاست های دولت کنونی این کشور، اعلام کرد جنگ علیه ایران موجب شد سپاه پاسداران انقلاب اسلامی کنترل تنگه هرمز را به دست بگیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/akhbarefori/653786" target="_blank">📅 09:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653785">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EN7fcv7HgsREfSrqv2jm-XbgicjnhYZAoAG0VkD0JbE5UsJ2TG8fqwiOPmR6lQF5nA5B_RM5HL_ZbrGosm2m_70nzae19V4YIBfwCs5GJfhnpVUYywTDKTD8Kr-LxarGSWb6wdUJHuZwTnDdVyaYYj1rMfnvSvCXl_yZ6KlxumE3qCM46EaYmhSqSKHkkXy9iMQhPKWzORoWlj8qW9hTnPBoHD5cEWNTHfKWhAStaCr3DHBpXodJmzAKq6uNiWTDxMIW2pfR_0ztI4-fSQHwGgBxn8Jfu4end5LC5nsb3aKGEzXmr0Xzo1OGYPMjF2Bdca9-mv4m_CRzOpxAqbO8ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توافق خیلی دور، خیلی نزدیک/ تب‌وتاب دیپلماسی برای مهار بحران منطقه
🔹
در حالی که خاورمیانه یکی از حساس‌ترین مقاطع ژئوپلیتیک سال‌های اخیر را پشت سر می‌گذارد، همزمانی تحرکات فشرده دیپلماتیک با آرایش کم‌سابقه نظامی در منطقه، نشان می‌دهد پرونده تنش میان ایران و آمریکا وارد مرحله‌ای تعیین‌کننده شده است؛ مرحله‌ای که در آن، «توافق» و «تقابل» تنها به اندازه یک خطای محاسباتی از یکدیگر فاصله دارند.
🔹
واقعیت آن است که تحولات جاری را دیگر نمی‌توان صرفاً در قالب «مذاکرات هسته‌ای» یا «تنش نظامی» تحلیل کرد. آنچه امروز در جریان است، یک معادله چندلایه امنیتی، سیاسی و اجتماعی است که سه ضلع اصلی آن را «میدان»، «دیپلماسی» و «افکار عمومی» تشکیل می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/akhbarefori/653785" target="_blank">📅 09:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653784">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWN08UMx3pNG3noDryPk7AD8ykvvfmE52zy1pUtOF6rmq77YTcfQkR-TaLD8F275hZ_5NV1vGn_0PIT6U57SWcoZYEvGxx9lscffMxVUHMZk2oAXfF70tYNkspaYn_EjPVxUjOBFiOveQ2ZVuarX0afuuAzy-CVrZ82DSCttg792GPwbGnJbJJs8FJOIJD1L1G5O2AFYQAXgmZi9GZIG3b_tG0Q_Cx4UxJeR3lXz_MqJOrsMO55JdLG82oo7SAuCJ8TD1L1WXz2JglzZkf5IsahjrREFE9OktijO4a4Jnqv7j16OPOSunEqc9WvWtsx5ciPB_70gDUGVwzbSx4M-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام مشاور رهبر انقلاب به‌مناسبت سالروز آزادسازی خرمشهر و تناسب این اتفاق بزرگ با رخدادهای اخیر ایران و جهان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/akhbarefori/653784" target="_blank">📅 09:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653774">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f7ytKMJb3eSO0NdaW-t8dCTvG8rnCZdIaPZ-HXu4gVo9r-VY8NVpaiBgXrsi5xecUyxgEnaEWnKHwX62ILBCpMXnBeD2qhsAgYeYYb7B65GMXgrTF3sJO_LHosYC8ll4urU3WDAa3LDPSi6yXfE7q5JfmT_dkxKcjQDz2jwEjss8ohM1Y73G82P_8ox0zcQmqPGORtNSs85o-iOaUXnEfTYnkM3QMzfyQ7Zli2edrPHPRy6nDaCXOoxajBBawuoHj3L_s6haqPG1P9P-rg8F9pt_hms_zdyjwE-LA3OdT7eGBQQjdUJgeonrwp7N7uu9uO67pb6lXdaTPUs4N3Lyvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pO-XKrKUe3uDpQZRUiDL8SbjL6XBBQhkLG6MC5EMyds4TR-7Es80sYHrULHycOE66aZMy0q2aokPA0xBJF6Nq3aXhJIwje8kcStxX6v1rMl2WfEc90JqeeBS1P9Mjl9MeR3__3Gzu4I11WELEYomeH_FYMe6tXJ4rYpETp9lYGmOpMfOSCUmHdlCKHMVZ-N0CJhdPcqgzEbGLXG8JyqfB3fC6VT77Mw2TFzMegiIKIUUpzYNaJXhy6UVp13dWx8vI3kgSx2PiOwJPZJWPdwdKnOeotY1LN1p06crTTJc_ehCom9HzpDCxp5b233POGvNf48ee3m2A7Zhcw2eKwhlNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQE8yBXqsY2zUc9reqaO3lnFt6WYbLBwpzmkmWpcj8mKqNoLraxdbuCuoXdaDGHDwZX1gcSuLoBystXsn_8y94IxoZlqtZPBFZLPbhpTVSzXKl_Lm9vdW26DbHcMlx6hoCCvfstpbYKOK_rJdJ5QBOlIvWMp-7gOzl0n28u7BsTf1hZK6NMo8k9MISuM_mulkFytddvd49wqOi5iMkx7bRzBBS4hZQa61OTsSVh3LWuTlqcdHGSLlafCsNuQEjv1pUy26EM66N5KMphqoGx8PQEjYZ_MSKNp02DD__R6roRgoWiIDHuSsUD6ReL4Q4nteY8VmXO5dpsXqH3AFkUDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a1HdOCgl6HjQiUwbrKJbH8Zmf7YLUT6sEr8pIB1i8Sv_fLhKatDwKXOaThW9EPATzsrEyi-1wtxBOFZZFWvbtEZbI554dwYvTCoUidReKCKf-ikbftRjLGOkPnoHV42l4suxTcQuPSDsNmzSw65UgHoaVwjNAu9S6_M7OnIC-Z8Nc1k6nclJWaWTldZLrp2ceJ1d_g-RQC9CVkCKsSYdGgFlaKZUkU6rOPvxrK2oiT8NTUold8t0WOI-rJLJAlNP-iRTzlCIbPND_byyWQ2Gbxs501KgompuBYSo8qzUKFMiACOTdZbOXkhoQU-4nsxBo1cYkM59RjWZWhdAhEnTVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hoTbEbIrt47QXz3fiZmVPIRrXAJlX5ik3StbIM8Pes9xEjGIjJSN6D3HRuOfWSQ_idYUuHez0t6n6D4VutBcdfnKOgcQ5sTdgf8t8tm4mtPkvFUR1N1Yr_dBdY0UAgFourv0VXVrfeis0qAF9Y7PEHwLB_wfOMgf1z5P9kHIvU7_Xpzh0zcUitu8WT5e9ujZ8Xo6YTS8wNd5qiYuCDGN0tftrXbu5toZdeaP0-SvLNGmt-m2oV1scimpJCAXIsson1eB7X_Qzx8rBehr7iaAtpxjyok9oeuYpaBui_MCWF6BxRRrbfS2auW33XiyUCXRk8K7IaGkcOuMPckq2TNhAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WD-IwrVZkpIcnxDJYDYCbHpI9to5C2XBP7lC4hrLyE0_6Q16qfy6Mm_jezAk9_OYMFxIl_XgYZMaZ6jlsf00LYnAXc5cG27afs9ceijNfrmw1hWQZGaufq5NA-ylJHswyEGQ3mluJXj39JPHgnT_7oTSwlQU2IOTcLdnThS14hADeQ5hMUZoS49Mcs4sR9ffzGZ9u8FzmZT6QxeFv_ntvCJZ_RZhNhr2az60rGnrCZ19bC9DopKlbTvFzhykEAnTRd_Qx_m-iMOMG0O0JX0FdZnYBcpwNlAmRqkMQwPKJBKZXnZbTRlEJFtlVSvKYhGXLFzLKJdrStKjLBZv9pRqNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TBmAco8K7548rf2bTq7e3SZZwAXAVfaLmA-Gn-_uNgFcX4vMh_Op3hG1IeT4A1FU_z3ob8-hLvUI8vHl-GFFvsdJgAgAwvgyZCf3SQA9oxXsKSizKlg8mJ38pVMiJsNUHg7x9iQOkCl4J3IoNzjO5XyEEKPuCZC0GrENzQ4PkMWC9Fjpu0w5z5WskoD2clsHAE_EA2-IEAeCtPSUu-rJbhKv-m0iFC0apDLSLdLA0--Q4hFTxZbsPuEHvQpYWyv4IKlBqcUdwpAoAD7qUGqyjG6PTdvhoj0a963ojLXv5hRcqGq0zDZgvRH2pyH4n2KJV9cbNiEUehHXiQITHi1zqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WAg943c5wnLQ5mPOhA27OiLa_pU6HXyjxH_zT-XlSDJvAu1H-O2N5yIQki4JUV5kH-pWiKuTZcpReEsnYPw5iUvCbGFt8SccJFfpcyBW6CDX5LXkddGjEvfufI14pl38125lazx7LNqJZekSMP6S3W3PXKVxDL8N6NuzlKQNaRV4-q9ayA4YZWjiBTYwXZHM-wLvxyr4aRGrk1rURuxi7i_kp8nUzIk8tunGXVVJu2mlW14pPpAdXTGpNKFDSWU_kiqSW50zIzmjSz3wJP3eGCDJaWWudr_-eR93AF2VewbNlS9S8EHwKce44M3VuW_zqhv8fEw320-lBL2OY6xsvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YY20fxHyfVxQZ0sa-DLnegiIgxCMpb9HAcQtoKtCjAAXOIwoB13KiCcEPOzPOrjcNO2O2vsnnkRTkD-nUpN4OUQ1qDSG0mw28WK6B74v60PirHxs44-J4ysiROmxGcmrAHAnDCtl3IHXDfq6xy6OovpChyU2HKLqnzs-vmUDqsL2YaUcYQ8rxhAycHdp5_KYGM_Em3Dcd5fxN-Xep7tZTRBV2VaEXPfR0RVD3FCgXKE9oUAEpHJxgwyC8LVinklO0jW6_u1LwtiQnoyCCAdjuqexGIPBEUIPiZ0aKFfoXtBviOf6zfqcpS6Iw6R9-lbMQXcV4Cobw4dRj4tSDsFmDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VzfPdWV4azRHajQCLenaSl3PwOwjvRX77E85_hpyi_oqkXqeTRJ7ILczScGfCKifkSJBKdm2l9wVa2LfZ-GQk_xFmkmHNXiWDyrcMJKa2dSShwOhZi3WaMlbBuFIAK2_z92mzc52SZYAbWFssgb5hluCZdRU9AhyDEdMm51ao6zdANX9ubfyRp_D7q_SL51fNEOY8UYwoB5LVYhTGeC1NM6K-LKQ90Bf7jkbRmDcK4X7id6Uq5LUKM0XylpAW9lPDj7jvgWmztZZpH7MZyQ-MMg_Z6b3X2gqbfJ2McI1RBGr63EJaDLc3q8CrgRfhrsc5SbDyMUph2Xsomo9OyDHTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از عملیات آزادسازی خرمشهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/akhbarefori/653774" target="_blank">📅 08:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653773">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQTNfNLFZ5QmeAndWYfsEh-HOXxy-XEkmFCA5SR4fFACB1mkBlIhmrnH1CY2B--ogTNp_VuCxUITxxFLz0RbRUkSTicq1YvmAJ02T-GYR_0MUb5lLrps9GKEUV8Rsvdg_TXZZCjDX8xawt6QBzkOxbW-bpyKaXfUtv5HXr-Z4CyG1CuyCCXysPkDZNFARGriSFckftXgGpulHRW7EScYoib_r3qzSV4Pe9NZgmIPQ5EE3Hq2GalXP5vBIfcIdrg-O5TC7e6180Hzq2JmnJ9oV51RKQR6ImT_-lFiWjkyvCUFZ4dbXoKqcupiZOOY77BDvAe7MgZ6HZ1wTRpXmkf-8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام مشاور و دستیار مقام معظم رهبری به مناسبت سالروز آزادسازی خرمشهر و تناسب این اتفاق بزرگ با رخدادهای اخیر ایران و جهان
🔹
دکتر محمد مخبر در صفحه شخصی خود در فضای مجازی نوشت: صدام و ترامپ هر دو یک خطای راهبردی مرتکب شدند: "نشناختن قدرت ملت ایران". اولی در خاکریزهای خرمشهر مدفون شد و دومی در باتلاق ساخته رژیم صهیونی به بحران سیاسی دچار شده است.
🔹
سوم خرداد به نظام سلطه یادآوری می‌کند که سرنوشت قمار تقابل با جمهوری اسلامی، شکست همه جانبه و تمدنی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/akhbarefori/653773" target="_blank">📅 08:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653772">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOXLxtH0uf8VUyp8jWtFdV6N3IVVp5dpu4fSYdCjKvCq7IpThCoYYZ5AYS679dPz4lZGcrZLb4lAXm-be515NYQlgoT_AcCRWvncFETY7Kx3nUdliPamST5tImZabk74stG5X3uedeoDG3mxnULNhjC4kheBnrL_5p7alY24AI6jQez5nfiZAxbGqzNI27HpDNHVZaFtby6t8IUfiM9xmCZS8T74vHrZTU5LE0dJ3vEWSuu2cN5eYl8n6xPrAspmNxxLnBtB3caAd1jfMqXGLsyzoWBGBSdUqszTSiDpGbdQU6O2krxBCgdpaVoN6CPa4IHP94zoTa93b8vpu6WkDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ ایران، کاتالیزوری که بحران پنهان واشنگتن را لو داد
🔹
استعفای مدیر اطلاعات ملی، برکناری رئیس ستاد ارتش و دو دستگی روزافزون در حزب جمهوری‌خواه آمریکا، همگی نشانه‌ای از یک واقعیت تلخ برای کاخ سفید است: جنگ با ایران به کاتالیزوری تبدیل شده که لایه‌های پنهان بحران نظام سیاسی آمریکا را برملا کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/akhbarefori/653772" target="_blank">📅 08:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653771">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
شبکه تروریستی در فارس متلاشی شد
🔹
روابط عمومی اداره کل اطلاعات فارس: یک شبکه آموزش دیده متشکل از عناصر آشوبگر و تروریستی در این استان شناسایی و متلاشی شد.
🔹
در این عملیات ۱۵ نفر از اعضای این شبکه آموزش دیده که در اغتشاشات گذشته نیز فعال بودند بازداشت شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/akhbarefori/653771" target="_blank">📅 08:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653770">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO7UUCy7Fu66gBmppUnNNtUoIOVrLAStEor42F5ZTNouRkKKIDfgdCshDpE6c527ZhRuhsKM9g5YDoqshYqb4Qa1vgeE0GoGG_3SJRt5ugN1QdmCpOgb5Xhg17iEP1Pvu0e5EDuiIFHgbpuWYgFjtjR5U03XL2ewXNB_AEum5R18xwKwkNsWTMScixFHXB1peoJ_vXJy6sLlJeclRK6rWK5QviI7zyJ_wygdi7pJHor-Oha08s55Qtimnjw1ShklEFatIdHwrePievnaYGb1mYAg6nAfIVv29vQh9YEyeXwK9mrXdChuRxqdS9hGCCwZ4Wz468BZr2n7Yf7r1dgD4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دو نظامی دیگر اسرائیل در لبنان زخمی شدند
🔹
با گذشت ساعاتی پس از اذعان ارتش اسرائیل به هلاکت یک نظامی خود در لبنان، حالا امروز این رژیم از زخمی شدن دو نظامی دیگر خود خبر داد.
🔹
ارتش رژیم صهیونیستی صبح امروز یکشنبه اعلام کرد که دو نظامی این رژیم در جنوب لبنان پس از انفجار یک پهپاد در نزدیکی محل استقرارشان زخمی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/653770" target="_blank">📅 08:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653769">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRHQ4C2_tvYSQN9e3h9ybiOJGkTM-sC81l3Na9ORXwp9ohjq8dkyKjsP0KgDGsaEt8F_mu_i2RUyOgCMsfVmv5Q1MGSaOwxJx9nfxVR84fBnvGMlckqdjJrGjiVKFqAwDROWSAUxp1FkAIPev9Hhw__0CkVcWifFqSzuUGwUljoBiQnnUSjetGhncp2uuUmRKFLr68qJ8q_RePgg751K_EgaW966ywBNbBMMECrkfEslbQzRbgo9eM0jApBx1HA0UwEqFRbSY_DKUZnJqLa8lFvftavBLqPSGEK2yob2RGuwtrBHI3Lriy0TnX2fgJLlj9r-cNF-iZhVflpIiCRnew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تتر ۱۷۰ هزار تومان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/akhbarefori/653769" target="_blank">📅 07:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653768">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rg5XRI5xIAqAFaTn_PMII8uXOXoGGQ467ivL4X0Pvh2qkCPXuItmzRF-1nF3qjs64GbyTyyMhyVSDk4d25abFlW98msj1v5UJO1YOb4jtRxobOZHGPIVIX2HPbC_8ZsTSHu_7Z3AQOK7NMlSKTpUz2Zc5UQLFdFw4102yEakC3THnw5oerKkQIv-DTZl41l_RMFqvRgcbPWMAPLqE2ppXwSjgzJ5TMDz6EzaNd6qBqSI6kM8zqI75aRliTPth4Dm4UNP-n7BDRTnFIhsFJHHQfb6YvEBLG2bzFm85wVhOYPrPv6LsHsKZfSKyaroc7Q7xg1fgP35OlktqZPu4JoE-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عارف: با همان ایستادگی حماسۀ خرمشهر، دربرابر دشمنان پیروز می‌شویم
🔹
معاون اول رئیس‌جمهور: حماسۀ آزادی خرمشهر آموخت با مقاومت و اتکا به توان داخلی می‌توان از بحران‌ها عبور کرد.
🔹
امروز نیز در میدان دیپلماسی، دفاع و سازندگی، با همان ایستادگی مقتدرانه و تبعیت از فرامین رهبری دشمنان را به تسلیم در برابر ارادۀ ملت وادار کرده، تحریم‌ها را شکسته و بر دشمنان وحشی خود پیروز می‌شویم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/akhbarefori/653768" target="_blank">📅 07:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653767">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9HzqV7rdmXx3zmr0AdvTV04Mg-vHnKKd4aR5de8a6HJzKLBc4NvavOj2cW6LcdLw711lyVHJ9tYu2yVh7ZS72e31Ad1YWjDNWmE4dxu1h6HHUv99aW0Ia5q6_PqVXGH8rl3_-1wrk7ERacEZQO6HbGwludBN1XR24j2JvwWswDDZ0gFCufIzh8MtCCJeJ_dwAEfQpSuZ6qIH_r25wGYqOv3m9nku8oFHwjazSP-5eyHou-3YnW0GUCe0z101HIxX2412s1g3O-gFvJ4DFZwYseElJlauBwHy7ti65iuVYgUjKSSfwbQPq85ZP_6huOtn6Fg8N762Y6Cqi3g2_1WtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عامل ارسال اطلاعات مراکز تولید صنایع دفاعی به دشمن آمریکایی ـ صهیونی در جنگ رمضان به دار مجازات آویخته شد
🔹
مجتبی کیان، از عناصر همکار دشمن که در طول جنگ رمضان اقدام به ارسال اطلاعات مرتبط با واحدهای صنایع دفاعی کشور به دشمن می‌کرد، پس از تشکیل پرونده و رسیدگی قضایی در دادگستری استان البرز، بامداد امروز پس از تأیید حکم از سوی دیوان عالی کشور و طی روال قانونی، به دار مجازات آویخته شد.
🔹
طبق تحقیقات انجام‌شده، نامبرده در طول جنگ رمضان پیام‌های متعددی را به شبکه‌های معاند وابسته به دشمن صهیونیستی ـ آمریکایی ارسال می‌کرد که از جمله آن‌ها، مختصات و اطلاعات محل واحدهای تولید قطعات مرتبط با صنایع دفاعی کشور بود.
🔹
محکوم‌علیه در شرایط جنگی، در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/akhbarefori/653767" target="_blank">📅 07:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653766">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">قسمت بیست‌و‌چهارم - پادکست کافئین</div>
  <div class="tg-doc-extra">بی بی مریم بختیاری</div>
</div>
<a href="https://t.me/akhbarefori/653766" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
#پادکست_کافئین
🎧
▶️
بی‌بی مریم بختیاری
🗓
وقتی شرایط ایده‌آل نیست و قدرتی نداریم، چطور تله‌ی فلج‌کننده‌ی «انتظار برای حُکم و سِمت» را بشکنیم و در لحظه‌ی بحران، بدون کسب اجازه، رهبریِ میدان را به دست بگیریم؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/653766" target="_blank">📅 07:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653765">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8964485f3d.mp4?token=ao5abePbh0qZkBOd8onXI1UVhZxz8ytGu_BH1pJNgScYUmWtXo9r68ZyIOMOznx1WyE84PaOgszREANONhCkj-QzQ4gG84Ox76VnATs0AAAjzAw0x9pcdMi9NonSUlSe-iPvTDbDfq1SQj9Y_oBjzEbLfrFbeE1PzO7GCXCBh53uPhw9YlkcbdACtWGsw4moovLAKlgIDdlVRnsS6uPpXqq3u-7rz66e0glws4pBTOsS9zFzBIFZqyz76m8E-kvmAw-HZmH-5h4PQoeg3o8o_5Es_oHnZT05N4W1k51rHkPdvImzCWtdIJtaMel9yVIDrKJqNFLy9k84BxYzE2BErK4RXKs6CiGUddaKU1WnjjM5MQv--S4S7V4p_TjHCPCmnc-aQO4CZOZm6_ybWvuRgBTW5PP4-cpz5AE6xk2E1ukyuoaxH52Nmgo9gIKL9TaIH5rGTGpt8yBa0bdj5rvasEo7UnHJajLC2bvlruc1ggBIIM9_yXcod896nyCmb4a0OFbbCw4wS5arq_i5WQqoSFkA7fB7la9D7F5qo78YvK7b3I8ng7ayoVAHTTepjpNJ_chWtRs_P3Kd_5AF4xHfiaKsYb6qxNXTtVvd1mMbcCmmXYk2yJj42vAQwtj5Y4FTmvFvAKtPk4LHpl6YjZMN_gk78YgzaN35ULI0zHwqiOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8964485f3d.mp4?token=ao5abePbh0qZkBOd8onXI1UVhZxz8ytGu_BH1pJNgScYUmWtXo9r68ZyIOMOznx1WyE84PaOgszREANONhCkj-QzQ4gG84Ox76VnATs0AAAjzAw0x9pcdMi9NonSUlSe-iPvTDbDfq1SQj9Y_oBjzEbLfrFbeE1PzO7GCXCBh53uPhw9YlkcbdACtWGsw4moovLAKlgIDdlVRnsS6uPpXqq3u-7rz66e0glws4pBTOsS9zFzBIFZqyz76m8E-kvmAw-HZmH-5h4PQoeg3o8o_5Es_oHnZT05N4W1k51rHkPdvImzCWtdIJtaMel9yVIDrKJqNFLy9k84BxYzE2BErK4RXKs6CiGUddaKU1WnjjM5MQv--S4S7V4p_TjHCPCmnc-aQO4CZOZm6_ybWvuRgBTW5PP4-cpz5AE6xk2E1ukyuoaxH52Nmgo9gIKL9TaIH5rGTGpt8yBa0bdj5rvasEo7UnHJajLC2bvlruc1ggBIIM9_yXcod896nyCmb4a0OFbbCw4wS5arq_i5WQqoSFkA7fB7la9D7F5qo78YvK7b3I8ng7ayoVAHTTepjpNJ_chWtRs_P3Kd_5AF4xHfiaKsYb6qxNXTtVvd1mMbcCmmXYk2yJj42vAQwtj5Y4FTmvFvAKtPk4LHpl6YjZMN_gk78YgzaN35ULI0zHwqiOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی‌بی مریم بختیاری، سردارِ خط‌شکنِ مشروطه
​
#پادکست_کافئین
| قسمت بیست‌و‌چهارم
☕️
​در این اپیزود به سراغِ زنی رفتیم که در اوج خفقانِ استبداد صغیر و جامعه‌ای مردسالار، منتظرِ هیچ حُکم و اجازه‌ای نماند. بی‌بی مریم مخفیانه وارد تهران شد، رهبریِ یک جنگِ چریکی و شهری را به دست گرفت و شیرازه‌ی ارتش استبداد را یک‌تنه از هم پاشید.
​
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
​از اینجا ببینید و بشنوید
👇
https://youtube.com/@caffeinepodcast2025?si=pSS41rtTzorAVCrI
​
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/akhbarefori/653765" target="_blank">📅 07:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653764">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQMxNYrRXNGim73sfJoeNHu6M6fjcmgQ4rb-9DpSr0Ydu5ZmBgQulelLcOQ9IxsfS_kTE_uPXqG5abP6rdKQng5RI2sJNcgVVEMCiJgBjj29ScAib2CBvxNUiyhbbCVfYQ-VnFKzEhtQR8wRo0boi4avzggkJNJsK40rnjLPNUSwA3orFPha2WBcGc4lo0ZcXb15NwwjltbtsW7MxJvOFORE-8xmsUynwpK8uuCBPvi73TeHfmr1l-76OkBEe9mLyaeEoG8q_NjbX_VCI6VRd0kcb-mobQX_3dkQat4DDT08xk9PJOLsaaCCbgVZf79nXUdQx0ocnfaiEMw39FjyXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران با دور زدن آمریکا سوژۀ اول جام‌جهانی شد
🔹
بعد از اعلام مهدی تاج برای انتقال کمپ تیم‌ملی ایران از آمریکا به مکزیک با موافقت فیفا، این خبر امروز در رسانه‌های معتبر جهان به سوژۀ اول جام‌جهانی و بمب خبری تبدیل شد.
🔹
این اقدام ایران را دور زدن مشکلات عدم صدور آمریکا توصیف کرد و نوشت: ایران با انتقال کمپ خود به مکزیک مشکلات عدم صدور ویزا و تعلل دولت آمریکا ٢٠ روز به آغاز جام‌جهانی را خنثی کرد تا راهی مکزیک شود و تنها در بازی‌ها در آمریکا باشد.
🔹
نوشت: ایران با موافقت فیفا کمپ خود را از آمریکا به مکزیک منتقل کرد تا با کمترین مشکل تمریناتش را انجام دهند و در آخرین روزها با دریافت ویزا در جام جهانی شرکت کند.
🔹
این اقدام فدراسیون ایران را نوعی ترفند برای به حداقل رساندن کارشکنی آمریکا در زمینۀ عدم صدور ویزا توصیف کرد و نوشت: ایران با انتقال کمپ خود با مکزیک مشکلات عدم صدور ویزا و بلاتکلیفی را حل کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/akhbarefori/653764" target="_blank">📅 07:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653763">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
روایت جالب توجه یک پزشک عرب از علت بمباران شرکت‌های داروسازی ایران در جنگ
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/akhbarefori/653763" target="_blank">📅 07:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653762">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpOeP8lHDi3iCDzSlLwm-5z3nSh_IWKNoRjQHqUT6j5MJ29AVVzV-tGsd-UEF6bmHINJWkxRKshsAw-ewRXotvHcRmZGQhtIu3QeUbQCDQHpwk-DldTbIwcvdaFht9aX1ua_p4eNg0p6ZlnFIuvHWCBoq3apIuxQ57ahe03--otKpyqLi71oEDiixd7W6XsdHFICUnWADGw7kQrS1eoy-wI9AndSDzG486JT7mjppw73QFX_tVzzogWA6ulDafDAx6PF8lnBcdYus13XRulC_XMjC0BM-la-rVnnlp7CYTOT4n9stEpwShXdKbSMlY7on2JcdD4VRx-OWM_mCd2-bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۳ خرداد ماه
۷ ذی‌الحجه ۱۴۴۷
۲۴ می ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/akhbarefori/653762" target="_blank">📅 07:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653761">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FO5LOrpMbpCskL1o1BT4Ps9YZBUIo9kqi8mLKoE-aKNdO5tF_xeURzGLgEXUGxNelep-ToS9sZw1HTF3Fy96jKcYzBXbs7uZXNTYTwXMYseFVMWZM_Gu3hj64JgLy21Zq9p5gTLth-J9TwB5tIbFsZxjZfVBLY4XDPBDb08D6-7TPsG-FODl9VG-FA7-agQbZKh2tLy6z5on5o0UeJ6yOa9Yg6GkK6oEPRbTWgESBkGCMYAlVoVfZ4Fgzj06n6Xaczh8Sevy2M2pBtejKscD-K4G6IyUdBGasm4o-KKVIrUeNo5vr3FsK2U9uyQE9Rv_EWs_GEXhJgh-j0WySNkxsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پروژه تازه واشنگتن برای خلع سلاح لایه به لایه لبنان
🔹
لبنان این روزها در کانون یک بازی پیچیده قدرت قرار دارد؛ بازی که آمریکا با سلاح تحریم آن را بازطراحی می‌کند. از افسران ارتش تا معاونان ارشد نبیه بری، همه در تیررس واشنگتن هستند. اما هدف نهایی از این پروژه امنیتی-سیاسی تازه واشنگتن چیست؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/akhbarefori/653761" target="_blank">📅 06:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653760">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xje4of36H26mnXzGSJKP9MrW1ge0_fD1D4Yg0cZBF39rRZ7xtvGsevWGrwFTWfdupdT9QmMQOA7QnnsL2SDZz2n4N7s_KEFssI0zumZtq_ofRX0mpFhoh8qWSaTTc4-8cL69rfs52coIqQTgvRuNCga_4Uz9826GvUa82GjADQNyjiWDH9RkIEINF93ALmxqOhIdIf7XTN9YzaXUpzx7KlPWqCA4nKFe6XT8QrywKDpLb3tINmIg_ybjjI01kdmSy9OSrPOZqdXlnGKjbY_6WT78yG3f9f4kPePdp2Tn-2jSpeUMrNqiqGYvjoaaFxYn2PLD1XeBclG7TppG_hkbNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون وزیر خارجه: ایران منطق صلح‌طلبی همراه با قدرت، دیپلماسی همراه با عزت، و دفاع قاطع از استقلال و حقوق مردم را دنبال می‌کند
🔹
غریب‌آبادی: ‏۳ خرداد، سالروز آزادسازی خرمشهر، یادآور حقیقتی ماندگار در تاریخ ایران است؛ حقیقتی که با اصول بنیادین منشور ملل متحد نیز پیوند دارد: ملتی که قربانی تجاوز و اشغال شود، از حق ذاتی دفاع مشروع برای صیانت از سرزمین، استقلال و کرامت خود برخوردار است.
🔹
خرمشهر نماد پیروزی اراده ملی بر تجاوزی بود که با محاسبات قدرت‌های حامی متجاوز آغاز شد، اما در برابر ایمان، ایستادگی و خوداتکایی ملت بزرگ ایران شکست خورد.
🔹
امروز نیز ایران همان منطق را دنبال می‌کند: صلح‌طلبی همراه با قدرت، دیپلماسی همراه با عزت، و دفاع قاطع از تمامیت ارضی، استقلال و حقوق مردم و کشور عزیزمان ایران.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/akhbarefori/653760" target="_blank">📅 06:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653759">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0sTnDhGANzAFFXBUU_pFEIUMwPEQEUulbTo2ywpAerXpJgDE-SDxqahIG93VJ9Nc54VYBu92P58fhOKZLlqqqc5jJiZTOm2V4Qot-vx39zW_Yh7gbDOiBiYwiyphzq_o3R3ZopjCSkG8Duh4rCbwYO_2yQeYcL8mcqACYqLxX5_tff914N9ISG2FadUwBnvjV3VtjwxmJWdLS7asqALpwrXmg1jCVnQUD4f8npp2L4YWGHhttCVr9spRvBIgaDHzOJJeMbC3eng9l_fvaWbpQ9730TVoo1Yh-eAMj-S-90jUOKMM4jYKPxrkEizCenw_Pt5Oaq4eEsgWibcMfV4Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سهم بیمۀ کارفرمایان، و محل حقوق بازنشستگان تغییر می‌کند؟
🔹
وزارت اقتصاد و وزارت کار به دنبال تصویب لایحه‌ای در دولت با عنوان «لایحۀ ایجاد نظام جدید تامین‌اجتماعی» هستند که بر اساس آن حق بیمۀ سهم کارفرما از ۲۳ درصد به ۷ درصد کاهش می‌یابد.
🔹
طبق این لایحه سهم حق بیمۀ‌پرداختی کارفرما و بیمه شده برابر و در مجموع ۱۴ درصد خواهد بود و ۱۶ درصد مابقی از محل درآمدهای مالیاتی تامین خواهد شد.
🔹
همچنین کلیۀ منابع حاصل در خزانه‌داری کل کشور جمع شده و حقوق بازنشستگان از خزانه‌داری پرداخت خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/akhbarefori/653759" target="_blank">📅 06:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653754">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
سی‌ان‌ان به نقل از سرویس مخفی کاخ سفید: مظنون حمله مسلحانه در نزدیکی کاخ سفید بر اثر جراحات وارده کشته شد
🔹
یک مقام مسئول آمریکایی مدعی شد: فرد مظنون از اختلالات روانی رنج می‌برد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/653754" target="_blank">📅 03:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653753">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sklOISk34FRkvHux_fOBFbLLiUxelS28xCj3rii1Zvf-nDyfVNwgnZBCHl9BZvPEAy86OcjkY6L43Hfr2XpJpAsR7QMPmTAYHCdTOXKveYYxSdlqjXes3yjpaorKfjQ74ydBBjwyxl0Zu4KegtYWMByEwfYC4RowkI5fYwVD6yALo7ur8qTo7ioh_mQtgAtZYIfI5odSNYG2QxxZRxOVhiUlYgTPyNWW1TskuhVZbMfFgoQYwz8PVf1nw-A3tNxf_gUWcIX3PKr3DZ2XXgEjOmg3fim_e9Pnya77SopP9bXwlkwUsJpjtYAyye1yeK-PAfW8pshu79tlOlC6adh1FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مایک پمپئو، وزیر خارجه ترامپ در دوره اول ریاست‌جمهوری و رئیس پیشین سازمان جاسوسی CIA در توییتی که واکنش به خبرهای مرتبط با توافق احتمالی برای پایان جنگ محسوب می‌شود، با ادبیات و ادعاهایی که شایسته شخصیت سطح پایین خودش است، نوشته: «این توافقی که درباره ایران روی میز گذاشته‌اند، انگار مستقیم از دفترچه راهنمای وندی شرمن، رابرت مالی و بن رودز بیرون آمده: به سپاه پول بده تا تسلیحات بسازد. این حتی ذره‌ای هم «اول آمریکا» نیست.»
🔹
پمپئو در پایان پستش، آرزو کرده که ترامپ دوباره به حمله نظامی متوسل شود و ناامیدانه و همراه با فحاشی، با اشاره به تنگه هرمز نوشته: موضوع خیلی ساده است: آن تنگه لعنتیِ را باز کنید. دست ایران را از پول کوتاه کنید. آن‌قدر از توانمندی‌های ایران را از بین ببرید که دیگر نتواند متحدان ما در منطقه را تهدید کند. خیلی دیر شده. [برای حمله دوباره به ایران] بزن بریم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/653753" target="_blank">📅 03:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653751">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
به گزارش فاکس نیوز یک رهگذر بی‌گناه در جریان تبادل آتش بین یک مرد مسلح و نیروهای امنیتی در نزدیکی کاخ سفید مورد اصابت گلوله قرار گرفته؛ وضعیت او نامشخص است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/653751" target="_blank">📅 02:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653750">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6JufmQLlPMYh7yMeT-g06uSlE2YpxCQkLGi26yh7paXn9Yp2IQDaLjoS8kT0UaOWFQBZsTpKAIj2Z4BIDZ4P5GsaaYGEvTXEwyg11tr02gL5rQPGRpEyE8_MSjbTWdOHOdM4GlM2jmNJ4-XTgx29mnIIRxdAg5PGJuWgdRj4ACBTsdpSpNjjhqVLl4LUffreyXy6MHNlMbZqqy8oTcjr5DqsyDMKwBAxPJp_WFIC0bcs5Mqu-_4e_ReUvkar_L_HaGrdvXSSYjQ6U7isOjNrds02nkvISTv57AkOPE0Sm7S2dsOUkyAqUuxluT2W0ONmmqcFiRstaFAga1K71bfAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هیچ یک از اهداف جنگ محقق نشد
🔹
رژیم سقوط نکرد.
🔹
رژیم انعطاف‌پذیری خود را ثابت کرد و می‌تواند به اعمال قدرت نظامی فراتر از مرزهای خود و در تمام کشورهای شورای همکاری خلیج فارس ادامه دهد.
🔹
برنامه هسته‌ای حذف نشد.
🔹
اورانیوم غنی‌شده در خاک ایران باقی مانده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/653750" target="_blank">📅 02:32 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

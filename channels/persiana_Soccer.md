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
<img src="https://cdn4.telesco.pe/file/VTowa2YT4JSguY_UEIRY_83e8fAdAX4v44whZpun5wcs48GhKwWLWs2bR9q8LeaudBMKFlZu2VYzVqQBR8MerMGe3dSWBkq9HWG4M7DZwdV7MB2cEC-v1ztGIbVOvlJmyotDyY3bIa8DuSxYBIhVU5nBcwI4J95X15JndBzyeFKT8G8tPdChe-qsLFfVSEsXGYScBA1j5ahRiVPQLyIIr06ZwXdM7qEi0U8a__krAFk7biDnTvFm85x12ZGXRnKFogl94AfbOkS2iC8udDRPk6v44yohFRESkqupz5n0axXtbhpITh62dsUHjhHXk3FoUWWcRA73383e3qL4KNvrjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 447K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 03:12:51</div>
<hr>

<div class="tg-post" id="msg-30450">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CS9-Pz7bqzOvju75GxKYXhJeXg_fg_PAcpvcwDEXz2-GrpmsfX4hXz8j9dGzlRYsi8lfxBuVSUKQGoNlJ5gEcqqFfIoWnHTT53Snv6-GwVCSPZwjiHPiXEq0gJonmYPFB8uQl-etZfDVBnvry6v1pH3FD3GGWRqM4Hvc6qivHv3-pIk4oF3KzpBAV0Z7NJmTT8MAd2qCM-3nruJRuRkGLFZNYthPgeJHD6N5BfU5I4iPDAt5HZLWfs6NJa52UeUqWce2CWY2giyuRU7ME553nct8DcijvzL2E4gf50VAoDXvipRu4WGORwQPP-VslnewmOswkwDSACrqz0essRwvHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
شوک‌جدیدفیفادی به مورینیو و رئالی‌ها؛ در فاصله یک ماه تا دیدار حساس با بارسا؛ کیلیان امباپه فوق‌ستاره رئال مادرید در دیدار امشب خروس ها از ناحیه‌کشاله‌ران مصدوم‌شد و زمین بازی رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/30450" target="_blank">📅 01:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30449">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34b91abd7e.mp4?token=XYCzFuGxjjkYcSL7rxD2MVCvyaICf11BfCgwcuV4PCgar_ew9LP8jMT7L91L4y3Jqn7_2vlHf-1WuF287HTEhF18OG6wNn11EfaCk_ZmAaJOb-XVGWdXgO35W2c1ZKRQT-4geA2QnbtSFJRG1hFORwlrvJ2-yRAVAV32rxc4-zl5triWY4sxQlRD90ifxCdqs5aAWFWzUbh-vaAOJQTH-3LwmlXYWF1FXXK0zV6_RnxHz15bVuvLJk5sh0TEG5lpWwADOeZEc5IieQgoo7X3mtsYa_7egLxzrWvvmT-JEzaoLt0IFuOnUbbUrqpFSiTiJUNOw9WweQgysxFdv67zWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34b91abd7e.mp4?token=XYCzFuGxjjkYcSL7rxD2MVCvyaICf11BfCgwcuV4PCgar_ew9LP8jMT7L91L4y3Jqn7_2vlHf-1WuF287HTEhF18OG6wNn11EfaCk_ZmAaJOb-XVGWdXgO35W2c1ZKRQT-4geA2QnbtSFJRG1hFORwlrvJ2-yRAVAV32rxc4-zl5triWY4sxQlRD90ifxCdqs5aAWFWzUbh-vaAOJQTH-3LwmlXYWF1FXXK0zV6_RnxHz15bVuvLJk5sh0TEG5lpWwADOeZEc5IieQgoo7X3mtsYa_7egLxzrWvvmT-JEzaoLt0IFuOnUbbUrqpFSiTiJUNOw9WweQgysxFdv67zWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش بازیکن شماره سه تیم ملی کبدی بانوان ایران بعد این اتفاق خیلی خوبه. اول برگاش ریخت بعدش رفت ازش عذر خواهی کرد بلندش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/30449" target="_blank">📅 01:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30448">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDWNJ1TInT5TNsAIh8nVQV1344v43w9kWurgBLbRmx8DQ7KseZKjdO9g5O1UiAOB3KNH2jsllrQWTB9oniqFPP10D6RkJYK3rws-GteApKbe8QW3GDMAVF-T4jRnAJIwY-FgHYbGIE0onXUpchuw_gbaZ7givBbKzi2hR21UqbK-C177lzUJcuTJbJpnRwuMduwILMwRYRmLnjTmWPmmUuM36vDQbnrTUOHu4cAXw4Qwem_G3aArBT7snZfoU4DvF-QDK97LlUG0USQkrSBZvsAJX9rWXjANxRVnhASHhwFZtmcEJYD6ON1bRhdjEuc4KPKkSWma2pGXSRJtLo80Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛تاکیدچندین‌باره سهراب بختیاری‌زاده به مدیریت باشگاه استقلال: بین مامه تیام و فابیو آبرئو یکی رو در نقل و انتقالات نیم فصل جذب کنید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/30448" target="_blank">📅 01:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30447">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWc4vcKNxiJqjoRVlU4JroPPdjBqYDvGV-wM3ZureU3Tia66qrhpjMrE2wS2FfiPsM0T7q6-z8VfGeffWpPkXRaR58IPNBnIYkOmrwwxBGSl-Kaa2pJvMRzL7OEBIFbD8p5phQdQHwwFZo0wHfD44nbsKIPfjTgWowzS5hfUMdT_BZqJIrtRbcCuDAdqCdTKGBLAHHBqdpGSQ65keRheEiWLKEBKrUb1MMnJHxSIBSXPuAhzhjFYoS2xZEz2GNETWGxz6ZhYiFqYWRsm6XDTo9534NuI8j5AsKlqKyZ1rcaTDB4x_xstfeaLMeza1TPiUYH021NWAo597MTtChs71g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ تکرار فینال یورو 2024 با تقابل تماشایی یاران هری‌کین و یامال در ومبلی لندن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/persiana_Soccer/30447" target="_blank">📅 01:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30446">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jj4Uz6NLyT9QBIghdlOdLHZoCKa9CSy8of5jKMFeQt0V5mMRe_jVDIK2IwA1siKJ4SYAylwuL8V2oUbVQsbIFosl80nv8t-oldWMYu5z_dpyB3DeKEjbnL8XdpzPLr9SUKO_48cxQtfqBo1gXOP79A02qJRaifVoQskLLvjKEDMlmRZESN_XoUndrASd62B3xQDkonEgm_1nO0c_fJ-ujefFgf45jBfQt8gnN9VCGcD7M8V9JLW4xd92aknjoBAeWqhRn6FT_lchidLwru26HNtJUBBmElzT6H8ELaiMozRGjORPfbjwdXXYRJhxjeMv5BxQuL2eJtbqWkzSJ5X08A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌ دیروز؛
برد فرانسوی‌ها و شکست ایتالیایی‌ها دراولین تجربه زیدان و بازگشت مانچینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/persiana_Soccer/30446" target="_blank">📅 01:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30445">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2v0jEjr0BpMmuCsd2nVj9hDviefP0NV8qJ6KNDE-YprAyEIhavFlnA55dHxFJCP7M-5zdhZ5v2_emr7_M0yLbMX_w-AzWkqsMD6_71KjYTV8_x-HrTW8-sfjhMXVurupfVvSOVE7BzU4YetgdrMWY2patE_fcalyy2CVebvZQd0Yez0NyGatiUxXzTftS2vOroj_mVJsLZF1ovmmgSW3HxelDef1jlvX5Eulg9K35IYyu1aWInkWJBoaDoBV_f3slKedBgp6iOJicZplkmCick086dcznU8o2k0kfYQE_VuLI8LbKDHPB1syrx_IHj7XK4TE_TGn99S0A8yzGyo_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینیYekBet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
‼️
طوفان یک بت ویژه درگاه های کریپتو (ارز های دیجیتال )
💰
🤩
🤩
🤩
فری‌بت ورزشی ویژه واریز از تمامی درگاه های کریپتو
🚀
برای تمامی واریزهای انجام‌شده از طریق
🤩
Fulgur Pay
🤩
کریپتوباکس
🤩
UWALET TRx
🤩
UWALET USDT
🤩
می‌توانید معادل
🤩
🤩
🤩
مبلغ واریزی خود را به‌صورت فری‌بت ورزشی دریافت کنید
.
💥
🤩
🤩
🤩
🤩
هدیه ورزشی ویژه اولین واریز
💥
🤩
🤩
🤩
فریبت رایگان ویژه واریز از طریق درگاه ریالی
💥
🤩
🤩
🤩
فریبت ورزشی برای واریزی‌های ووچر
💬
بلافاصله پس از شارژ حساب کاربری از پشتیبانی زنده درخواست نمایید
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
p3
🔗
https://t.me/+xNPVsLewpb4wMWNi</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/30445" target="_blank">📅 00:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30444">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Srf51yGUHDLeP92dwCOEtLEl9EYQUyaytlajP3g3CgVxl7PDDozvg2fvl9DKHEGzmB38JkNlG9SaF08wJXGV-EASydKyE1ShTV45EBNIuwNEgXQVF3S9J1jpco1pY6gdhiTQ4By9WGSdrtXSuL3sGqvsNiN-VFF68MmZSmA1lMfW-idSKZf-EYYNsJ-UZ6K9Em97gb26ZGlUGusxRcNTjlG5B1Md8Y1x3HWiEUrFILdGvUk26vBfHoXwXg745qO2GWnDMp4zUXHyWu_Swj344F4D-LbUm6OLCEAYfd2PAZKH-ZvDGWfQY2i_O9WKqIacFQ6hJNZP8KuvDqiuXEcyOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازیای امشب هفته اول لیگ ملت‌های اروپا؛ مانچینی با شکست استارت زد؛ زیدان با برد. سوئد با درخشش گیوکرش و ایساک سه امتیاز رو گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/30444" target="_blank">📅 00:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30443">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRvKICMWw_EpAQ2LwKfaIU1M4-Jqw95DwCvY6pUKUPXYXCFFU8j8qVhtHhneurD7jTsol_qow7Exuvon81wkVlGyYLFK7P7LqTJ0-ifs4jqLgweljuQU8hiCL4dpSxmFIkWSwY0Ye6tveqLjyfUSYbLW7EUpHp1S3LSPr6I69nh8_T9WWjn184FBvHQLZgMhUzRsGE2VOvcdOQwxAY3BnqymGU3G68zVQVNXZIPjvPvpYT8N2xCbMvx4CCUIziNQ4f7EI4M2aXJs0u-dUTPdUJe5wlKwJ7NdQyQPEfmDO_tjWrIuKg8j2YtEpxXyhtTjiOkbHZcQemeMfYu-ii4t3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ ازبازگشت زیدان به عرصه مربیگری تا نبردخانگی لاجوردی‌پوشان با یاران کوین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/30443" target="_blank">📅 00:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30442">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H95lNf2fCk4lxft6rsXiW_Ef690wPr_AmuYTF-HePvx2mQbI2C7szHFE65SFIiP_cYjyyQBiuN-fkrZcy4eaojxrtCnuKaY4LymK5ZaqlHknydTuIJJzr5I2Wd6ux73b2aCYveY_n7QS9_6yz-fOcozfAYEe-X8z-iLyTHDk4tKGJlv0XkKIUibEotIIcyS8b0CCv4VH8cqIDRmf_hJy7as0VA5mVkXOgULUVT-LxybRHsiF6TzWhaBzj5dDSbwuWWzHaLQio7zg1pIluMRkNudyFy6QpkZ3lLGgQ5aCA81CA04EV3b3drDAWWlMGEHN3js9nxZ3z9yWhTCAtM5jGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ قرارداد مامه تیام با تیم چوروم اسپور ترکیه تا پایان فصل جاریه اما هر باشگاهی که او رو میخواهد با پرداخت 300 هزار دلار میتواند رضایت نامه این بازیکن رو از باشگاه ترکیه‌ای دریافت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/30442" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30441">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nptYs_YOGGuBwK_rlCSL3E0XVMd-uLuCVetKT2M86bZYTY0cC-1jJ_hhzyJElgTILdulF2tKHo3KgAhBzmJPPg3zgk-GPBj6DRnqj1ToHAKcnApkZl9NoIDuCBQE1v9Bu4oFwJTpvzwPImVe-84kLhbzru2wdNbGmGkjbXwfyy8_GwhBnboM5Ckym0CPCbVLN7Z_USPpP7RptPAcV39-_PBap2PM6i2qsYLaXX6rblF10dc2MXoJkSwwQiId11NpYoGGNzl2CAbXlBsNNrQjKlnDuPm9LnlGs4u82XWw_je0o-MiVSZHVEm0JxhEyhxUG1M55XZkPrW7RC2_Vhxhdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج نهایی و جدول رده بندی رقابت های لیگ برتر بانوان در پایان مسابقات هفته دوم رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/30441" target="_blank">📅 23:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30440">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jli9nvZGfJe-WkqX6PQhO8njeVLHZrr273jvGfGmVI6X1EzIb0mw0b8YmZtMEf2kLvsvy5chcPPNX5vJr6OS2vkewhl8I32BpOYrZoMb4fVFkFr-PbdV9Qp8J6LIBQ32J4p2z7ot-KEOjj9iasGDbIzSRiZlT5opRwJloiPJPBkdL3VHmQfoysf6kAn4qtWJTxSE1njE9q-JDlzOh3U6rXcApD366IE0F33MP-NGE68IBq2ddFrD9uPTjz3tCZrEVf7spvlfrgOM6syt0GwBnMmjAltw1V0PXIKdkCd62kswlULXM9VyPC3iSRCa2SZJysLW_0OcRRGddg3uQW2cMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت مصدومان پر تعداد باشگاه رئال مادرید درفصل‌جدید؛ فده والورده و ابراهیم کوناته به جمع مصدومان پرشمار کهکشانی‌ها اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/30440" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30439">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔵
👤
مهدی توتونچی مجری شبکه ورزش خطاب به حسین گودرزی مدافع‌چپ تیم استقلال: مطمئنی استقلالی هستی؟ فردا روزی مثل جلالی نری داخل یه‌برنامه دیگه بگی نه من نگفتم استقلالی هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/30439" target="_blank">📅 23:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30438">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsnSkZgZxpg4Svha_9sApbK08AVAY2doH97HBXp2jfBCHqyPa_82ezS-Su6zMTIf1fmKZxNtTegVormRXl9ZgQ9BABHs-sRIDW4n2z3NeN4_DbTvsyqdOO_10u3lY5LO649NiGkoRiOZlAvQLXgh9Ppvt_cV5Zpj-U_1IHKTIpw_JCaP72_Zq1ZInBOkIcNeghPU4YNjpHK5Td0O9Q2Yk5G7-AAyKdLyh-ms8w9olYnKZJFncMIaT2AYj3dd9qFaXfTtSJP-ZnscJhfMuqVwGxclg3TeqHdxf8YFL3HxDCW4Ysg8P9q0bd0IludCZhiZ5pkn-UDQOe72mgqnM2ZAhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شاگردان مهدی‌تارتار درپرسپولیس امروز عصر در دیداری دوستانه یک‌برصفربازی رو به چادرملو واگذار کرد. علیپور بدلیل مصدومیت دراین‌بازی غایب بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/30438" target="_blank">📅 22:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30437">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tge8y2urWsws3A-8hbklBcGLSbsWQRRcktttnIlq8J-SjkRcnr-pEDfsltG4-tUJ01ZALlLBrqvdAD-Q32vppaX6O3C2F_ssqrvlC2kBXybsEc7BwjlBd5WT_5oDCqSIwLuLiy2uOZrNTJExT_WI0zAin-06IV2QhbSDxNX6sAEAzwx5kbGQufl7vWYDD5u41oEqZg1YTfq3gc9z8CbGKQsCSV4PkJTm6ojw4OuMgrtH2GSsytWfcvcxQty9gMKlFrZdQJpuPSKJ9b9VGTtuJeOkSCaZ6GiszDQK36WMKdtYsxYoOgc_uFDPPVEetiG7hPMnJIVNxedTFCBVdqFsIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇳🇴
#تکمیلی؛ باشگاه منچسترسیتی انگلیس برای‌فروش ارلینگ‌هالند ستاره‌نروژی 26 ساله خود در تابستان سال‌آینده 200 میلیون یورو میخواهد. از بین دوباشگاه بارسلونا و رئال مادرید هرکدوم این مبلغ رو پرداخت کنند بند فسخ هالند فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/30437" target="_blank">📅 22:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30435">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iRQ9J4brAc0LASee7RmnVQC2VthjbKQcbfLPhBkVy73BPFBLe1zVUFdih1_7PJW6lNttPNQ1La9SI7tpb-GymeU0jzNx-1-5NAzDwMqRgvTnXkALX4REzQ0fLLOVpZ_6-2BlRT32X02F4lCJp2Gr4Fba_FgucbwWSG8orqQ2wGdhTqgzK8msuvIBJPC7BIdZ7Wbd6hz7xOBxK_9nJjnNO-nDBw0ynUZ_sHcGI2j8ObX7CAVCRxJtsNkIoyubp8xJ7lkGwogfpd-lM8jccyCMLVmxrWcGvfGboUXuQvTCEYVgUaLQcUA2Fz6yTzqPjPZ9tUxJY7LAzoJwquTPkbYFKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tukTtHbbh3kPeTP2Lon34EOHvXboEWjiWpXWeJTx7cgI62t1wcTn2rlTybmZrrwohf-H7FlzUTUlGxt1WUdPIa-A4CuYrOm3SJheFCjCUwRGciZ1haCbYLvBJq3LTlzQVTUNGVcMEcUDAx5dk77gDzxEGZ6DdMNZUA3Hyq4qHTE8KLdBZ4MXgk_91Poe63VqkgAKOgo0JGARRLFFPt9GANAg_xRCjl0wBJ3Z4-3Eu5Vf7lKWPkTvvZ3M7s6aHM5MDs8ZSGRzNHvHacI9EKoto6EnzCbGfJQubIshvwiYkkWn8yJKoOQb8es9Shv5ztf_68TmO0jfNoB8GxA5IgEX1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول برترین گلزنان تاریخ؛
ارلینگ هالند ستاره 26 ساله منچسترسیتی‌که تا کنون موفق به زدن 370 گل شده گفته که هدفم اینه تا سن 33 سالگی به رکورد هزار گل زده در کل دوران حرفه‌ایم برسم. در حال حاضر کریس رونالدو نزدیک ترین به رکورد هزار گل زده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/30435" target="_blank">📅 21:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30434">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21cf909039.mp4?token=ungUb1xKBKeYf37A1t1ZTkARD2LloXTT5Y4opOH78vJp7qnTJZrN_NAQ84jISmXLeftmWgajpSQjagKRXTB5n0oKBVfttaStFyZnfTeP5ynyzc38qWRBdKZ8H8fcqBD-6oybvjELsA-hj-gjuJj1aQaGAvkgjDcGkRs_R8ha8IZZqANWacXjL6j7Rhkuh6RpCO6h1J1XQ_ETJFT2svDU7bCZSvp_RljKGAArtR9v6Yv19Ofca5tskqbhOExqq4wNoy7e9GjgWEsTq5Zg0C0hEoSNydRqz9PMFTYEVU4chxNtRw7dR_CXQ6mXSnL2F4U9XbBbH9IXLtfv-bRCbH0A8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21cf909039.mp4?token=ungUb1xKBKeYf37A1t1ZTkARD2LloXTT5Y4opOH78vJp7qnTJZrN_NAQ84jISmXLeftmWgajpSQjagKRXTB5n0oKBVfttaStFyZnfTeP5ynyzc38qWRBdKZ8H8fcqBD-6oybvjELsA-hj-gjuJj1aQaGAvkgjDcGkRs_R8ha8IZZqANWacXjL6j7Rhkuh6RpCO6h1J1XQ_ETJFT2svDU7bCZSvp_RljKGAArtR9v6Yv19Ofca5tskqbhOExqq4wNoy7e9GjgWEsTq5Zg0C0hEoSNydRqz9PMFTYEVU4chxNtRw7dR_CXQ6mXSnL2F4U9XbBbH9IXLtfv-bRCbH0A8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد تند جواد خیابانی در برنامه زنده برجام از فدراسیون‌فوتبال و کادرفنی تیم امید بعداز شکست تحقیر آمیز مقابل کره شمالی در بازی‌های آسیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/30434" target="_blank">📅 21:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30433">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJOMRgcj0FSEbv-KqLUQCdyXLbmqabbsGTc9-oTUaTpS1WhfF6otYqgOR-WHVKTczvM_aW0RKX0X2y7i-Chju8yPBLUGpH1njMtKz4-g6Z7a3LbzTmsYoyvhokSwameM19HkX0Yjq0R4y3W0ypiCN4LeOllq28VcfKe0AmrzbqNIS6xzwd2TD_5rMKRC6jnO2nVv4nWqz-TS5oNhb491-owKFSCXCMdGqweLf92ck5SCqKPtQCU1ygfsHYzlvCfHMrf-nOVpuIlnMqmfDKeFZoktP4zBQzNLVDg5Sg_eYnY5ntNNgVw4MTWDU22VEwNBA4QaUW92WjAEaEj2LfjLrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت فصل جدید لیگ‌ملت‌های‌اروپا؛ نگاهی بیندازیم به پر افتخارترین تیم‌های این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/30433" target="_blank">📅 21:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30432">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwzeCgz_iEj59qi3qk7DaSaFe5rpXlzPtPEkg2HhTBSSJIvUdCyydTPqug1SyZZBnbW67cU8BtcdICQjTUgFd5EIS6saUHBIdGIluMBtWuX-XkD5bcepYzcNr3cxS25eVMVdjTDE1__-1K9OsvRYY4WPyXAtRgVoAGbHsrvOxz6PWfk5n7nNuw1D8MhlcexGc86L-CBU2-HehO9kNWfRqV3VPFGixPBimxidoUiTHjTGCGE_JmYhFeO6NI13sMsvxDAQs8OqaDiDYj32EdhTAGbITS6ORny1dZifgeJsXQ6WdzG3w7fydU4CA-VBuyqJNwzilFDpCMRNfC8AsYw9NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
دو لیست‌متفاوت از تیم‌ملی؛ لیست محبوب امیر قلعه نویی
🆚
لیست‌سیاه‌امیر قلعه‌نویی رو میبینید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/30432" target="_blank">📅 21:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30431">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5WVrSVjol1nrf3cqkLglFRmzFhcj8qCvjLxG2JxbKcr12anLKQwWE_JrLvxML6V2kycOm1rv75t5asy3vVl2WVXJWLzpw2LoKjBNTL2nwL-t-z435fn67NgNUDPaZSDbtuos9kI6AgllRE5v-UpFN2r8C82dkafuUii59g0lLzIe9QYwy-DIJnnqnkC0kuhV-XrCkw2m4RBNMSpZyi8oCOveEKruVh148Q3ogxHEvrCTFwfZZdJ34q1iRUqrketJKbJjCKRW-tZTqu6l8VSta3KH4AwOcAIAIew1_PUbHCzu29ZD0dkM8qItBhtvB_vKFWY4DkK2fm5KuXQZLB7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینیYekBet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🏆
لیگ ملتهای اروپا
🏆
⏰
شروع بازی ساعت22:15
🇹🇷
ترکیه
🆚
فرانسه
🇫🇷
💯
اولین واریز، اولین برد بزرگ
شروعی هیجان‌انگیز با
🤩
🤩
🤩
🤩
هدیه خوش‌ آمدگویی ورزشی تا سقف 250 میلیون ریال
🖥
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با روش های ارزی و دلاری
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
با هر واریزی
🤩
🤩
🤩
هدیه ورزشی شرط‌بندی میکس دریافت کنید
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g3
🔗
https://t.me/+xNPVsLewpb4wMWNi</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/30431" target="_blank">📅 21:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30430">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/537ed2cb9e.mp4?token=mX49xOuoT9ZZ_pfF7OGbuOkOMMKmFx1yRo2vyyMfCCZU-hW__6DrX6moB-Gdmuzh7Dnb2EPJpPoYmq29WT3-gGL5gi_cOdZFEuS46SUU_PpYJAn5Nid4yA586s7Jvpu90wcoqqY-VvGuYm9RLB67C8FYeMBxXrrB63TxQlX1iKAavLmC8Qi2EJnV11EOuGtxIjP9yQ5FJ5kRqfPDIRvaAXZGCy1kFs2fgW4sBvad2DQAHYoPt3jIzX5UFKZwl7ioZJ0ikxqcaTf4s-3mEzyMYzwFGLQYSEr3vJLapOM2WKvvt6Nk-h8d9i3zBshX9TxLwTujVGbIJ8QsYSMqMFHXgFPaNCaFEtvTp7UnWt6iVMZHNjc4fxXChyeKJ7JxXaUvQAV_eWiy2dHqUdpjff3tr2etoIYDulaKVWbhoMLGqTl5ZdmOVkHM75ipcBhFjCyA2qTm_kwuIV_hF27HVnLhd2GyNEOWntAwW6VWS5NPEh8fqO1AIHjd5MrApEfTltBFzfg1I6XiVPt1eGLNWEKH7I-xm9BLR7n65ry4FlMfEy34LDmjA04aALFcW7C-bHPkK2ag4MDiIiREISeKwRp-RVpPURRu2sB2Jy9KxrlOiPEWKg1eiI4RvmQGlv_AzFoUjuk7xgwDJzcriDmBtS0xUnURdtrwLefFasVasuHt76Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/537ed2cb9e.mp4?token=mX49xOuoT9ZZ_pfF7OGbuOkOMMKmFx1yRo2vyyMfCCZU-hW__6DrX6moB-Gdmuzh7Dnb2EPJpPoYmq29WT3-gGL5gi_cOdZFEuS46SUU_PpYJAn5Nid4yA586s7Jvpu90wcoqqY-VvGuYm9RLB67C8FYeMBxXrrB63TxQlX1iKAavLmC8Qi2EJnV11EOuGtxIjP9yQ5FJ5kRqfPDIRvaAXZGCy1kFs2fgW4sBvad2DQAHYoPt3jIzX5UFKZwl7ioZJ0ikxqcaTf4s-3mEzyMYzwFGLQYSEr3vJLapOM2WKvvt6Nk-h8d9i3zBshX9TxLwTujVGbIJ8QsYSMqMFHXgFPaNCaFEtvTp7UnWt6iVMZHNjc4fxXChyeKJ7JxXaUvQAV_eWiy2dHqUdpjff3tr2etoIYDulaKVWbhoMLGqTl5ZdmOVkHM75ipcBhFjCyA2qTm_kwuIV_hF27HVnLhd2GyNEOWntAwW6VWS5NPEh8fqO1AIHjd5MrApEfTltBFzfg1I6XiVPt1eGLNWEKH7I-xm9BLR7n65ry4FlMfEy34LDmjA04aALFcW7C-bHPkK2ag4MDiIiREISeKwRp-RVpPURRu2sB2Jy9KxrlOiPEWKg1eiI4RvmQGlv_AzFoUjuk7xgwDJzcriDmBtS0xUnURdtrwLefFasVasuHt76Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پارادوکس‌شبانه‌ابوالفضل‌جلالی‌روی آنتن زنده: من هیییچ جایی نگفتم که از بچگی استقلالی بودم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/30430" target="_blank">📅 20:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30429">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opMDDiemdi0x0C3H7jd_MTTE_KzaSpNUoVtlclfwQAuLygSGJlI7gUChzM6pFins3ptYqdcn12OQZ8Ib6qf1pmy0Q4_Bq3LGHkdM0vCHvhRrnqwqm3OevjXCfTZBqshF92xr_1eTNV4GEn5e4ACUuZ0adZcn8yWTIFrVAH0Rjg2Go1D2jtpgmAZGq6-hts6YBOc2autw6dRIy55HnGYF4zVvjrT0aodrj353w9_YlBgcxs0prtIDy7rqXBZr6AbDobT0Zsl3EWyFr7VZ_9dCg56HxGH5z3ZjzrvD7PFVhAgvRqmIfWPGkCmj5z3cKfu4EfjAAKnDbxpjS1MazaefaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌برتر بانوان؛ آتش بازی پرسپولیس مقابل قوی‌های سپید انزالی و شکست آبی پوشان پایتخت مقابل خاتونی‌ها در ایستگاه دوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/30429" target="_blank">📅 20:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30428">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEJHaFtFd7S8gDkJgECdzn63PaL8ope9Hc8mJPLrFnxbzu9kmlTekIUQIpXmzAk3RHb1VRy17rW0jFYBBr6dVdUDZwrjqE3hOdfXRy_PSDGP-axP3ZmI0PAxwKSIgjs0sbGkrHkVzRPaEYvlCb2QxGd9tWYFmmLeuX7p77jJS__TyKk3w9bzDb32MjqnFMUbzr-ompiUajrWp2forLB3-qR3caPXvNg3O4cAUchlNjsn3ktqPxHE0iqZp5JiP6uzHZeGtevdOJablC7U3SOYE2PGMwz5rj0DSTWWpgnZrj25m_fLe9oeOJvGAnDXH3tCaj1iCoXmIk0HqhPqzjsTbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بااعلام کادرپزشکی باشگاه استقلال؛ حبیب فرعباسی دروازه بان مصدوم آبی‌ ها به دیدار شانزده مهر با تراکتور در هفته هشتم لیگ برتر خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30428" target="_blank">📅 19:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30427">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-ROpXu-lf4aDNJD8Jojca7ZJJx-6ahO2Z-i0DLrDVbyswK8QHnarLw8wXdbNV92K7V9aP5Q8RJw8_zYs7-xuEArYv1Sk_OupfQnVuXbQZoFiUaJPDnosOLzB945fzvsWf8FL8UsGMAO0vVALp30hGUS-SSouFIGPWQR9I5k6xhkCEMjIcLP206vE9MzdfI-x9wHMhiSaOOXvvWwKEPfS5osovtxQQPfSWm3o55MgMosxLiiVI1ehxBoW-yq_dYsBPAkWeBHDtGACWkkV14KhefPG_dmN1wj9P5qEa4cdDW2xJhC7u4jo-8kqlWw04RN5UL_-wlwzCCurktBvV60qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
عشق و حال مهدی قایدی ستاره ملی پوش النصر امارات با پسر کوچولوش میلانِ عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30427" target="_blank">📅 19:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30426">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXwNEXBLlZe0j6mlpcRT1p5QDY1coFF0EiONaWiDv5lWeBeLaXs3Bisf8VNbzQmmXLnc-bz6Imi0k1y-3nJo5o6aq4Y21JT1IHDrVHJX7w4CeTYCfAqJ6ph8ynq9hLkOhMGPhNjx3PBvZsmoA1QMqhDhKXd8aq9-mUmweKovXCz4hm6p5R_AZlKPDWUaebMiuigLAnOfc-WXh76wV7sjDfrxE9v_NZQdj4fpVRSgSIuZlq3nzGICmcpORIQyN4TXLL0p2CicwjBv1fXmqui_5UvgM_CWIHp5GcwDvMtqNgGQbcbZAF3qRk-PJ7TC--SYFg90dHtXWQJIb8kZ09xCLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ظاهر جدید وین رونی اسطوره باشگاه منچستر یونایتد با کم‌کردن 40 کیلو از وزنش در تنها دو سال. درکنار کاهش وزن رونی اخیرا یک عمل رینوپلاستی "عمل بینی" انجام داده که باعث شده همچون قبل خروپف نکنه و راحت کنار خانومش بخوابه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30426" target="_blank">📅 18:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30425">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKeg_MXkMwX6eJwwtxV7B9ETOgleFCA1z6Kr4ma2ckLs--WUJg5A5FdYM_uvKxcKHZYhs7bMlyuqxWQ35QmWd_v61lB8xGAxImCXQiTHSO_MGjWmk9HhqNBKTfmwnkC0V4D-7F_-e4wfxuSmFyojCjB23aLm0pX0Du-raBfvXOhBN-izs3wO96NCgdf3pHPNyVHS1LQI-PQCyZIkSBAWZWzUoUhA98k1MVC9fePf-A-CP-oCFXiKNg9M2XYEnJFRuCYJAqG_NnO5u0AE8T8I8fxqBwVFVltUQFCJrjZ6Qu2CMcdL5iEFgjv9X8g8KkoyxEilZNlTIRTwI4aMWwQYbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
بعداز تمدید قرارداد اوستون اورونوف؛ باشگاه‌پرسپولیس قرارداد پیام نیازمند رو هم 3 ساله تمدیدخواهدکرد. تمام توافقات لازم انجام شده است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30425" target="_blank">📅 18:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30424">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUR0lzYpa482OVzRspcc46aQDLF-YeQuEfYB17L-KrjyAsHL4mkF_ER0PZdFEZ5irITQNPvtrC_lvK_iZg2I4LrPj8anynr_C3DPJeBNpVqwO2nHWP2tQyVD7W6oQkZgSBnNm-yySYS8n-zm4-Z-9b6VYE1e44ICf5mVChxdyLL_734H2EujXhP-t6mcRVAJ7UDuDo0A3ZkDH2NJlxnpHUPEIOJq-8WB1P41s1lBVzY9KtSfSJeFl522nDx7UgmQOphFtiYVez0LIlGAgEeFMZETfjHg-4W_VVB7WD1bTtgXuwqIdt5CgtlVoMgfFdrG3mAzRPNI1B5oWT1Xg0nh4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌برتر بانوان؛
آتش بازی پرسپولیس مقابل قوی‌های سپید انزالی و شکست آبی پوشان پایتخت مقابل خاتونی‌ها در ایستگاه دوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30424" target="_blank">📅 18:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30423">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bz7P-bfBOOqJYz2bog1pOcfWja85qGP32g6zIQWDDYq9901IDMOx151rjhMe_R55meLcrawwwQ4PN0NGMIUSk3E7eI0mCxBaghUpczr6loKakqXGAVrMUHd4nVkWmF7-npTLB3T_IUOQy-1VT-c7YvbT4Ri1NluCM_J-I6dhPmkG7XgXKh7RVQpZiosELS6bOkgkdpvJyjv81lhs6ddO8rOP717kft-WkmSMXnF0IBaWIC0OXY5EtBNvOphC_of2ahcRvezfLLrhBNYPirPH08R-kQbsqctrP8Qxd3zjVe5-m9T84dFcNN9HjvxD1KfhyqrMMse__ewq0SgT6mooVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
پرسپولیس دربازی‌دوستانه امروز برابر تیم چادرملو با این ترکیب بازی میکنه: امیررضا رفیعی، پویا پورعلی، امیرحسین طاهری، علیرضا همایی‌ فر، میرشفیعیان، مجید عیدی، محمد خدابنده‌لو، یاسین سلمانی، محمدحسین‌صادقی،تیوی‌بیفوما و سرگیف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30423" target="_blank">📅 18:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30422">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0v-YQwGqcp2my-SR8oYRuDrTxwJ-SU7-CO4K8OA_4u18g7d60thxZz8UZ8x8pt6OtIAVBOjf6ThNhCaY9UMsMIdR6xFKbxPvhkz4Ie3_XoNlU9KjQGfR_oL1pAid7aL-tbT0MHzGjdrs_wMzxYsvpe7scYZ8eivHMjKo2AlgVNOj_GkZp0dUKPCkyPTuLwiC1Mfj3ULMCNl4CylCDgCxYWpDPUTyZokuwrKkcrpQws0tvxXVKCQ6lul8oSQS5w0GiOGaeTAdzaqyMXo3B3Ic2lQTpv4Mow-GwfLKnxp0irBMnsZK15SmU3_dC0Bupsi_6O8TzxPAHHmZ8ESQJ7niw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوید اورنشتاین: من سیتی درتمامی ۱۱۵ مورد از اتهامات لیگ مربوط به‌تخلفات مالی، به جز فقط یکی، مجرم شناخته شد...! هنوز درمورد مجازات‌ها تصمیمی گرفته نشده و تمامی تنبیهات همچنان روی میزه. این مجازات‌ها میتونه شامل جریمه‌ های نقدی، کسر امتیاز یا حتی اخراج از…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30422" target="_blank">📅 17:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30421">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQ7TgtKCZEa50iucjFS8z-TY5_c4lPLnbJ6nILJLaCd0vjFQkdqm-owJzdRR5fE3Vx1OLknsdxp9lgFFRy-VR-HtXPaCAbkyAY6y4WeGkj6MutdZo2DACs3J7iLqyQ86r29NUFTle4fnFbkA78NnQZ4xPcaSM0sICt3k_5hQSkU1-rhzVsvgaMVSGLyY7FTuvqhKK-FNjPYDfM90UAxfdf55DVWf2XUf98VDTkQtdGgr2kldNqONQRmcmDMditMF7_G473DKawwP0oiJL8W_1zs46Q9qI1GSkUlNWylEfoNvoi_ZxQzHwa-AQJPzBt9otvVA9iSBiriWmJHFHQicag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوید اورنشتاین:
من سیتی درتمامی ۱۱۵ مورد از اتهامات لیگ مربوط به‌تخلفات مالی، به جز فقط یکی، مجرم شناخته شد...!
هنوز درمورد مجازات‌ها تصمیمی گرفته نشده و تمامی تنبیهات همچنان روی میزه. این مجازات‌ها میتونه شامل جریمه‌ های نقدی، کسر امتیاز یا حتی اخراج از رقابت‌های لیگ باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30421" target="_blank">📅 17:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30420">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wzy_uKJY09wq4mc6ZO5B4DpkFhd5a5F8MGXeCmaloQd_104r0UOUIJ0pSHhTCmUdsxede9jIyI60798aXPFZ4XTCNVm6Mgk1kE-QmsbZtaKFPKxCONWCxzySNibFCRBfJPEOHiKrEujNTMd9TsQysiZ_srR883tWqJEuNz09Mh1WH62dSdr09W7hJDPT3NHHDU0ZYUYkDZd57yZefR2qiJHM1pCqtOQ19nfHmeGYxtW_QNEfK0gaZTmnr1kxl4waQEXquzYdSAeTrYcFmX1IYZIz3An4bOBi5dAdxY7FXI1N7zmbJOZiteCgKiw7WmRIm95DP-t_9AhUy10PYL5GBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
پرسپولیس دربازی‌دوستانه امروز برابر تیم چادرملو با این ترکیب بازی میکنه:
امیررضا رفیعی، پویا پورعلی، امیرحسین طاهری، علیرضا همایی‌ فر، میرشفیعیان، مجید عیدی، محمد خدابنده‌لو، یاسین سلمانی، محمدحسین‌صادقی،تیوی‌بیفوما و سرگیف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30420" target="_blank">📅 17:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30419">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlT_kEJ5nr4h8r-4GsUncZ9vqEj4z7kQzHAtxulz6W1oimPN9_IIhflhyIQAt1H5G4c2yXSllPlSYODhqZeJsYpJGR1JQcXgzdfNhDUtyK5imcrfdXh_i52g3k6ss84ehKFEuHwW3YywSjgsa2p9eYo8ofYYgG8H6euNW01kEwJ6oiqvyDTX5APK1J8_vc320cLqySnqikC_-kpBIq13bPICm3vVWbRR_Bz_MQP1cFewD-yEj4zRizX2azWJXYP_x9Bws49U-WUsNO1uQFtEx1tTDycutS_e0--gyfL6QSGqNgGJvngWBahZ6UP4B8XWzdWD-awHFvG09TmIXLaiPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تاثیر نادر محمدی بر فوتبال روسیه؛ گل عجیب با پرتاب اوتِ آکروباتیک! الکساندر کوزمین، مهاجم بالتیکا، بایک‌پرتاب اوت همراه با پشتک حرکتی شبیه نادر محمدی انجام داد و توپ وارد دروازه روتور شد. دروازه‌بان روتور نیز بالمس‌توپ در ثبت این گل نقش داشت؛ اگر توپ بدون…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30419" target="_blank">📅 17:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30418">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e998b3c1.mp4?token=mVchqkatbQbwqDXJ8zVKtaWsr_ju8WZqrAKSKc11zFVzencOIoQ581e8Ze-OAAZuUueBq2uCI2Cs5vS_I8QoxuDIM_0q4jvMzR7E4ZRehLIGXSEbAWpUOYyyIxOZZk2w-ixYVlRhwFoqDrPUFWl8k_gNKC9ouAQI7ob208K2Tbarrim7s0len0NVG1PPmXIRgJx1y-zOdPhWtEx2qrO85R-P59afFOd96N9irme5gcjcgCvBjPSulJ-dzM0PoO5CNqy9JIJIB_6WSPB_NE849bQNQcaDnpZ33UKjSWf-qQmTvzhVZ5klv07xdaALzJjscaHAPo6H3IBXCflydc-u3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e998b3c1.mp4?token=mVchqkatbQbwqDXJ8zVKtaWsr_ju8WZqrAKSKc11zFVzencOIoQ581e8Ze-OAAZuUueBq2uCI2Cs5vS_I8QoxuDIM_0q4jvMzR7E4ZRehLIGXSEbAWpUOYyyIxOZZk2w-ixYVlRhwFoqDrPUFWl8k_gNKC9ouAQI7ob208K2Tbarrim7s0len0NVG1PPmXIRgJx1y-zOdPhWtEx2qrO85R-P59afFOd96N9irme5gcjcgCvBjPSulJ-dzM0PoO5CNqy9JIJIB_6WSPB_NE849bQNQcaDnpZ33UKjSWf-qQmTvzhVZ5klv07xdaALzJjscaHAPo6H3IBXCflydc-u3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بعد درخشش نادر محمدی درلیگ روسیه با پرتاب اوت‌هاش؛ حالا تو تمرین‌ماخاچ‌قلعه کادر فنی یه توپ دست محمد جواد حسین نژاد دادن و میگن هرچقدر میتونی پرتابش کن به سبک نادر محمدی. انگار فکر میکنن همه ایرانی پرتاب دستشون زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30418" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30417">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e769a610.mp4?token=cUSME8yactxxTEimJkkhWb7ZWkLChe1crAN33vyE0pgSjz4h20OhEQqMsOhQ17OdnNvFJLuXiMijqKL2sFzZDrKfVOQgcwzjQR665RHORxYDYBJakzB2NJntHBdYo7zmQ6iaS7ew6C1W_gTmIv_Iu_tOwUhVha_4nx4RPxwR6_anqU4rXjNUJvVf5XInv1zkaUNRQlfSp-f3-7U-fvZ4aNYtERXLt46YJrFxg2yYCpzE37P_aKZtPgD_Xf0fKEvF-BWYC7PHntMxCqh_DsfF0KxYjJB2hTkq3BY4y5icgRtoGmUBZleg9hsg57VB0X5RjGp4OcIz4YISjGZos3eCxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e769a610.mp4?token=cUSME8yactxxTEimJkkhWb7ZWkLChe1crAN33vyE0pgSjz4h20OhEQqMsOhQ17OdnNvFJLuXiMijqKL2sFzZDrKfVOQgcwzjQR665RHORxYDYBJakzB2NJntHBdYo7zmQ6iaS7ew6C1W_gTmIv_Iu_tOwUhVha_4nx4RPxwR6_anqU4rXjNUJvVf5XInv1zkaUNRQlfSp-f3-7U-fvZ4aNYtERXLt46YJrFxg2yYCpzE37P_aKZtPgD_Xf0fKEvF-BWYC7PHntMxCqh_DsfF0KxYjJB2hTkq3BY4y5icgRtoGmUBZleg9hsg57VB0X5RjGp4OcIz4YISjGZos3eCxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ساعت13:30 تیم‌ملی‌برزیلِ کارلو آنچلوتی با این ترکیب در دیداری دوستانه به مصاف استرالیا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30417" target="_blank">📅 15:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30415">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AMuS5WqlEwpCFaUiUtLT-luTtHL6CenRcl95eOswrslj0du-NxYFow_wd3Fj1WrSY7mdX8VSVy5jeJC8IXxGgiX3kGnaR-TwjeN2ZpVd-WDbk_6p5P_6oEy1n28iLuOKVolu4TLiyGhTLSTBeLOKxe7e_JJahWF0p6xJSBssORMK2NSh5YvFRQjAgCghqPozE2BiypGzi9Wyb4A08xvshvn4ljzCPrRUG77WTBZPti-ZcPF2NBB7xJW7zEePYGtrfHZbjlQd_ibAAEQXkTQKuVGal3sHus3x0hWGpsdHHtI1JMDo93BrolJEeSla-hjtMe9Db-wVPDHdlzDsMnHGLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fp0M6C6f2hKSqpGsvvpYPZlBiyZS_sNwYlkWNG2Op12UorpPT3om0I8-qiYoq_D9d1yykJXM6TryvXuGl9BIzaEZSCJjXGJF2u-mwPBZakhrTECSBMlxDf5yPgYnxC4Y7EpIpADR3ycqFaZCoeBJURAmMslhWYa86661QpXMrysna_mkwDyRppLYfHzY-8ihp_4Fy6smIJOvdSVEl2ohBYYHInzD5CEkfXJUbLP0soI6wNFw3S4I0Yc2U-8qAgI6B6iiX0ezAK7BuysoJyPRp3AEhgfuLrBVGE6Oi-JX059F6QPevJIRqYhf_vgiL55imYRjRqJfIoUX-_gLZZWMlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
انتقال سهمیه بنزین به کارت بانکی از فردا؛ نحو اتصال کارت سوخت به کارت بانکی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30415" target="_blank">📅 15:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30414">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9587608d.mp4?token=vXZ4S2vti_eg2uryoFKr1u48vd1lgRYKFfs3asTGbz0Odu7A7BBRj7kqiuzuh5dYDdueDVfOxRhLrp4lVZRDlGlCG_DSmNz9D8zEjoa2FEVsu_-9Xir7KjyvcO8kPvc_o54aN7XsX5hit05EjhtI-303wRvvA5W-BN13hRmrkHLJ7IcyjEx646B57z1dHPuSojCZLrQRN_DDomuQmXnTMENQGmoCetXPEhwPY5lctR-W9WCNCfAMmlQEgPY3xtGJyP47MiKcGjfif6QzW9DFz8-2ZKyp3xG0pSuWlC90mZ9dyAQvxmtwGPOU6s7RgEz8NvdlnG48qlVsIhg3b-0IeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9587608d.mp4?token=vXZ4S2vti_eg2uryoFKr1u48vd1lgRYKFfs3asTGbz0Odu7A7BBRj7kqiuzuh5dYDdueDVfOxRhLrp4lVZRDlGlCG_DSmNz9D8zEjoa2FEVsu_-9Xir7KjyvcO8kPvc_o54aN7XsX5hit05EjhtI-303wRvvA5W-BN13hRmrkHLJ7IcyjEx646B57z1dHPuSojCZLrQRN_DDomuQmXnTMENQGmoCetXPEhwPY5lctR-W9WCNCfAMmlQEgPY3xtGJyP47MiKcGjfif6QzW9DFz8-2ZKyp3xG0pSuWlC90mZ9dyAQvxmtwGPOU6s7RgEz8NvdlnG48qlVsIhg3b-0IeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد تند جواد خیابانی در برنامه زنده برجام از فدراسیون‌فوتبال و کادرفنی تیم امید بعداز شکست تحقیر آمیز مقابل کره شمالی در بازی‌های آسیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30414" target="_blank">📅 15:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30413">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6521c21a5e.mp4?token=WXxVI7mZLmRnYm74MrBuyUo7EZ1xG2pqH1ozOqwvjXGaXXydPaAxSMg87xjwImcpya6tx_tIh2TnuOBhdv8kpRoW3Z70KEYvR2pMLF3LLtkp8gF7rXsOkz13NKkS9CdjHs2uZ3v-bwOWuDXjRN8_Gqmg6KCbpDDw_842OELgZvVC7I3eJzPoK5vXUXAXM5KpGDFM33rRgEX7zdfasSkC3GTcxXLpiXmJdWiGcIIl2ShVDAPh1OoXvbkm_pFoN1S8f0O_fSzXqD3vmtfto456x642miDDmzsApF2v4xP_IwzVXbm0BhdPriFr5qKubwtaul_cFt5ZvSe64ILDqZhKT5bj7EGNM4qblzgP-wbO1VnS3M-0bGfDKjnSbfyLAd5RnaG1kSJoro47_kBuMOF35_tLKCGOam1kmo4NWYFpA_9lc4VJ3ciK0r4r8nYaqI4fJwTw0puLGn46_70UQmjaZ07p7eIIg_uuUrhgxyolBI1T4J48GQicN_7TKDXmZFDJGGNC1B54bRHqxp0CXODBDGegDz9s5R_xWwJ2gSGQgTz7mvIzE_1dMpXoolCI3VRoexxRfy4wxfQJsY9I8kIYNZqp5n5HZRjfndmMI4nNlHh3KNAoyPaH9ZXGuJrhC3sC25p_MHqPBKTgC2WQHJS2lLar-RvvNATssUKPnETZnto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6521c21a5e.mp4?token=WXxVI7mZLmRnYm74MrBuyUo7EZ1xG2pqH1ozOqwvjXGaXXydPaAxSMg87xjwImcpya6tx_tIh2TnuOBhdv8kpRoW3Z70KEYvR2pMLF3LLtkp8gF7rXsOkz13NKkS9CdjHs2uZ3v-bwOWuDXjRN8_Gqmg6KCbpDDw_842OELgZvVC7I3eJzPoK5vXUXAXM5KpGDFM33rRgEX7zdfasSkC3GTcxXLpiXmJdWiGcIIl2ShVDAPh1OoXvbkm_pFoN1S8f0O_fSzXqD3vmtfto456x642miDDmzsApF2v4xP_IwzVXbm0BhdPriFr5qKubwtaul_cFt5ZvSe64ILDqZhKT5bj7EGNM4qblzgP-wbO1VnS3M-0bGfDKjnSbfyLAd5RnaG1kSJoro47_kBuMOF35_tLKCGOam1kmo4NWYFpA_9lc4VJ3ciK0r4r8nYaqI4fJwTw0puLGn46_70UQmjaZ07p7eIIg_uuUrhgxyolBI1T4J48GQicN_7TKDXmZFDJGGNC1B54bRHqxp0CXODBDGegDz9s5R_xWwJ2gSGQgTz7mvIzE_1dMpXoolCI3VRoexxRfy4wxfQJsY9I8kIYNZqp5n5HZRjfndmMI4nNlHh3KNAoyPaH9ZXGuJrhC3sC25p_MHqPBKTgC2WQHJS2lLar-RvvNATssUKPnETZnto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های پیمان یوسفی روی آنتن زنده درباره حواشی امیرقلعه‌نویی و دعوت نکردن مهدی قایدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30413" target="_blank">📅 14:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30412">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibqb74tCHmmKJ7h2iEkdgmQ2JtKjlPIVhXQXIC6VaCWqn7Hdb8s4qev9hpl95MyblBG6pD_-rms4brsvlR5YDrlvZp7VcM2m6fTjhJ6goTwAYV6R8HSal17FtzyZklLW2lFQ3_RrLyTOCIrPvkaR_N9dkNLu91uQpxcXdUnFxAwT8kde5yEPTi_bzhP9FQ6qPYseX0IYpAB-ZpgoOVtUUtJz-4Q2_acJf3ZRSZ7_VEWDDcgWKB5bFaOH3tMauH2ECTVuB8iMpb553GVx5xywzfJv2Z3M5b1sTZv_ZA6Db3jJOU9rKaYDahvSsF61dP0zdRikN2PeyvGKNvG7OIx2Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رافینیا دیاز کاپیتان بارسا؛ صاحب جدید شماره 10 تیم‌ملی‌برزیل؛ این شماره سال‌ها بر تن نیمار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30412" target="_blank">📅 14:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30411">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlgxSV9UAuhnxzRuBEknW-ujqgIx40Sg4_-zGKVMYKqTRpvsUzudHcXAhYxMMi2mLu1p-CFzKOLClsNHifMdE4pMMiGFy4lYhdTA_S3pQ3Ukkyd8L7Lfjw7unEPpf2aS8dn1_eM6jGTaqppziivrO2rtxEaUF3WL6J5eH650DfduNrFyFwOSGGO9cuzI3iIOQkCU-1y3B1lG-rppjyRdTWR3K2vUwu5shqiB-C0qfK2n79yS6TTjgz1WiJVqf8eVxN61LFNqIG4feAsTc2rLYOqAa-Of1sOe0eA9hqIdU_IWzkPiFZnJzyq3EyOiadD_S25ay2mhHKE7tom1sLkbYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه سپاهان قصد داره درصورت جدایی مارکو باکیچ از تیم پرسپولیس درنیم‌فصل او رو با قراردادی 1.5 ساله جذب‌کنه‌. مهدی تارتار علاقه‌ای به‌سبک بازی باکیچ نداره و بلافاصله بعداز فسخ‌قراردادش با سرخ ها با باشگاه سپاهان قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30411" target="_blank">📅 13:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30410">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVPXnbEyWXJukJkSUvnptTP1BmbdnsIkID2UHRWGqKYK562P5XCbMnw2uXdDegtbC5A5g5hl5szvtV9MuQIz63kMyrlCwT48Vi7j7Yt1PgG0sgWySzwZ8qDWCXxm5PJWR6aR-Sx8dFKCYTnE-oOHH3wrEcUrAjxyvIit3QCybzWTvLyajwxZjIsQQhFbPAyPG1cCHx4glvjVA3glhcg_1p2mIulOGCnMD29fRd8WYwbbFxmKMk0nBsamDcukNl3I4kbMTlKr3L9-AC6Zpnb9Brc9x44FEMg_HGVjSl9aWIROlvhfUh74p35r7Sj8K3ryXQu8ingSEKXSNbCvQUEFAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج 4 دیدارمهم‌امشب هفته اول لیگ ملت‌های اروپا؛ از پیروزی خفیف پرتغال با گلزنی ژائو فلیکس تا توقف شاگردان ژاوی مقابل آلمانِ یورگن کلوپ و پیروزی شیرین نروژ با درخشش ارلینگ هالند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30410" target="_blank">📅 13:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30409">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyxrXvq08QWydoMzFTCpI4jdIfKQBpb8u7JSIHHQhS64VGKMY0lY7VUK8SzEQk4slM49L7X4BkPq3QVQ1iS4OOdWsC9oa_l8fmH2wvd57W3uLTHaCJ7p0oumedh5soQBGyfyvKC5XKuywmBwh4zHcs6AUA5L87ZvoRjHJdZEJmAq9aLSYluPNTtzUUxeIn6o8lg18JHWufn2kwyH5WlMIMjr-Hcl8sl8u0orqwORZia5RHGWtr0IVflrdHf6c1v_q_Rq0l12sJdnvBypzWKA7Ictd2IDDfQiIsA-7Ny0L7hh5H1V5aqOjl1pyItLs6_GSmIXu5aHyFapf8kXmFW9RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30409" target="_blank">📅 13:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30407">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIh7sztruuzbr6w9J_cJ0pSsgI-ngRurhTGn5V1GM3jsapViesGwiD2RNRWN-DVQS6XQMOnDulr4TunftojczKA8YPzTu-VW-xM4pyGbBJEW1jp4iW1BDzqHBnWZ8m2YQl44-YwazsYFqo_hKr0W4VVgFRK_lltYPcSNT5Ep3tI1ubeqsisu2OAxuoSMRbDTLViJkFmw64iOCD0otOhw1ldDvesE8t-Yn-8OGnJK8LlrEcML3vMXBajfqvAg4VAsGV26L3oPCBHFLtJnYNaCIENIZzDl33uzkHpdEfSzEbeaQ_xstQEjaptLGr1YUm4C6Z2sagJS0qo0wk6QQfw_PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌برزیل‌فردا دراسترالیا به مصاف تیم ملی این کشور میشه‌. حالا اعضای این تیم به محض ورود به کشور استرالیا بااین‌استقبال میزبان رو به رو شدند. همشون زدن زیر خنده‌. قیافه آنجلوتی رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30407" target="_blank">📅 12:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30406">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QpyilfNzCqAFtRDjhY6VBLsyIA-9nVhmFoKIvOKvj8ojjqaEFgq0Pl6p1KoMFs-8VLJqe7PEIwhiSDgjzH8Dgu-Ru8SVccEqzpOs2by2DiozV2wmhxI38gBj_jttOzxYPVlEXPMSqUVZCGFjldZ0k79NVR9d3MFCIOw39X7WBdmejj0kxnZRgKwKEXpoLWirMbjvk58TeD3Z2ECHkex-YZtjMUauoeXYeFy830GbWjFHUljRejem810wZLmb12Zv-kx9c1hz95Ah7e655Ss2Ig5kOZOU5OnnCpnbOHz7K_oWIN0e2ASRP8SUWeeiggb2V3bJbqYQYkIqWFdJiiqGaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛جدایی‌دنیل‌گرا و مارکو باکیچ در نیم فصل از پرسپولیس قطعی‌شده‌است و مهدی تارتار به مدیریت اعلام کرده نیازی به این دو بازیکن خارجی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30406" target="_blank">📅 12:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30405">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9ZBeiJDgkdv6DeZJvQ5f4YL-hqcQtLrIxD3mauXKpNHqrXv4-3_Zd8grVBdiyOtzvHXqDwf3I6MkExc4UoLSbi1pAnSW0cxqpOn0fFP9U9hHvcbEZGsMBdMrh_aa3TBE4SSO63a9Pp330om8By3EsP1mz6_CVhUIiETR8Ewe6ML4m1r6c1ipD9c7-7_LtLo9_ybtxpUnYdkuctKOJmnAt5CdW85jYqb4hgocKQw6fnYfLX9HwKIRj__nKYJObx_OqbEqivd0Og8kltQ5JrzSTTxOxugv2Bbw27DENJuO7NvxJ7-TujZW1-7UIinjHjQk3seCYgb2dql__sEb0GF8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ دستمزدسالانه مامه تیام درسوپرلیگ ترکیه 750 هزار دلارامضاشده و دستمزد فابیو آبرئو آقای‌گل سوپرلیگ چین 950 هزار لار درسال ثبت‌شده. جفتشون‌هم 33 سالشونه. آبرئو در نیم فصل بازیکن آزاد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30405" target="_blank">📅 12:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30404">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1blkMaZ8TpGDx5__s0w_hXf8_nFW03CpsSG9-UXkhOqDNsP2R3C9qN-4VCpTSqrJb4iZNUu1lNAShBfIPK7q8VgEhrSYMSIsUUiPYEwvs0k0qdKkCRZ00v3eg7heiPbgLkIV_UgtG9cLZc8-zHijH7Fuxb6nodtG6sUblK0uzeG8ft56dyoNqx_PYpmAF2PCecEfmt0jFom3XBODdvPQeF_lcBWNDQgW9BEfJyNZr4zH-9Fy_X4FBeEY7Ev2M0FEhO_wPeb3LXjXmb2ucANZC5aD258W0rFhJIbXCAWcSvvLKKdyzdwofmjC6iJ3goy0WnE1zO8kimllwKwGQED_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آلیشا لمن ستاره‌تیم‌بانوان‌لسترسیتی: بارها گفتم بازم میگم نباید تفاوت زیادی بین دستمزد بازیکنان در لیگ مردان و زنان باشه. الان همونطور که لیونل مسی و کریس رونالدو در فوتبال آقایون میدرخشن من هم درفوتبال بانوان فوق العاده بازی میکنم بنابراین نباید حقوق ما…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30404" target="_blank">📅 12:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30403">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMLO9sIr7NXR10Loov-15sJEYMckY6dNe2VS169H1cEMOAFOJZan7cYiCtmwfD5kbUUUcMmubOWegh4VrxMbZwFAlBjl2Hc-E-gjnCLxfjA9u75OEFQqNz4VacINW1amdNLsXZ7pnFLjo_CLAyHQ_M0tbOdy22WIM8KY2KeqO4VCyxBno_YbVtFx4HOVmfnA-r2l7MP-6lkY8q_o8Q6Wk-1FSLVfWdPmFsILAsAo-tP037gAf1dsu86AGIXqaxOfyeZQfBdXujBJiw5NLySNFA7qWA_H6u9B1c774866kQdOESh2i11Q5Yvi3GGQbgpN1HWn9biVC3wjA5n3rGJ6uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
جمعه‌های انفجاری در یک بت
💥
🔄
🤩
🤩
🤩
بانس کازینو مخصوص بازی‌های انفجاری در یک بت
💬
پشتیبانی آنلاین 24 ساعته
🔈
کاربران میتوانند در روز جمعه پس از هر بار شارژ حساب کاربری خود از پشتیبانی بانس
🤩
🤩
🤩
کازینو را تا سقف 30.000.000 ریال دریافت نمایند
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r3
🔗
https://t.me/+xNPVsLewpb4wMWNi</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30403" target="_blank">📅 12:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30402">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciky19wKEdCsH4otU3zgKEqyxP5k4Y11tqWgSkRBP1YItwNq0PtJkpv1zXHf_MqIwrKb0nW5J5C5pCvOL-4gfprjQIGFljHKVBVNh6ctL1nf-a3NoHQaObcrB1fonxBSqLM0xjuu2BJnuO_re02jtSgfiFE9lPjyt9eojqwNHyU6pjmK1B2Avmwf7PJ87bF_Da2ndfO3NtKQU8Y49cXzUMUxdr9rnoO4N6GTUVwpcOPBbGCGrG2XLWZJt92jKgCrUcBuVb9e-JyZ8V3x6Onxk5O4xgKLQFyizCilHznlbcHLL38ByJSuayockq0Hr27WFHRqlW1imCct6k4PlOjEaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ال‌ناسیونال: اولیسه خواهان بند آزاد‌سازی ۱۷۵ میلیون‌یورویی درقرارداد جدید با بایرن‌مونیخه و گفته درصورتی تمدیدمیکنم که این بند رو بگنجانید و هر باشگاهی "رئال" این پول رو داد بند رو فعال کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30402" target="_blank">📅 11:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30401">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/638f1de447.mp4?token=vX7K8QMvi8bNzNRWawrw6yHZRBfVoqb68G9L1IP8L9KdxSZOlug0jyVcmc4coW-265B_tnhm_u_NyB2LwERxbZYerQu2u4N8MqDhhdKxvEfqCnccbla0n4YELp1SRGvCA0vuMB17XpWMTXeWSgXa5Yua11oqKMyVlq12tnF-jpd8UVlrWO2nJ6TyIEKYG_BxT7UfszORfUlLyZvA7P8j6HbhvASMUNx78z6397m3wodEWkckupvNmFzIJ0xcBidlBMXoj0GL8jlxLORAbvMW8QpEMCmEAZ9o47G8hkKxVb9p7bGfZ2s3x7fMkc9Vi7CLUbtJJaU04yYTlVy0icLJYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/638f1de447.mp4?token=vX7K8QMvi8bNzNRWawrw6yHZRBfVoqb68G9L1IP8L9KdxSZOlug0jyVcmc4coW-265B_tnhm_u_NyB2LwERxbZYerQu2u4N8MqDhhdKxvEfqCnccbla0n4YELp1SRGvCA0vuMB17XpWMTXeWSgXa5Yua11oqKMyVlq12tnF-jpd8UVlrWO2nJ6TyIEKYG_BxT7UfszORfUlLyZvA7P8j6HbhvASMUNx78z6397m3wodEWkckupvNmFzIJ0xcBidlBMXoj0GL8jlxLORAbvMW8QpEMCmEAZ9o47G8hkKxVb9p7bGfZ2s3x7fMkc9Vi7CLUbtJJaU04yYTlVy0icLJYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رافینیا دیاز کاپیتان بارسا
؛ صاحب جدید شماره 10 تیم‌ملی‌برزیل؛ این شماره سال‌ها بر تن نیمار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30401" target="_blank">📅 11:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30400">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5kFklbVfIuRJGwsFrikrc9B7u_h_cS1mP6G1G0mhzYoBt_RCNXPL7LHV1rNfduMsjKfXdoIT6IeDX1UbnvjfPv_0Qqer2rW4scxws0FSk0-N0dQmKS5INol22-e9XdfTmDH_l7feT0TvBj_b0BDN6BZind60aojbHI1D92aiU3gO0p2cPlms-Wq1mCLJMSpolKaqRUzX5OMbrp47rgYDYpkN1Rjx9hKpWnwiTpf_f8lb9RDlVEKfAaJ6a0D5_DbZJOiXXqPbYheLzsrEqwGoLuBwG0fX0XwfrqTQ4XpLLjsSqg1AogKdh3q55zHAYSfPZ1hgLvJcGpTgBdPNco51A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیویی‌کوتاه از تکنیک و مهارت‌های خیره کننده جیجی‌ گابریل 15 ساله‌که‌ بزدی یه راهی بارسا میشه یا رئال مادرید؛ هایلایت کامل عملکردش رو تو کانال دوم گذاشتیم. پسن ریپلای شده رو نگاه کنید.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30400" target="_blank">📅 11:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30399">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/649db87b28.mp4?token=Q9jMIn-xgKGgGPAkHGw7sOMT68CaA-B5urGXnvaRQlsLKukRvpQEEMdHkkvFcUCc6t0aE8puM5GvjeLeNeQmDi3VfrD2fT4ThOGL4WaoZEjZFnChmOhXGVa335iuzmBU7hxJttad-gaEyxVX37_BX-QHvxvIxnFULlG3FFZBpxeG9i2era0pZlu8jnZTmR-UJ7ZwgSPXPojXW8POnpXb0Uoguv6GGWTJk9gOET_SoZyxVkMC-UTMZPDScDAgkc14NXJ-F7yslJ9eZ1bBKKloGvbho8oFA9EPzfdE2jXDn0GsKrktmSmaymG2Eq98Mf0cvtmCOQR0hbca1G39NmN7oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/649db87b28.mp4?token=Q9jMIn-xgKGgGPAkHGw7sOMT68CaA-B5urGXnvaRQlsLKukRvpQEEMdHkkvFcUCc6t0aE8puM5GvjeLeNeQmDi3VfrD2fT4ThOGL4WaoZEjZFnChmOhXGVa335iuzmBU7hxJttad-gaEyxVX37_BX-QHvxvIxnFULlG3FFZBpxeG9i2era0pZlu8jnZTmR-UJ7ZwgSPXPojXW8POnpXb0Uoguv6GGWTJk9gOET_SoZyxVkMC-UTMZPDScDAgkc14NXJ-F7yslJ9eZ1bBKKloGvbho8oFA9EPzfdE2jXDn0GsKrktmSmaymG2Eq98Mf0cvtmCOQR0hbca1G39NmN7oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30399" target="_blank">📅 10:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30398">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBD8uitY966YfUIhNvECUNbbP0ilthmMEDf7mVH9OMWcMaFh8aG3yhTxWKOmYCboCLlam9aehlEW8yoUsVjWPteHiiV15TsjzIEarFUajI3CWemusr9m0ZlsBUYk_KKb1EZ-XbznpSSKFEKjAtZpa_FXqT8fTKUNbfZrwlEhkeUXzA4xZI7SDfyO9t4OgLj_dY63GvBp9GfsgJ5AmatSuZyfL6TDWzS1qdZrWIun1Mh_hM6aueXjVWgN4r36z1JWUrG4wqqRIvUgroXWyteXaL0btOORNMLhwTgfd94ZT4ANhfi0jsVDwT470D3CrLt2BAarN8lovvMSRat8oZhClQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30398" target="_blank">📅 10:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30397">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698f9deb89.mp4?token=tbKWp5Y5olzC29hvYT7QExGN4FbST7iqdcmseY71IIa-ITe6VUaR00v7Y-0vbzTIeI97hmE2ywSVFpnyij0hHUo3JcIh1hxS_tr7yg0a2E78aYifFpqDdyD7kyxx9c36ad6hgelXC8k6pKUBl56e8XLBrSSJQdUGyruq5zUxWnzXyssyWZjJ79_gT08-uJgyE2J6t7vegrkjRq8smZYVlibMXv9D02YdrX2zQshCuDtkTuAuPZC3rjdzYRBh-dl4lxLlnPPLwJrVCqiV2AIZ0xGWEqJmtUKKn3U7hnKpnnne5iVo_Ma345QQkmx0mzqvSkNpoqrXHXUAWh-Uhhj1Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698f9deb89.mp4?token=tbKWp5Y5olzC29hvYT7QExGN4FbST7iqdcmseY71IIa-ITe6VUaR00v7Y-0vbzTIeI97hmE2ywSVFpnyij0hHUo3JcIh1hxS_tr7yg0a2E78aYifFpqDdyD7kyxx9c36ad6hgelXC8k6pKUBl56e8XLBrSSJQdUGyruq5zUxWnzXyssyWZjJ79_gT08-uJgyE2J6t7vegrkjRq8smZYVlibMXv9D02YdrX2zQshCuDtkTuAuPZC3rjdzYRBh-dl4lxLlnPPLwJrVCqiV2AIZ0xGWEqJmtUKKn3U7hnKpnnne5iVo_Ma345QQkmx0mzqvSkNpoqrXHXUAWh-Uhhj1Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین‌گزارش نیما تاجیک خوش‌ صدا بعدِ جدایی از صداوسیما در بازی شب گذشته آلمان
🆚
هلند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30397" target="_blank">📅 09:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30396">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5ZJ0f4FWRM9CU21MaKpYfeiRQstgKbFo9mv1wfs2Lv3aRH3_smIyuHiktymnIqd0DoPmXQE-BF4y5UB7rPq-DE8rpI7Kf-y1XtUaEm_1gGg5bPPTcyJ4wSAGJJ0OcUDvGLCxLm8fGC-jhWPBhhYeyI58cQ_VEEyZicGTU4DtCdqntHJgdf9x2-BuT69t7KPMp7ysHPAj6aKbwYdXDif-95Z2RSUkc_sL3WtNGSGB72cjsaX_fhxcZXNUVLtL5vHAe2M3co0-OIRByQ2gXFzOBozZtfkP9t5u3x7ob118Rg2NP0hQcbrAFHzacV7IFChYTd23B68X9aPwcEnUf--DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
گلزنی‌تماشایی‌کریستیانو رونالدو 41 ساله در بازی امشب پرتغال مقابل ولز در لیگ ملت‌های اروپا؛ این980 امین گل کل دوران حرفه‌ای رونالدو بود. البته دقایقی بعد این گل توسط VAR رد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30396" target="_blank">📅 09:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30395">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da1f2ad337.mp4?token=hoQbFphHE7kniR6rp9heuY9FC-iBDYLRaGGqEbJtmadxciF2d8AlQiprwy6oM8q0fNz9g2cZObTU-Otw_inDFQiJFHNghPO-jUS4XqVg-IA6c44CtrsYsEO-t-8nFvqBeRCnXI0kM0gn8YEElza3jPeL1iSMRdoDpMRAsDiEf9xNFKqg1rnLpjD2m2voMSvJ1udD55u9kytgW8oJld5xuPwIxWuzmOdCSGxi1YvyL1NDUiWFnrPiMkbj5wLSxhqGs1imGYLi5l_eTO40OqABUF3nQ6bWKWrxY75Da4AiceFMU2nUKAKMbG1mEGlV4-DVsMnOgyf9jwDWuGEtLEWkpEIA_HSktP64JmlYBvIY0txNqloHJNXOqCXRPz_HqotIsffY4V_8a--Ypv1EkfMer5Bv6ZO_Tk2yk08SBrQCji-Aaw3ho9Ndl9txGKikd0BK2UfgRcQyXVZagoaE-hvxz7TSkx5mG3vppG2PfapqpvtnFEmZ4Gizd92dipr1kae97-RddK1-bmp2ygYUwXv9aXrDgkDvltz_39CnUTXdbCDvH6H71xCbvlvDF1defic3wHCMdn6_zPDGDYmtp78aTI-byfr5Sm9nhWHnKbnsyG55ntlUHDNutyG_fHJdZojWKZtKPmh1R8Tn1TQ_0YB4MbJXHJogqgnEEEgwwYee160" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da1f2ad337.mp4?token=hoQbFphHE7kniR6rp9heuY9FC-iBDYLRaGGqEbJtmadxciF2d8AlQiprwy6oM8q0fNz9g2cZObTU-Otw_inDFQiJFHNghPO-jUS4XqVg-IA6c44CtrsYsEO-t-8nFvqBeRCnXI0kM0gn8YEElza3jPeL1iSMRdoDpMRAsDiEf9xNFKqg1rnLpjD2m2voMSvJ1udD55u9kytgW8oJld5xuPwIxWuzmOdCSGxi1YvyL1NDUiWFnrPiMkbj5wLSxhqGs1imGYLi5l_eTO40OqABUF3nQ6bWKWrxY75Da4AiceFMU2nUKAKMbG1mEGlV4-DVsMnOgyf9jwDWuGEtLEWkpEIA_HSktP64JmlYBvIY0txNqloHJNXOqCXRPz_HqotIsffY4V_8a--Ypv1EkfMer5Bv6ZO_Tk2yk08SBrQCji-Aaw3ho9Ndl9txGKikd0BK2UfgRcQyXVZagoaE-hvxz7TSkx5mG3vppG2PfapqpvtnFEmZ4Gizd92dipr1kae97-RddK1-bmp2ygYUwXv9aXrDgkDvltz_39CnUTXdbCDvH6H71xCbvlvDF1defic3wHCMdn6_zPDGDYmtp78aTI-byfr5Sm9nhWHnKbnsyG55ntlUHDNutyG_fHJdZojWKZtKPmh1R8Tn1TQ_0YB4MbJXHJogqgnEEEgwwYee160" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین‌گزارش نیما تاجیک خوش‌ صدا بعدِ جدایی از صداوسیما در بازی شب گذشته آلمان
🆚
هلند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30395" target="_blank">📅 09:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30394">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7qBC8IdHcb0z9V3JrNzOG2aXR66VJIL0pey7qWQI4mlc8ufyh6JsXXTBl0G0iLP0LdMvaiCUGPCf5BP-bhQy0-7W1h3ruKYHe0cD-A79_oOVqIF76fuI2IHYV0PqtxNFp_FBiJSiZMb4iUAPmCmm_nTStL1cW9XFL2x_baMK6dHWeaxk-ypTxhW_9URrhV1AwHjHgYXVws10nLXDhqHy2A-lshiDgs0TTllMEMhZdnotgiNQoxguHtgssOBhAcrscYt5eUoLMpeW4M6tNiBAQnoFDfj4CLgzmPHy1_SQEyMudwxbzSIL-bFUoAKM1IFgqNLnk8E-n2wjYbNAA7glg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ حسین خان عبدی بعد از افتضاحی که دربازی‌های آسیایی به بار آورد بزودی بعد از بازگشت به ایران هدایت تیم ملی امید برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30394" target="_blank">📅 08:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30393">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ng2kCW4TbwJpbJi0qWembrtUf__4lG6LTfeOHKOXJp2EAo2H-zw4UC0I9bGd8NtzhiPQbyPPAwLrUVUxyYBPaUBZfa2BVbXPN7h4ZQpPh8W40rXwzNC6bDo0zvx_82g86MKMzgO-9IntbfmwEQHViTQOOp7rHLC2r2ReJixAvYMvxfr-Yjz2Pzr3laOYD5Tfwy1-MIQKFtXuTDFnOAqjMOPdR5H7IRr19J2ySvmCOnRWp9G4UgU2HXDbvb615Dta_ce-7wyUoYQmb6X0VRr9V_8kgL5B6eYSA2-UiuC6rn2E4KGGSfU2fi_ZsDuVoDsyNuvmHKWRliOI_IucuX4hwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ جالبه بدونید ازبکستان بعد از 6 بازی و 5 ماه بالاخره طعم پیروزی در یک مسابقه رو چشید. این‌بازی‌های‌دوستانه تاثیر زیادی رورنکینگ بندی فیفا داره. باتوجه به برد قاطع‌کره و ژاپن‌به‌احتمال فراوان در رنکینگ جدید چند پله سقوط خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/30393" target="_blank">📅 01:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30392">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57e45f06f2.mp4?token=fzzOtWojdiz8ojinvUZ07mSOf9FAlQVOKjgH4Rp07aQv-ZtBLyZXI7OwSJSLLjMc8P4UumWpfmGThBFYrrlqItzegriuOOY_ZRHZMLOG07OkEBCT7StSxsPZwFCAO3p7LdMFFXfm6SIMRN84ElNTpNpGJXdqsCRemhphqUcHgQrf5cdvNVH74TapkKXUkpOxK-25uJBH1UhAYjXbNQ5wpa7Z9dQmmWqRi_eRjgbVvMutPEswidxgfqRLJFdTmomjDg1Nw6UjYtVtCW-tSMcCI7KGZbM4qkSDliLX3AAWIav9JraRu2loYYcCNrbcnhqoSicAcmyVUktEErUhEwEYJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57e45f06f2.mp4?token=fzzOtWojdiz8ojinvUZ07mSOf9FAlQVOKjgH4Rp07aQv-ZtBLyZXI7OwSJSLLjMc8P4UumWpfmGThBFYrrlqItzegriuOOY_ZRHZMLOG07OkEBCT7StSxsPZwFCAO3p7LdMFFXfm6SIMRN84ElNTpNpGJXdqsCRemhphqUcHgQrf5cdvNVH74TapkKXUkpOxK-25uJBH1UhAYjXbNQ5wpa7Z9dQmmWqRi_eRjgbVvMutPEswidxgfqRLJFdTmomjDg1Nw6UjYtVtCW-tSMcCI7KGZbM4qkSDliLX3AAWIav9JraRu2loYYcCNrbcnhqoSicAcmyVUktEErUhEwEYJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/30392" target="_blank">📅 01:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30390">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wbcg2-jwhg1iAohS4l2bFm-YbgcD_H_RleRQKYCQgEUaq-bij_qD6sWWEU4QlZlES14KHEHSkLw_2CykZWaCKXCAUvYWNhQK3Wyi7CuombAtbh6r5v4u5BRbtnak__a-G_ABYHwlYinjFfk6_z5FvUIH7AfvpH2CpomxPSv3WCV-wTD7JcbU1IRacDfipyUVBRRYySdB4Pj5j10jDT8TSJYxJC-oOQTOx7aaxqbSItzevbjoK4f-ierj3Z6WbxZL5jsziSt55jSpqraazQ0MtyhRJ5D4u5ecpSS_e3tKgf7eft4Jq1hFFpwncVcIefHUK6zAdCAIto20ysZmMMY06Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ ازبازگشت زیدان به عرصه مربیگری تا نبردخانگی لاجوردی‌پوشان با یاران کوین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/30390" target="_blank">📅 01:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30389">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGP1i5o5VC39FiiM-zZfpTwXVXLd2jYuF5zhR3XEOfMNlcDziOiTmw98AnP0W_Ryk9XyS3ah0kcjHsumr-uDfHkP6ueD96SjBSB40R064eA0kuJhTFu_2O_tqa-P61lAaqgylo80h2Tr2hYdapiL2s9wsXlqQ7ai2s2Jvc1zlIhhLD_-XRyO6vSLUNiDccDYME9ScnAxW5FoAsPFuDgObGh6Mn21a0dqH3I4UEwArHtW3_NHQfSUILhd-NR6A2CEPrnAK_fVLFyOa8QCrXglKn-xEaYoAZ8d8HdEkhk-JHtPPZADCQ35YTZWctaRbisiP31JKtT0cA0Dx5t89OQu_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
ازتقسیم‌امتیازات در تقابل هلند و آلمان تا برد سه‌گله ژاپن و کره جنوبی در شب شکست سه‌گله شاگردان امیر قلعه‌نویی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/30389" target="_blank">📅 01:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30387">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDQj3xUkcdVyRIq5XtywFFSKfqsY8EMoDuCv89FGEBr8hUUlZT3zg6Wz49vXz85eUhiJ_Pt8Pd7jYRswxDZI9LRANPalrUB_cm0unAhXaI68ZCabU9VW8JRwRuSybF1S-QIv0B8KlmrnFoJF555Y_uWGsRxN-nb4mjq-SLhXhrBMz6-r6mJHHSYw1qLLiVWuDCk5qhYSzZWhFv9W9qAN6_aMx9DRHFcd1GEhfguUX5DlDWT5Nr3JU_Pn_bMSLgTMmzRdFS2kAvXzUHVIfGbnxhMjTlwEN1jZYEgc0W8srJvFyFpIm5OA87P7jr7G-WtHNc_6PN3sWQRN7JAy1Yo73g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق‌شنیده‌های رسانه پرشیانا؛ دو ایجنت نزدیک به علی تاجرنیا رئیس هیات مدیره تیم استقلال از صبح امروز تماس‌های خود را با مامه تیام ستاره 33 ساله سابق آبی‌ها آغازکرده‌‌اند تا در صورت عدم موافقت فابیو آبرئو برای‌اومدن‌به‌ایران بلافاصله مامه تیام رو…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30387" target="_blank">📅 00:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30386">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KW1Q-8nJLtPA-fTqi1_4swVM-GinkpS8yvvHlIat8mV_CPf2pNqXkwbtNZ1ZB4YWVwA8qYtz3uUavu9V3uji0HKsA2N4ZBKNWRJsb-SXNLrhfZFsZbjZqNpHl07UlYHEqW1lzq4EaXoXDXvPmilaUsrVoI-itvVWWKx8iEVYasW-9jd5478ab8mBzpXjk5gWm9ABZVe-8fadzRIPxm_T8ojitXfzBIyPWVCcibDuPt2xoulq1aDM_sI2HyHR_wkJ6BLXhUPg9U652O2DexaiLORo1U75ci93q4ippHs6-cZG1gIzAjL137PsYZ1_vGXQd7d4Xpz2HSZv7DrkCTFRvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
گلزنی‌تماشایی‌کریستیانو رونالدو 41 ساله در بازی امشب پرتغال مقابل ولز در لیگ ملت‌های اروپا؛ این980 امین گل کل دوران حرفه‌ای رونالدو بود. البته دقایقی بعد این گل توسط VAR رد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/30386" target="_blank">📅 00:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30385">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBqjQoYRhX4mjY6LURP3wrYQPb5z0bFoGmMqCHKjmwlscpkDU_UCB62HK_qPi98uImTK4ZkRwJfRkSqxeEhweOh6KNrElBOCqsMoJs4dFAbUB7qHkwl12-YuOcZFFM4_P2W12Pi-gvg1IQCLrUoXbAPMj7gYByFGhv9rC49DktUCSmGlUNvs_bDmx7Cj5HZxlY9pWR_ZrekenelvswVU1KZx34qrODw8IAgOzRvEiPI5Ngv4ZPBhFzgJeVhSdfpDRVwqo9Gzre7vjvglvoW8XXvich6nHI5Kjuc2Uh378zJHz3yrnO8kgMLuPobDEBdO5ESqiYoGfdz9W2UvQpXs2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
گلزنی‌تماشایی‌کریستیانو رونالدو 41 ساله در بازی امشب پرتغال مقابل ولز در لیگ ملت‌های اروپا؛ این980 امین گل کل دوران حرفه‌ای رونالدو بود. البته دقایقی بعد این گل توسط VAR رد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30385" target="_blank">📅 00:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30384">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVoGQnWc-vaQxffVXJmA4i5JdO3Ds6zNBtL3fDLZypXnoQ5xrXOUQCu2gaTUNklmCSALoKGFlwK8xIwhKAt1oRtAfuTbB-DbTq0cABP4pK5SRR4u2oswWaTJtHjPtFLCWv74Ahz3Rcf8NnYyI7ut7SXdmDnFG_0z4mCIBWtzBSEQeYD8fJorj8HezpRN6WG6XVLjh7B77h7tIbbOFsmDEj8DFbg9ileoA8_CCGiNMUIA1oWHMozNuGABLYuXq_wsKRuJ5t-MYHmKuSUS4bjXyVgq6AwMjkg8ihrEcrEGxvoY7E9DhiLSMcI6LUqQ2n3s8OfLv0EZTI_QVaU-ytGWYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
دو لیست‌متفاوت از تیم‌ملی؛ لیست محبوب امیر قلعه نویی
🆚
لیست‌سیاه‌امیر قلعه‌نویی رو میبینید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30384" target="_blank">📅 00:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30383">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYJx5p-eCA-sRla8s1fPHJGpgZclL7bsojlYfLb5syycP-zBqRAWuj_2x9Y5qzyvB1gYeLw--YotW-_NoysVKZrsiCRBK4amlnYc72XLj9wjVyXN_6IX15ycd-niLZ_D_M_0hQ181JZLm7xOoF1G5vp83_93U25EEA7pkNQoGZm8720hf7yXOjVfr7ohh4iIeIOx9Ij9Nx8YEJE2Pxm-R9ovf67iE_soFyrljvaUbsoTA_g87ujjZWzVNDo5Ag91RABW2jaG5MAtY3P7_MWWEUHu3KlFsjs4IMf7ucSsLkQ9S0wjPg1BGIFYogb6_dw15ntOkqHRdiJgsuPZQCUieQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحبت‌های تند جواد خیابانی علیه کادر فنی تیم ملی بعد از شکست عجیب مقابل تیم ملی ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30383" target="_blank">📅 23:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30381">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56e908efe.mp4?token=Xvo8gMnR2wyfNDQrQj4V3s3-pjPG9YmpOR9T1VB1ZE-q7RjhxoWWr15EfjFS_68BKUdKL6BXqolJI2J_BO1vUR8p2wExWAL0vSnaJ4MkRczXYfshqhD0sX4ps71FTU7NGTWhDdPwQBk5OVToIA62KhZwQYMpt0e4bVHM9mq1DgUFjzDiCTJBDChrNSsHfzY8GgOoodupICWsyoC4DbQi1v1FU-75kiE4xOk4U497mfEmBItBjkujSNh3DhE5tKe_eq2LaBeu3LLJDqI3VFMshpL3OQ6b1ZOIx-x89-YBDcj3K8SQIkqCwKv1JJqqFFKAD2TOT8MJF--GZja3DVVJCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56e908efe.mp4?token=Xvo8gMnR2wyfNDQrQj4V3s3-pjPG9YmpOR9T1VB1ZE-q7RjhxoWWr15EfjFS_68BKUdKL6BXqolJI2J_BO1vUR8p2wExWAL0vSnaJ4MkRczXYfshqhD0sX4ps71FTU7NGTWhDdPwQBk5OVToIA62KhZwQYMpt0e4bVHM9mq1DgUFjzDiCTJBDChrNSsHfzY8GgOoodupICWsyoC4DbQi1v1FU-75kiE4xOk4U497mfEmBItBjkujSNh3DhE5tKe_eq2LaBeu3LLJDqI3VFMshpL3OQ6b1ZOIx-x89-YBDcj3K8SQIkqCwKv1JJqqFFKAD2TOT8MJF--GZja3DVVJCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول لیگ ملت‌های اروپا؛ ترکیب تیم ملی پرتغال برای دیدار با ولز با حضور رونالدو؛ 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30381" target="_blank">📅 23:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30380">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoJvW06Dy0t0RZXrbdK_w_8mmCQfoIIz0BeGOEVX5EnrQCqq3oWfGwt9Z1KA09UYcq8EQbSlIpguIqlUwbHPWMhHux9HwE4QhbN_2xBYzTN3WmxTowxmQ35K0PdXaqVmBefcxnyQmY_qW2hgSgiFG2U_OmVPeR8e-0yra6QTA-_Nsly6Uifa6uP9XU3eH0J1g5TlJoM0r497JWO8_iUnoTvgkvao9HqlJpXW70R3KeLqb2Z7RICbdHMlW_DrpKvsdXbNEt3x5RgP_OOusMoeN3-k9cIlLYBgy2UXFBgDeKXhH-EcPlD6ZEzQ5KNKyXL1CaDCRVUXBTQc1K6gd2DWVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ابراهیم کوناته مدافع میانی رئال مادرید از ناحیه رباط زانوی دچار مصدومیت شده و ممکنه چند هفته روبه دلیل مصدومیت از دست بده. مدافعان تیم رئال مادرید در حال حاضر: هویسن، آسنسیو و رودیگر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30380" target="_blank">📅 23:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30379">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBvMjVJOpriEkhQ1ZrfdTeGM_9EC9oGezvT0iIeasYFnRLcEIwMhATLnNTu0WnLV07sF5LkG2bQcDzJztR_3O9pM4QIxKCEjvjudMYu2mw2P0ZS23kHcDjH6RubP_y_69LH-Yk4Hth-MtGZ9fhdB1K9cj5tHPjMHy1kCUdVh6snilmuG9z5sOwNZ7lhDklTq9H2mcaueikp0c0Z25y8P2A6W0_mf-jp_biBjHh1KHznrX9gQ_mvNn3pWyZQquG5zml7yPhLj0mlxtEAGzp5-X99JUm00ka3ov5YDzpFyzrkgguEsG7PkluHAUi8UNz9fPFIuxg58QKKqmmhY5aypRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اختلاف برگ ریزون دستمزد مردان و زنان در مستطیل سبز؛ دستمزد کریس رونالدو در النصر 142 برابر بیشتر از گرانقیمت ترین بازیکن دز لیگ بانوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30379" target="_blank">📅 23:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30378">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7pUZXPx1CjpKTEnxYnJpwPYrzJS9XNrHlrQv4bB4r_HjklXvgCfLh8buANdGJRFNMpnRTvHvp0MEF9fy-hrhHrqP_tL8tFhZHsV-EE35MHaGuVU2Ob7L0tHfDSoNyRP32SsIOIn13iXUxmiwdk1Gtsihtx_VPJS_kspRoDWxE1QpXK5vr4MHy8KeEmrqLydJOeUV-3-iTwVlBm4o1N20yF0xRdmJBQ6e0HEMWYV5utSSqbgVTuCCCO7JkjFjninHuKrgR43WPvHtUcOPP7W5b0_qDkaLR4xiRWQUjtzZzwRs70Mfgo3QYktlWRkdKDcx85QY-bXIONDBqNNj0ZylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌برزیل‌فردا دراسترالیا به مصاف تیم ملی این کشور میشه‌. حالا اعضای این تیم به محض ورود به کشور استرالیا بااین‌استقبال میزبان رو به رو شدند. همشون زدن زیر خنده‌. قیافه آنجلوتی رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30378" target="_blank">📅 22:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30377">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af2ff5c23.mp4?token=FB3pFNKYRx86oU2haMu-wIGzvJnI9oWiex0GYBxFpMsu5rQAkkKqKFpTQuYK7Q1pHh09z6auiSDkk6Ebe30YSMslNiXQL7KfskcpBJe5oWpneEH45sG-sfjDppdW7G7KKW2bIYW-LNOnmKArVhRA0OTJSqcJMZkANdzgPhZashKT3O6lC2A-dGlhYW3Scih1q9cv95DZPLgP27c0YnpbZf_gwMMbmpXNLyh_jUl6p3v2v_PmDAeAdZi0iIX5GYlA8JHZfQDjr7DMwbsz080bxtvRGJiNanfVMmX9L4N3xlf4QHJeq1tHEK3FjYdJftiSM0A6MTboD8lAv2-I2Z65LS_v0frEIJWoy0D1h7fS8sncelrenGnRPnuYzIf8qS11kcQklY6HViNp6Vu1p1Xg-OzMebZIM5eqeneI_xLH1eBI-53Qu4n5IgeYbOH5L_AoUHsiMSSdUd73kAtXN5J_jjuYGoKx6JJnI32oIRZ2S6YyIW8lo4GxfRVlUA1VlHbQB6pMC3yp9WQhTVsG0mBEJO9W_yWCMhej0ElcPuyjQ42RuR09nRQFKxiwg7_GjWiIlvvzYeWh8OWBglFcoStiRhJNFr8dMQCjjivLjI7VDLfj8RTaJo0TDhzGI-EYMki4QrCoyCFwaL1yjOvK9HPV6dPlz24fVc0JVEl_WT_u0t4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af2ff5c23.mp4?token=FB3pFNKYRx86oU2haMu-wIGzvJnI9oWiex0GYBxFpMsu5rQAkkKqKFpTQuYK7Q1pHh09z6auiSDkk6Ebe30YSMslNiXQL7KfskcpBJe5oWpneEH45sG-sfjDppdW7G7KKW2bIYW-LNOnmKArVhRA0OTJSqcJMZkANdzgPhZashKT3O6lC2A-dGlhYW3Scih1q9cv95DZPLgP27c0YnpbZf_gwMMbmpXNLyh_jUl6p3v2v_PmDAeAdZi0iIX5GYlA8JHZfQDjr7DMwbsz080bxtvRGJiNanfVMmX9L4N3xlf4QHJeq1tHEK3FjYdJftiSM0A6MTboD8lAv2-I2Z65LS_v0frEIJWoy0D1h7fS8sncelrenGnRPnuYzIf8qS11kcQklY6HViNp6Vu1p1Xg-OzMebZIM5eqeneI_xLH1eBI-53Qu4n5IgeYbOH5L_AoUHsiMSSdUd73kAtXN5J_jjuYGoKx6JJnI32oIRZ2S6YyIW8lo4GxfRVlUA1VlHbQB6pMC3yp9WQhTVsG0mBEJO9W_yWCMhej0ElcPuyjQ42RuR09nRQFKxiwg7_GjWiIlvvzYeWh8OWBglFcoStiRhJNFr8dMQCjjivLjI7VDLfj8RTaJo0TDhzGI-EYMki4QrCoyCFwaL1yjOvK9HPV6dPlz24fVc0JVEl_WT_u0t4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌برزیل‌فردا دراسترالیا به مصاف تیم ملی این کشور میشه‌. حالا اعضای این تیم به محض ورود به کشور استرالیا بااین‌استقبال میزبان رو به رو شدند. همشون زدن زیر خنده‌. قیافه آنجلوتی رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/30377" target="_blank">📅 22:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30375">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuQaArC7Sv_ksnSdZnXUWNL_GG1UlkfzoSAlVoqaQww4zo9NyZly1ZYcY1QnhooZr5AuNZwe_hMB1Rc-VXbS0QJOE-kfeI6nbUPM6s-CYEdPUduLyq18AEQDwJ7C6sW5M6xMNmYOgn3u9hNDWbQh81rOceZQLhYwVaSi5DNfG_LpRtMgBZ8M108KRdrilQZWgzCXB1Qg2YSgp9gIuJL2GtatZ4As4XsrUBHW72Se2l-EBzVH_UfWVx0Y3nowPVQPu3B0-DQnyJ2ZpZJp3-zuInyKy2i5JBOvUl2CNko5voKpzVscaYjI9pn9TgTv1KxnYpVyxKQzheqwF1Rxw2EtRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mr4uiRKI6yW_2H5Y_HU_wUNoM-UhE8CF5t1BEjFq489Acn2ZMlMDoU83SyUfsvn3k6cXyTAVat3dkuiKCXbQlkZx0m-4BUD0wSARuKSBRg9AvhOPTgbrd0AoWRDqzdghPUrbOs0xrVlWPkEhyaShNBhycPRGh3sMAtgU5c-Y-z2OFUW-y36ErVIs2py-dZABoE7azLjssZy5CFgEehMft5wRFn5XSm5dVlfge2GJcuncY2u65GnJ3xcp5WGSl_TYtgxVnBElUtGGQjeWaxjW-QpdFMbyqKfL7hs9Afn5Pn04D49m3us8vVLasurm3hVMvHRW6NYQUfZNtRpib9aWZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول لیگ ملت‌های اروپا؛ ترکیب تیم ملی پرتغال برای دیدار با ولز با حضور رونالدو؛ 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30375" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30374">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxcibcPWsgHmVBrHPNsAuoa3eBdhgV24gLYal6dRyExLj37XAsQ1iZ-EnGCZJyqdHdVNtAaqKSyZCBBCYOn22U5titW0IQp3mlv5IfhuXnfMsltPFTDBB8tBkz3Cl3LzRIYo5wuzG2zBFG7PXPZM5am8RubcAmsh9jjma9q5isdO4bsOr10NF4usCHsPrwxUsTvmKVr1qdNHPZAUDJ_Yr2Z1iv1mBMtSiLlVXJ1Mz4nliVIBWIusT8a53DwOVR0fjQu2tswMsXF5EWp08u32fhZZW--D6mBnHznXXo7kbwwiki4PcZTUoQ398wfLjIGtxwGAXWGurg6u0wj30rvqVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ گزینه اول باشگاه استقلال برای تقویت خط‌حمله‌آبی‌ها فابیو آبرئو33ساله است اما درصورت عدم‌موافقت فابیوبرای‌اومدن به ایران در این شرایط خاص؛ گزینه‌مدیریت‌مامه تیام است که‌رابطه نزدیکی با حمید مریخ ایجنت یاسر آسانی نیز داره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/30374" target="_blank">📅 21:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30373">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWoXIClakIaZ8KTonmLSKnMV32kRnBzM5lnBlCItGWJymue8YrxCb8N2zazJkKXUfBuYgXT2DFjAFMHh6z2AuddfUcs8hdbWxFK_tumuniYL02Fz_AFgGjvNzj3S5vM3RNOK2d8lO7w2nKl6cbDlVSqAhyaiXyxKDdBUPoHg7L1RxrMwL0nqRC1wgdT2ylimL9I5D2YnBsjLYUEX9zygiSLXEqrokkyTwytawHwG4YMjkHqKM4amXjgARVNdVtKLdwu9xxRGzaUnF9lUa609UUjxg6TFBJh0mWr6r_vb0-1hoA9hn3C9O1zqYwAYrlDzrQ9fR0Hl00eBMFm3qXK_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جذاب‌ترین‌مسابقات‌ملی دراین فیفادی؛ به هیچ عنوان این هشت مسابقه دیدنی رو از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/30373" target="_blank">📅 21:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30372">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🏀
پرتاب‌های دیدنی مژده نظری ستاره تیم بستکبال بانوان ایران؛ با دوستاش شرط بست 200 دلار برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30372" target="_blank">📅 21:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30371">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‼️
صحبت‌های تند جواد خیابانی علیه کادر فنی تیم ملی بعد از شکست عجیب مقابل تیم ملی ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30371" target="_blank">📅 21:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30370">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‼️
گل‌های تیم ملی ازبکستان در بازی امشب مقابل تیم‌ایران به این شکل زده شد؛
گل اول روی پاس گل دیدنی احسان‌ حاج‌صفی37ساله، گل‌دوم پنالتی دادن بیرانوند34ساله، گل سوم فضای خالی شجاع خلیل زاده 37 ساله به بازیکنان تیم ملی ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30370" target="_blank">📅 20:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30369">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiTxofk9b6qjaKb2x_osGMvtG40riuuKBP0A0aM950H9-dJWoY9QW9XKg3GQbymL0KAguHKlQRzkvnQ2pwx-m7R2yxmN7RRSeCKbGZHfmd0ScgOegDdoMu_0oa6w9uoCe8oZFfzlY4quycT_rRa9NlCcsxbWITdNDbQPNclFLRgLLJjfAJjmxzGD6m-QZssiadsBL2eY8VN9ED12r12yok_-GMz0nukA3lgbE-mHLV5Mm0Inz_CtCo7IiaenMt0LFxWMqjGOoMjkg6PCCsbPCyoxlH7YjhdvrPG8NVb9wLncRx3qqDV1-0QukJL0vXRlBKbj0ty1E3nOdaKtZOwSmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در روز پیروزی ژاپن و کره مقابل حریفان خود؛ شاگردان قلعه سه تا از ازبکستان خوردند. این نتایج بازی‌های دوستانه تاثیر زیادی رو رنکینگ بندی داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30369" target="_blank">📅 20:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30368">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇺🇿
پوسترفدراسیون‌فوتبال ازبکستان بعداز پیروزی قاطع تیم ملی این کشور مقابل شاگردان قلعه نویی؛ پیروزی مقابل ازبک‌ها به حسرت تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30368" target="_blank">📅 19:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30367">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfConfCv2dxGqW6LIqXVs4ZGw4OuhuK9M9d4JoDHdYdVqteLNJPQ-qdWpg3SA-io04UU_jd0m3Z5tyRu9O93eUiKJtor_FSx82oXu_q9sIqnVmkRzAfB7iQhhuV2PTGTjCE2KnHuLGRthWCBzQp2kARvwdgJcb_A71iu9JmDB6fBsQdjwOmfgjLx71QdVBMmmbXQrYkf3dtIQrTsAOB6uA7WCFIEJTNcPGg-yB0oVP5gksDXcq9qrZh0WJqXmUbg26TPYI93NLznHjBA44_Z-C3iwv96NrVXLP_j13nGKopK6sgA7WUxW5GMyVievRXzUdThIpBCIKuG-kpD2305JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
پوسترفدراسیون‌فوتبال ازبکستان بعداز پیروزی قاطع تیم ملی این کشور مقابل شاگردان قلعه نویی؛ پیروزی مقابل ازبک‌ها به حسرت تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30367" target="_blank">📅 19:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30366">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYGVr1kM1SR20o_XdWIdZzKDWWMKQXxIKQz86L1zlnDfwaUmt6Flyr0CaThlGlFcI2mD2oKPtPpNOxqfCLtXe_AwYYRpLO8yHwYZpd_yMK26e0tO4Cb5vp4NAraKuYxXMI_I9_NR3MQEK_OOEzbF_EJGRZa4lc9z5mspYwBL2IdzuuhEenIv8x4dkXo02Hsxq4OcjxzkBiuHk_TP6JUtb-lSra6SyNaBmYwi409k674l0nZssb7zm5K_Jezp-Qjb7a_TiUsGjYgwbpVhX0tvwbiIqtPl6iNAx046S4q9UXStN3mJ_IJyTAY4jxZPJ_LDB6owC4hl3hfJOyLfDeebJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇺🇾
نشریه اسپورت: مصدومیت مچ پای فده والورده تشدید پیدا کرده و او 8 هفته دور از میادینه. بدین ترتیب دیدار حساس با بارسا رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30366" target="_blank">📅 19:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30364">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMzKV3ZC51HJQVvPTF4T1SM5GOyKKv7QTpQG9L5dpxeuif-huxEOgnQrGYpHiBa36c1XaDc9GYuwviUIqWBm21fhnM0_9x5xT8hHB9gpJubi2vGjp7c8K9i4Kx3n6KfMbsUNK8ck-zqs2MOaZDl1ya-fhWxQQJO7S3h_O3suhxpmDpnrL29ViqQmCV3vDBCm9OfRDzW3h0xzfsKIHN1uD9yNPHNfxCWLITzJjnadH37ny4moF_MKkyLs427aZxTrRUI_xP5osotAWvk40m-mzTJCUXnKJPvtDQiSCsqDTdJQVldEuElOpaJZgeQevGzAHJtv0YG_bOZaGsDHDPiNZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
حسرت ژنرال در پیروزی برابر ازبک‌ها؛ گل سوم ازبکستان به ایران توسط نورچائف در دقیقه 95
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30364" target="_blank">📅 19:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30363">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb08c9fd45.mp4?token=goBtxFKldw-p8eMUgU6jkv0xR5wAFsAS-gbMXxIwhwz83Yta4Qfz35trH6p37TEiL4lcZU9NngGSErJ1yeF7-Q5Wo-3TxxUMQFtisRsuUWGipnXUETAfaK3ITbmONtIDZinUqYW4_l-4Rh_LqNJWFBCFGOPG6TaQZBB3_XvYc6qeUFgiWEDAHN3ogdPpl0HdwFsB4L8UEdfJn7tHJynr79OvrydPmxjK9vF3mA9XLvXreyQOwTBNPza5Zm7Eda_r3rHNwoYz8p01M9RAv2sQqjzb9oUmMoQUHUiFVuxRuUJ44serCcBkG3jyWjst7eN0iNqf691Rw4HhtDyCIVsqKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb08c9fd45.mp4?token=goBtxFKldw-p8eMUgU6jkv0xR5wAFsAS-gbMXxIwhwz83Yta4Qfz35trH6p37TEiL4lcZU9NngGSErJ1yeF7-Q5Wo-3TxxUMQFtisRsuUWGipnXUETAfaK3ITbmONtIDZinUqYW4_l-4Rh_LqNJWFBCFGOPG6TaQZBB3_XvYc6qeUFgiWEDAHN3ogdPpl0HdwFsB4L8UEdfJn7tHJynr79OvrydPmxjK9vF3mA9XLvXreyQOwTBNPza5Zm7Eda_r3rHNwoYz8p01M9RAv2sQqjzb9oUmMoQUHUiFVuxRuUJ44serCcBkG3jyWjst7eN0iNqf691Rw4HhtDyCIVsqKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
🇺🇿
شاگردان قلعه نویی دومی رو خوردند؛ گل دوم ایران به ازبکستان شومورودوف در دقیقه 58
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30363" target="_blank">📅 19:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30362">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oyo32djSIRXDBw2pInj24TsWuRnuu8mhbzLdDbspDQoQkic_G1ED-Qa7_agjCPx4ye2Dfq0T-PXdZT-Slx91Z4NVnPqxmFvE_LCiwU0MtlamfzovtG8_MtM4A6iP37ERb59X86oWYQuxCC_fbzBXIXCL3EWlZkQBvNMvYuBMluZY14vTWkxtmkREK4LZQzTuU-UsgqNv-QeDIlbuGeVRVA-wDJ1Ecz8PT-uWmv5UYZAVBrTkjCBUu9peVwe9G-dw2O8BjYJg95LUFuaEqyeBdSkr_LfbxNsHfCIOzI35fS4-mq-U88-ucvxW8mp1schW3EqanfzLx1rpMvATPenkPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
🔵
آیتک سلامت و یگانه اکبری با عقد قرار دادی یک ساله به تیم‌والیبال‌بانوان‌باشگاه استقلال پیوستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30362" target="_blank">📅 19:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30361">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/401621b710.mp4?token=iknlnxuYHw-4zZ-CvGN0PSlH8kFRwbEpNZeIgZuMc0OdKNjO_c_8_UlL13B_ysZopA69DNeL4aclTNi3PAosmKxz8cRx3SUheOcNgD1DKfdJuDEAQf3wqVQRHnew54FceIniw0yfvWOP_-qaWzlsXh5LmED-JNBMiDhCDoUFjic1U2zSk6sEHFS9QRhlmcxbEVqnaXZhV0zIDquKkoSF4ushhvOje51teQLRh5EneWlMVsZ-ZN6WuwWIHKgxjzVxxu3x0ukdL1mOQi-fxCaGxWL8fYow26kC4KaJz_QhziGL1yj6VklkIQKjpkz98u37A1XUmrHF2b3ZY_3fNSIM1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/401621b710.mp4?token=iknlnxuYHw-4zZ-CvGN0PSlH8kFRwbEpNZeIgZuMc0OdKNjO_c_8_UlL13B_ysZopA69DNeL4aclTNi3PAosmKxz8cRx3SUheOcNgD1DKfdJuDEAQf3wqVQRHnew54FceIniw0yfvWOP_-qaWzlsXh5LmED-JNBMiDhCDoUFjic1U2zSk6sEHFS9QRhlmcxbEVqnaXZhV0zIDquKkoSF4ushhvOje51teQLRh5EneWlMVsZ-ZN6WuwWIHKgxjzVxxu3x0ukdL1mOQi-fxCaGxWL8fYow26kC4KaJz_QhziGL1yj6VklkIQKjpkz98u37A1XUmrHF2b3ZY_3fNSIM1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
کاشته دیدنی ستاره 36 ساله ایران؛ گل اول تیم ملی ایران به ازبکستان توسط رامین رضاییان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30361" target="_blank">📅 18:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30360">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6b255c08c.mp4?token=v49CIZ_DmrFaMBQQsC6QbNY0FY9Ykl6j43yTkYBbYp4RqyJGBF2NJDHIM1pDhd1WYDeLmvvnY3k9yimHm2HvXEjZzjocMmEMPE6IEdcRq1nShYPz2yHoLuUk-O0i48NMD0crZm6Yzo9vrp09hqdUNE5VURF3-e5IiwE6z840-6bF3_7BJgTaoloO0P2nx3WP_mPjPf3m-Gijw0MYQ8Se2ZTcjR6guIxamHpSd2BDJ2gMZcPPyfzgfy3drQnn_hs4tVsWuIZY6smhlPmr7-SB0ITR0wtA09O4AUvMWrYZT5F8Rd_eRtCUREi5XMI_zufSKK5w7VQuBgYyLd0xS1K5qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6b255c08c.mp4?token=v49CIZ_DmrFaMBQQsC6QbNY0FY9Ykl6j43yTkYBbYp4RqyJGBF2NJDHIM1pDhd1WYDeLmvvnY3k9yimHm2HvXEjZzjocMmEMPE6IEdcRq1nShYPz2yHoLuUk-O0i48NMD0crZm6Yzo9vrp09hqdUNE5VURF3-e5IiwE6z840-6bF3_7BJgTaoloO0P2nx3WP_mPjPf3m-Gijw0MYQ8Se2ZTcjR6guIxamHpSd2BDJ2gMZcPPyfzgfy3drQnn_hs4tVsWuIZY6smhlPmr7-SB0ITR0wtA09O4AUvMWrYZT5F8Rd_eRtCUREi5XMI_zufSKK5w7VQuBgYyLd0xS1K5qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
شاگردان امیرقلعه‌نویی اولی روخوردند؛ گل اول ازبکستان به ایران  توسط شومورودوف در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30360" target="_blank">📅 18:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30359">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8206bYZCSenKdT-CA8IY96xa4oMX2N9BRYNZh7j-MfaGvm6BytEbng3JtBsyF0jhTWRBdqm62N7Ep0NdxuAFPnMVdmETEVm2p9aB13nAzZkygDrIWXforGj5r79UJMGpkNv7_cql1tUcNWMWwbCq99AXS2D_SYt_5_KRDolWjdaBLPDy39f6hvPNTYf4oczV-AsuyB4yCAPlD2FBL6fiOrd3LpsAYjf-2jUAgP24SlF0yZI_IHvNg3ntmI86RtiLdsWTZZ1oKwhS4cB8s0uHTxwZeYoBlkEW1ur0rsyRMhYvmfirWRyWRQLmS3IwxB2GW2B0qWrYW7ReE_y0KYaMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
شاگردان امیرقلعه‌نویی اولی روخوردند؛ گل اول ازبکستان به ایران  توسط شومورودوف در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30359" target="_blank">📅 18:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30358">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1995a5be8a.mp4?token=twU-QSO1tD0H2CyanOkwW1rMHRtT8zRuKn72QDosZSuMyA5EZIkjuY8SVzgV7OhmsamwTfeNUImEPsh5RBTdXeZsWtplg-wSSzwa36e7tCMpguhYX3aFHQYDo88LTwULcgLeBsaoZPk3pC-ZAHAVuKpjCvGw_h3qbGyClYxafC2wqkl-ZMKtFaUaifz_JM12PxU-uVLoOzxSMRl0BpEczkVE9pfVEDD6xEHfo6rgtuAFNY1lJvQ5a01t_BVE0KQJJVR9K5NaYGFczMJRCIilDr6RFLYQINHA_EYHSVQKhCYFRreGWyRuO4xHIhy79hYVDkcK8kfz9R210IuNQrRugQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1995a5be8a.mp4?token=twU-QSO1tD0H2CyanOkwW1rMHRtT8zRuKn72QDosZSuMyA5EZIkjuY8SVzgV7OhmsamwTfeNUImEPsh5RBTdXeZsWtplg-wSSzwa36e7tCMpguhYX3aFHQYDo88LTwULcgLeBsaoZPk3pC-ZAHAVuKpjCvGw_h3qbGyClYxafC2wqkl-ZMKtFaUaifz_JM12PxU-uVLoOzxSMRl0BpEczkVE9pfVEDD6xEHfo6rgtuAFNY1lJvQ5a01t_BVE0KQJJVR9K5NaYGFczMJRCIilDr6RFLYQINHA_EYHSVQKhCYFRreGWyRuO4xHIhy79hYVDkcK8kfz9R210IuNQrRugQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دیدار تدارکاتی؛ ترکیب تیم ملی ایران برای دیدار مقابل ازبکستان؛ ساعت 17:30 از پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30358" target="_blank">📅 17:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30357">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3181370a.mp4?token=Z6DD6jR_Nw-0eRsOMsmRnyQ_Act2_9Om884k1b7jq1UM7fpUfWorikuM3hubHPqk9NOwnst94Mr8CLKo_tigzBjjMTcjsSDt_wiIItyhCCQytSMnzJEMdwgCuNshXV4uqVW6mW1gk7kGm3xSLZkY8CObPcXRj2mNR3Dj7bvbLBCEwriMxwbsmDNmPgKHKDRxdYxfDNvMtscr9-p458V3ZpKsGcPOueGPK-qF5kGeCi5dHXPxPryAibF0YoYtDuwyG_uMmjuR2nsV_Odqsy6KeW-5krMW3Pa0UMikMFaw8EwWw0M_H5EPK6tsGHcOz7U1v56Kxtsz-n9mMjTL0oZQHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3181370a.mp4?token=Z6DD6jR_Nw-0eRsOMsmRnyQ_Act2_9Om884k1b7jq1UM7fpUfWorikuM3hubHPqk9NOwnst94Mr8CLKo_tigzBjjMTcjsSDt_wiIItyhCCQytSMnzJEMdwgCuNshXV4uqVW6mW1gk7kGm3xSLZkY8CObPcXRj2mNR3Dj7bvbLBCEwriMxwbsmDNmPgKHKDRxdYxfDNvMtscr9-p458V3ZpKsGcPOueGPK-qF5kGeCi5dHXPxPryAibF0YoYtDuwyG_uMmjuR2nsV_Odqsy6KeW-5krMW3Pa0UMikMFaw8EwWw0M_H5EPK6tsGHcOz7U1v56Kxtsz-n9mMjTL0oZQHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوخی‌های‌ بامزه عادل‌ فردوسی‌پور با لهجه های مختلف اللهیارصیادمنش‌فوق‌ستاره‌ایرانی لخ پوزنان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30357" target="_blank">📅 16:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30356">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMAI3wj8UCvPGp74KPISoL73TkmcDx9Pkk-xz6u7gZeElSsdvNsep3P4CRB2hLBeHefMnBqUZc2pFoj9bJCh5zljnrO3KR6Njjml030rxQYLeEQZHfOyTAS4dDkwgRug0esajyz_KkmizhVVtnC1aO7ye9YrnCSv8sKIhLKJq5uZFiqUWTPlncFtbBX3Usf22eSH2ZM3HeSd4gGrgUiRYaGooodJiRxFV8OCDZ5QeRY3cqlc7LTbnTJ7eX6If_1HEwDenwRSQpATBjQ1YVDNtkwWfBWqK6f2i5HfgCqXY8LegWbJQqDm3C4wmx1fLwQ6gR-IcnRJbjZ5dSFITts9qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال قصدداره که برای پایان دادن به حواشی پیوستن بیرانوند به‌این‌تیم؛ قرارداد حبیب فرعباسی گلر28ساله خود را در نیم فصل به مدت دو فصل دیگرتمدیدکند. محمد خلیفه دیگر دروازه‌بان 22 ساله نیم فصل به جمع آبی‌ها باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30356" target="_blank">📅 16:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30355">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ko0h_WcLKO9jzRAXBIt9ACujZoCp2vh8gC9HEVsc_sEJdug-VnAddZyyOszp4QAAfqck1ZJjK03_2nmFKPRyhUgZSjC3zEQh2ga5j-08bcaxQwhuszgAs8o4d83w4J0bspJuLYwSFDGSRd_E33IfAPjvGSuKNJ0mT3_1foRND8-L0_y1nY-W_YXr4sOPusWIpDQRY6IrqRBk6ZW_gmir1jqnUknBuB6zRIqReLA5LxWYj35M4DGqVwELeZ6AJIyunGkhz6drMZWSaAx8PZ4hzP_sBNeN5-4X0GmMi_D-GgFH9263AWvvLDEKz5t8gHVBFiLZst-PKKjhiK_m3QI6Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیدار تدارکاتی؛ ترکیب تیم ملی ایران برای دیدار مقابل ازبکستان؛ ساعت 17:30 از پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30355" target="_blank">📅 16:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30354">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c61f1d20ce.mp4?token=dEm1TI-JzyUHwwjzoZX6WuS4Zs8XWEMZhCsm89fgYgKtwOnwF6HDytG36o1vflyxOK0ez0ln3QwsxDSz5-6L2URhnS4gjPdT-EWomUTsmOPWEuw6z8gX-FRcRLe9ViSlrEQKkJ1o_lwZbUiEFXdAzaHLb2y3XH3almeOJa3H84M7gIoJRcV7K3e_h0MAeblPwFyHbAqmAbKeBFUN5PfJZQXjDyLFwyvfzaBPfM74rF_drU0wPFyECYa8XFi5ENlLKPZBtie662hiJ8t7npopgiGugBotrGSGiPg7gdPKqqpXzmtju1e6_AqHe3UroR_DcwxojdR7njGTHLx27dGVzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c61f1d20ce.mp4?token=dEm1TI-JzyUHwwjzoZX6WuS4Zs8XWEMZhCsm89fgYgKtwOnwF6HDytG36o1vflyxOK0ez0ln3QwsxDSz5-6L2URhnS4gjPdT-EWomUTsmOPWEuw6z8gX-FRcRLe9ViSlrEQKkJ1o_lwZbUiEFXdAzaHLb2y3XH3almeOJa3H84M7gIoJRcV7K3e_h0MAeblPwFyHbAqmAbKeBFUN5PfJZQXjDyLFwyvfzaBPfM74rF_drU0wPFyECYa8XFi5ENlLKPZBtie662hiJ8t7npopgiGugBotrGSGiPg7gdPKqqpXzmtju1e6_AqHe3UroR_DcwxojdR7njGTHLx27dGVzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
انتخاب قابل تحسین آموزش پرورش برای مراسم آغاز سال تحصیلی جدید؛ خداداد که الگوی خیلی خوبی برای بچه مدرسه ای هاست امروز تو مشهد زنگ آغاز سال تحصلی یه مدرسه رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30354" target="_blank">📅 16:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30353">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ دوئل تماشایی هلند - آلمان باتقابل‌تماشایی ژاوی و کلوپ درهفته‌اول لیگ‌ملت‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30353" target="_blank">📅 16:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30352">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cU_nn_jSpRxka7FvhWlqax_45WvQoQPAj-ljiTbMxENG9rLrdNTg1-waeXPojerhJHt20iTiOScTFAMofvSDTab10E6Ia6D_uClRMSO6M6wRgIKjQImUt5lS_A_At_Mb7TZVXKGsSVgLldf9pX2M4ikVUj9wkUVsy202YVlLiXWdMTIqFgSuk1FnyhDius8Oom6onJcJA_GGhK9nzTbrqel2yRV87UJiyLadoqgOpYYIB25b93m9270Z6wnUyTzs-M5pXPqqJ85YJb7ufvSpsvT0JJH9gw9CPJ7QwFAImlpZ7aLD47fnx7bTdkC0KgbU9X4CN7YAwYe8AT3npZT2bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دلیل خط خوردن قایدی از اردوی تیم ملی توسط قلعه نویی رو میتونید تو ویدیو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30352" target="_blank">📅 16:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30351">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lP3O8zE4Cyh8WqC2qC7eTFLUkNTfpHHPBRT8irOoKDGPnUsKhQhiPMm9JNL8808vEQ6vC0zca53OuSQzjs8G_jMbcr8edRayb0etBxkLXiRmPEXhTE9fPGuKD6Ty5Saw-STi-06gPha95VzOzoJTAkURz4Csu_KjUYIb0fC0NL-SLXVPwMCN-K8XLsEhtMUvVtUOM8p3Ea4K_emVs7t4S9iA7_qbEmXW7Jwj-70PVRRGLcVZECFooiojN951g01jUeHTYYgVxw5XslgbztSCruZHt9XLxkdqv9GrrQm28DI4PeWv-3bAhoMGV99JrhBn_HNneLWUCDCAPGwT_c_Hfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
یامال که قهرمانی‌یورو و جام‌جهانی داره:
من دوست ندارم برای بهترین بازیکن تاریخ با پله و مسی رقابتی کنم، همین که سال ها بعد بگن یامال بازیکن فوق العاده ای بوده برایم کافیه! ۸ قهرمانی لالیگا، ۳ قهرمانی‌پیاپی درچمپیونزلیگ و ۶ توپ‌طلا برای پایان دادن به فوتبالم منطقی به نظر میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30351" target="_blank">📅 15:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30350">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTC5EPzT8ZkVW8jy84HW0NfzrjZsa7N8kYdd_rxhx2b2vT0-OBbGxD8ERyVbFvL8fPie0LakmW_CHXknhZey8HRwal5mBwh7KbGO_wuXqqKL3nidw5M9O9gk21N2312tPBfkOKTrqw3QJh3B7snRDIerqiPWS8LhMDAaQUEzvMJ3Cjxjfi1ZqHYLfJg2SsuIjlI6O0VsXiDrBUwOm6LI1V7LqheZwZ4qIe4xcRGpv1EFdy1K0S1IcOoMuLGO9DPEVo_XjUWnBy7B8VWNtaqZ6D57f_jwRRT6DBWQPevCBh1Z9b8qsKbEzYwWshYif9-3ccM694vJwu16wA-F5VlnWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گروه‌بندی‌ فصل‌ جدید لیگ ملت‌های اروپا که از امشب استارت خواهدشد. این فیفادی با فیفادی های قبلی خیلی‌فرق‌میکنه. تقابل‌های جذاب یورگن کلوپ، زین زیدان، توماس توخل در پیش خواهیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30350" target="_blank">📅 15:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30349">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBOV4CNErWJiuWxwQ4739HjB1PSARR2Z6aZHLL10ug0SxscCNUAPrAVy_bC7CA7BP336J7eX6BEHtrduQiJwgi8FYfDhBoSoLzJZe7Omb8a-ypwdDBlxarSteiBWEYJ1_yj1u-Wy0-kJDWaC8Y37qoiZE0IICyL-uHrvxDED0opBFTT0ob76TpMXT-9wgsftpQzFHkoWzcjE9Es8TJ4SWHk8xIUuandHpLW7i-zRB0L4vNVA6zFDqYz8z4gY7IjEfwv2mPrQkbIgLtpV9F7lPA37oqkHpcgWcsUMwUAlG4NX7wxGlpHHRt2fpPcdajPaGhEeXOoA-zjWKWrpNgcfgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ حسین خان عبدی بعد از افتضاحی که دربازی‌های آسیایی به بار آورد بزودی بعد از بازگشت به ایران هدایت تیم ملی امید برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30349" target="_blank">📅 15:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30348">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgpzTaQptxoEmLfSpJBIQ_Yuubk7FZ_H8SYsKcmsmcO_iyZmCJfbiEHhYR7Ovm-FKfAMABokiPTMuqfj1sollC_T3Gr5U38vOOF-r8-M6JvroydTe75wtR4G7kgWmTHcLG_zkJzk_5tc899t8uIh_nOClBr_4meGEjqQjl_dafLP4zxaBAO4hieg802sBzH1Bs9S5IYThr9kbUkMh_uMVntsiZVJlRIo1uuPaDN0mfu9clsLyk-JylJyu34uIeLSGQE8nOPu0jlhDAda5vFJjeVXS7O-tMpSkg9VMZr3IlCUUBo_ECqZUBucq_TvXxZVfB6re98iZ4H7lvIeeKnIMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
فصل جدید لیگ ملت‌های اروپا با یک رقابت جذاب آغاز میشهه؛ ارلینگ هالند با نوزده گل در صدر جدول گلزنان تاریخ رقابت‌ هاست و کریس رونالدو با پانزده گل او را تعقیب می‌کنه. رونالدو برای رسیدن به صدر به دنبال هالنده؛ اما مهاجم نروژی هم فرصت داره که فاصله رو بیشتر…</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30348" target="_blank">📅 14:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30346">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbyX_iaLedwIY0vGlD-SUnPehJretP93rZ81qohAQbpjWBqL9UYmnjnv4zCapWQFDd42f0XJpUMgNBioz5UunWlG7M3giv1Inq29Y5HvB_6iq6vKH6TXX39ywlCnxwqxH_6ODTcQ8skSK2MucNrg6ZbNowMNnqY5LueNmo46Rd-S18BppQu5PGnTQxhotrGCHrPiTY1OzoFZua3h_JoX0FNFBmfAY9--BDn4cSgrkFB6eH60cF9azqpa_PP5Emo3p2VkLyO5DuvYPdk-peEpBSbdc5dq7PetUzH9FVmLfGReOZINrEIyW4Vm-Rc37UGTFsTjQyYjxxF3_hlVDXc4IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد خیره‌کننده‌وفوق‌العاده کریس رونالدو در سن 32 سالگی‌مقابل‌تیم‌های‌اروپایی در چمپیوکزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30346" target="_blank">📅 14:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30345">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1kKGMkMp0ArR1x0m5e5ftepG-dYARJqnAy91lxFTe-KiJrFYOoj3wioOZn8VS6qeHJXudbXLH_kAqYrVnYMcwEY5PWTwW8ZEILgCwN05xD-le6fFhiViVPHbOWgVWTCmYgqJS3Bxwu5c9AzhNm42PPupKMbJhEjzEi5hAO_BHyz-E7kGM45FIACMS46nUSoSCHwn_FVYpiihx4KHJuOJkZDqsXNOWEdc6NwIlG5unIFtCNoTX55BpIKG1XL5GNWNb45MsNEczq0OydLIXSrbPK8LLp2ighDxEztRaVu7RVPwrId151J61C5_qCdgzAr6gA82mZSSErgcARMsOG3mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعود بنیادیفر بعنوان داور وسط با کمک بهمن عبداللهی و فرهاد مروجی نماینده‌های ایران در جام ملت‌های آسیا 2027 هستن. علیرضا فغانی هم به عنوان نماینده کشور استرالیا حضور داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30345" target="_blank">📅 14:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30344">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6MpdsU9frSDJ3J_HRgahwumtABoRdiXZH2m08JUH6U1MNkAzMBKIgqlJhWTZsKRKKxLPWKC3kNpS41Ou0zK4Qv2U9HOYz7HJDA6w52v1hHdiRGvj2zqAFWpmJrdsFEAwAvQ-yNvN6oX5Tw2J4yRSaAg41ZltUfJODIm1A_f8FJJYg-tZVi7dXvnzrumu_8lCRwI7fe7HeXUWKrmeMLIl8hFreJtCb7JJ2bbWuavNG3aYu0AwkD56FBSQ5xUfGO0fkfB_nMzV8izlA1Tev1n9NoPoDDJ0qhhN7EQyegRF9JOMzqkNaTSzhy3UWgsAB05YTGYny0U72svvI0VHk2xuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیدیه اندونگ برای‌عقدقرارداد 2 ساله با باشگاه تراکتور درخواست دستمزد سالانه یک میلیون دلار کرده و اعلام کرده هیچ مشکلی برای بازگشت به ایران ندارد و حاضر است با تراکتور قرارداد ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30344" target="_blank">📅 13:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30343">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMDHZG92Xyg8yWcdv8igWj5M0yhbclVdXGGlRIkDF0qmirS3WRiHsIKk5LK6Fcs4DwMhUVazT1EaTIRyd3e07xLylQa8WHsr2vV9KAhqgSPp06g89enlkN4Tm4w35rxkUJeCyQOh43s2E_-5cZyONPqSLRwGQ_cFM3a0b51qjiECohfTvDZ1no-XmSwV2-a0V5jnCh53ETXMzJ9LMOAcEPRqizJ0NR_fiyVU5r5zQC5nlm1in1iwnP99Z0nvm4x5O_CgONllzsZGX2xmak0oAxlIlSe9MPtDp8pvxv9g2M8EJBDmqmbMakdnB_XCOvjNgwBNp719PoW3oQpflvNSWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
تیپ و استایل متفاوت بازیکنان تیم ملی فرانسه برای اومدن به‌اردوی‌تیم‌ملی این کشور برای فیفادی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30343" target="_blank">📅 13:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30342">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnmTe4kLiWOgEckIfC6AHTktkyettejArpak6PzTtWCeaZZPFoQpn3OXOpvRz8RpMfTyGzE5N6TCQJaAj7o2a7Col7RjlOAtIWnMRfamf6ciquDfk6zHOh92ku-RFB_9w4ZdPVxM9x38-H7uz2dHJ0G6SG3eoKtY1ii1VKYoL9xP4o9WygEWgdqQ161BnDjEHZh2zcJsO5tH_NXD7qTEupJdtQjvFFSyjpS_sSc-o6VVyGOe6OxPKC11fLVIfF1Uxs4m9eGu_wYPHknWQsVux6jbNuggH7QKXBrGdIl7vLbGnVs6Azkl4fxZM1VdpPoaL3jzHAYV8PxuLiVhySTx-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس امروز مدارک جدیدی درباره قرارداد یاسر آسانی به کمیته استیناف ارائه کرده و قراره تا اواسط آبان حکم این کمیته اعلام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30342" target="_blank">📅 12:59 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

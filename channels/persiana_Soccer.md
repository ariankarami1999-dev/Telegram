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
<img src="https://cdn4.telesco.pe/file/JrsEPndXhLSjgYLqJVYtMPs8BKmyyFw6I7YufMwrAmGr0ltk2v91X0R6QEfJP_UaeGn28zUvMlTG0FUF_mH5St4Y4_fYF5xAISMptj1K59NCaCBeUCYIObIal48mL2bcQGyHXLZ_1sJzera8WgmnXupcWYiHwXsoxntCvG2JyyeAIP4oURvC4rqelfBpsMBacRGGXHbuqFnpFfrbQPSEIKAFhtGdilZ8gAFX-EPz-jQUWrHzICM1lYnfobjsc-6_CW5WvkYHpqLqWU6o7R8VHwUJAIbNOtQUKPSjRdu67mw0tu53ahnVKrK2IO8_APifon-X93ujEtC7H1BBwdGFmw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 171K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 00:13:13</div>
<hr>

<div class="tg-post" id="msg-22966">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8bUwpG07T2EG2NMPiq7HUABoNlDxWfRdhRi8jCWPpBeflRg_IqxqpX9BomlQh7p2Ke-0VrO3mMKLBnMUo0PJDTq_eBPNBzEYwLluiPyB77P8nH_J-QVnlwf94q7wcqPLv2YX2XrlqbzQHu2penFyH4GC7VgTCka0817w7ICBEp9uBAMRAoBHaGpUWpcrUEzn8Qerfu_CaHlZPksJtGgcF8gQ15dovp3hH4vLxcBDmX8bQYastY9BaUGgwvZr92EyQY9zwUBRAGshiEBIgAhxk6rKE6LtghYrerS-PwGkldzFVqUN31oH4Wa1eIM4I1gNqkZKe7YwOcJ2WNUJ4I6MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/22966" target="_blank">📅 23:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22965">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGXoc-m_AoLPQ14aBAkM26QvQXEavkyGgs5MDQqRLUud-1tSwWo8hIjlEHOADpEVZsE9HBOvDjXLEI3NLdPkXxd4Qq1Kgiv88xZgmFzaP78xCoXy8wWMPwVEq998S8VYxH__2vZPGKcId0zUxHBTg8Dm0kGeCcNUIPDGebpYnsk-kiSV36rB5XBGxUlj5Kn_tR63bTUXX3P-Gs85aZYl5D3U97ObPzFimrqK5aC0hr2pj6DYn5pfNjxyUZXBfD_FLzBxERqymqCzFdO89VhiLjw_YdtL0ZRUtzefcxWT2XJEhDLIO-FNSAMapWpK52_nObuj5-xV-pFWM8Ikvwb7Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوشش‌کامل‌اخبار جنگ در کانال مردمی مجله 21؛ نمیدونم چرا سرنوشت ماها اینجوریه. انگار نباید آب خوش از گلومون پایین بره. امیدواریم که حداقل نت‌ ها باز قطع نشه که هم اخبار داغ نقل و انتقالات تیما رو بزاریم و هم برای جام جهانی دور هم باشیم بازی هارو پوشش بدیم…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/22965" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22964">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eaff3256e.mp4?token=HMuF_LGFPmdc4-5yj_We-HFtjYXzuz-eYOM4NKKhlN_bQFtVh2A74q4G3Gp0ewFDP4m60mqfe5gtHe9aJgc0dO6G2WE5HSPJXM1P9Iop4nvauDOWOjrH7--cuFszpyigzdC5xIN9Rq5Sy7LvoB_bvxgPV5TU5k71_M6NUhHdbrRANWEMZVFSq7jNFnR3EfpkVuyIKccEvfXwnnkKgboU2YAfy2A1j-lbMkgyAgDC9ZqblIcaog3rg1hCTPY8kiEtnpznZrLGuyVkH2A1YszcGY-KkQt-n8nG_dBghAYw-V5Ef_x-XRDcAihy4ilcsVnHrv3nddwxKTP1oD-QHJmB6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eaff3256e.mp4?token=HMuF_LGFPmdc4-5yj_We-HFtjYXzuz-eYOM4NKKhlN_bQFtVh2A74q4G3Gp0ewFDP4m60mqfe5gtHe9aJgc0dO6G2WE5HSPJXM1P9Iop4nvauDOWOjrH7--cuFszpyigzdC5xIN9Rq5Sy7LvoB_bvxgPV5TU5k71_M6NUhHdbrRANWEMZVFSq7jNFnR3EfpkVuyIKccEvfXwnnkKgboU2YAfy2A1j-lbMkgyAgDC9ZqblIcaog3rg1hCTPY8kiEtnpznZrLGuyVkH2A1YszcGY-KkQt-n8nG_dBghAYw-V5Ef_x-XRDcAihy4ilcsVnHrv3nddwxKTP1oD-QHJmB6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/22964" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22963">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇱
🚨
شمال اسرائیل آژیر ها روشن شد دوباره  موشک ها از تبریز و کرمانشاه ارسال شد</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/22963" target="_blank">📅 23:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22962">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxKUUOK0veXjaU-URZBCmCN2qsl-Kkqt25FbjtZE1hoB-GLVXSDpUgV1zfLTJeUpsCePXtUVxQLwgzo8MrYfdADaxlQdiQicY6AYakBTHuLVcnQF8Sk5BbzRZF3ZemhfswGnuubucQnG3A3FB84w2k3SHiYzc47PKgAue89TgGYU8isMGqgQUpT4ZiVugZ6wZSawgVFF8RKPR5rmrcZMgHUzHrYBH1z7J7nRgyydN1ZSCLm4RWjzQkxRP5DlWou9MTXJUhXku1lb9HVHrS2dlSycRfGEGXRw32w4-k3TGz5IOzso4HEf375nIg31Ls4IhgmKqtALOqkZj5fjMurirQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اتحادیه‌فوتبال دانمارک رسما اعلام کرد کریستین اریکسن هوشیاره و تحت شرایط خوبی قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/22962" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22961">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmMPa18yyZ3Uq1itibpjHMiIt48VcFZbB9LYD0dvcAltfE1RWERzoqCmHRsbqV_90hxJBsSIJ6MUbI1rtEN2X6U9sa-DQLxctjv4PCF9KpsAFFoDtbta3ZrRCwKR_Sq2XSFD6siVF8X3uNAhdEVS11x9u9QgQa9W2S87EwN9b5CRDTGZmuIr46YvCr5oXyzajJoZX9_6i_5yxun7xZ1s2qqgm_0cuz3gIDvtMnCjOhCWQC16EdmI94mlTsxozTztXOBnfvDEHmoIifa-WDhANGSvbQKb38f6ok5-eer2Rw9sjtJH9O2oXgENRXOc8J6KNaZ4OKOZYM5c-9MWf8a1EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/22961" target="_blank">📅 22:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22960">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW5xHiADNCzQQJZvMe8Ie2Ffbs12QZ2h3qkfxjgshjIFejvJrJCCag1QHqNWgG4iTm92T9QgHwc2XULigigZFQQwmSTvVpuviyIyvs98RSm3e3kT8cPiWFa6_kyNvX1efZ0SVBgqNm34UAE8xUEIrU0SXxnBryHEHpeVrbUflyo68I_XzqV_ClA3IhiKfucmQKKymajexekBXYekGQbf-YFcUWrJkHq41gESQQkf_5g1_V5N4OY2UmylrDPcpD4ouK5l6MSNm3FSqTZiQzpRMDnc8lTWhM-2uakNqqJdqme-J2HER0D4yvcdxLnCDxXuJFEc3KXNdwiYEFI9mufRQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری
؛ شنیده‌میشود محمد عباس زاده مهاجم سابق پرسپولیس، فولاد، نساجی و تراکتور به دلیل مشکل قلبی از دنیای فوتبال خداحافظی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/22960" target="_blank">📅 22:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22959">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j32RGU7pAzFhewz1alEYdHiSJqRPqPZ-ihV6kSMrwWszcENa-P3xEfQHcj4i7opAHwwa0iefQmAG-r1IY3IjRUY4dMXsLA053OEUlR3ZeL69RctcZnSwJx0lCpAtQtxl_V8B32D1KWIK8MdAQ60hZn-pP32eyTQKYWlO06J1BRMsdilQO38l5Lcw0M6EwdQL0ncjS1n87HMyCo0Mzc27HaOorjes0Qj4vWQeIpsTo9cjWmmTLkz_PtvQlOQ6hPBkc5_weM2ZsLHOkFMrDs1F5QWARCdLvO9ZLuUrbMU9PswtXk_zU1SFiN2SBcU2j4GFCxG-yuWEZHcpFK6p7RI6TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فوری؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/22959" target="_blank">📅 22:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22958">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bffa01c1d.mp4?token=pPPyzydwm8yWNg2uhDNL0xR9xgFgrqc8NEXNccridLAPP7AU9-9-OlfAJKwcYiO7whEnLxf1fFmcHIkb2g0L8DHTiZx5h9rD9IUZJCUBiD9eaDv48VT2U8-fydINkh3RwOXLYWyavTaLnM2ettwdvHPcK7gAnM1qWEdtjrtBLtsS08-9ln2Qe11mqEeJVlTjHZ73GbGkysEq962Z2IDPdcTjIk9BnutZNxe-XfRHZjRnlXW21JXj0nRYtRo6MDvB47qRllc0PsOuXFdUEUk67DD5QWttvzTcu794Eko0i6vLW_BpWdrA1NBatCyYu7t7tdk1OepF8XADiaARh2QCIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bffa01c1d.mp4?token=pPPyzydwm8yWNg2uhDNL0xR9xgFgrqc8NEXNccridLAPP7AU9-9-OlfAJKwcYiO7whEnLxf1fFmcHIkb2g0L8DHTiZx5h9rD9IUZJCUBiD9eaDv48VT2U8-fydINkh3RwOXLYWyavTaLnM2ettwdvHPcK7gAnM1qWEdtjrtBLtsS08-9ln2Qe11mqEeJVlTjHZ73GbGkysEq962Z2IDPdcTjIk9BnutZNxe-XfRHZjRnlXW21JXj0nRYtRo6MDvB47qRllc0PsOuXFdUEUk67DD5QWttvzTcu794Eko0i6vLW_BpWdrA1NBatCyYu7t7tdk1OepF8XADiaARh2QCIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#فوری؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/22958" target="_blank">📅 22:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22957">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCWZL-LZxPjDR8F6sWHB0JeT58_XTjZjOBQrmbhPjKelpYUdq-mr0vhHUUkosUoCGogfq3VGAHY7rkdvvTEyJAofo_ZeK4U6UqmwYCCjC1qvutakJNmBTsQeVj8v1Bt_cCvdu1Ztc0dy0K2sBuYlpvffDTd1tasE3WLPPpL46j01f6GXAsDyo86iW14Ce0j97ibpirJvbDIM7jMN-AVkNfOtRuhD69lVgxEHEO1ozG3ya3UojDtyoW0W01m10TQVN4otz9j5wHojT6kvCSDf3WgmjOMn_8y4IIAvmOVmETuN9Uibf_Xy7BMepvBp8mHIUo7PsTr3tn5VmZEcKHckVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ به‌احتمال فراوان آنتونیو آدان راهی لیگ امارات خواهدشد. او دو آفر از باشگاه‌ های اماراتی‌دریافت‌کرده.همانطور در روزهای‌قبل خبر دادیم جدایی آدان از استقلال قطعی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/22957" target="_blank">📅 21:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22956">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1b174faf.mp4?token=NY8MsVSBv8g6Ru7Gav_QV9SPmDBEdffJ-vi8PhyXFOnpselKd93vft99sDaKXgJPeyECOxWJcKmSXl-mq7hgm-d6I6tunxrnKKxTPW_FNs3AqfVizG2r6AHoZdKxMKFIU7NA9uUd1XaNBKC5FjxAqJhs3v4usdgkuAFIK7L0mqgOGOdYJQwnpdUyBCO_llL3szy7E8j2HGX1iB7Vi4k6MwYBfDKYiwmEb_qi9A7XwiK-l1FPO4hkiQql1C8SVNddZGJq_3PIA65sLj85qrLlhK16YaPOHjYiEMl0jQsamApqxO75DMhfwE_C6u8uhSZYoNj7QwdXE3Om6Sw5yxRv2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1b174faf.mp4?token=NY8MsVSBv8g6Ru7Gav_QV9SPmDBEdffJ-vi8PhyXFOnpselKd93vft99sDaKXgJPeyECOxWJcKmSXl-mq7hgm-d6I6tunxrnKKxTPW_FNs3AqfVizG2r6AHoZdKxMKFIU7NA9uUd1XaNBKC5FjxAqJhs3v4usdgkuAFIK7L0mqgOGOdYJQwnpdUyBCO_llL3szy7E8j2HGX1iB7Vi4k6MwYBfDKYiwmEb_qi9A7XwiK-l1FPO4hkiQql1C8SVNddZGJq_3PIA65sLj85qrLlhK16YaPOHjYiEMl0jQsamApqxO75DMhfwE_C6u8uhSZYoNj7QwdXE3Om6Sw5yxRv2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#فوری
؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22956" target="_blank">📅 21:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22955">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-GJg8IJaaZDWavB2kObT3iojTopHIfQbBwry0Cx56pKoyqgegvK9t3URmq3UDvmnJ8af5ZvOSiAoOborqAFQuBre6beWjW6sfccDqbgkHorZjlJF8ZZ6cu__XmIGU13DKK0nWjUhydxFdfla1yp93-NemjtWX_vrFBemK16PLax78VAo7k47c1YcvjM6_boGCOhOUXkbe1Cagjg56SuSXBmMK_jEV1ky-a7SwVd3Uq6WZJLtxiKBxiAike6spiBecuASqGPPsIXpaj7HCqtc8ezBMcYdf6mNSX9AWbvnXXA4I3xRKSiElyOXnyUGoPZd6onghfZUHOCcrHukFgwPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ کادناسر: بعیده که‌سرانPSG ویتینیا یا ژائو نوس رو با رقم 150 میلیون یورو بفروشند. برای هرکدوم از این دو نفر حداقل 200M€ میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/22955" target="_blank">📅 21:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22953">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDxXFEBbpeVfGP--ZwyZ65s3CVyypGx2F0Rzp0cs-Tsa22Bk0vmoKdPQBMxvKDrIE4mrgKb8ypQGI9etiyh41coQmlUtYHO-O-yksHdVAQeGqA9xJyQ_HQfdGHv3d8jujlh1pS3VEO04ROfEAEYWK4Ywfyu0VAYIfofj6xq5z_KX9q35K2Z3p9dbfqbgORWxtN0_dznNaduEdX5tuBz0YPJMEcTdn0svjZXyaOIbqE-Kd3PQ9xEhuA165XKyAdZGF5wzg1jXVcuo1YFBy2GaBvem6U4dWQryOJmsp8itv14pXfISIiDoBeV8NWupT76GMAxE5fhgYnB6O7mHEdTNIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gNlIWDAMawI8c-F3q0sHw3y64e35YIDgTy4DrHzuYCiZKW27JNJ0PTwYzox12QCvUMgHzMbzmNSEDxe9yPZC16kIkrH3yaQ3f7l6ZZybr54Eh231B6z3IPtm-BXRrUl7MxgjwDLn4qui0Gzs8vLdGmbnUJ6yDX-K0GVhfTxdsdEMNfuJEy9n2iBaCtoQgvmfX27hjdpi5XmncCvMGDBgYdImbsgpiw-oPJ2rFdiif5jvJzTvPeeJcpr4co6RknNnrcjRSROKvU35RCy6KEkHeF4cc-oFzU8jgeDtrug4I2P_BNIY4gJk_ZAzvMw_dPaoU5e21qDcUN81KtuRiDmxCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/22953" target="_blank">📅 21:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22952">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-aa02eBvqq28SPB36dYSmj8JZGpoNjsJYM7wLq-py0dUgm5sRHFjoSHBfW3ScrYziKJwSslblAyrfYvmK8-Wv8WZ6LQVhap8-5pnCkQBspBRxHgfxLviVf60TZgFU5lyZR5HBr9FCpNqmdYLPqYyWB_43poyQJlS1GxqAR8ok5XZqMah49D8h8POl4OmNwyiM0CFT3Xu7pHegH3G1A5kr5sJnvPBryOD5TehTiinusex6RMfsOO88gicBJMkSCcNxQ9KqRZY63cGS8YTml9IePaEKInEgMY1s3PCJvqGUtzeZ4py6m5JbTdrC_9v6OrcAcLYTuzThFw3Pe2FJFrAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
حواشی‌ دیدارآینده ایران
🆚
مصر در رقابت‌ های جام جهانی 2026 از نگاه هوش مصنوعی ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22952" target="_blank">📅 21:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22951">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=vjDBSYmEz7LiEP1hUlZhHJC0P4yfojf4dO9K_USq46sg6P0wNpVXVrVb4kB0w4c1MaEOXplQKK4XtS4VMQNCFIldZv8JV95jGVK4Qt5eLC8cIvjlutNraqlPUfUHm7Bf0HcCAYtPJ5okIsFIQg3EzgrN5Vm46drdeBriropnKhejPpULjnfNOyAZPMmM14o9u6DtyieitSXhu7GZ1ar6sBLwElsQfWj4TkRRIgO4-t3MErIjJ56RDJdhA0d0n2HS7dYTYLT4gL3fz_3UdbvNqh-uxgY4Ag9wie97K8H3Z9Vg3xGkhAilvG_feNl9CjuO3wSdWwE3LiT1whc6KXUWvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=vjDBSYmEz7LiEP1hUlZhHJC0P4yfojf4dO9K_USq46sg6P0wNpVXVrVb4kB0w4c1MaEOXplQKK4XtS4VMQNCFIldZv8JV95jGVK4Qt5eLC8cIvjlutNraqlPUfUHm7Bf0HcCAYtPJ5okIsFIQg3EzgrN5Vm46drdeBriropnKhejPpULjnfNOyAZPMmM14o9u6DtyieitSXhu7GZ1ar6sBLwElsQfWj4TkRRIgO4-t3MErIjJ56RDJdhA0d0n2HS7dYTYLT4gL3fz_3UdbvNqh-uxgY4Ag9wie97K8H3Z9Vg3xGkhAilvG_feNl9CjuO3wSdWwE3LiT1whc6KXUWvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تیکه‌های سنگین ابوطالب حسینی به تاج رئیس فدراسیون فوتبال درباره عدم صادر شدن ویزاش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/22951" target="_blank">📅 20:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22950">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_r2omQk9nt7Zps8EMMLifoiGAmIoUVnYyoVPuy8yJ6eW2V2XZTTIpHr-4TlbAryRqmZ4I2y_Aj4scHq7ZxYzoqVHgmjLOXi0DR39BCd2wxdF5MIaw8xiB_8dVCsmo6_hjiLLRcll-ppWp4KxEwsJ1k6x3LpReBuRFj0mY_vF89EZY2FGud6lBplKdElDum1gvTZfs3xhP7fd1_9UwHSTh1a_nT7QVfp66JBbtqLcsFYk1sQ50uJktfavONRHjqDrBbc95y4HL86qAzv22XwyntoGMopiy6BhauP4xBCvg1Q2UN3JUF4eNv7OGrfWpEZpwTaV7bCn_qb6_c47QcuEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌فعلی‌آبی‌پوشان موافقت خود را با پذیزفتن دستیاری دراگان اسکوچیچ درصورت عقد قرارداد با استقلال به علی تاجرنیا اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22950" target="_blank">📅 20:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22949">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNqMziCv3v7dKNR9Rlq0zLxoASKMR7wUPTzc6gUHFKiSiS-nTBB2dwvG-vKvy133OZQuYCpwX1F3z2c00bzo4D5Ee3PRx1FvQKoavQP-pf7PTZ-iI7xMyRfONVJa6ehAK-ojIqpdaNRnig4wAoY6XbaK2QIz3e9YPosaThF_cRrieggFVkfy_nWlCsQb_am5ho6q1hy0U54vc4XIcu3Rftf8JEoX_GvRW2dKSR5wSCVIghG8s7AiKQ7bcHxgJjvtG6q7dELy-j8voDl1P9fe2lglEiOycGyWkbglVZDLWQCqPozpdlgsP96YvQyvFnyWk2_Msk52ui0J4POInQanqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛ اگه کریس رونالدو در جام جهانی 2026 موفق به گلزنی شود؛ به مسن ترین بازیکن تاریخ این رقابت ها تبدیل خواهد شد که گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22949" target="_blank">📅 19:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22948">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QL8PzbXjWNhxaG9ojosFD_dHAvwFc95VqFuR-oZllT061v-mgsUXLDXLRm_QU28guRfBdTrGsthqiRgO3DdHzmwOIZHRp1qOdgS_6AleOkhQBpNAIYOqsQkGAQuVZmjT3gn-Qis7qQUqqYbzCe5q9G6oONldHWTkQQ4zU2drl9AlsndaHNqYklqFUXbBqFbzJ0FZ1KXIzMVr32lFjXWEMvREPlR1odC9OgpVbBb8hOWBEY7Iq4Xk444C4CpMxqVRTWk_TeIf1YUwGfoRqln9qxjk0Apxnt0yLHSxAGKKMTJ90mT0gJwEuCUPz4nGPbOFIRc1pdh2_DXv9EdDK8XDlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22948" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22947">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c78767e61.mp4?token=bwDwM3hh54NsAIpwkleiHjar4hFF9hWJqHUL03-apWvExh29eDY6QacCO-kVaGq3xzHqY0Vh6kYVXYPfQZHPSVicNLCH_yailZUUDBpbeoJ7Ya0kcKDIMtE-mexvZHoyj0V0zIaEuUvcU0EopL3KAljXxdgsgi3ht64tpitBCftaBFgtXLpFl6d3VUFTamK4ymWfmSqS4KMiYTrZsXk4cnT6loyRvlfsOUj9Sftk4guYeGcmJKQjheH_kgVn6q4SQwI_T3_E6JUif9Qd-iSn4nX6JIbDMN1_w8NlIKJuWThGyNFsXHbGns0a9CLD3WtCF1mSPUS5z7-8ekqhb7KmYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c78767e61.mp4?token=bwDwM3hh54NsAIpwkleiHjar4hFF9hWJqHUL03-apWvExh29eDY6QacCO-kVaGq3xzHqY0Vh6kYVXYPfQZHPSVicNLCH_yailZUUDBpbeoJ7Ya0kcKDIMtE-mexvZHoyj0V0zIaEuUvcU0EopL3KAljXxdgsgi3ht64tpitBCftaBFgtXLpFl6d3VUFTamK4ymWfmSqS4KMiYTrZsXk4cnT6loyRvlfsOUj9Sftk4guYeGcmJKQjheH_kgVn6q4SQwI_T3_E6JUif9Qd-iSn4nX6JIbDMN1_w8NlIKJuWThGyNFsXHbGns0a9CLD3WtCF1mSPUS5z7-8ekqhb7KmYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
آقای‌ممفیس‌دپای‌هستن مهاجم هلندی اسبق بارسا منچستر و اتلتیکو که داخل و بیرون زمین می‌نوازد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22947" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22946">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYjKdyXsQ-8FYOBTQMNQ0AWVscdVN4-INYvRyTzAYA3XLh0zCzY8oE3I1X8Ng9A60Yyb6qNtT9H3EuyhTxcJTLRDM2b3fG4QXG4JKtaoK7PBjZCB_ykcY4on6Qpa6AkfjJa4ki-O3_wk6jK0dcSVbgJKsTZ2xqcLPwZdHWIniJphhusiPQLl2sDJJnnhZMrDfNZivVBJ2rt3jZJPyVW_N1NhEYc49X-LLM3vHcUUVltMor-WHNOACsiAkhHZEw4tCZz18XOljc_AQQ7xZj4CJTe1RFFHF3jLSudAuN89YM9Y8e9K8RnXJOQJFvLK9YeoHgQVax4AmaJAfPaM6e7QIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
با ارز دیجیتال حسابت رو شارژ کن
🅰️
🅰️
🅰️
شارژ اضافی بگیر
✅
🎁
20% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
همراه با درگاه‌
#ریالی
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
16
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/22946" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22945">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zjwh9ZsOS26doBb8Am6h5R-Qv9N5RjWyY8ejGS7QtDeO01QwwCbad2U5ltNSqg8adGb7YYPw_OQjpq98tSipOw1stGhQl9w1YX_lirDfW3NlBDnt6J0QAJXvw3N6-9nDPPl-_eYyblywKpyTgtaeHgpr2VA5blZ0DV1Q8ps1ULzlnlJ1GOF76B5nXLPte4ERFEFSJg6oe5oENQoPWdvLRynDK5YIBp-vGQSUUWZvpeQ3KyzsxOM7PqfDFKTqbpnDiT5lO_qzM5xF5eETmYpzeQlF71LmQ67uu5jfr6dppYtI331ghS6FkneN3RUCvu0lwvxEPzunw5nzMuYDs4vG9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22945" target="_blank">📅 18:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22944">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZePzDdby3EhFWEOxF2K5f7TeI4XBeEFlN24sQW9iMawxPT2tchFxBMs4gik9YaNjNgED9XnOaBeTGQrrvaLyXTp9vyOhKUKN_fRlemHHI6CX9KDBfmv2y3fZlcJy1uRL29k-MHfe90UCnnwvjqb94HHpXwn8VFyHLyPn0MhwBFPwoKvpM2oZqvnTjQdTwQWAMyBFr6MzeRa5V8KyW7GD721dxk-NIhA5UYFkeNgAgtmeWaDfSjDttdffkPHlszGfYNGeEcVRHGb0De1lNq2oVBqsY2wQkdCeBPQoIWPNWwAw5Ocb_jIHANse7JHJOl1ZPxoL1kScx2xcBG-EYoijA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: منتظرحمله‌این هفته فلورنتینو پرز برای نهایی کردن قرار داد مایکل اولیسه از بایرن مونیخ باشید. پرز قصد داره به هر قیمتی که شده فوق‌ستاره‌فرانسوی باواریایی‌ها رو جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22944" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22943">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHly0IILeiePF_qCHBD4SRbb9Rm3urhHobK0ors47cB9I8QQvBepAliO5wsyqpdUFzNFhltqt32zv1QIgBgV_yKtTpQQ1NwCgTJhOMnDyaqiXGu9X_TkqTpTflW5YhfVvnQzRVWhorzEnwfhMX4MgUnyJ2VLeZg6QX7dZMadjSiU2kR0lpm5zPJQRoRrcJ5ldkuxTOOYKm0lPEpw6KVmykMlI6l9ljLmolS-5l1SifyNnv95zp8KQOD9H9PPWnFgtXJL_eJvZgI2mMagS0bbeAFr79NL5pzjoTE0npFC3GiiciTRK2-VRLH8qeyvqefG25hTwehdCDKPQky0bp4aQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22943" target="_blank">📅 18:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22942">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=NBPNW5M4LQpZsZJCrMrBXJPT6EudQyab6ksHOBA44xK-OuBp0J93EJGhI_cLvIU4N5_Kgcaxe2yOqdHkIkx7C9Dp-Zbc9enNaGh5eLyXIDkjrYdkjzSxKUJ3kPBylBn18MYFDYr4MPp0vfgPwnBZ8IlX8oFjWMh2LAnzQ2hCwHiHjJAl-BGp7prhBkE3dSk-Uqs697HayPZTWnmV4OSncZO0si0daRp7rvBFirK3o5ie-wTj-mq1S-4TE3TRmG8F7v7eVcABB6I3K40DcVw3LUxNt4yiGUz63gaeWad4HWDm9LVo1Xgg1n4c7O6TnaddZm0PNBnscFruOlzYbhcheg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=NBPNW5M4LQpZsZJCrMrBXJPT6EudQyab6ksHOBA44xK-OuBp0J93EJGhI_cLvIU4N5_Kgcaxe2yOqdHkIkx7C9Dp-Zbc9enNaGh5eLyXIDkjrYdkjzSxKUJ3kPBylBn18MYFDYr4MPp0vfgPwnBZ8IlX8oFjWMh2LAnzQ2hCwHiHjJAl-BGp7prhBkE3dSk-Uqs697HayPZTWnmV4OSncZO0si0daRp7rvBFirK3o5ie-wTj-mq1S-4TE3TRmG8F7v7eVcABB6I3K40DcVw3LUxNt4yiGUz63gaeWad4HWDm9LVo1Xgg1n4c7O6TnaddZm0PNBnscFruOlzYbhcheg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظاتی‌از مسابقه‌کاراته‌معلولین؛ این چه حرکتی بود تو زدی آخه؟ چرا از روی‌ویلچره انداختیش پایین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/22942" target="_blank">📅 17:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22941">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZ5SNRQ2SFpz0lTpVjersU2oMont4HZVlWfEmqu8_902xcFQEaVxu5D4-Xrvn2Ghyv-YEPt-2LI35pyIrB-i4zuHgQnGzF5aK4ewltaLKAgUPJVhom3rc_AChu7rtERkCptS_lNUv6sqLAeCAjWPCaW68bgzBY065-GDxcKFE93kzO5CT8l_pLXNxN7KsNhgy1847B1Nwl6H2MUve-xoUgY6XEKzyURqTLS-OJXq3VKdswvIt2ekuHCBCB_2wY-cGjlI8bWh0NwuJmJagaFdluyBpYPXBFT34aF41y8BnnpEcCdODGYJtAiu4tCFIhehbkPaaYBNpujoFkVkqAUf7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22941" target="_blank">📅 17:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22940">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzkX9afF1JyUjP2XblqhnlzKxxp9MMvVj6JCXbqln0RJ-yAuOsgERa44Gmt5_3GOnVzu1Ibxh45nChvzLR_JkDFearF4A5QRlYCQIHYedNSl_IJ3THg1RCwQayo5JL9YeW0FjLdxI7RswAxB2bzY_GYJ_3riLmDUKjp6Xvf0KoHfRwe_CQOSO7sY2Mc11s1EUUN0IyeRac_DwHOt8kWdyxv28qArW1-9Uz2jFZBjVP5DnZlG5QEYfmn5DtYwyK6_4sFTlX7U8d0ZkcAm4YEJ09lF7UXdazMYN5-OHzs6r90L2-_NeZYmoBmsw8cc7IpLUcoBEexaz4TqoFhmnQRE7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ مدیریت باشگاه استقلال به دراگان اسکوچیچ پیشنهادداده‌که تنها دستیاری ایرانی‌اش در فصل آینده سهراب بختیاری‌زاده باشد که درصورتیکه جنگ پیش آمد و اسکوچیچ مجبور به ترک ایران شد بختیاری زاده سکان هدایت تیم رو بر عهده بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22940" target="_blank">📅 17:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22939">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJpOnoB_70ioQ34EcOzw6XXvOhoGCoG_7ZOe4YmWioh4jMWADJV7jNdvMikhCNsxgXsaYMPayCiqrB7UiIIl4RVV01mPyVUHjAP7zi_lzPtopQPVqq7teAoiIXUw_totezaVqImcUKj-7ARgtTGE5sGfkWLCqpEtdyrU1Xi_qmy937ywJe9FB6CpQFjGk-_QUvlBkBMjSDcc8OvlTxDBd5YuJeQQadWEh3nKcJm5G9tSykuu6fW64N-e3xBLPt5tFQ3gMsOzc1TAulABdh578DNwNILlhab5n6BnSvXHIxa24-1PUzPOaXG6OSJAxEobRM5U_RHGQbEImacCjRjoUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌ های رسانه پرشیانا؛ باشگاه پرسپولیس در تلاشه که مجوز فعالیت افشین پیروانی در لیگ برتر رو از نهادهای ذیربط بگیره و در فصل جدید رقابت‌ها به نیمکت سرخپوشان برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22939" target="_blank">📅 17:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22938">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DF-cl74RbVYoqFIwOVoEfLuUyfv0RQjVbAD77DM1HE3BM6jrbwerfg1zKL0MJ2UMrQxdfF0pxxWobfi_YKyZWizspZe6PkbebURQ0dIRNyxeJU-BjPe5hNkdZA0cQCEUaJpMHCYTMBsFY9rOGF7tCXDgisNBhkS9S9Z5KQXFOa0ui5RSrGHZusoSF6grMmXnGJnvOZb53eH5BsFL6J4b2IU05Tym5qaFpyEvWw-KuodUwDi7rvFU4YLP0yP1AbXVXhEkDBVebZGucRsYWBIuohZqTWhZCJqv8AuTv0FW0v901Lhd_LBTh3S3DaKigZNpatb2MbhAoU8XoNpByw1S0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22938" target="_blank">📅 17:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22937">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0d90aad.mp4?token=q_9e8d6dLF-tYBAGP9xMgFy8aIjdhF-yB-1cZEOgpFq_q6FOMzoC04Vh8FrIWEQlfwPoPhw2dw6J_koPVXmVhIOxv7HhPpU4e6SjMY8hylIW2umJrYEPvbFyoXOJ8PRtA0e71jbgW4E8rFfOyD-Lg9c6Fukmoj4e96X9sMlRyqcwW4ZxH8TUDEBN7QG11k7FrWeP0hLrQ3FZdjIDT-FhbfqgJhw6M45LcD2S3b5KX8uWZUH_ZKutq3xXsT44Kg61zpGfpfJegOLtznhxhk1IgDU3ypeDDK0m_MQ1W4kHmihH5-8TwKhKEkBGUVAiwn5q6eF1q6L6qpT1ELGYZ60a7buQpaLnH069WTdS3o1OPcm5mGVwoiAGfghO_qN5VQxcJUMIekf-gb1eunHBOhT9E49vJS3UiwuaWCyif5CmDLiaDCgGqWDNTn7iL6srnX1nPVMn238Zze9y98AwxcZJgxd20b4zEPPjqVT-CdP5zhRwUsnsqaQLm6RVBC9pnKAdhlgpu3QDxGkEMwKS0fZN7bIP46xCJerw_YIMX0avNlVmW_7rSYkE_CtB0EVHukOO_2xGwiNOKPvpYTwMCVacTTQWwfskQgIEuH-uk2NipmfFbbn1FWFJoWMaZq0jHBZHMhClOElvWT3jkYt3EclbluY2MjvUeRZ-34RgtXr9u9k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0d90aad.mp4?token=q_9e8d6dLF-tYBAGP9xMgFy8aIjdhF-yB-1cZEOgpFq_q6FOMzoC04Vh8FrIWEQlfwPoPhw2dw6J_koPVXmVhIOxv7HhPpU4e6SjMY8hylIW2umJrYEPvbFyoXOJ8PRtA0e71jbgW4E8rFfOyD-Lg9c6Fukmoj4e96X9sMlRyqcwW4ZxH8TUDEBN7QG11k7FrWeP0hLrQ3FZdjIDT-FhbfqgJhw6M45LcD2S3b5KX8uWZUH_ZKutq3xXsT44Kg61zpGfpfJegOLtznhxhk1IgDU3ypeDDK0m_MQ1W4kHmihH5-8TwKhKEkBGUVAiwn5q6eF1q6L6qpT1ELGYZ60a7buQpaLnH069WTdS3o1OPcm5mGVwoiAGfghO_qN5VQxcJUMIekf-gb1eunHBOhT9E49vJS3UiwuaWCyif5CmDLiaDCgGqWDNTn7iL6srnX1nPVMn238Zze9y98AwxcZJgxd20b4zEPPjqVT-CdP5zhRwUsnsqaQLm6RVBC9pnKAdhlgpu3QDxGkEMwKS0fZN7bIP46xCJerw_YIMX0avNlVmW_7rSYkE_CtB0EVHukOO_2xGwiNOKPvpYTwMCVacTTQWwfskQgIEuH-uk2NipmfFbbn1FWFJoWMaZq0jHBZHMhClOElvWT3jkYt3EclbluY2MjvUeRZ-34RgtXr9u9k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اجرا چالش فوق العاده سخت ورزشکار روسی توسط یک ورزشکار ایرانی با رکورد زنی روسی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22937" target="_blank">📅 16:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22936">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OL_zhJEkmKaUC8rNxfBwyShswioI43Z4iTyJCHMvECtbSRpDKgD5axio2VcecVGo6FuxhFgKYpT8cCL7WIMRsl3FmX5mYInPyYeU6ydqlHcFuRNoCqXYdkw2znge9D-Mhx8Qb1qXDyu0yC6ZZAd3KsOi2_fl24rPNl_NcGM2_EvIcWVw-zmuafaeOkM3LBSFIrHpdESBfhJ6MyYkrxwQ-lPx90QZzF4yOX0ji_AzWCeke-q5C6GhvgnPTVfqpj37vLlHEV1DGe8hjqx0luRV0Gm_dAtwXePGORl9ThZjqQkFDt2w3LhbdR5TzFmv6MEbT_yv4C2C7_31ATdKoeH9fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22936" target="_blank">📅 16:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22935">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lax9yhjKNL9vJ_rldEiGHvr5zW8Gq9qoZTiGGwjt0-BqE9KGiVEQIvh5wMpkvYPmjI77wipqWd5lCKHUh9fJsxhpEVfbV9uGgQWU24WmpqF0udAaHM7_NDRNZBQrNAWxXdzRHWWPDnXsycTjhJCMiskVQZ6vq2gwnSRVImDb1DX1GIWTfCWh4moLC7beDzlben6Y4hmakti5qd8yigLXiBKsILU_CHvHjI3oGkapZU-ISbsSDj_dfYUwCA9jE1pCApkwWTV_F3PDOqZMPKqAGzjaDavK3jeO7yjlYzxpHG9DbhiTLx6GDPuJ3k7IlFk8MBWhEtaRTvW1ymSGCaB54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌انتقالات|گستون‌ایدول‌ خبرنگار آرژانتینی: با جرأت بگم که آلوارز درنهایت از اتلتیکومادرید جدا میشه. مقصد بعدی آلوارز صدرصدر بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22935" target="_blank">📅 16:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22934">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGb4bf1aCCyq8tuGJ5mvYk5fT2TvU2YIOv3PTNnLs_2-y_Z1atgivEOjM_MWkpPA3HQj-fGN5RgYrq0VXXKIEuFL0rkXHttGTH5pkqyqTQzdmEDVJ4NODfcCZltxY3HqhAHHYBdTu5N_glROUyDovTrL3QoAK5i-sgLTK9gURw6EeMIMGFY-aX1kwPhHHQaR-vybV9arduGsVX4eVwbWG5j-L1r12oU5LElUz0EXKWzMMEMXLtsMYwKyloxJ01OetbKSbKVAuYwDmhQ85x8HM2-90ImFWPJTsye5urEOXgIB9c_BZTmt0mERtma9sVuQVdGkshcXk5ogMXbAqF_FZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22934" target="_blank">📅 16:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22933">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=XkARHvqKBgZkA05ewjraQ5MTp94QtQjnNjc1iI3JMkQ2cHMu-rsr9XOPBdOwisFiInSU_uF0oNoK7QhtyyBlAKOj8w23wLhcwr9jl5Q_eJGE-UwPBMmGBY_2fSouINCnk1WBsf_9DsrNQqFScNvMZ32BbOd8RkO0B9LrV8ZD0NZ_xeWmY2RtdsNH4CRL40BtxQEqZGGnLe2v2DQzzP4gucWqPvWHxwxjU-2sQQnEEzAPYWTqg2uC6VLE-8vphzv7pY2M5gcBy3qgbDc_nl48rMVIe3sXnlGgWZEC1vVezgHIKPGu7nLJRx-_9AGB49lx_BAAf-hIZM-I_jdK6Iz-Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=XkARHvqKBgZkA05ewjraQ5MTp94QtQjnNjc1iI3JMkQ2cHMu-rsr9XOPBdOwisFiInSU_uF0oNoK7QhtyyBlAKOj8w23wLhcwr9jl5Q_eJGE-UwPBMmGBY_2fSouINCnk1WBsf_9DsrNQqFScNvMZ32BbOd8RkO0B9LrV8ZD0NZ_xeWmY2RtdsNH4CRL40BtxQEqZGGnLe2v2DQzzP4gucWqPvWHxwxjU-2sQQnEEzAPYWTqg2uC6VLE-8vphzv7pY2M5gcBy3qgbDc_nl48rMVIe3sXnlGgWZEC1vVezgHIKPGu7nLJRx-_9AGB49lx_BAAf-hIZM-I_jdK6Iz-Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آدریانا اولیوارس مدل مکزیکیم رو بدنش عکس تک تک بازیکنای جام‌جهانی رو چسبوند و از دخترای مکزیکی دیگم خواست این چالشو انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22933" target="_blank">📅 15:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22932">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gfurfh9ZYFXHE3-iQD1lMv7V-hKwirfT8msJv4QkW6qL3MOVXg3S236PhbiKcfQb-nd3kpTtQVdLKWfhPiy_yVE3VMDuyz3eKNdE1eSrn76bWUJsj5GGPg7slU5175QD5qMBy67MTajez5kXa0P3JugLKrMvn3JrqEnfSoKFNL2lJAW9aVkZ1IK2w9ZqTSCFRpsLygtIMjTvQ67P8KmjkB7bIpFDr62tTqoOv8tQIS_k4RBoUTvCij0pfhsYdILFEeyy2RmGWTWBpc379-yx2RXyEA6ZSBCk95eWh5wofSJiV0nY_s2s-S-ZawP828gQx-dZSU_DRyVLw1x9zNWEvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
انتخابات‌ریاست‌باشگاه رئال‌مادرید از دقایقی قبل شروع شده و تاپایان امشب هم مشخص خواهد شد ریاست کهکشانی‌ها به کی خواهد رسید. شانس فلورنتینو پرز بسیار بیشتر از انریکه خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22932" target="_blank">📅 15:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22931">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUm0jc_Z985ENhjVr79uYupxPXWj7sHPtSTCwo6dT437P3VXAtScrBB-upgahtTHDFbqjCAYfBoFGNuUOkWyW1Avu7yb_AARUrOWQezPuYV7XPmD7EyKjcrIBD8GwkS6fMKKmVGN9zUTIe7GslPvdHVMoPVxrKE1CTuj8erkc-80AodKMaMCSbb3IFtsIJkzCuCO66CpCxmXP_gndiOHmxk-zboGvq_0yk4qLG6LIXaUGl-zHmi_H7Is-lOzlP2u8sqlxtSDISpGp8J9I7lFDD1MBHC0z8hs0IWnJMNCmKyBXLWa3wBEg_niVdPkdpnyU7bq_auS1yLYvZ0YOVtumQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22931" target="_blank">📅 15:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22930">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvhkRFYyRgNlK-o_v4rpmEogdBCaM5gcd_UpFF7oQKzr4yzAQiG2BGm10gp7bc2HdalE6he3RQps4PrRds9vH8yfH0rsux6Sw-H3SO_F3U0s0I7MdKFRAMKQT_9e-GRjW_Dw4jUxa7kVxwA8I35fj0BjhkAREoBPfsJ7zreTrz_j622H3aocOYow6UXGLBsHUi5PV6ZFWCG0vmyq0qXEVGlVCvmjRX3Ci9jAW14xKmdmx2JsG2-Xb6xkjSkYshK8j0XVACLubgK_DCz3h-2Ehslj0TRxqsV7qOp1A7mtXjiagi_9MCd0Pxbd1z6NmQeoBWYGAB0iMkUleN9aBU5u-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22930" target="_blank">📅 14:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22929">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZl1mcDoI_JdnFB42XtXrYojR63BnVD3abjvllFIOeXuNhAFgQunmic6pVr0gK64ccnsf5_4FSr1ydBWXx84W6axrtVLpYdB9LBBH9f09pnwj7d46I3I7voEuSpPNRoG5jeEH81E--R0LoLVI9Z0cVg3XZCgGPwayf9SApwvGJINzcIXbuQltH3arXKpkkGclXCTsuejlzVeWmEL531IAuiopnl7e389Z1o9tLPQ2HGV6KRvG0WBV7pd69s0pyOy9esz8u1yWr-cwHopVPT05upQ78bYa7uhWTZmeMiJZqhv8u7ikLV36-XMa90qn-T4uVisARe8T_e3MQAeixzgXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22929" target="_blank">📅 14:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22927">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fq1YDIVfOjXgt2_yDpN6M-hVNnKckgY2c4cViBNErqKiXb5aRM9AjPyaiGGHJU-ME-ADEQ7OYm2jpQy1OUCGc1j7MJWliiQjnj_1fhM3IcmEPItjgmvLoisopdWOSaTISVMjFwayNhNJC_zMkFk9DtvwQu7NfalD-Wu0d9x5nL_oHjhhTdGAe7peTw1KPDKShMBsQgPwmUz07zq8GfJk63bSLkzXgP0ziPGZ7m4pTEAWhzHkNibcI_mQJ7GP72I2dqNe8vfhdSfWtFSPgr-d9HHOTX4iDWhKuhwT15MPuk-eXvrEGlcsj2hD71i9fk53ErSnZ-p-1bDQOsrkg1XJtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGpnqHYCr0dQ_DyiXnVBayshFJ4LuhoXSzR_Jmq5XbtBGnpuNZS7j1bxhDoNQTlHh8KlEqVDEzEmk5eDE88VHmutflqJemHm7Zitez9Yf5WlTFz23jy8UvM32QsqgzHIJcejE0xg_ZFym2zoA8Y9-zeT3_I4KlDCURbGRzU5_8niK2P_uPNcliZ1U9-0TVsJdVuoxVYzi-ndLem9TzXeagOO_5L6VHmX-q7lTWZivqqqJ9eVAN4U1T42QaydtBmaKPWqGWL42XHYROHukcXmf0UdqSGqguyRueCUUCL4LxCh0VpUhP9TYJVjmkmKXIiDo6PkCSRjosidSPTBMa2XOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22927" target="_blank">📅 14:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22926">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZRbNBgpsVD2311F6i1IL-lk3Lj8sYXnf0ZdZnM_1Ox0PBmhYOJ7cecOV46KNXdqTsoNjBkJXdw8y3GXCKk3Q5wNa_j6Ju08XGIyU_pFvmK4Z7qwgYeUm_URcCrzTcs1Xx15hZOZkOlW2xY9MkJ-BUt0lw-De13pVs4LMw40LZR0pegjeDF-dFSTXfEqRvM2rnXZcn7WIh7g-qr3l4sRqI2f52KrLWJrCmNp1y4X3uFf1G_VIVgQl5GopJSXoooJY6HyZ_tweCxB-Uhyx0ItutGmQVPIZsuMdUJS6xVFdMkPWOQgDa_APUAtFqwcdJya1eP-NKcXku2BrX77pI_low.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22926" target="_blank">📅 13:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22925">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBWsCvr-v5E8XKwWGHegiautLYiH8YbZ_cau4ij3rq1WidI3uEF10eJYtImzNXo2JvwByZ8PLOd4Pq0H88_sN0Azcndv0S695zEbaq8QpVOxFAaXfkV3izkUudSc5Bd9tV97NSat3QhbB7Cxk9IT_OO3q1o5et6j3CCFKeSHuwyIrvKxZWvQJNgZ4wuSiUdyfYo35bOPlk2v6s5rI2UTtagfo1x8IYnvL-bd9N9BGs7oc0tZWU0b3oSv_tv18BPtRUXBT9x2Xpzn3wXifdmHQjE0rubNcNs8nwhnt2M1cP_eOED9bok2h_u58tnmn8ZqYBjMZyiJaEzBWTFulGizkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی‌کنیم از این ویویو بسیار قدیمی امیر تتلو درباره استقلالی و پرسپولیسی‌بودنش در زمان‌های مختلف
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22925" target="_blank">📅 12:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22924">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYFOij0AgEd0DxBV4rQUdrdAcRzSvtLbM9gaFcBQMcJ5mbeFgMfpmKd0-tXrnARchmxvWoaFoga4dLvyXmELkuaTZBl7GlvhJmS6lhQE2wCvdyBuBtyA9bfBVNG5SIq65mObeqFZzuHR9WHQdob19IFGfdoznqRiKDEgADVb5Jc9q3RFRinpbkh6kYC0kfz0BrHwta2zhGbWKlGSEiwNYgVZsmk7HH5BrMJAltrndrg1vGhRHpGEebupPTkm2OnG2R51T1ZKdhhUYWMOT6I8MRt-F38oF0eqwBKbQzyKt1niIn8Yym4DP4xLcLUmWeszpyxQIdr5ue0SQOcb900LZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ هفت سال پیش در چنین روزی؛
ادن هازاد باعقدقراردادی به‌ارزش بیش از 100 میلیون یورو از چلسی به رئال مادرید پیوست. او در طول 4 فصل حضور در‌این‌تیم 76 بازی انجام داد و تنها تونست که 7 گل بثمربرسونه مابقیش مصدوم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22924" target="_blank">📅 12:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22923">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46a056081.mp4?token=by1cTaVeK3FNDsZSmP2od2Ity0Fm2rDV81OcSM6Jy2Z38obWGOXRVRo5HQMODBEX5KP5OQGqAVPRTcXLZ3erE4HMORMGIdbmYGjAvKKd3oqAr5klt9PlAFwfBDe9a_FE0CXmH2DByO__l2PGlD_WhG7TMrPrDSsZ4WK9J8Ou7dhxbKy198XKXBgvIi2W6DPoxgjZCTltxybzU3PuXabTU5SSu2EcFBYOQZj8coRew_9LY7AmY8nzI2_2wicvxXGJg11N8dLlGEOWg9eG9aIqtvojbB3ckSVxswuGlu53i1gjnL8z3F8TuY2j7ntNKHqWs8BWudNIBHEsvmboGbxU2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46a056081.mp4?token=by1cTaVeK3FNDsZSmP2od2Ity0Fm2rDV81OcSM6Jy2Z38obWGOXRVRo5HQMODBEX5KP5OQGqAVPRTcXLZ3erE4HMORMGIdbmYGjAvKKd3oqAr5klt9PlAFwfBDe9a_FE0CXmH2DByO__l2PGlD_WhG7TMrPrDSsZ4WK9J8Ou7dhxbKy198XKXBgvIi2W6DPoxgjZCTltxybzU3PuXabTU5SSu2EcFBYOQZj8coRew_9LY7AmY8nzI2_2wicvxXGJg11N8dLlGEOWg9eG9aIqtvojbB3ckSVxswuGlu53i1gjnL8z3F8TuY2j7ntNKHqWs8BWudNIBHEsvmboGbxU2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
وضعیت‌‌آکادمی‌های‌ژاپن؛
قشنگ‌ مشخصه دارند برنامه میریزن که یه روزی قهرمان جام‌جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22923" target="_blank">📅 12:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22922">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhtQT1B_rSN80NoI0oKkDaWPkoUBf26rxg8Yhfd23l5RbJkXivHsZdKXaz66Au5TgRyZ2rDJLtSYxukdFPuujupuFlMSw4re3LT2NrGEGXVQOLi_CWrrErbBY1v-kZKgR_rJPj-H3MofEYqZ6n_SZXvAN_MGvvtSmQP_FhKsrfrmcflaP9KfBDa9zF9pl6xZ2EZZ0g4ehuWLHcmgcz-95lzsnO9UVMePFvX3j8bGPHhOx8QWGFzioiFVz_AYiraV7vcfcbX-I4nlcK7Qe8biQJ0tWKfWC5A_hwXurjGs7RenfQmrUc7bFC1EXxZiX7PtK3AVSkrXm3088VUmiwLjXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حدادی مدیر عامل باشگاه پرسپولیس هفته آینده جلسه‌ای با مدیربرنامه مارکو باکیچ برگزار خواهد کرد تا تکلیف نهایی موندن یا رفتن این ستاره مونته‌نگرویی مشخص‌شه. باکیچ علاقمند به موندنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22922" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22921">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2a01aafa.mp4?token=ZDM65mLchSPYao5oY2BvcxWPOEu41_jIlOOLikyVUZq6BCPetE2i-kPSXbJBYc0lIXsaQipSdY0TpsbsVvZPt2bkYDncEAqQb0X30g5TWiFZwEUktX015IFHeA3v_yyn4EG1RngCBAKpUrz_9nrPHzcerbvbvLRCOr0JNJjC_9cBXqNhqmIIG_XSd5ksmXGxZQnb656aV7KmILWwBp0r4fzdhXovY8SQG6y3v85USp_dTroOKjPDymL8cI7whJVaFpNGz3y2MP6jmlQLyCaYcPzQ1JqPrIDd4W6dKoNjujP7L8UWRG_A_GKp8jRIyRk_41LJWx9kAVmtrHAD92o7mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2a01aafa.mp4?token=ZDM65mLchSPYao5oY2BvcxWPOEu41_jIlOOLikyVUZq6BCPetE2i-kPSXbJBYc0lIXsaQipSdY0TpsbsVvZPt2bkYDncEAqQb0X30g5TWiFZwEUktX015IFHeA3v_yyn4EG1RngCBAKpUrz_9nrPHzcerbvbvLRCOr0JNJjC_9cBXqNhqmIIG_XSd5ksmXGxZQnb656aV7KmILWwBp0r4fzdhXovY8SQG6y3v85USp_dTroOKjPDymL8cI7whJVaFpNGz3y2MP6jmlQLyCaYcPzQ1JqPrIDd4W6dKoNjujP7L8UWRG_A_GKp8jRIyRk_41LJWx9kAVmtrHAD92o7mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیبروین یجوری به تیبو کورتوا پاس میده که انگار هنوز از دستش‌بابت دزدیدن دوست‌دخترش فشاریه و میخواد کاری کنه در تیم ملی سوتی بده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22921" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22920">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22920" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22919">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBTf97_zp0uk-MKKTsdi9yU-pOquZ_qrFaoSirCVq6h-_yXpKRf1ATZQ7pM1QADhwf8HFZGsJ9zxYh9_rYVynltDF1xlmEMM60316fbL15O8yKzP76QnCj6NLGtcUqfu4VnnzKqUZl8d0piFptz6QsYTgR3kxIRaD5v3ZXJyMnaV3SKwaa_Chsy-Uo2QJxAGqgdTJgXpz7kO0m6v4LHuAznNIOtgt8UCniYE1RA7__I9Ak8auUqAEISeL1OY30cR2mesSjT44-L4O44LQ0DR2GHlzEiNf3Jp1hwNkOUPGkuZR4VPbirBRgjANFUsK4QkZWt4XiLVyxana-mU_d-rbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22919" target="_blank">📅 11:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22918">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTbmx9KWMS1lvl3xPRrMMvGqx6OUAdK9heTA4PT3uuKXsHrly74UB88h9LBO95_c65E2iwDlTU3bOQhBUAYadQ1kPNKeW4uDfeQHlzBgX4BYzU6hoQU8MOxQ23pwAOwxK4-ir5-ty2Uig7KnSETOWDaFp3UhRGhP3eMTaqrsL3xY_4NiVneI_o6Os7BSVHcPgZmDQYNceCJ8XMxH4JuSgedl3HOkExZw31Czkf3tJYhWTGcqlfqQjO-7SJ-viUtXZm3DX9RzoI3JwS3gQOJw3MKK2_e5QZax3w8XzML397slHWqtFoU3kQcLDgNFbnepKmm-IUDbD1cvoSHJkh8Cbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22918" target="_blank">📅 10:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22917">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d705d6a743.mp4?token=o049VnKqMkieFQxAoCHhmes4YLdvqj9HmJxpK_D8ZDWBiNysjTJlzoV-77NAs2212pVhTrtRrSR0WfJzXO3b95QBIaP8GhtI-McjvI5B7LZa-3GzsyFEscigRBdpMbNnUY6tSwo_NG7AFtIds0TmGphNm-y4PcOYlzVZmTLJm-h0ofeUemZZ2R6HG-XyEY3oT_3fdF1N9dHLj6tncxyO3yZa_nWyVBsc03sSlOmXQ49fdGbf0OtJLy-z94VqGscseEE24V9YQBqZvX5p_Je9n4HIWPRzjYU3MLIDUuqGfyPvCTHZRaZAFViI68JSsfAvcNiOm6qc4VM8HtaQJ_oV0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d705d6a743.mp4?token=o049VnKqMkieFQxAoCHhmes4YLdvqj9HmJxpK_D8ZDWBiNysjTJlzoV-77NAs2212pVhTrtRrSR0WfJzXO3b95QBIaP8GhtI-McjvI5B7LZa-3GzsyFEscigRBdpMbNnUY6tSwo_NG7AFtIds0TmGphNm-y4PcOYlzVZmTLJm-h0ofeUemZZ2R6HG-XyEY3oT_3fdF1N9dHLj6tncxyO3yZa_nWyVBsc03sSlOmXQ49fdGbf0OtJLy-z94VqGscseEE24V9YQBqZvX5p_Je9n4HIWPRzjYU3MLIDUuqGfyPvCTHZRaZAFViI68JSsfAvcNiOm6qc4VM8HtaQJ_oV0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایگزین تشویق ایسلندی رونمایی شد، تشویق وایکینگی هوادارای نروژ؛ تو جام‌جهانی اینکارو بکنن ارلینگ هالند جوگیر میشه به هر تیم 5 6 گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22917" target="_blank">📅 09:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22916">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epZzzZq4lTu5bIpAqlQLDyVg7FCRH-JLCu6qrztPgGEzs4Rk1HnYPvOXPmuf3TpSTPD_8Is2_KSmGQQ99eI59Wsf-kDNYWjua5hGXNpevnK-nYNZa1Vbfca7aGuSGzYHZhHn84XQsf7OQEo19e6VhFHJbrFOOwH1iFsvzF6yqLUdUWXrI65jhy_epsXR9T41xLFOEbk-yObx843roMTR5wYoTjiN7-E7HO9QPnZWdZi-5_CgoX5t5vV5s7IL7fhLPzV2fDVICZBhjgGFcFhLq6ZfK8l9rl_wUHB7inSJylGzEI_zbXMssE7PQsSc17zPPGE5lh9MQnyRkTI0CpDJpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصاحبه تاریخیی کاکا:
برام مهم نیست که بچه‌ هام بدونن یه زمانی بهترین بازیکن دنیا بودم؛ فقط می‌خوام منو به‌عنوان بهترین پدر دنیا بشناسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22916" target="_blank">📅 09:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22914">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mw9G-ZoF1XYrL3RPqteaXf0pzhadWE2wq6NWYLOXzcEQA4NuDFCiT8iSBq9I23nRZ6DKDLeI8KJcXHpS7CHcPd9cUAySiVAdK5XoN3MDWFIeBNkZzTvp0K-DCXumo2eByyI_wzOI8eD2QSAy2Ax1GCqFplL6Ffie6vC4PHebGTacneLFA_ydcZKz5mItU1o8rDgCwGhWN76AsShwtnJMOB7NF-NABXPZnBlCSVvS1NiOOfiRCggJAhMHcAa79p5WZLACeZ6jrwBiXhtngLLyj3BhQgEpuOp5CbH7AfJUcweqpwTHv-ly6mZZSV1vyMTPkTD-1UGRtSeQt4KUmqRD0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
تقابل شاگردان کارلتو با مصری‌ها و جدال یاران مسی برابر هندوراس
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/22914" target="_blank">📅 01:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22913">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzNCgaY5ouDuF4_ob2R69SRj2wNJkXymKlE9ifuwSjlXIkbuNOTyY3SeGbP-BmPR5tCbKUISYWx2WqEsBBKGUiyF219uzNBgzT7NKHndbPHNyXOPndlnLylJ2ASP88QyS48ThicdqoSntEeFFOJDpkWXM64Dq0EZftFzcLT6lfap81Cer0G8UW6o7XS6fVNaN2y8AivTIRlOviF96tG_eiZppQET5d3OEE08pQOBaPr1s_k-cik2Gw21maVq6RzXg3KEF6TGbZwPkC_mZJso9O839AQ0HgwNllDDLUs4pq336bAoOXK35lpc09Ni3q28R5J_kmOrZ5e7lZrdzLsS1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از بردپرگل بلژیکی‌ها مقابل تونس تا برتری تیم ملی پرتغال برابر شیلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/22913" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22912">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvLLkO536MxvJoQ7KU1-KR4WS0P02LRidK6-ZYsBtsgBCJhqzJftDuuasfmZFnYate8GFC39tMDkOkTe60w7SwT0iCZvgUizLVue9KWqMKvUy391C3xyLD-9mTqrZeVBYAU6PU_XhrlKbY5aIwTY4X9koGNvWketwRmYd6Dy_2WL9UH1mnmgrYQS6gWkl0ptu8KOrlnGgR1Hqh4PxDinbXnRFg9F3pXM2_7_B6xV-ur_9d748Bn7me6r0JoKr9Wsv043HX8wcztNsNtESJil_ZM7yT1WKRpqfIbr0-mVp9aP43Zser5cAtAQOE7IZyfYpt_CCB0RTleT9cSHwP5Xnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/22912" target="_blank">📅 00:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22911">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9d6ea65a.mp4?token=LuMFY8LJBiKeH9ZRooaVTHldpycnBAW5wm4mUQZihvpT5PIJl6VL1oqaiUHSd4-QQeKWpnnJw5O4CgpKrx7rKXvYfDljs2UnmaubTDtSMSxmbRG-8SyNLDChPcORS5G5puC68wats4YyeX6NCvpIf5KePhPTx_uFyeLbP25vk7mhxpsk1YMxEQKFUBacuzQqBWEy-So_1ZDWgN6diOTshGpJsL8seN-KYrC58qez9xE08evOBIELVTsgRb1_eKDD1o4RBo6EZ85Y5O4Mu6u7CRQiw3vuigY_qZCO-qMjJVd6ApHLlNduOYaWD4wf6vvCTKnH_Gab4ad_4TbqTx5ARg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9d6ea65a.mp4?token=LuMFY8LJBiKeH9ZRooaVTHldpycnBAW5wm4mUQZihvpT5PIJl6VL1oqaiUHSd4-QQeKWpnnJw5O4CgpKrx7rKXvYfDljs2UnmaubTDtSMSxmbRG-8SyNLDChPcORS5G5puC68wats4YyeX6NCvpIf5KePhPTx_uFyeLbP25vk7mhxpsk1YMxEQKFUBacuzQqBWEy-So_1ZDWgN6diOTshGpJsL8seN-KYrC58qez9xE08evOBIELVTsgRb1_eKDD1o4RBo6EZ85Y5O4Mu6u7CRQiw3vuigY_qZCO-qMjJVd6ApHLlNduOYaWD4wf6vvCTKnH_Gab4ad_4TbqTx5ARg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصدومیت شدید مهاجم صنعت نفت؛ ویدیویی که روزتونو میسازه؛ فقط کامنت‌ها رو بخونید
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/22911" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22910">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7334e55a73.mp4?token=hXYEpuRhlxtr1Wyp9KmRgav3St0x_xXtJ8arRyUGacc1OAcUXbLyH9RZdzJn-sjw3A8tDHaZfzk9gsVnYPRrBT_jN0CAw4Q6hg16OiM7eRug6lDTbQgG8fhco7rZEQdIhu2FBBZ_qfjsh5LzcqRBwz59rvhZ0aPO0SWGqP5Fa_ZdirLv8wSW-zx4H0PNsMdZXceLWdTfvpml-1q3O_FFB4ruo21yYsKtc3PiWBXFfUQFsV6N9FEEoYAK6-AiZ8kCF8j7vbiKLPOGh35XdxxcT3Tj8h2Lz5eqokF94oQOnU-gbBxbQCLxIMwp6M0_5ap96uYWtywHgl2mz8GJOhrInw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7334e55a73.mp4?token=hXYEpuRhlxtr1Wyp9KmRgav3St0x_xXtJ8arRyUGacc1OAcUXbLyH9RZdzJn-sjw3A8tDHaZfzk9gsVnYPRrBT_jN0CAw4Q6hg16OiM7eRug6lDTbQgG8fhco7rZEQdIhu2FBBZ_qfjsh5LzcqRBwz59rvhZ0aPO0SWGqP5Fa_ZdirLv8wSW-zx4H0PNsMdZXceLWdTfvpml-1q3O_FFB4ruo21yYsKtc3PiWBXFfUQFsV6N9FEEoYAK6-AiZ8kCF8j7vbiKLPOGh35XdxxcT3Tj8h2Lz5eqokF94oQOnU-gbBxbQCLxIMwp6M0_5ap96uYWtywHgl2mz8GJOhrInw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
امباپه27سالش‌شده؛هالند 25، اولیسه امسال وارد 25 سالگی میشه. اینم لیونل مسیه در 25 سالگی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22910" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22907">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c2e44c05.mp4?token=HYBxLWmv8IHNSF5tY_74JwT8KNa2IRiXuZs6M5luR8ofVMM5StGzss0i4fls1NsTqzVi-0jiatncoEI5PAABCeRZxhD7UjHcIxzWZX1O6Z2dl0o7b01mGLvVOMggCam_Yi59eIVmQxZ4E-4FMPUiBcLo4WxyMOx-f9CXJ2ojbEfDwSAhkUE4_MWHdAVUrtyViipVWcPreTzFLpO7szYHUd9EBwOkHinWJpX3glAezsdLQQ9e-3O14E2x_giibM8Ou-PyvARi1EAn8Yp61CGWeBTX7q1FCzqKwJrIqhQ6O8ZBFcpJ0HTA3CSg-wYHUmQH68TZoSndXGCMQOge-Tar5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c2e44c05.mp4?token=HYBxLWmv8IHNSF5tY_74JwT8KNa2IRiXuZs6M5luR8ofVMM5StGzss0i4fls1NsTqzVi-0jiatncoEI5PAABCeRZxhD7UjHcIxzWZX1O6Z2dl0o7b01mGLvVOMggCam_Yi59eIVmQxZ4E-4FMPUiBcLo4WxyMOx-f9CXJ2ojbEfDwSAhkUE4_MWHdAVUrtyViipVWcPreTzFLpO7szYHUd9EBwOkHinWJpX3glAezsdLQQ9e-3O14E2x_giibM8Ou-PyvARi1EAn8Yp61CGWeBTX7q1FCzqKwJrIqhQ6O8ZBFcpJ0HTA3CSg-wYHUmQH68TZoSndXGCMQOge-Tar5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وقتی‌داماد مجلس خیلی فوتبالیه، کریس رونالدو فن هست و به‌هیچ‌وجه هم اضطراب اجتماعی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22907" target="_blank">📅 00:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22906">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=qlg9KTBGbkq2rRdx0cjzcl8GNFmNWNBA4pIMZAG0aB3ivG23r_tfCSq_G6p3-Nbe5qmTY4V2qAbPoRW64-xwROsOvrNRdob8zKonaEHwl-9Otuvr-zlxUHI7IT50rq7cBH2pqxR8ERCYxHns-cJ59bBiVp7YTFhrOAl_6qhhiBU5mG7TWeq_dQCKliPiUlWFor79buv_TxCadR95f2MrK8mNrczIVn1S5rT2KZ1JEYoN5KW9u8r5ABqVSgsnW-26fwMfRue7Xj_bf1iH8e9WVJS5uyN8n_ANropG2lTGSt9DF0acfBsCfBwWdSi82SpId4XmeQPoVgh43ZbV9alciA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=qlg9KTBGbkq2rRdx0cjzcl8GNFmNWNBA4pIMZAG0aB3ivG23r_tfCSq_G6p3-Nbe5qmTY4V2qAbPoRW64-xwROsOvrNRdob8zKonaEHwl-9Otuvr-zlxUHI7IT50rq7cBH2pqxR8ERCYxHns-cJ59bBiVp7YTFhrOAl_6qhhiBU5mG7TWeq_dQCKliPiUlWFor79buv_TxCadR95f2MrK8mNrczIVn1S5rT2KZ1JEYoN5KW9u8r5ABqVSgsnW-26fwMfRue7Xj_bf1iH8e9WVJS5uyN8n_ANropG2lTGSt9DF0acfBsCfBwWdSi82SpId4XmeQPoVgh43ZbV9alciA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/22906" target="_blank">📅 23:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22905">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDZXWqUXvOrgKAv-TzszUJU3wkTq3CD8eKxPr4hC7B-xkeBDJDcrQp3zE5l8hUvbHxM3BJKDK8BWklIZEjsTHlEF6QPhK2aXIt6M9cBoEaOstEttH8BnGi8HauykRXkwf1gQbeirkZAb_z4MwsK7zKmLLJvXvQf22KnuSC5xiw-Eu4TPHkIN8BbKrHjdPbKy9Oco1CxzH7uLawZShSMyzY65cTdtmcm2DSb7VscK2nMNhShqYhlAJgB07qlLHqsYEm-Rlwb23JStymOSY7ywroyCWTAAezJrurIjB7eoKp68AMFAcrIXqci8jQf95S0Vftm5cONSjIGI0Vm5AimHeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
#تکمیلی؛خوزه‌فلیکس دیاز: مایکل اولیسه از طریق‌نماینده‌اش‌به‌مدیران بایرن مونیخ اعلام کرده که بعداز جام جهانی 2026 تمایلی به ماندن در آلیانز آرنا نداره و قصد داره راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22905" target="_blank">📅 23:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22904">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBtsbKdyy7dICaQS6FPY2Qte8sCWsi4oo0fE8ZLT1ukI_ajT2BBuyDz7GSheot7FDuLdhDF-m5tt3tbunaehqjfRatx7CKlEwoE5M6Q1Tz4XWvHHIje7xsiKVxa48ivwy1_sz3slrenT_fnEAlKCbv0DzaGtMiUaqrNuAVxd6lsux2sx_Q_0t3dTw_dK1iYc3al3hcLMEJklBlGaKr5sKqBROnsTUMUqIq6BeSPs6gUcvPjGM37POTnuT1UHc45ukJ43mHdogCXvy_YNywVT-wdQwFxuThpvoFky0BSN4WLE4Jo4-Uapqu1mIRN27UIs38d4HCsSXGjrvk7B-UdmAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق گفته رسانه ها؛ یوتیوب بزودی طی روزهای آینده بطورکامل رفع فیلتر خواهد شد و همین الانشم روبعضی اپراتورها مثل مخابرات رفع فیلتر شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/22904" target="_blank">📅 22:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22903">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RilO3Mt6H0Cp5NbO8OLXY-ysrRZNr6H7sa7tVK_ygms_Pm0Ozl6SDdD0OWmTNmPtbEElYhiKtGgrpsdTLQNdPtoKOQrilaZkWuYKrbYXtFrn6a7r-8CLWPfWb1-KizkMLaFSQz_G2lmS5WtooGBGlsrgR0EzNTUJQqJ-12GZRuKPO16EWMUiMqSihrOHgEhAeaRkySuiIc-3ebdj6VKZDq1GMKHcl2N7n63sK9iRRn-noWFOY5OzXLPrbZy1KIDZqFAM-60zdwv4dTSOkLMI62udoz-y6adBzmX2DclsKd-xTl7e8a0Id6fTR6FyCYor1TQReomF59oBrJCaiS2z_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌اخباردریافتی‌رسانه پرشیانا
؛ ریکاردو آلوز ستاره پرتغالی سپاهان که با شروع فصل جدید چهار ماه از همراهی طلایی پوشان محروم خواهد بود به مدیران این باشگاه اعلام کرده درصورتی که محرومیت او لغو نشود یا به حالت تعلیقی در نیاید قید حضور در فوتبال ایران رو خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22903" target="_blank">📅 22:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22902">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irjeX4Q_mS3XLlhGnbU0RRuR7XNwMo3kPzWqkZWxtKHZRMa_YzhSZbIBpVIrwncBpjOC0rriY1qUAk8sEb0KLb8cZfCZJLdarTd88WtTCzRQ8MSXHenqG9iEfRypZy9FVZjpSMtybJTpwoGpclpfQJkWInsElX8LnWQjx5b8DFZtnMSy9TNImSxxe6gGDTTSMYX90k7OM1LXkQyets5GnC2EbiNQdUslyxmoGksTYhnVsU5jnzYloRZU34PfoXF2K2VsJCLPFi-mLdaLD1_6nCyO3_L7i3Hi0Cw0mTqORqVt4VlsP9DIakPYiRIpbYjDHeB0xRYOLd1fBYXMoc4uXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/22902" target="_blank">📅 21:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22900">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c-Vu2qtT_HP-bIU5FRmvmN5LnjkWy8SKZ3GgK2IZP3XOKEeak8Ia1kuJsZX78HtsQJnTH6wzL8vAlvDWRsYDLngtxK1asqK4gkIVNeC1TyNa0xrXeeczCp-27JPVEOap3EFC2yTg7zU0xovTG5xvWrGcd8ie65Yz7-TqC6aBqF5mFB6r8DTYwXVyh2KBYjYjb0PNx4Qb-LG00QNK5edz3PCQ_7kJ5hDsT5VRZuKm0BFwMY-diObcJsNMMYvu_cqL2aBNW8ZczFsst-l1ArHCsn4AewgcB9MgYJSPhMi64w2tzK9FRGfsHBznucf6PWvaN_Y42EbTfhhZ33lDlwr00Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kKwV02JqQGORBddSR2L5x6HSoC9eJB4IKxxRhpBDHFi0bit1AfnGVviuwUM8xfqsmehyQZraijbjkDg-6I3GO9h4pVjCT2pm55Duy2x0XpkjM-uCsch_1_BQpCM41WFpJh82E8CuRBrJZ-UiGFu0TLK2uB88VZd05D5AdTohKk6Cc_WY0SFMrWJ1EXpChizXsQ4oW9-ftQ9EB5UDnJhtUzBEMDM7cqQyLGhixr90Wt_SwFb1H-aSJT2La3dDXRzzaLxTUt-w7jHH8v53z1Juz8ZTj0CkwB5zkjqJr20zZv-otPIigl1U6FG5czWsjO_TVvZwItn8MVwOHOKH44jmQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بماند به یادگار
؛ یه ریاضی‌ دان آلمانی به نام Joachim Klement که قهرمان سه جام جهانی اخیر را با مدل خود درست پیش‌ بینی کرده، معتقده قهرمان جام جهانی ۲۰۲۶ هلنده.
مدل او که عواملی مانند تولید ناخالص داخلی، جمعیت، فرهنگ و رتبه‌بندی را در نظر می‌گیرد سناریوی نسبتا جالبی را پیش‌ بینی کرده: تیم ملی برزیل در مرحله یک‌شانزدهم نهایی توسط ژاپن حذف میشه، آرژانتین تنها نماینده آمریکای جنوبی در ¼ نهایی خواهد بود و در آن مرحله مقابل پرتغال‌میخوره و در نهایت‌ فینال بین هلند - پرتغال برگزار شده و تیم ملی هلند نیز قهرمان می‌شود. البته این فقط یک پیش‌بینی آماریه و تضمینی برای رخ دادن قطعی آن وجود ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22900" target="_blank">📅 21:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22899">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2dJwveu7oEtQc4owt7UG_hNirQHsRBxZCX_1yE1468Z0mjocdPPoNlbuHHllX1C-F_TLSgxLKcJ-smeRaDUaJtCRUePmJolLKXtyDwgTCHXO-kCadau7jJFQ-Tst2ZKUFYvYnPsEwDwHuIol65e30CG5C8TWhNwB-1tuh1AhcLNHhOjQbra4hB-RH8fZ7XulPo_pYfEkF_I9z-qcXGy-daGImeDS0QM7zH0MViglaY_b07kVlCR8nHLnPOh5CWkDdm6buWujFlmWlI9Ri_2E2VKet4x4_cbKskzzBw5SHQVAUGNrkGCrnN2xUGM7u-pTq_iNp-Ok-bVpFVu8Teh0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22899" target="_blank">📅 21:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22898">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-QnMWYJL50iyT3Lj9z2fdeh3sr8bJpWoz-8xMD01eeAmj1ZywPjlYi9RVny9dvwuXfdbELbW4X9D0tqSW_AB_GXMW2hMa_9DMBqr77n7MVhcc148MDZxzdfMDEvPf0L9bV08Q_eYue6xqLPbB6eGDNmp7j8zPUwPRQoVFjtq64qCFzof2-InufJh9IVE6JRIGLMFjDktxPi9Ipg9JdOMELMUOVKi3lw57z5p3AVeEwgg3N0nfWlebckqFXkcV4tmHSW49h99vzbP-bFAoW7s_05y44lC3ZFdodDsX4d_o-xMyUTVMInQDsq_VgbH10ASTe_utjABtEOs_2FVXkiOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌استقلال با فروش جوئل کوجو به تیم نفتچی ازبکستان‌موافقت‌کرده و بزودی این انتقال‌ صورت میگیره و کوجو رسما از استقلال‌جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22898" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22897">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73008adba.mp4?token=JAXCYK0O4mRXtO1yQeWNqSun1o_yfdhhNB5EYwDU73aGNKDt5wZAOlbPlNf7mekRF0L2PT7_i55o8Isg67TI4-UBwBkF8Q5QWgEK6WwoZr9OJUHwiWQulEXQroerfpG3I2G84KLGEdJJYYRSlAVlsHhMKn_cjI6jNFp3JqXA80olGFMJe5CoY8pRZeHU2v_ICED1DkM3VZL2iB6D2zELYv2Ifp9XXG9WRkj7X6I-4j5m1Ia73tf7YY_O4dkX3HaySc41KFHMM1z-T-HXMfVhvxXFp2tVqMhEQrJ3ztKATRM5VZNuCD8JllNdGteKiKhFDZj2eNYdauh95VQlpmHcrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73008adba.mp4?token=JAXCYK0O4mRXtO1yQeWNqSun1o_yfdhhNB5EYwDU73aGNKDt5wZAOlbPlNf7mekRF0L2PT7_i55o8Isg67TI4-UBwBkF8Q5QWgEK6WwoZr9OJUHwiWQulEXQroerfpG3I2G84KLGEdJJYYRSlAVlsHhMKn_cjI6jNFp3JqXA80olGFMJe5CoY8pRZeHU2v_ICED1DkM3VZL2iB6D2zELYv2Ifp9XXG9WRkj7X6I-4j5m1Ia73tf7YY_O4dkX3HaySc41KFHMM1z-T-HXMfVhvxXFp2tVqMhEQrJ3ztKATRM5VZNuCD8JllNdGteKiKhFDZj2eNYdauh95VQlpmHcrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبیکه‌مسی شخصیت‌منفی بود؛
آرژانتین ـ هلند؛ یک چهارم نهایی‌جام‌جهانی 2022. درگیری بین بازیکنا به حدی زیاد بود که به نیمکت دو تیم کشیده شده بود و این موضوع باعث‌شد مسی به قدری عصبی‌شه که یه نسخه از خودشو نشون بده که کسی تاحالا ندیده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22897" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22895">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb1RcUZnLvbgkl0XeFbXhTJ15kYJepREfU2FKrUwEZYExo5-Rfdg1WVsDGrxRcSCGEHR44zCMUnvUmz1FJthfAegyBc2inh1o1NlJXcPqcxL5C5RpcxS16RV2-FjVdweeB7yBAysqdFmnRxDLOcn5tEzjja8U1HmfvVPKHTwbRiczvnkdLPgsb_2dmzpfXRmuub-_7FyE3YWHh0hKWrC_Q46T8oBKgiy5HZlowwc-U06y3CnOK22QoGbyzVoQ6ZfAZrLRUfeAMehYUrm4cum3-27HGZmV5k2asnPYj3yq2QLtgJqCc2YmJQqh2g7p-qUwEjoTnNQeAF5A0iQYCSAFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22895" target="_blank">📅 20:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22894">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc1ec4c74.mp4?token=ICYwwNUhqwlSVl5bnYS0gr2wdHu3TyVtdSwEGOlvQ5Qh1kygwrnWoqdUNJWT1u_YFRN9eEuwhEVqa-a0PPWpD3VTMHvwpiMsTPQkU4WOESIUKQ3pUx91Gc2n9DiLW2HmGsQsFKe1lE8dkCvtVeZQRTYxk3zlCXmC51r3qPVdlymk0AyuTo8HesLw68kmMJVQaO53gvIGWMa5rpMT0cqIkrRYlptIt8oIkWb5iueoWNcaeBr03lb7CfnThH_959Wp_7jZDNhseVtIxYUy13DfSqmsn68HV2cpI6Jn88XD7b433GGu4IpEpmYOg_Z3MugzAdlxPTxfs_fV1eRQX8JteA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc1ec4c74.mp4?token=ICYwwNUhqwlSVl5bnYS0gr2wdHu3TyVtdSwEGOlvQ5Qh1kygwrnWoqdUNJWT1u_YFRN9eEuwhEVqa-a0PPWpD3VTMHvwpiMsTPQkU4WOESIUKQ3pUx91Gc2n9DiLW2HmGsQsFKe1lE8dkCvtVeZQRTYxk3zlCXmC51r3qPVdlymk0AyuTo8HesLw68kmMJVQaO53gvIGWMa5rpMT0cqIkrRYlptIt8oIkWb5iueoWNcaeBr03lb7CfnThH_959Wp_7jZDNhseVtIxYUy13DfSqmsn68HV2cpI6Jn88XD7b433GGu4IpEpmYOg_Z3MugzAdlxPTxfs_fV1eRQX8JteA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇨🇴
وقتی بازی‌های باشگاهی تموم شده و از بازی در کنار هری کین میرسی به بازی در کنار این:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22894" target="_blank">📅 20:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22893">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojyHwvewES8A8GICzKezrKRKKrW2SYStfKDXTzgM4pyjkcNK-Iqz7_yANOpNJIvMuIN7DyKuV5MzkFMGKkknguvPq-gc2gZv1DhvK9sVWKaK1C5X1iIcAuPoDYB4m2lkXI-CnBPcMHT_M3DbnfTQmHCzV0IKQUTmB-NYH7mTfyBt2Zm2crWaHXH0ROO_Y38dVG3w4K5Ucbv2Jc9zHXfQksn7wYVez4UTz8iZ5FYoM9ZE0KGDVE74zC6RAuB91DY5bM4qqdv4deEM4_8GlqlGJ3toiwuxjG7bgylQHFoWr2tbHMQwGhomJP1-sRkYNZic5gC0RbLGGPIpaH-zYwmqJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22893" target="_blank">📅 19:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22892">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdA7H5R0JPMQUeFRBFGPWrNRGWHYYRMc7-R4-Ux4eTdbd8TLoWxaotsm8Vk2qXw2MNUrdCBjQpCQB3oLxvzIR5pHIqVLYStE1pJq9Ynp1hXZyEyVDHPJk3T5jKHM_XCdXeWIgC0cck2jMvFPEC8JYeS8_flUJj-dWB6kFvTDGbwCYNRmV-oAi6DK8kmGNgkNIUwHI330dfEFrx_eZdn4WTQnRSuwL-EqgCl54H1W-MNfgPbJYQYeQiA5jpReYpzLVyQhOARbKyvEfxaxcbVsjHIuwjrq2DK6ZBa6mMYWUinTJtu38sGy4h23kL0AMdIi7rnf57AzPx4cfAO41BL44g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در تازه ترین رده بندی فیفا و آخرین رنکینگ اعلامی قبل‌ازجام‌جهانی 2026؛ شاگردان قلعه نویی با یک پله صعود در رنکینگ فیفا در جایگاه دوم آسیا و بیستم جهان قرار گرفت. ژاپن بام آسیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22892" target="_blank">📅 19:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22891">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf50298d76.mp4?token=OAcqXnbRf19y6Ye7ClRUcPO8m_FoRwprsUibiQ8nRjDzYzYmORGnj8eMts1JTJjJ-X75ysHCkMAE375FcBDuoZh8MQQ7Ulo9UQ7QZtA-_xTcTfe86VQVV8nxf-aSlI7hKWe9Kkl0Z6nCUeh204P0K95EyZrRRBlURiR3cnhqbZjpGLTDbVIpR1R9VKuwOZ_FwbLbwVJZhs3JEBY4NePWexDJ0PIwjw4RkJE1TBOHixeLxH28izI689uVhZ6rR2GqisdIgoe-jL5lX-DpO6lPc8_B2z844aDZYv-o6KILWzawjk7Eyqe1xxdoIEJQi4ykewWLo3wZvYoYhuNGUjNsWCXnD0B4jPz-JjD-UiA3vKc99L0amU6WIKjmB89ysFgleZzQbftx6qGvIFj9qkG97GH9L9P4K4CZocX5rRq2IJo6DwBDWGQcGHq1E-_4r90GAg-cCO6Hp5cGtqToECARKCjIwJDtR0uqg8l8Qnu_AMCV0Dx7uCheQ0Ou2Z2tca96_n-ChGAguZ_7llLB5SvZtOjG0jcQVlV65ZrtRxxdk89u6h7vn8t2al_YAI0f2QkGWGvAZAWpi_IhwxptY9jFpnkfcrG-h28TnxmmBuAaioUzr2Wm8sbJpykzZbZfi61OkYi7x0ax0rLPW6ZcJuoIyPa5qcqUea4bozwIe3hIHnE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf50298d76.mp4?token=OAcqXnbRf19y6Ye7ClRUcPO8m_FoRwprsUibiQ8nRjDzYzYmORGnj8eMts1JTJjJ-X75ysHCkMAE375FcBDuoZh8MQQ7Ulo9UQ7QZtA-_xTcTfe86VQVV8nxf-aSlI7hKWe9Kkl0Z6nCUeh204P0K95EyZrRRBlURiR3cnhqbZjpGLTDbVIpR1R9VKuwOZ_FwbLbwVJZhs3JEBY4NePWexDJ0PIwjw4RkJE1TBOHixeLxH28izI689uVhZ6rR2GqisdIgoe-jL5lX-DpO6lPc8_B2z844aDZYv-o6KILWzawjk7Eyqe1xxdoIEJQi4ykewWLo3wZvYoYhuNGUjNsWCXnD0B4jPz-JjD-UiA3vKc99L0amU6WIKjmB89ysFgleZzQbftx6qGvIFj9qkG97GH9L9P4K4CZocX5rRq2IJo6DwBDWGQcGHq1E-_4r90GAg-cCO6Hp5cGtqToECARKCjIwJDtR0uqg8l8Qnu_AMCV0Dx7uCheQ0Ou2Z2tca96_n-ChGAguZ_7llLB5SvZtOjG0jcQVlV65ZrtRxxdk89u6h7vn8t2al_YAI0f2QkGWGvAZAWpi_IhwxptY9jFpnkfcrG-h28TnxmmBuAaioUzr2Wm8sbJpykzZbZfi61OkYi7x0ax0rLPW6ZcJuoIyPa5qcqUea4bozwIe3hIHnE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شنیده‌های‌پرشیانا
؛ایجنت‌مطرح فوتبال ایران که ارتباط‌خوبی باستاره‌های‌خارجی‌داره؛ بار دیگر ارتباط خود را با خامس رودریگز ستاره 34 ساله سابق رئال مادرید و بایرن مونیخ برقرار کرده تا درصورت تمایل او رو برای فصل آینده به لیگ برتر ایران بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22891" target="_blank">📅 19:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22890">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fdcd2c12.mp4?token=OWQofh3DmKZOsWUeLkJQUXxOXhjvwEQetcP5h2w3Y9wggzWUyLJ_lu-L5IB4-5-q-DvESNKwTkoNelGawbiPxyroHzShPzGNIFGxkovqA7eVnlf_D9UFvYgH1l3FZ_yeNGfvWrg3V-NT9u527UXHm1nHbq7hFESC5MqTYc8SfHxygdoEdCP3f2BtSnBEIVaPvZq7yftpeI9po_VePglcHBg3rItmWj_NRipgbiAm2A6GoUPPWkh2E4cgUDJScDQtjYPoozrkQ9MS4bzsjNGzFvBqol5RN9xHEDIa0dtR4_rdxrXd9i117Y6HDCczNp1LG2vIPupvDmxzJrmxOtrEQRnvAq8ztKb9zyhjmb7Ks24rbT4G9RdouCyIiyHYCsAjPlNzfsWQnQm4l-ooP0GlJ1kfZopZMAFNQjknMcEifDC9LVln3cntu5syaq5eYYwfCTuvTxurKo3WtiPd2D13eql_pIwOp_BxeDzZiD-wdFHoe5-oGQBYRSEIoz4j3L-PUd4OlxFf6Y4rDRQTOWqtfbpx006AK_R85eok_SdfFhWsIrtrsRmuCNnNLX97ZEIDS9yHN7Dh37rdCeMPa___zYrudviRmpI6wqmoaoXs5V0i_7Cn2u6dXyrftLrQH7UlnFT67110XFjufBUwfbfawscBae7Ecykyo_CUxjqBUyU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fdcd2c12.mp4?token=OWQofh3DmKZOsWUeLkJQUXxOXhjvwEQetcP5h2w3Y9wggzWUyLJ_lu-L5IB4-5-q-DvESNKwTkoNelGawbiPxyroHzShPzGNIFGxkovqA7eVnlf_D9UFvYgH1l3FZ_yeNGfvWrg3V-NT9u527UXHm1nHbq7hFESC5MqTYc8SfHxygdoEdCP3f2BtSnBEIVaPvZq7yftpeI9po_VePglcHBg3rItmWj_NRipgbiAm2A6GoUPPWkh2E4cgUDJScDQtjYPoozrkQ9MS4bzsjNGzFvBqol5RN9xHEDIa0dtR4_rdxrXd9i117Y6HDCczNp1LG2vIPupvDmxzJrmxOtrEQRnvAq8ztKb9zyhjmb7Ks24rbT4G9RdouCyIiyHYCsAjPlNzfsWQnQm4l-ooP0GlJ1kfZopZMAFNQjknMcEifDC9LVln3cntu5syaq5eYYwfCTuvTxurKo3WtiPd2D13eql_pIwOp_BxeDzZiD-wdFHoe5-oGQBYRSEIoz4j3L-PUd4OlxFf6Y4rDRQTOWqtfbpx006AK_R85eok_SdfFhWsIrtrsRmuCNnNLX97ZEIDS9yHN7Dh37rdCeMPa___zYrudviRmpI6wqmoaoXs5V0i_7Cn2u6dXyrftLrQH7UlnFT67110XFjufBUwfbfawscBae7Ecykyo_CUxjqBUyU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
5 سوپرگل دیدنی‌از روی ضربات ایستگاهی؛
از بین این پنج تا کدومش رو بیشتر دوس داشتی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22890" target="_blank">📅 18:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22889">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDvOXv5ei17vrEM00AP9K_hBzXm1bhPEfkojZk40akG1Ynrr2pZYtu1D0j1sR4yUAc0u9RUz_bGG2oM4RA6YafgrOVqAYtwX7UXR7leXyXsU55WU2IVGBY9MUbPmjcia27k0F4JHo6v0jfTplSr7W4FnB29a73yxHl5Ww3fHCqXXWpRjAjMMVdy1U4OLPWgsT7xWEIKFNjfkFo2_EWIKaJRfkdYj1p6FLfKL_zdVfCwxsfjadWKQZAoRn02KpGdtI4hwDh6I2rQeZVVb-xUtEvcbIvA77VQz5hMNfbkWXrUN9VsJA874ghD1bytw-ntNHFFJFAHTfBq3PmmO5z9qAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در تازه ترین رده بندی فیفا و آخرین رنکینگ اعلامی قبل‌ازجام‌جهانی 2026؛ شاگردان قلعه نویی با یک پله صعود در رنکینگ فیفا در جایگاه دوم آسیا و بیستم جهان قرار گرفت. ژاپن بام آسیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22889" target="_blank">📅 18:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22888">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb97f5a2f.mp4?token=pgpqlPYYYGRnkYFR6mIyjMu9bUXtaEuZ7mzxpNGpOlu5aeUuNfa2sTBHfAp_wf0CHQFdidJmES6pWoCN-CYq2UHgZviuMs4OWr8nZiLxJh7RjuVR8lHvuAqYrefuCfNyYgrUSOF9R6MMPudZ4zA2098MSoD3dsfmKAyLbY76w0G70103zpNH4NpozXNaV3tcLWOcjE9lHSUitBANyFR0GdcElZYUOpvy3h3A9OfJbJMDv9py-7zgowrGUZRyAjV2tvRlhPX9tkLfo8LqDSXEnq31aetTWwQGkO9fbRqsK6HtSTQbyOboqHJIJMFkYwYEc4AhzM3oK2um972K7hjiTZ5WQ5C4AIp7C6DW9B0Dscm80UVdasMEn16RsjJ63IhD4YJYriv9oWAZ59Ih0Sq7Fc9fbPSDrOYqo2dyXfugcn0si4BM09MYfqg3SD9jJX_gq8lg7MCqn0WecyKM-e_p7ZfQO5zxpN-YGNs2ESYRVxAP3OFgIVrl1fSlEvkL-SayA663W6CFhOph7sB9FN7MODypd43_aHaRSOQ2a19zg9rsv0N7c7UMO8Y_S_ARsYgTlGJYXpwFqgWNOXsWcSLcSWUWA7NcVS4Oq_r_pV7xnwreaUnoKCAbkI7Xdvf0TjcBjfx9CtjDAx2StVgzXJPK5ihCJi31ibD-4wDFqrHhaWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb97f5a2f.mp4?token=pgpqlPYYYGRnkYFR6mIyjMu9bUXtaEuZ7mzxpNGpOlu5aeUuNfa2sTBHfAp_wf0CHQFdidJmES6pWoCN-CYq2UHgZviuMs4OWr8nZiLxJh7RjuVR8lHvuAqYrefuCfNyYgrUSOF9R6MMPudZ4zA2098MSoD3dsfmKAyLbY76w0G70103zpNH4NpozXNaV3tcLWOcjE9lHSUitBANyFR0GdcElZYUOpvy3h3A9OfJbJMDv9py-7zgowrGUZRyAjV2tvRlhPX9tkLfo8LqDSXEnq31aetTWwQGkO9fbRqsK6HtSTQbyOboqHJIJMFkYwYEc4AhzM3oK2um972K7hjiTZ5WQ5C4AIp7C6DW9B0Dscm80UVdasMEn16RsjJ63IhD4YJYriv9oWAZ59Ih0Sq7Fc9fbPSDrOYqo2dyXfugcn0si4BM09MYfqg3SD9jJX_gq8lg7MCqn0WecyKM-e_p7ZfQO5zxpN-YGNs2ESYRVxAP3OFgIVrl1fSlEvkL-SayA663W6CFhOph7sB9FN7MODypd43_aHaRSOQ2a19zg9rsv0N7c7UMO8Y_S_ARsYgTlGJYXpwFqgWNOXsWcSLcSWUWA7NcVS4Oq_r_pV7xnwreaUnoKCAbkI7Xdvf0TjcBjfx9CtjDAx2StVgzXJPK5ihCJi31ibD-4wDFqrHhaWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
انریکه بال؛
سبک بازی فوق‌العاده و تماشایی تیم پاری سن ژرمن که ۲ ساله هیچ رقیبی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22888" target="_blank">📅 18:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22887">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3Jm37nnWVsvoHp7lhCLKHD3eyzLrwuoASK06xBTh-_itBK_xtRK24i4oVvSCRUt_T9akO2n2hiT1VzG2Mju3DhQfWM5EZVeT1jWxVKtURR3_nC7VUQtFTf3CiOFt2MxlHqUWX-pEWb00WFhfcPuCQGvK3MdYzSSK62yVTWwjNk6uqVerskPl1vY-wF7YWLv8TJA4mVggio9hXG7c-vZ50Oe49ugXlMUNo1cpSIoMTKaf-G8uVZl9eAPT6drOR8xuzPlj8i4gL8voqlgNkCuUEC-g2No0hyvN0fjoifAYlAVWXxPtrEUc8qa_04NRTu0aAvXX9H7ORctyujsdbk4bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌ بندی لیگ برتر بعد از سه هیچ شدن بازی گل گهر - چادرملو بسودشاگردان مهدی تارتار؛ پرسپولیسِ اوسمار ویرا برتبه پنجم راه پیدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22887" target="_blank">📅 16:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22886">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efa86e852f.mp4?token=J21U-8sHJSZUiW5cpLRW1z7bI9AV6XKHdZXP6fBrQee8Eufb_jtL9ddla_dEGUh_S8PSmSdUfSFWkFQphQ_qgV390zHiYKnSwtKq_omIBFfDZG-Zeq9NUVaWPBsARM-gr6hEmrzlBqSZNHwVKtdqWe7ateMiDsdWBGR60YsLNAMMC78E37ouj76flWHA-iRohUh7YEEvhMNVIFqdYKls2dvGxpXwkcTRMoq08QPv0KsSqhmbwoh2zC_CO_ogRplXcDOaq0bDpEfAlds4e9-LR1MAJ5g6N-xWYa28n7JkceGkLJJM-w1sfDXoYKshS247Rp3Dj5qVyu67DLsy2hslhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efa86e852f.mp4?token=J21U-8sHJSZUiW5cpLRW1z7bI9AV6XKHdZXP6fBrQee8Eufb_jtL9ddla_dEGUh_S8PSmSdUfSFWkFQphQ_qgV390zHiYKnSwtKq_omIBFfDZG-Zeq9NUVaWPBsARM-gr6hEmrzlBqSZNHwVKtdqWe7ateMiDsdWBGR60YsLNAMMC78E37ouj76flWHA-iRohUh7YEEvhMNVIFqdYKls2dvGxpXwkcTRMoq08QPv0KsSqhmbwoh2zC_CO_ogRplXcDOaq0bDpEfAlds4e9-LR1MAJ5g6N-xWYa28n7JkceGkLJJM-w1sfDXoYKshS247Rp3Dj5qVyu67DLsy2hslhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد‌هاوقتی‌میبازن
🆚
وقتی‌میبرن؛ لبخند برای پنهان کردن درد و اشک برای رها شدن از سال‌ها جنگیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22886" target="_blank">📅 16:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22884">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2MHjGd_kCM_pCklsp0fDwr493iVNJKFyz_jAp9fxNUsmr8ehqQuhubSM_nSXC2QS5QDHE9U9HI3RisQSpQe16XO7B9j5YGaDHGlGMEi2vWRYJDODV1Ijt2F5kuuEZsvZ9sPCP4Ngo4GE7E8mTZYbGwtmET2ShefsEvQIBle5u8Q_fhnl2UToPCKplf7oi4xwFHEbJnP-P-CpmymoueGTMaD0ZZvwYm_Qwyts6aWz7eoOqYDmTRsMKPL9O01sh2bwpoxD_QkaeWLQWs9kTrg5SHCEirjq08CF1CJiVfPnVulJ3t12g9OYOsvXOrIBL9KgcA-taTSf1mEeygbBOGyJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oxQvvTEuAukqzH6lsGrmHkywgICHKQkHLwoS6htwHKybRpjW53kHzt4t5d_8Q8bqRE66E7qg2zRknuUKNuZpy4lKWDgHs4thfGz8CFr6s_xtuwN6U1n0CLWHhiqz1e-vwriYwQdWy-t-g51ZX8YkHbHLjXpo8ivx3WSK7Hg4BFvKCdAZS3ZbaTzwKfEZiaNGLjBYCErYwuaISS-KMx6fRCTNskWbMYp6W5bQGytVApsVaaObpvsx_RVjCBVo5R1f-EQYKTHOdDEJEBB5YMzLbLTShjS069UHHk63s7plG_LryyfWAZ7Mukiw-VT448nNkVnwfpnIE5NDF0QTPeSyDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🟡
🔴
#نقل‌انتقالات
|شنیده‌ میشود آتوسا یوسفی خواهر آریا یوسفی ستاره‌بانوان سپاهان مدنظر تیم بانوان‌پرسپولیس قرارگرفته. آریا هم مدنظر تیم آقایون پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22884" target="_blank">📅 16:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22883">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWS6flNHjNoRoghMuezQFvmITQnBEke0JivPsXyfOJbXH-wqNXPb7zlCT8SK46XnJuHx72b9IpF3M-x-u783XJL3rQggrUn7HtKOd92snLpB0xwBHkJSrYZd9xU6mYgX0iOq3LZzwpjruthSFlH9yYyQ_tvQ4fUG3IXcSoY15MusPYn7bcL_H7-XezCTj0sBIuq_9YL4jJjKOupPk7rpBNkOPMQiwEmxRDOX2MIh8yAb18mIrs19wY3FRvKp9aXo5xPL8_bWR2t6Vgcgq1CKJSBL6bX_9UOtisoeNQBaIZDRwiHnRxkuN_zYItVSAetFUUAIAs-QG-tGY8QvbE82ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
#تکمیلی؛دولت‌آمریکا: به افرادی‌که حضورشون درجام جهانی ضروری‌بود ویزا دادیم. دلیلی نداره به تروریست های جمهوری اسلامی هم برای حضور در جام جهانی ویزا بدهیم. ما هرگز اجازه نخواهیم داد پای همچین افرادی به خاک آمریکا باز شود.
‼️
مهدی‌تاج:اصلا درخواست ویزا ندادم…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22883" target="_blank">📅 16:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22882">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWR4cdluYs-ttTHCh0P1vIXpqJAa1iqLRIqaWj1HEn0e0DNhwxXlppcwTK89giwWfDj_VlMBQmHf76TWO13w7CHNdD1is7P0tWNhBUmPQKLqjrbVUUgCB8zZoB89JSQ7PtU7Dxqy4sD1t0msVcqSj7zhKg1dgwXCPC3pgrRrfduon0uWw17RNjfJjwy41a1HmFu4ehnv4zN9fzzjQG-p_ijn_XaZD7UFD0MuOYSwDnj_s_VTqbAyJfKV7aDp4WfQY3aMjdjKExFwK8CtWyWZGz0iN94ISjSt25-qd2e_OMlZw4aJCgUaPy3NwViF1fhC-yYsAcLbT5_EFgjcOoXT1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22882" target="_blank">📅 16:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22881">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BARy3iEbID85QJ6KOHpTeuwqBHYw5oZHaXSrvsJqzteqjJNR4yJozmJDpPp4zSXGTW2OjCdLLfXc1cIYcY5vr62jMDKxcgYg0wHjpZ6FSmqnRQrUWGtELQGxQaNJphnB7FUccBjKHNeMK9dTN60kHRhswRqmzJemtohdQ84h2iKdE8Ig3Eex6qZRF1CMwLfqLPE3RV7y0Dwy24RoEgtdNYVcjH6ZqhLOY56148H0WOp7usDq-wMu-w3UEvqONDMJ28kCM4M8fOENOf5leamfEPjn2CB3BbKr-H09cnXpf4a7W1kIczjzYUT1v9V9RVOv64UzrtmKeeTGFOq_FQexcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/22881" target="_blank">📅 14:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22879">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBAakCviCabt4qT1QprJL9yby_9xCiZdXSdYVp2e1tYRSAXDE_GUlq6RY2W8n1pvvnaiUJRcF5wtLgPpYBMdvfFnOpsZ9_GSLoDvqWvRcknB5hHSsE41tIjA66D_YFn34Mw_8w_vTnmnfQuTboUAwY9yfDZUYTIcTHh1CZRDcxMZiPbHDL-t99JrnsCjuWcYx6wPLNJb7ovWHoIFSd8p4dBwHkj2EbbbY4RcoCQQ8dSJW_zArA_2l3LyFdzOFAcGzOTg1RFiPvhWIWkwHEUX26ouRLwShJgb-zD1kINzo-0KRBT2t3vcZOsTGR4TcLdtmKS_ffoGNOKC5-EThcqhrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xnd5Ibya6_Msgm6YkpV5TLCx1mLoJI0mA20zIWFfcwr0BdOjo-ENZCrNkMZPYwyHD6FS8UbiazBdXxND_a9XlHyc-p1-NSfBqz4A24BFj2oMuyqQ-ugOZ7C29yaYuUoiTXriZrmTCra9N4VvrrpOabhU2K5TztG85Q6XykVjBLiF9rwrbI7WKvnJphQKOn2TXOyADYRXtRKM12mebCf2ExcyumHE5SsNQ2ZQ-a-_IvKP8dj2m61Qvn4_6e9WMh1tlw-6wOHg_Q4BKeNKED5IAhjxqFk7AQ4woYsf2R94LkPYpWqJ3W54jzGWwn31MoV5WLBHdsMMb2AABFuQ_loiyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
خط حمله هشت تیم مدعی اصلی قهرمانی در رقبت‌های جام جهانی 2026 آمریکا
😍
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22879" target="_blank">📅 14:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22878">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G34GNTEElBTVUQdstPEt59D3p3kVGyrDAIGiY3XSdpUkTEhN_gz232xukO6vql0a3E7GQSBIOkmMLYURjFOp9c0doUgp4_4UFxTugjOI5iqffUpa1zQrgbfUHKgwEcRsojot5SzNbawVwJQxclvxAtMJ_nEGW2_wXx4qI26NhXB3_zztHW3twTtNGZJfSYpB5H6BKzj2jY7noMC0jiMDFXoH6OaVgcIZ9KzZijU7wo01LmJeLmT6LqkoL5F1eC2Wt0v_iOSFR5J-IbzGqin1hIduRIJ16pu1ZioEA_lyM2SiVTkC0WKHwHT3JmOehRUEQWibbLeZCKS_3ZAIzlrQ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22878" target="_blank">📅 14:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22876">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jucc9w1CuSJQPbbx90dKgqlUhrUgTQw2wsGUJOqyeSibJ92mSRA5DQ2N4vGdvJ9Dy7wSAa8_m2jEnZXMqLwbrfdBJpPhHMNIuhxXEyiN9OsweB07Irh_EAqeSu5lg9J4EZAp_vI7O2rSGx93tBa0pJqcUlCMo1qhhrMVgoxKRtn6Mqk0LNZRmzA7oTqSW5n0tvwetpZiCZtsGIAMlZG-MZ5jJdPtRXA8g6rYXznepYta96YkEcngEvMrPrfps508WJWum424n7pmn5yB6rnoMUfLbBfMdtlWTlrJWiBiv3mL1h36XSc5s4lDyD1wC-pD37cajD5MJjKMww3WNQE1sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال با مدیر برنامه‌های موسی جنپو برای فسخ توافقی‌ قرارداد این بازیکن‌به‌توافق کامل رسید‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22876" target="_blank">📅 13:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22875">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=hsAjTFqbxMhdsgw3MVrzcgSpSNirEt00WWAoXFK3i2VuoA9YrO-xdNuQC0eToNdrA22zvaDdRvLt5yGauNnjqkoLN6QC9PcH9Hd9fLMpgiKBW1J5K2xSlPaivi5R3lVCyjrhl9LpX4FH1rDGxefhIpx07wnADcS1-UOYxYf0J8REa5djj3EL-CyLZan6utHfeNzVYrBW6bU00l6SVwnMR6azU5EZeR7-I2MunIL4Si-56TtV7xJUQBIXUJJL9FUyw5roYnFUCw4qrHX208okPt0bDP2rOR510SlWYN2hKWMOzN0sv5VqqnBIbsiUloGqjpdg9ibU0OlMhc_gUU-6hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=hsAjTFqbxMhdsgw3MVrzcgSpSNirEt00WWAoXFK3i2VuoA9YrO-xdNuQC0eToNdrA22zvaDdRvLt5yGauNnjqkoLN6QC9PcH9Hd9fLMpgiKBW1J5K2xSlPaivi5R3lVCyjrhl9LpX4FH1rDGxefhIpx07wnADcS1-UOYxYf0J8REa5djj3EL-CyLZan6utHfeNzVYrBW6bU00l6SVwnMR6azU5EZeR7-I2MunIL4Si-56TtV7xJUQBIXUJJL9FUyw5roYnFUCw4qrHX208okPt0bDP2rOR510SlWYN2hKWMOzN0sv5VqqnBIbsiUloGqjpdg9ibU0OlMhc_gUU-6hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/22875" target="_blank">📅 13:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22874">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxx0DxA5quurNxZ1FaecxiSWYC7qLw_pd7aZdHwAILbLH3Fjk4kWyEjr8ebzyTP2cLygcwv4gx_hZA2fXltZbem5zIEbKT4VbThZ0CyW6rKzPM1NpnwUoLss59rEabYmajhf3l6wHgyXzneLDa7bhUk49xB7N7XWaSgcGFg3nVzIJjPKYk3fTjaPzArVqTBXVZkD1BKJWDxHMTXv2s6pqZ6D4D097hGE_xFMeEXTMp_vlYYdKW0ue4Dfd0RsyuvK_nD8EmEv6mz1oK5E5sjh21MPzKDcWAJDB3XAgMFfNaeGFaLDS3oaIA6WcSysiF70da0SdoyUpews_l4ogBVZjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/22874" target="_blank">📅 12:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22873">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8vsgVEOpFrrFY3HJJzLDSDnRRY1vfSaExeTv1rT6IxsNvmfN7YolZ0cvfTAId-TwbtFzgEGfK5TcEiWt2r_twPP9sPb_HF0DdYtlKfbY3IwQyFGRs4fq0lfZzaC_vQBEHrkscf9ZbqHaPhdZyxASRlfXsjjiwVqjWZATGMvoI_vGiR8MbvgOz6kt7wb2bRCmZMaXnFlzFOcxk3m5ESmoicSuV3MMOQqst6oNlYIt_wjVabRQbNT5EOEdgUmUybABd-60CAl-VIZuVXoB3MYGGgyWmhBV8dJSHrhw28gKwcnqwslY02a6bFfIU7Vraj7Js78m_LrnlXIMXRuKSU4mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
#تکمیلی؛باشگاه‌آلومینیوم‌اراک: در روزهای اخیر مذاکرات مثبتی با یکی از اعضای هیات مدیره باشگاه استقلال برای فروش محمد خلیفه و بهرام گودرزی دو ستاره جوان خود به آبی پوشان به توافق کامل رسیدیم و به احتمال فراوان این انتقال بزودی رسمی خواهد شد و پول خوبی به‌باشگاه…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22873" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22872">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSCh_IwAGS-70xKq6g6LGzKyNO8iQV_jM2HhHikTSySBvf-K3aOT5Ey1Wi7mSJEHVL0IkoacIjV8_hbFDOc2nSd8w1OOtVlmbAzjXQ6Fz-i9pa13N1oE9SFRHJKG7FyfbiLR0ErjWf_w0H9uBlmuXq-bD68cHRWbgVcqo5SNle-adEA7WhbPeOsfC2KQ-6nkohg3KG2HVrAquWgatw7p40g1S_Ni07NYcDZyOOLhHF5rWeUs3FXsvDxy1L6p2-qCqR_gYdXqcttn1SW0DfoWv7NScbIAXvhZ4z-c0SWMs0G5GhO3i2N22a7CMfdsCTu7VwTx9AzGsiTqdYhJfPKx0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل‌نفراتی که دولت آمریکا براشون ویزا صادر نکرده و گفته حق ورود به آمریکا رو ندارید.
‼️
مهدی‌تاج رئیس‌فدراسیون، مهدی محمدنبی مدیر تیم، هدایت‌ممبینی دبیرکل فدراسیون، محسن معتمد کیا مدیررسانه‌ای، مهدی‌خراطی مدیراجرایی، مسعود اردشیر افسر امنیتی، مهدی ملک…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22872" target="_blank">📅 11:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22871">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCV0MWmBfIdL5b1nF3v7TQ6BX6ssg9DbuJNVELqs5re-bCK_6pBj8JDYWn7Yp1gw4twGWN0hoznsl30ZlqdGLKwfy36lFghw04S5QjKk3m3qngWOSBPmocKYcTGjC-gbl2SQOWi8Q8R7rGW3aLSTljMJs4RICr51XRWOxin-VVDskIsi3MTYDMBjBnRcbWr_wrxS7RRraYLjJWU39bTo1zXGY-dGW5BMIS4jHt9ijxks_0mKyJLQcKbOxpBfMVZHyuaSUv4tGSENazLzWgYoKp5RNavles0hx-5mRMQJr8V-PVcK-npACkWZ8H3ovFUnu8z7YkJrJAMIR0ETYNcwfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام رسانه‌های معتبر خارجی از غیب احتمالی چندبازیکن تیم‌ملی ایران در رقابت‌های جام جهانی 2026 به دلیل عدم صادر کردن ویزا از سوی دولت آمریکا به دلیل خدمت در سپاه خبر میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22871" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22870">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35d2a48cbb.mp4?token=HO9WCFz9vG4Lj5mVwPKzWO5rFJweKxOVjkBjU4qoUatHh-6G2woJ0mRJBDK4wY_sU7J6V2p8s6A3t1th55EBxSENHVR9tbQ9_eDAKKWcFFKrrkG8BgTTd-Grt9bpLLJ24LTkW43b9zP9xNlSxbXOJ9ab1cUNx52fAThpK9pveOc6hPx1pKoWbFEwkD5RBIOWAPN_1phFwxFjt33sBOGcNhwX-uOpnJ4hAtB1Nirr_xBZ1YdVjgSlMss_4KD5-g0aqh2g_uM8Gx5A38eH7UP_6TY6BQdGPZWWJg5CIogq07XVjD2H2kzs4rP4n23CvbvtZLo5AYSwE23XwcCim9yGUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35d2a48cbb.mp4?token=HO9WCFz9vG4Lj5mVwPKzWO5rFJweKxOVjkBjU4qoUatHh-6G2woJ0mRJBDK4wY_sU7J6V2p8s6A3t1th55EBxSENHVR9tbQ9_eDAKKWcFFKrrkG8BgTTd-Grt9bpLLJ24LTkW43b9zP9xNlSxbXOJ9ab1cUNx52fAThpK9pveOc6hPx1pKoWbFEwkD5RBIOWAPN_1phFwxFjt33sBOGcNhwX-uOpnJ4hAtB1Nirr_xBZ1YdVjgSlMss_4KD5-g0aqh2g_uM8Gx5A38eH7UP_6TY6BQdGPZWWJg5CIogq07XVjD2H2kzs4rP4n23CvbvtZLo5AYSwE23XwcCim9yGUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
اجرا‌ها و موزیک‌ ویدیو‌های شکیرا برای جام‌های جهانی ازسال 2006 تا 2026؛ کدومشون بهتر بود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22870" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22868">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gT-wayj70lEPQv5wQ9JpZ9Y4YptZjQSaFBUchHxgdpCgZKTrBjKh8v2700kJV6VMBPQQrklY8hip9lbk-GmXkp6ltXHGG4fnKDMldAyIRtUzKWs_mEFcSaSw34GxkQjjtamJSv5O_S5bJIQiq_IDMuwJMm_KLBca3GEvKJ7GgKUIlLNlzOQ0a6vJEkr4Kw9ShwtdykEW89Ms4xIEb9WgWIAStWHlydd-mKBPE2bX2qbhiufAMzsZxwGcQt9Fj_4HScaWoTmuuk3xDazjyPTRKIKtZ7Ufns6LloJyVAsDdQ5demDgLjBD1U8uhJafR4d5PagXrfAqVOfJQLAKtmJOVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ظرف 72 ساعت آینده از لیست اولیه اوسمار ویرا برای‌فصل‌بعد پرسپولیس رونمایی خواهیم کرد. منتظر جوان گرایی و عوض شدن شاکله سرخپوشان باشید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22868" target="_blank">📅 11:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22867">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeWfFQPwwcvBPqDxw44gIvEJIBFvX_M2mrsYydblCwaX1l4Nfvww870yDPTdgoNdVfT8WSEGprlMozk-7PEW8bmV_Rp0pHg0w3L0wsIMzq-nZ5-7ebtRus6vWl7FPnEqHqo0nQ8XNlmK7zZPsqVSsg1bHR_2T_fGkXWIdMY5LFz4T5vAu6ww1SRlycWlKHzed7krWOzDT4TlkkOijO7tMYmoIN8vfx-X3dqB3Wk56ZpfWJ3L7bhYExRVHpTG1SNm5aKzpOGxD8xiazv5AtUkTinVZ7O0XGOyd9FqSC9yM_Oi-d_iPynrp5f1vNBeSjkrf4kXbakDkR2jnxIDBN6ADA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22867" target="_blank">📅 11:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22866">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=ZAthJspUxBevm-_Oh8jE5C6OmSb4DtDsEaiLkKWs-lm0VvqDdiXfUyYHXVQI7FvPbWZZKz4ioNMMXKDu9LP19myOydIStOKmhqhpESNb7EM_9ErSw1byPHtqsR4A1LZ6QDfLtSVr9qGQfeTxE1VTSks66mQJyZXi81HXKUM49be8-t6pkqdTrpk4V3eicEFjLYj6Q1IQp7-ofOKPuV-uj3dnvjNQOIsJ871mFsaqoD_P1mkwzWmBuBp8ru4R9QJA7ecWGO4jdPyeVskY20LrbK8K8-82aycXYHgc6YWCeiC2Wcwp4qlw3noRVhRhxevxNjE2M6SLO-eHPUVv6TlUKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=ZAthJspUxBevm-_Oh8jE5C6OmSb4DtDsEaiLkKWs-lm0VvqDdiXfUyYHXVQI7FvPbWZZKz4ioNMMXKDu9LP19myOydIStOKmhqhpESNb7EM_9ErSw1byPHtqsR4A1LZ6QDfLtSVr9qGQfeTxE1VTSks66mQJyZXi81HXKUM49be8-t6pkqdTrpk4V3eicEFjLYj6Q1IQp7-ofOKPuV-uj3dnvjNQOIsJ871mFsaqoD_P1mkwzWmBuBp8ru4R9QJA7ecWGO4jdPyeVskY20LrbK8K8-82aycXYHgc6YWCeiC2Wcwp4qlw3noRVhRhxevxNjE2M6SLO-eHPUVv6TlUKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تعدادی از هواداران پرسپولیس مقابل فدراسیون فوتبال جمع‌شده‌اند و شعارمیدهند که پرسپولیس رو به جای گل گهر سیرجان به لیگ دو آسیا بفرستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22866" target="_blank">📅 11:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22865">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">▶️
هایلایتی‌کوتاه‌ازعملکردخیره‌کننده مایکل اولیسه دربازی این فصل بایرن مونیخ مقابل پاری‌سن ژرمن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22865" target="_blank">📅 10:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22863">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9211e2c5d.mp4?token=AlxmbDdhZfyM6nbKgbKHcrQRocn6McNzdlgJ57QiFU-iH8aQUhNZWzgnbjlzvprLgtz8InASr41mzv-VrhGJ93vd0uPJnZ65zT5E2xTF2nnzaCwcGTEDh42iwLeYs1-sLT3J97mr_iom7IBnySiwKFEjMeUZSBw9foOLK3-_wD35CFZ5KR48zJEpDjw9SNJj8xaKrEYrEoKMsXTmKAPQovjAfxHpxN9LIfyOpeGh2E8x3HRLWt3yAelN9lJhMZ6sWyEENn7Bf_SQdnoc580OooDVEMEWdeDIjNK7KNWMKEnOU3KG_T-P8sPNhHsWebkstn3t5mkoxJHauVN2RosQrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9211e2c5d.mp4?token=AlxmbDdhZfyM6nbKgbKHcrQRocn6McNzdlgJ57QiFU-iH8aQUhNZWzgnbjlzvprLgtz8InASr41mzv-VrhGJ93vd0uPJnZ65zT5E2xTF2nnzaCwcGTEDh42iwLeYs1-sLT3J97mr_iom7IBnySiwKFEjMeUZSBw9foOLK3-_wD35CFZ5KR48zJEpDjw9SNJj8xaKrEYrEoKMsXTmKAPQovjAfxHpxN9LIfyOpeGh2E8x3HRLWt3yAelN9lJhMZ6sWyEENn7Bf_SQdnoc580OooDVEMEWdeDIjNK7KNWMKEnOU3KG_T-P8sPNhHsWebkstn3t5mkoxJHauVN2RosQrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کیلیان امباپه: همه فوتبالی‌ها قبول دارند که رئال مادرید بزرگ‌ترین باشگاه جهانه جز هواداران بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22863" target="_blank">📅 10:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22862">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVAPoaU2nTiWT_l3j7BDzEMm40S-x94qGP6RFh1MjsVZGhI8ndTZWm0k81tSrrn6SH3eLrIuUeRISuKXU2xKSEg2m1GRR9YORGJJ2BGnyJ0-QRsQA9_4Y9vwuYYWZLw6S5PAU4ZiILpF6ZTeSgcLpjsf1XBGwgiL8sXY_-1dC1DVFDIfmkxqrbcST5p-eLMdnelvhYTX6FYEJ0DlhVseHakXPdgkHV12rizWj4A8gmA6yLq8B51NXtybXQEGD2VH7uGvstJ1dDZ0alf8PcydJigPC9-oUw8KoFsD5NcHv3aRJ48Cp6kKxHLfNhFz_xzmibJl6SuwMYBByfbOFosFbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین‌سرچ‌های‌ایرانیان‌بعدِ88روزقطعی؛
بعدِ بازگشت اینترنت مردم اول دنبال چه چیزی گشتند؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22862" target="_blank">📅 09:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22861">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73764a80a.mp4?token=MfyOiEagH2KNexmJxJHQP3c6XIag-gTK-oEo4qZAYZekNmS-9R9vximg4psenJnFlUHzktt8AIkc6LFsP67KV7eJh0-64HyEKJrjpNheye8x1ACM_5PmZae7LfHhkpmmM9YEBQr0-sikFdh5DGBnIr7CFdeajCKu86qi1WvII9MLyNhlYZftPnnwlBQ6JiHajhhGKT2-XOzrYaS5n_3y5jk-TzalSN-4yneQxVJsvZ-uKnlj9wtGk_qtWoCP05q7hNg2sOqdRPFxC7ZEQ_YrsvIX45iiahrNjzla8PL-dYcbiXuF0RTzDqsyexT-Zhc982QRiRtVPAXf-hTwmrGb3l6Qo14Z5biEaZu7cSUD4lMHbcRBBbJ96Ea7oqTf4Id2RG86at2ID8BBpLq0BqrtTLC9RFXed-FgCphLp_MB4QLG1AijXUqXu-j1jQZnTW1OFPl5kdWZ7gkkpz7zg_IPVdpHRfZ6uVN4CZn0USc04I3dQ9oF-Wd-AcmmSlYhBS6U9dl7bHvEpElZ4yjxCfloNOmoxTySKhX7SZCIQj4ipkw7Txh_7diRRVcMQLHLdVQZN3dsR_KuWSKFtmOqAY61q8cMGmVenklt0PTclW10vrZDKcKj5QqXp8X_KLe0lQ_W-jMSVsLIzscGfvDD27xmWU1SpexBwxcj8gbpG70iyvE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73764a80a.mp4?token=MfyOiEagH2KNexmJxJHQP3c6XIag-gTK-oEo4qZAYZekNmS-9R9vximg4psenJnFlUHzktt8AIkc6LFsP67KV7eJh0-64HyEKJrjpNheye8x1ACM_5PmZae7LfHhkpmmM9YEBQr0-sikFdh5DGBnIr7CFdeajCKu86qi1WvII9MLyNhlYZftPnnwlBQ6JiHajhhGKT2-XOzrYaS5n_3y5jk-TzalSN-4yneQxVJsvZ-uKnlj9wtGk_qtWoCP05q7hNg2sOqdRPFxC7ZEQ_YrsvIX45iiahrNjzla8PL-dYcbiXuF0RTzDqsyexT-Zhc982QRiRtVPAXf-hTwmrGb3l6Qo14Z5biEaZu7cSUD4lMHbcRBBbJ96Ea7oqTf4Id2RG86at2ID8BBpLq0BqrtTLC9RFXed-FgCphLp_MB4QLG1AijXUqXu-j1jQZnTW1OFPl5kdWZ7gkkpz7zg_IPVdpHRfZ6uVN4CZn0USc04I3dQ9oF-Wd-AcmmSlYhBS6U9dl7bHvEpElZ4yjxCfloNOmoxTySKhX7SZCIQj4ipkw7Txh_7diRRVcMQLHLdVQZN3dsR_KuWSKFtmOqAY61q8cMGmVenklt0PTclW10vrZDKcKj5QqXp8X_KLe0lQ_W-jMSVsLIzscGfvDD27xmWU1SpexBwxcj8gbpG70iyvE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
#تقویم؛ یازده سال پیش در چنین شبی؛ بارسلونا لوئیز انریکه با مثلث خوفناک MSN در فینال لیگ قهرمانان اروپا یوونتوس رو با نتیجه قاطعانه و پرگل سه بر یک شکست‌داد و قهرمان این رقابت‌ها شد. این آخرین قهرمانی آبی اناری ها تا به امروز در چمپیونزلیگ بوده است.
⚪️
…</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/22861" target="_blank">📅 01:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22859">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p9EvlJGS-0IIc1msp44Rk0mplyOKuWV34KkWrdV_RAzzBfvLHRv078QPwUQr0aZ3ZxnrNKZ9xGBdykD80fLR8kXi7TW9-9mABKnjcssIHsHT4U9A4ZkrtRCUvfmYI6nNLA8FjSqE_o1HbMD60C_cT8FYirIrk05glQcaruQmYMWPRzvadtbk6lYdGPjg0qMsRQe7kmYv3LHaPyyZsw-T0uzHYdxYkcIdp_j2e3aaFMnlcLEcjM-uoapAjwgs8KBCB-eq8FdS9qE0AB-AMsHDkfWCsxqPM5sEBr96pzkxzEZWbHkuvMTRhhgfN6btTQeHaiLK2c85-ldhwXPIxWvrqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PB1JvNCTnWycxjSkFOTpx3zZVW29OqqinIB3rErx6xApc4IzQ5SjVIA2rO0Y2v-oZzZhC83K9bg__G5Mc-QFLU3MJy_k6PRidXCx7Yt-GIDEyiF0z9KDpNFph9_u7azNKOn79WYYx9rLwhvdOoEiaHMZSNRQIAAPiu4-Du5mvdRTK9QGsYZMzuXEb0N-80m73SGskiG2LuKYcW3hsiByWz3SWvkDxB3BcTj9wcZ_sNIcR1RjJ9_uB6mHf2bi0AyJcb0Qd_XznaNKaSWNIfKBU62w5mevaB-4wThEejFpQ4TvRsbO05BNUVq_C5bu_Wr5klifa69ktiAYiKbXQ_UxdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
#تقویم
؛ یازده سال پیش در چنین شبی؛
بارسلونا لوئیز انریکه با مثلث خوفناک MSN در فینال لیگ قهرمانان اروپا یوونتوس رو با نتیجه قاطعانه و پرگل سه بر یک شکست‌داد و قهرمان این رقابت‌ها شد. این آخرین قهرمانی آبی اناری ها تا به امروز در چمپیونزلیگ بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/22859" target="_blank">📅 01:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22858">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xz3DuUBZvSkoW2L6sT57-VwjUeQIzJEAo26QKEQeUXlrYI4yXRCRn43NHeJVL6GDKSbtLMpIVymFyWYw80gh3JZoR_Vatx6IgRVE-scFztBgwjq_42uW-CbBCRI3db-lGpHuB5_bsLMfqsCcltMtNKqFf--ZKBbPq8GWPGrPi_8Q9EWwJRlFqN-CJDfCNgzTFjzZRcJvJwCxrw_yQDZhfvqCSUjOkaEOdmtBF79ka4O8AXrsq7PqRa3Tum_RYBq-Pke60DW1ELzDI40Mjqy9UHbpPJ6DvxIQxQtM6dnWFEI6-2cbzAlDzzwaSpCP-lqaMmUnS9FQBTyE2B9RpuGbSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌کامل‌دیدارهای‌‌‌امروز؛
ازجدال‌یاران رونالدو برابر شیلی تا تقابل آلمانی‌ ها با شاگردان پوچتینو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22858" target="_blank">📅 01:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22857">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hK7Sd0I-7zXzuED5qDI-GD_ApPbpCZdRql8XOV0dpxwtCnpjqIbM1HTbyMAXhw4t3Bsc9MNMyaWxMP4DjEQS-azRiXYyCkpRpSzhn4jSCHffO0vSKOqJnq0X1yGmIbZd66dvyiO_dQeO8k6WsElwWrIlp_oM7tFoFcSYDRPl7zADnTiINUOo4fC8SIBbdXzs352ujz9Nq0c3CH2W62fbcnDuAotCJsuO9UjHuUbYh3XXfE3JmpRP6Qs_lEH0176czyaWvW_SbDWy3e_4qXbo7C5hdaWXT14gK8j4xPbJ8kO9PH0ZJYdO8N4YJkUrowziSw8-KFTAHj9aDqJq9irs8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌ روز گذشته؛
استقبال مکزیکی‌ها از جام‌جهانی 2026 با جشنواره گل برابر صربستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22857" target="_blank">📅 01:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22856">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H35AojbNIezp5yxZbcocCpPAFi6qnSnKjZfnVMRsSpUw4uGdS07hhDqYPno7b7WRzGPbPl_KqgsR9jwRg-1U0p7Fz123cXn92CIsnv8Xq8lhNlDzDvCqRw_FKNLUCUydEbORG2_jDgpyMOG3dchXwtcRXri1NhS5J_loi0JWIU_bhLaeOn4tedgPOYtjd5442-6v7tIbldIS3wS77LE4nd__zt3YSRuhPlZcdNkUQNpQxRgPgcnRdSHVk79TZciy8K7FvrZhMc0Jur5SCZq_IwMXAJ3K4Nrfh1PyMb46Xnye8Qo5L2nyBxLxHwQdUW5MMQ5nPMb3Z5ljdXzFwXMIcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شوک‌دراردوی‌ژرمن‌ها
؛ لنات‌کارل‌ستاره 18 ساله تیم‌ملی آلمان درتمرین امروز این تیم بشدت مصدوم شد و رقابت‌های‌ جام‌جهانی رو از دست داد. ناگلزمن سرمربی‌ژرمن‌ها بلافاصله آسان اودرائوگو ستاره 20 ساله لایپزیگ رو به اردوی تیم ملی آلمان دعوت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22856" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22855">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lg3BAJF_YOjG1GmkDn1TH2wLzyDIX8ti1LfKwRKz8mWX5CJWsAGbE4zBNd8KCzAn_-_YO0QJnCIa_xVuvf-VIlgROyK33reJSQE1xNSZyxeudnFesr3BoqvgXqyDyPE6Tzgd3xH1tQSwblbVFMoppSp0ej9BsAdSJxvOhSRb7bS2DS9fGDoPfljov5yG8Wi3UeRnnLzZ9Sy9fsyaCNkE2nSJe_3c_JYJZ7D3MPLNCNna0nt413HxuMgosnBOO9X_kG2QRWd4MUEmRe4BM-rZu_vR8-Wvbk1OMC1XmEDbBElrTppC2t4V0GZTtJ_i8boKO88gLeBsg_vwZ-EiPXRcXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛طبق شنیده‌های رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره ایرانی ماخاچ قلعه بزودی از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22855" target="_blank">📅 00:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22854">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifUMptjakNgzbiJWRsiBBeICAs_X1wv_RnDcin2miJms_RdsjxJBSJe_2DsYmvGnl72sKXeMpQwz_aBrkxU62k6TQTyWMJmo2wwHx74UvkDBrArgn353cvrLofzLHfl46U5S0LBiI3J14Qtq_Dp-e2C24nIW3PLZsMuIjCK26zYHW-_-Y1DGW8inrZhmTJ9NyLwwPMRG8FH-WvJ7-fYhaglCr2v1DkdN0eHrw7x66y4b_kaOtaMMu2XE7_cYQB9WpP7T_yhMkNkl0WclzCFgGhieB7OYeIrtN9livl0SrV5cFyIBDEkyUHonRGflm1ynLag8OAVpFbVR40BFwCzypg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چت‌جی‌پی‌تی،دیپ‌سیک و گراک بدون فیلترشکن در دسترس قرار گرفت. همه برنامه ها دارن رفع فیلتر میشن جز تلگرام،اینستاگرام و توییتر؛ سه‌برنامه‌ای که بیشترین استفاده کاربردی رو دارند باید فیلتر بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22854" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/NeDnU-n1HsV2ECaadhJeWzAy7hxOTmaza1KHJwzd570GgiL7PbNbmXiYrsedGnaMlfVeBUmYGAXCE_Gnc-QNRvFfR4SArASGdPL7X3Sshfnhm9AunJie9y3a2h4i49XFOhoizDUMTU7k1X6Hw0p3VGagb5NAja6-oBbTxA_i3z_urUKdtBvLTlAiz22Pb_RkBx6qZTCxvCbAoAold_GQbNjSXUnsipX1nRcrlT729wV3YvS_6s_TMOcn5Kk-LS2_JSawIIS0yXigr4oRwY3G6A_i8g5C6AD6ThzKzHtsS17yF5Jk0HvRDVc3HXesTGal9dRo9iSt4cc41wmdP3Y3EA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 441K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 05:55:29</div>
<hr>

<div class="tg-post" id="msg-30648">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4ToOKUxahh7efxXzjwLhgZPFKYlgtix-M9d57cpNgBnQI-a7RTCqMOG7oXZbyDV6Jl6cYIAcFSGvD-SoJnB_H_RvuSHXBF_T6mSY1EQwb7WlqIugC8LoZkCwA6SkAEOY-sa7incd1HyGJyM22ydWraiEfyUep8TlFzzONhL76BdmAh2DcAsR_jF9EAzNZS9PiNLVY-yXkWUaSEV7LZh0e4kgmgDIjSmSI6LnovMX2og5sDdHsaFlWAqUg9KcXm7JtQay-kJF0otB1Pz3P7JYtG9VbBRk7uGCtQ06NuzIEW_NIBgbC2Hw_kAc9a4r0Oz4pXT3LMtRVf2FjPzdmErlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ ازتقابل یاران یامال و‌ لوکا مودریچ تابازی تدارکاتی شاگردان قلعه‌نویی با روسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/30648" target="_blank">📅 01:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30647">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPfKeYXYVrtFRP4dx5lwctmPwaissS5d0vsBNZQUrIoESPqtjHSIVpZiqSsK7y91Mhz7VpMcAq8ABif2afwckwSN5tvvCKYRL1smqjfRjWKMA-KEgPvmKUQGNbzGg01uwGYWRz03U26Ump1XzTxS_R3C30fvHepN5CVjVfvlr3gIY6QBI1WaUai11RCS9YRXOyILDrzDrKYgTTc3byD8gGTRHIrpalSpwaXBr86ejr7ppiQ9Er5LIniVzwAZV_vjCfMI9oIR9lpF8XIvQyrkWmuyJGZJ7UdoayzROuSXdUcuuWzJQrTwZLEDvKz3mNG6-dNZe2kFIcrPmPWnQ084kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
دومین‌بردپیاپی خروس‌ها با زیدان و بردقاطعانه آتزوری در خاک ترکیه؛ برای اولین بار در 40 سال اخیر فرانسه یک مربی تونست در دو بازی اول خودش دو برد و دو کلین شیت ثبت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/30647" target="_blank">📅 01:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30646">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc93b6b651.mp4?token=u86MCKNKrqRoPCbX6Ssy2QA_odwxMfcMnc0Og6JP7QY9irwyb7OzRttQJesGGAzyRGcZlZHTdXUuJ95S_1FbVI0viGSSKpZxY1_TTmpF_PpxkEKjNJBCrK_6OMw79KXxOYHB_tSvpAmMjxj1zofLswKVOU-8sVZvaQ2sub1Q4X6eVMCDmBYdJuXR_XZaX97NyMqzciwwclEdC29sqsYre5FfK3iK6-U9wzSJ-6AJZu3KkYVonVm-lh9_l6uMN_yW9P2OohwIwGlh_l4F8YaheuamLQAq3wj5sbREApLgDpiqBqJklqknZj1dO6OyT8yEeHgJ5aW0snMHe2KOkEUq4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc93b6b651.mp4?token=u86MCKNKrqRoPCbX6Ssy2QA_odwxMfcMnc0Og6JP7QY9irwyb7OzRttQJesGGAzyRGcZlZHTdXUuJ95S_1FbVI0viGSSKpZxY1_TTmpF_PpxkEKjNJBCrK_6OMw79KXxOYHB_tSvpAmMjxj1zofLswKVOU-8sVZvaQ2sub1Q4X6eVMCDmBYdJuXR_XZaX97NyMqzciwwclEdC29sqsYre5FfK3iK6-U9wzSJ-6AJZu3KkYVonVm-lh9_l6uMN_yW9P2OohwIwGlh_l4F8YaheuamLQAq3wj5sbREApLgDpiqBqJklqknZj1dO6OyT8yEeHgJ5aW0snMHe2KOkEUq4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#تکمیلی؛ گل‌های دو دیدار امشب ایتالیا
🆚
ترکیه و فرانسه
🆚
بلژیک در هفته دوم لیگ‌ ملت‌های اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/30646" target="_blank">📅 01:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30645">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df13bf46f7.mp4?token=hmUNYoy2V0Iy8pkPs4eY1Zsg0IkZ1zsuWyN-0lo1MULsdHuIwkRPFkSMM8rC1eAcJNqBABeSwAgA37dcjm5xZCuVj55-MN6rek8gHrewmuL6h3jfqGHW-6JQVU7Saemp-lX9fJdL3QW9H5cnaTk6L61uTXq31gwVHFmMS7wELnuzgzv20zsR7IBEaH5KKreSWvmNZEKkh0K7f9R1AcUs2-_pqPnpY2O3KCDx2GhaYFQ8hmzMRXrMH0NDETMYQclPxGht0Z-eDSX2jbxBz2ZjOK94VqWR2z_5XCREofefbLpGbpVMIP602vNrGUB6AOWmydOg5mR0Jp5_WJC7az39LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df13bf46f7.mp4?token=hmUNYoy2V0Iy8pkPs4eY1Zsg0IkZ1zsuWyN-0lo1MULsdHuIwkRPFkSMM8rC1eAcJNqBABeSwAgA37dcjm5xZCuVj55-MN6rek8gHrewmuL6h3jfqGHW-6JQVU7Saemp-lX9fJdL3QW9H5cnaTk6L61uTXq31gwVHFmMS7wELnuzgzv20zsR7IBEaH5KKreSWvmNZEKkh0K7f9R1AcUs2-_pqPnpY2O3KCDx2GhaYFQ8hmzMRXrMH0NDETMYQclPxGht0Z-eDSX2jbxBz2ZjOK94VqWR2z_5XCREofefbLpGbpVMIP602vNrGUB6AOWmydOg5mR0Jp5_WJC7az39LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل باز هم تو برنامه‌اش از خنده منفجر شد؛ خودش خراب‌کاری کرد کم مونده بود که تبلت 300 400 میلیونی‌رو به‌چوخ‌بده خودشم خندش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/30645" target="_blank">📅 01:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30644">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5Icr5xwQIqbclN9ge-D4nUuwGAd5vv8bLr7qoHOVoEf1Ad__Nhw3CZMyhCWu_YQu7qEaxVvLV7ZPIEIgOC7ZLM72FF6pxkoIahny55RR5tcMjC7vMp_P28e0UfhcHCjXGRSfup2zbkDwVB0UPcE7d1cQU-aB4lRzl7K460J4HQvt3yGB16ltZLbyKSort-Ou77rjPcrFBsMhcNUyu-nNoIKQZZ5_KwocQJ4H7nWWWq17-4HqPraob3x03BUxfJQKBHN07XAN6RUJYeN47BrSE2k78aBxsq3KKVrcgSBVNyKN9VZymCULQ4vpEYXf_94YR1Z4N75fkI_CU9BDTHqxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
داداش فوتبال می‌بینی ولی هنوز ازش چیزی درنمیاری؟
😏
⚽️
یه سر بیا ایرانی بتینگ
👀
👍
✅
تاسیس‌کانال‌سال2020  اینجا خبری از حرفای الکی نیست؛ بازی‌های جذاب رو بررسی می‌کنیم و فرم‌های روزانه می‌ذاریم
🎯
📊
💰
اگه‌دنبال‌یه‌کانال فعال و رفاقتی برای پیش‌بینی فوتبالی، یه سر بزن… شاید همون چیزی باشه که دنبالش بودی
😎
🔥
👇
بیا داخل، خودت ببین چه خبره!
p6
🆔
t.me/+3P2wZvzhZbsyY2Vk
🆔
t.me/+3P2wZvzhZbsyY2Vk</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/30644" target="_blank">📅 01:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30643">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3RV18_w4bjs5BGaLMizdf3_d-8RgaLezy-oPMj2JN7cxWqXBew1kLYN5a4qEZdNONtWQMLBLH4ufwJCG81HY5VeR_z1vc-G51Og5FC4gZUsJgrbvj_lDKYzmcfgtrasADFJyYCZug1tzRPincvUWNqmXWKGPsMc5rpIFRk-1KUwvegs7VCHKQgAL7MI-EYRKv0mTSI6mrSkJZmu1hSZO1bRjdr1-Fy7ULYFIU7lDJAMGrDiX97Ff_Kqn3hK-fWtL6hcEDqeK2oyefESRQD0ITn6x7QQlYutLnUal8RMkyiAZB_RWEIxUGDAhPqdTt99vzjz8PBSDbJIDxByMtXVdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی پرشیانا؛ علی رضا بیرانوند در جمع بازیکنان تراکتور از جمع شجاع خلیل زاده و دانیال اسماعیلی‌ فر گفته درصورتیکه معافیت کامل بگیره درنیم‌فصل راهی باشگاه استقلال خواهد شد. این‌ درحالیه که کادر فنی استقلال فعلا علاقه‌ای به جذب دروازه بان 34 ساله…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/30643" target="_blank">📅 01:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30642">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY6TjKE_4DCpr-qLG-FQGSmK6zLc47Hg0a-88PUSg7aALSYZptftbzTlqp_e_72VLT1pZhTAnurSbl-WIMtqq1OxGg9SKOelFgifzW6vdl8YnwbXZd4Sdb74MSQHsjJXY1Vjb7NW_lSKdaiDJEtg5pqo2zo8NZP-AnP9lw3DNThYXWe3QNMY9Z0ukw5XsyMdRJRERdmGd-_j8B1r-NGjA1d8MmgLBGFVc7c55O7SsbY62tuTEbC-ZzTZrIZ-5LKOq0jZgDOUWLHvicsNzG2dhoP1oMEBN8jAC696qwe1kOYZJZv76emwFsU1Hz-coHinHL-bAmKLwSHkH7bJ4UDv_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یکی از مسئولان سازمان لیگ در گفتگویی کوتاه اعلام کرد؛ روز شنبه هفته‌اینده پرونده قهرمانی فصل گذشته لیگ برتر برای همیشه بسته خواهد شد. امروز در این باره به جمع بندی نهایی و قطعی نرسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/persiana_Soccer/30642" target="_blank">📅 00:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30641">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇪🇺
نتیجه دو دیدار مهم امشب لیگ ملت‌های اروپا؛ آتش بازی تماشااایی شاگردان روبرتو مانچینی مقابل یاران آردا گولر و پیروزی سخت و خفیف خروس‌ها مقابل بلژیک با تک گل فوق ستاره باواریایی ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/persiana_Soccer/30641" target="_blank">📅 00:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30640">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgVeTZSK3zVwOWWcBL3zJJFeK-8Qo3R20jegFMH6VyqDTQgdxCBcPletDCy_xYw2LpYAy23RnzThoMdoUskez7pPoO6FVZ1JaHqeMwd5S-K0TaRCknG1EQeRCnboOvSqbaS4FK8dralCpsWBPEnSPKgXN4QyqeKGXnDZTsSgrZa5axmHFJ3C322MuMO3zOdminVz4Ov70MgqQ7HtHkbxbyNxyHpda0vMhEmEFGoj4e6LSLUXLwibklfNAdb6_6SRehKt85bjA51NUxY5RocBSguTzRiyb4fBmpTAdPNFVfdFBa8aTe4BIla1gHvfJQRq2gurohtw8tj_rXrLlZy1LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌اروپا؛ شماتیک ترکیب دو تیم ملی بلژیک
🆚
فرانسه؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/30640" target="_blank">📅 00:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30639">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd8e0f64f.mp4?token=IrQgQv5KwdkrF5PelfiG4o6m5FAIOx9raYXZSHGD5xrCXTNq0A4WVwGl8soaqhqMwHF17Ul-b4eGC1XfOLoNdhtS9GtyLHo9Ym8rzClwRxtshhBD2fTZbhefRSrFEuHxFWmbar-bU1jn4-whbgwg7SjmYO-dmoIS1ZlemLebGgEjQ6mWS66FtrGOPUZTuw5Q8ZSvolwgV-seDrK-LJWc5PAQhXI0eLy0ag9B6BOu_wYcKwVTzYxWRwmtOqCZ3uHl_H63IEfAFhV6XJZ5Mv-7J2rAG8lkPjuFsTvhAWckmu37nL-a4PJsRB2ZMp7wRmTKEDAVGNc-nwDlKcONnojN3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd8e0f64f.mp4?token=IrQgQv5KwdkrF5PelfiG4o6m5FAIOx9raYXZSHGD5xrCXTNq0A4WVwGl8soaqhqMwHF17Ul-b4eGC1XfOLoNdhtS9GtyLHo9Ym8rzClwRxtshhBD2fTZbhefRSrFEuHxFWmbar-bU1jn4-whbgwg7SjmYO-dmoIS1ZlemLebGgEjQ6mWS66FtrGOPUZTuw5Q8ZSvolwgV-seDrK-LJWc5PAQhXI0eLy0ag9B6BOu_wYcKwVTzYxWRwmtOqCZ3uHl_H63IEfAFhV6XJZ5Mv-7J2rAG8lkPjuFsTvhAWckmu37nL-a4PJsRB2ZMp7wRmTKEDAVGNc-nwDlKcONnojN3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛صحبت‌های‌احساسی یاسر آسانی: بااینکه برای تیم پرسپولیس و هواداراش احترام قائل هستم امامن‌هرگز به اونجا نخواهم رفت. البته که من میدونم شما پرسپولیسی هستی آقای فردوسی پور! جلالی گفت من باپرسپولیس‌بستم توم بیا گفتم هرگز. اگه استقلال من رو نخواد از فوتبال…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/30639" target="_blank">📅 00:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30638">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYlQ9b35lkAGMhF0F0TP4XzauC1b_3QJZ6k8C1d9DJxiJvzy28PwOPsHu8qtykNbgVz9RU_NAhTI_kojBOzSNpfB02vpsNDI2G8EPJFAiUeKNRfX4QBmxE_1hl9GnMcJMgAfjCwrbJ3_fJoEY5y60HctGnt1IWft9HeQ8-G2NqqC-XA9hk1cloEvmH3OkGUIKM4-yRbfsL-Ze0nj6yHx_cVMukTxllBkaSK6pAllS2RwxTt2cTKRMKinhetdrIVi96V4NWnPnYmGdf-oYPdxqnR0UCgA6WWc-QFnmfccRzj1qO636OXp8nGHLd4JqV8c0KVLGfvSof2T3V6GN4-8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
لیست 10 بازیکنی که در رقابت های جام جهانی 2026 بیشترین تعداد فالور رو دریافت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/30638" target="_blank">📅 23:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30637">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
تایید شد؛ حسین عبدی سرمربی تیم‌ملی امید از هدایت این تیم استعفا داد و از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/30637" target="_blank">📅 23:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30636">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیاناتوسط یاسر آسانی: باشگاه‌پرسپولیس بامدیربرنامه‌های صحبت کرده بود که به اونجا برم اما گفتم علی رغم احترامی که برای این باشگاه قائلم اما جز استقلال نمیخواهم در هیچ باشگاهی بازی کنم و در استقلال موندنی شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/30636" target="_blank">📅 23:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30635">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aab94b2bd.mp4?token=KQA8q-ExTQApYgop_WA4TmScXHEEjoB8B4T-8HpuqGy5Tht6RUQc_Rd60p9QOmlL4QaGGs7cu3LLgi4moGk8Xv0lDLTpiiaTSm3YP5jRPDajKkVa8HD64OO-IsqgXOJFumbGp_u_-l2uz36TtSoF-WakTFXFuM-0nS-rP-m-5QiibNGqzvfJ9BUUbzgihXnaiNlCzAisrGJHDf5OG7N4D1PmB9mSdVbY-V_GVNs7sOxBLKgClovJjmWzcG_gUrYcEt1wb-ZEdpPdMs20cjCfSWLfqSE2L2tq8DotX6b3ousl3CC7AXpj11alSvG-I7WaXEopGUa7giE5yDRBspm42miUjkp41sWktoFghV-X6KQm1S9CKDIq_WaKdrN6yagCzsM9C4DgbEK82V6_oYgADsFPLC8yPLidacmKyVbeUWZzgSeuGVAJAAZzN7SUi_nsPlCXhG3mvLQvQnADCW8GDgyo68nlcxhAsR6gphUWMnnu8uiMDp-Ycu--BOZnKqrShXacxlnZ2bFPxY3vymF3-UEWAhZ0s2PkH_AyvBFyaIjSa7ywWBLz2DEy-QS7istYjI_T0HUPJ7A3dKA62PsbsDNRAXR5lLXJQloZQ9PjnkWRxfbJcPQThwkljcwfSXOuj4n-zj3PAPgRqZo-Gs89OpXbEMzU3N9BcTmbFkHpa4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aab94b2bd.mp4?token=KQA8q-ExTQApYgop_WA4TmScXHEEjoB8B4T-8HpuqGy5Tht6RUQc_Rd60p9QOmlL4QaGGs7cu3LLgi4moGk8Xv0lDLTpiiaTSm3YP5jRPDajKkVa8HD64OO-IsqgXOJFumbGp_u_-l2uz36TtSoF-WakTFXFuM-0nS-rP-m-5QiibNGqzvfJ9BUUbzgihXnaiNlCzAisrGJHDf5OG7N4D1PmB9mSdVbY-V_GVNs7sOxBLKgClovJjmWzcG_gUrYcEt1wb-ZEdpPdMs20cjCfSWLfqSE2L2tq8DotX6b3ousl3CC7AXpj11alSvG-I7WaXEopGUa7giE5yDRBspm42miUjkp41sWktoFghV-X6KQm1S9CKDIq_WaKdrN6yagCzsM9C4DgbEK82V6_oYgADsFPLC8yPLidacmKyVbeUWZzgSeuGVAJAAZzN7SUi_nsPlCXhG3mvLQvQnADCW8GDgyo68nlcxhAsR6gphUWMnnu8uiMDp-Ycu--BOZnKqrShXacxlnZ2bFPxY3vymF3-UEWAhZ0s2PkH_AyvBFyaIjSa7ywWBLz2DEy-QS7istYjI_T0HUPJ7A3dKA62PsbsDNRAXR5lLXJQloZQ9PjnkWRxfbJcPQThwkljcwfSXOuj4n-zj3PAPgRqZo-Gs89OpXbEMzU3N9BcTmbFkHpa4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/30635" target="_blank">📅 23:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30634">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWYtdOX9yMf5K61h9HnXvQFWWdt9G0lF8EDp89uoEBsT2yZYu7ZvvhsFtCx0opfyNsgg9DN9Vlt5FhV2sA-THxNG2_oWapxQKXXV9R8FW-IT8b-Pl3Skj53TAF6UA6y6HJCwecWtaTFkKa7in5ak_l6OioTV-ZcB0FUdpkwCKRQDRC-gmMmpXe4JLYzkOwtlBQLjcmQPZOC3yk6675-N4EAZjwTGw-vcF01XOY7--8ye4GaaZMtwljd0z_yVoCCtI5Vw1qyWN4NJMuQ9d91uJp8fOSJXzmpkBLTytfLEqaKWjofLq3hma824qeVYO2sKNrA6Pxbuwju1cxtYFuWLRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یکی از مسئولان سازمان لیگ در گفتگویی کوتاه اعلام کرد؛ روز شنبه هفته‌اینده پرونده قهرمانی فصل گذشته لیگ برتر برای همیشه بسته خواهد شد. امروز در این باره به جمع بندی نهایی و قطعی نرسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/30634" target="_blank">📅 22:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30633">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXHG1ZBplroLpeabxZCPx-4KkJlSTj4Dyf3qPvnZHj_z4Mhrba6EBonCYNROHfQVv2opNjdLI5NcGM4vzlbqN1hI45f-EWeLn5QUYXzmUMZZDtEsIWmp6fHadYeN2CNk5uf8i_CG5J-k6tXe1xG2JpyfpxG9dl0Bl5BsiinuoNlDFsceeKHNEFs7H8-in6H_F6TZohqTe1hRp-FvV8TPTHyLo1ZVUqibwwxd3OehfTnYkoZydB16-u25rnz0QaygiaVjcAqFRLVZqy6BIopZR5W57vvkCgHYCTa9ObkYfzg31c8W63ODud0iCRYY1z4zS7k6jCsQ7WR483E4WCZHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه کاشیوا ریسول درروزهای اخیر پیشنهادی دو ساله به ارزش 4.5 میلیون دلار به یاسر آسانی ستاره‌آلبانیایی‌استقلال داده بود که این بازیکن بعد از مشورت با مدیر برنامه‌ های خود این آفر رو رد کرده و آمادگی کامل خود را برای تمدید قراردادش با باشگاه استقلال…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/30633" target="_blank">📅 22:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30632">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efdabf6f72.mp4?token=exgBbilKwuUIdViEYhvx73S4-dqs-VqTdvTGrbvfGTm1Thqf-XNk3XI6qJd49Ymt6LarbY6rVskKK7FSd3kHF4WAKG86XAZtGpt1sgQNO6hgU5EE6oKRqiZE9AZVrbPWTSzloQzUY4MXuUPm_Erj0M-MfYT5qfSgD0jFC1j-ZlYScyBmMzl4O-UhIv7idgXVcPNpe8nu2gkCN2IuBtuYEeDPgFRZnqKK4-8LxL0IIMIkhA3GKZFXzsWv3dazoc_gT08PQ_Q-UxkzviGVNd4xUa3Gwb35gotMcxnz-ZbvP-iOiQfxkluLK2bJB8QfrNR-eSdqbVS_lPcmpCh2BHYH3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efdabf6f72.mp4?token=exgBbilKwuUIdViEYhvx73S4-dqs-VqTdvTGrbvfGTm1Thqf-XNk3XI6qJd49Ymt6LarbY6rVskKK7FSd3kHF4WAKG86XAZtGpt1sgQNO6hgU5EE6oKRqiZE9AZVrbPWTSzloQzUY4MXuUPm_Erj0M-MfYT5qfSgD0jFC1j-ZlYScyBmMzl4O-UhIv7idgXVcPNpe8nu2gkCN2IuBtuYEeDPgFRZnqKK4-8LxL0IIMIkhA3GKZFXzsWv3dazoc_gT08PQ_Q-UxkzviGVNd4xUa3Gwb35gotMcxnz-ZbvP-iOiQfxkluLK2bJB8QfrNR-eSdqbVS_lPcmpCh2BHYH3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
پست جدید سردار آزمون: پاراگراف اولش رو بخونید. رفته متن رو از هوش مصنوعی گرفته دیگه فکر کنم یادش رفته قبل از انتشار ادیتش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/30632" target="_blank">📅 22:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30631">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPhoJbLc4K1t4Bi9EllpaSLNJf0F_lCJlp5mBSsxdpsGZB5uqZke2l1_ruf4pIYs1X-_fiow7_lKFjuGSwzlavnq7FTClK2Cpn8xJXcZrhmcUNhPmiXgdWURy_XNOPMe6NOgZIDbil8hFS5ZP3GQIGozZIAqijE8s67iprIxNECY9fLs-GxZQhQLarf2XQxkf7-Xpq88SY_DocuBCQ2sR0JBjeGKZk5jTOvUrOAPQiI7i7RtlUh1U-c4Gz72P16HXTKbFZqHMv20PuR7Wa0UeUT41_JHZQzyNbeHRwERz1pYuEn5HXpRkuOcoXg9xIXzzyjc437nN-8gup1r7rxS_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنی که یه زمانی در دورتموند آقایی میکرد و به یک‌باره‌سر از منچستریونایتد در آورد و کم کم افت کرد در سن 26 سالگی سر نخواستنش دعوا شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/30631" target="_blank">📅 21:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30630">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWy-YdvDmTfPc91jz3RywZEHAGEeFtK19A4L1dP6G5n42-dTvWKoakGPEfB2HP2XYbbFPOBcL7BHGCGHzSDEGkP0bXd7K05YQnVHDDCFdcTTnVBgbuf0cwX0bEor2hpW-Oak_SogwLlJjSIJm3id9OJOHBaBuholZe7AvvNskm-hk6ILF9Xl-alpVLU636Ze_xCOfMS5IVe7Tee_iQ8qN8nWxwYgvTU0nRN4MCk5YUvbQnozNCEuIZzFizPcOE9F6gWwDyeSF9fXXxfkL4U5TdHU0qJ1kjWB1byzN2fmtMUEJK08hmTnfiWCS021_r9wTmaAnGr0JLrFIwQuTnUlRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رای‌دهی‌مراسم‌توپ‌طلاسال 2026 دقایقی قبل رسما به اتمام رسید و از این لحظه به بعد برنده توپ طلای 2026 مشخص شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/30630" target="_blank">📅 21:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30628">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qbj4JoSxJJj4U9Og02u9FtfN7V1pRXQyTq-74lPSbpUEhEqYN2DY9t7oSXXZnrG9IXZ6QW9dp8OdTfBwebdTChWi4aUjcgRVqQwKeSEVN3-tN_qWHCZYS3KUT_atKxp4NGW2t_9OjsrihALlZhhdSHLmZhOBJrXI6lInL8-9mrkCxsWkqNt7umH14ziEU6PJcwihC9awz5YoTK93d9I4ObkEkGp7HpR-Ce2CnD17UQJ2QvBS4zBWPf4PeOWK8hQLLQUnPfZru39B5lIkY__wTveThwC1kCITySLpN-z_ucElM5SZDIBgFc81yN1RJwj283QADTGHvTS5QYHdQva5hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pj82N7KtlFGFduJq2Ikg7ALvMmj69AyzO7QU2p14DKJ9zOaDim8xhxwx5r7zYmmAVRhVT_-HzoE9ydegElkhc2XWMf8HahiAGcPXypCC9nO8sIBwiaQ45UhzBeXsOdwXwHBM_7omYPZYNVi3REvIOsX5nnX6qaDf0gcwv4gtIu7wLLzUSCLdNKmrX6sW3WjGPB3zygZJ7aolm1cL-yJCpkFv-TNiA2kpa33mgoAJlWGvBMGmBeg4iv_WMPYjH_vKIH1a2YMR428KxHzesvOM2nZn1iPOlyJHlPodPEpxEDVSfAYHqS7Gd8MHpOKZictasj66wG1wX1IwuqfFoh_V2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌اروپا؛
شماتیک ترکیب دو تیم ملی بلژیک
🆚
فرانسه؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/30628" target="_blank">📅 21:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30627">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmGF3UX-xbvuKxNEOxvD2gQZqd-ku7kYH1SUt0T5aNf99FWZX_wSG2yyCXh-w-zgUKYO9AKRijM2feRW_WziaSsDMahLiEK1Jr_e7zg3AhVWpMS5925VByRjFItM-MMr7G2IL2SRoQ7_0MHwD3UMdFMu6irvrrWAFWDCCKJ3mpyrpB4PqG17imLWVA1Rnnnu2PaxkFs0pnG66YjbTo7wSB3l_BvGG-jvsK7POpoUj8Xvh8vtSfrQqv2GBKZI4U61YUa42PaskwoiZOQOZolBtXRDGdKtspACOLp_u-CFKitIA-b2vn00ln-W6yjjh3zjXRngk-6A_yUAl6gzQkosxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جلسه‌نهایی‌اعضای هیات‌رئیسه فدراسیون فوتبال برای رای‌گیری‌درخصوص اعلام یا عدم اعلام قهرمانی تیم استقلال در فصل گذشته لیگ برتر از دقایقی قبل برگزار شده. تا ساعتی دیگر نتیجه مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/30627" target="_blank">📅 20:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30626">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgGm4pEFXjGJyaVehHAsiBvvY58B-s1hfT9YfWYNRy3NBOIFbKVTHrZsj3U00geY2bV_dxyTEfhdxaldImZWFFBBTim5QhYLF8ARxIYUGHluvS9eZ_SyD4O8AjkSLXdJCIf_xiLhd-cktmVDsrZePPJXU-mT9_X36VZBRTgc-S3GtEEpH2B2oYpm7Qu_T0HaH4tcU4yUUllswEZWMgM6P7QjktFLalrw0DntnvIFHSdSQLYhCLuQIyxXBTj8CGkTAY4QWIpve1L0ue3JK828exTHga8KwoqgilehovUdhkpx_Mkh3j2-ed9xLg9HFWP5SvkgWOG65HFyO9FPbOtH5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارزش تیم ملی ایران داخل ترانسفرمارکت به 25 میلیون یورو کاهش یافت. یه‌چندوقت دیگه تیم های اندونزی و اردن هم احتمالا از ایران بالا میزنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/30626" target="_blank">📅 20:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30625">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/769a519ca4.mp4?token=a-JGq64iObWQWurpGR5RZrZXgIcdXVV5OA36bgebhf7b2V93jY5KayKFw6j42Ez-x4uu89LJr3ngog53_AMFHTmBcJ0cNHy3LCEXB34ajfb3iPTEHlFmvi6RuV_TMwfR2jq5VEys6C8y_3nq1ORfwvNv_NHJNFg1-EfywR5_JQh1r49Vzp87TttXzcU-V0dVMZ6tg89yW020n-Mxwz75Dp3RloWkzY8zLKzn6RaiHTcN9j5seQisxrXsuoDf9QDZkYfwdbinIC2dQKG52oj3SCUplpJunAo_0oSkGUqKnc1ayWLXrHcwHtrWyKjveuWSSFQ66ANyJ9-twnDGbbPeJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/769a519ca4.mp4?token=a-JGq64iObWQWurpGR5RZrZXgIcdXVV5OA36bgebhf7b2V93jY5KayKFw6j42Ez-x4uu89LJr3ngog53_AMFHTmBcJ0cNHy3LCEXB34ajfb3iPTEHlFmvi6RuV_TMwfR2jq5VEys6C8y_3nq1ORfwvNv_NHJNFg1-EfywR5_JQh1r49Vzp87TttXzcU-V0dVMZ6tg89yW020n-Mxwz75Dp3RloWkzY8zLKzn6RaiHTcN9j5seQisxrXsuoDf9QDZkYfwdbinIC2dQKG52oj3SCUplpJunAo_0oSkGUqKnc1ayWLXrHcwHtrWyKjveuWSSFQ66ANyJ9-twnDGbbPeJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
حرکت زیبای رونالدو برای هوادار نروژی
؛ یک‌‌ هوادار تیم ملی نروژی پیراهن تیم ملی پرتغال را برای گرفتن امضای کریستیانو رونالدو به سمت او پرتاب کرد. رونالدو هم گرم.کردن را متوقف‌کرد پیراهن را امضا کرد و دوباره به هوادار برگرداند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/30625" target="_blank">📅 20:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30624">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712c04d04a.mp4?token=nsIsIKSxBc7g6X_80V210go2BUN8zsNNh8FPTLtb89e-QHdbhyZwpWZxJF1NwcK7yIyQ1lN82rsDy5wHskzFhrtJHVujzWprWz-hn6ZVPSIak-TprEOG2xS-OJCTHTcitgI-HEu21A-ZS_H2HDCCyZIQPvt_lcHNwQmRCNJwnUtUI5pDnkWvbPVHawkuZln9fdfYhoOV1CLv5X36JthnF6yyQ1_owEhV7ch7mid5P4mHGFRHIZnibBuAf3Uv8CBGSv6zShmEPXHm0HF9m2cEZ68i2ZhBDfm5HVE5OXNqYrumMYD2uJLJNl-097WH1OHEMANo40P88rlte3zB04WEvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712c04d04a.mp4?token=nsIsIKSxBc7g6X_80V210go2BUN8zsNNh8FPTLtb89e-QHdbhyZwpWZxJF1NwcK7yIyQ1lN82rsDy5wHskzFhrtJHVujzWprWz-hn6ZVPSIak-TprEOG2xS-OJCTHTcitgI-HEu21A-ZS_H2HDCCyZIQPvt_lcHNwQmRCNJwnUtUI5pDnkWvbPVHawkuZln9fdfYhoOV1CLv5X36JthnF6yyQ1_owEhV7ch7mid5P4mHGFRHIZnibBuAf3Uv8CBGSv6zShmEPXHm0HF9m2cEZ68i2ZhBDfm5HVE5OXNqYrumMYD2uJLJNl-097WH1OHEMANo40P88rlte3zB04WEvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
ویدیویی زیبا و ساخته شده هوش مصنوعی از علی آقا دایی اسطوره تاریخی فوتبال ایران و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/30624" target="_blank">📅 19:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30623">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERNgPgdxVDOc9ew31SPNgUqvB7PArcWT-dN1MzrVPnpiyyM44aJx8WbH-LkG3_jhxyyFsPXSFwHxk5pHsvyK0zBcg73Sv0s6KUJTgvCaUVhuPri8TuX9tWYX_OoXrLU6_2P4-6QugnnRLxG8Fw_R0Jwm8LiTpcDF06BQ5MYTmxmZ2PHU4UGMbLeWJgv6YLoKSej_9i3kh08vM5cGDPAw7o8EQe76LMQqnge2TdH8IcrcZIumR3v67z5QNNgY_TzECXTqZhV-ZUlbj5WJJvATF75PJcOMZ02EeCJK-uYr3xMrpWZSrwkoDYCDG2TnEFSWisXHhbBVyb7dSUqQaOJv1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریه‌آاس
:ژوزه‌مورینیو پیشنهاد سرمربیگری تیم‌ملی‌پرتغال روبخاطرپیشنهاد رئال مادرید رد کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/30623" target="_blank">📅 19:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30622">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/808bfabc47.mp4?token=cIrmWkE8c2seGETIquXLwj88EQvpCUyWm8eUMoF8TE5oOMN6vvBhErHqUtUMbJwxOzq6I_q8bE9vNZhP25_B1bMBSs3BYL890cTN6LLss-PRpEkD9LsvzZB7LEwc0mzi2KZrJQpvNwiUpA35oZAbHGy10_lvYARo0-GxGYhm0k-SbLKDI3Aq7P3WcWYFIRB5jzdt542jfGfEjmuuMkaPuLHrLM0Q0XkYxffGNQIdlc0jARobUlLIXSe-69BXgAmKkSfHg2hPr0BMjMfKBWn_-aMms932Ajw7_EuOKFjRssk4IOv5ESpAOGvALdFt_va0s-RkOQajv6u9w_LdTJ8GJar3lpii55wgw2Fxv0Co3e8wGSZ7nBIaWhjAB-v1OzxWshXjSTY9UIAB108KmlvaG9UUfKG9mKbvM8MrsqtKYGcLTXDyd_AyEtJ0q3KgBHUcoXPSL9rUCG0BBThxJNR0BZcE5yGd9Jlu8CO9xeVFoPIQfFBNViYpaEWaUThXlcqcd_Yiwbytj7IHJ-xy0f2aDeYqF7uEh9TZPG-TwUwnw0V6CE3sq0oj8qgE3KwePw36V88n23uJxrBeofWYccIg3sCEj6zcL8zM6HEP46Zx1bySacFRxVqMBcoS5uy9A7pPjmAGsLJxT5O3yd8y63hzzbRkYy9MQlTUyba4i5QE_BU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/808bfabc47.mp4?token=cIrmWkE8c2seGETIquXLwj88EQvpCUyWm8eUMoF8TE5oOMN6vvBhErHqUtUMbJwxOzq6I_q8bE9vNZhP25_B1bMBSs3BYL890cTN6LLss-PRpEkD9LsvzZB7LEwc0mzi2KZrJQpvNwiUpA35oZAbHGy10_lvYARo0-GxGYhm0k-SbLKDI3Aq7P3WcWYFIRB5jzdt542jfGfEjmuuMkaPuLHrLM0Q0XkYxffGNQIdlc0jARobUlLIXSe-69BXgAmKkSfHg2hPr0BMjMfKBWn_-aMms932Ajw7_EuOKFjRssk4IOv5ESpAOGvALdFt_va0s-RkOQajv6u9w_LdTJ8GJar3lpii55wgw2Fxv0Co3e8wGSZ7nBIaWhjAB-v1OzxWshXjSTY9UIAB108KmlvaG9UUfKG9mKbvM8MrsqtKYGcLTXDyd_AyEtJ0q3KgBHUcoXPSL9rUCG0BBThxJNR0BZcE5yGd9Jlu8CO9xeVFoPIQfFBNViYpaEWaUThXlcqcd_Yiwbytj7IHJ-xy0f2aDeYqF7uEh9TZPG-TwUwnw0V6CE3sq0oj8qgE3KwePw36V88n23uJxrBeofWYccIg3sCEj6zcL8zM6HEP46Zx1bySacFRxVqMBcoS5uy9A7pPjmAGsLJxT5O3yd8y63hzzbRkYy9MQlTUyba4i5QE_BU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
👤
ویدیویی‌بسیارجالب‌از آنالیز تیم ملی فرانسه سبک زین الدین زیدان در اولین بازی با هدایت زیزو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/30622" target="_blank">📅 19:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30621">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCp2ywMX7zrPRAZP43oSCgX9yfhtgXLXJ1mZ6frB4sszk3gy4IHsLRNaWEiep0kwUoHU89kEz3DQ2xn5zxII4SKoVVOUQLC2q0I6MmZENwd6q8DcHYgbfGv3c4nupnPo4EHQ9aLlnFfl497SW-7JX1THosCrCEhdREk4bgv2V2QuV7L7KfaFxydTlM1mQf_fg22QBUlR5c4z6llR9sOOaXzVLEdjtCAuu2OgtaPidTEMYkZpXaOg-zsokzHTL-scaaGzll0qvPIdD3CdceIJQJS7EoYzxB_dMM7HDe42AAb7T_HPztScs3bK5dBq-XhX-gKr-OF4mM8G8gv3z8CcpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💖
خیلیا نتونستن از فوتبال تا الان سود کنن، ولی ما امروز با فرم هامون
400% سود کردیم
که نتیجه تحلیل درست و تجربه یک تیم حرفه‌ایه
👌🏻
هرشب بالای ۸۰درصد امار بردمونه
✔️
میگی نه؟ یه شب
بیا آمار چک کن
😄
فرم های مطمئن امشب فوتبال با ضرایب بالا از دست نده!
👇
👇
👇
https://t.me/+laf8I3RIuq42MDk8
https://t.me/+laf8I3RIuq42MDk8</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/30621" target="_blank">📅 19:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30619">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e3BU4ce7ENJIDS7n5CuQ19UvScgCnvr3RCDa4jBxSYYsg2Zr9Po7MkehTRoFDW3wV95UcjoJ-MYoCyKgmROB4jf7nLV6SW57tLHO-WPKrV5_Fs5RaxdO6trGbUbw2e52ivB9ZPkZIf9OgVF0R7JVwoNIiMKd5E5RwsjVMmlRYD-Nqlnj0uSZfD7aTml5TWXLdElHb3dFS39mATg89TGbN8KQEsZGUbTXq9I5XNaGm6HczFSfIKADWIJg3wp1zZtqebgaQ2FAI_SmTBtC8g5zIj5nwNHQmEBl0lmA6m_32dIVsox4hKWmHZm-KPf1o7K5JGF7CqbvctP0nHGF44MD_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eNWX8DMgiB6HVPpUBucP_M2bG7C7X3bv9NFIldgLIqqzpCN3ok5ODButtkRscQSLJtsm77lTfGKxge-gIlpOYcGetQDRRrTCMAeXga_V2IYbaPdlSEkHdUa_gvJUfchzrJeRnVxoUanJBM3FqwFeGKwZqy1PDDHPo-EGCe2DltYRE--KWGI9nBCTv5eihiGY5p8C5KOVdcO_926EV5dmJKQ-dNg9jDjwTLSn80IBKykWZEHnytWQYITT7jfffmlr7yh_txD0OJGO-150HP8cXxB0iLcfEvIhJ9UMKsLD5q9epNcuQUYW3diqd2PLh_T8K5LX-wWA4bJq5gofToskAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
جدول پخش‌زنده مسابقات ورزشی در شبکه جم اسپورت در هفته پیش رو..! این پست رو یه جایی سیو کنید که مسابقات رو از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/30619" target="_blank">📅 19:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30618">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aede9d046.mp4?token=YhTHsdh8nK5x6TbMm6r14d-dIUJv7rpv-jHUfV4dFN3pL1rV-5S74yJDxVJV23E-qcfwkMXaIBGMzFQYa_oIF6sdlAPQpbV7Ax3_C3eE_9E-p0OeXsTCAAxGIOkKFjuBUACBiwYVH26GR4qkckv18JnfuiRRdi7icvmCj3bKZ8pl_pxGhRAUydEJoEyIAVGYWWitLWqyE_IARqjNTDNhM1bcILxyrgxp0sBKH4mkEDAORm7-Ogax6UAB3FnjA9G1h-XA-2_c-wtAGoG89NHkVVP21-YYqg8KGdFkQrewbp_S-Dn6u-MfVkeSH9aeaRZWSli5lmNh60hs5kMitXSxew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aede9d046.mp4?token=YhTHsdh8nK5x6TbMm6r14d-dIUJv7rpv-jHUfV4dFN3pL1rV-5S74yJDxVJV23E-qcfwkMXaIBGMzFQYa_oIF6sdlAPQpbV7Ax3_C3eE_9E-p0OeXsTCAAxGIOkKFjuBUACBiwYVH26GR4qkckv18JnfuiRRdi7icvmCj3bKZ8pl_pxGhRAUydEJoEyIAVGYWWitLWqyE_IARqjNTDNhM1bcILxyrgxp0sBKH4mkEDAORm7-Ogax6UAB3FnjA9G1h-XA-2_c-wtAGoG89NHkVVP21-YYqg8KGdFkQrewbp_S-Dn6u-MfVkeSH9aeaRZWSli5lmNh60hs5kMitXSxew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نتیجه‌حضور تیم‌ملی ایران در ادوار مختلف جام ملت‌های آسیا؛ سقوط تلخ پرافتخارترین تیم آسیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/30618" target="_blank">📅 18:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30617">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmsQb83asXGLQxOn7_zvrKByF92W2bjFRhLKrJCR3kHFcmVTnFTksucT3euhtK2rdRMZJVAE1ac7T09dh5h_2f-SIWZq5jw7T45rUxg8wmYtSRDIeOmijTkvc0iAKES_bTddYWlFUADoZTkyh54DiLmd1IF37ID2K646fcA457YfPnut7E4tg1hX4wFsvcfIv1cpAIJNqcYQ2vUmxGUUP4vM0rSnVyQJ4C_z5u7URYyxQmToFc8BXuvXS6QbdSp2ePEUViqYNNaXIB8QpEPKBwyh5cbp41ItwZk-ziERUTdCucj9FjuOsKLzfUufBRH7dpolptATiIKDEuzfeFXCig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ فکر کنم تنها کانالی بودیم که بارها گفتیم که رئیس فدراسیون فوتبال به باشگاه استقلال وعده اهدای جام قهرمانی فصل گذشته لییگ برتر رو داده. حالا هم طبق شنیده‌های رسانه پرشیانا تا اوایل هفته اینده فدراسیون رسما در بیانیه‌ای استقلال رو قهرمان فصل قبل لیگ…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/30617" target="_blank">📅 17:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30616">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVDgQuOiRna9ncHCXXoS5wbois57tbjgEEPZgyHCyTobgRNmtIHDyc2KhR8ddULu4QifNtakZwxkO-cvqpXLGKh06EuAoqs6ckZLeYScpMrDxixZoiTH6iINDI44RjhU-BONdmnhFkwbXtj6D4_stfkY986-Q3CPTKMI-FWpGdL-h5jMMPnwWnA0_waNxeLtzRjz0Nhrq48KuVUl3TzHO5wBWUMF_pHnOLdC62RiZGeIuQz42hNczputpzV-K6nawrdLGfrsTq6D6i7b0LFEzml-4bXO79jTfN65z0ou4id32BKeP-obbpl13FiOSBUFPi1080YDH6UnjlEteSedRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌دوم‌فیفادی
؛ ژاپن در دومین بازی دوستانه اش دو بریک ونزوئلا روبرد و اروگوئه که در بازی اول به ژاپن باخته بود چهار تا به کره جنوبی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/30616" target="_blank">📅 17:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30615">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256eec1e5a.mp4?token=OyTDwBCJWT35sESuETiXtRBLSTbM0EktFHDdsH_6ZT_vpDte_ZzrZiOVdzyKkZABZi_luLVPPL36lligQHX-T-RzzvWnh5NnFvoA7byEEVd75nxdoicv-JoTeKx-5zZPWy-3LWoAJkoftDa8aI6GXsmtBEgnzSgb1atTkpNOxeBDokuv-C9v9I1fmsTQECOo4uyPLA8sYlpcB-BD0uxpnrl4_dyr_ci74kTzXOK1KsRH9mmI5SjHY7zK84PNtosiNXux2l4_Yab3kCov__ZI2wzNtpCuj3SjjNBJvUozE9o4R1HYuEYaUklcdxZXSsxjiS-YSGRxlRbdtwmgF3cymg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256eec1e5a.mp4?token=OyTDwBCJWT35sESuETiXtRBLSTbM0EktFHDdsH_6ZT_vpDte_ZzrZiOVdzyKkZABZi_luLVPPL36lligQHX-T-RzzvWnh5NnFvoA7byEEVd75nxdoicv-JoTeKx-5zZPWy-3LWoAJkoftDa8aI6GXsmtBEgnzSgb1atTkpNOxeBDokuv-C9v9I1fmsTQECOo4uyPLA8sYlpcB-BD0uxpnrl4_dyr_ci74kTzXOK1KsRH9mmI5SjHY7zK84PNtosiNXux2l4_Yab3kCov__ZI2wzNtpCuj3SjjNBJvUozE9o4R1HYuEYaUklcdxZXSsxjiS-YSGRxlRbdtwmgF3cymg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های هادی چوپان درباره از دست دادن محبوبیتش:
حس می‌کنم دارم کابوس می‌بینم. این چند وقت چیزایی دیدم که خیلی ناراحتم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/30615" target="_blank">📅 16:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30614">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/924fb238e3.mp4?token=YhWFqyX3oxZ81wiesB7OMAAz9bBJ9pDoDRoMdVR5nBhtXuvePH7rmTfZ6WZJczDGsxUj8opdfhjKuth7qxR6O37uddpEXV-aejAg54LlTmCUHreeRe91lW8cSpQ2hI1cDfDjsfaYw063CcwBWrra6TotzxUx6YBKlxnnJGg835LCusogyKRUtU4RggUJTpKKLwuFX3VRu8giDwfO8XxkR5Ro5isK4GGilV7s7lkRquhb-MPtRGKI8ufhgNR_NpPIHcjQShRqhl2OY8-25BaK8lPX9MMQeetN1M19p6_I6xlFl6922hKQoQ6Fyu1-yX5xw8SwgfDSlIfdQZvMC5fBKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/924fb238e3.mp4?token=YhWFqyX3oxZ81wiesB7OMAAz9bBJ9pDoDRoMdVR5nBhtXuvePH7rmTfZ6WZJczDGsxUj8opdfhjKuth7qxR6O37uddpEXV-aejAg54LlTmCUHreeRe91lW8cSpQ2hI1cDfDjsfaYw063CcwBWrra6TotzxUx6YBKlxnnJGg835LCusogyKRUtU4RggUJTpKKLwuFX3VRu8giDwfO8XxkR5Ro5isK4GGilV7s7lkRquhb-MPtRGKI8ufhgNR_NpPIHcjQShRqhl2OY8-25BaK8lPX9MMQeetN1M19p6_I6xlFl6922hKQoQ6Fyu1-yX5xw8SwgfDSlIfdQZvMC5fBKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لیگ‌ایران عالیه؛ باشگاه استقلال گفته بیرو مقابل تیم‌ما بازی‌کنه‌شکایت‌میکنیم چون تموم شواهد نشون میده سربازه. باشگاه‌تراکتور هم گفته اگه آسانی بازی کنه ما هم سریعا به CAS شکایت میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30614" target="_blank">📅 16:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30613">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7xKvK8gwRGsFy59cbVCWWLMxeFEwzoUbBD6DgfRHhPYMpoc4Nk_zP0K3M3w9ln5YklpQWfv0uqvDqF6bRdnukJ1-5W-O2JPrAUWuF-a_Hhu9uwD3qrbJI4qBBnwjdNp9nw1CJl8SwL8B61ml7zfleAB-tkeqUNw810yN23YOpPIw7Q_qXH-6f7ADpqrkUcsSmmMOWwsLH__l74z3ajvKLVVDq47SUAItg5udmhyEp1eVVh6W0KRpDwzLx8HZf2gmsceUVc7QbkKSovCVrlnei5fTBN1qMC2Q_VzrSRQNFrm6KKfP_9nhkO81Z0wfEcrpVUREt2-GYZnLwVv02pNOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکردهری‌کین، کیلیان امباپه و لئو مسی در سال 2026 در تمام رقابت‌های ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/30613" target="_blank">📅 15:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30612">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJV9vjhB_WUL76gK9Xj5BFdWr3B4U2hPptgOK8MLovQMjyKHtup08TOB7u81wsuzQUTrnmYHwLe1J7Ix8BPGcmekM1XEZUXAEGoAktK6ooa8mtwkIYZkVvAe-X3XdPWsRk_mwmqBg0F6MC3DzvJMH-an2gGN0lTF-Eu2Z17Q27Zhy5GzjptMBaH2gJwuJwEnucKPxZRYW_Z9sGswwayH8sD8Hv7AS4xG4CpXpHaBE5lT47haWJ7MQwHhNeWEGnZaa6Zfm8V5lP0XQfnQJZlJwDsqp8lxdcjE_R6U3sAqZB8F5Mb2lq7-5NS6RUbVBeuIJkpyEUQzqgxjRRpyvRpP9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌پزشکان‌تیم‌امید؛عباس‌کهریزی‌و اسماعیل قلی زاده دو ستاره تیم ملی که در بازی امروز مقابل چین مصدوم شدند مشکلی برای دیدار هفته پایانی مرحله گروهی مقابل کره شمالی نخواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/30612" target="_blank">📅 15:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30611">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4auGifgjSdN6rZR6t9r15YIUrhbq9ZJPJfZh4J18pUZYdq4cKlkun12ogSLogKOtetuz4_64U9mLlLgvSaed1KRe4VgSEz_IFIYLGd8m5-07zQ136dGaJ0CSSxV8HJOPgXtwbq6oz3Dugw6-O4WH4jhtG4INhlOrd7-dPZReji5KFTrqXQGqXN0C7rKGRoGNxby3ZrzpPOaXocVCg6xTUUGgDw0ZtJ9slh31CRnPbgXZZY7nOtyvPNw5D7LCoOr26Hr0soddHRSF_tFR9zxj1J8luB0NKRZekbpOvd5f_283uo8YrzRD6jofOnF1_n8qk4rydWlcMliVgqPnVB_5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سازمان لیگ مجددا کارت بازی علیرضا بیرانوند رو به مدت یک ماه تا پایان مهر ماه برای تیم تراکتور تبریز صادرکرد و این دروازه‌بان میتونه که در بازی هفته هشتم با استقلال تیمش رو همراهی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/30611" target="_blank">📅 15:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30610">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFLcsAFjQLwxrWasmAMQZr5qIedKxY7wEz7--KRfq2CEHpALRZCJWe6Llp4RkpVuJ19usB-MSQN5OEbpOUfM1iivZh2zxdX5bdSPxLrAQsfrkGoPEPvHP8_7knh1MSVgBvNYlLc7K1rg04ooUL59HVYonEK7I6QjMus5BJW_A-abVVgpm42Ns9E_ILcgqQbKI1ZdJq-QbX_Cl3Vzp3xn7SgbE8SRvwJzKUA7sWvaP0POcFwZkv4g2wV92MPmx-lf2dLGMyPPzxbgvBHQwx0D5jTgqv22kBlkOqnDkkZR61Rx-GuWK5rTteMTwst_MXytT3XRnj3F6S8YB4PtvcxR4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛دولت‌آرژانتین دراقدامی قابل توجه روز 14 مهر رو دراین‌کشور تعطیل رسمی اعلام کرده تاهمه‌ بتونن‌ آخرین بازی لئو مسی با پیراهن آرژانتین رو ببینند. حالا اینجا یادی‌کنیم از پاس گل تاریخی او درجام‌جهانی‌که هشت بازیکن انگلیس محو کرد. پاس جوری بود که انگار…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/30610" target="_blank">📅 14:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30609">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5lbHCpjb3qWGGdz5VahU8wHXBe45ZW2Br8LCZs_ZeHV9JStgVdWHYk9k6noej1eUs-nMjgvXS_LrQGLvGrokjFUPxhwhJ2qV1yiqJIoDBsJbZooIUZGQyF6mJcqUBl_bgWawYXj9IBeo9cs0dSHe2H1oBnPnk2Ctl9J7DjrMzYJzmpmrkdoKMGNzpgWnMjmCo7fg64EVtUNs2SSLzctlHPLH9qn5q7ABLz5J5oT5KvUOhW6g1RRItjRCAYc8PRjwLgKCQU_n-dP23DAtRuAv9ZjFViV4TI29YhIZSNVwCRZLlXFSsWeoh9Gxjmh5L_-lUbqF-L9YzUL4mjeeFEMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش ناگهانی قیمت دلار و طلا نسبت به روز های اخیر؛ دلار به 245 هزار تومان ناقابل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30609" target="_blank">📅 14:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30608">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9144acd02.mp4?token=CHfjaogaie55Xll7gmt9yMZGAeKYocAjTB3SbBJb7CwUaOR6Zc7B8HPk7Kfys4A6e0iYhVI1CBcTyEEUdnKWL6YxtCLga77EDIUFh2JWg9whGl9QkUHux84m9-pQg5pqxgcCUxTIOV7G2xJoE900HSYhJkzB2CsW-iIrKY_6Y9wYxoS1DpGqFJBLP61bxoi2Jx-8BavgY9lKVlTKmRODDLvNOhQ3fKAqR6HMcFmY95QgAGaXZgu6Lp16hhCiu--MPWQo3cih7N3WBtxpATF7Ud1JTuipumCXPk0LZK1KY4jx-dbgs4TDXC2psN0hVJ99AaW_8LP7rnu4Gkb79gxw7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9144acd02.mp4?token=CHfjaogaie55Xll7gmt9yMZGAeKYocAjTB3SbBJb7CwUaOR6Zc7B8HPk7Kfys4A6e0iYhVI1CBcTyEEUdnKWL6YxtCLga77EDIUFh2JWg9whGl9QkUHux84m9-pQg5pqxgcCUxTIOV7G2xJoE900HSYhJkzB2CsW-iIrKY_6Y9wYxoS1DpGqFJBLP61bxoi2Jx-8BavgY9lKVlTKmRODDLvNOhQ3fKAqR6HMcFmY95QgAGaXZgu6Lp16hhCiu--MPWQo3cih7N3WBtxpATF7Ud1JTuipumCXPk0LZK1KY4jx-dbgs4TDXC2psN0hVJ99AaW_8LP7rnu4Gkb79gxw7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
سوپرگل‌تماشایی‌لیونل مسی فوق ستاره 39 ساله اینترمیامی در بازی بامداد امروز این تیم. این 931 امین گل دوران حرفه‌ای لئو مسی بود.
‼️
این‌کاشته 76 گل‌مستقیم مسی ازروی ضربه آزاد در دوران حرفه‌ای‌اش بود و او راتنها دو گل با رکورد تاریخی 78 گل مارسلینیو کاریوکا…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30608" target="_blank">📅 14:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30607">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mj2NN8cIXQs9NjHhKhlfV7tTh_oK7aSCvxjsOJxiZIecixmXO9gZJFf6EmN7djp6qU-MN60F7c66NwVuwQreQAkXIFSfRkEiV208kuJTqyh6oUHWUSyk7Gw9wxcDkUMefbhh_DF_l6RldtdtkIO1I4-kj1bRxEdLH4R8N1ne2MfwDDfKWj8h7ALuKiZW2JJuTU_8G9dMuyQvKWQErgTBTTrgBhbxdnXn10DSZokVhNcumIRmENb3QlmS0JcIefxeiibAn7svGYnKd6h4LYMR_oLOYmgLD3odrLA95h2nwpNKv9zmVlPNd1rchFZ6Cnql-4vUiVK9zVPk0DrayHv6_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛شهاب زاهدی رو هم‌تراکتور میخواد هم استقلال؛ طبق‌پیگیری‌های‌پرشیانا؛ باشگاه استقلال میخواد علاوه بر جذب یک مهاجم خارجی مهاجم 31 ساله سابق‌پرسپولیس روجانشین محمدرضا آزادی کنه. بختیاری زاده به مدیدیت گفته نیازی به آزادی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30607" target="_blank">📅 13:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30606">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdDx76XLRvwEGjXwmXR0VDw8qtGmx_4ly8IPlZ-aSUw55xCpbA89UW9g8YN_FeWFb0uqbjHkB5fYUQekqbq1dOlHxj2CAHcWImeeQo3s9ZP7Jju9K7mCzhMNbPLyC2NAg3QQxAAZTxMhCl0D04TOTV0CDnrrs1vmeiiSVo1xYwlv19gWxQ6zpFcNFxi_Aru9roZENpeLt4zR98tlR69P0LEaudTtAFR99lxAzMJqooLEeIF5VZ3z9xD6Pv5Zrrs8KsE5eLXDQxwVcqUL5WiS1DnfqnG86Vq2j2CEgE3aNbzuBEbDq7o3rYQY2CFLIdZLDag7V4XKa-d-l4m8RNb2Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌مدالی‌لحظه‌ای‌بازی‌های آسیایی ناگویا؛ ایران با8 طلا، 15 نقره و 9 برنز در رده هفتم ایستاده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30606" target="_blank">📅 13:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30605">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3kXzoMkJp_YEIjhFo_iaEAlnFYOwvK92-aHd4Hlr5ZOO0Rx_cNB1O_-gGCWzC3SRlMQbCMmu6-GOj922YrneIqLnRJq3kOeTrs-VSYJBTrytgJLAr6eGIbuxIhl_Yg901vIQ2-1lF7yfuiaqa0PoG8UuVhYgxTy44PWD0C9DemIuQaq8hiAKnxO0SAmqP91OjZkUuC3Z7qVfJwaxAG9ttAnEtWrCiX9i9dbFtUoXhBEzBw40RrTvt9xJHnc6pTL9Qf10dDEQbSIWggfGP8fCLykcWqby-T0ZmV_LJZszs_dw8LwsWJxAptutqMeUPEEoQXA_AWKqvdtThG8a-hc_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی به ایران بازگشت؛ بیژن مرتضوی، خواننده و آهنگساز ایرانی‌که‌درجام جهانی 2026 نیز اجرا داشت دو روز پیش وارد ایران و روز گذشته در منطقه نیاوران مستقر شده است. مسئولان به شادمهر عقیلی خواننده‌خوش‌صدای‌ایرانی‌پیشنهاد بازگشت به ایران رو داده‌اند که…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30605" target="_blank">📅 13:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30604">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8rcV-bqzrM_hty-adJGIRs793mNNSQar4zbR4fhJ6SE-rFo97jBbQ5XIIiP4ceK1RyPiJG_Xexu-rUtjT1NgFoOeqFvxXslIN3igcvuREO-PVIj43SSmSPl0sL1QesYac-JYrkEInG40Pn_5MQ-qnU7798bzsDcSRJrU2IvlCwWMyKURiE1tqoW0PSg2YwybbhQsbRP-_H4vSysgPYxEmG36rdi3aDWRLcYI9kWPvxmr9RIkuqdL4XnMu34afNh4RVSg3TxM_OHbtcrxbX536frNwxPDoCCOnZIEhujr0AQFgy-ANMnYspvcBMRulOG3tIcoou0do4atXQDtyty1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
این هم ویدیو زیبا اجرای بیژن مرتضوی افتخار ایرانی ها در بین دو نیمه فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30604" target="_blank">📅 12:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30603">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZzgBWSPnWswPX1CBuzPZ23tbw5i2NIl8W21trGfHFtfC5NBZJCAEnP3jzhxc3h3Lms-FgwYF6jmNwj2YZghos0Bcy7KZLpiYLoUkBtuM5VebHcSnMEADQWyp-vWEWTOnz1LYh-6EXFFAa6EkgQliCDgrs3tkUKk3meVaAVduA8jCl-TuesGKcJgQwpkRvPcGlbvSbzgeHaLE0o0RqrYheqxE86jO5C_t6kKKTjlWofp2I71owaoDl9P69ThdkTwmmNpK8xiNP3rE8Vh8GXD68PtKgowQrW8nH9AbzWe2_M60Rhm4fl6b6WGrVy7bSd1GB99FY6pKD4zP_bRFRKhHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ حسین عبدی سرمربی تیم‌ملی امید از هدایت این تیم استعفا داد و از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30603" target="_blank">📅 12:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30602">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adyOfgFGFnJjuh8UuyYPZpdAM-zSzWck-KhDwJjgqSAKlAPsDc_8ELFKFsjwaF0fIwgpKL_-Ome5ZIRV1D8OYRwS6jgnp87AW5Vf8IILe11j6EIk5yTzDytGXt9nkNnBV1esFc-_Zcr-uoj3bA5GhEgGnI82-ztMrRw__bVIHuf61WVYfYbQEGhZ-NO_J8bvl968tFGlJSH5n--naEa6EfoKh_szHRaGswtGPP46feQrsKKZL8M1EQQ2-eHST1vrDr2pm4ratw3HUV4C1UMFL8nborCDL3qm-6IoS9KO2fP8tO_IEPZsEuUSjMYrgvyRQJ2EYMhOAjFtr56XkJKqaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپاهانی‌هایی‌که‌درپایان این‌فصل قرار دادشون به پایان‌میرسه: محمدامین حزباوی، آرمین سهرابیان، هادی محمدی، احسان حاج صفی، ریکاردو آلوز، آرش رضاوند، سعید واسعی، مهدی لطفی، کاوه رضایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30602" target="_blank">📅 11:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30601">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WO9SF_tkFSeUwNPSLGpeQk3KEIO7gd-jqV-crj_BGhDwpO8_Y9d9emD26JS5hhMCWIQh4_58Mz_ek2_VYJgIQfaigZ6mbIDlZDQRLuNTwMz_Bg9cmFuDiQbm5-PEhWsR_SPC0L4m1neOB6D6hbbNr_fyF9J4QnESoGQDMh4Q9fGIWhyg5mvr_ePW1GsOmo-UfLTp9iW7yG3E2jcYoyioYZKdOnxvxMZkRKbyvsOpQgcjPFD8y3grzTskpkZ1R4qCCmz9a1OMR03zW-qQy3DAqfDX850icSbx2oypQqFbiDvQA_Kk9XRgz9wbJlMgzguJO1G60Rq15Jahyc2aJ9B8hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇵🇹
گل‌های‌دیدار امشب‌دوتیم پرتغال
🆚
نروژ در هفته دوم لیگ‌ملت‌های‌اروپا درشب استراحت CR7
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30601" target="_blank">📅 11:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30600">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUEfx2qA8nTegU2YF4PhFGfTm9amHAH-G1Md5r2j3udNUp90gyICaJTOn9u3CAMablujrqlO4Le6L7SsOCK_72F5Ly5cP7WVheNWZEtDfDKFrlBCLLPbLUzo5nmLwoSU47o-uUyPxV5uf4PwjVX4S6unuPtfoOL7R4ehHBIkvyL4l4okH1hieiQBhGFYgTQjhmeRzN0L8wVfHb7BY8OW7or2DMHA3Z1qznzU-_Tl_5pfy12Os0KKboPd0gCI6iW2fNAOgujsSBrt5PVtaP9S0iNuZwDatK4G-4gb-YteR09ExF7Alt28euHtzH8wAVj1HwKjynL1MGe00qAkNY5iew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌رسانه‌های‌ازبکستانی: آسانوف ستاره جوان ازبکستان از دو باشگاه تراکتور و استقلال آفر دریافت کرده و نیم فصل راهی یکی از این دو تیم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30600" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30599">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPgl5VQzWV_ZXNXIgdONXDJ5KMceqFf-O52striaxCIgXJIfwyAPJ2mLMYrpL1JavGKkEyG5k16sC6FLu2CUXURm7HiKvWXyuHR3Kj9nCSmMC3HsVuy4rmYta0gEEOjuJuLlwBBxZqMS5MiCPgrNAyUNBB8Ce3Kn9egalp4raIPcfPTQh_wwozH7Jn7HMZZ8ja1kz5ZUZFbusqPXHmSqtnAHFOPRH39O_W9sKEchqVZWsP-wr6S_hc_Ifa_2RIDECzr8WD9IsopxtVdv4K2_BY4X3QrAUs42LjwswaWtcVB8oQhtH_0XDXFladdO06YwxiCLAPZPQFQL8k1RDS-_mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هایلایتی از عملکرد درخشان لیونل مسی در بازی بامداد امروز اینترمیامی در رقابت‌های لیگ MLS.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30599" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30598">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/30598" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
#جدیدترین
نسخه اپلیکیشن بدون فیلتر (WEPARI
)
🎁
کد هدیه 100 دلاری:
Sport100
ثبت نام آسان
☹️
✅
r6
🖥
رابط کاربری راحت و سریع
📲
کاملترین برنامه موبایل
🇪🇸
اسپانسر رسمی لالیگا
😮‍💨
بونوس
100
درصدی اولین واریز
💵
بونوس صد در صدی واریز یکشنبه</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/30598" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30597">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔥
هنوز توی
Wepari
با
این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
😀
😃
😄
😁
📌
بعد میاید سوال میکنید کدوم سایت معتبره
✔️
🎖
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
🙂
🎁
کد هدیه 100 دلاری
:
Sport100
🔄
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🌐
ورود به سایتwepari با فیلتر شکن</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/30597" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30596">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsfpvXekcQyqcdDLKxeaOUtQjHqO4dLxK1wptZZSGITqcdRiO2Gm7S7ORXm8WnaUm0JAjM_b_ByjsX27oqmh5w_fpuwiw6-Sjsp-HWut6knBRc9gK5oGVLbF5ZjRzOPs0I6S0cjbbltCOudwmK-yF-9SdrfNwiSLFe0Zlp3P7P2QZLcEHxBsunetyemjOt83zwAJgQV2w-ygzsMmT8mr-3EG8fghYyGQsoPGrduK7PcMzlw1OTZGU64UceDIHpk1yI1JS-KmAClyMVpWEzOeIgczhRjGpiiHsktecvYThZsDXOR5LVnvP-k7xdZ1j8bAot40ixQby_ZZ2gqE5ATzqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔵
سایت‌چمپیونات: شیرزاد آسانوف هافبک میانی ۲۳ ساله‌ازبکستان‌از تراکتور و استقلال آفرهایی دریافت‌کرده و احتمالا راهی یکی‌از این دو تیم میشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30596" target="_blank">📅 10:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30595">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njbGmoqtayDmQcGMBco6xv3OPX8oyo0MqdMk06pRTqlWDLcVYxic15fgKt8vPPqjAv49oMFYkN89olP8d2VVQ_DknmvpJSxDjuX6zlEpaeO96sPCUjhdvTQz8phz94Wxxy6SHvAFboyxZUckabYHT_g_slBS73cs0eJcacmyC_9clnBvt2onSVsHsA-jlbPoB88lCfw2mtmhmGXwrTgLomdHjuL-Edeaqdo0POTSiHbERhLTSFP_8gH5LRLBWFYbnKp11NGXsfCeFXF96hvsNRBQO6uYFlFC0VlCj6cWbI36hHm2sfbm7yi2_1QvkiaZQScruTb3ukwHxFhk-OkVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استقلال درپست‌وینگر از بین‌ مهدی‌قایدی، یوسف مزرعه و یادگار رستمی سه‌ستاره النصر امارات، فولاد خوزستان و فجرسپاسی دو تارو قطعا جذب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30595" target="_blank">📅 10:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30593">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFaYN4ac8dELxEUad6ebRlc0aRTwaJKahX7UERe0TEzVLbQg6vEKFfuHN-ximO_6YNxfD8EENSw2DVBg3D67MYG4o72qPCT_5ijYno_4nCSPx8frpYGUD-DpYDXc7WkmFlJFd5mc8x0XW7H4ZZ-thGmGNrHRgpOcUXrR-eNIVpSH1TwRa8iJZPeEsMhVcESpXgdqmx7PX24bUQ5ackR0OA3Dnvb4MrLbYShtJPHQhMNdCKdClGDU06de3Vxp2njV_GQceWctjlElO_o5OiBRIGRaDvEffC1eFhDHARzy30dDhoKAmOfm7Tn3ayqZkclWDQYhcVGquW2RDyoGRmHgbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3c75c1227.mp4?token=iKgJhAo1SilNKLybDujok1p7T8gectisaIC12FUxPOk1k61vnSoSNwHHovOfStKbx4uyulryzYp33vTsn27OgPP79iw6rdBhjviL60eo9B500JdxJHpc5JrCoSBAQIQiFjTUV-fwEGZMiqJG-FDKrKmv0SN5XchpA5D0ZMOhw-c51qjYQB94mjmA-eM7P-A6RVBGRcQrMX9I6i-zOjx4xAIE_j7_-g6gokQJUykv5iRD6OXfM7yQYQGP9loYfzI10imbh3cexpDPiiGDrbOf9qkDAjQXQwFBxBIk-HSbse0PKeKLxia3VHYWWjGmhftGbR279Lb90ut8w_-l-rhh8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3c75c1227.mp4?token=iKgJhAo1SilNKLybDujok1p7T8gectisaIC12FUxPOk1k61vnSoSNwHHovOfStKbx4uyulryzYp33vTsn27OgPP79iw6rdBhjviL60eo9B500JdxJHpc5JrCoSBAQIQiFjTUV-fwEGZMiqJG-FDKrKmv0SN5XchpA5D0ZMOhw-c51qjYQB94mjmA-eM7P-A6RVBGRcQrMX9I6i-zOjx4xAIE_j7_-g6gokQJUykv5iRD6OXfM7yQYQGP9loYfzI10imbh3cexpDPiiGDrbOf9qkDAjQXQwFBxBIk-HSbse0PKeKLxia3VHYWWjGmhftGbR279Lb90ut8w_-l-rhh8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آیدِن‌اسکپیومهاجم ۳۶ ساله آنگیلا که موهای بسیار بلندی داره در بازی اخیر این تیم در دقیقه ۶۹ به زمین‌بازی اومد و دراون مدت کوتاه باعث شد که دوتا از بازیکنان کارت قرمر بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30593" target="_blank">📅 09:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30592">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3abfdd06.mp4?token=cgNbZ08sXySHD0Pjww9NWE2s61l9yoJj4pl_qEgYLwC3BESvF2YPf7SS8R7KmpfbU4TnLZXLrJ5qY8FEN5jHR4xsXL6IT2hLl-UtEVZczGQOVCyGvVn4FYU7iJ1sc-ygbLQRwLdk57jMwAv6xs0gxcs7vJOtiOz3-dZzyLa0S_oYkAJMpJCDMUcZUyTqZpdWPmBtQo8hjSePPYTTSiSHhtYIPv0dCk3HpxAWmcO5e4Esc5kYxAlBmRLJBEYH0ztxm8HSmH4mNBy6fXtrxeRDZrDi__UmHRRPBbIhGBSTBbt3iVghIzHqwHhmAtnYfBcKLXzkEw9PSHiLQs3n7BvupwQ062uZ-2Kl3IFN3VZR17eCPpOuB-zUSsvtQRQfg9QdWJ2uVMAYmCzhQPEFWSjkoZiROQvZW9w0GLfYALCsqVSpFi_-XaVJuVZJU0zDXX2pBJmr0dCKM-o2XUxRTy2CVr3LrZclwmfDXOY1gVqc825BcMTQEhYwd6YNA_1TfeXYh09IVz7Jabj0SyqWGJ428P2m5FzijOS1X6aYNRhquu4E7jHBNvK5LCD0YuEBHGeINoCVZazXGyZVFtUoGyeBqULF_a7nY7qFu2CKBEa6YUgSWxb84_KWA7P2QtPkBpYh6_Qv-Qa14CiPdqRH3tX3K9LianGm0X42uw-4VVuO2vI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3abfdd06.mp4?token=cgNbZ08sXySHD0Pjww9NWE2s61l9yoJj4pl_qEgYLwC3BESvF2YPf7SS8R7KmpfbU4TnLZXLrJ5qY8FEN5jHR4xsXL6IT2hLl-UtEVZczGQOVCyGvVn4FYU7iJ1sc-ygbLQRwLdk57jMwAv6xs0gxcs7vJOtiOz3-dZzyLa0S_oYkAJMpJCDMUcZUyTqZpdWPmBtQo8hjSePPYTTSiSHhtYIPv0dCk3HpxAWmcO5e4Esc5kYxAlBmRLJBEYH0ztxm8HSmH4mNBy6fXtrxeRDZrDi__UmHRRPBbIhGBSTBbt3iVghIzHqwHhmAtnYfBcKLXzkEw9PSHiLQs3n7BvupwQ062uZ-2Kl3IFN3VZR17eCPpOuB-zUSsvtQRQfg9QdWJ2uVMAYmCzhQPEFWSjkoZiROQvZW9w0GLfYALCsqVSpFi_-XaVJuVZJU0zDXX2pBJmr0dCKM-o2XUxRTy2CVr3LrZclwmfDXOY1gVqc825BcMTQEhYwd6YNA_1TfeXYh09IVz7Jabj0SyqWGJ428P2m5FzijOS1X6aYNRhquu4E7jHBNvK5LCD0YuEBHGeINoCVZazXGyZVFtUoGyeBqULF_a7nY7qFu2CKBEa6YUgSWxb84_KWA7P2QtPkBpYh6_Qv-Qa14CiPdqRH3tX3K9LianGm0X42uw-4VVuO2vI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
سوپرگل‌تماشایی‌لیونل مسی فوق ستاره 39 ساله اینترمیامی در بازی بامداد امروز این تیم. این 931 امین گل دوران حرفه‌ای لئو مسی بود.
‼️
این‌کاشته 76 گل‌مستقیم مسی ازروی ضربه آزاد در دوران حرفه‌ای‌اش بود و او راتنها دو گل با رکورد تاریخی 78 گل مارسلینیو کاریوکا…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30592" target="_blank">📅 09:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30591">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cb5b7e2b5.mp4?token=G7NgyBMZi_VIldfoLXNQaCGT9mGzvyd3vHVZoV7JZF_rgZUKeXl6bSKkFCEbowTJIg38H4YzXeJ92yYY82sX6R-Szrc3x3YK_Pa2MPMYmtF8qOd2KR-T-VXR6g4dKWAY0zjRKACyGk3XFxjd6Zv1OhsoGPZlMXr7gPF2rWWhdxXAHGYvJfT_V76n3uR3SZ2rLMpj_fWHI0RSW5FPq87stkpmXyczgZkS4twFL8MUnPBS1ztHXVB-TMdtibvkClD5vRenWdgzNgUrPUxENL-P9Yt643yr92ZJtGkN0sBcsjMaaF_6QUPFRxFwkhyb3bfEdP0pMRnq7To5X_Rec_1pO2clo9UNBaaTw-Xs0WZyVnWWusn1OSX07tEn2IKf6vW-aU_euEpH0wLzQ2xdcrokXadz-2FzLwJGhJ5uQSQTJDPJc-IFT7lFZ54Py4MHMhjQCZoyET4fYbEduma9jF_Q_lkm3fbJ1qwYBrX8wRk6P0t7zvH_bqjBX5HOPeCb5g-is6OPS6CWf3GZjGmL1L1CC_C6C-JvVTg2YNrxx6x_zsmSNCrc7vol6wbeETAi8E-pmW6gg0M6JLB8693OrkQHYGVirJRpKUq8oBlor3HRZaj3ojHQaT2sjrw5XMMUA-XRHOgPoISZ2XZyyPir28V12YuA7vGTpw9N3quRbI-6YQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cb5b7e2b5.mp4?token=G7NgyBMZi_VIldfoLXNQaCGT9mGzvyd3vHVZoV7JZF_rgZUKeXl6bSKkFCEbowTJIg38H4YzXeJ92yYY82sX6R-Szrc3x3YK_Pa2MPMYmtF8qOd2KR-T-VXR6g4dKWAY0zjRKACyGk3XFxjd6Zv1OhsoGPZlMXr7gPF2rWWhdxXAHGYvJfT_V76n3uR3SZ2rLMpj_fWHI0RSW5FPq87stkpmXyczgZkS4twFL8MUnPBS1ztHXVB-TMdtibvkClD5vRenWdgzNgUrPUxENL-P9Yt643yr92ZJtGkN0sBcsjMaaF_6QUPFRxFwkhyb3bfEdP0pMRnq7To5X_Rec_1pO2clo9UNBaaTw-Xs0WZyVnWWusn1OSX07tEn2IKf6vW-aU_euEpH0wLzQ2xdcrokXadz-2FzLwJGhJ5uQSQTJDPJc-IFT7lFZ54Py4MHMhjQCZoyET4fYbEduma9jF_Q_lkm3fbJ1qwYBrX8wRk6P0t7zvH_bqjBX5HOPeCb5g-is6OPS6CWf3GZjGmL1L1CC_C6C-JvVTg2YNrxx6x_zsmSNCrc7vol6wbeETAi8E-pmW6gg0M6JLB8693OrkQHYGVirJRpKUq8oBlor3HRZaj3ojHQaT2sjrw5XMMUA-XRHOgPoISZ2XZyyPir28V12YuA7vGTpw9N3quRbI-6YQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
بهترین گلزنان چپ پا در قرن بیست و یکم؛ لیونل مسی فوق‌ستاره‌آرژانتینی با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30591" target="_blank">📅 09:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30589">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I-QP7anyfj9La2OB-fcYVVSaA9SncevlF4JeY94wWvBAJSD1wg6jFiezTxURAYJjDDbhmrHuvwK55MofCepPvuXBNQ9YPoEWsSp7Jd_OiKlgyCJKa5gRGgJ6GPKYqGBJta6hOL87fAL52WJrFtdjPkPrQK4IkrgDI-rLd2XIQYDGaRcWkMtKFYGpoglfPRXN57WwShmlD5rV3Hs2FN2LUx-ZuZu_DUv8WFuHcJUS-1OfulUGPCD8FvXv55L388yum0DJdTnNeAHt9t94BL4tDAtE3jIfLCxCCOE0g0YMbgvF7TZoKb33HJ_fXXEcCIfbtrgSBCuxgvvFCqZn9FI2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kT9S8NBR_ROCbJOH_ug4ni5yjJTN82P6Z4DgaLCimuTPF0XTC9F-ThqOl0Js8OIOdKKMCPWLHQLJ-r4CzCMDPn_u3Nv0BHaoCsEafxVAmP2s2IQjtRheZf-G47_NoPhdMMgPyL2FXMkyRftFmMx9HF9FYam37EGdJu0F6-i-8R3PEpVPlBsCAzT4gfomt8-iW_ue95GhfZ3m1ZMl6S96kLA_JrR3lmXQJ7MDaBXpm9yMWsNWmjKBFgBVqUZZo1JBGnfa-aB1KIPnQqjXhVyxvGr1dfrw4vibbSqis3xPdgQL1eKb3C8hDrrU8FVHMH8CX_oT85cFvMmB1WblT5_9iA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه عملکرد لامین یامال
🆚
هری کین دو کاندید اصلی دریافت توپ طلا در فصل 2025/26
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/30589" target="_blank">📅 01:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30588">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKxfh_s1pyYLPzsgtqpbbLVP5DTulkrqWc9DDpiqbl5R1UThyMhK_xYAb9Jk9nxzZnYOcMM-GKeX1SRLxftQ3Bb65iJEwNpX_e8JA3dGfvKOGR6lsAzMzgd3v-lv1OKqfDtkTBKhT7VpCH15ONrz5nzxl-2gL2XLBg0_XE6ISse1ectLhQJQYostcHPuln6glf9g5iBvgKzckJdahpoFoXUmD655Wpv_MH_UJMKtLTkD4aoH_PEUNmc5soMBmMsavjMLsS3L2-GiUFmZZpP6oh23vd_r2c3bCmf1ZkOC-gxB8kWTADTJ2cA1mOLzL9Fe0vkbmS_qFweR79DO-iLb4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛ روز شنبه هفته پیش رو باشگاه استقلال 70 میلیارد تومان به‌ملوان‌پرداخت خواهد کرد و با ماهان بهشتی هافبک تهاجمی 17 ساله این باشگاه قراردادی به مدت پنج سال امضا خواهد کرد. تمام توافقات بین طرفین در روزهای گذشته…</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/30588" target="_blank">📅 01:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30587">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUJWqyf3hXmM6uhkWH1yJlVamDlXj20Ochu-4k19aWmoI3TqYm2ORK1K0FamHW106N6vyEucgFvLfQLrABVLaZPfuUk1vBFuvFV8jGdchWBIcMwnLxgJ5Hxa1zjt23XBXuoU22Koneiq4S8cyclc8hbeOA4C9JSWbY3nAEkhlGV0cMO3KSxOqaXV3I2aoc-d8C3BK07PM_mk7L3FW2ErrrPp5VhvjWYnQw76nxdaF5wWxl5oAlXtUcHq9BSUmTuTQVgwE8pmfaakpJb-4q95SnK9q6wpCULMcBkbOIsZ2R5mTLrQyKUfkiRvUVEAd5SLSm2F1VkDrckveDKPh67UYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نگاهی به عملکرد و افتخارات شش کاندید توپ طلا 2026 در فصل گذشته فوتبال اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30587" target="_blank">📅 01:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30585">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvlMVBCa2xDTK6_3nAn6g3kWaqPUC_JLnyQn34wX6xcTluj-gRsZsIN-bQ8o6Oxt9X7ErUhKETWEdtHuAYE3X7D3nWPyZfsbgXfiq4oz71dZYN5m7dV_vLHpIWh5qmUuxIGEbuu2Ib_ZwKU9IcMPol2tsTS51Fgmxwv42w-YypUvtxvt4AEQbreJU4OmUdYVzHCF84u_lma_1ROfSd6WGoCmIROmXxT5JCHyuA8Of5WFqFjUtyjP0ru__5txtPlilp1gEOms3CqZrdTvXn3nilxaR1aV4P-rvS9tgU7FAD4yBWYBGGwC4UCt9jS48aVf209fqlDApoDLTSza0z3siw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌ امروز
؛ دوئل بلژیک - فرانسه در غیاب امباپه و رویارویی کره‌ای ها با شاگردان فورلان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30585" target="_blank">📅 01:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30584">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRlcAekkqrmbmIFje3F1kUdGpyCEX0_6GRNJTH0KsjFh_hcPcIdj0Ek8dDimrVt_Z3ANfEJJd7cRX2jZZP_GCQlprZJjAP0EMaxKwrEEkEP2-VGWk7XWkyEeUvxRBJthSKF7lUSbj78LzZRQIEbPpOjpakW3mQXWAcGUJnBpJIOm_xMkidfvqzO8IsCvn8pOsTWKUbVNpsIj0Cqnuu-21EDw7xNfTcZWleWmOfMNWUJYCDsK-lY2RAyqhwA89HlQnzuGzQLKGY9Dixw8A4KFwqpYThhc7wyrdL5kX4jjI4t8I-JYooo-TMKK4cJvx23U7ZD8rc4zRRACqgEfsHxAgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
اولین برد ژاوی با هلند و 6 امتیازی شدن پرتغالی‌ها در گروه با برتری دشوار در خانه نروژ و شکست عجیب ژرمن‌ها با کلوپ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30584" target="_blank">📅 01:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30582">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇪🇺
درهفته‌دوم لیگ‌ملت‌های اروپا؛ پرتغال در شب استراحت مطلق کریس رونالدو با درخشش گونزالو راموس دو بر یک از سد یاران هالند گذشت. آلمانِ یورگن کلوپ هم یک بر صفر به یونان باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30582" target="_blank">📅 00:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30581">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAbfe7wmF4xPX7vXsX1hhaFW69N9b9lyO6GuYfVysp-rEZPRSDG7xXQbfdOTLT8RFQghNrKgnC5BUlAhI0wSf-Y2Bb4SpjjWyBPYgd4k_o2Q1ITkcfoaP1gNTzZvVw0KVOll6lK3y_rRyHqWjScr08Hrz2jZzfbK5niQFL4LAEzsEb6CDFVG0Y60OW2YGaUwLdj6JFItQwHQdsXR1f6FhCtG_IgTUrRMlT9LerDPclSBnSK8Zh8OF537sq1P2mzGQm4Rqx0YXOVRUEw8zP48A2JwNft1P4hTYTXDlOR1IflD-FLPHpY2elQ6cZBjhZXxNR3awiozDZt3S8hCa-noWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌دوم لیگ‌ملت‌های اروپا؛ پرتغال در شب استراحت مطلق کریس رونالدو با درخشش گونزالو راموس دو بر یک از سد یاران هالند گذشت. آلمانِ یورگن کلوپ هم یک بر صفر به یونان باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30581" target="_blank">📅 00:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30580">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q34R68w661ZTutthhzfwrDWZYqOXaMwBBsKYNm0aRROPCVoG8BxaJAdsLJbEc_kq1A580hEeKLotjQhTR0ONDybBmec2lkgmRku4ou4_oH52mwnNPfZ40Rm78320pcBGEM2ngI9ruwaGzdpPbpAGREkGAvei9_5K5rauSw0-K2-GXqgqU6O9kvbMWqgshl53gTmiNmctm_7GJ-ErrsaMhPE9EPIDJARsjbFX7f2iOiGGoWcUeWGFXYCJUJ7mAvQfRhfAgzZlcd3AS1xhl1hTuc7qahuSfK7faujQdWA0uWFB2c0Z1RrmjyzTImh8GpzgNezrx3n47aBCkw7_gaG4oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
خورخه ژسوس سرمربی پرتغال در واکنش به نیمکت نشینی کریس‌رونالدو: رونالدو بهترین مهاجم و بازیکن فیکس تیمه؛ امروز چون میخواستیم دفاعی‌تر بازی کنیم و کریس رونالدو 2 روز پیش بازی کرده بود تصمیم گرفتم امروز بهش یه مقداری استراحت بدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30580" target="_blank">📅 00:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30579">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDRZvPu-duyRQoY9hzd4HaynzfCjcB5qTVBUhWJMBp44kO1D7TTq_Fd2aTnGZuyd1J0GRLs3FzJedDl8l35heNe3NmBVD7K4wUjmvrN6r7PmyPV_q-KXEJs8wFlZWCLBdbKgUcTJ21dKyG68WUBwhlrPNeCB3bEvRrM9LANbyYVNKsP030c7kJzUXBGIi8pmCo2d_UB5pwyqx6tlpyriKQKTrdN0zD11Ly_tvw67rsURB7o4V_Ues94xF3EZ9wMST62Qp5lBc8hbl-EQM6u2ix8hXA96AWExVovo8vlZuwVl30ytGJDOUJqsfD9jNU5K7IXCOg3qowfZJOksz7_VkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دوایت‌بایکس‌فوق‌ستاره‌باتجربه آمریکایی که سابقه بازی در NBA و لیگ‌ برتر ایران رو داره با عقد قراردادی یک ساله به تیم بسکتبال استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30579" target="_blank">📅 00:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30578">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcLB2H8sqGl6dbzbNotZd_MCSTJ8UVL7yuxNewKXWCo94RThkjo-RjTr8_moXXrEf_gT1NSw14fIHqQn8Os0Pl6_kD8KEAa_2ey-_pMDSbSZOXgW8WdvK4bVuAg9OGv7ROKgeYfZtWbsHFNPbtpoCjKi5-9hei3JAUVTc1hRBuwch_KH0q9pP8CT_KOic94AgPD-yt9BOc7BKdFItf1ZJnnxQL_GH_GVjz9JpcZbKNAcntZB82GmbhBQd7ni2pmfS0_cJExOKE75NqEcMk91602omsAs6jeyyLX_t0kUT9VHAhUJelJEv6Yu4KQV4Yc3Is-ieo0F-T4_bKHtL0EhBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیمان حدادی مدیرعامل تیم پرسپولیس: به یاد بچه‌های مینابم که شده جام حذفی امسال رو برگزار کنید و اسمش هم بزارید یادواره شهیدان میناب!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30578" target="_blank">📅 23:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30577">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nId2uXuxbn4wz4ygdMXUYF4L5hprSniPVoldAojK8MMIlrcOSkRKY_gjixd5udMbJeN84TbGDFdJg0Jlw-wQcS0-rL16LD2pdquVQ__xh9cC_7P9zIgFgrlsOcNQAoIyP82S0OORNk2tYLAayvVzBaOI7jjxUhwIgN0PuDhmbyrfmFwqEUvexChtZRcqTV9rJV9ILJf80gRQcQuOSzKG_jJ590LzdY4ozdw4JQySQVnY8RRZJI75WxIwJQk6NnM9QxQsCqTBJo-zMPYH-9febSXYQAG8W14SSwjxwp5ez_fjgupUeFn6SRbA6HinJEtkKXp1oTIMVxF1EwwJrL9N0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته‌دوم لیگ‌ملت‌های‌اروپا؛ شماتیک ترکیب دو تیم ملی پرتعال
🆚
نروژ؛ کریس رونالدو روی نیمکت پرتغال قرار گرفت؛ ساعت 22:15 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30577" target="_blank">📅 23:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30576">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVP5jPozjZoQ0JTZhlMOeHxb7FFqzVUlhKG-Cl0ySLmUVetoLsskyHVi5UrcWV6--bW-ojuW5BhEjR-2v2b3_J1DOdkaAGixSMjdyT7FekFunYa0edYhJKQBwebmQ99H-UMHWjfJ0FLOf6t7-zg4ioRnoOUsMJweUTWYTE-bmNj7zcQS4wuo6GRPwMa7CIN7pBGfQKMzkTk1grpSmVzmMBGYx2T-p7v5vjaLdzFam1yP8kB99zWsJ0VcQhy5Qy8qm8qBONNlqvq3hgxNE-crcTsnvvyOuKX8lN3SNMFvZ5dlUn7OnGUzL9P5Ea2O7rZgaDU1fBAgQl5SAbxV7m0Egw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛مهدی‌تارتار سرمربی تیم پرسپولیس روزگذشته به‌پیمان‌حدادی‌مدیرعامل سرخپوشان قول داده درصورت برگزاری جام حذفی در این فصل سه گانه رو برای این باشگاه به ارمغان خواهد آورد.
‼️
مدیریت باشگاه پرسپولیس هم امروز به سازمان لیگ و فدراسیون فوتبال نامه زده و گفته…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30576" target="_blank">📅 23:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30574">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/USoiEzg4kkb9BJQbGERq7bYnLYFUoFm1zpBFA-_1eNKLgBN4WNKWeY9B_jLkakZYn87fvJd-Z1LHxCTLk7wzY9LMv32mvXIyYbeViewsX7Tq5t0oAiD05NfWoFGlm2KqJ7Mr_rBp9OxApoxOU7On48-mG4L3TzlcILRk7yjoWmKJIM7KTbseae4tC8o1wtWmOE7ygXLp42gueCuhYBm1SpH1FL1iqyT6RFBY0wEch-vTOB4gmEe6ib2Xt8w9_dml6uO_LfS-NtSm4_RNM0P9mDJ_aO5PKE3haVPonpJ0OZ_ubpcN40b6JrN6xIuvBBeWXWhcifXKQ3sBUir51KzfHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dP2GVW9WPwWxQ71Koa6gO62jpqClgORFC9g2DBE4S_IHy7bTyu2p-8UEnIwhKpquGUBrBcJLtANqm_g14h6QbmNWPdunn2O_JDXPzeasWB9oMLWmU8G7-fQI3N23Xx-k4xD74upxtFbJ_hMN5Gt-iU41oGsuTwQptAgsP5gqdF9w6W4uY09aij3rA39z_L5wX8NsR_qk6f9v7Xbo9WBZVy92gLGcLbEYtb6PG7FmA_LVV-21BWdmuSbQqah5s9_vIsPI0sM8Ehr5tNA2Sxlp0ymEa7JiH2oU8-lhkyUqnbuBOF7XUBnCnpbZCX4O1DrkJmKoCyIrv2NZBkykLCWHOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم لیگ‌برتر بانوان؛ آتش بازی پرسپولیس مقابل قوی‌های سپید انزالی و شکست آبی پوشان پایتخت مقابل خاتونی‌ها در ایستگاه دوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30574" target="_blank">📅 22:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30573">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHy6D8xmGrgWmxabOe30WYchKi9tCdx2rOkra4mHiORwluLM5ANnuqzQqmOZ_0vWVMH98EwhEgK8FSiNXkmNrMh4kBm-hRmLAn8QR1NvofYxQwp2voYxMNKGuFj0zg_ykR6zyaQXQ9O4CVQn97Oa1gzHszqms2odEDCalB7_0E44hm8QwVjTrGP7vlx1W07bdmB-D_YX6CzobH1optOKkKvzU6UjH8X8asPYGnvlp9hWGyZGOJKtA66OQ2oBzzQIhfGBfZ14byCgAyr-IickGiEcWqiLmh7Zuxv3kKG27TbAqVMIlBD2al88IUpccAo07gG6Olwvyw53NfA1inrG5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلش‌ بک به زمانی‌ که مثلث‌ BBC امان به تیمی نمیداد. چقدر زود گذشت دوران لذت بخش فوتبال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30573" target="_blank">📅 22:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30572">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7922a3fb1b.mp4?token=VoQylaEqcahgfwVBJYIwQ4tdCll0q4Tg_bxXuv3Jl43a0Vc77rtx_5aea7irXp118PRH6p8svg2N8PGPpbayVRST-eiUR-soJskC-Lx08ic3ToNbv1aDfky93-c5RR21X51q-gHV5kcCJMQRVcS8KT2lojWnaFMvKzKDcFUwh0vbjnOMsj7G_013NA1NNad5NMYYJBzg3Pz5Z6UBGAutXxQoyfRD7aQeDyccVv8BNn-_DibrmxZ5oKbM6c3lMJHK5i10VsqtsN5zoWyk4t4W9Sfs4qZaCwhZHwpcqDdpZrbcLXreFhFHTusVYSB7RI5sFAWgxOUbi1oWXondwTXJQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7922a3fb1b.mp4?token=VoQylaEqcahgfwVBJYIwQ4tdCll0q4Tg_bxXuv3Jl43a0Vc77rtx_5aea7irXp118PRH6p8svg2N8PGPpbayVRST-eiUR-soJskC-Lx08ic3ToNbv1aDfky93-c5RR21X51q-gHV5kcCJMQRVcS8KT2lojWnaFMvKzKDcFUwh0vbjnOMsj7G_013NA1NNad5NMYYJBzg3Pz5Z6UBGAutXxQoyfRD7aQeDyccVv8BNn-_DibrmxZ5oKbM6c3lMJHK5i10VsqtsN5zoWyk4t4W9Sfs4qZaCwhZHwpcqDdpZrbcLXreFhFHTusVYSB7RI5sFAWgxOUbi1oWXondwTXJQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از این‌صحبت‌های جواد خیابانی درباره خواهر ارلینگ هالند در جام جهانی در برنامه زنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30572" target="_blank">📅 22:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30571">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxZecuCVo72KZ9EVtmYVea-6KBDr9JrvuZsJdrcSZKiyok-nffcssIwqdMCXik4PU9yUCvxtTDCON89yqH_GbSAIzk_sJIL_3ZpRAoLcqGImZm4DIHAx0VppPyf8iquZlwLXnb_0LkpPB2ywsB5nexP_KzNH2evBPKdOGUPgCV5xgeFzLXC1Fpp4ckg9vj3GFcos-ib1GXkyJjs6gcuuBXD7aOMzlD3IBfJtc4MuXvFzvvkpvqVNtC5pXSXhTtqWVKTb6UXq-H1akTvxa8zBiZ2wXnk7LaT7YYwN1LF8o1SwFHiT5_zXrTtEhmlh929IywZACZ4kW3Yj818WbxHxIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
CHELSEA. MORE THAN A CLUB.
🏘
اینجا جاییه که عاشقای چلسی مثل خونه توش زندگی میکنن.
💭
آخرین اخبار، قبل از همه
🔼
نقل‌وانتقالات و حواشی داغ
🥅
پوشش کامل بازی‌ها
📊
آمار و تحلیل‌های جذاب
از استفوردبریج تا قلب تو؛
🤔
Welcome to the Blue Side.
❤️
👇
@CFC365
💙
همیشه یادت باشه آبی برای ما فقط یک رنگ نیست، یک هویته.</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30571" target="_blank">📅 22:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30570">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuPum5a65VUACmfUNJFdaYoj8-jJI-maqeq9hg-gY4a88b7huCwzvUCRf8tR8UY5_Xdm5fqlCVZQFWRHHRdBPfoVgRN__wk1IDu0tAU36bj1XGUVulkJVZFYpKeHlePplvALLDbezac_WprUpKr6ZP_4cd1b6Ksv3ueOYIkWLK1zVHEf4J6vQDGXNE-yekIWi92xPUuTzikD-FJbWX5XwEgXayyWSjKGzPzEZeiFp_82MI0d9DhnETfdKhqsoRkR2CB2wdp2J-Uh2fpjo_Vu_aZtswWL6WbDDfVilUZG-qaQX6f27LGrfhCQeJtqxv3gC0pGClQ-YNFbwlTbQ4JIRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛دولت‌آرژانتین دراقدامی قابل توجه روز 14 مهر رو دراین‌کشور تعطیل رسمی اعلام کرده تاهمه‌ بتونن‌ آخرین بازی لئو مسی با پیراهن آرژانتین رو ببینند. حالا اینجا یادی‌کنیم از پاس گل تاریخی او درجام‌جهانی‌که هشت بازیکن انگلیس محو کرد. پاس جوری بود که انگار…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30570" target="_blank">📅 21:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30569">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sS1ru0LJ6b2OEYcgmGuEuQXXz5uUaQpy1rqURx1SOeRTXlMxhuuIQPxne_Ah9iUWQT2Q3oMyNgRtP2Zo8i5MDAYuI86uKdfqrhEVH_slKpNTNBFdxQ1e2dBmbG3DeM9jtTJB11pfgUXxpidcyt4J9Ev3CwfnKnFqL0gsmTGNdwRzonl9AMh2TD-OO-a1o639bxpQahqvO81bL52xjlH-zsZy2lExLrt5a8Hqz42OTNiEfk_N14eXt9dJ_EHXDAy7nZNV6Yjz6RjofmeoBGvP7HlwOo7T1GwtkwgGzVChCV4nn42dj5FA2mEBshEcbwkaakrGHiPwmckQKOxERJSCQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیرعامل باشگاه چادرملو اردکان: بایک مدافع چپ خارجی که سابقه چندین فصل حضور در اینتر میلان رو در ‌کارنامه خود داره در حال مذاکره‌ایم و درصورت توافق نهایی اسم او رو منتشر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30569" target="_blank">📅 21:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30568">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bamcAFhauO1n52O4pKthvEn_YoVj2TFh5mbk4Yl5Xc2srYO9Jx0IKXK6qarmhidRl8BHcaX1BqybJGBnr0_SB43F5JNmJnXTiOurPwKk9I28weLs-sOd0-wzK81FKzix_5elTd6Q1AnC6VlcEppuU1GGA8SgPd3YeSlbTVuOzaL54Os2Be4mboNr_eAJoTMQ71u7vekya8Dr7qpZi-vwJHT1p2UFsnh7mA_Cpw2D6u7VQM3eW_W5GkiFWNWDHy3N1kafGc1Gt8vBmnp9l6-Sd-n1DUXzYebWUiM_XJrOtSvcDI2koX40fS57pdqE0NFFG__nbvIwLyfdn7vmXWQ_-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ژائو فلیکس ستاره پرتغالی النصر عربستان: موقعی‌که کریس‌رونالدو به گل شماره 999 برسه همه جای‌زمین‌دنبالش‌میگردم تا پاس‌گل شماره 1000 اونو خودم بدم و اسممو تو تاریخ جاودانه کنم. با توجه به جدایی رونالدو در نیم فصل از النصر باید تو تیم ملی پرتغال این پاس گل…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30568" target="_blank">📅 21:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30566">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qEHqTwgd9Kf_KeGp6ztjXbJBVKfH87m2RwVXaVULy7FERhaxEWtIqYFA8MFQ4TtcoQtTXCg3DjcCtby_SE30HyBdQzYJ9DFZMD6OshCPK642QhN7Iy1CDiuUCj-RGtKVLVaU4t1ydDnhKB4p21ExVv9jks35Mbyu6MbwVCnOrcCzMRC7XCvbNY9CByvJ21HxGDcn-WfPLw9wa47PcZPXy6-QDIukqO60bsJB6CGldZANqxX8bpQoUfpolMHu0CFIzXLtn5c-eDWyYRDmvCIn7VtNSCxSvm0l6Fl4MB4R4QFYoKwHAi46tMjyXc9QHPLJg2wrQHt3nD0zJcAC0-bpog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d3VSPXA5Ho2MtOPYAnZs27o1jdXDk5HoG3iOvC-5JXJPXWO7EmbP81QBNKSXuP2iB-1a58yXSJBUddAhxntwLeSA9jiHnrnelhTr_q0j04RP7AdGAqNSObWL55s8t1LDtoI_YhRs_egpkMWfpfV5VZprIBHMLtURuf4VA6uYuMnp4mWIhBXpE1Mtv2w9sOt9JrXTsPwN6zphlkug9gurIO4ihYMrs1DPi__HF0ccnzv0eu_bkzGHSeoU1EQkFf8cw_ySMWFxGHOnldYoK1oKA8NNImwBZXb6fzSsgexuS4dmi0knF_Le5f9WHJM_uIJr2UuN1cSitzHPDafJGqtl-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه عملکرد لامین یامال
🆚
هری کین دو کاندید اصلی دریافت توپ طلا در فصل 2025/26
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30566" target="_blank">📅 20:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30565">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2qf3C4jTubMqDw6m1ZXRfPG6Fh9xiz7wGodMkxEYUio3BySR_Af7vbMd3AK5Vwg8btlrWuZu8zkbrjFNeZp9xiu7OaFpCgsf09-YAmfVcH5zfhYxxd4fFCpcfeP-DboKXrlUrjtaKqC4WuhCK5gI7Y_Sf4FIgezTDQB6ZUWqMNXh0QQ7LcphHzJXLrwljWixkCfrFgAwAPcX3tWZ3dFk3YFTkK0DPiaAubdVTaJpWxF6f4urfm6Rusz-44m_6xZTdXpRFaZQmgoYmlfqgl2F7qWrNNUQUtfb7KvDDK6BBTzbySti_1oFuzA612hrlJQke-betuv3A7mlssSGJXWbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آخرین شکست تیم اسپانیا در مارس 2024 مقابل کلمبیا بود این طولانی ترین روند شکست ناپذیری یک تیم اروپایی در تاریخ تیم ملیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30565" target="_blank">📅 20:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30564">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjBqNY43PxPn15Qe3OItQ_3HFLmGEfLXsPg-OIK2OXoCJJdryKoU0EOwRq6M7FWX10LHJCowtbx4WweQIuZYD_Gbosb14FNhxehhA6SM-R5DwJdOLckvuw2rWXR00x1WgVYR2Ek8SF1TO7UqvykRXFcqOoee4uWMeWnflnn8jE23ItpOLTyKxnF6-0wzS_btG6uT0s5zLSByULTCwRaQ4B7jMwhP34_xIswki3cd66O8ljeYY0P2C0C4vozD5aSTyunMIA2ip_ytdGJhqj0IjhA_7l_OBXUoi-1ElJSpdkadWKVlvM8ie2NpKVJLcZWlrQrj6EXUEm1PD7psODlH6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛مهدی‌تارتار سرمربی تیم پرسپولیس روزگذشته به‌پیمان‌حدادی‌مدیرعامل سرخپوشان قول داده درصورت برگزاری جام حذفی در این فصل سه گانه رو برای این باشگاه به ارمغان خواهد آورد.
‼️
مدیریت باشگاه پرسپولیس هم امروز به سازمان لیگ و فدراسیون فوتبال نامه زده و گفته…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30564" target="_blank">📅 20:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30563">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYlSdNvqhwAPms5soA3ctp2Ls6tm-T3b5-c1KkP_Xsu_kw2valzKVa0ji6dglBmk0MfEzkFKuF0UwmP4OycAdsZWjZcoxJlJEyJ4HAqOCAthbkOXZLEOsKPRcthPWcyi5WQI5noQkfzyjvET1agQh9DNsoS1Jzdmpz0ukBBWIYJyuK4_N0146Q_aa6L6NLOu85GbSJfQ8gHryFXOU9Zc76nKXYbuEhXDv8Nb1cZ_Li5zaDEOV0ry6_Pq_106Cn4kl96P6nrcGew30p9UoFRiXNG3Wh9MH4Y3tHm9YuQNUWSm_3tKnS_20nvh6-n5xYFrQlMuEaS6cBTLvSq3H1k2DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول برترین گلزنان تاریخ؛ ارلینگ هالند ستاره 26 ساله منچسترسیتی‌که تا کنون موفق به زدن 370 گل شده گفته که هدفم اینه تا سن 33 سالگی به رکورد هزار گل زده در کل دوران حرفه‌ایم برسم. در حال حاضر کریس رونالدو نزدیک ترین به رکورد هزار گل زده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/30563" target="_blank">📅 20:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30562">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbeQXk_lI5dhrwHOs6sMX4NTrg1_DU4ms-DRwHPNZcRWceapeDaKTgnV5wjnCarLUDzajv5Gc5MyJXxo-12OtRzSj-YfiescxCAjhXx9t2ZhjHBn96-BhskaKXxkVoS1qGcbzazR0pkiYT-QcKHpW2dvI_72DfRRQtVhU-d-WeZYON5xSpWBYo8ZM0ibe-VUSyBIOs19CeoCo-wU0Qc_iUn7A7y0hclw4yrbvdQM6iZq6rnNsiPtMw_HzV-KTdGJbKrNAdX75b15EToLkZ2QRFKuRFR3v8VVr_JV7KRAlOpKu2HQOv9tb95_cCg8pVfGs6tIOoYEyKH5PzweSfNl-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
حجت کریمی مدیرعامل تراکتور: هییچگونه مشکلی با اهدای جام به باشگاه استقلال نداریم و این موضوع رو به مدیران فدراسیون فوتبال گفته‌ایم.
‼️
رسانه‌رسمی باشگاه تراکتور: بانظر حجت کریمی مخالف هستیم و مخالف اهدای جام به استقلالیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/30562" target="_blank">📅 20:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30561">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhg6vDCPK_JkTEFiDgK_ROHd6BIfUWjteJ_G9mBH72IFdkBMYhvIcmzOQNyORiL__4X_mfs_LY0xeF2X16tYTAd075p5Ce_nWxklrObE2ys1PfedKAbvBXKEa8S9B3mCodUHSzmaSfTLX5lWi8FSOEb5kjlQeCxlQs4u9aDyjHwhybVfTKti1OHKrRu5zsiQZR2m8W_hfbzOsCS_mb7EJL3pzB1cGRzh6RXULltxxWAq4FS6MYyGti9lvLoICZefqj04oq82kaYyyHoVH5L4klIoml2jYggLj7ejiSVBEN2TWQ10pQRvJsVMcOC4FQ4aK3LeU_86rxA1TJl5jqSy9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💖
فرم Vip امشب با
ضریب 2.
0 بصورت رایگان قرار گرفت, برای مشاهده بقیه فرم ها وارد لینک زیر بشو
👇
https://t.me/+laf8I3RIuq42MDk8
💵
فوتبال های اروپا شروع شدن و هروز فرم های ضریب بالا وین میکنیم
میگی نه؟ فقط یه شب
بیا آمار چک کن
🫡
🔻
اگه میخوای فقط تماشاچی نباشی و با گوشی تو دستت سود کنی این چنلو گم نکن
⬇️
https://t.me/+laf8I3RIuq42MDk8</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/30561" target="_blank">📅 20:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30560">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHKAQ0GL_c10vyeKqPw6FqdLst0WeImOe1pEIOkMjJJtS6Fc4o2DyFzTq0kXXj0VGuphnE4cNhRm2js5KOhGeLswLPl9BF0z5lUu26iiD_6d0amVKvUdPwxNnru8TwhrqrQP_M2A3s2eh0X7LAZZUn12KUlfGDNGlal8PrpViJKJEk8-4QCcafsPBz_evIT2SneYyK06go362JGdm7mGdCku35vxYft_AeRb1zOT288j5P1YfNnxOX7VRSp9kthkmfJloNi72w1nnYlvhbWxTGl9TkbvTvqfxT9psgbpdKqCgOHFlzNhl3n4zA2kDRhFL5JY4N-COW_1WoUEU5f2Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ال‌ناسیونال: اولیسه خواهان بند آزاد‌سازی ۱۷۵ میلیون‌یورویی درقرارداد جدید با بایرن‌مونیخه و گفته درصورتی تمدیدمیکنم که این بند رو بگنجانید و هر باشگاهی "رئال" این پول رو داد بند رو فعال کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30560" target="_blank">📅 19:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30559">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76d469366f.mp4?token=ShTA0vRQKZZFFYAlex7yeKffchxpdGu6yInkKh22IBGCqTjYqEZzu8mIb-EUMIrvrTT18lgXbcKH8UUxtALUMunONTPP3Ty4VdEiy0nC60Ty7gS3iedDwosqWr_5CBOwIlVKqxL-5TqSPsve2DNWGV_7fK1uM1tlsJuYk95VhmPpBvZh5vhlx5PCD5GDur3pJ6wozmut13H9zC1WCnePPeWRhpgJs_vescTMysXjzpdFuLb9h8vtiEgOGTEPv0QTxeBCuiVlkx2QXhKQIEv_fkG7Jh2whIiUYwF7Gz_PaP7G-_dR8T7lrzMpLBhXHDkVSahgq_ZZED-HvkwFuBYyoD2Hd9w2HIyvsaBTYNmuRIsTZh5ze6yGiCnsatLhaVxi8fkwoBwwWxeby1ZRLU9vVFfz-9r0GlXKlmIGz44JvZ6VetjDOK3T8Wu3p3-wkQbzs87OdYojP0VFGeFYtZG4VvUZlYqUG3qajskK7mqyh2uQdk-0oWUPqrxjWQVdf3-82zuUQQhbmbSDdfhlJtSdR1_wf8wIh-2_fAVa34FP6BZnRaFrtPXkGvr-D0jg-FOEhhLP0s5fxqEW3R5faPyh1xasOilhsVEw9oPYjNC4udOfepGkYG_Hq9ARfjAMzF-_QoypEHVGzUx-yAUfCAa0ZWkeI-ZnjCpvLWTsIfIw9II" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76d469366f.mp4?token=ShTA0vRQKZZFFYAlex7yeKffchxpdGu6yInkKh22IBGCqTjYqEZzu8mIb-EUMIrvrTT18lgXbcKH8UUxtALUMunONTPP3Ty4VdEiy0nC60Ty7gS3iedDwosqWr_5CBOwIlVKqxL-5TqSPsve2DNWGV_7fK1uM1tlsJuYk95VhmPpBvZh5vhlx5PCD5GDur3pJ6wozmut13H9zC1WCnePPeWRhpgJs_vescTMysXjzpdFuLb9h8vtiEgOGTEPv0QTxeBCuiVlkx2QXhKQIEv_fkG7Jh2whIiUYwF7Gz_PaP7G-_dR8T7lrzMpLBhXHDkVSahgq_ZZED-HvkwFuBYyoD2Hd9w2HIyvsaBTYNmuRIsTZh5ze6yGiCnsatLhaVxi8fkwoBwwWxeby1ZRLU9vVFfz-9r0GlXKlmIGz44JvZ6VetjDOK3T8Wu3p3-wkQbzs87OdYojP0VFGeFYtZG4VvUZlYqUG3qajskK7mqyh2uQdk-0oWUPqrxjWQVdf3-82zuUQQhbmbSDdfhlJtSdR1_wf8wIh-2_fAVa34FP6BZnRaFrtPXkGvr-D0jg-FOEhhLP0s5fxqEW3R5faPyh1xasOilhsVEw9oPYjNC4udOfepGkYG_Hq9ARfjAMzF-_QoypEHVGzUx-yAUfCAa0ZWkeI-ZnjCpvLWTsIfIw9II" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
ویدیویی‌از پاس‌های‌تماشایی و خلاقانه تونی کروس دردوران حضور در رئال؛ زیدان در مصاحبه‌ای گفته‌بود کروس بهترین‌هافبکی بود که زیر نظرش کار کرده و به داشتن همچین شاگردی افتخار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30559" target="_blank">📅 19:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30558">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uATlD-VU_Px604ldxSSMJkUpGKmayMXiALaPwt6-UHKacnsX9q29Z4qjXvNVsCmFYKskPS5yN2Ap-YYJuS6DOrkfxt3Ff5dPpG3rptzzH7DXl7c0lsYePsJNjO2qPH_eEihYP5XzwVynZCw78YYyBr_0kl5jT_truCLkcMqgDqE24cWet2q0IYYHu8fRAgBk44TiOIHTgNgQQJnofNlMlxQ8G2m2AVwvNqGH2cJEdjigvGB0CYkicc3UsWJoapCZO99WKfmI1RNUHAmTWW25lDbapxhXAzwjYG-O-N5Pi5Zh6W6TEMGLbDjkg0yj36cPtDTFNttWddkJCon4M2DXDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ سید حسین حسینی اولین بازیکن مطرح تاریخ لیگ برتره که برای خودش فن پیج زده و سیو هاش رو باتعریف‌وتمجید ازخودش تواون قرار میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30558" target="_blank">📅 19:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30557">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHpX5exTMo61Fyoze5vi6hC-9J9pMOsRA_zFko7v8BABDUkuxrSL1VcTuRIVwLWLGRR2y-SyW_v_eVg9cHoAR4LTQyJeTNZ6nz9j8pBMgqKT5Om1r-Ukc9S5NRZfUMl9eEksH0rhovjs936r8sChHKPG4ywamhJsAm7lACuUIU9J1B7uetvkw2Om_6ch54ENG7uGBzRHQuDBbbCGo1RVUm1JQo3m_XnYCwydQ9DR_5ZG9WXbkHwYoQ_4Y-upyncrt2ZzgtIWEmVNJcKeYhuNkoZ_fuid_XdOjMUmv75PLqwk6HZD6MO1NszAZxXS0RahhI5MshPULwag2Bh2ENb2Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌ملت‌های‌اروپا؛پیروزی‌ارزشمند یاران لوکا مودریچ و کامبک‌تماشایی لاروخا مقابل شاگردان توماس توخل؛ سه شیرها نتونستن انتقام بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30557" target="_blank">📅 18:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30556">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7389e745f9.mp4?token=TTAzkOovhZnBla_sc9JGUQX1-Qo14V6WYeiSZ-lNJi-QifRMoopIvrDsFt33cOD6P20I--cEufwNBqOJwzPaKO2xHwElbm6Cvbd5-DagFZ6QJusnc3kDkV9RyQ2cIum8e20Jvlrc3BUlSScZ99Mmx-lDGJLrdrwquGep8EKWeOXDbsMfqpjOrVSvOVuw2cfRs7-1bAu4CNy1Iv2QS0Iwh8gtlZBDt5Mjhu9V51kg3syRLOvNIFTlQDCeET8RmqbmAL1-Lc5z4U9dsH0pSa4jX5c1qEnONSvb_N3wV4UsE-1FYsBS2Jh513SyFOuckobozDy0dh7-jvKgQUKHo-twDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7389e745f9.mp4?token=TTAzkOovhZnBla_sc9JGUQX1-Qo14V6WYeiSZ-lNJi-QifRMoopIvrDsFt33cOD6P20I--cEufwNBqOJwzPaKO2xHwElbm6Cvbd5-DagFZ6QJusnc3kDkV9RyQ2cIum8e20Jvlrc3BUlSScZ99Mmx-lDGJLrdrwquGep8EKWeOXDbsMfqpjOrVSvOVuw2cfRs7-1bAu4CNy1Iv2QS0Iwh8gtlZBDt5Mjhu9V51kg3syRLOvNIFTlQDCeET8RmqbmAL1-Lc5z4U9dsH0pSa4jX5c1qEnONSvb_N3wV4UsE-1FYsBS2Jh513SyFOuckobozDy0dh7-jvKgQUKHo-twDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
🤩
#تکمیلی؛ تمام85هزار بلیت مسابقه خدا حافظی لیونل مسی تو چهار دقیقه به فروش رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30556" target="_blank">📅 18:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30555">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdvWH8AmnJsjxuPIl5Brvrjaxs2RloA1vQQ_AYPIn9z9VhukQH7WSXdR8rmBJtOBPDyLquyb7TFvyPyHkMmcSa-bz-9b4GGAJk_OFjUppGLKmjQfe5U9C3o1BweXmeoWTeo8Q5-owUL81O7rkOGw4g2tBRyzCvdsSPqu9rRj8MA_dyqkmnPWIFEqeUZ1gFrDhAZSKdbHyx9ofKEFmNKCRxHB-p2RyyZ7NfW7CjAfdGoiNK1e0AipV3_j4Uenk0pZJdQ8zEN2EQF8_KadgpOfNd-Xtxxhy2BYwvduYslJDJsBMtaysqv87feDJKHsUtuWBr6o0FfuYf7THYxV7dsAwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه گاتزتا: روبرتو مانچینی در زمان حضورش تو منچسترسیتی دوتاقرارداد بسته بوده. یک قرارداد رسمی با خود باشگاه به ارزش 1.69 میلیون یورو در سال و یکی‌هم یه قرارداد باالجزیره‌امارات برای فقط چهار روز کار مشاوره به ارزش 2.03 میلیون یورو! هردوی این باشگاه ها…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30555" target="_blank">📅 17:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30554">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nc9Qtg9IVl64paTwdffjr4Ashb20SlIF8RLX0FSe3UG9yEvcGXHNiGzVsRk4Gmcgl_UqMjwm31wtc7wa9gCHDLx0JWgNHMMsZn_80E7DmnV41pk9x5O5UoLeej0BU0Zyg7p1TZYH11USF3jUEuvk-uw7ucshIoeksVeuVsWCwrgnIJcYcEA-PtHUbA_d1Y40OL0QumOiIIRF8MQSU5eQBXnnmoTqziY0ot1riRE0KTBEWkFAkxBkp6xvJLyF3N5Uljp08Q8uO3c1hs66-HwHnSC47Px8fVkkvUYN4lFDaD6faRuNFLp8qf-mOL9PvEfY8vy6lFv-xMsnjEcfc4wX0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حالا که بحث تخلف من سیتی داغه یادی کنیم از 3 فصل شاهکار فوق العاده لیورپولِ یورگن کلوپ که زیرسایه قهرمانی های منچسترسیتی پپ دیده نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30554" target="_blank">📅 17:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30553">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeqMahzRqhwd3A6q1abVEuZfNIp-pgPGjXdytzrDKXbSIikVRnOBAYhIiKYSbg6vBcUPuF4XGXHla4iG77J07ZQ21VhTKo4I-mvNKuhLfcZmNIYAou9HVjIPr1DIvasXqHp9DOrtssP3qwQNqSlH4cYu5ZyCuOU0XA3blTOLxP5ekg8v2Y4wjSIdsT1l3QPiCMku_bXqxIoYysOd9z7O9NE9mGlbeR4qvHyycfygs0Us0YFVLTEXuRjtXVFz18cXdQE9bfHrVo9fGhygS2vy_Luk-IW0uJuxr9PezAcGsTqG7S__NsOoQ1YWnSwRWy3bMpGEJmMeRp8z5cwuEsUxDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
سال2014
: کروس به‌رئال‌پیوست‌. 8 هزار هوادار رئال مادرید در سانتیاگو برنابئو از او استقبال کردند.
🗓
سال2024
: کروس با پیراهن‌رئال از دنیای فوتبال خداحافظی کرد. 80 هزار هوادار او رو بدرقه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30553" target="_blank">📅 17:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30552">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpEJe3Igckhp2kfgFKEYkz7Jc946npr7XyKsroR6WAfbk7UMwPNu1jgoU-JT3NbFgLDIS9WA5GSBX1e-GfBo0Jt-jH4Zf15lXGg-aLNGLfgU9PoDOvhkk8DKyFKWpBtP7rtk2_1NbA5rWN_5UOZbr9QIL63omZpVGYkQGEZHV3oEhd6vJtsoSk2We42D4X6iGcxpBiqaP5EUoWMn84Grq7QGVip5I_97ITAQduzXd2HsmhZ58NyJXfMBQVppNCBPkojr384cRzjMfgcr-aMEjz_jWcMfsHuvkLku3xDyKpTb6afyOx2OCp2iVI74T5OR3fOAsH8jICThhrH7YM1PYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آخرین شکست تیم اسپانیا در مارس 2024 مقابل کلمبیا بود این طولانی ترین روند شکست ناپذیری یک تیم اروپایی در تاریخ تیم ملیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30552" target="_blank">📅 16:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30551">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJ0i8M4sIzHZHAdV5TPP0vYyT69SNsywBVfEg8SYOZBvkHddYnRTUagjCAMs3cphXhKqMPVIqx945g5mH7zX10J2Gov8GJdZZazAYSLlIE8kWPrgfxMnTYbh-muQD8rsPgSxJ7cnwjnrAQV2JR8dnL3BHJ75w0Oh8yUcvpJbjXr07dNciulw5PxmDBCLBKM6Qk6m6Z82BTiDBfYo-3oPNOSHkZp-G_cuZrScAttKPWTWz8cpIaQt_3m3jME5EmT4SWwptYEM7TcXYF5TxJe_xS-pNplFNAFbUEuee3ZsxZtf0YVIhlLdi8RcQ5nX5LuF06S8tt_vAcQiweOFuYB_rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جما اتکینسون، دوست‌دختر سابق کریس رونالدو گفت که بعداز جدایی‌ بهش‌پیشنهاد پول داده بودن تا علیه او صحبت‌کنه: وقتی‌از هم جداشدیم به من پول زیادی پیشنهاد شد تاپشت‌سرش بدبگم؛ ولی من قبول نکردم، چون واقعاً هیچ چیز بدی برای گفتن درباره‌ش نداشتم پس دلیلی هم نبود که ازش بد بگم. هنوز هم کریستیانو رونالدو رو از صمیم قلبم دوست دارم.
​
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30551" target="_blank">📅 16:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30550">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
#تکمیلی؛ مستر المپیای امسال قهرمان تازه‌ای به خودش دید. نیک‌واکرآمریکایی قهرمان مستر المپیای 2026شد. سمسون‌داودا، درک‌لانسفورد و اندرو جکد هم رتبه‌های 2 تا 4 این مسابقات رو بدست آوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30550" target="_blank">📅 16:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30549">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfomH_etnrCQJi2B26y1xrk9G5pmzafLiqtFEirFLPGHOiho37HZT1oZI10QJHHJoDROgmE-0T5SYqBmxM8eRj0Bk1tC77Sgoe5osFnp4EE4g-h01U-ICA5Swix5Y_4iMQWS4OYa2aUao2kDt7FtdOvQrtaZ4oNBazKCQx6RFwhVXC31PiRwnVZz8qxn1UwEWDxk_BywJ9hJ6EmIbVlU6dd6G2o5jtDA23A-znLcKDhk3ZJqoygQXIVIv3DPicyE51OWMqfE-Lu-R9ROKP--56qzC1QAkiTtBoZaaYOUWMBM234GcvUbkSwqcIDzRzeV4gFAX72pwogw4i1CuPyHWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
حجت کریمی مدیرعامل تراکتور: هییچگونه مشکلی با اهدای جام به باشگاه استقلال نداریم و این موضوع رو به مدیران فدراسیون فوتبال گفته‌ایم.
‼️
رسانه‌رسمی باشگاه تراکتور: بانظر حجت کریمی مخالف هستیم و مخالف اهدای جام به استقلالیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30549" target="_blank">📅 16:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30548">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8b814e56a.mp4?token=iB69d5sQsE5GLZJ677OOnKJH8s3D4uFg5j0T-9njz1Ttl-z6jwx80odj7iwaV9FsVesFMRZ2tHptwvfF4yzu-E_UZ4f9UruPgAf655WYYz9n5xhtBzXw27eELL5YxoTpw-ASJyan8IP8UpxuRFI3rKjhx3Brg6JICcA9v8egT1BtcIiY0Yz3gTwM4qRLyjAv6pZd7b43fwaFB9RosSA-nVcXqtAjBFzNRTnIjDW6X6DrwuMoL62BSplvmiEPnvKs32s9y5VscZs_EjjDWKB4eFRdDstnH5MNa6-0VzKM0F0O8Ah2V2EK6BLFvAj5QRQDOXtcvT_qpX4VhsViUdYg6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8b814e56a.mp4?token=iB69d5sQsE5GLZJ677OOnKJH8s3D4uFg5j0T-9njz1Ttl-z6jwx80odj7iwaV9FsVesFMRZ2tHptwvfF4yzu-E_UZ4f9UruPgAf655WYYz9n5xhtBzXw27eELL5YxoTpw-ASJyan8IP8UpxuRFI3rKjhx3Brg6JICcA9v8egT1BtcIiY0Yz3gTwM4qRLyjAv6pZd7b43fwaFB9RosSA-nVcXqtAjBFzNRTnIjDW6X6DrwuMoL62BSplvmiEPnvKs32s9y5VscZs_EjjDWKB4eFRdDstnH5MNa6-0VzKM0F0O8Ah2V2EK6BLFvAj5QRQDOXtcvT_qpX4VhsViUdYg6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ سازمان لیگ مجددا کارت بازی علیرضا بیرانوند رو به مدت یک ماه تا پایان مهر ماه برای تیم تراکتور تبریز صادرکرد و این دروازه‌بان میتونه که در بازی هفته هشتم با استقلال تیمش رو همراهی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30548" target="_blank">📅 15:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30547">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQ6i2EADZahA6jRJ8x6NULQJYxurxjYaRNmZjWAGa37_s_7vOaEFjiC10zRZh9eLEsCKCLj2-4a6xkqYmxiCUHU3Io3QEKYOeUtFB0rEdshZ8kUtOoftsPo_ju6V1WDB--SNvVDZt6ovx16oBaUcHyT7g2h6efRdUp5DhBfJNl-qqDvVAqR0RCCo7z6h0GJWxb24bAsoxXMrAV8RZNQ_unZBlh1_7asPUhVdc7NvVqQQJ6dPjcMQd-1qIvb9nVwg6-fz23iwAYNLviqF0eaqjKs_c5Yl6sZLviC76RCUavJ16WSR9WyR0GbQYBbcYA4jJNXygAErJiYUn9PiG6mgAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد خیره کننده ژائو فلیکس ستاره پرتغالی النصر دراین‌فصل: 17 بازی، 15 گل زده، 4 پاس‌گل، 9بازی دریافت‌جایزه بهترین بازیکن زمین، نمره 9.1  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30547" target="_blank">📅 15:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30545">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sknjLHPpf965zU0jrwMP0p3l7BVzfEvgfCAFMfTqGQM2DpDQDBKiiVe9pvp_-SsRQvVgQQr4KqevwDU71tZwGeb7Z0qztifFu0LfvJEqIWabIdQGpf9JQPI6QcqtadMJRRYXTo9a9fZ56Op2GhZsYIYlnvoMPfihAqxHPokq_uLOfAaQT3BUGSN_8mNIy0BtT5hp6tJzwcvaDxY0okFykqErMigc4wBZyqR02khFDdIglclVxqF8K27zualOorLCvrfF-CmgJOPkM6Gp5R4xtVcU6ro7VbDOqOCrK4YrEVVcAlklNlsOZ7aKPEyfYF-E3AqSziZmCq0X498nhbl2kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IHiXXSIsleR9XFcVu2AsOMss1pQH0KTbcpoPWRyu4KzdtHK7UeELBcPiY0is1usZN2Mwt-O6YCIQCAIMTp9KrB0Rfr80xV1J0hMfc5AN4qAhtaSSWC3gsWVk27qOdEM2nluWOT2qMvCoycgGyF9DQcXNybzq2Fq5D4IdKUAdkijpRoziw06PeEek2BvsKegHb3IvmgzaC-28IGEqfJoh_JafSJoQ-H9keVi6q1J-EPa8LQVVqDSBysTsjpHANUJ2xx6QJ0ifhy_U64v14x4b6vXfLoAITKvm1xPTaQmNsIycMjFufbKBsry-MFC1PX4M4PRTIoXYb4wIw2Iq_FixEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ اسپانیاباپیروزی 3 بر 2 مقابل انگلیس در ومبلی، هشتمین برد متوالی خود را ثبت کرد و در این 8 بازی 17 گل زد و تنها 3 گل دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30545" target="_blank">📅 15:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30544">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnh0kFC_gPkhBTJz4vH2EqF5s_BphMX-fFhbGyYaiKLoVHLPkTwihMVyX1_kqHK7EBmNBPtH840a7iyJmlG7aH76Bfaw7vLJhclE3P3EQy5bpGD1luLKiD2csggKnfZjtTVGpxPstjaBdwlcO-pF2ownsHThX8MvkF4xFnVb0KlIT-gZppPjIqemPVlztlkd1e9u03n8PTi8xyJG27-38tN1jiB4ZsmtXvO5ISGKUzQZDwHBB40Ha30t33X7_wNbNR_ixh3H8QiN3TIWMwLm0K3ujYsq7ZP7G0_cdfdQe_JyqAUxZwcsl8N7PkoeOifVRreaBUinZZgQV5trJwsvWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ تاجرنیا پیرو خبر اختصاصی پرشیانا: فدراسیون فوتبال صراحتا به ما قول داده اند که جام قهرمانی فصل گذشته لیگ برتر رو به استقلال بدهند و ما منتظریم که فدراسیون به وعده‌اش عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30544" target="_blank">📅 14:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30543">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeuOS_uvAluwIoWHpwGUEbhumu5yGbRSNOMG9AjQWYsAIyxz5Bp9fnsRhL9iebCJ2d4s91tNymik4buXD_DgJvrhDtz6u96VZqjYx5MhNP9QHrvahQhb3RQvQOTTksk4uFFPIV9-ECcIEzBOHT4He34nWS4ah6scDococEJkpyCp7bhfyc78UJR8EiVx_ITXJ-p2MFKSJxqKVkFiZZi25PhOmar4AIstq415pE-wXbnjgj7gtUQmDqMKZs4z1x7qTqV8GKl6KYWIaHz43mWMAbzRbS7cXtF7oWvhBuHePgtzjs5p2f1-50piaUBhxTVQQs4yC8zbngFIt78EuCMmKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تابانی‌به‌فینال‌مسابقه‌مسترالمپیا 2026 نرسید؛ بهروز تابانی درجمع ۱۰ نفربرتر مرحله مقدماتی دسته اوپن قرار نگرفت و از صعود به فینال رقابتا بازماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30543" target="_blank">📅 13:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30542">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc0fcb29e0.mp4?token=s5qNO1h4olFrhvnLDKHBzJ6ZSo7j-DhOvZEr8JvNJ3Ng8mYKVRXVWkKRL8W-jTuOaEEoZOzLWMTctSGLQsrgAXeY-gjBvazAtnj_PXQIMGi4-3V1XxXt9ifEdf0hCnbEEfTh30Kbb9RfBfHt4S3E4uhuNmXEf1pePSdPhKoLK4XMmtBQVl4DdUfoTo_0ghVMy8LcAQ1V1TeGHKOX8xlKs1A6beSBW_pF8AmsqDSvGZz0DaLX5EhCgdTdZSFtnffs2HXxX597Vcimogl6gdRhaTjtyYFOnUepERLNvbE0Jd7ChYiXZfPupcvuCmp_YIomx_EnojiWY00FAUq0klhr5oD-QneA88MwsCD7qYH4fkwndC9SFdt69y4AppZqe8TG4P7pcturf4Kj9neEY5fe90N6hmBF1eDmaaS9__DDjSElJsgB0VFCb4jcrkEilFMyqV1sSjFSaOuTHtfT7jf2Fu3ZGZf7IOgspV7FovIignyxoZXgY3QvGHj7vguKeUesA_21u5_2C_eeytaQuHrQ0YVqoxHCy6-VRl2RbTHQB1bg83Z1RetzMpV8e31q5n35ejzwqAcyCYoapNbY8q07pzKStBwdfxc0vs8bs6Rhgvhk25o1flerRSLwuI1JpLVBc0dvYnF34Dobys1r1UivBaVwEfRpOOVRQyS7qKH38FU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc0fcb29e0.mp4?token=s5qNO1h4olFrhvnLDKHBzJ6ZSo7j-DhOvZEr8JvNJ3Ng8mYKVRXVWkKRL8W-jTuOaEEoZOzLWMTctSGLQsrgAXeY-gjBvazAtnj_PXQIMGi4-3V1XxXt9ifEdf0hCnbEEfTh30Kbb9RfBfHt4S3E4uhuNmXEf1pePSdPhKoLK4XMmtBQVl4DdUfoTo_0ghVMy8LcAQ1V1TeGHKOX8xlKs1A6beSBW_pF8AmsqDSvGZz0DaLX5EhCgdTdZSFtnffs2HXxX597Vcimogl6gdRhaTjtyYFOnUepERLNvbE0Jd7ChYiXZfPupcvuCmp_YIomx_EnojiWY00FAUq0klhr5oD-QneA88MwsCD7qYH4fkwndC9SFdt69y4AppZqe8TG4P7pcturf4Kj9neEY5fe90N6hmBF1eDmaaS9__DDjSElJsgB0VFCb4jcrkEilFMyqV1sSjFSaOuTHtfT7jf2Fu3ZGZf7IOgspV7FovIignyxoZXgY3QvGHj7vguKeUesA_21u5_2C_eeytaQuHrQ0YVqoxHCy6-VRl2RbTHQB1bg83Z1RetzMpV8e31q5n35ejzwqAcyCYoapNbY8q07pzKStBwdfxc0vs8bs6Rhgvhk25o1flerRSLwuI1JpLVBc0dvYnF34Dobys1r1UivBaVwEfRpOOVRQyS7qKH38FU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
ماجرای بسیار جالب و شنیدنی سرمربیگری دلافوئینته در تیم ملی اسپانیا؛ این ویدیو رو ببینید برگاتون میریزه که ایشون چطوری سرمربی اسپانیا شده و هم قهرمانی یورو رو گرفت هم جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30542" target="_blank">📅 13:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30541">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4E0QcjSFzyTLhsXaErPAS2OSaMukUhUqeL5srgRPivWv4G_tr4jfGud2tir_Nz9G7iTlXO2diI2CiTKU4Z_Sniix7gzMghz7Jj7yqJfqk7SxqeF_L6h2MObU2mHceiFR7mBMWKA6bjshhv0QjWaicn1G2xIzGkngpJabVgUrgPEo4FkpGWx8gXK_AqqIFbW-Cg05H1czKnDKiI09b7C6Z3wb4gRSMAP35wO9p_B2-29nABs0sa1iWisjRxYJl_ZYw8wiRWxP5wVHQdJeSHYV9g8vgZq57Ukz-eFSIaZrpNjJhJWglEGCogls4rfd11XFzgIEkR3gJFLApbwnlYnqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌ملت‌های‌اروپا؛پیروزی‌ارزشمند یاران لوکا مودریچ و کامبک‌تماشایی لاروخا مقابل شاگردان توماس توخل؛ سه شیرها نتونستن انتقام بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30541" target="_blank">📅 13:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30540">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQkJIAvO3yzDCDzcTuqEHL2gOMsGtGw7c_sX5KVq40XU511dDfn0Gf_Lb8wG4or9vHf_9Zg6vZ_Tmofw0E5kvV1TcdGlVq9cRVQWublYTmiQJ2g3ALiG4KJlZZC0nkAOYYiLIy8Wuz0UtHKCoM17FAiEwUod6NUs3h8Gpk-ba5WnC9jl5x0GOOhX6_wICV1FoBOGHi88-wkx-kJHWWhBfYiOLMVNU7AegJ_KCuklrflnxN3Og7_8MzWfC7zN7zeXcTrDM9Q70AKOoJzCysJxLHGAglb7MbZEZGFOkJkDP9lvr6x5WxVc2EK8Pt9Bz6DsQFItd_BY5lqH_b-EP4fPoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛علی‌رغم‌اینکه‌فدراسیون و سازمان لیگ گفته‌اند بخاطر فشردگی مسابقات لیگ، فیفادی و لیگ نخبگان آسیا احتمال برگزاری رقابت‌های جام حذفی بسیار کم هست اما باشگاه پرسپولیس اعلام کرده حتی حاضر است بدون ملی پوشان بازی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30540" target="_blank">📅 13:09 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

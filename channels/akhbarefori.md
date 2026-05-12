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
<img src="https://cdn4.telesco.pe/file/ixB6tXTcshTlCqs4McarC_Rmhfddiydd0Q1juglucSNN_ydlp1lvI9kLiFTk4vcojOAuWMJETlaJhqCGB7hdeqFKybqyCIjGW43mBUrLqTndHWY_Gx3f-mMcAL1t6ldvJkd1gZAHvndG1qy5020J5vLXYmsH20B3tUGhsHhgUxEU3wc5w1KjDfXZu_ShhDuZMRmzXtqBODPGhqhE8d41r2D9Kw-Hv47I7xzue347dBqFt4HG_G5hPmIE5GNZIwAXMHCctSyhXUVflglbLcFkTOqwYaWGw_g21PVXrdASQnAeAj69g6BwvNGbk6KpT8Jwuw4st_DDsD24aQkR5KoMvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.9M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 12:56:52</div>
<hr>

<div class="tg-post" id="msg-651916">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLlW8vzemsQ7mhe8Vl_RNgoVn1ENWHMFSRZmdr_R-WwLF650edsTzZs-ZzBbmYF32lwVuOPDQHYGBDT1ktCuD5TzIkavXFBu4mSNgLlS51d0KVvAYvLI2kSIqdCiPhCjRm_IMOdivA5TPnlz-Wq8ZWybjClyhjK_6hQLlNTQ3cIA4IV7lHPMJRN8NmlhghA30HiKeKDfuyuZ-8npYLPO3Ucbtrm3Zv7RGAx5iy8NRArM76uSZ_6N3XSP9Kihip_-CiHXItX19U149xOXs-8A9mI613FpDrO89l3g-Bq1yeS2VTVa0aQHMW2rBaPie6KIqsYV6mfKaYT7dky_z7raGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شیخ نعیم قاسم: با تجهیزات اندک مقابل گروهی وحشی و مجهز ایستادیم
🔹
پیام دبیرکل حزب الله: گفتند کار شما تمام است و شکست خواهید خورد! اما جهاد شما به اسطوره‌ای از پایداری تبدیل شده که جهان را شگفت‌زده کرد. از کجا آمده‌اید؟ چگونه خود را آماده کرده‌اید؟ تعداد شما چقدر است که پایانی ندارد؟
🔹
ریسمان شما تا آسمان امتداد دارد و پروردگارتان پاداشی بی‌پایان به شما عطا می‌کند. شما فرزندان پاک جنوبِ و دارای شرافت هستید و لبنانِ مستقل و دارای حاکمیت مورد حمایت جنوب است و انسانیت در آزادسازی جنوب تجلی می‌یابد.
🔹
ما با دشمن جنایتکار و وحشی «اسرائیلی» مقابله می‌کنیم که مورد حمایت مستبد خونریز آمریکایی است.
🔹
امروز جمعیتی زیاد با نیرویی عظیم و وحشیگری وحشتناک در مقابل گروهی کوچک، با تعداد، تجهیزات و حامیان اندک قرار گرفته است. اما این گروه کوچک پشتیبانش خداست و درنتیجه ما پیروز خواهیم شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 963 · <a href="https://t.me/akhbarefori/651916" target="_blank">📅 12:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651915">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
دبیرکل حزب‌الله: هرگز تسلیم نخواهیم شد
🔹
ما با تجاوز اسرائیلی-آمریکایی روبه‌رو هستیم که می‌خواهد کشورمان لبنان را تسلیم کند تا بخشی از «اسرائیل بزرگ» باشد اما ما هرگز سر خم نخواهیم کرد و تسلیم نخواهیم شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/651915" target="_blank">📅 12:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651913">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9rxYGJRhuG9bowtWihI8vBCKRiiok8X2_TV2wrrLoavqvZmVUvODLb8X4q4Be9n9NR0SmX5W3c1znghj5rBnAKdAYOiqNj8trnS5OADXC7PR7TYj2t230zYxVcOiVA_UDTTTOJFEF-2HC3DqDg-kGLEAj9z0035SToivV9ux5yNM__Gpy-rF3jbl7wDyKNsvMJyrc1kxu77E82_XlzGlHTpgVZo8iCzzhhiTOdd2gqTf60l29D5n4rco7WuD-gqGdUGEpbkDpQxx3N0HaxlMhSICNHxY75ed8NrCuTGtOunBCsE6fSb5wNjuOAti_6ZAY0eT0n82dChx5Ok8Zrtlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شیخ نعیم قاسم: پهپادهای حزب الله اشغالگران اسرائیلی را خفه می‌کند
🔹
دبیرکل حزب‌الله لبنان در پیامی به فرماندهان و رزمندگان مقاومت اسلامی : پهپادهای شما زمین را در برگرفته و اشغالگران اسرائیلی را خفه می‌کنند.
🔹
پهپادهای شما، اشرار و ظالمان زمین را به وحشت می‌اندازد، موشک‌های شما زندگی آنها را متزلزل می‌کند و آنها را دچار اضطراب و بحران‌های روانی می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/akhbarefori/651913" target="_blank">📅 12:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651912">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upEHr19Qo3Z_oew2MYC560RZy5IyX8DR9IbH8AeRUbKSBPiyoHRqWwQkdvI6heAZh4Nt-XnlhDibYItvUyByW-IIIR4fiuFJmu9MdV6y89AGze9bkmCMGcBoM3MWo8kjweHcuwCUS7Qq0zOa6bMJI3D87P7akrG_ejwm1tkV5Wfp40uwYvTdMw3XCLRl8klXmufXphmRtQibfT33wVj1ZNMnk4YswjKa-TTru-m9bSzyqbAKX1mcvtjjQTorjAXirzOCFLe3haVeybccnPb2fJlQMZhRnCGNWrv07AlylEyLFeLyiT2QKdzKEI-tCVeVYlVxV58BNPJB3uXD8xjLHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلوند، پرشور و ساختگی | طرفداران ترامپ که توسط هوش مصنوعی تولید شده‌اند
🔹
در آستانه انتخابات میان‌دوره‌ای آمریکا، موجی از تصاویر و ویدئوهای تولیدشده با هوش مصنوعی در شبکه‌های اجتماعی به چشم می‌خورد که زنانی جوان، بلوند و جذاب را در حال حمایت پرشور از دونالد ترامپ نشان می‌دهد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3214392</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/akhbarefori/651912" target="_blank">📅 12:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651911">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCYmoAhZCTIw07MllJ2cEHJlkdxAbCaeXPYEITAV0oGibQD1fcF5aCOX-v8MC8NzH1fiTL0YG-R7xclnFzKRWEpRXDWUzKKLWWfP1Q6gzsnaGFdu5K08D6ZM3vPcLHDFaizF4iFEU3fyzR8Kr0jORfAnxhKPAegBa_Eapn2ZoHo58XtwTqP12gD2XCQwY20cR2JVn8jM2XsXwz_hr132aA8fAgi3ir_CeP098KwPfxRYnDjvVyXybAVoYTApTUbzBN0SYctSLfDi10zSIM-QzXMckSJZTMOsuLPg_AdktQTaY1soKPNBavDDimqgq2WPso-lv15T_3DgmYKFEGFhpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابعاد تازه از آزار جنسی اسرای فلسطینی‌ به روایت خبرنگار ارشد آمریکایی
🔹
یک نویسنده آمریکایی در تحقیقات گسترده‌ای ابعاد تازه‌ای از شکنجه و آزار جنسی فلسطینی‌ها در زندان‌ها و همچنین از سوی شهرک‌نشینان فاش کرد.
🔹
نیکولاس کریستوف در مقاله خود در روزنامه نیویورک تایمز نوشت با ۱۴ فلسطینی گفت‌وگو کرده که تأکید داشته‌اند در جریان بازداشت توسط نیروهای اسرائیلی یا شهرک‌نشینان مورد تعرض جنسی قرار گرفته‌اند. او همچنین با وکلا، فعالان امدادی، بازجویان و اعضای خانواده قربانیان مصاحبه کرده تا برخی روایت‌ها را راستی‌آزمایی کند.
🔹
در میان شدیدترین روایت‌ها، شهادت خبرنگار فلسطینی سامی الساعی قرار دارد که در سال ۲۰۲۴ بازداشت شده است. او می‌گوید نگهبانان زندان او را برهنه کرده، مورد ضرب‌وشتم قرار داده و با ابزارهای مختلف و همراه با تمسخر و تحقیر به او تعرض کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/akhbarefori/651911" target="_blank">📅 12:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651910">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5P7QTkW_LTdOCFp0IyFnT4dueJ9jA6pJIPtO1reHXOvK9A-7JIclVEt38WfkFJXFHlXuuLbs1M9OMVYiw8nG2FSrfbPfYn6Co3xXpES7O5OGE1_0vP1bU_ccIQ2T3Vm1FlT4gpVSRTz9S38cEz7sglo8j7erKdZJCVEmU4tDtCXyPnosDBVjYhWplaoLqCDXJZGPjonU3B7RgvRMsHpZGJ87L9o8IyWRb2qnsCZlhhONH1J75WHRP0mND5TITx57c585_Z6IvEqoGOBqG0KH40BqsqiCgqacllH6uGtnTb8XmXWar9ZJcW8ayrQzlDqtk4devekx0JlHwWKqUmjVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لشکر «جان‌فدا برای ایران» از ۳۱ میلیون و ۵۰۰ هزار نفر فراتر رفت
🔹
تاکنون بیش از ۳۱ میلیون و ۵۰۴ هزار نفر از هموطنان با ثبت‌نام در پویش ملی «جان‌فدا» آمادگی خود را برای دفاع از تمامیت ارضی کشور در برابر تهدیدات دشمن آمریکایی- صهیونیستی اعلام کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/akhbarefori/651910" target="_blank">📅 12:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651909">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
سخنگوی دولت: دولت علاقه‌مند است تا هر چقدر مقدور باشد رقم کالابرگ را افزایش دهد؛ این موضوع همچنان در دست بررسی است؛ چنانچه به نتیجه برسد اعلام خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/akhbarefori/651909" target="_blank">📅 11:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651908">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXCWF0XVCj4eGrm4MiTLNLI-CnfgQYSSTllLjMkZP6gga-BJpYIpiwpDCE9zpuBX0wDP9qjKn57hkCziuYUUgIsY1YU1sqE-lz40_7Oqjysjz9mgAwAFs3HqaK7P6RfyfkoQ-zHb_GiQrEKnu5V1X-TcO7h6ZWYOKUyi2eSvAILVnREEWxAyBh5vBboeQhJav8x2YMIauBeR-_xj-sanL0DB-Clgw0jwwM6_E4RRws4aUken3dZOViwMNkrIdEbo8ZhVqdDm0YLCz_mH_bOctoj-VmAz6xkGZA9VXDnsV7Dx6xEo6hR9Y20jpZEfAKuj60Fl-jmDLT0KYjREamk5Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمین، قربانی مصرف ما
🔹
نجات زمین را از همین امروز و از انتخاب‌های ساده شروع کنیم  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/akhbarefori/651908" target="_blank">📅 11:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651905">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XaVI3IYNn8Z3X7zGE0RmOdm8pg8bX8EE11d1gsGWvS9XNeZIgFj13AHuBMs-L-2Y_cbHH7asI4sk-iUYd6MLwKhGOqijbro5UaTle-VpByW6EVFIbPd0MW__88IRy1kvYU-o03fn_OkvtqPPWpM9sygO9Eeaxt1rVGgc1ilF5PEFGiUDYL2Kg-KwHTcb6veQA6t5ajakERs7Dv04ZUWmNiNzSbO4J-T4Y2Ud5t3Ofq25noF56MeWDE8cc7NrQeJnjJNV1q58V9fJIgNP9A8fDoY0QWOce79RnVNJgwtgokwzIpec7jBo0nTC1_JDL-XJp7oHM-v8oFYm7sufOiROnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pRcfL5Lgrb1TdSihT0MfY9peZv7FeiQwDFpai7_xpWdFpwAooU7bpMbnKgw5i740uFbO7DfbZe02w7xeP-lMdoTXz_vaKJbCRHZ_gHNNmAgsHCyS80u1rkbMgKomdDNvodKqrGMCOXR0J5JN7DwfMobwx7MW6PRzBTuowDkpQbraSDybKfSpeys5rmgWmpfrHNkd28Vq4hKQV6ogXHEgN_pHPQ_zxFu1FJyBPtbtMsmGERwXD8MHOC2qQ9jlwFJUxwW_RlQ1v7Mw5yYLul_hkJ4JuQcd0ptVInDxXiI6b-Iy0i3zTvD10E9KlWaHglp9JNAVkXGqV9MdxziSuSzc7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33c24605de.mp4?token=t7N4VeR5DcmgiyzNWxn8xZF4LOid5s0nQ_ZIaHg7aH1fMwefpy3uvTcNAoF5RIJ2xOg1DO_bCLaUPpAFmDSpIYdqetkbQAezCAuOSa7yGZSfgMOvntFWRpNCufvhesY6l63ldu2ujIPRjsUjU3Jq_Rovy2DkmSJLHzXHaz1YdUUbXRm7KHJ6uEIkxjP6txzY2caSilqmmFl73TCqxLkrP7pFjqxy76MgngrL4TBEAL5OdRqJbt7N9g4xHTK7NkDPBRkppOBuCx-J9uG7CipT0fq84eq1LW00BFw863B7Zw4PWYFsfJx5p87549jUxJptlwJXiNnAFQIeCGGvs9ePow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33c24605de.mp4?token=t7N4VeR5DcmgiyzNWxn8xZF4LOid5s0nQ_ZIaHg7aH1fMwefpy3uvTcNAoF5RIJ2xOg1DO_bCLaUPpAFmDSpIYdqetkbQAezCAuOSa7yGZSfgMOvntFWRpNCufvhesY6l63ldu2ujIPRjsUjU3Jq_Rovy2DkmSJLHzXHaz1YdUUbXRm7KHJ6uEIkxjP6txzY2caSilqmmFl73TCqxLkrP7pFjqxy76MgngrL4TBEAL5OdRqJbt7N9g4xHTK7NkDPBRkppOBuCx-J9uG7CipT0fq84eq1LW00BFw863B7Zw4PWYFsfJx5p87549jUxJptlwJXiNnAFQIeCGGvs9ePow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر املاک توقیف‌شده خبرنگار اینترنشنال منتشر شد
🔹
مستندات املاک شناسایی‌شده فیروزه جابانی خبرنگار رسانه صهیونیستی فارسی‌زبان اینترنشنال که با دستور قضایی به نفع مردم توقیف شده است، منتشر شد.
🔹
مرکز رسانه قوه قضاییه: برخی افرادی که در همکاری با دولت‌های متخاصم موجبات ایجاد خسارات گسترده‌ای به کشور شده بودند با انجام اقداماتی سعی در اختفای املاک خود داشتند که با کار پیچیده حقوقی و اطلاعاتی و تلاش‎های سازمان ثبت اسناد و املاک کشور، در حال شناسایی است.
🔹
یکی از این خائنان به وطن که با حضور در شبکه اسرائیلی ایران‌اینترنشنال، در راستای اهداف دشمن صهیونی در تجاوز به کشور نقش فعال داشته ، فیروزه جابانی است.
🔹
با پیگیری‌ها و استعلامات صورت‌گرفته، دو واحد از یک آپارتمان درحال ساخت متعلق به خبرنگار اینترنشنال که تلاش برای اخفای آن کرده بود، شناسایی و به دستور قضایی به نفع مردم توقیف شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/akhbarefori/651905" target="_blank">📅 11:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651904">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34e4e31ae6.mp4?token=tdrPaJPZ5uPQ7OjUrCuCSkagmYnf2h2_IRPgBFJ1N9wwHWp6JKbDessnYuNqbr8MSD_W4YY5HAGG8WZDJ77lizfIevtccpi4UNq00I85NqfWAgfP-YDJmn7HuYVfRxTO2jc7twrzpgj3M9pwdsEHES5ScMDOa5W1vu_Dz_wnDvTM8LskGiswl39GO7ruRlIjEVmbkqn7eOSYyc3L6FkRrjzlN48vmmO1Ntk6HOe7L6y5tXswqO7nh-grUL7u_uAe_HOlVfurtXF5-5iMl9qEfdvBanWnZ55EwkOef2mblL1izbuK6IeGAv7IcmfB3-t7-KrjmqJp0Ya5Lo9EdqUc8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34e4e31ae6.mp4?token=tdrPaJPZ5uPQ7OjUrCuCSkagmYnf2h2_IRPgBFJ1N9wwHWp6JKbDessnYuNqbr8MSD_W4YY5HAGG8WZDJ77lizfIevtccpi4UNq00I85NqfWAgfP-YDJmn7HuYVfRxTO2jc7twrzpgj3M9pwdsEHES5ScMDOa5W1vu_Dz_wnDvTM8LskGiswl39GO7ruRlIjEVmbkqn7eOSYyc3L6FkRrjzlN48vmmO1Ntk6HOe7L6y5tXswqO7nh-grUL7u_uAe_HOlVfurtXF5-5iMl9qEfdvBanWnZ55EwkOef2mblL1izbuK6IeGAv7IcmfB3-t7-KrjmqJp0Ya5Lo9EdqUc8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احتمال انتقال سهمیه سوخت به کارت بانکی؛ مجلس دولت را مکلف کرد
🔹
نواز سخنگوی صنف جایگاه‌داران سوخت: انتقال سهمیه کار به کارت بانکی بارها مصوب شده و امسال نیز مجلس دولت را مکلف به اجرای آن کرده است. امید می‌رود این طرح بزودی اجرایی شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/akhbarefori/651904" target="_blank">📅 11:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651903">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsCz4KipmZ6I0sAkeAp5qhLG1EzsDqoHAgTGO0doZvxASwBJNnvp6ccd-EgqNX6L39-eZc0bxkxZ5AE4JjyiDVMkm8FA-zZzFj5z4dq8VoRoT5BL929dzCCQZVVKHdjLCeOvQAVqUWhvYD5KzJFbsSxatl1404v7LCWbGLJ361IzHnvHE7VLYCSnOMOxQGB0yjjLAVM1t0ZpE2xgde7-8ORVikPA1FwRQ_MNPK8DnD7QWSrZxnKfICGVqs9lKdmkdV6UTyeQnm7e3S6ZFvct3S25jDUFcGXtShZtbuMiDgYxsLhsjF2TY7PKiWTEfKCZgLDG1lAMX7XSFK6rT2Ef_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«ماندن به وقت جنگ»؛ روایتی از ۴۰ روز ایستادگی کادر سلامت در جزیره خارگ
🔹
در روز‌هایی که جزیره خارگ زیر شدیدترین حملات جنگ ۴۰ روزه تحمیلی قرار داشت و بسیاری از خانواده‌ها برای حفظ جان خود جزیره را ترک می‌کردند، نیرو‌های بهداشت و درمان همچنان در کنار مردم ماندند تا آرامش و خدمات درمانی قطع نشود.
🔹
«فهیمه زمانی» سرپرست مرکز با وجود فرزندان ۶ و ۸ ساله خارگ را که از بچگی در آن بزرگ شده بود را ترک نکرد، «زهرا کشوریان» بهیار مرکز با دو کودک خردسال یک و سه ساله روز که اول جنگ آنها را به بیرون از جزیره فرستاد و «سیروس حقیقی فرد» از کارکنان حراست مرکز که حدود ۳ ماه بود فرزند تازه متولد شده اش را ندیده بود، تصمیم گرفتند محل خدمتشان را ترک نکنند و در روز‌های جنگ در کنار مردم جزیره بمانند.
🔹
شب‌های بمباران، اضطراب مردم و ماندن در جزیره.
🔹
بهیار مرکز: کودکان خردسالم را همان روز اول جنگ به خارج از جزیره فرستادم.
🔹
نیروی حراست مرکز: فرزند پنج‌ماهه‌ام را سه ماه ندیدم؛ اما خارک را ترک نکردم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/akhbarefori/651903" target="_blank">📅 11:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651902">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6254b500db.mp4?token=Uy4PZ3xujuSFQoZP0wYE-ddk7DMvXVftq_o7gxJyV3feE4Cb5wylfjpGm5MXBxbN4BymmEFpiDcHszR3VYt9v3mARkPFyL9i3AsnjP0A2eglzpSqlWjz4zkJMnMEcA5bmdvmJsFmaHr8v1f7jtkGo5POqKaCq1sgfcSNBOxCkKeuxSER4ZVnumxU_NF0zvOSj7dH-rSS_Bz5VOsmzTgwKv42klVz34fq279h2hhzuQ6MZMlmIghprGi6pZbRmMux45NOB8i_9RB0rPSloYbSwDO5WnV9dvNP6nYqCsh_9pIqLsZiD3OyNbgqre-6-1BJYwN1R90Hj1YBcTlHf1rVtkAhIptQZnIbykODyioO3_gitm8xnRp2yZ73nESXK1vFmv8G3oxcI7xGZbjZUC7w2wOF925DSGs_-IzA_odrW2XhCmKQVNX_7AgZhCyogNCvRyDKPXtV0gA5hr6oOB2FMYOoJJQX91Ik6PQwYJQXWZV6x3MvgzsQvkXRVFAz_WuJtiAcPksfJf7gLV_Fs-o08Em8lcGXa0RSXBTDkSkxQwzltUub3Gj4AhZ9KxQfMsEVZD6XJCEoAyQZ8YKykV3__r8pRsNQv9Ue3nW5xP0RF-ivhSzJXJDaSGN3AvJwWIVK4J9vCmQ8Y0plGGK6YuYab_lqbXPJ6XMoBzgy6KbRX4M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6254b500db.mp4?token=Uy4PZ3xujuSFQoZP0wYE-ddk7DMvXVftq_o7gxJyV3feE4Cb5wylfjpGm5MXBxbN4BymmEFpiDcHszR3VYt9v3mARkPFyL9i3AsnjP0A2eglzpSqlWjz4zkJMnMEcA5bmdvmJsFmaHr8v1f7jtkGo5POqKaCq1sgfcSNBOxCkKeuxSER4ZVnumxU_NF0zvOSj7dH-rSS_Bz5VOsmzTgwKv42klVz34fq279h2hhzuQ6MZMlmIghprGi6pZbRmMux45NOB8i_9RB0rPSloYbSwDO5WnV9dvNP6nYqCsh_9pIqLsZiD3OyNbgqre-6-1BJYwN1R90Hj1YBcTlHf1rVtkAhIptQZnIbykODyioO3_gitm8xnRp2yZ73nESXK1vFmv8G3oxcI7xGZbjZUC7w2wOF925DSGs_-IzA_odrW2XhCmKQVNX_7AgZhCyogNCvRyDKPXtV0gA5hr6oOB2FMYOoJJQX91Ik6PQwYJQXWZV6x3MvgzsQvkXRVFAz_WuJtiAcPksfJf7gLV_Fs-o08Em8lcGXa0RSXBTDkSkxQwzltUub3Gj4AhZ9KxQfMsEVZD6XJCEoAyQZ8YKykV3__r8pRsNQv9Ue3nW5xP0RF-ivhSzJXJDaSGN3AvJwWIVK4J9vCmQ8Y0plGGK6YuYab_lqbXPJ6XMoBzgy6KbRX4M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: دشمن در سال ۱۴۰۴ بیش از ۱۰ هزار ایرانی را به شهادت رساند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/akhbarefori/651902" target="_blank">📅 11:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651900">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe01028607.mp4?token=tt0D-gCADxchKAQ8FFAEvu5Oo23Dcdn3GlYBG5NLQTSUgN6cvm51NS45cXjv_moCVRS8MbcrnBDOjlwMhdFWoaE6Kxf2vWS-PuEqW3SqhPuiI1_7oiCuVKuzBeVexC4uXweJ5jYMhEIdHCUnL0S1aB_u8OhDPVuaAY4kcenCPkW8WYrLxaA7-3cD56TFp84HUMKILmqhJ_TjtFBCKCVyCJwGnc1wsQfp5d1nUiI90L0c5_sPkG30Oa1cKIPjPvclrF1ofvo7cVF3OGbCoX0z93SlC-PaaakuNCc4v24mrSfo96x_JRrSNLR_VfDhS_8EM6Vb_2wfcfhHGTC_W8mCFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe01028607.mp4?token=tt0D-gCADxchKAQ8FFAEvu5Oo23Dcdn3GlYBG5NLQTSUgN6cvm51NS45cXjv_moCVRS8MbcrnBDOjlwMhdFWoaE6Kxf2vWS-PuEqW3SqhPuiI1_7oiCuVKuzBeVexC4uXweJ5jYMhEIdHCUnL0S1aB_u8OhDPVuaAY4kcenCPkW8WYrLxaA7-3cD56TFp84HUMKILmqhJ_TjtFBCKCVyCJwGnc1wsQfp5d1nUiI90L0c5_sPkG30Oa1cKIPjPvclrF1ofvo7cVF3OGbCoX0z93SlC-PaaakuNCc4v24mrSfo96x_JRrSNLR_VfDhS_8EM6Vb_2wfcfhHGTC_W8mCFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهاجرانی: فشار اقتصادی ناشی از تحریم‌ها حق مردم را ضایع کرده است
🔹
سخنگوی دولت: فشارهای اقتصادی ناشی از تحریم‌ها بر مردم تأثیر منفی گذاشته و دولت در تلاش است با پرداخت کالا برگ، افزایش حقوق‌ها و حمایت از تولید، وضعیت را بهبود بخشد. بیکاری یکی از عوامل اصلی افزایش تورم است و حفظ اشتغال پایدار ضروری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/651900" target="_blank">📅 11:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651899">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHMCyLE-sLZknGc6WbHNoRDikzvXKwXAjuNJxyuKhGrB7VRbbv4KcrnvIfQI4uS-zFFbXL26IsuMS_T0keA09a8HXObzs8tTzzwfnamvRP6HhiCGwGTf2OLqcwUXh_LyQJgM2AIfLvMzHp-2k5ukjO8ykIylhnqCyj4UVsCrlSFO-ISDnpU0YBcLRFG-_Q3euDUEpVsjGbDQSiCaxalrypbFH7nfLcfThLvzEDwS4UxBuQi8Afmi1G3o6rkt5OCMaCpxmaolLxjn-NJSNVb7mWoMx1Lf2GX2lU2fHVCZt4H1dDEg-1ITyVumcfWVb-WAFHjSjDulHdrY5tJYxp_HFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعایی درباره ساخت یک پایگاه توسط اسرائیل در عراق!
وال‌استریت‌ژورنال:
🔹
اسرائیل پیش از جنگ، با اطلاع آمریکا، پایگاهی مخفی در عراق برای پشتیبانی از عملیات علیه ایران ایجاد کرده بود؛ پایگاهی که پس از شناسایی توسط نیروهای عراقی، هدف حملات هوایی اسرائیل قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/akhbarefori/651899" target="_blank">📅 11:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651898">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsA8-hrfUr8C7XXZIevRd9IWvP_39kObBQ7ucvKo99_3d3WUbT6wLwO_KaIS3Qpy18XFyGwnlqpcXPDpXKMKMM73nBQ3lnLn_d1GY4Wm2adeTGlCcOzVx0zdMKjlp4MKqvsMFilCs1CmMPVqfEo-xoZHWMYaVSJ3PF15T2SA03PAhFTo2TNIxr27SDjB7vIQw65VLPTdT9n8gcVpqhya995BFJE6800WTPdV1r_yQP6FLHM0ThiOtMyz0eUTbNHpDCoYUAaHyfXND2tywsviL7v8G34A-28IfsNq0i-ocOT9khRkBGU-p6FCV-uYw3MS8bM6aDABA4x0yLjrs71p3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در ایام جنگ مردم بیشتر چه چیزی می‌خریدند؟
🔹
آمار یک فروشگاه اینترنتی نشان می‌دهد با نزدیک شدن تنش‌های جنگی، تعداد سفارش‌ها و ارزش سبد خرید افزایش یافته است.
🔹
تقاضا برای کالاهای ماندگار مثل آب معدنی، روغن و کنسرو بالا رفته و فروش تنقلات کاهش یافته؛ در عین حال فروش شمع ۸۶٪، کبریت ۳۹٪ و باتری ۲۶٪ رشد داشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/akhbarefori/651898" target="_blank">📅 11:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651897">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1GqwQmbBdLeL5hh12XXcGE3Z8KEfddgESRF2YOu-CPPxg5IBqR1O8690DE5VSNCkRLw_G8J9QUFCUPmtw9XVE_UutmzYC58u4_nm6eM3d0OVgDZS3bNrlmJQS6_H7D4Q3WATz9Ow01ysptXMdHhJUg0x_pfQHmthi1kyvZT7-A7fU5fveUgfd-h5k-r3tK6Su767kKMWTvcVj2vxHXu31lK1vi0iQZol5jQ0_j69FDJ00lC8yRAvDu7-mVYNhQYVwNdUM0Q5Zdzxmoa_d7ggYeYY1UrIe1witDw18w7egPGXkSIo1mZtQAH3VidMRTv_CLyFIXVUEfHt_XXxotX1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رپیس جمهور: اجازه سوءاستفاده از شرایط جنگی و فشار بر معیشت مردم را نمی دهیم
🔹
پزشکیان  در نشست بررسی الگوی مشارکت اصناف در فرآیند تولید، توزیع و تنظیم بازار: کنترل تقاضای القایی و مدیریت مصرف از سیاست‌های اساسی دولت است. صادرات ارزآور و دیپلماسی اقتصادی، به منظور تقویت تاب‌آوری اقتصاد کشور با جدیت پیگیری شود. یکی از سیاست‌های اساسی دولت در شرایط فعلی «کنترل مصرف و جلوگیری از شکل‌گیری تقاضای القایی و کاذب» است. ایجاد تقاضای غیرواقعی بدون تأمین متناسب کالا، منجر به نارضایتی عمومی و برهم‌خوردن تعادل بازار خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/akhbarefori/651897" target="_blank">📅 11:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651896">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f65082375b.mp4?token=KuVcA29l5M69oEDgFnkwJDNdkPzcR9xgsWhbUF8fC4AsbMagZp_KlBLikOG082VZ2Xb8omFhZXSthvV9QiXsdo6kyx5WlRRZA0XNq76C1eESNOk50q5SH33GcAP63h6xNqiIm990Vd9747iXJ9xuyRxBxvBDNtlqntV1AglYR2gi-f_YSTSkm_l9bSHxWtTcELGSxs5sIiuUBT_xgpgnUaUJo5gWdf_aeW2GYIES0la8cIP5ovXTTPysNZL9F2FE6gXf1fLzBjLK8uG6EnnSA8-g0LnozShoj2qMclzOYYje3Y2ScPnbY8d84xzRndTi9ynPBjYTStZFE2gVNVzDXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f65082375b.mp4?token=KuVcA29l5M69oEDgFnkwJDNdkPzcR9xgsWhbUF8fC4AsbMagZp_KlBLikOG082VZ2Xb8omFhZXSthvV9QiXsdo6kyx5WlRRZA0XNq76C1eESNOk50q5SH33GcAP63h6xNqiIm990Vd9747iXJ9xuyRxBxvBDNtlqntV1AglYR2gi-f_YSTSkm_l9bSHxWtTcELGSxs5sIiuUBT_xgpgnUaUJo5gWdf_aeW2GYIES0la8cIP5ovXTTPysNZL9F2FE6gXf1fLzBjLK8uG6EnnSA8-g0LnozShoj2qMclzOYYje3Y2ScPnbY8d84xzRndTi9ynPBjYTStZFE2gVNVzDXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهاجرانی: اعتراضات دی ماه حق مردم بود، اما تروریست‌ها آن را مصادره کردند
🔹
سخنگوی دولت با تأکید بر حقانیت اعتراضات دی ماه مردم، گفت: متأسفانه این اعتراضات توسط تروریست‌ها مصادره شد و منجر به شهادت بیش از ۳۰۰۰ نفر از هموطنانمان شد.
🔹
دولت در راستای حفظ سلامت مردم و رفع مشکلات اقتصادی، تصمیمات جدی از جمله حذف ارز ترجیحی را اتخاذ کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/akhbarefori/651896" target="_blank">📅 11:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651895">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGgchA9rT9w-8sWIjMJxfyBdVSiUj1OF1dHgs3lPQrDt2KhT9rsoIMhboQoFcaezLEIp3t7czLY6lDvqyif3aXYZiVWwYDI1Qux31-rRA4UuIAWjiy8Y4Y8hru11oO8X40PRiHg5XTMVlFiVkNUQRRAOD1EoyTisfmU8U99YSlLER3S001XRZMEjcpmj6CCqvABeYVtwG4ejJRpL7gBW-fO2ZUX1-k1wLaYgJwT1rQOz_c-4xaR-pJdfXnrv4vZO1zwChqjWvJh8B1sTlTnqbsKXuohb6-8boTTtMo_t-jjvQeCm9FrgjctoEKcXGntd99LZDJLIOIS_kh293w9X3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
متوسل شدن ارتش اسرائیل به تورهای ماهیگیری برای مقابله با پهپادهای حزب‌الله!
🔹
روزنامه عبری هاآرتص اعلام کرد که ارتش رژیم اشغالگر برای حفاظت از نظامیان خود در برابر پهپادهای مقاومت لبنان، به ابزارهای ابتدایی مانند تورهای ماهیگیری متوسل شده است؛ آن هم در شرایطی که از پیدا کردن راه‌حل‌های فناورانه ناتوان مانده است.
🔹
یک مقام ارشد در ساختار ذخیره نیروهای زمینی در مصاحبه با این روزنامه گفته است که به‌دلیل سیاست‌های نتانیاهو و ترامپ، «ارتش دست‌بسته مانده است» و در حال حاضر فعالیت موجود تنها به تخریب روستاها توسط پیمانکاران خصوصی محدود شده است. این مقام نظامی نسبت به کمبود شدید شمار سربازان و افسران هشدار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/akhbarefori/651895" target="_blank">📅 11:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651894">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3valQuxlodIyFX2fJ8y7RTDXj-38gCBVCJXROwCFWSCprv1PuLFJJgTQtINIUYxpSSOsiaj6dXaIld2NtQsIAyaWlICezTFduDBUMg4nYlqlnOy0IQdOXok2rIWP2HgIr5-9FHtE9kimcs8kWS-IxftG1vDxIvEIXSrcNeHpa3anHvZcRNdYO1QVJBuQWgknIa-fwY1a41kwAIFyO1VCjgqCO3RqhPzm0bfadoDc2Qxi87lp6U0K7Q3K7UuUmpzSQpop5YcjOwdnqfMUtagXJvPALSFK-l87GTn1-1eZxob4FUbBMOvSMF7FMlOrL4_h44kFMXacHjf1UWhxhSBJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خارج شدن موضوع هسته‌ای از اولویت مذاکرات ایران و آمریکا
🔹
در شرایطی که در گذشته، تلاش آمریکا برای محدود کردن برنامه هسته‌ای ایران اولویت مذاکرات بود، سفیر پاکستان اعلام کرد که بازگشایی تنگه هرمز مهمترین موضوع مذاکرات کنونی با تهران است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/akhbarefori/651894" target="_blank">📅 11:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651893">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVzAsAn9rCZOL1XE-94MPrnl7-OkL7zZ0SxUmqkBgpOfmAKvW0bTt5uorJYO4hpTZQrlEvui15qAdSlcfwvZOTD3cv5XOk4Uqse5uyBnbL6_BwvPHdKkIK0_WFpGU5OR0E53uZWze410P9AX3lo9HJZVaZukTwCNtEnomDTGMbpmiAfFUYh08ByLHySyVQPTf0JZyINELwuhfDUeG2RwTC9Yfv0pKsufXW3z88XhfUo8XEVe8Iti7XbLKEfyCVp3_vQRwfMj7uA9RbVxDHLLsYlGWt02_l7FOyj94vr1yk6VGu0qut_Cal3HcANFz6Nh7P6BpxgFR6Zy89ggJwfaWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارسال پیامک‌های تهدیدآمیز منتسب به ایران به شهروندان اسرائیلی
🔹
منابع اسرائیلی از یک حمله سایبری گسترده به اسرائیل، شامل ارسال پیامک‌های تهدید آمیز از سوی ایران، به شهروندان اراضی اشغالی خبر دادند.
🔹
طبق تصاویری که از این پیام در شبکه‌های اجتماعی منتشر شده است، در این پیامک آمده، «به شما قول داده بودیم که به زودی ستاره‌هایی را در آسمان شب خواهید دید که ستاره نیستند... به زودی خورشید را در آسمان شب خواهید دید، اما...» کاربران معتقدند که خورشید در آسمان شب اشاره به حملات موشکی و پهپادی ایران دارد.
🔹
براساس این گزارش، سازمان ملی سایبر اعلام کرده که در ساعات اخیر یک «حمله ادراکی» (جنگ روانی) گسترده شامل پیامک‌های تهدیدآمیز را شناسایی کرده است که تنها یک هدف دارند: برهم زدن آرامش روانی جمعی و ایجاد حس تعقیب دیجیتال. در تهران ظاهراً فکر می‌کنند اکنون زمان مناسبی برای برقراری یک رابطه نزدیک با شهروندان اسرائیلی است، حتی اگر این رابطه بر پایه تهدیدهای کلی باشد که از سیستم‌های ارسال انبوه فرستاده شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/akhbarefori/651893" target="_blank">📅 11:17 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651892">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6672cf69a8.mp4?token=lqLI1sezxdW-WA9ilvSpfvmj1SOmZ-IPVusb9Mh7EfjO5qEB9wrzqbmF86z-9zUiANffIOMA0hjxkoQ9bWlhbvayl5zrswcD7bQl9HWC0AgnedwpQlqO7fRfS-VOMcJMHqW11MdlM4L0_U2SwH9ata62tMYXuj2Ig5jFABF8OI0zyPVKAgOHvQK9NySFapQqdgfZJwkJYDExtS3WgdG9QQFhtq08vi0j7u21aiboEIp7wlyRADSGleWx9WEKtS3PXcXGhEnQFGfDA9s8vdO1MXqoN-5axWO2X_YTv3CkO03BeHN75_2Pw4hIylKb2Xsg4aT7KJfrt8x0QLFCWc3lgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6672cf69a8.mp4?token=lqLI1sezxdW-WA9ilvSpfvmj1SOmZ-IPVusb9Mh7EfjO5qEB9wrzqbmF86z-9zUiANffIOMA0hjxkoQ9bWlhbvayl5zrswcD7bQl9HWC0AgnedwpQlqO7fRfS-VOMcJMHqW11MdlM4L0_U2SwH9ata62tMYXuj2Ig5jFABF8OI0zyPVKAgOHvQK9NySFapQqdgfZJwkJYDExtS3WgdG9QQFhtq08vi0j7u21aiboEIp7wlyRADSGleWx9WEKtS3PXcXGhEnQFGfDA9s8vdO1MXqoN-5axWO2X_YTv3CkO03BeHN75_2Pw4hIylKb2Xsg4aT7KJfrt8x0QLFCWc3lgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: گزارش‌ گرانی ها به دقت به مسئولان می‌رسد
🔹
مهاجرانی در نشست خبری: افزایش قیمت‌ها در دو سطح بررسی می‌شود: کلان و خرد. دولت به دنبال کنترل تورم و مهار رشد نقدینگی است. گزارش‌ها به دقت به مسئولان می‌رسد و سیاست‌های حمایتی برای مدیریت معیشت مردم اجرا می‌شود. همچنین، توجه به تفکیک گرانی از گران‌فروشی و استفاده از نگاه‌های ارشادی مورد تأکید است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/akhbarefori/651892" target="_blank">📅 11:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651891">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سردار ‌جعفری؛ فرمانده قرارگاه بقیه الله (عج): تصمیم نظام در این شرایط حساس، همان پیش‌شرط‌های اساسی ۵‌گانه برای ورود به هر نوع مذاکره احتمالی است. یعنی تا زمانی که جنگ در همه جبهه‌ها پایان نیافته، تحریم‌ها برداشته نشده، پول‌های بلوکه‌شده آزاد نگشته، خسارت‌های ناشی از جنگ جبران نشده و حق حاکمیت ایران بر تنگه هرمز به رسمیت شناخته نشده باشد، هیچ مذاکره دیگری در کار نیست. این مطالبه مردم از تیم مذاکره‌کننده و پیام ملت ایران به دولت آمریکاست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/akhbarefori/651891" target="_blank">📅 11:01 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651890">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3875703205.mp4?token=ZW_WwHV5LgGgzmpa664wM20QdRGkOGvLJD7BewJchkmC1jpbNdXP7hsII_k_zaPbzsIpY4-r8cjyynY39hilrQqE6M1OeS1Xvwzz6nU1XUR2BAsincyJOU2ORTPIjYSKyyZxVa8wryYbec4nOcwofa_EjlQL6GfXoiD6e-ZGya3wNhU5eOcxuVy1-7V30Ta5FueqMzKlWx-ON2L1M1Ugu_8eWs99srqZ09-layIR9bemrBYQL73MNRVaCxyFmPKN_aPaWNztmiDR_jo9xj3xSZelArRzKw7vhJEJFOa3MmjDnE9fllVwZV72I_ukr2ginNv7Ey-eFvyTiw78iJ4Kqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3875703205.mp4?token=ZW_WwHV5LgGgzmpa664wM20QdRGkOGvLJD7BewJchkmC1jpbNdXP7hsII_k_zaPbzsIpY4-r8cjyynY39hilrQqE6M1OeS1Xvwzz6nU1XUR2BAsincyJOU2ORTPIjYSKyyZxVa8wryYbec4nOcwofa_EjlQL6GfXoiD6e-ZGya3wNhU5eOcxuVy1-7V30Ta5FueqMzKlWx-ON2L1M1Ugu_8eWs99srqZ09-layIR9bemrBYQL73MNRVaCxyFmPKN_aPaWNztmiDR_jo9xj3xSZelArRzKw7vhJEJFOa3MmjDnE9fllVwZV72I_ukr2ginNv7Ey-eFvyTiw78iJ4Kqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: انسجام ملی با پاسخگویی دولت و رفع حس تبعیض تقویت می‌شود
🔹
از مردم که بیش از ۷۵ شب خیابان را زنده و پر نگه داشتند قدردانی می‌کنم؛ این حضور امروز به یکی از اضلاع قدرت کشور در مذاکرات تبدیل شده و باید به‌عنوان شکل نوینی از مشارکت مورد توجه قرار گیرد.
🔹
برای حفظ انسجام ملی، دولت باید عملکرد مناسب و پاسخگو داشته باشد و به‌ویژه در حوزه معیشت، حفظ اشتغال و ثبات اقتصادی برنامه‌ریزی و پیگیری کند.
🔹
جلوگیری از شکل‌گیری حس تبعیض، تقویت نظارت مردمی از طریق سامانه «فؤاد»، به رسمیت شناختن احزاب و گفت‌وگو با نسل‌های مختلف نیز از محورهای مهم استمرار همبستگی ملی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/akhbarefori/651890" target="_blank">📅 11:01 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651889">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f77d4cec5.mp4?token=SYW-90RW-UNXd_O_6uuqTskwyEYxZg9w_adT1tZL9FKKSAMg_tupJ7sA6RqOfRG8Vbnm7L5L92skMWWu4yK_2QrveTb8mglLjWC2KIaOcUFLn9j6mQ7vePNbkx-3aBg4ACwaiBBGzCyEXoWx3llOYlZ0FJkOjpc95bq1hG9VUtPZZJ0ur7CN-HSBVy5qc4bVCNcIOCaxv5qKQdkOaYyvte1RdPzx7NFdtcPsBQ7yZmQkygnvdvs2ygubw_6j20A3dXu5zNtw1n0lBX1bxZzzUKxQcijDYTNi3YZt0Oi4rNOkNbcudth46-kMq5CFneFqG3sy5K3S2k_wuIj8f1lRrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f77d4cec5.mp4?token=SYW-90RW-UNXd_O_6uuqTskwyEYxZg9w_adT1tZL9FKKSAMg_tupJ7sA6RqOfRG8Vbnm7L5L92skMWWu4yK_2QrveTb8mglLjWC2KIaOcUFLn9j6mQ7vePNbkx-3aBg4ACwaiBBGzCyEXoWx3llOYlZ0FJkOjpc95bq1hG9VUtPZZJ0ur7CN-HSBVy5qc4bVCNcIOCaxv5qKQdkOaYyvte1RdPzx7NFdtcPsBQ7yZmQkygnvdvs2ygubw_6j20A3dXu5zNtw1n0lBX1bxZzzUKxQcijDYTNi3YZt0Oi4rNOkNbcudth46-kMq5CFneFqG3sy5K3S2k_wuIj8f1lRrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: کشور در جنگ است؛ بپذیریم که ویژگی جنگ امنیت مردم است
🔹
طبیعتاً رئیس‌جمهور، رئیس شعام هستند. بدیهی است که امضای ایشان برای همه ما معنادار دارد. تأکید می‌کنم که پیگیر حقوق مردم هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/akhbarefori/651889" target="_blank">📅 10:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651888">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/014db93225.mp4?token=viil-08vPRK2yhAbLbRSkkaYwFs21ezMKJ_PF3goFB3ImH7HR_MMQMe-3si4lg1ySG7YYuKBkMffKccNrzplMpMPK1xncBYLvQtALd1M3n2cljSNEL5mbpO89xHA-jRAeKXmb9GSVc-cRW_-trZXDO1oL9pp9EbzKV9DcoUjzyeVCpYycKOnfk1tosoEs2WqBHX9MJRSpIyL-5LxB3ihQUyktMJPkG-xGJM3woTSUYLiy-RHNEMjQa7QfAtZfeQbHDa_I9Xc4S95qdRwtGY33e8pnqDBdkS01fLLj1jtDa5YK8s_axYqzEgOYoOL-4Wk53QfGqinmh6ypL-Fd9C-xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/014db93225.mp4?token=viil-08vPRK2yhAbLbRSkkaYwFs21ezMKJ_PF3goFB3ImH7HR_MMQMe-3si4lg1ySG7YYuKBkMffKccNrzplMpMPK1xncBYLvQtALd1M3n2cljSNEL5mbpO89xHA-jRAeKXmb9GSVc-cRW_-trZXDO1oL9pp9EbzKV9DcoUjzyeVCpYycKOnfk1tosoEs2WqBHX9MJRSpIyL-5LxB3ihQUyktMJPkG-xGJM3woTSUYLiy-RHNEMjQa7QfAtZfeQbHDa_I9Xc4S95qdRwtGY33e8pnqDBdkS01fLLj1jtDa5YK8s_axYqzEgOYoOL-4Wk53QfGqinmh6ypL-Fd9C-xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: پس از دور شدن سایه جنگ وضعیت اینترنت به تدریج به حالت عادی تغییر می کند
🔹
اینترنت پرو مصوبه شورای عالی امنیت ملی را دارد که آقای رئیس‌جمهور رئیس آن هستند
🔹
آقای رئیس‌جمهور پیگیر حقوق مردم هستند و طبیعتاً پس از رفع مشکلات و پس از دور شدن سایه جنگ از کشورمان، وضعیت به تدریج به حالت عادی تغییر خواهد یافت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/akhbarefori/651888" target="_blank">📅 10:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651887">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2lnRMQ89xPRV7rXUe_2wPaKgaQUZeAkEc-NN9W3puAQRSjFG7kKCtWN4hxhpZpNOAzI8t9R9hdmQLSIAhyOhCAGfcjahYkWR7mrizm_RugMeEOnYvciQRpDDC0hoz3_0hb7Bawk211ZP5544Ni2a32uyzwIGiq4AGrqA06QnRtorYJQq94zFJk0vJ2uZMQ6WU911iFefx__BUWrQEKX5Eo-7fpTHQBZx-B1CiXLkBClTM4UgVEtmnQ1ISKkQ72Revs48LL_FjCqvCFd3-evvTK5yXKoAOzpfuxuM9mFQa_RMfmMioUctyxKIJMUBcvX0DWRvp3UPQ33Wq-YBTTmag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس قوه قضاییه: اگر خط سفید و اینترنت پرو موضوع درستی است آن را تبیین کنیم؛ اگر تخلف است برخورد قانونی شود
🔹
حجت‌الاسلام والمسلمین محسنی اژه‌ای: ما در قوه قضاییه پاسدار حقوق عامه مردم هستیم و به هیچ وجه، اجازه نخواهیم داد این احساس در مردم ایجاد شود که در جامعه ما، تبعیض حکمفرماست.
🔹
قضیه‌ی موسوم به خط‌های سفید و اینترنت‌پرو، در ذهن مردم مسئله ایجاد کرده است؛ این ذهنیت نیز یک شبه بوجود نیامده و اگر در باب آن برای مردم شفاف‌سازی نکنیم، موجبات بدبینی شهروندان فراهم می‌شود.
🔹
بارها اعلام کرده‌ایم که کسی تصور نکند چون شرایط جنگی است و اقتضائات خاصی حکمفرماست، می‌توان قانون را دور زد و یا عملی مغایر با قانون و شرع مرتکب شد و یا سوء‌استفاده‌ای از شرایط موجود کرد
🔹
در همین قضیه‌ی موسوم به خط‌های سفید و اینترنت‌پرو، گزارش‌هایی واصل می‌شود که فلان فرد با دریافت مبالغی هنگفت این خط یا خطوط را واگذار کرده است! توجه کنید که این قبیل مسائل بعضاً به حاکمیت نسبت داده می‌شود و سبب بدبینی، بی‌اعتمادی و شکل‌گیری احساس تبعیض در مردم می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/akhbarefori/651887" target="_blank">📅 10:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651886">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
معاون نیروی دریایی سپاه: تحرکات را با دقت زیرنظر داریم
🔹
در یکی از موارد اخیر، یک ناوچه آمریکایی قصد عبور از محدودهٔ تنگهٔ هرمز را داشت که با رصد دقیق نیروهای مسلح مواجه شد و پس از مشاهدهٔ برخی رفتارهای تحریک‌آمیز، نیروی دریایی ارتش با شلیک‌های هشداردهنده و هدفمند، پیام لازم را منتقل کرد و این شناور نیز بلافاصله مسیر خود را تغییر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/akhbarefori/651886" target="_blank">📅 10:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651885">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
خبرنگار الجزیره: حمله هوایی اسرائیل به شهر راس العین در شهرستان صور در جنوب لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/akhbarefori/651885" target="_blank">📅 10:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651884">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/331c298d8b.mp4?token=Q2opuQll5zWSB7Uw8vtqEMwgOGW2hYEOo_KJNNiO6jjplQazSUnrcedgAxK9u23MreSBeTLhjsNMSXGWJqz4YexNWKuju2q6z038K7uvjbPfaVq-ciCr-YXid7hTqUbMo-Vs4aJfdpSu18mnCfOUPtgs65l-K4ZMkrWqcW2vSt44VhC9LrtvTcjXUkLkZy7YLRZXy-0xDizTutgq-Cqa7wOOPBGQf8AHEf5fDmSHWasKGs0ptdJvgp-9288m7r6FrxPpW5V03Q56qBKYiehG33eX0tETAP6cr6mfXdDI1C0apkU3pb3TaGBVhRxTfOj5wMBgwuiU2V7_w9R72F8XGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/331c298d8b.mp4?token=Q2opuQll5zWSB7Uw8vtqEMwgOGW2hYEOo_KJNNiO6jjplQazSUnrcedgAxK9u23MreSBeTLhjsNMSXGWJqz4YexNWKuju2q6z038K7uvjbPfaVq-ciCr-YXid7hTqUbMo-Vs4aJfdpSu18mnCfOUPtgs65l-K4ZMkrWqcW2vSt44VhC9LrtvTcjXUkLkZy7YLRZXy-0xDizTutgq-Cqa7wOOPBGQf8AHEf5fDmSHWasKGs0ptdJvgp-9288m7r6FrxPpW5V03Q56qBKYiehG33eX0tETAP6cr6mfXdDI1C0apkU3pb3TaGBVhRxTfOj5wMBgwuiU2V7_w9R72F8XGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: ما ۵۰ نفر شهید ۱ تا ۵ سال داشتیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/akhbarefori/651884" target="_blank">📅 10:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651883">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUvFHMLpvfSE5_ffuxxzljRWftAVD7gkCmElXoUGx8_wEcVJBVQlaaDR-cSJc_GeK4Y64U_6GxOMqEEykWONbRXvQAeHT4TiMa5ggcI2v__7D0JOtJfVNAobPndEZ_nKxkc1tewn3U-6bwZ3A4ejNOy3N90BjB6yFWs2-HzclNhDUSRrIrt5UMmV1AZT_h89XB5ZHgdvr3gIviirQ4CGe3P2-ZaM7uUlMdqSFMzeLpEWm29XKoObbYoPuDxU-0oNb_03xJc0Nr34ePcSBo2vAhTxnCoRoIYEW6iQBj_2bfr03HtyRv-PUYo46dstaoH5yIbkHQHEi99QMW_xdPTdQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زخمی شدن ۸هزار و ۶۸۳ اسرائیلی از زمان جنگ علیه ایران
🔹
وزارتخانه وزارت بهداشت رژیم صهیونیستی آمار به‌روزشده خود درباره تلفات و مجروحان ثبت‌شده در بیمارستان‌ها از زمان آغاز جنگ علیه ایران را منتشر کرد.
🔹
بر اساس این آمار مجموع مجروحان از آغاز این عملیات تا دوشنبه ۱۱ مه ۲۰۲۶ (دیروز) به ۸هزار و ۶۸۳ نفر رسیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/akhbarefori/651883" target="_blank">📅 10:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651882">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
پرشدگی سدهای کشور به ۶۵ درصد رسید/ کم‌آبی‌های گذشته هنوز جبران نشده
🔹
میزان ورودی آب به سدهای کشور تا بیستم اردیبهشت ماه به شکل قابل توجهی نسبت به سال گذشته افزایش یافته و در مقابل حجم آب ذخیره‌شده در مخازن نیز رشد کرده است.
🔹
اما تداوم ۶ سال متوالی خشکسالی در کشور و انباشت کسر مخزن در سفره‌های آب زیرزمینی باعث شده است که بارش‌های سال آبی جاری نتواند کم‌آبی‌های گذشته را جبران کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/akhbarefori/651882" target="_blank">📅 10:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651881">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
سلاح زمان در دستان ایران
🔹
ساعت در گذر زمان و به ضرر آمریکایی ها است؛ به نفعشان هست که خود را در باتلاقی که افتادند، بیشتر فرو نبرند.
🔹
این هشدار سخنگوی کمیسیون امنیت ملی مجلس به هرگونه حماقت آمریکایی ها است.
🔹
آقای رضایی با انتشار پستی در صفحه خود در شبکه ایکس نوشت:
🔹
از امروز خویشتن‌داری ما تمام شد، هر تعرضی به شناورهای ما با پاسخ سنگین و قاطع مواجه خواهد شد.
🔹
بهترین راه تسلیم شدن و عادت به نظم منطقه ای جدید است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/akhbarefori/651881" target="_blank">📅 10:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651880">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a416e98c52.mp4?token=gcyHMnTpUiUNrK3v8uPYg0EiCphssgmgCbVEf0aufztMJVQpPtGpxQvbdjqCES1TWo3f91r32l4Dqurjigxa-xAgiijUXh5qvtVGVc_qXkTpdlKU_xvc_v5kCVqToP71hPUUZcg6PZSAH8gwlBX14YGEoReWQSEBTtF7vIfVX4MqwTrZ8BjMlVEHs2smLAikiBSsb3NC1FlvXwXKJt6yA7qXIqdjxeWD9uRLTTcCOm2SzMxWXgTqA0vowAN7v-uNZjbuHFq6siNF6YE6IipIjR9gdH0f8IXLoJH4S7MQu_iL1Bl59pxxsbTzfkfl3GZM3cH05mORzDbmjUayyCNz8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a416e98c52.mp4?token=gcyHMnTpUiUNrK3v8uPYg0EiCphssgmgCbVEf0aufztMJVQpPtGpxQvbdjqCES1TWo3f91r32l4Dqurjigxa-xAgiijUXh5qvtVGVc_qXkTpdlKU_xvc_v5kCVqToP71hPUUZcg6PZSAH8gwlBX14YGEoReWQSEBTtF7vIfVX4MqwTrZ8BjMlVEHs2smLAikiBSsb3NC1FlvXwXKJt6yA7qXIqdjxeWD9uRLTTcCOm2SzMxWXgTqA0vowAN7v-uNZjbuHFq6siNF6YE6IipIjR9gdH0f8IXLoJH4S7MQu_iL1Bl59pxxsbTzfkfl3GZM3cH05mORzDbmjUayyCNz8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزنامه‌نگار انگلیسی: موساد در ناآرامی‌های ایران دست داشت
🔹
مت کنارد روزنامه نگار تحقیقی انگلیسی با انتشار یک کلیپ ویدئویی تاکید کرد، طی روزهای اخیر یک گزارش در رسانه های صهیونیستی بازتاب داشته مبنی بر این که سرویس جاسوسی رژیم صهیونیستی موساد در اغتشاشات اخیر ایران دست داشته است.
🔹
این اغتشاشات که با همدستی موساد به راه افتاد نتیجه بخش نبود.
🔹
حمله جنایتکارانه آمریکا و رژیم صهیونیستی علیه ایران باعث شد مردم این کشور پشت نظام بایستند حتی کسانی که پیشتر با آن مخالف بودند، چرا که می دیدند از سوی طرف های متخاصم مورد حمله قرار گرفته اند؛ طرف هایی که به دنبال به دست گرفتن کنترل کشورشان بودند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/akhbarefori/651880" target="_blank">📅 10:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651879">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
معاون نیروی دریایی سپاه: محدودهٔ تنگهٔ هرمز برای ما بزرگ‌تر شده است
🔹
در گذشته، تنگهٔ هرمز به‌عنوان یک محدودهٔ محدود در اطراف جزایری مانند هرمز و هنگام تعریف می‌شد، اما اکنون در چارچوب طرح جدید، محدودهٔ تنگه هرمز به‌طور قابل توجهی گسترش یافته و از سواحل جاسک و سیری تا فراتر از جزایر بزرگ، به‌عنوان یک پهنه راهبردی تعریف شده است.
🔹
به‌عبارت دیگر، تنگه هرمز بزرگ‌تر شده و به یک منطقه وسیع عملیاتی تبدیل شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/akhbarefori/651879" target="_blank">📅 10:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651878">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
تداوم رویکرد خصمانه استرالیا علیه ایران با اعمال تحریم‌های جدید
🔹
دولت استرالیا اعلام کرد که تحریم‌های جدیدی را علیه ۱۱ مقام و نهاد ایرانی اعمال کرده است.
🔹
وزیر خارجه استرالیا گفت که هفت شهروند ایرانی و چهار نهاد در چارچوب دور جدید تحریم‌ها قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/akhbarefori/651878" target="_blank">📅 10:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651877">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
مصوبه کمک بلاعوض به آسیب‌دیدگان جنگ به‌زودی ابلاغ می‌شود
🔹
جودی، معاون بازسازی بنیاد مسکن: در ۲۰۵ شهر و ۱۷۰ روستا آسیب ناشی از جنگ داشتیم؛ تا امروز ۱۲۲ هزار واحد مسکونی شهری و روستایی مورد ارزیابی قرار گرفته است.
🔹
برای واحدهایی که نیازمند بازسازی مجدد هستند یا تعمیرات اساسی‌تری می‌خواهند پیشنهاد تعیین کمک بلاعوض را ۱۷ فروردین به هیئت دولت ارائه کردیم.
🔹
تمام کارهای کارشناسی این پیشنهاد انجام شده و احتمالاً طی روزهای آینده تعیین تکلیف می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/akhbarefori/651877" target="_blank">📅 10:11 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651876">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXaJp8vRR6Aff18XIGeZfQFlrQQoRRjv5CcvLLPqh7uh7s2WypxzUgm6FsDcofGGJNU1KQF0bHssLhgSTBRe3QJ3vvPSpnUuLRiaPzzAdSlbl6Fi9hrpFYWmYw4G7mfrUztfuwrJwu9E5q3WGBkVLdynv_yEccRV2NT6cp6FI4wTevY2i-jiaQddMSkilY2xT7lWfCEPO74MU1to_lciHPNFHjkEqV-1INHtr8yEi2MPzEZExO-oAGKrrlikPg6wBrFMUPw2MRoYokV8QSvhv55M1IodqiqiMz9qbsyrlLsazeNOlrBhJ6SAezv6osGflipkpNzgQtz54PS3N41KfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ ایران، نتانیاهو را به گوشه رینگ برد
🔹
نتانیاهو که تصور می‌کرد با جنگ علیه ایران می‌تواند محبوبیت از دست رفته را بازگرداند، حالا خود را در گوشه رینگ شکست‌ خارجی و فرسایش داخلی می‌بیند. نظرسنجی‌های اخیر نشان می‌دهد ائتلاف او به کمترین میزان کرسی‌های خود از زمان جنگ ۷ اکتبر رسیده و ائتلاف جدید «بنت و لاپید» پیشتاز است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/akhbarefori/651876" target="_blank">📅 10:02 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651875">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmYyS-bc86NO3tkwOy0_OQq_00SUYbtHc5llBRLqzBXduim7zRY-k-YyTu60sAllYjiYMYqSZqrvH3J_5ZXXEEDcz1D-eFgq68tVJWvva_mRQVXZ4CdxloNfBSrZ_yujcETrr47u11wn8VA36Jv6CJBZuoA6y2FE2U9mo4zt9_li9NCC3S61BMAuWQ63v7946qDsF98l0SS6-UYjU-UPjqk112axYy2ciL8PerU-hgWYrMvz2hua_ZgBd7YGXicptHAun5jRSrpeaaEqdFH8IeD9DwsMTy0JmSTEMdqyigqqT8ybrUSZDK_uh4NY1eOrhAUUCLqVBJYAKWL1r799qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسرائیل قانون بحث‌برانگیز محاکمه صدها اسیر را تصویب کرد
🔹
پارلمان رژیم اشغالگر (کنست) با تصویب نهایی یکی از بحث‌برانگیزترین قوانین چند دهه اخیر، راه را برای محاکمه دسته‌جمعی صدها اسیر فلسطینی در ارتباط با عملیات طوفان الأقصى هموار کرد.
🔹
این قانون، به دادگاه‌های ویژه اجازه صدور حکم اعدام را می‌دهد و نگرانی‌های جدی درباره تبدیل نظام قضایی به ابزاری برای انتقام‌جویی سیاسی وجود دارد.
🔹
قانون جدید حکم می‌کند که یک دادگاه نظامی ویژه در قدس تشکیل شود تا اسیرانی را که به دست داشتن در عملیات هفتم اکتبر متهم‌اند محاکمه کند. این دادگاه می‌تواند در کنار پرونده‌های قتل، برای آنچه «جرائم سنگین دیگر» نیز خوانده شده، حکم اعدام صادر کند. تحولی مهم در این قانون، ممنوعیت هرگونه آزادی این افراد در قالب تبادل اسرا است؛ یعنی کسانی که حکم اعدام می‌گیرند یا با اتهاماتی روبه‌رو هستند که ممکن است به اعدام منجر شود، حتی در توافقات سیاسی هم امکان آزادی نخواهند داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/akhbarefori/651875" target="_blank">📅 09:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651874">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f37f5e15.mp4?token=sg6teqsy4IsLaOjPeOGH8PXKg9lcOUmUXJTDo1S0-Qyi1jbH_z6V98Z_NWff_9OTqD-5k6PDkZLMFycRaV_y3zwwU_03q1Y5bXKsf9j1VAfM9-XgOj5xYW5e-AScLJhdmHMNiTcTJtE6HOkLghH08w7kP2wG-GuTDkbEGzvZ0PZct3C5FdPu4yMZf858xD8lKPDl12jo1BOKigX50CPOixIliStbzmNqvqja89RRz6EXKd3OHiyW2VlbM5375QoJSDSoXYTq8HyDm2nSoxlmkfvSnC4uMEsxI5JEBg-nO3D5UfoXdAr4ZQanB_TnRZp2hd8ZEjmx-I4lkw8DMXJcUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f37f5e15.mp4?token=sg6teqsy4IsLaOjPeOGH8PXKg9lcOUmUXJTDo1S0-Qyi1jbH_z6V98Z_NWff_9OTqD-5k6PDkZLMFycRaV_y3zwwU_03q1Y5bXKsf9j1VAfM9-XgOj5xYW5e-AScLJhdmHMNiTcTJtE6HOkLghH08w7kP2wG-GuTDkbEGzvZ0PZct3C5FdPu4yMZf858xD8lKPDl12jo1BOKigX50CPOixIliStbzmNqvqja89RRz6EXKd3OHiyW2VlbM5375QoJSDSoXYTq8HyDm2nSoxlmkfvSnC4uMEsxI5JEBg-nO3D5UfoXdAr4ZQanB_TnRZp2hd8ZEjmx-I4lkw8DMXJcUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخستین تصاویر از اعترافات عبدالجلیل شه‌بخش، تروریست آموزش‌دیدۀ انصارالفرقان که صبح امروز اعدام شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/akhbarefori/651874" target="_blank">📅 09:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651873">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
*خرید کالابرگی اردیبهشت ماه شروع شد!*
🔹
بر اساس رقم آخر کدملی‌، برای خرید اقدام کن
🔹
از *۱۵ اردیبهشت:* -->> کدهای ملی با پایان *۰، ۱ و ۲*
🔹
از *۲۰ اردیبهشت:* -->> کدهای ملی با پایان *۳، ۴، ۵ و ۶*
🔹
از *۲۵ اردیبهشت:* -->> کدهای ملی با پایان *۷، ۸ و ۹*
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/akhbarefori/651873" target="_blank">📅 09:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651872">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrpjbUaMFbIElLcBlUC_iutOGBmm0B4AqLhm0pmtn8rX25kKmAYw83WqEYxHYU8i7L0erQv9d9YC3yXJJbAsCsrfKUUWuh0AOqS4sf06hlzp4zFy4AZskhYpuJOrTSye8TmpmGWOB9lFTOX76jjBRHAuRghbjJR1TLXEEnv8rM0Ka-CkEfMvCsbp4yziLO1v-g3X8n4UJNMZrbvTTCsauFPfVnmThJO_DVmkUv5n7uYhBPgRfAIRr8NfPtik5JmpvR5ZcFEk-gm-QMDcK1zjRPOpcbDfgcKs2USqMQA2C1CfkQiq7lyPyDm7FzqnLbVBW80VO9RpGDxu_faPAC3O-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیپلمات پاکستانی: اصلی‌ترین موضوع مذاکرات «تنگه هرمز» است
🔹
فیصل نیاز ترمذی، سفیر پاکستان در روسیه، در مصاحبه‌ای با خبرگزاری تاس گفت، «مهم‌ترین مسئله در حال حاضر باز شدن تنگه هرمز است که در ابتدا حتی روی میز هم نبود. صادقانه بگویم، از آنجایی که این مذاکرات بسیار محرمانه هستند و ما از جزئیات آنها مطلع نیستیم، باز شدن تنگه هرمز است.»
🔹
سفیر اسلام آباد در مسکو خاطرنشان کرد که ۲۲ درصد از نفت جهان، همراه با گاز مایع طبیعی، کود و مواد اولیه برای تولید کود، از این تنگه عبور می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/akhbarefori/651872" target="_blank">📅 09:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651871">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By70rFmMnKruM3hLP05xbhV7yGLhvMwTr9OwEsWmYJ4oflFXzEsP4pTpeO0Y2uBp5lCBBWF4TaRzKnW8ti2aTs20XOxTtnQxIeCJQjaa8o_3KbD-1gsUurjn8xgZWYgBxuRoTVF2BShYJuju3tHFLqEjlL3MKzeYNRDnK5YWpLQ_TjnaQpHA2C_cRjpFmBCBj1ap8Y4u3C4Nfkw_nfYXCXnpHglf1A-LdZUKm-PJQYapPRlmAakBpVbp_SspGx9Ldkx8RIqucyoC91EJu5dXtgLPT7xSh7cLXRSZ1T44EKKyKNW9pdkWpvebM_ROCBgPX1HbPSBvVAyxaOj7T2_UAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میکروپلاستیک‌ها؛ مهمانِ ناخوانده‌ اتاق کودک
🔹
اتاق کودک را با انتخاب‌های سالم‌تر، امن‌تر کنیم. کم‌کردن پلاستیک یعنی مراقبت بیشتر از کودک و طبیعت  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/akhbarefori/651871" target="_blank">📅 09:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651870">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5af1030dd.mp4?token=oivW6BgFyclminC0xQMmcmXjqW3wD0F_MPIhoQ65Z8eWP2JIvoJi-skHHcp7RtMas7nHZzsPaDzw_zwLABd_M5IOJIpa15YZTnFlhot6zq5yCp6qYg3DbnKmVKADIqkqC_92hi4WtA_MGvRbSkfSihBiSBoK_rNM3C8YIkNKP8xWumsJf4yTv9a_hld1p_5FKz0-Ou-c9GRmWFjq0if88672PFQyEV5m6gmQmOfu1lh4ZM-KLih1xm8L6xs31RGshyRr0I3BK97P-PxZAXo53ofhcoZ5fEW7N0RnJQVqyLz-AdDM6Z1bH4Z9NUM_3jbk6wvii0kJKENF4bFQ4AOgxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5af1030dd.mp4?token=oivW6BgFyclminC0xQMmcmXjqW3wD0F_MPIhoQ65Z8eWP2JIvoJi-skHHcp7RtMas7nHZzsPaDzw_zwLABd_M5IOJIpa15YZTnFlhot6zq5yCp6qYg3DbnKmVKADIqkqC_92hi4WtA_MGvRbSkfSihBiSBoK_rNM3C8YIkNKP8xWumsJf4yTv9a_hld1p_5FKz0-Ou-c9GRmWFjq0if88672PFQyEV5m6gmQmOfu1lh4ZM-KLih1xm8L6xs31RGshyRr0I3BK97P-PxZAXo53ofhcoZ5fEW7N0RnJQVqyLz-AdDM6Z1bH4Z9NUM_3jbk6wvii0kJKENF4bFQ4AOgxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاور عالی فرمانده نیروی هوافضای سپاه پاسداران: شهید تهران مقدم از شکست نمی‌ترسید و همیشه از هر آزمایش نقطه مثبت می‌گرفت
🔹
به توصیه آقا به جای خرید موشک‌های ارزان خارجی، تصمیم گرفتیم خودمان بسازیم و امروز موشک‌های ایرانی بومی و با شناسنامه جوانان کشور هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/akhbarefori/651870" target="_blank">📅 09:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651869">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
عبدالجلیل شه‌بخش تروریست آموزش‌دیده گروهک تروریستی انصارالفرقان به دار مجازات آویخته شد
🔹
بامداد امروز حکم اعدام عبدالجلیل شه‌بخش فرزند جلال، عنصر آموزش‌دیده گروهک تروریستی انصارالفرقان اجرا شد.
🔹
در پی بازداشت عبدالجلیل شه‌بخش در جریان اقدامات ضدتروریستی در شرق کشور، پرونده‌ای علیه وی تشکیل و دادسرا او را با عناوین اتهامی بغی از طریق حمله مسلحانه به مقر‌های انتظامی و عضویت در گروه باغی انصارالفرقان به دادگاه انقلاب معرفی کرد.
🔹
نظر به بررسی دقیق پرونده در مراحل دادسرا و دادگاه و وجود مدارک و مستندات متقن استخراج شده از وسایل ارتباطی و فایل‌های صوتی متهم و همچنین اقاریر صریح وی در مراحل مختلف بازجویی و بازپرسی؛ سرانجام با ابرام حکم وی در دیوان عالی کشور، حکم اعدام این عنصر تروریست بامداد امروز اجرا شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/akhbarefori/651869" target="_blank">📅 08:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651868">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRr9Wb8QaN3jfu0ygTVasa_tr0v4N2St3cTGnG_dFHej1tA-q62FcJuXFc62ymWvBmJGgw6t5JPKz_5Qc_e8K0BoO4uRAxO94lx82I_Ry_2n5PomK788vFXpV-3ODUaGdQ-f1Pg__ct38JefTvsmvLaoaZQew-8Lk973xu3zeFXeBGY0mng_foRq0SiSVwf6TpOeeKIm3PtlHguDghrWCYm5Ys4PDuv6ujHkJciCIJfe_d5_x6DNAMdtfddiDRu_5_ubyinxoaTzJQ859JlBsQ04B1cQnEm0nwa3bmezMCKDOCrnNrhvYHoUrYHdrT1FholKcWEU784LEiYlnZ29fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب‌آبادی: هر متنی درباره تنگه هرمز بدون اشاره به تجاوز، محکوم به شکست است
🔹
معاون حقوقی و بین‌المللی وزارت امور خارجه نوشت:
🔹
تلاش آمریکا و برخی همراهان منطقه‌ای آن برای طرح پیش‌نویسی درباره تنگه هرمز در شورای امنیت، نشان‌دهنده تلاش جدیدی برای جابه‌جایی صورت‌مسئله است: تبدیل پیامدهای یک تجاوز نظامی و محاصره غیرقانونی به پرونده‌ای علیه کشوری که هدف تهدید، فشار و حمله قرار گرفته است.
🔹
«آزادی کشتیرانی» یک اصل حقوقی محترم است؛ اما نمی‌توان آن را گزینشی، سیاسی و جدا از منشور ملل متحد تفسیر کرد. هیچ ابتکاری درباره امنیت دریایی در این منطقه نمی‌تواند هم‌زمان از توسل به زور، محاصره دریایی، تهدید مستمر و نقش مستقیم آمریکا و رژیم صهیونیستی در تولید بحران چشم‌پوشی کند و مدعی بی‌طرفی یا اعتبار حقوقی باشد.
🔹
هر متنی که بخواهد وضعیت تنگه هرمز را بدون اشاره به تجاوز، محاصره، تهدید به زور و حقوق مشروع ایران در دفاع از امنیت و منافع حیاتی خود صورت‌بندی کند، از ابتدا ناقص، جانبدارانه، سیاسی و محکوم به شکست خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/akhbarefori/651868" target="_blank">📅 08:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651867">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a18333360d.mp4?token=tJHCks4blOThLExivkD2GpOadgaA0FcCHqyzmq-P6RLJb-WDwNLPWhQDfMLoqSjbtPVHjghLGNcRnkNI-HJVztu6H0N0PyFsi19NFT6x5CoTUBKA7pBXewtx2Tei93r_m_Hq5D07s1pyM7ictFOIh-0GaQoWZgI_WLAqSwZgzT8OeQz2c7sjoX6OIUd9Gnsre95nKsu1lS-Hiim1A1UPrkCl_QLSfOS0jovCYDmoy4KKkcNX7bIU9o3aGH-CCCiC4N6tISVNdPTgpvClt5i8raebhrmsz5RtrrsDPOp3OB_u7CzhYPeHqmfJUaZgasEmtytvh6xwbcbmbrpZajuhgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a18333360d.mp4?token=tJHCks4blOThLExivkD2GpOadgaA0FcCHqyzmq-P6RLJb-WDwNLPWhQDfMLoqSjbtPVHjghLGNcRnkNI-HJVztu6H0N0PyFsi19NFT6x5CoTUBKA7pBXewtx2Tei93r_m_Hq5D07s1pyM7ictFOIh-0GaQoWZgI_WLAqSwZgzT8OeQz2c7sjoX6OIUd9Gnsre95nKsu1lS-Hiim1A1UPrkCl_QLSfOS0jovCYDmoy4KKkcNX7bIU9o3aGH-CCCiC4N6tISVNdPTgpvClt5i8raebhrmsz5RtrrsDPOp3OB_u7CzhYPeHqmfJUaZgasEmtytvh6xwbcbmbrpZajuhgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بغض رئیس اورژانس استان تهران در حین روایت از جنگ رمضان
🔹
تلخ ترین صحنه جنگ برای من لحظه بیرون آوردن کودک چهار ساله در آغوش مادرش بود که متاسفانه مادرش فوت کرده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/akhbarefori/651867" target="_blank">📅 08:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651866">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GG4n35kipDuVYANcYJyAI3ASHv_DtVoFuApmY7xUPRv2pQIvc9I9F8COZzFVzvKq7mKdjc4SsUOupCURDs9sVSXCmAlZ-OcQhaf5njQqpRO8ivyFWpCjB1Hl3fn48T-64vNIiJGBHQkGCmQECrg3OMKsVC4e0RERSHrBchZaajsc4MMaRmvgEjE_UBHTX-wDzT7aU8tY--lCnvFnZp_KoqYExd97WPLEmi5xKYTjaVpdvRx8f0aTOnhU56nAHV7przl5wu05pJ8AOvn_szfHhAg_90dBbr1SkgXpy0kwtJau0bxr-0sHUXyhTZU6GjpAcKR3ejoP4TMJT_M_dgqHMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهدا میناب | امروز را به نام شهید محمد رئوفی نیا  آغاز می کنیم
🔹
شهید محمد رئوفی نیا به دست دشمن آمریکایی صهیونیستی به شهادت رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/akhbarefori/651866" target="_blank">📅 08:01 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651865">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
سفیر آمریکا: همکاری امنیتی اسرائیل و امارات گسترش یافته است
🔹
مایک والتز، سفیر آمریکا در سازمان ملل اعلام کرده، همکاری‌های امنیتی اسرائیل و برخی کشورهای خاورمیانه، بویژه امارات، گسترش یافته است.
🔹
روزنامه «اسرائیل هیوم» اعلام کرد که اسرائیل سامانه «گنبد آهنین» را در اختیار امارات قرار داده است.
🔹
دو مقام رژیم صهیونیستی و یک مقام آمریکایی به آکسیوس اعلام کردند که این رژیم در مراحل ابتدایی جنگ با ایران، سامانه پدافند هوایی «گنبد آهنین» را به همراه نیروهایی برای راه‌اندازی آن به امارات اعزام کرده است.
🔹
به گفته این منابع، نتانیاهو پس از تماس تلفنی با محمد بن زاید رئیس امارات دستور اعزام یک آتشبار کامل از این سامانه به همراه موشک‌های رهگیر و ده‌ها نیروی نظامی را صادر کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/akhbarefori/651865" target="_blank">📅 07:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651864">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCQriBOQoRuo6YU-4EcCrwUL8rXxl2vb_kYRNa6epaybgfbba61TnV_ot_rhLMl7hjPbOCa-hucJIUt_yza8t5fWIyvmhODXulRFNYdc69eQV8ee8W9GGSVvYQkLn0r9ErJy6lX3mKoPegKELd_lnGJi1Y59GrbfRsgKVQ3jP6BNF6uL-Fypa3TfZxwN6feJq7lwfOZp6K0WVsSg0kgxeb87rwwoIhZoWUs9Mmr2b0yJU09G7fjhtDeNU_DXGPYR95M78bgxuUNYrle3143wfqEslSwIRsL5023-YWwb4r6dcTaf6ygBcMcQCpz89rwCd4SYr9C4ytEI8VQ8N9Q69w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشست مشورتی ترامپ با تیم امنیت ملی آمریکا
🔹
رسانه‌های آمریکایی از نشست مشورتی ترامب با تیم امنیت ملی این کشور درباره ایران خبر دادند.
🔹
این نشست در حالی برگزار می‌شود که ایران با تأکید بر مواضع اصولی و حفظ خطوط قرمز خود، قاطعانه در برابر خواسته های تحمیلی و زیاده‌خواهانه واشنگتن ایستادگی کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/akhbarefori/651864" target="_blank">📅 07:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651863">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
سامانۀ گزارش مردمی گران‌فروشی، احتکار و اخلال در توزیع کالای اساسی راه‌اندازی شد
🔹
دادستانی کل کشور: با هدف دریافت گزارش‌های مردمی دربارۀ تخلفات اقتصادی از جمله گران‌فروشی، احتکار عمده و هرگونه اخلال در تأمین و توزیع کالا‌های اساسی، سامانه‌ای به نشانی
dadsetani.ir/ehtekar
ایجاد شد.
🔹
شهروندان می‌توانند گزارش‌ها و مستندات خود را دربارۀ موارد تخلف از طریق این بستر ثبت کنند.
🔹
دادستان‌های سراسر کشور موظفند در چارچوب قانون و با بهره‌گیری از گزارش‌های دریافتی، با اخلال‌گران در امر تأمین و توزیع مایحتاج عمومی با قاطعیت و سرعت برخورد کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/akhbarefori/651863" target="_blank">📅 06:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651862">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIs5SlpCPISRI1DMiRQbBOQEt8n3WRu4yIPWW4O2zt23ZxtZ2KiFSiJYS-O7qaWUKV1MdY2054dpCd9f-NM2O2JH7M08UpgvB0Z7o4cLesN6lH4SzWlr1FB_j2Kp3BB3N6jHpISPbntVJoVmGY3BDCUNgy10kc71Lz16VQr_FZGTmxFJZiKxaVUWfWfKY4dttrXlOxrLk9Y-4K7z40GsFwTvJ_z-Tqw-lDYEZCOd39e1lvl8VHN-hUsH8iT7jQOxWYtIbBdevVj12J0uNBkcbzSbCPZqW0gWGUeLHpLNJ9_tL3LOBRs9b1LRNiUfVbC3qM7SVU4lwoZ4c36izvvGIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌ان: تندروهای دولت ترامپ برای حمله به ایران فشار می‌آورند
🔹
مقام‌های آمریکایی می‌گویند صبر رئیس جمهور این کشور نسبت به بسته‌بودن تنگه هرمز تمام شده و برای ازسرگیری تجاوز نظامی به ایران جدی‌تر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/akhbarefori/651862" target="_blank">📅 05:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651861">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
مقام حماس: جنایات اسرائیل در غزه هنوز ادامه دارد
🔹
«طاهر النونو» مشاور رسانه‌ای رئیس دفتر سیاسی حماس شامگاه دوشنبه گفت که اشغالگران به تاکتیک‌های کشتار و گرسنگی در نوار غزه ادامه می‌دهند که ادامه جنگ در مقیاس کوچکتر است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/akhbarefori/651861" target="_blank">📅 05:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651860">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dfc83be7d.mp4?token=StABE6TkrXLsdjT0zGwPOUACqzcyNlqU1vDljdBamcyKmmgMGt1Oy0s8-GDj0MO4wIpytrYdh0roKYMUkrM-8rbQULsnrKjDem36VdxvlXsV_zorNMcvVM8kV6sB2Cv6rRwu0-ZtAGwXpBtDbNKj6g2rPRq3n9p9WuWB_-8zOQWWr36-BsVuTO1B3iNyQmKvH8muVVeBiUQCBL0Q_Z7omfJCENDVevJBHzb2HdkzpaVHCZKnFLoFX-xWrRrYxNxlZwtT1_3fs4JjYScV9Zg3xoA4UbTGhSBAlZju1J-XDK9mK4M5SKcTC-wje0mX3h_kos1k8eQE_hIrOx2myYlFj1oHXIHy6rmWit8IiHaV2eowzvKwwPGcz1qyfBGVdvFhsXgf6B7ivHhzX4KiF2uc1OC4L8X-DsB-C3I9JWCCrQf0Pu91HHXiZ4rVQfQ5KW-FiufVagWxUJzGHB7nSP0lRrqNd5QyfnLUQi6L8Tle287i0aZBlDG3DUhBwkMh9aH9_omSI5u3x9Agg1_ethaVqEB-kKrbjjmB1nd1dkLoRBGh97f27ZYYx64RgjcnJHClneDEJXddRwo7-AZJmTMfUeO-jKGJJJRuX7rExxv0sqfJusMLZIgorRwwi68dL45uM0mdmgqGaVsQ8g1w5tuKsf02RDY1NBflgYEDgTcV1l4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dfc83be7d.mp4?token=StABE6TkrXLsdjT0zGwPOUACqzcyNlqU1vDljdBamcyKmmgMGt1Oy0s8-GDj0MO4wIpytrYdh0roKYMUkrM-8rbQULsnrKjDem36VdxvlXsV_zorNMcvVM8kV6sB2Cv6rRwu0-ZtAGwXpBtDbNKj6g2rPRq3n9p9WuWB_-8zOQWWr36-BsVuTO1B3iNyQmKvH8muVVeBiUQCBL0Q_Z7omfJCENDVevJBHzb2HdkzpaVHCZKnFLoFX-xWrRrYxNxlZwtT1_3fs4JjYScV9Zg3xoA4UbTGhSBAlZju1J-XDK9mK4M5SKcTC-wje0mX3h_kos1k8eQE_hIrOx2myYlFj1oHXIHy6rmWit8IiHaV2eowzvKwwPGcz1qyfBGVdvFhsXgf6B7ivHhzX4KiF2uc1OC4L8X-DsB-C3I9JWCCrQf0Pu91HHXiZ4rVQfQ5KW-FiufVagWxUJzGHB7nSP0lRrqNd5QyfnLUQi6L8Tle287i0aZBlDG3DUhBwkMh9aH9_omSI5u3x9Agg1_ethaVqEB-kKrbjjmB1nd1dkLoRBGh97f27ZYYx64RgjcnJHClneDEJXddRwo7-AZJmTMfUeO-jKGJJJRuX7rExxv0sqfJusMLZIgorRwwi68dL45uM0mdmgqGaVsQ8g1w5tuKsf02RDY1NBflgYEDgTcV1l4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیپلمات ارشد ژاپنی: بازگشت ناو «جرالد فورد» به دلیل خستگی مفرط خدمه، نشان‌دهنده فرسودگی ارتش آمریکا و محدود شدن گزینه‌های نظامی ترامپ علیه ایران است/نبرد فعلی یک «بازی بزدل» (chicken game) برای تاب‌آوری است؛ گزارش‌های اطلاعاتی آمریکا تأیید می‌کند ایران دست‌کم تا سه ماه دیگر توان مقاومت کامل در برابر محاصره دریایی را دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/akhbarefori/651860" target="_blank">📅 04:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651859">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ادعای ترامپ درباره احتمال بازگشت به عملیات نظامی در تنگه هرمز
🔹
رئیس جمهور آمریکا در مصاحبه با شبکه «سی‌بی‌اس» ضمن تهدید به انجام اقدامات «بسیار شدیدتر» علیه ایران، مدعی شد که واشنگتن ممکن است به زودی عملیات نظامی در تنگه هرمز را از سر بگیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/akhbarefori/651859" target="_blank">📅 03:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651858">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
نوزادان تازه‌متولد شده، قربانیان دوسال جنایت رژیم‌صهیونیستی در غزه
🔹
نقص‌های شدید هنگام تولد که به بمباران، هوای سمی، گرسنگی و فروپاشی سیستم بهداشتی مرتبط است، به طور چشمگیری افزایش یافته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/akhbarefori/651858" target="_blank">📅 03:17 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651856">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l-H46p9jg7zvauNBPeG-7e8r4fZoVv_elkvLPVKIt5VB5pGREESDc7oPrcghLyTaeVIWib6eDc1zvffJC7fARN0ckSPYQyzde3JpTp5PrKKwNmr_USYapfFo-BhTVIbRORD_svbzOfOHvH3mULXHlpwLdc24wCZZ_-ncAElbaAoDT6u2Kgc2RuCuTmX8pS8nM0smMurD4l3sa__KcG6qUAHftrrsMnq0X2xVkzyTAHcyqNiu-xGO7oOxJ5S8JnYXmzRYnQM5qlvjV0jAIhdpNyuIv0Ak8hR97xBqkQIInlTMk3rNlQM8jW5WZe5U61NnPyVJLy2I_eDqR-QMO13K1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OIih7KaEC9lpiTSTAUA-z-xfsJPSqTEe-4OtDn7XbzBojYgMgx997KOQZBJzdMrn_4u5g2cGzzLN4QVAkt8GoGsCi2VUcS8iWy_g1zyXaZv64lTqlWjYNmxmAhpsq-Vv54D3OOddaDGyr74inshncijtDt7rzsdTIV-f-madJlAOKFPS7yzakt5LmVhPzjYJkXHkCjNnFZ_4txIW_Y_WoBXiWZrutxK9wPy9qAHk6ORe2Yem2rG3wq2EpnKqaggSvhFLt1H0dXdgrIQY4WMe4b8bHIFc7Dvwx0dJiaawe9Xx82kNhFN3JVUo5HQAz8SNtWPmsPPUXOu0mHKGFLPadQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نگرانی عمیق مردم آمریکا از افزایش قیمت بنزین/ مردم آمریکا نمی‌دانند چرا ترامپ تجاوز علیه ایران را آغاز کرد!
🔹
بر اساس نظرسنجی که روز دوشنبه تکمیل شد، دو سوم آمریکایی‌ها معتقدند رئیس‌جمهور دونالد ترامپ به روشنی توضیح نداده که چرا کشور با ایران به جنگ رفته است.
🔹
این نظرسنجی چهارروزه نگرانی‌های عمیقی را درباره افزایش قیمت بنزین آشکار کرد و همچنین نشان داد که بسیاری از رأی‌دهندگان مشکلات خود را بر دوش متحدان جمهوری‌خواه ترامپ می‌اندازند.
🔹
بیش از دو ماه از جنگی که در ۲۸ فوریه با حملات هوایی آمریکا و اسرائیل آغاز شد، می‌گذرد. حدود ۶۶ درصد از شرکت‌کنندگان در نظرسنجی، شامل یک سوم جمهوری‌خواهان و تقریباً همه دموکرات‌ها  گفتند ترامپ اهداف دخالت نظامی آمریکا در ایران را به روشنی توضیح نداده است.
🔹
این جنگ قیمت بنزین را در سراسر کشور حدود ۵۰ درصد افزایش داده است. ایران با بستن مؤثر تنگه هرمز، علیرغم تلاش ناوهای جنگی آمریکا برای بازگشایی این آبراه به روی نفتکش‌ها - یک پنجم تجارت جهانی نفت را متوقف کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/akhbarefori/651856" target="_blank">📅 03:11 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651855">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OECAegYQYpBP6j15_-RXp1ZvlxOwJiL4-N9hy77CsU06583jZoV6PvT4XnIPAgH7R6kHCDwXQANOwZCpfSyBObwIaK-0NarNS7rJgTQdRK4EJgndAeg_Y7ZiYAHkONMsnMgmuvESHJaQ5uDGBpn7MITEHLSWgM1hbdAkDNMKQv3fZN7tpSQijP_Vl7qOtlOON7lNCeUIjAqUNvjSvAslzaVQQcA5-648e66EUs-8CDpGma_ihMZc4iPUIbncAKIJq-FoRTRbJQ9W42XdN0o2pQMN4nMuiyh0PRPXL5gyggND6NIMTlWFlxSxyP-R0hfY7e0-wdsTO8Pyxqjjq6PcYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ذخایر نفت همچنان روبه کاهش
🔹
ترامپ مجبور شد بیش از ۵۳ میلیون بشکه از ذخایر نفتی را برای مهار افزایش قیمت‌های ناشی از جنگ آزادسازی کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/akhbarefori/651855" target="_blank">📅 02:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651854">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qby6_YG_RH97r2KsKiHRQmJcMkZrp4HTybZbPUKieo2WdLvNjrJt_tc_EUJ82I0YaFFhOAID18VRKQ7gw0cnLOf_20P-2JThG6FWujkGQXK6gaijonHXPPgmN0MAiKO4oPdeCsXm9ZIVMqRVkJRZjr3xmy7Jugpvehxv743MMWSWqaTNAP4fF77CdCuDexDUAfu7n4EHZFgAgxmQzu4rn7jeTk5pQ3iQQQfSfuXmI0T0ZeENQkiZLMje4_rqOyNcmhc0InVWhD5ZM3zwLvOSLHzDEhKCRIPcSs8T1B5Y15VuHgFmnbUNlTBJqqYyMmcOHW80dSj272KVXsO0sTDb2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«برنی سندرز»، سناتور ترقی‌خواه آمریکایی: وقت آن رسیده که آمریکا کمک‌های نظامی به اسرائیل را متوقف کند
🔹
اما قرار نیست برای این کار ۱۰ سال صبر کنیم.
🔹
زمانِ توقفِ مسلح‌کردن نتانیاهو و پاسخگو کردن او بابت جنایت‌هایش علیه بشریت، همین حالاست!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/akhbarefori/651854" target="_blank">📅 02:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651853">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckBadekmj21BuEN9t2K1caKoG6cT4EHTZ7ixgMMBrKb7xPf7jB-CTHkLP2hPYOflBr9B4cjCownwzloSDQyRz5JwYS-q1D1YcDUuO3BHop0OA0pH2EJToyRWSHkfWefdrIVc5RKgxGQ80KxXk4b2zb6qKBD8Fl2WSBYvz-H2COFeGB--tarQsdngcQ5t0GK5y0DjfjD9qHSehzGIJ__B82Dz2LjhugxJQ3Gx1NAPVvO0_FKpgTxxVldApkGeCFi_bRa2pOyVgBTNA21zNfAs6y4a-o_lf1bamw1wtq8ya7wtucNfx6rSQyKpJ-I80XTAbc9uuHkZnD8iNXra5wkEBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر دموکرات‌های سنای آمریکا: برای هفتمین‌بار، طرح محدود کردن اختیارات جنگی ترامپ و پایان دادن جنگ ایران به رأی گذاشته می‌شود
🔹
چاک شومر: تکرار می‌کنم، ترامپ آمریکا را به یک جنگ غیرقانونی، پرهزینه و بدون هیچ هدف و هیچ پایانی کشاند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/akhbarefori/651853" target="_blank">📅 02:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651852">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3f0044ce.mp4?token=FoLgX01gmAKrBpslmneEXSvcyaDJfeKHJaUQ37C1d6A8X6dMARuAmHqo368vM_p7DbkTZBMZ7MWBqs358I6cJthEu2jP698Bxd2HJRIUUMGGa8Komttk-8zv2vE4BTgPujNxaeT3QfyS3vMxy8mqZ3yNSooLNGQPbmBNMUxugZTvds3vN5Xe3_j2BQoRHW1t3hEYnIobsYeec7PO493-CwVx46KqYNPCgV9Ss_pRt0qA4bpyC7Vfh73gARSejdhaaFv-TNy3HbN_wE3aTfDin_yzwsG96a9zDP2yepC5Zu1zqOpZJhTJte4E9sN3OoAdmC75cFh9SjxX8n2NSw9OhYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3f0044ce.mp4?token=FoLgX01gmAKrBpslmneEXSvcyaDJfeKHJaUQ37C1d6A8X6dMARuAmHqo368vM_p7DbkTZBMZ7MWBqs358I6cJthEu2jP698Bxd2HJRIUUMGGa8Komttk-8zv2vE4BTgPujNxaeT3QfyS3vMxy8mqZ3yNSooLNGQPbmBNMUxugZTvds3vN5Xe3_j2BQoRHW1t3hEYnIobsYeec7PO493-CwVx46KqYNPCgV9Ss_pRt0qA4bpyC7Vfh73gARSejdhaaFv-TNy3HbN_wE3aTfDin_yzwsG96a9zDP2yepC5Zu1zqOpZJhTJte4E9sN3OoAdmC75cFh9SjxX8n2NSw9OhYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نشریهٔ آتلانتیک: واشنگتن نمی‌تواند پیامد‌های باخت در جنگ با ایران را کنترل کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/akhbarefori/651852" target="_blank">📅 02:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651851">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
افزایش حقوق بازنشستگان تأمین اجتماعی به ایستگاه آخر رسید
🔹
تکلیف افزایش حقوق و زمان پرداخت ۳۰ درصد باقیماندۀ همسان‌سازی بازنشستگان تأمین اجتماعی در سال ۱۴۰۵، احتمالا فردا در نشست مشترک مدیران سازمان و نمایندگان کانون‌ها نهایی می‌شود.
🔹
افزایش حقوق سال ۱۴۰۵ قرار است بر مبنای مصوبات شورای‌عالی کار، و برای حداقل‌بگیران افزایش ۶۰ درصدی و برای سایر سطوح افزایش ۴۵ درصدی در نظر گرفته شود.
🔹
بازنگری در مزایای جانبی شامل حق مسکن، حق عائله‌مندی، حق اولاد و حق معیشت نیز متناسب با نرخ تورم و رشد هزینه‌های زندگی در دستور کار قرار دارد.
🔹
بر اساس قانون مصوب مجلس، همسان‌سازی باید تا سقف ۹۰ درصد اجرا شود که ۶۰ درصد آن در دو سال گذشته اعمال شده و ۳۰ درصد باقیمانده اکنون نیازمند تصمیم‌گیری نهایی است تا این فرآیند تکمیل شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/akhbarefori/651851" target="_blank">📅 01:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651850">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
شکار شبانه مرکاوا در البیاضه
🔹
رزمندگان مقاومت اسلامی، یک دستگاه تانک مرکاوای دیگر ارتش رژیم صهیونیستی را در شهرک البیاضه (جنوب لبنان) با موشک هدایت‌شونده هدف قرار دادند که در پی این حمله، شعله‌های آتش از این تانک زبانه کشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/akhbarefori/651850" target="_blank">📅 01:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651849">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOBwdw5E4X5gPIDKUP9LsDAEtPytM5wkW0nz0DRhyfLgV3v5riKO9W4FlXQRre_IJt-jjAp5_ou3NnPiCV5fbxu7eSUHeolSyD1cxX69PCDUMmJMyhdzPH0aIqaa14w9tcMA2i5EHrqEdG0-xGgOgNS1JcAnvLZ2lG0r-_X6o02BfvQs3A2xuWKwqR9cS_v7kbzpFqikLWQZwJXu5bwtWyolkmc1ymlNC_WJwiwsK5jEq_yb7sN_tKSVr4rkaIMv_T4eFLVD9KXfCsPl5dvFtzsWF0S6kVsl7vVJjvT9SzHdNe7F3oSQazXa8kJW6d3mwLgMwYss7a6ZagwD_CgSpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعاها درباره تمایل ترامپ برای ماجراجویی دوباره علیه ایران
🔹
شبکه ۱۲ تلویزیون رژیم صهیونیستی مدعی شد که رئیس جمهور آمریکا در حال حرکت به سمت دستور تجاوز نظامی مجدد به ایران است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/akhbarefori/651849" target="_blank">📅 01:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651848">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnlV-A6-qAytZQcNPuEmf0lhu59Ub6faC4kkXjPEd6p3YzlW0JFmxdCBQHFXJ7XCqiBmOvAgzPUEmxJwQbBFmr8fDtqObq-7J5-vpd-GXFj8lmbsw5HIKK500PtwULZUZ2bLTcz1SdsKoFPfP1eP7NU863j3aOoZoEci8JIlTJ8-UP_iV76HjOE1WQ8wS2nIPtrtJsKy_UvKC7am2BbPjUJpIOX2GdoIdmtXsrAjtUES7kj2o20ccffHEmpMCv5IEeZ0D3-5-TjvDcTCQ-84v2O7ZoZyPeVG7mpPt-cSiShFzyPArMOqWBcsJTSExKBHwLXKN6PJ6GniPv4Y6JO8_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خاندوزی: کوتاهی سیاست‌گذاران باعث وابستگی اطلاعات ارزی کشور به امارات شد
🔹
وی اشاره داشت: مسیرهای جایگزینی تأمین ارز از طریق چین و روسیه وجود دارد. روش‌های تهاتری هم برای این جایگزینی‌ها وجود دارد.
🔹
وزیر اقتصاد دولت سیزدهم گفت: اگر این اتفاق بیفتد می‌توانیم یکی از مهم‌ترین چرخش‌های اقتصادی بیست یا سی سال گذشته خود را انجام دهیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/akhbarefori/651848" target="_blank">📅 01:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651847">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
حزب‌الله: دیروز ۲۰ عملیات علیه صهیونیست‌ها انجام دادیم
🔹
مقاومت اسلامی لبنان در پاسخ به نقض آتش‌بس، روز دوشنبه، ۲۰ عملیات سنگین را به شرح زیر اجرا کرد:
🔹
انهدام یک تانک مرکاوا، دو بولدوزر زرهی D۹، یک خودروی هامر و چندین خودروی مهندسی و تانکر سوخت در محورهای «رشاف»، «ناقوره» و «طیرحرفا».
🔹
هدف قرار دادن سه‌مرحله‌ای نیروهای صهیونیست در شهرک «طیبه» که منجر به انهدام محل استقرار و اعزام بالگردهای امدادی دشمن برای تخلیه تلفات شد.
🔹
درهم‌کوبیدن تجمعات نظامی و مرکز فرماندهی تازه ایجاد شدهٔ دشمن در «بیاضه» و مواضع توپخانه در «عدیسه».
🔹
مقابله با پهپاد ارتش صهیونیستی در آسمان «صور» با موشک زمین‌به‌هوا.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/akhbarefori/651847" target="_blank">📅 00:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651846">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: امارات حمله به تأسیسات لاوان را انجام داد
🔹
منابع مطلع می‌گویند که فقط ساعاتی بعد از اعلام آتش‌بس توسط آمریکا با ایران، جنگنده‌های اماراتی به تأسیسات نفتی در جزیره لاوان حمله کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/akhbarefori/651846" target="_blank">📅 00:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651845">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
مدیرعامل آرامکو: جهان با بزرگترین شوک انرژی تاریخ خود روبروست
🔹
امین الناصر، مدیر عامل شرکت آرامکو عربیستان سعودی: شوک انرژی که از سه‌ماهه نخست سال جاری میلادی آغاز شده، «عظیم‌ترین شوک تاریخ» است.
🔹
تأخیر در حل بحران‌های کشتیرانی کنونی می‌تواند اثرات مخرب خود را تا آغاز سال ۲۰۲۷ ادامه دهد.
🔹
تداوم اختلال در تردد دریایی در تنگه هرمز حتی برای چند هفته دیگر، باعث می‌شود که بازگشت اوضاع به حالت عادی در بازارهای انرژی تا سال ۲۰۲۷ به تأخیر بیفتد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/akhbarefori/651845" target="_blank">📅 00:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651844">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hs6fGBeCj4enRsfnVgJKKIO8npwWdqjUIN4y2-TwVyLfrcN8bWXrb-ZAqDAjYoCwz-JXbvGoBhHKhR1dPFY8hIzARbLTKtWSFKh9vx0HfP-5r534lOr260rdGtzIsrOm-t4VYKzFeNjjI8kCg8Ogi4fGNdbfaG_V8Wmwvkq-FAIzc4dBbou_GGfIDtXyyGJLtfC-P4GohMFG-GwDh1u87pUO6ywQjdw55Da4mJs8vyUmtW6plBF-vRdpiaX7CVISJmRrQxffQFpoxnBZ6PP-ZFlDNc5O_uv3cHF2Yyu8x-YsSEEuaDdgzxhdxZtFkkXeLFJRVOncsaneA4bjKRm1vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: جز پذیرش حقوق مردم ایران که در پیشنهاد ۱۴ بندی آمده، راه دیگری وجود ندارد / هر رویکرد دیگری کاملاً بی‌نتیجه و شکست‌ پشت شکست است
🔹
راه دیگری جز پذیرش حقوق مردم ایران که در پیشنهاد ۱۴ بندی آمده است، وجود ندارد.
🔹
هر رویکرد دیگری کاملاً بی‌نتیجه و شکست‌ پشت شکست خواهد بود.
🔹
هرچه بیشتر تعلل کنند، مالیات‌دهندگان آمریکایی هزینه بیشتری از جیب خود خواهند پرداخت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/akhbarefori/651844" target="_blank">📅 00:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651843">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtK1F5ub8vV5XD13FCKwJRTxKJoTy9aE5Mha73W-6k_l_E2fN_um5WASle44u3qgSh5hbI38cLUs1vvbZOo6ydyqqKBsqm71tlBzMyZdFMYPVOGgHFbhn2QOJISVGnDw7jKvpj8D7o-UG0um-93DZ9In4yc5_kPPMNKGq94dEFypQEkQHq0XnF_8omemGWOrtyR-wP0bN1w4UFbt292zcQzXxmgYinFdy6jaJhrzJF9j5-slbgfo96_45RnSiWi0eaIZFHL5JhbxGSUwU4L2fYvFx8qHbkKQsdMofH_l14bp_qg_O7nqD5hhNbnPx9GPKqtm6xp9h8VZmm915qst9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش غریب‌آبادی به تلاش‌ها برای صدور قطعنامه درباره تنگه هرمز
🔹
معاون وزیر امور خارجه ایران درباره تلاش‌ها برای طرح پیش‌نویس قطعنامه درباره تنگه هرمز گفت: هر متنی که بخواهد وضعیت تنگه هرمز را بدون اشاره به تجاوز، محاصره، تهدید به زور و حقوق مشروع ایران در دفاع از امنیت و منافع حیاتی خود صورت‌بندی کند، از ابتدا ناقص، جانبدارانه، سیاسی و محکوم به شکست خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/akhbarefori/651843" target="_blank">📅 23:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651842">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
میزبان جام جهانی در باتلاق جنگ گرفتار شده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/akhbarefori/651842" target="_blank">📅 23:40 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651841">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ماجرای حکم یک سرقت فرهنگی
🔹
پلتفرم آپارات با حکم قوه قضائیه به پرداخت ضرر و زیان ۳۶۰۰ میلیارد تومانی به صدا و سیما به علت پخش غیرقانونی بیش از ۳۰ هزار قطعه از تولیدات این سازمان و عدم رعایت حق مالکیت معنوی محکوم شد.
1⃣
حکم  3600 میلیارد تومانی علیه آپارات، بیش از یک اختلاف حقوقی صرف است؛ این پرونده، بزرگترین مورد سرقت سازمان یافته محتوای فرهنگی و هنری در ایران محسوب می شود. انتشار غیرمجاز بیش از 30 هزار اثر رسانه ای، بخشی از این اتهام بود.
2⃣
هدف این پرونده، دفاع از حقوق مولفان، سرمایه ملی و پایبندی به قانون در حوزه اقتصاد رسانه است. بازنشر و بهره برداری اقتصادی بدون مجوز از آثار، نقض آشکار حقوق هزاران هنرمند و تولیدکننده است. این منازعه، پاسداری از مالکیت فکری است.
3⃣
این رای قضایی مترقی که همردیف احکام پرونده های بزرگ مفاسد اقتصادی است، تبلور ایستادگی قوه قضائیه در کنار فرهنگ و حقوق صاحبان آثار است و گامی مهم در جهت تحقق حقوق مالکیت معنوی و آغاز شکل گیری نظمی حقوقی در حوزه مالکیت محتوای دیجیتال در کشور به شمار می رود. قوه قضاییه نشان داد در برابر تضییع حقوق مردم می ایستد. / خبر۲۴
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/akhbarefori/651841" target="_blank">📅 23:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651840">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9de4f171c7.mp4?token=uBGhqH1PYPGhGsz4SvjFdm8hwtVl08YO-QQSpCYdOo_fQVVHS-IOlL0CbATUE7BT2IOLgRWFXEj_NSMsqsQEcEka83-ZyrHEVlrfFIjcgRVO8V5R7HAuhQM6GQ0kIJmIcZA81iK5iN3VdDqqmXBT6XVEhIqy01ZcAlJ81qmIot1zR3JWZhswqnU9ImdqE2nyhDvMdPTJ4GVTeY11mB-up3vRa5mVjQjW_s1yuPWqFRUZkKE9XoE-TKl-PhRJO4h5eb-ZpQoyZH9f87HVV7CpDFmUnOwTi3iyDyFq_10ni0Q2thEOpMkHqsjZQkFENDCmROfmOHi_th-wOguZdbyWVnN9qkd8oCSRNtFWxs-WHpk8CxwCzKwF7CNYqL-p-BfTfzyesJ8uxc7c_RpQ30hcI8LfCIjW0Lv0fHglfjZ5y4IyoV30mB8SC87hIz5w-NsJdb4AFaQVMWkBPAdnz-SwFQIIjkUCp_HYhd95nymCA10RspZJoHkZgvbkUoAu9bZ_uahUI9VyNC3g77IsPF9r_BCjS0GBDwzyjfjXw-CSgOrypMZRLcAf3oO7UzWkSmWDpWsxnNypc7kMGy2yskbYDZvZ8VqXx4M4D6XAwzBTZBi6QcVAyq2zxg7sUByxL2_TX_6hXsUpmixZ8VL1jnRSxlrjqWTSOy1QzeaC_eXJw1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9de4f171c7.mp4?token=uBGhqH1PYPGhGsz4SvjFdm8hwtVl08YO-QQSpCYdOo_fQVVHS-IOlL0CbATUE7BT2IOLgRWFXEj_NSMsqsQEcEka83-ZyrHEVlrfFIjcgRVO8V5R7HAuhQM6GQ0kIJmIcZA81iK5iN3VdDqqmXBT6XVEhIqy01ZcAlJ81qmIot1zR3JWZhswqnU9ImdqE2nyhDvMdPTJ4GVTeY11mB-up3vRa5mVjQjW_s1yuPWqFRUZkKE9XoE-TKl-PhRJO4h5eb-ZpQoyZH9f87HVV7CpDFmUnOwTi3iyDyFq_10ni0Q2thEOpMkHqsjZQkFENDCmROfmOHi_th-wOguZdbyWVnN9qkd8oCSRNtFWxs-WHpk8CxwCzKwF7CNYqL-p-BfTfzyesJ8uxc7c_RpQ30hcI8LfCIjW0Lv0fHglfjZ5y4IyoV30mB8SC87hIz5w-NsJdb4AFaQVMWkBPAdnz-SwFQIIjkUCp_HYhd95nymCA10RspZJoHkZgvbkUoAu9bZ_uahUI9VyNC3g77IsPF9r_BCjS0GBDwzyjfjXw-CSgOrypMZRLcAf3oO7UzWkSmWDpWsxnNypc7kMGy2yskbYDZvZ8VqXx4M4D6XAwzBTZBi6QcVAyq2zxg7sUByxL2_TX_6hXsUpmixZ8VL1jnRSxlrjqWTSOy1QzeaC_eXJw1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر شب به عشق این نظام، در خیابانیم
🔹
ساکت نمیشه این قیام، در خیابانیم
🔹
شعار اهالی شهران در شب هفتاد و دوم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/akhbarefori/651840" target="_blank">📅 23:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651839">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJcbDeiTmgcinMEJZRyFsouL794Z-XTXFnyw-FcRkQWGBfjxIoEDd9OOM2GbCedCJcZgW8O96Z5_hT8q-af8QzEFjcdPz745-6IzkQo6wEu1yTvdc60q3y_HrDXOMvanJzCfuXnA7G-2iMbsl8NDb768y5onbInpFXbLFmnAasuCPJDRpZUgGpVwAJIC-moYWcYqvJ1clzDDyzJgybmhUdcKXPUQgpdjXN-6THIQsOxNZKQsQGILNZliUu3nP3p6JAOLmVfEwRYRY4GfRmFA-XsqznlmkTewrKL3d3lcLy1sPmsTgOM-94swuqJc4IKSBd53Nv_6QOGt_yT0To-ZhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یمن: وضعیت نه جنگ نه صلح با سعودی‌ها را تحمل نمی‌کنیم
🔹
معاون وزیر امور خارجه یمن تاکید کرد که وضعیت نه جنگ و نه صلح دیگر به هیچ عنوان پذیرفتنی نیست و تعلل سعودی‌ها در برقراری صلح، صنعا را به سمت گزینه‌های دیگر سوق خواهد داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/651839" target="_blank">📅 23:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651838">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9711dc3681.mp4?token=nNkmtaoGhwagcyJwFRFvQIYXtGH6BzPkAzeBBsvz9Rp1ywesQFkIWq3T7lwfDPAfpYcemqHVOqk9D4NgyidYtMDebe-HXPmuvEAAKa4GsanJxYJq-ILLA1cLHs6lJd0m9R3HzpMritXqzy3swkFn863dBZDHy2UrQOfeviyWpra93k9foClpixxyl-GT27mRy7zZANBK2T6PyYDz1LD_Ofgi8NOCbiphOL5AocL1no00Muepwm1K2bg-Z4Tm0PyHQ4JzqdjxxXFZ9SqQ6cq_CzEj3VosNu5Kmaqq4nK6mDx5uQganZxTVEUpDeWb89fwV-tFLvMOmhJFwLavCFdP7ToagAHwpNVGqmkHdBh15DzMKcFcih4yOikSnw1uCasP1Vj8oMYf4nBNTeDq2DKUW-80ClBvnS-9tBgeGVawzNtRPWuVflc9isFJuDOtEQg-aftAG4_vwaDhgmE_l5Ydgayr8dE5NG_JEJfr2dt4_9iSrIbsOg-NcC_Wqlo4wZmezCR38tjlhWhNeOnrUbkr23cnzwcaFBNzb34_-sytEZRvZ1DVRBKK6cGgj3BKQ6ry0s8S-eQxeB6vVvzfo84oR8yhpuHGu2r5GfQ3AwvJ0BG3MNkktkdFFDySasovMqnjHP60ywGKsudYsfhRhdAgBTjYiIJkUdideNc9BumD-a4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9711dc3681.mp4?token=nNkmtaoGhwagcyJwFRFvQIYXtGH6BzPkAzeBBsvz9Rp1ywesQFkIWq3T7lwfDPAfpYcemqHVOqk9D4NgyidYtMDebe-HXPmuvEAAKa4GsanJxYJq-ILLA1cLHs6lJd0m9R3HzpMritXqzy3swkFn863dBZDHy2UrQOfeviyWpra93k9foClpixxyl-GT27mRy7zZANBK2T6PyYDz1LD_Ofgi8NOCbiphOL5AocL1no00Muepwm1K2bg-Z4Tm0PyHQ4JzqdjxxXFZ9SqQ6cq_CzEj3VosNu5Kmaqq4nK6mDx5uQganZxTVEUpDeWb89fwV-tFLvMOmhJFwLavCFdP7ToagAHwpNVGqmkHdBh15DzMKcFcih4yOikSnw1uCasP1Vj8oMYf4nBNTeDq2DKUW-80ClBvnS-9tBgeGVawzNtRPWuVflc9isFJuDOtEQg-aftAG4_vwaDhgmE_l5Ydgayr8dE5NG_JEJfr2dt4_9iSrIbsOg-NcC_Wqlo4wZmezCR38tjlhWhNeOnrUbkr23cnzwcaFBNzb34_-sytEZRvZ1DVRBKK6cGgj3BKQ6ry0s8S-eQxeB6vVvzfo84oR8yhpuHGu2r5GfQ3AwvJ0BG3MNkktkdFFDySasovMqnjHP60ywGKsudYsfhRhdAgBTjYiIJkUdideNc9BumD-a4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ذوالنور عضو کمیسیون قضایی و حقوقی مجلس: هر شناوری که بخواهد از تنگه هرمز عبور کند را می‌توانیم از سمنان، تهران و مشهد بزنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/akhbarefori/651838" target="_blank">📅 23:22 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651837">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f59256642.mp4?token=dvgudHmFO0raP3ML6bXrjuVhefnPddu8Af69X3IsBTGqKnXOYxEKBhpJw4OJFiHDKZ8_56T1L03tfJJkTGC7BJGDRyR11RbQxhvjKR3JtzU_0azEsHGlgTJNPK0YvlQvhdST5R3rNCOfaiw8XOPloY2NmjtI5T8CS92zEsDGoOljj_FKMM6jg1KMKk8CvcGGbjQIutM2pJ35cqrci4E-6fiszzSrLyo01y6oEQKUl1NgK6YqnPVTVdPZM6_YEfJEoc3bK3vaoFk2iHbW1C50PFd_HcKZm0A_uICuw4HFUCPF1rxaMuThvjHfHH0hiLPaKP8VSINNH9s9_kNSy6CAaYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f59256642.mp4?token=dvgudHmFO0raP3ML6bXrjuVhefnPddu8Af69X3IsBTGqKnXOYxEKBhpJw4OJFiHDKZ8_56T1L03tfJJkTGC7BJGDRyR11RbQxhvjKR3JtzU_0azEsHGlgTJNPK0YvlQvhdST5R3rNCOfaiw8XOPloY2NmjtI5T8CS92zEsDGoOljj_FKMM6jg1KMKk8CvcGGbjQIutM2pJ35cqrci4E-6fiszzSrLyo01y6oEQKUl1NgK6YqnPVTVdPZM6_YEfJEoc3bK3vaoFk2iHbW1C50PFd_HcKZm0A_uICuw4HFUCPF1rxaMuThvjHfHH0hiLPaKP8VSINNH9s9_kNSy6CAaYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نباید فرض کنیم که ترامپ در حین سفرش به چین، به ایران حمله نخواهد کرد!
🔹
نیما اکبرخانی کارشناس مسائل نظامی: رفتارشناسی دشمن در ترور سیدحسن نصرالله نشان می‌دهد که حتی در مواقع مهم هم ممکن است دست به چنین قمارهایی بزند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/akhbarefori/651837" target="_blank">📅 23:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651836">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGHp8rmAxGlYjwCMXeg8Oq04eT47kgA9l87tIG5hTLjnqjB1SQ86_KpY86UiZwba1Y_sXQxOfvEN0dpn-TXTw6sUA7hIQ46L4JoqGZUY9SZzAcOumh5KPtloaH2-nC__B_Pb9m0bPVIOrHHphJd0rjLMT87MuEeRRogyhKmEGB9HhirARZUlGvxyBIu7ttmWM2DqbI_IeeRKjd4Z7YS2yX2sU9wukIF9SKQJ7DOtJfHvVhKIxdYDERXvIwTGEgAy2gV5kWjAEXJ2L_ll5OWEuo6u_UlnqsBtF05ZDAvpnRwy8OC2RPDGYUib26OEGYxEAHjmAc6VNXQa-dtSXfj1iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تهران، تایوان، تجارت | خطرات پیش روی ترامپ در نشست شی جین پینگ | آمریکا بعد از سفر ترامپ حمله می‌کند؟
🔹
اگر همه‌چیز طبق برنامه پیش برود ) که این خود فرضی بسیار خوش‌بینانه است) دونالد ترامپ روز چهارشنبه وارد پکن خواهد شد تا در یکی از مهم‌ترین دیدارهای دیپلماتیک سال با شی جین پینگ رئیس‌جمهور چین، دیدار کند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3214160</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/651836" target="_blank">📅 23:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651835">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا فهرستی متشکل از ۳ فرد و ۹ شرکت مرتبط با ایران منتشر و اعلام کرد که آنها را در فهرست تحریم‌های ضدایرانی قرار داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/akhbarefori/651835" target="_blank">📅 23:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651834">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
‌مدیرعامل آرامکو: به ازای هر هفته که تنگهٔ هرمز بسته بماند، بازار نفت حدود ۱۰۰ میلیون بشکهٔ دیگر را از دست خواهد داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/akhbarefori/651834" target="_blank">📅 23:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651833">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
آمریکا تحریم‌های جدید علیه ایران وضع کرد
🔹
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا فهرستی متشکل از ۳ فرد و ۹ شرکت مرتبط با ایران منتشر کرده و گفته آنها را در فهرست تحریم‌های ضدایرانی قرار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/akhbarefori/651833" target="_blank">📅 22:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651832">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e31696814c.mp4?token=S22wDKnmqfnRvXNQbb5Vp4Fid3JTuF3RP2153u4BWoIOWXmCMBh47EqzDvQs2Id2katkc07idSPSu1QLsZ7H17K_l6esOUqTLTh-OIXkDJRD7wZ-uD7dY_aZcQn92qwpRWmBI4frfbsIBE0MVkrYdsKr5ejr_jTlxoF0ZQVzLhrUrnldLi2stn7Hb1jUe7HUI5EvjdNHr3UbKQ6Wx0Rz9-k0nebT58VNgajWXl451tiCK7yHOUh4raUQFB2Z2WazlA7PpYho7XFnMamVsBDFghnxF_Z8EdrXU678ytauMhmQDClfjPgfXrBAEPHs0IX3Ueq4CFlexk0w0CxPyE34vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e31696814c.mp4?token=S22wDKnmqfnRvXNQbb5Vp4Fid3JTuF3RP2153u4BWoIOWXmCMBh47EqzDvQs2Id2katkc07idSPSu1QLsZ7H17K_l6esOUqTLTh-OIXkDJRD7wZ-uD7dY_aZcQn92qwpRWmBI4frfbsIBE0MVkrYdsKr5ejr_jTlxoF0ZQVzLhrUrnldLi2stn7Hb1jUe7HUI5EvjdNHr3UbKQ6Wx0Rz9-k0nebT58VNgajWXl451tiCK7yHOUh4raUQFB2Z2WazlA7PpYho7XFnMamVsBDFghnxF_Z8EdrXU678ytauMhmQDClfjPgfXrBAEPHs0IX3Ueq4CFlexk0w0CxPyE34vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار پاکپور: ما برای حفظ این خاک جان می‌دهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/akhbarefori/651832" target="_blank">📅 22:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651831">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f164f209bf.mp4?token=f3ClgRNraXouJ2KYKp8yCGmV07LJ33uc9VEjK3LFxlgODPL-YRxHouN4OfQJzXXrX0qfb3_51W4gb2qp9INr1V4ShMIOFp47bCRkK0pJxNro7LLSbrcveVIx8_2EkZ0PfvKwx_GxdfJQeHYyHd0gOCM51NGzwM3DiPonc_1mnkQNRlB280qeIplc3p8P2eq60hCxrvLjahTBqk00_mbAZ3lflAHXEkjV6rd8_R0Xz1FQWVdGmgpyJpjCpZroRXq69zJ7DVfrl2E7-Aba2PqxTdajuPCBPKmyXhXJLW3Xan0UvHoMZYregpUkbG9GE9ka06eLgHNntxz6QzW3mTjewBOxYzUwyb7W3UEyx6KXxaB2ZseEE9k5RqK_T6zkI3nglocExba8wKdOAQhlvLl1o10CnZmtWol8M1-XJCd3MPhfISX7hGMrDGeZfmsRFTQqHfU9Io_F-DLajmbo5SmztI6Ly66fs99c-PdAVBVM5NUEL0NgvRuqzwarT_P5RHN1TPeAymkhWkc5yGn5HBSvH514Ba7ZbCp_ZinrnKixA83Y9eE-aKFO_IX7K34yaxvmfhvnSG4F9Ev_l7Bmbysopg-iPxGdyVGTEEKk2ChTyGEee8-08GZcopBg1z0XKZDs_1IoH1eIKfNMTJE0sa7lUDL8Fzn8r_W-JxFZRUqA2lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f164f209bf.mp4?token=f3ClgRNraXouJ2KYKp8yCGmV07LJ33uc9VEjK3LFxlgODPL-YRxHouN4OfQJzXXrX0qfb3_51W4gb2qp9INr1V4ShMIOFp47bCRkK0pJxNro7LLSbrcveVIx8_2EkZ0PfvKwx_GxdfJQeHYyHd0gOCM51NGzwM3DiPonc_1mnkQNRlB280qeIplc3p8P2eq60hCxrvLjahTBqk00_mbAZ3lflAHXEkjV6rd8_R0Xz1FQWVdGmgpyJpjCpZroRXq69zJ7DVfrl2E7-Aba2PqxTdajuPCBPKmyXhXJLW3Xan0UvHoMZYregpUkbG9GE9ka06eLgHNntxz6QzW3mTjewBOxYzUwyb7W3UEyx6KXxaB2ZseEE9k5RqK_T6zkI3nglocExba8wKdOAQhlvLl1o10CnZmtWol8M1-XJCd3MPhfISX7hGMrDGeZfmsRFTQqHfU9Io_F-DLajmbo5SmztI6Ly66fs99c-PdAVBVM5NUEL0NgvRuqzwarT_P5RHN1TPeAymkhWkc5yGn5HBSvH514Ba7ZbCp_ZinrnKixA83Y9eE-aKFO_IX7K34yaxvmfhvnSG4F9Ev_l7Bmbysopg-iPxGdyVGTEEKk2ChTyGEee8-08GZcopBg1z0XKZDs_1IoH1eIKfNMTJE0sa7lUDL8Fzn8r_W-JxFZRUqA2lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ذوالنور عضو کمیسیون قضایی و حقوقی مجلس: نقطه دوم استراتژیک ما جزایر سه‌گانه تنب بزرگ و کوچک و ابوموسی است
🔹
می‌توانیم به مین‌های موجود در تنگه هرمز عمر خودکشی و عمق دهیم. ما با مین‌ریزی می‌توانیم تنگه هرمز را حفظ کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/651831" target="_blank">📅 22:51 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651830">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ای بی نیوز مطرح کرد:
🔹
پیت هگست، وزیر دفاع آمریکا گفت پنتاگون بررسی خواهد کرد که آیا سناتور مارک کلی، زمانی که این دموکرات آریزونایی نگرانی خود را درباره فشاری که جنگ با ایران بر انبارهای تسلیحات آمریکا وارد کرده، مطرح کرد، اطلاعات طبقه‌بندی‌شده را به طور نامناسب افشا کرده است یا خیر.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/akhbarefori/651830" target="_blank">📅 22:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651829">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3a30b45fc.mp4?token=Hq-NaQtCh1ORq4KcgA23JMo7970XrmNwd9q2S33YjLoDM5lRmmtBn7v9EQem4wAhGsynHLXhGK6G5SudQRipNgcSyKfIpI3SDCCvRKATW1uDdrzWL9W6_WoBoq9j97BOTZFLQ6mYtw-Qpvi7GWxHnfXTlRHCaykt_m1IUi1aA3S7BS3eYNQH_aHn8BiFa60tndxOmr0dWRHG-w0A5WGjyVXkN1V-FRMX7AdSCl_jRFmMHY2wxbvpgPmO1nInM7edGFUVZ650e6FS7DiSjtiIcI67ZT2c8W28AKOXNs7kMJ--1nqqJCNYfjL_clsVfhhF4YwmRVNreIradlfzAvKGPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3a30b45fc.mp4?token=Hq-NaQtCh1ORq4KcgA23JMo7970XrmNwd9q2S33YjLoDM5lRmmtBn7v9EQem4wAhGsynHLXhGK6G5SudQRipNgcSyKfIpI3SDCCvRKATW1uDdrzWL9W6_WoBoq9j97BOTZFLQ6mYtw-Qpvi7GWxHnfXTlRHCaykt_m1IUi1aA3S7BS3eYNQH_aHn8BiFa60tndxOmr0dWRHG-w0A5WGjyVXkN1V-FRMX7AdSCl_jRFmMHY2wxbvpgPmO1nInM7edGFUVZ650e6FS7DiSjtiIcI67ZT2c8W28AKOXNs7kMJ--1nqqJCNYfjL_clsVfhhF4YwmRVNreIradlfzAvKGPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خط و نشان دادستان تهران برای سوداگران اقتصادی
🔹
۵ تا ۲۰ سال حبس در انتظار مجرمان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/akhbarefori/651829" target="_blank">📅 22:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651828">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccc884b904.mp4?token=hQrS5ryK801H965M2BJ0P5rtTm1r3XuLqOCr1K7_O6sNbMuwRo7uqOGtL8hX_T-zgogqAC8trjFR53YZMVzWNlvMp9sFloGTJHZ3dmm8jRQDNRXzNZ_i8lqBFWTYrlKn-xFotNkGNYa1HcAxo4zYN0oHmmpjaeC8au8jbpw-1IsuMekNyquBOwd3t1rwebhGEeZ5K1dGoC2yRJJdFs9dFeW7h_e_dJqW3uh04ChI4eh9nwqIlm0exzx8v4qw4hIOcjlXAMLuX2OtldA7AZVVf6v9vfERt5iP4l18SEt892YqVzc44MwCRzYUlp7VykhPJfu2elFRjd0ZWjK4HCwGuCLPilWIympLj0NvivkkGGdpzesZ6FRWWw5s-pHNPPEcj4LlcepbvBUOVvLIkOquKnO8cwRGYQqxNQPytnm9Tjx8Y3NWuvubCmHGgeDX5J9HDH5nYLNseLDTuXTVgTd8ggrpksjclY3X6l6kIJEcr1hq_21LVkAhkTuV_PvCIFUE5d52bwyzH9-zIu2dGvBY_G9NwI-NsssqF94KMcL7T1ZzRRVoAiavWdru_5ZEmQMIVj6_2nRWL2UcXsydIaomnFM9yHJfRbx1ha7GTvpfoWp6tTcIcat4iXX4xI3_6tcdFBewZ-mGYEOu5OdCY4qgxKMaZyfiFkjSt4hhVoYnOMk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccc884b904.mp4?token=hQrS5ryK801H965M2BJ0P5rtTm1r3XuLqOCr1K7_O6sNbMuwRo7uqOGtL8hX_T-zgogqAC8trjFR53YZMVzWNlvMp9sFloGTJHZ3dmm8jRQDNRXzNZ_i8lqBFWTYrlKn-xFotNkGNYa1HcAxo4zYN0oHmmpjaeC8au8jbpw-1IsuMekNyquBOwd3t1rwebhGEeZ5K1dGoC2yRJJdFs9dFeW7h_e_dJqW3uh04ChI4eh9nwqIlm0exzx8v4qw4hIOcjlXAMLuX2OtldA7AZVVf6v9vfERt5iP4l18SEt892YqVzc44MwCRzYUlp7VykhPJfu2elFRjd0ZWjK4HCwGuCLPilWIympLj0NvivkkGGdpzesZ6FRWWw5s-pHNPPEcj4LlcepbvBUOVvLIkOquKnO8cwRGYQqxNQPytnm9Tjx8Y3NWuvubCmHGgeDX5J9HDH5nYLNseLDTuXTVgTd8ggrpksjclY3X6l6kIJEcr1hq_21LVkAhkTuV_PvCIFUE5d52bwyzH9-zIu2dGvBY_G9NwI-NsssqF94KMcL7T1ZzRRVoAiavWdru_5ZEmQMIVj6_2nRWL2UcXsydIaomnFM9yHJfRbx1ha7GTvpfoWp6tTcIcat4iXX4xI3_6tcdFBewZ-mGYEOu5OdCY4qgxKMaZyfiFkjSt4hhVoYnOMk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آمریکا در آستانهٔ تسلیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/651828" target="_blank">📅 22:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651827">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
‌مدیرعامل آرامکو: جنگ ایران و بسته‌ماندن تنگهٔ هرمز باعث شده که یک میلیارد بشکه نفت صادر نشود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/akhbarefori/651827" target="_blank">📅 22:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651826">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWiN8RGEGhi4fkZD2p7TtjYpsofocL7qaC-lRZSQZf5mJ_3S7Lgw8LXlZ88sBmpOhB2NnAaGQhgQRT8TeGq86Jcck2Aj1YRvImKR07gNAGqSP-hN_VF4j_3ZO1iHB3mo-Kgwc4WaGNPuIiaAcHUJfMk4gWpMRXMytId6WJ92q00hGwi6hWhQIgKQIypajq3Q95Tt-S30EmheY6Lify2VpG0biyDN2CuZnsd70ydl3mDhw_7v8HotvO2O9VL_0JORGmUf0C3wdRQZDUlrDAi9kbqNwvouBs9Js6j2HR1RKL2ofqsgrbLDY3kPQbjEdv_Jm9xvLdTh-eZ1VgYsDTa2Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون وزیر اقتصاد: انتصابات اخیر در نظام بانکی و بیمه‌ قانونی و برای اصلاح بوده است
معاون وزیر اقتصاد درباره انتصابات اخیر در این وزارتخانه گفت:
🔹
این انتصابات و تغییرات مدیریتی در چارچوب قانون و مقررات موجود است و وزیر امور اقتصادی و دارایی نیز در چارچوب همین اختیارات قانونی، مسئولیت سامان‌دهی و هدایت تیم مدیریتی نهادهای مالی را بر عهده دارد.
🔹
نظام بانکی و بیمه‌ای کشور در سال‌های اخیر با مجموعه‌ای از مسائل ساختاری مواجه بوده و حرکت در مسیر اصلاحات، ارتقای کارآمدی، بهبود سلامت مالی و تقویت نقش بانک‌ها و بیمه‌ها در تأمین مالی، نیازمند انسجام و هم‌افزایی مدیریتی در سطح نهادهای مالی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/akhbarefori/651826" target="_blank">📅 22:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651825">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
برنامه ریزی شبکه‌های معاند برای جام جهانی/ پیشنهادهای کلان به برخی چهره‌های ورزشی و رسانه‌ای
🔹
در شرایطی که بیش از دو ماه از حمله دشمن صهیونی-آمریکایی به ایران می‌گذرد، شنیده‌ها حاکی از آن است که شماری از رسانه‌های فارسی‌زبان خارج‌نشین دارای سابقه دشمنی با ایران، برای تولید ویژه‌برنامه جام‌جهانی ۲۰۲۶ با برخی چهره‌های ورزشی و رسانه‌ای داخل کشور وارد مذاکره شده‌اند.
🔹
منابع آگاه می‌گویند این شبکه‌های معاند وابسته به گروه جم با هدف اختلال در مسیر مقاومت و تضعیف جریان رسانه‌ای داخلی قصد تولید برنامه‌های ورزشی دارند.
🔹
هنوز مشخص نیست این ادعاها در حد شایعه است یا واقعیت دارد؛ اما فعالان رسانه‌ای خواستار روشنگری نهادهای مربوطه و هوشیاری افکار عمومی در برابر هرگونه همکاری با جریان ضدایرانی شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/akhbarefori/651825" target="_blank">📅 22:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651824">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23385c085c.mp4?token=SzS3pLubf7-Uznv-ota9dm6GZcwAec0_XDAoWSt_OE3yjxIuh69Q-e3mJ4q991xvsGtsPEv939_wreS272tCOk4eHa3kk1NF_QkyRDBk-C3aTNVD_wd_gVu69L4ONCfqzv_FxotRpyEsLxDcPXEVbkPmqEfjeakfVPYnMcvdFeCsI2iWd-20opCNKf3d7MPBVjLwnxrKWVLZ6cr-6Sb06BXg5A_bATDAx2wPKQxqvFfqFUFdvi891ym2TJtpFm3bf_bmpvYtVJQztOABOxYVdir342Bz-_bKpTUnHQI5X9gRqE-9S4rH2rUqzkICz32f9ZtZm-6pt97JjA10Qt4sCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23385c085c.mp4?token=SzS3pLubf7-Uznv-ota9dm6GZcwAec0_XDAoWSt_OE3yjxIuh69Q-e3mJ4q991xvsGtsPEv939_wreS272tCOk4eHa3kk1NF_QkyRDBk-C3aTNVD_wd_gVu69L4ONCfqzv_FxotRpyEsLxDcPXEVbkPmqEfjeakfVPYnMcvdFeCsI2iWd-20opCNKf3d7MPBVjLwnxrKWVLZ6cr-6Sb06BXg5A_bATDAx2wPKQxqvFfqFUFdvi891ym2TJtpFm3bf_bmpvYtVJQztOABOxYVdir342Bz-_bKpTUnHQI5X9gRqE-9S4rH2rUqzkICz32f9ZtZm-6pt97JjA10Qt4sCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ذوالنور: آمریکا وارد جنگ گسترده با ایران نمی‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/akhbarefori/651824" target="_blank">📅 22:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651823">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgz5GZooTgCk98E5RV2fyFnQbC_296CXPtOXvL99OE8gdLZLm9c62ZQkr6mv8GC7q2l7XZTvon_Z0ervH5RcRa1evjsXP6Bpi9sArtHehSNkA0lAaecb2zG4q1a1JH24VEE2xc7fOEFxnAhC434PNzlZlWGQcTe6LuKeOMa_0FNvMUs3ePLiKbd03V01m07v1hM3orhmIYwYwRpFhZWOJc40fsFY09W0UklGwm3_xWkzNil9iAaHGiA5hs-3-zEr5XXeTBWd-tNIu4VVYTum2nmlLl5-RyM7FSZ4ewH84GqWpYe8XPmJ9BqMtyc5cfPSg2QGTRTW8mMiEFXFY0SlvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرعونک
ترامپ در واکنش به پاسخ ایران که بقایی، سخنگوی وزارت خارجه، آن را «حق ایران» خواند نه امتیاز تهدید کرد:
🔹
«آن‌ها دیگر نخواهند خندید!» اما تمدن ایران بارها نشان داده که از دل سختی‌ها سربلند بیرون آمده. لبخند ایرانیان از جنس غیرت و مردانگی است و هرگز در محاسبات خصم دیده نمی‌شود. همانطور که نتانیاهو اذعان کرد تصورشان تسلیم ایران در روز سوم جنگ بود و محاسبه بستن تنگه هرمز برایشان غیرممکن بود، ترامپ فرعونکی است که به سرنوشت او دچار خواهد شد. روزی که ایرانی‌ها می‌خندند، شاید دیگر او نباشد.
🔹
هفتصدوچهل‌وششمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/akhbarefori/651823" target="_blank">📅 22:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651822">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91109548b9.mp4?token=tvXESAfdpA7UTs13iRNUZFeDGNtF1O3CdLZlKc-1y_hBu_2DAqjb1wY0PgizSEzBuMqzl5wS7EeuaUlIIYeoIqKmO8PZrPlaCgikVZ20K2I7v1TNWPPQglSfV-YeGkeoBNXdP7RYzI3JFIQB0G2snEEyyB0IxZX-U0bVDNjjwnf5EhpdPAOPF0m_hUnl4UvP3Yf0P3IN1Ow66gFPMPBZWdBA88DFEFLE0mUEI3FLEVQu98jMFbIG0dX9_wuQZWD7Yt1PGfF_UHl0KYKKCdG_vWqdr8HQaFy5S5EU09Io02lBMa9XSxo1LMjjzLhiyDi8Z9FZItJXGItMDNlDVNNuUgOcW5uuOUTo9PSmwj-f0QOW9B2HXPW7R4e_IcPgO4v_QyobvTw82sNZUt6kT9wGh7yD1wF1hUr_hMKO0LWd-c_30xECVKTp9AXjTbs6YjNqD3BLYJmyL18z4b-DWKUZ2y_jdbjrAPS4YNVx9Avs3RFtALE9x5uY5145vMad0iSt37nwj7cddphv6C9LVR1mpXNaKeIvO1k8gmPR6QJccT3Sg9wup4PvjzJSr9LnZ6lqIUNHdkqFMDNIAN7xr0GRzhZjWeODsXcQ0HMUCYSBKS9M_TJdlhVeeaL1KdkLKVBt0RnEqmlBba-Y_bv9h6LeGBzzAHQqOCvxGXX4VA_rERQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91109548b9.mp4?token=tvXESAfdpA7UTs13iRNUZFeDGNtF1O3CdLZlKc-1y_hBu_2DAqjb1wY0PgizSEzBuMqzl5wS7EeuaUlIIYeoIqKmO8PZrPlaCgikVZ20K2I7v1TNWPPQglSfV-YeGkeoBNXdP7RYzI3JFIQB0G2snEEyyB0IxZX-U0bVDNjjwnf5EhpdPAOPF0m_hUnl4UvP3Yf0P3IN1Ow66gFPMPBZWdBA88DFEFLE0mUEI3FLEVQu98jMFbIG0dX9_wuQZWD7Yt1PGfF_UHl0KYKKCdG_vWqdr8HQaFy5S5EU09Io02lBMa9XSxo1LMjjzLhiyDi8Z9FZItJXGItMDNlDVNNuUgOcW5uuOUTo9PSmwj-f0QOW9B2HXPW7R4e_IcPgO4v_QyobvTw82sNZUt6kT9wGh7yD1wF1hUr_hMKO0LWd-c_30xECVKTp9AXjTbs6YjNqD3BLYJmyL18z4b-DWKUZ2y_jdbjrAPS4YNVx9Avs3RFtALE9x5uY5145vMad0iSt37nwj7cddphv6C9LVR1mpXNaKeIvO1k8gmPR6QJccT3Sg9wup4PvjzJSr9LnZ6lqIUNHdkqFMDNIAN7xr0GRzhZjWeODsXcQ0HMUCYSBKS9M_TJdlhVeeaL1KdkLKVBt0RnEqmlBba-Y_bv9h6LeGBzzAHQqOCvxGXX4VA_rERQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شروط ما را بپذیر یا اقتصاد جهان را منفجر کن!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/651822" target="_blank">📅 22:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651821">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
مدیرعامل آرامکو: اگر تنگهٔ هرمز همین امروز هم باز شود، بازگشت تعادل به بازار نفت ماه‌ها زمان خواهد برد
🔹
اما اگر بازگشایی تنگه چند هفتهٔ دیگر به تعویق بیفتد، عادی‌سازی شرایط تا سال ۲۰۲۷ طول خواهد کشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/akhbarefori/651821" target="_blank">📅 22:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651820">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">جلسه 46_مراسم دعای ندبه_سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">@masaf</div>
</div>
<a href="https://t.me/akhbarefori/651820" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه چهل‌وششم
رائفی‌‌‌‌‌‌پور:
🔹
0:3:30 اولین تنبیه ای که خداوند برای حضرت آدم قرار داد
🔹
0:14:45 انسان ترکیبی از فرشته و حیوان آفریده شده است
🔹
0:28:30 یکی از مؤثرترین روش‌های ترک گناه
🔹
0:37:00 غریزه بخشی از هدایت انسان است
🔹
0:52:00 تفاوت صبر در انسان ها و پیامبران
🔹
1:00:40 اتفاق شنیدنی برای موجودات بعد از نحوه ی پاسخگویی‌شان نسبت به خداوند
🔹
1:04:25 عاقبت کسانی که به اهل بیت دل دادند
🔹
1:11:00 مطهرین تنها کسانی هستند که به ذات قرآن پی می برند
🔹
1:16:00 وضعیت انسان‌هایی که قرآن را بدون اهل بیت قبول کرده اند
#دعای_ندبه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/akhbarefori/651820" target="_blank">📅 22:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651819">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دلایل فنی ایران برای دریافت عوارض در تنگه هرمز
نادرقلی ابراهیمی، عضو کمیسیون محیط زیست مجلس در
#گفتگو
با خبرفوری:
🔹
کشورهای حاشیه خلیج فارس و شیخک‌های عربی بالغ بر ۹۰ درصد آب شرب خود را از خلیج فارس تأمین می‌کنند که نمک و ضایعات برگشتی آن وارد دریا می‌شود.
🔹
نمکی که وارد خلیج فارس می‌شود بیش از حد مجاز است و بابت آن باید خسارت دریافت کنیم.
🔹
یک بحث آلودگی تنگه هرمز ناشی از خسارات جنگ است؛ خساراتی که به پالایشگاه، امکانات نفتی و کشتی‌های سوخت‌رسان ما وارد شد.
🔹
موضوع دیگر آب توازن کشتی‌های سوخت‌رسان است که هنگام برگشت، آب داخل مخازن خود را در خلیج فارس رها می‌کنند، این آلودگی‌ها کل آبزیان و پرندگان ما را نابود می‌کند.
@TV_Fori</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/akhbarefori/651819" target="_blank">📅 22:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651818">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
ایران از پاکستان دلار را دور زد؛ آغاز تبادل کالا با ارزهای محلی
🔹
نخستین سازوکار عملیاتی تبادل کالا با ارزهای محلی میان ایران و پاکستان با موفقیت راه‌اندازی شد.
🔹
این طرح که توسط اتاق بازرگانی مشترک دو کشور و پیاده‌سازی شده، دیگر نیازی به دلار، یورو و حتی سوئیفت ندارد.
🔹
حالا صادرکنندگان می‌توانند بدون واسطه‌های بین‌المللی، وجوه خود را از طریق مرکز مبادله ارز و طلا به‌صورت مستقیم و آنی تسویه کنند./خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/akhbarefori/651818" target="_blank">📅 22:07 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651817">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کوثری: ایران عمان را در تنگه هرمز شریک می‌کند
اسماعیل کوثری، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبر فوری:
🔹
وزارت امور خارجه به عنوان نماینده دولت، اقدامات مربوط به لایحه کنترل و مدیریت تنگه هرمز و خلیج فارس را انجام دادند وبه  کمیسیون امنیت ملی آوردند.
🔹
مشخص شد که عمان را هم باید در این رابطه سهیم بدانیم و با آنها نیز رایزنی شود که در این مدت وزارت امور خارجه این کار را انجام داد.
🔹
تنگه هرمز بین ما و کشور عمان است از این جهت این کار صورت گرفته است و نتایج نهایی آن باید در مجلس به تصویب برسد.
@TV_Fori</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/akhbarefori/651817" target="_blank">📅 22:07 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651816">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akZDyWGqJeTJ1gBOQl2XqjnAak0DsPgD9ng8UEux1XTGTQpWJngzsxYPQzXmEmJcrZ13yliDy0gl2eqgR9M51al4feiCL7wQpeTiWaJT1pSJva6_ZpfLuROXWEeNFhla3zW9l8QL-9Tk_PXQ4plTMnZ53qISepQzMQ7LREVWKwq3yJTwfTkiK4vjCtM59dd5a9x58o_77VePDGG5T2NoWEiZSxMrrIv1Bh2vPigXpTF-ZOHNGfOHIvIUgBOhY9ZCpvnkhP5pDFLoohQl9F9FKGetCiSjCh--lQVHEdcPJnraGMCFTdfVQmytGhPTr4OfAX4Bgj8Z0efxXUNWcZhwVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: برای تمام گزینه‌ها آماده‌ایم، شگفت‌زده خواهند شد
🔹
نیروهای مسلح ما آمادهٔ پاسخگویی درس‌آموز به هر تجاوزی هستند؛ استراتژی اشتباه و تصمیم‌های اشتباه، همیشه نتیجهٔ اشتباه خواهد داشت، همهٔ دنیا قبلاً این را فهمیده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/akhbarefori/651816" target="_blank">📅 21:59 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651815">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8c8193b.mp4?token=Mj0pa2UaqPrM9qIZ9PlXI6m8LYs7CdMGB5w5Ykg4oN4FS6vHnhm_W4UMuYvc-Sqyknjsa8WT5P3xCMyFJLZw1LVYnkaJv9CfkYdLY3v3-q0nIhXnF78NtjxWafL4CjWbtE4w9k5REcK4b6wexBFa651GQ00hXWcyYwCea50TqwdUW7WYiyO3kFufTWECnu6X1j2O4ShDaPNOqi-pXlbIQdmQZPFl59yZblgJAa7NTMegBgUb7IVOuXSCE40dxOVzVyJgKxCk9eBq_UST9ajaxpMbxeX3EU61jD_g8j5ks0MsHoWthSiht6Cvoe0IlUeftdp_VCDLEeyjkZyfHMmnOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8c8193b.mp4?token=Mj0pa2UaqPrM9qIZ9PlXI6m8LYs7CdMGB5w5Ykg4oN4FS6vHnhm_W4UMuYvc-Sqyknjsa8WT5P3xCMyFJLZw1LVYnkaJv9CfkYdLY3v3-q0nIhXnF78NtjxWafL4CjWbtE4w9k5REcK4b6wexBFa651GQ00hXWcyYwCea50TqwdUW7WYiyO3kFufTWECnu6X1j2O4ShDaPNOqi-pXlbIQdmQZPFl59yZblgJAa7NTMegBgUb7IVOuXSCE40dxOVzVyJgKxCk9eBq_UST9ajaxpMbxeX3EU61jD_g8j5ks0MsHoWthSiht6Cvoe0IlUeftdp_VCDLEeyjkZyfHMmnOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت دریابان بازمانده ناو دنا از جنایت آمریکا
🔹
دنا خاکمون بود حتی اگر [آمریکا] اخطار تخلیه هم می‌داد، یک نفر تخلیه نمی‌کرد
🔹
ناو دنا همیشه یک افتخار و یک غم بزرگ در دل تاریخ ایران باقی می‌ماند. سوگ دلاورمردانی که بدون سلاح برای مانور غیرنظامی اعزام شده بودند و ناجوانمردانه توسط زیردریایی‌های آمریکایی به شهادت‌ رسیدند تمام نمی‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/akhbarefori/651815" target="_blank">📅 21:59 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651814">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
مقام ایرانی: تهران مخالف انتقال اورانیوم به خارج از خاک خود است
🔹
شبکه خبری الجزیره امروز دوشنبه گزارش داد که واشنگتن در پیشنهاد خود خواستار دستیابی به اورانیوم غنی‌سازی شده با غنای ۶۰ درصد شده است.
🔹
این مقام همچنین گفت که آمریکا با انتقال اورانیوم غنی‌سازی شده ایران به روسیه مخالفت کرده و کشور ثالثی را برای انتقال آن پیشنهاد داده است.
🔹
وی با بیان اینکه ایران با انتقال اورانیوم به خارج از خاک خود مخالفت کرده، در عین حال خبر داد تهران آماده است اورانیوم مذکور را تحت نظارت آژانس بین‌المللی انرژی اتمی رقیق کند.
🔹
این مقام با تأکید بر اینکه ایران آماده است اورانیوم با غنای بالا را به سطح ۳.۷ درصد و ۲۰ درصد رقیق کند، تصریح کرد: آمریکا خواستار توقف ۲۰ ساله غنی‌سازی اورانیوم شده، اما ایران این درخواست را رد کرده است.
🔹
وی در پایان گفت که آمریکا پیشنهاد پرداخت غرامت به ایران در ازای خسارت‌های جنگ را رد کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/akhbarefori/651814" target="_blank">📅 21:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651813">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEyvy9B2x2GDkxiPiuwtOGAjoXwsa80xZreYEd_ky_8s5XfM6JM2ax6zCvZshZtYRJxcjxxbZybdlLIk5jkZAu0C1p3l9KoVta_3FkbmC__LdobAUL5q7p_kbt5ULnaz0-Kca0nQ8AWqPmKYpK8znueLntooJIlEDh4mwsSuCxwsG88HlAyzWw7Q6FBPOgouP0cV1WTtm4cvLwdssW4KiUNcVKw-k4QVjKcjInGEEO-YO9KPvs017dnhTeq-kqCSemTtx4XVIuunC5WVc8q00LBnY_M3ac2H0cHaMGXTFQdpw1OTV6gfd5v2fUeKQQi9lRRyXRS1ZC6SKbvldeojqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شوک تازه به نتانیاهو از داخل سرزمین‌های اشغالی
🔹
در نظرسنجی جدید روزنامه معاریو، از افراد شرکت‌کننده پرسیده شد که از میان نتانیاهو و بنت کدام شخص را برای تصدی جایگاه نخست‌وزیری مناسب ‌تر می‌دانید؟
در پاسخ ۴۶ درصد بنت را فرد شایسته این جایگاه عنوان کرده و ۴۱ درصد نیز به نتانیاهو رای دادند.
🔹
در دوگانه آیزنکوت- نتانیاهو نیز، ۴۴ درصد از نخست وزیری آیزنکوت حمایت کرده و ۴۲ درصد، رای به نخست وزیری نتانیاهو دادند.
🔹
مطابق این نظرسنجی، اکنون وضعیت محبوبیت نتانیاهو در نظرسنجی‌ها با کاهش محسوسی همراه شده و نخست وزیر فعلا از محبوبیت بالایی در بین ساکنان اراضی اشغالی برخوردار نیست. /خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/651813" target="_blank">📅 21:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651811">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هزینه پذیرایی از اهداکنندگان خون سالی ۳۰۰ میلیارد تومان است!
بابک یکتاپرست، معاون اجتماعی سازمان انتقال خون:
🔹
وضعیت ذخایر خونی مطلوب است، اما آمار آن را نمی‌توانم اعلام کنم.
در ده سال گذشته چنین ذخیره‌ای نداشتیم و رشد ۱۰۰ درصدی داشتیم.
🔹
تجهیزات فنی نزدیک به ۱۰ تا ۱۵ سال خریداری نشده؛ هزینه مورد نیاز آنقدر زیاد است که رویاست.
🔹
به ۱۰۰ دستگاه سانتریفیوژ یخچال‌دار (هر کدام ۴ میلیارد) و ۱۰۰ دستگاه تجهیزات کامل تیم سیار خون‌گیری (هر کدام ۵ میلیارد) نیاز داریم.
🔹
سالانه ۲.۵ تا ۳ میلیون اهداکننده خون داریم و هزینه پذیرایی (نوشیدنی و کیک) سالی ۳۰۰ میلیارد تومان می‌شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/akhbarefori/651811" target="_blank">📅 21:50 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

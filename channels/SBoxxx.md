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
<img src="https://cdn4.telesco.pe/file/J6JF_LgI10-tfdw1a34k-ZUcLlvQcN3vyftkfmG4Wpmnlcm9yy8KZ1vyMJBUxNcgYkTxTOGpgP8HEC5-tHggvYgf8m0tyJ4swkV2NY810wapBQvGGMgBnrL_7-CI3cLjYafC9x4UveWNMEW1-nlH02w_H4CIWqOvnrc-Cdzjf1ZTCzgNRSMSomE0xAArzA5UTPJ3euIKZYmPNOaca4gfcLQC12P4tdT7gCS6hbIoZp1wjjoqQgKMert39SHv4SqMlAHWXyx64PmnpWZdRpAp6T1WPrdDh_AtuYYxp7EH6cy7CqcGXObooXL-bKpYPoV4W6VDsj4p-4AA6f_JYVD3Kg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.99K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 18:19:09</div>
<hr>

<div class="tg-post" id="msg-17039">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">به حمله رژیم صهیونیستی به ضاحیه پاسخ دردآور خواهیم داد  سخنگوی کمیسیون امنیت ملی مجلس: امشب به آسمان سرزمین‌های اشغالی نگاه کنید.</div>
<div class="tg-footer">👁️ 553 · <a href="https://t.me/SBoxxx/17039" target="_blank">📅 18:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17038">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تشکیل جلسه فوری شورای عالی امنیت ملی ایران</div>
<div class="tg-footer">👁️ 583 · <a href="https://t.me/SBoxxx/17038" target="_blank">📅 18:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17037">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تشکیل جلسه فوری شورای عالی امنیت ملی ایران</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/SBoxxx/17037" target="_blank">📅 17:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17036">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ:   رهبری جدید ایران منطقی‌تر و باهوش‌تر است و (آیت‌الله) مجتبی خامنه‌ای بخشی از روند تصویب توافق شده است  اگر رهبر ایران بخواهد، من آماده‌ام که مستقیماً با او صحبت کنم، اما هنوز مستقیماً با او صحبت نکرده‌ام.  من این جنگ‌های بی‌پایان را دوست ندارم، و…</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/SBoxxx/17036" target="_blank">📅 17:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17035">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">امروز اسراییل به ساختمانی در ضاحیه بیروت حمله هوایی انجام داد که گفته می شود تا ۵ کشته در پی داشته است.</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/SBoxxx/17035" target="_blank">📅 17:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17034">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فوری | ترامپ به ان‌بی‌سی:   من محاصره دریایی ایران را جنگ نمی‌دانم، اما هر کسی که می‌خواهد آن را جنگ توصیف کند، انتظار دارم بتواند این کار را انجام دهد.  ایران روزی ۴۰۰ تا ۵۰۰ میلیون دلار بخاطر محاصره دریایی ما از دست می‌دهد .</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/SBoxxx/17034" target="_blank">📅 17:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17033">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فوری | ترامپ به ان‌بی‌سی:   دلیل اعمال محاصره دریایی بر ایران این است که آن‌ها سعی کردند محاصره‌ای اعمال کنند و اکنون ما محاصره‌ای بر آن‌ها اعمال کرده‌ایم.</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/SBoxxx/17033" target="_blank">📅 17:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17032">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ:   اگر به توافقی دست نیابیم، ارتش ایران را بیش از پیش تضعیف خواهیم کرد تا نیروهای ما بتوانند با اطمینان و امنیت کامل، اورانیوم را در اختیار بگیرند!  هیچ پولی را آزاد نکرده و هیچ تحریمی را کاهش نمی دهیم!  لبنان بخشی از توافق نیست!</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/SBoxxx/17032" target="_blank">📅 17:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17031">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ:
اگر به توافقی دست نیابیم، ارتش ایران را بیش از پیش تضعیف خواهیم کرد تا نیروهای ما بتوانند با اطمینان و امنیت کامل، اورانیوم را در اختیار بگیرند!
هیچ پولی را آزاد نکرده و هیچ تحریمی را کاهش نمی دهیم!
لبنان بخشی از توافق نیست!</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/17031" target="_blank">📅 17:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17030">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ادعای رسانه اسراییلی: تعویق حمله به ضاحیه بیروت در پی مداخله آمریکا  سازمان رادیو و تلویزیون اسراییل  گزارش داد که طرح حمله نظامی به ضاحیه جنوبی بیروت به دلیل دخالت‌های طرف آمریکایی به تعویق افتاده است.</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/SBoxxx/17030" target="_blank">📅 17:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17029">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سخنگوی وزارت خارجه و سخنگوی تیم مذاکره‌کننده اسماعیل بقایی در مصاحبه با سی‌ان‌ان:
ما چندین اختلاف نظر در مذاکرات داریم، که مسئله اصلی پذیرش حقوق ایران، از جمله حق غنی‌سازی، توسط ایالات متحده است.
از زمان اجرای آتش‌بس، آمریکایی‌ها چندین بار کشتی‌های تجاری ایرانی را در تنگه هرمز و آب‌های بین‌المللی هدف قرار داده‌اند.
وضعیت منطقه‌ای و آتش‌بس بسیار شکننده و خطرناک است و این وضعیت نتیجه رویکرد بی‌محابای ایالات متحده نسبت به منطقه و آتش‌بس است. نیروهای مسلح ایران با تمام قدرت به هر حمله‌ای پاسخ خواهند داد.</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/17029" target="_blank">📅 15:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17028">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">Secret Box
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/17028" target="_blank">📅 14:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17027">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnimTUsFRJn7I2IRk8e11wMsQIUcgrEuLvneD67HHmaFpGtcDD70GOUinzJoGN6F5MjZYlxRyzOUyFf8_sTDkQtEExyWnUr1bKmIRXTW-B3UJG7_v0kup4deBycB56aRtp9ZXbT2Rh99zPdRbymsEFM43zkqouhM9dzxjOhIUrlJGH6JkJUdCuR3KsxUhSU2KM1c3pH8-mkFVYPadz-3X2okoTIeQ1r-tWydG2T-6XV9CMohNEOquzTb2NyrN_cNYpV8nEl8FmFYnz3-PPjGElysoXHnLLVkymuZCW9Z3drYUb3lWfoSp2cfOMsdV4B8oC608_scyuAduoHr1is7wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرانجام کتابی که وعده دادم درباره پیوند ژئوپولیتیک و بازارهای مالی ترجمه کنم، به چاپ رسید.
به نظرم در این شرایط که چندین جنگ همزمان در منطقه و جهان در جریان است و تنشهایی که میتواند بزودی تبدیل به جنگ های دیگری بشود، فقدان وجود یک دیدگاه تحلیلی چهارچوب بندی شده و متدیک به پویه های ژئوپولیتیکی منجر به ادراک نادرستی از بسیاری نوسانات بازاری شده و فرجامش افزایش میزان خطای تحلیلگران و معامله گران خواهدبود.
این کتاب را که پاسخی به این چالش است میتوانید
از اینجا سفارش داده و تهیه کنید.</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/17027" target="_blank">📅 14:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17026">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZ3nSxOR7z17GgFjZKvhEbVW4fz16NycRUI2rkX8U_GJgtl0aYRAWoUnFwsA2Ln3mZ42gh0TmQwris12kyWf6HouIG2l5SpwzjqnA_LaM-zOBiKkh0O6svpjExJiUGbTq2w22AkySx3yDt13hATRX3KY-yFOGpcf7enKurHrio6A-6N5VBC_lrPanPlQ7gxo6yBn4rl_HF5lVkSnX3JhdA4NAgob2E7B2VB8kMKUxANq6j68Q80vI2xZDwlTNhTiGxtFUCSiwQ9xeAUaRuVnhKzRAp9NYP_V-nxwQhcoTpS4tKtdPvPMp3YH-dR3JTqTjZCqXrtVEs_3V31aU77A3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▪️
خبر این است: وزیر کشور پاکستان پیش وارد تهران شد  مایلم یکبار دیگر صراحتا هشدار بدهم که ابداً نباید حسن نیت داشتن پاکستان را پذیرفت؛ پاکستان یکی از فاسدترین کشورهای دنیاست که توسط یکی از فاسدترین نظامیان دنیا اداره میشود. نظامیانی که وابسته سعودی، آمریکا،…</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SBoxxx/17026" target="_blank">📅 13:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17025">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دقت کنید که سنتکام می‌گوید که دوباره «سایتهای راداری نظارتی ساحلی ایرانی» را در گروک و قشم زده اند!  پیشتر اشاره شد چرا مهم است.</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/17025" target="_blank">📅 13:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17024">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بیانیه حماس در پی تیراندازی امروز ۲ تن از اعضایش در یک شهرک اسراییلی
«جنبش مقاومت اسلامی (حماس) عملیات تیراندازی قهرمانانه در مستعمره کوخاو یائیر، شمال قلقیلیه، و همچنین عملیات قبلی در تقاطع مستعمره افرات، جنوب بیت‌المقدس را تحسین می‌کند.
این دو عملیات در پاسخ به تهاجم مداوم اشغالگر به نوار غزه و سیاست‌های ادامه‌دار یهودی‌سازی، کشتارهای خارج از چارچوب قضایی، گسترش مستعمرات، بازرسی های بدنی و حملات علیه مردم فلسطینی در کرانه باختری و اورشلیم صورت گرفته است.
اشغالگر، هرچقدر هم در سرکوب و جنایات خود پیش برود، موفق به توقف موج مقاومت در کرانه باختری نخواهد شد. مردم ما مسیر پایداری و سرسختی را تا رسیدن به آزادی و بازیابی حقوق کامل خود ادامه خواهند داد.
ما در برابر تشدید سیاست‌های گسترش مستعمرات، مصادره زمین، کشتار، بازداشت، آوارگی و تروریسم مستعمره‌نشینان هشدار می‌دهیم. تأکید می‌کنیم که این جنایات امنیت یا ثباتی برای آن به ارمغان نخواهند آورد، بلکه منجر به تشدید بیشتر درگیری و مقاومت خواهند شد.
ما از جامعه بین‌المللی می‌خواهیم مسئولیت‌های خود را به عهده بگیرد، با جدیت برای توقف تروریسم اشغالگر علیه مردم و سرزمین ما تلاش کند، تهاجم آن را پایان دهد و رهبران جنایتکار آن را پاسخگو سازد.»</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/17024" target="_blank">📅 13:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17023">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">زلنسکی: روسیه عمداً سایت ذخیره سوخت هسته‌ای را در حمله‌ای «بسیار شنیع» هدف قرار داد</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/17023" target="_blank">📅 12:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17022">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">قطعی برق خانه‌ها از اواخر حرداد شروع خواهد شد  آرش نجفی، رئیس کمیسیون انرژی اتاق بازرگانی، صنایع، معادن و کشاورزی ایران: پیش‌بینی می‌شود که این روند از اواخر خرداد یا اوایل تیرماه آغاز شود و مردم ایران احتمالاً به مدت سه ماه با این شرایط درگیر خواهند بود که…</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/17022" target="_blank">📅 11:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17021">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXpDsrvQjPfoaNJV6al7QYwuQzQwIJNWLpT6yPLLM2E-Cq5onFPt109jXfW6bUwS_C-dpiKFY0-1fbPkLztA-Oi-LFodcWjfQke3sI5GPxJ3U85Kg24yU2iw54Lycu7Q5Q3gTZVypDeN78YkT8AKHIjX8eFcuOWz2JQFT3KCcj72tL5uwRLtqK4H5xOOMn7KP72u4fUh75rbp5LpwAwPDn6fuhLBzHDWAhOk_kEBl5XWRU6d5_aAUDuaHD_SMQsjjQSgwps5BdbXO05DXTAsJEE2P25mFmfMOyR1JDKklmgGJyG0MgMli4q-TQyZPGqpEGfiZf-_uKLU71sbOC8IKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فناوری_هوشمند،_جنگ_را_به_انتخابی_احمقانه‌تر_تبدیل_می‌کند.pdf</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/17021" target="_blank">📅 10:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17020">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بازسازی کشورهای عربی با پول بلوکه شده ایران!  رویترز: واشنگتن دارایی‌های مسدود شده ایران را برای حمایت از بازسازی و تعمیر خسارات در اختیار متحدان خود قرار خواهد داد.</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/17020" target="_blank">📅 10:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17019">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOj8yxihRYWEDRFNIEVfbzIaoLAWDVGnW3e2UEwV20IT23Ded-3n5_L9XLeExb2a082VLJqTJxYzZ1LnGPPikmxZQ7VkD0EsZlYf7EODEswAfLAwI9k9K2fbUTyLP_UY-hp2ytymFUF2edZrWVwVJ8AZxKyVli_eWUKhx8XbFGx0AVn6Gh6nGGQVka9bCok4PYqdYW9TxsF73AdNd-F5tNwGJHKozkdzhC_FslxEIIvBZjBvIN2ct_CcgxonuCWF7aSBi1emMXuDPqw-73sFZNmUWhvrWPRdLAOE4wl3IsvbOh0BVOHWA2AXFyA9fVo-1sHMH8VLPHxKUzWVgxbxvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازسازی کشورهای عربی با پول بلوکه شده ایران!
رویترز: واشنگتن دارایی‌های مسدود شده ایران را برای حمایت از بازسازی و تعمیر خسارات در اختیار متحدان خود قرار خواهد داد.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17019" target="_blank">📅 08:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17018">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گزارش های اولیه از حمله آمریکا به مناطقی در جنوب کشور</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/17018" target="_blank">📅 07:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17017">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گزارش های اولیه از حمله آمریکا به مناطقی در جنوب کشور</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17017" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17016">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">باراک راوید خبرنگار اکسیوس:   دو منبع آگاه به جزئیات به من گفتند که معاون برکنار شده‌ی رئیس موساد، یک سال پیش بودجه‌ای به مبلغ یک میلیارد شِکل (حدود ۳۵۰ میلیون دلار) و تیمی متشکل از صدها نفر برای پروژه‌ی سرنگونی حکومت ایران دریافت کرد!</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17016" target="_blank">📅 01:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17015">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تبدیل ایران به یک دولت شکست خورده (Failed State) پلن B اسراییلی ها بود که ثابتی نیز به همین اشاره می‌کند   پلن A اسراییل، تغییر رژیم و کمک به روی کار  آمدن یک دولت غربگرای حامی اسراییل بود که فعلا شکست خورده است.  در این صوتی طولانی که ۸ ساعت پیش از آغاز جنگ…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/17015" target="_blank">📅 01:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17014">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uU3SLTX0V2gxrvZ2VgWonQCiVU1otCzLAQOYS-sQMkPsyvkWityYcF4z1OqOd7RshGcVTt4pPgsOq9mVVNZCEg1Y8HsU2YPlqS8Q_T1gx4PAo6tNbqsuBio3A9nizsfnHl-AYbKknEOvn_OBY0sXlD83iSksn2p_Mbn7aJbuC1on-siCoJXdTsgCP2Y60omNcP42z2UFrmB2XH7pBrNhARQ-fUb0c0SIOkW-99qmp2O_CuHZV871_QPxVE_HmwF920dE4aiAl1Q0Oh_klN8O5SfL4CJYBC86OtFP06jhRidNH01_ijysESF2Oe7HFh14Bay7rPADBYvUPr4Pb3FJig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهش ثروت شخصی ترامپ به سطح 6.5 میلیارد دلار!</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/17014" target="_blank">📅 23:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17013">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">محمدجواد لاریجانی: رفتن آقای قالیباف به اسلام‌آباد غلط بود و هزینه‌ای بزرگ بود
▫️
ترامپ معتقد بود برجام کافی نیست برای همین آن‌را پاره کرد تا امتیازات بیشتری بگیرد.
▫️
دلیل آنکه آن‌ها در میانه مذاکرات حمله می‌کنند آن‌ است که ما وقتی مذاکره می‌کنیم به آن‌ها سیگنال می‌فرستیم که می‌توانیم با آن‌ها کنار بیاییم و برد-برد کار می‌کنیم که آن‌ها فکر می‌کنند اگر بیشتر فشار بیاورند، امتیازات بیشتری می‌گیرند.
▫️
نخست‌وزیر پاکستان، آدم خوبی است، اما لازم نیست ما و آمریکایی‌ها را مقابل هم قرار دهد تا مذاکره کنیم، باید میانجیگری بلد باشد.
▫️
اگر ما بخواهیم خودمان با آمریکا صحبت می‌کنیم نیازی به میانجی‌ نداریم. /صداوسیما</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17013" target="_blank">📅 23:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17012">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نخستین سند قطعی دال بر خودکفایی کامل کشور در تولید تریاک</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/17012" target="_blank">📅 22:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17011">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">▪️
خبر این است: وزیر کشور پاکستان پیش وارد تهران شد  مایلم یکبار دیگر صراحتا هشدار بدهم که ابداً نباید حسن نیت داشتن پاکستان را پذیرفت؛ پاکستان یکی از فاسدترین کشورهای دنیاست که توسط یکی از فاسدترین نظامیان دنیا اداره میشود. نظامیانی که وابسته سعودی، آمریکا،…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17011" target="_blank">📅 21:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17010">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دقت کرده اید هر کسی میانجی این جنگ بی پایان ما با آمریکا و اسرائیل شد به خاک رفت؟!  راند اول قطر میانجی شد و همان روز ایران به قطر حمله کرد و چند ماه بعدش اسرائیل هم به قطر حمله کرد و در جنگ اخیر هم با حمله موشکی وحشتناک ایران به تاسیسات گازی راس الفان، بیشترین…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17010" target="_blank">📅 21:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17009">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqEz3Z7kixg5gmFcIRi7LcyK3JWHPdj6SiQH0lRRuyrdX3GGfAiCN0ucSLyXRjyakNBEMyhgwH00XlyabyMUJ4d8eL0j63EE4pe8D5zUFVhwGItS0a_7KE61idx8K6D2iW8JznkfRJsdiVIgBjcca8g23VMsXuo2b4VWMOYB2gcrrim739n7mlE33Nyqa6rWk-yUlm-nwiFhbh-VtIF1uSY2oNWbXYDCi35X_YuNmJdI4TYys4NR3gDq944yjFHoP3IUHoOgq_1anG1HyACLm433k_C6JIQNzWjhd6h5WD5YIg1fZfUlSj4OIdprfc84AnQMBmqqQNzOTNIg8BgT1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ایران در سال ۲۰۲۶ با یکی از شدیدترین فشارهای صادراتی خود در سال‌های اخیر روبه‌رو شده است. داده‌های منتشرشده توسط شرکت ردیابی نفتکش Kpler و منابع تخصصی بازار انرژی نشان می‌دهد که از زمان آغاز درگیری‌ها و تشدید محدودیت‌های دریایی در اواخر فوریه، توانایی…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17009" target="_blank">📅 20:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17008">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وزیر کشور پاکستان، محسن نقوی، برای دیدار با مقامات ایرانی از جمله وزیر امور خارجه عباس عراقچی، وارد تهران شده است.
— خبرگزاری تسنیم</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17008" target="_blank">📅 20:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17007">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تروریستهای ازبک دولت الجولانی را تهدید کردند   گروهی از تروریستهای جهادی ازبک با انتشار بیانیه‌ای دولت سوریه را به اعمال فشار علیه خود و تهدید به بازداشت و اخراج از سوریه متهم کردند.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17007" target="_blank">📅 20:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17006">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">من بعید نمیدانم در این سفری که علامه جولانی به آمریکا داشته ، به پیشنهاد عربها از ترامپ دستوری جهت اخراج این وحوش اویغور و اوزبک و چچنی و … دریافت کرده باشد</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17006" target="_blank">📅 20:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17005">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIXhvo6czSzRCxxuKxHW_UtuUHtfhFAJPWdWW0qV0lmqTEBdL-BtvY1Vtvrw8ZCtv0QxyxifOdQCNZobNH01Cp8j6cMxTpqL6NzbwPfxjMv73Xo3ILlsw3obBampOBUjGMRqqM3QqKJ5NW_nEY5rrCw5PQhAslryoWXARu9qZ0yMPAdPYMfYO2hzi3mr-wczYmrKBaZHYg67mdYLOaKmT9lk4JKaWkZ0GMlR4-OwgGiLLgo3BNa7Kt-9H8bzZ9W2YZSmUJlZaLVFAOSOmaBmSqgUf0rkV3PwAzDBiFMQjbvXdZ4tCfnbXfekYQDj-sgBlk158NgauvcKChkdTRWP6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا چرا غیرقابل دانلود؟!</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/17005" target="_blank">📅 20:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17004">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">شما ببینید وضعیت این منطقه گه گرفته چطوری است که پاکستانی که خودش در‌ همین مدت در غرب (بلوچستان)، شمال (وزیرستان) و شرق (هند) غرق در تنش و نکبت بوده حالا دارد برای ما میانجیگری می‌کند!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17004" target="_blank">📅 19:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17003">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پیروزی اوکراین با ربات ها و هوش مصنوعی !؟  در سال‌های اخیر، روایت حاکم بر جنگ روسیه و اوکراین حول محور بقای کی‌یف در برابر ماشین نظامی مسکو می‌چرخید. با این حال، شواهد میدانی و مواضع تحلیل‌گران غربی نشان می‌دهد که ورق به سود اوکراین برگشته و اکنون صحبت از…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17003" target="_blank">📅 18:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17002">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGpii4QUquOH5H_WwmhO2wtVkUo147yTMgIHBF8GZjVuuUOWRnwlizKDAEUeSaYBPMHQFkvzxOxgU4UJIC838thl5ZCN5EmoDnp_BDcNAHQf8_vcmu_Yeilorb50tTis3ZCSlqN1JweBTFrQRJDnAZA_TjMLAHud7wApwsrWyvet7tuUdjbR6jlQQrAxheZYeNF64yN_5T7zbdNFNeu4eaaEAb8QxwrSfXkVe-jUFVueDyTEW54-qZpPTmim6MLKs4qPvLocmXP5WiCR5xb0DheqlkxLdsliPiuh_ZkhGP9GbVRjyzbRlxc889SzLiKbSAWh7CkZEyu1kA9ZSnpWtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
ربات ها درحال بازنویسی چهره جنگ امروز
♦️
رباتیک در میدان جنگ به عنوان نظامیان  برای کارهایی که بیش از حد معمول خطرناک، تکراری و یا با پیچیدگی خاص برای انسان است بکار میروند.
🔸
از هواپیماهای بدون سرنشین، عرضه به تانک های خودمختار به تانک های خودمختار، روبات…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17002" target="_blank">📅 17:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17001">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔻
برخی شنیده ها حاکی از تلاش گروهی از نمایندگان مجلس برای استیضاح وزیر ارتباطات به جرم اجرای دستور رئیس جمهور و بازگشایی اینترنت می باشد</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/17001" target="_blank">📅 14:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17000">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">📡
اینترنت پاکستان ، به دلیل اعتراضات مردم علیه حکومت ، در آستانه خاموشی قرار دارد</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17000" target="_blank">📅 13:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16999">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✈️
پاول دوروف ؛ مالک تلگرام
:
فیلترینگ و محدودیت‌های اینترنتی، روسیه را به «حاکمیت دیجیتال» نزدیک‌تر نکرده، بلکه از آن دورتر کرده است.
به گفته دوروف، متخصصانی که می‌توانستند در روسیه سیستم‌عامل موبایل بسازند، به‌دلیل وضعیت خراب اینترنت، در حال ترک کشور هستند
او تأکید کرد تا زمانی که گوشی‌ها بر پایه سیستم‌عامل‌های آمریکایی مثل iOS و Android کار می‌کنند، حتی اپلیکیشن‌های «ملی» هم در برابر نظارت و سانسور از طریق بک‌دورها و فروشگاه‌های اپلیکیشن آسیب‌پذیر می‌مانند
دوروف این سیاست را «تغییر بسته‌بندی بدون تغییر اصل ماجرا» توصیف کرد و کنایه زد: مسئولی که به نام حاکمیت دیجیتال، اینترنت روسیه را خراب کرده و کشور را دهه‌ها عقب برده، شایسته دریافت مدال امنیت ملی از آمریکاست</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/16999" target="_blank">📅 12:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16998">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDhgRkW3QtVyVyYjL604Pz8cTqM_Mvz4T4kle-hkhCHt-3fRfEAJ9X8rgpCjq6j49vs0dBCuIImn-U6B3QKMJboKSmlmlN9ojnolF_g_sO4KvWH4HEnb-BjvwD8ljF8Rp0UjCyo7syMJHKHzvUSxCZ1Cu7_s6Ztw7vG6MHhPO6GfODsULNG-UfyOPScLzy2nZhSM_0lSOPf83gGAiYvGaUSQ53I5QKfFa1aCpOH515LaqC7E-Dh7dw_wsNjDRK6VIcJBd7GHB2HDAj4k5wX4ICUaSsqgUMpeKcH9DupQNw1pkn9jIgBga1sHrZGsaphqsoA5tnwUKejEvxK_DFFn6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
اینترنت پاکستان ، به دلیل اعتراضات مردم علیه حکومت ، در آستانه خاموشی قرار دارد</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/16998" target="_blank">📅 12:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16997">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">این یعنی نه ایران و نه روسیه از این جهش بهای نفت حداکثر استفاده را نبرده اند؛ ما به دلیل محاصره دریایی آمریکا صادراتمان افت کرده (پست ریپلای شده را ببینید) و روسها هم به دلیل حملات سنگین پهپادی اوکراین.  عربها هم که عمدتاً ضربه دیده اند و لذا بزرگترین منفعت…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/16997" target="_blank">📅 11:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16996">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ارتش لبنان اعلام کرده است که چندین نفر از پرسنل نظامی، از جمله یک افسر، در حمله هوایی اسرائیل که یک خودروی نظامی را در جاده الخالدیه–نبطیه هدف قرار داد، کشته شدند.  بر اساس گزارش‌های رسانه‌های لبنانی، این افسر دارای درجه سرتیپ بود.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/16996" target="_blank">📅 11:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16995">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ارتش لبنان اعلام کرده است که چندین نفر از پرسنل نظامی، از جمله یک افسر، در حمله هوایی اسرائیل که یک خودروی نظامی را در جاده الخالدیه–نبطیه هدف قرار داد، کشته شدند.
بر اساس گزارش‌های رسانه‌های لبنانی، این افسر دارای درجه سرتیپ بود.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/16995" target="_blank">📅 11:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16994">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دقت کنید که سنتکام می‌گوید که دوباره «سایتهای راداری نظارتی ساحلی ایرانی» را در گروک و قشم زده اند!  پیشتر اشاره شد چرا مهم است.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/16994" target="_blank">📅 09:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16993">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فرماندهی سنتکام:   چند لحظه پیش، نیروهای مرکز فرماندهی مرکزی چهار پهپاد تهاجمی انتحاری  ایرانی که به سمت تنگه هرمز پرتاب شده بودند را سرنگون کردند.   پهپادهای ‌تهاجمی تهدیدی فوری برای ترافیک دریایی منطقه ایجاد کرده بودند. نیروهای آمریکایی پس از آن به سایت‌های…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/16993" target="_blank">📅 09:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16992">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فرماندهی سنتکام:
چند لحظه پیش، نیروهای مرکز فرماندهی مرکزی چهار پهپاد تهاجمی انتحاری  ایرانی که به سمت تنگه هرمز پرتاب شده بودند را سرنگون کردند.
پهپادهای ‌تهاجمی تهدیدی فوری برای ترافیک دریایی منطقه ایجاد کرده بودند. نیروهای آمریکایی پس از آن به سایت‌های راداری نظارتی ساحلی ایرانی در گروک و در جزیره قشم برای دفاع در برابر حملات بیشتر حمله کردند.
نیروهای آمریکایی همچنان هوشیار هستند و برای پاسخ به تهاجم بی‌دلیل ایران در چارچوب دفاع از خود آماده‌اند.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/16992" target="_blank">📅 02:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16991">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUHunhWpAlcU5RWcMb9OUp_MY345y42Th-G6D8fFwk9PdZCBTlSIi4FAEjzUPAq6-R-9f44mNqAoQ5_sEWtw2g0htG-00d6h44fWkZKIsXiP55RrfZqspLdO-HtboYdpwM1YMECKE-vsVs25V-Iv-MxTxB7k792rQpcpnIup6Fz8bKwcFGYy9OT5tW6XHlc2XtIq_Tb3PV_TapMY-YbtY-06TFKKccLs66sz3Zt4JW8rpAHLSQkyXk-iCZCkkWJjG7PORIh1jEq-qG2eMESonnba5glZGezUo3PeZSU64z37pOzq8cFfhVKrdtCyCbWlrqgGxMjGqfLk6gp1CRC-iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضرات مداوماً از جهش تورم در آمریکا سخن میگویند و آن را سند موفقیت خود میزنند!
این هم تورم مواد غذایی در کشور خودمان!</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/16991" target="_blank">📅 00:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16990">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فوری | ترامپ: در مدیریت پرونده ایران موفقیت بزرگی کسب خواهم کرد</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/16990" target="_blank">📅 23:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16989">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فوری | آکسیوس، به نقل از منابع: واشنگتن منتظر پاسخ رسمی ایران است و اختلافات باقی مانده را نسبتاً محدود توصیف می‌کند.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/16989" target="_blank">📅 22:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16988">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فوری | آکسیوس، به نقل از منابع: واشنگتن منتظر پاسخ رسمی ایران است و اختلافات باقی مانده را نسبتاً محدود توصیف می‌کند.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/16988" target="_blank">📅 22:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16987">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">فوری | اکسیوس، به نقل از دو منبع: اختلافی بین واشنگتن و تهران بر سر اندازه و زمان‌بندی آزادسازی وجوه مسدود شده.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/16987" target="_blank">📅 22:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16985">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
محسن رضایی در گفت‌وگو با سی‌ان‌ان:
🔹
اگر ترامپ مذاکرات را جدی بگیرد، ۲۴ میلیارد دلار برای آمریکا مبلغ زیادی نیست.
🔹
اگر او می‌خواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتمادی است که ایران می‌خواهد به طرف مقابل داشته باشد.
🔹
این آزمونی…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/16985" target="_blank">📅 21:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16984">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
محسن رضایی در گفت‌وگو با سی‌ان‌ان:
🔹
اگر ترامپ مذاکرات را جدی بگیرد، ۲۴ میلیارد دلار برای آمریکا مبلغ زیادی نیست.
🔹
اگر او می‌خواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتمادی است که ایران می‌خواهد به طرف مقابل داشته باشد.
🔹
این آزمونی است که آمریکا باید از آن عبور کند و راه باز خواهد بود. این پول ماست، نه پول آمریکا.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/16984" target="_blank">📅 21:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16983">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دستیار ایرانی به سی‌ان‌ان گفت دیدار خامنه‌ای با ترامپ رخ نخواهد داد</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/16983" target="_blank">📅 19:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16982">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رضایی ایران هشدار داد که اگر آمریکا درگیری را از سر بگیرد، ایران «جنگ را» فراتر از خلیج فارس خواهد کشاند -</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/16982" target="_blank">📅 19:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16981">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کاخ سفید:  دیدار عراقچی- ویتکاف  گفت‌وگوی مستقیم ویتکاف و عراقچی در مسقط    «استیون ویتکاف، فرستاده ویژه ریاست‌جمهوری آمریکا، به همراه آن اسکاروگیما، سفیر آمریکا در عمان، امروز در مسقط با دکتر عباس عراقچی، وزیر امور خارجه ایران، گفت‌وگوهایی انجام دادند؛ این…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/16981" target="_blank">📅 18:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16980">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گروسی:   ایران و آمریکا به توافق نزدیک شده‌اند</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/16980" target="_blank">📅 18:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16979">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گروسی:
ایران و آمریکا به توافق نزدیک شده‌اند</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/16979" target="_blank">📅 17:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16978">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ایران دارای یکی از بزرگترین ناوگان های نفتکش دنیا بود اما با این وضعیتی که پیش می رود باید از شوتی های زحمتکش مرزهای شرقی و جنوب شرقی کشور برای انتقال نفت بهره ببریم!</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/16978" target="_blank">📅 16:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16977">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">Yinon_Plan.pdf</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/16977" target="_blank">📅 14:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16976">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">امیرحسین ثابتی:   آمریکا بعداز جام جهانی سنگین‌تر به ایران حمله خواهد کرد  ایران را تبدیل به غزه دوم خواهند کرد.  باید پیش‌دستانه پتروشیمی‌ها و زیرساخت‌های منطقه را بزنیم.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/16976" target="_blank">📅 13:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16975">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ایران_جنگ_را_برنده_نشد،_بلکه_چیز_خطرناک‌تری_را_به_دست_آورد.pdf</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/16975" target="_blank">📅 13:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16974">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3R_zoZKf8vFmzIiPX3j38z6mEx4X9-KP5VMwkh9uK8bsYr8vg2OwbtxknBdH9kiXiQ5DENPMDHrvb-HUgw7Asf2DG-dwPEILKz0TjfNFjEb1PyxR8EVsGJTEKD14J4c1hVVtvc79mq9OG-LZuCCYdT5OxyJJSx1ohxJ3epoROjWNkCO046OfZ4UbWr3f_ZzXIOa_6UmUB00y78h6dt3begy17cvcuSNRxdaZ0w8gWk5Ac7MxVW-qj-2Rnmi9XwbD9XPv02L72nYpVda7FZC3m6QLqLFOMNnvJ1zYXxH3mgXHtS5WV-z2_n57k-2Ukp9BituEBwWOZ3fY2BNAm3ATg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدرسگ ها چه اسم هایی برای بندرشان گذاشته اند!  بعد انتظار دارند حمله نکنیم!</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/16974" target="_blank">📅 13:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16973">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">عمان پس از انفجار در بندر فهل، بارگیری نفت را متوقف کرد  سلطنت عمان بارگیری نفت در پایانه بندر فهل در خلیج عمان را به طور موقت متوقف کرده است. به گزارش رویترز، دلیل این امر انفجار در منطقه بندر است.  بندر فهل یک نقطه صادرات اصلی نفت خام عمان است. اختلالات…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/16973" target="_blank">📅 13:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16972">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دقت کرده اید هر کسی میانجی این جنگ بی پایان ما با آمریکا و اسرائیل شد به خاک رفت؟!  راند اول قطر میانجی شد و همان روز ایران به قطر حمله کرد و چند ماه بعدش اسرائیل هم به قطر حمله کرد و در جنگ اخیر هم با حمله موشکی وحشتناک ایران به تاسیسات گازی راس الفان، بیشترین…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/16972" target="_blank">📅 13:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16970">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kJ83Cgi8ICioXpfkA9IUPnTFYOsolRXQ2ZWq_HQRNaVbKSjE6B9FYDjVB1i0Otg_oHRhFa0N1YWSDE3G0soHsQWRpmzFKC73FTaXfDKdI1mPuO-AKrudbEQKfHcWb8PVbUllZyeEDbV0EAWHwz2hu1WHLiu_3osP0VwDsGq3nR3iEMWYETvs6PG7ZAQmSnf6T-JBkSvxB0wVXXu_90a-6IfaqJFBr_l1Nt27aM87pYXqFALx7G4D5aHM9KjFYsAh5HmvnM_GuWuPeQS-mhXQhyXYNH76TOkwSn5v6BJ_bJ-rZkuWcuzabeAC6IW8kafjDQA8Ak5GwXLQQ0qlhK7QMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TgzlzIMIJcp0WKitQolKcttiMus5AIbGZkhM_Ud5rrinhgCT7-KxdI_S6Ax5Ofmuutx-XOxo0QbLj5R-TCClWybmcGVTsqej0NGyW-KXhnPvtnGaMgvzDAPvaEbSoWJjzW4OZPGF4D9NELOExV4AZxokz0U8hUzHqvBLwYaS4o5X2c23U7E2DmxyHmBlRTRgKVIRElatE-L4pREySQ39CMsW3TH7aE6CDBnY6Tf3KgEQ7NzLS4wQ_uKT2Gy5r3Jku9uAWnCKncW-FYYV1c5O-xDtS6liU5_qXJsiCZk5CA5PzPD_H3RlQkYi5QHd_qn7M_ZlTYDYl8LXtgS_lGatWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به نظرم با خر یوگا میکردید بهتر بود ولی خب</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/16970" target="_blank">📅 12:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16969">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اکنون ثابت شده که باکو میزبان گروه های تکاوری و جاسوسی اسرائیل در حین جنگ بوده اند، منتهی دولت پوزیده صرفاً به استمالت از آنها ادامه داده و حتی یک موشک و پهپاد به تاسیسات آنها برخورد نکرده است.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/16969" target="_blank">📅 11:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16968">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">این پوزیشن را دیروز به همراهان پیشنهاد دادم.  کماکان بر این باورم که خریدها سبک باشد و کسانی که سنگین کریپتو دارند این فرصت خروجشان است.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/16968" target="_blank">📅 11:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16967">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvdOlrJq4uOQmRFaqMWuDGNP7iwBzSic022LUJp7P64AMv-MPLDmXiAPfIAce4ZDuAgXhLy9Bz6zJ0ac7RgvtzggaDYljZxgQnvMCeQSkePFMUkeRr_NiaJE9a9OVfcvWsCVScG_rhBU6qk0vKwd5hfUDLaN-dUhDsJv--nQrx2Yg1CuLg0W1LjZpAO06udcK4UCiVmowTLr-r5Z8_qsqKkCPWY9DxSQiFp0ssVfS8jqOfxqALzG4wHqIX4G1Lib1KDJRz2SNkyYsp-poz1DMYNEsgskHcn2eMobLV1RKy52MlYoyocjv0HYd0ZW0z30Tkzt9mQkbRIlUX1ZhasLZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری باکو بین ۵۰ تا ۶۰ درصد از نفت اسراییل را تامین می‌کند و میزبان بسیاری شرکت‌های نظامی و امنیتی اسراییل هم هست اما تا کنون از ضرب حملات موشکی و پهپادی سپاه به دور مانده است.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/16967" target="_blank">📅 11:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16966">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ایران_جنگ_را_برنده_نشد،_بلکه_چیز_خطرناک‌تری_را_به_دست_آورد.pdf</div>
  <div class="tg-doc-extra">232.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/16966" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این‌گونه_دکترین_نتانیاهو_برای_ایران_فروپاشید.pdf</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/16966" target="_blank">📅 11:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16965">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دورویی اروپا در قبال اسرائیل: محکومیت‌های کلامی و خریدهای میلیاردی سلاح
اروپا این روزها در قبال اسرائیل دو چهره متفاوت به نمایش می‌گذارد: چهره‌ای سیاسی که با محکومیت‌های پرسر و صدا و قطعنامه‌های نمادین، خود را مدافع اخلاق و حقوق بشر معرفی می‌کند، و چهره‌ای نظامی که در سکوت، میلیاردها دلار سلاح از همان کشور می‌خرد. سیاستمداران اروپایی با برگزاری کنفرانس‌های مطبوعاتی و رای دادن به تحریم‌های نمادین، سعی دارند تصویر یک قاره متعهد به ارزش‌های انسانی را به نمایش بگذارند، اما در پشت پرده، ژنرال‌ها و مسئولان نظامی با امضای قراردادها، واقعیت دیگری را رقم می‌زنند.
در ۲۶ مه ۲۰۲۶، شرکت البیت سیستمز اسرائیل اعلام کرد که سفارشات معوقه‌اش برای اولین بار از ۳۰ میلیارد دلار فراتر رفته است؛ رقمی که حتی پنج سال پیش هم غیرقابل تصور بود. در میان این اعلامیه، قراردادی ۱.۴ میلیارد دلاری با یک کشور اروپایی ناشناس برای مدرن‌سازی نظامی در حوزه‌های زمینی، هوایی و جنگ الکترونیک به چشم می‌خورد.. این در حالی است که کشورهای اروپایی با صدای بلند، صادرات سلاح به اسرائیل را متوقف کرده‌اند، تحریم‌های جزئی را مطرح می‌کنند و شرکت‌های اسرائیلی را از نمایشگاه‌های دفاعی اخراج می‌کنند.
اسپانیا صادرات سلاح به اسرائیل را متوقف کرد، چند کشور عضو ناتو تحریم‌هایی را پیشنهاد دادند و البیت سیستمز پس از اعتراضات از نمایشگاه یوروناوال فرانسه اخراج شد. اما در عمل، همین کشورها در سکوت، به خرید سلاح از اسرائیل ادامه می‌دهند.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/16965" target="_blank">📅 10:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16964">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqLBNPJI460W8B8KIOr-24FqhWlv7Vftz6BkmBDBcQIiV8opbMzRYAla5SCoxzCEolKZ4GWV9n6rdhaq0JDOCOgMG7zp0EqvQWelLQP2lAixEQIPNDZyKl-X44vyrwXxwhA9ynlszZ6zWnGsEeXAOdfKqlcp_GQFCnMoEs825Ugem3zdoalNP_kznltNIxoloG2Q3wKcxlVe1wclSTYnyVK4yk7ZBf8OimDGP62pzA4kegp03Z-soOH9bbczqsZNclBkWzXvME2jW1EEiEbgpQuPE8JDik5HpITHUwRQ1TwSBYsGBJ0JbvtcKTOGwq_MqLNHsfeZXRJmRwHHbo3njA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشتر گفته بودم که یکی از انگیزه های اسراییل از تعقیب پروژه تغییر رژیم در ایران ایجاد یک کریدور داوود بزرگ است که او را از امتداد آویزان بودن به آمریکا برای تامین امنیت ملی اش بی نیاز کند.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/16964" target="_blank">📅 10:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16963">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">به گزارش بلومبرگ، بریتانیا و فرانسه تقریباً طرحی را برای اجرای عملیات مین‌روبی در تنگه هرمز، پس از توافق احتمالی بین آمریکا و ایران بر سر آتش‌بس دائمی، نهایی کرده‌اند.
این طرح یک تلاش چندملیتی خواهد بود و پس از بیش از یک ماه نشست‌های چندجانبه به رهبری دو کشور انجام می‌شود.
به گفته افراد مطلع از این طرح، این عملیات شامل ۱۵ کشور خواهد بود که پرسنل نظامی و تجهیزات خود را به مأموریت اختصاص می‌دهند و برای جلوگیری از درگیری، ارتباط مستقیم با ایران حفظ خواهد کرد</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/16963" target="_blank">📅 09:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16962">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">خواننده Secret Box از یک سال پیش آگاه بود که دلیل زدن هوانیروز و پایگاه ها و پاسگاه های مرزی ارتش و سپاه در مرزهای غربی، گشودن فضا برای ورود نیروهای مسلح کرد به داخل کشور بود.  اما چرا این طرح آن گونه که باید و شاید عملیاتی نشد؟!  بخوانید:   موساد سلاح‌های…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/16962" target="_blank">📅 00:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16961">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بشدت به همین سناریو که 2 ساعت پس از آغاز جنگ اشاره کردم، ایمان آورده ام. تقریباً تردیدی برایم نمانده که مدل «فروغ جاویدان» صدام را این بار نتانیاهو با پژاک و گروههای مشابه ش میخواهد اجرا کند.  نکته بدتر اینکه در صورت موفقیت این طرح و با ورود نیروهای شبه نظامی…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/16961" target="_blank">📅 00:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16960">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">محسن رضایی:
امیر قطر و ولیعهد عربستان دارند خودشان را با واقعیات تنظیم می‌کنند اما امارات، بحرین و کویت همچنان فکر می‌کنند قدرت آمریکا مثل قبل خواهد بود. این‌ها فکر نکنند که اگر این روش را ادامه دهند ما بعد از جنگ رهایشان خواهیم کرد. اگر امارات و کویت با صهیونیست‌ها همراه هستند باید ابوظبی و بوبیان را به عربستان و عراق بدهند!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/16960" target="_blank">📅 00:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16959">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJbRdtJ90y961uPRoR9i97EQkCgrFLqcUUvnR-JW83lh4n9Dklv2X_L-an_QNMCo5TxS4n7sLnId2uJYN-JWQz25QbfVjUbxdNtwcOxsa58uZ4CTwrexg5YuaLMJ7v2ItsphyirG0XO4UTrgR_qTS6W1VcBgq85xARuC9R2bJ6fTyB-4qUo7vza_AiJRUGhV3Zghwhf97gsI6NtCSt8m2fWJXzNokJ6vqTmSksjdxz31VDyXoQdofhAcQJWow2e1ecIhTNpaciV6PYIPda6eokw_LSoXPNFvi-omeELG-SDAgdgSNtV1vBed470dMl6XU0nAdMrOYzpf1V0s6a7tRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یعنی نه ایران و نه روسیه از این جهش بهای نفت حداکثر استفاده را نبرده اند؛ ما به دلیل محاصره دریایی آمریکا صادراتمان افت کرده (پست ریپلای شده را ببینید) و روسها هم به دلیل حملات سنگین پهپادی اوکراین.  عربها هم که عمدتاً ضربه دیده اند و لذا بزرگترین منفعت…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/16959" target="_blank">📅 21:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16958">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ایران و روسیه یک تفاهم‌نامه همکاری به ارزش ۲۵ میلیارد دلار در بخش هسته‌ای امضا کردند - تسنیم نیوز</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/16958" target="_blank">📅 20:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16957">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رویترز:   روسیه برای اولین بار اذعان کرد که تولید نفت این کشور در سال جاری کاهش یافته    این اعتراف در زمانی مطرح می‌شود که اوکراین در ماه‌های اخیر حملات پهپادی و موشکی خود را به تأسیسات انرژی روسیه تشدید کرده . آژانس بین‌المللی انرژی تخمین زده که تولید نفت…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/16957" target="_blank">📅 20:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16956">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">صنعت نفت ایران در سال ۲۰۲۶ با یکی از شدیدترین فشارهای صادراتی خود در سال‌های اخیر روبه‌رو شده است. داده‌های منتشرشده توسط شرکت ردیابی نفتکش Kpler و منابع تخصصی بازار انرژی نشان می‌دهد که از زمان آغاز درگیری‌ها و تشدید محدودیت‌های دریایی در اواخر فوریه، توانایی…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/16956" target="_blank">📅 20:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16955">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4fK7N4-cTGkcWozzQ7Nf-YfPlD8isTxGf3hPNUJh07mQgaoZacoFGjGCzeMMxgD2tkG-AUsBlhEoAV7nCY7eis0erm5nokmku6S7Is4TYG0QmJsAgWOWejUOFcWsjEsdS_zwE4o0QJrf-TVdGXNhhld8hGocA10mdT3jfzl2KQ6vyx8ie4tL85_tSZhwJ103TDzj1PgGYVdVZpfHC3BGY-ls11ukb1F4XvtPKIuh_MpGgTQCX6QBSmuGZ-VvNTNFODmGbZpLUiIh0T8Ze91o9PtovlAV0iXI4lPywyeD6M2hgZVwFVtqqsJe_uzVLt_lvdPIFSTCgWj4a4hVfFkQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:   در حال حاضر، ما کنترل کامل ۶۰ درصد از نوار غزه را در دست داریم و دستور من رسیدن به ۷۰ درصد است... ابتدا ۷۰ درصد. از همان شروع می‌کنیم</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/16955" target="_blank">📅 19:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16954">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حالا اینجا همه حضرات میگفتند ترامپ دست خالی از چین برگشت!</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/16954" target="_blank">📅 19:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16953">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔥
ثمره دیدار ترامپ و شی/ سپر چینی جلوی جهش قیمت نفت را گرفت
🔹
فایننشال تایمز نوشت که کاهش ۴ الی ۶ میلیون بشکه‌ای واردات نفت چین و استفاده این کشور از ذخایر نفت خود، منجر به کاهش تقاضا در بازار نفت و کاهش قیمت شده.
🔹
خاویر بلاس خبرنگار بلومبرگ می‌نویسد که…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/16953" target="_blank">📅 18:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16952">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-REMJSQNHicQ3yNETh7yBO8LCBKWqz2LA8TlNRmAvIKA9ngP5MFIvIMVULWRIKKzyPK9UZcI72OjiHRH9tQe-pjlC3iA8JVRBVyMMYu7MtSe-6lt7o-fmCUqQvlgjwL9eFY19AxhGEzS0NJgt6jmff2aGuJsWPb0FCq8LWOFkGShCAnHLfpPuLg-36ECcBzscFEFhhHAlAcOnBOwKoB5jhX-n3ZYSDiNHWzrn6RcqKlKNBMxOzUbv_Hn9KAh777zu79wD4-pml3gqCEoNjLFP0N5H8ozOQaHfnK7YPWU1FPcqOFRPAJfm73A1Vumm-OP607P8x4om7vXMbqejQxLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ثمره دیدار ترامپ و شی/ سپر چینی جلوی جهش قیمت نفت را گرفت
🔹
فایننشال تایمز نوشت که کاهش ۴ الی ۶ میلیون بشکه‌ای واردات نفت چین و استفاده این کشور از ذخایر نفت خود، منجر به کاهش تقاضا در بازار نفت و کاهش قیمت شده.
🔹
خاویر بلاس خبرنگار بلومبرگ می‌نویسد که اگر چین واردات نفت را کاهش نمی‌داد:
۱- قیمت نفت خیلی خیلی بالای ۱۰۰ دلار می‌رفت.
۲- فدرال رزرو مجبور به افزایش نرخ بهره می‌شد و وال استریت کاملاً نابود می‌شد.
۳- رئیس‌جمهور ترامپ در مذاکرات با ایران کاملاً تحت فشار زمان قرار می‌گرفت.
🔹
به گزارش خط انرژی، برنامه دولت پزشکیان برای توسعه روابط با چین چیست؟
@khate_energy</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/16952" target="_blank">📅 18:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16951">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnMUK_JQv1FT9pRcOx8fAJuyhyiCNI_6RztO2Tk69DxrEdpmLIwQqRKBB-J5lw7UI8jpg6HzbeHC79UsymicczNwArKiFsG2G5vemAiabr6h6AkhneYtnnWNhvSr_-5GIdDFf1LmGdXf4agk-TW9agXqb21NyXHG_FN_Vi3YwntkQ5I8gf0EUcjWDMe1jHw-Kjmsf3t4X06Kj881l3HwqIsR9IGN80i96ppWQa3yVme0J-UWcrkGefMFa_j4ixpgWcVX9sD63uVwrzh_a5vAa0tCT-JjHFpaF5f2asTkLonZ81oamdTBdI3OdSXJ0OD2uIri-755hti3uoNiSmzEPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/16951" target="_blank">📅 17:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16950">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آژانس بین‌المللی انرژی اتمی (IAEA) اعلام کرد که نتوانسته به تأسیسات هسته‌ای ایران (به جز بوشهر) برای انجام فعالیت‌های راستی‌آزمایی میدانی دسترسی پیدا کند.
این موضوع نگرانی‌ها درباره خطرات اشاعه هسته‌ای را افزایش داده است.</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/16950" target="_blank">📅 17:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16949">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سپاه پاسداران:
شرط اولیه ما برای پذیرش آتش بس در جنگ منطقه‌ای، آتش بس در تمامی جبهه‌ها از جمله لبنان بوده است.
دشمن می‌بایست با فوریت حملات خود به مردم لبنان را متوقف کند، و سریعاً با تخلیه سرزمین‌های اشغال شده لبنان به پشت مرزهای بین المللی عقب نشینی نماید و تمامیت ارضی لبنان را به رسمیت بشناسد.
هیچ آرامشی در منطقه بدون عقب‌نشینی صهیونیست‌ها از مناطق اشغالی لبنان برقرار نخواهد شد
همه ما با تمام وجود از ملت لبنان حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/16949" target="_blank">📅 17:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16948">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUY5faTNcXpw0BysG4DSm7kHqPmSgeD9WvDZebWvj66mayAycIUluxcOYMu0Inhahppp9pRsIEk4d3Go6EI8wCiXm0rjpoOy4PrnZFW7hk1ReX0BHq8JG90J3ZWqV4vsgQ8ZPFu6Fw8RhVBJv0epDisr0SoQP0l-jqHzxbJ6ySMdQ9vwYgSxgAtwSaGKMyh9MUM13l99bDInW8DFhmlc4VsaClaxgku6mYaxsF6VrTIwvQhWjYRWmovU_8QT9RpWFRiYC7WndlxVBBNAox6cfmSWH_IzSJpTzmnuLxke0S4D7s_PRXwapmzIRjnehKB48NefSiHr3Qg4IUhSmLLnEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکونومیست:
تصویر روی جلد این هفته: «نسل جدیدی از سوسیالیست‌ها قصد دارند اقتصاد را با کنترل قیمت‌ها، مالیات‌های سنگین بر ثروت و موجی از ملی‌سازی‌ها دگرگون کنند.
این جریان که با خشم ناشی از غزه تقویت شده، با سرعتی چشمگیر در حال جذب رأی‌دهندگان است.»</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/16948" target="_blank">📅 16:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16947">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce28a3a45.mp4?token=GOgwRo6gIKuX53quKD8SLViLdskAAa91YEv-mqCyD6EhxJOWT4QPxhhFWy7Q5yFeMgX4stNWSIJZaZARaZzL7hYVZ-ahV1Ry3DhoDTxRDWig1s46-V7lOAavf_NMQxAWyofvl0MIlaq1SBXHRQYhA5VA5szTHwYDBfl4GYopBPJ94hoIB_-RZdrGeKbdWg-Eeya1IBtOFaaRGnjvaIWLhxiRaIq3HCURA0NGPJBp_pKwytrTuF6TStQn7fsUVnPX8gnGnLf_d29MGniwLAYgd-nafb-POqEsATWSTzEtV35hLtj0_Qrg9Egmzy0lPAGSYxvshIsWdJ91JzeMny5A9j4Z_qD3C_FOg0d-8t9VPOdeXNX7BKt6Sk13WK_fYxL1HF-Wp4fVIZY--Rr8I8HV__rOOQGFtb3ZT1hofQoLpHa7Jauz8KVZD-g--mLiA499Zn0n9IPCrDwIyVFp_65s1sUy6dSCLGcj_m4qUxiCT02BP5z38nl_Wqzqh_OqY5Wgbq8MY4kVydeqGoaVWNQt0Sw9C51EQpbOR2BxDOUbVy7FgcfGp5HCWEAD6UaUTrgC-Om-c0tJs_duWW5rHazfAobAzpf4le51XXLUQM9bv9WIMFYYPW3nSHplofSV3OLhJSBRg7_Z9z4yqINNnP0fTrRtebCtDxFJuZDDYCo3mnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce28a3a45.mp4?token=GOgwRo6gIKuX53quKD8SLViLdskAAa91YEv-mqCyD6EhxJOWT4QPxhhFWy7Q5yFeMgX4stNWSIJZaZARaZzL7hYVZ-ahV1Ry3DhoDTxRDWig1s46-V7lOAavf_NMQxAWyofvl0MIlaq1SBXHRQYhA5VA5szTHwYDBfl4GYopBPJ94hoIB_-RZdrGeKbdWg-Eeya1IBtOFaaRGnjvaIWLhxiRaIq3HCURA0NGPJBp_pKwytrTuF6TStQn7fsUVnPX8gnGnLf_d29MGniwLAYgd-nafb-POqEsATWSTzEtV35hLtj0_Qrg9Egmzy0lPAGSYxvshIsWdJ91JzeMny5A9j4Z_qD3C_FOg0d-8t9VPOdeXNX7BKt6Sk13WK_fYxL1HF-Wp4fVIZY--Rr8I8HV__rOOQGFtb3ZT1hofQoLpHa7Jauz8KVZD-g--mLiA499Zn0n9IPCrDwIyVFp_65s1sUy6dSCLGcj_m4qUxiCT02BP5z38nl_Wqzqh_OqY5Wgbq8MY4kVydeqGoaVWNQt0Sw9C51EQpbOR2BxDOUbVy7FgcfGp5HCWEAD6UaUTrgC-Om-c0tJs_duWW5rHazfAobAzpf4le51XXLUQM9bv9WIMFYYPW3nSHplofSV3OLhJSBRg7_Z9z4yqINNnP0fTrRtebCtDxFJuZDDYCo3mnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗
رهبر حزب‌الله نتیجه مذاکرات مستقیم لبنان-اسرائیل را رد کرد!</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/16947" target="_blank">📅 15:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16946">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انصافاً ترامپ خدایگان دروغ، دغل بازی، فریب و سخنوری است.
زاده خرداد است و ...
(امیررضا هم زاده خرداد است و میدانم این یعنی چه)
سبحان الله!</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/16946" target="_blank">📅 15:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16945">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJ9lbhVQSyWe4CY_-906m447JHDUI9yxnilDoT4TT5QmG4t_XktAngoycZfxyGL-Q0GUmw1QK_URRGf8d8uYoc6dTOBDEbTFwTPbijCKNPyhxDaCg_-oLHLbUdRN0KU9UtM8yOZoOkWUWEAnd5Cr6y4KYrnzdGujN8I4tXelJNdC-SMM8lpoI894k1boJqpdVJKdKDEWXimjXce9kR_zBnpd4ztBkjQqEGqb0XIwDoaft8CVavDChfMBp1BVeEmlDOS4ERV9Zh7YiXYJEQ7qagYfR4t8tB5E0fjVznBZ3whm5emudAw4ZAlW5w3PsazVWbcl78l20OgJ39M-3hIkZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/16945" target="_blank">📅 15:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16944">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❗
رهبر حزب‌الله نتیجه مذاکرات مستقیم لبنان-اسرائیل را رد کرد!</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/16944" target="_blank">📅 15:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16943">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACg05ysld4e8Dsu6pP7WTfnAH2u0rQKwPiZGZt-A4gw8xacpxwtbE5NVmCRCncYcnaV3ddL_b7tnhKqMUqWtPTJTM5ijsd2CNE0jj-6_5ZxlvZ6Xt0QsGnPYuYOtQEoM_7RoOpeRYUdcNvRCHzoYaAYlJcUt9XYGSxDo-8QIB7RLiYYo8zpRUqZOZ8C-jj7mGVr2atuOba52JzdQtzbQzcUkW4VoosLLzpPDV598moLI67yzoGwhwkeg4GxAE3cnWZ9trYw03bQczzmoP9wKtGUwxIrd-G4Hfsl5d031aeH8OXj3iIbTmPvMxfdjAp07SDQmjvM-3MmBqZRVfRd11A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضایی حصرشکن | حصر ترامپ رو بشکن!</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/16943" target="_blank">📅 15:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16942">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">از منظر حقوق بین‌الملل، «محاصره دریایی» یکی از شدیدترین اشکال اعمال زور میان دولت‌ها محسوب می‌شود و در صورت اجرا علیه یک کشور مستقل، به‌طور معمول در زمره اقدامات خصمانه با ماهیت نظامی قرار می‌گیرد.
بر اساس منشور ملل متحد، اصل بنیادین در روابط بین‌الملل منع توسل به زور است (ماده 2 بند 4). تنها دو استثنا برای استفاده مشروع از زور وجود دارد: دفاع مشروع در برابر حمله مسلحانه (ماده 51) و اقدام جمعی تحت مجوز شورای امنیت. بنابراین، اگر ایالات متحده یا هر دولت دیگری اقدام به محاصره دریایی بنادر ایران کند، این اقدام از منظر حقوقی صرفاً یک «اقدام اقتصادی یا فشار سیاسی» تلقی نمی‌شود، بلکه به‌طور مستقیم در چارچوب «استفاده از زور مسلحانه» قرار می‌گیرد.
در حقوق بشردوستانه بین‌المللی، به‌ویژه بر اساس قواعد عرفی و راهنمای سان‌رمـو درباره حقوق جنگ دریایی، محاصره زمانی مشروع تلقی می‌شود که در بستر یک مخاصمه مسلحانه موجود انجام شده باشد، اعلام و اطلاع‌رسانی شده باشد، و به‌صورت مؤثر اجرا گردد. به بیان دیگر، محاصره دریایی ذاتاً یک ابزار جنگی است، نه ابزار صلح.
از این رو، اگر چنین اقدامی علیه ایران در شرایط غیرمجاز حقوقی (بدون مجوز شورای امنیت یا بدون وقوع حمله مسلحانه قبلی) انجام شود، می‌تواند به‌عنوان «اقدام متخاصمانه شدید» (hostile act) تلقی شود که ظرفیت ایجاد «وضعیت مخاصمه مسلحانه بین‌المللی» را دارد. در حقوق بین‌الملل معاصر، حتی بدون اعلان رسمی جنگ، وقوع چنین سطحی از درگیری کافی است تا قواعد جنگی فعال شوند.
در نتیجه، محاصره دریایی یک کشور نه صرفاً یک ابزار فشار، بلکه از نظر حقوقی یک اقدام با ماهیت جنگی است که می‌تواند به تشدید فوری تنش و ورود طرفین به درگیری مسلحانه منجر شود، مگر آنکه تحت چارچوب‌های محدود و مشروع بین‌المللی انجام شده باشد.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/16942" target="_blank">📅 15:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16941">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">عجب فریبی و عجب تاثیری در کاهش بهای نفت!</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/16941" target="_blank">📅 15:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16940">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-qanNO7kjVYRFNJCjE9Mn31SpXeCszHxAXwEjshYaEMLXPD4i6IBXnufTRes0S7ZHIzYUsBRvTA7L2zRopu6Q7xaIUpkFeSPtKNQj6t9cso09Vq3460SDFpNq9kvamAT7pTAtgXyI3VmathabzCE1Oik8mqKhd0HsRoLDHvNKSmIT1C6gCdkVPxxvEROmDwElVybCPvAxIumMc1cO6m71OlsczBTnLRwqzN-U7BogAbT2QMVjTGIXZ9zoCgr9PylJtExr2dU9JKUK-10hS8pck5G8EAn7EWZ3Y7grKQ9WvhHOSavJGzxJW0mbbh4-W2ajcx-5yAE--9zX4y3AD-2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلا رفت برای این سناریو که عصر گفتیم…؟!</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/16940" target="_blank">📅 15:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16939">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ به دستیارانش گفته است که جنگ با ایران را از سر نخواهد گرفت مگر اینکه نیروهای آمریکایی کشته شوند.  — وال استریت ژورنال</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/16939" target="_blank">📅 15:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16938">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کاندولیزا رایس — وزیر امور خارجه پیشین آمریکا :
«جنگ علیه ایران جنگی محدود بوده و نتیجه آن احتمالاً قطعی نخواهد بود، اما برای ایجاد خاورمیانه‌ای بسیار بهتر کافی بوده است.»</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/16938" target="_blank">📅 12:41 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

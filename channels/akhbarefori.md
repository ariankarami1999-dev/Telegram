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
<img src="https://cdn4.telesco.pe/file/Ps-Lj4siS2NW9JMPFU7CIEXdxb3Q91K0zBsXb-KFCuNPH09DCoNifX2ycnGuDe_RsweuG7gp57CmyJVKN2Exq-omU_RFn1ROC2WPjZSVM72y9tCYYPamNBFzu8eoSssOy3aI1RbdCvy6BFDkg3t2SX-jV09RW_a41Iz67J11xwgYeAfFI5jrGX9_mfYpk-EtDs_2eVQYQTTFuib4Kr_En4357Jw1S_bzEe2WllecsLIwGq-h0L3HmynaYUE4eX8PnhFPp-pGJFCDBIQdxbzPts7WijDpBIt8OKu0atA3QJHdVkc0qB8zBKqS95wvhzrSCSWGOFXxC2A2iZg7slvNSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 02:34:10</div>
<hr>

<div class="tg-post" id="msg-688379">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50529400b6.mp4?token=vnhpu-w98lOvyNF8a3zF1Njk4E9J8_oXscfKLSZsSC0xft1Ixs8hwiFPzY6CAnDRirrn0bVrggvnjgiWihPx0SUesYjYvwb-kcsK4LhgM96GF4HH6vM9njqYqMB7B-DpJHSa3vilTC2SilFxKgLaERvlmSaoyUIaYX1Yu2NcUs6qHIMoVT2fwMvLpalhX_PBTw76M7FdCty-c9qf3au4n9BZzEtjeNOfiVMRWtLZZ3rEPsK5ZX47uqBfD9oDsl0Pte7KSzNHnTrb23PqBWI-YVxtYp_IVPdSEtSA8EQ0tjfe3-2svcVVZkxb-DCi-BwbFE2sFc2dsRJxVeC17nxcpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50529400b6.mp4?token=vnhpu-w98lOvyNF8a3zF1Njk4E9J8_oXscfKLSZsSC0xft1Ixs8hwiFPzY6CAnDRirrn0bVrggvnjgiWihPx0SUesYjYvwb-kcsK4LhgM96GF4HH6vM9njqYqMB7B-DpJHSa3vilTC2SilFxKgLaERvlmSaoyUIaYX1Yu2NcUs6qHIMoVT2fwMvLpalhX_PBTw76M7FdCty-c9qf3au4n9BZzEtjeNOfiVMRWtLZZ3rEPsK5ZX47uqBfD9oDsl0Pte7KSzNHnTrb23PqBWI-YVxtYp_IVPdSEtSA8EQ0tjfe3-2svcVVZkxb-DCi-BwbFE2sFc2dsRJxVeC17nxcpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از شلیک انبوه موشک‌های سوخت جامد و مایع به پایگاه‌های شرارت آمریکا از جمله پایگاه نظامی الازرق اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/akhbarefori/688379" target="_blank">📅 02:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688378">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
تصاویری از شلیک انبوه موشک‌های سوخت جامد و مایع به پایگاه‌های شرارت آمریکا از جمله پایگاه نظامی الازرق اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/akhbarefori/688378" target="_blank">📅 02:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688377">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی بریتانیا: گزارشی درباره یک کشتی تجاری در تنگه هرمز دریافت شد/
جماران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/akhbarefori/688377" target="_blank">📅 02:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688376">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ادعای ارتش آمریکا درباره حمله به ۵ نفتکش ایرانی
🔹
سازمان تروریستی «سنتکام» بامداد چهارشنبه مدعی شد که پنج نفتکش ایرانی را در روز سه‌شنبه هدف قرار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/akhbarefori/688376" target="_blank">📅 02:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688375">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
سپاه: آشیانه تعمیر و نگهداری، آماده سازی و محل استقرار جنگنده های F-35 ،F-16 ،F-15 و شلتر جنگنده ها مورد هدف قرارگرفت   روابط عمومی سپاه پاسداران انقلاب اسلامی: بسم الله الرحمن الرحیم قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَ يخْزِهِمْ وَ يَنصُرْكُمْ…</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/akhbarefori/688375" target="_blank">📅 02:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688374">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
سپاه: آشیانه تعمیر و نگهداری، آماده سازی و محل استقرار جنگنده های F-35 ،F-16 ،F-15 و شلتر جنگنده ها مورد هدف قرارگرفت
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله الرحمن الرحیم
قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَ يخْزِهِمْ وَ يَنصُرْكُمْ عَلَيْهِمْ وَ يَشْفِ صُدُورَ قَوْمٍ مُّؤْمِنِين
🔹
مردم غیور و مبعوث شده ایران اسلامی عزیز؛
تداوم حضور شما در صحنه، دشمن آمریکایی را خسته و مایوس کرده است و مقاومت و اقتدار فرزندان رشید رزمنده شما در تنگه هرمز، سردمداران کاخ سفید را کلافه وسردرگم کرده است.
🔹
ارتش تروریستی و متجاوز  شکست خورده آمریکا از روی استیصال  چند کشتی تجاری - نفتی ایران اسلامی را مورد حمله قرار داد.
🔹
با عنایت خاصه خداوند متعال و تحت توجهات حضرت ولیعصر(عج) ارواحنا فداه و به تلافی حمله متجاوزانه رژیم آمریکا به نفتکش های ایرانی، رزمندگان قدرتمند دلاور و جان برکف نیروی هوافضای سپاه پاسداران انقلاب اسلامی در عملیات تنبیه متجاوز با رمز مبارک "یاحیدر کرار" پایگاه آمریکائی الازرق اردن را زیر ضربات سهمگین موشکی خود قرار دادند.
🔹
در این عملیات برای تنبیه متجاوز با حمله سنگین موشک های بالستیک سوخت جامد و مایع آشیانه تعمیر و نگهداری، آماده سازی و محل استقرار جنگنده های F-35 ،F-16 ،F-15 وشلتر جنگنده ها مورد اصابت قرارگرفته و خسارات سنگینی به دشمن عنود وارد آمده است.
🔹
دشمن در مواجه با نیروی دریائی قهرمان ومقتدر سپاه پاسداران انقلاب اسلامی در تنگه هرمز از موضع ناتوانی و عجز و ضعف، دست به حرکت های مذبوحانه زده و بلافاصله پاسخ قاطع را دریافت نمود.
🔹
هوشیاری و نبرد قاطع رزمندگان نیرو های مسلح ج‌اا بر علیه روز به روز دشمن متجاوز تا توقف تجاوزات را مستاصل کرده است.
این نبرد مقتدرانه ادامه خواهد داشت.
وماالنصر الا من عندالله العزیز الحکیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/688374" target="_blank">📅 02:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688373">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
کانال ۱۴ اسرائیل از تلفات برخورد مستقیم موشک در یک پایگاه آمریکایی در اردن خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/akhbarefori/688373" target="_blank">📅 02:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688372">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ادعای ارتش آمریکا درباره حمله به ۵ نفتکش ایرانی
🔹
سازمان تروریستی «سنتکام» بامداد چهارشنبه مدعی شد که پنج نفتکش ایرانی را در روز سه‌شنبه هدف قرار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/akhbarefori/688372" target="_blank">📅 02:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688371">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/704c3b815d.mp4?token=WpqE-eoWbwjaS7yfnr2cxiDC4T4azupMfP7sNjbRWD6KNMzMDI-NIWKeOX09kaJZW-eMHpKQJXx6G3eX9fxGTCSkFcA2sbCZ3Q0kMhq1Pzi88QQaVUN0znVNPhmjiANQhH39UoDl2zw8fG6Mq8g1zl25dnct423tfgCK14lb3sGrmF1ABi0pa0xUa4nxuTxTr5C4Fu_HjOB2nYzqsG_Q7maEVTiTcNNB7a2MaVqhWksOOKnKWCSDWWxdCWC4E8ycYVYOZ2CwLCy8Mp0Mwg6hAFpLehkMtltdOrBhK-NuOIMitf0VbxqDmo1IP8JAYa_P1LYUCk6YyQ4wS2p63ljtKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/704c3b815d.mp4?token=WpqE-eoWbwjaS7yfnr2cxiDC4T4azupMfP7sNjbRWD6KNMzMDI-NIWKeOX09kaJZW-eMHpKQJXx6G3eX9fxGTCSkFcA2sbCZ3Q0kMhq1Pzi88QQaVUN0znVNPhmjiANQhH39UoDl2zw8fG6Mq8g1zl25dnct423tfgCK14lb3sGrmF1ABi0pa0xUa4nxuTxTr5C4Fu_HjOB2nYzqsG_Q7maEVTiTcNNB7a2MaVqhWksOOKnKWCSDWWxdCWC4E8ycYVYOZ2CwLCy8Mp0Mwg6hAFpLehkMtltdOrBhK-NuOIMitf0VbxqDmo1IP8JAYa_P1LYUCk6YyQ4wS2p63ljtKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه‌ گویی وزیر امورخارجه آمریکا: از این پس هربار ایران تلاش کند به ناوگان امریکایی آسیب برساند چه موفق باشد چه ناموفق، تعدادی از ناوگان نفتکش‌های خود را از دست می‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/688371" target="_blank">📅 01:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688370">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ادعای سنتکام: پنج نفتکش ایرانی را هدف قرار دادیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/688370" target="_blank">📅 01:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688369">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4362d9420a.mp4?token=ac1jmpc9X4ZglNBOPs-y1l04bTyMtBaPV0A4xF7Ob83e6UFB60NJj0QWIYT8S1iWyMTg4Dwj4W9v3hgB--VPf6F63tZeEazXkSWFbQr16wirq_deQ-eScmQJjGyYXKDy7y2X7KZTv51UtclHqyNdo07kjSkQsPLgC9GeczxE5VS4VAboVWiYtOVqE5IWhWBsxBh7mH3BubnEqyofeZbE5VSTFk2baAkRDfw-mN8MdSrFjaOoj4SlpXb9EDIbkcHjBIAgxHQKqEwLkuusjTt3dzwqi9pNiJazC8rAHZYZBa4dm_k0hoqdzI1uy36CdlqepP6JELVX3eQSyX1FFG0LRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4362d9420a.mp4?token=ac1jmpc9X4ZglNBOPs-y1l04bTyMtBaPV0A4xF7Ob83e6UFB60NJj0QWIYT8S1iWyMTg4Dwj4W9v3hgB--VPf6F63tZeEazXkSWFbQr16wirq_deQ-eScmQJjGyYXKDy7y2X7KZTv51UtclHqyNdo07kjSkQsPLgC9GeczxE5VS4VAboVWiYtOVqE5IWhWBsxBh7mH3BubnEqyofeZbE5VSTFk2baAkRDfw-mN8MdSrFjaOoj4SlpXb9EDIbkcHjBIAgxHQKqEwLkuusjTt3dzwqi9pNiJazC8rAHZYZBa4dm_k0hoqdzI1uy36CdlqepP6JELVX3eQSyX1FFG0LRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرود یکی پس از دیگری موشک‌های ایرانی بر سر روریست‌های ارتش آمریکا در اردن
🔹
خبری از پدافند آمریکا نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/688369" target="_blank">📅 01:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688368">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
رسانه های عربی: یک موشک به شهر سویدا، در جنوب‌غربی سوریه برخورد کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/688368" target="_blank">📅 01:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688367">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
کانال ۱۴ اسرائیل از تلفات برخورد مستقیم موشک در یک پایگاه آمریکایی در اردن خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/688367" target="_blank">📅 01:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688366">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
شنیده‌شدن صدای چند انفجار در بحرین
/صابرین نیوز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/688366" target="_blank">📅 01:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688365">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dd4640421.mp4?token=f_ywPjL3l_CszrzP2Bai4Mez6MVlzXSX9uYWV47D0veRAtdzZJ3eZYMWFvksBpcwPxbTtgEbf8qSlkthV9w_p4RPnqn3c2L_jb8Bj70XAloZFKIUY4i-SqxefKB-zpNUkqqd3nTGLw6ab60HhnXOjaPFZmpKKTuoGFsYO9GIMhmqKh4UPohZUzgIfYbeDAj2gXBfPT_d7ke_6DRNxFO3lY6wXiRhHEtEgpRUug0CDprJlk2ziKzr--KX3wev8yidlaFAMMqfxRSA6qiNz5fXfna2KD1DNqj7cJzrVyWwVo7e71brvKYjSo6X3dDLr5tttk-r9w-kbGvqqYM1CYgrOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dd4640421.mp4?token=f_ywPjL3l_CszrzP2Bai4Mez6MVlzXSX9uYWV47D0veRAtdzZJ3eZYMWFvksBpcwPxbTtgEbf8qSlkthV9w_p4RPnqn3c2L_jb8Bj70XAloZFKIUY4i-SqxefKB-zpNUkqqd3nTGLw6ab60HhnXOjaPFZmpKKTuoGFsYO9GIMhmqKh4UPohZUzgIfYbeDAj2gXBfPT_d7ke_6DRNxFO3lY6wXiRhHEtEgpRUug0CDprJlk2ziKzr--KX3wev8yidlaFAMMqfxRSA6qiNz5fXfna2KD1DNqj7cJzrVyWwVo7e71brvKYjSo6X3dDLr5tttk-r9w-kbGvqqYM1CYgrOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاهده‌ی حرکت موشک‌های ایرانی به سوی پایگاه‌های آمریکا از کرانه باختری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/688365" target="_blank">📅 01:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688363">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6647713bf2.mp4?token=iaz6_njPQcNrJV5bdmaw68NXixC9v0BqixC1wB8TBi-2v6GkdXGlwarN8zGeGWHmoyTKvenpL1VJKPpiAbSn_m8teL2HwihrbakLnBvVGCl3oBurMZDTYySKk2k0145Z9oK35-HKaE0Lh0wYd0E1euiDE0NrMzShrOizBXoFx8HPjYQ1HnOlSzghwl8AjgkBdw3PPlYS-tnDDDR3hG3PzqUsbacNjYO6DgoJ-MiV8yH1KCiDndiPcLwQWN3qFadQd4f1-8g8QOlFTNh0BrIKg1CsGJrBs3H4vs5MsD5mWNknr8qrAnqGexosSTvAJeHlBT_hJViCGED-6rCQWfWtDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6647713bf2.mp4?token=iaz6_njPQcNrJV5bdmaw68NXixC9v0BqixC1wB8TBi-2v6GkdXGlwarN8zGeGWHmoyTKvenpL1VJKPpiAbSn_m8teL2HwihrbakLnBvVGCl3oBurMZDTYySKk2k0145Z9oK35-HKaE0Lh0wYd0E1euiDE0NrMzShrOizBXoFx8HPjYQ1HnOlSzghwl8AjgkBdw3PPlYS-tnDDDR3hG3PzqUsbacNjYO6DgoJ-MiV8yH1KCiDndiPcLwQWN3qFadQd4f1-8g8QOlFTNh0BrIKg1CsGJrBs3H4vs5MsD5mWNknr8qrAnqGexosSTvAJeHlBT_hJViCGED-6rCQWfWtDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شلیک گسترده و ناموفق سامانه پدافندی «پاتریوت» و عبور بی‌دردسر موشک‌های بارشی ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/688363" target="_blank">📅 01:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688362">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UF_znFtBFu3OQFzS0k-e1ZL6axMEqZYZiCeNlJUF0XPQLdzCPJfMoW9L9eUL_eePOQaXx4TdPjHWjG5QZ6Y0HOSBzjKkPSeCKXX9iXm28L7kbqNTVzVD3cvujtxsjGwPqJVKE-DovxocisAFqeDBHsxEBOSXcm6LCGOrTVs7mO33C9E-iclo20VZ1sT_ZfZ7N4Y-TFbxwN-jooXw7bf0XRzg5ngv-xp8CLIlX0tsqpFKeZ52uUS1H6juWuguSiccX-mAfQCjZ1j-_5Jkq14a_TtP9clokGO_oB2K7iHbUdZKNaLfBH14aLcvfiDtVaxzE2WHEcgCqfVjqz19up38Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توصیف جالب شبکه های عبری زبان پس از حملات موشکی ایران به سمت پایگاه های آمریکایی در اردن؛ باران موشک های ایرانی به سمت اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/688362" target="_blank">📅 01:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688361">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46d8d79f30.mp4?token=X5tvCK-fva1JADT9TqWbthBmVDjRohN9fyisbU6D1smxoW3Q1Is7wQoLLQv3nSGxUuN_qFJ4xH2D5HEZtk9cHq-UhRbLuGGrWrhdGrwlnGM4lJP4PaEJ83c2VQNo-NGC9yPodrHw1LNHaSTs7PpRCAfO2inMB4hEEKhpSTSsTGOqDjaC50fZhCaYS-yrNbFtw599f0aWpeCWMbBsN2q6Iim4gQ-xKeXZXwvauBeq5r3p-oJb4-30qaE57x8xjydDGBLjT0xGKMdqOjDZdkWSrNj019SWze0QHscTKbUJBhcqRPW5hhT1NiovF8dLDrv4JraOWE-Fu7m-B5qMmp0GPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46d8d79f30.mp4?token=X5tvCK-fva1JADT9TqWbthBmVDjRohN9fyisbU6D1smxoW3Q1Is7wQoLLQv3nSGxUuN_qFJ4xH2D5HEZtk9cHq-UhRbLuGGrWrhdGrwlnGM4lJP4PaEJ83c2VQNo-NGC9yPodrHw1LNHaSTs7PpRCAfO2inMB4hEEKhpSTSsTGOqDjaC50fZhCaYS-yrNbFtw599f0aWpeCWMbBsN2q6Iim4gQ-xKeXZXwvauBeq5r3p-oJb4-30qaE57x8xjydDGBLjT0xGKMdqOjDZdkWSrNj019SWze0QHscTKbUJBhcqRPW5hhT1NiovF8dLDrv4JraOWE-Fu7m-B5qMmp0GPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه اصابت موشک ایرانی به پایگاه آمریکایی در اردن، از زاویه دید دوربین فردی در را‌م‌الله
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/688361" target="_blank">📅 01:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688360">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c979df33a5.mp4?token=sM5aQJ4MVtbXDUwzcAokOXB1hVOJR0V7Yf1hqLHOZt-q59Uobwf7xkBMB5Pn96vL_jcFCZ5fMvMYpLrgwkF1h6xlFS-BqAPqhGwp8dseTnmHR0xXcYZez-eMLEyxoC-lLbyCrjyALJVR2_uLQP4SDKtqh71nIiJ6BeD-6bDEKG_m3q--hABCj4tQ2c2OmupKSz47xKQ1s8xqZ8bOqgbowdYpNkPHKnCjpo9OOoUQmps-N2qj-pfib_fYgRORW5LThtI2s4gJB8LJeJ7T-VTS2lMVUM7fsl0EJJ7SSSPjtfUIASbLCZjRQQsrbwOk66MhMv38IN7zZZiHv_iegJ9uGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c979df33a5.mp4?token=sM5aQJ4MVtbXDUwzcAokOXB1hVOJR0V7Yf1hqLHOZt-q59Uobwf7xkBMB5Pn96vL_jcFCZ5fMvMYpLrgwkF1h6xlFS-BqAPqhGwp8dseTnmHR0xXcYZez-eMLEyxoC-lLbyCrjyALJVR2_uLQP4SDKtqh71nIiJ6BeD-6bDEKG_m3q--hABCj4tQ2c2OmupKSz47xKQ1s8xqZ8bOqgbowdYpNkPHKnCjpo9OOoUQmps-N2qj-pfib_fYgRORW5LThtI2s4gJB8LJeJ7T-VTS2lMVUM7fsl0EJJ7SSSPjtfUIASbLCZjRQQsrbwOk66MhMv38IN7zZZiHv_iegJ9uGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر رسانه‌های عربی از برخورد موشک ایرانی به پایگاه آمریکایی در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/688360" target="_blank">📅 01:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688359">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
بر اساس گزارش‌ها، ارتش اردن به دلیل ناتوانی سامانه‌های پدافندی آمریکایی، جنگنده‌های نیروی هوایی را برای رهگیری موشک‌های بالستیک ایرانی به پرواز درآورده است./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/688359" target="_blank">📅 01:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688358">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f690d038c.mp4?token=IkHHTfHuIzpD0HfVN0jqdfRW74mnM-hlnFaCphfBB_nBWWcMlTHifZpCnwLuDxHU138B3177_ScrTqu9h6BBAW9pu8sD_1CBDgBHN2KRUYKPZAMVfZau6_iUga96SzwrDZDwyn7cKhJ70dI5MYm6ZlRfrlleDikPeYQQ2Fa1s2IYewMIk9v11FhvDk_Msz0aG6H-EF72C1VdGBSDUrYdSVuZAaiNxaHRENpkr5NrNivfy1sL4N2U4a75xQ1xwStxAgLU5DUsqGu4rav-PzXhfX4BP6hFbsWZkwWHJQcQah4VMYpXAn3HaG8donrN1KrJLYTymeXM1yDOWqARs_FPhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f690d038c.mp4?token=IkHHTfHuIzpD0HfVN0jqdfRW74mnM-hlnFaCphfBB_nBWWcMlTHifZpCnwLuDxHU138B3177_ScrTqu9h6BBAW9pu8sD_1CBDgBHN2KRUYKPZAMVfZau6_iUga96SzwrDZDwyn7cKhJ70dI5MYm6ZlRfrlleDikPeYQQ2Fa1s2IYewMIk9v11FhvDk_Msz0aG6H-EF72C1VdGBSDUrYdSVuZAaiNxaHRENpkr5NrNivfy1sL4N2U4a75xQ1xwStxAgLU5DUsqGu4rav-PzXhfX4BP6hFbsWZkwWHJQcQah4VMYpXAn3HaG8donrN1KrJLYTymeXM1yDOWqARs_FPhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیرجه موشک بارشی ایرانی بر روی پایگاه آمریکایی در اردن
🔹
هیچ پدافندی به سمت این موشک‌ها شلیک نشده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/688358" target="_blank">📅 01:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688357">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10069258d9.mp4?token=hhMRj1VbMKfkNxFt93aWYZfVlmIAq0AFaHOSOquMa0G6vDCmT5w4JiWdqNz8OPm-hbWMFZtyo0NaBguDd8cBuGK8j4FMW2lzkGFVWf2ATReBojG8OESZy9UZ5TQc-QWZR78Wo4Ye9265cCfjSjsyK9PdNPwdTuoAYUdt34KI4pQe6D9WFANUqPwFgxzoBbs1uSCj_NP-Z7Lqv0_h9g52SNVnvw7l4QsNCffUF4VorAuae4wn4ibWE6o5atqrJrnCCP3wx89Ls14CNnsrDrMnzai85mU8AVupuy1AM2485WLQX-6S9hJXRKAf1IlocbhGHB1J-qJ6eioE2bFiiY6fmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10069258d9.mp4?token=hhMRj1VbMKfkNxFt93aWYZfVlmIAq0AFaHOSOquMa0G6vDCmT5w4JiWdqNz8OPm-hbWMFZtyo0NaBguDd8cBuGK8j4FMW2lzkGFVWf2ATReBojG8OESZy9UZ5TQc-QWZR78Wo4Ye9265cCfjSjsyK9PdNPwdTuoAYUdt34KI4pQe6D9WFANUqPwFgxzoBbs1uSCj_NP-Z7Lqv0_h9g52SNVnvw7l4QsNCffUF4VorAuae4wn4ibWE6o5atqrJrnCCP3wx89Ls14CNnsrDrMnzai85mU8AVupuy1AM2485WLQX-6S9hJXRKAf1IlocbhGHB1J-qJ6eioE2bFiiY6fmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دسته‌ی دیگری از موشک‌های پر تعداد ایران در حال شیرجه به سمت اهداف دشمن آمریکایی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/688357" target="_blank">📅 01:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688356">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/071b105580.mp4?token=qKf7uWaHXpUSiKH7pZvpgFvU1x_AjnG5B9YWhfAiWHCr8y0zVEb5H37cXnf427XozS3z1yxWOjqtuUQrIMYL-P1dezOUKN2_F30ssxZkOFqTPcmQOxgLEdU0wdSQ7jvH0iHeeuw6PHLo92HO00gIL7l2xiY5LFWG0YrnO-uqq_biUKGnVVGqaGvcyUUl8VQo6HshCbwiesaX9CiSQnWKIejlFjNGRO828aegnkUU7HtRy7W5T6RXAeMbt2efXEpkIDQWviR_bHfs6feYD3NT1B-ZZL9DfY54bV7qY_XuQQ9CzwXn-d7DQEA4ivvwxf7w_kqS0uqf_ibdr-yMo9YHHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/071b105580.mp4?token=qKf7uWaHXpUSiKH7pZvpgFvU1x_AjnG5B9YWhfAiWHCr8y0zVEb5H37cXnf427XozS3z1yxWOjqtuUQrIMYL-P1dezOUKN2_F30ssxZkOFqTPcmQOxgLEdU0wdSQ7jvH0iHeeuw6PHLo92HO00gIL7l2xiY5LFWG0YrnO-uqq_biUKGnVVGqaGvcyUUl8VQo6HshCbwiesaX9CiSQnWKIejlFjNGRO828aegnkUU7HtRy7W5T6RXAeMbt2efXEpkIDQWviR_bHfs6feYD3NT1B-ZZL9DfY54bV7qY_XuQQ9CzwXn-d7DQEA4ivvwxf7w_kqS0uqf_ibdr-yMo9YHHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قطار موشک‌های ایرانی به سوی اهداف آمریکایی
در
اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/688356" target="_blank">📅 01:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688355">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b66dc72d1.mp4?token=rmwEh-PWVCywGS4JLw9zlDcVDCUHxE4XeRq4rs6ml2EcWuJJ4gR_Bt7ApMCMnDC4CSr_yOGh8eh0cG_3TTBBAiXdJHFJYSPEIhAR2LOkGo867P163WGlgfc1pdrsAa9f3-peqCOs9IRGHq5zjVnfHNzNWRyFJBt-a1BxrrbZCODnoRJQkAMUaJYXG_SXBPe6r6E6ZJTggNMkZLY7veJ77ac84ZqKnaxvGtqAMFg7SVKY0TSFLw7nZ12w65U94KRi5DFbzc8H50PIiNCjtwXpF48Qea4QvvWD0l7UZss8hmXnwBy09I1hIFPoIM44ioGHIerE2-6E3Mghla5PJME5rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b66dc72d1.mp4?token=rmwEh-PWVCywGS4JLw9zlDcVDCUHxE4XeRq4rs6ml2EcWuJJ4gR_Bt7ApMCMnDC4CSr_yOGh8eh0cG_3TTBBAiXdJHFJYSPEIhAR2LOkGo867P163WGlgfc1pdrsAa9f3-peqCOs9IRGHq5zjVnfHNzNWRyFJBt-a1BxrrbZCODnoRJQkAMUaJYXG_SXBPe6r6E6ZJTggNMkZLY7veJ77ac84ZqKnaxvGtqAMFg7SVKY0TSFLw7nZ12w65U94KRi5DFbzc8H50PIiNCjtwXpF48Qea4QvvWD0l7UZss8hmXnwBy09I1hIFPoIM44ioGHIerE2-6E3Mghla5PJME5rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم اکنون موشک‌های ایران در آسمان اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/688355" target="_blank">📅 01:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688353">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d77db0c15f.mp4?token=D6R7PHYXIK21nLB7Sm62Pn7feDYm_nYyVq5pS5wg_Q_ancanQr4AhU4Oq_r4w5DQGGiplMHkj4QdAjYQEb4Wf3URBNsT4ukzMbUaS0yhH9LuKZSPGUd3eIsbGThqtVzWzv-7R7dZeAwndHuYiLngcNKqaZD5JjGwVh4wpJFHKisdVul6qAwcyDMgivsw_x-1zHF15brUJ9ABYnNDxcg2uK6piIbne53quDZCXAYyp1x_d9oGq2SCc7BihvWF2K9EIGSAUIKTHLhJPdRGcRgnGOE_5NWVCIaQArGDDiUIY2I83xuiikUz3E26_b_aIBVP0i59V6GPO1RaRvhUTXHoAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d77db0c15f.mp4?token=D6R7PHYXIK21nLB7Sm62Pn7feDYm_nYyVq5pS5wg_Q_ancanQr4AhU4Oq_r4w5DQGGiplMHkj4QdAjYQEb4Wf3URBNsT4ukzMbUaS0yhH9LuKZSPGUd3eIsbGThqtVzWzv-7R7dZeAwndHuYiLngcNKqaZD5JjGwVh4wpJFHKisdVul6qAwcyDMgivsw_x-1zHF15brUJ9ABYnNDxcg2uK6piIbne53quDZCXAYyp1x_d9oGq2SCc7BihvWF2K9EIGSAUIKTHLhJPdRGcRgnGOE_5NWVCIaQArGDDiUIY2I83xuiikUz3E26_b_aIBVP0i59V6GPO1RaRvhUTXHoAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرود موشک‌های ایرانی با کلاهک‌های بارشی بر سر تروریست‌های آمریکایی در منطقه «العقبه» در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/688353" target="_blank">📅 01:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688352">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c87916aa64.mp4?token=KmSVDruHEV0NM3F5UbRka2LFuQYj5mzUviBdhYdLrWK18yTQ9e1_JkSlY9U_4gEJcR4oOtr7Zq66pCkIK_HMfsh4j8SBdnM-vvRNBz6C84Y_Q25n5h3Dq6Dh-kS6GiSY4xJTWL70uQmMujury4FjLdSPJG_y3LwoIES1kGwO9uaPVRnVAWcHADqVJzwA7LG6CNfOCe-LoXXqQkH2DwQrigsejxwtqlkCTipwTf3XmU50FroQOWPeYg8tLU0EXoU9W40g4eZq0mDeMwSdOgm8O1fpoNLpTvGCv80vpEbbC-DpDTe0BwLjlymph99yuB5HO4v0thpBIM6geMrdavlRUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c87916aa64.mp4?token=KmSVDruHEV0NM3F5UbRka2LFuQYj5mzUviBdhYdLrWK18yTQ9e1_JkSlY9U_4gEJcR4oOtr7Zq66pCkIK_HMfsh4j8SBdnM-vvRNBz6C84Y_Q25n5h3Dq6Dh-kS6GiSY4xJTWL70uQmMujury4FjLdSPJG_y3LwoIES1kGwO9uaPVRnVAWcHADqVJzwA7LG6CNfOCe-LoXXqQkH2DwQrigsejxwtqlkCTipwTf3XmU50FroQOWPeYg8tLU0EXoU9W40g4eZq0mDeMwSdOgm8O1fpoNLpTvGCv80vpEbbC-DpDTe0BwLjlymph99yuB5HO4v0thpBIM6geMrdavlRUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصابت موشک خوشه ای به پایگاه ارتش تروریست آمریکا در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/688352" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688351">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
شنیده‌شدن انفجار در اردن
🔹
منابع عربی گزارش دادند در پی حملۀ موشک‌های ایرانی، انفجارهایی در اردن رخ داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/688351" target="_blank">📅 01:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688350">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
شنیده‌شدن انفجار در اردن
🔹
منابع عربی گزارش دادند در پی حملۀ موشک‌های ایرانی، انفجارهایی در اردن رخ داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/688350" target="_blank">📅 00:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688349">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
منابع محلی از شلیک چندین موشک از مرکز ایران به سمت اهداف متخاصم دشمن آمریکایی خبر دادند/دانشجو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/688349" target="_blank">📅 00:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688348">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
دقایقی قبل نیروهای تروریست آمریکایی به یک فروند شناور تجاری در آب‌های ساحلی شهرستان جاسک حمله کرد
/ صداوسیما
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/688348" target="_blank">📅 00:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688347">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/009da00baf.mp4?token=VTR0rwEB9Af6p07X-7Dsed9cjkFXMPkmWX28XfCv-DLUv88tgJ7sJjT7g1ZxcRexrCtpDsQEJj9Wb53ct4ouA22LwMc7nSGXlhB5hVI9R7a8IbhKknnwtl0u6u0HWAHswvECrEQIDBaZn4xWMtVwID79zg7fWeDYD2relCKCovH-t6QPZtq0UalA8q9i_XiFgAllaOlsxJdVuCCo7DJyiSh9dbet2C1LIrCNI2MxwpDpOdQkQDBeEOQNtVIOYqIO7xA_yzmtKfG2Un8br3AWt5-7FeNLGeiJiCWYN55O1aI_T4ciYIjAc57Jbqd76HGFp6Rop-JkW6mp71DdqPv5tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/009da00baf.mp4?token=VTR0rwEB9Af6p07X-7Dsed9cjkFXMPkmWX28XfCv-DLUv88tgJ7sJjT7g1ZxcRexrCtpDsQEJj9Wb53ct4ouA22LwMc7nSGXlhB5hVI9R7a8IbhKknnwtl0u6u0HWAHswvECrEQIDBaZn4xWMtVwID79zg7fWeDYD2relCKCovH-t6QPZtq0UalA8q9i_XiFgAllaOlsxJdVuCCo7DJyiSh9dbet2C1LIrCNI2MxwpDpOdQkQDBeEOQNtVIOYqIO7xA_yzmtKfG2Un8br3AWt5-7FeNLGeiJiCWYN55O1aI_T4ciYIjAc57Jbqd76HGFp6Rop-JkW6mp71DdqPv5tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این ماهی بادکنکیِ نرِ کوچک، تنها با کمک باله‌هایش، شاهکارهای هندسیِ خیره‌کننده‌ای را در بستر اقیانوس خلق می‌کند
🐠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/688347" target="_blank">📅 00:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688346">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
سی.ان.ان: ۲۶ نظامی زخمی دیگر آمریکا گزارش شد
🔹
بر اساس داده‌های سامانه تحلیل تلفات دفاعی پنتاگون (Defense Casualty Analysis System)، ۲۶ نیروی نظامی زخمی دیگر آمریکا ثبت شده است.
🔹
با احتساب این موارد، مجموع تلفات نظامی آمریکا از زمان آغاز جنگ به ۸۳۸ نفر رسیده است:
🔹
۱۸ کشته — شامل ۷ نفر در حوادث غیررزمی/ ۸۲۰ زخمی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/688346" target="_blank">📅 00:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688345">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ادعای وال استریت ژورنال: ایران به سمت یک ناو و یک ناو هواپیمابر شلیک کرده است
🔹
در روز یکشنبه یک ناو هواپیمابر و یک ناوشکن هدف موشک‌های بالستیک ایران قرار گرفتند. روز دوشنبه نیز حمله دیگری علیه شناورهای نیروی دریایی آمریکا انجام شد، اما نوع شناورهای هدف‌ گرفته‌ شده در این حمله دوم مشخص نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/688345" target="_blank">📅 00:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688344">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: حمله به یک نفتکش ایرانی در نزدیکی ساحل یکبنی بندر جاسک
🔹
خدمه هر دو نفتکش با قایق نجات در حال انتقال به سمت ساحل جاسک هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/688344" target="_blank">📅 00:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688343">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6414c4663b.mp4?token=BR94xrbt29MSm9dFtMFotLWaA2a2Ic_eCwP7hp7QEjgPSTjyq_d8LKbfYblHQlEcm43AlYCwJNBowEAoOD8oLxKXA1cGclBSpnRwegiWlWFZtPsHyZ65ElV_aeLa4Dh-puaTnj1gu2Y2Y7geTF--m_Hz92at9BBEjsGCeYRwGY-ZraD1M3V0iioTxRofWGwL2EzoHV8eE7fy0DEtkM6Np78CQjNjHbnVQXMOqCtAowi9IraEcgCrEPRekyGRhlImXZM9BfIepcY3JxOnu-2v2BzWJDBMNMXcFxwWlrOTl9kGK-e6HV5RpAEbuvLEaM8d4yjQdH97TbeufkNn1ny7K0qR6RwBkdKJHRBCdvpZEm1rH3VA2gUOOECnfZpkFXtZ2F_Jtbciy2v28aAjteEUvqAKio5oAHOTTk_u9IrVdtH3i3oZ57lWlN-dxVwPS9X2IUABxb5KfVtJmWBXA9FbV0KLcst9k33tVCL82MykVoGQqVnYsTf9SPBwVxOpHuM_FdizTiRxrUiYeglV55GwKQQj1WG68ChNUoJgreS6pY9_Om88_gmG-42PjFqE_kOoJstnWtDRQmcA8gTzQBNRgmrvVi3RtmQkPNcQ9sSTzNZKHWeUZxfEOhexbHBNyckrMCRoq4_ENtrmdDdZ66Dr8ugI-BLlvymFEsUtIUCVVPo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6414c4663b.mp4?token=BR94xrbt29MSm9dFtMFotLWaA2a2Ic_eCwP7hp7QEjgPSTjyq_d8LKbfYblHQlEcm43AlYCwJNBowEAoOD8oLxKXA1cGclBSpnRwegiWlWFZtPsHyZ65ElV_aeLa4Dh-puaTnj1gu2Y2Y7geTF--m_Hz92at9BBEjsGCeYRwGY-ZraD1M3V0iioTxRofWGwL2EzoHV8eE7fy0DEtkM6Np78CQjNjHbnVQXMOqCtAowi9IraEcgCrEPRekyGRhlImXZM9BfIepcY3JxOnu-2v2BzWJDBMNMXcFxwWlrOTl9kGK-e6HV5RpAEbuvLEaM8d4yjQdH97TbeufkNn1ny7K0qR6RwBkdKJHRBCdvpZEm1rH3VA2gUOOECnfZpkFXtZ2F_Jtbciy2v28aAjteEUvqAKio5oAHOTTk_u9IrVdtH3i3oZ57lWlN-dxVwPS9X2IUABxb5KfVtJmWBXA9FbV0KLcst9k33tVCL82MykVoGQqVnYsTf9SPBwVxOpHuM_FdizTiRxrUiYeglV55GwKQQj1WG68ChNUoJgreS6pY9_Om88_gmG-42PjFqE_kOoJstnWtDRQmcA8gTzQBNRgmrvVi3RtmQkPNcQ9sSTzNZKHWeUZxfEOhexbHBNyckrMCRoq4_ENtrmdDdZ66Dr8ugI-BLlvymFEsUtIUCVVPo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آرامش و زیبایی در دل کوهستان زاگرس
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/688343" target="_blank">📅 00:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688342">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTqK7lp0H7j0xc1nIhoZyHs8LVCzETGUi5557TSOjbIrUbIdyqPPxnnoXbw70yXu-XPCl2QyjcMT6schcvELmd6O9QchBWknL6hGFWQg0ekDzJTbWAPhWaB16TuXis3I2PFpE4_UV9qp0hBuDzFT8LjJX-1Ly-xU3Y-jmH0QkQX2p5SxOx68lOxdbrBhKe8Oiq2-jcWK4B3Xw84fxPkNeKpcZX_7cz7udxT7qzLKfnuGTsORm5MjIOkxZq5HVqbT8w3hjN7B-n2csZcrZygnbFFOrwSrROnOsjS6YHtem2vbsMitN5P-8LpLSNUn4FnZ6SVgKMo3-LZ7cFN07tYE1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت رئیس کمیسیون‌ امنیت‌ ملی‌ مجلس: وضعیت آمریکایی‌ها در انتظار پایین آمدن قیمت سوخت بعد از هزارمین اعلام پیروزی ترامپ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/688342" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688341">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1JtQAlt7XbKof1Gk7bMm7lkAvw8DxmIrYhCxBKr65mAA7b3yYch74ml3zxudL_WRVMahobDLUpPjEESDu8Q30RXb2S_DIANSP_InowMLOui4hG0lfKpzlNknSIYKNervNQC4sqXe9xGbsMnjxQ8ef0fzsP9B_bwfmjV3g-Dl3WG0PSCuVkMcYUS_qq3gDKLN-Q0A_ZLgO-MGM-6bJD500-yHPJiK3Z2N9vsKpDZ4lGTqN7q_JIZZ3QGNUxaGMFDBI6O1eeJuhgUkLslH6ILO7KwVS0VCIpDBbVDQEJW7IPElMgZ84COThxkBVGZwXZ0pvRCxquNNgBp5Kx4LtupbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازتاب صید گران‌قیمت نیروهای مسلح از خلیج‌فارس رسانه مطرح روسی‌زبان
راشاتودی:
🔹
زیردریایی ۲.۵ میلیون دلاری پنتاگون در نزدیکی تنگه هرمز توسط ایران توقیف شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/688341" target="_blank">📅 00:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688340">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/570e8110a3.mp4?token=hVXObO5FSBu1dh-M5KO1U7KjeSXsQQAAY-LIqKYKlHu5YOpV__Z0FnY0VPDNMNNlAGRe8eqOwpiEuJrBCtNqdrpwEngdcXZCyoYqonD5thPWVUnqdWYsPuCw2aNvC6u56gtwqtuOp9pTuO8onqQEgSBUSdG6NCuxkkHDbNeGVOit-vDqbpyWmAsaebBT4IaKUEqXMKkhZmt4Qt1W81yrv9k0c3AP-GjSeVuTTECydyaOjzxSA9JpYRYqWe_iRanK6UEpEr8MJTXhxBZGz8Q2a_LDJZeI4pwxqf1K_j0AyTgtHTmqCV3m5_fLBQpg8r3ZXPPJx3i75sT5EyGymNDvCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/570e8110a3.mp4?token=hVXObO5FSBu1dh-M5KO1U7KjeSXsQQAAY-LIqKYKlHu5YOpV__Z0FnY0VPDNMNNlAGRe8eqOwpiEuJrBCtNqdrpwEngdcXZCyoYqonD5thPWVUnqdWYsPuCw2aNvC6u56gtwqtuOp9pTuO8onqQEgSBUSdG6NCuxkkHDbNeGVOit-vDqbpyWmAsaebBT4IaKUEqXMKkhZmt4Qt1W81yrv9k0c3AP-GjSeVuTTECydyaOjzxSA9JpYRYqWe_iRanK6UEpEr8MJTXhxBZGz8Q2a_LDJZeI4pwxqf1K_j0AyTgtHTmqCV3m5_fLBQpg8r3ZXPPJx3i75sT5EyGymNDvCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💡
چراغ قوه ۸ کاره  LED TORCH
💳
868 هزار تومان
🏠
پرداخت درب منزل
❇️
۳ روز ضمانت تست و تعویض
خرید سریع:
http://istgaharzoni.sabzgostarr.ir/FastCart/smscart/5872</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/688340" target="_blank">📅 00:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688339">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پشت پرده تلاش در مجلس برای استیضاح وزیر ارتباطات؛ ستار هاشمی بزرگترین سد در برابر اجرای «طرح صیانت»!
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/688339" target="_blank">📅 00:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688338">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tg9mBLoCWlbTYYWxLieTbSuTCkEXKMv08kjojfDlazyYsz3SqSfmo2Yv6-Mbkf7LpgdVET9ut7ldbYuVvwFRvp_x66tCb299c1UKIMsOBDnPU12K-ntZTVvmVg7ikxBscyOroCNAnyM5ZfaCUpy3-GdihK9-eKalnyfzU9jqY9_b6Gw5Km8PmDklRsbTu9Mu4NV866SgTDIANiIZGvDRJaQ18LYZtkSV8D1KpHmZa82GF478-n9ZWthJpn3QvdofhtUsKo6sHkBWKsKDZWjYHxNJLa7MZep7uZnLosv5yms2lvs54NnGxgpYU9ldoiNHwNadUKnrwJMGe3VI2eABig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/688338" target="_blank">📅 00:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688337">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbUYlBaJPdslCW2VGrEY95Uky2m-1BRmGKzzpDhFDPgcXfz8Axx2g5AV3-k826cOVKUmpYpAVxN-QlLt6M_5SZdLxsDLmwx3zCg90d760F5PZdjPwQ_WQOEqZ1cd6vhkB6-Lr5UPm1Scu2VAGUKO5-UgJHEtslf6-3GbAejR2-lHx-cKI1HSD2NHObt-JvC66OArayNqha2IexdGNbJ9D6L0kI3LiPOkKEAOQwGUSAEBVAhtDMr-PTJv9tDvhM1kVzN0XTtkZ-WxT9_FHhC7CAlkBAUVCsSTcKGAh_j-b1Dk1G3y6GhbYuE89HbODIg3MAMKXMCMToV7ykXkMkmDvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بله آقای ترامپ، نیروی دریایی ایران در قعر آب‌های خلیج فارس است؛ منتظر شکار ارتش متکبر و پوشالی آمریکا
🔹
Yes, Mr. Trump, Iran’s Navy is deep beneath the waters of the Persian Gulf, waiting to hunt America’s arrogant, hollow military.
به توییتر خبرفوری بپیوندید
👇
https://x.com/akhbare_fori/status/2095856638485839910?s=46</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/688337" target="_blank">📅 23:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688336">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206796ec3e.mp4?token=gEmNIf4wsG-e6-FM5-dvBBWAuavpV0MtAZvQjZFyWYs9QMJvne1ve39nZCFwMpXAcy45dYMsdygkyh0ZYvNzdkxp95FX5aAhi97yR-byAb5FhdgKXGEFCWnivtYmA7y3c1nPLxu5aNH5GATOnPyuCgvytkhMTfG8S9KshFGX0nYYKv3YgTtxGWCO6VW4CZs-IccGTAgy-VMppbv_PtXzHzYk5r7l8ziNWYxoTXtfk0c73N_mXtW08mRgh1KjwoYeMpjnG7fOy4L4oKdC93S8fF6uGeMI3E3L6Ur53qx_3kgjrdM-0Ryyl3p5tpZURWveOcUTTCPhFy0Nsm2JvFvH2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206796ec3e.mp4?token=gEmNIf4wsG-e6-FM5-dvBBWAuavpV0MtAZvQjZFyWYs9QMJvne1ve39nZCFwMpXAcy45dYMsdygkyh0ZYvNzdkxp95FX5aAhi97yR-byAb5FhdgKXGEFCWnivtYmA7y3c1nPLxu5aNH5GATOnPyuCgvytkhMTfG8S9KshFGX0nYYKv3YgTtxGWCO6VW4CZs-IccGTAgy-VMppbv_PtXzHzYk5r7l8ziNWYxoTXtfk0c73N_mXtW08mRgh1KjwoYeMpjnG7fOy4L4oKdC93S8fF6uGeMI3E3L6Ur53qx_3kgjrdM-0Ryyl3p5tpZURWveOcUTTCPhFy0Nsm2JvFvH2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات عرضه اولیه اوراق سلف موازی استاندارد سکه
🔹
عرضه اولیه اوراق سلف موازی استاندارد سکه بانک مرکزی با نماد «عسکه ۲» از ۱۸ شهریور در بورس کالا انجام می‌شود. این عرضه شامل معادل ۱۰۰ هزار قطعه سکه تمام بهار آزادی در قالب ۱۰۰ میلیون ورقه است و به روش حراج تک‌قیمتی انجام خواهد شد.
🔹
دامنه نوسان روز عرضه ۵ درصد و دامنه نوسان معاملات ثانویه ۱۰ درصد است. معاملات ثانویه نیز از ۲۱ شهریور تا ۱۸ آذر ادامه خواهد داشت. خریداران می‌توانند با کد بورسی در این عرضه مشارکت کنند./فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/688336" target="_blank">📅 23:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688335">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WI-d_ZRBAafMOdmltF-OZp6h8a1FNgb6sHaN-vucUY_xZwd1I7Evt3sBJr5b-tCBXBmNXjxzKhf5S4dt84AqIBA-3dd7sxI4L_1zFqkG-T6T1b6tOmDz52j-HHL_f51-IWDOPrddeaH-eVucfQZRH1EcNsc8LnVRTkN9fYKlC5i0xRjU9d9z8Xmtx_njI97OCOnhakjIgiCiD4iV6d0PVpQugHQxqXndy5aa3eeVJe879m-DclU-AA2vA-4DceB-yiLtQ757PoRNoAAKLK55eFX9E42ZBaZv1-wNXkXXVRgYkdiy_F83vOigMnbVO5HQPZ4bvGcv_ivDOrw9Ts1ruA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تنها یک دلار تا نفت ۱۰۰ دلاری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/688335" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688334">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ذخایر خون مطلوب گزارش شد
عمر علیپور اقدم، عضو کمیسیون بهداشت و درمان مجلس در
#گفتگو
با خبرفوری:
🔹
از جنگ رمضان تاکنون بیمارستان‌ها، اورژانس، هلال‌احمر و سایر دستگاه‌های خدمات‌رسان در حالت آماده‌باش کامل قرار دارند.
🔹
از نظر ذخایر خون نیز وضعیت مطلوبی داریم و با کمک مردم تاکنون کمبودی احساس نشده است.
🔹
همه دستگاه‌های خدمات‌رسان پای کار هستند و برای حوادث احتمالی آینده نیز آمادگی کامل دارند و بنابراین جای هیچ‌گونه نگرانی وجود ندارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/688334" target="_blank">📅 23:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688333">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
حمله به دومین شناور در اطراف جزیره خارک/ هنوز اطلاعات دقیقی از شناور در دست نیست/ دانشجو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/688333" target="_blank">📅 23:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688332">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
تایید حمله آمریکا به نفتکش ایرانی/فاکس‌نیوز به نقل از منابع آمریکایی: نفت‌کش‌های ایرانی را در نزدیکی خارک و جاسک هدف قرار دادیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/688332" target="_blank">📅 23:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688331">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
احتمال استیضاح ترامپ/ سناتور آمریکایی: اگر جمهوری‌خواهان مجلس نمایندگان را حفظ نکنند، ترامپ استیضاح خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/688331" target="_blank">📅 23:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688330">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
سپاه یک زیردریایی بدون سرنشین dive-LD آمریکا را به غنیمت گرفت/ سنتکام بیانیه داد
👇
khabarfoori.com/fa/tiny/news-3243787
🔹
هدف گیری یک نفتکش ایرانی در نزدیکی جزیره خارگ
👇
khabarfoori.com/fa/tiny/news-3243816
🔹
روضه‌خوانی فرزند آیت‌الله مجتبی خامنه‌ای برای مادرش و بی تابی برای رهبر شهید
👇
khabarfoori.com/fa/tiny/news-3243644
🔹
این مداح گم شده است!
👇
khabarfoori.com/fa/tiny/news-3243800
🔹
تصویری از وضعیت جسمانی نامناسب علی اکبر ولایتی
👇
khabarfoori.com/fa/tiny/news-3243638
🔹
صفحه ویژه اخبار پربازدید وبسایت خبرفوری را اینجا کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/688330" target="_blank">📅 23:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688329">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6ax8r96VPSFT2A53X64h2Z_K8RoIS5GWxra59bhUSsX5dHYTo0UBnHGPb9Gxhc9e4uxynFsxw4KQC6mZP96MFM57trkvoNaXPhXnAZISKCSvKTU0FftqCaHu0Lm5XahbuWyBgkzhht41X69G5pEELr5vqBSlpsEZtrcPYxBOwWROcAKP1ZHXODHItZLJmt2FfgEuoGiSbHt15z632np4VBe3NnbvaVtOrE-HgJ883iH7eNFaF5lU1-dSoFGTItNQq1zZSFkVe4k6rdM3k5QfuBb9AANvMOpk4quW_l8hywgTtUCIWJwfd5DYumohUqw5s6oqE3rk-ZGiDBU9stUGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فتحی: رسایی باید حد ادب را نگه دارد
محسن فتحی نماینده مجلس:
🔹
جلسه تبادل نظر نمایندگان که شب گذشته در حرم عبدالعظیم حسنی برگزار شد، موثر و مفید بود و نمایندگان در خصوص مهمترین مسائل کشور بویژه شرایط اقتصادی مردم تبادل نظر کردند.
🔹
متاسفانه از توهین آقای رسایی به همکاران محترم متعجب شدم؛ ایشان باید در گفتارش حد ادب را نگه دارد.
🔹
وقتی جلسه‌ای با استقبال همکاران و با حضور ۲۰۰ نفر از نمایندگان مردم تشکیل می‌شود باید از این فرصت استفاده کرد و به نفع مردم و کشور قدم برداشت نه اینکه با نقار، توصیه‌های رهبر شهید و رهبر معظم انقلاب در خصوص لزوم رعایت وحدت و همدلی و انسجام را زیر سوال برد./ ایلنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/688329" target="_blank">📅 23:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688327">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gv_7wEJQUPbnSmzk9pxmf3umQB0iycG8lNhAwOk-YTpSk2igVw04TRenefJ0Zps4tA5STMJifttZJxcAjRn8lfLKgGdN-dbgz7HHNx-grBzmsomJVqCl7hpJzg3Y7IFdMCq2Tc0ecs6TEyxBVblwxXJdL5jqe3r_fVRZ16Arq9BdhlGiWXpa45B_EzYlM8FWxbAVev5az3LpBWsl5bbUph322AlwhdS-G6hQHzcXlZNrBLC53hgRBGbusUMSvVTaU1qID4Hz3THLjcCGwY4tfyciM8k3rC6qrHLrG5SJFNlBmvSKK4IMm43Qj9LVucW_865p-dnDxgqxiRlVMOfB7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار فوری نیروی دریایی سپاه در پاسخ به اقدام بزدلانه ارتش تروریستی امریکا در حمله به نفتکش‌های جمهوری اسلامی ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/688327" target="_blank">📅 23:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688326">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
منشا صداهای شنیده شده در جاسک از روی دریا است
🔹
ساعتی پیش صدای انفجارهایی در شهرستان جاسک شنیده شد که طبق اعلام استانداری هرمزگان، منشأ این صداها مربوط به اتفاقاتی در دریا است و اتفاقی در سطح شهرستان رخ نداده است./ مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/688326" target="_blank">📅 23:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688325">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
وقوع چند انفجار در آرامکو  فایننشال تایمز:
🔹
پالایشگاه جیزان با ظرفیت ۴۰۰ هزار بشکه در روز هفته‌هاست به‌دلیل حملات از مدار خارج شده و حمله جدید، بازگشت آن به فعالیت کامل را دشوارتر کرده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/688325" target="_blank">📅 23:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688324">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
المیادین: عربستان ظرف سه روز بیش از ۱۳۵ حمله هوایی علیه یمن انجام داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/688324" target="_blank">📅 23:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688323">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
حمله موشکی آمریکا به یک نفتکش ایرانی در نزدیکی جزیره خارگ
🔹
یک نفتکش کوچک ایرانی در فاصله ۴ مایلی جزیره خارگ، هدف حمله موشکی ارتش تروریستی آمریکا قرار گرفت. این نفتکش در محدوده لنگرگاه جزیره خارگ مورد اصابت پرتابه نیروهای آمریکایی واقع شد.
🔹
منابع محلی اعلام…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/688323" target="_blank">📅 23:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688322">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ذخایر سوخت مایع نیروگاه‌ها افزایش پیدا کرد
آرش نجفی، رئیس کمیسیون انرژی اتاق بازرگانی ایران در
#گفتگو
با خبرفوری:
🔹
قطعی برق در زمستان به میزان سوخت مایع بستگی دارد، زیرا شرکت پخش و پالایش فرآورده‌های نفتی ذخایر سوخت مایع نیروگاه‌ها را به سه ماه افزایش داده است، اما اگر سوخت مایع کافی نباشد یا استفاده از مازوت باعث اختلال فنی شود، ممکن است با قطعی برق مواجه شویم.
🔹
با توجه به پیش‌بینی پاییز و زمستان سرد نگرانی اصلی ما از اواخر بهمن و اسفند است که هوا گرم می‌شود و این گرما تا تابستان ادامه خواهد یافت، بنابراین باید برای مدیریت مصرف در ماه‌های گرم سال نیز برنامه‌ریزی کنیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/688322" target="_blank">📅 23:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688321">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
شانس جنگ گسترده بین ایران، آمریکا و اسرائیل چقدر است؟ / این نقطه، محور اصلی درگیری واشنگتن و تهران خواهد بود
یک کارشناس مسائل سیاسی در گفتگو با خبرفوری:
🔹
واشنگتن پس از ناکامی در دستیابی به اهداف نظامی خود، فشار اقتصادی و تهدید نظامی را همزمان دنبال می‌کند.
مشروح گفتگو را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3242652</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/688321" target="_blank">📅 23:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688320">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
حمله موشکی آمریکا به یک نفتکش ایرانی در نزدیکی جزیره خارگ
🔹
یک نفتکش کوچک ایرانی در فاصله ۴ مایلی جزیره خارگ، هدف حمله موشکی ارتش تروریستی آمریکا قرار گرفت. این نفتکش در محدوده لنگرگاه جزیره خارگ مورد اصابت پرتابه نیروهای آمریکایی واقع شد.
🔹
منابع محلی اعلام…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/688320" target="_blank">📅 23:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688319">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/829194f886.mp4?token=Cb5H8LGlm_cubbWntssUzf2KJu4XUONq7a41gH4F1C1DhC4wtFd5-BfrWPS1lsgQlxt-ldo4rQHVif5E0HrZvEqGn77TvyJ0HXDAeCmBMwIstNySsHTymCsuxm2mkLrZUgL6K0RcFsC2U4pyUj9Zu5e4rNlh4RH68ZLkKEFvIuTzTmWa15rsJWUawhzCI50vYsFu8ct6ypQeIEYG9b-HHoLYfBOJjdg7pmV4pSSCaZ6yHYnlaUOfKbG03aPBCvRRmVq7TxRLNUghG0AjXFvcoCCIzYDVQznKoDaHLFvCmkfRVt2TXvQJPF-t0UoqSAcRsjR-lbMwotHhSXpXurpYz1F0R2W9w9Pp5K1rQzHfGqVeZN0_xwPBcpJzunb8zhxQDkksU_IhJ0SvGoAdA6J8Bl33eJqOik5wrSKhZa6yZYkiFOjwZprXzPKQbuqGI2e7iYI9ftqekjbUeC2UIenXo4LQ2W_VGSoF4o25JMsaqBWo-zWBTXhgqh9fUelwKxIkJ4dXv3zmFplR-rN55ULEUGGWBFWpPrpIpmK8H41TpthAn8ke8qJwpd2QZqTWI-ayZc08HZKjCvwwl4yK6sMg3GvbwoXUKzqAHRt6l53ap_btJV21IhDaaTE99mg0_N63mZcw3Zm3qk4s7DVCkFNUOuUdjAf9uhA9jFEogG9FHSY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/829194f886.mp4?token=Cb5H8LGlm_cubbWntssUzf2KJu4XUONq7a41gH4F1C1DhC4wtFd5-BfrWPS1lsgQlxt-ldo4rQHVif5E0HrZvEqGn77TvyJ0HXDAeCmBMwIstNySsHTymCsuxm2mkLrZUgL6K0RcFsC2U4pyUj9Zu5e4rNlh4RH68ZLkKEFvIuTzTmWa15rsJWUawhzCI50vYsFu8ct6ypQeIEYG9b-HHoLYfBOJjdg7pmV4pSSCaZ6yHYnlaUOfKbG03aPBCvRRmVq7TxRLNUghG0AjXFvcoCCIzYDVQznKoDaHLFvCmkfRVt2TXvQJPF-t0UoqSAcRsjR-lbMwotHhSXpXurpYz1F0R2W9w9Pp5K1rQzHfGqVeZN0_xwPBcpJzunb8zhxQDkksU_IhJ0SvGoAdA6J8Bl33eJqOik5wrSKhZa6yZYkiFOjwZprXzPKQbuqGI2e7iYI9ftqekjbUeC2UIenXo4LQ2W_VGSoF4o25JMsaqBWo-zWBTXhgqh9fUelwKxIkJ4dXv3zmFplR-rN55ULEUGGWBFWpPrpIpmK8H41TpthAn8ke8qJwpd2QZqTWI-ayZc08HZKjCvwwl4yK6sMg3GvbwoXUKzqAHRt6l53ap_btJV21IhDaaTE99mg0_N63mZcw3Zm3qk4s7DVCkFNUOuUdjAf9uhA9jFEogG9FHSY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای استانی که سه‌برابرِ نیازِ خود سوخت تولید می‌کند اما بنزین در خارج از آن راحت‌تر پیدا می‌شود!
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/688319" target="_blank">📅 23:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688318">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3GkEKEG8DB3kHaypqjNSUBEoaHrtWHhleSoUniPCIXEMnkwERGS-a1mGrwKVWC51AlJmiFGxEdBq3QlrMkEHXRcjgUH4uakqSVn5vGuMqhF4noAQWN45jx2iNt2KzsbqXqlbtlL_ZkxRbHt63g0LF0YsIgMd5UgqJpy21fNgudcgm_JF4P5fTatK4zvNkSfPU7WINJJV_NZ4jOibP7kL7aFb7wXBDDG9ZDA6vijW9SJgaK0qrAzAZYfw2wSagmKZYzMsyjSFL4q-Ho521eOqsHqdMiV1EwGF1SCeakWEVkWUR82wmJLgaPCV4IVla0YlqGhOvJhtum3-nGP6wOj2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبل از اینکه یک حادثه هزینه سنگینی روی دستتان بگذارد، خانه‌تان را با «جام آسیا» بیمه کنید
آتش‌سوزی، زلزله، انفجار، سرقت، ترکیدگی لوله آب از خطراتی هستند که می‌توانند به خانه و اثاثیه شما خسارت وارد کنند.
🛡️
طرح جام آسیا؛ بیمه جان و مال
با پوشش‌های متنوع و
۵ بسته بیمه‌ای
، متناسب با نیاز و شرایط شما.
از سرمایه‌ای که برایش سال‌ها زحمت کشیده‌اید، امروز محافظت کنید
📲
برای مشاوره، استعلام و خرید بیمه جام آسیا کلیک کنید
👇
👇
https://online-li.bimehasia.ir/issue/jaam
https://online-li.bimehasia.ir/issue/jaam</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/688318" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688317">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYUsf03JPWZQ90P_vTzemf5UMZnMqS4YDpE07ktV6OM1NoNrE6G9HYZHJxqvAHOpTEMc-P0Ep8Z9ooXwpsACgVbPfKKkqULuFmbyFAh_cfFV9Zlonmb0JWoKw71qHVpfDmn0tsu7Oj2ryE3fW2lz9OByjKdvpZYZ-xJoIVYVLbS6Um6bK1peHMbvsJDCGvl0HcWybrbiHNbZCAR2D9kL8tx0kT71pX5Qamlb5cJ0z11NaLIqifgVFaE6wwJE3TtD6Oh4M3L-smr5eFj5aR11Ic5MmBrKhWE5TCT4Q4vbkh_NJVq2xv6r5WC7xoyYzaKkgmPkQ2tE2RI36iUpqHxK0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکتر محمد محسن صدر، رییس سازمان فناوری اطلاعات ایران، در شبکه اجتماعی خود با اشاره به کارت زرد مجلس به وزیر ارتباطات نوشت:
«کارت زرد مجلس، حق قانونی نمایندگان و فرصتی برای رفع کاستی‌هاست؛ اما قضاوت درباره عملکرد یک وزارتخانه باید بر پایه همه واقعیت‌ها باشد. وزارت ارتباطات در شرایطی کم‌سابقه، از حفظ پایداری شبکه در روزهای جنگ تا توسعه ارتباطات روستایی، پیشبرد فیبرنوری و بازسازی زیرساخت‌های آسیب‌دیده را دنبال کرده است. نقد منصفانه زمانی شکل می‌گیرد که موفقیت‌ها و چالش‌ها، هر دو در کنار هم دیده شوند.
ایستادگی برای دفاع از حقوق مردم اگر هزینه هم‌داشته باشد سند افتخار است.»
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/688317" target="_blank">📅 23:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688316">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
حمله موشکی آمریکا به یک نفتکش ایرانی در نزدیکی جزیره خارگ
🔹
یک نفتکش کوچک ایرانی در فاصله ۴ مایلی جزیره خارگ، هدف حمله موشکی ارتش تروریستی آمریکا قرار گرفت. این نفتکش در محدوده لنگرگاه جزیره خارگ مورد اصابت پرتابه نیروهای آمریکایی واقع شد.
🔹
منابع محلی اعلام کردند که این حادثه خوشبختانه هیچ‌گونه خسارت جانی به‌ همراه نداشته و کارکنان نفتکش در حال تخلیه هستند.
🔹
جزئیات تکمیلی درباره میزان خسارت وارده و ابعاد دقیق این حادثه توسط دستگاه‌های مسئول در حال بررسی است و اطلاعات متعاقباً منتشر خواهد شد.
جزئیات بیشتر
👇
khabarfoori.com/fa/tiny/news-3243816</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/688316" target="_blank">📅 22:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688315">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
۱۲ کشور خواستار محدودیت تجارت با شهرک‌های غیرقانونی اسرائیل شدند
🔹
فرانسه، بریتانیا، کانادا و ۹ کشور اروپایی دیگر در بیانیه‌ای مشترک از اعمال یا حمایت از محدودیت‌های تجاری علیه کالاهای شهرک‌های اسرائیلی در کرانه باختری خبر دادند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/688315" target="_blank">📅 22:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688314">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
آمریکا در حال حمله به نفتکش‌های ایران/ پایگاه صهیونیستی آی‌۲۴: نیروهای آمریکایی در حال حمله به نفتکش‌های ایران در تنگه هرمز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/688314" target="_blank">📅 22:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688313">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
سخنگوی قرارگاه مرکزی خاتم‌الانبیا: ارتش تروریست آمریکا تهدید کرده است که سه فروند نفتکش ایرانی را هدف قرار خواهد داد
🔹
در صورت هرگونه تعرض به کشتی‌های ایرانی، نیروهای مسلح جمهوری اسلامی ایران پایگاه‌ها و منافع آمریکا را در منطقه به شدت هدف قرار خواهند داد.…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/688313" target="_blank">📅 22:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688312">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32b385f32d.mp4?token=ihMnGU9XYmuL6S1XZY33rjBuyaWZEdF27FtqO_moxC6R3wNVzNEk0Es2QbLcy96dqaa2LBTPTYo7wB51XOCXZUkAX6rHakDmm-z-QzaDWT6QoFHOmMNtiz2cqcJVCNlIjT6Au3tMcUxHv7u2DY_sAIJDGlSr86W5LBdHWzeelut5RxwVnRe1eVtQYNCOJC41iqLT0M7c-Vv2iaX0SlWdKRz4ixAM8nRdygY2-tqF-oCjGgm_AVtl_UE62k-OjWmtx1DtRGoKLJkAHd_EKKwx8oPrco3TiGQac0YQUtdz6McpQSBbaXIuRBLD2cgZ8nrxoXJC5qGSOG0lENag2zyRcYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32b385f32d.mp4?token=ihMnGU9XYmuL6S1XZY33rjBuyaWZEdF27FtqO_moxC6R3wNVzNEk0Es2QbLcy96dqaa2LBTPTYo7wB51XOCXZUkAX6rHakDmm-z-QzaDWT6QoFHOmMNtiz2cqcJVCNlIjT6Au3tMcUxHv7u2DY_sAIJDGlSr86W5LBdHWzeelut5RxwVnRe1eVtQYNCOJC41iqLT0M7c-Vv2iaX0SlWdKRz4ixAM8nRdygY2-tqF-oCjGgm_AVtl_UE62k-OjWmtx1DtRGoKLJkAHd_EKKwx8oPrco3TiGQac0YQUtdz6McpQSBbaXIuRBLD2cgZ8nrxoXJC5qGSOG0lENag2zyRcYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر رضایی: تنگه هرمز، تنگه عزت ایران است...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/688312" target="_blank">📅 22:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688311">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e0fac0ecb.mp4?token=m7tadJBiZ8DQsfSOp8n-FNsiwfYn-yLOQTppN8C9HTjn5be0QewTlpiuM9bbqqbmw3PK96_0gwUtnVexNGdG4cgRZsZAFNSl4bY6fL4Y6ZB2LeX7h51bPvH6dJUA_mPcxLpt4rppomKzKXr-AvJEqXFrq7GyPzpKPGI4etsFqX3BRB4XdZPDmE9acnEOvEcNiahlQUhf0dZulsivs7KVKJdZh5USPSAKr9mCnj7HHuwG3fTNzrY6zNBZshxIn9XbgQwHeF9LDYf32pRNFREqP-sWLmZHciakE7CvfbE-FKWUGkoMONUMQhJxbiiY75zzizY8Urdo56fCrDtesdwKmj727yqHcqea9ZvhdgACdmpgWInuJEWso68xjI6py8lHV0qdRPeVcmfRm1RLHWguPq6wQJi7XEuF_kyK3bkm2qVapZVwKl2tvklRErHPxqx7D-V9pMz-SjpjTRfJNq17b08htZx5TQH98Se4sEq40Xnaq31ua6Pw9mc5MA27kyhqxJe5NfffNaI9kzMgCaoo9LC93NqwdDtwN4Q7GuE3f2h0V0JelXvdz9Qo4r2CTfMQtoBAgPH5vklYB4eEKAFQgGJXzIIpFxd7yCkxXC9V1ocUhP1DBVv7m4Jm_D3w57FUqYWrIftgeQbMgPlduW1tHsmyVZ7nQPezVya6joJPJzI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e0fac0ecb.mp4?token=m7tadJBiZ8DQsfSOp8n-FNsiwfYn-yLOQTppN8C9HTjn5be0QewTlpiuM9bbqqbmw3PK96_0gwUtnVexNGdG4cgRZsZAFNSl4bY6fL4Y6ZB2LeX7h51bPvH6dJUA_mPcxLpt4rppomKzKXr-AvJEqXFrq7GyPzpKPGI4etsFqX3BRB4XdZPDmE9acnEOvEcNiahlQUhf0dZulsivs7KVKJdZh5USPSAKr9mCnj7HHuwG3fTNzrY6zNBZshxIn9XbgQwHeF9LDYf32pRNFREqP-sWLmZHciakE7CvfbE-FKWUGkoMONUMQhJxbiiY75zzizY8Urdo56fCrDtesdwKmj727yqHcqea9ZvhdgACdmpgWInuJEWso68xjI6py8lHV0qdRPeVcmfRm1RLHWguPq6wQJi7XEuF_kyK3bkm2qVapZVwKl2tvklRErHPxqx7D-V9pMz-SjpjTRfJNq17b08htZx5TQH98Se4sEq40Xnaq31ua6Pw9mc5MA27kyhqxJe5NfffNaI9kzMgCaoo9LC93NqwdDtwN4Q7GuE3f2h0V0JelXvdz9Qo4r2CTfMQtoBAgPH5vklYB4eEKAFQgGJXzIIpFxd7yCkxXC9V1ocUhP1DBVv7m4Jm_D3w57FUqYWrIftgeQbMgPlduW1tHsmyVZ7nQPezVya6joJPJzI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امنیت خلیج فارس بدون همکاری کشورهای منطقه امکان‌پذیر نیست
دکتر گاردونیو، استاد روابط بین‌الملل دانشگاه UNAM در
#گفتگو
با خبرفوری:
🔹
تنگه هرمز یک اهرم مهم راهبردی برای ایران است، اما امنیت خلیج فارس تنها با همکاری کشورهای منطقه امکان‌پذیر خواهد بود.
🔹
حضور نظامی آمریکا در خلیج فارس نه‌تنها امنیت ایجاد نکرده، بلکه به افزایش تنش و درگیری در منطقه منجر شده است.
@Fori_Tv</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/688311" target="_blank">📅 22:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688310">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd71fc45ab.mp4?token=AxMRjGFt4tjqKduUoTpvLxp9vwRVq-IZ67hpilb527H4IWhO5SNa2-rR-RcD828nXxPw4rbu5AiFp-cBtTGqL5RR5NIlvPV2TWIJKUl8E3QxozzTCc2NSIYfaeGElEc1x13KXNNURHQ1JdZd0ypq09aBT-YudI6t1jnBq9zOssgjcJnYoA--E-V-OiCBzyT15bUkezSkDzZZHTDlgGuKdQKGAeoV9KwRgsdMBJ-fwWGdhnby4xS4QHCSFQEC2wdoSqVuCfytCpKsowpW8-k4usnRKA-seNXEDa5ajCc4y-H5F3b6O2LHstxD_bNEqtAyJIvSJpigQDpsTvrdv7TrJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd71fc45ab.mp4?token=AxMRjGFt4tjqKduUoTpvLxp9vwRVq-IZ67hpilb527H4IWhO5SNa2-rR-RcD828nXxPw4rbu5AiFp-cBtTGqL5RR5NIlvPV2TWIJKUl8E3QxozzTCc2NSIYfaeGElEc1x13KXNNURHQ1JdZd0ypq09aBT-YudI6t1jnBq9zOssgjcJnYoA--E-V-OiCBzyT15bUkezSkDzZZHTDlgGuKdQKGAeoV9KwRgsdMBJ-fwWGdhnby4xS4QHCSFQEC2wdoSqVuCfytCpKsowpW8-k4usnRKA-seNXEDa5ajCc4y-H5F3b6O2LHstxD_bNEqtAyJIvSJpigQDpsTvrdv7TrJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون ارتباطات و اطلاع‌رسانی دفتر رئیس‌جمهور: رسانه ملی به بلندگوی آن یک نفری تبدیل شده است که در شعام مخالف تفاهم‌نامه بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/688310" target="_blank">📅 22:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688309">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f1d070c8.mp4?token=ayjIFJZC9urTf0NB77tmmgREMAz40Vb0cNx6SG6mSBbIKAHKJdTjfp7qlfs6jov79JzaSq2kMwJi4jVggvSpkAhlxIFYzp8gLcZYQ6M6DAXHYfEBrFo4G1i70VKAceJbj9uGpNS94I1GJGjpchVgGyMrnHn3Hxavdp9S3fsU1gJBnGuPJyMg6g1C4Gi76poo6CMUfRxYkSZANiW83HQfrkDSF4q-Nv3dnGj6D425XdKkT2MehuKpqSi5q8j_u3SkYsSdpOAMkR8UXi4PzRrZ0XRZhiYEufaSRdUAqeU6mx8WzQDt0s-ki9Vi-myOPfsWqOkQwhB4A0fnUuLKy_nSnINKLFXetgpDPu6LlmmRGfbDuXF9zQoJzwo0lBO38bcyUlGYhU1YBIDra-Dx8yFf8aE7ft3IBiunf8oldfPtqYpPfcFTJxsEKkcmcXxwFJ9ndy66eEnfdfUrK73x3YJcawQinCCdNpEfGXgF6jTyub4jHVzA4SUqE4KNp8NSeGYeKu7PkLhksFDS8LmtlFFxf3z7ZDZlaM7W4ZjGON8Ki8-TtYfQPHulMwjDzRZopiIyltm_EtznemYQMDW4Idpkq35ZWzlJEaIrok5vuF_k12O9Ua7Osy2VX_zzy-RJ8pxYY7eh1Q8INHzmozqQRUngHW6uW8YbDOyolZyhcZ1q9VI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f1d070c8.mp4?token=ayjIFJZC9urTf0NB77tmmgREMAz40Vb0cNx6SG6mSBbIKAHKJdTjfp7qlfs6jov79JzaSq2kMwJi4jVggvSpkAhlxIFYzp8gLcZYQ6M6DAXHYfEBrFo4G1i70VKAceJbj9uGpNS94I1GJGjpchVgGyMrnHn3Hxavdp9S3fsU1gJBnGuPJyMg6g1C4Gi76poo6CMUfRxYkSZANiW83HQfrkDSF4q-Nv3dnGj6D425XdKkT2MehuKpqSi5q8j_u3SkYsSdpOAMkR8UXi4PzRrZ0XRZhiYEufaSRdUAqeU6mx8WzQDt0s-ki9Vi-myOPfsWqOkQwhB4A0fnUuLKy_nSnINKLFXetgpDPu6LlmmRGfbDuXF9zQoJzwo0lBO38bcyUlGYhU1YBIDra-Dx8yFf8aE7ft3IBiunf8oldfPtqYpPfcFTJxsEKkcmcXxwFJ9ndy66eEnfdfUrK73x3YJcawQinCCdNpEfGXgF6jTyub4jHVzA4SUqE4KNp8NSeGYeKu7PkLhksFDS8LmtlFFxf3z7ZDZlaM7W4ZjGON8Ki8-TtYfQPHulMwjDzRZopiIyltm_EtznemYQMDW4Idpkq35ZWzlJEaIrok5vuF_k12O9Ua7Osy2VX_zzy-RJ8pxYY7eh1Q8INHzmozqQRUngHW6uW8YbDOyolZyhcZ1q9VI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از طلا و نقره تا خدمات بیمه و کسب و کار، روایت مسیر تحول داریک
محمد زرین مشاور برندینگ و استراتژی داریک در
#گفتگو
با خبرفوری:
🔹
طی سه سال اخیر یکسری خدمات جدید به برند داریک اضافه شد و استراتژی‌های کسب و کار تغییر کرد.
🔹
لازم بود متناسب با این موضوع، هویت بصری داریک نیز تغییر کند تا با تغییرات استراتژی همسو باشد و به همین منظور بحث ری‌برندیگ رقم خورد.
🔹
داستان برند ما این است که در این آشفتگی و پیچیدگی‌های مالی، برند ما نقطه امنی باشد برای مخاطبان و این داستان هم در خدمات و محصولات خواهد بود و هم در هویت بصری برند آمده است.
🔹
داریک به طلا و نقره محدود نخواهد ماند و خدماتی چون بیمه، لندتک، آکادمی و ... را نیز ارائه می‎دهد و در فرآیند تغییر در حال توسعه بحث انبار فلزات هوشمند گران‌بها هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/688309" target="_blank">📅 22:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688308">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MT_AI1yU7PVIfTAGl-368BlE2I4M8Uvn7EgKhcGUxrky1bpTnET7Cltc3fg5wzOkxqRJ8Odoi7-zirng3gMj1HX2Ouf_FO8GVXknng8ZtTT9EjuM1yFRDZFyY8JuESSpIi3K6JHU3HBiLEpWbpLjiM_A_FiwesFlZMwBqGiJWzdo_GtsRhyEupvpZJ4GzTYmX3yIiR8WAW8WfTeGs1HoK_BnkDJcYnOp-cJCZUcX0OTy3pKzAVPYIKReczrhq3NIJrrTjExCnSS0XMxhiKx2IuWyYrBwJUqc1paO5UsNJTR0EDtn7ELB9YXVOVx8NBAgyupR514dqrO-JGyktbSb4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تو که لالایی بلدی، چرا خودت خوابت نمی‌بره؟
🔹
نتانیاهو سال گذشته وعده داده بود تجربیات اسرائیل در مدیریت آب را با مردم ایران به اشتراک بگذارد؛ حالا در سالگرد آن اظهارات، گزارش‌ها از ازکارافتادن ۵ آب‌شیرین‌کن از ۶ آب‌شیرین‌کن اسرائیل و احتمال بروز بحران آب شرب خبر می‌دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/688308" target="_blank">📅 22:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688307">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CY0EJ82VKfLjfmcd61Sn-UHEb1w2N12nLHwF0faH4Srs_rcoifhUvCJ2sVUtHOmG6TagpuSJ-KnqZ1UanUpctmLfsO8gkHfWqWUVhzozZ-9lP7CJx2f2cobybSFyQknrj9Udy2h_qIQ7LY52xce6WzCmRmdxNaFrwVbsKJMuuTHpljS0bMUd8JgM5_QzyISjF28ehASnF2VBwjWMvuK-CmHj_Zj_L4sTYMg5IkoJ4X8xNNiOlf1askSwYFVLaQMNkxapHj3D2HaENWioahKpYWjZdVaYqR11cv2STtsfIPZvS8fJ2vZiXNhBbO8w479QUL8Db_KVH3VlaHWN_YH2XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیر دریایی آمریکایی در دیوار آگهی شد!
🔹
واکنش طنز کاربران فضای‌ مجازی به شکار زیرسطحی دشمن آمریکایی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/688307" target="_blank">📅 22:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688306">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
شنیده شدن صدای چند انفجار در جزیره خارگ
🔹
صدای چند انفجار دقایقی پیش در نقاطی از جزیره خارگ شنیده شده است. تاکنون اطلاعات رسمی درباره منشأ و علت این انفجارها و همچنین خسارات احتمالی آن منتشر نشده است./ مهر
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/688306" target="_blank">📅 22:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688305">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksIhexFLDxR5QJkDE_1Iw2e0jTYFTLU0PF404v2t2IDIUfoG4N5Xe8WhF7CZwI7f9Ij79zXmFDy_5H4tJOAHHDfTrjBCeBjtVog4iMsTeCuR47yhOYvDozRv1TZERNFcdt6bJvq63cQ8qFRyuDC9c3FY_YjySlyHzPxy26HyHi_ZeLslRh4b-fJ7ILPXw77PDBAeD6_L9RbiMxNVajvY4JYSCwp3OK8mjUMtOFD9unjRXQxJa9jd-2InhcjLiqBvtGnNoP8dxmMVB8Wc26GRBu9JDr2K30W4T5J4EecH6IjyTghSwdA_0hUTjg4D2q8apHsbfjhTAlHBbOCdo8vLlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی قرارگاه مرکزی خاتم‌الانبیا: ارتش تروریست آمریکا تهدید کرده است که سه فروند نفتکش ایرانی را هدف قرار خواهد داد
🔹
در صورت هرگونه تعرض به کشتی‌های ایرانی، نیروهای مسلح جمهوری اسلامی ایران پایگاه‌ها و منافع آمریکا را در منطقه به شدت هدف قرار خواهند داد.…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/688305" target="_blank">📅 22:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688304">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5GXdKMLJlqEmgaSZ5ll9JvFrUPPNW2TUKHGCQbGDn4YA7dGFY6J1Us1fJwZfdc5QhIfXGu_3SM6pTq7uVHNkSiKRwgYC-RCu62peATE9ytcHYicsLfJhVpanwYaWx9L1dWw2mdG33JkDJd9tkLePY1vPGkR4r8Dphz8tS0vGlA1CzShKmRl84MK0sNahhGg4KAuLb5pSBr6ysXYOBkcHrLdvxSUK5Fhr_KYglffCaH8TzlPLI_92EPWsd40KODtCiuiMMM6hY7nnaF6kRa2HVTDBWGTO0Mx0rWHAwxoFG6L7DdCIxie4VNcvgH0GF4QbnR4wWpDWv19ffNH3BfOSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمجید پاتریک هنینگسن، تحلیلگر مسائل بین‌الملل از شاهکار امروز نیروهای مسلح ایران: یک غنیمت دیگر برای ایران
🔹
آنها موفق شده‌اند پیشرفته‌ترین زیردریایی بدون سرنشین آمریکا را به تصرف خود درآورند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/688304" target="_blank">📅 22:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688303">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
شنیده شدن صدای چند انفجار در جزیره خارگ
🔹
صدای چند انفجار دقایقی پیش در نقاطی از جزیره خارگ شنیده شده است. تاکنون اطلاعات رسمی درباره منشأ و علت این انفجارها و همچنین خسارات احتمالی آن منتشر نشده است./ مهر
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/688303" target="_blank">📅 22:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688302">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ویدئو شرکت سازنده زیردریایی DIVE LD:زیردریایی شکار شده برای تولید انبوه  طراحی شده است
🔹
آمریکا برنامه داشت تا پایان سال ۲۰۲۶ تا ۲۰۰ فروند از زیردریایی بدون سرنشین DIVE LD را تولید کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/688302" target="_blank">📅 22:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688301">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
شکار یک فروند زیرسطحی هوشمند دشمن آمریکایی در تنگه هرمز   نیروی دریایی سپاه :
🔹
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/688301" target="_blank">📅 22:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688300">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
سخنگوی قرارگاه مرکزی خاتم‌الانبیا: ارتش تروریست آمریکا تهدید کرده است که سه فروند نفتکش ایرانی را هدف قرار خواهد داد
🔹
در صورت هرگونه تعرض به کشتی‌های ایرانی، نیروهای مسلح جمهوری اسلامی ایران پایگاه‌ها و منافع آمریکا را در منطقه به شدت هدف قرار خواهند داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/688300" target="_blank">📅 22:12 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688299">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CX4qvi1nltpRf71M3YocJJLJrOxZ0UldNswTlK-3aex89Lhk_HP6hYzJRzT2yGyizsRb9hMTQdGI4eVpX8e6mIIkJjGzdrX95GQ3d2c45uOZQRx0lHV_UVynaH_JLEg8MFdhMSE2Zo8leGdj_dce4UtfBoXt8qivCqDzHXtYJffUE4SdHKuoxdhM3fmVeOwo6H0heNbq9XFmEmJjNBUnMkUkKMcemBWg6lx0D0lcYHAFxYm91CIZxuE5I0Xxo-q-lY9q6FMxmMHmsnQzl9AZn1jHeKlbnRb1KKmVwu_GskG5tbS7eT84Hea2IZL4h34Nb3z_-5IkC8BR3vXoCZDIqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: برنامهٔ زیردریایی‌های هوشمند آمریکا ناک‌اوت شد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/688299" target="_blank">📅 22:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688298">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4Xi1bX79RufLwMuRX2WV0yvvHsWC-aRBds9b3nc2z0tRveYfAvJeibvvR2hz1mBvJoU3guMu849kmd_xG3TXbTnFLV9bwLrkFfpGuQpKnehwXA-wE5jRf9gLVseYXvDZQxOCOh9lgfiAZp1uQZcVytZprUYmaUTYYM2MCQbhLnfnpO0fKeucUtKmN1ZHlicSUq_WCPsv3Rk2XW6ecOrNxCE-Bn9bgueaUGVEUjY5BFfxgqWccOihFN2Woc5nNJKD-xXfLfI2AXQXVzbIIiIe86QTuPeEqqpJfebT3RfU_qG2mc4zBI1HGw5Ol-04EyTSif97Bq2ItimO7RPpt2UhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اذعان صریح امارات به هماهنگی‌های امنیتی با صهیونیست‌ها
🔹
وزارت خارجه امارات در واکنش به گزارش‌ها درباره هشدار ابوظبی به رژیم صهیونیستی پیش از آغاز عملیات طوفان الاقصی، ضمن عدم تکذیب این گزارش‌ها، با افتخار از تبادل اطلاعات امنیتی با این رژیم سخن گفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/688298" target="_blank">📅 22:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688297">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/585a8df792.mp4?token=e8zsSFOe203j1F9ve_EiXQkmLO5XOwHkxLq2ydaLnlbIEqeiSYSBsuUblIGwr_0ftwl5ItT-ynfd32dyb_m--zvRVb_CNuv48sYsQc3xTt5gIGeX9ldDNkpVZxHCEwcY_FXaT7jnD3MVCvrK4abXfPGg6wuMC2x-BLM3N8K6aVfpQQMqxgTzBQb2uBncEdev7aWIjqUY9h1eXKDkup1AQr4idz9OMyWnKgnVgZnJ-FkizlVmJHKgw2ajIbdrXqLkSQQk7GwOYp7Jt-yeNlk3EDGcAoKl0iI7nftrx7xrhK7oZ17FzVsGfisdZaFNlvarWzyqkPRFQnB-KK9hd_MlsjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/585a8df792.mp4?token=e8zsSFOe203j1F9ve_EiXQkmLO5XOwHkxLq2ydaLnlbIEqeiSYSBsuUblIGwr_0ftwl5ItT-ynfd32dyb_m--zvRVb_CNuv48sYsQc3xTt5gIGeX9ldDNkpVZxHCEwcY_FXaT7jnD3MVCvrK4abXfPGg6wuMC2x-BLM3N8K6aVfpQQMqxgTzBQb2uBncEdev7aWIjqUY9h1eXKDkup1AQr4idz9OMyWnKgnVgZnJ-FkizlVmJHKgw2ajIbdrXqLkSQQk7GwOYp7Jt-yeNlk3EDGcAoKl0iI7nftrx7xrhK7oZ17FzVsGfisdZaFNlvarWzyqkPRFQnB-KK9hd_MlsjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همسر و فرزند، یا پدر و مادر؛ کدام‌یک اولویتند؟
🔹
وقتی ازدواج می‌کنیم، چطور باید تعادلی پیدا کنیم که نه حرمتِ خانواده‌ اصلی‌مان شکسته شود و نه زندگیِ مشترکمان آسیب ببیند؟/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/688297" target="_blank">📅 22:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688296">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
شکار یک فروند زیرسطحی هوشمند دشمن آمریکایی در تنگه هرمز   نیروی دریایی سپاه :
🔹
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/688296" target="_blank">📅 22:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688295">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5MHyY-Tqjl2Z66QdGZ5pFsY6YhQuN2m4UiUhzBX84EV5iPri2kgTzLqaDI5mGOBn3ofQGBTT-VffGjh4kLiHYcU8QfvBSCkkV90mpjFMxADwkK2FIZnnt9Fk_EAEtnHFeIU4gLcZhQlLKiZ0D8nViSMQcV00zf4LLHj0P3dMfmVV9XekJSnWr2D9B5SJxNVwZC1WhnZ9hzZ27wxbhDXzfVv4sI7MstwKdKtkFkCepdZODNQqDv2EG-jRwzhpvDduisLPASDLH_auQy_CxBa6ImMa9_ZC57xPzerxOHW9qmNQQ9QHlX2i21feKnhGmC_QrYVhrJyCkG4jTXtzb4RNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه عراقچی به راه‌حل خلاقانه آمریکا پس از ۴۷ سال تحریم و جنگ
جدی می‌فرمایید؟!
وزیر امور خارجه:
🔹
پس از ۴۷ سال تحریم، آمریکا به نیابت از اسرائیل وارد جنگ با ایران شد؛ جنگی که پیامدهای فاجعه‌باری برای آمریکا، از جمله برای جایگاه و اعتبار این کشور در جهان، به همراه داشته است.
🔹
پس از آنکه واشنگتن نتوانست با تحریم یا جنگ به اهداف خود دست یابد، راه‌حل «ابتکاری‌اش» این است: تحریم‌های بیشتر!! جدی می‌فرمایید؟!!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/688295" target="_blank">📅 22:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688294">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzZ1RLRNU4JLaY9w2McbU3OCv7-DsGf-aZ5o_zJJG4RMOF5wc1e7iJnlqOyE6GWkm-GIVzzrRycfqpoAP5ACclGfWS-hv13wZgfIsvCOR6ux7K-vMUgVrlDiVsbrZ--XPeS4zBWh4LYudSaDy3iUfnG5EjufV77UuX9984js097Rg7Sa_QZ1yK4n67qymPCS_UT9M8f8Fn5i3qwuVWKUsKL9GpxGXLL6ROTo2qh17JeGeVgzFkX6QHP8HufwVcbJSWC5G2zRjv8UMhlzf1xghW-CupE-sduqgCEeH-66GOiQCbcAFh-9xqb3ukId9-lXSVcDY48UuY088QqNhIADGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صید هرمز
🔹
نیروی دریایی سپاه یکی از مدرن‌ترین زیردریایی‌های هوشمند و بدون سرنشین ارتش تروریست آمریکا را در ورودی تنگه هرمز طی یک اقدام پیچیده اشراف اطلاعاتی و عملیاتی در سحرگاه امروز به دام انداختند. این زیر سطحی هوشمند از جدیدترین تکنولوژی در حوزه زیر سطحی در دنیا برخوردار بوده، که سال ۲۰۲۵ میلادی به ناوگان ارتش آمریکا تحویل شده است. این زیر سطحی اکنون به غنیمت گرفته شده است.
🔹
هشتصدوپنجاه‌وپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/688294" target="_blank">📅 21:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688293">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ca1bb43f.mp4?token=b1oEA409YcwzZ0uvxW3mgxtqtZIRaG2w1U4PVPYZxky_jNm4MP5ezAVI0Ppzor1mOmcUg_1BoQzxmILzMFJRKkpWtb0-wsDqOzy9xoz1WMYoY_xALf050J2Ec7GvyBzbp-5vSK5R6pBkfJgmGSlvFizJ6tjilOqAjIYb9D8AeZuFgY5RripsrREo3TWpN9zJHtMVSdSFTpowJnORhIbhiKYs4ZCSrm-DP1UKX0CQMQ6O83ty53sTTTsnPyQOPBgm4WR8SKqOobMysMwKGDc6ntuCswiGvcyNGY1j8QkupcSopAiqlG8aU-hQ7hT5JAj5LrJkU8FMFtbdXjSe_cXSpEF82GCd8AN-0FfLKrzyaCucGW7QJurj9BHiDl3tbd2XhvtD48Tp4-sWWt-UdQ2KrjQZg1whDQ2M8odiMyP_riRUBIKEb9diWLD7QxeRFrmTAPy-SK1asGphju2FvYiXC-nUfVCLQUXyGAUohjSfJ2iFzdevTvC9axtDP-tK_WCS3qtDfhNPyfdNSI3ALZ68-kbSHuDe_u_ASe7ZYOKF131gQ4eV9dhxKA_SuT2A5CaGKp-6Y1Hqmr_HisvLk35lq5KmJ1k_8SBXK6M3UqlK_DYfhUUFSAXWMZJRKGqZ1Oc1zCE_s8g9wMgaG9xWdPotL7DT363eQpsSLpj_8ta0phc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ca1bb43f.mp4?token=b1oEA409YcwzZ0uvxW3mgxtqtZIRaG2w1U4PVPYZxky_jNm4MP5ezAVI0Ppzor1mOmcUg_1BoQzxmILzMFJRKkpWtb0-wsDqOzy9xoz1WMYoY_xALf050J2Ec7GvyBzbp-5vSK5R6pBkfJgmGSlvFizJ6tjilOqAjIYb9D8AeZuFgY5RripsrREo3TWpN9zJHtMVSdSFTpowJnORhIbhiKYs4ZCSrm-DP1UKX0CQMQ6O83ty53sTTTsnPyQOPBgm4WR8SKqOobMysMwKGDc6ntuCswiGvcyNGY1j8QkupcSopAiqlG8aU-hQ7hT5JAj5LrJkU8FMFtbdXjSe_cXSpEF82GCd8AN-0FfLKrzyaCucGW7QJurj9BHiDl3tbd2XhvtD48Tp4-sWWt-UdQ2KrjQZg1whDQ2M8odiMyP_riRUBIKEb9diWLD7QxeRFrmTAPy-SK1asGphju2FvYiXC-nUfVCLQUXyGAUohjSfJ2iFzdevTvC9axtDP-tK_WCS3qtDfhNPyfdNSI3ALZ68-kbSHuDe_u_ASe7ZYOKF131gQ4eV9dhxKA_SuT2A5CaGKp-6Y1Hqmr_HisvLk35lq5KmJ1k_8SBXK6M3UqlK_DYfhUUFSAXWMZJRKGqZ1Oc1zCE_s8g9wMgaG9xWdPotL7DT363eQpsSLpj_8ta0phc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شروع فصل جدید داریک با توسعه و ارائه نوین محصولات
عبدالرضا عسگرخانی، مدیرعامل داریک در
#گفتگو
با خبرفوری:
🔹
هدف از ری‌برندینگ داریم، توسعه و ارائه انواع محصولات داریک و پروموت آن‌ها بود.
🔹
پس از ۱۸ سال فعالیت داریک در این اکوسیستم، اکنون وقت آن بود که محصولات این برند در بستر آنلاین نیز ارائه شود.
🔹
در داریک سبک جدیدی از توسعه محصولات را در پیش گرفتیم و از توکن‌‌هایی که بر پایه فلزات گران‌بها هستند استفاده کردیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/688293" target="_blank">📅 21:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688292">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kClSbp6HUUclqhWOSH18yiq0z7lvMAlSwsHayRFFATlZSIiWBizM37nKGvhU66vzjWGduYaQcCnd8_pkWzgqcyBKsTZ_q9TDKOHLSh6r9uTUDxaauikPETOOPE25pWgbkeDFUViQ0rYadSOg0fxCZkQnLr05Md6K5NUKUGaDMHckobqjgnX13XHqo0YAglbEe8KJwdm2f4ZooKEqF8LBloj8w2oienLvW8XMaDUu4foKiGC9zIZx-VGCmZz93sPGMPllJ-PYMzfbI293IzKcN17jvQucty5j_Fa1g1IDTrl06o4QIuS8X2eFE-9bdTW_LQtuqMR0-SzSBp4f4v3egQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیر سامانه هوشمند سوخت شرکت ملی پخش فرآورده‌های نفتی: کسانی که کارت سوخت ندارند با مراجعه به سامانه سوخت من، یک روزه کارت سوخت دریافت کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/688292" target="_blank">📅 21:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688291">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
۱۲ کشور خواستار محدودیت تجارت با شهرک‌های غیرقانونی اسرائیل شدند
🔹
فرانسه، بریتانیا، کانادا و ۹ کشور اروپایی دیگر در بیانیه‌ای مشترک از اعمال یا حمایت از محدودیت‌های تجاری علیه کالاهای شهرک‌های اسرائیلی در کرانه باختری خبر دادند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/688291" target="_blank">📅 21:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688290">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
پرس تیوی: نیروهای مسلح یمن کنترل منطقه الیَتَمه را دوباره به دست گرفته‌اند و ده‌ها تن از نیروهای سعودی به اسارت درآمده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/688290" target="_blank">📅 21:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688289">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFtSPZio7hiifVqgPzUjZwQ66dcPTjxCIYRDABfvm86PoO_31sFgRE6GyhJYlkHz0UfJJMWzKXeSL4Ymjn6mrs2ebrGGna5Nq6oTkphWPwlDRugz7BwO-QRBffMt5nHXpHsdIxi3TJnf9ufX04-rMPkr9k7sqO7AgTyystJYKdmin6HtDvAYfDLPAW5Hfo3ct89Nmq6CC-KjyYEm_zDgAdpG6ukPpmTgyDPfvaByRbRqq32svi-7_839WLmo6lFNeDamKrSKmZv-XzPWtltFjzQpgIrYST7B6PKFq184Xu3ubDKj1qZuK9OD7lDJpHyV9r2bUOp7HbY4keDMfv8jyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شکار یک فروند زیرسطحی هوشمند دشمن آمریکایی در تنگه هرمز   نیروی دریایی سپاه :
🔹
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/688289" target="_blank">📅 21:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688283">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TYvYNls3NgRSuvPwoBtu2RfStdfiuol2gJZ47B4N9X2gSkBeAfX3NYWuwYuIQjk2bJd9-dWAvonqnvsaEAMSxsHPZgEa9F3g9ED5So1yLpsvR8gwEupXGrfCyya68jB8lIHHQVMViGg4DjywtzvBOp__bEYIQFjq-BK0379O5jJvaN1CZeBrQc2NfkDdOGh3Lp1Yhzhk9JsSX1jXjzXd2w9o3y51ZThpaCv5ogTWrDDWNJASKjdXdabkDC4VJ-GfoYRvlcaJ818ScBAQwYqevNeJ-H7oZjKwYwb2Yb3BLufXS1iHQSYNW1GABDROOZhRV-MUjrWRpxKCsYf-CfsBXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XdR0YybzPbcOTdlW-69AYc13h3inunR8bGGROuSmAMaYwzmrt4jqkDSxlkHh26fsX2mahXR8Qx2Ryz21T1fmzXJoug9NDhagMnr30laHDjHmyWGqB5715paRu82eS-tD9p85wIR7qMrxUlhU5cOwXmwkPRNbL4UeGDvnxNMz6OieKVZ3Tao8GojqBsWl43EDsJmSCngAU0dSWzN0YL9GFmCidMivd6kJACZu9MTIGpSBREHRlBGykHy8ZeAEj_VeRFaBg86dhqjfRimzEEp9zLpkjx0zLTUC64evtHNremQnUA16qyyUGJHhph_G3iwzewC1CL2GgX_4vfNv4vAJyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JkQ-ks8sjst4P3uIbwcoltGQpJ83DSGea0Bezpe_2mgLkkPut7YVa_XOjh70rS65uiYc_hnj0vZ0dAoa-4sB-YkUqI1PjyNpVdC9c15pYwbdxW2CQGtIe-XK-KPdJEBeYbBZfOrj26z77u71XarYdgiQRnoJw8yuvtXcGsEGG-eX99rhYGrLDFp-3NuBZ_pmm4ibdapDb4ITvv2vsuS_eQq1wgtI4cywynd9cYcU7eblf5pzhE_JGNoti2dDkmiff2PSMiMXTImftlmI0Xgih9UfFcrqI2crFmG-VZPl8ZKqcerwtBT2Na_fynx-cEXaB2vOcqESRSs-GxjCBuoUMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QnFtKMFPB1M0jjgDan3sXfgvfM6-1OG82lnjBZH-4k-iAiYWVK6vrsuziTkNHfrEG1cBQrJiaBNLtM-bCkD7wrK6-60nh6Rwxr-4xKEpQ6xOAzwvRrsp7QBXclrtf0y1BV4iaGpkxYfiX8ZBzcFouAJsaRc21XpCTNBdHQorVBxpHi2rm-GC9K5HOBQfgFQZfMkWSsIWDXEK6aydcCa_gbp_FmMpZHiXCh4VVZvXcyv644yMSQBwBI1hInPwf3JkNdt5TmaGYxVTX0Y_e1tTO-j3gA3oM7hQ1K5JBJi8SYK313APe9LHfXHMKiIqqKDDk2A_ctC-VlEYytnQBMhjQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D4Huso5WC-pLierXbL31JGR5LIC2KXGwjNNFOiO8uY5NlJQkt0VwYJEG-hHtf021MsCERmerUc5xHXA7f5i65Bf9dIZaJa_f3e3EtFjLieSD8FWinIyuhdvMWY_GkQK_yBncxxAEG2JHZXlsNgtNCmp9CiX90YzMy-fUduPLVtUJ3oswk-335fT4grM90PC2GpPXVpzX5ScwZrrKxhFFIz2Rg29r7qvOCyi7DVoPx6brC2_3-_aBd9iAeH6WPuq4Cs8bK6fIB1d3SPBqSRMEL5i2YIQtdGhPik64ZAWNj2I7awQ7KXwxYE1hK1S79v7tSmZRC-gy_VjVDGssdv42QQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اولین فیلم از زیرسطحیِ هوشمند آمریکا که در تنگه هرمز شکار شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/688283" target="_blank">📅 21:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688282">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afd80bc80c.mp4?token=lEAXFbeokcCVGEv8suDJGozyS1EF4X2gfGfOmq4EgAQQTsVhqicvAMwoaR9X6MMV2NmU9R9i9CrCneryJVny82Xu-jTmnCBEPt_MGgRaShBeudM_5jX5lBzpkw59Wdslgw1SYRgx4o2B8el4OEXQqcmJnSjHxroVmiMEXA29UCJkDYRgKEllTJJtTrDMN4QZlvSvurBEV81pxgWRudXbNnyhm6bnbd_Ixxrk44wI6O1rBYTtzhOIk1wvxI3jZmKI41SC3T50oyGvkoU4urJUo7Y5tdZaU7B8RUWmXI3V5f0pB6VZo2eyQs6wUnGByzfolXtiIGVbysNj2XVJQ2Znmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afd80bc80c.mp4?token=lEAXFbeokcCVGEv8suDJGozyS1EF4X2gfGfOmq4EgAQQTsVhqicvAMwoaR9X6MMV2NmU9R9i9CrCneryJVny82Xu-jTmnCBEPt_MGgRaShBeudM_5jX5lBzpkw59Wdslgw1SYRgx4o2B8el4OEXQqcmJnSjHxroVmiMEXA29UCJkDYRgKEllTJJtTrDMN4QZlvSvurBEV81pxgWRudXbNnyhm6bnbd_Ixxrk44wI6O1rBYTtzhOIk1wvxI3jZmKI41SC3T50oyGvkoU4urJUo7Y5tdZaU7B8RUWmXI3V5f0pB6VZo2eyQs6wUnGByzfolXtiIGVbysNj2XVJQ2Znmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون اطلاع رسانی دفتر‌ ریاست جمهوری: مقدمه تجاوز اسفند ۱۴۰۴، اغتشاشاتی بود که در دی‌ماه در کشور شکل گرفت / به تعبیر امام شهید، آنچه رخ داد یک کودتا بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/688282" target="_blank">📅 21:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688280">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5d5430a50.mp4?token=FGoZBlAZ1DOUEMSxK2OMCKYNrMZORCYx73knoZB977m3aPfK8ZCvzdiGOg5YB0y-xxoJ_jlFRS-qux7jqvIaRJtAqWX_DbvljklxK_8ZYNy0JSdGtiap5ZTA4nq_KfSoMQQXYWcLq-J07QeUTVNWPS_1D41rZeG4YIIQYwG6MV7IbgZO05cyGwsE6dxegXmao5tHIRCVtjDGBOENAUwy31BNnH6oMID0dgc6sMW56B-GZni6xpCG9RSeEz30DXIZQz3yMI6joADUpRWO-sFRxucID2Zz3w7lPJHXyV0iIPGEyIAuk64C8RCdW5GHv3yn0L8MDkPy_rZV96jRnAPryA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5d5430a50.mp4?token=FGoZBlAZ1DOUEMSxK2OMCKYNrMZORCYx73knoZB977m3aPfK8ZCvzdiGOg5YB0y-xxoJ_jlFRS-qux7jqvIaRJtAqWX_DbvljklxK_8ZYNy0JSdGtiap5ZTA4nq_KfSoMQQXYWcLq-J07QeUTVNWPS_1D41rZeG4YIIQYwG6MV7IbgZO05cyGwsE6dxegXmao5tHIRCVtjDGBOENAUwy31BNnH6oMID0dgc6sMW56B-GZni6xpCG9RSeEz30DXIZQz3yMI6joADUpRWO-sFRxucID2Zz3w7lPJHXyV0iIPGEyIAuk64C8RCdW5GHv3yn0L8MDkPy_rZV96jRnAPryA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا حالا دیده بودین رعد و برق از بالای ابرها چه شکلی دیده میشه
😳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/688280" target="_blank">📅 21:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688277">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
از انکار واقعیت‌های اقتصادی تا دلاریزه‌شدن انتظارات مردم؛ چرا مردم به پول ملی اعتماد نمی‌کنند؟
🔹
سال‌هاست سیاست‌گذاران وعدهٔ کاهش نرخ ارز می‌دهند و مردم را به سرمایه‌گذاری در سپرده‌های بانکی، بورس و صندوق‌های سرمایه‌گذاری دعوت می‌کنند؛ اما در تمام این سال‌ها، کسری بودجه و چاپ پول بدون پشتوانه، ارزش ریال را کاهش داده و مردم را بیش از پیش به سمت دلار سوق داده است.
🔹
در این ویدئو بررسی می‌کنیم که چگونه انکار واقعیت‌های اقتصادی به دلاریزه‌شدن انتظارات جامعه انجامیده و چرا دلار به معیار اصلی قیمت‌گذاری در کشور تبدیل شده است؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/688277" target="_blank">📅 21:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688276">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/142daa5f1e.mp4?token=NC1pwAJr0XE8LGsM4niaCnEj5PV37AUAQ2BlzIkJc4MtfEmZwA5Ypd5nIiD7lHrU-aHKtVNHwbrO3OehQ4Ny4NcWyNjoFK2IhXKIOHlz5Idbs7kIqGDC3DxP8CUgDVsIUbz63B98jbndr3Duf4C74mkgTu0k3FTzNbRaaWxP2m-8jfVO-vYAkDRS3Cuf2BDe9auS0PW4yE0c1CvYq5t2dC0RuWh35J54u3B9xjDzQYDkgrAlxPLTMQpeBKwa-cJW4FmU0f72ToE2eetLTFEOqn080UT2S8pTam63LSJzNy0wKqQ37sW1GtfeT93kwBxhTjQvAEpaPFNomARGHGtugQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/142daa5f1e.mp4?token=NC1pwAJr0XE8LGsM4niaCnEj5PV37AUAQ2BlzIkJc4MtfEmZwA5Ypd5nIiD7lHrU-aHKtVNHwbrO3OehQ4Ny4NcWyNjoFK2IhXKIOHlz5Idbs7kIqGDC3DxP8CUgDVsIUbz63B98jbndr3Duf4C74mkgTu0k3FTzNbRaaWxP2m-8jfVO-vYAkDRS3Cuf2BDe9auS0PW4yE0c1CvYq5t2dC0RuWh35J54u3B9xjDzQYDkgrAlxPLTMQpeBKwa-cJW4FmU0f72ToE2eetLTFEOqn080UT2S8pTam63LSJzNy0wKqQ37sW1GtfeT93kwBxhTjQvAEpaPFNomARGHGtugQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گرانی بنزین در آمریکا صدای کامالا هریس را هم درآورد
🔹
کامالا هریس در پمپ بنزین: سلام به همه، من اینجا در شارلوت هستم. از زمان آغاز جنگی که ترامپ انتخاب کرده، هر بار که باک خودرویتان را پر می‌کنید، ۱۵ دلار بیشتر هزینه می‌پردازید
🔹
قیمت گازوئیل هم از زمان آغاز جنگ ۸۰ درصد افزایش یافته و بدون شک این افزایش قیمت روی هزینه کالاهایی که با کامیون‌های سنگین جابه‌جا می‌شوند نیز تأثیر خواهد گذاشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/688276" target="_blank">📅 21:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688275">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tz9MpRuJJffBlIX8DDZlaKbMNLdrgPp_Uwvtd8mQU_1WexMqH8tnxuI3n1r_pEgQ7C1iYeKl1ZFsjjwlpUmWxUGiQ-xE7ZNDqmonKBSGp8E6o8A6Iu2CVDvxmHt1r7BPV5FBqhVEeDJ-_QNgQGrvZKEyS_8nZ64eLPAz8G12xE3VHqz4agmdORva5tXq9sdzfEzbpmHlnZGFZ562Ch_JPig20bZ64rxViQ8hIfGORDJE3ND_9hK-R0ZPlfRglFTwphOvnd0N3AInaEqo7YOA-nAuvV_YknbAGdyljOrAjSdF9YVExyLhubvLzDdzoX9Criv0wSsP_5p83vp2txamEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
سرنوشت طلا، دلار و باقی بازارها
در ۶ ماه آینده؟
🔴
امشب اکواحسان (بزرگ‌ترین رسانه اقتصادی ایران)
🔴
برای ۴ میلیون مخاطبش لایو داره و پرده از ۲ تاریخ مهم سیاسی-اقتصادی تا پایان ۱۴۰۵ برمی‌داره
✅
این لایو حیاتی؛ امشب؛ رایگان توی اپ اکوتراست برگزار می‌شه
⏰
زمان دقیق لایو فقط توی «اپ اکوتراست» نوشته شده. همین الان نصبش کن تا جانمونی:
https://ecotrust.ir/app/live-stream?utm_source=ArshiaYar&utm_medium=TelKhabar&utm_campaign=live-ehsan-0606&utm_term=socialproof</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/688275" target="_blank">📅 21:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688274">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrCro0SkVM3D2BDT-v15kfZqT-vl0MTOUHSag4_YQYXSDqxptI9s3FC5kUXLkpU1zpDYnMNSHr8K0_WrGnMhTAJMT15EOq421Ok2mUJ1MTHiSMDjYXZSkupPnsOxCsiJ9KpiFObc4z7HnGBu_uuJVBrhESwK79QQZzepHpPcuPae2AsECRswYvR4iQm1dMKZK3J2TT-eJpiSARVeqqPcjSlyBuqsww5OgbyEIX_PqnShULu1N45EDwb4ug_cxpoVAFwhUbAmH8-l7eO5MkHb34IM88mUPv5LUnjwRkqVG2phJGkvmHByhLJ2aHvdPt0A-bw_rRlgNPuvnKUlT0xUxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با هفته دولت و در آیین «یک ایران متصل»؛
بیش از ۵ هزار پروژه شرکت مخابرات ایران با حضور رئیس‌جمهور افتتاح شد
https://www.tci.ir/portal/home/?NEWS/235300/235321/575208/
@tci_iran
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/688274" target="_blank">📅 21:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688273">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
وزیر نیرو: رفع خاموشی‌ها در جنوب کشور در اولویت است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/688273" target="_blank">📅 21:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688272">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
دستاورد تازه شرکت ارکان سازه در سریع‌سازی پروژه‌های ملی
🔹
بار دیگر بخش خصوصی در اجرای پروژه‌ای
ملی و ماندگار
، رکوردی تازه و متفاوت در سرعت ساخت، همراه با کیفیت و نوآوری به ثبت رساند. مجموعه‌ای
هوشمند با ۳۵ هزار مترمربع زیربنا
، تنها در مدت
۲۲۰ روز
، به سفارش فراجا و با اتکا به توان مهندسی و اجرایی شرکت ارکان سازه احداث و با حضور رئیس‌جمهور به بهره‌برداری رسید.
🔹
مجتمع شبانه‌روزی آموزشی و فرهنگی سپهبد شهید محمد باقری با ظرفیت
۱۲۰۰ دانش‌آموز
، مجموعه‌ای جامع از کلاس‌های هوشمند و آزمایشگاه‌های عمومی و تخصصی شامل
هوش مصنوعی، الکترونیک و مخابرات، پهپاد و رباتیک
تا مجموعه‌های فرهنگی، ورزشی، اقامتی و رفاهی را در خود جای داده و با برخورداری از فناوری‌های نوین و استانداردهای روز دنیا تجهیز شده است.
🔹
این پروژه، نمونه‌ای از
ظرفیت بخش خصوصی برای اجرای سریع، یکپارچه و باکیفیت پروژه‌های بزرگ ملی
است؛ ظرفیتی که می‌تواند در مسیر توسعه زیرساخت‌های کشور، نقش مؤثری ایفا کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/688272" target="_blank">📅 20:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688271">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
دلیل رسمی کم شدن سرعت اینترنت ایران در ساعات اخیر اعلام شد
معاون وزیر ارتباطات:
🔹
کندی اینترنت ناشی از قطعی فیبرنوری در ارمنستان است و تیم‌های فنی در حال پیگیری و رفع این مشکل هستند./ جماران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/688271" target="_blank">📅 20:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688270">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpS7ieWQtRVNd9FCtpcYYuvLh4P0uVMP01qBMazjRYuVO51oAirCfiRQS48OVrxd_zRGUFA9Z5c9jhxAPp_8L4WFtyHyd1F6tQ4wusUpJY5sSW1Y_MJXobsa67BzJYi-dcUI7GHzkVnK9KqPy_IqrJZ8zsqHoqMXr8TrCp9cvdMU7ErK-mSlhQH9ZFm9kYxVo2NvI51IGWOSv20_OGWUtRrJnMWDp6rtKTu9gMSCjhJ4vYNuKCFDo3BizaOlCvr7ZK2fFlJqNLQgm9UuTKCmYdkx_SEcM1aZTxpY51cs-RdvY2aFkoparNS6hj0swxCqeFgjcTzUVdhz0eXd1EhmvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ذخایر راهبردی نفت آمریکا باز هم کم شد
🔹
درحالی‌که قیمت نفت امروز به مرز ۱۰۰ دلار  رسید، آمار جدید ذخایر راهبردی نفت آمریکا که لحظاتی پیش منتشر شد نشان می‌دهد که این ذخایر ۱.۲ میلیون بشکه دیگر کاهش یافته و به ۲۸۵ میلیون بشکه رسیده.
🔹
میزان این ذخایر از عدد بحرانی ۳۰۰ میلیون بشکه هم عبور کرده و درحال نزدیک‌شدن به کف عملیاتی ۲۷۰ میلیون بشکه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/688270" target="_blank">📅 20:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688269">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d03ce3a78e.mp4?token=H894K20lnruGjpFYiEdPaBT92uayfrQMfLpzYG9ieBJjYb6LJ4nMTM514jzaLeuJFWmnmlRinCBDlx8iw_HAw5j5QaPgfKflxSUs5Vq-IGwDLn1EDMqzWOIGepKftLCdZhxDEIW34Tw5nZa8TOCj1XV9a3y18u4KqjitVFXQ_KrUx-FqS2qdOPr1WOEEj3dKsUNow_aVS5IzU2gGGPgVN0DRSIXAolvL40Gpd0JejJLevJgZfJohrh2SjR8tM6tVkb29E2Wwe2lof3dcZ8BJF86wJJC3C3FwonhZcTfaqtVGkciiHOW-xWjdGqD22E0tn6LX12qXR7je19fsWpBjyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d03ce3a78e.mp4?token=H894K20lnruGjpFYiEdPaBT92uayfrQMfLpzYG9ieBJjYb6LJ4nMTM514jzaLeuJFWmnmlRinCBDlx8iw_HAw5j5QaPgfKflxSUs5Vq-IGwDLn1EDMqzWOIGepKftLCdZhxDEIW34Tw5nZa8TOCj1XV9a3y18u4KqjitVFXQ_KrUx-FqS2qdOPr1WOEEj3dKsUNow_aVS5IzU2gGGPgVN0DRSIXAolvL40Gpd0JejJLevJgZfJohrh2SjR8tM6tVkb29E2Wwe2lof3dcZ8BJF86wJJC3C3FwonhZcTfaqtVGkciiHOW-xWjdGqD22E0tn6LX12qXR7je19fsWpBjyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از لحظه رهگیری و انهدام پهپاد متخاصم MQ1 دشمن آمریکایی توسط پدافند پیشرفته نیروی دریایی و نیروی هوافضای سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور بر فراز آسمان تنگه هرمز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/688269" target="_blank">📅 20:48 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

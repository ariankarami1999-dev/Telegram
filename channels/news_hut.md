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
<img src="https://cdn4.telesco.pe/file/H0gSLo44wN019_qRbcYjQXGb3S61J7h90V2Gve4JngBdf785ZasJnWzh4aIhGrUOT8pN-OakIurkl4dC18katcpjSix4_3GMvqmquuZ8WkM1C32ckKjfr-PyYEdKSM5piFDc_9lQFSwuBu6kv9TXaqy2ZEiCMOFAMzByknotIZ_gEGwIYQE_GjYA2GcJ2HiHz_XqwdNQhK77a4_9KOXNSOaqYhUNJWETGWreX0T6MrHkXjd-P9iptwe2hQa_bDJzsD-kD6fISQQfyQszgmWi_jCWx6L9AD1sYLRA8ml78tv-HhmrPMs8ZBlTd7gP_sI7QyIkC-R_t7cqx8rjLvG4nQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 12:43:35</div>
<hr>

<div class="tg-post" id="msg-72938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beJQSl6F0femEvrDlXtJaohoRVWnb6URBeMn999A02yRbdEB8NfPg9rXaFZcCqVbXidTIsKAjT8Zfx-BW-dC1nBDmWnLErpJQBHZmn4rhJpAB-nWo8jd7ruzIT_UrfhyXi5NhSXzzupT3XLVzSL4SxxK81z7PDmk14VxjY14JZQUGBv4gn7EbQdzJWuPaMlI1gWlpte4wrgyysNBoVQYlP4GTaR4CT7XKsb11Q96W5oI__7-AeJRXNvsl1fWhWo5xFZZDpNAF4fUPwYROebzKABYNjZUSqFy-ufwl9f61rhIzXvxefjbbAPgcsoDxinA6w2zLXfSFL-21Ek_MZC9WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت رونالدو برای مسی:
لئو، سال‌ها برای کشورت جنگیدی و یه تاریخ موندگار ساختی. بابت همه چیزایی که با آرژانتین به دست آوردی، دمت گرم و کلی احترام برات قائلم. بغلت می‌کنم
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/news_hut/72938" target="_blank">📅 12:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72936">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5lMsJOVyY_Z5BhsJqGbODVcKj-WVVb2Fk5Qecf4SmbyPGzaiDbw_e7EQWSBFfkxPD67Ys6IDcPsZgUUkmK87LS7IHbiqRewH17T2WcrAzGfDc8-WT-yY2UZKVA04jycQLQiNvf-lGLLOqSjIjdnD6pLfQL9Pqwelv6SFdF8PQP9w2q6Q36nbu3QN5WSV6tzQCiH5b949aqyAY-Jwz3yrn8oirHg8qUNr_5UcDAhWl5xreBhJX5b-n5fjQKc9KDgzCAkoGXZgyz2XFVLLY6ZiBJztsUNzbr_S4VZpiwTjJ8ffoH7CuVzf9MMu_o94NL4o62DoCWjtJy2vEg5dH7Kig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca5f1c5b88.mp4?token=Sf91gVAtfvHquIXzdaVzAJvn6-ngrkEzM8TjEytJM02IWtGT__JWBA09BKAHYLEqk89w1i96j_0huSB1Esc3BV5PvNsel_WrGvttkomeu04q_z7UCZmS6dGpCrlMmBCGYeWozf75RR4TmdT_TQkfjoJQkIcbUCTWSYTewYB4dVsgtLE4qNMTEVveJfwCW_qYbTD-pckrklKNuhhB7W9Xw-Ibc9QjBqZP6H7JjoJzNwrwbu9lvCEZLSlgyIh53Mrdr2PbNTEa93XZQEh4rRgAH1CqY51OQMw8Oc0wtlsTL7g1PCl4BYDdlf4SlJuTbIZtI3JzHRPut5GlEPmuCvymlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca5f1c5b88.mp4?token=Sf91gVAtfvHquIXzdaVzAJvn6-ngrkEzM8TjEytJM02IWtGT__JWBA09BKAHYLEqk89w1i96j_0huSB1Esc3BV5PvNsel_WrGvttkomeu04q_z7UCZmS6dGpCrlMmBCGYeWozf75RR4TmdT_TQkfjoJQkIcbUCTWSYTewYB4dVsgtLE4qNMTEVveJfwCW_qYbTD-pckrklKNuhhB7W9Xw-Ibc9QjBqZP6H7JjoJzNwrwbu9lvCEZLSlgyIh53Mrdr2PbNTEa93XZQEh4rRgAH1CqY51OQMw8Oc0wtlsTL7g1PCl4BYDdlf4SlJuTbIZtI3JzHRPut5GlEPmuCvymlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داریوش بزرگ؛ نامی که پس از بیش از ۲۵ قرن هنوز در تاریخ ایران می‌درخشد.
پادشاهی که ایران را به یکی از قدرتمندترین و سازمان‌یافته‌ترین امپراتوری‌های جهان تبدیل کرد؛ از ساخت تخت‌جمشید و گسترش راه‌ها تا سامان‌دهی نظام اداری و اقتصادی کشور.
داریوش تنها یک پادشاه نبود؛ بخشی از تاریخ و شکوه ایران بود؛ نامی که قرن‌ها گذشت، اما از یاد تاریخ پاک نشد.
امروز، به احترام مردی که نامش با شکوه ایران گره خورده است؛
یاد داریوش بزرگ گرامی باد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/news_hut/72936" target="_blank">📅 11:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72933">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZNqT3zCnAHZCZlVOhWUpvNwKVcJde4yicy8Sq9teemCSAtBGFwSdvTDQgm9JI0el0yH-SXGsXBMBWq1FZiKRSXus_L6Csg2gfgIyJta0l7hL5R4XmVFhBT90JUeANjDRmqWSOvxfVoDGxbmXr_s0dkDUht3qs_B44b88F107zzg_xgyDJ0Inb44J7rlp7HZHScnkzbo5jgya5v8OBkgN7hxeA7jFo3DIVjQSte8_oNRw1rgYjXyinmeNoUCp_nKYjIg1uo4d5vMA2mkMZrThAJf3WiYsSdWBT18BkH98IDNemLA5o8fdRuD0y2ya_zZmJUOIT0aNKl_gVNWUMmOHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ۲۴ ساعت گذشته، ۱۱۰ فروند هواپیمای نظامی در منطقه شناسایی شدند که شامل موارد زیر بود:
۱۶ فروند هواپیمای ترابری ورودی از خارج از منطقه (متشکل از ۱۱ فروند آمریکایی
۲ فروند بریتانیایی
یک فروند ایتالیایی
یک فروند آلمانی
یک فروند با مبدأ نامشخص
۱۰ فروند هواپیمای ترابری نظامی منطقه‌ای
۳۳ فروند تانکر سوخت‌رسان هوایی
۲۱ فروند هواپیمای شناسایی
۲۶ فروند هواپیمای ترابری نظامی فعال در داخل منطقه
۴ فروند بالگرد نظامی.
@News_Hut</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/news_hut/72933" target="_blank">📅 11:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72932">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxpJqsdZXZFO006EBnF1onCpH6tiLAR4B4IGxhdsAmQzQXv4zaoCIya69wcuCI7YjxK-_MxoLq_57a_K9dk4RvtAgCu4cZGF8UEJ-hHQl6va0IjBhfU9jSchwHGfuywiDF7IY5LPN8WGfPRNzIc4Dz4mAkTseKM597BR333fEkDfl-DmtLyJlGvkzq7sIZQdChgUBiN56kVUIvAJukIoAUa2taaGbs1geL9EE5jWJ3gskZBuvfvWsz1jFBe0i4Y5Bj0j_AhcgPabP4nhBZ0AmOV_cE6_l3sQOciCFKoeKJ-a9utk1m7rbQ31-TaU_8UO_ZQeyd797LbcIBHa63d45A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووری
؛
پنتاگون به ارتش آمریکا گفته خودش رو برای حملات احتمالی دوباره به ایران آماده کنه:
طبق این گزارش، هنوز دستور نهایی حمله صادر نشده و ترامپ همچنان درباره زمان و اصل حمله تصمیم‌گیری می‌کنه.
اگه حمله انجام بشه، احتمالاً اهدافی مثل تأسیسات هسته‌ای، زیرساخت‌های انرژی و دیگر اهداف راهبردی ایران مورد حمله قرار می‌گیرن.
منابع آمریکایی و اسرائیلی می‌گن احتمال انجام عملیات قبل از انتخابات آمریکا و اسرائیل مطرحه.
همزمان، تیم امنیت ملی ترامپ درباره جنگ جلسه داشته و ترامپ هم طی چند روز اخیر دو بار با نتانیاهو تلفنی صحبت کرده.
@News_Hut
| Axios</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/news_hut/72932" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72931">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72931" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/news_hut/72931" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72930">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAltVedgwGwjxTXKpJkDoF2TdRMnP0_SWxxxRce2Ae3iU-8hvE3GcCneAQZHTPva7aVfhOHLa5w-BMGT3uiY01A82kEGu4xZJIgu6OdgDhfpEytgfZpm75jichP94umCsUr_LHd1t7R0DJ-sgCoPCZf2_-536pqKwgApwSjKGyIOUiBKXpZ7Tm7haMObv-DZPUxsbDi5YTWWoAKeA8cnOC_ddf5opoj_eIGwy9T3dmUEv6EEo5BStF5HVmqFb9j-rXkUq_GhnXaeaeWlbPGaI2i8b8iE5pwwjAKuSNEXBnCEqlkTxDlwmnN6fNcmOk5NO5uwq7lvUoqY_Ix5Elt6jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تراکتور
🆚
استقلال
⚽️
رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم در ۵ رویارویی اخیر:
⚽️
تراکتور: ۳ برد، ۱ تساوی، ۱ شکست و ۶ گل زده
⚽️
استقلال: ۱ برد، ۳ تساوی، ۱ شکست و ۳ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/news_hut/72930" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72929">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/96ef1b8d29.mp4?token=kQo9MWsh_eq_JeHufTnWCej2RiTFsBccjhG060m1SBAHbv5-Hds2wAqEBs6Cl-tbzzHxyKiEp4UxOMntdCCFMEq3MQf_8ZSI5nnp1zviAVJUzi6oh_wc8wyLqoCeKkYchOWOy_Odx6bg6JxMe2hUZzc2xnO-EL0hKiJpVDfYcvHtspFPqFGpEmPvKB4rW5BAsNjAFD2Ku-Hby_dRC7wHAGZjXNJFOhN6PEdtmoL3eaoaszdKYbQdBsBDtkTrRRNMijjq1lalsliyoWVSFj9sbtF222LdNQwXcvVsVgY2OaiPYZ-gWxZcNL2SziqMG1rDeX80Vw9-8PnkVHfIc_GesQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/96ef1b8d29.mp4?token=kQo9MWsh_eq_JeHufTnWCej2RiTFsBccjhG060m1SBAHbv5-Hds2wAqEBs6Cl-tbzzHxyKiEp4UxOMntdCCFMEq3MQf_8ZSI5nnp1zviAVJUzi6oh_wc8wyLqoCeKkYchOWOy_Odx6bg6JxMe2hUZzc2xnO-EL0hKiJpVDfYcvHtspFPqFGpEmPvKB4rW5BAsNjAFD2Ku-Hby_dRC7wHAGZjXNJFOhN6PEdtmoL3eaoaszdKYbQdBsBDtkTrRRNMijjq1lalsliyoWVSFj9sbtF222LdNQwXcvVsVgY2OaiPYZ-gWxZcNL2SziqMG1rDeX80Vw9-8PnkVHfIc_GesQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به یه هموطن گفتن که این خونه جن داره، اونم خیلی پرقدرت و باشکوه وارد شد،
اما خروج جالبی نداشت:
@News_Hut</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/news_hut/72929" target="_blank">📅 10:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72928">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e69732ec1.mp4?token=UKQ7zUyXhvhyTTnogLgilnxA0mAQBliliZc2LX97PihurARaSKiw7pT4KavTscOsBTacHdOSxxi_KAxIG_6CrZma7F6bTfbC4YmHuRUx3A1W1n4NRJZuatbP7l7_uMMhf2lSSNH5JnvlJwLdXIcSLZO2E85qhm2L04-1Ogm_iVc2FQa861GfgwdLqqVyXy68yuag4-PhPVgJIJ7y0LEoEDPwy8B5Iq_cm9JwTCNy70F7HaXIrXFdgfzzoL96cVsT5ny30s1bHD8JKa2yWaGf6LtsIsu8zbiYRD7dEzn8KjW9NiHGrbGaPxTrdSokUijjtKuHtnVMe9htiFs1ryNERA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e69732ec1.mp4?token=UKQ7zUyXhvhyTTnogLgilnxA0mAQBliliZc2LX97PihurARaSKiw7pT4KavTscOsBTacHdOSxxi_KAxIG_6CrZma7F6bTfbC4YmHuRUx3A1W1n4NRJZuatbP7l7_uMMhf2lSSNH5JnvlJwLdXIcSLZO2E85qhm2L04-1Ogm_iVc2FQa861GfgwdLqqVyXy68yuag4-PhPVgJIJ7y0LEoEDPwy8B5Iq_cm9JwTCNy70F7HaXIrXFdgfzzoL96cVsT5ny30s1bHD8JKa2yWaGf6LtsIsu8zbiYRD7dEzn8KjW9NiHGrbGaPxTrdSokUijjtKuHtnVMe9htiFs1ryNERA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«استیو ویتکاف داره روی توافق با ایران کار می‌کنه و خیلی هم خوب پیش می‌ره.
فکر می‌کنم این توافق واقعاً چیزی نیست که بخوام انجامش بدم، اما ایرانی‌ها حاضرن برای اینکه این وضعیت متوقف بشه،
هر چیزی که ازشون بخوایم پیشنهاد بدن.
»
@News_Hut</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/news_hut/72928" target="_blank">📅 10:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72927">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ درباره ایران:
«همون‌طور که قول داده بودم، دارم مطمئن می‌شم که ایران هیچ‌وقت به سلاح هسته‌ای دست پیدا نکنه. خودشون هم اینو می‌دونن.
به‌زودی از اونجا خارج می‌شیم و می‌بینید که قیمت نفت مثل سنگ سقوط می‌کنه و قیمت همه‌چیز هم پایین میاد.
این عملیات بزرگی بود که رئیس‌جمهورهای قبلی باید سال‌ها پیش انجامش می‌دادن. باید انجام می‌شد، ولی هیچ‌کس حاضر نبود زیر بارش بره. ما چاره‌ای نداشتیم، چون نمی‌تونیم اجازه بدیم ایران به سلاح هسته‌ای دست پیدا کنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/news_hut/72927" target="_blank">📅 10:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72925">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f2348ec3a.mp4?token=WmbdRiXORsZpLnaHMhJthHDB_zkD2lAl_sL6XP-3YQQbFytGk-6AYwHUWB2Q3cRgtZpCV_HPixJsuwbsv7cq39-HTklZIfQCOydSduvzGEObJ21caBldXJZfuHC_TB7FaK3z3ag_iM1AIy_qZ684lOrwCQ2b8PZ55SS3lmSPLGls0wWlq_vuo98hsUzcB8H989pFh7cYHRiytwqrfJnEfiDcTopZogipwgnzZ5__pzg8Mqy2W220o5mwwFp0p9Lu7GzpiajRI2ZdjQMJDGlmTJowPlps8c352odU0vJ0Y2vr1IX3ughk9zTVW5XggFfJFhck_4Tp41O_3rj0h8OdEDXhYKShJaZzgV_AhPJxBrfFHGFqlDfJCLRvBFxCnOFaWfutz8_lBa-gMDWLkiMelDjxc0vsfOWc_NgwMxNnBAJYCMbsfzvx0l5GRY4FXorlxJ-4zFaGS0PxVHy7XMoVbo_B7mfNq9mV1wzo7sGzKTh5mksVNpAzogy4pysomef73XRb4v4LTVqPnNesudVyCR_FBao6H3DIWRpohh31dUToTZVX_G74SK_l4oS9dAsu2PcPs_qLcC9h7ichyEChSeSRIkqOSBEChBTBdFlrTF9nrY9kefBTZUHv0wU0RcGvLRUAbT1n92tNTTlj7ZdhURFgtlBi4yYMsT_Obh06EXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f2348ec3a.mp4?token=WmbdRiXORsZpLnaHMhJthHDB_zkD2lAl_sL6XP-3YQQbFytGk-6AYwHUWB2Q3cRgtZpCV_HPixJsuwbsv7cq39-HTklZIfQCOydSduvzGEObJ21caBldXJZfuHC_TB7FaK3z3ag_iM1AIy_qZ684lOrwCQ2b8PZ55SS3lmSPLGls0wWlq_vuo98hsUzcB8H989pFh7cYHRiytwqrfJnEfiDcTopZogipwgnzZ5__pzg8Mqy2W220o5mwwFp0p9Lu7GzpiajRI2ZdjQMJDGlmTJowPlps8c352odU0vJ0Y2vr1IX3ughk9zTVW5XggFfJFhck_4Tp41O_3rj0h8OdEDXhYKShJaZzgV_AhPJxBrfFHGFqlDfJCLRvBFxCnOFaWfutz8_lBa-gMDWLkiMelDjxc0vsfOWc_NgwMxNnBAJYCMbsfzvx0l5GRY4FXorlxJ-4zFaGS0PxVHy7XMoVbo_B7mfNq9mV1wzo7sGzKTh5mksVNpAzogy4pysomef73XRb4v4LTVqPnNesudVyCR_FBao6H3DIWRpohh31dUToTZVX_G74SK_l4oS9dAsu2PcPs_qLcC9h7ichyEChSeSRIkqOSBEChBTBdFlrTF9nrY9kefBTZUHv0wU0RcGvLRUAbT1n92tNTTlj7ZdhURFgtlBi4yYMsT_Obh06EXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از مدرسه دخترونه.
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/72925" target="_blank">📅 09:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72924">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05c961e8d3.mp4?token=GavkoFeeMIljhECQ7pCrrb8i98BW9zfO6TgpdSYvUjS_zAyFKxWrKTijVoxAax4tt1tUtHBPeqLuaEaGkTWtBoJ3o3zTz13SGv5ZUx-V2v2SNV4V5dzgwPPbi_k6n3MC82PMLackojY1OADA3BXOo_tt2zp_wmScXp8oYK519WxsI8KmFbbt1Uk9gzQ6G_U7gw0XHYdDPEcN6zxSc96iQfz8tPk8mijGjPW4YEEOlfxsDqrVxZJqzU1aXC5cU4I_teih_KAT9bBcRMmPQMxRu29tx9Foe2FQW-rMl4_6AhKStIKl682fm3suDlcJv1-j1gXixw1JMpbYM74C0WI5hFiHBNJePhku_3BeBjUOlIl6JExHu_69AqTc2EXjg8uQLfk4AJjokDGekE0g2rbocUxTDr_auavTmqMd3ZIYF-puLOxkzUMUn08WwHQFUKuyZfxObLH-OkBAoXWQuYinu1MmaOJcB7LOtEHghoMUwBd9DPgUCqtnQulXkC0lsCVlwXBZcnvbybyBzHGqoJVZhcL5X5P4rAgmc0FBHJlkcJSz0WFeS4DcXb7QpgA582xnweBy-74PsnkrjQqATM4xEIJCD1nH6B9hzWdAfmiwMmFbU7cwhg1SYYiO2atKGPXF7-gNtgzHpTn-qaA3SlrzT3o5K0NzaZpuSW1FhFeT3vY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05c961e8d3.mp4?token=GavkoFeeMIljhECQ7pCrrb8i98BW9zfO6TgpdSYvUjS_zAyFKxWrKTijVoxAax4tt1tUtHBPeqLuaEaGkTWtBoJ3o3zTz13SGv5ZUx-V2v2SNV4V5dzgwPPbi_k6n3MC82PMLackojY1OADA3BXOo_tt2zp_wmScXp8oYK519WxsI8KmFbbt1Uk9gzQ6G_U7gw0XHYdDPEcN6zxSc96iQfz8tPk8mijGjPW4YEEOlfxsDqrVxZJqzU1aXC5cU4I_teih_KAT9bBcRMmPQMxRu29tx9Foe2FQW-rMl4_6AhKStIKl682fm3suDlcJv1-j1gXixw1JMpbYM74C0WI5hFiHBNJePhku_3BeBjUOlIl6JExHu_69AqTc2EXjg8uQLfk4AJjokDGekE0g2rbocUxTDr_auavTmqMd3ZIYF-puLOxkzUMUn08WwHQFUKuyZfxObLH-OkBAoXWQuYinu1MmaOJcB7LOtEHghoMUwBd9DPgUCqtnQulXkC0lsCVlwXBZcnvbybyBzHGqoJVZhcL5X5P4rAgmc0FBHJlkcJSz0WFeS4DcXb7QpgA582xnweBy-74PsnkrjQqATM4xEIJCD1nH6B9hzWdAfmiwMmFbU7cwhg1SYYiO2atKGPXF7-gNtgzHpTn-qaA3SlrzT3o5K0NzaZpuSW1FhFeT3vY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو تهران، عده‌ای ساعت 9 صبح از خونه زدن بیرون، کفن پوشیدن، به سمت قوه‌قضائیه رفتن و به پسر پزشکیان لعنت فرستادن :
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/72924" target="_blank">📅 09:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72923">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/72923" target="_blank">📅 01:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72922">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/72922" target="_blank">📅 01:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72919">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZAwcLmWNg_2EoaLprX2Ub-8QmrD5YLVkcSDSY1oYvs0WstHfalIl0YBhO_uvWN1MQTOTKKe50ouahWfzad4HFlEE3TEIturERCQE8cTb7a8ZCzYzA1FTSMTTWU-q3G6u-z7rIHY-I7bjSmXbHxuamvvyizpohytz0PWHJH5-IbmmoSdzIbTZMz64GAAVwyfAAwbEkiH27RKnpU-ti0p4TfInzuYY64151OiAS5bhUozIWdTKrVcbNWWsmnWChrSmsLwVNnXs9nWxpcyFeCcnbHM6LjmdfAtcCYm50Z90zOVzOOiA_FpGZvsfz-praSpS7OUmriFd590XILtbOnGhEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ce4yhSfQTZ_wOkokYX2_MKq7S0MHreG8bO8k9uXq3NXetAfuIZIsenVotqscldQ0WkHyqIZF9Z-Ju2MOi9pC0xv8f3dEM18YkzpFEl1nqQrD2xCc-7X-VrIERg0QjYCX0o2i1ogSusX_Ke-38qUyVrGwsdADJ_QWDfjRC_jyafL9bPASjzcVmFeobBxkreKDUfOtyqYfBKA6D-E_8WBUb47FXMctWJC4iY-736r8X3m4dabL_cEeIgy87VPqyLeXX94kPO6r0Es5HpALOduB9zWHcRoYx5WY5tA9OmLvyzyPv7xhm6ETqJnMiNylm0eioajpmoT26379JKr3ImwIsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adea54d8bc.mp4?token=TFqQJi_dbAJTzrNZBlBY5jmxdUvquYI-AVCff7RYgehAEjfa1b8ACJVqOWEgDj9jr2HkBO0epgO2_Ey7VTKd2WPi_bJ557G3uAZhkyBQKU1h3nYSXZ5UFoN0yOlGS4fUnKcIldXs3nEpaqghyx3uiSRcbxPmw_9msyy4FL6aUmJvIT6g1kTuuEdFAuWyhNXZmAjCUXJzDIljV1X637BMbG9aPo33HJH5HUKK1oMxMj9wRgb239e5Edjm9lIvLcJVv45B9afDaXyRJaVtLIgTyfNw4qkv-c6XfSPI-EYsRe4f3ftDE_KlpNe20OfkhRKauThARQxmauK_PN0do4ScLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adea54d8bc.mp4?token=TFqQJi_dbAJTzrNZBlBY5jmxdUvquYI-AVCff7RYgehAEjfa1b8ACJVqOWEgDj9jr2HkBO0epgO2_Ey7VTKd2WPi_bJ557G3uAZhkyBQKU1h3nYSXZ5UFoN0yOlGS4fUnKcIldXs3nEpaqghyx3uiSRcbxPmw_9msyy4FL6aUmJvIT6g1kTuuEdFAuWyhNXZmAjCUXJzDIljV1X637BMbG9aPo33HJH5HUKK1oMxMj9wRgb239e5Edjm9lIvLcJVv45B9afDaXyRJaVtLIgTyfNw4qkv-c6XfSPI-EYsRe4f3ftDE_KlpNe20OfkhRKauThARQxmauK_PN0do4ScLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۷اکتبر ۲۰۲۶؛ناو هواپیمابر کلاس نیمیتز «یو‌اس‌اس رونالد ریگان» (CVN 76) در حال ترک سن‌دیگو:
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/72919" target="_blank">📅 01:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72918">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b185c0bc3.mp4?token=XIGvKj_m-14wbh5pJ4mg2fi483Ct4ufx7k-NbIKfIOYbE82gEzaw3uKuX0UCdaWR0J1uKBdQJ58r3Y3wj2i23-xRZcoIBdP7Sjv4Znh7-YuMKQKGVP563U07cGxu4OmDEJX-18beIMIOwZIF9DFK-zoBPlv6tStOIMChvXodjElYROBdnDR_mCUcU69pkCDqWzlyeICd332ziN5Dbvvk3at5dM7AgjbeZCdShrQvNIGjUdzjm7idlGOHReZdy6sWQ5LQISFCuAK9zqSS1e3DVbulc2-52T0eFj45jYA91RBywT9YmCHJLZUYmnPyE9O0LO8gMJi9UPnUt3WGy4Z5VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b185c0bc3.mp4?token=XIGvKj_m-14wbh5pJ4mg2fi483Ct4ufx7k-NbIKfIOYbE82gEzaw3uKuX0UCdaWR0J1uKBdQJ58r3Y3wj2i23-xRZcoIBdP7Sjv4Znh7-YuMKQKGVP563U07cGxu4OmDEJX-18beIMIOwZIF9DFK-zoBPlv6tStOIMChvXodjElYROBdnDR_mCUcU69pkCDqWzlyeICd332ziN5Dbvvk3at5dM7AgjbeZCdShrQvNIGjUdzjm7idlGOHReZdy6sWQ5LQISFCuAK9zqSS1e3DVbulc2-52T0eFj45jYA91RBywT9YmCHJLZUYmnPyE9O0LO8gMJi9UPnUt3WGy4Z5VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست وزیر جنگ آمریکا:
«ما با نیروی دریایی ایران به یه توافق رسیدیم؛ تصمیم گرفتیم اقیانوس رو باهاشون شریک بشیم.
نیمه پایینی اقیانوس مال اوناست.»</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72918" target="_blank">📅 00:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72917">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7AWcHv68OgmUyfr2lJblKEWhn1Evwb9iYrw_HXFwIj4jksuC2EI6noukzOC5tCIwJ-PwaaM-yM4YTwf5mxseoQzgjclQC6RmuxN2XZgrsbzFyNiuV8xFpSLFOPIC9Z7H2qZky0uGRXWqDM2ssRgPFb92nVPi5mdUV_LA72kaVtaxlLb3z2ZsL3365f_fK-XFE9i-vLYrq6aVnPNYI1pShGncQ2LnjhggG921qaQ7MA2Re2tlEqDIFvIJrgJnwbrHDbG3yaa42sKQWDF7lAK_JIbaHnG8naECmdFRgo6cA1lBCR-ah0T-mWicHPR8EmbAGMED_fMS2VvbFFtuTgFVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتلانتیک: کاخ سفید از پنتاگون خواسته گزینه‌های حملات جدید آمریکا به ایران رو پیش از انتخابات میان‌دوره‌ای ۳ نوامبر آماده کنه؛ البته هنوز هیچ تصمیم نهایی‌ای گرفته نشده.
به گفته مقام‌های آمریکایی، ترامپ می‌خواد قبل از انتخابات نشون بده که در جنگ پیشرفت حاصل شده و هم‌زمان به کاهش قیمت بنزین کمک کنه.
همچنین گزینه‌های اقدامات نظامی گسترده‌تر برای بعد از انتخابات میان‌دوره‌ای هم در حال بررسیه.
@News_Hut
| The Atlantic</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72917" target="_blank">📅 00:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72916">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce779c5dfa.mp4?token=AyWl8RUWBBSwecwIXKuXtsFk2POzCZ-OWMmOQIivOPcdZvhTL0lq_7MCLTXbYqvEAScDPI8m9B--izAFrIYIozWW3bab1szzaeDeovEW6zTjOShauKCqbXI_qsFE5CLD4X7Ua66IWARDPq3nbbhsf6PMeagOxecLKBLcexC8ItR1j2rLwVYxPNHYbPKvmYCvkl2Ddo_dcvhrTWeM-2SG5zCJhrEXawH-RvxclERf1iIUatiHthZgX4nOGUXTjJgcFNOhN1OWHmKXdEuFbylKHYXABMIZOragCHpfFBUYOCmYPPKitiFECmAwhgaaJ2gD2_fGb_juc6OzKq0K1mAUVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce779c5dfa.mp4?token=AyWl8RUWBBSwecwIXKuXtsFk2POzCZ-OWMmOQIivOPcdZvhTL0lq_7MCLTXbYqvEAScDPI8m9B--izAFrIYIozWW3bab1szzaeDeovEW6zTjOShauKCqbXI_qsFE5CLD4X7Ua66IWARDPq3nbbhsf6PMeagOxecLKBLcexC8ItR1j2rLwVYxPNHYbPKvmYCvkl2Ddo_dcvhrTWeM-2SG5zCJhrEXawH-RvxclERf1iIUatiHthZgX4nOGUXTjJgcFNOhN1OWHmKXdEuFbylKHYXABMIZOragCHpfFBUYOCmYPPKitiFECmAwhgaaJ2gD2_fGb_juc6OzKq0K1mAUVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست وزیر جنگ آمریکا:
«ما با نیروی دریایی ایران به یه توافق رسیدیم؛ تصمیم گرفتیم اقیانوس رو باهاشون شریک بشیم.
نیمه پایینی اقیانوس مال اوناست.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72916" target="_blank">📅 00:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72915">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4015ec5f18.mp4?token=tWt2KeTnmhfZXM4mwYYV7fDTuVQACTkQtT1kecaR_ygPLsJkxdh7POaYlHlSPYXNHYTPUGqIWVTcU7xHxzD1UeDQbuS2IiiZKpSJ8k15t2QfU27N9qJuiqOJiG2cbUEKxgql4DT4N66peII6tl_RkSjv483TzqO5q2evO4bbv4M5P5luVLF-B4paKqnuE8uoFwlW0goIx8Jf-UZvH27xkQfU3X4Q1LyDPKL9BU3FBeuYUIdTsFsKBSwTn4hxKUhYCDWHLie013ODwM0qZ1CNShLcFp7U1KmV8bUWdIFfQfeZn0is4u5KnXsbh12sT9nXiA-fUOLpdFHbyVGBydnmMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4015ec5f18.mp4?token=tWt2KeTnmhfZXM4mwYYV7fDTuVQACTkQtT1kecaR_ygPLsJkxdh7POaYlHlSPYXNHYTPUGqIWVTcU7xHxzD1UeDQbuS2IiiZKpSJ8k15t2QfU27N9qJuiqOJiG2cbUEKxgql4DT4N66peII6tl_RkSjv483TzqO5q2evO4bbv4M5P5luVLF-B4paKqnuE8uoFwlW0goIx8Jf-UZvH27xkQfU3X4Q1LyDPKL9BU3FBeuYUIdTsFsKBSwTn4hxKUhYCDWHLie013ODwM0qZ1CNShLcFp7U1KmV8bUWdIFfQfeZn0is4u5KnXsbh12sT9nXiA-fUOLpdFHbyVGBydnmMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله سرحدی، مقام طالبان:
زنان بی‌عقل هستند. آن‌ها از نظر عقلی ناقص‌اند.
آن‌ها هیچ‌چیز نمی‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72915" target="_blank">📅 23:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72914">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/982682c0ce.mp4?token=HYwl5kBAkq43NZ6CT-P5YGuW3u22Bz_CPNsJMzWc_1X4mjQS4M2NkqyiEEf17DMAM70BNqwGzgB50XaWyb-SGijcIhCcQ-9Awnqk0HkM4jqOdZW-2MENXR6OqAA3rAePEy9VSZXYPdOSCcd9oAV-_fbajuaQ5DYRzPnR_XAcGPL6sgOfgA-_RLs-AZXyhI8_naClCVueyJaBBJcWNE277F_TI-8LD_YWsmcbjUyoixbEF78mm8zTfAr0x8d2tNIMVcTGuWT-aKtLj8AM7fIFjEvJzHRd9q9IgqQM0YQRnzDN13eDSJHlXmJ5AkW_ZL6q5uCTOzbC5F61N9YN-Zk1EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/982682c0ce.mp4?token=HYwl5kBAkq43NZ6CT-P5YGuW3u22Bz_CPNsJMzWc_1X4mjQS4M2NkqyiEEf17DMAM70BNqwGzgB50XaWyb-SGijcIhCcQ-9Awnqk0HkM4jqOdZW-2MENXR6OqAA3rAePEy9VSZXYPdOSCcd9oAV-_fbajuaQ5DYRzPnR_XAcGPL6sgOfgA-_RLs-AZXyhI8_naClCVueyJaBBJcWNE277F_TI-8LD_YWsmcbjUyoixbEF78mm8zTfAr0x8d2tNIMVcTGuWT-aKtLj8AM7fIFjEvJzHRd9q9IgqQM0YQRnzDN13eDSJHlXmJ5AkW_ZL6q5uCTOzbC5F61N9YN-Zk1EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انگاری پرنده‌ها با این هموطن مشکل شخصی داشتن و اینطوری باهاش تسویه حساب کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72914" target="_blank">📅 23:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72913">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f06b3f32e4.mp4?token=p83g57JMwb6Ucwm228T6mEUn-u9wrsCu53lydzyVouhDJabRmOezsAG5vO40-_wX4lKbFWBHd43ce5e9bUJwt3moby56BjuKpwM31qIYb8x41AtpBYWFFAtMd4QPw1pKUrSdCJZBBn3JZbEntVigkpqSboTY48LnCEZbBBrenf5UFHQyqjMAsXHpM7MtTDJbxLHnT3Ay7JwKFuSYxMK_TmpsXUEoI4zNAxJObh1ZXVo2OQZl-tIIOlUY6N7pW3fQ1x8I89iCiKpty1BM5YiyPGYiMG6zQxgrmDWoseTSeDzdV8I3fpSxIGiht1qPKfYpz4JnORq445ZOmzoqIif7uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f06b3f32e4.mp4?token=p83g57JMwb6Ucwm228T6mEUn-u9wrsCu53lydzyVouhDJabRmOezsAG5vO40-_wX4lKbFWBHd43ce5e9bUJwt3moby56BjuKpwM31qIYb8x41AtpBYWFFAtMd4QPw1pKUrSdCJZBBn3JZbEntVigkpqSboTY48LnCEZbBBrenf5UFHQyqjMAsXHpM7MtTDJbxLHnT3Ay7JwKFuSYxMK_TmpsXUEoI4zNAxJObh1ZXVo2OQZl-tIIOlUY6N7pW3fQ1x8I89iCiKpty1BM5YiyPGYiMG6zQxgrmDWoseTSeDzdV8I3fpSxIGiht1qPKfYpz4JnORq445ZOmzoqIif7uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختره 300 تجربی شده و زنگ زده به مشاوره‌اش داره گریه می‌کنه که چرا نتونسته زیر 100 بشه...
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72913" target="_blank">📅 22:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72912">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aaff4cab2.mp4?token=fAF1-5E8N-6ZPF6r_3-S9PvQ7PHxaaF-bjhLVqpZRHWtjvSDNHuGdnjVK14nIwBSYB5Z6xdIT9JlXapecZfi1MOhbiWW30MZQq-7JG2FI2TLsdP63zyleCtatZAHouK-99JEaS8qjuT-lXxzEnQWHAvZwhmt86XcMG3H75DWmvMpe9NGIMhvwg-UrsKPJl-hb-vlKhQtIhvk1UTE9jo_wNUPFSibnP1lN6lFtMO8ycPefV68AwJ4TBt0ExT6kcP0tr1DBt7_aZF45SB9lLRqs-Eg9ORVFPIaYRYYdMgIwkGInx5XU4Ip5RiPOUAR27QEsFWTe7-IDc3pqNbhQvIIOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aaff4cab2.mp4?token=fAF1-5E8N-6ZPF6r_3-S9PvQ7PHxaaF-bjhLVqpZRHWtjvSDNHuGdnjVK14nIwBSYB5Z6xdIT9JlXapecZfi1MOhbiWW30MZQq-7JG2FI2TLsdP63zyleCtatZAHouK-99JEaS8qjuT-lXxzEnQWHAvZwhmt86XcMG3H75DWmvMpe9NGIMhvwg-UrsKPJl-hb-vlKhQtIhvk1UTE9jo_wNUPFSibnP1lN6lFtMO8ycPefV68AwJ4TBt0ExT6kcP0tr1DBt7_aZF45SB9lLRqs-Eg9ORVFPIaYRYYdMgIwkGInx5XU4Ip5RiPOUAR27QEsFWTe7-IDc3pqNbhQvIIOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیوپ برای استخر یک میلیارد تومان!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72912" target="_blank">📅 21:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72911">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b310f181e.mp4?token=ggcU_p3kZ8SI7rVIsrDIuFemgEfznFAV5AyuSKWS8ys0iidEAY-4eHkFAxPVtbww7t0N4SlfW33_n7E-W5VLgegcicSPgMwTr4oCKtnEm6StbV0fZo9_bT_-DvfRuNAeU8QsmPw1vtLS5WsyVGAgWhauTEb3pQoxfI6_QTMRdTK5yFip78wyMctNmW8Sg2svurcHaKVT91MkHjzz1HpRQNJvjCnc8lX_Rqu8MWWwRaUdq5DbtvjTjtNqePohmZ7z1nARAsevjkz2nKXiyzeeC45iVPkgkqilzmtxsrVt-6x7wD7_kgnjDNNKIo35nnH5vnGJQ46P2vTDT1rG9RHlrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b310f181e.mp4?token=ggcU_p3kZ8SI7rVIsrDIuFemgEfznFAV5AyuSKWS8ys0iidEAY-4eHkFAxPVtbww7t0N4SlfW33_n7E-W5VLgegcicSPgMwTr4oCKtnEm6StbV0fZo9_bT_-DvfRuNAeU8QsmPw1vtLS5WsyVGAgWhauTEb3pQoxfI6_QTMRdTK5yFip78wyMctNmW8Sg2svurcHaKVT91MkHjzz1HpRQNJvjCnc8lX_Rqu8MWWwRaUdq5DbtvjTjtNqePohmZ7z1nARAsevjkz2nKXiyzeeC45iVPkgkqilzmtxsrVt-6x7wD7_kgnjDNNKIo35nnH5vnGJQ46P2vTDT1rG9RHlrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«شاید من جلوی نابودی کامل جهان رو گرفتم، چون ایران هیچ‌وقت سلاح هسته‌ای نخواهد داشت. و این اتفاق خیلی مثبتیه.
رئیس‌جمهورهای قبلی باید این کار رو زودتر انجام می‌دادن، یا اصلاً یکی باید این کار رو انجام می‌داد.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72911" target="_blank">📅 21:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72910">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ecb506785.mp4?token=vyAVFA4KRFzM8LumP2d1mNamvHWVNk4ikbyR9UGDTKfKPD2bYy41CFkBJOtfT6lxE61p8EdNWd53ky1OodMBIlgbjVElB4xvXjb03AeGKEHG_oL0oMdaOmemzuV1U3PG5H8yDOJxHx5mf4IwjPKCui1Yxqb9A9OVXxG_KPBzcYUhR9N6RkbsTqwgTYmzB3iaElXb4oclW7JZqhrrYLLdYYjIrpmgn3N9p9UzQPXeXfNuuRaLzdaWNNK9nftFBQXcw39l7j4QDsb60-CEvd2TXv6_RfDRF_Onse9O0SSAXo768JdYtVK_0zdH2ZkKd-b5lWYMgb0vpSxjWUgYhRyU-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ecb506785.mp4?token=vyAVFA4KRFzM8LumP2d1mNamvHWVNk4ikbyR9UGDTKfKPD2bYy41CFkBJOtfT6lxE61p8EdNWd53ky1OodMBIlgbjVElB4xvXjb03AeGKEHG_oL0oMdaOmemzuV1U3PG5H8yDOJxHx5mf4IwjPKCui1Yxqb9A9OVXxG_KPBzcYUhR9N6RkbsTqwgTYmzB3iaElXb4oclW7JZqhrrYLLdYYjIrpmgn3N9p9UzQPXeXfNuuRaLzdaWNNK9nftFBQXcw39l7j4QDsb60-CEvd2TXv6_RfDRF_Onse9O0SSAXo768JdYtVK_0zdH2ZkKd-b5lWYMgb0vpSxjWUgYhRyU-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: الان از روسیه همون حسی رو می‌گیرید که اوایل کرونا از چین داشتید؟
ترامپ: «چین اون موقع خیلی چیزی نمی‌گفت و روسیه هم الان خیلی چیزی نمی‌گه. ولی روس‌ها می‌گن که اوضاع کاملاً تحت کنترله.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72910" target="_blank">📅 21:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72909">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded261ded0.mp4?token=Jqehxe3WTo009zaPVpNdPQKSePT8mTTMgraGBOwZWxSy1MjumnjkQLisOBrOc23KbAzdsgskN7OjzUnFicnupwLSEaGUkebkyczPZNq5PyRyRo88EeC_57WPmbBE7IAh4b8yx6p3cgwJRtHYnNBvZpycvowiqZXDCb5hV3oLO2teGt7A8UrLQEV9Nc2ZdOVr7WOEyvg-jMwvNm-NSzusDufTTZNQCQovC0dARK8akTIiIph5aI-Gr0d_joDw8jRzdRS94GdG2U9R7AplGPZA6WoT15lLYWiMqsjpQ0vBSlFBfaqqMcHKDjjQAmR3VayGXl17G_KVTy960haVSM42Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded261ded0.mp4?token=Jqehxe3WTo009zaPVpNdPQKSePT8mTTMgraGBOwZWxSy1MjumnjkQLisOBrOc23KbAzdsgskN7OjzUnFicnupwLSEaGUkebkyczPZNq5PyRyRo88EeC_57WPmbBE7IAh4b8yx6p3cgwJRtHYnNBvZpycvowiqZXDCb5hV3oLO2teGt7A8UrLQEV9Nc2ZdOVr7WOEyvg-jMwvNm-NSzusDufTTZNQCQovC0dARK8akTIiIph5aI-Gr0d_joDw8jRzdRS94GdG2U9R7AplGPZA6WoT15lLYWiMqsjpQ0vBSlFBfaqqMcHKDjjQAmR3VayGXl17G_KVTy960haVSM42Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا طاعون در روسیه یک سلاح بیولوژیکی است؟
ترامپ: «فکر نمی‌کنیم این‌طور باشه. خیلی زود متوجه می‌شیم، اما فعلاً فکر نمی‌کنیم سلاح بیولوژیکی باشه.
روس‌ها هم می‌گن اوضاع کاملاً تحت کنترله.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72909" target="_blank">📅 21:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72908">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا، در سن‌دیگو همراه با تفنگداران دریاییِ بال هوایی سوم تفنگداران دریایی در تمرینات بدنی صبحگاهی شرکت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72908" target="_blank">📅 20:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72907">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c97edc55.mp4?token=n07azNhjZaff3C1EfVFBEPty2P0pP2xbervo_Z-aiQk32X-IHjPBPKKa8tYNNF0TzeXp1wOgPUjwN5J-j4iXnaPpS_Ydhecc0w9HKDoJbE3VejnIAiucXXzvERdY-qWgtbkPd1UrUnYeY9GMYruVuA2bt36DGiwiFGM7gieYNgpo6ohg2_6D_J0cwTYOc4Ce_8WJ9KWNc7sue0ehkDX2Bs87_W2XcbKu-hP5cKAfn1y-B50vfl_XvK4DCSySSN9o1ApXDR2CRn--76iujOYTzhjdnQ4jRNIWCXfJEznPfd_iopT4L9Gadwy-STl6KOgYL-pAqmdusCxpP1LGEZHP7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c97edc55.mp4?token=n07azNhjZaff3C1EfVFBEPty2P0pP2xbervo_Z-aiQk32X-IHjPBPKKa8tYNNF0TzeXp1wOgPUjwN5J-j4iXnaPpS_Ydhecc0w9HKDoJbE3VejnIAiucXXzvERdY-qWgtbkPd1UrUnYeY9GMYruVuA2bt36DGiwiFGM7gieYNgpo6ohg2_6D_J0cwTYOc4Ce_8WJ9KWNc7sue0ehkDX2Bs87_W2XcbKu-hP5cKAfn1y-B50vfl_XvK4DCSySSN9o1ApXDR2CRn--76iujOYTzhjdnQ4jRNIWCXfJEznPfd_iopT4L9Gadwy-STl6KOgYL-pAqmdusCxpP1LGEZHP7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجایی که مشاهده میکنید تگزاس نیست، کوهدشت لرستانه که یه چند نفر با همدیگه به مشکل خورده بودن و تصمیم گرفتن با کلاشینکف حلش کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72907" target="_blank">📅 20:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72906">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXlXro9wdaigkDFBr4v_co9MQiSgXZCg25eJnf1Pf5E0GQcYUH3roQp5sX8DX7ZMx2LplyE2sq7aC0QHtRlWCFT70wTUVT_DDD0NVXYEG-xVNr6IxoHyOLT_ya0Z36dFuwd5CYIQ30UVch9q714i7q5wapzlK7HPPm8DuVCi-WNqvQWK6ZE1Cn3E7kas5zrVnv6J3PjRmHLRhzXtYC4y0zIpy913FtPXdviXiyy8FQBjIZzYcoAp5Mg3c8iHTdQjYgdcs7FIv3SbN3sXhsGd62YrLfSP-fQKhsWPyNSoDjBho3r1CO-jh313ADFR1lNjBNRKMgNrBI67feHy8DqdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: حزب‌الله حدود ۲۰۰ میلیون دلار از ایران گرفته تا بین لبنانی‌هایی که در جنگ امسال با اسرائیل آواره شدن، کمک مالی توزیع کنه
!!!
طبق گفته منابع رویترز، قرار شده به هر خانواده ۳ هزار دلار پرداخت بشه.
حدود ۵۰ هزار خانواده که خونه‌هاشون تخریب شده یا از روستاهاشون امکان رفت‌وآمد وجود نداره، در اولویت قرار دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72906" target="_blank">📅 19:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72905">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb95b8f0e3.mp4?token=JkQyy7GJvPTobNXNY2Hjb5LGpu7iYVr-4NRb9cNS4iVxe2pWktwS614EvLJ745yelJRgN7RPiowmj2DNK409-hw-9iJ3iFMAcTwfB6HJpl9ueSZb55iUvjfLW9XQH6oslQk6h5qfLWNvK98kuXgDtgSr2HaTis-QqqnWnPAX_646XTCHUDVtoKDRvAndos54ojy9FOylfek0N6uy5wfSFwgavD6kioML5aW3m8rSs8iawbx-zsmY6qHN93M1fyVcnlCYcvXmVsZo25zlj7yXd_wwsHCI3cPtF3CCIrSX3PrS9g5tjysXZKJd6zTKXVJvgMP8Ri7R1l9c4Ad3zpB6Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb95b8f0e3.mp4?token=JkQyy7GJvPTobNXNY2Hjb5LGpu7iYVr-4NRb9cNS4iVxe2pWktwS614EvLJ745yelJRgN7RPiowmj2DNK409-hw-9iJ3iFMAcTwfB6HJpl9ueSZb55iUvjfLW9XQH6oslQk6h5qfLWNvK98kuXgDtgSr2HaTis-QqqnWnPAX_646XTCHUDVtoKDRvAndos54ojy9FOylfek0N6uy5wfSFwgavD6kioML5aW3m8rSs8iawbx-zsmY6qHN93M1fyVcnlCYcvXmVsZo25zlj7yXd_wwsHCI3cPtF3CCIrSX3PrS9g5tjysXZKJd6zTKXVJvgMP8Ri7R1l9c4Ad3zpB6Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همتی: علت این‌که ۲ میلیارد دلار ارز برای بازار تامین کردیم این بود که به ترامپ و وزیر خزانه‌داری‌اش بفهمانیم مشکل تامین ارز نداریم!
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72905" target="_blank">📅 18:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72904">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a9610ab5.mp4?token=VgclEwo3KsolDYjH3FjKMuGCCOnZ-g8LjNbtnAHZIjiSEHcLPDTTevEBFNZn3qVw6rxM6376xPH_Vapg8R7HA-tDTacZg7XNZ9nvThb3Xqy7mn5JNagxtJCtwrxp2hww1tldOL_Dkh6QRsv0bwh6fxr3CBfvCey4JoT9-sTH_di7VU4B3WvNx1BOEjYaeMnbbUcjbOPr2WzLKUcsHP4deK3WIAa_kb34QlXu8GDXzfuYXFH0j9bqjyeu4zFrUg7QpfOTLBd5rwmtu0dfkP-86jaGbxvZalZxNBAUyKagO-nWAXUidiKQw72oEYIrie9Z-9EuoX94lPpsHFF43xvs7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a9610ab5.mp4?token=VgclEwo3KsolDYjH3FjKMuGCCOnZ-g8LjNbtnAHZIjiSEHcLPDTTevEBFNZn3qVw6rxM6376xPH_Vapg8R7HA-tDTacZg7XNZ9nvThb3Xqy7mn5JNagxtJCtwrxp2hww1tldOL_Dkh6QRsv0bwh6fxr3CBfvCey4JoT9-sTH_di7VU4B3WvNx1BOEjYaeMnbbUcjbOPr2WzLKUcsHP4deK3WIAa_kb34QlXu8GDXzfuYXFH0j9bqjyeu4zFrUg7QpfOTLBd5rwmtu0dfkP-86jaGbxvZalZxNBAUyKagO-nWAXUidiKQw72oEYIrie9Z-9EuoX94lPpsHFF43xvs7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#مهم
؛
مجری: «شما در سازمان ملل گفتید: «یک روز، که شاید این روز چندان هم دور نباشه، مردم ایران آزاد خواهند شد.» منظورتون از این حرف چی بود؟
نتانیاهو: «مردم ایران خودشون می‌دونن چه زمانی و در چه شرایطی باید کاری انجام بدن. وقتی زمان و شرایط مناسب فرا برسه، اون‌ها به پا خواهند خاست و این حکومت سقوط خواهد کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72904" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72903">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72903" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72903" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72902">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3tnzkPZTU41i8Il0x8yZFj9z9slzoa0_mQMl131aSd4jhPwmrmQQwE40KyVrBedVpXSjQDsGMSATypM4-24iSPc0rlxmgfxKlYaNKTZTfkrLrk3AxjwGvS_7_nvFU8Qx3zjBCMUUtzfE5L5UHSb1ZXfYWnsaPsViEoiK5GB12a8i5pQrCjfZMwOKYcPeyvjsCm_lgTypKlOdm5-oaDF-fAh3VCiYVdk-NWMg3k4aekdOu4NkGQPGLQLeZPpUn5q-W14kAuXp0JGtj-DwyYpj8ULBaQJQVVBz700dh_CAzWXGNQGesgnnPcUeJXcMsRVP-8vk7vg4_oweMqGdxxWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72902" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72901">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0613e028.mp4?token=C18I7yR7tqU0dMtUO4byQ4XqW251nY5ubY6MsihK_LWhnxtS_iJjqAGBiVogeqwVYRu8zhrU75cKPnxOpYGsEHG5m3f7uDEQZf2WoppixY-QONJc_dhjtPGtlvu_mmVCFdKVCTG3IgdNiQx9wvB_iVpHdWut2VSdSQtbj-Q0tSrwCYQ5XH80kRm5S1tLu2AXi0YeaxVunu3BRMddiZhYkIij16XlPzrJwT-lz49_zLyR47acbTyl9gRJOfy-vRhMI81Esww8wri0ia_hrkEtXlJ426cr8fR6IOWJBfwkXh7_hKFUx4Nj2kQxrR-XmTZYZ08Ey-E1QI2GghsgUof_iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0613e028.mp4?token=C18I7yR7tqU0dMtUO4byQ4XqW251nY5ubY6MsihK_LWhnxtS_iJjqAGBiVogeqwVYRu8zhrU75cKPnxOpYGsEHG5m3f7uDEQZf2WoppixY-QONJc_dhjtPGtlvu_mmVCFdKVCTG3IgdNiQx9wvB_iVpHdWut2VSdSQtbj-Q0tSrwCYQ5XH80kRm5S1tLu2AXi0YeaxVunu3BRMddiZhYkIij16XlPzrJwT-lz49_zLyR47acbTyl9gRJOfy-vRhMI81Esww8wri0ia_hrkEtXlJ426cr8fR6IOWJBfwkXh7_hKFUx4Nj2kQxrR-XmTZYZ08Ey-E1QI2GghsgUof_iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این تریلر Gta نیست، ایران خودمونه!
چند روز پیش توی بازار آهن تهران، یه نفر با ماشین میزنه به یه موتوری و فراری میشه، پلیس هم میفته دنبالش.
چند تا تیر میزنن به چرخاش و در نهایت گیر میفته و حسابی کتک میزننش.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72901" target="_blank">📅 17:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72900">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aced9e8ba.mp4?token=Whi8RWH_kDQq55IhMuPK_Yf9As6xXhiXfS6rwCmeFhYpJOicciDEc3uyRhKR5kc81WqpBeUa_Sxhof3_KZjiLplm9f0c4EIGFmAk5FFrmHtLWzhput2yx_HyBKFJ1rb8EAfXXv1e6w-07Qsuo9T31teXg3TAbRFUWpAhjb8L0PKjS9unJUQjuPAYUymbL0qlJXUJjt_eLxQtEs5WoEL20rPSeLO2aYcSO9aVrRBFAUuhURRHkyZ5BgcQo1I3WqOFZLfZNDN-H5P7CC-Lm65bkA2cXOqtzchv4L36m7v6acXmJnXNcl5wriyu8Poq9SKbnqSpq8HJaxQbiiJWcy9OIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aced9e8ba.mp4?token=Whi8RWH_kDQq55IhMuPK_Yf9As6xXhiXfS6rwCmeFhYpJOicciDEc3uyRhKR5kc81WqpBeUa_Sxhof3_KZjiLplm9f0c4EIGFmAk5FFrmHtLWzhput2yx_HyBKFJ1rb8EAfXXv1e6w-07Qsuo9T31teXg3TAbRFUWpAhjb8L0PKjS9unJUQjuPAYUymbL0qlJXUJjt_eLxQtEs5WoEL20rPSeLO2aYcSO9aVrRBFAUuhURRHkyZ5BgcQo1I3WqOFZLfZNDN-H5P7CC-Lm65bkA2cXOqtzchv4L36m7v6acXmJnXNcl5wriyu8Poq9SKbnqSpq8HJaxQbiiJWcy9OIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه خانم در جستجوی کار:
بعد دیدن یه آگهی منشی مطب با حقوق ۱۵ میلیون تومن رفتم مطب اقای دکتر
خیلی همه چی هم شیک و با کلاس بود؛
وقتی گفتم برای کار اومدم اقای دکتر(آلت متحرک) بهم گفت اون ۱۵ میلیون حقوقی که نوشتیم فقط ۶ تومنش برای کار تو مطبه و اگه ۹ تومن بقیشو میخوای باید به خودم خدمات جنسی بدی
😐
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72900" target="_blank">📅 17:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72899">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94cb601ba6.mp4?token=JdETC5TZxkteGvyyOJWZwIMAqPqY-XaLlh0i5lKFWCJKawTLfwcaQ8W43XHnjmWZDgoAJAV9g5QVPUg00kFMUBhzgMcEXnNCn2g3Zg12euThtTKDcZf6DtClhglhEiIUETLclG05eUn_OgXTpvsEMp5TqBqGdhs_VQ4kpqZ5leg9teE3qJy_kNp5YbUiGJKlhkorxmr1HBkNTX5k4UsbJURnNfgKQMb0WfTc6SdjYDSAz_whdXExJEr3Js5eC70wnv0oYMvJuM5NsdT6EPCmNq_71FEXma0ePM3DaCHgS_1Q8tuAOQsCXdngUBS-kKH4oGHxZuX4F1PleS1669OFhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94cb601ba6.mp4?token=JdETC5TZxkteGvyyOJWZwIMAqPqY-XaLlh0i5lKFWCJKawTLfwcaQ8W43XHnjmWZDgoAJAV9g5QVPUg00kFMUBhzgMcEXnNCn2g3Zg12euThtTKDcZf6DtClhglhEiIUETLclG05eUn_OgXTpvsEMp5TqBqGdhs_VQ4kpqZ5leg9teE3qJy_kNp5YbUiGJKlhkorxmr1HBkNTX5k4UsbJURnNfgKQMb0WfTc6SdjYDSAz_whdXExJEr3Js5eC70wnv0oYMvJuM5NsdT6EPCmNq_71FEXma0ePM3DaCHgS_1Q8tuAOQsCXdngUBS-kKH4oGHxZuX4F1PleS1669OFhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی از اینستاگرام پکیج پولدار شدن خریدی و خیال میکنی دیگه کار تمومه...:
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72899" target="_blank">📅 16:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72898">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7100f309a7.mp4?token=u45ry_UeSiRvKPUaQ4tQXg_FjfZQcjUb2M4PDFZ0SD-_ogC5mMOrisdQ8YTrgeGs3Mcr7LBD6qYgvEVca8R2ckHVR5CQAwmUqj04kfiYYKV7nXXg4sxiJh3bdiZAwh8KFkNQ2dWz4Gww2GWmb62yq331_w6fXkN-YPghVoQyn84DzGKlUkFeL02kzlPLaSRXaQnxosBvs0_dVhWuibHcXHgKoymOPEbZBwUHUv7-PQihil5QFDgfoCqZmTOH2LRbmNQB55llLRWJM18f5A2VYD18gxDOilmbjQ5GcTvgL5opUw10IsJbwh1J0CzakGvzC6jXs5E7xVZpxVLLMuwqHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7100f309a7.mp4?token=u45ry_UeSiRvKPUaQ4tQXg_FjfZQcjUb2M4PDFZ0SD-_ogC5mMOrisdQ8YTrgeGs3Mcr7LBD6qYgvEVca8R2ckHVR5CQAwmUqj04kfiYYKV7nXXg4sxiJh3bdiZAwh8KFkNQ2dWz4Gww2GWmb62yq331_w6fXkN-YPghVoQyn84DzGKlUkFeL02kzlPLaSRXaQnxosBvs0_dVhWuibHcXHgKoymOPEbZBwUHUv7-PQihil5QFDgfoCqZmTOH2LRbmNQB55llLRWJM18f5A2VYD18gxDOilmbjQ5GcTvgL5opUw10IsJbwh1J0CzakGvzC6jXs5E7xVZpxVLLMuwqHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از سورپرایز تولد علیرضا توسط مامانش. دخترا اگه نصف عشوه علیرضا رو داشتن سر خونه بخت بودن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72898" target="_blank">📅 16:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72893">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LLE2g-fCSryCzljLb-D-HjZCTaNo16suZbGg8Yc6pTBOdTMzp4iolk7iocZq_6ovX39Pyv7xhVpjOlMZQy4WZN9R0C6WzmkEf4dmyC4GD4wnfKPU4jMcCtrmy8RB3HW-qhLCH_oLHh3UXtjjNb5Oz-ZoI3vECEKmo7EvfgRt7gbmaDc5kQSDHzl3RaeaJB2YYYu2eIP2jwaOkcDgFx_4aT55vRH0Io0Vh06W29l5E4X0woTReBq4zeT1yEp4gFHS0Ft12jcfR-wohF-93Vyo9Qwvl66VOXCdLZA48kKShmAsWS1rlBBKQsXjY7JM9VuJ0esZKZXuuXezJk6uEM_mfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFJIlIi5iDnsHQCbn8MkqgTOXZujakpes54ZR_GJqwtdD0UYp6pKH-_dAQoZSkZFRUfJWy8xcMgpeb3MypDBfq5KNVutyXmfTU1rrK0jhk-rW6TPmFAB_qLLVfYvpMord6D8tkSAm1EEqhEGX7yq98xB3qcDpnnkP35xUVwqs52NfAExhQ2ktAUapiW1lNXtc4MwqJ5M4udNA-8pBCAdQIvwc_bFw37_Z5OffiFPV_lsWEMMxQiya5_q12n71kEhjLUPPEDnqKm0VqugsjhycV0R-iOZ2GzgsNy6iuEnR12fbvbq0EjOkhjWXM2XrFsoxz09H2P_GMieMLa0mVTIIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d935bdc93d.mp4?token=Mhr_vNGotDc0vZk-bTBZCGaHi20bhd1QDhs8BPG6YxCzggzUsOGCSNtJUMzZKPVVvK1zJyLLsljcNM0VksvbU3y0idjG8Ojueh806wBGJEZJRa5jPVuf_CNSG_g6rGf86jWlwjdVW-bFDKp-ctTTrMaM_0rBz0FsVEvtnjOfjNT_N0XStCHqbTsxUNpM6L9aAKwzm0X94O1M3A2gm9Kzll-YLGmjzhs8nlLusyW4ZQmoGkHj2M9ytuiSyEMACYH5aGq3WIYckVNCTCh9rYOLDnShOJLHmq6NPFFUnIoOAoL-8NlLYtrnC4VYo_RjpgS9Df1hLaUB973gS-NGWo4zhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d935bdc93d.mp4?token=Mhr_vNGotDc0vZk-bTBZCGaHi20bhd1QDhs8BPG6YxCzggzUsOGCSNtJUMzZKPVVvK1zJyLLsljcNM0VksvbU3y0idjG8Ojueh806wBGJEZJRa5jPVuf_CNSG_g6rGf86jWlwjdVW-bFDKp-ctTTrMaM_0rBz0FsVEvtnjOfjNT_N0XStCHqbTsxUNpM6L9aAKwzm0X94O1M3A2gm9Kzll-YLGmjzhs8nlLusyW4ZQmoGkHj2M9ytuiSyEMACYH5aGq3WIYckVNCTCh9rYOLDnShOJLHmq6NPFFUnIoOAoL-8NlLYtrnC4VYo_RjpgS9Df1hLaUB973gS-NGWo4zhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز، ۷ اکتبر، سومین سالگرد «طوفان‌الاقصی»؛ حمله‌ای غافلگیرکننده که سال ۲۰۲۳ توسط حماس و گروه‌های مسلح فلسطینی انجام شد و حدود ۱۲۰۰ نفر در اسرائیل کشته و ۲۵۱ نفر هم به گروگان گرفته شدند.
بعدش اما ورق برگشت؛ جنگی شروع شد که نتیجه‌اش ویرانی بخش بزرگی از غزه و کشته‌شدن ده‌ها هزار فلسطینی بود. اسرائیل هم از همون اول گفت قرار نیست ماجرا رو همین‌جا تموم کنه و دنبال کسانی می‌ره که در حمله ۷ اکتبر نقش داشتن.
و این وسط، فهرست ترورهای اسرائیل هم کم‌کم بلندتر شد؛ از فرماندهان حماس و حزب‌الله گرفته تا چهره‌های ارشد نظامی و امنیتی جمهوری اسلامی؛ یعنی جنگی که قرار بود با «یک حمله» شروع و تمام شود، سه سال بعد هنوز کلی حساب باز و بسته‌نشده پشت سر خودش گذاشته.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72893" target="_blank">📅 15:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72892">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GR2jb0RuNOjz1-_ZYXBl6sZKOFCTzDi8QMjUhauOGZFkUwJ7mZdT8lY7ZuykMmT-ThCl1qsiHG_rqSjVYX2eS5-ULYdSiqfZdpvqC3vC5v9s562P43WuJUiP3kSNI_sijWDqLx5ydYVRXBajNWU5WiQSO8TZFOvmflXfliwce0cPl9jFNM_5ndKee0BAtlhvKkiBP6YWmENELrZMdnc1hqwk-nS_udw1qUkc_4La4vM5iij-XTztRtfAL7tCtRdHLcOAf0g5IQHGVYjEeoQID_DYKekpIyevsI78235XEpRDG-w06JdqD-Hn3AP0kQ-YI-I-fo8FEt0sMrygx_7-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رتبه‌های برتری که مدرسه فرهنگ (وابسته به حدادعادل) تو کنکور امسال داده :
زرین، پسرِ بادیگاردِ علی خامنه‌ای : 16 انسانی
محمدباقر، پسرِ مجتبی خامنه‌ای : 106 انسانی
محمد‌امین، پسرِ بذرپاش (وزیر راه سابق) : 173 انسانی
محمد، نوه حداد عادل : 910 انسانی
محمد، نوه محسن رضایی : 1700 انسانی
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72892" target="_blank">📅 14:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72891">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e1e3a6f34.mp4?token=AGFWSqvmRYHch8FOKhMpJemtJAGf28DmOxSBOFxMTeMMofYErR2NvWAL6Y-QR3TOEVZ9OS82jtJz1rdrGFX-bg9rODepKVyrdiyV7qVeaPzIt8Z48MWoXfhmSBF65hyiUYIvlsKEze_QMprAV9OwkvjY0zthveuuEKqsnzALfv-a1K4A3-e43zpg1C-dmkUtox7YMe90wGS4l4zOIwkfGGGux2Pm24YogwQgqTzBlZvu8YTXj8rFIKIrLrh-D1T15ocbykR19OfnLRzgIlntnA18FMvqwlYfiTldqjY6die7RB9jriNqLzSjXOlZt_R7n0TQv88kP5IguRCP0cIioA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e1e3a6f34.mp4?token=AGFWSqvmRYHch8FOKhMpJemtJAGf28DmOxSBOFxMTeMMofYErR2NvWAL6Y-QR3TOEVZ9OS82jtJz1rdrGFX-bg9rODepKVyrdiyV7qVeaPzIt8Z48MWoXfhmSBF65hyiUYIvlsKEze_QMprAV9OwkvjY0zthveuuEKqsnzALfv-a1K4A3-e43zpg1C-dmkUtox7YMe90wGS4l4zOIwkfGGGux2Pm24YogwQgqTzBlZvu8YTXj8rFIKIrLrh-D1T15ocbykR19OfnLRzgIlntnA18FMvqwlYfiTldqjY6die7RB9jriNqLzSjXOlZt_R7n0TQv88kP5IguRCP0cIioA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوچک زاده نماینده مجلس:
به یوسف پزشکیان بگید یه بچه دبستانی از پدر تو بیشتر میفهمه!
حرفایی که تو میزنی باید امریکا بزنه نه پسر رئیس جمهور ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72891" target="_blank">📅 14:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72890">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab42cc577.mp4?token=bCwwLzwydRKsgwPAwBxdwhMR5voxK76-XAR4W92J9bIDI7yZS-XRpviZ00sjubLY4YehB3ez72rllDHhxkxhFou6MqKjsipK3-5_sLDxZIq36FtZMqOkCnQWi9We9eEU5UX2_rdJfAsZytyW66G9_4LtB6bDilZg2O3lbrZ4x_zKTsqeNbvxcoDm_1i5wjsYtFZ9bnePaurGWffwFTp7w5n8d7SgipUoMhyGFfOSLRjcBSz2apEufLFn2fxnaMXsrSvNaj8ltJdpHwat3SvzBTR6HWUhiim3tAoTV4L_ikEjE0EOAssdUCk3D0rls4Wr4HCTZREXAZlTDR9aJ5fmeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab42cc577.mp4?token=bCwwLzwydRKsgwPAwBxdwhMR5voxK76-XAR4W92J9bIDI7yZS-XRpviZ00sjubLY4YehB3ez72rllDHhxkxhFou6MqKjsipK3-5_sLDxZIq36FtZMqOkCnQWi9We9eEU5UX2_rdJfAsZytyW66G9_4LtB6bDilZg2O3lbrZ4x_zKTsqeNbvxcoDm_1i5wjsYtFZ9bnePaurGWffwFTp7w5n8d7SgipUoMhyGFfOSLRjcBSz2apEufLFn2fxnaMXsrSvNaj8ltJdpHwat3SvzBTR6HWUhiim3tAoTV4L_ikEjE0EOAssdUCk3D0rls4Wr4HCTZREXAZlTDR9aJ5fmeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر نتانیاهو درباره ایران:
«کشورهایی که حتی به ما حمله می‌کنن، یواشکی و در خفا می‌گن: اینا باید سقوط کنن؛ دارن همه‌مون رو خفه می‌کنن.
ما مطمئن می‌شیم که سقوط کنن. سقوط می‌کنن.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72890" target="_blank">📅 13:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72889">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec68a44315.mp4?token=I-3rBJU5sU86q4JDxHY60bILlyFaxFqmjqnmcnSWEtKKI3aUZMqQiLb6WvJrfcB0SkNHdhe7tM02mGSDm_uNAdCcMZrNQPMmIiPjqEr3mR84NjLyFGzD2iuUMNxAkMakYB3EW7HxmmItkpq-St_P5k50Sir2U6PzepB6LPcsddFYv2U0EjydypTB2T-CrGSVm1L55bPn1Qz6dptd_CUGz4u3NuZrzKfrbZnl6HBMAXLY930Q6Mev1inJbl46TETIlu2nbsutB7MZ--yjB5F53KPQk2LM-RaV-DdK9UGYkxf9suuNUdWcj5gK8zpeyyMaaMmxnmG4zY8ICnu6_yX32g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec68a44315.mp4?token=I-3rBJU5sU86q4JDxHY60bILlyFaxFqmjqnmcnSWEtKKI3aUZMqQiLb6WvJrfcB0SkNHdhe7tM02mGSDm_uNAdCcMZrNQPMmIiPjqEr3mR84NjLyFGzD2iuUMNxAkMakYB3EW7HxmmItkpq-St_P5k50Sir2U6PzepB6LPcsddFYv2U0EjydypTB2T-CrGSVm1L55bPn1Qz6dptd_CUGz4u3NuZrzKfrbZnl6HBMAXLY930Q6Mev1inJbl46TETIlu2nbsutB7MZ--yjB5F53KPQk2LM-RaV-DdK9UGYkxf9suuNUdWcj5gK8zpeyyMaaMmxnmG4zY8ICnu6_yX32g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران:
«هر دلار و هر سنتی که این حکومت به دست میاره، خرج جاده و پل یا بهتر کردن زندگی مردم ایران نمی‌کنه.
این پول رو خرج حزب‌الله و حماس و شبه‌نظامی‌هایی می‌کنن که از داخل عراق موشک شلیک می‌کنن، و همین‌طور حوثی‌ها.
باید پولشون رو برای مردم خودشون خرج می‌کردن، اما به‌جاش پول رو صرف تروریسم و تسلیحات می‌کنن.»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72889" target="_blank">📅 13:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72888">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aba6a5b62.mp4?token=ATGe7BkC9Hmm-EF3O7sqgheRTw3HyH-eYr78zGDEmIgPUSBBM6BKANjIVsqbBmf8bvSexQwTkvjUoEcoYXR72dfm84eghY6jLIBeoOXtmhqaZv2pgG9lkqRTT-2D-1Z9kTe2kdh6vvmzoGgh5aeiKoOzZcQpzD4xT5NpooRbssqLf2FpqqpZrRbwSXYR1S5IE9c4EYRO09OdA3zknWCjwiNiq-QdRZesNGJF5JfpmPLK055ka4zj50w2joBWq6KZbySpTBxYE6dkEs6CbCtp8Iw-jjdsV6fsBQto5Vgj020xIaWhcmB7q1GAcZ1kT10OPJjzMtRPy1a4zjWkbmVODjOoguwwmAQmf0Np02YSfXQybjBplQkDkCO9BMVi3SnTPVfHu4w1D9kQJ0FQjXAxun4PY3s9cTnCG_G6w4-EMlWqYrAz__xTFS6qeBsTPBSY-ERzsyXVFT1SnYT3EZVeWui0OyrcGqqfIkb-N3HqCumBOBRxobHlz6SWjr1MW6C6caQa-BN9s3FVxnXM4x5Hkw_2NV2Yq1hh9GUIluGBzJROxF2PvbdkVvt9-VzhXj7QdeBU66BtO8D0IyeNruHbtjyR8G-DXz3vCTVVm5NgUf9iRDYp2CZiVVW1Y3nPAaefcXjbxlFJf8t4e_I6CD4Gi-BIJD-RbnGZ4OAzM4oJ7Wo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aba6a5b62.mp4?token=ATGe7BkC9Hmm-EF3O7sqgheRTw3HyH-eYr78zGDEmIgPUSBBM6BKANjIVsqbBmf8bvSexQwTkvjUoEcoYXR72dfm84eghY6jLIBeoOXtmhqaZv2pgG9lkqRTT-2D-1Z9kTe2kdh6vvmzoGgh5aeiKoOzZcQpzD4xT5NpooRbssqLf2FpqqpZrRbwSXYR1S5IE9c4EYRO09OdA3zknWCjwiNiq-QdRZesNGJF5JfpmPLK055ka4zj50w2joBWq6KZbySpTBxYE6dkEs6CbCtp8Iw-jjdsV6fsBQto5Vgj020xIaWhcmB7q1GAcZ1kT10OPJjzMtRPy1a4zjWkbmVODjOoguwwmAQmf0Np02YSfXQybjBplQkDkCO9BMVi3SnTPVfHu4w1D9kQJ0FQjXAxun4PY3s9cTnCG_G6w4-EMlWqYrAz__xTFS6qeBsTPBSY-ERzsyXVFT1SnYT3EZVeWui0OyrcGqqfIkb-N3HqCumBOBRxobHlz6SWjr1MW6C6caQa-BN9s3FVxnXM4x5Hkw_2NV2Yq1hh9GUIluGBzJROxF2PvbdkVvt9-VzhXj7QdeBU66BtO8D0IyeNruHbtjyR8G-DXz3vCTVVm5NgUf9iRDYp2CZiVVW1Y3nPAaefcXjbxlFJf8t4e_I6CD4Gi-BIJD-RbnGZ4OAzM4oJ7Wo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
«اقتصاد ایران داره به نقطه‌ای می‌رسه که از نظر شدت وخامت، فقط تعداد کمی از کشورهای دنیا چنین وضعیتی رو تجربه کردن.
و تمام این وضعیت تقصیر روحانیون شیعه افراطی‌ایه که توی اون کشور تصمیم‌گیری می‌کنن.
همین‌ها هستن که مردم بیچاره ایران رو به این شرایطی که الان توش قرار دارن، رسوندن.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72888" target="_blank">📅 12:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72887">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aatAPQ8lo2JlEGjhJFpGavR8FX9MpGk-LlDqy03z8ak4La9IABlocE4Ofw39mnsEGFu1_ROXKa2eLNIOnBdLIhLpjeulBJZFnE5aULqSi-XthA-NaGWmEQMnPvUckh-PMc5af8TSf7nZNlD67hpX8p-Ha0bu-iOfcT4HIDlnHmJGLnkUOeWhBBEfDVfOem2pIGtw5EjB2IwYYSjJAKekj1oi6zpm96dQ3fbz92UYxEAh-ZnWE4DvZGECvsreNgXzyKByHmvD4RSxxTEH4tYqvaV4cNObvHIltQ9Zm_UIThenZjv-SJMgiU3wScxUmNRZENMCNqrSfFbawJX6EPQ9Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله ونس، به رویترز گفته آمریکا هنوز دقیقاً نمی‌دونه بعد از کشته‌شدن علی خامنه‌ای، چه کسی در نهایت تصمیم‌های اصلی ایران رو می‌گیره.
ونس گفته آمریکا در حال مذاکره با مسعود پزشکیان، رئیس‌جمهور ایران، و عباس عراقچی، وزیر خارجه است، اما مشخص نیست این دو نفر در ساختار فعلی قدرت ایران چقدر اختیار و قدرت تصمیم‌گیری دارند.
او گفته یکی از چیزهایی که آمریکا متوجه شده اینه که «کاملاً مشخص نیست ایران چطور تصمیم‌گیری می‌کنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72887" target="_blank">📅 12:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72886">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGesCtXQ_qiiV6CNbUOzCSfFAx9PJmWOqP5_krjWyWkEH0zthv-dObdfDUZneonvuIUcTJoYC0sUOAm5EPMC5trSgMvOC8ho5K9WI-941LGQGlo2SBbqZvktMCXIwtUidjLZtxmheB-46zdU_SJP-tSC7kivctvdLf52bv5D_g1ysYkzLoTPyLxj4AtcjRkjfohS2QvHzhchT86IReM6iz5zXIyHMkCMNwu4krLDQw0b-90qLVohgntMUkS6oDTEscULwLB_8HuYpv6GVLofFJDQS0qcgxDT-FyRKUT8sunpS_9EaTb7vp7SVvQfhdc9lN5Dr1vmJXIkqs_5A5erbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله ونس، معاون ترامپ، به رویترز گفته اگه ایران بخواد به توافق برسه و جنگ ۷ ماهه با آمریکا تموم بشه، باید ظرفیت غنی‌سازی اورانیومش رو به‌طور قابل‌توجهی کاهش بده.
ونس گفته آمریکا دیگه به وعده و قول برای محدودیت‌های آینده اکتفا نمی‌کنه و باید اقدام واقعی و قابل لمس از طرف ایران ببینه.
اون همچنین پرسیده: اگه ایران واقعاً دنبال ساخت سلاح هسته‌ای نیست، پس چرا باید اورانیوم ۶۰ درصد غنی‌شده داشته باشه؟
با این حال، ونس گفته آمریکا همچنان برای توافق آمادگی داره، اما امتیاز هسته‌ای واقعی از ایران می‌خواد و تأکید کرده: «قرار نیست حرف رو با عمل عوض کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72886" target="_blank">📅 11:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72885">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bff0381d0.mp4?token=CTxdx6dgSmXO3VjNdO0VX4zYKmmyvHhKOsiRSsu5lkdW9NZc5PKQ1Er7RA4QX4VrfvKXwv6Ikg9FdxSgpTwIIyie78B8WfJRV5R4zDZ8DZos-lnzTkFS40VljwxLy9TsZRelkElGH38rz5rn4KzfTeKHyV6woYlb_nFjNSZrKmSMOP8yzHBLv51kxwHh3HKqPzDYworTnGw7iNa9UWHnKabkbQLzRVJcThr2c9Qk4mav6ysWY3GQCSSUAYEfHAnt31-B-7TkRF3Xu7NTQouJAFFjNZBN2jIgSvBzOa5lJADSEG0XBIUx089nYavhhhI-Fr4pXxjHhNu8JImAAv03ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bff0381d0.mp4?token=CTxdx6dgSmXO3VjNdO0VX4zYKmmyvHhKOsiRSsu5lkdW9NZc5PKQ1Er7RA4QX4VrfvKXwv6Ikg9FdxSgpTwIIyie78B8WfJRV5R4zDZ8DZos-lnzTkFS40VljwxLy9TsZRelkElGH38rz5rn4KzfTeKHyV6woYlb_nFjNSZrKmSMOP8yzHBLv51kxwHh3HKqPzDYworTnGw7iNa9UWHnKabkbQLzRVJcThr2c9Qk4mav6ysWY3GQCSSUAYEfHAnt31-B-7TkRF3Xu7NTQouJAFFjNZBN2jIgSvBzOa5lJADSEG0XBIUx089nYavhhhI-Fr4pXxjHhNu8JImAAv03ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخوند نبویان: نماز و روزه و گناه و... مهم نیست همه کار باید کرد تا نظام حفظ بشه!
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72885" target="_blank">📅 11:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72884">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94194705f4.mp4?token=FHGgq3R4WXW7afcoEufFT0xWnBZ-0HPNdei0FmdBgT-s6--PaL7623MGCIylicGtPmIiyMgBGQfCymw4o2fGh-_TYtxSEw5WeWBm40so-3A8jPg-BKROCiyWwHildeHymvunaq1WcOTHNvS8RjsdOWmgK7TnfjnevJ_K9n_BGvy8PfKvw2pCq0QyHiOapcgB8jj0tJpiqYPVRx7eFTPi4GXIiUOI4atP5iGe6qjIet14437ovXKxrappmISzPBjWRjPYNT9caOPJhmGgyh9N56REmZn7YMmwag8qpA8BVrBrBoQ1Kl2at0yByU06dQDNF9cM4XXrZ_y0A_1RI6ClKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94194705f4.mp4?token=FHGgq3R4WXW7afcoEufFT0xWnBZ-0HPNdei0FmdBgT-s6--PaL7623MGCIylicGtPmIiyMgBGQfCymw4o2fGh-_TYtxSEw5WeWBm40so-3A8jPg-BKROCiyWwHildeHymvunaq1WcOTHNvS8RjsdOWmgK7TnfjnevJ_K9n_BGvy8PfKvw2pCq0QyHiOapcgB8jj0tJpiqYPVRx7eFTPi4GXIiUOI4atP5iGe6qjIet14437ovXKxrappmISzPBjWRjPYNT9caOPJhmGgyh9N56REmZn7YMmwag8qpA8BVrBrBoQ1Kl2at0yByU06dQDNF9cM4XXrZ_y0A_1RI6ClKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم زیبای و ویژه برای وداع با مسی با نمایش پهبادی در آسمان!
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72884" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72883">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72883" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72882">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLrrN9eIBpx1SFKlk_yX7OZsg64K2_AZX0qhTahCDJd1kXe-I9KKBcq102oT3brsweCUHXH3KuHQHlzzCRbNbjSnbGCvHI5ooQy7XipNuNtDt1RWf9uD5JS0r2eOjdAj4npxMeU8JbZfn8aHGja2k8-6PeRDximicVanUw9FD9oZ_Fdcnh0vWy8Y5yGlMvxzw2cJZDmx0QknyZIX_Xs2P2tZoDH1hdoHRxHX0xlptromGs3cGEO2wOHIS6hytlCS5FW448X5oQN5Sx2oKaxaicKJd-7levoxIaRCi2Fn-YTMBRo29-hgrTW5XD4Jw-nSazXQbkycMwXh7Wa5d4XMJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72882" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72878">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d39cf67708.mp4?token=KjofhmbK6Uxk5tNL3mAqXmSb9pW28HpNC38y0pc5N6u5qZ3emRtGg5BDa8we4zKvHL3I9VXiljFZJMQeMZpNhq-X2MtG6s3cP1w8ErK9ib-dj48LKU1dDvJIMz2shnNXZsHMwd64ipu7OIEsacM3CFfdvds2iJPpISqkK2sxtClXWd67KX7aAfYNnsvd7lpYUA5QJuXbNcT4eqS2NS6pcnitan5yAWutvOFXN5F6MYdCMVxbKJYiugt75jjETcuhr2Cpt28V0QAObssxwvpxITtnHam6Z03Qlc9Wx853QcyUPGrtkhPlaW5eF8SeL4OqjuiD3lVrKhC6n_85IpQgEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d39cf67708.mp4?token=KjofhmbK6Uxk5tNL3mAqXmSb9pW28HpNC38y0pc5N6u5qZ3emRtGg5BDa8we4zKvHL3I9VXiljFZJMQeMZpNhq-X2MtG6s3cP1w8ErK9ib-dj48LKU1dDvJIMz2shnNXZsHMwd64ipu7OIEsacM3CFfdvds2iJPpISqkK2sxtClXWd67KX7aAfYNnsvd7lpYUA5QJuXbNcT4eqS2NS6pcnitan5yAWutvOFXN5F6MYdCMVxbKJYiugt75jjETcuhr2Cpt28V0QAObssxwvpxITtnHam6Z03Qlc9Wx853QcyUPGrtkhPlaW5eF8SeL4OqjuiD3lVrKhC6n_85IpQgEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره رسیدیم به اون لحظه‌ای که عاشقان فوتبال تحمل دیدنشو ندارن...
لیونل مسی، اسطوره ۳۹ ساله فوتبال، سه‌شنبه ۶ اکتبر ۲۰۲۶ برای آخرین بار پیراهن آرژانتین رو پوشید؛ این بار در ورزشگاه مومنتال بوئنوس‌آیرس و مقابل بنین.
مسی بعد از سال‌ها افتخار، جام‌ها، اشک‌ها و لحظه‌هایی که برای آرژانتین ساخت، جلوی چشم هوادارانی که برای خداحافظی باهاش ورزشگاه رو پر کرده بودن، رسماً از تیم ملی خداحافظی کرد.
از این به بعد دیگه مسی رو با پیراهن آرژانتین نمی‌بینیم؛ پرونده یکی از باشکوه‌ترین دوران‌های ملی تاریخ فوتبال هم اینجا بسته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72878" target="_blank">📅 10:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72875">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca1a543a9.mp4?token=L4Q4tSlXiCtVdQ6XR319faT5zpv60Dl9AxH29NVL3aC5b9Oo-LLAS80jmfD9KUOJA7_sUxTtw1qXbSlAdwlksggDcIKUlX-RTL4AJ9LVTs5EEC8R8Ct0AafA5LaeJA-DJebTV1nTdXL04ESJ2mJVcbwvQNkSSvURxRHa-pUdd6_rtGx-TeEb6z1Ei_KxEpRH2uaeIUiGAMHA6zJoTNM9rHkZHxHIhP2mFuZt_qisKKwEBNu3RSiErZ8h-v1w3XO5P4Rl1EvhD5gznLN4-UKQ22p5C4DUxL7hOEFtVoxutp_h8EenXSYb0Nafe8FheqDSatQpJewygte3Uq9m8O5-fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca1a543a9.mp4?token=L4Q4tSlXiCtVdQ6XR319faT5zpv60Dl9AxH29NVL3aC5b9Oo-LLAS80jmfD9KUOJA7_sUxTtw1qXbSlAdwlksggDcIKUlX-RTL4AJ9LVTs5EEC8R8Ct0AafA5LaeJA-DJebTV1nTdXL04ESJ2mJVcbwvQNkSSvURxRHa-pUdd6_rtGx-TeEb6z1Ei_KxEpRH2uaeIUiGAMHA6zJoTNM9rHkZHxHIhP2mFuZt_qisKKwEBNu3RSiErZ8h-v1w3XO5P4Rl1EvhD5gznLN4-UKQ22p5C4DUxL7hOEFtVoxutp_h8EenXSYb0Nafe8FheqDSatQpJewygte3Uq9m8O5-fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی ایتا و روبیکا تصاویری از یه سلاح ایرانی تو مرز ایران و عراق منتشر کردن که حتی خودشونم نمیدونن دقیقاً چیه :
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72875" target="_blank">📅 10:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72874">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78e235c72.mp4?token=T6OvhZSPHFpo5-eViDqCb44WvYLsOAMTmjcvTr6IrmOhFJI-EZkeOMmsQSuodubemgyzhOYuA3FtRhZS-fzRAWaXXyy53UIac0vM8n4MG0sQCzvzHmC5fgsL4iXSww42ohR36G6KVmkw0q-HQxpoRmRMWvAPtPhqdVO8Msa6BdMmq06PspmGicUUmeT3qPSYWghdoc3bdG7eI82nalqked-rk5agueVkJnST378wQ7oFk7o7AaVWqbRisesfwG5kVHXCxdDBERE7JrB2PRrcGZOYV8Kg7o8OVSCRX6So85J512C5ajXOSp2l9RpJdEnIds2ExJdbcKbeiPL_6jM-2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78e235c72.mp4?token=T6OvhZSPHFpo5-eViDqCb44WvYLsOAMTmjcvTr6IrmOhFJI-EZkeOMmsQSuodubemgyzhOYuA3FtRhZS-fzRAWaXXyy53UIac0vM8n4MG0sQCzvzHmC5fgsL4iXSww42ohR36G6KVmkw0q-HQxpoRmRMWvAPtPhqdVO8Msa6BdMmq06PspmGicUUmeT3qPSYWghdoc3bdG7eI82nalqked-rk5agueVkJnST378wQ7oFk7o7AaVWqbRisesfwG5kVHXCxdDBERE7JrB2PRrcGZOYV8Kg7o8OVSCRX6So85J512C5ajXOSp2l9RpJdEnIds2ExJdbcKbeiPL_6jM-2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک اخوند در تجمعات شبانه: ناو آمریکایی آنچنان از ترس موشک ما فرار کرد که چند هواپیمایش تو دریا افتاد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72874" target="_blank">📅 10:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72873">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=NGijFZlVksxD-F7vFd6t-OxXQGNBPltCenOKEXruLt_qJFT1S9OLKQZZoGP9h1DtCiSKlGXue93QrVUiDMwcGdyh2TrRG-14rswC6Pee4gDBp0M4e_IARQwBKi2WacbO8L2wax81tu3hUgjSzMk8_meO66nLm0q6fBP8_b7fsKltgGlfqScnrzNTRXpAhTnOjbxYoNPhmd4PpUUP3vKbH0C08XhBczkFPlc7e3TDUOhwHCpo0Tp05NcjXS7qDZg2wes3lGrAjlHdHmiAWx98rDNCBnXpZawNL3T66mjGaVQvnAlTxXy3d1OvUZ4dPAAmgIkaHFaZ2VN_uVxCwz4xZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=NGijFZlVksxD-F7vFd6t-OxXQGNBPltCenOKEXruLt_qJFT1S9OLKQZZoGP9h1DtCiSKlGXue93QrVUiDMwcGdyh2TrRG-14rswC6Pee4gDBp0M4e_IARQwBKi2WacbO8L2wax81tu3hUgjSzMk8_meO66nLm0q6fBP8_b7fsKltgGlfqScnrzNTRXpAhTnOjbxYoNPhmd4PpUUP3vKbH0C08XhBczkFPlc7e3TDUOhwHCpo0Tp05NcjXS7qDZg2wes3lGrAjlHdHmiAWx98rDNCBnXpZawNL3T66mjGaVQvnAlTxXy3d1OvUZ4dPAAmgIkaHFaZ2VN_uVxCwz4xZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدون شک این یکی از عجیب‌ترین پرونده های فساد توی تاریخ ورزش کشوره!
یه خانم با تیمای بزرگ فوتبال مملکت قرارداد می‌بسته و می‌گفته بهم پول بدین، منم در ازاش با داور سکس میکنم تا نتیجه رو به نفع شما بگیره!
بعد از دستگیری، این خانم اعتراف کرده که با بیش از ۴۰ داور سکس داشته و باعث صعود خیلی از تیما شده!
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72873" target="_blank">📅 09:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72872">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da58b38a06.mp4?token=RTC-pLURM-axZJlU5vJN9iZKJp65QMRK7Hn2efqG62AFGvFOI_AaJNf7zyOdQXes_ilORAKyj8v0TPU15QBKGlE6wIivbznxIv-MIHulUkp4H2jdrjyRvq25eGLl1PznmAjRyDK5WU-WKbFUwn9EF1Jzj1W1kDRUUW6MVGVjByE2KH1HoFFwoKax_TWSBkMePnnNRlILD_zUMjWk8Ajkt2iTyGrotFMJAB-rOEBXz7boJjDqgWa7ITKs8QwJJUtUbecp92PHaLg4sXa76cRFoDyQIGd-5L_bQT453WFLNwN3JV4MS0JsZwQ1zss9GZwfRLbDx5VWi2jmuTqT6NVEyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da58b38a06.mp4?token=RTC-pLURM-axZJlU5vJN9iZKJp65QMRK7Hn2efqG62AFGvFOI_AaJNf7zyOdQXes_ilORAKyj8v0TPU15QBKGlE6wIivbznxIv-MIHulUkp4H2jdrjyRvq25eGLl1PznmAjRyDK5WU-WKbFUwn9EF1Jzj1W1kDRUUW6MVGVjByE2KH1HoFFwoKax_TWSBkMePnnNRlILD_zUMjWk8Ajkt2iTyGrotFMJAB-rOEBXz7boJjDqgWa7ITKs8QwJJUtUbecp92PHaLg4sXa76cRFoDyQIGd-5L_bQT453WFLNwN3JV4MS0JsZwQ1zss9GZwfRLbDx5VWi2jmuTqT6NVEyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همتی رئیس بانک مرکزی:
حداقل شش ماه اول امسال، عمده کارهایی که کردیم این بود که دو تا موضوع مهم رو به نتیجه برسونیم؛
یکی کنترل تورم، چون به‌خاطر رشد نقدینگی و فشارهای ناشی از دو جنگ پشت سر هم، نقدینگی شتاب بیشتری گرفته بود.
دوم هم اینکه توی این شرایط بتونیم کالاهای اساسی، دارو، معیشت مردم و مواد اولیه کارخونه‌ها رو تأمین کنیم.
این دوتا استراتژی اصلی بانک مرکزی بوده و خوشبختانه بخشی از اقداماتمون هم به نتیجه رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72872" target="_blank">📅 09:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72871">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اینم شیرینی مدیر به شما عزیزان
😁
امشب سه شنبه تاریخ 1405/07/14 به مناسبت تولد دخترم آیلین خانوم
♥️
از الان  تا ساعت 10:00 صبح لینک کانال vip طلا و ارز یارا را #رایگان کردیم برای 100 نفر اول
👇
꧁༒VIP CHANEL  GOLD༒꧂
🔞
ولی اینو بگم شرعا راضی نیستم جایی بفرستید…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72871" target="_blank">📅 01:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72869">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اینم شیرینی مدیر به شما عزیزان
😁
امشب سه شنبه تاریخ 1405/07/14 به مناسبت تولد دخترم آیلین خانوم
♥️
از الان  تا ساعت 10:00 صبح لینک کانال vip طلا و ارز یارا را
#رایگان
کردیم برای 100 نفر اول
👇
꧁༒
VIP CHANEL  GOLD
༒꧂
🔞
ولی اینو بگم شرعا راضی نیستم جایی بفرستید
لطفا رعایت کنید تا حق خودتون ضایع نشه
🙏
چون عضویت فقط برای 100 نفر بازه
هرکس سود کرد دخترم و همسرم رو دعا کنه
❤️
🙏</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72869" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72868">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72868" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72867">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D8msiXaH2pc_mqqB-VNg0ukVUr3BVQLmaJ1TDmyL4KEnQPL8aAkhppzuqcs-_5GDdg_xL23C-9GdEF13BHiNjbzPzSr-guRjge2w4A2iRc1YUB2KO2g7hXjHypqtLAGoH5b3zyA0V0cuzNTGjmQdxVaNHdVJnwz7Fr5pwqh8f5BKAzty_6zhqdRBkRgTETerZgGu1z7laiRLt10jpCfLrHB8wTsHrhFaLgTBFNnJZpfI8rcSBlkUp9VdgwdTwoNeIjsS32ox0o5vzQN_EjSYaPVO2iHHVDPNBICXPI4D4fHGfsrgrnwLw3CukOrscywK7liAKuzwAb3lIpF5lv8SUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72867" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72866">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIeEFIYo4XZMUcOKgbZJI-fEju6LfQRNY7wfPXMaYrx5aDNjrYWQG3A705jW483HPwQsqEd_criU5_KWL2r3-G9xKe43oIInlTcaRJue7SRk-vqJNSXv7HK-nlJYHhfm58VjTISj_R_8wq6aBF_BC4Y9sCY7u5y1coMnsGvXWEjv0w-r8c4PX3tq1igQeYbVHIY4J94-H7Fdpa4vRkkE-VXuT7aKnnjJzDdf5BHM5-_lmuk4CL3huUFxMvGyUvEI8BUVprUWMjwfljNkawHaA89mPdA3MCg54PA5VJitJBKzpkzwWP2Z2XkTw3skoFRE3vZG41exC0LZKXeEHXN6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسنت وزیر خزانه‌داری آمریکا:
«ایران یه وزیر نفت جدید داره.
با توجه به اینکه ایران از ۲۵ اوت حتی یه بشکه نفت خام هم روی هیچ کشتی‌ای بارگیری نکرده، این وزیر نفت دقیقاً قراره چی رو مدیریت کنه؟»
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72866" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72865">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c65f0143c.mp4?token=BcRlHUHfdd-HVcwfBc5RcuZXgjX2H5mvgCwItgz_hp869jFSt4to3hvdaK0tuSveSx7aiquCgXdya37dV7kJns5KiWxkDS4ddWzTLL5CncweyS0xgkKHL-l7SVwj-v0fQEAkCPWmmQ8zpJhZ06JLFoyBp8kUfocjKA6ex9QAV7AKb3nCKf_Y20lHXS1u4S8i-gG_W6Iij052H2eVXI1MyGguwOKUKgUHRmzREPA4EkU-8QWsKk0JRPrgzt9Ckfh1HhYc_U3L8dHjNBqW1KbAovCx49_jVV-5IhXA35QXd5-LOIhbOx48sGU3nhH_IzrOSXyGOqAXEz7HpRGsIbGjdjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c65f0143c.mp4?token=BcRlHUHfdd-HVcwfBc5RcuZXgjX2H5mvgCwItgz_hp869jFSt4to3hvdaK0tuSveSx7aiquCgXdya37dV7kJns5KiWxkDS4ddWzTLL5CncweyS0xgkKHL-l7SVwj-v0fQEAkCPWmmQ8zpJhZ06JLFoyBp8kUfocjKA6ex9QAV7AKb3nCKf_Y20lHXS1u4S8i-gG_W6Iij052H2eVXI1MyGguwOKUKgUHRmzREPA4EkU-8QWsKk0JRPrgzt9Ckfh1HhYc_U3L8dHjNBqW1KbAovCx49_jVV-5IhXA35QXd5-LOIhbOx48sGU3nhH_IzrOSXyGOqAXEz7HpRGsIbGjdjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: درباره طاعون در روسیه، با پوتین صحبت کردید؟
ترامپ: «به‌زودی یه تماس باهاش دارم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72865" target="_blank">📅 00:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72864">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f6433023f.mp4?token=mkNTs0ZuV88riZi8LsFJ4tbK3W4GPci8DjT1nVWou9QzsBe3tnEVroczEQVxNmRDjmsLHbk61BSCeoEZMMkv3jQDk9M4G4qeQKt0D0jI0NlGxZQXFzsafNApy4uBBT_j8JGqJ6KP0cbL1S9MXjeq4bPIg7xRDkFnpZuuitAMl6Jq_UVkCZ_LiVVeI8Ci713ZzaKXpKXkgOrw7T6KPj1yZ2_CjX7tLLczd5uI5YPZBdoid500glU-Ur4yebMXhVNDN0Y4UmMb2B8R34ZKMAF6EKDZaXnSeUcrbi8fsJfth-0sQzt7wQz4DhLXmmEYmkzhRYNWo0KqtIAef-LNK75kgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f6433023f.mp4?token=mkNTs0ZuV88riZi8LsFJ4tbK3W4GPci8DjT1nVWou9QzsBe3tnEVroczEQVxNmRDjmsLHbk61BSCeoEZMMkv3jQDk9M4G4qeQKt0D0jI0NlGxZQXFzsafNApy4uBBT_j8JGqJ6KP0cbL1S9MXjeq4bPIg7xRDkFnpZuuitAMl6Jq_UVkCZ_LiVVeI8Ci713ZzaKXpKXkgOrw7T6KPj1yZ2_CjX7tLLczd5uI5YPZBdoid500glU-Ur4yebMXhVNDN0Y4UmMb2B8R34ZKMAF6EKDZaXnSeUcrbi8fsJfth-0sQzt7wQz4DhLXmmEYmkzhRYNWo0KqtIAef-LNK75kgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«می‌گن: اوه، ما شش ماهه که درگیر ایرانیم!
ما عملاً همون لحظه‌ای که بمب‌افکن‌های B-2 حمله کردن، کار رو تموم کردیم؛ چون با اون حمله، برنامه هسته‌ای‌شون دیگه تموم شد و ۹۵ درصد دلیل این کار همین بود؛ شاید حتی ۱۰۰ درصدش.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72864" target="_blank">📅 00:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72863">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50efa3f342.mp4?token=OfIIPpASaQAuGIOFuauBgNEvw8fIXYZlv5AzimIeiXluZfnzpBU2rLWZwGIlDcg8y3KPUSZrCrASW_uWeaKkY0uZau50mJ9MCotOgDCRRbVblTvp6Lrbfvmof625mdg3Ia8penVp58dQXy-xxTsHboFEDHCW81XElNKv54OVgZqImjbR-X-xAqsUmM2tMIf9qsfr-qUxvxpNY6s6dGqVC2kU-fH4Nyi-PLyGIf0UACobBo1fcS2sghHdCQT59eZuscxJRlY_fldO5JMM7316M4UlyZLqHPVej6kTK3692nypqk8xKLbWyu7XFKQ_O34a2NHNl1YyiOvoVKRYHL1-gGoPSqMrESLY7kgxcvaIdFBAepin8jxfOKJetQD0Aqff_gp9Fn1VhYBrKkOxSFVgj8coQQWSJfbz2Tjqptw8lGlClykK1pKMMEyCCl7NwsqsjsN3OMelLg9pZL8ks1WUM7a-pnoUDq_K13EDk0WPMECdIV7P69Ky0hNeqDNc6FNBHvbr_dZ9vfgMHOflPQ_YIgnAUMw9T0eJ_ZRyBiyL_mi81MWSpFy-hvzaOQka2GDZHkEghfPLduuptmv42YbkR8rtZ2YNi5HMCzbBc7r-a_X_U_NxhgB790Qps9Nhbyjd8Fm5d6udtUmA72oqgg2JuepNU5vQu5-YlPvAJg1ZfRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50efa3f342.mp4?token=OfIIPpASaQAuGIOFuauBgNEvw8fIXYZlv5AzimIeiXluZfnzpBU2rLWZwGIlDcg8y3KPUSZrCrASW_uWeaKkY0uZau50mJ9MCotOgDCRRbVblTvp6Lrbfvmof625mdg3Ia8penVp58dQXy-xxTsHboFEDHCW81XElNKv54OVgZqImjbR-X-xAqsUmM2tMIf9qsfr-qUxvxpNY6s6dGqVC2kU-fH4Nyi-PLyGIf0UACobBo1fcS2sghHdCQT59eZuscxJRlY_fldO5JMM7316M4UlyZLqHPVej6kTK3692nypqk8xKLbWyu7XFKQ_O34a2NHNl1YyiOvoVKRYHL1-gGoPSqMrESLY7kgxcvaIdFBAepin8jxfOKJetQD0Aqff_gp9Fn1VhYBrKkOxSFVgj8coQQWSJfbz2Tjqptw8lGlClykK1pKMMEyCCl7NwsqsjsN3OMelLg9pZL8ks1WUM7a-pnoUDq_K13EDk0WPMECdIV7P69Ky0hNeqDNc6FNBHvbr_dZ9vfgMHOflPQ_YIgnAUMw9T0eJ_ZRyBiyL_mi81MWSpFy-hvzaOQka2GDZHkEghfPLduuptmv42YbkR8rtZ2YNi5HMCzbBc7r-a_X_U_NxhgB790Qps9Nhbyjd8Fm5d6udtUmA72oqgg2JuepNU5vQu5-YlPvAJg1ZfRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«نیروی دریایی آمریکا یکی از مؤثرترین و نفوذناپذیرترین محاصره‌های دریایی تاریخ رو اجرا کرده. هیچ‌کس تا حالا همچین محاصره‌ای ندیده؛ حتی یه کشتی هم نمی‌تونه وارد بشه.
اگه کشتی نفت داشته باشه، به کابینش یا سکانش می‌زنیم؛ اگه هم نفت نداشته باشه، کلاً غرقش می‌کنیم.
الان محموله‌های نفتی که از خارج ایران ارسال می‌شن، تقریباً دوباره به بالاترین سطح خودشون برگشتن.
یعنی به زبان ساده، تنگه هرمز متعلق به نیروی دریایی آمریکا و ایالات متحده‌ست؛ جای واقعی تنگه هرمز هم همینه.»
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72863" target="_blank">📅 00:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72862">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52bb6008cb.mp4?token=BNDxnlkHW9GZuH743iwTcw6Ph4IOtk_WQbyzr_XHjUd4bUCEpVGnZRO_TC1QH9mySkcDxVh0Y1jvyGXMmhFvTIYe_VolL9ti4oE_S1wtjjtDeVgCXKZ1bsuT11RZHYDprNVi-MyXbJllgRJ5b05HPN9bwyEBTfL1vSblt3dleiH26ShwSvHzSqlilTnDEtxjqGOFgXzNgaZFVTGM3pPm-AN-NpKVVGT4Z6Un2tOZIbbZnACrAuR3AY1dWQpyQBDwhzmB4Y8KEQ3k10aIrCTtkPne3oZa9KEsq5Nur7FSxKjzF2m1K-oZSSVWbz7Egzmq-BdmisedxQIgPTCByU6734DlRfLtOYKKMwpY9qyHHw-ZFPuRIBXzbUM7hN-5PGS7Ob2XC8wGU90qzCbJ0YfpYP-R3hTc-U7qRJDhLBbnMTXnaApDSFb4T5RJaWi1Myynbggoop1PAfoaOFDCxLbBnA3m8X4F0EblE54Py4QI4G0KJXOocmsgC4Pw2TEG3S7aEwHDVjUAP0Xj8IsYspIUuMbmoBHHcaF6CAgD2Z6jPtv5czsBN47ubnwl3fh0RBQpXeC-sIxas51qV3whThXjM2G_QhWXciKAlpLnZzP405OSyABME9XXg7MNzmBLdReC_rejreNNZE04_v87dSZ_egREBoY4a8eYy5K60bHrzG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52bb6008cb.mp4?token=BNDxnlkHW9GZuH743iwTcw6Ph4IOtk_WQbyzr_XHjUd4bUCEpVGnZRO_TC1QH9mySkcDxVh0Y1jvyGXMmhFvTIYe_VolL9ti4oE_S1wtjjtDeVgCXKZ1bsuT11RZHYDprNVi-MyXbJllgRJ5b05HPN9bwyEBTfL1vSblt3dleiH26ShwSvHzSqlilTnDEtxjqGOFgXzNgaZFVTGM3pPm-AN-NpKVVGT4Z6Un2tOZIbbZnACrAuR3AY1dWQpyQBDwhzmB4Y8KEQ3k10aIrCTtkPne3oZa9KEsq5Nur7FSxKjzF2m1K-oZSSVWbz7Egzmq-BdmisedxQIgPTCByU6734DlRfLtOYKKMwpY9qyHHw-ZFPuRIBXzbUM7hN-5PGS7Ob2XC8wGU90qzCbJ0YfpYP-R3hTc-U7qRJDhLBbnMTXnaApDSFb4T5RJaWi1Myynbggoop1PAfoaOFDCxLbBnA3m8X4F0EblE54Py4QI4G0KJXOocmsgC4Pw2TEG3S7aEwHDVjUAP0Xj8IsYspIUuMbmoBHHcaF6CAgD2Z6jPtv5czsBN47ubnwl3fh0RBQpXeC-sIxas51qV3whThXjM2G_QhWXciKAlpLnZzP405OSyABME9XXg7MNzmBLdReC_rejreNNZE04_v87dSZ_egREBoY4a8eYy5K60bHrzG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«من مدام از رهبران کشورهای مختلف دنیا تماس می‌گیرم که بابت جنگ ایران ازم تشکر می‌کنن.
منم بهشون گفتم: خب، خوبه! کی قراره پولش رو بدید؟
ما داریم بارِ کل دنیا رو روی دوشمون می‌کشیم. اتفاقاً از این کار هم خوشحالیم، چون خودمون قوی‌تر شدیم و بقیه ضعیف‌تر.
اونا دیگه ضعیف شدن؛ دیگه کارایی سابق رو ندارن. ما داریم کارهایی می‌کنیم که هیچ کشور دیگه‌ای از پسش برنمی‌اومد.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72862" target="_blank">📅 00:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72861">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ درباره ایران:
«ایران یه کشور شکست‌خورده‌ست. همه دارن کنار می‌کشن و می‌رن. اقتصادشون هم عملاً به خاک سیاه نشسته.
وزیر نفت ایران هم گفته: «من دارم می‌رم، چون کشورمون دیگه تمومه.» خودش دقیقاً همینو گفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72861" target="_blank">📅 00:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72860">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24dabc9ec.mp4?token=W5vz-OHhmXQ4iMTHSlPS9JIAZC7jKyODBGI7Nu5R0hs8uaiC3Hok0gRWaKhZXQG_p4Yzn7UeQYGo9R8p8nE25BYpXfE19TpWd3BeXgcRLNkB-UaUVo6q1rHsX3erFUD8rKh1uSe-_gNlzfi6lRCYW4Yfaw6Jv-1WARGRyH9zBO6dpOHX6gm0jIHTQkk4vV2J8bg00Yfw0hDO1ROYGUTsWRvB-X0T70BBsAy0WemaEwOE8AA9TalQJMGpXcUhDlaRiR_1rbbBvnnv2QF3rAHZhRCXvsR6fNkinqAlWyQG8kklQtS3kewSEedTFPVDiJs2fIOPSFUMdpMu_Vok4NwI3bH-l4hQ5657mBStv3NcnowDkfQlQBAFZAISHTS544BQ_ZVip6GiZdE-Yj63vSQtBra4-Uk64d7IX7NjuQugTAk14wfHdsdjCTDpvuUhvLGkyFrLKMp0kTSXKDDsqX65mnz86VXGTICBuHNHw9MxaIwamPDLM7J2dusI8DkSqSGQyP5mcqLl-m8tIh5pL3ahrLJnJ0PIm8WFb59peD0Z9KAjhgKWaALOkfP8D5-xeuZhsGMINNIljNSdyv_3_wNJfN0DMnjF3z3nWSXlXDRRo9okvnfDtmQON7cBFwv3y9khwx3TmBBd_DmNQoZSbnczrGTygy6ifZ1m7aexLZYwPKU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24dabc9ec.mp4?token=W5vz-OHhmXQ4iMTHSlPS9JIAZC7jKyODBGI7Nu5R0hs8uaiC3Hok0gRWaKhZXQG_p4Yzn7UeQYGo9R8p8nE25BYpXfE19TpWd3BeXgcRLNkB-UaUVo6q1rHsX3erFUD8rKh1uSe-_gNlzfi6lRCYW4Yfaw6Jv-1WARGRyH9zBO6dpOHX6gm0jIHTQkk4vV2J8bg00Yfw0hDO1ROYGUTsWRvB-X0T70BBsAy0WemaEwOE8AA9TalQJMGpXcUhDlaRiR_1rbbBvnnv2QF3rAHZhRCXvsR6fNkinqAlWyQG8kklQtS3kewSEedTFPVDiJs2fIOPSFUMdpMu_Vok4NwI3bH-l4hQ5657mBStv3NcnowDkfQlQBAFZAISHTS544BQ_ZVip6GiZdE-Yj63vSQtBra4-Uk64d7IX7NjuQugTAk14wfHdsdjCTDpvuUhvLGkyFrLKMp0kTSXKDDsqX65mnz86VXGTICBuHNHw9MxaIwamPDLM7J2dusI8DkSqSGQyP5mcqLl-m8tIh5pL3ahrLJnJ0PIm8WFb59peD0Z9KAjhgKWaALOkfP8D5-xeuZhsGMINNIljNSdyv_3_wNJfN0DMnjF3z3nWSXlXDRRo9okvnfDtmQON7cBFwv3y9khwx3TmBBd_DmNQoZSbnczrGTygy6ifZ1m7aexLZYwPKU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ درباره ایران:
«ما توی جمهوری اسلامی ایران داریم خیلی خوب پیش می‌ریم. کل اونجا دیگه داغون شده.
باید کار رو تموم کنیم؛ فقط مونده تصمیم بگیریم چطوری تمومش کنیم: با راه خوب و دوستانه، یا یه راه نه‌چندان خوب!
خیلی زود می‌فهمید قراره کدوم راه رو انتخاب کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72860" target="_blank">📅 00:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72859">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423715c427.mp4?token=TphYCMJ8YbBumCIukl0cVF6ZCFkfWaym2-H-QYDwNuir5gvhq5oZkcNmZo-NW6oj0VLjei0AaQ_XR99ct5P6jeqIY2Z6aOGYV08B0aPZOj9Sjz-LGbv0K2uUEPJzvL_ebD-A9hxetFTcj1jku81FyU9RBzYfgbagJhA-dlIPFMN3U3OzXYtOMwgf7iTPWk2B5MkQT2fybio9peev7CBxS2san0MELCS2R75toNj5SbAP0gKk7ijuxAh7AQgyXnMkv8eNtuttbNBK2e1qj58TtpKluu5JvbNFFpTnAhnFPrazq_UNfN_WgDZL7xLc2v-yfSYB2xVEfdA2-oPdN7KvgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423715c427.mp4?token=TphYCMJ8YbBumCIukl0cVF6ZCFkfWaym2-H-QYDwNuir5gvhq5oZkcNmZo-NW6oj0VLjei0AaQ_XR99ct5P6jeqIY2Z6aOGYV08B0aPZOj9Sjz-LGbv0K2uUEPJzvL_ebD-A9hxetFTcj1jku81FyU9RBzYfgbagJhA-dlIPFMN3U3OzXYtOMwgf7iTPWk2B5MkQT2fybio9peev7CBxS2san0MELCS2R75toNj5SbAP0gKk7ijuxAh7AQgyXnMkv8eNtuttbNBK2e1qj58TtpKluu5JvbNFFpTnAhnFPrazq_UNfN_WgDZL7xLc2v-yfSYB2xVEfdA2-oPdN7KvgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«یادتونه خمینی رو؟ همه‌شون دیگه نیستن؛ همشون رفتن.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72859" target="_blank">📅 00:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72858">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/484ca32fc4.mp4?token=aLb7I3TsYay_2cITGsvb-ExBN6NqlA-nJCwCT4B9e576mEEVPC6QTkKGR7lOzi7JWKKtvlxk89q2neO5sjIvz4iG5JriVAe4XKVm9K2O5w-hcpPxO1fqxrj298IkNvJvRsehjngwgJZlELs69kWXGflbVH8qyzlTAbPAGQLtToPNg_pM3eG2Yb89AAjCRx6s8qG-_FGva5DSvWozvEyCn_Z3D23VxE5Q_YY2irioP1JoEWcbLakN2gZJzN0xs9TQ0kUD-WWkq11UrJ2FcH3KrA5tOv-BXUlb3-7nSzbeowF9LCw9vAvEEqxn2PyAUjFQvhnPLlT8nYTB7zaJXU7KDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/484ca32fc4.mp4?token=aLb7I3TsYay_2cITGsvb-ExBN6NqlA-nJCwCT4B9e576mEEVPC6QTkKGR7lOzi7JWKKtvlxk89q2neO5sjIvz4iG5JriVAe4XKVm9K2O5w-hcpPxO1fqxrj298IkNvJvRsehjngwgJZlELs69kWXGflbVH8qyzlTAbPAGQLtToPNg_pM3eG2Yb89AAjCRx6s8qG-_FGva5DSvWozvEyCn_Z3D23VxE5Q_YY2irioP1JoEWcbLakN2gZJzN0xs9TQ0kUD-WWkq11UrJ2FcH3KrA5tOv-BXUlb3-7nSzbeowF9LCw9vAvEEqxn2PyAUjFQvhnPLlT8nYTB7zaJXU7KDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛پرزیدنت ترامپ درباره ایران:
«ده‌ها نفر از سران تروریستی ایران رو از هستی ساقط کردن و مستقیم فرستادن اون‌ور، پشت دروازه‌های جهنم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72858" target="_blank">📅 00:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72857">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da78ea97a3.mp4?token=pjkCdovpYgu0U1vsZ8CU7GacL08uFUEKXgZ-Q1pO2CSgdbej8KO6EhJvi2sUhkUdrywMKf_QX0mN1xHc4KvmWABfj8V9A7tiNh43B-KlvaGk7pb3zv2zyn33yNHTaVf3eU53Al9pCzC-wbipahjkjKo_xRa1ryqXtoT9DYpS60UE_mbNDIc5yz5SlX0-bt6YiGAEQkRn_VtdDFwda2wWOq_0ifutFXwB2EWZAE0IJLQMGfB-UpQpSqqB_m9th2VQ7zCdtjVjYIJyl6wbsrNz7V3sgbfAQxkpNoCISOoOF-UNidoQMa1lpSMuCi7ZZTgZ-6OlpfvTeDZ1wEq91d2Vwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da78ea97a3.mp4?token=pjkCdovpYgu0U1vsZ8CU7GacL08uFUEKXgZ-Q1pO2CSgdbej8KO6EhJvi2sUhkUdrywMKf_QX0mN1xHc4KvmWABfj8V9A7tiNh43B-KlvaGk7pb3zv2zyn33yNHTaVf3eU53Al9pCzC-wbipahjkjKo_xRa1ryqXtoT9DYpS60UE_mbNDIc5yz5SlX0-bt6YiGAEQkRn_VtdDFwda2wWOq_0ifutFXwB2EWZAE0IJLQMGfB-UpQpSqqB_m9th2VQ7zCdtjVjYIJyl6wbsrNz7V3sgbfAQxkpNoCISOoOF-UNidoQMa1lpSMuCi7ZZTgZ-6OlpfvTeDZ1wEq91d2Vwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری؛محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی، استعفا داد.  @News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72857" target="_blank">📅 00:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72852">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Shatel-VPN.apk</div>
  <div class="tg-doc-extra">58.4 MB</div>
</div>
<a href="https://t.me/news_hut/72852" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فیلترشکن شاتل
🔥
✅️
تازه نفس
✅️
تست شده رو همه‌ی نت ها
نصب از گوگل پلی</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72852" target="_blank">📅 00:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72848">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y_Xn8h8nmGf9Rx8gzfabt4fkFeh6JDboKAylzpycBv_P60nlv6TalcbosVmuTbUGIs13c9OR7IvusFr2lU_hTQWjoH0PTuLqYlxuNMuBNFLGHQbr6mxKo6N7HKSC-4KEDndKy9tvH7yAOYS3IoKHvBdqjBUywLb7zC_3nJLxXb-oEg7Zqn4l-XuNAmRs04NowaykcKN9YbJwnHCnLm8kVoMPOLzOUcDdAoc3TrCAnEL_CCaGBEepKJwR3nqaBG8oD7f_mQSUj0gU38K0vQxxOa7mtO231ThOtoF94r5oCqPiQflfo6zifqPQ0fRkBq2I1M4P5J9-YG-1IUbawF0YXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vKvTcHlttRxvFOWu3Bg0j_8vSZ3UTy9F4VtMGxjvXmHB-x9QfBPgOUb0q7xzSXMZ1U1Myr-DDtSAKVfubxp8QJ4Sq01GBWaO3UpTpCTVUk8Q4HtP6rjQGjdHDRTs7-jifXeYRCyjBWzk2eAPotOeZj5tMusJA4wFgHxAIfjkMC24wqQht5pmRMnzSbXut-hIwCj0pKnMEHjdptadbdWYKRMNQoWPHHiV-dtf-MG85Bw8XRAMdEDfv2OoOjC-scF9OHD0hQ-B4rsTYW7EgzswVDLwxeJf35qWH6uTy6i6Ga7DpoAqIKYb1wPXKvrWeB79qCW4_7_adhU-jUi7Qm9WVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6fa9e6973c.mp4?token=WTGshpO1xdO_KPBltTy43c0TKylAFYP5mUzTAyQyggqvi6Xh9-_Kj3BOX_6_q7Hc7x85TetrRdzTgKIOybIquUB5tbWL6Y3qBcwHYZT5Eu2esXUa47QLO6ZN69kpheXOCCtRYD9zDNAbM2ytzpmYKLL1kMdE09mVy9KBMSj_NuIqWszweQd4ov-lohh2WqhzEIs6UJlUkZoJnBYfi96smGERj66u5LA67tN9wP2wBOYKwL5W08Xia-tMiKODJmY5d9Y1ifFTA51LuJ86T-ohAdcJdsUr500a8ATrIPZqJmjz6OOxTeoJmfnBNraDOgtuGg6UkX87M9l7QUlqy3GBTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6fa9e6973c.mp4?token=WTGshpO1xdO_KPBltTy43c0TKylAFYP5mUzTAyQyggqvi6Xh9-_Kj3BOX_6_q7Hc7x85TetrRdzTgKIOybIquUB5tbWL6Y3qBcwHYZT5Eu2esXUa47QLO6ZN69kpheXOCCtRYD9zDNAbM2ytzpmYKLL1kMdE09mVy9KBMSj_NuIqWszweQd4ov-lohh2WqhzEIs6UJlUkZoJnBYfi96smGERj66u5LA67tN9wP2wBOYKwL5W08Xia-tMiKODJmY5d9Y1ifFTA51LuJ86T-ohAdcJdsUr500a8ATrIPZqJmjz6OOxTeoJmfnBNraDOgtuGg6UkX87M9l7QUlqy3GBTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا صرافی ایرانیه «omp finix» که دارای امتیاز رسمی و تایید شده هم هست، پول مردم رو بالا کشید و ۳ ماهه درخواست تسویه حساب مردم رو پرداخت نکرده.
مردم هم مقابل قوه قضائیه دست به اعتراضات زدن و خواستار تعیین تکلیف و پرداخت پولشون شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72848" target="_blank">📅 23:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72847">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bd2fd9d91.mov?token=WHcv61QivLBR1PIt23AsiYigHTb3URe7YxrN1xgpgXZnjJEbgnbNu0ZVMGXCacOPbu6JuToaNHxF8LdgcOaOHPq8rZgVYnpQ08i44whIAW9dwJqPEw7p4IfRdNhMpQS2eiqesmzZiS7DEGcs6F1RZlg8QaC38-HoT3UfZauXkCW5mqNwLd1MbEz67UzqfNgKy1jw2gw9KuG_ecOLYxQow91kNpvZWvCW-mQY9pE40t8MYk6YmN4roYKTmv-i6wjjmzEt-INbHENFSmz97TxO6g7rs9aW6zBhXF2KBAy5EjRJu8G0tq5EM0K0heN6fmozDm_anrlgkXJzu7G2b1ZFtAPfn-8eHkKT9sI0-J1Jyhx89oEAPxoXHfopbLPUobkAQiYJjX_YzRMXEeD2gbnekoshXi7yRWDvDKpGXH-JYKPrb9XE_EazebeEgRKaPeUdZYIJfVPm7cWe2GSoecm93EAnGTIDMmGyc9yvy3QpdFDN5_pZ7PEYoBdXZDVMJhbbIkXu1h5NwYnWiqfYqDum6_LNm4hRLnH0yYaf39ohS_UERwfx_p-bkOfTmk8hQyrBnQMpb3IF8d0XPwioo-tLEz5aU0iACF6jSEpqxv8Dm1Fcnex3SzosDVt7Vbla7HLGysbbGqskeYq57YwjMvdaV1tk7IQ1E9scu5dfOTH3Umc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bd2fd9d91.mov?token=WHcv61QivLBR1PIt23AsiYigHTb3URe7YxrN1xgpgXZnjJEbgnbNu0ZVMGXCacOPbu6JuToaNHxF8LdgcOaOHPq8rZgVYnpQ08i44whIAW9dwJqPEw7p4IfRdNhMpQS2eiqesmzZiS7DEGcs6F1RZlg8QaC38-HoT3UfZauXkCW5mqNwLd1MbEz67UzqfNgKy1jw2gw9KuG_ecOLYxQow91kNpvZWvCW-mQY9pE40t8MYk6YmN4roYKTmv-i6wjjmzEt-INbHENFSmz97TxO6g7rs9aW6zBhXF2KBAy5EjRJu8G0tq5EM0K0heN6fmozDm_anrlgkXJzu7G2b1ZFtAPfn-8eHkKT9sI0-J1Jyhx89oEAPxoXHfopbLPUobkAQiYJjX_YzRMXEeD2gbnekoshXi7yRWDvDKpGXH-JYKPrb9XE_EazebeEgRKaPeUdZYIJfVPm7cWe2GSoecm93EAnGTIDMmGyc9yvy3QpdFDN5_pZ7PEYoBdXZDVMJhbbIkXu1h5NwYnWiqfYqDum6_LNm4hRLnH0yYaf39ohS_UERwfx_p-bkOfTmk8hQyrBnQMpb3IF8d0XPwioo-tLEz5aU0iACF6jSEpqxv8Dm1Fcnex3SzosDVt7Vbla7HLGysbbGqskeYq57YwjMvdaV1tk7IQ1E9scu5dfOTH3Umc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار رحیمی: از امروز اگه یک سایت یا رسانه قیمت ارز (مثل دلار و یورو) رو منتشر کنه با اون سایت برخورد قانونی میشه.
جدی‌جدی اینا فکر می‌کنن با پاک کردن صورت مسئله، اصل مسئله هم پاک می‌شه!
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72847" target="_blank">📅 23:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72844">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c58dc98573.mp4?token=CEFtQg04WX9yCDYvEVBvfuYlFAgHb3FXi-TV-_9C6cgGJZcl7uZeJOiFzx8cg61RWvM9YmkqGm197fZO166hVX2fZHx8DAk_K7UpK0zv3lgKOzun9ZzFAWeAFy4P1RXTub9E7H7JGrbWzoANXC1W_V1twS5ntKzzobD5xm5Y2TMDcTZLI9VRMGshm1BuGVpK-D1nacKYIt2uONBfhtpC20FNgEAgdiQeb5WWfhM4SW6xzEgWDCe9FxesGDR20ZXo56Ip4LjOAkNzeOMhii8hbkamZKNl3z0hKdzwA0_yP4W_BlsFXEUmgKoVbjmbR_BdcQxVqE6Et2akdSqKToH_Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c58dc98573.mp4?token=CEFtQg04WX9yCDYvEVBvfuYlFAgHb3FXi-TV-_9C6cgGJZcl7uZeJOiFzx8cg61RWvM9YmkqGm197fZO166hVX2fZHx8DAk_K7UpK0zv3lgKOzun9ZzFAWeAFy4P1RXTub9E7H7JGrbWzoANXC1W_V1twS5ntKzzobD5xm5Y2TMDcTZLI9VRMGshm1BuGVpK-D1nacKYIt2uONBfhtpC20FNgEAgdiQeb5WWfhM4SW6xzEgWDCe9FxesGDR20ZXo56Ip4LjOAkNzeOMhii8hbkamZKNl3z0hKdzwA0_yP4W_BlsFXEUmgKoVbjmbR_BdcQxVqE6Et2akdSqKToH_Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی بزرگ توی آب‌های نزدیک سوچی
امشب یه آتش‌سوزی گسترده توی آب‌های نزدیک سوچی روسیه راه افتاده؛
توی ویدئوها یه خط طولانی از آتیش و یه ستون خیلی بزرگ دود سیاه دیده می‌شه که از نقاط مختلف شهر هم قابل مشاهده‌ست.
حساب‌های نزدیک به اوکراین مدعی شدن این نفتکش هدف قرار گرفته، اما منابع روسی فقط گفتن یه شناور نزدیک بندر آتیش گرفته و فعلاً علت حادثه مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72844" target="_blank">📅 22:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72843">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شلیک چندین موشک ضد کشتی به سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72843" target="_blank">📅 21:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72842">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ایران در اعتراض به برخورد دولت فرانسه با اعتراضات دانشجویی و چیزی که «نقض آشکار حقوق بشر» عنوان کرده، سفیر فرانسه در تهران رو احضار کرد!
وزارت خارجه ایران هم از فرانسه خواسته به تعهداتش در زمینه حقوق بشر پایبند باشه و آزادی‌های اساسی، به‌خصوص حق تجمع مسالمت‌آمیز، رو رعایت کنه.
جالبه رژیم جمهوری اسلامی که بویی از حقوق بشر و برخورد مسالمت‌آمیز نبرده میاد به بقیه کشورا برخورد مسالمت آمیز و رعایت حقوق بشر توصیه میکنه!
یه نکته دیگه هم که هست اینه که تا امروز هیچ گزارشی مبنی بر اینکه معترضی در فرانسه کشته شده وجود نداره و گزارش های رسمی که وجود داره نشون میده فقط بیش‌ از ۲۱۵نفر دانش‌آموز و ۸۵کادر آموزشی زخمی شدن.
از نیروهای دولتی هم حدود ۷۱۵ نفر نیروی پلیس و ژاندارم در جریان اعتراضات زخمی شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72842" target="_blank">📅 20:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72841">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8FzSARpgT7VWn8yD9qYpXzI6j5m0XNtQ2l0NFBEdv0MdfWo-MP99XQtAPZjjMbeHtIhqXUYyzTvqnKt7TU5IFlEVgmUqSGU4iNzzlHkpkci5FivHNIjt9yF-4p2Qyj_WnVX2bPTimImYuXneztfP7KKKLSWpXKIVhA5XHHQ8fmcOpVZbvC8g89O2zFdN03DRLlpVpSV3ITKsgzR9VoPA2I0wWahB0B6va8CeXuvByNaVNgnu4oaGhtwscwhN4hL_ragFZd3xIX16rX-nLRCuxknL1DG71GAurCk9teaZWzb3m-uuEmYS9l61oXckK6d1Yd9S2WyQ4pgs0du7xWyag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت خیابان های فرانسه پس از اعتراضات گسترده دانش‌آموزان و دانشجویان به دلیل کمبود معلم و وضعیت بد مدارس</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72841" target="_blank">📅 19:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72840">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">#فوری
؛رایتل رسماً به مزایده گذاشته شد؛ شستا ۱۰۰ درصد سهام این اپراتور را با قیمت پایه ۱۳۰ هزار میلیارد تومان (۱۳۰ همت) برای فروش عرضه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72840" target="_blank">📅 18:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72839">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یه مرد ۲۲ ساله بریتانیایی به اتهام مشکوک بودن به آماده‌سازی اقدامات تروریستی، در ارتباط با پرونده مشکوک پایگاه هوایی RAF Fairford بازداشت شده.
پلیس ضدتروریسم انگلیس گفته این فرد امروز توی وست‌مینستر لندن دستگیر شده و هفتمین نفریه که توی ارتباط با این پرونده بازداشت می‌شه؛ البته تا الان برای هیچ‌کدومشون اتهامی ثبت نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72839" target="_blank">📅 18:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72838">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d2245088c.mp4?token=gX0Kpn7NvpSEJHrPdKJXmsy-BnhftAzISJGulbtuFqDSvmCtktWq4_pDG7-WK54pXp6V8SGrDfRugwpMz0EnGraTSq7FoyrxVLBjvO2yMFxMSfxBrCo6cQ8qCRFIBvdvGjPDKaqTdhjf0BjeNt1ivQ-g3r369zglS2goTBH3epYUWvsNvA9HoVu74JxCgBYcGrwtgIRm-Y8VXSK-Mk6KRH-QHAz0IDp4fPcrK8R8khOx4G9Lr33eKcDPVu3dFVNqRMMwx2di550eW88fq5LN2Aoi7CmV5sHls3ZjRDiAcsVBTVnaHV3UZsPrUANiJ6aqZHpnkS-5Wb4c_v10rQA0B4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d2245088c.mp4?token=gX0Kpn7NvpSEJHrPdKJXmsy-BnhftAzISJGulbtuFqDSvmCtktWq4_pDG7-WK54pXp6V8SGrDfRugwpMz0EnGraTSq7FoyrxVLBjvO2yMFxMSfxBrCo6cQ8qCRFIBvdvGjPDKaqTdhjf0BjeNt1ivQ-g3r369zglS2goTBH3epYUWvsNvA9HoVu74JxCgBYcGrwtgIRm-Y8VXSK-Mk6KRH-QHAz0IDp4fPcrK8R8khOx4G9Lr33eKcDPVu3dFVNqRMMwx2di550eW88fq5LN2Aoi7CmV5sHls3ZjRDiAcsVBTVnaHV3UZsPrUANiJ6aqZHpnkS-5Wb4c_v10rQA0B4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکرون شاهد نخستین شلیک آزمایشی موشک بالستیک جدید M51.3 فرانسه از زیردریایی هسته‌ای «لو ویژیلا» بود.
مکرون:
این آزمایش، اعتبار و قدرت بازدارندگی هسته‌ای فرانسه رو نشون می‌ده:
«برای اینکه آزاد باشی، باید ازت بترسن؛ و برای اینکه ازت بترسن، باید قدرتمند باشی.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72838" target="_blank">📅 18:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72837">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b292f769f.mp4?token=VgZ5MUxk_hXIo8fqBggV8kO1iRgtYhjs9qWN2THUDBtPQjAcMMsiJyuP5Fq3kQR9xiIiIwAz5N4lvSwAoAtwBJOBursE5eIFtlJngjsLGxbK4ocj6lvI-GyoOD4QEsf4HSxgM5kbNanUYiYb32QXfIDL1QG4t-L0H2ZIfB1GjScwOWJUPKlbl9mmDpdCD5RoWH2Mti6thB-DGobg_NuHHrFS9foDNJxWZgdTlRTkw2i9_v8o-g1MEtX2qTWam2YrkpJH4U7SKCs9gSrfAMB-wb5t1WdabbkQYhcm8ENkMBtNnWhXZwXLiGOpqDtIGDZ_RQSkKZBBLyiuBC3WAUAh1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b292f769f.mp4?token=VgZ5MUxk_hXIo8fqBggV8kO1iRgtYhjs9qWN2THUDBtPQjAcMMsiJyuP5Fq3kQR9xiIiIwAz5N4lvSwAoAtwBJOBursE5eIFtlJngjsLGxbK4ocj6lvI-GyoOD4QEsf4HSxgM5kbNanUYiYb32QXfIDL1QG4t-L0H2ZIfB1GjScwOWJUPKlbl9mmDpdCD5RoWH2Mti6thB-DGobg_NuHHrFS9foDNJxWZgdTlRTkw2i9_v8o-g1MEtX2qTWam2YrkpJH4U7SKCs9gSrfAMB-wb5t1WdabbkQYhcm8ENkMBtNnWhXZwXLiGOpqDtIGDZ_RQSkKZBBLyiuBC3WAUAh1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل: هر موقع میرفتم خونه و می‌دیدم کفشای لِه و درب و داغون پشت دره، می‌فهمیدم مجتبی خامنه‌ای اومده :))
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72837" target="_blank">📅 18:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72836">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72836" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72836" target="_blank">📅 18:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72835">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfYG-I13CugFxVa0Ee8taMsQF-S6DC0Usa_LF5cAtmbFZh8ez4YEkf_xdiejN4Q2hDtFI5uMkpvz196ou-ggIx4jRPybvRGo_oD_dMFeC9bqK63f3AKcIxHKxyJa-ChIdThDihLB7k9a6Tgxq2nsyPNSlcqzioF9O3Ci8pxrw1zyyhS0N2oFnPyZuwHY3nuva9vD0vF38hiTh0d27tQwRMSibIwJ4kQh_zsxIwiwwX0FAXaPJftH9-FY9AgTVovagDAZSHpKo9LF2AnSp-KlWnBYO67hOKhCI5r2n9ZaenbJRb4jscVkD5OWFOLI6qmivhmHzZ6rJLBgYrzUdozYYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72835" target="_blank">📅 18:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72834">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مارکو روبیو درباره مورد مشکوک طاعون در روسیه:
«فکر می‌کنم روسیه باید اطلاعات بیشتری رو در اختیار دنیا بذاره. کاری که باید انجام بدن همینه و امیدواریم همین کار رو بکنن.
ما هم داریم موضوع رو خیلی دقیق زیر نظر می‌گیریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72834" target="_blank">📅 17:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72833">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab24bbc88d.mp4?token=FrilJdprhZVu_X9X3GrT5fuiLVvlq56-dykVK5dgxb3oLgQza1LmPxPl_muiogHUeJ2D2d6ODBSxY4BKyy5Hp1-v7V-WOSc5CuZVvwK959zdEvePhb1phVIy6Mw4jnBFoqBgpt1OxGYkchqj4Hk0IrgBY_UKqjEmrqDKjze_QmXDET5_LL6VLcz1Glg7_eRTEddzCA_nEyxLdfez20jQxXmyTTD9CzT9G2x3f_zZzos2uNX_wXHUHp6hMq1n8W8TDrr11vFkpBSngvsQHfqOXhYefslCkM-sNArarBRhPpZpGORCEv75T8uAu0g4EeAk4DFQkYFfiqXKUbSexXA3qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab24bbc88d.mp4?token=FrilJdprhZVu_X9X3GrT5fuiLVvlq56-dykVK5dgxb3oLgQza1LmPxPl_muiogHUeJ2D2d6ODBSxY4BKyy5Hp1-v7V-WOSc5CuZVvwK959zdEvePhb1phVIy6Mw4jnBFoqBgpt1OxGYkchqj4Hk0IrgBY_UKqjEmrqDKjze_QmXDET5_LL6VLcz1Glg7_eRTEddzCA_nEyxLdfez20jQxXmyTTD9CzT9G2x3f_zZzos2uNX_wXHUHp6hMq1n8W8TDrr11vFkpBSngvsQHfqOXhYefslCkM-sNArarBRhPpZpGORCEv75T8uAu0g4EeAk4DFQkYFfiqXKUbSexXA3qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زن بیژن مرتضوی : مردم ایران در دنیای واقعی خیلی خوشحال و شاد هستن ، واکنش ها تو فضای مجازی دروغ هس و حقیقت نداره
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72833" target="_blank">📅 17:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72832">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4be4d4d973.mp4?token=Htpz2ZPCoqflXL_jtZNsI9jAGN1bKsTMHfXxTz5o1CY37pLUKcF4HGX6WIKkSX4eOP7Tfkv197WeALJfcsa8k6-U6pD2U4360biOorpPWzLzJMIQo5hh7wD-htYx4mNhRJLtZPmMeMpyXQ6HljfFzmY5Hi0mX-Oe2n1C2BngWtVZagHZuBNvhVu-SW09GIMkQHrkMMVMmFLg2cm1ZFcBM8pZi1dWipWuXWBSl7h6DpSkfWKajyOKsASSWvStrcVM76MI5qsIlXPRyuWoQ_fl0EoGhEFn1atBGmBqrO5AN2rA_SLsPvMYTWBUXmWyideWva4ZICHVwcb-fxOEs4oJ9DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4be4d4d973.mp4?token=Htpz2ZPCoqflXL_jtZNsI9jAGN1bKsTMHfXxTz5o1CY37pLUKcF4HGX6WIKkSX4eOP7Tfkv197WeALJfcsa8k6-U6pD2U4360biOorpPWzLzJMIQo5hh7wD-htYx4mNhRJLtZPmMeMpyXQ6HljfFzmY5Hi0mX-Oe2n1C2BngWtVZagHZuBNvhVu-SW09GIMkQHrkMMVMmFLg2cm1ZFcBM8pZi1dWipWuXWBSl7h6DpSkfWKajyOKsASSWvStrcVM76MI5qsIlXPRyuWoQ_fl0EoGhEFn1atBGmBqrO5AN2rA_SLsPvMYTWBUXmWyideWva4ZICHVwcb-fxOEs4oJ9DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش چشم بازم تحلیل کرد و گفت جنگ در پیشه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72832" target="_blank">📅 16:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72831">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd2b481530.mp4?token=QzpNqcZiHnmUPA59PiBpqd8S3FAgwvvlymKOPIqN41IXETWfeVEiQxG5Ys1tRztVL-y-4z4kMujxHe3uwsRvaB7LwhLdIZsQm7d78qsbDFzypfjK6mPwXGxUbwfxhkB7wSqj3MGC7aia8EUTAygm6V4RWpFUrZy9NDMEf0z1IedlF0QPmHg4DLXgAimFh4-iPxrafFhPUuSoPwJEeUIN5fhA7sAvI7qb58JQQ_GxOFiNX2oZofL6rxWl8Af4nMrovjFFL21qhieFTI2mk8jAyXjeIpoVp08i3gDWFOocbJn-b9t1sea3QthQc69XSfp1UDy5LhYETqZWxefnkKrJwA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd2b481530.mp4?token=QzpNqcZiHnmUPA59PiBpqd8S3FAgwvvlymKOPIqN41IXETWfeVEiQxG5Ys1tRztVL-y-4z4kMujxHe3uwsRvaB7LwhLdIZsQm7d78qsbDFzypfjK6mPwXGxUbwfxhkB7wSqj3MGC7aia8EUTAygm6V4RWpFUrZy9NDMEf0z1IedlF0QPmHg4DLXgAimFh4-iPxrafFhPUuSoPwJEeUIN5fhA7sAvI7qb58JQQ_GxOFiNX2oZofL6rxWl8Af4nMrovjFFL21qhieFTI2mk8jAyXjeIpoVp08i3gDWFOocbJn-b9t1sea3QthQc69XSfp1UDy5LhYETqZWxefnkKrJwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدنی وزیر دلقک اقتصاد: درمورد قیمت ارز از همتی سوال بپرسید.
خبرنگار: همتی هم گفت از شما سوال بپرسیم.
مدنی دلقک: نه دروغ میگه از خودش بپرسید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72831" target="_blank">📅 16:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72830">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cac062b9b9.mp4?token=TdIsw9GHBKiQLMf9KOxEhxVwYXMv9B_GW7tQX-Ra-bFXeb_CXjgO9aaKj0IgY-p7kayf2zqWWUd67PnAoakmuwG-lyxyXCavFsEhKuUe5Cf_lTG9y2C4Hwvr3xS7F7GQowhpMkH4p8nV1JmQLgQBdRDmlb_X4s3f7FuFle5ZIJZHssAB1wNr5TiFEiol0xjCKlz67nhHgE9DjVrNRImHM9iFUQ71SHeHkickiPdOr59edhyLpmJ-WcE7rzxV18h4VrMNCdzB3j_CY1j441JhQW5LCVvgIkelAsN1poQ4PTVqTHrHWhwPiiy6jA0NiTF7gQO_r1oYCu06Ejil-OYtSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cac062b9b9.mp4?token=TdIsw9GHBKiQLMf9KOxEhxVwYXMv9B_GW7tQX-Ra-bFXeb_CXjgO9aaKj0IgY-p7kayf2zqWWUd67PnAoakmuwG-lyxyXCavFsEhKuUe5Cf_lTG9y2C4Hwvr3xS7F7GQowhpMkH4p8nV1JmQLgQBdRDmlb_X4s3f7FuFle5ZIJZHssAB1wNr5TiFEiol0xjCKlz67nhHgE9DjVrNRImHM9iFUQ71SHeHkickiPdOr59edhyLpmJ-WcE7rzxV18h4VrMNCdzB3j_CY1j441JhQW5LCVvgIkelAsN1poQ4PTVqTHrHWhwPiiy6jA0NiTF7gQO_r1oYCu06Ejil-OYtSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراد ویسی:
اسرائیل توی ۱۴ ماه گذشته اسم ۱۴ تا خیابون و بزرگراه توی تهران رو عوض کرده! اونی که عملاً داره اسم خیابون‌های تهران رو تغییر می‌ده، اسرائیله؛ اسرائیل همین‌جوری مقام‌ها و فرمانده‌های سپاه رو می‌زنه، بعد شورای شهر میاد اسم همون‌ها رو می‌ذاره روی خیابون‌ها!
دفعه قبل هم بعد از جنگ ۱۲روزه، اسم چند تا خیابون و بزرگراه رو گذاشتن به اسم حاجی‌زاده، سلامی، باقری، رشید و شادمانی؛ یعنی اسرائیل اینا رو می‌کشه، شورای شهر هم جلسه می‌ذاره که خب حالا اسم کدوم خیابون رو بذاریم به اسمشون!
در واقع اونی که داره اسم خیابونای تهران رو عوض می‌کنه، نتانیاهو و موساد و نیروی هوایی اسرائیله؛ شورای شهر فقط می‌مونه و تابلو رو عوض می‌کنه!
با این حساب، اگه همین روند ادامه پیدا کنه، باید منتظر باشیم هر بار اسرائیل یه مقام دیگه رو هدف قرار می‌ده، تهران هم یه خیابون دیگه به اسمش دربیاره!
یعنی خلاصه تقسیم کار اینه: یکی می‌زنه، یکی تابلو می‌زنه:)
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72830" target="_blank">📅 15:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72829">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pK_xnTGQBFLsG27yALpsDla9qQSIdJ_GbrJRcYyzbO3ED3cgWgkSeVK71BXyJdPBXssROqUQmPFWGdY8Q9D2RWugkwctcwq6KXRFgpYokZDXAwAuK7bwfNjWCophZNRGBPbdNi19R4ZuUqFMp9UkjvMu6JYpkCCBDBZrzqVh-FuScYx9Xxh-zjTYQhDHZHdCNOc699fQzQuom7RBdsEDOw8c-fh82OQ2hTywy23pEM6-qQt6jcicgHDitfwNO8wNxom50cnOGgNPI1E56vBrPLqf5t1HC6DfFL7COoqWWCa9N_JW8I0FbkbWNR1lx_xqr_i0R-jGl_nnCx3JgvCyUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماتون بریزه از تاثیر سهمیه! توی کنکور امسال یه نفر رتبه‌اش ۸۱ هزار شده بوده،
که با سهمیه ۲۵ درصد، رتبه‌اش ۲۸۳ شده!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72829" target="_blank">📅 15:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72828">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2512f994a.mp4?token=Tlu8tpEjdmP3IvtDCTwdPKA8Zf67D8WwY_-2zzEM_6CkK5PACwzXwVZ-FIanfDpMvkgkdLK-FOE6KEJ_EurOZgK5uyAPN5GU-p2U9fEqBLCb45D77WMzgytqa86yvieRWO2DcQb3uY0CnYUUotr4pMvVHw1JpkruMTP0mQBFNngnfKGuPcbaESrdMNw49f4_FVju87eTi-y_zl6COeXEl7PhzKr5dR5XBtD8YA6-EduAm5CVXPnHcF93-z3w2LU1liw8-TJvQiFGyH7IAKIFC7k37L73cx-F1UMjuOK8fWYTcy_RZzWArN-jtQIasc6kFHimjy1I6Ed3CMz-NNRddA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2512f994a.mp4?token=Tlu8tpEjdmP3IvtDCTwdPKA8Zf67D8WwY_-2zzEM_6CkK5PACwzXwVZ-FIanfDpMvkgkdLK-FOE6KEJ_EurOZgK5uyAPN5GU-p2U9fEqBLCb45D77WMzgytqa86yvieRWO2DcQb3uY0CnYUUotr4pMvVHw1JpkruMTP0mQBFNngnfKGuPcbaESrdMNw49f4_FVju87eTi-y_zl6COeXEl7PhzKr5dR5XBtD8YA6-EduAm5CVXPnHcF93-z3w2LU1liw8-TJvQiFGyH7IAKIFC7k37L73cx-F1UMjuOK8fWYTcy_RZzWArN-jtQIasc6kFHimjy1I6Ed3CMz-NNRddA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشور چین واقعا عجیبه، روی یه شهرک یه شهرک دیگه هم ساخته شده. شبیه فیلم inception شده.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72828" target="_blank">📅 14:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72825">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hd0xWrA0Y-PlSV05DzjpW9fSZeCQxV1tU22xe915tdA48W9HIrRW8FgE4GR-OP63ptiwZIYspshFx0Ib5MM2eYANriUkYcng16H9CERe8gPdbw_exAOTiSXLnWrXKOuIhZaL1K6GRSoxleRkgPk42eWwbsMh-Mk2N3g5xO0YxaOLOKQaP4bNjyM4NN3Jxnz0wxHPOpN8KcET-kTXxUY7Z4VL-ujkMLQe9EsGflhKsqrEA8EO_9ob8po9pNRPD8G2pdPYaoJ1LaLMPVHcGPzhXF28HNYIRAMU9PQlDEXglNGRRMc_cHkHalQ7TsvJLhM6v7v-rVS3fsqqjPuiIMVBGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HlKM2EfE-xM1M0vPf0x7M844CVrqVuuekojAq-IchS62xN_f8rktgMIIE4m6RG5BX7NRI5RXuP4WUDZIGAx9RwNZL7gZgMvFQonH5Q9lHL3iKQh9WyZra88K90f5LNSuxPyFfTJjv-MLjCSG_6YG5Z1mp4tTh3U4Jnne7AAaA8xLKhhFNCFimEp3sj3YwvgsrLdFkQvxb4M55v7f7SqJmdNMjngJ466AAf79OmIPFlgK2R7mMRsXsEm4bU55st9ePuE1FfCndEoSaZKS57Ad5p2EXOD2P46j2AteE4zprC4NItoqodTl-jnZ00LlbYvpdMEofJL84Ma6sQ7XMqrSwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e31c23155.mp4?token=FLiSZsmBYl_Dv2btW1gSBxIgbFQlG1BgRCIg7mhNgxg_37gr9xZWs_LIYyro57Gs6FCxmUOZL1yHe5BwzeHIe9QrWiYx1pi_Qmg7k3dOjqjf6R7bx7K3Hl7y6MV3GjUkHd5kWOL0WYftpgNd3dLyjWvTixX7UJtXffP3RhRDs2NHRuvOaV0MgsbV5jRIrPKg0kSfvg3mPwMhfXCpIvbbstuWWRPzMAI_yIS2hSAc7fLGFFtMGrBZjH2T2XFxzrLLWH6bIf7sjZD919KxK_iChcnCzkNGk48SHlk3wr7RBZOEgeScVCq0QqCUcCLS3KQAHnMP4pdpv1-Cas5KM16Ijw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e31c23155.mp4?token=FLiSZsmBYl_Dv2btW1gSBxIgbFQlG1BgRCIg7mhNgxg_37gr9xZWs_LIYyro57Gs6FCxmUOZL1yHe5BwzeHIe9QrWiYx1pi_Qmg7k3dOjqjf6R7bx7K3Hl7y6MV3GjUkHd5kWOL0WYftpgNd3dLyjWvTixX7UJtXffP3RhRDs2NHRuvOaV0MgsbV5jRIrPKg0kSfvg3mPwMhfXCpIvbbstuWWRPzMAI_yIS2hSAc7fLGFFtMGrBZjH2T2XFxzrLLWH6bIf7sjZD919KxK_iChcnCzkNGk48SHlk3wr7RBZOEgeScVCq0QqCUcCLS3KQAHnMP4pdpv1-Cas5KM16Ijw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم یکی از همون ناوهای آمریکاییه(USS Delbert D. Black (DDG 119)) که سپاه تو بیانیه‌ها گفته بود موشک بالستیک خورده و «خسارت قابل‌توجهی» بهش وارد شده. ولی خب، به نظر من برای ناویی که موشک بالستیک خورده و خسارت قابل‌توجه دیده، زیادی سرحال و سالمه!
الانم برای استراحت چند روزه خدمه، وارد پوکت تایلند شده و بعد از تمیزکاری جلبک ها مثل روز اولش می‌شه!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72825" target="_blank">📅 13:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72824">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdf3b5b159.mp4?token=Ob1O1UWlEPz1Q5NWDohOdV-G8E6vg1jYgmIGSi11y_AH9pLPFhres_2S3rEQCezDyDLnpRD72t1yQT8xQA4MIycuNfgtHBIGK_n75zZ63iZzPnD25gZu0Lqdh20lvprzmIQvTa7ujOWDWJhgKnGo91PJknlaiMBAt_5CBBjmeWDB5BQgwcmJJkb9RFXZIAPtXSKjq1vEaXd8tqzK-_KQyvgS-1p8AGUS3Yxfhu4__F4cFJucWQwbvUPx6NGm3bwvpWfw3kj4wZufpnb3XgoUqI48HGLq8tQhHBmAoxUJgQEbHaAgcVi7VtgcVGfqaGSHBO9gW4T86EehQ-h1Br0fKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdf3b5b159.mp4?token=Ob1O1UWlEPz1Q5NWDohOdV-G8E6vg1jYgmIGSi11y_AH9pLPFhres_2S3rEQCezDyDLnpRD72t1yQT8xQA4MIycuNfgtHBIGK_n75zZ63iZzPnD25gZu0Lqdh20lvprzmIQvTa7ujOWDWJhgKnGo91PJknlaiMBAt_5CBBjmeWDB5BQgwcmJJkb9RFXZIAPtXSKjq1vEaXd8tqzK-_KQyvgS-1p8AGUS3Yxfhu4__F4cFJucWQwbvUPx6NGm3bwvpWfw3kj4wZufpnb3XgoUqI48HGLq8tQhHBmAoxUJgQEbHaAgcVi7VtgcVGfqaGSHBO9gW4T86EehQ-h1Br0fKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه خانم طرفدار حکومت:به پسر نوجوانم گفتم اصلاً نگران نباش!
خواستی سیگار بکشی، بگو خودم برات می‌خرم؛
خواستی قلیون امتحان کنی، با بابات می‌بریمت سفره‌خونه؛
فیلم مثبت۱۸(پورن) هم خواستی ببینی، بیا با هم ببینیم! این‌طوری دیگه خیالم راحته که همه‌چی کاملاً تحت کنترله!»
@News_Hut
😐</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72824" target="_blank">📅 12:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72823">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e258d805f.mp4?token=TkN0r99zipiRaz-oMy8TBeQfcik2HgfOxNEpR-gFGzm3dvQkbQeguvnloTMTxUXhPaixaDr65Ds_Na_QjbEh2IGm-LAbN-aps7Py24aa2dzCR6OeUlAFxRhIZ0iW-GmrZ_Jl4JoOpe0yihGRNLY1P2aIeRyLPlxz6L6JKZ4iRQ63y360GQxbIlr90_UeQrjFm3w68rPLaYUxq0QntZYLOWWES-TJP4aInn1DAMe9wA0N1L2_2N9fiWMSBojbIhjBfAX0WF2AAFBuOicpbWsluMuata9gg9IuMsg7yyWH2D4auT71slbS4DLzGsT0FLIW7ngjzy2C9WHBth8mTd_gCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e258d805f.mp4?token=TkN0r99zipiRaz-oMy8TBeQfcik2HgfOxNEpR-gFGzm3dvQkbQeguvnloTMTxUXhPaixaDr65Ds_Na_QjbEh2IGm-LAbN-aps7Py24aa2dzCR6OeUlAFxRhIZ0iW-GmrZ_Jl4JoOpe0yihGRNLY1P2aIeRyLPlxz6L6JKZ4iRQ63y360GQxbIlr90_UeQrjFm3w68rPLaYUxq0QntZYLOWWES-TJP4aInn1DAMe9wA0N1L2_2N9fiWMSBojbIhjBfAX0WF2AAFBuOicpbWsluMuata9gg9IuMsg7yyWH2D4auT71slbS4DLzGsT0FLIW7ngjzy2C9WHBth8mTd_gCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سال 2023 یه میم به نام Opium Bird خیلی وایرال شد که یه موجود بزرگ و پرنده‌مانند تو کوه‌های برفی رو نشون می‌داد و سازنده‌اش گفته بود که سال 2027 (۲ ماه و ۲۶ روز دیگه) می‌فهمید یعنی چی؛
حالا شباهت Opium Bird و طاعون
👺
و همچنین لوکیشن برفی اون میم و آب و هوای روسیه، دوباره همه رو داره به این فکر فرو می‌بره که نکنه داریم وارد یه سیزن جدید می‌شیم...
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72823" target="_blank">📅 11:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72822">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dc05a4717.mp4?token=aZeN99IbLHezu-DWHA-7yCbUNj89g2E8BA07x1Qfo_UTstFWiKz4aHRACeTX_OVLL-rvdNcKoR1Y8gUtlRaNXlCOsd3MCdwMfKygdqt7Zcmr4-nLClR_8ET9BEDEXGUxdLPBc-9-g-n6dWla0kuPw17ype6dQOvGOLGpX_rF391XJJeSduneUtlONq-2pQVrourOXp0TTmLZIFLGvin3LcOlyDwKS5JvXU0mtqe4MJ22Mqsx8HQMQRWCghtrPVzv0GXJjXCzHNrs4IBhNZnkIEMwZfuDYFLGPPMeUwnOjZr5P5reBmnkSxx9G8OlCUfrAz5M9ztYSoAMdvBAJ1EKKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dc05a4717.mp4?token=aZeN99IbLHezu-DWHA-7yCbUNj89g2E8BA07x1Qfo_UTstFWiKz4aHRACeTX_OVLL-rvdNcKoR1Y8gUtlRaNXlCOsd3MCdwMfKygdqt7Zcmr4-nLClR_8ET9BEDEXGUxdLPBc-9-g-n6dWla0kuPw17ype6dQOvGOLGpX_rF391XJJeSduneUtlONq-2pQVrourOXp0TTmLZIFLGvin3LcOlyDwKS5JvXU0mtqe4MJ22Mqsx8HQMQRWCghtrPVzv0GXJjXCzHNrs4IBhNZnkIEMwZfuDYFLGPPMeUwnOjZr5P5reBmnkSxx9G8OlCUfrAz5M9ztYSoAMdvBAJ1EKKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«همه دارن می‌گن من GOAT ـم، یعنی بهترینِ تاریخ.
من می‌گم: «پس واشنگتن و لینکلن چی؟» اونا هم می‌گن: «شما از اونا هم بهتری، آقا!»»
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72822" target="_blank">📅 11:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72821">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/affe4d122e.mp4?token=SS4UMhEXDc-GHBCT6dxPys35JHZjKUv7wvTDDbV0KH5dwtlo0OahvZru_M1aF6bmn91B5kVoDvWw2PHDBuqwXjxtaQ36pYLH5xuKfJ7lWoq1nrdZtqa9FJeLfpEb-lIU9a-kbF8oWj8d1vPfkB7jeDJLw6GN5998dtoWsxDrjmw8TZZzOnYmzyXk3OAEaLgXvjh0D-u4_4P0Fqvr0FfTNyHLq07170gTPQMFGQVL9bn00VxgvuKQMgcXf3T4O22CEnZleNzYDdiV-BiGr8n-ayG1E_4hNIHsZVaf9R4rTj2CfKWdgJ9A0mr08DZtluPX1clDlwNuX--_crUAB0zTig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/affe4d122e.mp4?token=SS4UMhEXDc-GHBCT6dxPys35JHZjKUv7wvTDDbV0KH5dwtlo0OahvZru_M1aF6bmn91B5kVoDvWw2PHDBuqwXjxtaQ36pYLH5xuKfJ7lWoq1nrdZtqa9FJeLfpEb-lIU9a-kbF8oWj8d1vPfkB7jeDJLw6GN5998dtoWsxDrjmw8TZZzOnYmzyXk3OAEaLgXvjh0D-u4_4P0Fqvr0FfTNyHLq07170gTPQMFGQVL9bn00VxgvuKQMgcXf3T4O22CEnZleNzYDdiV-BiGr8n-ayG1E_4hNIHsZVaf9R4rTj2CfKWdgJ9A0mr08DZtluPX1clDlwNuX--_crUAB0zTig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«این جنگ خیلی زود تموم می‌شه و قیمت‌ها هم قراره حسابی بیاد پایین. شاید حتی خودتون بگید: «خواهش می‌کنم آقا، این‌قدر سریع ارزون نشه!»
😂
خودتون ببینید تو یه مدت کوتاه قراره چه اتفاقی بیفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72821" target="_blank">📅 11:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72820">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e9f8cbdc.mp4?token=ro-30RsLBNDOsoxnAfvwT1naYQV041Io4VQ3sBu3FgVGT0pvNUbXkbSNcaOEE9aWsY9oxGB8PIlRihru2KW7A0lN35nnKGFuyPBeC0b4XOBxK97NHhW7a9dliprW78x4YPWtHfYWLITHmHo1nrIk6t-lfsy7303aBwz5IUPxcU8zF9juX8GrCdgczDvV_3_kbNBXa2vW9pwV7FemvL1-_pLEBcFxXcXXPKOwMRTtWpEIlz-zfV87Om590x7gKgm4veEtJKNkEzHL0IhYKF9l7ncIS58xiDawTKcYAIu3Z8-W_VH9sEtborrZIjgr3YCqC73lDPEzWno2fVSRxcJvDiDoA1is1qnscY6ikBgKIwmbYFxwx26Thca4BGgGbxz6N28MJTYLI5fxif4LXrmfgNxqWdeQu5gWo8i9GQcmLil6t30PL0y08dBkzvfYLiqT-nU_diSGXV5XczBb8ediHOiJ7aFnXYEP6UVuKW0mSAn5nL2XBMu589dtPXZt3w1NDXovwEEeblDPI5KAXCephhrUWOR-yAVx6cuqULNyrrFessitjrADJe_U5cLZAYsoKFJB-MTKS7z1uHs3TP8vImat_wMhQBTCurODWmvvyNVfCE76B3Fau1891_IV1MWcZYqeG1P6EHKx1Kui2Fz-NfKAguxee21ujgNjORwYx-E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e9f8cbdc.mp4?token=ro-30RsLBNDOsoxnAfvwT1naYQV041Io4VQ3sBu3FgVGT0pvNUbXkbSNcaOEE9aWsY9oxGB8PIlRihru2KW7A0lN35nnKGFuyPBeC0b4XOBxK97NHhW7a9dliprW78x4YPWtHfYWLITHmHo1nrIk6t-lfsy7303aBwz5IUPxcU8zF9juX8GrCdgczDvV_3_kbNBXa2vW9pwV7FemvL1-_pLEBcFxXcXXPKOwMRTtWpEIlz-zfV87Om590x7gKgm4veEtJKNkEzHL0IhYKF9l7ncIS58xiDawTKcYAIu3Z8-W_VH9sEtborrZIjgr3YCqC73lDPEzWno2fVSRxcJvDiDoA1is1qnscY6ikBgKIwmbYFxwx26Thca4BGgGbxz6N28MJTYLI5fxif4LXrmfgNxqWdeQu5gWo8i9GQcmLil6t30PL0y08dBkzvfYLiqT-nU_diSGXV5XczBb8ediHOiJ7aFnXYEP6UVuKW0mSAn5nL2XBMu589dtPXZt3w1NDXovwEEeblDPI5KAXCephhrUWOR-yAVx6cuqULNyrrFessitjrADJe_U5cLZAYsoKFJB-MTKS7z1uHs3TP8vImat_wMhQBTCurODWmvvyNVfCE76B3Fau1891_IV1MWcZYqeG1P6EHKx1Kui2Fz-NfKAguxee21ujgNjORwYx-E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«یادتون باشه، این جنگ یه چیز مصنوعیه؛ یه مقدار هزینه‌ها بالا رفته، ولی خب برای اینکه دنیا امن بمونه، قیمت زیادی نیست.
اگه اونا بتونن یه شهر رو بزنن، بذار لس‌آنجلس یا سن‌دیگو رو بزنن؛ این در برابر حفظ امنیت دنیا، قیمت خیلی کوچیکیه.
در واقع، این ماجرا تقریباً دیگه تموم شده.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72820" target="_blank">📅 11:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72819">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb2e238707.mp4?token=bxtcWvNk7I9RNCbs30ArwHAMlp3x1cX-PHP99MTM3yyPzMoaIwCj5T_ttEb1wuswhdpr10C5EiQZKDjPkQ5McXzuXrZPsnv4IjYM_dA_DSD_MVFKHooD3ah_7W7x-_UV461MAWbvIJwfpjAGHYlguVdK152wt6ju8KtC9lwxm_FC7RGb_ii22-krngPYWvxafJT0heJgDaNYhiCmdTtO8uKrrM9v08IOqK7qVZhAfpnoXOccKDSgM_-mPbg5bIbtPWs6aPMHKNFPJiy168C_uSysQKTR5Z5R-DTchOnYc97K3tqvvTRH85RpAc71skRuKz9FcXQkVgY7O3CDIzYHtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb2e238707.mp4?token=bxtcWvNk7I9RNCbs30ArwHAMlp3x1cX-PHP99MTM3yyPzMoaIwCj5T_ttEb1wuswhdpr10C5EiQZKDjPkQ5McXzuXrZPsnv4IjYM_dA_DSD_MVFKHooD3ah_7W7x-_UV461MAWbvIJwfpjAGHYlguVdK152wt6ju8KtC9lwxm_FC7RGb_ii22-krngPYWvxafJT0heJgDaNYhiCmdTtO8uKrrM9v08IOqK7qVZhAfpnoXOccKDSgM_-mPbg5bIbtPWs6aPMHKNFPJiy168C_uSysQKTR5Z5R-DTchOnYc97K3tqvvTRH85RpAc71skRuKz9FcXQkVgY7O3CDIzYHtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: جنگی که علیه ایران راه انداختیم برای «
نجات دنیا
»ست!
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72819" target="_blank">📅 11:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72818">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225b755540.mp4?token=twhhaM0bmjStgLeMuFihAxI9iaPARCiztyO1ZUOoaiXakPBFVNXazAwSWK4O2HpjpCWqGSWo4s9gsGzYrFNBwIR7c8GK-2AE7xjkpub3HsejedoxJykMfeBsPgbZWZY90iMfKPPCfxxj5c8pRa6CbtyKWr21kprh70UNYjk9aRg7qFj6wTlK4tIohNzaftajjheZcl49A9jiLnkgc6zlbyfDsOu6_fv8sCAvdv5SDx7UkjjiuF5HTeYW-EbKwGJEeoDt4tbSQrbJqF4gGbgS2ipVbEkcx2NaPwaxbjsIXTDsjmgzyk9KnXZ8YfCqp3zWgc9A6vMWFIiTFmh4Ct_RWoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225b755540.mp4?token=twhhaM0bmjStgLeMuFihAxI9iaPARCiztyO1ZUOoaiXakPBFVNXazAwSWK4O2HpjpCWqGSWo4s9gsGzYrFNBwIR7c8GK-2AE7xjkpub3HsejedoxJykMfeBsPgbZWZY90iMfKPPCfxxj5c8pRa6CbtyKWr21kprh70UNYjk9aRg7qFj6wTlK4tIohNzaftajjheZcl49A9jiLnkgc6zlbyfDsOu6_fv8sCAvdv5SDx7UkjjiuF5HTeYW-EbKwGJEeoDt4tbSQrbJqF4gGbgS2ipVbEkcx2NaPwaxbjsIXTDsjmgzyk9KnXZ8YfCqp3zWgc9A6vMWFIiTFmh4Ct_RWoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«راستی، داریم حسابی ایران رو می‌کوبیم، اینو که می‌دونید دیگه؟!
در هر صورت، این داستان خیلی زود جمع می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72818" target="_blank">📅 11:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72817">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72817" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72817" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72816">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0FhHN8sSbldN0rqHUud0538FHXOGB2_QyUtaNOo7-q7gcgm44Ypj4sT-hiQH5rPBhUs0la34kYNfV2Ncfac35Db31itvVEGpuHaAQQeJKHl8sfJEZ8hUutkCsrdvXrWzN7HaCSv0R2EOwWF_gbCJtjKiU3xT2O7iXs6lCzP5bXCY6dd0mdEvDys_NrzuGeebgkPYnmR9TGD9kKCz6iZER8ySKklwi6Eyw5RLmex2jSUSAyRwmmaPOyonqDeZYUCON3inBxJQsSofq1Ga_iEXc5Zb0SEEsVpVVDXZzGCfIhGfPxXHVd5HWax3LY587spa-G_sgTQXRCvvIYP0pC51Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
اسپانیا
🆚
کرواسی
چک
🆚
انگلیس
اسلوونی
🆚
اسکاتلند
مقدونیه شمالی
🆚
سوئیس
ازبکستان
🆚
کره‌ جنوبی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72816" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72815">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c201257b1.mp4?token=PyrG11QrAd01yfX93Ly_Dpj_oguiYQhIDGpAPH0kTNlCpFhdRr2CfP74Hgtrm5y3man3LwxqAH76qtEu-ZPbOo9eFjdtEP9jvSajQ1IN-FaEVHG7Aj5hJCZYYmyGGA0vYXHuCnNfQ-Ybknkq8akj0MgkYpxxS2-QWd6LxuvYXrXvBB3rZS1BzRL51itmXk0nttlWgyt0Ap9AFlNgN1gqYyrtMfk-4AlJo6JZw3XlYxWhDoFdttQefuiequevMGXBBrpYB2NYM2cTKvTjacHajy4GA8QkTBSg2vzOkQagY0k4fSek05J6pePI8jEk8YHEc9yWyUkTGzP1HsX6Mt7XzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c201257b1.mp4?token=PyrG11QrAd01yfX93Ly_Dpj_oguiYQhIDGpAPH0kTNlCpFhdRr2CfP74Hgtrm5y3man3LwxqAH76qtEu-ZPbOo9eFjdtEP9jvSajQ1IN-FaEVHG7Aj5hJCZYYmyGGA0vYXHuCnNfQ-Ybknkq8akj0MgkYpxxS2-QWd6LxuvYXrXvBB3rZS1BzRL51itmXk0nttlWgyt0Ap9AFlNgN1gqYyrtMfk-4AlJo6JZw3XlYxWhDoFdttQefuiequevMGXBBrpYB2NYM2cTKvTjacHajy4GA8QkTBSg2vzOkQagY0k4fSek05J6pePI8jEk8YHEc9yWyUkTGzP1HsX6Mt7XzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوستاد خوش چشم: اگر آمریکا بمب اتم بزند، ما هم پدر بمب‌ها را به آمریکا می‌زنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72815" target="_blank">📅 11:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72814">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/796b47b54e.mp4?token=ITbeThhR7OVlgVtigzZCxUyLBpAu9IWKt3nHdXkvQR50B5Lb-Wjs-24-FO9La8mx8xrhOPtbrNxparlS1u2IL190BsvX_tjfI8BcmbGcmUv-B2PPg2S6_FVkET0aSDBEsTzwcZkyKhsBRRzfUOdLaZImBC9qvI5utQCa73vSasEr9b4rsVKUVAu2EGtu3RIduCELE5dTC7IhLDmW9hnrHHsmezc8U-tHdADKY8Tv7MXKENLBNSSgCedEPuJiiD5_Xom6DRSLmVuk8tUy8hyDOpVyksjBwMy3MhQbnIgcbLvJXgfcAbGFnkzwfOtuf5lvfCQkhzrOU6hyqtBBmWisAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/796b47b54e.mp4?token=ITbeThhR7OVlgVtigzZCxUyLBpAu9IWKt3nHdXkvQR50B5Lb-Wjs-24-FO9La8mx8xrhOPtbrNxparlS1u2IL190BsvX_tjfI8BcmbGcmUv-B2PPg2S6_FVkET0aSDBEsTzwcZkyKhsBRRzfUOdLaZImBC9qvI5utQCa73vSasEr9b4rsVKUVAu2EGtu3RIduCELE5dTC7IhLDmW9hnrHHsmezc8U-tHdADKY8Tv7MXKENLBNSSgCedEPuJiiD5_Xom6DRSLmVuk8tUy8hyDOpVyksjBwMy3MhQbnIgcbLvJXgfcAbGFnkzwfOtuf5lvfCQkhzrOU6hyqtBBmWisAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران هر روز ترسناک‌تر میشه، یه پدر برای اینکه پسر 3 ساله‌اش رو تنبیه کنه، یه بسته مداد رنگی 24 تایی رو فرو کرده توی باسنش!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72814" target="_blank">📅 10:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72813">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0246c863e9.mp4?token=Y8T7h0gonOoIptOvo9PzekhCSPrmtooLL_HwQhJUioor_to8zhiK5w7xjgwMxda20nGS-mwkgkEMMbbrgn5QhGLiH5APiwIM9jVYd-rPMUjRnpCFvrexPoQ5sZ6SB2UySYmGBNHNMiEw5-CiG40M9G3FiSleuwl10C7BoWVddguMwtnl2Q7b2D9c-gBBGMLHjJz6Vyfjjb0A1V5_-wiYEZvBbNSdd3h3y15I8zrT2GR0ubGMbGC4pA9rVfOkaIV1fM680PUXyz-15PZ7Ajdwww985tnu159oCLotENE6r_QrwqRpbhFV2n-2CDVRBdTfIgEwANPIJ2ZgHgeqEj_XnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0246c863e9.mp4?token=Y8T7h0gonOoIptOvo9PzekhCSPrmtooLL_HwQhJUioor_to8zhiK5w7xjgwMxda20nGS-mwkgkEMMbbrgn5QhGLiH5APiwIM9jVYd-rPMUjRnpCFvrexPoQ5sZ6SB2UySYmGBNHNMiEw5-CiG40M9G3FiSleuwl10C7BoWVddguMwtnl2Q7b2D9c-gBBGMLHjJz6Vyfjjb0A1V5_-wiYEZvBbNSdd3h3y15I8zrT2GR0ubGMbGC4pA9rVfOkaIV1fM680PUXyz-15PZ7Ajdwww985tnu159oCLotENE6r_QrwqRpbhFV2n-2CDVRBdTfIgEwANPIJ2ZgHgeqEj_XnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو تا از لوکس ترین مدارس بالا شهر تهران که شهریه شون یک میلیارد تومنه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72813" target="_blank">📅 10:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72812">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84c2a17b7a.mp4?token=WXanNG_u_7h5304IG5EMHOR5T63FyG22oD_dESfCBD_Pg1N4CVNlS_N1e8rUPchA68CD4QD2D-WZ9Se3YMLub736081U3UUH2sUjff7IDrLj0avaLGIOt2XE2VAVcT86BtQl-RmXkeyiL0xNS3-EZqZ-8kPLn9xgyU-PH6iNVzjh7Fzki25HFWjlA857ld1REq_Q-v3I_VigbUdzQpKg5bwp2HpeU6Iwgz0Zz45P4WmaFYAQLsQs_wH0wzMnUU85rfMbmO6WfqrGfe9XrRvuxZK5XkUYTAr58Y6Ih4IuefdVzeN1-qL1XLz1Wk_1Ux0aD8JlO4jq7yV_Fag1-UkY7ItDuJp1tX0q92BERM03BeeJkb7A9u5lhU5TLhcKS8zlRbQFQWHdH3mUTh9kNXHd0Iz8Hd0xTzaA0AnafE3U1QxuF9sJSogy4IZ8YqSrB-AaaWPN7PpZ9Q_zUti3jN7pJyqgQmuJq9rTT_tBByL4RCbj72V_VueLAVNnLwdNR_-LPmq6l35vZNuV_oIDQxgGwNM06eiJ4f4iAvsvZ-ISg4RmvqHLQ-TigCRm4gGYxRCYtVVpohNeeJPBXZz6GP6S577Wf-C6cqmlDKUREJoOGPOG99ipg17tpBAuqKEFqI2sbkmgJ_cbjUTHjGkFuuvJ3PROZdJsU0OwuT0tRBtF9_I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84c2a17b7a.mp4?token=WXanNG_u_7h5304IG5EMHOR5T63FyG22oD_dESfCBD_Pg1N4CVNlS_N1e8rUPchA68CD4QD2D-WZ9Se3YMLub736081U3UUH2sUjff7IDrLj0avaLGIOt2XE2VAVcT86BtQl-RmXkeyiL0xNS3-EZqZ-8kPLn9xgyU-PH6iNVzjh7Fzki25HFWjlA857ld1REq_Q-v3I_VigbUdzQpKg5bwp2HpeU6Iwgz0Zz45P4WmaFYAQLsQs_wH0wzMnUU85rfMbmO6WfqrGfe9XrRvuxZK5XkUYTAr58Y6Ih4IuefdVzeN1-qL1XLz1Wk_1Ux0aD8JlO4jq7yV_Fag1-UkY7ItDuJp1tX0q92BERM03BeeJkb7A9u5lhU5TLhcKS8zlRbQFQWHdH3mUTh9kNXHd0Iz8Hd0xTzaA0AnafE3U1QxuF9sJSogy4IZ8YqSrB-AaaWPN7PpZ9Q_zUti3jN7pJyqgQmuJq9rTT_tBByL4RCbj72V_VueLAVNnLwdNR_-LPmq6l35vZNuV_oIDQxgGwNM06eiJ4f4iAvsvZ-ISg4RmvqHLQ-TigCRm4gGYxRCYtVVpohNeeJPBXZz6GP6S577Wf-C6cqmlDKUREJoOGPOG99ipg17tpBAuqKEFqI2sbkmgJ_cbjUTHjGkFuuvJ3PROZdJsU0OwuT0tRBtF9_I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: خبر داری دلار شده ۲۷٠ تومن؟
یه خانم تو تجمعات: اره ولی ما بخاطر وطنمون اومدیم، اگه ما نبودیم دلار حتی گرون ترم میشد
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72812" target="_blank">📅 09:34 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

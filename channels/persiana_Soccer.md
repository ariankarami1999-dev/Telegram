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
<img src="https://cdn4.telesco.pe/file/peoXE9vanxvysLb0_stXpi1BlvuRyLxwVF5e7TR_N3vGE1ytQtS3Exn0n58MdQa3yb4HRbjdO2Ts_aH51m7bdHrB6oZG5ZMyxnR3H3EgHK7guApVMjeQRrZFEmJ2f_1R1H5U0fKQlUHm62WTq4PiNKlXfL271Tn9ZzSKIe6IBztl75_LaHFIpEa6dPA57UPuz6yCzaRhsQBJMabDBn15lxVSjwmTVu8Xy573AhqlYr3qhoUimX7_UPIzcQ2Y1U91YLScDXOuf3vq2OsRAWFcNhw52CAjRytfL-TC5SKesMN1SQRML-YhNdWc-jS8oh5fQ11uf7AV4Upo-sYzT-0BRQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 443K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 06:13:59</div>
<hr>

<div class="tg-post" id="msg-30589">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ALpMGnodzvG-YuHUB-WeUoC3kbM9eaAZc-PByh5qS4Crew7mLYijPYJQH38hIMxxDB_mgha7O6M7YqK3tnzEZFvYwWpOz4dxwj1Q06u73U0-O04BFEtMJTOBcatcF3sn6QGZmWhH8hb8GsIL0zYJqssyXKtg1XwD1nsv14SNsQsbJsT2DiLJosCOgIMHnmHJWeZZTXy5kpl_ieShH5WkuTvzBLHvvGUEODwO_OMz7QogGIRpRJqMuVKNqBoFwlt1BZW8MYz-oD2WWU5npmHWDPCMojppwO9PaKbTr20mvBYoLC1E2pNT16_WwxFjawEyCVSWktjoPPJqkdzWi_r0mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l1HhnJ5CZLiezPrmneSRk5Nw0Sa9_d89Gk5nGoNGPDTCuIn6SGoADuXlR_6Fs2DNhoA0ZyBMMvihabIhXylt5X4LtEI9nciEP_g_1ivU2v-7iJ_1Ze-59H0LpFDxy1CExz8LmeRU_UlcXSAlfV_SJf8EV-YOHXPxWVGHi7x6xUk_oRkizrM1Y-m90fmPBAS1psP3refdSq6uAIryF-33__VQ2ygy4x37MCniaQTe-xTIPuFlmFYUMp45j5kC49wL7hvTKfVMxYUl6-7Q_7-0efWAZGZJXilZ7EQlMw7kkxGrRKKziG88XgMy_YR_iwZcXKDDPagJaWpunGOYKZ5kdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه عملکرد لامین یامال
🆚
هری کین دو کاندید اصلی دریافت توپ طلا در فصل 2025/26
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/30589" target="_blank">📅 01:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30588">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLDbd9pw1PojICQXadBrd-zYBPSaupVkH7SnrhJceLwm8aDU5xYGF9IFQb3kW5fcyDwdvj1ySp-3ZYY1Hi4KgiCW8be0Od4sqQWeZPnINYxVSMBsQlVkMJQev1x7q_G8cfhQ5FZGdmASPMH_qRansZT8i8Sgf-KoRohGYkFXWRXcQ4U16KzheWyk7hDp6xzAmqYhA3kd5agyRjXnO9SmFPeViYukAj3dgPG5Cl1cqzmwq_Yfkbp7U_Mqoa3ycPXJgyT_-7ZN84lU3oRH4Pld0cm1DU2jdHQKp5PuHR1tqVhwszX2JY27h15FV7nvi4RSf7hzoWvymKPgierLNqGu9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛ روز شنبه هفته پیش رو باشگاه استقلال 70 میلیارد تومان به‌ملوان‌پرداخت خواهد کرد و با ماهان بهشتی هافبک تهاجمی 17 ساله این باشگاه قراردادی به مدت پنج سال امضا خواهد کرد. تمام توافقات بین طرفین در روزهای گذشته…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/30588" target="_blank">📅 01:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30587">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPWWaE3aorjXuKiynQRW5jpEd07BywvZVZDLUsEY2DzJeYvDEzGBMHymJph8izK2y0tqP0gBOkQm7Hxhtl5Qkq_90e7ksLGHddnsMgoZddAj0eO5lhXzVKJyLhMRGyGS10dEgdDkAqCH50nkpD_mSWoFLPNkKhVcghHBNU3lWsRFL7R6bGJytypUToHYgpgoTsD0SKyHg9js2Z_9NkhMQa7E7qB12sXmIJ27dl5jEgNVy7b5FgBZwGnoVd2BZucheqQG3ZL0wQFAi323ECUvKgyue1PzMC2CKXNQ3DHUHy3QYziM_SEVEnkoRhn0dbe-E_FPEemfBt8t5QED6nL4rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نگاهی به عملکرد و افتخارات شش کاندید توپ طلا 2026 در فصل گذشته فوتبال اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/persiana_Soccer/30587" target="_blank">📅 01:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30585">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgTwp3C2adBwlljqs9InR1-cWWXSiRSTj9UCzHhWCeVTgCP3bQ4ijrJq1VHsvUfLUlBSlj90XijW2WoFoPYsRa49CDbBWmfJzH95vXAd0tpWLZQC2qweE6U7w_TfDtJglU6xP3rf1VlCTtkA4D0DncasgYmLSsi6liwRUuR3fZNCwtMY6qp7ffyLVyYONv8n9JBetGuc1mmEws-o4bFM3o6vBn5rs8ySAtFpjRSULyh8d1HyXQIJLu6rUXJ8TTZCmdq_1cbwWm-30ZLCHyXE8XERd9bGIGABU8zrQw4_uctysb9NtvUGQ_L3Um6YWthlyLQXZfl0bZRP9vZHa7zDHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌ امروز
؛ دوئل بلژیک - فرانسه در غیاب امباپه و رویارویی کره‌ای ها با شاگردان فورلان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/30585" target="_blank">📅 01:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30584">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBPPR_ba9DwwoCvJOzgYzOFUcZPiqpdI5QIxg5QpM1jtXrJbYRPcHl2RKMOfHYoQKtd5j8ffFij5t_6Rd0VOKeVIdktINuRKzTZjW5-qjMLcuAcZPctkZTXLu1RSR8ASp_urhnUYimMReNuUzA69vd937avcF1wPKfQvyQ0jnbdtpSybb3GBWJdR01jLUhogPL0tTXiDl15XTpaeOKeUklHeT1cSlgCGcFA3-_idYF8xtZgHVtH_t69nyhnxKycfwMtmS0vJOt558hcVQqXEQ7EN8GrVQLXvVt3Hv-MTGljmztgwmLqjttqgMFSgyuU3fSlNkCcTJ9x-eizOfLE-VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
اولین برد ژاوی با هلند و 6 امتیازی شدن پرتغالی‌ها در گروه با برتری دشوار در خانه نروژ و شکست عجیب ژرمن‌ها با کلوپ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/30584" target="_blank">📅 01:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30583">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9eofJ7HoH3uVPIGNu4_D4aBAs3mA_DCOrWLeSnR44hVILWrGOIl22eJqtjrHChJJphpeIH1Kyv3xiK749biS_YiqRCJLfg6DyGSGsf3bxHio5pp7OiYmz978Z2VGgmh6-1gfpqnhGEqVuKsXtmmxhBpMhg4sMNFByp-cYFLm4qCyuYtBt7NlDOpYGCjS2sojiBR1sKu0kWM_d60YbRU0Lmb_ASvfnoYljVrlloBApXr3nD1g0r-KZge5Nj0DiK64hmh4GlMvaC3vLP1nV4dv-y0YVhSsMjyKkLLxEzmyKfBIrptoGS_XFlGJB5eOLrklNFNSqDIbWI08ANHGh5t2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💖
سایت بین المللی
ژتون بت
💖
🎖️
معتبرترین سایت روسی فعال در ایران
🎖️
⛔
شارژ از طریق کارت بانکی،ارز،ووچر
⛔
تسویه حساب سریع و امن بدون احرازهویت
💎
هدایا سایت جهانی ژتون بت
:
➕
واریز اول دو برابر شارژ میشی
😍
➕
15% فری بت هدیه برای شارژ بانکی
➕
15%  شارژ اضافی برای شارژ ارزی
➕
50% بونوس جمعه برای شرط بندی
➕
50% بونوس دوشنبه برای کازینو
➕
100 اسپین رایگان هفتگی
➕
20% کش بک روزانه برای کازینو
➕
20% برگشت باخت هفتگی برای شرط بندی ورزشی
🥇
دنیای افرهای بی نظیر در ژتون بت
👀
🖥️
ادرس ورود به سایت:
https://jhet0n.online/fa/?btag=2786270
🔖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،ترکیه،سنگاپور،فنلاند و..
💖
کانال اطلاع رسانی:
👇
P5
🔔
https://t.me/+bnTnbHERg7Y3NWU8</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/30583" target="_blank">📅 01:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30582">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇪🇺
درهفته‌دوم لیگ‌ملت‌های اروپا؛ پرتغال در شب استراحت مطلق کریس رونالدو با درخشش گونزالو راموس دو بر یک از سد یاران هالند گذشت. آلمانِ یورگن کلوپ هم یک بر صفر به یونان باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/30582" target="_blank">📅 00:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30581">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeSefepN5_G_5ipAv9WFg88VGQ-X-eNmRU0ObVeDseaYlI75TaJ2vi01x7dg1r3hKuCslIhzRyasqCdC66FoX4Ehx5M1H2rAoz60VM8LlkL0tHWWD8FNh2vtHF4lK3diTkS5Fc6wEja569b7IRWGroy9cbhZrq7OWPdbNpPSFwj-Zyh9nNzGM7irlUZkyg-k9Tw2ztwj9EZjK6_GyejOKb3ev886lST1WBlBruQod1KfLKtqEEuQd97NJOMUiHOjwRQj-i9J2HF3BzV-NV-tEK1kj2xs0VVzDHtmTwWjBu0-mSgJ3aIwwZ16OjPr4ns4z43t42fmAIptaLNZLiW9BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌دوم لیگ‌ملت‌های اروپا؛ پرتغال در شب استراحت مطلق کریس رونالدو با درخشش گونزالو راموس دو بر یک از سد یاران هالند گذشت. آلمانِ یورگن کلوپ هم یک بر صفر به یونان باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/persiana_Soccer/30581" target="_blank">📅 00:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30580">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLbdzfJnKqhkpI0m6gkBfR9bc3j93Qyt533siiF78sZc359Ii1eNPDdoHgBxy01y9LydhClEE9to2bQ0dzqCDqJKIXPmWNti8j7B2-KpRxdC1LHlI0riaBWiTvS2fVBLiKBtZeNO9GN22NKwN2mUNI2WSoMC_dBEQqdRmu1ezjQB_BflJ5F6HsNv8r43uT4j8p-qBPoo3_EKd4bLgSJqFz2UIwMX2HE46YIdwhqKgFjuiJrHoQYe0yxIiJ6kcIqs9hxi7eMWpj2q8wCdJtX47Cb6mi9WUQ1U4NEf9LMYJFu8gBGiV1TTjJ4arpPw00JmuDp5fGzCFsJdBIKo7Jqafw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
خورخه ژسوس سرمربی پرتغال در واکنش به نیمکت نشینی کریس‌رونالدو: رونالدو بهترین مهاجم و بازیکن فیکس تیمه؛ امروز چون میخواستیم دفاعی‌تر بازی کنیم و کریس رونالدو 2 روز پیش بازی کرده بود تصمیم گرفتم امروز بهش یه مقداری استراحت بدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/persiana_Soccer/30580" target="_blank">📅 00:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30579">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1j7lGiUumkkmO_4rnORn6kRLJ34eHemfONZVmLcrAwtZyJpNcYrLr1UDMvfPu9XehDyC5kcwRW38FRv9aslJlm8n5FnPZ8hV8TGOD3us2vcsJddL08Qku_Y3vGl4DL2BN-XAmLcySt759Uv36LQXkg51HshTBDxzXgPNmcZAfnKABk08my2S35wRTcBqtxK2Dn64vG6WraNEIe01ibeC8vJnfKFNfxso7VzNdkDHtYHzUxM1jk1EpOn3_9w_WN7iP1kDEBY5wrwLatnmQttxzxIqTiE3o3S8QMCy4lqJlar8QbJh_N7rXIiFL6ey43mNG73cfW941U4epXmlrcmRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دوایت‌بایکس‌فوق‌ستاره‌باتجربه آمریکایی که سابقه بازی در NBA و لیگ‌ برتر ایران رو داره با عقد قراردادی یک ساله به تیم بسکتبال استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/30579" target="_blank">📅 00:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30578">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEHN12W8beprAraymzAikEwvJqWzmA0Qc1_5fax6h29nV-lFeSNJUB84DDlFvpVZ_QDssee237e7kJ53cEQUEvf76F5KTH8ExXDzD6w3ZVcBtJUs1CbAMxSIdliBtpyy9rW3m5BSHGWiBdfO4uYn4S0iaba7ojOkzN13dyVOGaboSna33Dza2Zc6iBvYTas_IYeY_7PBrEHNPFjLLRZjsKrvsfD-pUhi524nNmGaL5unXJJFqhyNlpmcwTMlMWfDMLzqFY8BI59OUo8RrPxy_eaOUvr9yKhJmaMaY1Fu1YjRrS8kHkstUQAtD1QiW9k4w62YQzREPokoB5CpVuzM3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیمان حدادی مدیرعامل تیم پرسپولیس: به یاد بچه‌های مینابم که شده جام حذفی امسال رو برگزار کنید و اسمش هم بزارید یادواره شهیدان میناب!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/30578" target="_blank">📅 23:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30577">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IV79CUWQMDfYfZIkVSJUzfS4FrXlab0a_7XOw5P_GFGgXa-t9vpKBCtHCN4erRDQxl7TIcx9PhcyWY22mLQTgRT2yZ2n5mVyGqfA8YFBKiP_Ht_JYCCKWu8Gy_Y257k-yRltgVb2KlcWPADpcQz6di93xuUVU-jYT_Agluu_h9WuoB5KntHyfgUN0VwsVbwmw5sVSt4E7XPSHwvXvWHUl66E1Rx1Oy_StRBzCU9Pt_47D-JC9HeBV4jB7SXXyi69mTH0Fo2QwrcI9UAHADaR4GkalfDZCLlHPgrs6E8_0mM8NvYWPU_u9VUAb9IxQsoD7-lkSo5hyHdCFllnSrby8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته‌دوم لیگ‌ملت‌های‌اروپا؛ شماتیک ترکیب دو تیم ملی پرتعال
🆚
نروژ؛ کریس رونالدو روی نیمکت پرتغال قرار گرفت؛ ساعت 22:15 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/30577" target="_blank">📅 23:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30576">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjIjb5EefVHga-eT4QuQguYeDRTbv9FFlLw5C1OcQwm2GvnKYpoh3lD8SZQs2rOYQ3XxnnsbfK8_qdcMIrGxXNYR-J-U4rNKUx5XwVQpFyzzZ_KPe3tBhNSXcT2-H1Eh3e_crCnRctQV-XwyCrKwMRitGi9K02oB0iqRKoi63yJH12rGQKplozw2Ggv8HRtgVpxTe2M6BmKhPzV-zJb-3zgoqYvjXVGKoGUeLIo8qroVILtd7QtTnAfAXI-BWVSEwDfSqcW5aoN6J66aW9yYQKepqKvC7PuBaczGl5dZUU0J4cQ0eahOtP4Pp1OrUIYUzqR9eGf01TVB1enVOYTqBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛مهدی‌تارتار سرمربی تیم پرسپولیس روزگذشته به‌پیمان‌حدادی‌مدیرعامل سرخپوشان قول داده درصورت برگزاری جام حذفی در این فصل سه گانه رو برای این باشگاه به ارمغان خواهد آورد.
‼️
مدیریت باشگاه پرسپولیس هم امروز به سازمان لیگ و فدراسیون فوتبال نامه زده و گفته…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/30576" target="_blank">📅 23:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30574">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qVmlAAfZIrXVJbleGUdXxAuNBq1VeA363JToF8eQrMYQVyO5Mm-KJy8zGOa5vPCIfbcXvnBRi6BHt5yMfmxjuTSKtZgOG9FgLc_ZO6iy2UEWLwqLgILqy0axvjZ0QUjGn1WQRqMTdaRq_sL0tB4OEsxVZlL83Hh4DSe7gF8EZZ4_Fd8yGKY3iSMJKKF9-bQAx03hPv7-KJ2WfWjC8T_u5VYmZb3Gz3jHlXLT_XFwZJ0IEp9ZJHPfZeDM4e0BKPqJmU_6duktBd2tX31f9LIfe3qhvgWH5G_IBquAIEiO98UYFlazbHCDGUIDHPhuMQTRozh25Mw_IZwrsIMCdDg63Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cgWFFFQLOHLRcvyqyvuhf7QMSuoneOvc23bM_oDtoZ4XxdLgJss84GEWqz55LGGKIKujQaL0vlipn0mXIPe_yD3vE47YNZ6FKBmkM0BU28hmz4JObSvZ2xwGt2fTp27bEWEZ8Q3kFHgQ-kMR3JgyO2zLGJ4XapLGSFG0znY8k5AvoE9WEBEH0jZfSiC3O3_IS0Ygmr-pO_0h3UBwq2jQkOAPNYtVduuf5-avZW0wa5hAjRRWV-sxDTZdCkHA2fCGIBEMK214M1D3Nz_hs7DL65Bk1jxrwamF5l5tnKsI0dRhtS3vxhGC8JuFHYsiYsTDa-rLjtC8tMjAofbZpFWRDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم لیگ‌برتر بانوان؛ آتش بازی پرسپولیس مقابل قوی‌های سپید انزالی و شکست آبی پوشان پایتخت مقابل خاتونی‌ها در ایستگاه دوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/30574" target="_blank">📅 22:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30573">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djHcEPmzaishCQE4q0UwjHyrFFPCPAATbYyCG7dgnjyDlHaysfohe1D23ATtbEZz-jBydnlFqLgIPkgniqfyw07e1zn9dIGH49LqP6k0giesHqmLeXxOT3EH_vMPU-rt7yLi7h08SRBqEc4eUAAER2tQPVn-GXqpOU3KOPKHMVxCBK7_jBSY4A2iy_Nt-zR41XT6iVDvxDtStX7zvmUYMxomDh65GHnvL16ayYkP7NDRDZXC_gB-73U_PKFT8crhqxEoGg7KFDrEI6z97Bfm9iMEEUQnQKWwuK0Crt8hfAOljqPCNGEpEJf5-wR2ejL38dqjg_kIN9kQBJrb-57HKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلش‌ بک به زمانی‌ که مثلث‌ BBC امان به تیمی نمیداد. چقدر زود گذشت دوران لذت بخش فوتبال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/30573" target="_blank">📅 22:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30572">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7922a3fb1b.mp4?token=oZcZi0WzJz8RsL74y0H3p5ShnzHif5vYQVS2gahRZxSrSwS6g0Wla-6t0kp8MogIHuqFCW4u_yhAS-mIGF0wHindou6hm7ARmBXzaXJ6852263zZDXbE17uu0bQWXm7UJUNFiimV0Runn-Hox6MjT3HpIdZggcm3ddaPyk1WvTGQfu5qBZGhYW4tD3MywgI7YSkgsQCGBIAELA0U9GXJuqFX2H_iKkovdUNqAgmDi1G5njrNK9JMTCPL0dh4Sn-E1YWkUlZxu76WD8dubT1LYKaABY3xl-Yh1De_3Z24VeafVCFogSVDx0B60URvnL6WRbso9OdT46028L-n7ng_AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7922a3fb1b.mp4?token=oZcZi0WzJz8RsL74y0H3p5ShnzHif5vYQVS2gahRZxSrSwS6g0Wla-6t0kp8MogIHuqFCW4u_yhAS-mIGF0wHindou6hm7ARmBXzaXJ6852263zZDXbE17uu0bQWXm7UJUNFiimV0Runn-Hox6MjT3HpIdZggcm3ddaPyk1WvTGQfu5qBZGhYW4tD3MywgI7YSkgsQCGBIAELA0U9GXJuqFX2H_iKkovdUNqAgmDi1G5njrNK9JMTCPL0dh4Sn-E1YWkUlZxu76WD8dubT1LYKaABY3xl-Yh1De_3Z24VeafVCFogSVDx0B60URvnL6WRbso9OdT46028L-n7ng_AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از این‌صحبت‌های جواد خیابانی درباره خواهر ارلینگ هالند در جام جهانی در برنامه زنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/30572" target="_blank">📅 22:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30571">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ln-eOs7GO8bxZIj8hdTQB39BLdE9kQQPQBELFMoe-h1TXU7Ezk_Gakt_ePRs_AP8rkvmFcTW33vlfZicYMaWj3xK0YojuoRnFL7WhOB5ylkWoZWPVxhZOmbO82v8zkeNNfcc9XtV60pLOrLxaOaeRrCHENAQfdzAP8Y13FoBEqNN0pYswaHpRQjRNz8wTMTE7SFYoFx32TxyDAq4vDdRLfjrX-WmYMyNGP582_BwLzWk0JAZ6zgIzMR_sarfDf7EdiGs3YhsM4Ota_YkJ5-xM-Q3gguqhihqzAlmmBiSH1VOPKxpT0pB6_IQ2Ag3EA0snRQVjMj63TCwa1TiVeestw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/30571" target="_blank">📅 22:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30570">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_vQKmm7Jk44qh_gP3iN7HgNIKIyVRTGfN__-ELAgAotRfN2HCHA8ywMONKDjCt7QDjgTAIxkupTCUIYxPhGdbzSzK2TYXqaTcJu796fB_opl2-0t62Isy8t3CSPfBuxHTwlk8Rxrsx_VG1-sZrBq38Dg1cjNtaG61MeLbrrtDrwaSk5o_ZO1cGl__frXtUHafktvoXHpmuarZQiEfdR3D5pV8OiRGq3L2-ahDXL2gHuvwJ1cw-P7XD7r5SwxsIS1OIE8TDnW34gEqCaFFViXbfSRm3ep7rv_MClYV6LYgw_GnE7bi_0XH8LfWaxtYm8Tk3D5yGQxBKJtXj-ADIPaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛دولت‌آرژانتین دراقدامی قابل توجه روز 14 مهر رو دراین‌کشور تعطیل رسمی اعلام کرده تاهمه‌ بتونن‌ آخرین بازی لئو مسی با پیراهن آرژانتین رو ببینند. حالا اینجا یادی‌کنیم از پاس گل تاریخی او درجام‌جهانی‌که هشت بازیکن انگلیس محو کرد. پاس جوری بود که انگار…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/30570" target="_blank">📅 21:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30569">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0GmQO66Zc1w8EkaffeYSJwC3iFBBCcHAbYyxaLUvAaT_sGSxcCMvfUnrR7AmY3qaPQQjmHhgc_6BAStgRUHuOdfX9JjLvPDTosbnye_2QgaDpvmLIOR_s4VVxhuKnfhEuj1rVTdLoFQfATrRRC-_ou9U2iMMgW5uX5ggXSayzqveWf5SEqa3-0xFPkZPRsZ5lC6hbRlKBytEBPCuxErfCH4rM8EfHHxAaXRnWvbIv3R_Mp8nyNPUxFtgGIX6COA3dwPsUsYtKyfTKgYIhk3Zx2x4lA6duax7Ttr577Lfoq4O8qEPqSpxqIzLCPqLQ2jcvf_Aevsn9YXJ0JyYoFQOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیرعامل باشگاه چادرملو اردکان: بایک مدافع چپ خارجی که سابقه چندین فصل حضور در اینتر میلان رو در ‌کارنامه خود داره در حال مذاکره‌ایم و درصورت توافق نهایی اسم او رو منتشر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/30569" target="_blank">📅 21:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30568">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKG35SrmdICwSLgiUMbkrljNtOzJT9vjlklxOP8xAw7HzKvLnWa59ptTMUq-kVU2ZfIiTCY1nELAtloUBpMTd5t5erJEzBlwrVJ0o2MJr5q-QSnsE3pBJ4DTt4SYjsNadIrHiqfb8d98ebtmw3ziC-mjXTOdbtaldhtniA2wuZUoxGIQI2CUqEppkbk2WNdu3_HMRXmO_JefavPiFOp2pQ_Mw_1Odiai8F8h7JF29eJ60cy8hD9G9u-CvwJ-2HijscX0GnTpfQaRuA3hzoP1uUycrlTAO8Q1NmAQr8XsxCU_P7O8YXUueHxHZFViJZG2fsfvn6LjOYZOgiHXtMhyoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ژائو فلیکس ستاره پرتغالی النصر عربستان: موقعی‌که کریس‌رونالدو به گل شماره 999 برسه همه جای‌زمین‌دنبالش‌میگردم تا پاس‌گل شماره 1000 اونو خودم بدم و اسممو تو تاریخ جاودانه کنم. با توجه به جدایی رونالدو در نیم فصل از النصر باید تو تیم ملی پرتغال این پاس گل…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/30568" target="_blank">📅 21:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30566">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_-JrhjHNh1vE7_gW156N1EspejFr5k6RDcAG-OECnxQdq0cp3cjegnFDlAS-XI4kcHbYfJKS8bpn0uPhlTrVfwaPQpfXpCleUvk6Wap2YP_6KpSgunjjbOqvx6bO_J3amZCQr6PmI0OsedB-pGJOW00Ca27rbEZCaH6cCmUVJ2JRnkCKS1hfOvu31ccopl9vD35zQpiI2lh4ZDzF19pdMex5JlmQvI1bg4lfxjsD2NfIja-ODDytmYby4FjYkHy5t94vf_3kyotSjEa2EqG8cECUQEKyKQSnqtzUJleJRHRxNgDoF30o1kVr6SQQIamKW0_IMO-iepLllNXnu1i2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mu0B7qIuSfILTXBQogkfMRwZ39lymYWHMIEb-Gs-J96G2fW1y_QKP3D6_C10cYGBcsK70q4AEnVhwZ21HKhDyhr3xOEpSrZ9-okgcKz3U54tRox5jpFLsKauUihOEkiTOQY8rRZc663QH3EopQfjX_boMvtuFswSz2FJHd5_fAb-nWGnz1YmPRaP5ZswejTETDJVmFzUVnJJ-OUClenSvrTRtAjmvFUEIELeQQH01N1GxB-TZbazC4A3YXKkI4UUNQyvJpsILlelqKs5l5o-lpLqV5V7I7eV3cZMW5m45HtRHeeRFwo-aI_5xhhjkseYTxnnm4X16CEg4DVGVhikhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه عملکرد لامین یامال
🆚
هری کین دو کاندید اصلی دریافت توپ طلا در فصل 2025/26
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/30566" target="_blank">📅 20:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30565">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6ppwF4MkgaKtFjo1r9nY8gVylUYmRwqzLVc_h-zvKLXoCfGRGfhwe2KmcIdgELQCLSt2MtxIt3o0wnWiRUlMdhbrbJTy0WryqyRigfuwzvhKT1AJlr0sAozmGZnvjw5Cg87EZb4FY3ZyrPnRusr7R_uLbGqrI776gmfHrGcPt3XfQ9QjnjTaz4BR5qQRxvrAaLSMGi7Vq-VxJeAH25ZSXdpSrcGPDZ5Zb8l09AVxPf1Zm0xNUatlY_BEK3M50cp0zx2aajpZ2Ty5IZ7sYHVckwTsuL_RoH7XfHVojdIZGI96rLdrBL6xp3Dg7oF5jk_pjCOhwvWw-4D5gv-ZIMyhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آخرین شکست تیم اسپانیا در مارس 2024 مقابل کلمبیا بود این طولانی ترین روند شکست ناپذیری یک تیم اروپایی در تاریخ تیم ملیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/30565" target="_blank">📅 20:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30564">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IshsGo2JGDTWH_J6Ch6kaVLjCoJUjsKHSC6U611QGw5fEidHv02uHmM67TV_LuiGqlzvqVEtXAdobM5-UrlyjRGwVNHdP3oiqBdKYowcFewxYo3ouHOePBsLBgWDvWPSbmQng2K76ectYl_W_Y6-GwHGQhOuRSV7K8bnCoPUdA-9jwNTzpUWDb0pnDGpwpMYFU45uMPatw2goL6kxTwWYYVDebD3h1MZ3HkRhMu045Lu1oWEgyve44a1K1powMgFEvmfv_mWv8YYZcSLn3ylUqcdIACWFaQA8xcCJXGlq2cq9fRsSy-mb_LcL3JQzR8qZLCEnOkG7lyFbdu8CrjNQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛مهدی‌تارتار سرمربی تیم پرسپولیس روزگذشته به‌پیمان‌حدادی‌مدیرعامل سرخپوشان قول داده درصورت برگزاری جام حذفی در این فصل سه گانه رو برای این باشگاه به ارمغان خواهد آورد.
‼️
مدیریت باشگاه پرسپولیس هم امروز به سازمان لیگ و فدراسیون فوتبال نامه زده و گفته…</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/30564" target="_blank">📅 20:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30563">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCtDP6Wgsu1tvFm3e7skmxg_WwVTrF3cMLZ3UHDEUBmwCbb_pL-4bTY2mQXsBOKlKot8Sl46_NcXdw9qyaIaQTpYQRDU6uY6_e4zsORRa2H0GIUt0Ru8QeuRX1p5flZ1cSenaTrNKVgtZ0wfvkb9dSN_dp4QxOlfDlk1aSWgLGAjQ4Jp6NMe1SInDDlYL15ShT-kMcoukNM2Q7VbF1D5OZBPNQFt77dNKUCw-qZZtr8wwY4nhNmpuLLwiWy2LrmYpzUENn6nvSvk1wx0T1jYlwixtu27P4m-YEUpDsRdf_d68Upl7BO6bmyBsDsMoS-qCaIu6pwnOUNdaVT3Mvo8Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول برترین گلزنان تاریخ؛ ارلینگ هالند ستاره 26 ساله منچسترسیتی‌که تا کنون موفق به زدن 370 گل شده گفته که هدفم اینه تا سن 33 سالگی به رکورد هزار گل زده در کل دوران حرفه‌ایم برسم. در حال حاضر کریس رونالدو نزدیک ترین به رکورد هزار گل زده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/30563" target="_blank">📅 20:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30562">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n34X4MzV2B_I-olf9lVisXADiU79WmSSFWdWu6BvkQQsrdfh50Bji1g-4Lj8oV-lNwsyvX6PhqICb7GuqfjLnKsYQi43_ysJqufCEWDVVUFhcETuquAePYN1K-D7R81JAzwBub0I0E8yJJaIM9N80vtX2gvjE-Vl_JB9qQJ9Sw8yfoeujkvl0vupZjBINfrFPBYV2yIK7kU_YjEjzST2lDH5hAji5G4MkcP43WyRVjKTkiGZBtv7VOHP3BXlpfEMmJuauvwkI7uLSFtI87P6z7tuzV0S7tcGlEu20kcqTLnizIlz8JczpYA4hr6cNG7Rqoc4yk1HstIrvKh9JJdhDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
حجت کریمی مدیرعامل تراکتور: هییچگونه مشکلی با اهدای جام به باشگاه استقلال نداریم و این موضوع رو به مدیران فدراسیون فوتبال گفته‌ایم.
‼️
رسانه‌رسمی باشگاه تراکتور: بانظر حجت کریمی مخالف هستیم و مخالف اهدای جام به استقلالیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/30562" target="_blank">📅 20:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30561">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQD0aBEcrI-1gKNS-IkrrmnsZFNl9WGpSQqxWoS1kLRCsWkqjgTTk-1U7wCsFpWixoSCMZOPqCvzqwZEBXZ4_IBJ3x0l1WCSICDzHZwuptm3jHsLUqKUQKxr-E_z4ZyVH8_pSWkXtV2nbwB3vllts_qWQxKtQ7stRI88kqX0xEAo4EWNG_zXUmWTynqtLBxH0Tuic9obqo5kCJATX262r4Op24fBDPnBuecgioyloiAX5wZizVcTtlPZnLhjbrO1SY4-1p6y_f0U0Feo7gV7zey3oSaS4YA4Q_0BPhM70xLPZdx34886Utmz-YdsTWmMdvVU8VZMdzH0RIxeUdPo_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/30561" target="_blank">📅 20:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30560">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sq00gD8DfgBuf3-Yy4i1hP27Q10H8EC9XmnlXcB9kvkapYLlt7N81dU1lhmcQrhnREwVLHukBIpa9BIXivy0xaDnGPF4pycmrh9HzDa_ovZS0kqpvc9UIUEVUSV6sgSnoHdeAQbgdJjz6dA9wt3hxqSuPkQI_b4p6QS6Ha1e4pR6rkIYC4qEitLxH_5cqInRspISwYrCTivLpTphudUTl17AEFde41RItqY7LgMJOtwI5GPKB3fEbb1ez5ILRP_KtVCg1V6ENV-bxskbuh3JrFbNM81kd-uugYCxw8twQ_9p9GWA5bAjMwNupUb4cp9xz3lHuFMbBN-iYxqmDqsTSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ال‌ناسیونال: اولیسه خواهان بند آزاد‌سازی ۱۷۵ میلیون‌یورویی درقرارداد جدید با بایرن‌مونیخه و گفته درصورتی تمدیدمیکنم که این بند رو بگنجانید و هر باشگاهی "رئال" این پول رو داد بند رو فعال کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/30560" target="_blank">📅 19:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30559">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76d469366f.mp4?token=kOkECJbWiQa2w9BZX-in-O4ytYQV1Ax2Ao0CIaW7vGemSTw9AWQkFAQBifJEVS72PR07cma3PYyjor_4D85wVlkXtujhuCwf9xpBq3GHhEk_fyDb0UCYK5ICf-vUDphyJdZUFryaEEaPEmAFBupRcSOOLJ7hXUkdyfzIsGcYMc8a_JFx6Y_XzZQbBNwPJdPzMBLv8K-LOrpUYZjw7vdRjucpR0wFTpiAYJIymkezLbTapv6JIYoJGAzWcNxHAftZzVLn-Re7iqnOY2p-wJeT7ohMNsqLAdHgtgPVvwSMSb9McWOt9P3IDkb3AEXZX4msYGqCIgd44AwPpE6Fkc8wv6v1D1pg2N9eQSdvqqDgWhLVYCz-5cgqcSXg3m5Vc0oelY4zXq2tOodzC4GWXRnnNjoI0yFBTzQTf5iqatl0ynEyehg_dSrS3-8CjhgNaagD9XDjCwRedvhyG1GtVJWyT-VAvwHdoPmY68-YAXe66PSJuUwQR3lb3LLSGK-cu8rd2cRwAb5i4BIJArBDEEwtu-M9ipnlsIzRb3XJUxc68QQ7MQ9QZkw5MZqod_3GWA4IRNUUfJxHL2BUUcU3TsrkB7YzzeNGKPc1A9uz4qpfKHK27KWWRe6tIKmHPHR5yOVnClHFOIpAnPsgTXT9-td5uhfLt98bFbb51biKqs88U68" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76d469366f.mp4?token=kOkECJbWiQa2w9BZX-in-O4ytYQV1Ax2Ao0CIaW7vGemSTw9AWQkFAQBifJEVS72PR07cma3PYyjor_4D85wVlkXtujhuCwf9xpBq3GHhEk_fyDb0UCYK5ICf-vUDphyJdZUFryaEEaPEmAFBupRcSOOLJ7hXUkdyfzIsGcYMc8a_JFx6Y_XzZQbBNwPJdPzMBLv8K-LOrpUYZjw7vdRjucpR0wFTpiAYJIymkezLbTapv6JIYoJGAzWcNxHAftZzVLn-Re7iqnOY2p-wJeT7ohMNsqLAdHgtgPVvwSMSb9McWOt9P3IDkb3AEXZX4msYGqCIgd44AwPpE6Fkc8wv6v1D1pg2N9eQSdvqqDgWhLVYCz-5cgqcSXg3m5Vc0oelY4zXq2tOodzC4GWXRnnNjoI0yFBTzQTf5iqatl0ynEyehg_dSrS3-8CjhgNaagD9XDjCwRedvhyG1GtVJWyT-VAvwHdoPmY68-YAXe66PSJuUwQR3lb3LLSGK-cu8rd2cRwAb5i4BIJArBDEEwtu-M9ipnlsIzRb3XJUxc68QQ7MQ9QZkw5MZqod_3GWA4IRNUUfJxHL2BUUcU3TsrkB7YzzeNGKPc1A9uz4qpfKHK27KWWRe6tIKmHPHR5yOVnClHFOIpAnPsgTXT9-td5uhfLt98bFbb51biKqs88U68" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
ویدیویی‌از پاس‌های‌تماشایی و خلاقانه تونی کروس دردوران حضور در رئال؛ زیدان در مصاحبه‌ای گفته‌بود کروس بهترین‌هافبکی بود که زیر نظرش کار کرده و به داشتن همچین شاگردی افتخار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/30559" target="_blank">📅 19:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30558">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCQV3rdXksS8gAPous77XHNtlEY_k7xuID13ewmGJ7rTyVlY-Q2lqH51UMKUwXs5imU7ltxWQQKXTkCW7noKpZk3hMoZkZiJj4jem4AWUmGYb4298JHowDp7P3akj4Jjy8BMaeSax83OWnSGHtDa2kgI5k8uG_q-JAFE2Q2BE_OBdyP-jMtGeMDFbROVtuQMFh57gdW3V8Ti5Osys14-JyCyRb15_CrhmwlgtDerixbbNy87QEnSjuuqdg6bCnnKA4PK4yMDYGPXtJGYR1_jflpA_0KsXTrAasRfka-5f44_lt83JoEnTsZmmvijv4nV-I0TPgx3NVXZPF7B62epXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ سید حسین حسینی اولین بازیکن مطرح تاریخ لیگ برتره که برای خودش فن پیج زده و سیو هاش رو باتعریف‌وتمجید ازخودش تواون قرار میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/30558" target="_blank">📅 19:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30557">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYNjHkdGJRtHMAWKxjZ_Ur3S-VDj0B5dwpc5yVDslNWSN5J9E7Yt_euXFM6rdSLRtyGEroN26No6typx28bND-FzNdM7gzRPUq1AZD7o5zR9UJsMVYWHw7tVeBCR2ST1MWUDuwwucuXoUrkGLNZ-G-S3dvUCkV3twAi1UtT2tnlld6BBrGJ2has3vmm6DTFDYj2jHHhhcXilRsLKQ3JP62Ai271Cpp6yYhapeKmvxwJYjd0PxLIKOY7spG8g7JCVkWfQ7XV3FVYI6oAAntp-XkC2ds6DJUnYfeEIFGxSmnSjqTwZgpd7efeGC7vllP_FVrkjMmEvY7jCQjZoQJ2aOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌ملت‌های‌اروپا؛پیروزی‌ارزشمند یاران لوکا مودریچ و کامبک‌تماشایی لاروخا مقابل شاگردان توماس توخل؛ سه شیرها نتونستن انتقام بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/30557" target="_blank">📅 18:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30556">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7389e745f9.mp4?token=LGHPS1XezkZIw8xxnYl_OcneG3F8YIMhiJ6Kbgpo8licJ5AjqymcHRmXBoYos_HlOliplujjHkvKDHDFi931R00kg-HQC2XMfnfbxfKcrQ2VSbC-WBhFpoSuM1TV-0jwzBGT9hZIkBcCrVlNwbSKZvZ1VwOjhhTcCF9D9Zi4NdcHyYRt6-_vbMqp9gCjeLB_hvzn-1-7MCg9O4Bhd-Q8K7oDsLWnZgPfe9z9EzTHssu5Z5nhjWp810rEAfym7OYEw8sPEEYDVPvlssM0zQ-ArOZKpix84Xot410UUqr1FetaZaQibd7__3f8m2re5ekPatV5l0S48Ex5I1qEcPCkCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7389e745f9.mp4?token=LGHPS1XezkZIw8xxnYl_OcneG3F8YIMhiJ6Kbgpo8licJ5AjqymcHRmXBoYos_HlOliplujjHkvKDHDFi931R00kg-HQC2XMfnfbxfKcrQ2VSbC-WBhFpoSuM1TV-0jwzBGT9hZIkBcCrVlNwbSKZvZ1VwOjhhTcCF9D9Zi4NdcHyYRt6-_vbMqp9gCjeLB_hvzn-1-7MCg9O4Bhd-Q8K7oDsLWnZgPfe9z9EzTHssu5Z5nhjWp810rEAfym7OYEw8sPEEYDVPvlssM0zQ-ArOZKpix84Xot410UUqr1FetaZaQibd7__3f8m2re5ekPatV5l0S48Ex5I1qEcPCkCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
🤩
#تکمیلی؛ تمام85هزار بلیت مسابقه خدا حافظی لیونل مسی تو چهار دقیقه به فروش رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/30556" target="_blank">📅 18:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30555">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxFVB4vIaP1pggD2JtmRIBrxplV_LsDrIUi44_I7jdO2V1K3gAvZiVV_lS-gtesMV-gLsdmZGmOeP9TshGE_Nq5PxyakMNaZxqf4IjzW_NxvA9TuNRcRYC-ah2O3_6UUDw3WOam8DfIg3-L7LFLqkXHrTxyrklhmFJ4CUxBpU6KuYRcpwT9TntT1Kx0kgv6r6i6qUnoh2dKoan7KAEg_vyMVaq1RNriRoIQHyYpvNNNNmB8Ck1ScM-u4jqRMcjSM7t9ggWwaBxrnCsqYNT6x-D4bRw0zKBlRjHQHRR64B2nD63gHgkUhwDddUFm__18v7QCoxyRNRQZGRIlSmB5LQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه گاتزتا: روبرتو مانچینی در زمان حضورش تو منچسترسیتی دوتاقرارداد بسته بوده. یک قرارداد رسمی با خود باشگاه به ارزش 1.69 میلیون یورو در سال و یکی‌هم یه قرارداد باالجزیره‌امارات برای فقط چهار روز کار مشاوره به ارزش 2.03 میلیون یورو! هردوی این باشگاه ها…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/30555" target="_blank">📅 17:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30554">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVoNXAh7QIYC9wciXON4eQW1N56uG7tuDMTt1MvKZlqyQ6_Fevoi_91QCpwfih-4QCL7KD7AW4Ms5n3ZEPyfXzjUdw496QwySKqDhe7EZVy1xolP5TaAgUxXz7v99WT3EkcZ8cYjPsPdOisM02wi46OhWjh7Y14O2YvIPLYkKDeGdjB3cRM0xYZWhUG8JzsEtucFUG0zYZrZV0Ujq-Av-mYVY7gNFvDqlc3-nUDXiyWXP5gdbg2-bph7j9oH2uJ-z3DheetylH6fZGosRXFLmgdm44eQINjykzQa0hksLzxacL1D9asyxzI38CNygCLbexjG3WiKxvl0KvV8A14iUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حالا که بحث تخلف من سیتی داغه یادی کنیم از 3 فصل شاهکار فوق العاده لیورپولِ یورگن کلوپ که زیرسایه قهرمانی های منچسترسیتی پپ دیده نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/30554" target="_blank">📅 17:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30553">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krncJDph2zQU3402ZGIFYg9av82j6DIx5i3sOnQM5-Z4zrXpX7j2ffOT3uqHNVgE02rONSWaUsh3ithcaAwyvSVMCsup7fbkTTvQ2HsamYmdvUVUuPJVDgoCun3dPky82hGxDkrQXldRtAQViFynFKIWBLk0qvc_Ocn9cWYRLbAHXjJJv5s_K94Ckc5E04NPhsetH47kh2r_rZxJv_uY1Fx3SUL6pka8fnZsIydwQxnZV3sQB1fHn1a-jmuDB32mcyVXUkEIwDq4XFEV8EZKOWOndseTsgYbINM7ic4MlqyhSZ-C_l9CgFxjSffatQCfO-jQ5AHohKDWejtdampFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
سال2014
: کروس به‌رئال‌پیوست‌. 8 هزار هوادار رئال مادرید در سانتیاگو برنابئو از او استقبال کردند.
🗓
سال2024
: کروس با پیراهن‌رئال از دنیای فوتبال خداحافظی کرد. 80 هزار هوادار او رو بدرقه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/30553" target="_blank">📅 17:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30552">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vs35xb2OKsvMFPGuYvM0S7uYiM_3qzWWzlBFX05xIMqNSK-MrAsmpn50TV9H5Y2Siz965C6VQ9uAQLe2q0iAlyb7MjdQeAn2o4fQVnztEr2uXrac7-Ljt-hCyuvpilkTvbULloi8fzCFYZHkv3SQI7FOIFlLUci1puKTSgq9HX1Af9Yl-1zWqUs6t5VVgaQWZ2KQYmR5LSlAZZPKgJJ3K6I7W-tm3_b8D7UwiOvJStGnGtgOpizZci9M9fSEoJhTHXfF-V4HpRjasTuelmdg0Tv25HXmXka0NeoYuG1V3L5tHLK3GiD-CMsSnNVsmUPL-lHo-SrsLX2jyJpj96FcJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آخرین شکست تیم اسپانیا در مارس 2024 مقابل کلمبیا بود این طولانی ترین روند شکست ناپذیری یک تیم اروپایی در تاریخ تیم ملیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/30552" target="_blank">📅 16:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30551">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFNY816gG9GwlA4koRwSRO3wl1l6rVoUqNqDtnT5v5fET_CgoS8fWfukE04WcKBszrJFKvur9i7QFuaXCPa_bTlAFgt3RHW0XSxbaJlyq00SM3MDL5pb7GfUpQ9syuuu_wyTEnWBs11-IUwy_FHRRsZUZE24oODPsS8rN14_GDrhHT7E1AXXS1yE233GEIDQUtPCa0LMbnfxlbrpD3VSBWDBla-2qlnKfv0J6NXk4_yu9OF4xV9MALE82yjr50VjzXE5tibOdH0jwlJtMSisObEmHKp2o7mQRXYOqNygIgPfSLIimcSdYzlzKqdgFV8T5B3fGplJehaAunaQ6Tx8Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جما اتکینسون، دوست‌دختر سابق کریس رونالدو گفت که بعداز جدایی‌ بهش‌پیشنهاد پول داده بودن تا علیه او صحبت‌کنه: وقتی‌از هم جداشدیم به من پول زیادی پیشنهاد شد تاپشت‌سرش بدبگم؛ ولی من قبول نکردم، چون واقعاً هیچ چیز بدی برای گفتن درباره‌ش نداشتم پس دلیلی هم نبود که ازش بد بگم. هنوز هم کریستیانو رونالدو رو از صمیم قلبم دوست دارم.
​
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/30551" target="_blank">📅 16:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30550">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‼️
#تکمیلی؛ مستر المپیای امسال قهرمان تازه‌ای به خودش دید. نیک‌واکرآمریکایی قهرمان مستر المپیای 2026شد. سمسون‌داودا، درک‌لانسفورد و اندرو جکد هم رتبه‌های 2 تا 4 این مسابقات رو بدست آوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/30550" target="_blank">📅 16:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30549">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUIjWO6nnW0odS0FHaouc5_06G8t9Jyn2ctvKkpJk-WQuCpS3i7TFWXyuQBJI16VqJWz5jJI7fcs37yLh2-OBCjj52VhMim5ZxXtdRnMZXSyk7_jYU3eZ2_Hor3KvE12CFhmbZuC9QCkIu68Qr4XejKLSBFV9wq1yc2lpq0q_oN0TJ6WceYjl7lb4P1lQfKZGNTGGrsrXe0eMF0sdHrshz-Q1K4gepBjFkS0lT5o3Il4bWEikfTxT0mKEJnmGzPlh8aBb_jCVMp9kB8Pb3j7cwk7XyRFOOmQJf3F2__hAKkcyn0KpGQZDXXWOLGkMuvju_OTV6G6bGtuE8amSAgJpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
حجت کریمی مدیرعامل تراکتور: هییچگونه مشکلی با اهدای جام به باشگاه استقلال نداریم و این موضوع رو به مدیران فدراسیون فوتبال گفته‌ایم.
‼️
رسانه‌رسمی باشگاه تراکتور: بانظر حجت کریمی مخالف هستیم و مخالف اهدای جام به استقلالیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30549" target="_blank">📅 16:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30548">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8b814e56a.mp4?token=DVNB5AZdVez3AHB_aj0uMReuG9cPsdH7_5UISqG11f4WWan5Ue8tYkhr1Dz8TQcRRLzPXxyGjoRlZe3XZHuIBPF-RyvHYALVHqFwakqAfrvPblWpVTlAWe_Xpko96YSSYmUCzH7YktZBbtPQRg3BC4RXLZJWCxs0LQLJv18lrr8Wj7Iz3joE5iJAVHMXy0Pb5cmsbzuzUVIOYAjFTdVcNGL0EGy8446NVsBJpUqlnFmh1goIVQDaXZAC4CGqTDsEyM7ZKX4MhZLuvH9wLcERbol1GZvU_6pNlv77b4GdPXopia-OEPPeanIYN2hdf4b0Ed_bVKD6iUmX-_i1D3qCAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8b814e56a.mp4?token=DVNB5AZdVez3AHB_aj0uMReuG9cPsdH7_5UISqG11f4WWan5Ue8tYkhr1Dz8TQcRRLzPXxyGjoRlZe3XZHuIBPF-RyvHYALVHqFwakqAfrvPblWpVTlAWe_Xpko96YSSYmUCzH7YktZBbtPQRg3BC4RXLZJWCxs0LQLJv18lrr8Wj7Iz3joE5iJAVHMXy0Pb5cmsbzuzUVIOYAjFTdVcNGL0EGy8446NVsBJpUqlnFmh1goIVQDaXZAC4CGqTDsEyM7ZKX4MhZLuvH9wLcERbol1GZvU_6pNlv77b4GdPXopia-OEPPeanIYN2hdf4b0Ed_bVKD6iUmX-_i1D3qCAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ سازمان لیگ مجددا کارت بازی علیرضا بیرانوند رو به مدت یک ماه تا پایان مهر ماه برای تیم تراکتور تبریز صادرکرد و این دروازه‌بان میتونه که در بازی هفته هشتم با استقلال تیمش رو همراهی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30548" target="_blank">📅 15:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30547">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnvjytxZ8GFREhe0-l9mJTAM_MNWpzCi-V647q2B50YsFv8_7v7KfG-heS-y1EVmpAnwnlBEuJYwmcOTLIdsqkKpsgkZrreZPiJ61HTz3A8-tlACZJq0DYu8ryEi67urr01XWHOve2cV63P3-sMTStBuSRVrdhCTNsJ9lBlZ0b1HGzmBiJwE6fW0j10yrRIy8joHLncEt_iYPKsGqUwF-zw264rwOyEyzJQzCMWdgYSuYkswqemiXDMzNdnqkQNaIlQh10cCJ4jiRI5gXxenWMWH5sedM_qZ1TxlA0jHhJDPT8plDN5O0u78NhFUqh0BRwn0XRfZp6G-PbpW1XsT8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد خیره کننده ژائو فلیکس ستاره پرتغالی النصر دراین‌فصل: 17 بازی، 15 گل زده، 4 پاس‌گل، 9بازی دریافت‌جایزه بهترین بازیکن زمین، نمره 9.1  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30547" target="_blank">📅 15:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30545">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k8PxtsqpRS_dR7vuX6E_B23qVM6Y0VYUiEmV2YUhXQZFEJ8SxOPT9DYRIznpni-OEuzV-7YG_ZvS1bmlHqbST5lxTVBVUN7T76b8mcvfeC0qihOrTEuoyoDqTPo-WxUMsOlybfLyXLycXaObsYl7fxoL0xd181sjfN6POkyR8rhUC7aZbVeq3f07HOgjJt9L47iBfjp0MbEURIbK6i4Q8UbuufJTlPwVdOktCoFpEtgyhu7MXS4jxJuzd23geP55C0EhZb-IXItJzC9F7Ysj_vucyMTMds-Ms1Z54ik_rz_J6gpoFMH7u8GD9b83A9acnD1Meeyt3-alT8XfvxzvoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SRpZ-ur5LnOz18IByL_VbDmnnuRhYPad0kqbSCC2RYJH3PMF9iD3Q8Afh0Mcc1jb7Wj0VQ9cVCYS-FE38SITjrHvMP0XLJgkFxAM14UYHdJGx3GZ3jJGlSVtyXHwMjl_ggSLU4qWs0XwzOOpYOPeLp9aLJg9k23HyrL9RquUlDiYgCjc5myolbUNGsmUsDLj2VdjAufMYoiLKo8_LP_SXmidN46PQ4Ih-I1vRf4BhSMjrcPwu_E63Mo0F0P_ln36_WxJGi4IltILJaR2qx9T26IpU-ywL7ELwxiiIPu1GAjxsvANPZsuXVHyuOlL_UCURwrE2Y8LHYPeKJWG_Rpuxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ اسپانیاباپیروزی 3 بر 2 مقابل انگلیس در ومبلی، هشتمین برد متوالی خود را ثبت کرد و در این 8 بازی 17 گل زد و تنها 3 گل دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30545" target="_blank">📅 15:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30544">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C53bDhRV_1G0eZDsxSU43AxMYTt-zkrePN4a2Qo3L3aP-m7BQKuMGHjApy0P3GxDm3eWiZTCnTu7S37thmnCbKkrax4wZOvNrc87Y5-cmz42CcWvg8NrXt_Z_-A9dgDEroFUMj7cHqiNNXlqDtPLVGxn92oBHlgJ393JF0SXbQ20RsNIhLLcEl74VjNFOjD0XTaHnI-jBjN1QKVERYhmSI04ZNJOmD1GsaR_ZqOxz3cFHP3BNaetwIhOeinfjlof6oEf8gf5MPILsjG8s_FaXotzVgQi1ZeYJn463Epk6850WAwX7HLufyGMliQfgxkVCb998no4QnPIDx8wEzKkGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ تاجرنیا پیرو خبر اختصاصی پرشیانا: فدراسیون فوتبال صراحتا به ما قول داده اند که جام قهرمانی فصل گذشته لیگ برتر رو به استقلال بدهند و ما منتظریم که فدراسیون به وعده‌اش عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30544" target="_blank">📅 14:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30543">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKB16l8LtLenIQfSxpmQvtrzHyL59LPleTC1h_yVuXo1jdlN3wGqhasdSzBZ4DAvjRy40F3rxjI-B9cISEcAQu_KlnGRBloGlKcMEv6tA7H5HMNKDLUKJcB4LoKOxVQI_jxZTZWS2Mw0MJnvNGQXf_X26E2X8BhbkfZrPgm0WMNVT23S5_vu4K97kTGoRKmhLqsI_LsgBBqTOsVRqVds6RA5uCwEgoJFFqFepDUMGk3LvTRG4Mg5RZxx7k2IS2LaBGHtWJiqc8A9Jm8XE-dOFrrJ8PKIT5HT1bXd7GJ4JuhC0SGAfKZI-QSNUq5hEc3C-IhhbvyWFtBsnNppbagEYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تابانی‌به‌فینال‌مسابقه‌مسترالمپیا 2026 نرسید؛ بهروز تابانی درجمع ۱۰ نفربرتر مرحله مقدماتی دسته اوپن قرار نگرفت و از صعود به فینال رقابتا بازماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30543" target="_blank">📅 13:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30542">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc0fcb29e0.mp4?token=s5qNO1h4olFrhvnLDKHBzJ6ZSo7j-DhOvZEr8JvNJ3Ng8mYKVRXVWkKRL8W-jTuOaEEoZOzLWMTctSGLQsrgAXeY-gjBvazAtnj_PXQIMGi4-3V1XxXt9ifEdf0hCnbEEfTh30Kbb9RfBfHt4S3E4uhuNmXEf1pePSdPhKoLK4XMmtBQVl4DdUfoTo_0ghVMy8LcAQ1V1TeGHKOX8xlKs1A6beSBW_pF8AmsqDSvGZz0DaLX5EhCgdTdZSFtnffs2HXxX597Vcimogl6gdRhaTjtyYFOnUepERLNvbE0Jd7ChYiXZfPupcvuCmp_YIomx_EnojiWY00FAUq0klhr5pgUR3V3VH_PSScQdUr9625GfNsbVypsuZXMyVB2WLgUfIEdZyIHWin_aTBq6wqoeuGBGGGwqhQ2gmye3pg2yleiERgBbuBvUPn5sakVHoq0JA0cB0-Oi4GtCnEr0wc6wkKTRzKGQZduQ_iDSXW_FeE96Jq8D0vS80ym9BpgxdDvdrQyzmyAGEGH7XS2sxWuK9b9nrPZJ3MnCLc5FanIlvhvM49F1HH3XrHBnFOoh_LKofjK5C0MBRJZ7ePwpEhrNuH2quafAac2zDvGLB3ye-RZb-101b7Zvc6bOLddjKG3RsvfDo-bHfICSZeKW0ZFN9Qrk1vYJT-rIWs0surS-CE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc0fcb29e0.mp4?token=s5qNO1h4olFrhvnLDKHBzJ6ZSo7j-DhOvZEr8JvNJ3Ng8mYKVRXVWkKRL8W-jTuOaEEoZOzLWMTctSGLQsrgAXeY-gjBvazAtnj_PXQIMGi4-3V1XxXt9ifEdf0hCnbEEfTh30Kbb9RfBfHt4S3E4uhuNmXEf1pePSdPhKoLK4XMmtBQVl4DdUfoTo_0ghVMy8LcAQ1V1TeGHKOX8xlKs1A6beSBW_pF8AmsqDSvGZz0DaLX5EhCgdTdZSFtnffs2HXxX597Vcimogl6gdRhaTjtyYFOnUepERLNvbE0Jd7ChYiXZfPupcvuCmp_YIomx_EnojiWY00FAUq0klhr5pgUR3V3VH_PSScQdUr9625GfNsbVypsuZXMyVB2WLgUfIEdZyIHWin_aTBq6wqoeuGBGGGwqhQ2gmye3pg2yleiERgBbuBvUPn5sakVHoq0JA0cB0-Oi4GtCnEr0wc6wkKTRzKGQZduQ_iDSXW_FeE96Jq8D0vS80ym9BpgxdDvdrQyzmyAGEGH7XS2sxWuK9b9nrPZJ3MnCLc5FanIlvhvM49F1HH3XrHBnFOoh_LKofjK5C0MBRJZ7ePwpEhrNuH2quafAac2zDvGLB3ye-RZb-101b7Zvc6bOLddjKG3RsvfDo-bHfICSZeKW0ZFN9Qrk1vYJT-rIWs0surS-CE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
ماجرای بسیار جالب و شنیدنی سرمربیگری دلافوئینته در تیم ملی اسپانیا؛ این ویدیو رو ببینید برگاتون میریزه که ایشون چطوری سرمربی اسپانیا شده و هم قهرمانی یورو رو گرفت هم جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30542" target="_blank">📅 13:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30541">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5d8oqfWu-ixP-vhsNRSSR0jJo1xG3ZGDST7EJ7s4wLDqPTZPZe0EdaE9xkMFXhFDs3b7wk3Jdo7oq1Aft20oKo46b_65Iq_r4pa_oShMtR-D7LTfxu6mbohEYGSB1nIDwFdYi2MTqtuVCelzNq-ehi8PRKraSBfWL6I8yaUzEPNzo-7Nn2VASVV-v8O1EuvcR9SKD8VbecxsqhgO0dGx-WEJgrInOAxkffQyJqb61dX_AqktiefvzaFImDMBif2sif2O_MZOknIsso6NBABmQkgUTsAjgF3ixiWYn_gt0ZeJRBZz23FfOyDnfi5Ri3pbCUBaJ9rOo3E94cPpqrCpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌ملت‌های‌اروپا؛پیروزی‌ارزشمند یاران لوکا مودریچ و کامبک‌تماشایی لاروخا مقابل شاگردان توماس توخل؛ سه شیرها نتونستن انتقام بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30541" target="_blank">📅 13:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30540">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZR0gPiP027PM5-3tmKaE54fw20t2WbIKLvIJPNXyfARfKJb8tf0peyqUipve2CW2wOn4EJeW264TuxvGvd6LeYXaOQVxb_c7hwujPbr456BbgqnQcf-A39dL1yCsIW7fRh-qXPhXRFyYCEp4T2nagH8WOSPwGSjczfNWOlLKL0hhX-r9K5aVhYckEL8Xx57rvF-hkOqwq8zFQOXmqkirk9ZFBVfF8kOoDbmrIPhc_R_68D8PwtNXj_MQ-xfBMO5njhs0uyo6vTR5bDWSLqdUDyZpFo8BEIeo0VqvltKxqx-iGB7hqavdFothG0-6jC0elykQtQ8DNzFf650-7nTBZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛علی‌رغم‌اینکه‌فدراسیون و سازمان لیگ گفته‌اند بخاطر فشردگی مسابقات لیگ، فیفادی و لیگ نخبگان آسیا احتمال برگزاری رقابت‌های جام حذفی بسیار کم هست اما باشگاه پرسپولیس اعلام کرده حتی حاضر است بدون ملی پوشان بازی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30540" target="_blank">📅 13:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30539">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9a7ecd973.mp4?token=mALj6g1IxBJoxOG-5FOMRz1lJ4Zy2fS4ggrkYQuBQwyYaa7eVoDgVcI0lqeawFMo9wJUUQV51ElaXpdzGRd6EyUD1lLzYm8VvCWJ6UU3bbPFaXizOdiPvT52--VrNBvsgcrQD8aoKldunzOrMRVwc3tl6lDuowHzNtefXKr3GV0xshjefOPqme7bCWHXBA-q2UHbjl_v7XYaivEk1zPrpH2q7HHDZN7WRMGrjPO4KFgRmvepYinlM2NUis46oHH0SaXScwhCQ0i4f9l5OxWdE4VHaDavmRvjEfWSelLfsm1F9eSCrMB9N1GckwvI6wQZGmQotUJiNQUGor7IlvAJKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9a7ecd973.mp4?token=mALj6g1IxBJoxOG-5FOMRz1lJ4Zy2fS4ggrkYQuBQwyYaa7eVoDgVcI0lqeawFMo9wJUUQV51ElaXpdzGRd6EyUD1lLzYm8VvCWJ6UU3bbPFaXizOdiPvT52--VrNBvsgcrQD8aoKldunzOrMRVwc3tl6lDuowHzNtefXKr3GV0xshjefOPqme7bCWHXBA-q2UHbjl_v7XYaivEk1zPrpH2q7HHDZN7WRMGrjPO4KFgRmvepYinlM2NUis46oHH0SaXScwhCQ0i4f9l5OxWdE4VHaDavmRvjEfWSelLfsm1F9eSCrMB9N1GckwvI6wQZGmQotUJiNQUGor7IlvAJKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای بین دومجری زن‌ومرد تلویزیون روی آنتن زنده: دفعه آخرت باشه که اینجوری صحبت میکنی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30539" target="_blank">📅 12:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30538">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U55gWnKBg2vrdwJkFg5WQB5w7g6iCr4hbapusRv5SXjyY-pNPtCHExgRBsFcKx8l0iwxvkKCgw24LAUTHYvcqLdGZEdKujuuptSj1_Fu-sqOK4KHYtYM7_jasMZbSmMU7kMv5KwAABfWgWh1-32xRo4PehgWnzOQzHBe3bfv1vWlcx7xXZ1O-bjG_-dKCmMwYWxWVrkdoeeC18cgqZLQDceZ_h4Uxnzp_WrALhHpmI-0sWhZX6zwm-8-bmYe-en9g7e-6c4EAIhzLP52rf1mn8pFFY2ALwNM8O6OU_5dcMFb6crMsoYfC9LRtl8MZiPUfds6j5I9jhIdDEBlR7SDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ فکر کنم تنها کانالی بودیم که بارها گفتیم که رئیس فدراسیون فوتبال به باشگاه استقلال وعده اهدای جام قهرمانی فصل گذشته لییگ برتر رو داده. حالا هم طبق شنیده‌های رسانه پرشیانا تا اوایل هفته اینده فدراسیون رسما در بیانیه‌ای استقلال رو قهرمان فصل قبل لیگ…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30538" target="_blank">📅 12:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30537">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qU6J7Sm612wVK7mqa9sfcDGDGZhYhfvZg0X2lCOgpicozCfKA_Xvbpt8YDSlohefM4HpVG9wlH6twX62VlZil1hmMenZ5PfO85QWCo2qsTpST6X9JodphYe02XiFoIKu2W48I4tvsPUtbAmCKgPkszuhM2A8DE4Gl7jd2mGHT6QndJRG1IOkOrM70KSBBL7cB1g6pmowk3YetrGikIhHgMLMDhPPMyQT36uaIW6_Bne4LhzsrDBnjYQWhoT8i5zlPKHspqpdsecd0QiEHXnf0bZ9zKvxBp6wfkKFCnQYxBuGdnYKT6nCuGJ2vI4dt3tHVxOOeZnsPrTggzVCopkerQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حاشیه دیدار دوستانه امروز؛ کنعانی زادگان و ابوالفضل جلالی دو بازیکن اصلی پرسپولیس دچار مصدومیت‌شدند و اززمین مسابقه تعویض شد. هنوز میزان مصدومیت و دوری این دو از میادین مشخص نیست. فردا بعد از MRI مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30537" target="_blank">📅 12:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30536">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">📹
👤
شیدا مقصودلو همسر29ساله خوزه مورایس سرمربی 60 ساله سابق سپاهان و الوحده امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30536" target="_blank">📅 12:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30535">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epDPA3Lvio8UV78o7Vch-jdE5djclQIV8YUID5EhnVL4115oKaZl6wcAcEsajzT7Jg_YNpbI_EQlNJPXJzDTggK7c9Oah7uAc-Is-nev7e9mDOgkGHqQzhkQCdo9Wda0wlRV3XJRyLaNPlr6LsSDgVNMpPt8aMlK1qjrq4GjcwwL_7tuZ9jLhfAWu_BiY1o5jIRlJoF24tPWvVX0R-f8jAjy4MuZnv8bafnBE1Q55-87rPIyJYppIqwvJAo2WkizlbITbETnQbvqMf9HL_fGEyKaz3th182TJSStoX10FLfvkB65SW7zmXH32YB44QuvRWJnWsx2BUOOeAceN7s5-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
درصورتیکه سهراب بختیاری زاده تاییدیه رو به‌مدیریت باشگاه استقلال بدهد؛ سید مجید حسینی مدافع میانی 29 ساله تیم ملی با عقد قرار دادی سه ساله به جمع آبی پوشان پایتخت باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30535" target="_blank">📅 11:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30534">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MemGpLP-fOSrhR3eK3SwcLS934pk9D2n2fklxlE3TfouhsIWW7xvMoScMUKPgB6YZUdKqwn9jOtTW8xy-uFCyHbK7Foi3uOG9ZFxpQ-ao5DyNavYoHmqfT75Q8Vgro782nQv3ctGQzFmaDLWKr49uzzHWZhE7BmCGXE9qGfrDCm4TTtiV1rVn3tJR5-FJ0nYnVIX-QlA306-_OOskiEL3TPA6Ctr6Btd2P0ZWqAlPVcskEz87_hIStgGgr8ohwasqrGjtyydLeG-IQ49coavN3p649YI49mA3e8RfSFIlShCtkHSOTlNUSbNtQdScgHMO9jUMcVlZ-ytq-4zzD1ppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو بازیکن تیم فوتبال پلی استیشن ایران که مدال طلای بازی‌های آسیایی روکسب کردند به‌ عنوان سرباز قهرمان از رفتن به خدمت سربازی کامل معاف شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30534" target="_blank">📅 11:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30533">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJcRTf_oD3uu_yXWCESfZ4sSu4h6MGf2npfLYCiD9HAXkIJdgcrxNg2tLwgg_Qkmrxm6pSN_nfhqfdmoNpWO8DD4JrQeHNA6LB-jBMXyiBKPi05v48UPk7gUygsXz6raswP0U84J9APj957aTuduFt2B6-h9fWF4iyLWtsO62kuzLEJu0fg9LNT-g-yPcq29OKUlyGTjE9QH6bsDYNvOJ1ImcgDwosND_8b88tNuzafx-8aN53VCopd9lOadcyFGSkcvUPcFRCv3TceOWDY4_OD0cw4H9BuraDulVPcZwofrwfLz_sj-N56pgxMjBYIrRQXTLhfGoplE45I50I-Q5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه عملکرد لامین یامال
🆚
هری کین دو کاندید اصلی دریافت توپ طلا در فصل 2025/26
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30533" target="_blank">📅 10:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30532">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzw4bHilAazW_xgdECaepV9LIDqOZyt8KYRdUerwVO-7FJHx1xcqSxquDn44FM8ONqZt7rsI9GY9YRW73u1IXEbxQ7VY07n2py0dmEcczic4c9CaVnm5lJiW6Dl0knYKWLOMm8SL3TsEr_PLhBun3d94O2c-kIsTjq0Ya5GLMuDeXKQ9Sx9lAQUJtikwOFNL8Wh5vyyJTwg1YYlG5TQ4anTxyzIPfU7nS2I22zJoKfeyKxYL20h3sxLXkvy-eEjd7Lyv1LkOnK-BkukPvZt7Mqg0A_dshC6ETkGFDSBwoaIwhfOQHqU7vl6XcGmcoMHLGwK7sVsCkYnWcDXQcXS8mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌جدیدترین‌اخبار دریافتی رسانه پرشیانا؛ اواخر هفته‌آینده احتمالا "چهار شنبه" باشگاه استقلال قرارداد یاسر آسانی رو سه ساله تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/30532" target="_blank">📅 10:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30531">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3Hhsp3ssxerXlooNLQtzVERGps2h476buGu_qT1-L5zfh5zg5Y72xn4Q-X7PlA6EAIuUDAL1Rjl1pJE0mkZMHzWsgGWE3cnKeL6KZR8AxmALHt05jLl7aoRJCQsxFC4KaV2PjouW1sZc-GTdAFe7khaikelZf6q37kYwws2HAVlyfpVmlQV7c5KJp46_w8JW49NduDPUgLSRKE98dW_ZFt2xmfUYCblY1ZgBJKiMbpITjnbai_-SGN6D_hfB6_AsZ2u6Xybc3ZRPUef3byTxlIXQTNUG3jlh0nKOlppsjLiT7hJieExdf5at5eZF86khAazqueO5wBPh3GcHuO9pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
🤩
#تکمیلی؛ تمام85هزار بلیت مسابقه خدا حافظی لیونل مسی تو چهار دقیقه به فروش رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30531" target="_blank">📅 10:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30528">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZlNF2dszt4izrWPSABmwwB__0KEQod6q4YWYMfhfu41r16gdC5HZZH5v_OencQ2BlCabhR6zz3wkb_Ktr9m20qLppmsKMA-9p1u4MoRQbpHmhBE-SO8kn5yIZSeU-uMTkWngrFessSDjES8lYDrGIs9zJ47N2qDwp2T4XE_I95ZJQF8hhXr5w4QubQMc4GYRlDudzJN21Or-50zcCV5Uxj0-sGYxlB2Nk5pQjvgbmOL3YXvp-KrWyAydguKDa9BaEl8py6dmbTc7Eo7GZpql7PmwPWuw_wgatrHgWOxaBKSJjLJTMTYE13N13ivWpntvbdQWWivJII6StOtG8O0bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیرعامل باشگاه چادرملو اردکان:
بایک مدافع چپ خارجی که سابقه چندین فصل حضور در اینتر میلان رو در ‌کارنامه خود داره در حال مذاکره‌ایم و درصورت توافق نهایی اسم او رو منتشر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30528" target="_blank">📅 10:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30527">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWgHenEVR-b8IwYrAe7MMV-_Yjw4zuUhUYkh3L19XM8vQcY7TEzjiO0uWahr8L9HWHLnRixicc3R_RV5AFwheGy8vhjBXaxLv6yXk1CU7VUbokoChUykgU5XPcy_XBUEPOSvz-7tNjJ0rpw9-Qjlfx3qtJxf7i0mZZ-Cr--BY1P15I-87RuiRH8PkRb1P8lqb1DGie9lcoiaaEFwNKFdYFgERfNIR4_l6_Ofj7otfHLONDUllGCu7tD8-Ef3SK7lVwOaTSFroZ2zjjE63SEmZMBJytbdDm4bmAKmkbGwFj5MHlbl6sqJpR0WfPog6S-FoAY64BqBdE6Y5_b0plL-Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اسپانیاباپیروزی 3 بر 2 مقابل انگلیس در ومبلی، هشتمین برد متوالی خود را ثبت کرد و در این 8 بازی 17 گل زد و تنها 3 گل دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30527" target="_blank">📅 10:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30525">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTBqRCQ_ZSdXVTKUpwFM5oymkS9aK0ub6rcHLpiRhSYruGN9qNGk2KKf0-MGCRyqyAgE8Nq1-bbExWT5jOIGf86cV4vgofQ8lWT5pMOW-rgHxSthJAmnyOIZEGTWUiBwin8cT3jmwyqFjQNSVOS_caTL4hDyAJnDrl-jTB9fcjXDvRpi5seONoaL7uIOIKPBfNlguZaetbfiLXUA3uBuhcPxdDdMGV7FE17aDH_XLcuyxINbwV-brTtjYA8CTLYMHU4mUtdmMZjX3PFDLgUbyrp3qgtWqLEiJ8m98xRtH-dHUWYGVIrD3QNGGz4_YdT5DGAf8wyhfEIadSC-cA2dGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
گل‌های دو دیدار امشب اسپانیا
🆚
انگلیس و کرواسی
🆚
چک درهفته‌اول لیگ ملت‌های اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30525" target="_blank">📅 10:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30524">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8xz222Vfjf3qnMmJgtO9hfr7Oye08WRzX8Ihs5XOXh1ljpF9eIt5DTUBLz85P3CeuKvgSZmwob6_xiLdKRDN1NvXGOEpAnRTaxXPb_TC3cCn5k5CQbpX36Gg71ouEUJ7lcpAUN05bazmPJsU7Aat6Ota3FAl_cn8nvqJu4Ejq4dlqrM9YXRoQcw7RR-sDHsRDqN6BKTl45Pe-NxirxHIAEePBEP7kXalasKb07NkjpE41ZLDET0LVzMmEaM-_h6ngT-mCgWC0amVtLeFhQaWmn4Bza9xN9bE__N-hrmZHkFM3wCJQkmR90klNu4fCcoAaoRbiuRWVEd9T-EZXbIMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🏆
درخواست کتبی پیمان حدادی از تاج برای برگزاری جام‌حذفی!مدیرعامل‌تیم پرسپولیس در نامه‌ ای به مهدی‌تاج رئیس فدراسیون فوتبال برضرورت به برگزاری مسابقات جام حذفی فوتبال کشور تأکید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30524" target="_blank">📅 09:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30523">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/826b26c676.mp4?token=jgwhn7cCpcZW2NemmAhNw7XWfdYrDlyBiATZYoGgfmROI2qD4qORU-HIC0HpACTCvik6094dyHa96icY-yrgEA_lUZZyKwToq_wqrqZIMvhXE-mocBCu6JDP3wz4yI-TqSupwb7ciobciS2qwdWvNi1SnUhwjNh1y6f_F_XQABX_5pSq8bXRg6xu50OX0RQbEsy-P0DvSaMnPdePZmXwGt5wXfSoppn4IVMh0tpiYquf6KLOZG3HpxKiN4f8y0UzEfG1MpOFSlN19_a2XsK791V9qj6WpqOvOI3F5pCPslfLIn84pEsaNz4DNYnt0vRFYjlycAhs62r4uVWOx3pG0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/826b26c676.mp4?token=jgwhn7cCpcZW2NemmAhNw7XWfdYrDlyBiATZYoGgfmROI2qD4qORU-HIC0HpACTCvik6094dyHa96icY-yrgEA_lUZZyKwToq_wqrqZIMvhXE-mocBCu6JDP3wz4yI-TqSupwb7ciobciS2qwdWvNi1SnUhwjNh1y6f_F_XQABX_5pSq8bXRg6xu50OX0RQbEsy-P0DvSaMnPdePZmXwGt5wXfSoppn4IVMh0tpiYquf6KLOZG3HpxKiN4f8y0UzEfG1MpOFSlN19_a2XsK791V9qj6WpqOvOI3F5pCPslfLIn84pEsaNz4DNYnt0vRFYjlycAhs62r4uVWOx3pG0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
آنخل دی‌ماریا: اولین چیزی که من با حقوقم خریدم 206 بود، اون‌آرزوی اونموقع من بود و بخاطر همین باتلاشی که کردم بهش رسیدم، شاید میتونستم ماشین بهتر هم بخرم ولی قبلش میخواستم اون رو تجربه کنم و بعدش برم سراغ ماشین‌های بهتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30523" target="_blank">📅 09:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30522">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDD4pAtpUgNx-UVXplRwMSMe85IdzYFt7vhpEbjIg7gRpox9vLHSgmT28Vt2Y7t8od4J-Af-kt128-rCLaTyO1cucK6loC7kCHd2ffQ2JU9tYoo6C0SY4W3p0rIVlnyH6YQovS4Y02NPCbdmYFykIAEOJ8Kiix6gmZfc0MlB5HsPLndRxwBHtepI0HYjH5fxkIJ-YWIx3XqQhiqa7PoVB9pN-OpK6Byjvwrc_K2Vg2YyJECL852xs7z9YDjxTAcPW7pGDkzvxXzStne2wHvGOxFqTRELRSKpNdHahk1IRNNCwxOML4zhWI5LsTkr3OQnzI1J6-GaKmAJjc2xPOGSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علی رضا دبیر رئیس فدراسیون کشتی: از تمام قدرتم استفاده‌میکنم تابیرانوند ازخدمت معاف شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30522" target="_blank">📅 08:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30521">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQnfl0qib3cYaLT2G2yzibZjTrFmqrKWN7R32VQJeE-GUNmKdMl0DxptnrkKVzZx81RlvxGodVZ0cHaNgfhCopjL4-n6qn7tzbaRGlNlP5hu0071VdOkBOrJ2_Ztz6D8ZHvTjJm58JUH5cmtwm96zDafkxzw3wmi07N1FOD5MVrX-nb8cPg03tG7dIfJ-8z5aKjhhp2415dzicdP5lAKF7QlrGAQ--ICzx7u97CYt8GdP480yY6g0OzYDS23vL1ByuYF0hXuNChpGTPkWsyIHUHMz9F9tPrxSSWZHUfGVWTXeCd1o92riWZOM0B_VeIRAz67-M0goeZzLdVI1sC6Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گوگل رسما ایرانی‌ها روتحریم‌کرد و از این به بعد مردم ایران دیگه نمیتونن‌حساب‌جدید جیمیل بسازن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/30521" target="_blank">📅 00:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30519">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/009c394c65.mp4?token=ac0ZONcxO_x43PeZv4lu0bHookPCJfvS121Moh8X56lRSQIKUrjHqfdgqqi94lmQPpESZ1WQz-ZDTeVyTVX9GPaT-Yckf51HXZe4hTDIHogT4eDcuIahta7aIS_UYoBB99CeA493hhYIcTXC-t-iiNRVyocyT9eZLySRphcRtxbRxCnZ9OdUMF1C5Bt4G97_7W7TZ2GXF78VigtH-eAYCc55KKXeKLgg11drOC5qAqhxH12GJRKU2uJF_3Cr1vE4yT_4Dat-NfJpI4788o2RJ9oKSvJGHl8IjmTdl9wBui5X7XSjMwtT6U6-mqnSzMKWIwUUrnHhssc_tWZSz3Hm0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/009c394c65.mp4?token=ac0ZONcxO_x43PeZv4lu0bHookPCJfvS121Moh8X56lRSQIKUrjHqfdgqqi94lmQPpESZ1WQz-ZDTeVyTVX9GPaT-Yckf51HXZe4hTDIHogT4eDcuIahta7aIS_UYoBB99CeA493hhYIcTXC-t-iiNRVyocyT9eZLySRphcRtxbRxCnZ9OdUMF1C5Bt4G97_7W7TZ2GXF78VigtH-eAYCc55KKXeKLgg11drOC5qAqhxH12GJRKU2uJF_3Cr1vE4yT_4Dat-NfJpI4788o2RJ9oKSvJGHl8IjmTdl9wBui5X7XSjMwtT6U6-mqnSzMKWIwUUrnHhssc_tWZSz3Hm0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌ملت‌های‌اروپا؛پیروزی‌ارزشمند یاران لوکا مودریچ و کامبک‌تماشایی لاروخا مقابل شاگردان توماس توخل؛ سه شیرها نتونستن انتقام بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30519" target="_blank">📅 00:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30517">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCBlTHHF4M2HcPkdYVYvj6Bvt3rD-9GSs7Z0m7cfPhUC1_9WiiDF7XAiVSNSOjRIW6vjHqp-jxtxbjTP3kkV8cMw1JEqqQuLdro3iXZRb9m3tIUN7rzx56j5kzaIf0hD8MxFkqafO_1deU58KNDXFkJ1BlfeM2iplCXWbUeuXL2vHDRQm3uLP1nwf6lCI75GHL9mxXdlwOSfKRymPnW6xE6mqjMFbk-h5SDaZChQFtvisUWRj6qpMOnGcH4yxEJPlFtHBYe8fU13bTT3BpEBK93Vtm8CUPzwchXmL0NUpd-5fuuELAZC6cNSiBnEGgdutpFSDqSnwV-e2ong8vBcKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ اولین رویارویی رونالدو و ارلینگ هالند با دوئل جذاب دو تیم پرتغال
🆚
نروژ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30517" target="_blank">📅 00:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30516">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoXe3JLjina8AYEmPO4-nzJtvxEm4LEwA8U3Vuw9boLbzyKXpkd7sWG1q58xMutGFoEZH_P57vJXFZevHDUMm7NzjS5eQ8B0BK-iK3hA9P-JgK7hTbki0Znm-RyTq9owTOK46z2Z4_kWm2hPT-5Kq9yhF25wLLp1SfPskI1B7WU0h5UAzXryuZil35WvM4SQZqrJXJgXsxPbdAlr8FSlji7Nysu4x95TYTpjuc87Rxuz47m1ETwg5x-Tqf0bCirYhI4YnejrQSHvgzXszEXM_BqKcnQIJ3at79d8WV7FL-UcOXBJts9oprEcZoeFnEmM0rGlP4W0JFjaY1xW7dfWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌ دیروز؛
برد ارزشمند ماتادورها در خانه انگلیسی‌ها بادرخشش‌الکس بائنا و لامین یامال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30516" target="_blank">📅 00:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30514">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtFh5lUqHZXO1jGi4oPn2MxgkX-PU2ZIhfhLfgBtZ2-JxkDnekBIzjXGENy_vwz0NCBigh1iR8YCCHMdMyKKFYQc02ACrQzAw18FblJk6wPjnGioYZ7J_MGX4pDbOYHRmBVi9ES5PiivyNavdNUgv0OtJRWMJVjj0LV3yNK2NrVCg3tYPk8fSXWl5RYxIngfxPMXiTRvRfsd8JbF56x-Gg_0_R9vgIsr7TY2vT56Rn-Tj9aX49J41BSJlSdLWvzR9bZA9KEQYcPM-Gm_qqEm21qohPntzMtmhtzWB_f-HRIxd05NOpJlXVnNEBht5h-9fIpAY3DbkFXFINjnq91wNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول لیگ‌ملت‌های‌اروپا؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
اسپانیا؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30514" target="_blank">📅 00:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30513">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9QK8lOHVhD5PuA-ulF43y7Vm63tEl031lkSzoTZu6bV46BE442xqVxIz7d74vPf9KDT05ZPc_fBEdtel5S_AJ0XZ_Cgr_FHNQCQEMHwETDMv7_1vJ3TynBGGWszzQ72ZAz2ckfQeb0cLWuWmSAyWllYN208dWhrBAyeoV0laz0MBYfP9vqCRwUQfIEmGiNult6suQVBaQcowjykXEv6LwUBFLpqvcrjAVCxtqiLo9IeFyMUBSQdwkKQspe8xTAuzf63pI9txxSUVF8Mq3JD0WuAO3lmQF2mqqlvfKHiWV0hYl4LWv3mE6sPpVW90Hd3IxA0aVL1bsMlNfK4KrvgKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛جام‌‌ملت‌های‌‌آسیا آخرین‌‌تورنمنت‌ حضور قلعه‌نویی درتیم‌ملی‌خواهدبود و بلافاصله بعداز اتمام این رقابت‌هااز تیم‌ملی ایران کنارگذاشته خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30513" target="_blank">📅 00:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30512">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCflh_qnxyVg-jnBpRJgliFrnWZ19kEiqNsjvUJDmpOTja9f_aom-hyijm9nOzWi14mPRIEftNGXhimKadgzUO98QMlHr763BQnBpFsHMN5edW9qV-wKdc1za4Ff-ZR0FYoa5CBx-gb4kqBjry5QnwafTE-tXVFdvRbmYNwM1awQbk73h-PuiPsScAx8C-1_ktf1HFTVqsUZm7UWop1wcF_ZhY-rJ4SPq3cwzhXtrW4GvS_7BHJG30KoYMEUDdutS5J3xWkCgzwEGDVWpn3-IA7PRIbwKyakld2Rnzzpdh3IQG3DyNg9lP7GLGXWOVdTsguL8fl9YS7pKyvETkGcdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ تاجرنیا پیرو خبر اختصاصی پرشیانا: فدراسیون فوتبال صراحتا به ما قول داده اند که جام قهرمانی فصل گذشته لیگ برتر رو به استقلال بدهند و ما منتظریم که فدراسیون به وعده‌اش عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30512" target="_blank">📅 23:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30511">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzTJ7Z9RMOTivgHpC1noqTILbShiDh3gALJTxCubK2wixrk9Pz1xXOFeYcSYOlrN39QmVkzuvsysJhXwo-0hbMbhxog9AFz9TR-tN9aG309ld-D0-rJ3pJNLGlYXScvXICwyiEXif5SX2j8AMk3syjRA4pulEcadElEiRfr2LjDcT9xcx_wWAduP2lvFR8WdWNs6axk1bqLlFzQZdmkKwTMGW36yk80Fa4QUZwMC8Ej6-BHrjjNVzxwny3OoF_fo58XPAKizfz6MzkfclFc1u7MM3kiHhUrDPoVGGw7Jazn39P7I64lotzRu-QnyXbMuC-ASqPL9_aYWZD2-XhXxvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#تکمیلی؛نشریه‌کوپه: بعد از آزمایشات گرفته شده روی‌زانوی‌مصدوم کیلیان امباپه مشخص‌شده که مصدومیت این‌‌ فوق ستاره حاد نیست و امباپه بعد از دو هفته استراحت به تمرینات رئال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30511" target="_blank">📅 23:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30510">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1JySQONuIu0Q0GeFqkxL6d1OJ8Ok-PIMB31I21KgJBVvCDyZzpqWPotBqyzm6EvbC8i28jrcQBAXEfJHkOSFmoT8GKjrO6hjTLeLCd5pLRFz25CQnh2EmJmvE0RK1Nn3LlJ7xsDe4gxcQlVijsjGTHCfNc7yCggHSSGHKptBjkQTd1udGitfA2NTmQiiudvEsFSwu2jAp9kFYcNx-9NFYx8PIrJoEZhADtRzlFDDhwMJ_QDDNLgRa1qcJTLKJkUGY1FkW-GwmNSOz5_HW8b5B7kKH40nLLtRT_bxHyL4Nq1HqQzrqgCp0km1cqooe8Sld4WVY7LvngO3Yg26NaMgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ ادعای بن جیکوبز: خطر این سناریوی فاجعه‌‌بار وجود داره که باشگاه بزرگ منچسترسیتی به‌طور کامل از دنیای فوتبال کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30510" target="_blank">📅 23:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30509">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5szwHKj0w2hhIFh3F3ElDknDFH7Wde7BqSCtWGX2_PVti1jy6M1aOqWqaL3XdWI47rANbE0oQywej74AA7T9l_VuJikjUS5KYVBINJ0utTTNqCnv8HOzIkvkFk9lGkab5hyMUZYIWsXuFrH0heo6ufcYU1hvDYGS9RWiEG14bhKPkdaf6FIGBzyqvP6li2pcOVlYtuJRbdYve4ZoqGjWttrySxM3uRj0z6UgN0iDD9ZoZeHeoG4Pyi2uVTtOAcAglqbjje0J3iaguYzx4Yy4BVWNcMIZR-lt-eoRXrT4ieV8l3aL9omsotyG1Wp36GUcoEZZpTLo4EZg6R_yFKSxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه تمام هشت قهرمانی لیگ برتر منچسترسیتی از فصل ۲۰۱۱/۱۲ به بعد پس گرفته بشه و به تیم‌های نایب‌قهرمان‌داده‌بشه این شکلی میشه. تو سایت‌های شرط‌بندی احتمال‌محکوم‌شدن منچسترسیتی بسیار بالاست و ممکن این تیم به چمپیونشیب سقوط کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/30509" target="_blank">📅 22:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30508">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BR-cTxdI5N-gRpB1VGrin3NsN8jgIJe-r4hhyn3R1APx19jGmag2ykCgE6pLg0wLkrytdbPgMdMdx5cMb84DzbIrcNErmd2NQiwwn8TaX9ylEkZCV_ZT4jRMPvlKEoOtE3pjtJqAKJ1ka7KeAQAWsfF8_hHZJZRjmFiExSvifOUXVhKU-9iOCBumtHgIJ54RpWUs8QbY9LLVsYOrCAsXzAobMuZUKxJKsxRtQRHLcdPWSW1cnS99k5xb4JoC4o1xmsnP_xGrQ4wk6AO-w4dix4CyQdjEGZYpr5eCgVCR-aJBZrDl70VWfMY0pwDm7BLf8_OPY1qVN25JpWPqSnsgMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری #تکمیلی #اختصاصی‌پرشیانا؛ مهدی تاج رئیس فدراسیون‌ فوتبال عصر امروز به مدیرعامل هلدینگ‌خلیج‌فارس قول‌ داده که روزچهارشنبه باشگاه استقلال روقهرمان فصل گذشته لیگ‌برتر معرفی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/30508" target="_blank">📅 22:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30507">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjD1U3CC9_hA_ucGNBf18wcVCf6Ej3oyBKNAiiy2vevCFbskUQ8MPGtTPUjOxbYz8_wqM5Syi1bwMrcVbnMRwa0bgGYMqznqFfCV-O3rrXSAkVcviHdwIe0QjpuCkX_Zm1imaBRCnZlqo2HXXuSl7F5I46RqzkITLTSqZ6Uu9wwfrVTGhZXH1T5emkmdA00xCng-_XwEjPy9_911aV-vlBudgpRhc6u6IZBVnnACKQJrXD5Um75xhF7paWkreqMnRhl_ChQELj_iBOD6f0Wx4bkbZNwCEcW8VCd-WLOQcgNkztiW5l7mxEqu84DFp-A52e7fI01CfB0ihANyy3Zg3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا دبیر: مهدوی‌ کیا یه گل به آمریکا زد و از سربازی معاف شد. حالا به علیرضابیرانوند که ۳ دوره جام‌جهانی‌بوده و پنالتی‌رونالدو رو هم گرفته و مقابل بلژیک آبروداری کرده نمیرسه از سربازی معاف بشه؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/30507" target="_blank">📅 21:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30505">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iyBsPDRS6y2zxJ6EIZw3c5_C-McpMBn4huSSVNkq1OEkaqRsfKgjOb2SwyJsPN_RSbf9wrmbFt1jmU_v1gGTpipWDHjpGbxLwJ3lcVGWFENZYbmoXe9nBC4C3E-FP389Xf67stKJNQ7qCQ_YeHTlkrhqY8Ysu4lVHtJ1MUTBs0W01ZF09nvBZ2Jhr6WxNpTOyo6b6MwCmypvi_sozIAPwLQLBmhzDn9tp1PHxmM84VS1M1wxmEgsAF1K4--MrXQPpNCfPLzdy4cWI6xvmygRMsJze5xQU5oRIcezpwf-yQKHlje1KGfaxJ0TEyP6PvrYEzJx4mVZc-_kWDX6UeaEYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HMtMy6PK0u4YMrUc3v1r4aBjRiUhFF4dKxh3gXfNZ6VGXDef824sv92-0qQHOwRfgFB4VSDPhhvLFROQ77Ya8c7jN5kFPvTcdvzcdAl500LQ4QIY4wislQRiJyOD-_m0S8mYE1byQjd20tVxMtLoDfDcHBU7UlbOYzOXchc8Zsw-zIj0PwosH1Rsuso-Dokgu5iuftxsLLbL75TGhta6rEQ1h6hQpaMrUew89NWO3YYxOus6Cn_L6gFPjdUQdX1Azvw_6z59UDiRh8zMg1ZcYefhVOHqpTYjfp6gpY6YcG0oOrD-ckt7-RifUnhZeHAFbOubq0VqUmc4O6HgJmNLZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌اول لیگ‌ملت‌های‌اروپا؛
شماتیک ترکیب دو تیم ملی انگلیس
🆚
اسپانیا؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30505" target="_blank">📅 21:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30504">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsdppFBVb3w8oM1mwli_22cmGgxzWfwbdnYMWCDbrZjCgl6U70eRNsz8Cx5xghcvML4ohQtd_pguERR6wkAG4lrO7yKh6GOMPmqtb6j5Vd9YwjQ1otknp6ZYUSZXjH2-ZCiNKnqVfJRR_biYTc7DaXQWTY_AjELiDkjpuF6EWcmSE_AZPIFXcgbKxf2sCunIfTuHKwILRllRsO_saGXDMGd2lsQC51f7mEx8xGI9sr1OW7-3Fpxzk4F-jMxgNykpW0q25CK-8WPEMdw4BaWvohSjsLdyKL8uZSjHKohqbQ--BzahHpbY2HvfPQugI7aTbxTSEk9bbs0EIvTkgdZmXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛درجلسه دیروز هئیت رئیسه فدراسیون فوتبال سه نفر موافق اهدای جام قهرمانی به استقلال بودند و دو نفر نیز مخالف. مهدی تاج تا پایان هفته تصمیم نهایی خود را در این باره خواهد گرفت. احتمال‌قهرمان اعلام‌کردن باشگاه استقلال توسط فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30504" target="_blank">📅 21:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30503">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AS2p-qon08mPS3xaCR38yyrsXtpSVUBes1v1EP1W3qYnLmkzw72MW2dOX1dlpegYgLpT4qUU_HCY7S5Hj9ztng5TBDdfpCcCOyiI7UinlmtfXdXMH_9xsGJHYe89lCkp7QCJWmOlb5LxsNNit9TOLZEv2MmHrXK91EH5XOGrZGGk2KMMmIIxafaqFGSgeR0mp1HmcS4cgmmmZsVos0byYrhI4Ct0Ktbqk0ZM_OjzXtKi46vkKi-JbQ0JtOvya3cSYIYmrxCSMdIyoDynXLpmpOfBy2noolsP0EJL_iMySLYWibBTwEP0GYuV3zVbanlbxbmTjoKcxouwfVaq_zVQOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30503" target="_blank">📅 21:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30502">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ee53107b.mp4?token=T3M2gB1BwbV5GErliWxR3UdKEpqm44WOxb0FWbgdsymAsM5vrLzfoOT1FB6IQg2q_P1oiZH3XKZCVjtCKI2XKI87UHv3dTpQvFcfHUcEjnwvEaSpArSQGCW22zzWE-ZuJUAfOL1jd3rL2WqyL9UA1d4ckmlWRGImMeF7uc8GfevAshyGK1vHNcFcqH1Y4arGb9V4F9A_5V3dT5TEBMHYfByXYWWmko0oJV3qwaLiXM3XzS7ayMk22_unXK5fG4eHQHC715U42JY75eyRq2AJGiJdY1X95fDHBZGxS7w6tFpJ1igBmQLfK06A_Oe2fDQhA9DfCDXobWhD4qCOdcmarw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ee53107b.mp4?token=T3M2gB1BwbV5GErliWxR3UdKEpqm44WOxb0FWbgdsymAsM5vrLzfoOT1FB6IQg2q_P1oiZH3XKZCVjtCKI2XKI87UHv3dTpQvFcfHUcEjnwvEaSpArSQGCW22zzWE-ZuJUAfOL1jd3rL2WqyL9UA1d4ckmlWRGImMeF7uc8GfevAshyGK1vHNcFcqH1Y4arGb9V4F9A_5V3dT5TEBMHYfByXYWWmko0oJV3qwaLiXM3XzS7ayMk22_unXK5fG4eHQHC715U42JY75eyRq2AJGiJdY1X95fDHBZGxS7w6tFpJ1igBmQLfK06A_Oe2fDQhA9DfCDXobWhD4qCOdcmarw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه بدونید که نستوری ایرانکوندا و خانوادش وقتی سه ماهه‌بود از جنگ‌داخلی در در تانزانیا فرار کردند و به استرالیا پناهنده شدند. برای آدلاید بازی می‌کرد و در 18 سالگی به تیم اسپورتینگ پیوست. تو20 سالگی به تیم ملی استرالیا دعوت شد و مقابل تیم ملی برزیل یک گل فوق العاده به ثمر رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30502" target="_blank">📅 21:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30500">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odpthFCGbKm5rSQG112_tN7ubRsBetT0cIoU-iWTSP_kOMsC-yKrC7TJxulMxW5qR0I86gMMB94fGA3XoIYBR_pmhNbyYvV2BEvZFW5_mW2E883aAmoJCX42EQ8pKuQkq5YSeVAjqjTRyLOh4d04kNePGZ0yH3h7tAoNdCLq9HvPLPUytcEoTOY_RQ1GKqt05nnE6zYkVgDzWrxli9OrmZhUp4LanS8R-nvmZrlY5YEjb6gCm2_8dLDYM8Z6h3H15oXVQ7MXcj0rYQkOrsSLtN2PF-um90DAG6yNl1u57zAiACvcrsxayQ16A2kJF--G94ZiDGdkRb_YPLa9zAjGnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
#تکمیلی؛ بااعلام‌فدراسیون فوتبال فرانسه؛ مصدومیت کیلیان امباپه از ناحیه زانو هست و بدلیل جدی بودن مصدومیت امباپه، او بزودی به مادرید باز خواهد گشت تا روند درمانش آغاز شود. گفته میشود امباپه حدود 3 ماه دور از میادین فوتبال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30500" target="_blank">📅 21:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30499">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIL21IFE-qWogO4oTF3g0gc0pek7mpY9orAzRc_IhgOA0B-q6sKD3pRx1kvTj3yMO4RDs9TJqiBc6wIg93kFa72e0rRXCz8D7J_PHRUM4Iw_7h4t9m03cq59xJa8S7nVRh5eYIzhXYhX6V31Exefr-TYJ2oulp5eZsKt58_CBl5ro98giKTch1pgfP5BK30jfvkPjAlYN0_N6lamZkJSErfghiyeK3ZDeeBjjoEF9uzrWPPM_j-_2RrAaCbbCK4fBvM7PiDHlh8U4IfQdFdJN_pI4UgtOK7P8sYm_djVwXC81u9jKEmUPnL22XJDwFQ15VI_4J_nM6KBxPMF3oQpRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحبت‌های تند و جنجالی اللهیارصیادمنش فوق ستاره ایرانی لخ پوزنان: میدونستم قلعه نویی هیچ اعتقادی به سبک بازی من نداره. تا روزی او سرمربی تیم ملیه هیچوقت برای این تیم بازی نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30499" target="_blank">📅 20:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30498">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jd_pP8-bLT7BpAa1L332ei8t6Ih6DFPLq07eH5NYEvPayXqLMDtIMKJD3xVszdI0i11oWFjzlVgUJt4HSvMFp4atQcpuPX_XjLOMxy8jNT-sQIQHZihjCcu0ty8EZo_uf6LckKuahcxj8h81Y9pDcOw-bJpypgPwFKyeLfbORgLHWp6eE1lvJ2sFkwlWdsSXCM3-OvtEVCR7kpPxyjpgi-w-eHwhLHEqb_R-ETje7kvSEGtL1sPBtY3-SazkK-GRsxO2_zuzDC1_2wpQJ0NN_g_Rml-IQ8VOrqA4t3wlpoHi8Zjdc2XDe6ss_akZjwWngg9KdhVSc0YrwK03jeixxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
81 سال‌پیش درچنین‌روزی؛ باشگاه استقلال تهران تاسیس شد. آبی‌ها باداشتن دوقهرمانی درآسیا پر افتخارترین باشگاه ایرانی در قاره کهن است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30498" target="_blank">📅 20:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30497">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d9a03df6.mp4?token=crmurWFevo65Hn3JmTiwQ2uz5VljG92u-NcAOUTquf1sB_pLr98kNKrQEQ61yx4sNNvDuy-JzARWWvnk_t95Vr0zy3t_9dEr0klTXSJ2PWFfX3RqCQHo0fIHJGPqLBw1zpPpY4c63WU9kHfGq_Y0r1E--Kuw18MLAXnHM8gQNFEDz5axAQhF_9EoWa4v4LjCgSN6zS1tDWPHIN6Rww8gxE7d2xEUIhrMDdLBAbXc4oujmO-g2ir86o1nrXg5LIxntkzlkC01CMNhEZKB1OPDW4SplIjMr71Feb-N-cV5_OZh3s33g0fHQnIAypkKSo85WHZHJBvFMrMpNuRnPPqYUq384wKrE9EnlQJ2gCHYH5o7zf5VRV9aMpAqSg2QwLk_icvTiq2_tMmmVgvOLcolRI8ZI76L9uEWHuJ-RDWWjLN5QzhUajwZ1CeQL4-CF4Dtput7WOXa2epYO1Jg0ANhbXpMEec9hm46RCIzV_3Fa-toSqAsVcqk2_8i2N4O-eyDDNP_j2f1grpdcBT38iaE4sIMO0K3hZ2vERpwCXZB-AnEwLsdEp7mVHUfuxHsT7sW34nAquCksuLg3KyAQUxQSI-jenjqwEncB_ZJLIltC2wmGuTlt1wXUQpaxgsSijlxvyyFi0KWM5jsR_ILRMeoFuBNErhMLpSKgHMzsOw9_hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d9a03df6.mp4?token=crmurWFevo65Hn3JmTiwQ2uz5VljG92u-NcAOUTquf1sB_pLr98kNKrQEQ61yx4sNNvDuy-JzARWWvnk_t95Vr0zy3t_9dEr0klTXSJ2PWFfX3RqCQHo0fIHJGPqLBw1zpPpY4c63WU9kHfGq_Y0r1E--Kuw18MLAXnHM8gQNFEDz5axAQhF_9EoWa4v4LjCgSN6zS1tDWPHIN6Rww8gxE7d2xEUIhrMDdLBAbXc4oujmO-g2ir86o1nrXg5LIxntkzlkC01CMNhEZKB1OPDW4SplIjMr71Feb-N-cV5_OZh3s33g0fHQnIAypkKSo85WHZHJBvFMrMpNuRnPPqYUq384wKrE9EnlQJ2gCHYH5o7zf5VRV9aMpAqSg2QwLk_icvTiq2_tMmmVgvOLcolRI8ZI76L9uEWHuJ-RDWWjLN5QzhUajwZ1CeQL4-CF4Dtput7WOXa2epYO1Jg0ANhbXpMEec9hm46RCIzV_3Fa-toSqAsVcqk2_8i2N4O-eyDDNP_j2f1grpdcBT38iaE4sIMO0K3hZ2vERpwCXZB-AnEwLsdEp7mVHUfuxHsT7sW34nAquCksuLg3KyAQUxQSI-jenjqwEncB_ZJLIltC2wmGuTlt1wXUQpaxgsSijlxvyyFi0KWM5jsR_ILRMeoFuBNErhMLpSKgHMzsOw9_hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌فوق‌العاده از آنالیز مسابقه شاگردان امیر قلعه نویی در بازی هفته اخیر مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30497" target="_blank">📅 19:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30496">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777a222aa8.mp4?token=g98wIG2u1LJsxF0nHXQqGK3mECzq3fgsHR9mNYSJDUXX9UHGvAQwSW5s1prwaR12tLalOGTg5WhvpE8XE-8dnbNky2pI-EN3U1HxC8FJSSnPDA-2YJjwvOc_KxZUChJ0ZjSaDMBG36aHaK15fJTkrHbY605dfiwrKDPIxtT7E-K95ZkIV_oTL0MllkHS8RuDxfIjg9kAyzP2NaJa6AEW5Vv43DEtM5nEyYocnLMiUDE8zPX_TFCcrY0FtgmzcJ3EntZLSaO4bn6C2Yxu8F2DARhhd5zP3I7I2Z45WMETZ79KGlvjOzHALhuLJmU6Cb2r4Czs1_Tqxnv-leNqVLoMzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777a222aa8.mp4?token=g98wIG2u1LJsxF0nHXQqGK3mECzq3fgsHR9mNYSJDUXX9UHGvAQwSW5s1prwaR12tLalOGTg5WhvpE8XE-8dnbNky2pI-EN3U1HxC8FJSSnPDA-2YJjwvOc_KxZUChJ0ZjSaDMBG36aHaK15fJTkrHbY605dfiwrKDPIxtT7E-K95ZkIV_oTL0MllkHS8RuDxfIjg9kAyzP2NaJa6AEW5Vv43DEtM5nEyYocnLMiUDE8zPX_TFCcrY0FtgmzcJ3EntZLSaO4bn6C2Yxu8F2DARhhd5zP3I7I2Z45WMETZ79KGlvjOzHALhuLJmU6Cb2r4Czs1_Tqxnv-leNqVLoMzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇧🇪
#تقویم
؛ هشت‌سال پیش درچنین روزی؛
ادن هازارد فوق‌ ستاره‌ بلژیکی چلسی این سوپرگل دیدنی رو در ورزشگاه آنفیلد وارد دروازه لیورپول کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30496" target="_blank">📅 19:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30495">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzlzEoGK3f4iZAZ9zqL-AXI5wJmsvsRNNXTNNdo4PgiE2u48SU-xM0JNtLBDp6JO0cQwA1cpG8ZmOov9jRBf1pvILQ21I-moxdWsXaGMRbFgljCF51A-goOQKbdbdwC1Y2Xikl9F_i8Ci3VvfOjuW1ztSyeH2bkCsNMzbOaApQh9Qlk--p9HqKpwD1FX5Mblh4-Ic23ZzPa1NOEYmzxxWAkTV_xN69XawwW5ybmlkiNBzZIlZcCE98IGzJamHzVdyRxvheF6Mh-qqGRW9Ytp9XtAtTobnoVED5gDqn3_zyf77undZv137n3HHmGOh7pbX8UBn78ZbTTkMFhxXYl7OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی فوق‌ستاره تاریخ فوتبال روز 14 مهر آخرین بازی خود را برای تیم‌ملی آرژانتین انجام خواهد داد و در پایان اون مسابقه از دنیای بازی‌های ملی برای همیشه خدافظی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30495" target="_blank">📅 19:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30494">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇪🇸
🇦🇷
تعدادی از کاشته های استثنایی لیونل مسی فوق ستاره آرژانتینی در دوران حضورش در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30494" target="_blank">📅 18:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30493">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSbdC_YkbFfRHMnQSYl7XCKpgEEGI7qZFqfytNU5uUEJNPmTEqm-tnsSSK88nk2u2Yk5i0zdynoxZvjZ4sXWWcXd4XjywGfpR9D2CFryAtHW2hKF6aPxRKn4ZGAW3NXU-QJXA9kcW40fCC4ZFROgSaEOnpkP_1oK7wgOF06dKaJDZo9sVolwte-2N4zwaiu0VQgMpEQr_IG0IqMXFr7sZEMITKAJh_CT2UBSWYIIHMy5dd-gOyk8QJaCSVP0RFTVNqY-54wi-ERS8gh-_Mcxs3KNn6gIsnE2DVIarNnZVXsaP_pxYKiEzAEUuf59uVuicAbDFlYKBp84n-hycmP04Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
رسانه‌تلگراف: قرارداد هالند با منچسترسیتی بندفسخ نداره حتی اگه این تیم بره دسته پایین تر باز هم بند فسخ ندارد مگر اینکه سران منچستر سیتی با فروش این بازیکن موافقت کنند. بین رئال و بارسا هر کدوم 200 میلیون‌یورو به سیتی پرداخت‌کنه تمومه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30493" target="_blank">📅 18:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30491">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oeBDdUx855-Kr9_FJIzat8lBK8DznMKxvybZQzJ_24ZCx7GZI02O4N497d_zE8YEzgV0mX342sCv58v_TVTUwNMb-bEkjln9ACxGRjpoQC2Db_1m6_JsXm8nyQUJywXp525auyX30raVfK0bMLBUkbXytHycvCZFgkaV3WxwHf41v1YpE1hzIzOd_SfycRMwZLyrIoIWRMwsHGkQA60sYLbxuzxZaPqPr2SCRxz65TsU0alDAZlHiZXQP3W-0uPkRPycAQE6ZcO-kP77hxgkN0_grmfQxwDEtdSswIS_IAZ4Jkb1OsxoFK-ARUpQaw8DgiMO-x36YfUHsOZvLr3A7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/holydJhQwsFshNZzGMahhLzb_3RSjxT5gRpozV0VtXUT2q_QKokMlcFMBdQSvSGE1EHwVf4LGtLreq1zy8WieGaQ5Qb-OBw89feKPzjJbw2xyV1hBIOSVI8f7TiThKcUs3os4FT7t36kX_K3VA5suxxzRbSHdqKlSQyzRe2HboYVxzQ7xN3TDQIZfQ0tZKCivLAI5DYw7Zo58G78F8jwpGya0w4_p9QvHQj4QPM7PXQ8j_1zQBRRAfjLzka_q4VwLmD5wt5-IsrOYNIjE_D7kEdF5cvv8WsKha72fnCnBfJ59z9sUy02kf1cCLaV6ei4_IuI7ENmxTqpK-QlH95Q8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
رونمایی باشگاه استقلال از آیتک سلامت ستاره جدید خودبرای‌تیم‌والیبال این باشگاه درفصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30491" target="_blank">📅 17:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30490">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6bSe0ru6KQnEnsNODoKbi8hwDzvDTikR5_OckrTjGucd4SmqBjTjwwJneec2JmHUc8NbofdWviBh9SOzp11Ud3ZmLVk0po5OHous148Ctg-sCvNroaRLGSfo2CSW_SyjWF3bhTXBbQ5zfoRf_mhhqPHvmdNglEFJ0V6L-DmrxcNl4x1ZvRToXDN0nMbr-yGQyJlT39Hv3V97A-0Rj2G9uBFJnJ2nft_DmNO3PGjpc3TbyYqzRLSfgrIFfwqc9Y8ndRDcKRE-2Rsnn0oe3kqDvmA_UHeNXaxVY0GmeznMuhhZinTxT4ZCKADx00RCyE3VHnS-w7kYypMXuu60ut87w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه عملکرد لامین یامال
🆚
هری کین دو کاندید اصلی دریافت توپ طلا در فصل 2025/26
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30490" target="_blank">📅 17:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30488">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4YdT3U1kJ3N7LixkzffPkdGXg7lo-krMnW8PR3Maj3O804ZwDjtCcLCPSYeD_cJNLeW2S4a55qs6wAb3bo8GNvFCI-gbvmezkmeyJb8Gtl-8lhnGMBvQNGoHqXxFduyYpO4AufyA184N1bVDoHAUgg9BmZlccUD9xdyvsJYv6VsMnbLzhJqmXNF7jguEJzQzFgtbG90WUSv_NIFn1SxRhWkEEtJJhqk_FXX9AFS913L8KVnHi59r5_XvUKJEmyku0RrU81AuoSRr38_9vF4KP8OG622X_kl_FA5QZZOdPtzX5tfLir8PshWmorT18IxbtjXUCco7JekdPq4nS1WHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه جدید دونالد ترامپ: پیشنهاد ۷ شرطی جدید ایران را رد کردم. مقادیر زیادی نفت هر روز از تنگه هرمز عبور می‌کند و شب قبل ۲۹ کشتی از تنگه عبورکردند. ایران می‌خواهد تنگه فورا باز شود چون خسارات زیادی از بزرگترین محاصره متحمل شده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30488" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30487">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkaoiL8lVlWQni7JXBeP_bZykc7T9c6qSgnzOjROuFWqXAAVHNRBHBNpAbm-1IG5dMkOqZXyfTbq1q1k_6qwU2kAuozjf2XYS_9kwzYZU-7LQ7OVVmEqy_VZgwKnXew7xlYpfGJYw_LNudP_HOy41nPhsOZaGHcS3_BMiGmTRga-lhODrYToBYOdM5bzk0GvkPZAoWc5gJuieISIfAZ-DKixMJSDh0H8BAdtlIJU2rexlWgDVlZKsJC64UOAjuwn8mmTgI7-2ROdVg6BlTRpz9aZn3eaR06eY1xhoq0tZ8cBzA26HWO-u-C7dVY1nlPiED4PwVyJHpWiz3q9xyTAkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
یامال که قهرمانی‌یورو و جام‌جهانی داره: من دوست ندارم برای بهترین بازیکن تاریخ با پله و مسی رقابتی کنم، همین که سال ها بعد بگن یامال بازیکن فوق العاده ای بوده برایم کافیه! ۸ قهرمانی لالیگا، ۳ قهرمانی‌پیاپی درچمپیونزلیگ و ۶ توپ‌طلا برای پایان دادن به فوتبالم…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30487" target="_blank">📅 17:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30486">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgjMZfLjRg_bFVBk1N9R1XdCGq9MCd_xB4n2EXoT8-rwCh6hqE1JYl0K33kFwDXoD_U_HeFfytplmzhllPTnu8b60DEAAPSsHX6hclvu2yfmJ_5-SvJJYzS-cgMC0Fo2cgz4HB9ThNDq4al-QHHQPX9OAbfDP161-mpsZwQZXjfLDMJ9NiLOFPBTkYCxoOcKT-OdAlip9VKHgBizxN3dT5OLtJ9u1_RmuCgkmbjTDm8PEmUKSGwG77Hmf1uxRkk2_1RLSBWQgg0nIeUGL5UyD3bZNyKcWdM5kpbKD-07mu_Ikpiru-Bu82CAWc8N7b0l1iLSR_LWfIKYtPBD8TgmdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برسی کامل‌ودقیق سیزده سال ناکامی امیر قلعه‌نویی سرمربی تیم ملی در رقابت های ملی وباشگاهی؛ وقت بازنشستگی فرا رسیده ژنرال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30486" target="_blank">📅 17:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30485">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKoOlHqzjBufkkTDXOZHpBY4Tg2-DAkdsFmTY2ZAy2rjEWy_Yq7KbvntACwAkAKGUXhk4KyOt5TPZS3CfDZziBxm84iXvw0sWedB7CBGschAgTqP0mB7sh9Bnl0gpsMqI6FZY1lZhbB082nGvJeVWAQzftQdL_B90rj8gmRcBEJCrGt9Fnvix5J1p2J-wEx0UFlsp1mgknYgRMT5829zIG2Q1ObpGsw2UyT8LK9GfSebRujg6fTUSE2zjvtXj8dwAjRj9c5nr5WW21-FbEiTrce3uPb0iXrEv5hp-4Bp8puRwcqvzcHyjLCaxKHmvcIMDphfcLqCD05F9yfFN-oZ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبرنگار باشگاه‌فنرباغچهه که امیدواره هرچی زود تر انتقال کریس رونالدو به فنرباغچه نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30485" target="_blank">📅 16:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30484">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8miTYiWmYMAr6kPqjsF9lgEj6-1LMGmJHXELrIr0tlACvW21FvPHxw0selMdMqcoZhjbd3l8D8vs5OMpStQR9MnhT6cD4BTOORuFxuKnWL-FkaBzsbIfhIDZIGePR5eGbSjHAAENFNyIaY5KANjrgUDdj0bDmC4ECGQeUazgEXLH6I7NZDPn-kynQO8JAr4mjaAtjByPA_xAyYtmIUKwYMZRl6dCn6QCFucKIAx_yfwL6B2grErIR0oKQFLm6yUrnTi7o4ExdrmKXi5ZpF0CRDqOlnMwtQPxXh1uMXTmiiE_CUGWesqt2YzkkMCFF6MQ3nG2aNYRpEbkSkE7iPgwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام حجت کریمی مدیرعامل باشگاه تراکتور؛ معافیت تحصیلی علیرضا بیرانوند یک ماه تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30484" target="_blank">📅 16:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30483">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjok9Sd_XmuH6YA198hdH7Ndd4lhKZx4EDpQ8_DltvKJvjaDaZOLF0y1WWNcVCjU_zOyq-UZz6wgRg-hhkxOdEPRKAZSuJSmWL_lg1kfj39EjJ7RTFx0EnU7cZpdB4AjhU9yBD6IlpQuX9Nb05OWoyITohmGqyVOQ6e-ePPcgWLhaKi1qL2GjjF6wQB-9Bepwf99x16zo7Ny4g4-BqodWXYIWgrPnc4uzDtNnnDRDodhabeCZSgDf82IQ6T-2ZG-qt-f-VNQ7OYnooGChUf0gYaSDvPRW9gGJ0lyQyZh8yoOSCj4lyuihH_hkbInXww0EJHCFV7MoU7EeAgIfOOcqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
👤
مصاحبه دو سال پیش علیرضا جهانبخش کاپیتان تیم‌ملی: بانهایت‌احترام بازیکنان ازبکستانی هیچوقت نمیتوانند خودشان را با مامقایسه کنند آن ها نه در لیگ معتبر اروپایی بازی می‌کنند نه عملکرد خاصی داشتند، آن ها توانایی شکست ما را ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30483" target="_blank">📅 16:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30482">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ES0D4Bm2-AZEbRb-TvDUHUPpCB4eIPe1MkqZQgtM4APtrBu40zafx7VPd7XKSdqXFdkYDyLG57nRc-9hxnzKyBpfCLjyDlBevqwJU_ObCvvtDcxPIirKvEbBCiU5tLI2GzJpPOGYhreDASUI4rLDI91otB9AYv6kIOetmO8NAOzDTtJhIvnuVjhYrZ-fJPC-0jb1cSfhYUJN2YU0gg38F4yC7b50r0BA7nvI6idcgvRWXUuI2RjuxEsFhsTcCYpJyvA3ddXGCS-BUa5dQkSbyjl0wRVp2h2ybwPMNFUK1RdoS9Z8ae3-YSbsBToyF_MPkWgugN59YnSCaa17_5N4Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناسان AFC؛ سعید سحر خیزان رو بهترین بازیکن دیدار امشب استقلال
🆚
السد انتخاب کردند. سایت فوتموب‌هم بانمره 8.9 لقب بهترین بازیکن این مسابقه رو به یاسر آسانی ستاره البانیایی آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30482" target="_blank">📅 15:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30481">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPbYsXwY0HvNAeJiGq9CuWAS5IaLkx0nO1UDJDmiezncotu9ZO1AVwuhsuVjE_DWNLFcqV8Mn6N-jPDsDTmKaFjKJwUGVH2E_TKKMQ4bmIMHyuiW1JSjP7yo5ePDqDKy8IuPdXZmmPhEZcpZqKyw9O-pF2aq0z7u__DGjZNJ6vEt1qwOZ-SfEDDp3DGyK8olp5qHFVJY_MxGA3iAa1k4nXEoE5_L2hI-MOutddwB6Cz50dxXneNpB3rCNxjbfH2k-dk1ghI1ob0hrPpDFEW3xI5c9Yoxh65T9dSlX88qG_8oFDHbot1ToaDnKF9t2h3gucbg-ZsMgliemx2s29H6ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه تمام هشت قهرمانی لیگ برتر منچسترسیتی از فصل ۲۰۱۱/۱۲ به بعد پس گرفته بشه و به تیم‌های نایب‌قهرمان‌داده‌بشه این شکلی میشه. تو سایت‌های شرط‌بندی احتمال‌محکوم‌شدن منچسترسیتی بسیار بالاست و ممکن این تیم به چمپیونشیب سقوط کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30481" target="_blank">📅 15:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30480">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✅
تابانی‌به‌فینال‌مسابقه‌مسترالمپیا 2026 نرسید؛
بهروز تابانی درجمع ۱۰ نفربرتر مرحله مقدماتی دسته اوپن قرار نگرفت و از صعود به فینال رقابتا بازماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30480" target="_blank">📅 15:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30479">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7AD8zM5B5YWXIERmoDCSSrD9q0l-dnvZOI23oP_p1Iyd0FkpAy8K19o9CUrxUSTAUbRN6sVArFuliO8P72eujDwd2PWJd3LW1uufv1e71oFUyUTQnprvunFX06JV0CgNFLxp0i1fyxrCOzX48Oo9p2H10jlT9zHhUA3PJpYEtSLMlqkA4m-L6BRDxdfzCfmRsm4iysGwm_4g8tqoXXIYzc0P3sVczO00hOuGJxx4YsUV65kN87qmZ4hElqwtMVfVHrDjqNvqqRg3ANmLvI6dmp4QBCEPSVNrqddEP59GUBVviZCNmVtf7w5dqiTSQDaqJqb_N3tFO7uRCQyykhpVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
مقایسه‌تعداد جام‌های تیم‌ملی پرتغال قبل کریس رونالدو و بعد از اومدن کریس رونالدو به تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30479" target="_blank">📅 14:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30478">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mO0W1O19NEI9nquki52qBd66lZM-6ZUOQs7aRV0cMxeKMSBUUladXZ1dRREWSxWA3mjwkvuajGpi0BuMf82ofFznr_XNxUKeuGGAAkMvO0JO1K1TxpBwXUxskC6LYDlCqDhUdoNod9Rh1A75tHC1htjcOF0A4-hhT5vQ7bvRlVaoNCx8d6U0fPVGNO46j0fVr7n_Vkclh5PvN2ZwFGfUBkpbgO2S4QqT_i5lbfaK1fMO9xll566_FCn4owhApvznglfJLOUK-ZWyGwHRPwiJHd-CxaNPswuQY9B211xdna1Ztn174KMA0cWN4--zop7srjpQKh3qHJyPQc6hxoAziA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مدیریت پرسپولیس طی روز های آینده و تا پیش از نیم‌فصل‌قرارداد اوستون اورونوف ستاره 26 ساله‌ازبکستانی خود راتاسال 2030 تمدید خواهد کرد. توافقات بین طرفین انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30478" target="_blank">📅 14:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30477">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKqnLD5aEecEsJzKW8-rrGnQCkzAu4Ria8eQLHdP_EO28KTJxrPWb8IG1RNspHueB6jYql7eoElUsVAc1qcxWOKP6W-Y2BFohjUTUtamy8sbinH0yXFFFdSjox3qpg-TIujdczeLh1dXFhAmyUfxs3vQp2_pzqZE7YuKyOn_Z9GMPh6y2oN-uLf4RHa5fUfSM9fsVvYJgJu_8d_IKI8dr6ojL2lN7qiDMkFPjD0GCXfZ4kBRw2N0bDwcc2Sw-YO8JxolYPT6qJ-DaVJOw6UI92rYOZ5uHrRLlGaBa841jm_4Q0j8XnASz2BdktAedmlyCZ3KNmvHUIHGCtJjR7lRNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلیمانی وکیل علیرضا بیرانوند امروز صبح بعد از کلی رایزنی باعث شد که سربازی‌ این گلر تا اوایل آذرماه به تعویق‌بیفته. او به بیرو قول داده که تا آذر ماهی راهی برای معافیت کامل او پیدا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30477" target="_blank">📅 14:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30476">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MD2zDMjXoCe_cFmpWRDPdsghugxaqea284uaSVpGR922VZKTDE9t1xxZOkTAKCIBpTyZW9EO2V9ci3VytgPZkvONhHYJDZu7sDtCCPqful-qQBnnBDiU9mn3k87UUGnSfeDuA492tRACFQ0MtNmKwvjj8KB694R55S_U95lansYQTA-3ETBP3VoSV8VQLGReKYOqYZvBRq5UK3I_YDMaZXiGhPBh-w3zYKIRv_PT62snHvQ4LImQk38yKOW-sRUt_ogHMfS4H_bS_KhJeX7xJb-YK4IjLgQFefxhQS4w47Fw91-90liiUKxwCK7YVvSz2aAHFaIay_HFbPPEMLy7GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کول‌پالمرستاره24ساله‌چلسی:
خیلی دوست دارم که یه روزی درآینده نزدیک شاگرد ژوزه مورینیو شوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30476" target="_blank">📅 14:07 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

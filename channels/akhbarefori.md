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
<img src="https://cdn4.telesco.pe/file/mM_iCbSU3kev9xxpdCLSqktQrqH9MEaHz1s5fnTiewCoZ5v2ixrFWsS1bvaTI-_th3tQVtI12svRScHzpUyko1O2Jv36sgtZeS0-nWqOHVrkXQmug37LVc9DfHYBPoIWjFejhKVTu4nGpQbb8MY9Q8LtMyIrc8jAUZHGeosWqeOpDBGDS7EIK__qc7wKNGnCHos2vkYohaYshZ0ssJ6pxXD1-sTgqu-fjYYJGMU0jVQdghHq1aEpioRbw2CgqLJiaLhwE2tE1Pfh_4YSK_ttvw8nH_BPhkuUg-SkWUu3mjednWPmUpRaVp9L5n3GCA5ghGoHZfieeUrSpd04x9Kncw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.31M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 12:14:42</div>
<hr>

<div class="tg-post" id="msg-694786">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
تصاویری از اعتراضات دانش‌‌آموزان در فرانسه
🔹
۶۲۵ نفر بازداشت شده‌اند
🔹
۸۳ مأمور پلیس موردحمله قرار گرفته‌اند
🔹
۳۲ معلم زخمی شده‌اند
🔹
صدها مدرسه به آتش کشیده شده‌اند
🔹
خودروها و کلیساها به آتش کشیده شده‌اند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/694786" target="_blank">📅 12:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694785">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ادعای ترامپ جانی درباره حملات ژوئن ۲۰۲۵ به ایران: آنها درگیر مواد مخدر بودند، اما در عین حال روی برنامه هسته‌ای کار می‌کردند. اما این کارخانه‌های مواد مخدر و تأسیسات هسته‌ای، به‌شدت هدف حملات قرار گرفتند #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/694785" target="_blank">📅 12:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694784">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/513ee42a9e.mp4?token=UYJkCHdDjkVogbNOKYyZ0xwbnpLEKDojJCcNmkaZ4gmnRhoI3_ufI6KclyLGgm7O9p9MbLd1Pq-sIAckGV9cnIcrTDIjWHJz635OCIBiBe_RkGdD5_xHhseJucdmHX6zvsdEyaWmewt8edxMhrQOsaDVt8ygC8OAJutprH4xonsrMKweXMVhZeO5_PZVkm67151fNEioscVrLl7ji7xjd9AtJR0OOWrFWjiNGHgdiVpFeusTv8kMSgomnmC3au_I8MKnq3N6yOarCs_zPO_jLqKgtE9RsPkLuA_E0uNy969DiedzqjkH5dv01bHxzkA2db9KN-ohHRaKf4CYcX8Sxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/513ee42a9e.mp4?token=UYJkCHdDjkVogbNOKYyZ0xwbnpLEKDojJCcNmkaZ4gmnRhoI3_ufI6KclyLGgm7O9p9MbLd1Pq-sIAckGV9cnIcrTDIjWHJz635OCIBiBe_RkGdD5_xHhseJucdmHX6zvsdEyaWmewt8edxMhrQOsaDVt8ygC8OAJutprH4xonsrMKweXMVhZeO5_PZVkm67151fNEioscVrLl7ji7xjd9AtJR0OOWrFWjiNGHgdiVpFeusTv8kMSgomnmC3au_I8MKnq3N6yOarCs_zPO_jLqKgtE9RsPkLuA_E0uNy969DiedzqjkH5dv01bHxzkA2db9KN-ohHRaKf4CYcX8Sxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ جانی درباره حملات ژوئن ۲۰۲۵ به ایران: آنها درگیر مواد مخدر بودند، اما در عین حال روی برنامه هسته‌ای کار می‌کردند. اما این کارخانه‌های مواد مخدر و تأسیسات هسته‌ای، به‌شدت هدف حملات قرار گرفتند
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/694784" target="_blank">📅 12:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694783">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pouDPdGOurakPH-lLRShdQ9IY_pLc6Bm9I92aBvoOfuJ1e3wcoSKHtl16u8S0eiY0Uh6kt0EwjpWJdO58mZf7DFCL9Mqj8l9UfDHNbzeCCVi44UJ9B9OLyJIIZLko1lB1cZIg2pZdtldYeOzWBE5y31QvnKD1l-scH2Gvc5yWEwXSP53L3McFrMY7t8KVH1Xj7ru2tBwUrtP1I0w5Z8u-qUmOFbEhVY1n9RMjQohEo4pg_Fe4rwCDyaU3IukmRhK9Yu70m7bvwwtftFLDWVsJMg89T6poT227GtmKZ2z70Mt1sRocyY8Un4agTD8Q0Di9rFy57nNSVYIpQv_yVulJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ نابغه: قبل از دستگیری مادورو از هوش‌مصنوعی مشورت گرفته بودم، هوش‌مصنوعی خارق العادست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/akhbarefori/694783" target="_blank">📅 12:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694782">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a6d833d56.mp4?token=F1qdwASri0rrw-OcmiM24C5YYkWzlg_AqS8NgqgR-tHPBOaiY4eazy6RBtIEIiowj5JjnhTbllXdWXbQx6s_EgWrebd0tSwR3x377dtIxRipqr1cl50S21SWBV0xe8zfm3gE0mF5-M8ffFYf_CAY6oxBwais98W4emE4BfyLl8DkFS9QAiBzbznvD5Rl_Zk3aitc_Kh4XZYHuXVyzUnC8OcK4bZhjQCm88fnccA_i6jmNqSV4hlMnNGFFJ4478rNL-vI2IcB0YHlRFV8fQK6uekiR4zphPtvR7Uydq4T_VwCJ1qytxfv7rUJi9-nBpzOd2vB51BoV05wdZGFGlTwNIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a6d833d56.mp4?token=F1qdwASri0rrw-OcmiM24C5YYkWzlg_AqS8NgqgR-tHPBOaiY4eazy6RBtIEIiowj5JjnhTbllXdWXbQx6s_EgWrebd0tSwR3x377dtIxRipqr1cl50S21SWBV0xe8zfm3gE0mF5-M8ffFYf_CAY6oxBwais98W4emE4BfyLl8DkFS9QAiBzbznvD5Rl_Zk3aitc_Kh4XZYHuXVyzUnC8OcK4bZhjQCm88fnccA_i6jmNqSV4hlMnNGFFJ4478rNL-vI2IcB0YHlRFV8fQK6uekiR4zphPtvR7Uydq4T_VwCJ1qytxfv7rUJi9-nBpzOd2vB51BoV05wdZGFGlTwNIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نازک‌ترین ساعت مکانیکی دنیا؛ ساعتی که ریشار میل برای فراری ساخت
🏎
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/akhbarefori/694782" target="_blank">📅 12:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694781">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
شرکت فرودگاه‌ها و ناوبری‌هوایی ایران: آسمان ایران باز است و ما به تمام پروازها سرویس می‌دهیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/akhbarefori/694781" target="_blank">📅 11:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694780">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8bbc2f536.mp4?token=cCpPpThSmuorizl29wKqEpnUWxJRXBqtJOODTZx89d84fQgZHKP1AaTFrABHzQlLWysYUifcjKStMqiBGQs1amwOJsAyYntPXRhoO2EH-15OMqmwy2BjjZVAk-4_xrTJGFP61E3tXJhLYenmcpku24dYTED10OGVeFwKQ4U8dD42eS8dar7sMVZvTd1UQIHjZRd7_5mTIO_sVg0QP-RqH_n2RUB1QsXSgUQiMmp8UD7ufh7UzkGm5Rnow3z5_fpvGNtw1v6fmhz-lfolydCz5lQnMakO5DXwDuB-J17OB5r-95mBV96fqvV8_DNAZc2S05_xmAYGRIgsjQj8Y_U0mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8bbc2f536.mp4?token=cCpPpThSmuorizl29wKqEpnUWxJRXBqtJOODTZx89d84fQgZHKP1AaTFrABHzQlLWysYUifcjKStMqiBGQs1amwOJsAyYntPXRhoO2EH-15OMqmwy2BjjZVAk-4_xrTJGFP61E3tXJhLYenmcpku24dYTED10OGVeFwKQ4U8dD42eS8dar7sMVZvTd1UQIHjZRd7_5mTIO_sVg0QP-RqH_n2RUB1QsXSgUQiMmp8UD7ufh7UzkGm5Rnow3z5_fpvGNtw1v6fmhz-lfolydCz5lQnMakO5DXwDuB-J17OB5r-95mBV96fqvV8_DNAZc2S05_xmAYGRIgsjQj8Y_U0mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای‌
ونس: وقتی به پرونده‌های منتشرشده اپستین نگاه می‌کنید، فقط یک چیز کاملاً روشن است: بله، این دونالد ترامپ بود که جفری اپستین را به پلیس محلی معرفی کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/akhbarefori/694780" target="_blank">📅 11:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694779">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
آمریکا به‌دلیل ملاحظات امنیتی، خدمات کنسولی سفارت و کنسولگری‌های خود در برزیل را بدون ارائه جزئیات، تعلیق کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/694779" target="_blank">📅 11:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694778">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
وقوع
تیراندازی و درگیری مسلحانه سپاه با عناصر تروریست در راسک/ تسنیم
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/694778" target="_blank">📅 11:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694777">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ادعای آکسیوس: گروه آمفیبی، نیروی دریایی پیاده‌نظام و گروه اعزامی دریایی سومین گردان تفنگداران دریایی، از پایگاه سن‌دیگو راهی خاورمیانه شدند
🔹
این گروه حدود دوازده فروند جنگنده F-۳۵B، حدود ۲۲۰۰ تفنگدار دریایی آمریکایی ویژه، خودروهای جنگی پیاده‌نظام و نفربرهای زرهی را به همراه دارند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/694777" target="_blank">📅 11:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694776">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dd987a56a.mp4?token=TxFON8htmdEsLUR3udNo96GJqHAjL_0LsXxgrqvFFTMvkrqr9q-KgfnHr65r2LQBjVgut-L6KFHlH8ui1yLxacU9-gJRky3CoANkQmuBsL4d7W8kW4KeVqCV06VSnn8yGUPS-u9tUlb00KQ8FwU4SwD9aRqwD_PiiC3te1U_ZMIhFlmNu-maYQdKzTp15IoExzqB6qRqMrUHFOOPmkFRUiSBvUJvbSXutI3z7lAN3qDTNE2M3sKk-DfuB5Ez0g2gqM_xnnW4-CPTL7s1XjV7193XNSLc4xoqFc3jsoSlfmleA7RSQHBBv6F68ZOUExxY5w0-2-YQqkmJPHgCTVOyxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dd987a56a.mp4?token=TxFON8htmdEsLUR3udNo96GJqHAjL_0LsXxgrqvFFTMvkrqr9q-KgfnHr65r2LQBjVgut-L6KFHlH8ui1yLxacU9-gJRky3CoANkQmuBsL4d7W8kW4KeVqCV06VSnn8yGUPS-u9tUlb00KQ8FwU4SwD9aRqwD_PiiC3te1U_ZMIhFlmNu-maYQdKzTp15IoExzqB6qRqMrUHFOOPmkFRUiSBvUJvbSXutI3z7lAN3qDTNE2M3sKk-DfuB5Ez0g2gqM_xnnW4-CPTL7s1XjV7193XNSLc4xoqFc3jsoSlfmleA7RSQHBBv6F68ZOUExxY5w0-2-YQqkmJPHgCTVOyxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این مدل کفش برای افراد دیابتی ممنوعه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/694776" target="_blank">📅 11:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694775">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F48DAnta8yN-laJYWqf1XwFNR0JyLpvrlEvw8sN3VP_6bhfpBotR_Ay9Qc0BEDWG1jFq2HJpOnmPg5-TMVH4jdioNRqEVvfH5lWO3mKkDuPHcvaYWw0h4FnQicE_9Nb6nVdcea1v2pli4wzB1VYPtTB1St_EnQtiimy4lGmch-PgiU3oHyzPAO3R35zNceOYpqS5fHY4INvnA7-kzwVPD8SFriN-XdZGxnPswhUOn0tG8y3pwC28u6-tENkmtWp3lrmpxk7BW_MRxnjVbEnTPJ8VsG1sOlFdPrg7ZRtdPHC8bDwb4zJ9skayG8vVxKiWzHRaJOIlxfEw9TBaSAjNfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هم‌اکنون/ حضور هواپیمای نظامی پگاسوس B۷۶۲  ارتش آمریکا در تنگه هرمز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/694775" target="_blank">📅 11:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694774">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148764d5c.mp4?token=MhRlr3ZOe0Qeqka9s8AteBvITAj7Ubr0cRnjTTVsrDlYYCfJx9qvlbagW1IyIa4ZlAEFv6e8ys3My8fIItTS6cMuY67s-7YabWu-_JI9ReeLgNfwUFbFr7rfMLDF8A_XvY1ouidVbebuaX9fc8RLL6JWncI9MiCQ7LYWcRWFVLEzBZ1MRLAKReZluHqdFEFdAf04vM3wI7UgCRYHw3TuvEKdecHidDyatTB_thEeh6IX7e3JZoNg_YUVQmmRuYs0UcrAuqfE84K3Z0M9AI1xU7WSgvAvQbQ46EDD71PUtXhAQesH-KFBdgqYQh63D2mb5GwVbbMUv_Jme2Gxaafmgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148764d5c.mp4?token=MhRlr3ZOe0Qeqka9s8AteBvITAj7Ubr0cRnjTTVsrDlYYCfJx9qvlbagW1IyIa4ZlAEFv6e8ys3My8fIItTS6cMuY67s-7YabWu-_JI9ReeLgNfwUFbFr7rfMLDF8A_XvY1ouidVbebuaX9fc8RLL6JWncI9MiCQ7LYWcRWFVLEzBZ1MRLAKReZluHqdFEFdAf04vM3wI7UgCRYHw3TuvEKdecHidDyatTB_thEeh6IX7e3JZoNg_YUVQmmRuYs0UcrAuqfE84K3Z0M9AI1xU7WSgvAvQbQ46EDD71PUtXhAQesH-KFBdgqYQh63D2mb5GwVbbMUv_Jme2Gxaafmgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور برزیل: ما اکنون نفت در حاشیه استوایی کشف کرده‌ایم/ ترامپ از شدت حسادت، تلف خواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/694774" target="_blank">📅 11:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694773">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c53b02cbab.mp4?token=bHBAnlX3dHyhcT71A5pEiYIlugqRI53ztKxFs-eI45FTLeUmfGp2WJCVslduFMBjkimgQxXdZME3cpQxuuqyV3LVPyba_4X9oYl4kgWfdkC6zQkbHRSII2EIB0qG-PcHTBQ9gFjXkCBlfIF8gSX354m5aaEm8n0l1iePoXEtizc5H3fLC6ytbJwkM73y6DaatKyMu0YGKH63bowlGixHDYmG4UUQw4okpJzQIEbQxBHAcYByMwwbtnEdB9voxob8_4YbdcAYtAuuUqBlmKrOQu3SGn7iP-jr33k3aNU-widu5Rb62TFCPkiFCLAzuu7zpI1xYwOvBgD4ectnLPjDsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c53b02cbab.mp4?token=bHBAnlX3dHyhcT71A5pEiYIlugqRI53ztKxFs-eI45FTLeUmfGp2WJCVslduFMBjkimgQxXdZME3cpQxuuqyV3LVPyba_4X9oYl4kgWfdkC6zQkbHRSII2EIB0qG-PcHTBQ9gFjXkCBlfIF8gSX354m5aaEm8n0l1iePoXEtizc5H3fLC6ytbJwkM73y6DaatKyMu0YGKH63bowlGixHDYmG4UUQw4okpJzQIEbQxBHAcYByMwwbtnEdB9voxob8_4YbdcAYtAuuUqBlmKrOQu3SGn7iP-jr33k3aNU-widu5Rb62TFCPkiFCLAzuu7zpI1xYwOvBgD4ectnLPjDsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی وایرال شده از کلاس تخلیه گریه برای بانوان در تهران!
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/694773" target="_blank">📅 11:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694772">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
وزیر جهادکشاورزی (۹ مهر ۱۴۰۵): بعید می‌دانم نوسان شدیدی در قیمت برخی کالاهای اساسی وجود داشته باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/694772" target="_blank">📅 11:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694771">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ممدانی از آمریکا خواست به دیوان کیفری بین‌المللی بپیوندد و نتانیاهو را دستگیر کند
ممدانی:
🔹
اگر در دست من بود، آمریکا به دیوان کیفری بین‌المللی (ICC) می‌پیوست و حکم بازداشت بنیامین نتانیاهو را اجرا می‌کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/694771" target="_blank">📅 11:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694770">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yt6HHixc9KiGJzgMqA2wIktUTQnkuBNzdlwdebG5QWDqju5w4n4jH5YEaXT-Cfo5tR8d_bdvZ_GcbOPMXEX2YzhjN0VZXJKY6hh6aOREGSZuRCsBLmimnVQXvUg00Cob5dqigoQ7F_blkXB6z7pSTRJOUN9ejHW_jbrMmyeRv40E1Lt0-Gdk3KBovlN6BH5k386KgWgQTPAz4ivW9GZ4neqxtHc6Fio7Bpk_jh4wsEJIuwvNl3vo2YMAioBYA2Vv1Y4eaTLJVSbhENLwrOGQ5UuIXSX1eYsIAfgsbmnrhUqEgqn8IIHwKDBljGYCBCfotTrHcb6g23utTS9-G5GCIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارلینگ هالند از شرکت هواپیمایی نروژی به‌دلیل استفاده بدون اجازه از تصویر و ظاهر منحصربه‌فردش شکایت کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/694770" target="_blank">📅 11:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694769">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmPKf0c9a2S-GOfXx1QMbFYTCA_4hn-tIX3wuu4RXU1jk7NcnPPkp2AcXf7rg-Voln5wxny23u_620LKsUXX8_tAzRveE6Q1OuGMxVe2AeGCVrAz4B7VPOZEVAGxKZ9hy2MgUUzFNUGwnQjTEQK0fA4uslL-NoVwPqHNuzZPYVtK_MFKOkZDHU19KxAemb3I4eNb59Vrblot9dnt9NqIf2YnJEwkvNnA0boLSW5j2iV_26dKSBvP65vk9mtdsOC78xgs-rhdNYg9h_aL7LxL9m8QG4HmudUIAgcSeQY_rtUTRWeTh8Fk4Ey3kimFkDlo5oVVHzfeF43N5gGKjN-Whg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترین‌های خودرو در ایران
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/694769" target="_blank">📅 11:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694767">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fa0-F8I5XFgI2qr5B-L2Baf-3Jx4Eoene-Qc4oZomsbxKZtKdr2d9618k6IQjgCEF2dJzDvV0zPwGdhA7ggQ46CQU-0CeSQVZhi5n6U8JL8xyyymH1n4OdUdi4G3cwwCkrEMamuoswaf8YEAQyuuiQh3j4A3m9N59vPJgJf-ItJtEmjyzEzrl7PLR9ilid98tJh01_a5DKVX0HU88kF5U2jnh9L2jrcpLRG-SaneHT1LqgeiQbieCecxJJF-0Mhsoh4z5i_NAqivded1wSw75VXkp9UOzjfcMGlJtUW2Z25KiTjvb-ODU8FFF9mOD_OKJoFB4TafgMKC4GOh2UlVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dCUp70oXqU4v-b5D5uHVQJypjneD9INcblvfqMYQ6l7XY209gF-FZ3jikTMuCOZX7Q4ELVL63CDUOV_Ya258DCT3Y35zkF-zVCXoQC8rOgUadpOFMC0Inz8j2lTG9_TdoHXrYOkWuRGpcJ5x8wajgy22_8tcKHRDihlVnGfHm1F5SShQT-giFUuD9WRlwk9G479rgkH6e7BlzaEACnpGaVidRBaInBfHfX-MddWqysRrGlctF0_cBU99ph7FbMIIwU8OZHpgUUL3NCVOg9-pIFcWgq9h4btoFqQclcHASFdJgwz0C91vpNqno3q8p65h9KL7yi3Z7psaEJ2to9d7pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ناو هواپیمابر روزولت به غرب آسیا اعزام شد
🔹
آمریکا که به اذعان فرماندهان کهنه‌کار ایالات متحده پس از جنگ ایران با کاهش شدید مهمات و کمبود کشتی‌های جنگی روبه‌رو شده، این بار در بحبوحه تنش‌های واشنگتن‌ ـ‌ تهران، ناو هواپیمابر «یواس‌اس تئودور روزولت» را راهی…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/694767" target="_blank">📅 11:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694765">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ecef6a0b2.mp4?token=pO4JDG985YeH6hCfAsTYQYVgZMLbnhLi6-38jgC-cs-zHK09uRfgPiXpFLz0lZu7hgyRF8n4r-8N30dXTIPWkSsVJQlApXp0K3pToPdOABWJJcwq9Cv9eOpioDkjLVly0y9Kphgc3Klbi0hw1mr4Mh5-AgtSQroh2fxH2aXxjB99aesGELEOemZkSD5EkJzBC8ob5NXUe_zQMVdRj5ICeFd_kpE15G8nFJPm4OE_e3OJal2hb3qTL_-QuBAZeH3oWoDO7wWN0HQRCZGmsSBSZLw7BZRADDTBlr3Fx_ZsK2uhQb7Dqf1HFbGDOz4S_6aYf3NWyjBN9RWSz6I_Yw_Cyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ecef6a0b2.mp4?token=pO4JDG985YeH6hCfAsTYQYVgZMLbnhLi6-38jgC-cs-zHK09uRfgPiXpFLz0lZu7hgyRF8n4r-8N30dXTIPWkSsVJQlApXp0K3pToPdOABWJJcwq9Cv9eOpioDkjLVly0y9Kphgc3Klbi0hw1mr4Mh5-AgtSQroh2fxH2aXxjB99aesGELEOemZkSD5EkJzBC8ob5NXUe_zQMVdRj5ICeFd_kpE15G8nFJPm4OE_e3OJal2hb3qTL_-QuBAZeH3oWoDO7wWN0HQRCZGmsSBSZLw7BZRADDTBlr3Fx_ZsK2uhQb7Dqf1HFbGDOz4S_6aYf3NWyjBN9RWSz6I_Yw_Cyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ به التماس افتاد؛ اگر رای ندهید دموکرات‌ها مرا استیضاح می‌کنند
ادعای‌ترامپ در سخنرانی‌ انتخاباتی:
🔹
ایران می‌خواهد به توافق برسد. شاید توافق کنیم و شاید هم نکنیم، چون اگر قرار نیست به آن پایبند بمانند، اصلاً توافق نکنیم؛ بیایید کار را تمام کنیم.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/694765" target="_blank">📅 11:14 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694764">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b553c78bab.mp4?token=re5Szmtb4K_efmPmdHyONPSBo7KnDOwslYzdQYDOulzyzh5zyT_ihzrMj6ieR9CqJzUoup72BLwcXsS4Plica5LUU1s77hTZBFXouoi9Pz2zZSYF_sO7P5dFMV3EgCVGxkaq3QsXnaMjKNYQIhYRcezoPvRJbwGTwuHYS_sPobuTEZK6cqu0_KjBGj_DC8Fb_F2tpKSmvryhWWYNId2ftQjpTw5d4JyNJRKdWxZpWm4OHkRg8MRkJVb_ZiHZcWGnDxLmotcpihYeJEK1perQKggAoEj_nuB9713SZZn5agXHen4M64HO2z1DPxwBaDxnaOXEjlaRIDxDpoZXEm145zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b553c78bab.mp4?token=re5Szmtb4K_efmPmdHyONPSBo7KnDOwslYzdQYDOulzyzh5zyT_ihzrMj6ieR9CqJzUoup72BLwcXsS4Plica5LUU1s77hTZBFXouoi9Pz2zZSYF_sO7P5dFMV3EgCVGxkaq3QsXnaMjKNYQIhYRcezoPvRJbwGTwuHYS_sPobuTEZK6cqu0_KjBGj_DC8Fb_F2tpKSmvryhWWYNId2ftQjpTw5d4JyNJRKdWxZpWm4OHkRg8MRkJVb_ZiHZcWGnDxLmotcpihYeJEK1perQKggAoEj_nuB9713SZZn5agXHen4M64HO2z1DPxwBaDxnaOXEjlaRIDxDpoZXEm145zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسب های وحشی در سیاهکل گیلان با شروع پاییز در حال کوچ از مناطق مرتفع به مناطق گرمسیری هستند
🐎
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/694764" target="_blank">📅 11:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694762">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
رویترز: ایران در حال تدارک‌دیدن پاسخی شدیدتر و وسیع‌تر در صورت ازسرگیری حملات آمریکاست
🔹
پاسخ شامل هدف قراردادن مواضع مرتبط با آمریکا خارج از خاورمیانه و حملاتی مشترک از سوی هم‌پیمانان ایران در لبنان، یمن و عراق است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/694762" target="_blank">📅 10:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694761">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
مارین‌ترافیک: پس از هدف قرار گرفتن ۴ کشتی، تردد دریایی در تنگه هرمز از نیمه‌شب پنجشنبه تقریباً متوقف شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/694761" target="_blank">📅 10:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694760">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd954cd0d.mp4?token=G5nSUSwLPRknqtrBU1HtLeI9_iACpaMuLpOjbysZP1wNB6Oj7fv-239uMIHWqSeAC8yWEjDW2zPfB__dJMR08nvIKcXoklxxkJReyZ4OlHhfxIDdUCI6ucfLclU9NuNHM5PnYTW9NMWRYog3u703qTzzu9JkXmsPB9kmDN2cWgf7eV5bpNPV04Q_UcIRfO_xGv4oaFK3OxQHkuR66SnkRzsgpO3DbBLEIiVlCBM2evqSXpY_I9i7Ofs27aaLwM53Wzbp8Jg5NoaUEArbqqhb_OAvudv8UXXSgGl0AzA6nqMDLMKTGp6EyRjSGPiifCSo0IseV7dfLUvNtObJl4F_ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd954cd0d.mp4?token=G5nSUSwLPRknqtrBU1HtLeI9_iACpaMuLpOjbysZP1wNB6Oj7fv-239uMIHWqSeAC8yWEjDW2zPfB__dJMR08nvIKcXoklxxkJReyZ4OlHhfxIDdUCI6ucfLclU9NuNHM5PnYTW9NMWRYog3u703qTzzu9JkXmsPB9kmDN2cWgf7eV5bpNPV04Q_UcIRfO_xGv4oaFK3OxQHkuR66SnkRzsgpO3DbBLEIiVlCBM2evqSXpY_I9i7Ofs27aaLwM53Wzbp8Jg5NoaUEArbqqhb_OAvudv8UXXSgGl0AzA6nqMDLMKTGp6EyRjSGPiifCSo0IseV7dfLUvNtObJl4F_ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار به رانندگان؛ چراغ زنون می‌تواند خطرآفرین باشد؛ نور شدید چراغ خودرو ممکن است دید رانندگان مقابل را مختل و حادثه‌ساز شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/694760" target="_blank">📅 10:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694759">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
روزنامه یدیعوت آحارانوت: مسئولان پرونده حادثه فلای دبی تاکنون وجود ارتباط ظاهری بین کمک خلبان این پرواز و ایران را بعید دانسته‌اند
🔹
امارات نیز با ارسال پیام‌هایی خطاب به رژیم صهیونسیتی خشم خود را نسبت به پیش داوری‌ها قبل از تکمیل تحقیقات و مطرح کردن ادعای…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/694759" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694758">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
نظرسنجی جدید آسوشیتدپرس: ۷۱ درصد آمریکایی‌ها از نحوه مدیریت ترامپ در قبال ایران ناراضی‌اند/ ۶۹ درصد گفته‌اند این جنگ ارزش جنگیدن نداشته
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/694758" target="_blank">📅 10:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694757">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v17yvVG6aBt_U_y4oFyfSPEAozuZVqSvdNBJwa30NzXjHFQuuhoj4uof405KZhSEjjk_P_V4ZA2wyWeNZrxDHpFnQHp_eaLNNzBtZqeawo_9yqUyWFdsleUb4rw5rj7b6p6epZXMIBK59rJfv7WjssRJpethc0YUY5WsvG4VF4odu3Z1SlgF54Lvn-GuXxS37ZsW7m2ga-GH6gekuzrMaij1mUlEUHLzckA8E7aB90fZVf7RRFWGX24o9QKefR9O_4C0m4sICaZZSlTgK9dAy4shBFDgBk3NOP2cNLiNygmTQq_DhhRD_8vs4gGR9sXOByMQspRMBO91KiOb5elIDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واحد‌های وزنی طلا
🔹
از سوت تا اونس، همه‌چیز درباره وزن‌های طلا
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/694757" target="_blank">📅 10:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694755">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad7550e337.mp4?token=DzRoRXwwRCkgPNKqEXjxQP8Hf4oURlhvS6wacVAJpRHCvpFDiu36BsoDvEFoNCrOo18Jh7FtZesbJMIi86f_05bPNysnYEwR3e25bhD4jOKFIBNv-SU0V9kfMehbhlFA7A5lmKZm0SRk_MCBzRKsFiQ-d-lfzZADD63JrGphbps6HrG6oBt4pgBqlDpCjd_NdevJ3-JE89xmRXtJ3GGXFNa0HYNGLTzfOA5rv5uaNj554-WNjyIM60R_m9mD08P5R9KRaBOEcWFOwCWtSxbu1iRZI8HpxlXKlwZAwfeF5Ks1lav-8pBuWg3qwjLkGlkodPjNZiP-_GBGei-x_vU7VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad7550e337.mp4?token=DzRoRXwwRCkgPNKqEXjxQP8Hf4oURlhvS6wacVAJpRHCvpFDiu36BsoDvEFoNCrOo18Jh7FtZesbJMIi86f_05bPNysnYEwR3e25bhD4jOKFIBNv-SU0V9kfMehbhlFA7A5lmKZm0SRk_MCBzRKsFiQ-d-lfzZADD63JrGphbps6HrG6oBt4pgBqlDpCjd_NdevJ3-JE89xmRXtJ3GGXFNa0HYNGLTzfOA5rv5uaNj554-WNjyIM60R_m9mD08P5R9KRaBOEcWFOwCWtSxbu1iRZI8HpxlXKlwZAwfeF5Ks1lav-8pBuWg3qwjLkGlkodPjNZiP-_GBGei-x_vU7VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاثیرات جالب بادام زمینی بر بدن
🥜
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/694755" target="_blank">📅 10:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694754">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOUMro1Z8LZmg8h7K8vuvZPWUC4DOONhaz1EmKjcinnlQF6uqFzlDWiFDPfM1UjMKNr0pflSGlvQ5xn7xTZRmHFrvAFBhB0jCd5gtGLzKEqSHDXBnh834fiHL-xkYblDlkoYl77dNar4l-8oFF6jskbuyYXvfXT_ml0VknsC8Q-5aSDiJswPV9bPjM6nmOzu3aAGC_WmdUZnINZ07fPw6lMhg4QX_OvSnTMm9hZ1kPZB_eb-RDUaBV5J-H4OOr8U642ct03ap7oDJ2V28vKgOtl6tuGyqfLsJWILoINmg-I_wVCMW8GL8xe7ksqFDjf19UsQmMYRUcp6eX-t-t764w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدام برندهای گوشی بیشترین میزان خرابی را دارند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/694754" target="_blank">📅 10:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694753">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
توهمات ترامپ: ایران آماده تسلیم شدن است
🔹
ادعای ترامپ: ما الان می‌توانیم به راحتی پیروز شویم. من معتقدم بلافاصله پس از انتخابات پیروز خواهیم شد، اما شاید حتی پیش از انتخابات #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/694753" target="_blank">📅 09:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694751">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار سیستان و بلوچستان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9793d08f9.mp4?token=vO5Jt9ck6kZ4H4Il8-5XlQgknpwHJSHRIZpgGGL-e7Sab5eAjclAGKDgorcA3jQ8eQ7bniaop3lLijrIiZWEPh8fv9_BojOk07F8VEgwvvQwHWOQaOszUMFsQ5EBhGUUX6nDl_mH4LwJKUa37V8s-_I8xl90-m3Q_IXz6oDOVzF8PGrbjO3O1sQonXMMPV5A_AA3QJnHSr1vzdI6aoQ8D9r9VG7ir1W4YMSTlvX6oSswYbqMP4Jn1W8mXUsRQXo3CkqOFDyMWYluEKekh1IO3csFW3MC3z3hI0fef-lQvk_efjhTQYxlcpzewMturgi901CTirGiZQV4Up_7nBqSRy2LugvXOLcn0l7sNoFconvf4M14D39EJRzskwg1js5KO6c_0C6Q0NVR5OXfszbTy756tMBBwJ3oA4EAfGhEMTzxdbPj_xEHD_xO9asINN2Gx-BTegzC_2GxuhG0qDB_kVhOdL-jYMTi-B8dCxDxJohMMClIbk9hl1Rcmvg8m0SHbxiKAcByEGnHrD8iQUYMF38MfZMFDXNKkds1EV6BjzRsdZB0T7Ys8MaSqf0diROd6ByMjoisrIBxPoclSz_AF3llYrs7v0W53DTMcomKrtq4rmpQHjTOZ5sfeVgfxU3z27p5qTc_57t1H1VPtf_led8h3TyLomotV7NEwR7Lm5E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9793d08f9.mp4?token=vO5Jt9ck6kZ4H4Il8-5XlQgknpwHJSHRIZpgGGL-e7Sab5eAjclAGKDgorcA3jQ8eQ7bniaop3lLijrIiZWEPh8fv9_BojOk07F8VEgwvvQwHWOQaOszUMFsQ5EBhGUUX6nDl_mH4LwJKUa37V8s-_I8xl90-m3Q_IXz6oDOVzF8PGrbjO3O1sQonXMMPV5A_AA3QJnHSr1vzdI6aoQ8D9r9VG7ir1W4YMSTlvX6oSswYbqMP4Jn1W8mXUsRQXo3CkqOFDyMWYluEKekh1IO3csFW3MC3z3hI0fef-lQvk_efjhTQYxlcpzewMturgi901CTirGiZQV4Up_7nBqSRy2LugvXOLcn0l7sNoFconvf4M14D39EJRzskwg1js5KO6c_0C6Q0NVR5OXfszbTy756tMBBwJ3oA4EAfGhEMTzxdbPj_xEHD_xO9asINN2Gx-BTegzC_2GxuhG0qDB_kVhOdL-jYMTi-B8dCxDxJohMMClIbk9hl1Rcmvg8m0SHbxiKAcByEGnHrD8iQUYMF38MfZMFDXNKkds1EV6BjzRsdZB0T7Ys8MaSqf0diROd6ByMjoisrIBxPoclSz_AF3llYrs7v0W53DTMcomKrtq4rmpQHjTOZ5sfeVgfxU3z27p5qTc_57t1H1VPtf_led8h3TyLomotV7NEwR7Lm5E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیاوش پس از ترک ایران، راهی سرزمینی شد که روزی در برابرش ایستاده بود؛ توران
🔹
افراسیاب درهای دربارش را به روی او گشود و سیاوش در سرزمینی بیگانه، آرام‌آرام جایگاهی تازه پیدا کرد؛ میان بزرگان، در میان مردم و در دل کسانی که بعدها نقش مهمی در سرنوشتش داشتند.
🔹
اما هرچه نام سیاوش در توران بلندتر شد، نگاه‌هایی هم تغییر کرد...
🔹
و گاهی برای آغاز یک فاجعه، نه شمشیر لازم است و نه میدان جنگ؛ تنها یک زمزمه کافی‌ست.
📖
روایتی از داستان سیاوش در شاهنامه فردوسی
این داستان ادامه دارد...
#شاهنامه
@akhbar_sob</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/694751" target="_blank">📅 09:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694750">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
سخنگوی کمیسیون اجتماعی مجلس: کالابرگ برخی یارانه‌بگیران نیم‌ میلیون تومان افزایش می‌یابد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/694750" target="_blank">📅 09:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694749">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f25116db0.mp4?token=et819HyWBPkkrjHxvSlehxqqK-9BL-6upqyUB665-ZwlFK2Zb930tG9UcDqBtfX3XOpW9B9uyJ6PHuKE1OOe2-3kzhG1xB0KgrIB2h0uX10FOmfWIPbFReefmiRJct_q5iP9VBzd7d_0rv87bcRL-ZVl0dxnkCePaoPsTFl_ZDtVIsmPuO0q1pUWhpAnJ6HQ_r3_I35m1PnXwxtbsqmpeDEv0c2uZU0bXRX05Nl6NwAZDSiMModzo_KAB_P54uKxq7lfnNsQTZz_AxbAeNUvtGJtmV9BM94PNfvxUWn4bKSHZumsfZQicRRt7_ZRQprh2sAFBK4h4c8zhVwTM37Ynw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f25116db0.mp4?token=et819HyWBPkkrjHxvSlehxqqK-9BL-6upqyUB665-ZwlFK2Zb930tG9UcDqBtfX3XOpW9B9uyJ6PHuKE1OOe2-3kzhG1xB0KgrIB2h0uX10FOmfWIPbFReefmiRJct_q5iP9VBzd7d_0rv87bcRL-ZVl0dxnkCePaoPsTFl_ZDtVIsmPuO0q1pUWhpAnJ6HQ_r3_I35m1PnXwxtbsqmpeDEv0c2uZU0bXRX05Nl6NwAZDSiMModzo_KAB_P54uKxq7lfnNsQTZz_AxbAeNUvtGJtmV9BM94PNfvxUWn4bKSHZumsfZQicRRt7_ZRQprh2sAFBK4h4c8zhVwTM37Ynw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع عربی با انتشار این ویدیو از انفجار در فرودگاه نظامی تنفتناز در حومه شهر ادلب سوریه خبر دادند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/694749" target="_blank">📅 09:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694748">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCBZNAICUmiIO7i_XZQI9jXW2NeyMjSUMTq5SYbZNMl1gZI64507r0iB6oUWNyPkXV4osPqTa29iHbaftLoHrX61gRA-rKReQ1FZCRcUniefRlVVNUgP5q-dxxOnhAHA7Js0vQzyx9ADTCNiUmSa-59hmG04p4YYCflO3plmlIGR8qwvszhm9uYrCEeU8vByYTczdrRzz54ktl-A9xz_YuzwV1Of6M6YRea26KuC21nr-H5YZ75YSS6O6me6z9-CeKSZ8f1TbFwiZ9gvWlzQ7mxNVuLnkXOIB85eq7CgMR-u-uBHi_nrd1CIvO1CWo_cUAZSsO1JST0BysV6VKlONA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قابلیت جدید ChatGPT: لباس‌های مختلف را مجازی پرو کنید
🔹
اوپن‌ای‌آی قابلیت پرو مجازی یا Virtual Try On را به ChatGPT اضافه کرد تا کاربران بتوانند با آپلود عکس سلفی و تمام‌قد، لباس‌ها را به‌صورت مجازی روی تن خود امتحان کنند.
🔹
این قابلیت با مدل جدید ChatGPT Images 2.5 کار می‌کند و حتی می‌توان از اسکرین‌شات لباس‌های خارج از ChatGPT نیز استفاده کرد. OpenAI همچنین امکان ذخیره محصولات مورد علاقه در Library را فراهم کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/694748" target="_blank">📅 09:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694744">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e94a1e43b0.mp4?token=bLYO6CVznPenG5fVM6wdFCZF2SMx3WMuEqoAOUqVhzb6W9zTgVerYcue2boWHGh5q9Kc5VziEOwop2D5ARqD9TF_AOnpXTZudq-1EcAGiQ59dy2jrUaF-b2_JG51DuEl03XA8eo8capDPvw7jxphoaEG3K2x4CfiS6ZUh-b9CEVBnLjFLGodB-6a1GOM_exUCEIoXmTrxUf50FWJJ_wJ3m-YrWZ6XzwIPv_h1GLW1qCYsulX1RK9gtiK9s9dF8A_YhVkx0-BN9WFY2r1hnveN1wZkcgM14JhCnMQXf-ty2vps5YKRFfiVHI7e0wOfZ3b3q99TwIVgm6iSRUOjtYf3V30bS4xv_XvoGrQvAcs-ZN9OZT09h9GojNVYYMOyPKb0kxtmbcM-q81otKcb2vUeVacwOTSd4qH7r73d-pjyLKrG8PGwutNFDUTRMbnX1qsWZF-HxfNyy8DX1vXBCUe64BCFhqHAWCBXmVfrZi9YHk1h040qk8v6aMpxk5wM6pfe4efdg-jAVDk5V79T6lLPQreclBunsW5nVu86TZkDn-fYKYLEJ69cvBv5zk28AY05qEN0RCECKfIZgu75XxgmAiyzTfijPH_m62Ah7JOkVxUF0taHzUdLnes4-TnD1rKExc8WNvQflaSquqGEm5cfj9k2KIoHiQD2UqG_wetEQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e94a1e43b0.mp4?token=bLYO6CVznPenG5fVM6wdFCZF2SMx3WMuEqoAOUqVhzb6W9zTgVerYcue2boWHGh5q9Kc5VziEOwop2D5ARqD9TF_AOnpXTZudq-1EcAGiQ59dy2jrUaF-b2_JG51DuEl03XA8eo8capDPvw7jxphoaEG3K2x4CfiS6ZUh-b9CEVBnLjFLGodB-6a1GOM_exUCEIoXmTrxUf50FWJJ_wJ3m-YrWZ6XzwIPv_h1GLW1qCYsulX1RK9gtiK9s9dF8A_YhVkx0-BN9WFY2r1hnveN1wZkcgM14JhCnMQXf-ty2vps5YKRFfiVHI7e0wOfZ3b3q99TwIVgm6iSRUOjtYf3V30bS4xv_XvoGrQvAcs-ZN9OZT09h9GojNVYYMOyPKb0kxtmbcM-q81otKcb2vUeVacwOTSd4qH7r73d-pjyLKrG8PGwutNFDUTRMbnX1qsWZF-HxfNyy8DX1vXBCUe64BCFhqHAWCBXmVfrZi9YHk1h040qk8v6aMpxk5wM6pfe4efdg-jAVDk5V79T6lLPQreclBunsW5nVu86TZkDn-fYKYLEJ69cvBv5zk28AY05qEN0RCECKfIZgu75XxgmAiyzTfijPH_m62Ah7JOkVxUF0taHzUdLnes4-TnD1rKExc8WNvQflaSquqGEm5cfj9k2KIoHiQD2UqG_wetEQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری از اعتراض دانش‌آموزان دبیرستانی در فرانسه
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/694744" target="_blank">📅 09:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694742">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d566ca9f4a.mp4?token=dBCHPnB8X5mcrLLU5HUc3IhMGib7jPzc9YHWOBAXLw2lo0dqAPQarmuDGUVgDSURp7jTdIOEkXjPIkK-iIZbNOEcTiM4TDkpPpXWtYS2KXU3rlY7DgrifcZjiY5Iv4VPfY9W5r9qEsJbXjtzVZGE2ozyOHh2KCwzb2oddSzP2-xlq7rIKL40pv10b1sayBiNIG1j9IqM1Sh0UW7pGYTIg_Kwe-Uw7zDFdQo1cOiuiFmX6GH8CzG8d3MzCR2c8hPYavCLSQSht4-woLs3ZvUibxf-FfwlU2XyAof63I2CE1yFxD3_Lh5A1x0qiSAHJ_Q0VBNXPm3OQZdV9uF9RUOhrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d566ca9f4a.mp4?token=dBCHPnB8X5mcrLLU5HUc3IhMGib7jPzc9YHWOBAXLw2lo0dqAPQarmuDGUVgDSURp7jTdIOEkXjPIkK-iIZbNOEcTiM4TDkpPpXWtYS2KXU3rlY7DgrifcZjiY5Iv4VPfY9W5r9qEsJbXjtzVZGE2ozyOHh2KCwzb2oddSzP2-xlq7rIKL40pv10b1sayBiNIG1j9IqM1Sh0UW7pGYTIg_Kwe-Uw7zDFdQo1cOiuiFmX6GH8CzG8d3MzCR2c8hPYavCLSQSht4-woLs3ZvUibxf-FfwlU2XyAof63I2CE1yFxD3_Lh5A1x0qiSAHJ_Q0VBNXPm3OQZdV9uF9RUOhrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
املت لوبیا سبز
مواد لازم:
🔹
لوبیا سبز ۲۰۰ گرم
🔹
گوجه فرنگی ۴ عدد
🔹
تخم مرغ ۴ عدد
🔹
پیاز ۱ عدد
🔹
سیر ۳ حبه
🔹
ادویه ها (نمک ، فلفل ، زردچوبه ، پودر پیاز ، پاپریکا)
🔹
شوید خشک در صورت دلخواه
#آشپزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/694742" target="_blank">📅 09:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694741">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم النور 4_ جلسه دوازدهم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/694741" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه دوازدهم؛ گذر از رنج
🔹
در دوران تکامل فرهنگی، انسان‌ها باید مراقبت کنند که دچار اختلاف، جبهه‌گیری، دیکتاتوری، سرکوب و رنجش اجتماعی نشوند و در احترام، فرهیختگی و راست‌کرداری باقی بمانند.
🔹
در این دوران که جدال خیر و شر آغاز شده است، استواری و پایداری بر درستکاری و خلوص الهی می‌تواند نور خیر را تصفیه و هر روز شفاف‌تر سازد.
🔹
انسان در خلوص الهی باید از زخم‌زبان، ریاکاری، آزار و گمراهی کردن مردمان پرهیز کند و صبر، نیک‌رفتاری و جوانمردی را در پیش گیرد.
🔹
نام‌های مبارک الحی و القیوم، نور زندگی و حیات‌بخش پروردگار را در ذرات وجود انسان‌ها و سرزمین‌ها جاری می‌کنند، دل‌مرگی، ضعف و سستی ابلیسی را پاک کرده و منبع امید و حیاتِ پاک برای مردمان می‌شوند.
🔹
گذر نیکو از دور سریع تاریخ و فتنه‌های آخرالزمان، تنها با زیستن در نور اسماءالحسنی، خدمت خالصانه و تطهیر جسم و روان از منیت، امکان‌پذیر است.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/694741" target="_blank">📅 09:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694740">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ادعای نتانیاهو: خلبان هندی ناجی جان ۱۷۴ اسرائیلی در پرواز فلای دبی بود #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/694740" target="_blank">📅 09:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694739">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/of3IrDTeX4uCgvdP--JDbwYd6k2aLkNg2OVyi5thbj8oVvSd1kDlm1T3cWSwj0IeUOIWx-G2Q8m_TgbyphgMSzBWLSnCWp2X3Jg3gtuIe-pLNzM6DtSDOeADhQ4ZjxNqGy2Q-8nwX1Nazo3TORmo2oIc1oIcaemFaIavIaTeWp9q8EnwwMI7A7qVrBXPLZWRyaGsg2cCm2QLQ2HD19R3OZd9YlLLi075_P45YnJmrsdJynFjCBWvPPycrlYg7XN2yHgmI_cbWIlCGofySvhsWSmIHlQBYO69zcNFF8pfutcDMJK5CqKfGc_8fSHc1dqop_hH1nw4dgXN4Ibo3-GICg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شب‌بخیر امارات!
🔹
تصویری از پهپاد شاهد در بلوار خوردین شهرک غرب| محل سفارت امارات در تهران!!
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/694739" target="_blank">📅 09:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694737">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdeaba89ed.mp4?token=ZrGg5yHnvqseySobkceSzxflmGyuBhyQBV3FcC8xX6H44nM9eeLBK79R18Kiiy6f-Gj0vJS0pHKA63MMe3d5gkgJ1pLgNpzilNsFV09v7sF3o4viXSxOYOkEukLrfvkfL4vW57LON5KWDOOrbn1cNqDI7v7eIt_Rh4JVHoVBNBjt2TiF8CNjBOS01dHPhG3wsbbL-H1eC4q4Wjzs3fz7QDWW3eSVkyN8lNxvRS0ebmvcakpm7ceQ7cC3QSSj9YFTJvQyrlc7lw_rUTx-KRNj8ZL0i4egSJefVGvxXojfSGReTlZKQ4KfFG3wlbJwH1KbEQH8Jv0JLeaHQhAAKH8Fjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdeaba89ed.mp4?token=ZrGg5yHnvqseySobkceSzxflmGyuBhyQBV3FcC8xX6H44nM9eeLBK79R18Kiiy6f-Gj0vJS0pHKA63MMe3d5gkgJ1pLgNpzilNsFV09v7sF3o4viXSxOYOkEukLrfvkfL4vW57LON5KWDOOrbn1cNqDI7v7eIt_Rh4JVHoVBNBjt2TiF8CNjBOS01dHPhG3wsbbL-H1eC4q4Wjzs3fz7QDWW3eSVkyN8lNxvRS0ebmvcakpm7ceQ7cC3QSSj9YFTJvQyrlc7lw_rUTx-KRNj8ZL0i4egSJefVGvxXojfSGReTlZKQ4KfFG3wlbJwH1KbEQH8Jv0JLeaHQhAAKH8Fjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداحافظی گوش‌نواز سفیر ژاپن از مردم ایران
🔹
تسوکادا تاماکی سفیر رسمی ژاپن در ایران که پیش‌تر در آستانه یکصدمین سال روابط دیپلماتیک ایران و ژاپن، موسیقی سریال پرخاطره «اوشین» را نواخته بود، این بار برای خداحافظی با مردم ایران در پایان ماموریتش، در کنار این ارکستر، موسیقی آثار میازاکی را نواخت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/694737" target="_blank">📅 09:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694736">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf8c12104c.mp4?token=GfWGc9nxy_4WNaT72yCjYCb9mbbpuNJ8Ya-WzN79T5p91JRRFdBKxybVRtEeEvCX-oguz3oBAaQmWPQwEno6KzmodNfB9IEaTVQTlNp0uo9BQieUYpeTL_pZ8IRUa6JAY-cP675fdP6p0OD3UdQ8m1HbLWWPj_nMaEx1JOz3Ea0Bz5jdkYpoh7cDJFd00tplfdiB2spIBYoMQYpIQ97jLbZz-HTL0WWpgIkOz4niVaAvYTD5jjspzUVBpg4PFdnQz8GcrTcIqlbGaFhUxnc9MiB9-gmD4a0mfm6re4LJcemyfE_ifMpvuq8ID9Qd4AD5u9VUFHxf1e-6-aTKUkd4Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf8c12104c.mp4?token=GfWGc9nxy_4WNaT72yCjYCb9mbbpuNJ8Ya-WzN79T5p91JRRFdBKxybVRtEeEvCX-oguz3oBAaQmWPQwEno6KzmodNfB9IEaTVQTlNp0uo9BQieUYpeTL_pZ8IRUa6JAY-cP675fdP6p0OD3UdQ8m1HbLWWPj_nMaEx1JOz3Ea0Bz5jdkYpoh7cDJFd00tplfdiB2spIBYoMQYpIQ97jLbZz-HTL0WWpgIkOz4niVaAvYTD5jjspzUVBpg4PFdnQz8GcrTcIqlbGaFhUxnc9MiB9-gmD4a0mfm6re4LJcemyfE_ifMpvuq8ID9Qd4AD5u9VUFHxf1e-6-aTKUkd4Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت عجیب پوشش یک مسافر؛ مترو تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/694736" target="_blank">📅 09:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694735">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KY9nkdi0KgrMVt99JwU3ZOvjqg-ggMnXARB9DbxwzoQEuvYqORQkZI2M0QOIu_bEfL5KWYxPrtcqX6vYJ735Ab4TTYoMrtK4mAjocGldLO7Ykb3-jCowQq4i_QOSxmtWhcxec3I07WFm7f7xpy_NkAhCXeo2wbHBwe4anzn-_lQFTIwPqpAFeU5O1_JIm0ZWZMlFfbCzHe-H2B_G50MEwxUFd4fL8CNBXLSE0pD4j_qc8OKzFITJbmBW59vGBanp8R1kMjIQccQyQhu-WJebW-ifXjiUt0nocdwUNA3PyeZ5YYno09_9ZwOQVNv0Od8WsXxh3BYtLj32XYLXpD8zxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای هر سلیقه یک کتاب؛ فهرستی از پیشنهادهای خواندنی در ژانرهای مختلف
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/694735" target="_blank">📅 09:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694734">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YABRshOFq6uA_GcHtAZYtx8jA79GLODNLhIysGjkGFiwde8uejUCl91BJGkY7b_d3pvqHK13l-ZjcU4pCVGl56W9DGkAY0UbW1XSk2NHxmgy0r3OxINN3KLmOFxCmIYopjP5wl_KLKr9WXK2nbOA4glcRs0eR_9CBXKctT9609WILpmNFSn3eDkgO98eYWGeyFhvIEXUi0Y_Scte6IVMKBp2w9wJEmYKyhvRzos0L6ja5vyqegJjphIgzaizp_vnEB4VX44YUaCkNRK-JWStTobaRotzRvZk_Dv0iFU3qEzs2zMWsbNK8L8IUGvDDh2BEinckpKOWukrzfkwSQk12Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتراضات دانش‌آموزی در فرانسه؛ ۶۲۵ نفر بازداشت شدند
🔹
دانش‌آموزان فرانسوی بخاطر شرایط نامناسب مدارس دست به اعتراض زدن و در خیلی از شهرها، اعتراضات به آتش زدن سطل‌های زباله، بستن خیابان‌ها و درگیری با پلیس کشیده شده.
🔹
تا ۳۰ سپتامبر، ۳۵۶ دبیرستان تحت تاثیر…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/694734" target="_blank">📅 08:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694733">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
سردار قاآنی: آمریکا با وجود همه امکاناتش از عراق اخراج شد و در برابر ایران شکست خفت‌باری خورد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/694733" target="_blank">📅 08:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694732">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQxCwIiKM095DgNGHGjyoHyjLVPmFDQPLzxRqKBxacmcM77x4llDF89og-dNN641_hRuU8KTpFFuDiMt2ZkbzdZ9ZUwsqzrpEOybbqt5DGG1JZhLu5HC9VdKeJQgT0Rl39pczMhkjFh_Z3JUm52oQhHhWwffZGggp2Czn0GW8VFG4WTVwghJ6VOSIOcDWVjZB7mnhHpmyH-kfcVcqinXZnY49qS6CKl88130tbTcYDGPGtR6vrpQSZQiZuIvD1bdHiehvdRh61Fp3g7NoXb3YGzboRj8XUIqqEhvSFfDDNIheQbxAcGxXnA1wApFB_s9VxSIyQnCe9gNdnv80wvDCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر منتخب ماه سپتامبر رویترز/ تصویری متفاوت از دیدار ترامپ و شی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/694732" target="_blank">📅 08:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694731">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76db34fa6a.mp4?token=bSpHxaWY51DQFVa0I9VISlzZwQq4OK6rORQ9QNXpb6OdYsr2DOheZMS7C1MIj9Frce7JpZdBJTIuP7_mggP26gmCqpdElJzGolR-KNbAsH3J_OBjkmhO2ga2E8VZ4syAeY0FEEk93Qrid8mC5z5awtmxq1gPEZbaC8eaaRaK-nh4eVGPuFkFUqVeD7IcEbva_F3A-BP--c6mWstqr2ZVSEzzD62yD-OxapoSkty07BtudSsUFfS4-0Iq-Bk-aRxh8k-kV1corvxBpNeZP6onXOg67RKnjSpxoc9IF5MPSkPQNUgjHg21vlYBuL9bGiaHJCYXlinllxFXNErKYkNBJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76db34fa6a.mp4?token=bSpHxaWY51DQFVa0I9VISlzZwQq4OK6rORQ9QNXpb6OdYsr2DOheZMS7C1MIj9Frce7JpZdBJTIuP7_mggP26gmCqpdElJzGolR-KNbAsH3J_OBjkmhO2ga2E8VZ4syAeY0FEEk93Qrid8mC5z5awtmxq1gPEZbaC8eaaRaK-nh4eVGPuFkFUqVeD7IcEbva_F3A-BP--c6mWstqr2ZVSEzzD62yD-OxapoSkty07BtudSsUFfS4-0Iq-Bk-aRxh8k-kV1corvxBpNeZP6onXOg67RKnjSpxoc9IF5MPSkPQNUgjHg21vlYBuL9bGiaHJCYXlinllxFXNErKYkNBJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نحوه دست دادن سرلشکر رضایی با شاهین مصطفی‌اف، معاون نخست‌وزیر جمهوری آذربایجان، مورد توجه رسانه‌ها قرار گرفت و به سوژه‌ای خبری تبدیل شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/694731" target="_blank">📅 08:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694729">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b914977401.mp4?token=ZIb2MiUZzAlxWEuehbA7pSMcA-fxMWTIggT_sKObup2nHOPaiO-WaGFv_QIz1LdJ822pKK_ahv5ZqpnnurhA_UG1s1Nii4bDNhWhofnNhp0IZB6BpnaPh5fOIYItMsLA2B0Edw0x7l7hFVTM3xSL3sJmOLhsXTEYflD-DFmzwG5fVVJflUFEdbx3xiw9SJ9KIN4ABZ2mC5Tzslq7rfKaEazNaFXs7G_CYFW4Cy8ErWFj9kaPStA9LjY-0VFWdbukZCyS-rwTRNBLKN1zNYgRU4T9oWNNfepXq4IqLtvS2LNH56dcdQGTkY3qo3jpZCvcusqSyWw40Kx9iFO9sLytbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b914977401.mp4?token=ZIb2MiUZzAlxWEuehbA7pSMcA-fxMWTIggT_sKObup2nHOPaiO-WaGFv_QIz1LdJ822pKK_ahv5ZqpnnurhA_UG1s1Nii4bDNhWhofnNhp0IZB6BpnaPh5fOIYItMsLA2B0Edw0x7l7hFVTM3xSL3sJmOLhsXTEYflD-DFmzwG5fVVJflUFEdbx3xiw9SJ9KIN4ABZ2mC5Tzslq7rfKaEazNaFXs7G_CYFW4Cy8ErWFj9kaPStA9LjY-0VFWdbukZCyS-rwTRNBLKN1zNYgRU4T9oWNNfepXq4IqLtvS2LNH56dcdQGTkY3qo3jpZCvcusqSyWw40Kx9iFO9sLytbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتصال نخستین توربین بادی ۲ مگاواتی با طراحی داخلی به شبکه برق
وزیر نیرو:
🔹
این توربین به منظور انطباق بیشتر با شرایط اقلیمی ایران طراحی شده است./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/694729" target="_blank">📅 08:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694728">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
اکسیوس به نقل از دو مقام آمریکایی: آمریکا دو سامانه پاتریوت دیگر برای حفاظت از تاسیسات انرژی به عربستان و قطر فرستاد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/694728" target="_blank">📅 08:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694727">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/694727" target="_blank">📅 08:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694726">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/235fc9796e.mp4?token=ctuHLLXn2AjWVOzaHZUtw4uiw3EB0S_fQveeo19T-3biDSe4Vp0Kkt_RzO_SVlnQBsgwnr89VHyjOH0vIf1g-4OWjG9BFW0rpMwI6-NZFSjWN2Op9IL4pZKLJa_oY_3P8dgrjsMqKJz5NfeY_MDLYSMeWzaLKe7cl49aYzikWqeFSSHqI82A5CoDWgYDPUfYV6HDizr3VbMu_ajq_b50w4pfZQoA-9-bmKqEZHbGdor8DfakxHhxkVWt3ci3IAW95I7xuIVKl6-Awe3COX1vzoLiv-BXDMuPzAZMieQaGy6gCG9za7xKcL5929KbqL5gh5d8-qLAF5nWuWeE24wzWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/235fc9796e.mp4?token=ctuHLLXn2AjWVOzaHZUtw4uiw3EB0S_fQveeo19T-3biDSe4Vp0Kkt_RzO_SVlnQBsgwnr89VHyjOH0vIf1g-4OWjG9BFW0rpMwI6-NZFSjWN2Op9IL4pZKLJa_oY_3P8dgrjsMqKJz5NfeY_MDLYSMeWzaLKe7cl49aYzikWqeFSSHqI82A5CoDWgYDPUfYV6HDizr3VbMu_ajq_b50w4pfZQoA-9-bmKqEZHbGdor8DfakxHhxkVWt3ci3IAW95I7xuIVKl6-Awe3COX1vzoLiv-BXDMuPzAZMieQaGy6gCG9za7xKcL5929KbqL5gh5d8-qLAF5nWuWeE24wzWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت آتش‌نشانی تهران برای اولین بار از نجات مسئولان بلندپایه پس از اصابت در ارتفاعات
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/694726" target="_blank">📅 08:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694725">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
اقدام عجیب سنگاپور برای افزایش ازدواج و تولد؛ دولت هزینه اولین قرار را می‌دهد!
🔹
سنگاپور برای افزایش ازدواج و تولد، سامانه‌ای همسریابی برای جوانان راه‌اندازی کرده؛ کاربران روزانه با یک گزینه پیشنهادی آشنا می‌شوند و در صورت قرار اول، هزینه آن را دولت پرداخت می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/694725" target="_blank">📅 08:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694724">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6f975755.mp4?token=oNu8Zlxmy-z4I0RXZjeoTrWBXtoMGsrVRl2Ruw_9sp54ZJpLcz55bfjFfGiwQtfGxN2fz1NTTSiUtT74f2Kpkw_gUUsZZ-A9WOswI68DhnbTV0SWHpnuZ257a7ZJ6roS_QVguVAFaytgI8yVH_YTT7I_GHrRMzrWD6pDKNWqIvg8VlarN3qxYoTns2x6WPw09yCWElfq2dYKblrlg21sXCOEx2lbMWLVIdOcrXUSnAK-Ll8_eBH5fFgZcdqz_5HPz68EJ-uQ5lLgHs7MPDjOjSo8raBx4wIlUOAPdvMKcCXJpdBWPqfv-hBJcVCEzIxpYVnzR2GEUKtAia0MrhUdyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6f975755.mp4?token=oNu8Zlxmy-z4I0RXZjeoTrWBXtoMGsrVRl2Ruw_9sp54ZJpLcz55bfjFfGiwQtfGxN2fz1NTTSiUtT74f2Kpkw_gUUsZZ-A9WOswI68DhnbTV0SWHpnuZ257a7ZJ6roS_QVguVAFaytgI8yVH_YTT7I_GHrRMzrWD6pDKNWqIvg8VlarN3qxYoTns2x6WPw09yCWElfq2dYKblrlg21sXCOEx2lbMWLVIdOcrXUSnAK-Ll8_eBH5fFgZcdqz_5HPz68EJ-uQ5lLgHs7MPDjOjSo8raBx4wIlUOAPdvMKcCXJpdBWPqfv-hBJcVCEzIxpYVnzR2GEUKtAia0MrhUdyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر ساعت‌های زیادی می‌شینی یا با موبایل و لپ‌تاپ کار می‌کنی، فقط ۱ دقیقه در روز برای شونه‌ها و قامتت این حرکات رو انجام بده!
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/694724" target="_blank">📅 08:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694723">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
اعتراضات دانش‌آموزی در فرانسه؛ ۶۲۵ نفر بازداشت شدند
🔹
دانش‌آموزان فرانسوی بخاطر شرایط نامناسب مدارس دست به اعتراض زدن و در خیلی از شهرها، اعتراضات به آتش زدن سطل‌های زباله، بستن خیابان‌ها و درگیری با پلیس کشیده شده.
🔹
تا ۳۰ سپتامبر، ۳۵۶ دبیرستان تحت تاثیر اعتراضات قرار گرفتن و ۶۲۵ نفر بازداشت شدن. همچنین ۸۳ پلیس و ژاندارم زخمی شدن.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/694723" target="_blank">📅 08:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694722">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
طالبان: تحریم هوایی ایران را قبول نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/694722" target="_blank">📅 08:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694721">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
سخنگوی وزارت آموزش و پرورش: استعفای معلمان شایعه است/ عده‌ای دنبال تعطیلی آموزش حضوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/694721" target="_blank">📅 08:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694720">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f413bda660.mp4?token=p40ofH-C8yAQpg5YCUOTN57LZ39O5ZyScy69hsGi2OeJyRwrZzmFi8iiQ2NRm7ZH5zvBWDigmMMVkw30HD9OSKEekJp0_u6T7ZKNj-UhnV2Ja55bGy6OSu3_PYS6ZSOFvJfOCp0J8daCcMfuCS0emx2UWoKs_AAM-q-KSYwYQyVquqRMi3I_x13lZFcESUqmOfon2hWpFS8EIiekrWz_KC5XfcQbdk1wNCTNW7vqreMDogxMxPIfHhlrDz9Lh-J3lufTIv2ZIZ7--L-ui0XfYiCBRbGa8BXBfRvRZNkN-2yxD5TS27DEmdflhkB6rQthj196zZPTKnezPqcNRjZI4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f413bda660.mp4?token=p40ofH-C8yAQpg5YCUOTN57LZ39O5ZyScy69hsGi2OeJyRwrZzmFi8iiQ2NRm7ZH5zvBWDigmMMVkw30HD9OSKEekJp0_u6T7ZKNj-UhnV2Ja55bGy6OSu3_PYS6ZSOFvJfOCp0J8daCcMfuCS0emx2UWoKs_AAM-q-KSYwYQyVquqRMi3I_x13lZFcESUqmOfon2hWpFS8EIiekrWz_KC5XfcQbdk1wNCTNW7vqreMDogxMxPIfHhlrDz9Lh-J3lufTIv2ZIZ7--L-ui0XfYiCBRbGa8BXBfRvRZNkN-2yxD5TS27DEmdflhkB6rQthj196zZPTKnezPqcNRjZI4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اهالی بخش «التعزیه» در استان تعز علیه مزدوران عربستانی بسیج عمومی تشکیل دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/694720" target="_blank">📅 08:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694717">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZDsIXew4nd3MXJh8r4LJjaSkIfwb-nbo_3Z7ZV-WrWaDXJJQOWvHqHg6-A0VvHh5HQAZdJNqtyHGe8LyQQTg2JTzHPtLqGBKGrYzLfYw9qWPeI2oDMCCz6JVK4fQg4FaHU40DXQPID3ji_gfcUxlMjz6tbO_qAV-IZss4C25u5DLSweq4FxV3v7J1NW-LHje-HwuNFfuB2KLWEzMRqN4GB4Oimcn9j1qv1g-bCYC5jQ8IouDJVzjPa69YhGevSmXrjOoLdp8YEvjQLE_M9UcGDr0Ys42aBJUTLpH_ypNHEtFeyrV0aA1Yv1eOIOVLoLGDRB_SLm5BqY54uRUxazx0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OFmbzMBCvtrDFUsUWqJvmdlYK5OY7ejn8JoVS0fK7_NNbW_aXxdFQjV85bzzqtiKLlU_fny43RRbbeasbDzH0PHa9TPxPOpMa4Dvq1D_dympp-dpVMc_7YmobogEzoi9AQX7WMc7YviNjkb15GEAFK-dPUobR5liRD61NNf3rmV8gLIa0yYFB45evZnJ-UB2ZmZfrvEEsRrCwHEBwrtw-Fsd00rl9WeV4lkhpfNC4x5gr6cD8auWxDh56i62Agl7bYqymrrGPJlvLZewmmwxJ1_EUYto85KsOizGdVQm1GyuYhCV96N7BC7e8pb6XGtWTIL9-Ac3D_nTMCfdQ8tPXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AxTorCcqY6XBbOtIGNv30owG3dRW5KA_URPIjdooyjTx_YmZX7szbz-xLxNxfxLeHurG84J1QtjnfkkZHz8964W5LlnvTdiQaLBt7dzUqDd3AGK5FuD2nRAPvI9RARq9OKToc11BR9a-SP1D4mT4P4wdFi6IX3_wsbQogwTrCMAO7Snw9ED30rH5lk2RSLEjtSSTW6VVjTyHJFNeE59fvRAQqy1nCIKlIpkLzNG4NtrJ7rbwNoIQbYBJTMMabGP5k7WJL6L7YGfzQUsL8KiF1rPV2I_vSRS50-YRtvGWZ4jSZUkpdplRRuRiGJPuBKVC3OsOOzoawJYiDGB10t8WBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گام نهایی سفر وزیر ارتباطات به سمنان
از آغاز ساخت مجتمع ICT تا دیدار با خانواده شهید باصری
🔹
در گام نهایی سفر سیدستار هاشمی به سمنان، عملیات اجرایی مجتمع فناوری اطلاعات و ارتباطات (ICT) استان با حضور وزیر ارتباطات آغاز شد.
🔹
به گفته وزیر ارتباطات، با تأمین زمین و پیش‌بینی منابع مورد نیاز، هدف‌گذاری شده این مجموعه تا پایان دولت چهاردهم به بهره‌برداری برسد.
🔹
دیدار با خانواده شهید باصری و آیین پلاک‌کوبی هوشمند GNAF منزل این شهید نیز از دیگر برنامه‌های وزیر ارتباطات در سمنان بود. شهید باصری در جنگ رمضان، ۹ اسفند ۱۴۰۴ به شهادت رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/694717" target="_blank">📅 08:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694715">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
ادعای جدید ترامپ: به نظر می‌رسد ایران در حادثه فرفورد دخیل بوده است
🔹
ترامپ: ممکن است از اروپایی‌ها بخواهم ذخایر اضطراری گازوئیل خود را آزاد کنند #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/694715" target="_blank">📅 08:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694713">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc1ce4b41.mp4?token=gsjjIKNOhxX1tw9H6Myn9Udk2DxPbQ8gC9vEV5bPu7SKKsD1qz-GCXBRIEr05fM-0JPJ9H-hIdu0pUYCKK4DYbW2mz71X-uIL2ZpORG7Y2NXLsfFcIl8r-yT81vNU9YrZZhu1rPxif-qqnqpw1XAPjnmzr6hL1dzrdQWsYcz4dQUK_rm5n9uNRZPCKHGLuVcTFZcolXweaDg9GmAuddPZxHrmhDYg2heosYW9cKZfBM4ARGvfCvxTQb7ciBOoM6hj8c_Dj7qKqTXGepgembWa2KcyiVNYrZVtzXFF_qFELXh46IUylk8PTA0niWW31DtNmnkovN6XnLeY3GlUe9wfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc1ce4b41.mp4?token=gsjjIKNOhxX1tw9H6Myn9Udk2DxPbQ8gC9vEV5bPu7SKKsD1qz-GCXBRIEr05fM-0JPJ9H-hIdu0pUYCKK4DYbW2mz71X-uIL2ZpORG7Y2NXLsfFcIl8r-yT81vNU9YrZZhu1rPxif-qqnqpw1XAPjnmzr6hL1dzrdQWsYcz4dQUK_rm5n9uNRZPCKHGLuVcTFZcolXweaDg9GmAuddPZxHrmhDYg2heosYW9cKZfBM4ARGvfCvxTQb7ciBOoM6hj8c_Dj7qKqTXGepgembWa2KcyiVNYrZVtzXFF_qFELXh46IUylk8PTA0niWW31DtNmnkovN6XnLeY3GlUe9wfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشف ۵۲ دستگاه ماینر غیرمجاز در شهرک صنعتی کنگاور
#اخبار_کرمانشاه
در فضای
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/694713" target="_blank">📅 08:14 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694711">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ایران‌خودرو و راه‌آهن در فهرست تحریم‌های آمریکا
🔹
در فهرست تحریم‌های خصمانۀ آمریکا علیه ایران که امروز منتشر شده نام شرکت خودروسازی ایران‌خودرو و چند شرکت تابع آن و همچنین شرکت راه‌آهن ایران دیده می‌شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/694711" target="_blank">📅 08:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694710">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
عملیات انتحاری در مسجدالحرام صحت ندارد
🔹
برخی منابع خبری خارجی ویدئویی قدیمی را با این ادعا منتشر می‌کنند که مربوط به خنثی‌سازی یک عملیات بمب‌گذاری انتحاری در مسجدالحرام است؛ اما ظاهراً این ویدئو مربوط به فوریه ۲۰۱۷ است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/694710" target="_blank">📅 08:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694709">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIeumBtSIBFBI9ETNYmk3DTQSNPXDhnq6gPy0EzEK9GJ8yyNBV5qEEf48DLpH_GvBFnSbdvAtHP43fxa5KXqtE7xI42G2Bz-gVZWesCAvGqbU3NAn4fHGTjKF3kG5nrutcem9iv2eRsMAh76f9WpdJkupyTG_4uzEwX-2vo7pCViupQOooHzoD0ZD3DI4fO5q9oxpmZOyjXCkU2AaR2ID2MnC35W3rzpyDyvfBiv7BpjjElNSyCzz4wUW0lOSTxxE1sCuXoYMXkpr43OYxJcTXlTzS6lT2lPz1NBQg9E6-zpuIRKZhoOpf9S8U3pcY4frn1T8CaxY9L3Hf2nkyZ-7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۱۰ مهر ماه
۲۰ ربیع‌الثانی ۱۴۴۸
۲ اکتبر ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/694709" target="_blank">📅 08:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694708">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1KQde-m7QVmrBy1YAPTj2ZNKE6zVcmjhfZs6TYh_YsR55PgDKlvbvVCrtrfgDReT0bbcedZHwHL9o6-7uLUaAwqC1ZT6SSOu5HNXyQv7y4kHdEEnECCoVrtvPAbb4OAE8sheNEmLwFsn3sMPA6jDDKsydDAX3Alglm1I6qsalHM7-164m52EkRPMhvW59iMgYTpvqQTTaPwzGUzyosjKjiGmbobfnDmN9Z3xJqvc-wSFLJg6HB-GC-x5v1utTt90-hs2K372-s4v_oKqvFSe7sTM3j5xxDXJgdez6oppX3uAoaL0gLyjFJyWkyNvXRUjQZBtpZBepdPZu0HiqRJEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧥
پافر کلاهدار زنانه و مردانه Zinox | دو رنگ خاص برای استایل پاییز و زمستون
🍂
❄️
سبک، گرم و ضدباد با پارچه مموری؛ مناسب برای روزهای سرد و بارونی
👌
🎨
رنگ‌بندی:
مشکی | سفید
📏
سایزبندی:
L | XL | 2XL
💰
خرید نقدی درب منزل:
۲,۱۸۰,۰۰۰ تومان
💳
خرید قسطی:
۴ قسط ۶۳۰,۰۰۰ تومانی
🔄
ضمانت تعویض ۳ روزه کالا
لینک خرید مشکی
https://memarket24.ir/product/fast/64809/180124/
لینک خرید سفید
https://memarket24.ir/product/fast/64808/180124/</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/694708" target="_blank">📅 00:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694706">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
سردار قاآنی: آمریکا با وجود همه امکاناتش از عراق اخراج شد و در برابر ایران شکست خفت‌باری خورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/694706" target="_blank">📅 00:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694705">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd21e9719d.mp4?token=cHsHHZRxTP6BCwiV4ZAmCNeyru0LTYAMwRQPVbkZjSJq2gcaBL0PyPjgnfnYFEYIcIlfxDaY91JD4W32w7oRxgwAd9ta0CMhJ6esxpzS9zD6trA_zPrFd4V-yg7Xc_IUGoQVpRD4kwTwiCXIDTorucfMCX8XYyrtwyw-uPLWtAEy1rBk6Mi8RuT0sAOCz5PcD1VUaqOEaePfuSjTd2XtLVIX55npNXN13fAxwEiI4ED5CqpoIXy-YfMth5zMRu_dQVaJVx5PdmOqS_yE4AQ9UOGzvqFzqBICm-5OV-FE7FRoRcVlZwajvC-z-jzwlLMbaVf7kHnV-nyylpL7dwdziQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd21e9719d.mp4?token=cHsHHZRxTP6BCwiV4ZAmCNeyru0LTYAMwRQPVbkZjSJq2gcaBL0PyPjgnfnYFEYIcIlfxDaY91JD4W32w7oRxgwAd9ta0CMhJ6esxpzS9zD6trA_zPrFd4V-yg7Xc_IUGoQVpRD4kwTwiCXIDTorucfMCX8XYyrtwyw-uPLWtAEy1rBk6Mi8RuT0sAOCz5PcD1VUaqOEaePfuSjTd2XtLVIX55npNXN13fAxwEiI4ED5CqpoIXy-YfMth5zMRu_dQVaJVx5PdmOqS_yE4AQ9UOGzvqFzqBICm-5OV-FE7FRoRcVlZwajvC-z-jzwlLMbaVf7kHnV-nyylpL7dwdziQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رگبار شدید باران، دیشب در شهر رشت
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/694705" target="_blank">📅 00:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694704">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWyh0KrojDRSRhHXfTy5v3DUVlw1CnKzEmpJzr1934FLDGTlse1DJTslHtytydnta2s_Mq_HdBCJ_iJQnrDIP9CuHacj2OzLXzWz1u6TZ3JA1utBrC2lrwSHr5Vr3IchalEgud7imTcJwpucmoRFoqdbeb1733-3AxTRwPODmULIdXdn4ZY2auwHpOMe7MX4-OocgyEUaCln5de-VfgDKE9yBDvB-YWCOwA_8j0m2QBrKbWWdRTsp0T3Nt1so2-9_hpNeSy7iylRS6-Gtp1nvyVddyT0fElMGQXETK7pJUVWTvcTK3SPHLoRlA3CvtE1M7On4Nr8e8P6Ak1xhlTULw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گیاهت چی داره بهت میگه‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/694704" target="_blank">📅 00:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694702">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoyppOTcSlQLbZawvnJVOgMlsRyuz892VaWC6Rrf2U8fxTNCi9TKBFM1g8x_RDrYCsnFcy_I5xaiRckWhkkohnxfSTRxbvLAP1bGkKFeUWmZcB_jR6K9Zq94RxoJeLW44qynXqVWwvs8C6czXKXPkD2QxpfBcwGvtYetfGK5pabboHMjPg9MRItNNfpts7qjtw5afQPe9jJUUun8FtooTfChyp5HEv9WaRxYEe37_qK-cz0HzQTLbQKfGGR21OZUY-TldfVcgQHneTK55bF_NqoYiv8Vo7bULUDiXRAWAIr1bcfthrgyD5LaXZ6vzgc37mIb6Y9OkYGdagh2l6FQEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02d9be492d.mp4?token=Y6NGrbL_i3Rp8thRfwzlHmf7z2EQxfxKQ3S4aPk85tJY6bnr2znLTunl-gnzhiWC2-QsH2mxO9EPb4_azYq_LwWiVJEddSXIf4gNurnmhUrkUB3STfn5zXcA1-4-WppHdHV6kLrAL8gWnrkjH00vUf0Da8RJP2EJNZT2FclEqq58n2Gf9ck8mGrb9leahxdBE-GpCOUoi3UHdE7MIucOIeAr9G8DkkLq8FPJYNJg5RyYfAKgbv4iBcYCPZvQPqxugHoeq0EvGRQs969YUDfj4Jz0hATzeOrOjAewCl7flkTMCsrNhHeTNljXzp74Yjljk5dNftrKFIR2U80gbpxlXrChZF5EqLlyQ0N34bqwuW7ijnX-_eqeNRHmMgY0wuMwLJnpZJTM-nuXyQ-RxrOxFxQcYbkNWNgj5DW6ToE0_ou8sbdpNqfnwuvwC56PLT3gQyeNfxx5noJlNNsVGnvyVj2REuXFrA01b8aro3PzKCXOW99xWPDmgdgxhh7Zx_bEhmc3M1UypKHBWyGF_sNJ-yid4dPSc9buATKD1jC6mjj46snuUbKhSwMLdwJdL_OVG60miG3eFEsShJ4WobWNSyoUXqhO4nYon8U9T2P0IZNiyqVjHsaAJQUjdUFVcbp0zIJu447gXHyeZ2b8ZwF23s8p5Ym72Mt4mmKQCrfW6OU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02d9be492d.mp4?token=Y6NGrbL_i3Rp8thRfwzlHmf7z2EQxfxKQ3S4aPk85tJY6bnr2znLTunl-gnzhiWC2-QsH2mxO9EPb4_azYq_LwWiVJEddSXIf4gNurnmhUrkUB3STfn5zXcA1-4-WppHdHV6kLrAL8gWnrkjH00vUf0Da8RJP2EJNZT2FclEqq58n2Gf9ck8mGrb9leahxdBE-GpCOUoi3UHdE7MIucOIeAr9G8DkkLq8FPJYNJg5RyYfAKgbv4iBcYCPZvQPqxugHoeq0EvGRQs969YUDfj4Jz0hATzeOrOjAewCl7flkTMCsrNhHeTNljXzp74Yjljk5dNftrKFIR2U80gbpxlXrChZF5EqLlyQ0N34bqwuW7ijnX-_eqeNRHmMgY0wuMwLJnpZJTM-nuXyQ-RxrOxFxQcYbkNWNgj5DW6ToE0_ou8sbdpNqfnwuvwC56PLT3gQyeNfxx5noJlNNsVGnvyVj2REuXFrA01b8aro3PzKCXOW99xWPDmgdgxhh7Zx_bEhmc3M1UypKHBWyGF_sNJ-yid4dPSc9buATKD1jC6mjj46snuUbKhSwMLdwJdL_OVG60miG3eFEsShJ4WobWNSyoUXqhO4nYon8U9T2P0IZNiyqVjHsaAJQUjdUFVcbp0zIJu447gXHyeZ2b8ZwF23s8p5Ym72Mt4mmKQCrfW6OU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
دوربین ثبت وقایع مگنتی A9؛ مناسب خودرو و منزل
🔹
کیفیت تصویر 2 مگاپیکسل
🔹
دید در شب تا ۵ متر بدون نور قابل مشاهده
🔹
فیلمبرداری، عکسبرداری و ضبط صدا
🔹
اتصال به گوشی‌های اندروید، آیفون و iPad از طریق WiFi
🔹
نرم‌افزار موبایلی برای Android و iOS
🔹
زاویه دید ۱۵۰ درجه
💰
قیمت نقدی: ۱,۶۹۸,۰۰۰ تومان
💳
خرید قسطی در ۴ قسط، بدون چک، ضامن و سفته
هر قسط فقط ۴۸۰,۰۰۰ تومان
🚚
پرداخت درب منزل هم امکان‌پذیر است
؛ مبلغ هنگام تحویل کالا پرداخت می‌شود.
🔄
ضمانت تعویض ۳ روزه کالا
🛒
خرید از سایت با تضمین قیمت و کیفیت
https://memarket24.ir/product/fast/30028/180124/</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/694702" target="_blank">📅 00:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694701">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ادعای تکراری ترامپ: تهدید هسته‌ای ایران را در یک شب از بین بردم!  پست جدید ترامپ:
🔹
من بارها گفته بودم که برای از بین بردن «تهدید هسته‌ای ایران» ۴ تا ۶ هفته زمان لازم است، اما من این کار را در یک شب انجام دادم! باقی آن زمان فقط برای این است که مطمئن شویم…</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/694701" target="_blank">📅 00:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694700">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pw6SmbcS-s_E_1b190FHvNedprFUc27QOSnOvDPh6xuzaI90vg6DZ08sdZ29TWSDPNlEgMt3n8BFbRp1T4BwhLjA3dFlb54JdPLJR8PV-HnrwobOMhX4WVFtjqBT5BaW1lImOl9JqU0pa-L7qPWmISGBxnZk26FsrDIvtQSUdnYvnXmeg_yLDdqUn2P9k4n4hOkxaDBzLSxTkcqtvq_9VsxppqZ7oa-6IgOFC4NlAWt5Ni-7_ze3yIfJgg-cA26-09XuUyRKbT9lsQFSDTeyAr9Wgp_oKGa3fL4cXVQeqBXh3BRXHBVW-APifAp7CPF-EBSCt2AOxt0ApizSNJypbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/694700" target="_blank">📅 00:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694699">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1003893947.mp4?token=VyJsFRJGGOBYnJ62Wf_YjlqIH3pVd3ut7Lsz6od4W_VJ1dDdaosH7ahqqPGdvnNIXcnjODbxC7kRArn4ZEYC8FBX6O93QQbHmIS3V_OeDzdp1kYeIfXSYkxoBWekjosC-iQs_K31Yg4qQCY71mGbA30BPiHfitt1GLnULQV8MGuOdtJK-NecwzULnUHcaWC5mA_qdg2uk-Ksmni90LB_E-UNgLr92aZBbKoStxNYU4Yw6AKqYt0g1Uet3HD3AndDNqoMU8WWeg8FLd3u-6VXWBQ7Ne_yIOqzldauc_1yyYVTvG5FsStAd9IDWUNU1kK60aaPlUxkV0kYJRbruHK8Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1003893947.mp4?token=VyJsFRJGGOBYnJ62Wf_YjlqIH3pVd3ut7Lsz6od4W_VJ1dDdaosH7ahqqPGdvnNIXcnjODbxC7kRArn4ZEYC8FBX6O93QQbHmIS3V_OeDzdp1kYeIfXSYkxoBWekjosC-iQs_K31Yg4qQCY71mGbA30BPiHfitt1GLnULQV8MGuOdtJK-NecwzULnUHcaWC5mA_qdg2uk-Ksmni90LB_E-UNgLr92aZBbKoStxNYU4Yw6AKqYt0g1Uet3HD3AndDNqoMU8WWeg8FLd3u-6VXWBQ7Ne_yIOqzldauc_1yyYVTvG5FsStAd9IDWUNU1kK60aaPlUxkV0kYJRbruHK8Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقاد جواد لاریجانی به مصاحبه‌های اخیر پزشکیان در آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/694699" target="_blank">📅 23:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694698">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc3d734775.mp4?token=YaMPhFe3IfPDFYdEBYQ4ld1N1KnK1VrmW-WWD2z1iWjTyNLyHfnbZkcGDTniqvk6hP0vPldJIXcu-cr8t5rjxU5dsL2ukJdsSEglY-iYxU0er_97KAlNyUvD5QfFyN2AUEybytbX98vj6os-UVnvWp2oE0RYoOt9tr_XVJdt4VpWfgCyIS8AbS4wisIMzxy75sxEyn_sUISjMab7k7m3gsWmb1SK-oUgk_L1fPMaZ2Abf5O9HFo-evtQLVG8KVGvfV5Ex6I4-SO6f5ockbIYUPF2y43q-3CroOGnI5zjoB_aZ4f2OkPK2C1gJtuEbHj1W70HVS2R6nO0WjJJ9xZl8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc3d734775.mp4?token=YaMPhFe3IfPDFYdEBYQ4ld1N1KnK1VrmW-WWD2z1iWjTyNLyHfnbZkcGDTniqvk6hP0vPldJIXcu-cr8t5rjxU5dsL2ukJdsSEglY-iYxU0er_97KAlNyUvD5QfFyN2AUEybytbX98vj6os-UVnvWp2oE0RYoOt9tr_XVJdt4VpWfgCyIS8AbS4wisIMzxy75sxEyn_sUISjMab7k7m3gsWmb1SK-oUgk_L1fPMaZ2Abf5O9HFo-evtQLVG8KVGvfV5Ex6I4-SO6f5ockbIYUPF2y43q-3CroOGnI5zjoB_aZ4f2OkPK2C1gJtuEbHj1W70HVS2R6nO0WjJJ9xZl8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیژن مرتضوی؛ مرد ویولن سفید میان شهرت، مهاجرت و حاشیه | او کی رفت و چه کرد و چرا بازگشت؟
🔹
کمتر خواننده‌ای در موسیقی پاپ ایرانی را می‌توان پیدا کرد که هویت هنری‌اش تا این اندازه با یک ساز گره خورده باشد. برای چند نسل از ایرانیان، نام بیژن مرتضوی پیش از آنکه…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/694698" target="_blank">📅 23:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694696">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
پرس‌تی‌وی به نقل از منابع آگاه: نتانیاهو در حال طراحی سناریوهای مضحک و جعلیِ «پرچم دروغین» مانند هواپیماربایی برای متهم کردن ایران است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/694696" target="_blank">📅 23:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694690">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZrFOudZUs8DW9rkOum4Bj6j3Ly54Ot_dkSUNDw3LYicbWIQgs2A9pNwfDeEpKvNiIA32BJRek1jnboIE2MLnWaVkiXT5LbECujIE3iC2lrSlxXFbfR8u8ZiMulo17WamS6xaNMrz7Bop-GrhXiC-Wb3XQJf-cQ_dM1qZMXaGdN4LustP8vQwrF01RT6EccPiY5KEmzMkePtuQMvF7BxlgcSLf9ZcqpaqAzZCfUsM-po6xy2BqFQruKvbhkIWxCQAIOKrDgBRXT9Oz92cGSNuA4-9kfpS3SSfpDJTopZ5eYLehAdS1oUIDz-o1QqdKNAj3VzIQCsrN0dulQDrtao0lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cv-d_t0TKqlR_P2WJvfhqc0NwgiKIkQWmYZMwL4i5M7USpbK9WdOcK8rDIOd7SRfoDKat2lV_U-HjVvPWx203tiV-iXPeKYeibJzCYJbwwZPziL816gps2GUb0Qc3Srtv2ukqueRvDAqG7OlIGkeTgBVoP9E6N0kI10LM1SpsNEDBT3cpiMGGF1AaZBSTZiFzSQ23RIlId8vGFGh5cvKBSPH2O6kh3ocoRetAX1e9230drjDxoTw4yxYIL_GB2fSEoZ5_cJIIvDgdpgTc4WN7gzCwSoM0dxVeIq1dYnxQJ27tFdi1U3-0UAkVlobhTFoY2XrEGRXVminW2YRalNmKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TisKbd10BW_XxZMezPqfZvJMaqwNK2D-vOe1J-YcpGB_0_l2WQijZFBaA36D0d5Qr8NiyeRWI-P4OtkE7hffzEEp0MiVdMAdBUYfsss21RbdAVTGl9_HN1QCdE-QJ_w6-UIKT1bjgjGJ6nRX1yopOnZ8Ij2YLP4pFdNsHPn2GgAfz9vP-wYd1kX2fcOV4q3zke8vpHIzeda8guEzCGKrMED3IuRRh4UEf6aFmBTWDHPwI_1pQmR8cyfLFu3QcPG4WSIygEFxIKoj-ibr8oBJ1QYPwnnZDCrT0HnRcjFekDDpFzcv7gQipnAssD50nIIqcGi47zEbdaIXVSIBSTcGiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ltis-1A3DnZ-eBs-HkabYItL4s2AR2wQ_QHWotxmTbsaaxNaoUQxi1j1icLe7R87VLDybhKl4k0bVxAfJw3oHRW0YrbIZO4Ddl66QTssj844S1_YhbfZZrDsQQ8-2HLgK0-8JcOoJm9vLwvEH5PzLQsDAd9nHZu9VvdLRw6HDd2XZ7I9T1WKlS4L2_XQK0PH40BNNwgVALKFeTtk1A46-S3KMUjLfYbYygiSrJRURyPidgB3WM9u8256JPu0CGqCbeIa6z2TKtaxW7rJlMI7kpIUO1zgVwJegmAEZ-LG0YWGiPbWW66--fHEpzAe8UqbMmYGPO8zUNBlPe7nWgwfOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cAQUsPn9RxKoGJz0QwLzhb2-DYMaicgd5E_OqZpE0lE8zULKDrDiX4NUk_nnlRkTmsMdh6tuBczzRP4Wco10j-oclRY-uBrLEKsSvsoNaWETzRaK0knTk_2ABaX2oK0CQQOTbhY4Nf7aKeND0rf0gZCDwnrt_CqbUmJ8snQLC17dwHxvwEJPE_dgX1Yl71xyT9vvWr9FIUv2t1zCYnjJqjX5Ey5iyB_dcssM8Hk-kzvXgqkdUsul3uSy75qTF7J6eiHEHrCLiNXGtwocR24HYX-1whxBdW58hUM7C4FnjOO_XVcIdxp6uvRE-pzx0y8DOys0SazeaxZp6FnvcE4hdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pr7D1ai2tAqv8IOLkr3kfrDERBTSPNvzecEMtADYm7J0k78GTQwaNQm_o9IKfTQ3JK46qnso2DCbDEDMkPu84TmFXz0ksGm1LihrK5qKitAJw-2_x6i7QbpesTr82JhfrpSSyzsfAG5jxWZjRz5ix4wkxd9Pmpe_mC2TnT9c2Dr_Kp4jYo5p1A6P39SP3YyPwqU_ox1tn5gQGBYfDSlXvdFoGbfpgMix0QcdGxz5d7qGxEHNlVKpnQVsSFDh02V73Iaya2LI5hScCcOb-eSRzXG59IrciFv1mbibe1mAvQVt12951yRNytpt7u4iJu4_WfHcBCQ4pbPW93Xby3aIgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
در ۱ دقیقه چند تا نکته کاربردی برای یادگیری اسم داروها یاد بگیر!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/694690" target="_blank">📅 23:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694689">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
رئیس پلیس راهور فراجا: جرایم رانندگی مشمول دیرکرد به مدت یک هفته به مبلغ اولیه بازگشت/
ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/694689" target="_blank">📅 23:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694688">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
رئیس جمهور: اگر در مصرف انرژی مدیریت کنیم هرگز کم نخواهیم آورد/ ما سه برابر انگلستان گاز مصرف می‌کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/694688" target="_blank">📅 23:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694687">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
پرس‌تی‌وی به نقل از منابع آگاه: نتانیاهو در حال طراحی سناریوهای مضحک و جعلیِ «پرچم دروغین» مانند هواپیماربایی برای متهم کردن ایران است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/694687" target="_blank">📅 23:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694686">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyPVPAIig0GShSXrDkaJUebtUeKJzi1S_RfFI24q9qv-RyVkr-P_dUmo5y_X2fMvCxM6DuMyiRr5cKe5fFR-tBUAdABHFWMIc_kEygge-MHd2bHwDnLOGNwByTKM4XK_xX4-8cRMp4Ul1pwuaucd6TfnwxokuqBPggQX-c96lOnzAlg-yckYUOXB3EF2Fta4pizwhkKHD44xfPsTBloASCPEuuC4Hwfb_c4ZOnCq3OnQPC59uA172vhj909SHLiTpNAryisIEdFi7eisuGuDR1M8ebHu1x5Iz8VDw6vWYPxcQ6bLDOhw-eltzmCT9ZdhiErTFlyqxHDH7Gt8HQ0IbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو در مورد حادثه هواپیمایی فلای‌دبی: این مثل فیلم‌های هالیوودی است، اما در سطح بسیار بالاتری. نمی‌توانید چنین اتفاقی را تصور کنید. نمی‌توانید باور کنید که چنین چیزی واقعاً در زندگی واقعی رخ می‌دهد، اما این اتفاق افتاد #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/694686" target="_blank">📅 23:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694685">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f78ced2b93.mp4?token=J7Ge2zJ0SppkRg4VicPqlkl_q5xAVIuOnLz2HvM4agqKOpmSejwRIQ9mhRc4K3byAhGzxNNidd8pczu0lZ5B-Z8CjR3AaohOSOPZ67dnKGoxkJcOPVJyJuL9ChhXi64pI3qDmme0Rtmq72khHHJFkkPYZkfDeEEnLFY_yCUsSUacVkBFQm2EiEdN4DK8kAyTqePX8UlucraBEtBBxn04CcsdFG8OwwDrM0hiiCixcv7LwVbOnLfXWO--te3J4AZwnvfpiPcCnHqW40GcBRQ_a55vwjp4IzjW2oUAt_TbhZgeGAxHhYtrO2i_74URr0HIhgF6i6Tu3vR8W71QVV42Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f78ced2b93.mp4?token=J7Ge2zJ0SppkRg4VicPqlkl_q5xAVIuOnLz2HvM4agqKOpmSejwRIQ9mhRc4K3byAhGzxNNidd8pczu0lZ5B-Z8CjR3AaohOSOPZ67dnKGoxkJcOPVJyJuL9ChhXi64pI3qDmme0Rtmq72khHHJFkkPYZkfDeEEnLFY_yCUsSUacVkBFQm2EiEdN4DK8kAyTqePX8UlucraBEtBBxn04CcsdFG8OwwDrM0hiiCixcv7LwVbOnLfXWO--te3J4AZwnvfpiPcCnHqW40GcBRQ_a55vwjp4IzjW2oUAt_TbhZgeGAxHhYtrO2i_74URr0HIhgF6i6Tu3vR8W71QVV42Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس جمهور: اگر در مصرف انرژی مدیریت کنیم هرگز کم نخواهیم آورد/ ما سه برابر انگلستان گاز مصرف می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/694685" target="_blank">📅 23:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694684">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صد میدان 3- میدان سوم، انابت</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/694684" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
شرح صد میدان خواجه عبدالله انصاری
🔹
میدان سوم - انابت
🔹
انابت به معنای رویگردانی و بازگشت از همه‌چیز و همه‌کس و روی‌آوری به همه‌چیز و همه‌کس آفرین می‌باشد
🔹
در مقام و مرتبه‌ انابت، فرد هیچ‌چیز را از آن خود ندانسته و تنها در برابر الطافِ الهی سر تعظیم فرود خواهد آورد، شکرگزار خواهد بود و با تمام وجود به آفریننده‌ خود عشق میورزد
🔹
قانون توجه، قانونی بسیار تاثیرگذار و مهم در زندگی بشر است
انابت سه قسم می‌باشد:
🔹
انابت انبیأ: بیم و بشارت_آزادی و بندگی_استکانت با شرف پیغمبری و بار بلا کشیدن با دل‌ها شادی
🔹
انابت توحید: اقرار و اخلاص و بینایی وی را پذیرفتن_فرمان وی را گردن نهادن_نهی وی را حرمت داشتن
🔹
انابت عارفان: از معصيت دور بودن_از طاعت خجل بودن_در خلوت با حق انس داشتن
#صد_میدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/694684" target="_blank">📅 23:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694683">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcseyrVp2ITT-tO6QVHhbLMTUrUkQp1oL8Qv9y3pQxFoLVv10AqmIMiPEQl_2pql-o1x5UeELN078P0bYIswQXy1ySoH3oWJK8c0ect9mn9raxw_GnxjCu2QbHEBYsW_A-cSsXjDOTcr6kCPlSL-Oz7a0qHFf-7Sv8r6LaixNmLkv8WYrD7ZM2_bbjlKAmE30wEyNCdLr88TKK0AXrcvzCo-j7C_RugLTh8MWGJ41Q20qCt1ZXkX91v4C8AXkTZvyPiA7bAjt-UOh5KWinK44VCBpSfn8MBw1-A9f0XWxtx_FMYqmoRCZcGoqj_cP0gGCIF8GaopC_kouaFdLFlwZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۹ عامل سرطان زا در خانه شما!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/694683" target="_blank">📅 23:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694682">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSMw1xF9sNqDkfcTI5Iq_3eF5XCSgSiMDaW41erUOt7Q8GrvC-7DnNRbDPEaZtw5onj1k1zVlpl4YQ6w75MSYtLxOV0nIonwI2rM6JrkuLf8aYtplX7_CSrAxb-1gGE81XuMKvFqxtVR73ZdkvDZIGYFXAzMuOXDA8Pyvpkio-LupC-zG7352b6P4lyVmTfuoNj6DCY6Ew5qJnr8qHPVrR83qXy5xEbSC4ZMOqXNMe_q-bmdP0_ETx9h8oWax2V5dem2g2wW74riNIzDH91_lkTi3yIv_Pulvo809Gl0f69CJAZ0zzzhbhmrmLIqcG79hhZATfvS2qEQVMxU21q4pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پولتان را پس نمی‌دهند؛ اما نمی‌دانید از کجا باید پیگیری کنید؟
موضوع را ساده برای آداد توضیح دهید تا مسیرهای حقوقی پیش‌رو را بهتر بشناسید و برای اقدام بعدی آماده شوید.
⚖️
آداد، هوش مصنوعی تخصصی حقوق ایران است؛ به شما کمک می‌کند پاسخ حقوقی بگیرید، مسیرهای پیگیری را بشناسید و اظهارنامه متناسب با موضوعتان را تنظیم و آنلاین ارسال کنید.
از سؤال حقوقی تا اقدام بعدی، همه‌چیز را یک‌جا در آداد پیش ببرید.
👇
رایگان شروع کنید:
https://go.adadai.ir/qhm3TX0</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/694682" target="_blank">📅 23:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694681">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40099ddb82.mp4?token=i5ytxKR79M1jAyKAxdaSciFalog-jpmA0eT3UfogNYV5CpM6RR99bT-SHFLewPuQZL9exZOd0UtFNHoA2ulaPvpq47Eh-55lC5Tvl9IoQ0yPMptkCctdiKy8e6w7-sNqmPOCJvacVzhjuF2cJeZgI04IiF8-Rb5VDmiVf5GMBIxzgzN8qYleABi4dy83W7JUKVhdhqrlnd28vewjarZOfRGpthona1mG2l7_7o-aHU8cZCZvWGBarIj6Zjwzt65oJE1fBqvRUMVEN_3hnbnm0HOAKzTdGJlPMwoLNeYKqAJwhNeIZYOKaUj4zHPwF3ZaVFXqyjv16Pxh8FlX_7I8iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40099ddb82.mp4?token=i5ytxKR79M1jAyKAxdaSciFalog-jpmA0eT3UfogNYV5CpM6RR99bT-SHFLewPuQZL9exZOd0UtFNHoA2ulaPvpq47Eh-55lC5Tvl9IoQ0yPMptkCctdiKy8e6w7-sNqmPOCJvacVzhjuF2cJeZgI04IiF8-Rb5VDmiVf5GMBIxzgzN8qYleABi4dy83W7JUKVhdhqrlnd28vewjarZOfRGpthona1mG2l7_7o-aHU8cZCZvWGBarIj6Zjwzt65oJE1fBqvRUMVEN_3hnbnm0HOAKzTdGJlPMwoLNeYKqAJwhNeIZYOKaUj4zHPwF3ZaVFXqyjv16Pxh8FlX_7I8iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این روزها اخبار طلا دوباره صدر رسانه‌هاست
🔹
از ماجرای خبرساز شمش‌های بابک زنجانی تا دلهره همیشگی مردم توی بازار سنتی و پلتفرم های آنلاین طلا.
🔹
اصل ماجرا چیه؟ تو این ویدئو ببینید.
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/694681" target="_blank">📅 23:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694680">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10f37f482f.mp4?token=hj5nv3gMtTjzfBevUUUQ_6xqD9z3EhOCbetKB7XDXXxt8S3-bZYxq4ObG9jUIgGOVad8lrADfbh3axyznzxML4gaPrJBTyEWJ3O8zn9TW7xlJkhIOR7mcwo7VxZS4aSQA2A9AEZD4VEa1MWnTOvVaf6x9CeV4WELdKFw4_Km4DOfcaPPse6BFYdYcdOkyvQrqOyIpBB4IIvB7PJ4qU-nS3KGDMGsrrocebz5WuhY3BzORhbmY-Q9l_iVYdKjk3xG_PykqEgHxRAiH1plR0zFaM7Zs6vj_VJT61voYh51rTQ2g2Q-R5LgonTsAMT0cElQ5M3re4Mjpo1zJvbSjAEh3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10f37f482f.mp4?token=hj5nv3gMtTjzfBevUUUQ_6xqD9z3EhOCbetKB7XDXXxt8S3-bZYxq4ObG9jUIgGOVad8lrADfbh3axyznzxML4gaPrJBTyEWJ3O8zn9TW7xlJkhIOR7mcwo7VxZS4aSQA2A9AEZD4VEa1MWnTOvVaf6x9CeV4WELdKFw4_Km4DOfcaPPse6BFYdYcdOkyvQrqOyIpBB4IIvB7PJ4qU-nS3KGDMGsrrocebz5WuhY3BzORhbmY-Q9l_iVYdKjk3xG_PykqEgHxRAiH1plR0zFaM7Zs6vj_VJT61voYh51rTQ2g2Q-R5LgonTsAMT0cElQ5M3re4Mjpo1zJvbSjAEh3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین یکتا در شهر صور در جنوب لبنان: نگاه ما همان نگاه آقای شهید است؛ آمریکا از منطقه اخراج می‌شود و جوانان به‌زودی در بیت‌المقدس نماز می‌خوانند
🔹
آنچه امروز در جنوب لبنان می‌بینیم، روحیه پیروزی و مقاومت در میان مردم است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/694680" target="_blank">📅 23:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694679">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ff6deb449.mp4?token=pBhzeDWDvhQkVwvLbMqRlhnfESJ63Dw5G-JEbJvpMwUJiNUrlldu1jjnQCuNCxznRnc5qkfOVzV8WMkvSzK1g0KD0cW8as7DcYogPllMUcJos0DpetLWsH5liwIcG24PxhehF4jPz_ddJjt4krzEBxXhLwyYrT4kM8Mh1kGEivcVwTMrtr5yDVoqmMjUN-lFzdIEuAwUN25_0deZVTiqDrIiCbvzHjMecCzzpvbazj2YvGBs0-ev722Bl6zK9P8zvNnLCtp5hIoly5leF6rIoFWmNIJtu8y7mLRtjwII1wpFKPwW609XdYg1m9aztMSmdCNzQ0ijPhF9hAqcMatT4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ff6deb449.mp4?token=pBhzeDWDvhQkVwvLbMqRlhnfESJ63Dw5G-JEbJvpMwUJiNUrlldu1jjnQCuNCxznRnc5qkfOVzV8WMkvSzK1g0KD0cW8as7DcYogPllMUcJos0DpetLWsH5liwIcG24PxhehF4jPz_ddJjt4krzEBxXhLwyYrT4kM8Mh1kGEivcVwTMrtr5yDVoqmMjUN-lFzdIEuAwUN25_0deZVTiqDrIiCbvzHjMecCzzpvbazj2YvGBs0-ev722Bl6zK9P8zvNnLCtp5hIoly5leF6rIoFWmNIJtu8y7mLRtjwII1wpFKPwW609XdYg1m9aztMSmdCNzQ0ijPhF9hAqcMatT4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پوتین: روسیه امیدوار است تنگه هرمز باز بماند و تحریم‌ها علیه ایران لغو شود  پوتین، رئیس‌جمهور روسیه:
🔹
حل‌وفصل بلندمدت مسئله فلسطین تنها با تشکیل یک کشور کامل و مستقل فلسطینی امکان‌پذیر است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/694679" target="_blank">📅 22:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694678">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/504076287c.mp4?token=mxqnqXw6_L7CNjwKNL7olp3ID8_YV3Q-0pZG_ABtKwmCu51FK6OzQyVUEH8UaDrseOAd3mzpi6jEfJyoW4JorKH-8d6suj7vgKIw16wGu6TavtWxSZ9Y9y5pSq2CjcjWrJuwxSabGiv2wfxAQfeuIcdp_Ru1GkgEUmbcb8D5olSJt5FkM-TML904coS75PBywxYf9-06dul-PElSpmvrrNZEZpou0PJqTj1CJQfVT3Xx3wtOUIhW-btW-mY8lon5tYeHnI_k8huJI7LPPWWzVOG_j9Dk_m_eycc6y8sL-ab2L1jggkGNIMXZPXwOQrGva3bpiskQ2GkWngTSvIN-1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/504076287c.mp4?token=mxqnqXw6_L7CNjwKNL7olp3ID8_YV3Q-0pZG_ABtKwmCu51FK6OzQyVUEH8UaDrseOAd3mzpi6jEfJyoW4JorKH-8d6suj7vgKIw16wGu6TavtWxSZ9Y9y5pSq2CjcjWrJuwxSabGiv2wfxAQfeuIcdp_Ru1GkgEUmbcb8D5olSJt5FkM-TML904coS75PBywxYf9-06dul-PElSpmvrrNZEZpou0PJqTj1CJQfVT3Xx3wtOUIhW-btW-mY8lon5tYeHnI_k8huJI7LPPWWzVOG_j9Dk_m_eycc6y8sL-ab2L1jggkGNIMXZPXwOQrGva3bpiskQ2GkWngTSvIN-1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه فکر می‌کنی تمرکزت بالاست، این تست رو انجام بده!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/694678" target="_blank">📅 22:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694677">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
بلومبرگ: ایران پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای را بدهد
🔹
عراقچی این ایده را در دیدارهای محرمانه در نیویورک مطرح کرد. به گفته دیپلمات‌ها، این امتیاز می‌تواند بن‌بست مذاکرات با آمریکا را بشکند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/694677" target="_blank">📅 22:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694676">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
منابع محلی گزارش کردند یک سوپر نفتکش با ظرفیت ۲.۵ میلیون بشکه که در مسیر غیر مجاز تنگه هرمز تردد می‌کرده در ۸ کیلومتری سواحل عمان مورد اصابت قرار گرفته و در حال سوختن است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/694676" target="_blank">📅 22:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694675">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
سفیر اسبق ایران در عراق: آمریکا پس از اشغال عراق دنبال حاکمیت دلخواه، حضور نظامی دائمی، آمریکایی‌کردن ارتش و کنترل روابط خارجی برای رسیدن به ایران بود
🔹
ایران مانع توافق امنیتی آمریکا و عراق شد، مواد مخدر پس از خروج آمریکا از ۲۰۰ تن به ۱۰ هزار تن رسید.
🔹
هنوز پول نفت عراق دست آمریکا است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/694675" target="_blank">📅 22:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694674">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bd8265650.mp4?token=seFmsC7Dh82kI_YTtOX8DOnD8qHsWFlsHSeAPoQc6X70CgSgXLMvCbZ2HTTKWafexPC0XBWZr7_dh7lYu9yAYY0WMy8BtnwM4L_kxfUnV7wTn7tqZdd9Nv8BBNAAnyiXo7abXSN4CLIWLOFIv-2gV4ykm4go2pfhpZrIOpplhl1NLmYcBT2PReqqP8o4IbOUug-yQ9aSo68_qnov6bBcVC21UgA_vT7IxN8Ij6uZCwYx0atVVcxBdHel3XXYST14pVWw8hhKNr_R8TW_FvOV82TYQunif1aBTyOYKyTuCu5zKOcBJ01jPEnzo_Mb6AlyVSJuhfu6GnMPPx4r6Gbkcra2dmYwygQbpR7xhq3BJTI8rhMgHt469coMNFauF2i6nM34nVWLVnBwktR7iBNd_cqJEH1blZEECWy0_2UK70N87smUl4FC5ItFDCsJmfN30a0ikzIKhyFOVjrDr5viTpDEI5Qo7Tvly9UjBDVoZa1IruOYkXuBWRLOdXezbkkc02HkKIXZQ1zzVFWE0ApgNP7TN-a40uPajw-RnqPCjVDMAslDVWwjAogHW6gPUpD2-dQXKBiBpvmUCWy8XhWFaIs3Nm3nGUIODOq__TXpy0Ih7QDNTWjNMp-N0N5enkEhJ2w4ywU_J6hKNG5tV9YJ4HlkDfc4MjwXSVhc7HRbWXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bd8265650.mp4?token=seFmsC7Dh82kI_YTtOX8DOnD8qHsWFlsHSeAPoQc6X70CgSgXLMvCbZ2HTTKWafexPC0XBWZr7_dh7lYu9yAYY0WMy8BtnwM4L_kxfUnV7wTn7tqZdd9Nv8BBNAAnyiXo7abXSN4CLIWLOFIv-2gV4ykm4go2pfhpZrIOpplhl1NLmYcBT2PReqqP8o4IbOUug-yQ9aSo68_qnov6bBcVC21UgA_vT7IxN8Ij6uZCwYx0atVVcxBdHel3XXYST14pVWw8hhKNr_R8TW_FvOV82TYQunif1aBTyOYKyTuCu5zKOcBJ01jPEnzo_Mb6AlyVSJuhfu6GnMPPx4r6Gbkcra2dmYwygQbpR7xhq3BJTI8rhMgHt469coMNFauF2i6nM34nVWLVnBwktR7iBNd_cqJEH1blZEECWy0_2UK70N87smUl4FC5ItFDCsJmfN30a0ikzIKhyFOVjrDr5viTpDEI5Qo7Tvly9UjBDVoZa1IruOYkXuBWRLOdXezbkkc02HkKIXZQ1zzVFWE0ApgNP7TN-a40uPajw-RnqPCjVDMAslDVWwjAogHW6gPUpD2-dQXKBiBpvmUCWy8XhWFaIs3Nm3nGUIODOq__TXpy0Ih7QDNTWjNMp-N0N5enkEhJ2w4ywU_J6hKNG5tV9YJ4HlkDfc4MjwXSVhc7HRbWXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام پناهیان در ارتفاعات علی‌الطاهر: خانواده‌های شهدا می‌گویند خود را مدیون انقلاب اسلامی و امام خمینی می‌دانند/ با وجود خانه‌های ویران‌شده، روحیه مردم و رزمندگان این منطقه همچنان بالاست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/694674" target="_blank">📅 22:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694673">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pX3hhMji1k7qRjYvzaO36dOIFiT8Nmof0uyAmStQ93mfc9_WGdu629ycs-WVP-kECjMR1u6pykZV4qRw8YIy_WlZElSDS6U2c97pxMbFIl3S3J3_Fz9esuww0gMdUHAioq1CTj2NMQ-6brPcYifNR7gx5ri3VbB94YzsoAnTlaYt9XYqCL48F64lV_m65zq_HUL3F03PnB2fJbvZklBfSM_Tzt4NPmsuYyZpFmysnkNnEoObgH6qfBuzJoqBbYcQ8vM4np-vDBbUBdcZKXcYuUIOHr-8bp1B8hzAbpNFvddkdP8gw8icmhplze53aEKMljvcB3ddNQkWNddig9Cchg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هدف قرار گرفتن سه نفتکش در تنگه هرمز در روز گذشته  سازمان عملیات تجارت دریایی انگلیس:
🔹
شمار نفتکش‌های هدف حمله در تنگه هرمز در روز ۲۹ سپتامبر به سه فروند رسیده است و هر سه نفتکش با پرتابه‌های ناشناس هدف قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/694673" target="_blank">📅 22:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694672">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
بلومبرگ: ایران پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای را بدهد
🔹
عراقچی این ایده را در دیدارهای محرمانه در نیویورک مطرح کرد. به گفته دیپلمات‌ها، این امتیاز می‌تواند بن‌بست مذاکرات با آمریکا را بشکند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/694672" target="_blank">📅 22:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694671">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
هم اکنون| عربستان اعلام کرد که خمیس مشیط و جازان هدف موشک‌های یمنی قرار گرفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/694671" target="_blank">📅 22:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694670">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360c5b33e7.mp4?token=fBJoCUkwnUTaqgKJ3N0bcOyINEogcjBFh9EEVf6GVadc_8Dy1c62oK-BK9sRrB57-JR1ZPh7i0y9QJixALQNq_L87-nkjDUDI4bOI2XvOMGXEA9PC6ZDX1kAA7ZBSjvT4Mi5ueqenQoNXHg2uWxPmMChBEN3Iz7AUBXNsZxVE_dp_dcVyOHEV8Dwo77fU6ugVfbNjpP6EOPpAZg0Tu82yztkAEI9gHXog_9ZbY6jyJ6sc4i4iyxdVdTK8xpKIyg9AHqwD9pX8O1NN7hoRVhTuTJQKzOnlj2mEbQQGCFSyxLlJS4R3LEnHRW60zMIJFBMAZ1RzBC6WkFHfG-HIOtf-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360c5b33e7.mp4?token=fBJoCUkwnUTaqgKJ3N0bcOyINEogcjBFh9EEVf6GVadc_8Dy1c62oK-BK9sRrB57-JR1ZPh7i0y9QJixALQNq_L87-nkjDUDI4bOI2XvOMGXEA9PC6ZDX1kAA7ZBSjvT4Mi5ueqenQoNXHg2uWxPmMChBEN3Iz7AUBXNsZxVE_dp_dcVyOHEV8Dwo77fU6ugVfbNjpP6EOPpAZg0Tu82yztkAEI9gHXog_9ZbY6jyJ6sc4i4iyxdVdTK8xpKIyg9AHqwD9pX8O1NN7hoRVhTuTJQKzOnlj2mEbQQGCFSyxLlJS4R3LEnHRW60zMIJFBMAZ1RzBC6WkFHfG-HIOtf-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنج ماده غذایی که کمک بسیاری به مغز خواهند کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/694670" target="_blank">📅 22:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694669">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
آمریکا تحریم‌های جدیدی علیه ایران وضع کرد
🔹
آمریکا نام ۲ فرد و ۲۸ شرکت را به فهرست تحریم‌ها علیه ایران اضافه کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/694669" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694668">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
بلومبرگ: ایران پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای را بدهد
🔹
عراقچی این ایده را در دیدارهای محرمانه در نیویورک مطرح کرد. به گفته دیپلمات‌ها، این امتیاز می‌تواند بن‌بست مذاکرات با آمریکا را بشکند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/694668" target="_blank">📅 22:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694667">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-hAMpsUkbiKqysMGTa2PWE12LlOBpW71-oev6KOXckfFaBfsJ7e_lTbrq-dn_giiEXBrYu7yrlBHFpwjx5tqRbCY84uuoz-i8Gi9tDacDuTeq__0QEIsisrB1pFP_GCePlg4F8mqCjkzwd4othspB6Px0lsOmpdG07sllLUsy2B-w0u40XSNyP3ggKgc_pPIiRxZ88UtEZMX1Uh6XUrGfJI1YVUc0aYu24e80jl3oyKujiWmo8N0XB2OpxQj0Il-jmiQKbWomwttr71M2PcauGpC2LT8JU7hqON-z0f-fYJO2Ywdxu6MGGVOPNFsHEN3ToGSes1hiX9ia-8-b6SlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جکسون هینکل: سفر مخفیانه نتانیاهو به امارات مقدمه‌ای برای جنگ روز قیامت علیه ایران بود..
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/694667" target="_blank">📅 22:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694666">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zo72IsLZ4lwQbtLGi-voysbC4eTjemCT5jE_Spr8QGcoT4bq0mm4Z0vprXqvs0FPu66aqH88maSCXbSbvUlHq4F4TH7kqlpMQpRrZZZd1uxp6EV7a2vmaWoh2YyeqZhtYx_p7PoVvHzlTIMueaCcUa3K9bszveJuMEhxOmp6-4LlVSlUMsoOOyWqM9I1NOdKCog95BQK7RCjINDlm0v0WLAt2qpOv1EEtywlHWYjDNxvo5r2_8y-wyuf5kUmKMrLOot7wl6FKEhjtPPQN-ZFbwhNuZtcPhT-W3FN84ItWXrTjVT4sxUtEqdkgppYo2q1voSl0IacYjhNzITGmLXIVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسی یک باشگاه دیگر هم خرید؛
باشگاه الدنسه اسپانیا اعلام کرد که لیونل مسی، مالک جدید این باشگاه شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/694666" target="_blank">📅 22:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694665">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtm0AgHYdkJti6FgN_PAGhM_TJUHytCdeeVaFxqa2Jr1He8WY7s0tlaQcKAro3hDkSoxVw2JkVOS9waDIFpq13xxrrj9_jmzDekXJrmy5iYsnsffYxxiySzAWqDBbhdQvjg3d4rqlstZgl9f6DK3eIXvbMAwDdwgiBmfBICFx_ALRx3JLzhnqd1yH5x4yi_qrw4WJc5dGyvmM5L08hCty6oyyJIFntNfgY7TLbb_b6-5Y0HpLVtvyEHLf-SYKcYXWR8TETWH_qLh9rOpGpfjnD8yZgxQUF0vrPcjOJ1ZXGevra0wdO1VgRtu_ITKjdic7zqW_yQO1rwVtDyQ2Huu8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌ان: جرد کوشنر در حالی مذاکره‌کننده کلیدی صلح خاورمیانه بود، شرکت سرمایه‌گذاری او بزرگ‌ترین سهم را در یکی از بزرگ‌ترین تولیدکنندگان تسلیحات اسرائیل داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/694665" target="_blank">📅 22:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694663">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TXaTCe10FGi5BGz1BkawHSsB0hWDWZqQkP4kmEm4WrvngTr5pOJypRuielZc1wlwCIn8y9j2E3kUSQMZIrmbPMBZ3LxXBRRnAT3xg23Zq_7HqQhUjjaeAx5zgSWooxz-6_lcPGKw8Udd0_DnTcWgZ2Kf03FPOezpCDvG0a4j268o3xDGs1R6En9k0OxdI80vS6oip8fHzlYmQO_8TgiCX_zkFbewny1JUTTm3eMorPRfdQN3KRWZWHzqqdbWJzYnECCZhape-qgJzQlwe_U-IaoxkyYk0p-N4KQvOT1Cf5tlaarPCID0_XbiW1tLqmpwLg8scfd7e1VqePWikDzk_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WDJD4GpFjHtMPkX798GD0N7FHAjWL-foEMa1Gamb4VWV21HVBaGekcTH2nR7S0A6or7xfJ_jLtKq1Mg3Zxg7mNSNGl7fg9aE02yKP9U2d3Bx3yNknkfCyO_nW3G3sGMRZuxA0FaZZ9GAXtxVk9Aq-rgn5RiJnWb4jMx1QsmpETe3V1diTBLAOxCfqnBtXzSEl8x_6qPOOhu2wob4cMwnq5aBpQ_uBrBAkMfqtIjY__EMEOZyLzQ_vK1sO431E9EFlqp7MDZYP-J0ZV2bChG8gc6CBrL3l3gDTmVCk3netKOd2t81OsGjU-j0P66FAgoNWAbAdKdE2nK32F3S7thQJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند سبک برای طراحی پوستر با هوش مصنوعی
🎨
🔥
با اضافه‌کردن نام سبک‌های بصری به پرامپت، می‌توان ظاهر و حال‌وهوای پوستر را تغییر داد؛ از جمله: • Skeuomorphism: شبیه‌سازی ظاهر اشیای واقعی • Neumorphism: نرم، برجسته و سایه‌محور • Glassmorphism: شیشه‌ای و شفاف…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/694663" target="_blank">📅 22:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694662">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvT-Fmf0Qa5Vg1M6Z9Iy3yix7L-mkdPWEz9ywOoCuF4euKM97d4D9vwoAhiqupbCmjFgHLTVv1Stu8mF-0YlCxh7I3OgtMmWXpspudQe8Gh2TPw7tRCXaeVXydSvpZOwlXzDEEkCcfBqToElSIWnh2n2uEXxfa_oHUB1qn8njuffWjUINt2B9-dTJKtlNE33h3NZL_QnztkPAPyLP5j5E-aR4C_Wve9PPzJURzsInO4i2gjmvC9Sv9OA9N90r3GGXUX3yQ1D2hCWguXFFvboNFQOanIKUquN-2h7lY2i2TAchtXP3_GYJBNlyr7hI3bxr8z_Q9Txr1Q6dkszltCokw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کریستیانو رونالدو در پی خداحافظی از تیم ملی: یه زمانی، همه مردم پرتغال رو در جریان حقیقت و دلیل واقعی رفتنم از تیم ملی می‌ذارم؛ تیمی که همیشه برایش همه توانم رو گذاشتم و از هیچ چیزی کم نذاشتم. فعلاً فقط می‌خوام برای پرتغال و همه هم‌تیمی‌هام آرزوی موفقیت…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/694662" target="_blank">📅 22:04 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

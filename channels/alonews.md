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
<img src="https://cdn4.telesco.pe/file/qLhLmHA8OLXraenVcJUmytpExJKMH8newebthXSX8tIjEnzP6QW2pU2pOHXKeYM_l8-IbnaqMArVnH779FbVc-358vSHVVto8dXiOJpE9FiHoUiHC8mLwHnct6KT1x9GnwGogZBTHXIBjGi0qHDQtdcKq0-VKRjbgMJgs7u6Oj-SYmp-nSvQT6Pn11h2Dfx_QS8y-Er9pPr_Oi2-cIDz9vQAgH2iPa0byVHs9H0xgTAv8TCNybYDNNhQhMagss1hK810mOOzMJr09dChbMSpVcBmGJc51nzAPTlN8lTg5ol9IijeO9rP-exxzT6c_Hs3vk-2KJ7555Xl7Mwb-DgWng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 973K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 00:22:18</div>
<hr>

<div class="tg-post" id="msg-148278">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سفارت آمریکا در اورشلیم به شهروندان آمریکایی در اسرائیل و منطقه هشدار داده است که با توجه به افزایش تنش‌ها، احتمال بسته‌شدن فضای هوایی، لغو یا اختلال در پروازها و محدودیت‌های تردد وجود دارد و از مسافران خواسته وضعیت پروازها و فعالیت فرودگاه‌ها را مرتب بررسی کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/alonews/148278" target="_blank">📅 00:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148277">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
گفته می‌شود کارشناسان سپاه پاسداران ایران از منطقه باب‌المندب، بندر و فرودگاه مخا و همچنین پایگاه جبل‌النار بازدید کرده‌اند تا امکان نصب رادارها را بررسی کنند و بر روند حفر تونل در ارتفاعات مشرف به منطقه نظارت داشته باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/148277" target="_blank">📅 00:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148276">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KztRVUl5o3fiMiH8nuzUZUB2WWefvjbTPpSg2TzwW9guGUb0PIS9hrb93b3QowdZniZ7sm77osIlB3uJULaoRXMEDsc_dzL5u25OQP8-c9jU__EokFjW_m4MseJyvTkv_D_VOpI2GKt8DEKovMOLkGE3qpMzUgrhnHspes7AkZNyvywi9an6lP4kbFFFxGD_GWJyhzZzMca0kWOzvr_hGAMw2PKbB4aBf7Vjgy5S285HAuD5uIEHynmg983Lz9vgdCnfXiYo_1qIWzTbMCXWfo-KCJ3ivH-h0QvF1vDM0rEr1JA5a1dvYlDa3rzT8Sqeo9FZA8vgcQlPWXRVPfMoBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این وسط زن سابق سپهر حیدری وارد اونلی فنز شد تا عکس و ویدیو اشتراکی بفروشه
😐
اینجا ببینید
😐
👇
🚨
مشاهده فوری</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/148276" target="_blank">📅 00:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148275">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
امارات گزارش هاآرتص درباره هشدار به اسرائیل را رد کرد
🔴
یک منبع رسمی اماراتی گزارش روزنامه هاآرتص مبنی بر اینکه ابوظبی در هفته‌های پیش از حمله ۷ اکتبر، به اسرائیل درباره حمله قریب‌الوقوع حماس هشدار داده بود را رد کرد.
🔴
این منبع گفت: امارات مسائل امنیتی را از طریق نهادهای مربوطه با کشورهای دیگر مطرح می‌کند و چنین جزئیاتی در سطح رهبران کشورها مورد بحث قرار نمی‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/148275" target="_blank">📅 00:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148274">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af31257978.mp4?token=D8S0c02OzDsQVZWueXVj03R1DNT0lpTlVylNmxq-StPPWj9M2j4Fe97o5xmWcBtmszxsHKSEMnvUQCAWxHqmU4IhUd09G1jS24zQ_wTz6OWHBH2MIPD4Qo1M7tdmBtTpn14JB42jc4SHijE64pjjOQ4N-2rn8ijH3_SBetVO7vXWmLda4Z13NGRpg3X-BVC9x5kWHUNwCXiQINeIG08Qt1E1k--noCq4J_mL4grH2v0YQGd6Mitgc7uqCzNwTVdnn1lH_8dRgwGyUjk5tyZwdupPUJg0mFC7D7fcjn8gOwOyNtgMOVvxU_Bl9cqHx-fEPAN62WwkzH9BQYzCwGlLbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af31257978.mp4?token=D8S0c02OzDsQVZWueXVj03R1DNT0lpTlVylNmxq-StPPWj9M2j4Fe97o5xmWcBtmszxsHKSEMnvUQCAWxHqmU4IhUd09G1jS24zQ_wTz6OWHBH2MIPD4Qo1M7tdmBtTpn14JB42jc4SHijE64pjjOQ4N-2rn8ijH3_SBetVO7vXWmLda4Z13NGRpg3X-BVC9x5kWHUNwCXiQINeIG08Qt1E1k--noCq4J_mL4grH2v0YQGd6Mitgc7uqCzNwTVdnn1lH_8dRgwGyUjk5tyZwdupPUJg0mFC7D7fcjn8gOwOyNtgMOVvxU_Bl9cqHx-fEPAN62WwkzH9BQYzCwGlLbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عضو دفتر سیاسی انصارالله: این پیام به ترکیه و پاکستان ارسال شد که به خودتان احترام بگذارید؛ اگر از عربستان سعودی حمایت کنید، ما به شما حمله خواهیم کرد و شما را تنبیه خواهیم کرد، و دست‌های ما از فولاد خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/148274" target="_blank">📅 23:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148272">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4X9jGAmr4cfYjpzFHiPt66C_TMTVECsmQ0u2_wocqAgTYT3hmVg-Uc5tcQylSgSUczNciQX3kYoeFCQvSBopUCk0Z5WG5Bf50QIXoxG1HA1IwD-0EaAyfE5dF7LADmi4bO-89aD_tw-VmWxzez9KyS7HGyfFWadKHtNbYmdSY7bVsCklradoGZK5ODt9LV9jP-bnO93JgF5Mt6T4tufKLu9tcqqvsyyFsV-wCckDkAl48qNTb6WbrUClDKCUleZPy7iwJIL6wwhdLfAGIATPlSn3NDQMvCSvjFsQqjGmRyhOnXHTFXevf6t0pnkS8JB12PwLjjXEdv7PK81wiHJzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4e49b11fa.mp4?token=SEYKLD5LRPNqt5CBDMVOeS-TInaEHSGQW--I2-nH3dnUaHAsxu_7h3AWXTCEpeBgLxqKEY4Q9nIRWpcEwE6G7CCbqIln-85v4kylmAHty8KuyCXm5RVSlxT59jXhUntrZ9noVeLlB5gtYN_14653iUt1bn1sqcpX--wP7LJWb-BuCU73_ZFAC2lQGV3N0FOSxHRwO449MoIAXEJ36z8VGBW8u0iTCmftx9mXrM_tpKY6AfcltAST6V2kyIY1dc2ieZp30DXQEcjUCkuKJ96A3AkzklfrJD02HYGYAUBgFoGg0hE39qwvRxTf6_RFXHz9nEoPvsDxQ-V0KK0GCQhTVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4e49b11fa.mp4?token=SEYKLD5LRPNqt5CBDMVOeS-TInaEHSGQW--I2-nH3dnUaHAsxu_7h3AWXTCEpeBgLxqKEY4Q9nIRWpcEwE6G7CCbqIln-85v4kylmAHty8KuyCXm5RVSlxT59jXhUntrZ9noVeLlB5gtYN_14653iUt1bn1sqcpX--wP7LJWb-BuCU73_ZFAC2lQGV3N0FOSxHRwO449MoIAXEJ36z8VGBW8u0iTCmftx9mXrM_tpKY6AfcltAST6V2kyIY1dc2ieZp30DXQEcjUCkuKJ96A3AkzklfrJD02HYGYAUBgFoGg0hE39qwvRxTf6_RFXHz9nEoPvsDxQ-V0KK0GCQhTVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواپیماهای جنگی اسرائیل حملاتی را با بمباران هوایی به شهر کفر تبنیت و منطقه نباتیه الفوقا در جنوب لبنان انجام دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/148272" target="_blank">📅 23:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148271">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نخست‌وزیر لهستان: درس تاریخ 17 سپتامبر 1939 فراموش نخواهد شد، اگر کسی جرات حمله به ما را داشته باشد، با پاسخی قاطع روبرو خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/148271" target="_blank">📅 23:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148270">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
نقض منطقه پرواز ممنوع در محل اسکان ترامپ و اعزام اف-۱۶ به منطقه
🔴
هم‌زمان با اقامت دونالد ترامپ در نزدیکی کمپ دیوید، یک جنگنده اف-۱۶ امروز شنبه پس از ورود یک هواپیما به محدوده پرواز ممنوع، به این منطقه اعزام شد.
🔴
بر اساس بیانیه نیروی هوایی آمریکا، این هواپیما حوالی ساعت ۷:۵۰ صبح به وقت محلی رهگیری شد.
🔴
در جریان این رهگیری، اف-۱۶ مُنَوَّر (flares) شلیک کرد که احتمال می‌رود ساکنان منطقه آن را دیده باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/148270" target="_blank">📅 23:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148269">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQxK0AoUcGtWNgmG__iFkccoKaK4pTN99DJunNPTzHVo-FXsbkSid7WBzRq5CjqBQb2w1DdiJEI24n85pB79ztXOGV5tBBhfTSXd9cZnQA-65VupQKtMOCa_a-qF_AutL4Z9m279UeT1x248Lvvoj7rmmS4eNr3odOoo-71E16l48rfvTDP18BSYwohSCts60b_spgBG3pMtLUA1zhaK-3AAji3DvRp2Y_DURz37KZqZMh-y3d5S-DIK2RTd7B1MVnZCGfsc_Hhk0a4jRyMq-hPG5tlesJPjm9P-bDGG5nXMX1OarP_9wV8OawHTGJMpyeh109ZWJnybG2r_HCHHLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان سعودی میگوید یک موشک بالستیک شلیک‌شده از سوی نیروهای یمنی به سمت شهر ریاض را رهگیری و منهدم کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/148269" target="_blank">📅 23:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148268">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEGY-VAF9QFky0kkYFubdAqVqalsnytQhx137K6z_4F9PWaqhVzFz3zcfZNdfJd_RedZWo-ycojXXYjdvNycHapMf2F1DNGQ_3YYu2a4znCyHZZoLJT9TukaX3f9NGJCNTaRGcMnNOAVYb20TUbbLAiUu6nkFVyy-a8-dwKcnxbVQnT0WEd1wbNI6Up0TEgIbLlt57DkTQfHDiAQSDIsfVEKRC-_WTJSt2xt-rK19fNnEWjdWQIrk1yqc057A-Tk7ec4OiQJPwXc_b8XxrcIMN3Pz8_IpUKpIb7UqSWfFbg-UzpdT3xTeX7f8RRLSLSUoy9ox8aoRoLR0KSdaGURkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو تصویر از یک کشور به فاصله چند دهه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/148268" target="_blank">📅 23:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148267">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
رئیس مجلس نمایندگان آمریکا: جنگ با ایران در مرحله پایانی قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/148267" target="_blank">📅 23:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148266">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
وزیر خارجه ترکیه: ما نمی‌پذیریم که عربستان به بخشی از درگیری جاری میان ایران و آمریکا تبدیل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/alonews/148266" target="_blank">📅 22:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148265">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
امارات میوه و تره‌بار صادراتی ایران را برگشت زد
🔴
رئیس اتحادیه ملی محصولات کشاورزی:
بیش از ۲۰۰ کانتینر یخچالی ۴۰ فوت حامل انواع میوه، تره‌بار و سبزیجات صادراتی ایران، از سوی دولت امارات متحده عربی برگشت داده شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/148265" target="_blank">📅 22:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148264">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
سخنگوی سازمان غذا و دارو: واکسن اروپایی آنفلوآنزا امسال به ایران نمی‌رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/148264" target="_blank">📅 22:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148263">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فوری / ترکیه: آماده کمک نظامی به عربستان هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/148263" target="_blank">📅 22:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148262">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
آموزش و پرورش: ازین پس آخرین جایی که تعطیل می‌شود مدارس است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/148262" target="_blank">📅 22:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148261">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوری / ترکیه: آماده کمک نظامی به عربستان هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/148261" target="_blank">📅 22:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148260">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
واشنگتن‌پست: محاصره تایوان می‌تواند آمریکا و چین را وارد درگیری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/148260" target="_blank">📅 22:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148259">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpEMY3T-58N3EZiNKkvvGuzdZvzvvmfZN0q6fyxLyFUlN8Wm4YYYAkldaVzsEzetzVgtSZQgnH9Fchr_BTSIGHtN5YFvahdSyLQh45cLW0fpy4DRsAeyzDMMWdTl3J69KCXn8p-9coZkbNU3ZDBtlTrJs90bUNS5QrOE3Kd0DM1GbZWFqWFPzyBXofVXuWBBHsxTbIlBBHcSYaFdK2UtUyyfCat_Ao9vcz8mnqkwWyNRjMIT_RkJjFqo1u-jFmpBgY27a3hnRpYl9l5LQCHvlXvImH9IPvMfobTfOUfaUNKIkVg0DcuGsNXPRkBWFS3IisaUvTtoAy2euCZaRxt9nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتشار تصاویر از اپراتورهای زن پهپادهای FPV در ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/148259" target="_blank">📅 22:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148258">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
تاس به نقل از یک منبع ایرانی: ایران آماده بازگشت به مذاکرات است، مشروط به اینکه آمریکا حسن نیت خود را ثابت کند
🔴
تهران همچنان برگزاری مذاکرات درباره موضوع هسته‌ای را ممکن می‌داند، اما تنها پس از اجرای کامل توافق اسلام‌آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/148258" target="_blank">📅 22:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148257">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
دولت لتونی فاش کرد که اطلاعاتی در اختیار دارد مبنی بر اینکه روسیه در حال برنامه‌ریزی برای حمله ای محدود به اعضای ناتو است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/148257" target="_blank">📅 22:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148256">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
حوثی های یمن: با تعداد قابل توجهی موشک بالستیک به اهدافی در ینبع، تاسیسات آرامکو و ریاض حمله کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/148256" target="_blank">📅 21:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148255">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ترامپ: نیروی هوش مصنوعی [در ارتش آمریکا] تشکیل می‌دهم
🔴
رئیس‌جمهور آمریکا: درحال تشکیل نیروی هوش مصنوعی هستم؛ درست مانند «نیروی فضایی» که در دوره اول ریاست‌جمهوری‌ام تشکیل دادم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148255" target="_blank">📅 21:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148254">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل : ترکیه به طور رسمی مجوز فعالیت بانک ملی ایران را در استانبول لغو کرده است. این تصمیم، عملاً تمام فعالیت‌های این بانک را در کشور به حالت تعلیق درآورده است، از جمله تمام شعب آن در شهرهای استانبول، آنکارا و ازمیر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/148254" target="_blank">📅 21:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148253">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
به گزارش شبکه i24NEWS، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، قبل از سخنرانی خود در مجمع عمومی سازمان ملل، در شهر نیویورک فرود نخواهد آمد.
🔴
به جای آن، او در یک پایگاه نظامی خارج از شهر به زمین خواهد نشست و سپس به منهتن و مقر سازمان ملل سفر خواهد کرد، جایی که قرار است روز پنجشنبه ساعت 14:00 به وقت محلی سخنرانی کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/148253" target="_blank">📅 21:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148252">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025ae7d2df.mp4?token=jJAP2aX3ALaxunkW1Vkz39NQGlbhaknGHsBcGOdyKVE9-n7riax362PyNOjXibETtBXNy-KoLknyT9qaS_-ZwZtZCl1yyfWVnXIzmaUYTYFNZ0M7GaR_b2BOLVSLpnSqC_ExFck6e-QzVxHS_HGxgTKXoW7DdvJ6dr15CFlDaRA0BOWa6m6_2YecVfixe3DEZ2Aji8Kt3N3MaMLn2wVxO4X2QdUQGgkPIyYSue1wbwi6T3n25PNo20cq4XQIMIUpirtE2zqmRw23XXCmbh96MqzOQFno3e8S_t99aIebx71nC5mVCiycWBgS9KlePMnOEkWcMkTDq7zZYSPSbyE3pIzwaTGWCogcV5bccFSUNLyjMR3W0IsCWoyYwFrluavDcuIgqfdfmvOXKJ76GWLEs_bFVF7CDk9GzOfhB8WIlzwiNjlWziilTQDwV05bNcDSV6kHwbUq-PBANwR0hi0ipyN9W21igkdbb6DTvxA4AkQEB1OO2AEVxvQAXyZFzMup7JufoZFxgNmRlMTFkFg6bhdQDEbUaq7Htkipa4mcHD0Bw8K8AjXF5WXneUBCCavBtrzUxNUPn5TE2QvcbGuBpqb96gMi0bsQpKMzmIlCAQPjwI3LZ9vtW2_-283q_q47tT7z6-Vn-wdTRDrnmxSPD7-vX_EFc_fO6vKJ9SgyEZs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025ae7d2df.mp4?token=jJAP2aX3ALaxunkW1Vkz39NQGlbhaknGHsBcGOdyKVE9-n7riax362PyNOjXibETtBXNy-KoLknyT9qaS_-ZwZtZCl1yyfWVnXIzmaUYTYFNZ0M7GaR_b2BOLVSLpnSqC_ExFck6e-QzVxHS_HGxgTKXoW7DdvJ6dr15CFlDaRA0BOWa6m6_2YecVfixe3DEZ2Aji8Kt3N3MaMLn2wVxO4X2QdUQGgkPIyYSue1wbwi6T3n25PNo20cq4XQIMIUpirtE2zqmRw23XXCmbh96MqzOQFno3e8S_t99aIebx71nC5mVCiycWBgS9KlePMnOEkWcMkTDq7zZYSPSbyE3pIzwaTGWCogcV5bccFSUNLyjMR3W0IsCWoyYwFrluavDcuIgqfdfmvOXKJ76GWLEs_bFVF7CDk9GzOfhB8WIlzwiNjlWziilTQDwV05bNcDSV6kHwbUq-PBANwR0hi0ipyN9W21igkdbb6DTvxA4AkQEB1OO2AEVxvQAXyZFzMup7JufoZFxgNmRlMTFkFg6bhdQDEbUaq7Htkipa4mcHD0Bw8K8AjXF5WXneUBCCavBtrzUxNUPn5TE2QvcbGuBpqb96gMi0bsQpKMzmIlCAQPjwI3LZ9vtW2_-283q_q47tT7z6-Vn-wdTRDrnmxSPD7-vX_EFc_fO6vKJ9SgyEZs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) در ادامه تحرکات نظامی خود در جنوب لبنان، اقدام به تخریب منازل  و زمین‌های واقع در شهرک «منصوری» با بلدوزر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/148252" target="_blank">📅 21:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148251">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plQqZv4Edh2bho4RjQdONrYWLHBEamkEv-LZCMF0YC-MoOf6W0HT7b_ir4T3jFNGgj47LfeaIOLmL9hFeE0_LTeWGTC8wChQayLfEv4x8XEQlzPQJgh7OIhWpjUrCncOJiPGC8-CqkGb9r0i_grpakw697ez0QqJzUrMOg89mxPKZwKJt5ViAUF-jhhzRb0ugpW9-r2LUTv8VyaS_NGHz3pnxhl8mTQDmAjwT0Mb-LYUucuzHY6icueVzgUr-JPA8nFTTMElxQD8gbKPlb6fFR7xAgQuWzo8p4EB4WkzyLGaMuB0AsRokyhJNWh7CjEraKV9D_y3mTzjCe5QmmBR_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: متأسفانه، دادگاه عالی ایالات متحده از شجاعت برای بزرگ کردن دوباره آمریکا محروم بوده است.
🔴
در طول ۶ ماه گذشته، با تصمیمات معیوب، سیاسی و احمقانه خود در مورد تعرفه‌ها و شهروندی حق‌الولادت، آن‌ها هزاران میلیارد دلار به ایالات متحده آمریکا خسارت وارد کرده‌اند و برای همیشه روشی که مردم از طریق آن شهروند کشور بزرگ ما می‌شوند را تخریب کرده‌اند.
🔴
این فصلی غم‌انگیز در زندگی و دوران آمریکا بوده است، اما ما پیروز خواهیم شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/148251" target="_blank">📅 21:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148250">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daafee079a.mp4?token=VV4nx9QQvwMGD-W2HzL05DW7BubQMUgWiktN4tbjY6JCXqOhoBnnEHSGaVxIoGH1R5XXmh_WG1FOErjpntFvYo7VtOQUD2v-vcxCNX7DHPAITxivuLBmzXb_KArbKvo6LQ5xuyLC5A4S9BlVFveSgTEe6shlhv5gTZwy917zsWSDaJE8pcPfDUHZzEXO0cEfRG4m5RGx3LokblnXKLDIDF-67mvw6TzzxfWz2IpsWvqewlb9NVmN6GDjIcXkuPM-dp-oUZM3i0rpdB9eACL21zM_AzEum8JhDlqEu-Ksboy7ALcR4pFYUBWwQG66mpl2xnj813N_OJjoiWrW1_yotiyJceruwbesd6FW7xK0RK7kNoLqOUEKYucveXEmLRODhEjjKFG6nZojvVSVoL65CoCrkeApqKIhcfTqrXREknnf3S3rqq6fpH46JJSV93hOnJH0G-5ZtZZyLe3S_-k3WeBC5KOimAGWorDLRRiWaK9_5AbMRlUBdKGhKi4jgITYdpJqHyxrP5Hxo5Q84dHBDVfvutuz5ibn1SKZGOdl7YHWmhSlB7rzL_5HlhEpgKWGn1dgf85kEf-BELM-tZicwoKHWfgkm-Xlmn0hdlQ2etg_7HoBK2YDol6RK-mW8rulR7628aoo25WvTMfzk6JG9CJCOOiUc7Teasz6RlRD8GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daafee079a.mp4?token=VV4nx9QQvwMGD-W2HzL05DW7BubQMUgWiktN4tbjY6JCXqOhoBnnEHSGaVxIoGH1R5XXmh_WG1FOErjpntFvYo7VtOQUD2v-vcxCNX7DHPAITxivuLBmzXb_KArbKvo6LQ5xuyLC5A4S9BlVFveSgTEe6shlhv5gTZwy917zsWSDaJE8pcPfDUHZzEXO0cEfRG4m5RGx3LokblnXKLDIDF-67mvw6TzzxfWz2IpsWvqewlb9NVmN6GDjIcXkuPM-dp-oUZM3i0rpdB9eACL21zM_AzEum8JhDlqEu-Ksboy7ALcR4pFYUBWwQG66mpl2xnj813N_OJjoiWrW1_yotiyJceruwbesd6FW7xK0RK7kNoLqOUEKYucveXEmLRODhEjjKFG6nZojvVSVoL65CoCrkeApqKIhcfTqrXREknnf3S3rqq6fpH46JJSV93hOnJH0G-5ZtZZyLe3S_-k3WeBC5KOimAGWorDLRRiWaK9_5AbMRlUBdKGhKi4jgITYdpJqHyxrP5Hxo5Q84dHBDVfvutuz5ibn1SKZGOdl7YHWmhSlB7rzL_5HlhEpgKWGn1dgf85kEf-BELM-tZicwoKHWfgkm-Xlmn0hdlQ2etg_7HoBK2YDol6RK-mW8rulR7628aoo25WvTMfzk6JG9CJCOOiUc7Teasz6RlRD8GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش سوزی در یک فروشگاه درپی حمله موشکی روسیه به شهر دنیپرو اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/148250" target="_blank">📅 21:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148249">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فوری/ساعاتی پیش عربستان سعودی رسماً از پاکستان و ترکیه خواسته است تا پس از حمله به فرودگاه بین‌المللی ریاض،
پیمان دفاعی مکه را فعال کنند و اقدام نظامی علیه حوثی‌های یمن را فوراً آغاز کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/148249" target="_blank">📅 21:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148248">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
وزیر کشور پاکستان فردا به ایران سفر می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/148248" target="_blank">📅 20:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148247">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1367899db.mp4?token=vL_zWd21t6kFGcZM5Lp3jRmbvrTEACdu7c8f5PGh5lusJ1FXJB2zTCfmWWHus1pDd--clkdBqCTBHoFfU8eRi46MHeFzn-9Q58jeqUR1afQ6GsHNld9vY2agb7Q5-XDTj97mzaExgdossCVgj7k90E21_RzmICiQhtiSQur7iMOzdD3b4AWpn9gO6UK1nHPC5mc09InRdiVx_R-QGAeJOtZK4NZz6M-U-1iKCZ-EuRNXLqJRL61_j_ezq5ROxeiVdWIY9aBglyWjI9OzkQJ7XvYCkXe7mUbn3qM64J6mUblYBlKBI7wwKGcCXk32zJ23zHFKdFqF5CfgPjziXY3RUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1367899db.mp4?token=vL_zWd21t6kFGcZM5Lp3jRmbvrTEACdu7c8f5PGh5lusJ1FXJB2zTCfmWWHus1pDd--clkdBqCTBHoFfU8eRi46MHeFzn-9Q58jeqUR1afQ6GsHNld9vY2agb7Q5-XDTj97mzaExgdossCVgj7k90E21_RzmICiQhtiSQur7iMOzdD3b4AWpn9gO6UK1nHPC5mc09InRdiVx_R-QGAeJOtZK4NZz6M-U-1iKCZ-EuRNXLqJRL61_j_ezq5ROxeiVdWIY9aBglyWjI9OzkQJ7XvYCkXe7mUbn3qM64J6mUblYBlKBI7wwKGcCXk32zJ23zHFKdFqF5CfgPjziXY3RUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ساجده سلیمانی، مجری شبکه یک:
آقای جبلی میگن ۷۰ درصد مردم صداوسیما رو دنبال میکنن
والا من ۵ سال تو شبکه یک مجری بودم وقتی میرفتم بیرون جز یه مشت پیرمرد و پیرزن که صبح برای نماز بلند میشدن و تلویزیون میدیدن دیگه کسی منو نمیشناخت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/148247" target="_blank">📅 20:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148245">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‌
👈
سخنگوی وزارت خارجه: سفر وزیر کشور پاکستان به تهران دربارۀ روابط دوجانبۀ ایران و پاکستان خواهد بود و قرار بر تبادل پیام خاصی دربارۀ میانجی‌گری نیست.
🔴
شروط ما مبنای مذاکرات بود و آمریکا آنها را نقض کرد با این شرایط نمی‌شود از پایان جنگ صحبت کرد
🔴
ایران و عمان درخصوص تعیین مسیر امن تردد در تنگه هرمز به تفاهم رسیدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148245" target="_blank">📅 20:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148244">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YnDOetuTimbIw4agZhvSxgG-WeS1Fr8c3A_p56VnHWxprsdhk40a7H3pgZ3gcBBZNI60rvjeDUvXgUAPW-7hxDFqXIDutOyd_Ty6y9RuW3vC0Kd-rATMMUEINjam5WP_pkiFYNK8aFjl_vLDkSpXt8XGgsKRnktvBrilvCv8moJFFYwqPzalxQEp8xTqwCL1Ut1zIqioZo67WSQssKaLTFrrd_aOiDu4AC0jcDRABgahMpqbkVNWafKI-FeEA27Q8H3H6Zonsq2N9hFRljsdoMqe6BEUktkBwwrWYRLTYCfyabmcuOnr0WlXxFbHb-sZChuqQMdn5PU2_JJtMvnhkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر وایرال شده یه خانم تو دورهمی دیروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/148244" target="_blank">📅 20:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148243">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل:
قطر شروط تهران برای پایان جنگ را به آمریکا منتقل کرده و ایران اکنون منتظر واکنش دونالد ترامپ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/148243" target="_blank">📅 20:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148242">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دلار و طلا تا کجا بالا میره
⁉️
🚫
پاسخ عجیب هوش مصنوعی
👇
https://t.me/+cs85WnZxgpM1NjRk
https://t.me/+cs85WnZxgpM1NjRk</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/148242" target="_blank">📅 20:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148240">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
هشدار سفارت چین به شهروندان خود در عربستان
🔴
سفارت چین در عربستان سعودی اطلاعیه اضطراری صادر کرد و از شهروندان چینی و شرکت‌های تحت حمایت چین در این کشور خواست تا اقدامات ایمنی را تقویت کنند و بلافاصله پس از دریافت هشدارهای امنیتی از سوی  مقامات محلی، به پناهگاه بروند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/148240" target="_blank">📅 20:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148238">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZDDVgQRC-KZbKmxEFvqB7PM3nAegaImD-4M0IhYXx8AOQriZIyFblN9JhtppFuesNIk-FO-o9BZcsVrb0EOFXZWOOwJ2jrDHliJeAJZVISCfxBiYJDfLBa6kULxU5ZXnjvRA4w8scW7pmmpic_40BZyG2Ux965xPn51Uu8Dz1ax3-oMT_oEHCbxhpNiqYrgjTnQLd-7P-YgCr9lz2VTSq_ydpwlcmJkI5064BsGL5IJr1WvFS1uz4eSegu61MeGZBCuI46FYx0q0ph7Yn3QIYNpVrew3tNwJ5coACIigOivewlp75h5fUWy1VBzuCscFoxN1H4VowYci7mDGsOyzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mzPqDRU47SNic257HB1_alTUmwZDvUaEz0i3VsXGlM4ySjcdwU5FMrQQYCz4el60ncWBzhm6fDVwC_QHvv9QJN8jv8iQQPZCecbvk7PKsB16fPaZG4nzt8uNN1fDpXYX9bEPODtW5IWhgtzYtBzqdi0t1AeQcjpQg7c3qPjhTBpie7LqdgxP-L7GhddXOI_kyD0ePHaU3V6Jh41PVhkwq5YuM9jTibUssMJkFczjeEdG7bIYKxAic4m_wdyPKjl0Q0z-lfWz0w3TFhVrOsbc9E8g_zT0s3rdBw8IqA02UQkRcV6i52i__7uHJqJ87U5VffC5HB6XN8cKoXnZxx3TmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
قیمت امروز انواع محصولات سایپا و ایران‌خودرو تو بازار آزاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148238" target="_blank">📅 19:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148237">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
نایب‌رئیس کمیسیون امنیت ملی: عبور کابل‌ها از تنگه هرمز هم منوط به مجوز ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/148237" target="_blank">📅 19:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148236">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
نتانیاهو: دو سال پیش، نصرالله هنوز در پناهگاه خود بود. حالا اون‌کجاست؟
🔴
سنوار کجاست؟ ضیف کجاست؟ هنیه کجاست؟
🔴
و ما چه کاری با خامنه‌ای کردیم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148236" target="_blank">📅 19:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148235">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ساعت کاری جدید ادارات از اول مهر: از ۸ تا ۱۳
‏
🔴
رئیس سازمان اداری و استخدامی کشور در بخشنامه‌ای ساعت کاری دستگاه‌های اجرایی را از ابتدای مهر تا پایان سال جاری، از ساعت ۸ تا ۱۳ تعیین کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148235" target="_blank">📅 19:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148234">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‏
👈
محسن رضایی: ما خواهان پایان جنگ بین عربستان سعودی و یمن هستیم و من معتقدم یمنی‌ها نیز خواهان توافق با عربستان سعودی هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148234" target="_blank">📅 19:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148233">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی، دبیر شورای عالی امنیت ملی: ما با میانجی قطری که شرایط ما را با هدف توقف جنگ به واشنگتن منتقل کرد، در تماس هستیم و منتظر پاسخ رئیس‌جمهور آمریکا هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148233" target="_blank">📅 19:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148232">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALn9dpzSFY59LxqSJ1mjAtiUbPrH9t5gM6TaPsfu-piiR758aBBAejmxssYyB5nuNef0J_lT8k_k80e4J0s-yRlHmShEth3Y2ZjdjPtHbbyoF5fnhiKr1Cksz52In0ygKSYFMS_cuSXO3CrA4b1Xe-hHDEJrSGyj-v1yMcEfyz3WhKqW9Y4Nbn6zlMA-kHd4POEGUFO13tcr3CEffdXTT2EYAg4NOtyrhSd6W4PQOSaxouXRTTLF2aZDPgRXZ-7QyyZCr09-XbApumLwFvXDLX-NlWAe-y5UHY43OVzSIuLIECxGCDSP1GcP8cX8QuMEmu8gPTwKxtG-iGYHR4A4iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ماشین تارا 3.5 میلیارد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148232" target="_blank">📅 19:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148231">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qogMSTC8iOLM01v7AuJPaB6gGLI5qTXfzZlc8eGeqSNrFj3uq416B6YBx2esrU-9brlPZGk7jkCxK2nUSBVmJVyVQrUHXRyyF7p8vbLyQ3koLutkUJn5_xdMJ4XITk14QvWxTEZPoj9HueuwAy3DFh2NPBM3aXhrIrj5QngxTEzhEma_gD4cFH0MAsAlxt2sFCy96iyLUZVCv_hfNqpOHrnkwijeDAfWBYAfpGlJbQftvM206IrwiqGoPcE7WuskOQWEa90zYIFMwqQGA17JzV-msNVHDC8gIu9o4nuRHLA2UKGFtBAF8aheTu2MRxOM37huatNpE_3A9D0ipWKJlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کوبا در خاموشی سراسری فرو رفت
🔴
شبکه برق کوبا به‌دلیل نقص در خطوط انتقال فشارقوی از کار افتاد و میلیون‌ها نفر بدون برق ماندند؛ تلاش‌ها برای احیای تدریجی شبکه آغاز شده و برق برخی مناطق و بیمارستان‌های هاوانا وصل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148231" target="_blank">📅 19:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148230">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3De9_wJe7SF2VMMqG2ad4Ii_kUmgxjVO-zhkGYoyzN1w7nbDEJRg4zAcPPga05G2h4k5LdNccbi9fuFx47KVvRBJLwFiS6s0JRHRtKus7bigWwmfiPQ2Wd5Xv7gd7pHqlMtO8GWpu93AbZvFRM-mjZ4gAoosGdwlRNrnRYV9RQTWDKF27MGZ0B3Ldewf8j3jxL2EsijIcdKN0mkbzEmqLVjKIwSwL5VHbtho6z02uRiCL6w7STC0Us2eSHvTGXLYTMRyc8sk9AWoOyVQgM_mnnXiIOi_5Moq3KZAPM7aqkDePayRBZ3WxMdtcXLNYYoqyTrfYuOe91b-vzsHwRp4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ نظرسنجی‌ای در تروث سوشال برای تغییر نام هوش مصنوعی به «هوش برتر (SI)، هوش افراطی (EI) یا هوش معظم (SI)» منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148230" target="_blank">📅 19:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148229">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
گاردین: بحران سوخت در فرانسه در حال وخیم‌تر شدن است، زیرا جنگ در ایران باعث اختلال در عرضه انرژی شده است. در حال حاضر، ۱۱ درصد از پمپ بنزین‌ها کمبود بنزین یا گازوئیل را گزارش می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/148229" target="_blank">📅 19:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148228">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
فیلد مارشال رضایی: برآوردها و محاسبات رئیس جمهور آمریکا در مورد ایران اشتباه بوده و جنگ توسط نتانیاهو آغاز شده است.‌‌
🔴
به نفع واشنگتن است که شرایط ما برای خروج از جنگ را بپذیرد و تهدیدهای ترامپ نتیجه ای نخواهد داشت و ما آماده یک جنگ سرنوشت ساز هستیم.‌‌ …</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/148228" target="_blank">📅 19:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148227">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
پولیتیکو نیز اعلام کرد که خبرنگارانش در روز شنبه از ورود به محوطه کاخ سفید منع شدند، پس از آنکه ترامپ تصمیم گرفت این رسانه را همراه با سی‌ان‌ان و ام‌اس‌ان‌او از ورود به مجموعه کاخ سفید منع کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148227" target="_blank">📅 19:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148226">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">ویدیو وایرال شده از ارزش پول ایران
ادم نمیدونه بخنده یا گریه کنه..
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148226" target="_blank">📅 19:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148225">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
فیلد مارشال رضایی: برآوردها و محاسبات رئیس جمهور آمریکا در مورد ایران اشتباه بوده و جنگ توسط نتانیاهو آغاز شده است.‌‌
🔴
به نفع واشنگتن است که شرایط ما برای خروج از جنگ را بپذیرد و تهدیدهای ترامپ نتیجه ای نخواهد داشت و ما آماده یک جنگ سرنوشت ساز هستیم.‌‌
🔴
ما نقاط ضعف ارتش آمریکا را می دانیم و بیش از گذشته برای مقابله با حملات هوایی آن آمادگی داریم.‌‌
🔴
به این باور رسیده ایم که استراتژی خود را در قبال واشنگتن پس از خروج از یادداشت تفاهم تغییر دهیم.‌‌
🔴
اخیراً یک موشک ضد کشتی را در نزدیکی یک ناو هواپیمابر آمریکایی آزمایش کردیم.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/148225" target="_blank">📅 18:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148224">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
حمله هوایی نیروی هوایی پادشاهی عربستان به مواضع انصارالله/حوثی در جبهه شرقی تعز، یمن غربی.
🔴
این جنگنده‌های نیروی هوایی عربستان از پایگاه هوایی ملک فهد در طائف، عربستان غربی، به پرواز درآمدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/148224" target="_blank">📅 18:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148223">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
پیت هگستث، وزیر جنگ: برای پیروزی، به رهبران کشنده‌ای نیاز داریم که بدانند چگونه پیروز شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148223" target="_blank">📅 18:37 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148222">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6cbcc478.mp4?token=XEc0Hx66khmALQc1lKH0E227CSAgJao6me2tuxlbZMjUfa6wdIFnaoWId6Fs3oH-KdtERPxx_xS0bb64ykbQMQWH4chS5cZEkdDRDJ-gVeFGxd1PpMukwmThc4LXrCj_FwCTucnW_gy3fJl46x_KzJ5uAAGsMXQBsYrs91G5xTtHTcAmUlanZdSasnuLUEXl4q_8jDOuopTl-OSY9BpVle_Yfjgn_yxAC758w-AxxglAjUirD-JZjjp0WVMoRWAsIY6oytkXTt4krTkb1KK7V3FckmQEOBbhrNT65PO1FE8lLJ8-r51AeT8TJvfxE9l4Jyvsa45uHV9yP_z65Mdgrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6cbcc478.mp4?token=XEc0Hx66khmALQc1lKH0E227CSAgJao6me2tuxlbZMjUfa6wdIFnaoWId6Fs3oH-KdtERPxx_xS0bb64ykbQMQWH4chS5cZEkdDRDJ-gVeFGxd1PpMukwmThc4LXrCj_FwCTucnW_gy3fJl46x_KzJ5uAAGsMXQBsYrs91G5xTtHTcAmUlanZdSasnuLUEXl4q_8jDOuopTl-OSY9BpVle_Yfjgn_yxAC758w-AxxglAjUirD-JZjjp0WVMoRWAsIY6oytkXTt4krTkb1KK7V3FckmQEOBbhrNT65PO1FE8lLJ8-r51AeT8TJvfxE9l4Jyvsa45uHV9yP_z65Mdgrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت
هگستث، وزیر جنگ:
برای پیروزی، به رهبران کشنده‌ای نیاز داریم که بدانند چگونه پیروز شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/148222" target="_blank">📅 18:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148220">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62dbc95860.mp4?token=NOJF5fhmNA4rJ5VnD0zfS1UhedwBTJyeEIQD7e2-jmaK0ej6EgPbK7GL4gPCzIcsJfGpePe49rbpCzc_64e_ZsmoSuEEPV1y4JVJCh_aZOQ7i7I8lSlEjw3KcAXeTL_I3cEGqBrwHZrCGIM121C7Mm1q6DlQv_SxJyA1aIkf0keEJSBGOUc5SFUSnShUMwQyHVY1dWtb4BB4EUqM9kRehnaIzwFRcxM6zoYSLRKD4aBgxSDbj98rDi8l1N-Iy0h7Y8ppOZ8PvWTFv-zQeU58fddzvItYOVGeX_DuOYhvusTSlcQEUOH06Z2UkGhguGnC6Xxm_h2C8CrjhvxYyQ3Hlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62dbc95860.mp4?token=NOJF5fhmNA4rJ5VnD0zfS1UhedwBTJyeEIQD7e2-jmaK0ej6EgPbK7GL4gPCzIcsJfGpePe49rbpCzc_64e_ZsmoSuEEPV1y4JVJCh_aZOQ7i7I8lSlEjw3KcAXeTL_I3cEGqBrwHZrCGIM121C7Mm1q6DlQv_SxJyA1aIkf0keEJSBGOUc5SFUSnShUMwQyHVY1dWtb4BB4EUqM9kRehnaIzwFRcxM6zoYSLRKD4aBgxSDbj98rDi8l1N-Iy0h7Y8ppOZ8PvWTFv-zQeU58fddzvItYOVGeX_DuOYhvusTSlcQEUOH06Z2UkGhguGnC6Xxm_h2C8CrjhvxYyQ3Hlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث وزیر جنگ:
اگر ارتش ایالات متحده آمریکا رو به چالش بکشید، شکست پایان شما خواهد بود.
🔴
در دوران ترامپ، جهان آموخته است که ما فقط برای پیروزی می‌جنگیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148220" target="_blank">📅 18:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148219">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54da84d255.mp4?token=CLY3OfZ0fjGiBcPbPkebuLn9_fm8rWrRn4qPB_s9JwMwi9j-GtuJcy9SWz-67RtU-86X4L0IOIcdRQTgF29ch_JnT5PjatRokm4rGns9DI5LBGbl5Y-HiG-rioMDKuIqWPgA2mmCjgTcyFNK2zJ1A0i2wFdbBjnk2Iwcc77IKsgsMmZR9Xo-GWydSZaIXEbk8OGvMbn1jmZRXadzoppnU0I8f25E2Ows_aVderXfYXNULJOQI3o2Dmn3iV1t3QyH-x2qu_HCci0_07Dw9UJpNi7JoMciMQir1GqUbyVHE-xw7frPxCkzZM2uNRJIDvwDYjVUdurIIXAA3UuwXuoZnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54da84d255.mp4?token=CLY3OfZ0fjGiBcPbPkebuLn9_fm8rWrRn4qPB_s9JwMwi9j-GtuJcy9SWz-67RtU-86X4L0IOIcdRQTgF29ch_JnT5PjatRokm4rGns9DI5LBGbl5Y-HiG-rioMDKuIqWPgA2mmCjgTcyFNK2zJ1A0i2wFdbBjnk2Iwcc77IKsgsMmZR9Xo-GWydSZaIXEbk8OGvMbn1jmZRXadzoppnU0I8f25E2Ows_aVderXfYXNULJOQI3o2Dmn3iV1t3QyH-x2qu_HCci0_07Dw9UJpNi7JoMciMQir1GqUbyVHE-xw7frPxCkzZM2uNRJIDvwDYjVUdurIIXAA3UuwXuoZnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمزه صفوی: من جای ایران باشم، دنبال ارتباط مستمر با ونس می‌روم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148219" target="_blank">📅 18:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148218">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5phdGSj23PJrjOPCq-D24XozCv70VQLv81W17uDMJUnSRlVGJxmwXYDXovSWs4vfo48VwSZcr5yxZDyS5sS-H0aUMn7iLOqAs1SFJfORlSYSrQxyh2gDxP7GUn9OclH93dJOnf3ekq4Gf7x7FIUXW8c76M2mK0hwvq_OrJJVZf_XKir27jdSBCNKDD-6cmABp1ZPYMhcqLH2zMdLFbK33EEuHQ-v29a4ZpR-la9piu-iXwO8VC_sBTxSkwI5vBQSk4onue_3tLcnjhmu2QaRE4QDPTC9sIOmBcL2puEBZqpYbyJmBXL9XfQFuvdbFKSspTCtrGnZi67Q5Z--98LwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخی تراستی‌ها برای افزایش سهم محموله‌هایشان، کشتی‌های رقبا را لو میدادند تا توقیف بشوند…
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148218" target="_blank">📅 17:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148217">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75801e50d0.mp4?token=T6dGIwHWmt_vaA9DzmFWXcrTvEP0cD-WYD_VeF0n8be2N1WHPJnLJkgXHxCw6xH1esXzJxEHx0dURiSQUDQta4XOvs9q78hszZF-2XQUgINBcNAqq3v-vnNLO4C1FLsuAC4mFNAP-1EvFBApcinbDovmsFbVSuyavEh1odPKJujjYI51w5sBehYwyNnlOm8QNW-LlbIzGD63GIIeOP38cimjbSwmwEpcYlSjFwxVu_G8wnlsGbjSjJpxBZqJvwvXVMYLprayijpgGmq8oxaAFvftUKK-WocgJek8Fj31djZMNMgqOyngUF4wbaSSxazzNXFOEOwZDYX6_q-tQSoKlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75801e50d0.mp4?token=T6dGIwHWmt_vaA9DzmFWXcrTvEP0cD-WYD_VeF0n8be2N1WHPJnLJkgXHxCw6xH1esXzJxEHx0dURiSQUDQta4XOvs9q78hszZF-2XQUgINBcNAqq3v-vnNLO4C1FLsuAC4mFNAP-1EvFBApcinbDovmsFbVSuyavEh1odPKJujjYI51w5sBehYwyNnlOm8QNW-LlbIzGD63GIIeOP38cimjbSwmwEpcYlSjFwxVu_G8wnlsGbjSjJpxBZqJvwvXVMYLprayijpgGmq8oxaAFvftUKK-WocgJek8Fj31djZMNMgqOyngUF4wbaSSxazzNXFOEOwZDYX6_q-tQSoKlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اسرائیلی به تخریب در مناطق مایس الجبل و المنصوری در جنوب لبنان ادامه می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148217" target="_blank">📅 17:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148216">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
حسین پوراکبریان، عکاس و طبیعت‌گرد، تصاویری از پرواز صدها فلامینگو بر فراز دریاچه مهارلو در استان فارس منتشر کرد و در توضیح این تصاویر، با اشاره به گسترش نمک و فاضلاب، نسبت به وضعیت زیستگاه فلامینگوها ابراز نگرانی کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148216" target="_blank">📅 17:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148215">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
رئیس‌جمهور لهستان: پوتین در حال برنامه‌ریزی برای حمله به کشورهایی حامی اوکراین است تا اراده ناتو را فلج کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148215" target="_blank">📅 17:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148214">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
این تاریخ بیت کوین میاد رو 200هزار دلار
از این تاریخ پرواز میکنه تا 200هزارتا
👇
https://t.me/+4jOgodAq96dmYzY0
https://t.me/+4jOgodAq96dmYzY0</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148214" target="_blank">📅 16:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148213">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d70147ef.mp4?token=mOj61g0KHkRZH8TJRK5fISL4S19x-ZbOIC4VPGgmEOSrNAowLxjq1Sz2hjD9IFLrnhbwb1dgOIsghV8ifVJaEkHznzErrKeL3q1tqq4w4L4880rKpVc3j7wU536rTlgAmqIvPN1G75KNBxGcgtkGFk9mppGFawel9aEsWVkKfOo8VWGGTyYviKDmZ0f3pSFgowzDPRqVUXvBtfNX36Dy7-TJkjbewu0XUYwHUwnyY5hBeTc0Jn8_W0G1B48AfPAOwUCmFwEBh7UutG0FWTqbk0HmPM8pY3KffSm1TJ6KXXs61e3WHxiyzyNaJycWwkAr1yYRjU9EC0Q9cRY8oT3fxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d70147ef.mp4?token=mOj61g0KHkRZH8TJRK5fISL4S19x-ZbOIC4VPGgmEOSrNAowLxjq1Sz2hjD9IFLrnhbwb1dgOIsghV8ifVJaEkHznzErrKeL3q1tqq4w4L4880rKpVc3j7wU536rTlgAmqIvPN1G75KNBxGcgtkGFk9mppGFawel9aEsWVkKfOo8VWGGTyYviKDmZ0f3pSFgowzDPRqVUXvBtfNX36Dy7-TJkjbewu0XUYwHUwnyY5hBeTc0Jn8_W0G1B48AfPAOwUCmFwEBh7UutG0FWTqbk0HmPM8pY3KffSm1TJ6KXXs61e3WHxiyzyNaJycWwkAr1yYRjU9EC0Q9cRY8oT3fxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جوزپه کاوو دراگونه، رئیس ستاد نظامی ناتو: در مورد فعالیت‌های ترکیبی، درخواست خودکار ماده ۵ (معاهده ناتو) مطرح نمی‌شود، زیرا معمولاً این فعالیت‌ها از آستانه بحرانی پایین‌تر هستند.
🔴
منظورم این است که یک حمله مستقیم در دستور کار نیست. اما یک حمله مستقیم، به طور کلی، فوراً منجر به درخواست ماده ۵ خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148213" target="_blank">📅 16:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148212">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
فوری / گزارش انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148212" target="_blank">📅 16:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148211">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
کمیسیون امنیت‌ملی: کاری کردیم که آمریکاییا دخل و خرجشون دیگه نمیخونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/148211" target="_blank">📅 16:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148210">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده: ما با دیدی روشن و تمرکز کامل در کنار همکاران خود در سازمان‌های مختلف دولتی ایالات متحده، همچنین با تمامی شرکای عضو شورای همکاری خلیج فارس، و همچنین شرکت‌های بیمه و حمل‌ونقل، برای افزایش حجم تردد از تنگه…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148210" target="_blank">📅 16:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148209">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده: ما با دیدی روشن و تمرکز کامل در کنار همکاران خود در سازمان‌های مختلف دولتی ایالات متحده، همچنین با تمامی شرکای عضو شورای همکاری خلیج فارس، و همچنین شرکت‌های بیمه و حمل‌ونقل، برای افزایش حجم تردد از تنگه هرمز همکاری می‌کنیم.
🔴
این تلاش‌ها نتیجه‌بخش بوده است. حجم نفت خام، بار و گاز طبیعی مایع در دو هفته گذشته، بیشتر از هر زمان دیگری در شش ماه گذشته بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148209" target="_blank">📅 16:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148208">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ژنرال برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (CENTCOM):
نیروهای CENTCOM در ماه‌های اخیر، انتقال بیش از یک میلیارد بشکه نفت خام از خلیج فارس از طریق تنگه هرمز را پشتیبانی کرده‌اند
🔴
ما به این دستاورد مهم دست یافته‌ایم، در حالی که با ارائه حفاظت هماهنگ، به عبور بیش از 2000 کشتی تجاری از این تنگه کمک کرده‌ایم.
🔴
مسیرهای اصلی عبور در این تنگه از مین‌ها پاکسازی شده‌اند. هزاران کشتی از این تنگه عبور کرده‌اند.
🔴
بیش از یک میلیارد بشکه نفت خام از طریق تنگه هرمز از سوی کشورهای هم‌پیمان خلیج فارس صادر شده است، و ایران به دلیل محاصره قاطع ما، هیچ بشکه‌ای صادر نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148208" target="_blank">📅 16:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148207">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a12d9906e4.mp4?token=U6g34qlg2oy5D9Cw1JEsJrGRRVgmYdR470ArD5erq13B_i6aTAt0ZO6NN2J7u3fn1YSBeaaiYF8n7SMNIBtA8ErYYdbFYjYcyig-wGsZyzoG-Ba15DhRPA5zNAHjfQyu-5_462HBwGTqxAogA_1aiFhFu7Nuc7Ik8pIW3aDdVFL99akAMpnXDL_UlamLDyRN84srm-65xFc3EvXd35O-PFRjAONDaNWoBdpJGF8VZBkVD9iJOrGL-rgeMD5RFglQFY9a_3_vJrTtHmBuPu1aYpaGtizV-KydvCqkynKf8oZPhzI4RN0YupjmjXS0DOV4w_UxHwa80R2F588P4lt52A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a12d9906e4.mp4?token=U6g34qlg2oy5D9Cw1JEsJrGRRVgmYdR470ArD5erq13B_i6aTAt0ZO6NN2J7u3fn1YSBeaaiYF8n7SMNIBtA8ErYYdbFYjYcyig-wGsZyzoG-Ba15DhRPA5zNAHjfQyu-5_462HBwGTqxAogA_1aiFhFu7Nuc7Ik8pIW3aDdVFL99akAMpnXDL_UlamLDyRN84srm-65xFc3EvXd35O-PFRjAONDaNWoBdpJGF8VZBkVD9iJOrGL-rgeMD5RFglQFY9a_3_vJrTtHmBuPu1aYpaGtizV-KydvCqkynKf8oZPhzI4RN0YupjmjXS0DOV4w_UxHwa80R2F588P4lt52A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محل وقوع آتش‌سوزی در فرودگاه ریاض
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148207" target="_blank">📅 16:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148206">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
هیمتی: چرخ اقتصاد کشور فعال شده و اوضاع درحال تثبیت شدنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148206" target="_blank">📅 16:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148205">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUMclqIJ_PiN0m-2XoSEKnVK9wiCYjgHlgnWdFGmGbKLdApb0SMQOmtb59H3F8k8gvMITY0fpuO9yChEbE50jWej7aQdKiBUPMr-qYEYbGhbjgxBx1_x3M5zJ5kP4QgeD4cAp8Boz_Yk32DIULOPnlwrhWgb2wceP894Wv4QzITqasW8OuGkvYKIkJDYQ8M1ZwetOfXLRPcr54JfFI6ExGV2OAUt8GDfSXLCyh1Nlt4f0uITVueJ0lgvj-3gw9X_8TyzPZLCse9uc_U239W4OXzJvM73KlkfToxpJ0XDRb9qlv5CKGli_K4-x1IQ04jl6YPBXz64cUSorf_8smh4Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاسبی جدید با نوبت گیری دکتر: ۲۳۰ هزار تومان بده وقت بگیریم!
🔴
نوبت‌گیری پزشک و دندان‌پزشک حالا برای برخی افراد به یک منبع درآمد تبدیل شده است. برخی بابت این خدمات بین ۵۰ تا ۲۳۰ هزار تومان دریافت می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148205" target="_blank">📅 16:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148204">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7383ac988.mp4?token=imv0JY1MPyY0jL7DGyAoBAsOXmYg4naNHs1vDD3HN_G4sxgkL00TutADVi2hTJQzMc0BBkr4yLHfZXZmNrhnjsmScifgxETiFrRdd8iPjO9cFk0QzfWdIThNEPwr7O5v03i_2bOTX1N0VUP8tpkyoEQyyl3Ybs5o-kVM-mr3PJloX4Mw7cz5HK7sqHt79lsNGUyP2jDOoCHqZCgj5RKvbvQ1vXV0NFj1M0yGvB0rkQCmh9cG_L1fIoYJ8IeM7Xo79qtGZy1X8ZW_d_NmV9myWxbXdDfBk8ho_SYfG3eykH8tZxZ5wjp2pjUx99uxx3BqVCWJEPm54XyiH2bhZ5iUQXXjIqKPUIck7MxcB29W_m8brK9tU9SGX1rVFehG62qfQoe3akF-ikgDP7lALsh-ARsg4_QfoBNfTtQzWXgPCRT3GriYefmGJCllvK9t7TllCxMWHZks3cczgjjKYERIOrlAOSVoG510SyjDLp5C4lLvXycokE3_XfE9Kg0fo_OpEnY_If0KekyrKzjS3g8ymwgLNEFEBXEzTx6hhEbNt3W3AHy6aTCdX2p6Znd1GxLVtC9E15q6guKz6mphSk7mY0EngNDfxrkda93ACCkbLLzXE5MdXEq2SGQFfnAxoI2Qi0msrGso2iGwoX4pa5vDRAzxobsJnxNMztWCKjFofa0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7383ac988.mp4?token=imv0JY1MPyY0jL7DGyAoBAsOXmYg4naNHs1vDD3HN_G4sxgkL00TutADVi2hTJQzMc0BBkr4yLHfZXZmNrhnjsmScifgxETiFrRdd8iPjO9cFk0QzfWdIThNEPwr7O5v03i_2bOTX1N0VUP8tpkyoEQyyl3Ybs5o-kVM-mr3PJloX4Mw7cz5HK7sqHt79lsNGUyP2jDOoCHqZCgj5RKvbvQ1vXV0NFj1M0yGvB0rkQCmh9cG_L1fIoYJ8IeM7Xo79qtGZy1X8ZW_d_NmV9myWxbXdDfBk8ho_SYfG3eykH8tZxZ5wjp2pjUx99uxx3BqVCWJEPm54XyiH2bhZ5iUQXXjIqKPUIck7MxcB29W_m8brK9tU9SGX1rVFehG62qfQoe3akF-ikgDP7lALsh-ARsg4_QfoBNfTtQzWXgPCRT3GriYefmGJCllvK9t7TllCxMWHZks3cczgjjKYERIOrlAOSVoG510SyjDLp5C4lLvXycokE3_XfE9Kg0fo_OpEnY_If0KekyrKzjS3g8ymwgLNEFEBXEzTx6hhEbNt3W3AHy6aTCdX2p6Znd1GxLVtC9E15q6guKz6mphSk7mY0EngNDfxrkda93ACCkbLLzXE5MdXEq2SGQFfnAxoI2Qi0msrGso2iGwoX4pa5vDRAzxobsJnxNMztWCKjFofa0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بوریس جانسون: به نظرم این استدلال که روسیه به‌نوعی به‌خاطر استقلال اوکراین چیزی را از دست داده، کاملاً اشتباه است. داشتن یک همسایه آزاد و مرفه چه ضرری برای روسیه دارد؟
🔴
اما درباره اینکه چرا این موضوع مشخصاً برای پوتین اهمیت دارد، پاسخی وجود دارد. پوتین می‌خواهد یک الگوی سیاسی خاص را حفظ کند. او دموکراسی نمی‌خواهد و اوکراین آینده‌ای جایگزین را برای روسیه به نمایش می‌گذارد: کشوری آزاد، مطبوعات آزاد، جامعه‌ای کثرت‌گرا و رسانه‌های آزاد.
🔴
او از این متنفر است. مشکل همین است. تهدید علیه ایدئولوژی او، خودِ اوکراین نیست؛ بلکه اوکراینِ آزاد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148204" target="_blank">📅 16:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148203">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سوئیس کشوری که ۲۰۰سال توهیچ جنگی نبوده و نماد بی طرفیه وضعیت جنگی اعلام میکنه !
🔴
با این اعلام آمادگی برای شرایط اضطراری که اکثر دولت های اروپایی دارن اعلام میکنن به احتمال بالا روسیه قراره علیه ناتو اقدامی انجام بده ‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148203" target="_blank">📅 16:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148202">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbtPhMtXSeHTlWq-zKxijE9bThN2j0qBjeNPb8UmoN3CyT3jLelW1ovq8txGQhhTCtSvy6ejTZlYtQrOp9dEW-SuO-5MD5kaRQ15PVulMCxmDlEDkE19NtPeiM4cGiryXuMMXagZvf3hLZfYRcfAgAzePcc9ZHX-xJemYWjUEJG12M0WSeyRSuamHHdfMkLLGP4qwKt5b7m4CSIFlLpMOqcC0phiMQcvIbjB40I7z2Dcqo_JUwP-9JicTV-kAek1mdPdAHJXAPB4oSIfZ2Bammw8mEg9wzsMh5FbbSPbdP2jt5Z5bK27sC6_bYl0oiQSCimyw0wnnLHkKiY9JcGuwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوئیس کشوری که ۲۰۰سال توهیچ جنگی نبوده و نماد بی طرفیه وضعیت جنگی اعلام میکنه !
🔴
با این اعلام آمادگی برای شرایط اضطراری که اکثر دولت های اروپایی دارن اعلام میکنن به احتمال بالا روسیه قراره علیه ناتو اقدامی انجام بده
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148202" target="_blank">📅 16:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148201">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7509fa857.mp4?token=d2N79xlqjGabSdBWe55etijfVhTdmoLueLs-76zaLxn8SzvS8fIS7rnkW6WasRURb2dcdIoI6Ig5v7WB70U6rqutc3OjZdoPz5svATFTb-cE0hL0mB5u6i76-QJ-N0j82iSUg4IJvZQ3-SgEK9SlKLPF3niLnS5PE_j0i52DsCdK9_PAxABhkzMyI2i9ushDtsXvkIZdDlqmrS3jhB1qonAW5YV0PtAD69ERp43f_I9ectupZ8QI05zStwmupFZ3mrX6XTILXsfzSvlmH5WrqKeGOVqtP4QYfz-9sm6VpeOTAXDD7dbmNWqZCLzx_IQJJNO-XIrdy3842TAgoDSrcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7509fa857.mp4?token=d2N79xlqjGabSdBWe55etijfVhTdmoLueLs-76zaLxn8SzvS8fIS7rnkW6WasRURb2dcdIoI6Ig5v7WB70U6rqutc3OjZdoPz5svATFTb-cE0hL0mB5u6i76-QJ-N0j82iSUg4IJvZQ3-SgEK9SlKLPF3niLnS5PE_j0i52DsCdK9_PAxABhkzMyI2i9ushDtsXvkIZdDlqmrS3jhB1qonAW5YV0PtAD69ERp43f_I9ectupZ8QI05zStwmupFZ3mrX6XTILXsfzSvlmH5WrqKeGOVqtP4QYfz-9sm6VpeOTAXDD7dbmNWqZCLzx_IQJJNO-XIrdy3842TAgoDSrcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ای از فعال شدن سامان‌های پدافند هوایی در ریاض
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/148201" target="_blank">📅 16:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148200">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCrMGti7UBeR0gGBMUeNHvaOhiC0fM4I0ap8JXvAkv1gGN_86aUVhdwVTo3wlV01a0J8lKn0N0mSPFIWSuf66KxCBceXmqBqO7Y6MIQ46tqifCnOWE8WuciN-d-PAT73vr5GxxTvxUiJbxMrj9yvFBtJEP3FmJ1ZA7O9MXWsLCJ7yXOpHq_SHHD8XT9dyXJo_IdXtW-xD88K25XH9kjdIEgZpMMykyCt0ffEcf3TEAO1bH8z7oSBym7JaQNKuIVQtI0z9eSiDLyGS-ZsDa36Al90271gZRwTNqjFb-xQ0eNOLI3u834Y68_UspcwmjZ8UeerTxmPU73yRYcvWcMwkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواشناسی: شدت بارش باران و برف در مهر و آبان ماه به حدی شدید خواهد بود که در اکثر استانهای کشور احتمال سیل و کولاک وجود داره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148200" target="_blank">📅 15:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148196">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e1hG8GTyvS1mVo2cWCLA05I9I1EHLf2EIYu87cExTLtwddmz_7ew06PDwOUVxPxElfmkwgEwlrYmy_VkRJxQpMRJZp0KbtD-kAGmAJol6I3chG9qlhF2OuCHdAKQoZ_G_dyXXx_nkojRKlPtswlMSsPeZswIFmVZjRDllWR79xDw5YHQajOVb-1ED-MG5h7-p8xgd82sVUry4pX_Q2CAAG8koiMFd2h5ZMbtJSlRvm-WsRGP0W8CjA6q3azqBnFQzLsjBTJc7Yk55wOUUl8P65jbO1ZQZKZjQP1GPKHSqnZXoHoOEJb3zuNULkSGE_Ogek0pEmKuiQbGkxGTeYza8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DaZFGAvNc6syV0NvGzDDT_G7i7a4Sjt1Lpjl6EN5KDPhumHftkPtJEOSBI8N0NDk6uWv3JSziLSrnYIrSC7OK6fLef5I1qnEC9pzDXnOY7K4S3pK3C69RVPHacc6VWQSkziYMTYLNhtCK3AAAjcp_3ZznsykmLExnBHXiyZuE1IW8p4CDOTlvr6GenC_l_Kq5HQCDHmkI13X8ZJvcME6V9ssiVDEQt3byrPBUqLAWwMrrsJ-9IFnBL6VQQJe87LGxArCY8vxEDyUBnvIMgkKlsj_LxoL_y-QqkPpoy_rGVwTbCBDneovei1GQ0g4i9SDwpUQr1RBYl0oGWrm_Eatbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vv_6rJ_4Euwhgbbu7vtq7ev5etbgoNrjOYyW4PZaCD0CurGNZuBbidw607GZ0fL0IGl-rrGLG31FVe70bMWUoiMDSkySknYlVEojEOmx0IgV7QtsV2-Kqy6ZlgzNy8ihe7P25nXr0izmOVL_DbGahrOnTxuyEevQYUAPIHK3EuMflhaRtv2NVC6TONXzQ041aK_lm-j5NcGGZM7ebfXMGNvfd5agB15cj65NSaotxeSrFumsr2ULjV-DRetyX6P839gTIrE9kHJjP9qliUGY1iIgRdhJm7bq2mtasPJkBBCbt3wskrqJn_I_AVHy_YWCzqVl1qaXvKNLw0HhMFTWpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C_PF1tr5gGNy9_L0_0uvH_03MGYIOByySrTDcNDsTPOkUpMriDKHZkHS9Md3QPzpmmjJvX5v7Qyk_76PdWnH1rG2CyOCDtd62K7QTwBZIwjWSGTMQMSVoNgsyoiW67gM6NekS7ezJhHmYt1AnFtssj_oRrVMbKxda6R1B5aTGvxrBWaVl7FAhJHqRbvIz1L85VUIP1jbu0RmOgbealNj3JlrB-d5FbFVhziJY_yVFG5nqg1ISJ6MtQdZWQlYB8NicBzyupEEjSGMuoGlYqnG4CN0tq0W6festfyS0S-_3IgkTdZ0yDxMikz9AXXJYNAIT7lSKBTVfqTaZ2sGtJyahw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جزیره فارو اعلام کرده که مهاجر می‌پذیره.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/148196" target="_blank">📅 15:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148194">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/243abf4097.mp4?token=Fy3uKiLQ_7snVSCnoL1FWm9t588vEkwQK7VO_SkPRKVzTZv56xMzKppliD450LLGokQNYXzh1Z-2oHGIJ-m62NkXWojaKkUgXwb9yx_PMIOewQ-haoltkcb8TQu39Q6w6jCyMQMp2vPZqoX3zvCVSJgYnCZzze7CBurMhcnq9mxzn1q-zGSkkJYKYmJ45W5CTo0Z9heZKSKB1lAuFihTRodN2YpMjbsHb8EPp9e1dRO_5u8TtfHoLIZ46T9qdvNbX94Vzu_WFIGshCxLqceZeKhOH94xIlfwXMdnWePIQrF2wxTLKoy0yKirYUX09_LVa8r5rzeX9Vg3GAxQNgxO9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/243abf4097.mp4?token=Fy3uKiLQ_7snVSCnoL1FWm9t588vEkwQK7VO_SkPRKVzTZv56xMzKppliD450LLGokQNYXzh1Z-2oHGIJ-m62NkXWojaKkUgXwb9yx_PMIOewQ-haoltkcb8TQu39Q6w6jCyMQMp2vPZqoX3zvCVSJgYnCZzze7CBurMhcnq9mxzn1q-zGSkkJYKYmJ45W5CTo0Z9heZKSKB1lAuFihTRodN2YpMjbsHb8EPp9e1dRO_5u8TtfHoLIZ46T9qdvNbX94Vzu_WFIGshCxLqceZeKhOH94xIlfwXMdnWePIQrF2wxTLKoy0yKirYUX09_LVa8r5rzeX9Vg3GAxQNgxO9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قار قار کردن و توهین عده‌ای به پزشکیان در دورهمی دیروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148194" target="_blank">📅 15:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148193">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
پوتین: رهبران اروپایی در روز های گذشته به صورت آشکار اعلام کردند در حال آماده‌سازی برای جنگ قریب‌الوقوع با روسیه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148193" target="_blank">📅 15:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148192">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
یاشار سلطانی: کشور صاحاب نداره! رئیس جمهور و رئیس مجلس یه توافق رو انجام دادن اما عده ای خودسر موشک شلیک کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148192" target="_blank">📅 15:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148191">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
یاشار سلطانی: کشور صاحاب نداره! رئیس جمهور و رئیس مجلس یه توافق رو انجام دادن اما عده ای خودسر موشک شلیک کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148191" target="_blank">📅 15:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148190">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
مکرون: خواهان بازگشایی تنگه هرمز از طریق دیپلماسی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148190" target="_blank">📅 15:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148189">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
واردات خودرو مدل ۲۰۲۳ آزاد شد
🔴
تا پیش از این، تنها خودروهای مدل ۲۰۲۱ و ۲۰۲۲ در این رویه امکان ثبت سفارش داشتند، اما مدل‌های ۲۰۲۳ نیز اکنون به این فهرست اضافه شده‌اند. جزئیات شرایط جدید و الزامات قانونی، همچنان اهمیت زیادی برای متقاضیان دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148189" target="_blank">📅 15:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148186">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRoKtP2NRsiNfezbWbFMZqlakSAgTkR3Hrjq9jMQn8Rmp4ofITVJN-7pG7ROq7WWlZ7DeaxMdR_qsWN_J6QLZAFWUAgQXhelgZOmg56lBmnZNcpZ3ktMoWBhUkfCWFZcr_gq4O4GkRcwT6QJL96AfP001DaYsgP6C4uzKcqv75mP4nGwz-aOIq3Roc9DoVPuejOwe4jqEJvsUPFFpkMM4v40usFv2OztLKr-4Mi-W1-wof75GqcvaRjFslcc7BnSJKdKwxUilhhrCFi4jHSAO_fCMA-kNfad5xgcX9-38Jbmc0KSKmYe0gHPXrEE9qYwCRYHR5uJEaCDD2noFdqFtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a4c429f9.mp4?token=Qo0HoWk0gIZj6VVfu3dxvW8sYiOXPCG4vyFL7DX01tFIjgC7RfbvtV0KrPZXTwkg5JWE2mPK5b2OEkd_uqacX3bnx04QnmfxK-Q_TzB9rKHd6WB6sxPRBv3hhb3YlPAI5qzwaAAm_wijmk_Z1gcR1FgVrfYbI6rP4G8aFvVPsj2Sk2pjIdKF8xW85QUHUM60bu3vsoAVcgSEDZ2ttaI6EmbcGwXHrlCBF54nhVOpMQRAZ3ExuGlKgep4daqUkAVwUXsrwW5wz7RfXupf-ukxtULE_ywc2EJKLjycXEl64MpTkuhoHlqReFBstBiwggc8cvmVr8tKF7PxKIPbl7e25Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a4c429f9.mp4?token=Qo0HoWk0gIZj6VVfu3dxvW8sYiOXPCG4vyFL7DX01tFIjgC7RfbvtV0KrPZXTwkg5JWE2mPK5b2OEkd_uqacX3bnx04QnmfxK-Q_TzB9rKHd6WB6sxPRBv3hhb3YlPAI5qzwaAAm_wijmk_Z1gcR1FgVrfYbI6rP4G8aFvVPsj2Sk2pjIdKF8xW85QUHUM60bu3vsoAVcgSEDZ2ttaI6EmbcGwXHrlCBF54nhVOpMQRAZ3ExuGlKgep4daqUkAVwUXsrwW5wz7RfXupf-ukxtULE_ywc2EJKLjycXEl64MpTkuhoHlqReFBstBiwggc8cvmVr8tKF7PxKIPbl7e25Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر دیگر از انبار ذخیره سوخت در فرودگاه بین‌المللی شاه خالد در ریاض، عربستان سعودی که در حال سوختن است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148186" target="_blank">📅 15:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148185">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bd3300290.mp4?token=UlsiubB_sfrlVEoJ0TCRNTsvJ2zb3TtjPA7DgGFm5rs-pm49U9KYHIENAa7_1Q85jzp10LXLeBvKqB0yVpKS6T67g_mmIPE2jqecYPiPkBJQqWwR9mucPFJZtSO8rnICm8DH4CO08X9phBh9zVURjqzs8pNnkYb2ugs0V7Rw5YS_CiwEwccQCPRPKXg1pUpDh18pA6az2oSdUgoFP_K0Esc8tdwGryDTpmmqZopjHRbth9Xrp6_-XeMgyNyVgjjtS3zH_4ZfFn5CAgQ7xJ5uXutl8vpyLfTjNe0cPl-g_XCTIjK46Xpkxbot3lNFIKUfKVWTmlQhrvtPeeVgHXgY_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bd3300290.mp4?token=UlsiubB_sfrlVEoJ0TCRNTsvJ2zb3TtjPA7DgGFm5rs-pm49U9KYHIENAa7_1Q85jzp10LXLeBvKqB0yVpKS6T67g_mmIPE2jqecYPiPkBJQqWwR9mucPFJZtSO8rnICm8DH4CO08X9phBh9zVURjqzs8pNnkYb2ugs0V7Rw5YS_CiwEwccQCPRPKXg1pUpDh18pA6az2oSdUgoFP_K0Esc8tdwGryDTpmmqZopjHRbth9Xrp6_-XeMgyNyVgjjtS3zH_4ZfFn5CAgQ7xJ5uXutl8vpyLfTjNe0cPl-g_XCTIjK46Xpkxbot3lNFIKUfKVWTmlQhrvtPeeVgHXgY_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زین واکر بازیگر ایرانی هالیوود با انتشار این ویدیو از جمهوری اسلامی حمایت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148185" target="_blank">📅 15:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148184">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
امام جمعه دزفول: دختری که تا پاسی از شب در کافی‌شاپ‌ها و فروشگاه‌ها حضور دارد، نه فرزند خوب نه مادر مناسب و نه همسر موفقی خواهد بود.
🔴
پ.ن: این یکیو راست میگن
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148184" target="_blank">📅 15:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148183">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
معاون پزشکیان: شرایط اقتصادی خوب نیست؛ مجبوریم پول چاپ کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148183" target="_blank">📅 15:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148182">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
دود از شهر ریاض در عربستان سعودی به هوا برده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148182" target="_blank">📅 14:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148181">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d0c461c6.mp4?token=A6MJvsN1rHvHz4pZnRirGlmD26Qmso6BF2CHpx0Un3zuolErUoMKccQYja88w6yqdk3Lu2-mxAqqMfk_4MWoU689eFiKCwGcPW70Ml5FT_YzdvFqes2AEb_4Fj93Ei8dAJWPtgaxTfFyE940e6GzM-JHgXi8iuN6fGS4A36YD6Q77_nyNqaDjh5rcE9vpbBcYHOiLMv7oeMnbYAHKjm_JxaH7v1f9BwlAnhDsULLta3I_No7iqg9F7Rjv7QcrusM2wcKbRgSuFdJiOrelD026s_NGa_FKd_rHneU-5goxo4u_m73TV1uR7lev1LWm4DT1vVCnFX_3FmRXdbc9TMVzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d0c461c6.mp4?token=A6MJvsN1rHvHz4pZnRirGlmD26Qmso6BF2CHpx0Un3zuolErUoMKccQYja88w6yqdk3Lu2-mxAqqMfk_4MWoU689eFiKCwGcPW70Ml5FT_YzdvFqes2AEb_4Fj93Ei8dAJWPtgaxTfFyE940e6GzM-JHgXi8iuN6fGS4A36YD6Q77_nyNqaDjh5rcE9vpbBcYHOiLMv7oeMnbYAHKjm_JxaH7v1f9BwlAnhDsULLta3I_No7iqg9F7Rjv7QcrusM2wcKbRgSuFdJiOrelD026s_NGa_FKd_rHneU-5goxo4u_m73TV1uR7lev1LWm4DT1vVCnFX_3FmRXdbc9TMVzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دود از شهر ریاض در عربستان سعودی به هوا برده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148181" target="_blank">📅 14:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148180">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
مکرون دیروز  صبح تمام سران سیاسی فرانسه (حتی احزاب مخالف) را به جلسه‌ای محرمانه دعوت کرده بود. موضوع جلسه امنیت اروپا، احتمال گسترش جنگ در اروپا و خاورمیانه بوده است. جلساتی مشابه در آلمان و لهستان هم برگزار شده بود. گویا احتمال وقوع جنگ بین کشورهای اروپای…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148180" target="_blank">📅 14:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148179">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
رسانه‌های عربی: پروازهای فرودگاه ملک خالد ریاض پس‌از اصابت پهپاد یمنی متوقف شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148179" target="_blank">📅 14:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148178">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b27b34a2bb.mp4?token=jtcvM2mzGDRdnjDXCk7atAdTTZhGv6XoUB4gLB6aqerniI3jr0H_f5lSSZRDmS3JFTG9eQ5daZ2kiaUhMejPeveWNbgXlTiPe0KOaasfpzF3EVCXdaqD9PYYt78BmNApj47HzNxegVSU_HbgtFTqub3qd2m-xyCMw5WYrIfufXsgCcUaMeMSW5_R0NRFiJfOi2RN5Bhe8ADpiuq2PXu9sajwc0fvNdZ8uwq9XMcjzzN_-bTv13KCmZInrOrDQOD1w3z2zdMeZWP9bqSmz17WGXb1fP3MbmPgzbPUoDoZslb6WBBnPHKBUIzSuMa77EQnFiTPd55rlrSKwqvr7XUIlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b27b34a2bb.mp4?token=jtcvM2mzGDRdnjDXCk7atAdTTZhGv6XoUB4gLB6aqerniI3jr0H_f5lSSZRDmS3JFTG9eQ5daZ2kiaUhMejPeveWNbgXlTiPe0KOaasfpzF3EVCXdaqD9PYYt78BmNApj47HzNxegVSU_HbgtFTqub3qd2m-xyCMw5WYrIfufXsgCcUaMeMSW5_R0NRFiJfOi2RN5Bhe8ADpiuq2PXu9sajwc0fvNdZ8uwq9XMcjzzN_-bTv13KCmZInrOrDQOD1w3z2zdMeZWP9bqSmz17WGXb1fP3MbmPgzbPUoDoZslb6WBBnPHKBUIzSuMa77EQnFiTPd55rlrSKwqvr7XUIlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امام جمعه دزفول: دختری که تا پاسی از شب در کافه‌ها وقت می‌گذراند نه می‌تواند مادر خوبی باشد و نه همسر خوبی
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148178" target="_blank">📅 14:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148177">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrVuY1Xjd4mfybnWhG22T91jzeDoRLjt_hoxvCJy9s0HWkwHBm6MQLcpBhEKz3XHlssodf0XGWK7AL1_6gmCs5OCWZCikt8LmbsCRV1sYRTDAr2lraaXF_O8d_AncoYTJTjIws0zX1ITBcE_-Y3pZUyDbBcSNqIWGEa4MD08eRMCMdUBIPTOc1ggoU53MOKh8oFUPss5YYk9YHfoZFcXiFx3dasITBN1HUrSF58eQxLMHE-jXywzgb0BU5K1bXR3AG-p1YOAqXjs7-qR9oexaDnkkXsfcKE0hVq4lh4OlhkXKSaQwpvLVQH2jbWSPlvbX02c0WPuSDKj8kFvm1_BXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرودگاه‌های عربستان سعودی با مشکلاتی روبرو هستند...
🔴
تقریباً ۹ فروند هواپیمای مسافربری قادر به فرود در فرودگاه ملک خالد در پایتخت عربستان، ریاض، نیستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148177" target="_blank">📅 14:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148176">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
رویترز: شعله‌های آتش و ستون بزرگی از دود سیاه در نزدیکی فرودگاه بین‌المللی ملک خالد در ریاض مشاهده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148176" target="_blank">📅 14:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148175">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
وزیر امور خارجه پاکستان به همتای ایرانی خود:ما بر لزوم تضمین عبور ایمن کشتی‌ها تأکید می‌کنیم، زیرا این امر به نفع زنجیره‌های تأمین انرژی جهانی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148175" target="_blank">📅 14:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148174">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bcf4947eb.mp4?token=ZwxMAby-MmPSMJ7jdoyxFh2cIyFLsYGEctohTUD_sbhCetyYNYiDKN3ns8JI04BLiNfbZvBbyLIwIoJQeOwmtiRuy1NgUdJT1KWCP5x8MU9UkI2p3yveHF4lms6SlzzSgzCnxIYbRjJ8oLgtsX_bhX3SDjQj7qZsF4LP-bMD89tOpg5ULQFjAih8N57T9x9SgxzNU0O-obnG-PJ4b7wszD0MOjSJLhM3KWJCGL8_fICoHrzeJQbzdCZOuJtG9R0D6PK6M4Em-fXPtVr9cy2Mf1FW86gydyt9go9GUsUBCBewgDS6WEy2SVYdluqDDXeCCwqyG3_42leJm0Trnmg1WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bcf4947eb.mp4?token=ZwxMAby-MmPSMJ7jdoyxFh2cIyFLsYGEctohTUD_sbhCetyYNYiDKN3ns8JI04BLiNfbZvBbyLIwIoJQeOwmtiRuy1NgUdJT1KWCP5x8MU9UkI2p3yveHF4lms6SlzzSgzCnxIYbRjJ8oLgtsX_bhX3SDjQj7qZsF4LP-bMD89tOpg5ULQFjAih8N57T9x9SgxzNU0O-obnG-PJ4b7wszD0MOjSJLhM3KWJCGL8_fICoHrzeJQbzdCZOuJtG9R0D6PK6M4Em-fXPtVr9cy2Mf1FW86gydyt9go9GUsUBCBewgDS6WEy2SVYdluqDDXeCCwqyG3_42leJm0Trnmg1WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو صدا و سیما مجریا‌ با تراکتور اومدن وسط برنامه میگن با همین میخواییم اسرائیل رو شخم بزنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/148174" target="_blank">📅 13:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148173">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وزارت دفاع روسیه:«ما یک نفتکش در بندر اودسا و یک کشتی باری در دریای سیاه را که برای پشتیبانی از نیروهای مسلح اوکراین مورد استفاده قرار می‌گرفتند، هدف قرار دادیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148173" target="_blank">📅 13:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148172">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
مذاکرات پکن و آمریکا در حوزه انرژی /  بازگشت چین به بازار LNG در بسته ۳۰ میلیارد دلاری
🔴
آمریکا و چین برای کاهش یا حذف تعرفه ۱۵ درصدی پکن بر گاز طبیعی مایع آمریکا مذاکره می‌کنند؛ توافقی که می‌تواند هم‌زمان با سفر رئیس‌جمهور چین به واشنگتن و در قالب بسته گسترده‌تری از قرارداد‌های انرژی و کشاورزی اعلام شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148172" target="_blank">📅 13:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148171">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJVDjX9lSRjyYDOE1gpGcL0MicneaKaPrCccSSaopV5LH_rzJctxirmjxQp_M7drEd3LobgwdbuQGI-lRPDFH_Q_-9LNsaHaVerzmkYmrsfYw1m7B1b5QRQiMNNu3_vPNg_ZabPoKs1p4o9U7Nx1PgJBOEQrcjNfiZxTO82MCbuEEpkkIepOSkoLfZbXMqPO3U2jOOApga_0ZPJwcfI1XspyILLhl8tfPmPp0EZiDThxXFhGTv5rtVbjIZ_zbjQusVEm-WADxLtvdHcGVxQelXMqYRM4zjvhbNKL8_K2qxYRug1fzfQtrASCGOZZpoW3B1tUjaMu0z6LUxORVGL1aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاسخ ایران به پیشنهاد جدید آمریکا احتمالا منفی است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148171" target="_blank">📅 13:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148170">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
سخنگوی ناتو: از اعلام توافق بین ایالات متحده، گرینلند و دانمارک استقبال می‌کنیم. این توافق، امنیت و ثبات در اقیانوس اطلس شمالی را تقویت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148170" target="_blank">📅 13:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148169">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ان بی‌سی: روبیو، وزیر خارجه آمریکا برخلاف ونس، از قرار گرفتن در کانون توجهات درباره جنگ نامحبوب ایران اجتناب کرده؛ این فاصله ممکن است از نظر سیاسی به سود او باشد
🔴
روبیو در تمام مدت این جنگ، یک «دست پنهان» بوده؛ او به تدوین راهبرد دولت ترامپ کمک کرده
🔴
به گفته افراد نزدیک به وی، نامزدی احتمالی او برای ریاست‌جمهوری می‌تواند روی میز باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/148169" target="_blank">📅 13:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148168">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
سفیر آمریکا در سازمان ملل: محور سخنرانی ترامپ در نشست سالانه مجمع عمومی سازمان ملل در هفته آینده، ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/148168" target="_blank">📅 13:14 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

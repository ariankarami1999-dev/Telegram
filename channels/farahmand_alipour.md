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
<img src="https://cdn4.telesco.pe/file/fbIiqgv3pg1s4j9uWSr-UFKnstlmQ3nlvj6AUWjMygjYexED5GJwlY6nRr5in-gFmaFyBZUaJyRAAjRCcHLVcrA_aw-Uk0iRMNGNK-GRYvMKxb7zk8z6yCmiWldVHbAQZZgEPYX7DZ2Vk4Q1g4tMYYAJaKrXah1EDNHIiZB7EJ2NJZyWI1LlcBdfF6vEvPR-howDOMlHMRgYNNn9x_IVLlF-J_fPqj5zZBZjdVuBpLNZFTJ4U4HMbdUmb3CK_qK0UQwCz43dSktXKePaS_G-e7vXZLCCJxJP0MNQnvFQXqa7gqevXKXM3CnQWmKwfaowB-knrD8BA4RhQSp_tJcBkA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 10:57:27</div>
<hr>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rie3AQP4dmNq1HVw1llkQzRxdNmR1Y3dFfJw0LD_2_mZR7Uenv1IHplnKxMPkzHBUtdCDzC_PJ6xoeZ_b5keL8lyEqfOAqFtc06P4WNufx8Hd9oHq9IOHNOIL8ALlixE_kyvXX4pmRSsoUuJSvkAp9FkZkm0UDoETCcp3x8fOrGNgRSE6ZaMcrQuhZXhFexJrYXkarR6pzvm0O5NH0KNaJRheqhC2oF6z2XCgJV7UDX2eMeHXFho4EK1JmOa0lUxqvBZVoVDL3lJmDkae46WxQz3faYY1FaoiBXzLntBscRAJrGBqGFp2eJnrNTmyyinDldq6RF4D4NUBaS_8dYVPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_MYiELFmaCuRW4K5t0iXHsssd2nPiMseMwen1dgWTGx0m971qi-AcVBeISstXpS2AyhnVfeeXj43LZfC1a-n6iEhO1pLR5J8AjQeVBRIDzE0hoTO035zhwm40ORszerLXQ3R1EB7bdLoaPRi7z1gEHLYz1yPvQOeylFMUoWTsNdB-Wyj9WO6Lh_cKCtDskntTuSWGzhc64DTBaWW5NU6x0JofnTmwFHfCG8oI5v8NHEnW_23l3seiHCmfb9pwqZPsieW01qN7cWJ0SZVmNsxn58HBGoo7_XYd6Evpn52kw2uv84qYS14b1-kwxyfc2KIq2ogzrCXocJdHYsfBoUgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xg-Q3oMjNfneqGUWi4Z_1_MstfPfS4pGtLE4XIZUqBTrmlAEex5yamJ31WsLEbXUrJ-nvHulM5RyQayp6mY86zJcCG1upFCSb73SL8oMMmL_gudu__Yp3pqb3B-yyyfSCmrvmyP7wh-qerG7BMWcpRj2OHKl5Bl4g4bsa4IWs-nctM8EAgN2_DzbmkRtxe55kTQHaNeGyFet8H4R_GH-ka5iV0CRe3tuFntWAMvdDR5i1Ye3vByc9Wpgy4pUzgAuQbvLIIIZLZLOLofizDGc1LpDMGi1iOGo4m_gAvYvCBrrG8cOKcwv39kS_9hwyAh1KTughUDl2IpdIsjU-XK8cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9xy71n0rwES08BgRnS5CI06Imk1wO2CPfDhIZIuzvnWkQ1nXvfFgVnD_JqtWO_iB1WvzvKHQkDqSfEndC8xyRQoTr0qqe2E6XaP9tyHScVso9z0XOrY32wmeZ0iL9hyx0ZJJcAtd-hLXEmsifIKBIWnT5LECtqfuVM-7O-6qAfVbqFEaiPYgrnI2A0the7NodDcboTKWWy-l6PA2gDiTp1kxhBmPYpIeMeJQuDMpUmCKUZta3wKeQL1omHIgHcvDG4uvDkL6FhhucJjUwAX4cvbP5Fn-jPt-Yi4zG9Yf3MbB5B-3jhVWYD2rEgA9tdhbS3w4fnijPPxnOjJRYJKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqTv0tDDRPxZzYOo2L4sj8WYppog81ssV4xXPe_12FSqUkPM1O27C9npMUs0vvWAwj3JEBwSppM3pAnpYg3n4Vqe3Yb3kRmJysU9z_LyZMHDvZIehl9s4xA5xdeN_ZO9hcTVIMRhyS1r4qRvxZuCX_pxBISpXeHuM6L6Y-Jgq_ZYbIVxiSWTSrsFfE9t7OEyK59XrOTcY65NIsz42mgHwfLWLOlVGHzoiR5aijkl6fjchtqgEJt6GFDiXt_oAzC_NWN7GhBzBgV2LBny4T-n8vnKXYjEKHtbognBjzL35n9cuPebscTz856YcRk06wMgfvU_LzPk2P6CYeRFHZHKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZWXiG9Pm2zdfjszEwuYn5iU5V_EP7mO1aAFznmjNvBb4vK53U9R-oc_LyVwBBrHhHuR-sBwCy_jc0Nea476C6z8iHttZJMPGlvQDHTrIYkiCVt8S2P-rH09MTF1o4g2cIp_jW7QQ5Vq0oKEl-WaohwfhDfBBVgP1uPt5CvybKOE3aKnxLp7jEBWCjbfLFsUoHaxeC5rgQ9eNgdhv8wSn6CO7_muNTtjWMvoU5HWziOdqHYqVW_g34aNwrjnYbmYRYGEoaLV4e-cpxhzDxThA1KlocF6jW-Rle3XzG_ji0cCRQd4_grYiy2z9D3A7SqjvHvn3ptLnRPiI_30yogJQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eo_IqMKFX8OgRbLEyw8rO2mEHMGLx_WmMsGQDl1n5_3kN3eSCTlCD11f1NHr7rnYvypYaGN1AXY05fm56NvWd9FF5Q-49tQZLNAnxGKdOArZKot470ndZRggLwjgbOmeEom13tvgoCpOC6eqMoPNrLYoPrijUXuqcUdC8jo1RMpKR_YDklvUL7PlFaxj0_QsnMKXaaieAk-juF6zrsUhy24-t9KH0iWUrPnGtQ5uIuXBX1B9iFrtbAqaqULCopqrLPROUPcbSSqaq4EoapGn8D2s4_Hd2ZXbzNYR8C7y67bUAF3aysWc_-uNoGDmPO-1MlT9Zbpko4JymG84l7IQQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VD9ZlWx9cVj_jEsUeEeF9DP-nqMt96Gk8HGEqi6InLVrmhwyynXOv_qwSC-_FVZpUnpmUo-ZPu1FAn-AKLFayMq8iKJZ5Cmc83tEyHdKuEkUNCFLBi96XJw08YimuBBP1jtuuqLIsdUO3ZrxfyL4Mi9lk5aMG4iHq8lci_vhP8LXmdUinvQ0XCcplh8IBVVbfAUGOKKSZkVHi5EWJ_EpzBR2M3uPk5Mzt9vpxumB9kwiLfPL9Di6Fy42sBQlR4IZzSmpXGtD9YkKePEUYXmnQmVrhcOBUISAk75ruzcbcMhrTgI9kIIACX6WmfzOvm2b8QZsObCSyGA0qw5ENngmPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دولت ایتالیا آزادی رفت و آمد هوایی و دریایی
بین ایتالیا و اسپانیا رو به طور موقت لغو کرد!
این بدین معناست که تا اطلاع ثانوی،
پروازهایی که از اسپانیا به مقصد ایتالیا است،
دولت ایتالیا مسافران آن را کنترل خواهد کرد.
اقدام دولت راستگرای خانم ملونی،
فشار بر دولت چپگرای اسپانیا را افزایش می‌دهد.
دولت پدرو سانچز هم اکنون نیز دارای کمترین حمایت شده و پیش‌بینی‌ها حکایت از آن دارند که در انتخابات سال آینده از قدرت کنار خواهد رفت
گرچه برخی از راستگرایان امیدوارند با انجام انتخابات زودهنگام، انتقال قدرت سریعتر انجام شود.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=KdJGnGjofmO1YK1ZR9o8o7Me8-W-cqhr90nL1hHKsLlpu_Z0ek5Y9adT7NdSfnxGeFPHzqz7AJuNgvuFxxZpMLYL9JVOG8wIFQVMjlzmI4v3G55Ez55UvfnlU2Pa9STmiCWfoGfGhzvAqdorx5UVU8t8BB1YO89wUEBJ9LA1EMFSHG0yQpFmsJKNdz3Vb8aohbXZimAXrpDxPfRshEFnKWDFFfWesH8trdnywMqKB0kI7pICPoq4BG7AJZITFVlpIRd7Mzat0sgnUZpmam6WBX1uTFeu9rYqUjYATCoMLXcG3ErrSCkzp28HRmJVPIWWCQHQztl54q3IuRSdgz8qMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=KdJGnGjofmO1YK1ZR9o8o7Me8-W-cqhr90nL1hHKsLlpu_Z0ek5Y9adT7NdSfnxGeFPHzqz7AJuNgvuFxxZpMLYL9JVOG8wIFQVMjlzmI4v3G55Ez55UvfnlU2Pa9STmiCWfoGfGhzvAqdorx5UVU8t8BB1YO89wUEBJ9LA1EMFSHG0yQpFmsJKNdz3Vb8aohbXZimAXrpDxPfRshEFnKWDFFfWesH8trdnywMqKB0kI7pICPoq4BG7AJZITFVlpIRd7Mzat0sgnUZpmam6WBX1uTFeu9rYqUjYATCoMLXcG3ErrSCkzp28HRmJVPIWWCQHQztl54q3IuRSdgz8qMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUBX3Qdqcbnf53lQGgTXV6dCFAb2qOwnIby2Q4oHGqZ7yEML1YV9gNozBzoiax9MY_dmkiPhtsiHevAIvLSWIzYFgZsP6fwjVCvsZ213RFFZWNOkRlrhsU5h6zQ8IQZgtPpD5bgmOHqQWxOlYYLM26WaPV-YJKZKEB22U72w4fa6tFsDLuFsVeZJPSJaRQEMvrkF6lB6CYCsDYaMybIhKyDBBSpegFNMxBtmIOe-H0SRu2FWZxzhdHPCw08tS6sWPf0q2wqTBmHXOhf4HaOC64CqC0-UhbQ66Z-vExq4HjJmkR9EwimULFg2EhzMJis8fyglBX-PPP7KvytCZgilLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-kOBSioRoYtMGTqcY-IBM8rWqdEzKzh872WkLXQ7m2MVmDG0U1JmkJpKriqo8REoTKUNlihb7IYSP6rI_SR3y6fYWu1KI_OUsZEo13y-l2-dqHYueY2p7EkcgXN2KUd6nGlLbRgXnIlXA4XnFxMIJSX9r9qNFadSzzi428XVl2eC8fSGLyesYa-Y5PFzW7nKPxvqKAvUYZzNzR0O_wiuytBcMkUUNOYDkrJTyHHNxIafbXoVldFCQmVDuLrsiSrA2GyyjwFfUnQa-sms6kaPpScnPH15M8Icp2n-zDCvJ1-JC5XECjVMKoSzohZY79RnLASckoa5v3_2jiV4y8XbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgINaJIP1ZyAOPM3iTC1tLCFUVXkU_UlrWgn_cZDyZL7_JzY9rS7m-fg5YDxm1gqhfnEGab7we05E5HKJOTVQj-Lopr8P20f2JK8NwhoPLa3F2a9aZ5tCG1ONZNmLSzuIriy0ZK2KaBOJellWmjkKPx3_rldj7d0HM2crhcZxQEiloDan9ws0bFigfGZ8jDGtwJg_PKqvF-tcMuIkXaFbHUEPkiDTsh27Q6AFlJ8AFkNGs7Srm3NIs6CH77cc5VxBVuqWr58DSeI42rac_feM9Qu6IOkF7nUJlTVDYLJ5jIGq7n4kJe9MJMzFBQG0zNaSDPmHlvUnOCmrYXykYs01w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lm_fHN1nHjyvkaB-7tPOtmZceBjRoGHp3L4iX-tJZ5cMg2Kff5fgtMs1QiL0miXEGA9ycrJI9fFPON0ejXoAQBYMmlAMGA3JkN35ATa9LLfUljVrVdJ0jKI4ktTYju9lIYTzE-VodFMmxet1tBnwKkn7m9r0IE2pqysKnN6kyWjrfmqRhLNeC_7KHKAmQWoFc5CCqnSlPiRgZ2Z6s7YMx5v7eaTR2b6sNVde_oGhI4z5f-w8kpFIe-CCE1-CrsMY8139jkzD5xAbJfWz6_reCBBTdJyeN_oOFHsO_2vF0IvoUhzMWf09AWMlg-Jbw8yF3Pz2tygDA7aU7NRQt9Y2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMmKCFhB9pYWn_a6jsuz822pq2sb8jcKBrKDGiGghJmReZMhT6FLLr_8jISUrhdI1prpkTvo5aYakNG1yFYeV66GhsQCyYn_3McQC0AY1hP0v-icUhaE71oT_yLpYEnmGfOvOu-xSODoJvmBfSOuBW2U_IncU43uWAlJPTe5s-g6x5ixm9fpPvhpBuOMFmGEKD0Cag6FHpnDd2bO965spJy5MPssoYyXE6CN0vEINXAkSE_-AVgJv3EeMJymo2IejOg5cc4HhyudBc6ikzDaaGFLjJr1lOsLr7ecBS9IKBfl-r_WAi0ZyczU2Y1DeXIvWPvQsmyTqqRJexYhCTyPxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ss5LsYsSu1bTIb2UxXMd3N9qkH5zx22In_lszP513GGWkQaaaJJZ_Fmym-A_BHX0srIwHm8db2shPuvTVgvLfJCZwxokozeRNnSa3toSS8-2P0Knx5_QnSJPdBdcX2XAiZijT_I6G05RcwAqBuWfSyyExSBX5zzwGWYwguXHVRQndZaDynooC6zlo8PLC_xojC5Nk4Buwdpd-8cw__VSYhmvSXlIFGq5X80iocmT-fA4wsgZdoY2PwTZ9iQGnil0Keu1gPFDiLOWwN4Z_kC4DVkwd4js8Cc1ms85wHe1bFcRm9bnM0UvalOKySJyYhKD7CL2rkFmPNEgwkgaSU5Few.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kW3GqkA_yUw4ZJ97Hniq7n8b7VY8gqwn48WozSD7BqYIdsRSSpphKzfvIFc7S46V3dybYUJcpIP41qqDdMol--i6s0PbeA6c1m1WF97JrpaqYRZq2B4nEgvbhhxkfJwkMQAZc1_fMTK3maKAVsM3fxWV_10g8m-f0gPEGz59tOkAaqa67BCaBu79NNqvrFg1yamaWyZDeKSjpb-s2sveUsE4ASK9ML0jwDN5pvHeXaiMxCviYd652yecRdQdIbEjRjI8J4RallO47rsSageC8jzbBDO2Yerb9JzIVSoRYNIsILxSQpO8Cn9AiM1DUn3d26Ev96Ow8iiPCuu0F0Ylxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=DvywSXMJveFCU0s9HQUY13slKabVbqnGx9Kq8_r5k_h4tAPlPBkDPLjx0pflLGu1UBZafNkWMZAaldxItNRihmfHJmvXklDBznuCUFmKurWZJaa4gVD4hR0JCcM9oP6_VE8I_YSFY4leZFpko4fQt0y5M86IksVCmXtHWX1iOXMI6qqDAvKWhj9nOqDCvxW3hHxR-SmxwjVeG6qNVd1sGzI6ipqkLR8RKhESzYai3iAMIl5HfPSIJ-263aj0b3zY4cQ0_Y2J_bt5-eXrrqnFMQVH6O5pxNSFTjhsuh9P4hghZXAE5_M3CyIw9kqIsAVsZAMrR1fNmg8zWB_PMSSMNQY3IUp11Hidlvb_fYg1XF5yQAW3ggR9ROiq9Clqs60sV6-dgx6rghgqZ0QIoX5tK3bIuu2J0IOL4WbK92RtT5B6tHtcJs6PMDPktlAXIdItvczypfMXsIUyAfMA-mA01U4FOyoql_PojXvy3hhpJufX1SPlHnDgcBoGJBJ6N2NmtqCAOWnzOW7QEYE2elyR5N9dG2K47Psc_8rcNquJ3nbZwmJRCs6FNv6PTsVAJ9919fwoeFlqZZbPAEy2CyiC7r5IQuO3D04gelv0kO2S7S-4djkQ_BXfvQxOp4sWFZfWVdJZ5zUoWt-ZyEg66msH1IGzN62X42l2ur4K100kfUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=DvywSXMJveFCU0s9HQUY13slKabVbqnGx9Kq8_r5k_h4tAPlPBkDPLjx0pflLGu1UBZafNkWMZAaldxItNRihmfHJmvXklDBznuCUFmKurWZJaa4gVD4hR0JCcM9oP6_VE8I_YSFY4leZFpko4fQt0y5M86IksVCmXtHWX1iOXMI6qqDAvKWhj9nOqDCvxW3hHxR-SmxwjVeG6qNVd1sGzI6ipqkLR8RKhESzYai3iAMIl5HfPSIJ-263aj0b3zY4cQ0_Y2J_bt5-eXrrqnFMQVH6O5pxNSFTjhsuh9P4hghZXAE5_M3CyIw9kqIsAVsZAMrR1fNmg8zWB_PMSSMNQY3IUp11Hidlvb_fYg1XF5yQAW3ggR9ROiq9Clqs60sV6-dgx6rghgqZ0QIoX5tK3bIuu2J0IOL4WbK92RtT5B6tHtcJs6PMDPktlAXIdItvczypfMXsIUyAfMA-mA01U4FOyoql_PojXvy3hhpJufX1SPlHnDgcBoGJBJ6N2NmtqCAOWnzOW7QEYE2elyR5N9dG2K47Psc_8rcNquJ3nbZwmJRCs6FNv6PTsVAJ9919fwoeFlqZZbPAEy2CyiC7r5IQuO3D04gelv0kO2S7S-4djkQ_BXfvQxOp4sWFZfWVdJZ5zUoWt-ZyEg66msH1IGzN62X42l2ur4K100kfUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=KgNeNI2JElr1uHnpOMdzzNy64mlohQE9u3tbD7lm2QG8WtQxRnbjpvJg4bmTnYUUAEl9LHAdEzOeifSo_TLd1TUHA1yu_uuvvRnrquKDKpUNpL-oJSc8El3ejfPSBtAWwkbWVH-KHuI7NkZ0wcqJf8mwtp_WOu5--JlrBEDUBNeu5Wj7-jeH9ZoYB0UquMH7_fTLWhK4t0NpR32JsUqO9Eno3JhPIAK81KHUO0jCuc_-sJQBIqP7NDCqv6fafbcdVQO8FvLX8SY2bJlZXZ0OWgqVK5AoOElyc6VrhHhWnDtuBs8VD8Zl_ZzoSjRYXBcLH1lKdJ06O0xbFB_MXnmJ3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=KgNeNI2JElr1uHnpOMdzzNy64mlohQE9u3tbD7lm2QG8WtQxRnbjpvJg4bmTnYUUAEl9LHAdEzOeifSo_TLd1TUHA1yu_uuvvRnrquKDKpUNpL-oJSc8El3ejfPSBtAWwkbWVH-KHuI7NkZ0wcqJf8mwtp_WOu5--JlrBEDUBNeu5Wj7-jeH9ZoYB0UquMH7_fTLWhK4t0NpR32JsUqO9Eno3JhPIAK81KHUO0jCuc_-sJQBIqP7NDCqv6fafbcdVQO8FvLX8SY2bJlZXZ0OWgqVK5AoOElyc6VrhHhWnDtuBs8VD8Zl_ZzoSjRYXBcLH1lKdJ06O0xbFB_MXnmJ3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ub7H5bICdkFtgUF1Zm997D52JP6VKJeGC9_mPNPi1em-hWyuW5uV27QY0UjSXeCfmpU_4gEF3beztRUVBVTj8uiRDopdLnPmdyJUtUrFf2GB9ZOo51F0iYZ_eqe26wjZ8BywmhedRBvpmDm8Jf39rovjTCwKiKCxM-C3H7UxLsjuuMmDlIIttjvwSZpRuqxg7Ia0pmQfZ48vsNOTj1TzGElFayOGQerw2Ep5hezysotI8pgknoS1iS6HdOZ2C6yP8kiR5vM-xrC9d0rUQ6xYW3es8zVNyJKf8Q1zm2vJyKKHDxeLmurwQYFvFiC5oh_2qHcymUB4QQGiyH6gGJ93dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uI52zQ-Hggpt4EztlbYr-RJVZLJaoOub-GCMhYCNy0ECeSNElqRUZSdIRCpa9LHMqiz3IMpSzHvPjd4J3e-HEi1WbYHLauuAUxJZAR6pmZ-lCXVTQop8NM_bUgJOX4UdnsYc8SOr8cmfqpnWUtftpiEFO-Yt5-q7hMDzlBWypFMnF0lQEwob8X-bDdXf_yDLgfS-ygoSi4g1sRQGYCwEfYut0JpuGoOStfQi2GQClXJvkWfTQDtZ9qgw9v5PutXB5O6ipsCy6s9QA2TOIotPIONjddbvK413z2yXvLMYEyV-lpI0_ZIpxNIv2Mc2BmilZpLvbZtfLBuPbHAbwM3KHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=sFkUJViOxGQGjoC9AQC1HeWHuHm70ukdr49C20B_xJfjUh7JdnECTiTDdULr5SsWIcfgd1RWHSvU-XDCNmNILIIvFDrPr11qgr1bXUWShf4mTH9EK6BJq1Yh1HIcEV4xlxJDuHV9o0kpKDcjELm7A8sQ9g5_Ay2mVSIDw2_ZHsBrowLqnCml7Twk3AHtocIVtAAxSJAbYuuueCvOgRkDIv5kS1ccmSot4eVSytAh0wxHSFe6B7Igu7gpmf3WZ8HiC9eAFbXUFTTFkFaO8wXKAUvBajEclieEDq3e-wUr6ryEpGIVXx0Qe_ATZKnHlq0DG_QZK9Ktoit0YKEae9GyTzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=sFkUJViOxGQGjoC9AQC1HeWHuHm70ukdr49C20B_xJfjUh7JdnECTiTDdULr5SsWIcfgd1RWHSvU-XDCNmNILIIvFDrPr11qgr1bXUWShf4mTH9EK6BJq1Yh1HIcEV4xlxJDuHV9o0kpKDcjELm7A8sQ9g5_Ay2mVSIDw2_ZHsBrowLqnCml7Twk3AHtocIVtAAxSJAbYuuueCvOgRkDIv5kS1ccmSot4eVSytAh0wxHSFe6B7Igu7gpmf3WZ8HiC9eAFbXUFTTFkFaO8wXKAUvBajEclieEDq3e-wUr6ryEpGIVXx0Qe_ATZKnHlq0DG_QZK9Ktoit0YKEae9GyTzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJoUjNgQ-7CKFEnASY32Ja2LIJzZT5rs576gLmH-ExqwKY1m_n1pZnvDGczyFH2KLc6TE6detZ5XlaJGqueO4PYgim0GqBGVK2BX2gmG0TN4YQxWTL9r7Gqckg1uTS2E-dGYk96VW30Jiu8SJYp4c7AO4q6VNohYaBCGHD97mbkU_vVXwef2Ldfoqj_OXScY2lQUp9utgrkBKJAX9VYNemrVwcMWR1sJPblB2krNiPWg93W6CmLAq84FDnc3vWzuaaQtlRkM8GkguVnmIw156rmzf-2cB49iRPRZQ2FuNjsA3V9Llwx5jfytd1XWg2R-pD0_m-IQZI6bUGIXrREpxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی ۶-۷ جمله نوشته که خط به خطش دروغه!
نوشته که مصر یک شریک مهم منطقه‌ای برای ماست و نمی‌دونم امنیتش برای ما فوق‌العاده مهمه!
در حالی که مصر و جمهوری اسلامی ۴۷ ساله هیچ رابطه‌ای ندارن و مصر حتی ویزای توریستی هم به شهروندان ایرانی نمیده!
همون موقع که پروازهای جهانی در اوج بود، حتی یک پرواز بین دو کشور هم نبود!
نوشته که اسرائیل علیه اتحاد و همبستگی اسلامی است!!
مصر حتی برای کشته شدن خامنه‌ای، یک خط تسلیت هم نفرستاد! براش این اندازه هم اهمیتی نداشت! کدوم همبستگی؟؟!
🔺
دیروز به دو کشتی حامل گاز مایع در مصر حمله پهپادی شد، دو تن از مقامات ج‌ا به روباز گفتن این فقط یک هشدار بوده از سوی ما.
دمپایی پوشان یمنی هم گفتن کار ما نبوده!
حالا این اومده میگه ما روابط مهمی داریم و همبستگی اسلامی!!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmB0deMgWZk9aJnlnSLFODlBvPB2hZ-_D3T83RTjNfT8FQhfIw_q2hVIt8goQP7wq7vkxAyPaYGRWlivUvI-Kfs4njqFqlDgaL0wT1UyRMkWfCgq5Xc6CA-9NeB49YnZWYBidcmHUjaBdvi-4GHvhzT05L3hfcozLpTBM-2nxhvUmaR9t1YLj1uQmAiJqmIWaLqnx6SratIS1ky5Q0bmT2_vT8ZDTIKSoxSXBL-06xst-Fi47JhKVqAhPgeIkHM9FQ5EANl0UbPLziKMOC8GRbF45mc6RXiuV30a5psQJyN5MaJwoV6mzF7_4CfALkMf2nR_RFQNKsBmKN-qORmzeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8jRAKPd303j_rXAgXEekpSidjPB1L3aOOBlsTRt7HKKd7y4QhUSSv4E91JFD6APDWyOhAx7WkcFyP2XPRxluWasBgIizZbwVAdsVQ4l1p7RZ2vcvXCKIrWr5wCJLe-vfS_oewppbM9D1LL7aSCX_-afprKYcYWaERPNkO5QiuM2PHI1_xtCnUBJnC0fPAL70b30yczJY_sWBXd-CTGoJ5l1UQ0MxKDy20l6lktn4HnlTl7-kmH6QLsHDnvbtigsgX4SNaQEsOu1kdXqoF8TBJ1u2M5vWpkvjCo66ourDqGS_ZOxRAqKbfT8nJMq582ziCPI9ORraEobVQJcFTgHvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNbsq_CXcu_KXt3IgptOYL1lHAhelYV5zkidmP572VWRo5BKwuHj4C6EFN-Q9Bla4O86kDPAkGDAv2ktT2WucZ6HRLmblY3m029RCy-Vk-XoRJh0qkoCP5xNq8XwhyJw7MGnx3qwvobKvlJJDjFs5Rz0OgwHBD08Z646Z6EJW-NK4I-uU2eByafyvyPWOsRQKstrkeXVBHqDTWl6Vhn9TTO1PuTA3pwyMlrC3QakeeOtCP793mMl83DzUOIbaNqXjPoa7HkGIdPWAxKWYvcbAzGFXrNE7KhSJBKyOzpkmKwbfUjPWSyq2bDqSTEPStSt2fF4nxs2DPOAxgmJeqdPzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بار هم درباره حجاب نوشتم،
در حالی که اکثر زنان جهان اسلام
(نمیگم همه‌شون، ولی اکثریتشون)
دوست دارند مثل زن‌های غربی لباس بپوشن و…..
زنان غربی هیچ تمایل و انگیزه ای
به لباس‌های زنان کشورهای اسلامی و چادر و مقنعه
و عبا و نقاب و برقع و پوشیه و ……. ندارند!
نیاز نیست حاصل تمدنی که اسلام
و جامعه‌ای که ساخته رو در ده تا کتاب قطور جستجو کرد! همینکه جمهوری اسلامی با حکم
«۷۰ ضربه شلاق» و «گشت ارشاد» و بگیر و ببند و پلمب، ظاهر حکومت و فرهنگ اسلامی رو حفظ میکنه، نشون میده، این تمدنی که میگن،  یک آدم برفی و یک توهم بیش نیست!  که به سرعت آب میشه و میره!
فعلا پول نفت پشت سرشه و بگیر و ببند!
حاصل ۱۴۰۰ سال عمر و ریختن ثروت و اموال مردم ده‌ها
کشور برای صدها سال به پای این درخت، هیچی نبوده!
نه هنر، نه علوم انسانی، نه صنعت، هیچی!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L99NCm9cUpkp5osJcNs7_UtqYqIBXX6ctx27okiF4rQdfZOz68lGCFItYCDtaiemaOTBgKlLDmmw4HxQkQ8O7QgtrfLtskexjtxCW1XmCg9Dw-EwjPRhwZLdONc_nB1jcm8e-0CCj2Fb2fJh5phVDeqRpjfoyoshbH4RF3Thur3_cOsTHmIHL5A8nJfa7E9W63-VmXwPQNuhCYjYu8BnPI-ZX5_z6Zt0f1GS0RREbmayoSnDiT4DvmVhTpz6OOWQPWiXxara4b-kmjOZ0Yuul1VIpNdEEJ5_QqRlc59PCGGipHZQ5LR5E3oegpivw7nJVZBsgicPMAVQb_CdGGdPUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJUQxen-TgXN--S1fQvbkpYDwC8jO_CO010Yy-F2cdJHT4PtEeKEHe-q1ub2zTpr0YOXa9y0FsvT7KRxAauSTN6nKAb-ON0CoorBzeV8GJviDcX5OzT3PeeRXB44DAyNMgH228JH8lzWoz1zlfJGisk-v0PSIa8qIyiO-M3zBRYTP13X8oU0mt0tCzizCcN0S4I-1npHm9Jsn5Mvo5dNAPf_lyqG3Lpmb0BT4gIoX6sb7-GSMtoVYSgzSPdIrHhyz7bfTt5gSqUQVxdWcnUEyMiDhcn-_UWhLzysHeCHw4yduh5BY5ZiyZszNlTKl8nIVSBzU7Y7KhVVmoNQGpQct6yc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJUQxen-TgXN--S1fQvbkpYDwC8jO_CO010Yy-F2cdJHT4PtEeKEHe-q1ub2zTpr0YOXa9y0FsvT7KRxAauSTN6nKAb-ON0CoorBzeV8GJviDcX5OzT3PeeRXB44DAyNMgH228JH8lzWoz1zlfJGisk-v0PSIa8qIyiO-M3zBRYTP13X8oU0mt0tCzizCcN0S4I-1npHm9Jsn5Mvo5dNAPf_lyqG3Lpmb0BT4gIoX6sb7-GSMtoVYSgzSPdIrHhyz7bfTt5gSqUQVxdWcnUEyMiDhcn-_UWhLzysHeCHw4yduh5BY5ZiyZszNlTKl8nIVSBzU7Y7KhVVmoNQGpQct6yc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnI-Eu-oYm7fDAnIlZm9wl5OaBDNjEZyH8gxlC2NRJI6-3-aRRm_t9X1K4WcBxhMUkFlfjDOeWCCOzdQGTgaWcufRd_DxtLSY_iHtc1aAOZZJAgp43KkboW9XgsDdQseP6zwQASlyOgEoS_kRQvEwUq2l6uD7Xl1TvcKAwV13o7HX9Z7Yo-gz7ynCuxChKvAUGo24PG1rCcSnLGz8cy_6i-8GJxutAhqPr5muN-AoLOXLmn-mhBtUMNFX19FdA0ftwtrV7MCSrOrwrzrGTUocJG-F1klVxMcbv5-VwSQNB9W_QHEus5sysCT2ATBQaBgcHx0WEAfqL1OlcUJkJGroYnI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnI-Eu-oYm7fDAnIlZm9wl5OaBDNjEZyH8gxlC2NRJI6-3-aRRm_t9X1K4WcBxhMUkFlfjDOeWCCOzdQGTgaWcufRd_DxtLSY_iHtc1aAOZZJAgp43KkboW9XgsDdQseP6zwQASlyOgEoS_kRQvEwUq2l6uD7Xl1TvcKAwV13o7HX9Z7Yo-gz7ynCuxChKvAUGo24PG1rCcSnLGz8cy_6i-8GJxutAhqPr5muN-AoLOXLmn-mhBtUMNFX19FdA0ftwtrV7MCSrOrwrzrGTUocJG-F1klVxMcbv5-VwSQNB9W_QHEus5sysCT2ATBQaBgcHx0WEAfqL1OlcUJkJGroYnI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=NMj62a2I3M-VQ-kEDh4gEvlUsmxTdywgkwd_ifvh_ew9Yo6Q58_tpeY7lDucaCweHWh2_175g_1Sn2YakbkPeV9ijWfB_RqRpTzGGZ3IZB-gd0bbuav0EoGnfYYB7TVlCsPUe7t80Eq1CKY91mBUnCxYbG4FR6vEtcgIvjJx5JdKIg1B82iiNJWTOdsLvCcvlDbA0lP3P7sLrjq7lmiCoUmjx1ygpTJE3q1gdH44AYqOQzMo692G86dgP1-CVzVw_gjGeAjcQKAHlNUmYUO8DQC6SwZwxuWI-I9IVNUNLlZoTfVPUyWkN6Zruh-kcXPDwk0goYP2YHhCnl44MgNF8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=NMj62a2I3M-VQ-kEDh4gEvlUsmxTdywgkwd_ifvh_ew9Yo6Q58_tpeY7lDucaCweHWh2_175g_1Sn2YakbkPeV9ijWfB_RqRpTzGGZ3IZB-gd0bbuav0EoGnfYYB7TVlCsPUe7t80Eq1CKY91mBUnCxYbG4FR6vEtcgIvjJx5JdKIg1B82iiNJWTOdsLvCcvlDbA0lP3P7sLrjq7lmiCoUmjx1ygpTJE3q1gdH44AYqOQzMo692G86dgP1-CVzVw_gjGeAjcQKAHlNUmYUO8DQC6SwZwxuWI-I9IVNUNLlZoTfVPUyWkN6Zruh-kcXPDwk0goYP2YHhCnl44MgNF8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipLB6t2XbEWtNbexuA74Y15sQYj86eDIsuaNp3djZe5c9zfWG4JRKnfpl_auqmng2gQ1_Vlqjqk48dI3duLKZ7ojonQy70N85-w4rewF6J2gmHl9qhXeltnbRiJV9ekQ3JOr-0FL8KXKHxFct0WfMXuFBakmX8Ro98J6m1sSEFcWQWqRCr5FP9Ts_Cjr15SLeCfzXchGllcnIJ3AHIPKf6TUFgjJFIKHiv7bVm0t5Vo2-I2HtoimxYxqej66MivPxO5iCGF5X40bOvU_l8qQfThkWpKCk82TtTHqYN8FFGODHpt4KE7gYKpRKFlEhUZyLzhGdhhWac7FQnl_5BoL2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGzoOmX4-7k-ExJnDR-YxwIGQ5E5BMu4dFwI7bW0hALhTirxt4uLgwqtsV0TmhM4Z3UB7_4bkvLX2XhC4v5LR6Uh0hrhBlrOLW_dPsfVWkKhT_5Dcp056XjXlCWAn5tn7K_Ocu1BbKBxn_EKSGqcvlPc7UAYsHyjFan3f1DpIN6pF0SN6pBKcytQHqmKhPP6XOA2TN0pCxfsPvm8e2-fZU66ueCYU_qIG7MlWeLe1jFg_XhLP_O8kFNBMzM5xhIbdvq7I5SBKEUTPC26HFVTnlX4UGWz2Eq6mqM5epb8Y-VqfScdfs5CziKIvjW8Eq9mvDdJugkKAOowsU6T8yGfzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=meRlo29_iYWPOqAQP1EyuUaGoouvMH1lN279UYNZasGbfxCzHk7EeR4hwuDFUfHjHdxr5ELJ4-YOkpRajG2fiiLsx531o1uvrbPBix_6zPLg7l83jYA8_3xxyQmEI5LCkzcGFKLMcBBLSmFwSnBBtlbmdLiNm8tI4BxQ3j6sWCfvto1zx3Q21ej_S-RoF2NfWHrb_itr7pciTMB58e_UVkhdK6susAj2eN6A6VQA6S2H5big2phyA02LnBxAGGxpAipB3-QytLyaKAQ_qaEdgWnPQxL1XFES7kzG3EJ7A3jklgLk4A5VlcP3874xQWsSg0DEAj27nRXDbZ7a1gspmYAL3JmHnXNBRJgPRDtLJBssnKAt406BiSAWDh_Zi_atG-wIeLYDZgbXQ6NlKZYOPrQO4e3QWmQjuh4y9fkrur7B52re2vH_quY2LFo48WmoCly2yOoOOAlTTBHsFBLSwj5A6TROFDsvEoEGnGY1zmrYHGx-DutJaBYpj4T-pDpNy73HRDZkcG5yh-pWiD67VrLYcq8eiGvsm99BefEblOM1vDj8HO2DTuL75nzuSX1kFQkvvg77kImSwr1R3MyUewJg7jZax58AqPsP6Z-vubFa9OIehTnL3LULIqtTW9fchteKHLUkuE1slgk-FBq7Cv66p3d5VJu1t2zKLVbtLGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=meRlo29_iYWPOqAQP1EyuUaGoouvMH1lN279UYNZasGbfxCzHk7EeR4hwuDFUfHjHdxr5ELJ4-YOkpRajG2fiiLsx531o1uvrbPBix_6zPLg7l83jYA8_3xxyQmEI5LCkzcGFKLMcBBLSmFwSnBBtlbmdLiNm8tI4BxQ3j6sWCfvto1zx3Q21ej_S-RoF2NfWHrb_itr7pciTMB58e_UVkhdK6susAj2eN6A6VQA6S2H5big2phyA02LnBxAGGxpAipB3-QytLyaKAQ_qaEdgWnPQxL1XFES7kzG3EJ7A3jklgLk4A5VlcP3874xQWsSg0DEAj27nRXDbZ7a1gspmYAL3JmHnXNBRJgPRDtLJBssnKAt406BiSAWDh_Zi_atG-wIeLYDZgbXQ6NlKZYOPrQO4e3QWmQjuh4y9fkrur7B52re2vH_quY2LFo48WmoCly2yOoOOAlTTBHsFBLSwj5A6TROFDsvEoEGnGY1zmrYHGx-DutJaBYpj4T-pDpNy73HRDZkcG5yh-pWiD67VrLYcq8eiGvsm99BefEblOM1vDj8HO2DTuL75nzuSX1kFQkvvg77kImSwr1R3MyUewJg7jZax58AqPsP6Z-vubFa9OIehTnL3LULIqtTW9fchteKHLUkuE1slgk-FBq7Cv66p3d5VJu1t2zKLVbtLGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=Gtes3zLjK3a-xrwQ0rG2nOxY1mMZvgoYzqSabOT_joyg-7cb5-h3JFk2C45Y9T61fCvYct5QFJwJ60KkUb4l8uRfMOVwtvra-eYb0veK1zKAnY3xiDCENA6jjeqGwfCMcu6QKSqcX2ntZ9YIYqzjtyqJe-NboslCbg2AvQmopdEEdzlub10eD4MwLBywNF4ob0_IoWkU5orZ9esqXFei6OaN7DLBAI16x9Nbe5fxPJNVoGCypsx7WyRo2C-iMzTJVGEXCyzozQjyJlxwEvoCs1yYK6qCn3foopSaHIMjObmPxsaR_nbcIVvtROAGxG4Ztln0NIXgoVlvt6Httn1zrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=Gtes3zLjK3a-xrwQ0rG2nOxY1mMZvgoYzqSabOT_joyg-7cb5-h3JFk2C45Y9T61fCvYct5QFJwJ60KkUb4l8uRfMOVwtvra-eYb0veK1zKAnY3xiDCENA6jjeqGwfCMcu6QKSqcX2ntZ9YIYqzjtyqJe-NboslCbg2AvQmopdEEdzlub10eD4MwLBywNF4ob0_IoWkU5orZ9esqXFei6OaN7DLBAI16x9Nbe5fxPJNVoGCypsx7WyRo2C-iMzTJVGEXCyzozQjyJlxwEvoCs1yYK6qCn3foopSaHIMjObmPxsaR_nbcIVvtROAGxG4Ztln0NIXgoVlvt6Httn1zrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2nVMPVl-mupDwGRDqpKecab0AKYFt0SlghbP5UT4UxqKgabWpVrksAAxspW6rqCqe9KbanOUZ_CUz6Nm9W_pdHBbqhQhB3QrZDmA7Od5Yfhhm2t2jv-HPNv53DjtuhGWCegTQB3OSuj7daPW6cgKGdXAaawmfSHiYJ2M6urTlCyqKIzgh0OvJVHaCwZKWz89vi97g3Z0rdnEkhQfupUHaXrwUaRLUVcJV_ytF7U5lu4vrJ6S2OZQqH6tquF1v5M0QGO-41KZo_fEcZEUTMLvJ-iP1rq02lJR2zmDBUOwd3hGL_gxSRXfGgR8FrEVrJy90Ppx16VUb0cAZbYjk9qxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuIKu1A_RylXCrt7H5a-MSOBVH7YPnwYBZNt2lYzASI7Q7EZ_3VnbrgNtzx4FZJCz9tG1G6S4AKYa41h5Cm0vXy-ayKKRkS54FE9-K2ROpctVXtP6iiAippI0Ws8KUrmfIHLLVlgvTXHCUiXQ14fPH4GyiHdAEiV2pekXiQi4cuzZxIWzaeGdxRmxxC6WIrBnhJ5iLGWaVGb8wPunB8D30EKntz0TRmJdDrnF55ecRyHoKy1flsBUsIz_S6kaOZf1KOLh3vB64P80fWmrfvTs0aBEQkYf0Mx8MdORIbpFqBnQ5arG8loVUJHTfP1BBgCs4-eZFobcoTSVWaa5c0fMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HtbFpGKOYALIuH1eaXsI991EwuyztE1Wxf2HzaM6GtZbS_beK4bTWl6kYtszDeglFrHKk1nB_knSOAv0gJiWe5S3JjI-i57CZpTFt0sWDBTXgdPDbaeomapxoPqU18beFTSL1Ef6xO_PTobt1i2HflPNEeYLpvgv_QCCXXN1QkqXOumQYRRf0jpgXpdexFGswgiJnUPJxfXyiiGHS3grB4B__jQkxgDvXo_3cuO0Gs6R1StHYewO21GKuxZJM_A9W3jCwFdGpaDa0g0PBqPa4BIDPyzuvpWrsMIUJZtMoYZbaBswvG32FcKu8MYUgBJThbYzqgw1kbkynTxBr-dckA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=QtB7FgfHoZ61RAUvM0kxiDil7-Ux3nXChexpyHFV2SglMxKko_lDwgeYf8BMaZ4J-s1ZK6dTjJblcYh5F1X4-s076GJlKnF71C-ZRH2Ho1ncABuMXyvNb8Vathtg7xqGI67RbL51o0WyrIO_sb_2MxPNSjtUaojmoHUfqiT4HROrJN3WfgqjBr9FCCcJ6Lx3CIZmwe-kmbMWseXjShcPSSWnGbL03edDJRxFGZwDyzxqysvnZ3MHtGxB1kL08fw9uP0WglNGabo4JiVNjsY7RhIswOuSMLXOKsigsTzz6IJmHa8GLRYR4Jb_LRZSs35SvygcqXpxyAT5InbtIdj1cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=QtB7FgfHoZ61RAUvM0kxiDil7-Ux3nXChexpyHFV2SglMxKko_lDwgeYf8BMaZ4J-s1ZK6dTjJblcYh5F1X4-s076GJlKnF71C-ZRH2Ho1ncABuMXyvNb8Vathtg7xqGI67RbL51o0WyrIO_sb_2MxPNSjtUaojmoHUfqiT4HROrJN3WfgqjBr9FCCcJ6Lx3CIZmwe-kmbMWseXjShcPSSWnGbL03edDJRxFGZwDyzxqysvnZ3MHtGxB1kL08fw9uP0WglNGabo4JiVNjsY7RhIswOuSMLXOKsigsTzz6IJmHa8GLRYR4Jb_LRZSs35SvygcqXpxyAT5InbtIdj1cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=jhNC7cGTofKYc3DUpNmerAM5Y8gqysvdkYhnI1G4rCE9t5duBAmTUaq5LKJO25V6EU45h6YA-oBl0vWL9-MpIGA74ADihkMOLv1PKfySb5RqiTLFxGFotgeMtqaHUT2Hi2JEk1WkDli-6FCJxBrha9s2Q8OM8K5jNikQvZEq_9a1A8WLdrm086wMmeaYqc6auSyEMfV6SndmpdqdDaUG3hHWOLvAJrIgxjQsjtroq1iPeOQV3h15yayd_7MK_VEmTHHQgewy4jnkjzREp4uIaH1R2_0OxGDECZnheJ5Rao_kce_XdH6qa-7et7khJA0kHD4w2IvtMRSY1c0DNsw1mw0uFQS3YFJdqzRfyUqe6uvjb7aUR1jlBQ4LiEL7AINAzvQ_NwGGqfP8O3iPRSX_MJ_EPJkl-N1XXpgkZV-bFcP9S_W-yX-OMMpJWHoe7M58amjihDl89b-fYY5rXSkHr83SgzxYRebhmaATmJR_-9v3LBmlvtDkMRgC_b1qHTFfoUmLmm3UFKEUS7EqEzKkDQPSiSodonjIr-ZV2BDOSxwWoJs0YFPu65iZ3s7quMJNNQuJ21VZGfFOgW4YSlYDRldMIdWZo0N7L8Y_-SqG0roDUDq9d9DPRl9lOEdHWrQ4XxdC_ByNz-jVTF7xyJjoMhYCL8O6zneiVrSEk0wFcug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=jhNC7cGTofKYc3DUpNmerAM5Y8gqysvdkYhnI1G4rCE9t5duBAmTUaq5LKJO25V6EU45h6YA-oBl0vWL9-MpIGA74ADihkMOLv1PKfySb5RqiTLFxGFotgeMtqaHUT2Hi2JEk1WkDli-6FCJxBrha9s2Q8OM8K5jNikQvZEq_9a1A8WLdrm086wMmeaYqc6auSyEMfV6SndmpdqdDaUG3hHWOLvAJrIgxjQsjtroq1iPeOQV3h15yayd_7MK_VEmTHHQgewy4jnkjzREp4uIaH1R2_0OxGDECZnheJ5Rao_kce_XdH6qa-7et7khJA0kHD4w2IvtMRSY1c0DNsw1mw0uFQS3YFJdqzRfyUqe6uvjb7aUR1jlBQ4LiEL7AINAzvQ_NwGGqfP8O3iPRSX_MJ_EPJkl-N1XXpgkZV-bFcP9S_W-yX-OMMpJWHoe7M58amjihDl89b-fYY5rXSkHr83SgzxYRebhmaATmJR_-9v3LBmlvtDkMRgC_b1qHTFfoUmLmm3UFKEUS7EqEzKkDQPSiSodonjIr-ZV2BDOSxwWoJs0YFPu65iZ3s7quMJNNQuJ21VZGfFOgW4YSlYDRldMIdWZo0N7L8Y_-SqG0roDUDq9d9DPRl9lOEdHWrQ4XxdC_ByNz-jVTF7xyJjoMhYCL8O6zneiVrSEk0wFcug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxzpXth2aW4sbE4nmSkpuzpX3prOfJ1-s5snX9-0BSTd07hHG8JE2xDsXtN6zN0xaE4jx351HfcvpmdPJf2cgebxuAJ7kKNQ8BkdD2Wl_o2HkRw3O9kojBYxPdUKxHYmNgzpZd0XzRQ2xu_F6MHAo6wAU9_cAWYla0SaNut_1tS7ARHgRm1iF4v3FJYlqtHVOp8KEcbXev-nEdtbik7oZH1IjE4mvrYgOF7YLAfu-UFYiLSiCTrq33OXZ5v4yJoVwyjwbKEt72BIgKiZ4Vhfon3S-WRpyuUB0RqBN-DfO5TJqF-uJr2B6vQftQuKybwowDxKkeFf-CYwryXbFpOV6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnETlJ1GAaO2N9QfrKrrUCvyG9fI4N7dbEIn6VdTtYLcrWqOq8muDECx91ZvMvR9mqcsjV-82JxB_0kb6UJBVSXPZNMmWEfL-eVFCf-972kt2nnVroUxYvIwjdGYUOdU2oNg2ImzN5BgCzMfDuXSOm-V3LXMyd4YfC1D_hZ4Pd_XEMUQ8PQB27IaNoz3p8SXX_ASlc-KkIzyAWdy59E5SeqHr7P1FdFm29odiehrgpyjYYnMqBzT5bo0iUqsJwmzliPJsjWktBwzwApTiWiOC47r2p2mQEaJVQlQZ325T9Tp2u6EM8Ov8cPaHvBWj8CjRV9_D8hShJEupusWSE0xBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=T8ML8Av9LbuOl11nl3I7Oj_myoPRwZcXeg3BOnO0_X-ih0D-9CFH2k3YW_NOcScEdqscqt9kenN5Oh4BCd0wUYJKeeQidTFGh5MGSfsafIaUcuzX3uB3kJpntoXR-PkJMcFh7ctYwD73atr94Pl6l4efzeKtrHYMSYrb5Ct5KeDqG4D_Mzawed0XwYO1axzQKgNKyAdCHkPuCBddeAj2T5wUdRXFjdnXtst_qkA5yFgGFovP9EHj32GjbNcgeuOSCvIuu3q2S5rihoIJqfxrAI5XKuGCO-XqY--wJwWesBFDiwio_ENEwQibj_vWHjRJp6ZGAibeZX1d3p8rNOP2sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=T8ML8Av9LbuOl11nl3I7Oj_myoPRwZcXeg3BOnO0_X-ih0D-9CFH2k3YW_NOcScEdqscqt9kenN5Oh4BCd0wUYJKeeQidTFGh5MGSfsafIaUcuzX3uB3kJpntoXR-PkJMcFh7ctYwD73atr94Pl6l4efzeKtrHYMSYrb5Ct5KeDqG4D_Mzawed0XwYO1axzQKgNKyAdCHkPuCBddeAj2T5wUdRXFjdnXtst_qkA5yFgGFovP9EHj32GjbNcgeuOSCvIuu3q2S5rihoIJqfxrAI5XKuGCO-XqY--wJwWesBFDiwio_ENEwQibj_vWHjRJp6ZGAibeZX1d3p8rNOP2sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkIs4atDiJTt6H6BdTbKiDWJpqm504RX3z7PligZKtzSsffQqF2rg0Jc98XRYpbGYYwt6B6Fk4FvBCo3ma1X14bAAgSYTlSWOBO6tgzhLanADOzin4tDJeH7UxqZUWQQITtrAAeTbJb9I-PGYqt1bKa95xz1gEQawesSfvR0Y5M-Q75DRB14kZSxUv4vAcvvwIryByJDMd1rC8GFnLN9aGgiwDnNxb48rmllkzONeUOOluUnpAXq5TdAJ9y3lkdZ2RoqU74kn0sfOMAuFc4p2c8kIlhlc9rBeVt2jq_CFA_kvQQz68IFT6JG10ctgzeGFwpvwjvdUEtWclKiJGlScw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmKZKgIw0tu-ZFxPlEwflDkMga4XMoTPbWpsSRQqICR_O3Y8pR-n33n4pyFvHp66iBWTHajaF2tzaHp-wqj9KaMDjnrzF5cjxxJB7O0SEoVery3EsgcI9tFiM8OZI6A_aZaNobSxg1h6cfQ9uO0j61p62rFnyFpecdETKkPyAyzsL_FqU47jqmdYp44ccNpn-LhYs5bd-6NOIBRWE-74GTxFoCFtFkzHx2IoNOnUiML9eBft-MO9zDuTnMC2mmxUYAWgbOM5uo3v7jPq9MROdnp5yLmWzp9kxV3dlWBOLteAXpVGjJVxDReZCQWDwSdOskuOgZEt7rvET_GzmNNP-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRKUL52eQfl-H5yk8155Mf72C1clcQR9qx489Kvap46Y1rf8wjqJlw1OqvNU5k7XupVp03SuXgcFj7dRKSZE9pwp3gIArVF9VR60yERHAg1ScssGiW3xUv_y6bAMyok2nfoAMssNNNc2KM3dXxvlzFoAkm_xoAryiygsXFf0dF6zwx7IKCyXQdGrEVB0IkcZ37KIPET2Nef17g-VrOtavDM9CVK1ctSYrAMj1F7t_5qKBP6hkD9r7V7J01l0qJqB9QjzcMadeKc-bJYPudAoiF-wViEEq0h-imPtbpvueZ2Z7lrAXm8hqIPSyv-fL9bC03VRNZAzSd5zNkEdW55NzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLS4CvovJLYhS864zSgXfrg3kharS47oNRJiIoKIKHcNzarUdGww6NuLPTmnu18Q0ELx6WMBproY5hnOu-OEx6qOmSCS2vzl4FMQ8tv8htCpdCf_vmB6T2JxQw2VLlu7v80NVFEn_-oQn_iXvQJEMfsc0vVeZULBf2DaCiCGhb9m4j-wAwbVxqGcHDAXqGZ8bFaN9yb-ar8zlyxz5npeIFjPplBjVtV1xmp3jl7T9J3nia0hofJUqSmYfREQzierXHssYgeRm7reWXK9bsaUPYoT2CLGK1dImYcUg3Qo_6q-kAUEL2TTlTEGq0CBWe6_hBgPHWCnPWI1IqwcQaFicz4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLS4CvovJLYhS864zSgXfrg3kharS47oNRJiIoKIKHcNzarUdGww6NuLPTmnu18Q0ELx6WMBproY5hnOu-OEx6qOmSCS2vzl4FMQ8tv8htCpdCf_vmB6T2JxQw2VLlu7v80NVFEn_-oQn_iXvQJEMfsc0vVeZULBf2DaCiCGhb9m4j-wAwbVxqGcHDAXqGZ8bFaN9yb-ar8zlyxz5npeIFjPplBjVtV1xmp3jl7T9J3nia0hofJUqSmYfREQzierXHssYgeRm7reWXK9bsaUPYoT2CLGK1dImYcUg3Qo_6q-kAUEL2TTlTEGq0CBWe6_hBgPHWCnPWI1IqwcQaFicz4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFNEpUNbvYh9PPxOSTbC7s9aWtunW0JqjN9ZrdWc3IJV1D3FwQe-x3pSXNMrm3EaFC5fajYm9LVw9WCgW-dkKli7Q6xmqDDY7RT9XY7-sTTZrxS1ipBhA-0-UKQ1kjZ7TABLzWNOtFUgHpF9JAvFq9q3TRGNiBD2rDaTBRzNQ4f90_sQbo4YDFsjKCq8S7-VcNBRC4kFAqekTjiRx311Pxayqc58RFpESpE4cUpVvBi4shrM8M6euJBhkbGxskiW7M8lwyTQiND5WQWeCbMrYl47E4mTWidyo1cPc58lGpJcbOpez2anUr3Swn7uqGxZnq731Pie3YuWsMjKFLwoAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WFT90zK3r69mP0NgUMxJ8EMbqYjpu4Drs07-5hxryr4gyzFdSKwY0ELygsy3CC7oUu2s5gqCn-4NL4gzAYdJU74ODZvvrSEtxKw0AY3DlC2lRFlW-w_jK89JZvWUuWUSvhzP90eW9AjiaTiHeUqzpaJgApZF3DR4kuLUpl_XSFADLJK84eQRNe9si3eHABXYjFBBYY9JR2kmIvljYjSrwLcOfzxIjA96ougc7RWmvwa3C6gPS-W78z5AFx3k9YYiJiNLA6vH0AfkMlHPA_q8We8sIlU_da1rQNYPbkLoxr2hk-CBWSXwQIvqmOMA0e7oSMhKc2hUFn6nHjbPlJpOnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=O6ngHwnB_-cRLgBT3ykEGemDMDv74R8dv-Oh3-aLo4Iq1m5YlBCnY1sSvIf2oQaG9muDipapoC6JmgamRupqT8iVNvoeVx--6dxTseF_j-gWfa8u4-TwFmdh_ETf683ecbCcg9ZYzDLGcgP5XfB2guqv8MXsRMXtU7pbKOFFebiuVDSRL0mnqQhazs_f4zycuH4PG8kiZJOEJdVuu8I41qI4S57Xujvqbt2-QxDSSfzI7PfNjowHypAV3iyoVM7V7g_8WTqiJjHCQMJLRtYB8bdwhHbaX4OtblSUCU2IH0SK9cEtqtz5_F86KIm7y8jYnnQNBXbjFnayaYBIqU-tzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=O6ngHwnB_-cRLgBT3ykEGemDMDv74R8dv-Oh3-aLo4Iq1m5YlBCnY1sSvIf2oQaG9muDipapoC6JmgamRupqT8iVNvoeVx--6dxTseF_j-gWfa8u4-TwFmdh_ETf683ecbCcg9ZYzDLGcgP5XfB2guqv8MXsRMXtU7pbKOFFebiuVDSRL0mnqQhazs_f4zycuH4PG8kiZJOEJdVuu8I41qI4S57Xujvqbt2-QxDSSfzI7PfNjowHypAV3iyoVM7V7g_8WTqiJjHCQMJLRtYB8bdwhHbaX4OtblSUCU2IH0SK9cEtqtz5_F86KIm7y8jYnnQNBXbjFnayaYBIqU-tzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=EYl_g3qK6kOmbN-5Zjec1PQ__wcQfpPUeWqhpUztNT8VLRCu5lhFHphTIetN_g_j2Wx9QbUpY4aelSd6Q74ySQg9V-1DwcRgWjXpM3TAaQUZsD8U4kQ_2tTtEwxECUC_vvAyDiba62NVY92oBn3iilK1EAOCy4Tz7pfnXIc9zk0BHvjKG2v2fvJpeGh77yfi2U3aqc0ihOmXsGD1CnqtQGjwxzSyAR7MkC5oFs1Bek5t6Pcyh09G2KXSVxE47ScBBJT16jBM3SU1Yyh4Hy5BeoX49KRkUFZHNGIKqY-0vNh2pjtxDONG9NSjmAV-ZtdrEdSr43jxda5PVBslVYzyOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=EYl_g3qK6kOmbN-5Zjec1PQ__wcQfpPUeWqhpUztNT8VLRCu5lhFHphTIetN_g_j2Wx9QbUpY4aelSd6Q74ySQg9V-1DwcRgWjXpM3TAaQUZsD8U4kQ_2tTtEwxECUC_vvAyDiba62NVY92oBn3iilK1EAOCy4Tz7pfnXIc9zk0BHvjKG2v2fvJpeGh77yfi2U3aqc0ihOmXsGD1CnqtQGjwxzSyAR7MkC5oFs1Bek5t6Pcyh09G2KXSVxE47ScBBJT16jBM3SU1Yyh4Hy5BeoX49KRkUFZHNGIKqY-0vNh2pjtxDONG9NSjmAV-ZtdrEdSr43jxda5PVBslVYzyOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzRVwruoo50E3vOsydzKox2Ka8BYFRhTlUu9p06SuF7JwP_7Bskb4t1RmB4LcWDTlEEOXYpvUzQMRQMJGWHxhvAH64IciLOhrBDeRF_4OH9_HaOnzEGqkqQRqVSrzOWE9-vOKU9r_8J1DaY1VKCGR77ZzCImXNmL1pnGtko9mqTEiywehPwcW2kMNKa_5fBFVoVpKSFIkR7OaSWv1SNPIdoqX9ZH7_A6hIaueiNc2Ht6IgvBuKb7o2gSP4khv1dA3booBra7GraUgh_Q59K8_AsiUPXHxmTYfmBuPVVnGyxy6w0Bz2oMt5xHdeTmiu5G3lHhVyUf0Ppr4xNSGtLtsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ahl6jfK10CTRVYLyYMc5s6jMwjmCRZjYBPCZMHO7I-eQ9NhHd0oLbbsQd6PPEIyJrKEQFIjWcEAf9EXYQCCkz9BEF2nkbgQYYq8dGRyha3SvYYaY93j68f6RPj6dO_mql-wvYP7tuCFg3FWZ8QYFaQOiMWvGX4jw0mFU_b-8qg5sRj6IpCSzwRsSc6tASy3kGO5__bdv6oDPXdM1UcbbR5mRcMJBQOXfhRI50n9dBFThv0fWFzzNdYJeVeC7bdVtTucxRsxuubpjSVqM3dRWg8Xu6OC70B4B-mhrnNOges_FBA8oAoDTYRLx2VPu_3TnsJ0d5r9dVTzF-Vn2u8EinA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=j54ioV8VR6DzuLDEfFSEw6ZPR0KyPyiOyCBoASsZKhf-CaFyAYQXf7smqVFrDFCjh3AklFtIv9E2DuHc_LAsDw7_K3SCky92DO4ADKn8wCWNzmi3UiomuQf0p2XXV2Vj1nLbhqdZiwi9WgrEIyclvZGI0kW0BDDR0yLm8fYx3IaOezRwVBBtYrfEsD_hiJvbDeRZuqEDbFrCwm-A6D83FmDykd4a7eXSL9wS9tuX-VSTQ5gPgZbgFKenIO6l9MZ2a0BQkDP92kLA2OdsfxeD7aon1Q5OIHBqJtgnOxcGcn6kz8LwZXkR5Tha5jN7tE5Av9XBRLRJBEfnh8BUKhMjww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=j54ioV8VR6DzuLDEfFSEw6ZPR0KyPyiOyCBoASsZKhf-CaFyAYQXf7smqVFrDFCjh3AklFtIv9E2DuHc_LAsDw7_K3SCky92DO4ADKn8wCWNzmi3UiomuQf0p2XXV2Vj1nLbhqdZiwi9WgrEIyclvZGI0kW0BDDR0yLm8fYx3IaOezRwVBBtYrfEsD_hiJvbDeRZuqEDbFrCwm-A6D83FmDykd4a7eXSL9wS9tuX-VSTQ5gPgZbgFKenIO6l9MZ2a0BQkDP92kLA2OdsfxeD7aon1Q5OIHBqJtgnOxcGcn6kz8LwZXkR5Tha5jN7tE5Av9XBRLRJBEfnh8BUKhMjww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا و عربستان شب گذشته
به چندین مقر گروه تروریستی حشد الشعبی
در عراق حمله کردند و تاکنون اعلام شده که ۳۲ تن از این نیروهای وابسته به ج‌ا کشته شده‌اند!
حملات به مقرهای حشدالشعبی در ۷ استان عراق صورت گرفت بصره، کربلا، نینوا، کرکوک ،
دیالی و واسط.
در ۷۲ ساعت اخیر حشد الشعبی بیش از ۳۰ حمله پهپادی به عربستان انجام داده بود.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=en33QW1hiqSWId15tJFLY06pSsvyMyptnze83Lo1Rcbq09VTxjp5M64Rsx2PmDQXHSxXI2VCJFrO8Ow4CjExYOArh9CAxyIp3KaGoybauwGXE9qjxqc3iz7pjFTCmIZmhkopV5rqB-WM0PgXGDJAeptqb6ob5ZnH_bPscvfsyzNEPhf1ZjrW5RozMDbr_R6XVYlogrDvUfmKJ7Wmrd9I0h7HQ6rgpU1QPz6PmMdx6-lLNamG_GaVBSW7tFJTeQfvspVQ7K-fc71c_rLUi-CywA7j-_sYrV2ebM2V733SlCpK5ZtUuZzyZleuIwz76HXvpyOjUXUqK-by2H4YYi9c9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=en33QW1hiqSWId15tJFLY06pSsvyMyptnze83Lo1Rcbq09VTxjp5M64Rsx2PmDQXHSxXI2VCJFrO8Ow4CjExYOArh9CAxyIp3KaGoybauwGXE9qjxqc3iz7pjFTCmIZmhkopV5rqB-WM0PgXGDJAeptqb6ob5ZnH_bPscvfsyzNEPhf1ZjrW5RozMDbr_R6XVYlogrDvUfmKJ7Wmrd9I0h7HQ6rgpU1QPz6PmMdx6-lLNamG_GaVBSW7tFJTeQfvspVQ7K-fc71c_rLUi-CywA7j-_sYrV2ebM2V733SlCpK5ZtUuZzyZleuIwz76HXvpyOjUXUqK-by2H4YYi9c9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOrLGDn90iCdC-m2w3Q_PQa9cwSjeIlP_EUheGuYWBNj0-JyRiifajfO56frs0qzyGWraKwdKycGSbhlVjCiVqMIMkK0asO836f6-B1Fh1B1UgtDD5YAD-ED4pUSxDjH41tI3Y1UBUE80J3oyPXt9Pz9adLp3xBCTxoMN81S7XmiP3vWTpopPcQPCWryAPbHCfGz3rGhekqgTytT6Tj74ohZrRGY6Pk99npnVEsJfJgJx5U6d1A3lsd9P1dg5dRD-5AXrwf01Wnw8EaXVMRsHNYeNET9HZbJaFnkAj0LXvtWMQ6mKcKMHlCEF6-B5nBnE1sTwAAmnC9lxjI7m6_5sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟
این تجمعات شبانه دست کیه
که هم دولت و وزیرخارجه ازش
ناراحته و گلایه داره و هم سپاه!!
کی بهشون یاد میداد که بگن «بزن» «بزن»؟
کی موشک میزد به ۳ تا کشتی در روز
و توی خبرگزاری خودش (فارس و تسنیم)
می‌نوشت : «به تیر غیب» گرفتار شدن؟؟
مگه معاون سیاسی سپاه در یکی از همین تجمعات سخنرانی نکرد و نگفت
: حملات آمریکا به ما «واکنشی» است! یعنی ما اول میزنیم و آمریکا پاسخ میده.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wmn0n5z53h_S-EULxOFwtXGtmorTAtjHtStFT5SerqylZj-arI6Cxa6Ep0Vf6tOBP2-XvH8f2S311vqpzEyEWrlPlN-XDI3AIyLlAT5M69Mbhi60PutsCuvj-sLziXAR6gF3yHpsO0e3i5JK9jx0TxDSTRQySpesQGrBgbJFK0UYryltlvSDBm3FKB4T6POA07J2wwD2wHVZirA1vsGF38-f7bFO4MS-9-S2S6iSUXw5iTQY46yz_uACKxYkWi2FsOpb3I59DweRWEz3Uz6SdiOnHyg_asCD7M6aCpJT-6IYxF8TLp8vl4ZNB5d2CL4NWDu4Z0wMJ9tglI595rjLYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1HaWLGML7JGoDTrEqZGGvR068VqYFAuDSVOJY7dQMv7a7_gfn5wOOVQn9umkdo-H1qbo1h2dbm0U9TuZHDJ9yfG6IcCJiAnwvM09UWWJqEpobVLPHKO34tBQwTsbYpXxAN_g5NX5EmEtFFSHiixHPFAkNIvCODNSjks44ZZlnL-YhVsVtgienoW-0UFpzy1T0FoiWWIF8Y64yfLhyV8FBiJljL25OtuVjdmKD-S6w_DFI9835ssbQKaq00TTxOPXmcZUCW84bYbmyv4BydTnI96tDzx3XFE0y4m-JRVOHFpR-vEldl74szF66HRZHkagX3H243RnorJOt8zX7XvlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzEa-Fw9h93BGXfZpSLKtfxeEAmE32Cl79G4EUG_Y5AMKmLgT9evj6FFxGfAG4DqzR39BfZvy9e6R5bGXQ11I2mf4-KeS4BDcvFjLRzkyuTBD8UQga_0WkWwTUtL3JOCHi2M0DCToipRFhsd1fkfh6iuWt98la2fPS52BZPU6pPjCg0tfxhxqO-vOmGSLD7SIukJ4r1hOO2aUb8djizybfNw1xhdGU3cSmbiu4E_8TURq5lkj4rABVoMGwrUbIp9cI9ZIrfe1mfc5D4ixfGwK5SraNaB5Dd9F7cmKmP6erDHgJvZBAm5H_bDdWiMenObI-bI4-UGBWK1miRR0cklsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JCSM1rMQAw1vh--LvwZuZBbE4L7HjNSfhTnBWkUMMBzRUEGeQwN-FV9cLU1FswMJpXtGTcPZJ3is_ukvapv7MxMTTTmvB6glbWRq9Jdf0hgFlU5GVQDTd5GezbhwlZqedy0hc6P29QkY1bwVGf7bqVzSXezH3KeR29wzh6GTQhIXXSkQ74zrDJjeYLrqnd5DM_yPN82gxT85lNlOnln_V2qhg_UmUqiLpvCc0IOlpUbq8GfulotUF7-0E0ZpVe1873lwLoM5feItKNkV4K8E382CM6RzWVqSHh9Wi8wNWrc0tgnhQpaCFfhg6Y9PyCQ_HE_qjB7JW7iJPpP634by6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FWvbhvukSMk59h5K4RvnoySCWnjbQsuZIc7bNkMBa7Iw1LHjOh0wAVe7iTbY3v3GpbDx0SCNx0_T_SCWFySu1PCGe_HucAqZQt7rzP9SV2bFqH4hbiIdJP5OjKEpwFUezdxisW0IdPLpkEHtcd6tGS8xcFPZLwc9yM3mpMdbdASRKS8amNI6s5sRX73jZ7qZwBDlBZcL_gqOX9O37Szs3F_lVm0Sz1tvGcSKwqr75hWVAkqLKhcc3aWrKl59j0DP02-YL3Jfacik4L3ijrDfK8ccp4u_M3-93Yh6AthgQP3KTcDoTe1nqNowOYw0cffC90N37A61cAM6iz6sprZaeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gw7y5H6kBFwPjh3f3N3znz_E5YRJyKHAyY18bQ22sgyU8PqD1JgEH16q1Ac9Qp81YlF_iUDBqpGt6n1BpGKOIIf9lIkeOv44ab_HhAB3MsryOTgfdlyFcvUlUD22NbRi-xMPKPgJPgaNF3v9mfwhcjGFqvVMNcyAyTyXHNKYwkxnahC0LiPoQS42xBLgzYZvT8KnAdOhuRY3LBKHnJ_lAlq_0Ag8WbjemzMFraPAECjshYlPIEiLO2rhZT4Nhbdh5UY8ewWP3ZX8ETl6HOe94SiPE96Xqjy5TUWIIxX_muAmyiA5WgHA4wDEqxS_x7KVJWNepGNQRHeqtSCpyajKHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tUGAOsFAbPA7v9Bhu6YTt1TxY1NF22EbLFK_GxWZLPORgXpwfjTs0-ZhCQiax0F2DmwmQWA9H3LhZGqoJHvIEu8W-v036Zq6oTx0xXpli4FyyVzgJ6AKP35vRvxRJEmC9mOawjLFwblV3IByJPLwjzjvqCjh3wTz1IL-phUNZN--edTw9CI28vUZ-9RHSIr-iMSLOAUM55c7fhwTrvz9NN7z4v3TTybBBuRSvx8T9wr4f0WfccEDMwQhj88BOZxf2jhfkXI0AZkK-cxOSWglEj_MnNdY-m17mZz5natACeDyLfJBQaUoFPmoKBxc99vtYyTPJPrqHOrrJUBuQSYc1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">میگه ۷۰ سال پیش ما در خفت بودیم
که وقتی اسرائیل به مصر حمله کرد
حق دعا برای مصر هم نداشتم!
اما امروز باید خدا رو شکر کنیم
که از اون وضعیت به جایی رسیدیم
که آمریکا و اسرائیل مستقیم به ایران حمله کردن!
اینها از اینکه به مرکز فتنه و جنگ تبدیل شدن
احساس غرور و افتخار میکنن!
امروز با مصر قطع رابطه هستند
اسرائیل و مصر دوست هستند،
اسرائیل و آمریکا روی سر ایران بمب میریزن.
زمان شاه که در خفت بودیم هم مصر با ما دوست بود هم آمریکا، هم اسرائیل! معجزه آخوندها !</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5jN24SQFLV3nHoRo8YyVjFlPvj3H33C2XM0L92BjXbwvxo5BS1LlXHWT2X6SV5YVBDcoqf_dB0QtjC-aV6HnYDPdK6dLuZ8vKt1vtgzPiFoU9uMhfOpBkOuhAINfWBx1wy3tzWotFaCyJsWMeIahivdHYuZqtzqglA79dBy8Sce34mFkwpUzUenVUpIZdIE2aqbMiuyNWQZHdTtBfzytwa3LLMWLrxWDZqm8kLVEAAjgJOPwQal4hzGtpYXNiU9bmqXHLiWJ-_KitBY3y1W-HtFJ8FKIWkPQXVbottDjIxvjQTBhcxGZtlxrc0o8jdK3Xb2ZPwaQGFNdOdxVVl7_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oqqx1heAjdG4Bon01ZZCJDfSfHQPfUu1AzFSZ8ODhaPnV5C8I3YRacvXQ0vbkB05Ej92oyYRpvD3uviB2blfGFmOwQbje_PXbIW1-OSRgZl8zgQ0Fu42LjsqQYKsXQQpvd3gHZ4K0eO7VZzh42cEMkm3C5LXMjh4MYbjve1JEEGqUl1SJvB24_zMkFUZ_4zsvK-CFI2IGVeFVQKruoL79vhWsOfBePTkqAiie_LnyzKIWN38SdBydk2-doOugukfcrbOfVfF329XDnd0OM8iDpvqzvXeM8RM00M7HdsBq4CE0eoLspEaCUqD4nYqVjB2CFyvxWAyBuCyuUXaYgLn0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=hXXPy3co2qLux-6Xh2Yu2sxWdUHw2J8tVS4-BgA4Iwj4k1DFE23bK3gvmFE3jaTG3JVp2I2uXGAH-Tmq5tFfST1dv2n0xlKNQSKkwm6cgFVPoK0Nk9bnqR7oIugm5Edj7hELVWLodd8Ucx4RPEbaeK3ShHxfjg85wN_ywZEb-TcQbmPubhnvu69Ksg5syqxmhmgzCb4u8i0ydNYqw0DeAloN2UQ0h-jt9yeLEf33wK9SEwXWGiUHmcamgDS-7BkYhV89q54HdnP5oCwODOl4zK0yyYyeXGB_-rHY5-ptPT_i2qVN7TInf5AgJrqL5gaeKJWbZ8OzFALNMbUftOEffg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=hXXPy3co2qLux-6Xh2Yu2sxWdUHw2J8tVS4-BgA4Iwj4k1DFE23bK3gvmFE3jaTG3JVp2I2uXGAH-Tmq5tFfST1dv2n0xlKNQSKkwm6cgFVPoK0Nk9bnqR7oIugm5Edj7hELVWLodd8Ucx4RPEbaeK3ShHxfjg85wN_ywZEb-TcQbmPubhnvu69Ksg5syqxmhmgzCb4u8i0ydNYqw0DeAloN2UQ0h-jt9yeLEf33wK9SEwXWGiUHmcamgDS-7BkYhV89q54HdnP5oCwODOl4zK0yyYyeXGB_-rHY5-ptPT_i2qVN7TInf5AgJrqL5gaeKJWbZ8OzFALNMbUftOEffg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=JzLpmiHNQM8bUNYxV0pNyNN7jobtftdFHf0MqAx3UOc1F2t7yzPu9DYCIRuSUyBOTTt6LFR943VgI3gUGkz6Db4jhId1EQHQbhT6SUZc21x1gZ6vU8Umgq6RpkQmR9YKP6pbmVCQ7V03j_r_rqWkVKE-g48RrStSLqmmwtSpweRUVm9Q2ZFqPx-wSKDMCNes-xqilafOoCgOkl8p5UqQJuGEvPeKOagwxOAhSMmrOQlr1TH77uUtV6OVEuez0tZAngG6U-PXlQBmUpJdp6bkar4TaKv_8xF4pGa6ed9aTHQ0SRmX6r4WwHVPXluS31BBWyfiloXLnlcQVtEukLze_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=JzLpmiHNQM8bUNYxV0pNyNN7jobtftdFHf0MqAx3UOc1F2t7yzPu9DYCIRuSUyBOTTt6LFR943VgI3gUGkz6Db4jhId1EQHQbhT6SUZc21x1gZ6vU8Umgq6RpkQmR9YKP6pbmVCQ7V03j_r_rqWkVKE-g48RrStSLqmmwtSpweRUVm9Q2ZFqPx-wSKDMCNes-xqilafOoCgOkl8p5UqQJuGEvPeKOagwxOAhSMmrOQlr1TH77uUtV6OVEuez0tZAngG6U-PXlQBmUpJdp6bkar4TaKv_8xF4pGa6ed9aTHQ0SRmX6r4WwHVPXluS31BBWyfiloXLnlcQVtEukLze_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=PdSoe3g_zEOhU8ii7L0rwlL8KMFWgTdHqAeKy3gMpMwxBDiB4LAKeKQwOzvpjjmAhedh09FS0hcGC3Z11iNbX8BA5ocFvmEkqisk2BnfZEVyYCvsLtwjWb7njh5MCs_cV8skC-sLvgeeb4MUlCeyI04evpp5ap4PWZi5Cfm8n57FqCw3a6RH9rpOxG6qCD4VDE97l_Rb4A-MhGMJ8Y7Hx_-SsvESamR5CLz1ji31xY7da2NGEcYfjP0Yj51SdnzJQxUZHgr7zDCWIV4ElNxfKFd-8fQKbunHa31HPdIWKKKdSIO7FDcAeQHLrkRjrvrYNL9ZWiZUU24ZNNssH8-XpBAurX2iJBwqpwO9ay6vSt5pbZEX2G0wP7TMjwxEVd20qNTLhzFKHGgE3bOu-D5Whky6shU5HBXanhDAEyvVRt-QZ-hNhOSSwEj04NFNs2Ty6frll6sN2xPMiJtk_x7N8l2gorptBpabFK7d8fejtzq03uHRSyIJSnHKQuqa6B3N-1O1cbjbj9ePVhUKyGLnwklyCEdTuHbO4ltkdRwxtiVwmvCd6C69FD32dPaIZjSTDjM_C3eq3ksC9NUfaAHnmu2QkNYbMq9yTa0D5_9Rjug8ejqz2PZpBSDy1ibxSjMT1NK482QSjr1TPsQ_YpK-rwGcrflSjOV5LYCRZa7uUNI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=PdSoe3g_zEOhU8ii7L0rwlL8KMFWgTdHqAeKy3gMpMwxBDiB4LAKeKQwOzvpjjmAhedh09FS0hcGC3Z11iNbX8BA5ocFvmEkqisk2BnfZEVyYCvsLtwjWb7njh5MCs_cV8skC-sLvgeeb4MUlCeyI04evpp5ap4PWZi5Cfm8n57FqCw3a6RH9rpOxG6qCD4VDE97l_Rb4A-MhGMJ8Y7Hx_-SsvESamR5CLz1ji31xY7da2NGEcYfjP0Yj51SdnzJQxUZHgr7zDCWIV4ElNxfKFd-8fQKbunHa31HPdIWKKKdSIO7FDcAeQHLrkRjrvrYNL9ZWiZUU24ZNNssH8-XpBAurX2iJBwqpwO9ay6vSt5pbZEX2G0wP7TMjwxEVd20qNTLhzFKHGgE3bOu-D5Whky6shU5HBXanhDAEyvVRt-QZ-hNhOSSwEj04NFNs2Ty6frll6sN2xPMiJtk_x7N8l2gorptBpabFK7d8fejtzq03uHRSyIJSnHKQuqa6B3N-1O1cbjbj9ePVhUKyGLnwklyCEdTuHbO4ltkdRwxtiVwmvCd6C69FD32dPaIZjSTDjM_C3eq3ksC9NUfaAHnmu2QkNYbMq9yTa0D5_9Rjug8ejqz2PZpBSDy1ibxSjMT1NK482QSjr1TPsQ_YpK-rwGcrflSjOV5LYCRZa7uUNI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به این سخنان «موسی خیابانی»
فرد شماره ۲ سازمان مجاهدین خلق
و جملات و کلماتش دقت کنید،
اول دیماه ۱۳۵۸ دانشگاه تهران.
انگار همین امروزه
و جملات یکی از سران جمهوری اسلامی!
که داره میگه
«اگر ما اهل چانه زدن و گذشت از اصول بودیم، امروز خیلی عزیزتر و گرامی‌تر بودیم.
اکنون هم که وارد این میدان شده‌ایم
باز حاضر به عدول از اصول خود نخواهیم بود.»
یکی هم اون وسط فریاد میزنه : یا حسین!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEV3Bpe0JklkOVokon09TGalkBtYUG1Fl0X6Y1YsmZoTZ5Y4x5KsSU3YosdmzdYD30XmakJVyfXXNNcLopdomqokbok9ye1dqCNrrkHsqY6ELdFbwqEOXKqGNwST_BWG6E6lEabTUm84TYlpgSqayVs74e8BfrEOzsudtX2gS9W8NS1bmCFYIueS_T5OZ2Q37lPk-BCEImGFrW-mRtso9TSJ5hPaRepycpCuGWUpJiWDy2QB6BdtAIuzmlypZlK1RxqkVmm-g-O5VsM33KAiMIyFsDWar4dL_7bBBP0bliuwdNAdOvI5RFb_MLOwcsHhHWeKT8x8owFZzB9cykhX4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=R2S5ItY2kvhTGYTU50v5Tf4xvgEHRomVqki-OmUy-zYIhiALOWQ0qq9ZbFtpZOHmJGdk-yQ5nz461CP5tcC-iIf8QCzxwZbhJFN314E8FsH3KL8D_aaRPi0plj5unZBi1c0LbAXfggBaFGvg-zMHGnb17F-1Hc2A9ETtU-XjKyydcf0npcMfIyPy8_mz2i162ZmNzDS3YD9ah7UZR9VOdXJkV-55sI71MIUvBmPx4HkMpvl09wJsT0676tMjkWpzohAju_BBEnfQgxtz56yL9uPfdz5P-yZBEJn1ai_5KDnWCeUkV4YQGqvCRnloZDShyPT3pbUeOUTq6-6WRDWtvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=R2S5ItY2kvhTGYTU50v5Tf4xvgEHRomVqki-OmUy-zYIhiALOWQ0qq9ZbFtpZOHmJGdk-yQ5nz461CP5tcC-iIf8QCzxwZbhJFN314E8FsH3KL8D_aaRPi0plj5unZBi1c0LbAXfggBaFGvg-zMHGnb17F-1Hc2A9ETtU-XjKyydcf0npcMfIyPy8_mz2i162ZmNzDS3YD9ah7UZR9VOdXJkV-55sI71MIUvBmPx4HkMpvl09wJsT0676tMjkWpzohAju_BBEnfQgxtz56yL9uPfdz5P-yZBEJn1ai_5KDnWCeUkV4YQGqvCRnloZDShyPT3pbUeOUTq6-6WRDWtvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jp0lsq5SxbZRFAS1H_SELtARE6Ug4-ZPmrnW0UJC4pHNGaV29oUPWQ2vanfcecbcvdX7SfCUotgtrd1lgnMWEAs1oWcae10Yca6GXvjgQ4va3hf0KnJ99tqUueyrsLseDAGBG5xf5GfsSWa8mefB4FGRijwU66oONv28m0_skT4Qs8gHH1B-gjQcuklv2RgRJbOI7dzY-ei_3GvzzJYMaxskZY1I3jxRNE0JeUhvr0jqyP6ZsDh96Gd3a92lck156g7Q_sqlFthQTDtCxpcO57nXsljgKQYyUvNJQAfRxY9RVM81ejEky1TbjUF37nc4qX6idHR5WeBZMDpE-QgjKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sd7iqjKvSjUZ64Bd1-BuX5ZY7IOGj4UthKkecCxLJ9kEsPkdOHPvDi3W1BZZpRc5a5cCBltQwv-ZnlfLGXFV3Ug1g9mRKhbbWBFMYZsaoepOUc6xQAnBakpddkW_0jo7jRPl2agvIy5htP47DFb2XA6qNvpw75emM-lrnBaAXnjGpc3tWLW2d9l7Q3KPMpZcQu2RKly1s-fkt5sXOK4-TYw518evx38mCxchBqP0zymPoQtP0KIDDFPH7Fdr3svrU3qOPlnLoCtiekHp4vBjZrFhZsXAE10MgWxuHX6bu13pwVsbtiVxv7Bw2X6GGL5gzXOcJxnoZjSAsMs89m7ndw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hO12xftW8vbhUrCWe8xCFiMwhrqKgYnOeiI3fjmXej8jh-pseDMMwuBIK8dwZyEZn7Dr7_NuCd3HCXs-icf_7B9XXr3Wc7EfLlPJcwV68aIJGLi9TNJXKKcm_dWyMd3WslBtBwT6OVsceR5574KfwZXYOwCVgtTrfF4MT9a5m1SArnRY1nLJYRAzkW_HPLnoc6ijAnlo39ZqjzHTPI8dRkVQEXuiq78pQ5HNB6P8RjHtpkJOUYPOXEI8CIFrHpS7Ei3FjqIkL8RLS6IFsx7d-yKyPaR8K4obJ1_dF2qUdc7aT5BrdEo91Q6u1B6XISPo-S4g3ox3o4wgzLaZWY30PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cwp9Nhi4-TU0DLv4V-qcYrzQVPoAKCyK6-sbcs-jx0j_dihzxE3spHreE7BeidX7iYoMHsuuyjjJQeAzKC7U3AtZr1MbkAMF5sBhf9nB9FypLmx7UXhKXl6PkfF97Lbnr2ikcU_8_DbMQcpHJoshK2oRYXrjGSnH26xzu-mSvJK9nREGKo8KX9DsJ-JvGugDDgJ2-qmZVu_UPt2wvCZf8YcpUkckcIbcf8RFAxjbMHWFEfyKZk_7--nZ3P7DRaUTf2077HHxFGtti9AEg0949EGejhJfseUqk5-XlbOJ_FUdedQk9VfQGUq-3zuJ88lEvy6OjsC4yWUeey10DZ8ozQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D7jyq7AFq9guRe3ncs5mv-H4UMuohB7AIpFwv_O-CvXO0DN8KdXEt498ruvg86dxQZN9Q3IJulqvHJoA7zdH0WVOBKxHYWwcHH_k5HWHyaMJ7wEcKtaXS_9cclk87N3nPmtVneh3Zl2VMeFBoObuLBr_aPJTWbgfXFaGCyfJodl7qEdZ4qfuke9DIbe6bkaXl7SPQKk4mHb6bZ-XIGtWdNFs1kAvBffgBFGGWNgHCMZYapMQtn23Uxohuo_3M2RwX08S-KrtZ41e-zbFSuYDA2_4VZCe1gQNWoomMyHtC24FWi4FNOayhttzSbhw5g4VenbFfIs6RepSIx8gh8i-8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYvVKY1u_UDRqJCC260NNeoE-SG0nq6OSnWj2IwnjdCrcTt6FlzWKwE1Yx0c7J9CVERkuKUKXFRkRSE_-LQ5v-jAZC7QZPBwTXg8DelVsRbx4BIRe4K0hXdBbwCNuvO5Dq4eDnxmK7mUrk83UcY55AbUbvyuzlCSUCuZyjA9_lzdh79_Juf6p51xRavbzbLOAHxFqQZqFpZ5WRcfhzdNSwvvUBM56z0NgDfpDiFmWrG6uAoKtoh_cikclpA0kcPafdl30OxPeb7TT16H1aogvBXxKMW1SsWlSDCsJ2xOVdxAOtjokFc1l5OMptYRpld5xMqGo1ZCU-5Ke7rNwfzEYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LrnD1l9H8yUEph1yIJZxX9b5GhK78_d7jTybmzo6ljcdSlMw8S7IPGN95jBmd3Ujfrs-HOSfLQ7HnWWRw6YiHbI8xSExV_A4VhTRxCF4EXmJxPrhk_r5GhxKPwoXUd-veuin20Sllkj4B9_dUyvljwTLNWTH-rUEIDDUD9gP7ei5RYcVHaX99aS8b07P__ojN--n2hm0OnpwJCbPEC-k2u2G8Q4QQ4pGgSzgoo3PV7qBO_TPT7zZUcajYToKfEdlva_XUtUNSatypFSCz2xfm6iE4tH1o_H3PuBN9JkJl2nulu7vaD80rFgvo49OR4z1XT5AfCOivPEM-xJjuPA_aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X2jVpRwfYHNLQrrD9aaHYNeqI8AZIp9xUYIrgGaRm-1VEVojcnuI3jRPcC6y3ZFdZUyP2ZLpL-Jyt6xT4ZsIC7pN0K1TNIyWrjD7Wjxg0qrLEkUQX6jZG-v9ZRmcw2XPpUEMDiPHXUY2dyzSVyqVYjj-4m67n1iUB2a9DbmCN9RtgwQoVwYPfKYIlNIhMAYv8kuFF5skwTaCQvk8yRFhp0DKYW4jV4hx1Pl2a62b2eS0Ln-so17cKcBuuCwNO0Q0iLJOHmTDL4lQ-SxfjoJqnIlT8XRGv0PJSyrIBXt1Cgc24SA1t7jfFHoBqgdx4kkcJ2y4pL_9i3ZdI-NQGd9Yjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bnzreB8QXzJpt__4jpEbyqOrz9Y0Wan3_VmHKhqXyEPfD1SnyoAUMLtFqoiLQpbB5ovM83L-t92FlpiZ0gXxRuo4A7d_WfdEIVLhLlvmxWBpRcF1hHoV4uKuLbSkUscuQWjVXYkjjxc4XRL3jA9YwZg96B89tFrVq3vFltgLpT59r0SUhHNqHDNuyglCg1rMm5N3JdvcZUODExSESPhSPGIBHxbtRfdCA8T2aXf6OjTWBGHcj9QlBHm1XVJ37U6SPP_bER5uvt9SjvPJiietoRVYeSyB6iBdSlMPLial1k1pZk2BwHUP7XqxYjRFkm0a9qYcSOJbqrsf0Q9lTVp08g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AJi9jGf05YbV4XGan881POrUWJRE8D-eBmDfFg0wRgRKuJLFoxTHNTHKEiOPCBe4y7NVk2pu5OMkbWJiltLgLBZTnn-xW4hWQ1ivW_BW0aKuCq_6UFdoMT7JomPCRhdJE5FjXVxnlrrh9cyr1pR6hd0vUpwtuaB6sp6Nn6cKCW_YY2WIbvC3yWLGhrLHmPYoqABUBlp9q7-tAy3BC_Rw2aOfeZIJSp0901QWqb_UsqGrHNPdn7T8ZEa0Ap1QS_76p7QgLZ4IolSJUc_2d1yjvP84eAwpJ8qVCWaW39TOQR3uK8MU7MipUWNWk6Dq7o9lZozibPr-cCfDvjiVlkIY_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfyS5BnLFuJmchkBLu1Nqj3NOHx02NagQOUrJ0hJCFydUomo9zSOEsDBR8QuqGt9xr74esPrCdJ-t2qgXYoL_XrOf_Xdvc3Nv6UqC2tK2aKKV0czM8V9hjoUnlvmSUarpy_5yRPIRZbLH5CfEi4gzGz5eWnQF8q1r1HG9AmXi-Na69t3WLlL_QVi-bvmkPsjlXWd9cKVn-EbxSgDOJL3eLuMwsx4nFbTKT2sa4RZBgZfMn1yOyhdkVEjWxR4LfTayG7bEMolA2GtortjRBgNUGWCRwhPgEvDIbv0YRNMMQbeNbBXsgTvu-69No8P3LWx2k9LG1GuUpzKKpfC6fhkxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLAilGIhN-GT6RFM2REeR9eDnnf7TtBwEhlGxWF_ALmwIYqkNh1ILlkXZVmvjXK0iomikik5lg_bh9Bgg6pHiHDvOqN1E35QXyEOFDkuDAilp-4RlkBRouByXGRoiOAbbXfxIEjwHVsb5lq4pofBRSMyd3uZ0Fmg8lXeTbvvAjHKUkusUuz1uEdvobVeO7cemKT79Jjp9BqyK0g3SgK0urlgPNXLRtjQycjFXzEj1owGOrYYJXzFrBNr9-H9hpHy8fYnXhUBtiikxE2F7YS8lVxKmWGKPxztZC3P3a2FWjWnBoEHgpzdzMt7zroOcRuBjdyhI1EH1VRaO7jLGJvStA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QEvNaMusHekUSjptZIp7SZZ9XPdbpvEUFLDNA8Pk6JsH_xSUNNP4wakcNsK2QkwJu51PU-KStGpL0C4h9AusY4KRPY9unSG2fccM4qFwDRRjmOklU8ZUzJrRBFx849phv3426e3iCtEJqX-m9tk3gdidhbPbOx-7FNETejshf2Xx-ZGIPIK2o0Mp2KyE7Bqoz405ViVuL9VncEzmRVQYsAKCiVHyO8Xnlx-HwOoE5oQI2ZTt-pWtZYpvRUIxkpzief7VVwvI6cN0Bc1O_oHgSsXlw74UMVm_gfHzxcRaWAATk3O2oR6Dmt9TafVeT7edYqiDF3jvUdajCwzvavOBOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZFwwIAJ73gubV2ZI-XD85w8tBnsYjTP5BqVFOylSfUJU254hwGVG_9gqPh1nDBxlPVZf2WcePs32vdQJntAxoZg-L2u4C_Y4Fkh3hmB6O-l1l2jg3gF4ZWmG887XoHGD4tzJoxyPbGATy-uvJY2dvuxSCjntBdhbxlPOZz_NQoYPYuZT5BtD18CFUXffat2Zfz6xL-xii24sjwnAaKuECgQFvVDLCiQhv647VFYwngdUCLiYOdmuqwxdkjbBA34ea7jPuFPFOvzsSlKDMg9U9zmBzCSHJeiC6_b09M_qPxdjkNrcmAKdAMNxKqqMS05C0Ujcgqp5yT-Kk83gM61jA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینکه بارها نوشتم، چپ‌ها، با اینکه گروه گروه توسط ج‌ا «اعدام» شدند، آواره شدند،  نابود شدند و ماهیت سرکوبگر جمهوری اسلامی را به خوبی می‌شناسن،
اما نوبت به تقابل جمهوری اسلامی
و آمریکا که میرسه، یهو مصمم و قاطع
میرن کنار جمهوری اسلامی می‌ایستن
و ازش دفاع میکنن،
این یک نمونه‌اش!
به خاطر اینکه برای اینها مبارزه با آمریکا
مهمتر است! اولویت اصلی است و اینگونه است که جمهوری اسلامی تبدیل به یک متحد میشه براشون که باید ازش حمایت کرد!
و این روزها خشمگین هستن
از مردم ایران،  که چرا کنار آخوندها و سپاه علیه آمریکا نمی‌ایستید؟
تصویری از پست ایشون و یکی
از هایلایت‌های ایشون.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

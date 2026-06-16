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
<img src="https://cdn4.telesco.pe/file/ZST8GQZAuGoKIuxjVOLrbtnEh3uQLdxfuR56-qfImCCcl5kP7H3GM75I_bUzFX45dIVegsX43X38u2d2JKVKRcg9PsMgrhDv62q_X_yrgZfseSj-sJErCUdot1hhgdl8OLl7uFplRqAIE-0JE1mZJRQd7ssKNpVyLNghJv-KloKyDsSEbyndRQLbdGKDR1tGK_XTSU-kPk0xX9Iu-aoVtgWcWIfcvOVuFOBST6-7FWt9lQh2nepth3nZEFLIrZ6Y09LT-V6l82zQk5Y9GTMKO240WoMOxIi9OJYHeUQcFqc_-Lz74Denl17TwXLJiAexc2zS2a6paYGZOC24RAAerg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 301K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 00:53:57</div>
<hr>

<div class="tg-post" id="msg-23638">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmsALYl4i53WYrNZireDeVruUZ3Iq11BuzpdEX30O8XG5kuHWO1-spCwtCEmDbczaWBnbqNDsuUW7BpM71WoNgobIQl7Q6hE5TKFq8D39fZdcWjFWlRkOmRgEx0ydGMeMcKgTaj1xfZHdIWmLDr4LzS0xceMTkUVrSv_XTqSKhS1CqSVJK27lu8YZSEOWSZUzZzWkjWcXF1X2l2CKMbl7Tt67OPH9KDRD56phXyIxjQcFc19kKFM5TwYAiB6R6LU1dpFIpVixq1yBpxfLEhFLnEGM0VSbYImJOMWxTPxLBRtebjHK3XaQPsE2X3oNr7OSacrUM62Adso3w0UJfwwlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#تکمیلی؛ جدول‌ بهترین‌ گلزنان تاریخ رقابت‌های جام‌جهانی؛ لئومسی و کیلیان‌امباپه برکورد تاریخی میروسلاو کلوزه اسطوره آلمانی ها میرسند؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/persiana_Soccer/23638" target="_blank">📅 00:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23637">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی شیرین و ارزش‌مند خروس ها با رکورد شکنی کیلیان امباپه و در شب قضاوت درخشان و بی نقص علیرضا فغانی.
🇫🇷
فرانسه
3️⃣
-
1️⃣
سنگال
🇸🇳
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/persiana_Soccer/23637" target="_blank">📅 00:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23636">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JX1lM4I1Ydk8W12Q3cxvr1EDWr96qlHTT9UqDhBv3r3vtgXM0c_6RzSf63kC-SFVgdegwM8MDe3-qoSp8lsBgdSiRCYdEB7U71eDlmiQz7Pl9UcXJI7214-K78McmNHBs4kPEFxDB9s75pkg5Xatds_ocZlWjcAPHMCN82nmk8og08C5nlGc6YRjAzoeErzA3rRncUKiDE5CskRc3hoZiHuaW1HJSVK5XFdl867lCTSEdvEt3pOYiVz37vqOSIFF-tzrsyfWU-QAvE3YPbgfLqNam8mvP1Ypw5XzZ9tAZzPX6hvME9597IbBlyCIvGqdPMcfiCzNhIuEtZ7FSoZZ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛ شماتیک ترکیب دو تیم فرانسه
🆚
سنگال؛ساعت22:30از آپارات‌اسپرت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/persiana_Soccer/23636" target="_blank">📅 00:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23634">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SU5195ByBIiWY-syxCtVwYFkX1yH6jPY9a_-YTBKopYdbxkY4Ga-g06G8_Xk-47G9sorZ8OImlMZpJ5Mzr0YSw8afOpZVQvZZO_eJu_TkygichMKwM0O1LWzvj_Bsce-qSWK7xPirUPFWwPXg50UN12JQtQoOCGTm-vq6aUJFB2O7iAjv-1cXHcoS9dbwP9sGAqBIvMy9FBKNviVggmkk7BUE6AJj_tbSlmI5LcXC2QXaoT8GiuwmO8L13wjkIg-NW73YS9rO3SW3svlTgXlvWVo8M15IfYa6EXYaaqZ6yur8-Nmtpo2uCL2_Kv3ROCkMfoPhgYm0TVholAIvyn5Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IxudeaD5fmTteB3Pfok9h4XTBf5vOlwgoySJyH9dkklWJo78RWiFXMw7ciaJbB6q-2lHoQk-o8Awok7eaPgnfrvig_IPuv6JhRkhmX_XhzzAwqEoUKLScrgKJziW4Br0Utw8Pqi16xae4u_302RxmC1UcJ5dyaP8xW5yw6mFtWWNYKmxdb4VETCr51mCogSKKqHIis2SEdGXbgubF53KHuAj5iuO8tlH81ayFuQYnB38INrZO5ghAB4jcwz0mVMwH6hPU5WZAb_inXu4zKCPAW96f1FQixVGdMh50qjoYchmqVPso4Ge_4hxzCTuxO5429wQc807faBfbaC8kQJt-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی
؛ شماتیک‌ترکیب دو تیم نروژ
🆚
عراق؛ ساعت 01:30 از شبکه پرشیانا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/persiana_Soccer/23634" target="_blank">📅 00:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23633">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brpQxMJbbmRB4XkYpd9PuI9WiEMk7xxWMJgZy4OmBwdPT9Rm422L2nWhkw-5rlD3T3vZ2eLms9q0udbHRaWDYUfloRH1l5sKtphQDf4gDMG9BvfVQ928i_b0LQ8nL_FpavnUEFoqyB4WIr_JyP-iDyLJ6q3CYAkU8bF7syDpfiD7Hn7Yh0UTxHFoVHOl71gAAjLSn2Zi4HZB_5X782D6lnVT8nxdwSslm8xo5EAgiMcugpkNz9Mya6q4RF0NH34GuRfJyDWNDzRUT1hFDlSpR2GSBVBGOaXiJDMCR7_5l9xGp81ecK-SnEoAF4uKWeaWuYzKdnBYJ5GS6tVBzk59NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
شادی گل محمد محبی که تو رسانه‌های خارجی جنجالی شده و میگن احتمال محرومیتش از رقابت های جام‌جهانی‌زیاد است! زلاتان ابراهیموویچ هم که کارشناس شبکه جام جهانیه ازش انتقاد کرده و گفته همینکه برای تیمت‌گل‌زدی کافیه دیگ این‌کارا چیه که تو خاک کشوری که رهبرت رو کشت…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/23633" target="_blank">📅 00:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23632">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2uQ63QXbRiIVYa_fH6t-MeafEKr51exMCgSb0SXTuzX1xk_T5PnvNzfDdxFm_v_49GXEhXHACLeAgmWeds9FFB9Q8F6z6uM0wWo_tiTzy6oWad2g-QnNZHzmL0KUJdWOngQQe1WFgwpY9abqjsUlaKwJhkUKiozEh0WhdkrRiEas3DOzmSvvu40A02sEao3J-ckfHa-oSHcE0gsJPkqVfeGp8K-SVhMqapnUhQUXZnQ4rGW-Y4JOyDizBIVDuWr9JdDUVXDba8kKxQbXAiBColxc21V_fnRMT-tjSn9NUaRD_K9xsLNZLIxwyDFtaPld9nUTXk7UGhRe8e9cv9APw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/23632" target="_blank">📅 00:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23631">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsO6Ax1fGHQk6kJm0OuYBe9uDL31YSObZZtSoN0felhs-8d-vBDxsVttKVmCj0SHCGIzCi7VNPoxqFBFWfJ327Z19jnbJZciWcLNyTgZgWLBk_bGP_Eqzcnp6W9YU4864V8nOsJtVpIQZCNa3HOPsCVLisRj6BMTkghXV7s5GDSLzcDYItHzF9nAFHlRSzny8YhIrhUYe255UttDp15v6BpwDzpFRisKNfNW46EQL_ou3R0gWtbgsjfA5u4D3EWM4WnrvmMchL7balYrDvAQ9yOOG8ag-WEcU-7KyaL0upemT7e9w4W0tFghYoSXFG7u9kteWBGXUSLNgW69cvVNmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ به‌احتمال‌فراوان بزودی شاهد هیر وی‌ گو رومانو برای خولیان الوارز و بارسا نیز باشیم. اکثر رسانه ها و خبرنگاران میگن که نماینده آلوارز با خود بارسلونا به‌توافق‌رسیده و فقط توافق با اتلتیکو باقی مونده که با توجه به فشار آلوارز به مدیران تیم اتلتیکو…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/23631" target="_blank">📅 23:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23630">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlO60K9M68Zk4PFwZIhLQ7E4ZfatG6n6I3g_uKsZh2KwMY_UT9kzC7D7eX95w0Py4jkERmkC3PJbopRFd3s6kpWTZhb7cMYriHYT9HHXd7ybxcwQbbGWZLf_3LHBmfxYbdsVfdo79Wwxv4382M9mY_3zV00Ne6LwquTnBkfeQtxp-VBGismxKZhQkrO4xfnAWXXYd63caGg_gFS9LqIHUsCKhnBRTeDuTey1gEfbxsHPjWqSlOLQ6N3Hb9r5e61v4V0TpTBsdd4ZFqtjPgtRvjdcd8vvsPV3aVBrh2rdp-1Do6-82p6udRsSyj28QZ14Xqhwsj0N1DWD-Ft1FT6Ixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/23630" target="_blank">📅 23:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23629">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f28c9e179.mp4?token=AdxnRpD_dwgifQAHw2Wt8aRRzLvtGITpqczoV-g86Ce6izJ_rlkC5_k_AZMKlC2FocR2nmxjWv278SN9H9VUmREk6x7F33uEppqzHJ_jK_7u_1VwEBp9hm3JfSsWNcKHV_6axSvr9gYmFR5lQspXZV1HAMnma8te0d25QWxre1JNHqsfqP3Ht-tx6kG4amT2sFa-B3ixah_zc98XxxbWs9Z7FRDHnZylbUr59yK1dxuSY3RPwMypPVvS2dpCrQGNzBTjES8iMDq6mpSBFJw4UlUMk74rgQlUuOflzuNCSFJh6p8iUUzdO-Y10Rx593VQSsjO6kEIGBtWMcPC_6tEGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f28c9e179.mp4?token=AdxnRpD_dwgifQAHw2Wt8aRRzLvtGITpqczoV-g86Ce6izJ_rlkC5_k_AZMKlC2FocR2nmxjWv278SN9H9VUmREk6x7F33uEppqzHJ_jK_7u_1VwEBp9hm3JfSsWNcKHV_6axSvr9gYmFR5lQspXZV1HAMnma8te0d25QWxre1JNHqsfqP3Ht-tx6kG4amT2sFa-B3ixah_zc98XxxbWs9Z7FRDHnZylbUr59yK1dxuSY3RPwMypPVvS2dpCrQGNzBTjES8iMDq6mpSBFJw4UlUMk74rgQlUuOflzuNCSFJh6p8iUUzdO-Y10Rx593VQSsjO6kEIGBtWMcPC_6tEGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
تیکه‌های سنگین عادل به کارشناس سیاسی صداوسیما:
هرچی‌میگی برعکس میشه. بسه دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/23629" target="_blank">📅 22:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23628">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftHIMZjzxRW3-zYCe2gYyCwxRAUMBE1c1vUVoyqA-i9ZjcYFhvUJZhN9O_uRWjxvu4DTxMN6SCLrXcuSJH5bJ72e1g6rlNLwLTU-4Q2ABe7biojlCMT7bppcpDlkUbIHOvHVWCCx70D8_e02yB5muGWiltJOsyJxkifJSfPw-zRa5VFVnRW55e8NcU_x09yPae4aqIXzPTg38Bj860anGzLvlP4AgjZgWvWj95_uiIOakBSP6x9SsIJUE3rqP2R9e2o4oO3tCpOhs-s8eGZjeodeyRkK9bJmaND-pD9hw6o0gLs_STkD9Zmmv0kqlzt0pXqlRhsG1zHQgOtR5UNy7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی|توقف شاگردان امیر قلعه نویی درگام‌نخست‌مقابل‌تیم کم نام و نشان نیوزیلند.
🇳🇿
نیوزیلند
2️⃣
-
2️⃣
ایران
🇮🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/23628" target="_blank">📅 22:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23627">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdL9tvka0ATga4I3nXl2UPT86EUKKjdMuywjC8NtCcVQPtaklkSrgWVjXtSPs5vld5bUJGEf8PUWELDHRt9nVzFJyi3-YglEhoSPLyK-V5UACbTwb6PPC4BedPNcUlYtrmxoI638sh6eIDTGChtCsDa5o72OYvX8LQUKYzfjPan_8UqSqUsCy83Z2hQEyvInG6UcyIR0jaA_ar6sAouqlMHyqRw-jbBmp8saAMP0LlWVRBkJnx7vQK3KRYsPHwftOCzF0T6SgJUK0YwS3cDRFsGty3gQE6w8nGgIU3_gb5f5_CpiVj-UB4kck5ZL3QpFiwSs3ijUluIKlJaIILRwjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رامین رضاییان در گفتگو با میرر: شادی گل من سیاسی است اما اینجا نمی‌خواهم درباره آن صحبت کنم. گلم رو به تموم مردم عزیز ایران تقدیم میکنم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/23627" target="_blank">📅 22:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23626">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xeyof_msgX47IyAurvfq511i081sJFa8qiRj8EdSusu342nQqBxi-NIC_q1uJ-KOdRRCq25lEn4RfqDuWwWQOkwD5tjoX_cWQPdWnsA_jw_YUk0CO-SMcm0eDlJQ-ZGS62VH_yJ_ONH_LEiGmZxByXego91exENDS85ZAJM0GmIUH2IElQkscpQU5zXxug1CazE0r18jl7cbSAomNW7n26xjDmPSOwzVMK-0wxvE5yXBrV4vMwzwjX5jT7lZkJ8kAgdVHl5G2xfQTlyDOOtGKDhMmVsxWm4yRhxzke3GmHKzJ5UWK1Mmszq0An03CwFDejuIrQOn2n2uWLZNBsbtXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستر باشگاه آث میلان برای روبن آموریم سر مربی جدید روسونری؛ قرارداد سه ساله امضا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/23626" target="_blank">📅 22:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23625">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6CALQ49RQhjnI_GxaP3_A0YJ5dr0rH3bL8hiRxtRMp8gga2XMUqxBYdSaMiNK8DolfhA3ntgB5lBhUeURet47jpjH4E46nnEnbGMTCrpzrP4ePkzPzMhfFYaW5gGyeJQMbF--zLfTVOI5L5fYSL69MiojM0uLJfv4l3-nUAxdyPL0Npk3ttprub7KsXaPoy9Dgg9RwUIPeLhrZV3IGOPoDzgUg9Fdaj4N8OeGQWXIyTbgpxciZuSsA9NFFN0XhkwMknKvBTXrGkF-kBKXjLMmqXyuwTLEYPeUOwtdvT-C7DAEzgH_hRZDsFUD-KmUMQGc7ptrRjgHawDrmiBgUOpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/23625" target="_blank">📅 21:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23623">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uPJXn4yB1BKOr3qVrxmdWPasl45wLrSj2Z8LMXW9Q0AhNPU702OKn5tsa5xKIn_a01Is7P92bWWlV-g7Np_Rt37rCcLO6anNKlRFlVN-Z5fvIGZtuVN2ONLc2Qt1eWQ8tr3HbXlooYG_CRMxy194eX8kGfQZLxkSzy9ipIxc7nMR2FQlCuO9imNTbNC5NR5-T_ZN--cYFCYA_9Qfwdh2ri1lRBejLtNIn5Bph2vmbLEbNcWkmrXHuH9KiZkh7vc6z7PqLP47TstPziCHbWYuw6u-S-kyZ6KUFTAT2nvM68hwBjdgjLNoIwYuzQZJXbDTVWsjVcj3fsBX07Mt4DVBAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5YHMOFPLL_VgRGDgIQ-QJ63MyA2TyUdvh-s5L_oxmFw8yIg08_LdDG7j2wqNk9vxxf2pECfLEfXUfmrk6O7CM9gwbNT0xLGB30bU1Y0DlJnS5ZfhJw-MEbrH8Pd3NdLlO4twD7w3Bykdqp7QjVKFhH_ZaV5J_GoM0IVjfKek1zA2EuKlnTI9PCxoGkxsjgxJT_rbl-_ssrR6kseMUBvCTWPqsYWTVRnGimsfNeq4AkkRyekK-oM36Q-8wFi2ioQ8C-F_fgdssGjbrPDeLD8kHA8X9gJ6IZi88Kv_6tbVEENXrsmd2T4KmrbCFPYHbpkGo8zIvGkNv7WX6Ns15x-1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بازی جذاب امشب دو تیم فرانسه
🆚
سنگال رو عادل فردوسی پور در آپارات اسپرت گزارش میکنه. روی پست ریپلای شده اپلیکیشن آپارات اسپرت رو گذاشتیم اگه ندارین دانلودکنین کیفیت پخش عالیه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/23623" target="_blank">📅 21:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23620">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwUcDN8jEVFXgueHPaPzvA64GAomCIPrjPJr1zbk8WIfKuxSoDgqWvQjcHqwpkXva_1lXLO5xiwYZgyij7x1I3CnfLyfxmpc17pOiqsPp45wlqjFa6QMq8VaWkIOa3QZhmk5vlR4QDRMvKGunt1_2LZaHd3Wv6j1Ytj_MEQ02I1KE-IaH7je5S8rhNvlyXZKpGVhrmc14MY_cUe22b81ulecnP0EMrW-GsUBUZbrm6hoyDN1tRlLmLfRwCzqOfVvAjFv8ucEcFcK2dmXa44_qGPWvVBIAUiL6U44pHCKoJv909zTFNqZWOW5nLa0bvTjt6czVD8ZsGBBBqMbdyVaBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/23620" target="_blank">📅 21:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23619">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2rmGWA_L8nAOt4cHnCqDFoJVFhjZKKgnMGfXFiUcR3mAiyQeGkfHxAO3p2CjkIWjv9TaON2b5NVzCgkbwfaGdNwG87EBtTEUGn-XeAgpCZMl12YAC2AtzklRelGN1S8nT_8fv_FMOBMvDIxQuUvOUvB3kEKklut1WG8Nt19iqsaGwtYxyP2bjkaoH84GLN-JgYzGjkDAGAlctmdxLNqVnxRcQpC05sLcUUzuhZX-vp6fm6FuDUdi_gsjGa-U_XTL4vPDPtjva_net_tNUvTASZN7ngwVLLDHVDb1GLUoNWCEbTwTHlpALbuk2uI4Z1V08YoyAZHSW_i4180H-xMxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بامخالفت تارتار سرمربی گل گهر؛ انتقال مهدی تیکدری به سپاهان در پنجره نیم فصل منتفی شد و این بازیکن تا پایان فصل در سیرجان خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/23619" target="_blank">📅 20:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23618">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/335ba40687.mp4?token=axY_azJ1U4q3oGFEdh9y5xvD6dcB2IJCKeZgLMdZ8pMtEoKT7107b7dK-4jOCmb9V8pv6xw95LHxT8nTIyGGsbZBjwBfDGb8FadMuLF9j40fCbjVTLBM8KY4enrMj_uw3NS44VJSXhcM_z_54-oGuL5UYlizyJMnXWBGZty8AyvjHOakOTLLtvuW1bGCDC5BqmDEQE4iQhxdsjUIZPDOKokqBCjUePMAzCgfcbPi3TPGoRr5IQigXSr5L1tzOheOYYujWScbV3yn3nOXCQ7svUOETU3ktw6x1a8TAsNuEJOBWLhHGAWkuLIgMt2QtNk_cR7f9BXNNas_15w3P5TBkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/335ba40687.mp4?token=axY_azJ1U4q3oGFEdh9y5xvD6dcB2IJCKeZgLMdZ8pMtEoKT7107b7dK-4jOCmb9V8pv6xw95LHxT8nTIyGGsbZBjwBfDGb8FadMuLF9j40fCbjVTLBM8KY4enrMj_uw3NS44VJSXhcM_z_54-oGuL5UYlizyJMnXWBGZty8AyvjHOakOTLLtvuW1bGCDC5BqmDEQE4iQhxdsjUIZPDOKokqBCjUePMAzCgfcbPi3TPGoRr5IQigXSr5L1tzOheOYYujWScbV3yn3nOXCQ7svUOETU3ktw6x1a8TAsNuEJOBWLhHGAWkuLIgMt2QtNk_cR7f9BXNNas_15w3P5TBkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
#تقویم
؛ 20 سال‌پیش‌درچنین‌روزی؛
لیونل مسی اولین بازی خود را با پیراهن تیم ملی آرژانتین درجام‌جهانی‌انجام‌داد. مسی 18 ساله در اولین بازی اش یک‌گل و یک‌پاس‌برای آلبی سلسته به‌ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/23618" target="_blank">📅 20:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23617">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3B7H9xmk3kekKFAzrFRaeq_8jp1cx8CJBi2PuHQrmQPyUrYpQJibZF4WwRVrJXfl1IOPQFDKjgmS8B9QA0lrahlg1OPz7b_uNjrE7yeRgJCslKjGmswYF3l3d6eNMxZU3wGilcgm1D5VYgNedcsiI-g09DUs_-9Xbv0r4gJNxxvdBhs_ZPOwrE6DrWiTtnEsXooEmAWsYN78P0f1R-OK6s69w9xUs-_yPw7xBfgl9KBztFfFaACOiCi6Meh_eB08N8VEH9yOV0bbstM_FBoP3sWH9f7q7dtwB-9S-wCfItP78jxvveccKhVkf0e5eduDxtITZTRGEwqvNu4plZh_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇸
تیم ملی اسپانیا در جام‌های جهانی اخیر:  2014: تنها یک بردمقابل استرالیا و حذف در گروهی. 2018: تنها یک بردمقابل ایران و حذف در یک هشتم نهایی. 2022: تنها یک‌بردمقابل کاستاریکا و حذف در یک هشتم نهایی. 2026: توقف‌در‌بازی‌اول مقابل کیپ ورد. دو بازی بعدی مقابل…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/23617" target="_blank">📅 20:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23616">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPzmOas3jpESLGJqlYtgoP-K8yE3ldLacMIoepkC2pXWmGKdHHBzVrBiixVfXUl4X4FT5V4gAlNnRcdLEEgE4q6N3sHCiAgBRrE1x3IDqqDhAalg77AMurNrTd4tzhPCabdQ-WQ_zJPh2yUnj6l9ewp65nRqZY2Z92yNHbec_Q_NOXi3xzCTuH_bpKz7cBXQqbrwUh6XnyFfPoDarCamMpEE-3LR52vnIqrXr9m_tWj4WMP-pDDWHhnEft4dp33fgWNJGhTPK-3gWsYqj_AA-eNyI3hCR6N9ZV7LlMeJkn-hx6Ehradc9Q7TyG2OhgPul6OBcWKiCVaTFp06oo4qWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی جالب و متفاوت‌از خرید مارک کوکوریا مدافع تیم جدید رئال مادرید توسط فلورنتینو پرز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/23616" target="_blank">📅 20:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23615">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G57ahAZhoEbroXyD0ofi8677z4sjNc2rhLWQVK4T_q8XVRlht5TKhIX6oOjGIFKHrgYv0guUvzjejznoUCO079ErG8arxjAGNoevaSc9ZZjKg0aH2z6PhyE7MJV_evdOfFhnGOW3E8XHLw4xA_q-PQZllNB2ZkeY98xheDjZI-bsRT8Y52mf9LwIge8yEQzFwTzF_HlZ5lGXh2K5aVX4K1EcnINhR3mtoO1t-IzwL9Qrw2lITZf_beeiUUwoPA-OOlhb8qoMqOH2ZACQ-hFzxa81wPplBzUfa-QUPL-83dQkWc-ym426Rf7YpOUCr9qzt8krQRBSNrksx7qDjH5JKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی های
#جام_جهانی
رو بدون استرس و کمترین ریسک ممکن پیش بینی کن.
⭕️
⚽
فرانسه
🟢
سنگال
⭕️
⚽
عراق
🟢
نروژ
💳
حسابتوبرای‌این.بازی در
#رومابت
با ارز دیجیتال شارژ کن
🅰️
🅰️
🅰️
شارژ اضافی بگیر
✅
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
همراه با درگاه‌
#ریالی
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
26
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/23615" target="_blank">📅 20:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23614">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWigVdpuZzF79RSbJQ1o0FN7pr2tqKnEtdg3FtrXho4JRL6iyeoCTvZYBrULmMSClO22SU1s02beGXUt8tZcyAf3GExAPbbfrtzgqTSpGd41lQHAN6hzEYtfT0YfLvDWFyKYVFKo2qDSS_dMkcJQuUB_kZxjlHBMMLjBtsmr30jzAnHMvuu8AcgEAlEo596QCjpmiwbBaJPNyrV0Ct9rOzELCqJ4TD8AXYPXASv0AnM8dl6WTUYJ2-hjGrMTGFn_dBAUmGazOby3aixfHUcVAS5-SgRh7Szrv8wa31ivR9CKWxIXNxTEMWUma-W6kAf_ftgaZb5WNXXorejxMjQ1qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی رسانه‌پرشیانا؛ فرهاد مجیدی سرمربی سابق استقلال پیشنهادی دو ساله از الغرافه قطر دریافت کرده و در حال برسی این آفره. احتمال اینکه گابریل پین به کادرش اضافه شود نیز زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/23614" target="_blank">📅 19:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23613">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw15cSoqqxvH73K5GyDCV4pzqdGBICPvZ8TwQG_EGgqAXRytHZUHk7YylibF_erOxA8P5DbtcPXVL08bxEXcLzcTzCM0irY_LFG7iE8VXAlwTMi7dstjDsWzATNHP7YQdL92psDAYBsU74v67MrHLyX83QXg2c7S7RqctqTMOIGRsNMz9iSAUE7ov9pK-9XEwAsX2HqNaQ30XZiJoPHzvr0u1UD7nwUNqeZURhKr0gtZtgJuvgd8nEL39gworHsXEgkssrbuIwFNfyf5Fjep80MjDxfmei1z4qnKXSQl3K3l3i3PnBqCJ4QM15jygy8F8bWTT6fYFtPZn0LA5Jssqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو: روبن آموریم باعقد قراردادی سه ساله رسما بعنوان سرمربی آث میلان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/23613" target="_blank">📅 19:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23612">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEgCiO7A8U-NYLa-7jrqnVM1PtJOD6rTPYLczF7ILllfAfRlxT6sp4GwSWINJWEAIWJN8VX-YrN-H6UdbIHe2AXNpntfmCFr0bEjVKkIDsDuHAoIqtUSn1yBES0Gq15EW43Q4eIrpArgc9E-4hUQ4BZeSlcWCic5xijyrhmZvTaCLpPdKy1fdgoYfVJAXpKtQfH9sUcCMMBtKNC0bLRsLYXXBAoX4Bu_oxj2-XOY_2RhG4xVydKzt2LKtH0vFHMcotuZK0g3X_5tD3Td7g-u4gsle8eA-v_2975ATDnjsO7mGq12JWip5DseC1fArL2nbuhGXTFJ7DwkCpSNtek-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
⚪️
طبق شنیده‌های رسانه پرشیانا؛
عارف علامی و آرمین سهرابیان دو مدافع میانی استقلال از فجر سپاسی و ملوان پیشنهاد دریافت کرده اند و به احتمال فراوان از جمع آبی پوشان جدا خواهند شد. سهرابیان از ابتدای مهر ماه سرباز خواهد بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/23612" target="_blank">📅 19:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23611">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/328fe52870.mp4?token=vdQsivTdpI661RkZLkxqCew1d77_FLmiae1Wwl0axS9BG9bmlLKOM1NlHRemj34E1OKkaaxD6g7VAB5NISfynq5zaZkdfTR3-XETKUJDjffnJJh44YbowVkU-5pCRNtHSXQRVaOWQyWHNwJl17UwfQxkJzAB06wbHBRa9Q6qlHaJwi6AK3zJgSEXzG_mGdSrIIJSvQroWKen1tmG8E0IQs9lMeCabTHA2qnqKanSU4GS9lDtZGCT1EYfKrDhEHnWsiG6D5dpvStzuRpGyoxURkjJx-53mHvlt0YtXKjHtNKcAv0ps91AhAdI9FRdM_5KlAzPCm8ZrXawwtUFv1AYVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/328fe52870.mp4?token=vdQsivTdpI661RkZLkxqCew1d77_FLmiae1Wwl0axS9BG9bmlLKOM1NlHRemj34E1OKkaaxD6g7VAB5NISfynq5zaZkdfTR3-XETKUJDjffnJJh44YbowVkU-5pCRNtHSXQRVaOWQyWHNwJl17UwfQxkJzAB06wbHBRa9Q6qlHaJwi6AK3zJgSEXzG_mGdSrIIJSvQroWKen1tmG8E0IQs9lMeCabTHA2qnqKanSU4GS9lDtZGCT1EYfKrDhEHnWsiG6D5dpvStzuRpGyoxURkjJx-53mHvlt0YtXKjHtNKcAv0ps91AhAdI9FRdM_5KlAzPCm8ZrXawwtUFv1AYVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
وقتی لیونل اسکالونی سرمربی تیم ملی آرژانتین رفیق سابقش رو در کنفرانس مطبوعاتی میبینه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/23611" target="_blank">📅 18:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23610">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1q09hveSwxdW2LCEFtXUgcqXKE36aSYTiZAGsVkH_PxZ-SPBsoW03eHAApQi4uX2MPhETAvBuiASSZgm9YBf34HHFpWjtHhFiPQBJqrWFOQYbDRgPNtcQ5wJqGZVh44KQqrZi-f5BHWiBYF8HsjwGh-z8eAko_p_moKGZc1z2g9WyC8zxICmzzDwFdEJ4XFJvXBuTsCPkI8n5L_Z-g9AWO3FOTYhAFzZsKLlbnYC1qhuwhvsTiH9zGx4q1oT4ALMgvsVkbCcQ98rcNLNQ48bo7vCHwS6v72JCVHzjr-gxs2oCZkJqg_TeWjzavmx3Su45Vu6wy0sHExbENBPMIuMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
آریا یوسفی در اردوی تیم ملی: فصل بعد یا لژیونر خواهم شد یا در پرسپولیس بازی خواهم کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23610" target="_blank">📅 18:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23609">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSBYZ38532vsf3p-Pruw_vzFdBSBH5t4xYirl1o1QvHldE-NCGKI10bNsKYz6WN7UX0i2UUwLM0IkSd_u3wYJvdwojW3UaT4IjFRi-S03sCLUqmAToYawc088rtH5H73hpGb6g2YxhiJ6G1ilI-Nq_VIkkViH2Aq741v_lNUdrT9YEAE4JufblXubS67GmGfIyG56Ty3F2IYjHyzBBTQ2m3UStToy2-4o8IePO4VsJGjlQ77_ZeofRFpCTWmIRBXkImO7gR-0D01Liq0BcL1xVqMZd6NOJN8HUtABrDx_4QeObe7vix3cjm36OG8dNjAGa5afRQrd6r4rnXHad8pkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
مدیر ورزشی باشگاه بورسیا دورتموند: چه رئال مادرید چه هرباشگاه دیگه‌ای نیکو اشلوتربک رو میخواهد باید 60 میلیون یورو به ما پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23609" target="_blank">📅 18:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23608">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e34a779f0d.mp4?token=GAHyk1jb0_uGBWyWf-2LHRyzPfHdA55ibyo3fFcG8HoUNib39t3IsHnqeJGJQDLStEtXrbQXVshngbNdJxzDgOa60H0vTsEUhW3-iR4SodQF7jwBw4xHpqaoYpqMMeXNM311BAIK1NolGkVpXebtgXmRRhUzEpVtpcAfKtp4Ci3bw63WaP8C0TNVT8i3e4Vu5lhN85YPzjM8J8PXyNy4TW7uOzro_ag8IoP7-zJfO7Q3zc_kMShgfZBjS_Scvbx6NbImrt0dNuZFubvqPqbkjKE2uXyImIRcvyuv35iEY-wtYlQjQI-6mgXCxU-dHzbYMy8V9JQNFNxSb0emJNzYk2sTJOV_o-iEkiai68-wu6pfnQJ-9Li9lORZf6L1xAgH8w-hkI1M_JeCZO0gwSrLhfpNjQVCQ_noIwAsB-HLQS89Bvj2WDkwTH5r_f52HBY5lOD3d5if8ntsn4QeFda-g7hWi2T1fHgssgjHEFdQS1l0Ob2LjovDi6q_DJJZhDJA0Lnevfv5u4VBQ3L3q5jUwfjV5O1EwU-LttaZQLd1vq6SR9GTbrHpQKhWX6qb_f6BS6YEpOjvtTWp0i99S10xVMw7ZOZdH_Sgxge5FpUc_FQrXR45KKG2Vm_FHzJibL5fxXcIFJXjJgvg0iry6WVEOfbnf-Z3gfxvxX0fF89mTU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e34a779f0d.mp4?token=GAHyk1jb0_uGBWyWf-2LHRyzPfHdA55ibyo3fFcG8HoUNib39t3IsHnqeJGJQDLStEtXrbQXVshngbNdJxzDgOa60H0vTsEUhW3-iR4SodQF7jwBw4xHpqaoYpqMMeXNM311BAIK1NolGkVpXebtgXmRRhUzEpVtpcAfKtp4Ci3bw63WaP8C0TNVT8i3e4Vu5lhN85YPzjM8J8PXyNy4TW7uOzro_ag8IoP7-zJfO7Q3zc_kMShgfZBjS_Scvbx6NbImrt0dNuZFubvqPqbkjKE2uXyImIRcvyuv35iEY-wtYlQjQI-6mgXCxU-dHzbYMy8V9JQNFNxSb0emJNzYk2sTJOV_o-iEkiai68-wu6pfnQJ-9Li9lORZf6L1xAgH8w-hkI1M_JeCZO0gwSrLhfpNjQVCQ_noIwAsB-HLQS89Bvj2WDkwTH5r_f52HBY5lOD3d5if8ntsn4QeFda-g7hWi2T1fHgssgjHEFdQS1l0Ob2LjovDi6q_DJJZhDJA0Lnevfv5u4VBQ3L3q5jUwfjV5O1EwU-LttaZQLd1vq6SR9GTbrHpQKhWX6qb_f6BS6YEpOjvtTWp0i99S10xVMw7ZOZdH_Sgxge5FpUc_FQrXR45KKG2Vm_FHzJibL5fxXcIFJXjJgvg0iry6WVEOfbnf-Z3gfxvxX0fF89mTU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلر کیپ‌ورد، کشوری با500هزارنفر با 7 سیو مقابل اسپانیا بهترین بازیکن زمین شد. آخر بازی گریه کرد و گفت مادرش چون هزینه‌ویزای آمریکا رو نداشته، نتونسته بیاد و بازی‌پسرش رو از نزدیک ببینه. فالور های پیجش بعد از این بازی از 50 هزار نفر به 7.5 میلیون نفر رسید.…</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23608" target="_blank">📅 18:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23607">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5fa7cb37c.mp4?token=Zbywe8YpUJIY-Sx2qp4-SVuNfNF9izApLN5HnDnoWB0ajFIopB7DDuXWMhaHGwQNdtIou4tlWbIStJKvxD2fhFeO4pIACk0ydej1JcUFXoaIZEWygq6C3fyQ6SbaXNygvbuGUq_ocHgc147wkDgzSXvUSr0XIjtP3WhPFjgwdCzsZRo8Q0nyu5_YULyinTAVB3QGhbSltsjV35ARP3wm5e35uaRUOHWO9OTogOpTAenW-lgkD0hOadsZkD4o2h1D50ZLcwvTVO1YNEVG-FplAZYslYP74s07h_tGSi443V9HgS6E_cwU-gYcdIpZL40E7bsKQRsAFkvLe-kZyTzWZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5fa7cb37c.mp4?token=Zbywe8YpUJIY-Sx2qp4-SVuNfNF9izApLN5HnDnoWB0ajFIopB7DDuXWMhaHGwQNdtIou4tlWbIStJKvxD2fhFeO4pIACk0ydej1JcUFXoaIZEWygq6C3fyQ6SbaXNygvbuGUq_ocHgc147wkDgzSXvUSr0XIjtP3WhPFjgwdCzsZRo8Q0nyu5_YULyinTAVB3QGhbSltsjV35ARP3wm5e35uaRUOHWO9OTogOpTAenW-lgkD0hOadsZkD4o2h1D50ZLcwvTVO1YNEVG-FplAZYslYP74s07h_tGSi443V9HgS6E_cwU-gYcdIpZL40E7bsKQRsAFkvLe-kZyTzWZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطره‌خنده‌دار هاشم بیک زاده از حج؛ میگه بری حج نمیتونی با زنت... دست بزنی بغلش کنی
😂
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23607" target="_blank">📅 17:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23606">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-dSBrAFOoUlYPpHv00YcWRVZQUfCj8AYAvEUWD4Nu2_O-EBUSjgPC0ShW_eGf01Kd175UYpq4OknBDPCtlLaz6z5f51vM_pHBf_BNglvGoJau5IBkxO6nNVGZXQKI4U0vcuaix9B3z06_a2mFXDnV8CfeosRbmhXCkEiCwXmo3-7C09_I7uCF60_4UXxJIhlaa8H7NBz__AzHqIsw6vifGLs5LsP_rHddoIFKUhASChnTBQvRXQn4qrgpsWQbjlfDrlzGo23Gen4ynkE-6b4WuWk2megVQevCgeAX6GUbu14cd-41rus9RFG8_f0_ukUn5cjKzXz4pvuBOlXlf9fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلر کیپ‌ورد، کشوری با500هزارنفر با 7 سیو مقابل اسپانیا بهترین بازیکن زمین شد. آخر بازی گریه کرد و گفت مادرش چون هزینه‌ویزای آمریکا رو نداشته، نتونسته بیاد و بازی‌پسرش رو از نزدیک ببینه. فالور های پیجش بعد از این بازی از 50 هزار نفر به 7.5 میلیون نفر رسید. 15 برابر جمعیت کشورش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23606" target="_blank">📅 17:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23604">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/clSeeqG35B79nIJQTTm4mSx52ncPYLZ1rLptWNK7D8bCwC7to-TRVcU8eG_pmPRnqt2mYRd9f-s-j-ivRfX5bns59y3oJRT4P-5x7UyZsJ10Z_WSaImzbXe8hTty6r8KHQmrPW03Bs_ktD7k6k5aSP65W1RBybm5jjNo6q8GX77GMNQpFJjdKrKne-i0c3_pZSgKYQEH1hdiWLJHT4G7VZbR-kuqANvqGVS7Hl04auLjiZKSg6B83v5RnUKJT-bVCiR9vLwWmmKhT0erfRmLnNQTvsRwAT7fbUtUqmA3NIhggVMYtgOwy3eXl8YpApAPelzenYkKhKkLBAM2CHIVAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PnTH7T12lq9yKzUR6Yj_f7du13UDtN7QqwqlwOxxbEzgNks886RsCbuAGdDQfGFXi4jbBxL6heymrQzydK9x0FOJxIQiKklx5AxvDcZl-JC4cnbppVkudxFpM2Vqc7OSsT5pLVnOodwgeUCjywfEq-TKoPX18OJMulxoXKS8qZhPLlnel4j-9G6VCc3AQKpsrwKvsNa6C8sHqYCqWYnxxcE82Rwg-JjvTHOWA8_d9y98Q8iRtnlyNhtUsTFmGo8EdKHiehNNDyvUBbzbJ3OdtXAvGG_qtbUovZGi8DSXTOxKeCVC5ebcC7ox0MZBu2XN_aSFHJeieXBZqVjFdUC3Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
دو زوج ایرانی در حاشیه دیدار بامداد امروز دو تیم ملی ایران
🆚
نیوزیلند در جام جهانی که حسابی در فضای مجازی وایرال شده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23604" target="_blank">📅 16:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23603">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVEQ8Dra7OpspRc_sfnqP9QHylNPiRgLjfAKOCoXhgVcBimLrsD5sAY2PeLk8H3Ekls1sXYEeshYBGIfUIpcxLBygiPBwC-1mfZYIYgXFUaKPy7EalDJCwJ9hasjRRqTfPT8NLo7QytHpMHo3OR7Gif21u803fWn4RzK66C36IwptHU76IG2renzhrUxuqTIFex_EK5V4itOqA_FBdtub9oAfzGzVXfutepfQyCf62un31dgCOyJK6Gz-J2txpgnf3HaIrzEYcj7P4o04ytlF_w07sESqa_8d6kph0_mkS6r7PcPPXtU8wr7Twq30976qOao8jBbhZ6_-1CuKqXqNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌هفته‌دوم‌رقابت‌های‌جام‌جهانی 2026؛ دیدارهای این هفته روز پنجشنبه استارت میخوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23603" target="_blank">📅 16:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23602">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXVbWehCU9jbDtKLWbTiUvN7X_pk-38VdZUOu8rj1x0dkJuTVBx6XYNa5oLLpRR-dKw1EQruLfBhO9_-Ut54M9SFAbHSL2gyvYBoygVEmHd-3uEs4Y3RL2xwvV7xV0bhj_5Miv-pgQSUhaUR8qnLuu9X8Tjd5GSI6U-qn5I3EmtuNYbfcOkzRJFYPqBJ8WUCbwJsrwq96Uyl5mFSiMrb4PhBw4kTt_BUNYm60TpqzMtWhyMIPYMBOBzNzXDHfMGoLRAoh81k5Aq0VdYaJeefNDBpfHKq5WGVXaLtpEvQIo4TBYfRVyTwORqwd1rmU-KkWLl9vy9qj6PDS7wA_ExZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
علی رضا فغانی اسطوره داوری فوتبال ایران به عنوان‌ داور دیدارحساس‌دوتیم‌ فرانسه
🆚
سنگال انتخاب شد. این دیدار رور سه شنبه برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23602" target="_blank">📅 16:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23601">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b865e790d4.mp4?token=vK_AW_9_Kyqcqsn3sWPkep6MepmfXHArefk27538Zsn5dTpa0TdMgOolTAl-atrVFGdPJPGea2fyXj62gszw0rl6GVz7O49sLDEO37XaI8vZMVI2rrIO9-Wq8ZWsKSOTTfuwk0vTBMLPYaEQBztxUZQh-EeLm9LQfkMOz4r-6heVzx3lNrNavaumCeQLognbwHkyTCt1mvFK4IkGlWgoz17TVefO570iFHzCbH-m1hrpQzTeeOP8iJxh6OcH4t0vjXUule_sZgeJsgmK_TiwZUL0i1M-ji-Q4RuSrNY0ddlOeR2O9EVZRrkiwof3B7aR_FFE7O03AGS-Whxv55bBkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b865e790d4.mp4?token=vK_AW_9_Kyqcqsn3sWPkep6MepmfXHArefk27538Zsn5dTpa0TdMgOolTAl-atrVFGdPJPGea2fyXj62gszw0rl6GVz7O49sLDEO37XaI8vZMVI2rrIO9-Wq8ZWsKSOTTfuwk0vTBMLPYaEQBztxUZQh-EeLm9LQfkMOz4r-6heVzx3lNrNavaumCeQLognbwHkyTCt1mvFK4IkGlWgoz17TVefO570iFHzCbH-m1hrpQzTeeOP8iJxh6OcH4t0vjXUule_sZgeJsgmK_TiwZUL0i1M-ji-Q4RuSrNY0ddlOeR2O9EVZRrkiwof3B7aR_FFE7O03AGS-Whxv55bBkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جز‌ ترجمه‌های‌ماندگارتاریخ‌ ایران
؛ پیاتزا میگه به خلاقیت‌توحملات‌احتیاج داریم؛ حالا مترجم: سرویس خوب میزنیم تو دفاع باید عملکردمونو بهتر کنیم:)
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23601" target="_blank">📅 16:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23600">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
#فوری؛ کسری‌طاهری امروز بین‌دوستانش گفته مذاکرات خیلی خوبی با باشگاه پرسپولیس داشته و بلافاصله بعدِ اینکه مدیریت این‌باشگاه‌رضایت‌نامه او رو از روبین کازان بگیره راهی این تیم خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23600" target="_blank">📅 16:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23599">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSah-oagIjZSInL1ypV_MUzj4rpr25KfqauEZf-VmdQukPQ4bUYaE-2OMzymME0ndK3LNIapwlj6PANHEPdnfWK2PzOC8OnxxYhiIEknBw1DayYzvQSrxv-tVyDNWqIpMrbDjn1Xxw2fauD7PG8TNz-GlQKz9WULzVLHQnCAYj8C7mMP7UVIXj6Z4u8ON9wa0HLyq2xn9xFt_VbhAYpPfSAPYs16RtFaSsuSADy3ZGV8ASJX9_X7HBl6C-4tjscOzu6g_kaGlfoahHRlkGBWxGGINMcXLX2qVaxPN4EpQPzr4TWXnYVe9RvL735aST6vXJf3qlUZryRbWf5NQqEObQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
تیم منتخب روز ششم جام جهانی با حضور رامین رضاییان و محمد محبی از نگاه سوفااسکور
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23599" target="_blank">📅 15:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23598">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kf02u2wFYmQX2ZUW-SrjrKbStBCifojbF7MkYqPSJptW1PZlRFDG83Tk-iBn0v5MzpMkO8nUqF1HLsjJa1RAzVkjudZeWDkt5ccWQXrCufkbAUGHbVVv7gUzZIDKRue7ZIV0XfkUxgq7TuHkr7aJtAmM6X0R9CvDYKTAujOJ9mMFayjyoXn21_I9XPrWzDCfjNIkIDx7IT3XjVvLL5V3dd15ZzehqP-r9PS0AqDf4mZ2V2REAVhGkShhPc-p-X2Ml1-eM860pqY1vq_-8-zkLJtLzWC2uxfcQ99dwMuUcJsgqyczaSxX7J7JPGVr9Q7P4I1pmvOj--alwM17qdIcGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
روبن‌دیاز پس‌از ۱۸ ماه رابطه و زندگی در عمارتی مجلل از مایا جاما مجری‌معروف بریتانیایی جدا شد؛ بلافاصله پس از این جدایی، با حضور دانیلا ملچیور بازیگرپرتغالی فیلم‌های‌هالیوودی مثل‌جوخه انتحار و نگهبانان کهکشان ۳ درجایگاه‌ویژه‌بازی‌پرتغال و شیلی و تعاملات این دو در فضای مجازی، شایعات رابطه جدید دیاز دررسانه‌های‌بریتانیا و پرتغال بالا گرفته تا او علاوه بر فشار مسابقات، با حواشی سنگین زندگی شخصی‌اش هم دست‌وپنجه نرم کند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23598" target="_blank">📅 15:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23597">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c17684a49a.mp4?token=fumm8TLZId5v_7TKXlZRSkPAYdM34EOCMOTXpP8oTr6N-iNhlg8eiXGjXlamgGUIj3FbZugEPEJ0f99xuuW-WCimtQk5FiZGa9LWiPt7W230cMCTeffnIzIEGlWrqV_ZS_ePYXejBbKKcElhJcLDJCWWplifQrR-fzVczZSsQzmNwJaOoEOlXAnY2o_j22PCoZr4CA1bcLDhpjZv_bv7QtT0qSfCT_NJ_AY1SzviMrv263DOb_bAE4xXRUthjrEgpf4w0ZoN-HV2qW36h8Hmb8aiigdBoS3Gj7UBYc2EQaNyYJDHWTMl99vqEiRtU0F71o-33akxPd65YGgMVuObgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c17684a49a.mp4?token=fumm8TLZId5v_7TKXlZRSkPAYdM34EOCMOTXpP8oTr6N-iNhlg8eiXGjXlamgGUIj3FbZugEPEJ0f99xuuW-WCimtQk5FiZGa9LWiPt7W230cMCTeffnIzIEGlWrqV_ZS_ePYXejBbKKcElhJcLDJCWWplifQrR-fzVczZSsQzmNwJaOoEOlXAnY2o_j22PCoZr4CA1bcLDhpjZv_bv7QtT0qSfCT_NJ_AY1SzviMrv263DOb_bAE4xXRUthjrEgpf4w0ZoN-HV2qW36h8Hmb8aiigdBoS3Gj7UBYc2EQaNyYJDHWTMl99vqEiRtU0F71o-33akxPd65YGgMVuObgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
یه عینک بزنم تو برنامه زنده جذاب‌ تر بشم کسی زیاد توجه‌نمیکنه‌بهم؛ همون‌لحظه عادل فردوسی‌پور:
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23597" target="_blank">📅 15:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23596">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpXB6ttZWna_gNDTvObKtGNpaO0S3Aubk9ZOLgA7HqMU8QeuOhRjqsTQ3AYSP6OeK59kFVWGsjbNEQW6GwQplOuWqZAb8I8ujJAD_c3s_XJpfkIFFyTAvHBQL-oXLMv1XegBWCIyn7VA88FG8YpHQeFZ0g_ZKAprWWPo3z4s78blrhtV7lDZHNTv4KQKB4NLk_z-Mv1iqcsVwi5YQWG--jaTrybvCq3jAvIxC6mmghauIgw8zB6VN7g7THg3mrBnkRefoHgaLIgIi_lOaXWmUzgOSE84MEAaUnY4bVI1sXIqT3BKRo4Ankv4Z8EUTigSKGOVBaRDkLPIMdoq4mrAuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌نشریه‌فرانسوی لکیپ:
دولت آمریکا ویزای مهدی طارمی و مهدی ترابی دوبازیکن ایران رو باطل کرد و نمیتونن تو بازی با بلژیک تیم رو همراهی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23596" target="_blank">📅 15:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23595">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qz4aj0geGm_vKBUAOLJ0OEiL67MLeBPO17ABUdVHAtY_vDmob8NFZ1QdH7gEPdh0eQBQpoamLM6emELGvnMMAydTcrs3z0AR4-GZUJWWAKyrYC0_PyDyCmPKHj8Gpi0ZKh1YKjigF1oJdkvPnLWMsokgCXTdpngZrCD1BAdffzPemEXotHCs3eJ_shVSEXnwdfpzHIerrV3_GwMgxmXV8TKmoNbsUvIBR6QaidgJJR677iYSmENIFEDPOsrVEAGTMEZXzMQ2Uxvm81rrOYho7A7ecyZkAWMkIMLKcXlGsTQ-NvefQlKBCxrR3ar5irweOiKXX7N7o87P0N4r-2kYYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بااعلام‌استقلال؛ سهراب بختیاری‌زاده بعنوان سرمربی جدید آبی پوشان در فصل بعد انتخاب شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23595" target="_blank">📅 14:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23594">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEUaZX5RgpFR8592tCZXWZAc-Mg8jN07xT92ouGDdxSKHx5cTPnyfP3XrjZuSUoCs2M3mVfE1t83nDHcM3yD2Ua0ooxN4cfYcDeoSNQ2RegxSuIEK9eSPNP5aXlzrUeS6IC808guG93KfA16hlFQFl1y9qqEuCzIH80s3k132yb1y22c3oHP0lOH6VdJzctYzmU-bfsFTj7vwDpO6p5r88HMef1zqwxVBe2MbSPu7YrKEuEoguuCFkeg8a4cIWSIe3nZAXVV8EtE_mTJk48WNyZ3lIJk0Elp4OGUkSJ0wLMpUrfUs6nEwr8ebY8xqdNSnUQdwNDqHg5JJNc72PPwgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇳🇿
بازی که مساوی شد با اینکه نیوزیلند ضعیف‌ ترین تیم‌جام‌جهانیه؛ ولی کاش تو خارج از مستطیل سبز هم همه چیمون با نیوزیلند مساوی میبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23594" target="_blank">📅 14:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23593">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcCf4eahGWesWECbeq_1xLA-982sjlr4i8u3Q2bLSbecsgU2AfVhAyB0mWMBXe8TGjSkZajLOU2ovrF_WwabuyHE0CmlB-Blk8Jm7k7CqaAoCBtL57o0t68mXQKOyFAeCgAKqP5dnCAROnUX-eGW2bFZpEzwR8HYIMqQCOVXugsEYVZfflgn6dZQCNjoeMMGttwmsHtRvxkBByxf4WGXPEN5LlXj8sdj5QGfyj_2DuWVHTR299kjTMUcgVUKycreRhIdyUrr2xoXZv-0SE4KKs8zCOSSnHCObq-9M5eHS8CxW8pNrA9rkGKxwRcBLFGWlQPKajBUWUfCWyrYl6DYMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23593" target="_blank">📅 14:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23592">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_QjYFDtlW_9CPdejvWo9niMEmnLtjFHbkAzupHDMzFmqkVAwZtQJgvU08f-uoGOXV6vx8fc136De490qSHXgCYGl-xC9Vaj54aJvLbZWqOoomvYG05GsooluLQwkGG6DKcNFVjGLf2ZjJdhHViAHn6v2btmzkVORNhyRWQbei5eJW_gDch25yQD-vrpld3Rbam0t88bB9gtnxDhjx-FY62t-AatZ0y8Vqls-o7eEFGFAKPqvAwjsZn9MZ0Dq44eCmyBvK8KBW5ucBC-ROKxwNvuNoof2hQNJH_hcDkpn-G9W4EaYwltX6D7HRf9muunLY7xSG6oeIDDKD2QnkrwuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aparat Sport [3.6.2].apk</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23592" target="_blank">📅 14:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23591">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-tq9ij7eP8QWhvsvkU3_SMgVbqXP_lBQ5_JrQ1c7tnwosmih5YdgbgKYEKn0_NAV6x7lTsR7tgvTPwuKpXwc1avjf3qGAH-ir6Q2OxDWw6BZ2s1Nq23qsuKC4hAu5Yl3E7yP_ePF95SIP76ldKdmUi3bYptW7_W7rVuwwCX-yqyC-TKfyaMqDzdr8Nmq5GiafgISxYh9WtwSi7qWLOCXOeKUiApx2TyS1cq_oCPAeyZ-Y4x-leZQVj-OIWlULhpHfQiSKasy9ev7MQ144pFKzJ8inY3TMfjWC1LHGU42RferaLfL4OfpCwcRoflcn0hdBRTeQ5pLJYyRXnwRXXhIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
#تکمیلی؛ رومانو: نیکو پاز به مدیریت باشگاه رئال‌مادرید خواسته که اجازه‌بدهند یک فصل دیگر در کومو بازی کنه و تابستان 2027 با قراردادی پنج ساله به باشگاه رئال مادرید برگرده. نیکو پاز 21 سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23591" target="_blank">📅 13:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23590">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1f5900223.mp4?token=CmZ-TlHH3Ua4p8DRbihVkz9Bp1XVLxVVj5SpcHNOb6GsXaS7PB_k3uziCkyePAdKS7DdCDLwCAzrVH-r2G6etFCkKMJxVmnvIfxdCwsNDiBbl9iWIOVF2it8G4Op5Axo1g-KCsyE-xtvgX9klZ2tvZ3rnyS0GEOWjVwo1AxM4W4REgNOwuhODRCjE3D0pfcP5B0iRxosKYlJN3aY_WgmFcN7_iYA57H_MHgSOiPvRUgTgPmmYb1XV5cygqI8NUMyPez7v2NkBpqKzUp7LMOBdGbihYnQ1hJNjSMJL_4PwC3mDtMhI13i71NKiLbiKAYlSkBJ1fXOfFDr8-ggJs-cpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1f5900223.mp4?token=CmZ-TlHH3Ua4p8DRbihVkz9Bp1XVLxVVj5SpcHNOb6GsXaS7PB_k3uziCkyePAdKS7DdCDLwCAzrVH-r2G6etFCkKMJxVmnvIfxdCwsNDiBbl9iWIOVF2it8G4Op5Axo1g-KCsyE-xtvgX9klZ2tvZ3rnyS0GEOWjVwo1AxM4W4REgNOwuhODRCjE3D0pfcP5B0iRxosKYlJN3aY_WgmFcN7_iYA57H_MHgSOiPvRUgTgPmmYb1XV5cygqI8NUMyPez7v2NkBpqKzUp7LMOBdGbihYnQ1hJNjSMJL_4PwC3mDtMhI13i71NKiLbiKAYlSkBJ1fXOfFDr8-ggJs-cpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
رامین رضاییان در گفتگو با میرر: شادی گل من سیاسی است اما اینجا نمی‌خواهم درباره آن صحبت کنم. گلم رو به تموم مردم عزیز ایران تقدیم میکنم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23590" target="_blank">📅 13:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23589">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzSd2F1uiTjF_ND39pM8yo9lqYh17yJqSUYt0fw1xaa9ZpF8Q7h6HgIQGB3vDIyl1TaEbmBhsSCFoE5tKdb8eblz5sbJ0u3Ybj3pPSD8OPMmDweR4wDI1ILJBTwou2LQr9WP_DNZFruwb71S9NqVfG8Izy1uwJGvxaMjYLGksxnthMSJYA2BdAe18ep6BPwTRt_ZTrMstfTyujEPX3-LfqETbi0f1TOlKz9s9AaxKa3lgJ9Dgsuts9FSZD5Fx4jwDFb0oi3SpuYDd2qX09TN0FCajYwDFTN1W0aqyunPx_tUBMDqhFR9G2Ig57Qoxf2UnWZYk9kEn81ED9mwC8RLGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تعداد فالورهای وزینیا دروازه‌بان تیم کیپ ورد از 50 هزار به 3 میلیون رسید اونم تنها در 5 ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23589" target="_blank">📅 13:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23588">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0-Cfw1KI-OkURudRGp5TYb2MqJLdPEN8wUqdYa1ySpswOyLbvHkE68eprd9p0zry62rWGalsjQ2KNT0Tse6V0SDVmZMsPkg4-8StOGm1-P8vQ0JwLhCOGZczerV6_CwDcwMG2S17xuo0-5omUihBSnuLxLXWrL4Izhmy1bbxRaJffUTkFUnTrO69n7a5bEqzu4Outw0MwexDSZBv7G1zKuY_LXet6-T1UTKn7oeWz6HSE3D9raJKlse32rab1FLFpwlF9jgIGuBiMHr0UobKKTrLAfjK7DkE1CsmsqqD9AH80kvhR4RQFKXz-s_GQmf-0M7OTUqAGX6R7goaCOTnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دهنت‌ سرویس پسر یه حرکتی زدی شدی سوژه همه؛ حالا تیری هانری اسطوره آرسنال دیگر کارشناس شبکه جام جهانیم درباره خوشحالی بعد گل محمد محبی گفته فکر نمی کنم منظور بدی داشته باشه. خودِ محمد محبیم گفته بخدا فقط یه خوشحالی ساده بود که اون لحظه به ذهنم رسید.…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23588" target="_blank">📅 12:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23587">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5FoU72BtComQBfsXXD9sCLHMfWNnXWmGQiuBBl0GuYHD_ymGjIhYS2rIKcJg_zhGRZak4U0g7b70sHLYsW2-952w1kWjF_23Hd_6-kUa0OKIdeLdlkpt8KwiFx_Ur3q9iUd92r_Wm2XcJ32foGCi68S-dN9qI4DVX5I2Je1JWuZaMMEmow81b9J2lGk9Gj6jtKN1D-oPobtbwYsIts51-HU734zgceeLQekZ4R5IMUuSpWVYZwGkmVFboPHN9cCcgEMuNJaP7KGrw1T9f53Bg3MUzDqiywaomZSXPDZGWyldL50VWB8K7ke-A2thwMChbtclcuI8hk1z7fLtGaX5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو: آنتونیو رودیگر مدافع میانی رئال مادرید قرار داد خود را یک‌فصل دیگر با این تیم تمدید کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23587" target="_blank">📅 12:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23586">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ym-ln0nMe0qLgyA1yL6iBjcmyAXnLSHofRjvLYKWSQoHGWHpu6M3brTkX1sGYidqZky1ooHRJccBd16GfFEvDyYFQFTK4MHAA2Hqj2ogU2lsvuqlusxpFuuSS2AoHqy7t-w0KThQInr8qepVq4jF5Yp8ZgkvJyRkrq24IrS9HHgIgCGY2SYm99XYGr50UJMB-FWELvEyiQFnLyCX0DRtmQnWWuP0L0YgoYqohsclpfzyhKzgr6G0GNEEEwNzIDPr-SE7lsjR36wcfllbjWyi9BzmScfo39tdFn7unJ1YPQ-P-uaE4JOJAdNW9OFES1z7BU3uuNy3xxlCbR4C6YZ-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
درباره وضعیت آریا یوسفی، محمد امین حزباوی و مهدی لیموچی که هرسه مدنظر باشگاه پرسپولیس است و مدیریت‌این‌باشگاه مذاکراتی‌نیز با مدیربرنامه آن‌ها داشته بزودی اخبار تکمیلی رو خواهم گفت.
‼️
آریا یوسفی جواب تماس‌های مدیران سپاهان رو نمیده و چند بار گفته یا لژیونر…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23586" target="_blank">📅 12:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23585">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8ASf4wEoc2ox8On9iNX7GUaqmRF2eqV158GYyJgQfdKFqBnWvZdscjL0RMWHxoqqhtJXCVpwIw7afmETvVFFI_hyEwPrtBWyqMalJHLnYTfe_IZuXnkRKln5kO8j71e8fA-z5fJ-FKUfOLSAgKQIaCU40NHMd6hZdEGd6mEddqJhMo4HUidJJlCbdvOrSgnBBSvLeZeiEEVojG30pLzffr5htT4yic7S0NacOQUgG8zkpoI4XcyOrazpe4uIHTBg1QBJnsKPG1RIzUbh4rfskevqPn0WvgRgjUcQUYpebHAaoP3eVW2LONSnL8LqWDeVZWUrXZy4z9s9ABUCD8XPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
شادی گل محمد محبی که تو رسانه‌های خارجی جنجالی شده و میگن احتمال محرومیتش از رقابت های جام‌جهانی‌زیاد است! زلاتان ابراهیموویچ هم که کارشناس شبکه جام جهانیه ازش انتقاد کرده و گفته همینکه برای تیمت‌گل‌زدی کافیه دیگ این‌کارا چیه که تو خاک کشوری که رهبرت رو کشت…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23585" target="_blank">📅 11:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23584">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXWw7tGVTh2_BLJBVoK9oKuK3fjbEWevpAmzN9jOVt1C07n6Ug6bWNZLEbbn8hTuow4XADdDUUiVkQimR8JXFzDe3J2fVb8wTSCIrEYToC2kpwcjFt-q8k1zx7PNCwG1MuS9f9Lq_mMKGZQBGOgRLZ27zEDrJ0kNWnvUAUfcl10nY4G2fmC7vFKnB11eE5dF5y06h0eSHHQysoW4C7vd-6x1q0W4dFFvxaGreBMMVh5VoBSK3CF20SQKDv9o4GHGlXtvEw8lFLAGaFT_3WObTdMCG19dan98RvV9XYBmVTxvG0IS0Ts9_lsN80PQ2GLHX9bpZXRG7nkdOccCj6LEuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#نقل‌وانتقالات|رومانو: ژوزه موریینو شب گذشته درجلسه‌بامدیران رئال‌مادرید از علاقه خود به سبک‌بازی ماتئوس فرناندز ستاره پرتغالی وستهم خبر داد و درخواست جذب این بازیکن جوان رو کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23584" target="_blank">📅 11:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23583">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⚽️
خلاصه‌دیدار امروزصبح دو تیم ایران
🆚
نیوزیلند در هفته نخست رقابت های جام جهانی 2026.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23583" target="_blank">📅 11:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23582">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBEBsV6kZoHh6z20-sdX-AjzH4x0C1QbxnSRFJ5Kl6UsO5HsDNAXXrAJ-NB7Okozme1TjDM1tBm0lx5D4qWQNcQdvgHGEw4sOZB_w-T4x-95mHzHdrv-CG14OF4z2vtINJVfWmX5XUunzJ0PHqVg9GdFFYEaffFvfWn1nv_hSd0E07b-6P8kpVR9odKJPO08tDC1hj_2_zrWEHsc71I0ekr6Ypd4ZXjm_NGtzbm0e5OEVwN_Uac14ZRdoI5AIsg5J_rDq03K4B75SKMq7yPFZDFnq_8TaQN5UQHAHeyFLzOuqBABGMfEgxywnl-_juqv45YFfGahCsE_hV7aKHBzDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد درخشان‌رامین‌رضاییان دربازی با نیوزلند درسن 35 سالگی: ۱گل، ۱پاس‌گل، ۴ از ۴ دوئل برنده،  ۲از ۲ دریبل‌موفق، ۲تکل، ۳ قطع توپ، ۴ بازپسگیری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23582" target="_blank">📅 11:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23581">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwVCDYW33KTX0lyKl54TiD-ZwZ-xfx2pZZmW3iApjy6coFKJZgauXxaIN7wEcwwi27BD9QBaf-E2XhApwma5uQorJbi2StLoskq1VFAC8C2aalFEcvKNX8IhGtOf-DRJmM1waIMAl55ZNyNtGuaVaEnEjhtvM2WDl_06bW6RqTmVO2fulsoQvZjVwtlpQcVxIsX3mZd5dA4xOOa0fmn7-QMEx7A_Ea82OcJtz8Ba8VdtSUY0mlmyt2xJ58mzU83jMTCuFpafRZE4QQkNIqLsveThr_pwH3LsTvpSFYDM5ll5F7g-rA_yuhI-4YAZqjN6dTN1dyQX2TdKvWsxAkldaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
امیرقلعه‌نویی‌سرمربی‌تیم‌ایران: میخواستیم دو شب قبل بازی بیایم آمریکا، گفتن نمی‌شه و فقط باید شب قبل‌بیاید. الان هم میخوایم برای ریکاوری بیشتر بمونیم لس‌ آنجلس ولی بازم گفتن باید همین امشب از آمریکا برید. ما مظلوم‌ترین تیم تاریخ جام جهانی هستیم. ساعتم هم…</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23581" target="_blank">📅 11:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23580">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28dc4a75ce.mp4?token=E3_yN8UNlp8KiqC4w3Z5BErU2MVJraKRuBCpwz8oT6vZ0Zn2hTwaLoDBDBSR7cRfbgaaoguWVhBIqpB9iebKeHLjFNvxmfXc-4qhKjJXYfqvf-k6XQn1QDTLwMyOBEkGCEDgE5boVgQ7aYrkOA8t8xcWzKgz3kMroROwujEhZ7_9hVbT6A1PWOcBWUI8QqbLdWwEgDsJcsxxtGeyaLYBY_iXzcx9j-CQC8vrQq1MmxK_Ms2_nkD3Uavkeg6fTBOBPNyT2A2vtLp9E__Elqts_vO1ZEd-8ouhp6VrqLyVpXzqaWwmUFm-qOygk4vJaNabh-Al6f_zfj-Jv91kiDU4aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28dc4a75ce.mp4?token=E3_yN8UNlp8KiqC4w3Z5BErU2MVJraKRuBCpwz8oT6vZ0Zn2hTwaLoDBDBSR7cRfbgaaoguWVhBIqpB9iebKeHLjFNvxmfXc-4qhKjJXYfqvf-k6XQn1QDTLwMyOBEkGCEDgE5boVgQ7aYrkOA8t8xcWzKgz3kMroROwujEhZ7_9hVbT6A1PWOcBWUI8QqbLdWwEgDsJcsxxtGeyaLYBY_iXzcx9j-CQC8vrQq1MmxK_Ms2_nkD3Uavkeg6fTBOBPNyT2A2vtLp9E__Elqts_vO1ZEd-8ouhp6VrqLyVpXzqaWwmUFm-qOygk4vJaNabh-Al6f_zfj-Jv91kiDU4aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
امیر علی اکبری در ویژه برنامه شب گذشته جام جهانی به این شکل انتقام همه رو از ابوطالب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23580" target="_blank">📅 10:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23579">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4eABUc0pgfAzyxYX8GjFeq0BxMTAnRBR_Iib_2sEA8ngjXCf2HPd43yBTDXdir59xtbPp-3QskV8kdg28S_zMBuBJSfp4X3xBltIRpRbwV94Af6cBRiYf1yVvyaMJFsx39mNyXXmuGew__TgBHU3fKzsNcvXsbAMUjbge8I6fz1WLRP3MS22HCzIFdleCNnzdug7OeS2dodVYG77HW_o9Bit7OUNUrwXdFp7vXONfcrrwaXQ-0bOBRoLyi3BJlVDbpShk-zu2lNrzHb7lx4RcUqw2iQRD8eRV_rmQjIMgWUD-krdnVemkxLQUHA7eYOoA--RCCZxoUJuuwZ4hV7fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه سپاهان برای فروش محمد امین حزباوی، آریا یوسفی و مهدی لیموچی روی هم مبلغ 220 میلیارد تومان میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23579" target="_blank">📅 10:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23578">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ea73ae1d.mp4?token=Uv5CdGFEqV3tWYZGLDQAoNVVsR0lwDkqEkHZQ9YBpFNxqRg7YBJXvcuL_3VkzRU-nSMZTQCBSCH085N8iJ4EFfhVmcggxc0A6VW1Q3D2iELIbyTnrdGr8hQNL-K_6zInph5qmodJR8Kgasl7ihB0Q63yyxXaM6Zr9hFqC0sj5tpG6K8T-xl9rYwCbTh50ODciwQ4wZe94_KvqD4bwh0KoAJUwX9s9N4uiWi3NfCi_Tm3xBkTHijZ0FqH9ZFzmRdXyqQs7diGKaCSiuLXhjtCvX9OPlo2megbztFF8sutqc62bqOJp0rQmVIbzBoXMRUrl-FR1nvPbuUiwBB6tlNejQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ea73ae1d.mp4?token=Uv5CdGFEqV3tWYZGLDQAoNVVsR0lwDkqEkHZQ9YBpFNxqRg7YBJXvcuL_3VkzRU-nSMZTQCBSCH085N8iJ4EFfhVmcggxc0A6VW1Q3D2iELIbyTnrdGr8hQNL-K_6zInph5qmodJR8Kgasl7ihB0Q63yyxXaM6Zr9hFqC0sj5tpG6K8T-xl9rYwCbTh50ODciwQ4wZe94_KvqD4bwh0KoAJUwX9s9N4uiWi3NfCi_Tm3xBkTHijZ0FqH9ZFzmRdXyqQs7diGKaCSiuLXhjtCvX9OPlo2megbztFF8sutqc62bqOJp0rQmVIbzBoXMRUrl-FR1nvPbuUiwBB6tlNejQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این گیف عالی بود؛ امیر قلعه نویی حین بازی با نیوزیلند بدنبال‌ساعت گرونقیمتش بود. مشخص نیس کی ازش دزدیدتش که اینجوری داره از هم میپرسه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23578" target="_blank">📅 10:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23577">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W76cvCmzuBgDkijbxQIpB-2PEWHlqKLR7po1RQynxLpBQzDdExxbk2bS-QHzmwldt5FlTBwGf2mCnqFk11mud2E_mAbTzStBGd3_qJCfIKOAN_wr_fTSIBnxGZwF704q4JOLFi2Oq4yecgPpWdSdF7N9XYtmgsSGPvrtit7yd1dEnWQuxh5Fnod-KU-uuT96RV0kNFhH9BoYeYjgCszSeuijiTRXDtcITmEcbtXtupYb_5b7Ev0jjTYUArHG9QBwfbR0Nvm_HD9ScBiGmjx4ObfsDwQDY3pA4U_8RTym_ey3aC9AXj91oWKmQ40qY2V8luY6vRleemrbxxBlv5THpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
شش تیم آسیایی حاضر درجام جهانی 2026 در دور اول مسابقات‌شکست‌ناپذیر بودند. ببینیم اردن و عراق امشب‌وفرداشب مقابل‌رقباشون چیکار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23577" target="_blank">📅 10:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23576">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QplkIJAvXlIMUTPUrV98hp3weNguD0DK6SA_ktWmuALVpg38fpfnlzTu9qoQxY4t9Yf7-AMOYbcFQmAzcefMCXFj1huSYHUjkyssb_eOjmcebmHGH-AGTIwM2TsWu1dlZgnXwjQVa-W1po0Py6UZDC8schSpsaEwCp28de988axV_tH2X2eELybj6y9emSC0VwJEJmwWdaXh_e-SxqZuKTH-ripRIXk3XxssfSUybcYbjemHtzZkRch2CjsRYSlIXMiv89WG0Q-U-t6ZGS4BTvSKMJuGtA5-nMS7l_vbhFpn7BobnSLyqarntvaq2gJSoBNpsrl9LDroOfQYXEnDhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
شش تیم آسیایی حاضر درجام جهانی 2026 در دور اول مسابقات‌شکست‌ناپذیر بودند. ببینیم اردن و عراق امشب‌وفرداشب مقابل‌رقباشون چیکار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23576" target="_blank">📅 10:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23575">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a244147c.mp4?token=E6vKLWl519lruX0knJW4HXkZ_raUO58RJNV6ZCfuV_kBQcJKUlYwV9-vuQ1vYcylq4uKVO-biGH9phFmCnbWW9VYNTXmAgW-9b7FCuKfiDkTTxfryxVI9wCRRDsZsN05oez-SA77kulrreryHL_LGj-3nbjBercMPkQuUkxPglzVt2M71VZl8YKFdipi5fNQKriHN_d2B3W1UpHmBftSMbc_dIGi9QibpUTJAMtgc0IGlQatgxogdDWEQFbploQIBbXrNAKWvYDuXA9XHOWU8v08QGNyLukuyd0MJ5xXI9eX7NuQegk9qXWGdShnPsBq0RI1LJ_QIpo8xOj9GmgmuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a244147c.mp4?token=E6vKLWl519lruX0knJW4HXkZ_raUO58RJNV6ZCfuV_kBQcJKUlYwV9-vuQ1vYcylq4uKVO-biGH9phFmCnbWW9VYNTXmAgW-9b7FCuKfiDkTTxfryxVI9wCRRDsZsN05oez-SA77kulrreryHL_LGj-3nbjBercMPkQuUkxPglzVt2M71VZl8YKFdipi5fNQKriHN_d2B3W1UpHmBftSMbc_dIGi9QibpUTJAMtgc0IGlQatgxogdDWEQFbploQIBbXrNAKWvYDuXA9XHOWU8v08QGNyLukuyd0MJ5xXI9eX7NuQegk9qXWGdShnPsBq0RI1LJ_QIpo8xOj9GmgmuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
سوپرگل‌دیدنی‌امام عاشور ستاره‌تیم‌ملی مصر در بازی روزگذشته مقابل بلژیک درهفته اول جام‌جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23575" target="_blank">📅 10:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23573">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeuAaLp-accqZutNprsw3hpffWlXkxIXv0M2I58JhyLOfmyHe1e7xzEoeVBbheiQxxLQgNBRA4wtk1QVo8lpNRJjalnZkJcSLmBaj1j648Hp-vyL1JsGkCXMFVDBdKgFNgJQP6E1xp76KtbRFk5T0fo8Ve_fe1FycqSGeYqaOQqCbNF62d5KLx1v9xC4QsaaRjDKycNq0j21z6cKly3DD6Us9kiGmgQHeaewpcmCDUFADj9-kmTIusVsBYsCEGzqpDJYJMMmQVks6t12WA3E1xdHD8m-EFy_GLBhD1gpuDnabacwyCKznl2rKXRvaG9emq6McG84QECIDoiNyIFXVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23573" target="_blank">📅 09:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23572">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJ4Bv6vFzic63h_3nvErF2Ox-AzeYYmaUhRMIYaFLnuAuUeAm2LS-XjZyC4fxzWeGJq9bXSgoqsnhKibKmqNmFZHoTsL6ILGrLgmqjO7--MaBXbcxDh6bi2MWcOJNoBtsEQoTL7qotUfCrMIWCXdp7GsUAh99stB5ox9N2qR-EEHPyT0eWYM7Y9JYRSlAbwzaJsLtZOrgP8hWmHw7p1MkADTFmWEsEzDE7kkgKhAof9TC1FpVXKEqlNxNBlno03S2A95ZwiWQtP9tO_fchq30gtQQyDC9k5puuqZG_gM7X_j-MolXUGEmC0E7KPFi66bEnX2P7Ol9lQogmLVvarmtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران دو باشگاه مس رفسنجان و نساجی مازندران در روز های گذشته مذاکراتی‌باسهراب بختیاری زاده سرمربی فعلی آبی‌ها داشته‌اند و درصورتی که بختیاری‌زاده با تیم استقلال قطع همکاری کند با یکی‌از این دو تیم قرار داد رسمی خود را امضا خواهد…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23572" target="_blank">📅 09:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23571">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/607d3917ea.mp4?token=Er7nOhDMeAw9L7luO5dZbzea5FUvdeTsZf0tw2slqMsBV-QzV1NmKBYKOE8QLcN_TXtmcwH_DZtAYjNH-_kB1oQ32hBeWJCYtAqbw9Ts9-hUfZQ816Qeo91n8p1iOcgEf43YmSb0bkAJsl-BFG-LKO1FpkDc-QEEHV0NMdmEWhF5v_jbZoVu0twbnvoJbalLVkiA7C-QmsAQJTHKI1dGO_uV9lrsNWZXYp0d_r3DD8NoqwRnYRX9AWaLR-4DFWVk8Cs4swi6wG5LDcOS9nZW1oRGzDnlS1pPDYqTPPl5O9vkHw-SjGpGrkjnmqEe7pODJtLreltDFjAT8kLcvTSf2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/607d3917ea.mp4?token=Er7nOhDMeAw9L7luO5dZbzea5FUvdeTsZf0tw2slqMsBV-QzV1NmKBYKOE8QLcN_TXtmcwH_DZtAYjNH-_kB1oQ32hBeWJCYtAqbw9Ts9-hUfZQ816Qeo91n8p1iOcgEf43YmSb0bkAJsl-BFG-LKO1FpkDc-QEEHV0NMdmEWhF5v_jbZoVu0twbnvoJbalLVkiA7C-QmsAQJTHKI1dGO_uV9lrsNWZXYp0d_r3DD8NoqwRnYRX9AWaLR-4DFWVk8Cs4swi6wG5LDcOS9nZW1oRGzDnlS1pPDYqTPPl5O9vkHw-SjGpGrkjnmqEe7pODJtLreltDFjAT8kLcvTSf2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین‌ولاتی امیر حسین قیاسی خطاب به محمدحسین میثاقی مجری سازمان صداوسیما
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23571" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23570">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeLW0bZgJMUkM7tKk8u9Ul__6y5QClhP_4-MqHbV5Sbo1pGexlBP_IVpEpmE8bquHH1stAu2tk-gmNSA_seS3OlROGXECrb_C6B53wetdyfjjvjBu2_vLw0WcoI4-FFCH2CrnfepMD53jFWqghFf-A14haud43zdgG_jAqgPc00fSrTz-aUyQnnLF6AdiVwvIF_US2crT2qgYv3hcxwAlkFXoLaqY-MPnXqD5viHu2db1NtGOhE3xnpLptCQpvqgMn6YFKBMJ2NPUXqrmlSI9BWdhUnCuc7vMcqw_puFlOvKEyKfmZ4YJsKq6UhZxXgWb2welfj2j9ejGnzKCzBOmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇯🇵
موریاسو سرمربی با تجربه تیم ملی ژاپن با شنیدن سرودملی‌کشورش‌اشک ریخت. یکی از تاثیر گذارترین عکس های جام جهانی تا اینجای کار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23570" target="_blank">📅 09:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23569">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e9cf628c.mp4?token=P92Ajuu306qJZ4p2MZWnoqBOsm4QpKyM_SKLTBiR4Q7n_p3UtPmOVtVFgTsPBypyMjBfzShxwbQbTQ0kWWUgyZuJeIpDZ7ZqTNHUfTVkaTGt2EfzONr_XNEov3DDtuJDjhrozSvmm6crkMsbNhIBNuuGH4nLXKOHx_MT-YXiufEzf_X6efW2ylsNzInOuLJAGT0ozIjg_XqUh87Ujwj2WGPV8aBS-438YUtYaHtrcAIN2WHzG60J2ydf6xKPVvRCwYwaCD77W0FEQYtzbZKUtSgTXHvSwJVxFnFh-VCkkKN2foTlge1Wqr4vlaC1ckfLhvrCFbdegFZ1J8ruSLBGhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e9cf628c.mp4?token=P92Ajuu306qJZ4p2MZWnoqBOsm4QpKyM_SKLTBiR4Q7n_p3UtPmOVtVFgTsPBypyMjBfzShxwbQbTQ0kWWUgyZuJeIpDZ7ZqTNHUfTVkaTGt2EfzONr_XNEov3DDtuJDjhrozSvmm6crkMsbNhIBNuuGH4nLXKOHx_MT-YXiufEzf_X6efW2ylsNzInOuLJAGT0ozIjg_XqUh87Ujwj2WGPV8aBS-438YUtYaHtrcAIN2WHzG60J2ydf6xKPVvRCwYwaCD77W0FEQYtzbZKUtSgTXHvSwJVxFnFh-VCkkKN2foTlge1Wqr4vlaC1ckfLhvrCFbdegFZ1J8ruSLBGhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه‌نویی در نشست خبری هم ولکن ساعت رولکسش نشد و به‌این‌شکل‌اون‌رو به نمایش گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23569" target="_blank">📅 08:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23568">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9YdPWd6SA4e9q5F0LCns0vOMM3g47ERCYV6G9ROMvr6_-NkP6DSowCET-wt2ejCZBuE3hHzBajUnTpvV03nrr7Ukwd-jMeOHW43awnyt3VnmtBqsVox9exSXLFE1-5DkU-qLkAAFBUHeT7N6ilcMo2P7UW42_QLyaCEkFLipii2FBVCDCtI13p0pF4JnLcx9DqCarNSjTeBLriYcQXiQ-9MXK92ww8naKYrFZbB-1TROyvcsU2Sz3sDq4_420S5wJez8TGIdytAdGN42-c0PcTtJn-YiXeMAr-imXYNXTMJSpSHXQDMqOLr0u1iwORbxNJHYlH43YQmm1Y9IXpJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه‌ بنده‌خدا دیگه رو برد امشب بلژیک مقابل مصر 8.5 میلیون دلار شرط‌بسته‌بود که خیلی شیک باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23568" target="_blank">📅 08:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23566">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hWadNxs2VVzbOs4KQ_Ntkk6ppHb4Gu_n3Jv5qiRG0tBmfOY3JUM8KdNLZyteJtVQl7ABdOB-aKvyZm9mhECJG0d85GmSOhDhtJsSWy7bGmfbJw5Px0LUbGX2QEkYtI8aKbQVgHUelrLXd5Y2WEI7foVH2eXQUv0U3_g6LuJbEDu6YgVsE2Xb12nhCJ7Nu2cv1OGnlXcdy5IpbuZaL4FZSPdi2Ff08UfRbQWyCstNdvHHwVFPnqB2NYuL1pidMRi7PysDbkvo7QE5YkEyq9AW9KzUzePd1z8gMAX0mAVmB7fcb2ygJmNAEBQ-Wlzl8Ui6jkXf7ScvNaqh8gDGwTpR9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pZxlyme1zkkV_Enmv-PGOdtWzVA7fpNrq3JVk0PFLwaJhBcDivu17QdogptxJIchlGPkw9oPU2Ar957ocwdJugitlR3uasz21cr-fVtmzy8-n3tVJotx7WgxREUvq7wh6_0RwZOEc-EYWTN_aW9MV3h_BYgG3Ams7eF7Cbek351qZBAJQ51yr0pPOZOLNRBJgaAHhC1XDbRzLcmt-7WhHRMcCEHrEXFKZ6DUItbXbmeU57tpDrkzPWibYCWHf5N_wBMExsH7389UaGn6E6kj9kOhTOO-7XSysQ8zoJBDsr7W-pKK_Xm1tx6dzmEjFlrRjPV_GCi4AGLiVF9-LPoKMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
نیمار جونیور اعلام کرد که پارتنرش بارداره و قراره یه دختر خوشکل دیگه براش بیاره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23566" target="_blank">📅 08:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23565">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvTTybXaQQRO-TUtdIghZgVzQ1w1b9XU1OXQzyF-qHPYTH8dEv7tweE4KGjSm99qCoHVNGedAodaRCqqMVptnXxrzcTw61JJR4LpIpAq8XHe5D7ZBwYag3MO_rVhnhso2JYvkuFsSmc4GVBCkeW8kuqFZ5VylDi2sExN2fINLcrEmb603eLwz9hR0eORXOkIzJsvn35d6HsJtvFFyX3g7ZSEPHXOLXLQmjEI0Je1LZ_Nudb4lyqWTsp6ks1VunOJctsY4aXFU0AlU5c5z7el-wfk2IK_Lsvsk2cSQW-G13bHbOXPNmyie4Eyz1nniLqzU0HZD4XMXtcADzm1JwcF2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد درخشان‌رامین‌رضاییان دربازی با نیوزلند درسن 35 سالگی: ۱گل، ۱پاس‌گل، ۴ از ۴ دوئل برنده،  ۲از ۲ دریبل‌موفق، ۲تکل، ۳ قطع توپ، ۴ بازپسگیری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23565" target="_blank">📅 07:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23564">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ae8867bbe.mp4?token=SulqpFFJGODw5SEoqYf__vm55xzGI1SAOJu0zpYaMyW3kpnTV7bWv3qx_zafO3DTkep8eVWAWubJy8XTaMmMOv96x7fzJ3-RqCEQ9Zj2w_ZyZrU7k32EeldVOqMvQuxVtUEgjzdh3z_kdM1E62C7uCauRZtmgjj37-7jILErTaacvRJ71L86QFrxQOEJ428UljT7PO7IvknQFNT-bMB3xV3U0PqsUAGyp40IV2d8H9niL_WMvxpBR6ZxXGUZXXmI238G53_uWBxPMjvuytETGiWqPfTrPbLsw9kK3xfDTGL5Qws6WnB-5oglGCcIENmhe0fNy5MNmiMZqVt2GhkZ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ae8867bbe.mp4?token=SulqpFFJGODw5SEoqYf__vm55xzGI1SAOJu0zpYaMyW3kpnTV7bWv3qx_zafO3DTkep8eVWAWubJy8XTaMmMOv96x7fzJ3-RqCEQ9Zj2w_ZyZrU7k32EeldVOqMvQuxVtUEgjzdh3z_kdM1E62C7uCauRZtmgjj37-7jILErTaacvRJ71L86QFrxQOEJ428UljT7PO7IvknQFNT-bMB3xV3U0PqsUAGyp40IV2d8H9niL_WMvxpBR6ZxXGUZXXmI238G53_uWBxPMjvuytETGiWqPfTrPbLsw9kK3xfDTGL5Qws6WnB-5oglGCcIENmhe0fNy5MNmiMZqVt2GhkZ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل‌های دیدار امروز صبح دو تیم ایران - نیوزیلند در گام نخست رقابت‌های جام جهانی؛ رامین رضاییان بعنوان بهترین بازیکن زمین مسابقه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23564" target="_blank">📅 07:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23563">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b16918ae52.mp4?token=O2fe9sd_eazjnAqoTs7jhRNGalnjSVd9daD9y3vwTgM_0Sxxvo2A0Eafu5rhCkArqVGcCqDXd7b1yK92SkGMbo91TTkCq_k0ah8uJDR9SLP44DtGJ0JjUr_j46xMCJ6VLKxLTU8QEh9YFTw3Wiqac2kqBBkU07599dmdAck-RqBMXBo3lWbIm1hUZj4hGrj4e7fOuOpZbGjvyDypeJetpy68OKgGXjlFCkXzJ-Ny_f3CrfP_XVno3cdjbwi_WbBs8OCYdzbAuq6ow55k7Lsful-Fn9kojrb9T2TW1CrDLll1ZAyJL7pzwQHXvE4xybcok9ZpBvmr12nzUD_YUc6izQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b16918ae52.mp4?token=O2fe9sd_eazjnAqoTs7jhRNGalnjSVd9daD9y3vwTgM_0Sxxvo2A0Eafu5rhCkArqVGcCqDXd7b1yK92SkGMbo91TTkCq_k0ah8uJDR9SLP44DtGJ0JjUr_j46xMCJ6VLKxLTU8QEh9YFTw3Wiqac2kqBBkU07599dmdAck-RqBMXBo3lWbIm1hUZj4hGrj4e7fOuOpZbGjvyDypeJetpy68OKgGXjlFCkXzJ-Ny_f3CrfP_XVno3cdjbwi_WbBs8OCYdzbAuq6ow55k7Lsful-Fn9kojrb9T2TW1CrDLll1ZAyJL7pzwQHXvE4xybcok9ZpBvmr12nzUD_YUc6izQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول جام جهانی|توقف شاگردان امیر قلعه نویی درگام‌نخست‌مقابل‌تیم کم نام و نشان نیوزیلند.
🇳🇿
نیوزیلند
2️⃣
-
2️⃣
ایران
🇮🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23563" target="_blank">📅 07:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23562">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
هفته اول جام جهانی|توقف شاگردان امیر قلعه نویی درگام‌نخست‌مقابل‌تیم کم نام و نشان نیوزیلند.
🇳🇿
نیوزیلند
2️⃣
-
2️⃣
ایران
🇮🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23562" target="_blank">📅 07:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23561">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErCIv6sVTOgt0Z_y2yhXGnRCEruEcbymvqa_624wLa7XCXcjNEA0MFH7RzbBEsSepO0RBrPaxkRCL-xPC4-XM0at7C2A8BEsFB6zCMpmj4qOlYrSGVmf3oj-YoAyQFZg5gH_-6JgRa5R68ZWw7LLMLCYR2UhTMaViyjXDaDt5id9tzZxIaOtIBAFTKN1QJE4N-pBjjeLYCDsxgLke64LJhymqBEfegz22nVB8bJxrM8n8bR35gUJXXU9ZB9nyuK4Mj56wUOpbked5RfuNREXXJzW_5UwGLtAGhV9f3iTeS08fr0xJr1gyKopD6M0eXo6bP3sEzGKjNiBSOKpkLKxFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ از مصاف شاگردان قلعه‌ نویی با نیوزیلند تا اولین قضاوت علیرضا فغانی در تورنمنت در جدال حساس فرانسه و سنگال
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/23561" target="_blank">📅 07:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23560">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hL5KFY8EuskqjON7JH__rZZmaQfV4CawGWWz0A3AxaJ3gf376uBjwWvSWVUuxZxpSoK_7BcmzQjKemxsxyJ85YQUGgHbINLGhvoLfo8zT5fGX7oPbGC6Lw_zFvdYDmttgW4HCJNfx__wFDM6kxBbKYmwg5BMG2AduND89dfK7ZQESy63rW5WSFefAezm1dlOpFTlPHLkJVEcOg1RMx_Mu9D_t5W6RybATmntHlBGWgf5UjV_N5zjJ_xUW9LeGdvUBA2PyolscIygfFMN1VZ_xkhdikiXV_F5qiaykzQCzlpB7iwm5F3wWKR_-qYRMp06SrdO2CBy8OuM4W4ZK5D52A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احتمالا فرداعصر ازتیم‌جدیدکسری‌طاهری ستاره 19 ساله فصل گذشته پیکان رونمایی خواهیم کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/23560" target="_blank">📅 01:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23559">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHn6OJP0JRDJNYx81jHQGUYxPyZhi_HsDGjdyZXcIeoQpIJGNwhfhm7K7wr4JZYwhEP2uxTsnBzYFcKWxNR9W5trZiSQjB4Mjqc1t4THBRDRsPfDbb1p_Hy1LqpN5mEwXRmxZzPh81lKo-WEowEJ6fBdeTGoH_SWS1qb5N6xrInBlYL31jChvnfHJzl-8SPTDdiUqW_D_CFkFBkZTuFDv8ujZIL2k0_4kgb2JHur7aFoRW2xxinjoKwx5h0TfLC2DecNlF5ZFG9Fi5hIXoluU861k-yktJ-4ggiYFFT4KC0Insh4ohh_ZugGyQb_zTsnTyPhFDRVH83YZZUH6gxAHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وزینیا دروازه‌بان 40 ساله تیم کیپ‌ورد، قبل از بازی اسپانیا و کیپ‌ورد فقط 50 هزار دنبال‌کننده در اینستاگرام داشت و بعد از درخشش در این دیدار و انتخاب بعنوان بهترین بازیکن زمین؛ تنها چند دقیقه پس از سوت‌پایان بازی، آمار دنبال‌کنندگان او سر به فلک‌کشیده و به…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/23559" target="_blank">📅 01:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23557">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQuOpqrOi7TyGzoYE8plG0-_7cZZMaXUEmhV-kHjHxRQBbrkOZXwRwBSxhUroaV4bSWo39vOPaUnSbSGnZ_Bt8RW2oPfmMkNtsYA4yfYIHEZW-NseLIBleum-i6UWcDyXFwER0HbeG3lBtCij3sa1HGkxOPJFwo2oxvJ7I7SEglJ0CmaJFWI0JwcXkp9fMNj-KYPrmQdTdss4jlyb2BDGwXzvEbW7yss-6ckwTKGej406Fy7vUtGgko8T_XtYchqZX5myZMfm8GuhWzeX4VRgi9_DaKfLpHYevA237gyjgdejxfvTg_FBt-M4iB97BwrXekD7LUzEzXcxBQjm6tsbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از مصاف شاگردان قلعه‌ نویی با نیوزیلند تا اولین قضاوت علیرضا فغانی در تورنمنت در جدال حساس فرانسه و سنگال
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/23557" target="_blank">📅 01:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23556">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KF9At2nXH7T-_epuSWfjeZAKrQHL1hrGzyItV7wWqMlthiYcRbTF60R1rMREk5XVm9fDCtUMmyziSApNI0QDVvIlzYPxADVa7o-FWZqceCZHSEFkL_ZcEjw6VxlEYcFheuZEgKQVmjyQlfAjq0NAcFaAcwZScU4DrW-jNQGYvrzCvgzg4t14To1cPjH6q42sY4NHFbx3GjgsEKO9Db5BE_KzsoeHLDHSCWMS30P0EqqX0yWVzrYbQYK2necrKIIq5KGJWv3x226Z-iQPniET8LBPND57YMK2B_3jylwKBDRUVgYVp-mS-g1axzYz0-aW2g1ivlrNpI1Xlf19roXJ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌‌ دیروز؛
از آتش‌ بازی سوئدی‌ ها بادرخشش ایساک و گیوکرش زوج خط حمله خود تا توقف‌غیرمنتظره‌اسپانیا و بلژیک مقابل حریفان خود
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/23556" target="_blank">📅 01:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23555">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11adede3d.mp4?token=MgpILioFMrNUd19ya2g0s4SNYWHM7sWt-aKLvCUzalu50eTK_zj_Zv5jgKIsaO_gm6819iVuZznNb31ns1W-S3ZFxOD255viDgZoc7R_gXC5ejTNri8LvqA1_Y-qcPsBmL81SsbZI5u3pAK7sEHoUo9AjjAsbqAgT3hFmVnpAN4Vag6G36ERW9jMycr8GI93atazlEqRrJtoSiMolyds9ZtduQ2Nh3B9A0nN3dCVVTcQdDl4mUAXt3Mcwt5TtGtxYiy6qenPLN39VRQrCePZPYHdyrT9jvDe2wn7TuDrVeiw_Yf2xBbvwHBp9gYvyNS5RiBVWxlbkiNtYdPuj7E15w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11adede3d.mp4?token=MgpILioFMrNUd19ya2g0s4SNYWHM7sWt-aKLvCUzalu50eTK_zj_Zv5jgKIsaO_gm6819iVuZznNb31ns1W-S3ZFxOD255viDgZoc7R_gXC5ejTNri8LvqA1_Y-qcPsBmL81SsbZI5u3pAK7sEHoUo9AjjAsbqAgT3hFmVnpAN4Vag6G36ERW9jMycr8GI93atazlEqRrJtoSiMolyds9ZtduQ2Nh3B9A0nN3dCVVTcQdDl4mUAXt3Mcwt5TtGtxYiy6qenPLN39VRQrCePZPYHdyrT9jvDe2wn7TuDrVeiw_Yf2xBbvwHBp9gYvyNS5RiBVWxlbkiNtYdPuj7E15w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
نمایی‌ازاستادیوم‌سوفای‌درفاصله‌کمتر از ۴ ساعت تاشروع بازی دوتیم ایران
🆚
نیوزیلند در جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/23555" target="_blank">📅 01:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23554">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a904e7169f.mp4?token=qF9oFdOJMUv6Xx-EA1OgVol2Todfm4AMhe-3Tx8Kanz2pdL_orreuM32u1U55de0mR5G5iOQ5Vy8SZ66ZctxE70MlcZ66wF62FHZ_kz-a7rx97MdnrII4N9d7i-0c1IIamG6NbDaZQDI-R3KX5hPd2UOzBNFJwtr5DjHwxSvdaPorZT2R8tqJqxyXVEVpgpAqimCnD51y6K-DqQpFqxOgdAOYi7fcxhgZnxr6VlgYCkQmWYO-sDbTqpoZsypbppqPK7uDY-FDRmewBWUPsqY220qLZRqOSdNjwf-KONIQEoLtP0uryj7JuZsYWobAYeMj3Bjt5vBLiEkJzIRCgxHlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a904e7169f.mp4?token=qF9oFdOJMUv6Xx-EA1OgVol2Todfm4AMhe-3Tx8Kanz2pdL_orreuM32u1U55de0mR5G5iOQ5Vy8SZ66ZctxE70MlcZ66wF62FHZ_kz-a7rx97MdnrII4N9d7i-0c1IIamG6NbDaZQDI-R3KX5hPd2UOzBNFJwtr5DjHwxSvdaPorZT2R8tqJqxyXVEVpgpAqimCnD51y6K-DqQpFqxOgdAOYi7fcxhgZnxr6VlgYCkQmWYO-sDbTqpoZsypbppqPK7uDY-FDRmewBWUPsqY220qLZRqOSdNjwf-KONIQEoLtP0uryj7JuZsYWobAYeMj3Bjt5vBLiEkJzIRCgxHlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
🇪🇸
دین هویسن دفاع اسپانیایی باشگاه رئال مادرید و همبازی‌سابق‌سردار آزمون درتیم رم: سردار همیشه به من می‌گفت باید بیام ایران و ایران کشور قشنگیه. مطمئنم ناراحته که در جام جهانی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23554" target="_blank">📅 00:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23553">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhF8p1wsWr_ooVa_mcdTj0m3M-pCVA7ueMwKCxizOMXLAyC-oCk9zlQzG1_hkJfC2F1w0kbpQAh7ta_UgHNZj-M3zgOSjDhsXGl2it6mmrOu1gR2dIpreMbgiXD6iYTENz4p4R0UWPli0HeylQQVN37S358HLMHFKrBbGH2agDuLCMQfTNW8T3QYL_JKRQP1hMTLKSWQQvwypF3zmGrCSYOt0Tq1PPK-EalTqFnViZvfPEDdtghHCmTzPMNafdQUJ2sJCn-nFkhq21O1kfLvDzVhyGHNcHNd3Evka_VwBMPEnUlWDaSOq6QjsjwPYy9lmTIMrPzCxc8r5PlIDrZH3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه‌بنده‌خدایی امروز برای اینکه 85 هزار دلار ببره 1 میلیون دلار روی‌پیروزی‌اسپانیا مقابل کیپ‌ورد توی Polymarket شرط بست و الان همه‌ی پولشو باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/23553" target="_blank">📅 00:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23552">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPuhRwEn1Nhfwx2Oc3GPxjDIUS0iGqM-NXHhCQuiF2rStqRzjas_gVW9n9hdimZMAOhqKHT5w9zKTSxJDisb25VspA6oQQdsZ0DPvigvQ81DEbCOwI7qMJDuJlASSmD7V7lyXvdTRj28ZNyAGCDXnwtMgnllYPgKo_sZn9_tWBDs526FbCIa4cvz_cQb2LVeDkIqX3VB2wSeCg2SbMAe8pbr0s2QWWRvBF6aBKCRLHJfJuUQvMJth1BAhIhYkas35yIQ4MNG76Lb_G9FG_vI1P_lCG7jLJkmji_JUf-rgcWOaGTWN0Jf4KK7EoJpVxlS6FnTElRTj-S5SpMFqRJpKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇬
🇧🇪
این‌هوادار تیم مصر پیش‌بینی کرده امشب مصر بانتیجه سه بر یک بلژیک رو میبره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/23552" target="_blank">📅 00:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23551">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIa0cKEVVrGUo4X4ZgDeVFZChZ8nzyxRi4ozrlQEUDVZxpKzHXJHZOnrZnzyvcfxiLLJB1keOvQX0Izf8-tyfpymyZvTj__jabql7YLxEtkgMi0engLz3ealXk4lnBiw-TDeTBC1tu9orJEw81cGsQK9nJyYaSCQGif1j3YEXTSLSW093pkV4i_WzPGOjekhnPPKp7yQESEljJsfwLkh4EAV_tyPscq0On4IAk3DS29xnk0Nhd3fkLw9z4vifffeOMt3o-7Y9P05fl5fEEnepzfWUkZYtkuAtts5odwFhMyXO2A53VcpqHC76jTdXp8UKU823McRJ8HcZBgPouTAyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ همان طور که دیشب هم گفتیم؛ نماینده کسری طاهری مهاجم 19 ساله روبین کازان امروز صبح با باشگاه پرسپولیس جلسه داشت...اما طبق‌‌ استعلامی که از مدیر برنامه این بازیکن جوان گرفتیم هیچ قراردادی بین‌طرفین امضا نشده است.
🔵
جلسه‌نماینده طاهری بامدیریت استقلال…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23551" target="_blank">📅 23:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23550">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_ZTHwSjAlgA6lYNtJSl9CTwEq921w7-efrpw2g09mpdFpEcFQB9ZCmAOfCRW8ciOGt2Q2qI4HF9q2ao_6yVRRJlF35-UZnAS57ET1oP99omEHbgGVZN6sT0qHaUtMj7RsJlZ5lwbzndGgqFCkHllreBRvPPug91L1shEl6rg-nOcYlNbA1RRYr3I9Lz09t652z9T_lAhROsacxn3rtq9bJC8glJqlHVGET4so1P2UN0pLp4h9Kccps4432Js9u3655_FZNOx3ddrs8CSRx-ya7xV_ec4jVuUuMatSveA0zGNsBRcXGC97rf1F3fNpVAavIPoTAKMsrVwzGjIFfgCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇸
تیم ملی اسپانیا در جام‌های جهانی اخیر:
2014
: تنها یک بردمقابل استرالیا و حذف در گروهی.
2018
: تنها یک بردمقابل ایران و حذف در یک هشتم نهایی.
2022
: تنها یک‌بردمقابل کاستاریکا و حذف در یک هشتم نهایی.
2026
: توقف‌در‌بازی‌اول مقابل کیپ ورد. دو بازی بعدی مقابل عربستان و اروگوئه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23550" target="_blank">📅 23:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23549">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdbLJVwHEVrtEIetgL1xBcVXIItf5fRdlmhYZfitPoNeKZc1ardfLA7Nfl_tbkhNW6Crm_NBjKVUvighHb6sdCbq8P57Y86RXmwrgEraQf4TRDPdZWGhOUn6Y_zh0hZ767yfDS8FVSOyfI212OvJ0NYqtUqvKygFzR5fdspMujA4yCMNy6s1K8CEy7R3PDXWMHJMTPLlhcW7Sj6qyei7eUvcsuBa65sjABMBh5pZpZPqbBVKx680hQ1HhUm2rheRdHkpQcGHRn9nQc6i0P9xs721FT2H58j6u15iXJQXv05cGPpFGZp4MeTWW4VA8zxmuPKHrVX2wKfzpWbzd1VKOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل‌های دیدار امشب دو تیم هلند
🆚
ژاپن در هفته اول رقابت های داغ و جذاب جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23549" target="_blank">📅 23:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23547">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392bb7bb0d.mp4?token=MLkWd69Ax77VW_tYtwB4Z4fdRmifu-vH7auSgLJpInLVDs95HDc49IxH0VR8WaZM0SOMk4qcPF5cZ7PKM-KgHTYfYmu8ackIlXDySeKYM6zkropK1VWYVWfPrB-cEY0R7e8ji6c0IOh9dRlxaEA7tCvbg__WKU1LW54h0wbHsjOipQU96vgEqRjwvJ2tku-ApCJgFaESwSJFFugl0C4PRxwaLUC4_UU3K71CeWoHxqnMs2_dc3sZQo5a1eeIgzJqSlehuvQCTNH-s0NKaBEBXSkpk8gBOFgnqEq4poJFD1BCRzxDEKXMZ9O4mXra_c603hZjBKOU9S1XQFT00MpVzGDTN1bkvmMbs2SJaFcXDsqPbhZThpSlLaEPxFllQmesdV-Wi277lBJZjIadL3r-37rAGsqYT2D4D88V49DVxTkTHVHeFs2ABXyfzqYTjmzy978GzcfFcwTYorW9_MrLrhZl1XjfahI0lDggQpOto3ZDgx6gZ14BZCQ64MzyfqNxgcZNMZq_oS3MuWRK88fJkmMGF0R70zB3HHglTnRQC-B6RObcG7lJMa3EmHFIFZ-hUxR-8c9qnJCnje4cX7yhtydfED_6dJeOKCgCBdgYAfWIgCEOG51JtVKKniJT7RD_Dw_ZRyWxBskD-8BldTZ0F_O2xMY0r3A-fd74kC5kvcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392bb7bb0d.mp4?token=MLkWd69Ax77VW_tYtwB4Z4fdRmifu-vH7auSgLJpInLVDs95HDc49IxH0VR8WaZM0SOMk4qcPF5cZ7PKM-KgHTYfYmu8ackIlXDySeKYM6zkropK1VWYVWfPrB-cEY0R7e8ji6c0IOh9dRlxaEA7tCvbg__WKU1LW54h0wbHsjOipQU96vgEqRjwvJ2tku-ApCJgFaESwSJFFugl0C4PRxwaLUC4_UU3K71CeWoHxqnMs2_dc3sZQo5a1eeIgzJqSlehuvQCTNH-s0NKaBEBXSkpk8gBOFgnqEq4poJFD1BCRzxDEKXMZ9O4mXra_c603hZjBKOU9S1XQFT00MpVzGDTN1bkvmMbs2SJaFcXDsqPbhZThpSlLaEPxFllQmesdV-Wi277lBJZjIadL3r-37rAGsqYT2D4D88V49DVxTkTHVHeFs2ABXyfzqYTjmzy978GzcfFcwTYorW9_MrLrhZl1XjfahI0lDggQpOto3ZDgx6gZ14BZCQ64MzyfqNxgcZNMZq_oS3MuWRK88fJkmMGF0R70zB3HHglTnRQC-B6RObcG7lJMa3EmHFIFZ-hUxR-8c9qnJCnje4cX7yhtydfED_6dJeOKCgCBdgYAfWIgCEOG51JtVKKniJT7RD_Dw_ZRyWxBskD-8BldTZ0F_O2xMY0r3A-fd74kC5kvcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ماجرای شیر نگه داری علی اکبری قهرمان بوکس چهان در خونه از زبان خودش در گفتگو با ابوطالب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23547" target="_blank">📅 23:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23546">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d02367735.mp4?token=XlU4iBZF_F7yNSTqusrxZcnxJQfQciGQnFfl-R-MJ2OYFjZJhHLEOLlatcrA4VkDcrAkPClFpdyjZEU6bJGVT0kt9m-YYXXk3f7lmD5y_ffKfqR-_8OCRgim39h7J-C8_jXaKZOlh90FcLxb_zjdyKqVEbv77L-JFW2YXg-dN5NFA1GigfsPgtj7Jra0Vwxm2qcSd6OnRpS0Y4-VmUShFBaq_ZTIPvaLekC1dTcz5iXVQoJ3SnUnig0XEFWUYMVy_oBcDGzrrzpk3MIl66xec378dDmxtAcj8AK3DiPBjoemB54fYqQRqcfiCXyZ47HwTdT76KwVoGXGNlK0V2602A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d02367735.mp4?token=XlU4iBZF_F7yNSTqusrxZcnxJQfQciGQnFfl-R-MJ2OYFjZJhHLEOLlatcrA4VkDcrAkPClFpdyjZEU6bJGVT0kt9m-YYXXk3f7lmD5y_ffKfqR-_8OCRgim39h7J-C8_jXaKZOlh90FcLxb_zjdyKqVEbv77L-JFW2YXg-dN5NFA1GigfsPgtj7Jra0Vwxm2qcSd6OnRpS0Y4-VmUShFBaq_ZTIPvaLekC1dTcz5iXVQoJ3SnUnig0XEFWUYMVy_oBcDGzrrzpk3MIl66xec378dDmxtAcj8AK3DiPBjoemB54fYqQRqcfiCXyZ47HwTdT76KwVoGXGNlK0V2602A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
وزینیا دروازه‌بان 40 ساله تیم کیپ‌ورد، قبل از بازی اسپانیا و کیپ‌ورد فقط 50 هزار دنبال‌کننده در اینستاگرام داشت و بعد از درخشش در این دیدار و انتخاب بعنوان بهترین بازیکن زمین؛ تنها چند دقیقه پس از سوت‌پایان بازی، آمار دنبال‌کنندگان او سر به فلک‌کشیده و به نزدیک دومیلیون نفر رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23546" target="_blank">📅 22:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23545">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOl-Xtf_Ey6Sny6f6DdoAMfCDJW01KPZamuwnr4R_d8NcM3lE4D1BGneMd0fYZQCGOff4nj4NVYDmyem2oQlt3BM7qYwtAbzWAvQfsDdomEHr5qFz6jXDugme8DFs3OWjD0e-Nt9E_ovmaFWfNQw4sOujKIWiAuBSsC20wjQBQfSNptHRz2Np5ZyFkeK2a9oWlA3MD4ZYQyip_yDfyMII4q_Q3nas77N9PfgZvxyRtB55efO2F-Iz3QrZsr_RdnNrlEv1yLvL1aiSPe5V98BKqtUSJHSiE9t5SFl-lMUhgyhN_VdbAaNDd8c45jnBe_HuTnUSnOa8kuII6MQ-XSV2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دریک رپر معروف کانادایی یک میلیون دلار روی قهرمانی آرسنال تو چمپیونزلیگ شرط‌بندی کرده.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23545" target="_blank">📅 22:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23544">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZThaJJKCtIwaOvneip5hGcPfjzAxmsl7XW1y1hxW-YDDWFahToXqFXnAI30ZAbi0qK9joKa7is77RTKJfBPV8xTHW2sQl7ALkj4cpE0_dNDrIy2Q1dkVuFZC-CmRblhimee4_sU_FGtQIqVUj5XcsLJ2n-FeDUe3PcdKh81Gm6oNJkZAAVzMBxMjbEKWSLZcJc-6hDdd8WzxcuYGAdDhEfVczQuFpyCfhrVmBILK28_m93g4wY7iqSiCCGTMQBx2rMsmVMYTOb6gNQKnzaGAdquPsZoa1xtQ9uClHmcpmSfvjhUCNtm-dka18LTpsq1Bl8TSIp3Dtxn5YExM3iJbHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
جلسه‌نماینده کسری طاهری با دوعضو هیات مدیره باشگاه پرسپولیس دقایقی‌قبل به پایان رسید؛ ایجنت طاهری به باشگاه پرسپولیس رقم مدنظر این بازیکن روبرای عقدقراردادی ‌چهار ساله اعلام کرده و منتظر پاسخ‌نهایی مدیران این تیمه. جلسه با تاجرنیا حدود دو ساعت دیگه درسعادت‌اباد…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23544" target="_blank">📅 21:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23543">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q957p4z5pSFgnkEo-WoMPnhL7MTlLkn3NwHW8BeyHw2ti91WbSER0nwlog2QGLnQKuRznPNq2WPMLIl7jlzHJJFnRw2GP52rkUlCM5PeGAyug6NAtRT2DjPZgyiIKI8s3-JDJGHAtQOlkxICdZ5vDk7M9xlbKmMt86VcQjW6fo0ZbZWDJ-kNj9DyWSjSFOZiAD2WBcDFE062KVQLPetcfRvl0U4uUS-Mi3v12k0-Fd8IC6KV7Bx4lPAusGlIpmA3r0oEUzv5kBvJgrgtHjo8ANLuvaqMSxT4wpfvViDJQTx1ULd9PZhMFHFxl6HjlAwc7ODZsRnbwi6mqDuXSzQoUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026|توقف لاروخای پر ستاره مقابل کیپ ورد در شب درخشش خیره کننده و استثنایی دروازه بان 40 ساله این تیم گمنام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23543" target="_blank">📅 21:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23542">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lF-051rkXhv52Y--Bdh7h5S7YV-5Y6GmCrDrvxxTrmsT5pU32URIZ4YaNSu5wJSzVTFjwJ0Au6NwAWvfW9ftBNxn7S2cGvAif_OiKdatVGLj7nkXq16toG8a4isL1bOmDO_rPtuEqj5mxZx2HTv6KQh8r-SRXBIGeGl0IQUI-SdoL3SPP7chyQgUs01d2CjHwpDSU4uXyIhLNVIN31er4ms_krZ2B6eYowFA9jDsNEJHnllSjp3MxSZTTQCff5yjR_cyrxiVI4BUq1dVQAN8qMNhSSDtDAWVjqnDXG8eDEk4OR1zfBv43b_0_lsD3OONnQ_A64wnXqX7PCqLeqNg9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026|توقف لاروخای پر ستاره مقابل کیپ ورد در شب درخشش خیره کننده و استثنایی دروازه بان 40 ساله این تیم گمنام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23542" target="_blank">📅 21:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23541">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URLo8LtUztdU9ReAQnf1s-443icSgmee3-NH84ShWlH6nSjwU4gijGwB4Tnjsk3T7gZcH-Td3Ry3yJcIqWSJ--de1LF-SdgD6j1oW6myUVHw8_GIyM5Pk7Edt4oN7BowmsNE6Yne8kIKN3RnszjrkfX58e4xyfVW-taYjXH9SATFQBXunHvCzk4YDwveTptQ-tXIF2UfBoVab9WlH-EjJWHMkABc4Jj5ubYwGKPYgvJ60rheBo06GIRUJRuV4QU5Dh0TdmSFdzPVqaPbGFAPJP6KSxzhjzm6sViNmyn3fTuSPprOMx_6RILGZtWbnN6aZ7ae1orLNl9FxSgJB02mkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درو‌ازه‌بان کیپ ورد در نیمه‌اول دیدار با اسپانیا 7 سیو موفق داشت و مانع باز شدن دروازه‌ اش شد 40 سالشه و ارزشش تو مارکت تنها 50 هزار دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23541" target="_blank">📅 21:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23540">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J97wm2tW34QSOgshaMXM9PBAcoMvxI3Ar1DVE1MlWgleIyUw7h_qN2BWYzNxCr_5rUh3lUzbzop1-rYMbLmR3jz-boiCa5tIKIHmk0UT-8oxZu4xqquAUHJpJ-yVWCGi0yR829KjGXKB7L9thgbnQw5rcKxsVibhROjgz0jauXxy1grkNNPWVLqaAkbDSdqfm2Z35_PUih-pVQhmsur82nlDMB0_9x4AtdveC8FKfSLBuDooA1yyPFSchrwnz0BSbADcBfvR8G7Mgy8egkeNphW7mydzOGMbTS6n4Dy2_l2NXTRuAwUFSDlzaZqbwYe0cvgLi8KSsx7g2FNKIYhWrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
برنامه‌دیدارهای هفته‌دوم و سوم تیم ملی والیبال ایران در لیگ ملت‌های والیبال؛ هفته اول تموم شد که یک برد و سه باخت برای شاگردان پیاتزا حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23540" target="_blank">📅 21:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23539">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGsL3ArLJWhAZ57yjmOFgqW3pumZi4UwhB5r7yFnrdKVruIqMTOaT-EOVW56N8LceywLNLYUkBrdJLDLtJDvEXnYYKd05D8Tx6tLo8zVd8xzvFez00fnjE4fJri70XamP6oX2gteVmYVpQvxX8nuseRYaZSTJCiPQnD9bXcqWgPauNJSCMhK2DWWPXtdTdldd9LwNCJ-fX7XgnDI_QaH6E77lO1WbZtwgdvcWJyqgb3XycJUuGLaI9eNFtB7Ii7CMjbhj8AWWKXlFop8XWNOlob2VwyLSpzJkFSyev2r8CbKE9OwtA_-70SYvuQzDlvvYeTymftxyh-PVKSXydWtjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی جالب و متفاوت‌از خرید مارک کوکوریا مدافع تیم جدید رئال مادرید توسط فلورنتینو پرز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23539" target="_blank">📅 21:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23537">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLYLToLHB9m42jnComOboe81kCUYXexeQ0nBPO-YUqGNU6e-hP_luQg1RJXj7O4EmbMRCcLMRMou46WO8iIKm27wfjOIposfivJB_ft1XIGIMpeIhS67_9JMXUGjr1CUKX1LfiC4P6jrw5K8XSMvU0BPM2WUIF0iSFP5sxlV0cLaUSa5qoR61KMZ0xDohkGBhNZdRImDpv3FZ2Xa1ht2b9JWGdQ2foPsAlNzbrtcVGzQYYGv9rZM5iVAoEBA7dd-L0vHMnJ3AL2iwV-0ZxAuX8oDFln19V_4sKSyEJ7k7b-S1Ck2B-V9FwE0c7Nqs6qjtHXyLid4_Min_VtFUCoNSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی رسانه‌پرشیانا؛
فرهاد مجیدی سرمربی سابق استقلال پیشنهادی دو ساله از الغرافه قطر دریافت کرده و در حال برسی این آفره. احتمال اینکه گابریل پین به کادرش اضافه شود نیز زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23537" target="_blank">📅 20:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23536">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7bkR_ROL4-yZIAyOOvSZCnnI60sHZUVvLqP8ruLNyFjwoHMXDNZx9zRQNp4H9LeOvGw3OcsNhuCjPSsr8vzJ7UTNb6qdQDKyVnnQlUBr5HrUW91hu6RI9HH-rzaWDwFhnUwqRqT8HDxwTuUswurewo9kBmyd1Urf1vQgDLvb4Y5q1439qL4GXxY-CyW5MQfRsW4tGSqP1RbV_pz3BDtBhUqOZtbjLsbcDbOCfGXhnzbkOhsLhrtAKPuW1tNX2PBFNU0r-yA4Olein6uN22HQcfAKZeAXqDwEP204TDt-gj3og5MJYrjqkOuhyYky8BZ6Ot2-AbGmkzTJHuulph0KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ از آغاز کار ماتادورها در جام‌جهانی تا دوئل تماشایی یاران دیبروینه و صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23536" target="_blank">📅 20:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23535">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwNXsZG9he9CObVmRKu01hJG8AKlUJ_uHEPmaPhEDb2dLJb6cpP__HYND7Rqp3k30ZSd7tP85eHggFv89asSRDdAiDY-u-A_PUyv_xnUx5J0EdFe6HeUhNqfM0nuNqGn4oOEnZWP7NjQyWH4MKY_BS4QRkwHNQNBHJCqw9bySy7znsSZwAh38UfBHVqW50xkq12fQE58D9-ZAMdmtjMnyJJto35dEIZKtPTfcl7sS_Se1k31nDXmKGvrqV314mohqEUe-fAcManD_-RpvR_Kv_T1T609wg6teYIrjS10G_ZL3FROaPOPAt22jP6zE-dfyZXqxWztBOeDoD3pbKVB8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نتایج‌اولین‌دیدارهای ایران در ادوار مختلف جام جهانی به‌بهانه‌دیدار بامداد فردا با تیم ملی نیوزیلند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23535" target="_blank">📅 20:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23534">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a3e86a106.mp4?token=t80AnadTGnRvmUdh8sjg-JRp1sEc8IIoHsOG_oCkY4FKirtJusnwJW9paTC34QDpwRJjWxHwoOEEWJaFKrhbkdwtv3y0-fzY1DshgbG5YzkuBkg-Q1R3vbLpDWGX_SVJSB47o4BqDp_trKC3ELP8-N_0DWxO8OdymkhB7czxdlAaNB3iCeWcTpxZb1f7Izw-6ksACiplLEQVNgVQZznvyULkUJ2IVzwImcXhN34uElEBP2wnuHiOIjhtIEku046zVL2M67Siqyj1liVpAB_M6q1eUgwbo2YdMgjqHAynSg4XGlnG-wF_h60SDo6WU2yV-QApUhVT0XKt47Zi8ed0Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a3e86a106.mp4?token=t80AnadTGnRvmUdh8sjg-JRp1sEc8IIoHsOG_oCkY4FKirtJusnwJW9paTC34QDpwRJjWxHwoOEEWJaFKrhbkdwtv3y0-fzY1DshgbG5YzkuBkg-Q1R3vbLpDWGX_SVJSB47o4BqDp_trKC3ELP8-N_0DWxO8OdymkhB7czxdlAaNB3iCeWcTpxZb1f7Izw-6ksACiplLEQVNgVQZznvyULkUJ2IVzwImcXhN34uElEBP2wnuHiOIjhtIEku046zVL2M67Siqyj1liVpAB_M6q1eUgwbo2YdMgjqHAynSg4XGlnG-wF_h60SDo6WU2yV-QApUhVT0XKt47Zi8ed0Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
بعداز پائولو دیبالا؛ دین‌هویسن دفاع رئال مادرید هم درویژه برنامه‌عادل‌فردوسی‌پور حضور پیدا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23534" target="_blank">📅 20:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23533">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtjQIxCWkjQrxY_4QoVqDxcTjD9aT56jMhF2gKEhzVszXorA3gMawy8RVRcleqFTEWlDTIIndVY7YbuwOt-_2FTK-uS-5uh5N0s1I2dpVpKfGrYGP4uo5agkDDEQ2ksOZkDXtGjzBSU4Nl7HAn19uiel10QgGGb4JPc5W9KhDAAhNA2YS_3O7AM6yJX1aD7KGKg5WNZE4kmuO_DeBGZndXvAy9ESIg7LOD-AH8zQgu_Yh6mzdBOaoYkdFinOAqSIyxJ077gvbJf5S3QNllYg1VXBBcbNmvKCrrm42h36e15peZOq1uAM9p_SA9sldzaY6jMcYiqYp3tLgD70Lr2LnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عادل فردوسی‌پور: مشکل‌پرداخت مطالبات یاسر آسانی توسط مدیریت باشگاه استقلال برطرف شده و طبق اطلاعات دریافتی ما این بازیکن فصل اینده‌نیز با پیراهن استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23533" target="_blank">📅 19:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23532">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyzIxT43ym1q8fIvAvDH03_NvzaYB-8EfDgcMw2Quu1DT_gBbH7TRqYVpTQSYrcvHVHUI1hjfEcAj15OHsrSspDaHWHwXv6BPSWG06geZgrnsDSBCSYr4A5tbmIDvFke17SLxP4RxM8Z5UpdTu-YvfKZqqNFHgFIlV85v89BtCwpXa_KSgJBwXmnbf_pvPKuC_iWK3ifauRhjcc9eaocj08ft72OoDoTLr_TgVteiqY5UHQA4hqJrdiJ6rdCmmS7QhXSA-avDlNOJO_WvvZylVy2naB-MWqbjMTahdMtTw-KFcwE9yE18JOH166kfTaSLbfY8FueU1KUYb-WLDI6EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رفقای‌گل‌لطفا تو این نظرسنجی که تو کانال دوم گذاشتیم شرکت کنید. اگرم دوست داشتید اونور هم داشته باشید محتوای جذابی خواهیم گذاشت.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23532" target="_blank">📅 19:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23531">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqV1O5ljsZp8GPQKPcSJG8U9d8yEMJC9ADmsL9boYNxeZAcuK3NtxFNJk1fPvKMKYU4Kl16O-RiiZC3ZrSr8WMl8TXgQc6T-UTwrFZeRpdwxkfwO5MP_nMQ2XScn2bXytptGaLRponIH1jJfupnTpWPBDMzqwadQqqBmHKfU82D12BkQV9LUG2fNF0xBqGvDjd4RBTmfALYa7fjBx5GhwiMF3GJPzHnjBJS-OEW7PEWqxWafdPWKb7quNu7Lc4AcxnMlakAPOoN-pz0-3h3KdTWuh2G9E9OUjigHyeNW6k6_2SfqqpRwqHoIVEyPjI0RVgneG1Q03_jF3W7w0iiRig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین‌نژاد، محمدقربانی،احمد نوراللهی، کسری طاهری، رضا غندی پور، مهدی قایدی محمد محبی، محمد مهدی محبی بازیکنانین‌که‌احتمال به لیگ برتر برگردن بسیار زیاده. اللهیار صیادمنش هم آفر خوبی از اروپا نگیره احتمال بازگشت…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23531" target="_blank">📅 19:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23530">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23b2efb67a.mp4?token=RKnKwmq56CzpmOr8rVgQFAMpOawHblZKay2-GSbGp4Ser1-RZ3ErsdcPNLpT7mm8dmsCKT63gq4a_wFixa7iSW3FYojG1-aleLop69iu3eZTT8l5oiHQL-PJgrvR2HNpvzMYHbX2hG6g1LsHwF03mpQUl495lgd-MF53XTZ56EaCEXNWOFyIbVAiI1s6VvaxbySIvSgH_e4WYAhMmaiDRXsONpsqlw7z3QEYzCWVEbipGCXOgiFENW5wSyqDSyh6F06NcDi4rrA-eJdu3gzq6H6cdi8OvpgS9RNTbkSUbRdi9flTV60YKH_qiuWz26fg-Rwbbst2wdhh3iLtVs39-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23b2efb67a.mp4?token=RKnKwmq56CzpmOr8rVgQFAMpOawHblZKay2-GSbGp4Ser1-RZ3ErsdcPNLpT7mm8dmsCKT63gq4a_wFixa7iSW3FYojG1-aleLop69iu3eZTT8l5oiHQL-PJgrvR2HNpvzMYHbX2hG6g1LsHwF03mpQUl495lgd-MF53XTZ56EaCEXNWOFyIbVAiI1s6VvaxbySIvSgH_e4WYAhMmaiDRXsONpsqlw7z3QEYzCWVEbipGCXOgiFENW5wSyqDSyh6F06NcDi4rrA-eJdu3gzq6H6cdi8OvpgS9RNTbkSUbRdi9flTV60YKH_qiuWz26fg-Rwbbst2wdhh3iLtVs39-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی جالب و متفاوت‌از خرید مارک کوکوریا مدافع تیم جدید رئال مادرید توسط فلورنتینو پرز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23530" target="_blank">📅 19:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23529">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZHtivKuYX0jKAq1zaJlcBy2M6Q-vcstvj7yxsMqx2PHFA2EL2YdFdZMexjc0_98mxoCfu_bge5-2iP2tQuRR1JGZR6Y22bi5_B16v9JaX7OYzkcG5MTpPbft78GE7WfSH3ivu3oisluNoMEcETGpH9odXCmbvHCzXjepEuwNK2TdRpIH5VcvxOuoSX9FmUIJ_z7Z1FhcApx9h_Lm6xwuFt5NyDPYGgiGeI-HNQlAwZ_SixIfqmpvJviA56iINZ7I4ACAXM00FUXkZDCaHY-oUxpmzLcSoXf9dl1JVCStJ9VD44AhIQUghWmDAuWEfo9oCt-ql_Ce3A-lPiZmTHmog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تایید شد...باتاخیر چندروزه باشگاه استقلال امروز صبح مطالبات معوقه یاسر آسانی رو پرداخت کرد تا مشکلی برای ادامه فعالیت ستاره آلبانیایی ها آبی پوشان پایتخت برای فصل آینده بوجود نیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23529" target="_blank">📅 19:11 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

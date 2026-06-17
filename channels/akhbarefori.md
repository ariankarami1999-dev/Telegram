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
<img src="https://cdn4.telesco.pe/file/QxbYo3GoczwfkbD4gZCtl2dWB-8RKPGH2FS8rVQCuKwt_rUNNbW1NTvXSTiY5mTklEQYzeT7G5xKIVXkL26Iy92Iu9mX080k4QXMJ2S01vBcub4f1fDE-igTunWPn4Wf8SZK3_hgbivtL8GLVQltLzold68MOxNLGJkvuavRBzpfm11IYv_9Hh15DFF6BbOiRmbXJyrn3lWUgGWKQgOSC3CmTt1V-MhK8-h4AwgZJpbonB7k2NXAAnBmvveUI6Rp3wmOwxtKBCIhx6qT0kTkJdWNwfesMgxMHNtVvbeNglN-EAzDuokdeiF1LC_swcmYBBSCNbS6GZAwbBaOgMaECw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.5M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 13:42:08</div>
<hr>

<div class="tg-post" id="msg-660359">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
از تسلیم ایران می‌گفتند اما حالا از قدرت ایران حرف می‌زنند!
پروفسور جفری ساکس، اقتصاددان و تحليلگر سیاسی آمریکایی:
🔹
آمریکا نتوانست ارادۀ خودش را به ایران تحمیل کند چون ایران دارای ظرفیت نظامی قوی و پیشرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/660359" target="_blank">📅 13:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660358">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی مجلس: تفاهم‌نامه نیازی به تصویب مجلس ندارد
بروجردی:
🔹
یادداشت تفاهم نیازی به تصویب مجلس ندارد و فقط قراردادها باید به صورت لایحه تصویب شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/akhbarefori/660358" target="_blank">📅 13:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660357">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3219a1fd4.mp4?token=kWYXydlRozJVSL-32h7FxSPNx-8TrNNLUrSKM7_g7hs0JYxg1BVnLjBTmJdDUUl23MXAOsJOutHabnLsxl4nPpXcDMYrL0blYayrQBRt02l1xcCBzDwXNGKIBZpeAQ-7YyAemjSAMH-INqHJITjDWKSTAynzvXNysYty1MCKZ8xzBkdq7Gh5YX39S_BOMRomCD1tPKkfirir-4oi9LHkFkdKxjpf2AYMSNH9zRqn6XXRxhADrJ_dGTzBv_LzgPw33lwZ0ZaOPe-vqXw2OXyX-BTViG72eQ7eSFgtmucEbuDASto8tkhatOaXuB_Boz5yg0-sO2dzS4V5DgSgjxtSQndh81b74ITLklcJlrM2Og0SECD7AwbtFSCi7YipYLxtZ2OjcH3z8J-7aarW7TDeO4Vtv8gd_8hFV8I9RX1T2pAXJOkho2-XNBto6QxzNVANDI6EzwbNyX4m5lGJ3mramguMSClV-FbmJH2qKDjRDLz_T7mhR9QDVhByzrkdcWnoH1Y2w_UI3jIrjC2BmGR5SPyjXNfXGz7GH6JtNntGHVgJLKOanbvnYjvErx47U-biHMLUpcaGWpcBNn8F3C429uWWpKQEtXpM_qx5tc0VDyuB177bj9SePws1t2iZn_YESGWyLiflZR-j_BGZljQ1VKpCIHkbkQedvHKQ4gVtgcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3219a1fd4.mp4?token=kWYXydlRozJVSL-32h7FxSPNx-8TrNNLUrSKM7_g7hs0JYxg1BVnLjBTmJdDUUl23MXAOsJOutHabnLsxl4nPpXcDMYrL0blYayrQBRt02l1xcCBzDwXNGKIBZpeAQ-7YyAemjSAMH-INqHJITjDWKSTAynzvXNysYty1MCKZ8xzBkdq7Gh5YX39S_BOMRomCD1tPKkfirir-4oi9LHkFkdKxjpf2AYMSNH9zRqn6XXRxhADrJ_dGTzBv_LzgPw33lwZ0ZaOPe-vqXw2OXyX-BTViG72eQ7eSFgtmucEbuDASto8tkhatOaXuB_Boz5yg0-sO2dzS4V5DgSgjxtSQndh81b74ITLklcJlrM2Og0SECD7AwbtFSCi7YipYLxtZ2OjcH3z8J-7aarW7TDeO4Vtv8gd_8hFV8I9RX1T2pAXJOkho2-XNBto6QxzNVANDI6EzwbNyX4m5lGJ3mramguMSClV-FbmJH2qKDjRDLz_T7mhR9QDVhByzrkdcWnoH1Y2w_UI3jIrjC2BmGR5SPyjXNfXGz7GH6JtNntGHVgJLKOanbvnYjvErx47U-biHMLUpcaGWpcBNn8F3C429uWWpKQEtXpM_qx5tc0VDyuB177bj9SePws1t2iZn_YESGWyLiflZR-j_BGZljQ1VKpCIHkbkQedvHKQ4gVtgcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شارژ به سرعت پر کردن باک بنزین
🔹
خودروساز چینی بی‌وای‌دی (BYD) از فناوری شارژ جدیدی برای ماشینهای برقی رونمایی کرد که سرعت آن به اندازه بنزین زدن است‌.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/660357" target="_blank">📅 13:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660355">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
صدای شنیده شده در سیریک مربوط به خنثی سازی مهمات جنگی بود
استانداری هرمزگان:
🔹
صداهای انفجار شنیده شده دقایقی پیش در سیریک مربوط به خنثی سازی مهمات جنگی بازمانده از دشمن بوده است.
🔹
بر این اساس حدود ساعت ۱۲ ظهر امروز صدای دو انفجار در شهرستان سیریک شنیده شد که مردم در این زمینه نگران نباشند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/660355" target="_blank">📅 12:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660354">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
اینترنشال: ترامپ مجبور شد امتیازات زیادی به جمهوری اسلامی بدهد؛ یعنی کمپین فشار حداکثری، تحریم و... کشک!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/660354" target="_blank">📅 12:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660353">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_RFyHrCz1CfZ13L9bYVT-iSY9CJFomCGypTyHdigr_UpLQuSQZXD6KC-0tUimkmCKAkdS5RsyNic77tuG58ajCOat0FOtKEfPh9Ow-159pAszF8AcvSXIQUdbHjqn5ufO5I2LP9CmuKFAa-1j5Ac-O_ov78GFHr6Wp6yjWr15RnnaMRbtpC-G5TKG_clPz3X-n_yaskOJKmPOjFJFqscgmnod-npZXJDupm_6K2o-ktcEYsBE-pD32WTYSRjNWMzTWiDrh879swJwbQQsgMrc_lXjakEZucjv4EmTWDTShk0dKf-Iimrw3MuD9_mCNwAJLIxlUM1SrY0duDlCVOLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برناردو سیلوا رسما به باشگاه رئال‌مادرید پیوست
#ورزشی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/660353" target="_blank">📅 12:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660352">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSExtEa_sjIbAeosB6NPRxib5kpBf7grRknZRJtIQLC397sMA5bnKKs1ozFMCOTbyjW16EUxsmXLCYDHNSPKdxztG4S9XQq8STuKyG34bNLGRuGH1gFiHtGjQlunkH0Nx_mZNkLVfXyiD6ezAnnHdVkSbX42yjs9kARjJ54ukP1fgx1NuZD2tWxwlXzZWLjSbNfCejXDtfNVqKwNpVPCx4YMe2NL1PKS5uzkTkSreMnOkldAzH3r-d2XMjZXvaWg1bBW-GGaGd2stS7E-r68UHAZ1GRwrC_RqW9dkyY4pTJAv22IFrDUoe_Oxq4-OOrk4mIg5mxLWu69QlaHTnXrcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد بیش از ۵۰ هزار واحدی شاخص کل بورس
🔹
در جریان معاملات امروز شاخص کل‌ بورس با رشد ۵۰ هزار و ۸۳۳ واحد در سطح ۵ میلیون و ۱۵۱ هزار واحدی ایستاد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/660352" target="_blank">📅 12:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660351">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hb9RkvnixgQj_xvSnFEqVpY7UI8AZV-pTrjw4Mn42Nr-nS0iu0wOSnXxwbDOFqP45cIGrdQxnIaV4fB278mKI5FTcDQKE9oMvl5EDcyXfPC7nzw86XwVyJjKNgTXsJ1xLBcp4Xd4MJLkUZGYFU0C9YcDHXqnbjSd7___wNu4VALIddOutSTc7V_BRKH-snLBCJpm24tr-dCedz2Uh8Y0WBhSBnyDhfzxzkB5zDS0lPvJr9Fyj90LLQ8d06nuIJ6YlLOKvV6JIVE7GCy00NcZ1ZMYG1pOGgxH6Bj8Qa02atLBlBi0dJ1d3jh5bEwu3otlC5NQJcEXLJQGqamn3FvStA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش قیمت محصولات ایران خودرو و توقف نماد این شرکت در بورس
🔹
مدیرعامل ایران خودرو در نامه‌ای به سازمان بورس، ضمن اعلام تصمیم هیئت‌مدیره برای افزایش قیمت محصولات، خواستار توقف نماد معاملاتی این شرکت تا زمان اعلام رسمی نرخ‌های جدید شد.
🔹
هدف از این اقدام، حفظ منافع سهامداران عنوان شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/660351" target="_blank">📅 12:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660350">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90e6a34dfc.mp4?token=rSX9Ym1zJ5jQ5NVLXjP8PLn0Efqy2_KXYD7sN7wDKjHhwoz8nD5XDQdNh1x2yzqz0UWk8Mau5oBdgwSlkRMJvqcyX3Jr3RgE1Cr9PN5bDGxEgBG1Nm6r4B8gs8qVeNfw-o25at_8c-jHrGltCCddOqRv9ycYNfcHkeRg-gew-CZV_-ZVC3UrshkTwpdfvNujKNwCgxFRVV8RCect_GGxvVzwWVoAF9nb9VfDfbK3Aw0C6LJqUmW_aK_-zbsYxh0DtQXPOZXHv2mBmQO8Dtbn36Ur5IYPwpvzz_Y1HL9Ga7oJakMXxSdVIvbUg_E9rEaeQbq8baR0MEwYgFSaC9brfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90e6a34dfc.mp4?token=rSX9Ym1zJ5jQ5NVLXjP8PLn0Efqy2_KXYD7sN7wDKjHhwoz8nD5XDQdNh1x2yzqz0UWk8Mau5oBdgwSlkRMJvqcyX3Jr3RgE1Cr9PN5bDGxEgBG1Nm6r4B8gs8qVeNfw-o25at_8c-jHrGltCCddOqRv9ycYNfcHkeRg-gew-CZV_-ZVC3UrshkTwpdfvNujKNwCgxFRVV8RCect_GGxvVzwWVoAF9nb9VfDfbK3Aw0C6LJqUmW_aK_-zbsYxh0DtQXPOZXHv2mBmQO8Dtbn36Ur5IYPwpvzz_Y1HL9Ga7oJakMXxSdVIvbUg_E9rEaeQbq8baR0MEwYgFSaC9brfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
مسی از سه گل آرژانتین چهار تا زد، فرانسه هم تخمه‌های کل جام رو تو یه بازی تموم کرد؛ فینالیست‌های دوره قبل اومدن که یادآوری کنن هنوز مدعی‌ان!
🔹
تماشای خلاصه بازی این دو تیم
🔹
قسمت چهارم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/660350" target="_blank">📅 12:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660349">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
رد ادعای بلومبرگ درباره جزئیات تفاهم‌نامه اسلام‌آباد
🔹
یک منبع نزدیک به تیم مذاکره‌کننده ایران، متن منتشرشده در بلومبرگ از «تفاهم‌نامه اسلام‌آباد» را غیردقیق و ناقص خواند.
🔹
وی تصریح کرد جزئیات مربوط به بند اول و مسئله تنگه هرمز در گزارش بلومبرگ اشتباه است و برخی کلیدواژه‌های اصلی در آن نیامده است. طبق اعلام این منبع، متن کامل این تفاهم‌نامه ۱۴ بندی، پس از امضا در روز جمعه منتشر خواهد شد./ تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/660349" target="_blank">📅 12:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660347">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31b02ba16c.mp4?token=C-5ub7S58N_jBfZCDQxjjpK_ctqnmqydgkR5Qmn_S2S1bi_wVfEeUrt1lz6hJxggpZcktvo9WNnRnpc27Vb9T3MWhfpsyW6po8_TpLRLFRp97fmbTvD5y8fx1HReVRV5UerEQo_Y7HEbvkEfs0FLHb_7cybgrhcVxYx_ZWQthy44uNQ4ber8SANkhmfntJIZM2Q1uWZKl9vl7beAbteDvjSc_wO5q5UeQCivS4lvI4yDaLxnZGbdK9DGhfedf6DIEC-3_KZHEjHv0cv17Xw3Wc7M5aamIYsKdrtByfoC2fNGZ3JsfYQ4wRj4MNvLkSXOUaEmU9nzsFj-2p__Qd9gzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31b02ba16c.mp4?token=C-5ub7S58N_jBfZCDQxjjpK_ctqnmqydgkR5Qmn_S2S1bi_wVfEeUrt1lz6hJxggpZcktvo9WNnRnpc27Vb9T3MWhfpsyW6po8_TpLRLFRp97fmbTvD5y8fx1HReVRV5UerEQo_Y7HEbvkEfs0FLHb_7cybgrhcVxYx_ZWQthy44uNQ4ber8SANkhmfntJIZM2Q1uWZKl9vl7beAbteDvjSc_wO5q5UeQCivS4lvI4yDaLxnZGbdK9DGhfedf6DIEC-3_KZHEjHv0cv17Xw3Wc7M5aamIYsKdrtByfoC2fNGZ3JsfYQ4wRj4MNvLkSXOUaEmU9nzsFj-2p__Qd9gzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متن توافق با ایران را به نخست‌وزیر کانادا نشان داده است
مارک کارنی، نخست وزیر کانادا، به خبرنگار CNN:
🔹
او یکی از معدود افرادی است که یادداشت تفاهم بین ایالات متحده و ایران را دیده است.
🔹
این متن می‌تواند ساختار خوبی ایجاد کند و تغییر دهنده بازی باشد؛ توافق جدید ساختاری است که کشورهای منطقه از آن حمایت می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/660347" target="_blank">📅 12:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660346">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fba406a50a.mp4?token=LGOc-2G6juopdyAmfIxtYFyX0115MGn7LlXba9aKgyfguxRS6MBhLeOoyNRiyLglc4PQnzKxS_Q5xq6ZbhQ-JB7pMEhRKtrQ5qxKkWSkhH8JP45RWS-nQyLAXPoEE8f0I9Cd4ZnMEzxqkaD9MOdQCWiwoiogT99TnCmhBgIk95jSxBcpwdKZuqdtagu7hvolgBgKCnoOMkyO-D9Dk-PHGdolSx06A2CVFp3QGo4E-V81-tK3th5EUKQuxwy1hUKSVSnobL3tZs_wwk-C2MCRf_0nrGmLlZmF3y0nGm5TCfTybrpgVRXTGRHbsM4dtY_HOc7r8z85UXutKzSCsBYOMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fba406a50a.mp4?token=LGOc-2G6juopdyAmfIxtYFyX0115MGn7LlXba9aKgyfguxRS6MBhLeOoyNRiyLglc4PQnzKxS_Q5xq6ZbhQ-JB7pMEhRKtrQ5qxKkWSkhH8JP45RWS-nQyLAXPoEE8f0I9Cd4ZnMEzxqkaD9MOdQCWiwoiogT99TnCmhBgIk95jSxBcpwdKZuqdtagu7hvolgBgKCnoOMkyO-D9Dk-PHGdolSx06A2CVFp3QGo4E-V81-tK3th5EUKQuxwy1hUKSVSnobL3tZs_wwk-C2MCRf_0nrGmLlZmF3y0nGm5TCfTybrpgVRXTGRHbsM4dtY_HOc7r8z85UXutKzSCsBYOMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیدحسن خمینی: ۳۹ روز گذشته جهاد اصغر بود؛ از امروز جهاد اکبر شروع می‌شود؛ باید از نزاع‌های بی‌حاصل دست بکشیم
🔹
واقعا باید از نزاع‌های بی‌حاصل که نتیجۀ منیت‌هاست دست بکشیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/660346" target="_blank">📅 12:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660345">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUAxzlkrEITZ8zFxwFjFWwwl6bU0b4O9pdj0_bw4cp4oTBY8dp1GOkMFX-YYYatMrintd7xF16dsSfSt1T8uA3fc9Xw_OAzBbvPvxpo9LMI9ZD9_beCH6Iinn1PatQbeophGwmj0E3gBgn0ObnNXfBSJPdzI5Xo-iaipjWTGTR9dT4-LQDv6MXdWBCZJhKl2juMEfGMRU_ACgpjoFV6I1EMKRkcCRA86yVAf3RGr9LyWEHLstZwZYuKPd0roN-bkbLZEUbHW6fCXdsuiVmZFHc9E6CnUNzK9xaHpxpE9vBvCbPgCY1oQronLLMJdQwLovoQ1Tv8XU0E3kdigA4KMew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست اینستاگرامی مهدی قایدی پس از اولین بازی در جام جهانی
🔹
لحظه‌ای که سال‌ها رویای آن را داشتم، سرانجام به واقعیت پیوست.افتخار می‌کنم که نماینده کشورم هستم و در کنار هم‌تیمی‌هایم می‌جنگم. قدردان تمام کسانی هستم که در این مسیر من را حمایت کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/660345" target="_blank">📅 12:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660344">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6NRWFXw0oyraTohEnRXtFjG1uJ_x_wkNXn2VwADT05v0yLNwugxpUxs6sc44SpFVHifKuxInlLS6TbPpDyaz9vYf7n_RWqufbCayy3oFyL02kAKeiIJ7Nahdc8_Z7DL11ILUdRt3D5_AQM4C0y5RlnkFCeL-N07iZctWh5KJRLry7oSKUXSpX77uu-gs_He6OxTwbdG-rgwShlHbtUkUbNzJrwYnJlrYm9_Is-fRcZHIPgs_bAw1dcbVI5iGrRmvEgM1HpOuqXoS7nScyJziJzXgSlB2AW0vRVbcSqA11-9evD5HFmi3P5_IqnPvho77UNeqZ4jhQs08XW4iLjfRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فیشینگ چیست و چگونه اطلاعات بانکی شما را به سرقت می‌برد؟ #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/660344" target="_blank">📅 12:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660343">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
اتفاق قابل احترام و عزتمندانه در تلویزیون عراق: پخش سرود ملی ایران و ادای احترام نظامی‌به کشورمان توسط کارشناسان ورزشی عراق!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/660343" target="_blank">📅 12:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660342">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6655fd79.mp4?token=ah8jQHuupSNUTe5LdstzPv0VlH4SjqyAWQIkF0dHBWY-Q6hB8Zr1Pvw3TjFsUyEXF0NRQhk6UbdYe_zwpb07B5dHQwtEBRDm2-XJXq6tohGAlBkcxFTr2sVRuVo3Z0NeIPhDc37OyGmvnEuGx3mw7MQZskBpVZpP12mkB7y9FqpPUOP4VEAbo4NVLG4GJg793-ubMREOmUQfVBCYtnPJgz8XJGV2a3voOBCMufNLEkXQ9gvZcTOzN-CGzdjYxkq0fJ59aerUpmwxuzw0Jut6iwE5wmyruoOHzjkS81ZcAWrPg5-WE6UvmcEVsGf1I-ZhG8F2O0T8aGaFqTKsUA2J3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6655fd79.mp4?token=ah8jQHuupSNUTe5LdstzPv0VlH4SjqyAWQIkF0dHBWY-Q6hB8Zr1Pvw3TjFsUyEXF0NRQhk6UbdYe_zwpb07B5dHQwtEBRDm2-XJXq6tohGAlBkcxFTr2sVRuVo3Z0NeIPhDc37OyGmvnEuGx3mw7MQZskBpVZpP12mkB7y9FqpPUOP4VEAbo4NVLG4GJg793-ubMREOmUQfVBCYtnPJgz8XJGV2a3voOBCMufNLEkXQ9gvZcTOzN-CGzdjYxkq0fJ59aerUpmwxuzw0Jut6iwE5wmyruoOHzjkS81ZcAWrPg5-WE6UvmcEVsGf1I-ZhG8F2O0T8aGaFqTKsUA2J3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شروع طوفانی فینالیست های دوره قبلی جام جهانی/خلاصه بازی جذاب فرانسه سنگال و آرژانتین الجزایر
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/660342" target="_blank">📅 11:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660341">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcfQKVb2zfWUQigvxHhbfIJpREvvubPEWDx1fmTKUOxH1KJjEuCQGoZf0nY8w8xjSiPD5gIBJsXVrgfmGPhLS9TRRdLeW_svngfC--R3P-Hr97rtZKHhmD8iIyinaR8wUB1co1w-hwwWXDmMr6V1amf_3sP6RUqFFUyXnNYaOppSn7kvJQVq4jiEabJRy1EmKXb6JDS6sEQYzMqWnUUqM3e-RukQ_4t7b4n085WoKnBX3_IndqNO2rV_pnsgusfuxug7hLwmPRn1AQQft1CSNmUFGISK9NmfOxVNUfU3Hoz7odEyziDec3iC_Z-STqvK0E2rXMJJzQ8WV2hu5y6_Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در بریتانیا به‌زودی استفاده از ۱۰ شبکه اجتماعی معروف برای نوجوانان زیر ۱۶ سال ممنوع خواهد شد: تیک‌تاک، یوتیوب، اسنپ‌چت، اینستاگرام، ایکس، ردیت، فیسبوک، توئیچ، کیک و تردز.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/660341" target="_blank">📅 11:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660340">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
قیمت نفت برنت به ۷۸ دلار سقوط کرد
🔹
قیمت نفت برنت با کاهش ۰.۷۲ درصدی در معاملات روز سه شنبه به ۷۸.۴۲ دلار سقوط کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/660340" target="_blank">📅 11:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660339">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006b6f0f1e.mp4?token=C2f_O-qrASsDQYlsSq1buPu-ZuXAp0xzHh91xdnsC63MO2aULT7F5Ot014Mnl9MWRiPhp4_HHdeI7dHBzTukqSYns18wYrwYdK_Nc5G3oyB0dzM6FdaJPxg-JPeyUCc5IyN8TwSnH4iO1PKUmu_Mp2twuycmrzq8wJanXIa1MFooPXMp9O7lBHKJ03olEA67ldGTdnpeN4n5kXE0gPiEH16scMPfuC2uGFj3vdvebXWTk-NaJtoHCYBvA5Oeozw44AqoR_KU_zsPyPJlAsWOr0KrHlxk1hyTk1AzVUSiZ0UDVy2jLwE9WIdY-ZpBJ87K_Kj7lvB4Ayrpiq9fTyIiBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006b6f0f1e.mp4?token=C2f_O-qrASsDQYlsSq1buPu-ZuXAp0xzHh91xdnsC63MO2aULT7F5Ot014Mnl9MWRiPhp4_HHdeI7dHBzTukqSYns18wYrwYdK_Nc5G3oyB0dzM6FdaJPxg-JPeyUCc5IyN8TwSnH4iO1PKUmu_Mp2twuycmrzq8wJanXIa1MFooPXMp9O7lBHKJ03olEA67ldGTdnpeN4n5kXE0gPiEH16scMPfuC2uGFj3vdvebXWTk-NaJtoHCYBvA5Oeozw44AqoR_KU_zsPyPJlAsWOr0KrHlxk1hyTk1AzVUSiZ0UDVy2jLwE9WIdY-ZpBJ87K_Kj7lvB4Ayrpiq9fTyIiBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرقت از یک بانک با بیل مکانیکی در انگلیس
🔹
سارقان با یک لیفتراک تلسکوپی شبانه به شعبه بانک در کمبریج‌ شایر رفتند و دستگاه خودپرداز را از دیوار کندند. پلیس اعلام کرد لیفتراک هم سرقتی بوده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/660339" target="_blank">📅 11:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660338">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
دادستان تهران: کیفرخواست برای اعضای یک شبکه زمین‌خواری در سعادت‌آباد که ۲۲۵ هکتار از اراضی دولتی را با جعل اسناد تصرف کرده بودند صادر شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/660338" target="_blank">📅 11:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660337">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 مسابقات جام‌جهانی ۲۰۲۶ را از چه طریقی تماشا می‌کنید؟</h4>
<ul>
<li>✓ شبکه سه صداوسیما</li>
<li>✓ پلتفرم‌های نمایش خانگی</li>
<li>✓ شبکه‌های ماهواره‌ای</li>
</ul>
</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/660337" target="_blank">📅 11:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660336">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bea36a8b92.mp4?token=gT6BcyOteFy3Eg2WBPmwB9RuSjrnQLMobakfdX749SF2ZPz4JiZrhaoh-5fvFmEomsLtI5ofo4BrlyEeJm7Ybp1ZbiBnjclu80WEdrFvS0ktBWkNX3QemUGGMNZI86HEPpNWCEMvFbfWnfTD_QZLiSwelUnBwY3i5BzNIVT25j3rh3_X_tUV2K9ZQavprjTKhiB2PW51uqDMugoF_zpXGWYA3HzqUaayDWezMJqyt_SmgPqzfFf9W5vY_Y59RZzdcAkL3MvPpi6OZ0aOGdGp44LtFDSC23i0_aM_TkrC-j_rl6Ygf-lAmGwKNOmThPmhhWyIJ5GZBlFaQ5Vvg_Uy9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bea36a8b92.mp4?token=gT6BcyOteFy3Eg2WBPmwB9RuSjrnQLMobakfdX749SF2ZPz4JiZrhaoh-5fvFmEomsLtI5ofo4BrlyEeJm7Ybp1ZbiBnjclu80WEdrFvS0ktBWkNX3QemUGGMNZI86HEPpNWCEMvFbfWnfTD_QZLiSwelUnBwY3i5BzNIVT25j3rh3_X_tUV2K9ZQavprjTKhiB2PW51uqDMugoF_zpXGWYA3HzqUaayDWezMJqyt_SmgPqzfFf9W5vY_Y59RZzdcAkL3MvPpi6OZ0aOGdGp44LtFDSC23i0_aM_TkrC-j_rl6Ygf-lAmGwKNOmThPmhhWyIJ5GZBlFaQ5Vvg_Uy9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرکرده اوباش در قیطریه، با شلیک پلیس زمین گیر شد
🔹
سرکرده یک باند زورگیری و اوباش که با حمله مسلحانه به یک واحد مسکونی در محله قیطریه موجب ایجاد رعب و وحشت میان شهروندان شده بود، در عملیات ویژه پلیس تهران بزرگ و پس از حمله به مأموران، با شلیک پلیس زمین‌گیر و دستگیر شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/660336" target="_blank">📅 11:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660335">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/263955c247.mp4?token=JVbZD5Gdm1qB6PC9tgyPGmcOd_3JSPsXN_sLFjHRvq4-6VkNVou1jPN4qqIE5VUsb_Ji7tE4pWPAk4FcNcN9V4ps1JwT5x-zMVzmGg6mpWFvGNUQ19Ha7CEmsigRGcj_GPC4naGjD3ERLGZWzVuChJW4S0uqcrlKqYvVFlrzD2Pi1W1YU5HPTEqiYKKX9FoT1Tlj-xjVOObd_HNPnrjQH3m99aHmSqAy9YezYgn_hypz1mgDX19wSIDziJuIjd6Mg8yx6YO5ISa4JCmm0kiAhuDOYNEqYbE8NXqZUwnMa4gUUnkNZunvJqbNCkUIpWsTp0o3TmNEsfm4FHRTjBWH2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/263955c247.mp4?token=JVbZD5Gdm1qB6PC9tgyPGmcOd_3JSPsXN_sLFjHRvq4-6VkNVou1jPN4qqIE5VUsb_Ji7tE4pWPAk4FcNcN9V4ps1JwT5x-zMVzmGg6mpWFvGNUQ19Ha7CEmsigRGcj_GPC4naGjD3ERLGZWzVuChJW4S0uqcrlKqYvVFlrzD2Pi1W1YU5HPTEqiYKKX9FoT1Tlj-xjVOObd_HNPnrjQH3m99aHmSqAy9YezYgn_hypz1mgDX19wSIDziJuIjd6Mg8yx6YO5ISa4JCmm0kiAhuDOYNEqYbE8NXqZUwnMa4gUUnkNZunvJqbNCkUIpWsTp0o3TmNEsfm4FHRTjBWH2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هوادار متفاوت آرژانتین در کانزاس
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/660335" target="_blank">📅 11:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660334">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
افشای استفاده از هوش مصنوعی گراک در حملات متجاوزانه آمریکا علیه ایران
خبرگزاری فرانسه:
🔹
گزارش حقوقی دولت آمریکا نشان می‌دهد ارتش این کشور از ابزار هوش مصنوعی گراک متعلق به شرکت اسپیس ایکس تحت مالکیت ایلان ماسک در جنگ غیرقانونی علیه ایران استفاده کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/660334" target="_blank">📅 11:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660333">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
شرایط جدید بازنشستگی تأمین اجتماعی
🔹
سن بازنشستگی مردان به ۶۲ سال و سابقه لازم به ۳۵ سال افزایش یافت.
🔹
زنان با ۵۵ سال سن و حداقل ۲۰ سال سابقه می‌توانند بازنشسته شوند.
🔹
مشاغل سخت و زیان‌آور، رانندگان و زنان دارای ۳ فرزند یا بیشتر، امکان بازنشستگی زودتر دارند.
🔹
تغییرات به‌صورت پلکانی بر اساس میزان سابقه (کمتر از ۱۵، بین ۱۵ تا ۲۸ و بیش از ۲۸ سال) اعمال می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/660333" target="_blank">📅 11:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660331">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
۳٠
شهروند ایرانی از پاکستان به کشور بازگشتند
🔹
طبق اعلام وزیر خارجه پاکستان محمد اسحاق‌دار، با کمک این کشور ۳۰ تبعه ایرانی به شامل خدمه یک کشتی توقیف شده توسط آمریکا به ایران برگشتند./تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/660331" target="_blank">📅 11:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660330">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0632de855e.mp4?token=Lkqq_-MnRF8dqihTD2iXELcn356xFXLiUBq9eBg5oNF6CwqFw_-kZ70qiKk4Pd-trYDaXwcgilkStCgg-Pd2WSXapy-p9HDEI7ImQNijAVL0QAbbu2NM-G54y01IYKmIFieEi4VJTIbNGAsn1L7Inbpc3yZoJBEGt_ZCek-IEB_78kzMTf6fVhHVSG0PPrw7mi2xWsc5tyWQ32Jm1M-AqfBpz7WR_2Db9Sov6ZF4jFbMcgjgNtkvvapIRamVGeKCXslkeqvAdLwHbUfYoUrd39kYlX_343UI2BFliLVz6C7X1TTZN2dhCA50WMw-SekUVp-YbMyUAspWwrtMF9rlNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0632de855e.mp4?token=Lkqq_-MnRF8dqihTD2iXELcn356xFXLiUBq9eBg5oNF6CwqFw_-kZ70qiKk4Pd-trYDaXwcgilkStCgg-Pd2WSXapy-p9HDEI7ImQNijAVL0QAbbu2NM-G54y01IYKmIFieEi4VJTIbNGAsn1L7Inbpc3yZoJBEGt_ZCek-IEB_78kzMTf6fVhHVSG0PPrw7mi2xWsc5tyWQ32Jm1M-AqfBpz7WR_2Db9Sov6ZF4jFbMcgjgNtkvvapIRamVGeKCXslkeqvAdLwHbUfYoUrd39kYlX_343UI2BFliLVz6C7X1TTZN2dhCA50WMw-SekUVp-YbMyUAspWwrtMF9rlNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت فرهنگی عراقی‌ها پس از بازی با نروژ؛ متشکریم بوستون!
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/660330" target="_blank">📅 10:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660329">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ممکن است اسرائیل ناچار شود به «خط زرد» در جنوب لبنان عقب‌نشینی کند
هاآرتص:
🔹
به ارتش اسرائیل دستور داده شده که از
حملات گسترده در لبنان
خودداری و بر حفاظت از نیرو‌های خود تمرکز کند.
🔹
ممکن است ارتش ناچار شود به
«خط زرد» در جنوب لبنان
عقب‌نشینی کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/660329" target="_blank">📅 10:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660328">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a63a7346fc.mp4?token=CQQVTc02iL1KO5VpPlg8vYAycHWbxyUpChkjPsAa-R3kVnSPKu41GdxoW7a0d8xAVAjjKivdJkjGTFLFwswQDtbT5n-rpQRv9MRlWpPKR5-7HZ2vbiU94uKFktqqrxwtqW-3lvclZnNvFHXQL5rItQPUuKe1jK4IqmbGrzsfSRrowpwyxqPXqcEZeO6SbG3spx8vlTCYvHhPUvd9dlLdSKaZnKcgL0ZvUKnk2T5NynvQ_WDqC4wdcpzIN6tGSeoUvhvQYLVfXmYn0gF9QOi6p0aZt1cU36spdfY8Cu9zUFRMOPdm_ayEoXEFjAWRZiobdUlzgX1_V4_eV8wtDA5cxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a63a7346fc.mp4?token=CQQVTc02iL1KO5VpPlg8vYAycHWbxyUpChkjPsAa-R3kVnSPKu41GdxoW7a0d8xAVAjjKivdJkjGTFLFwswQDtbT5n-rpQRv9MRlWpPKR5-7HZ2vbiU94uKFktqqrxwtqW-3lvclZnNvFHXQL5rItQPUuKe1jK4IqmbGrzsfSRrowpwyxqPXqcEZeO6SbG3spx8vlTCYvHhPUvd9dlLdSKaZnKcgL0ZvUKnk2T5NynvQ_WDqC4wdcpzIN6tGSeoUvhvQYLVfXmYn0gF9QOi6p0aZt1cU36spdfY8Cu9zUFRMOPdm_ayEoXEFjAWRZiobdUlzgX1_V4_eV8wtDA5cxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونالدو رو هم توی آمریکا اینجوری گشتند
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/660328" target="_blank">📅 10:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660327">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mpf85ITJjYPuOCXSXb02kbU18BdA2bac6fV51UHpgHvbEYydw2fGHMh7yA4kwHA--CvNbVEa1tKLF-5Uh5fenm9mAUzDQaMoyDH2HICSDo6Tl5gJJPiXim7esbAfbhDR7RjjNG7GErsM40XRXbJjqtZsnnjw-QJBfdyPyfiYEIzh1g1s9xLvd9GNyCDwGMWywQOCL4EXGLTrkNJO-SInO7TUjgBJkDQ2A16wHohs9wJAzH_4PbRTtdVu8Spto9xw0jZFCK31eLPSREmgThoQFpgacf-nl2tdHGFFtM-v2rSJcBUsM0ZmfDzgx6pcTWxCzo2lWK-lwevWYxskC1FPRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قابی زیبا از معماری بی نظیر شهر هورمان تخت کردستان
#اخبار_کردستان
در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/660327" target="_blank">📅 10:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660326">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c298afccd2.mp4?token=GVQvEASbN5JyMLBPR00H9dH3eAhqCIAGF7Dhq7KPLSO58f1CHTAnO3gBnB2aez59bmaI3WGBsIPMeTFeBkvW1eVRSDeMUXT8aYz_jEdw8mwC3vFuZ_laR8VqO5LO22P954dcvelIgr2_jwOPvQNEnoIJTghoXtGbCXR1gQ47LK-GDYcd_rW9lalD6XXYJMK4HqPl2nZ69OIiX2kWAuEd_6rmRkuCMdQZXHaQVSoRJFutB2C1nUBPWl7Q6p7WPG0hM881gBZqPanskal603pVrj14YHQAJrI8-E7j1koDuwRUmR0PMZ4hOHeJFommy9c91kN3AIVE1P82DSk9kgDQpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c298afccd2.mp4?token=GVQvEASbN5JyMLBPR00H9dH3eAhqCIAGF7Dhq7KPLSO58f1CHTAnO3gBnB2aez59bmaI3WGBsIPMeTFeBkvW1eVRSDeMUXT8aYz_jEdw8mwC3vFuZ_laR8VqO5LO22P954dcvelIgr2_jwOPvQNEnoIJTghoXtGbCXR1gQ47LK-GDYcd_rW9lalD6XXYJMK4HqPl2nZ69OIiX2kWAuEd_6rmRkuCMdQZXHaQVSoRJFutB2C1nUBPWl7Q6p7WPG0hM881gBZqPanskal603pVrj14YHQAJrI8-E7j1koDuwRUmR0PMZ4hOHeJFommy9c91kN3AIVE1P82DSk9kgDQpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینم آسون‌ترین روش پخت لازانیا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/660326" target="_blank">📅 10:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660325">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2425fb3e1b.mp4?token=kEUJECRkETI9PajLHcUsTtuRiF1p2WgYyekX362xKtVLBZph8KttL83MUFP8O7qpfjD-bzuRABHMIfzxz2iJmEGfa3Vg6SYRzfaLMcTonQGWM5S6ax3KtCjnt7McPChys1NhczWvfo-6MmZB0weROAUnTrB_4r3oTLA9dRFm909U5ivlQzeO8RkVww7KH4M-jkP-588uTDKNg5kIBZ-6AQVySV1jJL3zt58-2n7LLwyUO5o-LhfLtiV1qzUq1dsTuI8ytU-ZOJIKneJag-m80Vz1_LViU7TCU4kyUe4vh1gtPxqcz_TYdRt8biX4MtAObgLD1bx8zQzbfCvyAE5sgpFv2_HN_GmEKScqCMKmUAwq-fG6lhqaZqXBVMvmvxmtfjsKmNdMWGbT3vLMRQPjKiCdHrIAPhJ1OkYXdxJZPJBkOj0d2naL4xky7nKGGrzop5uAhxQNOQUEN6Bku2rJM2ssUU00BMyesiqU3EO572YI9HTV5zT_WkVAqapkldATihuuMjFCM_C2pMmzIPUzM8nSFuRQ9idpDD7RUjmcq59l9MGwLcB4mcZFpshA_4bVT_suLKp874XKx6lkW_vky4sPJxWyW1P5-pBiMFf2SG-pBjWPYp4b_nHmJsmLV_ZAEMELNeB_pTzcoWC-tR4y_hhYCfLtcK6_6CNT3i09g9E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2425fb3e1b.mp4?token=kEUJECRkETI9PajLHcUsTtuRiF1p2WgYyekX362xKtVLBZph8KttL83MUFP8O7qpfjD-bzuRABHMIfzxz2iJmEGfa3Vg6SYRzfaLMcTonQGWM5S6ax3KtCjnt7McPChys1NhczWvfo-6MmZB0weROAUnTrB_4r3oTLA9dRFm909U5ivlQzeO8RkVww7KH4M-jkP-588uTDKNg5kIBZ-6AQVySV1jJL3zt58-2n7LLwyUO5o-LhfLtiV1qzUq1dsTuI8ytU-ZOJIKneJag-m80Vz1_LViU7TCU4kyUe4vh1gtPxqcz_TYdRt8biX4MtAObgLD1bx8zQzbfCvyAE5sgpFv2_HN_GmEKScqCMKmUAwq-fG6lhqaZqXBVMvmvxmtfjsKmNdMWGbT3vLMRQPjKiCdHrIAPhJ1OkYXdxJZPJBkOj0d2naL4xky7nKGGrzop5uAhxQNOQUEN6Bku2rJM2ssUU00BMyesiqU3EO572YI9HTV5zT_WkVAqapkldATihuuMjFCM_C2pMmzIPUzM8nSFuRQ9idpDD7RUjmcq59l9MGwLcB4mcZFpshA_4bVT_suLKp874XKx6lkW_vky4sPJxWyW1P5-pBiMFf2SG-pBjWPYp4b_nHmJsmLV_ZAEMELNeB_pTzcoWC-tR4y_hhYCfLtcK6_6CNT3i09g9E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض حریدی‌ها در سرزمین‌های اشغالی به خدمت نظامی اجباری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/660325" target="_blank">📅 10:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660323">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
استرالیا: ما سطح هشدار عمومی سفر به منطقه خلیج فارس و خاورمیانه را کاهش داده‌ایم.
🔹
هاآرتص: ارتش اسرائیل ۵۲ درصد از ساختمان‌های اردوگاه پناهندگان جنین را تخریب کرده است.
🔹
احتمال شنیده شدن صدای انفجار در تبریز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/660323" target="_blank">📅 10:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660322">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1IsgHPkNDXYK9N_RK26E0vc-dCeWRbclmgJCkUjp6faOUfZyrj1usFjUDICfYvPxcpwyl7_vV01mbVjgPU6ewZ95wfVKaEtcCVpstin7eTCJkmTMWdjQiWk9Zrq4hjFpeFCl5RHIZEXi8YVUimvo2QkErx_KY9wddHgS84HolTcsrv_mirrjsXjvzRC3X88Cm0ZTI7pqfy_VHi33-GDVoKcB2ZJrFiEEXeXFKVzJt16hi2T7VIpnMWX3Y2VH-pH6jlBVwhTgkkUzrwkTgB5a5S9YWQQO1li45PT_IiFlZ3TIyHT_XqfFoc82V1CoCkyHN5qgg-8TJsNzGeKl-zXmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول گروه J در پایان رقابت‌های دور اول
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/660322" target="_blank">📅 10:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660321">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
آیا خرید و فروش پول نقد ایران در مناطق مرزی و انتقال به افغانستان صحت دار‌د؟
نماینده سیستان:
🔹
گزارش‌هایی از خرید و فروش پول نقد ایران در مرز و انتقال به افغانستان وجود دارد، اما هنوز تأیید رسمی و قطعی درباره ابعاد آن ارائه نشده است.
🔹
به‌دلیل محدودیت بانکی و تفاوت نرخ ارز در مناطق مرزی، گاهی معاملات نقدی غیررسمی شکل می‌گیرد و نظارت آن بر عهده بانک مرکزی، مرزبانی و نهادهای امنیتی است./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/660321" target="_blank">📅 10:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660320">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6971a5404f.mp4?token=rRhu46H7yOKMnej-9ZPLttvK4xQGY8abOJ67Rjg3DZGuj6A2L4glNI1NmiXquewGUmz0NE6J_M1D2Aj1IcmW_v4jFJ9939XAnO17aXoix7PgLDeKXdOH1zIPJzwYv2ku5FatbZ2xavWeZy7UgX2vgO8TQB_wqTtAMbOlfWVdHVwlrvXrFYzxn7l2vuoakC_0ZMCnOTZaTgaROoNFuL5VO-RWLG_B7bISgOXtwH_eR2z5myl4mP1Bzkq5h_IVAoufg8BZzfpsQT9zxkNFEBuoOXS2Tx_xnJwFB43EqZ_EBeB8T_PxvVt-w6WfzBigpzCABY4iyIolHRgRe_mZTFhVXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6971a5404f.mp4?token=rRhu46H7yOKMnej-9ZPLttvK4xQGY8abOJ67Rjg3DZGuj6A2L4glNI1NmiXquewGUmz0NE6J_M1D2Aj1IcmW_v4jFJ9939XAnO17aXoix7PgLDeKXdOH1zIPJzwYv2ku5FatbZ2xavWeZy7UgX2vgO8TQB_wqTtAMbOlfWVdHVwlrvXrFYzxn7l2vuoakC_0ZMCnOTZaTgaROoNFuL5VO-RWLG_B7bISgOXtwH_eR2z5myl4mP1Bzkq5h_IVAoufg8BZzfpsQT9zxkNFEBuoOXS2Tx_xnJwFB43EqZ_EBeB8T_PxvVt-w6WfzBigpzCABY4iyIolHRgRe_mZTFhVXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تفاوت استرس و اضطراب به زبان ساده #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/660320" target="_blank">📅 10:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660319">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9797c47bc3.mp4?token=HMFXqVzwkn0WGoeAkE9K3Xk3TwRuR1tfWgEplzW2iJuOLYWPLavspjffrwUFjtEI8ZL3ietXgYWHxaaBIxU08rb_222AxAbCTClIoaME8l7Z9r7nm6YlWZcJXVAxNrA76xDVa5__8VuMejUerja4MEt4oNT-9JA8oK4a7HSQsRW-H1WNSvSRmKYwRBxsOXyQX8-E16KAG4ML3fq_eg1qiT-AB-hXLBLKlj_2h0ZDsD9TM9fNDpRpQRHo8ZJObMbSLCFppGEykn3O6zngnivbhPyrMq7JzQq7x0wt-ykgbACPm6H6fbFGO-KrPv-prrO54lCVS2CVZsq2ycdqoqz0cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9797c47bc3.mp4?token=HMFXqVzwkn0WGoeAkE9K3Xk3TwRuR1tfWgEplzW2iJuOLYWPLavspjffrwUFjtEI8ZL3ietXgYWHxaaBIxU08rb_222AxAbCTClIoaME8l7Z9r7nm6YlWZcJXVAxNrA76xDVa5__8VuMejUerja4MEt4oNT-9JA8oK4a7HSQsRW-H1WNSvSRmKYwRBxsOXyQX8-E16KAG4ML3fq_eg1qiT-AB-hXLBLKlj_2h0ZDsD9TM9fNDpRpQRHo8ZJObMbSLCFppGEykn3O6zngnivbhPyrMq7JzQq7x0wt-ykgbACPm6H6fbFGO-KrPv-prrO54lCVS2CVZsq2ycdqoqz0cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لیونل مسی با ۱۶ گل همراه با میرسلاو کلوزه برترین گلزن تاریخ جام جهانی شد
🔹
او برای اولین بار در جام جهانی هت‌تریک کرد.
🔹
بازی آرزانتین و الجزیره با نتیجه سه بر صفر به سود آرژانتین پایان یافت.  #جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/660319" target="_blank">📅 09:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660318">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
رئیس سازمان فضایی ایران: پرتاب‌های منظومه «شهید سلیمانی» تا پایان ۱۴۰۵ شروع می‌شود. صنعت فضایی ایران طبق گفته مسئولان فعال است، آسیب جدی ندیده و خدمات ماهواره‌ای بدون وقفه ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/660318" target="_blank">📅 09:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660317">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a91c6e03.mp4?token=Q2sJZsZE5BSAL2TFZqhFTgBmeeoHopAiiq8Fbft01Doib045lE47WpnoPe6wHqwRyIMLUKuWveAp2h1uSx6cxHvloj33nVujk5wfkzmymqfO40nnGBve9cZsIJlqKMbBwhENE_uh1m6I4pxidxCOv2f73dyUB7BpiAuhii-HaqcC64dDcf2tu_xQe-B8qK-2BM2VZ_s06UYvN61-Hz6P1P1WUCuWAKCGZ43kOOZFwqm07AvkUsYivZpB_QTYy6bR4uKzsnHAqI_h5YJvRuUSZ2cSujxxKfxfKFtVqYzbeo_Df9Q0THKLSIClG9pg-Fzk2mRvkoMOSfJ-m8Ppg9igHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a91c6e03.mp4?token=Q2sJZsZE5BSAL2TFZqhFTgBmeeoHopAiiq8Fbft01Doib045lE47WpnoPe6wHqwRyIMLUKuWveAp2h1uSx6cxHvloj33nVujk5wfkzmymqfO40nnGBve9cZsIJlqKMbBwhENE_uh1m6I4pxidxCOv2f73dyUB7BpiAuhii-HaqcC64dDcf2tu_xQe-B8qK-2BM2VZ_s06UYvN61-Hz6P1P1WUCuWAKCGZ43kOOZFwqm07AvkUsYivZpB_QTYy6bR4uKzsnHAqI_h5YJvRuUSZ2cSujxxKfxfKFtVqYzbeo_Df9Q0THKLSIClG9pg-Fzk2mRvkoMOSfJ-m8Ppg9igHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس: ایرانی‌ها در موقعیتی هستند که می‌گویند می‌خواهند تعهدات بلندمدتی به ایالات متحده و کشورهای عرب خلیج فارس بدهند تا رابطه‌شان را تغییر دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/660317" target="_blank">📅 09:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660316">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
جی‌دی ونس درباره ایران: دلیل اینکه متن تفاهم‌نامه را منتشر نکرده‌ایم این است که برخی از میانجی‌های ما؛ پاکستانی‌ها و قطری‌ها؛ از ما خواسته‌اند که این موضوع را به ترتیب درست انجام دهیم
🔹
حساسیت‌هایی در جهان عرب و مسلمان وجود دارد که ما در تلاشیم به آن‌ها…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/660316" target="_blank">📅 09:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660315">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3530ff42fa.mp4?token=FprsvCoHRqosZKTByrsQ4lQmEr1_JtE-PRe7fofrcFPdTLNtz9XODcHo5haJLeijmxxtzaMwh9UM0kezwANsHoW2J5oDksaUx5yrW2a1stVmPHhx0aryLPgPU9pz0GkSgjlPO6YwtgEfRyXqagU6CDLvypTLqHEOIMyJgEl8OZi3-YFzGdlIasUD8jdvjMZmfwuazXH_N29cCtdpA23MgY9Nls0rFzPKXscy6EHSOcoIKqaDR1rXV8XkJxtPwFZHc_ikEPqq8nCOaNoD4s995dtuE-KtziaAbWCU2QrGqtrqyszZl-c4HoBvglaXFOMfWzBNhxAlgQEtrQFisGQca4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3530ff42fa.mp4?token=FprsvCoHRqosZKTByrsQ4lQmEr1_JtE-PRe7fofrcFPdTLNtz9XODcHo5haJLeijmxxtzaMwh9UM0kezwANsHoW2J5oDksaUx5yrW2a1stVmPHhx0aryLPgPU9pz0GkSgjlPO6YwtgEfRyXqagU6CDLvypTLqHEOIMyJgEl8OZi3-YFzGdlIasUD8jdvjMZmfwuazXH_N29cCtdpA23MgY9Nls0rFzPKXscy6EHSOcoIKqaDR1rXV8XkJxtPwFZHc_ikEPqq8nCOaNoD4s995dtuE-KtziaAbWCU2QrGqtrqyszZl-c4HoBvglaXFOMfWzBNhxAlgQEtrQFisGQca4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس درباره ایران: دلیل اینکه متن تفاهم‌نامه را منتشر نکرده‌ایم این است که برخی از میانجی‌های ما؛ پاکستانی‌ها و قطری‌ها؛ از ما خواسته‌اند که این موضوع را به ترتیب درست انجام دهیم
🔹
حساسیت‌هایی در جهان عرب و مسلمان وجود دارد که ما در تلاشیم به آن‌ها پاسخ دهیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/660315" target="_blank">📅 09:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660314">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvqIWoyAdAatxwH-AzsXueHDI08ivkts1TSQLx5l2U-Hnxm7ZPMhzdqDc7KQof2lhke5J_T6gzdkwxYTfmDn8KKREtYZPjzM744l6vPB00wDii6u4AvOS5e8OB4aQcrjhnMHELS3LydqKpdP6FgluALo_ODcxxRiXfpORxf1sVv5XXmNmatJUeOrId1CUsRTJ4Xu5z8KHD3pueVlxOQF6c9EB7JXTeTh-osNKOUYvARREoPV6Pj3jU_DouUmhPZkB1gR_kzkbm3dTEd5nZelJF-XVK6sBfobjW2pErwGxG3uELSZ5kwz4xQSPjkcq5MQY0OziSLnLITyP3Gj3d1Sew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۳ گل و ۳ امتیاز شیرین برای اتریش
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/660314" target="_blank">📅 09:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660313">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47fbbdcf45.mp4?token=JqvEtQVAV9Yx2ITRf7F42DyJTY1IYYWVEVeNXCFmvwcTo2dSzoXvH-MqXXqhhfU9uvEc_Gzyj20YTEQZdHtf0QbUCq26rw6fjmQ-qqsSAehp-KoIRVvOpEbDVqyPlq2yS8BWmFez3MiIvBLRQjMwnMxTF_mWLXWLd7CSL6EqpkxUBzAppXpNWywt_YpbRgpKfyrRfs3m0dhOuk8w6jceIuReQT-QX6_r1MIaakEd9_WNs6Wq8-cMPJF4bBir9N83-4VZ5B4cmUZN9YNvyY60OklxrSjd_sx65Mzx-r0sMTd_RKyMLj8tz77dcIMQp11vYa7AyYyHao2E_MRFXM4Vgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47fbbdcf45.mp4?token=JqvEtQVAV9Yx2ITRf7F42DyJTY1IYYWVEVeNXCFmvwcTo2dSzoXvH-MqXXqhhfU9uvEc_Gzyj20YTEQZdHtf0QbUCq26rw6fjmQ-qqsSAehp-KoIRVvOpEbDVqyPlq2yS8BWmFez3MiIvBLRQjMwnMxTF_mWLXWLd7CSL6EqpkxUBzAppXpNWywt_YpbRgpKfyrRfs3m0dhOuk8w6jceIuReQT-QX6_r1MIaakEd9_WNs6Wq8-cMPJF4bBir9N83-4VZ5B4cmUZN9YNvyY60OklxrSjd_sx65Mzx-r0sMTd_RKyMLj8tz77dcIMQp11vYa7AyYyHao2E_MRFXM4Vgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسموتریچ: جنوب لبنان را ترک نمی‌کنیم
وزیر دارایی اسرائیل با لحنی وقیحانه اعلام کرد:
🔹
«در جنوب لبنان می‌مانیم و حضورمان را گسترش می‌دهیم. تا زمانی که حزب‌الله خلع سلاح نشود، هر چند سال که لازم باشد آنجا خواهیم ماند.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/660313" target="_blank">📅 09:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660312">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/263458b237.mp4?token=PklHwPTWADiZNNRVw20gknItLrJqTAd0dGDG9IjowjRtfpx86o2vloCRc3PyUPucjkohNvzK4-JM6O8scQJbAqvI3NWaHk4rVqnCY3CqCBggdz9Zh4LmmcO3fOxKomPEEBValFVi5aPl91DE4QftBOKM7FXgk7RWFFnKULfsILtUy-S2XrUyM4MH63iQxFd5gjyEDjGAurpHGmxPiLFD1u_PKUEjgAMDUpEydivZyJcJqxSAbH8dvKrUfOzen64MN3fMT-uHIqPSs289pm6JznyL6-XmbMEh4XFkLHK2EsD4dlk69qUmEg4CLNAYes53oCj_sCYwQ-S2vvJgpKZKRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/263458b237.mp4?token=PklHwPTWADiZNNRVw20gknItLrJqTAd0dGDG9IjowjRtfpx86o2vloCRc3PyUPucjkohNvzK4-JM6O8scQJbAqvI3NWaHk4rVqnCY3CqCBggdz9Zh4LmmcO3fOxKomPEEBValFVi5aPl91DE4QftBOKM7FXgk7RWFFnKULfsILtUy-S2XrUyM4MH63iQxFd5gjyEDjGAurpHGmxPiLFD1u_PKUEjgAMDUpEydivZyJcJqxSAbH8dvKrUfOzen64MN3fMT-uHIqPSs289pm6JznyL6-XmbMEh4XFkLHK2EsD4dlk69qUmEg4CLNAYes53oCj_sCYwQ-S2vvJgpKZKRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تولد اولین گوزن قرمز هیرکانی امسال در پناهگاه حیات‌وحش لوندویل
آستارا
#اخبار_اردبیل
در فضای مجازی
👇
@akhbarardebill</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/660312" target="_blank">📅 09:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660311">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8244f36fd6.mp4?token=dp-WfWbj0IprfVdY3AHNsVsa90dUFyIxe1pH0SjZmxVYEYCYSibfO1cWEdhjYBEByk-_kyq9aBbfXXe7Hd4oqBjsEliwxARhxz45wXIBg2yAGQ8m47tJ-5SFRmB566pzB7VdZZ0GmWHj_DF1bJC3-c2YEhCpa7OI-UZPvQ6ieVi2TnE6JCHaYBP_hWfHdBjUjbZBZVftnKXp2ML9DnCFvvq22Mv99Yo90Z82lpps8kYWo7TK3kg-SsC5eSy7K3Yk7bUcQNpyWBAcDq-5UpGVDvTlctZTgmaHdEvYD1wvQvRkiH-wo4xW6YAPCg64zPKrgqrhPw1Ypx1l9F9Owfx-qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8244f36fd6.mp4?token=dp-WfWbj0IprfVdY3AHNsVsa90dUFyIxe1pH0SjZmxVYEYCYSibfO1cWEdhjYBEByk-_kyq9aBbfXXe7Hd4oqBjsEliwxARhxz45wXIBg2yAGQ8m47tJ-5SFRmB566pzB7VdZZ0GmWHj_DF1bJC3-c2YEhCpa7OI-UZPvQ6ieVi2TnE6JCHaYBP_hWfHdBjUjbZBZVftnKXp2ML9DnCFvvq22Mv99Yo90Z82lpps8kYWo7TK3kg-SsC5eSy7K3Yk7bUcQNpyWBAcDq-5UpGVDvTlctZTgmaHdEvYD1wvQvRkiH-wo4xW6YAPCg64zPKrgqrhPw1Ypx1l9F9Owfx-qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف وزیر دارایی اسرائیل به اختلافات جدی با آمریکا
بزالل اسموتریچ:
🔹
در حال حاضر اختلافات واقعی میان اسرائیل و ایالات متحده وجود دارد. او گفت چالش اصلی، مدیریت این بحران در عین پافشاری بر مواضع اسرائیل است؛ به‌گونه‌ای که «طناب روابط دو طرف پاره نشود.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/660311" target="_blank">📅 09:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660310">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-h-KDI3EOehXLdu1QbXDNj1ypRvlyNH2xbcE_2FJ2L9f_JuosL_JyMkPXRpaRRvzJ47wM3e3I8Z1mrzY9QPVzRkcECO63g1IBweGuUW3NEp30HQOjhsTqfb-SSL6rw6xQsHOJs6bI6OsCsYCZKHfiCgYKd2gKqO_GvDhdNo9Kgg8kUoLi5xLMneATFU8Klx-RSl4rsRufEk6pP0jnXM9eS0Cuz_AvdGzRyrs74AecPEeJRyA5ECGTKALdnbJVnf_j1MSqMjkbHwgNxJourDOOwb5Tu4jIB71gQZp0dCSJVWJATP4M2bPUGCpKQzs4OPJqDgbePbnExjGwWtA1K2yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمسخر ترامپ در روزنامه «مصری الیوم»
رویترز:
🔹
ایران شرط بازگشایی تنگه هرمز را قهرمانی در جام جهانی فوتبال اعلام کرده است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/660310" target="_blank">📅 09:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660309">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfWPISjuL7jhUAxhUTrWBqLP_FWhQFfHyexuSEhBX6-9Uo7kknmm38Q126A4xDN1XWJO-i2ewGBArJU_r-bqO3VRG9VBgE7Mz0Oa9DSJtIj8myeiG_pvx4DuutF6S9WaO12hC2fUNiHbgc7BU18riNO_LVqGKK4JJuLKOp9P5RXafUey34zQX6z0zmTggz2DTkL8_nGsGJhl6jdsF6zMDMX7VVcXLZ2O0AqBXVSldKCivoxXE7T-SrvCPQ8dX4aZ6wV__AJ1GK81NS_wRNh2keRQp3ayaFNXBJYf6cAIaouxloKKxdCCwMdV1WsEq0_SPBL2XDQ5FTHM-0VWUXGGiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
داوران جام جهانی چقدر درآمد دارند؟
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/660309" target="_blank">📅 09:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660308">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2bf449e48.mp4?token=YpB868p2GVDzms2U6pjOnoz26Wp2X4yjDbaKAcmtaVQmS-nzQq70bNdIMPpCZEijxDhKh8bDPuWTovjVWlQpqxy8hJQwO4pb65AsOpwDuMzaWjqZRq5R6jW04I20CShq4OR_5dfggY1uKdGqYErg4l6G7MxRCt3DHJO8_SGgK9xFmTKvIf1z0G1_ZTVLKV7e59QS3wB4J2wXehmThp2hXeOzWndfzj3dW6Kj4D5rWU6OvRfS358h-laIw1VSL7y3wuMfmb3cu22qfS1h_YimhLUSDDckO2YCuWo42RUEF2xOBkGRm8Cx1GgIDczJXwMEsREfxk2Gc8V2_YYZm7tdbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2bf449e48.mp4?token=YpB868p2GVDzms2U6pjOnoz26Wp2X4yjDbaKAcmtaVQmS-nzQq70bNdIMPpCZEijxDhKh8bDPuWTovjVWlQpqxy8hJQwO4pb65AsOpwDuMzaWjqZRq5R6jW04I20CShq4OR_5dfggY1uKdGqYErg4l6G7MxRCt3DHJO8_SGgK9xFmTKvIf1z0G1_ZTVLKV7e59QS3wB4J2wXehmThp2hXeOzWndfzj3dW6Kj4D5rWU6OvRfS358h-laIw1VSL7y3wuMfmb3cu22qfS1h_YimhLUSDDckO2YCuWo42RUEF2xOBkGRm8Cx1GgIDczJXwMEsREfxk2Gc8V2_YYZm7tdbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جان بولتون: ایرانی‌ها ترامپ را مثل ویولن نواختند
مشاور امنیت ملی دولت پیشین ترامپ:
🔹
«این یک توافق بسیار بد برای آمریکا است. ما نمی‌دانیم در این توافق چه چیزی وجود دارد. اگر توافق خوبی بود، علنی می‌شد.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/660308" target="_blank">📅 09:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660307">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/047e511923.mp4?token=KgHQYR6y8FWpsan6knQqDPkX29LmZTSZnD8qIostz2O8yF6_9zmJ3IhMeUWHmKv0GrWCRBoAI4KqiKnBW32IAL7GZAbfml19kUa-u-cPJ6QxkmpTgj8I0qpIJElhlQThmo6uODvLeVv4YYMc9C6BrBXzEJKGDXJTML5ms2Yg80G2awKk1mZdw6oIWo-UfuRPWFuOe7pODJGUM_UFEWXk5qpjAz6u1ObVv66CBS8gV0TNiXy-aGGg1I6IAoeLCp12VrdlfU0T88tdBE-7n-FLyPShimRagHIQFhtsWQUclU6qfHVvZ0s1amXWvwgbDJ4x86-yGHSzrpvQrkM69BoymA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/047e511923.mp4?token=KgHQYR6y8FWpsan6knQqDPkX29LmZTSZnD8qIostz2O8yF6_9zmJ3IhMeUWHmKv0GrWCRBoAI4KqiKnBW32IAL7GZAbfml19kUa-u-cPJ6QxkmpTgj8I0qpIJElhlQThmo6uODvLeVv4YYMc9C6BrBXzEJKGDXJTML5ms2Yg80G2awKk1mZdw6oIWo-UfuRPWFuOe7pODJGUM_UFEWXk5qpjAz6u1ObVv66CBS8gV0TNiXy-aGGg1I6IAoeLCp12VrdlfU0T88tdBE-7n-FLyPShimRagHIQFhtsWQUclU6qfHVvZ0s1amXWvwgbDJ4x86-yGHSzrpvQrkM69BoymA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر صنعت لبنان درحال پخش شیرینی
🔹
خبرنگار:
«مناسبت چیست؟»
🔹
وزیر:
«آتش‌بس»
🔹
خبرنگار:
«گام‌های بعدی پس از آتش‌بس چیست؟»
🔹
وزیر:
«از سفارت ایران بپرسید»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/660307" target="_blank">📅 09:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660305">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a2e0f9b7.mp4?token=P-zx3cJA5cvUH7I2bG1YYOCIJdp0JC1rt-Ml1VHFA3eN3rcBa1AEUye_EDWhUYKcM6ApFBnpaft6BLB1bfWJV0i07laj-lOxDA4uKidEVW1ZybLWWClxs1Rih-BeHVPKlAb-lRo6TaIeKpC7mF0acUM8YgdJk1CCu6m9ncQa0LpGfBZHIEfNgBULOAuIMUdfjjwkCdSJ8YnQ0l_ozgQdtqsQBpVTv4diLk-ng61cGu1qP6YrKh6k108Q6eRG45H89AWlkFg6U9ap47EcbW6EwiT57xlVL5kPLJdMkOIKPwDCNCRGpbGRlzImcbTJaNLV25J3BWlEpSZgPTC-BneO4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a2e0f9b7.mp4?token=P-zx3cJA5cvUH7I2bG1YYOCIJdp0JC1rt-Ml1VHFA3eN3rcBa1AEUye_EDWhUYKcM6ApFBnpaft6BLB1bfWJV0i07laj-lOxDA4uKidEVW1ZybLWWClxs1Rih-BeHVPKlAb-lRo6TaIeKpC7mF0acUM8YgdJk1CCu6m9ncQa0LpGfBZHIEfNgBULOAuIMUdfjjwkCdSJ8YnQ0l_ozgQdtqsQBpVTv4diLk-ng61cGu1qP6YrKh6k108Q6eRG45H89AWlkFg6U9ap47EcbW6EwiT57xlVL5kPLJdMkOIKPwDCNCRGpbGRlzImcbTJaNLV25J3BWlEpSZgPTC-BneO4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هتریک مسی در بازی مقابل الجزایر
🤩
🤩
🤩
🤩
🤩
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/660305" target="_blank">📅 08:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660304">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992d6374f7.mp4?token=S-dEuA7LpeAg7mTKe3ow5BU6_UjJCTwYyA0S26565YSkIkztqlbhXcvJKOufNRwvvmSkD-qwetYia2qE-kJ_dQjWHwfkkzdWvUFQXs-eaCYip_hgRCTZgaWL70dYXQ33PkNvN44JGVgcIBPuv6v_ETA7rn2zaYy6wroWEnofBODXs9Q06HelV3Iaq8HzBj0LBDB4dluHI2U-RwHbYuBNTKZoqp2vcoNuRkTL2FsoDGvMrvb4UwP2VJIH5xOpeA1lNk8L5gfF4qTrEMpBCcDEpeZ92-11IuJJjP70YDvjQV9ohsG9geRLuw1S4mVSZXj8vryxUc9AGfKwCZ6nDojctg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992d6374f7.mp4?token=S-dEuA7LpeAg7mTKe3ow5BU6_UjJCTwYyA0S26565YSkIkztqlbhXcvJKOufNRwvvmSkD-qwetYia2qE-kJ_dQjWHwfkkzdWvUFQXs-eaCYip_hgRCTZgaWL70dYXQ33PkNvN44JGVgcIBPuv6v_ETA7rn2zaYy6wroWEnofBODXs9Q06HelV3Iaq8HzBj0LBDB4dluHI2U-RwHbYuBNTKZoqp2vcoNuRkTL2FsoDGvMrvb4UwP2VJIH5xOpeA1lNk8L5gfF4qTrEMpBCcDEpeZ92-11IuJJjP70YDvjQV9ohsG9geRLuw1S4mVSZXj8vryxUc9AGfKwCZ6nDojctg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم آرژانتین به الجزایر توسط مسی۶۰
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/660304" target="_blank">📅 08:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660302">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7bd7f779.mp4?token=U3t7z9cFPmbBukH8QFWh6pAAzhZ--EC-5VuY7bBX66QDbndnY5k0j62VTVc72wJZ3EoHfZGhVbaW9_UCw8KOVcmPEBOX4I1bqi4UYU56LHWyccXwtZ9KuPhXyR-YMdvpFwo5yKs1ZLGZ55ShWm9MMaazTZYE6pvLMSzen8KCb95bo-Xgcnci3rME6wRLeX9SoeVKUl0fD7cbuqbhLHACHkvSnHxrO6m1au_A7zklF8E70ZgWbYvXN02-pv4Iojy0W561ESUu_VZIHGE60kPKniJMy25D2b7WSkrgYHzFT6hMgjOjPUHuKo3jNzxxb-P6GIITFDGMjhslVT3j6mt14g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7bd7f779.mp4?token=U3t7z9cFPmbBukH8QFWh6pAAzhZ--EC-5VuY7bBX66QDbndnY5k0j62VTVc72wJZ3EoHfZGhVbaW9_UCw8KOVcmPEBOX4I1bqi4UYU56LHWyccXwtZ9KuPhXyR-YMdvpFwo5yKs1ZLGZ55ShWm9MMaazTZYE6pvLMSzen8KCb95bo-Xgcnci3rME6wRLeX9SoeVKUl0fD7cbuqbhLHACHkvSnHxrO6m1au_A7zklF8E70ZgWbYvXN02-pv4Iojy0W561ESUu_VZIHGE60kPKniJMy25D2b7WSkrgYHzFT6hMgjOjPUHuKo3jNzxxb-P6GIITFDGMjhslVT3j6mt14g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول آرژانتین به الجزایر توسط مسی ۱۷
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/660302" target="_blank">📅 08:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660301">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
زمان برگزاری آزمون ارشد ۱۴۰۵ تغییر کرد  سازمان سنجش:
🔹
به‌منظور فراهم کردن زمینۀ حضور متقاضیان در آیین وداع و تشییع رهبر شهید انقلاب، آزمون کارشناسی ارشد در روزهای پنجشنبه و جمعه ۲۵ و ۲۶ تیر برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/660301" target="_blank">📅 08:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660300">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097ef7de48.mp4?token=lwwABmfyB6G78ToG6bPQvr88xF469-PbZYAoHTE2RKFxfIUqcnPmLUvAcefQ9PTZE9Zozw9lspbKQQKn6QcE0dxPx-zlNKT--UcV8bNsFPyecUOOE9fcFeWK76l2vkLT1NsxDtCyRTjmb3pXutTCpfclB9mHoJblWeMZ8U_DTEaj3PXPdhY6yiUcr5ZrRHGbY_oGBhjCVTaCj4UO3Fc2bJIjDw3TYxsBpz33d3bsABsk-vOoyj29mBV7jK4HrXDUe4hU-sKhdvU5yVfEu9uGiZnABr8Ab9T1qsnU57XNlXk7itoLXPSob0u1Yoyz25RxZBZvvTJxpWt0eWY2jlMsuoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097ef7de48.mp4?token=lwwABmfyB6G78ToG6bPQvr88xF469-PbZYAoHTE2RKFxfIUqcnPmLUvAcefQ9PTZE9Zozw9lspbKQQKn6QcE0dxPx-zlNKT--UcV8bNsFPyecUOOE9fcFeWK76l2vkLT1NsxDtCyRTjmb3pXutTCpfclB9mHoJblWeMZ8U_DTEaj3PXPdhY6yiUcr5ZrRHGbY_oGBhjCVTaCj4UO3Fc2bJIjDw3TYxsBpz33d3bsABsk-vOoyj29mBV7jK4HrXDUe4hU-sKhdvU5yVfEu9uGiZnABr8Ab9T1qsnU57XNlXk7itoLXPSob0u1Yoyz25RxZBZvvTJxpWt0eWY2jlMsuoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات شنیدنی شقایق نورزوی درباره پروژه براندازی سیاسی؛ برچسب‌زنی برای نابودی هویت ملی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/660300" target="_blank">📅 08:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660299">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32074fbed2.mp4?token=gPGmGuWSRLFk885FAA9VgSwlETAgAeC_m6yMaBz6R9Nyg96Qt_muJQIq6XdnpDgwws_96hlOjRVZm9t9tDC6Q_LTlh20lS1cNpRbreK-dpl-OXpsQ2ChQmavaMLutXPElOWsAsLZjc-0u4mmdEfh-_lz-MkIyDuELC3ydkpMrRMaD_WqweVuq1GLblxGDmwxCTWGpKLzgCdeahZA89hvi6BkMUQWCSmKQ_fpG9dZw3XMZsF-L_9YO0qlty1T5WEjYrE60rWJtJcHINqMZT2gKn3-CrQGhDGBndrcq5tUUkePJ8Ig528fagCRsKnb8SnPedscv9CA45Q_m2dC_Jjcpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32074fbed2.mp4?token=gPGmGuWSRLFk885FAA9VgSwlETAgAeC_m6yMaBz6R9Nyg96Qt_muJQIq6XdnpDgwws_96hlOjRVZm9t9tDC6Q_LTlh20lS1cNpRbreK-dpl-OXpsQ2ChQmavaMLutXPElOWsAsLZjc-0u4mmdEfh-_lz-MkIyDuELC3ydkpMrRMaD_WqweVuq1GLblxGDmwxCTWGpKLzgCdeahZA89hvi6BkMUQWCSmKQ_fpG9dZw3XMZsF-L_9YO0qlty1T5WEjYrE60rWJtJcHINqMZT2gKn3-CrQGhDGBndrcq5tUUkePJ8Ig528fagCRsKnb8SnPedscv9CA45Q_m2dC_Jjcpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین از پهپادهای غول‌پیکر به صورت همزمان برای ساخت دکل‌های برق استفاده می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/660299" target="_blank">📅 08:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660297">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f529146bc.mp4?token=ThkR3StWncFGLm-H3NNxOASOrbmOdSsSVd-d7wCi6DnKUJLKCM9J0FbVMxBKFebDdAB6Sh7iJ-vrCsode_CTNfvPrEgMe8knC6dIPnJ_KTKt6Xr32PaLkOMAI61eLr2vxMGX-kmhs4OzYRZCb6jtlHeQQ6kB0FYshjGtdTZWaVETPBtFKTgOuZm5yX6DKpLj2gORau8mmBwg4Jny_aFNWuGf_COoXlmWpak-1jgvzUlqfhiwXMRF9AABpeWJgD6Qq4mgZ8PhhHmtqfDUkpACsRSZl23w1RqZpH-LaOkOSGsa_l4QhL2CraV5aDPlcbyaFfEGvEAjGI9ozqFPG4fzMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f529146bc.mp4?token=ThkR3StWncFGLm-H3NNxOASOrbmOdSsSVd-d7wCi6DnKUJLKCM9J0FbVMxBKFebDdAB6Sh7iJ-vrCsode_CTNfvPrEgMe8knC6dIPnJ_KTKt6Xr32PaLkOMAI61eLr2vxMGX-kmhs4OzYRZCb6jtlHeQQ6kB0FYshjGtdTZWaVETPBtFKTgOuZm5yX6DKpLj2gORau8mmBwg4Jny_aFNWuGf_COoXlmWpak-1jgvzUlqfhiwXMRF9AABpeWJgD6Qq4mgZ8PhhHmtqfDUkpACsRSZl23w1RqZpH-LaOkOSGsa_l4QhL2CraV5aDPlcbyaFfEGvEAjGI9ozqFPG4fzMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیراندازی مرگبار در بیمارستان ایالت دِلاوِر آمریکا
🔹
تیراندازی مرگبار در بیمارستان ویلیمینگتون ایالت دِلاوِر آمریکا، یک قربانی برجای گذاشت و عامل مسلح حادثه همچنان متواری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/660297" target="_blank">📅 08:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660295">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">واردات پرشمار خودروهای خارجی از قشم/ نگاه بازار خودرو به قشم
🔹
با فعال شدن کریدور جدید دریایی بین قشم و عمان پس از جنگ، محموله‌های خودروهای خارجی به این جزیره سرازیر شده است.
🔹
با شروع این فصل جدید و اقدامات مثبت صورت گرفته در جهت تسهیل واردات بی‌سابقه خودرو از این مسیر استراتژیک، پیش‌بینی می‌شود شاهد افزایش واردات خودرو خارجی و تغییرات چشمگیر در این زمینه باشیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/660295" target="_blank">📅 08:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660294">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuFP25H9tQlfXSNWRKmOsm79FZhEz9_c29LuFQx3GhLm7z5w6nvLuWYNgjop8yM1RZ2uCT6DPx0cHOw2xKWzVGh_6mojUqiPjYc5ccpmySHfyj-KMSHOwtHIPZEIicHKoUZP2FXg3UkHn2XrjVca9lltCUclHd6cVCuFI8NnHS44eBptPAUmNb0mnuNKzy2YolGorvEKOQPThsiGj-RKNb1ood1pB7KhIRf2PIzEpHvvQfbuXG2Lnqnq17g8INslvMOkEJ0z6jxnXiQG86rPOv2idV_dmRy35PezSgv617PbUFOLDcgSXirXslLr_R-Ias-f3EqqYIP2yQjySPopqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دست‌کم دو ابرنفتکش شرکت ملی نفتکش ایران (NITC) به نام‌های دیونا و هیرو۲ با مجموعا ۳.۸ میلیون بشکه نفت از حیطه محاصره دریایی آمریکا خارج شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/660294" target="_blank">📅 08:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660292">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
ویزای مهدی ترابی منقضی شد!
🔹
مهدی ترابی به دلیل ویزای یک‌بار ورود، پس از سفر به آمریکا با مشکل انقضای روادید مواجه شد و فدراسیون برای تمدید آن اقدام کرده است. #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/660292" target="_blank">📅 08:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660291">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993fab37b6.mp4?token=WNUaJGrpBlpUEcvB_jNZwfQaaSxeVZpbBgHfp7p3hoqZyaCKlMwbNyrCWs7SWFlveSbZfoPkRkF2C15IKe6M-1j5v3ZgysXRoMx5hAaa7_CTt124djDNYKut6sGr-FYki5InpUuc13VjXkOig2FH8dl_pRuoEp_KbQDTaC--lx32DIYb2sRWGzj3bK2AQNCVaSD5Stg6QKzNiw4SZep1aC7lMJFYygKu8Avwl7qFIYzS38bBHUQRO31qIPlYPnSs3ar4xUQnu46T3PDxUybfB-zLHiYxNYdb52XYWBkokv7UclT0z_cGWAZUqIJpyC8NVQmZdL8zlE_W9i2jbC45tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993fab37b6.mp4?token=WNUaJGrpBlpUEcvB_jNZwfQaaSxeVZpbBgHfp7p3hoqZyaCKlMwbNyrCWs7SWFlveSbZfoPkRkF2C15IKe6M-1j5v3ZgysXRoMx5hAaa7_CTt124djDNYKut6sGr-FYki5InpUuc13VjXkOig2FH8dl_pRuoEp_KbQDTaC--lx32DIYb2sRWGzj3bK2AQNCVaSD5Stg6QKzNiw4SZep1aC7lMJFYygKu8Avwl7qFIYzS38bBHUQRO31qIPlYPnSs3ar4xUQnu46T3PDxUybfB-zLHiYxNYdb52XYWBkokv7UclT0z_cGWAZUqIJpyC8NVQmZdL8zlE_W9i2jbC45tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یورش نظامیان رژیم آل خلیفه به مراسم عزاداری در بحرین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/660291" target="_blank">📅 08:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660290">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6e7cfacd5.mp4?token=D6T1nkqqw5fvCLqAN9YbRBS_Qs9eYV5AluiYSOIyRgxfl6M15C0Z9cCZI5HlLZcuRvHEEILJ_TJJE2ZF2cxsbQHXx6EGAepYoZpb-h_Xpc0LeVaLpLS0_kgjVdyOr3rwMsg3skwWG_T05efa8eosI2n4YmDZe5oDCffJpU2ULtBhVAm5RT-f-CIzwz16IE7QMWT4nLrzD1HRR12N9RWbedhmCgQVHdkt73zoSTUDHQxGfBAk-XHPwaNOFp0ywXWJkiBrJLdqXO_boWRrfyYOlkZEsCHJtijWYkaC27DfeAHRMCg9T4IQjG5vrNWtC4E5ca-Cq959NWNwOJrwfMuDrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6e7cfacd5.mp4?token=D6T1nkqqw5fvCLqAN9YbRBS_Qs9eYV5AluiYSOIyRgxfl6M15C0Z9cCZI5HlLZcuRvHEEILJ_TJJE2ZF2cxsbQHXx6EGAepYoZpb-h_Xpc0LeVaLpLS0_kgjVdyOr3rwMsg3skwWG_T05efa8eosI2n4YmDZe5oDCffJpU2ULtBhVAm5RT-f-CIzwz16IE7QMWT4nLrzD1HRR12N9RWbedhmCgQVHdkt73zoSTUDHQxGfBAk-XHPwaNOFp0ywXWJkiBrJLdqXO_boWRrfyYOlkZEsCHJtijWYkaC27DfeAHRMCg9T4IQjG5vrNWtC4E5ca-Cq959NWNwOJrwfMuDrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه میخوای دور شکمت آب بشه فقط دو هفته این تمرینات رو توی خونه انجام بده #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/660290" target="_blank">📅 08:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660288">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bocm6DAvxFMmkUZQGSQ3ljRDnn5MIG_qkgSppz9gNk_3AD522GD8BxA_Z2cBXuelbTYns2fbyJcKUBg_w6HIFtI-PQXAfQvL9vSzGjNc5dgxd94wzXfb6SxLkzaS6akBTSdNNPFZ7Blbf2TRffk1vePb970nGIn5jmwN0acLPVmiB1pLblnTox5WjXPcEoviahpIUzL5LcyN09uGiiRXzsxKN5tZQ1TTyBkccIzbgY0kv95bzOnSZGUx47s5VmDzJrPYRjB0m5xbPzwSNEV2gNpgxrV87qnS3vOQNi34eqnedlB1VjZ9_PikaQT-VStHyC3OOL5N1XkecmWROfWOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیونل مسی با ۱۶ گل همراه با میرسلاو کلوزه برترین گلزن تاریخ جام جهانی شد
🔹
او برای اولین بار در جام جهانی هت‌تریک کرد.
🔹
بازی آرزانتین و الجزیره با نتیجه سه بر صفر به سود آرژانتین پایان یافت.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/660288" target="_blank">📅 07:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660287">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
مخالفت دوباره سنا با محدودکردن اختیارات جنگی ترامپ علیه ایران
🔹
مجلس سنای آمریکا طرح محدود کردن اختیارات جنگی رئیس‌جمهور این کشور علیه ایران را با ۴۸ رأی مخالف و ۴۷ رأی موافق، برای نهمین بار رد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/660287" target="_blank">📅 07:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660285">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین - قسمت دوم</div>
  <div class="tg-doc-extra">عباس میرزا</div>
</div>
<a href="https://t.me/akhbarefori/660285" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
عباس میرزا
🗓
نوآوری بدون سیاست‌ورزیِ هوشمندانه، زیرِ آوارِ حسادت‌های سیستم‌های سنتی دفن خواهد شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/660285" target="_blank">📅 07:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660284">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba30c27ac2.mp4?token=jPZfyDXqEkDb6r-3N-OTce9UIFcmXzm9LuO7n0U5vviCy3sFXLxuiY7rVL0mF9D81QMa28wpJouvssbrUx0ElNviLn6if9zw-Hi1xYebcEe-sqezrHocLJEwSBbDn7oq0biGs5-7uBgrgzJNeOxz847h0eD7GfAxOkBjJeC9RECik0x_oisLrBKBFzBPuI6zL9tmv9OPpmItBBZ7G_eUoN2ut5AZYrwtADiyTbDPrGNann-giIfCl-LBMhcvXxBMx6EidoiTG1YzFoBPVI4ExPK3psU3BH1pQXty85PgmNmiqRBVCQqsJM1pNVusbWjcq_1kj4YWxi_SUk9fDRBciQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba30c27ac2.mp4?token=jPZfyDXqEkDb6r-3N-OTce9UIFcmXzm9LuO7n0U5vviCy3sFXLxuiY7rVL0mF9D81QMa28wpJouvssbrUx0ElNviLn6if9zw-Hi1xYebcEe-sqezrHocLJEwSBbDn7oq0biGs5-7uBgrgzJNeOxz847h0eD7GfAxOkBjJeC9RECik0x_oisLrBKBFzBPuI6zL9tmv9OPpmItBBZ7G_eUoN2ut5AZYrwtADiyTbDPrGNann-giIfCl-LBMhcvXxBMx6EidoiTG1YzFoBPVI4ExPK3psU3BH1pQXty85PgmNmiqRBVCQqsJM1pNVusbWjcq_1kj4YWxi_SUk9fDRBciQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملۀ مرگبار آمریکا به یک قایق دیگر در شرق اقیانوس آرام
🔹
فرماندهی جنوبی ارتش آمریکا از حملۀ مرگبار به یک شناور در آب‌های شرق اقیانوس آرام خبر داد؛ اقدامی که در ادامۀ سیاست بهانه‌جویانۀ «جنگ با مواد مخدر»، جان یک سرنشین را گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/660284" target="_blank">📅 07:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660283">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1a36081d4.mp4?token=JY5v2y1M-BvK_S0lBCrxYypYCmU837TDENrCPMLzx_CnDxz9EGUcJNyAc0lxYsqjveh-n5o2a8ekdZ4aG7VGoUpRDbJgPSwQUM9Ja-m4ZwTxLBoNaGoid6CoBBeoqW6C2veBIk8zzHjqH3mfYyq5pIocGuYDUrLVktwWbvotTfA1qDo_f2IoOxnOqRlQn1E0dExDgApYnABuguAWdWmZFXj3KzzP7sRW9-z1lSSPdP4spFWVFCrEo603dTrkkbzBrVKrdIcYYMiCawBRdQU7gRVBroLrTkr8K5azyCN-ODYGe_fXzTuvlijnh12nNEldB3zZHu1QRkdz5l9iBYoT1JIrn4-qXpo4VqCYpc2BXste59VKpL2YnP3ZqUAGvP7uINlssgqG6LOu1H7eekHLvbCM89fZX_CJe3Olgp36KdrWLCzw7qQRalfkIpCkNuQuIL7h7t52QxChPr7-Hhv_8iq5Rzk9lgpILwAsjGNAVeTqbuIDHHTAP9g75yazne2Baf8ow9x8SBvHKkrq4LO7d43y_A9TmyCL0FntrDKiIR5QGTTJH3FyRkOBY3qXQvdlNVuKZLlTP7-sFa8gDfYbQFHIIyDySLm6PfpAhUdh1M-V5xX10Ql1QEz6lX1zdUGdlaugW8TilL864zmrarusMaCNjrUvgfum2iL_ueS-6p4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1a36081d4.mp4?token=JY5v2y1M-BvK_S0lBCrxYypYCmU837TDENrCPMLzx_CnDxz9EGUcJNyAc0lxYsqjveh-n5o2a8ekdZ4aG7VGoUpRDbJgPSwQUM9Ja-m4ZwTxLBoNaGoid6CoBBeoqW6C2veBIk8zzHjqH3mfYyq5pIocGuYDUrLVktwWbvotTfA1qDo_f2IoOxnOqRlQn1E0dExDgApYnABuguAWdWmZFXj3KzzP7sRW9-z1lSSPdP4spFWVFCrEo603dTrkkbzBrVKrdIcYYMiCawBRdQU7gRVBroLrTkr8K5azyCN-ODYGe_fXzTuvlijnh12nNEldB3zZHu1QRkdz5l9iBYoT1JIrn4-qXpo4VqCYpc2BXste59VKpL2YnP3ZqUAGvP7uINlssgqG6LOu1H7eekHLvbCM89fZX_CJe3Olgp36KdrWLCzw7qQRalfkIpCkNuQuIL7h7t52QxChPr7-Hhv_8iq5Rzk9lgpILwAsjGNAVeTqbuIDHHTAP9g75yazne2Baf8ow9x8SBvHKkrq4LO7d43y_A9TmyCL0FntrDKiIR5QGTTJH3FyRkOBY3qXQvdlNVuKZLlTP7-sFa8gDfYbQFHIIyDySLm6PfpAhUdh1M-V5xX10Ql1QEz6lX1zdUGdlaugW8TilL864zmrarusMaCNjrUvgfum2iL_ueS-6p4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
#پادکست_کافئین
عباس میرزا و «شجاعتِ پذیرشِ ضعف»
فصل دوم | قسمت دوم
☕️
🔹
رهبری که برخلاف دربارِ متوهم تهران، وقتی طعم شکست را چشید، اسب و شمشیرِ سنتی را کنار گذاشت، یقهٔ فرستادهٔ ناپلئون را گرفت و پرسید: «رازِ پیشرفت شما چیست؟» او به تاریخ نشان داد: «تا زمانی که ضعفِ خود را نپذیری، هرگز درمان را آغاز نخواهی کرد!»
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://www.aparat.com/v/iqt8zvo
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/660283" target="_blank">📅 07:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660282">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/An2p3WWamWP02VIvwThnCTLaVSaD2QgO5P5JFMdDSukh83pWPDxisnDicx9Xq8ZoEQJKLtazJACJ4XdaAXTJHIyfLAJ5UPVxIGHt-tpIubaNpsCKa6uzJtdh0gpvrayFNtPfwnx4tapSvj8WZHjG8fzAV7NVQ1Y31jHblMytg3UaKkZbysP9W_1bEWRyO0SJgvoLn9kKP3Z5_f2jMp9RIjQpBPV7yxHCFADDXaxUGvPisyzALmuh_7Ot-RVtl_CUSn_jX6Vf9kXJfxTnBfRWm7VwKlIp6McSzgjWLRrFe0v_cAex22w03QCAoB1aAkiuagsBGrFV_uhj_Js-6wjiNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۲۷ خرداد ماه
۲ محرم ۱۴۴۷
۱۷ ژوئن ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/660282" target="_blank">📅 07:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660281">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_GS8XNsE6pwQpw9EY1ANM011OhDVW68D0BFoVJRn2M2yc4SqoaedLgSaMb071ZVwjxWYG8PaiRqKY1qhjKPMofjsEXM7T2kUSEnUa0GnImqI_nx1SiWsNAurY8GOFFvFaEcNSLlc_vhZ77iWqDEiiFLOITTYWxZjj_6-mewI4v3G5sqhkuf2MFICXDTJqdM-dtPPhXzGbZXu0nM3ddKZt0W3iZ8uEW4RqXk22gEEviEKt06kiffkt8wzfN4Ff9MZD300jIg5QR6EUKW0vUA6Q6gmMhISaZ5WGPFurKAMZRSSk6c00yoKuPAUwwNY2jtg99purSMfY4dhRrOBlHHXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
برند شما لنگر است یا یک قایق سرگردان ؟
💭
برای تحلیل برند شما فقط کافیه یک پیام بدین :
👇
https://t.me/+Xot5PGy2C04wMzA0</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/660281" target="_blank">📅 01:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660279">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c515eb4bb.mp4?token=eh3GrSmp3fCiapvq8aGv4oPd__11-fnrFed7kPKzMaJy4PjczthhFVQWgDRM51L28BYU9FUbGPrVxr7KrRIbTZKnaDAcNY4gbwZ1kc8N8X2hsGeKGOr0oS3Mg0jXKSLL6-e5xJnCELSqhgT0yqxCuI0Vq9BTEOcreRN_PLkX6VCpzil0XsmBZohw7uxccwDSGI8BogYo_1igefZpTHDav2XxL3ULfL9uhCQwRCKvZ6Ufubz6tgkr5sZPeD-W2ifqbckAqgLD9F1cDKo8SnVunHDXyxZ5U_qksjHQIhUGfWSJ3qzn5MwgmoewZncxrHoTWSZYR-wYuyY01s-ulNGcvDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c515eb4bb.mp4?token=eh3GrSmp3fCiapvq8aGv4oPd__11-fnrFed7kPKzMaJy4PjczthhFVQWgDRM51L28BYU9FUbGPrVxr7KrRIbTZKnaDAcNY4gbwZ1kc8N8X2hsGeKGOr0oS3Mg0jXKSLL6-e5xJnCELSqhgT0yqxCuI0Vq9BTEOcreRN_PLkX6VCpzil0XsmBZohw7uxccwDSGI8BogYo_1igefZpTHDav2XxL3ULfL9uhCQwRCKvZ6Ufubz6tgkr5sZPeD-W2ifqbckAqgLD9F1cDKo8SnVunHDXyxZ5U_qksjHQIhUGfWSJ3qzn5MwgmoewZncxrHoTWSZYR-wYuyY01s-ulNGcvDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات ناامیدکننده ونس برای معاندین و ضدانقلاب
معاون رئیس جمهور آمریکا در مصاحبه با برنامه آنلاین «مِگین کِلی»:
🔹
«ترامپ هرگز نگفت که هدفش روی کار آوردن رضا پهلوی برای حکومت جدید ایران است... آنچه ما می‌خواهیم توقف برنامه هسته‌ای آنها است».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/660279" target="_blank">📅 00:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660278">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ادعای تانكر تراكرز: یک محموله نفت خام پس از دو ماه محاصره دریایی، از ایران خارج شده است./ مهر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/660278" target="_blank">📅 00:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660274">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ScOvFlvcUCdjF9sHqbMjJyJGheWFCsrCzvnXBw4NbvZfx4L5dPo8naqXwjZ_hF4wT9ZCSwEfH4exUZf5N9GX38ZfPxoGcPM6jbgQLJcZRHYAAzoppEFw5smsHgiVwHtWxc33uy37xJ3i504g-QiCMeusSajlo3LqElgoS4HCh2yTidBLjc-mAfqd4r6sl9gFqzg4iJywN_NrNtDYVdCjvmpRL3RSXQQ63A_IUmqk9wpJNyleai3CwT8CXRI1PkgMDtU1jKy9F6Z3JO8LaRi9S2acu46hX5dFknGpMdLOdly7c1KyR_r7-hliPl-9bXv133TsWaJnIX4z_OInkbMmtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQ_62j__eGzVjvcOBXBlQEijmflbeql-R7I1hyKYUwU-g5n458WMdU_jZiuSIHZNaVuAXXscHV8Af-8ZaZOs8hEUnyyT5KRkZIyohb4HfYhROqvhNlbLdVm16OQ8mk-quLbNfMhlSu5-j5jUrCNMaBHIdDEJw8_NGZBESIja5XHQtdfN4DcWBvuXEdEWT6HfFmsAhab4GAGVH2qbL6Tc_KXvvzJDCWi5KCAhKisqoG3z7Ila0LcBfuljrnUcam2duh_JHwvvo7rB5mfMsK5EYmzxfsrHn4XZtXqkVKQguabpNl8XFjlunt0Mgny4qfheD1aJBOIfeXd3GxfHpRMCPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I2wMRMpK4zvIQaSX7sRHiuiPOjfSWYkeSAC8IN1HxVROFGlE23px2fb8ubbhsmT7QP2Z1KrKjJey4yOC4Q9TDIzSvvo1vUangchZEPd1TaVJDw8taAXaeyZteM9dsiUPI8_bd6Cm-2JB4McrjMLNLaL1zILEmsZmo-k9jfU77uefhZj-QWGbTeIzY5oAC_EOZP7W84nyTzCxJFsOh6DlYSSAJ43g1IlglM3RlpqNRexGTzdaxwwqbJhQdokP3uOzH_YVKjMJS50649PJhcUddYSHZQGmz0F0je4rmWPUW4Tt8J6FQ0VPeYCT71mdUKPuM5A7fxv2e3zPcGqNj8JBoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lYuTgueF_tQrrBM2jqKrQSqVlg_SMb787SMEYoWK0bB48RiK2Oc59hsA00MIqd_C2ZJbKX_VLR800F819u4YrMM0lB4jVGi-Q4c_7y55GclokZi-eNkSjhoqsPZb-ObBtbobM83MosHCkEvUR7x7FB48HmLsfICCvZpkkBy3uHrJluxZt99dTrfL6cdjK6-8l1OGkyHMTFtFiAqNoiWvtpKk4rLoiQ9qAYlg8bTfCKQDdtIdfV1uEyuHslcaPUr6c_Fn3HiCAlrc1y93ovvge-h7lgw3LQ-HcZf52sY11so667_lHFvxv12ak3eljjxHy6IJUmWu6J_CrDOZdwtvMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رویترز: تفاهم‌نامه ایران شامل اعطای صندوق  سرمایه‌گذاری ۳۰۰ میلیارد دلاری است
🔹
تفاهم‌نامه بین ایران و آمریکا شامل برنامه‌‌ای برای  تشکیل صندوق سرمایه‌گذاری ۳۰۰ میلیارد دلاری به منظور حمایت از اقتصاد ایران است.
🔹
این صندوق تنها پس از امضای توافق نهایی راه‌اندازی…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/660274" target="_blank">📅 00:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660273">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7nLEEWPsAQzItoWpRErN9YNcDWWcrE1HuGS9-eXmPhyLsCIEUlrsM1xoMJvNnlpixr8JV_8t9pjWlrtOt6hr4lmGLdqcvxedJ-Lnm2GFnAbjFfUEt_hNZn14_1SQNelSlO64RvVTTG3m90V4S5srCLOXnz2mPXPxT84CB0rFBBR6mXEEfMex925IiyjZMt-rd-0BQPLfnfvePvAfdoua9k9cCot8gJyk0Dt4gBMAdbHuxIuLHV46_ywcKngxzD-ZZtySOmwleDY1Pp8-jfrOLrOn1YZu1mjEA2ytKBObbeKoM1_V8kEhUDO2KsvfGJ9rseE2X7GmfyivnDkYVW0_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جام جهانی فوتبال | امباپه با توپ پر جام را شروع کرد
🔹
فرانسه ۳ - ۱ سنگال
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/660273" target="_blank">📅 00:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660272">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d84fcb79.mp4?token=uR9G7nZdekUq_e7DJV6748Q4c974i305ltK23jPPjrSWCLcSyeVuY9rulNVZjqg4dw9l1W2bIaUi4RRM0DYmZ5aBQkoYA0A_mYogtQ2KTVngFzd80LeI7ix9vHvCNKYRTYvBKi2UYwoYXdbMNdPAVFbmMcGtiVEWZoB30ntLWkU904rfcTWQNSz5YJRlvJroozAF87fovno5Z251HrEkdLDr-XNsQPwxW9lFD48fDWJ_ULxIGpfxARBQN4Ir7_SMp7iA91KO1NUs_ayYEVsuFDYDJYxFKhnjLBUuTOcsNirsv-yK8yhjC307rR40YVvUVUCVj6l8OlvZZwe8NASCQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d84fcb79.mp4?token=uR9G7nZdekUq_e7DJV6748Q4c974i305ltK23jPPjrSWCLcSyeVuY9rulNVZjqg4dw9l1W2bIaUi4RRM0DYmZ5aBQkoYA0A_mYogtQ2KTVngFzd80LeI7ix9vHvCNKYRTYvBKi2UYwoYXdbMNdPAVFbmMcGtiVEWZoB30ntLWkU904rfcTWQNSz5YJRlvJroozAF87fovno5Z251HrEkdLDr-XNsQPwxW9lFD48fDWJ_ULxIGpfxARBQN4Ir7_SMp7iA91KO1NUs_ayYEVsuFDYDJYxFKhnjLBUuTOcsNirsv-yK8yhjC307rR40YVvUVUCVj6l8OlvZZwe8NASCQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوپرگل کیلیان امباپه به سنگال در دقیقه ۶+۹۰
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/660272" target="_blank">📅 00:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660271">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e180aedc5.mp4?token=TFJfg6sEZuxQl8RlwVYsM6hPCQ99OMPJF3DtyzWJiqFAwhWN4xfnYYDa5BiSms65o66WMkIGukn8b8JQpPvL39hZokaKzRyAClNoRMS_UQOOLfpau0wB35jlOyvH3qPPPBd9MJz_b0nKwkYnMtQDy9TFrKrvur7rHXsQj49KxKiPKlKtqk7Fe7E-pduVRQZLTy6UELYdd-2aA_VaqAz4NgMxozj2lJTGNDF_3ZyxTZFeiWpT2iyS3mYBsqufX7PzJUJKaX9U7m9mWKhAkZVcbyZjIiWnC7pqDijBeIjq5o3633UgTQ1wmOUxlov5NKYc0JSpvuPfoMHJ8odJkCQlhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e180aedc5.mp4?token=TFJfg6sEZuxQl8RlwVYsM6hPCQ99OMPJF3DtyzWJiqFAwhWN4xfnYYDa5BiSms65o66WMkIGukn8b8JQpPvL39hZokaKzRyAClNoRMS_UQOOLfpau0wB35jlOyvH3qPPPBd9MJz_b0nKwkYnMtQDy9TFrKrvur7rHXsQj49KxKiPKlKtqk7Fe7E-pduVRQZLTy6UELYdd-2aA_VaqAz4NgMxozj2lJTGNDF_3ZyxTZFeiWpT2iyS3mYBsqufX7PzJUJKaX9U7m9mWKhAkZVcbyZjIiWnC7pqDijBeIjq5o3633UgTQ1wmOUxlov5NKYc0JSpvuPfoMHJ8odJkCQlhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول سنگال به فرانسه در دقیقه ۵+۹۰
🔹
فرانسه۲ــ۱ سنگال
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/660271" target="_blank">📅 00:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660270">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72d7ae431.mp4?token=nZItIti8hdRuprtECSsAqJDuX0bcQzEBcUtsykz78aRJMtw_3ulkk5P6OA_bEXkoKoboFowQLApfRMOzGzSRbis4c-oHDjP6iHWcHU7vLvOYyEeTXn08rkS0OlWMkQ6EiFAJVqIUCT8fE6qwEzQhRZP88TmUN6AxtTFZTuotqYb812okmU--NPnb3Wk2-IfuC0UmCKa3CoMk1Fv_xSeurjZwgmPq7_U3KNpoFxrAIyN8bEmav9W4pK8V2uNL_I8yns9QpySUEcXpHb1gr6SoQ26u7S2K0n04ieUA_w1AUcfFXHgZzsSXV2328Yrg1iqvwCQh4XqiHQu0dxNKKKktjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72d7ae431.mp4?token=nZItIti8hdRuprtECSsAqJDuX0bcQzEBcUtsykz78aRJMtw_3ulkk5P6OA_bEXkoKoboFowQLApfRMOzGzSRbis4c-oHDjP6iHWcHU7vLvOYyEeTXn08rkS0OlWMkQ6EiFAJVqIUCT8fE6qwEzQhRZP88TmUN6AxtTFZTuotqYb812okmU--NPnb3Wk2-IfuC0UmCKa3CoMk1Fv_xSeurjZwgmPq7_U3KNpoFxrAIyN8bEmav9W4pK8V2uNL_I8yns9QpySUEcXpHb1gr6SoQ26u7S2K0n04ieUA_w1AUcfFXHgZzsSXV2328Yrg1iqvwCQh4XqiHQu0dxNKKKktjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون ترامپ: تفاهم‌نامه ایران، شامل لبنان هم می‌شود
ونس درباره مخالفان تفاهم واشنگتن و تهران در آمریکا اظهار داشت:
🔹
«آنها می‌خواهند این [جنگ] تا زمانی که تمام بمب‌ها انداخته شده یا تمام ایرانی‌ها کشته شوند، ادامه یابد... آنها یک درگیری بی‌پایان را پیشنهاد می‌دهند».
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/660270" target="_blank">📅 00:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660269">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a713a7d66f.mp4?token=p2O9yNtUnLft4LiUN39RTQIQEy1Fq-SJSUYiin7e84dYmBXehbS0OME6sr6qXAajjgINayNwAfZbzgeLNHY8v8M8e4b7XxpQn849yby72fGWwNG3sDcaPc_brkK7Jxq_zT8KwJoXp6nPzvSwdRM2gZXirhEMbcdMov6PE0zzQSoSG1ctzwEH_JgOqXc5dAnWEC2c0coqan2B9t-UthcqOgwzneJFT0uL50hJuJGXw2ZVKFfEQcYo-8-JnAq_KfNse7evGmNNx1Eo8SzWo88oJoqHVFnwUcBUBIEq74PKxpuuGMQtUPQAnZZR7YJo1f23Of1bwGIZ8p7qfDvKCDutFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a713a7d66f.mp4?token=p2O9yNtUnLft4LiUN39RTQIQEy1Fq-SJSUYiin7e84dYmBXehbS0OME6sr6qXAajjgINayNwAfZbzgeLNHY8v8M8e4b7XxpQn849yby72fGWwNG3sDcaPc_brkK7Jxq_zT8KwJoXp6nPzvSwdRM2gZXirhEMbcdMov6PE0zzQSoSG1ctzwEH_JgOqXc5dAnWEC2c0coqan2B9t-UthcqOgwzneJFT0uL50hJuJGXw2ZVKFfEQcYo-8-JnAq_KfNse7evGmNNx1Eo8SzWo88oJoqHVFnwUcBUBIEq74PKxpuuGMQtUPQAnZZR7YJo1f23Of1bwGIZ8p7qfDvKCDutFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم فرانسه به سنگال توسط بارکولا با چیپ دیدنی در دقیقه ۸۲
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/660269" target="_blank">📅 00:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660268">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e388fdb82.mp4?token=dCeYmR5DutxJB4ETba3UXeCAtPLu77qAW9o6WoRgIkNeWQRsvxWptM0JNAzPNl8e3LwRmBSw1c4Ncb1B16KvQtUFfr-nS8UfXzZU5uAiu3kqeDC13UzBWG4X3b_-dlBY6yDWwvaSZT0uo4M3bDle-avGgUYaEQMtHk8hi9AuYSzTjqow_BnCZblSoYKWEBwxYGJ2mOVmucPTL49IH6bwfpgqNVqQC50112MarBhi2lCqrSUkJ6YKZp4teObMo4UgSSSmsK7QcwM1qsqQsb-9COJ7tXyrD6LZhkM-eVdzD8yWDRW3qgB3GnOYrDoBcyPvgFnKdi2_xFIchRAlh3psjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e388fdb82.mp4?token=dCeYmR5DutxJB4ETba3UXeCAtPLu77qAW9o6WoRgIkNeWQRsvxWptM0JNAzPNl8e3LwRmBSw1c4Ncb1B16KvQtUFfr-nS8UfXzZU5uAiu3kqeDC13UzBWG4X3b_-dlBY6yDWwvaSZT0uo4M3bDle-avGgUYaEQMtHk8hi9AuYSzTjqow_BnCZblSoYKWEBwxYGJ2mOVmucPTL49IH6bwfpgqNVqQC50112MarBhi2lCqrSUkJ6YKZp4teObMo4UgSSSmsK7QcwM1qsqQsb-9COJ7tXyrD6LZhkM-eVdzD8yWDRW3qgB3GnOYrDoBcyPvgFnKdi2_xFIchRAlh3psjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس: اگر ایران حزب‌الله را تامین مالی می‌کند، ما اجازه نخواهیم داد که مجموعه‌ای از دارایی‌های بلوکه شده به ایرانی‌ها منتقل شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/660268" target="_blank">📅 00:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660267">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noNM2ETA8m43YenzAM0aMiSsIAn2UAMOex8prlS2aY0Cb3p6HX2YNjIarviLRsJoOI10p7VHvCJQyZtsB-KDuelirWLfZrJ7Z6za1HWsA42ntbwmwXSpXcRHa8KNTmGBuw5aX_an-mgvs20o0f7ZMmor8Cp2BacgBdL4kaau9o4DaRFSBaQkkJxN2On2SBpgQOHtvxFhhitI2B9ePEq2rcxg0NVYX-K3cMiVTnR_rfNiVxVMUncX7q0xZgYk0fyYYngTZOpG3CwAPm5U6t5b2LJNR8dDCg7ERGTtYPZtSJgoxXit4TX1o-A04viCSanEABIagHz1xo2IL8-EVoUgCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان تعارف‌ها
🔹
اقتصاد، مهم‌ترین میدان نبرد کشورها در دوران جنگ و صلح است و تجربه روزهای پرتنش اخیر نیز بار دیگر این واقعیت را آشکار کرد. از همین رو، مهم‌ترین مأموریت کشور در دوره پساجنگ نه صرفاً جبران خسارت‌ها، بلکه آغاز یک اصلاحات اساسی، عمیق و شجاعانه در ساختار اقتصاد ایران است. بسیاری از چالش‌های امروز، از ناترازی‌های مالی و ضعف بهره‌وری گرفته تا موانع تولید و سرمایه‌گذاری، نیازمند تصمیماتی فراتر از اقدامات مقطعی و کوتاه‌مدت هستند. شرایط پیش‌رو می‌تواند فرصتی تاریخی برای بازسازی اعتماد، اصلاح سیاست‌های اقتصادی و رفع گره‌های مزمن اقتصاد کشور باشد.
🔹
همچنین هدایت نقدینگی از بازارهای غیرمولد و سفته‌بازانه به سمت تولید، صنعت و کارآفرینی ضرورتی انکارناپذیر است. مسئولان باید با درک اهمیت این مقطع، از بازار سرمایه حمایت کرده و با حذف موانع ساختاری، زمینه تنفس دوباره صنعت و شکل‌گیری رشد پایدار اقتصادی را فراهم آورند. آینده اقتصاد ایران در گرو اصلاحاتی است که نباید بیش از این به تعویق بیفتد.
🔹
هفتصدوهفتادوششمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/660267" target="_blank">📅 00:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660266">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
ونس: ترامپ به‌دنبال تکرار تجربه عراق در ایران نیست
🔹
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، با رد سناریوی اعزام گسترده نیروهای زمینی به ایران گفت دونالد ترامپ «جورج دبلیو بوش نیست» و آمریکا قرار نیست وارد «باتلاقی» شود که برخی درباره آن هشدار می‌دهند. او همچنین تأکید کرد که باید در برابر درخواست‌ها برای اعزام صدها هزار نیروی زمینی به ایران ایستاد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/660266" target="_blank">📅 00:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660265">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e34e7174.mp4?token=cK1TK8nsr4j_2mde4M9zf4l6L77SALvCE1SUAwcG0lZZyYCrx0Gu1SUNeh_XSBC7kqIrAej_9QngbTp4g8Yg70G75Vopb8dRBZAR_rqx2InPTkWquab6HcirziklovY2KDERLPiNeB0kdLWHMvw5mykw1VsO8vsM1E_oCU9eV8iZmNPsBKlQ81NcUGrmeNF1K8nFdf7tDM6Lpo6_b_8YIycqOxB07qZO4FsrlBotrXPSa4dp4o7yW2Ys1E-ztbr9h4A336Olzi_PnNrKR7mAnjYyVxFD0-uwW_-KYe3-xfoKKN4jOFDU91OAt5yu9LmomFjnTe2FEfNt-yPgs2RzEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e34e7174.mp4?token=cK1TK8nsr4j_2mde4M9zf4l6L77SALvCE1SUAwcG0lZZyYCrx0Gu1SUNeh_XSBC7kqIrAej_9QngbTp4g8Yg70G75Vopb8dRBZAR_rqx2InPTkWquab6HcirziklovY2KDERLPiNeB0kdLWHMvw5mykw1VsO8vsM1E_oCU9eV8iZmNPsBKlQ81NcUGrmeNF1K8nFdf7tDM6Lpo6_b_8YIycqOxB07qZO4FsrlBotrXPSa4dp4o7yW2Ys1E-ztbr9h4A336Olzi_PnNrKR7mAnjYyVxFD0-uwW_-KYe3-xfoKKN4jOFDU91OAt5yu9LmomFjnTe2FEfNt-yPgs2RzEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول فرانسه به سنگال توسط امباپه ۶
۶
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/660265" target="_blank">📅 00:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660264">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xlr8wokCow8oomRvY286LC6ZL6ywHqHrGe6FmwicjMMcDlO-MVEKcK3CCZvM1ZsEJZLw0ZmyrnsbkTKg9EQvz3JA6W3jdUIc42gpoLx8bbYcW9CTxvfQYHntfCHU3LEsQDFiR6yZPzjPvwphtRkRWyKavy4qLXP3CXlwGKfocPIPHmVt3-rPSuiUYNTl1vuQjyjZaIBEVYGQwrW-xObAoJF5Wc4wdZC8cpik0ZweWTBAoTcIZ9r_vu7OmKnsHFccKsw1AjIP-tRDKQejkBwYAJe6hZlW5XTAz8sxDgIIhCsxKfZqjqHVhPdpLgKy5dX6wL6BvapuxodZuLMI7VWlMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/660264" target="_blank">📅 00:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660260">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70bdef0fa1.mp4?token=EdZut5fcADwvxuT_7zsTN_qkUKKC7PlNbkd-I5Q0yJhlsmoJKB-Jm0VgBIOXjI0LB710LvoH84tG-nQhJsKdvO7Z9KTAF105wUfSyAa0nGbs8plXpCIql0e90M0Fiz-1gZNKzkJQ9-jnQf8-KI8kWH-hm7Z6cp-BNruXBHfzhGnfhqGwRHtrVzv_yIsnPUqCLhivq-ldF2ysWhFWfoDryh5eiRh9R2fVyEVcfBdMqb9VG6Oiyc9C9agLx1YRIJa3TcBxqpDv8gsOqV3Obz2sB3i2X4bHv17OcC3q3Z1jP-VB5R8cksgzxBsbOml529YThr9TWfDMyHS00WKJQNZO7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70bdef0fa1.mp4?token=EdZut5fcADwvxuT_7zsTN_qkUKKC7PlNbkd-I5Q0yJhlsmoJKB-Jm0VgBIOXjI0LB710LvoH84tG-nQhJsKdvO7Z9KTAF105wUfSyAa0nGbs8plXpCIql0e90M0Fiz-1gZNKzkJQ9-jnQf8-KI8kWH-hm7Z6cp-BNruXBHfzhGnfhqGwRHtrVzv_yIsnPUqCLhivq-ldF2ysWhFWfoDryh5eiRh9R2fVyEVcfBdMqb9VG6Oiyc9C9agLx1YRIJa3TcBxqpDv8gsOqV3Obz2sB3i2X4bHv17OcC3q3Z1jP-VB5R8cksgzxBsbOml529YThr9TWfDMyHS00WKJQNZO7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله طرفداران الجولانی به مغازه‌ها و منازل علویان در دمشق
🔹
براساس ویدیوهایی که از دمشق منتشر شده، طرفداران شورشیان سوری با حمله به اموال شهروندان علوی خواهان اخراج آن‌ها  شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/660260" target="_blank">📅 23:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660259">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
این که الان یاد توام برام غنیمتیه
وظیفمه، نه خواسته‌ای دارم نه منّتیه
🔹
محرم امسال، بیشتر از همیشه یتیم
شدیم…
🔹
ذکر مصیبت با نوای حاج امیر کرمانشاهی
شب اول اقامه محرم ۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/660259" target="_blank">📅 23:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660258">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
کلینتون: نتانیاهو برای بقای سیاسی به جنگ نیاز دارد؛ توافق با ایران می‌تواند پایان کارش باشد
هیلاری کلینتون:
🔹
نتانیاهو برای حفظ موقعیت سیاسی خود از تنش و جنگ بهره می‌برد و معتقد است توافق احتمالی با ایران ممکن است به نقطه‌ای تبدیل شود که زمینه کناره‌گیری او را فراهم کند. او همچنین نامزدی دوباره بایدن در انتخابات ۲۰۲۴ را «یک اشتباه بزرگ» توصیف کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/660258" target="_blank">📅 23:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660257">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
ترامپ بالاخره اعتراف کرد؛ تلاش‌هایی برای تغییر رژیم در ایران صورت گرفت، اما موفق نبود
👇
khabarfoori.com/fa/tiny/news-3223498
🔹
شلیک به سمت تماشاگران آمریکایی | شادی گل محبی جنجالی شد
👇
khabarfoori.com/fa/tiny/news-3223387
🔹
«60 روز سخت» پیش روی ایران و آمریکا/ این 4 مساله توافق را به جنگ تبدیل می کند
👇
khabarfoori.com/fa/tiny/news-3223563
🔹
سوتی امنیتی در اجلاس سران | میکروفن روشن، اعتراف غیرمنتظره مکرون درباره ترامپ
👇
khabarfoori.com/fa/tiny/news-3223598
🔹
یک بانک دیگر هم دچار اختلال شد
👇
khabarfoori.com/fa/tiny/news-3223577
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/660257" target="_blank">📅 23:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660256">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78b5fc6840.mp4?token=tcLFSrI6FiwsOhyGIHKsg1g0-VAnqWe1feE9GEC9G0nkNv2wkVMkGfp9cwRBNh4nwewdYYTaZp4O2Ir5JnGL004vjPn_T9srFbzAhrTAvcFgcEMs931xDzDO_N6IQUt1DreHZcFicllKxH0kP87X9Lq7b-ayHS-QTYAbTK7gDvzPqhlFjsd8cCjHTrsVg8sUBxXd7PUAbZFZdd1tPL-ufhUahpyrKvcgqjwWoRTtSAwzerfVb7QGalGWPAhGsOk2Isw6xDbE-IDfMawn1SuWkGtsm8zFnmqILXk5vrXzQ_0V8AXcW6BR1qlSiCfxK12Wrc7hSTIz0TGKITJXcYCftkbcbSLIxEZT9tqVi-bVqMuVjkuyerwJPxjb8NH9Ln8H-3Oxdht0gzxL4T-s4he0Ss4P6_51qKDcoJlOX8pYCN0yh7G4Zh_YuBVK3N8XTQGHQQ1Pi3x1YTLXKDkSa9S-hZXtwB5i5PgE-Y0ZwSi3_Vj2z6GkpVX8_-KmZRnAnmewHJ5MWSfla-d9PEvv-kEJE0aVRSit1ump9SlZdnmkZNye8un9iXRJT26dfdn4BCR7rNlFFVFETNzbgg6bLuEnfbxC3rO_8VVNK9WE1P2PbsLkSjWyBsh0ZYZeKL6J10-ZuilQpZIm5brMJ1i8pGmY6mM6r-6hcll1LpT7B8t2EUk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78b5fc6840.mp4?token=tcLFSrI6FiwsOhyGIHKsg1g0-VAnqWe1feE9GEC9G0nkNv2wkVMkGfp9cwRBNh4nwewdYYTaZp4O2Ir5JnGL004vjPn_T9srFbzAhrTAvcFgcEMs931xDzDO_N6IQUt1DreHZcFicllKxH0kP87X9Lq7b-ayHS-QTYAbTK7gDvzPqhlFjsd8cCjHTrsVg8sUBxXd7PUAbZFZdd1tPL-ufhUahpyrKvcgqjwWoRTtSAwzerfVb7QGalGWPAhGsOk2Isw6xDbE-IDfMawn1SuWkGtsm8zFnmqILXk5vrXzQ_0V8AXcW6BR1qlSiCfxK12Wrc7hSTIz0TGKITJXcYCftkbcbSLIxEZT9tqVi-bVqMuVjkuyerwJPxjb8NH9Ln8H-3Oxdht0gzxL4T-s4he0Ss4P6_51qKDcoJlOX8pYCN0yh7G4Zh_YuBVK3N8XTQGHQQ1Pi3x1YTLXKDkSa9S-hZXtwB5i5PgE-Y0ZwSi3_Vj2z6GkpVX8_-KmZRnAnmewHJ5MWSfla-d9PEvv-kEJE0aVRSit1ump9SlZdnmkZNye8un9iXRJT26dfdn4BCR7rNlFFVFETNzbgg6bLuEnfbxC3rO_8VVNK9WE1P2PbsLkSjWyBsh0ZYZeKL6J10-ZuilQpZIm5brMJ1i8pGmY6mM6r-6hcll1LpT7B8t2EUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون سابق رئیس‌جمهور آمریکا: نگران آنچیزی هستم در مباحث عمومی درباره تفاهم ایران و آمریکا زمزمه می‌شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/660256" target="_blank">📅 23:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660255">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3nolfddeWoGF57fnkk4RzA40SRwvuDAuOIWyPWy6qjEaefY02Q1nE65qv8kcPPCw3AE6RNsgVyRMUIy8AOpEmW2nsf2yaW0ihLYCFd9yrD22qhPDSp-XxI0HdLbckao5e1SgX_1fyIxCM2AdxwGRxWv3yyEjwqH2h2Vxg3WWzT0g_Gf0v5YisJxYJFzl7Ce0PwA8WxufrxJ___jwykN2J2W6OWBbNyV-p-gP1hbA-LPJ_P56PCZTCC2915X_kKoPSKKYNs8IjVEnmnaR0o-JAKy5fZY3KpbiT-QyaSUvgVe87ixQ41mDjSmNJHWJWPOd-vP9HD767ISbry5lvqbmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخورد قضایی با عوامل اخلال و هتاکی در دیدار ایران و نیوزیلند
🔹
بخش قابل توجهی از افرادی که در جریان دیدار ایران و نیوزیلند در آمریکا با سردادن شعارهای توهین‌آمیز، ایجاد درگیری و هتک حرمت نمادهای ملی اقدام به اخلال در برگزاری مسابقه کردند، شناسایی شده‌اند.
🔹
بر اساس این گزارش، پرونده این افراد برای پیگیری‌های حقوقی و قضایی در حال تکمیل است و محدودیت‌های مختلفی از جمله بررسی وضعیت توقیف دارایی‌ها و منافع اقتصادی افراد مرتبط با آنان در دستور کار قرار گرفته است.
🔹
همچنین در ادامه فرآیند برگزاری مسابقات جام جهانی نیز، چنانچه هرگونه اقدام مشابه علیه منافع کشور صورت گیرد، مرتکبان ضمن شناسایی و تعقیب قضایی، با اشد مجازات‌های مقرر در قوانین و مقررات مواجه خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/660255" target="_blank">📅 23:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660254">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
این روزها خیلی از بازنشسته‌ها می‌پرسند چرا افزایش حقوق بعضی‌ها ۶۰ درصد و بعضی‌ها ۴۵ درصد بوده.
این ویدیو پاسخ همین سؤال را می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/660254" target="_blank">📅 23:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660253">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmTioboVrDWySNwUiO6c2_BZLzrVmkcPyzDF5JQmaK_CM7yYi-Id-qswvaW4wuqNKUJh5wULAstulNsMXqIYewQuv5dENx53mVEX7DHwWA6yL_rvsO-pz0bs-gEgNMqL9n4Lc_aG6tmsfj2MoFxauaqOmpGjDcjlVLFWAs4uMzDgg7WW3eGgslnWbFJn6CqA8ePe5bl78VAfg_yUxGASVmVYqbIYEkjoWw0fEAPzfqmzgrBLedt_IBO3lvMXol5KDNWCB_C0ANxNViQoA1PZ8yYD-wbNXmAm1zRk5ecNyEmkbdWd1h_UKHhM2b20Z-65q0sqnWq84UU24Y9vzeJn9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکذیب خبر خداحافظی محمد شریعتمداری از هلدینگ خلیج فارس
🔹
برخی رسانه‌ها اخباری درباره خداحافظی محمد شریعتمداری از مدیریت هلدینگ خلیج فارس منتشر کرده‌اند که این خبر تکذیب شده است.
🔹
بر اساس دستور رئیس جمهور ادامه فعالیت محمد شریعتمداری در هلدینگ خلیج فارس بلامانع بوده و این موضوع به وزارت نفت ابلاغ شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/660253" target="_blank">📅 23:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660252">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
‏
ارزیابی اطلاعاتی در آمریکا: ایران ممکن است در پی حملات صهیونیستها در لبنان، بدون هشدار قبلی اقدام به حمله غافلگیرانه علیه اسرائیل کند./
تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/660252" target="_blank">📅 23:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660251">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
سفر محرمانه هیات اماراتی به اسرائیل طی ایام جنگ علیه ایران
🔹
یک رسانه اسرائیلی فاش کرد که هیات امنیتی بلندپایه اماراتی در ایام جنگ علیه ایران به‌صورت غیرعلنی به اراضی اشغالی سفر کرد؛ سفری که در چارچوب تبادل دیدارهای امنیتی و هماهنگی‌های فزاینده نظامی و اطلاعاتی میان طرفین انجام شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/660251" target="_blank">📅 23:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660243">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JvGUukxMAslW9Egqui5GLN1KGIBQfjI1IKsiO6LnWFN1U6uRZf2u3VzltYku259T9UhdP2Zl3RRnwf6pHT5NAiPgNIHrlxS291XNqxiyJgscC5BRns1aFF_1a3r0UjU9-FNRw_EMqpk0rsuZEYOzIH80EnR1qIS7UK-XGW5NsdmLDtRPypUHiUeYucJTA0pkhINVyhO9Y_ZHW-4386D2BFKlGE612VS9TqzYE5k8sViZgrVzt-c7Z7rWfxVFi8NrHCzYlG5VpGfKaD3pVYulA4SEslLjEp0s4cPAcE8I2bUr12yiboYglh2M1ZKzOfgYvPVH0WDMyc0Or5G-1j2wqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KZI4NFWDh0hA2kEiYbMykvFSJ5tTh-Y2bfGqc63bECoO_gG1M_dp0aE0IRBT732WC7GodRzIgbC4JAha65n8woLm-4aA08mmylMD70U8l-VFDUyxZCvyMCW2LR7kmzuXScGEq-3RBrP-I97jwUkZ0Bn3fZLjZc2enGc1XgerOGGkeuyGCI4DgVaO7BXFK40G86GZUAt16lawCkkCkKngkGolKC_q2B4JUE_5sB_LIIV6J95arnNkCxOiVsOZlRDNmTNm0CAzBzDAEFGC-VcoaX1sPZJVrYJVVussdir25uRyjQh2sc1_RSTZ2hG6qTqnEYBf4huWBxk3kK26xPU0lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/InqLfshk5DbLWGxZPLTISAGOZNengKxUqoL_6kxFQD8vUi_m1MnLQaD8n3qgkH1Ei0C3Q_rTsZn3gGEIjZUmQyfhcPqA8e_JRKsGgmDVE8H0luny8BUMl3nSMsKwZjXo2lth2H9-jETj6HwUJSVOWfWgZRR91QDjP2fVFSpBpn-lON2IpCSOjBUp2zD4MlzfsakPe2d3b54ko2UQwvirMexjyZ6Q6yEekklFmYq6z-j4TW5l__zYRNG0ZGboAjDquMUGvQI38IXrGpXdZk2WvrGbBH73UD8TGr52em7l-suIh8xNeSpvJwW0YMMEXWROUR3wF2kz8s7pawWSAe4SxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zbg_gsN3Wb3HnyhW_fKG4YZMLZUIh5JCwbCF2JDfi03XZ-Y02so1-Z6z771cSwXZRHz9WcikMwC49QM81ljoUq59sdbdKaND40c3hI13XSMdKNmlE1yTzp2eU3-ItOATbXhE3qqUZeqJ-QKmpeb4v3siP03DkWfHKuZRgLismeVkxgB0lFa4xm8Rna5_w7xO90pAWAV4ZSJjukz-GGFQ7q_x-4JcTvoDPX3nYNbagsBziDm2B2s4q9H0Ae9KQBj9Ik5keNXk2RHc4q1Cbl1kU_5GW2kZooDZu06Ii4xR4NtcLaNlyky8tW9GZ3FxvlKir4sO_vQbnZQGpTtuIPmYSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u3lu2W17pe1Jxbk_geBMVDGbN-NYHj6BJyVx_R4zU2vzxye1gq7Nkd4Rwssbdkr7w88qiHBRAGvW1mPFmpy8vthJWEA7xt9dZjEWuwPBjBa8xj7XSZhArqbBCK3uomQbsirfJTagVIWR1j1dWmwRjg3582H8trA5_YXCclXOMn691zHy-raWoc34LQN9Eq3cSSOPRgD9nb3drHNTDpdpfIq181j6tNDIRTXuasaoewjppKoUyWS83EggwtbC4IbOeWHKlSZkqd_wi8rWu_cMh2XyQ0crRtsMdnQ6BI3bIzl2CVgUq-WIpRSN-UirO1iN9XFu5j47kXsSnoyGnn68JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nOcPlSSmXgbp4CWFLNM4DETWcGZc-kjOePiS6ZBlk4FaeUHCFYk1l6SYFhWOfgwWmHaNux_qJa1jw-EUOjx9NHWedTKYyY9AziyWZGJ1_86QfR5ewy8DYlt1Tw80kBRP2YqWGV8dQTFhXTVSLdKauGfo0IyfxWucQRWOq5tdVwFqZco4t_GPWI4EtuoCNBzVNUO4oyhNJp-aLS9TIXSpUDkr0eml-wnEyldjRK4aLEj-ScwlE7SSHVzZnii66rPrdOL8CXf1VFaGcNnhPCwMuWuxDzO5NpryZXKPAafbdhDI7uTR9aSVDqq-SUFWJv4pKbDOBtC4odCH-Q_ePB_DSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hevbeEX1YZTP3j82lDM96An7BeaMuaLLJQNk9a2uG884IA7dXxNCjUYX3J2B4F3DpAJh8NFgVWjWEsIkBzwYJbZ0mP99zrhgs027FLjMc2dc5sjO0E0ePLhMCX_zAzdS7uqG91Bg9XJPgqVVgBlfn1GYOAfiRFLzvUH0Bf-v0bDre6wrl6z3rpGB42x1Tqw4bbfnMGj0oIrsPBXvCleLFqdr4oJhAXS80FDJA2NtUJMMYCokPkuSozppttRY2yrA04EZ2sADZx3skMOBsP_Is9n1np1MFvPqe6Q77BtKavUN6bj4omq1s5uPwiqTnJYWmzFvUkAyfVTNvUNb8XHVNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mACGXYAP6a-_Erf9Rz7NLt4DmX-9J8H2AXsWlPfqtLir669hIKDLY-hRrpLVNs6lxHzd1pglhGlvjbPl7HQTtDzi6TXd1wqr7yErG_0qbGzk-0jTLp6zTPOCdAvf9lcnaMNh7wrwZGzsi_Yc30nq12Gnk84KtZ0l5gLRoRNcaNJVRqigLw3Tp6L3UjJ45pOc5mifUBpSTY8xjQX2W7Vn-Hmg2Ii3OZY5Pcw2_d6qMAAUcor8WHgKkkpNdEWSzn0cZpWxoQ9Te3jfScTj_WnioqqGjcP-HinkGPS7rVzjObxUETAZa3DJOdKn7AH-mOHxM1oQAXWkNbVKQ6l_RLQrRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🥀
عکس
#پروفایل
ویژه محرم
#محرم
#امام_حسین
(ع)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/660243" target="_blank">📅 23:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660242">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1457e1cd8.mp4?token=pLCBocoIYv4rzmo3DiEm4pCZr_PB1I40MpwjLCpY_Em8-AnaTtVZ9QBPcR_qy_WVAITANCi1UEsN0o4ciCZGfdkAkjYkI8YJG6JCtepj-FJsX0JivvS7vVyIEggTXq818I2qjJt_Q5uwu2RZgh7hI_vAGzGWzu0LQxjL8WDWgm-Z_2YmhlAwWk4QeWi110apTMW-vXjt2SI-_b4IHmkg7ICF4EMJoAf4ED8pYpN2SlYTh08Ke5akCbDd0O6roHavD0dfqXLRvvr3jsWRx9o5_anVaDNZkQDGJUqvjemulpDRWTMcaNxFCHQsHTnGWQcISH3NzvWqwN7JI3BHsrBy57GWsqhG-pMZMimNDdA0UkrTYU1V9IDDOCbGsKMD1vL2KJUzJLy_5ANiIGtJfooAAwCZMXawsbDEd1YLFIVeBRVRCkQTatqKOy-HclmQhHu66w8dMBncyo25KDXGMvDO0kiS_4XxrgPyG8yCaejU-ipuk2KpvW4xImwUvWIoytQaSICIE710YEA-m_jt3LmvCGLmmCJrcoIkj4ikSm_J82j5XECQh4zok7db64kTYy5e2KszJfyYfweq6zY47DCLjooysqbuthY2gOhiIio4d5JssBAvlXCQXddvmnOHzgo7OSnMdvAT-k3MDgyrGdc5wFnr1wjrc7i6OH_b2IvJVAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1457e1cd8.mp4?token=pLCBocoIYv4rzmo3DiEm4pCZr_PB1I40MpwjLCpY_Em8-AnaTtVZ9QBPcR_qy_WVAITANCi1UEsN0o4ciCZGfdkAkjYkI8YJG6JCtepj-FJsX0JivvS7vVyIEggTXq818I2qjJt_Q5uwu2RZgh7hI_vAGzGWzu0LQxjL8WDWgm-Z_2YmhlAwWk4QeWi110apTMW-vXjt2SI-_b4IHmkg7ICF4EMJoAf4ED8pYpN2SlYTh08Ke5akCbDd0O6roHavD0dfqXLRvvr3jsWRx9o5_anVaDNZkQDGJUqvjemulpDRWTMcaNxFCHQsHTnGWQcISH3NzvWqwN7JI3BHsrBy57GWsqhG-pMZMimNDdA0UkrTYU1V9IDDOCbGsKMD1vL2KJUzJLy_5ANiIGtJfooAAwCZMXawsbDEd1YLFIVeBRVRCkQTatqKOy-HclmQhHu66w8dMBncyo25KDXGMvDO0kiS_4XxrgPyG8yCaejU-ipuk2KpvW4xImwUvWIoytQaSICIE710YEA-m_jt3LmvCGLmmCJrcoIkj4ikSm_J82j5XECQh4zok7db64kTYy5e2KszJfyYfweq6zY47DCLjooysqbuthY2gOhiIio4d5JssBAvlXCQXddvmnOHzgo7OSnMdvAT-k3MDgyrGdc5wFnr1wjrc7i6OH_b2IvJVAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نوجوان عراقی که در ایام جنگ دوچرخه خود را برای کمک به ایران فروخته بود، از امام رضا (ع) دوچرخه هدیه گرفت.
صحبت های شیرین نوجوان عراقی در حسینیه معلی شبکه سه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/660242" target="_blank">📅 23:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660241">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
نائب‌رئیس مجلس لبنان: بیروت در قطع روابط با تهران اشتباه کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/660241" target="_blank">📅 23:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660239">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fh0XmyXse8CpYiMVtZHlN6p4BgztvPpXy_IARf2Rkv_117cBm-gVVzsBe9L5ybJOyFI5GH2y1xnETUJb_J4M9tTEeXswrO_KbF4T-6ARUGWdzczxeyuapotYBcb1ZWohhUD1bOuRA8djw_3HW2N8H1klJM1SOLs3Axf7N_t9pnzsDSJpb0V_mSDMdj7WDtZrZJHc9uMq1POvMZ-gMsOSUWVY8Gj1ElO65cIG0OX5S3aFBg2eP64dulvk035ysg5NR_OxQZL5ubQiB0FD-v675MVX4lhmA7qblvXz6QAuiWIPZm_utfWlANFGqLbn0-PLWRNHe4fYdxbRQ_2Wldhl1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W2_L4yhpYtdvZUblZsqkA3dXRn5Uaw8tfRRUGB4IwKRvPm2HamGwbgNZoWWOjb59BpoeEgbljNxNwptcxFT24DaJfRvcRUc-pFFblTwu1nNwzlyVwCw5FAT3DIZOAFP0p5HVquVnMcYFypcvVUsbjfCgGKGhydGCWeMaoxz4yoY4AxcOJSXLnKqGOBGC28bjzT0nu5h90wvTBRGwD6t4s7kxTlXzeHRpmUXZBDyQpiCfIe4xGnfNZqlPwzWfREk3tP5pqwcwqmdH5mvwLj5kSJDuRDXsLlvzkczaeeIztm0JnV9Jv3WwVt0YtDJUqP53jt-dmN0AFDmOwFcSTbsR4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ترامپ: رهبران ایران باهوش و عقلانی هستند
🔹
رئیس‌جمهور آمریکا در دیدار با امیر قطر در حاشیه نشست گروه هفت در فرانسه، رهبران ایران را باهوش و عقلانی خواند اما بار دیگر ادعاهای قبلی خود درباره ایران را تکرار کرد. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/660239" target="_blank">📅 23:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660238">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce0812858.mp4?token=g3pSa6ubzUCYz7lHcWR-Jh2N3AEgKg1IF0dV2cpzZq9cOuyh-O-wdPKqI6nZ6Fy4jRA1XmmnkmY4KHe6hJQGZqkeNkGBmUMBXkNclR2c6NezLGklurx2T-Yf5Oq1taA4yF5SGlCYhrZSPGNwOdHEsIc63j0ZeRh_2ezmh9SowRlEUMDa0rkc9gNHuZ5WnGBGFBztcfERuRSjtJ4AFQI31i_XPnIP4YWOV4Ga2K3W5b2wBLJUYZDym0sa9StykO1mRSxcOSkU1qx3wDDllbFzWhZOwxcnF3RQ-Q5AqghFX-8wLhhmzPE5WDBWGMKJ4rlwbyQbLtmCX5p8j8qxbs_2xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce0812858.mp4?token=g3pSa6ubzUCYz7lHcWR-Jh2N3AEgKg1IF0dV2cpzZq9cOuyh-O-wdPKqI6nZ6Fy4jRA1XmmnkmY4KHe6hJQGZqkeNkGBmUMBXkNclR2c6NezLGklurx2T-Yf5Oq1taA4yF5SGlCYhrZSPGNwOdHEsIc63j0ZeRh_2ezmh9SowRlEUMDa0rkc9gNHuZ5WnGBGFBztcfERuRSjtJ4AFQI31i_XPnIP4YWOV4Ga2K3W5b2wBLJUYZDym0sa9StykO1mRSxcOSkU1qx3wDDllbFzWhZOwxcnF3RQ-Q5AqghFX-8wLhhmzPE5WDBWGMKJ4rlwbyQbLtmCX5p8j8qxbs_2xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در اربیل عراق
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/660238" target="_blank">📅 23:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660237">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
رسانه اسرائیلی: واشنگتن امتیازات بی‌سابقه‌ای به تهران پیشنهاد داده است
🔹
بر اساس ادعای کانال ۱۵ اسرائیل، نسخه‌ای از تفاهمات در حال شکل‌گیری میان ایران و آمریکا از رفع کامل تحریم‌ها، خروج نیروهای آمریکایی از منطقه و سرمایه‌گذاری ۳۰۰ میلیارد دلاری در ایران حکایت دارد؛ ادعایی که تاکنون به‌طور رسمی تأیید نشده است./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/660237" target="_blank">📅 23:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660236">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78daa50780.mp4?token=FT1eXG7OogsmSgGTlKcZ22DOXFOVlUlEwIlocWKGqMz2JIXxlRfD5Oz3elYrWDs1Snn07sDJ46V2kvYToUVlSOmpEE1jpGf5nh-Bjx0kWmMMIoZSiIHgkQ53hHHZ-JpwifS4skpphIDI3nCVggWlTqCV8OxvX7ZeeS948FcoDSUNsuYtjBoHu3OG77WNM8OXgz9DJiqg2oFWLPVuNF4sOFD0K5jtsGatyTInsiETW4nE7iGR44LooPLlVEUU9nDKu5XNs3anDr-JGPalP4K5VkRNoWaRekwwi462l2oIf0WKOR3uahszCXxqTe0P4Erx1n4m4BZGK1bP6erXDC13PREmaxbofrrCrMFyH96C2P2e84ih8wuMz6gr70ufMh-Ny-T8NFOHC4tajDDRTuLGbuP-P_h_eVfr825x7GWLYGWO9Ti1U2ZqyJSFPPZfM23AVROOnA6axFQKTeG9d_G1gKNxrFiApuxXBTsVGxgBpWbicuwPJru8lpFYk2K7SKkMPHuzVxaVYZwLwk7xifwCD0G6AltwQOoYqG8lXW6Lhyc-XYWzju1daPG1LTCbOIhbICh8LG_FqlvqTBr4Q7x4V2yscEfTrgvMoM4wOi08hnflhmNlEl4lJ7SbveNqeTQ_WIAw74v6_3GOVPnzvXurUL9ZUhQEjBAdbvy4Qbsn2Z8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78daa50780.mp4?token=FT1eXG7OogsmSgGTlKcZ22DOXFOVlUlEwIlocWKGqMz2JIXxlRfD5Oz3elYrWDs1Snn07sDJ46V2kvYToUVlSOmpEE1jpGf5nh-Bjx0kWmMMIoZSiIHgkQ53hHHZ-JpwifS4skpphIDI3nCVggWlTqCV8OxvX7ZeeS948FcoDSUNsuYtjBoHu3OG77WNM8OXgz9DJiqg2oFWLPVuNF4sOFD0K5jtsGatyTInsiETW4nE7iGR44LooPLlVEUU9nDKu5XNs3anDr-JGPalP4K5VkRNoWaRekwwi462l2oIf0WKOR3uahszCXxqTe0P4Erx1n4m4BZGK1bP6erXDC13PREmaxbofrrCrMFyH96C2P2e84ih8wuMz6gr70ufMh-Ny-T8NFOHC4tajDDRTuLGbuP-P_h_eVfr825x7GWLYGWO9Ti1U2ZqyJSFPPZfM23AVROOnA6axFQKTeG9d_G1gKNxrFiApuxXBTsVGxgBpWbicuwPJru8lpFYk2K7SKkMPHuzVxaVYZwLwk7xifwCD0G6AltwQOoYqG8lXW6Lhyc-XYWzju1daPG1LTCbOIhbICh8LG_FqlvqTBr4Q7x4V2yscEfTrgvMoM4wOi08hnflhmNlEl4lJ7SbveNqeTQ_WIAw74v6_3GOVPnzvXurUL9ZUhQEjBAdbvy4Qbsn2Z8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارت قرمز به کودک‌کشان
🔹
برای کودکان بی‌گناه ایران، غزه و لبنان؛
برای آن‌هایی که پیش از آنکه فرصت رشد، بازی و رؤیاپردازی پیدا کنند، زیر بمب‌ها و موشک‌های آمریکا و رژیم صهیونیستی جان باختند.
🔹
زمین فوتبال برای رؤیاهای کودکان ساخته شده است،
🔹
نه برای کسانی که کودکان را به هدف جنگ‌های خود تبدیل می‌کنند.
کودکی را نمی‌توان با موشک خاموش کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/660236" target="_blank">📅 23:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660235">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در اربیل عراق
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/660235" target="_blank">📅 22:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660234">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
کانال ۱۳ اسرائیل: ترامپ مانع اجرای یک عملیات نظامی برنامه‌ریزی‌شده اسرائیل در غزه شد
🔹
این طرح در بالاترین سطوح سیاسی و امنیتی اسرائیل بررسی شده بود، اما پس از ارائه جزئیات به آمریکا، واشنگتن با آن مخالفت کرده و خواستار عدم اجرای آن در شرایط فعلی شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/660234" target="_blank">📅 22:55 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

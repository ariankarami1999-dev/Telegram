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
<img src="https://cdn4.telesco.pe/file/R-Gx3Mz_-1VjddNgHpdHQYlLi50S90lyzFtJoT9VcsHiidNeojEi7Kja1faHJacZt63hd-dLI-JnWxoG2Q9lTETruhOCxHMEKzyF7WpPHgpU9gQNbSy2FcxtsaYvRRc2xFyojbHkHZLZvJ25l92iYaPrVoBD981nMoYXhtDPmOLXkDX1DzZrbNV9iiK9sosTd5rv2VMSSOk1hkwOhvQdhRg_qE1qQBtKaLXmV0UKeWUeCqrNnVz348Nge5nco1Ait1EdAR4a_LtYvJ5mFyufSUfl8V5iwUIpSgE_BpKAtG3bHyV7Le6IggbrTHNLlKFBVB1XUdr3GBUBp86EMUhAfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 926K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 18:41:02</div>
<hr>

<div class="tg-post" id="msg-131092">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
امارات ممنوعیت سفر شهروندانش به لبنان را لغو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/alonews/131092" target="_blank">📅 18:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131091">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d5133c623.mp4?token=fmuhda9nlGoAqKAt3f8_utKj-6RmZuoTaPx-_Cq6EZybAD86lu4d2Km5v4x_BSsxGDwhTurMt29dpwaNnVzR6CC5OvjY6_4mhI-Xq84mmvVIOS9yXQNaBKl-6neMOhdEto6voeQHO_aTZRL78Hbavo7K5ZYbRrl9QQ9gduAuBPdf4M95wBMPKkwcOXPUCBJQ9dxOPt2D5zQK_Mobi96_Wup7lwOUge4jpIs3Q925U-RaV9gBDg7v6UPNfbDoj5EyYBAB9wh0CjCdpdEpIdu6gFclBh4kt6lO43xlVJiZRC9bu-6_YGfFU3XX98yMxyfa8r0BzZ0Yf-7N8oKsdo42Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d5133c623.mp4?token=fmuhda9nlGoAqKAt3f8_utKj-6RmZuoTaPx-_Cq6EZybAD86lu4d2Km5v4x_BSsxGDwhTurMt29dpwaNnVzR6CC5OvjY6_4mhI-Xq84mmvVIOS9yXQNaBKl-6neMOhdEto6voeQHO_aTZRL78Hbavo7K5ZYbRrl9QQ9gduAuBPdf4M95wBMPKkwcOXPUCBJQ9dxOPt2D5zQK_Mobi96_Wup7lwOUge4jpIs3Q925U-RaV9gBDg7v6UPNfbDoj5EyYBAB9wh0CjCdpdEpIdu6gFclBh4kt6lO43xlVJiZRC9bu-6_YGfFU3XX98yMxyfa8r0BzZ0Yf-7N8oKsdo42Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک خودرو در شهر حیفا با صدای انفجاری بسیار قدرتمند منفجر شد که موج آن در سراسر منطقه «کریوت» احساس گردید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/alonews/131091" target="_blank">📅 18:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131090">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVfZVvXm9Pgu_5nVkVCzyrPrh-KEpPt0tz2-octraEU_eD0ybhl9SxKVQ3pmHhjhphgXjgZZsdtgJHO0q5m69QC2hR0HTHXk0Id5hr9wWZlujXjUmXQ8TvvHPHawjH9C4BEaowOMJ4hlo1L9zRFk19uhN7A2puczgmlSObXmt9YFWjnVVyHGjqji2j15OoCl3FdNYK4oSsCb1J83eydl5wF_UlJw7D7fPfFybs2wUeJuusD1zr-PgfkDpTnQCpXSQ_gu1ySv9zYPkuterNYTTXZ6QsCP516owJYpPz0ntb5yZDpRUbxqX1Wi6FQCcOSnEhNDnjQKLlkdtxjvpSYNpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال:
"پیروزی بزرگ: دیوان عالی ایالات متحده همین حالا علیه حضور مردان در ورزش زنان رای داد و این رای، آن وضعیت مضحک را کلاً منتفی میکند."
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/alonews/131090" target="_blank">📅 18:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131089">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
نیویورک‌تایمز: ایران و عمان، علی‌رغم مخالفت آمریکا، در حال پیشبرد طرحی برای وضع کارمزد خدماتی برای کشتی‌های عبوری از تنگه هرمز هستند
🔴
عمان این طرح را رسماً به واشنگتن و سایر متحدان غربی ارائه کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/alonews/131089" target="_blank">📅 18:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131088">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f02b732e9.mp4?token=oI7XWnYNUEEC6wu2yrxK61SVIVUMg_g-43OrjTMLNgNpXpqX792QLsa3mxbpfjF_dP1mgDKTn7e-k9zuBOX7k1xevrV1uRXjWQoab-zqWo2AreBsuwAgjMJCxdIQCFqthJjCZN7Or97uwhU8wOcN7UE3gBhJa7G2SSapwP2W6Q6FSgjSYXgavSZ2COECJVZsPPxhl87FyOD_9g-lawS6ksrzRHjgDVQ7_LZKVZJCGz0Wo2TBfZDiSvgG2WsrnaST6fOyd_78QN892bacJwv43HjCwIfMYKBaSElUcH8-Wai68DHy13OpmW7lMljN5ekCNVom_VEQQG8ecfRHap2ed4eyBA8ub1RkRHhdXTzZWB_Ldbnk1Kkhp6rd_rLpF9MLQQqd7HY6_1HpSiGhngHfZAPrTNyf1hsjQ_8az66-lRc1oPeDQdLEByMz-QBMIOCWzSH3oTtpMSRa13wWd6ElZMSjTER-vEGhhEGzM_B9KkwraFFRmgGUiN_rN-K5kVJvJ53WDh2JrfBZ4l79dX7yC_rj9ribgoIg3kin5_WreV7EOW80-Ry9NWh_DhqDO1vSIR8KGnmOY5ZiRpmPU3uKDBq3v8J0v4NFnZp_Z0bjPdkXTXZl8zET8rlPb4PdxZGFqt2L4YKBFuEhwSw7HL55CA5vi7yBJ5Rl-UQ6oRFOBWM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f02b732e9.mp4?token=oI7XWnYNUEEC6wu2yrxK61SVIVUMg_g-43OrjTMLNgNpXpqX792QLsa3mxbpfjF_dP1mgDKTn7e-k9zuBOX7k1xevrV1uRXjWQoab-zqWo2AreBsuwAgjMJCxdIQCFqthJjCZN7Or97uwhU8wOcN7UE3gBhJa7G2SSapwP2W6Q6FSgjSYXgavSZ2COECJVZsPPxhl87FyOD_9g-lawS6ksrzRHjgDVQ7_LZKVZJCGz0Wo2TBfZDiSvgG2WsrnaST6fOyd_78QN892bacJwv43HjCwIfMYKBaSElUcH8-Wai68DHy13OpmW7lMljN5ekCNVom_VEQQG8ecfRHap2ed4eyBA8ub1RkRHhdXTzZWB_Ldbnk1Kkhp6rd_rLpF9MLQQqd7HY6_1HpSiGhngHfZAPrTNyf1hsjQ_8az66-lRc1oPeDQdLEByMz-QBMIOCWzSH3oTtpMSRa13wWd6ElZMSjTER-vEGhhEGzM_B9KkwraFFRmgGUiN_rN-K5kVJvJ53WDh2JrfBZ4l79dX7yC_rj9ribgoIg3kin5_WreV7EOW80-Ry9NWh_DhqDO1vSIR8KGnmOY5ZiRpmPU3uKDBq3v8J0v4NFnZp_Z0bjPdkXTXZl8zET8rlPb4PdxZGFqt2L4YKBFuEhwSw7HL55CA5vi7yBJ5Rl-UQ6oRFOBWM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوباما در مورد ایران
:
ما تمایل داریم فراموش کنیم که هر جنگی - بار آن بر دوش مردم عادی است، مردمی که فقط سعی در زندگی کردن و مراقبت از خانواده‌هایشان دارند.
و بنابراین اگر بتوانیم از جنگیدن در منطقه جلوگیری کنیم، این برای مردمی که آنجا زندگی می‌کنند خوب است.
اگر تنگه هرمز دوباره باز شود، امیدوارم که به مرور زمان این موضوع به مردم عادی کمی تسکین از قیمت‌های بالای بنزین و قیمت‌های انرژی بدهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/131088" target="_blank">📅 18:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131087">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18bdf673ab.mp4?token=c_HZfUP0zJqKU1s35bMg0JTNA7D83Ek7O0hmrQhqSTOQRdy9YI-Z1hafABnQffeIomtSUAxYUcthz_2Fc8ElQbduOVegrhpiYA617jex1Oc6xStob9g8F3qsG5c6w1iOLexnyzKo5pCtyyLoRFgR1IrMA6MfnRZyM7HuxTylH-en4AHwPOHR7mSp8I6n-hue7uAQAxhXeYBbL1IkjWY3ubjfUBkMyMFfahvJyBwLR_7vPUtQvF6088d4zx09xR2QhTSZ2aF1aG1qFReu5PUZ7TATG_0Mhzi0hgHTbZl441CXVENgT20kv7_9jw1V8FVONkRkBS4Vek2zamoQiHzf-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18bdf673ab.mp4?token=c_HZfUP0zJqKU1s35bMg0JTNA7D83Ek7O0hmrQhqSTOQRdy9YI-Z1hafABnQffeIomtSUAxYUcthz_2Fc8ElQbduOVegrhpiYA617jex1Oc6xStob9g8F3qsG5c6w1iOLexnyzKo5pCtyyLoRFgR1IrMA6MfnRZyM7HuxTylH-en4AHwPOHR7mSp8I6n-hue7uAQAxhXeYBbL1IkjWY3ubjfUBkMyMFfahvJyBwLR_7vPUtQvF6088d4zx09xR2QhTSZ2aF1aG1qFReu5PUZ7TATG_0Mhzi0hgHTbZl441CXVENgT20kv7_9jw1V8FVONkRkBS4Vek2zamoQiHzf-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
در طول درگیری ایران، اقتصاد آمریکا به پیشرفت خود ادامه داد. اقتصاد بسیار قوی بوده است.
ما حدود ۱۷۰٬۰۰۰ شغل در ماه ایجاد کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/131087" target="_blank">📅 18:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131086">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44dac01f78.mp4?token=J3P6kk8eTZOwyLMKO51YgLxrV6Oq-TOWdSWepwyBASIGMl5UWohvelqwcb0Lr17QlgQStGEE-Ox0IElqP-af3NTf-j5GRlid99WYit6xfc0IL8PeBchhWRO6_ANk8pO0g45yesMQCY1M7dCU6WdailVJkpHg8Wp947Z88UzMiUt0ut4bJ10ZZeaxetX5YZm2RyFsc5_FXq5Eu1phE3PMaPfdvnJxXtVsGHvI2-kxBZIa0yR9v166NbsFuQzDgCcmjSnzAZzUsQkom_RcEakiad7xAnXHMGNeJdb10OFDCSwvKhzgy6X8VF_49JxpLHACtrM8xhDV9FgXa5cj791Ofg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44dac01f78.mp4?token=J3P6kk8eTZOwyLMKO51YgLxrV6Oq-TOWdSWepwyBASIGMl5UWohvelqwcb0Lr17QlgQStGEE-Ox0IElqP-af3NTf-j5GRlid99WYit6xfc0IL8PeBchhWRO6_ANk8pO0g45yesMQCY1M7dCU6WdailVJkpHg8Wp947Z88UzMiUt0ut4bJ10ZZeaxetX5YZm2RyFsc5_FXq5Eu1phE3PMaPfdvnJxXtVsGHvI2-kxBZIa0yR9v166NbsFuQzDgCcmjSnzAZzUsQkom_RcEakiad7xAnXHMGNeJdb10OFDCSwvKhzgy6X8VF_49JxpLHACtrM8xhDV9FgXa5cj791Ofg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی:باید طی روزهای آینده روند جاری را ارزیابی بکنیم و بر اساس آن تصمیم بگیریم که به چه شکلی و در چه زمانی مذاکره برای توافق نهایی را شروع بکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/131086" target="_blank">📅 17:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131085">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
العربیه: ایران تا پایان هفته 3 میلیارد دلار از دارایی‌های مسدود شده خود را دریافت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/131085" target="_blank">📅 17:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131084">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fi2HnI7MxQke_uFNlYZjO2e1LTO9_b46QdZUZ_cUjwixbG8lbRPsWk3eto1bRIgB64rGVxBo9FCE9ZBEAE71Tq4THnS2FH-9XmUkwGR0f8pdx42LUqQI7WI88yyv54yZIkgupPRWCpj1iSeUF5CokPqjlRDJhTwpVYHjVaT36BVmN64ll7BXqox11i-M47vIC2jUkB73af8F02J4GIjVYPWrUf8KJNM02ct3NHWBlwT7ilZa4rQ7MctTTIk5FJrMbdlBRIPuWJgIb3w3RYKstTRRKMSV25EWaDGqjM0-dm9hsC-daLIe0NZg3y7lSAjHx2dYd8G7h9Y1xoGfTM5qFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: مجلس رو باز کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/131084" target="_blank">📅 17:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131083">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-3ZW_8LdSzYqvnxUO3tETLph09Z7dfeywzFof9C0sHaQTQtnZrIHXZxO4GLI8SJBcGR6L_0HFXZYCNRcumWV5ripdDlyUkv3JsDqPh5uuHSH_6sqt2LYtJoBMRVXVDAdVUwTSZY7AX2vlPKdrHIp1QptEHwBfcRbxZVu3Dh12muikYQLfBi361mYYYF2RsiNZ4hBt9iRfHGgqKvaheR6xnhv27-LB8-Ps94Rzd4T4tYyH9YBeV9mb90Ls2ZAr2ixH2bBh43oP3xczv0437C41hv9PBxvgsIlQtxlyYZBp_CclJOl_zOo2MKrc3PtQQ9d9X3ACZmACdm-ID2lU9oEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: با وجود معافیت تحریمی کشوری جز چین نفت ایران را نمی خرد و از بازگشت تحریم های ما می ترسند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/131083" target="_blank">📅 17:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131082">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6KdplXqAbvKIMC2qvcrITUkt1wNk4cqbqv176AJl9B1R_fkfuSvhe-ubBOXjgDaZOmK72S6U7fRIZIxQFzBMxYemxCVaxbZRm8-akXfmkO7M838h939pFR_SBvKJJmRkSowNNtsLaS43Uj83m1SqH8NVUOJx4mrQMeLdF5tjffMLIBSN_bX5vxTuJMuqbie03cIQJwcE2m6wzjXZSVu47SeGB4A1AhiMb30yv2UlwlIZc3cqDCtVOlnIvIv538HRfNenDTYj1wBMLs4w9aEtSeJKCfLjlNzhPbsYV_XUTYgtj2qNw4hAeBkPTF5_FtQcrizwsgkhjcWSZpRBOC9Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو مراسم قرعه کشی جام جهانی هر مربی تیم بزرگی با قلعه نویی عکس گرفته تیمش حذف شده (هلند و آلمان) حالا مونده دوتا تیم دیگه که آرژانتین و اسپانیا هستن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/131082" target="_blank">📅 17:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131081">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00e51d5a7c.mp4?token=H3M163WwsQa6EBYyMh2QSim1tAaqDiYFGb7QmMh3v2pYZKNTZSo69DcQz5tyQP6MpqscmsHBniwj8rSQ7nvCITqIWYR-eZBZvIAaanhPdEwFeVzw07V-eP188KUTbmKqRS665sp1PGsc9S6NWAWysj8auH-BlQD32mFxHsaziECaYC3nbTZfumyzqFb58zSQ9RE0Ri_33H9e0Qt42Rz7NlesXmJU9yCyqZ3oCmqcfxARXP0j7BjaEGfXZPW3XjKDlDRwGvqt4XCHx-SWF7dDPDEPy-byXSUXH5xYGaPntTdklKMGGdscIBEbOqvdKgrfLtdwRdkx7FKyxZAI-2ZVqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00e51d5a7c.mp4?token=H3M163WwsQa6EBYyMh2QSim1tAaqDiYFGb7QmMh3v2pYZKNTZSo69DcQz5tyQP6MpqscmsHBniwj8rSQ7nvCITqIWYR-eZBZvIAaanhPdEwFeVzw07V-eP188KUTbmKqRS665sp1PGsc9S6NWAWysj8auH-BlQD32mFxHsaziECaYC3nbTZfumyzqFb58zSQ9RE0Ri_33H9e0Qt42Rz7NlesXmJU9yCyqZ3oCmqcfxARXP0j7BjaEGfXZPW3XjKDlDRwGvqt4XCHx-SWF7dDPDEPy-byXSUXH5xYGaPntTdklKMGGdscIBEbOqvdKgrfLtdwRdkx7FKyxZAI-2ZVqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توهین زشت حسن آقامیری به شاه عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/131081" target="_blank">📅 16:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131080">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSNHXfAUsbwn4kxwUZ-omjug9G4ZSuGCtAz23wqoJRbaL9GbFVw2mbIYj7d6IKvpQtToFnU2Mq3D5psJ6NcAe6N3Qr3ilTcmUQca0guRIz5GZzKtdxUDYE0bRw_UP5RAg9Bz3TSq250cV-cLeVLqZD5oa9WCIzxcZYeO_XLk3XvAqxeQPuWAfd8a6JC7id2ze1ACcU4aeUPPywI3JCdhuxHwQMzPg1UQXv8fdXMIgkEOwzFDwEeRPI-1FtjXT6dFM9SYq1b_OeuAKr8mz6nvBR9D797NnV6t0IWtCkR1h91W3WU7oRV3QGYWmEiDucspPCfHWYzQA8e9Pyalu56Mig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تاچ: نتایج تیم ملی عالی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/131080" target="_blank">📅 16:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131079">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa861dd055.mp4?token=boDFwANOWIaUUIUk3RyaN_Ms5PAp_lqct95E8HzUVkfFPWaTuJUwlgc_wUCV5AMeEMh5KoemCREOQ0Y-GzwMb6HGktY6MCGiHZ7Pg-pmTNfGwlqbknnIHCW3iWRZLfQhLqLxpxyyF1B3365lSjovARdHV1yd9Nqyb4Otg88nu_c3lmCzX9eWkmC2vKcIieO6PSsEgiCTC14cq-6q6v4GqSGp9vlZrAKEyIPv0wXmIIkqWR6T7lPqjLz3QdPZJOccq2N7RebzRBUM7DadY8sg1SEP8o-zuS0HHQL7VkTJDzLyfarMLbr4vP4xV8PcwmVbgA3fiRhXogXdezeykFzPAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa861dd055.mp4?token=boDFwANOWIaUUIUk3RyaN_Ms5PAp_lqct95E8HzUVkfFPWaTuJUwlgc_wUCV5AMeEMh5KoemCREOQ0Y-GzwMb6HGktY6MCGiHZ7Pg-pmTNfGwlqbknnIHCW3iWRZLfQhLqLxpxyyF1B3365lSjovARdHV1yd9Nqyb4Otg88nu_c3lmCzX9eWkmC2vKcIieO6PSsEgiCTC14cq-6q6v4GqSGp9vlZrAKEyIPv0wXmIIkqWR6T7lPqjLz3QdPZJOccq2N7RebzRBUM7DadY8sg1SEP8o-zuS0HHQL7VkTJDzLyfarMLbr4vP4xV8PcwmVbgA3fiRhXogXdezeykFzPAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تمسخر کلمه دلیل؟ تجربه، آیت الله خامنه‌ای توسط مشاور قالیباف در آنتن زنده
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131079" target="_blank">📅 16:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131078">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
بقایی: مردم عراق برای حضور در مراسم وداع و تشییع پیکر رهبر شهید در کشورشان لحظه شماری می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/131078" target="_blank">📅 16:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131077">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚀
اگه واسه کانالت دنبال
ممبر، سین، ری‌اکشن اتوماتیک و حتی کامنت با هوش مصنوعی
می‌گردی ارزون‌ترین ربات
کلیکو
هستش
قیمت‌ها عالیه:
سین کایی ۵۰۰
ری‌اکشن کایی ۲۵۰۰
ممبر از کایی ۵۰.۰۰۰
⚡
تحویل سریع
💰
قیمت تضمینی
🤖
ثبت سفارش خودکار
👤
پشتیبانی 24 ساعته
لینک ربات
👇
👇
✅
@ClickooBot
🤖
✅
@ClickooBot
🤖</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/131077" target="_blank">📅 16:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131076">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
خبرگزاری تسنیم : روز دوشنبه بورس ایران تعطیل میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131076" target="_blank">📅 16:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131075">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c7de37440.mp4?token=rIH7qqm9EShI_jv7BZzPGXlHjoZHKZSVH59i8nOhjfw8ew8IACNAUtfMsTcDiQr1ieie4S5efRhj6ud3VxR8d4zFAnZMoFSMMTvqGkolq0FQflQpn784fVehtvywy8399ofUsb8nv4tl2iSpW5bfUMDxLNnDoIxqXcFa3nDBVp37g9fZnPQEGPy8sw42G8fP9hJpkaETk67poVrRLWMG3nNIro-D10MgwRRfSha8uo_uHEMxHlJCVOklaPkWSpW4dZ2t4DhRefJgnQZwF4kffS3WJQuWUPyfaBvrxwEwhNvSQE97aMMi_4CUw9Jbt1fNp_fktXRhq8jpXZUEHnqF8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c7de37440.mp4?token=rIH7qqm9EShI_jv7BZzPGXlHjoZHKZSVH59i8nOhjfw8ew8IACNAUtfMsTcDiQr1ieie4S5efRhj6ud3VxR8d4zFAnZMoFSMMTvqGkolq0FQflQpn784fVehtvywy8399ofUsb8nv4tl2iSpW5bfUMDxLNnDoIxqXcFa3nDBVp37g9fZnPQEGPy8sw42G8fP9hJpkaETk67poVrRLWMG3nNIro-D10MgwRRfSha8uo_uHEMxHlJCVOklaPkWSpW4dZ2t4DhRefJgnQZwF4kffS3WJQuWUPyfaBvrxwEwhNvSQE97aMMi_4CUw9Jbt1fNp_fktXRhq8jpXZUEHnqF8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای نظامی اوکراین امروز صبح مرکز ارتباطات ماهواره‌ای دوبنا در منطقه مسکو روسیه را هدف قرار دادند.
🔴
این سایت که بیش از ۵۰۰ کیلومتر از مرز اوکراین فاصله دارد، برای شناسایی و هماهنگی فعالیت‌های نیروهای روسیه در اوکراین استفاده می‌شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/131075" target="_blank">📅 16:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131074">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: آقای قالیباف به‌عنوان نمایندهٔ ویژهٔ ایران به چین سفر می‌کند و ترکیب هیئت همراه و جزئیات سفر به‌زودی اعلام خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/131074" target="_blank">📅 16:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131073">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا به فاکس نیوز: پس از رفع تحریم‌ها، هیچ‌کس به جز چین نفت ایران را نخریده است. ایرانی‌ها نتوانستند نفت خود را به دلیل ترس خریداران بفروشند
🔴
ایران تلاش می‌کند نفت را با قیمت‌های پایین‌تر بفروشد و سود آن اندک است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/131073" target="_blank">📅 16:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131072">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcd78855cd.mp4?token=po04wefwYZH53rIOGy-ZDQyIgLEtWCrl9Eo5UjgEHFDGgwrtUU2p10IzHQQwdOiuGpsr7gdc0XgkImuZ-6DET4yhiCuNQeRBXD6_LZVG86BjWPi1DIHNfcBkF6rgOnuHwyW_5NrILKeNd1_uVKpGtDX4jkOlxlL3-X5VTGMg0yoK8Y3HE_4IOJFWi6viXMD9i9CghtlIf4KxY0Ba47e_pHONxpCdJ9-6EXDTuWzF8JjXGRe6fPfvTa70bCmcIbNOCcOQbaat15VN2LRs5z_jz4qMdERk0BDNIarWbNAVahCIDfBr33sSkA_UWSx54fIiAR55ZdqbIdeEMJOPm6EoSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcd78855cd.mp4?token=po04wefwYZH53rIOGy-ZDQyIgLEtWCrl9Eo5UjgEHFDGgwrtUU2p10IzHQQwdOiuGpsr7gdc0XgkImuZ-6DET4yhiCuNQeRBXD6_LZVG86BjWPi1DIHNfcBkF6rgOnuHwyW_5NrILKeNd1_uVKpGtDX4jkOlxlL3-X5VTGMg0yoK8Y3HE_4IOJFWi6viXMD9i9CghtlIf4KxY0Ba47e_pHONxpCdJ9-6EXDTuWzF8JjXGRe6fPfvTa70bCmcIbNOCcOQbaat15VN2LRs5z_jz4qMdERk0BDNIarWbNAVahCIDfBr33sSkA_UWSx54fIiAR55ZdqbIdeEMJOPm6EoSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسماعیل بقایی: ما هیچ درخواست رسمی در خصوص بازگشایی سفارت کانادا دریافت نکرده‌ایم.
🔴
اگر درخواستی دریافت کنیم، آن را بررسی خواهیم کرد، اما تاکنون چیزی دریافت نکرده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/131072" target="_blank">📅 16:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131071">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3834c581a9.mp4?token=ExwlPpYgCnTl9x9zC4WwFU5yd_Um1XvnDZ2HZtojFWr-WLYj0bSqkq1MJQTpOAWAqIERXLv7uo6hazdsf26A-veLrbcEoEIEP3yPWvuwHTq9fx9YNVr12FnzQgjirxLgOYq1hFhr80J36DmviAGPIqU44fJWQ1d9RQr-TnOsaf49ER4A5YusjIpUEjiJLi7yMuKybuOUOuQSmxLumefnD4fU4Qgv-tBiUwMX83s9olx0li10RafM79344JB4abH26DXiP3_eiUHNXfuywqZeSSl-bmvXQEjwhtFuyOJ28WJLFgO042ibwZP3kxkE3hvYdEscfq8R_08HKOu_OMBe-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3834c581a9.mp4?token=ExwlPpYgCnTl9x9zC4WwFU5yd_Um1XvnDZ2HZtojFWr-WLYj0bSqkq1MJQTpOAWAqIERXLv7uo6hazdsf26A-veLrbcEoEIEP3yPWvuwHTq9fx9YNVr12FnzQgjirxLgOYq1hFhr80J36DmviAGPIqU44fJWQ1d9RQr-TnOsaf49ER4A5YusjIpUEjiJLi7yMuKybuOUOuQSmxLumefnD4fU4Qgv-tBiUwMX83s9olx0li10RafM79344JB4abH26DXiP3_eiUHNXfuywqZeSSl-bmvXQEjwhtFuyOJ28WJLFgO042ibwZP3kxkE3hvYdEscfq8R_08HKOu_OMBe-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسماعیل بقایی: رقص و جشن مقامات آمریکایی به خاطر عدم صعود ایران به مرحله بعدی جام جهانی، تمام استانداردها و هنجارهای پذیرفته شده میزبانی را نقض می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/131071" target="_blank">📅 16:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131070">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده ایران:
در رابطه با تنگه هرمز، تکلیف کاملاً روشن است. بند ۵ یادداشت تفاهم، مسئولیت جمهوری اسلامی ایران را به‌صراحت بیان کرده است.
🔴
بنابراین، روندی است که آغاز شده، تداوم خواهد داشت و قطعاً جمهوری اسلامی ایران به‌خوبی می‌تواند این روند را بدون نیاز به مداخله هر طرف دیگری انجام دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/131070" target="_blank">📅 16:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131069">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
قیمت کولر ۳ برابر شد !!
🔴
مهدی بستانچی، رئیس انجمن تولیدکنندگان سیستم‌های تهویه مطبوع ایران: کولر آبی ۷۰۰۰ از حدود ۴۰ تا ۴۵ میلیون تومان آغاز و در برخی مدل‌ها و برندها تا ۸۰ میلیون تومان نیز افزایش پیدا می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/131069" target="_blank">📅 16:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131065">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hr-Ua-BRznyvRzGTC6pZeaCzgYjvzwMqE0K-fhRXPnhbJrvlY7zYMNh015eV5OrgTiV1GTRy4yjeFZKYee8YSyWcSHHMLgUWZaUGlF2BY4eXzgkjV28vv60qzOWU8EbuM7qGc_NxLP4D-nGzq-YYqpXcZ1gZ-pbl_ru9W2B8u7BcZGPNRTdlHSuBrwoKGFJnyrz2C5FyMTzBTs2KGvZvfwwWebvADmPlc2T6yhhh_5jZQQ34kH8MXvehF3YV9aW04jo31vjd7N3wrm_5iUZJey7btl-__qvgrT3OVHYm0tNm6gm4G9yitFB1S5P7qBRJKbcpirSzHqaQXsDf-eeyDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fdmw6BvGTVQWRpsfBhTUR80Q6JQE_QPZUqRTrs3xng-UvuOtLr9yIlBbnHEYGGMb8X1wDi_AQOnU4_6zLsghLej0SgSKPMNcUSa99o38GSStKsb6_BtYoTxMWcaz4ZCKqtjqAB7HiDWaGWXavbrXf5NXZ7dK5InfHrDI6muKrUGg7aQ33YEJmFbkn2_QQFJMjJxRwn3SAdkHrPajT22fLGtPznQopb5ZItiAspwoiOwT2GnWwfZ6-zcpOHXsLnQ8bhadT7F1R3WjtnKQbJVtNfq7bSLDpjDd2Q7j050r2vtdhXuZpSaf7U_uYSIotoE_YzxETH3JtYBcD3P_0axMQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PwpHwHow7Jm28SEf0UaqcC_FGIj1ylSAWWDdW-x3a4KmhNdxZBatanv85wIcZA2gHnFQTCNlXYCKfY6SWFpTBspdz4WSy8WBXnq_PgnA4lFJjeiOxiO3LqWC2pdsRM3Za9hBHeSNpWXJGZ3OOBU2UPWtnZREw7PdhicOazdI5mWlbXGTEgpwmTF0A0MxY1VppUwMDhJhfax1PjPN6eF_9EUg9v6v96M3AOaS1iTeFZYzEEdjD-tZshGVYeBuTzDyPw6jTgrulDG9J_k_s8bYiYMcwWUu2Ld81WWPc6JrOs-hzZ0__eFcsRICXnjsdfOD2NoXUCR3OtMl6Uk_0oLiVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hcQWafCeKFDa__BZhld1fVg-2czsJPFQPgtr_Dsj9mc2BX6bjEqRlEPru8wmJiS0LxzG7FdkRjkxqSuyVlQTBBeOu57I55CTr1m8j3DbG_VKTxeolk-0yjj0lQNKcy14OjfODNbf1sYl4IDlWL5J1MdVX-8h7XxMj5BUffkPhbXP5yo9zYLZW1quWDkzB52ysLpiCisfwHX0tTr5YTsI7UQ8UTsGC8WRrBBPlDOEXH4jOxDuWnYI5y4b057qIg9yKcwIm4zgci5D_TwSG0PYPxUijF3KYRQE1TwNlu9jw8G_oAEgAtc7EA4QaORgQMKd4hcvtDXmDN6hJBF4RtK7hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
در ادامه دستگیری ها در عراق موقع بررسی پرونده معاون وزیر نفت این کشور، ۱۱ میلیون دلار و ۴ میلیارد دینار پول نقد تو خونشِ پیدا شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/131065" target="_blank">📅 16:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131064">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7907cf315e.mp4?token=HQrrD5JjVuAvE4mrZl01TNYkQPWZ15kKj0CUr0J3fhPgw72yTCn0iz-OrAjOz-7gduo8P12jyxW5MGCIIwsBtMA0k1pvGqhSDKOfocIbVq8XUB26MeTdhzrt9rwklPfr4SeWPDRKeF7H8wBxfxxhBzyD263mzkNjfz26_IsvXv6pYnhk0I5Q8pNb4PSZk6BBXWhH2NDPrc5HX8UcV1Fy0tE_C49-dXGZgYm7WF81If85DA70GRo9bPPNslwzPZ96zxIgsYutwNhbTmb1m2lTY0hQNhRxVqF6fgPyFc6kKd0s9pKNFglCLsSK26aFTMPir-Fq6flnFc-l4M9qVlzhlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7907cf315e.mp4?token=HQrrD5JjVuAvE4mrZl01TNYkQPWZ15kKj0CUr0J3fhPgw72yTCn0iz-OrAjOz-7gduo8P12jyxW5MGCIIwsBtMA0k1pvGqhSDKOfocIbVq8XUB26MeTdhzrt9rwklPfr4SeWPDRKeF7H8wBxfxxhBzyD263mzkNjfz26_IsvXv6pYnhk0I5Q8pNb4PSZk6BBXWhH2NDPrc5HX8UcV1Fy0tE_C49-dXGZgYm7WF81If85DA70GRo9bPPNslwzPZ96zxIgsYutwNhbTmb1m2lTY0hQNhRxVqF6fgPyFc6kKd0s9pKNFglCLsSK26aFTMPir-Fq6flnFc-l4M9qVlzhlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسماعیل بقایی: احتمالاً آنچه فردا در دوحه اتفاق می‌افتد، بحث درباره اجرای بندهای یادداشت تفاهم است، از جمله بندی که مربوط به آزادسازی دارایی‌های مسدود شده ایران با طرف‌های قطری می‌باشد.
🔴
بنابراین، تأکید می‌کنم که هیچ جلسه‌ای در هیچ سطحی با طرف آمریکایی برای چند روز آینده برنامه‌ریزی نشده است
🔴
تمام آمادگی‌های لازم انجام شده است و امیدواریم کار به‌درستی پیش برود و به نتیجه رضایت‌بخشی برسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/131064" target="_blank">📅 16:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131063">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEAiybIERrGGDp9eTF2oG8K8xLejZGfFbt8UkG7IZlEbBM_p1B_bRDG71WdOSif2cCeny5uj8dr5rclwq14QKQGj3dTIOLbltOD0jR9VIwZgsOzGzFWtJenWxX4GPUH4P-jbd7usSZP43KT8gET6GSCydxYjaCgpKXtbITFC3NXLJlpSsWhC4WN2GEQ-WRRBWFmRoBts8MVI-I6hkglqkAgBqrKa6ux4SKH5QX6Y41pV5J4-V3d60_4fUPD82awV5lkGDC6lUMQ6mZydCK2V6jXe76u9MiGThABSEe8DdirZegFJBQJookyULpWV_qFYWjRwZLO5iia5dndiYVEeMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع العربیه: ایران تا پایان هفته ۳ میلیارد دلار از دارایی‌های مسدود شده خود را دریافت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/131063" target="_blank">📅 15:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131062">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
بقایی وزارت امور خارجه ایران: خط ارتباط با واشینگتن میان این وزارتخانه و یکی از نهادهای سیاسی آمریکا است.
🔴
در روزهای آینده در مورد زمان و شکل شروع مذاکرات توافق نهایی تصمیم‌گیری خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/131062" target="_blank">📅 15:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131061">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a081ef12.mp4?token=BbyDh23ductZhPCSlIqBTEdFBvPflRFEfDUdYmV8oyXCTqzAsjzW_nYdLfsJBXUiVh9TK0ayXEcqiY5V9pQDEEm6mSC7cOUDTA83fyM10NwjejnL4EJYbGtbwQXXrdFpnyb6SG3rHpyDD3HDfcSt6rdyWAJqIx63yzTJCiEjUChQ0gZ-eecEQXYlJCTMsvLf00eeK1BG4vVK1rm1FdqTVzDAbOhp4W6wd8qX1RuoxwrNRx86QgUeN-lzKkLYJnvZVqa29cefct72ZaGNT8_5_7Rqt2_-1bG5jLj-yU6hJU1-FP7J180tmuLWxg7MLy_GdQH7zpP53mnV4NQrF-rnXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a081ef12.mp4?token=BbyDh23ductZhPCSlIqBTEdFBvPflRFEfDUdYmV8oyXCTqzAsjzW_nYdLfsJBXUiVh9TK0ayXEcqiY5V9pQDEEm6mSC7cOUDTA83fyM10NwjejnL4EJYbGtbwQXXrdFpnyb6SG3rHpyDD3HDfcSt6rdyWAJqIx63yzTJCiEjUChQ0gZ-eecEQXYlJCTMsvLf00eeK1BG4vVK1rm1FdqTVzDAbOhp4W6wd8qX1RuoxwrNRx86QgUeN-lzKkLYJnvZVqa29cefct72ZaGNT8_5_7Rqt2_-1bG5jLj-yU6hJU1-FP7J180tmuLWxg7MLy_GdQH7zpP53mnV4NQrF-rnXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: روند فروش نفت و محصولات نفتی ایران خیلی تسهیل شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/131061" target="_blank">📅 15:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131060">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
فوری/ منابع العربیه: مذاکرات غیرمستقیم فردا بین هیئت‌های آمریکایی و ایرانی در قطر با حضور میانجیگران برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131060" target="_blank">📅 15:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131059">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: جنگ با ایران ممکن است هر لحظه شروع بشود و ما برای آن آماده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131059" target="_blank">📅 15:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131058">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
بقایی: هیچ درخواست رسمی درخصوص بازگشایی سفارت کانادا دریافت نکرده‌ایم/ در صورت دریافت بررسی خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131058" target="_blank">📅 15:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131057">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده ایران:
در رابطه با مسئله لبنان، موضع ما روشن است
🔴
تعهد ایالات متحده آمریکا برای خاتمه دادن به جنگ در تمامی جبهه‌ها، از جمله جبهه لبنان، یک تعهد صریح و آشکار است که وفق بند اول یادداشت تفاهم بر آن تأکید شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/131057" target="_blank">📅 15:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131056">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: اساساً برنامه‌ای برای دیدار با آمریکایی‌ها در هیچ سطحی نداشته‌ایم که بخواهیم از آن منصرف بشویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/131056" target="_blank">📅 15:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131055">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی:
با قبول کردن آتش بس، به آمریکا فرصت تنفس دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/131055" target="_blank">📅 15:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131054">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f440c5937f.mp4?token=Iyx0EaejKVkVgo29DN0g_es6bQqT-JjcA-XAcBgAcDwiRYJbrPb_bF0sNzRIUTLE5R1Kbwiw34xJraZj-uEMKGgrXIm-rw9MKmV1MKQMCmXCBPEWT_TFIRGcWpJ0UveoJK4Asl8nuiTuGS370yJhDcuZ4PrI_6DoqzJDDZDrLqpi_K_WqOEtwRcchBQrBTqXKJ87vuwGBEKvP9iJjwPbUzJXHufUueCMri9bVtjMLlf42UQJ-lQMp-7cq_DsIZF3vZgJ9vkz6rKXUVbcIrL4jTpNjqNZs3EOmxRGFy2Do561Y54R4nvAu7vjv_oPLLTm86Sq34z3-MLYWibhilMFfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f440c5937f.mp4?token=Iyx0EaejKVkVgo29DN0g_es6bQqT-JjcA-XAcBgAcDwiRYJbrPb_bF0sNzRIUTLE5R1Kbwiw34xJraZj-uEMKGgrXIm-rw9MKmV1MKQMCmXCBPEWT_TFIRGcWpJ0UveoJK4Asl8nuiTuGS370yJhDcuZ4PrI_6DoqzJDDZDrLqpi_K_WqOEtwRcchBQrBTqXKJ87vuwGBEKvP9iJjwPbUzJXHufUueCMri9bVtjMLlf42UQJ-lQMp-7cq_DsIZF3vZgJ9vkz6rKXUVbcIrL4jTpNjqNZs3EOmxRGFy2Do561Y54R4nvAu7vjv_oPLLTm86Sq34z3-MLYWibhilMFfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برج ایفل ۱۰ سانتی‌متر بلندتر شد!
🔴
در گرمای شدید، سازه آهنی این برج به ازای هر ۱۰ درجه سانتیگراد افزایش دما، حدود ۲ سانتیمتر منبسط می‌شود. وقتی دما کاهش یابد، ارتفاع آن به حالت عادی بازمی‌گردد.
🔴
تابستان امسال برای این نماد مشهور پاریس روزهای سختی داشته؛ یک روز دمای هوا به ۴۰ درجه می‌رسد و روز دیگر صاعقه به آن برخورد می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/131054" target="_blank">📅 15:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131053">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سخنگوی وزارت خارجهٔ قطر: اموال مسدودشدهٔ ایران آزاد نشده و آزادی آن به پیشرفت مذاکرات ایران و آمریکا بستگی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/131053" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131052">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f60302362c.mp4?token=dUvo4BJKUOmp6wiUtW7xz8VTua4utxWjTpQ0i1bdaXqhL1cZR_9XWvuY1BcB9Lkg1Djty5IkaHb3diAs78zVslGc-QMa_U6QIV453wQpzgxl3wNPoXgovLzlUjJXU7JSz8VABXfdhiuH4PhGOv_b9BlhQyWIndGj3_cAhpLZwW-3ITAouHU0sb62ZjqaZv6p9wrd6CJqlUHNKPJopA1Wz-cPL7zyG-DwuRJ4M-wPTdrbBucEhhQGLSnjKMey9bB6oz3zW_MPhYG2uBCk2_5ELQS-9knftwzGs2SqLtqRnUYCpSfW3Ws1pyaF2ofWQs2ntjcXcfr77-OXyp4JTwp4WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f60302362c.mp4?token=dUvo4BJKUOmp6wiUtW7xz8VTua4utxWjTpQ0i1bdaXqhL1cZR_9XWvuY1BcB9Lkg1Djty5IkaHb3diAs78zVslGc-QMa_U6QIV453wQpzgxl3wNPoXgovLzlUjJXU7JSz8VABXfdhiuH4PhGOv_b9BlhQyWIndGj3_cAhpLZwW-3ITAouHU0sb62ZjqaZv6p9wrd6CJqlUHNKPJopA1Wz-cPL7zyG-DwuRJ4M-wPTdrbBucEhhQGLSnjKMey9bB6oz3zW_MPhYG2uBCk2_5ELQS-9knftwzGs2SqLtqRnUYCpSfW3Ws1pyaF2ofWQs2ntjcXcfr77-OXyp4JTwp4WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل یک تونل حماس به طول ۱۶ کیلومتر در غزه را با بیش از ۳۰,۰۰۰ متر مکعب بتن مسدود کرد.
🔴
این همان تونلی است که جسد اسرائیلی، سرهنگ هدار گلدین را به مدت بیش از ۱۰ سال در آن نگهداری می‌کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/131052" target="_blank">📅 14:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131051">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffe136f3fc.mp4?token=elzkc2T5HhqD0wNmtotrwG6od0W6ixJJdu3jBteC2s8_InIUO1_oYvf5Kl3LaKqNIeK8Kg4RgS5dQnQXcmddw7TiiJKPpKH0PaXblJX37U7-ePhfrtW7EJqgEcALPkSkdBNgJQ5ttE49xljFWU2CXtCkjVVMSh4-OmjO-6Dj4Ou8ho801ibDp-B48kcdLb7fuqU3n9ICYB2oMXA59au3uA2lhHtNh12XQ7tK-_I5RH92zDVvEhzM-UYBCHtYW2IndksevKDDmZBVDToXE_VED7OZLQiiJvyN0ki7gWaS_TMFRA0O61J_sojvHrPH76p2BpIluCWhb_Ia_qS6OERxvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffe136f3fc.mp4?token=elzkc2T5HhqD0wNmtotrwG6od0W6ixJJdu3jBteC2s8_InIUO1_oYvf5Kl3LaKqNIeK8Kg4RgS5dQnQXcmddw7TiiJKPpKH0PaXblJX37U7-ePhfrtW7EJqgEcALPkSkdBNgJQ5ttE49xljFWU2CXtCkjVVMSh4-OmjO-6Dj4Ou8ho801ibDp-B48kcdLb7fuqU3n9ICYB2oMXA59au3uA2lhHtNh12XQ7tK-_I5RH92zDVvEhzM-UYBCHtYW2IndksevKDDmZBVDToXE_VED7OZLQiiJvyN0ki7gWaS_TMFRA0O61J_sojvHrPH76p2BpIluCWhb_Ia_qS6OERxvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر بریتانیا کیر استارمر:
۶۴ میلیارد پوند برای نوسازی بازدارندگی هسته‌ای بریتانیا سرمایه‌گذاری خواهد شد.
🔴
این پول صرف ساخت زیردریایی‌های جدید، توسعه یک کلاهک جنگی مستقل جدید و خرید ۱۲ فروند جنگنده F-35A خواهد شد تا نقش ما در تضمین امنیت بریتانیا و اروپا حفظ شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131051" target="_blank">📅 14:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131050">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از سخنگوی وزارت امور خارجه قطر: اموال مسدودشده ایران مشمول توافق سال ۲۰۲۳ است و به‌طور مشخص برای خرید کالاهای بشردوستانه اختصاص داده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131050" target="_blank">📅 14:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131049">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه قطر ادعا کرد: جلسات فنی بین واشنگتن و تهران متوقف نشده است و میانجیگران برای تسهیل آنها تلاش می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131049" target="_blank">📅 14:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131048">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
وزیر ارشاد: دیدگاه‌های مطرح شده توسط مراجع عظام، علما و فضلای حوزه علمیه قم در دیدار با رئیس‌جمهور، نشان داد که بخش اصلی و تاثیرگذار نهاد دین از دیپلماسی عقلانی حمایت می‌کند
🔴
در دام تبلیغات جنجال‌سازان قرار نگیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131048" target="_blank">📅 14:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131047">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوری / سخنگوی وزارت خارجه قطر:  ایرانی ها از دیدار با تیم آمریکایی منصرف شدند. ویتکوف و کوشنر در دوحه حضور دارند اما با مقامات ایرانی دیدار نخواهند کرد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/131047" target="_blank">📅 14:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131046">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه قطر: ۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است
🔴
حاکمیت و سیاست جدید ایران در تنگه هرمز اعمال خواهد شد؛ چه با عمان، چه بدون عمان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131046" target="_blank">📅 13:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131045">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری / سخنگوی وزارت خارجه قطر:
ایرانی ها از دیدار با تیم آمریکایی منصرف شدند. ویتکوف و کوشنر در دوحه حضور دارند اما با مقامات ایرانی دیدار نخواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131045" target="_blank">📅 13:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131044">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7204ae52a8.mp4?token=o18pCHj8Y2_YbD667Uy1eKdtefxhU9RrqP8-TlQRi2wWo1jX2tM2TuuT3_Ls0g5l8z8U5H4M6RmAo9CcB4Hjwrg94hY5NA33YcpgF8Owo7jXEQmukyvms-RyRhxsmLuSvhG2GmW07itWUNWHSkQRxQVteCwSfw5lzCR0f95K7F62LtQKuxuEyHe_PDvX3X9oaQnAkBBsfZfaoBLzjw3mXXUSCZ99g24xBdW7pqcKwFK2gHKogmzT8OokXh_MMfAVKp0bEKBusswrILwN40lprRPbKBUsqE4NvhOvy8wVBCYyjOemXcg1DxgqWtaXd1SXkZJeIkOujk1lXriv1bS_BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7204ae52a8.mp4?token=o18pCHj8Y2_YbD667Uy1eKdtefxhU9RrqP8-TlQRi2wWo1jX2tM2TuuT3_Ls0g5l8z8U5H4M6RmAo9CcB4Hjwrg94hY5NA33YcpgF8Owo7jXEQmukyvms-RyRhxsmLuSvhG2GmW07itWUNWHSkQRxQVteCwSfw5lzCR0f95K7F62LtQKuxuEyHe_PDvX3X9oaQnAkBBsfZfaoBLzjw3mXXUSCZ99g24xBdW7pqcKwFK2gHKogmzT8OokXh_MMfAVKp0bEKBusswrILwN40lprRPbKBUsqE4NvhOvy8wVBCYyjOemXcg1DxgqWtaXd1SXkZJeIkOujk1lXriv1bS_BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایزدی : توافق ایران با ترامپ و کنگره آمریکا نیست توافق با نتانیاهو هست
🔴
باید ببینیم نتانیاهو متن رو می‌پذیره یا نه چون تصمیم‌گیری نهایی با اونه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131044" target="_blank">📅 13:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131043">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d66c8103ea.mp4?token=foMqiNxqRiu9AYhDFZ3xHcYNeWQyMobUDOXL9xDBG5SA1j2gMfXEq-ABk91SuDZeiO--1CvbDGDaMuGvNl4m5qvl6Yvym6dO8M-b1EanRLY6ByxItSrTBuj432KiEb6QcsnqTujvtdkd1QVepkwSNX-7lAL_HdBbtAXRQIWwFOniOasAi6Alhb_GEFgSHoNrkPqBPQUz4gqmIQFgCXOQcy33JowZFFzKP4EScV6ZKLHC8EUQ4my8u6AHZ4kb-28I9mIMQMDX3xcexVH_i3KpEj3NsVyw2hH7uM5rj1N-1TJ4pjPj5zgSmpEF0FN_rce9Pv4nT7LKHUd1TFOklXo-fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d66c8103ea.mp4?token=foMqiNxqRiu9AYhDFZ3xHcYNeWQyMobUDOXL9xDBG5SA1j2gMfXEq-ABk91SuDZeiO--1CvbDGDaMuGvNl4m5qvl6Yvym6dO8M-b1EanRLY6ByxItSrTBuj432KiEb6QcsnqTujvtdkd1QVepkwSNX-7lAL_HdBbtAXRQIWwFOniOasAi6Alhb_GEFgSHoNrkPqBPQUz4gqmIQFgCXOQcy33JowZFFzKP4EScV6ZKLHC8EUQ4my8u6AHZ4kb-28I9mIMQMDX3xcexVH_i3KpEj3NsVyw2hH7uM5rj1N-1TJ4pjPj5zgSmpEF0FN_rce9Pv4nT7LKHUd1TFOklXo-fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایزدی : جای تعجبه که عراقچی می‌گه گرفتن عوارض از کشتی‌ها در تنگه هرمز خلاف قانونه؛
🔴
سؤال اینه، کدوم قانون؟
🔴
اگه حتی رئیس خلیج فارس هم باشیم ولی نتونیم از این موقعیت استفاده کنیم، این اسم و عنوان چه فایده‌ای داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131043" target="_blank">📅 13:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131042">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/055600096f.mp4?token=SpjsuCnwOV3vDt_96Z0_TNdrbHuuJVFiLqcjoX_L04TkyHWFvAYt_46S5-oo3Wa7kmD9K4POxmqJEdiQE6IROsuulZcg8K57NjkIreEtzM7G7EaqcXJccbKwVQzjktyfJTj21dPZbpNfAry_EriwX1OBAMM9CwG5nTe3NcxTtw6we9pXttYvWuOsVeJDNnctaAmFjBlJm06QZk28L1CqrFz0Zld8LEK3miwc6KwePz9rVWlqiFhJGaao23v3XCujBg9ClyA2uwIUYrUIpGzLXbehw6MbXITbSU6n03QqzwHnVWHdFNXWrnlI5dI-CnfiaBws8F7boTtQ4Q8hRGJq6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/055600096f.mp4?token=SpjsuCnwOV3vDt_96Z0_TNdrbHuuJVFiLqcjoX_L04TkyHWFvAYt_46S5-oo3Wa7kmD9K4POxmqJEdiQE6IROsuulZcg8K57NjkIreEtzM7G7EaqcXJccbKwVQzjktyfJTj21dPZbpNfAry_EriwX1OBAMM9CwG5nTe3NcxTtw6we9pXttYvWuOsVeJDNnctaAmFjBlJm06QZk28L1CqrFz0Zld8LEK3miwc6KwePz9rVWlqiFhJGaao23v3XCujBg9ClyA2uwIUYrUIpGzLXbehw6MbXITbSU6n03QqzwHnVWHdFNXWrnlI5dI-CnfiaBws8F7boTtQ4Q8hRGJq6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فواد ایزدی، کارشناس مسائل آمریکا : ما
هی از آمریکا می‌خوایم تحریم‌ها رو برداره
🔴
در حالی که تصمیم اصلی برای برداشتن تحریم‌ها فقط دست ترامپ نیست؛
🔴
بخش زیادی ازش دست کنگره آمریکاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131042" target="_blank">📅 13:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131041">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCpQ5RKesA-XZDPJznpJrgpJ0282ig7nnmjZ4Y0BXuCBc1x6aT4dWOPLZXp5PSkSBQEENsO1H33VupghpPPo9QXynbVJzltzvM53F-6F4NNREHfhHIb-IUw-aGOJmT-53XRVTsavEMQrc6JDckeP0QyADg-BjFw4D8aI8dRyw815dZXV9msadsV2RX_oEhEDk2Kg1VOZK25qDbKp9QxikeSBLzRWH1MHPHo5lxCaFZaHpuoTFVREHEow1fOneWR7_FTgFBraBaUzp20mkGJhLmXuRY0ld7BqvvTlYxbiDHMu__kUdkAsNK7gbgFUPnw2Hiz4qiFt6VA7B4fZuAzxSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه همشهری با این تیتر ترامپ رو تهدید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/131041" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131040">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
پزشکیان: اگر آمریکا به تفاهم نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/131040" target="_blank">📅 13:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131039">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
نیویورک تایمز :  بیشتر سربازان تازه‌نفس روسیه در خطوط مقدم اوکراین تنها ۲۰ دقیقه عمر مفید دارند !
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/131039" target="_blank">📅 13:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131038">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزارت دفاع روسیه گزارش داد، شهرک‌های لسنویه و رونویه در منطقه زاپروژیا و شهرک مالینوفکا در دونتسک  توسط نیروهای مسلح روسیه آزاد شده است.
🔴
این وزارتخانه همچنین از انهدام هفت بمب هوایی هدایت شونده و ۸۰۶ پهپاد اوکراین طی شبانه روز گذشته خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131038" target="_blank">📅 13:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131037">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: چرا اعراب پس از جنگ اخیر دنبال رابطه با تهران هستند؟
🔴
پای یک چارچوب امنیتی جدید منطقه‌ای در میان است
🔴
کشورهای خلیج‌فارس در حال فاصله گرفتن از اسرائیل هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131037" target="_blank">📅 13:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131036">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-qaRUKsSftEzcmncNEEA1MZPRDx0PcBAORIcpFKde9fE0B9XKJvr__DXejZyCGM2PTZXx0xxE4zeZM-FHOPeLY7o4XCiMOttgfI1c10ykTBxDhR1ESLpSeWa-xXY2b_eLX1jeTIH6fm6-GPaeDY3YE6JU-Ik-hsuWEH_yTGuiMHfPndYnP6lBkSvhl42_oBPxttqiP_4JSRwyUI4cKWm_O_nkKgU7TplU27wel0-OIUsBYkYw2e-PCtWtXpXM7FaWPa2hDxrX-ytiaZFam8H81_UUJag5_vXU3FeKWsYwrIN0KG607H6bp9QJi5Hy1WX9JtqH_hPCz5rwh0t12QAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون اجرایی رئیس‌جمهور: جلیلی به امضای تفاهم‌نامه میان ایران و آمریکا رای مثبت داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131036" target="_blank">📅 12:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131035">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-zeFz3jL_ApChkDA0RTGWIOeGpcLaOB8ooQPosWWSiV3m3ct2Nbd4Ui0YGjOvgpfrPf7XmECTPMq6elrqSgnOhvF8ERVzCP1z68bSClLetyq3dUav2U8nB_yWDM9i5FMc_FzdFsHZ96wcKz2tn-qOEXzpiJTZDo36032KWkVxpPD3zoEgHm0U6XZaANAOm1sOWIfqGokEic1Bi9Kzljhx36tJ7fE-GBt4WzyMkQ8DDYCI2CxK_6-w1s5Bfqf56cM-8sUObqclgYWcy1fDxyjqZ4zyrEqzfRk2PDTN83lDJmrz9WjRike_z4R-V6bV8M2ddkDBzsUjnGAoTRLHM3Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مخزن ۳۰ میلیون بشکه‌ای هند و امارات برای دور زدن تنگه هرمز
🔴
بلومبرگ: هند در پی اختلال‌های ناشی از جنگ و انسداد تنگه هرمز، با امارات برای ذخیره‌سازی تا ۳۰ میلیون بشکه نفت در ذخایر راهبردی به توافق رسیده و قصد دارد برای نخستین‌بار ظرفیت ذخیره‌سازی گاز طبیعی و LPG را نیز توسعه دهد.
🔴
حدود ۴۰ درصد نفت خام وارداتی هند از تنگه هرمز عبور می‌کند و این کشور تقریبا ۸۵ درصد نیاز نفتی خود را از طریق واردات تامین می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131035" target="_blank">📅 12:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131034">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdsL9BHuOUwxjCFzI3hPiJHfK0l2beWnAM_XDvrvT384tjadoH1sT4LBAW8NNC0jPu5fnQTj4QtV3hIpWco9Kpxl8cagXNMo2Jfx6IpcHK1oXYex8N4Ri0QrdGC1MnHMAeqm9936anfYjcBKkgSGG9fmo9UUcRVOVPsvyxB8vposeGs-_MVxBYOjm52snwFo59g8t6lOEx1pIKyXQvngkdeCAATp6Znm6FSu_l-oQn-ejn0uPKLKVAZVcVGWWn0StNadcmV8iHu3N5fmVzrfo6l7Me13yTyDg5sVaXJGuQ2CBZAo6YyWt1D0ZOSTQvRfBJoznMi6kySNHlnmddmn4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با جهش ۶۸ هزار واحدی به ۵ میلیون و ۱۲۸ هزار واحد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131034" target="_blank">📅 12:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131033">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
فارس: بیش از ۳۰ کشور برای حضور در مراسم تشییع رهبر اعلام آمادگی کردن و نمایندگان و بزرگان ادیان از ۹۰ کشور به تهران میان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131033" target="_blank">📅 12:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131031">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mPDVYlUnVVDILVGvpal2kppeQ05a0MCl-VT9rymTCyz3xwTodzvH6e3U3VQQxlosaUt7RQuanNXwhREvD9tYxpQCl9TrgKZmep1y9C9jddkMIPrkhbtxlYPVboN__Rx7Rapw8y9lq-cn_5AnuuUrm2DadHs3S7jFANV5lF4YShhx2I3JWhKTbR6KsnB8R3Ef14_RBJoGpiACllQhaMM5AFmqP1cvR9kJBh-sUiIijZN556sMfCA28BcKEV8Yz7zWOXorwQVRwNoK0MBBNrZq9WPvZk4rBizyWJk_Rz1jZVMiIYIaze_J9ykPWMibG-O_AQs1O2SqT6pjtki6P2oXSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OP19sV4Xbvi1I2f_jy4WPp476CN7hNTPI6x7yVe8DvRJ0feYo9ENinPIecoZ62_BmZJEtkUN6SfD7Qn_PGVJJYaEc4hnZHFUOOkiVh0-aKZ9ZbOtD2gz8144Uss9DiLW7mSzFaXeUrkG9tcT_syJ5IK_Z6Ef3WTJE4_Adl1AfmgZp7MoXx79xeiGv_33ki_nbWzITOLaEXY5507t1VZvUb2iHRhcUuP5o9ZvPBVo6GzhYEnPm4utUPdrJR94T8h5dj0cHmW56tZaKD_Q5rA65AVu1dcj80AA8xkeezR6cVaMjHrhuwZMKE9AI1mXyyuC5zm5GtKvRar6i0Il0vcIeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله هوایی آمریکا به یک پست مرزی ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131031" target="_blank">📅 12:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131030">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
اژه ای: در حملات موشکی به زندان اوین، افراد زیادی می‌توانستند فرار کنند اما فرار نکردند؛ بعضی هم رفتند اما خودشان برگشتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131030" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131029">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
منابع خبری از پرواز گسترده پهپادهای اسرائیلی بر فراز بیروت، و ضاحیه خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/131029" target="_blank">📅 12:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131028">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=V5dKa52lJfQdqtZPi0zIF5MvadSlGqIqq-26GdTknLENCTBzEO_tNjuYJ0kn-lHAGloXkxzrBS_wmUXB68mpKTbObVRkF0mapX6w-Z5Cu8k-5YcEaLHK4fsOBeCGJPUEczrZRWwz68KxBIaiDI03BlCyBx4Nbv0uSnTCzSnGxtjnSIMDgBk5mLaFoN_j3FqEhwTwO_A9-bxKkAMj96CL4V0ratZJcKgjIhpvQfLI1o-xNEfeLZzfzaQsqknyLtS7141egFV-wA4YDggZOrLlp_Uk6KsgDp6FmrjKz0sQXjixI3qANr28DGKTHbtjg-ndfAYAnFrvkyl76NZ-GrR7uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=V5dKa52lJfQdqtZPi0zIF5MvadSlGqIqq-26GdTknLENCTBzEO_tNjuYJ0kn-lHAGloXkxzrBS_wmUXB68mpKTbObVRkF0mapX6w-Z5Cu8k-5YcEaLHK4fsOBeCGJPUEczrZRWwz68KxBIaiDI03BlCyBx4Nbv0uSnTCzSnGxtjnSIMDgBk5mLaFoN_j3FqEhwTwO_A9-bxKkAMj96CL4V0ratZJcKgjIhpvQfLI1o-xNEfeLZzfzaQsqknyLtS7141egFV-wA4YDggZOrLlp_Uk6KsgDp6FmrjKz0sQXjixI3qANr28DGKTHbtjg-ndfAYAnFrvkyl76NZ-GrR7uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو:تفاوت اصلی این تفاهم‌نامه با برجام اینه که برجام یک توافق واقعی با تعهدات و چارچوب مشخص بود، اما این یکی عملاً چیزی جز یک کاغذ امضاشده نیست؛ متنی که فقط می‌گه طرفین قرار است درباره ادامه گفت‌وگوها، باز هم گفت‌وگو کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131028" target="_blank">📅 12:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131027">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hds751Vyu5scKJstfd3XhRZgegqmjCIfqf9woCBWpFGCiXen4xl4hg4MVOGdKNwF2p7SHk7GhqUi0qwHUCVhL1mfsGv9gVvFQ1bS0wvysnFI0s9UAh4muXlPYVE2afNmjUT5QBc_YKCs-smX-rn5lGSS7-8T5FDq7fAcScir8rROBAQWN8AhKWSfUE1chgjNNuWbFyypi_nSI7bk-vUlF4cFDrZIS4zIAegLVell2OYT1rTtOCY946jMJCTtfnoKuaoquFo8yrNo0CzSgOvb_I42A8tslF0UAZFmVCkfXMQie1enU2vfsGeayjBrINqiK54CtrPfTk6tjF_iP5k4Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه نیویورک تایمز گزارش داد، مارک‌وین مولین، وزیر امنیت داخلی ایالات متحده اعلام کرد که پس از حذف تیم ملی ایران از مرحله گروهی جام جهانی ۲۰۲۶، «رقص شادی» کرده و حتی «چند آهنگ» خوانده است
🔴
مولین روز دوشنبه در نشست خبری مربوط به جام جهانی گفت: خوشحالم که کارشان تمام شد و برنمی‌گردند. وقتی ویزاهایشان را گرفتیم و گفتیم باید خاک آمریکا را ترک کنند، خیلی خوشحال شدم و ممکن است رقص شادی کرده باشم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/131027" target="_blank">📅 12:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131026">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
میخائیل اولیانوف و رافائل گروسی درباره چشم‌انداز حل مناقشه بین آمریکا و ایران و نقش آژانس در این فرآیند گفتگو کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131026" target="_blank">📅 12:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131025">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
یک هواپیمای دولتی آمریکا از میامی به مقصد قطر در حال پرواز است و احتمالا فرستاده ویژه ترامپ، استیو ویتکاف را برای انجام گفت‌وگوهایی با ایران حمل می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131025" target="_blank">📅 12:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131024">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
بلومبرگ به نقل از داده‌های شرکت کپلر: حدود ۲۴ کشتی باری، از جمله کشتی‌های حمل نفت و گاز، روز دوشنبه از تنگه هرمز عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131024" target="_blank">📅 12:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131023">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFcTmyHX5J9-S6yrUKm2BdGWV4FEhV2w9oq8qzAeBYkIZaBjJ7-mXi75bIcEjKlj7uck7Wms7JOC7rzadgej1Ul8y15tU8Gyk0TmlpZ8X2Z_fZq5MfcKnzAOM0GYFLtGJ8bPAKJGKi74LSwAJr9SZqhn0zCXqmjv4noxrvraCbRvBJse336dZfcwBNzoeOrGYk_tU8SPloqTf0VX5r8HYbWi8TstGwLsNNbpsUmFHGFIEJE1xuZDMt5Vrc-TItPn-8jqBtQpe7Zt6gWT-voQ99Cuc_4YVC9cBvySNvwABe6fkhXN8kCR52aWfsc9yujGCMJ86i88x-0pvibyk9sViQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صداوسیما: فرزاد جمشیدی درگذشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131023" target="_blank">📅 11:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131021">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-5-6O6fO4KaGh5mxdgpaPVrpPscJCT70MfmyINIkXjs28F25l-1wJ9Z1UZFln3SIhlaYtMZS3XdYoFj0-a_XHTcmzli7vQSGYehEzYI42vow-H8ptG_Rc81YNnRLAnkyTBkgVryThvrtMiREML92GYpqzIHRFflTov6_9R0rbcZgnbL1MBfB8uupfZyC4eUADI_NrnnVIZmr6zpi1X41Pht1LfOy3mLDrxnrk5A9KIpqhHPac2bM-Hl9ebqgH9n8QUSdz_oDG1hruW4_PIpv64oC7DzGwsYtvCFG7umFAR3IsYrvcmpvUykHbTsuyqVuQBpH0BwNWlJXDVOAgE15A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PmZvwYIfzFGDuJtkd_fJemqUyTvzW5B2wHG1AZ1OW5ZVxX61Db-AhxR5M-dQTlAdLgOrr1mhG-wLy9CqaVBUzlx2IQOFAkRgc3eKnEQ1hR_Y3XePvFmHE0cRr4dbFzZTjlnLzyf6RKC6Z4L1u9sEqh60nGEiinyw-rT5KvVNF3JmaHgseEHjyglRrKER9hBUw1G5c4S1dRvPFl1QguyXYHqi_rYbiYtoGtZ0ZiHCph0k3ZQ-p_r7mNgazbCs4YEbf159nFnZF_aUy1EdwDA9X4oYZ2JRWldj6m9L9O3ZnMgdOEi4IjE9HzkWhMlGo3w-WIWqwQxxptg7OgMt9dyqXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
آتش‌سوزی در پالایشگاه شرکت هالدیا در ایالت بنگال غربی هند به دلایل نامعلوم، ده‌ها زخمی به‌جا گذاشت و حال برخی از مجروحان وخیم است.
🔴
شرکت پتروشیمی هالدیا یک واحد اتیلن با ظرفیت ۷۰۰ هزار تن در سال را در ایالت بنگال غربی هند اداره می‌کند که بخش عمدهٔ سهام شرکت متعلق به شرکت خصوصی در آمریکا به نام «گروه چاترجی» (TCG) است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131021" target="_blank">📅 11:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131020">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
واتس‌اپ به‌زودی قابلیتی جدید ارائه می‌کند که کاربران را از اشتراک‌گذاری شماره تلفن برای آغاز گفت‌وگو بی‌نیاز می‌سازد.
🔴
بر اساس این قابلیت، کاربران از همین هفته می‌توانند یک نام کاربری منحصربه‌فرد برای خود رزرو کنند تا پس از عرضه رسمی این ویژگی در ادامه سال، از طریق آن و بدون تبادل شماره تلفن با دیگران پیام‌رسانی کنند.
🔴
این قابلیت که از سوی شرکت متا، مالک واتس‌اپ، ارائه می‌شود، با هدف افزایش حریم خصوصی کاربران طراحی شده و یکی از مهم‌ترین تغییرات این پیام‌رسان در سال‌های اخیر به شمار می‌رود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/131020" target="_blank">📅 11:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131019">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
کاتز، وزیر جنگ اسرائیل: من به ارتش اسرائیل دستور دادم تا خود را برای عملیات «آبی و سفید» در ایران آماده کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131019" target="_blank">📅 11:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131018">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وال استریت ژورنال: وزیر امور خارجه آمریکا، مارکو روبیو، موفق شد ترامپ را به دیدگاه خود قانع کند که اسرائیل باید در لبنان بماند و به ایران حمله کند.
🔴
معاون رئیس‌جمهور، جی دی ونس، مجبور شد عقب‌نشینی کند و او نیز حمایت خود را از توافق اسرائیل و نه آمریکا اعلام کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131018" target="_blank">📅 11:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131017">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
وزیر امور خارجه عمان اعلام کرد که ما طرفدار اعمال عوارض ترانزیت در تنگه هرمز نیستیم، این امر طبق قوانین بین‌المللی ممنوع است و ما به آن قوانین متعهد هستیم
🔴
این مسئولیت ایران است که مطمئن شود خطوط کشتیرانی عاری از هرگونه خطر مرتبط با مین هستند.
🔴
وزیر امور خارجه عمان با این حال، اخذ هزینه خدمات را به بهانه افزایش ایمنی ناوبری، آمادگی برای حوادث اضطراری و مبارزه با آلودگی رد نکرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131017" target="_blank">📅 11:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131016">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
الحدث: در آخرین تحولات مربوط به مذاکرات تهران و واشنگتن، قرار است تیم‌های مذاکره‌کننده ایران و آمریکا روز سه‌شنبه وارد دوحه شوند، هرچند تهران تعیین تاریخ برای دیدار دو طرف را تکذیب کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131016" target="_blank">📅 11:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131015">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qu1z9H5RvGsvqv7hD0AZfPIVVhlA3YgOhZwLFO6YyxQiCMc5tfBIl0J68NgZ8P0aik5Xm3HOdk9G3evXpHb3VOrN1ndLVqI3CVvuAePu3JONxhGuTT2qlaUYcZ4xpKnoVOe5Fy_XYTz03Pz7IBLdGAYe9zpormNkmzPCLcEGU2r2JfXnew2CVBAJyUEYz_vHtQwHLhxAK8_0gWqr0ceI-DDI6wLDoVdxina-9F9CTACm9j9bbzIIOp4_LzSFSVPOOJHW-a79-03wKbOEE_Vv0YFrCpwJyUv7n6gypXOyG2TCNJM8Fk-TdowE7JMMNeAjlYA2zvpYMqSfCVfB7RCnaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دخانیات صدرنشین مجموع تورم ماهانه ۱۴۰۴ و بهار ۱۴۰۵
🔴
تورم ماهانه گروه دخانیات در فروردین، اردیبهشت و خرداد سال جاری به ترتیب ۳۰.۷، ۱۷ و ۳.۷ درصد بوده که در مجموع به۵۱.۴ درصد رسیده و این گروه را در صدر جدول تورم سه‌ماهه قرار داده است.
🔴
نکته قابل توجه آن است که الگوی تورمی سال جاری، مشابه روند سال گذشته است. بر اساس همین آمار، مجموع تورم ماهانه گروه دخانیات در سال ۱۴۰۴ نیز با رقم ۷۲.۶درصد، بالاترین میزان افزایش قیمت را در میان تمامی گروه‌های اصلی به ثبت رسانده بود و این گروه برای دومین سال متوالی در صدر جدول تورم ماهانه قرار گرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131015" target="_blank">📅 11:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131014">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLH8kgyLdOjNCtqPntZmrCRZ29IzC9klYtktkST0jVAyDO_6QDKx4bmh-QVAW-6NYsTef7nvxoFcfetCo1cxz3i6TUCO3sQYEharfvlO5BoGa2p6tCszU67kyS1OfnUNc4vYD-ofcxgIsSwHbgZUtXjLA-DOnWsDne8PQ_hi895dzgwpu0Ot6Zq5Z0a-5Ats4_nid4b8hvjGCRu8LqTHHIyDo2NZ51DNdTzFXRtO9dCPUDzRmQuh78N_RMJT2Iw9G85ZaqZ72Kcr3FRu1OddEOU2omjdxImoFpRmdA5wm2Il8t6LMJVwyZSJGVofesi5dODGvwj0M2AnmKfXVXlFYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۱۷ سپتامبر ۱۹۴۴ عملیات مارکت گاردن و فرود چتربازهای بریتانیایی و امریکایی در هلند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131014" target="_blank">📅 11:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131013">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veqAeKZSIT_329fZ-_0-5mdlNc8tfV67oRT6SJOoKDRg1WSHs-X25S9xB5rHqvfKPdEQxjT0XTj3tRQ3KnBn0KUPto9gkh-BlGh7sfs2wg_KvnoOSIVtMg_21YqB01D8EvTsty1W4eP9XGHJzrbtZ1pBuOHkh0Dfy1dNV9p79cIdHr26jiXNl6VSYp4MwCSnjS5GxaUKGAhuqTlrgtLc4tWZA77xTvUXfffHD2I4o1KHgiQfSHKS6HIF_kyvogAbNrScTN5Fysoqpbk1xauEmoXXkEkK8SFjX6t64D6EF6B_DOkwzMh3qvkAaWEOkf8T3ruFDf7VybZRVCZbKhyRcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ونزوئلا: شمار قربانیان دو زمین‌لرزه به ۱۷۱۹ کشته و ۵۰۳۴ مصدوم افزایش یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131013" target="_blank">📅 11:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131012">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
یک شرکت ارائه دهنده خدمات رهگیری کشتی‌ها : با وجود نگرانی‌های امنیتی، رفت و آمد شناور‌ها در تنگه هرمز در طول آخر هفته ادامه داشته
🔴
طی سه روز، ۱۰۸ عبور ثبت شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131012" target="_blank">📅 10:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131011">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
الجزیره: ایران اعتراض‌ها و نگرانی‌های زیادی درباره کندی روند اجرای تفاهم‌نامه دارد
🔴
در مورد اجرای ماده پنجم توافق هم سوء برداشت وجود دارد؛ ایران می‌گوید می‌تواند تا زمان دستیابی به توافق نهایی، تردد در تنگه هرمز را مدیریت کند، اما آمریکا بر این باور است که ترددها باید بدون محدودیت ادامه یابد
🔴
همچنین تهران نگرانی‌های فراوانی درباره ایجاد مسیر‌های جدید دریانوردی در نزدیکی بخش عمانی تنگه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131011" target="_blank">📅 10:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131009">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OC_rNEG4g27u0nYMCRCn9yaDG8anWZ1e7xoSDl-L2TuuXJ_bNTbGjQVM3728j0d2uk6PWJyNOW42qvKMT1sfcAZxExVp0zv99OSl2a0jhMiTgrxiMALwmADHjUfq0ctgf5pqeoD25Bj8mbQS4I9kJCabnkDV1byVNlfFvxeWC_Mzx435j62U46LhmoT3ZO3AT5ps5naCLYbsITNx2yeetdmqrlqX9-YBFKTp-XwLcUUNhd_I8CzLdy_B4xOeM_1sWuPlWXFRb6ofwLT-JRSAWFq-AXsPAb7TjKHtcKENlOMiVOeSz7rm-NV8GjHpTHZD-G_q7RTfEC_2SyhZMekTxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cILYtHfExSXbQKRdxg_phch4S0on03exMwAzH4WJwp6ctCniVc33Q3LlbVLEnKdRhh0wt1cVarVLlTBotq5SYbFjdffKsmIJFWp6BWJGIlu8LFGSeJ2EmQEQ36vKCfqvEWNAeuSAf7ybrHlfr1orqUV6bVIJaGG4EvhHPWlPVCOFMRRtlL10pOAOpaHkP3giKV976XFJgTcosCzjhJUpV6TeKh8adNPoy6oT0xxvHd-uCGBaxw1mB8_CV_CBBrZXPeKXnqB9QXz9gJAaarItF2GjZ03WX9t1vypNC5ssVEmBOe_B6hUlU-eED8Q1rUCqEgXKqTkmMdi7blL6wxMCGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک نفتکش صبح امروز در کریدور آمریکا مشاهده شد
🔴
پوشش سنگین هوایی به‌صورت ۲۴ ساعته و بدون وقفه فعال است؛عملیاتی بسیار پرهزینه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131009" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131008">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
دبیرکل ناتو: چهار تا پنج هزار سورتی پرواز از پایگاه‌های اروپایی در چارچوب عملیات علیه ایران انجام شد
🔴
آمریکا بدون اروپا به‌عنوان سکوی بزرگ قدرت‌افکنی قادر به اجرای این عملیات نبود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131008" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131007">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سرپرست وزارت دفاع: به دشمن اعتماد نداریم؛ دستان ما روی ماشه است
🔴
در صورت نقض مفاد آتش‌بس، اقدام و واکنش متناسب و لازم را خواهیم داشت
🔴
امنیت، مقوله‌ای درون‌زا است؛ کشورهای منطقه باید خود درباره امنیت منطقه تصمیم بگیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131007" target="_blank">📅 10:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131006">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سپاه: انهدام مهمات عمل نکرده در محدوده سرخون و ایسین بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/131006" target="_blank">📅 10:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131005">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
پزشکیان: توافق اخیر در هماهنگی کامل با رهبر و حمایت شعام به‌دست آمده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/131005" target="_blank">📅 10:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131004">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
سخنگوی اورژانس آذربایجان‌شرقی:
حادثه واژگونی یک دستگاه اتوبوس ساعت ۶:۵۰ صبح امروز سه‌شنبه در ورودی چهرگان شهرستان شبستر به مرکز فرماندهی عملیات اورژانس استان گزارش شد.
🔴
عملیات امدادرسانی به حادثه‌دیدگان آغاز شده و بر اساس اطلاعات اولیه ۱۵ مصدوم تحت اقدامات فوریت‌های پزشکی قرار گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/131004" target="_blank">📅 10:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131003">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sn9PDDRYJe1NuCYRXKLY84WFRtC2VohiNtfT_vAHO4XyTDtM-MyBNHyP6-UyZGCRdrsEy3f88oe8I4dGGeW1nJxXiQkixaGUG4eiXW9MztBsPh-GCy9FWdeUJ-AGbXW9elBOHUR1WXFyfRu_degI_5mzAW0iBXx-bImZDiG3jNwkX9P7v4GszoMW2EnXAC8TNrHAjiqQDuLhr-2ExFgiN1vfBRbb8aX5SrXFwHjCw3J93tyHk4Sup6gpRHjt9dVUnVfKXl1j524TE1a6ywq5GxiiSA8QE7WKnZgS68LZB0rLTNsCeyGhZszwCv5I7w8Y3DTU3wPcAQXtop-OUWWQHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ: هدیه‌ای طلایی به کاخ سفید به مناسبت دویست و پنجاهمین سالگرد تولدش
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131003" target="_blank">📅 10:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131002">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
وزارت خارجه آلمان: توافق آمریکا و ایران برای ازسرگیری مذاکرات، گامی مهم برای دیپلماسی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/131002" target="_blank">📅 09:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131001">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
روزنامه جمهوری اسلامی: در جامعه سالم، مداحان نسخه دیپلماسی نمی‌پیچند / دیپلماسی با شعار اداره نمی‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131001" target="_blank">📅 09:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131000">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
پولیتیکو به نقل از منابع: روبیو و ویتکوف به قانون‌گذاران تأکید کردند که ایران تاکنون هیچ مبلغی را بر اساس یادداشت تفاهم دریافت نکرده است
🔴
ویتکوف به قانون‌گذاران گفت که تیم فنی مسئول مذاکرات هسته‌ای، سوئیس را به مقصد قطر ترک کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/131000" target="_blank">📅 09:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130999">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
دونالد ترامپ از خرده‌فروشان سوخت خواست که قیمت‌ها را «فوراً» کاهش دهند، با این ادعا که قیمت‌ها نسبت به قیمت نفت که در حال کاهش است، بیش از حد بالا هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/130999" target="_blank">📅 09:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130998">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ادارات شهرستان کرمان تعطیل شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130998" target="_blank">📅 09:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130997">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbc09fa73.mp4?token=fjeKCa0oGKMgZv-haxAWE0ECk6cogq78V8DZNhCDLAM-D7tnxj3hPp2uxfTgLtvaFZKx3LrYHKUhQeUZYDua5NQdC8WPNvDOCssFgwOpOfQHkA_JHE8KxJb1d5xgSKblfRU-uUdNEThjOhcePy2q5czKhJdFGNCPiuvPQd-u3pz1-RjuYpCwv6PUBqW_Yxfm1UDKCFSL1LwzXrk-KGIS55l7HDQl1hKgGkCY_E1hGPKnBzV43eGRv3cgaP-5F4qu5Wi8GlUNejt7L15WQ87yh632-UvuAP07SHcU0dSTIkae7qeKBX9Y_pLt9Ta0ubMmMR8TyPIpRBu8MZBWmYxmNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbc09fa73.mp4?token=fjeKCa0oGKMgZv-haxAWE0ECk6cogq78V8DZNhCDLAM-D7tnxj3hPp2uxfTgLtvaFZKx3LrYHKUhQeUZYDua5NQdC8WPNvDOCssFgwOpOfQHkA_JHE8KxJb1d5xgSKblfRU-uUdNEThjOhcePy2q5czKhJdFGNCPiuvPQd-u3pz1-RjuYpCwv6PUBqW_Yxfm1UDKCFSL1LwzXrk-KGIS55l7HDQl1hKgGkCY_E1hGPKnBzV43eGRv3cgaP-5F4qu5Wi8GlUNejt7L15WQ87yh632-UvuAP07SHcU0dSTIkae7qeKBX9Y_pLt9Ta0ubMmMR8TyPIpRBu8MZBWmYxmNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در اردبیل جلوی پلیس اینجوری به یک نفر حمله کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/130997" target="_blank">📅 09:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130996">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUkZnCy8MaKajCRGOJCKxA021a1oAmCCiUZql4gg20d1-Tec9P2SWlsfQUPJRNcr5KONm6uTuhSFiS4oMc9RhRXJ78f8VZSY9px5YMxGp8sQwDcyB4tfSDm-f82XbaBMtaf0DfyZcsgwnHdVXaaQKNKM3H7_srTcr08UfYyHM7jAUiu3NCXUhnlN1N9kIyWRMhC20FnO9WVKkgC8Q3kB9fiTXn3UkXfhV_ploGUw2W8XqDt5OZSfU76RfsaoFhPHm8iPn0rJd4msrdnQQBWZL0sOQe0zXL-N9peDOq0jdWhJJp7hBrkTXkZSdcJ2vHpBaeOgteadrmmld-s1iz_VbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دریای خزر در حال کوچک‌شدن!
🔴
۲۴ هزار کیلومتر مربع آب کاسپین در سه دهه ناپدید شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/130996" target="_blank">📅 09:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130995">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFFxBxHIiF5NKrpWeOtVIGjeqa7wwYuYDzvXytciIsxctEc2xJsaJQR2BKvS7aFPvyef6oMp357SoE02VkYkgK-cvS3BBQjtIpsFV9d8NZF6vlS_7RhDsP1zer9B8-3nr8L5YRF_oEoPeEAcIaW7OqRNX7UIkUktArTR_SYh8XmmT1CiXLh02fg97rnUPsv0DLSE271fRIw0Fwc6BYpO_BgjIffbElK9wpnSX018zNGnXW1b5rphN0OHVjHvNC-8cTMxuAMxesn_Wp6SwwGyc1wUsY9XrVlouA53v83-JX7iy24QQ4CKZ8XsT2E7-mV3-mnQdzERhIUsGBkr7ycgXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش مشاور رئیس مجلس به ادعایی که نبویان درباره کودتا مطرح کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/130995" target="_blank">📅 09:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130994">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFMjXYEsVdzamjuQ9qEfbRlz7hpVxou9xAwOAkvZhe9DNP8ZobfQ7JNhGV0jCO0JmzF_3M9g4PbGSEhkzKHhJ6UKkMMlQARzg5bjByIJ8nMNhp2rS-zceiOM8EPXOhKyXoA245QwWT5whnkeNkg2G1JzChJwh8itPQFxpfNmLICgn-rM0om04GKNiWDHfMXe3bQXw7Lk7WSROOLLGokDXtn3bEolTASM5F5sXR77CCjO9CcFJfvsInRt-P9O4gLLOoU_AeF7DZq6xv1kLJ09IUXi6LzlX2cfe5-i_2-_fWf2Hk20Jq-vf9NYuAeNriz5a6huxBR4fBwsjjwCisKCvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌ان‌ان: ویتکاف راهی دوحه شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/130994" target="_blank">📅 08:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130993">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
شبکه «ام‌اس ناو» به نقل از منابع مطلع: روبیو در جلسه توجیهی با اعضای کنگره آمریکا، گفت که دولت ترامپ هیچ توهمی ندارد که مذاکرات با ایران آسان خواهد بود.
🔴
روبیو به کنگره گفت که احتمال شکست مذاکرات وجود دارد، اما دولت می‌خواهد به مسیر دیپلماتیک فرصتی بدهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/130993" target="_blank">📅 08:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130992">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plrLdmQsQoNth-HSi8fm9-Fu2ej19oGafkUI0j_CiXFnA5OKG7Nv2YlizqThQR_z7Q3bCios7pV_KUFkqhZW1RfXmcWD-lfM_c8Q3jW_y7eJygO9SGX90WjN9aNRj-fQrZqekCoALnR2mu6vdivNg6aIlUeUpaNarFxqsQYBdRLl6zEJ2Jh0KSCRQRQOGhB_zxrMnL6_3dPGWIIqK6eyYoXw7tQldtLFnDDq4TRnE0WlDyNEwptz-8tDj-gW3FLU9TZhMg-elgyIM0YLhhg-03wDx6XYMk0V8CWkGqm9VsMn90Z_UaTbgDxe01DV0TKON5jY2Aqx5MkueLvxS422yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه نویی 170میلیارد تومن از فدراسیون فوتبال حق الزحمه جام‌جهانی دریافت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/130992" target="_blank">📅 07:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130991">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAvcKP9sFQePKQQAnrKwyq9b-1ZthlkW5BcAhApf1iEJHg6JzNQmPLMGbfH0yc-ogByiazfN52tMrk6bdu9QinzgSX99c57368oTNBCWy9tLF-9Vhm2TAgkAEBRM4AjDUNbt63nilSdWWb4OcJsZlcFfj73RWYd1kZWTu5UxYWAmYBoTk8uHJCXs-r87Yrzy0u2WX0n6ywqsbHmYUPd0cqNO0eH-80LHSb3_jY1lxsA4eSE4zlm_7Pjg87tWQF0d7ePsXaMo-QpjV3AtAGuyG8URfZkccAG4CMf3r9yleYF_HpG3l25DSyQoiuFU-cVnO5cba0r_KcyqP1_mdgmc7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شریعتمداری: باید ترامپ را اعدام‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/130991" target="_blank">📅 07:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130990">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSooraSkyvia@chToolsBot</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyJCK32sBHy3QkzFveV6d9I6ss61TtwsRet6lOd3VCzFvNQH4QKfglM9hhZgxWdTeRKSbKC7U7OCrO4IZE6iHD_KxtgHiKhmGCOTjw9Ls4H8ASGC7jLTX_I7-yfm8_2h0-J5JNo4CWp_COHxOlvO63tlH19XCdwhdwSSIwag2potU0HXmL32XeyOmB52FIwkD78fvN-NQfjbNOMOf5iGOLVqI6MllXP6YhXTgEYBI-LDBSIKZZwdzT1m_xm0sSChuL-xrrIrjCaNnEv1eODa8m7I1rSHGCJgtwewWMdJvORpfyCbJUtZw06k6NaWcokYgTcWTYiaKSUNPFuKzSJyTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اگه تحمل شنیدن حقیقت‌های تلخ رو نداری، اینو اصلاً تست نکن!
❌
همیشه به این چارت تولد و ستاره‌شناسی می‌خندیدم، تا اینکه خودم امتحان کردم و لال شدم...
😶
دقیقاً همون مشکل‌هایی که تو
کار
و
رابطه‌هام
داشتم رو مو به مو آورد جلو چشمم!
انگار یه نفر از بچگی داشته منو آنالیز می‌کرده و می‌دونسته کجای کارم می‌لنگه.
👀
اگه می‌خوای بفهمی:
✔️
کدهای پنهان شخصیتیت چیه
✔️
مسیر اصلی موفقیتت کجاست
⚠️
این آنالیزگر روانی رو از دست نده.
⬇️
فقط یه بار تستش کن تا بفهمی چی میگم
⬇️</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/130990" target="_blank">📅 01:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130989">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=egkdt6h4m8DbA7uKKQ7BdpuIxrB24ejDLmvwFeqbLakRTetLhEmDub1lDW4S9o50LjXywyrg6C2OMYVlGgmPBG5tXX3J3qKNyJ-2C1MjOjBmP7sVh-_PoP8w1Pj7zZMMlK_oGjnysKzrqWo2pDojtm69HwoGPOxKMmv8tVluc9jYPUJDZzNkCpjoE_VaMJ3TF0DltIXFfK8SzE1xWPNfOhY8Ej8zEAZqVnfx47w3KUURX0droUJBajN-SwMk_t5P0cMpfiNNnBuCXO1WXcXol_lBx5_teNWNg4H9RxLqXLbTPiVpUXIjiErRK1Yl5trjxDZF4yMVLk_U-k3ymrYHgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=egkdt6h4m8DbA7uKKQ7BdpuIxrB24ejDLmvwFeqbLakRTetLhEmDub1lDW4S9o50LjXywyrg6C2OMYVlGgmPBG5tXX3J3qKNyJ-2C1MjOjBmP7sVh-_PoP8w1Pj7zZMMlK_oGjnysKzrqWo2pDojtm69HwoGPOxKMmv8tVluc9jYPUJDZzNkCpjoE_VaMJ3TF0DltIXFfK8SzE1xWPNfOhY8Ej8zEAZqVnfx47w3KUURX0droUJBajN-SwMk_t5P0cMpfiNNnBuCXO1WXcXol_lBx5_teNWNg4H9RxLqXLbTPiVpUXIjiErRK1Yl5trjxDZF4yMVLk_U-k3ymrYHgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک مداحک:
رو هلیکوپترشون غیرت داشتن بهتون حمله کردن و علی خامنه‌ای رو هنوز دفن نکردید
🔴
۱۰۰ میلیارد دلار پولتون دست اوناست، و میخوان ۶ میلیاردشو بهتون سویا و ذرت بدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/130989" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130988">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
شمار قربانیان دو زمین‌لرزه ونزوئلا به ۱۷۱۹ کشته و ۵۰۳۴ مصدوم افزایش یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/130988" target="_blank">📅 01:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130987">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUByXKcs1cfmLNCJiyEIkgkkwWNVptxu7MwlpRbpY9MSSp99B5xAwZj_7E8Jmf-PQYTVE3Va6Bd9N1eaDD7Z5I75CuTEaNCR2ri-EBmRt29h5X1EmzwZIJXxajbcVLZDvptPmQ7ewmdsblGRZIjKgzlsoEehzucAwpEr-m5eLmiTbxEMv1C0H4xJZvFBypX65A0TXsjhS0nYHakA_NzUTrX9KhkNrnXQRJ5unkpXBc_svAhQ4Q2I0ify5ZrYGCt-pctTay9Y3_8En-wzg8Wsvu5rBatWQMhI-59R156y2SP1W88ICLsBcmVgvjaZGttcAjwWs-0Km_Rch3W9WSalBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امام جمعه اهواز(مِگامَن):امتحان نهایی هارو به تعویق بندازید تا بچها از امتحان الهی یعنی اربعین مردود نشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/130987" target="_blank">📅 01:01 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

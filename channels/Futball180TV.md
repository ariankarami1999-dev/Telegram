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
<img src="https://cdn5.telesco.pe/file/l9Ok3GDC1DKY2enHntFJFNcOH_b8T7gktxg69k9FgjctNIlr6-kkfK_MUQREOZU1RMSxLi6V9BcBdldG3vKrxMc0PSSYSWPwTlC79eRM46_6xLhZGzmhYA5CCFJVdIxV00uV5-SF2lFKKTgfsbxpYQnslJZfXWZS_xWtQesJVM3iQATWgOH1QujRmMQu3Nllil-c-CLD3426uVDwN5kEfwRA7oDNJv-Po8PxJNn4ZVNwry4KbwWpZ45B2Ta1DPk0GI16Ti47j5JnbhfsvFwJANQNqbJS7m86DDwZldqLt3nhXgyObQ3CqpUGaH7VCAIFDRrA3EOb0JaXYEFUKr8I2Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 667K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 17:57:40</div>
<hr>

<div class="tg-post" id="msg-94210">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FccbTx7bfMXcnIuE_38POxPCKhgA2nknpxwEIvcDD8Zk-chzEF6XrZVm0cNVcykmOizOpcV9ilxKfZ0UVb00TmQBAUhVKSI8c2rPQXf5o4MaQgY0dGlmJBfeWXRkJyyEuaITLGRZ3wTPzsmGp9DMICWYs5xaZF-3Jq_O38xDVxW5ccwP5_OA_LcdsDVylQe-l-R9-OnnFwjpC9iw5SyepDj7EY3jZ6yZo9gREEEUKpIpkCUDuKfpgOUm-Mg4lzn73ou49kuh4IINGdDdYDE5LHFs10h-5lcn3Fz8sVYnOTBb7qsmv4awC4bIYo2ZZaq1hT-SlYQ9GnOwYr91HdR2cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B38LmOjwomvgBl88-Fv9cCF80OSXqrHBsaMVRdUvwr7zH2-93vM6cy2jdgkzYjKsNElDKQRUYSYhiHx_if1pVyp9tTSl4MDL6iLxmksblM-PFTfM1w7PvJQgChie3q5Y-u3SjtTVe2dU45vVbiTjh7Z32Iu37chCJEWETfW95g8QtFeyRRg4CN4159now6CIl7kwZYdQ5KA1Ohpo1hyodrSkx0vfRXUZFY1xvIDf4JHwKCDr0JuwwrPlbvPBK43q92u2eOxkc4qQt1LYMjUhqjhHMe_LqSvS0R0NIpksuqtt9QyMnDeo8HNf_pOzieDIrxpi3EkcBWu-0tJVE4pNfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚪️
#فووووووری
از مارکا:
رئال مادرید در حال بررسی ارسال پیشنهادی رسمی به مبلغ ۲۲۰ میلیون یورو برای جذب مایکل اولیسه است. رئال مادرید همچنین میخواهد این تابستان هر دو بازیکن انزو فرناندز و مایکل اولیسه را جذب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/Futball180TV/94210" target="_blank">📅 17:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94209">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/916898ff1e.mp4?token=n6YILFhyUhlnECE0sAKiz598Uk92QqWfH4vRNSdukF7YpFhRBW09BwMy0Ln010USehkD_YyODI5xZAh9TIW2JT_g4XmkyF5Yt5ArFiQD3WRQ5m-CaGzWDe3w-Whu1KhJixqgQLnH5AB9xaN4wEqoJM_LZzD9a65SnYqBCdZQmMnJ9I5PaGLDfLGxXSWKEUE3wrjhy3Jz6zQePZ8JSlY9Ti968kJnOM8J4OweivqGakL4sPMneHuBfGiyChb7hMhIPz2kcFRCeX8s1ZYSxB0ia6Y2YlWQZ__ZrKnNkp0YGCXOQajbzSUMI8ppGG-tP67RSvBYkcJatVg5b_WJp-NSow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/916898ff1e.mp4?token=n6YILFhyUhlnECE0sAKiz598Uk92QqWfH4vRNSdukF7YpFhRBW09BwMy0Ln010USehkD_YyODI5xZAh9TIW2JT_g4XmkyF5Yt5ArFiQD3WRQ5m-CaGzWDe3w-Whu1KhJixqgQLnH5AB9xaN4wEqoJM_LZzD9a65SnYqBCdZQmMnJ9I5PaGLDfLGxXSWKEUE3wrjhy3Jz6zQePZ8JSlY9Ti968kJnOM8J4OweivqGakL4sPMneHuBfGiyChb7hMhIPz2kcFRCeX8s1ZYSxB0ia6Y2YlWQZ__ZrKnNkp0YGCXOQajbzSUMI8ppGG-tP67RSvBYkcJatVg5b_WJp-NSow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🏆
خلاصه هفته‌اول مرحله‌گروهی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/Futball180TV/94209" target="_blank">📅 17:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94208">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37dc9fa1fc.mp4?token=K6c3WpMtJqtXgjI6lqOd-lG_NPb_PkscUnXXY7EpMgPg-IPF2IICJ7Bmt4WfAYnjui9P0jMVQX1PUp-pl6TlkvapI9XHRRJXj9stUxsxiHgDydAjAkqYbnSafrZReJlYCS8JcdfK-DETgDhYnPXO_91UEB-RpEoJQ158qkVE0CIKt1FoGd13mFoqJwexnFbU3_scrGjiEd9QQvVcEt2k54cybr1izQqmAasCYAxA2v3miRhLaQqSNbEX0DOT7VNHq8s8NC6INES5qPjyoWDtjklkHJITsMSDTq4Iv8S4ghzdpXW_rC4m4LEMNeuplYvsUthNz6hHdDgQB7ITLa0YZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37dc9fa1fc.mp4?token=K6c3WpMtJqtXgjI6lqOd-lG_NPb_PkscUnXXY7EpMgPg-IPF2IICJ7Bmt4WfAYnjui9P0jMVQX1PUp-pl6TlkvapI9XHRRJXj9stUxsxiHgDydAjAkqYbnSafrZReJlYCS8JcdfK-DETgDhYnPXO_91UEB-RpEoJQ158qkVE0CIKt1FoGd13mFoqJwexnFbU3_scrGjiEd9QQvVcEt2k54cybr1izQqmAasCYAxA2v3miRhLaQqSNbEX0DOT7VNHq8s8NC6INES5qPjyoWDtjklkHJITsMSDTq4Iv8S4ghzdpXW_rC4m4LEMNeuplYvsUthNz6hHdDgQB7ITLa0YZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
🎙
روایت مرتضی پورعلی‌گنجی از مرام و خاکی بودن ژاوی هرناندز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/Futball180TV/94208" target="_blank">📅 17:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94207">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/182af5a6db.mp4?token=i_kDuL2vTmT4ZKJxymFttjubani8-hMU3VBqmtAfA_p1iD72msvLGuGWZbUdyyrLZC9D0orKY4RuhDl4R7FjdMtm06of6b2ed4lEvFiYTuyEg9LG-MBbv76rtn0Uuc3nPP0808AI1qNJVRI6MW95lnB7geL64jPlRzmJ7jFHlK_fLsCzE6ZQjj7Cdf45R86mqRfwOJ2QglMl8pgneIy-FGCIR2AzcAKd2dh9gVawBxNYw9e2X5A-cMv0GjLJ1cUZUEYJMo7rrpLxLGWpg4GTnaHT5wPFgzPokcV4pLcCjckb0plKaQbsMadXB9WxYAmKChgUb2MplcsHeUgZCBbZ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/182af5a6db.mp4?token=i_kDuL2vTmT4ZKJxymFttjubani8-hMU3VBqmtAfA_p1iD72msvLGuGWZbUdyyrLZC9D0orKY4RuhDl4R7FjdMtm06of6b2ed4lEvFiYTuyEg9LG-MBbv76rtn0Uuc3nPP0808AI1qNJVRI6MW95lnB7geL64jPlRzmJ7jFHlK_fLsCzE6ZQjj7Cdf45R86mqRfwOJ2QglMl8pgneIy-FGCIR2AzcAKd2dh9gVawBxNYw9e2X5A-cMv0GjLJ1cUZUEYJMo7rrpLxLGWpg4GTnaHT5wPFgzPokcV4pLcCjckb0plKaQbsMadXB9WxYAmKChgUb2MplcsHeUgZCBbZ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رونالدو نازاریو:
به نظرم اگه یه نفر باشه که لیاقت اینو داشته باشه که جلو بزنه و عنوان بهترین گلزن تاریخ جام جهانی رو مال خود کند، اون آدم کسی نیست جز مسی؛ مسی بهترین گزینه برای داشتن این جایگاهه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/94207" target="_blank">📅 17:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94206">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c565269871.mp4?token=rh6XiEIZWljBCu4ljfezMAfVqQFTcJCI0IAeal4hMar4jYqqvR6mL4ppQ15OZsMlJ-_8slxbYflKHDocQfw9hc3mH3WG1QZRzJg8TwkMKgxJcd9yyiLpGuhIHYlAYeOeJXATY3vXBAlO0KMpAljdTTbQNyDFFe_2My2wrALZVicAVg_hWcqr4oEhcbs2T7d-P4IyLI3WLL_TvI_cqEY9jRNqdcISMk2jK9HAAaMxfet_J9cdj1CmDNs0ubXWZN1L2EK8gaW96oF9tMWKZHb5Df28VfwNjHXXCveEW2OljttBR7bpCzcmsLPh9ZY5ybK2yM4MUwxsc2VLgbMloS9vYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c565269871.mp4?token=rh6XiEIZWljBCu4ljfezMAfVqQFTcJCI0IAeal4hMar4jYqqvR6mL4ppQ15OZsMlJ-_8slxbYflKHDocQfw9hc3mH3WG1QZRzJg8TwkMKgxJcd9yyiLpGuhIHYlAYeOeJXATY3vXBAlO0KMpAljdTTbQNyDFFe_2My2wrALZVicAVg_hWcqr4oEhcbs2T7d-P4IyLI3WLL_TvI_cqEY9jRNqdcISMk2jK9HAAaMxfet_J9cdj1CmDNs0ubXWZN1L2EK8gaW96oF9tMWKZHb5Df28VfwNjHXXCveEW2OljttBR7bpCzcmsLPh9ZY5ybK2yM4MUwxsc2VLgbMloS9vYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
حسرت یه موتور روندن اینجوری کف خیابونای ایران رو دلمون مونده
😢
👅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/94206" target="_blank">📅 17:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94205">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tvnw5eyJ1pRGKqDkwllOMNLJIettzcBnoEfSfqoUIWFCEHe78clMdxn647U5rKs3VzVCfvapQL4q1HImA_Bx994k7KL8JaocjXAXAK9LBTeCUqNSip2_EY67ZK60oFiunp8_ZmFxcqaD-dhHfNuXStnQ3kqQzvyrTHuT6y7kj1pOVchAsj-BrfqLLjibjNn9zPrQj8mRF1UEvZLBTDJFRRsRYXDbwXILsUPl25U5S9WKVVHR_AV-3ptmflnyRN_ZZ_M2KY41VZQ_2iuozE5vz_2chzfC8i-oHDkO3nz5ZWVq7F-mBbr9FOYmWSyPSeHwFhWzPBl9B4146cl0GcDVEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پیتر اشمایکل:
روبرتو مارتینز، بدترین مربی تاریخ جام جهانی، نسل طلایی بلژیک را نابود کرد و این برای او کافی نبود. حالا او میخواهد این کار را با پرتغال انجام دهد. آنها نباید اجازه دهند او حتی یک بازی بیشتر روی نیمکت پرتغال بنشیند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/94205" target="_blank">📅 17:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94204">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUeSnnMeWOyrHtPXjcMTus8yqPYN8Bh4KP2wxk5RE0VTemXdxURcYhm2ZPM7oykfQqJ1g8rL7sk4QfHCRzlluyjJNOJXt7fDX59j3dv9CzXlp4kTG7dwvCbNLBksAF5vrq0iEf3PUjA_-e3cvf0FQ0RNNUQKBBd_8tolfP-q6-arCwF_TlUI2qzf3onY-XyA6_pBYaPqfJ5Jb6AMrHRj2XcA52u2rkt2XRG5kNPk1YO034ERdRIUfWu0F9NeL4N2CNYDeInv41drIq9IEARov1gAbsZY4TdJ9k98PNawttLKDMmqETO-BxMmtP85B7UYItocAAtAIEh9QYH5RqGxZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
فابیو کاناوارو چهارمین بازیکن تاریخ است که برنده توپ طلا شده و به عنوان بازیکن و مربی در جام جهانی شرکت می کند.
فابیو کاناوارو
فرانتس بکن باوئر
اولگ بلوخین
مارکو فن باستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/Futball180TV/94204" target="_blank">📅 16:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94203">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f7bc36d5.mp4?token=mRXtv-BoidrqaP0Mx6HrsmbnzXkNwvdC2tNxObjPc-oElPerE7AVBeOrSCQWHrJSowTUXvmW9OblsIqmY6FMo_A2Cwf3z0TkdoddreCV3A8QY8okXdRUvxQzIyfU78ktG268oIB5A5GzlzgJWNHM6feuFOqY9_ik7rkECGt0--8AgRR_g5-FFo8qt1eRb6OkglWkL6gErGPYHL9T0gdKChypi5gWfY7Y8TAONZcEOEcBDMrKKx_bK1qPzmAstDbLA_xfFt-TryhSPNxqgKVX18dzSI_ZxADQGmCc61NI-wkd_HVXeWYPNZaZYLxOX6YgEw1Dq307D_IJT37W_MG8Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f7bc36d5.mp4?token=mRXtv-BoidrqaP0Mx6HrsmbnzXkNwvdC2tNxObjPc-oElPerE7AVBeOrSCQWHrJSowTUXvmW9OblsIqmY6FMo_A2Cwf3z0TkdoddreCV3A8QY8okXdRUvxQzIyfU78ktG268oIB5A5GzlzgJWNHM6feuFOqY9_ik7rkECGt0--8AgRR_g5-FFo8qt1eRb6OkglWkL6gErGPYHL9T0gdKChypi5gWfY7Y8TAONZcEOEcBDMrKKx_bK1qPzmAstDbLA_xfFt-TryhSPNxqgKVX18dzSI_ZxADQGmCc61NI-wkd_HVXeWYPNZaZYLxOX6YgEw1Dq307D_IJT37W_MG8Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
یه ماه دیگه میفهمی به بختت لگد زدی مردد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/94203" target="_blank">📅 16:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94202">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vi-gbulRr-J65gd8Jr5FM321N9_-vkTL-x8u_uQguSlF7i6Yuvg4MBdyYBJVFhmGNbuyBKetDSiRaiO40MgphFNgNdq5ESbVSb5qo7qnKdYMPrUwdbmvD5vLrM1zwNWBuHiGQNnIznWf9liQj4YCYwBEPTqCd7ieBA1KOIH1gZ-huTbt6-6FNj6X8Zu5QeyMcv6ub4y4vqWXF53rNNB1IQ7mJahHm8sCOTq4Qm7XsuP-mGY-RbHMbk0UPUYUqGC1L5dw5kUTSWte6Ez2__1yiczeC4xYVp2kgdfsngZixU696wNEaNv3NbCcNzYI1uUc_CqONCrB_LUXliBOuuzNkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل تو رختکن خطاب به بازیکنای انگلیس:
دلیل اینکه این پست رو قبول کردم خود شما هستید. هدف کاملا مشخصه: قهرمان شدن در جام جهانی. باید از همون اول درباره‌اش حرف بزنیم. میخوام به جایی برسیم که قوی‌ترین تیم دنیا باشیم؛ تیمی که هیچ‌کس دلش نخواد مقابلش قرار بگیره.
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/94202" target="_blank">📅 16:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94201">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxEUbJGjxkEf7F40QVvcV70OT19wqLtaytFALEjc3HCgQ6BkIcRnJ4U_R0rgkuB7MnIs7bEY7Zitvkhhl1c3hDfudbgv88-mtNePK8zBJiqo2KbVnzlULKPOsRjjdCRsnm4C7XjWsDF354uMNWOrkTMsYPnaklD_0j07qh0UGe70h92rKFbmPwqw_8UutouMtO4_VT68A-wRfcRJgv8kX2vCv9Im_4NtXtWDrKcqM8ZqKXcEwfvYEqXdw1HkfiGHiaG3bgHeqp4IDBFQDWotR26qNa8YHW-XhfdF0brG-NMvvyU79Tgu23jDaeFsPSed9seSHSVpO8wK1CegSC_nEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خواهر کریستیانو رونالدو:
بازیکنا انگار یه‌دفعه یادشون رفت چطور باید پاس بدن، توپ‌گیری کنن و حمله بسازن! تمام بازی رو به عقب و کناره‌ها پاس میدادن، ولی اشکالی نداره؛ شروع بدی داشتیم، امیدوارم آخرش خوب تموم بشه.
🙏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/94201" target="_blank">📅 16:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94200">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTQaSUaSR-XPYofidNaVmZ02O1by8surcdsii_dfVsjDOGeMahXkBS5Rfd9A1IrvlhAohoGjCEFCUCgjbSxHuMbpeCZnjYeN1-MgkyVWSXYUPz4P96YpmvP6J64lKcMc_yEhzkvs2oLBoS5jZpPdcRBCQY253xtpe9OjvLnQwc9Jy6giUeKMfz7BmGADvQR6fkoMjlaKHAZsTRbMmHgUKRWotmWM91LmY4tov7vfZTp1asG3_gt-Sv_4b4xM958NuJW5cpHUjh61NnESy--HPwVDez9aJIsrt0HyYDiKY9uM3ruTb7n7VoVxWEyXVi69VjU3__iLkrFQVciIWOy6VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله
جیمی کراگر به رونالدو:
مسی مشکلات تیم رو حل میکنه، اما رونالدو ممکنه گاهی خودش تبدیل به بخشی از مشکل بشه! مسی سطح بازیکن‌های اطرافش رو بالا میبره، ولی رونالدو دیگه اون تأثیر رو مثل قبل نداره. بازیکن‌ها رو باید بر اساس چیزی که الان ارائه میدن قضاوت کرد، نه افتخارات ۱۰ سال پیش! فوتبال بعد از سوت پایان، به گذشته کاری نداره؛ فقط عملکرد امروز مهمه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94200" target="_blank">📅 16:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94199">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b65f43b16.mp4?token=us_RapEE4cYsU0szxaGyrrtEhjzfJ1HpjLO5_nCQmpm3z8LAATNlWHC9WqLjqB_4DDKvGggEuJ2G15vXP6CzojGdFgYSjlwWj4MufEB0dTptZRuqY8XhS2G3vABN_8kTU79WWNj5FKfQvr9UGrGqpy9ivQd1cQ2oVCwKTcVMJWyYuR3xe3eGDAHgVlZOViBK6xLdnLnZ3y89Y6DxaNRlZUVNzV4iShwFeOBYhjHx1K1dCzimo5Zat1PtqktgftyY99c-1sib4Z5NZNY6jaT3LQtN6YK_FkhuJhb8n6M98vQswEjkbAWLqatMSeIvGxuXnGS9FU_MKNGrVan4hT78hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b65f43b16.mp4?token=us_RapEE4cYsU0szxaGyrrtEhjzfJ1HpjLO5_nCQmpm3z8LAATNlWHC9WqLjqB_4DDKvGggEuJ2G15vXP6CzojGdFgYSjlwWj4MufEB0dTptZRuqY8XhS2G3vABN_8kTU79WWNj5FKfQvr9UGrGqpy9ivQd1cQ2oVCwKTcVMJWyYuR3xe3eGDAHgVlZOViBK6xLdnLnZ3y89Y6DxaNRlZUVNzV4iShwFeOBYhjHx1K1dCzimo5Zat1PtqktgftyY99c-1sib4Z5NZNY6jaT3LQtN6YK_FkhuJhb8n6M98vQswEjkbAWLqatMSeIvGxuXnGS9FU_MKNGrVan4hT78hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🏆
خبرنگار: «ولی تو در کنار کلوزه، بیشترین گل رو تو تاریخ جام‌های جهانی زدی؛ این عدد و رقم‌ها برات مهم هستن؟»
🇦🇷
🎙
لیونل مسی: «نه، راستش نه. واقعیتش اینه که خب باعث افتخاره که اونجا باشی، چون نشون‌دهنده ارزش کاره؛ اینکه اسمم کنار کلوزه باشه یا اون بالاها باشم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94199" target="_blank">📅 16:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94198">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2d6b9ef8.mp4?token=aDW4qf-euuz9llkwIFwB0ep0HZ3zPqnJyFs27NIL5cBAcFmMtFhwOwcqEQx8gRIysW81usrpjBy5lkrXa-Mh_IxJOo57IL1snCriLSgSePceiPtoSisG8IHndKxD_5YLqS_K8y_YFr93jbkbQJmWUVB49fc65ciWKMbTy0kr-uR_S1geeQFeKqhQ_2FyhTMUv9LH_JZszhjflFzUCtddtxCEvwm_UrFy3NHvUfNfz9A36g11oYNNJH3evLuw5_nju7wD5E6gotOXvTYXaUiYsxpC5z7gQLqRfy4FgvIMUO4TqL-B_KC5H_qUgSu2ZyclUAMkDoze9UfYdpD1q33uL2yrrW8E_AVmDuiJqYXNJKiYZ6vKM1Zmk6VJl8zAAoBKNX1N2dWPEVp_MeqWOIseEYOwEXcC7hhjOJi_HWyCMWbrkD0yeJxALDEaGN-FInw5cft0boAAD_L1ztUpciti3OVnryYKgW6m1AEjSWcpJmD3JqneVxUyuL92csBYgET5-hVF-b8iGl05NKmZt2Q76Y5_Ib6XMuXbJv_zzSL9MtrGFTOrJjnelO-TlYW9Ay6xgnUKoD47xgZ9_EInMePXHmNEBczeXGKV4qOOVDl6nbsKjuqoY-LE1ZzLVZAC78Ow-C_BnCMif17wk20TeLkrcEDWQ1m8bAzsh5VwksUMD9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2d6b9ef8.mp4?token=aDW4qf-euuz9llkwIFwB0ep0HZ3zPqnJyFs27NIL5cBAcFmMtFhwOwcqEQx8gRIysW81usrpjBy5lkrXa-Mh_IxJOo57IL1snCriLSgSePceiPtoSisG8IHndKxD_5YLqS_K8y_YFr93jbkbQJmWUVB49fc65ciWKMbTy0kr-uR_S1geeQFeKqhQ_2FyhTMUv9LH_JZszhjflFzUCtddtxCEvwm_UrFy3NHvUfNfz9A36g11oYNNJH3evLuw5_nju7wD5E6gotOXvTYXaUiYsxpC5z7gQLqRfy4FgvIMUO4TqL-B_KC5H_qUgSu2ZyclUAMkDoze9UfYdpD1q33uL2yrrW8E_AVmDuiJqYXNJKiYZ6vKM1Zmk6VJl8zAAoBKNX1N2dWPEVp_MeqWOIseEYOwEXcC7hhjOJi_HWyCMWbrkD0yeJxALDEaGN-FInw5cft0boAAD_L1ztUpciti3OVnryYKgW6m1AEjSWcpJmD3JqneVxUyuL92csBYgET5-hVF-b8iGl05NKmZt2Q76Y5_Ib6XMuXbJv_zzSL9MtrGFTOrJjnelO-TlYW9Ay6xgnUKoD47xgZ9_EInMePXHmNEBczeXGKV4qOOVDl6nbsKjuqoY-LE1ZzLVZAC78Ow-C_BnCMif17wk20TeLkrcEDWQ1m8bAzsh5VwksUMD9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🏆
🇦🇷
حاجی جو ورزشگاه بازی آرژانتین رو‌ ببینید. ناموسا چه‌حالی میکردن با لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/94198" target="_blank">📅 16:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94197">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb2cdbc7c6.mp4?token=UVEhOSlevnIYxKozqRpexFc3V2wzMwFq0zl0BEaUPBZyr5tXAkRzAzttTqQJ9ou875ac2mGPOgSHZCWAvvXOkCD2wQVDAz8Zw9NRyyTjwqdgfv4PE1K1vW775F0qMOXVSEvBU_agp6-1JyhGPIi_nC-s0cdgiEIBrFr2cdgw_VpC1TKr8LJBRm_zmjPrRhLyt4cgHxGrezD2hTMneY2dOT94H84Tu5PlAI7evfiv3Y9hMqnQo0b5LQSaVJNp53s323el84oLmnayxLVc19fBxx4hguezEdLLF4dHo_JgBO04df-8u9gI3FycFxfJRFQXSFGLl0ryxM4H9HE_vjbEKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb2cdbc7c6.mp4?token=UVEhOSlevnIYxKozqRpexFc3V2wzMwFq0zl0BEaUPBZyr5tXAkRzAzttTqQJ9ou875ac2mGPOgSHZCWAvvXOkCD2wQVDAz8Zw9NRyyTjwqdgfv4PE1K1vW775F0qMOXVSEvBU_agp6-1JyhGPIi_nC-s0cdgiEIBrFr2cdgw_VpC1TKr8LJBRm_zmjPrRhLyt4cgHxGrezD2hTMneY2dOT94H84Tu5PlAI7evfiv3Y9hMqnQo0b5LQSaVJNp53s323el84oLmnayxLVc19fBxx4hguezEdLLF4dHo_JgBO04df-8u9gI3FycFxfJRFQXSFGLl0ryxM4H9HE_vjbEKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلمبیا با این هواداراش واقعا شایسته برد و درخشش بود و هست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94197" target="_blank">📅 15:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94196">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7zzqnUQ_Lah1IH9dsFfXvBx_iidVZtFvrle-ZIqx5B5lY39ur5ccgNXdjM8b78srptD9y42-07FoqnEwvT7N0JSgbXgVlGgjOk32I0ulImojmzdRZZ6j90xmCNE0jaHVQxdJlYKqyNDcWjNpGiy0_b_culWBgmz381RLEOMpeg3lyQvz3Et5Ci8zuuCIlRN1gaNvjuKvHfi2m9d-kmgE5yooXCOUyrOhpfEmF57gjiAhhgPC0ymfJ2B0RFBAdNBP5NY4HpAUQc-ks_EfY00nwW4GIE_AhtOzNuHE838FJCG1l2GYCLJSlYTgpJBUKJpgHh5aQfBDeTjfU1P_xHS7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
به گزارش موندو دپورتیوو، مارک آندره ترشتگن و ایناکی پنیا جایی در برنامه‌های هانسی فلیک برای فصل آینده ندارند.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/94196" target="_blank">📅 15:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94195">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65efc6e80c.mp4?token=NQ2DaTHsuSLyKAYIUQJ6bvIjxvYaVHqyQdeiIGuwgAmIBPkV-GFTUMKDUJREMKCKCn4A5fBHC7OkMmzGOjPlezp7z0_tEtkBxE3LV6lqqeLd1eyVTko5RupD1P5w_RiAhnyIZEzs-5-FnycWZVeHe6IgY4D5v6SxdEV2UuVHk3ALFjADrDW1YGrYQQMPHTrfQY2_XKf2OZCKWMnfzzc-3tpFyjuAGE2fLtsfvJmLds1vMcUA3XcrcCmTKFx9fR3uCpUJMZYz92Dwr2ZVi3Awkoh6nglKvza74bDN_PlQdw5xpyP00I7htR0mqk19-BWiIi-Xzqk-uIPMdQWPLtEomQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65efc6e80c.mp4?token=NQ2DaTHsuSLyKAYIUQJ6bvIjxvYaVHqyQdeiIGuwgAmIBPkV-GFTUMKDUJREMKCKCn4A5fBHC7OkMmzGOjPlezp7z0_tEtkBxE3LV6lqqeLd1eyVTko5RupD1P5w_RiAhnyIZEzs-5-FnycWZVeHe6IgY4D5v6SxdEV2UuVHk3ALFjADrDW1YGrYQQMPHTrfQY2_XKf2OZCKWMnfzzc-3tpFyjuAGE2fLtsfvJmLds1vMcUA3XcrcCmTKFx9fR3uCpUJMZYz92Dwr2ZVi3Awkoh6nglKvza74bDN_PlQdw5xpyP00I7htR0mqk19-BWiIi-Xzqk-uIPMdQWPLtEomQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
کف خیابونای بوئنوس‌آیرس این نقاشی و بنر درخشان از لیونل‌مسی رو نصب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/94195" target="_blank">📅 15:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94194">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuzXgoPGwWq17PTyZV56_csMUTWYJX1OWhM7s4_iLmQNk6jCv9RpsCvN3oc8frNosVwQq7GDrw3r882bvnvYpnd7RfPV9qfV4A8vX1cB6t9b6g1QvLWJ84arOPzKSWKqhAZOp-t0Ebryq-FX9W1NWb8QncZAK5VRKkMMcTiKt6tqdOf_CnfPsuxjvzsHqqKtKa2ECFRm0KuA0kzVpDt1Eb2bWhPkcMDrTY-zqc2QTf1EtqbuXCmIquWmDSm11NFSKqOKLACk-PTkw89Zt-OTQ8kxTYjI35jNympmpHoT-kwaInL54sspGV36RXVX3L2tq3UgTIGKJNk_RO-q4_Hfpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
خوزه فلیکس دیاز: ادواردو کاماوینگا اصلی‌ترین گزینه خروج از رئال مادریده؛ هافبک فرانسوی مورد توجه چند باشگاه پریمیرلیگ و همچنین پاری‌سن‌ژرمن قرار گرفته. البته خود کاماوینگا به هیچ وجه حاضر به جدایی نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/94194" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94193">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/94193" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/94193" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94192">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jinlcn4xetDLA6nEkKH8Ssr95CpnUjZ3A66Y_OdTHUBUumfw54R-Yp-wjLpYfEdnpvAkK8LXySlGAl4UQ3C2WWTEZc5wthCSY3r1QJk1PjtMZJofaKF43mxuOpICr1baS354PhmsAxo--6hNj0E25coJinPuzKhxbLsfWkVHxjnpVzma7SV0uNu0AGmkI4TYngbsLkakiQkPL3v7gNp9z7p6cIegTokr8oGCHAtzgZNndijRMkECYFvvZ0TT2TfkPfqx2KdWECKzP1rva6Vks16lk6_KAvj-OcI7NSm1LYFPVej-umNFrZ5v27ogcwuDSxpW7yp7SN1C_vHJbOcP7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/94192" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94191">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BY_NMAnjVLKnuqTBcnFBc1fnc8ld8E9Bz_nphrwPf90-T8GEy0s2zfOoi0Jhut7OQFJ7pbtBcgIyr54bMubljvmLZCjfDsnojlaYyNUL-WI0kOBb1_x_r1rXDxB4nvNZFFH1sAeTmsriNzpB-nZWiEbZyaihnubfziw9Du9Nren5ZjNRuKkZ1sKYd-WAR8W5pEJJTyVutkRXemiiB0w4gDES8vEfYlGJdSaHpXdTNYXrp7dy4eVopOP12574I4TYnmhNHSPwYkpE4PKiH1d-WCU2R8PEADuc9qqjbmSxrbvOTvOOrJmCI1qL8PpiAEhjFmrI8eZaYPj015F56-MEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
خوزه فلیکس دیاز:
ادواردو کاماوینگا اصلی‌ترین گزینه خروج از رئال مادریده؛ هافبک فرانسوی مورد توجه چند باشگاه پریمیرلیگ و همچنین پاری‌سن‌ژرمن قرار گرفته. البته خود کاماوینگا به هیچ وجه حاضر به جدایی نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/94191" target="_blank">📅 15:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94190">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozncJUc5-kN25-n1CFxaJtaZVDGgzRfTMcskAeNWmQnQzglDpj_MLw8tTmjUYOakaFmtsmL5vQ0iV8pz8Lvspr_3TWS_v4Hh_Z0b8blD-Gu1Rz1Xha_y0JUhKRyvCuzYXx6DKlXtEa2535Wo8erWv_RMYJvA_nxeoekwFn_d0R91jx8K83etaIWhwDWT9kJWqRhuSwnGnJ9HQWVbSXF-A3kzs388iwCHpD3c4UGOGgf5ver9H7XOhhjt9K1BGO0X2SknW89EFG0YTB6kGlmf_5AgVZcm_546T-kVwHuEsiQea4A7hE3NkgCFI6Bn8BLlfyoFi6eRjXQaRGFjqbInQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🚨
#فوووووری
از رادیو مارکا:
فلورنتینو پرز در حال آماده‌سازی یک حرکت بزرگ در بازار نقل‌وانتقالات است. گفته میشود رئیس رئال مادرید روی یک انتقال بسیار بزرگ و جنجالی کار میکند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94190" target="_blank">📅 15:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94189">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFG4dJi8Bns8mP204Ea8Cbj86H418txq9YC_5L4LRj6KSclnDX7vT6uqk3tQrqzZLz1yTbwm2nvrIw1V3nHXoGOjdiXPl15xp6r8xLlgwS4kCzaxqti4G0RxJYf1eKA3ksywceJXsWKJ7VXZIAgP3BDz-RXDE8v_olOOfQR-qxnV3tS8x2Kl9MhUB8XluFRygXXa4n1Dd8HBpMSHy2Pd2LMPaMV_37D5Q2tBxacoqeVHwY5X4LvvIYNhHSMnlzIxqChtqI2IupIApsdZ9ImkRSFKni5ZK8x2TQvw1kJ8wiqS3VRa51uoiPkaHaEcYBSbQlcqRqqzLO2C15K3ENHCHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🔵
بارسلونا از ادکلن 75 دلاری خودش رونمایی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/94189" target="_blank">📅 15:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94188">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZC7PckTcle9HeNbDUm4Hh8O5jDZUfIhdgZux-N1bmyokEq7qFfr4zQmhX_HDEnNOtz2NHO5TPTGB6-tesOsUYrWJ0fUWOKDPhdDXfkhWL1Tw0KvZaAMuNHZ1lBi_1LvQTTpzPUHiORttbdWtYbSOzvNw80V89enqTrD2AM7ZbFQ6-L9Yo4uGyvgFJfDcpYPRHxyR6MDMd0kCcy0ez9KXsdc9M_ftCtQKufxBdRJxgAu0hnqDuFRuCUEEVjmozOMXAxeaK_Qpm6Yfb2fYU0vyOSsSeJk3V5JDti5yFaHDxzuZSM0U_YAEGwYmYjZkYPnay11O9Jg6cUP1r0K_MXkGuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🇦🇷
زوج آرژانتینی بعد برد فوق‌العاده کشورشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/94188" target="_blank">📅 15:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94187">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrRmT66duP24SULRwmDIZzij14DbOfzEfKnXLCg6dMh-J3EBbTkVTxNZHuqdh4S0YTw-KjsMfazIOrM1o9lH2pLRK_OwsFCV-onIbOhHnoEdpFg3eRvJKx1-Ashia9cRhDh8mRDZeYw1e-8IwMlo2ZrhhkxPcUO8n8AyP3y8dey_mK3rb491BW2sZqbRkMvZMkUn3XKvvGzQqVST9FHL1_-BxOGzaNJ4O4kq-xuY_YrywzpuFgcEZ_irvDpmncaWFSI49y8vktG0rbOtuZDU61kBPGmDRgKAXWwHZ0UCUeDVpPdXO1cuzmL-__lffzTVtIyAb-PrA8qfIrIoO01Oyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
آاس
: رئال مادرید استعداد مراکشی ایوب بوادی را زیر نظر دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94187" target="_blank">📅 14:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94185">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BUR_IpUeR35lp260hgm1G-HiEsASFA5Cd-ccry9Up6RdGRepovi4PXKJb0sRkBVXqa_9GtIqFqq67TRR84J29r9bx9sERddK6wol3pJn_-11QTnRVZI8IDl0eT6L9xdzp1kdeVVkHfDD3rzXYaVtDwZmJy876hvaYsczwz0LSgpphhzz23hicZ1_2Q7L9JXSwqGIF3boua09aGrZXm2fffSBmqzn-xwuYGkFN9Jf6Y7aFRtWqkrIohYK7boyytyvfD4c3-L2OwtCCzH9r9wvjpP2kAdgYgevo0LbZ2p2W5m1PmgxWH70oIzJRCKUcmdNgh03oi4dKY_xahmPYLcL9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rch99HdHllO3dsx81m_Cl9OKHTyUn365ZoLBCO6xt5WM2Dr9gJ588hBlJ-ewdg09wNLvB1vPzX5E-TCts1CTR9tMk_2epv5lESGtYMVFeu746QaKBdfIkWfHcfM1xvRsgYns4Ly87p6fYTI88bBCnirERlKvdIIGAaOmd-SXwElSk34UvF19mb-PgnIWWfievDt7Bqaw9YMJtneb4FRb4q0mEDWL1-T-dbaWzYs7RuXLzsJyfWKGdrVp2V2lY3xXobi_L0G3nk5PvI-hxZ6-IVTMvDxpcsex-2_mG5yub9IKAURQKXnlHgT_B-h9mTjzK1WjlYPq5epEG3717pRo_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🚨
فوووووری از آبولا پرتغال:
⚽️
روبرتو مارتینز رسماً سرمربی باشگاه النصر شد.
🇵🇹
ژرژ ژسوس رسماً سرمربی تیم ملی پرتغال شد. اعلام رسمی از سوی النصر و پرتغال پس از جام جهانی
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/94185" target="_blank">📅 14:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94184">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c54bbd91a7.mp4?token=SV74HpkFrHAgy2QP-X29frnKLn99DKark5LuhkyCqWujyXxw85syz7nTiqAytIgkw1LlMjg26Q4reFoxbTN8VZlGFWdZBpQkVkzA3pv2tIp6V9lnw3FkU5aMMuB08JB6MnybU5c-S81-tfSwugaylnFfl8m0tzbp8C7ICUtzG-N2m46h8QJLCy7qdaoetv1z2nGRUnbBWv4vR1tQ5yQpyTDrzhDPwWUwQx_rc1JpnPBH_PrH2M7RZfBOyjQtLlZfYYx7E6Bh1eDvp4jJA62NSOxD2bbP0IY63vXBtnx2mRRiRaKeOxLdYHquLTjRfTDRZSuvUsADFBfWQBSw7oTQzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c54bbd91a7.mp4?token=SV74HpkFrHAgy2QP-X29frnKLn99DKark5LuhkyCqWujyXxw85syz7nTiqAytIgkw1LlMjg26Q4reFoxbTN8VZlGFWdZBpQkVkzA3pv2tIp6V9lnw3FkU5aMMuB08JB6MnybU5c-S81-tfSwugaylnFfl8m0tzbp8C7ICUtzG-N2m46h8QJLCy7qdaoetv1z2nGRUnbBWv4vR1tQ5yQpyTDrzhDPwWUwQx_rc1JpnPBH_PrH2M7RZfBOyjQtLlZfYYx7E6Bh1eDvp4jJA62NSOxD2bbP0IY63vXBtnx2mRRiRaKeOxLdYHquLTjRfTDRZSuvUsADFBfWQBSw7oTQzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سباستین ورون، اسطوره فوتبال آرژانتین: تیم ملی ایران خیلی متحول شده است/ فوتبال ایران ظرفیت پیشرفت زیادی دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/94184" target="_blank">📅 14:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94183">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f86cfb3e2d.mp4?token=iGpIdNH6aX0mF2wZ2pXpvEZ71iGub54P_DFQN9Y6WgFpF8eXeB4DtChUT_A3JBn40gCbm4tBimA3a9cJlXxDLr2rh485daotPrxfN1sdJDXA0VY7GkYftcA5Y2E0d0utDgs56dDsqHgzvey4R2-rozYZ5lDOKLwcuirqe9FTsgHAjUo0ePGbjvSr1XscF0Meuz0CshWkHuedpjTibzv4fkjOUhg-6r1AffqIeDwfsmK1GApjhH5EUBkpH6n13H6k4tGNjIZwTzh7JLR6sGN2WwCmKn_phuxPeZ_lmJDo-MeNQgleG3seokopYN4fnGRRc6QTDJhEBVYZdf9Siwyr6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f86cfb3e2d.mp4?token=iGpIdNH6aX0mF2wZ2pXpvEZ71iGub54P_DFQN9Y6WgFpF8eXeB4DtChUT_A3JBn40gCbm4tBimA3a9cJlXxDLr2rh485daotPrxfN1sdJDXA0VY7GkYftcA5Y2E0d0utDgs56dDsqHgzvey4R2-rozYZ5lDOKLwcuirqe9FTsgHAjUo0ePGbjvSr1XscF0Meuz0CshWkHuedpjTibzv4fkjOUhg-6r1AffqIeDwfsmK1GApjhH5EUBkpH6n13H6k4tGNjIZwTzh7JLR6sGN2WwCmKn_phuxPeZ_lmJDo-MeNQgleG3seokopYN4fnGRRc6QTDJhEBVYZdf9Siwyr6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‼️
⚠️
پیروز‌قربانی: با تیم خودم فجرسپاسی از این تیم داغون نیوزیلند می‌بردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/94183" target="_blank">📅 14:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94182">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtXBiJSo4BcB7O-B-unKMgbrDcnzdgo7i01JJoqbTpbKpi5hCWTlBZf-P2DIhg-Cip7Qq2QVPAwOESV0kWabjBE1AE5aKrFf4NgKyoecBnWYHcuoVAy2LRFKXRp0EmHhRVSJ_wtPd_7yhIHgYHeWgMSW9VGs2dd0QtQydJ0bH-3xfepVV0QYvWh8R5zJaeH2uldqtQlrXYxehJk7FhMC27qZDkE__iynlph-S_wLYb8YwrtNamgTy7RNlx-kBIBA4Zkop2i00Zcc7sH4hYnQeUvj8un673zoSCl7AK7B83BSCoaA8-4kSqgX5rndoX2xPThQdB2mwcTOOdCibeyj4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری نیکولو شیرا:
رئال مادرید آماده‌ست یک پیشنهاد بزرگ به چلسی برای جذب انزو فرناندز ارائه کنه. بازیکن موردنظر هم علاقه‌منده چلسی رو ترک کنه و به رئال مادرید بپیونده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/94182" target="_blank">📅 14:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94181">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQa-Z3s5ECzom-5qtIDfEC-1PmNl1UHzru7KoMN4EaXxF7jiTppPBCYWQsC-MudfDcIxSg4JgvJOr7yBlXNx1_REGgzUA_L0fP9FCqQu7IAoec0mlAkOQk-fv4TwkclnlaB_eggAoIqFIYw_fNwcpJIsTIj-Ljuq8kmXgXD2OFwiy4KJHHGIwwbimkJiWJrbWaGeiHgre4on89OO7EwzP3YjyGVcXZLkzmcpsPPYyJ0efoHI1IlGvWv-T9efNgT3ZZn5q7XyrmviSj58RK_x70-7V6S6re84FfNtQlIV0Kx4nbb2zu2R_iV5lwYQ5p7PYfz4IGMO5_VJ54mdJQfeRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇳🇴
📊
عملکرد ارلینگ‌هالند در کریر فوتبالی خودش بعد درخشش در اولین‌بازی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/94181" target="_blank">📅 14:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94180">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9087c58782.mp4?token=INUR9gCYa3m2ro3EHadeoaj18ywf_48FCUzFTy0uraogD5TtS5E9HRLvsTi0yUE-S0tDbG0bB1YSk5SqG7o5vZAeyTTzuKldbARLVcLy-THldWwcvhObQVcy4mtjpCTxMmqVLj7IriMGHxSuAdJ5vd9xSg1Jf8UUOmUaN95RgZ3l2mMm_3E4be-xhH4gmNOFFAEVFH-_6UT0T0sfCWQrdeBm0qo5oBUhTaaGJO7oodq730169U2BLNC6Rz6JKhx_tf0sMT-pgxY5vPge6si1TdJxGMkOK8GFOmNeWZxxu5SEseBRN_5grUkRJHZ2dWSNu3K5ewGt38_BmcLzFw3RwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9087c58782.mp4?token=INUR9gCYa3m2ro3EHadeoaj18ywf_48FCUzFTy0uraogD5TtS5E9HRLvsTi0yUE-S0tDbG0bB1YSk5SqG7o5vZAeyTTzuKldbARLVcLy-THldWwcvhObQVcy4mtjpCTxMmqVLj7IriMGHxSuAdJ5vd9xSg1Jf8UUOmUaN95RgZ3l2mMm_3E4be-xhH4gmNOFFAEVFH-_6UT0T0sfCWQrdeBm0qo5oBUhTaaGJO7oodq730169U2BLNC6Rz6JKhx_tf0sMT-pgxY5vPge6si1TdJxGMkOK8GFOmNeWZxxu5SEseBRN_5grUkRJHZ2dWSNu3K5ewGt38_BmcLzFw3RwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های زیبای دکتر انوشه: فوتبال و زندگی مثل هم هستن و شاید دلیلش همین باشه که ما اینقدر فوتبال رو دوست داریم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/94180" target="_blank">📅 14:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94179">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oayXOoN7gb6xAzWp2F_fC9dGntvcBgkxGC7dDLVdvzimlCVVgq7jtYUGvK0mHLpYhxgAwUizZUnwAZs1CBA3Z58epH6KLcSvDKaguQN1-GUlz5TSSohRlDcIrXTEDDFPKR-PCKkQp4Kw6GECQ54WovhzSyzsDzbsgfLGbQbhLhBzXURMuBXHKHryuo9nW-fTHgmZOB5aar6D0pA4w9MH6YCri0E_8e8KrEcOGkoNDVmXE3TLctUDAzPconp7WiU7wYeN7MRp7bm8ztFRr5AbqDqPKiS3SJpy82yGhDeFswTYMhxkfNiHi_75tNEI2BXbNg3jnjKvaazMj8kQ4ykATw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پستی که رونالدو تو اینستاگرام لایک کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/94179" target="_blank">📅 14:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94178">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39843c046d.mp4?token=TQQilmVndwmBQEcUnBcojWZLv6KRoW-F-TTGDoh0QcIoNF1SwsFyc-p5cE_Fc7cHQj-Nu_4Z2ajnAZwTNtZFJ7NzgvvVKNTL_u0pqvKegrCzQCzRXRKAPhUqebf8Pwzbs2C78qXaAA6iu_iCKxmgaXcVN9CgyLn3DTPgKS548E7VkCyfYIq0KWSqEHDhHlnX3mH8ktbcVuf7hBlEYOUSy7wU0EiTwf9ay-VKb-zJCu0k9ZrGDMJMdag0IUYeL1mi7BnNc1nWLP_rWz9jtLw8s2BWYhfKfAU4c_xeKeN9ZEGp9YERRS37S5wWlG9jfC80jWZgYD-VnG2wXqU6Y9uPpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39843c046d.mp4?token=TQQilmVndwmBQEcUnBcojWZLv6KRoW-F-TTGDoh0QcIoNF1SwsFyc-p5cE_Fc7cHQj-Nu_4Z2ajnAZwTNtZFJ7NzgvvVKNTL_u0pqvKegrCzQCzRXRKAPhUqebf8Pwzbs2C78qXaAA6iu_iCKxmgaXcVN9CgyLn3DTPgKS548E7VkCyfYIq0KWSqEHDhHlnX3mH8ktbcVuf7hBlEYOUSy7wU0EiTwf9ay-VKb-zJCu0k9ZrGDMJMdag0IUYeL1mi7BnNc1nWLP_rWz9jtLw8s2BWYhfKfAU4c_xeKeN9ZEGp9YERRS37S5wWlG9jfC80jWZgYD-VnG2wXqU6Y9uPpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇨🇻
خیابونای کیپ‌ورد بعد درخشش گلرشون جلو اسپانیا یه نقاشی غول‌پیکر ازش ساختن و فوق‌العاده شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/94178" target="_blank">📅 14:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94177">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">امضای پزشکیان از نزدیک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/94177" target="_blank">📅 13:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94176">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnfP0laITKTpVjDO_3Dve7OkJ3g4df20eXs3wklvQXDsThri7hByY9ZpKEk47oM-pQkW5UaOEvjTUfmtRWyXFntrgF3FIfPhzn1ebBn-E1StVDwr7-BcCO5RaI_7iCKc-DcttQUwDyAzcpEPPSyhLo42pGeF6uDoBQ9VpqhfB4KV6VaQ9fwL7tzVfL4NotNjzFmbknMs3g3_QENThGKamKJd_JsK9NjtRxzif6V6hPxrmsAQtsEfyx7HBxUyalSWLwJC86e08IA2H2kU91-gJ7ErAX7NAMTFuYQk-UBwspfeZwJK5GknD2bC69s5WutqZXG5Q5dh0JCE_trV6Q_-IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
سه‌گانه ترسناک بایرن‌مونیخ:
🔺
‏اولیسه: پاس گل
➕
بهترین بازیکن زمین
🔺
‏هری کین: 2 گل
➕
بهترین بازیکن زمین
🔺
لوئیز دیاز: گل و پاس گل
➕
بهترین بازیکن زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/94176" target="_blank">📅 13:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94175">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6df6576c1.mp4?token=beMrO5vIvEazopbUgIkpZL04lXDEMkjewhuEA7ecCqSkLsGr5aBicCNN1QPPIhwJVv8B8ViGRs-Kv3QNYvKbZwzwj1fCG5MSmCxYBF1OxElFf4UBtzFHZZRntm41zIqETFIip5Z7AM9-vAkuzrdIuPn57h6oJPsTx_RfH2NjS6d0m4FqwHk_qlGJeJXJnIMQUr43G6kL3crYTpP5ObQ8-0EBYkZ6S9BHc8b5dFQ0STEJAKSZoFO9AohbYIrhwk1MiUqbPL6hDvPbbQU11veWSNTjRMiICpoNsOST4Z34v_4ndaunfxpB4gSrejz5Et5nGRFX53cPhMMS3u-3kMhDeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6df6576c1.mp4?token=beMrO5vIvEazopbUgIkpZL04lXDEMkjewhuEA7ecCqSkLsGr5aBicCNN1QPPIhwJVv8B8ViGRs-Kv3QNYvKbZwzwj1fCG5MSmCxYBF1OxElFf4UBtzFHZZRntm41zIqETFIip5Z7AM9-vAkuzrdIuPn57h6oJPsTx_RfH2NjS6d0m4FqwHk_qlGJeJXJnIMQUr43G6kL3crYTpP5ObQ8-0EBYkZ6S9BHc8b5dFQ0STEJAKSZoFO9AohbYIrhwk1MiUqbPL6hDvPbbQU11veWSNTjRMiICpoNsOST4Z34v_4ndaunfxpB4gSrejz5Et5nGRFX53cPhMMS3u-3kMhDeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سباستین ورون، اسطوره فوتبال آرژانتین: اگر مسی مصدوم شود، آرژانتین با چالش‌های زیادی برای ادامه جام جهانی مواجه می‌شود/ در ۲۰ سال گذشته مسی نماد آرژانتین بوده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94175" target="_blank">📅 13:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94173">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33819b4cf6.mp4?token=My8eORNCwS4hBL0TmibUmTo82CATIfAbX-dv9Cjr_iC1QbMC-E3-vTmJtE-3xO5O4p0t0ejRBRLGtt3XbFc5WH6KcAyD9eru-BmkmHqph00BiaMGnF_Ah_aSLobYgB1qlk8NrGSM-OzKpkYTvfDl-aQvifrW69XbZHWPME-9VDhaI15n0OYyd5kQ8qbzyk3DQQY_E4SgFKfokLZfLrtIwB53G48hIw3LDbfWcOUc_ju4dEmETpD31fAd7Rp6UoTE1rArH7uxScHrlgF9QfvbRql9TDhSoWp6LCHBtH6Tvfmah0a0XKZeEm9Zra7m2YE86lNX_peC0G3ShmTkiWbmVol1sdWj8kuhIWvmBpdAN0yol_3z4V-1bJ7v7iUOq4x0idjjkDdJLCq66Mo24p1EIpxB-Yzurkwz18-17i4nyN0fLOCZ8Ptyo8Mh084yfK-fzxfSCl7m1do5Ey2-ZzrgvUHS1ob-WvTGvYzYy0HTAssCBWe09PKWrSIFVO4aUakFEVud5tOPwUDKl-vA__iCbrLp7dua87VJIg45C2UetvARIhT8PshCtBal-rF71uFMlVqqr6ikC-LfwN8BZUOsmYOnA8w5QCjZzZ6VzUUx85puGQOJXvrDjIMr8vTRg-IvAkRUZYZ-urPuOjthQGBFqhVp2tDme8AZ8n6DBEIS-Ak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33819b4cf6.mp4?token=My8eORNCwS4hBL0TmibUmTo82CATIfAbX-dv9Cjr_iC1QbMC-E3-vTmJtE-3xO5O4p0t0ejRBRLGtt3XbFc5WH6KcAyD9eru-BmkmHqph00BiaMGnF_Ah_aSLobYgB1qlk8NrGSM-OzKpkYTvfDl-aQvifrW69XbZHWPME-9VDhaI15n0OYyd5kQ8qbzyk3DQQY_E4SgFKfokLZfLrtIwB53G48hIw3LDbfWcOUc_ju4dEmETpD31fAd7Rp6UoTE1rArH7uxScHrlgF9QfvbRql9TDhSoWp6LCHBtH6Tvfmah0a0XKZeEm9Zra7m2YE86lNX_peC0G3ShmTkiWbmVol1sdWj8kuhIWvmBpdAN0yol_3z4V-1bJ7v7iUOq4x0idjjkDdJLCq66Mo24p1EIpxB-Yzurkwz18-17i4nyN0fLOCZ8Ptyo8Mh084yfK-fzxfSCl7m1do5Ey2-ZzrgvUHS1ob-WvTGvYzYy0HTAssCBWe09PKWrSIFVO4aUakFEVud5tOPwUDKl-vA__iCbrLp7dua87VJIg45C2UetvARIhT8PshCtBal-rF71uFMlVqqr6ikC-LfwN8BZUOsmYOnA8w5QCjZzZ6VzUUx85puGQOJXvrDjIMr8vTRg-IvAkRUZYZ-urPuOjthQGBFqhVp2tDme8AZ8n6DBEIS-Ak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
▶️
انتقادات تند پیروز قربانی به امیر قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94173" target="_blank">📅 13:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94172">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EX-VUAPysH_Wv-E4VrgBSj9IivQxFv-iIjmsRS_j-F8ofR57_uxxyW1w89OOyv99kL_we5Gp098Y3GC6RvwI5iEIqJbuu_cEZq8_zyPUoy3CrFfhVyzY37RiEHPIiivvJHIyAkywwuEuIFJelOJzp_3zd_6MN_bzqWj12HfrSHqu49lRUmDXtSCNBeaIOsql6a-nu6qyy-R6LYIDJeNYmNqz6v_8fgF_LACQjG1si-hZAfTI_MqmS87qucK4EcstV7TyIvZr6bPgwHOTbDW-5E1XYnMuWAvdfUmnH8srCZwrArd6-wv9ssNJ5olMLKkfKyYE_INyTDfMJjpaDE9ASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
خانواده لیونل‌مسی WC2022
🆚
WC 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/94172" target="_blank">📅 13:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94171">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb6168a2a.mp4?token=NvtaSGzyhTx14hNrxs2LgUyfnDhgtbLAZpUSnvnm4IyhulnvAAEdQwSh9-Lzn7OGFMkmPv_sdI5xwyeZoOgEy3KqJBXvKkihqRm8AUqPhIt2gTPeC-3L9Lc0cf2bAyg79H5uCnZSKubQpFO-_qepLwb-YoiEZrwKXquamuEv6oODr5e15u9aMxSn9wZXXJCr3RBzaD4RC2fBc3Axyh-xBzGDUMWUnjsR9ljrz3PdNsrWnDlPthVTDvX-Ws2MDwVvEPFNICF1ymhhK3hCHoXfflyd4Y755oMmK7y3vz1pBJZ2e98RHd0WpDLqynsHPgF3NHN2e8KaD0KUhQByJ-G8zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb6168a2a.mp4?token=NvtaSGzyhTx14hNrxs2LgUyfnDhgtbLAZpUSnvnm4IyhulnvAAEdQwSh9-Lzn7OGFMkmPv_sdI5xwyeZoOgEy3KqJBXvKkihqRm8AUqPhIt2gTPeC-3L9Lc0cf2bAyg79H5uCnZSKubQpFO-_qepLwb-YoiEZrwKXquamuEv6oODr5e15u9aMxSn9wZXXJCr3RBzaD4RC2fBc3Axyh-xBzGDUMWUnjsR9ljrz3PdNsrWnDlPthVTDvX-Ws2MDwVvEPFNICF1ymhhK3hCHoXfflyd4Y755oMmK7y3vz1pBJZ2e98RHd0WpDLqynsHPgF3NHN2e8KaD0KUhQByJ-G8zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇦🇷
🇵🇹
صحبت‌های محرم‌نویدکیا درباره تفاوت حضور لیونل‌مسی و‌ رونالدو در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/94171" target="_blank">📅 13:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94170">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3720508738.mp4?token=gvRLwlN5jjP9bqmhqXYs1chIh090AiI6WppfoZsGrnPcSm_5WxxrmMUYNEinTjGjU7g7rxIKWUuuolB-nUW5-5mC6nqJBeBfBRZ1nlhyCFCha7TvYKHR1F8raDPwyU7viGhH8h4E77uHK9nRlnMJ7XNunaMdEDNaHGw82YcNozfwV--VpQCDWvYssW60M___IsM9Q-Q66leyJioeqcsZv_P9OKyhPzgRnF7Ds3WcRAgzkHCEqsUQpnLw8Vi-_FUO3hM7IAxIx4k2VaAQ_yoOE73Br--CSK1zs4onmY3DKxi67oy0ut4s4tDnA5GgvWEDrcvf359bqv4BORT5_tvQrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3720508738.mp4?token=gvRLwlN5jjP9bqmhqXYs1chIh090AiI6WppfoZsGrnPcSm_5WxxrmMUYNEinTjGjU7g7rxIKWUuuolB-nUW5-5mC6nqJBeBfBRZ1nlhyCFCha7TvYKHR1F8raDPwyU7viGhH8h4E77uHK9nRlnMJ7XNunaMdEDNaHGw82YcNozfwV--VpQCDWvYssW60M___IsM9Q-Q66leyJioeqcsZv_P9OKyhPzgRnF7Ds3WcRAgzkHCEqsUQpnLw8Vi-_FUO3hM7IAxIx4k2VaAQ_yoOE73Br--CSK1zs4onmY3DKxi67oy0ut4s4tDnA5GgvWEDrcvf359bqv4BORT5_tvQrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهار نظر جنجالی سباستین ورون, اسطوره فوتبال آرژانتین: مارادونا از لیونل مسی بازیکن بهتری بود/ او در زمانه‌ای فوتبال بازی می‌کرد که حتی زمین‌ها صاف نبودند ولی او رویایی بازی می‌کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/94170" target="_blank">📅 13:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94169">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWbGTARGF3i5EG8M4JqT0VT12Ivv5rhpF8iNtFbDcBTNFvEYwJbURdkq1bPMSQZjTOpcM71Ah_ZWn_SnQVBLx8YwpXBjyj7eYMe4qy4Y6Kz-0ccR2JxNmcIyuM1WifNLF4sy0_D9sR5I73su5eVBy_b2T31jn-O7vy6Q3tL8HZirEqkDgk_QOYwwpd8rrgZ2FEC41gzxAeR9eN2CYtHh-ztjm3wnKYYuSdY-YA3elH4re8rb0EZM4_sOqCJP67ZneJgiwyXw_LYsMgJK_1EC3RgJgadQTm-OuL7DWh8grVbAxVS6BhUv-i3GdUl5XcUAMN2VspmKHo3yveW5fghZSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بیشترین پاس‌گل تا پایان هفته‌اول مرحله گروهی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/94169" target="_blank">📅 12:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94168">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8bc47b42.mp4?token=ifcB9PStvS0ERjq2t0_UTEtv2z-LfIgp8LdLejyHLixUYxN-4x9grlpnQkd-nqCiVKuCcoZOFsXefLhPiaJ8eWzhsLGHTUNq9gMwAuriPTnGyROhTW44MGJFBXoi0m7qXDapHSfy1zler_XZ6qHFyvgce4B6voKoxV-hORkRmjcL9d9ajKDpeJVmXNSyYMqwKfBE5oOyGc8HZYqyCk07eXUXxhZktC6AjulTemv0CmlLnd6ocNBCW9dnkQ1b3ZbopQcOICw6s1dO_ONx6JGqsxjndY4ywT_ImxOhRjUd0KeEbZ4UlgqeUZ4Oxc-c-1-ooDTyOHiE307FP6tyxZM9Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8bc47b42.mp4?token=ifcB9PStvS0ERjq2t0_UTEtv2z-LfIgp8LdLejyHLixUYxN-4x9grlpnQkd-nqCiVKuCcoZOFsXefLhPiaJ8eWzhsLGHTUNq9gMwAuriPTnGyROhTW44MGJFBXoi0m7qXDapHSfy1zler_XZ6qHFyvgce4B6voKoxV-hORkRmjcL9d9ajKDpeJVmXNSyYMqwKfBE5oOyGc8HZYqyCk07eXUXxhZktC6AjulTemv0CmlLnd6ocNBCW9dnkQ1b3ZbopQcOICw6s1dO_ONx6JGqsxjndY4ywT_ImxOhRjUd0KeEbZ4UlgqeUZ4Oxc-c-1-ooDTyOHiE307FP6tyxZM9Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراتر از سم
😂
؛
🤣
چالش بازخوانی نام بازیکنان تیم ملی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/94168" target="_blank">📅 12:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94167">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb354f20c.mp4?token=mEVwG_OBp_WT8kqJFNU6DWkV77PIlt1Z3li-nKOkej2QZ9FrSrCwo6XIYGHNRpn-GvQ8-yodl6NRqpOJLg1v-O3sa1x3feOjT8Zpm-X60UvmQcx7XRD8ZTqlmR_mvKHwGEiZx_pAxy3CKFqHE0q7dMEGTA3r8tiEttIJJTNauscb_KeoL439eCobrTp7EkKrAgvauyxZt5ypqmKXJCiZI1S8uPvGaazaZ0rRX2VB5I9pukEYS7ZuVOa2r__jH_uuOxZJRWEoeHTB_1q7BA9U0Vi6PGw02rR75l6PVQlB4nMRKiC_XwL4VD67Kjbx7Gxqdwkls5iqSACWr10cprIbhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb354f20c.mp4?token=mEVwG_OBp_WT8kqJFNU6DWkV77PIlt1Z3li-nKOkej2QZ9FrSrCwo6XIYGHNRpn-GvQ8-yodl6NRqpOJLg1v-O3sa1x3feOjT8Zpm-X60UvmQcx7XRD8ZTqlmR_mvKHwGEiZx_pAxy3CKFqHE0q7dMEGTA3r8tiEttIJJTNauscb_KeoL439eCobrTp7EkKrAgvauyxZt5ypqmKXJCiZI1S8uPvGaazaZ0rRX2VB5I9pukEYS7ZuVOa2r__jH_uuOxZJRWEoeHTB_1q7BA9U0Vi6PGw02rR75l6PVQlB4nMRKiC_XwL4VD67Kjbx7Gxqdwkls5iqSACWr10cprIbhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهار نظر جنجالی سباستین ورون, اسطوره فوتبال آرژانتین: مارادونا از لیونل مسی بازیکن بهتری بود/ او در زمانه‌ای فوتبال بازی می‌کرد که حتی زمین‌ها صاف نبودند ولی او رویایی بازی می‌کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/94167" target="_blank">📅 12:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94165">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTk2UeFJA05G3oD7EW-aaxYFz8tr_RlDeF-c2uoCeb57XTx0jaUvkQvkvzyQWZn0DlYpHG0VuIbwYau2et-G0R2JNus34bat_Vpw3T5OZJKpV9JTUUAMggc541XeYwO0u9qjkaMTl2vM5owgyb_Y7jFl9SS6RbbqX7aF7dQdJyV9getWzQHvNzeDRSB7LCZ8rKVFG1a0Ja1wApH5pZu68Hij0uOKs2XqrAclnrG2TsWnDb7Gy7rE4ZfJgcCRmjzpkcFTnOX2HMYWJwb5hbDtTBWf7f-xmejAW5lEBaJd27Q2z97PjOaejIaaVy2yai7x-VwGvHzotRmNigZGvZRCkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🤣
تو ورزشگاه‌های مکزیک یه پیرمرد فوت‌فتیش بجای تماشای بازی درحال عکس گرفتن از پاهای خانوما بوده که توسط تیم امنیتی و اخلاقی فیفا از حضور در مابقی مسابقات محروم شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/94165" target="_blank">📅 12:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94164">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFVcfWZCoprSfrjOdjwNENoVQ7_F-U8234m24-TikXsIBNo1K8HW8WAlZb7X0FG5nbk5Y46gd6o5WGygPTehiuvtoO-OyOdjHHCt-EiPKc2d15nKfFYabacInojVStg00AXR_VB9iJrK0KVaQcunwRYTB3gJOrkxA-9cK2ugh5eG4orlCeBUYMtdtTOJycgztxNrIKmkBohjjUcCJcTbbhcmtfH7zgwrd2lRagFkWFttFp7PU_6OTIcwHZVONIWCq6Z_VjLtTFrBfEK2QSW8xxcRZ0IcD29V4R1kV1643Sn5G33ZedFQEA3ImvEb48JwfNlIoGSs-dWUpEpDkoXDrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فوووووری و رسمی ابراهیما کوناته با قراردادی تا سال 2030 به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/94164" target="_blank">📅 12:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94162">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtnjcqDe1FKFY-6L1xvz9o5ER17YHM8TAq99Kglj4D3QXTABuJBO3qzuteuAk_mD2WwNRawpFtnoE518LYwuu8EvlWvhLepq_nwzGoDyh3e7-CPynGb63SQ7AYRHSoBz2LlUm4j3rq1W1j_sEyvE4MO651tXUasn8zr51r0wFq7IrNVhM3kbWnDQovMDGl7D2Kq6d765jj83A5OqNlpWZH7avW4WhOY64tZ_1vcwNe9Ykwqw8Rhe2xZfNhnLKqEAg6hg-M_VV1E5QX1bHgnCqPoupPTjnX6iCN3KSWHwlioiWI9PJVtb-iAXikPMaBAsXFd_NaMHYzADfgKdUSKzwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🎙
مارک کوکوریا:
رئال مادرید یه ابهت خاصی داره، واقعا سخته توضیحش بدی. هیچ‌وقت نمیدونی چی قراره اتفاق بیفته. خیلی کم پیش میاد کسی بتونه درک کنه چطور رئال درست وقتی همه فکر میکنن کارش تموم شده، برمیگرده و بازی رو میبره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/94162" target="_blank">📅 12:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94161">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5767fe2278.mp4?token=eGzM6JOZfRKHFflK0m9uHRruFQvaRJy5uRGpdBPWh21hnNra2Uu3O2kdQEtRihiik3kpVZj7mgG7MpH1wZVpbYU90VBoRlXjwKrg1OSmYgGrvggvLRjjhBqZS8PQZrMkD86DjdN8hJdMV36Ti4X1PEIHgMZXmuph2r9vgWTk3JzYmWzPHOIuYnD0eLKqtufRqffWJXJOzs3snsCEAEKu2_7N7m6MbDQbM9bfQTtRDeX9nUak44oPzQPprFYkXCBYqtrKcQOaKB79hJL_r09ObReJUI6ydAJO_kfcV1DDmMw7Dvf7FgaL7Gtp4J49tfzIKB-d-QG0d1sgMoPZ13MekQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5767fe2278.mp4?token=eGzM6JOZfRKHFflK0m9uHRruFQvaRJy5uRGpdBPWh21hnNra2Uu3O2kdQEtRihiik3kpVZj7mgG7MpH1wZVpbYU90VBoRlXjwKrg1OSmYgGrvggvLRjjhBqZS8PQZrMkD86DjdN8hJdMV36Ti4X1PEIHgMZXmuph2r9vgWTk3JzYmWzPHOIuYnD0eLKqtufRqffWJXJOzs3snsCEAEKu2_7N7m6MbDQbM9bfQTtRDeX9nUak44oPzQPprFYkXCBYqtrKcQOaKB79hJL_r09ObReJUI6ydAJO_kfcV1DDmMw7Dvf7FgaL7Gtp4J49tfzIKB-d-QG0d1sgMoPZ13MekQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🏆
🇬🇭
رسانه‌های خارجی با انتشار این ویدیو نوشتن که غنا دیشب به کمک سحر و جادو هواداراش تونسته دقیقه آخر پاناما رو ببره
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/94161" target="_blank">📅 12:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94160">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5190506dcf.mp4?token=qsnlvkrpEH0LN3HlQG4o_Az5j_kWb6cJc2DOD_RnXQi0qrDutmAr4MLggMFXL2Pu2I3znOHR4dm9WOmloI6dLS8IaPjtg3SP5mK-5HWAVUHPqikJ5ABAgi3km2mwLn_nSP8ElHmpMOI02qGM6ZIbnWbzWMSuhyM_iHHyhCujhrw49k0zppQ0b-XaDB9R-3Oig2CazYU6522xvMd5n49rluryJQOJCRvGrt4zX1vU4U1srShsroaqxtj9XaDyyAF-g-OBlq5v_AceF71YdlNyq7kd2rKgZTPd_5D5Bx8w9J8lI5IJTUGKzUkQzgQy6k6w14Y0ReksidTyqCUFbRBJTzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5190506dcf.mp4?token=qsnlvkrpEH0LN3HlQG4o_Az5j_kWb6cJc2DOD_RnXQi0qrDutmAr4MLggMFXL2Pu2I3znOHR4dm9WOmloI6dLS8IaPjtg3SP5mK-5HWAVUHPqikJ5ABAgi3km2mwLn_nSP8ElHmpMOI02qGM6ZIbnWbzWMSuhyM_iHHyhCujhrw49k0zppQ0b-XaDB9R-3Oig2CazYU6522xvMd5n49rluryJQOJCRvGrt4zX1vU4U1srShsroaqxtj9XaDyyAF-g-OBlq5v_AceF71YdlNyq7kd2rKgZTPd_5D5Bx8w9J8lI5IJTUGKzUkQzgQy6k6w14Y0ReksidTyqCUFbRBJTzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔺
حمله نویدکیا به قلعه نویی: وقتی حسین‌نژاد رو دعوت نمیکنی حتما باید از لحاظ ذهنی به خودت سر بزنی
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/94160" target="_blank">📅 12:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94159">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfvdXFzbE5hzfEXxsgVwz75V1mH94PZyFeugxxskZeDpUlkQnHqoRFMlqQmztx_SWcdl41oBlFSkt2_Fax6mU47QxtiU6ul7Vs7rDD4sBmbMQPmW1kwnc3mDU7-jyFqUp4AbHFo2oRZvsGQeT-Rir3XwgGLA9BDNHhYAJL6KEntZ2ysHfCqhreQ52aWtrf6oX8Mp0ImeqaPZpiwPi8csqI-Rht40iJTUIHd7PufyaXQZCyjL4P3mvs0Bsb5v6TfXPpii8LIaRsuih_W2VK6iyo67ObRd-7e0He6RE6fn_K-pjeJs1KsZeRxuP41uA7BoLuLQk-aNqBt3QL3n4pE09g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جام جهانی ۲۰۲۶ در پایان هفته اول به میانگین ۳.۱۳ گل در هر بازی رسیده؛ آماری که از شروعی پرگل و جذاب در این تورنمنت خبر میده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/94159" target="_blank">📅 12:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94158">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/CFOX1opPYo0C76DaDPDQxhYH2D9qrllYSAd8lFJt2qb64rEdINjuWqv6gj0p95-n9xBcfI5K-eL70UCf2PXOf9ncpBxGdDuXyPdwZLNa0MIHmd6pkYOuJLer6mMAzEr7fSyhfSYj5kmp3UYDtl8k6JJXrQsRHbFIvlmpK66xS0Bb32f-oVmkMaj5FDOX_wPdMfWU_F4mlIU3veNj3VeH4jSbB_ITZBUVdQnSCDonV1tOAW2gTgU7fwq3q6IM5IR6FjDsjZIvoTz5zf32URHY49KgXNRMEzI202C0F0lAFv1u0S-T8CyqRLZtYSKIqtCcHgZO9n5i38BU55n1tactwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نابغه خودتی پسر بقیه اداتو درمیارن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/94158" target="_blank">📅 12:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94157">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWDW6dEZsvyTi28IcczcnwLAr9TtIoCEPy7jq6aQAWHly4LHjcnleljq21o2TsfrZvEfU1ysyak3ti3SiR3XxTXc2VTRR3Trncp2L1_cjpweYLDbkvFyv3tZ3ikk_Zp8LS9o_THnVRf-43b6utPd5BrRVt1L_SkDzn1snqyH4dLeDdEZPeUmRlnLy_xhLqonAhN1CsrPc_cNwNwwVDw5y6Oj2Gb86hQivg9DYpL5soWwQ5q9uL0KSTzao34pHzDsE66s2X6zqFmRlZki9MKua0nDdEmub7m40hmzRnHhLdi11zqLK2ZUHIWIrG8NN7C6yD5pO0xCU6xeK1e8wksIVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
رامین‌رضاییان در تیم‌منتخب هفته‌اول مرحله گروهی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/94157" target="_blank">📅 12:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94156">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDOCw-Z4qhziLopgr-p5UADrbyGb1CoUWEQcNqjginpF0jEetpdJwF8cQ3lXK2bUKEg8EBE4zI58C2lnCXQpM8TdIJbEUwjg3Nhg37dsnYh_gby-qCc3T-Ic0WJV-D5cln5rJtePklgFgKC2_3ExYUMuaucZS7DA4_c0yyUxNGthzPaduDCvNRuGFwI4shVgTwFgXLoLAx1AfUXY08WtJAPoUz2JXR8LFBD2I1U2WNjJTJsEUlyS5NNOemTeZ8mdFvQjVcdIb3dZH94CFcCyOrrQlaHthdor4yBmAa2tbRPKZzbsRyDTED2sqMsePdO6wn_7jk2LWTOiit1fKpbKMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود‌بلینگهام ستاره تیم‌ملی انگلیس بعد درخشش دیشب مقابل کرواسی با دوس‌دخترش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/94156" target="_blank">📅 12:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94155">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7db6ffd41.mp4?token=rTiFG9HybGoRv7b5K7ih1pG0diRxMXmHYaX6SQ0i_JCDgJjmojTQIkj3AZ3fp9K-gpfv8MR9vZBs5EdQCnuOE5MPulJc4VQOhi9uAzbzWL6YZIKDMQctyPBMwmpLwFD9aI4aqSEfV1sridK7mnS3de4dYqCMTuR7ogVTCTNOeu2ytwY9TyIv75emgX40nNBIrKBAKKFDbS7oxCnHNXU8EAqDub3qZQaBs8--DTnNZuKkTbMqvtUNQDI2fa9lylhOgJErZhQcyxEm1XGrwmFyeI_oelc05a7ydQ4eD0m66emdXGXm48f-CT28PBO7Fmt-mwBMxMnMkqo9QkPN4KpIfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7db6ffd41.mp4?token=rTiFG9HybGoRv7b5K7ih1pG0diRxMXmHYaX6SQ0i_JCDgJjmojTQIkj3AZ3fp9K-gpfv8MR9vZBs5EdQCnuOE5MPulJc4VQOhi9uAzbzWL6YZIKDMQctyPBMwmpLwFD9aI4aqSEfV1sridK7mnS3de4dYqCMTuR7ogVTCTNOeu2ytwY9TyIv75emgX40nNBIrKBAKKFDbS7oxCnHNXU8EAqDub3qZQaBs8--DTnNZuKkTbMqvtUNQDI2fa9lylhOgJErZhQcyxEm1XGrwmFyeI_oelc05a7ydQ4eD0m66emdXGXm48f-CT28PBO7Fmt-mwBMxMnMkqo9QkPN4KpIfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
بدل لوئیز سوارز یه جمله گفت که باید رو تمام درهای توالت‌عمومی و کوچه و خیابون بنویسیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/94155" target="_blank">📅 12:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94154">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXN-5cxhfgq5r2tf97zZOliJm3U5AdphdOn8XQmKJbblLB4kOu8KICBdmtnCl1Me5SdxIxjqVuCbc8VIgCorwoW2YllKvMwmnYCWApLbIvPz41NZQx7h-N9m8siM5_Yd-SEMd9T7R3eF24y1FNq9OBdgHMXiW112IpF3ggcp4WfZWUzBQPUOCTSb-Zm6vpoVerGkyqECC1BzK89YBz0sEqNujt0XOWvA_z59wB_YhmqCfnBsl_lqrECktfM-Su7MKfSZP7ceJvue6d2dG12YRoNJo521HKHt-10FhCmLEz5vT7KpwRNou72tX5sD7XiO1jTRPA30oot6jN_r7j36Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🏆
میزان حضور تماشاگران در ۲۴ بازی ابتدایی جام‌جهانی؛ تقریبا همه بازی‌ها ظرفیت استادیوم تکمیل شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/94154" target="_blank">📅 11:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94153">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2491447567.mp4?token=TFYMYaJbPf9gclmuUQ1F6r6yfa0GSLp1dB3bi9aGkCsytXNKiS6QOT20-9bVQqIguDO4k_8PeHMDd3JPwtL4yigrtCRlFsSqHx2Uy09RyWI7juxBuvcH6YgWltxKbSN1bWzYn_CqZ3qylnp8rs01vabUiKN1l_rRKrWJF6uCHMsbBCZGzn2dDb35rbakJWEvLZjwNJXKwHkHuuJ-0L9AtM-xNsYBgCQo8uHK189k5JyfvZC7rv2TnxowrJgYRojYiwx5dWHcPU1ctTg1hWTEJ6yKpdkPOJlfLVCPkqepICEiuQRwF8FyBMVg1vRho94bWWe09SzpWxZqJQ5Ssstc2BIDpfqaBheOT1OtIRC23bdpYHqpZUpSG25aa4FMo_x3Rui8--GiIhreUUJAYjSrbFbZTlO2oZNCWyax_pqG8WH_CDcK4TGdLuXdhV1I_wszsK2V0SRjKWDOxEsPGcLBoa151Cbd3hxwCf_JZL108O4q6B63cK1kE8KtvXA8Kj89tqj10KOkTtOMar4JqT-hcpIpnLS7M4k34Qv1SkPtK22juykqtp1oElbbeLI5lmE6QpgL1Q-7BYHxy26_lfibk4QWgYi_rYcgIJrvi9JNlgLFJfmT0R0H46_tM7ug36tKbp4Ak9hRWvMaSY4lp5O6SRjlAc03ITS-PculZVFNMac" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2491447567.mp4?token=TFYMYaJbPf9gclmuUQ1F6r6yfa0GSLp1dB3bi9aGkCsytXNKiS6QOT20-9bVQqIguDO4k_8PeHMDd3JPwtL4yigrtCRlFsSqHx2Uy09RyWI7juxBuvcH6YgWltxKbSN1bWzYn_CqZ3qylnp8rs01vabUiKN1l_rRKrWJF6uCHMsbBCZGzn2dDb35rbakJWEvLZjwNJXKwHkHuuJ-0L9AtM-xNsYBgCQo8uHK189k5JyfvZC7rv2TnxowrJgYRojYiwx5dWHcPU1ctTg1hWTEJ6yKpdkPOJlfLVCPkqepICEiuQRwF8FyBMVg1vRho94bWWe09SzpWxZqJQ5Ssstc2BIDpfqaBheOT1OtIRC23bdpYHqpZUpSG25aa4FMo_x3Rui8--GiIhreUUJAYjSrbFbZTlO2oZNCWyax_pqG8WH_CDcK4TGdLuXdhV1I_wszsK2V0SRjKWDOxEsPGcLBoa151Cbd3hxwCf_JZL108O4q6B63cK1kE8KtvXA8Kj89tqj10KOkTtOMar4JqT-hcpIpnLS7M4k34Qv1SkPtK22juykqtp1oElbbeLI5lmE6QpgL1Q-7BYHxy26_lfibk4QWgYi_rYcgIJrvi9JNlgLFJfmT0R0H46_tM7ug36tKbp4Ak9hRWvMaSY4lp5O6SRjlAc03ITS-PculZVFNMac" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
💎
🏆
تعریف و تمجید فوق‌العاده محرم‌نویدکیا از قضاوت علیرضا فغانی در بازی فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/94153" target="_blank">📅 11:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94152">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jASghb2Dks-EW964YeC6j--IviJJ8sq3Z8PQXiy8-ykEt5MOdw7I3qJJIOr8PqbgWpfxyEyYv2GXY_7yH_3Xp9wqrFsRsNdsVqFzqlGesTXiI0uGGMZkssbY7U9Ci53MpztHAGUGhUN30OzqBeYrQMdqOrF3knbmLhEXGgpJ3l6tddRzFQskFnIf9VWs5DTwWB9cieUupo1DsnzxJUkHZNIEu-u3WGBWake8Ifz5Bq0_eLFQBS9AAacOZ6CS938vbGk3Oq2sR4gokjG4qnBt1BRdlAS8cIKekDnJg-lf62zCNbejQxf6eUokmN0Bfh2IyAyTE_lAwuz9WQnhIktOzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
زرگر سرویس سپرده‌گذاری طلای ملّی‌گلده.
شما طلای خودتون رو برای یک دوره مشخص سپرده‌گذاری می‌کنین و در پایان دوره، سودتون رو هم از جنس طلا دریافت می‌کنین.
یعنی بدون اینکه طلایی بفروشی یا از داراییت خارج بشی، طلات می‌تونه برای خودش طلا بسازه.
✅
۱ ماهه: ۰.۵٪ افزایش وزن طلا
✅
۳ ماهه: ۱.۷۵٪ افزایش وزن طلا
✅
۶ ماهه: ۴.۵٪ افزایش وزن طلا
✅
۹ ماهه: ۷.۵٪ افزایش وزن طلا
✅
۱۲ ماهه: ۱۲٪ افزایش وزن طلا
طلا برای خیلی‌ها فقط یک داراییه.
برای کاربران زرگر، یک داراییِ در حال رشد.
🏆
و یادت نره؛ تا پایان خرداد هر هفته به قید قرعه یک شمش طلای ۵ گرمی هم به یکی از کاربران زرگر هدیه می‌دیم.
🔗
زرگر؛ به طلات وزن می‌ده.
🟢
ملّی‌گلد؛ پلتفرم امن خرید و فروش آنلاین طلا</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/94152" target="_blank">📅 11:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94150">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c14ca557dd.mp4?token=MOA2Dv_ZlRt616T-e9MMUepzVgZvjphA6iXNU_1i1FAp7ykmMVepc9sCqtKCHHiEYaFhWI-zItwk4gbwcMJaApU-U471t46LDQPt6IuRKvcPoPBrjbvI2xFpA7A0_ojSuVvjdyeFAe75CoQQ1nCbJ3FkyRPVDf0snMMuqK2hV0VNiJDP7sORiyOG0JrQm8ser3-v6U-xlmGFGJPZG_JrBFkiw8xP0a9Eqc4do1-g_Xm6mxTtsTCLCfpPwxMnY8h-IacS8S_zhOUjCrQ1IVBPAwkPsXlMRGgU6RkUwszN-OaBetgmZYrLVY50NBeR7e30dtd6qrkI-PzqEhQ-5u_h_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c14ca557dd.mp4?token=MOA2Dv_ZlRt616T-e9MMUepzVgZvjphA6iXNU_1i1FAp7ykmMVepc9sCqtKCHHiEYaFhWI-zItwk4gbwcMJaApU-U471t46LDQPt6IuRKvcPoPBrjbvI2xFpA7A0_ojSuVvjdyeFAe75CoQQ1nCbJ3FkyRPVDf0snMMuqK2hV0VNiJDP7sORiyOG0JrQm8ser3-v6U-xlmGFGJPZG_JrBFkiw8xP0a9Eqc4do1-g_Xm6mxTtsTCLCfpPwxMnY8h-IacS8S_zhOUjCrQ1IVBPAwkPsXlMRGgU6RkUwszN-OaBetgmZYrLVY50NBeR7e30dtd6qrkI-PzqEhQ-5u_h_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⁉️
تفاوت هواداران فوتبال اروپا و آمریکا از زبون زلاتان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94150" target="_blank">📅 11:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94149">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab0ef7f628.mp4?token=Xvqq-QWuKkoI86GWE19LYHTrUm41l6uGaQR33tUd3a4pgpg211nkBTl7fN6Rn3qO7MRKqWJNzrn1lBIZHov7Sdj5WvkLkF5nAmARf4ouG8nZznegINdl8Y-sg51QxLuhAHJ400mj6Bv3m2OUl_Yjlkd37lU0KRVqrUF1cYlOzP0h4IYjE5svBlol0ayvt-kgW2fWjYkey7bBk3AnJ9fjSkswKQAyZCAac2HS6vpwr_TzyShB8jiA7lB7Sasayi7yyrPUl1hLryOx4Utnt7cJ5_e0rh7vG5DnEu3pVceKKs8eJzBwrfl0_A6FRMvABmBFb1YYeQR1xtODXIOVL5xAlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab0ef7f628.mp4?token=Xvqq-QWuKkoI86GWE19LYHTrUm41l6uGaQR33tUd3a4pgpg211nkBTl7fN6Rn3qO7MRKqWJNzrn1lBIZHov7Sdj5WvkLkF5nAmARf4ouG8nZznegINdl8Y-sg51QxLuhAHJ400mj6Bv3m2OUl_Yjlkd37lU0KRVqrUF1cYlOzP0h4IYjE5svBlol0ayvt-kgW2fWjYkey7bBk3AnJ9fjSkswKQAyZCAac2HS6vpwr_TzyShB8jiA7lB7Sasayi7yyrPUl1hLryOx4Utnt7cJ5_e0rh7vG5DnEu3pVceKKs8eJzBwrfl0_A6FRMvABmBFb1YYeQR1xtODXIOVL5xAlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔥
دیس پیروز قربانی به میثاقی: با تتلو اون جای خالی رو پر میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/94149" target="_blank">📅 11:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94144">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BzaYY6JZMxfHsmuOwfqoJBs6y3B2NhHvSzWYBsGc_9plhW7MJ90Mw5Bjff6Ks283qVRKV359EklipYT3D2NWDxa9VStMqaFRVnQvmlE66ZQUkDGabDTnpKenYQdXwo44r0n1YfCzHrT63IZhqdWfjbSsJW4Hq5bRK94AgnhSxv0J20Li6s8PUgyf06-0zKLya1U-LDQ3GlhQ3bIYKP_zEhl8h0Dvw-t4r2_4rNSC3rqedorwmu2KQgynjFwrxQC11FNlTWJOcZpzfKXvbn1GwIE80xgvGRp4unGCcMzd9kIA2oxxTywiCZ3-P7hRLluUBJwNH2B0ZOO94hSdG7W6zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u0_f4RdAH-5uocpB_UOAgW_8YuWuaak9oy3GdQxCTmJsEK8NjzLONetAtCb0XQzQ31RLm_kgH6GjOPXc0M675op0d7cw2OZWuovW4njmqPlwA5zK5tABtNSdV4vVHPao8BqhH_PsnPvxFpZHVZUOg4CqeB9fAwpyZIng7fQgvxV-41kFwT4_LI_otqjagIYSPAdTEcip4SzZvyYjdZnW0Ksh6zAvqjlNSBJ_U1wtSYYFuvDsdTLpNBvuT_FZsbi-6F-zrd1MyG7O7mvoRYTLvReRbHH5se5YHHHMz3h9lC5OM-cCAT4Gm4_BlP-Df4jRSyS3VW5ceFTbK1XvRisTEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uP3etKc7gL012xgilDa7Juv2DAv5sLZNpjijWgT5f91dLMhhG88EhivNKW8W4LNUD-uNjpeU3hIeXoWYnduS0kJfNCGywTujJFG9g2zfxlPQTFHDkR6X0EugWHUMKoV4SjJcy1p48SWVnT9HGP-ceJpJkK6PB-8l6gUzOO2Vl2nUF4errd7Xr3scEyFpttxgWR3kzOQzOGnlRH8cvzfRFW6yZLTh8F35RWsjLiJoJ21lv5tnJXXsVQLbr0rjI443WoliksOS3rrGZHo2j_sArFbxW9Amlh9THEKmLNc0MOT0OSlu_jz-8Q3-A3Siaue25eiXFj6oKXCmNSlUajQM7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/irw_e_3WD0WLlD_v6ZBCkGfx6RRzoljdFXPlP8-B_nb1ycZDVp4k3cVJNGNYhuvKYACgI7FNbU4NF_RzRGF7s2lYZYYwHDi-HNi_qhEiq_pD_X6e4ji9m_2gvSd5BfGa0Oczhb5O1xx7yMwjJhsX5TyUI2SqI_8bTOYaBPjinfMUF11fjzX4KpFw86gKdJfKEI5ee1CkNF0em9T9QhWE5Cppe8smvGnSM9SbowPSOUX9WJ6YxzLH3jLsHiP1fpW0V3tzhZCd2EnYqtXBVMJPVM682Gpbs3LhQanGrhH-PT8OqWr_qnsDkXHByMDpJbuH1krs3whv2zbaAjt2-aP4_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CGAskMmYLMqZjYJJhvUM_Vw-o90DajdqSt9O3vDyEWLNHfj0k8taPCtDaWrduDyICcZNg0yowPANIC4mZVMe6MLgrqkeFBRxpAAVLnZbCi_sQZQdEPz3SpKCHYMoQuZ6h7WP4v9RU-YpPMFJPJ65GfUs1wYqvLjmR3BJKDRWw0RgjurYLP8RZSXRtdUISAGl6UNMJ0S00v37rUP6HBjwq0fbJK_ImQRoul_gYB1cOuklsptnlKxpdc3xFkDx2Yax4sg5tmK_v4jziueUS4a_7X2536N-wdIsoEmsjnQRd3Rbx-KXlnrdLJYGS3Uw4L6JlLR_Tbmf-UNyWTF6GwTbRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
بازیکنای کلمبیا و زیدیاشون هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/94144" target="_blank">📅 10:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94143">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgVmjeXBiEP4EPsq-vi3rzLvBnLj_y6rQzJYCk6vABay89LsjDLigPb537UhiUIwUX3IOeoRzGzxHJubZDPO_FGnwcRXIYBaVlpou1Dx3t03UEQSQVu6ND8bIILyeZz2GwZgtUHNWI_f_te1GdTuGWqA4P6txNMB5m9AUtdm8y8Qm6siUapE8kD4EDJYhZCo3Lj5rOPN6H2QXgrRP2JX4IGREPKUcee5hHWyFJaIuRTEAbWpp0zT43mcRx30kuP72tzyxs0do538Dy2IViYxQOtb8uPtoyiNcdwS5drDtT6VcTV5G95i-FRDQt8v7RprQk7bhOgxBGLzcilNZboHtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
رفتن دیدن رنگ صورتی به بازیکنا اعتماد به نفس می‌ده و بابت خاص بودن رنگش، تلاش‌شون بیشتر می‌شه.(روانشناسی)
🔻
از طرفی هیچ تیمی صورتی نمی‌پوشه و این رنگ به دلیل تفاوت با رنگ لباس‌ها بیشتر تو چشمه. (اقتصادی)
🔺
اینجوری شد که امسال یه بخش زیادی از بازیکنای جام جهانی استوک صورتی شدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/94143" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94138">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qkHeqAS_rnoqHcdrDLcU7hE-z4W-FGJ-mHde8dWf9Rew0j1y1szibv71g1namWTqmbf8XiF4-o7fY2O_IoNFJym5CgystqN0gedIoT0U9mVCwlYuoz_DZP3WWwIHlx7pAgHlGJUHQcKAXy13UmeRWzhVfBnCj5zgvl47C82cy48Bz2cxA1kPhskUanWlD5wNmCmwKLQcy4To0f7u03iTfNSjQRJTsxMZIr7atRd0CQNoasJKwi7cOIlTOTnfMK_QnQeG4PqJhX1e1lFYw92g2mwT-63IKZy_9yjVXJftpDaZvY4_f0CwcIWU6zOnQKi-_RPY1s0QQpIBj8GppwNkXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hSs0Y_YLB1y9K2D8nAnXym3wX9FzaImhOvptJdC9nBdMGs29t6dFtjttpQW2PgiOsaU4BbkOSFy11Zkvlzje1Zd8UAJozgQnzZfCI4O_9KtjO2Ca8HrhoO-s_1s5LXaPJquuVKB3ivKeHDZqK8inlGhGWG-CMWpIM5JkouEvfcTG69YhsFxEsBj6SlwH_zA3Td2Mlmhc7DMvJHcphuF2YbT-z2tld-JRwNWX71z8_QEJUb5m8wWkzt3jxerYQ7ZA23q6OHjY1zgivNi0-lOH1nP72Vxa6DU4HzR0G5qCzlKcU-_GNRU06sxxCUAEz8uoFFoDsgyIbsQ611COdDgrZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c08bkPgGtCXdUwZRKZhdGImNqF8qIAthHte7w7il9n7qpcI_oxz0U6rHjYxLfW_2i90Av2qJtC7ZjczCsDM6S446IK5V7tUGnEQ4yKyCld0VVQE-u8SU3FxDNChRJ8Tbuwmc97LsJ74YxAwIJzxrZmhterEUWQ4cmF096WDNBLuOApXhG0V0d9GggI9QdinDn8q2syNe9ToNV574inWaCnjdU2twDxAIpv32NsCm0D_pLmfjLDPj6gIT5_NxUUrhoDhxV-zexL7WrwyKYrEFYFwQYVmQ-tDjKZ_vJPRUDG_tSDFDSZPUbS09eR7KlQIjn7g2gHmoLFKuEbDdJW19MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xya5DqQvKVqnakv2WB83tfPXlAAgTKSn2iuRUSHFUUHbriROjgM32qWG6PGL2pkohqmzS6Cc6bUKQX-v-xpf6cxj7sovpowQH9YjYioWvkzLQvGW4Mpypm4I9smlHKzwz2ZNcQEPwieI62snnVlN0GZ8VhsWdbYOiekF9Kym3o7VaB4L0MBYs04AXf2PHIiz2PZ4N6FkFSxqQg-kqvjKYST_Y1GZNnnRoNN5tOtUul3QpeQeh6uyJ81pjR0H2YLBDsj-LCXEneXthvbeBlmWqXc96qk6glFtNVUF0qVT6XD7xsfk9OJhg4i1obAgNFjhW-k7zSJ5K4FK8yI1-FOHhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
حق برزیل واقعا قهرمانی جام جهانیه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/94138" target="_blank">📅 10:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94137">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a99ba4fd6f.mp4?token=iIm5My_l_UO1ox-ueA3Mh5xI7RMBvjGgBiX_BhUkGOpQk4EDfGAGfucKVqd5xUE-uykAl58TJK5ceBshwnySwbOvgB4LJh38_3YrEBI3BZyV5JfJB6ZkcfB5Rnx_MvbE4Cz0p_AxvWeXWfqToHaeUS-BApYl-62ZONW0kEBid8TiDhlZw6RYqa9HuMHTRqy-Bbnb3RKpTbANOGfXfXfWP_6-2lwz3p-PtSeLMjqJK1ILUeK5Z0Lq5WPwBFzrTsfAduh0xklvIvM45eYWa9foneO8ZOZZkzrRuJ3z6VRLhaBTOhPQvUNtrpkufsgzd_m_m2pghjOmis8XUaCrOUKdhmBobK_zcwWgZ8zpW6iaka8JmbEuYRIGCSV9U3PRnTRUdwyxdhSlG6KZ1P3QCnvmJvSfyc_cTHKi415Ie0Sn3NGMDRRR88xwOgMsHuLvR-hyc_ZJXXfXTmaKAdI93EC55jEMqKNh9zIP8t_W04UtbPnC7PT4HSYDmPquJxEYLd7AHmPrEszioRTXIEqQp5FeualY4mHfQt7EPWsih5f7uDi6lZ-bDV-UBgxmcwvT_K_MYBcH9Pm4-y3VPk1YxkuTed5LKFlEUntwQuk97TsSrVeXvwn9oWY8DpAJfxTlqdEL34254zr0qhFQTWKqh3vyYFuVSOmH5TO-mH6axtQ6WQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a99ba4fd6f.mp4?token=iIm5My_l_UO1ox-ueA3Mh5xI7RMBvjGgBiX_BhUkGOpQk4EDfGAGfucKVqd5xUE-uykAl58TJK5ceBshwnySwbOvgB4LJh38_3YrEBI3BZyV5JfJB6ZkcfB5Rnx_MvbE4Cz0p_AxvWeXWfqToHaeUS-BApYl-62ZONW0kEBid8TiDhlZw6RYqa9HuMHTRqy-Bbnb3RKpTbANOGfXfXfWP_6-2lwz3p-PtSeLMjqJK1ILUeK5Z0Lq5WPwBFzrTsfAduh0xklvIvM45eYWa9foneO8ZOZZkzrRuJ3z6VRLhaBTOhPQvUNtrpkufsgzd_m_m2pghjOmis8XUaCrOUKdhmBobK_zcwWgZ8zpW6iaka8JmbEuYRIGCSV9U3PRnTRUdwyxdhSlG6KZ1P3QCnvmJvSfyc_cTHKi415Ie0Sn3NGMDRRR88xwOgMsHuLvR-hyc_ZJXXfXTmaKAdI93EC55jEMqKNh9zIP8t_W04UtbPnC7PT4HSYDmPquJxEYLd7AHmPrEszioRTXIEqQp5FeualY4mHfQt7EPWsih5f7uDi6lZ-bDV-UBgxmcwvT_K_MYBcH9Pm4-y3VPk1YxkuTed5LKFlEUntwQuk97TsSrVeXvwn9oWY8DpAJfxTlqdEL34254zr0qhFQTWKqh3vyYFuVSOmH5TO-mH6axtQ6WQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
💥
وایکینگ‌های دیوانه درحال دلبری تو جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/94137" target="_blank">📅 09:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94136">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1df67b89f.mp4?token=HX8ah47EQF8SM0wAH9zGuzVA50Yy0b0gLb6wXvOg3FCe8JE0EVLMl3b4c5760qlU_-JEEf0u1uoSjuzl3EDcMz2E1EIdGQtuIUChWms8oOwqqO8oBv2PzvVh7bVHbLCGx30E0rCQ6Da0Au2EeNoCBOs9ClMxQKScUlnqU8jHNI18d3LKHYF3rMzzCXt4p56tsRTwIhs-qvwRH73QZ8q4uvzGjlFNDHkO4cMop7D_dAvQxdgAOxhjI754VHnJorsUBNZjX2EA-H38niuIDV1Wr-8LB-QvgeTZ_U7uhApH0duwwVY1V7Eym9dWkcqOizJtHcmiEPsC_sz7D7JH8j8xWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1df67b89f.mp4?token=HX8ah47EQF8SM0wAH9zGuzVA50Yy0b0gLb6wXvOg3FCe8JE0EVLMl3b4c5760qlU_-JEEf0u1uoSjuzl3EDcMz2E1EIdGQtuIUChWms8oOwqqO8oBv2PzvVh7bVHbLCGx30E0rCQ6Da0Au2EeNoCBOs9ClMxQKScUlnqU8jHNI18d3LKHYF3rMzzCXt4p56tsRTwIhs-qvwRH73QZ8q4uvzGjlFNDHkO4cMop7D_dAvQxdgAOxhjI754VHnJorsUBNZjX2EA-H38niuIDV1Wr-8LB-QvgeTZ_U7uhApH0duwwVY1V7Eym9dWkcqOizJtHcmiEPsC_sz7D7JH8j8xWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🙂
دیشب وسط برنامه زنده عادل فردوسی‌پور پاش گرفت و اینجوری داشت بگا میرفت هرچند طبیعی جلوه داد
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/94136" target="_blank">📅 09:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94135">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d434481e09.mp4?token=ozOnh5LosTJqF2DvBoD-0IMQxE1cSOFWjAZvQxg3N77C6olxHkTfD3X3QlAcxPiXmItn97ITydbpI4pC0a_MfgHHbdFaJ2XGrXPuUt5BtfePDW2GIsnZv0Jd4-p4Q2zuu6hn2I30Yue4ya_Pt-vhbT_yFYm6WGbU3zfgJ1SClLfE0fweO0tW6IdZ9WYdHLrFtMex2oGGuXI6k2EL4-SUDqBvE1S7qo0UPy44iAW_EqiJGrWRnJZ5FQXewvHahdY3T24Ww_459Wd7mZZzV7Tt6z6m9SqQFYVdoB3zMbIV9OLPGBgijomx75SgiQ6IcNOj3waYe7NGWDjWYcA4Xf40kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d434481e09.mp4?token=ozOnh5LosTJqF2DvBoD-0IMQxE1cSOFWjAZvQxg3N77C6olxHkTfD3X3QlAcxPiXmItn97ITydbpI4pC0a_MfgHHbdFaJ2XGrXPuUt5BtfePDW2GIsnZv0Jd4-p4Q2zuu6hn2I30Yue4ya_Pt-vhbT_yFYm6WGbU3zfgJ1SClLfE0fweO0tW6IdZ9WYdHLrFtMex2oGGuXI6k2EL4-SUDqBvE1S7qo0UPy44iAW_EqiJGrWRnJZ5FQXewvHahdY3T24Ww_459Wd7mZZzV7Tt6z6m9SqQFYVdoB3zMbIV9OLPGBgijomx75SgiQ6IcNOj3waYe7NGWDjWYcA4Xf40kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🙂
👀
منتخب ایران باید این‌شکلی باشه تازه مورد قبول مردم قرار میگیره :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/94135" target="_blank">📅 09:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94134">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AA0JoEwqocQRy3WK4tTh4b9hSHQqLOifVNGZXtgdWaZrtK5Bd5efOH5IKJ5Vu_l-xSqqdQZ9Kc4jRmqT78BkbzmlXB8UAGDoFV09QxhoSUsy7uqGhKMd7m9d6C0KxVtE4Ii1XAbbrFN2g2ObU4wQHPTCwtxlmAAw_zecLnTxjO2p4BPvETjsK6sJ9BY-uFFVd-uXo4SMXHtdm1zNxMmGhR7lR83ryl23dMjvjdY8oXUaInFs-6H8TkO1paNucBLtsqt6NPMlRcbwNEDAILfdXlKVUnaCvKMra5Zb4pqI1ACCAOe-XPaUdVMnb4_gIcpGC1Q6lgYxXQwy_0pTGkFMvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
نتایج دور اول جام جهانی:
‏
🔥
۲۴ بازی
⚽️
۷۵ گل
⚽️
یک هت‌تریک
⚽️
۷ دبل
⚽️
۳ گل به خودی
🟥
۳ کارت قرمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/94134" target="_blank">📅 08:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94133">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vD0XXPz-EvqTT1STX4QkKNHejgWMraVSVKeyx-p63_3qOU3vuEKm36itngZ_l9XtZrUuKFYUxcdUYcHAhKoy1PnJ3m0i4m67SATehrx6FnRBqugtFTem7wF0PQ9g2oPmpgALhTYQ0Mw2d1KMwLbHROVGSR_10rHjW2xCcQcEOvHVKEKkkS2emUkyYHlDi8b1fUiNM6BhjE_TotRaJm0jUPc6K7zDchJuJwpzuHshi2hT0HBMZRO5JZO1H-lNttD3xS4_WbBW3wMRMTAnZt7JrbWRksg1svVDGvwvLZJQ-LOCCFQOmOst2iPeqLSUz3wzyByU1zKw8fFMlESElECYuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏆
🇩🇪
مثلث خط‌حمله بایرن‌مونیخ تو دور اول مرحله گروهی بهترین بازیکن زمین شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/94133" target="_blank">📅 08:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94132">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tile_4nST6-Ce55EXGimYAS19bBO5Dt_4PeFKv6m1GpoTSLt3EeKZ-LIFfDBMoZ5bkIxrne2uDtpap3AR0h48NOgCei7YS4NukITVuOBE2kXVZKif3fTP8qR2urd_e77t8vONHvcS9si0XJDhrHN2-dugagvWwB2pv1HXFxE0a_BSVFedXwfGGD7X58y06Fytcjwi7GipXQmi5LKPTLZeSzfhi1ELEzVJlM4CBGkFMjWomln1PWSJBrdE_kqqEsUjAHJXbG-RdEEShVLVR4c_2OORPhwGg_DnG3wIqxGlbpqhunlslABwVbbNN1om95PRy-Zz-oTPg9kNk6acZBwmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
رده‌بندی بهترین‌گلزنان هفته‌اول‌ مرحله‌ گروهی‌ جام‌جهانی با صدرنشینی مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/94132" target="_blank">📅 07:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94131">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUG79-XCmsGGTx40_JVze6oNuIy2ETrYscymNHn6dUod7DrX6Hi3n7FbvPP_NAmv2_oE5oC9SbEi1zfSEMX9fNfXSHAKXco6CCE0IooDMg_ZoNKw6d4FHDwt01zZZi7TrrfcG2Z0T7Ry65Q7vA8IIjd073ewS8zz246RstmA2djtinxDaRzZ6mHesefqkaXQYrKpSqX9J2cXO-JvbDE2wo_pZEhniKkhoUwVMIxm3LBL70GlJ4lHkMuSlynxJvNJUsptxhSm97pSoVsz2o5F27jk6pm1yu1OL7C8pt_m9ju6Gr0DG9xnaJsK0AF8cI5cgeMYn2VbX6BRIjXgNV8wDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
رده‌بندی برترین تیم‌های سوم جام‌جهانی تا پایان هفته‌اول؛ هشت تیم از دوازده تیم سوم مرحله گروهی، به مرحله حذفی صعود خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/94131" target="_blank">📅 07:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94130">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbeidRgzGJgH5E1Qfb7Kjt6pIVNHeU5LPlSXNjI_qocegrARRHxwQjiFgg1MQhdGsuIojxV7Pbst0IRjesEfkSDNVPZiuLAVpBfMmdv1_AjP_zlMtPzy3FkPagRcHjX773wJeNEMorbuQW52tYOGszoepMEejC93t68kOXpMP2elqFQcXZjIoaz5khq9U02Xa-QqbTCCwwuNZ8KUcdKF6kIvoKSbjoFW3aqJWjffxMjdNS1QZ-pAGSCNJ7EDtnt2714Tp9laf-Qgz2A43L5Eut4iaN1Gj-4aChccX8o_vAsvrs0kjEPCLu2uuI2Mc_9cuvXld3oH1HUAtvZZjdEBMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
جدول‌نهایی ۱۲ گروه‌ جام‌جهانی پس از پایان هفته‌اول مرحله‌گروهی مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/94130" target="_blank">📅 07:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94129">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mI63Dzx7rCIdkNyMzXz6qAqiEj4hIrs20W_r3TcrnzraMFCjnQjLw5zAII4q8tXSr2CU-jLgiHJqVEmhrZ2SKuJ8oBv00kcDe9Ws35SpNoISzYMVvCo2reWqebOmVu46Vup4lcTU9owlW7q1dSjTNRYBUIEl2yvYW2avel9q74ztMwzeqez9-tZuHi2m20JzG5aZH9yR0NT4HeY2AywqlsD0H1gSN2hKR8ivpAkaRllc1gP9Uaf7yEdDeCONaokNxcyBCQ29yQzQ92r2b9zo3IRRynA1Su_3f3lXWKsfZ2Eu2b5JCvv10dTq3Emx6_SaAdvyArMMFgymwn5ony0QxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
لوئیز دیاز بهترین بازیکن دیدار کلمبیا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/94129" target="_blank">📅 07:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94128">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWsgEgfOau2Q5V40j_2GmpZaZyY90ZMNuJHyOShhNbVm1TMgpZMBbFPywfHQzN0LiTxT5dPi0UNyCVFQOL-aA7n-3pJcuY66-ofZ6Bz0eO5wqius-aUaJv1zDvyFBPu6FdGPJuXOSdJzfZc9l9edzJGKIcuA987mGMwkclW0YJRI2x5BtWqB0_Rinh2tuLKqOrq6-_6BG81Au8wnxM_FqyzUYD6wiqmdm6_3yCC0rR3herQwH_FA0STT5QCr9adiJ4kUpm5svRJPakA7NDudJk-r5Ip_lXU5Z25QUHJU-L5cALpJ34QtoRdHpCGGB4I44bZSaUaVfH2c9bGHHlJaag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
جدول گروه K جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/94128" target="_blank">📅 07:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94127">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی رسما به پایان رسید و بازی‌ها در هفته‌دوم از امشب آغاز خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/94127" target="_blank">📅 07:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94126">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🏆
پایان‌بازی|کلمبیا
😆
😃
ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94126" target="_blank">📅 07:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94125">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVhhIffeMHwyquytNNYqwQCIja4MrGQGM1dmbIW6tDVEbKaeOO8VcYSj-jbysBEKxNQomqFRilCK3siKuSYZZWJEOIrUJu2mNT5s-GD-OTSaMc1do1jbDXdYvtzgkxgp0KNeI_mzmUdlDBjdpxQhTQZkdYxuS4XLskc_2x6bStkXnhrt3-isD7og-xnc5VVAkDFXk8cqAhLrkcbAhn9lqY_x4DX-HwaibXUlADZduvldyUUFHqSLaPnYPalxANOobeiQvrNyMLkrrCDBdBhaP1CYJt_F5xgafArYdzX3Gb24H86z21_AlwKTFmHCM0RIZU3aC0HFNuekFgZ_xpL5cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏆
۸۰۸۲۴ نفر بازی امروز کلمبیا و ازبکستان رو در استادیوم آزتکا از نزدیک میبینن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/94125" target="_blank">📅 07:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94124">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEQhWQ2_0UpJ7mpYCZr0j6RR6Iot64suvb0UwNokJ8xSDq6bRzjZWGhVksD8xXafGb8eZMopEqa-iNd5_IxN_zy5QThCgjmXF9YNSHzK0qg_XYNYoexg9P0IaCHg5smenZrvW_Ro5IXzhz2GcT9j0c1JegBZ3r81h7sur0z7VQDHTL6FDF0srwdrtRpN1jM2wFiivsYVFEmrac_Prpt-oKRkYldxc7CXxlvKhJhXuDP2fc5NGxqjoag6jshFy2kEZrivU4l6tJCITKdAjt4mUd56swyk2mg0QdMLQexQ32lRAqKiB-6UtJH6Y8iygX4zAMNnUsyonEljcVcefU-vZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
تصویری تاریخی از امضای تفاهم‌نامه میان جمهوری اسلامی و آمریکا با امضای رسمی مسعود پزشکیان و دونالد ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94124" target="_blank">📅 07:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94123">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0618ddcda6.mp4?token=vSrnnH5iSNN-i8uEi7C3FwDMRhEaI57KqjYqNR6WF7i5MwA90ZSpV2UOLP9Eu1brtHZBlQBP26IZEySvczDx7eA0-a4Ivz5--rfvXJx3-mZylzyrrjiiK6NN1OvA4jDqEzAO-JjNm_omGRhFFiBI8xifA6ehq01qs13ER2bhfp9xPcDgwTZyYa6e7GhMYWTqX4ZJCiA9QUiI21iSCPbUuxPRtdRzwTm1fLwG10Oed1qtm2iO_SQ-AIXVspZWqS6QdI-gX1rMQwU3VHjQmsGK8JuRJIi9VOjvMT3v2GmlaCzjBoAjiiIrTSRVZL0Pj7MAI1fwKYWgKArs7Bch9yen6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0618ddcda6.mp4?token=vSrnnH5iSNN-i8uEi7C3FwDMRhEaI57KqjYqNR6WF7i5MwA90ZSpV2UOLP9Eu1brtHZBlQBP26IZEySvczDx7eA0-a4Ivz5--rfvXJx3-mZylzyrrjiiK6NN1OvA4jDqEzAO-JjNm_omGRhFFiBI8xifA6ehq01qs13ER2bhfp9xPcDgwTZyYa6e7GhMYWTqX4ZJCiA9QUiI21iSCPbUuxPRtdRzwTm1fLwG10Oed1qtm2iO_SQ-AIXVspZWqS6QdI-gX1rMQwU3VHjQmsGK8JuRJIi9VOjvMT3v2GmlaCzjBoAjiiIrTSRVZL0Pj7MAI1fwKYWgKArs7Bch9yen6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
گل‌دوم کلمبیا به ازبکستان توسط دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/94123" target="_blank">📅 07:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94122">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82ffe050c7.mp4?token=s99w7LvMqNSeK61RhLO3IwdD2TQdkW_GtSb3gfA3SjmiBOlZE1efYICZ5ey8jvSqfwWOM6f4fXdnFvgcpIU4iNlxDFsEnmOSgOORRfN9k284UGLKtgs8rL-wTcp4Pvl7manRd3aOB6D5_QaxMqPiQaWNNxpuP2V-lvaPzC6rq-KszX651jVOtJMAnkfQ3o7mhhQklx7PLje9Fa6y39NaVobxl-EUgffv8xpiOb6iLill_1Z0PjNTTNcY7N-qvONNIqICvBEYvwAmbtSvrF9Ysrt1T-fMgulUuizkbyVWDbhRgFBfh5MGlJxyfUjQiUGAKTd0LW7wWIlCSrYnygH_4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82ffe050c7.mp4?token=s99w7LvMqNSeK61RhLO3IwdD2TQdkW_GtSb3gfA3SjmiBOlZE1efYICZ5ey8jvSqfwWOM6f4fXdnFvgcpIU4iNlxDFsEnmOSgOORRfN9k284UGLKtgs8rL-wTcp4Pvl7manRd3aOB6D5_QaxMqPiQaWNNxpuP2V-lvaPzC6rq-KszX651jVOtJMAnkfQ3o7mhhQklx7PLje9Fa6y39NaVobxl-EUgffv8xpiOb6iLill_1Z0PjNTTNcY7N-qvONNIqICvBEYvwAmbtSvrF9Ysrt1T-fMgulUuizkbyVWDbhRgFBfh5MGlJxyfUjQiUGAKTd0LW7wWIlCSrYnygH_4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
لحظه اولین گل ازبک‌ها در تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/94122" target="_blank">📅 06:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94121">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">لوییززززززززز دیاااااااز</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/94121" target="_blank">📅 06:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94120">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کلمبیااااااااا زددددددد</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/94120" target="_blank">📅 06:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94119">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دوممممممممم</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/94119" target="_blank">📅 06:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94118">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گلگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/94118" target="_blank">📅 06:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94117">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فیض الله‌ افففففففف</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/94117" target="_blank">📅 06:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94116">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اولین گل تاریخ ازبک‌ها در جام‌جهانی</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/94116" target="_blank">📅 06:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94115">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ازبکستان مساویووووو زددددد</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/94115" target="_blank">📅 06:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94114">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گلگلگگلگلل</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/94114" target="_blank">📅 06:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94113">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔥
🏆
🇺🇿
جو پرشور ازبکستانی‌ها در استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/94113" target="_blank">📅 06:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94112">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c320d9c471.mp4?token=CZpJWvUHsl_RJXPoEmgEi-MoyS_NWmfNdgtsMbGQaNJDIlMLoHMZaKv4bXZXUJgoiSpf5QlR6cJsEIzX8ornaK1llE6pUAPeYDte0YZYpXUaV_DCnO5l1sx3c-v4S2lL7TKvMfVS_JNbGvw9-TbVSAvlEQhf695VtjtImyCrbNCQlSowrXNbMQPqgN2x-vhk2Dn-zhyGPEWa1qvlCHt34Ek0vNO_PF2Obq5BFTobpkgvj9ONGDUxhG3Gl1kyid04FH8ZSl9Kfbo3A0rfHmEWUFoZ3Br4x3nDWAb8cOEKoj8HghAsij9TRCv6lNd2ivMfhwfvBYg0Psg9L-hz8miCXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c320d9c471.mp4?token=CZpJWvUHsl_RJXPoEmgEi-MoyS_NWmfNdgtsMbGQaNJDIlMLoHMZaKv4bXZXUJgoiSpf5QlR6cJsEIzX8ornaK1llE6pUAPeYDte0YZYpXUaV_DCnO5l1sx3c-v4S2lL7TKvMfVS_JNbGvw9-TbVSAvlEQhf695VtjtImyCrbNCQlSowrXNbMQPqgN2x-vhk2Dn-zhyGPEWa1qvlCHt34Ek0vNO_PF2Obq5BFTobpkgvj9ONGDUxhG3Gl1kyid04FH8ZSl9Kfbo3A0rfHmEWUFoZ3Br4x3nDWAb8cOEKoj8HghAsij9TRCv6lNd2ivMfhwfvBYg0Psg9L-hz8miCXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
گل‌اول کلمبیا به ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/94112" target="_blank">📅 06:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94111">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کلمبیا زد
🔥
🔥</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/94111" target="_blank">📅 06:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94110">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گللللللللللللللل</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/94110" target="_blank">📅 06:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94109">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bnm0Kn52q-SqNmh_TuvlUNCgRCebs0S83JturHHJ-jHwdqTxQE8ss8mZ3mlg9KhtFtm_-9UV9t0RmgMVufllSUnOCjPle5cEE65HcslLMlaCPQC3kDmZUW9oFmeBjDKwWGkA1h-etxUC1i2X8GadXmUzbrJnJFLp_Qp9ngYPeYRfevGNPoF5P57sX4XCuOqpX_j9b6rwiGo2F_ZTpVjUuCyISCTVKoZWyMem8z8A_Xhh91UsaQ_XcjP0vbY3mw9lwpL6oy0snwb7ecOXOZ30TX_admr3z6aJBcgiLy8-VnCXhQQZLj7uwidvb6ynpDggm4APqzoXtOPsQXE1EBnT9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی از حق نگذریم تنها برنده بازی دیشب ایشون بود که زندگیو برده..
💗
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/94109" target="_blank">📅 06:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94108">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شروع بازی کلمبیا
🆚
ازبکستان</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/94108" target="_blank">📅 05:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94107">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAAKNqryN8gsUCd604vWGok5vf5fEQ83RoPnjAiHKCPtuiZWFFPSh_khrPtpWeuEjIRHesBhveLX5tH_3heXJrlZwnDUuBYyiNpmjKORfwC-VRXnj3fVbEJ5xYMi8IxJ3No3M-GbimJxA5d50rBAKNqH-L2Zz2A478t3p38qmDVgoEu04AttYkz4mXiZrivogJvrHo_2R4Dv13_rv0SxwXE82GsuG9XpPFf7VmeN6_QC6NsYsTaVQKoCPwcwckkl7_aKRxwxKEMT2R3vArbZbB7csQLicgTgljvnvnVT6dz9nVbI7gOztKT0X_7k3KvaNX9WQRi_wAc9OgSdravTxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر جنجالی رسانه‌های اسپانیایی از کص‌ خنده‌های یامال و زیدش بعد ریدمان جلو کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/94107" target="_blank">📅 05:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94105">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aKIuA3qe_fJ4NyhGkVU2ftLY2pcL16RXr_agEFajqn8XiQThtAoJxIzIpBvh4Tay-Zub8nye9ywWo3rMd4NEvd-8kuaTUzmGWE8Mn_18ND8JMo_7qRoBmnsZea6WkoSc_q028gg-PMso9M29H1cvxmadDQmzoeklFLw5nbKmRNQeAxmH-rPegzizI-uDuJMA9oVBlWQ2S4GNKQIIs93Y6RrSytl6lwfnPxLT7wwnKL-9yAXtfGMdPuxQ1-IPvRArPcc1EZ419Oczux5AZtmK4ARzZsXv5cuxJXDe8i8qr1oFuK_4rut02OGshFf_gbJTrOQOYcc_YTw45fgN_vA3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GPque72PvpT_Bqa70ZgmqFIxwvN8OIElVFFoDrELxRZeIX8b3iqe3s8gc72lnyV70V5H19TIzaKN9VdzTCQsA0lV_0vfTqN22eBZ6Uuf543cLaD92YLBqbmR0WlOtsli3JNVrfhwbWqLwv5o4_eKHdTJx06QplyBVx_khLc7nta7T73r4NTMyQlhQVzmm3SCjA4UeauDrDfPKjhS14z642c5LWRqsRDxtHHxNod0r15r6DuaShe1go6ddSFcaiccpmy504N7-n00fm29cwlNdmRevZH5R2AfUeBWcFGY55YskgaFV_sld2TjBSy8ZXRZSeQeGrxe8VuEj_lHQ2Dyug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">2014
✅
2018
✅
2026
⏳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/94105" target="_blank">📅 04:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94104">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGWs7cIZMXMUEtUvpX7e1WTwDD2YNuJX8NxG-dLE_Aa3sND1jWoptLIQIULFAgymPh2qpEEk8ns2swud1MKJrQgwbm2_xWjZkzeAPdkzxZNS6odG7UMOVEcdBfgZ_7X0zSyqhSWGhV7A8AGtY_45iDMnA448mwVZ5vSowdU91Hc34uyng_L3dK2Kt0U7Kl2DJr5mb-qgRp7XKdvsUz95VOAAgUHKATKFvTqLNId3sjsLMa1ufnAGzDcwJUwlkMN7eVfKgHN-0UI3q5rfcWBU1TaAzbi0Thld5PJ3pppLTczSj_oNupP3pvWQ68r5DtolzRHdGRc-CqCgrHBwLyoGYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🎙
مصاحبه روبرتو مارتینز پس از تساوی ۱-۱ مقابل کنگو:
🔻
نتیجه خوبی نگرفتیم اما ‏در جام جهانی هر اتفاقی ممکن است بیفتد؛ آرژانتین در ۲۰۲۲ مقابل عربستان شکست خورد اما سپس قهرمان جام جهانی شد و اسپانیا در سال ۲۰۱۰ مقابل سوئیس شکست خورد اما سپس قهرمان شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/94104" target="_blank">📅 04:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94103">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwxKThlw9dOSjS9XO4h7aUwdBfSJnuMsqmsGJMVtEzUVMV1Nod5BCcISPnBMEsfAOq43zty4nbau6rOjtF3dvOzPYinoTzeUgRlvjcEZh3EUJXlwEPRzicuQFGHE8dfDzMHV3vjmwGJU-rwDAIxI-Q7wUri9WQ1i2kUYcn2ZH3yqzDXHltdWiDxVv1T9bJSVYCfwiaBWVCqQo6-Oz-m1cWgxRjMdxcMWjwS_DiYFl-7i6GRXOHqXVrGr09_8LOZjsiZMiIk1hEPeltRsnBKJwaaetePVh5sVeqOwfxPnXDr_-_r_TBs1yBZm_pafY6R27fIKe9B6bL_P8NdZfagmTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇺🇿
ترکیب رسمی کلمبیا
⚽️
ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/94103" target="_blank">📅 04:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94102">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJId-pvcWtSsdDTKJemBcg0-E3x3uKKu_JM-Jr3V0-tUTCROxnJPg7nPTVwi8khW0lfQIeHxCKrVL58cWqVw4sNtLHfN4yxJpVzcacvKLXuA6SWXwQ5if8KQOQMlWUM-jE-1SRQ0CE1dFZCtYAY8Q_TCY-oAkIkmv03S6ouvBTk_zo5D11VQzAdtsB4uT6PE5P2YcVcyZC1GUM2dtRULrWoct13CfCvBbts9kTJm2_wZmqvBEU6_FwHGZ2inp60QVBkC52eZuC4MZkF676NQlkT3O6i47pPIPHzncuAkYnHiRT_gQZ9-xnA0W0-0yxtiEbdWipvJo0xK3hyXMyZ6uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه L جام‌جهانی پس از پایان هفته اول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/94102" target="_blank">📅 04:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94101">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vG5Ut2mrZvPAf0wWATCasZhFt6_olZypc9TjghfkQZ3ThTw2HV4SdW-CcHmAvfROIL5BeChq0eshjc8q0zdb7_aOan0dWNVyFsiUjNoMvHZ0tj0_5wK89K5mqtEGtU-LxenMHrSjdfk-PjGjudRkI9RYljhuBa6Dojsnz6X325u3C3LyHy8S1iOKAGuLAjbDSS0VBRv1jmGq5-OfnUOMixomITyGrNvPQDPPnJL5J-3cabFUbfzg0CDWVtsDxVkaDXNvflLfu9rUqIdrdxQPhBxN-kMFO1Tw5riHsBO6oYIx2pIWupQ_buyCOAdkQhlpf122JanMbsk07M29IZBs3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | اتوبوس همیشگی کیروش با گل دقیقه 95 به مقصد رسید.
🇬🇭
غنا 1 -
🇵🇦
پاناما 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/94101" target="_blank">📅 04:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94100">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1bb7784089.mp4?token=UzroyKanCaF5JU7lSENzjLGlzdzluAaOiBuI0dMUdE6QtNoaVcGY6Ntt0QYsA5WEIzCpHD4QNIl9NPkQ1rvoFygYMx6NM53C8j-4pniXxrKlLPTdUEnLuLIv6jBq-VxEEngzWeQODoGEAFh-0DC-AzItu1tUfgljmnyRHCOOHy1M0NSFoNFFDShoTupajMhmnWbGpDH9U6ABuRSPk2T8oCMK2FCJv_ATS36CvPaFv7kMbTnbnurse1VVK_UXEnxWA-jOPUGSjrxDyK7dm_J0W0YeXOy7OJSpMFHHjre-hzsVYcvMTHqgJCskheptmtfFviusP0ZfMa-bUNG1FYZRrb2uidowGXgnAep2Zzlqxsh4wdVLkhsStUD-45Fjfg_GyZOdetkc7P6-WxJViHYlkCo8c-9GLFpv51AUODMD4vKOfxhcr0bnrJALIbf_LDAR2gnnljsHf3OHtAVGRj0l7HZtYXVxgnwajrhfCqm7WxWtHULGd6ka-A5sWnrsFNFNYHPyoYS8nbLvuGtip_f3pVYLNdvOEwyDjdrDfYril1fpREase-XCHv3lSlJ87pMakAgu8wHwIOEwcETCgTEMzSwXLT3DeYNoXww3EfauKYtF-drkxDsNJ0XRmOLVqHsVSoe9v9pqRI35Up9yX8hdDC4Bc_8ITllXEhj5yyV8SvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1bb7784089.mp4?token=UzroyKanCaF5JU7lSENzjLGlzdzluAaOiBuI0dMUdE6QtNoaVcGY6Ntt0QYsA5WEIzCpHD4QNIl9NPkQ1rvoFygYMx6NM53C8j-4pniXxrKlLPTdUEnLuLIv6jBq-VxEEngzWeQODoGEAFh-0DC-AzItu1tUfgljmnyRHCOOHy1M0NSFoNFFDShoTupajMhmnWbGpDH9U6ABuRSPk2T8oCMK2FCJv_ATS36CvPaFv7kMbTnbnurse1VVK_UXEnxWA-jOPUGSjrxDyK7dm_J0W0YeXOy7OJSpMFHHjre-hzsVYcvMTHqgJCskheptmtfFviusP0ZfMa-bUNG1FYZRrb2uidowGXgnAep2Zzlqxsh4wdVLkhsStUD-45Fjfg_GyZOdetkc7P6-WxJViHYlkCo8c-9GLFpv51AUODMD4vKOfxhcr0bnrJALIbf_LDAR2gnnljsHf3OHtAVGRj0l7HZtYXVxgnwajrhfCqm7WxWtHULGd6ka-A5sWnrsFNFNYHPyoYS8nbLvuGtip_f3pVYLNdvOEwyDjdrDfYril1fpREase-XCHv3lSlJ87pMakAgu8wHwIOEwcETCgTEMzSwXLT3DeYNoXww3EfauKYtF-drkxDsNJ0XRmOLVqHsVSoe9v9pqRI35Up9yX8hdDC4Bc_8ITllXEhj5yyV8SvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل اول غنا به پاناما در دقیقه 95
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/94100" target="_blank">📅 04:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94099">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حرامبال واقعی</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/94099" target="_blank">📅 04:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94098">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اتوبوس کیروش آخرشم کار خودشو کرد
🤣
🤣</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/94098" target="_blank">📅 04:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94097">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">غنا زدددددددد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/94097" target="_blank">📅 04:26 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

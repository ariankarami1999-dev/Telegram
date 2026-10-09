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
<img src="https://cdn4.telesco.pe/file/mbbTpbiP-x0ZqK1KzXCWUbrs852sdBOhPrAYE0No85g2Y88GNYKUCfUfOBN_rvuDFRbKSWnnmFb3MjSDP3rTj9y_ZTJiCgVkBNQB8dji_vV9KYcmdgHrHf6kw3dSooWjxnKt_edOHtJf073N6hQqPaTn9xMg0dHycFIvKWAu7NrHdWhDskrA_l-rkWJoyU2w1LNTSoga6rbA9lSdo1u7kNiUoBMUi2PqDEX5beUkGx5zeLJ9CCY1QEuuYV4lmcQ5wq7DMpXE9jRqgRKnUvp-QE1I7iuZeNovHRN_MghbnaUFsof4DyNnIfKr9s4PMMQtdHN74dMug3VVO09hMoo0CQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 23:40:59</div>
<hr>

<div class="tg-post" id="msg-151850">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/npRY7brwapZMV1EdzhvKJYXpxDbJgkpslyuu_s8GCl7OYftQH_9bsTDwftMQgR9blDWLPXIe1Y77idYfi7X6KW6dsPUIe6o0jDZGkc2P-deMmAXuaggSsaa-vQLW8ukNq6L2Ki3wlJNBKYijEv13RLUjH64R8B7ERDWB8tBIgduUh3kZv1CGftfwe7HHYsHoLw_UcfbdutVvt50kmLzAlexR6YqKNX7_tXqJy8t4d8tzZh8PgrElHpDE93rHSGAVM0OosUF2e-NrL0tF0d6EDz9C-LRNt2b4FktMamCHZ4w7QRpNre1GS9E3VuNJKkOnqIhmlU_N-pPCk6IPi0wp1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر فارس از تانکر منفجر شده توسط سپاه تو تنگه هرمز که حامل گاز مایع بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/alonews/151850" target="_blank">📅 23:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151849">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RETB48sXWFGN8H1NfWiLtohfs1F23hKzE5exYF-gtidEQG-kLDrAsSV9r16r1xw-gfalDdl3KKbLqbKFv1Y3bkqnyVFdtUS6R5LlCPeNQE5swkfd6UE7PxCobJz2e7IDgMhts6wGwGoaOoLp1tCzBJdtHAc0E3VFibILbQcUSL8T5Rxg3E3ucA5my-dOFN0jVpkgTB5uykMiCYClsKIeITS6qp_M2DZEsScn0iQrBX4Rj7f66Tv5n2tA8ZQALkYlBR7bLhYSthFwurJpSZ4ozd6wdO54hVu59rCOWYh9yLLN4d1XGG9o60F1jD8hF0JNQYixObFHgx1APhhdB3uokQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب بیرانوند رفته هتل اردوی تراکتور که برای بازی با الشمال آماده بشه ولی مدیرای تراکتور تو هتل راهش ندادن
😂
@AloSport</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/151849" target="_blank">📅 23:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151848">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6JUSpV8QJp8-P_hWXIXFd1MiBYjpEUPgDoqxlM9OPo3Aa4_I4pWgBkArSab73bogyYGfUJKHA4XlYJYZI9PKfFpIir4sUmrx8npgezWQt993jbtmIKywZIB-XGfwGHF-xXLlX4TT4zx52eXlU06QyYvQhmnZpGghLRq6ZctH3d3OLSwYsOHaE6vF63VndbrvyulBqvxVl0qTjo7yLPYYlrx_fBiFKfJ1ywu6DlfQqAnxQ-acHUZiEH6pIvDaVK8KBSzUTCngYtWwXrQviQtpMTO8K7fhhIOJfFvbUvWIdWztnOhTtplXQrTDdn29NEgYg7nqsy6x-JnsgLI__n2VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میرسلیم: مردم حق ندارن راجع به نفت حرف بزنن چون مال اونا نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/151848" target="_blank">📅 23:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151846">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScskJVGfFXSW6sRavJUGkPN9CiQ6kwaLbnmb78x2QxyOML2uimmIXlwktZqEZAzAaPlH9WJdW-ppY4q8TvtwwKI-YlZXpO0GFQkdqAeiYW_cjnbkaR3TJWbwoZcAPmJi_C_lFOPpLlB4DZraOiJe1mIKcRwR1joCrfia7bnaPanpQlwOHq0IXxouYXamBiagUxk4IsI8IqhWlnTgA89VvfBBrTyjzc6dY0BnJTsNfxmnh5pia-yzEWI5f_kSmtt-hrMMpDXitoYBPL847FWUcJToJTtbrka2cr47CTbe28VvKwlR4UzJKFwkHN0p9diRkM9bcnf4m_39Y7sIRgu5Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بدون شرح
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/151846" target="_blank">📅 23:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151845">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4174043f46.mp4?token=tKSuVlNNw0Z5AJSZtvnmFRkRvE8crwmAq9ozle-F8vuJfBtpuNqsKh3JlOa56x9jMmPnVE4vFgxpPNpeBIpzHCZItBzt6aMch0U1uAwf0Wv8ewacXnprdF5y8flMlE1it7B2mKkwsnz-H7D145DPvwpnv30aUcWfBUBhAnwu7wIZHu2JTt7ySTEg0BwRk1J8huMyz1PdaXCQjNS6b9BDj-hB1j_b21Oxks7ltAxD1EnKYsLn2U-Y6MJFNXlySha9I5tE51LS-N74tZ9mHJ4KVjaHD3nbiv-p_GyOraOS7rfzH0rIyzAlVDzrkynpPNP5BvTYEO74cF6Qi8nuPwD23w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4174043f46.mp4?token=tKSuVlNNw0Z5AJSZtvnmFRkRvE8crwmAq9ozle-F8vuJfBtpuNqsKh3JlOa56x9jMmPnVE4vFgxpPNpeBIpzHCZItBzt6aMch0U1uAwf0Wv8ewacXnprdF5y8flMlE1it7B2mKkwsnz-H7D145DPvwpnv30aUcWfBUBhAnwu7wIZHu2JTt7ySTEg0BwRk1J8huMyz1PdaXCQjNS6b9BDj-hB1j_b21Oxks7ltAxD1EnKYsLn2U-Y6MJFNXlySha9I5tE51LS-N74tZ9mHJ4KVjaHD3nbiv-p_GyOraOS7rfzH0rIyzAlVDzrkynpPNP5BvTYEO74cF6Qi8nuPwD23w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حوثی ها در باب‌المندب
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/151845" target="_blank">📅 22:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151844">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGylcmvWkJr0qZk0d6GpU0TVWr5CDS-H8Bt09Nrpa9-NCIKJ-6NBWPUWBx9y57n01u19mbCN0XZ3iAko4RXE8Msp_HFTlZWIdzoUyRkQ98tTTenvTqZyrOBf94c1jmaiozoq-0vw9CNVBoCO3IswqUVwgXOyfIgoD32lUEDHLBDKenhKjKAag_rnjHvYpitTNgX5AWxbdWmwz3_nUP6qVEPOPwxNb3IqjghxGT0jy-rMNWuZyTWVcuLTfPzmWPa2zM07kWtgWf-kHdvvLLFnYHooUencnyA1hT9hYZpDH0gTYzRpBZ8XPkxQujkWeM6OSXqp1fCdC39gVo0RHsB_Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ریزش قیمت نفت بعد از خبر صادرات گازوییل به آمریکا توسط روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/151844" target="_blank">📅 22:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151843">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره
👇
👇
https://t.me/+WqvKmlByMJMyMjA0
https://t.me/+WqvKmlByMJMyMjA0</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/151843" target="_blank">📅 22:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151841">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
میرسلیم: تیبا و کوییک میتونن با خودروهای آمریکایی رقابت کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/151841" target="_blank">📅 22:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151839">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kntwo3GzKQ8-gLcrznlgPQlNY6_bJnfpCMh12bgZfvwyfxopRLwAd-Bwgxqb_Y4eiX-xp8ISrgwW5QcjJ_OmnMCSFkFb05U3XrlBQpfKQzx4bDGcNgG7nLMx6ANyvSDPDk_fp9iqKJ-AQzF2EONGo2irCJhEyHfwrsBB6r0UaEyEs3BITXY7b2D0x9bqz1lZSlyZ1TkDjP4Q4rzB87C9G2LAZPa9oMIO6B1tKlZPWrqHODUz3suSSYVTDZcjTCjpH7yRHel19JYFKJ4m5pLlI6-dAiWizCCQTGLw8CT7p_Za1dsmd_zEnZVT18bxeRvJlk_cVseYiCy-gySUFBoh8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بنر عجیب در تجمعات شبانه: به یک ۷ اکتبر برای بازپس‌گیری اقتصاد ایران از غرب‌زده‌های اقتصادی نیاز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/151839" target="_blank">📅 22:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151838">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6db7b2cab0.mp4?token=G7mcOm6HLQTzhyVFcgUuEiL8wJnCliHX8eYZ8VZnvmLj-_TyUgJ4gjAh3yD1NtbcCAyFzLWJMzWuuywQW1duTXh2Q755Y4Vs9tyTAtczU9SoIG6LI0-D0m7sQE1R40LdwFaL7Ehogi6SXq8dpaBr95LdlaZYgF6-JMIUbVsqbOmGCrecBPlC2FZ4IYgDoWA_2EYhmTfx_y-2IhjOnlCMTKJkMAQ6MnOb9Kr9wlTshMMRtD3UmwOtmplvcmbDEXPYDFqBO2zeRceVBWgdQpLuTaPl8HDN9wuE0ZnyQYjlHa4Qj-WaTi9i9UKwlxpeFjZL4St6HQK8rlJiUYNuKRZD6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6db7b2cab0.mp4?token=G7mcOm6HLQTzhyVFcgUuEiL8wJnCliHX8eYZ8VZnvmLj-_TyUgJ4gjAh3yD1NtbcCAyFzLWJMzWuuywQW1duTXh2Q755Y4Vs9tyTAtczU9SoIG6LI0-D0m7sQE1R40LdwFaL7Ehogi6SXq8dpaBr95LdlaZYgF6-JMIUbVsqbOmGCrecBPlC2FZ4IYgDoWA_2EYhmTfx_y-2IhjOnlCMTKJkMAQ6MnOb9Kr9wlTshMMRtD3UmwOtmplvcmbDEXPYDFqBO2zeRceVBWgdQpLuTaPl8HDN9wuE0ZnyQYjlHa4Qj-WaTi9i9UKwlxpeFjZL4St6HQK8rlJiUYNuKRZD6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نطق جنجالی ظریف علیه امت معکوس شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/151838" target="_blank">📅 22:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151837">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SU91OPDXSSvoEifjrelKfvr9fVvKMgsjeH-6GmCtGNvfSd7N_YSmcgOyNvBlSEZi9_4BuIFtiIxvMcIKbe5kH8NVUC0fEj6e-RoC7RWSxWjI0WGKFN0QALeOAOjR7hURp3VvrEi0ZcoEgFOIh4F0FCxgEoWMX0UzPGbSzX3M4P1aqO8CTyQF4nFmGrk8wqwxgehSkiuz0b0Q9wHa5-Px6mwGMu2pUtS3zMbsDWP2J9vPWtpw5fmIPo0uGmYztci76SbNWkRuxd1bZmkpSfi4VftwEHHRA7qeSdgtWX51QqkXJwliWafEc-DTgA0pZNDV1XuLnKuWWW6ZxRt-Z7e5PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: کسانی که راه اسکندر را دنبال می‌کنند، به سرنوشت والریان دچار خواهند شد؛ شما زانو خواهید زد
🔴
ما ایرانی‌ها در طول تاریخ با کسانی روبه‌رو بوده‌ایم که خود را ارباب جهان می‌دانستند و به دنبال نابودی تمدن‌های باستانی بودند.
🔴
آن‌ها با آتش و شعله آمدند، اما سرانجام در گردوغبار و با شرمساری رفتند.
🔴
کسانی که میراث اسکندر را دنبال می‌کنند، به سرنوشت والریان دچار خواهند شد؛ شما زانو خواهید زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/151837" target="_blank">📅 22:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151836">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فوری / ترامپ در تروث سوشال: من به‌تازگی گفت‌وگویی بسیار موفقیت‌آمیز با ولادیمیر پوتین، رئیس‌جمهور روسیه، به پایان رساندم که در جریان آن توافق شد روسیه بلافاصله بیش از ۳۰۰ هزار تن گازوئیل به بازار آمریکا و بازار جهانی عرضه کند؛ ۵۰۰ هزار تن دیگر نیز در طول…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/151836" target="_blank">📅 22:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151835">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فوری / ترامپ در تروث سوشال: من به‌تازگی گفت‌وگویی بسیار موفقیت‌آمیز با ولادیمیر پوتین، رئیس‌جمهور روسیه، به پایان رساندم که در جریان آن توافق شد روسیه بلافاصله بیش از ۳۰۰ هزار تن گازوئیل به بازار آمریکا و بازار جهانی عرضه کند؛ ۵۰۰ هزار تن دیگر نیز در طول ماه نوامبر و یک میلیون تن دیگر بلافاصله پس از آن تأمین خواهد شد.
🔴
علاوه بر این، با توجه به وضعیت پالایشگاه‌های گازوئيل، این کشور در مدت‌زمان کوتاهی پس از آن، ۳ میلیون تن گازوئیل تحویل خواهد داد.
🔴
با توجه به کنترل کامل ما بر تنگه هرمز و این خبر بزرگ درباره انرژی روسیه، قیمت گازوئیل برای آمریکایی‌ها و در واقع برای سراسر جهان، با سرعتی بی‌سابقه و به‌سرعت کاهش خواهد یافت!
🔴
کاهش قیمت‌ها برای آمریکایی‌ها، به‌ویژه کشاورزان، دامداران و رانندگان کامیون کشورمان، بزرگ‌ترین اولویت من است.
🔴
این خبر بسیار بزرگ و مهمی است. علاوه بر این، باید درک شود که ایران به سلاح هسته‌ای دست نخواهد یافت!
🔴
از توجه شما به این موضوع سپاسگزارم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/151835" target="_blank">📅 22:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151834">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
میرسلیم: چه کسی گفته نفت ایران متعلق به مردم ایران است؟ نفت ایران مال مردم نیست و متعلق به خدا و پیامبر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/151834" target="_blank">📅 22:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151833">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
واکنش رئیس دیوان کیفری بین‌المللی به تحریم امریکا : دیوان از کشورها می‌خواهد به اتخاذ اقدامات عملی ادامه دهند
🔴
موضوع صرفاً دفاع از یک نهاد خاص نیست، بلکه حفاظت از نظم بین‌المللی مبتنی بر حاکمیت قانون است
🔴
اجازه دهید صریح بگویم، دیوان کیفری بین‌المللی در برابر تهدیدهای خارجی تسلیم نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/151833" target="_blank">📅 22:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151832">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91eb635079.mp4?token=IdQuHo3Px68sZb1ESXwn4Btr1nsL6_rJU49IcpbC9cu-4BO0JSDXhcTvKbPlAP2H2TljxHzdjcXNfa1rs1Ms4H_kMwSF8yi7dyElkCRjMtLYKhHSj0e4EgtO301B2tN94v_vgErnBoPrAjRPMj0BCYsSOWG1GOorbBcXrUBtvWY_itsMoop-4BahBjG22FFzo6FNUJ-A-0JIT19f8UH2asPFq9BnjuEAJfgHgTzDzlGbETJNz3CWIJ6O5TgxuzTnTfcz3WmSRwiq1wRr48-mDER8mASIfRlOOsJZJ-pdaMQ9jHKV4bOfOEtfl_2_4v13gLA3XnIcMyJyYr3Bv19-dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91eb635079.mp4?token=IdQuHo3Px68sZb1ESXwn4Btr1nsL6_rJU49IcpbC9cu-4BO0JSDXhcTvKbPlAP2H2TljxHzdjcXNfa1rs1Ms4H_kMwSF8yi7dyElkCRjMtLYKhHSj0e4EgtO301B2tN94v_vgErnBoPrAjRPMj0BCYsSOWG1GOorbBcXrUBtvWY_itsMoop-4BahBjG22FFzo6FNUJ-A-0JIT19f8UH2asPFq9BnjuEAJfgHgTzDzlGbETJNz3CWIJ6O5TgxuzTnTfcz3WmSRwiq1wRr48-mDER8mASIfRlOOsJZJ-pdaMQ9jHKV4bOfOEtfl_2_4v13gLA3XnIcMyJyYr3Bv19-dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دقایقی قبل پدافند تهران فعال شد که گویا تست پدافندی بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/151832" target="_blank">📅 22:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151831">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LelLaiYN7P45avaJybuIQ4ss8vmDEATTVxFMG7AzgzaDfeQQJlaRFnIFSv7Dm53btONzVErm29mmw0hs0E-sGKWnLvelxeERf9lWo4fOK4FfRYCW6OGw4k5lLzCi5gIn9fQwp3JGezrsit8Zv55nahLDPDFcsxt_KI2XCC71OcVIprc8a8WM4gXgKzu1bwXFcdcHBtkHPIFdOqAdITl7fN_yLZiqp2lwtNJsl4lzEz3uD70K6pvsBjyMwAMKusdkiyypZkMj7WWBNTTlnq0YP3nNo4AOWYQBhYizDYb5YcTavbzXu0owNc_a0xkpqo_LK53DwQa0N-LRxjbgMQrpsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
تبلیغ حمایتی از حمید رسایی در چندین فیلترشکن
!!
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/151831" target="_blank">📅 22:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151830">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دلار بزودی 300میشه
‼️
تحلیل عجیبی که مثل بمب ترکیده
👇
https://t.me/+WqvKmlByMJMyMjA0
https://t.me/+WqvKmlByMJMyMjA0</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/151830" target="_blank">📅 22:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151829">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
معاون امور بین‌الملل وزارت خزانه‌داری آمریکا : ما تمام منابع مالی ایران را قطع می‌کنیم.
🔴
سیاست ما اعمال فشار بر مردم ایران نیست.
🔴
ما اقداماتی را برای قطع جریان ارزهای دیجیتال به ایران انجام داده‌ایم.
🔴
نفت خام با سرعتی نزدیک به سطح قبل از جنگ از تنگه هرمز عبور می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/151829" target="_blank">📅 21:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151828">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
سنتکام: از زمان ازسرگیری محاصره علیه ایران، مسیر ۱۳۳ کشتی تجاری را تغییر داده شده‌است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/151828" target="_blank">📅 21:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151827">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
سنتکام: از زمان ازسرگیری محاصره علیه ایران، مسیر ۱۳۳ کشتی تجاری را تغییر داده شده‌است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/151827" target="_blank">📅 21:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151826">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
معاون وزیر خزانه‌داری آمریکا: بیش از ۱۵۰۰ شخص و نهاد را در ایران تحریم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/151826" target="_blank">📅 21:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151825">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
زمین لرزه در پاناما
🔴
زمین‌لرزه‌ای به بزرگی ۷.۵ ریشتر پاناما را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/151825" target="_blank">📅 21:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151824">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 300 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/151824" target="_blank">📅 21:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151823">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نماینده آمریکا در شورای امنیت: حوثی ها ابزار تهران هستند؛ ایران باید حمایت از آن‌ها را متوقف کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/151823" target="_blank">📅 21:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151822">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ایلان ماسک رسما به اپراتورهای موبایل اعلان جنگ کرد!
🔴
شرکت SpaceX با یه قرارداد ۸ میلیارد دلاری، فرکانس‌های رادیویی با باند پایین ۸۰۰ مگاهرتز رو خرید.
🔴
ویژگی این موج‌ها اینه که خیلی راحت از دیوارها، ساختمون‌ها و درخت‌ها رد می‌شن و گوشی‌های معمولی هم ازشون پشتیبانی می‌کنن.
🔴
علاوه بر این، مجوز ارسال ۱۵ هزار تا ماهواره نسل جدید رو هم گرفته تا اینترنت ماهواره‌ای پرسرعت رو مستقیم روی همین گوشی‌های هوشمند معمولی بیاره، بدون اینکه نیاز به خرید گوشی خاصی باشه.
🔴
ماسک داره کاری می‌ کنه که به‌ زودی کل شبکه موبایل از روی زمین به فضا منتقل بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151822" target="_blank">📅 21:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151821">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
کاخ کرملین: سفر به اروپا اکنون برای شهروندان روسیه خطرناک است، این امر آشکار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/151821" target="_blank">📅 21:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151820">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c59f52ebc.mp4?token=DeZ303KLV2jU512s2qs9rePkEQ1o6x-IsLK3Qln8xsEQ3UOT1iiDHxZuM9kTrkMEpC795i2Ehwb1IdmVFGbIUX-CQvN-iJdG_x3NCZZrzvZUntN9pl9VFHcMK80cYifDxNDgKTbD6x_KWgy-jK8jFFQ_zismafHaLN5LH2pLRYp6AX-5EhUdXMywolOp1pT3Wkx0EaNRB5aB5Tbwtv2U4P0yG8Ptt8trOloMyxq_iQvRQAn_uCWeDNnPBdLRdr1AFCj_UFNsSNb6t2FMSgSjQNqmXrnG8mFJ9sKKdXDJjC_hCLNBwThqwtDxnifLcP4Jn3Z8gmm3S94I3AZn8OonQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c59f52ebc.mp4?token=DeZ303KLV2jU512s2qs9rePkEQ1o6x-IsLK3Qln8xsEQ3UOT1iiDHxZuM9kTrkMEpC795i2Ehwb1IdmVFGbIUX-CQvN-iJdG_x3NCZZrzvZUntN9pl9VFHcMK80cYifDxNDgKTbD6x_KWgy-jK8jFFQ_zismafHaLN5LH2pLRYp6AX-5EhUdXMywolOp1pT3Wkx0EaNRB5aB5Tbwtv2U4P0yG8Ptt8trOloMyxq_iQvRQAn_uCWeDNnPBdLRdr1AFCj_UFNsSNb6t2FMSgSjQNqmXrnG8mFJ9sKKdXDJjC_hCLNBwThqwtDxnifLcP4Jn3Z8gmm3S94I3AZn8OonQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس: می‌دانیم که مردم نگران هزینه‌های معیشت هستند و این موضوعی است که هر روز با تمرکز کامل بر حل آن متمرکز هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/151820" target="_blank">📅 21:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151819">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سؤال: اریک دیترز می‌گوید کیمبرلی گیلفویل از او ۱۰۰٬۰۰۰ دلار برای دسترسی به مقامات دولت ترامپ خواسته است.
🔴
جی‌دی ونس: این‌ها ادعاها هستند. شما نباید پیام‌هایی که به‌طور ادعایی افراد داشته‌اند یا داستان یک نفر را برداشت کرده و به نتیجه‌ای برسید. من فکر می‌کنم این کار احمقانه است. بیایید ببینیم حقایق چیست.
🔴
اگر اتفاقی بد افتاده باشد، آنگاه افراد باید عواقب آن را بپذیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/151819" target="_blank">📅 21:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151818">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
سؤال: شما زیاد درباره ایمان مسیحی خود صحبت کرده‌اید. این موضوع چگونه با اعلام‌نامه پنتاگون که مایل است اعدام شلیک گلوله به شلیک‌کننده فورت هود را به صورت زنده پخش کند، همخوانی دارد؟
🔴
جی‌دی ونس: نمی‌دانم که آیا این اتفاق واقعاً می‌افتد یا نه. این مرد بدترین حمله تروریستی در خاک آمریکا پس از ۱۱ سپتامبر را مرتکب شده است.
🔴
اگر در نهایت این اعدام به صورت زنده پخش شود، من آن را تماشا نخواهم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/151818" target="_blank">📅 21:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151817">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43bfffd5ce.mp4?token=SM6p_Z_h_dWldGOlOmmsZETV90UwNgjD1OgOUPBE28qUpIo24EOeZb9jX6BWyIDjCmuW4uzKFIp-4EkMkTTchWgrOPckwS1kHTrTFxlgPPqGeekEZVCy4XpsM9zwUBMT_EN6YDnWMxLflDd2WdlCxGt1bG1dErpdI5SUvKhC-PBZyj2Lag7C0yxlBmZ_lffgL6dB6sYPDgKeUIKQQapogAcdUyLNK2JCzorCJJZNfDmeCFE5d4kTQc3e1o1h0mLhab8ZhFEfolwF9iZym3i4O6a9aFcMvAI1feBUuKbSw8uH-CGuaSeSuxgma7XcIWtzG4jqWk1T29exEqUTZdHQ2xjHlpNDO2oqZhxdNH6mHG0ds5RJYlPxQoOtutjRaZ9km0YGjqnn2Cg58uZIL3U0NdoIiOWYabjHU_Mki5TMz3Bv3FXYR51SJae2Vt3XUXYOqPDCMeZv8Ciz50EuiHba_CubUtfbfKphelOwRBw-8zEwAto-5gJ6E161QvCIRS5UsKafhEOkXCMeSuR-XLNAw8WDIS0m2r_S9iPuEQIq718_hralXSZFBKmKfOvh975HDKN1-F606vNiMWpiQEz28j4voGxyvk0FG6hz6LHetXhVNcWjhEhfRHSL6UVhuXfh_qc_7T4XZ_iE5N5nW4SvwT28FBKss5DGArnC4JsqRZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43bfffd5ce.mp4?token=SM6p_Z_h_dWldGOlOmmsZETV90UwNgjD1OgOUPBE28qUpIo24EOeZb9jX6BWyIDjCmuW4uzKFIp-4EkMkTTchWgrOPckwS1kHTrTFxlgPPqGeekEZVCy4XpsM9zwUBMT_EN6YDnWMxLflDd2WdlCxGt1bG1dErpdI5SUvKhC-PBZyj2Lag7C0yxlBmZ_lffgL6dB6sYPDgKeUIKQQapogAcdUyLNK2JCzorCJJZNfDmeCFE5d4kTQc3e1o1h0mLhab8ZhFEfolwF9iZym3i4O6a9aFcMvAI1feBUuKbSw8uH-CGuaSeSuxgma7XcIWtzG4jqWk1T29exEqUTZdHQ2xjHlpNDO2oqZhxdNH6mHG0ds5RJYlPxQoOtutjRaZ9km0YGjqnn2Cg58uZIL3U0NdoIiOWYabjHU_Mki5TMz3Bv3FXYR51SJae2Vt3XUXYOqPDCMeZv8Ciz50EuiHba_CubUtfbfKphelOwRBw-8zEwAto-5gJ6E161QvCIRS5UsKafhEOkXCMeSuR-XLNAw8WDIS0m2r_S9iPuEQIq718_hralXSZFBKmKfOvh975HDKN1-F606vNiMWpiQEz28j4voGxyvk0FG6hz6LHetXhVNcWjhEhfRHSL6UVhuXfh_qc_7T4XZ_iE5N5nW4SvwT28FBKss5DGArnC4JsqRZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی به ایالات متحده: کل اقتصاد پوتین را از کار بیندازید. دهان روسیه را ببندید. با فروش‌های خودشان را تغذیه نکنید. فقط تحریم‌هایی بر تسلیحاتشان اعمال کنید.
🔴
دسترسی به استارلینک را به اوکراین بدهید. شما وقتی به ایران پاسخ دادید این کار را انجام دادید. همه چیز آنجا کار کرد. اسرائیل به طور کامل آسمان بر فراز ایران را کنترل کرد.
🔴
بنابراین به این معنی است که وقتی به آن نیاز دارید، به همان شیوه کار می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/151817" target="_blank">📅 21:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151816">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
گزارش ها از اختلال شدید در جی‌پی‌اس تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/151816" target="_blank">📅 21:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151815">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRIxmfDpuFh-ZX_HktVlSy_fEqD_7vgNeM7XXgVh3bAU422YDIX2_gZ-MjEqys6iVSbId3B7c1M8bO-8EPCOyO1EdqiLAgIHonxgM1S-wRVA3-5ZcJTQK_yspSg8K8zZBZmNlinU_Ng2d019FEhwpUmw_kHIe3gVNeLJV6cTLZ-DsXF9LR4vSIyNi4S30LUGK1UaBMywU5hziIIriY1H_lCqFhA3zbA26rZqhwenrXp-2wuNI11Be430v1HqqWxvSxZE6qSM3Ou2Qkfw8MoZu2An6cftSpksX-HU8bsToN5pOBRhvDdrVSkzVMsYfNVDGbdX5VtGK6BLDtFgpqnXTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دفتر نخست‌وزیر اسرائیل:
کمیته نوبل، حس اخلاقی خود را از دست داده است
🔴
این کمیته، بالاترین جایزه خود را به فردی تعصب‌آمیز اهدا کرده است که حرفه خود را بر پایه اختراع و انتشار اتهامات بی‌اساس و نفرت‌پراکنانه علیه تنها کشور یهودی بنا کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/151815" target="_blank">📅 20:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151814">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
دادستان کل امارات: کمک‌خلبان شرکت هواپیمایی فلای‌دبی قصد داشت در فرودگاه بن‌گوریون، «عملیاتی انتحاری» انجام دهد
🔴
او طرح خود را از حملات ۱۱ سپتامبر الهام گرفته بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/151814" target="_blank">📅 20:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151813">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ : اگر ایرانی‌ها به سلاح هسته‌ای دست پیدا می‌کردند؛ ابتدا اسرائیل را نابود می‌کردند و سپس کل خاورمیانه را منفجر می‌کردند!/ بعد از خاورمیانه، نوبت آمریکا بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151813" target="_blank">📅 20:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151812">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EplhReR5YNK1_MEZwYXCXgLBW5cdJpgrryXmRpQreiXZXcLCIhuAJPO3GKb8Mt3feTjR4u7EjtFZtXJPAOflbTB7KYKYDuyr7lzG3QqOr40z-1EWAQvtSXlfugfq6GEDoOubqNVzHRW9oJcbzfyfL1lXNwA7ZEFS1DhPwlbD8C0CdO3eL7kAsdn-GtngNwQ-b_DSgiJ-qcuoRvf1fCm-cE3cUFt7LXO7FANOQN3oRlrRc_ANLKrYPqdxVQohc-ndIQcrVJpViZDdM8jjMu0AO-LjeVOsns1BQKFEMz9suEup22ltKMP_3Prj7NxhfZ2bRbe1y1sQ2bcoaX2eq1cPuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی به آمریکا: برای تکرار شکست‌های تاریخی از ایران آماده باشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151812" target="_blank">📅 20:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151811">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
اگه دنبال درآمد دلاری هستی بیا
👇
https://t.me/+WqvKmlByMJMyMjA0
https://t.me/+WqvKmlByMJMyMjA0</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/151811" target="_blank">📅 20:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151810">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ: ما یک جنگ بزرگ در ونزوئلا داشتیم. این جنگ یک روز طول کشید. آن‌ها حتی در مورد آن صحبت نمی‌کنند. ما یک جنگ فوق‌العاده داشتیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/151810" target="_blank">📅 20:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151809">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3cb81c36f.mp4?token=KndqIYz4lyZUhgNhuUy-GGodMQH5RyNn8jQSTNYiFGPpS5lzBdbK4WmCKSN0q9R1KRvcrwkkiU-b5Cb_qsmG84HTo8ysDFy33vLiAs2k53TfiRU9OUWHiV4eugj7dHeIm70UKy4qF5amPK0NT-ETmpuKZOFlo0coCDTvD-ieHvAqQ8BoLupRGo0VFySwlvX90-kYuQzcjco41UdJaE-hnucHhfsYTZkFFrfXhAV84mjXb_uUVxeAUgpwh_1VopLjUUI4fgmNRxTkh3LlveQvuvblr3A8s6Heb2cpUC-n_fI6d2l1207qG28GXeKPSX89DPTChqRr3-w7KorGpe-cIgRuZx-r3PCN4ASVlqU2RqSu1DznKQW3NjP9s7_avlS_31Z7oub7NVGs5bWa5didnHhFsP9qfNkFsySNu2vbMfFPK-8eR5hs4K98onBXeWv_NLcss_c_lLhNtdvyyly-YjwjE8Q_P33Qy4lV8XwBarhWf07LyzkA-bu9zYn0UjsnjWiMjKkhaiDzMBQq5rCFCsFRG_M1LWHJYBNB4aOQjLcK2LmS_QqL2XMSwWPgf8rS84gBkqdPhDrdzDHhUTEI3kfk-q6cUljkQmMx73UHlSmTb-hUTqZSBQ3OcsGPKFkvO0w1VgkKPq7DVTYqQ83x1edzcayjXOjJwFhhAEr75DY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3cb81c36f.mp4?token=KndqIYz4lyZUhgNhuUy-GGodMQH5RyNn8jQSTNYiFGPpS5lzBdbK4WmCKSN0q9R1KRvcrwkkiU-b5Cb_qsmG84HTo8ysDFy33vLiAs2k53TfiRU9OUWHiV4eugj7dHeIm70UKy4qF5amPK0NT-ETmpuKZOFlo0coCDTvD-ieHvAqQ8BoLupRGo0VFySwlvX90-kYuQzcjco41UdJaE-hnucHhfsYTZkFFrfXhAV84mjXb_uUVxeAUgpwh_1VopLjUUI4fgmNRxTkh3LlveQvuvblr3A8s6Heb2cpUC-n_fI6d2l1207qG28GXeKPSX89DPTChqRr3-w7KorGpe-cIgRuZx-r3PCN4ASVlqU2RqSu1DznKQW3NjP9s7_avlS_31Z7oub7NVGs5bWa5didnHhFsP9qfNkFsySNu2vbMfFPK-8eR5hs4K98onBXeWv_NLcss_c_lLhNtdvyyly-YjwjE8Q_P33Qy4lV8XwBarhWf07LyzkA-bu9zYn0UjsnjWiMjKkhaiDzMBQq5rCFCsFRG_M1LWHJYBNB4aOQjLcK2LmS_QqL2XMSwWPgf8rS84gBkqdPhDrdzDHhUTEI3kfk-q6cUljkQmMx73UHlSmTb-hUTqZSBQ3OcsGPKFkvO0w1VgkKPq7DVTYqQ83x1edzcayjXOjJwFhhAEr75DY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: مقامات شهر نیویورک نقشه‌ای را منتشر کردند که مناطق مختلف با اکثریت قومیتی را نشان می‌دهد. این نقشه شامل مناطقی مانند "سنگال کوچک"، "هائیتی کوچک"، و "یمن کوچک" است، اما "ایتالیا کوچک" در آن گنجانده نشده است.
🔴
ما بلافاصله برای رفع این مشکل اقدام خواهیم کرد، در غیر این صورت، هیچ یک از میلیاردها دلاری که آنها می‌خواهند هدر دهند، به آنها اختصاص نخواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/151809" target="_blank">📅 20:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151808">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a77afe8c6.mp4?token=IPQG2BqydkI0MUBXdZi0-f7Cc3XQPz_c-ez39Cc84_pcFlMfn0xq1xoOToNmI5xmKCHSJWmp1R_U-G_ZI-RMC2EhSnOq7m_VzioNcUL4S05Hmcx89d608FUxXlV_Od-pnx242eqCEo_x-um9qlEUDf11BXRNrXmISFFmmXQepThOKWEv3Wuxj0hBsJ6aJ_DFsME-SK6lukpA59gzQHZM-HdoPF0r9ILJZsCXGoL565Y7DkKdl0JJbdKlJ8lKEuZLO6C-36pkW6kw_J6HaIvyHWTz0fWEceIjET3xBZn5bgUeCKF_3uL4SRjzOhVyVhl7LS1lHoXL8kH0pLp8r4NRVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a77afe8c6.mp4?token=IPQG2BqydkI0MUBXdZi0-f7Cc3XQPz_c-ez39Cc84_pcFlMfn0xq1xoOToNmI5xmKCHSJWmp1R_U-G_ZI-RMC2EhSnOq7m_VzioNcUL4S05Hmcx89d608FUxXlV_Od-pnx242eqCEo_x-um9qlEUDf11BXRNrXmISFFmmXQepThOKWEv3Wuxj0hBsJ6aJ_DFsME-SK6lukpA59gzQHZM-HdoPF0r9ILJZsCXGoL565Y7DkKdl0JJbdKlJ8lKEuZLO6C-36pkW6kw_J6HaIvyHWTz0fWEceIjET3xBZn5bgUeCKF_3uL4SRjzOhVyVhl7LS1lHoXL8kH0pLp8r4NRVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کامالا هریس معاون جو بایدن: آیا کسی نام خانوادگی کامالا را می‌داند؟
🔴
او معاون رئیس‌جمهور بود؛ ولی هیچکس هیچ ایده ای نداره اون کی بوده، هیچ‌کس نام خانوادگی نمیدونه فقط میدونن کامالاست، حتی امروز، آیا کسی فامیلیش رو میدونه؟ جدی میگم؟ نام خانوادگیت چیه؟ (خنده) ما می‌شناسیمش اون کامالاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/151808" target="_blank">📅 20:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151807">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1280b1bc1.mp4?token=ZSpzciBp5W8wmDTXMKiAT0oIs7lyAdR1_I3xw2ph-SlJePHjFpJKyJr2-Tk5YFR3Cqctbe4YZC8tUhemuPosSCEzrVYrvBWo9IsRUBvOTp8wIBwwtgBKQaCAL9rYDFN-sTXQWBv01403Vnout-eHaiWPIIfoyuk2KObXaZ56tJVXsdij59J8yuomNwZek2A5aw_VIE7eHisdDYUVROuKEJRDmv3BPOw5WpZyQ2bT5ZOZXXIQiw7aTQFGxHN4r-DeBCRl9eDAbsGT--ceUcz_IOsSJqzifxhez4Cc4KN90ky7JiAY2lf3eaYoc9aUcGT1p4-T9p7WeilBBwvgKGinmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1280b1bc1.mp4?token=ZSpzciBp5W8wmDTXMKiAT0oIs7lyAdR1_I3xw2ph-SlJePHjFpJKyJr2-Tk5YFR3Cqctbe4YZC8tUhemuPosSCEzrVYrvBWo9IsRUBvOTp8wIBwwtgBKQaCAL9rYDFN-sTXQWBv01403Vnout-eHaiWPIIfoyuk2KObXaZ56tJVXsdij59J8yuomNwZek2A5aw_VIE7eHisdDYUVROuKEJRDmv3BPOw5WpZyQ2bT5ZOZXXIQiw7aTQFGxHN4r-DeBCRl9eDAbsGT--ceUcz_IOsSJqzifxhez4Cc4KN90ky7JiAY2lf3eaYoc9aUcGT1p4-T9p7WeilBBwvgKGinmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: آن مردان نظامی جذاب را می‌بینید؟ همه‌شان ایستاده‌اند. قدبلند و مرتب هستند.
🔴
تبهکارها نزدیک می‌شوند، به آن‌ها نگاه می‌کنند و می‌گویند: «من از اینجا در می‌روم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151807" target="_blank">📅 20:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151806">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ: ایران احتمالاً ابتدا به مناطقی مانند سن‌دیگو و لس‌آنجلس حمله می‌کند، زیرا مسیر پرواز موشک به سمت این مناطق بسیار مناسب‌تر و آسان‌تر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151806" target="_blank">📅 20:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151805">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
دولت سریلانکا: برنامه ای برای کمک به ۱۹ کشتی ایرانی که در آب‌های بین‌المللی نزدیک این کشور لنگر انداخته‌اند و با کمبود آب، غذا و سوخت مواجه هستند، نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/151805" target="_blank">📅 19:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151804">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ : کریستوفر کلمب برای ما یک قهرمان است.
🔴
ما کریستوفر کلمب را زنده کردیم
🔴
کریستوفر کلمبوس شاید نخستین ایتالیایی-آمریکایی تاریخ بوده باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/151804" target="_blank">📅 19:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151803">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
مدارس هرمزگان فردا تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151803" target="_blank">📅 19:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151802">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری / ترامپ: به زودی مانع دستیابی ایران به سلاح اتمی می‌شویم
🔴
رئیس جمهور آمریکا: مانع از دستیابی ایران به سلاح اتمی شدیم و به هر طریقی که شده، به زودی این کار را تمام خواهیم کرد.
🔴
جنگ با ایران به طریقی بسیار زود به پایان خواهد رسید و ما توانایی پایان دادن به آن را به هر دو روش داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/151802" target="_blank">📅 19:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151801">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ترامپ: ما دیروز، ۲۸ میلیون بشکه نفت را از تنگه هرمز خارج کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/151801" target="_blank">📅 19:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151800">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
وزیر آموزش‌وپرورش از تعطیلی احتمالی مدارس خبر داد و گفت تعطیلی ها بر اساس شرایط هر منطقه طی روز های آینده تعیین می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/151800" target="_blank">📅 19:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151799">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
میرسلیم، عضو مجمع تشخیص مصلحت نظام: تیبا با خودروهای خارجی قابلیت رقابت دارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/151799" target="_blank">📅 19:18 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151798">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwAUT8LRpnq_qWPTm0tmRrJFkeGTsSnP3x4fuzkZD67cQqPRpsYZfsL53TC_Ctwp6gRxNfrwpj-TYpXWR1oMpIk6Qv64e7MYUw2LQZ6BwG3COWiEmUKC9ixc5_heTh41NPJCAet-j0RKR-UKeMEC9QmUwaKJ1PP3vbKN8c_29JewaiTKfPvSNrdG9TtC-ge-6C6uP0KOl_pWD0k72Q_j1a3F5WYRblVLChmCp3ogci-_3LH5Z51Dp-kX0H_XdUYjWhOELtSfX7PYEC1_ITNRLovKd7Ur2VubYFvgQQAUrdcP2wdLcNjKZHdu7YqzTM-DYNVtDDXP6ahv731hcqa2Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک منبع نظامی به الحدث گفت که نیروهای حوثی مقادیر زیادی مین در سراسر منطقه باب المندب کار گذاشته اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151798" target="_blank">📅 19:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151797">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
رویترز: آمریکا ساعاتی پس از برنده شدن قاضی پیشین دیوان کیفری بین‌المللی در جایزه صلح نوبل، این دادگاه را تحریم کرد
🔴
این تحریم دامنه‌ای بسیار گسترده‌تر خواهد داشت؛ زیرا ممکن است شرکت‌هایی را نیز مجازات کند که به خود دادگاه خدمات ارائه می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151797" target="_blank">📅 19:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151796">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
امام جمعه تهران: توقع مردم، تجدید نظر در دکترین هسته‌ای ایران است
🔴
از ان پی تی خارج شویم به غرب می‌گویم هسته‌ای ما به شما ربطی ندارد، غلط کردین؛ برید گم شید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/151796" target="_blank">📅 18:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151795">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VDHBSYxIsdSpJf9j0wI1hG8UG3-9mJLoP3sQabTOBJ6v__L7YPYvTtaUYbcRXv1rZGgsM6DiD1NnTFMHhqE_tEmVggKvpEvcxH3sUx6iO8MsiAqDKDOgdWFnI0gMQ5VhGW36WzGZBPxvsl9RHBclxNMARoz4JrFokO_shN0vG8nGkBxYfDicOKkAaeJPTRS7R3EFIGptRQhl-KbhjOGo9oMyoS3rz6ubXcl2vduyzkTVSxkWw6ja65sEKeQDp2ovQPnnDbOGmeYf9GinnO_-_p8mtUx5TcvE__p7mU5TY1zNoXnbo5NwyMN1pIlVaTAeMXlugXxH2iEB3KzTsKI8rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اطلاعات بیشتری در مورد کشتی که در فاصله ۱۳ مایل دریایی غرب منطقه الخلیج (الجزیره) در امارات متحده عربی غرق شد، در دسترس است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/151795" target="_blank">📅 18:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151794">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b67cd80c6.mp4?token=J3hFqVALBYQ2TCXG7pUy0hLfIH_tRgcUHv_orRqQfHyfMo_1yS5lUj7uglQVG3UNXc5IQZmr2nOfdbDTUOEASMw8ingGpIvgPeFcg2Vw8XXVsieWnWdcJnkqE7uWJ28RLcHn65PvnHHI73hv8kfkuftL-AFtgHiLm6_xhNqjGdLe1Tf7ztM9_026clyf3QICzCR9A4Btt6uphW19c2czzZ3dvYGVTbpIdtuIbFDEAlJ3U-GlWhJnjKk55oBl02fWabgo09qcyl68dWlgbp20192Wz7tHHZXuFyJun3Ud8bhbJAhct94TA6xohOty9Pb9YYrGUuoPgpfxzONxO4K9Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b67cd80c6.mp4?token=J3hFqVALBYQ2TCXG7pUy0hLfIH_tRgcUHv_orRqQfHyfMo_1yS5lUj7uglQVG3UNXc5IQZmr2nOfdbDTUOEASMw8ingGpIvgPeFcg2Vw8XXVsieWnWdcJnkqE7uWJ28RLcHn65PvnHHI73hv8kfkuftL-AFtgHiLm6_xhNqjGdLe1Tf7ztM9_026clyf3QICzCR9A4Btt6uphW19c2czzZ3dvYGVTbpIdtuIbFDEAlJ3U-GlWhJnjKk55oBl02fWabgo09qcyl68dWlgbp20192Wz7tHHZXuFyJun3Ud8bhbJAhct94TA6xohOty9Pb9YYrGUuoPgpfxzONxO4K9Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو دربارهٔ تحریمِ دادگاه کیفری بین‌المللی: یا دادگاه کیفری بین‌المللی تهدیدهای خود را متوقف می‌کند، یا ما دادگاه کیفری بین‌المللی را متوقف خواهیم کرد.
🔴
و ما انتظار داریم متحدان ما، بسیاری از آن‌ها که عضو دادگاه کیفری بین‌المللی هستند و برای دفاع خود به نیروهای نظامی آمریکایی متکی‌اند، این دادگاه سرکش را مهار کنند
🔴
اگر این کار را نکنند، ایالات متحده کمپین خود برای تخریب دادگاه کیفری بین‌المللی را تکه‌تکه ادامه خواهد داد، تا زمانی که آمریکایی‌ها دیگر تهدید نشوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/151794" target="_blank">📅 18:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151793">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
بقائی به فرانسه: استفاده نامتناسب از زور علیه تجمعات دانش‌آموزان را متوقف کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151793" target="_blank">📅 18:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151792">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: امارات و عمان در اجرای سیاست انزوای کامل ایران با واشینگتن همکاری می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151792" target="_blank">📅 18:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151789">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iAw4H6YChx36A4r-MgwdD7RulkQH9mTr8nmF0Spr2NUS7PWdKHQlfEr-yYEWnX_nyXUXlFovR_r55dCuDrSPa5-PAxGvGhcxCQJY6DFukQ9W21iTLbX4q8hnUlQQRUAzgiyLa8KUU__ppb4dvSSqHM3pXMP88AsZvvhmTGYXwAqtzD7M4Xva08966_xhEy5mO1GVKkdUjsBtWDPeO24smvWweliAfRKXN4EzhGdkAzpo0i6LhNvaJ7gRYl6HTpHI6tSo1EcOAe9eB9yX-naXAHxmfdOfFUjAcD1Dt3ujuadIKu7ShlmcnHF9Eb_Cbu4UlqO9OVeesiWwH_G4TY0B-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H07mjEVEwrnLW26DsgYiThZhCXXf_GLSjrMDju5Ld3Z_PyjYeMvYOv0iHlNDgXEgKhuNrJJTVjwwFarBZZL8Pk36HjivI10vG-QKf8wrB0FcKnq61GU2nCSea9KFdXlfN7kcEJXBqFlLnAbxay3fri-k0tehrkWCBOv4nW0ORajlcLlqvHTMQ1M7NT4f1tyM-5VXt3XT8KkbRrr2YCTn4aohLg-_VKP4psy1RZo8zul4CG2W8iZ0J5Nqn0TXuQfKp8MPxssAjTqL6u6kpkU07VzolNMkTuWAoz6fwGyZRhV89yvusgV6ZEMN450kBGAVNoZ1d9UooKKPjkMi3nRelw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c93bb666a.mp4?token=sMMasTh8hRNaSUMDOj7JclPQwbc5_Hc5vnlkhj9FDzUXFrnqAVDQcphu5_z16dKsWeSocJ1vyeEqorxPTE1-nczmXuwoAJjxrtYGx1MyzQhOmm5lpuoP2ZBzbdQ3DpMDYu-nIsKrf3Hlt3zqE8FAZY6BUpyc3IigR6TcMDhl8OuEsW9j4Nd6_DXq-4Ur6rwqcchlRuEjMyt8MkSNWjgpnJsCcyQ_sdcNCAaW4dNGA11u6Z4lEDBwueB2BBOPutZxbvwIxHXAykK3austALe4NgsrLpH_zKEleX6MtkC8fq_YQulPw51zn8zgCaBycxKfseW6mQSSfLEx00CM1MUz-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c93bb666a.mp4?token=sMMasTh8hRNaSUMDOj7JclPQwbc5_Hc5vnlkhj9FDzUXFrnqAVDQcphu5_z16dKsWeSocJ1vyeEqorxPTE1-nczmXuwoAJjxrtYGx1MyzQhOmm5lpuoP2ZBzbdQ3DpMDYu-nIsKrf3Hlt3zqE8FAZY6BUpyc3IigR6TcMDhl8OuEsW9j4Nd6_DXq-4Ur6rwqcchlRuEjMyt8MkSNWjgpnJsCcyQ_sdcNCAaW4dNGA11u6Z4lEDBwueB2BBOPutZxbvwIxHXAykK3austALe4NgsrLpH_zKEleX6MtkC8fq_YQulPw51zn8zgCaBycxKfseW6mQSSfLEx00CM1MUz-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات هوایی عربستان به صنعا
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151789" target="_blank">📅 17:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151788">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
صداوسیما: با درایت مسئولین و پیگیری ها، سیب زمینی ارزان شده و به کیلویی ۷۰ هزارتومن رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151788" target="_blank">📅 17:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151787">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVeHCJNeGzL94xJSLLjO6I5dKZyvoL1ybijcBe0JO0CWwcMX3GLQD5k_ZyolaDnVnlmXXiU_MNGCuK1ON48Yq-RO2godW4tlXo3MKZsCwuOYjreWTPZLF9Q-I1pDyeNcfKYoiHd0BhlaXHVvNKBQjBbB9wqjKfqrztE6FQddfA9vf0mAk08atEcfv4YYRS54BGDvJZmJpwIa5Uh_-u4kt_j06vsYYEHGXlJ4weohfE2W43T5TeFsEpc4utbUsWmxypggHpg08-vO0p3N7rO6ommXO5pyZ-ScggNEc6VE2vjVcJhHvIUzkgfdfXzZMsegwKk80vSiSL40AvDjHPlu3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز عملیات تجارت دریایی بریتانیا (UKMTO) پس از دریافت گزارش های متعدد مبنی بر اصابت گلوله ناشناخته به یک کشتی در حدود 13 مایل دریایی غرب الجزیره، امارات متحده عربی، در حدود ساعت 10:00 امروز UTC هشداری صادر کرد. این برخورد باعث آتش سوزی شد که از آن زمان تاکنون خاموش شده است. وضعیت خدمه، میزان خسارت و هرگونه تأثیر زیست محیطی مشخص نیست
🔴
مقامات در حال بررسی هستند. این حادثه در خلیج فارس و خارج از تنگه هرمز رخ داد. این در پی حمله روز چهارشنبه به یک نفتکش در حدود 51 مایل دریایی شمال مدینه الشمال قطر است که بنا بر گزارش‌ها تلفاتی برجای گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/151787" target="_blank">📅 17:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151786">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEESZojdXnvZyIVHqvY_0TwMkKmcD3s8IBmd7ltAaDzqawj00LL-VvcLKWTpl6SiFBFJYdsw2sfjh0KmD7S37OGmrHZWPIwnbKP7tQAonwqrPSoFpg-BAW2wyet3QUvNNUwQ8hd-K40EbUopqLyRTdsgsSpFdemIFFOw3mHLXUX2Cr8-tYaQdeCIoxT_1kvhTxJiL7JCZwq1k7YHamkhSUwzDVrCnkkT7OE2JLp8P9HmH-TMe3uiLgBG5cp89qmTQuMPIqUMcqKsYrN94QkDgEaOPtPxsC7x_Brg2Y1mQTVBk3w9xs26ruIXpKXRh7O7RedkHof-xS7vWst1430zZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: مردم آمریکا میگن که آمریکا در مقابل ایران شدیدا شکست خورده
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/151786" target="_blank">📅 17:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151785">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
وال‌استریت ژورنال: پالایشگاه‌های نفت آمریکا از جنگ ایران و اوکراین سود‌های کلانی به دست می‌آورند
🔴
اختلال در فعالیت پالایشگاه‌های خاورمیانه و حملات اوکراین به پالایشگاه‌های روسیه، آمریکا را به آخرین تأمین‌کننده عمده سوخت در جهان تبدیل کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151785" target="_blank">📅 17:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151784">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
فوری/ وزیر خزانه‌داری آمریکا: دولت آمریکا در حال رایزنی با پاکستان و ترکیه برای بستن تمام مسیرهای زمینی ورود و خروج از ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/151784" target="_blank">📅 17:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151783">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
دقایقی پیش یک بمب کنار جاده‌ای در مسیر حرکت یک دستگاه خودروی پلیس در چشمه زیارت زاهدان منفجر شد.
🔴
اخبار اولیه از جراحت چند نیروی پلیس در این حادثه حکایت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/151783" target="_blank">📅 17:18 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151782">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
هم‌اکنون گلوله باران مواضع حزب‌الله در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/151782" target="_blank">📅 17:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151781">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a74a32557b.mp4?token=c4dGzkuqax9UcKXjSsfFS3HqoeWtkdQeF2EZNEe8kZXmTweoA9j0amtQ-4oVQpqu6hjJuHAENnEvxmZhhMnZ1uQTPd604wijUJCrmPFyH7T70Be1T0PcF7AlkIU8w8tiTcL2h3thiqLTlzykYQc7Df2SWzWp9iAIcvyU05AKGwAycTwY56yIQCteRrIxpi5u3LfF5GXvcGK55lUadmmqB_rF0qiV4ifJuToMxiFfDy_56XYxZWoxYxjOznvKUkzkdvBTxunI_tt1SWzJD7IPR6IQ8O_5FVFi0g52Rk27IzU34ZmFW8OQoZ802V_ObQcbVRwmK6m2OhK-fHOG3Mmvwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a74a32557b.mp4?token=c4dGzkuqax9UcKXjSsfFS3HqoeWtkdQeF2EZNEe8kZXmTweoA9j0amtQ-4oVQpqu6hjJuHAENnEvxmZhhMnZ1uQTPd604wijUJCrmPFyH7T70Be1T0PcF7AlkIU8w8tiTcL2h3thiqLTlzykYQc7Df2SWzWp9iAIcvyU05AKGwAycTwY56yIQCteRrIxpi5u3LfF5GXvcGK55lUadmmqB_rF0qiV4ifJuToMxiFfDy_56XYxZWoxYxjOznvKUkzkdvBTxunI_tt1SWzJD7IPR6IQ8O_5FVFi0g52Rk27IzU34ZmFW8OQoZ802V_ObQcbVRwmK6m2OhK-fHOG3Mmvwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تریتا پارسی: بعید می‌دانم جنگ سوم از جنس جنگ اول و دوم آمریکا باشد که به بن‌بست خورد
‏
🔴
اگر چینی‌ها درک می‌کردند که دور سوم آنقدر بزرگ است که آن‌ها نمی‌توانند خودشان را از تبعات آن دور کنند، ممکن است وارد عمل می‌شدند تا جلوی آن را بگیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151781" target="_blank">📅 17:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151780">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
پزشکیان در نشست سران کشورهای مشترک‌المنافع: جنگ‌های اخیر منطقه نشان داد که امنیت و ثبات منطقه‌ای مفهومی تجزیه‌ناپذیر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/151780" target="_blank">📅 17:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151779">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab6397cd2.mp4?token=uTlWtbsyhyfLzVZ01cex3yK_F5BcTSTCVDUcDckm7bnzZSKEWN8AJfVwe3x5Gq_WNDsEdMFK7ENtVUrC0ohFV03FdK4k7ifamV90Zv7_GkFpXL2RSBPHOuQ8cXCm52TRFYOKAfuo5_6WQnb9WpvK1Qbc1Jarl3Ca_lK5Z0kVostQmjutmyQELKTNLDvYHcDZk8l3uZ3ufN830bDwCnmCwsIuQ-6DdMLv08MQVaxvutd0iRwZQWDBwzcusqMBs-jRe4lGXoSJfqSafPXl7lOOxupJsYMJGryQYk32tHWGCKkuZRuKfoRClTJU0o7QbcBWrH-___UJE_xOadBbO311lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab6397cd2.mp4?token=uTlWtbsyhyfLzVZ01cex3yK_F5BcTSTCVDUcDckm7bnzZSKEWN8AJfVwe3x5Gq_WNDsEdMFK7ENtVUrC0ohFV03FdK4k7ifamV90Zv7_GkFpXL2RSBPHOuQ8cXCm52TRFYOKAfuo5_6WQnb9WpvK1Qbc1Jarl3Ca_lK5Z0kVostQmjutmyQELKTNLDvYHcDZk8l3uZ3ufN830bDwCnmCwsIuQ-6DdMLv08MQVaxvutd0iRwZQWDBwzcusqMBs-jRe4lGXoSJfqSafPXl7lOOxupJsYMJGryQYk32tHWGCKkuZRuKfoRClTJU0o7QbcBWrH-___UJE_xOadBbO311lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان در نشست سران کشورهای مشترک‌المنافع: جنگ‌های اخیر منطقه نشان داد که امنیت و ثبات منطقه‌ای مفهومی تجزیه‌ناپذیر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/151779" target="_blank">📅 16:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151778">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
عوستاد رائفی‌پور:  الان دشمن دنبال اینه جای رهبر رو پیدا کنه، حتی از روی پیامای متنیش
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151778" target="_blank">📅 16:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151777">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b3a06504.mp4?token=bcX-x5HRnZQKAfkmelWm_QLgG5l7FE1WZwn1LrZWecZrTcmEfrKB6D4uVK2YvzIJZPIl9E7up5ZZC3wOTlqm5wqPNZYZXa8Y5oGgvySPEbRxTRXVhl_CkNiVM79SMoBGlambPZ3fVHL-HT_S0ssZ1xGQaYRUHd04KuTRkBUYidy0IkXuJLso7sIyPVcLFR04FkO0Orw_wuyvJgmBXRkFW-CNejSEUmrRp0DFdctz2ef-eVUyOwL8UEjSaypT9UYdYlgO_2rDapeO8Pnx_CRkVj31_o7u1fcq2Z6DE8SidoeY_w8Mo6Nj6qlq5al6YdSXDIo3BEtdlSLRlO5WNosNBXRdzlteA5QR50MwKFKAcTGliSYuGcs6wdIdEfscaoWPyUGFBxaaYEnJ6bVaj3hx_cd59GNhTpzUomJ1uLPxNhr1HR0xtLehTKDAKDvv9SjPeTe_jlLJRboP_BOSSdztt5EmQykXJQOglFD_Nmv36w1Nxp50LMywEtl0FYzl3g3rEO5UpoxdxTSLotPB9YhSJTZwH_lG-a8Lskf7DermS_KTSjgO5uJOq7cwF0bO36im2bk-p9I-MdZFl8YQY965y82tEziiALUKDdTnQX3WSisROts65sBO_Qci1nQ9NCWs0wvVIbpkqPYz12H78sZmILCZZNhfCQhJbtX_SaLGUVY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b3a06504.mp4?token=bcX-x5HRnZQKAfkmelWm_QLgG5l7FE1WZwn1LrZWecZrTcmEfrKB6D4uVK2YvzIJZPIl9E7up5ZZC3wOTlqm5wqPNZYZXa8Y5oGgvySPEbRxTRXVhl_CkNiVM79SMoBGlambPZ3fVHL-HT_S0ssZ1xGQaYRUHd04KuTRkBUYidy0IkXuJLso7sIyPVcLFR04FkO0Orw_wuyvJgmBXRkFW-CNejSEUmrRp0DFdctz2ef-eVUyOwL8UEjSaypT9UYdYlgO_2rDapeO8Pnx_CRkVj31_o7u1fcq2Z6DE8SidoeY_w8Mo6Nj6qlq5al6YdSXDIo3BEtdlSLRlO5WNosNBXRdzlteA5QR50MwKFKAcTGliSYuGcs6wdIdEfscaoWPyUGFBxaaYEnJ6bVaj3hx_cd59GNhTpzUomJ1uLPxNhr1HR0xtLehTKDAKDvv9SjPeTe_jlLJRboP_BOSSdztt5EmQykXJQOglFD_Nmv36w1Nxp50LMywEtl0FYzl3g3rEO5UpoxdxTSLotPB9YhSJTZwH_lG-a8Lskf7DermS_KTSjgO5uJOq7cwF0bO36im2bk-p9I-MdZFl8YQY965y82tEziiALUKDdTnQX3WSisROts65sBO_Qci1nQ9NCWs0wvVIbpkqPYz12H78sZmILCZZNhfCQhJbtX_SaLGUVY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان در نشست سران کشورهای مشترک‌المنافع: تحریم علیه ایران، اقتصاد و نظم منطقه‌ای را تهدید می‌کند؛ ایران یک مسیر مناسب برای اتصال آسیای مرکزی به اوراسیا و آب‌های آزاد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/151777" target="_blank">📅 16:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151776">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وقوع انفجارهایی در اربیل عراق
🔴
منابع عربی منطقه از وقوع انفجارهایی در اربیل واقع در شمال عراق خبر می دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151776" target="_blank">📅 16:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151775">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
نیروی دریایی سپاه : ساعاتی پیش کشتی غول پیکر حامل گاز ال پی جی به نام اِن‌وی‌ سان‌شاین متعلق به شرکت نات‌ویت که قصد عبور از مسیر غیرقانونی جنوب تنگه هرمز را داشت مورد اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151775" target="_blank">📅 16:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151774">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
به گفته برخی منابع جمهوری آذربایجان به معلمان محجبه یک هفته فرصت داده که حجاب را کنار بگذارند و یا استعفا دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151774" target="_blank">📅 16:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151773">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJIW70Z9ow39g-dcYRt1XcIOqwxY2zUj5gQ8FQlAQs_6gpqbL8Tqy2b897rVjo3gxz3omiQ8i5wsr7p9QmcCWpQXmc3B8tgOkykJIdnklXEbNJmvyeUsJHeqpE1l8eUv1K_2BcRiWHYPFRLUmcMulfieZl-41Dv8QADm1tljlA43qGMAwDa4Js0NHks5hACND2gpmOImZRkKv3pSk_a1VisLUrOeaLa6lX1VcVAN2qBBc4JytX5YlG2TG3hgktv86JvCN1YN-xtLHKMOoa1uFD7hTO7yncPyH3HG1nziGnND8RR09iduz-xe_wf78u9FZF7cPtHOWoakU4J8I_aPhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهباز شریف، نخست‌وزیر پاکستان، بار دیگر دونالد ترامپ را برای دریافت جایزه صلح نوبل نامزد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151773" target="_blank">📅 16:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151772">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbkxkSpKvqjwDJgnh5CDxokit7f9UlkFSrRfahoW85jCDkzG4rglPju9rtAgHs1QzHcdnoQXUin6gR2caDwdLw6EDU81Z1AIYInpvxw8OLOnGgRKQ9Z2F_ty-o-AW5n18xkxfu2z7tZo4DcU0Fq3Sn1HOxZURO_VuaHG_s2Dur4k91a6ITW1CgYI5ed40USANYCFUa9zLmNdDy7noVCcTMjW9uxthG-yVimNjgWKeEQtnd_5x4hIwrn6C4vp6RkFi-IeLWIYY5lv1PKuq1Wap9tmnr2sI-1pSn2MsELB44ZrWsWlwmnr_zYYIEVPhl1OHZFZJ8G9_iTL6QJJv9cvoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثروت ایلان ماسک امروز به ۱.۱ تریلیون دلار رسید؛ این رقم معادل ۲۹۶,۰۰۰,۰۰۰,۰۰۰,۰۰۰,۰۰۰ تومنه
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151772" target="_blank">📅 16:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151771">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
اکسیوس به نقل از یک مقام آمریکایی:
واشنگتن رئیس ستاد کل ارتش اسرائیل را در جریان آمادگی‌های نظامی آمریکا برای ازسرگیری جنگ با ایران طی سه هفته آینده قرار داده
🔴
زامیر در این تماس گفته که ازسرگیری جنگ می‌تواند انتخابات اسرائیل را به تعویق بیندازد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151771" target="_blank">📅 15:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151770">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5QZ7lqUVzlUG4sXf-y7QkMqLCo9tu7qBaIs3r5dnvsujQGcM-2Ox3tW0r_67hbK-VWy9-dqRKaeIbTyC9Lt8It-9O0Cc--sDIdHLaiCeFquuCm3g2TUBzsFLZe0aF0UW3VzZqEPfRbH6xcCuGPeOWHWSfFtYQEgvPdg_54rnUnnvfqmUK3PTJT6t8P72db3qpc63SK_Ab1gCkbRlZoOxHHFGo3CMZ8QnI88sh7EOk1_eTDSuXQDbMo62Bq_H9BG5UflNbLRwDSq_Y1N3Y6kZwu92LK74g22fxOSH2cPM7Jzdosj38CvWDZGSHt8VhEFPATW5wzAEJDqX2UdsqUgMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
ورود توده تندری به همراه صاعقه‌های شدید
🔴
چیتگر تهران هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151770" target="_blank">📅 15:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151769">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
پزشکیان به دبیرکل سازمان همکاری شانگهای: تاثیرپذیری از آمریکا و عدم استقلال در تصمیم‌گیری، منجر به از دست رفتن قدرت و انسجام شانگهای و بریکس خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151769" target="_blank">📅 15:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151768">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
آژانس ایمنی هوانوردی اتحادیه اروپا:
توصیه می‌کنیم از پرواز در بخش‌هایی از حریم هوایی عربستان سعودی که در منطقه اطلاعات پروازی جده (FIR جده) قرار دارند و مشخص شده‌اند، خودداری شود.
🔴
منطقه دیگری در شمال‌غرب عربستان سعودی نیز به فهرست مناطق پروازی‌ای اضافه شده است که توصیه می‌کنیم از پرواز در آن‌ها اجتناب شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/151768" target="_blank">📅 15:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151767">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ابراهیمی عضو دولت رئیسی: آمریکا نمیذاشت تو ایران بارون بیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151767" target="_blank">📅 15:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151766">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
بر اساس یک گزارش آمریکایی، ارتش آمریکا در حال استقرار و تقویت سامانه‌های پدافند هوایی در سراسر خاورمیانه و افزایش نیروهای خود در منطقه خلیج فارس است.
🔴
همچنین گزارش‌هایی از تقویت قابل‌توجه پدافند هوایی در اردن، عربستان سعودی و امارات متحده عربی منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/151766" target="_blank">📅 15:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151765">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
وزیر انرژی ایتالیا اعلام کرد در نشست وزیران انرژی که قرار است هفته آینده در ریاض برگزار شود، حضور فیزیکی نخواهد داشت و به‌صورت ویدئوکنفرانس شرکت خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151765" target="_blank">📅 15:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151764">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
آمریکا دوباره به سفارت‌های منطقه هشدار داده
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151764" target="_blank">📅 15:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151763">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
مقام آمریکایی به العربیه: ارتش آمریکا روز یکشنبه در آستانه حمله تمام عیار به همراه اسرائیل به ایران بوده است که در لحظه آخر حملات به تعویق افتادند
🔴
نیروهای آمریکایی تا نیمه‌شب به وقت آمریکا، برای اجرای حمله‌ای نظامی و گسترده علیه ایران در حالت آماده‌باش باقی ماندند و انتظار تا ساعات اولیه روز دوشنبه، برای صدور دستورهای نهایی حمله ادامه یافت اما در نهایت ترامپ حملات را به تعویق انداخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/151763" target="_blank">📅 15:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151759">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85b45c931b.mp4?token=O_f63tABzcKSdGXGjjQ00N3C4rCUnMIlPM-Jy59RpXE-RUP4ohQ_w-yGoyApc2CNqeov60IxV6V73jtSINbsyKQil7J1dsphZMDEeHfxRsraudw_4_TGwQmv6mTNMx2tS99V5L6aLeXBvnHLf2XyfMwXNjZyLRKz3zWkM3lNDZhuQluhPefpNLoF7D5686UBEHMy9zapSOvvG6FqEYMzsc6s1Qrm4seBLiaxUbUA7Z4NvUZJhi2wbvZTQnPnJwJeWbnAbquwxa74L-1SNWIWPx7k1v8a3fKNrlw3Wp5IyqcHPRQd2_kVqr59PN1EebD5L_ZBaUmXCOy78RgnBV0E4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85b45c931b.mp4?token=O_f63tABzcKSdGXGjjQ00N3C4rCUnMIlPM-Jy59RpXE-RUP4ohQ_w-yGoyApc2CNqeov60IxV6V73jtSINbsyKQil7J1dsphZMDEeHfxRsraudw_4_TGwQmv6mTNMx2tS99V5L6aLeXBvnHLf2XyfMwXNjZyLRKz3zWkM3lNDZhuQluhPefpNLoF7D5686UBEHMy9zapSOvvG6FqEYMzsc6s1Qrm4seBLiaxUbUA7Z4NvUZJhi2wbvZTQnPnJwJeWbnAbquwxa74L-1SNWIWPx7k1v8a3fKNrlw3Wp5IyqcHPRQd2_kVqr59PN1EebD5L_ZBaUmXCOy78RgnBV0E4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراضات بعد از فرانسه به بروکسل و بلژیک نیز گسترش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/151759" target="_blank">📅 15:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151758">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
دو مرد ایرانی در لندن به اتهام انجام عملیات نظارتی و شناسایی مقدماتی با اهداف خصمانه علیه سفارت اسرائیل، قدیمی‌ترین کنیسه بریتانیا و چند مکان دیگر مرتبط با اسرائیل و جامعه یهودیان، متهم شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151758" target="_blank">📅 14:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151757">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: ما قصد داریم به عنوان بخشی از تلاش‌هایمان برای منزوی کردن اقتصادی ایران، تقریباً ۱ میلیارد دلار دارایی ارز دیجیتال را توقیف کنیم.
🔴
هدف از کارزار انزوای اقتصادی، محدود کردن دسترسی مقامات ایرانی به منابع مالی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/151757" target="_blank">📅 14:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151756">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
میرسلیم، عضو مجمع تشخیص مصلحت نظام: تیبا با خودروهای خارجی قابلیت رقابت دارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151756" target="_blank">📅 14:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151755">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swX-EOnWhXBx51efiI9WqZERHWb-Jl4Rl625S5AUsR7Vry_gfUSUEOak9TA8yulu1vc-NTSipvozVwzMYEQQs03Z_37118aRWwqQhGzBC0ZmWxbAFNnAioBauJqgYheg3GUchj7B2PSIhUjmIjXkgFcDOYi8oXLUwFkv8YG2sjpffHCRwCbuznmHdWBINpcGzw6wUkaz6edwVDqSWGC7jzIzUYy8A-Tp6YKGjHjV18oCFDa7zT62JV1etPhZtBBSahkGYr1gh29H2GBEY4rnxi4wLsMjqp3kpFOsue5q3cW1VXcIBn-gl2gX05-LGerXSAncBIlB-BRiLmAIHi_5VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور پزشکیان در کنار سران حوزه خزر
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/151755" target="_blank">📅 14:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151754">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBPI4vncjWzFRBbnbtiBWBi_A3gRI3AKbP7oxwMgfRdKI7dYrQ_BD3UC3_0WUHUOXen5geax5TfYAz0T9RCU8yohx_O4TzKqvn2UCqU3txhxCgoq6xzibc7SUtctyu30CEgHzV6QXkaYTLNf6zNJZL9QoWXYMmz_dDC3J3xUW39ZYTeN3brrzHT27OIX5U1hEcPLzwLQt5XEdHIfMOPLP1-2_gWEIEum8KQj6Z-E7-FxY2ZJ1YW8U4WjtLWivyj9XlFXrbdS1sRAZls1QKG-vPg30iAbL4PEIOquw_bIkpXedFpJ915VvtxUEEpvaSR9ZOBGEInkmxOpYuHw5XHkpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آلمان:ایران در حال آماده‌سازی برای حمله به تاسیسات آمریکایی در آلمان در صورت تشدید تنش‌ها است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151754" target="_blank">📅 14:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151753">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
پزشکیان: ایران همواره به گفتگو تاکید کرده است اما گفتگو زمانی کاربرد دارد که در سایه زور نباشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151753" target="_blank">📅 14:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151752">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
زلنسکی آمریکا را به انفعال متهم کرد:
نمی‌توان از یک سو با روس‌ها درباره پروژه‌های اقتصادی آینده مذاکره کرد و از سوی دیگر گفت که در نوعی بن‌بست دیپلماتیک قرار داریم
🔴
پس حقیقت کجاست؟ این چه بن‌بستی است؟ این یعنی بی‌میلی
🔴
استارلینک را برای اوکراین فعال کنید؛ به ما کمک کنید از آسمان‌مان دفاع کنیم و در آنجا برتری پیدا کنیم، آن‌وقت پوتین پای میز مذاکره خواهد نشست
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/151752" target="_blank">📅 14:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151751">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
لوفت‌هانزا و پاکستان پروازهای ریاض را لغو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151751" target="_blank">📅 14:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151750">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
سفارت آمریکا در بیروت هشدار امنیتی صادر کرد
🔴
سفارت آمریکا در بیروت با انتشار هشدار امنیتی، از اتباع خود در لبنان خواست با توجه به تحولات امنیتی جاری، احتیاط لازم را رعایت کرده و سطح هوشیاری خود را افزایش دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151750" target="_blank">📅 14:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151749">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nslwBzncUqCbDZtc9JL6d0XXhLjCbQMsaqAYnWFTAULvNZk6z7pTpQLz1zHo3tTqEWytPEatjr7SMR7kpwCIcIw4SMEcm_LeyxfDzlgT1WTWNpYYWbNkGOsWsNHW98w8g4avHF8Nf786gRt9aYTZm8s2byLaEnKDu9xuD43upCsEQRhTL4z0oNy8jzyj6Eh3kyE5cdaQoQza9_aAzRo4hnqOveRBdCw8_QHtFQ5ZzWv1Qe-0c-cZM6tp2y79YamIkxgY85XB9YSHwDoo2TzwbZoDCQokhZdoOSSw5IDTWgEKDgGsQM2kyMeLXpYjqy17e06L_A9gVrdx040c79RL8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منطقه خاورمیانه شاهد رفت و آمد پروازهای متعدد هواپیماهای نظامی ترابری مدل C-17 است. به نظر می‌رسد این فعالیت‌ها مربوط به استقرار سامانه‌های دفاع هوایی باشد، احتمالاً به منظور آماده‌سازی برای از سرگیری جنگ علیه ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/151749" target="_blank">📅 13:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151748">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
خبرگزاری فرانسه: پاکستان تأیید کرد که نیروهای این کشور در عربستان سعودی مستقر هستند و مأموریت آن‌ها دفاعی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151748" target="_blank">📅 13:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151747">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ادعای نیویورک تایمز: شرکت‌های چینی برای عبور از تنگه هرمز به ایران عوارض پرداخت کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151747" target="_blank">📅 13:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151746">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSItvvrkz6i33Nd_abmhTq1sh8Zb0tuNHXAvB0tGycdiRspytQNG_ndqz3aHmXVsm46vqW8_H0a2Eg9smNyNLM90wOTACZFC4d6Lo7zumZUmyu3vPhlhgYPNlHr3iME0BUx-bbYc_oNS21napJrA8Fcx5yVlZov9NAfDqDIbm9jhXZNRA3C0ZG5OdxakcyxUKG-uwVgMIxYlNB3VHdJHoZuSHH3ReYl5_hkC_ABAL4THyf9eggNNW8AnTKs1lRjWmzgWLDRJqi4D7g_mXQripfPWfPgXc2jpZoq4TmGuSWYrBRsaG1lZN9KJVpThL-j21L5HU3BQjM3q4iLow_6Nuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار امنیتی آمریکا در اردن
🔴
سفارت آمریکا در امان، پایتخت اردن، از شهروندان آمریکایی حاضر در خاورمیانه خواست با توجه به «شرایط پیچیده امنیتی منطقه»، هوشیاری بیشتری به خرج دهند و آگاه باشند که احتمال لغو پروازها، بسته‌شدن حریم‌های هوایی و اختلال در سفرها وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/151746" target="_blank">📅 13:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151745">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
یک منبع منطقه‌ای به خبرگزاری فرانسه گفت، عربستان سعودی با آتش‌بس با حوثی‌ها موافقت نخواهد کرد تا زمانی که دولت یمن مورد حمایت عربستان تمام سرزمین‌هایی را که در هفته‌های اخیر از دست داده بود، پس نگیرد. این منبع افزود که ریاض تسلیم «باج‌خواهی نظامی» حوثی‌ها نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151745" target="_blank">📅 13:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151744">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
روسیه: آزمایش‌ها وجود طاعون را در مرگ کارمند آزمایشگاه سیبری تأیید نکردند
🔴
این کارمند ۲۸ ساله به ذات‌الریه اکتسابی از جامعه مبتلا شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151744" target="_blank">📅 13:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151743">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50bf5cc17a.mp4?token=dga7MuA46_xSks1TgbBq49k03HxxMDOYJyc8VsOqQbRitjYUXnP6bvBi3MgFKGLeV4crrljiBNfuQjQwr9UifEGNy_d3qKc4uQpCYdMP0dXWAlHMCjUzxLBs7l266-x4_w1bj6gRm4jipbrKhuBC9YtgylT6EAwxJ2qbx6AYDl2XwTfKLvN3sKGaCfwAkXGbrTSLs-o6paL26zWYW7v7PJwVfcHxfrusVdrHgZHLSbaGMV1IAgZw3K3SePbjSQ5ll6lLgX0Z8lqNKN-AGEZ51H2iDwlOI4cz43uPHZIr-82boIGMUXBQEWArxCQ0lj87ZbKqkMHkHI1WDy-iSAI-rw0NPX40f4D5yAIe-eMU8fmFnlUYLDXf9d25J2e-9pXch2pdwQeNwQuWqShGLdSkUHwlcfUhBbHCLZXaLk4iq3ULK9E3xjdqdKX2WEVw16ulUrJZer_f3eVPjtnvv7YsVcoE7mgzfgK3kQU3BT7DBSwZq79Q_xtJPP_n82haZfgHm4EA-TgjlxwHrapCza4GsxCB3seUgyBN2vM9GmPDXXyU3BUEznLuw9lTuO46IilhmSORE7GCm99SgVjl8WD1Bn319B2hUnwwEJq3t-t3WOyIBHVrRTU2ji4__ntMUM6vMlsTdrO0c6cd4iWUghkFLoTJr2YjJRC1Mem97jvfUiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50bf5cc17a.mp4?token=dga7MuA46_xSks1TgbBq49k03HxxMDOYJyc8VsOqQbRitjYUXnP6bvBi3MgFKGLeV4crrljiBNfuQjQwr9UifEGNy_d3qKc4uQpCYdMP0dXWAlHMCjUzxLBs7l266-x4_w1bj6gRm4jipbrKhuBC9YtgylT6EAwxJ2qbx6AYDl2XwTfKLvN3sKGaCfwAkXGbrTSLs-o6paL26zWYW7v7PJwVfcHxfrusVdrHgZHLSbaGMV1IAgZw3K3SePbjSQ5ll6lLgX0Z8lqNKN-AGEZ51H2iDwlOI4cz43uPHZIr-82boIGMUXBQEWArxCQ0lj87ZbKqkMHkHI1WDy-iSAI-rw0NPX40f4D5yAIe-eMU8fmFnlUYLDXf9d25J2e-9pXch2pdwQeNwQuWqShGLdSkUHwlcfUhBbHCLZXaLk4iq3ULK9E3xjdqdKX2WEVw16ulUrJZer_f3eVPjtnvv7YsVcoE7mgzfgK3kQU3BT7DBSwZq79Q_xtJPP_n82haZfgHm4EA-TgjlxwHrapCza4GsxCB3seUgyBN2vM9GmPDXXyU3BUEznLuw9lTuO46IilhmSORE7GCm99SgVjl8WD1Bn319B2hUnwwEJq3t-t3WOyIBHVrRTU2ji4__ntMUM6vMlsTdrO0c6cd4iWUghkFLoTJr2YjJRC1Mem97jvfUiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
۱۱۰ هکتار از خاکِ ایران به افغانستان واگذار شد!
🔴
محسن زنگنه: قرار شده ۱۱۰ هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.
🔴
البته قرار بود سهم بیشتری بهشون بدیم اما یه سری محدودیت هست و اینکار مشکله، ولی حتما پیگیری…</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/151743" target="_blank">📅 13:16 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

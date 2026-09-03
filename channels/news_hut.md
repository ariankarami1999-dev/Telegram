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
<img src="https://cdn4.telesco.pe/file/FDrOZfdkW0TIIOVoM1CWU-8lsw1SHVqJdH7JkBa3bXQVdOenECHwo1RQatnY4FH8MWaICa5baQJ7slLjaDW_QdvH65bugnpCHDZrhUzFuOny9B3o6SxDm6_8Z0H0UQV5v5IOXhCDVQltCEL1zSY2uq6aO6qOn3IiQABJUM9N1CGLDj61aodAHVaIsVn4Q_ILI4laWIncJ_BSh0k3QtA4ELIQ0LGph3BOfGA5kDp1l9rSEmHBq-jfF9_k-Anc6CTnpfd4knlhgV2rN3LnWtqKlx1aLg6ODV4LdkueKKK0FgSow6PHHx892uuJ98ashmrxw35CDoqQpYISSJmVGTtLaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 112K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 12:48:51</div>
<hr>

<div class="tg-post" id="msg-71040">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2218c2694e.mp4?token=qwYvlyxKpW0_YhnZ4uCD2tah6jD8N4VAJR7BXo0GseBUBj2KLHw1shhoRCSE3pu_l_7MfyqYqtyKxgunlMwe1rtTZgQsoTc2y6q_-s5aoyvkYvV2qXUw-iuXMveuf94XOuko5Vn3WWyvGw9eUFxmTePqNp2mE0JcLRl21Jz9WcHR56WAnzDWxx2XyDPFtojbO8LvB5EIlZd1SFvielxxN7hN4SVPxLKBuOEll5q7LGRHuXPmO1S9sdH6_W2KQpEgsZN6mCJEq0islM_t8X_rtgGTUEwv6wSxgdoWwCR9DsCPnDKVJtSIlIsnm4xixmpdUEEaTFn7osfAq_JZILCOTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2218c2694e.mp4?token=qwYvlyxKpW0_YhnZ4uCD2tah6jD8N4VAJR7BXo0GseBUBj2KLHw1shhoRCSE3pu_l_7MfyqYqtyKxgunlMwe1rtTZgQsoTc2y6q_-s5aoyvkYvV2qXUw-iuXMveuf94XOuko5Vn3WWyvGw9eUFxmTePqNp2mE0JcLRl21Jz9WcHR56WAnzDWxx2XyDPFtojbO8LvB5EIlZd1SFvielxxN7hN4SVPxLKBuOEll5q7LGRHuXPmO1S9sdH6_W2KQpEgsZN6mCJEq0islM_t8X_rtgGTUEwv6wSxgdoWwCR9DsCPnDKVJtSIlIsnm4xixmpdUEEaTFn7osfAq_JZILCOTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تو میدون تایمز نیویورکِ آمریکا، یه خانمِ چاقو بدست بعد از اینکه یه مرد و یه زن رو از ناحیه شکم زخمی کرد، بعد از اخطارِ پلیس‌ها به سمتشون حمله‌ور شد و به این شکل بهش شلیک کردن و کشتنش.
@News_Hut</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/news_hut/71040" target="_blank">📅 12:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71039">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f52d28bc.mp4?token=QZHtbqdC0nqbbHCKWZ7sFyT9M7YQY_LVbqgQMvND5tVWLnamHyB24tA2GoInrI4c73amLmHw2BBWOt4kEFh_fsUWOG5_zbLNqcrFTMalJ4ETqMPC_tqQ5jDf1GEs6E0zTWHNVJzJGXfxWrEO0Vp7z8d2kdf1X1xrpqEsnC_9f87uM_ZBHqUXDPAt_s1uv35gaRykCACox95H8ohkxnjRv14Ks88Vvi9rnhCmukLbzgW6ajgdJ2-5c_WM1cmoZ3BwR7Q1PAH2z7uRUDtB0nHyXNK14A4lc5vn5YzoQsq1eM3YFCKnSHZzkZ3mRGwjXNpnb0WORXGcFK0IIFwix_lHYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f52d28bc.mp4?token=QZHtbqdC0nqbbHCKWZ7sFyT9M7YQY_LVbqgQMvND5tVWLnamHyB24tA2GoInrI4c73amLmHw2BBWOt4kEFh_fsUWOG5_zbLNqcrFTMalJ4ETqMPC_tqQ5jDf1GEs6E0zTWHNVJzJGXfxWrEO0Vp7z8d2kdf1X1xrpqEsnC_9f87uM_ZBHqUXDPAt_s1uv35gaRykCACox95H8ohkxnjRv14Ks88Vvi9rnhCmukLbzgW6ajgdJ2-5c_WM1cmoZ3BwR7Q1PAH2z7uRUDtB0nHyXNK14A4lc5vn5YzoQsq1eM3YFCKnSHZzkZ3mRGwjXNpnb0WORXGcFK0IIFwix_lHYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سایپا تو ماشینی جدیدی که زده ماشین با اینکه راه نمیره ولی براش کیلومتر حساب میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/news_hut/71039" target="_blank">📅 12:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71038">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xg9gVFulhQXHc8O23W7c2kVCxFuEzOLeV_hgwa19nI20EY5jgQUSREsCYzoNd_Xo-x8veiZYgiw7Xvtc3VfYHj9qLdliWeaZvRoZjuWnz9loWuRoB5_1V9-Ksj4gUybkOMzWECDvz6DJPl89M5gi5z4R4VhIIUT3_O8jZxseVOstVEiLbnIuGhmf0dSoYzUSzucoas5a4vHDjC4P5B9smcydlRteOEIRHYH7EF_O7-Z9mTRrIR5avNlVsNeSiQrquuLwDMEL6SpBrTD6Lv3zLf6wFnFY-S0UH6ZKnYZZ2XiWXWBQzM5fThNbI-BTJ39awEBK0ekvTsQSQhOnEcnPkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
اکسیوس:استیو ویتکاف، فرستاده کاخ سفید، آخر هفته گذشته در ساردینیا با شیخ طحنون بن زاید آل نهیان، مشاور امنیت ملی امارات متحده عربی، درباره ایران دیدار و گفتگو کرد.
این دو مقام درباره گام‌های احتمالی آتی بحث و تبادل نظر کردند؛ چرا که دولت ترامپ در پی بازگشایی تنگه هرمز و هم‌زمان افزایش فشار اقتصادی بر تهران است.
امارات نقش کلیدی در تلاش‌های تحت رهبری آمریکا برای عبور نفت‌کش‌ها از این تنگه ایفا کرده و در راهبرد تحریمی واشنگتن، کشوری مهم محسوب می‌شود.
مقامات اماراتی به دولت آمریکا اعلام کرده‌اند که هرگونه کارزار مؤثر فشار اقتصادی باید شامل تمامی کشورهای عمده‌ای باشد که همچنان به تجارت با ایران ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/news_hut/71038" target="_blank">📅 11:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71037">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به بندر سوچی در روسیه حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/news_hut/71037" target="_blank">📅 10:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71036">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef77017317.mp4?token=OtEDf0zd02zH-GvByiRMtHNJiBDiE_OFJH41zb2X3G2LDg8rzPSkXqA0OK4dxQXDxwUCCE7qYJTn5YtoNP-z9QEoP1cdwViLWBnuYIX1iXc-66Hhd4BejGWeEuZh7sOLpztlrR5vDVbKi2fXRgDRUBsL5Pq-AJoNwgBCyCz_-a73SrG51XqkouQt2PN2VKZSp7TOaV3G9UbMQ2Kp56v1a2Mut87yo5CkjF2XhLgRHIcAvuUiokwizRGTlvx7Gc4fczf_XPQlIBc2DG0tI3GJGgXDUS8XO1dpDu7sFXF0JmuCp1A5oSaE1NqGO3ILNzov5srzqJ8_g9JMNWcRmm_QQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef77017317.mp4?token=OtEDf0zd02zH-GvByiRMtHNJiBDiE_OFJH41zb2X3G2LDg8rzPSkXqA0OK4dxQXDxwUCCE7qYJTn5YtoNP-z9QEoP1cdwViLWBnuYIX1iXc-66Hhd4BejGWeEuZh7sOLpztlrR5vDVbKi2fXRgDRUBsL5Pq-AJoNwgBCyCz_-a73SrG51XqkouQt2PN2VKZSp7TOaV3G9UbMQ2Kp56v1a2Mut87yo5CkjF2XhLgRHIcAvuUiokwizRGTlvx7Gc4fczf_XPQlIBc2DG0tI3GJGgXDUS8XO1dpDu7sFXF0JmuCp1A5oSaE1NqGO3ILNzov5srzqJ8_g9JMNWcRmm_QQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی وایرال شده از پسری که چالش گرفت که تو خیابونای شهر از مردم درخواست پول کنه(نفری ۱۰۰تومن) و اکثرا قبول کردن و در آخر هم پولی که جمع شد رو رفت به نیازمندا کمک کرد
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/71036" target="_blank">📅 10:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71035">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7de7f7edfa.mp4?token=iqcGl5xXLWRHqdCJpQsCAYApAOLUk5CzYEaqwFz7BOW7PKX5ucUsM4X-1cGU5SDdxh3C81B0nQTTlTc70Ye3LA6PfWALrS9K5gLeMFLtnZMCJ5uSsiN2AIFyWkYgFzph4ajkSMrGHsoV0fu8V_ubi7LR1Tar5Um95yCNvnPyqFbR5PxBgNorFohNnLi-o9WSIekn048y3acGq3AW1W409kZnpvpR5untkJofgl_VA6Y0xB3wL5LydyjrN8uHADDUcfB0UfnZsM22mybXtK29yWwsxH_NVoSRdf5OY4V3sfESKR9mCwnZ17gXfpekYVB5F3caK8fMImkZp5-69t2vYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7de7f7edfa.mp4?token=iqcGl5xXLWRHqdCJpQsCAYApAOLUk5CzYEaqwFz7BOW7PKX5ucUsM4X-1cGU5SDdxh3C81B0nQTTlTc70Ye3LA6PfWALrS9K5gLeMFLtnZMCJ5uSsiN2AIFyWkYgFzph4ajkSMrGHsoV0fu8V_ubi7LR1Tar5Um95yCNvnPyqFbR5PxBgNorFohNnLi-o9WSIekn048y3acGq3AW1W409kZnpvpR5untkJofgl_VA6Y0xB3wL5LydyjrN8uHADDUcfB0UfnZsM22mybXtK29yWwsxH_NVoSRdf5OY4V3sfESKR9mCwnZ17gXfpekYVB5F3caK8fMImkZp5-69t2vYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ویدئو جدید از پرواز هواپیمای HC-130 Combat King II آمریکا در ارتفاع پایین در عمق کشور به دنبال خلبان آمریکایی جنگنده F-15E
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/71035" target="_blank">📅 10:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71034">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad58d044a.mp4?token=FnlQp6GJOAblOxPCudmp9XDV73oUabhS9HBISQ9JWcxVG6MNRRpwtY4VJ6X6Dqnn-ZhUnBH3KFMqVBnrHST6a4iKCDcJf4m2LjAbOgIkk_cDdUH71KKC5qIIdVq6LEBnPjYmYwRGOawGfm_oqEjYCQ6AX1-cuJ7nbixSzmXS5pnB11vefvD41i80TM27unvw3TFRGljGGjc_f24P1cG39-7AZP1oXNObh1KsJeNwl8YaYxOS2e5znmbwmIhy_TvNUYiKl_govlB84uVcf6U7A2qhMT6C23TkyEeBZabeKhaQ4rUya8iZNx9F-ueyqldC5NGh37u0t5UWFgWNjknekg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad58d044a.mp4?token=FnlQp6GJOAblOxPCudmp9XDV73oUabhS9HBISQ9JWcxVG6MNRRpwtY4VJ6X6Dqnn-ZhUnBH3KFMqVBnrHST6a4iKCDcJf4m2LjAbOgIkk_cDdUH71KKC5qIIdVq6LEBnPjYmYwRGOawGfm_oqEjYCQ6AX1-cuJ7nbixSzmXS5pnB11vefvD41i80TM27unvw3TFRGljGGjc_f24P1cG39-7AZP1oXNObh1KsJeNwl8YaYxOS2e5znmbwmIhy_TvNUYiKl_govlB84uVcf6U7A2qhMT6C23TkyEeBZabeKhaQ4rUya8iZNx9F-ueyqldC5NGh37u0t5UWFgWNjknekg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
تو یه فروشگاه تکنولوژی تو روسیه، یه ربات بعد از اینکه مشتری هلش داد، شروع به دعوا با مشتری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/71034" target="_blank">📅 09:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71033">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e73b2179fb.mp4?token=HQn_PHaA8UEfcMIeBQ8vcDNKlIVAHSsH92LjAhW5G73podqudP-4Gb5XE3cVq4eP-OIvI-0KDMige4vI_cAJf2oe9b1CMDWmdXoPCpVmFseDfzxU1rtuTsokVXbZVoV_Von2If1LPWkdgARUD2QA1nADlS9cn9a1CUAHPsoavg9YJgMF2c9Pmak2-GJclaaETNaXY1DAKDcAaTS_Em_OQPuPiYED94qQQxztNAOf8-bkn2pYOPYJ2lHVhXVbyPZOXRrQOPEILOEYz6bNm8-dM67M2Zqe6sXz0KUqdE7TTZ_LWwovhTW9CJVBbP9qXMYBEdQGI9tFdhN8mNGTlNYFVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e73b2179fb.mp4?token=HQn_PHaA8UEfcMIeBQ8vcDNKlIVAHSsH92LjAhW5G73podqudP-4Gb5XE3cVq4eP-OIvI-0KDMige4vI_cAJf2oe9b1CMDWmdXoPCpVmFseDfzxU1rtuTsokVXbZVoV_Von2If1LPWkdgARUD2QA1nADlS9cn9a1CUAHPsoavg9YJgMF2c9Pmak2-GJclaaETNaXY1DAKDcAaTS_Em_OQPuPiYED94qQQxztNAOf8-bkn2pYOPYJ2lHVhXVbyPZOXRrQOPEILOEYz6bNm8-dM67M2Zqe6sXz0KUqdE7TTZ_LWwovhTW9CJVBbP9qXMYBEdQGI9tFdhN8mNGTlNYFVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیح عباس حیدرزاده مداح درباره‌ی وضعیت مجتبی خامنه‌ای :
تولیت آستان قدس رضوی گفت که شب دفن رهبر؛ مجتبی خامنه ای ساعت ۱۲ شب اومد حرم برای دفن پدرش و تا ۷ صبح اونجا بوده.
وضعیت جسمانی ایشون هم عالیه، هم از لحاظ ظاهری و هم از لحاظ جسمی؛ حتی مسئولین هم پشت سر ایشون نماز خوندن.
همچنین ایشون نیم ساعت کنار قبر پدرش دو زانو نشسته بودن و گریه میکردن.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/71033" target="_blank">📅 09:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71032">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71032" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71032" target="_blank">📅 01:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71031">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrYFBIyj6MshT__ZXmWZqWqBO6cxH0TRWxx98l3OaoGUko7XTnwxn4oAt-WGy8Omd7No_HashpolWyOoYOfmY8lUugxQ9PsryBso2D1C9jr5tZuY061wgefkszURYPRWc0s3Wbo3q_ph8dZqwUI9ayEkCpmOMAcleEKvxmCzFkK6b0OOlEQ9z4hCgHqnCHDD_6IBvflSFYkBQVLcTMqZqJ4t1SlvYMGmkVIYncm2hxFybOsI9UyqmYLmUtLFFfT25r7dSBAQGZGTlm3QPy6TXeOvAE5belluu-afMY9RcyqznzbhZ1xMEM6_F47Qwjq3bs67_YV0jmxqk1j2q9VP7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
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
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71031" target="_blank">📅 01:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71030">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
⭕️
فوووووری/ همین الان با شروع مجدد جنگ دلار و ارز منفجر شد
😳
‼️
همین حالا چک کنید
👇
https://t.me/+S5Mn2k3LOf0wNjJk
https://t.me/+S5Mn2k3LOf0wNjJk
فوری برید ببینید
☝️
☝️
☝️</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71030" target="_blank">📅 00:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71029">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa78544f7d.mp4?token=ElQ2QFI_aC37xpEMpxFKCNFD3N7EX4acSDDdqvNlDslvvqPNuygWLeYRlAIhBBQsVj3dbWhakQFvyoJTBLQTJhZtVoFHta5gJXht0alOskw6Z1qRSMWRKzDxbmP22QwxhSSDYPPW3lw35XGHO8cHczgmwJVUa0gP4JWoLsaFofwgegvUo7SRw9dJfHrkddfXiB56HZBOHfJ5BmH1fRXW20pjQf98tR5rl4yDpeBtsUD2fp3Bd1YJzOKsjKZOSd8KjlwGDyZQgp-T0EGNLWcK7D0G0pcaFf41JM119LC1g4cMdsgWSeHLzRB0056fGkwz2fRZMidyNN7s54gKm6FCiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa78544f7d.mp4?token=ElQ2QFI_aC37xpEMpxFKCNFD3N7EX4acSDDdqvNlDslvvqPNuygWLeYRlAIhBBQsVj3dbWhakQFvyoJTBLQTJhZtVoFHta5gJXht0alOskw6Z1qRSMWRKzDxbmP22QwxhSSDYPPW3lw35XGHO8cHczgmwJVUa0gP4JWoLsaFofwgegvUo7SRw9dJfHrkddfXiB56HZBOHfJ5BmH1fRXW20pjQf98tR5rl4yDpeBtsUD2fp3Bd1YJzOKsjKZOSd8KjlwGDyZQgp-T0EGNLWcK7D0G0pcaFf41JM119LC1g4cMdsgWSeHLzRB0056fGkwz2fRZMidyNN7s54gKm6FCiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇹🇭
ناو آبراهام لینکلن تو پاتایا - تایلند پهلو گرفت و ملوانان و اعضای این ناو برای یه استراحت  کوتاه مدت پیاده شدن
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71029" target="_blank">📅 23:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71028">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14a1d4faa9.mp4?token=OZDzubA_-lp1_fo73IFIMqYOrO5QfYa6A7s8pKyJH_keOtk00HMHV_XMNfpoBLE5ZhOR2edkJbOzqL22Mt7ZvOIxLX5qVBrCkc-YH7z-Q7W8DJTRU3HnboHKymFeIX9zugdEsgF2Zjj4DtfnOWokoNuYtBhsmovy5lehTP5L0PVBkbYgUhrWjeakT3XdFHSppPQq1Jx37fM1EeYA5WhXxPZZ3zYI2gi3jDU7PonzaiHD755qm7H8f6JJA80PM6a3vVjLYP0B3OwNaxfKmCmM69t0w2crL2WcWNhQ84Lpm09EH5rxRDRueb1xrDCsAy-Ou6-GraiBweF46IuudqXLXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14a1d4faa9.mp4?token=OZDzubA_-lp1_fo73IFIMqYOrO5QfYa6A7s8pKyJH_keOtk00HMHV_XMNfpoBLE5ZhOR2edkJbOzqL22Mt7ZvOIxLX5qVBrCkc-YH7z-Q7W8DJTRU3HnboHKymFeIX9zugdEsgF2Zjj4DtfnOWokoNuYtBhsmovy5lehTP5L0PVBkbYgUhrWjeakT3XdFHSppPQq1Jx37fM1EeYA5WhXxPZZ3zYI2gi3jDU7PonzaiHD755qm7H8f6JJA80PM6a3vVjLYP0B3OwNaxfKmCmM69t0w2crL2WcWNhQ84Lpm09EH5rxRDRueb1xrDCsAy-Ou6-GraiBweF46IuudqXLXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان خطاب به پوتین :
قدرت‌های بزرگ صرفاً چون زور و قدرت دارن، حق ندارن بدون توجه به چارچوب‌ها و قوانین بین‌المللی به بقیه کشورها حمله کنن.
حمله‌ای که آمریکا علیه ایران انجام داد، نه مبنای قانونی داشت، نه مبنای علمی و نه حتی توجیه منطقی.
ملت ما با قدرت جلوشون ایستاد و اگه بخوان این مسیر رو ادامه بدن، بازم با قدرت مقابلشون می‌ایسته.
ما تو اون تفاهم‌نامه چیزی بیشتر از حقوق کشورمون نخواستیم و الان هم فقط دنبال همون حقوق هستیم.
ما همچنان به تفاهم‌نامه‌ای که امضا کردیم پایبندیم. اگه آمریکا هم به همون تفاهم‌نامه برگرده، ما هم طبق همون عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71028" target="_blank">📅 23:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71027">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/180c2bccea.mp4?token=g3J2-rCidCt4HiqufqLpzkGX9vjtVOIAZQ28VLqKSp3XFx8lXzrkCUfIfCOy_zNBSGpcMAtfyRupLs5e4guOFxRkL5SIQjSLX1eCbITQRwdpYSenspEKQEsgdMPMQtVVrp5pGBTCp9-GxgHywlizc5RiP6VfaBar_dY6xUvMnJyGFlAVSisamA1GbYrGEZz_8nXzaAFcOreOnxWg9a0t8Ud6ucVN8jM1XUdqGIMcXL7_24uSb-Vk4QPdDkAW0iMvp513AUCGCrCjurFNtBAR0TL09qTiyHaI5BDl6e_kGf_nqwbeupu12Nf9Y11EjdMQJnXlUASS4t0p9LOilKN_5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/180c2bccea.mp4?token=g3J2-rCidCt4HiqufqLpzkGX9vjtVOIAZQ28VLqKSp3XFx8lXzrkCUfIfCOy_zNBSGpcMAtfyRupLs5e4guOFxRkL5SIQjSLX1eCbITQRwdpYSenspEKQEsgdMPMQtVVrp5pGBTCp9-GxgHywlizc5RiP6VfaBar_dY6xUvMnJyGFlAVSisamA1GbYrGEZz_8nXzaAFcOreOnxWg9a0t8Ud6ucVN8jM1XUdqGIMcXL7_24uSb-Vk4QPdDkAW0iMvp513AUCGCrCjurFNtBAR0TL09qTiyHaI5BDl6e_kGf_nqwbeupu12Nf9Y11EjdMQJnXlUASS4t0p9LOilKN_5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره انتخابات:
من تحت تأثیر انتخابات نیستم. خودم نامزد انتخابات نیستم؛ حزب من در انتخابات حضور دارد.
به گمانم حزبم به این واقعیت احترام می‌گذارد که ما اجازه نمی‌دهیم ایران به سلاح هسته‌ای دست یابد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71027" target="_blank">📅 22:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71026">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53f1ce3ca7.mp4?token=A6gNDme_6isf9E2nK5GFVJfLtwlDMH2a-6U4z0htyJRlFtw5ekaIJzIEQZ24pwcn9h7o2mibewe39lFwONdXo-CKkrwYKx9m9njAZax1fD_E49I-ppT5tuJEPg3LHnkz3XoWAlAytXGncRG3T2Bv5oaZmkGCpnqQ6WXGoapO8sF-OXdnH-ZiEkB4p18EjMX-RXsRqcwiK6adcOYAUt58DDbDTbzfpDsWPLYTgToc38UKjMqohsgWkP33pU0ZCtdz5DhXhmDj03P7NiELizJQYbkh6lAWr9m9pM3sH03xM6BQGQwQjsSyougXVqALtb8QoEFUXR1uNRkkut5yFaQ1EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53f1ce3ca7.mp4?token=A6gNDme_6isf9E2nK5GFVJfLtwlDMH2a-6U4z0htyJRlFtw5ekaIJzIEQZ24pwcn9h7o2mibewe39lFwONdXo-CKkrwYKx9m9njAZax1fD_E49I-ppT5tuJEPg3LHnkz3XoWAlAytXGncRG3T2Bv5oaZmkGCpnqQ6WXGoapO8sF-OXdnH-ZiEkB4p18EjMX-RXsRqcwiK6adcOYAUt58DDbDTbzfpDsWPLYTgToc38UKjMqohsgWkP33pU0ZCtdz5DhXhmDj03P7NiELizJQYbkh6lAWr9m9pM3sH03xM6BQGQwQjsSyougXVqALtb8QoEFUXR1uNRkkut5yFaQ1EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
دیشب حمله بسیار سنگینی صورت گرفت و ما آماده‌ایم هر زمان که بخواهیم، حمله دیگری انجام دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71026" target="_blank">📅 22:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71025">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a230c24bdf.mp4?token=CmPaub4Co3UBaKvkHnZLFS9tZRBM0dTm4knpOpWj_bJm6ERFzbAQD9s_GJawgYPC04B2tvXoDpAl_V-awzGeuCUH_GVzOOC6ihWclRwoD-3oYlRh-MJifZbu7PvoaJ0AM_nhK1aAM5RO2HX4VGH5VNkDMF-mrss37pPNSMzjI-IA3viDs9PULPhwbfooo_lG0nkCNy1RdU8Ghtbg5boET5AQSi5MmbaMomiaJ084YdBKzq_scUge4MTlOLw_7SA506UMgVmDT9f3zaHJoPWgevVpTmTpCOZDCHhNUw5RA5WnjfI9kF-djYK1vfwegXWsGrO-iImYSJu3O5jYLHVOsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a230c24bdf.mp4?token=CmPaub4Co3UBaKvkHnZLFS9tZRBM0dTm4knpOpWj_bJm6ERFzbAQD9s_GJawgYPC04B2tvXoDpAl_V-awzGeuCUH_GVzOOC6ihWclRwoD-3oYlRh-MJifZbu7PvoaJ0AM_nhK1aAM5RO2HX4VGH5VNkDMF-mrss37pPNSMzjI-IA3viDs9PULPhwbfooo_lG0nkCNy1RdU8Ghtbg5boET5AQSi5MmbaMomiaJ084YdBKzq_scUge4MTlOLw_7SA506UMgVmDT9f3zaHJoPWgevVpTmTpCOZDCHhNUw5RA5WnjfI9kF-djYK1vfwegXWsGrO-iImYSJu3O5jYLHVOsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
یک ضربه کوچک بود، اما دیشب ضربه بسیار سختی به آن‌ها زدیم.
ما تمام تجهیزات جدیدی را که سعی داشتند در امتداد تنگه هرمز مستقر کنند، از بین بردیم؛ تجهیزاتی که برخی جنبه تدافعی و برخی جنبه تهاجمی داشتند.
آن‌ها تلاش می‌کردند موقعیت کشتی‌ها را رصد کنند — چون همان‌طور که می‌دانید، قادر به دیدن کشتی‌ها نیستند؛
ما تعداد زیادی از کشتی‌هایشان را نابود کرده‌ایم
آن‌ها نمی‌توانند کشتی‌ها را ببینند چون راداری در اختیار ندارند؛ چرا که ما رادارهایشان را منهدم کرده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71025" target="_blank">📅 22:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71024">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991fb05c67.mp4?token=Na9JbyvBTzqQ9MQnp2cfA8QcrJfr_Tpv3ygdMDjvlxYSu2SJT7J9EonFrTzd94swtHxrC-8OMUHLXICHWO3VYTW-8CxlYb7nbWs9irnlVcaNhDsYlN4V3UMIle7WgDco-XligAFBGsjb_5J2KieB1SiUgyJYZrTI2jI9_kyPu_tZ_Ond36BxAVxjtpdvHkC8jKnslRL5A_Z66kPoPXD9ctkafvitGZtj-KNJuovbaLUSi8UOscLJko-pbYFWNZjzxCl5pkQCTaZRnsOimav2449UCgUuDXP9Lil-rSIOpLnUSscw1Rh0vBMk3pJfJamsuQCFjaszbw4BPae4kZJV4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991fb05c67.mp4?token=Na9JbyvBTzqQ9MQnp2cfA8QcrJfr_Tpv3ygdMDjvlxYSu2SJT7J9EonFrTzd94swtHxrC-8OMUHLXICHWO3VYTW-8CxlYb7nbWs9irnlVcaNhDsYlN4V3UMIle7WgDco-XligAFBGsjb_5J2KieB1SiUgyJYZrTI2jI9_kyPu_tZ_Ond36BxAVxjtpdvHkC8jKnslRL5A_Z66kPoPXD9ctkafvitGZtj-KNJuovbaLUSi8UOscLJko-pbYFWNZjzxCl5pkQCTaZRnsOimav2449UCgUuDXP9Lil-rSIOpLnUSscw1Rh0vBMk3pJfJamsuQCFjaszbw4BPae4kZJV4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
ما هر کاری که آن‌ها انجام می‌دهند را می‌بینیم.
آن‌ها حتی نمی‌توانند به دستشویی بروند بدون اینکه ما متوجه شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71024" target="_blank">📅 21:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71023">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/504db2064f.mp4?token=aTrzgxxhxRsmZe52SoVQv8b9oZ5LlLKWplhey6dgjflMxFUcpW455XCXwUX0ELH9cb2dYpRzSZpzqMd6mPUhSkzUG-dhXw8l0JQR0NSNHjC7MOIgck-rUdYI0cra8tlXIgC1-C_1RRgVOA3Z_L0b9alTgZzMYnixu_RBNEuByXIA32VrZYuoVYZBQEtE1TlQx7aHUcDiEV0zpr4G0jBE_LrsPkmn-kcGxblHHBCRekuGjBcdUDBc3CWWL8QNhkxqJ1Zo2FqVuXUiqbgq9sJ_DzViQNpj4Uy3q76j043aosvJMmMfiAmMvPiUkB_-BlVLAv4EPsYt2nRd7mrYjrKKwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/504db2064f.mp4?token=aTrzgxxhxRsmZe52SoVQv8b9oZ5LlLKWplhey6dgjflMxFUcpW455XCXwUX0ELH9cb2dYpRzSZpzqMd6mPUhSkzUG-dhXw8l0JQR0NSNHjC7MOIgck-rUdYI0cra8tlXIgC1-C_1RRgVOA3Z_L0b9alTgZzMYnixu_RBNEuByXIA32VrZYuoVYZBQEtE1TlQx7aHUcDiEV0zpr4G0jBE_LrsPkmn-kcGxblHHBCRekuGjBcdUDBc3CWWL8QNhkxqJ1Zo2FqVuXUiqbgq9sJ_DzViQNpj4Uy3q76j043aosvJMmMfiAmMvPiUkB_-BlVLAv4EPsYt2nRd7mrYjrKKwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
بیشتر مردم نمی‌توانند به این شکل آدم‌های خودشان را بکشند.
بیشتر مردم سعی می‌کنند منطقی رفتار کنند، گفتگو می‌کنند و بعد شاید کار به سرنگونی بکشد.
اما در ایران، آن‌ها مردم را می‌کشند.
وقتی مردم برای اعتراض بیرون می‌آیند، آن‌ها را می‌کشند؛ درست وسط پیشانی‌شان شلیک می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71023" target="_blank">📅 21:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71022">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c319507bcf.mp4?token=S4OyeIMPksSHhJW3_z_K73DH441LgYjuSm0IHPMO1t68ClIrfJ2E-Lc9SGbe79-FtpRIzYgNz-yAYVsTb9s7EvyK2lm2-6nAE8Kbd3kMiBRACh2ZYOhoAzb1ALddfMDsjIznMy8gwUp-AZcAGlRxWcJEgc3lDLy5accywmLz7H1LNK5NbkrHDjrjpAPL175Y8KmsyG3zEOkbU2dFZInXpU_BXbdrv2LZgeJ4mRAOaHWC1YRMbcldXZYZT58wwm7t2YRclB9vxvdhFL9JW1U1GCxXjrf_XLew0gpz73onAPQVr6qE79AujmmomQuQg0Auxd104M6ToB2y_Po5VC1Tmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c319507bcf.mp4?token=S4OyeIMPksSHhJW3_z_K73DH441LgYjuSm0IHPMO1t68ClIrfJ2E-Lc9SGbe79-FtpRIzYgNz-yAYVsTb9s7EvyK2lm2-6nAE8Kbd3kMiBRACh2ZYOhoAzb1ALddfMDsjIznMy8gwUp-AZcAGlRxWcJEgc3lDLy5accywmLz7H1LNK5NbkrHDjrjpAPL175Y8KmsyG3zEOkbU2dFZInXpU_BXbdrv2LZgeJ4mRAOaHWC1YRMbcldXZYZT58wwm7t2YRclB9vxvdhFL9JW1U1GCxXjrf_XLew0gpz73onAPQVr6qE79AujmmomQuQg0Auxd104M6ToB2y_Po5VC1Tmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
تا سه ماه پیش، پنجاه‌ودو هزار نفر از معترضان کشته شده بودند؛ می‌توانید چنین چیزی را تصور کنید؟
و حالا شنیده‌ام که احتمالاً بیست تا بیست‌وپنج هزار نفر دیگر هم به این آمار اضافه شده است؛
یعنی شمار معترضان کشته‌شده به حدود شصت‌وپنج هزار نفر رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71022" target="_blank">📅 21:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71021">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78e478b4b0.mp4?token=MYQkGIlYlr9lGEmCr12XCGaAHWpgDD1OGJidVakgJJ42rfkPlUwBNY8BAHB4Bj8hBk5O2e2isj3i6iInhwbTTCWsveoTQXvVrDjjjGQtaS_ZMJQntF-i-Zn453m_qatx3ZrfP2sakXvfuHN_gQSj7OPy2HuhXDzXOOKBFDR6hRMbuS-x0bLEfhW6sbyFCPJx09m6WCWM9T9vEcjzkXAWO4n9s2d30bCVKr-kU3IiEYEnD9qvw5iWyM7fsZTbJA8qU-ICdvAFFTM1abiwql3IKB8GAwk5n47nh94EbLZGS4w7ejBZ4LE0tEhhdyPhbY-6yA_46Mc_VYN1qeRVHfOxOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78e478b4b0.mp4?token=MYQkGIlYlr9lGEmCr12XCGaAHWpgDD1OGJidVakgJJ42rfkPlUwBNY8BAHB4Bj8hBk5O2e2isj3i6iInhwbTTCWsveoTQXvVrDjjjGQtaS_ZMJQntF-i-Zn453m_qatx3ZrfP2sakXvfuHN_gQSj7OPy2HuhXDzXOOKBFDR6hRMbuS-x0bLEfhW6sbyFCPJx09m6WCWM9T9vEcjzkXAWO4n9s2d30bCVKr-kU3IiEYEnD9qvw5iWyM7fsZTbJA8qU-ICdvAFFTM1abiwql3IKB8GAwk5n47nh94EbLZGS4w7ejBZ4LE0tEhhdyPhbY-6yA_46Mc_VYN1qeRVHfOxOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما امروز در «تروث سوشال» (Truth Social) نوشتید: «مردم ایران چه زمانی قرار است قیام کنند و بجنگند؟» خب... اگر... اگر این چیزی است که شما می‌خواهید، آیا سیا (CIA) را برای مسلح کردن ایرانی‌ها اعزام خواهید کرد؟
⏺
🇺🇸
ترامپ:
خب، پیتر، من نمی‌خواهم چنین چیزی به شما بگویم. خیلی دوست دارم این را به شما بگویم، اما... اما گفتنش مناسب نیست.
ولی... منظورم این است که من وضعیت دشوار آن‌ها را درک می‌کنم؛ آن‌ها هدف شلیک گلوله قرار می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71021" target="_blank">📅 21:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71020">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):   گزارش تأییدشده‌ای مبنی بر درگیری یک نفتکش در یک حادثه امنیتی دریافت کرده که منجر به دو مورد تلفات انسانی شده است.   @News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71020" target="_blank">📅 21:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71019">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8edb01b99f.mp4?token=KL6uV-k4foLmRz91ykRL0ZFCPT1-hDZt2eQl9cg4FWoLkwYGh3MplH5sFOup_xkHXdlBHs7mgHyf__6lIXpuXmy9wRB42GKCTf9ZGFg5_KbfrSR-8npknTZWxy9d9xrHkGM_kkjcLB0Ly6jU47yZvr6M1nWpV_4wQ9qK-qYViiy-iYqKXhWRTIqYgV4OWYZmOmXcGSgXikmsmoD2rgy2iz9EFbjHo4NKTRvESXWcvIlZNF7XYEuTBGIhaLe0c9Pi7Je2KAIzcWM5RIR30EW8IQvcUKT1R4o2zQV90z48IzsO4n9dtzVMQt1ZaDIU2ZzrR4e6ghoSRFDSRHEI2UTOqnVKnOprXet-AtPNeNkpzfWZ5ZhpykmP0XIrL5eqXFlYQHQIxzwjnax3Dyb05AUOWHUpu78mGNtTSR_EmxKpYfbWFEVYV_f2dHVjBIbiyoYNFysQqDV1McH-5tLOdk5pSm_689EOXmjzKJlIX28MaHbQDYZzoRhDeRPsRYffjxfT_YpgXMGEtLyKhsBnrAE1vVH3mxLOgVn55-s_4xw52xZa-5QskXmF27gZYlBvWHQORQA6JGoA27yMiW7Onlq2NNkbT9lGGGyI8HOeBoVBfKoAXOZ6h5AMVAwGrVRHFtmwUeOXQ-QlyMLC_yzIcyiLs_-3HotEgJkOGhaM02XWprM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8edb01b99f.mp4?token=KL6uV-k4foLmRz91ykRL0ZFCPT1-hDZt2eQl9cg4FWoLkwYGh3MplH5sFOup_xkHXdlBHs7mgHyf__6lIXpuXmy9wRB42GKCTf9ZGFg5_KbfrSR-8npknTZWxy9d9xrHkGM_kkjcLB0Ly6jU47yZvr6M1nWpV_4wQ9qK-qYViiy-iYqKXhWRTIqYgV4OWYZmOmXcGSgXikmsmoD2rgy2iz9EFbjHo4NKTRvESXWcvIlZNF7XYEuTBGIhaLe0c9Pi7Je2KAIzcWM5RIR30EW8IQvcUKT1R4o2zQV90z48IzsO4n9dtzVMQt1ZaDIU2ZzrR4e6ghoSRFDSRHEI2UTOqnVKnOprXet-AtPNeNkpzfWZ5ZhpykmP0XIrL5eqXFlYQHQIxzwjnax3Dyb05AUOWHUpu78mGNtTSR_EmxKpYfbWFEVYV_f2dHVjBIbiyoYNFysQqDV1McH-5tLOdk5pSm_689EOXmjzKJlIX28MaHbQDYZzoRhDeRPsRYffjxfT_YpgXMGEtLyKhsBnrAE1vVH3mxLOgVn55-s_4xw52xZa-5QskXmF27gZYlBvWHQORQA6JGoA27yMiW7Onlq2NNkbT9lGGGyI8HOeBoVBfKoAXOZ6h5AMVAwGrVRHFtmwUeOXQ-QlyMLC_yzIcyiLs_-3HotEgJkOGhaM02XWprM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
#فوری
؛نتانیاهو درباره ایران:ما رژیم ایران را سرنگون خواهیم کرد.
ما این رژیم را شکست خواهیم داد.
🎙
مجری؛
«شکست» چه معنایی دارد؟ آیا سقوط خواهد کرد؟
🇮🇱
نتانیاهو:
سقوط خواهد کرد. ما آن را سرنگون خواهیم کرد. این رژیم به هر حال در آستانه فروپاشی است.
🎙
مجری:
آیا رئیس موساد، رون گوفمن، برای سرنگونی رژیم ایران تلاش می‌کند؟
🇮🇱
نتانیاهو:
تمام نهادهای ما، تحت هدایت من، برای سرنگونی این رژیم و شکست دادن آن تلاش می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71019" target="_blank">📅 20:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71018">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5723b906.mp4?token=OM1gw-aa84bQcDDPG_S0s5cwWVMitkosF67arMccQSv_FyQx5tx2HS6_tcigcPddG4wYnN2HpIV3K4CAL7Sq_2tRgqWi0HsUeN0MslHxCvT_AwJwN5602WIdQESU7peFp74SaiDhnyWlXV4Dw1YM9SYh8DpGorNBFNItuOlTFR7_F2bOtKUp7Z-yhSmI0Rwgq7-M-SGRNzUd7-lAfoofWye3i6ebh2_W4m6VGr9gM66PbkWk7urXol3EfLyxUNpgsYjb19kVHYuGQ6AJfNMhF4VNc9bOL2DV8JDt25aO1xrn2gZbW-LwSPr-1ZqmR2R6j0PehK2Ri7J6GsNgfNbNXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5723b906.mp4?token=OM1gw-aa84bQcDDPG_S0s5cwWVMitkosF67arMccQSv_FyQx5tx2HS6_tcigcPddG4wYnN2HpIV3K4CAL7Sq_2tRgqWi0HsUeN0MslHxCvT_AwJwN5602WIdQESU7peFp74SaiDhnyWlXV4Dw1YM9SYh8DpGorNBFNItuOlTFR7_F2bOtKUp7Z-yhSmI0Rwgq7-M-SGRNzUd7-lAfoofWye3i6ebh2_W4m6VGr9gM66PbkWk7urXol3EfLyxUNpgsYjb19kVHYuGQ6AJfNMhF4VNc9bOL2DV8JDt25aO1xrn2gZbW-LwSPr-1ZqmR2R6j0PehK2Ri7J6GsNgfNbNXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از دیدار محسن نامجو با مجتبی خامنه‌ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71018" target="_blank">📅 20:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71013">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5fMGAXuaXGaC4m5gyoouDGIpcDGhaSQW1MBkRIA22pBz-K2lZjJHjP-g3FW3fHzbULrY4v3flI05N-dFxujZz3tjohuFbqQTD5E5slT4rKl9xd7e_kLCp6ErjF9cYf5m4dDd-fLt4KLmLWc_xzjfENcYQgVSXJwyABWpQJgQiuOMKLS-o67ru0lLC8Wro9inpjwb0F0BmGcb2DibqTO4IFNXG9z3Rq-lIpj9GOLfB192hco3aVJA19MVW0EB_Q0LXyM7QxNh2dEBO1utjIXIb6h1qGh6QE58aMxAEhCVnfbNxEuALOSkGoQ25Dc3VVULwEQuE0u32FOSEEEgsbfMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDQc7T_0bOY3oinUIIRDSis4McC7mSMWbxC6G6Dd-dDxSCvLC4UB-l2QwO8KK_2INGVM7Eq8OZNzCV-0y8OFWm5ozL5u7SJD1k6qgO_S1RZ19V7I8TU5KM8HnElgmMNrRoBlY9cvDCfA0RDwDE1_30y3dkJWCML863apjBgiry8i_QW7KSspWL22cszI6k-5X2Bx1eLWwU86jW3rHVLBa57Wc7f9UzUAX9mGwBZTVaGdw_MzdsccxUGKYFK2xXEfTXSQbTn5oDaZ_qMRtyHB-mb0dXNGUeGllz48IwTJA2YwAgyT9kLLPBEgsAIHI3ZEcaDMALtJk0n3e7sRjbhouw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21e8023466.mp4?token=I7TSvjg2gvIfhTrpVVWTtiajbtsA0GkJtTp4ntbfNGd0uuesQlLJ5ytvr_RwGlbICP1ovSIM17gc5n3omLlUg7MwsVXJK0RzDoyhpjGe1GUl-jJkZQvWosL9RxVGz6fYfHwFEM-q-LIETnpK6ZRULjdtGGqGOfazfcKgQI-J4bu4t_K3Ua7HGPI48FUWxJLkbImFhMKSBPch3X2nCacm42JBakh2PvR_5ABU4kCGcZPF6DjsyRS_2xQtwav3ESyRwUSEMmR7QLdMne-CGYCQwGQaOdylzE5-4l4VEkekhnNqeFZvy468g-oNIjHu53wkbrZ-37rfx3yJKmINTJaH5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21e8023466.mp4?token=I7TSvjg2gvIfhTrpVVWTtiajbtsA0GkJtTp4ntbfNGd0uuesQlLJ5ytvr_RwGlbICP1ovSIM17gc5n3omLlUg7MwsVXJK0RzDoyhpjGe1GUl-jJkZQvWosL9RxVGz6fYfHwFEM-q-LIETnpK6ZRULjdtGGqGOfazfcKgQI-J4bu4t_K3Ua7HGPI48FUWxJLkbImFhMKSBPch3X2nCacm42JBakh2PvR_5ABU4kCGcZPF6DjsyRS_2xQtwav3ESyRwUSEMmR7QLdMne-CGYCQwGQaOdylzE5-4l4VEkekhnNqeFZvy468g-oNIjHu53wkbrZ-37rfx3yJKmINTJaH5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
حملات جنگنده های اسرائیلی به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71013" target="_blank">📅 20:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71012">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/600c9063c3.mp4?token=fkknasdlyaj71SKNQ6_a0BnxKCh_kOWVp6rN7_E1Ns9gQx1DkDTYSYMKt8AEVaz90RyLStTF4gA3PARcMOQe943rF5x5wKHodWjXLC6Xn-nqQ_kl2eX-_IKkkNy4ZnkLqn4HF2kI_S7YHuOGNGzDKYZbmfAt87-N5NLGuN1G4lzSHGScnW8FYeTa0650PkssO3motT-XsThqTx2Nwaw44tFJ5RuEi3ZabQ9s5cVlSRwnZvyFsCS26WQUjsJbETDgXoQZaQmLTuqMdDmMOcOWUGVgAI4hghj1rxXZ8EuaZyY8uIHuTFMcw5gEoUiFV3EXAqf9M7_AxtT0BYo9nF2zow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/600c9063c3.mp4?token=fkknasdlyaj71SKNQ6_a0BnxKCh_kOWVp6rN7_E1Ns9gQx1DkDTYSYMKt8AEVaz90RyLStTF4gA3PARcMOQe943rF5x5wKHodWjXLC6Xn-nqQ_kl2eX-_IKkkNy4ZnkLqn4HF2kI_S7YHuOGNGzDKYZbmfAt87-N5NLGuN1G4lzSHGScnW8FYeTa0650PkssO3motT-XsThqTx2Nwaw44tFJ5RuEi3ZabQ9s5cVlSRwnZvyFsCS26WQUjsJbETDgXoQZaQmLTuqMdDmMOcOWUGVgAI4hghj1rxXZ8EuaZyY8uIHuTFMcw5gEoUiFV3EXAqf9M7_AxtT0BYo9nF2zow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مردی در نیویورک آمریکا پس از برخورد مستقیم صاعقه به پایش جان سالم به در برد
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71012" target="_blank">📅 19:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71011">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuiNmWMs1c6Q0FTLPyNML_qWy9G5R0IX5JEnzGOumXy76CQPTE9-wIAZdpJ5vT0ZEMHUSX_P97K557qMaBw7_jZFCdJ-dgEvaip7sCpKZmUe_L5d1mmeLLf86Yt3J5CNePd1lYpbUFg_1MO15jhSIgJajIR5_1r8mYeIjdHBRm4o3kQEmNCo1Kd-lpTpsIorDl3s1BzaF9JLpAUMTddICsl-ge03tdxHy6cpvru0jkcxDCO7x3WV6qG5DQ8kS3LkZ3hcSD0V3z2GpLgRe-rrTSxFuLvzLG4_JyqvFdBG6NYa_YITv1w076z-t3X-fbQ7Wfjr0_w_PU1nU8P53rdUWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال:
حالا که تنگه هرمز تحت کنترل ایالات متحده است، آیا باید نام آن را به «تنگه ترامپ» تغییر دهیم؟ این تنگه هم درست مثل خودِ آمریکا، «داغ‌تر» از هر زمان دیگری خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71011" target="_blank">📅 18:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71010">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اسپویل:
سپاه دوباره موشک می‌زنه و ترامپ هیچ گوهی نمی‌خوره
#hjAly‌</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71010" target="_blank">📅 18:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71009">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f635b0ff.mp4?token=T9itzoYSOGkyoRsccA_1vRumwIP3SUHCrKpQYBGBIjWkLtVwL5bf9e3_t4NBSCV0MyNb0f2_QpGUzEPImCNJnMNu0eK9IgU5ltUQwgvW4VeFucJY1Ya7LlTZkrTQayKGesZBX4mUbTdOMsVm_-3MNEQdEplYvM5GsYSsqjTsHGdXKBMq7Zkw-Eo8h2-lPDH1rzjLTBG9DU4l0-lXhsP81OhOG0znxxQLPjmVpaOyHu-RIns52E-lrDB8JeV2Gr8mw1UZr-JKXXnLPRTNQBNavG2viScrEYstij-CPEGkRI1XZE14Jej_ubzQG5k4eFAgrSSnvEEsyl5MonwX-AmAEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f635b0ff.mp4?token=T9itzoYSOGkyoRsccA_1vRumwIP3SUHCrKpQYBGBIjWkLtVwL5bf9e3_t4NBSCV0MyNb0f2_QpGUzEPImCNJnMNu0eK9IgU5ltUQwgvW4VeFucJY1Ya7LlTZkrTQayKGesZBX4mUbTdOMsVm_-3MNEQdEplYvM5GsYSsqjTsHGdXKBMq7Zkw-Eo8h2-lPDH1rzjLTBG9DU4l0-lXhsP81OhOG0znxxQLPjmVpaOyHu-RIns52E-lrDB8JeV2Gr8mw1UZr-JKXXnLPRTNQBNavG2viScrEYstij-CPEGkRI1XZE14Jej_ubzQG5k4eFAgrSSnvEEsyl5MonwX-AmAEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ما اکنون کنترل تنگه هرمز را در دست داریم. ما آن را کنترل می‌کنیم.
دیشب ۲۸ قایق و کشتی را از کار انداختیم. ما کنترل آن را در اختیار داریم، آن‌ها هیچ‌چیز به دست نمی‌آورند و ما آن کشتی‌ها را نابود کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71009" target="_blank">📅 18:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71008">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/116dfeb2e5.mp4?token=BRvt73bzbI_bMJd_4DxOMhjxjPFj8ErBUPwBzxjBndzHgeSgE64ohTISnOjhWj5mEX7wEuOCEf8M5bOu2sz6Sxia-jFHX-UQZAbC6cYKl1zfoFVzEgxDP63xZHC2vfvPUOBut0VZIAq4ohkfVctINMuoXo4Z699P-0shZryuGJKWaWS2XkOt_mQ8kI-ApPd3IeMl3hy9qi5gcgrClOGEy10N-M9ZGoPzBb2ov9eBgpm5EETSfGWmxAAvhZmvLFMSW2EPmjXc08t859sBznawkE-jRxZNgA-hDzwkNXvm609IcdmyhP4JAx9hQ4hy-NtMebMcD1jR5wXZNcw-jOydUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/116dfeb2e5.mp4?token=BRvt73bzbI_bMJd_4DxOMhjxjPFj8ErBUPwBzxjBndzHgeSgE64ohTISnOjhWj5mEX7wEuOCEf8M5bOu2sz6Sxia-jFHX-UQZAbC6cYKl1zfoFVzEgxDP63xZHC2vfvPUOBut0VZIAq4ohkfVctINMuoXo4Z699P-0shZryuGJKWaWS2XkOt_mQ8kI-ApPd3IeMl3hy9qi5gcgrClOGEy10N-M9ZGoPzBb2ov9eBgpm5EETSfGWmxAAvhZmvLFMSW2EPmjXc08t859sBznawkE-jRxZNgA-hDzwkNXvm609IcdmyhP4JAx9hQ4hy-NtMebMcD1jR5wXZNcw-jOydUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
🇧🇭
لحظه اصابت پهپاد شاهد-۱۳۶  به مقر ناوگان پنجم نیروی دریایی آمریکا در منامه، بحرین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71008" target="_blank">📅 18:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71007">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzsDCAPFz9BX0h9ys6jXqQtjeAo-vJ83OQqg0hXDvQWdaXWKjLq88jgYbzyblJehVXzyvgJmByIfTrSPYCS89HKgVjmBw1PWrhjujZbKajd9jMZyKG9F1Htjh_tx8hpWM615h5izj_nNBuLGhZMtOqjXvGGNf37tAe3P_TCGYY5pQB3dTxfu5HxY0AimbdwQbDoluaisJCCsLlq4U_naBPMSHL03KxJlu9vowtFVMo02Vsn_FtNKNKZBlyyoWf47U8SM2YyZAeVzLcqS5i4K_qETYhKbcFVyb4yCtX7tu94sJe0BukySvB8ZDEFGCwlkEDMFzwESdUBrPCw81lKnXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه:
ایالات متحده به هدف قرار دادن ایران به دلیل حملات به کشتی‌ها ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71007" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71006">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71006" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71006" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71005">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baYY48YIae203x13l62TUuRfTiylJGPhGIh6vNtf9iskeqaYBKNIalBwQjOg3roeVF0OSkjDt7KoE1Ak1JjvVC2ckGsplhuEJShF4lz9Xja-uIBt2snYsa9C4k7uWyAQ44bH-tbXG3sFZSoeRxWVim_HyTYQO7RFypvWq30-0iCGdRM-Zvgi_7ZVLouU5IKfj5TOhaQrJUmB33tcm-X9H9gkWUsYZZyS8aRN-xTwfEjaHNKrkKxbLKXXOSguaH7dcEyyFcjt4xjvcvDqcJD42DLCT_wdlzoWsvBCzE7RPZjEyR6iBDJqNSusTcstybbE1qT32xduNMwjq8RqkaYnEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
استقلال
🆚
پرسپولیس
⚽️
پیش‌بینی دربی رو در
TrexBet
از دست نده!
📉
نگاهی به 5 دربی اخیر:
2 برد پرسپولیس | 0 برد استقلال | 3 مساوی
4 گل پرسپولیس | 2 گل استقلال
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71005" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71004">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26734edca1.mp4?token=jHlXhsrc-hiw-EiT_E7YipENOoFF6Cbbzm56P4oO1Jy1DQhXHJp-47wdPqAe9_awf1x8WCXiW27NqydInDiQuRhlqAT8amPiohYVB4oQn3X52NnqtSQk4BWtcMZFC5YLfUMkc1DTarjj6GhCtjHSb1WTXlWvX-Pr6-7zlp2M9deDvww81lASdoHGYDq6xrM3oOpMZJt69BnaKyrfuLj8VygJ6y_lH5Rwb6GHMayGE_v0N3Vu7zQf7yyDrn5fzgjG-xOG0Umm25GKso09lsIbn5-tUiXuOBjNdlh13S4Al0WEB8VI-8h6qMTUDhLyPYnLz4u9vO5sgTnTpjSO319Tig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26734edca1.mp4?token=jHlXhsrc-hiw-EiT_E7YipENOoFF6Cbbzm56P4oO1Jy1DQhXHJp-47wdPqAe9_awf1x8WCXiW27NqydInDiQuRhlqAT8amPiohYVB4oQn3X52NnqtSQk4BWtcMZFC5YLfUMkc1DTarjj6GhCtjHSb1WTXlWvX-Pr6-7zlp2M9deDvww81lASdoHGYDq6xrM3oOpMZJt69BnaKyrfuLj8VygJ6y_lH5Rwb6GHMayGE_v0N3Vu7zQf7yyDrn5fzgjG-xOG0Umm25GKso09lsIbn5-tUiXuOBjNdlh13S4Al0WEB8VI-8h6qMTUDhLyPYnLz4u9vO5sgTnTpjSO319Tig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
📰
اینترنشنال:
⁉️
🇺🇸
🇮🇱
از شهروندان پرسیدیم پاسخ شما به پرسش ترامپ درباره زمان قیام مردم ایران چیست؟
یک شهروند با ارسال پیام صوتی به ایران‌اینترنشنال خطاب به دونالد ترامپ می‌گوید: «چه تضمینی وجود دارد که ما بیرون بیاییم و تو بعدش مذاکره نکنی؟ ترامپ، کار را به نتانیاهو بسپار که او بلد است.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71004" target="_blank">📅 18:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71003">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4349c8ad3.mp4?token=Lus5V2NfJdROM1LfGKZi7ijfyIQYIWzQVQjxZFaWk6Dj-zmDSdPsHjp8MT81XmBFEzHVR4qD90ASdu_LDrZL5P79DM2YbGhMJZuBovietU9sYw3fQSrmZuSqSV_szbn_HQDrsO2HscCymvaNYmQS-DhwGZFlebXXDMtMB8WRaz1lvpQyEPYijpxrN3_zvEM3FVxREr7QBEPXfoWkLsgcR9KXoUzNjJDijiwb99KlnRlLFfPlwYx4c0RVKw4egxJaSMg-sNEmSxMHOtjJewWMH0B_fZv6sG58s7cFtEQnOl4P6LZW6Xn9d6a3M9TxNX9nliPXYdG7_wLPk5EWqbUUow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4349c8ad3.mp4?token=Lus5V2NfJdROM1LfGKZi7ijfyIQYIWzQVQjxZFaWk6Dj-zmDSdPsHjp8MT81XmBFEzHVR4qD90ASdu_LDrZL5P79DM2YbGhMJZuBovietU9sYw3fQSrmZuSqSV_szbn_HQDrsO2HscCymvaNYmQS-DhwGZFlebXXDMtMB8WRaz1lvpQyEPYijpxrN3_zvEM3FVxREr7QBEPXfoWkLsgcR9KXoUzNjJDijiwb99KlnRlLFfPlwYx4c0RVKw4egxJaSMg-sNEmSxMHOtjJewWMH0B_fZv6sG58s7cFtEQnOl4P6LZW6Xn9d6a3M9TxNX9nliPXYdG7_wLPk5EWqbUUow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
فردوسی پور:تاج و دوستاش نزدیک ۲۰ میلیارد از پول بیت المال رو گذاشتن تو جیبشون.
چند وقت پیش تیم ملی جوانان ایران واسه برگزاری یه اردو قبل بازی‌های آسیایی، به ترکیه سفر می‌کنه.
تو آنکارا، هزینه هتل‌شون طبق سند خودِ فدراسیون، 116,160 یورو شده.
بعد برنامه ۳۶۰ زنگ زده به همون هتل گفتن که قیمت‌ها اصلا این نیست و انگار مسئولین فدراسیون قیمت‌ها رو الکی بالا بردن! و هزینه ای که کردن چیزی حدود ۳۶ هزار یورو بوده.
خلاصه تاج شیرین نزدیک ۷۰ هزار یورو کرده تو جیب خودش و دوستاش
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71003" target="_blank">📅 17:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71002">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1896637f6.mp4?token=exqdaYmKGGVRNfTOZYB3vxGXhSc5kCgznSAsFeVNaXSx_sDHpNZryNgBuHjJhn_pRNXdS5ewWIck5aRZC1Iu365eictU-IG-kuIvZ7s2S-u-TolXdkGei-6626TiFtrllDTpLw3NT-9SEPTxEcxPVUrZHBtKzKtByGqv1A5Xw2to16p1hykaHjsdmE5F86hiLDI7vB0grrhkp9FNJ0bjx_8jqUSds0Z-MZLwLvMMu3aLxy-ZATh5LuOBzh8w6uUwYqLRiCqmvQFx8hiHCzsTNP4CdTlZScLoAMDCflZ_-TJpOdPJM82f7bWJ9ZTAREe41uBMrjBqvT5vjEOaPPFIH3MikzAV79GgaG9aIoBjk_4l00PJh_H7VdqDw41lY7RclhwpxsiGgS726ZtaKCZ1UYvWsoEaWJnhZO1VKppBtS91ORrCAXDkcOwlirkiy1t6S0q9stCDuqEronnvpuKGAdFFUeQnznQrLKhvVyvRTfj4a12l9nH9zrTIOMGEnadLMggUfHLAuTBn7FuWTtL2oezb-PKiDkzotL9_30900TpoNSZmYeA3YyyNUc0xQrR7NCgmWHo8cKRBO3vM3hhdzp6u9SMePHJcDWeYo85JHt3KL4Mm90-GC89BAFPZbbiQRgLJo80OWxA64ck3y_x23ftzCGuNOLT6QxocmoPHDpM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1896637f6.mp4?token=exqdaYmKGGVRNfTOZYB3vxGXhSc5kCgznSAsFeVNaXSx_sDHpNZryNgBuHjJhn_pRNXdS5ewWIck5aRZC1Iu365eictU-IG-kuIvZ7s2S-u-TolXdkGei-6626TiFtrllDTpLw3NT-9SEPTxEcxPVUrZHBtKzKtByGqv1A5Xw2to16p1hykaHjsdmE5F86hiLDI7vB0grrhkp9FNJ0bjx_8jqUSds0Z-MZLwLvMMu3aLxy-ZATh5LuOBzh8w6uUwYqLRiCqmvQFx8hiHCzsTNP4CdTlZScLoAMDCflZ_-TJpOdPJM82f7bWJ9ZTAREe41uBMrjBqvT5vjEOaPPFIH3MikzAV79GgaG9aIoBjk_4l00PJh_H7VdqDw41lY7RclhwpxsiGgS726ZtaKCZ1UYvWsoEaWJnhZO1VKppBtS91ORrCAXDkcOwlirkiy1t6S0q9stCDuqEronnvpuKGAdFFUeQnznQrLKhvVyvRTfj4a12l9nH9zrTIOMGEnadLMggUfHLAuTBn7FuWTtL2oezb-PKiDkzotL9_30900TpoNSZmYeA3YyyNUc0xQrR7NCgmWHo8cKRBO3vM3hhdzp6u9SMePHJcDWeYo85JHt3KL4Mm90-GC89BAFPZbbiQRgLJo80OWxA64ck3y_x23ftzCGuNOLT6QxocmoPHDpM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طراح ارشد موتور (بمب‌افکنB1-Lancer) متولد سیرجانه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71002" target="_blank">📅 17:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71001">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618f407212.mp4?token=aJORI91Hcdkr46wMstUD8JnsZpOetjXWGB9xV34-W5wt2eOai_b3oCyV9QO9lZcrKsNE-9eBdpcdm6k2dr_2arhUxGUtvNRgC8qMoAf_ptSOdQWxRH4aT9Z_eAhbXA_gzOWn7_KuM6LbitlviLBNza4my7irYrjYJSq_u1TNgh2pxeLKw91XnRxorQS58RX_EzXwbpaobexmv-iHaa_woWvf2xqyctSvE_gR-6KfLZdOCleDItkuR3fGaJW1L6liARLKq9SSpgtVTXXU3vxwS2JEhhdjuHLOvu_xB56U1aHDAzW_fbLgapKpfyXOi__GjtEZy7V5KLBvsv4VHHoreA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618f407212.mp4?token=aJORI91Hcdkr46wMstUD8JnsZpOetjXWGB9xV34-W5wt2eOai_b3oCyV9QO9lZcrKsNE-9eBdpcdm6k2dr_2arhUxGUtvNRgC8qMoAf_ptSOdQWxRH4aT9Z_eAhbXA_gzOWn7_KuM6LbitlviLBNza4my7irYrjYJSq_u1TNgh2pxeLKw91XnRxorQS58RX_EzXwbpaobexmv-iHaa_woWvf2xqyctSvE_gR-6KfLZdOCleDItkuR3fGaJW1L6liARLKq9SSpgtVTXXU3vxwS2JEhhdjuHLOvu_xB56U1aHDAzW_fbLgapKpfyXOi__GjtEZy7V5KLBvsv4VHHoreA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بررسی قیمت چند داروی پرمصرف از شهریور ۱۴۰۴ تا شهریور ۱۴۰۵:
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71001" target="_blank">📅 16:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71000">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df28769cb3.mp4?token=tT5_Lfpt6-AjZ-UOYqf0LDA3jM_OIIYBjUhAStPbpiGW91zVIeA-a07hFPDCRtcQFAs3pas1kwmo-OZ4MhqvhCV25wgbMDAgigFPZbwDTvYJjUAX4vryzPNLan4juXh2svk5Fexe-rgllHSmPnFZ_xxk1QR6ZUv5ZRKYVctdlF8BRFh0hCn02K1M1bALrO5Lj9BUbrCiGdcPJUWoe2Wn5qIa4jpJK8DI-CTOya9QPARw_RgFz_LBSpcNfpWYkhZ6yaGwcb0fSUf9-nDL654Fo8hATfa6qqRhA0D5VHmWuR2dnpmF_Nv7vbowhfvU3Kb2BTOumNUxtODnbGQG85FA-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df28769cb3.mp4?token=tT5_Lfpt6-AjZ-UOYqf0LDA3jM_OIIYBjUhAStPbpiGW91zVIeA-a07hFPDCRtcQFAs3pas1kwmo-OZ4MhqvhCV25wgbMDAgigFPZbwDTvYJjUAX4vryzPNLan4juXh2svk5Fexe-rgllHSmPnFZ_xxk1QR6ZUv5ZRKYVctdlF8BRFh0hCn02K1M1bALrO5Lj9BUbrCiGdcPJUWoe2Wn5qIa4jpJK8DI-CTOya9QPARw_RgFz_LBSpcNfpWYkhZ6yaGwcb0fSUf9-nDL654Fo8hATfa6qqRhA0D5VHmWuR2dnpmF_Nv7vbowhfvU3Kb2BTOumNUxtODnbGQG85FA-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرت زدن وزیر ورزش و معاون وزیر خارجه و تمیز کردن دندان توسط وزیر خارجه هنگام سخنرانی پزشکیان
😃
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71000" target="_blank">📅 15:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70999">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIUWbj5IAmUuQKv-MGjWdb498P36ZUJyLWyhktzEZ5V8TnOPf1kZLalrNStdQkYN91LXzmI7l5ngD0bgGeLPpDa5hpdDNq8HIHuSVwxpa8pYY3k58NfuLRQ5_71_VGtpWm-PPqMxz4FEHPStckSLqtXKw5KpWIAW19jTS32VDL-FlQlxAZ5NMCN2c_g73Ma3wwz3pK1_ueLsYj7ic9GLByYEZdliWXg5Udmdq6--osqF2noKIufj-QgJG3wG9Qaym6QKW0dezjYOOVY9_zLZjlZDyLIiHzhdcdAUJCe19pGIMzYg5eI0n2Fh2wYtuj06qYeV19S-B7MvUoL39MOP_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارش تأییدشده‌ای مبنی بر درگیری یک نفتکش در یک حادثه امنیتی دریافت کرده که منجر به دو مورد تلفات انسانی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/70999" target="_blank">📅 15:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70998">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bqt2X-v4QV3z3uq0j2VIC0EwVKd0cG3UvghSvnaJ3XItPuOAi5idLImmcpTxLBfcz9VQ98QJssGPTBYBV6JxJA3Dpmf682j_R57e7_SQWT6_16gcMgsNPcPadx2todzYzKMpt7fguY7wMNKCgY5xPC82PPBexRVTU9oxnDKQItIMPCPe7xBaOD0AzmEulXI54hbtVOn9qnRc9DBAd383I18Hj5dsucKohYID6NVHJTD5FgZUV4SGnxMlFkS-rEpLBAT-siFE40tOiwkYIN6S8bSsgr60dtx-o0ZHeWts01JGYNqfzeO6C9iuQv_H_dzrMjchivbrdMywAs0biZ8m1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
فیلد مارشال محسن رضایی:
با این دست‌وپازدن‌ها، نه تنها در بیرون آمدن از آن ورطه هولناکی که برای خود رقم زده‌اید ناکام خواهید ماند، بلکه به‌زودی خواهید دید که راهبرد جدید ایران در میدان نبرد، دیپلماسی و مقابله با محاصره اقتصادی، بنیان‌های شما را درهم خواهد کوبید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70998" target="_blank">📅 14:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70997">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13235e9918.mp4?token=vDSs8U-iF_5uPHE8GUOGLm-raejao0Ny_AM4-7VNKiPnVX7PJijsPHpExi9GwPrOQ9IRQc4xWVp8XK6Dyu0J-pXIkbzk5M76eZRJLljH-9yrS39GBNU9p5fkv0a3f4GIKwsPI02nbDECp7YBp8aEZODWc0zj7hRpHbWMhXx14c4IWCeu6Z6Ze8_PBVs5Odt-6DvoOnLq__gVe8hzhmwBn5J88ZpI6z7R5JiAmXlCjct1F3Vi_9eEkBDWGi920D0nbRWwHOx8vVg-wDQiCKKEQg-cUHouwxj3KNFxG6g9V9DYH2Adb7a9QSxaqucin-F9TcOqsv1Tqz0t6tnseDRKPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13235e9918.mp4?token=vDSs8U-iF_5uPHE8GUOGLm-raejao0Ny_AM4-7VNKiPnVX7PJijsPHpExi9GwPrOQ9IRQc4xWVp8XK6Dyu0J-pXIkbzk5M76eZRJLljH-9yrS39GBNU9p5fkv0a3f4GIKwsPI02nbDECp7YBp8aEZODWc0zj7hRpHbWMhXx14c4IWCeu6Z6Ze8_PBVs5Odt-6DvoOnLq__gVe8hzhmwBn5J88ZpI6z7R5JiAmXlCjct1F3Vi_9eEkBDWGi920D0nbRWwHOx8vVg-wDQiCKKEQg-cUHouwxj3KNFxG6g9V9DYH2Adb7a9QSxaqucin-F9TcOqsv1Tqz0t6tnseDRKPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
پوتین خطاب به پزشکیان:
تو این شرایط سخت، داریم سعی می‌کنیم هر کمکی که لازم دارید، بهتون برسونیم
.
قبلاً هم دربارش با هم صحبت کردیم و داریم کالاها و اقلام موردنیازتون رو تأمین می‌کنیم.
با وجود شرایط نظامی و سیاسی فعلی، همکاری‌های تجاری و اقتصادی‌مون رو با همون روند و قدرت سال گذشته ادامه می‌دیم.
همون‌طور که بارها گفتم، ما تو روسیه کنار مردم ایران هستیم و باهاشون اعلام همبستگی می‌کنیم. شجاعت و مقاومت شما واسه دفاع از منافع ملی‌تون واقعاً قابل تحسینه.
لطفاً سلام من و حمایت صمیمانه‌ام رو هم به رهبر جمهوری اسلامی، مجتبی خامنه‌ای برسونید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70997" target="_blank">📅 14:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70996">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">1
💵
= 200.000
💸
🔼
یک دلار آمریکا=دویست هزارتومان   @News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70996" target="_blank">📅 14:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70994">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a6a11bf6.mp4?token=jlho69FEz3W7XU3D0FWFrQJ1OX9p0XUh_tPXxRxHWmrlVXCkAJX08-l9yZgQCvDhJdOR6FleInhQJiRxQBUYrpeUbHW7FJ0I8MN365RptQLShmZGmTvkMKlVwanthQH9UgdgBGRxDcBXsckjA-ND-Ib3Ofl--Nz65e5QL4tXAZ3SlYcwJxwn0TSfU0B51AzSEmiWhphgBBF_b0tRAb8d6TT8LkR6Ygeg0OCtVeS6df54TaZsBHkfQbnmTj6rjSWGD58l6mw5qyy7bNRI7VWXxzCyNgdCIOQ2AUDCCl66se57OsXR017cRlbkFFtu8zrFVx6iLbrKZly1PybWT4s66g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a6a11bf6.mp4?token=jlho69FEz3W7XU3D0FWFrQJ1OX9p0XUh_tPXxRxHWmrlVXCkAJX08-l9yZgQCvDhJdOR6FleInhQJiRxQBUYrpeUbHW7FJ0I8MN365RptQLShmZGmTvkMKlVwanthQH9UgdgBGRxDcBXsckjA-ND-Ib3Ofl--Nz65e5QL4tXAZ3SlYcwJxwn0TSfU0B51AzSEmiWhphgBBF_b0tRAb8d6TT8LkR6Ygeg0OCtVeS6df54TaZsBHkfQbnmTj6rjSWGD58l6mw5qyy7bNRI7VWXxzCyNgdCIOQ2AUDCCl66se57OsXR017cRlbkFFtu8zrFVx6iLbrKZly1PybWT4s66g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
〰️
ناو «یو‌اس‌اس آبراهام لینکلن» در تاریخ ۲ سپتامبر و پس از ۲۸۶ روز حضور بی‌وقفه در دریا — که رکوردی مدرن برای نیروی دریایی ایالات متحده محسوب می‌شود — وارد بندر «لائم چابانگ» تایلند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70994" target="_blank">📅 13:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70993">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل درباره ایران:
هم‌زمان با افزایش فشارها بر آن‌ها، تشدید تنش‌ها و تنگ‌تر شدن حلقه محاصره — آن فشار اقتصادی خفقان‌آوری که رژیم افراطی بر مردم خود تحمیل کرده است — احتمال دارد که آن‌ها واقعاً دست به حمله بزنند.
چرا؟ زیرا ممکن است برای رهایی از دوراهیِ میان «خفقان» و «جنگ»، گزینه دوم را انتخاب کنند. ما از نظر دفاعی برای چنین وضعیتی آمادگی داریم.
اکنون در ایام تعطیلات هستیم و آن‌ها معمولاً در تعطیلات یهودیان دست به حمله می‌زنند؛ هرچه باشد، آن‌ها از یهودیان بیزارند.
اما ما — هم در حوزه دفاعی و هم تهاجمی — و با هماهنگی ایالات متحده در این جبهه آماده‌ایم. بله، در همین جبهه.
با این وجود، سناریوهایی وجود دارد — مانند حمله به اسرائیل — که ما به هیچ وجه آن‌ را تحمل نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70993" target="_blank">📅 13:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70992">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0dd8120289.mp4?token=QQhqFOF3uFeMlrMotuFHe8JpRQBoMXIcGusGXs0Xidbt3rb1Uv4DYrtrykVaesvGDYPYR8pVS-eYPCTErt2SJBog-PN0hHkmlMY3fvP4aeGU2bBnR3sWs2kgkl76_ZZsb9fvxiKvPXTosEGBnOsAYur3HOWQbRrjAnmJFVvwFPgZ24j7TGfeH05bEI55e52lQAzXNiNMLhnVqrb3dA2cM3BIUP3eAfxdBbT4czu0X2859j4LRAYfVHHE1ukvaIKJrB1AJIA3fjQTmDhOguabEfrVj3zyPHv75lq9yxmWtPfoI1D4OU-wCOth0wXrZyUs3TLLyBocD2ZO4rnDJukqlg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0dd8120289.mp4?token=QQhqFOF3uFeMlrMotuFHe8JpRQBoMXIcGusGXs0Xidbt3rb1Uv4DYrtrykVaesvGDYPYR8pVS-eYPCTErt2SJBog-PN0hHkmlMY3fvP4aeGU2bBnR3sWs2kgkl76_ZZsb9fvxiKvPXTosEGBnOsAYur3HOWQbRrjAnmJFVvwFPgZ24j7TGfeH05bEI55e52lQAzXNiNMLhnVqrb3dA2cM3BIUP3eAfxdBbT4czu0X2859j4LRAYfVHHE1ukvaIKJrB1AJIA3fjQTmDhOguabEfrVj3zyPHv75lq9yxmWtPfoI1D4OU-wCOth0wXrZyUs3TLLyBocD2ZO4rnDJukqlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو از فروش طلا، به دلایل کاملا نامعلومی بیش از 5 میلیون بازدید داشته!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70992" target="_blank">📅 13:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70991">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70991" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70991" target="_blank">📅 13:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70990">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0_TbRrE_WbbIRsAd5cDYdt1HZh6FBd3QBJsYkZasQFuDyF05g0ZL_YnABVoeTHn9QXnAt9G-Nm4uVIB5Dectfd2q6ACviCAOCuXEALeL7X7fOFhGf-A0qE6GQJx3GqA2wY7t-McPqPKklXn2VgRBcjpTStuQqg1VYy2fZEnKZ-_EAvWl91vz16QX-XcGYDt5ub1G3izSWWOdIBA5Ye9xuA8Z8HCLXVXw5rqxN5uHTKawdaOgaB-7WwknuPU5CV6j57k-2fTRVbnVsR_toEMXMlxGbvLVshGo3CXspnQz_Kc4QpRiaWqd8ckJ1-BIlxO4ChSn6zGAJJWb-PGGZOmPA.jpg" alt="photo" loading="lazy"/></div>
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
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70990" target="_blank">📅 13:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70989">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1829295007.mp4?token=Wznchs9wKg4W2Pvc8tbvuWeMohedO63XuDoJ48kNSxp5IpXfC2FHeef9SjHskbxmr6feXX20Lk2G3jpbxMjFQ_nHr9fF9yFxh9mFln_Y0sck1g6ke3QUjvpZ8vD2yRADbrzewVqRrPuWAfHJSpAfZx3ksyjsgVVByAI9KrdyAYM0eEFLB8LJf2ir1PCoD4SvPFE1-OqdjqqvpQYmgw-sJNZDAL1-VkNfzd8AA1AwyTTIoLuT5StE9wauH7fgy3aC_RFrkHVINmXWJ-BeauVDyhtMDT5jVPj4X82ar0aXfXY2b6XZDtzO2lItP4cuzxtSwgjsE3hqIgpqD2gIGhtzZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1829295007.mp4?token=Wznchs9wKg4W2Pvc8tbvuWeMohedO63XuDoJ48kNSxp5IpXfC2FHeef9SjHskbxmr6feXX20Lk2G3jpbxMjFQ_nHr9fF9yFxh9mFln_Y0sck1g6ke3QUjvpZ8vD2yRADbrzewVqRrPuWAfHJSpAfZx3ksyjsgVVByAI9KrdyAYM0eEFLB8LJf2ir1PCoD4SvPFE1-OqdjqqvpQYmgw-sJNZDAL1-VkNfzd8AA1AwyTTIoLuT5StE9wauH7fgy3aC_RFrkHVINmXWJ-BeauVDyhtMDT5jVPj4X82ar0aXfXY2b6XZDtzO2lItP4cuzxtSwgjsE3hqIgpqD2gIGhtzZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇨🇳
⭕️
حسین مرعشی دبیرکل حزب کارگزاران:
🍆
چین سفر قالیباف به چین (و گسترش روابط تهران-پکن) را مشروط به موارد زیر کرده است:
۱- باز کردن تنگه توسط ایران
۲- دریافت نکردن هیچ‌گونه عوارضی
۳- پایان دادن به اختلافات خود با عربستان
۴- پایان دادن به اختلافات خود با آمریکا!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70989" target="_blank">📅 12:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70988">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران:
ساعاتی پیش دو فروند کشتی نفتکش که با تحریک ارتش آمریکا خدمۀ خود را پیاده کرده و برای گذر از مسیر غیرقانونی در اختیار عوامل آمریکا قرار گرفته بودند، با رفتن روی مین منفجر و متوقف شدند و در آتش می سوزند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70988" target="_blank">📅 11:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70987">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awkVcanaLF4K0fMzcv0t_uOpBSJa9wZXL5iL-XcLtecTJbHvddkwLIeeMbTur1VwTH-J7mCXoA5aLbqsMKa-4q6CMIw6vdT5Jf-VvIIlSdEjpWij2NppkU9IzTsDZ2adHbja9J1kzQXjFPZ3zvwRxbXRx3CbSnAunFPiEaF8ckaF1lmQ2htitu2TBKiTVg1T1IH8SQRyhdlVQwKx6eLoBIC4zcEIXSWYakKb7pZuhnfM-x-FoVxBv5DrutFS05p0mM6C7nSTW_kJ7emZ3kkpr1-1KLxOr5PKT0cnHVqWWjp-F_aoYNiR8NfMi89Bfyiaw95CjU05MmaVWEm2Bwa43w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ:
من برخلاف گزارش «ای‌بی‌سی نیوز» (که اخبار جعلی منتشر می‌کند)، سعی ندارم ایران را به پای میز مذاکره بکشانم. برایم کوچک‌ترین اهمیتی ندارد که آن‌ها توافقی را امضا کنند که از نظر خودشان بی‌ارزش است.
وضعیت فعلی ما را بسیار بیشتر می‌پسندم؛ چرا که تقریباً کنترل کامل تنگه هرمز را در دست داریم و اقتصاد آن‌ها نیز در حال فروپاشی کامل است. آن‌ها صرفاً دارند زمان را سپری می‌کنند تا با سرنوشت اجتناب‌ناپذیر خود روبرو شوند.
مردم ایران چه زمانی قرار است قیام کنند و بجنگند؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70987" target="_blank">📅 11:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70986">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43dc462e7e.mp4?token=HJkuOGx7Qe1ykzI8iAPqDrgTVQRq9TDBkl7xtwEXTJ44lR8_nNuqLak4CijQMHJq-Au11vBwDFSFvWq2iiIrq8psxhybuKZiEH1s3o5gRKhI2IrxFu-66xe0-DMjjwaBm-STUDGgipPtGKAnicbr-tCaSanTwFAIqISM3RwAmYxn1RYNsVmt0gHr43FtWc4mSqWENXcrNxIX-1n3UkDXXlr2aU4FbVLdvA0xA5l7wf-XO2m4OHsXUc8JXVUJXvT-rXC59T_tW0tM31blF29CU6uJxgcNrK5VzZ8TA2ELFoK-ZL05aXCPFvlX6-OE24JLU7EWIYru_BGJ5Ewv8pgs_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43dc462e7e.mp4?token=HJkuOGx7Qe1ykzI8iAPqDrgTVQRq9TDBkl7xtwEXTJ44lR8_nNuqLak4CijQMHJq-Au11vBwDFSFvWq2iiIrq8psxhybuKZiEH1s3o5gRKhI2IrxFu-66xe0-DMjjwaBm-STUDGgipPtGKAnicbr-tCaSanTwFAIqISM3RwAmYxn1RYNsVmt0gHr43FtWc4mSqWENXcrNxIX-1n3UkDXXlr2aU4FbVLdvA0xA5l7wf-XO2m4OHsXUc8JXVUJXvT-rXC59T_tW0tM31blF29CU6uJxgcNrK5VzZ8TA2ELFoK-ZL05aXCPFvlX6-OE24JLU7EWIYru_BGJ5Ewv8pgs_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عطریانفر، عضو شورای اطلاع‌رسانی دولت:
پزشکیان اول توسط شورای نگهبان برای شرکت تو انتخابات ریاست‌جمهوری رد صلاحیت شد ولی شخص علی خامنه‌ای صلاحیتش رو تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70986" target="_blank">📅 11:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70984">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dA6HgvnVfqwq_OWdfaDc2r0cum1tqYehq_n6ND2kXt3e_cTv2uXWjx80P7_qz7NK_waEofmOljv_sO2Ds-IM-OOuALL8gQpek2TNXFgEE-B7iNJNHPkjnfwIZ2Fkg86G0jhF0uM_r4O_hlCsrh8e-h3c2co9bE_ttFG6TLQFOD_GpNvRftyfB6D0x7GnRKWUxTiM0jjyTulheoI5gfrpIwT9AItu3Aq4NsGwXxvNR9Vv7kc-Vr1JoYd8OzimVG6yvZzbVOcYmRuoX4IJV_mzKYYueDDjp-OWbXQ-bo1VUKLCWSvj4iIPEgDOq8mqPfLO2obn3tbDrdJFzA0A8OEm_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f0caae86.mp4?token=QVdB-4ffC8mObp-C0fCKdghDEazyRSdv3v0kgPX2nSHLY-wjM_yJoYtHFseKrce-eIqHxxBF0puW9hCezAOPruXjHK5H9zU8XVucHjH9OLBb8Qaaj4TSrrgI-4b0SXJgWOFJxnw1mzcA5eJSIjiCxBX846LmO_J8pP6hKezhk-TpsfIvghDnVkWfNVgJ-ao63QLG88BZsV7p2jHNTyFKBxMxx7_YqoRQ4FnUEKwHQLfVt5CwSiU1GgNauZPHkzPtG_lpclHaI2H8xPYBrZAKROePxo8zkTtatwJLlTs5myVfVmXh_D8va02rRokHWBRWfrHsLC9ucchr3w4_YmAdNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f0caae86.mp4?token=QVdB-4ffC8mObp-C0fCKdghDEazyRSdv3v0kgPX2nSHLY-wjM_yJoYtHFseKrce-eIqHxxBF0puW9hCezAOPruXjHK5H9zU8XVucHjH9OLBb8Qaaj4TSrrgI-4b0SXJgWOFJxnw1mzcA5eJSIjiCxBX846LmO_J8pP6hKezhk-TpsfIvghDnVkWfNVgJ-ao63QLG88BZsV7p2jHNTyFKBxMxx7_YqoRQ4FnUEKwHQLfVt5CwSiU1GgNauZPHkzPtG_lpclHaI2H8xPYBrZAKROePxo8zkTtatwJLlTs5myVfVmXh_D8va02rRokHWBRWfrHsLC9ucchr3w4_YmAdNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇮🇷
🇮🇷
پوتین در دیدار با پزشکیان:
خواهش میکنم سلام گرم من رو به آیت الله سید مجتبی خامنه ای برسونید
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70984" target="_blank">📅 10:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70983">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48458cadfa.mp4?token=WtnzwMeVAN6rePwVe0cLwjJ00O-Yz7q2Oj2ZMygwIY67xnUAeB3r0YVo75NwvbmUEXuYA_BBFbwjuwvvFUMVd2z4HmqNofjjBeMwkadPQmQmVRZYmlQ7psom_m0uVFfJrxphWd3-GxEyZFFJbD2VOjnC5qgeDYTQqMX1MZxus6W4Kl9R00oSo8h5zg44xpMgg26ZZEn4TnxYBDgihnaPekSQjuFBFXZn72MumA3zHYQQ0vPy9WlbxfdAbvxZurcZuKeXL7WGbHZmRhbf6cQJHjuzdJtV-91f8W4uDcNhcdGtUIoLPMlwhztyNMUO7viPweuTT2YTL-LtsziEv0BFDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48458cadfa.mp4?token=WtnzwMeVAN6rePwVe0cLwjJ00O-Yz7q2Oj2ZMygwIY67xnUAeB3r0YVo75NwvbmUEXuYA_BBFbwjuwvvFUMVd2z4HmqNofjjBeMwkadPQmQmVRZYmlQ7psom_m0uVFfJrxphWd3-GxEyZFFJbD2VOjnC5qgeDYTQqMX1MZxus6W4Kl9R00oSo8h5zg44xpMgg26ZZEn4TnxYBDgihnaPekSQjuFBFXZn72MumA3zHYQQ0vPy9WlbxfdAbvxZurcZuKeXL7WGbHZmRhbf6cQJHjuzdJtV-91f8W4uDcNhcdGtUIoLPMlwhztyNMUO7viPweuTT2YTL-LtsziEv0BFDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایشون رکورد دار عمل زیبایی بین آقایونه و تا حالا بیش از 300 عمل زیبایی انجام داده!
پسری که عمل زیبایی نکنه اسکله، تا حالا 200 میلیون خرج ابروم کردم، 150 میلیون خرج لبام شده
😶
استایلم فقط 400 میلیونه، 500 میلیون دادم که خط سینه بندازم. پسر باید به خودش برسه.
هزینه روزمره‌ام روزی 100-150 میلیونه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70983" target="_blank">📅 10:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70982">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⏺
🇮🇱
نخست‌وزیر نتانیاهو:
آیت‌الله‌ها می‌خواهند من در انتخابات شکست بخورم؛ حزب‌الله و حماس هم همین‌طور؛ و البته ترکیه نیز خواهان شکست من است. آن‌ها این را آشکارا بیان می‌کنند.
صادقانه از خود بپرسید: دشمنان اسرائیل می‌خواهند چه کسی در این انتخابات پیروز شود؟ به شما می‌گویم: آن‌ها نمی‌خواهند من پیروز شوم.
ما برای کل جهان آزاد می‌جنگیم. آن‌ها این را می‌دانند و به همین دلیل است که می‌خواهند ما شکست بخوریم.
ما اجازه نخواهیم داد آن‌ها پیروز شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70982" target="_blank">📅 09:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70981">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=BZa6Z54C8jo75hrnP_--Erc2Lc4q_5A5KRWEqb9LBlnLw3miT_1APnIuPQiD0Dkh6SNeVCEwI2RWTXYJSyRFkbbwGc9oseMuDqhOrEnMDpaVlm4WXzfJukXelJH5Hf-LpxTUa3skZBFpLwUe1CaBO4k1M0E7ZPFH6b7CnzFESTuarCxifWG1LnnHGKfR3s5Few0yB2v2d_uinvRsR5yswczRGbnBnCMLZ9nnxd7a_gptSMeC_Wa6VNoa44tuxyYDhuNnOFNlh7FwxJ6x-GK7CyfUzxvm8Rrptxu_TqnmYXR4bmt0qvfpfqKvAGsxcPZHvP6Zni0JVGgFxP5QQrugYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=BZa6Z54C8jo75hrnP_--Erc2Lc4q_5A5KRWEqb9LBlnLw3miT_1APnIuPQiD0Dkh6SNeVCEwI2RWTXYJSyRFkbbwGc9oseMuDqhOrEnMDpaVlm4WXzfJukXelJH5Hf-LpxTUa3skZBFpLwUe1CaBO4k1M0E7ZPFH6b7CnzFESTuarCxifWG1LnnHGKfR3s5Few0yB2v2d_uinvRsR5yswczRGbnBnCMLZ9nnxd7a_gptSMeC_Wa6VNoa44tuxyYDhuNnOFNlh7FwxJ6x-GK7CyfUzxvm8Rrptxu_TqnmYXR4bmt0qvfpfqKvAGsxcPZHvP6Zni0JVGgFxP5QQrugYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
〰️
سنتکام ویدیویی را از حملات به ایران منتشر کرد؛
سنت‌کام، فرماندهی مرکزی آمریکا اعلام کرد نیروهای آمریکایی در روز اول سپتامبر، موجی از حملات علیه اهداف نظامی ایران را با موفقیت به پایان رساندند.
بر اساس این بیانیه، مواضع پدافند هوایی، سامانه‌های راداری، تجهیزات و تأسیسات دریایی، زیرساخت‌های مرتبط با مین‌گذاری و مراکز ارتباطی سپاه پاسداران هدف قرار گرفتند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70981" target="_blank">📅 09:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70980">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70980" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/70980" target="_blank">📅 02:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70979">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozIPmTXB3YSnOwg7yenhG0_UcilTCyoSncsmNt0buJWk3PhCKFkzDeRxGma0FgI6mKV8JOLKs0R5kWyiCwcWn7eoBm6i_NyryBvj8_Js5ddPM_Xu4A6MlkBoK7GxbirHuWfQLLsOaPz9lraBv5nGHAe6q51BT88YEUaQhHRuj8ULButC4iAFwcokpFh8KPtKOSfBkxlcjFn9D2ZaCAYGkps3IP0yn4ynHX4QYioIE4_0FhvEiEo4I2IiHuk2aeCb73gBLW_6THZspltLr9EPuBLQMl__tZQYr3bRk1rXvb4su604K9szwgmEucoN481njuIFT4O13OPy0hBpcY-qNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
سایت جهانی
TrexBet
می‌برتت وسط
جنگ
بزرگ!
⚽️
استقلال
🆚
پرسپولیس
⚽️
اینجا فقط فوتبال نیست… دربی‌ـه!
۹۰ دقیقه جنگ، کری‌خونی و هیجان تا آخرین سوت!
🦖
🦖
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/70979" target="_blank">📅 02:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70978">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
منابع عربی:چندین انفجار در کویت و بحرین رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/70978" target="_blank">📅 01:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70977">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePXdUyG8a3McbbMjjGOYdVDO-qE4z2M7W7GttB5idOKTOzVDeMqEpVDr-xl7MQdtLjbpYVpKHWu5eNmGztXt_FzeRj716HSoEpVmxwmJR-8XFzCIuYX-7tjZxO0qyx6Ls7J2VZEiekgo3VbGfjr17b2szmxLxYMv8Y2r2BMLhCGFN0s11zbD_xK1K0YgkIAZ80HpCJyzjL1NVyVrjqCYIMKPc8h6srnMosPxc-1V8iBZSzbQuYKwUIXuSn25D8GICq4cgJlopv9jPoBApIfAglDYKCaVKNvSAoJfb5yEr8UnWgedSE41nYLrZ8HGl1ZL9MztDMonrfNh8bDm5zEtoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کویت اعلام کرد پدافند این کشور در حال مقابله با پهباد هاست.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/70977" target="_blank">📅 01:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70974">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⏺
🇯🇴
نیروهای مسلح اردن:
پدافند هوایی کشور ۱۳ موشک بالستیک را که وارد حریم هوایی پادشاهی شده بودند، رهگیری کرده است.
به گفته ارتش، ۱۰ موشک رهگیری و منهدم شدند و سه موشک دیگر در مناطقی دور از مراکز جمعیتی سقوط کردند.
در این حمله هیچ‌گونه تلفات جانی یا مجروحی گزارش نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/70974" target="_blank">📅 01:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70970">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OJhqLvfnTnB1QLgsIyEG77wev1kWOaivfIVN8b1zVqZMXEWkTgKH8HeeHjZF3b0af42HVlaceSjkLTKPCQoJZlT-HRTql6H7PGVKG6uaTaeBQdz8397j68uQbV8DIWBJ74MT05H7yePogKjhkQCFDb4xd3aYzOP3X2A6vgC5t4AJyygNf50wQ968yvEUUGSDWzyG4sUfW2dRQgRklb4aHQeH9HawLXKz_HynT_T1n8TMk9rB_7BNQUaEvgl-d1coHSYg4cp5EtzO4VvWclUkBYqR1tQ7NILtQ-vimV1eygN-Qg4I0DXw_trRi2FfCxlHlEPc9gkxQRtJQua6FYp69w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/703c34050b.mp4?token=ldr1dRY4dTIWTuD-P0lExkOgsAZ2ufXDBmX8jdbiJqtI7uAZ_u-61-umY_guql49hag6lHkhdbRTScqzYv0BSwi0UVtm4SOljLyu-f7zmpAgVZlQzML67UfMof4wQO1gvDSbVp1w82JGG65XE_bgVfkdbP6lrYeXNcvWIwPi5BL_vbzCrs99GO25vt2WCKZYstfsk6Wzxg8yQHAn1p_TzujfImsrsyqUlhx6vRkZeA2-SZ-JIa5uIY-E92qEeWzkc1lUahQSrh6xAIcmymzTetNteK3IHD1PyuKZ60uiDxOGcsVVQ6nyEOUgO1q_525qllLuZg0SMpEj6RSHOReb9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/703c34050b.mp4?token=ldr1dRY4dTIWTuD-P0lExkOgsAZ2ufXDBmX8jdbiJqtI7uAZ_u-61-umY_guql49hag6lHkhdbRTScqzYv0BSwi0UVtm4SOljLyu-f7zmpAgVZlQzML67UfMof4wQO1gvDSbVp1w82JGG65XE_bgVfkdbP6lrYeXNcvWIwPi5BL_vbzCrs99GO25vt2WCKZYstfsk6Wzxg8yQHAn1p_TzujfImsrsyqUlhx6vRkZeA2-SZ-JIa5uIY-E92qEeWzkc1lUahQSrh6xAIcmymzTetNteK3IHD1PyuKZ60uiDxOGcsVVQ6nyEOUgO1q_525qllLuZg0SMpEj6RSHOReb9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
امشب از نقاط مختلف کشور به سمت مواضع آمریکا موشک شلیک شده؛
🤩
تسنیم:
امشب یکی از گسترده‌ترین شلیک‌های موشکی ایران (به نسبت درگیری‌های اخیر) به سمت پایگاه‌ها و مناطق آمریکایی انجام شده است
ایران هشدار داده بود که حمله دشمن آمریکایی با پاسخ چند برابری مواجه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/70970" target="_blank">📅 00:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70969">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران: پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تبتین هدف موشک های بالستیک قرار گرفت. تعداد زیادی از نیروهای آمریکایی به درک واصل شدند
⏺
روابط عمومی سپاه پاسداران انقلاب اسلامی:
در پاسخ به این شرارت سبعانه، رزمندگان دلیر نیروی هوافضای سپاه در موج دوم عملیات تنبیه متجاوز "با رمز مقدس یا رسول الله (ص)" با حمله سنگین موشک های بالستیک به پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تیتین، واقع در سواحل خلیج عقبه، تعداد زیادی از نیروهای آمریکایی را به درک واصل کرده و چند تاسیسات مهم و بالگردهای هجومی دشمن را منهدم نمودند.
عملیات انتقامی نیروهای اسلام ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/70969" target="_blank">📅 00:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70966">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/appR07Li9hzKOKVhHsEw0VgJCat6dW7ChfRvud1dOAoQA1WvmEXMlTC1-FL_kSqdP8_qubi1aPGm7Pm2LavNmjIvVXqSu3s0LYYgSPJpKPburD-HWTA9acDv1CTZcUZh7a89nIAaSDprCj5eVMj7_TpkAeL4D31lF-J81IeoLE9Q96QHHDm4PJ7EvTRJCe0RYLzoRYOUjRtKSQLzIV2M0kQ6zZEs_MQ-iGVxNFOkWAqCjQH4x2qG6YBSTUcVU7bkttqum_B54W7Pr6-ZuFiycACMrRPPLHjVUXLRFQGsQKI1TKBPVTL_LL-rpQPDJSmnRIa_3-hTBWW_xCa6NwMiiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b67f6c5b37.mp4?token=k-cL0_ngksqvz9BoYq8P8DFNsny88hX9U7i2OMu96J-40B9Go4zkC6GkfA9L7ZADWS0sea0WMqw4p2NGJFcxvH_W56glvQTwCovfRfT4A7oDYHpgBpwe_ykgEWNC_N1dTvIGA5WfVoqz-nnUJGKIKiVbPuBxtF5LuVjEIWlj9oBTApehW5ta5rv7gLpRFc3uphBvPzyTZ12S3MksP0ILMzAum_ztTQkUw_44Oxclqn5uNVPrsPBgOXLJVrijE-mpX6gouoAg3sTnP-gZKo-yCDe2SUgShoIGNo0K7_4PyxrrMhf7qtdrxWDGGVfhJRgl3vc2aKIhyXUagfzrHu_BWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b67f6c5b37.mp4?token=k-cL0_ngksqvz9BoYq8P8DFNsny88hX9U7i2OMu96J-40B9Go4zkC6GkfA9L7ZADWS0sea0WMqw4p2NGJFcxvH_W56glvQTwCovfRfT4A7oDYHpgBpwe_ykgEWNC_N1dTvIGA5WfVoqz-nnUJGKIKiVbPuBxtF5LuVjEIWlj9oBTApehW5ta5rv7gLpRFc3uphBvPzyTZ12S3MksP0ILMzAum_ztTQkUw_44Oxclqn5uNVPrsPBgOXLJVrijE-mpX6gouoAg3sTnP-gZKo-yCDe2SUgShoIGNo0K7_4PyxrrMhf7qtdrxWDGGVfhJRgl3vc2aKIhyXUagfzrHu_BWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متاسفانه امشب یه خبر بد هم داریم، در طی حملات آمریکا تو بندر کوهستک حوالی سیریک، ترکش حملات می‌خوره تو یه مراسم عروسی و چهارنفر جونشون رو از دست می‌دن
🖤
#hjAly‌
@HutNewsPlus</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/70966" target="_blank">📅 00:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70965">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hz0Xk07p2l_IIjsqnb25Asn-GNkNl_unbeGDic8azARv3aXOUThoDQFUahLirJCb7Z71iGaruKyfHEPO0Nnz7Nej6SN8fn-7MXTCx35ZFu9s1o-KpEY26XUVt_oQA8jMHdTwNQCm0cK558bAaUF05oapbDRD5zOVmtp5rYRlwLYl1kLjarwv28Wm5XkE6orRas3ZSqH_9p9hQOTH5f9tEEKI2NQMemCbym4agtEx5C3lh4c8s7LeRAen-VSI-FRxQzE2lYBqkXD2iroD0N5CosBkM31vgOv2KSXBD3nviiub0en5u3ICfhVH2mfB87H8qLGfyjZ_vm0mevcgxitvhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ایالات متحده در حال حاضر هشدارهای امنیتی به‌روزرسانی‌شده‌ای را برای چندین کشور در خاورمیانه صادر می‌کند. این هشدارهای امنیتی برای بحرین، قطر و اسرائیل (اورشلیم) صادر شده‌اند.  @News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/70965" target="_blank">📅 00:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70962">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4e410d017.mp4?token=rVnKOk_hF_hWWD8_kJ4p2ccYodu9HnU1qYR7MPgzrp9upxknh4gEhR4QCERdrhV7x0w6NsnTmoXamt4PuAcUrQjiGCM6_ySr3nQFCMoYxfRMtCESxPFwzYben2kNkymb4X3bnmY1pdGBqwLDen97MwMJRrVY0OcImOixHUrQxzHQiOMvXFFE31MF1zPQS-AStEfFuEGr1PPxaiFU2_ZP8qF2Uihgxp1dxfPxLQJ69eOZvZX_gySLwhGjC4l5sme1qa6WdK2Kt74T8YUY6o0j0SFGuo9iM1l82YsuLb6oeLNw5HW0YRVU2r8Wv269p22AE_nXaoyLR0svLMPLIX2pbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4e410d017.mp4?token=rVnKOk_hF_hWWD8_kJ4p2ccYodu9HnU1qYR7MPgzrp9upxknh4gEhR4QCERdrhV7x0w6NsnTmoXamt4PuAcUrQjiGCM6_ySr3nQFCMoYxfRMtCESxPFwzYben2kNkymb4X3bnmY1pdGBqwLDen97MwMJRrVY0OcImOixHUrQxzHQiOMvXFFE31MF1zPQS-AStEfFuEGr1PPxaiFU2_ZP8qF2Uihgxp1dxfPxLQJ69eOZvZX_gySLwhGjC4l5sme1qa6WdK2Kt74T8YUY6o0j0SFGuo9iM1l82YsuLb6oeLNw5HW0YRVU2r8Wv269p22AE_nXaoyLR0svLMPLIX2pbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تو وکیل آباد مشهد یه ماشین به تجمعات زده ٢٠ نفر کشته و زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/70962" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70960">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4jncgIXf8I7oPeFCJsvSWFe-ISIHoN7SOeMMB6gW6FGnopscz8w1jM143h2xm8uk4e92i841zF7gUQoJ8xAXtYcREGlZp1GGQTIs-kpJCcRyECGV-AOgXUCcQsMEF193bD7DiBJ1PEXp5FMZEs_c0SJIGPeF4B1nhOSVsHZ0desNFehWKQMDuBLtXIMTDwFyzCom_BRKah-24-1f7L6XEU6XpsfpOG3U7E3GGCjQQ7bwuRvQ1brgXv_4Kl8LKUv-Yjoou1oIREh2MTQTq3nw4AgIMCQoSa2VDdx3EWlIJ549q0iECnB33Fpd5MknAUYfNu72CPErttgLYu3ixi38w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/791bfa967f.mp4?token=mWC3wQ2RAmfSP591slZfkbFkLDJ8WaQv_-Ld309Vbg9AuKWAgXoOQ04Sa1G8n9I0mpEnIPwu3MBJ2__m6LgQNmoTpFEulglK_IDOqXA_0NnjXQSot8O1BFksZpVDV68KB3cgzi7YbVWyiNhWG_CQJBhD3EFFnMxzICJfua7EnlIAFF6eoo_1ZkFacVVfChBh9M6XGYboxVmLvfVfStdklXBCG0L_kQ-SfFiPtEwnom5n5JF4y5dNy1DHtiCmjXadLwhizau8FFcaaYgB_J0x9b86McMouokc8CrAFzNZzTywI0XdpX9H4Be6cvPPDBaiJ-wRZ_7Yn5fq8i7oC7dS-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/791bfa967f.mp4?token=mWC3wQ2RAmfSP591slZfkbFkLDJ8WaQv_-Ld309Vbg9AuKWAgXoOQ04Sa1G8n9I0mpEnIPwu3MBJ2__m6LgQNmoTpFEulglK_IDOqXA_0NnjXQSot8O1BFksZpVDV68KB3cgzi7YbVWyiNhWG_CQJBhD3EFFnMxzICJfua7EnlIAFF6eoo_1ZkFacVVfChBh9M6XGYboxVmLvfVfStdklXBCG0L_kQ-SfFiPtEwnom5n5JF4y5dNy1DHtiCmjXadLwhizau8FFcaaYgB_J0x9b86McMouokc8CrAFzNZzTywI0XdpX9H4Be6cvPPDBaiJ-wRZ_7Yn5fq8i7oC7dS-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه حمله آمریکا به دکل سیریک که با پهپادهای انتحاری لوکاس(کپی شاهد) انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/70960" target="_blank">📅 23:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70959">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/541d79e411.mp4?token=KuXW3WVMlthGGhF_KZ2ROKllGyXixV8xJRlbCHFsIg1bkWCrEkJAG4ybmZxlfTVwoNOWXGvbmki1AJG1IICuwI8Prpoth9d8602obYYATwAQWcdz8_ckLMfKxuYxfmfWwScGKrIgtSn9ytTttrAVDS2nZr9OF3FOeV4PusSFPrqC22KMMqeGxksNi3Kd5yf55kOuoCkx1tjnRHV0gcS54giEz1wO5eo1ws84LNoz--nKSh4emj5EemJbgryK0cc9yYWpYW8aJcjDAmSWroETiSLdyNu0aheiatTEuFpltnLa9eydiuIsEOe0OPRkJBeq_kJIfGsnSDrfhLmu-2pdtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/541d79e411.mp4?token=KuXW3WVMlthGGhF_KZ2ROKllGyXixV8xJRlbCHFsIg1bkWCrEkJAG4ybmZxlfTVwoNOWXGvbmki1AJG1IICuwI8Prpoth9d8602obYYATwAQWcdz8_ckLMfKxuYxfmfWwScGKrIgtSn9ytTttrAVDS2nZr9OF3FOeV4PusSFPrqC22KMMqeGxksNi3Kd5yf55kOuoCkx1tjnRHV0gcS54giEz1wO5eo1ws84LNoz--nKSh4emj5EemJbgryK0cc9yYWpYW8aJcjDAmSWroETiSLdyNu0aheiatTEuFpltnLa9eydiuIsEOe0OPRkJBeq_kJIfGsnSDrfhLmu-2pdtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
اصابت موشک های سپاه در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/70959" target="_blank">📅 23:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70958">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
‼️
وضعیت دکل مخابراتی کوهستک سیریک که امشب بهش حمله شد</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/70958" target="_blank">📅 23:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70957">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خود ترامپ، هگزت و بسنت هم پشماشون از این حجم از کله‌خری سپاهیا ریخته
#hjAly‌</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/70957" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70956">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
از بیدگنه هم دوتا موشک شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/70956" target="_blank">📅 23:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70955">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
شلیک دور جدید موشک های سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/70955" target="_blank">📅 23:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70954">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">من فکر نمی‌کنم ترامپ قبل انتخابات دست به حمله‌ی گسترده‌ای بزنه، سنا تو تصویب بودجه برای جنگ نقش اصلی رو داره نباید بیفته دست دموکرات ها
#hjAly‌</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/70954" target="_blank">📅 23:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70953">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c95b26a1b.mp4?token=FZPifnvuDkGtdr-iMpSWAuPI2zwc_oeewLdXbjV7T_cEmXYU04GyagafinuPpAeUIKi0xBliR7ATkZjkuog_yMTqx9xE7U5fey9fDO01usE9FHTLSTkR54yiXths-1Nr8YQtXvF2GYohqgYdc0hBB0gEbw1XVNF_HDJ4pJWETeB8FcNBuGH-o-oIUvdexLWiMvNxZwTkx_NXVZUqu4kFXvhyAwYcJ0vVQ8onr2TBRBQcziyCG-DID8dzjjQ7PS1y6E94CIf8Ify__WwHSFpFWDrmJwTOBEvykaAFKSpWXC1rOwfBhsxKkz4rQUmH-uT7vvrTjBS86kcVIqIFgiC3wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c95b26a1b.mp4?token=FZPifnvuDkGtdr-iMpSWAuPI2zwc_oeewLdXbjV7T_cEmXYU04GyagafinuPpAeUIKi0xBliR7ATkZjkuog_yMTqx9xE7U5fey9fDO01usE9FHTLSTkR54yiXths-1Nr8YQtXvF2GYohqgYdc0hBB0gEbw1XVNF_HDJ4pJWETeB8FcNBuGH-o-oIUvdexLWiMvNxZwTkx_NXVZUqu4kFXvhyAwYcJ0vVQ8onr2TBRBQcziyCG-DID8dzjjQ7PS1y6E94CIf8Ify__WwHSFpFWDrmJwTOBEvykaAFKSpWXC1rOwfBhsxKkz4rQUmH-uT7vvrTjBS86kcVIqIFgiC3wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هم‌اکنون حملات موشکی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/70953" target="_blank">📅 22:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70952">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfcd58ff7e.mp4?token=FSpUg0Om1I-LBj_U8B08QuiXWFvtYGaKB1N3sXX7zSUCTRBLVjZPABlPbZdc5DYQMMrnt_hs6MlBWwrJLzWIU4b9H5vzKvE4NAeTgz1aROB8-YiDXN10EX2FHh-RCOUMS7Ii9QfEP3MNdim2zdko3mVhrFNQCZeNea4xsZVmhs-oQB721pvBsJIBZOqR4gYkV1-f5TxHyfX3sxLGDz2h3C1ZAgP61HzfYlQUmMZvn5CrD6kUy7XqNZdUJb_pbsuKQN0fxD-CSEnLOqRp0uzXsq5ogbdV_JHm3k3btv4X2i6tRXDEaNQDjxFzcHRN_z2mvzIn4WADDyO2APdfqc4RIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfcd58ff7e.mp4?token=FSpUg0Om1I-LBj_U8B08QuiXWFvtYGaKB1N3sXX7zSUCTRBLVjZPABlPbZdc5DYQMMrnt_hs6MlBWwrJLzWIU4b9H5vzKvE4NAeTgz1aROB8-YiDXN10EX2FHh-RCOUMS7Ii9QfEP3MNdim2zdko3mVhrFNQCZeNea4xsZVmhs-oQB721pvBsJIBZOqR4gYkV1-f5TxHyfX3sxLGDz2h3C1ZAgP61HzfYlQUmMZvn5CrD6kUy7XqNZdUJb_pbsuKQN0fxD-CSEnLOqRp0uzXsq5ogbdV_JHm3k3btv4X2i6tRXDEaNQDjxFzcHRN_z2mvzIn4WADDyO2APdfqc4RIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات موشکی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/70952" target="_blank">📅 22:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70951">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رسانه های حکومت: آمریکا یه مراسم عروسی تو سیریک رو زده و چن نفر کشته شدند
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/70951" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70950">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">همچنان هیچ ویدیویی از موشک های سپاه تو آسمون کشور های منطقه، منتشر نشده
#hjAly‌</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/70950" target="_blank">📅 22:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70949">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:  اگر ایران پاسخ دهد، انها از بین خواهند رفت  @News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/70949" target="_blank">📅 22:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70948">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اسپویل:
سپاه دوباره موشک می‌زنه و ترامپ هیچ گوهی نمی‌خوره
#hjAly‌</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/70948" target="_blank">📅 22:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70947">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=O5CVoFwY83vapZ_Phsedj5X3QpKkYY-MIHdwSqFRNGuu9lKdAlrMug0Ys-66lmPmvSb7BnUIkVNVgUSFm8AnQ3qDeVCz8W1ZbGqzk-OobT57-BjpxUUQJlBsKPCbBgtenJJiFnFYSumZNOvyS1L0TlQ41JClGhMMl313RwxgCHmI2i7AiM_OC7Xjv0-yb-2a0gPvWbh_yl7I6Llq_B26oZl4F1tvK4ZQCI3CC1JGymJH8WYIsDMWO6KP_2zpQBOsNt714SrRyc3bGtnz2ZJLMYcnf5VzOl096AUHJQIjLzN1GyFoyRXROdiWMxhIX_kBzseI-ygOLGSt_BHlGG952w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=O5CVoFwY83vapZ_Phsedj5X3QpKkYY-MIHdwSqFRNGuu9lKdAlrMug0Ys-66lmPmvSb7BnUIkVNVgUSFm8AnQ3qDeVCz8W1ZbGqzk-OobT57-BjpxUUQJlBsKPCbBgtenJJiFnFYSumZNOvyS1L0TlQ41JClGhMMl313RwxgCHmI2i7AiM_OC7Xjv0-yb-2a0gPvWbh_yl7I6Llq_B26oZl4F1tvK4ZQCI3CC1JGymJH8WYIsDMWO6KP_2zpQBOsNt714SrRyc3bGtnz2ZJLMYcnf5VzOl096AUHJQIjLzN1GyFoyRXROdiWMxhIX_kBzseI-ygOLGSt_BHlGG952w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پرتاب ناموفق موشک سپاه تو خمین
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/70947" target="_blank">📅 22:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70946">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
⭕️
🟥
رئیس جمهور ترامپ به خبرنگار فاکس‌نیوز می‌گوید که اگر ایران به حملات اخیر ایالات متحده پاسخ دهد، با پاسخ نظامی بسیار قوی‌تری روبرو خواهد شد و هشدار می‌دهد که اگر درگیری بیشتر تشدید شود، این کشور می‌تواند «کاملاً محو شود».  رئیس جمهور گفت که این حملات سیستم‌های…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/70946" target="_blank">📅 22:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70945">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1cb4c9444.mp4?token=LlWjopBwtpJndecddBCnnG5uILTR4nRJ_fCMV0wiCHc86QgXvHRspg6l5f5TeMomHlR0Dp3QIGGfCnjI3N-eYRzaPXXOUor-yQ3v9W8icuCXeWQQBGjLSsQgJMKIFmY7Ahkki5iuz2kPWnIbwMUCvQt2EuVHSsjO39OTyj6VdtRpMP4UodquH7tM-_siBZVa1VS8R4H1-qVTqbCy7_tlGq_OfTXqG2UuIURASGDHnoFAu4oNZwnKHDtVpRRzQ3XCvKqza_hvd30wg5BqEuUMbv7AClIVhjVfIGy8aQRDn_f-lSmmEiWNEKjxIckHLBSUMd_1VdAQdy-BCMpb87Hg5RW9LwBwTugtn_z1DLOR2x0ok8Vjw3kBL6DxsU4hi44mWgMpVL6wmlyV7DxUSRZ0tL6VV-pXwylkV93D9CMWCSJLPylfqKGZ3gyx616vbuJvezyE8DRGqjPAdEbmi1bzzxgVnYViT6-S746aCHKfR89gr0jx8ERfrm_Vb1HqcYoJ9XFTinGDZsJVfD9ZwMmahWmpAHcIuym2GUg5I1pFeKMbzWy18lYbW49O0_2qSc2hxhwVwR62DUjfupy5aw7AOqzShDqfpC3VkWoXqdWB4YqC1skJdRxLKuPA-MBQddU--OtlIe3oIq6lxrTJfzNaoE079MAnd8DWtfAehXl7NEM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1cb4c9444.mp4?token=LlWjopBwtpJndecddBCnnG5uILTR4nRJ_fCMV0wiCHc86QgXvHRspg6l5f5TeMomHlR0Dp3QIGGfCnjI3N-eYRzaPXXOUor-yQ3v9W8icuCXeWQQBGjLSsQgJMKIFmY7Ahkki5iuz2kPWnIbwMUCvQt2EuVHSsjO39OTyj6VdtRpMP4UodquH7tM-_siBZVa1VS8R4H1-qVTqbCy7_tlGq_OfTXqG2UuIURASGDHnoFAu4oNZwnKHDtVpRRzQ3XCvKqza_hvd30wg5BqEuUMbv7AClIVhjVfIGy8aQRDn_f-lSmmEiWNEKjxIckHLBSUMd_1VdAQdy-BCMpb87Hg5RW9LwBwTugtn_z1DLOR2x0ok8Vjw3kBL6DxsU4hi44mWgMpVL6wmlyV7DxUSRZ0tL6VV-pXwylkV93D9CMWCSJLPylfqKGZ3gyx616vbuJvezyE8DRGqjPAdEbmi1bzzxgVnYViT6-S746aCHKfR89gr0jx8ERfrm_Vb1HqcYoJ9XFTinGDZsJVfD9ZwMmahWmpAHcIuym2GUg5I1pFeKMbzWy18lYbW49O0_2qSc2hxhwVwR62DUjfupy5aw7AOqzShDqfpC3VkWoXqdWB4YqC1skJdRxLKuPA-MBQddU--OtlIe3oIq6lxrTJfzNaoE079MAnd8DWtfAehXl7NEM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🟥
رئیس جمهور ترامپ به خبرنگار فاکس‌نیوز می‌گوید که اگر ایران به حملات اخیر ایالات متحده پاسخ دهد، با پاسخ نظامی بسیار قوی‌تری روبرو خواهد شد و هشدار می‌دهد که اگر درگیری بیشتر تشدید شود، این کشور می‌تواند «کاملاً محو شود».
رئیس جمهور گفت که این حملات سیستم‌های راداری در جنوب غربی ایران در نزدیکی تنگه هرمز را که در حال بازسازی بودند، هدف قرار داده است و افزود که ناو هواپیمابر جورج واشنگتن کاملاً مجهز است تا در صورت نیاز به عملیات خود ادامه دهد.
ترامپ همچنین احتمال توافق جدید با ایران را رد کرد و گفت تلاش‌های دیپلماتیک قبلی شکست خورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/70945" target="_blank">📅 21:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70944">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری فارس از آغاز حملات موشکی سپاه به مواضع آمریکا در منطقه خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/70944" target="_blank">📅 21:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70943">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
⭕️
🇺🇸
پرزیدنت ترامپ:
"اگر آنها تلافی کنند، ضربه بسیار سخت‌تری خواهند خورد. و اگر دوباره این کار را انجام دهند، دیگر نخواهند بود."
"آنها متوقف نمی‌شوند. آنها دیوانه و احمق هستند."
"آنها سعی کردند رادار خود را بازسازی کنند زیرا نمی‌توانند چیزی ببینند. ما صبر کردیم تا تقریباً ساخته شود و سپس به آن ضربه زدیم."
"من فکر می‌کنم توافق با آنها ارزش کاغذی را که روی آن نوشته شده است، ندارد. ما به آنها فرصت‌های زیادی دادیم."
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/70943" target="_blank">📅 21:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70942">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ در گفتگو با فاکس‌نیوز:
اگر ایران به حملات آمریکا واکنش‌های مکرر نشان دهد، ممکن است «به‌عنوان یک کشور کاملاً نابود شود».
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70942" target="_blank">📅 21:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70941">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=fIfMEzKzTwIMVT_KIUI8gGXc04JrnMdleQ78up-Q93ZHkDD0Bai42ea889nF6OyPVLAdb4bh9LYRU_6dhlQW_RdHQlqVshw12uO9UyrCNyGXrhFj5GRQEhsNCIaxiovREih2D6tZpfaV1eJ8vSNBXs--0gp_h7VolyaDnzMi3f_Nwa3Ry2BkT5vF6iT0B-GLOrSmCmRHQzqXIcDMcWtJkp4GG8-hDPxYvYuwmPJNyXrfbYar01HerOmKwwuBzkJKD9U3DVIEQdIrewndQa0ONVZYBQzEiyUYiHzdhz8jtXuQ7dppneLaiR9D4QUuO1wztKNjAwW9LSwMyPvet_8Htw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=fIfMEzKzTwIMVT_KIUI8gGXc04JrnMdleQ78up-Q93ZHkDD0Bai42ea889nF6OyPVLAdb4bh9LYRU_6dhlQW_RdHQlqVshw12uO9UyrCNyGXrhFj5GRQEhsNCIaxiovREih2D6tZpfaV1eJ8vSNBXs--0gp_h7VolyaDnzMi3f_Nwa3Ry2BkT5vF6iT0B-GLOrSmCmRHQzqXIcDMcWtJkp4GG8-hDPxYvYuwmPJNyXrfbYar01HerOmKwwuBzkJKD9U3DVIEQdIrewndQa0ONVZYBQzEiyUYiHzdhz8jtXuQ7dppneLaiR9D4QUuO1wztKNjAwW9LSwMyPvet_8Htw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیویی دیگر از موشک سپاه که در خمین سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/70941" target="_blank">📅 21:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70940">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91af576da.mp4?token=hMr_EJIEKPH-Hvs_NdiJkrizUMPAS9KOLHWFoPb33Vf9q5wg96rdUJScNdgk9vlGAcLVf3Z6lVgVou1y0U0CgvpJo77QdT047Uab00T_-L1HqT4Eijm8bng7ybi43rN6-PZcL8Sf7QX7-yyu_hTchLk_m53-NhFkvwzRJP8wdeuvYGKcUgIv7Zpm5uNL8Msqo4QE86L158IvUje4nZln_eJhhffa5sGUEigQPK7WyYJqO2qA8e70CZ875dXNACeM7iGDMdwXnJnDGzwaF9-3kUyv5xZEbpmNcb6NbeY8NpYvmzpcv5VSuivN_dK3DTh086GQBgTOzSeS2Pug4wYixA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91af576da.mp4?token=hMr_EJIEKPH-Hvs_NdiJkrizUMPAS9KOLHWFoPb33Vf9q5wg96rdUJScNdgk9vlGAcLVf3Z6lVgVou1y0U0CgvpJo77QdT047Uab00T_-L1HqT4Eijm8bng7ybi43rN6-PZcL8Sf7QX7-yyu_hTchLk_m53-NhFkvwzRJP8wdeuvYGKcUgIv7Zpm5uNL8Msqo4QE86L158IvUje4nZln_eJhhffa5sGUEigQPK7WyYJqO2qA8e70CZ875dXNACeM7iGDMdwXnJnDGzwaF9-3kUyv5xZEbpmNcb6NbeY8NpYvmzpcv5VSuivN_dK3DTh086GQBgTOzSeS2Pug4wYixA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نقص فنی موشک بالستیک سپاه پاسداران در آسمان خمین
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70940" target="_blank">📅 21:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70939">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trjl1PCh5J2cR0HMsxa1X4fQlvxs8iBWSdQA1swCk5O-LsgW7WpYlBdK94fm0XRVLE3jnRYfFCpO-NFOJyOAB0Wnul6kktjBbdOvqwx06Y4C14nf2xfWnyONPJc6YEMKz_wBUFVHVlGhwT50ND5HDZ9gTurTZeBDy4ZR-Dw-7KXnIdMOyzuMeXVznoUIE8B3AdXUgR24P_Yzo838g0MNL1XW3Z34vLPYOWpHni8UDpGm-5k_lD0206G0j7aUqJEn99bYiEDgXuWvJ63j7ETg5NibFFBAT7CS-ikSrQMb-vVsFunzbGMopvXM0OKKLxNNqggx3Cml9ZELUtlyXLYGCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ستاد کل نیروهای مسلح: هزینه سنگینی بر دشمن آمریکایی تحمیل خواهیم کرد
🔴
ستاد کل نیروهای مسلح و قرارگاه مرکزی خاتم‌الانبیا:
در پاسخ به تجاوز هوایی ارتش آمریکا به نقاطی در سیستان و بلوچستان و هرمزگان، نیروهای مسلح جمهوری اسلامی ایران ضربات کوبنده و شکننده ای را به دشمن زبون و شرور آمریکایی وارد خواهند نمود.
ارتش تروریست آمریکا هر چقدر اصرار بر شرارت در منطقه داشته باشد باید خسارات بیشتر و سنگین تری را تحمل نماید.
بارها اعلام نموده ایم و اراده کرده ایم تحت هیچ شرایطی از حقوق ملت قهرمان ایران کوتاه نخواهیم آمد و هزینه های سنگینی را بر دشمن آمریکایی تحمیل خواهیم نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70939" target="_blank">📅 21:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70938">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
گزارش انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70938" target="_blank">📅 21:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70937">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgU7zRXZDCtB8ai0V1H01OmoSGCxfNxLyMUnZ0JbIvEk-d57X9zKU4B5qfYyZR9tJSJZmLwrYjCvmkcqZG19vy7wJ2tFrEpbXyMa33jxp28e6iB5Az9vm0ycM4SY8VuFMYeWBlw21bvvyqK1c54csYuvsJBpymB20axmG386G3GEGvSqfv3YnEn0Mj3IrozoxNftGkavnX6LW0XvMjAaw8yaRX5Ey2YyXCDJh3a5UD9iLSIVRtlBejMgsxjrpYi4zTYFr00B-gp6FRKF8sAXnvOhW63dttbCtvCrECC6qEPgr1VRPEWn4WzRRyXdn1nxEyTyL2pdTO54hzezuqx9dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:ایالات متحده همین حالا در حال هدف قرار دادن مواضع ایران در نزدیکی تنگه هرمز است.
🔴
این حملات گسترده و سهمگین هستند و در واکنش به دو اقدام صورت می‌گیرد:
نخست، تلاش نافرجام ایرانی‌ها برای کارگذاری مین‌های دریایی در تنگه‌ای که در حال حاضر فاقد هرگونه مین است (مین‌ها کاملاً پاکسازی یا منهدم شده‌اند!)؛
و دوم، شلیک هشت موشک از سوی ایران به سمت پایگاه نظامی ما در اردن که همگی با موفقیت سرنگون شدند.
اگر ایرانِ شکست‌خورده بخواهد به این حمله کاملاً موجه پاسخ دهد، بار دیگر با ضرباتی بسیار شدیدتر و سنگین‌تر مواجه خواهد شد؛
🔴
اما آن حمله، بزرگترینِ حملات نخواهد بود، چرا که حمله اصلی در کمین است و پس از پایان آن، چیز زیادی از جمهوری اسلامی ایران باقی نخواهد ماند!
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/70937" target="_blank">📅 21:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70936">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⏺
معاون امنیتی و انتظامی استاندار سیستان و بلوچستان از اصابت چهار پرتابه در شهرستان‌های چابهار و کنارک خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70936" target="_blank">📅 20:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70935">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRBJ81OWXvG6KzDJv9UJJRVgJisKzjLxeHy4koDv7s8uWZSGe3SXSfGaXrAXlajIlpXlR7ComwBorJ6lQAGdDbPi9zumIAcSXXhAAqJ1eVsz5TsD9pgfOK-UnLB2bVaJ9qYY2-bjMyeUnjFc8MtEuu77MBxDw3f1R7ZeeaakcFPrY-Zaxwaiws8L7hR7vXNjo6aCHNHM3BGPlVo_LLP1NtPbQ9P1u-Hxn2gXnaNS99RPjZdiws8EjPG3vMcxhiDq40GpPHyjdIx27mbX5677gzUHy9e459tCLjHyM7BfeLOL2ut9LzwIPoqNfMrrjDH9-jPKIaW5a4Xa63uclb7iow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ایالات متحده در حال حاضر هشدارهای امنیتی به‌روزرسانی‌شده‌ای را برای چندین کشور در خاورمیانه صادر می‌کند. این هشدارهای امنیتی برای بحرین، قطر و اسرائیل (اورشلیم) صادر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70935" target="_blank">📅 20:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70934">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
تا اینجا در چابهار، جزیره قشم، بندرعباس، کنارک، جزیره لارَک و سیریک انفجار گزارش شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/70934" target="_blank">📅 20:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70933">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFlCe4c9l7gf4tgnr_LpaIwRZtg2o8_1dthXKUqf_4KvzNTCeo93-qeYRMlcemF2Fvj3uHfoCQQd1wey-b0_TpNPO00k4NqWgBD-JPK2xN37SxBS52XxVOahd-HMrsCiVFO5I4aHWHYtdVeAw7nYk2qUjgFtAcp2H4Tk3GFSaVartl5Y3HjsEjjXD5QBXapBhnVIXIH5Sbi0U_CaJgcYx09lhFVDH5Il6jEXQqc-Ohd0MKY4iGhjJ2WDKY1XxvVBQ4EAYZTNqFa_0axiAsX_slymaNIdgItTaFDomJFLujaRhWJaA_08At011rH-PliFPMVUCW_1z33NMhGecs4oNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
〰️
#فوری
؛سنت‌کام:
امروز ساعت ۱۲ ظهر به وقت شرقی، نیروهای ایالات متحده حملات خود را به اهداف سپاه پاسداران انقلاب اسلامی در ایران آغاز کردند. این حملات در پی تلاش‌های اخیر سپاه پاسداران برای حمله به کشتی‌های تجاری در تنگه هرمز و همچنین نیروهای نظامی آمریکایی مستقر در منطقه صورت می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70933" target="_blank">📅 20:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70932">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تا این لحظه سنتکام هیچ بیانیه‌ای صادر نکرده  @News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70932" target="_blank">📅 19:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70931">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s4CiccnlZ219KH7M-KY9Idn0QYc_w7dX6HC67ZSAs_x3skZq9oaAihy34JhEYo5wOM9UTE7c316udj0i58-HUPqHv36GxrX8Imyj0-Hh50aQJSBqIqU8yRGyDqIjTOa_7rvwnChxx3JSKUgKaHs_7PGbBbpRbHjA1yXqdzOjr1z3CJJwQzetTDLSVkgiNmETTf0hAblPyTxOADbrrmodMN9clnNp8T1H38eHLZUs0uSBP0jIc8kyC2a4YcXvfyhHbmMtHiUX4dW6AxjCw-tZE6O4SHapuWNuE91VdFCiMXoBxcIbY-_R3dUFQ073vZY_jXr6JqNqBdxGH1mASFZiSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا این لحظه سنتکام هیچ بیانیه‌ای صادر نکرده
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70931" target="_blank">📅 19:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70930">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
گزارشات از صدای سه انفجار  در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70930" target="_blank">📅 19:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70929">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c2d67d465.mp4?token=trTdJTLfoUmmRbAxWWc7SXDfMLcAMI6dH9B-R0ANu_1iR8Iy-O63t4k17F10rp48BlXwBZFqL1Jvep5WNaQLWud8YaCuHM4-kBCurZ1Sq6ahtSdRnoGBoUxEuHz6iOb2UeMCVjreb5ovBMf4LFlEr-AfDmGNDqf9FXDfkQgL5mRsKByYYmEGOJsriSHpONvLTa9zezWVeq09FPZAfFRqPh0B1z0d2fmxjDPq7jHjUi3iCkUQZoLbjIfTHSCveQmNGTVrN9KsTnzZYjgfUmzBke_vbD0jO3OuKi-fVobz2zxmmKms3FSAdWH0DlujlK_iG4Qqzx4P8WGaDuXMtT0HWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c2d67d465.mp4?token=trTdJTLfoUmmRbAxWWc7SXDfMLcAMI6dH9B-R0ANu_1iR8Iy-O63t4k17F10rp48BlXwBZFqL1Jvep5WNaQLWud8YaCuHM4-kBCurZ1Sq6ahtSdRnoGBoUxEuHz6iOb2UeMCVjreb5ovBMf4LFlEr-AfDmGNDqf9FXDfkQgL5mRsKByYYmEGOJsriSHpONvLTa9zezWVeq09FPZAfFRqPh0B1z0d2fmxjDPq7jHjUi3iCkUQZoLbjIfTHSCveQmNGTVrN9KsTnzZYjgfUmzBke_vbD0jO3OuKi-fVobz2zxmmKms3FSAdWH0DlujlK_iG4Qqzx4P8WGaDuXMtT0HWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇳
دیروز تو دیدار پزشکیان و نخست وزیر هند، مسئولین به پزشکیان میگن پروتکل رو رعایت کن؛
🇮🇷
پزشکیان میگه :
بابا ول کن این پروتلکو
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70929" target="_blank">📅 19:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70928">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4f6e57831.mp4?token=f0OT0XkkxcfKi5JyXyPZKXX2JQqfNj6seBysOZOTf2e0hwo5C6YgvLenipQ65GTGulWFD_NDdFUgK6h4Oi4Ephh94flRKJyEJY18Fbp6lD4Z7PfK8tmYYh6VReP7JWHI83K8YTB6vGGphqxtvaIl3c77NTwSr9prvl8n7saWG72u5HL24-GoV9t01lxW9gupx6a0rFjB9i-bUqojAzHrcyUEfa02_bR4psBxdQJj2k044YtuTNRVHFU__A_dw-ChSK1S46PW28Vhl8zSOecDl5Hc34bhp6jGuOGAINWmCMZJAyXVS1vj8p9x7Hd2f1Hjiwmmcvu6Gnc1ddLwAYc1T1iwh7g7fdKG2ut7Brp92rOeik2xIChUGAORz7hCg38o96VczMYT_e21fsVK-kTSt8NiBASkpllJWrRbylix1DvXUVgGjJTWE8qxqCfBwROzAd-b7Pt5zuBmc0gxjdsFTTra9gIpCttzbxQSM5w7AkiybeYMT7UFQByGULFmiQaqjkwo75MfLKvzuySZM-q-pTEGs_kRdehdXZBaWjSFQS95zlZutZU8Uk9htXVr1xkKoaGz3f9NPAhpmtv8-T8lSv1h0yIv_XG6JhDDB0v3TvCGgVPdOdgGY8mxO29axnjNQ7E1KMxFOrT3qzPEtPxj6gyi8sV34mNrXSzKE93MRmk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4f6e57831.mp4?token=f0OT0XkkxcfKi5JyXyPZKXX2JQqfNj6seBysOZOTf2e0hwo5C6YgvLenipQ65GTGulWFD_NDdFUgK6h4Oi4Ephh94flRKJyEJY18Fbp6lD4Z7PfK8tmYYh6VReP7JWHI83K8YTB6vGGphqxtvaIl3c77NTwSr9prvl8n7saWG72u5HL24-GoV9t01lxW9gupx6a0rFjB9i-bUqojAzHrcyUEfa02_bR4psBxdQJj2k044YtuTNRVHFU__A_dw-ChSK1S46PW28Vhl8zSOecDl5Hc34bhp6jGuOGAINWmCMZJAyXVS1vj8p9x7Hd2f1Hjiwmmcvu6Gnc1ddLwAYc1T1iwh7g7fdKG2ut7Brp92rOeik2xIChUGAORz7hCg38o96VczMYT_e21fsVK-kTSt8NiBASkpllJWrRbylix1DvXUVgGjJTWE8qxqCfBwROzAd-b7Pt5zuBmc0gxjdsFTTra9gIpCttzbxQSM5w7AkiybeYMT7UFQByGULFmiQaqjkwo75MfLKvzuySZM-q-pTEGs_kRdehdXZBaWjSFQS95zlZutZU8Uk9htXVr1xkKoaGz3f9NPAhpmtv8-T8lSv1h0yIv_XG6JhDDB0v3TvCGgVPdOdgGY8mxO29axnjNQ7E1KMxFOrT3qzPEtPxj6gyi8sV34mNrXSzKE93MRmk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
بسنت درباره ایران:
ما داریم سرِ مارِ ایران را زیر خاک می‌کنیم. این مار هنوز نمی‌داند که مرده است، اما وقتی خورشید غروب کند، دیگر تکان نخواهد خورد.
کارِ رژیم ایران تمام است.
و آن‌ها هم متوجه این موضوع خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70928" target="_blank">📅 18:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70927">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f392bbd4a.mp4?token=RF48D6BdQ_z0fardn6a-vQUsG8tFXtKOWit8Jh9mKA7czx_A8OhcD___0FP5d1w2hrzeA2H0xyMXrJIuuRqHigI6Ul31TvIvi-D-IDNSuHrBC_oRKl6lOVLVhgXeFo9IQ7-Gsjv652Zdcp-hNGeRUcnvnob6k-4SlbWdw1a3Z2MKAL6zLhmgzRKk89Q36bpn0TPF2EtmxuggPbDFQ0UorTOiu-qXL50mKCviF2HB4nRvsLNnV29i1_88gDQVNI1AqQT4T6dlS7WBNd1NOEdUV93AY_wTiuHEiPyMeLne4MPO0gE7AnBogjuUHCBE8tliElQuCny20V7FWn2auZdxyHyzdE8HHVZzQM7Ith_9D38pdixvCicAerjkBQhympEk9cr_9GlHKrJ-kqvJeOezjEZNiWuX4xXqMKWja-No2djW7YYkQs_vw2nZT_jeU9mumTTeSpDv_yKEJupDLp-7NASEnnOxfrDdVYA8J4ikrN7FoqCGcBP8rApEfRwTOnknZ-SqFBgjuoG7CRExMdIlIU4A7fETlJv3FfJILYvUBO9dy7909IFrWvIXkSFSMDGUlxu4GuZfunoCqpeWtM5rgwcZtTdO-uDhERIWrlPzC3vGeMEo0FQfudwWlr78HCMM5awA8KphfD_3vQF8gltb0qZBq-5M2EV1OWeuE30uNqo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f392bbd4a.mp4?token=RF48D6BdQ_z0fardn6a-vQUsG8tFXtKOWit8Jh9mKA7czx_A8OhcD___0FP5d1w2hrzeA2H0xyMXrJIuuRqHigI6Ul31TvIvi-D-IDNSuHrBC_oRKl6lOVLVhgXeFo9IQ7-Gsjv652Zdcp-hNGeRUcnvnob6k-4SlbWdw1a3Z2MKAL6zLhmgzRKk89Q36bpn0TPF2EtmxuggPbDFQ0UorTOiu-qXL50mKCviF2HB4nRvsLNnV29i1_88gDQVNI1AqQT4T6dlS7WBNd1NOEdUV93AY_wTiuHEiPyMeLne4MPO0gE7AnBogjuUHCBE8tliElQuCny20V7FWn2auZdxyHyzdE8HHVZzQM7Ith_9D38pdixvCicAerjkBQhympEk9cr_9GlHKrJ-kqvJeOezjEZNiWuX4xXqMKWja-No2djW7YYkQs_vw2nZT_jeU9mumTTeSpDv_yKEJupDLp-7NASEnnOxfrDdVYA8J4ikrN7FoqCGcBP8rApEfRwTOnknZ-SqFBgjuoG7CRExMdIlIU4A7fETlJv3FfJILYvUBO9dy7909IFrWvIXkSFSMDGUlxu4GuZfunoCqpeWtM5rgwcZtTdO-uDhERIWrlPzC3vGeMEo0FQfudwWlr78HCMM5awA8KphfD_3vQF8gltb0qZBq-5M2EV1OWeuE30uNqo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
بسنت درباره ایران:
ترامپ می‌خواهد یک‌بار برای همیشه به این وضعیت پایان دهد.
مردم ایران ملتی بزرگ هستند و این فرصت را دارند که به نظام [بین‌الملل] بازگردند؛ آن‌ها تحت سرکوب قرار دارند.
نمی‌توان انتظار داشت که گروهی کوچک برای همیشه قدرت را در دست داشته باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70927" target="_blank">📅 18:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70926">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0VAFGI1EuucapShqytynBuvbZtgWNzIJyrwgfT4XW7YkxjvXKRM5UuAWnDNcIjup9i3Fi_LHeIyYGWaEXkG5Dlr7-Ezytz8h5FKB6L5X5ISZdtbTYQ-SIR2wB9tMj70i8ZzvVjjr4SMNms4PYqxZxSfK71-fguVqpQTs7L6EgdEB35DFP61wCYK2trS6B-RFJ_4U-OTFq8JJRmLM1oGF1neZ0M6ZRpiaOGsfz12LpaJZ3O4pBO_kmslDAUAwXKSJhhQBj8AH6Z6jajx9KQw-RqXpAiT4YxFogpMisvUn-VTj3VQ5unCd7wagD7ox59HR6iRUHyB-8O7h8k6Fp6dGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
سنتکام:
از زمان تشدید محاصره بنادر ایران، نیروهای آمریکایی مسیر ۸۴ کشتی تجاری را تغییر داده، ۳ کشتی را از کار انداخته و برای اطمینان از رعایت مقررات، وارد ۲ کشتی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/70926" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70925">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70925" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/70925" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

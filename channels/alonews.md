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
<img src="https://cdn4.telesco.pe/file/vU0cYvg2ehFajBZI3vdfpz2vtLz407iAWJP-prkxAaFPuRfcmOjf3ZasNAdWKUsIZWylwET1i0NCFNiuPS1n29QNGUHYFKLq4yoXdz-c5JP1uFlwVGqwc0W-uFJgYP7X4U6gZe2ZHqWVqiPhQkUUVtxHN3RQ5ph6mVWxhtOLgpvBACSq2FgFv0K86-SmvEB0L8RuLkbE0Sw058dkdUntaZY03n6AfJMk5JLlk_RA96R4s4-tx-d3cX2XccIs_kUYpEWfId3pn6DV8BgXKqank0ulKemmOJ-ArEwYwyWO5CjufAW-5YKzv7I9GsTXIQoZrye-805k0NYhfwHrUyEI4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 913K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 15:26:15</div>
<hr>

<div class="tg-post" id="msg-147560">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vsax67SpOWYgVQTb1eyy9CtQ661fYhRGlNP-BPMo9k-jZPTPT-sX6MlH_yA07iif_IuholY7T1MiAtWgnsF7uDlSqaZSYBtyaH7AmWij_NjsNNU4SeptZ2WcH1dIjJ1pkphy_U7cgHYMnzWcaqpB61gFX31CDpD5u9Ms_ArUxPIzNsF3DjfJizMWBkZa4P27p9R0_fmFoVBrT3Yba8GBbCpT2b-nXetBNSLPpJGp6ygPIk5G44AMWScd9QW7z9WHrxBD1Mez-5GWgDg-dhbUKbbr3B6VZVPZYe-U26BxBiZAYC_CVl8uazgL1KvkVqnxqtOkuv3ve5ESbRaU2m_Eww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس نظرسنجی‌های رویترز/ایپسوس، میزان محبوبیت رئیس‌جمهور ترامپ اندکی افزایش یافته و به 35 درصد رسیده است، در حالی که این رقم در اواخر ماه آگوست به پایین‌ترین حد خود، یعنی 33 درصد، رسیده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/alonews/147560" target="_blank">📅 15:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147559">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
هاکان فیدان، وزیر امور خارجه ترکیه:
امنیت، ثبات و رونق ایران، به طور طبیعی و مستقیم بر منطقه ما تأثیر می‌گذارد. از این رو، ما خواهان این هستیم که این درگیری موجود در اسرع وقت از طریق راه‌های دیپلماتیک حل و فصل شود.
🔴
افزایش حملات متقابل در دوره اخیر، به طور جدی تلاش‌های صلح را تضعیف می‌کند. این اقدامات که باعث افزایش تنش در منطقه می‌شوند، باید فوراً متوقف شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/147559" target="_blank">📅 15:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147558">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17a03d9b86.mp4?token=ETd-EZnh31REN_btMEcZOXAnkms0WUZmZpvLE7HKAN0r3f5nzLlphpdBXjnEJMdM1MrswHZtD7_-Ah0etatkobVh6JW1W2_dJIzgh6qx0YeVIGHOHHJHIQfc9KHcQ32rPbevxk0DPDH6sMTYsaS2sMnP7FmQkheL2tyFFmXfPCz40iUdw4Q6EX3uCEJJtmBTikpQ8tSb4LyMQiAYMqOqai6OJ8HxMwxOX15fJvSglT47fpEQLuKnk6TyzfPLNzdLytfx6v_J9fzboj7x9sOC5ShJm-dqUVj77V9YDXLq6rRApzd9WgVnzX3eAxgWz0GSWJr6j6HP3Hyl7KxNyM9jQUu3PHA0Wa2OqItbFOgF8ihS2BZN7AcSyIOuX26I6AKUwud3Kvy7gBFqmF24yr1klxmXYdHINnnofCu6oePJdPiseSLeBVbhletrT87vQvIPJB-1m2Yn2TQWTgAa5Govd_v5tZYpatfztO3a_QcEfAYsHluJk9Kt1JLs7_fZtUJ4ALxmIx3FMoe6rUEodzK5P8VouerAy-BAkAEgXjQft61bKopo3jTDK5jRX1bEZneLBgn-aKxnnRuFkPtmf6PvYr3ye2rxSTaoEUxY4H2ik3rIhzXM5KIw7GKxZ5M_gll3wWJtTbop7DTrzdxoOiNPBH4PQgJ-564p80tuR-ufEj4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17a03d9b86.mp4?token=ETd-EZnh31REN_btMEcZOXAnkms0WUZmZpvLE7HKAN0r3f5nzLlphpdBXjnEJMdM1MrswHZtD7_-Ah0etatkobVh6JW1W2_dJIzgh6qx0YeVIGHOHHJHIQfc9KHcQ32rPbevxk0DPDH6sMTYsaS2sMnP7FmQkheL2tyFFmXfPCz40iUdw4Q6EX3uCEJJtmBTikpQ8tSb4LyMQiAYMqOqai6OJ8HxMwxOX15fJvSglT47fpEQLuKnk6TyzfPLNzdLytfx6v_J9fzboj7x9sOC5ShJm-dqUVj77V9YDXLq6rRApzd9WgVnzX3eAxgWz0GSWJr6j6HP3Hyl7KxNyM9jQUu3PHA0Wa2OqItbFOgF8ihS2BZN7AcSyIOuX26I6AKUwud3Kvy7gBFqmF24yr1klxmXYdHINnnofCu6oePJdPiseSLeBVbhletrT87vQvIPJB-1m2Yn2TQWTgAa5Govd_v5tZYpatfztO3a_QcEfAYsHluJk9Kt1JLs7_fZtUJ4ALxmIx3FMoe6rUEodzK5P8VouerAy-BAkAEgXjQft61bKopo3jTDK5jRX1bEZneLBgn-aKxnnRuFkPtmf6PvYr3ye2rxSTaoEUxY4H2ik3rIhzXM5KIw7GKxZ5M_gll3wWJtTbop7DTrzdxoOiNPBH4PQgJ-564p80tuR-ufEj4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: عموی من احتمالاً، به طور خلاصه، یکی از بهترین‌ها در تمام دوران بود. او ۴۱ یا ۴۲ سال در دانشگاه MIT تدریس می‌کرد و به عنوان یکی از باهوش‌ترین افراد شناخته می‌شد.
🔴
بنابراین، من کمی از نظر ژنتیکی قوی هستم، اگر به نظریه منابع اعتقاد داشته باشید. من به آن اعتقاد دارم. من از نظر ژنتیکی برتری دارم. من در مورد هوش مصنوعی (AI) اطلاعاتی دارم.
🔴
ربات‌ها جهان را تصرف نخواهند کرد. هوش مصنوعی نیز بقیه جهان را تصرف نخواهد کرد. کل این موضوع یک فریب است
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/147558" target="_blank">📅 14:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147557">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8ae5f579.mp4?token=mLVzkp1GsXJyQumudsXDzPRcJIbjIDilGUWzdu6O-2NPuUStYbuVrg7aqZa8fOAR4ahUZWA-9FxZVvos8UrZa3xcC1iA-k5ZjQobADyXEVwa8jmzl7dJbr9VKq24rVRr0SLyNC9jUWpQy-_Jn8nvZN8cGFO0mJgNd5Vyyo2Bmt6wLi15EsoI9iDgQlPddwxDVuaGE9S2MUwLcE63Y6mYwyPea4eBIQJRZSjW_nxwKMsbZ4PtSSpr99Xfx9lLbqz-9ZvnM3Q4j0_bMCpooxx6tqGJwFuqw8TBLjlU34UVUyTZH8d6HpD7TQ2JGjMrqvVAIsDZNMgNTtBP2KS7-ZukuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8ae5f579.mp4?token=mLVzkp1GsXJyQumudsXDzPRcJIbjIDilGUWzdu6O-2NPuUStYbuVrg7aqZa8fOAR4ahUZWA-9FxZVvos8UrZa3xcC1iA-k5ZjQobADyXEVwa8jmzl7dJbr9VKq24rVRr0SLyNC9jUWpQy-_Jn8nvZN8cGFO0mJgNd5Vyyo2Bmt6wLi15EsoI9iDgQlPddwxDVuaGE9S2MUwLcE63Y6mYwyPea4eBIQJRZSjW_nxwKMsbZ4PtSSpr99Xfx9lLbqz-9ZvnM3Q4j0_bMCpooxx6tqGJwFuqw8TBLjlU34UVUyTZH8d6HpD7TQ2JGjMrqvVAIsDZNMgNTtBP2KS7-ZukuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره هوش مصنوعی:
ربات‌ها قرار نیست جهان را تصرف کنند. این اتفاق نخواهد افتاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/147557" target="_blank">📅 14:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147556">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
عمان: بحران تنگه هرمز به زودی به پایان خواهد رسید
🔴
حمد النعمانی مدیرعامل شرکت گاز طبیعی مایع عمان (Oman LNG)، امروز سه شنبه گفت که بحران مربوط به تنگه هرمز به زودی به پایان خواهد رسید.
🔴
وی در کنفرانس بانکوک گفت: بحران تنگه هرمز طرح‌‎های درازمدت این شرکت را تغییر خواهند داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/147556" target="_blank">📅 14:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147555">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
آمریکا به دنبال توقیف ۶۱ میلیون دلار از دارایی‌های نفتی ایران
🔴
گزارش‌ها حاکی است آمریکا برای توقیف حدود ۶۱ میلیون دلار از درآمدهای نفتی ایران که به شکل دارایی‌های رمزارزی درآمده، اقدام کرده است.
🔴
در این پرونده نام دو شرکت چینی و صرافی رمزارزی بایننس نیز مطرح شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/147555" target="_blank">📅 14:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147554">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
کرملین: روسیه معتقد است فضا باید عاری از تسلیحات باقی بماند و امیدوار است از طرح خلع سلاح کامل فضا حمایت گسترده بین‌المللی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/147554" target="_blank">📅 14:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147553">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
وزیر خارجه طالبان: هم جهان اسلام و هم غرب از ما می‌خواهند مدارس دخترانه را بازگشایی کنیم، اما نباید با نگاه غربی به ما نگریسته شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/147553" target="_blank">📅 14:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147552">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
طلای جهانی در آستانه تصمیم فدرال رزرو درباره نرخ بهره، با افت جزئی به ۴۳۰۲ دلار در هر اونس رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/147552" target="_blank">📅 14:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147551">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
رسانه عبری والا به نقل از منابع امنیتی: تماس‌هایی میان عربستان و اسرائیل با میانجی‌گری فرمانده سنتکام انجام شده تا از طریق ارائه اطلاعات، به سعودی‌ها در دفاع از خود در برابر انصارالله کمک کنند
🔴
نگرانی‌هایی در مورد اینکه آمریکا با ایران و حوثی های یمن به تفاهم برسد و سپس عربستان و سایر کشور‌های منطقه را با مشکلات حل نشده خود تنها بگذارد، وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/147551" target="_blank">📅 14:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147550">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
کرملین: پیشنهاد ترامپ برای برقراری آتش‌بس در حملات به تأسیسات انرژی میان روسیه و اوکراین، «ایده خوبی» است
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/147550" target="_blank">📅 14:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147549">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">💢
رو کدوم سرمایه گذاری میکنید؟
💵
دلار
.
🔴
طلا.
🏠
ملک
💸
بیت کوین</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/147549" target="_blank">📅 14:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147548">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tX4riMRkXXrbLGuv-r4DdiBztnmzmGBaTG2i5K5pXPdZP7YjSMEhTHxLOZq9q-EhE-z1PaVuw5UhUZtosCv0bXGtk0Vp3PFMWtJSBYkDOOpXcwUCgld_fkj2Nh6NPIj4lfbAXtCNWuYC48FV5SNDRBzL8-wnbhSfdxzmEoAPQXFkSDbTgfkOQd7Mjz_5_-EJc1VQUtnpm-baZbPmncKZFzfEF80tRBR-4qkmtz9_YiGv7kPz2JxaH7sULTTn-muZ-IyDwvgaYbqF7KlVmrpUu1sRdXx3UBKbsbHkT64xucXsZI9SmZXE0ePl2tWwXoIMggXAkCzQXRiJjOX367OddQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کرایه روزانه یک ابرنفتکش از خلیج فارس به چین برای نخستین بار در تاریخ به یک میلیون دلار رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/147548" target="_blank">📅 14:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147547">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وزارت خارجه قطر: دولت قطر با جدیت و همکاری با شرکای منطقه‌ای و بین‌المللی خود برای دستیابی به توافق درباره تنگه هرمز تلاش می‌کند.
🔴
دولت قطر با شرکای خود برای پیشبرد گفت‌وگو درباره امنیت کشتیرانی در تنگه هرمز همکاری می‌کند.
🔴
دولت قطر از دستیابی به توافق درباره تنگه هرمز و توافق طرف‌های ذی‌ربط بر سر یک راه‌حل حمایت می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/147547" target="_blank">📅 13:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147546">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
عمان: ۲۳ خدمه نفتکش «الگایا» نجات یافتند؛ جست‌وجو برای ۲ نفر ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/147546" target="_blank">📅 13:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147545">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
چمران شورا تهران: ما تو جنگ میریم رو پشت بام، ولی نتانیاهو میره زیرزمین
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/147545" target="_blank">📅 13:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147544">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
مرز چذابه بسته و کامیون‌ها پشت برخی مرزها متوقف‌اند
🔴
رئیس انجمن شرکت‌های حمل‌ونقل بین‌المللی ایران:مرزهای مهران و باشماق بازند، اما در خسروی، میلک و دوغارون ایستایی کامیون‌ها وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/147544" target="_blank">📅 13:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147543">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
آخرین قیمت نفت: ۱۰۸ دلار و ۲۰ سنت
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/147543" target="_blank">📅 13:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147542">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
دفاع مدنی عربستان سعودی: هشدار رفع خطر از شهر مکه، استان طائف و استان جده اعلام شد. برای حفظ امنیت خود، همچنان دستورالعمل‌های دفاع مدنی را رعایت کرده و از تجمع و فیلم‌برداری اکیداً خودداری کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/147542" target="_blank">📅 13:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147541">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
یک فروند هواپیمای دولتی ایران با شناسه پروازی «IRAN06» از تهران پرواز کرده و بر فراز ریاض، عربستان سعودی مشاهده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/147541" target="_blank">📅 13:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147540">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
پروازها در فرودگاه طائف، واقع در شرق مکه ، متوقف شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/147540" target="_blank">📅 13:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147539">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPTBsCIAAwsP3AWlY5TvRR9jMipkV21fvJ6bQDjUcPuQaoZzr9fckIG2sK4ZNmzN0lWxs6b4eVKhACnUmXgrVCdYnV9xdkSijhftjPyWwrTokCG76ry5sj501kLx3zl-UKCl8AacrqCTU2i5QwIgeQnnzy_fUXjDBAwp8Of_OY7wWnVFsVdilgrZ1ad2ZSkbGXfeMa2NvfNn-rbnNMthz6DburMzp8LfX95hJYfXISOnsAbUvDQNNCm3Mkdtvow_Wfzjfz8Nt2rAvwm7yDVcLACRjFFhG3y61N-LzUg957u_s6aTIIzQsiKBa-bs4A4wAd25QCOGT_DjzQYlBwYNkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پروازها در فرودگاه طائف، واقع در شرق مکه ، متوقف شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/147539" target="_blank">📅 13:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147538">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
برخی منابع عربی از وقوع چند انفجار در شهر طائف در عربستان سعودی خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/147538" target="_blank">📅 12:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147537">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا:
گزارشی درباره هدف قرار گرفتن یک کشتی با یک پهپاد ناشناس در تنگه هرمز دریافت شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147537" target="_blank">📅 12:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147536">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5knPYk10nFRg0rvq-HZEe0YL5uXajeL7-RVqwiPBFhXHulwNUOBt3FF2n0uti4Iz8g3Kz-KUr2mw2O-_aUwQhNLoM93TXKUrKi5Z1VW83BuhopHvcEcFOVaZ4d7gcmMIBJbrEGCxZ5L5yxYRYdsATL_LKyTB1jivLCVGayiP7HhdYoG5nR38tSW-IZNwQ1sgR9giowid7HdGr8vh_UgnN-guKf0_Q0uRTcCA0DzADU4O7kNz_-hED8TjUJx2MnCoFI-yjdGZDepPfbRUpJmGmvUygEJiN02BUJHfD4cATDvhrKI9orW0wRdj_WtkbjH6PF9IqCaaAORv2-zaJFgJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خارجه طالبان: هم جهان اسلام و هم غرب از ما می‌خواهند مدارس دخترانه را بازگشایی کنیم، اما نباید با نگاه غربی به ما نگریسته شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/147536" target="_blank">📅 12:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147535">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
یک فروند هواپیمای دولتی ایران با شناسه پروازی «IRAN06» از تهران پرواز کرده و بر فراز ریاض، عربستان سعودی مشاهده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/147535" target="_blank">📅 12:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147534">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
دلار بزودی 300هزار میشه
⁉️
🔴
تحلیل ترسناک هوش مصنوعی
👇
https://t.me/+cs85WnZxgpM1NjRk
https://t.me/+cs85WnZxgpM1NjRk</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/147534" target="_blank">📅 12:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147533">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ویلیام لارنس، دیپلمات سابق آمریکایی:
مداخله آمریکا می‌تواند به طولانی شدن درگیری یمن بیانجامد
🔴
واشنگتن می‌خواهد از کشیده شدن به درگیری‌های منطقه‌ای بیشتر، اجتناب کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/147533" target="_blank">📅 12:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147532">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbV4f8GRgsy8kJdQDXmRvpbZzRSrZ3jOlqttfojrnx1fwYaqwF9Yj0pcG06kPQA1a55i5ASG_Ow8GSNGnFORLbHvwfTW0rhreW6PD-so94nsntlwfPksW5jl9iX-vPbfW_VH9sL-Vi3fKM_izYZ44BH2Y3wYy1x8aETIF-eprXqNCvTJ_wnwHfhJk1D-ys9EVq5Sq1Mk9gFVqyrxOgyWIu0V4Kwfi3wybVqQMm5QIkmiQtuzJNSa5L2CsfquoeBSmeM9BmgpuI34aowAUWCbfrL19Yp8U4HCwupUU328tbDUwFOjiMjfLHA_xLSON7ZKSV_Hw5lRi3w7Xl0Lwy7-bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیت‌کوین زیر ۷۷,۰۰۰ دلار سقوط کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/147532" target="_blank">📅 12:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147531">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
کره جنوبی و ایالات متحده درباره اعزام احتمالی نیروهای نظامی کره به تنگه هرمز گفتگو خواهند کرد
🔴
به گزارش خبرگزاری یونهاپ، کره جنوبی و ایالات متحده این هفته مذاکرات نظامی در سطح عالی برگزار خواهند کرد تا درباره اعزام احتمالی نیروهای نظامی کره جنوبی به تنگه هرمز گفتگو کنند.
🔴
کره جنوبی هفته گذشته تیمی را برای ارزیابی وضعیت امنیتی در نزدیکی این تنگه به امارات متحده عربی اعزام کرده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/147531" target="_blank">📅 12:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147530">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
رویترز :شورای امنیت سازمان ملل امروز درباره وضعیت تنگه باب‌المندب نشست برگزار می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/147530" target="_blank">📅 12:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147529">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
عراقچی،  روز ۱۶ سپتامبر (۲۵ شهریور) به چین سفر خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147529" target="_blank">📅 12:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147528">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEOLQ5legS1d3aBOEgVjZXY6e6hAUM8H7oLxyPRZX6MKIszyTMXUpY-u2j0FYQvgHIZuBGHlR3xqinun_kS8CbX6Osejcg9t3_7Jn2qnM9ZRHriRYHoZMJlaWYMzSKuXA9Hq5jwv9RLgqTakfNWAOmxVQgt_2RCitqxaTVIv4zIeEwd7J7cMyyxG-Nt174Nf8SaRhRlafoeztE-9wqMXq0GRjfZyZ-2zjp-Mp7qQxOMrGnoUnotvR8pjLw2K9A0qvATbGTSSkdQvJbkfXqKWsGvT_v1tsiajOf9e4t1J9lHKgwjB4UaiUAAqBhieUR9xWovMI5ymgW8nfA9mPifQYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تحرک هواپیماهای سوخت‌رسان آمریکا بر فراز کشورهای خلیج فارس
🔴
حدود ۵ فروند هواپیمای سوخت‌رسان آمریکایی بر فراز کشورهای حاشیه خلیج فارس در حال فعالیت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147528" target="_blank">📅 12:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147527">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFSCeNm-eN91j8rGFG4GjQZNIAkBgFLqybcpq9xrlzGIv3BlxqGH0vD_ObmQcZOv17DGtVr7KUyey4KQ-rlEzurvXbA9eFIjYBmhuEUhLqMjxvRzg1YRFpkfpUaYq19FElOTlBwiQQh-mXOCwIDsPrP5ds5sJu7wdNY1E-P3vAGGU-huQj-yffQILTUukhQ1TzyGnXLU7xl4L9X175FvPzfdxxYoRG-Ir2EXerrojfRbiYm24ifqmD9PW3T6EgA7K_M7KlkULoCeWF9xdJBZkJCSuNAPYoYZBa3ArRduEE6CnfWIzPDH6IPJNTZrP2_5_7OqAFlpMBeRwpnROP9ebw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کویت حمله موشکی یمن به شهرهای ابها، خمیس مشیط و طائف عربستان سعودی را به شدت محکوم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/147527" target="_blank">📅 11:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147526">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8539665416.mp4?token=DpDdqlKvtxEY9wgeksns8sVzRZhRufq3wo82wfoi9yQL8ZEvl7PXO4UgD4cfFaQzk6AsPnXDWEKD9NPgyy4cmMsMQSXXU86yNEJ8qORenB2CFjbv7r-Ln_03gNrbstMSLsU2wYVUEl-wll0LQ7_bAeF9o_8Z-blA9xCdwV5o1b-7Yi2iMv1EHxRJ_i6miC1yLnnKi7HN6we2gg1Y5-6QOSQ7MUE7DRy3LK9FzkIyo962RKW6iJ1yBSkCGJM5UcCBJYJLeChDQyViSXxgqJFvrzgMF_E7vaNKGiTZnEFs-s7VwZCxlWvsURifBKfkSl8p1U3iDbhd0tguVB69peqyHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8539665416.mp4?token=DpDdqlKvtxEY9wgeksns8sVzRZhRufq3wo82wfoi9yQL8ZEvl7PXO4UgD4cfFaQzk6AsPnXDWEKD9NPgyy4cmMsMQSXXU86yNEJ8qORenB2CFjbv7r-Ln_03gNrbstMSLsU2wYVUEl-wll0LQ7_bAeF9o_8Z-blA9xCdwV5o1b-7Yi2iMv1EHxRJ_i6miC1yLnnKi7HN6we2gg1Y5-6QOSQ7MUE7DRy3LK9FzkIyo962RKW6iJ1yBSkCGJM5UcCBJYJLeChDQyViSXxgqJFvrzgMF_E7vaNKGiTZnEFs-s7VwZCxlWvsURifBKfkSl8p1U3iDbhd0tguVB69peqyHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایلان ماسک درباره هوش مصنوعی: «اگر هوش مصنوعی بتواند کنترل سامانه‌های نظامی را در دست بگیرد و مثلاً یک سلاح هسته‌ای پرتاب کند… این اتفاق بدی خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147526" target="_blank">📅 11:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147525">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DGdmsirTT6pm2MAYFgWSxHtNDqFkFti1XlMbw-wkkJ62PJDgPLm_5_D2jVgo6Qh_AF0wwGqvq6VmIObzruJfE0rs90LS9ZWwKdIQoOLbX4JYm6OyjPquGR_TQJD2y7CX2AbdhinTWdZ5irysO4u-gGdY43xtIRYUCoNz86hhfYIwrj-V0AbwON-IMRGyji028ejlVI1GAKDPUofKmkKvTP61VBRZT151nl8lT7md0QchTjpQTqM-ZUBUymswAmxL35WKn2SmJufBfWHSQD_wSo1IwwFhdcb1WRgvnUuejUwqPvndHtRQU9bUEKUybzYBuF8aaLb5CMXcyEqb6Ar0Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای دولتی ایران با شناسه پروازی «IRAN06» از تهران پرواز کرده و بر فراز ریاض، عربستان سعودی مشاهده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/147525" target="_blank">📅 11:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147524">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjJeXqnDz-wOCEY2FUoGv57aCthEQFIhmqomFGXNXVCJ4sGRXw1l7eulg-uuLslkG9xlvhXuvU6oNoIOFcN7R9zged1PysMfA23os6xXWrUmtqt6-8aMGry7FKCBFRX3BjLG8MteUaUeiuz28xbZXf6tyrW2JCovzNNB9bY5uiwix7j-7yKdzIJ1K2q4PanUvYbFoOQ_8hHgSEcuSS74gilsJnTXZScNZWvPmbsTppK-zMbKaxLOEDlEoOyYMwY0JTdSaYFSQvcGaiQiU7sYIJloCKi84NwQ15CRrMzKMsegsyOLNAR8Vqy_N0_dL924gothVoqvnj254ocVeV-_Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
نتانیاهو:
پیمان مکه فقط یک شوی تبلیغاتی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147524" target="_blank">📅 11:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147523">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‼️
اگه میترسی طلا بخری یا بفروشی حتما یه سر به اینجا بزن
👇
https://t.me/+jkJGKa0y56liZGZk
https://t.me/+jkJGKa0y56liZGZk</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147523" target="_blank">📅 11:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147522">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2pXZXaqAJj1v3hH6vNRggDof4VEXk1dqGu13jQoBiKpfb_fEoGmcrxsrxjN5NGBS8RU-AUIGi2IPuehDCmG6lhgfez5H3uTlaNso36slVUgMbeXGjHb7E5FcTOdsV9yE1natQ2jGtMazm-APeDStb8J0bmIr9wDuI7YxidnKq3K2GuaePlO1OCXF9WhGm3ISl3eSOQzYVhdQD992PuWE4k08cLtLkHOqz8BXBq5LUyh_9tiGd3nBAQhgjEcsgG43P5i6Zdm-9rQKpijE-_jTIppLQBmXqdyNbkuOqQIeZqNN5OmLb87y6JYNHDyQM-dWUbBUx34ltMWRTyRyW5Vkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بافل طالبانی، رئیس اتحادیهٔ میهنی کردستان عراق با عراقچی دیدار و گفت‌وگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/147522" target="_blank">📅 11:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147521">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
الجزیره: درگیری میان عربستان و انصارالله، اکنون بر «مأرب» متمرکز است؛ در صورت تسلط نیروهای انصارالله بر این منطقه، روند جنگ می‌تواند به طور قاطع به نفع آن‌ها تغییر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/147521" target="_blank">📅 11:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147520">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
تحریم دومین بانک بزرگ روسیه به دلیل ارتباط با ایران
‏
🔴
قبل از این هم آمریکا، شعبه بانک مصر در امارات و یک بانک ترکیه را به دلیل ارتباط با ایران، تحریم کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147520" target="_blank">📅 11:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147519">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01b896d38.mp4?token=fxMkvm4U5cc7RjMTkp-MWaiZmrXtpgI2D589TIizFCza5lL7z65G1QHn02VdmV6ci3B_lKhGS1TZDC3A29bAmVuAFSVLUgXpR2yvcuwMmZoHcX865gNkTA4IFB9ad2eqPw0stEa-Xidi-lfMIkXCZKH50RxYqC-EUQPqhfJozpdzUS8Mow1G6VSniRGehCm0ivrsnyeuo25CgtKkPzvYyrAB6gL1vGbLKC4z96syCY3lgaE-VA7VnXpF9EK3I-W_8QNcoIcWbma55D77Z3dfIDQTs5s8YGlzNKUgZ3ZGFhulZnQx7S5K_dZFtjFx0DVkxTyC3AIT_kT981rulecyyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01b896d38.mp4?token=fxMkvm4U5cc7RjMTkp-MWaiZmrXtpgI2D589TIizFCza5lL7z65G1QHn02VdmV6ci3B_lKhGS1TZDC3A29bAmVuAFSVLUgXpR2yvcuwMmZoHcX865gNkTA4IFB9ad2eqPw0stEa-Xidi-lfMIkXCZKH50RxYqC-EUQPqhfJozpdzUS8Mow1G6VSniRGehCm0ivrsnyeuo25CgtKkPzvYyrAB6gL1vGbLKC4z96syCY3lgaE-VA7VnXpF9EK3I-W_8QNcoIcWbma55D77Z3dfIDQTs5s8YGlzNKUgZ3ZGFhulZnQx7S5K_dZFtjFx0DVkxTyC3AIT_kT981rulecyyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهاجرانی: ان‌شاءالله شاهد صدور گواهینامه موتور برای زنان خواهیم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147519" target="_blank">📅 11:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147518">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
سخنگوی ارتش در واکنش به فیلم نجات خلبان آمریکایی:
طبق قانون، در صورت سقوط هواپیمای ایرانی، اگر ۲۱ روز خلبان مفقود بود، ارتش وارد عمل می‌شود.
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/147518" target="_blank">📅 10:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147517">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
المسیرهٔ یمن از حملهٔ موشکی عربستان سعودی به منطقه العصاید در استان صعده و مواضع حوثی ها در شمال یمن خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/147517" target="_blank">📅 10:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147516">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnPsjGw5_PzVQN1DYp0kZnTeVnO7kHQp8xbt6oB7tssrWW65egHru7xQK_9J14h-NjMp9WahD--itQH1hWESmeDtbBEi0VU5Va3Ygcu_9htE6_CaUFrrnvwIbG5RYYlZ7IOC3qd76j6tJyNJtJXYyRlsK8ysg6kWz_5TiPcBM2eYokXoh3Y7fI53WQZ9sYG6-jjzOY4RC-WPlGm6LsUU75BUl3XpmhH_03MU5-V2bCbl7S8wV-Ep8g3VpDHVUUNV4Za73Qyn5UXo_vKs920ym9ohcaDG4dcOu7Z6salku0ScmT0e-71ur5w2jm_o6F8jQ7fmUduiypqCtMwKvFG7iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که یک آتش‌سوزی ناگهانی در یک مجتمع نفتی در شهرینبع، عربستان سعودی، رخ داده است. این آتش‌سوزی از طریق برج‌های احتراق رخ داده و شدت آن حدود ۴ برابر حد معمول بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147516" target="_blank">📅 10:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147515">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">💢
رو کدوم سرمایه گذاری میکنید؟
دلار
.
طلا
.
ملک</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147515" target="_blank">📅 10:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147514">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سخنگوی دولت: مصوبۀ حذف سهمیۀ بنزین خودروهای نوشمارۀ بالای یک میلیارد بازنگری می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/147514" target="_blank">📅 10:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147513">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nl8hJIouCUIZpEMTViGJCSDaLxcKSqwKEPmHYFjJMsHCHZb3wlQ-fsvZxVidhlnLSeEVHiyot1Fib4sDz-dLjALJ-uBUX_H2dWNshFw4PpWfGYzKoEeEAyTnVWHSKkflXoFFWgaGC_eWsB2BvrEjYeIlhvpwrOHjzQuAZ57XIGhakwSrsdXumI5onucfi5CHV99mbbXaaeOYskmqG3XlQSfJznsDap31gx7uFD8RBz2xV_vcL-qJRUWPD2d-EVxNnwWJOgYzD8omda3xPnh8Cl69AICmb5bvwWjJj83V7Qw0Ik4y0o1vBKDHOoT5fWH33Z23K-vxsP6iPEzEpJknoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احمد البطش معروف به «ابو اسامه»، فرمانده یک گردان در تیپ شمال نوار غزه وابسته به شاخه نظامی حماس، در حمله ارتش اسرائیل به یک خودرو در شمال شهر غزه کشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147513" target="_blank">📅 10:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147512">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Imhsd-VC0efJJZ2bGgmeoew3O7y2UMdqFqYlhcHBH4j3izPbMEpO6WfiLOvtB80XuPaEtr6ghpxJggHWFYDYx6uYAa0zbc3dztI0ClhMwf2T62rolGNC1h8H2uYq2ZuIDAXb8tAOrS4g3tbaRnYqN0OXeTAr47bKc22BluSrlQ76ModtiQQsEYR0ME3COALAWhM5AY5PsqJZxSBDZzgsxUTOCPPL0RO8jOOdfEYewlB9US-w9GYBNrGfb46WQcoVCV42gvh0bOMdOJbcprx_kNla6npfuqXctz4hTvgIw84BKcUKre_zF36tF7UPpRDnKPGcohN10W8SnpJM_aFjEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بحرین حملات موشکی بالستیک و پهپادی حوثی‌ها به عربستان سعودی را محکوم کرد.
🔴
وزارت خارجه بحرین ضمن اعلام حمایت کامل از عربستان، از شورای امنیت سازمان ملل خواست برای توقف حملات بیشتر حوثی‌ها اقدام کرده و مسئولان این حملات را پاسخگو کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/147512" target="_blank">📅 10:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147511">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0ddab11d0.mp4?token=PtMARlwvF1vPOc4Lq0msyF9usiG6CBtPCJPYeaMypou1iSaNB4JDTJPTNoltXot1DmpzHW3i5kK4nzB9IOE_V_y5vJmrtxr37mx4atYEh8hpbTLo_mfUCFi_yQ8xvVDIxFSQlEWn4vQWY1S9PaOWt3aMUyJvrnahXHK9JHUGnvrs5tBBYF7BMDfmUibtF2tr1ftTqExkH7iOlS2bRU6-gc6p7P7k4Iwo4kj7UXB8P7kF4-WrEQ4uaNUNefScP9JriQpWvQKyfK66pGosFtM2DvRj5Fzv-CZ7r__w6ehhErTBKNXl6ntPjYmuvN66tt6GpJyBWs2bFIkNtxI24-0swg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0ddab11d0.mp4?token=PtMARlwvF1vPOc4Lq0msyF9usiG6CBtPCJPYeaMypou1iSaNB4JDTJPTNoltXot1DmpzHW3i5kK4nzB9IOE_V_y5vJmrtxr37mx4atYEh8hpbTLo_mfUCFi_yQ8xvVDIxFSQlEWn4vQWY1S9PaOWt3aMUyJvrnahXHK9JHUGnvrs5tBBYF7BMDfmUibtF2tr1ftTqExkH7iOlS2bRU6-gc6p7P7k4Iwo4kj7UXB8P7kF4-WrEQ4uaNUNefScP9JriQpWvQKyfK66pGosFtM2DvRj5Fzv-CZ7r__w6ehhErTBKNXl6ntPjYmuvN66tt6GpJyBWs2bFIkNtxI24-0swg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواشناسی: بارش‌های پراکنده‌ای در بخش‌هایی از کشور طی ساعت‌های آینده خواهیم داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147511" target="_blank">📅 10:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147510">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سخنگوی دولت: بانک توسعه نوین (بانک بریکس) با عضویت ایران تاسیس می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/147510" target="_blank">📅 10:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147508">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VMUyVcSpCFoUHVUQG5WqDAAcMaJnKGvcGt1iRLXlTY1IrnyAUTB3Kmt15-UZnKtRsO4QEMNzZAueLRFLX_RfUsXWr2CZWwYOrQajdtYi64MH55Mr3bcKpbMa8S3vcs7O3o9yDq_tWYLtD-CCaWQYItmfiGJF3pwJl5QEZmzYe6_Mja4dzEcqVSggEr9xqPQHHpdad6gluwHcITPBYeam1II2SuKAoNHJ1vKA1_NjzXUMjww3TjHc0xLA44U576ZFszxTpf-86UZTg_216g5SkONyP4PPzh6Ljp90R669thSLzpnVLvc2Lg0TTSskkVUztxxhiHVd-9WcPldsWB19mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qZVPS2ymiTZnkeNc0n3eN_5q_Hg1iyDPmEM9gyAU8SOOj_7MgOjH-xrQ3nLHwc5DEaYrfTSg7nl0szpRXJdXkfkiz69_hZOE-b71YdTBM-jcF07HF6c8O25d6TDF96qEsnkRfuHYz-OtJ84XMWzrLORGpet3PrV3EHiglgp8IHYe7KhaAa-JD5kvSo2acEUbQmK60ZHTi_e_e0Hnyz36ItXSnoRQTr93RrbXoBfmHbbSuddzO9ByQYMUQNw4jgPjlS2iPWXOIu8foKRxf-uLcoSMU9a_j5VVfSjhxgrBwNxeMUngaLBFJiYaNoOOD2AU5oGvxOY7k86FXvQvW3AHXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تانکر ترکرز: بر اساس تحلیل تصاویر ماهواره‌ای، می‌توانیم ببینیم که تنگه هرمز اکنون میزبان ترافیک روزانه دوطرفه ابرنفتکش‌های VLCC است. علاوه بر این، حجم بیشتری از نفت خام، LNG و LPG از طریق انتقال کشتی‌به‌کشتی (STS) در دریای عمان مبادله می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147508" target="_blank">📅 10:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147507">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
روزنامه هآرتس عبری:ارتش اسرائیل به مقامات سیاسی توصیه کرده است که از مداخله در یمن خودداری کنند، زیرا معتقدند تهدید "حوثی‌ها" فراتر از اسرائیل است و به کل جهان گسترش یافته است، و باید یک ائتلاف بین‌المللی برای مقابله با آن تشکیل شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/147507" target="_blank">📅 09:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147506">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
وزیر نیرو: صنعت آب و برق ایران در برابر تحریم‌ها خودکفا شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/147506" target="_blank">📅 09:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147505">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJrNi8oxBQyOP1JS_TQhYyCwdN5vVSB5dmVeqCYK8KZiAqtfER-cGAr9pU3yy1iqag4JEoOwlE41xQXCAipB_wFR2Z1ExmpKIYfy4ZgseLQqUnRHqu_s704rlXr_0UCpOM_kWa1ykvbwiUUKHbNJJE1ZaR2HuDgFt8zBVgnuQN5BvROV7XQcW1pQz04oUTiLd1xVfkJQQfxspBh4K1eQVDc3AEjIztNIR4CNg5J3X_rNt2tDqlPpsjHAwUHQP9vPBNuX24UtkjnQaBOxFgepSZATLIUb7HVQFRGajFoGDCy2ui914Uc6NJ0xkQOgG4vmvmeBqeWX4p8mXYtpMS3UFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: ترافیک دریایی در تنگه هرمز پس از افزایش تنش‌ها در خاورمیانه کاهش یافته است.
🔴
این موضوع نگرانی‌هایی را در مورد این مسیر ایجاد کرده است، و به نظر می‌رسد که عربستان سعودی ممکن است در عرض چند روز، ذخایر نفتی موجود برای صادرات را به پایان برساند، مگر اینکه عملیات از طریق خط لوله "شرق-غرب" از سر گرفته شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147505" target="_blank">📅 09:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147504">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
الجزیره: مجلس نمایندگان آمریکا رأی‌گیری درباره قطعنامه‌ای که خواستار خروج نیروهای آمریکایی از اقدامات نظامی علیه ایران است را به تعویق انداخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147504" target="_blank">📅 09:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147503">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
تاکنون، حملات یمن با ده‌ها موشک و پهپاد، تاسیسات نفتی و نظامی در عربستان سعودی را هدف قرار داده است:
🔴
ینبع
🔴
طائف
🔴
جده
🔴
ابها
🔴
جازان
🔴
العلا
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147503" target="_blank">📅 09:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147502">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHlGE7KTH3aGff0ASsbiskvKaR-Q7d6QvB1AtjCevW31wbnNtDENApqsv3whfY6-Md3-dFhLwmSuj7qOk1fzG-eLH5CFuUd5P6BIO6XiVYyp_LfYRmOIB0Qz-oasAarg2YN5NykYx_2PiWRkD1YS7x-i9s2u7Nb6T99M3OT_U7wmJG9Gk1pR_4CHkeiuCrIb-isrrG3sM0ndkLwfw-XlhlT1aF93eBJgsvDiIbSnK1DxZCFDEg67HFt2e8UqGTtSLnGc5ZGkSyju6PImHfPjtHVzEPxIUj12Tn3vLwN4SBVpmjQW5OWKV29bPRtqSYhjI735Kb_1wJtOWSe9ShkTcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز به نقل از مقامات آمریکایی و سعودی: عربستان سعودی با "بدترین سناریوها" روبرو است، پس از آنکه ترامپ از مداخله نظامی علیه حوثی‌ها خودداری کرد.
🔴
عربستان سعودی نمی‌خواهد به تنهایی با حوثی‌ها درگیر شود، به ویژه پس از اینکه عملیات نظامی قبلی خود در یمن به جنگی تبدیل شد که حدود یک دهه به طول انجامید، اما به اهداف خود نرسید.
🔴
هرگونه درگیری جدید نیازمند حمایت بین‌المللی است، و نباید فقط به عربستان سعودی و کشورهای منطقه تکیه کرد.
🔴
احتمال کنترل باب‌المندب توسط حوثی‌ها، همزمان با بی‌ثباتی تنگه هرمز، "بدترین سناریو" را برای منطقه رقم می‌زند.
🔴
با وجود سال‌ها بمباران عربستان سعودی، آمریکا و اسرائیل علیه حوثی‌ها، "هیچ‌کس به راه حل نظامی" برای مقابله با آنها نرسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147502" target="_blank">📅 09:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147501">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T0VugesB1bZtTxcHbOLZLLlKWN9KUTq7dCVtxKgjP0vlKfecJVhjBfCvGpK3IY_OMty8ZdPOJdjIURHk3fMuF3s1k2AEiknnHuszcJ-LQbxbgz24BRpRn5fX31hVbxW_P8PvDjDsUcrWsu_2OVOfvUG3Z9gCyemHCy-uIvzTY7_G0KCC7yKRCVrpFxUe4e4aYWYphjtwUPAozlI_CgRkNfPJD34GquWFRGIz7cg3fqsCId3lFyEkZOBdLFF-OvyORtI_nhvuYYN5kagj4q2DJu-UKR_NhX2g7H0tpoSLkE6ndpTFeCqUD5VDUlMk60pOiRajPF5aSmsrAXj3N13Q-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای عازم فرودگاه بین‌المللی ابها در جنوب‌غرب عربستان سعودی، در حال حاضر در الگوی انتظار پروازی قرار دارد
🔴
احتمال دارد فرودگاه بین‌المللی ابها هدف حمله انصارالله قرار گرفته باشد یا این اقدام صرفاً تدابیر احتیاطی در پی احتمال حملات بعدی باشد.
🔴
هنوز اصابت به فرودگاه تأیید نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/147501" target="_blank">📅 09:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147500">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
تأسیسات نفتی جیزان عربستان سعودی توسط حوثس ها مورد هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147500" target="_blank">📅 09:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147499">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNtPRGVnWYLWrT--8R_Hmud2KKgG754Ax-T3DdLqwdDK4vEEe_LM7Np4JTX0v8Cw0TM4LWRdICcwkkEnyWWQ1d01bS7z7TudYCdi5qFkv-bDtq-HVw0izVQPeWjmngwz9NZ12-Gl7bRiRFatU1e33qnX6F_vSeLi-MH7UCxhhthD20ttOvOgcDxMU1zWGReGZV2PNmNaeRgfHKIulU_jB34Tc3jP0D9vj_THDFl2TiQxplJR0AqZGqsZ-Wt5YE3axRpexY9AUb_aLNO6paOTKrua8k9a8r5atiBj9WWFzewvazs0fLmnn9TKWrD3CrW4PAw444abhZtHXl7BdDsJ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت ۱۰۷ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/147499" target="_blank">📅 09:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147498">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddc8166669.mp4?token=G6X22Vf4WuHTa9pAdoFrUCGcW_ZZm9Y7Y4j_1mvahTTKOk3qF8-XLpPxE1idH7Z18T29LJdpXSnW-05zURYx_L9VSDQzARwJLmdAbTs4FydGrxTrDvt4xV2WVZPyR0_2E5NCexQSr0M2gAgCOeu1e-KcbWOE4wZlgSwuOieOafXgak9MOAUkaTcx650-kLCLS4P72iIA0w5mHkA6jRMHqYuzAEKsMeNhVrf7Sbcu442j41FJmlmlvh0Na_ZdXbHWOVDZ8AbSGDb-1FbsmUpEX_GQjs170ftKCu5GmoanY6Xyzu-t5-e00Rp-H4BDUvaS30PEi-CNnhghqTRJp1_32Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddc8166669.mp4?token=G6X22Vf4WuHTa9pAdoFrUCGcW_ZZm9Y7Y4j_1mvahTTKOk3qF8-XLpPxE1idH7Z18T29LJdpXSnW-05zURYx_L9VSDQzARwJLmdAbTs4FydGrxTrDvt4xV2WVZPyR0_2E5NCexQSr0M2gAgCOeu1e-KcbWOE4wZlgSwuOieOafXgak9MOAUkaTcx650-kLCLS4P72iIA0w5mHkA6jRMHqYuzAEKsMeNhVrf7Sbcu442j41FJmlmlvh0Na_ZdXbHWOVDZ8AbSGDb-1FbsmUpEX_GQjs170ftKCu5GmoanY6Xyzu-t5-e00Rp-H4BDUvaS30PEi-CNnhghqTRJp1_32Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر منتشرشده از نمای یک هواپیما، شکل‌گیری ابرهای عظیم طوفانی بر فراز ایالت یوتا در آمریکا را نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147498" target="_blank">📅 08:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147497">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WY2Iy9Q_xRMPraecNiAZfJdTbvvHORQZEePpCh0vphSwidiqX4UWvEdhD0W0FnNoUGvGCy5VA1Zvk0p9J9z3f3W-u0uBSS4k13TgvoskTx2Gbvrci1P9CnqH1-PpB1liyQgM4eX0ikATOGLrxK_m1z-cWptKGXrau8mFBiJVWaqyvGvmpvFbM-cwQjK_DGhKuI3Wh-j_aAMvL6F5SrkXOc7V9Am469LGtap4mWaiYKCLvhYHt6OQsrClE5dvQAAAnqU0DC3wpM8w14ANwKHs7QNBiay8q2TTHMOJaDXjuALojXXphbdnameD6U9nv01E9btwkS0Wqwaf7LoU28TE-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای بدون سرنشین اوکراینی پالایشگاه نفت شهر سیزران در فاصلۀ حدود یک هزار کیلومتری خاک روسیه را هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/147497" target="_blank">📅 08:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147496">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وزارت دفاع ایالات متحده برای اولین بار اذعان کرد که سلاح‌هایی را در فضا مستقر کرده است.
🔴
تروی مینک، وزیر نیروی هوایی، گفت که ایالات متحده اکنون به "سلاح‌های کنترل فضایی عملیاتی" مجهز است که برای محافظت از نیروهای آمریکایی و متحدانشان در برابر اقدامات خصمانه طراحی شده‌اند.
🔴
او از شناسایی نوع این سلاح یا افشای قابلیت‌های آن خودداری کرد و گفت که حفظ محرمانگی برای حفظ اثر بازدارنده آن ضروری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147496" target="_blank">📅 08:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147495">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzVBttCQA52L7VA9cjarYO_545zSNIIx2qvJDKbce68TImK_YVGXYEn11mrHwIn9J2R3-QLPMGrM1SdC-pCBRAAu3CPPCmXS0ckU0yJcyBsdARZ4B7rknADvxj7CYnDx3zGAw6KMwaIA1jmx6-C3Ahi38SgBOn9SXg40ZdF6EsigjBhLX6fzqfaidVeK08v2xcQGcj6jaIPvG-LYEnVh0WlNALXsBWzP7LASpJm21drgt0CbnMYygfTkZzInrkm9elukWeUak5QSaYLmm-zYMBauOOT-3eaZKvv0NT9i6NAbCkN-7QERwoyCtRCVh-Wn2jiUy5kt8FA5J5rPa879nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوآوری جدید تو جنگ اوکراین؛ پهپاد چهارملخه مجهز به پنل خورشیدی
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/147495" target="_blank">📅 08:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147494">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqO_5rRn_7xF8OTk6g5dgdoUPwF0Ftzq0r-_UFsYjiGaj1cYktgaH-z87H-yImcNR1LjBqRiJydrufvajozB2sOcmss4EMLzfWbsFrqC97QUHo3OZiXE7xoR7qAjLEILc8-ztcIK42kGdIi3ZLjGymH1ID4xrgqI1lpBUAKGdpXOEZ2MmuomjtjNbHJMon3AScP2NRCsvLZhybA20xu6ZWkxUXEOJQ1nkOHCKiMtuCwa65gq1K_-NCt02q2kg_1Tfj7MK_oza3YVCvMHYiCM0lMOfrHOQEwY16UMciBdNuGKo0HoXf3WLm_MbUr24n5HY2v2G8KKcCdXqtSG5qhcyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: عربستان از پاکستان خواسته تا ایران را راضی کند به انصارالله بگوید از فتوحاتش عقب نشینی کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/147494" target="_blank">📅 08:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147493">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سپاه: بامداد امروز یک فروند پهپاد پیشرفته MQ1 در آسمان غرب تنگه هرمز زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/147493" target="_blank">📅 08:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147492">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBRmjx_PLKgWZVqDlMD2buDPWsbwDarQlqC3meb2gEZOHGK7VPnSmZlAEyofKNTTof-s_4uQY6weeIl2ad9RyRCqE3t3r6UXQYiwTh_rp5mVdCSumDF3Pi_m167pU1WRdbCftl8uPoz1C2k3hgAkNw3ZWa8tMQRkH3VBmg-7ynoeknv9bQIcvsqNkeFT-OnJb-nZwZo9X9RlE1kx9LNytSbYOFFoERFvng-RaRHLtdaY0hVTAFX2GT3KuGUlfAbdoigxyPR3jbHPHSeCPWRQYH-ZrWU0RVbLWRNWZLwNvL_y7BhSCTs4lpYl2fy_AOFKnmMgGKicyuBYl56YNBTu8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد بارهایی که دونالد ترامپ در هر ماه علیه ایران اعلام پیروزی کرده!
🔴
آمار سپتامبر واقعا نگران کننده اس. فقط یک بار
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/147492" target="_blank">📅 08:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147491">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erpNYWg9sTi0RnRIGTQRydzHSi4rC8st3cFNxS8tQVKEq7xTXIIjR6eXOx5V9mQITIG6iIGfXJA7xBkvY7DN448lauirJ2mRISQcSI8dYq4JZWCFmtO7ICKUS32EGqK9Y38DE9r_7Vyy14UF8HR6vRg4ztnRHXIbwzYb0LmHtEA-Hp6Z35xRVyWrAElUZFyzLuh0RCjoHB32LNlQ-BZgKQYOlE1_XPKrveTIOavGg7Q-5WbXm-4UWanikDS-Y2WGQPJ9igmbruu0U-2Ma1PAyJ465fGGzhp36eDj468y7vGzDR9ZFpW3QcmlgTDWYnOvbLBGmYOSYzWvoaQkfufj9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسکات بسنت: در چارچوب عملیات "تنزوای اقتصادی"، وزارت خزانه‌داری به هدف قرار دادن و مختل کردن فعالیت‌های آن‌هایی که از نظر مادی، فناوری یا مالی، از رژیم ایران حمایت می‌کنند و به آن امکان می‌دهند تا فعالیت‌های تروریستی خود را ادامه دهد، ادامه خواهد داد.
🔴
وزارت خزانه‌داری هیچ‌گونه حمایتی از این رژیم را تحمل نخواهد کرد و به شناسایی، افشا و منزوی کردن افرادی که به رژیم ایران کمک می‌کنند، ادامه خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/147491" target="_blank">📅 07:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147490">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوپینگ | EcoPing</strong></div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/147490" target="_blank">📅 01:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147489">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
جمعی از نمایندگان مجلس در بیانیه‌ای خواستار تجدید نظر عضویت ایران در npt شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/147489" target="_blank">📅 01:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147488">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0M9nnA2nXryb-nd1dUwt_s1Zmi2Nh92rhWcM8isZGuzgtvL5iexax0VACQwH6-yYNTBJCVESduR1ayekCYc00m1DrrX9oVGP2LA4SbGdMs19pKjyVIfIDqwMiYEwNxXWO1egdxfpFueOMAcdaQRJSqen6_u6S2zOqkqSpSCgr2zbZjRDSJuwleeLxSNeBpXZxUlXY82pDyiQpYS_ngBEUbcQrboLoylxzLrroRkTIicEeHsIOxeedCIM0xmHCzbPgcWPDyVsijy-NE0dTW7swF4BQSfPdvcvswqlvbuAlfX_zkKNEv7t-OemIRP4BDtx52AmHVKoswwLT26niKnZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صمصامی، نماینده مجلس: 56میلیون بشکه نفت تو کشور گم شده و کسی گردن‌نمیگیره
🔴
پ.ن: حدود 6میلیارد دلار یا
1,410,000,000,000,000تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/147488" target="_blank">📅 01:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147487">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
گزارش‌هایی مبنی بر شلیک توپ‌ها در منطقه المنصوری، در جنوب لبنان، دریافت شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/147487" target="_blank">📅 01:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147486">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 250 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/147486" target="_blank">📅 01:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147485">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI_e25j8aVFdDf7XYF2n0oGDFF2uwwCemfhHfPSi16oyhvbwj6-lcLUVuOYaNecSWSJK-glBNAMrzRrGsA8Er7i9eEc1dzZlEUrjUf0D7sZzDKzMeLSeIDA0XXq1Js1kNNDELt151Nc_R9gF5Q_3DNgQozYn6jLIQMXdwnrntAFtupkE0T2YmZBGFvZfJT8tfJQO5fIchh6eVCNb_u5ygm_STKUjMrA0e5vxpcSmYO7O9UlW_wJWQg_rQBi6diT48tbFwm8spt9McRUKFQbxIj7FhhiIK2trM_M7gkKbEHp2DY36TyYE9OV6jRFd-f_dRxktZkSeGe_A1jJak3rQMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محسن رضایی: تا زمانی که شروط ایران محقق نشود، هیچ مذاکره‌ای در کار نخواهد بود. تمام.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/147485" target="_blank">📅 00:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147484">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
بنیامین نتانیاهو میگه جمهوری اسلامی به آخر خط رسیده و شرایط برای سقوطش فراهمه. گفته هفته دیگه تو سازمان ملل درباره ایران حرف میزنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/147484" target="_blank">📅 00:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147483">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
۲روزه تو سوریه شدیدا اعتراضاته اما فعلا کسی کشته نشده، عوامل موساد فعلا نرسیدن اونجا و تو راهن
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/147483" target="_blank">📅 00:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147482">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnEZPrd4v2I1G5wJhcIwc3zC7d5Gbxdvco4fE2kZuDQhazcbB_xdxv3Uqqvhi6zfFf495JHuJA8VIBqlu0_IKm2tkyOnnJFMCZznz6_OOAb1xZZAfZzjolfqzW5JSxParvl5rfN1JWUn-t7LAoXlq_iyYFchsf-lZELM5uQehlpvFKcqb_5hrgWxEliGNdvPOO58pEc9QhQ3-KW-PJ9staGPEeXjj0uGRfLYgsBAacNaBweRbj3KB953OwqHDC14CviPHpB1OeiSkVgcOohFIk3jm-XdIqg5B6ONN5KtJly29uUtLrvoMDj5aQi8Rwj-vhnW0Qz94U7gqfAxSsdvTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت جدید ترامپ:
من متخصص افشای حقه‌ها هستم و همین الان دارم یک حقه دیگه رو هم افشا می‌کنم؛ اینکه هوش مصنوعی قراره دنیا رو در اختیار بگیره، همه‌چیز رو ببلعه و نابودش کنه و ربات‌ها قراره وارد شهرهامون بشن و همه ما رو از بین ببرن.این حتی از ماجرای «روسیه، روسیه، روسیه» یا حقه تغییرات اقلیمی هم عجیب‌تره.ممنون که به این موضوع توجه کردید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/147482" target="_blank">📅 00:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147481">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MoP3Kqw6p40nD7F5R8SB-nlTo-WxF-5LVkB8iUHTM2AUZ9J6nAnVjjV9CkONpbM9Yfg_MG_4pEV9ItMmQDRen8qaUt8pIkb1CjbXtXTh5HTmSRmBaZHl-aA8xYyGeUCVZW6-1ASEeUrfp9O0825jS8SRO_k6hy6x2ENrsmUiGhK4izWQEb9wD82oNtk4gduRP1KaMqrKPtd7EuD1Fujfhc6LxZ6zOjl-M5vI-TyxO_iw0dUX22d3SFDSjYLUMM7oigoXmPVt2fyW5Yx4Y15_tz0tD4LGNw_w1xGwzvkm8AcsAYocE8yWZ7AG_62p0GU0M18ADjPfjdT6litat3-MSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همینجوری گذاشتیم تا حرص بدیم بعضیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/147481" target="_blank">📅 00:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147480">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534f93c783.mp4?token=Sh6yPQlIGoPsHJdq62eDJxRhewBiMByyQccTNIzcSmJk8ucw_CauD0m1rIfHCt8L-8nw2HNVKt9rhVchIpxP3JDbSN0KNuEHg4WRHytfAcdrO9IZJodXlFExwm_BLXIbpnPRjQ3cTLNmBH1tHV1Sep__5l5DmCSBpJ8vqlyWzDiiAnnCnHBtXAieBQ8lPEbusH1Za_UleNHRbi4OdUNhu8m6ev51qOaF1O2ZJMya4gNQ8xIm0tFWqBh1i1rhkczu1rMwt4MTW7x3sKhkmuSKKGs2TyP77wOCOcd_JnyQbZ5x1Y1UiHDHLlTL6dyWXF-j51mdvEeXoDbDK_9IpCgFZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534f93c783.mp4?token=Sh6yPQlIGoPsHJdq62eDJxRhewBiMByyQccTNIzcSmJk8ucw_CauD0m1rIfHCt8L-8nw2HNVKt9rhVchIpxP3JDbSN0KNuEHg4WRHytfAcdrO9IZJodXlFExwm_BLXIbpnPRjQ3cTLNmBH1tHV1Sep__5l5DmCSBpJ8vqlyWzDiiAnnCnHBtXAieBQ8lPEbusH1Za_UleNHRbi4OdUNhu8m6ev51qOaF1O2ZJMya4gNQ8xIm0tFWqBh1i1rhkczu1rMwt4MTW7x3sKhkmuSKKGs2TyP77wOCOcd_JnyQbZ5x1Y1UiHDHLlTL6dyWXF-j51mdvEeXoDbDK_9IpCgFZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یادی کنیم از این کلیپ تاریخی که چند نفر میخواستن با برنو، سوخت رسان و جنگنده بزنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/147480" target="_blank">📅 00:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147478">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2qS21tU2uCrWcjBAsDvejV-PrObsKeAcGkrLgXvV-hwrxE_lAQK1hE6dWwDvVkm6PdvbiLfa6xrLNRs0717HEfeBbh5p1V1SiKgHIOD3RoUO0PtjkylKxXThf9qA_nSPJdU40V8fYqcQzzrnXY6dAcizpJVBlIBuiqr7Zwb9AYxKpnUHSTdnmuhQhh_6viwmNL18AsOyVOzUPRyXU8M_sAbt-lw4yvilQFDwkRqekLVeoaP_0gpeCeGTiAbvmZCambxM9wJ88WuctB5ZPK98mrphRDaxqzlo5h0-EmHmC-7P-5TcbTdBOOIM9Zhc37ohzjkEcEh_CTdebtfuyyRkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سریال خاطره انگیز قصه‌های مجید به دلیل اسم بی بی دیگر پخش نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/147478" target="_blank">📅 23:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147477">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lw88TTilUvP3DTWDZ5HrbU8ETKx6F-0grbaYqeyDfpvoYQfse-TiiGdRBkF_E8_gG3qjw8pb6_Zzo8tRFqhEgOqifrnSfAM8Ak23uGtqX2crdKrMT1qyGHLt4cMmwJqk8GcD0XFKXg3v0dg28orbDleJluic7fEPDRP6YzfkE29YxTSs2jAxFcw1NkTt9SMayQYY8cr4YR814dWCAjPkpYI8EEC1ojbO1uaqgxkzcOhQeEYRYxnFwKGDtFX5flnEmUyqnTBPasCl2LqImRRd1PKI94YoFo0WKzTUnJ0JRqi1mrwl_bTO4b46j1EFWJDNzOggFf0Mwjq02fH-e1-VpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هویت ۳پاسداری که در بمباران آمریکا کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/147477" target="_blank">📅 23:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147475">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⚽️
🇶🇦
| خلاصه بازی استقلال و السد  @AloSport</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/147475" target="_blank">📅 23:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147474">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxpOWMTXtInw80BwXKFxE1Ho0pHWK5gNFqNCzkYUM9rFgm63uJGmzuCnNAFdKQrQHgSx_GAzFt6WiDbMYL01UQFhJwldEIS4_IG7i4N9d81sM9N9NzhQO7FjEReV07lhDQJEtbKouKfeiFEIQjXfw0nXTx73I5rre8OPZB7w2C91KlZIezuVw3HumAg7TwWoH-H05P7OrZ20HePupquf96_--dnaDnxg127ynkJEybKNE8yKOesis7cqJSjlG9mSPthlOo2INv6asD1i5HlRlvB8eeySliaP8QdifZGImoL2DaDwu_hLNmYGClDdZPLwMSlDzLOXIlubNjOr2OLU0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط، فصل جدید همستر هم شروع شده
+اونایی که از دفعه قبلی جا موندن پیشنهاد میشه که حتما این بار برن انگشتش کنن که آخرش یه کیر چیز ببخشید یه پول بزرگی میزاره کف دستتون.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/147474" target="_blank">📅 23:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147473">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">💢
بیا اینجا بهت میگه دلار و طلا رو کی بخری و بفروشی
👇
https://t.me/+cs85WnZxgpM1NjRk
https://t.me/+cs85WnZxgpM1NjRk</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/147473" target="_blank">📅 23:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147472">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXiP6qPgZ8Onb_Xh86752FV2Bb50mMvhSAxwj2LbI_7b82ZidDfx_WF9WLx-XBxDEMTpYSmzY6IVn25Kk7DejUL1higQhEZkeAEto8O3azxRgHGO7tzV5QEmsePgE0SSrKf1X3IQw2_88Czi-SVAud8wn59f8S-03EjjtqBXHYCzx7tLwOUCQuIpAedopYLO4amCxF90uHxp8FV-jzyFlWYZqhpYLGDp1Q2TNbuoYPcqtgX1JBtDIfQelBxMpPMCkjH-0tHZLfAaRZ-VjtX2kh-vx4A1wbc_DGrWrwKiOXMon-bCXh_WGI8GsntzZxXP63nfECS2q3tAYQc60Dghtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
کشتی نفت‌کش "ال گایا" که پرچم پاناما را یدک می‌کشد، ماه گذشته مورد اصابت یک موشک ایرانی قرار گرفت و از کار افتاد.
🔴
این آخر هفته، ایران بار دیگر با استفاده از یک پهپاد به این کشتی حمله کرد، در حالی که کشتی در آب‌های ساحل عمان قرار داشت. در حال حاضر، این کشتی توسط یک شریک منطقه‌ای به کمک یدک‌کش کشیده می‌شود.
🔴
ادعای نادرست سپاه پاسداران، نمونه‌ای دیگر از دروغ‌ها و تلاش‌های آن‌ها برای ایجاد ترس و ارعاب است، در حالی که آن‌ها سعی می‌کنند تردد کشتی‌های تجاری را در تنگه [هرمز] مختل کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/147472" target="_blank">📅 23:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147471">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
پزشکیان: نمی‌توانیم تصمیمی برای مذاکرات با آمریکا بگیریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/147471" target="_blank">📅 23:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147470">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQkG0mhaMufymipL6WxAo6uYRqghvNd1EYM_4oR3VVshtKXorhB-JsaSQ2nw0CNgtEUK8PTw-3fMI9wlvOuKZN2Eu5HgnHn2zABdtLnsAbPT5T_jPx1F-17dSadeVKkAzAHJbTPP5ovn8H_tE8bnxuxPkSgwZ8TtHKhfkUc-ZTNOXkwh-aLNByCdTbRAEJX71HPeFtkC5396e-5GpZR4DqvfIXA0h93YmnQ11RcqrmCkStjV-R42BOnf7wtXoAFLhLxShjVi4i6WfmfyTy8dJgNF4izPb9kuN_zIFVVasFX3Ccbn8IJSVXZ1pk3Qtr4fV9ioUXcbYYrQwV_bhPsaRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نظرسنجی کان: ائتلاف نتانیاهو و مخالفان هر کدام ۵۲ کرسی!
🔴
بر اساس نظرسنجی شبکه کان اسرائیل، ائتلاف نتانیاهو و احزاب مخالف هر کدام ۵۲ کرسی به دست می‌آورند.
🔴
احزاب عرب ۱۲ کرسی و فهرست هندل و زولخا نیز ۴ کرسی کسب می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/147470" target="_blank">📅 23:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147469">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
تا انتخابات میان دوره‌ای آمریکا ۵۰ روز باقی مانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/147469" target="_blank">📅 23:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147468">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBYGEqiNy6nI1ODAjH0rVxBIuPZi77U03G7OL9AVfVKuky1qCWXy8hr--hmYq1SCU6CsX2SkYf1lWTojFF2EEoPxVcv_ntDyEuiXUTgaYXRpb76TgNoB1lo-O9vrVnaEMP6Z7AF9EDthosI22XaJAPZQsKR3bVTSXi4Uv39uXKo-GoDlIXGWhDEWCN1Y3YKFqeiTFtMty3lTTVZYkjhDWoUKKTkpTS4SiTU2jOlajkrZZfjkWU_5DVOFHPXTCnauvaUEpJ99a8Cyvez2og8I6Kkx60PTbR0hof8_TWj4O8LKMsdh2jxrPvrnyIWBLsFakZ9obbXo7omI0W0Ld4bg2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور: اصلاح طلب‌ها یهودی هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/147468" target="_blank">📅 23:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147467">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏
👈
فرود اضطراری بوئینگ ۷۳۷ سپهران در مشهد
‏
🔴
یک فروند بوئینگ ۷۳۷ شرکت سپهران در پرواز مشهد ـ کرمانشاه، پس از برخاستن با مشکل در یکی از لاستیک‌ها و احتمال آسیب به موتور مواجه شد.
‏
🔴
خلبان با اعلام وضعیت اضطراری، هواپیما را به فرودگاه مشهد بازگرداند و هواپیما به سلامت فرود آمد.
‏
🔴
در پی این حادثه ، باند ۳۱ چپ فرودگاه مشهد موقتاً بسته شده و احتمال تأخیر یا تغییر در برنامه برخی پروازهای ورودی و خروجی وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/147467" target="_blank">📅 23:13 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147466">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
پزشکیان: آمادگی داریم در چابهار با هند مشارکت اقتصادی کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/147466" target="_blank">📅 23:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147465">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
گزارش فعالیت پدافند هوایی عربستان سعودی درپی حملات یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/147465" target="_blank">📅 23:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147464">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
پزشکیان: آمریکا راه غذا و دارو رو بسته. آخه آمریکا هم انسانه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/147464" target="_blank">📅 22:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147463">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
پزشکیان: با عربستان جنگی نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/147463" target="_blank">📅 22:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147462">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
پزشکیان: آمریکا چون نمی‌تواند رهبر ما را پیدا کند، درباره سلامتی او شایعه می‌سازد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/147462" target="_blank">📅 22:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147461">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLzbXtyjCAJLfVaBUA_UrHaYUNkRhqXX8K0i2Ae5jSptzs2T18FiM-Ut9noekR3jKSy8_Xp1ssr5X2t2Fy5jm-XSL5baAF9t2cxii343f5K_OBrha9ht51rrgJVL569XxG1d0Is-NvxlLmAWtbRDmdgHmjNkfH_r5T9D6kzY9_t9o1n9wRLU5AWW8cX3rf-GBOq4ZBkPbe_q8dRD-hmOQFklilRdkcMg-aoSJn8sb85SZtVPnwFeVvVTHCFBsTr0xqBf-GBRZRdO9HwDelrS8lvuA2OVYVck6PHWAkkerhXKAqgMj6jnXE6k-3YqxiXKqqhrm3QIMz_uqW9YmDx36Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتشار جهت حرصی کردن بعضیا
#افتخار
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/147461" target="_blank">📅 22:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147460">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9ELbT_4KICHNJ2Vom5s4AYtEN3SuzYLO5XjUKSUuskfReidI-rPmxifTF7psfEhC4nPqvFBm33gywg9PGu4iiXn34Pq3RxSDpvs5e6wVcJQZqMOg9PwFRe42SUrLuNrRDHqCDOjyerzQhq10S-7S8MN8L-TRY9-SIQskTv2XizYSLShFvZApV84GUnRLwzYPYr3SfYMnYr-n4WgbBxxycHcAyPCMHzISvHOABg6p7D3poXdni0F5_2hqOx3fSt1RHQZGSheQkr52AkHdGD8LuEHXxVgmPSusGRScX0KrwWk956zyDpXqSbc1AOzEriLz7vhQ2Yy3m20QSuhrKK0xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوپر نفتکش «الگایا» به شماره دریانوردی 9325336 که قصد عبور از منطقهء ممنوعه در جنوب تنگه هرمز را داشت،بر اثر برخورد با مین های دریایی منفجر شد؛ تلاش برای مهار آتش بی نتیجه بوده و کل نفتکش در شعله های آتش گرفتار شده است پیش از این نسبت به خطرناک بودن معبر غیر قانونی هشدار داده شده بود، نیروی دریایی سپاه با قاطعیت اعلام می کند تنگه هرمز مسدود و همچنان تحت کنترل هوشمند ما می باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/147460" target="_blank">📅 22:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147459">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
پزشکیان: مشکلی با امارات و هیچکدام از کشورهای منطقه نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/147459" target="_blank">📅 22:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147458">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FD7W20xhw1phZn6Rpxa847_HLZ1gHAOl-5D9BF5ZcweqInA7wAbqagaBcpZK3scUZl72dPbz_eEn_pQZP7i25lMUo3xQtM0oxotGIO91DjxR0yh077UttQnuwF_8Bp9quaEyUJr1NKrYWOAhiFph59W3HIEWpQ4D7Es2EWl8isNN8fgeB5iabEMPbdGYV28WOvCPXYbwC-AoCPcK_VM6Nn7HeJL9-XBuvqXUdFZyzgQPjDidxw4xKrlK54EK4wQ4XYm1NmFUnZ1tGHHedwRKqk9IuvL46NtO1_L3aEFBl6Md0rh5Wz_ZwZjdamP-rtImM5JQRO-LIrdjb3cUC7NODA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شماره ناشناس تلگرام ۹۰۰ میلیون تومن
🔴
شماره ناشناس تلگرام تو ایران حسابی گرون شده. الان هر کدوم حدود ۹۰۰ میلیون تومن. سال ۲۰۲۲ میشد با ۲۰۰ هزار تومن خریدشون.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/147458" target="_blank">📅 22:28 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

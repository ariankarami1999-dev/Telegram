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
<img src="https://cdn4.telesco.pe/file/TFVI06otTWwqb3qYvcO7VHKFGXtD7EtWSsg1kLAwT_t7qJ2E7Y0yY1KHmMutoPd2xfgPm-JO2NOwWYZ29S05au9Atroaq4cKUa67gPkewEOSGQXdbBWMzFiJO4x8vpCOBNlCgnjE6_nzAxkP9nDCHgHcMMKJz4r7DoN15e5QI5-hUlWjJa7TaIAAmKkgrN5BosaoF-G3N6ZxmQb5aPr4j34FyR1R7KnT-6RjH--XWyi-yRx9vWIMq34MZ8gfejtnwehzeBYt7JQyqjVuTkJ-9Xn6L9_g4h73ZZiu3aYSgGuy_du34h3XEnj5zCXJdUJWog8Wn74gjAGkW7hQMv0kew.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.5K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 11:27:23</div>
<hr>

<div class="tg-post" id="msg-19348">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grBDKDJi5WCYS5erOA2TQLjjbl6dVRBH0VTV6m6XHiN2AKfVfLRMOQcNGN6OOLKAhTJh0xhxt9w-smWxU_D5xqWM2_DoemOaIn5EIQxQy9dE2R7dQlY1gphJPrtpkPQv5P-7QLUNe3FlwhrWb5z3bACrSxh4RyPlrJy1Yh1WWuRXsBONBNXMJB_xZdC28dGN5tgxZjY5rxA8lfVZgKzp9-Hf9-jWJisFTeXePJ4g-2YQlPNTGyQu_JwejGvDHOKz5USgIf3iiWC-Wwwx6RCeBVH_4twjax4XfdqH3kOt7kI8hRSrV9qcvL2CqhKXh-zOo_9MuXq2Rj22X6uAra-F0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله دیروز یمنی ها به مبداء خط لوله شرقی-غربی عربستان یعنی تاسیسات نفتی ابقیق انجام شده.
سعودی ها کوشیده بودند با این خط لوله وابستگی خود به صادرات از تنگه هرمز را کاهش دهند که با این تشدید تنش یمنی ها روبرو شده اند.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 316 · <a href="https://t.me/SBoxxx/19348" target="_blank">📅 11:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19347">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ:
ایران می‌گوید: "لطفاً، لطفاً،  محاصره دریایی را بردارید."</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/SBoxxx/19347" target="_blank">📅 10:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19346">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc3554F2LmZeUm3I7noAZ9pQCnM44C0XV7XhXTKkqf-Yu7gjUOjRDv0KfZe4vP-DXI7LfLFqR8tf9qHAELWjvf9C3bAsl8BUmZZAqXGdHs5IAthwoc5wwiofDzi1D49LBe02c4jIm30ERdcziTtRPQSfRmd80iHSOy5Hto03WEWehm1BYO3bjMrWaRidS_odBlhXTNGBksLTXJAa1WI3jpfVMI_pGOM_E1Z1T8f9tZxzg7qjx5qcMQVzDdk7JCvhARrVux2q6E10Fq9pOsqH0tTwgsh3EaTYDmkaICfa984pZqsCpwf6SND1PSCKPo4ne4TGEfNmtRD7J48xhvU__A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه محموله جدیدی از موشک‌های کورنت و پرتابگرهای کنترل از راه دور به یگان‌های خط مقدم تحویل داد.
این سامانه پیش‌تر علیه تانک‌های لئوپارد و چلنجر، خودروهای زرهی بردلی، استحکامات و مراکز فرماندهی استفاده شده است. تجهیزات پرتاب جدید به خدمه اجازه می‌دهد در فاصله از پرتابگر و در پناهگاه شلیک کنند.
شرکت روستک اعلام کرد کورنت هزاران هدف را در نبرد منهدم کرده است.
موشک کورنت-ای‌ام با کلاهک سنگین با قابلیت نفوذ ۱۱۰۰ تا ۱۳۰۰ میلی‌متر زره همگن نوردیده پس از زره واکنشی، تهدیدی برای تانک‌های مدرن است. هدایت لیزری آن در برابر اختلالات الکترونیکی و نوری مقاوم است. پرتابگرهای خودکار می‌توانند اهداف را پس از قفل ردیابی کنند. برد این سامانه علیه اهداف زرهی تا ۸ کیلومتر و با موشک‌های انفجاری تا ۱۰ کیلومتر است.
تجهیزات کنترل از راه دور خطر قرارگیری خدمه در معرض آتش متقابل، توپخانه و پهپادهای اف‌پی‌وی را کاهش می‌دهد. این سامانه روی خودروها، خودروهای سبک، چهارچرخ‌ها و سکوهای رباتیک نصب می‌شود</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SBoxxx/19346" target="_blank">📅 04:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19345">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بر اساس بیانیه فرماندهی مرکزی ایالات متحده، از زمان اعمال مجدد محاصره کشتی‌ها به بنادر ایران، دو فروند کشتی برای اطمینان از رعایت قوانین از کار افتاده، دو فروند کشتی بازرسی شده و ۱۷ فروند کشتی تغییر مسیر داده‌اند</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SBoxxx/19345" target="_blank">📅 03:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19344">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رسانه‌های محلی گزارش می‌دهند که شماری از پهپادها، احتمالاً ساخت ایران یا تحت حمایت ایران، در اربیل عراق و مناطق اطراف آن رهگیری شده‌اند. هم‌زمان، سامانه‌های ضد راکت، توپخانه و خمپاره در اربیل فعال شده‌اند</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/19344" target="_blank">📅 01:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19343">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONveGHbFRPVNL23ZXjLSaox2Z8_zx9jYa-uui8kxyKHw6pMq_aGjZwXmVspWP5jkGVZW5JQY6WVXGnO4JSMmeHCnigp54Ks_VgyCsyB9NSVZJmiLB_1MzQ-pC6O5cr1ZQqO5OIhxIkIv7s-C-PC9I-Jab9aUsF7R3g1PM2wJCw9okDWKZyV8bSPHoZNR1y7yBtd59QdpgvMWBaHLNCE1oPKnGn7-LahytYQZMS53LxmMWtkUyUUaGljhtAmNr7BUOBlQfRyfBRvCrOZw5FQINGzFMGko9MwzSTLbKLSCtRKYMb1hMMmoCTC58Pj9G40TfV50VnQcx1veGAQF6TfXTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک بالستیک Lora در خدمت ارتش یونان!  به زودی، نیروهای مسلح یونان به موشک‌های بالستیک هدایت‌شونده دقیق لورا از اسرائیل مجهز خواهند شد. این موشک‌های بالستیک نه تنها توسط نیروی هوایی یونان بلکه توسط نیروهای زمینی این کشور در سراسر جزایر اژه و مدیترانه یونان…</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/19343" target="_blank">📅 00:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19342">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">عمده خاک اوکراین در برد موشکهای ایرانی قرار داد</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/19342" target="_blank">📅 00:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19341">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یادداشتی خواندنی از یورونیوز درباره ایزنکوت و حزب ش.  لینک</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/19341" target="_blank">📅 00:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19340">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76775f04b.mp4?token=kRn8fQSjTUhOQq9kJz6xrDgfh1eFhpoRCDvhUta0aP99V1k3M7Ksxv4yWwGbfdJIicbB1u_MS67bRbY3PVXPKDX1bCpDfOvsJddqEh1rf-ZGFOQHQ1begfEe9RiGgmELL93eBD8Y9LGTdjzNHi916dkURQ0G6z9zWXnXqu7LYVZsfXWme_11RvSkghWlZl8ewLUh8cHt5wWoVen0DQVUWsGvjgrQdfJuPxc6GRyFBrvx0FRFsA9XPRQyODMeJoz0vmnEL6KMVYHocqKAoZK1nwMsyTAtN8YR7wwMik-kvu8-nm2sjfz4QdpVAiC3yl4w4sQ3JCAxZFNjM-D3nRmnFiaTJgHyCYnFjzdjI1Nchd-IaDEuDVUKql2jrHU7fAAM0bd-kct9yeax_CCT4-kR0h0h6wWJAVQLseiE067DVo42QQk_TiW9WBtnoyWSlbAeArdjmd8IisrDvvytLgO4iIyG1hmZrPljrbL9B8__q9yWPqGfpbbue9Zrzn2Xt4AmYjDiFXZhIk_wKlBaARQsVTM28la949euLZ6s1gZa2s5kkS7-f8XHu1kR_91Cpq0TgfGcqE_ZSjQkNdyncrYuEAIgOfbKKvg0thLmlsy8syKfkFPpWS_WmNhpOhfygqGuYs1kqfeUWgL4U6tzttYH6L917WARM-sjMEO9oB5yBeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76775f04b.mp4?token=kRn8fQSjTUhOQq9kJz6xrDgfh1eFhpoRCDvhUta0aP99V1k3M7Ksxv4yWwGbfdJIicbB1u_MS67bRbY3PVXPKDX1bCpDfOvsJddqEh1rf-ZGFOQHQ1begfEe9RiGgmELL93eBD8Y9LGTdjzNHi916dkURQ0G6z9zWXnXqu7LYVZsfXWme_11RvSkghWlZl8ewLUh8cHt5wWoVen0DQVUWsGvjgrQdfJuPxc6GRyFBrvx0FRFsA9XPRQyODMeJoz0vmnEL6KMVYHocqKAoZK1nwMsyTAtN8YR7wwMik-kvu8-nm2sjfz4QdpVAiC3yl4w4sQ3JCAxZFNjM-D3nRmnFiaTJgHyCYnFjzdjI1Nchd-IaDEuDVUKql2jrHU7fAAM0bd-kct9yeax_CCT4-kR0h0h6wWJAVQLseiE067DVo42QQk_TiW9WBtnoyWSlbAeArdjmd8IisrDvvytLgO4iIyG1hmZrPljrbL9B8__q9yWPqGfpbbue9Zrzn2Xt4AmYjDiFXZhIk_wKlBaARQsVTM28la949euLZ6s1gZa2s5kkS7-f8XHu1kR_91Cpq0TgfGcqE_ZSjQkNdyncrYuEAIgOfbKKvg0thLmlsy8syKfkFPpWS_WmNhpOhfygqGuYs1kqfeUWgL4U6tzttYH6L917WARM-sjMEO9oB5yBeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راه حل قطعی پایان جنگ پیدا شد!
استراتژیست نابغه ایرانی — مستر قرهی — موفق شدند با استعانت از خدای تبارک و تعالی و نیز هوش خدادادی و سرشار خود راهکاری فوری برای تسلیم آمریکا و کله زرد ریقو پیدا کنند:
سرش (سر فضاپیما) را کج کنیم تا بخورد به آمریکا و مردم آمریکا ضد ترامپ شورش کنند!</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/19340" target="_blank">📅 23:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19339">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6eT2TRdRog1O09sbpIQsD6zDFiY5F1CjVEOC_XC_5CNFj5mZASKkT3RkwrkCH_feBaShnkGlE1X38DQjIUFZE4MEnYmiCEmn79G6ndMTNh9P5Da9qdYllQTHZQdvs7UNWqC6zM4CyFb8lJk-3BbtbUsugTBtSOyoJu6gSEXCYVtPBfE3A7jkNMr3Urtr1nVZkvoebXULBRgdkbe2v2HRIxlUaOsXeCxsCV6Pd2PsRjcqSKRUPi7t1S9BBnOeaaqBU5x5DLdTNNYH3gKUbN6mPeZuIY5_wzglKbXYfydOq7y7BKT8aLWkfvxngrMWjlzZwJWKNi52Px_zdCDvyS1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/19339" target="_blank">📅 20:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19338">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اظهارات ترامپ درباره ترکیه:  ترکیه علاقه‌ای چندانی به اسرائیل و بنیامین نتانیاهو ندارد اما ترکیه برای من بسیار ارزشمند بوده است.  به هر حال، ترکیه یک کشور بسیار قدرتمند است. فوق‌العاده و با یک ارتش بسیار بزرگ.  ارتش آن‌ها تجهیزات بسیار خوبی دارد.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/19338" target="_blank">📅 20:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19337">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دقیقاً طبق تحلیلی که ارائه شد آمریکایی ها نخستین پس گردنی را به اردوغان زدند و علیرغم همه وعده های ترامپ، گویا تحویل جنگنده های اف-35 به ترکیه متوقف شده است.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/19337" target="_blank">📅 20:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19336">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLSitPygeGoxr_AuXNpCCVIK6MhjTZPiwDLbskpcivLZ0Opr8OW2O_D0_FJsSJ7pN39OS7-_8o9UtnVxoB8-7K-2FX6viJ3L8qwMdZabIS7g-t81tqxHE_-l0hhDTswYSOj-xDZ7k2yzxrwkSAA-w7G-YYtw2ZZqCGPUQGFFrKBGQoU9CRRSbHD6jOJyULUNoIUdu0mZ-qH_zKc2euPJSi0G3LdAwQU3iZsmAQ_KmnIDHFzJ1nzE7TQKNd0F9HUEbfEUlcVsPAmmUCnnG0yImhd9-zAKextann9Ho1UA2FcHmAdXiVLsyZH8Qd6KXET9wf0S1Ul_KegBthkFhO6lVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه است و پیش بینی می شود طلا که در سشن آسیا با خوش بینی زیاد بازگشایی شده گپ را پر کند و تا حدود ۴۰۶۰ افت کرده و آنجا کف سازی کند.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/19336" target="_blank">📅 20:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19335">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پدرسگ ما خودمان دزدهایی داریم 100 درجه بهتر از تو.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/19335" target="_blank">📅 20:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19334">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ:  ما میلیاردها و میلیاردها دلار از ونزوئلا می‌گیریم.  این اتفاق با ایران هم خواهد افتاد.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19334" target="_blank">📅 20:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19333">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ:
ما میلیاردها و میلیاردها دلار از ونزوئلا می‌گیریم.
این اتفاق با ایران هم خواهد افتاد.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19333" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19332">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">عاقبت به خیری
😄</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/19332" target="_blank">📅 20:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19331">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/19331" target="_blank">📅 19:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19330">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R82mskY8wJdk60za3piXD4Mi834o7zIzaq14QtK7F-gufUJJuBfe8suaBnlNNzJzsLxMtBd-LwU929z11mjUfimjuadKa9haWIA2XXWxO_ZIKVm44m-JGWdUKrmOHTI9NmZ_Hpf-4My92_Fr-DigjK7beeGrSKsWUSeff0cEkOVi_7-FOLI5zo_ftqsBSKHTvNCY_AkY4EZQP_apmVTmZEohuQHPxEaJEVeEMLpyvPvf0FdMJ2hy5ttonwaGYqPh5c-TTRiiI1s7Z21WTwz1iCetg3CdnFFYz9H-b0W-3ji_0tIgMgdMnCVueSv6eyH9kf38rSff6ThhqFCEVKN0kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:   به درخواست میانجی‌ها به مذاکره فرصت دوباره دادم.   فرصت زیادی به مذاکرات نمیدهم.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/19330" target="_blank">📅 19:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19329">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ:
به درخواست میانجی‌ها به مذاکره فرصت دوباره دادم.
فرصت زیادی به مذاکرات نمیدهم.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/19329" target="_blank">📅 18:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19328">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">276.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/19328" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 13</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/19328" target="_blank">📅 17:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19327">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گزارش هایی تایید نشده از وقوع انفجارهایی در عربستان و هدف‌قرارگرفتن تاسیسات نفتی این کشور.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19327" target="_blank">📅 16:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19326">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IO59sbPdYM6yPoc9cw1OCWde69WbV9FO3SpDTd6XyBP4iL89h4HrjASjT6wxZyfdo2srIw5uEOjEeMHIBnnqBJX0B6_pwC2g8CZIBQm7gJ9wX9x1GEQlTn-y9nk3RzynSayiBQDbMqOrmxpt1OCtpHXH4x4pnLK2BTej78WiHuUVPhsJuhM-1fTYfYzwmLes5KENFN_gC1XR5zPzlP1YI6wTS0OVWtkOQxWmDSvkqYMbl2iRA22S-C3Gsd0TxEhJ52qEihgTxilz87WnEsIy7rHHKJaWyYqZufNRnCMcii7OJYAutkIxJY1zIM8z7ujtlYRqUsYfPhCbwRooshwAIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
بازار اوراق قرضه پیش از فدرال رزرو رأی خود را صادر کرده است
افزایش بازدهی اوراق خزانه‌داری آمریکا نشان می‌دهد بازارها با نگرانی از بازگشت تورم، کسری بودجه و رشد بدهی دولت، انتظار دارند نرخ‌های بهره بلندمدت برای مدت بیشتری بالا بمانند.
تنش‌های خاورمیانه، جهش قیمت نفت و تعرفه‌های جدید این نگرانی را تشدید کرده و باعث شده بازار اوراق پیش از تصمیم فدرال رزرو، عملاً موضع خود را درباره ماندگاری فشارهای تورمی اعلام کند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/19326" target="_blank">📅 16:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19325">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وزارت امور خارجه ایران:  «عواقب حمله به کشتی ایرانی برای شما غیرقابل پیش‌بینی است.  پیامدهای اقداماتی که زلنسکی انجام داده، بر چندین کشور در سراسر جهان تأثیر خواهد گذاشت.»</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/19325" target="_blank">📅 16:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19324">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">از اوایل امروز صبح، نیروهای اسرائیلی حملات خود را به جنوب لبنان ادامه داده و در شهرهای حدادها، تیری، مارکابا و تالوسا و همچنین در حومه عیترون، سری از انفجارها را به راه انداخته‌اند.  آتش توپخانه اسرائیلی نیز تپه علی الطاهر را هدف قرار داد و در نتیجه حملات…</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/19324" target="_blank">📅 15:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19323">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">از اوایل امروز صبح، نیروهای اسرائیلی حملات خود را به جنوب لبنان ادامه داده و در شهرهای حدادها، تیری، مارکابا و تالوسا و همچنین در حومه عیترون، سری از انفجارها را به راه انداخته‌اند.
آتش توپخانه اسرائیلی نیز تپه علی الطاهر را هدف قرار داد و در نتیجه حملات اسرائیلی، آتش‌سوزی در حومه تالوسا و مارکابا درگرفت.
یک پهپاد اسرائیلی چند بمب صوتی بر شهر منصوری رها کرد، در حالی که سربازان اشغالگر اسرائیلی به چند خانه در بیت یحون آتش زدند.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19323" target="_blank">📅 15:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19322">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
نتانیاهو، اطلاعات به‌روز در مورد پیشرفت ایران در جهت دستیابی به بمب هسته‌ای را به ترامپ ارائه خواهد داد.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19322" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19321">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 13</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/19321" target="_blank">📅 14:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19320">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 13</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19320" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 13
دوشنبه 27 جولای 2026</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/19320" target="_blank">📅 13:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19319">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🟢
پاسخ به توهم برخی درباره شکست احتمالی نتانیاهو</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/19319" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19318">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7Fy6h7HYDAozrb91EIeqi5S-8im-ir96mDMttfln0QD_IohgRE0YCg0slgUrbbRKq2nQOHVjSGftq0HYRYuKdXNCD12CmxbHVbFyV6vCU6-h92Dx2ZPmFZ3H8AfBR6wEBgg1T7c5oWeKodZf-t7eB2owgLWB5jlgbHsF-_xpmPYhShNMJAkHyOUGqWDrdo86BWkH1jYS86P7_AcKipfacV6IAfQucjSyS1KtvmgtNRJcrgDdRpLvgMZNRU8LUMYA1grSDrTG9lN2WMo5p6DzCQT80kjRBZ1i7vxfVg7m52YJQ2BqgK00aMniWPf_l-ZWNpnUt7Bf2JoV9z4b5izyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۸ سال پیش در چنین روزی مجاهدین اسکل خلق میخواستند سوار بر تانک های چرخدار برزیلی از مرز با عراق تشریف ببرند تهران را آزاد کنند که خوردند به تور کبراهای هوانیروز در تنگه چهارزبر و مارجین کال شدند.
#تاریخ</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19318" target="_blank">📅 13:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19317">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سخنگوی وزارت خارجه: چین نیز مانند ما نگران وضعیت صلح و امنیت در منطقه و در سطح بین‌المللی است.  هر دو کشور نگرانی جدی نسبت به استمرار یک‌جانبه‌گرایی بسیار مخرب از سوی آمریکا داریم</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19317" target="_blank">📅 12:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19316">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سخنگوی وزارت خارجه: چین نیز مانند ما نگران وضعیت صلح و امنیت در منطقه و در سطح بین‌المللی است.
هر دو کشور نگرانی جدی نسبت به استمرار یک‌جانبه‌گرایی بسیار مخرب از سوی آمریکا داریم</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/19316" target="_blank">📅 12:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19315">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19315" target="_blank">📅 12:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19314">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUqdiENZshp_q4_hqzYfIktZECK4OiFvcd_bspSSDKBdr2VWcKz10M2mR0We0xOJMo1LvDoMzYrdOCA7uKRQJkIxZSgLaEqat5eTlNqYYVfUMDNvj1HiMCC9r3brhOjauEeQYHfk3jfj5aThO23uTGBE14VdxFlSWOvH-meQPYevKmsvSjnBnuj5rOtMsOh4dxwwIRQXJL6fe30jivb0YlwSB8XfZItIupW51XLJeFXb0p0_3YdIV5k2NoX_JpiKWkga4iDbVEN0VMcXXCRLAUQNpLKwHziqofA2GE_MjqbODtDguJx6yCa1j2e9N4al13k_FkdrGpdAxLzikh2w_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه است و پیش بینی می شود طلا که در سشن آسیا با خوش بینی زیاد بازگشایی شده گپ را پر کند و تا حدود ۴۰۶۰ افت کرده و آنجا کف سازی کند.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19314" target="_blank">📅 11:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19313">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/19313" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19312">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گزارش نیویورک تایمز، مقامات آمریکایی نگران هستند که پوتین و شی جین‌پینگ ممکن است کمبود مهمات ایالات متحده ناشی از جنگ با ایران را در محاسبات خود برای اقدامات بعدی‌شان در نظر بگیرند؛ این اقدامات شامل اوکراین و اروپا برای روسیه و همچنین تایوان برای چین خواهد بود.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19312" target="_blank">📅 10:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19311">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZpQQrP051S-KFfTfSqMUtE_hL30UuP_aW8lqMDfn4vmYnSDMYYKs7XWooRtAsU_CmfTlKWU_PBvoPIDSDHqm6WE6mae-XSNAkRbQQAgDCfH55RTj74DF6UA7LJ_y-wz6mg5z97wkJxycYaB1Z8uFekuqHLvIBf-G48vcBKKUTpOofcLFAUH9QrsiDl9TMSObgzdq3agY077B5yqHfHSkbgc5usP4xa_RHQOfHXKY1iXWWB_KRlowl6Ciz2sNkRQwNkPC0tKab_hx2ao_20SrpMEcrKTP3AiRgLOOlBsCpxhyQ5-vC998-bnR-qMD2GJhqU8AaGr4j-zU16Vg0SoDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حوثی ها و اخلال در مسیر جایگزین صادرات نفت عربستان
با ادامه تنش‌ها در تنگه هرمز و دریای سرخ، عربستان سعودی برای صادرات نفت خود بیش از گذشته به مسیر دریای سرخ و کانال سوئز وابسته شده است. ریاض از زمان آغاز جنگ با ایران، با استفاده از خط لوله شرق–غرب، بخش عمده نفت خود را به پایانه‌های دریای سرخ منتقل کرده و صادرات از این مسیر را از حدود
۷۰۰ هزار بشکه
به
۴.۹ میلیون بشکه در روز
افزایش داده است؛ رقمی معادل نزدیک به
۵ درصد عرضه جهانی نفت
. از این مقدار، حدود
۳.۵ میلیون بشکه در روز
از تنگه باب‌المندب، عمدتاً به مقصد آسیا، عبور می‌کند.
اما حملات اخیر حوثی‌ها به کشتی‌های سعودی، این مسیر جایگزین را نیز با خطر مواجه کرده است. در نتیجه، بخشی از نفت عربستان ناچار است از
کانال سوئز
یا حتی با دور زدن
دماغه امید نیک
در جنوب آفریقا به بازارهای آسیایی برسد؛ مسیری که
۲۰ تا ۳۰ روز
به زمان حمل‌ونقل می‌افزاید و هزینه‌های حمل و بیمه را به‌طور قابل توجهی افزایش می‌دهد.
در سه هفته نخست ژوئیه، حجم عبور نفت از کانال سوئز به بالاترین سطح خود در
دو سال و نیم گذشته
رسید و انتقال نفت از طریق خط لوله
سومد
مصر نیز نسبت به ماه قبل
۵۰ درصد
افزایش یافت. با این حال، محدودیت عمق کانال سوئز باعث می‌شود نفتکش‌های غول‌پیکر نتوانند با بار کامل از آن عبور کنند و ناچار به تخلیه بخشی از محموله و انتقال آن از طریق خط لوله سومد یا استفاده از نفتکش‌های کوچک‌تر شوند.
در همین حال، ایران پیش‌تر هشدار داده بود که در صورت تشدید اقدامات آمریکا، ممکن است
باب‌المندب و دریای سرخ
را نیز هدف قرار دهد. به همین دلیل، تحلیلگران هشدار می‌دهند که با محدودتر شدن مسیرهای صادرات نفت، توان بازار جهانی برای مقابله با هرگونه شوک جدید عرضه کاهش یافته است. در شرایطی که قیمت نفت برنت به حدود
۹۷ دلار
رسیده و برای مدتی از
۱۰۰ دلار
نیز عبور کرده بود،
گلدمن ساکس
احتمال افزایش قیمت تا
۱۲۰ دلار
را مطرح کرده است.
#ژئوپولیتیک
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19311" target="_blank">📅 07:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19310">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7U5F38MPLDbxBWvE38GRe5Cd8bHH9KS2e3MigHcGwpQyp1OiXE_8Ef7gmulbmrmpXcTnmwC44IrzBhzyW5ZFvQ83wHrjyxXRcZpFQKrORj6BzDngKhSrbNC0uX9xlCLk2Y-w7_mDPvERtE2AkU-upPLEzPHNFxzvNxYjM3TmlBZOATfwXBT_tODQXljghyF0JFi9RZ1EVcSVlZBatPm79juTJUHCyAlMH8j60vWjxo5ll8BApYGUY9FmtxN22fVrdrq6e01ayEZzagmpaqJN0maZlUCu3v01L6FOi85s6Ad0s3JueRbw5vCLdptdGoojJ1Aeom_VNswm-EjDkDblg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکونومیست:
برخی از حاکمان خلیج فارس به صورت پنهانی به ایران پول می‌دهند تا در آرامش زندگی کنند. برخی دیگر در حال عمیق‌تر کردن پیوندهای دفاعی با کشورهایی مانند
ترکیه
و پیوندهای اقتصادی با
چین
هستند.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19310" target="_blank">📅 02:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19309">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">روی کمپانی Boring ایلان ماسک حساس باشید. فکر می کنم بزودی همه ملل به سمت انتقال دارایی های حساس نظامی و حتی اقتصادی خود به زیرزمین بروند.  موفقیت نسبی و کم هزینه مدل عملکرد ایران و حماس زیر شدیدترین فشارهای نیروهای هوایی برتر جهان و گسترش استفاده از پهپادها…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19309" target="_blank">📅 02:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19308">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">شاید هم زلنسکی دارد جمهوری اسلامی را تحریک به پاسخگویی نظامی به اوکراین می کند تا رسماً پروژه تسلیح گروه های مخالف ایرانی به پهپادها و ریزپهپادهای اوکراینی را استارت بزند.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19308" target="_blank">📅 01:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19307">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ابراهیم عزیزی، رئیس کمیسیون امنیت ملی مجلس شورای اسلامی:
▪️
هرگونه حمله به ایران همیشه هزینه‌ای دارد و این موضوع امروز نیز صادق است؛ آمریکا و اسرائیل به خوبی از این موضوع آگاه هستند.
▪️
اوکراین نیز ممکن است به زودی درک کند که ایران اقدامات را بدون پاسخ رها…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19307" target="_blank">📅 01:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19306">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">▪️
لیست کسانی که اشتباه محاسباتی داشته‌اند همچنان در حال افزایش است</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19306" target="_blank">📅 01:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19305">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19305" target="_blank">📅 01:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19304">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K82aTGYnO5S31NT2WEO5zn1AplCZt0yxxG4mzmFrm6MD7-51K9KCUJ9TRiVtqvNURZkv75Yf4ZnfMT68srhYwBEKbVUIf17DfaU9LPn7HrbsfZ8IsDt20_xY9fLmCdSKvBaQRoF7ZgSfwJVYi8FF-89BFn_qKdPqPH5DELhACNvNWscaVOKQNOyv3zinxdZxrySMJin93JWgYE2k6ZdXCd0gZ43EmkfplTH-W7Hv0azBt2ag_o7n5tWrz5HM5C_qjmAvPXuNfDOf9oWwCYJ3EcIlu_Cef0whtilu6Gatd87LqbsOuCZKC1v9oWr1CTAF6AbKJ4FQT81IzhJRVKcMmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشایی نفت با گپ 7 درصدی منفی!</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/19304" target="_blank">📅 01:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19303">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOFbMl3GMSkrMxP1n31lebwf6MSzPrpJnH1wvA-fcQ-YfEnA36PZ-OfKu8mFFVMRUELr-g9Y7beEkKeOkXwVxZdPW3lX7n35e8mEstihOpuINOO9YbdBBTJiECfRj7OPXYhu0uXN9oyUyozOflPvhGWUZOgvtFyv4yX7ogKPPM9wGZP25wU8FpH4VLDK8Od1oQmWTa7HPfiLQYrUpdRAUOP2LaudCCwacrPooAlt7PFEQxP-TdnI_bg8obtGVQobmtsSZkAAhONDO5tGsBnBTbp4Ct-SOtWj-1k1SnYlTT-EUmDYisjuQSr4MwgQlUvxGSoAidgFtrH2yIDgK7ML_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از جنگنده جدید دوسر بدون دم توسط ترامپ</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/19303" target="_blank">📅 01:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19302">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLBbm6c4ssdGiDXnJsqd3EDKWJ1OTMIqKTjMU8SSS-PI0-rGgtMNprznGurQHd8DKk-n-_osNrDTLnqTmS1SJ6MJKSCtjj5YQ1F855PXDd8JlZLngYs1yB9MWX0crX1aIUXuVxOWDLO9TnNUEy-kwo5NyOIwYIH4-paH6m0KU_S_T8tZLwiUOx9-fsiY7Aa7jyTXVaD-nJKCKXSc6Eipv_Uij1HU9JSfKn2EXluG6KJ5rjZmJtqvygYpDnautKwLrtfRMj-fCYyrEa0j8Sk36iKmhZNNiWThvdeszmMBJcvRQXr0PDOT-Mt3Mtw-7kQZagy9OWhsJW4IUeLGmF8nyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19302" target="_blank">📅 01:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19301">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkJB4ZbFYdLPNode5Cb2i7achneZ7rcHO40XhamYFwOQvMcPEahDLnHtDyyJvPYPCjpKb8Kb_yot0QPy0auDrZeZrWwz1CuSj2RgssmcbwFqPNxyYQRMzyBjSGi0E4qUhbgkCtkpUQkPCaZo1BYeeMxXuvO3-g9jTiNdfJrp2Jo_ZbjeZSgz2v6XX3ewT9LoZg_6hKb9jzQ1TK0PFcXxvU90MReJ2J_sE_KEunUClF8CzYrlzKprbyKa7prB5cSDdI_3Ic-PS9Ttcws_RWR3MfTlr-pxFJcNaUfrMRGN5tQC5dUu1VEIAgwjh6OODHffvl-G6XjTTULkQrKHsFwO9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ول کن نیست!  اشاره به زدن موتور نفت کش های ایرانی که می خواهند محاصره دریایی آمریکا را بشکنند</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19301" target="_blank">📅 01:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19300">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رهبری ایران در نامه ای کتبی اعلام کرد:
در برابر اسرائیل و آمریکا راهی جز جهاد و مقاومت پیش رو نمانده است.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19300" target="_blank">📅 00:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19299">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وال استریت ژورنال:
الکس هولدر، فیلمساز مستندی که به زودی درباره لیندسی گراهام منتشر می‌شود، گفته که این سناتور در هفته‌های پایانی زندگی‌اش به تدریج خسته‌تر به نظر می‌رسید.
وقتی هولدر پرسید که آیا او خوب است یا نه، گراهام پاسخ داد که برای خوابیدن زمانی ندارد زیرا هنوز باید رژیم ایران را سرنگون کند، به میانجی‌گری صلح بین روسیه و اوکراین کمک کند و روابط عربستان سعودی و اسرائیل را تا پایان سال عادی‌سازی کند.
بر اساس گفته‌های الکس هولدر، فیلمساز، لیندزی گراهام به تدریج نسبت به هر دو دولت ترامپ و هم‌حزبی‌هایش در جمهوری‌خواهان به دلیل جنگ با ایران ناامید شده بود.
گراهام گفت که با «تعداد زیادی از افراد در داخل» که با درگیری آمریکا مخالف بودند، درگیر شد و افسوس خورده که مقامات کمی از دولت به‌طور عمومی از این تعارض دفاع می‌کنند.
«تعداد بسیار کمی از افراد در دولت این جنگ را تبلیغ می‌کنند. من شوکه‌ام،» گراهام گفت.
هولدر گفت که گراهام همچنین پس از اینکه رئیس‌جمهور در ژوئن یک توافق مقدماتی با ایران امضا کرد، از ترامپ ناامید شد.
در مصاحبه نهایی آن‌ها که چند هفته پیش از مرگ گراهام در یک مغازه باقلوا در کلمبیا، کارولینای جنوبی انجام شد، سناتور گفت که ترامپ بیش از حد مردد شده است.
«او اجازه می‌دهد این موضوع از دست برود،» گراهام گفت. «باید بروم و با او صحبت کنم.»
در اوایل مارس، لیندسی گراهام پیش‌بینی کرده بود که رژیم ایران ظرف «سه تا چهار هفته» کنترل شهرها را از دست خواهد داد و مشارکت بیشتر اعراب «تکانه‌ای تقریباً غیرقابل بازگشت» ایجاد خواهد کرد.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19299" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19298">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qi4qf6xN4ofXBJUBKrGSFngG5I6f4IqNiZDP2r0UOxK9vh6nXyiffDtkBok49zlyuCHsCMlGldUz5JLHSZ0LCJU8wBznOQYpImWainhYBn6oj2Uvu4REn7kuk_7PQ9sgNWmoBNdGlgyeTUN24F3klw76_Sk3J9D77tdTipNDF9XfHogk67a0jmjhIYLbVEw-DrVPuU1HRjIomH441Ur-NXDJSc-48fQWtcnEVjSlX5zDP7ZX_zXreCym2Fb1irzZjB8wO8y42plUDaF57UMg2jICD1nVp1TD21OGpg9el9T_XR9WZdCJSaNzoMu3LsqE1IkKdcakd3iXyAj1awBXvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آن عرب ها کیستند؟!</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19298" target="_blank">📅 23:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19297">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgDatuApFebjIV_b_4HgxtmoFrz38gwjoEqR6ZsixTSL20q1vcbK-r5rj7ZrjODtQdohYX8ioVRN2TVpHcixl4nDic9m2XuoeBv2mKeNdnQJk2gQQJO0C6bGGCggze40AOaLI8kO789cd7qkoOkoOObWY3JlNrlR47k3dQPvyPIJcRwpp2ZHB7ANfU9vm67QbRruTPfJZcbEpuWnUmlQiHOwlXm6Bid2vJVYt-JfpVr0BCwJcajeRNOGKBJSDeOo70ZgyIJh3nxhoeb8E16N7klW5snNf4Bfp7c2tIQq7L2RIHjwHcyUCcuBlyGmPHo1z_kh6nSfNjjYzGl5VXrQ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/19297" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19296">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q297MvqbkiLAAqOWcB0OhL5tyv7iff7EeX0V4jJXT8OVgkWzAK5XLhiFo5uXFr-kZ576P3h2svnmtktH0cPKWYALa9uK7eEho4Rh9ERr7jH9sgLJomHTwk3OAIrKFlWZgU2SJc3m5CBrsw2lZIFlprzJqqXMii6UflsZG95cShdmnJVMicJsdYFKve6YuBCWN15zAG1Gp7p1OPdtbxDzDjDBC7AwF9MJHplkLaX-AiBB1m3PB6p6QyQeNWqxH8buxrlnF8VcvnoPBvmPuwjVWKD7JpoGOkKCLLjohplWuRnFO5nPJgxxeLkcSXR-kOnJigLWtCZ6tLgrtJdCUEWtKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/19296" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19295">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">قشنگ دارند به نتانیاهو پاس گل انتخاباتی می‌دهند!  میانگین IQ وکلای ملت را دوست دارم.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19295" target="_blank">📅 22:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19294">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نماینده های مجلس شورای اسلامی با لایحه ای مبنی بر اینکه که از امروز تمامی شهروندان اسرائیلی اهداف نظامی مشروع محسوب شوند موافقت کردند</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/19294" target="_blank">📅 22:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19293">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نماینده های مجلس شورای اسلامی با لایحه ای مبنی بر اینکه که از امروز تمامی شهروندان اسرائیلی اهداف نظامی مشروع محسوب شوند موافقت کردند</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19293" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19292">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbMp-aVyhcK346zIC6LGtiau500lF7phxdtKln6hhZ7gyyz1EuBWXK2XMLfaYXT2l5DBCdH9vXcAooU7Nmzj35xo8nfl7EkkEoh3C6EH7VZnQ2F--f4BPewWnzVgwOQvEvL3oDPyB91PU0R911UtLujXOmkbxn7Q8CpvlqfJPFJac1HaWtbSPABQTw_nkAuQj2SqL7uz7UxGbM_ozZLmJA9RfIdemjL-LxAMLCi5lb9qE0DplVgcmdqc8Bbu7eFypGf6kc_PnolfMS9mDhXxMRcb3AUaaCWhpQZwgIG4nRXWBBZukzJIXn1i8LNKnDfH2gp0z5yadmYvQ8EDCZe-kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نایب رئیس اول مجلس ایران علی نیکزاد هشدار داد که «عمل گستاخانه دولت اوکراین بدون پاسخ نخواهد ماند».</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19292" target="_blank">📅 21:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19291">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFsRsrACpEpONRrbeASKZPwNzBMLCGUFgPJsfrI9mnv4YCV51ZaBtrtqJDoey_v8HnLO-cmuZEa-qpQQj-WJxLTDSsQPF3nvLP24BLwP4kLsGTmViYuK9yj_LAcuJtYRTuqd-L7vPnP6qOPHxkYGVTLrGhgGM3dBTF6P8ys857H5ltqKKzGzLbr_RV2f2dKJjituTx1R4MYCC91V7kIwO6mHQZ9_qPPOHsgnLu3y_4-CDARDbgd_alDyIr9HIs0JKSX8Au2SeuBQskAyF1WGFcX7IgOB_UaFZBv5oXgtqjry3mtcJoEY9i9QWqOI37xwC7NwqkVCKDZwQMoXbj2yFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انصارالله یمن:  یک فروند پهپاد آکینجی متعلق به ارتش عربستان را بر فراز استان الجوف سرنگون کردیم.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19291" target="_blank">📅 21:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19290">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آکسیوس:   فرمانده سنتکام «برد کوپر»، توصیه کرده که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به حد نهایی کارایی خود رسیده است.  به گفته این منابع، توصیهٔ کوپر (فرماندهٔ سنتکام) به همراه مشورت‌های دیگر مشاوران، بر ترامپ در روز جمعه برای توقف…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19290" target="_blank">📅 21:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19289">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سپاه با زدن پایگاه های زمینی آمریکایی ها در منطقه به نظرم دارد می کوشد تا تاریخ حمله را به جلو بیاندازد و نگذارد آمریکایی ها بسیج و تدارک کافی داشته باشند.  وقتی می دانید حریف می خواهد حمله زمینی کند خب طبیعی است پایگاه هایش را بزنید تا نتوانند آرایش مناسب…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19289" target="_blank">📅 21:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19288">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWDHxMYpB4DeT8EdKf8s7pTg517WheAaENbMoiRh5xGegRCjC_8NuCxt778JmWHgdAl8sueZ3piPpEB7V4XfAeK7bVZQW2UxJwzV8AXKSxx5s6h33dAEWxIVIcBeyiG6wOlvzb-YAKxQyNMsUnZtSpeS6WTJiojfe2WjxUpj8RJM5OQ1L0mPQZcankdOKTmcIocuzTT-_lyR27z4RQMZWJUvOXmrrpF2TtU088TQtSU01HBz4sik6N1Flr3mJZBgyVo5Ehi7iVdJOu99fH7ogoSFr6Hh0s5X9zGra8N8Ftgjglp38bazzssKQS38bOWpePlXM8b0Icg_hKF3JDZRQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت های پیشا—گشایش نمادهای مهم در بازارهای مالی
ریزش سنگین بهای نفت برجسته است.
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19288" target="_blank">📅 20:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19287">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">عراقچی:
زلنسکی به دستور اسرائیل به کشتی تجاری ایرانی حمله کرد تا اروپا را به جنگ بکشاند
‎</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19287" target="_blank">📅 19:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19286">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وقتی میگوییم اندیشه چپ باعث زوال عقل (و البته شل شدن ناموس) می‌شود یعنی این!  شاید فکر کنید این صفحه دفتر دیکته سید محمدطاها ۶ ساله از مندآباد باشد، اما نه! این نامه غلامحسین ساعدی به معشوقه اش طاهره کوزه گران است.  لابد با خودش فکر میکرده چه کار بامزه ای…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19286" target="_blank">📅 19:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19285">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2vMpi1Z135BHoM2NmSEYWTybFbcnSXRNaTEle65kfPA8apmvwdSVm2Cy5pKhkr2-CIOR9HX_si1Bm41-VgeoOd_oMSFHFPPmxkq2lczDDpCBODa92ZzvHoBhO6wnDafVSXbZMnfmrjvWvhKeFbd0irf4GQTcKhERAVvSSfj3sUfjEEs-Wnw0TjtPjeOufVOGfAsfyBYcw59yXq0So5ufDHZ4jGNDYvcbr9F6z_8QKGHGxCbQP_7NBBdFwUuDE3a5jAsmqlfKkxQHGYxbH8TSLhMecFEe1Ec_Fsl2fUdPrmRqzUA1zRTdCAZOPqLefPd6mRz-b2Ktb5cdSN7d-vVnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توئیت عجیب عضو کمیسیون انرژی مجلس:
فقط نفت!</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19285" target="_blank">📅 19:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19284">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9sdorrAuEKlsG2curuqmaEKsDR_Yb2mvaBeeE7Sc7f2Yxh2hVBPLZJZ3BZ1p_tKew9f3OQwZpSIPc-EvrjUvZgSt8ILuaGWArU42DhYFjhOZb2xeuylV4q_rJk6PQ09XG2e_gb3Nsl8zYEUnOJcAMc9FWsburvecLe8Z8NSlsaNUBvtMZttbQjI35c_gx2MLGSSMFoC7kI7li1AlLorSQykzogNZncIuI0Mb9n35gwHtxyUgeb6kPGKx9B83_dZ5W1KNBG00rXygtJ_hxp2FJZgKwnzP1D37Wi4SU8xsM2nvcMcIdHW-YBVLc01k0vyhaXF-NxYHp1ob6DQ88hXaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استالین و بریا!
بریا رییس سازمان اطلاعاتی شوروی در حین جنگ جهانی دوم بود که هم حمله هیتلر را به درستی خبر داد و هم با سرقت علمی از آمریکایی ها، برنامه تسلیحات هسته ای روسها را به نتیجه رساند.
جالب اینکه او پس از مرگ استالین در سال 1953 اعدام شد!
#تاریخ</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19284" target="_blank">📅 19:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19282">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نتانیاهو به فاکس‌نیوز:
جنگ زمانی پایان می‌یابد که نظام ایران سقوط کند یا چنان تضعیف شود که ضرورت پایان دادن به برنامه هسته‌ای خود را درک کند.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19282" target="_blank">📅 18:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19281">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d5b002cb.mp4?token=dX9DIvyARLdQDI4WOilZp0nKfeCZbr2kxXcKJ6jwwgC5CMacP-jPnXXiTlJnWx97E7QCI9CHk5jJIM4Zc6j4vusfiNP0-q63eH3guHNJWjDkWLypdXy65BpMwoKq_glIbJu9bCjkDKL0lU_k2KuwzAwMA083IKxOaSL8m-mDAdkCDkZHLEsWlf7YBDwwYjap33e1akIFxszL7Z9jLFX6mPcCaaA5p6IBtTkQo5k83yOrlh2EedW9epk0A86HJxOgnzX7C7d9hEFmWaX0FeQkLmEEqYVdInZ_nPvRoVJmp6t9SxtGM4GpOQtSCpUcC_AXlzF9plL80BoBXXoZWuka4yHJauaSdCPUivqyb9sa_pGBCtLhiXFf5jNSeF5NEvrfYSWKH2eF5wpGFsJKlW9fnp0Gx8omUChX-uC5V_wprm7DRLjNVM3ikzEjhUpd_qNF_tpkTzJNBuPCP3S6HFteCz0H_Qjsz6wlxcEGDzjv7Kv6hfdo_zULk8Y_vhJ3ONahb3qwD3p9h1BgMhAfV6GCEuK52Co4z31QJAqCf6yrtnfj9VLoK0fcKv4vTuU_zD1mziVe2wnfg0hl9_NFMGzRZNzw6MbaYvHEkmCOFwFHYqcVwi4htIDG8IxQvdW-ikILRxceR4F5FCc79U3BXTORmNL8_K5SMMk2yiM5HojWkPc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d5b002cb.mp4?token=dX9DIvyARLdQDI4WOilZp0nKfeCZbr2kxXcKJ6jwwgC5CMacP-jPnXXiTlJnWx97E7QCI9CHk5jJIM4Zc6j4vusfiNP0-q63eH3guHNJWjDkWLypdXy65BpMwoKq_glIbJu9bCjkDKL0lU_k2KuwzAwMA083IKxOaSL8m-mDAdkCDkZHLEsWlf7YBDwwYjap33e1akIFxszL7Z9jLFX6mPcCaaA5p6IBtTkQo5k83yOrlh2EedW9epk0A86HJxOgnzX7C7d9hEFmWaX0FeQkLmEEqYVdInZ_nPvRoVJmp6t9SxtGM4GpOQtSCpUcC_AXlzF9plL80BoBXXoZWuka4yHJauaSdCPUivqyb9sa_pGBCtLhiXFf5jNSeF5NEvrfYSWKH2eF5wpGFsJKlW9fnp0Gx8omUChX-uC5V_wprm7DRLjNVM3ikzEjhUpd_qNF_tpkTzJNBuPCP3S6HFteCz0H_Qjsz6wlxcEGDzjv7Kv6hfdo_zULk8Y_vhJ3ONahb3qwD3p9h1BgMhAfV6GCEuK52Co4z31QJAqCf6yrtnfj9VLoK0fcKv4vTuU_zD1mziVe2wnfg0hl9_NFMGzRZNzw6MbaYvHEkmCOFwFHYqcVwi4htIDG8IxQvdW-ikILRxceR4F5FCc79U3BXTORmNL8_K5SMMk2yiM5HojWkPc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی جالب است؛  از 6 کشوری که شدیدترین بحران های انرژی را تجربه می کنند، 4 کشور در منطقه ددخیز خواهرمیانه هستند و 3 تایشان (سودان، سوریه و یمن) در ژنده پارچه ای که به عنوان پرچم رسمی معرفی کرده اند، رنگ های نجس و نحس پان عربیسم (سیاه، سفید و سرخ) دارند</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19281" target="_blank">📅 16:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19280">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بیانیه وزارت خارجه در محکومیت حمله اوکراین به شناور ایرانی در دریای کاسپین!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19280" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19279">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">با این وضعیت می‌شود فهمید چرا ناگهانی تصمیم به دوبل کردن قیمت بنزین گرفته اند.  وقتی عرضه سقوط کند، کاهش تقاضا با جهش قیمت یک گزینه است.</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/19279" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19278">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFatLuL_tefEYMPmvuDEtl8Z7uouTgdPtviqlFm02Vrssjdv_mllJCnyBmlmw3Coo2ojfHZ8moV__3lXXD7aP5DRql69lzvUmr2vLD10nIlyL63LfXxwaK1xScCMGApOypV1CRWpjlBmoeNJfUfZmIfzyRiQMW3Wjm3dtZqCgDLX7ScdI3NqMG_180exnnAqCUMrTcElwnotqQLWVzjHwwpdzBMpGzeC7Va4gtDbBdUwZVHt8QE2cn1s5A3epkOnRk7nyofdDDUmtzP-iG7sc80ebdZFGmCWscyslj0HV4Abr0GO-SEF7bH1ULJKJZWGnSdswlnmhk5Twj-txdtnhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روس‌ها نوعا عادت دارند انتقامهایشان بی رحمانه ، مبهم، نامتقارن و شکنجه مانند باشد.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19278" target="_blank">📅 14:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19277">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">روس‌ها نوعا عادت دارند انتقامهایشان بی رحمانه ، مبهم، نامتقارن و شکنجه مانند باشد.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19277" target="_blank">📅 14:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19276">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وقوع دومین حادثه دریایی در دریای سرخ
سازمان عملیات تجارت دریایی انگلیس از دریافت گزارش حمله به یک نفتکش در آب‌های نزدیک سواحل یمن خبر داد.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19276" target="_blank">📅 14:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19275">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">برای نخستین بار در جهان!  کشف قله تنگه هرمز توسط اژدهای بندر</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19275" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19274">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312e3c4284.mp4?token=VHy9xLPblI3uyjlCF5S6O9hg_5iCYQLEqsLI-rehYlQKphV3zm5pieROnaivZaLMOJ6qOk6puLnUumxhOVG7lqv19AzFocLXtNEnMIdm0RqyTxNF0M4lEIl67qDm2qNc3QI0aeKkK9bjqfdtDOogfHR7nuiVXKgzUL16-gdTE7edVIAqaBunnY9Q2fKzmKigyHSNX07XyMhlqIeMCOVeC614XkSWxchBXgXQcj7YjIIxN7Rs2I-QXkwLTUxhR42A9zTh4t4qemw_LoWDzivPkT4vC_KYnakw-SLXlMHTKyacIt85C6iMokteniS-qpuHIV8JWy94Nf9ZKcQtXiptt2uoWjSa8kfiCFNViQYigVUZRAneJy-rUHYruqF-JKszSvpHvnIRYSovqTEVfvnlBATFnxb0Ghhf0zcVKGd23DouWlQ7mOH-paQSUDMFqh99VP5q9Tutr50G22HWqSsxPMGmDZhXWNvJjxh2gUmeFQ8NX42PFL63TEEO_rzmgP0_GUmj7h0RyDaMcIg-RcXejl0F48xdkrTsSeEHD0_sUC0AKsd-wHbJbHk1G7sn2ocPadEIz-SP476_x0tDKeFIW5sCV1LsyZoWmG4a8Mtk9uEaHkWCCOO6FVRhP1i8oHSxUDJLLJcp2lzVj2FjLNQ-FAbtfhjUiMFRbjoEsKh5aHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312e3c4284.mp4?token=VHy9xLPblI3uyjlCF5S6O9hg_5iCYQLEqsLI-rehYlQKphV3zm5pieROnaivZaLMOJ6qOk6puLnUumxhOVG7lqv19AzFocLXtNEnMIdm0RqyTxNF0M4lEIl67qDm2qNc3QI0aeKkK9bjqfdtDOogfHR7nuiVXKgzUL16-gdTE7edVIAqaBunnY9Q2fKzmKigyHSNX07XyMhlqIeMCOVeC614XkSWxchBXgXQcj7YjIIxN7Rs2I-QXkwLTUxhR42A9zTh4t4qemw_LoWDzivPkT4vC_KYnakw-SLXlMHTKyacIt85C6iMokteniS-qpuHIV8JWy94Nf9ZKcQtXiptt2uoWjSa8kfiCFNViQYigVUZRAneJy-rUHYruqF-JKszSvpHvnIRYSovqTEVfvnlBATFnxb0Ghhf0zcVKGd23DouWlQ7mOH-paQSUDMFqh99VP5q9Tutr50G22HWqSsxPMGmDZhXWNvJjxh2gUmeFQ8NX42PFL63TEEO_rzmgP0_GUmj7h0RyDaMcIg-RcXejl0F48xdkrTsSeEHD0_sUC0AKsd-wHbJbHk1G7sn2ocPadEIz-SP476_x0tDKeFIW5sCV1LsyZoWmG4a8Mtk9uEaHkWCCOO6FVRhP1i8oHSxUDJLLJcp2lzVj2FjLNQ-FAbtfhjUiMFRbjoEsKh5aHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای نخستین بار در جهان!
کشف قله تنگه هرمز توسط اژدهای بندر</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19274" target="_blank">📅 13:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19273">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">در حالی که اساساً مزیت پهپادها در کوچکی و سطح  مقطع کم راداری آن است، ترکها رفته اند یک پهپاد غول پیکر (همین آکینچی) ساخته اند که ابعادش دو برابر یک فیل است!  طولش 20 متر و عرضش 12.3 متر و 5.5 تن هم وزن دارد!  قیمت آن هم بسیار گزاف بوده و بین 5 تا 6 میلیون…</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19273" target="_blank">📅 13:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19272">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzrHXqALeQtwV5rgNY3P9O3y9B0JfhORdLHx1hQQzP3fqecpy85nIKwS20XcZyZTZ1ilQEnywjreLU2A4Zfu5LvUgyfl4YC6ZTs42wFCswtl7WTrbZsTP11CwCUKQr1pa1n5h0HAejE_ikLJZn0y1F0ZCPFWOhTqNMIeyjFiudApdbrs_NW0LVLT-bzsq9tBeoEmGr1yhn6EB5gPKrewTm6NLfaeP3O3WFotdFYjifaksvXMFqmB6-m-oSjJlnOYIqj-v4PnP-yOTslqRWlQrUrMJE8FWjOyvmpryBhrbnczH40tU7nPjObAK2B1WSsAob_UqK7tX83LzU5QmLuBKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزان بالای مهمات پدافند موشکی آمریکایی ها در جنگ با ایران</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19272" target="_blank">📅 13:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19271">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6066f7963b.mp4?token=bhvU6PWS0AX-eA5B34JYTLrOOjKNmmPQFs-_X-kJY5rH7GpGnzBkPNKReSGaWXpIMuhhhdVpnxcqH5eeQPrUgwcl8E9UVVYuLRKRic_wecLeC_IRXeTtQYaxVFS_T-IewDwrhmZQ4HNOw4HU6wQJQIKkjtwYSdKIgXLWiyO-lMquuGy-prywTlxBNevNPyqMmiQIOuzH_n8i_QsuV3gytAQN1A0WXTIbZKEhIP8rzQfShTWPtFQH_mGpdQ5MU5dhW7rSJqk5Tc8ilYyKsR24U6aNqru5fjTwKyk1Z-KVsgWea8eNWP_DdkhuA2vD3tR4e6dJRacC6q0gdeuIhlNAvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6066f7963b.mp4?token=bhvU6PWS0AX-eA5B34JYTLrOOjKNmmPQFs-_X-kJY5rH7GpGnzBkPNKReSGaWXpIMuhhhdVpnxcqH5eeQPrUgwcl8E9UVVYuLRKRic_wecLeC_IRXeTtQYaxVFS_T-IewDwrhmZQ4HNOw4HU6wQJQIKkjtwYSdKIgXLWiyO-lMquuGy-prywTlxBNevNPyqMmiQIOuzH_n8i_QsuV3gytAQN1A0WXTIbZKEhIP8rzQfShTWPtFQH_mGpdQ5MU5dhW7rSJqk5Tc8ilYyKsR24U6aNqru5fjTwKyk1Z-KVsgWea8eNWP_DdkhuA2vD3tR4e6dJRacC6q0gdeuIhlNAvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران هر روز برایتان یک سورپرایز دارد!
توحش و بربریت یک مشت گوساله در مراسم رونمایی یک یوتوبر ریقو گه دیروز در ایرانمال برگزار شده و ۵۰ هزار نفر در آن شرکت کردند!
حالا بماند که گوشی عستاد را زده اند و دست و پای ش هم شکسته!</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19271" target="_blank">📅 12:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19270">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPkzT5ebsFUSvSu0lgXkF-8VcFSrQkLJ9dfHrVoiiQBPgNZLLp9OTG2XfTz6lJhmtAnbx-aY9Xx7HIVGjpT0CHuZcSMc_mYc4rv33W7ihBIa0uFsDz8p83uPGy7Iw8Hs-gne4NfO8IvwXFWcu9YHPb3Jm02ba0CmE-mUfYxKTHu0cYgEYneRFqXvBvugtxVzuCZJW7TUNREiKTfsyCDX9Uzsppx_yNJjdHoWmC_7lEli2Q0_zcdZwyVBVemWr3wkj44hnuRaazRdtAIrMg5P0EpdxalN_T1QDl791h9A-RSxo9DTkPmzmphdX5WPlDD4qFd5fqAn4A1snkD7tDc4kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این منطقه سبز بالای مرزهای کنونی یمن که جیزان نیز در آن قرار دارد، تا سال 1934 متعلق به یمن بود که در پی جنگ آن سال به چنگ سعودی ها افتاد.   هنوز هم برخی ملی گرایان یمنی نسبت به جیزان، عسیر و نجران ادعاهای ارضی دارند و آن سرزمین ها را مال یمن می دانند.  #تاریخ</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19270" target="_blank">📅 11:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19269">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCWeZulaRO7ejwh9UhWXtF7lCtKxV-Vflj0EqMICcROeNpt1BDSJyRL5O1TAL_-pXiCFAwxIhCNGLfXKTdRNOLqeG-PcPRbP58khUwBGdmwzguPahonhXxYik42jHouyxWxNm95ifNsBeUcdqxePfcjsYbf9zVcFTVyj3hoVeicnUwJMXSRH1hFJkjqV9Z8ArnV1VWEfn4eq1sj-X9dFfH9QrWVMF6Vb1N4boBKSsM7G7J8qHVE9TPMIrQ43J8E2bak-c_kdOHOWA0CopLhZyFBH8KLY35fgHpZZ1je3uaRfFtNuO9zCN441hO_KF5OeFvcAPgl0jGST8L2BRrtvnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زد و خوردهای 2 روز گذشته حوثی ها و سعودی ها به روایت تصویر</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19269" target="_blank">📅 11:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19268">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RL7U1BRZonxjtjGYgCb6-atYTBFy8jxAqyrxmWLYIbdJUiRttqh2Lvf02o8Giw95TCItfL8AyF893_jXlZgTas6Vpv9-Bv1wZIiuq9zaJPmjNOun-D7QZ9lFPZ0suNtuk75fcsEnUh_dwVCVNt_QDB2drK0JE-WG_6KVUfOQH5GB_veiaUdTJ0z9P99p7Y58ehRkYdl9RtaYpAlTk0-h6Q8EdpHf1fO_N31CweJsPt-ie2eOnbb957u94Z8KdxI__-4sQPmuG-cAAoy5XXxfRKt4shajeMeOxoj7Sdz0ykQOSfwxz0tETzE-Q1L3xPOaPwIrnazyKZFmb6zVzXKujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زد و خوردهای 2 روز گذشته حوثی ها و سعودی ها به روایت تصویر</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19268" target="_blank">📅 11:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19267">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بقایی پس از مذاکرات دو روزه ایران و عمان:
مفید بود اما تغییری در وضعیت تنگه هرمز ایجاد نشد</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19267" target="_blank">📅 11:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19266">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c9dbca0a.mp4?token=mkO48m8o07z5OIxTSN2It5TbArGx3rskkMSD0MFlOW9IxvCtyJZn9Yx2llmjn81LBjGm7xQ3-ymlUNoQ2w1CN3wkopOEdbFBBY7toMi6xhgrQvVQf2lg71VxFO78L_hg0TbsZ44lBSv5h8a1t6Hr7Jhv9D3envGDQN4gDSLOROiCQ8fVEDxIV9TSzbKGE8ssmGdh0jxXAoUk7wi1sSIXyLE04Idx9KAKGE5JbTR-niMSxTdHTTIoklkx8wKH_Qn9LqVdcvs98S1zgcFo0g7eWbmMBu7S6-uoLZ2zrFDxiV4y02eRb6NP8vqdWR382kz_seLqVit283y8GDCBf54GpqqqwqhTaXWPrJs8S3FjH72Y8Wg3lDsYamwKdd5Aff5Emlfne47YiXMnIpybDn6wcmnPdo5P5c0uG2M9DX-R7rQk6RT3BOrxCqrRfeqXAz1UlO4b5s8a6WRkwd5V5oWjV31tk7a7EBir0eDJdoTVXRrf1c2WrlyqHg16qYvLypYrxgYOoHqfiFnepBFBKJbn84Y1VwXjq6wUXoJ5StjwjAk9ciwhS23yqUzRlfj6HtCpwraYkITdUBboDn4DNtjLyOwPG4GB2t70sgdpA5WbejGVg8bEOlMYsyZ6JYUa5n-HgoGUW1-j6gMCT2XkwkoZ47aLD1cpcbagoCB4XYXWQhI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c9dbca0a.mp4?token=mkO48m8o07z5OIxTSN2It5TbArGx3rskkMSD0MFlOW9IxvCtyJZn9Yx2llmjn81LBjGm7xQ3-ymlUNoQ2w1CN3wkopOEdbFBBY7toMi6xhgrQvVQf2lg71VxFO78L_hg0TbsZ44lBSv5h8a1t6Hr7Jhv9D3envGDQN4gDSLOROiCQ8fVEDxIV9TSzbKGE8ssmGdh0jxXAoUk7wi1sSIXyLE04Idx9KAKGE5JbTR-niMSxTdHTTIoklkx8wKH_Qn9LqVdcvs98S1zgcFo0g7eWbmMBu7S6-uoLZ2zrFDxiV4y02eRb6NP8vqdWR382kz_seLqVit283y8GDCBf54GpqqqwqhTaXWPrJs8S3FjH72Y8Wg3lDsYamwKdd5Aff5Emlfne47YiXMnIpybDn6wcmnPdo5P5c0uG2M9DX-R7rQk6RT3BOrxCqrRfeqXAz1UlO4b5s8a6WRkwd5V5oWjV31tk7a7EBir0eDJdoTVXRrf1c2WrlyqHg16qYvLypYrxgYOoHqfiFnepBFBKJbn84Y1VwXjq6wUXoJ5StjwjAk9ciwhS23yqUzRlfj6HtCpwraYkITdUBboDn4DNtjLyOwPG4GB2t70sgdpA5WbejGVg8bEOlMYsyZ6JYUa5n-HgoGUW1-j6gMCT2XkwkoZ47aLD1cpcbagoCB4XYXWQhI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عمومی بودن اطلاعات برخی نقاط حساس نظامی - امنیتی در ایران</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/19266" target="_blank">📅 10:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19265">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پدافند غیرعامل به زبان ساده</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/19265" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19264">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jje2-5JhTyJX8afHjzrsX5N6KVR1cJK6oxFcrnCNYuQydR2S-HHMmGbPau-2e1lLrE8VfxPL3VHDrYzrk4KQ334H-Cvq4iB0s3UxzzujrOkaWr32J4d1GYqyd34BEpQPx3UJOKgYuP3Gdp914M254RdEQkm5LFZ69Slf3u2vt-xs82r2WwVTjb19eE9KLGRioSqY3Z3Knw-UwamLnpKLctKwa9Ik_fUVKXSPLeTFwknKJZlGD7FtrCL5dQ_0LtvZRc3DK5FFKGqn7jjj2g2N6I1xFzZUThx-DebXvmDoHgpvN-Ql6dbBOel7gaj6aGaVqIRpJuMDLhKc8dN3ybL3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/19264" target="_blank">📅 09:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19263">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نیویورک تایمز:
ترامپ، حداقل فعلاً، برنامه‌هایش برای تشدید قابل توجه تهاجم نظامی آمریکا علیه ایران را به تعویق انداخته است که دلیلش نگرانی‌های ویژه ای است مبنی بر اینکه تشدید درگیری می‌تواند ذخایر رو به کاهش سیستم‌های ضد موشکی پاتریوت و سایر مهمات دفاع هوایی پنتاگون در خاورمیانه را به شدت کاهش دهد.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/19263" target="_blank">📅 02:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19262">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">انتشار برخی اخبار تاییدنشده از شنیده شدن صدای انفجاری در بندرعباس</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/19262" target="_blank">📅 00:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19261">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آشنایی با پهپاد کشنده اوکراین  پهپاد FP-1 (Fire Point-1) یکی از جدیدترین دستاوردهای صنعت پهپادی اوکراین به شمار می‌رود که در سال‌های اخیر به یکی از ابزارهای اصلی کی‌یف برای اجرای حملات راهبردی در عمق خاک روسیه تبدیل شده است. این پهپاد انتحاری دوربرد با هدف…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/19261" target="_blank">📅 00:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19260">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی حملات هوایی را در منطقه دمط که تحت کنترل حوثی‌هاست، انجام داد.  این منطقه یک خط مقدم فعال بین نیروهای حوثی و نیروهای دولت یمنی که از سوی عربستان حمایت می‌شود، است.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/19260" target="_blank">📅 00:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19259">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اگر تُن ندارید دستکم آماده باشید!</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/19259" target="_blank">📅 00:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19258">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19258" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19257">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بیانیه وزارت خارجه در محکومیت حمله اوکراین به شناور ایرانی در دریای کاسپین!</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/19257" target="_blank">📅 23:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19256">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9NCFGXgho50OHOGUm7qMuZClsCOBkMGyyQO5IFY_qC7pZgOLda-U7E8ApSujO7lzfqK8N3d8us0UDZqK16ASK4HUUuPUbfKZVWEk-5MfBeKQANIoxrf-u_DecwGrd83GExhq0Vu7wNBXZ-RaM8TY2fFb_HCXwDo5s9mxn0gBuXb5LfSs71Yn-b9RQ0GB5ipPk6WhcHNEfwu2JHzBAdO1u_lZJaqaHjR98KI0PM67gI0UNJwsQa-T8hjGLa2ZsbBW3Wl-cwx-L-Dl04pYOLQDfx_qCt-1ejRhjVbOEsjci7NOo9ececeM190kpG_Z4AxC3nIhN5sg4Zk6B24ymFLHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید هم زلنسکی دارد جمهوری اسلامی را تحریک به پاسخگویی نظامی به اوکراین می کند تا رسماً پروژه تسلیح گروه های مخالف ایرانی به پهپادها و ریزپهپادهای اوکراینی را استارت بزند.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/19256" target="_blank">📅 23:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19255">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سپاه پاسداران:  «هر کشوری، چه بریتانیا باشد و چه دیگری، اگر از آمریکا در جنگ حمایت کند، برای ما هدفی مشروع خواهد بود.»</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19255" target="_blank">📅 23:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19254">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">در عملیات 2 شب پیش دو فروند بمب‌افکن B-1B لنسر نیروی هوایی آمریکا از پایگاه RAF Fairford در بریتانیا به پرواز درآمدند و در بمباران جنوب کشور (استان خوزستان) نقش داشتند.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19254" target="_blank">📅 23:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19253">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIFicBin584ay8ZxmNrd0YWv30F1VgOtXGBYyY5soPA_cDS9YYR7DlOYm2U6OqCHUxcQA-9EpZj8a4aAWMdaJqAoAGxvZWdy9eskkv1xoW_4IgFvo2mkKJBTvmaK-B2E3ViG89jGFDbedQ-IjOsB3c9nDOl1DCP4LYIQevIpEKW4bjgnH_7GGCW_OnxF0DNKOu6WBuaf46fwI_Jakn900JNexPe9TjaXA-DywB3TFKzTL5ZixxWfTTScVHsszSWnT8h8SFICCOjOdzrVmUyvxT9ZfwWfmMXA7oqsHvPmKoAn3V2nAHuYUSiTgEqxPBYz-k3fNYUhsMJNrIlwC6jrkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عملیات 2 شب پیش دو فروند بمب‌افکن B-1B لنسر نیروی هوایی آمریکا از پایگاه RAF Fairford در بریتانیا به پرواز درآمدند و در بمباران جنوب کشور (استان خوزستان) نقش داشتند.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19253" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19252">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نیویورک پست :  «دقت وحشتناک موشک‌های ایران» این هراس را دامن زده که دشمنان آمریکا در حال کمک به ایران برای هدف قرار دادن نیروهای ارتش آمریکا و CIA هستند!</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19252" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19251">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ درباره ایران:
اگر ۱۰۰٪ آنچه از ایران می‌خواهیم را به دست نیاوریم، قطعاً از سرگیری جنگ تمام‌عیار را در نظر خواهیم گرفت.
منبع: LCI</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19251" target="_blank">📅 23:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19250">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی حملات هوایی را در منطقه دمط که تحت کنترل حوثی‌هاست، انجام داد.
این منطقه یک خط مقدم فعال بین نیروهای حوثی و نیروهای دولت یمنی که از سوی عربستان حمایت می‌شود، است.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19250" target="_blank">📅 23:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19249">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">شین بت از خنثی کردن یک ترور دیگر ضد بن گویر خبر داد.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19249" target="_blank">📅 23:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19248">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رسانه‌های آمریکایی: به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد تنگه هرمز خواهند رسید.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19248" target="_blank">📅 21:51 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

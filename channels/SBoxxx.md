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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 05:27:46</div>
<hr>

<div class="tg-post" id="msg-19346">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc3554F2LmZeUm3I7noAZ9pQCnM44C0XV7XhXTKkqf-Yu7gjUOjRDv0KfZe4vP-DXI7LfLFqR8tf9qHAELWjvf9C3bAsl8BUmZZAqXGdHs5IAthwoc5wwiofDzi1D49LBe02c4jIm30ERdcziTtRPQSfRmd80iHSOy5Hto03WEWehm1BYO3bjMrWaRidS_odBlhXTNGBksLTXJAa1WI3jpfVMI_pGOM_E1Z1T8f9tZxzg7qjx5qcMQVzDdk7JCvhARrVux2q6E10Fq9pOsqH0tTwgsh3EaTYDmkaICfa984pZqsCpwf6SND1PSCKPo4ne4TGEfNmtRD7J48xhvU__A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه محموله جدیدی از موشک‌های کورنت و پرتابگرهای کنترل از راه دور به یگان‌های خط مقدم تحویل داد.
این سامانه پیش‌تر علیه تانک‌های لئوپارد و چلنجر، خودروهای زرهی بردلی، استحکامات و مراکز فرماندهی استفاده شده است. تجهیزات پرتاب جدید به خدمه اجازه می‌دهد در فاصله از پرتابگر و در پناهگاه شلیک کنند.
شرکت روستک اعلام کرد کورنت هزاران هدف را در نبرد منهدم کرده است.
موشک کورنت-ای‌ام با کلاهک سنگین با قابلیت نفوذ ۱۱۰۰ تا ۱۳۰۰ میلی‌متر زره همگن نوردیده پس از زره واکنشی، تهدیدی برای تانک‌های مدرن است. هدایت لیزری آن در برابر اختلالات الکترونیکی و نوری مقاوم است. پرتابگرهای خودکار می‌توانند اهداف را پس از قفل ردیابی کنند. برد این سامانه علیه اهداف زرهی تا ۸ کیلومتر و با موشک‌های انفجاری تا ۱۰ کیلومتر است.
تجهیزات کنترل از راه دور خطر قرارگیری خدمه در معرض آتش متقابل، توپخانه و پهپادهای اف‌پی‌وی را کاهش می‌دهد. این سامانه روی خودروها، خودروهای سبک، چهارچرخ‌ها و سکوهای رباتیک نصب می‌شود</div>
<div class="tg-footer">👁️ 517 · <a href="https://t.me/SBoxxx/19346" target="_blank">📅 04:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19345">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بر اساس بیانیه فرماندهی مرکزی ایالات متحده، از زمان اعمال مجدد محاصره کشتی‌ها به بنادر ایران، دو فروند کشتی برای اطمینان از رعایت قوانین از کار افتاده، دو فروند کشتی بازرسی شده و ۱۷ فروند کشتی تغییر مسیر داده‌اند</div>
<div class="tg-footer">👁️ 830 · <a href="https://t.me/SBoxxx/19345" target="_blank">📅 03:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19344">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رسانه‌های محلی گزارش می‌دهند که شماری از پهپادها، احتمالاً ساخت ایران یا تحت حمایت ایران، در اربیل عراق و مناطق اطراف آن رهگیری شده‌اند. هم‌زمان، سامانه‌های ضد راکت، توپخانه و خمپاره در اربیل فعال شده‌اند</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/SBoxxx/19344" target="_blank">📅 01:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19343">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONveGHbFRPVNL23ZXjLSaox2Z8_zx9jYa-uui8kxyKHw6pMq_aGjZwXmVspWP5jkGVZW5JQY6WVXGnO4JSMmeHCnigp54Ks_VgyCsyB9NSVZJmiLB_1MzQ-pC6O5cr1ZQqO5OIhxIkIv7s-C-PC9I-Jab9aUsF7R3g1PM2wJCw9okDWKZyV8bSPHoZNR1y7yBtd59QdpgvMWBaHLNCE1oPKnGn7-LahytYQZMS53LxmMWtkUyUUaGljhtAmNr7BUOBlQfRyfBRvCrOZw5FQINGzFMGko9MwzSTLbKLSCtRKYMb1hMMmoCTC58Pj9G40TfV50VnQcx1veGAQF6TfXTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک بالستیک Lora در خدمت ارتش یونان!  به زودی، نیروهای مسلح یونان به موشک‌های بالستیک هدایت‌شونده دقیق لورا از اسرائیل مجهز خواهند شد. این موشک‌های بالستیک نه تنها توسط نیروی هوایی یونان بلکه توسط نیروهای زمینی این کشور در سراسر جزایر اژه و مدیترانه یونان…</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/SBoxxx/19343" target="_blank">📅 00:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19342">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">عمده خاک اوکراین در برد موشکهای ایرانی قرار داد</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SBoxxx/19342" target="_blank">📅 00:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19341">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یادداشتی خواندنی از یورونیوز درباره ایزنکوت و حزب ش.  لینک</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/19341" target="_blank">📅 00:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19340">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/19340" target="_blank">📅 23:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19339">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6eT2TRdRog1O09sbpIQsD6zDFiY5F1CjVEOC_XC_5CNFj5mZASKkT3RkwrkCH_feBaShnkGlE1X38DQjIUFZE4MEnYmiCEmn79G6ndMTNh9P5Da9qdYllQTHZQdvs7UNWqC6zM4CyFb8lJk-3BbtbUsugTBtSOyoJu6gSEXCYVtPBfE3A7jkNMr3Urtr1nVZkvoebXULBRgdkbe2v2HRIxlUaOsXeCxsCV6Pd2PsRjcqSKRUPi7t1S9BBnOeaaqBU5x5DLdTNNYH3gKUbN6mPeZuIY5_wzglKbXYfydOq7y7BKT8aLWkfvxngrMWjlzZwJWKNi52Px_zdCDvyS1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/19339" target="_blank">📅 20:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19338">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اظهارات ترامپ درباره ترکیه:  ترکیه علاقه‌ای چندانی به اسرائیل و بنیامین نتانیاهو ندارد اما ترکیه برای من بسیار ارزشمند بوده است.  به هر حال، ترکیه یک کشور بسیار قدرتمند است. فوق‌العاده و با یک ارتش بسیار بزرگ.  ارتش آن‌ها تجهیزات بسیار خوبی دارد.</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/19338" target="_blank">📅 20:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19337">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دقیقاً طبق تحلیلی که ارائه شد آمریکایی ها نخستین پس گردنی را به اردوغان زدند و علیرغم همه وعده های ترامپ، گویا تحویل جنگنده های اف-35 به ترکیه متوقف شده است.</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/19337" target="_blank">📅 20:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19336">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLSitPygeGoxr_AuXNpCCVIK6MhjTZPiwDLbskpcivLZ0Opr8OW2O_D0_FJsSJ7pN39OS7-_8o9UtnVxoB8-7K-2FX6viJ3L8qwMdZabIS7g-t81tqxHE_-l0hhDTswYSOj-xDZ7k2yzxrwkSAA-w7G-YYtw2ZZqCGPUQGFFrKBGQoU9CRRSbHD6jOJyULUNoIUdu0mZ-qH_zKc2euPJSi0G3LdAwQU3iZsmAQ_KmnIDHFzJ1nzE7TQKNd0F9HUEbfEUlcVsPAmmUCnnG0yImhd9-zAKextann9Ho1UA2FcHmAdXiVLsyZH8Qd6KXET9wf0S1Ul_KegBthkFhO6lVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه است و پیش بینی می شود طلا که در سشن آسیا با خوش بینی زیاد بازگشایی شده گپ را پر کند و تا حدود ۴۰۶۰ افت کرده و آنجا کف سازی کند.</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/19336" target="_blank">📅 20:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19335">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پدرسگ ما خودمان دزدهایی داریم 100 درجه بهتر از تو.</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/19335" target="_blank">📅 20:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19334">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ:  ما میلیاردها و میلیاردها دلار از ونزوئلا می‌گیریم.  این اتفاق با ایران هم خواهد افتاد.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/19334" target="_blank">📅 20:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19333">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ:
ما میلیاردها و میلیاردها دلار از ونزوئلا می‌گیریم.
این اتفاق با ایران هم خواهد افتاد.</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/19333" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19332">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">عاقبت به خیری
😄</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/19332" target="_blank">📅 20:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19331">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/19331" target="_blank">📅 19:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19330">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R82mskY8wJdk60za3piXD4Mi834o7zIzaq14QtK7F-gufUJJuBfe8suaBnlNNzJzsLxMtBd-LwU929z11mjUfimjuadKa9haWIA2XXWxO_ZIKVm44m-JGWdUKrmOHTI9NmZ_Hpf-4My92_Fr-DigjK7beeGrSKsWUSeff0cEkOVi_7-FOLI5zo_ftqsBSKHTvNCY_AkY4EZQP_apmVTmZEohuQHPxEaJEVeEMLpyvPvf0FdMJ2hy5ttonwaGYqPh5c-TTRiiI1s7Z21WTwz1iCetg3CdnFFYz9H-b0W-3ji_0tIgMgdMnCVueSv6eyH9kf38rSff6ThhqFCEVKN0kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:   به درخواست میانجی‌ها به مذاکره فرصت دوباره دادم.   فرصت زیادی به مذاکرات نمیدهم.</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/19330" target="_blank">📅 19:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19329">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ:
به درخواست میانجی‌ها به مذاکره فرصت دوباره دادم.
فرصت زیادی به مذاکرات نمیدهم.</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/19329" target="_blank">📅 18:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19328">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">276.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/19328" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 13</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/19328" target="_blank">📅 17:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19327">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گزارش هایی تایید نشده از وقوع انفجارهایی در عربستان و هدف‌قرارگرفتن تاسیسات نفتی این کشور.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/19327" target="_blank">📅 16:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19326">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDWbboUD_6_V4ksSxc52wywxtRXp5QwHM_38T3Dktm5FGhi23rf0DK_VkHvnwrtv0TfaFjKE_yy_LZEFlJnIEil-Xdyb-W2kMG8G9CK_VZk4kz5mEpOghMIb22A18CSykI1A80HXgR5idpMa4GMtYOMqOpqOCEUwowYv714dOIoTWRk3TriuVzHBjrVB6ciIagyBXYaCRD4YMrPnosYtQiK2wQRxP80eVnJ5IMxM3kzjSq8ONnFyb7FQZ_Mzs59mNvvIAfRZGsEr6rQS4-SX22ePTvRagZhh5MUf3U7FeSZ4JqxgiJOnQLCHZGl4l7Syg5OvQxeNJGKRn3D-o2h_QA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/19326" target="_blank">📅 16:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19325">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وزارت امور خارجه ایران:  «عواقب حمله به کشتی ایرانی برای شما غیرقابل پیش‌بینی است.  پیامدهای اقداماتی که زلنسکی انجام داده، بر چندین کشور در سراسر جهان تأثیر خواهد گذاشت.»</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/19325" target="_blank">📅 16:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19324">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">از اوایل امروز صبح، نیروهای اسرائیلی حملات خود را به جنوب لبنان ادامه داده و در شهرهای حدادها، تیری، مارکابا و تالوسا و همچنین در حومه عیترون، سری از انفجارها را به راه انداخته‌اند.  آتش توپخانه اسرائیلی نیز تپه علی الطاهر را هدف قرار داد و در نتیجه حملات…</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/19324" target="_blank">📅 15:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19323">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">از اوایل امروز صبح، نیروهای اسرائیلی حملات خود را به جنوب لبنان ادامه داده و در شهرهای حدادها، تیری، مارکابا و تالوسا و همچنین در حومه عیترون، سری از انفجارها را به راه انداخته‌اند.
آتش توپخانه اسرائیلی نیز تپه علی الطاهر را هدف قرار داد و در نتیجه حملات اسرائیلی، آتش‌سوزی در حومه تالوسا و مارکابا درگرفت.
یک پهپاد اسرائیلی چند بمب صوتی بر شهر منصوری رها کرد، در حالی که سربازان اشغالگر اسرائیلی به چند خانه در بیت یحون آتش زدند.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/19323" target="_blank">📅 15:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19322">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
نتانیاهو، اطلاعات به‌روز در مورد پیشرفت ایران در جهت دستیابی به بمب هسته‌ای را به ترامپ ارائه خواهد داد.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/19322" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19321">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 13</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/19321" target="_blank">📅 14:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19320">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/19320" target="_blank">📅 13:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19319">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🟢
پاسخ به توهم برخی درباره شکست احتمالی نتانیاهو</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19319" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19318">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmjt9P0zyfloGGBuJ16PhW8BH0JLWS82_T5nEHaTj2n_ubANHY3AuaE85oLfGpFc0ZBqKqn-rWm6JJRbKGSV76Shts2F0BW-_4idvPu6N5cWZswu8ZPBz9pUSKCx6SLRQTjyNnNS90mqftKnzzSGMkOClWqYMkiuVbMEXCVxI0s0fGKHqDee5kujJ6FAK_FSJD2wiLVNJz-F56qbkrhyZBIcw4A37UDEqaoEreBj5cgXszbOeBGRn9AyvHstziY4RcD_Pt0L53ziQKL5KcSFYCM39EpxoBvfnHfrLPqXmjVKa8pFPb8yd7v1FXNJMWUm7eDl2OAkIYoi1fyM2LNLww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۸ سال پیش در چنین روزی مجاهدین اسکل خلق میخواستند سوار بر تانک های چرخدار برزیلی از مرز با عراق تشریف ببرند تهران را آزاد کنند که خوردند به تور کبراهای هوانیروز در تنگه چهارزبر و مارجین کال شدند.
#تاریخ</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/19318" target="_blank">📅 13:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19317">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سخنگوی وزارت خارجه: چین نیز مانند ما نگران وضعیت صلح و امنیت در منطقه و در سطح بین‌المللی است.  هر دو کشور نگرانی جدی نسبت به استمرار یک‌جانبه‌گرایی بسیار مخرب از سوی آمریکا داریم</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/19317" target="_blank">📅 12:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19316">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سخنگوی وزارت خارجه: چین نیز مانند ما نگران وضعیت صلح و امنیت در منطقه و در سطح بین‌المللی است.
هر دو کشور نگرانی جدی نسبت به استمرار یک‌جانبه‌گرایی بسیار مخرب از سوی آمریکا داریم</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/19316" target="_blank">📅 12:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19315">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19315" target="_blank">📅 12:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19314">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9MRBlAxdm74NEl5GaUuZSPWCPEOqhTPlFE5LjPThfUpbURxaeGyGfK0iKzJ2gqbXbuuwtSxzlyeyLpETC5ZVpTqUfCmhTufEJ4rixlo6hZMYW8mqQ3hWFrjaZ4UMgM1enx3JqU1PXla9FNX20FqY1AkCKSs0tbApX4A6xKu5--tGnWjoyaVG2sRfoR4FtlhlRSPVcRsjkq9adch9dzVSsyZcA17nEKnVJNS3PNXwHHNVH2Z_xtck7aMLiOgGrApKDJ4OuBr5_sbGw89CzzZF6yt-11D3U59FgX4vD4ahGGKc1713sdo8imyS2N4lmRETAVmD8NKY6ds-grBbG-eAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه است و پیش بینی می شود طلا که در سشن آسیا با خوش بینی زیاد بازگشایی شده گپ را پر کند و تا حدود ۴۰۶۰ افت کرده و آنجا کف سازی کند.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19314" target="_blank">📅 11:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19313">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/19313" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19312">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گزارش نیویورک تایمز، مقامات آمریکایی نگران هستند که پوتین و شی جین‌پینگ ممکن است کمبود مهمات ایالات متحده ناشی از جنگ با ایران را در محاسبات خود برای اقدامات بعدی‌شان در نظر بگیرند؛ این اقدامات شامل اوکراین و اروپا برای روسیه و همچنین تایوان برای چین خواهد بود.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19312" target="_blank">📅 10:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19311">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19311" target="_blank">📅 07:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19310">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iz1df7hhp4f7PVLwPdvQoXj9MLEiDOQKsqOtUMZQcdcb18YsRQ5wG6y2M9Kvd8TYYCfdh_gsGMjF9Ab_9lxZlOsBuqcJ4F5mLOqpVz4H5i-9xjFN_YJ58zpn_YsIixKGPJ3HF3HW2DSwiS_TUj9EO510mUyobyrWlAqR9otxuHOFgTRlukSo4PTzAdI6xu-ws1jjxWF-ssINpoRgtDaWUQFqlrkExFm2Ndn4I8GIn-AMyidkNylTRcTmbiPkgQds0-Vq1nP6I0TrMjDbhKcZby3mg080Gj8LCeT4pHcaU-o6OvqhTl5uP_hd4HnrlsGqvvUsWRGSnK0DoUH_SHE8eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکونومیست:
برخی از حاکمان خلیج فارس به صورت پنهانی به ایران پول می‌دهند تا در آرامش زندگی کنند. برخی دیگر در حال عمیق‌تر کردن پیوندهای دفاعی با کشورهایی مانند
ترکیه
و پیوندهای اقتصادی با
چین
هستند.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19310" target="_blank">📅 02:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19309">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">روی کمپانی Boring ایلان ماسک حساس باشید. فکر می کنم بزودی همه ملل به سمت انتقال دارایی های حساس نظامی و حتی اقتصادی خود به زیرزمین بروند.  موفقیت نسبی و کم هزینه مدل عملکرد ایران و حماس زیر شدیدترین فشارهای نیروهای هوایی برتر جهان و گسترش استفاده از پهپادها…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19309" target="_blank">📅 02:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19308">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شاید هم زلنسکی دارد جمهوری اسلامی را تحریک به پاسخگویی نظامی به اوکراین می کند تا رسماً پروژه تسلیح گروه های مخالف ایرانی به پهپادها و ریزپهپادهای اوکراینی را استارت بزند.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19308" target="_blank">📅 01:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19307">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ابراهیم عزیزی، رئیس کمیسیون امنیت ملی مجلس شورای اسلامی:
▪️
هرگونه حمله به ایران همیشه هزینه‌ای دارد و این موضوع امروز نیز صادق است؛ آمریکا و اسرائیل به خوبی از این موضوع آگاه هستند.
▪️
اوکراین نیز ممکن است به زودی درک کند که ایران اقدامات را بدون پاسخ رها…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19307" target="_blank">📅 01:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19306">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">▪️
لیست کسانی که اشتباه محاسباتی داشته‌اند همچنان در حال افزایش است</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/19306" target="_blank">📅 01:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19305">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19305" target="_blank">📅 01:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19304">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7fpdajI8QhyT1g0_EvorMx_Jn_3np6Rvb1601DfP13LLBySbtwSsgmQlz0co2StcN6cM-NWGOsrkPYiliaCkuT1jsu6BsQsplqAJcu86xHwtzbJoDKun-uki0-QmdQr9204bkIrYK6zlt8-LmO-dPDRUSBPRulRZ_AhGh7v0qjJhlNuvJJ88R4pjqsTt5ugGy-xouNcfr-10ir1wYKI7aCemsgnNFQzf047AbhF7it49YH2w4FVPr6CSqoJ7gA2R1__quhCU5klU_N3Oe0bS1zpLcJ2uhZg2Nrbog47-_PGZ37xrn-wto_TZS-BujhZ40sbiouHarcSpYv9eQXmeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشایی نفت با گپ 7 درصدی منفی!</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19304" target="_blank">📅 01:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19303">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-dS_R_2liWhYtzl0gkL9Pxoc-PfReKksBh9qAbhTnl5yXfW-7wp2JClfynsejePWdOi7fqD1kDSlvnw8aYx-Foy95EHNIH_rs9DvQOAtuyipURS40BM915FF6JQAQM4dS6VXk8S7Uaf5trFHHLZbW4zDykgwYbSedQqLg_0hl1q13DE6uNDWXREnQ4GW9FroTl_CmOU3a6FE9du8ZlNYS1v2hVQ5_epZloGjWookbCjGVOLR7BlYov87_IxUnqfWRuq-0y83Y_S6GR1taOwMHQg9nqzq58PP-4aRWDiVg5pG3Nno0s826QA2PL2yYJMH5T9CkUYYLC2ve3lKe9rmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از جنگنده جدید دوسر بدون دم توسط ترامپ</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19303" target="_blank">📅 01:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19302">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7aXQmnJzGHl2h9ZlGdl1orObPIEfXi9SYbtFJFcBhTVingjCqmXGuLI3SrcZiIYFXshYoAJDjartWLGM6ay79_KIm7E6m5y1Gj3_pO3-juCBhXMc9sgkh1m5o_HSj6M45ji5lZ48YNhs1xlYLm575G03VHTe8yIN8kD6Sey3OjloUF0Vr-VoWxeQNOaO7X99SyvzZmp-HZWfSOaIO9ZymKxRuQs3pNlKhBO8MYn1rPwnwBnrkpEz76hShIYT-3r1QT1VZJ_0S2UyUHfN4g97K6BuQ6LaknohA6SSswC9GlzMXLVoBLsTY4cZ8z66Rw8nFt5Ife2495Yf320RMLWeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19302" target="_blank">📅 01:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19301">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJGBpCVguD2YgSlzWHyn5KN2ytEGAcBqptT5N3ayG3wvRXvdgpUHpaaeL2zm--e9IH6CrjcA39IqAm09dTLKAkXmV4Yo11e5YjQ5TKgE7h6RhwqARtpD2wVOEVE8kOASrEYuTUWSAM3lTMsCEDmt1ppSgQOax_dyYqqCd07aCh76NK9e--BX4dssd-bB2TvLuHJYUUPlaRhUr4-r25SbMoL64cVqIIYqXueEdSaoRycVwzWUviq6Pg89M3ECcK5PwhiU-s9uOi5y2NUKl7KH4NrY7l4C6o7rVYWsO-0fVkap-0cT6AVkUzM3vn_Qs01ouN3xz11rY6GZRiHygpG9Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ول کن نیست!  اشاره به زدن موتور نفت کش های ایرانی که می خواهند محاصره دریایی آمریکا را بشکنند</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19301" target="_blank">📅 01:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19300">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">رهبری ایران در نامه ای کتبی اعلام کرد:
در برابر اسرائیل و آمریکا راهی جز جهاد و مقاومت پیش رو نمانده است.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19300" target="_blank">📅 00:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19299">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19299" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19298">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fit8Vu630Qs56mbFeTP4ouIqlIH5U6s0kLeqcSzTE5FmRzVVOtE_KX5D5mtjrkd8qJs3BBuk_xnOXlhmDCClQ5-SnWBwSOHeh6ZQKitl_a_SKMpHeemNJGGPvkL433oqSFjCaUnO7WAUnYvJ6FggTgyht0aXKHu8-MHRL0pFodw5NjXoKeaZaYI-8a316zzTZcaiUyeZFh-VBpCDFZT6oT_xwS_u3CReDdHrVNzFgsd-zg2ko3TZNNFNGj65hEvE9IujXEiJCk4a47nNF5ibzNEAr47a6ooulRTIeGvIUvU-XA_PhWQ-CskCE5HipsmrAQAtPJIVvorRYy7SrqO6ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آن عرب ها کیستند؟!</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19298" target="_blank">📅 23:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19297">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgJbo1EBfZ9CIObpOlQZPfH5ZNfacqp7Nmjn8qOWka31RiZSnx5OkQBGbkUY7TIOYq4QIgOymp8GEU4Mu5n4YhX3_7eFVykz5zoHWqV-TARz8S_Sn-vX19vtyFJZYkSQwxKHz2-gG_QZGHwslOZgwGt4Q_ekHrRNpD-KmM5qC_2HLEXioqDUfWmGBvfmkml595OzMA2rr9ZKdYEbwLeo9yAzbPEyyML2siU4JujNIY_zTHFUxHcgZVAbsShILew6witgKUofS1dvq_MOj1YLkKGBWnWh4vbqwR31ayGD_aTXJRF9Rktk4REd14EPHV8ek3dsSuIFvGn3NEiHTFif4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19297" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19296">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJsZ2A7Qfn1xvuzZSKR3rhgsZxSiqgXXURHzowOqLK_J7_qDhuGfEsi-gQ5VbIa7WcgU1wcCDNZigV4IFSVNLrtWs4lq_WVkHj-EMkDf1x3V295qjSXKZSO86txiZHBZJUlsPJBx5cYFsW3LR-5ylkSUccdXpztbFMxNVZdFyGqzw6WSKQvx5Ozii7GAnMwazYBvDpB0gxSiSYc8M2iX6LmLzQJ6AP31r1oL1tEHWAXi-3yBdajIqSyJLDmXMnhfPKothXNoWGYzydLVBMJMtJxvZ_1OL5JaYi2Tbt6KNbVEPVxQOY2OVYpPApi0dFtO9CXWwbfShUqp17GBEnz_Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/19296" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19295">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">قشنگ دارند به نتانیاهو پاس گل انتخاباتی می‌دهند!  میانگین IQ وکلای ملت را دوست دارم.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19295" target="_blank">📅 22:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19294">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نماینده های مجلس شورای اسلامی با لایحه ای مبنی بر اینکه که از امروز تمامی شهروندان اسرائیلی اهداف نظامی مشروع محسوب شوند موافقت کردند</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19294" target="_blank">📅 22:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19293">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نماینده های مجلس شورای اسلامی با لایحه ای مبنی بر اینکه که از امروز تمامی شهروندان اسرائیلی اهداف نظامی مشروع محسوب شوند موافقت کردند</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19293" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19292">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snvBaBUszR_ZLvRAOVUx9VhmTgOSif8ZsWzYShCnnN1QqQEydMImRjHKh6BNAkZqbe3noygVN27rp_fkJTOoMuNJ_2VoaKfcnF_179nTIpnmo0UpprpxallQu4MD5dXyRfokgAqIzYdlczpisEUaqKxmPVN9ADpSflmMZ5FqJ7tgKpV7vuLPiSy0D090znTuRrF4gXCGAoSWxBPRT9rzEXQp5ucqS6zcS8AKsfRxIFr2Oe17lcZNxXaVZ76O6j5ZUhZ12C-be5Pa77qtp7CQTo8W1elHpqLx9mTX_Ujd55YilsVb8iAbLmJqAkvNhp1pn1RJu_PkP2MJp7R8RAiV1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نایب رئیس اول مجلس ایران علی نیکزاد هشدار داد که «عمل گستاخانه دولت اوکراین بدون پاسخ نخواهد ماند».</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19292" target="_blank">📅 21:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19291">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZppCIWPCxkf1obpM1uN-LnRiQxnNAzs0UweIqRIwldKkR44sG-CdYeLf3x7FGuwQIeVaiioPU72jnrxaOZZbDXdDgJ6ri7k5cm0jKqmOxGTMkzFciZfcBCb5t9o7NifOzpoCjLiVzzOKfPN36ZRjUR9PoruDwTq7QkIJcswuAu-htsJqrxgvRKXPDN-OUk0l586XswS751jQKYrygA_i07IuVi3nPekjxHJFvh4Q4mktrNc4eJzp6sIQfLqhnhIh2qjJSCFM1kyTBZezKpcO_aPIfwOJ-O6-VfXiCT04W-iXVltpCHC-A3jdGx0xKCXYmjYwmF3PU93bylrNzn_hmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انصارالله یمن:  یک فروند پهپاد آکینجی متعلق به ارتش عربستان را بر فراز استان الجوف سرنگون کردیم.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19291" target="_blank">📅 21:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19290">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آکسیوس:   فرمانده سنتکام «برد کوپر»، توصیه کرده که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به حد نهایی کارایی خود رسیده است.  به گفته این منابع، توصیهٔ کوپر (فرماندهٔ سنتکام) به همراه مشورت‌های دیگر مشاوران، بر ترامپ در روز جمعه برای توقف…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19290" target="_blank">📅 21:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19289">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سپاه با زدن پایگاه های زمینی آمریکایی ها در منطقه به نظرم دارد می کوشد تا تاریخ حمله را به جلو بیاندازد و نگذارد آمریکایی ها بسیج و تدارک کافی داشته باشند.  وقتی می دانید حریف می خواهد حمله زمینی کند خب طبیعی است پایگاه هایش را بزنید تا نتوانند آرایش مناسب…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19289" target="_blank">📅 21:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19288">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8GQG7-w3d1epOSvVxy4yZYUMnOu_OS4ZuipWe50vyaWOllzR3eGkk5_tS81dp9JN1Tdc5RGbtlqRPTmAxD_Yes8HyCTTCz8EPszGwBqI3uSB9hwoW7SnY9Q2YTetKQPKCpDYbacOLF_UIStXW7Qgklve_Qg9MSLbI29UWAk5xHJSqASym-CpyIeC0-kxbJvUf-D88yZAiMdgYDx-hquc0F36kxxlGTwOao6UL-U2AFqJjzl_Jy7AdIYHdSyXp3Z1rnuTbdgElgnLjNXavztWVeY9uPyq25u6sFC9CCkRv2GaKPGZ8VwOK21_2eBm4ZsbFT9DIRjjLY-aj611-SUAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت های پیشا—گشایش نمادهای مهم در بازارهای مالی
ریزش سنگین بهای نفت برجسته است.
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19288" target="_blank">📅 20:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19287">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عراقچی:
زلنسکی به دستور اسرائیل به کشتی تجاری ایرانی حمله کرد تا اروپا را به جنگ بکشاند
‎</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19287" target="_blank">📅 19:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19286">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وقتی میگوییم اندیشه چپ باعث زوال عقل (و البته شل شدن ناموس) می‌شود یعنی این!  شاید فکر کنید این صفحه دفتر دیکته سید محمدطاها ۶ ساله از مندآباد باشد، اما نه! این نامه غلامحسین ساعدی به معشوقه اش طاهره کوزه گران است.  لابد با خودش فکر میکرده چه کار بامزه ای…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19286" target="_blank">📅 19:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19285">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZI-P1iRJi6uidJTwKkKwJmqvKePQWwbtiJpWRb5MUjgODasa4Rtj1_CfBxjCbPl8vdPIBCy9IXS0sbpLHE2nIM4q5XCBAE2yXLL1GlQPMrKdNvqRno3jIc_SXyyCr8DvCV9m_3IBacovnaPnW9oCi24HQSDZXghLxgViVKtfu1TT-wDz2b89pW7f4BgX-Gl5YmxQZxHRj8U4mfx4EXe_vpFzLxVGQg9G18pNSqdnyJ1xx8-RnQEAMpPA4qKpWSatfKKi1DX5Yndzj1FpP0egxvt5ONIrSUPXgUf-pR9asDn1Ay7XZ0XgnWQocebn0Kw5oYWNfUJg-aHINBF3WjW7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توئیت عجیب عضو کمیسیون انرژی مجلس:
فقط نفت!</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19285" target="_blank">📅 19:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19284">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxvFtM2BIx44klZuHk-e2H1Ivexvow2RZgbQvcRu7n9XVnD8pn7Cmq9j2N5lFT_Aic3Ub75V97WspOpnTY-kn5VDUZenJx_2rm8vlXQhintH7vLfcgZ98ePhiZehzBo7OxunNt3i6R_tllOuO3Pt1DLPZBlVBefCB8klzv781E7LgKlFoAgDhMfPt59R_pTVSbUBxumSwJI4us0fMQMrdcRCYBF6pDNyFHeBPeQMqSiNMR4q13QJ6q0KIpfalRqehshLz1Go6sYP_J0cIZt8NeH8vBN9CchtL0jlpql73mJ-uKUGwahdt1J-fKW-0CxPP2udrgyTbLXXZe-q7vxRzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استالین و بریا!
بریا رییس سازمان اطلاعاتی شوروی در حین جنگ جهانی دوم بود که هم حمله هیتلر را به درستی خبر داد و هم با سرقت علمی از آمریکایی ها، برنامه تسلیحات هسته ای روسها را به نتیجه رساند.
جالب اینکه او پس از مرگ استالین در سال 1953 اعدام شد!
#تاریخ</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19284" target="_blank">📅 19:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19282">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نتانیاهو به فاکس‌نیوز:
جنگ زمانی پایان می‌یابد که نظام ایران سقوط کند یا چنان تضعیف شود که ضرورت پایان دادن به برنامه هسته‌ای خود را درک کند.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19282" target="_blank">📅 18:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19281">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d5b002cb.mp4?token=GpyhGQjHLn3reeqpJ74kkFS-mEviD-JVwcMBprV4aEDnKqy2Jm7hfLaZKrCv9U8I4rhixlgw78neaz7sPtTrVAKSxFntRHEmLjwn4xG9xkh7v0fiDaxEqYn9SXb7cJo8-kXWJQwemt4ffT858b8gfb_ELnqKHERTRUdkY2N6jqGsFmPUsRD1VKLDTYO_j_ZVBcdp7WwJbhtplNAVUnsKG2gfncVdEv4ZkC-vZ2t1g9_yajoUKGf49jrC2cAZCR84QiEBrEeICdWsOAWMyrJUYcXAN6YuCOCCNGcs12lc_W_3mSeXLhrLPBA-twK550dt5STEQjSIhtRzxeZwJlcsgX_L2YTp4DMRz4-AINNTTXX9gnQ4-tu0zuPr7uO0tr2LCVm54XhL4kBQIDEv7SoYgDUBlwYHHi4amN5KDGYDRyjAMg50rUzsfTVOhwIPMUWoKUCRyM-awS-iR24DySc-lwGNj_t-GRcxIG8aaJH8b9eOkFaZKCksIjpcE4JcBF-TLWumg10sCORsQNlzRqE9EP_qRjWKRZhTg-0SjwxsAuvjITqTKI8aTKukG1NwTiK5Mxl65_26Btn3L8it-0syqfvh8EXbUuNRWPncLGLu0Rnev42JdXnlb0Zr8eIaq_ghetS1yRyIbpAnhx7KR7F_d4TE1UJy5TLX8RANLM_fhlM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d5b002cb.mp4?token=GpyhGQjHLn3reeqpJ74kkFS-mEviD-JVwcMBprV4aEDnKqy2Jm7hfLaZKrCv9U8I4rhixlgw78neaz7sPtTrVAKSxFntRHEmLjwn4xG9xkh7v0fiDaxEqYn9SXb7cJo8-kXWJQwemt4ffT858b8gfb_ELnqKHERTRUdkY2N6jqGsFmPUsRD1VKLDTYO_j_ZVBcdp7WwJbhtplNAVUnsKG2gfncVdEv4ZkC-vZ2t1g9_yajoUKGf49jrC2cAZCR84QiEBrEeICdWsOAWMyrJUYcXAN6YuCOCCNGcs12lc_W_3mSeXLhrLPBA-twK550dt5STEQjSIhtRzxeZwJlcsgX_L2YTp4DMRz4-AINNTTXX9gnQ4-tu0zuPr7uO0tr2LCVm54XhL4kBQIDEv7SoYgDUBlwYHHi4amN5KDGYDRyjAMg50rUzsfTVOhwIPMUWoKUCRyM-awS-iR24DySc-lwGNj_t-GRcxIG8aaJH8b9eOkFaZKCksIjpcE4JcBF-TLWumg10sCORsQNlzRqE9EP_qRjWKRZhTg-0SjwxsAuvjITqTKI8aTKukG1NwTiK5Mxl65_26Btn3L8it-0syqfvh8EXbUuNRWPncLGLu0Rnev42JdXnlb0Zr8eIaq_ghetS1yRyIbpAnhx7KR7F_d4TE1UJy5TLX8RANLM_fhlM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی جالب است؛  از 6 کشوری که شدیدترین بحران های انرژی را تجربه می کنند، 4 کشور در منطقه ددخیز خواهرمیانه هستند و 3 تایشان (سودان، سوریه و یمن) در ژنده پارچه ای که به عنوان پرچم رسمی معرفی کرده اند، رنگ های نجس و نحس پان عربیسم (سیاه، سفید و سرخ) دارند</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/19281" target="_blank">📅 16:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19280">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بیانیه وزارت خارجه در محکومیت حمله اوکراین به شناور ایرانی در دریای کاسپین!</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19280" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19279">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">با این وضعیت می‌شود فهمید چرا ناگهانی تصمیم به دوبل کردن قیمت بنزین گرفته اند.  وقتی عرضه سقوط کند، کاهش تقاضا با جهش قیمت یک گزینه است.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/19279" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19278">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwx6xxg70EdPOJaCiTJccbmJEdRNZ8m5BFytVTM51x7pEvnRk8Zci3X0VGUClnQuJ1hNwx4DO1KJ1JwPOOlm1UFPErtUIiQrA3W2V8eEbd394uPNapoXbK75Rsp8FHQB98z3InXdgv0rW8-w3KEDdQG0-etFc6mRXvyw8AeSncC5YRdNHeCYnDN6141FPzvu2a7sJGwMthqy3_n8KJGm2dZDJStdUeKo1ISXeNLNL-8-2XiYeOLeq9mJFd-EpSIsPlI-kLqNqdLcxnFVR8gDDdbtJU9kimrhpzrf6lWpm8w52NL-qPs2vw7ZvCt72QvO_6CthtO7z2r2mPPoXoCZdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روس‌ها نوعا عادت دارند انتقامهایشان بی رحمانه ، مبهم، نامتقارن و شکنجه مانند باشد.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19278" target="_blank">📅 14:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19277">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">روس‌ها نوعا عادت دارند انتقامهایشان بی رحمانه ، مبهم، نامتقارن و شکنجه مانند باشد.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19277" target="_blank">📅 14:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19276">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">وقوع دومین حادثه دریایی در دریای سرخ
سازمان عملیات تجارت دریایی انگلیس از دریافت گزارش حمله به یک نفتکش در آب‌های نزدیک سواحل یمن خبر داد.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19276" target="_blank">📅 14:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19275">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">برای نخستین بار در جهان!  کشف قله تنگه هرمز توسط اژدهای بندر</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19275" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19274">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312e3c4284.mp4?token=TkxcvP3QP8V0JgBOBOC-33lL6_LbTO96aZLA_Xb5Fm5mz27Eu7AO0zGI9hfqRbGw14PdOOIDJqqeuzpTyH8hfogf8bmwgC7ZiV2yVg7GtqAOmMLrJA4ByiF8c-e_EHfRYt3VuoBoWo52AB4xPDuFG-Nld9J-WLK66fP5s7kWHbA3TYZbfzN4fSpWA0thzhabnjDZ9FlzmXphw2PfT9DihJ98zABUGw57RifaWrPLUflYLwUwp9l-9pZdl42oH7W1iH39uWCxDzdxMC8MBjNIBHY9O7qlN7UJDcnQXCXM0URyyiQ58dGJ59NKN0zxowxj6nwh2ruQGyJzUuC5vG0H4B-ag71S_CcN4hWnMrqxBbk5oCIcvPQQuxokZwUZEBIHe5UHQUTmvFpSIZga7oJAvNtQLVUX9IlzrYACg2LFjmbZlYj3CMVn73NUleg4uyw14gMgitceLm8QQqyfLaHXfqZuzn_je-1K6GYDhtrvs8ZAl4B4RRCZCKPY4N5ZZJIt_rnfO5n65QnPt_EVhY8zXbbQSk4gzSuk0r2gS4hwg4M3MIThZngCj4E4IoYblZnA7_XgG5sQEi9LXwH3pn0-LsUQjiG1kO5gjLouMYxIONwjfWZu4UKI8wGj902EC2R1V4zKPgwyAyQQWzXMLNqQ2B7eiMuLUP_3CoLUUu_xmxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312e3c4284.mp4?token=TkxcvP3QP8V0JgBOBOC-33lL6_LbTO96aZLA_Xb5Fm5mz27Eu7AO0zGI9hfqRbGw14PdOOIDJqqeuzpTyH8hfogf8bmwgC7ZiV2yVg7GtqAOmMLrJA4ByiF8c-e_EHfRYt3VuoBoWo52AB4xPDuFG-Nld9J-WLK66fP5s7kWHbA3TYZbfzN4fSpWA0thzhabnjDZ9FlzmXphw2PfT9DihJ98zABUGw57RifaWrPLUflYLwUwp9l-9pZdl42oH7W1iH39uWCxDzdxMC8MBjNIBHY9O7qlN7UJDcnQXCXM0URyyiQ58dGJ59NKN0zxowxj6nwh2ruQGyJzUuC5vG0H4B-ag71S_CcN4hWnMrqxBbk5oCIcvPQQuxokZwUZEBIHe5UHQUTmvFpSIZga7oJAvNtQLVUX9IlzrYACg2LFjmbZlYj3CMVn73NUleg4uyw14gMgitceLm8QQqyfLaHXfqZuzn_je-1K6GYDhtrvs8ZAl4B4RRCZCKPY4N5ZZJIt_rnfO5n65QnPt_EVhY8zXbbQSk4gzSuk0r2gS4hwg4M3MIThZngCj4E4IoYblZnA7_XgG5sQEi9LXwH3pn0-LsUQjiG1kO5gjLouMYxIONwjfWZu4UKI8wGj902EC2R1V4zKPgwyAyQQWzXMLNqQ2B7eiMuLUP_3CoLUUu_xmxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای نخستین بار در جهان!
کشف قله تنگه هرمز توسط اژدهای بندر</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19274" target="_blank">📅 13:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19273">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">در حالی که اساساً مزیت پهپادها در کوچکی و سطح  مقطع کم راداری آن است، ترکها رفته اند یک پهپاد غول پیکر (همین آکینچی) ساخته اند که ابعادش دو برابر یک فیل است!  طولش 20 متر و عرضش 12.3 متر و 5.5 تن هم وزن دارد!  قیمت آن هم بسیار گزاف بوده و بین 5 تا 6 میلیون…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19273" target="_blank">📅 13:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19272">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHlPpIO93SvCj3J4oZmCyHt4KgSpw34JelHkxilViu2v2JFlALRp9PTKccGqE-hc5aDiANpV8lQ095yTTZN04WZy4LtZKKAnc50DkaG6rsGAyqgJxFmVT_QQNEPWSQk_ylDUK6bGRMuBdMX5H-zPmiX7CL3MKak3_mm1T_br5G2jsQnLTw1vTXscoBFdGCFoOfvP2KPgWmUu6twFSOcdnMDtQJ2FMENAeTB4HY7WRI8KMTTiU4Zkzf_kju3cS6parNzr2X2wIeffGgXPI7ouT0KlShTwv59w5c_STeRkc_00hum2KlqnWIYf_ciLx7j6NW2FhlgDzBi2q5GNhpqOHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزان بالای مهمات پدافند موشکی آمریکایی ها در جنگ با ایران</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19272" target="_blank">📅 13:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19271">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6066f7963b.mp4?token=pprqBIs88P-AylsuOycI6lSd-HsX4WkiMey935YqC2RUz7WYGIjRWvG74rug9Oq9gEb7LN7KeFp6RMUuKFEotOu3cQPr1wAMWJSyuYAanFSNix9tYPixgT33ODq725JCWNwX270J5hfiosdAdtgFIAGTqkt-KdJ3ohRKNBPiap-lSKogT6HSVVGDrWjNEP4gF9RgnkLYaanF5GJv_XEahOKu9F41vmR8stN9DR1CtLNZx-BiqVo6tUI2jAPw5wSMyCcvX7umYNjhh5bLpZUVoynzWnxsUXPrGnabkq1TugxOMHZDRJT95JZbTiGW52w0C2SYLRyj_SFW6WJAdmVfMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6066f7963b.mp4?token=pprqBIs88P-AylsuOycI6lSd-HsX4WkiMey935YqC2RUz7WYGIjRWvG74rug9Oq9gEb7LN7KeFp6RMUuKFEotOu3cQPr1wAMWJSyuYAanFSNix9tYPixgT33ODq725JCWNwX270J5hfiosdAdtgFIAGTqkt-KdJ3ohRKNBPiap-lSKogT6HSVVGDrWjNEP4gF9RgnkLYaanF5GJv_XEahOKu9F41vmR8stN9DR1CtLNZx-BiqVo6tUI2jAPw5wSMyCcvX7umYNjhh5bLpZUVoynzWnxsUXPrGnabkq1TugxOMHZDRJT95JZbTiGW52w0C2SYLRyj_SFW6WJAdmVfMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران هر روز برایتان یک سورپرایز دارد!
توحش و بربریت یک مشت گوساله در مراسم رونمایی یک یوتوبر ریقو گه دیروز در ایرانمال برگزار شده و ۵۰ هزار نفر در آن شرکت کردند!
حالا بماند که گوشی عستاد را زده اند و دست و پای ش هم شکسته!</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/19271" target="_blank">📅 12:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19270">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTOkQkFr56YsqHe9TFkMWLFFm3mYjM4eLjxECORahUTwz1ny-F47mN0GX5lNaBS5swlc6ql6HFzQeeaK2xaKLgnJBS5PAoEn__9Yz6ZVbkfrq6s09gJ8Um68QzuxXV4SF8-LWTxV0X8mNQN3fQmEkkQC8XjKiiKy5QGjouc_DAKzM0HojPl1_WUohVEE9IODmZSbPpBc5jJuMamDZz9FsCx_7Y30yMUO5OtYE8XvgvyuhhD-2GhAbSdGK9RTzlDIeB06c6BYQ9veMWgULOavMf8rmHkPuOU-NZtMIN_OH4aAvyZ5YVrlbzdeG2z6PJ_Gg4G1q9WlSXHXk_SQOO4tcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این منطقه سبز بالای مرزهای کنونی یمن که جیزان نیز در آن قرار دارد، تا سال 1934 متعلق به یمن بود که در پی جنگ آن سال به چنگ سعودی ها افتاد.   هنوز هم برخی ملی گرایان یمنی نسبت به جیزان، عسیر و نجران ادعاهای ارضی دارند و آن سرزمین ها را مال یمن می دانند.  #تاریخ</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19270" target="_blank">📅 11:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19269">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjDBmy2Cl1ljoHnD3NCaqZxMAQtxqm9qjwfvzfGCxS2wMlfLPTWE71SrYf4VY3mjAw5O2C0czYnePe0MJnD-pxN7Haa51DVz5U2N5b_q5dfbE-HlEIDI6ljDCgiYE9QFn4iho3WSAvI3pODPc3rfSGqoSjHJ8mlZqpOJf11utzDZtGj7xiN-RfbXRbkaedraGVDQuXOAnjLa9Ls2628ZNOYL8gUZZzxxrCKK8cnOZ0C6aTfvyQh-bXwtD1pSjrMjMcnPVT4UUgBB0-CDG3uGpL8MNO7rF7g20rrf751K0-oXTS6sA_J2FY7DH8dQuKYbIoOjhxerbnYDPngcU2ri0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زد و خوردهای 2 روز گذشته حوثی ها و سعودی ها به روایت تصویر</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19269" target="_blank">📅 11:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19268">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVi3i6eUdKhX49n0qVa3x2chf8U735B8JOT_6LpPvvbZu6o-r3yq2K3ElPq10SiQ1daaM-Tf-_KpXN_rWFM0dr5LlPwMa5Enh1GYGlMZhYGXh2osXHtkZr3SGZckVa5TBMxMhRgrQehPT662s-q_qjBSh9294WAnFMcg8xtryY_G8gHzsyfSD6BNJJQk3mvOUDbsexnK3pLp-byGHoPTm58yFQaTlyftFlVl_6zvFJY2rCOQWcexLyPWQ4WOZMQWRWoeQe2Dk1J22DILmaqbzGxurdR5czsDmFTzZ4Qcga2B2keHkfRrUTA-klm_4UHeT9m3us4_Wag2k9NnI_zpww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زد و خوردهای 2 روز گذشته حوثی ها و سعودی ها به روایت تصویر</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19268" target="_blank">📅 11:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19267">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بقایی پس از مذاکرات دو روزه ایران و عمان:
مفید بود اما تغییری در وضعیت تنگه هرمز ایجاد نشد</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19267" target="_blank">📅 11:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19266">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c9dbca0a.mp4?token=mkO48m8o07z5OIxTSN2It5TbArGx3rskkMSD0MFlOW9IxvCtyJZn9Yx2llmjn81LBjGm7xQ3-ymlUNoQ2w1CN3wkopOEdbFBBY7toMi6xhgrQvVQf2lg71VxFO78L_hg0TbsZ44lBSv5h8a1t6Hr7Jhv9D3envGDQN4gDSLOROiCQ8fVEDxIV9TSzbKGE8ssmGdh0jxXAoUk7wi1sSIXyLE04Idx9KAKGE5JbTR-niMSxTdHTTIoklkx8wKH_Qn9LqVdcvs98S1zgcFo0g7eWbmMBu7S6-uoLZ2zrFDxiV4y02eRb6NP8vqdWR382kz_seLqVit283y8GDCBf54GpryBVKYVJo2XjD2RYjLlcHE7FfSqwahPw2FZ5EsQIKHOPRtm2n_02of1tO0Y-PZTJSVm1SlgwWYgONzNpVHE_59xHzzPF8vwBzI4bj7UHTjME1WQp5AOpbdMzrRqbCEcuV2Py4lB-MrhsMIe5oMVzYaJUPY5ZacT3zxVZ8-rNxJzokiUiSuljNBKzh7Rq_PRSa_JpUyzCa8BAVMa2J_GEkaq9sORZt3UBqGTgK_Ka_rLJCMi5cm_39SjhOKGUUGI3cOVQ0st131PIoEg15fR6S_BQ3vTC8PcwCVUcTreIBcHIbGk8d9KVrWzl_EGcbxLNEqp7DzqnHeR_nEYX8XBIYE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c9dbca0a.mp4?token=mkO48m8o07z5OIxTSN2It5TbArGx3rskkMSD0MFlOW9IxvCtyJZn9Yx2llmjn81LBjGm7xQ3-ymlUNoQ2w1CN3wkopOEdbFBBY7toMi6xhgrQvVQf2lg71VxFO78L_hg0TbsZ44lBSv5h8a1t6Hr7Jhv9D3envGDQN4gDSLOROiCQ8fVEDxIV9TSzbKGE8ssmGdh0jxXAoUk7wi1sSIXyLE04Idx9KAKGE5JbTR-niMSxTdHTTIoklkx8wKH_Qn9LqVdcvs98S1zgcFo0g7eWbmMBu7S6-uoLZ2zrFDxiV4y02eRb6NP8vqdWR382kz_seLqVit283y8GDCBf54GpryBVKYVJo2XjD2RYjLlcHE7FfSqwahPw2FZ5EsQIKHOPRtm2n_02of1tO0Y-PZTJSVm1SlgwWYgONzNpVHE_59xHzzPF8vwBzI4bj7UHTjME1WQp5AOpbdMzrRqbCEcuV2Py4lB-MrhsMIe5oMVzYaJUPY5ZacT3zxVZ8-rNxJzokiUiSuljNBKzh7Rq_PRSa_JpUyzCa8BAVMa2J_GEkaq9sORZt3UBqGTgK_Ka_rLJCMi5cm_39SjhOKGUUGI3cOVQ0st131PIoEg15fR6S_BQ3vTC8PcwCVUcTreIBcHIbGk8d9KVrWzl_EGcbxLNEqp7DzqnHeR_nEYX8XBIYE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عمومی بودن اطلاعات برخی نقاط حساس نظامی - امنیتی در ایران</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/19266" target="_blank">📅 10:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19265">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پدافند غیرعامل به زبان ساده</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19265" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19264">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3_0HkRs0QzGwAsvyJZKaRevUViAPYAXcBUlmrafzcWk6RrFJXeKqkdwEmAg4VtucCy61GDE5ccUywv6VyaOuzzlNRUfqVS_BcVqPdBm_8UF7bDnGWtjCd_qU4Vi1Hdbjp5XdFQeR-GrJzSSVwSF5VOq0JeV3dL4b05gLVcIx3s5kFgojUwrTSKDhocN89xwxRZrbHaTyLEJt3yqq387HMvRvmKwkmNTb3r74K7eJ0LF9xOVBRInPVt5K0o2tYZZsuMwCcP3W173LucIkxwVUscS5ZdNz0luwYEW6lfHMo-ZBKw9QouFgbRr8lPmETxAr84ZNjOijlxN5sHADvUAmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/19264" target="_blank">📅 09:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19263">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نیویورک تایمز:
ترامپ، حداقل فعلاً، برنامه‌هایش برای تشدید قابل توجه تهاجم نظامی آمریکا علیه ایران را به تعویق انداخته است که دلیلش نگرانی‌های ویژه ای است مبنی بر اینکه تشدید درگیری می‌تواند ذخایر رو به کاهش سیستم‌های ضد موشکی پاتریوت و سایر مهمات دفاع هوایی پنتاگون در خاورمیانه را به شدت کاهش دهد.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19263" target="_blank">📅 02:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19262">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">انتشار برخی اخبار تاییدنشده از شنیده شدن صدای انفجاری در بندرعباس</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/19262" target="_blank">📅 00:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19261">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">آشنایی با پهپاد کشنده اوکراین  پهپاد FP-1 (Fire Point-1) یکی از جدیدترین دستاوردهای صنعت پهپادی اوکراین به شمار می‌رود که در سال‌های اخیر به یکی از ابزارهای اصلی کی‌یف برای اجرای حملات راهبردی در عمق خاک روسیه تبدیل شده است. این پهپاد انتحاری دوربرد با هدف…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/19261" target="_blank">📅 00:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19260">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی حملات هوایی را در منطقه دمط که تحت کنترل حوثی‌هاست، انجام داد.  این منطقه یک خط مقدم فعال بین نیروهای حوثی و نیروهای دولت یمنی که از سوی عربستان حمایت می‌شود، است.</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/19260" target="_blank">📅 00:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19259">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اگر تُن ندارید دستکم آماده باشید!</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19259" target="_blank">📅 00:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19258">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19258" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19257">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بیانیه وزارت خارجه در محکومیت حمله اوکراین به شناور ایرانی در دریای کاسپین!</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/19257" target="_blank">📅 23:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19256">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLG4RchhYSO9HXV1P9eg4gw3GzHL5K7XuB_E68-_p_pV7AbGnXmwckRWJLc7wNL73I05p1JcLDGzVV7Vels8jqB2Hv4ofaDPMBFUAw9i0QZyVgoZtuDI0AdnyiN_G9gAXkG4e1JYbRppw_2PF2cwnSk3Iu72MqUxKU_QmLP1eWVrIl_OWLk3Q7DoeSRpcw0Pe1k7DKivOLM9kvI7ReVdSbAUhXw5j_P3tYiRZeTu1thTKxS2wRBYUUMxfz_RQekb2r6hfVCRMoVqzfFzlAwNf6p8AdSe_zSVBHu-7rP9Sy52ytkHnu2tpr-8b-4dRYmKZDF5jUOl94eEG9Xv3KjCtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید هم زلنسکی دارد جمهوری اسلامی را تحریک به پاسخگویی نظامی به اوکراین می کند تا رسماً پروژه تسلیح گروه های مخالف ایرانی به پهپادها و ریزپهپادهای اوکراینی را استارت بزند.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/19256" target="_blank">📅 23:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19255">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سپاه پاسداران:  «هر کشوری، چه بریتانیا باشد و چه دیگری، اگر از آمریکا در جنگ حمایت کند، برای ما هدفی مشروع خواهد بود.»</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19255" target="_blank">📅 23:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19254">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">در عملیات 2 شب پیش دو فروند بمب‌افکن B-1B لنسر نیروی هوایی آمریکا از پایگاه RAF Fairford در بریتانیا به پرواز درآمدند و در بمباران جنوب کشور (استان خوزستان) نقش داشتند.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19254" target="_blank">📅 23:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19253">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3c53p93GohMaMxDLU-uo5QZItkEA1Shv89HeZTtG7wclU-3XIoK7jnZPT_0QWwKxqmfjpnQB6KRQXQ7ikY5N08Dnxb4aFPsFM0iqwlb7PqPmYqZ4uGqJUkqCqoVzn-c5DPp7dF0eM2KAdAiJyCn7y9kAZBRQMJPBoHy_a_GjovvRcxp7bqbbasu1ShvoIiDjuSa_GtHlUaXowOiWFammahPxKfCR00_cEi1j5auitZnoRsNlkLLSV2rJtg1J6JXb5UHiA7SEqwFWuajHb2nkbyuSzV6K5lAbj31yJxrHj01Ztn5EvyV9b8kjSAj-kSp9OYVdgWSjl4acsIexhqE1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عملیات 2 شب پیش دو فروند بمب‌افکن B-1B لنسر نیروی هوایی آمریکا از پایگاه RAF Fairford در بریتانیا به پرواز درآمدند و در بمباران جنوب کشور (استان خوزستان) نقش داشتند.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19253" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19252">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نیویورک پست :  «دقت وحشتناک موشک‌های ایران» این هراس را دامن زده که دشمنان آمریکا در حال کمک به ایران برای هدف قرار دادن نیروهای ارتش آمریکا و CIA هستند!</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19252" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19251">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ درباره ایران:
اگر ۱۰۰٪ آنچه از ایران می‌خواهیم را به دست نیاوریم، قطعاً از سرگیری جنگ تمام‌عیار را در نظر خواهیم گرفت.
منبع: LCI</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19251" target="_blank">📅 23:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19250">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی حملات هوایی را در منطقه دمط که تحت کنترل حوثی‌هاست، انجام داد.
این منطقه یک خط مقدم فعال بین نیروهای حوثی و نیروهای دولت یمنی که از سوی عربستان حمایت می‌شود، است.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19250" target="_blank">📅 23:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19249">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">شین بت از خنثی کردن یک ترور دیگر ضد بن گویر خبر داد.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19249" target="_blank">📅 23:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19248">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رسانه‌های آمریکایی: به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد تنگه هرمز خواهند رسید.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19248" target="_blank">📅 21:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19247">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">این هم موج شماری
😂</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19247" target="_blank">📅 21:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19246">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HT0KbumU8H1_k-bLfUuMCyWKCiUN7w494SDM0frxH3ld3babZLBUF1nbVYbOEPdU2NmdNWS-tED4gi5mrN_KSpPF4SUxHLyU5JxOwGE46y5rh5cKSc-Q_wtUIWj6Ly6HX3GQ2V3TYhHFD6ZaszLoejmEAt9h1UJDSPedkq2C8yHCPLvxc6cNkP6seaRkOKAGNummrckDPRu_BX1C-0WR3OqQAz1XIoSJJVNI6pbn2HsQ8GB_wwDvJFWBwW3wY_mFZMNjDu9Ow7-4YDLsytmz8_5BlwQDOLXpRel6uJYOmiIjCGOYGi6B20kNRufBPIFWrvpU7ro86AG2xNzlpI16hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم موج شماری
😂</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19246" target="_blank">📅 21:34 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

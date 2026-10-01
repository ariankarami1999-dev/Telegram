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
<img src="https://cdn4.telesco.pe/file/twB2f5s8u8cxNRFStLaAIydVA4yvXu-8XXfU6EqeAFU8fRKfYnWIJan_V5xbIO2JS1jwU8p-RtnQc_DWSwH1eTm0pq13vqFpTnmcIwIhdIYxxqMfvGcLfSuFE3k_olntFJYSUMnsw7xl_w0lu5Aj1NlsBMkHc1ZqlqtwCue0gy6A4OKYS8mY43U1Bh1IG3Zgo5zdAAleaWYU7aksCx09uOb0dmw-GFg7Qbuu6XPGQTon3eN1StGNWkCpaJ9dCMhwrrPF1X2HKVzAb5Dc82UN4NKjBSm9JalgFBmTBHubu60UM9YuHpEg_dBVl7IkEWFzQeN1VKsjL44hria09xlhTg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 22:39:44</div>
<hr>

<div class="tg-post" id="msg-72597">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaetEoFG7S1IG6D7pyg1rHtRpmypHQPUj67-eOTqq3xX6s6miEP0Xs27xPUcKS15jvFyKa6OBA1fd1ggnDPvMebrb5CipOGWGVAuhPGlJwemfUvjwwHXLPtjFfkhvYOL85tVW46vOoyQ5s0gBPRsMVEWPs14zolD5RzLQRZQvswjyWz7hfU4lLhNdCwzaVU-zAI4fNVx8CtLylyghtg6U1o3nMAKkF3qmYXsrjdHJ0_GYkQTq7P_N-BuJhdbgQsN9sr6WLs6jq512NIru4-zCzidlR8GD0aMX1mC189ZENJEb967pYvoYBWP_Md7x6dGfCriB891HHe516cvDfHgyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛پلیس بریتانیا اعلام کرد که یک تبعه ۲۷ ساله با تابعیت دوگانه بریتانیایی-ایرانی را در مرکز لندن به ظن «تدارک اقدامات تروریستی» بازداشت کرده است؛ اقدامی که با حادثه روز یکشنبه در نزدیکی یک پایگاه هوایی در انگلستان (که مورد استفاده ارتش ایالات متحده است) مرتبط دانسته می‌شود.
دو ملک در این منطقه مورد بازرسی قرار گرفتند.
مأموران مبارزه با تروریسم همچنین از مرد دیگری که تبعه ۲۶ ساله بریتانیاست، بازجویی کردند.
ویکی ایوانز، هماهنگ‌کننده ارشد ملی در بخش پلیس مبارزه با تروریسم، تحقیقات مربوط به پرونده «گلاسترشر» را «بسیار پیچیده» توصیف کرد و اظهار داشت که تیم‌های تخصصی در حال پیگیری «چندین خط تحقیقاتی» هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/news_hut/72597" target="_blank">📅 22:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72595">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_zpWOm7vuusdaFYHdFTiRvdNp9RH8PD0_AK8SG2jOdHF5G70RI1vEMC72UAxI-MQ2hL8bzM1P1poD8Xn-paNP0uglydIcPldfKn9PkfDIeC90myppW3h_ALviAH2lyuege3r5Ge7pph1MoVRYjk1vuUoAUBuBj9xeV4BeBZfB1KLAXhbPw6QDIGxqlKhjGyd9z6EYtWScLCSuI-mC09IlIH58nmJwIjSpejIUII3_V5EcX0j5KlRQqh6nYpzgKv3W_uqePVUmniEo6y7BOuG0k9-8dGUZLP7JjRFcJV1XZSekC8swjpy682ZCbqvhmQ2ziHE4p12vXIV0UQWgtVYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b5d4066c.mp4?token=CpQMTT7wzFovSHAW5JOLJvXgkddUQUK-GXK7eLvrtliP1ttWehyRjgk5L2G9luZB-a9t0RRDH_Hjy1I7xUaIFKRcE-ppBgcmJzvuQQ7ZThAqPVqdM-pxZ_hxe420pxYtCtv--iloEInNwkhlcIFdVabLFdx3ItDuIgB-be5c-w6_WvN8YMbEa0vK0zEXrUESIzikXFEtkZUtOs22-iYhsAV1O6JoR4GSzpBVEQ4M6CS5du6A8fO-qz2qhe9juHWlyXg10EYPK6OyXAFVULXKJvlI-APN8rfUcIED7AUrjy8lHxsoS0RZGl_StLoNmdUihwS5aGc8s9AprDdNY5Cydw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b5d4066c.mp4?token=CpQMTT7wzFovSHAW5JOLJvXgkddUQUK-GXK7eLvrtliP1ttWehyRjgk5L2G9luZB-a9t0RRDH_Hjy1I7xUaIFKRcE-ppBgcmJzvuQQ7ZThAqPVqdM-pxZ_hxe420pxYtCtv--iloEInNwkhlcIFdVabLFdx3ItDuIgB-be5c-w6_WvN8YMbEa0vK0zEXrUESIzikXFEtkZUtOs22-iYhsAV1O6JoR4GSzpBVEQ4M6CS5du6A8fO-qz2qhe9juHWlyXg10EYPK6OyXAFVULXKJvlI-APN8rfUcIED7AUrjy8lHxsoS0RZGl_StLoNmdUihwS5aGc8s9AprDdNY5Cydw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ترامپ در‌تروث پستی از اعتراضات ایران منتشر کرد که مردم در آن شعار میدهند «امسال سال خونه سید علی سرنگونه»
@News_Hut</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/news_hut/72595" target="_blank">📅 21:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72594">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQiyHdajGvBONX6QbRG216ua2qWU5cfLFrZJiyRmUlubgUW2DCe8Ay6VIztPUo4whSJix2wCdPHKdH1ChtXBUQh6mNGINfWQEGSEh9V56WC3HyqzMSs1YbSTPhgw1AkPhXgsWrM18uWJnd7Rwa3QfeHLK4EvPO8beN2hys-Hqhgt5-vIaKC_chZufGUm_WEyAKUTu2-UvAY7f8TfdqFttBQykZmdJTdxUJwrrr7WYZYEoT2e-Ftu6WwMpHA6w5f2x7ZulIzoAa20peeXa7e8dPahXcegfrluvhMor2Vmob61ftJAJULAlYkxL3F9t2KrluaswtqQb0z6xYAHRU-7Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت ترامپ:
«گفتم برای از بین بردن تهدید هسته‌ای ایران ۴ تا ۶ هفته زمان لازم است، اما این کار را در یک شب انجام دادم. زمان باقی‌مانده برای اطمینان از این بود که این تهدید دوباره بازنگردد.»
@News_Hut</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/news_hut/72594" target="_blank">📅 21:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72593">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/210cf276f7.mp4?token=sNlhwJcga0gwlMxpbid0rfVu1umgF6oL70G9D-7AsyyShWl2iwScG85JBjv6Ppnmyn-6kLy-z-qQyaFLVJ4t7TpL9E2VX9SWoH3cK3Q-2so92_uQJ1v7sEz43N3qvmiIyWUmD7NG8o-xtIjiGx6GHtXQUGyHgiBFlQXhpsQqrNooan6MH0Ru3kH42LCMAaxf77YkPTnTMdm5UPBlZDJDGZyl2Rp-F-vcSnHBYLyIzqfHHrO9Jln_cCZPkar_iL_Nzt-3-30rXg_6KLl-vc9dd_YJW_eEBpDFYPG-qE0wE-0QUgXBu5w_y6zRv7Wc5pwt6CIAyYfNcrX2buHtmN0Gxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/210cf276f7.mp4?token=sNlhwJcga0gwlMxpbid0rfVu1umgF6oL70G9D-7AsyyShWl2iwScG85JBjv6Ppnmyn-6kLy-z-qQyaFLVJ4t7TpL9E2VX9SWoH3cK3Q-2so92_uQJ1v7sEz43N3qvmiIyWUmD7NG8o-xtIjiGx6GHtXQUGyHgiBFlQXhpsQqrNooan6MH0Ru3kH42LCMAaxf77YkPTnTMdm5UPBlZDJDGZyl2Rp-F-vcSnHBYLyIzqfHHrO9Jln_cCZPkar_iL_Nzt-3-30rXg_6KLl-vc9dd_YJW_eEBpDFYPG-qE0wE-0QUgXBu5w_y6zRv7Wc5pwt6CIAyYfNcrX2buHtmN0Gxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیتر دوسی (از شبکه فاکس): آیا ممکن است این خلبان [در پرواز فلای‌دبی] توسط سپاه پاسداران در آنجا منصوب شده باشد، یا به طریقی دیگر افراطی شده و سپس تلاش کرده باشد هواپیما را سرنگون کند؟
ترامپ: بله، ممکن است همین‌طور بوده باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/news_hut/72593" target="_blank">📅 20:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72592">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31205a46fc.mp4?token=G7Ev7M-g3RPcmcV_NyB_wZ30jvrsSF1F0-m_sXp_uVeSarTedgHzDgj1z7V0mllfsC8ntZRO0CFwJh-YHDFKH1I3vJ7Q43HrSkq85gv7NBQrV2BPtYE7WdAw65bzuu9TYd-_YgTlZU9r-dHVfXqrga5PqlLwzcqeK6gYr88pyH8tS6BJHVac8SCAGpipYeu1BqyS9qoYlhp6Pc6dwgYJ7dFtgd7LjjMhVOYqjFtHl8FDOkxVaghRiTkqhTB2x-BmB6-0QXKEU08-ewjN2iE2xpEpfqHbbH82MZ55UOIK5rjiDj3Ii4kdWF2jAPj_XVaXy6FF3834aFrzxIlU4w-HGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31205a46fc.mp4?token=G7Ev7M-g3RPcmcV_NyB_wZ30jvrsSF1F0-m_sXp_uVeSarTedgHzDgj1z7V0mllfsC8ntZRO0CFwJh-YHDFKH1I3vJ7Q43HrSkq85gv7NBQrV2BPtYE7WdAw65bzuu9TYd-_YgTlZU9r-dHVfXqrga5PqlLwzcqeK6gYr88pyH8tS6BJHVac8SCAGpipYeu1BqyS9qoYlhp6Pc6dwgYJ7dFtgd7LjjMhVOYqjFtHl8FDOkxVaghRiTkqhTB2x-BmB6-0QXKEU08-ewjN2iE2xpEpfqHbbH82MZ55UOIK5rjiDj3Ii4kdWF2jAPj_XVaXy6FF3834aFrzxIlU4w-HGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات ترامپ درباره احتمال دخالت ایران در حادثه هواپیمای فلای‌دبی:
بر اساس آنچه می‌شنوم، پاسخ را «بله» می‌دانم، اما در حال حاضر مشغول بررسی آن هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/news_hut/72592" target="_blank">📅 20:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72591">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b0dca1ef0.mp4?token=OO4bcJG-a_3pb_72dbivvzEt8ZRa379vvEbEDI9k9UYAemi7fyybpj0kg3FonsV4Xnw1BfUKQ3f5dKOgr4jp792xffmbPeUN0pAR0Vj2jtz1MfigI9MsbB5lDjljscVu6toJPaLWARYVdumtCkvbnh4P8EcSkipkTb0jkICS3zmuekWvdQA4vSIXjC6TnCCcsrrPd4rY9GF8Ie8oOJtdRQ9SEZ_SqCtJCyTTZFU8Uv7gOB6XjKuEDoYia1ymdmZcPbHBMbqJYxkrJCZLCa6SumxREHxUYQqWwNsvMRfLGoz0mXIqkcuGkunwTvAvIBiRFaUH_xDEuj9bnHcL0dtbJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b0dca1ef0.mp4?token=OO4bcJG-a_3pb_72dbivvzEt8ZRa379vvEbEDI9k9UYAemi7fyybpj0kg3FonsV4Xnw1BfUKQ3f5dKOgr4jp792xffmbPeUN0pAR0Vj2jtz1MfigI9MsbB5lDjljscVu6toJPaLWARYVdumtCkvbnh4P8EcSkipkTb0jkICS3zmuekWvdQA4vSIXjC6TnCCcsrrPd4rY9GF8Ie8oOJtdRQ9SEZ_SqCtJCyTTZFU8Uv7gOB6XjKuEDoYia1ymdmZcPbHBMbqJYxkrJCZLCa6SumxREHxUYQqWwNsvMRfLGoz0mXIqkcuGkunwTvAvIBiRFaUH_xDEuj9bnHcL0dtbJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#مهم
:سؤال: در مورد نیروهای نیابتی ایران، مثل حزب‌الله، چطور؟
ترامپ: سرنوشت آن‌ها به سرنوشت ایران گره خورده است؛ هر مسیری که ایران طی کند، آن‌ها نیز همان مسیر را طی می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/news_hut/72591" target="_blank">📅 20:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72590">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ درباره ایران:
به جرئت می‌گویم که صددرصد مردم — از جمله در سراسر جهان — با دستیابی ایران به سلاح هسته‌ای مخالف‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/news_hut/72590" target="_blank">📅 20:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72589">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سؤال: اگر ایران پشت آن حمله به هواپیما باشد، آیا دست به تلافی خواهید زد؟ آیا آمریکا تلافی خواهد کرد؟
ترامپ: ضربه بسیار سختی به آن‌ها وارد خواهد شد؛ نگران نباشید.
@News_Hut</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/news_hut/72589" target="_blank">📅 20:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72588">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8061e95725.mp4?token=BUeZGZfNUTVS3aGVLFps8C-BLUXoxsF_VHDqAjIzBQTzq39xZ8SQ3vRrGzOaahqLsI9bF_qjTCQcLPo1r1NVha4SWFSlabXevLdyRNfXBvVh9EybnobS14B0rLnzl8Yl3CfK_fFbvLkWPHZAZdKBIoUxF4wgVBL34lQpCI2NiUb6DyH6YEf2KG6bxp9LGyF3_GSWV5VExU8C_1cNM8TOFQOU7ho3MPcH-wAsM0yf_V5BOk2oDm5Q8H6gYEB-Co4Pm3miF_XMgHnU-CnkZSATncdXxncH8MDPiWAg-MIO2ybBllM87hBN98nhOMKSK7GvbKBp_LxNms0LCmOFM_iXEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8061e95725.mp4?token=BUeZGZfNUTVS3aGVLFps8C-BLUXoxsF_VHDqAjIzBQTzq39xZ8SQ3vRrGzOaahqLsI9bF_qjTCQcLPo1r1NVha4SWFSlabXevLdyRNfXBvVh9EybnobS14B0rLnzl8Yl3CfK_fFbvLkWPHZAZdKBIoUxF4wgVBL34lQpCI2NiUb6DyH6YEf2KG6bxp9LGyF3_GSWV5VExU8C_1cNM8TOFQOU7ho3MPcH-wAsM0yf_V5BOk2oDm5Q8H6gYEB-Co4Pm3miF_XMgHnU-CnkZSATncdXxncH8MDPiWAg-MIO2ybBllM87hBN98nhOMKSK7GvbKBp_LxNms0LCmOFM_iXEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛رئیس‌جمهور ترامپ درباره ایران:
اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/72588" target="_blank">📅 20:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72587">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ درباره ایران: «آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند — و نخواهند داشت.»
انها توافق کرده اند که سلاح هسته‌ای نداشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/72587" target="_blank">📅 20:24 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72586">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خبرنگار: لارا ترامپ گفته است که جنگ با ایران ممکن است انتخابات میان‌دوره‌ای را برای شما به خطر بیندازد. آیا موافقید؟
ترامپ: ممکن است. [اما] باید کمک‌کننده باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/72586" target="_blank">📅 20:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72585">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72ce76f49c.mp4?token=G6gSADseMl-cRfn1HXl5dmsci0meI_NvSDctJ95pV98BNJ0RwRg6MwIZQo4QgKe1syOiZnanmDwW4fkH0qKjrDXLURlH-9wxmFtU0GZw82kx5WUFqPKR1eD2XrVOWDl-k7wogPcHFHs9zG74VuGbJfIO1XOo-3qYg2C1aqkbYNqdNa52LDZgCsdtM4G_0QA9hBjAkmXXewU4rtB6_GFOTkOnpxDcYE9Vqw1OH8SSwB4lse6vqNM8qd50N2xmUVwUAosnMVC66I_8k0S15g0V2F4ZnquvvC5sIFeA4plt_44Rjxt-bwYp8Y8GHmzJt3Xsuy_qenogFjfAZAP9tUPGxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72ce76f49c.mp4?token=G6gSADseMl-cRfn1HXl5dmsci0meI_NvSDctJ95pV98BNJ0RwRg6MwIZQo4QgKe1syOiZnanmDwW4fkH0qKjrDXLURlH-9wxmFtU0GZw82kx5WUFqPKR1eD2XrVOWDl-k7wogPcHFHs9zG74VuGbJfIO1XOo-3qYg2C1aqkbYNqdNa52LDZgCsdtM4G_0QA9hBjAkmXXewU4rtB6_GFOTkOnpxDcYE9Vqw1OH8SSwB4lse6vqNM8qd50N2xmUVwUAosnMVC66I_8k0S15g0V2F4ZnquvvC5sIFeA4plt_44Rjxt-bwYp8Y8GHmzJt3Xsuy_qenogFjfAZAP9tUPGxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ایالات متحده در حال اعزام گروه ضربت ناو هواپیمابار «یو‌اس‌اس تئودور روزولت» به خاورمیانه است.
تا پایان ماه نوامبر، سه ناو هواپیمابر و دو کشتی تهاجمی دوزیست در اطراف ایران مستقر خواهند شد.
@News_Hut
| NBC</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/72585" target="_blank">📅 20:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72584">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a42198336a.mp4?token=ACDuFQC9hEPZPfvuO9H-TgCBbT9horTJgFBeEvohASoWvWvp2dXiOcJ4py-0yFu8nuqdYbBBX1fdxNcIXwfqAuZiSKxGW4tkh8l6pqEmGqCwKrfRs_qS6v8xK8Zdm5v5A-bZh20DcAPgQPUBO0rHlt2XhdvgyRJ5Z95_Fl0VeWD3_wWl_1Varesn-YUGoacby_HjwJOhgw-1Z2BwTfco4v51Vcq3ixcTHLAfQGlS5LWjUaYIfqSGna6oQENvHAkgWEKmws2TKD6FRl21-gwc3JPyhFeawbM5kqlvrAfHn1Pogg2WUx8Tnuin1kZdGD46jxJaI3urahZplBkLOVDJgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a42198336a.mp4?token=ACDuFQC9hEPZPfvuO9H-TgCBbT9horTJgFBeEvohASoWvWvp2dXiOcJ4py-0yFu8nuqdYbBBX1fdxNcIXwfqAuZiSKxGW4tkh8l6pqEmGqCwKrfRs_qS6v8xK8Zdm5v5A-bZh20DcAPgQPUBO0rHlt2XhdvgyRJ5Z95_Fl0VeWD3_wWl_1Varesn-YUGoacby_HjwJOhgw-1Z2BwTfco4v51Vcq3ixcTHLAfQGlS5LWjUaYIfqSGna6oQENvHAkgWEKmws2TKD6FRl21-gwc3JPyhFeawbM5kqlvrAfHn1Pogg2WUx8Tnuin1kZdGD46jxJaI3urahZplBkLOVDJgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری ثبت نامی های خودروی لاماری با شرکت وارد کننده، که ادعا می‌کند به دلیل محاصره دریایی چیزی وارد نکرده.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/72584" target="_blank">📅 19:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72583">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5610e80a6.mp4?token=c0UZM5kWApg4bz3dCe-ndgi5GPnMGU49XZtjXmeBs9EpPAla7yp5GcaPC2cCXDwXvJEKtFY3a0E6MHsefdoISSQPd9-jX1XO61ZyBbjOA8v1buAB_n-iiZdjM4lLXgsTeriUr4dNT0fb_TG_mf_8JHOYq_3tXMQxVQUEZuUMSCeY6yInkl925oIDAUj0VGpepNrZc6byKHYNivHtJAkkliPRm1CVkqkxifaHbTFtEoFj3RM_BgdcXH3eQvGX3Sx7pkfk3qVCdPkBNMxMZA7Hw5tBYAq63c6WIAR-JL17PHCkXu3uAy9CDQkHzstI5ZtPrGPLyYSAjPY55JC--onKLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5610e80a6.mp4?token=c0UZM5kWApg4bz3dCe-ndgi5GPnMGU49XZtjXmeBs9EpPAla7yp5GcaPC2cCXDwXvJEKtFY3a0E6MHsefdoISSQPd9-jX1XO61ZyBbjOA8v1buAB_n-iiZdjM4lLXgsTeriUr4dNT0fb_TG_mf_8JHOYq_3tXMQxVQUEZuUMSCeY6yInkl925oIDAUj0VGpepNrZc6byKHYNivHtJAkkliPRm1CVkqkxifaHbTFtEoFj3RM_BgdcXH3eQvGX3Sx7pkfk3qVCdPkBNMxMZA7Hw5tBYAq63c6WIAR-JL17PHCkXu3uAy9CDQkHzstI5ZtPrGPLyYSAjPY55JC--onKLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهنشاه آریامهر:
«کلمه‌ی شاه در این‌کشور (ایران) معنای ویژه‌ای دارد و همه آن را می‌پذیرند. ممکن است اهالی روستایی دور‌افتاده در کشور درباره‌ی اتفاقات جهان چیزی ندانند، اما آنها معنی شاه را می‌دانند!»
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/72583" target="_blank">📅 19:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72582">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72582" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/72582" target="_blank">📅 18:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72581">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fm-7tZv02EfmO_BIRXnHsgscTlFxlubRv6d9EAUJROVwGV3XJF5FWMDZlLznRbpN88d1ivjGqGbnSQ63ur_703MSL3i9VMS8A0LUye6bTprV9TEayXToPi-qznNZ5oTE_rmykR0-vndea2DXFEf-bnb_x7Mv8mSHZt-5k4Ris9QowzO1CCDq7cRfoWIVipeBnMfMCorvsIi310qWNpp7Nn8aiLEz1T6_9JIaQWsEOqOBv6Pg7Vktlkl4NO6FqHFoPc9GnyAv6PSDeLndx470K4--Hyk1ykiDUhZqa8qKjpRkWZcB4cEF0WVcNpDxOMftYYyO6Zpf2XPTN9JFRMyR-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز پرتغال
🆚
دانمارک را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
پرتغال: ۳ برد، ۱ تساوی، ۱ شکست و ۵ گل زده
دانمارک: ۲ برد، ۲ تساوی، ۱ شکست و ۱۰ گل زده
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/72581" target="_blank">📅 18:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72580">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">#مهم
؛
یک
مقام آمریکایی:
ناو هواپیمابر «روزولت» و گروه ضربت همراه آن، سن‌دیگو را به مقصد خاورمیانه ترک کردند.
گروه عملیات آبی-خاکی «ماکین آیلند» نیز دوشنبه گذشته سن‌دیگو را به مقصد خاورمیانه ترک کرد.
حدود  ۲۲۰۰ تفنگدار دریایی در قالب این گروه آبی-خاکی به خاورمیانه اعزام می‌شوند.
تا پایان ماه نوامبر، سه ناو هواپیمابر و دو گروه عملیات آبی-خاکی در نزدیکی ایران مستقر خواهند شد.
با این تمرکز نیرو در خاورمیانه، فرماندهان گزینه‌های متعددی برای مواجهه با ایران در اختیار خواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/72580" target="_blank">📅 18:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72579">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MVM1MZqpvZyU9-wjOwfqMVoc-Cs9hKvVQHuQNsfvfwC4gXsMQGi-_umfQVEmyOwPIC_5Ydus8r1uu7jSQV9ALg0I3kVcKdO7xw6hXwV7pp2GxBVxQSE3Q8qdAoiSGaSriOEDrnMuCaNgFSimmNctWD7vGyY7lJEnWT-YJrlrU0S0vCBPllNLSzIweU52eMYULQqV-MZhvm0YqQUJ_obtQVSQsPuMUYuQInMBgIlG-BAHKthz01jL3RPn_oTsKibxUlo56xU7MxYXS6iYO4q5GI-tUzb4XZyaGCICP87guSS52_tBB6gUjynsVLHs3RqPkwWbeywwv60t5kp7883NrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیرمحمد، خواننده آهنگ سنی نردن گوردوم، از بدن فوق جذاب و عضلانیش رونمایی کرد
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/72579" target="_blank">📅 17:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72578">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f32d27e64.mp4?token=cVxq3X089acroYzxdr6yQJuqF0PcG_zR4G3WH_fQG_J6kxuLnh9I1Ck-rqtHl3s6vHGtFvwBlm6QJXBsi-auBr4pIUOU9eIDebP4-vKI6lVHtBkaosQ4Rv73lCSDhfy5p63TcUqIvEMfA6e0yphwWM9dHn9nNM5QtAbRWEqXfKcLrI_9eX42dFozumb88qXvFB38uATD-J2u0LcBQfdWISh678kHbRS1so4w4JVy44LcHweD7jHvwUtrx3mBdp4YDxnfrZvslWRmZ8HtPr61eUiItC-Gd7gHVr9KitRFximLG1P_U80nfWDdiuWC3uJr3bUqVQz9lAdsht1PSRHxxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f32d27e64.mp4?token=cVxq3X089acroYzxdr6yQJuqF0PcG_zR4G3WH_fQG_J6kxuLnh9I1Ck-rqtHl3s6vHGtFvwBlm6QJXBsi-auBr4pIUOU9eIDebP4-vKI6lVHtBkaosQ4Rv73lCSDhfy5p63TcUqIvEMfA6e0yphwWM9dHn9nNM5QtAbRWEqXfKcLrI_9eX42dFozumb88qXvFB38uATD-J2u0LcBQfdWISh678kHbRS1so4w4JVy44LcHweD7jHvwUtrx3mBdp4YDxnfrZvslWRmZ8HtPr61eUiItC-Gd7gHVr9KitRFximLG1P_U80nfWDdiuWC3uJr3bUqVQz9lAdsht1PSRHxxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جزئیات حملات آمریکا به ایران از 28 فوریه تا 8 سپتامبر ( ۹ اسفند تا ۱۷ شهریور ) :
@News_Hut
| thecuriospark</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/72578" target="_blank">📅 17:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72577">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a8db6d91d.mp4?token=v-wdZrwkvs8IuOORtl7PPwYOAhiLuBsAbjHb1Iw6v9fF6hPbA-Uyz1IuqSjMvUVSirAct_wdAo8A1wBKDDTSoRMlcRHPjNbBf8gd9rUhdW-qvDDNJxnOf7XjEy9h-Pap9Tak_jPVdebX46FlZmfyEHIT8HStDAFA6mIF-noSUoiATvauQd6CYmmVE6D-ViRcKOQASkLkHRsVSRpBEats7Bp8f9nPSkfgrMFuCnluvqw5rO1zaRuXi6-wBHMiHH3TNPWtblrK3a4Ws1fR2zMvD6ZLzoVCW8fOh_49zeVUGrVOW5RtkZUtXEfN3x6IueLMbINzwtdHxsWJbj8BUJ-NWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a8db6d91d.mp4?token=v-wdZrwkvs8IuOORtl7PPwYOAhiLuBsAbjHb1Iw6v9fF6hPbA-Uyz1IuqSjMvUVSirAct_wdAo8A1wBKDDTSoRMlcRHPjNbBf8gd9rUhdW-qvDDNJxnOf7XjEy9h-Pap9Tak_jPVdebX46FlZmfyEHIT8HStDAFA6mIF-noSUoiATvauQd6CYmmVE6D-ViRcKOQASkLkHRsVSRpBEats7Bp8f9nPSkfgrMFuCnluvqw5rO1zaRuXi6-wBHMiHH3TNPWtblrK3a4Ws1fR2zMvD6ZLzoVCW8fOh_49zeVUGrVOW5RtkZUtXEfN3x6IueLMbINzwtdHxsWJbj8BUJ-NWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو رقص این خانم ایرانی تو وان ترکیه وایرال شده و واکنش‌های مثبت و منفی زیادی رو در پی داشته:
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72577" target="_blank">📅 16:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72576">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a415ffdec.mp4?token=tn-aCw1HJ3D4qJEoA_Ul-Mgvn_Vf-HeOLXVS-JbYfS0R4-ANmx37eS94nb82duR7L5eHDh3bnIAha8Af3eVazy4Vt11-4vqsnKkfOZagfUc517TjnqHUz27PaiXbRHeIdy3KK18w58MPq-dXZzbURhrGYW4Fykj5BIYv0VFuE612Ozwxx64-4tB6zmeTp1vvCXA9YTyWEXhGWTQJY6A9BJr1jZJWi5_1R2dgPus7q-JhUczebyAaVoIr3WbGdc16dT2KHadiMLKlmr-slHxeYxTignXlWORVr87X2SCDre1BPH5PG-9WvErZB5I8ZezzqeKvkDQF0eRUDhjY4c73Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a415ffdec.mp4?token=tn-aCw1HJ3D4qJEoA_Ul-Mgvn_Vf-HeOLXVS-JbYfS0R4-ANmx37eS94nb82duR7L5eHDh3bnIAha8Af3eVazy4Vt11-4vqsnKkfOZagfUc517TjnqHUz27PaiXbRHeIdy3KK18w58MPq-dXZzbURhrGYW4Fykj5BIYv0VFuE612Ozwxx64-4tB6zmeTp1vvCXA9YTyWEXhGWTQJY6A9BJr1jZJWi5_1R2dgPus7q-JhUczebyAaVoIr3WbGdc16dT2KHadiMLKlmr-slHxeYxTignXlWORVr87X2SCDre1BPH5PG-9WvErZB5I8ZezzqeKvkDQF0eRUDhjY4c73Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حساب اسرائیل به فارسی در پلتفرم ایکس:
حالا که بحث هواپیما گرم است، یادی کنیم از هواپیمای کیش.ایر که 31 سال پیش در مسیر تهران به کیش با 174 سرنشین ربوده شد.
زمانی که سوخت هواپیما تمام شد و در شرف سقوط بود، اسرائیل تنها کشوری بود که به هواپیما اجازه فرود داد و جان صدها بی‌گناه را نجات داد.
جمهوری اسلامی هرگز نتوانست پیوند بین دو ملت ایران و اسرائیل را از بین ببرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72576" target="_blank">📅 15:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72575">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ اظهار داشت که ایران خواستار توافق است و درباره پیشنهاد آتش‌بس ایران که در آخر هفته رد شده بود، ترامپ گفت پیشنهاد ایران برای باز کردن تنگه هرمز کافی نبوده است.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/72575" target="_blank">📅 15:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72574">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سؤال: نتایج نظرسنجی‌های شما هرگز تا این حد پایین نبوده است.
ترامپ: این ارقام ساختگی هستند. من هر کسی را که امروز نامزد باشد، با اختلاف ۲۰ درصد شکست می‌دهم. نظرسنج‌ها فاسد هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/72574" target="_blank">📅 15:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72573">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سؤال: اگر «گادی آیزنکوت» در انتخابات اسرائیل پیروز شود، آیا آمریکا می‌تواند بهتر از زمانِ «نتانیاهو» با او همکاری کند؟
ترامپ: خب، نمی‌دانم. حرف بدی درباره‌اش نشنیده‌ام... فکر می‌کنید او پیشتاز است؟
سؤال: او نامزد اصلی اپوزیسیون است.
ترامپ: خب، خیلی‌ها بارها «بی‌بی» را تمام‌شده دانسته‌اند، درست همان‌طور که بارها مرا تمام‌شده می‌دانستند. من بی‌بی را دست‌کم نمی‌گیرم.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/72573" target="_blank">📅 15:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72572">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سؤال: گزارش‌های متعددی وجود دارد مبنی بر اینکه پیش از ۷ اکتبر، به نتانیاهو درباره احتمال وقوع حمله هشدار داده شده بود.
ترامپ: امروز برای اولین بار این موضوع را شنیدم.
سؤال: گزارش‌ها حاکی از آن است که مصر و امارات به او هشدار داده بودند.
ترامپ: فکر نمی‌کنم؛ به نظرم اگر او خبر داشت، حتماً اقدامی در این باره انجام می‌داد.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72572" target="_blank">📅 15:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72571">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ:
اگر من رئیس‌جمهور نبودم، عربستان سعودی الان وجود نداشت؛ اسرائیل هم همین‌طور. آن‌ها از روی کره زمین محو می‌شدند.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/72571" target="_blank">📅 15:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72570">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سوال: شما در ابتدا گفتید که جنگ با ایران حدود شش تا هشت هفته طول می‌کشد. اکنون وارد ماه هفتم شده‌ایم. می‌توانید توضیح دهید چرا این‌قدر طولانی شده است؟   ترامپ: فقط به این دلیل که می‌خواستم فراتر بروم. آن‌ها را از میان برداشتم. می‌توانستم همان‌جا متوقف شوم،…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72570" target="_blank">📅 15:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72569">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سوال: شما در ابتدا گفتید که جنگ با ایران حدود شش تا هشت هفته طول می‌کشد. اکنون وارد ماه هفتم شده‌ایم. می‌توانید توضیح دهید چرا این‌قدر طولانی شده است؟
ترامپ: فقط به این دلیل که می‌خواستم فراتر بروم. آن‌ها را از میان برداشتم. می‌توانستم همان‌جا متوقف شوم، اما می‌خواستم پیش‌تر بروم.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/72569" target="_blank">📅 15:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72568">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سؤال: هفته گذشته گفتید که ممکن است ایران را نابود کنید. این همان واژه‌ای بود که به کار بردید.  ترامپ: بله، این کار را می‌کردم. چنین چیزی ممکن است.  سؤال: چطور ممکن است «رئیس‌جمهورِ صلح» خواستار نابودی یک ملتِ کامل باشد؟  ترامپ: چون با نابودی ایران، صلح را…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72568" target="_blank">📅 15:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72567">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سؤال: در مورد ایران، آیا قصد دارید پس از انتخابات میان‌دوره‌ای، حملات هوایی را تشدید کنید؟ گزارش‌هایی در این باره وجود داشته است.
ترامپ: ممکن است. ما سلاح‌های زیادی در اختیار داریم.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72567" target="_blank">📅 15:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72566">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سؤال: هفته گذشته گفتید که ممکن است ایران را نابود کنید. این همان واژه‌ای بود که به کار بردید.
ترامپ: بله، این کار را می‌کردم. چنین چیزی ممکن است.
سؤال: چطور ممکن است «رئیس‌جمهورِ صلح» خواستار نابودی یک ملتِ کامل باشد؟
ترامپ: چون با نابودی ایران، صلح را در جهان برقرار می‌کنیم. به عقیده من، تا زمانی که ایران وجود دارد، هرگز نمی‌توان به صلح دست یافت.
@News_Hut
| time</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72566" target="_blank">📅 15:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72565">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نتانیاهو با مسافری که به توقف حمله به کابین خلبان فلای‌دوبی کمک کرده بود، ملاقات کرد و به او گفت: «بدون شما، می‌توانست یک یازده سپتامبر دیگر باشد.»
یانیو حیون، لوله‌کشی که هنوز پیراهن خونین به تن دارد، گفت که مهاجم را خفه کرده و کنترل‌ها را به عقب کشیده است.
او به نتانیاهو گفت که برنامه‌های تحقیقات سقوط هواپیما را از تلویزیون تماشا می‌کند و به این ترتیب می‌داند که چگونه باید کنترل‌ها را به عقب بکشد.
او هیچ سابقه هوانوردی یا نظامی ذکر شده در گزارش‌ها ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/72565" target="_blank">📅 15:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72564">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff0687bd0f.mp4?token=LTqLxdsTQL-sxK0xbwN7QVPR2jhRPL3keJrioXfA1LCn7MR6dlRuDhAKkC7rzqkLIPkCNqQnhQX4H4ZObr61WFkS1CijNUOZLZxDoW6OCnU3if-CDre6blpQVRCCKcBuWzpDZObwEq8dSU6Bxb8ridnlC8qlQL21oHw1gPvNH0YdJWc8G2Xw7OkWSBKyKdpu50PsIZya2c6S4IPkV7Gm7laH405qkpnnEE_BJ-b5p0MXGVobmFGwImfiaIlovvyPGfJdPVZ-6UyeMJ5EqvP9fAWIyJbDwXrShGysnNqTxQDdQ7Fg4JHKdbv27RyRSJhvHl0xywyhzW9PUrJNJZiFkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff0687bd0f.mp4?token=LTqLxdsTQL-sxK0xbwN7QVPR2jhRPL3keJrioXfA1LCn7MR6dlRuDhAKkC7rzqkLIPkCNqQnhQX4H4ZObr61WFkS1CijNUOZLZxDoW6OCnU3if-CDre6blpQVRCCKcBuWzpDZObwEq8dSU6Bxb8ridnlC8qlQL21oHw1gPvNH0YdJWc8G2Xw7OkWSBKyKdpu50PsIZya2c6S4IPkV7Gm7laH405qkpnnEE_BJ-b5p0MXGVobmFGwImfiaIlovvyPGfJdPVZ-6UyeMJ5EqvP9fAWIyJbDwXrShGysnNqTxQDdQ7Fg4JHKdbv27RyRSJhvHl0xywyhzW9PUrJNJZiFkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی آقامحمدی، عضو مجمع تشخیص مصلحت نظام جمهوری اسلامی:‌
گروه‌های مسلح آموزش‌دیده در امارات و اسرائیل وارد کشور شدن، مردم در محلات مراقب باشن.
جریاناتی در محلات استقرار پیدا کردن تا عملیات‌های ترور انجام بدن.
اومدن نتانیاهو به امارات رو جدی بگیریم. طرح نتانیاهو اینه که به‌جای اسرائیل از امارات بجنگه.
+البته این چیزا رو میگن تا تو اعتراضات احتمالی بخاطر تور و گرونی بهونه قتل‌عام دوباره مردم رو داشته باشن!
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/72564" target="_blank">📅 14:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72563">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnSTpFTZuDoyUi4FHemt0t7X39MLBpw56XyFMVbhapVHC88_-dRCOSaY82cuMvTomu2oqqafNv-ca4tsgXQ_cHjN4yTc9wLa1m-XLcYTbCdvL4CAVq7Z-kq0L3HZ061RxcB0-Uszs8QvYWAOTXLlVp5A--Y1Wbo00In4XpS9ivotv26v9qQ8bhOpro_HW805ih18mqbVdLoZlfecKDq9f3blyMMJbaiKzwgU0-6Skb7UVM6onsQLdO49a554hKl2_M92xPD5zy2kHHe3PWD65qRp_pe0c3-59gcPfX6IKFCo579L_0D0-E_1fQi85JpF1elUr8myWBPMiFF4S_gT0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ گزارش نیویورک‌پست درباره هشدار اسکات بسنت درباره اقتصاد ایران رو بازنشر کرد.
بسنت: ممکنه ظرف دو هفته «چیزی از اقتصاد ایران باقی نمونه».
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/72563" target="_blank">📅 13:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72561">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eEXnZLiEssnFw6-RYjyRxslp7rbD8IJ5AjDsPO11BwOHOi7eiuzNvWiemgTVHIPzzpYZ6gOiJtWbx8q0UElbIiRsAdbKasLgMAhQOKdTCbBtUHtq1nNM_EXkCcq7Hfz-b5BdPJ4WHedcHeVnlpQ72oWUad_pFVn1LYh8yf-SmGRn21YQjUMxrnBTkXtlf60MaJTBcnSHEMTRP23BWHixaLw1OrEOiD6f0viQXXNz1wVwZUXXNjqB6_jxqf1lX2zmckJuCAbBFN-yzTjDC7oGuHPfnOiyJiOXtcLs6_IXDXEgSLqPXwCgbL1Q1TMQVYXTXmFtt1Iaue9MsluuR86ZNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OKpnn0qjjq1SIQI0nW4VCdkzSIz5PVg8L4PqXTqdvhgpk4A-w68JzjoGj17SdvMMqpL9-4SxMxL9Rp8BvuNu5XvxoMxoeAwr3asTFb40Zv2nXq4mpy6VA2xdz7npfdd7bggIZ9JnVpaPzG2V1PHD15TlOUPrnN_WLWU8IlbcvSMMW2jPsK0mcpufBjYBliV4rDTfJhhc-T7fOvK90eknYJX8XyH00FYWBT8AZoiLxBLcUriFKBre77iEk_ECBLXxY7nRxa2vu630lnjoZNCJPn3ph1atASdtOo3ERRfwzcPMxBGoH9JEcw4ktStjm7Qtllr8k1A1S0OWFf1LpRyIHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بیژن مرتضوی که همین دو سه روز پیش گفته بود شایعات باور نکنید و نمیام ایران دیروز لایو گذاشته که اومده تهران
+پست چند ماه پیش بیژن!
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72561" target="_blank">📅 13:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72560">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/565ee82707.mp4?token=FpD-Z_8uyMKXs2QIN_R34FAyo42oEcR1hXrrOo-uqb1a9aWX-TAaNESBB7TMW5YGu1Cb1gTx893JL2rnmhYmFZTaJ4SkZZur5SaWdwzo4SfRqYB1ePpwVL128-NDfJq-SwuhGF8VpNq4wEFLu8xkU5StkDB1BRBTaEj3y5_Ch0CgpF4t5v_bONvP43Ec_fhOdhzOXazN9Y7BgvOENXBqbhlrJwOPnHmvNNFsN9UFZT8Bkuw54tp7qpck-xxDbcGlg0TIz4qmvBu9MrTSBCqzZ85S_FCd4CqE1_lC2MnhnpHCo4mvw2KnEgiVJfbRdq2SdlTJKyGNI8AAwDdNyyP6lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/565ee82707.mp4?token=FpD-Z_8uyMKXs2QIN_R34FAyo42oEcR1hXrrOo-uqb1a9aWX-TAaNESBB7TMW5YGu1Cb1gTx893JL2rnmhYmFZTaJ4SkZZur5SaWdwzo4SfRqYB1ePpwVL128-NDfJq-SwuhGF8VpNq4wEFLu8xkU5StkDB1BRBTaEj3y5_Ch0CgpF4t5v_bONvP43Ec_fhOdhzOXazN9Y7BgvOENXBqbhlrJwOPnHmvNNFsN9UFZT8Bkuw54tp7qpck-xxDbcGlg0TIz4qmvBu9MrTSBCqzZ85S_FCd4CqE1_lC2MnhnpHCo4mvw2KnEgiVJfbRdq2SdlTJKyGNI8AAwDdNyyP6lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد حافظ حکمی معاون وزیر ارتباطات و فناوری اطلاعات با اشاره به قابلیت‌های فعلی استارلینک و فعال شدن قریب‌الوقوع «Direct to Cell» تو سط ماهواره‌های استارلینک و امکان اتصال مستقیم تلفن‌های همراه به ماهواره گفت:
«اگر استارلینک فراگیر شود، وزارت ارتباطات و شورای عالی فضای مجازی را باید شهربازی کنیم!»
اگر قابلیت اتصال مستقیم گوشی‌های موبایل به ماهواره‌های استارلینک فعال شود، سازوکارهایی مانند رجیستری تلفن همراه عملاً کارایی خود را از دست می‌دهند و شناسایی گوشی و مالک آن غیر ممکن خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72560" target="_blank">📅 12:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72559">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72559" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72559" target="_blank">📅 12:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72558">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3yd9kbvV3alkDHAFw7xTErXxX-By1U9oSkAMrfMZ6grCAeAUdpuh4v3T5fzxi3S-xXfkdIvXJG1xQHGU9ujCPrr5I8cAw6z6kkj1jh6Q3QfnrZYlbPJsLAza5guwtsEtaLUPRThfiq5w6MAF6ouOp-b0I6_XFl2zMbWg_6YXefgTQ894gWSV2woaEYJY0xLHFPGQoB3ktm7SwSNd7qA833sS_r2cSy4cZmij-jlFiQQBETA2r8e8lMSMufw_niFtv-gBR1PLfTBLmGT24sMyg4iE0rbXrIz_6NUjSgHG0raivs8gARTjubdtnRxgQPuNKCyKBEC68hd5lH70ZE6QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
صربستان
🆚
آلمان
هلند
🆚
یونان
پرتغال
🆚
دانمارک
نروژ
🆚
ولز
بولیوی
🆚
آرژانتین
اکوادور
🆚
ژاپن
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72558" target="_blank">📅 12:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72557">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbA9B6zmL6-EY8UhLv5UCrLE9QKxLNrJvS4oX8fYUsHqXBl1VjG7Z9DcZVvMKnL1vGkw1kvBo8jZLmOkbG5-2ANbDOd0nZan7FcmAoc-vmzctJ9eYHgekV43CYeljaZPfgqSOzDJ0OA5gnyvlcJ9SNPAEYiax2pzC1gsVPI6Zq3bKounJRbovSgEwB6VJ3akbFQUZyqXTbrcw5zcEoPGnQgaShIT3MJ0mtN1Zw8BxHL-9ccMI5JnI1VIAUswnfOIGnafDtNlcBw0x_n269mWbAs9KpQ46DtQRN3nHf0W8nmmQKu5Kgedv6YgXc1IAbRMGPqmGadFnP2my4WxtHW1fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام اعلام کرد که نیروهای آمریکایی در چارچوب محاصره بنادر ایران، مسیر ۱۲۵ کشتی تجاری را تغییر داده‌اند. این رقم نسبت به گزارش روز جمعه، حاکی از تغییر مسیر ۳ کشتی دیگر است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72557" target="_blank">📅 12:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72556">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1be557ff64.mp4?token=XX49lb8ZKj7Yq2-NfLM3lU9-7anyKM4oincMlSgcRiYuVz3B3Kj8PsnmX2loLIfnaVe_fNhS3Y92mun_zx0qI3PO4qaQ9lXd8O5N0WdbR8nOcXig7hLQqYK4lzejm_UnfHc1xx6lfsP_woDK80jbn_Incvhb8XhVF-2zWFohOTNtzQakxDRGY3FNBn3wTqsID-xyiufWPI_BsaSpDlDXjP3cWY-62ICMCywKTgjlmO1HjlId0IE7R5TYweryaAeMPWCYokVmxfjoAYyS8SlwcDe6NJrhoIkLODxiziJtugZopTUmUfHEk4XKFILbcyhFbdk-TjcMifTlv0Hq58AteQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1be557ff64.mp4?token=XX49lb8ZKj7Yq2-NfLM3lU9-7anyKM4oincMlSgcRiYuVz3B3Kj8PsnmX2loLIfnaVe_fNhS3Y92mun_zx0qI3PO4qaQ9lXd8O5N0WdbR8nOcXig7hLQqYK4lzejm_UnfHc1xx6lfsP_woDK80jbn_Incvhb8XhVF-2zWFohOTNtzQakxDRGY3FNBn3wTqsID-xyiufWPI_BsaSpDlDXjP3cWY-62ICMCywKTgjlmO1HjlId0IE7R5TYweryaAeMPWCYokVmxfjoAYyS8SlwcDe6NJrhoIkLODxiziJtugZopTUmUfHEk4XKFILbcyhFbdk-TjcMifTlv0Hq58AteQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند نفر از هموطنان رفته بودن شمال که توی مسیر پلنگ مازندران رو هم دیدن:)
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72556" target="_blank">📅 11:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72555">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mv_ml6-c0wetIOW_iUszQPaVDFwWcYPPWjEctsA6gxJibi90mwVH5a0iMQH_HnUu3zfMEqubHUawy_KXHWgbUvJKcZJKGJKFeR5cPz721j-s_ODnmbvmBOSDR47FdIhXssxkPWsg96Oc1nb36_96woL1YWvhdDt6KEdZCE0gh0rXBkPIp5wevG-OzMXMRmRfS5Ysuj-pBBuElZ4I081wPV8HGaDGy0dMtrMlAICjl1JYi1G_WauL_nuvQ3jKOF6Ulohzg7kWbqp9nyci4lBHX5iy5V787RYQ6rVPVmhSPMc84Qx8PyoR5KtWO2TJ2wxVTsbUVifDS7SVp0dvbH3zOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛اکسیوس:مارکو روبیو وزیر امور خارجه بعد از اینکه مذاکرات میان آمریکا و ایران در روز دوشنبه به بن‌بست خورد،به هیئت نمایندگی ایران ازجمله عباس عراقچی دستور داد که فوراً امریکا رو ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72555" target="_blank">📅 11:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72554">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/74ab0dda5d.mp4?token=jVdGYLZbM5j-c678Ty5acfFtRxaXGgIoLKHLmBzNKivJAj47rpR7gQFLEjVEfY5Al341eFVHTRykmdhoixB2NB4ito8jM06VmAZnwplEHG1GPcmMMQoodiTHwdPF3KWVU0hXnEvGz5U7-_RhTHg8hrawPtl-TgmUG1-SLL8b_5YEy925v9BbG6a8pHtBgIwGB4WmD_D16iu5FwaK0l0lkAyEFgFFX2yDAHNvbpttU6g-Zbmn1OMAkxDjkNBA1039HZvsObV402-9jpATvHaP4d5UESkcXt86UxvgansurAliitVnF0DW5Jzy6ihWySwOEmkzyeQJrzero6nN806W1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/74ab0dda5d.mp4?token=jVdGYLZbM5j-c678Ty5acfFtRxaXGgIoLKHLmBzNKivJAj47rpR7gQFLEjVEfY5Al341eFVHTRykmdhoixB2NB4ito8jM06VmAZnwplEHG1GPcmMMQoodiTHwdPF3KWVU0hXnEvGz5U7-_RhTHg8hrawPtl-TgmUG1-SLL8b_5YEy925v9BbG6a8pHtBgIwGB4WmD_D16iu5FwaK0l0lkAyEFgFFX2yDAHNvbpttU6g-Zbmn1OMAkxDjkNBA1039HZvsObV402-9jpATvHaP4d5UESkcXt86UxvgansurAliitVnF0DW5Jzy6ihWySwOEmkzyeQJrzero6nN806W1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی یکی از وبینارهای مملکت بین یه دختر به اسم "پرنیان" که پزشکی قبول شده بود و "اشکان" که کنکور مردود شده بود، یه مسابقه برگزار شد.
نتیجه جوری شد که همه آخرش ایستاده اشکان رو تشویق کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72554" target="_blank">📅 11:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72552">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HUQIp3RSzu9KUEtG0z1ISXgopql6zC7XQNoC2apnAwqQNGLRFZcLT8DvNfwOlpa2NoU7l_eRyFdH8kO5oqG1sge8kxoOJfBjAC2bX02cKg8iYXbEPcZCaoFogeXD1GB7vkCXXnvOigr94Q6pG6Ze7VFZqol5Hya2KcBdxDvzMJl7FRJlJH3RZOOUBw2FBd29mxzQF84gFd3S_HLsy-liKXwNXutsqjglFi1X6LleAzrOEPiph7U73sj_3O7wwGpriH9OnB_T1MN0sq5_XFMz9hhZRCFR0_FVtHRBVtYEiEMCa99zsWRYieVmwHQJyqaVpCm41PEreGSUdlUgNMr5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V5941gjcczOnToAafS_nIx27wh99kYPpj_Mpk-rRiCifsUCMwRLqNCBmsqq5sM8GHgVGrqWQiVqQKOhbXTuue_VISWMTuRZ2LazuhAMtdOz-Hyq2mStnaXw7wfLFEGuAiW4XPmRoCW-M_nPyb4cLWB-VkMQLgL4fm148XbyYfMgSc2tUmcPLR9Ts_SqDm0pGlMt_hBDtleN8JIaVCzu2SBpGQ9kP_7sfnjR5_D431DJ9_-w5rPigFTg6zlW2h5XyuGXiZuguvm4xkRagCZJv1gJJc-LSbS5Ft32tj0oc-QHIxdjZX-9HetrTbQHVVvj6HD-c9_iEPGn15QaRGs4jMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی از حامیان حکومت: من 13 ساله که یه بیماری درمان نشدنی دارم، دکترا قطع امید کردن و گفتن و تا آخر عمر درگیرشی.
تا اینکه یه شب رهبر شهید اومد به خوابم، بهم گفت درسته من کشته شدم، ولی مملکت رو اداره میکنم.
یهو اسمم رو صدا زد، مصطفی! رفتم جلو و بهم انگشتر هدیه داد، صبح که از خواب پاشدم دیدم الله اکبر! هیچ اثری از اون بیماری نیست و کامل شفا گرفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72552" target="_blank">📅 10:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72551">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b14d6c45e3.mp4?token=KX_-eRI0b3S1fROlfwQIiITmePaeeB9U8Py54TSecV0RIOH091eOxMv2bpe2_U4jo7-_XbtLjWMOt0HUAE4qIXd7mBL4EIUJBaQB-n4_USvltaLU0UbiWMy0plokxyzO8oSM3P-9VsSXcIzKHu9etoAwa-RCqynIdeS-IOrWIrYmKXiNlcOno_8Xb5ZbJ9JIJF6qBwNRWYJF1zjw_55Tl3dJvSlX0rTZ1Wi9_8BFAke0CEWT6ySR9mCUUR13gMKw-dYfAfLZUn73LM1oBCeKTMduoShf7uhjon8u0N7kspTL1Hzoiho-LRybeJ6uHlkePZc3sn46qWU7KBCJM0YP6g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b14d6c45e3.mp4?token=KX_-eRI0b3S1fROlfwQIiITmePaeeB9U8Py54TSecV0RIOH091eOxMv2bpe2_U4jo7-_XbtLjWMOt0HUAE4qIXd7mBL4EIUJBaQB-n4_USvltaLU0UbiWMy0plokxyzO8oSM3P-9VsSXcIzKHu9etoAwa-RCqynIdeS-IOrWIrYmKXiNlcOno_8Xb5ZbJ9JIJF6qBwNRWYJF1zjw_55Tl3dJvSlX0rTZ1Wi9_8BFAke0CEWT6ySR9mCUUR13gMKw-dYfAfLZUn73LM1oBCeKTMduoShf7uhjon8u0N7kspTL1Hzoiho-LRybeJ6uHlkePZc3sn46qWU7KBCJM0YP6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از کلاسای دانشگاه مملکت، یدونه پسر، با ۵۰ تا دختر، همکلاسی شده!
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72551" target="_blank">📅 10:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72550">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/969c5e0df6.mp4?token=Wowrw5230BK2WcjCG2KQIBr8_flHymaYhfRj85vWTOMxG2wJggAf8m7IsYsGAbkVLP4U2h9CMWTQwrNhmj7esb8C3nLoIDPCQP4XhyKmYhhL7fxgiiddBKtzPkLSe7CbZCCoyoXiDjhomF6mQN5oqWliZcJD64baMt_wrkhEK_RxI85_fT9ypSDeLqVhURO87f71E8d7n42EiSyjpgOtMmBc8G7-CexRCKHN3g8U8epMwYlLcMZjD1F-mRaVhLRA0Vo5yn4nmbcqDJ8LN1eEDIsF3u4FTyEo6x12wPMNwBLCoJwpDhSKefZ0wRyV2jW0f-7FYD3mpPmdUk8hgZoK33errWtGKIMRNcBwmxU-o5oYjP8TAbRWAqi-mDvB_qaSuX0ydgGNIeIW02OH7qunWWOV_GXHw3w7gr8YxSthzxjmoCDHBrMr947ILot0JmxBPjGVmJ0DVOFzR83P3mpOM5rFFnGOgIqV1GG2iRAWZZxWDFuMhJ4EeO9Hqg0NdEUUWKtFtaP7MNAMZnzIw1xYFjCJD7g_spRN3FZukERa2vwl1ch35U3wfWyoy6y57PJZmM3JVwLjlB7KwS4UZ_R20XgRE7JAZ4xWzFWAjazZ64Swuf4Pv-83JZd8Rhq2kWgTtoM2wJ07x0uQAdOGBwLoDrJO22oLLxQ827y7WyASx8o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/969c5e0df6.mp4?token=Wowrw5230BK2WcjCG2KQIBr8_flHymaYhfRj85vWTOMxG2wJggAf8m7IsYsGAbkVLP4U2h9CMWTQwrNhmj7esb8C3nLoIDPCQP4XhyKmYhhL7fxgiiddBKtzPkLSe7CbZCCoyoXiDjhomF6mQN5oqWliZcJD64baMt_wrkhEK_RxI85_fT9ypSDeLqVhURO87f71E8d7n42EiSyjpgOtMmBc8G7-CexRCKHN3g8U8epMwYlLcMZjD1F-mRaVhLRA0Vo5yn4nmbcqDJ8LN1eEDIsF3u4FTyEo6x12wPMNwBLCoJwpDhSKefZ0wRyV2jW0f-7FYD3mpPmdUk8hgZoK33errWtGKIMRNcBwmxU-o5oYjP8TAbRWAqi-mDvB_qaSuX0ydgGNIeIW02OH7qunWWOV_GXHw3w7gr8YxSthzxjmoCDHBrMr947ILot0JmxBPjGVmJ0DVOFzR83P3mpOM5rFFnGOgIqV1GG2iRAWZZxWDFuMhJ4EeO9Hqg0NdEUUWKtFtaP7MNAMZnzIw1xYFjCJD7g_spRN3FZukERa2vwl1ch35U3wfWyoy6y57PJZmM3JVwLjlB7KwS4UZ_R20XgRE7JAZ4xWzFWAjazZ64Swuf4Pv-83JZd8Rhq2kWgTtoM2wJ07x0uQAdOGBwLoDrJO22oLLxQ827y7WyASx8o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از اولین موشک اتمی جمهوری اسلامی در  ایتا و روبیکا آزمایش شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72550" target="_blank">📅 09:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72546">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rMjffzKrxmjaiAApNcv7ciyPldrTAru8nt_C43ZWtigBkXSGsEN4ORxd5uJKfzTts0WBC9gDFhn1y8GID6e-ERU5lHkLbTEIY3mwPgFEG74sciNoOcu0eC7aQUVZ8Z8ShDCmrlc3C013ifKaWb9hrVFZD-zKHk5iqR1wZ0How551qij0UloYoMIAGVGeIr0cDpXVyyHDPU8K8ZTIUsdXju_zC6h8me44gW5Et7ig7T1dM1eZdAWzbYFDqxgAksX2YKTFvyD-73fRet-XCBcGgwObinkdig3u8Fl5abbEEDRfeB6cVRYI-nzOWBHiZcgif-J5fwTX1b43BI1aFVqljg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jvU5Sq58kRvA8qkP2D_RUE5v2hLLXz7tpCeAz4UHlAflYViJSSNZ4EMtKwzEhXIgatgr_06dh--qw1pPQhFhmdVy3lJc5tIvnkk1a5kGHWpAhoVm1dX6aDB2QttP74WxVXzd3PXaYmCyqSqwgwhshMVTncN7z42VfWeMmr2edzlap6Yugov4fRxw_CDR0b6kjLUtuffRp6ppqwazzQqAgwlA8dOF5mcQ8UZyrEqjC86LhJL5fNJt9DmMrn-zcYrN9p4_a87X-d6zU5UbrkdGz5I6pgPe-IQVqGISPOc49MP1vMW5R_Rdzr5L7RsTCrRuOvLkexMX1UUXEt4h9E9Q7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E5L9N5b0Lp1xdBiLX7d5sa89nmbPNYN8ujPjFK5deQ1bqc3ZoesI8-PNN_NGOypYSz7e3l0nl_JQEG0iLTrl63WUWuZjSF9zY-fFWXYPYPaRWrUlI40NJ3C3GYUCu2Rk_9-kPwPitZQYuA_HdbWqROJ5KMpk1VfoejOKYoc41D3Ql6Ayan2tA2VJgcVPGRcb0pLvgpq7qbedycZgWrucK2qzEY1Xq25KB5oaDNqOBn4mj-HK9ruOJwppJ-DpWQTinKbJ7t1CL7LsaA56UmH8IvH_8hmNO2KF1NaxoTb9I5O29iecBn_wxggKZYvxSF86lZ3m69ypGpcYwLAxuWmxbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb63ca7239.mp4?token=gaiFzJyG8XZWpy6mPbYKSUxixmpveJa89aLJxP1Aulvf3UkuiWsjzFPagrSmZbZXKqDcmDzBaT_o6xR1vuboFVMpAieBuJ64X1R8tsQykumWT3sz0f4OeW4LNJCU7SI9fDl438rnP9lcqRAqNI28sZgJd2fEjh31DzaRO1ZJeVjdI4G7bS1Zo28QMbgS7IqfpG03wOxCImHsrzp4q6NCoCECsutWh3qK35PmK_2BZa4irgRFcrKAMSx2x9xpl9NSOMr7612Xx-clUuNtvLD2T1TU8HCm951wzfVpLZzpDJ9AR0xBmhmDwPG82BTogD2eQLbOE8nIM0mPeO2aNSrD7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb63ca7239.mp4?token=gaiFzJyG8XZWpy6mPbYKSUxixmpveJa89aLJxP1Aulvf3UkuiWsjzFPagrSmZbZXKqDcmDzBaT_o6xR1vuboFVMpAieBuJ64X1R8tsQykumWT3sz0f4OeW4LNJCU7SI9fDl438rnP9lcqRAqNI28sZgJd2fEjh31DzaRO1ZJeVjdI4G7bS1Zo28QMbgS7IqfpG03wOxCImHsrzp4q6NCoCECsutWh3qK35PmK_2BZa4irgRFcrKAMSx2x9xpl9NSOMr7612Xx-clUuNtvLD2T1TU8HCm951wzfVpLZzpDJ9AR0xBmhmDwPG82BTogD2eQLbOE8nIM0mPeO2aNSrD7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دارن خودشون به جنایت جمهوری اسلامی اعتراف میکنن!
دو روز پیش توی بندر کنگان، مامورا می‌ریزن خونه یه نفر و جلو خواهرش به رگبار میبندنش!
انگار گزارش داده بودن اینا گازوئیل قاچاق میکنن و مأمورا ریختن در خونشون، تا پسره درو باز میکنه، به رگبار میبندنش.
پسره، باباش جانباز شیمیایی جنگ هشت ساله بوده و خونوادش ۲۰۰ شب و هر شب توی تجمعات شبانه شرکت میکردن!
حالا خواهرش پست گذاشته که مردم راست میگفتن، این حکومت قاتله، ما اشتباه کردیم، داداشم و رفیق بی گناهش رو به رگبار بستن.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72546" target="_blank">📅 09:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72545">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72545" target="_blank">📅 01:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72544">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/news_hut/72544" target="_blank">📅 01:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72543">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0sC2C4A4dzY0sMJ02j5Wu5lZjTinXRLHcT2wxb6b-LAvz_M2Btz94k0Ix4gSpCyq0gXaQ-kkJ3UfEobR4bfdW42BImpUsmUE4dfLUgtNlZwgYPnoRvm_GpOsWAgGxiOdMyeXqMUxDKlibJqGXhguRR3m_yuVeIATQ6kKTJUJ5r8HIHuB24EpOVOueB5OHFUSte983bv_WSwtL7KVtPnsWvQ2LOgNptMOhE_nXNXxS3zgxxrYxXYezOE4yOtK_r4NmoQH12ABWaQYJs0AYE69XvIcKBdAJ3oOxPxq43aEzl81ycuH7i4iZUkFjCWaF6VM5DedDqy70m0S-TdEXLvmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز پنج فروند سوخت‌رسان آمریکایی در نزدیکی تنگه هرمز؛
+دارن نفتکش رد میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72543" target="_blank">📅 01:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72542">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d22a56348.mp4?token=AtFdf9MO4vN6d8fKce0S1aJgh9iifwq7K3KHhzXTpQLkRunvPS06ZzS2diNIVT1z1nx6W2KWCcZjSPILz00Wut95ADGxmiBWD2s0VVocCD1zs1oTu4cDsuDV0gYTFyCqvaJrINPE0XI4ExQOb0YO-XQ3lYXg9vSS_rgPfbw0rabc0QG_dNqEVQUrB6CrQKyUabFEn4IeuvM4FK6POjF5f8i0j8tfqtKVVYziUqr7ijwmKPdaEJCRPWT1uRz_T4Igx5ZWfRegXipbz4iBK_xxfkvVqfshu8ymEX9vJD_4W3aAkc_Md828n04le0CUu2sK34h6HNIHtCksaDNJJ6OnIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d22a56348.mp4?token=AtFdf9MO4vN6d8fKce0S1aJgh9iifwq7K3KHhzXTpQLkRunvPS06ZzS2diNIVT1z1nx6W2KWCcZjSPILz00Wut95ADGxmiBWD2s0VVocCD1zs1oTu4cDsuDV0gYTFyCqvaJrINPE0XI4ExQOb0YO-XQ3lYXg9vSS_rgPfbw0rabc0QG_dNqEVQUrB6CrQKyUabFEn4IeuvM4FK6POjF5f8i0j8tfqtKVVYziUqr7ijwmKPdaEJCRPWT1uRz_T4Igx5ZWfRegXipbz4iBK_xxfkvVqfshu8ymEX9vJD_4W3aAkc_Md828n04le0CUu2sK34h6HNIHtCksaDNJJ6OnIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوال:
شما ایرانی‌ها را دیوانه توصیف می‌کنید. چطور می‌توان با آدم‌های دیوانه به توافق رسید؟
ترامپ:
شاید هم آن‌ها را منفجر کنید. ما باید در این باره تصمیم بگیریم. یا آن‌ها را منفجر می‌کنیم یا توافق می‌کنیم. زمانش دارد فرا می‌رسد. ماجرا خیلی زود به پایان خواهد رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72542" target="_blank">📅 00:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72541">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02359c50e8.mp4?token=Cim4uLw_X3aYOWgAH4Y1XSh95vuPQ6-MnEjxgANfKbGcuDS4yPnKor-GFGWzU69jPr2aYyjPyXjdEuD5VLHjZ7FhywBp5-ewwigafx572PlbIqFDamxalpt1wMd1Ys-DNnIFcZ9tbdp5xmknOM6r0Gq4Ait-UY93b0wZdeqCBI4iE6jgzCD5QR9fS1eexld0clkvRBhhq_YrqlYaSLvWZdogbFGaeE-BvkCYNmEAut82BIwk9AjmWsU41xAY0VCjoUBQl8EcBwYTN_T0quxJigkGCaguyxDcOCTudZRinxs5MOACId8rYiiforkWG6riwGD_pXi5LL5ITHfYGgRDyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02359c50e8.mp4?token=Cim4uLw_X3aYOWgAH4Y1XSh95vuPQ6-MnEjxgANfKbGcuDS4yPnKor-GFGWzU69jPr2aYyjPyXjdEuD5VLHjZ7FhywBp5-ewwigafx572PlbIqFDamxalpt1wMd1Ys-DNnIFcZ9tbdp5xmknOM6r0Gq4Ait-UY93b0wZdeqCBI4iE6jgzCD5QR9fS1eexld0clkvRBhhq_YrqlYaSLvWZdogbFGaeE-BvkCYNmEAut82BIwk9AjmWsU41xAY0VCjoUBQl8EcBwYTN_T0quxJigkGCaguyxDcOCTudZRinxs5MOACId8rYiiforkWG6riwGD_pXi5LL5ITHfYGgRDyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
رهبران ایران با تمام قوا برای به دست گرفتن کنترل می‌جنگند؛ اما کنترلِ چه چیزی؟
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72541" target="_blank">📅 00:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72540">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fe1c6438a6.mp4?token=N1T7eUUYJ883GVqa4PuD3SVpriC-gCeQbuzeLf3cgaKVg7C85DWb9eLZhJ7wdr4ACT9VAmZO0SkgmjHC03hzz0QzfBD77l2fRBg2BxOm8XGlwc7z-MXz8trEWZSz6i5oIm5q24Od1PXK1Ptlm9L7I3NMVaUV0zZ5HrBysGEVTdVDI_ZBlicgzgLa3G-pBb9q0yBw9Hm-vntLLozFge4RFmz9zTRiV5X7_VCpi_j20oF5YwkmNWn1M5fX4XnAc5ZPk01tpYPUxIXYXUu0LXTfkUImSPBMcQztNp11c9pEKhQEQC22Dkqm-dcU7SINUme2q4p0FpPrv5IKMr-vTL0n6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fe1c6438a6.mp4?token=N1T7eUUYJ883GVqa4PuD3SVpriC-gCeQbuzeLf3cgaKVg7C85DWb9eLZhJ7wdr4ACT9VAmZO0SkgmjHC03hzz0QzfBD77l2fRBg2BxOm8XGlwc7z-MXz8trEWZSz6i5oIm5q24Od1PXK1Ptlm9L7I3NMVaUV0zZ5HrBysGEVTdVDI_ZBlicgzgLa3G-pBb9q0yBw9Hm-vntLLozFge4RFmz9zTRiV5X7_VCpi_j20oF5YwkmNWn1M5fX4XnAc5ZPk01tpYPUxIXYXUu0LXTfkUImSPBMcQztNp11c9pEKhQEQC22Dkqm-dcU7SINUme2q4p0FpPrv5IKMr-vTL0n6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنجاقک‌ها زیباترین مدل رابطه جنسی رو دارن.
اونا بهم متصل میشن و شکل قلب تشکیل میدن و تو همین حالت پرواز میکنن و... تا کارشون تموم بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72540" target="_blank">📅 23:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72539">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a16c7cb51.mp4?token=U2GCgSFBae7iqf0vdF16aPIAu4FR7wCjm8oyseJFQx9ni6t_AAG7gUC8pHtxZD6o-ez3qRXgkjB5HEHLW3ju2FGtj4e9BcPPhJVO_EhriTzOU5cJLj3JIBaGIYZLbszC-duTUIwOX8JKXuLFeTc7PBPGIlxY9_dy9hITgyWdLxGaza1Bq35U7WBiqA_bDrym0EzO9Gsi5ZOFnt38XrebQzXOy2QqWUapEgQrgWz1rQKm6QRJUaocFn-vlmVFzNSpLDFxVNQqB23kssN45EhIMCRfRq_ojdA1C_0kiem7djd87kmXniuEjMhvIVF3fKTyhkKLSkMib7r0ia35vWRIuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a16c7cb51.mp4?token=U2GCgSFBae7iqf0vdF16aPIAu4FR7wCjm8oyseJFQx9ni6t_AAG7gUC8pHtxZD6o-ez3qRXgkjB5HEHLW3ju2FGtj4e9BcPPhJVO_EhriTzOU5cJLj3JIBaGIYZLbszC-duTUIwOX8JKXuLFeTc7PBPGIlxY9_dy9hITgyWdLxGaza1Bq35U7WBiqA_bDrym0EzO9Gsi5ZOFnt38XrebQzXOy2QqWUapEgQrgWz1rQKm6QRJUaocFn-vlmVFzNSpLDFxVNQqB23kssN45EhIMCRfRq_ojdA1C_0kiem7djd87kmXniuEjMhvIVF3fKTyhkKLSkMib7r0ia35vWRIuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای زیبای این پسر در مورد وضعیتی که برامون ساختن، ارزش اینو داره که ده بار گوش کنی و براش دست بزنی!
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72539" target="_blank">📅 23:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72538">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIC4HrZfxjJgPvuTZ8pRJ9UYeOsL2cq_gwqqDsbAmGqF8FixPz9sFvsFmTeGtjXjusQHwfl6DKYys1AvResuVrETQXmvgmDbzj7dz9-Ks9VGdDt6rZJ3jT7axfgo_0dxZqnNW92cL8oWuESI-8z3Znpm11UzgKIjlXYB23A10diHCus6FDNCK5a1UsfHATbVsX1xVVWnAqQfGVi_hpi1ydEpmwCmK5Rg6V2Az6TNNmV4qRyC2w5HQAPhbjG1PQB55gJIhudrkCD4yJRYVbalqRRiEqrMnaD-z-cT7N5Mx1p7wZQZLGgR13A3VWaYx42iQC1B6lps9QYNCRXlgquHgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت بوئینگ با پیشی گرفتن از نورثروپ گرومن، برنده رقابت نیروی دریایی ایالات متحده برای پروژه F/A-XX شد؛ قراردادی به ارزش بیش از ۲۰ میلیارد دلار که به توسعه جنگنده نسل‌بعدی نیروی دریایی برای عملیات از روی ناوهای هواپیمابر اختصاص دارد.
انتظار می‌رود این هواپیما در دهه ۲۰۳۰ وارد خدمت شود و جایگزین جنگنده‌های F/A-18E/F سوپر هورنت و EA-18G گرولر گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72538" target="_blank">📅 22:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72537">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره ایران:
ما تقریباً کنترل کامل تنگه هرمز را در اختیار داریم؛ البته باید بگویم کنترل کامل، اما هر از گاهی آن‌ها مین‌گذاری می‌کنند و اندکی در وضعیت اختلال ایجاد می‌کنند.
با این حال، ما عملاً کنترل کامل تنگه هرمز را در دست داریم.
در سه روز گذشته، حجم نفت عبوری از تنگه هرمز بیش از هر زمان دیگری در تاریخ این تنگه بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72537" target="_blank">📅 21:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72536">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ درباره عراق: داریم با کله از آنجا بیرون می‌آییم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72536" target="_blank">📅 21:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72535">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88278c6cad.mp4?token=brnUk7YL9oFnYSBpsUX-JQJ_3NSEnRDT_8FlSBqf4hXMIRhjgdd1kH6mXewzs_Wn-s1PGg4E6XEgL9Jx0ugoa_kmX9tT-97adLn40GV5ODyFplUqddszBUTpJpPWK-E97D9DpQu-EkbJk6CfXn-jSHnbd4iCRPQlvPbvaw5yxew9ko8ON1eT80KmrooiGrxGlSE5dlJ_9O3OiXlVUTQt8mllQ-tbFrLfI_XL-1dfLebVDQb6U0BF80jhJKw-fhAZEZfmohZgepRixIP6NPocmJeljoMlr_GN8TW09ugKA325NOtZK84QxjP4mcwTkGY8NrnhN8Gkr9fWlT-MGxpQGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88278c6cad.mp4?token=brnUk7YL9oFnYSBpsUX-JQJ_3NSEnRDT_8FlSBqf4hXMIRhjgdd1kH6mXewzs_Wn-s1PGg4E6XEgL9Jx0ugoa_kmX9tT-97adLn40GV5ODyFplUqddszBUTpJpPWK-E97D9DpQu-EkbJk6CfXn-jSHnbd4iCRPQlvPbvaw5yxew9ko8ON1eT80KmrooiGrxGlSE5dlJ_9O3OiXlVUTQt8mllQ-tbFrLfI_XL-1dfLebVDQb6U0BF80jhJKw-fhAZEZfmohZgepRixIP6NPocmJeljoMlr_GN8TW09ugKA325NOtZK84QxjP4mcwTkGY8NrnhN8Gkr9fWlT-MGxpQGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فووری
؛ترامپ درباره ایران:
خیلی زود شاهد وقوع اتفاقاتی خواهید بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72535" target="_blank">📅 21:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72534">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مَردی پنج ساله به بایدن فش می‌ده که چرا از افغانستان کشیده بیرون، الان خودش تمام نیروی نظامی آمریکا رو بعد ۲۳ سال از عراق خارج کرد
#hjAly</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72534" target="_blank">📅 21:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72533">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af74dbf4d.mp4?token=pkrqloHLrLNpnnT_XJ37RmbE8mg79o6tUX82DX5Su32YPygQAczQOUmnXX_-3Ej8E7JhFWC2my3mcEr4orHkvtfeawrML8JRr3Cl9E4iizjmAqUJRNd0Tyxg8XFU_rgpkRL7kTf0Sm7SYcS9xWmcpwg4XjENHCxSksuWpake9bQv0CgKvazV-i69XJKeOKTTcLBXqh2IsanPt9Hk6zDTHqttKx6ByKrEc-VcyzrzkF-9mOyL8NjDOWgv7KsnoWa6FF6A3I2nzIdX8PrHqNKRRIKH1P39Lq7QY30YiuUpn5TcABaZacfleiFHUxllNCyrx1R_0XkOYu0CoOByR68CsT8xiU7bQ4QZqXbDacSjvyzVHN5MPLk1B3PRlG2v3BTa1joabsEWlKtNHxeVme-DBE6bpwAcHU8dYhSbDjr3mpozOJrxvpOxGB89qjcrPNi7dbVUdVxLTK8OWt2jtx_EgJnn_9wYVE3UHihFuP1_Q7ppygjbdQUBi9aJpvjk9fq-b6K9O4WE9db_vw5FAm77H-jAQRb7U_IBIDbM6FhvMOLuqWP10gX3LhoY0ZEXmvIcGMcPt6kwrRD1j327eDkJCpXxhIVm4KbchRalvGfj1BPSVxUdOCeYQY7RFQx2iVUySivXgTj4HxbzEx7E1x2_L4wjp5pQRtmPqsyC4FLZVxI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af74dbf4d.mp4?token=pkrqloHLrLNpnnT_XJ37RmbE8mg79o6tUX82DX5Su32YPygQAczQOUmnXX_-3Ej8E7JhFWC2my3mcEr4orHkvtfeawrML8JRr3Cl9E4iizjmAqUJRNd0Tyxg8XFU_rgpkRL7kTf0Sm7SYcS9xWmcpwg4XjENHCxSksuWpake9bQv0CgKvazV-i69XJKeOKTTcLBXqh2IsanPt9Hk6zDTHqttKx6ByKrEc-VcyzrzkF-9mOyL8NjDOWgv7KsnoWa6FF6A3I2nzIdX8PrHqNKRRIKH1P39Lq7QY30YiuUpn5TcABaZacfleiFHUxllNCyrx1R_0XkOYu0CoOByR68CsT8xiU7bQ4QZqXbDacSjvyzVHN5MPLk1B3PRlG2v3BTa1joabsEWlKtNHxeVme-DBE6bpwAcHU8dYhSbDjr3mpozOJrxvpOxGB89qjcrPNi7dbVUdVxLTK8OWt2jtx_EgJnn_9wYVE3UHihFuP1_Q7ppygjbdQUBi9aJpvjk9fq-b6K9O4WE9db_vw5FAm77H-jAQRb7U_IBIDbM6FhvMOLuqWP10gX3LhoY0ZEXmvIcGMcPt6kwrRD1j327eDkJCpXxhIVm4KbchRalvGfj1BPSVxUdOCeYQY7RFQx2iVUySivXgTj4HxbzEx7E1x2_L4wjp5pQRtmPqsyC4FLZVxI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛
اندی برنهام نخست وزیر بریتانیا:
شواهد محکمی وجود دارد که نشان می‌دهد ایران در وقایع آخر هفته در پایگاه نیروی هوایی سلطنتی «فِیرفورد» (RAF Fairford) نقش داشته است.
در زمان مناسب توضیحات بیشتری ارائه خواهیم داد، اما می‌توانیم این باور خود را تأیید کنیم که ایران در این ماجرا نقش داشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/72533" target="_blank">📅 20:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72532">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">#فوری
؛کانال ۱۴:
بنیامین نتانیاهو نخست‌وزیر اسرائیل طی ساعات آینده با ترامپ تلفنی صحبت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72532" target="_blank">📅 20:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72531">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e30841564f.mp4?token=Is9bJKBzLC8-Zn2IgQ1vpwv99B8HWRd26-MCw77vDMwpLr-NO1ebZeGj7_blEr2f7Z3mAQHkxvda_WH_olJ1UwKu_m4KAqV8d8E1-QlcBDPKEL6dQl23qMp60-JXE5RMrEvGawHi0YuwtTVxWy_jiR38k8psWMWlCmVOVYaTspZcgsWUbnQcNC0rq5okES2kYtcuDaIIL4YvCLlMfWGoITF54VEEsCisWkQPDaZjle3zLg_FM5PBpa0uC0585QebwLd8SO_jVl5cc4KH5HeBJBFjQFoNIDhq8fKH3OC9rEaXu95Zf_u-wswr8yETCoJwykiQdwrDf5UT9MQwRePCnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e30841564f.mp4?token=Is9bJKBzLC8-Zn2IgQ1vpwv99B8HWRd26-MCw77vDMwpLr-NO1ebZeGj7_blEr2f7Z3mAQHkxvda_WH_olJ1UwKu_m4KAqV8d8E1-QlcBDPKEL6dQl23qMp60-JXE5RMrEvGawHi0YuwtTVxWy_jiR38k8psWMWlCmVOVYaTspZcgsWUbnQcNC0rq5okES2kYtcuDaIIL4YvCLlMfWGoITF54VEEsCisWkQPDaZjle3zLg_FM5PBpa0uC0585QebwLd8SO_jVl5cc4KH5HeBJBFjQFoNIDhq8fKH3OC9rEaXu95Zf_u-wswr8yETCoJwykiQdwrDf5UT9MQwRePCnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آشیانه‌های مرکز پشتیبانی لجستیکی شهید اثری‌نژاد نیروی دریایی سپاه پاسداران در شیراز، پس از عملیات خشم حماسی:
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72531" target="_blank">📅 19:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72529">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vWjojhjHSuw3D2GIbNmMGjAGsunT90NbzdpDE1a7EPirAvSrGIev9bwYJQ_vDFMY7gBwHjkL8dlRBe_51k_d00W9wT4l7i8lw_VpvZ4R9MpaqbFXwXUsSdM4KXLrv3sWJ90FDjBeemukEsvkzOsQZW9w9UKbmUi169btMtndfsktjUidi_o6447ZjYw89GxGeaBPPSQol4_vyr3mRYhaYVuea08J3AzpcEqjiP5F7di6zw2GfzWEJZ1W8-Vh2GoLTuKjFaDn9wCofVXQDL3b17hE7fUnP2NcThe0ecwe5j9zqMqpGaOxyDNvF6uumCEqsPYwcX-9_isfR2Df6PFs6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LAEPyOV-svJpLWDg05BPZ1nNrsXy1sUs5ru_y-0AIoyM5hU1bHrPVfCaB9BJOdh0X64w1DT1RKQZHhQ1qt6D8LQCTG9qMqMY5vghwfllPF-BKwlTGhJ4tBr3HTKJkvdpYYanKm71R8aXohnXh9LKKwxrNJbcQIg915m5BhC_JlRNm8F-iE5rRD8QiBiPRQK-PNJ0-sN3MNnnXiW-V4s668JxTayJlbIxvblW8qO1540UZo2ymra8TpbXAALSTOlnMDGNWwl4bRME3cBVs-IGPSAepaYhkz-PWrOy_CBOfPrNag-RO9lLCvqMn_Ggb8Sjg1FvTwMn5tf8v-XyYrItFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرتاب موشک از استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72529" target="_blank">📅 18:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72528">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نتانیاهو درباره حادثه پرواز دبی:
«یکی از خلبانان، خلبان دیگر را با چاقو مجروح کرد و ظاهراً تلاش داشت هواپیما را به همراه سرنشینانش سرنگون کند.
هواپیما وارد حالت چرخش شد و شروع به سقوط کرد. یک مسافر اسرائیلی و یکی از اعضای خدمه وارد کابین خلبان شدند و خلبان مهاجم را خنثی کردند.
یکی دیگر از اعضای خدمه پرواز نیز موفق شد هواپیما را به حالت پایدار بازگرداند و از وقوع یک فاجعه بزرگ جلوگیری شد.
خلبان مهاجم هم‌اکنون توسط مقامات سعودی مورد بازجویی قرار دارد.
به دستگاه‌های امنیتی دستور داده‌ام برای مقابله با تهدیدهای احتمالی دیگر آماده باشند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72528" target="_blank">📅 18:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72527">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72527" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72527" target="_blank">📅 18:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72526">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHm7XL9nnPsVmCWmmg-QsorQJx3Hz0uK5NiW9gXjIeS_1X2CnmSWX7qK0auv7EjIxotAmRluuGpGFsrIcdcyATmUIW0ffr9CZQg4oB8eNaB_lVzlmtYH_tOaonl2nVJYt7s4ZGZtCQpNUDGsqRJLXiOhaOgGL7kZws_DOZ0ncjKYNYyYvji_09bYYgDV4xGuw6NhvpHVCMTEIEL7A2dG-oA6RISLKJ9vCBQX3tbT-TpA5kUfygp7bflNCTgH8imr7Qyp48lDR98stwwVhVfZKG8Rd8cOXC7xgRxx9qknjr-ZicbBrpVko_YjPTvM_PvS4v4yW78GFADpioZVwQK_4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72526" target="_blank">📅 18:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72525">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fbae6ebe2.mp4?token=JrtI7HMq_zKmx_hvUetpkHLZc3mMAhUuESp-RaWJgw5P1-Kb2sLCemXLCwfW4bkmSbvLwWBUqV23muB8aD23APJrdP0SlttZqkTtRGZ0GzsV8DDEM_F-56HPTxV4xQUxIxE40ipFb9HZl4hRptB3kbexr2x4pVQFCznurx6q3-JKcl-0RIAulGaK5QYEeUL_HnQLW-UdvGAkqS3emBwWQDeDlqwPMO5lcuFhl00m54g9Q-yNE-neZlql0rmdDgoLhAdxfHxkf5XA6mOq4MSPZE-XE4vvCU-AYvTOuCnxx1DlfBLbN_mOgxkEzM4YETEPKvjTQS6ZmmL4vtfSee2wRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fbae6ebe2.mp4?token=JrtI7HMq_zKmx_hvUetpkHLZc3mMAhUuESp-RaWJgw5P1-Kb2sLCemXLCwfW4bkmSbvLwWBUqV23muB8aD23APJrdP0SlttZqkTtRGZ0GzsV8DDEM_F-56HPTxV4xQUxIxE40ipFb9HZl4hRptB3kbexr2x4pVQFCznurx6q3-JKcl-0RIAulGaK5QYEeUL_HnQLW-UdvGAkqS3emBwWQDeDlqwPMO5lcuFhl00m54g9Q-yNE-neZlql0rmdDgoLhAdxfHxkf5XA6mOq4MSPZE-XE4vvCU-AYvTOuCnxx1DlfBLbN_mOgxkEzM4YETEPKvjTQS6ZmmL4vtfSee2wRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏عاقبت لایی کشیدن در نهایت همینه؛
ممکنه چند بار تو رانندگی از روی دست فرمون خوبتون موانع رو رد کنین، ولی بالاخره یه روزی میرسه که ممکنه یه همچین صحنه‌ای برات رقم بخوره...
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72525" target="_blank">📅 18:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72524">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8caf88eae.mp4?token=H93vrjG7BryAzVNxuHxEMcyD5xt0eRXLIF3wbTKYvHULgfGN6gVYCoLT4fDgJHSmBNw2lOcPQOKd8mE2KJkOdPTJu84RHDLgsEEnb6b_W4AbnuadYPF4gx7xd09jglby5dkOPxa2sRVbSu0fEcs2RR53vK1vFuhQiR4i7WCwsp51cjEd4O9LDokOOaRHyrbUVJwKeKZ_yzofdg1oFi-KdoCfGgRNP5O3X9ayXF3BgDKUk5Ul9u95P7rNZme5sntMurwR06DYenwmQuUn82IB8HEd3jwDfMGLshlguGu4447MIpAy8HDsCgGOJAOjb96xg-fbJl4nTXKC36yh4huWNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8caf88eae.mp4?token=H93vrjG7BryAzVNxuHxEMcyD5xt0eRXLIF3wbTKYvHULgfGN6gVYCoLT4fDgJHSmBNw2lOcPQOKd8mE2KJkOdPTJu84RHDLgsEEnb6b_W4AbnuadYPF4gx7xd09jglby5dkOPxa2sRVbSu0fEcs2RR53vK1vFuhQiR4i7WCwsp51cjEd4O9LDokOOaRHyrbUVJwKeKZ_yzofdg1oFi-KdoCfGgRNP5O3X9ayXF3BgDKUk5Ul9u95P7rNZme5sntMurwR06DYenwmQuUn82IB8HEd3jwDfMGLshlguGu4447MIpAy8HDsCgGOJAOjb96xg-fbJl4nTXKC36yh4huWNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ بعد از دیدن این کلیپ تمام ناوگان های دریایی شو جمع کرد و دستور داد همه برگردن امریکا
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72524" target="_blank">📅 17:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72523">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f862c5d3f.mp4?token=sAjiR580KxdAByKp0IvRs42H5YfxjzyBaOa5EDwP0wctTcLMD52qFd1hzCZGWUlatHZ7cY7f8fmnkvSLXmVaZEGmHDjI7JWVLvsHtoMYvZ5d3UTCZ9vGfVq1Z5ybPy5Yzx2YCJt3bRjzZwK0_gqB7Wzj2V7JJeCjZloZ1pnEXLUp8Qt7Nw-Wye_qAVxH8sQtc1UxpM1HsAKjkKyNmLu2D1eqjKRz5JQy4Z2o-Rahhl5s7l7eIyF4H5m5oKVLtYaDycm3STa5tHDeeXs2pA8Up2T-MHQSHF3drOrrfeQ3RKfPtre-FFJ26QHdrNGfkzgRclqP4CjiVUgI2onqVBjPOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f862c5d3f.mp4?token=sAjiR580KxdAByKp0IvRs42H5YfxjzyBaOa5EDwP0wctTcLMD52qFd1hzCZGWUlatHZ7cY7f8fmnkvSLXmVaZEGmHDjI7JWVLvsHtoMYvZ5d3UTCZ9vGfVq1Z5ybPy5Yzx2YCJt3bRjzZwK0_gqB7Wzj2V7JJeCjZloZ1pnEXLUp8Qt7Nw-Wye_qAVxH8sQtc1UxpM1HsAKjkKyNmLu2D1eqjKRz5JQy4Z2o-Rahhl5s7l7eIyF4H5m5oKVLtYaDycm3STa5tHDeeXs2pA8Up2T-MHQSHF3drOrrfeQ3RKfPtre-FFJ26QHdrNGfkzgRclqP4CjiVUgI2onqVBjPOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسر بچه دهه نودی با اجرای رپ خیابونی، این شکلی کلی مخ زد و از دخترا شماره گرفت و بوسش کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72523" target="_blank">📅 16:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72519">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RC5RCuRmACdFS3vovdqgK5cDcpbaQZJhutSueCl7G6lcDJa0TkoMhgbzUc-0Xmp4NShfykFfGCr_nhRfbK1QrD6JXtdPbIHjIPhV6slYctlflQbPImVc7nIJ_2vuFX541a8uUsxSkiqJZL7SmxV5Urrd2bFkne78Jk5_gu0HPpZn3xJ3AJSfPZzojir9-ByNzppnLCm6TaL-nbepQtRq635BUVOcjmJk5D1tulk-Uy2QJitzSOx5NtCoDV2smftiGbtGZdghyEypiZY9pdILBI2v_5h6fpKifk9VemIeX3D3JhYc2b10z63v7pN5G3QLQMcqb8GN7qWfRwVo5joJVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/670f963d1a.mp4?token=mr4Qh36yEh4n0Yec6pjJF9ytjUbQ2gImFMVg7wO87zJaoyqYyMISsgVQzgV0X3RRqTwf2NOBNSX9NTayvb2giChveK589NFypgYC0QPjB61BE28tOLy5KkS6lfS7ylIwoSO9pZ3qBtKyj1_nGqK7s6oUuCvcNpXaYHfe3hO7UE-4QWnddR-dSH9wbBDn-ooxKG-m1W0BU_bebmesMVsPRVRXON3kEhdanhLB5x0KM56-LAuyPd3UEQ95_9rU6nU510vgyO1n0MbC18moYmx8P8E7QeQLTfPGVZTRrNfShNwUkiLAxJ0RHZXTtOPzsPcdYravXwImEvr-ruWbq6Hkvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/670f963d1a.mp4?token=mr4Qh36yEh4n0Yec6pjJF9ytjUbQ2gImFMVg7wO87zJaoyqYyMISsgVQzgV0X3RRqTwf2NOBNSX9NTayvb2giChveK589NFypgYC0QPjB61BE28tOLy5KkS6lfS7ylIwoSO9pZ3qBtKyj1_nGqK7s6oUuCvcNpXaYHfe3hO7UE-4QWnddR-dSH9wbBDn-ooxKG-m1W0BU_bebmesMVsPRVRXON3kEhdanhLB5x0KM56-LAuyPd3UEQ95_9rU6nU510vgyO1n0MbC18moYmx8P8E7QeQLTfPGVZTRrNfShNwUkiLAxJ0RHZXTtOPzsPcdYravXwImEvr-ruWbq6Hkvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک بمب‌افکن استراتژیک روسی از نوع Tu-95MS در جریان یک پرواز آموزشی در منطقه «آمور» سقوط کرد.
این هواپیما حامل چهار خدمه و سه سرنشین دیگر بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72519" target="_blank">📅 15:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72516">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ahyUB2OujvWs0UqgdgC69_4M6sU5I8lBvh56pMDYp7ClJe8YR_8Ub97aj3lHYQynODInXBasl-1YpwlyUtsqy_f-KirFHO_W05FigdngrLX8sp3WBD2paSYkU_Kfduqtm4sd7FJCUsK61UwWeNV_BkK6On7HJ7FcV5-49XeSflbdxBoLTtksB_lv3k27MwpWFTZcdIM9xHTCYqKHhkh2Pr4UHiGZTwBdGjYzJX5zUoCEwjhFNdsXaWtzRuDx1BIYKTbnAL3HgwCysfYcUOWvdOLL5YvDf9kXpxvrmR2eKK2skIrO5xj0dPhWt5mue4GEecpih3cZoC2UTaSZjz4LdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hUw4w_F7GxyO4a7yOi3nI3X80gTwM3aI7mRWTfq2Erh9hxsA7FDKoesZxnwpi5sgoCMY1CHrOqUcfKMWTycC6LlT9fYdRPrr8eJxRNoxK10dKP_QBrGLjS7dI-hxa1DPII-GMnEFzdwA1YERzEmrkHdQ4cu02wSnkQEKJP1u07T2fsiAGpI-pJfFd1ijpa3edECtcS4KrSC5VOTAEfxPpBXll45M50bRam3jy4VOzwlW0rEH9jhxzn_uoUjZya3RrQT4MDU1lwEY5LEXl4SEYfnK8cb93xuYiW_JS8YniS4FJD9uo2Vs8TWDZiKdKgJEehx2yI9rGs2bfo7bwSdIRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fykk0L1J7SGzMcUiMT8_qLNdRH9DnfhpYf-QYJ5GTRd4N-aOuw4-GSOddYlGZ2O3V2B7VR058c47DW2kYIsFQcPbmLcUKb675RWxLV3xg7AH_1dG9CbR_1qUI6W81FY8BrT-SHPVkH490dtBlCpYZVsXLKCeIuw1rfODll7ps8P8LyogPryZdmFXe3InhTH8zo-dv5RIKUewSsZCOiXgJxKzHuvJbzRFr7TIgULTlRInbTWXlOWoii8MnUJSQzbXNfMx9zgCy4ME0LEwmNhiim8CZvgxBqzAZ5dYo2ALu-bzvbU1jBn3cJGB_pSq6JeiQzTzHNRE2vgSigrs5mt10Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنا بر گزارش UKMTO، سپاه پاسداران امروز به ۳ نفت‌کش و کشتی حمل گاز در تنگه هرمز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72516" target="_blank">📅 15:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72515">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4993b45c70.mp4?token=PS40XMd7JOu4SYs_IO8d8PLq_gfHul6FCa8WEyrEsJ2f-q2ull68mSt7p-J2AgBSgD9arUH63qS5O6dm92THg-JJsLKK5ouePlKhiyrEus7zALcX3VzuBxEDjjc-kd4o86RU_HaOwXKyGVxpj5mJCQybRfQpl8p-O8ig8NaEe0c9LkJsA5mRf4Eu5TdX6qow9oaOu2kum_POAxtTf5LCgvUNjWSyk53PwLBWwMgp_cm2hf9ADg2cDIw5YY4ZKTNbiDPqtf5emVI2uJPi6l0IEpcUNrRascNE6UGH_Wy-KTPn_Khf-7MN8tgjA_q_gCLfAl7IUsf9uLNedSPgacSLKlgJELh9hKm7QLEFG8fH4ehUnRuAcaVS_rMuRPzWsg_bEyblcx-yhGLpoFx9ub-hAH6riovXxlNPli_B2tswbEghLh5HZj4yV1OsvtUuDGQ5VlGefiSlxyG7ZBIlXbhPZXsvNNZPJ_ME14ReWvH6M-tgf2d5NuwPfB13hvg4n1cKIMCYhvwkKQ7CSrp4E3aG2e5iZgrGG5l3UQH5XexToA6XBohRebLiS5JyGew2jOeJqzuW_9H8yoK48Ykr6qGK_AYYmzeKj25V4Ymw_ymqd2K18Ygd7BOxaJ45_YBe_rf3lm9kYx-Cqy9NzSgWKSB56nuyC1tKKOOSCDe1yUPo3F4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4993b45c70.mp4?token=PS40XMd7JOu4SYs_IO8d8PLq_gfHul6FCa8WEyrEsJ2f-q2ull68mSt7p-J2AgBSgD9arUH63qS5O6dm92THg-JJsLKK5ouePlKhiyrEus7zALcX3VzuBxEDjjc-kd4o86RU_HaOwXKyGVxpj5mJCQybRfQpl8p-O8ig8NaEe0c9LkJsA5mRf4Eu5TdX6qow9oaOu2kum_POAxtTf5LCgvUNjWSyk53PwLBWwMgp_cm2hf9ADg2cDIw5YY4ZKTNbiDPqtf5emVI2uJPi6l0IEpcUNrRascNE6UGH_Wy-KTPn_Khf-7MN8tgjA_q_gCLfAl7IUsf9uLNedSPgacSLKlgJELh9hKm7QLEFG8fH4ehUnRuAcaVS_rMuRPzWsg_bEyblcx-yhGLpoFx9ub-hAH6riovXxlNPli_B2tswbEghLh5HZj4yV1OsvtUuDGQ5VlGefiSlxyG7ZBIlXbhPZXsvNNZPJ_ME14ReWvH6M-tgf2d5NuwPfB13hvg4n1cKIMCYhvwkKQ7CSrp4E3aG2e5iZgrGG5l3UQH5XexToA6XBohRebLiS5JyGew2jOeJqzuW_9H8yoK48Ykr6qGK_AYYmzeKj25V4Ymw_ymqd2K18Ygd7BOxaJ45_YBe_rf3lm9kYx-Cqy9NzSgWKSB56nuyC1tKKOOSCDe1yUPo3F4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ای که هواپیمای فلای‌دبی دچار سقوط ناگهانی شد و به سرعت ارتفاعشو از دست داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72515" target="_blank">📅 15:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72514">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8d2f0129c5.mp4?token=ZlD-s53HjJW_-ej4Un4_NnFelDy3EXQItoWgLs6WB40UNgGElTF__OrXn_PEoMEQd2mrLkkB7IbbkuNSlKOK5uLNyCd_6IcOrAm1b1FlcgAs50ZUttIejcOpvPXJh5lrFHqSOhI1guJmbxAPDT6BE9vLllXuRGMmiePnRxAN560-ihaiBAXB90bYVu8R2kob6IAiQgiw6TAOROwS6kEp5Xwy_L49IyFsMTMUDSwPrBINPgxo5e1YWWSQGgtjFrQS0jNlV82-xlAuG3p4Fh8xv9EzYq9-wy58LcN9EDxUaF6vN-m-zHYRvIJq-J786sSEjUbqY5VCWkW5TeRYCmElYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8d2f0129c5.mp4?token=ZlD-s53HjJW_-ej4Un4_NnFelDy3EXQItoWgLs6WB40UNgGElTF__OrXn_PEoMEQd2mrLkkB7IbbkuNSlKOK5uLNyCd_6IcOrAm1b1FlcgAs50ZUttIejcOpvPXJh5lrFHqSOhI1guJmbxAPDT6BE9vLllXuRGMmiePnRxAN560-ihaiBAXB90bYVu8R2kob6IAiQgiw6TAOROwS6kEp5Xwy_L49IyFsMTMUDSwPrBINPgxo5e1YWWSQGgtjFrQS0jNlV82-xlAuG3p4Fh8xv9EzYq9-wy58LcN9EDxUaF6vN-m-zHYRvIJq-J786sSEjUbqY5VCWkW5TeRYCmElYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این موزیک به اسم «مفقود» در مورد مجتبی خامنه‌ای، فقط تو چند ساعت بازدیدش میلیونی شده
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72514" target="_blank">📅 14:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72513">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آی‌۲۴نیوز:ارزیابی‌های اولیه حاکی از آن است که خلبانِ عاملِ حمله با چاقو در پرواز FZ1073، تبعه عمان بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72513" target="_blank">📅 14:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72512">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mz5OA3NStczfsh0Nu0GX5lgQ6ZVoS6QAcmC2uFT7-8nPrtBgWVGY1u3vZf2LsZrTIero2dAlWdSnm19W1lxvoslQykXEUTzAHxJYmqz7-Fjjw5ZhsKbPpJP-zMSlZm7hmECp9izZ1YrEPj1vXmb8jpSw2Qua1VQqX3_vMeFLdKYD_3k_DnqeTACd7I8RHZvxuXqcMhVw6CvGoMZaeiA2yPWvXuaCFzN5z_RTwUvWJGeO5RxIEdGUC94B6gkuNLu7woDb1DRNqnjoy2zNjF527-vVy94uDjH3z1V8FiJX-lp-cyS-sP1cuYUb_hQp7TcWtcmwY4P0FKNiSXEyW4hM3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدیو اول تصاویری دلهره‌آور از داخل پرواز «فلای‌دبی» از دبی به تل‌آویو که ناگهان تا ارتفاع ۱۵ هزار پایی سقوط کرد، وحشت و هراس مسافران را نشان می‌دهد</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72512" target="_blank">📅 14:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72511">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af8284df28.mp4?token=RFM-fAsDac3w1ovkFEYdPgaTrZByuFKreAXfl2qm7KcEPBztKqVBY_liXVhbEC8lU3ir41VX5kvhY_GWGCbywUqqxWaCU0kmtRgQRx6zBziOlgS0oprKjlwsD7CUJOgaS4tw-o9RbuLL2fNaF2ogtDF2GU841OAmBEMFFxqMEwId-J-JwO3mI3ylQYY_bf7LLl3HnPMgsX5i4ME65juzpMvgjjAcGAPA2N9z6RFOOEtbuqadF3VdqbEIB6nsIaHQiz5aUKZiAe89fDOwtKAiRhOEC1mvjvGN1iHaP0vpaDwHlH8jgx_Cvsog71HxSzKgxFWazZckHkvawWAqtC-zDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af8284df28.mp4?token=RFM-fAsDac3w1ovkFEYdPgaTrZByuFKreAXfl2qm7KcEPBztKqVBY_liXVhbEC8lU3ir41VX5kvhY_GWGCbywUqqxWaCU0kmtRgQRx6zBziOlgS0oprKjlwsD7CUJOgaS4tw-o9RbuLL2fNaF2ogtDF2GU841OAmBEMFFxqMEwId-J-JwO3mI3ylQYY_bf7LLl3HnPMgsX5i4ME65juzpMvgjjAcGAPA2N9z6RFOOEtbuqadF3VdqbEIB6nsIaHQiz5aUKZiAe89fDOwtKAiRhOEC1mvjvGN1iHaP0vpaDwHlH8jgx_Cvsog71HxSzKgxFWazZckHkvawWAqtC-zDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارش‌های غیررسمی؛
علت حادثه پرواز «فلای‌دبی»، مشاجره‌ای میان خلبان و کمک‌خلبان بود که به درگیری فیزیکی و ضربات چاقو کشیده شد.
خلبان تبعه روسیه و کمک‌خلبان تبعه اوکراین بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72511" target="_blank">📅 13:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72509">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0f8e2c2fd.mp4?token=AkkAxbfQKlhZ1ds67N2XGm3nzEVUf7WAdfwdPH3TpGS6Zca8amSvMmCJUActHdagth9oG7KcIwdR0v99zdw-VFkNV1Pvat37U3tYm2M-GsmDMSCGE4l1b7ugic89NnOD-c8tOF-lb1YtUsQaX4faL2PbkBkG-fkQdAMoKmfliD714XzhhbuMpGGkhUp91V1WMXW9DAaQOcuePQMSNcom37eFmstkLY3NUcG0mUVFZF-sbmU2aMmpBmNhiW5ENMKfiMS-SDF_FSlkTACJHNz5UAPTEzApuEcki7vRIzyi4DBFmC17J_jvnXbdzdgBTbYZ22UPRr2O34HF2HyokbByWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0f8e2c2fd.mp4?token=AkkAxbfQKlhZ1ds67N2XGm3nzEVUf7WAdfwdPH3TpGS6Zca8amSvMmCJUActHdagth9oG7KcIwdR0v99zdw-VFkNV1Pvat37U3tYm2M-GsmDMSCGE4l1b7ugic89NnOD-c8tOF-lb1YtUsQaX4faL2PbkBkG-fkQdAMoKmfliD714XzhhbuMpGGkhUp91V1WMXW9DAaQOcuePQMSNcom37eFmstkLY3NUcG0mUVFZF-sbmU2aMmpBmNhiW5ENMKfiMS-SDF_FSlkTACJHNz5UAPTEzApuEcki7vRIzyi4DBFmC17J_jvnXbdzdgBTbYZ22UPRr2O34HF2HyokbByWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو اول تصاویری دلهره‌آور از داخل پرواز «فلای‌دبی» از دبی به تل‌آویو که ناگهان تا ارتفاع ۱۵ هزار پایی سقوط کرد، وحشت و هراس مسافران را نشان می‌دهد
ویدیو دوم مربوط به فرود اضطراری پرواز «فلای‌دبی» در تبوک، مسافران اسرائیلی را نشان می‌دهد که پس از فرود ایمن، سرود «اُد آوینو های» (به معنای «پدر ما همچنان زنده است»؛ سرودی یهودی درباره ایمان و بقا) را می‌خوانند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72509" target="_blank">📅 13:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72507">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CH8t_Yc6N79gWFI7F1uuRj-nePQlQvPkQ_4wIwKCBoj8wXkW-BTHKIiAl9IAItsalWjz4xVUa4suleuDP2IEdE-L_WToZXiz0Y02fFeQsgmqg4zB16Hmew94ruXqPxk2oT3s0enwibqQqDtg-_ziMayJOIXS9FW2NqUTetC4_VE8XyRghLNTtUyVmpaqF5wjiLtIiTZJzPUZTVXK_3VbehZOZrQwGT9ku3EJR-BYRGTBHTuSblcqe__zd8ZBvShs_UrKkV8BcCBKI25C8f7PGbMGG3UHeOhlgE2b925cg4tanjlj37N7coMP_I2g3yzzbBHVgiRdSXizQipSr-gyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fZwHehKNLt3s-Lld7lZwdcP_pjvxykjTZZcsK-0Uk6RBwCYZZQskC825LNR249BIU7e9t_KEwzxXq8MTpmIfYDg0vRfGWAy-vBzI-Q8fTvUi6NfKs0U9KXdf76krgZ_lOtkXWmT5sxV7HcS3GwiP-deYX_9Xwj8tQ1ZMo7Z2IoQjOzoLr6EVgQsRswNDDtVeV2vSFkt0vnd1fEhHhPK0RvCehikcBK2YqrGtdoEDQK65QXdAB9YYoB0efQq_f1bKr3EbpwY3MLjCFBAr55KpiGKE1cr2qLzcP-qgJu118SPIyJ6H6N8wGD65uJqFgBPdMoA7-ep9D8cBvCnKdW4U6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حادثه در پرواز فلای‌دبی؛ فرود اضطراری در عربستان
پرواز FZ1073 فلای‌دبی از دبی به مقصد تل‌آویو، امروز پس از وقوع حادثه‌ای در میانه پرواز، مسیر خود را تغییر داد و در فرودگاه تبوک عربستان سعودی به‌سلامت فرود آمد.
این هواپیما در جریان پرواز کدهای اضطراری ۷۷۰۰ و ۷۵۰۰ را ارسال کرد. کد ۷۵۰۰ نشان‌دهنده احتمال «مداخله غیرقانونی/هواپیما ربایی» است و باعث واکنش امنیتی شد.
بر اساس گزارش رویترز، یک مقام اسرائیلی گفت این هشدارها پس از درگیری فیزیکی میان دو خلبان ارسال شده است. با این حال، فلای‌دبی تاکنون تنها وقوع یک «حادثه» را تأیید کرده و جزئیات بیشتری درباره علت آن ارائه نکرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72507" target="_blank">📅 13:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72506">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4587e16a26.mp4?token=Dkbukbd6C2ndiH3z5TuzpJI-7oLas71eq6JPsozLfnUcmedNtoB89AGGZl7orU_UHcMqtCQ-0KeQwwQpRW1SidEAXqBLYvd33GnW2cc2oI5DJzd_umvHxznRJvU8iMi6sHAnFuq1imEWVFE77TO3dX07bY0_Fv6p0GLp18YCLrX35774EQEml1z6db1XlCxVpi8hizaZ8QQvNxx-Gx14njxnY_ZfVBBtvrRMySA8WUtFtWTRk5VzNWy3gxGgdG6cXlJwAJaQvwBkX6x5MzvzypaVJF8GNGjAtFmJGrInIZgAUOcaIyQ55-yd457zwpMdaVujqPHVHTy1G2K4TwvWfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4587e16a26.mp4?token=Dkbukbd6C2ndiH3z5TuzpJI-7oLas71eq6JPsozLfnUcmedNtoB89AGGZl7orU_UHcMqtCQ-0KeQwwQpRW1SidEAXqBLYvd33GnW2cc2oI5DJzd_umvHxznRJvU8iMi6sHAnFuq1imEWVFE77TO3dX07bY0_Fv6p0GLp18YCLrX35774EQEml1z6db1XlCxVpi8hizaZ8QQvNxx-Gx14njxnY_ZfVBBtvrRMySA8WUtFtWTRk5VzNWy3gxGgdG6cXlJwAJaQvwBkX6x5MzvzypaVJF8GNGjAtFmJGrInIZgAUOcaIyQ55-yd457zwpMdaVujqPHVHTy1G2K4TwvWfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر ۱۸ ساله به جای اینکه امسال اول مهر بره مدرسه و درس بخونه، با یه پسر پولدار ازدواج کرد و رفت خونه بخت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72506" target="_blank">📅 12:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72505">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M82s49wlF3w4e8VypasW-gSwM6YCPVHPfSqO7yaJZ7aZdEbrjZCFuYZxMT7MxMiF-SklsSLMIlmtZDlFiDD5_074GU1o2tdP-saRyZQQwyPtTuUMQzsVXiXk7MXjSef4pL1hxrsqDRbHuNz60GaCvrTwodm62mMcF7U6w8V3TTssMrKaEKevVXHP2pPWhzXxuZ0ONr-AgNfGjYyqgm5eVo1uDpEeLS1VuuVPOQ7QpDhuP9WlK9U3cH7D-0qgQYEBfqPA71Pd2Jzx2B9wCZb-4m6w0LCLToOOk1fx3jZNJ7AcGQCO9gu3Pi4jgpHuZJSN57iKj2RsDFJD5rBefwBL7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده و شرکای ائتلاف پس از ۱۲ سال، با خروج نیروها و تجهیزات از پایگاه هوایی اربیل، رسماً به «عملیات عزم راسخ» (Operation Inherent Resolve) در عراق پایان دادند.
پنتاگون اعلام کرد که از این پس نیروهای عراقی مسئولیت اصلی تأمین امنیت و سرکوب بقایای داعش را بر عهده خواهند داشت، در حالی که ایالات متحده به ارائه آموزش‌های هدفمند و پشتیبانی اطلاعاتی ادامه می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72505" target="_blank">📅 11:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72504">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLKTbgrT8aMYIve4jjxXXLOrdYk5mwDE-usRh0vDdYeKpjUNYS2cETA9G3MOI4aazd6QPqZ4TdSgilX3swcL6tXjd8sMrUvtWdbHMYr2oCPKMWg-Dr9jgUr6ijRDLlTwfocrnlYq6hHTpxd1qZwT17_fM--gO9TZ-RJjcMx4dmmUSE76aecQJEebMB-47_2mAVYPuGZePY8yFKuaTvToWSfVogZdiAYTBMoOpJQGK1t8J0Dy7qKe7WAgadqIFDhv83c9lJMtCNgygwfgS7grryYS0CvUHHWDa_dy7Tz_5U9n73YusGFarjHsjjgUN7MqjGFkIT923NB2bODzT62teQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش سی‌ان‌ان، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اطلاعات اطلاعاتی جدیدی را به شیخ محمد بن زاید، رئیس امارات متحده عربی، ارائه کرد که نشان می‌دهد ایران در برنامه هسته‌ای خود پیشرفت‌های تازه‌ای داشته است.
این اطلاعات شامل جزئیاتی درباره ساخت‌وسازهای جدید در تأسیسات «کوه پیک‌اکس» (Pickaxe Mountain) بود.
یک مقام ارشد امنیتی سعودی نیز در این نشستِ گسترده حضور داشت. گفتگوها همچنین تحولات منطقه‌ای مرتبط با حوثی‌های یمن، باب‌المندب و تنگه هرمز را در بر می‌گرفت.
نتانیاهو همچنین به حاضران گفت که ارزیابی اسرائیل حاکی از احتمال انجام یک حمله منطقه‌ای از سوی ایران در هفته‌های پیش‌رو است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72504" target="_blank">📅 11:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72503">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72503" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72503" target="_blank">📅 11:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72502">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dF6-HiV6BMPfBA9cJjdaHEnHJlgCL2Otk4MN7fCE3HGN6mVolKalNM7eS8qesxPSHWjYcWS9D6KY7gEpiJ2YvhE4UUc77Me9jDwpGywywXi0-6885lGeDEOu0EyZeBGbuzfGa8NM_Ims_chFLC0TZ8psIisk0TeUEjoKx-a2tYb72BGpRGKagWW395AUGgU-IhGMUHP-_0_ia6PqjJQJK-vjmtDiqGjpKJeS30cq1TYBuGP2FlCz0bNd55XfxeUJMZVO2GdAZDV8wJnMgaLLj5PNWk7CHJMkkx_IPkgUZDT7sxYoqZW1EnkOtK4SuAFZsCornz6HC2y3p1zIiGXGsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط ۴ روز تا انفجار در قفس
🦖
​ناتالیا سیلویا در مقابل وانگ کونگ
جنگ سرعت و تکنیک؛ چه کسی قهرمان جدید
UFC
می‌شود؟
🦖
​شانس‌ات را در
TrexBet
امتحان کن و روی قهرمانت شرط ببند!
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72502" target="_blank">📅 11:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72501">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58cfa5fb8d.mp4?token=I2wFYU1jCAnbrZkBM2v7wWPMyNVRzi-xiUOeeePyfMPG2D7zoyRb827iih4OcFeFbmkKT5YbX19c7aTzv-3XRFgJF4aeFlnj7ZMNG49Yc67rbzUa8PEhATfhzxegC_EG5mhcxNj6UWzw31mR7g3jWbwjo_3eTLHrL5HqUuckW3aJkydASrKMTWAklkQ1cSLyXZyb7AzppICjekadnY-0WHW5XpiilXzkbJ5xFgB8PlK6WiTPhb6jMGyxM-3Wqj2Q8lICp8z7-17CV57Px_AGe8fK2qsbMdRM7CXOYXp95iJDaaVFpf1b56hDQthjhMU56PEO-jRU-K8txlQNZOdz_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58cfa5fb8d.mp4?token=I2wFYU1jCAnbrZkBM2v7wWPMyNVRzi-xiUOeeePyfMPG2D7zoyRb827iih4OcFeFbmkKT5YbX19c7aTzv-3XRFgJF4aeFlnj7ZMNG49Yc67rbzUa8PEhATfhzxegC_EG5mhcxNj6UWzw31mR7g3jWbwjo_3eTLHrL5HqUuckW3aJkydASrKMTWAklkQ1cSLyXZyb7AzppICjekadnY-0WHW5XpiilXzkbJ5xFgB8PlK6WiTPhb6jMGyxM-3Wqj2Q8lICp8z7-17CV57Px_AGe8fK2qsbMdRM7CXOYXp95iJDaaVFpf1b56hDQthjhMU56PEO-jRU-K8txlQNZOdz_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هادی چوپان:محبوبیتی بین مردم ندارم و هرشب کابوس میبینم.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72501" target="_blank">📅 10:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72500">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2b6a15d8.mp4?token=ny_08lQnb7oJ1tNoAv_qZ9ueYYywK5dg3sY_AEGHk1Wqzm9mmQ_fJboKsX6h6VvgWO77rMg15ovBd60-fzUMGz1UH6pTaRyo0y2jT8k4vo38DcIiM4hxK1ESVA4aTn58wh4G78BBklsQX1HY_Luo0WZ0YWat8lm5bIXceX4r20g0vo9E6Fn8preV4EOAM-dKpxhAQpWb1Ueb9Svnp2CeY0Rq2pRBBSgTib3v_QXCxK3HDmpXEYX4GqDvlLqYVCWloQA-FBngdJNCvQgXM17CUlYMf0MrP0PVjLlYE6ZzCJ6UBzH7uqQJV_I675xWOCXocQcw_mhask8an7TuMZRTww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2b6a15d8.mp4?token=ny_08lQnb7oJ1tNoAv_qZ9ueYYywK5dg3sY_AEGHk1Wqzm9mmQ_fJboKsX6h6VvgWO77rMg15ovBd60-fzUMGz1UH6pTaRyo0y2jT8k4vo38DcIiM4hxK1ESVA4aTn58wh4G78BBklsQX1HY_Luo0WZ0YWat8lm5bIXceX4r20g0vo9E6Fn8preV4EOAM-dKpxhAQpWb1Ueb9Svnp2CeY0Rq2pRBBSgTib3v_QXCxK3HDmpXEYX4GqDvlLqYVCWloQA-FBngdJNCvQgXM17CUlYMf0MrP0PVjLlYE6ZzCJ6UBzH7uqQJV_I675xWOCXocQcw_mhask8an7TuMZRTww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی یکی از مراسم‌های عروسی در ایران، عروس یه دفعه تفنگ رو برداشت و این شکلی پشت هم شلیک می‌کرد!
از نگاه‌های داماد معلومه ریده به خودش ولی کمکی از دست کسی برنمیاد
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72500" target="_blank">📅 10:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72499">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cc8901fca1.mp4?token=h3WMoUNpt8nDFO0ZiOWKabSEINRNlvApUiK1333wraCu8C3yI-LqToG_YA8GJtUQGRkdnzpirf_Aucg-JS3omHt_LsmeGwttjArHBk2AFsb-e737Rhxh07hlk-a8Jovyq0T_W6pqRVf1URLkvOCShNPVrJ5DBS7JoChgo0yrTIY84xAN6vtJykN5emtwJK-1yitSbiV94Db76C1VJ-GvaMfRbhlloT_5ggBpyyV1KucAVUZNeGwRZbOGELz0UvjvhPUP29QruBJu_PT_EJ7fA6zxrLxciCgUNWK15eliNqGw3YkVgWIvQ6jT-qcINay7Pstu9nPNzaBq1YPi2QOnKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cc8901fca1.mp4?token=h3WMoUNpt8nDFO0ZiOWKabSEINRNlvApUiK1333wraCu8C3yI-LqToG_YA8GJtUQGRkdnzpirf_Aucg-JS3omHt_LsmeGwttjArHBk2AFsb-e737Rhxh07hlk-a8Jovyq0T_W6pqRVf1URLkvOCShNPVrJ5DBS7JoChgo0yrTIY84xAN6vtJykN5emtwJK-1yitSbiV94Db76C1VJ-GvaMfRbhlloT_5ggBpyyV1KucAVUZNeGwRZbOGELz0UvjvhPUP29QruBJu_PT_EJ7fA6zxrLxciCgUNWK15eliNqGw3YkVgWIvQ6jT-qcINay7Pstu9nPNzaBq1YPi2QOnKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این فیلمی از رینگ کشتی کج نیست! یه دعوای سنگین تو فوتبال پایه مملکته بخاطر یه تکل ساده‌اس!
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72499" target="_blank">📅 09:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72498">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324e32bd1.mp4?token=HA2GSF1X_LUVXP_XS4-38oKUcxot6suUVhqvY8UmUBFpe-7shKwfKptyBBX0V1dT1KoB-fbEGVrhC2WC2f1wKpHcwQ4nuaobM-UF9Z-EJcmtsHhg1-9oKXPA3wInqpFF2tmtqokpwjgT36hmS72C2-mrDz8SrNMSOFYuA0cOhRakO_hb_D7f4pItSc7v9L4ait3mobko3_QPmF5TGQ-E90LO4LpER0n8W4gTRtb-MPnZ3Ecg6mx665GW3_HTydYMz5hpqGusH29WT4VTCSvtDqhn54ku0O_rJ-aOAGAmAp53NwRV3dsx2rfIxpJLpBFLXlavcHeb68ZYSroQPGDD2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324e32bd1.mp4?token=HA2GSF1X_LUVXP_XS4-38oKUcxot6suUVhqvY8UmUBFpe-7shKwfKptyBBX0V1dT1KoB-fbEGVrhC2WC2f1wKpHcwQ4nuaobM-UF9Z-EJcmtsHhg1-9oKXPA3wInqpFF2tmtqokpwjgT36hmS72C2-mrDz8SrNMSOFYuA0cOhRakO_hb_D7f4pItSc7v9L4ait3mobko3_QPmF5TGQ-E90LO4LpER0n8W4gTRtb-MPnZ3Ecg6mx665GW3_HTydYMz5hpqGusH29WT4VTCSvtDqhn54ku0O_rJ-aOAGAmAp53NwRV3dsx2rfIxpJLpBFLXlavcHeb68ZYSroQPGDD2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره روحانی از ملاقات رئیس‌جمهور سوئیس با علی خامنه‌ای:
رئیس‌جمهور سوئیس به آقا گفت ما ۱۵۰ سال قبل کشور فقیری بودیم، اما دو تصمیم گرفتیم؛ دانشگاه‌های خوب ایجاد کنیم و با کشورهای دنیا روابط خوبی داشته باشیم. سوئیسی که امروز می‌بینید حاصل آن دو تصمیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72498" target="_blank">📅 09:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72497">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rep1za4VNK0dgmpBNPl_eHxS-bSfEy9PMP7_nIot3rX7qK9Yy69BoZpJ9G_-Gvyg28Sl7ejUEgU_LTw0Y1b2k0916it5X6vMrXimA7NOXjiI1_925FsYr-ZmqDRhnhRT2JPOsbB9sbZc0DgC3qy0WQOOE-NhGmv1dfiy83h-zd0zYbdfsoFeR81_X-XAIxtDwIYCC5M2Uh_xpqqzg711Jc-ncED5QMkG3ugYVq_P4-lHUCGnxWBdHa_YTrXcGbCcCOZVZnf5cPLjyhY7RtCes-1sLLqzJWjSC6Wib6hNtWsjMzvsxvThgI_B5eLTNRbxBn5MzhDWxAAWI5YrAJ0PLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووری
؛مذاکرات به بن‌بست رسیده،ایران میگه اگه آمریکا به تفاهم‌نامه اسلام‌آباد برگرده حاضره امتیاز هسته‌ای بده و آمریکا هم میگه حالا که دست بالا رو دارم پس کیر تو تفاهم‌نامه اسلام‌آباد و کوتاه نمیام.احتمال شروع درگیری‌ها بالاست.
اکسیوس؛
تلاش‌های قطر برای میانجی‌گری جهت دستیابی به توافقی جدید میان آمریکا و ایران پیشرفت اندکی داشته است؛ چرا که مذاکرات بر سر دو موضوع — یعنی درخواست ایران برای رفع محاصره دریایی توسط آمریکا و مطالبه واشنگتن برای دریافت امتیازات هسته‌ای — دچار بن‌بست شده است.
ایران تأکید دارد که تنها پس از بازگشت آمریکا به تفاهم‌نامه ماه ژوئن، حاضر به بررسی اعطای امتیازات هسته‌ای خواهد بود؛ در حالی که واشنگتن دلیلی برای کوتاه آمدن و مصالحه نمی‌بیند.
قطر، پاکستان و مصر همچنان دارن خایه‌مالی میکنن و تلاش میکنن که توافقی صورت بگیره.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/72497" target="_blank">📅 06:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72496">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/72496" target="_blank">📅 00:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72495">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72495" target="_blank">📅 00:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72494">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56db93255e.mp4?token=QT7PZJD1Z_CvI_tcMDY56sEMEoI9u95zrFMWJ2s1crUMwcig2WWc1DL2e-TzIAxpRZwseFWjdrtkjZvHQbCZlEf86_11JQHm7Vh7vsOT0Ax5LEjmKKQ4qEjqKMxHhUYxBMFV6d4Mmm9cxbs8lXcqK-pWWTLKVCDhDc960qgS_d7Zy8U1NK4vqFdi-3l9BpU7iZL2FEtBfVFu7WuSpj8qbh2GWH6e9cURAH_2Bhl3U3eYc6OkXdL8FXFsFrUOsYf1V31VzXTC9FChjmIm4ZtbAX6xO7pCFW1IWcs71WuhLBzNEYUj2ykA8Y6I3yLdBpJf50F2VXei0ril76mU2qNOlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56db93255e.mp4?token=QT7PZJD1Z_CvI_tcMDY56sEMEoI9u95zrFMWJ2s1crUMwcig2WWc1DL2e-TzIAxpRZwseFWjdrtkjZvHQbCZlEf86_11JQHm7Vh7vsOT0Ax5LEjmKKQ4qEjqKMxHhUYxBMFV6d4Mmm9cxbs8lXcqK-pWWTLKVCDhDc960qgS_d7Zy8U1NK4vqFdi-3l9BpU7iZL2FEtBfVFu7WuSpj8qbh2GWH6e9cURAH_2Bhl3U3eYc6OkXdL8FXFsFrUOsYf1V31VzXTC9FChjmIm4ZtbAX6xO7pCFW1IWcs71WuhLBzNEYUj2ykA8Y6I3yLdBpJf50F2VXei0ril76mU2qNOlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو نپال بر اثر رانش زمین، این کوه با این عظمت به طرز ترسناکی مثل آب، نصفش تو رودخونه سقوط کرد :
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/72494" target="_blank">📅 23:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72493">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299316a1b0.mp4?token=B8J3kU751JDePRvBlczy_qRYxP4G4KWUuv-b-QhXFu2AW-brneiWOLtJaATa2M203Md6LeUOBLx5Dpc4-_XlZlzRLC9a9B0i4tI1orC2Zz1MHMg9IKNB-VPpauUwpxcTVKEGBM1qPpjC25pEDMBIgk8aeBOW-LsU2M3ebG1K_2YGuV_dSzrxWafD7iGvH1aMhOb9qwiGxBt4ZGxubU3X4Tud49QB5Xt34K-3RU-yvGi_ltrHdCdgBiBm5bJHwOT0Ajj1Jckvu3n3K4ZfKyOnVxIAIpNvDmdoKpSBLkprtUAjMtjmgAPzOWed1fZ51k5JIpHzS9PV83emc59L2wQhDRUTjiWp3rK5ldUKBaf8efqBoOVDytT2gs-3BmoDGxsQqPluH1AHPAUm4oLfL7mEcwjM3f81_re2yR4FbcX24n3wBuhJELD5JhTg3U8c5qTTVb-CCtV8XfYmQESNDbQQ5Q98mm1shXJXnEL9QyVCmHgUW2Atxq9rRK3vZvYBnmsloar1L3D_kUBFCKJ3wD-XSAYUzAiWX8AWhe5bYEtQS_N3lc5guZfJUbuSpNy-x8Ojo1U4koSomcKgfUEmlrVJPCE98UzjurYNWniKu6MfmKwargQ2XbK4mZs5xvfCMnG4CVOCIvvT44OqxgwHSx9myDdVqTVKAEyWV4D2ykUmsRs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299316a1b0.mp4?token=B8J3kU751JDePRvBlczy_qRYxP4G4KWUuv-b-QhXFu2AW-brneiWOLtJaATa2M203Md6LeUOBLx5Dpc4-_XlZlzRLC9a9B0i4tI1orC2Zz1MHMg9IKNB-VPpauUwpxcTVKEGBM1qPpjC25pEDMBIgk8aeBOW-LsU2M3ebG1K_2YGuV_dSzrxWafD7iGvH1aMhOb9qwiGxBt4ZGxubU3X4Tud49QB5Xt34K-3RU-yvGi_ltrHdCdgBiBm5bJHwOT0Ajj1Jckvu3n3K4ZfKyOnVxIAIpNvDmdoKpSBLkprtUAjMtjmgAPzOWed1fZ51k5JIpHzS9PV83emc59L2wQhDRUTjiWp3rK5ldUKBaf8efqBoOVDytT2gs-3BmoDGxsQqPluH1AHPAUm4oLfL7mEcwjM3f81_re2yR4FbcX24n3wBuhJELD5JhTg3U8c5qTTVb-CCtV8XfYmQESNDbQQ5Q98mm1shXJXnEL9QyVCmHgUW2Atxq9rRK3vZvYBnmsloar1L3D_kUBFCKJ3wD-XSAYUzAiWX8AWhe5bYEtQS_N3lc5guZfJUbuSpNy-x8Ojo1U4koSomcKgfUEmlrVJPCE98UzjurYNWniKu6MfmKwargQ2XbK4mZs5xvfCMnG4CVOCIvvT44OqxgwHSx9myDdVqTVKAEyWV4D2ykUmsRs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش:
اگر بانوی ایرانی یک سرباز آمریکایی رو اسیر بگیره بهش ده میلیارد تومان پاداش میدیم.
مردم کشور های منطقه هم اگه یه سرباز آمریکایی رو اسیر بگیرن و بدن تحویل به اونا هم پاداش میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/72493" target="_blank">📅 22:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72492">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دلار ۲۵۰ تومن
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/72492" target="_blank">📅 21:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72491">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1SRA4u0aahhXhGFxy3MBoJ_lG8mjMRc_ZiPfaMoYyoRzqzWiRez-4mUTGo0fzZZaPowRbpgw9rWTy-TJspGhyuXnJoiClDSJTzuGUCLxsVzfIdAzYy7OjAPlWgBtkJUPk-3vt_7h65aN7o_jFEcPYEnIF0YDADY1fDp8ef8PqgCCzmQlf5TnFyiGYAQPeSvlIolaC5ETRs0tmQHuWDdLiOlT8onlZHxh7c10d0MhbzHGhmqfabce3wMK9L3LPkZX7TlK4KjFH0wh75aR3gNs9x5YhW8QgOR-EyI-spaHi-kfH5R63etHiizGDLMZGIlS6XQjA4lvBoRwnjGfcXXwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا ۱۰ فرد و نهاد را در ایران، چین، هنگ‌کنگ، پاکستان، عربستان سعودی و ترکیه به اتهام حمایت از تدارکات نظامی ایران در چارچوب «عملیات طرد اقتصادی» (Operation Economic Outcast) تحریم کرد.
به گفته وزارت خزانه‌داری، این شبکه‌ها برای «وزارت دفاع و پشتیبانی نیروهای مسلح ایران» (MODAFL)، تسلیحات، تجهیزات الکترونیکی و قطعات با کاربرد دوگانه تأمین می‌کردند که در برنامه‌های موشک‌های بالستیک، پهپادها و هواپیماهای نظامی مورد استفاده قرار می‌گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/72491" target="_blank">📅 21:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72490">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBHMzoYvMekRkeMNd6kK_1KBfCdPCZZnYbIQYudCqtz7lnAFFxC0JzrgM3jlx17Gwr_TAZ4i7twPnPc4G1471W_HleNlmVTHR-fUhSA8u5sa-t1SzezAFZ5Nass_R6uLvleRbXWEgs3HGtR7axQmqqtJ4gB1cUAkULHrFR34Xok1WFJEa0F9W7FiEcIeOyvZ2dP3yGiyletUQ26uawAoTRn-tkmTJrpLpLGqQfhYJhK-lARmfer1EsATNKfslgFy6gMGujwn7Iv4fGOabSNiAw8SaxvDTwnb3l4nuibr_UOkQ_LUZ3ZWtjEtVdxWE2VrHou8zHmgi3u5gVlQq53cuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آی۲۴نیوز:
یک مقام اطلاعاتی آمریکا به شبکه «آی۲۴نیوز» (i24NEWS) گفت که ترامپ با ارزیابی نتانیاهو هم‌نظر است؛ مبنی بر اینکه ایران یا متحدانش ممکن است پیش از انتخابات به اسرائیل حمله کنند.
کابینه امنیتی اسرائیل امشب تشکیل جلسه می‌دهد و نتانیاهو نیز «یائیر لاپید»، رهبر اپوزیسیون را برای ارائه گزارش امنیتی فراخوانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72490" target="_blank">📅 21:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72489">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f526b16f27.mp4?token=GjL4RdUy1JnjLIp_dUtEJMtJ2DsabSYBnMEXEoZdcZSa_yQHSui5PjG5gPwonXOmJsd0tgHyHDYnF45U0_bfLWYg2lvf9vf3kgsxhmmYMW0XN2fnNYHwgCXTqKPiPsHxH7o8QHZeLDkgkUXBr7BMJFG7r_0sxC-oRlQWa9QNkzNfrAOBUyitkSKgygaUq3iN7B5VvVuDUp5nr0AbJr9nQr8IwYfdqsKHAn0UaJxzJeXQtLm42QoUZnom4XiB26Gs18WfatnYHBrgui6sfvw3HtRgHoPUgul3XjnLVZhiw_7P7suBERWmFEakwk_WcNfbZb89kGqM3v6S4viI2n7XdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f526b16f27.mp4?token=GjL4RdUy1JnjLIp_dUtEJMtJ2DsabSYBnMEXEoZdcZSa_yQHSui5PjG5gPwonXOmJsd0tgHyHDYnF45U0_bfLWYg2lvf9vf3kgsxhmmYMW0XN2fnNYHwgCXTqKPiPsHxH7o8QHZeLDkgkUXBr7BMJFG7r_0sxC-oRlQWa9QNkzNfrAOBUyitkSKgygaUq3iN7B5VvVuDUp5nr0AbJr9nQr8IwYfdqsKHAn0UaJxzJeXQtLm42QoUZnom4XiB26Gs18WfatnYHBrgui6sfvw3HtRgHoPUgul3XjnLVZhiw_7P7suBERWmFEakwk_WcNfbZb89kGqM3v6S4viI2n7XdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از فضای معنوی مدارس مملکت و دانش‌آموزان نمونه و پرتلاشش:
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72489" target="_blank">📅 21:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72485">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8f5d17f2e5.mp4?token=W0y-YroKg-0i3oAjNwwy7L-QHAlqlkOzEDCWftBAv6YpTSMrZ3QIoMsVMI6DsrzlOMM5AjJFq8N_v_WY5Ar9Rtz_p1yrkurva_zn4Y4yNLGuZy4zMR1OrjutFsVzCdNnUhG0EOp229agjCCfVJeJdRJbf-jzD7jQSYf-1P51IwzMw8FYl7rmUaEgjM5m9DtHDB35nN1sdnYs6r5-mryWfqnPbtQwcAHwn63ck24Sp8KD-Fkx8FsADartFkXzd5hKJ0omT1FCTOTRAQtN4CWCHeWFIpxEbEcymLYW8TOJINwMgSbVFqXGaiqkD9BW0O-NoOd2bWVhnUXDsqd4mOamrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8f5d17f2e5.mp4?token=W0y-YroKg-0i3oAjNwwy7L-QHAlqlkOzEDCWftBAv6YpTSMrZ3QIoMsVMI6DsrzlOMM5AjJFq8N_v_WY5Ar9Rtz_p1yrkurva_zn4Y4yNLGuZy4zMR1OrjutFsVzCdNnUhG0EOp229agjCCfVJeJdRJbf-jzD7jQSYf-1P51IwzMw8FYl7rmUaEgjM5m9DtHDB35nN1sdnYs6r5-mryWfqnPbtQwcAHwn63ck24Sp8KD-Fkx8FsADartFkXzd5hKJ0omT1FCTOTRAQtN4CWCHeWFIpxEbEcymLYW8TOJINwMgSbVFqXGaiqkD9BW0O-NoOd2bWVhnUXDsqd4mOamrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج استعفا در ایران طی ۷۲ ساعت اخیر!
طی چند روز اخیر، یکی از شدیدترین موج استعفای تاریخ ایران اتفاق افتاده و پرستاران، معلمان و کارمندان به علت حقوق بسیار پایین، از کارشون استعفا دادن!
به قدری این موج استفعا شدید بوده که خیلی از بیمارستان‌ها خالی از کادر درمان شده!
خیلی از کلاس‌های درس هم دیگه معلمی برای آموزش وجود نداره و صدها نفر استعفا دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/72485" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72482">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f441db6e.mp4?token=huPz8SgcTOWhoumZof1whqtpuf-O3BCN_3baXozyaHxTp2oUiVy9XC-HUrYpl6xhxpaHe0B-zudepyhJcevjFzy2DemHyYGgveeY5uPPG_i9YZZFQf8_GfKg1W5FG3R_YWWnPWWKmJ7lEHZYx1MCKMt7Jqypjd5HUXDYOU6lv1SV6tzEuoaB2bTO8RCUqc1vB-aqqkwQWu1AS-TDEF9CS98QdEAzfGvZpch7LIpbJc-6YxhLFvj1QLsKH4V-px7rwZkKKLKfP3SecxKM4_V5Nm5-H-0f0F8dYkLdE2uEaxAx76bRYHpPoMjYw4Zbq4UH_Uxv8Uw-uxkzfAcM1bnUug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f441db6e.mp4?token=huPz8SgcTOWhoumZof1whqtpuf-O3BCN_3baXozyaHxTp2oUiVy9XC-HUrYpl6xhxpaHe0B-zudepyhJcevjFzy2DemHyYGgveeY5uPPG_i9YZZFQf8_GfKg1W5FG3R_YWWnPWWKmJ7lEHZYx1MCKMt7Jqypjd5HUXDYOU6lv1SV6tzEuoaB2bTO8RCUqc1vB-aqqkwQWu1AS-TDEF9CS98QdEAzfGvZpch7LIpbJc-6YxhLFvj1QLsKH4V-px7rwZkKKLKfP3SecxKM4_V5Nm5-H-0f0F8dYkLdE2uEaxAx76bRYHpPoMjYw4Zbq4UH_Uxv8Uw-uxkzfAcM1bnUug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه حال‌وش:درگیری شدید بین نیروهای نظامی و افراد مسلح در ایرانشهر
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72482" target="_blank">📅 19:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72481">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/488280f6be.mp4?token=Pz6wThJEjw_UaBQ594sidMBYGtCJM21Od1l942g5kwHMWb_e4njGKTr2xHn580z2aUCRIEmOiz5DcxIVRfR869eCTXvlOw8sKd7LZXzC2ByulmqkBP2_TnoSTQX_OkfrEWoto6OmFr8_bahW_e_ki0b9aJ2y89o6yzkdQohuWJANoERcdO0Ak8_9gJ4dS6ws-ipHk3InAmmq6o1oMwwUY0Zjm4SSibwoN5lu4b8urRPNQDr0um2sK1mdd0NbFr_jv5s84LvDV95PisWtphGrHSHcImMmNMBDJuj9n6gcuyZ-X6vTrOn53OsbfRO8UdlWroOoRWWu6bLSbTBj8zuvmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/488280f6be.mp4?token=Pz6wThJEjw_UaBQ594sidMBYGtCJM21Od1l942g5kwHMWb_e4njGKTr2xHn580z2aUCRIEmOiz5DcxIVRfR869eCTXvlOw8sKd7LZXzC2ByulmqkBP2_TnoSTQX_OkfrEWoto6OmFr8_bahW_e_ki0b9aJ2y89o6yzkdQohuWJANoERcdO0Ak8_9gJ4dS6ws-ipHk3InAmmq6o1oMwwUY0Zjm4SSibwoN5lu4b8urRPNQDr0um2sK1mdd0NbFr_jv5s84LvDV95PisWtphGrHSHcImMmNMBDJuj9n6gcuyZ-X6vTrOn53OsbfRO8UdlWroOoRWWu6bLSbTBj8zuvmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور، درباره مجتبی خامنه‌ای:
ما تصور می‌کنیم که او زنده است. البته دقیق نمی‌دانم؛ هرگز او را ندیده‌ام.
اما بهترین شواهدی که در اختیار داریم، حاکی از آن است که او زنده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72481" target="_blank">📅 19:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72480">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSxJMe6fOQ80uusoNGT7PGsm1X1wzhylJAqJBtZrhXzaCQrqWDYoyuHuvajhiXDTUAWbbaZeEaFDZqlSXK5zyXdTm1LSaLIo9xcrfWnR6mRzSmr1NUfaijtoA1GCZROC3-8gYtz_4R_tO0vsGyYQocesegODhtd61sovkCVuLq3eQXUovrBmt8_7PYY3h-wQ8UhLZqIQPs58jXNHhG9N3vkDSbUpenyBKboxadTKKmTd1SLYb-_paUhTUU2Db3S4_Mt2ZligE8TbdwQMWCVDPWHfSAVY-FkyHJ5J5c0m3klcgGQbg8Q7fnLj7oJc_mwyIiHOPJRLu4Zk1hPA8tYHWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی از اصفهان؛هر لیتر بنزین سوپر۱۴۰.۰۰۰تومان!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72480" target="_blank">📅 19:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72479">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72479" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72479" target="_blank">📅 19:30 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

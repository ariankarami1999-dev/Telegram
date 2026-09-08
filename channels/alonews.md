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
<img src="https://cdn4.telesco.pe/file/iFi5XvlBLPrOdghwSKbo3rsmT6J8NefTDpmM2MaujNGFLpc5Xr1HKyLPdEtFEaxMFPYVCg0qxZ6Xg6CoXXKBY9t7Lf2pQdt2cWu3UCJHDtc7nMpnRha9UAQG35ErEkEFqjN1Tl64xZTnYiHlyGcsgQD8ssZVrbwLZncwkcg8WCyP3WCJOAX8RMDstqNtLGyRte2ACBX_54xpjFmNhJCUW19pIZdHFrRZv5Sgb7-lKBG4p8FIjYk2Fmwew-feTTLKhm9drDRErod1H2I_GStVyJtl_KlMH79YifL_NurBwTUnN9gXeY9rLMeYElRwVMimV_q44xRcUtMhPHwiu4VybA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 928K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 08:58:33</div>
<hr>

<div class="tg-post" id="msg-146179">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70365c549f.mp4?token=p27x9HZC202y6FgV61oUrXLHUqHOWVKgSt_o8OJF-yWGIpNE_qbaDj8uv77Rd49wWJ_IR6Jy2R9JwQxmYzmls8EQDi_rWUv1dxsXn4nqA3axxKg5gqldif3nQ3TPEuHuDNa00X8ugnY4Wia6fWy1B5gPmSNs9Fy1JyUZhy-L_EEHclQW5GuRzPDXChzywaf7NwU9590pPt4OLm7Na3heihv2FeCxeOZnoECl8lNd7vK1h95ii1Z61BC9zuya_jjXXPUnOYFjomsE5C2ZZojN51b25y9Se_PDm6J3-Z914sjFfZjJuulZNO0ofYXthH8seCtd1-MsUgz48fHUqys7YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70365c549f.mp4?token=p27x9HZC202y6FgV61oUrXLHUqHOWVKgSt_o8OJF-yWGIpNE_qbaDj8uv77Rd49wWJ_IR6Jy2R9JwQxmYzmls8EQDi_rWUv1dxsXn4nqA3axxKg5gqldif3nQ3TPEuHuDNa00X8ugnY4Wia6fWy1B5gPmSNs9Fy1JyUZhy-L_EEHclQW5GuRzPDXChzywaf7NwU9590pPt4OLm7Na3heihv2FeCxeOZnoECl8lNd7vK1h95ii1Z61BC9zuya_jjXXPUnOYFjomsE5C2ZZojN51b25y9Se_PDm6J3-Z914sjFfZjJuulZNO0ofYXthH8seCtd1-MsUgz48fHUqys7YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آب‌گرفتگی منازل در پی بارش و طوفان شدید در مازندران
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/alonews/146179" target="_blank">📅 08:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146178">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8osYrdaY6hCLhkhMJXF3EYyzmpi7YBZ2gzoT6NZt1a5td8qKy9P5cYj0TwmfN-kVofZVcAevoU1yBI4lbmcnC9qNV2OCTI7uMXPHR4Bga9MZaTNf3AlhPl3J8Uh569HKAEOszoGnHDc0bh_g7ePL73JK-07UnhndHzjBhb6vzZ0wYYLMR-gqNK3ejXUNUoG6xr9PnoPGXMTtKie7rymujiiNRbV1jGMjmna2Fpi5qfTyQYcVhsr3DcXOOjR2y4PyydBMjzC_e-Ekd11uasZUd6FKM2_LjF-4lb0Vdz_WaWf1Wzd74QeJUkm8x9_y3Tg9fxMFXYdl12oJyOYz7Qqrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایتامار بن گویر، وزیر امنیت ملی اسرائیل، از دولت اسرائیل خواست تا تحریم‌هایی را علیه بریتانیا به دلیل "اشغال" جزایر فالکلند آرژانتین اعمال کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/alonews/146178" target="_blank">📅 08:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146177">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d0ce49abf.mp4?token=TjD1xnum1E2mmQq_0Fw1rm_gDDXCGF4CtUWa5IU7a5N0iMiY8nUhhbVsx-vF8bmWHb96XiVcGIZXhgV8VGXj4YniH6TypInbPpTZrKB41aQx8X2H2OXJMD5SU_3hCNkS7jO3GZcSrQzd_lDpng89z70fUzWa2nCbGylMyFJ12cNctZMBvPGo-wCva4T8_n-dhpwEopDBoB8368m10Vx72zcIrUSOaDbsDmpBV5tvhANh2My5bzJdIpkwldbbEqlMZz_4zzc5ZRrOH_0D-XAqnUe5-A6j1LfEodBx5VoYfXI2IN_nr5rX22jOcr2mZvFy_9jgPRrJgRqzxWuQGRfoPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d0ce49abf.mp4?token=TjD1xnum1E2mmQq_0Fw1rm_gDDXCGF4CtUWa5IU7a5N0iMiY8nUhhbVsx-vF8bmWHb96XiVcGIZXhgV8VGXj4YniH6TypInbPpTZrKB41aQx8X2H2OXJMD5SU_3hCNkS7jO3GZcSrQzd_lDpng89z70fUzWa2nCbGylMyFJ12cNctZMBvPGo-wCva4T8_n-dhpwEopDBoB8368m10Vx72zcIrUSOaDbsDmpBV5tvhANh2My5bzJdIpkwldbbEqlMZz_4zzc5ZRrOH_0D-XAqnUe5-A6j1LfEodBx5VoYfXI2IN_nr5rX22jOcr2mZvFy_9jgPRrJgRqzxWuQGRfoPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این زن ایرانی اسمش فاطمه حقیقت پژوه هست، سال 1381 تو خونش خواب بود یهو صدای جیغ میشنوه و از خواب بیدار میشه، میبینه صدای جیغ از تو خونه ی خودشه، میگرده میبینه صدای جیغ از تو اتاق دختر 14 سالش میاد، درو باز میکنه میبینه شوهرش لخت تو اتاق دخترشه و داره به دخترش تجاوز میکنه، از شدت عصبانیت و در دفاع از دخترش شوهرشو میکشه، تیکه تیکش میکنه و میندازش تو رودخونه اطراف تهران، پلیس میگیرش تو دادگاه ثابت میکنه داشت از دختر و ناموسش دفاع میکرد و به 7 سال زندان محکوم شد اما دیوان عالی حکمشو تغییر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/alonews/146177" target="_blank">📅 08:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146176">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه آمریکا به الجزیره گفت: ما در حال هماهنگی با شرکای خود هستیم تا اطمینان حاصل کنیم که مانع‌تراشی ایران در ناوبری قابل قبول نخواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/alonews/146176" target="_blank">📅 08:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146175">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6mxpPz1Krf9TIFiC4Se8PlSHYXX_BWCaN2TTliqKna2gMx80agXs9UwPnF4K5l9QJfXN-GwXtriUP119MS_Gd5psokv5M5e8F_QLadC8GdYpKF_2dflopYoTdtO9CuemlU5nzxR-zu2LE_xzYeUCY11rL5fKIHSnT8E0McrRCEl3_fT2j0EzcoNDOpQ67KAiAonerEh0q933wUGcAhBIg5FRXBkXl1FvKOppuW12Kl7orypZLI-f1FINxLUhpEOg0H8IGzjH8XSuhE19aDMMZ0Q4XCnuF7pohH8c3chnHgTJS19sf1R09gnQquivYCzfEHeoBwdARRdXhbgCOTrow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پهپادهای اوکراینی بامداد امروز پالایشگاه نفت ساراتوف در جنوب‌غرب روسیه را هدف قرار دادند و موجب وقوع آتش‌سوزی در این مجتمع شدند.
🔴
پالایشگاه ساراتوف از مراکز مهم پالایشی منطقه بوده و در ماه‌های اخیر نیز هدف حملات پهپادی اوکراین قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/alonews/146175" target="_blank">📅 08:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146174">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ اعلام کرد که شرکت هواپیماسازی کانادایی «بومباردیه» دیگر اجازه فروش محصولات خود در ایالات متحده را نخواهد داشت، مگر اینکه خطوط تولید خود را به داخل این کشور منتقل کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/alonews/146174" target="_blank">📅 08:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146173">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjuKWL-fsiOe__cjz-wFGCHWLOCQgfTtRtN2ubBm3kXkMqEsqA7e9VeIrPIHYvBYUBHCnFY65D4ztGKE4jYZ_J5YmUBwQCHmPdP6NzJ1LTiLja1Gyca4skwUT4XuBitY9KsUnlZIPoxjNWBko8URxjRxqlt6wv1LJImv0tEoF2jjlZuoX5iQY-N5GHFrj68idotn2OIBXEap-5WZ7xapFRuuMbmSbaM8cqi8S8RdPilParcynExnv_XZo5UVZZ7JTeUW34bJ4gBktvHU3XTZNN-AeG3quidKRbqglDrkALepP2de3JTRbjS8xjDVEJnYXs4Cklj811oICvofSKMOAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانادا رسماً تعرفه‌های تلافی‌جویانه‌ای تا سقف 50 درصد را برای صدها محصول آمریکایی اعلام کرد، در پاسخ به تعرفه‌هایی که رئیس جمهور ترامپ اعمال کرده است.
🔴
این اقدامات شامل حدود 20 میلیارد دلار کالا از آمریکا می‌شود، از جمله فولاد، آلومینیوم، پنیر، لوازم خانگی، پوشاک، لوازم آرایشی، موتورسیکلت و تجهیزات کشاورزی.
🔴
نرخ تعرفه‌ها از 15 درصد تا 50 درصد متغیر است، و بالاترین نرخ برای فولاد آمریکا اعمال می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/146173" target="_blank">📅 08:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146172">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTi_rHQR5Gcw01KnYaTIXzZUjSvuKombOSQXHq4h-OEvjG1xzr7U2UsQqWLjRbwJls8aHQMbzCd1fH79bpGDFS7Fn32gSzuwjpxmqDp0byXInjIx5XF2Avwf8A5Wvrt0s-DTCrFRCbv9n7oNl_fiqw0ZxWCtjjz7NfcNVjjQaCEw61AH6ok5QQmGBaKtbm2dYpgcFha5ndNouAkZahlie5e-KPK-qdRY7AjByUt-l4vqabPPZoAONP-zbqXcLTLRUXQPWqn8T73rYXy09Lp0PG0FGZrqkBj3yKE5z3gvBI_aGjHtaXtM9-E0xd-npo0im3uXiLWXwEDulzF-sTHbEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : قیمت نفت به شدت کاهش خواهد یافت، درست مانند کاهش قیمت همه چیزهای دیگر (اما بیشتر!). زمانی که ما در جنگ با ایران پیروز شویم، این اتفاق خواهد افتاد.
🔴
قیمت هر گالن به سه دلار خواهد رسید، اما در نهایت، از دو دلار به ازای هر گالن کمتر خواهد شد.
🔴
این اتفاقات به سرعت رخ خواهند داد و ایران هرگز سلاح هسته‌ای نخواهد داشت. ما دوباره آمریکا را بزرگ خواهیم کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/146172" target="_blank">📅 08:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146171">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
چندین اسکادران جنگنده اسرائیلی به همراه سوخت‌رسان‌های آمریکایی در حال پرواز به سمت یمن هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/146171" target="_blank">📅 02:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146170">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ارتش عربستان: عملیات نظامی در یمن هم‌اکنون ادامه دارد و در ساعات آینده نیز به قوت خود باقی خواهد ماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/146170" target="_blank">📅 02:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146169">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51336edb7a.mp4?token=QU4X0lL_PoMKr0F-ebBDNh2XiAmwdTCgFNhzTMSS_jOBjuvHXEb2tBKd_l_KY8lWUzEL3PbhIIWFQxxqdEQJfY-HiRZW0oAdZ9mcXeurwoenDrhh7S8dzb0dghxUoL0zkJGakvoKc3RDKQUzCni2tFJmGpJZ6OpV0wcR3X8O4qXMeDVDSNX_Ian4DMsXaUvyGJ7xsTL9P_s0Ypef_Ug8j3W1hXBH52ozokyyvMRbwFFLUnT4pNaXVVzlkO4iLun-viEjGkfEFrkW2jB7l-Kg0wlVplad0M5XLfJ6UCxhvNF_ln3ThGhMLCr4P0Hxyi01Go4a9NAjUptQ-IdG23toBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51336edb7a.mp4?token=QU4X0lL_PoMKr0F-ebBDNh2XiAmwdTCgFNhzTMSS_jOBjuvHXEb2tBKd_l_KY8lWUzEL3PbhIIWFQxxqdEQJfY-HiRZW0oAdZ9mcXeurwoenDrhh7S8dzb0dghxUoL0zkJGakvoKc3RDKQUzCni2tFJmGpJZ6OpV0wcR3X8O4qXMeDVDSNX_Ian4DMsXaUvyGJ7xsTL9P_s0Ypef_Ug8j3W1hXBH52ozokyyvMRbwFFLUnT4pNaXVVzlkO4iLun-viEjGkfEFrkW2jB7l-Kg0wlVplad0M5XLfJ6UCxhvNF_ln3ThGhMLCr4P0Hxyi01Go4a9NAjUptQ-IdG23toBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک‌هایی از یمن به طور مداوم در حال شلیک شدن به سمت عربستان سعودی هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/146169" target="_blank">📅 01:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146168">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
عربستان، یمن رو بدجور بمبارون میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/146168" target="_blank">📅 01:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146167">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b9JweW-7fsBdA-YCr0kjGohub7oGBj0-WKM8tEa6cCfDCdyEfhCyoEEoBDczupgH74JoJy5A4SpmplHiGp9LiEygLcPEpEFMj666UrEHICicDkvm6YRgdj0J76-a0nexRnh56ExdxQnf0sbO4PngY0B4MViN5DakD3wOtN6uTO9CKm6lKJPD3kiCvh902EPamsQ6gxHWCE3RSUGpn6oafBLBR-SXkRB80-8JXLJcwuDd3U267t4pGhMMAIXnNzyz520rjuomDYKcAlmgPj9epcOebKFSfzgeQoVCCaWGPMkbZLtfJ01Bc8PH3nRve5GX3BSzHNUS9ftLDxBVCeqHcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط فیلم....... بازیگر تگزاس در اومده
😐
📥
مشاهده فیلم</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/146167" target="_blank">📅 01:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146166">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsCgADqKydrtw9NDvm5udN-gKM4Nw-2GylGutKKkuizvo7uvwKSjFC6VNuQgEWpv2KBCPG27kN5R0eKR6MotcP0G4WIvQb9mxJMDRmGDQZYGP-Fho7ylAwVXWEX1en0dpSCKaCoTLbT9Vp69wvcE4hHEYLgrhBLrjpS_2NRj7Hwt8Ab2F1tF8tgj3QGqkPSA8qmyQXnngvbfxc7DjXirbz7ptZm55EkyJgd9i35iReT2Oy13I16fkSyl60xoaZAshy7ty9-WURzcgzVsZntYgXxfUDrtm6P-CMp2DCDdDR6-Wgikc3vmn0Cmo6ubEM2rj7eA01fo0QjPZjZPgQiogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طی اتفاقی عجیب بابک زنجانی بخش قابل توجهی از املاکش(مال مردم) رو به نام خواهرش نوبهار زد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/146166" target="_blank">📅 01:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146165">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a515fc01ca.mp4?token=FzlW7ERisQG1nPScmjV6wNxIXBvKSUAzqpxHyIZz6vVtzEOgM3LN7uWb7SYw-jNzm4O2QZlZrH90FgAmlHj1reF9Vyjxr63vOHfw-XfTK1H35T2rZfkuDTJnLUxX4iQ76sUd0Hmud1FJyjLoVVpqRXdBpc0gFWPMUQwbCZxUOO8ZnMktzTe2IMOGwPnC5_dtw0YM4eRpaxiiJSSk04UrztzuhU_aE9C_sTSvPM8_IGNmcOPkGJ9tUJIrb67W9ynv0urGFWm1Fwlr2oVzWrjZufde-AM61iKFA3-k1HYT7SGfPGr6sXQhnyQkqTUdjHKYONjtFzZTLLpFo_DJcdHduw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a515fc01ca.mp4?token=FzlW7ERisQG1nPScmjV6wNxIXBvKSUAzqpxHyIZz6vVtzEOgM3LN7uWb7SYw-jNzm4O2QZlZrH90FgAmlHj1reF9Vyjxr63vOHfw-XfTK1H35T2rZfkuDTJnLUxX4iQ76sUd0Hmud1FJyjLoVVpqRXdBpc0gFWPMUQwbCZxUOO8ZnMktzTe2IMOGwPnC5_dtw0YM4eRpaxiiJSSk04UrztzuhU_aE9C_sTSvPM8_IGNmcOPkGJ9tUJIrb67W9ynv0urGFWm1Fwlr2oVzWrjZufde-AM61iKFA3-k1HYT7SGfPGr6sXQhnyQkqTUdjHKYONjtFzZTLLpFo_DJcdHduw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انقدر ارزش پولمون تخمیه که تعداد صفرهای قیمت بنزین جا نمیشد و اومدن کنار نمایشگر‌های جایگاه بصورت دستی یه 0 اضافه کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/146165" target="_blank">📅 01:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146164">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
هم اکنون حملات هوایی شدید عربستان سعودی به مواضع حوثی ها در جنوب یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/146164" target="_blank">📅 00:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146161">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WUZvprctvwtXX5p9U0cNMqDvCoUHl6U9gIVIMyi1GxcfoWa2MFiL2MmRU598j2UwjarE-LXumVh-0EON_TDyjL-KOBAZfIymroqkCQz24HkDOb5Uvbn7nyJ-yYrJu8UkPgYFpI_RhFRfn8NQW3FoAWfu8xdW-1J5UhqR1gyqRqsAXINYn01ZCsd4NneBjaQ_W0rAwZQ9H27KeVYVK3kCBJN52w7TKwgtKRS1BKl9IJMvCIxTOP8F5EiwyLaCYWrohojv3-UnXel2aKY6htJ0najnvuTHImhIwpl9GzVdsIgacjUJmt82TcaACT4GnnipViKO4hdD8iSZZzZBaUBXRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8833895957.mp4?token=D1Huk5YBcn7GOw_pwOld591pDZwr8Bi9LRuiRWfVAVQBbqr6vLapunPVLyP4XwuQ4UAKTWJoMy8yNPbPeB-VF0iR9OIOMLoMfNbltWHMw6TBgSh9JcquS4eRiQmhvHBAitOb_78nzq7y4XccY66iag9YN_4Oxcul2am5tMGBcrI3CFf12VicIO4SdUvXFUM1ywkpN_gLm-E6jjHS5SNIPvjfy5siYWaYP5JDlJT_0lM7kK9elAlvXIXTzpzSwWCyrjRsyQ3PIwaqWFR-RC0zJJ5z7uOMZvy2Xxa6Qludo74d6dnFuVbHe_XFjvUSsC_aNSAjGkOWMTYBs2BarTb0NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8833895957.mp4?token=D1Huk5YBcn7GOw_pwOld591pDZwr8Bi9LRuiRWfVAVQBbqr6vLapunPVLyP4XwuQ4UAKTWJoMy8yNPbPeB-VF0iR9OIOMLoMfNbltWHMw6TBgSh9JcquS4eRiQmhvHBAitOb_78nzq7y4XccY66iag9YN_4Oxcul2am5tMGBcrI3CFf12VicIO4SdUvXFUM1ywkpN_gLm-E6jjHS5SNIPvjfy5siYWaYP5JDlJT_0lM7kK9elAlvXIXTzpzSwWCyrjRsyQ3PIwaqWFR-RC0zJJ5z7uOMZvy2Xxa6Qludo74d6dnFuVbHe_XFjvUSsC_aNSAjGkOWMTYBs2BarTb0NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این وسط تو رشت سیل اومده
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/146161" target="_blank">📅 00:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146160">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKBEnKrUM0ondKnuWW2yzEF_weN3Ve3WYMEz6J5jDlI-WM77B06dcq7sAvSs6y6bZR421nk2B-DoOF4nXtbSa-yqVGYxI06t16gKikQk04BkhSF1Y117sN0yZFuvz3Ch1gQwq7GpficNtM3oFn4x-9kKFOhfTVhpbUci0XTm5sQyNaAHBr8MvfVpv_tfJe8c52gRgWCY0PY18Sj-BDL9iXe_myyAS9Frmsfp3nuqvZdsA_bLy1VAYJBPdwzgrMMPVwApVC3ZXXwcPdcCp7ZbEQgESqBr9yuSuzIMVCT4Wb2ldo8RAEoAsGlhHZPih6haQtWsTgupumKfm-fWLDN4-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز تولد سید مجتبی خامنه‌ای هست
🔴
وی حدود ۶ماه در غیبت صغری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/146160" target="_blank">📅 00:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146159">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وضعیت این روزای ایران خیلیامون رو به بن بست کشونده
درآمد 95 درصد مردم الان ریالیه اما قیمت همه چی به دلاره
اگر بخوایم از زندگی عقب نمونیم
و جزو اون 95 درصد مردم نباشیم چاره ای نداریم جز اینکه درآمدمون دلاری باشه
همه وارد کانال زیر بشید لینکشو گذاشتم  همه رو به درآمد دلاری میرسونه لینک کانالشو میزارم عضوش بشید
👇
👇
https://t.me/+fDXpi2Dbi185ZjRk
https://t.me/+fDXpi2Dbi185ZjRk</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/146159" target="_blank">📅 00:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146158">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e221ca09.mp4?token=O4czq_HIPVmgn_qELh4XeMtuyWnDu7bQO2Hlz7kh9LFnG5Ft_040k8yqzFfj5VJsp8lPxkoCPaDSyGjP5a2C-fCpCsX0OSauXoEySSKvojSG5FIB1xQGFPFy7HaAEqOrku0k_-W5Ik50sszgRPpCOVNH2WJqjE2EDHD7d31gZiwM13gYwE7iWfSkXmcrgyYn4jfUa_p2nRGoRy8MEu5Ch0O80doCBE0JFsG0KKre_h2QP55iqBGNNP0nZvrrHygZt3ygVznJoo5NT93d8P_ZqLsOVKaVTMxTnumIUDCV2td5daeHk3bwOQwYX6p-ajuBVF7hHZtk5Wo5Lb3-Vzyfrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e221ca09.mp4?token=O4czq_HIPVmgn_qELh4XeMtuyWnDu7bQO2Hlz7kh9LFnG5Ft_040k8yqzFfj5VJsp8lPxkoCPaDSyGjP5a2C-fCpCsX0OSauXoEySSKvojSG5FIB1xQGFPFy7HaAEqOrku0k_-W5Ik50sszgRPpCOVNH2WJqjE2EDHD7d31gZiwM13gYwE7iWfSkXmcrgyYn4jfUa_p2nRGoRy8MEu5Ch0O80doCBE0JFsG0KKre_h2QP55iqBGNNP0nZvrrHygZt3ygVznJoo5NT93d8P_ZqLsOVKaVTMxTnumIUDCV2td5daeHk3bwOQwYX6p-ajuBVF7hHZtk5Wo5Lb3-Vzyfrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سردار ابن‌الرضا: توان زدن ناوهای محاصره‌کننده آمریکایی را داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/146158" target="_blank">📅 00:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146157">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
سردار ابن‌الرضا: توان زدن ناوهای محاصره‌کننده آمریکایی را داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/146157" target="_blank">📅 00:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146156">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
همزمان با ۱۰تومنی شدن نرخ بنزین، جو شدید امنیتی در برخی شهرها حاکم است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/146156" target="_blank">📅 00:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146155">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eac7169fd.mp4?token=FItI7kj0APGqjKvWoBiE9zh1k60xJlUkuKCf2--c6u6uQewZP3PR10glXiIW1s0eCm1g8fIJAbZr0QlBlPTjjd-PNZbU8RDx-oMbRYe1P7hSQgcNomz0RNzMVdhOpK6Ls5GBEd3GG6H29J033HsYTTQCKK2k8lFZAxKg5BXgr44avdWPbM3D0bB6OMYLgV9HOJy-mDW3nly9QATbr0z-FYrP5AT6xlfmk0dPoDdJYyVOWOu6P487U1PS3Hl9YMm7Gud2GD_v9-8PkEtNEnM_d9M_aFyRVSFOYonTy4frc_NQqX18yxFtx8PN_AkqBh0GS0OR-6Tc2Sepdblj2slBQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eac7169fd.mp4?token=FItI7kj0APGqjKvWoBiE9zh1k60xJlUkuKCf2--c6u6uQewZP3PR10glXiIW1s0eCm1g8fIJAbZr0QlBlPTjjd-PNZbU8RDx-oMbRYe1P7hSQgcNomz0RNzMVdhOpK6Ls5GBEd3GG6H29J033HsYTTQCKK2k8lFZAxKg5BXgr44avdWPbM3D0bB6OMYLgV9HOJy-mDW3nly9QATbr0z-FYrP5AT6xlfmk0dPoDdJYyVOWOu6P487U1PS3Hl9YMm7Gud2GD_v9-8PkEtNEnM_d9M_aFyRVSFOYonTy4frc_NQqX18yxFtx8PN_AkqBh0GS0OR-6Tc2Sepdblj2slBQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عادل فردوسی‌پور: خداداد عزیزی احساس می‌کند کسی باهاش کاری ندارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/146155" target="_blank">📅 00:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146154">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61664472bf.mp4?token=njWLWsfEFjdsi5mNQT_l58Xdc0FFDx4z8s_u1nEs4hq1MNBXXDJY0uvn12vQmzz0CAZmNfl9TgvXetljCs8FSgsKkRlluEgxT7Dx6Qncs-96CqAaKKWbCxhGGHOVN759KDzBe5NJYLBL-6gQLickCg2HMDOJ2qCG8jrp_PTymp-FjY_zvBVI8amgzVdAmcOctyjQvxOqN4FicVfV0mjmcLraHwS35PrM8Htipv7OnAgyYzr4n3UscOsmX_ZGlfXUXOsXNWXvS_epwPBSxiSkU_g3HyYaF6OK_45TUJEK74-xs2bThMpbRRqMcHs6oQ7tCD3CA7rKJkqcXkEd-bxtPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61664472bf.mp4?token=njWLWsfEFjdsi5mNQT_l58Xdc0FFDx4z8s_u1nEs4hq1MNBXXDJY0uvn12vQmzz0CAZmNfl9TgvXetljCs8FSgsKkRlluEgxT7Dx6Qncs-96CqAaKKWbCxhGGHOVN759KDzBe5NJYLBL-6gQLickCg2HMDOJ2qCG8jrp_PTymp-FjY_zvBVI8amgzVdAmcOctyjQvxOqN4FicVfV0mjmcLraHwS35PrM8Htipv7OnAgyYzr4n3UscOsmX_ZGlfXUXOsXNWXvS_epwPBSxiSkU_g3HyYaF6OK_45TUJEK74-xs2bThMpbRRqMcHs6oQ7tCD3CA7rKJkqcXkEd-bxtPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز جنگنده پیشرفته جی-۳۵ چین با کمک سامانه پرتاب الکترومغناطیسی ناو هواپیمابر
✅
@AloNews</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/146154" target="_blank">📅 00:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146153">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POnKbwvwhrFDMzGUobrc2prMGovdhX-w3yFeINJu7yr2vvMO6Rg7bebwp4qz1AERH4B482PqiyUvPwyhV7TexnsyAVEfi2QAnpMij15bIpYhmN9ZQeh_2c9eEtrKBhFTEm6lSgRzhrberWdhYZdygkIXGPuOrUGrjzbtp0Fu5-jwjsZKBiIdVng4hh658sKwP8ofxvwDmgkb0Ia_s8WJoKkMJsu5QUYr-hzaJNFA6eo9yHOP3TJst8DdZBiLjWpXHmg3KZRX2hdBbg8591DCIn2RZUywMFZuJ-AXBfwcANUFJAH93I6Y2St7QlhxYRH2W5ozwr1ax3fZd1F1L99qcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تورم خوراکی‌ها در مرداد ماه به ۱۲۸ درصد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/146153" target="_blank">📅 23:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146152">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
تانکر بزرگ قطری حامل LNG از مسیر تعیین شده توسط ایران عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/146152" target="_blank">📅 23:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146151">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnYRsPFJVgOpT0B_aU59UI8LV2rF7ALTsrssqJtJJmXoNmWI16lJqh4IL9Ex9Ww9b6M553-xVtxsJGrERj4eT5VGwRLGYkc4pfMUflXmIeE194ELaDcBOdqpy8GR9BvuIAQfU4td0DZSpwzgQDEvoGs4d1szaRe95BaI7d0vK9TVfJxswRUjUe8G_dS6RQpPBh1-3fS3VfE_NjmHcypPsPBK_n7bpYfr-gVHBnhyQ5PknUDeMkl9QLBc1VgqPwG48VECpWIJfzsiqTjr8WTzA5hejJHgNJ5QaHBQV1U9SLJ3HoBdzNIR6MYBbyT2fYakPfCy0E63fALU4-i8sst2ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دوستان این تبلیغاتی که پایین کانال نمایش داده میشه کلاهبرداریه حواستون باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/146151" target="_blank">📅 23:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146150">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
خانعلی‌زاده، تحلیلگر صدا و سیما یک سال پیش: تنگه هرمز و باب‌المندب را ببندیم نفت ۴۰۰ دلار می‌شود، این تازه ابتدای ماجراست
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/146150" target="_blank">📅 23:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146149">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/684d994c3b.mp4?token=FPXz0einMPoc8elx8wIC6G7J-fpJuMCMzPs43kMbjWaaw6DSXUN5vh7T7cyXoBGFjiw3kbDXlobDnINZh4wCL4hzRqIu010_bD7Fy7LT0v-2pxOjX2r0PXxIZjGqZXMNiNEruyefTzgryeMYpjEXH2LzxDsAJuzFK3m_dQt_3YwJXWRedHpjo-bAIE0-O7uk-hB0Mt2AfwQ18EtVYbjXImemlRWvawfZJ0AUzLWcuV2FfEd2gqY3ERobylM8kYevTErfQQArlgUWPu8Eg2SvE-UeWUNINtJ4V60pkq12-hoXaIBKhXWanTyZFBFrHdS6LlKvSDSGB6zc-fxOPgNvHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/684d994c3b.mp4?token=FPXz0einMPoc8elx8wIC6G7J-fpJuMCMzPs43kMbjWaaw6DSXUN5vh7T7cyXoBGFjiw3kbDXlobDnINZh4wCL4hzRqIu010_bD7Fy7LT0v-2pxOjX2r0PXxIZjGqZXMNiNEruyefTzgryeMYpjEXH2LzxDsAJuzFK3m_dQt_3YwJXWRedHpjo-bAIE0-O7uk-hB0Mt2AfwQ18EtVYbjXImemlRWvawfZJ0AUzLWcuV2FfEd2gqY3ERobylM8kYevTErfQQArlgUWPu8Eg2SvE-UeWUNINtJ4V60pkq12-hoXaIBKhXWanTyZFBFrHdS6LlKvSDSGB6zc-fxOPgNvHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خانعلی‌زاده، تحلیلگر صدا و سیما یک سال پیش: تنگه هرمز و باب‌المندب را ببندیم نفت ۴۰۰ دلار می‌شود، این تازه ابتدای ماجراست
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/146149" target="_blank">📅 23:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146148">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b7e0f35c4.mp4?token=ZIszTYcV_9b2dM1L7R6UG0qebzWX5pRZkzPs5ZuON6xpC1f-iYBllov18m0l8wPD7nT2M-mSh_rsenxkMS-EMLgWtvs0dqa64WAbu7mN92irorgztyRIPrCOtrGRBefAAHmgq8dHiJ9S5Rinq-PFgmyvy_DP0UNS1drIkaG595mTop-D8UnG7vLAey7QhzIZXY8E8Dj5rfONFZUD6tmLQZIb3ouvmYj-7-pMBxLBREuswhH3IGMUUMUdcC-TrEujiA4S0P8ujA3_dYRQWtt9OKm28u7UrIJM-Le1CujDZwbi9E7XEjW_Pbs7I_f7H3oX5393_gfKCaOGmQHJ5g0rS2tHKBkg_hv9PkN3k2vgCAZ1_SlUdaCEyu1FoJlkcloDmaj6QZXHdq_MPFWDl2XcldRjygiky4QFAHVX4t4f8tRD_tpHwNH1fTZ7ZzAhEvJzbjwFN0NYXfEKPWRUX9b8IrejaykTrJmj82vSuvIOmIRGPf3WNmtwpV-taUpm9TJmxHtc8nYiJarViHN4lUA_lwtw6etHnssR79HUJ08pBLwc1V2ROlyA5pzJfaszyo4Ap9FgNTuOrNBQXt5bX24MeoAuJCqEwF86MlZN1Eo4B_WVct_Ck7DD4AwoUHoPvcDCSRvnN993G-en3rbytoghkl0BbJDdfh9DD-aI9CQ7B10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b7e0f35c4.mp4?token=ZIszTYcV_9b2dM1L7R6UG0qebzWX5pRZkzPs5ZuON6xpC1f-iYBllov18m0l8wPD7nT2M-mSh_rsenxkMS-EMLgWtvs0dqa64WAbu7mN92irorgztyRIPrCOtrGRBefAAHmgq8dHiJ9S5Rinq-PFgmyvy_DP0UNS1drIkaG595mTop-D8UnG7vLAey7QhzIZXY8E8Dj5rfONFZUD6tmLQZIb3ouvmYj-7-pMBxLBREuswhH3IGMUUMUdcC-TrEujiA4S0P8ujA3_dYRQWtt9OKm28u7UrIJM-Le1CujDZwbi9E7XEjW_Pbs7I_f7H3oX5393_gfKCaOGmQHJ5g0rS2tHKBkg_hv9PkN3k2vgCAZ1_SlUdaCEyu1FoJlkcloDmaj6QZXHdq_MPFWDl2XcldRjygiky4QFAHVX4t4f8tRD_tpHwNH1fTZ7ZzAhEvJzbjwFN0NYXfEKPWRUX9b8IrejaykTrJmj82vSuvIOmIRGPf3WNmtwpV-taUpm9TJmxHtc8nYiJarViHN4lUA_lwtw6etHnssR79HUJ08pBLwc1V2ROlyA5pzJfaszyo4Ap9FgNTuOrNBQXt5bX24MeoAuJCqEwF86MlZN1Eo4B_WVct_Ck7DD4AwoUHoPvcDCSRvnN993G-en3rbytoghkl0BbJDdfh9DD-aI9CQ7B10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی سازمان امور مالیاتی: از سال گذشته تاکنون حدود ۶ هزار شرکت سوری شناسایی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/146148" target="_blank">📅 23:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146147">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
طارق صالح، عضو شورای رهبری یمن:
حملات زمینی و هوایی را در تمام جبهه های شمال، شرق و جنوب یمن بر علیه حوثی ها آغاز کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/146147" target="_blank">📅 22:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146146">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
معاون اول پزشکیان: یارانه واردات بنزین به‌تدریج حذف می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/146146" target="_blank">📅 22:47 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146145">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VL1vvRq5JHW5YhumVFbJGSLBs6NTAEAq-WCIgVMT1sOfM49BiQnY_-wweAZI8mRfehNEV3-kin8G4gPRLaCJNn0hT6X97Z4noZfLaq6EXRSIrTMhwLWfq62xvGCfb6aCOd95fG8Kmhj1UshODAyez9cE7e1SGpjPrHtYopu2AYDaVbiawuob1BYdV2VeZ3Jt0u8zn5Um2pWh58EG7R3jUWGs3kMufRd4MfsLOA96yS5h7LN5DG94B4IDWJoZSEml0RRv1Rz1T0aA7lVs4kilHVq8xUuHcmDLDswM7oXTFuxY6Ps5ylOJGxoT28sNeZXD5GU0zHyh4TB3bnrDRMfyhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از جنگنده های سوخو ۳۵ روسی که بهم برخورد کردند.
🔴
یک خلبان کشته و خلبان دیگر زخمی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/146145" target="_blank">📅 22:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146144">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6864bbb8.mp4?token=MbK3whAzc5Sq5ArqeYsiftSDL5rF1iClPyLigSCvl2ITIx8PRR4ujEW2df6ktSZVygrj8U-ZQKmqDW0fW6vIvVXeJiYsraLfz-83M-0JZ02UM6E7j0Mz_ar52xMOz3w1ei22HttYxlUHSN2soqTxzkKJ-N4JOFCrD4PvWXikuPTpfn5jMQ4_0WnxFrQVPTX9k3xdzR0lyhMPlhHBH4eaS9WnO-nhneZqCZeY0ifuWTNo4utqhSczUeZzS4eVsEYiGjwAtpF1XEFhpWRe6koFl5LGSQ0fEQ0QaAgnKQUTJyKJket8nkzxTQjgrJXBduzm2qXMiBEtbv0wKM2G8bs2Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6864bbb8.mp4?token=MbK3whAzc5Sq5ArqeYsiftSDL5rF1iClPyLigSCvl2ITIx8PRR4ujEW2df6ktSZVygrj8U-ZQKmqDW0fW6vIvVXeJiYsraLfz-83M-0JZ02UM6E7j0Mz_ar52xMOz3w1ei22HttYxlUHSN2soqTxzkKJ-N4JOFCrD4PvWXikuPTpfn5jMQ4_0WnxFrQVPTX9k3xdzR0lyhMPlhHBH4eaS9WnO-nhneZqCZeY0ifuWTNo4utqhSczUeZzS4eVsEYiGjwAtpF1XEFhpWRe6koFl5LGSQ0fEQ0QaAgnKQUTJyKJket8nkzxTQjgrJXBduzm2qXMiBEtbv0wKM2G8bs2Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو رشت یه خانم به این شکل با ماشین زد به یه موتور سوار و عجیب تر اینکه موقع دور زدن یبار دیگه زیرش کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/146144" target="_blank">📅 22:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146143">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
گفت‌وگوی تلفنی ترامپ و نخست‌وزیر انگلیس درباره تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/146143" target="_blank">📅 22:24 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146142">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qvYlQnc34HQ_rRw2oVcbsE1KKlWSt0RKDm_Ehd1mzADTZ2tVfadKeMdaGi6AjRMu_DOlHwNYqbInrXSPV-FOfHCdbyR97zsP_ECE_PGhuiwm9AGzjM6kCuIjADcz6OzaLeH68u6p9WpvuLAWMgqShP3JVCaTJn0o35MpnNOls7RWeNs7ZgE8H7wg1CNTAnLHcge6HLNpeZUHkaDkFm2MDHUrit31oU_bpQI68QacrDVoBrJWu2fxx1dXM1uqUf2l8uV0SzEmjKUx77MXbtVch9xqJOAxUL2LxK31JUm7Zc126LIX3x5Fu27DuP7ATxagc9gZUWMqR_KWPqkcIQXgUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکر بزرگ قطری حامل LNG از مسیر تعیین شده توسط ایران عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/146142" target="_blank">📅 22:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146139">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c412317904.mp4?token=PQiIb2Xp37KPYEm32VGMCTJblrmSacJDfdEHeYtGRevRNzMS3x8nDBnt29sz3F5SMA9YljdaJXFbljskg8I_BR9nXONn1JZ44CXqCX-KYdptRl3notww8hH0O3aGxJBWEgc6zBRuv-0Of0AQhdgVb897_DcgfBKIdOyTSEWyidQYPU0Z_wCyRtErBac80Jax4LaYJRRqD3YOlny5yJ84cJYfLwITCcewwnHNmG-MaEzBwOuWQlsUSFOVku74dLDDxeShAgn9c8ijVuUg1BhTgDO3ThJevupZhOIoOt4tivCApVdpdPOzR4DcdijKRSHi0JP6MBKsmyIz1KbGnWVyO7X935yCjDfV1tZ4EqAEW-QT-ETsNW1dwYB6iGw6vYqdUrJ9AYl6yOgvP-APNVa581KNsjtd0mENIfRO60ficwYB1RmjrORpc1Qlm1o9T8byon1VnYsSzzlPZHJgY2OlH30znmfCChSCdOnBylcnYpoJuDYHqQCtlaEjVaaB4_ZAMqc9l6A4bZ2R2OxnOEDtySISTOVImmYQ-pLr1hC1IV_1k9ppsizWEipk90PcYY12VdBQOWWOOLnFnwcmmOc6ODxLwJy9u-0fNTQxlVZTro3qaUxVa6VjB5k_Khw9vMLy-lk0PguOMCxqoLJIi_0CfP4_o0_tOt9YWuBkTtVAExI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c412317904.mp4?token=PQiIb2Xp37KPYEm32VGMCTJblrmSacJDfdEHeYtGRevRNzMS3x8nDBnt29sz3F5SMA9YljdaJXFbljskg8I_BR9nXONn1JZ44CXqCX-KYdptRl3notww8hH0O3aGxJBWEgc6zBRuv-0Of0AQhdgVb897_DcgfBKIdOyTSEWyidQYPU0Z_wCyRtErBac80Jax4LaYJRRqD3YOlny5yJ84cJYfLwITCcewwnHNmG-MaEzBwOuWQlsUSFOVku74dLDDxeShAgn9c8ijVuUg1BhTgDO3ThJevupZhOIoOt4tivCApVdpdPOzR4DcdijKRSHi0JP6MBKsmyIz1KbGnWVyO7X935yCjDfV1tZ4EqAEW-QT-ETsNW1dwYB6iGw6vYqdUrJ9AYl6yOgvP-APNVa581KNsjtd0mENIfRO60ficwYB1RmjrORpc1Qlm1o9T8byon1VnYsSzzlPZHJgY2OlH30znmfCChSCdOnBylcnYpoJuDYHqQCtlaEjVaaB4_ZAMqc9l6A4bZ2R2OxnOEDtySISTOVImmYQ-pLr1hC1IV_1k9ppsizWEipk90PcYY12VdBQOWWOOLnFnwcmmOc6ODxLwJy9u-0fNTQxlVZTro3qaUxVa6VjB5k_Khw9vMLy-lk0PguOMCxqoLJIi_0CfP4_o0_tOt9YWuBkTtVAExI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بارش شدید باران در آستارا، املش و تالش
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/146139" target="_blank">📅 22:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146138">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
مدیر طرح CNG شرکت ملی پخش:
با استفاده از همه ظرفیت، هزینه سوخت خانوارهای پرمصرف سالانه تا ۵۰ میلیون تومان کم می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/146138" target="_blank">📅 22:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146137">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb225132d.mp4?token=YkhFd1YvNx_qwUslFCnCS2dbGE2B5nnGyscxYyNUxO7TSN1nraqQjJl4kumfJZ4MBexJ0e6C2fhtY_3zvfBQxeWCcJispkbx_ug55L7xquU8MshVWC8fcXEWLxhUX7AZZ7UfzKjFxPQfuD0KKIf7ix2JylArmfohsIO4UDFaeFkR8WxsP7nFiu97L6AAZQx392Oi0H1o23Czyv2QtW2QGGhcBQQVUQ0hnA76rZTmI5VxHxxpDGcNP5agnbyVd0ZU5OVFhz-UXRss0oBl9uc4-ADgpgMJgJMRUZV4hHs1xJ3rEw0MFG5onwS4S3b8TBRnI_DFId9Vb-rALi_3bv8x_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb225132d.mp4?token=YkhFd1YvNx_qwUslFCnCS2dbGE2B5nnGyscxYyNUxO7TSN1nraqQjJl4kumfJZ4MBexJ0e6C2fhtY_3zvfBQxeWCcJispkbx_ug55L7xquU8MshVWC8fcXEWLxhUX7AZZ7UfzKjFxPQfuD0KKIf7ix2JylArmfohsIO4UDFaeFkR8WxsP7nFiu97L6AAZQx392Oi0H1o23Czyv2QtW2QGGhcBQQVUQ0hnA76rZTmI5VxHxxpDGcNP5agnbyVd0ZU5OVFhz-UXRss0oBl9uc4-ADgpgMJgJMRUZV4hHs1xJ3rEw0MFG5onwS4S3b8TBRnI_DFId9Vb-rALi_3bv8x_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مصاحبه جدید صدا و سیما پس از گران شدن بنزین: یک لیتر بنزین کمتر مصرف کن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/146137" target="_blank">📅 22:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146136">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhGBwDFQRiNCDVhaJHngBxphB4-9fx7n3zbrjBewx9gj7HnTk996vkD1-VD1idrffFUT7H4XJ4ZE2Pa-W12ZV-ZUpk_458Q1iN9f5ZxZPNnt8q47ZCj6NSolS_w1VEr4QhHPBiAxTCLWM0FRgl338Rt-uUoFEVejglnHlKXStwAykBKvB0M6IW3wZamdtntN7avAjL6VfKJ59TMC4SZaVzLGZ-Gqjeur8UKbLKu2PRZG5FoaCZKiJlmmwHOd-oQaECzLEoZRmbTpGwpFXmnz6xgculgIZuUEzZNng8EUdzTbHpUkeafR8edLhQyv6LJXoGmxnHbzFmqGr88qwD2FYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون گزارش های اولیه از شلیک چندین موشک از جنوب ایران به سمت تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/146136" target="_blank">📅 21:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146135">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a30ef5442.mp4?token=BwvXyFKdpdBAV8dFFZuNLYlNgSjFud8JbhYyzZ98ubhsAAE89uvlgUQJGZrJjeqSFMCSP2cuBalNZ05lQScCmgAR1gWNlmcPWzdWxc1N25yJ9ckUYF-1QC8VkPJ97oBiaWPR4YivRGOKSDqVeT88ijxeVMLuKiCz3tPiNRcofUoLcoLxb7-e7rJ802BVyi4aehd2s1WTdFof8gWDwh11-mmUCTK7A5VPPRorspivbRXgsTF7e_nmgnJqkuwGGsaYRnlh30JtMWSLUdGYeMXQioHdiIbOnIY6Pxobl1k3XVs172w3Bx-8QWwsjCpb_vC3Rhx859ak5jlYSTnCVTsh1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a30ef5442.mp4?token=BwvXyFKdpdBAV8dFFZuNLYlNgSjFud8JbhYyzZ98ubhsAAE89uvlgUQJGZrJjeqSFMCSP2cuBalNZ05lQScCmgAR1gWNlmcPWzdWxc1N25yJ9ckUYF-1QC8VkPJ97oBiaWPR4YivRGOKSDqVeT88ijxeVMLuKiCz3tPiNRcofUoLcoLxb7-e7rJ802BVyi4aehd2s1WTdFof8gWDwh11-mmUCTK7A5VPPRorspivbRXgsTF7e_nmgnJqkuwGGsaYRnlh30JtMWSLUdGYeMXQioHdiIbOnIY6Pxobl1k3XVs172w3Bx-8QWwsjCpb_vC3Rhx859ak5jlYSTnCVTsh1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش ها از حمله اسرائیل به منطقه النبطیه الفوقا در جنوب لبنان گزارش می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/146135" target="_blank">📅 21:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146134">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
هواشناسی: شدت بارش‌های امروز و فردا منجر به صدور هشدار نارنجی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/146134" target="_blank">📅 21:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146133">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
هم اکنون گزارش های اولیه از شلیک چندین موشک از جنوب ایران به سمت تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/146133" target="_blank">📅 21:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146132">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
زلنسکی به اکسیوس: واشنگتن به دنبال کاهش تنش‌ها بین روسیه و اوکراین در طول زمستان و از سرگیری مذاکرات صلح است
🔴
احتمال برگزاری دور سه‌جانبه مذاکرات آمریکا، اوکراین و روسیه وجود دارد، اما هنوز تصمیمی در این مورد گرفته نشده است.
🔴
اوکراین تمام امتیازات ممکن را داده است و هر مسیر دیپلماتیکی مستلزم تضمین‌های امنیتی و حمایت اقتصادی است.
🔴
آنچه از دیدار ویتکوف و کوشنر فهمیدیم این است که پوتین آماده است تا در مورد ایده‌هایی برای پیشبرد مذاکرات بحث کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/146132" target="_blank">📅 21:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146131">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEFY63pQ0YX7jxUr7Eb0ND82jjvDVWxvzog6oRj0L3vTckshtdM6lwpZmx7EXjE9b7wJEE_Bd8noCY8Y5XAjrcDOX9vQITVDLtxrlvWEcTBlMFJpDlp6K_6hQXEMSv1GxguCp6E_LyrbZ-qAAZF3vvC8sTqFXzbSgyabO0r7UEW5WbEYsm3Ncha11Tzy4MwGnzetjSdQo7o7OoJUx2ozP034Ab53P1Puh-iCmQcenQJr0AEvN9c_l1R8bDpy2FaB9tsnjn96cDqeA60uRdxcq1HAq8KNStyQFmwuG696Xz-pdfKh53AzuKz7ztFaCy71c1MSFCBt03bm5nmRM81aHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : دیگر هیچ فروش محصولات شرکت بمباردیه در ایالات متحده مجاز نیست! محصولات آن‌ها به اندازه‌ای باکیفیت نیستند! بیش از 50 درصد درآمد آن‌ها از ایالات متحده به دست می‌آید. آن‌ها از خریداران آمریکایی، شرکت‌های آمریکایی، فرودگاه‌های آمریکایی و خدمات آمریکایی ارتزاق می‌کنند. در حالی که کانادا، بانک‌ها و شرکت‌های بزرگ آمریکایی را در سراسر ایالات متحده تحریم می‌کند.
🔴
آن‌ها حتی شرکت Gulfstream Aerospace را از انجام تجارت در کانادا منع کردند. این کاملاً ناعادلانه و غیرمنصفانه است! آن دوران به پایان رسیده است! اگر آن‌ها می‌خواهند از بازار ما استفاده کنند، باید در اینجا تولید کنند و از رفتار با آمریکا به عنوان یک "جعبه سپرده" دست بردارند.
🔴
محصولات آمریکایی را بخرید. با خطوط هوایی آمریکایی پرواز کنید. از مشروبات الکلی و نوشیدنی‌های آمریکایی لذت ببرید. در دریاچه آمریکا قایق‌سواری کنید. آمریکا اول!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/146131" target="_blank">📅 21:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146130">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
طبق گزارش رسانه های عربستان،
چندین قبیله بزرگ در شرق یمن برای جنگ با حوثی ها در حال بسیج نیرو های خود می‌باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/146130" target="_blank">📅 21:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146129">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ne9Zx-boMBWuo4EIfeCLxNXpJnUaBfz9gZTtCcr1u-Rq9920AkXPalyX5jtch0lKmIFzSbWmyJtrQ-TkeQo_bQ2Keu9tJ0jPi6hyAswgl1AQB8O_jPE1YzmyTODEjfOPakNfw5e4QzV5yMOtLCiFIlyOROrV7BQB-NJNLekvxH_Qp8RQuXbEuQRYQyTW0VAm0JZczhTtuj3v_o4SKNHIgsGN_dXWmIzXokLgOcOEL9PKmJoHdvZn8fpum9Bkg7zEULQdH0G_pEMBbRo3QtU2SFNYwLVowONlI2ogAaNqWIU4b_i5sbAhQ8lfR87qc33Dn4169UwQBEzllvqvyAPIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
این پیام میتونه زندگیتو تغییر بده !
می‌خوای از ترید سود بگیری؟ بدون اخبار و تحلیل درست، فقط داری شانسی بازی می‌کنی!
💎
ما اینجاییم که بهت بگیم:
💰
آموزش گرفتن درآمد دلاری بدون ریسک و سود تضمینی !
اگه می‌خوای به درامد دلاری ثابت برسی جات اینجاست
✅
👇
https://t.me/+fDXpi2Dbi185ZjRk
https://t.me/+fDXpi2Dbi185ZjRk</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/146129" target="_blank">📅 21:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146128">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
بسیج عمومی در سراسر یمن در حال وقوع است، یمن بار دیگر پس از 5 سال درگیر یک جنگ داخلی تمام‌عیار شده است و نبردهای متعددی در تقریباً تمام جبهه‌های یمن در جریان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/146128" target="_blank">📅 21:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146127">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
آنکارا: اسرائیل تفاهم‌نامه اسلام‌آباد را خراب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/146127" target="_blank">📅 21:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146126">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyV9pfWliZx7E4c5mqU-ZgPno1Ge1o-W2UB4kbKtlp5Ee-mw08YhZke5nqKUByoZ-36FyDAZF1A90nQIjnzm9rRIsH4N-itTDsW0BSjKMrdt7DMJMiTCuwvNotw3DxZVEvSt23IFExi0lYZ2Wu47zWur5CAFC5oUX5niUsnMlK0m98P_WLDMfIrw2MhAV31BX_mFfPzS7fqjEcspWMO0HlUZhUI6-mMqDFu2D3tiP-lovk4iEsHzbrD9Kk5X4YcB6p2btbCJFHteRsHphR9tAWHdpWDcMDREov3FKXAzmswtEebuGHx3iKGY2WSyNxW0wcEpirQG0h0cc_U2Jkl9Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه تلگراف انگلیس: رئیس جمهوری سابق ایران ( روحانی) خواهان برگزاری رفراندوم برای پایان جنگ شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/146126" target="_blank">📅 20:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146125">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFzRcqT-zEcDB0WRf4c8ii57m4X93qOG5t0I6EUAw_HrYRsA9aJ0-MZn-PFjgKZdbqjJqx9YotDEAXGvu3z7iBX2hg2RVMCYQj-ynIq3a9fz0cpGsocNbu0BVF7HnVUqGn6sGhRqTTiSWbWCGQY3NJ28I8rAQw8a6VocflJVb4gmNMGW-TwXYJMuknHThiULehLXKPVcVUK6vzQ5IFg48Dt7wUB4FQVphqgYI1zzqKSiSagsI9MZqie5FRQDm5pKA2BbLgGQ7u-wuQKZ_npOWGWYK1y2jzbyWDsFrG0DVfIBNoL9TZSDYUhRMQM-r7wRs-gIyxWuYlYOlkYFFgVm0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۴ ماه محرومیت و جریمه ۲ میلیاردی برای خداداد عزیزی
🔴
عالیشاه هم ۴ جلسه محروم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/146125" target="_blank">📅 20:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146124">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
پرواز چهار فروند بمب‌افکن استراتژیک Tu-160M از پایگاه هوایی اوکرایینکا در روسیه. انتظار می‌رود این بمب‌افکن‌ها در ساعات آینده، موشک‌های کروز Kh-101 را علیه اوکراین شلیک کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/146124" target="_blank">📅 20:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146123">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه قطر در گفت‌وگو با CNN: ما نمی‌خواهیم درگیری را متوقف کنیم و پس از ماه‌ها دوباره به آن برگردیم.
🔴
اولویت ما باز کردن تنگه هرمز و کاهش فشار اقتصادی بر مردم منطقه از جمله ایران است.
🔴
ما در تلاشیم تا از تشدید تنش، حملات موشکی به مناطق مسکونی در خلیج فارس و حملات به ایران جلوگیری کنیم.
🔴
ما به اقدام جمعی منطقه‌ای برای آغاز گفتگوی فراگیر که شامل همه باشد، نیاز داریم.
🔴
تحریم‌ها ابزاری دیپلماتیک هستند که مدتی است در منطقه مورد استفاده قرار گرفته‌اند، اما به نتایج مطلوب نرسیده‌اند.
🔴
ما چندین ایده ارائه داده‌ایم که برخی از آنها شامل یک یادداشت تفاهم است و ما همچنان در حال توسعه راه‌حل‌های بیشتر هستیم.
🔴
تاکتیک‌های فشاری که توسط هر دو طرف به کار گرفته می‌شود، در نهایت به بندهایی در توافق تبدیل خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/146123" target="_blank">📅 20:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146122">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2TnVQcvlAPKUnFTaA51Mods9GruUArzIyM4iUd8Pi-AQC2dFUrchnwBU9eXMqynLGzFezSm-fU0NCRXMs-J-kSJS6uTYnYWESgUqTBQAshkiWtqHVfO-c0fIq7cFK0iPV3XlODkJv03NglKc7MOrjwPJsW-R4cMdmziLJuT3cCj8uT6huTSnwg7-g5FEJrEqXcTCbDVBdDCfwl5vI37cUcMoeRKSteE8jYkUAAk1fr2a965x7NZ0lI6IwuhobbvyckYmAGTEVFIg0biuoPh_JCBIFdSRN2NjmEA4FoHTZG6BjuO15x990bBMijLHeAmzGAWS-6cl4VDGcwFcRlqUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چند روز پیش از رونمایی طرح اقتصادی «فشار حداکثری» علیه ایران، وزیر خزانه‌داری آمریکا در یک نشست خصوصی مدعی شده بود پس از اجرای این طرح، ارزش ریال در برابر دلار در تهران به‌سرعت دو برابر خواهد شد.
🔴
مرندی این ادعا را تکرار وعده‌های قبلی آمریکا دانست و به وعده «سقوط تهران در ۱۰۰ ساعت» اشاره کرد.
🔴
وی تأکید کرد این نوع پیش‌بینی‌ها همچنان ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/146122" target="_blank">📅 20:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146121">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
اتحادیه اروپا و گرینلند با امضای توافقنامه‌ای جدید، بسته سرمایه‌گذاری ۲۰۰ میلیون یورویی برای سال‌های ۲۰۲۶ و ۲۰۲۷ را نهایی کردند؛ توافقی که در بحبوحه ادعاهای دوباره دولت آمریکا درباره الحاق گرینلند، بر تقویت روابط اقتصادی، مقابله با تهدیدهای ترکیبی و افزایش تاب‌آوری منطقه قطب شمال متمرکز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/146121" target="_blank">📅 20:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146120">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
گروسی: اینکه ایران می گوید سایت‌های اصلی هسته‌ای برای بازدید بیش از حد ناامن هستند را مانع نمی‌بینیم
🔴
همچنان هیچ گزارشی از سوی ایران درباره این سایت‌ها دریافت نکرده‌ایم؛ این گزارش باید شامل هرگونه تغییر در موجودی مواد هسته‌ای و وضعیت دسترسی‌پذیری سایت‌ها می‌بود
🔴
به ما گفته می‌شود که تا زمانی که در مذاکرات گسترده‌تری که در حال انجام آن هستند به توافقی دست پیدا نکنند، همکاری نخواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/146120" target="_blank">📅 20:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146119">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4jf-rhlCRkdGS4ZTjvEYFqHIP1mT394AsPvpy8tFDZ2Z0xnfC4Y-Zi_0ej8pmM79rnPD06zYYBBwNV37mYGRoaBw3XLKtSFJZGUBN0iB4nSljntdSJQiWSEMkDVuTYqGgGz5AeiND_mUHXXfX_S3nxosK5IHw3-7dJn7vNT4HuhHG2ovgGjsiy2GuvQzezJQ_TYiQMejrB_q-NBrJ_4xdK_mEkeQxVC-ZkdRHuoGy5PKF5kRcjld1K_UXMr4FsG0-Cv-SuE8kOIxfU62ZBwiLM3OtcfXSpsdHPndlzrTSx50kQxEHgq5UADd62ZWv-jQfP2_Mb2tK1kEKAH7GSuNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال تلگرامی «جنگنده بمب‌افکن» که ارتباط نزدیکی با نیروی هوایی و فضایی روسیه دارد، گزارش می‌دهد که دو جنگنده سوخو-۳۵اس در منطقه کورسک روسیه با یکدیگر برخورد کرده‌اند.
🔴
این کانال اشاره کرد که علت این حادثه در حال بررسی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/146119" target="_blank">📅 20:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146118">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8c7c5ba81a.mp4?token=QlpFDQw6kY0QZ2FZHIy3Zuv1sRO74h456YYwx1v4S4XBOuUuZIwe_PG-sRzrf0zQaNjCTaBGN55qBeXdQtJtOXFcVWmb20CITJvgmdG7fPWdXDt94VE7lGodMeEeYWEjVhgqFqczQWG0ENVWEnNGetiL2nUJbz8ySB8PVJCk0Z2AP9vKG--YzGdQAufRInfmzJmrMxWzHsd5VvjEpubUp4_GfWiYBmeM1JS_Lk_2nkniNDvG8YmOvU-R2eioHOo5hhTr5wqoLbv5o5tI5pElZCeCAvlIAXAxozIBux6ZsG3Y2dD1RR20jPaK8KgiUIfppr9wREBwD43s5guB7J9sNw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8c7c5ba81a.mp4?token=QlpFDQw6kY0QZ2FZHIy3Zuv1sRO74h456YYwx1v4S4XBOuUuZIwe_PG-sRzrf0zQaNjCTaBGN55qBeXdQtJtOXFcVWmb20CITJvgmdG7fPWdXDt94VE7lGodMeEeYWEjVhgqFqczQWG0ENVWEnNGetiL2nUJbz8ySB8PVJCk0Z2AP9vKG--YzGdQAufRInfmzJmrMxWzHsd5VvjEpubUp4_GfWiYBmeM1JS_Lk_2nkniNDvG8YmOvU-R2eioHOo5hhTr5wqoLbv5o5tI5pElZCeCAvlIAXAxozIBux6ZsG3Y2dD1RR20jPaK8KgiUIfppr9wREBwD43s5guB7J9sNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرکات زمینی نیروهای ائتلاف در استان الجوف، در میان گزارش‌هایی از یک تهاجم زمینی در این منطقه
🔴
همچنین یک حمله هوایی علیه زندانی که توسط انصارالله اداره می‌شد در الجوف انجام شد که منجر به محبوس شدن ده‌ها نفر گردید
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/146118" target="_blank">📅 20:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146117">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
مقام ارشد آمریکایی: تنگه هرمز کاملاً باز است و توسط نیروی دریایی آمریکا کنترل می‌شود
🔴
به لطف محاصره تاریخی و موفق، هیچ چیزی به ایران نمی‌رسد و تنگه هرمز برای همه باز است.
🔴
روزانه میلیون‌ها بشکه نفت از تنگه هرمز عبور می‌کند.
🔴
ایران از طریق یک فرآیند اقتصادی و موفق‌ترین محاصره تاریخ، از نظر اقتصادی در تنگنا قرار گرفته است.
🔴
از پاکسازی هرمز از مین‌ها، حمل و نقل به بنادر غیر ایرانی و از مبدا آنها به طور قابل توجهی افزایش خواهد یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/146117" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146116">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARIvw42AZounEtFAz9xYMi57bfY3CJpJObFn71pBKfg51A9hOL30kNWT-6i4ymGS5oMkLqAREE4LR_UyDF2TYS3xhq_dE0J0JfVyC5sy8WuOKbXalWDp34Dv4nx0ZrTX_-23e28qMbFYXzKdWF3OmVeu-XS1Z4Zu63jx3VzCgMg_3UzryjYBtpBAKF8F8nnVyhbPQfCMVJpH5bLAkB2VCfDtX_fikFO1ztenIkXKVMATws4n2pHcXlYr3E-UN03A6AODKO-xIijJVp8P0ucvs9B7DytMDIwU8hqo6ePFTF9BPrB6zyGJFNETACZPKaH8trpKAonxnRxlzpmPHGgFDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نورالدین الدغیر، خبرنگار الجزیره:
با هر تنشی، دیپلماسی دوباره به جریان می‌افتد
🔴
یک هیات قطری در تهران حضور داشت و پیشنهادهایی را مطرح کرد
🔴
هدف پیشنهادها کاهش تنش از آب‌های خلیج فارس تا دریای عمان بود
🔴
بررسی امکان بازگشت تهران و واشنگتن به میز مذاکره از دیگر اهداف این پیشنهادها بود
🔴
در دیپلماسی، همه پیشنهادها از سوی طرف‌های ذی‌ربط با نگاه مثبت مورد بررسی قرار می‌گیرند
🔴
وزارت امور خارجه ایران نیز سفر این هیات را خوب توصیف کرد
🔴
قطر در هفته‌های اخیر نیز بر کاهش تنش و بازگشت به میز مذاکرات تأکید کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/146116" target="_blank">📅 19:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146115">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
چند ساعت پیش، نیروی هوایی سلطنتی عربستان سعودی حملاتی را با بمب‌های هواپیما علیه مواضع جنبش انصارالله در مناطق جنوبی استان مأرب، که تحت کنترل این جنبش در یمن قرار دارد، انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/146115" target="_blank">📅 19:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146114">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0de73320.mp4?token=c3sj9rfnyED8hWGpeNMwsxOITN1ouCcwz9SY8QVtnifkViMDaWRRBH8yrxzdl98GJHh-Upy6dAJLGIb4_jGlpbM_EQ82hzx8OGU7UkQACtUTmyHx_FuY3c6VOVJ61WEoC9AMldPAZSwtITkVogz1dZRdDD0UED0ZRm228v-9TnMg4pZmWr7rNB8egkIWbJCYRaDxM_q4pwmbzBGJQAHggvI6VAEeUpRz8hU2lWP1b0MB7zfvcPtd78JA918-EOv_I5CrRMftr57fyJ7-3aX0gzqEBFMvwzxMytCZeGVvEjhM2TawVvU0RKF1aq2l8KZ-HGhDGj6Ls_LKHuWcnW-9xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0de73320.mp4?token=c3sj9rfnyED8hWGpeNMwsxOITN1ouCcwz9SY8QVtnifkViMDaWRRBH8yrxzdl98GJHh-Upy6dAJLGIb4_jGlpbM_EQ82hzx8OGU7UkQACtUTmyHx_FuY3c6VOVJ61WEoC9AMldPAZSwtITkVogz1dZRdDD0UED0ZRm228v-9TnMg4pZmWr7rNB8egkIWbJCYRaDxM_q4pwmbzBGJQAHggvI6VAEeUpRz8hU2lWP1b0MB7zfvcPtd78JA918-EOv_I5CrRMftr57fyJ7-3aX0gzqEBFMvwzxMytCZeGVvEjhM2TawVvU0RKF1aq2l8KZ-HGhDGj6Ls_LKHuWcnW-9xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پهپاد اوکراینی در طول شب، بمب‌افکن تاکتیکی سو-۲۴ روسیه را در پایگاه هوایی ساکی در کریمه با موفقیت هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/146114" target="_blank">📅 19:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146113">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0536ca7f15.mp4?token=ldEuot6jOtb0lcnKWy4clrzfd1MeuzngSE1o0V7b7ZbmbPf0sRN_yxnKqfYsSsi-NnVovGCT0t-07cAnVDIuBlMo3vm53pVo_5036iVVsJkucFMHUnPu1lNmBSGehnOt8Wzj9DeAn9xa5fuI80uT28LMrV9UBUfqoJB2-DuEb2Kvv98E4GctZYszir3rDu3bClLoUVi-yMCF394yGGtMZnBKmSFALTnXWlJ8GixNQylekOlc-8pC9DKb7GNGIxmDkqj-6iqJrsdNHnkU9RBmBIrBDLhKQQEWyeUSuytc8a6SdZPePA1jJE1PRK4_NGnCtAMwT-XzZ3N4wIvG6USzvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0536ca7f15.mp4?token=ldEuot6jOtb0lcnKWy4clrzfd1MeuzngSE1o0V7b7ZbmbPf0sRN_yxnKqfYsSsi-NnVovGCT0t-07cAnVDIuBlMo3vm53pVo_5036iVVsJkucFMHUnPu1lNmBSGehnOt8Wzj9DeAn9xa5fuI80uT28LMrV9UBUfqoJB2-DuEb2Kvv98E4GctZYszir3rDu3bClLoUVi-yMCF394yGGtMZnBKmSFALTnXWlJ8GixNQylekOlc-8pC9DKb7GNGIxmDkqj-6iqJrsdNHnkU9RBmBIrBDLhKQQEWyeUSuytc8a6SdZPePA1jJE1PRK4_NGnCtAMwT-XzZ3N4wIvG6USzvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آبفا، تهران را در آستانه زلزله قرار داد!
🔴
استاد پژوهشگاه زلزله شناسی: در ۳ دهه ۴۰ میلیارد متر مکعب آب زیرزمینی را بیرون کشیده‌اند.
🔴
فرونشست زمین در تهران محسوس است؛ روی گسل‌ها تغییرات رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/146113" target="_blank">📅 19:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146112">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
کمیسر حقوق بشر سازمان ملل:
هوش مصنوعی می‌تواند خطری «وجودی» برای بشریت ایجاد کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/146112" target="_blank">📅 19:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146111">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
اردوغان: اسرائیل محور شرارت است و باید متوقف شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/146111" target="_blank">📅 19:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146110">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVYl2OMfA07bi65KoKBCd8Qo6uYDPZz4xO5TsQmxBpD-G6Ajjlg1ixwUN4a744TSpZGz5a3VaACv1ov03bRBYlaD_p4Vdfmw3qaOoD6R8OvCLSYnGv1r2ncNv9dfF0qx8o6JFyiDUyOYa9xjXL_Ae3ciPwJhTbs-bwQn78Hv5aTjJ3Z4l7LPLNZw-xPvVorEnLpSenOdZwHYFkxNMVJ0zi-1U2ZlMU_zls8L_YcdgjCTVNHS3OHoIp7W3SpTY2c4O4WvCDG90h_AaqHx4eMXRBCy9UavONBIDBJ22e0xru2MIlkTJ0VV9ZFT2r5s5u5lLWy4QBnPR2TAqH69GfaNig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت ۹۸ دلاری شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/146110" target="_blank">📅 19:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146109">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
فواد ایزدی: اگر ایران آب شیرین کن های منطقه را هدف قرار دهد، چین از تهران تشکر خواهد کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/146109" target="_blank">📅 19:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146108">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlTjrqMO-13TRWIz8hO9ZfZ4mtEILiKwtJzG1-fQv22rPoGs7RQSDJUFFoUNEorYmB1Ylmwh66k_2L30jJhVbSBwi6HqJLnHayJyPBIQ3-jUaoeIWncA9uvnp8Rll8czOcp-uqeC7oQJ3SaC3ZX6LKYpjQMPb3vefzTtJluAoPxlaJ-AtVdK6YtwvM5JGi2FflzIJFiJkw-lNymPDbuu1ppKiCcSuI5RQt5Nx5ka6bCaseEcn_5jbPda4MVyn03GH1KOBzaP71zIo9X7cm56Cr0kL-2lFFxtAw7BfXTdAjmiUBEsJOqGqFWw3FmzCZRbeCrJ1kuIJL2f_DiDAfox-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ خبری از وال استریت ژورنال درمورد اظهارات پزشکیان مبنی بر لزوم پایان جنگ را به اشتراک گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/146108" target="_blank">📅 19:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146107">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzNVw6GAJWzNJdiirxjR3jOhiuw37yaTSfY3-U3ThNAY6trSeuj5jKdWASnt7D7_B0LyNwCJH-dLpfI0zn2gexAhIqEfUb6d7w7qyiGSz32vRfO9HWrPzUOiVmgAZF3XhOoyfiVuVm0UxGQ3u3EGlw4r6KSD0NOU4VwNeizpOjFmdT837xE6E4ozp9v4IZQNIfxDFVhpadVy2sOy4CYXKW9w3olirzbz5Ne9OmbJoCdJbx3XgCadRo4FWJmP0UcJEkMAatrnIWuCTo97doUxuZK0qtng3rRi66mS-WlFqBrWCbhfVh6ZHnNQ4gfoFzXFfTl5392h7AEVvV9gR6xLgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/146107" target="_blank">📅 18:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146106">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab852706fc.mp4?token=dzC1fI0vSU9We6EIktrp1O9p2PHmr0xugUwT3pGAOhNPsAn2ykrezimmPJLzQFkvIxtWnc7FCRmSCX190A2NONQC_xqlyNfzpiFpUO3NVV6hzrpNKikFUk3xLOX-ZVAZVb6mw0Kq048Ja5CZaQueMhD4DIr1oiqxcVKsc64TkRtihHNjXl34Q2H2mDzJdSjWqIutLb-MgcyBg3Ace02ovqfxupi34hZnZpDuOn8jZV2TEtT6n6tVngHjzKcfxenS51hnJL3nisdbwPBDFAYSqv2knsA172QqJIaGaymejMiqS8Et4fvNQGNdaD8CuZJM7yMvDIxRUxYvaMlKgpl-aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab852706fc.mp4?token=dzC1fI0vSU9We6EIktrp1O9p2PHmr0xugUwT3pGAOhNPsAn2ykrezimmPJLzQFkvIxtWnc7FCRmSCX190A2NONQC_xqlyNfzpiFpUO3NVV6hzrpNKikFUk3xLOX-ZVAZVb6mw0Kq048Ja5CZaQueMhD4DIr1oiqxcVKsc64TkRtihHNjXl34Q2H2mDzJdSjWqIutLb-MgcyBg3Ace02ovqfxupi34hZnZpDuOn8jZV2TEtT6n6tVngHjzKcfxenS51hnJL3nisdbwPBDFAYSqv2knsA172QqJIaGaymejMiqS8Et4fvNQGNdaD8CuZJM7yMvDIxRUxYvaMlKgpl-aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیروز یه خبرنگار لبنانی داشت از شهر " نبطیه " لبنان گزارش تهیه میکرد که همون لحظه اسرائیل بیخ گوشش حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/146106" target="_blank">📅 18:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146105">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ: در انتخابات میان دوره ای به پیروزی قاطع دست خواهیم یافت و آمریکا را نجات خواهیم داد‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/146105" target="_blank">📅 18:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146104">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4221662e8f.mp4?token=dHlOb57aicHW5A64k97Zei-2IxqQ_bnuPR74fC8uBduOH7FrB3Z0dy2y1ATkrUPHxYMEPx5ZsU451DKbqW7kDuCi0QGGfM6d4j-_ylK6RqxdQj04sgU9UUZ90IWSy6oJ6VS0QTD9IIVf3PA8FoaJS1dpx-zJJ8KJitx89QBi0EhCp9xiPYs8JFCQB0eNtC5_aAG3z78pVPjrNh4I6pe1VsEqD56ZsmQfMf6YcN-m_GSPOjT0Yls0M0cLhLm7PuIwTHLzFmx3WDDMoGz2m5xA1fcJoH9zxUBfRJdESZlGHg7ArPRqLMhp7djQfq7iQEvdMR41PsE_6E-H6Ktc_mmwebr2RKffON0A4wXxKOkGcBJr3isp3raYIB3K73yO42cYntwTzcg-Kc9RyxIJ29QBZzvSH1FEuShnhDtk47x5tkk97-BPsgu0nwbNTKUTURuR4c0XsOmrtbeufMWuK_7BR74wR8SBtGDhXtUJqcRh-EV_HdzIfd7I0LR-RD8UPdRD9Podbzd2KUEtm3Yxkr6mka7o_LuBPedz-1xMyHCEI-rcqpNBsuWcR7k4zwMVf2OyBAgm1eccFkBjU7QMy6Qw7ydfzv9bBDgqb2KaskIwzO6vj8j2Zl0Q9rOsdP4jgETDDm9uIQzgr0Gkd1FExFbpsy-fbnhpOOgmXBZsxcfWw9k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4221662e8f.mp4?token=dHlOb57aicHW5A64k97Zei-2IxqQ_bnuPR74fC8uBduOH7FrB3Z0dy2y1ATkrUPHxYMEPx5ZsU451DKbqW7kDuCi0QGGfM6d4j-_ylK6RqxdQj04sgU9UUZ90IWSy6oJ6VS0QTD9IIVf3PA8FoaJS1dpx-zJJ8KJitx89QBi0EhCp9xiPYs8JFCQB0eNtC5_aAG3z78pVPjrNh4I6pe1VsEqD56ZsmQfMf6YcN-m_GSPOjT0Yls0M0cLhLm7PuIwTHLzFmx3WDDMoGz2m5xA1fcJoH9zxUBfRJdESZlGHg7ArPRqLMhp7djQfq7iQEvdMR41PsE_6E-H6Ktc_mmwebr2RKffON0A4wXxKOkGcBJr3isp3raYIB3K73yO42cYntwTzcg-Kc9RyxIJ29QBZzvSH1FEuShnhDtk47x5tkk97-BPsgu0nwbNTKUTURuR4c0XsOmrtbeufMWuK_7BR74wR8SBtGDhXtUJqcRh-EV_HdzIfd7I0LR-RD8UPdRD9Podbzd2KUEtm3Yxkr6mka7o_LuBPedz-1xMyHCEI-rcqpNBsuWcR7k4zwMVf2OyBAgm1eccFkBjU7QMy6Qw7ydfzv9bBDgqb2KaskIwzO6vj8j2Zl0Q9rOsdP4jgETDDm9uIQzgr0Gkd1FExFbpsy-fbnhpOOgmXBZsxcfWw9k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رقص و پایکوبی سربازان آمریکایی در یک کلوب شبانه در پاتایای تایلند
🔴
تفنگداران و ملوانان ناو آبراهام لینکلن، چند روزی در تایلند مشغول استراحت بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/146104" target="_blank">📅 18:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146103">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وزیر دفاع سابق آمریکا:
جنگ با ایران حداقل 6 ماه دیگر ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/146103" target="_blank">📅 18:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146102">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
موشک‌های بالستیک حوثی (انصارالله) به کامیون‌های سعودی با تجهیزات نظامی برای دولت یمن در اردوگاه الوادیه در منطقه حضرموت نزدیک مرز با استان نجران سعودی هدف قرار گرفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/146102" target="_blank">📅 17:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146101">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEo_q9gAxYu85lsq6h-ELfDEQ0QO1AtBk2Ewysr279UciqDdKdZkvIpZw-xGQVmxYMOrOxG_jcbOU4k3cHaEbTCvQaR6_8U4lMS3EVfqvdLsQ7MIqVfFFR4C6M0iKumEUUSRWAZlzmN7VaJe36_iKM6YB1aMzML0XUc18xemgVkzn-SfzzO26zcesZAzkmnPoNv3v4MhtQDtsB40bME7AT_RyeIjTZb9nerQTftil0zQcdOVO4-EMZiuvUZR8vJzsuo3D2KQkHq8qN-KWV064iRIOCUJssRkNxjts1BWsEYX6cvREm1w4wuRMvOgU8Q4t2req_iDePSNRMi-UH2R1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت محسن رضایی:
دیگه اون پسر مهربونه نیست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/146101" target="_blank">📅 17:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146100">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF): در پاسخ به پرتاب دو پهپاد انفجاری به سمت سربازان ارتش اسرائیل در منطقه امنیتی: ارتش اسرائیل به تأسیسات تروریستی حزب‌الله در جنوب لبنان حمله کرد
در طول شب (دوشنبه)، تروریست‌های حزب‌الله دو پهپاد انفجاری را به سمت سربازان ارتش اسرائیل که در منطقه تپه علی‌التحریر در منطقه امنیتی جنوب لبنان فعالیت می‌کردند، پرتاب کردند. هیچ زخمی‌ای در ارتش اسرائیل گزارش نشد.
بلافاصله پس از آن، ارتش اسرائیل به چندین تأسیسات تروریستی حزب‌الله در سراسر جنوب لبنان، از جمله یک انبار سلاح، حمله کرد. علاوه بر این، ارتش اسرائیل به چندین تروریست که شناسایی شده بودند و در حال انتقال سلاح در منطقه کفر رمان بودند، حمله کرد تا تهدیدی که برای سربازان ارتش اسرائیل ایجاد می‌کردند را از بین ببرد.
پیش از حملات، اقداماتی برای کاهش آسیب به افراد بی‌گناه انجام شد، از جمله استفاده از مهمات دقیق و پایش هوایی. ادعای اینکه چندین فرد بی‌گناه در نتیجه این حملات آسیب دیده‌اند، در حال بررسی است.
علاوه بر این، پس از پرتاب پهپادهای انفجاری دیروز (یکشنبه)، ارتش اسرائیل در منطقه نبطیه حمله کرد و چندین تروریست حزب‌الله را از بین برد.
ارتش اسرائیل اجازه نخواهد داد که سازمان تروریستی حزب‌الله به شهروندان اسرائیلی یا سربازان ارتش اسرائیل آسیب برساند و برای از بین بردن تهدیدات ادامه عملیات خواهد داد، در حالی که به توافق آتش‌بس پایبند باقی می‌ماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/146100" target="_blank">📅 17:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146099">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
اژه‌ای:هرکی صداش دربیاد جرمه
🔴
هرکی خلاف وحدت(ما) حرف بزنه جرمه
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/146099" target="_blank">📅 17:24 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146098">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1b21e927.mp4?token=lSO7-lF12xshwUKYJIRmi73B5QRiBl4MXQIt4seNyyjEVhBuvc8F_GewMBiCUAKwWOCdJqzZPVst4yKan6M73crZily9U_hUsn6mjGibgKZaMA1al04sasxKoQ1oA-jwFv_7t7Ew7j34j6nnRiPjPYOXmF5I-y3epGN6NZiYx8Ud1ZGelvgtMhs_7m1SIl1j-ePAOVWc2ASC8gpt4gYc6sSItc42qIPzNbr1HUFoXFKfkjYacndAkeXVvM1XI6PQB3QGRDy3SAI3sWDEZ8picx6t-QKJpzn-UM0LUdni4eUoIAXgr7JV6TZvbN2gM3tcRUYPZRxf5EwgPSTh13OH5nW3ZmeD7z0tPyvFFzmIcaPfrp9UGMEPvtcQrNptQlfric5phrkAUG-388xlqVuP64CpBHuJkZfyqmddwscXW4KYrTg3aB1zDQzWhBTpLSwloHeGwYIdDBk-FwhwOmcN6QvMGLK7VED0IfzWoJi6LKrEiSEp-nKHMqD1KKBNWxG0zoyC9Q5yN7SyoZ1GtqVbWHA866gx9Ni4rHsa-SRZasusS0hKChtZu7hUPy9fJk-GV0Dlnrp8XQtabgU5Tg2iRLlXC3_V6YcsWa60-iKXA7TnxvZa-84Gd4IqjePuiWA4YUsP0lPhiJsklNoLHEoxVeJklNxpksLDKh319J61_x0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1b21e927.mp4?token=lSO7-lF12xshwUKYJIRmi73B5QRiBl4MXQIt4seNyyjEVhBuvc8F_GewMBiCUAKwWOCdJqzZPVst4yKan6M73crZily9U_hUsn6mjGibgKZaMA1al04sasxKoQ1oA-jwFv_7t7Ew7j34j6nnRiPjPYOXmF5I-y3epGN6NZiYx8Ud1ZGelvgtMhs_7m1SIl1j-ePAOVWc2ASC8gpt4gYc6sSItc42qIPzNbr1HUFoXFKfkjYacndAkeXVvM1XI6PQB3QGRDy3SAI3sWDEZ8picx6t-QKJpzn-UM0LUdni4eUoIAXgr7JV6TZvbN2gM3tcRUYPZRxf5EwgPSTh13OH5nW3ZmeD7z0tPyvFFzmIcaPfrp9UGMEPvtcQrNptQlfric5phrkAUG-388xlqVuP64CpBHuJkZfyqmddwscXW4KYrTg3aB1zDQzWhBTpLSwloHeGwYIdDBk-FwhwOmcN6QvMGLK7VED0IfzWoJi6LKrEiSEp-nKHMqD1KKBNWxG0zoyC9Q5yN7SyoZ1GtqVbWHA866gx9Ni4rHsa-SRZasusS0hKChtZu7hUPy9fJk-GV0Dlnrp8XQtabgU5Tg2iRLlXC3_V6YcsWa60-iKXA7TnxvZa-84Gd4IqjePuiWA4YUsP0lPhiJsklNoLHEoxVeJklNxpksLDKh319J61_x0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو کرج دوتا از والدینی که اومده بودن مدرسه دعواشون میشه؛ یکیشون اون یکیو هل میده سرش میخوره زمین و متاسفانه میمیره...
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/146098" target="_blank">📅 17:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146097">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه قطر: جنگ ایران نشان داد که کشورهای عربی خلیج فارس نباید برای امنیت خود فقط به همکاری استراتژیک با ایالات متحده متکی باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/146097" target="_blank">📅 16:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146096">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
روزنامه هآرتص : ارزیابی اطلاعات ارتش اسرائیل نشان می‌دهد احتمال دارد ایران، در سایه فشارهای دو چندانی که بر این کشور وارد می‌شود، تصمیم به تشدید رویارویی با اسرائیل بگیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/146096" target="_blank">📅 16:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146095">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
نفت برنت در پی تشدید دوباره درگیری‌های ایران و آمریکا طی یک هفته بیش از ۱۰ درصد گران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/146095" target="_blank">📅 16:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146094">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
نفتالی بنت، نخست‌وزیر پیشین اسرائیل، درباره نتانیاهو: در حالی که نتانیاهو بخش‌هایی از سرزمین اسرائیل — ۱۳ درصد از کرانه باختری — را واگذار کرد، من یک سانتی‌متر زمین را واگذار نکردم.
🔴
در حالی که نتانیاهو به بایدن قول داد کنسولگری فلسطین را در اورشلیم تأسیس کند، من امتناع کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/146094" target="_blank">📅 16:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146093">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqWtGqN9iLd8N4lk7kjk-PZyBwfZ-b2jDjXrCpif9N4FNGNQnOqNLhN24Jc-m73bLXQnJf-rP8FgXEnijFKUZV6riTbPN8V-s7Hkz72nusxM6UFjsEV4MZIjLG5r3GYhyp1_jWmkjppa4As0CuL57c7enDgpAOZcG6kS5HGwN7kkfUtwRO5UfbZvG76_oLv3PMma2wgAq9wqnBhSmE-UoFAaX-kHaZDjpPiXGKdxYfVFqhdFTq-9YypwY03W6QOM53Jb5Dfij1I5pi4whEQBYNKa84ArVjrDtVDBlEpT7F3yQuH8JBDManOd-oPl6IExd2dMJS_jTwisC8o51Hl8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت ایران در غنا با انتشار نقشه آمریکا با طرح " بته جقه" ایرانی نوشت: نکته جالبی در حمله به ایران وجود دارد: دیر یا زود، فرهنگ ایرانی شروع به رخنه در وجودتان می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/146093" target="_blank">📅 16:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146092">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBwtBT1cq6x_KeMEZvqhsB2Ys4skSu7S_D8i9UOGSYle_9Twr7HBBkJbaMquGKZBMyxOZXkEsAE6zZvJ6vSfwt8IvKWQhJxVs894LUnrzsDC29e8Qt4BNfSAmMFBxaZTWoaG8X4QZcyRq1F6Yk8fZ5RPPYn1GFYFyjHURVt2WalO_04Ert_Xb8q1U6uc9oEBtNioj7Tid6XbWv2ynrXVZoXRZH7EFptgi9VEnw5WzbGxkEkoFFV5lBIk8eV7f3QKo4UItbxTP7krF2QEsWra-Sm96MfxszHjBuzYVVmd8ie8rt3O266OsDvdKAKPmjkkEleRAVSKtJhx_H7YrJxQ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره :سوخت کشتی‌ها در حال کمیاب شدن است و سوخت بانکر مورد استفاده کشتی‌ها در حال کاهش است و این مسئله هزینه حمل‌ونقل دریایی را افزایش میدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/146092" target="_blank">📅 16:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146091">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
فوری / بلومبرگ: آمریکا قصد دارد امروز پرونده هسته‌ای ایران را به شورای امنیت سازمان ملل متحد ارجاع دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/146091" target="_blank">📅 16:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146090">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4aab690b.mp4?token=Cmz5x4jrQXk9OMHYV9LORh-b-jr9UoUuVKGzmKUnPZiEWXKoPHS0hz2Y8HyVNBnGQBmR2Ea9io33scN9O9DXj_gc_JIakil4l_0o6k6juQGInHyd8OsNFcXS6sAyT4AiS4jRE1URlurcXYFaLzKwzguG2IkwlTgIAVMfhbZ7HESytMAS2fhh6My5gjzHwr4iSDa_LnjmsIGbxfY-Jiw5A8iH9RfUylE-XaQczSZLEIsqJYwtzpNXWVf5SiVYF87vTtyvrFXJos_nfpQ91-MX9OlppRzpxoEvj7DRbdm3G066akrj11BgdoY5N_snoKfhD2WfaIc1yCSNhT-LvY7MGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4aab690b.mp4?token=Cmz5x4jrQXk9OMHYV9LORh-b-jr9UoUuVKGzmKUnPZiEWXKoPHS0hz2Y8HyVNBnGQBmR2Ea9io33scN9O9DXj_gc_JIakil4l_0o6k6juQGInHyd8OsNFcXS6sAyT4AiS4jRE1URlurcXYFaLzKwzguG2IkwlTgIAVMfhbZ7HESytMAS2fhh6My5gjzHwr4iSDa_LnjmsIGbxfY-Jiw5A8iH9RfUylE-XaQczSZLEIsqJYwtzpNXWVf5SiVYF87vTtyvrFXJos_nfpQ91-MX9OlppRzpxoEvj7DRbdm3G066akrj11BgdoY5N_snoKfhD2WfaIc1yCSNhT-LvY7MGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار گسترده‌ای که توسط اسرائیل انجام شد، شهرک زوطر الشرقیه در جنوب لبنان را به لرزه درآورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/146090" target="_blank">📅 16:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146088">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GNe8m_3nk0na8uggCBGdDvwvSrrc0g_ZaDMGT6TfPBcP6_BL2ouFILelPy3zu22uOXTVpbxL9-ehWwz5fKskXlMYV5atD0y8qcoEk5SIdTAJYItfgdb5K2bkEchdr1346PfT5RzNUbeGROgfSlbrDpwmAQ4pbCRRBdXb8_GXr5cdx2ARLr2whwIGSWYSBXgv1RrHgZXP3Gg5y4wNTOsjzVuBK1XhVhLdxH6kUrNxixGetSdiGq7YRo9_3H_Ex6mYPPhf4KZbqpW2cFhntEDih4fz9AtJ9OZKVEWeG5Tz5xTl0lhA6Ls47Awls8tqnqAywnhquR757RhPyxy4M-2wCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YVoYkLUkxP6IcrSBIQxtm8mM_QSitsu9lPzJHkvzItMEu4wXBGzgvu9lZfjI9iODYG3lg4axW5nzJR0l77ghquPJ66fouPVXV1iqatnvuYtiVILuqjXagjwWFphATIECpToofTPFDyxCSfRI76Yj3d7FHVFA5CyzwXRlvLjQDZbvqjISbjK3hlaY02fFmsakAlHMdTJ3iN6YfQUUNuPogsNYRIfvTvWg6zX3LYy3AyRtycS4TW9G7rrFj46XBaBkj9gSvF5Db5jmHTaE_m5zGQWDkfCFX47Rmu0Wylp0B77NuwZg4o-2beJ8CRq1XvCu14spsXId3v4jttMbp3u4Lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پالایشگاه جازان در عربستان سعودی در اثر حملات حوثی ها دچار آتش‌سوزی شده است. تصاویر ماهواره‌ای این موضوع را تأیید می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/146088" target="_blank">📅 16:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146087">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
پزشکیان: ممکن است عده‌ای از ابزارهای فناوری سوءاستفاده کنند، اما نباید به این بهانه، راه رشد و توسعه را بر خود ببندیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/146087" target="_blank">📅 16:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146086">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
فرمانداری: احتمال شنیده شدن صدای انفجار‌های ناشی از خنثی‌سازی مهمات عمل نکرده در حوالی پایگاه هوایی بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/146086" target="_blank">📅 15:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146085">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
رسانه‌های جنگی یمن: منتظر بمانید تا ساعت ۴:۳۰ بعد از ظهر، تصاویری منتشر خواهد شد که لحظه هدف قرار گرفتن و آتش گرفتن کامیون‌های حامل سلاح‌هایی که از عربستان سعودی می‌آیند، در پایگاه ودیعه را به تصویر می‌کشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/146085" target="_blank">📅 15:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146084">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
گروسی: ایران همچنان عضو پیمان NPT است / آن‌ها باید به حرف ما گوش دهند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/146084" target="_blank">📅 15:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146083">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
هواشناسی: شدت بارش‌های امروز و فردا منجر به صدور هشدار نارنجی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/146083" target="_blank">📅 15:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146082">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee153a30e2.mp4?token=durZQ85CZhghFcBrqT5Rjat_uVQ8lfbPIpkgJfT6c01HAm1YpqLSsXS4hzu3hC4V6n86X2jY_LMoQyMhHxImvM6sDF5K2J4dpQUVGUHMpFAOLJxHOFjgFIWL9GLCKQgX_8vfys--2oNe2ZtrbVlkRfi5uZy_8-RC5xHhqZp_uofQ47DP829RdjbrYnQmsce8lqpNcQtjpL7gIiwTnmiL6Dfhe-ZDf3aGj86P4ROTutkqisQ1vgg8EdxQU30O6YhMu83_OvuBWXRNR7I2MBd6-7q6fEdBn4V9MbaW8a1cBiw0mUnvyLIZ_UfF29hiVtDgZBc0sNaNIfG1csEk98Ks8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee153a30e2.mp4?token=durZQ85CZhghFcBrqT5Rjat_uVQ8lfbPIpkgJfT6c01HAm1YpqLSsXS4hzu3hC4V6n86X2jY_LMoQyMhHxImvM6sDF5K2J4dpQUVGUHMpFAOLJxHOFjgFIWL9GLCKQgX_8vfys--2oNe2ZtrbVlkRfi5uZy_8-RC5xHhqZp_uofQ47DP829RdjbrYnQmsce8lqpNcQtjpL7gIiwTnmiL6Dfhe-ZDf3aGj86P4ROTutkqisQ1vgg8EdxQU30O6YhMu83_OvuBWXRNR7I2MBd6-7q6fEdBn4V9MbaW8a1cBiw0mUnvyLIZ_UfF29hiVtDgZBc0sNaNIfG1csEk98Ks8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه روسیه، لاوروف:
غرب به این شهرت دارد که تمایل دارد از طریق اخطاریه‌ها مذاکره کند، و مطالباتي را مطرح می‌کند که برای بسیاری از کشورها تحقیرآمیز است و بوی استعمار می‌دهد.
🔴
ما باید به مردم یادآوری کنیم که استعمار چه رنج‌هایی را به سرزمین ما وارد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/146082" target="_blank">📅 15:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146081">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
علی رغم ادعای وزیر نیرو مبنی بر پایان خاموشی‌ها، برق در مناطق مختلف تهران همچنان با قطعی روبروست
🔴
طبق گزارش تعدادی از شهروندان، از صبح، لویزان و شیان با خاموشی روبرو بوده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/146081" target="_blank">📅 15:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146080">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
نرخ بنزین با کارت سوخت جایگاه یا همان نرخ سوم از امشب به ۱۰ هزار تومان تغییر می‌کند اما نرخ اول و دوم بنزین، بدون تغییر می‌ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/146080" target="_blank">📅 15:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146079">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: برای یک جنگ فراگیر در کرانه باختری آماده می‌شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/146079" target="_blank">📅 15:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146078">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g30rR1hcR7dvPMPFG1vEBfUQfksHAkixkd86GdumELLIKHanMPM88j_-ETIeAo7RdkHKf-kvymKqHdMcyRT7fvd-znGmSNFl0sPEB7Y80QvmGdws2vkMl3-owginSCYvXGk2mDVf7JiPn67crcO2glbanw_mwScljAwajTupi_ZD3-Yz5uZItwjrQcxXPAsbYOJiiNAVKd_iImmfcs3OKPUZsinfrI2W9kcSl57TE4JUOGPO3tl9qmMQLcVkd5x6BCO-8Pmn7BfR_vV82WLlqE-x2MNmp8VBbuDJFR2qp59AVVtQbW_N44ifioZaPrh3dLDcSRqdxLAKy0IuUhnZew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بابک زنجانی اعلام کرد واسه استخدام شدن تو شرکتش باید گواهی عدم سوء پیشینه داشته باشی و تا حالا زندان نرفته باشی
🔴
پ.ن : بابک خودش چند وقته آزاد شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/146078" target="_blank">📅 15:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146077">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
الجزیره به نقل از یک تحلیل‌گر: ایران به آمریکا اطلاع داده که در صورت تصرف تپه علی‌الطاهر توسط اسرائیل، مستقیماً وارد عمل می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/146077" target="_blank">📅 14:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146076">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjSvirwW-cz6sT_GrK81s_Wcsl0Q0y7y_w26U20k7KVUH3P9zOkgMjRO9xa8d_Xnb7c7JaiMcN_SDH-LQ5fhFC4-Y8a82TxuVam67uQqTDijfWDVa-Z8uoozNyxkPNmJw6MOTDe666hLTJCzO0_c27MkmCzohlyqVJnecviA5k3P5DhBul7fY7BxJrLhDHK3h07R0UnYYg0pmc4pQijIc1bXQ5A6zjWQBWBFPNf_vcv6bpmgquPemDs6pJGoup48K8haRzMTlO9_okfm7FoMcIVhI601pVMfnonJPBBix2SmnWdq7qOLwVPrr7nSzVr-Uib5dPfg5-vflrB77Pp2ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناو هواپیمابر آبراهام لینکلن طی ساعت گذشته شهر پاتایا تایلند را پس از توقفی ۵روزه، ترک کرد
🔴
گفته شده این ناو اکنون در راه بندر سن‌دیگو آمریکاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/146076" target="_blank">📅 14:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146075">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏
👈
پزشکیان: اجرای یک روز در هفته تحت عنوان «روز بدون خودرو» برای دستگاه‌های دولتی دنبال خواهد شد؛ توسعه دور کاری و کاهش سفر‌های غیر ضروری و بین‌شهری نیز باید مورد توجه دستگاه‌ها قرار گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/146075" target="_blank">📅 14:50 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

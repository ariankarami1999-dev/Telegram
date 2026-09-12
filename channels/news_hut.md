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
<img src="https://cdn4.telesco.pe/file/Z4wiiuiVe61UCx3MfhDVZoJfvttJy6ziEJxQM6q0EBAqKuT1xPMaaA5zmyWug2XWvUsibuGr8ZT-vkAtNbtCDDOkDsNMaAsK1PhgWtWmXzXuBZYfzqeC0Q_Ly6YanQnIKTOzLe0ZsznJ1XP-PSmZIr9Jh931rOU7xL6JL53I-8fCFju36Vwh3E5DG6jqMxUYr0nCs_UQf4as2ULk75ITWkRWU4TdaaGXj7h-yS1GZiHvGonYKB5yujj7zYLyizQlRpJv1RjKv_sfxvswYiAB7k5C0N0DSQBsB3I4jpL5atg_ne1sa_DFGQCfJLiq9ZkdTpAasb3MAEBxOi7NIpCzFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 111K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 04:50:25</div>
<hr>

<div class="tg-post" id="msg-71491">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/news_hut/71491" target="_blank">📅 01:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71490">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVMzAd4wSGjRJaHpN08c8w7YQnsN2-b0OGS8O2P0JxIOihaFls_y7MqXGzPqiHXtBx4F9QtC0t0qb2DBB0QMoHvztPDC9xNYuiKU1t7C_AUTZc0_0jXIOeFjCtJI0grCYyj_aRgTj9UsUodsOFVRnFQEu0FkRLP3Yli7HQbNvgaGRHhzYVpHxzRT58PMMuK1qp9TJFZ3HUz7iNGFYxo4VctbgZhkna3MpccbCGKgS0zljflIMX-GFqLsxQzEkUHxrcMy8HBSWeJ14My6Ar-g9fQ3J0yyIj0O57kaM7QhQoWASy479YOc10rTy_Ur6PqecovXRiTGrciWWuymrMDcVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/news_hut/71490" target="_blank">📅 01:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71489">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c20cfcda3a.mp4?token=AlxdUmjrrWsp-jZ8HF9VCf-I9fObj5MQa9O9EBSeYbo4Z8AxF_T18ahxLbuGZNaFf9I1ApGuzCOjFqMPIcWUbURUI3UpTqoQTkQ7GPnuGycnr6JXLX0p_NYP--3DjsLPTXZR9uHlMXGIpGq9Dc67SxOtdYMeUj4IIUxoys2zNlj64UpxWIf_QpIrDUQRQiVV-Q5xTlk3BoZgLGc9bfdPXFKf9302kTVhsVKhanFh3Lw_N-EILy5-tl6dYBlnIB2AVzFgu4tiZ0y2uF1QxIP0cxi3zYUJE8mJ8IpVFmYp4P8hs0TpL_ggHTAlwjpIXMKON0BoA3UFYFP2kZBsVzhXKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c20cfcda3a.mp4?token=AlxdUmjrrWsp-jZ8HF9VCf-I9fObj5MQa9O9EBSeYbo4Z8AxF_T18ahxLbuGZNaFf9I1ApGuzCOjFqMPIcWUbURUI3UpTqoQTkQ7GPnuGycnr6JXLX0p_NYP--3DjsLPTXZR9uHlMXGIpGq9Dc67SxOtdYMeUj4IIUxoys2zNlj64UpxWIf_QpIrDUQRQiVV-Q5xTlk3BoZgLGc9bfdPXFKf9302kTVhsVKhanFh3Lw_N-EILy5-tl6dYBlnIB2AVzFgu4tiZ0y2uF1QxIP0cxi3zYUJE8mJ8IpVFmYp4P8hs0TpL_ggHTAlwjpIXMKON0BoA3UFYFP2kZBsVzhXKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
❌
🇾🇪
تصاویری از حملات هوایی نیروی هوایی سلطنتی عربستان سعودی به بندر «مخا» در جنوب غربی یمن که تحت کنترل انصارالله قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/news_hut/71489" target="_blank">📅 00:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71488">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIDmMeufIKXNZ8R4XIz80JcYf863dpoC_D4fcDI8Lgw9Li3ldwM6GDJjELsjsXZYxu7SOSFCGT_mWNgKoOUOu8AqBK-nBHDHt9AKW0Guhv9UUV_oqKf98mHytoRg1zZoaoJLpAwWYJO6omdZICf6vHyuHgpeLM4mHG_BchmrAh1fVRcPcyyQfm4tn_vM0qiRIgbwWHS1RcFQ8OCkZ_2xgdSrdW6gHdGXZsz4xZywUb6zILa8KWdWu3sLq2AVHcm69f8xHzDHW3kX_QO50VweSILlMMqRE4Pj3Uo-XMWMQ9WfS7pKOu64clhENEppp2Xcxp1v4zMQqa-6RB3sfqIuTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با پول ۲۰۷ در ایران تو کشورهای مختلف چه ماشینی میشه خرید؟
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/71488" target="_blank">📅 23:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71487">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2da32c63e2.mp4?token=TX-lY29P3dlWwOukpRW8BZZoEMM1Z_VEwqME_pWB6SGhYPrj1XAeoYdYO7-5LaGoA0ImoDWlPbpauH1X4V9ObRyMGDbA-6Ifwk-n6Kpr0hg0FzsL5IYRNG08PZYSAIYWmSVJq1G81DrmzmpWNFV3Mtk7DTYbhSK1A84Z4jW2gClahI6e4y7Mb515OizHYRNgXPn5cSiATXn97gXcRZXdWquPM24hadUe-zpA2BKilHfMkOoaekHMKOTUV86R7UQFEz8NuUt-yyQwv8h-bHhXaDxrGY_izOZhawi2rDGTpl-xO6d0gU4Q7Jp2xB74qPh_Zb_ESQsoXATgSCxhGLhctQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2da32c63e2.mp4?token=TX-lY29P3dlWwOukpRW8BZZoEMM1Z_VEwqME_pWB6SGhYPrj1XAeoYdYO7-5LaGoA0ImoDWlPbpauH1X4V9ObRyMGDbA-6Ifwk-n6Kpr0hg0FzsL5IYRNG08PZYSAIYWmSVJq1G81DrmzmpWNFV3Mtk7DTYbhSK1A84Z4jW2gClahI6e4y7Mb515OizHYRNgXPn5cSiATXn97gXcRZXdWquPM24hadUe-zpA2BKilHfMkOoaekHMKOTUV86R7UQFEz8NuUt-yyQwv8h-bHhXaDxrGY_izOZhawi2rDGTpl-xO6d0gU4Q7Jp2xB74qPh_Zb_ESQsoXATgSCxhGLhctQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇱🇧
🇱🇧
رسانه های نزدیک به حزب‌الله لبنان وویس هایی رو از اعضای حزب‌الله منتشر کردن که در زیر ارتفاعات علی‌الطاهر در تونل ها گیر افتاده بودن و درخواست کمک میکردن.
همه این افراد بعد از حملات ارتش اسرائیل و نابودی تاسیسات زیرزمینی کوه علی‌الطاهر کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/71487" target="_blank">📅 23:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71486">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68083de4e6.mp4?token=jdw2dpTGKLfatf7UBQOiarE1LHz7BngQG98-CikeYjwou0FcIkTbBEWQBmh9ySjDbtlSB8bH5QHnwHdtZLs_DGx-NiSNBsSqKIYtTBf27OPjz2I6UTLcLFLAmQIC0XaPxDPhRT1QtsM66NRO--jg39zShgqLRt_Ujj0VKq8UrSvOd0kJhOSST1Wg7sTNgAgCSROiQEMLM-jrbohWa5de14Vfd9HNW-t92Zw6HelVM_iMX8311YAVurdUtD551GK_J1Oh5WnhvHdvPZ1_-VwpDC0NW0dl5rc99WVU85lsxHZn2REVPD8JFotG7TUTAtkcIC4gtzZw2Y32tcKuzlNO3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68083de4e6.mp4?token=jdw2dpTGKLfatf7UBQOiarE1LHz7BngQG98-CikeYjwou0FcIkTbBEWQBmh9ySjDbtlSB8bH5QHnwHdtZLs_DGx-NiSNBsSqKIYtTBf27OPjz2I6UTLcLFLAmQIC0XaPxDPhRT1QtsM66NRO--jg39zShgqLRt_Ujj0VKq8UrSvOd0kJhOSST1Wg7sTNgAgCSROiQEMLM-jrbohWa5de14Vfd9HNW-t92Zw6HelVM_iMX8311YAVurdUtD551GK_J1Oh5WnhvHdvPZ1_-VwpDC0NW0dl5rc99WVU85lsxHZn2REVPD8JFotG7TUTAtkcIC4gtzZw2Y32tcKuzlNO3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یه دختره که پارتنرش یه ترنسه
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71486" target="_blank">📅 22:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71485">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c1f7e0a7d.mp4?token=qvlaFC2XEZx1XEEdLOs1zuxjJaCtWNNvxkMq4aYy7q65hZwPBtM-2br85XflTHU3eMsWIKC8aNdin1ydx23zG41WVwcvtSZ4qYWln4zYkwgDFPz28wAKmPr8fFkPsBS5sbIfxGtL_Ws01pZO4t5vj6aEhK_lRzN9BSX4TEu8Gl72p0v49v-DeXeHEmSGCtuuFT_a_hlQRJFK8iR9b2ngCSi4-UhvKC8ZhFSOnB5vbYFEuDCNs6zolrWdRA5Tf89nbZXPjcUTOjjsWokS_ZIWwkCYFlQlOwA5IqXl32tyaa-J_OFxJzWlLjcbwDm_Poojn52IVa0f22lk1gJyky2J4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c1f7e0a7d.mp4?token=qvlaFC2XEZx1XEEdLOs1zuxjJaCtWNNvxkMq4aYy7q65hZwPBtM-2br85XflTHU3eMsWIKC8aNdin1ydx23zG41WVwcvtSZ4qYWln4zYkwgDFPz28wAKmPr8fFkPsBS5sbIfxGtL_Ws01pZO4t5vj6aEhK_lRzN9BSX4TEu8Gl72p0v49v-DeXeHEmSGCtuuFT_a_hlQRJFK8iR9b2ngCSi4-UhvKC8ZhFSOnB5vbYFEuDCNs6zolrWdRA5Tf89nbZXPjcUTOjjsWokS_ZIWwkCYFlQlOwA5IqXl32tyaa-J_OFxJzWlLjcbwDm_Poojn52IVa0f22lk1gJyky2J4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای زن دعوت شده به صداوسیما درباره ترامپ و نتانیاهو:
ما میخایم با پول حلقه های ازدواجمون طناب داری بر گردن نتانیاهو و ترامپ بندازیم
درست ۷ کیلو و ۲۰۰ گرم طلا به قاتل ترامپ جایزه میدیم
ما میخایم خون بر شمشیر پیروز بشه
از مامان های محترم تعهد گرفتیم و به مقدار توانشون طلا کمک کردن که به قاتل ترامپ بدیم
از ارزشمند ترین دارایی هامون می‌گذریم تا ترامپ کشته بشه
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71485" target="_blank">📅 21:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71484">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🇮🇷
۱۰ دقیقه پیش، نیروی دریایی سپاه پاسداران یک موشک کروز ضدکشتی را از سیریک به سمت تنگه هرمز شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71484" target="_blank">📅 20:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71483">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dcbed492f8.mp4?token=Yc_edyAsiHaBz9dHEgOkRYADvRC01dO_S31xLHE7hxrPJUcWLmSn92Uqgxnap8aYhiSoqabNzWf4dt_GPdgJtDP9N5fv1lUlS67sEGeku70pbgfhTb_C8SMQvju0zHTTQ1ULh9PrmpjHti28yMIMHUk_8x1khzAvxzYuxBL07zqSX3FZaxrKmvn2fb_GHzlfR-sadQVJHM7D85yRKrxUWdov_yjBCckyAz0huwU9HVf0GqgZS5n7cLQSSLg6dARy69wqEBfg-1PAxzj4d4hbHFQxpY6k6sCKM7GFL6VSfoybvOREmgXrqtFVc_oiQRCZeIceZx_aVIWD4NAwo53NfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dcbed492f8.mp4?token=Yc_edyAsiHaBz9dHEgOkRYADvRC01dO_S31xLHE7hxrPJUcWLmSn92Uqgxnap8aYhiSoqabNzWf4dt_GPdgJtDP9N5fv1lUlS67sEGeku70pbgfhTb_C8SMQvju0zHTTQ1ULh9PrmpjHti28yMIMHUk_8x1khzAvxzYuxBL07zqSX3FZaxrKmvn2fb_GHzlfR-sadQVJHM7D85yRKrxUWdov_yjBCckyAz0huwU9HVf0GqgZS5n7cLQSSLg6dARy69wqEBfg-1PAxzj4d4hbHFQxpY6k6sCKM7GFL6VSfoybvOREmgXrqtFVc_oiQRCZeIceZx_aVIWD4NAwo53NfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
آتشفشان ساکوراجیما در جزیره کیوشو ژاپن فوران کرد و خاکستر و مواد آتشفشانی را تا ارتفاع چند هزار فوتی به هوا فرستاد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71483" target="_blank">📅 20:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71482">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d66564850.mp4?token=C0BRAkfKGtI2j4jK0kfricER-s2X5PziNKW3Yz_qKNvrvstnoATaUxGFlFN8R49pJ2Uqp_Q432ANUCQhCh28pa3gvKcdkNN0QA0cspiajGpAairEULSEOjgLlzKIja9BwgDkDcg59iQ1r917KnjbUh39S_BnGFMgpREuvyppCVXx9NOnfMyHh1H898ylLV1FsK5Bhp3mJLvl_XHKFiga4y0QGjCUjY80GbU6H7UNqek37AiukcirUDXHvTJvllo9O5f160m1d4s6gqVs34B2WBJjM91dNWknH1JUod31OWn4aqUgLmP6725FDSN3Fg5PG0-kz517aKIWFbOXYv5zDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d66564850.mp4?token=C0BRAkfKGtI2j4jK0kfricER-s2X5PziNKW3Yz_qKNvrvstnoATaUxGFlFN8R49pJ2Uqp_Q432ANUCQhCh28pa3gvKcdkNN0QA0cspiajGpAairEULSEOjgLlzKIja9BwgDkDcg59iQ1r917KnjbUh39S_BnGFMgpREuvyppCVXx9NOnfMyHh1H898ylLV1FsK5Bhp3mJLvl_XHKFiga4y0QGjCUjY80GbU6H7UNqek37AiukcirUDXHvTJvllo9O5f160m1d4s6gqVs34B2WBJjM91dNWknH1JUod31OWn4aqUgLmP6725FDSN3Fg5PG0-kz517aKIWFbOXYv5zDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
صحبت های عجیب
پوریا بختیاری کارشناس اقتصادی در مصاحبه با علی ضیا درباره ابراهیم رئیسی:
نزدیکان رئیسی گفتند که حاج‌آقا خودش اقرار کرده که اقتصاد متوجه نمی‌شود.
بعد گفتیم خب، یعنی باید برای رئیس‌جمهور کلاس اقتصاد بگذاریم؟
گفتند نه، کلاس اقتصاد که نه؛ حاج‌آقا ذهنش می‌پرد و خسته می‌شود. بیاییم موشن‌گرافی بسازیم.
ما یک تیم انیمیشن آوردیم که برای رئیس‌جمهور مملکت کلیپ‌های اقتصادی درست کند. قانون هم گذاشته بودند که هر کدام از کلیپ‌ها بیشتر از سه دقیقه نشود، چون ذهن حاج‌آقا می‌پرد.
ببینید چقدر این موضوع تلخ و «دارک» است که برای رئیس‌جمهور مملکت و بالاترین قدرت اجرایی، بروی انیمیشن درست کنی تا بلکه اقتصاد را بفهمد!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71482" target="_blank">📅 19:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71481">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90c5de5a1.mp4?token=PhD6V8B_UjbUKcC6yPu4Lx9gPWUCO1bWBnB0OMBK_HWsw34zCnqmgdAzdck-ebh9fQIrDi5Wq-sRzwten_U6wvXVcHmrBLgncrMLLnycfZT4dcTExy2xvv3XjB_OMW0mugNrN58I9_tSFBeCfDnfKmlzf0_rS0EYFe9KW8L1ot9IRQP8zTOB1VbkdfVzQW-PJpca6iBhUumpxkaLIkXIgjaK6FwpS4YmAfxA0jdB80ZhB0nVf6JFh7LDfrvfuer5SAOBoVtL_K3_eYTssvLnMh8KsxDkWjYV9paSZcVp0HFv2JD6l2zF-fht8PQE9qAmmjVTE2A-SMNjXlDVQdaKGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90c5de5a1.mp4?token=PhD6V8B_UjbUKcC6yPu4Lx9gPWUCO1bWBnB0OMBK_HWsw34zCnqmgdAzdck-ebh9fQIrDi5Wq-sRzwten_U6wvXVcHmrBLgncrMLLnycfZT4dcTExy2xvv3XjB_OMW0mugNrN58I9_tSFBeCfDnfKmlzf0_rS0EYFe9KW8L1ot9IRQP8zTOB1VbkdfVzQW-PJpca6iBhUumpxkaLIkXIgjaK6FwpS4YmAfxA0jdB80ZhB0nVf6JFh7LDfrvfuer5SAOBoVtL_K3_eYTssvLnMh8KsxDkWjYV9paSZcVp0HFv2JD6l2zF-fht8PQE9qAmmjVTE2A-SMNjXlDVQdaKGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین پایگاه دریایی نووروسیسک روسیه - بندر اصلی باقی مانده ناوگان دریای سیاه - را با حمله ترکیبی پهپاد و موشک در طول شب هدف قرار داد.
لیست خسارات تایید شده قابل توجه است
؛
ستاد کل ارتش می‌گوید سه کشتی جنگی (مین‌روب ژلزنیاکوف، ناوچه حامل کالیبر، دریاسالار اسن، و کشتی پهلوگیری پیوتر مورگونوف) به علاوه انبار سوخت مورد اصابت قرار گرفته‌اند.
اطلاعات و OSINT اوکراین، ناوچه دریاسالار ماکاروف، یک کشتی موشک‌انداز بویان-ام (غیرعملیاتی ارزیابی شده)، کشتی گشت‌زنی واسیلی بیکوف، چندین قایق موشک‌انداز و دو رادار دفاع هوایی در نزدیکی گلندژیک را اضافه می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71481" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71480">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71480" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71480" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71479">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kva-lxxIwH3mH8gUW2hvHc2W6yK-ML_sTxHdLHxNSClQeeHwr09w5LMvmHd9AFGA_sCLbLVY8LkJODSKKsYDn1CDl6-TKUWcjGKV9Z_KvlQ9BAvMCVFHm_TDhyRJ6DNK06t1WC4ROZAYZ-YOdVhqb0X-Y-ttuXbpR-WJpQIeRz9BmaJumOy3TQvWLIzjyiTShwCrpY9nWystkLhsXuR66QnLV89QbQ0DBTy0m47jNEh3zzMwcJb37CEQnGlxuhqJ2x036gtHizkKGZLuxFRm4FZo1ZyNiMUBb2KpQl2rG8LzQ-M_gi4FwkNxtsHJ40oimFihSt9Ox5Oqz4K8rvvvNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71479" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71478">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hADUewyMLtkbS6r0yJr2o_5q8XCijdHuKiUA9hKY-DGXnXyNR96NgFdiHNejDPa64a1F6IQya5Rjl2ce4zTKLE9tvOWNuAZBsMqW1WCRQV7zKoLTGrCRL6HxnZRIYgX_UR8C6nJxrhMHJor596FTXZ9HjTX3Hpg9M-iM38GCFrTZqjlKt9QSom2_QMOHAcQOVvUGedFtaMRS1KyutpCqYgC6TwlPLASjxcgeyDO4ajDKk5k05Oyluz1cw8WUNlB-vrOSlNkgNmicnriYxYQcHqw9gyqzLswAYOKRgBT-uqn4iluYA-SKBIGG5s89d9HT2IIVSmgMunE3vKg41uZ3-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
می‌خواهم برای رئیس‌جمهور دونالد جی. ترامپ، خانواده‌اش و مردم آمریکا آرزوی «شانا تووا» (Shana Tova) داشته باشم؛ سالی نو همراه با شادی و سلامتی.
در طول سال گذشته، ایالات متحده و اسرائیل با یکدیگر به پیشرفت‌های تاریخی دست یافته‌اند. ایران و محور شرارتِ آن، ضعیف‌تر از هر زمان دیگری شده‌اند، در حالی که اتحاد میان آمریکا و اسرائیل قوی‌تر از همیشه است.
من به رئیس‌جمهور ترامپ بابت اعمال محاصره علیه رژیم شرور ایران و فشار اقتصادی بر بزرگ‌ترین منبع بی‌ثباتی در جهان، تبریک می‌گویم.
مردم اسرائیل در مقابله با نیروهای ترور، در کنار مردم ایالات متحده و رئیس‌جمهور ترامپ ایستاده‌اند.
در سال پیشِ رو، ما همچنان به تلاش برای امن‌تر ساختن جهان برای همگان ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71478" target="_blank">📅 18:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71477">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0625ae5db9.mp4?token=Z08VJALKYBaIwVoZDUPfB8D4KUeB-mOayFAEFAFM6mUf0YpJG7hSRwdXiXGnRxh7fD0nGUUKrhDP33SHxcOhP16SfsumQXf4I61-ngf28eF0qreRMrshcYOGDfUj_ev2JqNBa0pa8spAQEBJktooOZ3lbu9ns1RzjIrnllz3IUo5SKgLBw-zCfp76krYjx_fT6f2hlpVcnNIjTYI3VxsI0-OYmA1fbVVcB1l65QQm7LayL3Lpfp5MS-pQIkoV9uvWfTlk9f_FOi4efLBg7_BM_ao-X0ufzt3F3tTTRH00h5s0yYkekgfBffDB-v_VLswmAotmSrWO3yZ4CTJul7bFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0625ae5db9.mp4?token=Z08VJALKYBaIwVoZDUPfB8D4KUeB-mOayFAEFAFM6mUf0YpJG7hSRwdXiXGnRxh7fD0nGUUKrhDP33SHxcOhP16SfsumQXf4I61-ngf28eF0qreRMrshcYOGDfUj_ev2JqNBa0pa8spAQEBJktooOZ3lbu9ns1RzjIrnllz3IUo5SKgLBw-zCfp76krYjx_fT6f2hlpVcnNIjTYI3VxsI0-OYmA1fbVVcB1l65QQm7LayL3Lpfp5MS-pQIkoV9uvWfTlk9f_FOi4efLBg7_BM_ao-X0ufzt3F3tTTRH00h5s0yYkekgfBffDB-v_VLswmAotmSrWO3yZ4CTJul7bFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ما به نیروهای نظامی‌ای که هم‌اکنون در تلاشند تا اطمینان حاصل کنند بزرگ‌ترین حامی تروریسم در جهان — یعنی جمهوری اسلامی ایران  — هرگز و به هیچ وجه به سلاح هسته‌ای دست نخواهد یافت، ادای احترام می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71477" target="_blank">📅 17:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71475">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=Ns8YaXynhZMf5bR1xMXfJF_nyD_Iv-_aT54yKcfG6l65HFnGcUP9fFXxwnWLy79eZuhgq214Wzcx-DZJG78_ARaiWYKzREFBrN4AnPHGtVvxo37DXWjs6LpZwRJ4dZg3ub97Xt03O9SR9Ax9epkdiCDI8iy2KEwG55O2DIWpRB-LoM4ICdUM04lV6N97sH0_ndHFvsmnZSH0DLIs6jPpecCAt5Lfg28Ffhko2s3NrYVPvxPPCsKgiB_OovPpcJCIXMVF2t6jGb6zSyRVk3jqrHF2UnTfBi0VyIIAQaCbgCtX_H0y3kmiOj8dTvxzGK3ZRI2IIHDNvBy4uKi3STjoFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=Ns8YaXynhZMf5bR1xMXfJF_nyD_Iv-_aT54yKcfG6l65HFnGcUP9fFXxwnWLy79eZuhgq214Wzcx-DZJG78_ARaiWYKzREFBrN4AnPHGtVvxo37DXWjs6LpZwRJ4dZg3ub97Xt03O9SR9Ax9epkdiCDI8iy2KEwG55O2DIWpRB-LoM4ICdUM04lV6N97sH0_ndHFvsmnZSH0DLIs6jPpecCAt5Lfg28Ffhko2s3NrYVPvxPPCsKgiB_OovPpcJCIXMVF2t6jGb6zSyRVk3jqrHF2UnTfBi0VyIIAQaCbgCtX_H0y3kmiOj8dTvxzGK3ZRI2IIHDNvBy4uKi3STjoFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ واقعه ۱۱ سپتامبر را به جنگ خود علیه ایران پیوند می‌دهد:
به همین دلیل است که امروز می‌جنگیم. ما چاره‌ای نداریم؛ تنها گزینه، پیروزی است. ما سرسختانه می‌جنگیم. برای پیروزی می‌جنگیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71475" target="_blank">📅 17:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71474">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c788d5732.mp4?token=Ke7G666fnBDuSqVeRfrzIamHgZGT_2D-5JpU9iodfJH7TB4cZzk0ELlkr7YxjK48B_GolV0AHmtBrrkWocnwGq0KLKNkBbwqwAZlohPnMnraiU6qmjjPGeostQSSV7xrKyylP2SlEQX-yD75bhJ0WqzMGbJZj9jbNvYx634mLQmB0rpOHQ60afEcaC-mdscBaXbWnN3RRCNuFic94kQfAhbNzefkM_TJ9E1wTrF-XyVZrtlHGYxdsbK-79TLRB5dQNEIVMqNawOY5czKe3oShyCGaZ6esPcZ8tNZAYSCj9yraPpIeDc3beb-EnCmqYrRYnX57nbapnSu7vKfOv0qvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c788d5732.mp4?token=Ke7G666fnBDuSqVeRfrzIamHgZGT_2D-5JpU9iodfJH7TB4cZzk0ELlkr7YxjK48B_GolV0AHmtBrrkWocnwGq0KLKNkBbwqwAZlohPnMnraiU6qmjjPGeostQSSV7xrKyylP2SlEQX-yD75bhJ0WqzMGbJZj9jbNvYx634mLQmB0rpOHQ60afEcaC-mdscBaXbWnN3RRCNuFic94kQfAhbNzefkM_TJ9E1wTrF-XyVZrtlHGYxdsbK-79TLRB5dQNEIVMqNawOY5czKe3oShyCGaZ6esPcZ8tNZAYSCj9yraPpIeDc3beb-EnCmqYrRYnX57nbapnSu7vKfOv0qvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
آنچه اکنون در مورد ایران شاهد آن هستیم، حیوانی است که در تنگنا گرفتار و زخمی شده است.
این آخرین نفس‌های رژیمی رو به احتضار است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71474" target="_blank">📅 17:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71473">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/971b0d1003.mp4?token=Fdc7vizF_QeTsUpKKquxzSvArMpEcHekrho-VrBewobSD4FVzXQSwYZXlW-cxvY9g2i1L0g-i7YYOMOVjQsgjEZM4cEFFc4-z_wudl0kf1g3bntsIi2igCM0Qljvlj_SBUpSdqq4yf7RKZUpCNe4_ThCX-zJUjuoqkuvhgKcije1mMJG_9gwt05IQfF5AgkdSCz9h9FydenzQ-A6Oe7ApuZS0G9G7fSQSOC5VFYV272E16AyTRiohdpgXrzY1Hidgu6XdN1UR8dhl8CQTo0WWGAIoNLZOVFb1-wYNQ_t7rpzwxYQDe-h4IkHjO_B-8GDgU_OG2ZM3M_H8k2otBlIAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/971b0d1003.mp4?token=Fdc7vizF_QeTsUpKKquxzSvArMpEcHekrho-VrBewobSD4FVzXQSwYZXlW-cxvY9g2i1L0g-i7YYOMOVjQsgjEZM4cEFFc4-z_wudl0kf1g3bntsIi2igCM0Qljvlj_SBUpSdqq4yf7RKZUpCNe4_ThCX-zJUjuoqkuvhgKcije1mMJG_9gwt05IQfF5AgkdSCz9h9FydenzQ-A6Oe7ApuZS0G9G7fSQSOC5VFYV272E16AyTRiohdpgXrzY1Hidgu6XdN1UR8dhl8CQTo0WWGAIoNLZOVFb1-wYNQ_t7rpzwxYQDe-h4IkHjO_B-8GDgU_OG2ZM3M_H8k2otBlIAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇱
اعتراض ربات های انسان‌نما در مقابل وزارت امور دیجیتال لهستان و سردادن شعارهایی با مضمون«ما خواهان قانون‌گذاری هستیم»و «از مشاغل دفاع کنید»
😳
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71473" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71472">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3ddeb433.mp4?token=F15lPqRGbVJa6UzlXxbkkL7ErTLskhprJX3Qq-f2QtKAS3Lc0-NMwvf0Xv03Qgx4rHXJ6Gjjli16Ee_jv0gO0T8LVl0LxsDEV4MLdFpFB1zODspzbhu50EbFjbjPuzeGIl1wruWTNWdlc6b5C0BCUFRW7eSz_VkvjT051yH1TUTvLYMpQyMuAobXpzpRZ5NkEmT-TrZpe6tOGWKaGPqCMxX-I6q_A3oyIssKvYxzI0o_PBJKA77I2K3wFDZ5JAeWhosZyRzcwMH_MZaSQlkScAme0DYQLcSGp7S74HF22KgH6rAaN-ULeBoJ2o8RJCZMNHz35o2JV2SzIiq9b8DXFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3ddeb433.mp4?token=F15lPqRGbVJa6UzlXxbkkL7ErTLskhprJX3Qq-f2QtKAS3Lc0-NMwvf0Xv03Qgx4rHXJ6Gjjli16Ee_jv0gO0T8LVl0LxsDEV4MLdFpFB1zODspzbhu50EbFjbjPuzeGIl1wruWTNWdlc6b5C0BCUFRW7eSz_VkvjT051yH1TUTvLYMpQyMuAobXpzpRZ5NkEmT-TrZpe6tOGWKaGPqCMxX-I6q_A3oyIssKvYxzI0o_PBJKA77I2K3wFDZ5JAeWhosZyRzcwMH_MZaSQlkScAme0DYQLcSGp7S74HF22KgH6rAaN-ULeBoJ2o8RJCZMNHz35o2JV2SzIiq9b8DXFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
❌
🇶🇦
هم‌زمان با نخستین سالگرد حمله هوایی اسرائیل به دوحه (قطر) در سپتامبر ۲۰۲۵ — که نخستین حمله اسرائیل به خاک قطر محسوب می‌شود — تصاویر جدیدی از این رویداد منتشر شده است.
این حمله، مقامات ارشد حماس از جمله «خلیل الحیه»، مذاکره‌کننده ارشد این گروه را در جریان مذاکرات آتش‌بس هدف قرار داد.
اگرچه رهبران ارشد حماس از این حمله جان سالم به در بردند، اما شش نفر، از جمله پسر خلیل الحیه و یک مأمور امنیتی قطری، کشته شدند.
این تصاویر جدید که منبع آن‌ها شبکه تلویزیونی «العربی» (Al-Araby TV) اعلام شده، لحظه اصابت را از زوایایی که پیش‌تر دیده نشده بودند، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71472" target="_blank">📅 16:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71471">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e182f67792.mp4?token=jfYj0hTg41jEoLjo97geIA8myNaHMVgA9iOgVMhRKLK_73uOCNpU1n50oqIxsfIuFsH-rf0VmCTtfdYHvA3tgtAsvFe60yl2iLKY6Oeft8q2L92oLyCA-av9x0HTzKjqqd7yCMos8PUycWEQx89EiIvalJRjex9i6FlNmEgcC-NJw6njlRkGMV_7WhOn8c-AV8uX1lq9ITQzWlQycRu2y_NEtl5RFG3iIE6eXGZk5iVplyIZve8FYqSWBhkHorFKAvzxWKJdM0ZdX-vcpSrmBVeEqyq58MU5R2J2ZViSsSa5nWKJHWFC9ni4gLCsma7lJl9njB_iox3TZ9KZXpJ63A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e182f67792.mp4?token=jfYj0hTg41jEoLjo97geIA8myNaHMVgA9iOgVMhRKLK_73uOCNpU1n50oqIxsfIuFsH-rf0VmCTtfdYHvA3tgtAsvFe60yl2iLKY6Oeft8q2L92oLyCA-av9x0HTzKjqqd7yCMos8PUycWEQx89EiIvalJRjex9i6FlNmEgcC-NJw6njlRkGMV_7WhOn8c-AV8uX1lq9ITQzWlQycRu2y_NEtl5RFG3iIE6eXGZk5iVplyIZve8FYqSWBhkHorFKAvzxWKJdM0ZdX-vcpSrmBVeEqyq58MU5R2J2ZViSsSa5nWKJHWFC9ni4gLCsma7lJl9njB_iox3TZ9KZXpJ63A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه های این بانو درباره وظایف زن مرد توی ازدواج ۳ میلیون ویو گرفته واقعا مفید بود
😏
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71471" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71470">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28a9989cd.mp4?token=qaInI9hoBYDs-ZWoxaSiq71mNIia5rs5d21CK3fV3WtwKi40GkZ0NGLeGhqg0tLzNzcDmGvVHOjph-1hsIXWq6FQyMiFzMfKxCchWsvgd3NuNZBdKg4T-p1TdpZcARdGHVHAZ-izq6jZfji7oQ60kIOXaRruB6Qb4ImGagveGc-3ELNnXStYI53xmdhqZVuHRbaoOk9N2RMOsMYJIu2cPYDy4mh80ONCepGNUdwpuXIdGiZEgsKwMWLfufxgK-THijuCVjyph916HL5MVC1FYaKMmTVIE26yoaWKklsTDgFaerX8aab0KKNfU1ZMyg4GnQ8iHEWc9gLg6EwGLdoXDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28a9989cd.mp4?token=qaInI9hoBYDs-ZWoxaSiq71mNIia5rs5d21CK3fV3WtwKi40GkZ0NGLeGhqg0tLzNzcDmGvVHOjph-1hsIXWq6FQyMiFzMfKxCchWsvgd3NuNZBdKg4T-p1TdpZcARdGHVHAZ-izq6jZfji7oQ60kIOXaRruB6Qb4ImGagveGc-3ELNnXStYI53xmdhqZVuHRbaoOk9N2RMOsMYJIu2cPYDy4mh80ONCepGNUdwpuXIdGiZEgsKwMWLfufxgK-THijuCVjyph916HL5MVC1FYaKMmTVIE26yoaWKklsTDgFaerX8aab0KKNfU1ZMyg4GnQ8iHEWc9gLg6EwGLdoXDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شرکت پخش فرآورده‌های نفتی:
موفق شدیم رقم ۱۰ هزارتومان را در پمپ بنزین‌ها نشان دهیم و برچسب‌های صفر ثابت را بردارید
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71470" target="_blank">📅 15:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71469">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc8b06f7d.mp4?token=QADaBRGfwhJ91Jz1X_yIlNwJRQSidiluZDBMsdJtmomjMZS5gnVaOfDuoWoc-ZFAj8cBdpsMgyMgZZYr7u9DEcEerEO6-KMB4vYuv2qBO6PE_0YnKXbbazCxqDnOdM3P7EbPHIxOu7SxnJHUbEwjY3fqjD7Pl1VnVo-_SJCtG9JKzNOg0nzPiUiMsqCso7S49LAkEHmVxgp5vV3HdNj3fSGzRoHf9C-g3xBKA1kucBSu8-xQxGEuhBwJex1CZD4Yce8UkUFHC6u3HzaLRRqWxxYQFF7ozNppsTbX6qVJBGXRmLSOFNN8UkxAAT43lsP5nJPVWIO6FGFNVRPb9PAuDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc8b06f7d.mp4?token=QADaBRGfwhJ91Jz1X_yIlNwJRQSidiluZDBMsdJtmomjMZS5gnVaOfDuoWoc-ZFAj8cBdpsMgyMgZZYr7u9DEcEerEO6-KMB4vYuv2qBO6PE_0YnKXbbazCxqDnOdM3P7EbPHIxOu7SxnJHUbEwjY3fqjD7Pl1VnVo-_SJCtG9JKzNOg0nzPiUiMsqCso7S49LAkEHmVxgp5vV3HdNj3fSGzRoHf9C-g3xBKA1kucBSu8-xQxGEuhBwJex1CZD4Yce8UkUFHC6u3HzaLRRqWxxYQFF7ozNppsTbX6qVJBGXRmLSOFNN8UkxAAT43lsP5nJPVWIO6FGFNVRPb9PAuDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔞
اگه بدون کاندوم رابطه جنسی برقرار می‌کنید؛
این پست رو یه گوشه‌ای تو تلگرامتون ذخیره کنید که یه روزی بدجوری به کارتون میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71469" target="_blank">📅 15:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71465">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54fcf2b7ac.mp4?token=Y9jrafRa63HcEi9nLkjogY5zcSze2Aag92Nm6L8QK1RrsxVZEJw2be6obvFveSC1ScCXVbIR1i6WEp2_VvrbIHkHY7ktvUjOfpYFoIqlzrT-8ayQA0ZkiUiGxTC6G4xZcKpeK8T0SQ4kY-syADzpd7Ltly2xXDWwlid6gpCIPCdnlS1Ub4yULJmXBgRJbn2SPgmCfOx8j-YhduBaLjuAcWeGIpxuXHTh-1GnnpWkZoX97ViC1fCTK2Xpl1N4Hn_OtRSc56Cw-0Htn14fl-7KTEq7lQ_6UjInooheIuw5pTDYfK4hPcPRha0kFSRKwqKTQ3SCRZeQg2xXdDpRsjBAOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54fcf2b7ac.mp4?token=Y9jrafRa63HcEi9nLkjogY5zcSze2Aag92Nm6L8QK1RrsxVZEJw2be6obvFveSC1ScCXVbIR1i6WEp2_VvrbIHkHY7ktvUjOfpYFoIqlzrT-8ayQA0ZkiUiGxTC6G4xZcKpeK8T0SQ4kY-syADzpd7Ltly2xXDWwlid6gpCIPCdnlS1Ub4yULJmXBgRJbn2SPgmCfOx8j-YhduBaLjuAcWeGIpxuXHTh-1GnnpWkZoX97ViC1fCTK2Xpl1N4Hn_OtRSc56Cw-0Htn14fl-7KTEq7lQ_6UjInooheIuw5pTDYfK4hPcPRha0kFSRKwqKTQ3SCRZeQg2xXdDpRsjBAOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
در ۱۱ سپتامبر ۲۰۰۱، شبکه تروریستی القاعده به رهبری اسامه بن‌لادن، حملاتی هماهنگ‌شده علیه ایالات متحده انجام داد.
🗣️
در این عملیات، ۱۹ عضو القاعده چهار هواپیمای مسافربری را ربودند.
🇸🇦
۱۵ نفر تبعه عربستان سعودی.
🇦🇪
۲ نفر از امارات متحده عربی.
🇪🇬
۱ نفر از مصر.
🇱🇧
۱ نفر از لبنان.
دو هواپیما به برج‌های دوقلوی مرکز تجارت جهانی در نیویورک برخورد کردند و هواپیمای سوم به ساختمان پنتاگون در ویرجینیا اصابت کرد.
هواپیمای چهارم نیز در پنسیلوانیا سقوط کرد؛ پس از آنکه مسافران برای بازپس‌گیری کنترل هواپیما تلاش کردند.
در مجموع، ۲٬۹۷۶ نفر در این حملات کشته شدند و هزاران نفر نیز مجروح شدند.
تحقیقات گسترده FBI، ارتباط مستقیم این حملات با القاعده و نقش این شبکه در سازماندهی و آموزش هواپیمارباها را تأیید کرد.
پس از حملات، آمریکا عملیات نظامی در افغانستان را با هدف سرنگونی حکومت طالبان و مقابله با القاعده آغاز کرد.
اسامه بن‌لادن سرانجام در ۲ مه ۲۰۱۱ در پاکستان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71465" target="_blank">📅 14:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71464">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇹🇷
پهپاد «آکینجی» (AKINCI) ترکیه اکنون با موفقیت موشک‌های UAV-300 و UAV-122 ساخت شرکت «روکت‌سان» (ROKETSAN) را آزمایش و شلیک کرده است.
نقطه عطف این آزمایش، شلیک موشک بالستیک مافوق‌صوت UAV-300 بود که با اصابت دقیق به هدف در فاصله‌ای بیش از ۲۵۰ کیلومتر، توانمندی آکینجی در انجام حملات بالستیک دوربرد را به اثبات رساند.
موشک کوچک‌تر UAV-122 نیز در جریان این آزمایش با موفقیت شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71464" target="_blank">📅 14:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71461">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd5a9f3c7.mp4?token=APX9lVhZU0ialwtyozX94bbJtaknDCAKVBlRnPSg4lD1D9GD_Lu28SsKQiG8ekiVROdqTyWPSTx8xB21PjOuQvG3zFO9Kxx0G4feyjR-h1uJ5GfVqn_ApCZ0zm55pXK13H0sdnFHBteZT0SODEb_5XcWFgcAC3ItZQQCNrtBmvzG1tNPnMdagoKPk01zcN6HCJfEifJQgiLLCVAeJ32FRg6BOH4AzcmqLKTOvd4PLVPhWabxDYrSY-3Zy6riqlO93vfh8Hk9HobIhuwrODgEFikMKydfWpM_4IPZUQy8GLvSnXeA42skbQc_7HPq1Xb-KUbSL1xgigD-Xa84nBobLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd5a9f3c7.mp4?token=APX9lVhZU0ialwtyozX94bbJtaknDCAKVBlRnPSg4lD1D9GD_Lu28SsKQiG8ekiVROdqTyWPSTx8xB21PjOuQvG3zFO9Kxx0G4feyjR-h1uJ5GfVqn_ApCZ0zm55pXK13H0sdnFHBteZT0SODEb_5XcWFgcAC3ItZQQCNrtBmvzG1tNPnMdagoKPk01zcN6HCJfEifJQgiLLCVAeJ32FRg6BOH4AzcmqLKTOvd4PLVPhWabxDYrSY-3Zy6riqlO93vfh8Hk9HobIhuwrODgEFikMKydfWpM_4IPZUQy8GLvSnXeA42skbQc_7HPq1Xb-KUbSL1xgigD-Xa84nBobLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حمله شناورهای بدون سرنشین (USV) اوکراین به بندر سوچی در منطقه کراسنودار روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71461" target="_blank">📅 13:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71460">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWGfMfxSbYpyJ-d3OUimRnWnd5xCyF7vSLyAkM5gSHubV3fBwRjMGliw2xf071tY_mYUzLhO_uXfWol-S-2XvKpEyvw-p1hvnZTlYMRGOBdQCxRlJx2cO5e67YlgQnxVJnH0BVhSBnfP9JheA8lQLZpP7uSgbkO2K8d8zIIRJh21gZjALdf3Wa6hWFkmzbxeIlGr9TVYfoeY7CY5CNxndzC3bydtwaJoVMlWatdyQjEIyaA55MiJc6Lx0PzaksZbY98ZMJ1cskYXUHKTXPVJPuRgqE7T_UT76WiYEIXgsxaxm4ova0STtPevRWZNgw856ngo69cHHII_ZzhFqCmc6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇾🇪
🇾🇪
حوثی‌های یمن جزیره پریم (میون) را تصرف کرده و کنترل خود را بر تنگه باب‌المندب تکمیل کردند.
⏺
🗞
خبرگزاری رویترز نیز در گزارشی جداگانه اعلام کرده است؛
حوثی ها به شهر ساحلی «ذوباب» — که درست در کنار این تنگه واقع شده — رسیده‌اند.
حوثی‌ها اکنون تقریباً تمام نوار ساحلی یمن در دریای سرخ را در کنترل خود دارند.
این دستاورد سرزمینی را می‌توان از نظر راهبردی، مهم‌ترین پیشروی در کل جنگ یمن دانست.
جزیره پریم در میانه این تنگه ۲۹ کیلومتری قرار گرفته و عملاً آن را به دو مسیر کشتیرانی مجزا تقسیم می‌کند.
تسلط بر این جزیره و همچنین نوار ساحلی مجاور آن بدین معناست که حوثی‌ها می‌توانند کشتی‌های عبوری را با استفاده از توپخانه و تسلیحات کوتاه‌برد تهدید کنند؛ نه صرفاً با موشک‌های دوربرد و پهپادهایی که از مناطق داخلی‌تر شلیک می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71460" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71459">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71459" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71459" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71458">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYPH6B9NTq2OOGuDuyIp5zKhHRktqySza1PlT_cqg6gOv5mkv9QccFI2O1yNUiQ9R3jBAwjXsPxLEAJAgYN2FhWpgvcu-OG6y5jos1yNk-5ljsvN-ih6TtdCQ95MDPw91AUUohHfEddc13b51Y_-dGtOlSscSUPRSnr2YwSHlZcIar0BUcg3e_vMNlo4gxbzSCwzCqx3dtyW1rbbByTNeN5RUeMVxvoU7HL_jLDL8nv-dLGtLpXeAzRFq9ji75IIv7IxdxftBVKsXIa1cWo1QmFhhE20wVmly2k08ym7IHfqgxNq2hAiRvCLndtnmR2l68Em3JSc7HhDyplQ8Pmhog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
والنسیا
🆚
سویا
فیورنتینا
🆚
ونزیا
شالکه
🆚
انیون برلین
مارسی
🆚
رن
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71458" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71457">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4149a89627.mp4?token=wARcd5p148YlDvw_ezcgpfqw9eehQuTADDrLeLOg2HNQJBKjSUSoVcEtFewg0Rt406d3_gecjsKmAcgN-UzSMQgG7Io0aap_7VVNhoXS1HFeQdQwbIXCo9Rj_0fNX78pmld4MvHziKRt7jZwBx_OxmHuwBGe5-aCxqrbTe2A6LIApPalq1U9YRyhiDh0wsaPpZEjc0B3jmK9QwBzxJXkGwt2v5ZiJk3P1TQ651sh0cEsVBqFb2QFwUzMYtwz39PgCWlB-HCMNzuoV1ewX0SQ_KvpJCTGCRnRT0LxKL5TcrBAXVMHzuYPFGt8n_v5B0-EYb_DvXN8nI5_vyDkPj8dKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4149a89627.mp4?token=wARcd5p148YlDvw_ezcgpfqw9eehQuTADDrLeLOg2HNQJBKjSUSoVcEtFewg0Rt406d3_gecjsKmAcgN-UzSMQgG7Io0aap_7VVNhoXS1HFeQdQwbIXCo9Rj_0fNX78pmld4MvHziKRt7jZwBx_OxmHuwBGe5-aCxqrbTe2A6LIApPalq1U9YRyhiDh0wsaPpZEjc0B3jmK9QwBzxJXkGwt2v5ZiJk3P1TQ651sh0cEsVBqFb2QFwUzMYtwz39PgCWlB-HCMNzuoV1ewX0SQ_KvpJCTGCRnRT0LxKL5TcrBAXVMHzuYPFGt8n_v5B0-EYb_DvXN8nI5_vyDkPj8dKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کارشناس صداسیما: ما ۵۰۰ میلیون تُن طلا داریم.
ـ مجری:  الحمدلله
+ کل طلای استخراج شده تو جهان ۲۲۰ هزار تنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71457" target="_blank">📅 12:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71456">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/27045da6d6.mp4?token=v18qfxlFqVgDbmHmxFbJ5idkSgz0gUidHFxzyK4ckb2SdH-6usdM9d3kKe7569B3_wHsbM-Huq_BpFyGKcHDBtej4LTLQDi1UWfxToc3Dpnw62qPkSChCUR7qq6VSdyeB_h5VKcCd6g9i87alRwShZWu_j43dxJmRO0L_Xjk8a5j0ejJzGTTE0CsEqYNm7EqT9h-ecidzrDHuDe-EM3FVHKOKvD5e60Q27SP-FpyOLufhA0ij46FTxyKLvEhQi-1_5tP_jr9wXR8ge_dVlHUubkesNEw45poUrpIFiHpRgf_liT1_iFUUCOVaz-CoQXIUXwLDvfVlarf1IsYCK9F9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/27045da6d6.mp4?token=v18qfxlFqVgDbmHmxFbJ5idkSgz0gUidHFxzyK4ckb2SdH-6usdM9d3kKe7569B3_wHsbM-Huq_BpFyGKcHDBtej4LTLQDi1UWfxToc3Dpnw62qPkSChCUR7qq6VSdyeB_h5VKcCd6g9i87alRwShZWu_j43dxJmRO0L_Xjk8a5j0ejJzGTTE0CsEqYNm7EqT9h-ecidzrDHuDe-EM3FVHKOKvD5e60Q27SP-FpyOLufhA0ij46FTxyKLvEhQi-1_5tP_jr9wXR8ge_dVlHUubkesNEw45poUrpIFiHpRgf_liT1_iFUUCOVaz-CoQXIUXwLDvfVlarf1IsYCK9F9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به زنش گفته دست پختت رو سگم نمیخوره! اونم برای اینکه شوهرش رو ضایع کنه، رفته غذاشو گذاشته جلوی سگ!
در نهایت سگه این شاهکارو خلق کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71456" target="_blank">📅 11:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71455">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c6ecedd2b.mp4?token=dgkqhOuglU1LGhtE7TDLYI1a8yBhtfUujhKhKdM5W0NvpD6nDCjwMM2seW4B7u2KvAdRPIe7OMYymuxaX0fN1uwf-pAx5IHEgIvKCO35v51-vO1fz4_vDi_AbGutFqzRqsj6D4jkcSSEKYsjCWJzBrfx-zodOU7mREsz6DrpBTk3gFrv1wn-aB70-8SkXi0oTkRKGkh_W8d231r4ppKoDYHBiYQ-3iWBOX5lUyGpXSIExXLi5JVn-Ei9ru8tpowNEDe8Msr0hUIHNohhsYuW31Vs13lL8ZIdeMhV3iJ_hh5ScKen2a_KwGQDqMWvFCB_cGVWpSTSMqSAHT-puj_mfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c6ecedd2b.mp4?token=dgkqhOuglU1LGhtE7TDLYI1a8yBhtfUujhKhKdM5W0NvpD6nDCjwMM2seW4B7u2KvAdRPIe7OMYymuxaX0fN1uwf-pAx5IHEgIvKCO35v51-vO1fz4_vDi_AbGutFqzRqsj6D4jkcSSEKYsjCWJzBrfx-zodOU7mREsz6DrpBTk3gFrv1wn-aB70-8SkXi0oTkRKGkh_W8d231r4ppKoDYHBiYQ-3iWBOX5lUyGpXSIExXLi5JVn-Ei9ru8tpowNEDe8Msr0hUIHNohhsYuW31Vs13lL8ZIdeMhV3iJ_hh5ScKen2a_KwGQDqMWvFCB_cGVWpSTSMqSAHT-puj_mfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این آقا یه ویدیو از چینی‌ها گذاشته که یه شیشه‌دودی واسه ماشین ساختن که با یه بیلبیلک میشه درصد دودی بودنش رو کم و زیاد کرد؛
حالا به جای اینکه پشمای ملت از تکنولوژی بریزه، 98 درصد کامنت‌ها اینه:
بهترین مکان واسه اونایی که مکان ندارن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71455" target="_blank">📅 11:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71454">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c4f2b29b.mp4?token=MAlTmJ5O_yOIK_IqWZXGbik1qItIX7t7UlOQZhofHWAtMv5pYdzJ_8wq3CGqOsWz7ClsErb2MhB92tIz0hAmhgeUZXIIk0t-r2Elfhcl3evMgFbiLxsqR8LhV2GKcwwfR-SJYVeCSoScCkANoBG_AwF-NujDijOiY9aK8lOkZblX6FrMYKy1_UVgAFZ_5VJtHeNGg4rvkSNyG3kam3mcmongawFP_n7C3TiDBZ1Yr-DEK203oQ8tKlPJ8J5vzBJWhYnZPB_gcFyH0HzISsxMiVvvPBQlcUJYkfY02KFSngx64NBQillK2IJIWZnhqamECmxlMQ4L3WYJNJh7iI2v8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c4f2b29b.mp4?token=MAlTmJ5O_yOIK_IqWZXGbik1qItIX7t7UlOQZhofHWAtMv5pYdzJ_8wq3CGqOsWz7ClsErb2MhB92tIz0hAmhgeUZXIIk0t-r2Elfhcl3evMgFbiLxsqR8LhV2GKcwwfR-SJYVeCSoScCkANoBG_AwF-NujDijOiY9aK8lOkZblX6FrMYKy1_UVgAFZ_5VJtHeNGg4rvkSNyG3kam3mcmongawFP_n7C3TiDBZ1Yr-DEK203oQ8tKlPJ8J5vzBJWhYnZPB_gcFyH0HzISsxMiVvvPBQlcUJYkfY02KFSngx64NBQillK2IJIWZnhqamECmxlMQ4L3WYJNJh7iI2v8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
از سالن زیبایی مذهبی برای عروسی رونمایی شد، از آپشن‌های خاص این سالن میشه به این موارد اشاره کرد:
رد شدن از زیر قرآن هنگام ورود به سالن.
عکس گرفتن با سران مملکت که کشته شدن.
پخش مداحی و قرآن به جای موزیک.
داشتن وضو توسط پرسنل قبل از میکاپ.
خوندن نماز دسته جمعی برای خوشبختی.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71454" target="_blank">📅 10:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71453">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9e0d9418.mp4?token=tlyBjmBMgPsIsklYbo3XFBMrLjYrCO2fE9otVooe4VfGyID3Ok16f-SZdNZKPV9bKVex9GiiKp-sAX2JwxZQoNlxUgXgxSks2SBxq_zRrugk5KaPCBDhKN8pyfFixXfqSmRbIvSiQRAm06081L42LIcJyUGQhml8QOKUYpchEZdf3WsZVfZuvg1z9wpZf-X_WDQUTKezg1DeW7Rq57ZESPwG-A89tkVVJxm5xPqy3YY4i6QM_HGk3qc6crKTwhHBISJnV--rIb0Vf1g3tDt28WIUpESeutZfilB9Hq0Bkiqfm8pAijFUxNhUYZ8eyrfvG32NnrGe4Vw_Wkzv3pHkpg6anZ-UuSfMkKqnZ0OVHrTdXxYXwmFeDs72UTq8GmeQHHWBwsOjFlKVtby_zIRWvl9zonfJem93J7bmYkqdzOgsq7TQEU-rm3fF47431ak1gPJXdriBlkGxZcorsd-rHTy1cxiATFiaxzmqvUntpQcW7OHN1xIgFJJm8VLR-jav5ZgWyB9mDOFMoZgo9EdvnESP7yxtBv4zBfk4Fvj2DR2BxZMCSdOhsqw2XLdn652IKa_LfzM82eIIVIJxCdkCjabYWneCU8MXQ3sljUzBbNmzBD-MM8I-nh_0iaihD3wXJHS70uufmyPLdMkMIDXY21sApaKNu8hZEB3idfa1TyI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9e0d9418.mp4?token=tlyBjmBMgPsIsklYbo3XFBMrLjYrCO2fE9otVooe4VfGyID3Ok16f-SZdNZKPV9bKVex9GiiKp-sAX2JwxZQoNlxUgXgxSks2SBxq_zRrugk5KaPCBDhKN8pyfFixXfqSmRbIvSiQRAm06081L42LIcJyUGQhml8QOKUYpchEZdf3WsZVfZuvg1z9wpZf-X_WDQUTKezg1DeW7Rq57ZESPwG-A89tkVVJxm5xPqy3YY4i6QM_HGk3qc6crKTwhHBISJnV--rIb0Vf1g3tDt28WIUpESeutZfilB9Hq0Bkiqfm8pAijFUxNhUYZ8eyrfvG32NnrGe4Vw_Wkzv3pHkpg6anZ-UuSfMkKqnZ0OVHrTdXxYXwmFeDs72UTq8GmeQHHWBwsOjFlKVtby_zIRWvl9zonfJem93J7bmYkqdzOgsq7TQEU-rm3fF47431ak1gPJXdriBlkGxZcorsd-rHTy1cxiATFiaxzmqvUntpQcW7OHN1xIgFJJm8VLR-jav5ZgWyB9mDOFMoZgo9EdvnESP7yxtBv4zBfk4Fvj2DR2BxZMCSdOhsqw2XLdn652IKa_LfzM82eIIVIJxCdkCjabYWneCU8MXQ3sljUzBbNmzBD-MM8I-nh_0iaihD3wXJHS70uufmyPLdMkMIDXY21sApaKNu8hZEB3idfa1TyI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر موقع پریود اومده نوار بهداشتی استفاده کنه و با یه صحنه شوکه کننده مواجه شده!
خودتون ببینید...
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71453" target="_blank">📅 10:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71452">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6849173423.mp4?token=VYoar4fApAh5Qms3BQtWIyYts5bAsPcz9LcKlwhzu9shQxoWDs4D4rBytJuCKA7cayD9eQfyMC6K4YqhRcgoeNIO0h3IEC4maEEwH63onar-OkF0XupGxMtnO0kKBkmFrRk5oiCA8nca9eSndWbRyB_9SRYXNNZ93IAtfVPLs1FIPN2nN4-lmfL6mRtjDCadqZS--QBR-Ko5s4w5Rj6jOdnvRQGjqFvcWtaFZutK3mFhdH-8fMBkMajQeAzFUB0TR1YgqzCHeFeHwSUSZWiQLatWweYj_c1iUMzDmpoU6xafdMDw_YyfyhSAnObKFR14y5WqVDZvnX6n3gkHPy7XnE5cAbE8UPn069KbqVQp6ae7pst0VwnADVql-Gtk_KGACSwK4GPbxvv_abIJkt7Ff8q_-OdZ6GY5HWjVyRXuGNFDURvBbi7hF2ip08Tf_gjdnf4sYy29tEovocwlWARavixucTG9VrsTIBuujYx4qGVrWmjwRRizlHxN8PL-U6EYzn7hZpIdJ3C4Ko9sz30C5itgP3Ur69T8BGAMXeutdZklfF_4PQ5ceYU8DboAIZ1MEbwI6hH3btbyuegv8TS7iOLZGcoX9nScsplWQzE0YagBG04HbTh6Hh8s6-Z7HlJxwKXcdTBF2jsrNjMch0h-Rc6twpZw0ir2SjGqqdmDKSE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6849173423.mp4?token=VYoar4fApAh5Qms3BQtWIyYts5bAsPcz9LcKlwhzu9shQxoWDs4D4rBytJuCKA7cayD9eQfyMC6K4YqhRcgoeNIO0h3IEC4maEEwH63onar-OkF0XupGxMtnO0kKBkmFrRk5oiCA8nca9eSndWbRyB_9SRYXNNZ93IAtfVPLs1FIPN2nN4-lmfL6mRtjDCadqZS--QBR-Ko5s4w5Rj6jOdnvRQGjqFvcWtaFZutK3mFhdH-8fMBkMajQeAzFUB0TR1YgqzCHeFeHwSUSZWiQLatWweYj_c1iUMzDmpoU6xafdMDw_YyfyhSAnObKFR14y5WqVDZvnX6n3gkHPy7XnE5cAbE8UPn069KbqVQp6ae7pst0VwnADVql-Gtk_KGACSwK4GPbxvv_abIJkt7Ff8q_-OdZ6GY5HWjVyRXuGNFDURvBbi7hF2ip08Tf_gjdnf4sYy29tEovocwlWARavixucTG9VrsTIBuujYx4qGVrWmjwRRizlHxN8PL-U6EYzn7hZpIdJ3C4Ko9sz30C5itgP3Ur69T8BGAMXeutdZklfF_4PQ5ceYU8DboAIZ1MEbwI6hH3btbyuegv8TS7iOLZGcoX9nScsplWQzE0YagBG04HbTh6Hh8s6-Z7HlJxwKXcdTBF2jsrNjMch0h-Rc6twpZw0ir2SjGqqdmDKSE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
❌
ویدیویی پشم‌ریزون که ارتش اسرائیل از عملیات تخریب تونل‌های زیر ارتفاعات علی‌الطاهر در جنوب لبنان منتشر کرده
😨
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71452" target="_blank">📅 09:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71451">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c57019ecf0.mp4?token=YX9XZ2KJMgRu_PAtBVZONCyZbmUmxsLHwDssR7rFJyHGrCoGHS8SeEWwzCxuhbcYrgZZxQ7gs-U68eyNngLZP0eA5o-FmIwdpwH0qZBzYZhlJHElzPpCtBv_JxKHh--K6ek-0f7XpHKlp5qxFreg1SudfqHRk_VwYR_vJOmwwae2oTZhRyVAbG7AyL0wo9G0zsdz613afOWCAlIWCa3fgYeQL-i3TaJbqGs4iZoGGkWIdlWzfh_Kn6tCoWdJPzFz08n87rfEa6TusekjLE57qKcWeRll9rBwyj3-VuS1CkcU8grBO0rm6_uuhPbLrmyIvz8xe6ua8Pru1DyiB-degw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c57019ecf0.mp4?token=YX9XZ2KJMgRu_PAtBVZONCyZbmUmxsLHwDssR7rFJyHGrCoGHS8SeEWwzCxuhbcYrgZZxQ7gs-U68eyNngLZP0eA5o-FmIwdpwH0qZBzYZhlJHElzPpCtBv_JxKHh--K6ek-0f7XpHKlp5qxFreg1SudfqHRk_VwYR_vJOmwwae2oTZhRyVAbG7AyL0wo9G0zsdz613afOWCAlIWCa3fgYeQL-i3TaJbqGs4iZoGGkWIdlWzfh_Kn6tCoWdJPzFz08n87rfEa6TusekjLE57qKcWeRll9rBwyj3-VuS1CkcU8grBO0rm6_uuhPbLrmyIvz8xe6ua8Pru1DyiB-degw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ:
اگر ایران سلاح هسته‌ای داشت، ما با آن‌ها تماس می‌گرفتیم و می‌گفتیم: «جناب، آیا ممکن است با هم دیداری داشته باشیم؟»
آن‌وقت رفتارمان با آن‌ها بسیار متفاوت می‌بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71451" target="_blank">📅 08:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71450">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534815e8ce.mp4?token=ADb9_CJwDbqXpy_iX0nf0mPCRmdTOWUOvVhSEBZYCZrkWEb59YgFOYn09YhUP9RYALgeRTbU1gCcNj4dJSoqp-RoWUkzNSc79r0Fz1EMJ0kjgsxwkbIq4e0rcurInewnKpB0n3xWlgvaFaF40WnIt3jqtGA8pF-Pj3BiJppbv_BKK1_eKdWLPD94IzD_g2-42mhurA7bLgclbuPSjmyddJChNWfP-cstoehymWrkrBiouGZL-zy0pON6X2OywsOlDblTUL42MFcLZQ-JCI9Bg2tbQvaxUt4kVE6yVsbpMk_0tNqEFw2tAVajdwX_spbmBh5IfeKyOR0oPQU6_jH3KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534815e8ce.mp4?token=ADb9_CJwDbqXpy_iX0nf0mPCRmdTOWUOvVhSEBZYCZrkWEb59YgFOYn09YhUP9RYALgeRTbU1gCcNj4dJSoqp-RoWUkzNSc79r0Fz1EMJ0kjgsxwkbIq4e0rcurInewnKpB0n3xWlgvaFaF40WnIt3jqtGA8pF-Pj3BiJppbv_BKK1_eKdWLPD94IzD_g2-42mhurA7bLgclbuPSjmyddJChNWfP-cstoehymWrkrBiouGZL-zy0pON6X2OywsOlDblTUL42MFcLZQ-JCI9Bg2tbQvaxUt4kVE6yVsbpMk_0tNqEFw2tAVajdwX_spbmBh5IfeKyOR0oPQU6_jH3KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
دیشب ما ۲۲ قایق را از تنگه هرمز بیرون راندیم. می‌دانید، ما کنترل تنگه را در دست داریم. آن‌ها کنترل تنگه را در دست ندارند. آن‌ها هیچ‌چیز را کنترل نمی‌کنند.
آن‌ها تورم ۳۰۰ درصدی دارند. حقوق ارتش خود را نمی‌پردازند. حقوق نیروهای انتظامی‌شان را هم نمی‌دهند.
و بالاخره زمانی فرا می‌رسد که ارتش و نیروهای انتظامی دست از شلیک به معترضان برمی‌دارند. شگفت‌انگیز است که چطور آن‌ها [تاکنون] چنین کاری می‌کنند.
می‌دانید، چین با استفاده از تانک ارتش این کار را با موفقیت انجام داد. یادتان هست؟ کشورهای دیگر نتوانستند. ترکیه نتوانست این کار را بکند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71450" target="_blank">📅 08:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71449">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fa815d3aa.mp4?token=eH7yQJDei_XMGV4bdDdSw6zbiYQvbplUYnk3VIullzLaur0-10uooKlGVcz9rIL2XQikHbeSSAEdITxUXz7fGB94XMClpbABTI7HAJ0bke0NTR3n9t9Rt3EyLsd3y6gd0fEU_t1Q61rF7ySL-iDoiZ_t4N5ydfcxTaewn8Z6vdy49RFKJul4F2c-ISFG4DXSESxX4RCw1YF-HT82XjOMIuY6wUoKm8PZSTlp1s1pQP64KxSMjz0BW3zb8e3Xjq1_AnCm4bSZOEvS3W7JBt4YOmhpy1sEAEf7Hs8qXa_POIcG4zS5Lz_HbcAyEij8uqHI1cWJe47lRSZHXStyHAfg9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fa815d3aa.mp4?token=eH7yQJDei_XMGV4bdDdSw6zbiYQvbplUYnk3VIullzLaur0-10uooKlGVcz9rIL2XQikHbeSSAEdITxUXz7fGB94XMClpbABTI7HAJ0bke0NTR3n9t9Rt3EyLsd3y6gd0fEU_t1Q61rF7ySL-iDoiZ_t4N5ydfcxTaewn8Z6vdy49RFKJul4F2c-ISFG4DXSESxX4RCw1YF-HT82XjOMIuY6wUoKm8PZSTlp1s1pQP64KxSMjz0BW3zb8e3Xjq1_AnCm4bSZOEvS3W7JBt4YOmhpy1sEAEf7Hs8qXa_POIcG4zS5Lz_HbcAyEij8uqHI1cWJe47lRSZHXStyHAfg9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
حتی نومحافظه‌کاران هم می‌گویند اگر قرار است وارد ایران شوید، باید تمام‌عیار وارد شوید؛ فقط بروید و کارشان را تمام کنید.
🇺🇸
ترامپ:
خب، شاید به خاطر انتخابات چنین کاری نکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71449" target="_blank">📅 08:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71448">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2230f2a78e.mp4?token=MGiXWHuFxSCXP_ED4jWJX6GQMfyNbIZUytkYElmynz5jfSzgQTL81IqofyCRPSXF1kjPSelqmlugaV9osmC8LktEax22L5q5SDfydQ_dcGzqRzsGN9UBpCLpdDJZlSF_Yekj0LltMuJZE4KTL0QSWvBlwoL8VVBXelj14vgEwQCLiBm27yycAoSQPh3GTxED9TrqBmlQ02nm6BsTbEwSy_NkXJotV7qemQsAAKo9LD3esXch-GK6UDVC8Lz6OAbY-HbSz8VmLiAD-4BAV-OYd0_VXHZk4wgrUfmCICuP4W_LX8XD-hoD5cWWLH3kztz1b6NACKl8shV17kYlrAqWiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2230f2a78e.mp4?token=MGiXWHuFxSCXP_ED4jWJX6GQMfyNbIZUytkYElmynz5jfSzgQTL81IqofyCRPSXF1kjPSelqmlugaV9osmC8LktEax22L5q5SDfydQ_dcGzqRzsGN9UBpCLpdDJZlSF_Yekj0LltMuJZE4KTL0QSWvBlwoL8VVBXelj14vgEwQCLiBm27yycAoSQPh3GTxED9TrqBmlQ02nm6BsTbEwSy_NkXJotV7qemQsAAKo9LD3esXch-GK6UDVC8Lz6OAbY-HbSz8VmLiAD-4BAV-OYd0_VXHZk4wgrUfmCICuP4W_LX8XD-hoD5cWWLH3kztz1b6NACKl8shV17kYlrAqWiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
اگر ما توان نظامی ایران را درهم کوبیده‌ایم، پس چطور آن‌ها همچنان موشک شلیک می‌کنند؟
🇺🇸
ترامپ:
آن‌ها همیشه می‌توانند موشک شلیک کنند. آن‌ها تعداد زیادی موشک داشتند و هنوز هم تعدادی دارند؛ هرچند بخش عمده‌ای از توانشان نابود شده است.
تولید موشک برایشان دشوار است. بخش اعظم تأسیسات تولیدی آن‌ها از کار افتاده، اما همچنان موشک در اختیار دارند. آن‌ها همیشه تعدادی موشک خواهند داشت، و ما [موشک‌هایشان را] سرنگون کردیم.
آن‌ها ۱۱ موشک به سمت ما شلیک کردند و ما تک‌تک آن‌ها را سرنگون کردیم. البته اجازه دادیم دو تا از آن‌ها رد شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71448" target="_blank">📅 08:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71447">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a731a8039.mp4?token=gS7LGelhAU-_sssbz-dFYMB3MoEk3gw73uCPSKuVZUTx6byq4pftQoBbpnh9Beb2PUdE5BQsnxBKsUCcKyGmA26IsWhNVzB2_WAmJiTvUxu5hxNeJaaOSSiguTm9EiGm1aZvwp68AqH6I8RUNs050AlFaBEp9ZwDBUv8MtyhZh5rVbeVocSLaPdLhJYok-VTzDKQh9OIZV4u9U3fnoHDc_ncF0gAgw2ixyooJTpJCQcCZBvYSfWPq1_q5OBoT_gJusgWjECOqKcVbo6NnQaYF4Wbo1SsoLBhppdL9xSYvhimM6NJEWDzGtCTB-LUnKv5ldvFdc2B7erc3-DxNvpKBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a731a8039.mp4?token=gS7LGelhAU-_sssbz-dFYMB3MoEk3gw73uCPSKuVZUTx6byq4pftQoBbpnh9Beb2PUdE5BQsnxBKsUCcKyGmA26IsWhNVzB2_WAmJiTvUxu5hxNeJaaOSSiguTm9EiGm1aZvwp68AqH6I8RUNs050AlFaBEp9ZwDBUv8MtyhZh5rVbeVocSLaPdLhJYok-VTzDKQh9OIZV4u9U3fnoHDc_ncF0gAgw2ixyooJTpJCQcCZBvYSfWPq1_q5OBoT_gJusgWjECOqKcVbo6NnQaYF4Wbo1SsoLBhppdL9xSYvhimM6NJEWDzGtCTB-LUnKv5ldvFdc2B7erc3-DxNvpKBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
ماجرا درست پس از انتخابات به پایان خواهد رسید.
نمی‌گویم چه زمانی، اما فکر می‌کنم درست بعد از انتخابات تمام می‌شود.
آن‌ها به‌سختی و با لنگ‌لنگان پیش می‌روند؛ در مخمصه‌ای عمیق گرفتار شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71447" target="_blank">📅 08:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71446">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dedfdd2dfa.mp4?token=QHcofGujYe7m8V2B6N0RfqcMaFiASDYGv0z6sl2_eKYFGYTVcEl3Yx8Xy6aKHjGEGrQJ8O4ZL8K1enIKCfDnnCcl1WVIAPxzrsFpLb3YII8mX2dkpJBwIpHEXUktkWEtrHeMtT2Mndkqz99yYTebZa5In5UfFtDO40CDfOcwI0nFVWgr6aNoR9vUJBMMCduqSLLw_TQUXXw5kB5hgBHyJkdBzGZLdyDvrA4EuQmbhQhudbz0mwYuavss3gMujQjD9ogUUwlTd6AWI5DSZ-MUm0VpfbBbaxSdodt7qXbpfNSr8GbG8tturHV2owlTjvjk9SjIa8ORHXj_zomVWKBZLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dedfdd2dfa.mp4?token=QHcofGujYe7m8V2B6N0RfqcMaFiASDYGv0z6sl2_eKYFGYTVcEl3Yx8Xy6aKHjGEGrQJ8O4ZL8K1enIKCfDnnCcl1WVIAPxzrsFpLb3YII8mX2dkpJBwIpHEXUktkWEtrHeMtT2Mndkqz99yYTebZa5In5UfFtDO40CDfOcwI0nFVWgr6aNoR9vUJBMMCduqSLLw_TQUXXw5kB5hgBHyJkdBzGZLdyDvrA4EuQmbhQhudbz0mwYuavss3gMujQjD9ogUUwlTd6AWI5DSZ-MUm0VpfbBbaxSdodt7qXbpfNSr8GbG8tturHV2owlTjvjk9SjIa8ORHXj_zomVWKBZLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
اگر ماجرای ایران پیش نیامده بود، با خیالی آسوده به سمت پیروزی در انتخابات میان‌دوره‌ای پیش می‌رفتید؛ ۲۲۵ [کرسی].» آیا حسرتی دارید؟»
🇺🇸
ترامپ:
«نه، من به واژه "حسرت" اعتقادی ندارم.
آدم همیشه ممکن است کمی به کار خودش شک کند؛ چند نفری هم این سؤال را از من پرسیده‌اند.
اگر قرار بود دوباره آن کار را انجام دهم، دقیقاً همان‌طور عمل می‌کردم. من توانمندی هسته‌ای آن‌ها را از بین بردم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71446" target="_blank">📅 08:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71445">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71445" target="_blank">📅 01:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71444">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Woq7ojaT2qw5-7iOcTFJMKuNhf5xI5CxiQ2-oqtJzAo94BQUrizHfAtEZKEkHLZASrYaxXsZXuoWTczpYlJF1a04YsJSNr2m6qxxHo9jfdEljErjvt93cB6LKIEBjGyTdt1WISlitiGVFu9r-CqY7KVLYAVrHpkQh9MikLFLr8BxJdsiBNB3B6Uw5xagoQRiEIkG2YQajyGfAdqCj_jwm0fJvUGQpxIlljzzZkZ2H-TJg9Sl4HZbiqnTq9GgDt9fIodshmW95uhI0DybvYpvyyWXIMtWgCSX4S3YJ27ZpXjN1lw9ImA_yFHvQNRyrOfvljLDB1dAWRpqITKRRCXaXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71444" target="_blank">📅 01:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71443">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KslBfl14lRd7Rn6kxM3bz-bezPNgYrzC7dEDai-86l1Kbtro5g8_p6VOTQxdTSRQp4152yaQ5Yx_rIFwbRK0sTT4PyEH8pjWDnkr8dKQgqRlORY31ky_JDe6WyArc30wxan-nCcjIqCvPkFlV3DUDBOCkwYg-MHN0-Nx8Um1brg7NsmziyOVCwRN8bAEzno5EaphV8306JuNoln6vpLefrwBmU1m1xZCX4DzTDC3bt23Eiypl713EkWsz0YZuy31XuvPWc7jLtBtPfkOYh36qLONtK2EM42SyUXj6pi7SQOB6L3w3Q3zLWBe4pqJsDq6r_UpccEBDjAULDQn-lSUuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💸
🛢
بهای نفت خام برنت به ۱۰۹ دلار در هر بشکه رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71443" target="_blank">📅 01:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71442">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCkHP86wtQPO_O5yDFhk4cfCaT8bXg9fZ4R0z5KoLQjeU5rxjMHPyCRMfL2bce_Kr9cmug_vt1VEMu2ctb9FohghX6bjGe5NOqUihPpCRx1L18I-MZea71GJhBtBJGqkZhxWDPeUr0z1UhyX0TDdJkGZrdGXsWuPVnsvFKbQiHiKrFRnvFePRd2LSf4693iwOpxo8pjOKaQbAGkPq_W8E1ep_JchVVqOsIHEqJTDHTecgAIWcW0WrROeiT63Uy2kY-Gkvg8pObUzQkFkRN36b6a4F3-aTuHtAqiFiJ6mTzNoUmbe8ZwgiToTsvLNy287pLToXx168acVCtRiHs_DUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
❌
🇸🇦
میدل‌ایست:امروز برای نخستین بار، حوثی ها خط لوله «شرق-غرب» عربستان سعودی را هدف قرار داد؛ خط لوله‌ای که نفت خام را از «ابقیق» به «ینبع» در ساحل دریای سرخ منتقل می‌کند.
تقریباً هم‌زمان و در حوالی ساعت ۱۷:۵۶ به وقت هماهنگ جهانی (UTC)، کانون‌های متعدد آتش‌سوزی در شش نقطه از مسیر این خط لوله شناسایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71442" target="_blank">📅 00:57 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71441">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klm9W0zXcYv_BgStwrIpqZBv6Sit9coQE0QbQNEjpZjR8XOPlVa6K6AGAzMoHB2Qx5OQpbPa-EHyD_goRjz4bhUdRuQYJ8vzVhhTeFGutq_j3Z2xoRaGKiIHqExd7P2PS3APz9XP-Et1hVd833zkwvdyBU6ytVoCBTMLZ0CZH_Yn8ReU7kmpMy8ERKZQ17MyM3WItjG5VyJRmCuqvt3ks9_yICci_S-TYSaXf_4gLMaIukRbbI3MeM_PPk0UayLxIGgyp39O8cDugGD9wqBIw7SnRQLJX_FNmT7WC6dVBAh_mEa_fLwIDlqp9CsXkZ6OCi_es1YOmn1vRPsZvX_6Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
دو شناور در تنگه هرمز، در فاصله ۴ مایل دریایی غرب عمان، هدف قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71441" target="_blank">📅 00:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71440">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⏺
🇮🇱
❌
🇱🇧
ارتش اسرائیل اعلام کرد که برای تخریب زیرساخت‌های تونلی در زیر ارتفاعات «علی طاهر» در جنوب لبنان، بیش از ۱۱۰۰ تن مواد منفجره به کار گرفته شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71440" target="_blank">📅 00:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71439">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae4183a669.mp4?token=Vox7wNW_dHagDpbyzMCaF7_aYPgcdKXAqFqfg1r6FNoMpwI2QLG6U3x9WoVkXoxvFkA2sf1KF0XSaAFER9OCSNbQzgCO1xGVA6YJ82UOz39-UvPveSJFN8wh9wQJhCvmDUiPEURngKiRZSFw28KHVzIKAzllUjbkZD22ZsK2juX28ynePWO3Ylb_A-EW1a_mQMyaFZmoq7LDDRrdMaSRoNHhrWu_Y8xTr8KqFEU5t_S5bf9hKY9Sp2IfcI00DimDfO4jSZLc5wz4gRWdDyAfwQfNN9Eywqj74j9OVDnsTlr-nVzq-6WrHYX0inevy1K8-OOpzDqll8qgjJkaFx2gUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae4183a669.mp4?token=Vox7wNW_dHagDpbyzMCaF7_aYPgcdKXAqFqfg1r6FNoMpwI2QLG6U3x9WoVkXoxvFkA2sf1KF0XSaAFER9OCSNbQzgCO1xGVA6YJ82UOz39-UvPveSJFN8wh9wQJhCvmDUiPEURngKiRZSFw28KHVzIKAzllUjbkZD22ZsK2juX28ynePWO3Ylb_A-EW1a_mQMyaFZmoq7LDDRrdMaSRoNHhrWu_Y8xTr8KqFEU5t_S5bf9hKY9Sp2IfcI00DimDfO4jSZLc5wz4gRWdDyAfwQfNN9Eywqj74j9OVDnsTlr-nVzq-6WrHYX0inevy1K8-OOpzDqll8qgjJkaFx2gUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئو دیگر از تخریب کامل پایگاه عماد ۴ حزب‌الله
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/71439" target="_blank">📅 00:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71437">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4770f428.mp4?token=tgeqAqum6QXrWQasPBzlpbUvHXzAcXnbs5UZlzPczYb2btQfjZs0bx0COSzMDqMMycsLUV5-E_A1uxXQKh1PnUDT-vxi-JGD4A2nLR1neQBaT6cTgsemircFbSA48BF4kmQPG9jNqv7xRfv3qZSvC_PyDVcAzqJAo4XKgNA6Sj2TcmsXWzkCuDyByjsWsELXQYetl1G-MOHhEjRR0VsZ2Z18p7vDRirNth-qEfTfiaPm9bpLnqhm2h_96yxm1HY_f_uxYhq7p8AyNBjeU9defGddc57vG2rcKfr_Anpy7Eyj7dkSwczmdWWctcOsBgC4hLL5BbSbCo-p5ZNO_sWInQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4770f428.mp4?token=tgeqAqum6QXrWQasPBzlpbUvHXzAcXnbs5UZlzPczYb2btQfjZs0bx0COSzMDqMMycsLUV5-E_A1uxXQKh1PnUDT-vxi-JGD4A2nLR1neQBaT6cTgsemircFbSA48BF4kmQPG9jNqv7xRfv3qZSvC_PyDVcAzqJAo4XKgNA6Sj2TcmsXWzkCuDyByjsWsELXQYetl1G-MOHhEjRR0VsZ2Z18p7vDRirNth-qEfTfiaPm9bpLnqhm2h_96yxm1HY_f_uxYhq7p8AyNBjeU9defGddc57vG2rcKfr_Anpy7Eyj7dkSwczmdWWctcOsBgC4hLL5BbSbCo-p5ZNO_sWInQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
#فوری
؛ارتش اسرائیل عملیات تخریب تونل های زیر ارتفاعات علی الطاهر را شروع کرد.
تصاویری که لحظه انفجار تونل‌های زیر «ارتفاعات علی‌الطاهر» در جنوب لبنان توسط نیروهای اسرائیلی را در همین لحظات پیش نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71437" target="_blank">📅 22:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71436">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249279a367.mp4?token=HZcVENjAHW8D91Q2_8_SBi2_YFggimWTAJjIJ6aDvHYfkEXrxCTjyoZKJYbxkc_qxGrENz3eOHS_zzPe7Vs5GZpL8RB7prZctw59LoLXFkfrQWr8874XDu2tl8J6icALtezYi63vaMI3h-7UVJYjOrGiuBy8m-O549KECShsqeJsc9FlAxedVPZVd5zJhKYiC3z-6MinsXD-XSZuZu4VP7si1UKXiunaylUmgg4UhGuLte1lzve0WNJPLu6kMLAAC-UBFdNel-a1VVfYfMvE1pAN95cq-M-JD4Wy5i8lKOUO07-9Vi4rJA8cJXcNY_RJN2xXLi5ZC5WSbrqyOMqOtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249279a367.mp4?token=HZcVENjAHW8D91Q2_8_SBi2_YFggimWTAJjIJ6aDvHYfkEXrxCTjyoZKJYbxkc_qxGrENz3eOHS_zzPe7Vs5GZpL8RB7prZctw59LoLXFkfrQWr8874XDu2tl8J6icALtezYi63vaMI3h-7UVJYjOrGiuBy8m-O549KECShsqeJsc9FlAxedVPZVd5zJhKYiC3z-6MinsXD-XSZuZu4VP7si1UKXiunaylUmgg4UhGuLte1lzve0WNJPLu6kMLAAC-UBFdNel-a1VVfYfMvE1pAN95cq-M-JD4Wy5i8lKOUO07-9Vi4rJA8cJXcNY_RJN2xXLi5ZC5WSbrqyOMqOtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
#فوری
؛نخست‌وزیر نتانیاهو درباره ایران:
رئیس‌جمهور ترامپ امشب اعلام کرد که ایران بار دیگر در تلاش است تا به سلاح‌های هسته‌ای مجهز شود. این سخن درست است.
پس از آنکه ما توانایی فوری آن‌ها برای تولید بمب‌های هسته‌ای را از بین بردیم، آن‌ها دوباره دست به کار شده‌اند.
من اینجا، در کنار «دیوار ندبه» و در آستانه «روش هشانا» (سال نو یهودی) به شما قول می‌دهم: تا زمانی که من نخست‌وزیر هستم، ایران به سلاح هسته‌ای دست نخواهد یافت.
هم‌زمان، ما در حال ضربه زدن به محور ایران هستیم؛ نه تنها ضربات سنگین در نوار غزه، بلکه در لبنان نیز. ما ارتفاعات «بوفورت» را درهم کوبیدیم و اکنون در حال نبرد بر سر ارتفاعات «علی طاهر» هستیم.
اقدامات بیشتری در راه است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71436" target="_blank">📅 22:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71435">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یه بوهایی میاد، مثل اینکه آماده دارن آماده می‌شن تا دوباره مراکز هسته‌ای ج.ا رو بزنن
#hjAly‌</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71435" target="_blank">📅 21:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71433">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQm_4RHSky-11Y0TWmWxFtMSn0cmTUuO9iJBSc4OFiWeoIHddWmMQKbWqAqYwY8wjc-s7874AoZ3juqlGsMXZLn1-_DhbIvHThzpNBAEialv-izUH4qIdluqiMbAk1xoSwx9pcSPmZTuiQa4FWKxPhHsu-ZH2XdzD3MDgkAeyZjsCIdszKcJwhXaeXGtXTtfBNIPhayZA_XE7a1jOZ5Gv7of4hA10tR11GPnbCo1KmujNzrF9_HndnXyzXLMuySsmM5g2JRFjFFyQX_Q_aeokgsXQEZMJozKOUGorUOUwrFH_Cd86BopgihiWHDkDCGoU0djCrI7jcVsiMJMDEXSQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d882666df.mp4?token=X79xYNDWIATmMt_KqsOncvFeNlskSN_D18o57eymvqowhADg45ISYaUxhxSZYtMMgviNL6wXlaXwg2Z71S3F5jp3ix7U4sUqnnlU44jcr9mpsw89kueSJCenMep2kVniL9n9bSZONazt3gj8u-nJ0Sw2ivAZicz6jeiGHKHtJ54-gq9SLF8AiKYi2omSYXntAhPt6ktAYX8u4ITx7PSo499VqEIUb0h84ke0Gt_9qwZYxGLXvJEjcnTMULHysQpvSgPszgoeYZzy8MemC6A2r8jbwpyhOJ8ZpMMHrJ7O2Dk1QyqHnDLG03_CdBjPw_RY3XGuE5qNETcBaaRUBM10Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d882666df.mp4?token=X79xYNDWIATmMt_KqsOncvFeNlskSN_D18o57eymvqowhADg45ISYaUxhxSZYtMMgviNL6wXlaXwg2Z71S3F5jp3ix7U4sUqnnlU44jcr9mpsw89kueSJCenMep2kVniL9n9bSZONazt3gj8u-nJ0Sw2ivAZicz6jeiGHKHtJ54-gq9SLF8AiKYi2omSYXntAhPt6ktAYX8u4ITx7PSo499VqEIUb0h84ke0Gt_9qwZYxGLXvJEjcnTMULHysQpvSgPszgoeYZzy8MemC6A2r8jbwpyhOJ8ZpMMHrJ7O2Dk1QyqHnDLG03_CdBjPw_RY3XGuE5qNETcBaaRUBM10Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه پاسداران انقلاب اسلامی  اعلام کرد که یک فروند «سیل‌درون» (Saildrone) — یک شناور سطحی بدون سرنشین (USV) که برای نظارت و شناسایی دریایی به کار می‌رود — را در ورودی تنگه هرمز هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71433" target="_blank">📅 20:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71432">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
بلومبرگ:
آژانس بین‌المللی انرژی اتمی می‌گوید فعالیت‌های جدیدی را در سایت بسیار مستحکم کوه پیکاکس ایران شناسایی کرده است، اما هنوز هیچ مدرکی مبنی بر آنچه در داخل این مجتمع زیرزمینی اتفاق می‌افتد، ندارد.
رافائل گروسی، رئیس آژانس بین‌المللی انرژی اتمی، گفت بازرسان به این سایت دسترسی پیدا نکرده‌اند و به تصاویر از راه دور متکی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71432" target="_blank">📅 19:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71431">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ebe5e9d2.mp4?token=NwuU1WjRifU1LodnN3rsX-FeP1N7ITUQFtRuFL3raK6qB5hehUXmo_yknodaMVUctX3dMaY20iM6WeKO6nRPSp_H2xX_OO5Da5xky6eQvP_GyBy_vpDKhZ-yQy6xTwon1tFcL69zJWLlJodEB9en8XULbO3FJPBBssrPZ715kiH9fRa18dMHFN2B10N4TuGcKa9wTPtApVOpw_u73fVVYJ0MUyN0-__o3S3fsCF-CS-Naxnifq-GARQcl1rpWhCKqjhUPHBMnbeC5KyjJ9Ip6kW8YPcKpKdkn39Cw1E4pf-crLY0Eey8-pKg1e2Bz3n3J-EnB8de8i_lb06Axn5Q7UEKrUbLtWjYsBOERR9Wj9UxPvXZzGlPKOFnLw0taxFmXy3XMzvigPdWJEaLUWqP1UWuh9PcyN_3a2ZuhXxMPYSiGmqDHzQNFV6gu9CFfYe2LGHHt9v84ukAgFMDNCuYIuMN52UG6OW0lrB5GEbNM-EXXFN2BR9eWP7rAlK-RcKpuFLA2MqR1VRFTCEOyehldXKTt6BteW56Lv6m_A67Rmekc3sV7FAHMADMyBbyB61M6NPa5UrIK3AmEIZxproo65gW_qAm8-iZ_zcOg0yjY0VzrvOI3p4UyNMOKJkbTwBb5DUGFh_L3vElk-pPHJtT5V98WYGs2KX3bfhzVPx0uA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ebe5e9d2.mp4?token=NwuU1WjRifU1LodnN3rsX-FeP1N7ITUQFtRuFL3raK6qB5hehUXmo_yknodaMVUctX3dMaY20iM6WeKO6nRPSp_H2xX_OO5Da5xky6eQvP_GyBy_vpDKhZ-yQy6xTwon1tFcL69zJWLlJodEB9en8XULbO3FJPBBssrPZ715kiH9fRa18dMHFN2B10N4TuGcKa9wTPtApVOpw_u73fVVYJ0MUyN0-__o3S3fsCF-CS-Naxnifq-GARQcl1rpWhCKqjhUPHBMnbeC5KyjJ9Ip6kW8YPcKpKdkn39Cw1E4pf-crLY0Eey8-pKg1e2Bz3n3J-EnB8de8i_lb06Axn5Q7UEKrUbLtWjYsBOERR9Wj9UxPvXZzGlPKOFnLw0taxFmXy3XMzvigPdWJEaLUWqP1UWuh9PcyN_3a2ZuhXxMPYSiGmqDHzQNFV6gu9CFfYe2LGHHt9v84ukAgFMDNCuYIuMN52UG6OW0lrB5GEbNM-EXXFN2BR9eWP7rAlK-RcKpuFLA2MqR1VRFTCEOyehldXKTt6BteW56Lv6m_A67Rmekc3sV7FAHMADMyBbyB61M6NPa5UrIK3AmEIZxproo65gW_qAm8-iZ_zcOg0yjY0VzrvOI3p4UyNMOKJkbTwBb5DUGFh_L3vElk-pPHJtT5V98WYGs2KX3bfhzVPx0uA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جورج دبلیو بوش درباره افغانستان:
این باور وجود دارد که همه خواهان آزادی هستند؛ و ما این را در افغانستان دیدیم.
برخی می‌گفتند: «خب، آن‌ها نمی‌خواهند آزاد باشند؛ آن‌ها... می‌دانید، اصلاً تفاوت را نمی‌دانند.»
البته که آن‌ها تفاوت را می‌دانند.
دختران جوانی که برای نخستین بار در زندگی‌شان به مدرسه می‌رفتند، تفاوت را درک می‌کردند. زنانی که پزشک و استاد دانشگاه می‌شدند، تفاوت میان یک جامعه آزاد و یک جامعه استبدادی را می‌دانند.
و متأسفانه، آن زنانی که در مسیر شکوفایی کامل استعدادهایشان گام برداشته بودند، دیگر فرصتی برای تحقق آن پتانسیل کامل ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71431" target="_blank">📅 19:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71430">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71430" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71430" target="_blank">📅 19:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71429">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6KIq55bbZFVLSNMa9WCqQqBWac-6aBFIu_yAMTZD4Ewyk_g2GfGUIvD32fPVXKEKOIVwffuF-vwX_vHVGy7pY6B228cNUJ-2d3TGMyl6i7x0ocEEGZ37U8AVORj9QSf6aFHteKjIrZJKz7u97x0rhxrX2aYuqF4S3TdJC9P5iAUOcyU9cyThmVQr0FOBcPSlOjqYQKfzNhVTyfpsp1BNfWr1fTVvcCjAnjOg3lMP8x-_B57QamhdYF6OD5WYVd1kQYAqL68arEA6pVR3R3NI3VxsALeGxCt01EcgrdnlH5qGzzk0uVK7UiQ8DgQp-ZI0hhhqn7IoY3lMQk_Wv4NUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فوتبال اروپا امشب دیدنی‌تر از همیشه!
🦖
بازی جذاب صباح
🆚
منچستریونایتد را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار ۲ تیم در تقابل‌‌های اخیر:
صباح: ۵ بازی, ۴ برد, ۱ شکست و ۱۳ گل زده
منچستریونایتد: ۵ بازی, ۱ برد, ۲ تساوی, ۲ شکست و ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71429" target="_blank">📅 19:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71427">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd5897a7d3.mp4?token=S7DgOYmXTqDKhfZL4bhJXvbNKE4OVFCQ2PTa9sB-I4BRLZnM9IjCHlL6wAZEZxIsmRTyvKlydW9GT0Lf6z1Gu-Gd7fEoqFUJNfhzXzQQISaAAdsPdqHdxta9d1V89Siap1DiJfjnWaHL3au1AoRs-zGbtA7fq-HNc5GICmtuw2Y9lWlYdASj0AewTeE7_6pbUHGktSzulfBL9NA_5YVohobUZZeP7WDrNMnJN1ipYylHCfcVkvvPXk4lIvsAfwgxtzAnz2dtyAv_WYo8sLpmv9hcAR0UOMpFIEmVITDflUymZUcMBTr6tQBJGLP1sMi9R00adDrk7BOY1IuWGGvBgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd5897a7d3.mp4?token=S7DgOYmXTqDKhfZL4bhJXvbNKE4OVFCQ2PTa9sB-I4BRLZnM9IjCHlL6wAZEZxIsmRTyvKlydW9GT0Lf6z1Gu-Gd7fEoqFUJNfhzXzQQISaAAdsPdqHdxta9d1V89Siap1DiJfjnWaHL3au1AoRs-zGbtA7fq-HNc5GICmtuw2Y9lWlYdASj0AewTeE7_6pbUHGktSzulfBL9NA_5YVohobUZZeP7WDrNMnJN1ipYylHCfcVkvvPXk4lIvsAfwgxtzAnz2dtyAv_WYo8sLpmv9hcAR0UOMpFIEmVITDflUymZUcMBTr6tQBJGLP1sMi9R00adDrk7BOY1IuWGGvBgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇾🇪
تنش‌ها میان نیروهای تحت حمایت عربستان سعودی — یعنی «نیروهای ملی» (NRF) و «نیروهای امنیتی ملی» (NSF) — و نیروهای جنوب یمن که پیش‌تر وابسته به تشکیلات جدایی‌طلبِ منحل‌شده‌ی «شورای انتقالی جنوب» (STC) بودند، رو به افزایش است.
فرماندهان جنوب یمن مسیر عقب‌نشینی نیروهای NRF و NSF را در کریدور جنوب‌غربی «عدن-لحج-تعز» مسدود کرده و از ورود این «نیروهای شمال یمن» — که کاملاً مسلح هستند — به قلمرو جنوب جلوگیری می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71427" target="_blank">📅 19:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71426">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMvefKq6vxQgBLG358GAl64FhmIp1qeJXGPhsgrflNmxho3luU5kxgldq-yrMmivr2wqOuDzTHmcLVjptzAesVaE_0hUqf5pMuIPsLfDR64_rd6TEZcq-cmYbJzWPh6mn7dscJ6gW5dvoKUHokYLHM_RNDsdAs1KKTOitGlNcJodXDr2FxmF_vTCQPvfKjEEZsz12lAJ9aJ_7POrnnaAH16u38WeyPidGE0XhKqMMq4zm3PfxfJkY1E0wlYOXbgBOgNxPxEeIixarjNvs-85NKj911f55l50ea2XPV17ygk2xfMX2DiXG6FIKAMwW7fbGW8Hqco08vv-W425lIvR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇨🇳
🗞
به گزارش رویترز، ایران از یک سازوکار محرمانه و شبیه به تهاتر برای تبدیل درآمدهای نفتی به اعتبار جهت خرید کالاهای چینی استفاده کرده است؛ اقدامی که به تهران در دور زدن تحریم‌ها کمک می‌کند.
طی سال گذشته، مبلغی بین ۲ تا ۲.۵ میلیارد دلار از طریق یک «سازوکار ویژه» (SPV) جابه‌جا شده و صرف خرید اقلامی همچون دارو، وسایل نقلیه، تجهیزات مخابراتی و — دست‌کم در یک مورد — تجهیزات پدافند هوایی به ارزش میلیون‌ها دلار شده است.
این سیستم شامل نهادهای مرتبط با چین و ایران است که مدیریت درآمدهای نفتی را بر عهده دارند؛ بدین ترتیب که حدود ۷۰ درصد از وجوهِ تحت مدیریت شرکت چینی «چو‌شین» (ChuXin) به پروژه‌های زیرساختی اختصاص می‌یابد و مابقی آن برای پرداخت به تأمین‌کنندگان چینی، به آن سازوکار ویژه (SPV) منتقل می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71426" target="_blank">📅 19:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71425">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🍏
اپل از نخستین گوشی هوشمند تاشوی خود با نام «آیفون دو» (iPhone Duo) رونمایی کرد.
این گوشی در حالت بازشده، باریک‌ترین آیفون ساخته‌شده تا به امروز است و نمایشگری ۵۰ درصد بزرگ‌تر از آیفون ۱۸ پرو مکس (که به‌تازگی معرفی شده) دارد.
قیمت مدل ۲۵۶ گیگابایتی آن ۱۹۹۹ دلار تعیین شده و عرضه آن از ۲۳ اکتبر آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71425" target="_blank">📅 18:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71424">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KqmiNuZa_dJQyz1nWIpeX2DwkhXDLF7Tc8xtnfFUj0we4DvN5-WLLcDB-W7AEWAlInYzAdThsm_gZUtuv6IhiORe3hDurVfeLouBRZw5AnfWsxQHp64uBJywNZC8eP9ov0-95CxBIFnbJBc9_IlsTgopYeXC38IEMhs6hzUjILk0H2YULqsbXaq86rNS6JjzjbT1NmUz9WnBZE_gSnkoW-ZLuo80EEd4aQXv7GD0-6nbu_EBp656761tU2wkaVnkXzCCZxHHxDgxjsa8L47S-jsYJF4A_nTxaLZh9hMGDEGhwIqjfbZ6pbsvFAgTc6QgyjpXGkTylsFBSuOWgZ-HYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروط عجیب پدر عروس برای ازدواج
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71424" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71422">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQHDEfkY9bWd9_QRyy5zG0xi-rBnH5-cj3w6mWcelOolgj2aSvD86o9EWq_yBvDbYt1xn7T6Ey3FS6k2iLxLW6vJFM7_YEjEAkn2zPzd1hroQaouw-6NY3fxfRsChmttGhGMaoaoWOBxi8fd2jaKtfPTSZYazaRuSw4yoPYGoScWFxygZ_1_zvhF7u_HrbnpZOhxxvaz43o3e7ScJplpwm0WTJhr9dbmb7wQ6IIDP_th25_fts08qC-7NQ3faoUZmVBx_U2MRe47ayE9lTzJnTAhqW3X3_Bs8M2h9GXsx2grmA8jGQ5EdkAmprm5iLipqqrblqep94opKd1kUwfTLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dfa56bc26.mp4?token=YMdbPyY-Jnpi0J4D0UZFdrRmBaAeXgI2gWxuZLh2rGp9WrH9QLHEGnwGxhcJKvcDt9POcEE5A8BxT4JTle2LtVelsq3MaVEHO3pZ45Fc80H8yAi4FTQhnfm6iGSwRAhq5h2qkBPZbtsdaLkLcYei7i_Q2DZ6pNeh6S7-RUOCw1QgbKlgxfncCfeBBMmcqe6t9pWgwhMt8NoeMzvoqkf2hgtZRJexMB39XpA12UPLRZj3yB5DAy-CWMyT7ofk0LMee8m40nTqOdm1lHaYaYzcpOMyWJBaZEVI6425AUKMTJbisog7R9G2kU4Y-hi9phasDb2Pl82RyWxpl8NXQvJFLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dfa56bc26.mp4?token=YMdbPyY-Jnpi0J4D0UZFdrRmBaAeXgI2gWxuZLh2rGp9WrH9QLHEGnwGxhcJKvcDt9POcEE5A8BxT4JTle2LtVelsq3MaVEHO3pZ45Fc80H8yAi4FTQhnfm6iGSwRAhq5h2qkBPZbtsdaLkLcYei7i_Q2DZ6pNeh6S7-RUOCw1QgbKlgxfncCfeBBMmcqe6t9pWgwhMt8NoeMzvoqkf2hgtZRJexMB39XpA12UPLRZj3yB5DAy-CWMyT7ofk0LMee8m40nTqOdm1lHaYaYzcpOMyWJBaZEVI6425AUKMTJbisog7R9G2kU4Y-hi9phasDb2Pl82RyWxpl8NXQvJFLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
⁉️
به گفته تحلیلگران CSIS، تصاویر ماهواره‌ای امسال «افزایش آشکار فعالیت‌های ساختمانی» را در کوه عمیقاً مدفون پیکساکس (Pickaxe Mountain)ایران نشان می‌دهد.
آنها ارزیابی می‌کنند که این سایت پوشیده از گرانیت «احتمالاً» به عنوان مکانی محافظت‌شده برای کارهای مرتبط با هسته‌ای، احتمالاً محل مونتاژ سانتریفیوژ، غنی‌سازی اورانیوم یا سایر فعالیت‌های «مرتبط با سلاح‌های هسته‌ای» در نظر گرفته شده است.
این تحلیل افزایش فعالیت جاده‌ای، ورودی‌های تونل تقویت‌شده و مرتفع، جاده‌های داخلی آسفالت‌شده و سایر کارها را نشان می‌دهد که نشان می‌دهد ساخت‌وساز از حفاری به سمت توسعه داخلی تغییر کرده است.
اطلاعات اسرائیل حاکی از آن است که ایران می‌تواند سانتریفیوژها را به آنجا منتقل کند، در حالی که ترامپ اخیراً هشدار داده است: «ما ممکن است خیلی زود پیکساکس را بزنیم» و افزود: «ما همه کسانی را که در حال حرکت هستند می‌شناسیم.»
پیکساکس حتی برای سنگین‌ترین بمب‌های متعارف سنگرشکن پنتاگون نیز بسیار عمیق دفن شده است. سی‌ان‌ان گزارش می‌دهد که ایالات متحده برنامه‌های حمله عملیاتی برای این تأسیسات دارد و به مطالعه راه‌هایی برای حمله به سایت‌های عمیقاً مدفون ایران ادامه داده است.
چند روز قبل از شروع جنگ ایران، پنتاگون همچنین یک قرارداد اضطراری ۱.۲ میلیون دلاری برای آماده‌سازی در یک مرکز آزمایش زیرزمینی گرانیتی در محدوده موشکی وایت سندز (White Sands Missile Range) صادر کرد. منابع به سی‌ان‌ان گفتند که این کار با توسعه و آزمایش قابلیت‌ها علیه عمیق‌ترین تأسیسات زیرزمینی ایران مرتبط بوده است.
ارتش به‌طور جداگانه در حال توسعه یک «نسل بعدی نفوذگر» است تا جایگزین نفوذگر مهمات عظیم مورد استفاده علیه سایت‌های هسته‌ای ایران در طول عملیات میدنایت هامر (Midnight Hammer) در سال ۲۰۲۵ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71422" target="_blank">📅 17:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71421">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8709946e.mp4?token=eqkVWpdHyErn4K0Jc3Gj4XhpJ8wjzj06UJRJtDjoENyaDVRPrHujUkfMNu9Ji_U2u7uKd2ErvRwgU8NxV5PkJthsI2OBNOHJ1hyLUxIbocRfLoPU-uWIFsU2AGF36D_Su5MTYv7XSEUkHmr5auahZQonx64bWw8C9-0SDNZpqykirGaGD10-tG-EK1y9VY_OWf1bVh4SGK3Oy_DT0N40ufm5TccryurUNlxgol3SzXM-fvnHuiSbS4a_6oNJuSfl3OjAr8YKHfpA_qjNPYsT5efZvMnExNSa51OLlerPo6cdIpWzYw4wJBrKpUqvO_sIVcPUHk0G9NcxeGo6-VLcpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8709946e.mp4?token=eqkVWpdHyErn4K0Jc3Gj4XhpJ8wjzj06UJRJtDjoENyaDVRPrHujUkfMNu9Ji_U2u7uKd2ErvRwgU8NxV5PkJthsI2OBNOHJ1hyLUxIbocRfLoPU-uWIFsU2AGF36D_Su5MTYv7XSEUkHmr5auahZQonx64bWw8C9-0SDNZpqykirGaGD10-tG-EK1y9VY_OWf1bVh4SGK3Oy_DT0N40ufm5TccryurUNlxgol3SzXM-fvnHuiSbS4a_6oNJuSfl3OjAr8YKHfpA_qjNPYsT5efZvMnExNSa51OLlerPo6cdIpWzYw4wJBrKpUqvO_sIVcPUHk0G9NcxeGo6-VLcpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
عباسی معاون وزیر راه و شهرسازی دولت سیزدهم:
آقای رئیس‌جمهور!
مگه نمی‌گید هرکی می‌تونه کار کنه بیاد؟
من می‌تونم
کجا بیام؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71421" target="_blank">📅 16:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71420">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aea684770.mp4?token=SsxQB4BCsJG8oUjXtRc9W7c-MFheI9J-479SblxB_x4grgXtDrdGDM0G0pej2eTEWFbLVDuVUGvBt3OEFnRU9ufHUqzFZN55xQkf55srUb3KHKvFMNpNEWsTCCEhl12u1mQoJ6uOl67Rql3_7FVNwFl_e6ywnuCjoPoxIUa1j2IXjwfjfGX6vGkVrjIqEucUZR_NdJt5O_QXUezfm4riCb5Ngv4sHQmTSQoRZSZvKMLl5D5fDf4yADYWhhOKbHYm_i1kXWE_JlOJOQW2DtnL4A2H6jzxIDKUOZ-IwdMxgNQfqJBsUXz8Lp_Nie7BrmIE9_AcfmJHVFmaRnNbJU5LVTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aea684770.mp4?token=SsxQB4BCsJG8oUjXtRc9W7c-MFheI9J-479SblxB_x4grgXtDrdGDM0G0pej2eTEWFbLVDuVUGvBt3OEFnRU9ufHUqzFZN55xQkf55srUb3KHKvFMNpNEWsTCCEhl12u1mQoJ6uOl67Rql3_7FVNwFl_e6ywnuCjoPoxIUa1j2IXjwfjfGX6vGkVrjIqEucUZR_NdJt5O_QXUezfm4riCb5Ngv4sHQmTSQoRZSZvKMLl5D5fDf4yADYWhhOKbHYm_i1kXWE_JlOJOQW2DtnL4A2H6jzxIDKUOZ-IwdMxgNQfqJBsUXz8Lp_Nie7BrmIE9_AcfmJHVFmaRnNbJU5LVTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
حامیان حکومت این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین، دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، ذلت نمی‌پذیریم.
بنزین رو کم میگیریم، ذلت نمی‌پذیریم.
دلاری گوشت میگیریم، ذلت نمی‌پذیریم.
مهریه کم میگیریم، ذلت نمی پذیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71420" target="_blank">📅 16:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71419">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1669b7ca35.mp4?token=uRbGEoSJJnhxIMq4P9jzybtdkZoGmo_cQ_nhC5u59fo7ccmw5mZVHwimeYFrJK7wNusEzXrn7_3a5q1TYlZmbrrBFE8ibqeXRVnJG4OdDwBU-TEFsaErzOdkK7SjHDtRp4u8VBaikeujhal-quaJnhIHft6zOhEGC_fLNuiO8YYNjOHwTcBHOg5EuEPhPIlYF-PDpo-kLrthNQe5EEDm0IG381NcWfsoBRB5pju9ArDaErnIT_fe7K4sQ4O93PrUErGpHLkaddn3SWVHe8TD-DV3W0p-uYlkspl7ycyBO1BOxtFdvcHSo42Ev2OEkEiMRvm4h2i-rxOx2rjAtnQS6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1669b7ca35.mp4?token=uRbGEoSJJnhxIMq4P9jzybtdkZoGmo_cQ_nhC5u59fo7ccmw5mZVHwimeYFrJK7wNusEzXrn7_3a5q1TYlZmbrrBFE8ibqeXRVnJG4OdDwBU-TEFsaErzOdkK7SjHDtRp4u8VBaikeujhal-quaJnhIHft6zOhEGC_fLNuiO8YYNjOHwTcBHOg5EuEPhPIlYF-PDpo-kLrthNQe5EEDm0IG381NcWfsoBRB5pju9ArDaErnIT_fe7K4sQ4O93PrUErGpHLkaddn3SWVHe8TD-DV3W0p-uYlkspl7ycyBO1BOxtFdvcHSo42Ev2OEkEiMRvm4h2i-rxOx2rjAtnQS6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رقابت رژیم جمهوری اسلامی با اپستین در کثیف بودن:
یه مرد ۴۲ ساله دختر ۱۴ ساله رو به عنوان زن سوم صیغه کرده، بچه حامله‌ست است و داره سزارین میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71419" target="_blank">📅 15:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71417">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97f71ba05.mp4?token=silcZ4_OsEBD8I0lgSr2vAHTw_P6u8IxQdyb7Qw4hURGYH1RnSvHqFJwCm3xpI5OVjNwx4vDDAtDxV-MV27hQ4lRxyRqJIQkjNTtsiWn6g9WnzOnm2aE4BTNxSTpVLBcIJdWWuecXZh8qDrUf-D4SbX05SQKv3zvqkxzFeGKxo7EWlilJSBysSM8s-6Lcleh_pQPPDLClNyJMwHoMAnOqCfyPL0nJiC82cJEC3gOhMsJ-17sVT7AFTx4wJozAXRvmmy-98BksSH0Z-ekIU68gFH2lENpSGvj6w2t5nkYp6MhlMYtEdYat6Fw3qSLpn0qvvlZ8n_NrRro04s2xZ4xDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97f71ba05.mp4?token=silcZ4_OsEBD8I0lgSr2vAHTw_P6u8IxQdyb7Qw4hURGYH1RnSvHqFJwCm3xpI5OVjNwx4vDDAtDxV-MV27hQ4lRxyRqJIQkjNTtsiWn6g9WnzOnm2aE4BTNxSTpVLBcIJdWWuecXZh8qDrUf-D4SbX05SQKv3zvqkxzFeGKxo7EWlilJSBysSM8s-6Lcleh_pQPPDLClNyJMwHoMAnOqCfyPL0nJiC82cJEC3gOhMsJ-17sVT7AFTx4wJozAXRvmmy-98BksSH0Z-ekIU68gFH2lENpSGvj6w2t5nkYp6MhlMYtEdYat6Fw3qSLpn0qvvlZ8n_NrRro04s2xZ4xDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از مراسم ازدواج فوق لاکچری «سامان گوران» بازیگر؛ کمدین و مجری صداوسیما
سامان گوران ۲۶ مرداد ۱۴۰۴ در صداوسیما: نتانیاهو از موتوری جنس میگیره که میگه برنده جنگ شده. نمیزاریم آب خوش از گلوی اسرائیلیا پایین بره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71417" target="_blank">📅 15:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71413">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/klroeIAuebiZH35XgkGKMUtH-1RuixqVQ5K7i2PinviKQXdneO-64YmdyiSC9wAFvp3OmLkaqPgDvHIQRin2rM0716TBaCHiCuh1pQF-IrE074lwzEpypO08X327HJQWiHW1S24YZAOuB_aagyknEkH9cZb3ko5lBe8ZbjzMykMqqMQWNlppsoKM-GOt90BasT6ISURhzG8RQqMllFgaHCP6EoAVzWzMuF-zoyFVSH0CSZt3ZUWODymFAmU6bavd85a4rUdmJKOmjXs9wkjMUWlh5lX8oSFu64jRFTCt0LCgydmfuk294BdiHpBcu1uGdkPUdzyibSYVnslaNhOMxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a27Tj3v1DgLGC1TCnaP8IsTlzLY_QtLMr-jfjNPEjKG78HGXiQx_4Gn0YHAc4l5ray_GylHexmCKPSIIcMJij0BL3iFMAK8lfPxd0fKIsaDeGRqNt-ianLibWuo-AKCfLJ0o0hCjYcowQ3GJxHariOziDyhEdPJb_ul315IYzeMExBNeyxRO6lcEeb2q0r6gdB1cerUShSdsRm-A5rrkWPv7m5TZYXw--M39tYmfL8Etvri7sCHUjGNTLkMY3cpmSDHgnSrzoZSM4V2mDvuNHmrfgV2DLeGwiN1tP_WiF3Yp2p85rx-LDNgad1dBaKjkLUVcnKcZAxSsoX5Iy4ey_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WzFY3HEoS5qbF_XvVBMXj9BzyjXFHhcRQfVjfe-gpDwdkSVl-V-0OXyRlkEVcTEhQB-YBAXARD2cQ1mfLlcRDPqXBfGzuHe2VoRMMmVtoC7_Pf_xLBk8CCPerxGkNn5H_z_S5opOzlcn9JetAsUmIIjOf-oxQtxXJ-0oCi9kvkoC4DCVzNr2suaTNOSNqhsUhI4ChBtzRB7ykXjI2NfYbhwI_N-U17F1yZcJm5-fHQpDN-6yvrwV_ORy-k1JhBCM96wISmUEFpN_J_Zvcya4ULE5bKAG9iQnI61wy-uMZ6W0v5l58YSygbgrhioB3mjXmrW-hkVxeGmzu5VXsP9faA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gxSgQERT0oePI_TGgUoOreEvaVccQWEBFXp8Fv39_QTX-mCl9TzJ-2Zf-PL3hQ3GsQE6Okc4kKBjYrgZp8pKbwaIIe6Vaq5VZGTZML7VYsT3nhyg8-eL2siJAFqLUnWDgdqxIt-Pb4MFikqGGe7LCJ541IS5EnuHKRX56VB5XejzviReHS4oYjf063a2aMX_Olfx7nDfhuNqYoQKIY9Xk4jdc0Prk61IG5A-y5e1kFWrhcjV52wIE_z-k8v9yf66UArvfJCrLXTJG-PaeAmyHD_2mCy3V8S34uHL70rhd7SI-WVbY4-fTaSepDtANthnNz-PeLjjS8UGAPCa6RBQdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇯🇵
👀
شب‌های ژاپن هم قشنگه
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71413" target="_blank">📅 14:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71412">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4414bb2.mp4?token=fG8sNxrZ-ojWn8o1GvAk6fJnadvrfKek2Y_52mn5NUoZB3d9fanEzsJ-QsgcfYGFr9_2o49-oKbanw4Uf396Y5-MaZo2DpQyTCQ8KVXDxYfMvPjyHcwWkH0vj-7Nxqjnv2_UtGxRuggEHRhEYGA_w6Jvc232k9dxmonvnU6Pe-aG5tY1vguPAo6gAy9j8OcBKe5F-JJr6mxGeGYeNHlKz7IJPuAzYdaRCqzvnaTuEcomVy00J5Vto-AEJVUw8MdfBZ4iU4DkIJDQpaXAlD7yKlf-3bk1VpwJjGEGLcQmZbyeYgnp97nH72_6QMrWMs-4csBwLNrajRoXecfzXGCHBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4414bb2.mp4?token=fG8sNxrZ-ojWn8o1GvAk6fJnadvrfKek2Y_52mn5NUoZB3d9fanEzsJ-QsgcfYGFr9_2o49-oKbanw4Uf396Y5-MaZo2DpQyTCQ8KVXDxYfMvPjyHcwWkH0vj-7Nxqjnv2_UtGxRuggEHRhEYGA_w6Jvc232k9dxmonvnU6Pe-aG5tY1vguPAo6gAy9j8OcBKe5F-JJr6mxGeGYeNHlKz7IJPuAzYdaRCqzvnaTuEcomVy00J5Vto-AEJVUw8MdfBZ4iU4DkIJDQpaXAlD7yKlf-3bk1VpwJjGEGLcQmZbyeYgnp97nH72_6QMrWMs-4csBwLNrajRoXecfzXGCHBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل:
به مناسبت سال نو یهودی، می‌خواهم برای جامعه یهودیان ایران سالی نیکو را آرزو کنم و برای آنها سالی خوب و امن آرزو دارم. شما بخشی از تاریخ پرافتخار یهودیان هستید و همیشه در قلب ما خواهید بود.
و برای مردم ایران آرزو می‌کنم که در سال آینده، ایرانِ آزادشده از سرکوب و استبداد را به خانه خود تبدیل کنند.
با توجه به این احتمال که به دلیل خفگی اقتصادی و فشار سنگینی که ایران تحت آن قرار دارد، تصمیم بگیرند علیه اسرائیل اقدام کنند، به رهبری ایران هشدار می‌دهم: هر حمله‌ای به اسرائیل، به هر دلیل و در هر مکانی، با پاسخی قدرتمند مواجه خواهد شد که ایران را با ضرباتی سخت‌تر از هر آنچه تاکنون متحمل شده است، هدف قرار خواهد داد؛ از جمله تأسیسات انرژی اصلی آن که منابع و توانمندی‌های لازم برای ماشین جنگی و تروریستی ایران و آسیب‌رساندن به شهروندان اسرائیل را تأمین می‌کنند.
به دستور نخست‌وزیر و با دستور من، ارتش اسرائیل آماده و در حالت آماده‌باش برای اجرای این مأموریت است.
چنین ضربه‌ای ایران را ده‌ها سال به عقب بازخواهد گرداند و رژیم آخوندها را بیش از پیش متزلزل خواهد کرد؛ رژیمی که مردم ایران تا این اندازه آرزوی سقوط آن را دارند و مشتاقانه در انتظار فروپاشی آن هستند
.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71412" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71411">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpzpRFUunEnf2z0eE-h1y7gDIJjEMSzyYRhPYwN_6XYIxZFVhFmasYZ-HpIH2dQuL9rP__vEjMvGmzeHxiTRvbt8mKhP1bMDcoeoPVm2v1lnHpI8WotNp_a3SYWrdGiFIVsOIJ-kppKEuLAnokZ2iZF6jCyHHylMbTI2uc0DqPCo_kfGOfDuivOUKR0ELEam1MtMxgX6bQkbK9J-xcq0HWe835JCUqZaHiIt1VwWfvFONAiJQB0ql_ec4tie-_z11orvPIDM2OE2vwDG__Wxb94hiprIrgggITmlWiVxgvXTPed2kW8HWU5H-_kXO7Hl_wxLitUzt7kYnFKoU99DPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
توییت سفارت جمهوری اسلامی:
سرآشپز رضایی در حال آشپزی‌ست..
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71411" target="_blank">📅 13:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71410">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb607ca379.mp4?token=TKfUwSbW8Cs_m0P2pD0WHCHsoqXXQkrtZ3DYv5D0eVU1THnNanugOw7480ZE2HdAUSMsyOcaJ1NapV0MioxIPRwBtqGZnbv0Wrcua-PVzP7cnvc6-1-b26aS9vVj7abrRAAPyT1crtuuzWsPNUJ2s9qVTkBX9_SwTNZiWgO5p_GCW3fkzmAB2hrirgNGuB9zKf-K4L6khzTMY2lYBDGgJsbcN3b5c2B6Q0qu469jldJQWLjiMgkfgn9A23aPW6BlULOOCMVIn0Hl-trhoxjW-hSyk1dvfnC3bTrAA1pSF4PA11_N2vD_yKWIHPhEMI7APGwsdhPo5fmKByEiLlp1QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb607ca379.mp4?token=TKfUwSbW8Cs_m0P2pD0WHCHsoqXXQkrtZ3DYv5D0eVU1THnNanugOw7480ZE2HdAUSMsyOcaJ1NapV0MioxIPRwBtqGZnbv0Wrcua-PVzP7cnvc6-1-b26aS9vVj7abrRAAPyT1crtuuzWsPNUJ2s9qVTkBX9_SwTNZiWgO5p_GCW3fkzmAB2hrirgNGuB9zKf-K4L6khzTMY2lYBDGgJsbcN3b5c2B6Q0qu469jldJQWLjiMgkfgn9A23aPW6BlULOOCMVIn0Hl-trhoxjW-hSyk1dvfnC3bTrAA1pSF4PA11_N2vD_yKWIHPhEMI7APGwsdhPo5fmKByEiLlp1QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
انهدام پهپاد شاهد روسی به وسیله‌ موشک اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71410" target="_blank">📅 12:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71409">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇺🇸
ترامپ درباره ایران:
باید بگویم که این به لطف «نیروی فضایی» (Space Force) است؛ پروژه‌ای که فرزند معنوی خودم محسوب می‌شود.
از همان لحظه اول، ما می‌توانیم همه چیز را ببینیم.
حتی می‌توانیم برچسب روی کت آن‌ها را هم بخوانیم؛ «محمد الفاید»... «میامید» (Miamid)... البته هیچ‌وقت «میامید» نیست؛ هیچ‌وقت «محمد جونز» هم نیست.
«محمد»... «محمد العزوری». و این نام دقیقاً روی همان برچسب نوشته شده است. ما می‌توانیم آن را از فضا بخوانیم. باور می‌کنید؟ از فاصله هزاران مایلی، داریم نوشته‌های روی لباس یک نفر را می‌خوانیم.
ما دقیقاً از اوضاع خبر داریم، اما متوجه تحرکات مختصری در منطقه «پیک‌اکس» (Pickax) شدیم.
به ایران توصیه می‌کنم که دست از شیطنت و کارهای زیرکانه بردارد.⁩
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71409" target="_blank">📅 11:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71408">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f498f58530.mp4?token=nldc6oqBcwWuJEM8g6z1-hkzGSWD9IgyievpZ_iGmknmbItl1zo7BKbyTQVH_ojG1AVgXCsUEua8GTcjvwJtqpFHgwMVgZguYOYp6EshO_wNFdWGpAYIRT6N3yGCu76MU8c9oS7KZ13Ya-tMVG3g2bdFiqZ6FQkaNTjBuifTq6ebbRfl-PFkyENqduvGpcdOTg5b3Bsh5FUevhuZE6VVVGmNRKAXNxUT_24Ir0tJ4fG-8WgjHSrcKzY2jEmLwXQv7OhBrghvYE-_a2pSmsxe6gxEWRTEEbLwbMC-c969aDXAhe1zk9fiEUXGiTXuODncS5sZLu9d4PU5pSQXjLrMTS55jlka94NSu7FM-1kNQTunoq5kJSkRHkEANYtu4H5vwwD85N28Hl3nNFeHl9BjeMwGTVIwWMQsvaFXcbJAwAYPPR0ZTpq0glZOwTyE7bITCZa1SCCPk-WL3WYUjHnqTbFLKa5ZXmYNNgNmWDxINDSWnksT9xyCWl-uRRiTBCQ8z6EYR7kpvdMk4bqU5djdmLWPM02XMmtT16NnYXvTlW8I8l8ZkRSebgRvBAsHG3q1cdjkKAzpHpNbD09XXK9o-Bs1HJBMi54JYs-VWJIFkJMoRRTWILHqNNlnvKebCZWrEdvPXm3etTfTj5R1m7lUyHV51QfV_ExxmlEQ3lnaRhg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f498f58530.mp4?token=nldc6oqBcwWuJEM8g6z1-hkzGSWD9IgyievpZ_iGmknmbItl1zo7BKbyTQVH_ojG1AVgXCsUEua8GTcjvwJtqpFHgwMVgZguYOYp6EshO_wNFdWGpAYIRT6N3yGCu76MU8c9oS7KZ13Ya-tMVG3g2bdFiqZ6FQkaNTjBuifTq6ebbRfl-PFkyENqduvGpcdOTg5b3Bsh5FUevhuZE6VVVGmNRKAXNxUT_24Ir0tJ4fG-8WgjHSrcKzY2jEmLwXQv7OhBrghvYE-_a2pSmsxe6gxEWRTEEbLwbMC-c969aDXAhe1zk9fiEUXGiTXuODncS5sZLu9d4PU5pSQXjLrMTS55jlka94NSu7FM-1kNQTunoq5kJSkRHkEANYtu4H5vwwD85N28Hl3nNFeHl9BjeMwGTVIwWMQsvaFXcbJAwAYPPR0ZTpq0glZOwTyE7bITCZa1SCCPk-WL3WYUjHnqTbFLKa5ZXmYNNgNmWDxINDSWnksT9xyCWl-uRRiTBCQ8z6EYR7kpvdMk4bqU5djdmLWPM02XMmtT16NnYXvTlW8I8l8ZkRSebgRvBAsHG3q1cdjkKAzpHpNbD09XXK9o-Bs1HJBMi54JYs-VWJIFkJMoRRTWILHqNNlnvKebCZWrEdvPXm3etTfTj5R1m7lUyHV51QfV_ExxmlEQ3lnaRhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
دو نکته وجود دارد. اگر من برجام را لغو نکرده بودم و اگر آن‌ها را با آن بمب‌افکن‌های فوق‌العاده‌مان — آن بمب‌افکن‌های بی‌نظیر B-2 — هدف قرار نداده بودیم، الان آن‌ها سلاح هسته‌ای داشتند. و من مجبور بودم با عنوان «رهبر عالی» خطابشان کنم؛
مثلاً: «جناب رهبر عالی، حال شما چطور است؟»
اما حالا دیگر نیازی به این کار نیست. اگر آن‌ها سلاح هسته‌ای داشتند، من به رهبر عالی زنگ می‌زدم و می‌گفتم: «جناب رهبر عالی، حالتان چطور است؟ آیا کاری هست که بتوانیم برایتان انجام دهیم — البته به جای اینکه حسابی بمبارانشان کنیم؟»⁩
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71408" target="_blank">📅 11:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71407">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1bfc54b65c.mp4?token=N4U9MHHQpsBKGfuMpssH3Fc5LiQCRpt8VRF0Xc_yUXFbsQXiCVj2924Bf4VfeZUsC7yatn08gKDbQBQe3hah4ANjfRZhgAWcCHos5JrR5rfoB91DLKWTB5C3vXJN5oBKmYa8x4-UqS3Lc0qRdr8qUMq2MFS8OP9Juy0Y5DLAWaUGHWU00SHuPUkoUT0aZu2RVlwXEVcaPVyfRKlrLUFEFvkLc-RU_kVaxJDgzl3kW45X9LvjqhBA0IfZkeXxOePN40NfICEv9_bMnvVcoqKouheSD2HaL2jEQiqgGtUXCtBgTkic8YPZ55CHOoOc85EzpA7zqYUD39WukdBKOmrV14WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1bfc54b65c.mp4?token=N4U9MHHQpsBKGfuMpssH3Fc5LiQCRpt8VRF0Xc_yUXFbsQXiCVj2924Bf4VfeZUsC7yatn08gKDbQBQe3hah4ANjfRZhgAWcCHos5JrR5rfoB91DLKWTB5C3vXJN5oBKmYa8x4-UqS3Lc0qRdr8qUMq2MFS8OP9Juy0Y5DLAWaUGHWU00SHuPUkoUT0aZu2RVlwXEVcaPVyfRKlrLUFEFvkLc-RU_kVaxJDgzl3kW45X9LvjqhBA0IfZkeXxOePN40NfICEv9_bMnvVcoqKouheSD2HaL2jEQiqgGtUXCtBgTkic8YPZ55CHOoOc85EzpA7zqYUD39WukdBKOmrV14WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکی:
به نظرم باید اسم آن تنگه را عوض کنیم. باید آن را «تنگه ترامپ» بنامیم.
بالاخره باید سودی هم برای من داشته باشد. قرار است نامش «تنگه ترامپ» باشد.
خانم‌ها و آقایان، می‌خواهم خبری را اعلام کنم: ما آن را «تنگه ترامپ» خواهیم نامید و مطمئنم که رهبران ایران از این بابت بسیار خرسند خواهند شد.⁩
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71407" target="_blank">📅 11:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71406">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2660237e39.mp4?token=ePdxt0b2KVJUP_32driLmI2z_8ytOgUikt-YBM1OHIHy5jZX1Hg5_QnqcZRlqvBiLm0nunVPdLGyRdr29wBDGNrQVlskAb5pjKP_JgjNsiPiwuuTseakhvfbHTmuh5VmdbVezvvPtG-DR-4VyonTRiVfUF08SYfEl9sGM6FAW1u5he--wTM1aUW_Rby4t60EPmhKNoYKgPJugopmWjFqV89w-s8O07FUn7PebEiNjjDdh9jL6Mgz11-FdGKGjp7NeA81UR7secUA2CwkETON3fLnUVi4eiJZ8JbglTeaS6MVrDHUDjl1eePk9dX8la1GKi9ObFVwyrRtnemZLyoCHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2660237e39.mp4?token=ePdxt0b2KVJUP_32driLmI2z_8ytOgUikt-YBM1OHIHy5jZX1Hg5_QnqcZRlqvBiLm0nunVPdLGyRdr29wBDGNrQVlskAb5pjKP_JgjNsiPiwuuTseakhvfbHTmuh5VmdbVezvvPtG-DR-4VyonTRiVfUF08SYfEl9sGM6FAW1u5he--wTM1aUW_Rby4t60EPmhKNoYKgPJugopmWjFqV89w-s8O07FUn7PebEiNjjDdh9jL6Mgz11-FdGKGjp7NeA81UR7secUA2CwkETON3fLnUVi4eiJZ8JbglTeaS6MVrDHUDjl1eePk9dX8la1GKi9ObFVwyrRtnemZLyoCHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
اپل از AirPods 5 هم رونمایی کرد؛
▫️
ترجمه همزمان و زنده
▫️
نویز کنسلینگ فعال قوی‌تر
▫️
صدای فضایی شخصی‌سازی‌شده
صدا رو جوری تنظیم میکنه که حس کنی از اطراف و جهت های مختلف مياد؛ مثلاً تو فیلم انگار وسط صحنه ای تنظیمش هم متناسب با گوش و سر خودت انجام میشه.
اکولایزر تطبیقی نسل جدید
ایریاد خودش لحظه‌ای صدا رو بررسی
میکنه و بیس، زیر و بم و جزئیات صدا رو خودکار تنظیم میکنه تا بهتر به گوشت برسه.
تا 5 ساعت شارژدهی با نویز کنسلینگ روشن
💸
قیمتش تو آمریکا 149 دلار اعلام شده.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71406" target="_blank">📅 11:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71405">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71405" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71405" target="_blank">📅 11:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71404">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzbWTbhtV3xq9RDB_VbonSo_Wfi7K2FjFJz584756JHZXGFdJauta4DPsSGNUofP_Y-jcC0srhVikY8kN564X_5HynGf2__bCuyLI5FMrki9jG3_zOKtOCnseAsP_2NfebUPrIpvVHxHg8GKfsS-ni0j7LQPwFFtZHZXCMEjqulWuqPSP7kGJj7gkWO3cWv_zUQk8t_KNGJSJwcxtx74HvZUuh5MghtOH1DIAXxiklaP_hRsLhBjbNj8GwTuJWeCCX1B_5C4HVhq7zefwqIQJZr91VYy0vXjCQMdS24MfTpuPZIOIU9hZu5x-ocfxPPPMRdDvKKRxqZDdgnjnIZtUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پیکان
🆚
استقلال
⚽️
رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم
در ۵ بازی اخیر :
⚽️
پیکان : ۲ برد، ۲ تساوی، ۱ شکست
⚽️
استقلال : ۲ برد، ۳ تساوی
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71404" target="_blank">📅 11:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71403">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86c3602295.mp4?token=MW4_VCnEKUZUNMpCOJQBViIMZ-a1tPw-n9L0lKWn9N2evUQMtWgMAVbsWKq4Ord2SK15x5QssIIpOzOR_XL7eY5OuZprzLWXucySKD-pV0Zz2xNiJmEqgnLarsvuIlekHr4rRDDMkENL39CKZyHWV1lumyOKEIlN0M8yMLLhULVY0R6Fg6uxwvi4tQDk6ynjglfXrJ1gOXBq0z1lhusgblvQd1Jhne67rUPqyk_HTrmJtXn_E3edLR3ImmwneF08IFkkhPCz0wau56B6kDHxJtSxHgKLFb5lwY7yeV6ok8RfSJrYG0nbVe0VGAa4dlTDAstvopZDurrMrIAJUdG1Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86c3602295.mp4?token=MW4_VCnEKUZUNMpCOJQBViIMZ-a1tPw-n9L0lKWn9N2evUQMtWgMAVbsWKq4Ord2SK15x5QssIIpOzOR_XL7eY5OuZprzLWXucySKD-pV0Zz2xNiJmEqgnLarsvuIlekHr4rRDDMkENL39CKZyHWV1lumyOKEIlN0M8yMLLhULVY0R6Fg6uxwvi4tQDk6ynjglfXrJ1gOXBq0z1lhusgblvQd1Jhne67rUPqyk_HTrmJtXn_E3edLR3ImmwneF08IFkkhPCz0wau56B6kDHxJtSxHgKLFb5lwY7yeV6ok8RfSJrYG0nbVe0VGAa4dlTDAstvopZDurrMrIAJUdG1Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رئیس بی غیرت دانشگاه سمنان: از همه دانشجوهای عراقی معذرت میخوام، قول میدیم براشون جبران کنیم!
دانشجوهای عراقی فرزندان ما هستن و نمیذاریم کوچیک‌ترین آسیبی بهشون برسه.
اگه خدایی نکرده یوقت اذیت شدن معذرت میخوایم و بهترشو براشون جبران میکنم.
تمام افرادیم که برای دانشجوهای عراقی مزاحمت ایجاد کردن، بازداشت شدن و انداختیم‌شون زندان.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71403" target="_blank">📅 11:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71402">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1423e28a88.mp4?token=rnQxGENF9ZSHbmEDyBCFbSqmoeTb_KT2uavst9CaDS22FOGda4IMUuUiq9F7ZA3tP7TCU_InuDq5s17Ss7tv_on8zqNCqsHDl4esA056dvr7oFI3g3wHzfQ4SknoP25XtE73n-PYdAXWkgVga06O9HIzMqyxrtlMtHST15UwhU6gjqQBoaXkYunj3Q-tISWMfLoVLlqEB9Ln4Cb0YKnyyDxyRxips8XqHiEhmrVPCUiKyxanWmmSMSxsX7IwaBBA1Sh2PxNNkxO0YL_9ScjL9z9vgOusiO_H1bYOrpbItOFGAaJN314zYmQ5ER2GrW4O3I9RXSjZmyb0ltTgIFtrrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1423e28a88.mp4?token=rnQxGENF9ZSHbmEDyBCFbSqmoeTb_KT2uavst9CaDS22FOGda4IMUuUiq9F7ZA3tP7TCU_InuDq5s17Ss7tv_on8zqNCqsHDl4esA056dvr7oFI3g3wHzfQ4SknoP25XtE73n-PYdAXWkgVga06O9HIzMqyxrtlMtHST15UwhU6gjqQBoaXkYunj3Q-tISWMfLoVLlqEB9Ln4Cb0YKnyyDxyRxips8XqHiEhmrVPCUiKyxanWmmSMSxsX7IwaBBA1Sh2PxNNkxO0YL_9ScjL9z9vgOusiO_H1bYOrpbItOFGAaJN314zYmQ5ER2GrW4O3I9RXSjZmyb0ltTgIFtrrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف پدر بزرگش چند سال پیش فوت کرده الان ی چمدون پر از پول از پدربزرگش پیدا کرده که واسه ارث گذاشته بود و پدربزرگش تو چندین سال جمعشون کرده بود همشون صد ریالی و دویست ریالی ان و جمعا ۲۰۰ هزار تومنن‌
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71402" target="_blank">📅 10:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71399">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13a43f0b92.mp4?token=PF9CJbSZklzzQfg1xp_-9TtMrkQseQVTfef-_frYaI8YYbNvoDhwqMhMI8vMoJv6H8fpFxZwV1wWMWz1EmA3WE-dXoV342YOQC41y89CxkCXy2Vj6lZyhboGTebE6QCZBBP4vBoDinDjFh8I5y--Vyx06YBzI5Men-p6rB9lLCBs9ZMXVqiEZeEwTJTgXTkAc3ooRPNZtlKsfdqXDyNrx5923RUBaEQO5smLdDcXipVNatG6JALyNfXT_XvYbVN1GncwAfft-6RNhwSATBkRSUPcxlyirTjjd_RwrkFd6RiNHuiKMVFGUhalr_111NTwWS49BDtYyYDsudmf9xnYng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13a43f0b92.mp4?token=PF9CJbSZklzzQfg1xp_-9TtMrkQseQVTfef-_frYaI8YYbNvoDhwqMhMI8vMoJv6H8fpFxZwV1wWMWz1EmA3WE-dXoV342YOQC41y89CxkCXy2Vj6lZyhboGTebE6QCZBBP4vBoDinDjFh8I5y--Vyx06YBzI5Men-p6rB9lLCBs9ZMXVqiEZeEwTJTgXTkAc3ooRPNZtlKsfdqXDyNrx5923RUBaEQO5smLdDcXipVNatG6JALyNfXT_XvYbVN1GncwAfft-6RNhwSATBkRSUPcxlyirTjjd_RwrkFd6RiNHuiKMVFGUhalr_111NTwWS49BDtYyYDsudmf9xnYng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
«موسی غضنفری آبادی» نماینده مجلس؛
فقط به خاطر این کلیپ کوتاه ۱ دقیقه‌ای از «شاکر بوری» بلاگر اینستاگرام شکایت کرد و به ۱۳ ماه زندان محکومش کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71399" target="_blank">📅 10:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71398">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkEhPLCQwm0plbsibgr_YPWFrNUzE7BWzEWKNtEqLBcGMYDpn-Y2xtENChwff46gaK-NczC8ADSUXEJrzU1x7OLhrfHF0nMdmGMvTDHlrsK66QE7DEdCxkKUINOhUklm7gj6nn5IdwoSdDF0livp6ChAHSq7anA6N4geJULRX8LiOkuBNXoPpq7sKdU46BLTTQECV8gsl5l4kKb5ir8_wVezc_n4BZbrO3PAnl8qYSeVxRtyq6v2aslpJGDNcECICLesda8ipfyn8cBXkZhtX6f-v0d4tZ6ZpFsNPU8kp1q_wm3DlBXvu-XzdzqjYUkDs7RKfe5ILwS-Ff6FxyUxIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇵🇰
🇸🇦
رویترز:پاکستان در پی حملات گسترده گروه حوثی‌های یمن به عربستان سعودی، پیام هشدارآمیز ریاض را به ایران منتقل و از این کشور خواست تا حملات حوثی‌ها علیه عربستان را مهار کند.
اسلام‌آباد پیامی به تهران ارسال کرد و از آن خواست تا با استفاده از نفوذ خود بر حوثی‌ها، از بروز یک بحران منطقه‌ای گسترده‌تر جلوگیری کند.
به گفته یک مقام ایرانی، ایران در پاسخ اعلام کرد که «کنترلی بر حوثی‌ها ندارد.»
با این حال، دو منبع ایرانی به خبرگزاری رویترز گفتند که تهران حوثی‌ها را به تشدید حملات تشویق کرده و وعده تأمین بودجه و تسلیحات بیشتر را به آن‌ها داده است.
پاکستان اعلام کرد که هرگونه نقش نظامی این کشور ماهیت تدافعی خواهد داشت و بر حفاظت از خاک عربستان متمرکز خواهد بود، نه انجام عملیات در یمن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71398" target="_blank">📅 09:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71393">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v4ZLuGEW0R2iW83DQtv4f6oXKHz5wIT4g1QwUhPOtillFwet2RQYYwo7nXXdmlzG8P1dYu049Cm5rb7F93WS_ef5ggnBR4AYCO8WHdEGpdzaPefm7xWhDNIpCO0RuMIjEQuSJ9kU1x-6RQhXua5kPhX8RvJDgdYQtt4jod7dF5rjMMHwcI8GkbjYt2f0F9jcbdHmu2PFN9QC5lpZQFiTMEAPIkIGbUcuMxAw7UoBxQXnpuTFS82aeIOMi4gnTG97iEOC9eE7mLw0CWfxFcWhnZ0EcuZFgKfCh4vVDK08zjFwLrHzn4i4yO_jiJzgLgH3HxRivz8qxCKSrtoE7g-2Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDVCt4MFRFSVM3gjTZBmqGOKKlPnhGShKRIX2CgNhFCkGpvZoO8GSWS2DcfseO4yeqG86G3fek263_86Xo8KHx7rW87_-o5pPjYNszK-gJsJ0PbQvVutzq3idKW6EXYYBHsqCfInqgqfEceml2PdpjskEt5A885uIYV_qtIm9DyagGPk1WkpBTVg1RccBJi7EYyXLXboanW7yD6Z8Bzvg5JqNnuBU9WGHGl2D6mdj-kz-udV7u59cLWx2S-0GEYhIpQ0aqHPYoEaK8tXEG-osd6kJCU9HxK7zjSg23bmog3YtNth2dEGEX7ZIx8452S-X6tFipHftgbbdnlXEQQAaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MCNfawuoZrQJNhHztr_ZXAvhae_QnlL5fvpytDkjv-03PfyfVSWofGxEV72cObZ0FLe85z-DeZ7mpCu7Me698LqZzfMEDpyKmYaplXgKlvrs0p2FevQbLl5Ln_u0H7o9jyqYcbwV1Nb_vbnLap9CUcpL62yvDcZnppgfkX0Q8bsuEuZr_zo4A901Uba85uyZlfkcRgjJiyZdicG2gKlzNKDsDgHnnBvkrVmMl2sueOtxMrERgqNXlk8q7Ycp_mZdmDFM2hWS_SGsFbUJO9MEFVduMC2r11yZR33jW1KnT-BZzVXzPb4E8wLyvdpnKD85nCdkqI53kAg88TtHsuSyqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bF-00KpwCigdHnTfzoqI2sBQQS8JEGdCpwcixkYh719TSI0GDAyyU-8lOGNn5iE-ozXjgtu4XQPQVrcVUZ-0qsv6jsyDyH0N1fJbOoDcHV0lBUi0vpyNnCKSlr18rY5hGebwULddXAZ32e105Zk47VcoHRNmOQ6BzdTvXPuetauRZEzGKJWESGD7n77O5qdqfWuqCircL9efsxhji74MyiOx12RhB1qg661L3-OsFwwTwfV47lM3_sL8dE3GcV_AgW2_kBF4HQhXLZMxHrqbnNUPmJ4sDY26dxuMCV03y27N3bA9GnKSJPhA2PXONNU4YC2E-MSrbSSTLmfz1d8u_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5fed9d1b.mp4?token=Z-UOojKCmVXg8f5oo3gAVrwbeswGIGwpdddBUoselMPEcOcZjP9RYDygTS7i9aekIn1aQqZzIz312fxcYjNELkqiKcGTVn_a6JX2rLSBz-erkMhjrfuDnSWeZ1ogcSdzJRvb0_jMDjZ9g11CSFKPw6P6OUedC3uqsmpBuX8doS-LMQy_rU0bsOE3DvFXr1Rxh2fJ80XFv6wEsPECWzx5bpJm9DukgMvOYEw46SEahMWZcvHWje8dL6nqGP-Q7Pa1-Tv_85a0B88rblxcHjx7wD6rsjZcbgMsV79jWXjSvX7uxa4iQrXS9qBraHXNqO2pGbaCiu0HRkXC6d4F26cEBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5fed9d1b.mp4?token=Z-UOojKCmVXg8f5oo3gAVrwbeswGIGwpdddBUoselMPEcOcZjP9RYDygTS7i9aekIn1aQqZzIz312fxcYjNELkqiKcGTVn_a6JX2rLSBz-erkMhjrfuDnSWeZ1ogcSdzJRvb0_jMDjZ9g11CSFKPw6P6OUedC3uqsmpBuX8doS-LMQy_rU0bsOE3DvFXr1Rxh2fJ80XFv6wEsPECWzx5bpJm9DukgMvOYEw46SEahMWZcvHWje8dL6nqGP-Q7Pa1-Tv_85a0B88rblxcHjx7wD6rsjZcbgMsV79jWXjSvX7uxa4iQrXS9qBraHXNqO2pGbaCiu0HRkXC6d4F26cEBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
شرکت اپل با انتشار این ویدئو، رسما و شرعا از آیفون 18پرو رونمایی کرد؛
🎨
این گوشی تو چهار رنگ عرضه می‌شه:
• زرشکی / شرابی (Burgundy)
• مشکی تیره (Deep Black)
• آبی یخی (Glacier Blue)
• نقره‌ای (Silver)
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71393" target="_blank">📅 09:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71392">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71392" target="_blank">📅 01:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71391">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nwl34W4FdorlsR19VKies3xFijg41nELtOPZwLAhh43NJnYddtMRq98A5ho9rAdB6Sq9X5GvSVQes91DkQwIztqWkDWx9DBAVpr0YeOj2XkSjlFg6_cLzoW66gJvVl2mxJlSJJcase-D7lvAF6MuT_1VLCDwAK3fC016gr_097qX6Sl2RgOojH6mOWZ-OW5sCouSMsgUAWXq45frV0FSnvMvrOVGovgh4N6wHSzRF4SlKJbNNuqkhQyiwqn2zfCh-GDsYCPjelwQjFFRXTEIo6JdQ0Tn3QJQ_fAM0qFtmyIC_diiyQTnguogF89MSOPehjo2LmzDXq958IkRlW3yCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71391" target="_blank">📅 01:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71389">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l1vdfaSeIpWvGUd9b88Fyz6DTcmxBz8wy8eiam35PtBUpNuyVL4QuUUWbCA040V6CQV6j5PpVX-h25tD5hypwHsEYWnidEPTNvDHg6yZ_kkIACUNPYa1qRXkjHDTCEqKoAoJKDZ6XzfRblNjElnTK76W7vMnGJ-IsKpp0kRgfRT6UKAxFMi4a3Fqh-ASe1EUFg055mvdQYRYTiZe_HGw8P2oLAn2_v5XBruSHfeSouEsrO1uwZU-tdcMpkVz97b4hASYhrdmB_m5HC1DHLSsvB7_LwmEnkZ3APq-9cCT4J_RwtiRgf2nC1a6Y5V6KbRj4IU_5-b2AE7VGRcNMWblPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q98OVEJwKdFbK64vD5m6UXFdzY2gMK0jrOos-hKqhalvYVh3IZonbAv9k7f43uWEk6Wq5ejRWij0IMxEW3sa-nyvLGme7pyv_HUv73pPJOj2bPYmRZF-jVk24eUTvJFVfhsaU53NDW2i2ONY33fbmhL0PUvMbm7ZbAhwV2coE7AP2jCoFganEYeDKE_0bRVvasbiHLk314zVMni8x9DWE-o7oV-62YSjS4woX_x1nclAJK_FmM3mzZ6uSrbTiLUPz0x50xFJIma_RvdqwaERY0QN2ZUXS3StlQpMfogcLZuXeEVlmaSKfrdrRfLE-bPQU8OceAkVcEYIP0A0IXF32A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
به گفته منابع عربی حوثی ها وارد منطقه حیس شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71389" target="_blank">📅 01:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71388">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
فارس:دقایقی پیش صدای چند انفجار در مناطق ساحلی سیریک و قشم و مناطق ساحلی شهرستان میناب گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/71388" target="_blank">📅 00:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71387">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
گزارش ارسالی از قشم:
قشم هم در خونه ما لرزید
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71387" target="_blank">📅 00:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71386">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
دقایقی قبل صدای یک انفجار مهیب همراه با لرزش زمین در کوهستک (هرمزگان) شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/71386" target="_blank">📅 00:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71385">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=gVeVf-O5OMO-pyASt52KRSjiQPVaniKQQqpaRibjyzZw62nu9QAtRZXOjj8XSlqVb3z0nVBlhEI2xbtzagC-HSq41b8VTA1A0C1F7ToERautfGbbqS9Akd2hetbnKoMapJrUwdP6x8iC4hOkHjZMqDn8BRYAOTyAb638NWQ74D0AK1iTJwo_hMtmD_ks2R_DV1QjSTwcfFhCgTuWUZwWv5wUgcYRAravaF-pFFQGClbcwbqlfDOYEs9QfbAyq_Lks1dW2WMYRYC2igxtgmFAnMlxNGmcYAwbit0Nks1y1qggkcEpHsDSk2DM7xf7EqX4_7m3eiDe2D_Yot6vW4sYvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=gVeVf-O5OMO-pyASt52KRSjiQPVaniKQQqpaRibjyzZw62nu9QAtRZXOjj8XSlqVb3z0nVBlhEI2xbtzagC-HSq41b8VTA1A0C1F7ToERautfGbbqS9Akd2hetbnKoMapJrUwdP6x8iC4hOkHjZMqDn8BRYAOTyAb638NWQ74D0AK1iTJwo_hMtmD_ks2R_DV1QjSTwcfFhCgTuWUZwWv5wUgcYRAravaF-pFFQGClbcwbqlfDOYEs9QfbAyq_Lks1dW2WMYRYC2igxtgmFAnMlxNGmcYAwbit0Nks1y1qggkcEpHsDSk2DM7xf7EqX4_7m3eiDe2D_Yot6vW4sYvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛پست جدید دونالد ترامپ در تروث سوشال:ترامپ ویدئویی منتشر کرده که در پایان اون بخشی از سخنرانیش در زمان آغاز حملات مشترک آمریکا و اسرائیل به جمهوری اسلامی آورده شده که میگه:
🇺🇸
ترامپ:
این رژیم به‌زودی درخواهد یافت که هیچ‌کس نباید قدرت و صلابت نیروهای مسلح ایالات متحده را به چالش بکشد.
🎙
سخنگو:
او به جهانیان یادآوری کرد — همان‌طور که بارها و بارها گفته است — که آمریکایی بودن، نمادی از چیزی شکست‌ناپذیر است.
اگر آمریکایی‌ها را بکشید، یا هر جای این کره خاکی آن‌ها را تهدید کنید، ما بی‌هیچ عذرخواهی و درنگی به سراغتان می‌آییم و شما را از بین می‌بریم.
ما آغازگر این جنگ نبودیم، اما در دوران ریاست‌جمهوری ترامپ، آن را به پایان می‌رسانیم
جنگ آن‌ها علیه آمریکایی‌ها، به انتقام ما از آیت‌الله‌شان بدل شده است
🔴
ترامپ:
خطاب به مردم بزرگ و سرافراز ایران:
لحظه آزادی شما فرا رسیده است.
وقتی کار ما تمام شد، کنترل حکومت را به دست بگیرید؛ این حکومت از آنِ شما خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/71385" target="_blank">📅 00:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71384">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71384" target="_blank">📅 23:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71383">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/364cd7494f.mp4?token=DOZhFYzDkg-kqAouvMlcRY9GBwjlykaiTyha8_QvY5ft37OFVW4cRzoRwY13LQqCWTrWKHd6islfTxgWHKj28yBotZIc_Cfg4d7rs6e9boKJ2bG5OBXbtskc_JPy6OeHmgo9NntJPeSSjhIG6jNicYAEcltUWKda-ND3LA5xqigkJrRtHzUhn17GEjTcBfBlE9R2JEeTba1u4Tt19z2RpJUjIW_OAkGFv1YRwYuNyqpaAKTSSDGUkmrmS7siT0QCAjvjVP8Y1iUXg8hF0dUF1D3xki5zcEW12xdY9hXzDU1c2tzMjghppB8O_FIaXKCAP69VAYAyQ_V_p9maiGur5TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/364cd7494f.mp4?token=DOZhFYzDkg-kqAouvMlcRY9GBwjlykaiTyha8_QvY5ft37OFVW4cRzoRwY13LQqCWTrWKHd6islfTxgWHKj28yBotZIc_Cfg4d7rs6e9boKJ2bG5OBXbtskc_JPy6OeHmgo9NntJPeSSjhIG6jNicYAEcltUWKda-ND3LA5xqigkJrRtHzUhn17GEjTcBfBlE9R2JEeTba1u4Tt19z2RpJUjIW_OAkGFv1YRwYuNyqpaAKTSSDGUkmrmS7siT0QCAjvjVP8Y1iUXg8hF0dUF1D3xki5zcEW12xdY9hXzDU1c2tzMjghppB8O_FIaXKCAP69VAYAyQ_V_p9maiGur5TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
پرزیدنت ترامپ:
انجام کاری بسیار فراتر از توافق هسته‌ای.
چیزهای بسیار بیشتری از هسته‌ای وجود دارد.
ما به توافق هسته‌ای خواهیم رسید، این ۹۹.۹ است، اما چیزهای بسیار دیگری روی میز خواهد بود که سه ماه پیش روی میز نبودند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/71383" target="_blank">📅 23:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71382">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8c1afb2e.mp4?token=TdbaI533OtqtZ84qRBSYHNyIeVbKmZR1fM-MGeYofKr2UdShWdCWAb-mJvgXBydC-Bt9lWncUCp0eN0VrD3OXzesKeQ_V5DBdvYNZP_7l348CEMXWe20Tpi_cP7ve60EiadWdzZERe7mQ-SusXvaDd-nM4J7Ewg_3NeWAQxMdxh-WHiO-rEHhVrvAETeKex2SwC9b-ts4oKGWo0ZYjeaQ9vBVhYRmN5EZ8KbSt1EelH4uaSRQ73UvydPbg1QvDJo_nfADJjF_JWyA79BKJZFfXaID7sKxTe6uQaonf46_ObGQraBBBp2Y-D20962gsSvdQ_X4jm0wNKZiiy9LjwUJ3_AfKGDijQ84awjCp7rUWDaLVgp-Xq7CtAjYJbcHg7KuvM4GaXTznyW_mvwhAtwJKZ9pz0EV_SC-jMH7YlyvkeZfR0DZTio3ekHCpoktlwmNEMW5R3DQSL5_ZEu4gSBhERuLCUYFU2SfGVCLyCx6SVNesLY1IgWyiNFJmlPKADiZgNI0-oPAnz_3M0Zr2lxrig8jzBxqdlM_TGzXNbpJCzyRq_EmXLaGQtU4GI9uYh0WMnc2C0fYoz_Q_SLDvNQZ1Ccltruw36ntHJJjswKG5d1KTaB9Gclfca_-e0vuNjySM1JUX8t1VcfR1Z2r-OfXVi4Hhy_ohRWsHsRip_USqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8c1afb2e.mp4?token=TdbaI533OtqtZ84qRBSYHNyIeVbKmZR1fM-MGeYofKr2UdShWdCWAb-mJvgXBydC-Bt9lWncUCp0eN0VrD3OXzesKeQ_V5DBdvYNZP_7l348CEMXWe20Tpi_cP7ve60EiadWdzZERe7mQ-SusXvaDd-nM4J7Ewg_3NeWAQxMdxh-WHiO-rEHhVrvAETeKex2SwC9b-ts4oKGWo0ZYjeaQ9vBVhYRmN5EZ8KbSt1EelH4uaSRQ73UvydPbg1QvDJo_nfADJjF_JWyA79BKJZFfXaID7sKxTe6uQaonf46_ObGQraBBBp2Y-D20962gsSvdQ_X4jm0wNKZiiy9LjwUJ3_AfKGDijQ84awjCp7rUWDaLVgp-Xq7CtAjYJbcHg7KuvM4GaXTznyW_mvwhAtwJKZ9pz0EV_SC-jMH7YlyvkeZfR0DZTio3ekHCpoktlwmNEMW5R3DQSL5_ZEu4gSBhERuLCUYFU2SfGVCLyCx6SVNesLY1IgWyiNFJmlPKADiZgNI0-oPAnz_3M0Zr2lxrig8jzBxqdlM_TGzXNbpJCzyRq_EmXLaGQtU4GI9uYh0WMnc2C0fYoz_Q_SLDvNQZ1Ccltruw36ntHJJjswKG5d1KTaB9Gclfca_-e0vuNjySM1JUX8t1VcfR1Z2r-OfXVi4Hhy_ohRWsHsRip_USqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
در مورد ایران؛ آیا انتظار دارید که [چنین روندی/مذاکره] زمانی آغاز شود؟
🇺🇸
ترامپ:
راستش را بخواهید، جف، ما به دنبال چنین چیزی نیستیم.
در ابتدا می‌خواستم به توافقی برسم، اما اکنون کار از آن مرحله خیلی گذشته است.
در حال حاضر چیز زیادی از کشورشان باقی نمانده، بنابراین ما به دنبال آن نیستیم.
بله، شاید مذاکره‌ای صورت بگیرد، اما این چیزی نیست که ما در پی آن باشیم.
🔴
این جنگ بلافاصله پس از انتخابات ما پایان خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/71382" target="_blank">📅 23:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71381">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088801b967.mp4?token=HnLbcj2nc3SAzfo0iwtlBncD62C9jXCMoQEvmyjRBBAHORuJwmLhl8_-6TdY9QiiWaEvm0ouJE8PRHUGpEoMTJA3ogX2el3tLXiT2iDOJSA365YOo2cMq-HutFRRptWrnjCZp955Vw4hve1FZWrHVOz-nI5iZFATWeVnr-spXNXaZ9QoKd5KXl_ukmnsA2jWkZ1aOuwvu_B6mZjns-wiQsz4CDgp3v2EQ4mx6lwrzLCfGEXYAgZVuOab0xDaOMVJpfwtBPekDo4ApuEnVhP9VgA-EiG9kDgWI9tdociMI9xQ8tKNuFtmcQ9Ixoc9GOJ7xbn_4Lz1rRm6eWYB-nnMtk7e6vtfwQ1S2SBL89idj3hlTs7Vf5iXvYhN3DnCRP14QShEIMZ-DdRq4aUW2GwlTIOjA_C-3Z5VrLsRK2CzbIpJlpLk6Y-pNLWkj0gEP156DZ4Bmzw_TiUBdyn4zWNYoNdcoGAMJF2nheZQ6pJdjfjfQ_WokSxEoNsOLpUxMjotROvFVWCUWrZTi5cmMqTuSA6sI1rHcqeSPSGjvUw0QNdktixkKZ_tKczH30JgInF-kx4FruYjq1yXoiqApTJMRhnx4C3CdNQ4ch-Itsq_iKWIJosE_D4s-hy8SnIEJmZZS4rS3Amk9wVv0fpnvuCko6aBlFexQBPuJL-rqA1hzmc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088801b967.mp4?token=HnLbcj2nc3SAzfo0iwtlBncD62C9jXCMoQEvmyjRBBAHORuJwmLhl8_-6TdY9QiiWaEvm0ouJE8PRHUGpEoMTJA3ogX2el3tLXiT2iDOJSA365YOo2cMq-HutFRRptWrnjCZp955Vw4hve1FZWrHVOz-nI5iZFATWeVnr-spXNXaZ9QoKd5KXl_ukmnsA2jWkZ1aOuwvu_B6mZjns-wiQsz4CDgp3v2EQ4mx6lwrzLCfGEXYAgZVuOab0xDaOMVJpfwtBPekDo4ApuEnVhP9VgA-EiG9kDgWI9tdociMI9xQ8tKNuFtmcQ9Ixoc9GOJ7xbn_4Lz1rRm6eWYB-nnMtk7e6vtfwQ1S2SBL89idj3hlTs7Vf5iXvYhN3DnCRP14QShEIMZ-DdRq4aUW2GwlTIOjA_C-3Z5VrLsRK2CzbIpJlpLk6Y-pNLWkj0gEP156DZ4Bmzw_TiUBdyn4zWNYoNdcoGAMJF2nheZQ6pJdjfjfQ_WokSxEoNsOLpUxMjotROvFVWCUWrZTi5cmMqTuSA6sI1rHcqeSPSGjvUw0QNdktixkKZ_tKczH30JgInF-kx4FruYjq1yXoiqApTJMRhnx4C3CdNQ4ch-Itsq_iKWIJosE_D4s-hy8SnIEJmZZS4rS3Amk9wVv0fpnvuCko6aBlFexQBPuJL-rqA1hzmc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
لطفا شهربازی که میرین هر چی رو سوار نشین؛ بعضی موقع‌ها همچی مناسب نیست و شیطنتتون گل نکنه بخواهین یه تجربه کنین.
این فقط دیگه نریده بود تو خودش...
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71381" target="_blank">📅 23:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71380">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0632abba0.mp4?token=pBur4a-deGVXVXT6sfGvL_s9QFpgv74GPzU4FNIGop-cbbo_KVYVIsA35yWY6nkzQb1GapEpHMfWXsYxvCosKs0H5-aFgtNKFF72lUqKJi0GBp-soBkeJD5I67jK57hlTHNfei56EOdTpxttlaOUkfzOKySPIFo-mIU7GFOGXCYqGThP_tYWsFCcRPzKfLbZi44jk8Szoi5wqZ7z1-OtwgU4KQ4sskFBa3CLYVWNmNUv30DPPza8X8i5TU2TOaeoqMQ87bMO8ue5VpoL1vB7EX4ZH_wvlWjONz0nhe5n2IXt28Zi2Fb7DFLtltF8XHlUxmc8xITH7k-vW9TPna1owrLj8d47cJGEEoa1lXWAR-hf4E64bdv6MAoPrAdJZXvqhTnvfhRxj2ja1iwwn1Fa2aiTM1lkWK1IwREIk7PjySs8FfbCsxVO33yOTsXW0XdFOMYa75_4PLxUMNOukJjw5jWCDidCLqNPKdeWgG8Q5r2_FqU5eSOhWZgyYYuMskJQR7zjoU0YVF4fassNvS4lCs0KCi1eijcw28UrYWf3Et57sJrmKraIy97G0XuLD8CmBtQdbcMV2mJZJY3WH__90c6OxKOcAbptX9j1fvDG3YAalZJ4dH1jHNki4ZSp_zd4LyjEwMtyLRiJj8VdKAezjwoEsUg9H8dCfuuRm74PDTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0632abba0.mp4?token=pBur4a-deGVXVXT6sfGvL_s9QFpgv74GPzU4FNIGop-cbbo_KVYVIsA35yWY6nkzQb1GapEpHMfWXsYxvCosKs0H5-aFgtNKFF72lUqKJi0GBp-soBkeJD5I67jK57hlTHNfei56EOdTpxttlaOUkfzOKySPIFo-mIU7GFOGXCYqGThP_tYWsFCcRPzKfLbZi44jk8Szoi5wqZ7z1-OtwgU4KQ4sskFBa3CLYVWNmNUv30DPPza8X8i5TU2TOaeoqMQ87bMO8ue5VpoL1vB7EX4ZH_wvlWjONz0nhe5n2IXt28Zi2Fb7DFLtltF8XHlUxmc8xITH7k-vW9TPna1owrLj8d47cJGEEoa1lXWAR-hf4E64bdv6MAoPrAdJZXvqhTnvfhRxj2ja1iwwn1Fa2aiTM1lkWK1IwREIk7PjySs8FfbCsxVO33yOTsXW0XdFOMYa75_4PLxUMNOukJjw5jWCDidCLqNPKdeWgG8Q5r2_FqU5eSOhWZgyYYuMskJQR7zjoU0YVF4fassNvS4lCs0KCi1eijcw28UrYWf3Et57sJrmKraIy97G0XuLD8CmBtQdbcMV2mJZJY3WH__90c6OxKOcAbptX9j1fvDG3YAalZJ4dH1jHNki4ZSp_zd4LyjEwMtyLRiJj8VdKAezjwoEsUg9H8dCfuuRm74PDTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ:فکر می‌کنم جنگ بلافاصله بعد از انتخابات تمام می‌شود.
دلیلش چیست؟
چون دیگر نمی‌توانند دوام بیاورند.
آن‌ها به‌شدت تلاش می‌کنند بر انتخابات تأثیر بگذارند تا گروهی ضعیف و مطلوبِ خودشان سر کار بیاید؛ کسانی که کاری به کارشان نداشته باشند و بگذارند به سلاح هسته‌ای‌شان برسند
تمام خواسته‌ی آن‌ها سلاح هسته‌ای است، و اگر به آن دست یابند، کل دنیا دچار دردسری بزرگ خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71380" target="_blank">📅 22:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71379">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6c19e60d.mp4?token=LABmfIYV9STZiX_eWx96Dp81GaRoks9Jg41Kq9p42gRlNhxguqEbb7z12Yr-ExeTuAfTh5bwEtqetGbWmXsEi-s_osf6Ag9aRt75lLQgc8pQcz3yzAUXhgtWo_chWyA4pCsKmdMlEWsKqdpcIAfypsqnQ0U25EZZGaBoQjRfa_qhZguKiA2qtJrCbnaoygKTPfEip5pSWBTSrVTEy4_8exohVEPtKavxFTIhoVSlBGc53b1JvICAKml0jgClgTNdBz38C4LvdL3o0UPidH4rFCgxXBi-pmPkGU3wNKIZhLzthkqlaGWJQHqw5t8yFtiDRp4ztFI6dttQ3Ruyq-CxSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6c19e60d.mp4?token=LABmfIYV9STZiX_eWx96Dp81GaRoks9Jg41Kq9p42gRlNhxguqEbb7z12Yr-ExeTuAfTh5bwEtqetGbWmXsEi-s_osf6Ag9aRt75lLQgc8pQcz3yzAUXhgtWo_chWyA4pCsKmdMlEWsKqdpcIAfypsqnQ0U25EZZGaBoQjRfa_qhZguKiA2qtJrCbnaoygKTPfEip5pSWBTSrVTEy4_8exohVEPtKavxFTIhoVSlBGc53b1JvICAKml0jgClgTNdBz38C4LvdL3o0UPidH4rFCgxXBi-pmPkGU3wNKIZhLzthkqlaGWJQHqw5t8yFtiDRp4ztFI6dttQ3Ruyq-CxSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شاهد حملاتی در تنگه هرمز بودیم.
🇺🇸
پرزیدنت ترامپ:
خب، این حملات... این حملات کار ماست. ما 9 تا از کشتی‌هایشان را از کار انداخته‌ایم. بله، می‌توانم بگویم که این حملات از جانب ما انجام شده است. اما... و خواهید دید، خیلی بیشتر از این‌ها خواهید دید... وقتی که به آن ضربه بزنند؟
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71379" target="_blank">📅 22:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71378">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c27e89aeff.mp4?token=Htdc6vbt5-qPO4STgddYVNrDBUqjVFVrFwnaWQQ7qcqnMC5wOJT0qmrsW4mbhu-jGfuHwH3p5Iq62foa5tRpCI9zaCT7Kd4f4l96m1Sbn9t7-hJT6aaK7hK5t4dh29XZlB_tN9FUiui7L0TFpSO_AEWX9JnY4IlS-uwK8jjM6_OuiSXE4QFxKv3jHvGP_B-YvmfWHA4zFxHV3GdUSx4PD3dwlKaqQp3FFn-MxeyaZXSzD9Y32OK9di3jpEYrBV-CzV68N0grRX2yZpVcu16fKSPCDXDBtJv57s99gKpBkzRPn7b2RCkgQXjBCF9yqZDHLPJm9idufdF5WmjRQ08DGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c27e89aeff.mp4?token=Htdc6vbt5-qPO4STgddYVNrDBUqjVFVrFwnaWQQ7qcqnMC5wOJT0qmrsW4mbhu-jGfuHwH3p5Iq62foa5tRpCI9zaCT7Kd4f4l96m1Sbn9t7-hJT6aaK7hK5t4dh29XZlB_tN9FUiui7L0TFpSO_AEWX9JnY4IlS-uwK8jjM6_OuiSXE4QFxKv3jHvGP_B-YvmfWHA4zFxHV3GdUSx4PD3dwlKaqQp3FFn-MxeyaZXSzD9Y32OK9di3jpEYrBV-CzV68N0grRX2yZpVcu16fKSPCDXDBtJv57s99gKpBkzRPn7b2RCkgQXjBCF9yqZDHLPJm9idufdF5WmjRQ08DGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
کمی بعد، اما درست بعد از انتخابات، چون آنها دوست دارند اوضاع به این شکل باشد، اما درست بعد از انتخابات، قیمت نفت رو به کاهش خواهد گذاشت. قیمت‌ها پایین خواهد آمد و فکر می‌کنم قیمت بنزین را پایین خواهیم آورد، به زیر ۲ دلار در هر گالن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71378" target="_blank">📅 22:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71377">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34c7f74659.mp4?token=Tr4Ux7LgllBuuSXtPtjpclEXuP21dE9ZH8ivWz4Qg0qG2orXLd8HZTpZz_1utQb63-jKBAqCRtAit1Z64kHuePlA7Ak0u6nfnhXcHwLTXlhgv5EZvJRTTckLP9WuV24E3T5Iws2xoIU7WrVxIZxJ_6zPnVCRloTX-Dhh9DQW2JO4R6oqkrydwUrnZ2-QEHU5enmD58UARN102wcd5wN63k6yHB9uMbmjMB9Qqo8WNPFirkMDU1HlgkCAH2dnUVtpY73rUaudjb1NWzYOoX_oQqepgzZAJI-3WIZkrnoxxL2qh39YpcNHTpAptr5Kkd9hczp7GhDYTtBdmnpNoIr0cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34c7f74659.mp4?token=Tr4Ux7LgllBuuSXtPtjpclEXuP21dE9ZH8ivWz4Qg0qG2orXLd8HZTpZz_1utQb63-jKBAqCRtAit1Z64kHuePlA7Ak0u6nfnhXcHwLTXlhgv5EZvJRTTckLP9WuV24E3T5Iws2xoIU7WrVxIZxJ_6zPnVCRloTX-Dhh9DQW2JO4R6oqkrydwUrnZ2-QEHU5enmD58UARN102wcd5wN63k6yHB9uMbmjMB9Qqo8WNPFirkMDU1HlgkCAH2dnUVtpY73rUaudjb1NWzYOoX_oQqepgzZAJI-3WIZkrnoxxL2qh39YpcNHTpAptr5Kkd9hczp7GhDYTtBdmnpNoIr0cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه هموطن بعد از گرونی بنزین زد به سیم آخر و از بالا تا پایین مسئولین رو یکی کرد.
حاوی الفاظ رکیک، هندزفری لازم
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71377" target="_blank">📅 22:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71376">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_t9kcaYJ3L65eyZwQmRm9rIzxrQhavlRM93iZkjqELAYGwByU4yBEbnIFk6GJ4p8SlTIs7hqMvgxOj8-p7fCpoGLZof_08qhCTln8mYCMuqHhjID-5r_I5cphqS3pJ9iqUgh_WIE0ZMuozvMpJPz8q5chF_1qt_QDd03ehpkBdaw_9mQnSPaqSl2CPMmNEGr_QJoKErSloXAG4BRUMlFi69yMfum3pCPbHpIm4mLseNIemPxE0oqi6WqbL64GLHzuiOI2x0c_ECMjjrX7cnO8KWhnBjm9v7xzgURbEl4CHHpMnoJXwKr-4ebRvaLulXUCzn527Lv54_8e0ViYWDxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇺🇸
🇺🇸
به گزارش «نیوزنیشن»، دونالد ترامپ همچنان در «بال غربی» (West Wing) حضور دارد و طبق برنامه، هنوز عازم دالاسِ تگزاس نشده است.
ترامپ در حال دریافت گزارش اطلاعاتی به همراه جی‌دی ونس (معاون رئیس‌جمهور)، پیت هگسث (وزیر دفاع) و ژنرال دن کین بوده است.
احتمال می‌رود این جلسه پیرامون موضوع ایران باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71376" target="_blank">📅 21:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71375">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22f299161.mp4?token=aZ-tLvq8QyA4bH-HMNev4-fgvZOYS52I2GgLsYxbZwKrDLOTPpxfGilEGspFSiqxksvvvHEAuerrtXJn8z8R9yCgpgL0hqitPkfg2yVYG8bOrOaiBKr1aWyetS2kWSifqi0A6XsMpMRXof7aTOc3WpFj4OKHLmmYOu9N4xbWORkOROkFytwRHA6pO2uL4YvJRdGeMTP5DJ2ng07MPqLpCOd00I_1ToGvMzC6jnUKNNcYyO5E6ikw4TaLjTPlclEL4bllK5HkqP6FhoGkgrk5_ncqTrmZso2ciFk932mqgaEzYOzqWlr7Odo8rRkNqTDEI_CLOdg3s23NAyvW3TMieg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22f299161.mp4?token=aZ-tLvq8QyA4bH-HMNev4-fgvZOYS52I2GgLsYxbZwKrDLOTPpxfGilEGspFSiqxksvvvHEAuerrtXJn8z8R9yCgpgL0hqitPkfg2yVYG8bOrOaiBKr1aWyetS2kWSifqi0A6XsMpMRXof7aTOc3WpFj4OKHLmmYOu9N4xbWORkOROkFytwRHA6pO2uL4YvJRdGeMTP5DJ2ng07MPqLpCOd00I_1ToGvMzC6jnUKNNcYyO5E6ikw4TaLjTPlclEL4bllK5HkqP6FhoGkgrk5_ncqTrmZso2ciFk932mqgaEzYOzqWlr7Odo8rRkNqTDEI_CLOdg3s23NAyvW3TMieg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🤡
اوستاد خوش‌چشم تحلیل‌گر ارشد صداوسیما:ما به سوی یک درگیری تمام‌عیار و کوتاه‌مدت در پاییز می‌رویم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71375" target="_blank">📅 21:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71374">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yv4TZmSuCHhaH-vw8cwXPu3U3wo8zrottgaMakosWBLSABvtIg1G4jafSxA2oH9zROLz_7Ffj5nbmm5UGS8Vuod64msuzxEtZBW__YO0KBxb1Lb79dBQZoyPhJqeIeek_5qmkrV7Fbe8B9LCgqzkXP1nZpA7YyMBoc29742SzRRj5aegpjddc8o4fKHAhTlclnu1Il8CuhQon6y5vi3tSrbW4nvYDKpPwrT5ZDZ4xkJR4eQN3UB75lJ4TmuJh2STfN05IJfAJJoKUx_Ge7BSn6LWeRosjiAg3AzjWDvdIiigDF54t3LbX_QfS3BlSC225GYpctTS_n0cY04PduYi5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
تصویری زیبا از رعدوبرق دیشب تهران.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71374" target="_blank">📅 20:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71373">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69c9063c46.mp4?token=PyKciRq9wL2jQd8tSijWmRdwdPbDTExQK4YxlkLBpTks4ojz9dJCciJ4w1deSYhAnoXq-IoTo_ceIW83nFE-JdHTMu8hzICa8ociXTcQyVEfAvnvIg1rAB4Ix8bsiJ35LiXN2M57a7algxe8tW8ZhBQYn23U-DlgHhc99clFcnlAA6vgzMSKF_2v6wDU1_a0iOndu1nkySx1c4Z0613YTMFzCgs4sEdOyn2-vSgIAu8kQAk31qaEZ6fGMwNmNwlLgYpcJuMbaKr6HNkdxIjd4o4B2LWtP4viOe2WbabTF1PSR2Rs9SmS-ZzIFV_gZWwlco9rz4YOu0bJwvn-NVKDrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69c9063c46.mp4?token=PyKciRq9wL2jQd8tSijWmRdwdPbDTExQK4YxlkLBpTks4ojz9dJCciJ4w1deSYhAnoXq-IoTo_ceIW83nFE-JdHTMu8hzICa8ociXTcQyVEfAvnvIg1rAB4Ix8bsiJ35LiXN2M57a7algxe8tW8ZhBQYn23U-DlgHhc99clFcnlAA6vgzMSKF_2v6wDU1_a0iOndu1nkySx1c4Z0613YTMFzCgs4sEdOyn2-vSgIAu8kQAk31qaEZ6fGMwNmNwlLgYpcJuMbaKr6HNkdxIjd4o4B2LWtP4viOe2WbabTF1PSR2Rs9SmS-ZzIFV_gZWwlco9rz4YOu0bJwvn-NVKDrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
⭕️
#فوری
؛شورای حکام آژانس بین‌المللی انرژی اتمی امروز، ۹ سپتامبر ۲۰۲۶، قطعنامه‌ای را تصویب کرد که بر اساس آن، موضوع هسته‌ای ایران به شورای امنیت سازمان ملل گزارش می‌شود. این نخستین ارجاع از این نوع در حدود ۲۰ سال گذشته است.
۲۳ کشور موافق قطعنامه بودند.
روسیه، چین و نیجر مخالف بودند.
۸ کشور ممتنع دادند و یک کشور رأی نداد.
🔴
قطعنامه با ابتکار آمریکا، بریتانیا، فرانسه و آلمان ارائه شد.
دلیل اصلی اقدام آژانس، عدم توانایی بازرسان در راستی‌آزمایی کامل مواد و فعالیت‌های هسته‌ای ایران و پاسخ نگرفتن درباره آثار اورانیوم کشف‌شده در برخی سایت‌های اعلام‌نشده عنوان شده است.
آژانس همچنین می‌گوید به دلیل محدودیت دسترسی، نمی‌تواند با اطمینان درباره میزان و محل ذخایر اورانیوم غنی‌شده ایران اظهار نظر کند.
⚠️
اقدام بعدی در شورای امنیت خواهد بود و هرگونه اقدام الزام‌آور جدید در آنجا با توجه به حق وتوی احتمالی روسیه و چین با موانع جدی روبه‌روست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71373" target="_blank">📅 20:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71372">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=r4Yf96A0ErwmztDA1TCGI6lie_L5WMS2BTW2p_68a5RVfnV6zXa4hcBBnaWahtv7p9_-ki6TPuFmucVcPvy_BZEnLwvgiB7G6lwWxtVwh-mhuZbwL7H1KZQngzMV3s-WBIb1f-WEF4VWJ_Y22KdjTbVgQkWsRrgQn_pT1CviD0Tvo5aR1TlzyI8gQgIrAXsbmeF3WpsN4YyADO1vL6bExQ1o-zBfs8Dtj3p6Y3ezYqZjdV6RQyt6l8Fy9XXfPa5Bgrs_etYZDLJF65Vx5OTmIFoAXZnnNWeZQXeOrtTq-ZmONxZ0dH8vYNblEmSjjQ8ZBECAc2hgw-EAbZW08n4LfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=r4Yf96A0ErwmztDA1TCGI6lie_L5WMS2BTW2p_68a5RVfnV6zXa4hcBBnaWahtv7p9_-ki6TPuFmucVcPvy_BZEnLwvgiB7G6lwWxtVwh-mhuZbwL7H1KZQngzMV3s-WBIb1f-WEF4VWJ_Y22KdjTbVgQkWsRrgQn_pT1CviD0Tvo5aR1TlzyI8gQgIrAXsbmeF3WpsN4YyADO1vL6bExQ1o-zBfs8Dtj3p6Y3ezYqZjdV6RQyt6l8Fy9XXfPa5Bgrs_etYZDLJF65Vx5OTmIFoAXZnnNWeZQXeOrtTq-ZmONxZ0dH8vYNblEmSjjQ8ZBECAc2hgw-EAbZW08n4LfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇦
🇾🇪
ساعاتی پیش، چندین حمله هوایی عربستان سعودی در حمایت از عملیات «شورای رهبری ریاست‌جمهوری» (PLC)، مواضع حوثی‌ها (انصارالله) را در جبهه مأرب یمن هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71372" target="_blank">📅 19:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71371">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71371" target="_blank">📅 19:25 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

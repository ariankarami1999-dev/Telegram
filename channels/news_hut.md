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
<img src="https://cdn4.telesco.pe/file/XhC8IC0QxWLVZdd0YMtNThT_mvixZKKB8OUuzvL-FeJo5fHoPDklLNFNfIwaxsbeGGo8S1rlrMLPz7U6ZGiPbjaOjXVF2CQrWHU25mm_400HaX7ttkoZbXw37aQwBIa-RtTBLPAThUO6Pqffni9APzorgRtJ0BROeYBMN5Izoek8OWdv_56tIwbWNdU4fvdc1xdyjR359uusUpecCDKIzXPId9LHLNsb3jZoaDU-opDXtxz5d16B5pS8KEGcYtIA4QSCbasVYKxbwoskt3BskyLhMX5nW2sn0BRf4FLLhVAxv0r79dEAmTpNVruFuSachrFQJvN7FVwd2YvtU8bPkg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 118K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-02 05:47:18</div>
<hr>

<div class="tg-post" id="msg-70490">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/news_hut/70490" target="_blank">📅 02:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70489">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAk7h40rWPZvuuVFSgQolM2I_t3GNiSwmEud6vI8rssTSy63hTo47YNCflHI8FA9ZK__9U9whVe5Dknb5kCntvyKZZ5264jQHU1bbYW258x1N-OYC3IX1wQPP895Sx3X9HLT448y3lSIFFsWNHtsfUwZUy_u99tgCyM7AHWBrSRdUkipQFWZ0vCU9irBazZxIUuIcVVOdYvlvq-GCrrXcroxu_wmKjz7qx_jIs3rnNcpMVfebieAyX_yNuMmfaeLtd7QLPf32LdwWbfwYP6WYeyMGuAB4phaO-ZA3ynEQMaelbpMUkKYKUnHi0MP2pkc6hlYISupaCr0MlR8Q3Zp7A2E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAk7h40rWPZvuuVFSgQolM2I_t3GNiSwmEud6vI8rssTSy63hTo47YNCflHI8FA9ZK__9U9whVe5Dknb5kCntvyKZZ5264jQHU1bbYW258x1N-OYC3IX1wQPP895Sx3X9HLT448y3lSIFFsWNHtsfUwZUy_u99tgCyM7AHWBrSRdUkipQFWZ0vCU9irBazZxIUuIcVVOdYvlvq-GCrrXcroxu_wmKjz7qx_jIs3rnNcpMVfebieAyX_yNuMmfaeLtd7QLPf32LdwWbfwYP6WYeyMGuAB4phaO-ZA3ynEQMaelbpMUkKYKUnHi0MP2pkc6hlYISupaCr0MlR8Q3Zp7A2E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
a1
⭐
کانال اطلاع رسانی سایت:
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/news_hut/70489" target="_blank">📅 02:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70488">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛وزیر خزانه‌داری آمریکا، اسکات بسنت:
«ایالات متحده در حال آغاز بزرگ‌ترین تهاجم مالی‌ای است که تاکنون علیه یک دشمن به کار گرفته شده است.»
او هشدار داده کشورهایی که به تجارت با ایران ادامه دهند، به «منفوران در عرصه جهانی» تبدیل خواهند شد.
🔴
به نظر می‌رسد فردا روز مهمی خواهد بود…
بسنت آغاز فشار اقتصادی جدید علیه ایران را به «D-Day اقتصادی» تشبیه کرده است.
هدف آمریکا، به گفته او، قطع شریان‌های مالی و تجاری ایران و منزوی کردن اقتصاد کشور است.
او به کشورهایی که با ایران تجارت می‌کنند، نفت ایران را می‌خرند یا در انتقال پول آن نقش دارند، هشدار به اعمال فشار و تحریم داده است.
بسنت معتقد است فشار اقتصادی می‌تواند حکومت ایران را وادار به تغییر رفتار کند.
او همچنین هشدار داده اگر ایران به نیروهای آمریکایی یا کشورهای خلیج فارس حمله کند، پاسخ آمریکا سریع و قاطع خواهد بود.
هدف این تهاجم اقتصادی وادار کردن رژیم به فروپاشی یا تسلیم در برابر فشار است.
@News_Hut</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/news_hut/70488" target="_blank">📅 02:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70485">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f407bb9f5.mp4?token=lJG5C4NnWzBu6YauKf_epg7fvuWq-TGkQuJGjuXHDwwx540bHqXP3ibMZwS-m5_epKgZoWAezFj_fvXHEGjh7bHSkynQuFRbCXtbQxecsB5wjXYdMFMr01o4V-zmCy2mRBoFfD0ESIjn3IxsP2kG5h-KFS2OOQV2o-09UVhJsXfopjT0xP-GczYIpcIKXpl38CBkHFTuu7aSnrT5ryAPgoYquOxxYqO8ZtCzUDJ7OVui6etEFQlq6_ZDAAjdr45FfXa4gwCmii0TQ_bi0ypLmyDvkxk952HFysoAwMGMV7FerVjVNUWMemLq1Z7_wOxHEjlk_kcmPeWUiSGmQY5uow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f407bb9f5.mp4?token=lJG5C4NnWzBu6YauKf_epg7fvuWq-TGkQuJGjuXHDwwx540bHqXP3ibMZwS-m5_epKgZoWAezFj_fvXHEGjh7bHSkynQuFRbCXtbQxecsB5wjXYdMFMr01o4V-zmCy2mRBoFfD0ESIjn3IxsP2kG5h-KFS2OOQV2o-09UVhJsXfopjT0xP-GczYIpcIKXpl38CBkHFTuu7aSnrT5ryAPgoYquOxxYqO8ZtCzUDJ7OVui6etEFQlq6_ZDAAjdr45FfXa4gwCmii0TQ_bi0ypLmyDvkxk952HFysoAwMGMV7FerVjVNUWMemLq1Z7_wOxHEjlk_kcmPeWUiSGmQY5uow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
راغفر :
رئیس جمهور مطرح کرد
گران کردیم که مردم نتوانند بخرند و اینگونه مانع قحطی می‌شویم!
@News_Hut</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/news_hut/70485" target="_blank">📅 00:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70482">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g7c-8nhmqr39KzuoReuMtuOPXrZzKsp7onPow1NbQtEcTTB6V-2lQPkJSVZiEa2G7G1-orK6jUIQ5cGy0safl-zktsHmiirYvkuLeCHh-noBhDk0Wj1_QIZmVrfbQiYUKI1KrMh_q5n2vm6OsMGX8wewGHBV-Sp2UCGvT8JqSfwUGxGbEayI1TyXk0nU4go4d0O52YgzQdyzL8jmKJTETDkHyfXKMMTKPk2UQ4ExUU4-7q2NqiaZxqthcV5GG7XxUTm3H_kCziZumS68DJEIHOdVnsexkA2L9NTfB-Nm_xEVL79QClW5kvUUWsNfop1CXnEncSu5za5tR33zHFBoug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FsdaUSqD1K0iLNEO9P7d6KqoaVy6l0hjKZ7W9wll8LVkcRPm4RMdBf1-QtzJPgyLV_0iWWi1GTxnJdQEHsKSKoq11RYZZ3c8BmYZRmJCn5bSSA6Ah7GXJil9k4GSwTSTFHD5nM5tq4k3elvKjGoSMRei_wRTVfVfPleyXxOMLPiKm3fElWLdiCO1cS4b3rq5oABBcM27yvamEo9DoMr6ImfTH5RyiPf9OQC_z2AnJX7x827ZzyKwvzfW6lS9MhBORXHCIVyY0jijX8cDOVN95S0B6t-dWlSLpdu4nGQh3AYa3LHE2dv3Ch-8XuPcs8GfkK-P9oA8hJke8dJDeOGh9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی امروز صبح منطقه آرخانگلسک در روسیه را مورد حمله قرار دادند. این منطقه در فاصله ۱۸۰۰ تا ۱۹۰۰ کیلومتری مرز اوکراین واقع شده است و این اولین باری است که پهپادها به این منطقه دسترسی پیدا می‌کنند.
بر اساس گزارش‌های اولیه، پایگاه فضایی پلستسک هدف این حمله قرار گرفته است. پلستسک یکی از مهم‌ترین پایگاه‌های فضایی نظامی روسیه است که از پرتاب ماهواره‌های نظامی، آزمایش موشک‌های بالستیک بین قاره‌ای و سایر عملیات‌های فضایی استراتژیک پشتیبانی می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/70482" target="_blank">📅 23:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70481">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d033a4797c.mp4?token=rjVhaqHENpLQHezKRPPypKnIPAXBc484ZmRTQkNcREdVO98TfpbZUlbuVJnqoQVDOAxgq69soXxAD2FlB5Q6zue5b-mprIJzIRZeKDMjrrWmCOm-FiaWxUNSekm81girXaoiq5IK9PQacAwfCSVexuH3ha19lV_-p7snQr88uYUN8d0xXxG_VaDXvvk1Pq7CXHgInrL81tDmm8iFKAV9SMqJUPPDH9NXzKn0oJIMyqcNIlIKLfIbsBnZecNjFIb__9H76SxFwgyXfGpfKA6LOQIfgDYqVkQrYstnd28c-t73uI29xPqkKnw5hTphHDkgk1jGvc87XhtEQBjxv8I2hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d033a4797c.mp4?token=rjVhaqHENpLQHezKRPPypKnIPAXBc484ZmRTQkNcREdVO98TfpbZUlbuVJnqoQVDOAxgq69soXxAD2FlB5Q6zue5b-mprIJzIRZeKDMjrrWmCOm-FiaWxUNSekm81girXaoiq5IK9PQacAwfCSVexuH3ha19lV_-p7snQr88uYUN8d0xXxG_VaDXvvk1Pq7CXHgInrL81tDmm8iFKAV9SMqJUPPDH9NXzKn0oJIMyqcNIlIKLfIbsBnZecNjFIb__9H76SxFwgyXfGpfKA6LOQIfgDYqVkQrYstnd28c-t73uI29xPqkKnw5hTphHDkgk1jGvc87XhtEQBjxv8I2hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
رئیس دفتر پزشکیان:
قرار است جانفداها به سراغ ۵ میلیون مشترک پرمصرف برق بروند و بگویند صرفه‌جویی کنن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/70481" target="_blank">📅 23:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70480">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1N2QRsjQqU8lZehj1p3fcUFNNDzu4pieeO-Mj4UpnO9plmpAGpo-z9HuPKwYH9PFCOfaly1vEnqnYmuZ4LEvvx1J6H9Zs-I6EtspGs1y8YrQPUS2rVGnn6-SJA6DdiRcvfoJbRzQKlJ__l0K4FEezz8YXOfiTyZ7-lWPKlt-L7g-MeThC23nay1X0XYIdxunhBNipsWVWTtrnF4RycsIN09I2nAVybJQIKok-kbSDXZOubDH5DTe4KQWMBQmcMtLhptx6_s7ujEXu4av0EuQBelomhz2sf5rp-G1AJhiyACmH-SpRsPxYHuYHtt07ENx5TgD0WaewXnnWmyhoy3RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
محسن رضایی:
اگر جنگ اقتصادی ادامه یابد، حتی یک قطره نفت صادر نخواهد شد؛ نه از طریق تنگه هرمز و نه از هیچ نقطه دیگری در خلیج فارس.
ایران مشارکت یا حمایت هر کشوری از جنگ اقتصادی آمریکا علیه ملت ایران را به منزله اقدام جنگی تلقی خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/70480" target="_blank">📅 23:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70479">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4t6rH3JVuJ5Viba4rWy0KjnzbLl2eNbKNBm6f2FsUwhkWT1wUMpK2RngaHRfZP4ttRiTT2xkdWihcy1yi8JkWq-Jqdl1_gnZwYFd0_aiPKk57CVdvATrr85Q294P5PnPsz62U5ubZRdt_7DzAiFMgwKBLJ8-3AB89m7Dir2vMqY4oHoPiNiVJLrLo7L_MFVZLH1nyzICNKCVlMJu9y8s6utnjNJEju8IaGR1C7sJpkMfjS6bIqrEFZPfBa1AUAuzs5r7mrzQOompYZWnDmSrktc_eNV4QXNoNP68AR-r4rcHooLwtp9uWpGPSLRTsrQjhpQQNw8Nwh5W7te3jLL-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گسترش فرصت‌های سرمایه‌گذاری در وال‌گلد؛ نقره به میدان آمد!
💎
تنوع، کلید موفقیت در بازارهای مالی است. پلتفرم «وال‌گلد» در گام جدید خود این امکان را فراهم کرده است تا کاربران بتوانند در کنار طلا، روی «نقره» هم سرمایه‌گذاری کنند.
🔸
روند یک سال اخیر نشان می‌دهد نقره بازدهی‌های چشمگیری در بازار سرمایه داشته است.
🔸
با این امکان جدید، سرمایه‌گذاران می‌توانند با ترکیب طلا و نقره، یک سبد مطمئن‌تر، کلاسیک و پربازده بسازند.
ورود به بازار جذاب نقره
ورود به بازار جذاب نقره</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/70479" target="_blank">📅 23:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70478">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pabQy0uTLyWGEvV_KviGuf5L-jx7jwVmkFmZvow8wTGOyggGbT_6-lhgqWcRcLnu_Q0VNKRU1pw95kM4Z1nksPUtefbI4tPj5q5BMa6cZuWa0DFGOhr3Af80WLIShRCVSKkmTkIo1CQZzlmuTvQcDgIiU4UO6CGfmqRbY0eSm88yV0YpLrgLZcFQw361CslmoQhD9oPtER_K6QtAcUZaHneSqGeQ8zgRzldAD8L2LqjvfAmiVCz3QxfUj8I3EWibODX_xVZmvFj4O7KzMHVClTOFehgNkmrcLaVK_66tJjWeAUiaTKg-Z8lU4HcZXrlPMH2suOqy403mhVPMlUeerQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تا ۲۰۰ میلیون وام بگیر فوری!
🔥
‼️
با اسنپ‌پی می‌تونی بدون نیاز به ضامن و فقط با یه برگ چک صیادی تا ۲۰۰ میلیون تومن وام بگیری و تو اقساط بلند مدت تا ۲۴ ماه پرداخت کنی
😎
تا ۶ شهریور ۲۰٪ هم تخفیف اشتراک داری
🤩
پس همین حالا از لینک زیر وامت رو بگیر:
👇🏻
https://l.snpy.ir/zj65d
https://l.snpy.ir/zj65d
https://l.snpy.ir/zj65d</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/70478" target="_blank">📅 23:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70477">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇮🇷
توقیف و مصادره در انتظار شناورهای متخلف در تنگهٔ هرمز؛
🔴
نهاد مدیریت آبراه خلیج فارس اعلام کرد شناورهایی که از ترتیبات اعلام‌شدهٔ ایران برای تردد از تنگهٔ هرمز تخلف کنند، در ترددهای بعدی با محدودیت‌هایی از جمله جریمه، توقیف یا مصادره مواجه خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/70477" target="_blank">📅 22:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70476">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QH_g-U3PgFS_1d-SSKHr4kDoY3F4OA1HMsCK_YHfjJ_Kj7rNlmEQ-6f7wTpkRfrKa5NpyDKtTwzT88CMQUd3mNMJM4Fw3_jMg2Lhk8doGGMR-4UhZreuw59egwV0jjoyXP_5lhOsSyguTFEyY_ftrmH4YAakMoBS7ZavqUsK97-OLV_5FxemMdpk-HUn9fHCTy3XrbhcmWH_IFLilMaZXCrG27ftRg40gD9F2COkz9IijC6_trawORfZJZGV5O9hO2y-DbYCCndcdFqHYYVgGUSsj0FlG5K7DfE_ydokri0JEM3gd9k61B-syIERvHWT2qv4R5nergp4sIsGwBFv9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجری عراقی با انتشار این تصویر نوشت به این جنجال پایان دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/70476" target="_blank">📅 22:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70475">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d44391ebe9.mp4?token=HG5FEqbsWH16ZGjvF5g2DgXW6xEI9caZG1WDibHH1DfeK4iGwG4bggwmBl_k1Ec2k0Zso2OJx4nSWQa3knuaK7Wkuhyxfex-efN0inQyX8G8__773YawlGDPLkjVCe-meoNKxTNXnaxfAwOoZIOJ1yntxWFWxP2zbDlnnRw2lCCRpDuI3YzX_ejpRWXqtIh83TQDnM1Gx1DpldqP2TelBCt_Z9NfjicHuNHVErrk7F4qCZg-HS-xSWO3ZFJzf6Wf7zYTCyvBow4aV6SCr3TUu0xIBbhAkOryWxncbIAPGZCWekMH_8ZSsaRvBGRqKMHcXEemjjOCBcAHPh5jDvP8Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d44391ebe9.mp4?token=HG5FEqbsWH16ZGjvF5g2DgXW6xEI9caZG1WDibHH1DfeK4iGwG4bggwmBl_k1Ec2k0Zso2OJx4nSWQa3knuaK7Wkuhyxfex-efN0inQyX8G8__773YawlGDPLkjVCe-meoNKxTNXnaxfAwOoZIOJ1yntxWFWxP2zbDlnnRw2lCCRpDuI3YzX_ejpRWXqtIh83TQDnM1Gx1DpldqP2TelBCt_Z9NfjicHuNHVErrk7F4qCZg-HS-xSWO3ZFJzf6Wf7zYTCyvBow4aV6SCr3TUu0xIBbhAkOryWxncbIAPGZCWekMH_8ZSsaRvBGRqKMHcXEemjjOCBcAHPh5jDvP8Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو سعادت آباد تهران دو تا گروه تیم‌کشی کرده بودن برای دعوا و این شکلی با بیل، چوب، سنگ و هر چی دم دستشون بود، افتاده به جون همدیگه
😳
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/70475" target="_blank">📅 21:51 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70473">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30c15be54e.mp4?token=RWbkMc12tPooBlVnXyVIGtv3VMKhdTpakyxhKI94Ktkrkf6YKcbWRopGWoyZgpojLl3kMLdKqdfr7m1ls7RFKVfWadQE4Q6vPTo-TTBOaZV2dV074-oL1xPpgM27yPxRvjsZBRicF2GTF4CWNqcRkaswTGTyDznVFhkrk-jt9ubkd_Wpc_FlgSnX3pPvET0NAXTvg2xUooe4gh0VgHiiW-akMO8vq6qelJa1OkLYDLceTjuLGvx1Zm3MofV4xE2JCYRDCKPQs6Y9GqmBvyVe3XRg0OVvHLvwN3FU89zWv2OkuBpePn3D4wjtKRsGGGnsB_3UqiKRYN07livEPHAo_FIcfAtISh8Q0RJtn3IXihk1-HDDN0UnKRfH4M0SuQy_FrLyx-9qvIqsRnIWMv99QHMPuKPR4pf7XzesSHwm3Z2xTkkEjSE0eSY0w9T_h3Qk5UBDFft8FhH25t2l1Sw8AaVfAdP2-zixZYAcr-7YV4usjLs4YxgjmVd7_tjzaFbv4xB7nH6VOCB2k5oVRuI7-q0cZQ9TQ2zSIYwT9_OaDkksaJw0fQ5oOSFRogq57Wca9BJvsKB_Yyzn-c5rL8LyKXGM-cl9oQQPwWDO_gSQJpginUAANVT3I_ayJWh02WtefeZuG_9vtoNm-5kjzddCiWLQ8YtOmZjTsfNe4k1u-7M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30c15be54e.mp4?token=RWbkMc12tPooBlVnXyVIGtv3VMKhdTpakyxhKI94Ktkrkf6YKcbWRopGWoyZgpojLl3kMLdKqdfr7m1ls7RFKVfWadQE4Q6vPTo-TTBOaZV2dV074-oL1xPpgM27yPxRvjsZBRicF2GTF4CWNqcRkaswTGTyDznVFhkrk-jt9ubkd_Wpc_FlgSnX3pPvET0NAXTvg2xUooe4gh0VgHiiW-akMO8vq6qelJa1OkLYDLceTjuLGvx1Zm3MofV4xE2JCYRDCKPQs6Y9GqmBvyVe3XRg0OVvHLvwN3FU89zWv2OkuBpePn3D4wjtKRsGGGnsB_3UqiKRYN07livEPHAo_FIcfAtISh8Q0RJtn3IXihk1-HDDN0UnKRfH4M0SuQy_FrLyx-9qvIqsRnIWMv99QHMPuKPR4pf7XzesSHwm3Z2xTkkEjSE0eSY0w9T_h3Qk5UBDFft8FhH25t2l1Sw8AaVfAdP2-zixZYAcr-7YV4usjLs4YxgjmVd7_tjzaFbv4xB7nH6VOCB2k5oVRuI7-q0cZQ9TQ2zSIYwT9_OaDkksaJw0fQ5oOSFRogq57Wca9BJvsKB_Yyzn-c5rL8LyKXGM-cl9oQQPwWDO_gSQJpginUAANVT3I_ayJWh02WtefeZuG_9vtoNm-5kjzddCiWLQ8YtOmZjTsfNe4k1u-7M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🇺🇸
هواپیماهای B-1 Lancer، B-2 Spirit و B-52 Stratofortress و چهار فروند جنگنده F-35 نیروی هوایی ایالات متحده، پیش از آغاز مسابقات «گرند پری Freedom 250» در واشنگتن دی‌سی، بر فراز محل مسابقه پرواز کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/70473" target="_blank">📅 21:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70472">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63aefba4cc.mp4?token=AdSrw5KtM1fuhx2Sr_lJRpGS40Ule5WKuYeUGub5TA0-PUvUYqJ2PS0tJvMLOp9FeAJFYdpB4u0nfyAA9P1-fT1Za-E5gno6cZ0_X-ZvCi8CP2p2ykqRp7BxrYn_VkmDW-Qay8rtFXcaB2wkZVQy5Y32o6KdfEIzx0tlDBC_yGkzLQRHCdbhn6lQG8fqECx982dngnu8I_k69M3HbNQYmkfVd94gjRyentOVYh5_YUfPqmDHwIC_XS1gaLgbyZ6XlZ647Ok9FFI21H9c1e4-iZVx4Ld5c0DuagMYtPfIy2K5FBCkmab2F6BrXRRxmBskOZzXd-snwY2xI9WDScNJKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63aefba4cc.mp4?token=AdSrw5KtM1fuhx2Sr_lJRpGS40Ule5WKuYeUGub5TA0-PUvUYqJ2PS0tJvMLOp9FeAJFYdpB4u0nfyAA9P1-fT1Za-E5gno6cZ0_X-ZvCi8CP2p2ykqRp7BxrYn_VkmDW-Qay8rtFXcaB2wkZVQy5Y32o6KdfEIzx0tlDBC_yGkzLQRHCdbhn6lQG8fqECx982dngnu8I_k69M3HbNQYmkfVd94gjRyentOVYh5_YUfPqmDHwIC_XS1gaLgbyZ6XlZ647Ok9FFI21H9c1e4-iZVx4Ld5c0DuagMYtPfIy2K5FBCkmab2F6BrXRRxmBskOZzXd-snwY2xI9WDScNJKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
وزیر نفت: ۷.۵ تریلیون گاز در جنوب فارس کشف شد.
بیش‌از هفت‌ونیم TCF یا به عبارت بهتر ۷۵۰۰ میلیارد فوت مکعب گاز کشف شده که با احتساب ضریب بازیافت حدود بیش از ۷۲ درصد امکان حدوداً ۵۷۰۰ میلیارد فوت مکعب استحصال گاز وجود دارد.
این میزان گاز معادل این هست که یک فاز پارس‌جنوبی به‌مدت ۱۵ سال بتواند تامین این حجم عظیم گاز را بکند.
این گاز خوشبختانه از یک ویژگی خاصی برخوردار هست و آن اینکه اصطلاحاً شیرین است؛ این شیرین بودن گاز باعث می‌شود که هم هزینه‌های عملیات توسعه‌ای کاهش پیدا بکند و هم هزینه‌های عملیات بهره‌برداری.
در کنار این حجم گاز، حجم عظیمی میعانات گازی را ما داریم که مجموعاً ده‌ها میلیارد دلار به‌علاوه ارزش ذاتی آن گاز برای کشور ثروت جدید به بار آورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70472" target="_blank">📅 20:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70471">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IL31Mq9BIrwRegwUotPOsPnOTfQq3WyV9WGFbN2OPGmDtNCWk-Vi4tNx8_dZWmeRGAXRSmbvbB4cZOINgUpGHSy9aCdoHSaOCNiTLrwZn45erdpwirtwCntXONvhdbdXS7eu6M2DNriQzLnPl4eiL48GdmBlpYWNZf9GxjYpccsjR-nGU6znfexASPXj3sK-9J0_LJ7vqF9jrYVwzvKtGce8jSmONvayZRHqS96dUbW__Pyx3iU1z9eMNKyn2d3W2j5e1FsiBu_Fd8K6ZPuiPakNtY2-H7yyoGEK6d7lOOh9ptHosnEt9c_dSkkIhNv3_ADnxgRBW4QLGuYEQgZ9oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف در مورد سیاست های آمریکا:
واردات گوشت منجمد برای مهار قیمت گوشت؛ خب، شاید این راهکار جواب بدهد.
اما برنامه برای اوراق قرضه چیست؟ واردات بازدهی‌های منجمد؟ خریداران مسکنِ منجمد؟ یا حقوق و دستمزدهای منجمد؟
سیاست خارجیِ منجمد، اقتصادی منجمد به بار می‌آورد.
تنها چیزی که همچنان در حرکت است؟ بومرنگِ ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70471" target="_blank">📅 19:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70470">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fd998e89b.mp4?token=DmuLENScqdGwUEK96qf_3tkyAXyaQwaqiJuV5uqZPoHlN8RG14E6Z67JMtDrA2Awn4ujZEFG2uoutBLb7vIAEh2bn_JuhJvvzO83avRP_jeXGJBePCVok2o9EWr89-1BRXIOOjR2ZNNq3WxKYo4mRczKP9mI5SuFM68Wg92tDjuO9fzWwnewucqN7cZ1a40cJHiZdoqXvZqZHMjM0XWxTiYuu2i1LuRVpcjIqekaowz66gO2C-u4aOyg3OtHhz8ltZe2CVmyZrwKTrMNJXzdxZHs7fna8G8eAWcDTTG_S2UZSUBksSrkADh7bLX2bRpRUfPD3Kb4OzZ_gwYrXJan_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fd998e89b.mp4?token=DmuLENScqdGwUEK96qf_3tkyAXyaQwaqiJuV5uqZPoHlN8RG14E6Z67JMtDrA2Awn4ujZEFG2uoutBLb7vIAEh2bn_JuhJvvzO83avRP_jeXGJBePCVok2o9EWr89-1BRXIOOjR2ZNNq3WxKYo4mRczKP9mI5SuFM68Wg92tDjuO9fzWwnewucqN7cZ1a40cJHiZdoqXvZqZHMjM0XWxTiYuu2i1LuRVpcjIqekaowz66gO2C-u4aOyg3OtHhz8ltZe2CVmyZrwKTrMNJXzdxZHs7fna8G8eAWcDTTG_S2UZSUBksSrkADh7bLX2bRpRUfPD3Kb4OzZ_gwYrXJan_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
❌
🇮🇱
نتانیاهو و ترامپ در میدان انقلاب تهران اعدام شدند
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/70470" target="_blank">📅 19:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70469">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join
Join Join Join</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/70469" target="_blank">📅 19:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70468">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mg8HgP0PIb0Xr4Utn-UqTzB4dZp7_9T5NrcAj_EBKK4p9qzrhbltj94eVQWs_sMEVfdz5YGvlaKvZvktt8Rg_CUe0x5sAj-Qhxd_x_BFBiF1sSI_AlYIzI2zDSbu-L9omT2eV8NM3ZGRkN_BtEX0oOD6BRWRhu302HScEOtDjUYvTkFssWajN2_N-jRadFJcr_YMsgwvW-762XrB8YlG3SWZDlWjb_1eLpzwQUu2X6d7y6mEohZx0rwBPU3bVFMxG1QrtlHewfbkLUxw49gheJWv_or4p1aGEZRJT49uFXd__45EdtUFpyYY4mEBZzZYVIwuYjP5wGm7cFQ_7TaRtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/70468" target="_blank">📅 19:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70467">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f7dd3a967.mp4?token=OOVSTJVWwcEnrXguNu2cWt3uLCXuMBVW7AD-jSDrLPIrZnlFqB9XUudnzmyGsghP4bJXc9XPOE8QLYHRdENrgCDM62hJcmKEbD8WauX8l6PfCqlL4m5PWNGwKuUu948EpNXLk-g4InzB23Ka9f1QWXSM8zKQki3jl2diFx42fRvCf6FbDKm6Nf6d-uedxc0gC6k9CSdGNIXV_NxWoi17n1e_LJZmjTzJMPSwnSbbkQwI_rz3jGuEL70yaraIWQj3TZa3FR6ZEcXjc_JFg32bwzSf3Pu0UCkbzX05erXqwZqs_Cmn33PNQq-zDv2_6VbrG51TymP1xch-4fDrLwjI4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f7dd3a967.mp4?token=OOVSTJVWwcEnrXguNu2cWt3uLCXuMBVW7AD-jSDrLPIrZnlFqB9XUudnzmyGsghP4bJXc9XPOE8QLYHRdENrgCDM62hJcmKEbD8WauX8l6PfCqlL4m5PWNGwKuUu948EpNXLk-g4InzB23Ka9f1QWXSM8zKQki3jl2diFx42fRvCf6FbDKm6Nf6d-uedxc0gC6k9CSdGNIXV_NxWoi17n1e_LJZmjTzJMPSwnSbbkQwI_rz3jGuEL70yaraIWQj3TZa3FR6ZEcXjc_JFg32bwzSf3Pu0UCkbzX05erXqwZqs_Cmn33PNQq-zDv2_6VbrG51TymP1xch-4fDrLwjI4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی مشهد طرفداران حکومت که علیه قالیباف شعار می‌دادن و خواهان انتقام خامنه‌ای بودن برخورد شد و متفرق کردن
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70467" target="_blank">📅 19:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70466">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c51d98cde4.mp4?token=OlpDSj3M82RSuCW5ScHa-K3szSJQ9tQLdBWkGrf4GCyh2j9c-s1zPqAp3FxEv2vPdCb6w5SjzkBrUw10hL48bR0ruTiNTygMNLmHxoomHZf6wlBX34PKWe3Vq1JY5OW7MMp_nlTTjsR3s549NdBXcNYXWAPLEFI9FuB672UkPlSNJf7MQB5FVYvsCLqe6zvN6HmXbeafVlLaeQXoZzhJqC6O3mXHhqU9Mg91rwLFyrvRiGo9ofuPge8xqzE4AlKoh7H929UvkcQg_wX9jzaMyxGXY6uiHwGJFGpx3-fYtBo6ctbHlJL5-rIuHiwqQ53oFbII0VWXDjuLUcm8vOuYFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c51d98cde4.mp4?token=OlpDSj3M82RSuCW5ScHa-K3szSJQ9tQLdBWkGrf4GCyh2j9c-s1zPqAp3FxEv2vPdCb6w5SjzkBrUw10hL48bR0ruTiNTygMNLmHxoomHZf6wlBX34PKWe3Vq1JY5OW7MMp_nlTTjsR3s549NdBXcNYXWAPLEFI9FuB672UkPlSNJf7MQB5FVYvsCLqe6zvN6HmXbeafVlLaeQXoZzhJqC6O3mXHhqU9Mg91rwLFyrvRiGo9ofuPge8xqzE4AlKoh7H929UvkcQg_wX9jzaMyxGXY6uiHwGJFGpx3-fYtBo6ctbHlJL5-rIuHiwqQ53oFbII0VWXDjuLUcm8vOuYFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
علی خامنه‌ای، بهمن ۱۳۸۹:
زمان شاه حکومت وراثتی بود. مردم هیچ نقشی نداشتند..
🇮🇷
صداوسیما ۱۸ اسفند ۱۴۰۴:
مجتبی خامنه‌ای فرزند علی خامنه‌ای بعنوان رهبر سوم ج.ا انتخاب شد
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70466" target="_blank">📅 18:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70465">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e23c4e23a.mp4?token=NcXHP4kol4QnZt_xhZnKlLGku0rINiciPqrTfGGRpwOTgjPRlrWjQ6I8IQQsHTHIYIh7pE_-rEQA4Gczsx1iv0Q3ubrzxOBYnoq9I14Y408xkkeMi9mehb8ACp1GLPSt7t37hkibxT-KL1aD831Wo6-NB70zhM7UE1xr65maf7rUcxqQHpOizkJeNzLhG5AKHJUzyJxCm51zIMOGDVT35wZbOSzAZ9xf1_GTE97kVBej0Tq4w0-ZPYJoabVfgMIiipdazlKVi-jwVadqvNh79L_XFkZq692Ls8n_msF9bmK9D_Iw5t5gOuJuCuYuouKIiU1BqZ8GK8m7Otv79a96RnsWda3tKI89g2OnSdNRY-U2Ofxsu3Rplh1VxdOkrgn-9Se3Pyi4Sqg2cUo28sQgfD1y15pURV75U-lHacK5gx-w0cEVQBukkE7nD8sZZYNFpFKNscqhvhOaK7mqYBNM8tKz5xjtV9zV0DPKj-EmA98GqVzh3z73TLcuX0yiLSH65AMlhU4lDlkUEPfZIOGKVKrF4d8m5WyS6WxlPCk3D0mwSGmvXLuUgQn_HShuZsDXxEf7Z5ZAxiFt1RTw5g9PYI10n0RnhnDx7XtrZCoZu4eEN0-Fe2OXXMK4Vjo-T96P2apSLxvHvyBhXg-glMBN70ppTkDUBI26s1tdpG-R3zk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e23c4e23a.mp4?token=NcXHP4kol4QnZt_xhZnKlLGku0rINiciPqrTfGGRpwOTgjPRlrWjQ6I8IQQsHTHIYIh7pE_-rEQA4Gczsx1iv0Q3ubrzxOBYnoq9I14Y408xkkeMi9mehb8ACp1GLPSt7t37hkibxT-KL1aD831Wo6-NB70zhM7UE1xr65maf7rUcxqQHpOizkJeNzLhG5AKHJUzyJxCm51zIMOGDVT35wZbOSzAZ9xf1_GTE97kVBej0Tq4w0-ZPYJoabVfgMIiipdazlKVi-jwVadqvNh79L_XFkZq692Ls8n_msF9bmK9D_Iw5t5gOuJuCuYuouKIiU1BqZ8GK8m7Otv79a96RnsWda3tKI89g2OnSdNRY-U2Ofxsu3Rplh1VxdOkrgn-9Se3Pyi4Sqg2cUo28sQgfD1y15pURV75U-lHacK5gx-w0cEVQBukkE7nD8sZZYNFpFKNscqhvhOaK7mqYBNM8tKz5xjtV9zV0DPKj-EmA98GqVzh3z73TLcuX0yiLSH65AMlhU4lDlkUEPfZIOGKVKrF4d8m5WyS6WxlPCk3D0mwSGmvXLuUgQn_HShuZsDXxEf7Z5ZAxiFt1RTw5g9PYI10n0RnhnDx7XtrZCoZu4eEN0-Fe2OXXMK4Vjo-T96P2apSLxvHvyBhXg-glMBN70ppTkDUBI26s1tdpG-R3zk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قرار آخرشب خوانندگان پروین ملکوتی و حمید قنبری محصول سال ۱۳۴۹:
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70465" target="_blank">📅 17:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70464">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76845d14b.mp4?token=MpLzQux7iycYwNalio5qQ9g4v7PT22DjDDU6HXRgQYdpqISzQwnie-hCcoNQgiJExVIRY_K6uYS2Z9gedZbZw-17bSppKxicRmwR7pvmst4VlZQMSlxrF8z1n90yMPmCkmF_SyY9fRtq1tMXVwT306blJOSRl1oLY1qBK7K830E8GaXVLikgSMrvIWfWnQ8IrLyt0EUm31mBslZgMr3JtCj6Wk0LVMBJU4mdGLxutjO2tBqXVSpcXsGYFNcAp2a9yEGY05wF-Hl6LlI3hq9HHFl2fmHBiDW-W6jo0q-wk1iAVDCsz7J8Fhr49joeyp0OV7S1QcsnLCHpgIH4aO_3Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76845d14b.mp4?token=MpLzQux7iycYwNalio5qQ9g4v7PT22DjDDU6HXRgQYdpqISzQwnie-hCcoNQgiJExVIRY_K6uYS2Z9gedZbZw-17bSppKxicRmwR7pvmst4VlZQMSlxrF8z1n90yMPmCkmF_SyY9fRtq1tMXVwT306blJOSRl1oLY1qBK7K830E8GaXVLikgSMrvIWfWnQ8IrLyt0EUm31mBslZgMr3JtCj6Wk0LVMBJU4mdGLxutjO2tBqXVSpcXsGYFNcAp2a9yEGY05wF-Hl6LlI3hq9HHFl2fmHBiDW-W6jo0q-wk1iAVDCsz7J8Fhr49joeyp0OV7S1QcsnLCHpgIH4aO_3Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فارس این ویدیو رو با عنوان «تغییر مهمی که در پدافند ایران رخ داد» منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70464" target="_blank">📅 17:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70463">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a699022499.mp4?token=vFYlOp1b34zhee4DL-UUdLnEz7gtHx7zQOOjp_GNoxUZ8lJi4v_PIetzBtSf7IAZlOF4jP95RHzM31YSTLhoI5tw_nh9F1Y_y8Jm9a84a1jey6ndYOi9QOw3ts8qADm43VDXwXlzrK2ObUfjfzVcvlSp_nHqq9vKQqYOYh2tjBhoSXP7elscvtTTsmwRzVwpZXvGLGMd8ZmVOwJ9RdmfAxCLbtx4FPRDJ4d5VRewGs0XMWZcVLkH3unH46ijh9pNYTJuRtKwVGmEscVth0bKMwudjsG2nj5mfRkNqezDejCgmqiQuiWU18gn0mMsGaNqOzxxU2hiD0SjTGjxfP2uxA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a699022499.mp4?token=vFYlOp1b34zhee4DL-UUdLnEz7gtHx7zQOOjp_GNoxUZ8lJi4v_PIetzBtSf7IAZlOF4jP95RHzM31YSTLhoI5tw_nh9F1Y_y8Jm9a84a1jey6ndYOi9QOw3ts8qADm43VDXwXlzrK2ObUfjfzVcvlSp_nHqq9vKQqYOYh2tjBhoSXP7elscvtTTsmwRzVwpZXvGLGMd8ZmVOwJ9RdmfAxCLbtx4FPRDJ4d5VRewGs0XMWZcVLkH3unH46ijh9pNYTJuRtKwVGmEscVth0bKMwudjsG2nj5mfRkNqezDejCgmqiQuiWU18gn0mMsGaNqOzxxU2hiD0SjTGjxfP2uxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی برزیل یه مرد همجنسگرا رو مجبورش کردن برای اولین بار یه زن رو در آغوش بگیره! اونم از شدت ناراحتی بیهوش شد و از حال رفت
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70463" target="_blank">📅 16:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70462">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
این زن و ‌شوهر بعد ۶۰ سال زندگی مشترک اینجوری باهم رفتن برای خانومش کارای زیبایی انجام بدن.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70462" target="_blank">📅 16:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70461">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd43a5dfd.mp4?token=KZNeMmqJfXH2GHkCa3pHCNLqF8luWH86T__ICQTiZ6yxWRSt361U7VUrd-hChN4QJ7hSwSK0aUcRpLLtd7_5L8PB63liRp0izjOaFK1OVhRKaIkb6zo5pRmtIPhCvWAakp4ZuTjd9-VR9WtF3kQUTAZLejp5M9w9R9hYQ_5KIessLvT-pqVAYRKMvYrIiHxpURyziAA6W8dx2Gqf3eb6PzuUhfrPYwmHlvS8UX8Rto5t6qE2owpKkwh-kyVPfGmjxa4Hj1LRtzuOUgGzkKSyODIEBTJNUYyYzcj6_sc1yFk1giZjIMbs34iw5XpmJrYNmfQX8OdHm697Sxy2HDz3gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd43a5dfd.mp4?token=KZNeMmqJfXH2GHkCa3pHCNLqF8luWH86T__ICQTiZ6yxWRSt361U7VUrd-hChN4QJ7hSwSK0aUcRpLLtd7_5L8PB63liRp0izjOaFK1OVhRKaIkb6zo5pRmtIPhCvWAakp4ZuTjd9-VR9WtF3kQUTAZLejp5M9w9R9hYQ_5KIessLvT-pqVAYRKMvYrIiHxpURyziAA6W8dx2Gqf3eb6PzuUhfrPYwmHlvS8UX8Rto5t6qE2owpKkwh-kyVPfGmjxa4Hj1LRtzuOUgGzkKSyODIEBTJNUYyYzcj6_sc1yFk1giZjIMbs34iw5XpmJrYNmfQX8OdHm697Sxy2HDz3gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت گمرک شهید رجایی بندرعباس، ۲۹ مرداد ۱۴۰۵:
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70461" target="_blank">📅 15:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70460">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">1
💵
= 200.000
💸
🔼
یک دلار آمریکا=دویست هزارتومان
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70460" target="_blank">📅 15:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70459">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‼️
🇮🇷
سعید آجورلو، عضو تیم رسانه ای هیات مذاکره کننده و از نزدیکان قالیباف:
آمریکا از مسیر جنوب تنگه هرمز تا روزی ۹ میلیون بشکه نفت عبور می‌دهد
مسیر جنوب تنگه هرمز همین الان دارد کار می کند
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70459" target="_blank">📅 15:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70458">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/155fedd97c.mp4?token=en_6znRl9e8zRirGmmCo-_dv8JJIFEmFIWJCp2JXMAkCREzUpgR5jpe9fO_mvL4XCqQ0qfd5KzDYdicSG4-b9xRxw5vtr7k2_0HoAHcQaSLVc2cLves9zeu5Eku4II4fHxf8dLY14_0Ht0C6hh4nhoKCkcJLPV4cXD5C9EftMMnT4wTbbdu2aFlEQPFG3kDHlR11L8CZFJifoF9pJR1uvWhiF-4I5EtOUyWkuoI3EabxM_mQ0b6_qwQnfnM-pLBr_Ls2O-5x-V9PFa5m_n-WaQctefNzrQtpdGBlzANtWuMs4OAznBE_vhlPe8g6RixOPeqH5eh_WMjaFzdclo3MiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/155fedd97c.mp4?token=en_6znRl9e8zRirGmmCo-_dv8JJIFEmFIWJCp2JXMAkCREzUpgR5jpe9fO_mvL4XCqQ0qfd5KzDYdicSG4-b9xRxw5vtr7k2_0HoAHcQaSLVc2cLves9zeu5Eku4II4fHxf8dLY14_0Ht0C6hh4nhoKCkcJLPV4cXD5C9EftMMnT4wTbbdu2aFlEQPFG3kDHlR11L8CZFJifoF9pJR1uvWhiF-4I5EtOUyWkuoI3EabxM_mQ0b6_qwQnfnM-pLBr_Ls2O-5x-V9PFa5m_n-WaQctefNzrQtpdGBlzANtWuMs4OAznBE_vhlPe8g6RixOPeqH5eh_WMjaFzdclo3MiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
شبکه سه صداوسیمای جمهوری اسلامی به طور آشکار بارون ترامپ، پسر رئیس جمهور آمریکا را تهدید به ترور کرد
؛
در این ویدئو، اطلاعاتی درباره رفت‌وآمد بارون ترامپ و محل‌هایی که می‌توان او را هدف قرار داد، نمایش داده می‌شود.
سازندگان ویدئو مدعی‌اند این اطلاعات از طریق زنی به دست آمده که با عبور از تدابیر حفاظتی، دیداری خصوصی با پسر ترامپ داشته است.
وب‌سایت حکومتی تبیان نیز این ویدئو را با عنوان صریح و تهدیدآمیز «بارون ترامپ را کجا و چطور بکشیم؟» بازنشر کرده است.
خبرگزاری تسنیم، نزدیک به سپاه پاسداران، در ماه ژوئیه نیز ویدئویی مشابه درباره ملانیا ترامپ منتشر کرده بود که در پایان آن بارون ترامپ تهدید می‌شد.
سرویس مخفی آمریکا در آن زمان اعلام کرد از محتوای منتشرشده آگاه است و هر مطلبی را که تهدیدی علیه افراد تحت حفاظت تلقی شود، بررسی می‌کند. سرویس مخفی آمریکا تاکنون واکنش جداگانه‌ای به ویدئوی تازه نشان نداده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70458" target="_blank">📅 14:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70457">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/625bbb5ced.mp4?token=cPu6LgGA2hJ8a4plcsEE0D3Rn3jqTroxOkiXE2RduEpHjj4NArnKi-spvVAgTD-W3G1U5AyMFRYg2eyRQhQJ_f0L8QnjP_eLjAfJWnRDrhYxZXJDBePfuqynwNiSBNv_BtYZ98NxImmD6djhuo0_JwK8r4KsXFTOEoT7LGvXk3yZVa2yTp9Md9TE4Of4grffd80txyF-7wki3uoy7QUoKF22HWWBSIaQq0L7kN1xY_awR0g0VfmHv0P7R3-77fedyEHxxfZuK_eGMdiCjmhG93DfTi2rTByfBYWTZwMkW_niKr4wXt7xR46aZ9gGVPOo0_FeQvejTFaYu1C6LzQg8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/625bbb5ced.mp4?token=cPu6LgGA2hJ8a4plcsEE0D3Rn3jqTroxOkiXE2RduEpHjj4NArnKi-spvVAgTD-W3G1U5AyMFRYg2eyRQhQJ_f0L8QnjP_eLjAfJWnRDrhYxZXJDBePfuqynwNiSBNv_BtYZ98NxImmD6djhuo0_JwK8r4KsXFTOEoT7LGvXk3yZVa2yTp9Md9TE4Of4grffd80txyF-7wki3uoy7QUoKF22HWWBSIaQq0L7kN1xY_awR0g0VfmHv0P7R3-77fedyEHxxfZuK_eGMdiCjmhG93DfTi2rTByfBYWTZwMkW_niKr4wXt7xR46aZ9gGVPOo0_FeQvejTFaYu1C6LzQg8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هیبت الهلبوسی مادرجنده، رئیس پارلمان عراق:  ما به قالیباف گفتیم اسم خلیج ، خلیج عربیه ، اونم گفت شما برای خودتون یه اسم دارید و ماهم یه اسم من بهش گفتم پدرانمون بهمون خلیج عربی رو آموختن ، اونم گفت هرکی یه اسم صداش میکنه! آخرشم به دیدار رئیس جمهور که رفت…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70457" target="_blank">📅 14:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70456">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2228bf806.mp4?token=GOPYx-_57a240OO0B_P9fL51vJk9KLoSysf4RlGVKiC5JnLdBLuurHrKdePO7I0tmcP6bo72xQbuQgknVMwoLwA9qJ9TEVO-kNyIynEep8y5U9AEfuGF4V5ZJ4XyJGO-nvvh4SX7WGuGQi4a04apriz6NZ67Tx-Fid56DeRuxqqYKSdFPPTLFjKd9aEXzk3JYWljniK-hUlIkKNYZXXx53_tkYK146ZNstn0k1mqoTEuWij22xcyZcfGRPHWLmzc7aaPms4tT8utq9ypeGWkHc9gYrsA6i2uUpzZvxL4eGkAPgsQDlMmKLf8JQKNiBP-0eeZVScJHMAAqZHLnIYc4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2228bf806.mp4?token=GOPYx-_57a240OO0B_P9fL51vJk9KLoSysf4RlGVKiC5JnLdBLuurHrKdePO7I0tmcP6bo72xQbuQgknVMwoLwA9qJ9TEVO-kNyIynEep8y5U9AEfuGF4V5ZJ4XyJGO-nvvh4SX7WGuGQi4a04apriz6NZ67Tx-Fid56DeRuxqqYKSdFPPTLFjKd9aEXzk3JYWljniK-hUlIkKNYZXXx53_tkYK146ZNstn0k1mqoTEuWij22xcyZcfGRPHWLmzc7aaPms4tT8utq9ypeGWkHc9gYrsA6i2uUpzZvxL4eGkAPgsQDlMmKLf8JQKNiBP-0eeZVScJHMAAqZHLnIYc4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هیبت الهلبوسی مادرجنده، رئیس پارلمان عراق:
ما به قالیباف گفتیم اسم خلیج ، خلیج عربیه ، اونم گفت شما برای خودتون یه اسم دارید و ماهم یه اسم
من بهش گفتم پدرانمون بهمون خلیج عربی رو آموختن ، اونم گفت هرکی یه اسم صداش میکنه!
آخرشم به دیدار رئیس جمهور که رفت ، رئیس جمهور بهش گفت که بهتره اسمشو بزاریم خلیج اسلامی که کسی ناراحت نشه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70456" target="_blank">📅 14:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70455">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">💵
دلار: 1,980,000
🔼
هرگرم طلای ۱۸ عیار: 21,907,000 تومان
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70455" target="_blank">📅 13:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70454">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd4541c3f.mp4?token=NwwgvAJcxwx1O94uf5HkcA4m3X97lVX2Kf_iNB4-9u2HE75jy-B_wHIfPCK3kJjNFYNg1MATViNdAON3STLP-NiHNOqEE8uh833PNG6zTPeas07GYIuXlY4FfamD_KEqI4LUWOqrWa4WNi6hrz_gO56d-zrnRuVT63wZNy0zlLol5Mo5A4BAZnZRf75z_Ke2kjCnrMTVw-t6Cu4iWtD6DvPC0on-B1c6Ueg_bIYDv5rXThS-S96ER8saSWARDFutXgdioqSznM2g36J0JdD7LYlnGSPlB8LUoz54E0edSq8_KQFKobiqkDPRoTfOkZ79j5yvuf5oqb54WJQDmCEbdEFZiv97RKhCbXeNWGOKGAuvunQDHARaFt88tTC-3BZ5aPPuZl9werMQUYbGuvPafRyjW_M78-tbRNJ7wxZ8dMko755X1mR3T3NwfmhPXPkPf4D63FuquioSXePotFiLe2GVfmt-J9vMG538LHQXVjo4PB_E0qQ4a6aDcnMrOSKyQxeQEwobPgB90-Hf5rWjmOeDaX8YYs6npQAhblFKzThdZ8uYTSsxQy6XvsWS9qJcF5F3gGyjmGe7Mb66GRjQqoYwYdX_iTLznr_xl0uSMgs2M-VGLK2CP7orV3Lna1Vwf5OH_2d-TsL6o02vwEu1RPeVFXspPMwNVdSwSL5T-gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd4541c3f.mp4?token=NwwgvAJcxwx1O94uf5HkcA4m3X97lVX2Kf_iNB4-9u2HE75jy-B_wHIfPCK3kJjNFYNg1MATViNdAON3STLP-NiHNOqEE8uh833PNG6zTPeas07GYIuXlY4FfamD_KEqI4LUWOqrWa4WNi6hrz_gO56d-zrnRuVT63wZNy0zlLol5Mo5A4BAZnZRf75z_Ke2kjCnrMTVw-t6Cu4iWtD6DvPC0on-B1c6Ueg_bIYDv5rXThS-S96ER8saSWARDFutXgdioqSznM2g36J0JdD7LYlnGSPlB8LUoz54E0edSq8_KQFKobiqkDPRoTfOkZ79j5yvuf5oqb54WJQDmCEbdEFZiv97RKhCbXeNWGOKGAuvunQDHARaFt88tTC-3BZ5aPPuZl9werMQUYbGuvPafRyjW_M78-tbRNJ7wxZ8dMko755X1mR3T3NwfmhPXPkPf4D63FuquioSXePotFiLe2GVfmt-J9vMG538LHQXVjo4PB_E0qQ4a6aDcnMrOSKyQxeQEwobPgB90-Hf5rWjmOeDaX8YYs6npQAhblFKzThdZ8uYTSsxQy6XvsWS9qJcF5F3gGyjmGe7Mb66GRjQqoYwYdX_iTLznr_xl0uSMgs2M-VGLK2CP7orV3Lna1Vwf5OH_2d-TsL6o02vwEu1RPeVFXspPMwNVdSwSL5T-gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طرف رفته ماشین "شاهین" صفر کیلومتر خریده، بعد بهش گفتن با مانیتور؟ اونم گفته آره؛
حالا که ماشینو تحویل گرفته دیده مانیتورش روشن نمیشه، دست انداخته پشتش بازش کرده دیده توش مقوا گذاشتن..
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70454" target="_blank">📅 12:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70453">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNrlstaY-OElzmcghYzTA3uyRqgBjuym_SUL_1vPcX9xpHI0iKwDOG6vjeD2tXMbTQXa2Eie75L3HOSfPtxevdfPiFpPpyXAEebKFEKbu26fKofsy2FFrZnTdOuSypdVaDdHoaRP0QJVjQIMglsf-gwCwsnq1iEc6Fq2pYvhPkQrffoE1C-IhHdhnrfFhV_7pvf4c-JrbhYWXpfMLsKNyncbmJdwr2ZcQS_qHbvpDEcse2Vw3IzD7-wvhbyoqd-X3YPsxNdI_QaU5pu70oAD0vTosjt8rv4ckRiK0FD_hFWYBPbfWHGb9OfUmJvkwok6DM9RVtMOZmUfe27mVxLxjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد کنکور و امتحانات نهایی قیمت چادر های تک نفره حدود ۵۰۰ هزار افزایش یافته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70453" target="_blank">📅 12:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70452">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/news_hut/70452" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70452" target="_blank">📅 12:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70451">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YozeQ7qhI4vdffPZUHi8SlAAchECiYtaBVw_qLA0rXsQjdncal8oB7hQE964vhja525xiXaTmiSWSrhnhOrZPdQtEXBHqHd2K3_wr6jPF_50zqbjk8lR_wOvGtkXLjPOICjkwo6TfJsz3W7akOI4Shgt009iK3fSFzmurHLTRQEMuEzJV1ZIeVgGMaFY-CWOr1MqhXno6sG_Ef3Um5SAC4K7vKXb_b6nLbP_yB2NnrCAtwqtmankskxvp7b8WnGcjc7KISpMjlXLNfesy2R49byL6GCuTXWsgPHwWsvQ1fNxSraV3CnS3RgxNA0d4zOb9uJ52AI2BxPcUhxZd6kk2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r1
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70451" target="_blank">📅 12:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70450">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/25b2c22e49.mp4?token=CSFEOUKsgH0UxaZJ-TWFo-mmNbw7iVwt5EeZolaA-Nin5dJ_gV4i3p93SEwxKVc6iIRx2fcfRzDfoNpkELULWDPhjYlePNznnKSv4nnnxzSwDYc2Ez29qd-OVp6YvJWQAlhf4zy2-kp-FWhIvEatchTq4327vnmd3aB_EA49vHX0xMSUZ2G6xhYVra2armZsaQI-Sca25FGVigqi86o23L8Sj8FWP_LZYyokYJPFeDihAXz4yt0LJt8vGz7ujihCQezR_ieOrKXfqhHCQVC67KRu9a1rsFAxQOSya_gFIRZCO3PaI9cMbKgdhzjgwEUZvHNlGkWAbdQLblC8MUUi8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/25b2c22e49.mp4?token=CSFEOUKsgH0UxaZJ-TWFo-mmNbw7iVwt5EeZolaA-Nin5dJ_gV4i3p93SEwxKVc6iIRx2fcfRzDfoNpkELULWDPhjYlePNznnKSv4nnnxzSwDYc2Ez29qd-OVp6YvJWQAlhf4zy2-kp-FWhIvEatchTq4327vnmd3aB_EA49vHX0xMSUZ2G6xhYVra2armZsaQI-Sca25FGVigqi86o23L8Sj8FWP_LZYyokYJPFeDihAXz4yt0LJt8vGz7ujihCQezR_ieOrKXfqhHCQVC67KRu9a1rsFAxQOSya_gFIRZCO3PaI9cMbKgdhzjgwEUZvHNlGkWAbdQLblC8MUUi8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
یه دختر ایرانی رفته یکی از روستاهای روسیه فیلم گرفته و نتیجه‌اش قراره شوکه‌تون کنه!
فرض کن یه دختر ۱۰/۱۰ داره لاستیک تراکتور عوض میکنه یا سیب زمینی جمع می‌کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70450" target="_blank">📅 12:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70449">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0832bfae35.mp4?token=tLBlE-xBF-pD1yhDgsGdyAlYWTtBqe4tvunurEpKx4k7FDbQ7UiygORLQMEPG4ztkajrlzj13XxfBfBqyjDKd8P71GACJO023tD2zdBpvg-fzycq9ByfXev24HORR_XVWn_fvSBoiCGXRNOWngIIpTFHiAVPotdxI1EYSQu4aFSMd1Q0HQKwuuNm3Iaz3E0fagb7sKefieBEJdEFUctAKZsocaOvAhHvPYXGgJZgAgfDXF4k4hHr0_4q-z-iKGY-lUmvPTo8X1UUaAAYO7MpIc5HLu3hPCbvU2D4mlghxGbTb_2K46HqEt5BVrHLEq5L3OSItJ7gJLz7EngCON-SfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0832bfae35.mp4?token=tLBlE-xBF-pD1yhDgsGdyAlYWTtBqe4tvunurEpKx4k7FDbQ7UiygORLQMEPG4ztkajrlzj13XxfBfBqyjDKd8P71GACJO023tD2zdBpvg-fzycq9ByfXev24HORR_XVWn_fvSBoiCGXRNOWngIIpTFHiAVPotdxI1EYSQu4aFSMd1Q0HQKwuuNm3Iaz3E0fagb7sKefieBEJdEFUctAKZsocaOvAhHvPYXGgJZgAgfDXF4k4hHr0_4q-z-iKGY-lUmvPTo8X1UUaAAYO7MpIc5HLu3hPCbvU2D4mlghxGbTb_2K46HqEt5BVrHLEq5L3OSItJ7gJLz7EngCON-SfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی ساحل میانکاله مازندران، حامیان حکومت با چادر دست به اعتراضات زدن و اعلام کردن مردم رسما دارن لخت میشن، ما دیگه تحمل نداریم، یا دولت برخورد میکنه یا خودمون دست به کار میشیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70449" target="_blank">📅 11:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70448">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⏺
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:عاصم منیر فردا به تهران سفر می‌کند
این سفر در راستای تقویت همکاری‌های دوجانبه ایران-پاکستان و ادامه کمک‌های پاکستان برای کمک به تقویت صلح و امنیت در منطقه صورت می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70448" target="_blank">📅 10:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70445">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8129d80281.mp4?token=Ke5L30Z1Kdz-u5T0-srB7zsLOC9yq3WUHZXyUEfSi7RaaOTrqxQLnk3oN0G5FuQAcM856Oc4GVWskmVx-0hJ2dUciw3_N1FWNk0wACbR4iOXwJlWAz3nePr_mz4zf4fZj3oqrCX14IjnS5E0LXzXgyFb0pDf4uEof1ueMONKS5vqDUU4xh2B1cHd_br19IoyPUDNfMwybeLA3dgD2NEhqmoWwSJUAe2Rky8nIQqQmTs7AyuL3kKRQIObo1CdNphet4-FAZX-xFfW6yk_9y-gFSYr6wjzO9H294_ayACTC6lU3F7I1alEsPdUs3YvFE9_pV3ZwAObPmu17Kd7bumWcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8129d80281.mp4?token=Ke5L30Z1Kdz-u5T0-srB7zsLOC9yq3WUHZXyUEfSi7RaaOTrqxQLnk3oN0G5FuQAcM856Oc4GVWskmVx-0hJ2dUciw3_N1FWNk0wACbR4iOXwJlWAz3nePr_mz4zf4fZj3oqrCX14IjnS5E0LXzXgyFb0pDf4uEof1ueMONKS5vqDUU4xh2B1cHd_br19IoyPUDNfMwybeLA3dgD2NEhqmoWwSJUAe2Rky8nIQqQmTs7AyuL3kKRQIObo1CdNphet4-FAZX-xFfW6yk_9y-gFSYr6wjzO9H294_ayACTC6lU3F7I1alEsPdUs3YvFE9_pV3ZwAObPmu17Kd7bumWcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
درحالی که تمام شعبه‌های ساعدی‌نیا پلمپ شدن، کافه قنادی "بابک زنجانی" تو شهرک غرب تهران دیروز افتتاح شد و قراره پاتوق جدید بچه پولدارهای تهران باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70445" target="_blank">📅 10:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70444">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc8a06759a.mp4?token=culBKM1J382X3lV1WsN2lbeOYiGlTBnrfJ7pFZwVG6Joby9BtaQgRyOpQwecbsIFDIBppv7AjPtZ4JYnK0eILVTXpJMseP8QngOaP6fLbFFwlpdmH6inEecNo87faVsH6_2hHX1ijmjg9QPMq9TlMRrouIvNK2_p-IITWVvbLBJ0eKs6VLeIcqzNpbnFR89-lyPnJ-O4ZGSzu3L5jnzQCJ4pjcPId4Qc3Jluk-WLrVXGgBY0umt04YePUvRd4KuHuZ_cpNbkUCYrCBWf_15GconeFWO5kGxHvzPOqU7ucrKRv4HmAkEPZyDKsEWbgzF0EZMbvzSH2Qw14A4HdAityg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc8a06759a.mp4?token=culBKM1J382X3lV1WsN2lbeOYiGlTBnrfJ7pFZwVG6Joby9BtaQgRyOpQwecbsIFDIBppv7AjPtZ4JYnK0eILVTXpJMseP8QngOaP6fLbFFwlpdmH6inEecNo87faVsH6_2hHX1ijmjg9QPMq9TlMRrouIvNK2_p-IITWVvbLBJ0eKs6VLeIcqzNpbnFR89-lyPnJ-O4ZGSzu3L5jnzQCJ4pjcPId4Qc3Jluk-WLrVXGgBY0umt04YePUvRd4KuHuZ_cpNbkUCYrCBWf_15GconeFWO5kGxHvzPOqU7ucrKRv4HmAkEPZyDKsEWbgzF0EZMbvzSH2Qw14A4HdAityg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یادی کنیم از سخنرانی طوفانی «معمر قذافی» ؛ میشه گفت این سخنرانی یکی از دلایل آغاز پروژه سرنگونی قذافی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70444" target="_blank">📅 10:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70443">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyIwXT9NvK_z7j6-BQpfPvHEL8x225BUgyrIke_diN7mhwmwGOuByZ8AJRGome_WBQqtEennNsJrTGEtYFge0d9le3mxE9MO8UrBGrkBgE6AHHqG9HaNDxmo9jI2xwjoDNl7_6q7rUIBYgNH_xl33vhFXYtH1EExoqM3ewvBQ_Kt41USbX8xNgavaCbad3LVGle1ZTg_5t94hByxbsajSUF4R8BaL2XzzOEBLVk1hgu9HAZteLGStaZTbC9aYgjXpw4lvdcWUMx1fHkI3_HGfs8XSX91ESNX2EO3EX0O3T4tYOSiuuEFnXiGCV63WIGZLewaQc3MVO4bPNerP-Me3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت کنکوری که گذشت:
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70443" target="_blank">📅 09:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70442">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78b2128551.mp4?token=KOTXWOPMoJCwNBocAw7nb6CDtoq20SV8chod8AwkR-_m2603wHMDxXFrDA9LublXdZDlkjRxMUw8ZlgsSukTBZhxm164H4Q5PLF65-GoxlYX35_KT71a6fKmcwdUi4YXYyEfkamxjYGAXfu_Z9Na-j6nfg3A8EK9lOd40JibEL7Rin5iRZl-nLyh7sqvKKNwLR5enE21Pf_BIj8x3YwEVd14TllkPlx4VDmJ8iIEgb2eA7p4AuQKDlMwtOoB5ECzblk5W8brACUEfcVbSwiT9cjUG_A8lUVdwBOZt-DomAjqNO2IMU9-t6jPyhA7MlnUxnC90B-AgzvgEZqpYIqJ7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78b2128551.mp4?token=KOTXWOPMoJCwNBocAw7nb6CDtoq20SV8chod8AwkR-_m2603wHMDxXFrDA9LublXdZDlkjRxMUw8ZlgsSukTBZhxm164H4Q5PLF65-GoxlYX35_KT71a6fKmcwdUi4YXYyEfkamxjYGAXfu_Z9Na-j6nfg3A8EK9lOd40JibEL7Rin5iRZl-nLyh7sqvKKNwLR5enE21Pf_BIj8x3YwEVd14TllkPlx4VDmJ8iIEgb2eA7p4AuQKDlMwtOoB5ECzblk5W8brACUEfcVbSwiT9cjUG_A8lUVdwBOZt-DomAjqNO2IMU9-t6jPyhA7MlnUxnC90B-AgzvgEZqpYIqJ7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
📰
مراد ویسی، تحلیل‌گر ارشد ایران‌اینترنشنال:
🔴
جمهوری اسلامی با سه‌راهی مرگباری روبه‌روست:
تسلیم شروط آمریکا شود
وارد جنگ شود
بدون توافق و جنگ، با فروپاشی شتابان اقتصادی مواجه شود.
🔴
این وضعیت اختلافات در راس نظام را تشدید کرده؛
احمد وحیدی، محسن رضایی و حسین طائب خواهان ادامه تقابل‌اند...
پزشکیان و قالیباف با اشاره به محاصره بنادر، قطع صادرات نفت و کمبود بنزین، توافق با آمریکا را ضروری می‌دانند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70442" target="_blank">📅 09:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70441">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">💎
میدونستین تو دربی بت
✅
با شارژ بالاتر از ۱۰۰ دلار ۱۲۰٪ بیشتر حسابتون شارژ میشه
✅
🎁
برای مبالغ بالاتر از ده هزار دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ بالاتر از هزار دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70441" target="_blank">📅 01:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70440">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70440" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر D
erby Bet
✅
✅
✅
✅
واریز و برداشت ارزی و ریالی
‼️
✅
بونوس 120% اولین واریز
‼️
✅
بونوس برای 4 واریز اول
‼️
🎁
بونوس ورزشی هر شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🎁
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
a31
✔
@DerbyBetOfficial</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70440" target="_blank">📅 01:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70439">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oqwa1bBTa-Gj5ov3d1SaTNHdYfrMB43xuxwl_gtEcOsklWHoqfTRdv9NPUGaCrwcxQWlgt6qXGjARc9-1OMJl-185j6cKib8Oz9XNMpSA2qsb5QwiXpg0QVibKdMqyt9aS_UdqfiC9o9xeWtOuhn0cKdK0fsE1PTmuIlBcs1hFerdZ8PIfM6ovwHaGIYuuIqBbStUOCZIvwhZvEIIhq4Ki9m_97RqkoG_GZwPUxqV2f55u335so1izWjjWbQ1BCqYos_-t-92N5bZNUbudj-EaeyuW1mNXt-0ebyPMG8IMosltvIIkxuvJr9ks1hts4EfQctQ8_vWRrRpEtP4C3Gag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ با انتشار این پست ادعای مارک تیسن مبنی بر اینکه بیش از ۱۰۰۰ کشتی با اسکورت از تنگه هرمز عبور داده شدند را تقویت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70439" target="_blank">📅 01:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70438">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXLr6XGxLyUWBjY76eP7DvfUcnClCh48vCC1M4_X2aeLU5FzS_Eugv2v2eSjRW7ZkuIzdjr72O7oGKGAAV4JrKmPnTeMB75X-XoB6XFHNyAXgBeM91m0I_WoQFTo4Jl3YSKpwMV944E8N6NCXnLKnK3ElIySaSaW_rIvuyDkOcIEbAdX8nRvvA-8rvipo-AhBDs6RJBY4ihN71hb4-iauIq574Ol6g4dRp5-GhSDrDZ_KJ5orJ_TmZRo-T4TN_yosJopV_qo60du8aoxwBjbna4kCjNI0HE2qiHvkRIu-RD0RKjKCjJCCvoFya_l1ZGlPkgrj_pxuTiablzoUsZskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
املاکی مجدد این تصویرو با عنوان تنگه هرمز قلمرو جدید ایالات متحده منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70438" target="_blank">📅 00:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70437">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39665a7cce.mp4?token=txJvm0kcFz-V_7sjfYYCCs0hxi4WU5QPUICu2JIcAoHLo4skAqevZThmZVlOKFA1JIkGa46z3dUFTuFJDQkAFfLwis0HYjH_x0G-UFsmHSX9-b3abUa0vP89BvWTv40Zoz4gpxRs4VPC_9pOud0Z8dcW-8W33KJbDPMKaTL6zi6-0FSO1j82fueilmsW8NOPebeDjlNXu9ypSyQ1c61Rb8wH_xYIixGDGNsTrrTKxpQeACHKcssF4qFWJgJAF2jcJ-W213fInOkGpx6Tv_p5oVU3q4KuOCRqOXX86c-kH96FSplxKwWcBNEpieZXmOy6SN6oUiBYJjhIsJBq0uKw4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39665a7cce.mp4?token=txJvm0kcFz-V_7sjfYYCCs0hxi4WU5QPUICu2JIcAoHLo4skAqevZThmZVlOKFA1JIkGa46z3dUFTuFJDQkAFfLwis0HYjH_x0G-UFsmHSX9-b3abUa0vP89BvWTv40Zoz4gpxRs4VPC_9pOud0Z8dcW-8W33KJbDPMKaTL6zi6-0FSO1j82fueilmsW8NOPebeDjlNXu9ypSyQ1c61Rb8wH_xYIixGDGNsTrrTKxpQeACHKcssF4qFWJgJAF2jcJ-W213fInOkGpx6Tv_p5oVU3q4KuOCRqOXX86c-kH96FSplxKwWcBNEpieZXmOy6SN6oUiBYJjhIsJBq0uKw4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی:
توصیه‌ام به مردم اینه که کم کم از تو همون خونه و محلات، شروع به تولید چیزهایی کنن که نیاز دارن
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70437" target="_blank">📅 00:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70436">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/927919a024.mp4?token=GTof_aTejlVQg9ph2VuFpaeQz7bW7LGguKez3EDktGzvD3WQkSmzvE_3kJge7N-IP6MszRCOJXzYr2XPP-7pSBgS3b2qgoik7mBjw6i2aUmIIumlJLe0Xim9KqzF5n36QGnXCjREqUee2oQHGRWKhWgzP6w72jL_LFG_TTJ50VqfUEBsnvkAjKJaiiJ8wpKAhDC8GOmeQUdG82sEWVrQUkMLibzVz7vQcjIQRFUgeIYjW3YRm-B1cpDlWJwXAGlaU__DSKK9qZhiF69Hfaln3rbO0ktyt8Vs8Vl6EZkjXwrmF4bN1XmCJAg71hxlbD6kxsO6dc6WItOHxTNtwPxV5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/927919a024.mp4?token=GTof_aTejlVQg9ph2VuFpaeQz7bW7LGguKez3EDktGzvD3WQkSmzvE_3kJge7N-IP6MszRCOJXzYr2XPP-7pSBgS3b2qgoik7mBjw6i2aUmIIumlJLe0Xim9KqzF5n36QGnXCjREqUee2oQHGRWKhWgzP6w72jL_LFG_TTJ50VqfUEBsnvkAjKJaiiJ8wpKAhDC8GOmeQUdG82sEWVrQUkMLibzVz7vQcjIQRFUgeIYjW3YRm-B1cpDlWJwXAGlaU__DSKK9qZhiF69Hfaln3rbO0ktyt8Vs8Vl6EZkjXwrmF4bN1XmCJAg71hxlbD6kxsO6dc6WItOHxTNtwPxV5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
محسن رضایی، دبیر شورای عالی امنیت ملی:
🇺🇸
🇮🇱
نتانیاهو به ترامپ گفته ایران رو 6 ماه محاصره کن، تسلیم میشن!
ترامپ بهش گفته اشتباه میکنیا، نتانیاهو هم گفته آقا تو 2-3 ماه تست کن، می‌گیره.
آمریکا به طور کامل از حمله نظامی ناامید شده و محاصره اقتصادی راه انداخته.
هدفشون هم اینه که یه عده معترض رو بریزن وسط خیابون تا اونا به F35های آمریکا کمک کنن.
محاصره و تحریم‌ اقتصادی آمریکا ادامه پیدا کنه، شرکت‌های آمریکایی منطقه رو می‌زنیم!
تا الان هیچ کاری با شرکت‌های آمریکایی نداشتیم و فقط پایگاه زدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70436" target="_blank">📅 23:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70435">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35614b49f.mp4?token=t4OY7fIrY67LcWXoKkNEpZvl34paLTqj-IcHKdEiGeSgaTgPJ0-UeaIwYly4Y7SR2sjOfYFOLvRcw4f49Oq4GoUZLfXMJtoii2yKhF7eV1M6x1hyJMZM2PnQh1bAcIAGecqqbul5GHWHi0fGj-PE0NiqEIChZqbDQ40uN9JeKJhSHh-sWdev4ZVWxzfbyzbrWZQKAXj62JByRNlkE3X6AKZbwNhiEVrhUHL0DRGGkZUQrZUxKqL3s5q-cNrQTkkFDWB4OiD4cGNKst-t2Gqbin9UjGTgo9uYE6ao2KnM7IwWXZl2iUvJ2jgO_o3rd7-0X3pa8EDPPV2gWcR_VAJ3Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35614b49f.mp4?token=t4OY7fIrY67LcWXoKkNEpZvl34paLTqj-IcHKdEiGeSgaTgPJ0-UeaIwYly4Y7SR2sjOfYFOLvRcw4f49Oq4GoUZLfXMJtoii2yKhF7eV1M6x1hyJMZM2PnQh1bAcIAGecqqbul5GHWHi0fGj-PE0NiqEIChZqbDQ40uN9JeKJhSHh-sWdev4ZVWxzfbyzbrWZQKAXj62JByRNlkE3X6AKZbwNhiEVrhUHL0DRGGkZUQrZUxKqL3s5q-cNrQTkkFDWB4OiD4cGNKst-t2Gqbin9UjGTgo9uYE6ao2KnM7IwWXZl2iUvJ2jgO_o3rd7-0X3pa8EDPPV2gWcR_VAJ3Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
فیلد مارشال محسن رضایی:
در رفتار دیپلماسی ایران قطعا اصلاحاتی انجام میشه و تکامل ها پشت سر هم صورت میگیره
تصور جهانیان از آمریکا به کشوری خوار و ذلیل تغییر کرده و ایران قدرتمند تر شده
ملت ۵ هزار ساله ایران با دولت ۲۵۰ ساله آمریکا داره رقابت میکنه
تصمیم رهبر انقلاب برای آمدن فرماندهان جدید نشونه جنگ متفاوت و غیرقابل پیش بینی از سوی ما هس
حتما شیوه جنگ رو تغییر خواهیم داد
دشمن روی تفرقه و اختلاف حساب باز کرده ولی وحدت ما کمتر از لانچر ها نیست
حماقت ترامپ باعث شده کل جهان خواستار دستیابی به سلاح هسته‌ای بشه
در جنگ جدید اقتصادی نیز به حساب اونا خواهیم رسید
ترامپ خالی بند است چندماهی هست اصلا حرفاشو گوش نمیدیم
وحدت بدون اطاعت از رهبر انقلاب ممکن نیست
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70435" target="_blank">📅 23:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70432">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XxmI4VlFHjywmyhN0PlY-6Fb7F6jOJ7BAJp8WUQwGxNrCgWuMivJs9X7xNW3khhJUscvZDLCwVQssT7HufDKmY2ggyAewny9js7Si9yJQop3pvx81NF05bkdlofWZh63Tbvzod4eJ1PO2q6iMFWbA4IMcHPqXJIB3Kaoa7xvVsfaS_IRcJWcfgxpFDmTT-U7VnUTSKKZG13xHOPOQl_Ax5fiRMY2IXrdZdDE3sZ3-NY2pOrv1Bv0cJDzcg1dH1Ng9IF3W4K4e10acr_zd34uCuGJHkOnpR-TcDO8fZ51NFik-m3z-YMDJvlDDxsUFYQpXZVZBYYIJvk6GrJxSUw_dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vKwmWm-nrtTwxe2kdZ2n4MIjgtKdHneRVST78eSLjkN3KIANgf2A2zQmEuKPlLN6c182acMzbUsg1jcSaobZY8Z09SQnWjr5teE3xZIzG39ksaoXU2EeOchbWUG-a9Q9UOZ96NQPxPwrCjBiVYdSjyO2uOhDy2US3qelbg7dCDX8u5iPm7EjINBupj_LCs8BEROMQNhHkWavEmoREscSxeLCUmOrWJSY0bCWaZY26xpwf6qMNp5uQnYWUxCCo6Ea1Eb0GLHw6KwwsI1sriUW_x01uiGgcE2HllYCkY07KRVssGdOB9N9oFwN6sk4scaNfppWGFIg0GM2rJ_M3VZovA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tzw65YaptjEyUlFYT8v2JhAhgGqsss6-jYr25TheYWWv5DBF9g_U9k76XglLWFIQyoL2L1xAmqiVKfr9lTy4AqT2zfztlfnjQkONaQxrlXEvr3mPpoPtqmAaxaWT1EwAmyAYC5H_5qwHHlBSz8OvNfOlV53vHuqURRQvbK9vXiBlKFJ_KPx0VAFQB0bjJo2e5bE9bjuGQ2iu2vv5wDBWuAGnl3EoB_zpbADSR4wbqSejKMcjbvWwAd86MHLjwRerc3Z73bhOhIolUiOR7gg6xB8pX_QDJEnfarAGQ2M9zN9GBIiSKXENhTUb2muOEwGxLY_cR1Okh2EzZu-w9XQkMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
جفت کنین؛ یه دختر به اسم نگین، سه بار به دوس پسرش خیانت کرده و پسره بخشیدتش.
اما بخاطر اینکه پسره با خاله و دختر خاله‌اش رفته بیرون تهدیدش کرده رو صورتت اسید می‌ریزم!
چند ساعت بعد دختره پیام داده که حتی اگه صورتت با اسید نابود بشه، بازم مال منی!
من پنج بار تریسام زدم اما تو وظیفته منو دوست داشته باشی!
فرداش رفیق دختره پیام داده که نگین مسته و با یه پسر به اسم امیر سکس کرده، اما خدا شاهده قلبش پیش توعه!
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70432" target="_blank">📅 23:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70431">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‼️
گروهی موسیقی در جنوب ایران همراه با جمعیت، آهنگی سنتی به سبک بندری می‌خوانند و با افتخار نام رضا شاه را فریاد می‌زنند
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70431" target="_blank">📅 22:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70430">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhGrBrCcR4kJVEOpzr3p3wSsxC-A_MREAiXOohz9-KDA9fw5fLR7gDPuG1j7f5fBY2TVHbmwRk9T30kCMG81oxFwkqDodKml-Og0WUQyY2dYIAO9ZxGPlGkriAQ5MrEoTwurBEIBZEfAgh5eAS2zs2SujTmeTuacWd3zrRj27DeHVcCSivAlF0E47BU84H0gRsqm_do3mZwDPWvXeWFSVbcuE3Y6gF9Td6n8RUCE2YE6nTIn1FrPLqFrcv-Dkh1eT30oZWTFGBaVqMLdK8OsgpDShmEmPcAQKmepOY_yf4w43P_Z2WFsn7tdAT8bI7Wz4oHZfhp-PCEJGg9f975c_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان اینترنت یکی از استان‌های یمن رو قطع کرده
حالا خبرگزاری تسنیم اومده نوشته اقدام ضد انسانی :))))
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70430" target="_blank">📅 22:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70429">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23b6fb2242.mp4?token=W9sHZ8ymb-YUih3Pe2bkYXQHGQuUv9AUdeI8F3Z77C54rOpMFIqmzB7EHw8u6zf-gJeGnE6MCCozqPbAZxa4TfKj6EzP_in00MR6jSomhRpHXXZH4ogfGu4MH2pY5ayGD7YrwTEK9pALxN4PApmaPp3qy8BfXzDV7cz0MjLovCwPaCSwHI-C3ni3F6VqARbm9tjDa6Mnyf6dTV-q_xebV-6yFqW1UMQwHwaQAL8TgdOHX6HmIJc-7IXZhOovXxiu68rECCeF5bAcem4xFIWWGo_Ktft3sA-GvonLyBScVFGMF-ugs1IqPsnVg8Yb4wWVNhMdIy1gpFxXKeGlChiktQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23b6fb2242.mp4?token=W9sHZ8ymb-YUih3Pe2bkYXQHGQuUv9AUdeI8F3Z77C54rOpMFIqmzB7EHw8u6zf-gJeGnE6MCCozqPbAZxa4TfKj6EzP_in00MR6jSomhRpHXXZH4ogfGu4MH2pY5ayGD7YrwTEK9pALxN4PApmaPp3qy8BfXzDV7cz0MjLovCwPaCSwHI-C3ni3F6VqARbm9tjDa6Mnyf6dTV-q_xebV-6yFqW1UMQwHwaQAL8TgdOHX6HmIJc-7IXZhOovXxiu68rECCeF5bAcem4xFIWWGo_Ktft3sA-GvonLyBScVFGMF-ugs1IqPsnVg8Yb4wWVNhMdIy1gpFxXKeGlChiktQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه عده از مخالفای بی‌حجابی تو محمودآبادِ مازندران رفتن فرمانداری و علیه آدمای بی‌حجاب شکایت کردن؛
حالا فرمانده نیروی انتظامی محمودآباد هم با این سیس و خنده‌های ریز اومده بهشون قول داده که با بی‌حجابی تو محمودآباد برخورد می‌کنن تا یکم آرومشون کنه:
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70429" target="_blank">📅 21:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70428">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48faea4858.mp4?token=nhQWsX5DRYPYTm4jr7uxnVWu2itiM7L-Y4989af6ZL02LJlfLHRpKpI5sI6Wy0wwkHRdQlE_3s_J4HnkV-PvKatBByckg-Ujs_Icz6KryLiYrRgyGQrVacSr53zSvN6sEjyTY5nKZeyu-Q_ehEz8WEs1R_MWnr5nGGAJNRmt-GxkCPo-lQzry1B9n9XRcWldzPnebq_cnnKT22dxFGU3VeQjUdRlyHCarkgOLvna603As5bSFXuKl26iYy6C5Eef-ZNoLf_m6ftnOq7P2lrqtTJ8dBsqEbW3N7qmdyLzoIFoXhma6b9UV_PTqLU8prmlstITJV4wJ2_dlBYEUrKs7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48faea4858.mp4?token=nhQWsX5DRYPYTm4jr7uxnVWu2itiM7L-Y4989af6ZL02LJlfLHRpKpI5sI6Wy0wwkHRdQlE_3s_J4HnkV-PvKatBByckg-Ujs_Icz6KryLiYrRgyGQrVacSr53zSvN6sEjyTY5nKZeyu-Q_ehEz8WEs1R_MWnr5nGGAJNRmt-GxkCPo-lQzry1B9n9XRcWldzPnebq_cnnKT22dxFGU3VeQjUdRlyHCarkgOLvna603As5bSFXuKl26iYy6C5Eef-ZNoLf_m6ftnOq7P2lrqtTJ8dBsqEbW3N7qmdyLzoIFoXhma6b9UV_PTqLU8prmlstITJV4wJ2_dlBYEUrKs7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاید ماساژ هپی اندینگ به گوشتون خورده باشه، حالا چی هست؟
بعد از اینکه ماساژ صورت گرفت، آخر کار نواحی جنسی مشتری رو لمس میکنن و ماساژ میدن، تا ارضا بشه.
حالا با یکی از خانمایی که ماساژ هپی اندینگ انجام میده مصاحبه کردن!
میگه هفته‌ای ۵ نفرو ماساژ میدم و از هر نفر ۵ میلیون میگیرم!
یعنی با روزی ۱ ساعت کار در هفته به غیر از پنجشنبه و جمعه، ایشون ماهی ۱۰۰ میلیون درآمد داره!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70428" target="_blank">📅 20:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70427">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
اخوندی که بی دلیل و بی اجازه از یک زن ایرانی عکس گرفت!
زن ایرانی شجاع بهش حمله کرد و چند تا مرد دیگه هم رفتن بزننش.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70427" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70426">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کانالی که همیشه در مسیر ورشکست کردن سایت های شرطبندی حرکت کرده!
😈
آمار ثابت 90 درصد برد
✅
فقط کافیه چند روز فرم هاش رو دنبال کنید...
⚽
@Tipster_Mafiaa
@Tipster_Mafiaa
⚽
@Tipster_Mafiaa
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70426" target="_blank">📅 20:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70425">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lArgQWBjul_hP8RKg6DsbGfH5PvrhWqwFwyEqsKza8lGb29jLLske1UdSVvdfrnbNJX73PAb1XItJPlKi-V6nsJMjwlHh0UDJPWceyjVUMh6M9FhmqUXcVFpRNRCswSFea4vuOO_vsCuCL68LcoiAtMfpoPYDnq6GYuhU9cPwITXaznSKm_J0vwFAXbKSBUtgPCs6UU3iv9PFK8D9hXPmwRhnvaFkvHthJglexP3XiTISd3ueiGoEdlBcrhcAsAf3nFOoB_NOMfGKaYDIAk7lu9XLiNDi5MC_XkzyNPHLJuyT4WmdnbGiyux7KSYnHWP5DGcv5qFd1VPokMXALcElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@Tipster_Mafiaa</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70425" target="_blank">📅 20:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70424">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89c9ecf73f.mp4?token=TqG4u76wXgLyE7m1xCyLL4woT2_BlHMAOKF62n4w_omT5AGFK1KKkQYPhmDEUcCjt0dKIEEq65a8aBfA4y4E3x9osKZCYfA0h6ajczVxbLGqvsnGzbL538KVWibH4MyJODqeDZm-3Xcf3T-Tptjy7RCFscFUZu1zm1uedm5LlW3wZCzmbr9fZmBPOli22f2e3lJU7ug1ZbSqc_NMEDOeYvsmpN1ObSdWrQ8idrDqEHF8udsiMyYa7NJedyBr0p7rVn4H7pAh2iwkhpWiU6aSW1MxekWPJN7hRdyxG2jOL6JYuPxsYiDbAa5gv2Jb6wsr-r-zdz7_AbcqGl_xraknpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89c9ecf73f.mp4?token=TqG4u76wXgLyE7m1xCyLL4woT2_BlHMAOKF62n4w_omT5AGFK1KKkQYPhmDEUcCjt0dKIEEq65a8aBfA4y4E3x9osKZCYfA0h6ajczVxbLGqvsnGzbL538KVWibH4MyJODqeDZm-3Xcf3T-Tptjy7RCFscFUZu1zm1uedm5LlW3wZCzmbr9fZmBPOli22f2e3lJU7ug1ZbSqc_NMEDOeYvsmpN1ObSdWrQ8idrDqEHF8udsiMyYa7NJedyBr0p7rVn4H7pAh2iwkhpWiU6aSW1MxekWPJN7hRdyxG2jOL6JYuPxsYiDbAa5gv2Jb6wsr-r-zdz7_AbcqGl_xraknpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
۴ سال پیش گفتید تحصیل تا کلاس ۸  مجانی میشه، به کجا رسید؟
❤️
محمدرضاشاه:
اون که مجانی شد هیچ، دبیرستان و دانشگاه هم مجانی کردیم
🎙
خبرنگار:
گفته بودید سال آینده درآمد سرانه به ۱۸۰۰ دلار میرسه..
❤️
محمدرضاشاه:
۲ ماه پیش رسید به ۲۲۰۰ دلار
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70424" target="_blank">📅 19:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70423">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeeNiALHkjLhHkkXZuPpqGVGjUX7s4i4OMIfH0czXDjUrc4tR7jLfNZg-0ZXEItQPtlmG0Tttw02WbJyKFFAb9Fc0P_jewJQN8Hr_TkEAFZiSS5yyP-rxGptc-kFOK22S-e4cvQInza1TbcIGB5VMoLZAVO29g6xiRTZWV4QzRjFdXFco-9AQpiBwJ-axx6yec7PsWk7G7cdvJR3D7HqvEw_HL7y8NFfsRYi5k0MtCNyizD0zeE3gWGNjutbyDSSWW29aWmJ3gFOr-O1HYW2806Rfq4bQE3cpQEpSOPCwewKplXxT9iqbAs53z0pnv8t4ysszCOyChEaF9qHxWKy5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
📰
اکسیوس به نقل از سه مقام آمریکایی:
شامگاه جمعه حدود ۴۰ نفتکش در هر دو جهت از طریق کانال آب‌عمیق جنوبی از تنگه هرمز عبور کردند.
در طول شب، حدود ۱۶ میلیون بشکه نفت از طریق این مسیر جنوبی از تنگه خارج شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70423" target="_blank">📅 19:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70422">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193d1b1501.mp4?token=XlWDaOOMkjiJMQvjwtkKNWLb_duDoUVJ8lmuu5Pb7_sP96fMJr898uq8f0AmV_DQkAL7bfGcyPijmDXe4nvArCqt-F2v-FEi8WD4RdXVu7W38j81z_yMpdgXzVc6whQOdZ7TtnRfP3nGXehbNuNpJWWImaF4z-IZfxh836a_LRkGyRCE-7SqBaI5fnflK4yajJ-ZCA-9DaGIVsGU2w0SCK9M87vmetkVm3l6G4wltevMquYnNBTuY1jELvv2e9-_6ReGOV7kSq8JyBboSjoQIsRHzHlhQ7Hvuad48Hz_IXNL_N3zYNK1MZ9NBVI0Y6sC830PT-0xMqTnMkQPvFFfrjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193d1b1501.mp4?token=XlWDaOOMkjiJMQvjwtkKNWLb_duDoUVJ8lmuu5Pb7_sP96fMJr898uq8f0AmV_DQkAL7bfGcyPijmDXe4nvArCqt-F2v-FEi8WD4RdXVu7W38j81z_yMpdgXzVc6whQOdZ7TtnRfP3nGXehbNuNpJWWImaF4z-IZfxh836a_LRkGyRCE-7SqBaI5fnflK4yajJ-ZCA-9DaGIVsGU2w0SCK9M87vmetkVm3l6G4wltevMquYnNBTuY1jELvv2e9-_6ReGOV7kSq8JyBboSjoQIsRHzHlhQ7Hvuad48Hz_IXNL_N3zYNK1MZ9NBVI0Y6sC830PT-0xMqTnMkQPvFFfrjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
علی عبداللهی، از یک کارخانه تولید موشک‌های بالستیک زیرزمینی بازدید کرد تا از آخرین پیشرفت‌های مربوط به تسلیحات بومی مطلع شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70422" target="_blank">📅 18:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70421">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e0051dae.mp4?token=KFpy9Z5RWUTfg3Kc7edXW1lq4itH1KX_YBkn1K43czBpIlO2s5cyn7EPGO4-N5wvoRyfWEvdbfNDU6JENMjtmPVyrtx_fJPDdgn0l5jGp4_nhVBVH1wj1i-5fGPJd55AO4JkYdSQ0wIm3nejv8Thm4XuihSC8JJjQqUzK70-qC5ohAFFKOXg84u7-XbT9b-efF-TyOhgoEilYHXZ_yNCg4aZopIX899RRSf8CDT_IVLoVFNjwNhrsjarXjKFLVDzbjxjT_-BKFbWknkHuFAzSckuOiC0xiuwH4KzP8b65QKm8ONSYCkeCmFXMD9Y1Fu64esJxIW8FWO3jeumNQn_lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e0051dae.mp4?token=KFpy9Z5RWUTfg3Kc7edXW1lq4itH1KX_YBkn1K43czBpIlO2s5cyn7EPGO4-N5wvoRyfWEvdbfNDU6JENMjtmPVyrtx_fJPDdgn0l5jGp4_nhVBVH1wj1i-5fGPJd55AO4JkYdSQ0wIm3nejv8Thm4XuihSC8JJjQqUzK70-qC5ohAFFKOXg84u7-XbT9b-efF-TyOhgoEilYHXZ_yNCg4aZopIX899RRSf8CDT_IVLoVFNjwNhrsjarXjKFLVDzbjxjT_-BKFbWknkHuFAzSckuOiC0xiuwH4KzP8b65QKm8ONSYCkeCmFXMD9Y1Fu64esJxIW8FWO3jeumNQn_lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
📰
فاکس‌نیوز:در حالی که دولت ترامپ آماده می‌شود تا موج جدیدی از فشارهای اقتصادی را بر تهران اعمال کند، او می‌گوید که ایران در حال تغییر موضع و نرم شدن است.
ترامپ می‌گوید: «آن‌ها اکنون دارند کوتاه می‌آیند، چرا که وقتی کشوری دیگر نیروی دریایی و نیروی هوایی ندارد، حرف زیادی برای گفتن باقی نمی‌ماند.» او می‌افزاید که بسیاری از رهبران ایران کنار رفته‌اند و «اصلاً نمی‌دانم باید با چه کسی سروکار داشته باشم.»
این اظهارات در حالی بیان می‌شود که ایران سیگنال‌های متناقضی ارسال می‌کند: رئیس‌جمهور مسعود پزشکیان می‌گوید شاید زمان آن رسیده باشد که «همین امروز به جنگ پایان دهیم»، در حالی که رئیس مجلس ایران لحنی بسیار سرسختانه‌تر و تقابلی در قبال ایالات متحده در پیش گرفته است.
اکنون فشارها شدت می‌گیرد: انتظار می‌رود اسکات بسنت، وزیر خزانه‌داری، روز دوشنبه تحریم‌های جدیدی را با هدف انزوای بیشتر ایران اعلام کند؛ تحریم‌هایی که روابط ایران با روسیه و چین، چالش عمده‌ای در مسیر آن‌ها محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70421" target="_blank">📅 17:56 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70420">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7d3e5c370.mp4?token=KZYw3Q8CjbInwxSqYVpntJ3nJ0xJtMBzrFSq-T6WGMiY6XLkHbLUJiXvdCf9GdlBAafgfGR21csoERqZwtaeKSvCRD1dBPRyyIw4iqUDJKOwMizXL5uytGHo89YO4hmVzDLp6alqY-0sznA8FOdL0hGJuLIA_TYPpl8I0kDE763e7F1B_vq_vZda7dky68-J-X6yEOSMJHoZ-1uAa-qSF0DEvohsoY_yFmpocZuZZ5HH39KAgeiXpvzGdZ1BZCdk-nAXMf_Id9i837L2kbUzxZ-mWqJrjwkrrLguvcIg4dEq4m5FaxnYdaBp3nXoSwusOrRfwxc5wRQM4Ltnc-Uz94O8kPmtCzxX3G4Rbd7Qa_gVBmXLtFDr0iJQyDoOPTwgp6YJS0qQzjWCPR28rPLUp-w5drootSNItE-05iQVYTtuTZ1zQfoQIfoYUQUKL4HXVwuce9pFWcoDJlpfpVp8Z2Pe5Zj3ypIzGuMHme9zBJOOaumGdgkNwtiE3P5fOTMHo0IO8eBW5SYjBSrFHf4luLrpZlovFpLp2w1w7vvtmHYj2GFD6mnHqTMQzR4_sxIa33o4BGCOoAySnRq3cCvw9RZSygjP92sHTCEoTBaf6rX9G8RiwByN-2nlxzNage26WVGePoitpvEOVvWHOcbiL4DCdsC-p7t13UritHxFA4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7d3e5c370.mp4?token=KZYw3Q8CjbInwxSqYVpntJ3nJ0xJtMBzrFSq-T6WGMiY6XLkHbLUJiXvdCf9GdlBAafgfGR21csoERqZwtaeKSvCRD1dBPRyyIw4iqUDJKOwMizXL5uytGHo89YO4hmVzDLp6alqY-0sznA8FOdL0hGJuLIA_TYPpl8I0kDE763e7F1B_vq_vZda7dky68-J-X6yEOSMJHoZ-1uAa-qSF0DEvohsoY_yFmpocZuZZ5HH39KAgeiXpvzGdZ1BZCdk-nAXMf_Id9i837L2kbUzxZ-mWqJrjwkrrLguvcIg4dEq4m5FaxnYdaBp3nXoSwusOrRfwxc5wRQM4Ltnc-Uz94O8kPmtCzxX3G4Rbd7Qa_gVBmXLtFDr0iJQyDoOPTwgp6YJS0qQzjWCPR28rPLUp-w5drootSNItE-05iQVYTtuTZ1zQfoQIfoYUQUKL4HXVwuce9pFWcoDJlpfpVp8Z2Pe5Zj3ypIzGuMHme9zBJOOaumGdgkNwtiE3P5fOTMHo0IO8eBW5SYjBSrFHf4luLrpZlovFpLp2w1w7vvtmHYj2GFD6mnHqTMQzR4_sxIa33o4BGCOoAySnRq3cCvw9RZSygjP92sHTCEoTBaf6rX9G8RiwByN-2nlxzNage26WVGePoitpvEOVvWHOcbiL4DCdsC-p7t13UritHxFA4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این مرد ۴۱ ساله درحالتی که مشروب خورده بود درحال رانندگی بود که پلیس گرفتش
:
از ماشین پیادش کردن میبینن دکمه های شلوارش بازه و یه دختر بچه روی صندلی شاگرد نشسته
۵ تا دختربچه خیلی کم سن و سال هم روی صندلی عقب نشستن ، پلیس بهش میگه اینا کین ، میگه اینا دوستامن
درضمن یکی از اون بچه ها هم حامله بوده
در نهایت این شخص به دلیل سواستفاده جنسی از کودکان ۳۶ سال حبس میگیره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70420" target="_blank">📅 17:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70419">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/357928b911.mp4?token=h9Li-O0LKe1M2R8Up7S-Fhd99Ab6BP_GykXRvoF1FX9W0ENk4_kXSQ1I5JsXk-kN26s8ivn035nxW2qS_idOKcaPgQY3oy7SQOMn3kHICauqOP3K6Schqz3-hC-HZAXo3-rzfQBDjvljig58ZhTY06NRlC-9UgfniFs28D_FRHZisHx4FxJErzkrSmM1ASyFBaDqoT4jFO6pnLqRXuFVGhJIgJ0gNxFNZtowCJ70jYT7vf8OJ9jHzsYawNeO14xSi1O61-qU7dj9NCKO6iradbVa16qfFYTRy7r0S6lVxJUrwNKE1jc_JPJ946jIrslHnyxiI74HYRtMR-bKgR_buA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/357928b911.mp4?token=h9Li-O0LKe1M2R8Up7S-Fhd99Ab6BP_GykXRvoF1FX9W0ENk4_kXSQ1I5JsXk-kN26s8ivn035nxW2qS_idOKcaPgQY3oy7SQOMn3kHICauqOP3K6Schqz3-hC-HZAXo3-rzfQBDjvljig58ZhTY06NRlC-9UgfniFs28D_FRHZisHx4FxJErzkrSmM1ASyFBaDqoT4jFO6pnLqRXuFVGhJIgJ0gNxFNZtowCJ70jYT7vf8OJ9jHzsYawNeO14xSi1O61-qU7dj9NCKO6iradbVa16qfFYTRy7r0S6lVxJUrwNKE1jc_JPJ946jIrslHnyxiI74HYRtMR-bKgR_buA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دخترا :
خیلی برای کنکور استرس دارم کل بدنم داره میلرزه .
پسرا به روایت تصویر :
خیلی استرس داشتم که چجوری کیکم رو بخورم که تا آخر امتحان کیکه تموم نشه ، که نفر جلوییم بهم کیکشو داد و کل استرسم رفع شد ، دمش گرم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70419" target="_blank">📅 17:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70418">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c46390cc4.mp4?token=On4tNTVp_ve4KSXGU1RxvwP1RmycyNhQI9fo13wjJtUN6H8JU8uDMuGMYWoMugys6RKxZdQQy-sEVg-_eDnSOb5VCgdTktOutK2Pd3Q37J5yl__DPmFtsKfqxOXEuh7EiCRfPxu925XYG1sU8LEdigYVIudXx_6rySQedopkQji8cFUgz2cBKb9vaWtB4mClVmFP5JT1UvrSGaf2uBAYI0FykEGWU_eYGZBZxuOfjDkUS9KqW94HdKOHRLfx_DS8WD-ZXjSaEFPl-8ssRE3J5x7ML3-yZjRkS6zGNncAdq4wVtrYNm82eUHA8fQRAK0-cqqLhf9anFU3Ow8E3P5CzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c46390cc4.mp4?token=On4tNTVp_ve4KSXGU1RxvwP1RmycyNhQI9fo13wjJtUN6H8JU8uDMuGMYWoMugys6RKxZdQQy-sEVg-_eDnSOb5VCgdTktOutK2Pd3Q37J5yl__DPmFtsKfqxOXEuh7EiCRfPxu925XYG1sU8LEdigYVIudXx_6rySQedopkQji8cFUgz2cBKb9vaWtB4mClVmFP5JT1UvrSGaf2uBAYI0FykEGWU_eYGZBZxuOfjDkUS9KqW94HdKOHRLfx_DS8WD-ZXjSaEFPl-8ssRE3J5x7ML3-yZjRkS6zGNncAdq4wVtrYNm82eUHA8fQRAK0-cqqLhf9anFU3Ow8E3P5CzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
قالیباف خطاب به رسایی:
حضورت اینجا خلاف پروتکل هاست
ولی بخاطر عمامه ات ایرادی نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70418" target="_blank">📅 16:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70417">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e1045a89.mp4?token=VZZXCUHZgYoi6AbzF0320FtOQVix8bgbuaHvIG1THKIQSgzM4pCpRhdlOhjIRxCOvwOMIuXQqsZ5zXW3s8iW3afoW749DVUoNRdDbyGGY6QA2nfESBY6efFqJKlZvTxqdet7sZbsrZm_soQz2Cn3SZuXU5MviagoT3v5qtvkkGkeMs_xPgvhJFjVvSitYvV5lUirJLQULB1S0FDpBGKdV2xYPvB3boXGwyTaJmzEp2AK6_me-cTT7Y1FptfgzDlGHpohTWCn58fY8Uqkg0UP0JbFiEdaoUntZqH6gopCDwj5CLTlB9Xz7giiFQbLjHTDy3AKXaG8ZMdEE6s2mzUrCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e1045a89.mp4?token=VZZXCUHZgYoi6AbzF0320FtOQVix8bgbuaHvIG1THKIQSgzM4pCpRhdlOhjIRxCOvwOMIuXQqsZ5zXW3s8iW3afoW749DVUoNRdDbyGGY6QA2nfESBY6efFqJKlZvTxqdet7sZbsrZm_soQz2Cn3SZuXU5MviagoT3v5qtvkkGkeMs_xPgvhJFjVvSitYvV5lUirJLQULB1S0FDpBGKdV2xYPvB3boXGwyTaJmzEp2AK6_me-cTT7Y1FptfgzDlGHpohTWCn58fY8Uqkg0UP0JbFiEdaoUntZqH6gopCDwj5CLTlB9Xz7giiFQbLjHTDy3AKXaG8ZMdEE6s2mzUrCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
#تاریخی
؛در این ویدیو، به بررسی نبرد حرّان میان امپراتوری اشکانی ایران و روم به فرماندهی کراسوس می‌پردازد.
کراسوس که برای کسب ثروت و شهرت به ایران حمله کرده بود، با ۴۰ هزار سرباز رومی در برابر ۸ هزار سوارکار و ۱۰۰۰ سواره‌نظام ایرانی قرار گرفت.
ایرانیان با استفاده از تاکتیک تیراندازی از روی اسب به سمت عقب، پشتیبانی بی‌نظیر ۱۰۰۰ شتر حامل تیر برای تامین مهمات و ورود سواره‌نظام که ۱۴۰۰ سال از تکنولوژی نظامی اروپا جلوتر بودند، توانستند ارتش روم را به‌طور کامل در هم بکوبند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70417" target="_blank">📅 16:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70416">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezoBv8WBLM4w42rfQ0evNaJ8tWtyPJolSvaS39uB7Zt0QAuTODn7nebgXxGgAqF3sybFjlJ50Vn2IFoqftpSkagfv8YpBq_3IuSwJ1rW-pOTs1nkyzW7NYUDwx0DS4s9OG1uMs27eYrg2UcrGNrhtBbeFwcQOZDobyjqK2vr2qZJXZg3t5SZI27OJeMrkGha3VImvQ9yVpBd0Nv3T0HPdJbPb8qybX5oBfe8xT-znz442Iy6bII6H-8Ug-81T-wOUAo4dBh9b08g8JBYUl7bltYDGu3kDG_s6nXE0aRvBBDieEPdlL-o8uZVen7QJZzeN3MogxBv-7YaO7_kHZB7Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
یه خانم رفته لیزر و خجالت می‌کشیده که اپراتور زن باشه، گفته یه اپراتور مرد بیارید صیغه بخونیم‌بعدش منو لیزر کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70416" target="_blank">📅 15:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70415">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇷
قالیباف:
ما پیام‌های متعددی از کشورهای همسایه درباره
شکل‌دهی به ترتیبات امنیتی و همکاری‌های اقتصادی جدید در منطقه
دریافت کرده‌ایم.
ایالات متحده امنیت تک‌تک متحدانش را با قلدری و بی‌اعتنایی مطلق به منافع آن‌ها به‌خاطر منافع اسرائیل چنان به خطر انداخت که آن‌ها برای لحظه‌ای، تمام هستی خود را در خطر دیدند.
یک نظم بومی و مستقل که واقعاً صلح و امنیت را در منطقه به ارمغان خواهد آورد.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70415" target="_blank">📅 14:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70414">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVxDIkunDeN62Vt8Iq6XYO_tW4oWDO-VXxMWOs9XzFdKOFgTe0HhOKwemToK8H8N6NSrtSERw9zupu7tFtDtbALMfKwGH-hlWisPkLy5u8gzezMYYZ7lfxlgke9T4XrqYXloMHlFf5g3XIUh-Ho_Tt4yddYC6-sWyXHPUZVccumVoy0cGFh34TGRP-zMT7g_aJX9Nmzi3UBWwfh3VWxgrUxVG6XNWH3BhECFzPTaIZnl6aiVfuqCnAtA7VKFbCom745iPqiktizhaMXiNhr9sX11mdhHpwDJVo0UGjOKZ61jxjx8fDHLjlAggDYYgZwsOpw40HCf-zXeT-DAUYKf0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
تصویری وایرال شده از پزشکیان:
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70414" target="_blank">📅 14:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70413">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df1159d44f.mp4?token=Osb9udNGIU6SP888CsSyuZC7m7mfWMPmHyrgv7unvsf3iEmPeNHV4-w658HYDEZ0lihauy4xn_CXwyWxsoUJVpVgKja4ndlhhr5cs8blA4d2FTOT0M5y_uDw3Slas0jKRKyxi7lDbUcoHE5y2c0CH5AFAOQfqPLJHrFd04LyUqitva8m40Q9UJTzu4AdWPMuY4In0bp178NJNGZXELaAFD69d9aTTr8FyUPY_TsldfmFfOhpSpIw5mi0SiIALz2Z-1LJZ1HJLAi77kQDMM9DYIyEpbJm4CoJjDBKfXY5JQiuOcClEbvr8NcqH9XXXYkXUbViL33458LYMGGkmCoZyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df1159d44f.mp4?token=Osb9udNGIU6SP888CsSyuZC7m7mfWMPmHyrgv7unvsf3iEmPeNHV4-w658HYDEZ0lihauy4xn_CXwyWxsoUJVpVgKja4ndlhhr5cs8blA4d2FTOT0M5y_uDw3Slas0jKRKyxi7lDbUcoHE5y2c0CH5AFAOQfqPLJHrFd04LyUqitva8m40Q9UJTzu4AdWPMuY4In0bp178NJNGZXELaAFD69d9aTTr8FyUPY_TsldfmFfOhpSpIw5mi0SiIALz2Z-1LJZ1HJLAi77kQDMM9DYIyEpbJm4CoJjDBKfXY5JQiuOcClEbvr8NcqH9XXXYkXUbViL33458LYMGGkmCoZyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ:وقتم خیلی خالیه باید چیکار کنم؟
خب الان من چیکار کنم؟ نظرتون چیه برگردم و دوباره ایران رو بیشتر بمباران کنم؟
جمعیت حاضر: آرررررررره!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70413" target="_blank">📅 13:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70412">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmAUaHMYs_mJBAiZF2oEhnoRAdOLl8xTD2riqzfz2NDNpD_ZoxXcSibWeVcvqJXJVrFtboK8gT49WcVZ7Z1Jz1ImFX7s1CYwif7DtNCci1k0oAsQVhHcTFMLN8YIQMhS_FtQ0glfdxDdAQaq_eCY7LVRcpCdSdg96XYHRW5HQvRfY0BkV1RxZ8woe2BndP0Na8QObGFW53FEEmwtQIAFAC174Si_zxRldtiCXSIRu1rlu7UYRpUF-2rE1faap6v5jn3zOr39KC3qW-NEFkK95wbeOwjSYxglIazohLluMIpsPmH-XrcAr2ETWCpekS1Dex8StrA7Htt68wDUfkQVRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
باقرزاده: اوضاع جسمی خلبانان ایرانی در قطر خوب نیست
فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح با اشاره به وضعیت جسمانی نامناسب برخی اسرای ایرانی در قطر، خواستار اعزام یک دستگاه آمبولانس هوایی از سوی کمیته بین‌المللی صلیب سرخ برای انتقال هرچه سریع‌تر اسرای مجروح و بیمار به ایران شد.
وی با بیان اینکه محل نگهداری اسرا بر روی آب، شرایط مناسبی برای حفظ سلامت آنان ندارد، از دولت قطر خواست اسرای ایرانی را دراسرع‌وقت به خشکی و یک بیمارستان مجهز منتقل کند.
باقرزاده از دولت کویت نیز خواست با استناد به کنوانسیون‌های چهارگانه ژنو، حقوق اسرای جنگی را رعایت کرده و زمینه برقراری ارتباط اولیه آنان با خانواده‌هایشان را فراهم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70412" target="_blank">📅 13:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70411">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTm_xS0S0qrJcJ3iWQMZeGv8VJkWvh24CN4FYs5hn4elgdhdVJp6Yo-d1As_3QAsljS7OGH4bUrMKqpDgT-G_nsW1ZpSm0IpeLb6xk6FvbRuj0440uKHdSZbWqXV6Gb_Y2r2fRrCBkxix2Hr117JzQ7dDJb-7I9naExA8b5CNUzBa2yc29NRDjzOiKKJLCR7nEsCNsPYEeZxYpEHFi83EDwO7a5b8_ECO_VDgHxFjauHTOWN0BdB7G0bWPh-amCfwkhT4MBYgHCT3NgpxyX6wVAP1r6ibFJQrjPYk0F3sJ2tr3FN6uC92-enzCY6uspzEVMn2vt21DbFv0_iyc1VnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇦🇪
یک تانکر نفتی متعلق به شرکت "ادنوک" امارات، با موفقیت از تنگه هرمز عبور کرد. این تانکر، شب گذشته، از مسیر تعیین‌شده توسط آمریکا عبور کرد و توسط جنگنده‌های آمریکایی اسکورت می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70411" target="_blank">📅 12:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70402">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQ54EaVHupOiWbPsL5xirtcK5PlOBJE9lpgGlCPjWO3nfLrjD9x7BeDz6nDqpHm7nGGtY7r1RbvGlyajyXuUcg8tWcdhqznyGkWCzHeGZo8RMeAgRuTyt7OEoIS7T_u7yhkdyx4Y-X6f7tJHPAz0TqpKhErq4hYdbXoandqnbivtrHK74MBD4JWO97iD46CsZ-Lnx45D3fIaUnR315nz-qzRsXGMiwNJrYp4pnvBLVSz54OAw9kGXPcBvznT2l0RqZQfEMgaJDdkBnIupQ31AdIjeka20-eBSp8x_39fk7BczSzLQJXon6wDMRhkiCwB0RkPK0g0RALRJLg7JEDR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d67kFCqzfufh0dMqPfRCRN_ufSoVxKdWGe31CKpAl_nfSNhZRhLeJmTwOsRk9gUp3tpSlB3PPEK0xAHYSICjX--tgkkfS7mFwQSMcDOmb1EB3ymxi0vElb_B4Lc_ZOFjBmGHqsps1yU7qbd6HbrlQaXcdMXexr4SE12o5jFa8ZaphOAnXGZV4CclKB4OE_FGEWFbXKgJjahZkF1-fvbIsTc6GnVshkl64c6KhKgJqliaamc57IF3otmMmOWEzMcDRFDnRZIT6KEP7UFPoR07irALyKXWW965ZibgiVPjn0ewzkOdP-vYnvVARelWwvWQQHYsn1i9ZEoKfkREzpLsBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DX_81D-XklmT4Jc0DsPupchCMVUGEZzB8aR_fxQKGRFk-M7fF9Bx2YXObpYmQWZwsm1cBixJRO76Bz8wqT7VhERqcekMgruzycNABXpqZW-_bav2zTCd-57oRdmwVPGSNuNZJWiR3hE8O9LmUb2mtVldat0B2Y5TLin1Uszjp-zr2v941xleuozB19f7_0xHdcR2uPr1TFLAv1o7Cege40X0NhfDgz_JEdcalccVO8jX44MQJh8nsO3HL2Rmg-7aA3USh3y601ij13ns--MRlfuINpYxbTRajReQ4vS5rRLbK_encRS3WJzrk5gcEjbbLiONFRq9Lt540p6ytb5EAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/izJ_BuuiQrBxwtAgi28iXnsTAlQ7NeSOxnNrnLBIf0qvJoFTz6ln9T9azqQonUcB5iIyt8rJY5oDJcd26NSw6K4lY2NSIiY3lHf7ywxn25MxBOxTkj2BWcedfF660zkKmwfALuW-j08C9lPiHE1v2H8KFz8Y6bC8sehrdPEPF-sAVb3KCJHB3SkiZ3tkWfTCkaVR8DfS9Re7pCsCWNCLE1cYbT9cj5JZeNOZ7q4IEarJG3JjQRRZ2pzxZZOL-Ya-Cdp4rDvWTBZ2bWArZLY-TeGOT3Tnsr_rsVoyfueBE-TcF81AmNYTqI8rFb0gPC_GecFk0F7hG1q84hCCM6t_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNfEm5tUt8W4HXG1w4PR9rvcgEUxOfubHRfgFpMIRgmpwlI3ps85CZWscsQ9k63sH0HjtK9nCmJDelr2xPoCtTg53Wh1Gihwv8kaU8hbJw3l-ak91KwMqWKq1m-fmTHL1L8HunkQLvK_Blvq7A28cpquqzFIX4v-jaIhyEdkLJxpdH-mQb2rO8HYnmpCRXzlJ7VIENDRCz7ojvbDFaYJm6qXtewfeiPNly2nCHjofwCPV3dH_3EPxFGWU6B8Fk0SQTer4ua2EO-B5h-k-qBmDfW1jNjDD1MXnb2lcoiqR9lO1lJ7JhxHeFHHdLdd1nnu1tBNlIZXaw9AaDLaIjMBPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YJQzC1lHr1kYBuUOQ4nSbsstQhbxH1MuJP5_-ZuPbyziFtXPv00TWAxzXmro377urZc7HvAGHM1t2fndSwrHT5vi81R2Frr6_upWc_jaFa58VhzM_ttqYsYXiCjP17D5K7nyojBe1-4EEAL9AgEOs-Qk2YXdN_tFd7cjavPGtYGvZRBB8mVWk5GdkP2rfJ8hfDnKlojGAB-ZCE1YOR7gsLHIzMr2z_LdR7jWzObaGj9qmF8NXiAKNb-_bgDr0HI0HMuBd6Qct17kPw49bL0E_VFxQdczrCC5_IcqmkSLilKgoqBszHqsWnb7YcJ5YHeCJZ1VWXgDMSKtdhxoiOUe_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S3DkAXWW39x1agjiMId3f5CJQfNIXFc8Mgq2ts90ebIsrvpACHMHkRpIPsv0aXJyWnFAbIcLGXoE2Ap-4Rkko31_0VwDoBBhDIMzNnkJvCQfpNfbzjZmU9hxdwIwPotArP_4yAm1hXhD7MEtR2C7VB2UxE8zeW4Nzix58jZAo-l4Bp12eeGH2bx8bZ0wjZ_Hdfg7PwHRv--3f6pjYncR4MB4fo3G7OCmRV7DMSB6TrT78dquv_DLvE7mDu5EeN0sSuyw40K6ILDqKFXGNOhaKq_hSTl3bZ4nhXKqWtjZ1lJeTdbHOwf3wAXtMaDsHBOk1APJ6P-U7MLM61zN03WNeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGi9lsnEvGv3NjOVYjz3WWiIwo49s7W1KyhvI73H70DSZOHFRyKBjJssH0AgllaScmtNB0Vyu0RjsxmxGoLbZRp7BdQqGGilFrlSmrHeYeY-jodSp1i4VEKm71rcgReLLCJEdlwsaSfcdUFDnMyGWYR00c4yCbAG6Lc0vxxoiFGMIXnu-R5BgKjxYc-H76qDUKAOPxV5TiuEph7wGVmYXo6grFt2ngVgzFU-HX81Djq06AM1bswFKZ9l3QsrcGjP2We28rPp6jrAuFcdqeJu-xlwY7OZuwWolcKCXijFTP3ToqlNVwibhwh3DMtr-gcQdJL2gvIdwAgWodR5pisCrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ceIKpSitHX9eBx5wrqKFZfcyQRVsCXKFT-wfFldt7qMKYXtWvdoN0OS2cNz7tQMWc377x_KlhtCWxdDignfnQCs-n1ZzYG4IjUbUyO9YKUjIh-DPYr5m21lK_ZIsKC-CpWCKYbmKR5fLilJYJWbFN-3Pl5qPZogvGQZfrJULANcioa09zNRKMUAxBofoZY69Glr7-MCquAvjWtAgWchicOo6NFfaX6F5eRMPex0yBC0QG1pfaNa0mgHP7pACyMghApo7JbsKgcV62KbejgM3aHDJbKgAC53u1-GtOS_TfgPzQmVI95c_-aLwqe3mqGZciXDhW35r7aN6mQZi6C_bQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حملات سنگین اوکراین به پالایشگاه‌های نفت چاپایفسک و نووکویبیشفسک روسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70402" target="_blank">📅 12:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70401">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/news_hut/70401" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/70401" target="_blank">📅 12:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70400">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARWFTI-n84gzDQiuTU14Ae3hzOFF5bwptT_YIBungwlaC76MZJB7D-FlAfJVDUOWBtiqpyM1I3T1dkEZuhZqTudFAliPs2uJtZtuivHCwXmcrK0pMCp-t6FQXjH9tQodORNpdgEeQEmbIM8j54vUpId-eXhiL9M0_X6Uk6LurGBJX0c4wbSMDZInyHgeMQcwYRAaXcJlgqMaZKKMkZR8r2NcJsAw_LdA2lK3cGXKW4h7F7SLYTAUcEUO3jJH7g0LdYNPUsvv64gBDeFHYvgBeRKunr958OF4xNHY9S8OQTipOOnX-pzvH4NljlsDdvUF5TvrBLRoP1wkum4uUdCS_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
a31
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/70400" target="_blank">📅 12:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70399">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163f624c09.mp4?token=sS6QCjkNclMpa5NQjQx-hDyXxBHi6SapVHNtppH0hCunyd9MzfQbhfAbrS4dzdPQtiXOS8hoU-2J6UMUgmp8TZmD99X2naTqnOo_STS3ZqRXBHri0el75ZgA8bZ7dCzKkmg4fGNvlmo3jwAvOzOrEMjRU9U7mysa3rsRjwnMb0zWViWMqQWAcsbSrfHMYNmOUFQiN1lXMaLfhf6tTXY2Fvzznq10FwrN9EdWj0eYgjaNghxt27ZdL4DQH-98Rfk_rwhhe2dK8dVVsNfHylAywEF0MgAwnX-6cwv8CIapYON9iY36ZnU52DTQwdn2F7x5A-bwfasXwDEOyE02cCl5_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163f624c09.mp4?token=sS6QCjkNclMpa5NQjQx-hDyXxBHi6SapVHNtppH0hCunyd9MzfQbhfAbrS4dzdPQtiXOS8hoU-2J6UMUgmp8TZmD99X2naTqnOo_STS3ZqRXBHri0el75ZgA8bZ7dCzKkmg4fGNvlmo3jwAvOzOrEMjRU9U7mysa3rsRjwnMb0zWViWMqQWAcsbSrfHMYNmOUFQiN1lXMaLfhf6tTXY2Fvzznq10FwrN9EdWj0eYgjaNghxt27ZdL4DQH-98Rfk_rwhhe2dK8dVVsNfHylAywEF0MgAwnX-6cwv8CIapYON9iY36ZnU52DTQwdn2F7x5A-bwfasXwDEOyE02cCl5_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
توی فرشته تهران، یه مازراتی بجای اینکه ترمز بگیره، گاز داد و این شکلی خودشو ده‌ها میلیارد پولو بگا داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70399" target="_blank">📅 12:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70397">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWhqloQNj_xtUyJW50kaBqse8oJvYspockbOfenF_ua4Rh-vb9bL8JLMO1LjfDw_R5ygr0tf6aSDvLGJtBfKh2-sDb84Iqu5AonXBZjUzt7yqDZGuQ9YrJ8uG2I54aNddt63xFKT9-nDsJd0DPWyqf8z529paN1lxI3lIvFRSdQZf_mVisM5Z9dLFwXpQFGu2P0JRSEdQek3SFD2gyGpb1OTEMt05rCIyNR-r4nCMS8yq3llkgOkfjdz8JFqCtT12YwS7XwpwBxS59DOBCBTW6kT7yb4pr752CEn33EITmBLVY7WgblaB62GL_Y--a34pYoGXVUn_doUY95Zp_X5vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d025747579.mp4?token=mHWUFYJANiCv_HXDpl4-1EVNAgSyuTCcHr4ugqSAqz2A7aQ-FUsGYUgoqnFTkxblRsIENP269c1Tjq0_yAH0M0jc7aLbPmuSPY7a87sMcdlUduPpUcD2jFEeu8jGQCeYp3IwIdydmsEiRIzzW8dcBW_5RnXTY0OkTBeRTtVZpi0mWwjQinT5jYftxjYt-2KzOrP1hiFjzUdXWxCbK-kjDMjZl6S0MPUW8ewVC5nCYdMKM3yFZ0jhM8NgUBtPwi8DLOMWKtXAQebSFxESc65iBEnps4WcXZqxq7K7HNcozJCmdqqkyiSf3JIuhy_Jufe4uPUn914-5XZ80ol7T56L5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d025747579.mp4?token=mHWUFYJANiCv_HXDpl4-1EVNAgSyuTCcHr4ugqSAqz2A7aQ-FUsGYUgoqnFTkxblRsIENP269c1Tjq0_yAH0M0jc7aLbPmuSPY7a87sMcdlUduPpUcD2jFEeu8jGQCeYp3IwIdydmsEiRIzzW8dcBW_5RnXTY0OkTBeRTtVZpi0mWwjQinT5jYftxjYt-2KzOrP1hiFjzUdXWxCbK-kjDMjZl6S0MPUW8ewVC5nCYdMKM3yFZ0jhM8NgUBtPwi8DLOMWKtXAQebSFxESc65iBEnps4WcXZqxq7K7HNcozJCmdqqkyiSf3JIuhy_Jufe4uPUn914-5XZ80ol7T56L5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خواهر پژمان جمشیدی :
برادرِ من امام‌زاده نیست!
مثل بقیه جوون‌ها، عشق و حال کرده و همه‌کار میکنه، نوش جونش چون شهرت و ثروت داره.
ولی وصله تجاوز به داداشم نمی‌چسبه چون اصلا نیازی نداره‌
ترانه علیدوستی؟
یه بار با یه کارگران بوده که زنِ طرف فهمیده.
یه بار با یه بازیگره بوده که دوست‌دخترِ ده ساله طرف فهمیده.
یه بار با یه بازیگر که دوتا بچه هم داشت بود که همین باعث شد هم اون بازیگره طلاق بگیره، هم شوهرِ ترانه طلاقش رو بده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70397" target="_blank">📅 11:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70396">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLvcMEKZvOBoUE2Iu_YcHmtQy_FmnUtaiazJSGjMS4-sLzcdsGWNC0kCFv4XsogB893yf2yYS3cJBj5K70vEHhUO7tnHEiZ_PYwMej2NdbQ6n8AIMkp25FNGaJd6nughH9U8I4wdX7Ql7hdYAjXMwvMhXp4n26wbXiTaFbejc0D4VmRiuKorLakax6o-N9bi2NKoI8x024Rd_BUuWkIvMkdLjEfYwXVKJ9gFtjVBC0BWny8bktPKhZTrPNodMoNf_9BDJtCPZgIeUHzmHrCyaRhYJD1msltved8hyfxBJbkuCKhFi_p7Mp3IWgrq82LE197R5DrjEDft1WKWDT7vtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شاهزاده رضا پهلوی:هم‌میهنان عزیز،
تلاش جمهوری اسلامی برای افزایش قیمت بنزین، بار دیگر بی‌کفایتی و نابسامانی ساختاری بازار انرژی ایران تحت سلطه این رژیم را آشکار کرده است.
در شرایطی که جمهوری اسلامی منابع کشور را صرف تروریست‌های خارجی و سرکوبگران داخلی می‌کند، مقامات نظام و نزدیکانشان در غارت اموال ملی با یکدیگر رقابت می‌کنند و بی‌کفایتی رژیم در اداره کشور کمر خانوارها را شکسته و ایرانیان را فقیر کرده است. تحمیل افزایش قیمت سوخت به مردم، اشتباهی نابخشودنی و خیانتی بزرگ است. نمی‌توان بهای سوخت را با کشورهای دیگر مقایسه کرد، در حالی که درآمد ایرانیان به ریال و زیر خط فقر است.
مسئله سوخت و انرژی در تقریباً همه کشورهای جهان، حتی بسیاری از کشورهایی که منابعی بسیار کمتر از ایران دارند، به‌طور روزمره و بدون بحران مدیریت می‌شود.
از یک سو، مافیای قاچاق سپاه روزانه ده‌ها میلیون لیتر سرمایه ایران را از طریق تانکر، خط لوله و اسکله قاچاق می‌کند و از سوی دیگر، مافیای خودرو، خودروهای بی‌کیفیت و پرمصرف را به ملت تحمیل می‌کند. این فرقه تبهکار که قادر به حل مشکل نیست، از طریق دستگاه پروپاگاندای خود بار کمبود سوخت را بر دوش مردم می‌گذرد و آنها را عامل افزایش مصرف و قاچاق سوخت معرفی می‌کند.
جمهوری اسلامی، رژیمی بی‌کفایت، فاسد و ضدایرانی است که خود ریشه این نابسامانی‌هاست و هرگز قادر به حل آنها نخواهد بود.
تنها راه نجات ایران و پایان این چرخه ویرانگر، برانداختن کامل این رژیم و استقرار دولتی ملی و کارآمد است. «پروژه شکوفایی ایران» برنامه‌های روشنی برای ایجاد توازن میان تولید و مصرف سوخت تدوین کرده است. این برنامه‌ها بر پایه بهترین شیوه‌های آزموده‌شده جهانی و تجربه ملی ایران در مدیریت منابع انرژی استوارند و پس از سقوط این رژیم، در دوران گذار، اجرایی خواهند شد.
👑
پاینده ایران،
رضا پهلوی
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70396" target="_blank">📅 11:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70395">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56910ac654.mp4?token=fUvFowciFDguss9pWU2xNShAQMh19SEnKvX2-BZFazXJ0e-npI7x_RxQ6dQMo3sT36osf4EQs_Gn-pGs7JzS02rI8KjYZNXmiWvWR6ICrAW5XyXZMhgfUSJYzgxGEF8px2h5VEkV9VltyTtCtIlxhQwmvcluyA3Y-6bPrzITEcQ39tKHSs0bDyfy5ElmQFf69UmjKUomRwj5ET98mR_hMc9OvsNb49ICx1vgRB2XcnD-ZWqcW1rkodHvKo5Sat5bFFmBvYT7CCwvdgUdNxQV0NGEJ6SHf9XoGwRFEYM1lbt7EDZjR1RONyA4N1_nmNK79hOSj72nLXEnlP1DCp9OaIuRCblGYlM00-8eQWeqElsL0Vl8VNTF5wNxqvUPYfl3mR8wTJeQDsTZn4uszwEEL2DI1d1vkwwI1ynlS1cvT6ZNSO7JRBD8r0gmsIr7vHsTVTZyASoQ_7V6kC_yvQ9mJwCLWyKn4EpxekKdLvqkjA11WHmsstXWT4rwUVKRLUp7Emr9OlsbCOaKtrEvLY9SBALUwgC0IjpxmJvP8YGqccakRSlpMWSj6ueELPoJCg-gMxs5IK7eZ9_Vn3BjfTJ6LkVu4N4bLj3V7Hskm84781kQymCnPQ-PgrCFFWVxwH2LynWWeuBtFN3cl31BDMUN_3WvrSmPppS9-kOpxV8oAY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56910ac654.mp4?token=fUvFowciFDguss9pWU2xNShAQMh19SEnKvX2-BZFazXJ0e-npI7x_RxQ6dQMo3sT36osf4EQs_Gn-pGs7JzS02rI8KjYZNXmiWvWR6ICrAW5XyXZMhgfUSJYzgxGEF8px2h5VEkV9VltyTtCtIlxhQwmvcluyA3Y-6bPrzITEcQ39tKHSs0bDyfy5ElmQFf69UmjKUomRwj5ET98mR_hMc9OvsNb49ICx1vgRB2XcnD-ZWqcW1rkodHvKo5Sat5bFFmBvYT7CCwvdgUdNxQV0NGEJ6SHf9XoGwRFEYM1lbt7EDZjR1RONyA4N1_nmNK79hOSj72nLXEnlP1DCp9OaIuRCblGYlM00-8eQWeqElsL0Vl8VNTF5wNxqvUPYfl3mR8wTJeQDsTZn4uszwEEL2DI1d1vkwwI1ynlS1cvT6ZNSO7JRBD8r0gmsIr7vHsTVTZyASoQ_7V6kC_yvQ9mJwCLWyKn4EpxekKdLvqkjA11WHmsstXWT4rwUVKRLUp7Emr9OlsbCOaKtrEvLY9SBALUwgC0IjpxmJvP8YGqccakRSlpMWSj6ueELPoJCg-gMxs5IK7eZ9_Vn3BjfTJ6LkVu4N4bLj3V7Hskm84781kQymCnPQ-PgrCFFWVxwH2LynWWeuBtFN3cl31BDMUN_3WvrSmPppS9-kOpxV8oAY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کجا بفهمیم طرف قوای جنسی قوی‌ و کمر پر ملاتی داره؟
این 4 نشونه‌ رو تو هرکی دیدید یا فرار کنید یا سفت بهش بچسبید:
صورت رو به سه قسمت تقسیم کنید، قسمت پایینی از دو قسمت دیگه بزرگ‌تر باشه.
فاصله‌ی بین لب بالایی تا بینی هرچقد ارتفاع، عرض و عمق‌ش بیشتر باشه.
لب پایینی گوشتی باشه.
سوراخ بینی گرد و بزرگ باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70395" target="_blank">📅 10:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70394">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFHxOhYUnjaNqi28-OY3tZnUZvO-yBPBdyU-3Cb2FdIGx1u-bPPZ5kZN8rBsN8wdxYa10f08NlXhcCzw5iXdEg0FoNe6MtOIFoYBLQajPA1377mOtELc_-khKQXH6wIFtV0RuBvGYQKmhqeaVWbGdCxnyLobQ0feRZ5fsnNho1pz7wEABwpvKQXcur7BX9YOJE-jNCgSxgkLGM38d0F57ZkRfR5y99w7B-AD2YILzODOo6ozKdgR_WMc29S-WC-249I4NWYjxLpXgsP8m9sPHvgVuCYv3Qa8a-4cSRV1410oJy_CmZ-RuvD95w9YwKAW3BmLJp8UvgVsRRTkFnM_GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
〰️
سنتکام:
نیروهای آمریکایی مسیر ۶۸ فروند کشتی تجاری را تغییر داده‌اند، ۳ فروند را غیرفعال کرده‌اند و سوار شدن به ۲ فروند دیگر را انجام داده‌اند تا از رعایت مقررات مربوط به بن‌بست اعمال‌شده بر بنادر ایران اطمینان حاصل کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70394" target="_blank">📅 10:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70393">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49fa266ff.mp4?token=DDhuCyDCcZlOCWHa29EIdItEiCUr2b5dLbXzHYu62jaj9ksbZSDa_Aqxyovv1A8nDwqaaaxmb3e1BQ84-ARX-X6n0E4H7UX6L7rSaHveP5tOQoAfaLqg52EBr7Rif5o-t0bOzjn4RYCCr4RkhfAWgAa4_7EU0lTj31-fvpajkE9fIpHrmj94fuCK7V-eyACQLY34DHo-7MprXFyVcAiKHnoaM1XWvryOcn5xi_MWEfwJKledxe4j-gYIc48NYXelu-_HJfziSlilNvmuI8riy7DXWIJjIcrVqY0evUbl3GVjJBorLyBMOxaJroZNRfz_U_Kyk9NKIb0F9TTw9ak2Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49fa266ff.mp4?token=DDhuCyDCcZlOCWHa29EIdItEiCUr2b5dLbXzHYu62jaj9ksbZSDa_Aqxyovv1A8nDwqaaaxmb3e1BQ84-ARX-X6n0E4H7UX6L7rSaHveP5tOQoAfaLqg52EBr7Rif5o-t0bOzjn4RYCCr4RkhfAWgAa4_7EU0lTj31-fvpajkE9fIpHrmj94fuCK7V-eyACQLY34DHo-7MprXFyVcAiKHnoaM1XWvryOcn5xi_MWEfwJKledxe4j-gYIc48NYXelu-_HJfziSlilNvmuI8riy7DXWIJjIcrVqY0evUbl3GVjJBorLyBMOxaJroZNRfz_U_Kyk9NKIb0F9TTw9ak2Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Ai
❌
IR
✔️
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70393" target="_blank">📅 09:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70392">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15aadac163.mp4?token=PiKmngOoLoJHuiEUNZzE5HTsqGoEQwGWvbfuAn07OYZyLU2plwVLqf6Z5_qJUDREe8L9JErskDgpI0aEDiCpczaDsmRCvYKcZ3PE1vGxoOVpS-bQXr4DH1gW7wl0w8bgZm1JlyN62wVpHBjIVm16uxeQOgViEa4iCLFRbqmpKTdWazEEXCzlnBLXJroPtpFAc-ckJObJqO0cLwTpEaAShB5W_Lc7EtoX5OpI71lGW4zTs9Jee9jlcJ8GnF0UYEheP4fEKFvjLvynRRPpDCxYa5rI01n4f_drfQylGlo7af73i2pmih7EwoXMOwBQ7CuJ0hLVQOZVCnRtoeH8SHoCVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15aadac163.mp4?token=PiKmngOoLoJHuiEUNZzE5HTsqGoEQwGWvbfuAn07OYZyLU2plwVLqf6Z5_qJUDREe8L9JErskDgpI0aEDiCpczaDsmRCvYKcZ3PE1vGxoOVpS-bQXr4DH1gW7wl0w8bgZm1JlyN62wVpHBjIVm16uxeQOgViEa4iCLFRbqmpKTdWazEEXCzlnBLXJroPtpFAc-ckJObJqO0cLwTpEaAShB5W_Lc7EtoX5OpI71lGW4zTs9Jee9jlcJ8GnF0UYEheP4fEKFvjLvynRRPpDCxYa5rI01n4f_drfQylGlo7af73i2pmih7EwoXMOwBQ7CuJ0hLVQOZVCnRtoeH8SHoCVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مصطفی خوش‌چشم تحلیل‌گر صداوسیما:
ما همه کاری رو در دنیا میتونیم انجام بدیم.
بریم چندتا مین کار بزاریم توی خلیج فلوریدا.
خنثی کردن این مین‌ها هم کار آسونی نیست و کار سختیه.
شما برو چندتا مین پیشرفته کار بزار اونجا تا یکی دوماه مصیبت بکشن.
بحث من الان تنگه هرمز نیستا من کاملا جدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70392" target="_blank">📅 09:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70391">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70391" target="_blank">📅 03:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70390">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=iPeEr0JfOCIYCMNKZt3VKuJ6WkLhL7E78tQDo9TaGGc_OPgtzqRV7pudMD1XJa9ukEU_pF9wGshEvGxAIqSWgByFn79uguyrSlkhAMBdKltoGjksNf_1TXQT3TNrVgYRd-GAl3qaX3Um9Gn4eilySIcNo5rpQy3ACRoKFk2AuqWOzBfujn3KeQ8nK-eFjYABL66-8xl_Yz0p2bbFoGbiwKOeI7kpVzvxDzYrpYBgPOKq09_D-0ZBAUiNl-hf0DweZZ-sltFGZnJw8CIHiHfGFE-vef-C-wiiNDP-g818LWKMQaISH340vp_CpjTJnBtPyV0A4tb7HBDkgNj6TD1v0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=iPeEr0JfOCIYCMNKZt3VKuJ6WkLhL7E78tQDo9TaGGc_OPgtzqRV7pudMD1XJa9ukEU_pF9wGshEvGxAIqSWgByFn79uguyrSlkhAMBdKltoGjksNf_1TXQT3TNrVgYRd-GAl3qaX3Um9Gn4eilySIcNo5rpQy3ACRoKFk2AuqWOzBfujn3KeQ8nK-eFjYABL66-8xl_Yz0p2bbFoGbiwKOeI7kpVzvxDzYrpYBgPOKq09_D-0ZBAUiNl-hf0DweZZ-sltFGZnJw8CIHiHfGFE-vef-C-wiiNDP-g818LWKMQaISH340vp_CpjTJnBtPyV0A4tb7HBDkgNj6TD1v0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+UfR2NG4GjAMwNTQ0</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70390" target="_blank">📅 03:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70389">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_6NIHunBHVIvrRGk6Wp5ICRJtQ6YWVAK62Fy9o2VMFfyH6ix7woVIenFaum74VqSZAGNPYi04VFmUqWMfjdmgeDcSLIUJ6lCU7UhiMbN3K4WHCOieVPwjGq5-a3ZnKhZbUIYoR0Bg8xaV_o_GeHElXZuzzakOFJCUmTRJk2YZL8Cxl9GGLYh2nFhzh3o9Tk6gwwWS-_eLcDXEZ1nTtYWkxpZ4_MSJHAJ5YZPEa4LNWjYu0N-gWWvzGg0kYOxB7Tp9Ezvc3ipBVL8S6S8FxHRqtjT0Jh6qctpPZZhF31GBVX5ThU80vqG5EiCE5RYkRb9ynPOfZ_KT03L-4G9n9rWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فعالیت پنج سوخت‌رسان و یک هواپیمای هشدار اولیه در اطراف تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70389" target="_blank">📅 02:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70388">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c253cab7c2.mp4?token=QXRije_6cQNJzi_7Bc55qW3vrqlq3dzsaGwT_VejXC8HqkoJVWYBSN1lxBSCJbApSbKPwtPm_thBAvCmz2KUHC0_SKhkUdv3dyReknrRd8xc8OruDHYmJBLUgcHRyFeQ71Ou8HH5n1YdqfNOCiQNio1rTuy_904oInj93Lf4WsCGksjnEV5ulxngH5nvuJO5SwEoysTRMWtINogh4k41b0ccz65UDWlv8nhXyoSH557T_-7Tq5UlcbnPrBgt7oAvMhS0iWNcHDVnDqdReMk1yVJzlrDmnSeT5Epr7MnFfI-Coet4lqRVag083JNGLjHxUxhQRowB3F1BP-XYIj1hMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c253cab7c2.mp4?token=QXRije_6cQNJzi_7Bc55qW3vrqlq3dzsaGwT_VejXC8HqkoJVWYBSN1lxBSCJbApSbKPwtPm_thBAvCmz2KUHC0_SKhkUdv3dyReknrRd8xc8OruDHYmJBLUgcHRyFeQ71Ou8HH5n1YdqfNOCiQNio1rTuy_904oInj93Lf4WsCGksjnEV5ulxngH5nvuJO5SwEoysTRMWtINogh4k41b0ccz65UDWlv8nhXyoSH557T_-7Tq5UlcbnPrBgt7oAvMhS0iWNcHDVnDqdReMk1yVJzlrDmnSeT5Epr7MnFfI-Coet4lqRVag083JNGLjHxUxhQRowB3F1BP-XYIj1hMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
〰️
سنتکام:
ملوانان نیروی دریایی ایالات متحده در حالی که ناو هواپیمابر «یو‌اس‌اس جورج واشنگتن» (CVN 73) در دریای عرب در حال حرکت است، عملیات پروازی شبانه را بر عرشه آن انجام می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/70388" target="_blank">📅 00:57 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70387">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4291f4458.mp4?token=SZ77NYsnHExALRVBcbDq22xWdTqgOq4p1NY-2gp4GorGOcANUWMZ1zZulkgb_qJ0_p5sSGhgRd8iQaxX325KIWMWGsX76y2szjCKwHlckhMFSt1eFi56cu2UrVaYE0d0r4kqivwVfUI7d4P13geb0YmQ2v_yInf60xrEyXCb47qy3wz3Js39guKI45VULS5M3rZL9ej5LiiOuP8vn-4uzAbydxPF6T2k8ZUE4rHNC2X_2uD3qZnNV25respIaWDxfPFbQ5h3FUY8cKHFyRZ8R-TsR-OPpB7qrI6kgbClqVRcB3oI7vgyuQMSnKAKgpd6JWc4tWwjVq_Jbe0hot3B3D3DJMAGn55taC9KW8DbqX5v3NGovq_VAQg5z4HK0Z5-Cn2C8PixOALs_46DNu1URB-esI-3NGTpZb50vnnU9fuqV5_XL6dQnLwK6KyqNale0Aoa2IDGlDHPXFAc8068rA_PrqtxpWtEy6xFX3e6oEcd5S2OnbvNP-uYqzz0E_i1Xqrby3gnyZJbl39rQL8ES30FapG-GX0LXatrocL4FhgejPwqj9_aeliMtZs1VTgUkAkoaa7MtBZNOlB4xiUudfLo21SUAUM0m6LMGsL-bIzauzjfmQaH9OYwQlDjGSEQZbi64G-XqZJNtV8je4DVNk5PGS40FB4q1HGiS_LtkyM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4291f4458.mp4?token=SZ77NYsnHExALRVBcbDq22xWdTqgOq4p1NY-2gp4GorGOcANUWMZ1zZulkgb_qJ0_p5sSGhgRd8iQaxX325KIWMWGsX76y2szjCKwHlckhMFSt1eFi56cu2UrVaYE0d0r4kqivwVfUI7d4P13geb0YmQ2v_yInf60xrEyXCb47qy3wz3Js39guKI45VULS5M3rZL9ej5LiiOuP8vn-4uzAbydxPF6T2k8ZUE4rHNC2X_2uD3qZnNV25respIaWDxfPFbQ5h3FUY8cKHFyRZ8R-TsR-OPpB7qrI6kgbClqVRcB3oI7vgyuQMSnKAKgpd6JWc4tWwjVq_Jbe0hot3B3D3DJMAGn55taC9KW8DbqX5v3NGovq_VAQg5z4HK0Z5-Cn2C8PixOALs_46DNu1URB-esI-3NGTpZb50vnnU9fuqV5_XL6dQnLwK6KyqNale0Aoa2IDGlDHPXFAc8068rA_PrqtxpWtEy6xFX3e6oEcd5S2OnbvNP-uYqzz0E_i1Xqrby3gnyZJbl39rQL8ES30FapG-GX0LXatrocL4FhgejPwqj9_aeliMtZs1VTgUkAkoaa7MtBZNOlB4xiUudfLo21SUAUM0m6LMGsL-bIzauzjfmQaH9OYwQlDjGSEQZbi64G-XqZJNtV8je4DVNk5PGS40FB4q1HGiS_LtkyM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی پشم‌ریزون از زلزله شدید چند روز قبل در کلمبیا که باعث شد ساختمونا برن رو ویبره:
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/70387" target="_blank">📅 00:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70386">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
⁉️
دقایقی پیش حوالی یوسف‌آباد و امیرآباد و فاطمی و... در تهران صدای فعالیت پدافند شنیده شده.
عده هم میگن صدای تیراندازی بوده و همه چی آرومه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/70386" target="_blank">📅 23:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70385">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc11d1c4b.mp4?token=Gv1_JD_EhD7j3EDnlJg6Kr6UThk55b3PsNZGlQfUpnzq5Jpem2uUwvNVMuRzCMWet6Jf0e4USY-tjxbN5emhT79-FDL6Prxks8pYc2yUUYu7yabNZUFa_YZP8637hDWBaqdRlzyQK2Yi-EDEmkJDa_l-uHijWxjrzJ6uSwVu2RBnPuo3yxY1aiOrGSvkj4zT1VPGJ_hqf7nPf4CBNE6yOo86rAcDJYy_uIkaxKcTqcPDzgemzNUnRGwYAv257_YezvtakmQoeRoAUS2DiMs9uDJbb8l6O7hyAY8hyuC-uUepTxDbKXj_eIcpfRZe2jfiakgkR31uCHPye48SMzBgUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc11d1c4b.mp4?token=Gv1_JD_EhD7j3EDnlJg6Kr6UThk55b3PsNZGlQfUpnzq5Jpem2uUwvNVMuRzCMWet6Jf0e4USY-tjxbN5emhT79-FDL6Prxks8pYc2yUUYu7yabNZUFa_YZP8637hDWBaqdRlzyQK2Yi-EDEmkJDa_l-uHijWxjrzJ6uSwVu2RBnPuo3yxY1aiOrGSvkj4zT1VPGJ_hqf7nPf4CBNE6yOo86rAcDJYy_uIkaxKcTqcPDzgemzNUnRGwYAv257_YezvtakmQoeRoAUS2DiMs9uDJbb8l6O7hyAY8hyuC-uUepTxDbKXj_eIcpfRZe2jfiakgkR31uCHPye48SMzBgUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ظهوریان، نائب رئیس‌کمیسیون اقتصادی مجلس:
افزایش قیمت بنزین مثل چیپس و پفک نیست که راحت بتوان قیمت آن را تغییر داد
هیچ‌کدام از ۳ طرح مطرح شده، برای بنزین مناسب نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/70385" target="_blank">📅 23:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70384">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9209031f2e.mp4?token=f6_Hj2M1WGwhuw8dzO_bj9u3TJEhGZAk7Nc83q7jXhQ5zgZ_Sn9mM1OCJecQKlwgcJ8Oul78H2es3vqMtKrK42kbvRkzVN-Ibc523XRw1Lc5ZsrPz9Iyiiwp16jYGQn5alY0eqb557wECDtx-L2PKPS455TkdcNCIkfcacXaJskB3u8zqCL39wqagIs5jHHkne08yr9yzqLjUTxY3oUL1Bj6woRVOucTulo6FdhNlzzp5_Y35YtDduBJzJndbmMkx6JCf1YcR1QhTltYpnigTJDrYo8IlIG99nRU80YSV1zHIshXXoCgAewfK9NN_XxPLrwfTb8o65RC8Gea7dRFmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9209031f2e.mp4?token=f6_Hj2M1WGwhuw8dzO_bj9u3TJEhGZAk7Nc83q7jXhQ5zgZ_Sn9mM1OCJecQKlwgcJ8Oul78H2es3vqMtKrK42kbvRkzVN-Ibc523XRw1Lc5ZsrPz9Iyiiwp16jYGQn5alY0eqb557wECDtx-L2PKPS455TkdcNCIkfcacXaJskB3u8zqCL39wqagIs5jHHkne08yr9yzqLjUTxY3oUL1Bj6woRVOucTulo6FdhNlzzp5_Y35YtDduBJzJndbmMkx6JCf1YcR1QhTltYpnigTJDrYo8IlIG99nRU80YSV1zHIshXXoCgAewfK9NN_XxPLrwfTb8o65RC8Gea7dRFmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
❌
🇮🇱
فرمانده سابق نیروهای ویژه ترکیه، زکای آکساکالی:
اسرائیل نمی‌تواند با ما رقابت کند، ما مانند سایر کشورها نیستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/70384" target="_blank">📅 22:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70383">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0l6UZYXrx6ImF6y3T5-gMrrnOiR6NckDFHI-5eAYIssh5uKk-fcMLyAtI9IdtpwSAiIm17HCDHOqGxDu8hHb7GkDtvaMXeU25WuSasqf8YZ1nb-DsWVUEw2eznwycGxBPN8c5bHtf1aE3lfpjRAIOue6sK4gKFFg-mCSFFABEch1hlUFgE3ViGSURieg2VsidPo1wXM2DVE_oaOWtTRXFxW1sSdCbxCDrLVEF1SzlfBPQ93NmW1LbkIKbN_AEhvFTSpKx9rzIOhEpImRUCa2cG6V1ZjTsQg0kggZfc_ePgA4cvDWvc6qXfNi5XssP0b1BQyD2wzltcFYY5NahD3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ بازنشر کرد:
رئیس‌جمهور ما به ایران هر فرصت ممکنی را داد تا سرانجام رفتار خود را اصلاح کند، از نقش خود به‌عنوان بزرگ‌ترین حامی تروریسم در جهان دست بکشد و به کشورهای تولیدکننده بپیوندد. او درباره پیامدهای ادامه مسیر غیرقانونی و وحشیانه‌شان به آنها هشدار داد. اما «رهبران» آنها چیزی جز رفتار تروریستی و قانون‌شکنانه نمی‌دانند و اکنون رئیس‌جمهور ما به وعده‌های هشدارآمیز خود عمل می‌کند. این‌گونه است که رهبری واقعی عمل می‌کند!!!
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/70383" target="_blank">📅 21:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70382">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7188f3aad0.mp4?token=s9wkZEUN3lxA_ZzGvz2DCFGeyVOGtu38yCYlrx8RacJN2tdMtWv2PI1sfPxOkN6tj9ozc9XTsco6-So89OFMcHyH-SCK5prByuqtn6hw5LjJuGjM2R011uuT44_AxShnAEBgZfrMFcc8_JM9iXLrd06eB0kmSyZJdQVgaDrNXPvN63MzD0sUHUZQ63l0wMaBguovwwzNpM_5JFAjnhnd4fyChdxbiWL405GrdoHEPcb1fPhfo5zQHqxP9e04VNHvTX5x8MsAZzsDUlYOGb_2he-6OyFPJF5UkRDDUwrufVxtEMoQS3xCh4jPCcMQgdga8KafaldwBVMC3zjJcuvMew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7188f3aad0.mp4?token=s9wkZEUN3lxA_ZzGvz2DCFGeyVOGtu38yCYlrx8RacJN2tdMtWv2PI1sfPxOkN6tj9ozc9XTsco6-So89OFMcHyH-SCK5prByuqtn6hw5LjJuGjM2R011uuT44_AxShnAEBgZfrMFcc8_JM9iXLrd06eB0kmSyZJdQVgaDrNXPvN63MzD0sUHUZQ63l0wMaBguovwwzNpM_5JFAjnhnd4fyChdxbiWL405GrdoHEPcb1fPhfo5zQHqxP9e04VNHvTX5x8MsAZzsDUlYOGb_2he-6OyFPJF5UkRDDUwrufVxtEMoQS3xCh4jPCcMQgdga8KafaldwBVMC3zjJcuvMew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
در شهر برن سوئیس در تابستان، خیلی از مردم، در مسیرهای مشخص بعد از پایان کار وارد رودخانه آره (Aare) می‌شوند و همراه جریان آب تا نزدیکی خانه‌شان شناور می‌شوند.
لباس و وسایلشان را داخل کیسه‌های ضدآب می‌گذارند و در نقطه مشخصی از آب خارج می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/70382" target="_blank">📅 21:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70381">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7Slv1M_i8Qzh8r386St5UUSsmZ8BdvB20k6vJ-bxI8JQ-gvqnf8C2NQoTy9PSXzUXqxCUK0cSHRluk4GzeLsQ4OT_oVFoW_1avLp-uwFIVWxBPiiT-4CGQlUMOaCrO7tGrtUhvVBR3IZaZkpbtaNJs9gpQti6u0wEcRDxIIKZ7lWYeQt6Y2WJFlbCUUIKPJstuE9zdWpAZoLYQX9F5yThj6w2rB4kPo8OGfTvLqfP_qt_id9gf-fSvBemhLKF37n0RkgodskffniwpyoPXE-nn9vOgF_4Wt9Msd5AdxuiJek2X208wdBIQ_nrKOmNyJXsE15wsvXlojdOvhLAdNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس:
ایالات متحده ثابت کرده است که زبان دیپلماسی را نمی‌فهمد. آن‌ها نه تحریم‌ها را لغو می‌کنند، نه منابع ایران را آزاد می‌سازند و نه به دزدی دریایی پایان می‌دهند.
با این حال، تاریخ نشان خواهد داد که زبان قدرت، آن‌ها را وادار خواهد کرد تا نه‌تنها این اقدامات را انجام دهند، بلکه از ملت بزرگ ایران نیز عذرخواهی کرده و برای همیشه منطقه را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70381" target="_blank">📅 20:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70380">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVUGwqFlUvHn_MphA4hwa_6fH_DNaOdbCDEAQl02uLF4buar_AzCl-By45DRSoaF-CZr07FX-QsCYe48FKNfD1Gtk9fkYSXPxr0Ksb1Y-lcudhIZg9wRUmBeRacxTZVOxXuWzMMgIjNg5W8u2c3E1hhnn4t5OioJyXuLAiTpxe4ONPYgKrudMNf-SrNE44RuZVIAYYrPzTgyIWeTj7uShWd7VzU6yeT7LLnKauyfmAuXbxV5E9eR79sjS6108FgdVB-KUjs8l0VpyAUHS9qxFiweR5b2RGpCDvjz9OPtbASuccdTdY-YmoFlIy-MqE9XV94ed-P2xQnCtiG67MM8mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی:
۱۴ سال پیش: «فلج‌کننده‌ترین تحریم‌های تاریخ.» شکست خورد.
۸ سال پیش: «فشار حداکثری.» شکست خورد.
۵ ماه پیش: «تسلیم بی‌قید و شرط.» شکست خورد.
امروز: «ویرانگرترین عملیات اقتصادی تاریخ.» محکوم به شکست است.
ما این فیلم را قبلاً دیده‌ایم. همان حرف‌های پوچ؛ همان قلدرها، اما با چهره‌هایی متفاوت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70380" target="_blank">📅 20:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70379">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781f58184f.mp4?token=VWgGsluMHkpdClRz2sIzgoI0zhkJ8Td7L35PN8qE7ub_1Ql9bHXXzzxcBYBY8az6KU-2_QCgoGs5bfzCOust7SpTXl1zEzVObO2XcDyiljcPO9R9jfyDQjZRFwxyp10WgrNynDAxUKuv8N4XReX97gQ9_HSfCCP7fGuugplRFAGF8di59DXrPJg7MbwS0oEE5-xWf6PXYWfJ5WpyjNkXsIk-xhEx7Qzm4Wid8gsllXHQWlmwQxcWLpnnuY9TTm8aqb8hZD8zFlhtVsHp269aa20tTB7dnoGtrONxZzqBDRZRL7JOmpt2Ttxhr09Uj27eKe2sMgI7TfCLVKfL8csSA65mZFHM8CGN8S2YX8lAMfsY52Cw2Kt18q-0UpOKZcb62dB_RUhM5GL8oJ0SYPxzq597heZ2abSGnwg_EJIa-NrvTxcFwNsvEIx2kzjc4RUmVLsvasiw8_yY6JzGLLlRKxGd7lmTJ_Q9JJFWoLrN8F0iUELLEgHSyylKeFc8r71oCD55pNCZcMr6adS9sq73N8q79TZGpj12HwGDvJeh9dPrORiCiKbZiPevL7kn4zS-au7_uIbFl62Sg2wV8ozbUZO8nkUbjgrvfZmrRn-V2TU1Q2RGhyDZ1wdWqSBKV88ZyAhG5XpNHRIaeFPsOONqtzMI-5Uj0Kzj0lkSXZfqI7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781f58184f.mp4?token=VWgGsluMHkpdClRz2sIzgoI0zhkJ8Td7L35PN8qE7ub_1Ql9bHXXzzxcBYBY8az6KU-2_QCgoGs5bfzCOust7SpTXl1zEzVObO2XcDyiljcPO9R9jfyDQjZRFwxyp10WgrNynDAxUKuv8N4XReX97gQ9_HSfCCP7fGuugplRFAGF8di59DXrPJg7MbwS0oEE5-xWf6PXYWfJ5WpyjNkXsIk-xhEx7Qzm4Wid8gsllXHQWlmwQxcWLpnnuY9TTm8aqb8hZD8zFlhtVsHp269aa20tTB7dnoGtrONxZzqBDRZRL7JOmpt2Ttxhr09Uj27eKe2sMgI7TfCLVKfL8csSA65mZFHM8CGN8S2YX8lAMfsY52Cw2Kt18q-0UpOKZcb62dB_RUhM5GL8oJ0SYPxzq597heZ2abSGnwg_EJIa-NrvTxcFwNsvEIx2kzjc4RUmVLsvasiw8_yY6JzGLLlRKxGd7lmTJ_Q9JJFWoLrN8F0iUELLEgHSyylKeFc8r71oCD55pNCZcMr6adS9sq73N8q79TZGpj12HwGDvJeh9dPrORiCiKbZiPevL7kn4zS-au7_uIbFl62Sg2wV8ozbUZO8nkUbjgrvfZmrRn-V2TU1Q2RGhyDZ1wdWqSBKV88ZyAhG5XpNHRIaeFPsOONqtzMI-5Uj0Kzj0lkSXZfqI7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یک آخوند در تجمعات شبانه:هنوزم از کنار بیت رد میشم بوی گوشت سوخته آقا میاد
🤣
🤣
یه روز یکی بهم‌گفت بیا بریم بیت هنوزم بوی گوشت سوخته حضرت آقا میاد
گفتم اغراق میکنی چنین چیزی ممکن نیست
خدا سر شاهده رفتم بیت دیدم هنوزم بوی گوشت سوخته آقا میاد
نامردا ۱۱۰ موشک سنگین به بیت آقا زدن
حضرت آقا بدن لطیفی داشت اصلا ایشون آرزوی کربلا داشتن هروقت میرفتیم‌کربلا میگفتن به نیت ایشون قدم بزنید
الان رهبر شهید شب جمعه ای کنار امام حسین نشسته و داره ما رو تماشا میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70379" target="_blank">📅 19:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70378">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rz5dtzccIq4Q-T1H4L7uCx4EAVzos1OBJsNT-vNOcPTqszioafyraJ_ojnKRVzQg-gXHoLgwoZy1bf6Gy_e8oEH3kDLjGcZC2V8nnf8DsBi3SyMtKLQoMp5Lz3X4M0gEusgN4-m-Td-LD92yOqis0do-Z_Y30AEscEXCw9YmErQe1_R30xOmJx0B2elmYbU1HA9M79uKnp9t_8aNvdAhaXZ3YitpuZaBxh1wAdM2-RZ63oCohPt5RZkn6TvGYPzxGztP7eBD2UCovdpSTJssgmB1qxnkSnpU-Nx1jzvqpMYjvQUFcBWVTYaREVKRpjRV_n7R8gzYTgOLkd6uHc03nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
〰️
سنتکام:
تا تاریخ ۲۰ اوت، نیروهای آمریکایی مسیر ۶۷ کشتی تجاری را تغییر داده، ۳ کشتی را از کار انداخته و برای اطمینان از رعایت مقررات، وارد ۲ کشتی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70378" target="_blank">📅 18:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70377">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb50540ec1.mp4?token=nWsErtZb9K0uYflJy2QEfsLL2zozZnK9Rvr26DE8rs4ftMFAPrcgRCAsiIx3KncmCf3-l-Q0HJdH5gMkvQIQ7rMuEG77LBaINoc6gdOPQcbBgsikAcnD4GVyz2o9rUmdbGjCkkLyRywLVIyXjRGPI4xA-ylKa15N1vOnYuwdqUjCZZT72zUxmLf-3tLaGBd_yWNJPPfrUgT3HbHMHuewBJl6xje9kt8btW6n3lETFix4NAerQezQyFaMbWqBLSFpuvFeIAhC2_lAskwMWu8zK3mVWOHxNE6bUKLrfY0ZGTvZGjIBKvvDv2R40bg4rbRPCelNi130a0lGL0hJNQYZC4a46xmTwZNtoh5yW8U5DUnB9QylCVmxPT-ihZ1k2z7_G7FwtPvDamcHAP_30PcdT1TrzaBxN0Hc0HPMEMY99N194Dl5w1tNF93vNRSisEXxhBnuci6XIpAzjv3I6ROGkF55EGhRIgFeehsxjfjB0Tt1fjhiZMts1yIkOgEeYPdQ6wlv7gVfl74UVN6WVDQ9HxkejpDNE57-CEjtbYaMY0sug5lNjx5VSsffuMCzTmlYJP0c_sEJYWxHslcKxy6eKQQsAjXowSfWMC8GlsxWf1jMslGc1pYM9DgCzwqObKBgtg10g1kE6z2fFnEk4oWaT9QMKk6D7KEhXneUOvxvU78" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb50540ec1.mp4?token=nWsErtZb9K0uYflJy2QEfsLL2zozZnK9Rvr26DE8rs4ftMFAPrcgRCAsiIx3KncmCf3-l-Q0HJdH5gMkvQIQ7rMuEG77LBaINoc6gdOPQcbBgsikAcnD4GVyz2o9rUmdbGjCkkLyRywLVIyXjRGPI4xA-ylKa15N1vOnYuwdqUjCZZT72zUxmLf-3tLaGBd_yWNJPPfrUgT3HbHMHuewBJl6xje9kt8btW6n3lETFix4NAerQezQyFaMbWqBLSFpuvFeIAhC2_lAskwMWu8zK3mVWOHxNE6bUKLrfY0ZGTvZGjIBKvvDv2R40bg4rbRPCelNi130a0lGL0hJNQYZC4a46xmTwZNtoh5yW8U5DUnB9QylCVmxPT-ihZ1k2z7_G7FwtPvDamcHAP_30PcdT1TrzaBxN0Hc0HPMEMY99N194Dl5w1tNF93vNRSisEXxhBnuci6XIpAzjv3I6ROGkF55EGhRIgFeehsxjfjB0Tt1fjhiZMts1yIkOgEeYPdQ6wlv7gVfl74UVN6WVDQ9HxkejpDNE57-CEjtbYaMY0sug5lNjx5VSsffuMCzTmlYJP0c_sEJYWxHslcKxy6eKQQsAjXowSfWMC8GlsxWf1jMslGc1pYM9DgCzwqObKBgtg10g1kE6z2fFnEk4oWaT9QMKk6D7KEhXneUOvxvU78" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این هواپیما پس از گرفتار شدن در تلاطم (توربولانس) شدید، ناگهان وارد یک وضعیت کاهش ارتفاع تند می‌شود؛ وضعیتی که با پر شدن فضای کابین از صدای جیغ مسافران، موجب وحشت آن‌ها می‌گردد.
تلاطم هوا می‌تواند باعث تغییرات ناگهانی و شدید در ارتفاع و سرعت عمودی شود. اگرچه این وضعیت از داخل کابین ممکن است بسیار هولناک به نظر برسد، اما هواپیما به گونه‌ای طراحی شده است که در برابر فشارهای ناشی از تلاطم‌های شدید مقاومت کند.
بزرگ‌ترین خطر معمولاً متوجه مسافران یا خدمه‌ای است که کمربند ایمنی خود را به درستی نبسته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70377" target="_blank">📅 18:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70374">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MOJkf_JWohMrrHCkKgU7M7jo48LRSuES6EKyyDr9xm7UzZsuhzXLyaZhwkBZCRPRCnbBrrEHy_yYCUW0Idpemm6C5MjGTC1SwzrzcMcy0U07rsxmbVXGsDIMzVZBwU_6j2vnlHgbk9El8xzZQ8FzfUcgy6qzxTnfPw-OQWBRRLyUP2CqGQxRJJ16EVb6S8wt8pAPF6-s2sqPBjUt-lIk-ebebDOSitjAVJ9M03764NWcinLgBEtH4A4hufS-EQko__VCEpj3YPYBr4iN8Q4Vy6YyNYIWD0Tm272Hv02Banb27H-65EsS_iuDIBsdw6ifMSFMMPcqPoJzPtAVnQycGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OmPukjlVd-vCm9Yqz2X3YXutoX87LFUpDdITm5AezrB4IhygKGO5SsbEi__h14Dh5Ca_qceoyWVNBMDWADmCA5LqGknj1zw-0HvU-LqwSiocIRlqNVs-Wu_XcfeW1yzc2K2pyl8w-LU8M9Wh_ZyMFHzz0vu9Nu3P1WSGcdpCoLMU3ZzJWF1Y-ZadYt-OTn06P2yI8_8aNaMBij0Y0HILKWVGNsM8-BOPczrm9gL5ESFuKhgRykHp6LHWy7-yf5SEMq3spXvjwYbguQeUy0KJddj0f91uLyp3bjNuASZYS7RUjcx760qcpf09bETeHABGC90vuwAKXS_lAIwC83ZryQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee703d2eeb.mp4?token=p8vcF41RLKpSqymXPqCZrtld3Co6U06vFxyz4d0dnnpkXlftq2Dx0OhP0rz9kKOVFdDL4-fg7bwj5Xh4vWee19faRF6GPcLu9bz3wfDS5Em0VUjRZ-k3EDLfRxNcdhonaPp2dKmESW1F2GvA5-IdCBKUfwNEznYDqcOUqy4AqHXzXE5H5JHd3eQQSQENILKXvx9o2cJmJymuwJiBWSl9lBr04HukrHAT9EL8kW3Go32kVdiGSpYMHVVo7fCoyamPo_S9zyIMPGiFKEikbkw4v89jUr07VMt76R-_uppw5aiiC6vhyl8k4jFvSgsFlzw_eavY2PQ6HlirsqLc1BzDoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee703d2eeb.mp4?token=p8vcF41RLKpSqymXPqCZrtld3Co6U06vFxyz4d0dnnpkXlftq2Dx0OhP0rz9kKOVFdDL4-fg7bwj5Xh4vWee19faRF6GPcLu9bz3wfDS5Em0VUjRZ-k3EDLfRxNcdhonaPp2dKmESW1F2GvA5-IdCBKUfwNEznYDqcOUqy4AqHXzXE5H5JHd3eQQSQENILKXvx9o2cJmJymuwJiBWSl9lBr04HukrHAT9EL8kW3Go32kVdiGSpYMHVVo7fCoyamPo_S9zyIMPGiFKEikbkw4v89jUr07VMt76R-_uppw5aiiC6vhyl8k4jFvSgsFlzw_eavY2PQ6HlirsqLc1BzDoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر لب ساحل ، با این پوشش ساعت ۷ صبح رفته و از اون ور یه مرد با شرت هفتی اومده بهش گیر داده که تو چرا اینجایی پاشو برو تو قسمت زنونه...
دختر هم میگه داری بهم استرس وارد میکنی، مرد میگه استرست بیاد بره تو کونم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70374" target="_blank">📅 18:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70373">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">امروز تو ویپاری رو برد آرسنال
⚽️
100 دلار بزارید 245 دلار (25.000.000تومان‌بونوس میده)  سود کنید.
✅
🎁
برای مبالغ بالاتر از ده هزار دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ بالاتر از هزار دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/70373" target="_blank">📅 18:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70372">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari (3).apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/70372" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر WEPARI
😀
😃
😄
😁
🔥
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 120% اولین واریز
‼️
🔥
بونوس برای 4 واریز اول
‼️
⚽️
بونوس ورزشی هر دوشنبه و چهار شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🔥
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
📌
آموزش نصب برای IOS
g39
✔
https://t.me/WePariFarsi</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70372" target="_blank">📅 18:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70371">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea7209957.mp4?token=vT_zAR-2PlSZu79eP_GZ_q7hfRersicyjVf5JaVqGHa-14fTD79DYSy99gaj7dPCrMh9PLm5goMTMPad62mZArBHrJXmp5EPuoeQZAWnIPpuE5aFQXJWY2M39ZYA3jsM8m69lDxYHbBhksG40AKoC4MS1XmBGsb8zzYOb0s8-B_I53NgdJ7pmrgsHdopHY0LM9X6Fdxp3OxpUzf7IYahpm8qPrG6YRoSgp2_vTgwxSnzZ3uAxUS2X5Vjo6y_iFa7uQHHAGPl69tyAqx8HfzlkjkezknoE0Mds3ZOA8xXTdb1ecLAM7gduZ-6IfKQLHu3i92ItF3dlscUp7whNAZXiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea7209957.mp4?token=vT_zAR-2PlSZu79eP_GZ_q7hfRersicyjVf5JaVqGHa-14fTD79DYSy99gaj7dPCrMh9PLm5goMTMPad62mZArBHrJXmp5EPuoeQZAWnIPpuE5aFQXJWY2M39ZYA3jsM8m69lDxYHbBhksG40AKoC4MS1XmBGsb8zzYOb0s8-B_I53NgdJ7pmrgsHdopHY0LM9X6Fdxp3OxpUzf7IYahpm8qPrG6YRoSgp2_vTgwxSnzZ3uAxUS2X5Vjo6y_iFa7uQHHAGPl69tyAqx8HfzlkjkezknoE0Mds3ZOA8xXTdb1ecLAM7gduZ-6IfKQLHu3i92ItF3dlscUp7whNAZXiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه سری دخترا بخاطر اینکه امروز کنکور دادن، این شکلی از پدر، پارتنر و... کادو گرفتن:
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70371" target="_blank">📅 18:01 · 30 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

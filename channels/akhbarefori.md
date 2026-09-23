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
<img src="https://cdn4.telesco.pe/file/sUmA3nd-B89jWW6HDwhHZo0ihHyuxftv5_fAebwwIAJvMmSCMjgr3nm42K229HPhRQX9QImlxeBf8fIW3OPmhm9bmcnpuw3sunaf7ewvfBLo19oonOvDpMyHuidhRw0CywTbwZ0xgO-cIjeOjJCfGnRVNev_k1AJWm2GE2teaiAEXDpsf9IKvGIZgNiVrSvFqBgfrn5G1B99mi-u6ZoImfT-vcrof1t-k1yslbapWGHkQA1WR3enu9II8tyP7T4rNL3cBlVDwLu6ytZ_anZmWTjqqM7QFhD5xJ8YF2d689jcaU8P_Uin06lMm-Mt87FzwvyrJYeK5TYY6M9ZoL3R-Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.05M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 18:37:34</div>
<hr>

<div class="tg-post" id="msg-692371">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a449a8b51f.mp4?token=ttw2aYz9uP5qWlHoBo5tcKM724oLyChRPYhWbRiAvkl_KuwfaRMjkS-W9D9Ut6Be9BwyiASsTAOAdz12frpU4FnI-4WikhP3mfbRkU_pEcapT5IvU4ZbjdX5X15qaMyFMJ4Kxen5WFySRYi73IhJcDTwTHtrXid6dru6uVTYrkWgdFhBpk6G3J6dmrudzyPXRsv4tMCCFLuFljRt2J_3nUw6pyKvQs6qzEzT_Wi9MLgaeNbjQ5NgRdObfIsmr8TnG-7xDYzWGh4CoYi3WvfiJ9i11IhH3pmEgublLP0pHgk_1WoAW2Z1iTP1YXdYsg49ndDuhmqFN9pZZ7NL_d5Q6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a449a8b51f.mp4?token=ttw2aYz9uP5qWlHoBo5tcKM724oLyChRPYhWbRiAvkl_KuwfaRMjkS-W9D9Ut6Be9BwyiASsTAOAdz12frpU4FnI-4WikhP3mfbRkU_pEcapT5IvU4ZbjdX5X15qaMyFMJ4Kxen5WFySRYi73IhJcDTwTHtrXid6dru6uVTYrkWgdFhBpk6G3J6dmrudzyPXRsv4tMCCFLuFljRt2J_3nUw6pyKvQs6qzEzT_Wi9MLgaeNbjQ5NgRdObfIsmr8TnG-7xDYzWGh4CoYi3WvfiJ9i11IhH3pmEgublLP0pHgk_1WoAW2Z1iTP1YXdYsg49ndDuhmqFN9pZZ7NL_d5Q6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سردار حسن‌زاده؛ فرمانده سپاه حضرت رسول (ص) تهران بزرگ، دکتر زارع؛ سخنگوی ستاد مردمی جانفدا و سرهنگ کوثری؛ معاون آموزش سازمان بسیج مستضعفین در اولین دوره آموزش نظامی جانفدا در تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/692371" target="_blank">📅 18:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692370">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
رویترز به نقل از یک مقام ایرانی: تهران در حال بررسی پاسخ آمریکا به پیشنهادش برای پایان دادن به خصومت‌ها است
🔹
هنوز اختلافات زیادی بین مواضع ایران و آمریکا وجود دارد، اما دیپلماسی ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/akhbarefori/692370" target="_blank">📅 18:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692369">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
مجتبی زارعی، عضو کمیسیون امنیت ملی مجلس: عراقچی مجوز مذاکره با ویتکاف را دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/akhbarefori/692369" target="_blank">📅 18:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692368">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
وزیر امور خارجه آمریکا: به تعهدات خود در مورد توافق دفاعی با عربستان سعودی عمل خواهیم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/692368" target="_blank">📅 18:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692364">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6cRQuqETp6QLM6KX5pcW6s-QuZuY6lR3qmX-VvZJf6Kbmo6pa-ZffEfq_ZZL3HrzVWyJUCTOw1WkJYHsLR9bntSs6dmBE6ztXcUediYHIzP9t0dNx7cQ9Zr6sFcf7WD3x1eA57NtTbLIqmjNrT3hl4BLDp-0NVbUY5gKNlAv6UfwnV-_BOOgDlzUCVJa8518IGXLskKOoX7K1aVxyDwSxQgExxzdRrbR3uh3YkmDypsiPE0H__2In_c9m3mjlkDerhdt-h-FohklmsxFeShrJKIZ1-3ojLhafAnVWwP16j_0gB_RJZvsUAtYM2vD7zK0zyZ6YOFidqAp420W_c84g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یکی از مهم‌ترین اصطلاحات ضروری، اصطلاحات مربوط به زمان هست که به‌طور کامل این پست بهمون یاد میده #زبان_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/akhbarefori/692364" target="_blank">📅 18:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692363">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/swHrxn8A--0MjI85jlb5VVeK65-HjWGEDQhQpT6J3-V_XVOvPPNOH9rFLo_3kdzCHbj0v0AF4a30lO3lAg63R_dZ8hUAp0GC330svdBLls4hwGj2GhebQFqa8ZNKv1vmrEc8dw5Wrc5gpUH-9cnClVv-plFiIH3SQktxHkytZdr08tVLET_avRJDeV5XVV-LJiXuuQmzWocpN02TrfCy8x2vloDiFZxiPGb1r9p3nw4udyeWWbFTZh55qoQJBgbd9ZdnwDYQ16dLvAvZVz5JBJ9EdSWDZbEPXNH1rIdK6Qd5qDZcmkniZyVwCpTRQ-JeNzQXdgItInnXejEbBXWIgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TEeqyi2-8E7wvBt77sv0-BPXqrnSIcXbonGKU21MuoZNS4M9Te2VJ83MzVlgs9ztzt9zIoZQLBPRlxa5l5dNiGOmK5z4kkfJcWvQS7jW-y8NIcIiVjFSbl_rFWWEykA7szlrnOS86JPHoVEW9MClMPWFbnAj5-YmHNpQ6yMoJqQdUco_OKp_sLij-UZ3mu5aU0785XTusA4_Ufqw5anoO3f1Q1QDDVcjkhB2gqgcsDKMah2cTWy0wJCxUHQdorIg53-deiug82k_5Q2zREVoZK-RxQpuMfNka2Raz0XcvqsQLjyF8WMAPciiiJ7ghtQAkRb8e-hIGQqgXHvLsjbN8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XCGBoMCwuLYm81R5gTrwY5ZDV8NaToHcXw1ZXhNMvA0zA3h5c40l3xwJvtMRQU1fJmukhqAaKPgUVcfSjIurPGieRK1e0tOo5CQYNSizTLN-ymwwq8oqVbD7Eguwta9ErlnuPmT4ttOuRtWdO-dZtXbO6utX6UQBlWSjX3XfN7Q1sonxTFwT7oHEyjWaG0rrbWhz_uGZakuxVrxQqehF6WXGlnx0LT5uhPoJnxmHgdBNvL-HHGVgOiqgo0VxRpIL0rhrKvP_CXYr38vIsNG5ArdyJkmTzRuVTOq2UuX2mRy6Myq6QjISxDBZ6SriiCvtojIC6KCayTem07L8neb94w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NnXKZTWub-Xl1ZTrsOHcIoVi5C1MPq6ANoGSRbucGFFHLQV8Uv-GEYiUHUXEun1G2HBuuFtQYOT2G7y5VHFn8-virJJuGBEjpmohVkDL6KY7Zht_4Zu6WXkBK5fOIKZgLam0vTfWvShxiSsjO8eGW6hN-IPl4jhmD-shP8v333bBH2ZV2GdH7hz13omNUsXfRxp2FpLepA7-e4jwrz_zzXj6tyAFb8FVAIzE4XF8YzkUCoSDr6oTUVC3-Qu4UbNFjZpYFdz5v-OA8ive5oUY8rIDccgv2XuiS4m9LcR8vFX_4yNR7DQdfRT6Fm9Z0YaqsdZ0LTvaltagS536RP8TzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویر شهدای مدرسه میناب در دستان پزشکیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/akhbarefori/692363" target="_blank">📅 18:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692362">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a556e0468.mp4?token=RsFHptX1jY_TeEMfxVXHYjhAeKEdLXz1gFP70uFieQeDoU3MGgDKBYPOkBKLdNW_n159_I_G5yAun_8lRBEKuHl_WqA1gnPJrRW-tqhP45u71rAqEg9IIfv5_YyXLRm7bQDaCneQYoxs7UB2lT80ZuwHE2OI6B4Qnv-As3kMLZJu6jjkN6ZKxYaOPmTrUdg5bLq3olf4mC-2Shpk31a2SoizmGDS_Py6jKPL_Rx682c9SF6mKxvaeCQp7xXbprN4yL5T8aXyzusTIGfLrwMu3tFlbfdZvMH9GphCdUuUB5CQgkO4jk5sDw68Jg0H6qcwNHjrYhSvhX_X1913QTs78aI34LopdEa6w8t-tcAp38gQjJ2-iLytR14jUNCh4X6RRGqf_kyXPvg1OE9r7RsHJue05ucMhhdPB6HakA_av2ANPRhEnCNrsix-oHwebCHl8kDZEC7s3hs2_3Ex9eE_0q2u_5-Lolp4CzpEvKNTeDdng923cWtE3fuqupHRmdan0xXwGHNc7PpN3bR1xJ2kWUv4OLZVV5BU6hSirTEh7WQd-8GHxZ95bK5bvnEJ43CkknfXu7GVs063gpF1gSkUE7M_GG7Y1vt752_4OzYY0qchvHB44o4G9Ot_57x3dtgunKvZMTbcIl_T1vK71F8g7H6A1xaQ-skwnd0lDvDP3pE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a556e0468.mp4?token=RsFHptX1jY_TeEMfxVXHYjhAeKEdLXz1gFP70uFieQeDoU3MGgDKBYPOkBKLdNW_n159_I_G5yAun_8lRBEKuHl_WqA1gnPJrRW-tqhP45u71rAqEg9IIfv5_YyXLRm7bQDaCneQYoxs7UB2lT80ZuwHE2OI6B4Qnv-As3kMLZJu6jjkN6ZKxYaOPmTrUdg5bLq3olf4mC-2Shpk31a2SoizmGDS_Py6jKPL_Rx682c9SF6mKxvaeCQp7xXbprN4yL5T8aXyzusTIGfLrwMu3tFlbfdZvMH9GphCdUuUB5CQgkO4jk5sDw68Jg0H6qcwNHjrYhSvhX_X1913QTs78aI34LopdEa6w8t-tcAp38gQjJ2-iLytR14jUNCh4X6RRGqf_kyXPvg1OE9r7RsHJue05ucMhhdPB6HakA_av2ANPRhEnCNrsix-oHwebCHl8kDZEC7s3hs2_3Ex9eE_0q2u_5-Lolp4CzpEvKNTeDdng923cWtE3fuqupHRmdan0xXwGHNc7PpN3bR1xJ2kWUv4OLZVV5BU6hSirTEh7WQd-8GHxZ95bK5bvnEJ43CkknfXu7GVs063gpF1gSkUE7M_GG7Y1vt752_4OzYY0qchvHB44o4G9Ot_57x3dtgunKvZMTbcIl_T1vK71F8g7H6A1xaQ-skwnd0lDvDP3pE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
نامی که یاشار سلطانی تعمدا سانسور کرد!
🔹
احسان حسینی: یاشار سلطانی تعمدا نامی از حسین آقایاری تراستی ابربدهکار نمی‌آورد که در کودتای تراستی‌ها در سال گذشته نقشی کلیدی داشت و منجر به حوادث دی ماه شد.
🔹
سال قبل ۱۲ الی ۱۳ میلیارد دلار از ارز نفتی را همین شبکه تراستی به کشور برنگرداندند و زمینه‌ساز حمله آمریکا به ایران شدند. چرا نام ۴ نفر دیگر به جای حسین آقایاری بولد می‌شود.
🌐
مصاحبه کامل را در
یوتیوب
و
آپارات
خط انرژی ببینید.
@khate_energy</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/692362" target="_blank">📅 18:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692361">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/478c35574b.mp4?token=h_AVsutiWdWReNS08ugwb81mkMXpRqwlZCcHPnRDfx0M28o2_BU91Qm7BwTrO4BekFmZxT2WAinWrfwhs240scpS5QXBG3-6M57UfvDItM649OHSXHi6lX3OOD_Js_n4q-tCLgosVJAcHBnTHKZJ2f4Wt8_lfRodUo5aSSYKW1fforNg4eFoMfbR05NUuQrHUXipsIRuWLDe3HSndEV3M1a8YCdFwFV-vSiVnuRH2gc2WauuWDB58U1ZIrTwt2FiRCMjugk9MriDTwsy50Ut8Vrk08CmNmRxDDDdGY-Xhpy1VYIyL5-Rt-nf-b7jseNY4fmq_l-rAYzNtG-MYfxZJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/478c35574b.mp4?token=h_AVsutiWdWReNS08ugwb81mkMXpRqwlZCcHPnRDfx0M28o2_BU91Qm7BwTrO4BekFmZxT2WAinWrfwhs240scpS5QXBG3-6M57UfvDItM649OHSXHi6lX3OOD_Js_n4q-tCLgosVJAcHBnTHKZJ2f4Wt8_lfRodUo5aSSYKW1fforNg4eFoMfbR05NUuQrHUXipsIRuWLDe3HSndEV3M1a8YCdFwFV-vSiVnuRH2gc2WauuWDB58U1ZIrTwt2FiRCMjugk9MriDTwsy50Ut8Vrk08CmNmRxDDDdGY-Xhpy1VYIyL5-Rt-nf-b7jseNY4fmq_l-rAYzNtG-MYfxZJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین دوره آموزشی نظامی یگان‌های مردمی جانفدا آغاز شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/692361" target="_blank">📅 18:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692360">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
بازار سیاه فروش کد ملی برای ثبت نام خودرو / قیمت ۲۵ میلیون تومان ناقابل!
🔹
انتشار آگهی‌های فروش کد ملی برای ثبت‌نام خودرو در فضای مجازی خبرساز شده و برخی افراد برای واگذاری کد ملی خود تا ۲۵ میلیون تومان مطالبه می‌کنند؛ پدیده‌ای که پیش‌تر در ثبت‌نام خودروهای وارداتی نیز گزارش شده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/692360" target="_blank">📅 18:18 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692359">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
پزشکیان: صلحی که برای همه نباشد صلح نیست؛ سخنان دیروز رئیس‌جمهور آمریکا نشانۀ بارز خوی قُلدری است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/692359" target="_blank">📅 18:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692358">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a83689d89.mp4?token=MjMA6CoKfxuMKCx4JSnksY9ZMz83zX3-F6wSljPbj6ZMzDWnX-kSMauw_JW9hKPlCIO7BLruYYvTkkyLiIzWUJGC8cDZlU9kEq_RaDeWFZRGuscs81FPpAjttgnfQLnNyC1VIfbVk6s-ljWXJN5iTh5tfVQ0jWoWQbmbSwWZmE_5beJvqfCQ0myRHQsEfdi8Nys-C9weOmGnED0za2zIl-fqBrQHD66dwOZdDbHbhcG4aYXnbTxB9F9PPvhNNG6vf0dsiX1yTtrXNBq5tK9sFILt_QEFUxVGOLocsUpS4-jOf4Uog457K8_lB9pwz7N-Ob90IvIXysJrA3uhq2PmOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a83689d89.mp4?token=MjMA6CoKfxuMKCx4JSnksY9ZMz83zX3-F6wSljPbj6ZMzDWnX-kSMauw_JW9hKPlCIO7BLruYYvTkkyLiIzWUJGC8cDZlU9kEq_RaDeWFZRGuscs81FPpAjttgnfQLnNyC1VIfbVk6s-ljWXJN5iTh5tfVQ0jWoWQbmbSwWZmE_5beJvqfCQ0myRHQsEfdi8Nys-C9weOmGnED0za2zIl-fqBrQHD66dwOZdDbHbhcG4aYXnbTxB9F9PPvhNNG6vf0dsiX1yTtrXNBq5tK9sFILt_QEFUxVGOLocsUpS4-jOf4Uog457K8_lB9pwz7N-Ob90IvIXysJrA3uhq2PmOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: ترامپ باید بداند که مقاومت مردم ایران در برابر تحریم‌ها، فشارهای بیشتر و رفتارهای زورگویانه، تنها افزایش خواهد یافت
🔹
ما هرگز سر خم نخواهیم کرد و تسلیم نخواهیم شد.
🔹
ایران باید توسط آقای ترامپ و کسانی که به دنبال تحمیل خواسته‌های خود به ما هستند،…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/692358" target="_blank">📅 18:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692357">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
پزشکیان:  ایران خواهان تعامل، همکاری و مشارکت با جهان است و این رویکرد را نه از موضع ضعف، بلکه بر پایه اعتماد به توانایی‌های خود می‌داند. او تأکید کرد که امنیت منطقه تنها از طریق همکاری مشترک میان کشورها امکان‌پذیر است و ناامنی نیز می‌تواند همه را تحت تأثیر…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/692357" target="_blank">📅 18:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692356">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f1e98216e.mp4?token=DnzkPFQ81ibZpdYY42M6MPod3LEX9bwF-tW8FrojB9J3b6lH9RfLJKBw7fxJ2eePlTzq5FqfSHpVM7zEXYa-y-1WYbCRQZ6I8yaoqILtbvejDg3NpEjZz1vxrhCkjRwjO_UvHGSt0Vs_hO_Rwn1P8pqRrT4F9sPHLsxDbfhggV7siodrLTt57gouSx0o9Kbg03S8upNkcXx0LzO7rua-lMKlyE4wY0GOVbQv5SSH4jDFAoFxqOUnE73-GQ38VlWSUrI5e6SnnHoyMlb63vvFkchkFkjB9ksy6vLH1lixoe4Ek5GZgverDgNpXtrPJZySozWmIYtzPv-_lJBR3WC0n4qfARdmWJdUz_5xVmouEJiL4FRr2sY_dooMLIn2yH9cYdBr4H-LAGcdaBBQg69bNR0sLwbC7_10WlnaXHWjJF6PouBuLcIjQVoqSYjgdcVXjcDX_Rkfl5QrCOBkvpxCFKDQo1NrZNonT9yS-mtnAv-LAsaARqF2yMyOJK54o69wtns6q0CIZ1pY-jDkH5U7o79NdS_v99h19PGCZa-wgwtrd3_OIHyvp4iR5Ymy_q6u6iPBVJ6PlWWxQM-P5V4umDOi4wzzYrjp1ndSwTGEkrJrgFrmdH2h6p6JK3rVcBm3wE7yuq5cUplupsiSFbdeHto-JQwjBh8SP5szQ-1rWTM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f1e98216e.mp4?token=DnzkPFQ81ibZpdYY42M6MPod3LEX9bwF-tW8FrojB9J3b6lH9RfLJKBw7fxJ2eePlTzq5FqfSHpVM7zEXYa-y-1WYbCRQZ6I8yaoqILtbvejDg3NpEjZz1vxrhCkjRwjO_UvHGSt0Vs_hO_Rwn1P8pqRrT4F9sPHLsxDbfhggV7siodrLTt57gouSx0o9Kbg03S8upNkcXx0LzO7rua-lMKlyE4wY0GOVbQv5SSH4jDFAoFxqOUnE73-GQ38VlWSUrI5e6SnnHoyMlb63vvFkchkFkjB9ksy6vLH1lixoe4Ek5GZgverDgNpXtrPJZySozWmIYtzPv-_lJBR3WC0n4qfARdmWJdUz_5xVmouEJiL4FRr2sY_dooMLIn2yH9cYdBr4H-LAGcdaBBQg69bNR0sLwbC7_10WlnaXHWjJF6PouBuLcIjQVoqSYjgdcVXjcDX_Rkfl5QrCOBkvpxCFKDQo1NrZNonT9yS-mtnAv-LAsaARqF2yMyOJK54o69wtns6q0CIZ1pY-jDkH5U7o79NdS_v99h19PGCZa-wgwtrd3_OIHyvp4iR5Ymy_q6u6iPBVJ6PlWWxQM-P5V4umDOi4wzzYrjp1ndSwTGEkrJrgFrmdH2h6p6JK3rVcBm3wE7yuq5cUplupsiSFbdeHto-JQwjBh8SP5szQ-1rWTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان:  ایران خواهان تعامل، همکاری و مشارکت با جهان است و این رویکرد را نه از موضع ضعف، بلکه بر پایه اعتماد به توانایی‌های خود می‌داند. او تأکید کرد که امنیت منطقه تنها از طریق همکاری مشترک میان کشورها امکان‌پذیر است و ناامنی نیز می‌تواند همه را تحت تأثیر قرار دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/692356" target="_blank">📅 18:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692355">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
روبیو، وزیرخارجه امریکا: توافق با ایران نیاز به بازه زمانی طولانی دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/692355" target="_blank">📅 18:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692354">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
تصویری از هیئت ایرانی حاضر در سالن سخنرانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/692354" target="_blank">📅 18:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692353">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGI3AzyS6lA5XdFl0uzpzAJMhGZtYnp32y6xavCA8R76I9BsYc97Vr4_Xcr6PHUNXvYtiwqYwy7_-6z4kbWQ65htEavueNO4ZQCN5l0QOo8mg7_1OWnE2DwsgtCem9PwZ1iQT57XqtuKGyZZ4FFwUl2UdYCo4Yz0PyJmIltQSjreVdIRjSz0qJnjkjYNLJFP6ic-vIidNfZ8Z2p761KLw4jkFaPsNlpRNRCSXe55bqoCTKPxkkeSEjg2jKrtrLq8y_ZsMwfXlh-uVpVbjMIk3HFZqqv24w9a4gVqaxmKv1c7qQHH8rdaAgKgYiNg-XQ9XZw9xmry2UYhqTOsLDrfAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: ایران هرگز، مطلقاً هرگز، آغازگر جنگ نبوده است، هرگز جنگی را شروع نکرده و همواره تعهد خود را به میز مذاکره نشان داده است
🔹
آنها جنگ را به ما تحمیل کردند، اما ما ثابت کردیم که از جنگیدن نمی‌ترسیم – جنگی که ماهیتی دفاعی دارد – و ما تا آخرین نفس در…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/692353" target="_blank">📅 18:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692352">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
پزشکیان: دهه هاست قطع نامه ها صادر می شود اما اشغال و خشونت ادامه دارد
🔹
اگر انسانی را با بمب و ویرانی از خانه کاشانه اش بیرون کنند حتما مقاومت خواهد کرد
🔹
مسایل منطقه ما در خود منطقه و توسط کشورهای منطقه باید حل و فصل شود
🔹
اکنون سخنی با همه کسانی که مسوول…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/692352" target="_blank">📅 18:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692351">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9788505185.mp4?token=PmIF5R7yiUX8fZ-H1eNH9Mx4QOZNd0UxumOYYHpz4qG6WB_Bh4WB6P-JA3unj60y3WM2OhmAD6OvsMgpt5WtgxggHYRCKRbqUuY__vxz41bZ-LgTrKp9tVDgjqJxgElupp2zv5gdlW0W-QD8_l6B1ofCGRpismTQOefNDzi_6L7za4IE9_TZZ3ifZVbhCS2GMnGvDRCNRak5yqfs-e9Onwx-igN_8p_23GpsWM5gvjC1oyz_pVxnL_gwHjmcBA0nPo65lqz6WL0hN_J2tyGFI4UaeRgMmctrxfKf-mwCTZvp9zBS3bMeQJuFu2VsTfWlsJIZcIjjHunat-QAD2uRrQSWTjJT3A5E6PMEI3Xgg1DZretLMZBRsTVq1LpzHYwJL5coWsfB9PE3vue2_nsEpV5tz9wXaFZ_b2aHttshDEVD7nmqafK0pDK_I3UY3WIjtTR53MUXj9duefOXzRdd6LSd4SdxhncvhgEHiD9kiUrlDbA253PdtNYULakvAwf2uWVQaPOhchVecLWXFiUqCtbeguZvnHqUvaN1NZnHnlAku_Ksx_HAglTIrAlDBugptirT6I25b4IVT1pfdZNBhwkCN_AFAGaEyhbuZKeA5VTPtlH3x42tQt7XDPmlStHPyz7lo8O_xi0-kHZOnBMmkoxHa1XTm5VXzB3466zPMlY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9788505185.mp4?token=PmIF5R7yiUX8fZ-H1eNH9Mx4QOZNd0UxumOYYHpz4qG6WB_Bh4WB6P-JA3unj60y3WM2OhmAD6OvsMgpt5WtgxggHYRCKRbqUuY__vxz41bZ-LgTrKp9tVDgjqJxgElupp2zv5gdlW0W-QD8_l6B1ofCGRpismTQOefNDzi_6L7za4IE9_TZZ3ifZVbhCS2GMnGvDRCNRak5yqfs-e9Onwx-igN_8p_23GpsWM5gvjC1oyz_pVxnL_gwHjmcBA0nPo65lqz6WL0hN_J2tyGFI4UaeRgMmctrxfKf-mwCTZvp9zBS3bMeQJuFu2VsTfWlsJIZcIjjHunat-QAD2uRrQSWTjJT3A5E6PMEI3Xgg1DZretLMZBRsTVq1LpzHYwJL5coWsfB9PE3vue2_nsEpV5tz9wXaFZ_b2aHttshDEVD7nmqafK0pDK_I3UY3WIjtTR53MUXj9duefOXzRdd6LSd4SdxhncvhgEHiD9kiUrlDbA253PdtNYULakvAwf2uWVQaPOhchVecLWXFiUqCtbeguZvnHqUvaN1NZnHnlAku_Ksx_HAglTIrAlDBugptirT6I25b4IVT1pfdZNBhwkCN_AFAGaEyhbuZKeA5VTPtlH3x42tQt7XDPmlStHPyz7lo8O_xi0-kHZOnBMmkoxHa1XTm5VXzB3466zPMlY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس جمهور ایران: ایران، کشورهای همسایه را به عنوان رقبای امنیتی نمی‌بیند. ما خواهان داشتن همسایگان قدرتمند هستیم.
🔹
در آب‌های تنگه هرمز، ما نمی‌خواهیم ناامنی ایجاد کنیم. ما نمی‌توانیم اجازه دهیم که برخی افراد به طور آزادانه به این آبراه دسترسی داشته باشند…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/692351" target="_blank">📅 18:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692350">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‼️
رئیس جمهور ایران: ایران، کشورهای همسایه را به عنوان رقبای امنیتی نمی‌بیند. ما خواهان داشتن همسایگان قدرتمند هستیم.
🔹
در آب‌های تنگه هرمز، ما نمی‌خواهیم ناامنی ایجاد کنیم. ما نمی‌توانیم اجازه دهیم که برخی افراد به طور آزادانه به این آبراه دسترسی داشته باشند…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/692350" target="_blank">📅 18:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692349">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
پزشکیان: ایران را نمی توان با جنگ وادار به تسلیم کرد  ما ثابت کردیم که برای دفاع از خود از جنگ نمی ترسیم تا پای جان برای دفاع از ایران عزیز ایستاده ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/692349" target="_blank">📅 17:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692348">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
پزشکیان: ایران را نمی توان با جنگ وادار به تسلیم کرد  ما ثابت کردیم که برای دفاع از خود از جنگ نمی ترسیم تا پای جان برای دفاع از ایران عزیز ایستاده ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/692348" target="_blank">📅 17:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692347">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
پزشکیان: ما نمی‌توانیم بگذاریم همه از تنگۀ هرمز بهره ببرند اما ایران از آن محروم باشد
🔹
راه را بر ایران می‌بندند و سپس از تنگه اسلحه و مهمات و موشک برای نابودی کشورها از تنگه منتقل می‌کنند؛ این امکان‌پذیر نیست و ما اجازه‌اش را نخواهیم داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/692347" target="_blank">📅 17:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692346">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
پزشکیان:اسرائیل می‌کشد، ایران تحریم می‌شود، به هرکس بگویید خنده‌اش می‌گیرد
🔹
صلح در غرب آسیا بدون توجه به صلح در فلسطین اتفاق نمی افتد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/692346" target="_blank">📅 17:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692345">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
پزشکیان: از جنگ نمی‌ترسیم و برای صلح از مذاکره نمی‌گریزیم
🔹
کنایه رئیس جمهور به آژانس بین اللمللی انرژی اتمی: بمب اتم در اسرائیل است و بازرسان در ایران!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/692345" target="_blank">📅 17:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692344">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
پزشکیان: اسرائیل به هر کشوری که دلش می‌خواهد حمله می‌کند
🔹
عاملان ناآرامی اسرائیل و آمریکا هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/692344" target="_blank">📅 17:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692343">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
رئیس جمهور: نه سلاح هسته ای، نه صرف نظر از دانش هسته ای
🔹
پزشکیان: تسلیم نمی شویم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/692343" target="_blank">📅 17:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692342">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3573a2cefc.mp4?token=kXgRnfkWB9duo7U7jv4EPHOcp3_w1tkruTeOAXi94gWIiQ9CofCX09_C0REmfZ7EUDTYHdtnrqvOGNOksR8UTVdKm7szbwbmPRT1k-ryn0bOuVueJshQ-ApEMeJC6X_3vzRCN-4PFCzMpR0D8tfczyIXHaW_89BJM7Lv8lXDJ-GS0yxt0d9Z4lccqy7V2Qq_Nldjr-oQ-J-83t84soAFqWkiybHc3-5jUkt7uBYCh9CduXgxV68ZRmgCArnYNwHTNOxr9sYj-Of3sKBDB29hopfyl4uc52iikV-TGy29VNRlxw3ec-zaF6LdTTC-q72qr58p41mtJzzGM3xIEMt-UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3573a2cefc.mp4?token=kXgRnfkWB9duo7U7jv4EPHOcp3_w1tkruTeOAXi94gWIiQ9CofCX09_C0REmfZ7EUDTYHdtnrqvOGNOksR8UTVdKm7szbwbmPRT1k-ryn0bOuVueJshQ-ApEMeJC6X_3vzRCN-4PFCzMpR0D8tfczyIXHaW_89BJM7Lv8lXDJ-GS0yxt0d9Z4lccqy7V2Qq_Nldjr-oQ-J-83t84soAFqWkiybHc3-5jUkt7uBYCh9CduXgxV68ZRmgCArnYNwHTNOxr9sYj-Of3sKBDB29hopfyl4uc52iikV-TGy29VNRlxw3ec-zaF6LdTTC-q72qr58p41mtJzzGM3xIEMt-UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: برای کشور ما انرژی هسته ای برای بیماران ما درمان و برای کشاورزان ما اهمیت دارد و برای آینده برقی پایدار است
🔹
در منطقه ای زندگی میکنیم که جنگ مرز نمیشناسد/ ما همسایگان خود را قوی میخواهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/692342" target="_blank">📅 17:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692341">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb9890865e.mp4?token=DOnn9CBbWXCsbuSaaDV33lNrjfX8OBIv5gdsYfkjtck3XdDm3A4l1QwIZoTqbUr59Sdzg4T-SkKPiGmRxtrFb_udwW1_RrOIrvvVSR5Rq1M3perbNlI9xQYKLW3HoGq9w-iJhrktyAMRBhjE7mtEo2f324e8ZKzC5sigFkcBdE4Xal3Ozpe58NjJyZyVdqcy0K9GuFKdQV5vDOKHBLtJWctDJCMIiGF1ePYJuEpa0IHpCidsBYgQLyaMKcvyJLQh1VVriCC-mBKnENXTV7SXx2rGu9KXHkwk7MEEicjYWHNXVNK7oEQULL2y_f7nASMgtyZCpnaeIyxpZJxhFcqEWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb9890865e.mp4?token=DOnn9CBbWXCsbuSaaDV33lNrjfX8OBIv5gdsYfkjtck3XdDm3A4l1QwIZoTqbUr59Sdzg4T-SkKPiGmRxtrFb_udwW1_RrOIrvvVSR5Rq1M3perbNlI9xQYKLW3HoGq9w-iJhrktyAMRBhjE7mtEo2f324e8ZKzC5sigFkcBdE4Xal3Ozpe58NjJyZyVdqcy0K9GuFKdQV5vDOKHBLtJWctDJCMIiGF1ePYJuEpa0IHpCidsBYgQLyaMKcvyJLQh1VVriCC-mBKnENXTV7SXx2rGu9KXHkwk7MEEicjYWHNXVNK7oEQULL2y_f7nASMgtyZCpnaeIyxpZJxhFcqEWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: ما سامانه دفاعی‌مان را برای آن ساختیم که هیچ کس تصور نکند بمباران شهرهای ایران بی پاسخ خواهد ماند
🔹
ما برای دفاع از کشورمان از کسی اجازه نمی گیریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/692341" target="_blank">📅 17:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692340">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
پزشکیان: ما سامانه دفاعی‌مان را برای آن ساختیم که هیچ کس تصور نکند بمباران شهرهای ایران بی پاسخ خواهد ماند
🔹
ما برای دفاع از کشورمان از کسی اجازه نمی گیریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/692340" target="_blank">📅 17:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692339">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
پزشکیان: ما چیزی نمی خواهیم ما پاسخ خود را یافته ایم و می دانیم قدرت نیاز داریم زیرا ملتی که قدرت نداشته باشد آن را له می کنند
🔹
۲۰۰ سال است به هیچ کشوری حمله نکرده ایم و همیشه از خود دفاع کرده ایم و امروز ما را عامل تروریست می نامند
🔹
این باعث شده است که…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/692339" target="_blank">📅 17:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692338">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
پزشکیان: قدرت می‌خواهیم که از خودمان دفاع کنیم
🔹
ما انرژی را برای توسعه می خواهیم نه برای تهدید جامعه و برای امنیت می خواهیم مشارکت کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/692338" target="_blank">📅 17:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692337">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
پزشکیان در مجمع عمومی سازمان ملل: آمریکا و اسرائیل مدرسه میناب و لامرد را با بمب خوشه ای هدف قرار دادند و کودکان و مردم بیگناه را به شهادت رساندند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/692337" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692336">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fed67b0e0e.mp4?token=Lv7WFGrDt9L8dIgFPcoajcmuYmrZ2VbslMJOWv8ro8Kh8oL35jtJHBMVWkHdEtTbdPwvZ11dY3RZ42WRrldK_0P8lDQR_FlxBetUrNpTCmUZFycZZfPyhPH-10iUN7h4JnYDqaqmht3-WhSRvgvipMuG4eod4ZxT9CvJTCPvdfyQW0ZOSO5K7FuSZwtv1UaulLVfi2fpToSbz0YiPX0Ym64FOndsHS6C5J2QhJ_Xg6lh8aQVehKDUSnd0vvrKJcYbZgNMq4rmNG7bbr5iV79r7DczsLLBbRHCs-TeUNUfJg6PBtHjhJvzy4FNpUSsClMDerPljMrWq9pQc9haCQPiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fed67b0e0e.mp4?token=Lv7WFGrDt9L8dIgFPcoajcmuYmrZ2VbslMJOWv8ro8Kh8oL35jtJHBMVWkHdEtTbdPwvZ11dY3RZ42WRrldK_0P8lDQR_FlxBetUrNpTCmUZFycZZfPyhPH-10iUN7h4JnYDqaqmht3-WhSRvgvipMuG4eod4ZxT9CvJTCPvdfyQW0ZOSO5K7FuSZwtv1UaulLVfi2fpToSbz0YiPX0Ym64FOndsHS6C5J2QhJ_Xg6lh8aQVehKDUSnd0vvrKJcYbZgNMq4rmNG7bbr5iV79r7DczsLLBbRHCs-TeUNUfJg6PBtHjhJvzy4FNpUSsClMDerPljMrWq9pQc9haCQPiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی میدان امام حسین برای شروع اولین افتتاحیه آموزش نظامی یگان‌های مردمی جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/692336" target="_blank">📅 17:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692335">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
تصویر شهدای مدرسه میناب در دستان پزشکیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/692335" target="_blank">📅 17:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692334">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihtjyoNJb2hfJEc4xFoFkVGuFLfA8G2ogCfgnovs4ql-G_HW3SJ7rbMbbV5j5mgtg5StcWFFkNNroAg3rRxqDcST5UuGS-7GDGatG7A7-uVy-je6RerKKNEDtvj5YPK0mYst2uIoveGq_O92HPCfxYI5vFkh3FtKFqji0uxWEdAbxHqqYAWqGV40IZpVQhJyILeIqTddJd3p7KYNrxmMxzMTIz0Asnv--l6fbjfbKPpl9JbKvIRrFWvmJnvo4k3hGToK0J-ZrIIOJ5BNhNlhVBll1xhBCx63lMEpBJrmXt6BRicQCtin9tBqxmnmW0NxWZEUxcZGdFFX2Fc4A4iySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشان دادن تصویر رهبر شهید انقلاب توسط رئیس جمهور
🇮🇷
✊
@AkhbareFori |</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/692334" target="_blank">📅 17:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692333">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c84e1a267.mp4?token=rSVw5PNV4uu0752Os3VYGR1-PXGVD1MR5O2yOUfVcPkHrjATCsEd58gDQ86WPKULh_LTiGiLFg_aW5J1Qynvt5OSeG-NU1UMzadpHiXC8MenwU7jWvw2VkRjeuxat1-6MIh4gAymyowJf2xl-FBlutuwtfXwLD9u6GXfZC5zfFzAXkXmF7j_kZDfIiSUWVFe-3e_0w7Kx5nCq4jFgpgPIhOsNWQDUbrhN5XdfoQ2dtA-qz2lIw67f5I5wdAp-Qrs_S_kGXb_YIPFdF2Y8zlFiUc_ddoMOYgeDv4UQpVrB0n7EDLiEzXW0lzzqyzbadVQFiQ9EujeZiwl80325l1TIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c84e1a267.mp4?token=rSVw5PNV4uu0752Os3VYGR1-PXGVD1MR5O2yOUfVcPkHrjATCsEd58gDQ86WPKULh_LTiGiLFg_aW5J1Qynvt5OSeG-NU1UMzadpHiXC8MenwU7jWvw2VkRjeuxat1-6MIh4gAymyowJf2xl-FBlutuwtfXwLD9u6GXfZC5zfFzAXkXmF7j_kZDfIiSUWVFe-3e_0w7Kx5nCq4jFgpgPIhOsNWQDUbrhN5XdfoQ2dtA-qz2lIw67f5I5wdAp-Qrs_S_kGXb_YIPFdF2Y8zlFiUc_ddoMOYgeDv4UQpVrB0n7EDLiEzXW0lzzqyzbadVQFiQ9EujeZiwl80325l1TIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان در سازمان ملل: ما تروریست نیستیم، ما قربانی تروریست هستیم
🔹
من از ایرانی می‌آیم که رهبر ما را بدون هیچ دلیل و برهان و قانونی ترور کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/692333" target="_blank">📅 17:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692332">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10de3f1271.mp4?token=UdqujzZqvA-2H9c2SCm2C6z2RFwkg5oP__lBCHpPjiPa878_DjzKyu1Z26UqfsTxK-aNXo370wSJ-HCSckyR76igBPbjTyVzFvylHzpJw6ZCkS39zEhd5zQ9ECC5-k7WIiHusdLjdUthyMoj3AXoP3waGfnsBPGHTYcVFDF-fJb7YfziPMYtSEWhIudklg1rTMhULCVIZ0cfLieFa7PIhfKnWZG3ItKRLkyDBlqOOODVJVZuVRjIyx0n-La2IUxsTUrvlk1mNuUA7-zCzyD2knd12uPnglUIYly5hP1JxPjp8x_d8eQProP_EbYjwXwaPnTQMIWX1tIMmQm26orfcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10de3f1271.mp4?token=UdqujzZqvA-2H9c2SCm2C6z2RFwkg5oP__lBCHpPjiPa878_DjzKyu1Z26UqfsTxK-aNXo370wSJ-HCSckyR76igBPbjTyVzFvylHzpJw6ZCkS39zEhd5zQ9ECC5-k7WIiHusdLjdUthyMoj3AXoP3waGfnsBPGHTYcVFDF-fJb7YfziPMYtSEWhIudklg1rTMhULCVIZ0cfLieFa7PIhfKnWZG3ItKRLkyDBlqOOODVJVZuVRjIyx0n-La2IUxsTUrvlk1mNuUA7-zCzyD2knd12uPnglUIYly5hP1JxPjp8x_d8eQProP_EbYjwXwaPnTQMIWX1tIMmQm26orfcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان در سازمان ملل: ما تروریست نیستیم، ما قربانی تروریست هستیم
🔹
من از ایرانی می‌آیم که رهبر ما را بدون هیچ دلیل و برهان و قانونی ترور کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/692332" target="_blank">📅 17:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692331">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
منابع عربی مدعی فعال شدن پدافند هوایی در شهر جازان در جنوب عربستان شدند
/ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/692331" target="_blank">📅 17:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692329">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGxJqutPy3wVA67dstMUnr08uXnTITG9fO5m0OgieDPTkp9Vd1cr_I1J0vKqIReBCurksdvjNiHewnO7PgxVVK0pyxoV8QUsDdDE9_lhquh2jIvy7TV4NJdXbXR5ts0z8hWaykeYf4cHvyDVT8L581XeOoAvGjQ6ozzLoKIyGv0Uwlaw5gUKt7g-POEHUfWw8ZawWVMsx9kHTcRu-psmQbr_XFncYLb1FSqp3MDE3kDV0AOpq5hkoZeoLdnUilo626ylWMTpkfFoPKgPx9wAVz2eT8HSHcBRZ4CiP3xUX3O5UreW414IBHkR3B3DMVMDgaynZ5S3sNh9f13yer9nGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tD24o_97rAl6Su23x4NCaeEn8c4FrPQ2fY-XdA82FFT6We1gBBY9B7P4zhh7a5lJEWR4YII-nnpGGARViWy0NE9KAq26gKhbNHbfzU74hJZCHXDQYw3DIUFyu2pLjyxnQh_RfXzjmGHscmfMGfvGCp6Bn6MFFQ3YU0whVvaolJmjQraJodj9-0Pm1ka2N-VVsrtWVvHE3vBpYFSglqzdoomDTRY6et82hihWxqOLVPNevpE2cT43yP0GsvxG9sJbx5EoYSynGLOKTsNoYLPvt_SMazdLLIAlAZdGUV8QEtFcKW8K9AjxgaaFtuSr3x2a85IotSBoLDmfJQesWampMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مسعود پزشکیان جهت ایراد سخنرانی وارد ساختمان سازمان ملل متحد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/692329" target="_blank">📅 17:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692328">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9cc6b849.mp4?token=HFnJCKwsvn4kkrYdfilgL-DifU6BTP_sFR0m-HJAJaSIqu--OWTQrxqBJmwJFEowZH6s8NzYWBNGUaoI_DB9yaInBEeBbCK6D-h07S76dtjGZTwNLIBm0CmRXYDNcdkWeUztMMxzVhPmw6O-xnwizqG4HB0NFQoDZgtey2W4OPzcWDv9ry9-WZWu7qzMfVmv9BuYxv9i0qj5MIcfQjFtXNZYZai7DSKOjVy1bnGQqFyndCLh038KUoJbDWAyo2LMsJ9y8O7t1s0fM6w35dap9m3LyeCpz4jg-2viTpNrBBLBC1Dcw7CLfPr1koKHgYLCz_sOrgiVWp03XvpeaBHnbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9cc6b849.mp4?token=HFnJCKwsvn4kkrYdfilgL-DifU6BTP_sFR0m-HJAJaSIqu--OWTQrxqBJmwJFEowZH6s8NzYWBNGUaoI_DB9yaInBEeBbCK6D-h07S76dtjGZTwNLIBm0CmRXYDNcdkWeUztMMxzVhPmw6O-xnwizqG4HB0NFQoDZgtey2W4OPzcWDv9ry9-WZWu7qzMfVmv9BuYxv9i0qj5MIcfQjFtXNZYZai7DSKOjVy1bnGQqFyndCLh038KUoJbDWAyo2LMsJ9y8O7t1s0fM6w35dap9m3LyeCpz4jg-2viTpNrBBLBC1Dcw7CLfPr1koKHgYLCz_sOrgiVWp03XvpeaBHnbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: ترامپ ممکن است بخواهد در کوهی در ایران کاری کند یا به سایت‌های هسته‌ای ما حمله کند ولی ما همین را هم تحمل تخواهیم کرد؛ طرح نیروهای مسلح ما برای پاسخ آماده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/692328" target="_blank">📅 17:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692326">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
نفت برنت ۱۰۰ دلاری شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/692326" target="_blank">📅 17:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692325">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/404e87b211.mp4?token=AE-xexTygnz2QPZEZI6Os_qv92G1ZYU-5eVNipiTBrLuGnsBAE-7NGZBcZTMiQQbExGCvhyDJc2xyV7UD_nqtIUVIdvD882uYYZzVlhrdpO_1jJ-VPpahhcOj9Rem27tGevvc3G77J0M16XKS9bamgztr16KsYcp3cPltQYOewGZ4-9jNJFChfVitTB2JlKcsAyTx5CbXfzyYOaU4n04e0ocLuH0KS-0BfIsUR-oGcPuWblht1lPexlbtR2GZoqZ0KtQ_odoiBeh24rKQ0tQX_LEUQ9ivzEwXg8mpiUoGH3HR8-DTis0-8_VEYAQ7d-CpbNKU6HcCEls7fwSWRmhOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/404e87b211.mp4?token=AE-xexTygnz2QPZEZI6Os_qv92G1ZYU-5eVNipiTBrLuGnsBAE-7NGZBcZTMiQQbExGCvhyDJc2xyV7UD_nqtIUVIdvD882uYYZzVlhrdpO_1jJ-VPpahhcOj9Rem27tGevvc3G77J0M16XKS9bamgztr16KsYcp3cPltQYOewGZ4-9jNJFChfVitTB2JlKcsAyTx5CbXfzyYOaU4n04e0ocLuH0KS-0BfIsUR-oGcPuWblht1lPexlbtR2GZoqZ0KtQ_odoiBeh24rKQ0tQX_LEUQ9ivzEwXg8mpiUoGH3HR8-DTis0-8_VEYAQ7d-CpbNKU6HcCEls7fwSWRmhOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
سرمایه‌گذاری را از همین امروز شروع کن!
✨
🪙
خُردخُرد پس‌اندازت را به نقره ۱۰ گرمی تبدیل کن و برای آینده‌ات سرمایه بساز
📈
💰
💎
نقره ۱۰ گرمی خاتم‌چی؛ شروعی کوچک برای یک سرمایه بزرگ
🚀
🤍
@khatamchii
@khatamchii
@khatamchii
☑
ثبت
سفارش
و
مشاوره
خرید
:
📱
09120715100
☎️
02122477938
خرید
از
وب‌سایت
:
🌐
Khatamchi.com
▪
️@khatamad</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/692325" target="_blank">📅 17:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692324">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
مسعود پزشکیان جهت ایراد سخنرانی وارد ساختمان سازمان ملل متحد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/692324" target="_blank">📅 17:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692323">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
پیام دبیر شورای‌عالی امنیت ملی به کشورهای همسایه: اگر پروازهایمان را ممنوع کنید و وارد همکاری با آمریکا شوید، فرودگاه‌هایتان پرواز نخواهد داشت
🔹
اگر کنار آمریکا باشید ما شما را تماشا نخواهیم کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/692323" target="_blank">📅 17:24 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692322">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f50039aa.mp4?token=pasXZML2yA8hR6-TIDjJhVbIoYApFnUC9-nnY5HVy5NE9w0gfuftm56sZCWqCP2LCIdT1WuKe6BGFyQARWmK4IrOY97SmTlX774FZ2gk05c5-_XPKjBbiuJU8gODM23QGtxekSt6KKFL4DFAy_5sRhnx-9XH3x3RzyhBmsIUOjxzRSNx-d_M0kkQTNbEBAUEj5ZTecWbRylru2_Sy8zbaOlOGnP1KyiUdKA8HGANcX_1DRrn7b70ycrC21KPmL4xheXez3nMrIp6DTup8xV2-2cbXnNuumWNB4We_YVnKghHzbFX4nyv-udEbk42RaBa699Ob830yMogwQHNfz0y1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f50039aa.mp4?token=pasXZML2yA8hR6-TIDjJhVbIoYApFnUC9-nnY5HVy5NE9w0gfuftm56sZCWqCP2LCIdT1WuKe6BGFyQARWmK4IrOY97SmTlX774FZ2gk05c5-_XPKjBbiuJU8gODM23QGtxekSt6KKFL4DFAy_5sRhnx-9XH3x3RzyhBmsIUOjxzRSNx-d_M0kkQTNbEBAUEj5ZTecWbRylru2_Sy8zbaOlOGnP1KyiUdKA8HGANcX_1DRrn7b70ycrC21KPmL4xheXez3nMrIp6DTup8xV2-2cbXnNuumWNB4We_YVnKghHzbFX4nyv-udEbk42RaBa699Ob830yMogwQHNfz0y1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: در دیپلماسی جدید ما اهرمی داریم به‌نام تنگۀ هرمز که تضمین مذاکرات است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/692322" target="_blank">📅 17:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692321">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7401b7d0b.mp4?token=Rn-SdVI4xA-mikF51BWV1Qb6B-WQRiH3kTzZsyJXZV33QwJsj_I2VztC3SfVRy5fAyAMYb2aWdeSnDHNeZ2Fu7ioi30GRQ5ShF6SlqIl2NUhIa75VwZ2YQVOLjrXasdZbUYDcV70FqgHf7kMMzYztdJw5czuO0aBNvBbXiHo5_f9gtzwKumoWxVOHATWPm6MFiQeKiznPc5FF3j5WwrH_T5qBmOwVANA_dl-8OEG-bdBlzcAYbs-dtjDU9iF3frOv4f1f5RTpT_h8FjOAGhdbX1KKrsK5_UC4PeVQiD2jUTgCUwDBZTBYjdHchOvAffbHHxCtGjPzHCyAJr0ocG1p0fbYmcIcer-ioEHZggLcnHHy_JhAkx23acFMinMtUyGaxCPcQqcag57bA7pKUohP0s4HledByt5wlH7QQycZoiwuejNkC0PwfVoO4wNf4FSa1uuJIPFWx8jcd80DSlm_e8RxBWLwVt-BDnC4TK4OY6ljkG1UXukgU89zglcGpmw-YpdK5ElOu3vGl8SMkxIBYQNEWz3onASbjrI6f7xhueKAR9n3JrvGQLy7lizB97b3U4X_2KMY90vPaPWPy5RYHofoBWrwmZPJDFd2Zzvr63K9jjW70hieuLmWFDEQAGl3PNBhsKaMDxCA2_l3ebGu-jzXKwiQpBdCPOqjZjJCBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7401b7d0b.mp4?token=Rn-SdVI4xA-mikF51BWV1Qb6B-WQRiH3kTzZsyJXZV33QwJsj_I2VztC3SfVRy5fAyAMYb2aWdeSnDHNeZ2Fu7ioi30GRQ5ShF6SlqIl2NUhIa75VwZ2YQVOLjrXasdZbUYDcV70FqgHf7kMMzYztdJw5czuO0aBNvBbXiHo5_f9gtzwKumoWxVOHATWPm6MFiQeKiznPc5FF3j5WwrH_T5qBmOwVANA_dl-8OEG-bdBlzcAYbs-dtjDU9iF3frOv4f1f5RTpT_h8FjOAGhdbX1KKrsK5_UC4PeVQiD2jUTgCUwDBZTBYjdHchOvAffbHHxCtGjPzHCyAJr0ocG1p0fbYmcIcer-ioEHZggLcnHHy_JhAkx23acFMinMtUyGaxCPcQqcag57bA7pKUohP0s4HledByt5wlH7QQycZoiwuejNkC0PwfVoO4wNf4FSa1uuJIPFWx8jcd80DSlm_e8RxBWLwVt-BDnC4TK4OY6ljkG1UXukgU89zglcGpmw-YpdK5ElOu3vGl8SMkxIBYQNEWz3onASbjrI6f7xhueKAR9n3JrvGQLy7lizB97b3U4X_2KMY90vPaPWPy5RYHofoBWrwmZPJDFd2Zzvr63K9jjW70hieuLmWFDEQAGl3PNBhsKaMDxCA2_l3ebGu-jzXKwiQpBdCPOqjZjJCBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رشیدی‌کوچی، نماینده سابق مجلس: بنزین را گران کنیم، قاچاق متوقف نمی‌شود/ مشکل از اصلاح نشدن مسیر است، نه فقط قیمت
جلال رشیدی کوچی، نماینده سابق مجلس:
🔹
چه کسی گفته که بنزین در کشور ما مفت است؟ اتفاقا پول بنزین را به قیمت روز و لیتری یک دلار می گیریم.
🔹
جبهه پایداری با پزشکیان نیست.
🔹
مگر می‌شود زور رییس جمهور به گرانی بنزین و فیلترینگ نرسد؟
🔹
من اگر جای آقای همتی بودم که نماینده‌ها اینقدر فشار بیاورند تا آخرین لحظه روی صندلی نمی‌‌نشستم که با استیضاح مرا بردارند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/692321" target="_blank">📅 17:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692320">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
سرلشکر رضایی: تا قبل از بازشدن تنگه هرمز هفت شرط ایران باید عملی شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/692320" target="_blank">📅 17:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692319">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
رونمایی رسمی از برند «ضرابخانه» در نمایشگاه طلا و جواهر اصفهان
🔹
برند تخصصی تولید شمش طلا و نقره «ضرابخانه» با حضور فعالان صنعت طلا و اعضای اتحادیه‌های طلای تهران و استان‌های کشور رسماً وارد بازار شد.
🔹
تولید شمش‌های ۲۴ عیار از ۵۰۰ سوت تا یک کیلوگرم
🔹
تضمین وزن و عیار بدون تلورانس
🔹
بسته‌بندی امنیتی ۸ لایه ضدجعل
🔹
مجهز به هولوگرام، چاپ امنیتی، حکاکی لیزری، OVI، جوهر نامرئی و تراشه NFC
🔹
امکان استعلام وزن، عیار، سریال و اصالت شمش از طریق NFC
🔹
ثبت سفارش آنلاین و تحویل درب منزل در حدود ۲۷۰۰ نقطه کشور
🔹
سهراب سجادپور، مدیرعامل ضرابخانه، در گفت‌وگو با خبرفوری اعلام کرد که این برند با تجهیز خط تولید خود با به‌روزترین دستگاه‌های دنیا تلاش کرده است که استاندارد تولید شمش طلاونقره را در اندازه بهترین برندهای جهانی ارتقا دهد و محصولی قابل اعتماد در اختیار مصرف‌کننده قرار دهد.
مشروح خبر
khabarfoori.com/fa/tiny/news-3247439
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/692319" target="_blank">📅 17:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692318">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
سرلشکر رضایی: به وضع اسلام آباد و قبل از آن بر نمی گردیم؛ آمریکا را وادار می کنیم اعتماد ملت ایران را جلب کند
🔹
اگر آمریکا به هفت شرط ایران عمل نکند نه تنگه هرمز باز می شود نه مذاکره می کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/692318" target="_blank">📅 17:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692317">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: داریم زیردریایی آمریکا را مهندسی معکوس می‌کنیم
🔹
این زیردریایی تا ۶ هزار متر در اقیانوس تجسس انجام می‌دهد و فوق‌العاده ارزشمند است.
🔹
شاید برخی کشورها در آینده به ما بگویند فناوری آن را به ما بدهید و در قبال آن چند میلیارد دلار…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/692317" target="_blank">📅 17:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692316">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLelOFk-Uqsv7uDb91Sl5zsUxTfBqcVSyvCjboP3HLOGb8i0NhrZnkvtIS_CPxbrIeBQk0OF3glTqkON7ysE7dY-VjUFzsBeQr4KqDp4SKndIopEGml9lWRd_9v175TUaarQn_rlY4QsTQVk8bkyp9AsDU399A_8MufjEhrZyuRytkKOwqZlBA6L1Pj_wIWdQachmGjvMpNa5d1dr1A0mEUa4mDtUoyvEcsShP2SBBNmbQzzJ9MoYWffJw9Df2uxH2Otdz_GZFJ_kVvNB7xBVRP2YxVQI0Jh1tdml-X9fLt7P0QcgwiAJESeofpSFZpKAMbA6hOCs6F_Ll2BjnhBYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار با مجوز یا بدون مجوز صرفا مسئله این نیست!
🔹
دیدار عراقچی وزیر امور خارجه کشورمان با استیو ویتکاف نماینده آمریکا در حاشیه نشست مجمع عمومی سازمان ملل بار دیگر موضوع نحوه مواجهه دستگاه دیلماسی و حدود اختیارات تیم مذاکره‌کننده کشور را در کانون توجه قرار داده است.
🔹
تا این لحظه اطلاعات روشنی درباره اینکه این دیدار با چه سطحی از هماهنگی و مجوز در داخل کشور انجام شده منتشر نشده است پس طبعا نمی‌توان درباره داشتن یا نداشتن مجوز این دیدار اظهارنظر قطعی کرد.
🔹
با این حال با توجه به جایگاه عراقچی و سابقه او در پرونده مذاکرات این دیدار نمی‌تواند احتمالا بدون در نظر گرفتن ملاحظات سیاست خارجی جمهوری اسلامی ایران تحلیل شود.
🔹
اما فارغ از بحث مجوز این دیدار مسئله مهم‌تر محتوای احتمالی مذاکرات و چارچوبی است که این گفتگو در آن انجام شده است.
🔹
در شرایطی که اختلافات اساسی ایران و آمریکا همچنان پابرجاست، هرگونه مذاکره با طرف آمریکایی زمانی معنا پیدا می‌کند که بتواند در جهت تأمین منافع ایران و پیگیری حقوق مردم کشور مورد استفاده قرار گیرد.
🔹
در واقع در فضای فعلی مذاکره را نیز می‌توان بخشی از ابزار مواجهه با دشمن دانست، ابزاری که کارکرد آن به نحوه استفاده از آن بستگی دارد.
🔹
از این نگاه اصل گفتگو به‌تنهایی نه نشانه عقب‌نشینی است و نه می‌تواند به‌خودی‌خود دستاورد محسوب شود.
🔹
آنچه اهمیت دارد موضع طرف ایرانی، مطالبات مطرح‌شده و نتیجه‌ای است که از این روند حاصل می‌شود.
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/692316" target="_blank">📅 17:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692315">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/720177a8ad.mp4?token=mWduBxcUoUH9iXYX7QYUF5SHxbgaBd34zrSrKIzxvZxTEhZG5EW60T99wenDrmMWHvEFMedxU0JH4OC1oYWXUJ_9B5FRwsYq_u0dOHkbBVnPPkd7xzNvTG7BRa1gP7Px7M2ZxFZsC3FKAYlhENouQPQg5f3LH-Iizjv-2caLt7BIpn2amB29V5JcLhmGkkLiekdz781QO0oQTe1qRSgt6WF_JHdLgpR56OdYL_4cKAe80BcUMwWZ4WpI_kvFeiLTMzcdThtf0DMLWZ8_dVFqm6l-r_J0U1pzcsuAVW_w90CbREMYrWRnVmrrrO8WSve_vhTpGUzYCTEtbQ4lKTuNuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/720177a8ad.mp4?token=mWduBxcUoUH9iXYX7QYUF5SHxbgaBd34zrSrKIzxvZxTEhZG5EW60T99wenDrmMWHvEFMedxU0JH4OC1oYWXUJ_9B5FRwsYq_u0dOHkbBVnPPkd7xzNvTG7BRa1gP7Px7M2ZxFZsC3FKAYlhENouQPQg5f3LH-Iizjv-2caLt7BIpn2amB29V5JcLhmGkkLiekdz781QO0oQTe1qRSgt6WF_JHdLgpR56OdYL_4cKAe80BcUMwWZ4WpI_kvFeiLTMzcdThtf0DMLWZ8_dVFqm6l-r_J0U1pzcsuAVW_w90CbREMYrWRnVmrrrO8WSve_vhTpGUzYCTEtbQ4lKTuNuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر رضایی: به وضع اسلام آباد و قبل از آن بر نمی گردیم؛ آمریکا را وادار می کنیم اعتماد ملت ایران را جلب کند
🔹
اگر آمریکا به هفت شرط ایران عمل نکند نه تنگه هرمز باز می شود نه مذاکره می کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/692315" target="_blank">📅 17:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692314">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: برای اولین بار موشک ضدناوشکن روی ناوهواپیمابر جورج واشنگتن منفجر کردیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/692314" target="_blank">📅 17:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692313">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
پزشکیان امروز حدود  ساعت ۱۸:۰۰ به وقت تهران در مجمع عمومی سازمان ملل سخنرانی می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/692313" target="_blank">📅 17:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692312">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
چه کسی پوز آمریکا را به خاک مالیده؟   محسن رضایی:
🔹
آمدند گفتند ایران را تجزیه می‌کنیم. اما نتوانستند و این شکست دیگری است. من اگر بخواهم شکست آمریکا و پیروزی‌هایمان را بگویم مفصل است. چه کسی اولین بار اف ۳۵ زده‌است؟ چه کسی آواکس زده‌است؟ چه کسی چند ده پهباد…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/692312" target="_blank">📅 17:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692311">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: سخنرانی موهوم ترامپ در سازمان ملل یکی از اشتباهات تاریخی او بود  سرلشکر رضایی:
🔹
صحبت‌های ترامپ در مجمع عمومی سازمان ملل و تاکید بیش از حد او روی ایران نشان داد قدرت جمهوری اسلامی ایران دوچندان شده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/692311" target="_blank">📅 16:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692310">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/720108b0d6.mp4?token=Xf9AHhX4Jlo28sDjcBeIpmRSBLv1I7db_dZ466KMlvrZZsVxdBobUUFe-yHAC-sLtI1Ijsn2-nt_d8JaDLmxiAGBpHwCT6tZmptERbd6eg8QuEGz9BqKz_V-QPlxhr1DxrpUWPQ1d3pUvolyxZhB8BB7k434jESApQutju4N4hkG8U7XpmoyFIH7WZRnTo5sWTawDwECUUlzF_MHDz0xyUIjD4UdDHvlkJdto5CyLhFj3DJb_0eB9DjSDr0fQXKve8TAYgnteCRe6EJPZE--92mLIhGasxJUXANjR0jR4kOVfS0E3omTJLXPA-lcFKM0WbrIUcRG6Phiel-tHQzorzNFmJL_hiVByOfWmPjV7LAxDcef0UgtOGBRlgdtWKa_gmw-7ZEf-iB6nXSFH2b97kOwVWsM_Dj_AXAMigCmUXESQe7vkZ5hdW0sa1obKuY7iPd45Tinlg9Hs7GWKrY48SAN7fk-uLA8w-vWJikaejCmUl9hxRhtNJXqcm-Q-E5ir0jGLg61BLrvSxdZCZ3L38N-C4_8KLkDAB-AuUXVC6BHmC65smrSVeJpqgsnCsZoFGzEiQMdxQFWHK5QpiH4U2giLIb5yGPc3Q4uScYN_PasEaucOUpLAGfYDJ--dN_Sfu1SyPum-iS3MEtcf_l9g49faaVN9GH3PHokXWKl6nM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/720108b0d6.mp4?token=Xf9AHhX4Jlo28sDjcBeIpmRSBLv1I7db_dZ466KMlvrZZsVxdBobUUFe-yHAC-sLtI1Ijsn2-nt_d8JaDLmxiAGBpHwCT6tZmptERbd6eg8QuEGz9BqKz_V-QPlxhr1DxrpUWPQ1d3pUvolyxZhB8BB7k434jESApQutju4N4hkG8U7XpmoyFIH7WZRnTo5sWTawDwECUUlzF_MHDz0xyUIjD4UdDHvlkJdto5CyLhFj3DJb_0eB9DjSDr0fQXKve8TAYgnteCRe6EJPZE--92mLIhGasxJUXANjR0jR4kOVfS0E3omTJLXPA-lcFKM0WbrIUcRG6Phiel-tHQzorzNFmJL_hiVByOfWmPjV7LAxDcef0UgtOGBRlgdtWKa_gmw-7ZEf-iB6nXSFH2b97kOwVWsM_Dj_AXAMigCmUXESQe7vkZ5hdW0sa1obKuY7iPd45Tinlg9Hs7GWKrY48SAN7fk-uLA8w-vWJikaejCmUl9hxRhtNJXqcm-Q-E5ir0jGLg61BLrvSxdZCZ3L38N-C4_8KLkDAB-AuUXVC6BHmC65smrSVeJpqgsnCsZoFGzEiQMdxQFWHK5QpiH4U2giLIb5yGPc3Q4uScYN_PasEaucOUpLAGfYDJ--dN_Sfu1SyPum-iS3MEtcf_l9g49faaVN9GH3PHokXWKl6nM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: سخنرانی موهوم ترامپ در سازمان ملل یکی از اشتباهات تاریخی او بود
سرلشکر رضایی:
🔹
صحبت‌های ترامپ در مجمع عمومی سازمان ملل و تاکید بیش از حد او روی ایران نشان داد قدرت جمهوری اسلامی ایران دوچندان شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/692310" target="_blank">📅 16:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692309">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a03f40bc00.mp4?token=Y4gM_wjXZS6qt4TAlFd3zq5I7Q8Ka0Z_zQpuVdhNPXy7CcO4Qx73Q7oNXSEM8eKo2OpK-IBbmwlKz34na9m5WHQQ7adpISryL6kwKFemwMgcsOVy6By__4DMF5rAfdqTyFPqbkqXnOusCKSVbsifE9M3tYkUIcN2KQhNJ3EX7tR8awIisHbsbj2f_NASOdswBj3es9lIZYIBj4Gqo85pZZJv_YcA8mQEYbG4YLIZL9DGZaLKa5qSLnFFUbt7EbRIrowl3y93uQJuOnfKPba80l2BEt-kHNwnGglb6qbx7l25Ay8-sjIo1wQYsRw5dPQ2r91LE-koz9KVGCyEnI34bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a03f40bc00.mp4?token=Y4gM_wjXZS6qt4TAlFd3zq5I7Q8Ka0Z_zQpuVdhNPXy7CcO4Qx73Q7oNXSEM8eKo2OpK-IBbmwlKz34na9m5WHQQ7adpISryL6kwKFemwMgcsOVy6By__4DMF5rAfdqTyFPqbkqXnOusCKSVbsifE9M3tYkUIcN2KQhNJ3EX7tR8awIisHbsbj2f_NASOdswBj3es9lIZYIBj4Gqo85pZZJv_YcA8mQEYbG4YLIZL9DGZaLKa5qSLnFFUbt7EbRIrowl3y93uQJuOnfKPba80l2BEt-kHNwnGglb6qbx7l25Ay8-sjIo1wQYsRw5dPQ2r91LE-koz9KVGCyEnI34bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
التماس ترامپ دیوانه از سایر کشورها برای منزوی کردن ایران
🔹
من از تمام کشورها می‌خواهم که به ما بپیوندند تا ایران را به طور کامل از نظر اقتصادی منزوی کنیم، تا زمانی که از حملات خود علیه کشتی‌های تجاری دست بردارد، از برنامه‌های هسته‌ای خود منصرف شود و از…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/692309" target="_blank">📅 16:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692306">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SHVjFe3iPvBNKYZSXyswgvkZt6SfU4HS-KBlaX43pdEddms429C6nQfWnyYxSmdd_L2CMt4mvAQVohpgG1jPjtyYkTDeFTaMtZ_XItZCZiJAuF0nuZp0fo5PN7ldt-5Qhukh8EfCchA7smyD66OC0sHmfiP8Lzondgcxsw4jFwfeYP0PZTbqXri5DvTAAEaQaN-zPvPzU6e-NXmy864_l9fHm5BtgwgGxJWM0eqvh48oVmUHrM2H6QEdgzkSX3OeNaedBVDIGaJO7LplsPfzFoh_Zl-T_FC8KdTTh6uhoAIBnzU8BF1kU0xZ_1pu0sBNPAQKNC-xg8bNkY1BkNskMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mRKQSXgE9JwYESvC-VL27J0Ja3KtEZs8yVwNNLtEgOo2ipP__LaTt6fReLka3KiioCCkFBhUO3oE-aTyGhncYNLvvxI45S4e95aI_A6u0tFcc33yUR7sEGTWJd5oxvJvXvRuARdMSpubUS5348j0AjFJvOO76hy8nFeHMOYBDnwOltO0rQ72Pu65ZSGDCtDD7t20IlDyM16JVBsuIDeCsaeP5yv6-Ekgc5CFcipPdee7DdKYNAEcFmPd2JvwNJ5icvvbolkCPKgXqLPK0nBRVnirkfdyOU_TaOP2NH8x4qJLrhsoWsJfvGhDLWmYdscKqCEqCM7z5xwiIsdOxxb1Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsVCsE2pPgM1gaNxqHynzq0fhd4gYq-lLa7_1tpeVbep2RTHwH6ItKr_nfoKTAc3VoJTr4L4CdxyY0O66PiLALB_N03UhrebuU_N2EXaqd2_4Kgv7hyeGhMgU4MtOEDu0qdhhXXlx1n8nQvR_jYHjWJEUPCh8y1OlxA-_e_eeOyN0m7l6nyiAerFUuU7sK2O9Bh1kmtWvGzJlti5wgENYJyBhRTG_n-DT1BaDQ2zx0dqaSHR3I7zA4Kqg5yUzDjBJVJ15UnSY2BiWPQHba72NaRDQ7F4c-XzVLCJvrGf7pO77NUgAdd7YrL1h7E1oZNv9PSTA7kq01vbYxjvYK_yGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فرودگاه بین‌المللی نجف: پروازهای ما به ایران، طبق برنامه‌ ادامه دارد و دستوری برای توقف آن‌ها صادر نشده
🔹
در صورت تصمیم جهت توقف پروازها، آن را اجرایی خواهیم کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/692306" target="_blank">📅 16:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692305">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e19aff9dcf.mp4?token=Hbz-0vBtSqr3Fr_jWXbdSdVSItvv5UzdkqCheCXWhG0ywJWV1c5nuyDXlcmt0oA2RJUp8GIHn-JevwvjGcUICVIVemZgZiPE58cVCY7J5gxNvk3Q11E57eeM3LKqdcXeRgm_OLYBWIjoWsFBnrian2c6Or8JbXUMMZJWQiHsxjmIxrSb7jjYW7I-6OSO5L9-V3U_KKHgSWJDwIlxtCUFlNEW0QUeVbDqFFFxqi7tO9Fq5n6qKbCdAAraapMQ1PMzAazu2yA_yy6NkIvlGaNHdlK4jsPfxdN_adFgECn4fEi8JMOZyBT4jZAxeuOh21dkdP_4kOfEX7qe36efDtkcHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e19aff9dcf.mp4?token=Hbz-0vBtSqr3Fr_jWXbdSdVSItvv5UzdkqCheCXWhG0ywJWV1c5nuyDXlcmt0oA2RJUp8GIHn-JevwvjGcUICVIVemZgZiPE58cVCY7J5gxNvk3Q11E57eeM3LKqdcXeRgm_OLYBWIjoWsFBnrian2c6Or8JbXUMMZJWQiHsxjmIxrSb7jjYW7I-6OSO5L9-V3U_KKHgSWJDwIlxtCUFlNEW0QUeVbDqFFFxqi7tO9Fq5n6qKbCdAAraapMQ1PMzAazu2yA_yy6NkIvlGaNHdlK4jsPfxdN_adFgECn4fEi8JMOZyBT4jZAxeuOh21dkdP_4kOfEX7qe36efDtkcHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
الجولانی: به ترامپ گفتم چرا نیوجرسی را به اسرائیل نمی‌دهید؟
رئیس‌جمهور سوریه:
🔹
در دیدار با ترامپ در کاخ سفید، پس از اظهارات او درباره تعلق بلندی‌های جولان به اسرائیل، به شوخی گفتم: شما مالک جولان نیستید که آن را ببخشید، اما مالک نیوجرسی که هستید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/692305" target="_blank">📅 16:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692304">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
طالبان و پاکستان درگیر شدند
🔹
روزنامۀ ۸صبح افغانستان از درگیری طالبان و نیروهای پاکستانی در مرز دو کشور در ولایت پکتیا خبر داد.
🔹
این درگیری چند ساعته ادامه داشت و به‌گفتۀ منابع، شماری از گلوله‌های خمپاره به خانه‌های مردم اصابت کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/692304" target="_blank">📅 16:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692303">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJqJC7jAUYOjqQQgOKW17NTy0RoEnprtmE2j0jkcANFSPj2HtypmQdVudIUUs_VadN5gCiIGzw1muszl8JSdQgYN2Eb3pJzRYuhGHqns9nOOl9oQ2IeAkTm5AiLd5OcDMu2lCUlDkk00OXx952DL9L7YWaEt9ko5I2acpv-lVFd8NhLjBNimHXeAT1fIw8n3KpkyfoRn73GjS26Q0YzJSeXocxpsVJ0B5qXHr5R2iOOzr6WrLXlqfaM0PXHKy6GRK5xCGDgHuirBvWDpv4zL4Pi2gEFWZZl59_YkV9H5USHxcMSIk6lBFkW2rdgWsbL5OjkTaZrLNGOdMFqeTx08BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
التماس ترامپ دیوانه از سایر کشورها برای منزوی کردن ایران
🔹
من از تمام کشورها می‌خواهم که به ما بپیوندند تا ایران را به طور کامل از نظر اقتصادی منزوی کنیم، تا زمانی که از حملات خود علیه کشتی‌های تجاری دست بردارد، از برنامه‌های هسته‌ای خود منصرف شود و از…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/692303" target="_blank">📅 16:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692302">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
رئیس جمهور چین به آمریکا می‌رود ولی به مجمع عمومی سازمان ملل نخواهد رفت، چرا؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/692302" target="_blank">📅 16:24 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692301">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFxIIRDVYPjah8k0cU0Pr3hr-SnEDUSmJKfglyDJIi7N7ED8FNL563bEcfQHZBdzg6TQM95qcrYpMGXPOZu6iySKdbNpGfdIF1awXYJkwhZuMsagx4lMaHxlTY0cy9nO1h2ir2hOAfSmfAP0hqIxisocD79LnDNzt66XbQz-hPg0uSioJmmbJALUUjPLLSc1e1-5duK2_vJ3CWs6iO8HknS0gQVz4px1iN8FnEp9NaMu7oVBzSBI5wMP7FtTPZzO5PCYJ8pR_JlH4bGRLZg--G7Gm-7d9_iUnwEGHcn9uZhx_QD9qgPUCqOekvRbSjfpLXToyjeZwc5hIGN4r8Ajzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابراهیم رضایی، عضو کمیسیون امنیت ملی مجلس: وزارت امور خارجه مجری است نه سیاستگذار. وزیر امور خارجه باید توضیح دهد دیدار او با نماینده دشمن متجاوز بر اساس کدام مجوز و سیاستگذاری انجام شده است؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/692301" target="_blank">📅 16:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692300">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWD26F0MEgi_umiVyxqiWoe93U6UA_RGYWnKg_wr8tlv7kDTmol3Gb_GUws0wfpne233rRwpagmgYxvJKiiZgWRdCt1czzhJjFnFmtikz6psU-5ZleXgbZ8ljnaOQKitZZIHu8PSxS_6jPs1mTLBs47GlKVVjNrf4iBow5MUsbUacCF26e3utiuVa4gq1n3kqTKCdrqpqxKGoBpQxhnmKXjrYjvuiT6o5dJHnaKAmU-R0FuDeVInmgNdejnzWbpmWD0fW8rHMJpn9uSIN8aBIJIL2I_Owjau21u8On8P_PDCAXYQEiet4U4otxHxE5tDjlGgD_FvjWkNHfoMX1SZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان عملیات تجارت دریایی بریتانیا: یک کشتی تجاری در تنگه هرمز هدف یک پرتابه ناشناس قرار گرفته است
🔹
دو نفر از سرنشینان کشتی تجاری هدف‌قرارگرفته در تنگه هرمز زخمی شده‌اند و تمامی اعضای خدمه از کشتی تخلیه شده‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/692300" target="_blank">📅 16:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692299">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkcikyP41Vdz-EQcoFejz5GFThYvjOc7J3EqYnhxaWGi3gnmT_uJ3fKxZHcG0Zp1QwUuXs-VqAwlddMsMILWoVCigEcnSZSsea9ZSfkGosFizmTMHKugT6gOt77SYF8sIN9Lz8G0NdcMasIxkYDUJV4cErTeUocg3NHrq1Bc6RR4AXQXuWGMc04sYxd7_-iMfbVI0GuYIIgqtlwkx1Ry4f1Cu_cNKf0TizPLOHII4PxRkUdaPzwLETsa7eMcZj5hB2mwS-1hWpL1MAopPPipHeryQFdfTDYWZuNScElnEMC_joi92hVE6Yeq7wBZuF301NGvG7EZBPELAS-pITPMQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«گروه زر» حامی ویژه‌برنامه «دهکده بازی‌های آسیایی» شد
🔹
گروه زر با هدف حمایت از ورزش و همراهی با مسیر تلاش و افتخارآفرینی ورزشکاران ایرانی، به‌عنوان حامی رسمی ویژه‌برنامه «دهکده بازی‌های آسیایی» شبکه ورزش، در کنار مخاطبان و کاروان ورزشی ایران خواهد بود.
🔹
این ویژه‌برنامه با تمرکز بر رقابت‌های بازی‌های آسیایی ناگویا ۲۰۲۶، از رقابت‌های صبحگاهی ورزشکاران تا لحظات پایانی مسابقات و اهتزاز پرچم ایران، تصویری نزدیک از تلاش و افتخارآفرینی قهرمانان کشور ارائه می‌دهد.
🔹
حضور برندهای گروه زر در این رویداد، فرصتی برای ارتباط نزدیک‌تر با مخاطبان و همراهی با سبک زندگی پرانرژی و فعال جامعه است.
🔹
این همکاری در قالب ۱۸ هزار دقیقه پخش زنده و پوشش رقابت‌های ورزشکاران ایرانی از شبکه ورزش انجام می‌شود و گروه زر به‌عنوان تنها حامی این ویژه‌برنامه حضور خواهد داشت.
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/692299" target="_blank">📅 16:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692298">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caa4a54621.mp4?token=r0UBUUJsYHNeTm308B6WqJi3rQEMdjyNa-FV4Sa4M3ukxxmCm5CWZ9S5jfbrYjojWfQs_VCX6tK-cbHQ2jbraUJ2oPMvLHBMEb_FPan0Re0UuDQ0fWGX_ZWcQAlNU9fdugKcOIa6H_w_4ZRRYjCIblJRGlF-o2PudMyeyRq1ZT34_StR94fUhGkqbvoiHwZdNhVPuMVztzaCrUwUy7TrDpoOHAw5O1NVCGJJ7lCSwInpFqlaQcFQPask9Nq1szh7M8UM0vEoLN49RjChPBi3QrkT_Q8Rs62lW9I_xDYbpj7EdfcSoFhwulLC-BqTYzp3y1vl4np7-RpnfU3_erh22w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caa4a54621.mp4?token=r0UBUUJsYHNeTm308B6WqJi3rQEMdjyNa-FV4Sa4M3ukxxmCm5CWZ9S5jfbrYjojWfQs_VCX6tK-cbHQ2jbraUJ2oPMvLHBMEb_FPan0Re0UuDQ0fWGX_ZWcQAlNU9fdugKcOIa6H_w_4ZRRYjCIblJRGlF-o2PudMyeyRq1ZT34_StR94fUhGkqbvoiHwZdNhVPuMVztzaCrUwUy7TrDpoOHAw5O1NVCGJJ7lCSwInpFqlaQcFQPask9Nq1szh7M8UM0vEoLN49RjChPBi3QrkT_Q8Rs62lW9I_xDYbpj7EdfcSoFhwulLC-BqTYzp3y1vl4np7-RpnfU3_erh22w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رشیدی‌کوچی، نماینده سابق مجلس: در حق شهید لاریجانی خیلی ظلم کردند/ رسایی میخواهد به هر قیمتی دیده شود
جلال رشیدی کوچی، نماینده سابق مجلس:
🔹
فیلترینگ ضد امنیتی ترین کاری است که یک حکومت میتواند برای خودش انجام بدهد.
طرح عفاف و حجاب راه رفتن روی اعصاب مردم است.
🔹
حمید رسایی فردی است که می‌خواهد به هر قیمتی دیده شود.
🔹
روسیه دوست نمایی است که گاهی منافعش با ما گره می‌خورد.
🔹
در حق شهید لاریجانی خیلی ظلم کردند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/692298" target="_blank">📅 16:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692296">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RMVGaLvqIgmhLWw7si7W3mwLHyZpTO2ItAtYC7_qUpR5BEpsDvSB5WHtj1kccG7T028B-oqQRodH2ZUTkNirXJquKT6NJXSHelfmFGFnK3YgRy4x43FTI1FjOmI_RTtyDYA-YVyq62Nnx9L09aOnSdpPxjssGASb4VAfzHEcLKPSslUK8PECSO5vlspCzyBUTaCyxgPX1CUvu8bAagN2g0iAtHaaxIDnBk6k8PbmYmrBTTwkCOxUlKB7kdQi2Znr_YVf-s67yTWFsS4ii2veCIpCGDAJpmPAhHZlOC1lHPvN_gKDKEzrZB4pj5YzW1sCN8UFNaWa86CjFGJg8mRPlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIW4lj6MqG8aBeXQ10lI4gGUgiDnlkddOJvNuE352njDu3pJTEfWkpNDfTC3_qcdZqlpZBidn6aUk7pZZLAWbGvnCHaq5M06__dGvJ60_XcG4KVMPkiVmzcCcC5KRT5P8srrw9hpJMhf1v54-UXF-aEujLdg4hrbZKjGntCXO58_kVb0tx_CRSVg79pbcMy5jZtY4bnsQl4OipeCMCUWxMzysw0f0wacyrjWJ39FLKb74m5Q0GO10r1OkNzuuEKk3tZ2LhbsDsoLvldE3y42XHvlc9wqvjSmUDrDZ9f5dhxDeUb9KkzbScJples4hzenh8w40d1GB-AD0vXuNerwzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اسرائیل یک مقام دیگر حماس را ترور کرد
🔹
بنیامین نتانیاهو، نخست‌وزیر و یسرائیل کاتس، وزیر جنگ رژیم اسرائیل با انتشار بیانیه‌ای مشترک اعلام کردند محمود ابوعلوان، «مسئول مالی حماس» را در یک حمله هوایی به خان‌یونس در نوار غزه ترور کردند.
🇮🇷
✊
@AkhbareFori |…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/692296" target="_blank">📅 16:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692295">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc524e737f.mp4?token=OJ7ydMz27wi9xj9WQrX6Ln3DmMQ2Koc9bID41XMxrVcA9aTGEi_nfQcEVFvntqs0jplLj_ZUxgOgukruFnGVTMfGtUEhUE2IDlyKubR9LDTBeOjPbamR1-ww77M4hgzymQXtMuZtokVuyNvIaWdSHTAVUVwrRzQbo_vbNRxQYYcw-MpYlOqW563-1aPt0HgU8AewoSenCCo3aJvPaR9H5CftFZnkio-6E1rnzjZB4dgHt3mJsUPvUdSj1fICPF_GrVbY9dS7m8S-tLpbbQb-VEZXShX9icnszvvAdh-o-7fZXayizRsNANqRKrPahZpJ14MpXF3hrJMHyx4R0iDtoLm1ZOxszV1b-yR80C6-VYdZs3QtMwTwRhygWa3dRjgAD2SHsiYCCP59CpUMOPSSKTptJKzA2iPWpBtxeFSSJeSWrOEH19WodOsWuIDQcvFh6RrB_xLedwkTbZwjLYBUwsxRJrIkNbVvh__DDQKst16_5FsZLYcXkBZnSzJ3Cc9NgTC-zlT3XaOV5N_eqpVvgXH1t4z5WnHweBoE8yulmO9D-S1hXc6pfrs2hJeV-vh1dz27YYzEarkStWaD84FuZoxnUgqNyU5t7GvKX56dqZRcMBg-npGy0ur5X4cKxRzZbW5zaXwfVcePsLodtPT58Z_MpA9a2jkWjFlJc0inpFs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc524e737f.mp4?token=OJ7ydMz27wi9xj9WQrX6Ln3DmMQ2Koc9bID41XMxrVcA9aTGEi_nfQcEVFvntqs0jplLj_ZUxgOgukruFnGVTMfGtUEhUE2IDlyKubR9LDTBeOjPbamR1-ww77M4hgzymQXtMuZtokVuyNvIaWdSHTAVUVwrRzQbo_vbNRxQYYcw-MpYlOqW563-1aPt0HgU8AewoSenCCo3aJvPaR9H5CftFZnkio-6E1rnzjZB4dgHt3mJsUPvUdSj1fICPF_GrVbY9dS7m8S-tLpbbQb-VEZXShX9icnszvvAdh-o-7fZXayizRsNANqRKrPahZpJ14MpXF3hrJMHyx4R0iDtoLm1ZOxszV1b-yR80C6-VYdZs3QtMwTwRhygWa3dRjgAD2SHsiYCCP59CpUMOPSSKTptJKzA2iPWpBtxeFSSJeSWrOEH19WodOsWuIDQcvFh6RrB_xLedwkTbZwjLYBUwsxRJrIkNbVvh__DDQKst16_5FsZLYcXkBZnSzJ3Cc9NgTC-zlT3XaOV5N_eqpVvgXH1t4z5WnHweBoE8yulmO9D-S1hXc6pfrs2hJeV-vh1dz27YYzEarkStWaD84FuZoxnUgqNyU5t7GvKX56dqZRcMBg-npGy0ur5X4cKxRzZbW5zaXwfVcePsLodtPT58Z_MpA9a2jkWjFlJc0inpFs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر در صندوق اهرمی سرمایه بذاریم، سود بیشتری می‌کنیم یا ریسک دارایی‌مون بالاتر میره؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/692295" target="_blank">📅 16:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692294">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3faadbcde7.mp4?token=jeIBqYGdaKyWMLALLEWlrZuEjXyymsy1F7owhkgimhg-tgZrQSgpyBxlQXuzY4S2sPsZK2-xc2wrrcez-Sa-ee6cNTRTuKE8Q742PZTPgIPhF_pBWk_WpRufRBaOIa1wO7BaaQB4WMnYelU1OeXVaRSYLDiD6h59HYYVvzhEs-L6MpWPdgfYwRSC4W9a478AJ2IZqf_S-B-0yIrVNWQXa6sqRCG8hTc7NpqB_usR72SNVARJVrAtGaTmrlXcCodIVB5MOM1ss68K1EKQOUvhle7S3gpciDppVKiwmxYPTR3QSBn2Nx0rwEQu6ckoVAkXnYT7V0n8n36rQsuk6mW2gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3faadbcde7.mp4?token=jeIBqYGdaKyWMLALLEWlrZuEjXyymsy1F7owhkgimhg-tgZrQSgpyBxlQXuzY4S2sPsZK2-xc2wrrcez-Sa-ee6cNTRTuKE8Q742PZTPgIPhF_pBWk_WpRufRBaOIa1wO7BaaQB4WMnYelU1OeXVaRSYLDiD6h59HYYVvzhEs-L6MpWPdgfYwRSC4W9a478AJ2IZqf_S-B-0yIrVNWQXa6sqRCG8hTc7NpqB_usR72SNVARJVrAtGaTmrlXcCodIVB5MOM1ss68K1EKQOUvhle7S3gpciDppVKiwmxYPTR3QSBn2Nx0rwEQu6ckoVAkXnYT7V0n8n36rQsuk6mW2gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاکسازی خانۀ تیمی تروریست‌ها در جهادآباد سراوان
🔹
یک منبع آگاه از انجام عملیات ویژه برای پاکسازی خانۀ تیمی در منطقۀ جهادآباد سراوان خبر داد و گفت عملیات علیه تروریست‌ها همچنان ادامه دارد./ فارس  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/692294" target="_blank">📅 16:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692293">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYLukddvRWwG_WesezzRYPz8kTvqdX7GChbTfdzP1eIr4M6rdOLX2pfJPmFieq48fBh9D-43spchXuSYv1a4C5_FH4BQLYpdmtrI30Zyz5Hn1o1uhb_X6XktM6FrOcaOiQEpSa9eenrtKTO4L2_x1a1K8qSb0166EZhXbZ3x529Rhtcbt7_Gw4xceOMC-VI567zFwSOSascop-eacSM57QDEfekhqe3vt3YWnE2BDauoxBxRpnXvGIYHkNBKEHSWJEh46_v8Do5ASFt6Jr7R7dgceAHVXnvkwzhgiYARedsFB67hnfkqM0-E8pIAhVkwYKTolgVNKPXMGpU0a0fZHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط جنگنده «هاوک» نیروی هوایی انگلیس در ولز
🔹
یک فروند جنگنده هاوک نیروی هوایی انگلیس در نزدیکی پایگاه RAF Valley در ولز سقوط کرد؛ دو خلبان هواپیما با خروج اضطراری نجات یافتند و علت حادثه در دست بررسی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/692293" target="_blank">📅 15:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692291">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d635e8d3.mp4?token=VaiWlgjJmmSfZCtyrMJz1v9Yca9tqprWw_OxLCu7pEt8awiNqIFLXJ6H_woi1zs6v2OHXCxS_xARQIf4T7zsEcr-gewXf_tLkfcwJtKa05HG9RxVcb53OuInK3rnUx1tDhSnQi2_Xqo2CbA_wIN4Jd-2ss7I30RCBcbwfBHocFWQAPGpVzzZZNbVu5SbAF4KAZlv9YWHai0djoafnut_N7AG_NjqLjyG3pCoEmehQku7q_H_8fMPK_sV2mRUECiqd5qdKxwfJBRMJ5OuYMjYAa7fqBsAdbywebiDbQ_I1jAPYhAAX_-R69MTc9hqskcUUL6Dbmq0DoFh9MUBd33fyqF_TyTPOMFULTth8DI9XX0LVw8VbuHVxJ5s7MKT-pX2Y9lspkLqoicKDM4MX-u_QupMc0b5hdDSb0P0u2irTHvdmHnEBoVd3shxfHXvyFlnzb4Htbl1UT6lw7Jzt1N2wFiOJz4gKWNlqtCWxqNGkmoVejNT-K5yFQTm7we5kO8HHU3A_VY297xdeU7SDjGEW2KlK7ZvUtrBEzhHFzQChk0zSs74-2ILNq-KX1dAzjk3p3jR5Lqx0W9xh_x5ecCPnYRgbj9TOTJ700PNXRrt2o4jFAummT8tumhLYbbJwGeRNedMwbELqqcky1ZB1Q5mmBszdKoT7ZFIhQYi0z5XrMI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d635e8d3.mp4?token=VaiWlgjJmmSfZCtyrMJz1v9Yca9tqprWw_OxLCu7pEt8awiNqIFLXJ6H_woi1zs6v2OHXCxS_xARQIf4T7zsEcr-gewXf_tLkfcwJtKa05HG9RxVcb53OuInK3rnUx1tDhSnQi2_Xqo2CbA_wIN4Jd-2ss7I30RCBcbwfBHocFWQAPGpVzzZZNbVu5SbAF4KAZlv9YWHai0djoafnut_N7AG_NjqLjyG3pCoEmehQku7q_H_8fMPK_sV2mRUECiqd5qdKxwfJBRMJ5OuYMjYAa7fqBsAdbywebiDbQ_I1jAPYhAAX_-R69MTc9hqskcUUL6Dbmq0DoFh9MUBd33fyqF_TyTPOMFULTth8DI9XX0LVw8VbuHVxJ5s7MKT-pX2Y9lspkLqoicKDM4MX-u_QupMc0b5hdDSb0P0u2irTHvdmHnEBoVd3shxfHXvyFlnzb4Htbl1UT6lw7Jzt1N2wFiOJz4gKWNlqtCWxqNGkmoVejNT-K5yFQTm7we5kO8HHU3A_VY297xdeU7SDjGEW2KlK7ZvUtrBEzhHFzQChk0zSs74-2ILNq-KX1dAzjk3p3jR5Lqx0W9xh_x5ecCPnYRgbj9TOTJ700PNXRrt2o4jFAummT8tumhLYbbJwGeRNedMwbELqqcky1ZB1Q5mmBszdKoT7ZFIhQYi0z5XrMI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امروز اول مهر است و اینجا مدرسه شجره طیبه میناب؛ مادر ماکان به دنبال فرزندش آمده اما...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/692291" target="_blank">📅 15:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692290">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‼️
پاکسازی خانۀ تیمی تروریست‌ها در جهادآباد سراوان
🔹
یک منبع آگاه از انجام عملیات ویژه برای پاکسازی خانۀ تیمی در منطقۀ جهادآباد سراوان خبر داد و گفت عملیات علیه تروریست‌ها همچنان ادامه دارد./ فارس
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/692290" target="_blank">📅 15:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692289">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrQ3-bteH_3Z0RIov232fnKFaCB-oGqieeri5D7bESJPqIi6kXFOH0lGEhXvFO_BoTRqVvui9-rJ5mLoMDd3zsvrtnSq3KM_M36dHMKDgY1ThzHlQD12IB2TvfInWhYNvsKQkSWsmARikhjhKVHuinckRTEdixM09sX9u6HQEWkIcu0ofckM8X-cI9STcaW8I1xTm24ektilhDAqW3rk85_luM6c9T67msZKCjdqzhcXqxMCjloXXNOVmK8RZELsX-cyDPUoHm0dAAkG-atPJzSSMI8KNeNSBkwfD1crLqIrzo75YS61NAeMVL5leMHCbCzIm7EoCL7AZ-FFwPdFLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان عملیات تجارت دریایی بریتانیا: یک کشتی تجاری در تنگه هرمز هدف یک پرتابه ناشناس قرار گرفته است
🔹
دو نفر از سرنشینان کشتی تجاری هدف‌قرارگرفته در تنگه هرمز زخمی شده‌اند و تمامی اعضای خدمه از کشتی تخلیه شده‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/692289" target="_blank">📅 15:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692279">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ewzao2mW5-kD9ke_XRbS777f-eKfKfPh8QGwwJgrdbbVhdBLdIk9YcvqYmSuQBpjm-cPAVNWolV3SEJT4UBBUck2F7udQeluY0GWJHw3WnELVTjSO4-X5xdq7n_C5Ls6phoPoZCK7SqM2zJdjparV5Z6LrXk0RDu7RQupCzb6S6cSDgp6k1ZslEkyVffqRJjkSM2EDp8lvxHNDCScm97DAbyyHacupiLKCw7BvgmbOdfErl9tZJKWj1wtXRRmAY_ncYpGu2D98b78moBEkIOj1YEQh7RWVo_Kaft5cFXD-9bndz-hKxf2_a0T6JkJbhqO8eNuJe5xZ9OTX22mJuhnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XfJPca-hHVpvfAa6rkyJM3cOnQ1Qj8u9O0mEmL8T4kZ3fwd04WOLX28mi1Zcjh3aFFlLbUshS8Ph6mrbc91tcTSagxQPAfXF61I2oi8YMDDJQuVyW9rSMdmPI4K908ZVVip0edwLPPJSvxQtsDyDHdsFG9seiAplRWJurqv8f-gowBE2yayKVGvqLA1MPgR3b2iSsxZbfr1xZ5aoc54qvBJPh2ziMuH4W3REjVQbJgtSYt32ci1v058TYalTGnxLUb8VpHbcN1YCZCwbYXFRP1fxIo8_DipsXP7l9n0y1sjdaL8sXjo4xHMxo0uOiyagmic6AYQj5tEFU8LMLn5tZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mb-9HkvLbzqJzTN6zCaQMAdQS9G-gkWOxHumHFH8y6MHKoizaVIeqs045mPr4SiVfI6bF3_Lh6eWEw1AwJGi4hLSJWLgkpG4KNIyfsdIVOMDgqxCYSmfYhk-DeKrpBYryuuLQ_r8i8d4MkXIJfXxP8MxmTG8CUMXM6gCkM3NiQWH8YSuQTdOXpCYGysOdGkkpEpZtHtCM6D0P1pp_f6Hv5DLIeDORz1wgUXwL4-6NNmNPVPgvKPVFY2t5XeX-RvxCUZBeaj5mXK0ZTvoDAYwRTPEfMSNAeTQaxuT5MJh64N-A6U7C-PqizIR4i_9GVVZleWexVEWrKHUmL6oaLmStg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HwGsFl7qiJcJKlYxiD4RIcFDEUwCrHNwk0shkgHntKVvWIi2CRlaRhZJENqxiw5GtMULy3yBKeAFlnVBdyvu4for8cVTdYwNdOt87ndNrkbTUPObUDrkZXFo_fQZDFZ_FZVv9tq1CvUmODJbIa8nCqSLBtpHhbylGh0obLFGn4bnXe4zTg0ElzrY9FTZHU7gD_hQfv2D73G5bZb-egmATGzWaZaANotT7ESrGEqOC4TkjHWPSsJQ6Gy0zNPCazBwso75CB_l09mJKlqTDbMDV-myzuTcRr3i-v6vYQ8d8r2JFxbiwuvSxGI6DyyXXtQPM2L8nIYTBdzl7j2bSkZIPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDzuJN-6cZuc_kenXdFa4gZKLZlzaWFeZZhFTR3WBahRz8pHg54-oqxZIolNTuyWzvVU_9_EHmEyJVBWaNq18p32dKPzE82dUOcDZDwQPWq9Y4kOWOA3teJf5BdtrD4tcM6xq-PgvEg2HEFC3GdhXJLl9g0jqsO7nRc1CoW0bz0HnqDY6emjQuICWAS5dAH0iH6Bi9iJvf4QYPBY9P-7QQSN6CjniTTA2baJ9OjxdCeGj7TpHSvt2Y3R2vmbAhFBCxuxleUzpkWK7IzVIfqmcyBkuIO_ucQmH5jRZsni4hjw91AecW9mJHwT0Uu9Ixje_rr_NMM5gAN3hJxDzD8lFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CBLZTLxw9qJocgIQ1WHJPvaAVvOI1AGwVXrobY3xu4fp9_PVNGUTAy1go6UJLt182fwCLWXm_jdSOeqlsyjI17CID6SrQ_DlCztLTS-0U8PDXHhqAObV-PRKs-CkaBECNpZjvgM0zZ7RH_dNqC3j-0aTqSg-nVDE-l7A3iL5OcYTNu_TIiTbSPNSZJIAQrjxF9f4NheXWbTo3zpw6JfTERPQYR5PoUIoNy6s82304Ywu6CCbF8zcIkE3fs7qkDaQy3rQeiRardZmS1z8GzwInpy7C1O6ITViyM83o3H0SrBJJiZ0eo66IiSE-X6h2wy9jmvdQ567UAUFbAX2b9gRLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2p2Jj8H4PcxiEY3iQlPo96qpq_NCmyJq14oa-OBmxT5fROsensaty6jmAgtcs54zKsHd_2h8BqKHLm6vstmPHeyIy3pyRZ_5cv_VmD5MWciq-DQ5Syn2JeaOMoed7Xtoia9dQVhCWrBagPKu18Cky4Vj__A-xPV3eDSiip2_sme_pMr8S794fNIL8etC7yS9TuoBZgcxjflaCM4lShEXtraoyO_F6ZO3MQPZjfzLmmWOv0UF0XSQGf_MvzX7zwZPCflQdke7taqeHZL3hM65xyccuLDwzokOv7AXXr36bQYXuhROhCty0UeJAzEoOhib_V_x2uQ584kug_oy7-1sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mb-jrEZIs_cjqG5hkK1qHTJfWu9pYi0k3_R5Q8_CS6krZ0Omen4Mc-DK9uLl43OFDTShGPTLg-uoltwJ3pHn905CZSGndd6zUTe39CNBesTTh6jwar5ctWT6OS-omaR06SnRXWHY-r_K9fnKMD3POap_j90JyzF8sGxvejuPH1p1ahzACXvrHEgXI9A6KJ5nlqMWw_8SuIOYjDN5Rfcgg2kR8IjaN-1I9XTN3OA45PgWKnDCQiZDrOZx1rfTfb9lnNKN3CbgKZAJkTz-alM6O-mz7YQ01IsGpJ9RVJDeStmXJCd4wHCzzsnqYZoB4yXtY9PuwIsLi0y9zteNuvt-og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bs43DTxnZxt_hpwtO6CUjGyOa58DytElAkCuQS4WD1gPysPDPTl-ukqslRdrOcdTbzfWFsjENxyF7O4YpzoanYXfzxvnYOTJdpuoVGQPgxBJAoaaqawyM_99GkRGkiEPDnTs7MCsJw18klAwHrxVpCnPM7jCDUMQjYPxE5wwpb0HFherkM9sbtv9ChebsXaJJDlKaBl-jr0Gw2QMo_cJv6cJV-ltQzYgxQBMA4LMzLU72aBdVsviUzNPY3ncJG51TcaE9Je5DPrXxsAxWbEFvEdghsHElgKRljaconFyEDDjzo6KatJeZWKXlTrcb42M314rEdH8Q3pYtXrl4Myejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LNtnHk6DUfmMMQKHGVgaBqIlQJAFwez-jflKSy3JfHNOxZ4QaPwdswH763imqoz7SUaewp_2ZbXotoEDdKN6nxzaY5Mg-FeVd3S-Div7lPXPlGxvR4hsPH7eECDXVI63nPJjXGX4dMt9F6ffKIxha-HnRsc1ReBDSJj0xWkUuATG614KxbJFruCKSvEoa61c37QMNwFCzcmB9SNHwW7pfs0xVfPrPX03uFany_XQCInpcLFBHCEqTtXpnmE5FQX-RclIvec4R5qRbBQ_t3nscKI4twV6ifE1AKdW9cuyPdVYC0nT2YQNFlLQQEIR2OIsPgKs4ieupiYzAX49rnQZig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
روایت مخاطبین الوفوری  از موانع پیش‌رو برای دسترسی آسان به اقلام دارویی ضروری.
🔸
در چند خط  روایت خود را همراه با نام، شهر و نام دارو برای ما ارسال کنید
👇
#درد_دارو
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/692279" target="_blank">📅 15:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692278">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ضرب طلای سوم ایران در بازی‌های آسیایی
🔹
تیم فوتبال الکترونیک ایران (حسن پاجانی و ابوالفضل آقایی‌نسب) در فینال بازی‌های آسیایی موفق شد مالزی را شکست دهد و مدال ارزشمند طلا را کسب کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/692278" target="_blank">📅 15:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692277">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e8763c8e9.mp4?token=eBPkm2-TGaAgKcQ8D3gD9YQ3KgZd3yB-NrFKCbg47Uplbm1jMcAdB66lzY3wN7ZWjEsAGzWW-TH08O0UA0Z4tfoSKNC0AqdsnmeTIMfHDC5K0ZPat0g0qt66IXAAifSIHW3kbUw4Ursy7aTI4XHdxP6lwKnfFiNKKnv4D-v87LbdvlpjcZ0_a_Xkgqc9wLubAkXhMR-AtYtXo_dKKKhjZDhdwHG_m2KxL7C-oxkzb43USfVa4kFl96NebEiBfXNSHTn_eLCcpGnFpS3KGGYAHAcruewaFw_UoX03ROIbkiZQoGk0MJyo3eav89RE9yTF2sptRU4CIbIJtfPDvmvG8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e8763c8e9.mp4?token=eBPkm2-TGaAgKcQ8D3gD9YQ3KgZd3yB-NrFKCbg47Uplbm1jMcAdB66lzY3wN7ZWjEsAGzWW-TH08O0UA0Z4tfoSKNC0AqdsnmeTIMfHDC5K0ZPat0g0qt66IXAAifSIHW3kbUw4Ursy7aTI4XHdxP6lwKnfFiNKKnv4D-v87LbdvlpjcZ0_a_Xkgqc9wLubAkXhMR-AtYtXo_dKKKhjZDhdwHG_m2KxL7C-oxkzb43USfVa4kFl96NebEiBfXNSHTn_eLCcpGnFpS3KGGYAHAcruewaFw_UoX03ROIbkiZQoGk0MJyo3eav89RE9yTF2sptRU4CIbIJtfPDvmvG8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلاس‌اولی‌هایی که امروز راهی مدرسه شدند، همان کودکانی هستند که در روزهای کرونا به دنیا آمدند
...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/692277" target="_blank">📅 15:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692276">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d278f89f.mp4?token=rACPtCbqzpmfoXdxGXHsqSxxEGUYMURgtd7TAaAG2loYTMKpzGCBRGGBUpS3eq128ReDivyLjz2a_h7Ic1LPojko_F89uu50JMM5yQiEnJvGaeP7At9vK5JeV3QXB0yLUFWs2O0WJaNM785m5u74B1Ox7T5wDxaY2iI0jlOeuIxoQXWrGIKWVfR7OieZwlqcpIbNLVChQ3ztrb2S49tFi1gwowyBajINp9AbjV9inSGpCtjFKO2QnboLqDlFQD0wyyZEoLsiSxPd56X0-SnbnirZr5ycJYhv9lx7xPXfouC_NMzhHBO0PEy4qfI-pZcngY1_8EzV3TT70CkGFiJwqAJVV9mb__WYOX2-d7Dv1De2S4sbKcdmxHgpZGfXDgT25AKjH2whCUn3FfdCKc4-unK8t-YZjBRgDNfFHm2nmTxO3JCFMbtJR1rLyMfGJFXTCuZkKZVtYALxA799m4IkMzoULOIR7FroFLDRJ8eQvYVq3eLbk7O9V4Lx-jAmWS2fxSADtQWHNvlNe0McBPPc246PkoKpkjrXAgbrjTtyNsTQf8a81JXfN7wU_xgwwdE2_DvX9EX1m2Pdg8II1hKtCXvCRLcPwWRfOOic61HQRURPWRq4rn89uFrGnH3CycuyUN0uQnjCyXAtjTetPXPNJqd3_WeoTC3BN7FmOjyw01A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d278f89f.mp4?token=rACPtCbqzpmfoXdxGXHsqSxxEGUYMURgtd7TAaAG2loYTMKpzGCBRGGBUpS3eq128ReDivyLjz2a_h7Ic1LPojko_F89uu50JMM5yQiEnJvGaeP7At9vK5JeV3QXB0yLUFWs2O0WJaNM785m5u74B1Ox7T5wDxaY2iI0jlOeuIxoQXWrGIKWVfR7OieZwlqcpIbNLVChQ3ztrb2S49tFi1gwowyBajINp9AbjV9inSGpCtjFKO2QnboLqDlFQD0wyyZEoLsiSxPd56X0-SnbnirZr5ycJYhv9lx7xPXfouC_NMzhHBO0PEy4qfI-pZcngY1_8EzV3TT70CkGFiJwqAJVV9mb__WYOX2-d7Dv1De2S4sbKcdmxHgpZGfXDgT25AKjH2whCUn3FfdCKc4-unK8t-YZjBRgDNfFHm2nmTxO3JCFMbtJR1rLyMfGJFXTCuZkKZVtYALxA799m4IkMzoULOIR7FroFLDRJ8eQvYVq3eLbk7O9V4Lx-jAmWS2fxSADtQWHNvlNe0McBPPc246PkoKpkjrXAgbrjTtyNsTQf8a81JXfN7wU_xgwwdE2_DvX9EX1m2Pdg8II1hKtCXvCRLcPwWRfOOic61HQRURPWRq4rn89uFrGnH3CycuyUN0uQnjCyXAtjTetPXPNJqd3_WeoTC3BN7FmOjyw01A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جاهای خالی لباست رو با این ستاره‌های زیبا پر کن
⭐️
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/692276" target="_blank">📅 14:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692275">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 بزرگ‌ترین مشکل بیمه تکمیلی از نگاه شما چیست؟</h4>
<ul>
<li>✓ پوشش ناکافی خدمات</li>
<li>✓ هزینه بالای بیمه</li>
<li>✓ تأخیر در پرداخت خسارت</li>
<li>✓ روند اداری پیچیده</li>
<li>✓ سقف تعهدات پایین</li>
<li>✓ محدودیت مراکز طرف قرارداد</li>
<li>✓ مشکل قابل توجهی ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/692275" target="_blank">📅 14:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692274">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
انجمن داروسازان: تاکنون هیچ واکسنی وارد کشور نشده است  روابط عمومی انجمن داروسازان:
🔹
تاکنون هیچ دوز واکسن وارد کشور نشده و واردات پیش‌بینی‌شده یک میلیون دوز نیز به دلیل مشکلات مربوط به پذیرش مسئولیت متوقف مانده است./ جریان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/692274" target="_blank">📅 14:41 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692272">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
آغاز به کار مراکز آموزشی جانفدا به زودی در سراسر کشور
🔹
ثبت نام در سایت
janfadaa.ir
و ارسال عدد ۱ به سامانه ۳۰۰۰۱۱۵۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/692272" target="_blank">📅 14:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692261">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rUf40o4yTC2RxHLb9cpE0qipTVh_p8A94J4Jgqu0XsSo49-7UpM76hu0iwhEb7BlkK1iUqq3bHMnm7Z2qE0RbiIG-Yo7bKWxwRDcxGzcu4ZyVM0xuDWE53KNVFi1PmdJW_0oAurV48kv5d8vntkgxnfGdJDeLBlwriFk0UshXBSy6LtuBo94Tojkygf1tYUfIWcpiV8lIOej9cvtUD5MHdsFHgyL7o6qJAHB28-AugeuBaD4J4BVIFy8BlK4JwvNbyarrsshwngNcCghLBBuOHQevkEh8aPqvxyVLXe8NlFlHtqJt2nmID3LBD_0J1CPRhtQ1CGEGIDRppHFiGR8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlYQeKYK_ZzzVATHfaxF3y2E4wCoHZatMpthSwmJ2dwhAFhL7xJAnstNZOARjuKB4KLcnEyNeEf9lfl40LqHURf3PhYr9CJXGW0V5HdnmruQ0Y9F_AL3txozYwxuVAiGdXQq8Z_ulko1uwFydbto44lFgK4HiIVPqjzTNyVVmw9t1jPQ7rsHg5q6giWHUUus1HWHlcLi1w_e8ps6gpnVI4t8qYP7OqmyX6nEti1R3kKct2cCe7pcyrmE9OaXefsbpqhOZUJmZgkDmXMWC1XM0Tm8P3OBrDguSllAffzHtMvCgdxNGhl7FSb26xpfiYS4Wqekpo9G5asyiTsTkv7hhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O4D6kt-ksk27PmmErXxVl1jFWSqgUUR9iOCc3bGY1VwzTb_oI3vD-7xLbj_8Cd7lVpezdlsV2brGJbXu7IdYf4Bj1ggSmN2wf55e7dqx9_36_FFXQAW_U0enHOMygU62dVYX-E7eVPheQVwOcYcFtPb_oCZcxP9KeMSjZQwOh2xrAhuuB5TbV0FwREn6VqI9IVcngydu9RSpgPdG46Gqu18yRm28SN_O3G9w4cNcyW7PgUH3YaCeK_bwMNsc-nLUpVO0db5ItbIvXqZ55D8vcxlYXR9LYpMlk4myq1Y07IH93Uca0aHodthjRrRnIK5-Rc-UM8IlwFEvniQbZK4XqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VzgskSDySze54-HrRB1HPLQzd7uxkLXXrQQMnrle8ntHkjv8HhqmOzR-1TJMmINC0-VUUAU4_BGLsuROZsT3O_3GXZFEfzfPSOijCCp29S5Y7OpGyIbP0RNUoKVffaN0Hte3l4vAqkzd5MmC7dUF25kgbSL7dyGIVjixVhS8hUhmPeaX982-5G9QT__M4maBCDY3bgQ3JZf0zx88Za41p0dHjHvXkoUeIpRtZI3KIE6jg8DUR6QdCCCG4f7vauuPXZqtsQc6Uh0Z1yhhUpHFvgjVIurFOCdmTjQkx-xh3FJgKmAp42bnIoTR0T-H15UV_F6f5yIADWcGOc3kMd-0tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXAWBOPLN6cfVVwUDiRLR7XxQkcDsjAkLGb92YJvYNUCLlxOkXlEdkofpieoF8fRWfSTLvxGNO7VrDJl5JqYtZGvpSoLo8D9s_IKrTqrK216xZCFjTo0vlQb6dMWEK3TE6HnmP8GyFNM_v-id9XDTfW_jUvqaaxrGAynLOOMaJCN-942JQ_I2nPwi6T-kyXpsea1Equch4Zvye_0atqMxr0WYtvZn4EIxB73OyHqy6qX008CQpSsi1aq3y3K4Ymwb5EFPS3rIL0x3-njpRIUbQDwq20fc7V6rzX7VwE_Rc-eq5Ya2ajiOzvG-I0Hbgm6GLh2_sHwCx_1CbM0Nwu4AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gQy629VFFQ6JhWV91mNt_k-4stvdhSR2agud5vlVDNG8Zp-as4AAYN_D8hyKZtYKTg9cSVhVHt-J0RYmCwsLSyLdEwPtyRHcaBgUL6QcsIvYQCV7LJpgdeV9ZO_R0XhX1yJSXdumzifAPBOIe1001viRw3C-nVRD-h6jZNIaP-r-I6zKo41LjrGTPwBIOC2OrpSxnAuKzLuI0O79JBL1ewzXz8cIM5GN13jzstCnKq45deE02kFKLjL4dY5606FsETBGpujebsKMj8ESevWHLA2b9sNyZrgDEs7urRlAth62jmbQiAmaZwUEQOj71sgGvKrHp7Uk1cFSFDUVHsM7ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UhZ56N2cU8uFuEl9XssvO5s5pvzYUCWle5-BCXwqkZON98ZofhqtQbARnt9blqTqsMoY0gLC28MIdhIeu10eAMyX5VLz6tpENHj8YJAZ-iNuEN64kcxPTvQrrj0Nuor8mhqRIx7_RhpDndTKOzzOrj4chGFWzUiFPJqwi1di0l5BVsfYU7vCXJBtCi1n3Xv5X3b6-4ygc9uJxK7RKH_SN4O_s9tDc4D2zwTx8pKMUPWDb87sJ-tGGsK1D4IOQFUm80cOlua19COmcxyFCmCcRGeHsUrRafZhubhxKotdk1OMgV8Ol1tGpMSazO5wx4cNIe2INKu8IixyUxAzIqFONQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QKE653kfQmnh4SIKMFvie85FTZUOPzADDPa8QyQlCc0oquGqLc4fE3Ir3EqmhBvdGdltzAb0_OOrTZPWlU6R3gBGv0qddJpG1dmBg502p-8RS0HsIT5oUxUzmMj6a5d914zYb4dGaXJTyCas630yVpcu7o89xtwDOC0L46yWejC3TEmhpswue2UYygGxP72x0-ufhTHmLYNDHBrNmR18yr6o6CiB1vdbYAMuUIEmOjGoQIF_QcToU1UpxoGcuxxvzlaEIMAy_Zi7hkoo2bFFdpV7SSOS0PSI6GtC5B1jqMsb6nHuRI79ie2UpY3IodSEEER92Fttp2QPqprSQpUAPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💔
به یاد بچه‌هایی که قصه‌شان نیمه‌تمام ماند
▫️
این بسته‌ها برای دانش‌آموزان کم‌برخوردار جنوب کشور، به یاد کودکان شهید دبستان شجره طیبه میناب آماده شده‌اند.
🤍
✨
فردا عازم سیریک هستیم تا این بسته‌ها رو به دست بچه‌ها برسونیم.اگر شما هم می‌خواهید در این مسیر همراه ما باشید، می‌تونید کمک‌های خودتون رو به شماره کارت زیر واریز کنید:
💳
5029087002135690
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/692261" target="_blank">📅 14:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692260">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
اسرائیل یک مقام دیگر حماس را ترور کرد
🔹
بنیامین نتانیاهو، نخست‌وزیر و یسرائیل کاتس، وزیر جنگ رژیم اسرائیل با انتشار بیانیه‌ای مشترک اعلام کردند محمود ابوعلوان، «مسئول مالی حماس» را در یک حمله هوایی به خان‌یونس در نوار غزه ترور کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/692260" target="_blank">📅 13:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692251">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca98292ccf.mp4?token=nug5WfGgq7uky1ipmpsZMHoaxA6XbKltZ81Kssa3OBwSRmfJNKnr-WK0QTExlo4ckm9K5Qi0WBMXZ8a3bIZ0DvlrMORcXeImlpfR87nRH9EqR7HYsPzG-MSlpHK9fiW5Wf098y32ukp3GCN-uWHVQ5Gt5LWfZ-UhQA1fwSD8d77q1rNd-t_58rOKRbO0DpvnhLSqYrWuyuX_JuWB-NUTxb3QkzTQhsPgo9XeNgcbxUk-9CtwPf25rqwgK5Gc-NsiLIEGnXqH9AU6-ModiDzUHGTWvt3_S2ugq7wJw1Nxea-1VEQmN8TaYqDOLoCPY7jvEdX29hUVNopUNN38SIAWCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca98292ccf.mp4?token=nug5WfGgq7uky1ipmpsZMHoaxA6XbKltZ81Kssa3OBwSRmfJNKnr-WK0QTExlo4ckm9K5Qi0WBMXZ8a3bIZ0DvlrMORcXeImlpfR87nRH9EqR7HYsPzG-MSlpHK9fiW5Wf098y32ukp3GCN-uWHVQ5Gt5LWfZ-UhQA1fwSD8d77q1rNd-t_58rOKRbO0DpvnhLSqYrWuyuX_JuWB-NUTxb3QkzTQhsPgo9XeNgcbxUk-9CtwPf25rqwgK5Gc-NsiLIEGnXqH9AU6-ModiDzUHGTWvt3_S2ugq7wJw1Nxea-1VEQmN8TaYqDOLoCPY7jvEdX29hUVNopUNN38SIAWCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری عجیب استقلالی سابق؛ صبح بازی مرگ‌وزندگی، چهار ستاره تیم لب‌ساحل مشغول اسب‌سواری بودند!
سعید بیگی، هافبک اسبق استقلال:
🔹
صبح بازی که حکم مرگ و زندگی برای ما داشت، سیروس دین‌محمدی، محمد نوازی، فرزاد مجیدی و مهدی هاشمی‌نسب لب ساحل مشغول اسب‌سواری بودند!
🔹
برخی بازیکنان، پس از فیکس‌شدن هادی طباطبایی، با اطلاع از ضعف او در بازی با پا، به هادی پاس‌های رو به عقب می‌دادند!
گفت‌وگوی کامل در یوتیوب
👇
https://youtu.be/vjdbU6MwRxE
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/692251" target="_blank">📅 13:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692250">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
خبرگزاری فرانسه: یک هواپیمای مسافربری ایرانی با وجود تهدیدهای واشنگتن به اعمال تحریم، در چین فرود آمد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/692250" target="_blank">📅 13:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692249">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ez0hkmU8OtKsbVjlAAs7Fwv3SFIIsuxsL783ZshHLtL3K0ad-9Gahe4RB6PCHWEHDL8VlbArXeBYsTnKnlQf0i7LG8T7P_zglW9J7p-dPopiMI_YyHj5gG2z_yDYX1LVKuItfq9Jlr--J19VmxIELoHPlkRjNn0afp4mntvb7oj0nrkXIxqxeetw0CoL_Eb8vXKerEoher7IHiegl_7IKgxGSXwoVEfk3y0DxNyiaRv1HsE4SKplT-zhUaSstYqBaLRJ53oVZoGY4E1roW4iBAJe8x9aR9dV0SBzoitgCCBxSV0eipIqgDADyzIeoeGKmCQtwQsU0Fa0zi1uKwZOWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش میلیادری قیمت ۴ محصول ایران‌خودرو
🔹
قیمت ۴ محصول ایران‌خودرو امروز حداقل ۷۸۰ میلیون افزایش یافت؛ میزان افزایش قیمت هایما 7X به بیش‌از یک میلیارد و ۲۰۰ میلیون تومان رسیده است.
🔹
این افزایش قیمت خودرو درحالی اعلام شده که پیش‌از این ایران‌خودرو توقف تولید محصولات خانوادهٔ هایما را اعلام کرده بود./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/692249" target="_blank">📅 13:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692248">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92ae946ade.mp4?token=X46S9FruG1ZCUx0e7F-7BVt04Ag3ORQRjKuas_sUQjBbZgTrpakyitGF60G3go5uApBFU4_a8xyVObV7jg3gA5u_ZHjNKsOxZVBATftfB_5jw8OzpisjHN_glJN0XD-es4xMIZSNW6Io1SlDsnsnOqrz0mCTwroz4aWjd9W00WxS60azHQH3QMuK87OYrgC4Y-LZ-3UF4g8PBI-d-o8-lQDYpAn1DVNsdwNB24IIP8-HqnFkYLYarEQriBnBkrnYwjBHco-ttt9X-axBJ1MMMcVHYbPW6npHwFYwsY1z7q9InV7-rBgNb1VlNjfmwwl-q95IHyTCti8DoaLgDYC97w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92ae946ade.mp4?token=X46S9FruG1ZCUx0e7F-7BVt04Ag3ORQRjKuas_sUQjBbZgTrpakyitGF60G3go5uApBFU4_a8xyVObV7jg3gA5u_ZHjNKsOxZVBATftfB_5jw8OzpisjHN_glJN0XD-es4xMIZSNW6Io1SlDsnsnOqrz0mCTwroz4aWjd9W00WxS60azHQH3QMuK87OYrgC4Y-LZ-3UF4g8PBI-d-o8-lQDYpAn1DVNsdwNB24IIP8-HqnFkYLYarEQriBnBkrnYwjBHco-ttt9X-axBJ1MMMcVHYbPW6npHwFYwsY1z7q9InV7-rBgNb1VlNjfmwwl-q95IHyTCti8DoaLgDYC97w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک مادران شهدای دانش‌آموز لامرد هنگام به صدا در آمدن زنگ مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/692248" target="_blank">📅 13:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692247">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vys3wZgi3zRyN3uMcpBEvUqMkESvg7xOno9wDB0bVlxd5jDrAaQ8W0W-ZATxm8WRruf7mv18E5djCs3FutWgizYnrM_fwfxTzv5nbHpxuawUCMtTfKtoyGavltYMwbFSi0azfRkcimHJt9XXkyxKJyYHROS48KDP-NQ-7PjEyX7AstqVSs32nMtKLn5ued06Pi2lEOLixJmPQd5O1S-WWo9DAkPnykSLFrO20OsQA38r-93F5ganTq8C1SmYLkgOgiH4FdJ55ceZtAHXUNCaJbgh8NH13jVBlzNBMV9XZoDA_DiftAIaMZFAXZZ5H7QRmaC2oIZJxDj7EuWnx1xxCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایدن مصطفی حمید؛ خلبانی که حلبچه را نجات داد
🔹
خلبان عراقی، ایدن مصطفی حمید، دستور بمباران شیمیایی حلبچه را رد کرد و صدام او را اعدام کرد. پیش از اعدام پرسید: «آیا ملت ایران و کردها سال‌های بعد مرا قهرمان می‌دانند؟»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/692247" target="_blank">📅 13:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692246">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/224b8e6583.mp4?token=k84cIBSrahp3bUqEQH1IIyRAqot_1AlAT-I896NNEaAdzeZdzcQgNZM2fBof9py1EQlVuigKW0iTU-2xsHTvFZW5W8wZUeYDunxt6y2CTJGeJ7WQY7lMIxlXhEO7KmCGfeutHlW6lfuSo47vt3YE_XM6WUa0w1-4i4wUnFfjqcihlyShnP-ROnuwrewesThlZ7Mi2qcqDAP35jkzXG5PqqcFawTkpNr6CILAYRJ4JnowSyPtkV6IHyg9kgAa3qjzzVwqdWrnT3Ht3pE6YCQI0Pp6hWdqDi5OV5WNQBPBHjKDJsvPVCV4uiA1-jQGFkOF_XuzWatBslkiLdyiqQvrMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/224b8e6583.mp4?token=k84cIBSrahp3bUqEQH1IIyRAqot_1AlAT-I896NNEaAdzeZdzcQgNZM2fBof9py1EQlVuigKW0iTU-2xsHTvFZW5W8wZUeYDunxt6y2CTJGeJ7WQY7lMIxlXhEO7KmCGfeutHlW6lfuSo47vt3YE_XM6WUa0w1-4i4wUnFfjqcihlyShnP-ROnuwrewesThlZ7Mi2qcqDAP35jkzXG5PqqcFawTkpNr6CILAYRJ4JnowSyPtkV6IHyg9kgAa3qjzzVwqdWrnT3Ht3pE6YCQI0Pp6hWdqDi5OV5WNQBPBHjKDJsvPVCV4uiA1-jQGFkOF_XuzWatBslkiLdyiqQvrMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو وایرال شده از این معلم که رفته بالاسر دانش آموزش و هرچی آهنگ میخونه بیدار نمیشه
😁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/692246" target="_blank">📅 13:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692245">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
وزیر نیرو: آخرین هدف حملات دشمن زدن آب و برق است؛ دشمن وقتی می‌خواهد خیلی ما را بترساند می‌گوید آب و برق‌تان را می‌زنم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/692245" target="_blank">📅 13:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692244">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff405a16bc.mp4?token=hSyuNpbTj9Wix_MZrhyv60eUWyA2ftI4d0MlN_ce9yTTBuoxAPc3BJqAXYyzHC4QXUTz8oPWfuXsyNQ9Gu-w9hdjRnuhBMjxpmv7w_mR5MZSmarpVrNiw3-LiHJXf-lUigu6SJhPofbgo-EXij8Vz3hSp-i2uyUfEeSNpcNzf0RoxgvJ6TBon26nFHN_Tg2J5W1tYJHvxMZRYKqdbm8HPs1HXP0nbpJwBMZ6ZG5_8qQj6Ijlh5zbqi-z1pVwsarREMUHB88Eisn3bJ9R5cgRYzL9Xtk7iKcGBBGWooWLqxlDI1cQ1bj_WR6WNdJLyyUWoNxmPQv_8wnRWGkPE-jpVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff405a16bc.mp4?token=hSyuNpbTj9Wix_MZrhyv60eUWyA2ftI4d0MlN_ce9yTTBuoxAPc3BJqAXYyzHC4QXUTz8oPWfuXsyNQ9Gu-w9hdjRnuhBMjxpmv7w_mR5MZSmarpVrNiw3-LiHJXf-lUigu6SJhPofbgo-EXij8Vz3hSp-i2uyUfEeSNpcNzf0RoxgvJ6TBon26nFHN_Tg2J5W1tYJHvxMZRYKqdbm8HPs1HXP0nbpJwBMZ6ZG5_8qQj6Ijlh5zbqi-z1pVwsarREMUHB88Eisn3bJ9R5cgRYzL9Xtk7iKcGBBGWooWLqxlDI1cQ1bj_WR6WNdJLyyUWoNxmPQv_8wnRWGkPE-jpVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرفوری ۱۱ ساله شد/از یک رسانه خبری تا شبکه‌ای با بیش از ۸۰۰ رسانه در شبکه‌های اجتماعی داخلی و خارجی/تلویزیون اینترنتی «مدار»و آکادمی «آوید» دو محصول جدید خبرفوری
🔹
امروز سالروز تولد خبرفوری است، از یک مهر ۱۳۹۴ تا امروز...
🔹
خبرفوری در یازدهمین سال فعالیت خود…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/692244" target="_blank">📅 13:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692243">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
فایننشال تایمز: برای نخستین بار، هزینه اجاره یک نفتکش غول‌ پیکر در مسیرهای میان خاورمیانه و آسیا، از روزانه ۱.۲ میلیون دلار فراتر رفته
🔹
حدود ۱۵ درصد از ناوگان جهانی نفتکش‌ها در سواحل عمان منتظر هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/692243" target="_blank">📅 13:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692242">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوهشت - دیده‌بان رشد اقتصادی ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nspDSoC-GbUugv4RUJoqnPPNclK6MjyC6LLpka65AJyhG3q7xxOSnf0Uy4PNprPgSy25WC4nsIpejpa3_pn-X0HuHFjgnRbqyyrvoZVUi5v-hs7ySNVg1Z7VozNqiHnZOhDHJaIE-q9LEGyw3ICnAH1L7wTt66CiEC3ahEjJXivoXQy6vPkzLTVf23SC3p0CZAfdRqboMp_OpixVc2c9G-TxtHgUu1HpgiT_xrFJrxqUMlCSoczqn0SU-4rmuFgRxkHtY0OQqDk7Ge_8tVXpfKo4UCAaTuzDz-O0Mx4DVCbXzFaLrUs4_x_rw6nUXZaJ4DJOk5WMrpGckGu2IThIAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
ارزپاشی یا ذخیره‌سازی؟ درس گرفتن از تجربه موفق روسیه در مدیریت ارزش پول
واکنش عجیب برخی نمایندگان مجلس به اقدام بانک مرکزی
🏦
الویرا نابیولینا، رئیس بانک مرکزی روسیه، پیش از جنگ اوکراین ذخایر ارزی روسیه را
از ۴۴۸ میلیارد دلار در سال ۲۰۱۸، به ۶۳۱ میلیارد دلار در پایان ۲۰۲۱
رساند.
📉
پس از شروع جنگ نیز
مانع ارزپاشی‌ شد
تا نرخ ارز برمبنای عرضه و تقاضای واقعی تعیین شود. ذخایر پس از یک افت موقت در پاییز ۲۰۲۲، ترمیم شدند و
در آگوست ۲۰۲۶ به حدود ۷۶۹ میلیارد دلار
رسیدند.
🧭
با این وجود اخیرا برخی از نمایندگان مجلس ایران با انتقاد از سیاست بانک مرکزی،
خرید ارز و افزایش ذخایر ۴.۵ میلیارد دلاری توسط بانک مرکزی
را زیر سوال برده‌ و معتقدند اقدامی برای جلوگیری از افزایش نرخ ارز انجام نگرفته است.
🛡
باید توجه نمود که اگر بانک مرکزی در این مدت ذخایر ارزی‌اش رو بیشتر نکرده بود،
امروز در اوج محاصره کشور فلج شده بود.
زیرا
سیاست‌ تثبیت
در دوره پیشین،
ذخایر ارزی بانک مرکزی را به تدریج از بین برده
و کشور را با بحران مواجه ساخته بود.
اکوهشت
- دیده‌بان رشد اقتصادی ایران
@ecohasht</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/692242" target="_blank">📅 13:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692241">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b793d049a0.mp4?token=Fp6WRk--ECB7DFipTurdJVBPgPDHATej6TFD59lAmmAHcPB1LeAEDI1MjKA-2XyTXTxbQ5JnOhUrcN-jzIVcoi0HjqkJXZVIehKzRDD1z5OqvwIOaunSOB3-NvE16CBLDTimTnEID5t8zQnOLBOZPx0hPbVdiBLAJQmKUjh3ZVx8mDW3gPI_agk4aR8Js0C8uEcGEeTVyVsI4cogJF4Rr1_RC6jEEziqhDuKt0YZU8yj9xgeKuP8cfNZWGfpzLz-VQ05quPfsahG5S30zEYUzGtiHbdGVqcEt8T3MGtt6qYl2_Ny8u6NBJ_oblnECs6USFTQvRCjouhek4NBAdhCJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b793d049a0.mp4?token=Fp6WRk--ECB7DFipTurdJVBPgPDHATej6TFD59lAmmAHcPB1LeAEDI1MjKA-2XyTXTxbQ5JnOhUrcN-jzIVcoi0HjqkJXZVIehKzRDD1z5OqvwIOaunSOB3-NvE16CBLDTimTnEID5t8zQnOLBOZPx0hPbVdiBLAJQmKUjh3ZVx8mDW3gPI_agk4aR8Js0C8uEcGEeTVyVsI4cogJF4Rr1_RC6jEEziqhDuKt0YZU8yj9xgeKuP8cfNZWGfpzLz-VQ05quPfsahG5S30zEYUzGtiHbdGVqcEt8T3MGtt6qYl2_Ny8u6NBJ_oblnECs6USFTQvRCjouhek4NBAdhCJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر کمتر دیده‌شده زایمان اسب‌دریایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/692241" target="_blank">📅 13:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692238">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKR5Vv7LjB8bS5K3W8zwC56Xyw3w1B8VHuzvrfSd0iK7rfmHDFf9RuHJ8De58pl9rikXKGmwdRet89wyGlbBFhk6gi8lQHsLki0Ig0vS9pLGV1ID0Xe3W55LHBF4pOZtshpP94PyrspjxESKLHZf_R0iEo7RxjnyWJBV3qdAwBW2-Eyj9UdjphgLZudLs30tuxNRsy6HU2u0Bxq6p0TOi-q_JyiTahPeYVQ_8NTuFHw-oCEl8zAOG1RZAPlufgKmd9buZ88Q54ucGpJ1VUm7FgSadn-aipf9p-uOXSz3jEbxmtPygasmUBpApUFxzePnoLbxGPJvwGUdLjdxyNYMTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر آخرالزمانی از پالایشگاه مسکو پس از حملات پهپادی اوکراین
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/692238" target="_blank">📅 13:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692237">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnTHPMB3YmHahuyafkDBmSgL4q7StkpmdQ70QyWk-UzaZ_kHyCJsMauDkBm2CsigQ0iTAJ3Tw4mV6JMDNv54Oa8gz18yYYoQKjl-KoTq8GRJOjzlsVZKV5tAwEVAmzF5s1XhTob7qg0vtvu3KAaGfEF7XGDlUHmW5P4cii-i8hAN4EJAhyzPf9mtjz2lsNWUsVLJQefTlpdGBWNTaAuSutuAfvZUDzk6Xx7OKoFV4qNEWipyoDJPdliCwpDfYuSeLTH1_W93odJEyp3ixqrQwQh75zMU6_oiU65G6ykupdKpq6VDEdtSvvHRK7_f0VJr9w2Am_atovvziEEUjG_OFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صداوسیما: با اصرار نماینده آمریکا دیدار عراقچی با ویتکاف در حاشیه مجمع عمومی برگزار شد
🔹
ابلاغ شروط ایران برای بازگشایی تنگه هرمز دلیل پذیرش درخواست ویتکاف برای این دیدار بوده است.
🔹
مواضع قاطع ایران در این دیدار به نماینده آمریکا ابلاغ شده است.
🔹
رفع فوری…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/692237" target="_blank">📅 13:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692236">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
کانال۱۴ اسرائیل: تعداد بی‌شماری از شهروندان اسرائیلی حاضرند با دستگاه اطلاعاتی ایران همکاری کنند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/692236" target="_blank">📅 13:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692235">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Du1FnXII_pgRhDVW5GBL8gq2dwJRt8ac-N13AmGq1ShR4oO343ublca7nwlK3-3eCWsaNGNIvfxvAWjqHERI1X1j6WVjygY_OAKzp8v6p-mOkjTIveTq-qEP8Q67M5IyoC-QW2fx_X5A4ZB_qzACvDZaGoQzDcFdFL-DJOUfNWPzyq_oc4PXw-7V3oVMhkNAYTtMzWmhhiT4uuUvNJOKHuYdFohugMXWHeKmEIdEAnZSr6CHE88_51mh_KtgIBKCOyBgOD_W70EbF_y4dR7JYx7ATfEmx46SV-6YjAkT4zXPCCOwoNAmKqB53AYOGKSboSeSDNgiGditxLLq0X9aYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضوری که برای فعالان رسانه‌ای و دشمن، نشانه‌هایی معنادار داشت
🔹
حضور معاون علمی رئیس‌جمهور در نخستین روز مهرماه در مدرسه «شجره طیبه» میناب، مورد توجه فعالین رسانه‌ای در شبکه های اجتماعی قرار گرفت.
🔹
حضور نماینده دولت در مدرسه میناب از نگاه فعالین رسانه ای در میانه جنگ معنادار توصیف شده است؛ حضوری که گویا حاوی این پیام است که در برابر حمله به یک نقطه، باید همان نقطه را به عرصه‌ای برای پیشرفت و آینده‌سازی تبدیل کرد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/692235" target="_blank">📅 13:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692234">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
یک گروه هکری با نفوذ به سامانه‌های اداره تحقیقات فدرال آمریکا (FBI)، اطلاعات شخصی هزاران مأمور این نهاد را به دست آورده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/692234" target="_blank">📅 12:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692232">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a72e35c17.mp4?token=Qzpu2fadm6Ic5LbUbH8tEgD5uFbe7YiO0we_0NtxTRavTAJCU73-qvoDJAAlb7uw_Hn-gzuPqTUXqRXFl1qx_pD7w4CUeRuRlieA6gbAizbvk8kL9tdiujxD2GjAAO9q4VYyzLKeM5aR8HV0ybLaxoV6LJREQIZ2hwJS8lq_siVKvcR2QImQmbT3sJ5FdlqynxcuSwRg3OQ80WE9FojZY2fmrBBwJ6G_qNM-47qHyiLmDeqWiPdGREB0rPcVwVQyaRCCyUqOsKd3aF8GKPkpQi-VcZh6gLvbq1Ol-8NyFO7YAgXJ-pX8oSNQRL_ygZKnMtIadRQEtJDQ--3_N2LK1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a72e35c17.mp4?token=Qzpu2fadm6Ic5LbUbH8tEgD5uFbe7YiO0we_0NtxTRavTAJCU73-qvoDJAAlb7uw_Hn-gzuPqTUXqRXFl1qx_pD7w4CUeRuRlieA6gbAizbvk8kL9tdiujxD2GjAAO9q4VYyzLKeM5aR8HV0ybLaxoV6LJREQIZ2hwJS8lq_siVKvcR2QImQmbT3sJ5FdlqynxcuSwRg3OQ80WE9FojZY2fmrBBwJ6G_qNM-47qHyiLmDeqWiPdGREB0rPcVwVQyaRCCyUqOsKd3aF8GKPkpQi-VcZh6gLvbq1Ol-8NyFO7YAgXJ-pX8oSNQRL_ygZKnMtIadRQEtJDQ--3_N2LK1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این تصاویر به وضوح چرخش زمین را به شکلی نشان می‌دهند که در واقعیت اتفاق می‌افتد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/692232" target="_blank">📅 12:53 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

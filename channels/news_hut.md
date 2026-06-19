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
<img src="https://cdn4.telesco.pe/file/ohJkvxcbBl1svpoh22ptzIfbPgMl0XMzaWEmrgsnZJpNTCho_HFgis0_dxAbh3Y2ik5ra_6q4R82w0G5X_lEXfsI6FBzaDDr-iWzY98DJLGisDiRf60yITCO8Y23QuXs07LIvJNJAhJArDVCpDaUtvHmk3xm-IUlIMU6dv5z2Bj6lTU59IOBsdUAQgEpIZabcT234PBD4LTbLb0Kr5lQTqNS169P_I_l8enRSHcgAOfKXvIAHjbYmXeVVyor4C25gJhOrbN7m177UJIN8TcIgIMTu7Lcn52Nefzy8412r1EZdgBPLdI2UKl_zfvwkULqxea8V3CUxtKjJNwF7BZd6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 222K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 19:58:23</div>
<hr>

<div class="tg-post" id="msg-66512">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
نعیم قاسم، دبیرکل حزب‌الله لبنان:«تا زمانی که توان ایستادگی داریم، چرا باید تسلیم شویم؟.»
حزب‌الله خلع سلاح نخواهد شد. این سلاح‌ها برای مقابله با اسرائیل هستند.ما تصمیمی «به سبک کربلا» گرفتیم و این تصمیم همچنان به قوت خود باقی است.
«ما وحدت نیروهای مقاومت را حفظ کرده‌ایم و وحدت جنبش امل، حزب‌الله و سایر نیروها همچنان در کنار ما برقرار است.»
@News_Hut</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/news_hut/66512" target="_blank">📅 19:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66511">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nN_ghPHCScaUhPduIgxmi7xH6sLzf3EPsidTDgP61ievoUb1HBeKyz0B8uIn-uoI7-yAty0OSj6HT0rlYp6xNpSoR4j4rUHXJwtDSBo3Xls6J-gYnrPjGuFWdT5w299cvcvIs1UPdEjdMUO4ZZN5gPSVyVzbKFVzgqHr33Q5EZh2YApmex0CuE9DaCJUX9cpZeI10t8Cvt56j2rpsB91YitakIb0skieW0XhHIAGVpV6RgxqRnI568sehW8lJwi08lc7RIeUfGZcjwkv9CyRvrpDSTSAdAiCDwMVA1pKgqh5ag3i52Ue-Q2TjAaOYb1Zjjick1wM-roqRAc5BnQgYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اتاق جنگ اسرائیل:
رژیم تروریستی ایران از نیروی نیابتی خود، حزب‌الله، برای حمله به اسرائیل استفاده می‌کند، به این امید که بتواند وقتی اسرائیل پاسخ می‌دهد، اسرائیل را به خاطر از مسیر خارج کردن مذاکرات سرزنش کند.
ایالات متحده باید به حمایت از حق اسرائیل برای دفاع از خود در برابر رژیم نسل‌کش ایران و نیروهای نیابتی آن ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/news_hut/66511" target="_blank">📅 19:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66510">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0ea7af18.mp4?token=Mb20T0uqPXDfqVz5-fye3UCzxZ2njVwhFI0zLUXsxk4hb6mwGMTjEFaa2lt8HXrb8HKjm0bfzAbZ3nQQGUtIt9ySFlAqSKNqmEoeIZiUgYLCTvAzdofBcjdk419btM99a2egeRQr4W-LOeYHz7uynqIjk6407FmWxuNny4xoERjfcSiK4YOX7nrHTbIGov5XKS43QVWpeHQhgFGuAQ29c6Bx6usqEGgHtcm1fXNq2TwGLlcT_fAN4XV9SOLo0e7nCZVG7fCVahKXyYX3tnRqpXZSgo0AQp-vJqw_wwdIKXyS4E7mgVtEC8o4xwLafry_lSfe-gKmunT9tGS2EMS42A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0ea7af18.mp4?token=Mb20T0uqPXDfqVz5-fye3UCzxZ2njVwhFI0zLUXsxk4hb6mwGMTjEFaa2lt8HXrb8HKjm0bfzAbZ3nQQGUtIt9ySFlAqSKNqmEoeIZiUgYLCTvAzdofBcjdk419btM99a2egeRQr4W-LOeYHz7uynqIjk6407FmWxuNny4xoERjfcSiK4YOX7nrHTbIGov5XKS43QVWpeHQhgFGuAQ29c6Bx6usqEGgHtcm1fXNq2TwGLlcT_fAN4XV9SOLo0e7nCZVG7fCVahKXyYX3tnRqpXZSgo0AQp-vJqw_wwdIKXyS4E7mgVtEC8o4xwLafry_lSfe-gKmunT9tGS2EMS42A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
«هر مشکلی در خاورمیانه مستقیماً به ایران برمی‌گردد. حزب‌الله؟ ایران. شبه‌نظامیان شیعه که عراق را نابود و تهدید می‌کنند؟ ایران. حماس؟ ایران. حوثی‌ها؟ ایران. اسد که در سوریه مردم را قتل عام می‌کند؟ ایران. این رژیم هزاران هزار نفر را کشته است.»
@News_Hut</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/news_hut/66510" target="_blank">📅 19:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66509">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ak-uId66iN2xxp0L5tlad5apiQkboWY-P-qji-7U_iWkaKvSI68dBFIY98y9DoPZAfUmLZ4wy2eeZeAxYSwakfEKesv7AG74Ic2I34U0fZ9P-Lz4zGE4BDxU9R-Djb7gda2Ejvka1tHA99ZGFaVg20dVtbmfrFJrmSBrCY4kFlZfoAB9bIqxfCaJiK_UynUBc2IGK1-uodBMOGeNDyZ3ZphcsweF4zjn-jGKg7ygKLcojJXdC4lWj9_kDzbBVZ8P-KIfDRv_VbE2BxiUdh6oPA5gTstaP-jT0QnIgE4hB9klzuAVBjsAdwlJoz5fon92dukicvcws2_hPV4_EMC1lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اسرائیل هیوم به ترامپ:
می‌تونستی بزرگ‌ترین رئیس‌جمهور تاریخ باشی، اما شکست خوردی
شما به منافع جهان متمدن ضربه زدی و ممکنه به‌عنوان رئیس‌جمهوری در یادها بمانی که باعث تحقیر آمریکا شد
به اسرائیل خیانت کردی و حالا تمام تحقیرهایی که قبلا باهاش روبه‌رو بودی، کاملا موجه به نظر می‌رسد
@News_Hut</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/news_hut/66509" target="_blank">📅 18:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66508">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ:
ما از روی استیصال پای میز مذاکره نرفته ایم.این ایران بود که از سر استیصال آمد. کارشان تمام شده است!
ما این دوره ۶۰ روزه را تا آخر پیش می‌بریم. آن‌ها هیچ پولی دریافت نخواهند کرد؛ حتی یک سنت هم نه!
@News_Hut</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/news_hut/66508" target="_blank">📅 18:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66507">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c09804d09.mp4?token=v9Rykgkj1E6U8L-_UioBcsx86O_1libQv8AAFuhHfIEnMtmLmhC23H3P1CRSuy8XLciAjG3gKJLYCwURScH_hw18nu-2ChuUy4URhLSwx8dlgI5vtKooYWdvHKytsgcf6Vx6rMLp9HqHtvFCI-iVzQ7OJCzQRI-RFECFcSHLHCh-jBzhWb0yuOVPMLVY43mUibzgjbs1EuvzlfQsp1KIx5xkHm7N6WyDTwXC0P39g8Px2xFyfiRh93lxguOLTkcexvW-qqIY_-zNBjWmhfcz29cxgtnPPpS_1NUZk5kXghsiNKzMjHOTCQfDuxkgvoHWXIAjzA5Xd7H7oitKp_u-gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c09804d09.mp4?token=v9Rykgkj1E6U8L-_UioBcsx86O_1libQv8AAFuhHfIEnMtmLmhC23H3P1CRSuy8XLciAjG3gKJLYCwURScH_hw18nu-2ChuUy4URhLSwx8dlgI5vtKooYWdvHKytsgcf6Vx6rMLp9HqHtvFCI-iVzQ7OJCzQRI-RFECFcSHLHCh-jBzhWb0yuOVPMLVY43mUibzgjbs1EuvzlfQsp1KIx5xkHm7N6WyDTwXC0P39g8Px2xFyfiRh93lxguOLTkcexvW-qqIY_-zNBjWmhfcz29cxgtnPPpS_1NUZk5kXghsiNKzMjHOTCQfDuxkgvoHWXIAjzA5Xd7H7oitKp_u-gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
همانطور که دستور دادم، ارتش اسرائیل با قدرت به ۱۵۰ هدف حزب‌الله در لبنان حمله کرد و ده‌ها تروریست را از بین برد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/66507" target="_blank">📅 18:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66506">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">Live Tennis</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/news_hut/66506" target="_blank">📅 18:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66505">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faa1be6643.mp4?token=YoeyvmIF4KyMeth-KlrcPOSOC9qB_AyY07ieHLYi9k4Z-T7VASrctArWG-dAwps9M53fD51dZPSarGkEdG52RL8FFd8CMYB_a1fGaMMBXejZrYTqCIXaLxsnHR5tm7GnOV95qPcTPdRiNZbLR9tgmM5pwMxaDctobQA2JtqM4I1F5lef7X0I9itXsFeLQ_10yOMpNzDCbKjRhY3Y50n2IHk949qq0NIgAXCCHX0MQF344ae0E-wbSf5dDVgEDsSyFTl-Jicly1kVYB0eU3s2OsSUlxkTuglO-CmnO4D8vpQGwJELrh9ilmX42CZjZoB8XD44tLsTBfbdWFm0gqOIbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faa1be6643.mp4?token=YoeyvmIF4KyMeth-KlrcPOSOC9qB_AyY07ieHLYi9k4Z-T7VASrctArWG-dAwps9M53fD51dZPSarGkEdG52RL8FFd8CMYB_a1fGaMMBXejZrYTqCIXaLxsnHR5tm7GnOV95qPcTPdRiNZbLR9tgmM5pwMxaDctobQA2JtqM4I1F5lef7X0I9itXsFeLQ_10yOMpNzDCbKjRhY3Y50n2IHk949qq0NIgAXCCHX0MQF344ae0E-wbSf5dDVgEDsSyFTl-Jicly1kVYB0eU3s2OsSUlxkTuglO-CmnO4D8vpQGwJELrh9ilmX42CZjZoB8XD44tLsTBfbdWFm0gqOIbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محکم تر بززززن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/66505" target="_blank">📅 18:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66504">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4b87f1a5b.mp4?token=SSnkbtL0Sb-YZ2q6sgKX2PfkYi5GBnP9PAwM0sBbkfIEphY0L8gPBDCfnpXZf3LO21T-AXyJO6ezLV_TBHF9fWmIXFm9zYdRemEjeptXKcU4VgAvn9dbNpdUrCyDtHbiUdEDllKyywuIWMJhWyiGN9BuGoybu24dIpJ1be-9ecyyCAsFw-obYLldt5_1TIGpvqgBkA_YM_L2UL_tllhSBtPX4n7l65BhPDIAeERgg9iV2iHUCmUctTCiO5k5ipKnrpxdXES4fFrhHGhJCVthQepIoFoekzXCFMKyi4uV5ypiBTqXfAboEUsYtbBatSWfRqMMIdW6-sPe0Kt4bNJ1JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4b87f1a5b.mp4?token=SSnkbtL0Sb-YZ2q6sgKX2PfkYi5GBnP9PAwM0sBbkfIEphY0L8gPBDCfnpXZf3LO21T-AXyJO6ezLV_TBHF9fWmIXFm9zYdRemEjeptXKcU4VgAvn9dbNpdUrCyDtHbiUdEDllKyywuIWMJhWyiGN9BuGoybu24dIpJ1be-9ecyyCAsFw-obYLldt5_1TIGpvqgBkA_YM_L2UL_tllhSBtPX4n7l65BhPDIAeERgg9iV2iHUCmUctTCiO5k5ipKnrpxdXES4fFrhHGhJCVthQepIoFoekzXCFMKyi4uV5ypiBTqXfAboEUsYtbBatSWfRqMMIdW6-sPe0Kt4bNJ1JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از لحظه سوخت‌گیری جت های جنگنده F16در حین انجام عملیات گشت زنی بر فراز خاورمیانه.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/66504" target="_blank">📅 17:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66503">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3273d3f5c.mp4?token=By-X3l2s_714Hyg1jLRJNhEK1W9nmZBOGJ3hOtMnP2Rcl0mWOaT95I4XysghdZLeyf6ODFXEkCxrTLxtfdvTo3kFPUbZr2GFHyrVv9qYJL5LGxx_i_spQpxzZ-8MQf6lnzXeeAM_UHD5tk4gIZr4wHSonbPv_qGKClaichVTWKcxMXaPbxAfmE-97HCWZb-vfSDzI1tYL8stxULollMhiE6KGC3E6f5WNdx0PTuL7QQo0JrHG2tusBvMCeq0d86vp-QocGR54mX2SSYCkh5TwkMEe4e4iQ7CbfL89i8cbx5rGYyZvrrFoL9anWDihg_F--A8OSd25HflviukQI_AZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3273d3f5c.mp4?token=By-X3l2s_714Hyg1jLRJNhEK1W9nmZBOGJ3hOtMnP2Rcl0mWOaT95I4XysghdZLeyf6ODFXEkCxrTLxtfdvTo3kFPUbZr2GFHyrVv9qYJL5LGxx_i_spQpxzZ-8MQf6lnzXeeAM_UHD5tk4gIZr4wHSonbPv_qGKClaichVTWKcxMXaPbxAfmE-97HCWZb-vfSDzI1tYL8stxULollMhiE6KGC3E6f5WNdx0PTuL7QQo0JrHG2tusBvMCeq0d86vp-QocGR54mX2SSYCkh5TwkMEe4e4iQ7CbfL89i8cbx5rGYyZvrrFoL9anWDihg_F--A8OSd25HflviukQI_AZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ بعد از نشست G7 پشت سر جرجیا ملونی نخست وزیر ایتالیا گفته:
این زن همش التماس میکرد باهاش عکس بگیرم. حالا جرجیا در جوابش گفته:دروغه، شوکه شده‌‌م. نمی‌دونم چرا ترامپ با متحدانش این‌طور رفتار می‌کنه؟
ولی یک چیز رو به خاطر داشته باش: من و ایتالیا هرگز التماس نمی‌کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/66503" target="_blank">📅 17:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66502">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
سخنگوی ارتش اسرائیل:
منطقه امنیتی در جنوب لبنان ۱۰ کیلومتر امتداد دارد و ما به تقویت نیروهای خود در آنجا ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/66502" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66501">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMRD-t6PBfy7eytlQbbinwERlnBn8nZgo8mdP0zxWMKEbxlkWYBsmBtxEKxD54DPUxri1PzXMf4IR_3mqeyXNTePBMycdrYQRgWzNwDvsSxLLBlxi-o9F0s3_iGWd34xXbprpR9o2ZfHOnJQ18boaDZ-VfLsCpMHJjTko_Or5jIMRzsVzGWx4269eY3H_f2PPsMAbfkPSLhaE27IDrYxBkN6kvqIQphvBMaL70y5f0Mg6rCZis-JuW2WG8S2TPAeXJihKcay9xFTd0DjJw9FirKAwThISaS_w8Ax6vd3mMYETUonLlpUFgmIqhd1bwfVjta3hlcUBChnjUtqyayA1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و حزب‌الله به توافق آتش‌بس جدیدی دست یافته‌اند. حزب‌الله از توقف بمباران اسرائیل و پایبندی به توافق‌های آتش‌بس قبلی خودداری کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/66501" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66500">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxweJoc7pnH1g5r-5om4cwKmhniY6Uv3YjN6yqLTV3gR696-rFvYWjGiLtD-3LQRCHYJAgn3PCEkykrOH0fQweyQqyb1eURMriRk1cWYEXxTrpkq9jsHatAKCHk1Mi7RDHQidIqdzZIdoI3UHucaYiDGA9dVimPC693vmTNbQHdf6PF9hyjEMZgwX4N1lJUNFh09YC1ULXu2ZZG6iRyV8rP171WOhevJv4OoYPBodbBgfC3qG9rcytGpudud2Wx4Bh08Em87ccbI8JMP_Z9sQoEpLIqC0H33OqQBjU0t6XzjtUjTp5vHjSIVu0cTB0FQG4TAo5ZSYf9mWfXa7QPAhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:
یک مقام ارشد آمریکایی به من گفت: اسرائیل و حزب‌الله بر سر آتش‌بس مجدد از ساعت ۴ بعد از ظهر به وقت اسرائیل توافق کرده‌اند. این توافق جدید با میانجیگری آمریکا و قطر پس از مذاکرات با اسرائیل و ایران حاصل شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/66500" target="_blank">📅 16:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66499">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eii3Y-fa_VmtsNkpFOXmBuM8mEUWs9N7B0S_E4thJeZ_10tAuM5maZIyl8PU9ELiC4_Wfo7AmrlXl0RjM7GAMT7K-3MSbMaPvrUeTSrIzVaM1SxeEp3a_7Iu9Gaeqk4CDjyNZU2O0z043OWfY830d8z403_7prJDT8wkIVn8itaYiD7EB8P96_JOSjwtj_0BZYf7W0v9P0b8X7XdqVXF9woFkEn1Wb7mKFjlxxKsNIXAYTHVNvgI1C767qZhPyQu9AggHhcnjO-oDgvY0NL1JVHBdvuwWPkJe3J8F_9YIyxMxmXH4qNWi2IKFxBUaJ6DdV_0mBsHF1_uDIr_-pl_hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما از روی ناچاری ملاقات نکردیم، ایران این کار را کرد. آنها کارشان تمام است! ما 60 روز را بازی خواهیم کرد. آنها نه پولی می‌گیرند، نه ده سنت!
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66499" target="_blank">📅 16:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66498">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECXuZOVxCW1Yaat6htAQNo9MjlERNgFrtfU1ZFgicGtX0W_nvS7vpwBCvVtB27jaLWoKBgCXShWY3PNTcRhMLUboTtwVP2cuHbzXv-Ips50RibgdGy58i85Xe_lN95VgDunsHJkmfG0QLzDZc2VwpknkJDrd1fw9BS4UyWz0UczRJYpokg7NVv6AGoNj_z12FLd9akKOr4LJunFrj5-5rM-JVSlHqFnt_lbe_J4K-zK_qh3TJkiJnpPSIcW_GdMQCM2DzR3aYJ7AxmX3COWDVSXu6Yo7DqFLsED-CohjQo2XNfp7OO-Ep1g4W2DZ432H5ih5cNW8l7YrVE-3t99FNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
این جنگ ایران را تضعیف کرده است! ایران دیگر نه نیروی هوایی دارد، نه نیروی دریایی، نه تجهیزات پدافند هوایی، نه رادار، و تقریباً هیچ چیز دیگری. با این حال، دموکرات‌ها می‌گویند ایران اکنون نسبت به چهار ماه پیش وضعیت بهتری دارد.
می‌توانید تصور کنید که کسی چنین حرفی بزند و از آن جان سالم به در ببرد؟ بعضی‌ها واقعاً تا چه حد می‌توانند احمق باشند؟
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/66498" target="_blank">📅 16:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66497">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
‏اسماعیل بقایی سخنگوی وزارت خارجه:
آمریکا مسئول حملات اسرائیل به لبنان است. جمهوری اسلامی همه تدابیر لازم را برای صیانت از منافع، امنیت و حقوق خود و متحدانش اتخاذ می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/66497" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66496">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXn3S1slJUkjN1nUQxIl_a4ei5ekUsnVC1Px_gvlOtZ83htimbt3GjYDEYOfsIirzvK-0hXEEn0hhTJK85lRPWD2-vZ7U8Cip11Olf7-lysjtQ3Ge4HpiWiefNIIguoSa-BSIj4KrlL9tGqvvs7UMpMW5w16aS8m9xWrSbTcCH2vqBbZ2oQ-ZVZINMJDZChfK9xpw5d6XrPe2DM6N1aRmZEnHg6HjtPcCf47DDGjZoLPlUDFKtMJRZLlk5m_x1eBSkNxvJIPxKHWcN7cVX9TtejNxGPu3L-gBMQiV_Y41GBZtapJQJRGzTC-HxhTLu6Y6CbtQwvncoFDIhF5sfNCKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اینفوگرافی خدمات فعال‌شده پس از رفع اختلال فنی</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/66496" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66495">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec2c7bdfe.mp4?token=d8CteydmpcTPYqg0lPLkVhq5i4Z4W9Kz71FSiCyg1kTXXvPPQuDBtJS5Rwrr_qNmmQ9OEzji58VuweTNX0Gp_DPvXPh1GjHcTAYWcRpw3ybCC1-sUtD-KKoLHeU1lxCzLfVJdBM2aL0PuvqwWUYTK-YNb2W9lSQfFQ70iF7kHSTRhyZS_JtGtvvQu6kIrhAOKaLj4yuV1xW_tFL_pE3zc_iawe4JnSe4jJ_K0uDJzVaG22kbHm1X09oQe0VnkCVuQgTjWG1yiyihx8d56XHn9FwnNFN6t4zKAg0cEahqanepga7q5gVYvdez1ySXNvFolTrtm92ivhCK4c0VvQjcvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec2c7bdfe.mp4?token=d8CteydmpcTPYqg0lPLkVhq5i4Z4W9Kz71FSiCyg1kTXXvPPQuDBtJS5Rwrr_qNmmQ9OEzji58VuweTNX0Gp_DPvXPh1GjHcTAYWcRpw3ybCC1-sUtD-KKoLHeU1lxCzLfVJdBM2aL0PuvqwWUYTK-YNb2W9lSQfFQ70iF7kHSTRhyZS_JtGtvvQu6kIrhAOKaLj4yuV1xW_tFL_pE3zc_iawe4JnSe4jJ_K0uDJzVaG22kbHm1X09oQe0VnkCVuQgTjWG1yiyihx8d56XHn9FwnNFN6t4zKAg0cEahqanepga7q5gVYvdez1ySXNvFolTrtm92ivhCK4c0VvQjcvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران شهر نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/66495" target="_blank">📅 15:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66494">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f017f858a.mp4?token=bRSo0VrTI8_HKg6jMWq0B8XyUQGApQUcHuX6lV7Gy04_KR2zx8BeUxpt2jrNEMAP5nVhWqwdPXQ7wvw0cgMTv7FUXaZWFl0nzRDS67iGZ9Ajb-3yDpgRHhzH2FTxYPAoqgTMgBhWLi13CEwzwQztGp5mPxcDWnSNyZ3WGMaOAlIp_tH3Lrp6uE1AePSTnc1hzAN22RQPqJq-awnjVhiZ4SpJz3mQ7KJ82R76EdHxKyeivafayfhDuRckaz2WEBxXF2yWkNCq8rKqDx27YQh0cbnbpPL-sp3neaotOyaHDIKYhiGiw-Ix_esQYBcYs9troU9O4_DCJDTCtJJ-M-ca7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f017f858a.mp4?token=bRSo0VrTI8_HKg6jMWq0B8XyUQGApQUcHuX6lV7Gy04_KR2zx8BeUxpt2jrNEMAP5nVhWqwdPXQ7wvw0cgMTv7FUXaZWFl0nzRDS67iGZ9Ajb-3yDpgRHhzH2FTxYPAoqgTMgBhWLi13CEwzwQztGp5mPxcDWnSNyZ3WGMaOAlIp_tH3Lrp6uE1AePSTnc1hzAN22RQPqJq-awnjVhiZ4SpJz3mQ7KJ82R76EdHxKyeivafayfhDuRckaz2WEBxXF2yWkNCq8rKqDx27YQh0cbnbpPL-sp3neaotOyaHDIKYhiGiw-Ix_esQYBcYs9troU9O4_DCJDTCtJJ-M-ca7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آیا می‌توانید جلوی حملهٔ اسرائیل به لبنان را بگیرید؟
ترامپ: «بله. آن‌ها احترام زیادی برای من قائل هستند و هر چه بگویم انجام می‌دهند.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/66494" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66493">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66493" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/66493" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66492">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aS2Kh5Xengf6MSG09GggYGDaIdLMT-CprxpsugsVICc-f36tueEm0NII2iBw40xP4qkVrzObtgYZQwC3C25zqvQQuGLM-TVhzsNqCT5p3cpUpIzcgQJu43zHI2MZsHBpox5QhuIfgT6GD9uF16htyUzOdseg3xteID9KkcWQxTmZ9XrdIgU_iYHgGqqU8yRnjiOWEyK-1FViW7AvDb9kEpm_9spWhiR9EdZ3oSlAuhzm1RH0R5LyIP3QzCk4Tbs8TZ-iUL2vmgX3cAwuuMEY_sLw89mNysI29CZK1M7DX-TKz2UrgpvWBKovl-iSteB-eKKYI1CaSo64Fi6naTAa-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/66492" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66491">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUtTHPCXzgDKFClzap6awfBgD8Zi8yZuDY95Zb-UB3GVfMkr3rh1P5mhnWevSxCEbwEHhfvkj1mk3U5Jd2_i3ArbyeQlhxbzxZQAnnYMGz0b4NeEsLN80O2595UEBZxe-4-qjGHtBEbmDBoBej4K9G4OsL3HqnI4hktCUQ3d9tTp-9Oqq-KM92QGhLTVkVNzolrtwIXmBE8yopjcEtoPStGsp0dsfsruw5zs_S-QpBxEP0M34GCYYBjXgB4OuKd8AfDiI7cTGCIR6S4Z2sXDTQOEg_m3lY0b3SpWo61spy1A7TeapGvrO-WuJie0_-xJhpjQHN58gNeIJ96mA72mlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به فارسی؛نخست وزیر نتانیاهو:
پس از حمله جنایتکارانه حزب‌الله که نقض آشکار آتش‌بس است، دیشب به ارتش اسرائیل دستور دادم که با قدرت به حزب‌الله حمله کند.
ارتش اسرائیل به بیش از ۸۰ هدف تروریستی حمله کرد و ده‌ها تروریست را از بین برد. متعاقباً، ارتش اسرائیل امروز صبح به مقر حزب‌الله در بقاع حمله کرد.
امروز صبح با وزیر دفاع و رئیس ستاد کل، ارزیابی وضعیت را انجام دادم.
دستور من واضح است: اسرائیل حمله به سربازان یا خاک ما را تحمل نخواهد کرد و بهای بسیار سنگینی را برای این حملات از حزب‌الله خواهد گرفت.
ارتش اسرائیل برای خنثی کردن هرگونه تهدیدی علیه نیروها و خاک ما اقدام خواهد کرد.
همانطور که به صراحت تاکید کردم: اسرائیل تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان باقی خواهد ماند تا از شهرهای شمالی محافظت کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66491" target="_blank">📅 15:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66490">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc6524eaa.mp4?token=nktxYXhfu6TIoiH4f-mcTsvXefXq00RtTggsCI5dPcTtS_JJIpp1y_3A9RVqSZi96YzeW7QDoNABuK2dQX4QNcS1Zlx-5-UCKDU1tJ0gyioJfnQcMvB3NeAKNOGOye6lfB8gFyyQlCWZLyVM1qPIpKQnwZXDhfUPRQFpnstxsTC8aVb7MBYZi3Ke4uBeCuA9rqrGtkwn1XzZUDVMakDphB-fsEXSN6V6qLI6hEEfnlvqnK-2YDSBs93z-SiZr-liQyPt_yLaiK4lgp4daIzHnD89no-jECTFphWPqW5qRP5eKl1q7eTPM8ZVxAeajfn9iMo7VdaeyCMycEH60PpTeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc6524eaa.mp4?token=nktxYXhfu6TIoiH4f-mcTsvXefXq00RtTggsCI5dPcTtS_JJIpp1y_3A9RVqSZi96YzeW7QDoNABuK2dQX4QNcS1Zlx-5-UCKDU1tJ0gyioJfnQcMvB3NeAKNOGOye6lfB8gFyyQlCWZLyVM1qPIpKQnwZXDhfUPRQFpnstxsTC8aVb7MBYZi3Ke4uBeCuA9rqrGtkwn1XzZUDVMakDphB-fsEXSN6V6qLI6hEEfnlvqnK-2YDSBs93z-SiZr-liQyPt_yLaiK4lgp4daIzHnD89no-jECTFphWPqW5qRP5eKl1q7eTPM8ZVxAeajfn9iMo7VdaeyCMycEH60PpTeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.  @News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66490" target="_blank">📅 15:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66489">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71570c04a1.mp4?token=F4puQ8JQ2W1G1SLCyAaxRkrRub6LQdIy13i2MZEl3HOMNS5xYvmkiDxzhlvVSIK4_SoVIyewOvHbcWbQwHed84lJFFq5QF_POMOVhHtP4Eo_Dp3a4TJCQA0pSnWcp2yVrf1Js91t09xH3p14jogZMftxIYksW9Lg6ulNwmZdtvgzeXCBdgKrrtMm0RGNP6ACHO-Z4hTRLycJYLp5w4_dNNIhu5uk4gkU-niHYpv7PRjI1jR9tIN573t4Rh2P3bmldUKuiLKsydrXSyinu3i61-DYCX0G4IAQ-NYMI_36teE2iaYLj4xc_wVQg-bL4_M_i81Ldvxu3STNlSFS8FKr1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71570c04a1.mp4?token=F4puQ8JQ2W1G1SLCyAaxRkrRub6LQdIy13i2MZEl3HOMNS5xYvmkiDxzhlvVSIK4_SoVIyewOvHbcWbQwHed84lJFFq5QF_POMOVhHtP4Eo_Dp3a4TJCQA0pSnWcp2yVrf1Js91t09xH3p14jogZMftxIYksW9Lg6ulNwmZdtvgzeXCBdgKrrtMm0RGNP6ACHO-Z4hTRLycJYLp5w4_dNNIhu5uk4gkU-niHYpv7PRjI1jR9tIN573t4Rh2P3bmldUKuiLKsydrXSyinu3i61-DYCX0G4IAQ-NYMI_36teE2iaYLj4xc_wVQg-bL4_M_i81Ldvxu3STNlSFS8FKr1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66489" target="_blank">📅 15:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66488">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3bba52e8.mp4?token=fTf0RYRyb0b-0E3p552dst6vMNhrQsGJK46AD8YfFsDl3AO9dYivr4vcUiLV-5JFzxqPkFV91nXO81VRsdX3nbfVr12MWTp3voR3tNzcTrfjXlY3WQ4O81H6RY3IlI4PkyCy7IVFg6ZeC7c-L5ifp66xrJW8xErZbkjwI3pFrVWlKHmlEVLoESnvUaVAve7AgD7EMR6z2rkqeVbZLhrbl6NcZosYn4aP7f26GCzdlTEJTxvxVYiDUbzgsOWpGDrCfyIxH6F-WYDIKfe9CL0LfWK7syIgereJ-vS13QbMSPm1EchzehtPQbjmJnPiWUdC7sshostlYWh2hegrsAGeIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3bba52e8.mp4?token=fTf0RYRyb0b-0E3p552dst6vMNhrQsGJK46AD8YfFsDl3AO9dYivr4vcUiLV-5JFzxqPkFV91nXO81VRsdX3nbfVr12MWTp3voR3tNzcTrfjXlY3WQ4O81H6RY3IlI4PkyCy7IVFg6ZeC7c-L5ifp66xrJW8xErZbkjwI3pFrVWlKHmlEVLoESnvUaVAve7AgD7EMR6z2rkqeVbZLhrbl6NcZosYn4aP7f26GCzdlTEJTxvxVYiDUbzgsOWpGDrCfyIxH6F-WYDIKfe9CL0LfWK7syIgereJ-vS13QbMSPm1EchzehtPQbjmJnPiWUdC7sshostlYWh2hegrsAGeIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
هم‌اکنون سپاه در بیسیم کانال ۱۶ دریایی.
“از آنجا که خروج اسرائیل از لبنان و لغو کامل محاصره دریایی و خروج نیروهای تروریستی آمریکایی از خلیج فارس و منطقه از جمله شرایط اصلی توافق بین ایران و ایالات متحده است. تنگه هرمز تا زمان تحقق این دو شرط بسته خواهد ماند، به همه کشتی‌ها دستور داده شده برای امنیت و سلامت خود به تنگه هرمز نزدیک نشود، هر شناوری که از این دستور سرپیچی کند مورد هدف قرار خواهد گرفت.”
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66488" target="_blank">📅 14:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66487">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
مرندی عضو تیم مذاکرات :
ترامپ بار دیگر ثابت کرد به تعهداتش پایبند نیست.
رژیم صهیونیستی مجازات میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66487" target="_blank">📅 14:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66485">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شعارهای دیشب مداح حکومتی در مراسم محرم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66485" target="_blank">📅 14:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66484">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddac5fcdb8.mp4?token=RaImOcdQDr1V95ZSP8bZkYvgJ5X5BSKMiJ_GYkD8rjDdPSqtmcYSDvxyl5P95TeDKLzot0_V8bcJ6gaGZKUGL5vGnBFAMLJG8c6OayGVmPcNGLaO4SuDr-oIcOVaksKCs0VTENdwQ5fy5Ta24g38B6lWausJZEx2Gtor-L6aO9v7AF-R4C-rBwLjz2HmxIDVqNCs4olmNCaGl_MVXfTvr7wapSREsZ4qhzfZFCSuWWROKDZ3JWNZSolELiggddSG1O54WajiIASZ0CcgzYAc9xX1DDK1gA-hXrFLbUSqUI8nd-A-kZp6xoAgSx9XU-vAP5gv2eBSk5Cc8leIyDEEdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddac5fcdb8.mp4?token=RaImOcdQDr1V95ZSP8bZkYvgJ5X5BSKMiJ_GYkD8rjDdPSqtmcYSDvxyl5P95TeDKLzot0_V8bcJ6gaGZKUGL5vGnBFAMLJG8c6OayGVmPcNGLaO4SuDr-oIcOVaksKCs0VTENdwQ5fy5Ta24g38B6lWausJZEx2Gtor-L6aO9v7AF-R4C-rBwLjz2HmxIDVqNCs4olmNCaGl_MVXfTvr7wapSREsZ4qhzfZFCSuWWROKDZ3JWNZSolELiggddSG1O54WajiIASZ0CcgzYAc9xX1DDK1gA-hXrFLbUSqUI8nd-A-kZp6xoAgSx9XU-vAP5gv2eBSk5Cc8leIyDEEdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکی در مراسم اعطای مدال هرکاری کرد نتونست گیره مدال رو بندازه داخل و گفت میخوام یک مدل دیگه برات ببندم و مدال رو گره زد و نزدیک بود طرف رو خفه کنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66484" target="_blank">📅 13:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66483">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
‼️
وزیر خارجه پاکستان: مذاکرات سوئیس بدلیل مشغله کاری مسئولان ایرانی در ایام محرم به تعویق افتاد
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66483" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66482">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd02588050.mp4?token=vNZuFwFvAceRQ_sBAn2CeTktCJpdh8FxFGKL8X0RBJdRlbPp4Pi_brrfKIUPFgoBegaYfSJWnA72Aor6HVUxdnQqqY99V8wPHhyuZtaU4B2dwhWreSVWtahFdYeQwbUAgNneqjJQVODwNj9WO7AdsKybIa-xwdk0aw9-cqdLPLPRq0bw2U2CMWe5tNqNTs2u5E8tUKYrhq01F5-GRrMuOVOXuojtDGBcSFJBdToUztfncDMuxWSKB4AoXh6bY5aXGkQBQ0jmj30uaTBwOJSCwuueBeIaod2CahmGvFeN6dxidXwKNLsaBvNC4vVF2VDTuDjHtjEum1X1v4bAoreTNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd02588050.mp4?token=vNZuFwFvAceRQ_sBAn2CeTktCJpdh8FxFGKL8X0RBJdRlbPp4Pi_brrfKIUPFgoBegaYfSJWnA72Aor6HVUxdnQqqY99V8wPHhyuZtaU4B2dwhWreSVWtahFdYeQwbUAgNneqjJQVODwNj9WO7AdsKybIa-xwdk0aw9-cqdLPLPRq0bw2U2CMWe5tNqNTs2u5E8tUKYrhq01F5-GRrMuOVOXuojtDGBcSFJBdToUztfncDMuxWSKB4AoXh6bY5aXGkQBQ0jmj30uaTBwOJSCwuueBeIaod2CahmGvFeN6dxidXwKNLsaBvNC4vVF2VDTuDjHtjEum1X1v4bAoreTNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلاش سربازان روس برای سرنگونی پهبادها
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66482" target="_blank">📅 13:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66481">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d70873ad.mp4?token=feHelQH-GAmRFJRYqIheBm6gqiErdn10ZHzwfpK7Zv-RJiF-Eeo9EFSm2psjvt1QynRhXkd4sNsse1cyYFqccshy1TaWU3ldqnD2iPTpiEn3T-sgV23_rHRR_kxpMaY4-9K47M17f89aqTxs558cepw8tkxCpEer_jQMArBjMBcOFPPuG-WRP6vhGlIxap3Oc-TWaBoEkrYsu6j-F0VmnzhfCaHvZO2ScCpTbbZ_WQczMVLjYGNHv2SBY-a8sljq-dlBB8X_9IBNsAcwdb9k22s7IjYyhVmdPZmghx07wHg1nxUauJYTAWXyQGDOOaPe5zmKzyclPOX7qwb5ppsScg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d70873ad.mp4?token=feHelQH-GAmRFJRYqIheBm6gqiErdn10ZHzwfpK7Zv-RJiF-Eeo9EFSm2psjvt1QynRhXkd4sNsse1cyYFqccshy1TaWU3ldqnD2iPTpiEn3T-sgV23_rHRR_kxpMaY4-9K47M17f89aqTxs558cepw8tkxCpEer_jQMArBjMBcOFPPuG-WRP6vhGlIxap3Oc-TWaBoEkrYsu6j-F0VmnzhfCaHvZO2ScCpTbbZ_WQczMVLjYGNHv2SBY-a8sljq-dlBB8X_9IBNsAcwdb9k22s7IjYyhVmdPZmghx07wHg1nxUauJYTAWXyQGDOOaPe5zmKzyclPOX7qwb5ppsScg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتز، وزیر دفاع اسرائیل، درباره سوریه:
ما آنجا می‌جنگیم. ما به الجولانی نیاز نداریم. الجولانی، تروریست کت و شلواری، نیازی ندارد که بیاید و به ما کمک کند.
ما سوریه را خوب می‌شناسیم. او قرار نیست در لبنان به ما کمک کند. او باید در سوریه بماند، در کار ما دخالت نکند و ما را مجبور به دخالت در کار خود نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66481" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66480">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15d1aff21.mp4?token=u-6TnmKW1bn8sUlOZQ0OWmewyXxD_qeuhcJuhU1zKvrlk201_ewJFKNfA7cv6eGn8LSMCLwcUKd2SnGCqwUasqmP1QzqBWLOY7UtOONgpd7Ji0EeO422h_6sB8TbOmpGjGUxtTK0kDN3I5bEpmDqp9_xnKjH8gn6AsoTUU3lbQr1Q0Sy4gJ5QNXlYAdfZfo5E3F5k_fmVQ2lD4Mt_b4gYoInyS5TLq-13O48OARIZRygFaiMA-RJZUk19wQtqhaKoAnEnUth5Bd4rE5YIkhig8iT-kLJqJ00y7ZgKbAvnoTHuC9QOdtuwkI9sQELwaOsTxb3E1V7Wyfd8EwJVFKZrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15d1aff21.mp4?token=u-6TnmKW1bn8sUlOZQ0OWmewyXxD_qeuhcJuhU1zKvrlk201_ewJFKNfA7cv6eGn8LSMCLwcUKd2SnGCqwUasqmP1QzqBWLOY7UtOONgpd7Ji0EeO422h_6sB8TbOmpGjGUxtTK0kDN3I5bEpmDqp9_xnKjH8gn6AsoTUU3lbQr1Q0Sy4gJ5QNXlYAdfZfo5E3F5k_fmVQ2lD4Mt_b4gYoInyS5TLq-13O48OARIZRygFaiMA-RJZUk19wQtqhaKoAnEnUth5Bd4rE5YIkhig8iT-kLJqJ00y7ZgKbAvnoTHuC9QOdtuwkI9sQELwaOsTxb3E1V7Wyfd8EwJVFKZrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حملات گسترده ارتش اسرائیل به مواضع حزب‌الله
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66480" target="_blank">📅 12:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66479">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae8db95bdf.mp4?token=SfEg6Vj54argJz21lxQGYDKm5qoThN3VhsTjA81fiaegLqRgVY78uf76oEPHK3CTo7ObyIUX2b2YLlIzh6NrX8077D-yJMDM60lo_AtDW7t0nAJKF0_WAWt-Xskedt6ZZ1h00eizCX0VE6-_aSJYD9YBRu_3kBBqaC9FPeorx3JKeVZTtz6fp5m2xbi4QvC7HPs7M2j_Z8yCatR6G2SvOR4ooYx26n2q0jtr7V5scYCxniOA7OiarAxk3k1Q97x2FgboDY63M6USapN38P9wrP2SDRaTl7X5nXvIcxVAk-jpB-fvk2aXna8Y4qs1JrSTybqfe5lsurkHGs0I_eNGTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae8db95bdf.mp4?token=SfEg6Vj54argJz21lxQGYDKm5qoThN3VhsTjA81fiaegLqRgVY78uf76oEPHK3CTo7ObyIUX2b2YLlIzh6NrX8077D-yJMDM60lo_AtDW7t0nAJKF0_WAWt-Xskedt6ZZ1h00eizCX0VE6-_aSJYD9YBRu_3kBBqaC9FPeorx3JKeVZTtz6fp5m2xbi4QvC7HPs7M2j_Z8yCatR6G2SvOR4ooYx26n2q0jtr7V5scYCxniOA7OiarAxk3k1Q97x2FgboDY63M6USapN38P9wrP2SDRaTl7X5nXvIcxVAk-jpB-fvk2aXna8Y4qs1JrSTybqfe5lsurkHGs0I_eNGTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر دفاع اسرائیل:
ارتش اسرائیل باید در آن سوی مرز، فراتر از مرز، از کشور اسرائیل در برابر سازمان‌های جهادی در لبنان، سوریه و غزه دفاع کند.
ما از «مناطق امنیتی» حرکت نخواهیم کرد، نه در سوریه، نه در غزه و نه در لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66479" target="_blank">📅 12:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66478">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CP0mXxq-mh6HmZ9mwa-hd36tMFUr1BFIOibHb7H7BrEyNkxa8bCEN851-2fqMxlqfNkGHEGfA9CbETvHVSnlOLBUhu4n98nGCBadSq3pTLxY5W-c34dIxN9M4lRipgW4Hz4aZTp_t5x6kpQYT1a4glLFGFKGlC-cYn7phGGHHsJ9jwo0RDtkkTDNMS-2wGVFdrTy-R_QiMMJd3i3sC_UXAiyVtEwiEUZVsexLk5Q-0uOcS-gZzhu78nJDd5xNftohH_Dlk77uo9B50FnYXIbAk9R1MwKUX8UbVShI-X0KWYzC0rw3S9grnvHOR_gVQMyshmF1GrV_6bUGiNe0pcE_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
گوش‌بفرمانیم، وظیفهٔ محول‌شده به ما توسط مقام معظم رهبری پیگیری تحقق شروط و بندهای تفاهم است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66478" target="_blank">📅 12:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66477">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=DILODUinwVd05yzzmsx9mFNWaRx-tDRd7grFsWign4kR4yr8FC30PUSaRlBdODffrzv82Pcs1ooT_j5Ji1pt6NaOMZTejTVsI9Sv-Bjr5n--vp1uXWg8U9HRHcauLSbdEcZNXV2_Ipah4qPp614o3W8AGtlZPTCd_k_wSzUdn3z0E3_LpvWFEHpohk_PHPFSXBo45kkYgZxpvplRDQ69mk6zDi5cAsoAooEX8AwxCjxLp0VIbzZg1olqss0XoiyJ3RwMFHKb40zPE-V-L78SyWNfdarDyMqzH-gNsFdE2EoXPkFLF1hOG-Ih7sbYVD41xnkx7ul12XjsbJK8M4FxAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=DILODUinwVd05yzzmsx9mFNWaRx-tDRd7grFsWign4kR4yr8FC30PUSaRlBdODffrzv82Pcs1ooT_j5Ji1pt6NaOMZTejTVsI9Sv-Bjr5n--vp1uXWg8U9HRHcauLSbdEcZNXV2_Ipah4qPp614o3W8AGtlZPTCd_k_wSzUdn3z0E3_LpvWFEHpohk_PHPFSXBo45kkYgZxpvplRDQ69mk6zDi5cAsoAooEX8AwxCjxLp0VIbzZg1olqss0XoiyJ3RwMFHKb40zPE-V-L78SyWNfdarDyMqzH-gNsFdE2EoXPkFLF1hOG-Ih7sbYVD41xnkx7ul12XjsbJK8M4FxAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بمباران شدید نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66477" target="_blank">📅 12:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66476">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cbfc5535.mp4?token=emBp60vION6caVBd3ctRwY_smK0NU6TaJhW0VI_C1RdmRUtk9FU0ryTAgHTwL6VHJ0i80wbdmBqoPzophXkCMEDodtlciD7e8BRq90awlltv46qaQv5TZHSr-x8ZEguTAVy9pW-Bim8BFZ9WTAedROd7HEwKWqis9X0vs206fksVkiTZXZDiEUcEFmCf9W6HI9SqfFff7Y7KltXE7YrlemyFGC11AwKBktwaunV7UZpXMKejVIlSczE28DSBSzCdwpOYJHatD2p3tE5n78zObtBqLFMg2L6SAxg3sfiUOKwMtZq9xFm0XZ9QneYGosFqzzZUM2T3oo2KbmQ3lXi_5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cbfc5535.mp4?token=emBp60vION6caVBd3ctRwY_smK0NU6TaJhW0VI_C1RdmRUtk9FU0ryTAgHTwL6VHJ0i80wbdmBqoPzophXkCMEDodtlciD7e8BRq90awlltv46qaQv5TZHSr-x8ZEguTAVy9pW-Bim8BFZ9WTAedROd7HEwKWqis9X0vs206fksVkiTZXZDiEUcEFmCf9W6HI9SqfFff7Y7KltXE7YrlemyFGC11AwKBktwaunV7UZpXMKejVIlSczE28DSBSzCdwpOYJHatD2p3tE5n78zObtBqLFMg2L6SAxg3sfiUOKwMtZq9xFm0XZ9QneYGosFqzzZUM2T3oo2KbmQ3lXi_5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتس، وزیر جنگ اسرائیل:«حتی اگر ترامپ چیز دیگری بگوید، هیچ‌کس نمی‌تواند به ما بگوید چه کار کنیم و ما قبلاً این را ثابت کرده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66476" target="_blank">📅 12:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66474">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba86fa7681.mp4?token=Ad8G5iQRHfKX0fBQp1ZT12cQbYywwG9tHvrM3EksFGSd-tWsc4wwAKENTT5YhwwM8tACzaUe1aNUAIagXWiva5R2rdoKtg4pcry_8UpHU3bjxMBaLjuh6gHzYpvNDGejLNCTtA7bfQZR94SXkj3wUZ8eupy1gAWeuLZ8nDhTGIaxXgGgs9pC-0z4RLFpnnNgVAUzN151VHJ8Je80QcC6Bx9S1vDt7R_keP0D_f8vI6rE9Qz-9V4ShTeERgn8PM4rF8shzgKXO-f0ppi5mNRjenASlG-pdhL-aNMxsiD3Hd7neWCjtXE9pGP3uGK1kkLijETujv6pICqQMsAMYa6w2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba86fa7681.mp4?token=Ad8G5iQRHfKX0fBQp1ZT12cQbYywwG9tHvrM3EksFGSd-tWsc4wwAKENTT5YhwwM8tACzaUe1aNUAIagXWiva5R2rdoKtg4pcry_8UpHU3bjxMBaLjuh6gHzYpvNDGejLNCTtA7bfQZR94SXkj3wUZ8eupy1gAWeuLZ8nDhTGIaxXgGgs9pC-0z4RLFpnnNgVAUzN151VHJ8Je80QcC6Bx9S1vDt7R_keP0D_f8vI6rE9Qz-9V4ShTeERgn8PM4rF8shzgKXO-f0ppi5mNRjenASlG-pdhL-aNMxsiD3Hd7neWCjtXE9pGP3uGK1kkLijETujv6pICqQMsAMYa6w2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی شبا میری اعتراضات و روزا میری راهپیمایی:
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66474" target="_blank">📅 12:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66473">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc0be5a6ce.mp4?token=ZhYx6GFzCejrHVEgeGTl_1qBdOhItW8CWazyey9sv89yshU0m7c3MGDIcr4RmSent_7ETBsS1RPbaJ9h5C-KKeVGDolrBAcA_Ias0W3uMQ_68sV_R3yns7PZKQR02IUk4oiKtbucSxYd6fNRAldkyjU5vx14oTDA3b8hdjyxtf_S223FhWTtNxIFgm-6DZOCuzj8mk3C1aYDgcOwzG569I98B1O0lT22SiGuoc3aSEptuOp245ytdx004MRsADtGqcsY1Q8ijtBGKnCTIjs5v2SyNp7F4L95wZNrDittP_3Gh5iPXvz78RyJ8x3433vECuBJJlIAUArW64Segk3RLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc0be5a6ce.mp4?token=ZhYx6GFzCejrHVEgeGTl_1qBdOhItW8CWazyey9sv89yshU0m7c3MGDIcr4RmSent_7ETBsS1RPbaJ9h5C-KKeVGDolrBAcA_Ias0W3uMQ_68sV_R3yns7PZKQR02IUk4oiKtbucSxYd6fNRAldkyjU5vx14oTDA3b8hdjyxtf_S223FhWTtNxIFgm-6DZOCuzj8mk3C1aYDgcOwzG569I98B1O0lT22SiGuoc3aSEptuOp245ytdx004MRsADtGqcsY1Q8ijtBGKnCTIjs5v2SyNp7F4L95wZNrDittP_3Gh5iPXvz78RyJ8x3433vECuBJJlIAUArW64Segk3RLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نبوغ اوکراینی ها در شکار پهباد
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66473" target="_blank">📅 11:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66469">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOTFx0uOfi-SaXMivfxyylHFToEcJ2XDKzeLHMYS43aa5ypbL1ad1WIR59Pi57KspoQWCxOiaeuwGcG5Mio_8B6cBLCz0A6VcocQmOpCpmLWM1M6HejORFZ1S8ykUNXssp-JF3ZsNUool7M66akugPwfvt_EmQsvc1gHzdvVD5b6hQQBltKhVSFsb9uOnANPX8heHqJhm8UfMd5U9KB-UnPjLnObtNHvm5PJA-INN6TwucTDIwopvOvaDSfSEj5KNs4V0qYt-_45pIlE3JL5gU59eOFHcCFwfG1wR4N6OBC8uuennM6gwkiz7YPkPTlFy6CKQc5wRUWnRwYKSGo0Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t93V6j_buzmEiid7DXcfqKo5sKkLWADHoiIdUYtz0NcOWLlJQDHTjMBSu_BdYaE2-3N-EWD3ZnqEkmC8ecgnQfGVBvlXyjfNWOy5JiJNap4bNC1ws8aNukWiZKbJbOkrPVfgIwQLGjRW9d5nzW-6eHqZvXAmDbdlmcX0V2AVJqSMeslpSKxassJeMsCfybHxdTMBDiSDUNG_gRmXLS-93Zja4CVWBCRRIXeVaUEdqd9kH4Yxpt2GHqGkJcK-mgIfJvQw7I_2SMjNIl-A6lVGHIM7Z6YXO47LxkXcDaXBeaIUJJIJX42OjqRZ9ilRic3oAHwo5gHtPYnwQin2BjK_xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ijPG1KP2M0w9FH5lvQGqhkV4qPmtG6XVxuJONEFXl3IM0-w7gtLcujXwBg6__TWyI9SCGtzwX2r8iWBVIGnUsMgOdR122AKQUUCH33W4icnpK6_s23I2MzPJOmnRxd_JEHMDIqaPOTP5m0KXVqDu06XvFxOtQaYt_N6umHKrsX-l3ouZgX6BMIBk2ZYeKZ6TGWw9qZY3RIvMozCT-PjmbrvROvdoAay94tfCPStslh-YDu-lZxxI1GmmdJ41M6XgYDYJ_XDXxcS7H-9jZlFXF9l_WbK5BuZ5jKvsfq02nwZ3Jii7bcv7Bwc_bICv6abKtOi8HtHhlItuAwrZP5RmZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cb0e601ac.mp4?token=nX1Ns7ATP3vTYGrigATFOEZ7gUOSkE2_FCjl5OlZgRtefVHU80tmBdNAWIKgHf8C_cEcY-CYFmdVuiKiurIMlo2Rn8GJlSfnCfiiL1sS9ISDh_vRiL_qhJvezgmTVEm7wue4-TwVbf75n4hlRgXHuPzRI2S6rxVBYHMfgC2zVJjJd6c6Gubt6e__7SwP8Qj-lPYubqLUepgrNQO6i9EG_2vnehJx5p-jNgi0hPHpPdO5p7yPr646pyaSSAeAb_uuGz_M7jaXlQfRyrEVUYfrw9Kns9Tq7Jv20oWQ4lNg46Z83EVeFY5uC3-DJ2Eu88m5rzangHOsV5vS49Sfl1umwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cb0e601ac.mp4?token=nX1Ns7ATP3vTYGrigATFOEZ7gUOSkE2_FCjl5OlZgRtefVHU80tmBdNAWIKgHf8C_cEcY-CYFmdVuiKiurIMlo2Rn8GJlSfnCfiiL1sS9ISDh_vRiL_qhJvezgmTVEm7wue4-TwVbf75n4hlRgXHuPzRI2S6rxVBYHMfgC2zVJjJd6c6Gubt6e__7SwP8Qj-lPYubqLUepgrNQO6i9EG_2vnehJx5p-jNgi0hPHpPdO5p7yPr646pyaSSAeAb_uuGz_M7jaXlQfRyrEVUYfrw9Kns9Tq7Jv20oWQ4lNg46Z83EVeFY5uC3-DJ2Eu88m5rzangHOsV5vS49Sfl1umwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات ارتش اسرائیل به نقاط مختلف در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66469" target="_blank">📅 11:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66468">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6XZHXZdOIuPYqOAnOnkrTogPNb129W3YjSTpH4ZRnSkdazRCPc0ijrnOJ-0f6Rdmy3Ftpr6Zc7Rx_4xbGdszRSTegbuWVS3Z1XaRvYsop0gH4xv2bbwOuyoqp-JPa6q0CU9lsnLd69OVjFE_rLEkSMw_GYxYxpiqhMvnRnXd08PcqRhglCwjl2pq6jKsIK9tRIKPOSULbRg3bI_dLVXezY5Zge4Zj7sq2G_kSd7srt9a-CKENUAS1fYjD-pokPo84L1-F9N32BwWGbmL6qrgzmfDLTG3TxL3mg8VXYRR5CLZ-IXf1iaNLb3F3jD4l2kaNcvpRuY5i0ROQF6hkdckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت ‏مسکو، روز ۱۵۷۶م عملیات نظامی ‌ویژه ۳ روزه پوتین در اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66468" target="_blank">📅 10:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66467">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7be955089.mp4?token=R07LvFqfCtikA5Uy7VXivIQi3m1KK2dhtTg2Q1MoOoti62iNvvyQ4XP5g1bGKrTZ_U5GEdf6J7F7bVu9CHyn89F9Wg28ilrdmgHyXEXO5hYo8Jn-flIpzys3gp8MDlIEBd1MeNxkOKWHiM57njEiY1oCEwDKR-Yg4yWQwGUnGEBblDNLnfdlDtT2ziezpeBALDpdvx8D2veWs78dB8YFmTmo3tY_l0LS94KCpoid0gBS-WlJULhZ6HhNkYt1fZYf7W_HbN8jtyiH4uH8LYjYL12hHl5hM7i6kTMfjbVvQTm7n3UVFi1l_X-k-nIpA2Gd2OX_1fHn3OnRoxBIGld28g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7be955089.mp4?token=R07LvFqfCtikA5Uy7VXivIQi3m1KK2dhtTg2Q1MoOoti62iNvvyQ4XP5g1bGKrTZ_U5GEdf6J7F7bVu9CHyn89F9Wg28ilrdmgHyXEXO5hYo8Jn-flIpzys3gp8MDlIEBd1MeNxkOKWHiM57njEiY1oCEwDKR-Yg4yWQwGUnGEBblDNLnfdlDtT2ziezpeBALDpdvx8D2veWs78dB8YFmTmo3tY_l0LS94KCpoid0gBS-WlJULhZ6HhNkYt1fZYf7W_HbN8jtyiH4uH8LYjYL12hHl5hM7i6kTMfjbVvQTm7n3UVFi1l_X-k-nIpA2Gd2OX_1fHn3OnRoxBIGld28g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری: شما گفته بودید که فقط تسلیم بی‌قیدوشرط را می‌خواهید. اما این تفاهم‌نامه شبیه تسلیم بی‌قیدوشرط به نظر نمی‌رسد.
ترامپ: خب، در واقع احتمالا تسلیم بی‌قیدوشرط است.
مجری: واقعا؟
ترامپ: من این‌طور فکر می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66467" target="_blank">📅 10:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66466">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/040ce8f378.mp4?token=Gak0iytzHiJZ_0foQphZJ8Kgw0x9Rek8zuCVpSUz9cNgWFUhr5YuSFnB5vb_El6DqPMGazK0vJubZ0PCClgG_x5X7nNxThwJlwQcY0QPJq2nQ39tOf-X5mQK1JaX20VmcOzGAdo40Prv37pezYpV2UB_d2iJML9TaJYDF8zYu3f0fxSCd-y0OELhVWi-Eg5KSljYRvB5UYlMd9RxUbyU6qgJeqCxgNujvCVIFrwvWkxkpTdCnGSsgpEJ50YCCGQOx2Wrxo9pPXFDd0IeFjOIAiD-q77CoibNCMstdw3eePFIds1jwwYBlerI6GNwx0qIc1sTiGdoxV7QG6GxjdGilg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/040ce8f378.mp4?token=Gak0iytzHiJZ_0foQphZJ8Kgw0x9Rek8zuCVpSUz9cNgWFUhr5YuSFnB5vb_El6DqPMGazK0vJubZ0PCClgG_x5X7nNxThwJlwQcY0QPJq2nQ39tOf-X5mQK1JaX20VmcOzGAdo40Prv37pezYpV2UB_d2iJML9TaJYDF8zYu3f0fxSCd-y0OELhVWi-Eg5KSljYRvB5UYlMd9RxUbyU6qgJeqCxgNujvCVIFrwvWkxkpTdCnGSsgpEJ50YCCGQOx2Wrxo9pPXFDd0IeFjOIAiD-q77CoibNCMstdw3eePFIds1jwwYBlerI6GNwx0qIc1sTiGdoxV7QG6GxjdGilg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ به شیخ محمد بن زاید:
وقتی انقدر ثروتمند باشی، میتونی انقدر آروم صحبت کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66466" target="_blank">📅 10:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66465">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635e862fe5.mp4?token=KOUnp3FcX8acP7MJqCuWmDQNlzVXgeWj_R0CwDY5zTVkVXETTVIXW5M38i6LF0nIrBieAJmHK-tzrf7oCBifP3OHbBQirxvPQAnsbV6lABtJlRNL0zJBh-CvlMT82fKE2E5eJat-VVwlI9AUTOWlDymaHHglisDnTzQSPkEpMXWbfTzFKkXejRU495fq8ufnvHI5N1yfZnRmZcObuy8_XVTURYq0kJBt3DVIlGBK67Ot-Sl9-NZq3CmpGir3hw20wz1DCoOPGGynKzhjhOydT49_H1EytzvxoNajb_XK2tCwsdw-h8N7pV_1LdVyS7MqAio3lVKC74yv8dAzzHmMlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635e862fe5.mp4?token=KOUnp3FcX8acP7MJqCuWmDQNlzVXgeWj_R0CwDY5zTVkVXETTVIXW5M38i6LF0nIrBieAJmHK-tzrf7oCBifP3OHbBQirxvPQAnsbV6lABtJlRNL0zJBh-CvlMT82fKE2E5eJat-VVwlI9AUTOWlDymaHHglisDnTzQSPkEpMXWbfTzFKkXejRU495fq8ufnvHI5N1yfZnRmZcObuy8_XVTURYq0kJBt3DVIlGBK67Ot-Sl9-NZq3CmpGir3hw20wz1DCoOPGGynKzhjhOydT49_H1EytzvxoNajb_XK2tCwsdw-h8N7pV_1LdVyS7MqAio3lVKC74yv8dAzzHmMlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختران حاج گاسم
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66465" target="_blank">📅 09:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66461">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BX4k-I_vjeTK0fsyrr2HOMi6RThqBYNk1gDP00nHPJq_5WXepDcnmlOvekbGt5fgV7dyV9W7BLLlS7Rge_pJN_oNhGmtnUIp-Y4qs_Xl-oEwsH2fxz8jG3_34vCATxXfsHHcEHF3QNK82YbcxRMslsnAiylNQ5y90kJQDGqLiENc4uLf-ojgSLGQGXMiXPWZu49Ektf1pnexPK7fWAyfnSeWvLmPJNcUhU3XEmEtRtEzChuPQOR6lr5sICyF8wFt6d4M8dsU_9ug36Y4Ic09lL12PT69GAe0dhJeSFEewEMHz_rcgukuMaQJ9Y0NKnbVNcNaKi8c1gPa39uc9i1oAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a17f4667.mp4?token=VrtPz57wYLNEmqmVdS6O1_puOTV1IGW4ykdHGYjwRml3LF85yxjzWz8Hmghusc9f7-4E6mEPhWEdEbBGCZUWivy6Hl-BRXjkzTeocHV7H8j9UuDLbpBj4Mv5bwYRQEHda-vpOVSxNYoBipooy84JGJJp7L9_w-_87ba-OYQxhwQ3huEdTqLjG2HOE3q8DtBt_rZ54OMEibhmsaNFB_vGxZnbE-L1zM5vwOXy4MQ66AQA3eDe4FHyf-wIsy6igzeNj91_Hke_efPv-gwl_YXQT_AYGTwPTWmIFfLq-ccBKixMgq5xKb3O0B2oCx9EQv4e_dFvevpfI3ZIoynRMNQanA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a17f4667.mp4?token=VrtPz57wYLNEmqmVdS6O1_puOTV1IGW4ykdHGYjwRml3LF85yxjzWz8Hmghusc9f7-4E6mEPhWEdEbBGCZUWivy6Hl-BRXjkzTeocHV7H8j9UuDLbpBj4Mv5bwYRQEHda-vpOVSxNYoBipooy84JGJJp7L9_w-_87ba-OYQxhwQ3huEdTqLjG2HOE3q8DtBt_rZ54OMEibhmsaNFB_vGxZnbE-L1zM5vwOXy4MQ66AQA3eDe4FHyf-wIsy6igzeNj91_Hke_efPv-gwl_YXQT_AYGTwPTWmIFfLq-ccBKixMgq5xKb3O0B2oCx9EQv4e_dFvevpfI3ZIoynRMNQanA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات شبانه ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66461" target="_blank">📅 09:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66460">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66460" target="_blank">📅 01:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66459">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ip-iERVo7ph9WAFLIUjh3tZ85Z14CW5jxyy0xDWEmYff9RUhKdSc0OuSDr9CswgxLF6x5aMkq7COOZZQizqTUR6KI_X91VuZmlTsaPt1tJw7NG7AxL2V8UU8dLV8jP_T0hvyY2R62U77M3MvIvUA4XfO0_iDsrL1Xr-bDryrb2d6G9rvOKRo1qt5Nd1rr0Zsb4pT5vh8YjMMKoFA3cxTseRY0vtaJkX2ii0KU0kna5gL-UOE7sGU1sc70v38GrVqAJ64ouLGsS9XIXjVBvtjmj1wa9vCiLudbeyQtr3EYJTT8SgjmjMwnj9i4-xQVil1mDH98XCAlosBiWAqw2hruQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66459" target="_blank">📅 01:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66458">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
‏به گزارش المیادین، هیات مذاکره‌کننده جمهوری اسلامی در پی تداوم حملات اسرائیل به جنوب لبنان، سفر خود به سوئیس را تعلیق کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66458" target="_blank">📅 00:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66457">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a4159b30.mp4?token=JbtPzwMJETEfkLvTc8CIJqpK7wBtQBMIh5zwrmGU2Qpb5AZ7ydNjb-3ru2LKUCttza3edCqtwZDGJJhB6-qVileNec2P8WwqSbXeV4j5HJFsy3WxZIrqnNxmCdrMa3eHmt1fFbh4JRBpBU1PNrT8b_bDTNGH82-Z4ygdySIiTmOFeMrZskQf8UkqrTLlNDJOEu94fcrMLsm9zF2Tnr6eHssp9sIKdZEWMu4VIktfCZnfErw5K4WgJg83D8UyL2z7udyp5zTNsjYKGftLk9gsgSqw7SqGPCoL2O9XockQdfbi_2Gq4wRk7oeEiLVxvvQihNYIy8Thhnq0IBGdW5Q4Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a4159b30.mp4?token=JbtPzwMJETEfkLvTc8CIJqpK7wBtQBMIh5zwrmGU2Qpb5AZ7ydNjb-3ru2LKUCttza3edCqtwZDGJJhB6-qVileNec2P8WwqSbXeV4j5HJFsy3WxZIrqnNxmCdrMa3eHmt1fFbh4JRBpBU1PNrT8b_bDTNGH82-Z4ygdySIiTmOFeMrZskQf8UkqrTLlNDJOEu94fcrMLsm9zF2Tnr6eHssp9sIKdZEWMu4VIktfCZnfErw5K4WgJg83D8UyL2z7udyp5zTNsjYKGftLk9gsgSqw7SqGPCoL2O9XockQdfbi_2Gq4wRk7oeEiLVxvvQihNYIy8Thhnq0IBGdW5Q4Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
آیا در جامعه اسرائیل افرادی هستند که بخواهند ایران را به لیبی تبدیل کنند، یعنی یک دولت شکست‌خورده با ۹۰ میلیون جمعیت؟ احتمالا بله.
اما نمی‌دانم که بی‌بی (نتانیاهو) چنین چیزی بخواهد.
من شخصا هیچ‌وقت چنین گفت‌وگویی با او نداشته‌ام. گفت‌وگوی جالبی هم می‌تواند باشد.
اما همین را الان می‌گویم: آیا تبدیل شدن ایران به یک «لیبی ایرانی» برای ایالات متحده آمریکا خوب است؟ قطعا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66457" target="_blank">📅 00:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66456">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47cfe42200.mp4?token=jhq3QnGfdIxrrstuBNq-riXsYOUGeaROfA1fDu5Op17Ie6CLSNbo1p1e0GbjQNqdLBqHoVJN5xMxIh_ctLoRa1E5nv-07KGl6N8D3NXQkim3SnwJQPEhxKarfyUfI9z_FE5BUrFIZehnPOVLDdgU8FixwxyUGvsgXm2uWqfaqoA3wLect2ruKMxFT-92EnCuzPDSfgPZAKn8ERCB3iO55nEyvyMQvmzXv_lx85KZsd5nHed_vpTUqLYDnMVv2DEZu3Z48Yt_kQuUZgfMpfzlnUNhPhDfwY2iAW9vPnJLEZIkpx7Fk4aTjy2L9KyZu23mis9PeSL8BMhoffkSAe8q6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47cfe42200.mp4?token=jhq3QnGfdIxrrstuBNq-riXsYOUGeaROfA1fDu5Op17Ie6CLSNbo1p1e0GbjQNqdLBqHoVJN5xMxIh_ctLoRa1E5nv-07KGl6N8D3NXQkim3SnwJQPEhxKarfyUfI9z_FE5BUrFIZehnPOVLDdgU8FixwxyUGvsgXm2uWqfaqoA3wLect2ruKMxFT-92EnCuzPDSfgPZAKn8ERCB3iO55nEyvyMQvmzXv_lx85KZsd5nHed_vpTUqLYDnMVv2DEZu3Z48Yt_kQuUZgfMpfzlnUNhPhDfwY2iAW9vPnJLEZIkpx7Fk4aTjy2L9KyZu23mis9PeSL8BMhoffkSAe8q6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس این انتقام ما چیشد؟
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66456" target="_blank">📅 23:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66455">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad18edc1d.mp4?token=cF9MwL7SwZRawDjJ6yQtrJBh2RCsaX_eyPnVnezehQJ_43WXs8t1yefxNi7XXGKXQtOBf_K5KayRr9Myokq2Pm6LQoh5MtpzltC3-JmOvzKOHqN0G0h6l7vvxGu2SruWEiEgVa0Hm9xQ1XIUfk8hxFSM9McntI4yvCJsFiy2zJuodCSyGLPWF4sndk_gilOi2hbyHUqMT2YmpASieLfOm4OQD4IMADHYf5K8aapSo6PC5Cfw9uDwAhy7P791bmLL5uAvRKj_v8S2PKysLHQ4Agq_glGp_U4Q1KXDGELv7xaWPnbp--v4kZK4mkLsZlJxykccg4Mwpv8oYGLOkAw56Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad18edc1d.mp4?token=cF9MwL7SwZRawDjJ6yQtrJBh2RCsaX_eyPnVnezehQJ_43WXs8t1yefxNi7XXGKXQtOBf_K5KayRr9Myokq2Pm6LQoh5MtpzltC3-JmOvzKOHqN0G0h6l7vvxGu2SruWEiEgVa0Hm9xQ1XIUfk8hxFSM9McntI4yvCJsFiy2zJuodCSyGLPWF4sndk_gilOi2hbyHUqMT2YmpASieLfOm4OQD4IMADHYf5K8aapSo6PC5Cfw9uDwAhy7P791bmLL5uAvRKj_v8S2PKysLHQ4Agq_glGp_U4Q1KXDGELv7xaWPnbp--v4kZK4mkLsZlJxykccg4Mwpv8oYGLOkAw56Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
آنچه من به برخی از منتقدان این توافق که شنیده‌ام می‌گویم این است که آن‌ها می‌گویند: “خب، ایران این همه منفعت به دست خواهد آورد.”
من دوباره همان چیزی را که قبلاً گفته‌ام تکرار می‌کنم و احتمالاً مجبور خواهم بود چندین بار دیگر هم تکرارش کنم: ایران دقیقاً چه منفعتی به دست می‌آورد که قبلاً نداشت؟ پاسخ این است: هیچ چیز.
آن‌ها هیچ چیزی به دست نمی‌آورند مگر اینکه رفتارشان را تغییر دهند. اگر رفتارشان را تغییر دهند، آن چیزی است که باید از آن استقبال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66455" target="_blank">📅 23:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66453">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‼️
یسرائیل کاتز به کانال ۱۴:
ارتش اسرائیل دستورهایی دریافت کرده است تا در صورت لزوم، برای عملیات دیگری در ایران آماده شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66453" target="_blank">📅 22:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66452">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkTuRwZDSf0-B0HUZi_aLPELFouev-nBelAzKvsm35brKgxJA_Y87TByf65nToQDjJ2gS1JagnYelXNtaSmZQ5LVxbNxPCVIfBHkZ3V_e4QNMQcZm5_Y1j7Lu-BKxwjkJzdLxiH__2_i2wpzj6sjA5Doq1pfFffm9cUBsmhoI99bP4mX_rzWHqJC46yW7xfUX768SUTCTJ5VWpPcdq7KktxXeSI2Wb2RJmow9rjiQkgK6_CMCnJzhvI_h5Bi8DcOsjOZogMD7agb7quSTow_lcH0wjRD8IK5AIO06tFAXM5aPdPD5cGTwz36fjs29hs2uQh4huMhD9whLKzikX-57A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در تروث سوشال:
ایالات متحده به صلح متعهد است و ما همه را در منطقه خاورمیانه تشویق می‌کنیم که به تعهد خود برای پیشبرد مذاکرات ما به زیبایی پایبند باشند. بازارها از آنچه که با کاهش قیمت نفت و افزایش سهام اتفاق می‌افتد، لذت می‌برند. ما انتظار آتش‌بس کامل در همه جبهه‌ها، از جمله لبنان، حزب‌الله و اسرائیل را داریم. از توجه شما به این موضوع متشکریم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66452" target="_blank">📅 21:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66451">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">هات نیوز | HotNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/news_hut/66451" target="_blank">📅 21:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66450">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم  @News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66450" target="_blank">📅 21:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66449">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">این پیام یعنی پایان پزشکیان و جریان اصلاح‌طلب در ایران، و آغاز حکومت نظامیان به سردستگی قالیباف #hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66449" target="_blank">📅 21:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66448">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم  @News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66448" target="_blank">📅 21:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66447">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lArd7JekZ8tQyN49K_LAE95JDnwfL4G7YI-2u6cjSYfZKDDRsu3Jb-WvFQdH7JoI4eOMrYz7VMn9tyM2cJDaHrbcMBhi3tb9lT_xsD0Ck-6xKug_Rn8ptVVWoXNCwBHjBz62Xn46VzpFh4eiWW-LMkVya2ngHXXL9G4vbcjzkb95ZxVX_8RMMshkL1YevrGdoWpaYcwXFJi7eA6IQqndpPY7zHY3VWXO3FyyvgrqyMCmwUBXWNm94PIOt6-ESjCthVDMScmLsi93XQjTvLAl6JduRYnFDZRwX8OvENMVOwk5esPvngJsTAZgu_mcNrMhQPu1EFTgOdpa597fk1Ou0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66447" target="_blank">📅 21:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66446">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sinO1k-Bxy-pkYTVIoFMcPhlnbmAgEZb5FC7Jn8xpmY1gV474EOrxgEt6GF1Qwr2fvcQeF07ekQWCcmhLVpEftG-HhnziQsoYIWjFPXLNqLjNBYbgx-W74ENglTnTPPyuz4x57fsy3wcMf2Y1VdOFjsNFu9Ny6IcEs9WroG7TBTJnOPOeJecRlnLjuJVsqvWQQqo8Qwzxhc0nGe6QMTus8elU6hb7mhyGeiHXHSRTV05jJokFlKkJKKFkadI5IlAf0bexs5LX8vA-yLCyvF8NR2TxHoLCbg2oq7UIxM4qoMQPSswwOprN1BMOcsk-cOKN1PSe1RcogUogJKSFyPE9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ: آمریکا هیچ پولی به ایران نمی‌دهد. اخبار پرداخت 300 میلیارد دلار به ایران فیک است. تمام آنچه برای آمریکا وجود دارد، موفقیت، کاهش قیمت نفت و پیروزی است. وضعیت بازار سهام را بررسی کنید. پروپاگاندای دموکرات‌ها در کار است!!!
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66446" target="_blank">📅 20:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66445">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏
🚨
🚨
🚨
⭕️
سنتکام اعلام کرد، نیروهای آمریکایی محاصره اعمال‌شده بر تمامی ترددهای دریایی ورودی و خروجی به بنادر و مناطق ساحلی ایران را لغو کرده‌اند
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66445" target="_blank">📅 20:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66444">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f51df7dfe.mp4?token=NAoeix5EoWMWdnsyABC2fBIqwmO96j4cfWOP42vP3bKuAdFIj8iJ0HpCXizYZx0y235vc5kBFKYwWDdJGnmCxjUctxIgetl2xf-_OJyuS7VQDR-sxKgiGtmZlvz81bTtlHHQmx0A1wYny81vYJb4pbyShU8zrf4hIyxqGyRR42IKvhV_YtwpDSasiB3RiSVhZK-jiF0xa4jeThzWm-jHv32kf9UFk86XHSo6EQVRslUTLqaGYY_SZC3JR1_DqW9G7Lo2bcEUzG3_P3OYtB5xFW5yboDFMEji-QFmeVakYX43OB3gBX1r76h_siwN7mjIGIiy_6h9lMRby7vidsyR4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f51df7dfe.mp4?token=NAoeix5EoWMWdnsyABC2fBIqwmO96j4cfWOP42vP3bKuAdFIj8iJ0HpCXizYZx0y235vc5kBFKYwWDdJGnmCxjUctxIgetl2xf-_OJyuS7VQDR-sxKgiGtmZlvz81bTtlHHQmx0A1wYny81vYJb4pbyShU8zrf4hIyxqGyRR42IKvhV_YtwpDSasiB3RiSVhZK-jiF0xa4jeThzWm-jHv32kf9UFk86XHSo6EQVRslUTLqaGYY_SZC3JR1_DqW9G7Lo2bcEUzG3_P3OYtB5xFW5yboDFMEji-QFmeVakYX43OB3gBX1r76h_siwN7mjIGIiy_6h9lMRby7vidsyR4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس در مورد اسرائیل:
در طول سه ماه گذشته، دو سوم سلاح‌های دفاعی که از اسرائیل محافظت کرده‌اند، توسط آمریکایی‌ها ساخته شده و با پول مالیات آمریکایی‌ها هزینه شده‌اند.
مشکل اسرائیل دونالد جی ترامپ نیست و هر کسی در اسرائیل که فکر می‌کند بزرگترین مشکلش رئیس جمهور ایالات متحده است، باید از خواب بیدار شود و واقعیت وضعیتی را که کشور در آن قرار دارد، ببیند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66444" target="_blank">📅 20:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66443">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab365474cc.mp4?token=Kg-nF6hbpU8MUCMiWMXckEKSdeYkrS9J3px7xmaFTGL93KY6em6Qxgsp3e7LX1sYUfMuWGYmLJGPI0t73pqhg1OUyV5m2-JnppjZ5fSUZzf9I9pH7GMB2HZySjSWc2ykume9ku79dhJ557ntzEtF2W4QTp1ianpCzLNP_GI0F4_sWEITushuERYTA2kd2LIfMPXTT5weOjUMYYoO4lU8t17IB2MXRmts2DTZEqAdbrMbQm7TFDDpzbC4ZZmkaA9i6UrNRJXBsM83GnGsW8W9oWljvhSpInb7KLydKYeQQS3sHlQein6qIZHHy2w5PoY3ZL5TpD1ePV5mbsjKUSR9mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab365474cc.mp4?token=Kg-nF6hbpU8MUCMiWMXckEKSdeYkrS9J3px7xmaFTGL93KY6em6Qxgsp3e7LX1sYUfMuWGYmLJGPI0t73pqhg1OUyV5m2-JnppjZ5fSUZzf9I9pH7GMB2HZySjSWc2ykume9ku79dhJ557ntzEtF2W4QTp1ianpCzLNP_GI0F4_sWEITushuERYTA2kd2LIfMPXTT5weOjUMYYoO4lU8t17IB2MXRmts2DTZEqAdbrMbQm7TFDDpzbC4ZZmkaA9i6UrNRJXBsM83GnGsW8W9oWljvhSpInb7KLydKYeQQS3sHlQein6qIZHHy2w5PoY3ZL5TpD1ePV5mbsjKUSR9mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏جی دی ونس درباره ایران:
آنچه واقعاً اینجا اتفاق افتاد این بود که ما روز یکشنبه تفاهم‌نامه را امضا کردیم. این توافق‌نامه مفاد توافق‌نامه را تثبیت کرد.
چیزی که ایرانی‌ها پیش ما آمدند و گفتند این بود: «ما دوست داریم متن را تا جمعه منتشر نکنیم.» من واقعاً متوجه این موضوع نشدم - می‌خواستم متن را فوراً منتشر کنیم. اما برای اینکه با آنها کنار بیاییم، گفتیم: «مطمئناً، باشه، تا جمعه صبر می‌کنیم.»
و سپس آنچه در روزهای دوشنبه و سه‌شنبه، در حالی که رئیس جمهور در اجلاس گروه 7 بود، اتفاق افتاد این بود که شاید رهبران خارجی با ایرانی‌ها صحبت می‌کردند و آنها را به انجام این کار تشویق می‌کردند.
ما قطعاً به آنها می‌گفتیم: «ما تمایل شما را برای منتشر نشدن متن تا جمعه درک می‌کنیم، اما می‌دانید، ما در یک سیستم دموکراتیک زندگی می‌کنیم. مردم آمریکا می‌خواهند متن این توافق‌نامه را ببینند. ما مطمئناً دوست داریم هر چه زودتر آن را منتشر کنیم.»
و بنابراین آنها به این نتیجه رسیدند که رئیس جمهورشان آن را امضا کند، رئیس جمهور ما آن را امضا کند، و مهمتر از آن، شعار را تکرار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66443" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66442">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66442" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66441">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LaQnccA_Yd7_nk4DwFVwNwm4EMzH9o9zF6lI6uuomwCsWLyaJhSo0pSF6dnpqX3HMF9AGW_Ar0rAl2tEnj19Xno_kaAm4y8fqKvqAhbL13XTNff-ZcoIuEfnBEQBfKTiPfmUIxmfn6rWEpzum5dR50QQWEvvls2tIB_Dml7Bj52RoHATSTGDFdTIY8x0gy9ZBfjvVZlzU5TwErQE5rE6siSv2nCGRBLXXJF43pq0LeTMJztb6w7PYmV_XNYnyAiuDR2ifRGEBsdnknNR6F3BLnN_9l11TKluAv-_ZJGBXuiifknY6zya2gJokSYuEH5pLk9Hw6Zx3IB2R3hbhVo-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66441" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66440">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b31dd3b8.mp4?token=JdKtbz5OhxnK88FX-lzGpQaVzB9N7KEaN3n4zuqjgnn1Gzb5grvBupbXmzAYLQoNIAd2eQQIYaypuyoeeX9f99AqDi7fyTVuodsxBUzHyRnLEQPLKP6mtUueTIVAUy8bd4aQeDA01xK0mEa6rPQS6ZiR2WENh3_N7ZgbpesHVXVTmkFiUmpq4GeskVQlqsLxAeacSteJPxQ2rzD7vJB7vLJzgb1dktG7fXvPwdYDeMLXyz9oU52pcOQUuLv-U9nO13UiUm1P4CuMyCs8hKVh1GLdMv_Z6nKZYIiCciS-m5bp1Te-535Xo3Chj2CWBid5mBB4C_moFb8qyUg2RRAHhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b31dd3b8.mp4?token=JdKtbz5OhxnK88FX-lzGpQaVzB9N7KEaN3n4zuqjgnn1Gzb5grvBupbXmzAYLQoNIAd2eQQIYaypuyoeeX9f99AqDi7fyTVuodsxBUzHyRnLEQPLKP6mtUueTIVAUy8bd4aQeDA01xK0mEa6rPQS6ZiR2WENh3_N7ZgbpesHVXVTmkFiUmpq4GeskVQlqsLxAeacSteJPxQ2rzD7vJB7vLJzgb1dktG7fXvPwdYDeMLXyz9oU52pcOQUuLv-U9nO13UiUm1P4CuMyCs8hKVh1GLdMv_Z6nKZYIiCciS-m5bp1Te-535Xo3Chj2CWBid5mBB4C_moFb8qyUg2RRAHhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
ایرانی‌ها برای دومین شب متوالی به هیچ کشتی‌ای در تنگه هرمز شلیک نکردند. تا این لحظه، آن‌ها به تعهد خود پایبند بوده‌اند.
سنتکام اجازه داده است دوازده کشتی از محاصره دریایی ما عبور کنند، بنابراین ما نیز به سهم خود به تعهدمان پایبند هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66440" target="_blank">📅 20:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66439">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fso_MXfVKpkUZvqqR5KWVA16sV8_wRpC3xX6rIbqv1gmoCx-pKEyMrUtMXxY7UMNa_P0jObfzUd-zx-Nv0XQi0eadHtZ-g62cJ1SyG61QWYPDkDvP1JvkDbZOjO7rcUBRTffX8r0uCbZL_XyposY3p467os5RyG0_lpM2CCQSOOmO5wcL2AryXoLv85P5mym10IDJvEEoQGi_D-o1tNH3UAh_U9KlpabcLwiQTOrF740p_M8L9QgJejCIH2xNwNRcaDx_slSsgb3ushMlak041cGgYlY-4eq2FLwqZeL2hIvtu-Pz48evBBlELAzAqo_MBYhB5WVTMr_u9mvbyh5iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
فایننشال تایمز :
گزارش شده است که ایران به ۶ میلیارد دلار از دارایی‌های بلوکه‌شده خود دسترسی خواهد داشت تا کالاهای آمریکایی خریداری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66439" target="_blank">📅 20:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66438">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBcgYChZBxxKXf8B6Dj7zW_fRAiEaQDMESAepj2T9GoK_C9VtrksQUpVsYjn-fF7Om-njxt6RTY7b8sH12gHnq_oPwaagQOBO95xbHqQDRnqliAl8mLjOn1P_EQmsr_mwTvS2OBYetcdah9Q_Ueso4UHx8Km1wZ_sc-wizQwgnZ53T_fIaipxBzAMOvRiuXFIWo_kzn97pavIdB6iUU_Y5OzyEwe7YQC3i0q9NK-suJK_hsyRue0Ve9hepWyHAPn5yokZLIxyH1KMk9AQwrbDHEwbtC4ofkPXi4AWQ8cfoNWrAB6wa3fdgvR-zFZBvEhCDtbKyatnpScxtt6dCcOOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
ونس: کجا می روی دونالد! «امام مجتبی» منتظر توست!
دونالد: از روی امام شرم دارم ونس! شرم! توان دیدن جراحات ایشان را ندارم!
ونس: تو هر کار توانستی کردی! تصمیم امام اصلح است بر ما!
دونالد:‌ چه کنم! چه کنم ونس! با این جماعت هزار رنگ٬ که دروغ را چون «رج قالی» میبافند! امام مان تنهای تنهاست! شرم بر من ونس! شرم!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66438" target="_blank">📅 19:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66437">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4fb90d19.mp4?token=H7hPekBb5zVQOTHGH0OOwZe9JIxMIRkI5I8xDoNT6gGoT3qr89Rx-g9JPg2PZCgVkZZPq6gCCGMuI-n3twAHuxmeei8EdjATwxdTjhaHHzGsjC5Q4LqU6h5FalvjC15O4fd_fTyNyskna1BAfzok4BuDfmgqarWQOyvZVoMdgtYItwasGMzOOLQIbgfWUjm0hiJUttj1Huycei-hFiYhMBv7ksX2VnB5FPBiYDqJUJV8rkYNqCgCgHa-_jWlrcqNp45Afilxw4bgzcjV0T2EVK3yfmUl0bV2gluT27H-5ynnAvJgxJxDjXkvBzmXhfB1LT4kJbzYktL3shA4ZakMrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4fb90d19.mp4?token=H7hPekBb5zVQOTHGH0OOwZe9JIxMIRkI5I8xDoNT6gGoT3qr89Rx-g9JPg2PZCgVkZZPq6gCCGMuI-n3twAHuxmeei8EdjATwxdTjhaHHzGsjC5Q4LqU6h5FalvjC15O4fd_fTyNyskna1BAfzok4BuDfmgqarWQOyvZVoMdgtYItwasGMzOOLQIbgfWUjm0hiJUttj1Huycei-hFiYhMBv7ksX2VnB5FPBiYDqJUJV8rkYNqCgCgHa-_jWlrcqNp45Afilxw4bgzcjV0T2EVK3yfmUl0bV2gluT27H-5ynnAvJgxJxDjXkvBzmXhfB1LT4kJbzYktL3shA4ZakMrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار:یه مرد دانا سال 2020گفت ایران هیچ جنگی رو نبرده اما در هیچ مذاکره ای هم شکست نخورده
ترامپ:کی اینو گفته؟
خبرنگار:دونالد ترامپ.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66437" target="_blank">📅 19:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66436">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pa2luEcNrLCIJNqW_hul8fObhPG6ak8T0PtX61q8LCPRibjhM-Dw9P383QfqQwaNJmRJ3t7VxjJCECN3RvxwUqd_wiJb8kBZUtRccLhjfAqGCK69GwSGw2zx0E_Al6Bpx-RCvOohANMmoZCw4d_Jd42kinXxWjjJoq5Z_9D1NAc1RKa0_iKi7gUx2tc1xVbPa4HZKKhlpg655TY-47kroWgsU4AR--d4B8LyXBEzYMqZDYfNR4CtxMu_aTonPLrdyBmxSjR8CBkPXtjnIdOSIkiqb8FBVkn3WbdOvt8nQvwySj97MjvOF6iJOKInUR5WYX46rUQ7gm92uNvPf9-z0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
الجزیره به نقل از تلویزیون پاکستان:
سفر برنامه ریزی شده شهباز شریف به سوییس بدون ذکر دلیل لغو شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66436" target="_blank">📅 18:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66435">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLIDi_B8qfo_qKHUnT9APr7HjC0AOrMobHCqWzLu4rfV5MoIv_1p1hZGT8-l3S7xrBRJg5qpQB45oDxzB5lYhi4ggQU7GhuRND3qCeZMYvkjq_Y8DIiCA4B_VWpR1WbFxSOTl3WKJtsJAsIMYGO7n529GWcup71wsABGa-re8CQS9v-894c_heTXcbeCRvhVfpHXLiM4cHm993iSEgf6OSq74Pye29-oZYueZC2OB-MR3jSYKMvOrgLeUVbk3Utnu_9gFh9eE8jC83oelOI2pt1RoFhpacI5wb8U5p7xkbsJO1xS0X7MtrbshcG994GqUx7cETxDTXvTrtMbixve1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
نفت جریان دارد، ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد (جهان امن خواهد بود!)، بازارهای سهام در حال رونق هستند، مشاغل رکورد زده‌اند و قیمت‌ها در حال کاهش هستند (قابلیت خرید!). کشور ما قوی، امن و محترم‌تر از همیشه است. «خواهش می‌کنم!» رئیس جمهور دی‌جی‌تی
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66435" target="_blank">📅 18:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66432">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vEDh_1vpK4InXhD9R_6oxPMOUbKnwyHVL_dWZkCz6CatlgwEdfgnagJDDNs_GHWplAt8f3Xi2thdPy8g8OkEOV7zHkdMGCWe8qcxIPWknSi1ZaoMhgntl95-sBlbcF4YW8WqsaVGmDnHhgGyobZQ0KAJzpeWQUroP07VbQevBe9PFnk8B71IZVb-APvpFDGN9iZEbsO6LMhSx2QHYU4Go98C6A4ZB6MVAQg6nfSfZHamtqnXH5zcz95CyR8thAUpvPRW3-qZ9KCMFT5jDzbzA8DfhpPqUzxG6c-_4AoZEv2Lt15LSoTwGPQYVD-df05D21BYYWFmwKUJIL_rgwT30A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VaH_f8WzoLOyTzJGCCNGnjmjXcxHqS4GM_P_1DlnaWjqW4TkITiAtOrmvM2fVDzvFDRtli3aZrES2aEtcECuWk3Mmos8U3ahqWnTk7XKmgKdTGwQ9_zAoR59UD2a1hcRg5rj3-auFgUxX3cczFnmizMxzzG-JXrGksuDjkWHSlkxaTgCNSr42RVmmpjYQX65mBhGFxNgl218onTW0fLfmmhp9Fj-TcYVinNfY3oyUD5-X-xQCbibhBsblM0RaGAsWTuh1imrp-2LwMQNYAOz4d2ZkMXYrKQYXFLAoRf40uL1ILOSA7uhUWa_YovHz8YNyLQp-WP-_z6Vqdgs01Bs5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13c6e64c5c.mp4?token=Qvfhmp4bdYJmcM6r9W5NurySQVbT9rlaFzmoWU8PHctZEejpqknVjn0DUKR3uX6JiUvlo85t9Cn5Opy7eSwrZADOWn1R-ki5n1Mi72-tSutJ5uSJgC147F8w7oTKHX4Fff7QGyX5IbpYLq-acVdjb5BKFr1BgUP0pgIZdDMAU5KsR0yV7sFqmH-172gywharRUXULJBVRCFWzU_dI210TgoY_TTYti8aHDfTNOdlBYj7n_5jIbyJrdmNPJK5U8U5MYL2y5ktOUr-HKD6T-Kf0-FOToghdmgpXa36rR3LD7IcEOpnGZ4QO7EGamR5PlDUlee_MtTTZlWEBLvUzVVBdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13c6e64c5c.mp4?token=Qvfhmp4bdYJmcM6r9W5NurySQVbT9rlaFzmoWU8PHctZEejpqknVjn0DUKR3uX6JiUvlo85t9Cn5Opy7eSwrZADOWn1R-ki5n1Mi72-tSutJ5uSJgC147F8w7oTKHX4Fff7QGyX5IbpYLq-acVdjb5BKFr1BgUP0pgIZdDMAU5KsR0yV7sFqmH-172gywharRUXULJBVRCFWzU_dI210TgoY_TTYti8aHDfTNOdlBYj7n_5jIbyJrdmNPJK5U8U5MYL2y5ktOUr-HKD6T-Kf0-FOToghdmgpXa36rR3LD7IcEOpnGZ4QO7EGamR5PlDUlee_MtTTZlWEBLvUzVVBdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پختو پز اوکراین در مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66432" target="_blank">📅 17:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66431">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bf3ba597d.mp4?token=A2parJ5Y5NIDZ8Fvn3E-MbWTR_iQceibpRt4ElnVi-jF-2IQkoohfjP_TNg2XYMkfIuJbCIivwyniI8VkprLy4kuJbCZ1EyunJBkrgxlapsHhey34BFSYeT22-p9O0P_kT2zcF1hQtmWXwpIWL0R12e3Su6HClGxJNWufs3bASYZ3JpMo7RfDnAqhLBy9JGINJCfLgaZc5gcxbdY_F8qVu-IyIZz-C2C_gzGKJdJrn4Wpdo7yv-g2-FFDP36xD1HIQTBpVIqqmwxoX4Ni20M36BbkppZQlcoOqACdwoD_RVzmE_IiwHvh2rgzxVE22kz5tTFjTdi0gOOlUlQS1-_qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bf3ba597d.mp4?token=A2parJ5Y5NIDZ8Fvn3E-MbWTR_iQceibpRt4ElnVi-jF-2IQkoohfjP_TNg2XYMkfIuJbCIivwyniI8VkprLy4kuJbCZ1EyunJBkrgxlapsHhey34BFSYeT22-p9O0P_kT2zcF1hQtmWXwpIWL0R12e3Su6HClGxJNWufs3bASYZ3JpMo7RfDnAqhLBy9JGINJCfLgaZc5gcxbdY_F8qVu-IyIZz-C2C_gzGKJdJrn4Wpdo7yv-g2-FFDP36xD1HIQTBpVIqqmwxoX4Ni20M36BbkppZQlcoOqACdwoD_RVzmE_IiwHvh2rgzxVE22kz5tTFjTdi0gOOlUlQS1-_qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد کشتی ها در تنگه هرمز پس از امضای توافق
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66431" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66430">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkkrv7vtSXmpvhJZzkjGLi81OZVsChbdXVNDIqFVAkzyoTTqe-pAiH22ilJO0YLvy99IaSjgQlRjTjfy7HagzQIy9nibkHWL1BTKigJ_5v24uEjQgaFi0QdaHnOrl9vbSC06mPctBXRX1KcfTA7DGjVJ-C9QZ65QwQ0hh3LgQWJ4IdPnqRQ0fyf-cXl6V5hHTninx5rF7_pvrjbolo69n2uymMdml9a9usdHj2g_NNlR7ScFcbP2tKmNB8tXmtsoJEjia5M0SeStK0vBTssAb-96KLbaqMlZzW2F-cNZru03raebj8Rwb6KeSb2ra9Ah144N4yCLU3o3JoxxHd0ULg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ارتش اسرائیل؛منطقه امنیتی فوری در جنوب لبنان:
نقشه منطقه‌ای که نیروهای دفاعی اسرائیل در جنوب لبنان در آن فعالیت می‌کنند
بر اساس نیازهای عملیاتی، نیروهای دفاعی اسرائیل در منطقه امنیتی واقع در حدود 10 کیلومتری داخل خاک لبنان مستقر شده‌اند.
نیروهای ارتش اسرائیل در منطقه عملیاتی جنوب لبنان مستقر شده‌اند و به تلاش برای از بین بردن تهدیدها و بهبود دفاع از جمعیت شمالی ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66430" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66429">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hS_PgtH3WQTiXDykLYEcoeMWrn-DJP7-uM2buUxl-SoiAsYLLL4NqLNFzOU1oQYvWSqjq8vFDw-1oEBHFvY0T0MVsDJ92a65nS9Yf6crWha4u76yUNX0RDeaCGqiWdI9mk3h68f0dyAvqPsoWGc6F5_W0dqwP0QRykjnRmsO9OxUulTpOL4T7lqjWURPDhMI8NK4qWlfdNjP_8f4mxiYSMKaAffoG0vHRUYAI93di-DT5hPSHqwNqNhA5a3pXyBbQxiI73jgietbQ99xKqJ-DncREo5ZfPev43-FSCsnySiDpH7lxiI6RNbRk8NSNKrFOMtIMyT26yQU0NhndFjSLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان؛این یک سند تاریخی و پیامی از ایران مقتدر است:
صلح در سایه احترام متقابل تحقق خواهد یافت.
جمهوری اسلامی ایران به صلح جهانی با حفظ عزت و استقلال، پیشرفت و همکاری منطقه‌ای همواره متعهد و پایبند است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66429" target="_blank">📅 16:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66428">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622db6728d.mp4?token=dpJ-q1mZHcnHWCTBzIiD_CkBA1Ga5fp5E0R8Aw4a05hpxf12vh_qtmxvrEOFP3o8p75UGs8qTbffUPqgFjbOYwO9GDKvcwd4i2Pej5xKZItkJTeCCcO-1GUBuaRzKrgNh8pvab4ka-DA3Oxkfmx0bD6fskibJxeatnLn91uE20H3YXA6lO2E4uBnwfDPT70WTUpba5znbps5GKskmGRE8Tkq_vrqRQZP_3ohGVT0TRLswGjfHgFpu--iJrBKTjgVtnPlSX09dnskYBSzhd0xnM5XklJq57rTKGoiIDELNpOrnK3glYJKrU1RChhRclvM0pl3vL1eQxTjvePyhn205Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622db6728d.mp4?token=dpJ-q1mZHcnHWCTBzIiD_CkBA1Ga5fp5E0R8Aw4a05hpxf12vh_qtmxvrEOFP3o8p75UGs8qTbffUPqgFjbOYwO9GDKvcwd4i2Pej5xKZItkJTeCCcO-1GUBuaRzKrgNh8pvab4ka-DA3Oxkfmx0bD6fskibJxeatnLn91uE20H3YXA6lO2E4uBnwfDPT70WTUpba5znbps5GKskmGRE8Tkq_vrqRQZP_3ohGVT0TRLswGjfHgFpu--iJrBKTjgVtnPlSX09dnskYBSzhd0xnM5XklJq57rTKGoiIDELNpOrnK3glYJKrU1RChhRclvM0pl3vL1eQxTjvePyhn205Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بعد سه ماه هرشب توی خیابون موندن و پرچم تکون دادن ، بهت میگن اقلیتی تندرو و خون رهبرتم پایمال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66428" target="_blank">📅 15:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66425">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4faedc1ad.mp4?token=Zetu7LheONmbusi-eRnNIOfoAA4WLH9pbJFc5uphwcAvOxAUWrsAXb8A2UUvrbJ60LQCVW_7wuenrlzmhhdMZmd3g4j80Q6ev3Uz006nd_LqMPUajLBNl5s5ojSHLsIk7e59khwiui-MMUlCYohvNfkw9VFOxV_6tVcpphX_FkEFU8kMKNNtSAiA-jTfJepMxHkF9p3PL7_F5MLgW24PVPdj69AEiIKDh2zltsZjcb6t6ehfNyIJbgz2BE4sveK8s4dSdHu4MUmXyN7wV8Fa48vxJNmeJhB7yj_TIKcXH2SMq0ja7lU-Gg359ECiahCqIEPglkewTOWIBcyxYVThXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4faedc1ad.mp4?token=Zetu7LheONmbusi-eRnNIOfoAA4WLH9pbJFc5uphwcAvOxAUWrsAXb8A2UUvrbJ60LQCVW_7wuenrlzmhhdMZmd3g4j80Q6ev3Uz006nd_LqMPUajLBNl5s5ojSHLsIk7e59khwiui-MMUlCYohvNfkw9VFOxV_6tVcpphX_FkEFU8kMKNNtSAiA-jTfJepMxHkF9p3PL7_F5MLgW24PVPdj69AEiIKDh2zltsZjcb6t6ehfNyIJbgz2BE4sveK8s4dSdHu4MUmXyN7wV8Fa48vxJNmeJhB7yj_TIKcXH2SMq0ja7lU-Gg359ECiahCqIEPglkewTOWIBcyxYVThXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات سنگین اوکراین به مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66425" target="_blank">📅 14:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66424">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92b0722cb.mp4?token=PpZvoec9vc-6EhnUW45D37qWhDXwSKImcEPfyINAMJbfj-OMLcMjrtg25U7wt7Gk3XOe8x6e0TyniUJB9CBsbrJ0KW-eqWpMLNc0ERizIWzzWCRgx-jN311RABz6xWWYyskL1GCfBzx8EOUUbKXHHx2JrRjqg6ZU7M0WNA4qF_-yR3luKTvxfymKr0_PahF_Ty5sOqmcmIXUtVNkrCD7rDGJBvTPFqkIaAvGd0eRd7HFXVKE-eteDASMAKe24QHQpcjLJK9-J8xZaN3m21aBcJIVPD2whVnt-JxZuQhb9Czb9u-WvNolSatcuPpbbycjcb4r2WpJYEQtiR-RKT39Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92b0722cb.mp4?token=PpZvoec9vc-6EhnUW45D37qWhDXwSKImcEPfyINAMJbfj-OMLcMjrtg25U7wt7Gk3XOe8x6e0TyniUJB9CBsbrJ0KW-eqWpMLNc0ERizIWzzWCRgx-jN311RABz6xWWYyskL1GCfBzx8EOUUbKXHHx2JrRjqg6ZU7M0WNA4qF_-yR3luKTvxfymKr0_PahF_Ty5sOqmcmIXUtVNkrCD7rDGJBvTPFqkIaAvGd0eRd7HFXVKE-eteDASMAKe24QHQpcjLJK9-J8xZaN3m21aBcJIVPD2whVnt-JxZuQhb9Czb9u-WvNolSatcuPpbbycjcb4r2WpJYEQtiR-RKT39Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏جی دی ونس در مورد مسلح کردن معترضان ایرانی:
در واقع تا حدودی دشوار است. می‌دانید، نمی‌توانید همین‌طوری از آسمان سلاح پرتاب کنید. واقعاً زیرساخت لازم برای رساندن سلاح به قلب مردم ایران وجود ندارد.
یکی از چیزهایی که رئیس جمهور خیلی نگرانش بود، همه این معترضان بی‌گناهی بودند که توسط افرادی که چند ماه پیش مسئول بودند، قتل عام می‌شدند.
آن افراد اکنون رفته‌اند. اما خواهیم دید: آیا این رهبران جدید با مردم متفاوت رفتار می‌کنند؟ مطمئناً امیدواریم که اینطور باشد.
و اگر اینطور نباشد، می‌توانیم وقتی رفتار واقعی آنها را ببینیم، بفهمیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66424" target="_blank">📅 14:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66423">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBojysGUoTs6wGE7WxqSrPi-2hKZ6x2lQiaFdFjDOC1fdMgJpw4TCtBuUIg86xrs__StiwWwkbXFGa9cfjo4IbxnBozPSUA4DiPq5Ndw3YAJKrWR1F93zYGoyLhmLihVFkVSJ-i36-bWDbfnu9lp_OJBwZyfvSRoxRgavwaIyUoC9543gGyEfagkx2b_IZpXbu4tw1Ys2QFV19sBpuYA7QP2isWVa5xKZNlOxNbbiA2mLeV0BXLlKgdSzB2V4gSkgDJK5C0Tjcb7OxSSuxMUO_ajj4S8pYkOPX4HNy-CRKKWV2HdEa74yx1BLxCee2u4r9lA3S6Gf3hqtT1pMRMRbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حملات اسرائیل به جنوب لبنان همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66423" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66422">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66422" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66422" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66421">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jV8Fpo0gLQMfwEJB5y9ob-wFNUtGB0_borfqrEpnRXfKI5cW6AJT3Zfgam1sKj0qj1nt8KvEExAH--ZU17SR9l1jhBrYRipXLfKXLBBFTVM-o5BGHHQdumf2Ku1_tlqzlXCiyKbf7E-SlVYxJrXEV7aNSL8Co0hMAVGzqMMcH7SrBO8-RsLnEBqW_c_x_iXIaFecCl1-gH24HvuP9xBAAHP-B3V3k6931m5zpNYG0VoRWqtCN2-K2DJWQzYXgczBeitFyaZODXVLbH5cSD09Zqnrj4k8g2RbBi45CmWCcXVf4VR4le_gB850P5p_Dca7W2EEhyH7iCwFnw3TuICffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66421" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66420">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvcIAAK5QI3pRGqApP63bVmwuAI_HRemMZGKthj0oAx2RXdqYsnMZEd_pji1kdYhlRiZG5a0FNAe2K2Au3O1sTkJd4FIIcPMjmdHfXBgRR2oVKPXvnEFrJnm3nlRqnLa5_p6F2-oafaXjVOpKDdlYbmk6lIbGfdhvTopfGa0_DEQb0ZcTqNXT-hQ4TNBm6dWZ140nQr4HNNpXIZ82sAES8wdfgirzu9SapExavGlNlhuafLC7q7zhwf-DAD0kWiW3cZ8gHM-iQ00ygzVEzOCYMFMDDgjpGahMqmXCR4GMYpiV6ZnrQ-a8bxXd8_mHOdv2NnRJTCpPlGzN1WKVKSHVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امضای پزشکیان از نزدیک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66420" target="_blank">📅 13:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66419">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1890fc432.mp4?token=CR_dmK4i3qsRkEQC_HNyGAJwW6svU51LgieT6CvHNa2h4SErl_-f4HzoRe6Qjo9UQrOKdQU_zVfnhPgVHnGnj5aYUx4tH3HLD7bK8M9FnZL2F1PhsobjTs6vF5XLAzVHDL3QJJE2iZBmYzETCArMYzvZCUqmcRH-CsoDwEPpiZZBl_cW67zhwJBPxshFY2dYBJnpBj6QuhC8P5oOykrM9ttmXyyVBruFU1M-sShfmB-sj0TE-1M-qDuOh9puMLO2ZJBE3HcXFS38AlbXLQlgBu9tCY67cH8TmLWxNW1WmFr2o8iRyuedPUVMPxEwmfBI2S0uQ-wuzMF8Sf5X_mU-dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1890fc432.mp4?token=CR_dmK4i3qsRkEQC_HNyGAJwW6svU51LgieT6CvHNa2h4SErl_-f4HzoRe6Qjo9UQrOKdQU_zVfnhPgVHnGnj5aYUx4tH3HLD7bK8M9FnZL2F1PhsobjTs6vF5XLAzVHDL3QJJE2iZBmYzETCArMYzvZCUqmcRH-CsoDwEPpiZZBl_cW67zhwJBPxshFY2dYBJnpBj6QuhC8P5oOykrM9ttmXyyVBruFU1M-sShfmB-sj0TE-1M-qDuOh9puMLO2ZJBE3HcXFS38AlbXLQlgBu9tCY67cH8TmLWxNW1WmFr2o8iRyuedPUVMPxEwmfBI2S0uQ-wuzMF8Sf5X_mU-dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظه امضای تفاهم‌نامه توسط شهباز شریف نخست وزیر پاکستان
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66419" target="_blank">📅 13:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66418">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fdfa7aaf.mp4?token=E5XjBsat0-BlBqDGtU9kloCa9jLu8NVEFJmRdaLUUQcdUfMQI9lbBFS9D9znR498BxrtDtUoimPyWgqQaIeHGMONtS8imN36thA2ZO0b3dTSOKIxH3H4_VKqTDAmCLVT7CfrnBlf3RKz2-2i_McFNN9J7kdVvmrlo067YiCS3EAZS5ImmTxLpI1_-VtPXiJOQvAhvBrMYkTro2BT4B9xY73ebrdM1MGgWcEt9JdRu1dMwVhhjgREmkWiuYbhNeSDx0BlN8AL-PYaCyvcXpKXiqxhFwf8uT-bYV7Xay52XYHF73J6_AtXdY3ciaoGOOBrkvRsBj0fnkGcTGMWflK8bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fdfa7aaf.mp4?token=E5XjBsat0-BlBqDGtU9kloCa9jLu8NVEFJmRdaLUUQcdUfMQI9lbBFS9D9znR498BxrtDtUoimPyWgqQaIeHGMONtS8imN36thA2ZO0b3dTSOKIxH3H4_VKqTDAmCLVT7CfrnBlf3RKz2-2i_McFNN9J7kdVvmrlo067YiCS3EAZS5ImmTxLpI1_-VtPXiJOQvAhvBrMYkTro2BT4B9xY73ebrdM1MGgWcEt9JdRu1dMwVhhjgREmkWiuYbhNeSDx0BlN8AL-PYaCyvcXpKXiqxhFwf8uT-bYV7Xay52XYHF73J6_AtXdY3ciaoGOOBrkvRsBj0fnkGcTGMWflK8bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیرزن کسخل مکرون دیروز موقع عکس یادگاری سران گروه 7 نزدیک بود زمین بخوره و شانس آورد ترامپ بغل دستش بود گرفتش
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66418" target="_blank">📅 12:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66417">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">قطار پیشرفت آموزش و پرورش کشور خدایا شکرت   @sammfoott</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66417" target="_blank">📅 12:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66416">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJ-CKa64ZEH1GdKc_Aa1kF9i8Jj2rNnRcAJkBnSjTtpxSkFTEzSxOplngnMIfCuucQ_4NNBAMhmPVQGww3EXafG9iP5Za9Rbf6wNnh0L2AGw0oiVA6V9FcMpM4ST4kQxumkuDDILtFXMX6PuNQbhqBasTx_yWMTfnB6PQEcyH876Pt3aZEzj0XwSWLAwHV5GzHRCSFNabSqCXyekPDLV48PMXRy5ZnyFf2EfCkwQPxP_1r6eJfMWwMu3E6ryu5EDqrVSDPbXPYheLD8hvR2TPn8MMFkBfsDOVPTh8m7lktL8bFF8m1StgHzYVGL-JDkNvA6jsXNF6EOObeY_CZtRUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«این احمق‌هایی که فکر می‌کنند من با ایران به اندازه کافی قاطع نبودم، در حالی که بازار سهام به تازگی به سطح بی‌سابقه‌ای رسیده و قیمت نفت در حال «سقوط» است، یا حسودند، یا آدم‌های بدی هستند، یا احمق. بیایید دوباره آمریکا را بزرگ کنیم!!!»
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66416" target="_blank">📅 12:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66415">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16c0579b45.mp4?token=qbqe7742JWsmH66VSPDJRgI2FCn5S58K9XorWB8XgaeKzxuGxnc7l6DCH7cIZtMMj4LGbr7vDqdGY1qMcIAL-wDDFr6AXyk4RRwzR0-V56Y0PUNaZVTraDQ1Of1MfTI_qI_iASgKLBEB_XqBtSkHkGJgwH0MV0KQeiK6xfXLrDb9Zv138yqo8sPpM1TWmpH-CHUr1Xk4Bpq-cONQeXZCVz3jXiM7WKvEQuBZpr4-VxugeBdmU29V2l9Em_I3S5X31ScFMMuKRdAPnzcM7hPBLJfRReTXiK0nK80n9doCuuGAAe_msOpEk1iAaRaRfholPNGMUTN790WZivliBpOwoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16c0579b45.mp4?token=qbqe7742JWsmH66VSPDJRgI2FCn5S58K9XorWB8XgaeKzxuGxnc7l6DCH7cIZtMMj4LGbr7vDqdGY1qMcIAL-wDDFr6AXyk4RRwzR0-V56Y0PUNaZVTraDQ1Of1MfTI_qI_iASgKLBEB_XqBtSkHkGJgwH0MV0KQeiK6xfXLrDb9Zv138yqo8sPpM1TWmpH-CHUr1Xk4Bpq-cONQeXZCVz3jXiM7WKvEQuBZpr4-VxugeBdmU29V2l9Em_I3S5X31ScFMMuKRdAPnzcM7hPBLJfRReTXiK0nK80n9doCuuGAAe_msOpEk1iAaRaRfholPNGMUTN790WZivliBpOwoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط اونجاش که یه موز و دوتا پرتقال بود
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66415" target="_blank">📅 12:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66414">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb19ef0a8a.mp4?token=V7Vo6xi2D0dFhOGzp-zAe4FkFH65HNz14EPC-Hh2Cb6PXyh5C6aF3KhiI6GHtfbF-U_vE7gQo05fOkw2uuTNt_TrWXzrGdsuhlJqmqcvJGD7RpmCeEEXkZ9QPQnA9NLogFFacBT77QeiKv3hjYrucGEq7e1m9PKBEqiJi-8VjRZ39H7Mxp6jJRfabF04Eb43zVLstCuMDMMhdII8eYK8Q5R7gmkCkUDW7qRKSocEjkpBlcDvaHm0bJSdTPs4o7nzzuwiFq5hTrlqQtbftEwA4U_peGVTZj59mCljfDpOFj_YYjuudYD9pyFmZKGLfQjQGRUB9fkJ4SDog_RXqztLpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb19ef0a8a.mp4?token=V7Vo6xi2D0dFhOGzp-zAe4FkFH65HNz14EPC-Hh2Cb6PXyh5C6aF3KhiI6GHtfbF-U_vE7gQo05fOkw2uuTNt_TrWXzrGdsuhlJqmqcvJGD7RpmCeEEXkZ9QPQnA9NLogFFacBT77QeiKv3hjYrucGEq7e1m9PKBEqiJi-8VjRZ39H7Mxp6jJRfabF04Eb43zVLstCuMDMMhdII8eYK8Q5R7gmkCkUDW7qRKSocEjkpBlcDvaHm0bJSdTPs4o7nzzuwiFq5hTrlqQtbftEwA4U_peGVTZj59mCljfDpOFj_YYjuudYD9pyFmZKGLfQjQGRUB9fkJ4SDog_RXqztLpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
با همچین عزیزانی تو ممکلت هموطنیم :(
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66414" target="_blank">📅 11:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66413">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6af0a234cf.mp4?token=g0dRsnzTXWeSFU2YCzHgdoa7Sx1nxirMZRzq3GrFXubRFMOPPSXD3Z46kva4BBtC21osIq81C6NN5bRbO1JFau5529pLWadkH4NqD0jiv2pBN8itjbVA5qfi16ljNT2ABZ4lKgDafcXjq4UFN5cTV_4qxdHU6stN7WTXKqXmIxIYv9Je5q5BZEfuiGx2mIqIrjKOsAxcDk47WcSvlzeTiXJ1Es5dUP98EqjrqPIlEbdXtAEnFDbReFJRviu-FskuJ3AzYulC8lqKifqW8ITzkeXpvaDKVngT5L7SlrB_DX5nF1eEPa7kMNvdQoJzA_Jf2Odr-kT7uTUbPq09fsgjZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6af0a234cf.mp4?token=g0dRsnzTXWeSFU2YCzHgdoa7Sx1nxirMZRzq3GrFXubRFMOPPSXD3Z46kva4BBtC21osIq81C6NN5bRbO1JFau5529pLWadkH4NqD0jiv2pBN8itjbVA5qfi16ljNT2ABZ4lKgDafcXjq4UFN5cTV_4qxdHU6stN7WTXKqXmIxIYv9Je5q5BZEfuiGx2mIqIrjKOsAxcDk47WcSvlzeTiXJ1Es5dUP98EqjrqPIlEbdXtAEnFDbReFJRviu-FskuJ3AzYulC8lqKifqW8ITzkeXpvaDKVngT5L7SlrB_DX5nF1eEPa7kMNvdQoJzA_Jf2Odr-kT7uTUbPq09fsgjZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
برشی از سخنان تند شب‌گذشته قالیباف خطاب به ارزشی‌ها و تندروهای کسمغز
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66413" target="_blank">📅 11:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66412">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04da6f24fd.mp4?token=X6P2yk5uNBDkfTK9wejwEC_Anl8euoLy6nqMgjfMHIKQWOCkR6L-Cc5kR0kTsnE_rInwPLBGwQdtu0JHLRk_VthDWMRxoqR5AJ1yXE0923hJ6t3CnbbGt-6k5CFMpfPy_kTsLwHic-jor_A-K1tCREgFu5i1OMGZ2Tdj8cxXm69PLK-Syn4ljpeiZGVeA6F0Qb1XStoTt-feEsc074yFOG8qoZS93_mHAMXAHw4LCPT0r-cQSAxr6NQrHfySWwG0wINErTCGV5fn0SyzsNGZzquZ8TH5uOoAHQ8gVLwV7C49_z8DQqqDkaH5JnczwXER2UWvOycNfvfVjuFpClNX_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04da6f24fd.mp4?token=X6P2yk5uNBDkfTK9wejwEC_Anl8euoLy6nqMgjfMHIKQWOCkR6L-Cc5kR0kTsnE_rInwPLBGwQdtu0JHLRk_VthDWMRxoqR5AJ1yXE0923hJ6t3CnbbGt-6k5CFMpfPy_kTsLwHic-jor_A-K1tCREgFu5i1OMGZ2Tdj8cxXm69PLK-Syn4ljpeiZGVeA6F0Qb1XStoTt-feEsc074yFOG8qoZS93_mHAMXAHw4LCPT0r-cQSAxr6NQrHfySWwG0wINErTCGV5fn0SyzsNGZzquZ8TH5uOoAHQ8gVLwV7C49_z8DQqqDkaH5JnczwXER2UWvOycNfvfVjuFpClNX_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66412" target="_blank">📅 10:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66411">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc5db481b.mp4?token=tbBhxxc34usxiqyUaCMpRkuSWIdCVPMfGlWuXCYHdF5vLG4XME7AWQopZjfmSiihEOaFY-YjUn_BfxbDM831e_VZDXZRyCRPaaBrt2XRn7Frs_z_g07SAnrPvLMLWlyTHTvWPzZhJQtNr1dgcR9FjSzjkgRTsb-GECYgmaZ6pcu5Tdsl-qsuTzoi8brziRUM53-Q_LquPZAV-LG64CTvHcJ8CtnmXzmyeZkXWxTNSTHsiB_JcCoQ95VHMQKXIbjaF1aJM8ZoRBCwWe0e7ieu2S57Gji08GfXP3galnK6-sL_yYxqomnZD1ZYqAo87zLvGJYWHCYvA6RfKXweCryeTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc5db481b.mp4?token=tbBhxxc34usxiqyUaCMpRkuSWIdCVPMfGlWuXCYHdF5vLG4XME7AWQopZjfmSiihEOaFY-YjUn_BfxbDM831e_VZDXZRyCRPaaBrt2XRn7Frs_z_g07SAnrPvLMLWlyTHTvWPzZhJQtNr1dgcR9FjSzjkgRTsb-GECYgmaZ6pcu5Tdsl-qsuTzoi8brziRUM53-Q_LquPZAV-LG64CTvHcJ8CtnmXzmyeZkXWxTNSTHsiB_JcCoQ95VHMQKXIbjaF1aJM8ZoRBCwWe0e7ieu2S57Gji08GfXP3galnK6-sL_yYxqomnZD1ZYqAo87zLvGJYWHCYvA6RfKXweCryeTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی عجیب دو سال قبل شاهین نجفی درباره قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66411" target="_blank">📅 10:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66410">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f1770ac7.mp4?token=dwlW13niwl1ewRLJ6N53aoLuy4u5Sv1UfapDU28eTSCiEZzjpvcqMYWQCCMmbw5dWhlEKWtZIXDDq9eWuKQZaTGp7u8Up6f9O44mZ1aDiCcLzDc_3MJK5SDvxR5iFUzDjy2ZWTg4tFoZ0exQYI2tU6l53yG4rFbPXCpUgdECUgVJGT0paQzRMg4ZPJHsYRI_oUtjMDDKjep83xUJt1L8CJhPA3GCJNlscG0He0xx2OUbT8cjR0bp9fInpbk1yfG8Tx9zw3liahaOuq3s7c1OIhCdFMh789niEQAJ25uBLUOLlGaK0Rsr9CBeKYiF3Ctf8DOC1UhB935B5vI4iQsf3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f1770ac7.mp4?token=dwlW13niwl1ewRLJ6N53aoLuy4u5Sv1UfapDU28eTSCiEZzjpvcqMYWQCCMmbw5dWhlEKWtZIXDDq9eWuKQZaTGp7u8Up6f9O44mZ1aDiCcLzDc_3MJK5SDvxR5iFUzDjy2ZWTg4tFoZ0exQYI2tU6l53yG4rFbPXCpUgdECUgVJGT0paQzRMg4ZPJHsYRI_oUtjMDDKjep83xUJt1L8CJhPA3GCJNlscG0He0xx2OUbT8cjR0bp9fInpbk1yfG8Tx9zw3liahaOuq3s7c1OIhCdFMh789niEQAJ25uBLUOLlGaK0Rsr9CBeKYiF3Ctf8DOC1UhB935B5vI4iQsf3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
10ثانیه تراپی روح و روان
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66410" target="_blank">📅 09:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66409">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95de07e4f.mp4?token=AO-QR6cMqnaIjTsoR3-a6qDRHtfVB676Err_ZYjPSkO7al2Z-940gsmvivCciMDogKDq4Xm-SrCCrbM0PbW4aUT9PjK0re0MGMDHW7CLwZLUHxsPlfzbCWaCOL0fJquz1Q7MbFF0Kh7jL7uuMB4KxHyl_4VJjSv9v09KKKY8IRZzE-EBHwdxjcPtaQfAilzJVkYb7uF_F188R4dhufD_7WQ2tQadKDQ_Tq6qFKd-oxfD-OCljFYl8xYRJLzfYO9CBdWBesvSEeHg-wDeVKLhbxSq7L6VbX25tOBubmUugIUH_iGwsmmC2cU_BL1evMdjLJCe2XUVXHzFHl52m0VNFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95de07e4f.mp4?token=AO-QR6cMqnaIjTsoR3-a6qDRHtfVB676Err_ZYjPSkO7al2Z-940gsmvivCciMDogKDq4Xm-SrCCrbM0PbW4aUT9PjK0re0MGMDHW7CLwZLUHxsPlfzbCWaCOL0fJquz1Q7MbFF0Kh7jL7uuMB4KxHyl_4VJjSv9v09KKKY8IRZzE-EBHwdxjcPtaQfAilzJVkYb7uF_F188R4dhufD_7WQ2tQadKDQ_Tq6qFKd-oxfD-OCljFYl8xYRJLzfYO9CBdWBesvSEeHg-wDeVKLhbxSq7L6VbX25tOBubmUugIUH_iGwsmmC2cU_BL1evMdjLJCe2XUVXHzFHl52m0VNFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: چه مدت نیروهای نظامی آمریکا را در خلیج فارس نگه می‌دارید؟
ترامپ: هنوز به آن فکر نکرده‌ایم. احتمالاً برای مدتی، جای خوبی برای ماندن است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66409" target="_blank">📅 09:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66405">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UlhF8rwRtRhbclxVPkO6YJy9xpumISmgp1DmmhbRrvDRW_e5MmgSPWLbQuSOz-w5hghjZsW2xt_VOvZ4h6bdVHQuSyKWNeXMmvWSfgAR759GCXCeyjlPfQY4p0FduXIknfjMHww6Zu_CIChcjG6OBxzoD9rkw7glivmtaQFxasqYQ7r6DE-T1rYFA5f0rxIdetjGOH_gjlN1GwwmhR1VndI7yaXtkZ2WJR29l_VNoix1DGXrLdchuUSf0E10zmQRLPK_XNq3uiidE2OKc8HmLVE6IRDlqPhPw_k43NLuUhK9QjZWQxELBZ3Dub_0c5j41VuE08o1R-NeLbr9nzKkfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KA602aU6N0mZKo6rumBMFOKlDWl4QT8kCzcYpWULaDdARG0Ifc8cP4imNGAyLOnoXwlcCoKnjIejjt3iRK8McX5UsYvZeBA15jPd_cDLdvN64-SE5YjXrjgolspW41PsOeHs4Mqmb6Tufv6rHvPfy9ey9wL39CzAgQWf2BWhqX6gEIL1dhTSK3fmcGexxPnF3U6m8L5eusE2vsh9INy9e74hYI64X50EJeUvIFyUT9Nrgrcur_Wo1UdWIJVWIWXa5jiSdvPpX9LWFN2OjwG7J4V0StcGWhY0rSlVQczMPPnwaZR35i5_n78qBnHB4p6hZYl5hYfAoxrH25KFgeig7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E1kcFG6lxalmMZ5vzLC4Y05RH0a-3uejC1aOURKzf15M3UZ_E-TE3c7jaf0XnpNUofNCioQAt-bhy0X8D9ciu4akvVQ82w_BxexZKNoJ2akag5M-UYSR4YZdVO0yOA-IqBat_5I6fjvhDh6AA2LFAwQwxpds5DPDaP9ae8PhujXxzk96ZpDuwluaB-X3rxHAHbWyQ2WU-q-W2Z-Z5_ow0hBTWzACSzdOrJ7EuVuxWY_6--KTNeSA9f8efrLz3__qx3dpQUSidrBaHelP-pCsRfcm24v0Jdgcn0bYGgNoZS-rfCfO9YRqbsbAOoJ5YTXon2ABP3XpRN2slZ7Uj8ynAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇺🇸
#فوری؛ تفاهم نامه صلح توسط ترامپ و پزشکیان امضا شد  @News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/66405" target="_blank">📅 04:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66403">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDG97DH9MdVGkMOU4CmHgVK1Rs1SugSOQ5dgC79sHFURwxPoaG8wliri6vqD2RLiCKerU3NFSonjzb7MwY-vOu0pE-GeDat6qlxvSA76ccXAaRa6sTPR1DNq6y2hqZtbKKOLLc7Nnvp6cNTDqYJ40dJy6mlU1ssQHNNoU9iqSNKDiFNLcUxIMKfz6cxMF597gKUoWnMTfaMMyyuBnOiN2DxzIc2KVM4a13f9zGVotIQokVDBNjoCiMfWn8AtGw7Aen6nwdBg_jYMkiR13BPzaif7qcEt2qlUFbMebB_SrsSx3-cMe8PGqxKCir8WaQPItf12bdPLZa2zJrxN3b99QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be88e9229.mp4?token=UcP-FojUjGsZcS4Q8_grbOLnBeTHfWmH_CV2MTJsIq-pmb3tRR-B6ibFbeOt4JPhakpovsWSIAjfdFman05HvjO7xEd4kMO8O33iti9gPZYy9cvRz_3JHUYtVLfJehoyUNFoIEdoUryhhQIrhftAO9lB1Y5ASEnkJvAeMYXUTIf5AJmL-D5j5V7oaBOaedg9-hK2qb2oQlfqZcK7F7xDK28d5bhwarbzkSUJpUB1DCf6n2dglw7HaTtKdMJ9mWLscLh2vmhkV9c3CC-UJuQvPtXyEDCXfcB2OzoidkFUSAqWC1DaSR8H3YrH906z8zq716-hZ8ZdtudlXk2aKUI2_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be88e9229.mp4?token=UcP-FojUjGsZcS4Q8_grbOLnBeTHfWmH_CV2MTJsIq-pmb3tRR-B6ibFbeOt4JPhakpovsWSIAjfdFman05HvjO7xEd4kMO8O33iti9gPZYy9cvRz_3JHUYtVLfJehoyUNFoIEdoUryhhQIrhftAO9lB1Y5ASEnkJvAeMYXUTIf5AJmL-D5j5V7oaBOaedg9-hK2qb2oQlfqZcK7F7xDK28d5bhwarbzkSUJpUB1DCf6n2dglw7HaTtKdMJ9mWLscLh2vmhkV9c3CC-UJuQvPtXyEDCXfcB2OzoidkFUSAqWC1DaSR8H3YrH906z8zq716-hZ8ZdtudlXk2aKUI2_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇺🇸
#فوری
؛ تفاهم نامه صلح توسط ترامپ و پزشکیان امضا شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/66403" target="_blank">📅 04:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66402">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66402" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66401">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dkBOf4dPKvp_PEgXMw1qLqVueVl-YgTLigYhf7YTKEXAP6l6K9DGK3h05BSKzaeQmuvZe9IIOvMki1Db6uVZukRr62NuXgcgN339Z3rcAb00oQqe4qCldzKZ5RyM5bM1pcC9n7jveFdsmzMxs5_RMOXryYHdwzvYE9IMbzNJo3xhnK6Rm9rRUt6ZTMAgJcOoRTOBKcr_T9S26Afmw2vNVXGYDHTAQNge1G634oc9gcPLzbqyYs4lI5l_jSoZQNmAof2EJeWTP7wYhtLXiDrMvYJWHNDcGbdzgMAzcxlOSs4B0S6jesQcwMbgUHoC1u5vA_AZfQ5oZFiBAS1oxCGr4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66401" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66400">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pajn2VmeZjD39RBO9Ahdyg4lrNpV8CvmI43c-FOGMnrVAmE7eTyqR_5Z7x_J60UEp1_kqcFV3jCr_dMeoF1zLy3Pm1M0fKG_RqqJn0Vd9yrHJ-loU9ZUKCqfS3yK_13tBr3Lb5iv3pNxfGF-Br96CCOXXHfmaJnx4CzACoHMVJQvlcKNm2W50n-xECUu0Ofj6DCRaCKNn7KIdCHcxFhg4g0RP4MNn4et_4llLwutA1PInPX0iOhKgXVljRqSZmtkp2zMY-GSz1brfgBq_iyU1-SAVjOY6WZe8WgxhKmFreQXB3B81FOqWHqhIqK65pq6cUyf1VMa6NxbCngI-FD_WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66400" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66399">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
متن تفاهمنامه جمهوری اسلامی و آمریکا:
🔴
1⃣
توقف فوری و دائمی خصومت‌ها بین ایالات متحده، ایران و متحدانشان در تمام جبهه‌ها، از جمله لبنان.
🔴
2⃣
هر دو طرف متعهد به احترام به حاکمیت، تمامیت ارضی و امور داخلی یکدیگر هستند.
🔴
3⃣
توافق جامع باید ظرف ۶۰ روز مذاکره شود، با امکان تمدید به توافق متقابل.
🔴
4⃣
ایالات متحده بلافاصله محدودیت‌های دریایی خود بر ایران را لغو خواهد کرد، در حالی که ایران به تدریج ترافیک دریایی را باز خواهد گرداند. نیروهای آمریکایی در نزدیکی ظرف ۳۰ روز پس از توافق نهایی عقب‌نشینی خواهند کرد.
🔴
5⃣
ایران تضمین خواهد کرد که ناوبری تجاری امن از طریق خلیج فارس و خلیج عمان انجام شود، با بازگردانی کامل ترافیک پس از عملیات پاکسازی مین.
🔴
6⃣
ایران و عمان درباره مدیریت آینده و چارچوب دریایی تنگه هرمز گفتگو خواهند کرد.
🔴
7⃣
ایالات متحده و شرکای منطقه‌ای ابتکار بازسازی اقتصادی و سرمایه‌گذاری برای ایران به ارزش حداقل ۳۰۰ میلیارد دلار را آغاز خواهند کرد.
🔴
8⃣
تمام تحریم‌ها علیه ایران، از جمله تحریم‌های ایالات متحده، سازمان ملل و آژانس بین‌المللی انرژی اتمی، طبق نقشه راه توافق شده برداشته خواهند شد.
🔴
9⃣
ایران مجدداً تأکید می‌کند که به دنبال سلاح هسته‌ای نخواهد بود. مسئله ذخایر اورانیوم غنی‌شده از طریق مکانیزمی که توسط هر دو طرف توافق شده، حل خواهد شد.
🔴
🔟
تا رسیدن به توافق نهایی، ایران موضع هسته‌ای فعلی خود را حفظ خواهد کرد، در حالی که ایالات متحده از اعمال تحریم‌های جدید یا استقرار نیروهای اضافی خودداری خواهد کرد.
🔴
1⃣
1⃣
صادرات نفت ایران همراه با خدمات بانکی، حمل و نقل و بیمه مرتبط، معافیت‌های تحریمی فوری دریافت خواهند کرد.
🔴
2⃣
1⃣
دارایی‌های مسدود شده ایران به تدریج طبق رویه‌های توافق شده متقابل آزاد خواهند شد.
🔴
3⃣
1⃣
یک نهاد نظارتی مشترک اجرای یادداشت تفاهم و هر توافق آینده را نظارت خواهد کرد.
🔴
4⃣
1⃣
انتظار می‌رود توافق نهایی از طریق قطعنامه شورای امنیت سازمان ملل رسمی شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/66399" target="_blank">📅 02:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66398">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛بقایی سخنگوی وزارت خارجه:
تفاهم‌نامه به‌صورت الکترونیکی بین پزشکیان و ترامپ امضا شده. جمعه هم خبری از مراسم رسمی نیست و فقط هیئت‌های ایران و آمریکا به سرپرستی قالیباف و جی‌دی ونس تو سوئیس دور اول مذاکرات فنی 60 روزه برای اجرای تفاهم‌نامه رو شروع می‌کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/66398" target="_blank">📅 01:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66397">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
سخنگوی وزارت خارجه جمهوری اسلامی: متن توافق با آمریکا نهایی شده و به امضا رسیده
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/66397" target="_blank">📅 01:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66396">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac08f5fbc.mp4?token=Klb7paN_OYQozO11ZAoGw0mH9_7wd5vT2uOGfIlWLa7JjMWCrSZ8ak-QazRPw5yw48iVS20lKIyckR_mnSaAtZO33rW8NuWfnDdXVTLjygVv-M5xTMd0AgMFaS3BDF_9DmJp3sj6bUEagUEmox1sEaKuqA6fco9mvJXaQCojmAH965588UmFvqLWVFiNQ1rGul7KFm7-HF5FQi7gGrd-iq-95IwuC0LInwjPwAXwt6niG698CCzCq3P_kIfzj14Ry9VT3IaQyREYVf5Zgua3Aw0MRlPB-MeP_so2AIijrA97WVXfCuWqPHd9A4lE4TkEj-w3yQUlnWsR2BVVQNw0hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac08f5fbc.mp4?token=Klb7paN_OYQozO11ZAoGw0mH9_7wd5vT2uOGfIlWLa7JjMWCrSZ8ak-QazRPw5yw48iVS20lKIyckR_mnSaAtZO33rW8NuWfnDdXVTLjygVv-M5xTMd0AgMFaS3BDF_9DmJp3sj6bUEagUEmox1sEaKuqA6fco9mvJXaQCojmAH965588UmFvqLWVFiNQ1rGul7KFm7-HF5FQi7gGrd-iq-95IwuC0LInwjPwAXwt6niG698CCzCq3P_kIfzj14Ry9VT3IaQyREYVf5Zgua3Aw0MRlPB-MeP_so2AIijrA97WVXfCuWqPHd9A4lE4TkEj-w3yQUlnWsR2BVVQNw0hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
به محض اینکه آتش‌بس برقرار شد، دیدید که دشمن در خلیج فارس اقداماتی انجام داد و ما بلافاصله پاسخ دادیم.
آخرین نمونه آن حادثه مربوط به بالگرد آمریکایی‌ها بود.
علاوه بر این، دو ناو جنگی دشمن که قصد عبور از تنگه هرمز را داشتند، مورد اصابت قرار گرفتند و دچار آتش‌سوزی گسترده شدند - موضوعی که تصاویر ماهواره‌ای نیز آن را تأیید کرد.
از سوی دیگر، هر فرودگاهی در هر کشوری که جنگنده‌های دشمن از آن برخاسته بودند، هدف قرار می‌گرفت. همه این اتفاقات در حالی رخ داد که ما همزمان مشغول مذاکره بودیم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/66396" target="_blank">📅 23:58 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

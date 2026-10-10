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
<img src="https://cdn4.telesco.pe/file/Max4xZCaw2eu5CrsAEMtDcsIFEwbGh2jBREciEy66DkSj-2aBeNQqpcHuIcrS2VtjgqtT6BxfwJF3gPv20BVVNF-9HOiibPYeBaTWT29bsXmVl_ukHSCcTac0DCz0zWiQ6s1-Per4TVXbO0SawLoN_L2O_fvy1_WLKQiut8cE0JHPNvqyU6aRoz12InSxvVmcOo4TAXcsRJ9LRN-A6qWHdGJsS2mRJViFO9fs_obcGZlqV7yXdmWLYcQ-E4DpAJTBi5WIptMK9CNVVFAPgQNjBsv-xvQUXI0Gxi4EsYQrQ-6Lo6t5aa_W0dz7Wimk55u0hy61tdSvpo9RAeFI99ewg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 104K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 00:25:11</div>
<hr>

<div class="tg-post" id="msg-73082">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c88cca8dd.mp4?token=b0hxIHq-WVeAqkWYzK0o9X6Kp-aJQDevHDJ9t_VU8ZrUj-NMVhXOcsojBuT_0yfiTVzQeJRYdiXZMS6bu6_sUSt74pdrUTID0z0bZhwJLJR0J4_v1zTbSiXijlz1yYAhzSEZ6JBJK8X9xvf1-J4xtJe7wTv_dHcmb6GZdHKEH5JV7r8tusLhVD67KIK3KRD9I2rbB39ebOg7REVkX3feSCM9IX7wtLJX3iysjcoD9bIMF56Vm5vdwak_WIylsmlHJxRFUsR3Nix6zmEMZZsEX1O0vMVBpZxZ7iNeHfb4Eu3huy9QctRBNZ16GvLPV3jrfZ3dzx5qjFQKCektYQn5pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c88cca8dd.mp4?token=b0hxIHq-WVeAqkWYzK0o9X6Kp-aJQDevHDJ9t_VU8ZrUj-NMVhXOcsojBuT_0yfiTVzQeJRYdiXZMS6bu6_sUSt74pdrUTID0z0bZhwJLJR0J4_v1zTbSiXijlz1yYAhzSEZ6JBJK8X9xvf1-J4xtJe7wTv_dHcmb6GZdHKEH5JV7r8tusLhVD67KIK3KRD9I2rbB39ebOg7REVkX3feSCM9IX7wtLJX3iysjcoD9bIMF56Vm5vdwak_WIylsmlHJxRFUsR3Nix6zmEMZZsEX1O0vMVBpZxZ7iNeHfb4Eu3huy9QctRBNZ16GvLPV3jrfZ3dzx5qjFQKCektYQn5pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">املاکی درباره تنگه هرمز:
«داریم به این فکر می‌کنیم که اسم تنگه هرمز رو به تنگه ترامپ تغییر بدیم!»
@News_Hut</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/news_hut/73082" target="_blank">📅 00:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73081">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e93cc318ec.mp4?token=ovEGP5GUdXlZifTz9oPmBWZ6DZYuRAajftvt041pNq7MK9oqootpc-K9QehQUm3sWj3c_Y5QzLs9WuPTND2HHVr98N_GCLaowNzA2TL9P3YH3RyQU3bK-_ILQQSMKMnMzBL5NtWip4-RI2E7qynHpTZXn7AIil8GU5QO-uLzohZGYtUtLp2vDNeTgVW3U71_phe0NHT0bRT09Y7qdtKb0SlgiRE16smUVfAAAo9X3uhDpbK3rwM2_NXmRred-01ersAYQFJUHKHSEtBXZRlKcpq_odZO3iynE5eCGeP6JtjBANXjMaPQY1nHKTgHrtavoaugplTZ8d_ST9qzxBicPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e93cc318ec.mp4?token=ovEGP5GUdXlZifTz9oPmBWZ6DZYuRAajftvt041pNq7MK9oqootpc-K9QehQUm3sWj3c_Y5QzLs9WuPTND2HHVr98N_GCLaowNzA2TL9P3YH3RyQU3bK-_ILQQSMKMnMzBL5NtWip4-RI2E7qynHpTZXn7AIil8GU5QO-uLzohZGYtUtLp2vDNeTgVW3U71_phe0NHT0bRT09Y7qdtKb0SlgiRE16smUVfAAAo9X3uhDpbK3rwM2_NXmRred-01ersAYQFJUHKHSEtBXZRlKcpq_odZO3iynE5eCGeP6JtjBANXjMaPQY1nHKTgHrtavoaugplTZ8d_ST9qzxBicPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«می‌تونیم خیلی سریع به این ماجرا پایان بدیم. ایرانی‌ها نمی‌دونن که من تا حالا چقدر باهاشون مدارا کردم و چقدر باهاشون راه اومدم.»
@News_Hut</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/news_hut/73081" target="_blank">📅 00:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73080">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988c9468b6.mp4?token=WrrIVduOcgkHXjbv3Txmc1Wwxn4aRURoAQNOjve9IE0pw9aFWiRiRkBtDy4Ehgb_1mv4V8Z56LkqP6sq6yRoyos8PUQk1InFnEUB_RoSCWWT_nOUajafyOuYGrkLfOWLuNaXN9cdZ4QuppzKnh09WltEwDlLBF-Ax8akGnm5jgjQ_JIaRHO0Ucmyb2PKgQK35quuRm5m1q2gZTBXrO6_taR9APsycm97RG2pL0mhrLN6LQFDs8ZVRkWaDPPEV-YGwM1u5C1AYarpLP8dUylwz4ddLo-HdJvQo14YB6SmRpclUU3afluYBK-ipFzsNETLnRTvtxJ7-1UYZ4sI_rhGXSfNDNf-UATjPJ3H21QPFQufsPAS-l5n03tIUzYLgJtIQiXmnaBPanKztE_V63MObZXP8-ZzF3lsr24Pd1eMUS0IZlImJOjEeVYUHj_jghZK_EO8xoPV0YxnxWImBKUfQsEFt7Siad1L092ZDJ_0DY_kOeOUbufitNF-G9dgU5RoMxsGQMBglKF2CFKOqS-4hUXP65v3GhW2w4VAeMjrZ-9sTtCC_24Gbqnc_5U9hVYhGSAX5HR7vyQQurJd23ig-o2kPDxooRuJZP8UmBYgfMv5b_P9-uVajtsGGXv1DXYSDjrezdHXFqXmvACm0Jj-5wM7B7UhgdPzse4YJjqmN3c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988c9468b6.mp4?token=WrrIVduOcgkHXjbv3Txmc1Wwxn4aRURoAQNOjve9IE0pw9aFWiRiRkBtDy4Ehgb_1mv4V8Z56LkqP6sq6yRoyos8PUQk1InFnEUB_RoSCWWT_nOUajafyOuYGrkLfOWLuNaXN9cdZ4QuppzKnh09WltEwDlLBF-Ax8akGnm5jgjQ_JIaRHO0Ucmyb2PKgQK35quuRm5m1q2gZTBXrO6_taR9APsycm97RG2pL0mhrLN6LQFDs8ZVRkWaDPPEV-YGwM1u5C1AYarpLP8dUylwz4ddLo-HdJvQo14YB6SmRpclUU3afluYBK-ipFzsNETLnRTvtxJ7-1UYZ4sI_rhGXSfNDNf-UATjPJ3H21QPFQufsPAS-l5n03tIUzYLgJtIQiXmnaBPanKztE_V63MObZXP8-ZzF3lsr24Pd1eMUS0IZlImJOjEeVYUHj_jghZK_EO8xoPV0YxnxWImBKUfQsEFt7Siad1L092ZDJ_0DY_kOeOUbufitNF-G9dgU5RoMxsGQMBglKF2CFKOqS-4hUXP65v3GhW2w4VAeMjrZ-9sTtCC_24Gbqnc_5U9hVYhGSAX5HR7vyQQurJd23ig-o2kPDxooRuJZP8UmBYgfMv5b_P9-uVajtsGGXv1DXYSDjrezdHXFqXmvACm0Jj-5wM7B7UhgdPzse4YJjqmN3c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ایرانی‌ها می‌گن: همه رو می‌کشیمممم! همه روووو!
همچنین می‌گن: الحمدلله! الحمدلله! الحمدلله!
منم بهشون می‌گم: بابا، شماها واقعاً دیوونه‌اید!»
@News_Hut</div>
<div class="tg-footer">👁️ 555 · <a href="https://t.me/news_hut/73080" target="_blank">📅 00:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73079">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8279d9c497.mp4?token=S7EaSWCsMWDgYCBqBRtd8t00I7ieEMYEvTxzcSn4qTZMJ69OUIoDFtlpsWTh6WRf9HmQmMyGyaoZMy3qxFWrnOnivT4CZlUa4VP4fniIhl20bDVLx3diGxD9WKgOk6Md0rgHQJIWbsT3mG3XPw8PCqEkiRRFx-YctIvaeG89jsjMzGRdc9xE8Yh6QTYpi0-lGGfttZolwERHRDIkLdhm87xZP3YMGRM_BJEGTHwoQLhYEo1t7d1C6fpyUxTJ7OQJ2ms3CzzL_SxdBMLtzR4Hhvq3D3VInt1FYjG4jcJwnd09rrNiOjehJNX3-yTb0Vy13OxmCyT1krGdZoXVVzb5Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8279d9c497.mp4?token=S7EaSWCsMWDgYCBqBRtd8t00I7ieEMYEvTxzcSn4qTZMJ69OUIoDFtlpsWTh6WRf9HmQmMyGyaoZMy3qxFWrnOnivT4CZlUa4VP4fniIhl20bDVLx3diGxD9WKgOk6Md0rgHQJIWbsT3mG3XPw8PCqEkiRRFx-YctIvaeG89jsjMzGRdc9xE8Yh6QTYpi0-lGGfttZolwERHRDIkLdhm87xZP3YMGRM_BJEGTHwoQLhYEo1t7d1C6fpyUxTJ7OQJ2ms3CzzL_SxdBMLtzR4Hhvq3D3VInt1FYjG4jcJwnd09rrNiOjehJNX3-yTb0Vy13OxmCyT1krGdZoXVVzb5Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور گلشیفته فراهانی در فیلم Matchbox: The Movie 2026 و صحنه لب گرفتن او با جان‌سینا!
+ نکته جالب اینکه همسر جان‌سینا هم ایرانیه!
@News_Hut</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/news_hut/73079" target="_blank">📅 23:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73078">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be8b607f1d.mp4?token=f7OP2mOzNdxuZRFid9EabqNQeCZZMPgrrwhyXBZm2VxbxnFAXAljS6SFpNsPwcBUCTsCqnibfb1CUOhyv82Fuzw6kB7WmL1_ci3gY5Ty2YcYAuLhy-iCt4O7y2J4NhPE9M36JhhTZZ9IDoee-eorNI_hH9LXaiJqlng2kysVWAoB6jorqkBedLg3UA1iEQgyY_1llRyTvK9qHWBh9mgutP4tAsDW4VyB1YScICYjHq7diOAeqHriUBtyOiBGAmZV7b_ggGYrNKAcsdy50DolopPaiwfwarhv-cuE6AJGt-WwmZEMgAWGnaEoj5aJ2-3nxOGN-XetFLO9M9dOne2wRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be8b607f1d.mp4?token=f7OP2mOzNdxuZRFid9EabqNQeCZZMPgrrwhyXBZm2VxbxnFAXAljS6SFpNsPwcBUCTsCqnibfb1CUOhyv82Fuzw6kB7WmL1_ci3gY5Ty2YcYAuLhy-iCt4O7y2J4NhPE9M36JhhTZZ9IDoee-eorNI_hH9LXaiJqlng2kysVWAoB6jorqkBedLg3UA1iEQgyY_1llRyTvK9qHWBh9mgutP4tAsDW4VyB1YScICYjHq7diOAeqHriUBtyOiBGAmZV7b_ggGYrNKAcsdy50DolopPaiwfwarhv-cuE6AJGt-WwmZEMgAWGnaEoj5aJ2-3nxOGN-XetFLO9M9dOne2wRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پلنگ حکومتی :هر روز صبح و شب اینجام که بگم ما فقط جنگ میخوایم  و مذاکره نمی کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/news_hut/73078" target="_blank">📅 23:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73074">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a72e1a5c.mp4?token=UwAahyPSYtiXC0snjrW8iGXE7I6DPJWVu1TrX0B7RhQc6522jICdR6abiQKr1GVgwwWtKhwLHgj2WNohgXkYQEKmAwmc1zQap-8dbZdwOAe_IERGREYV6UL2viej_OhAeXdLNNfkPoFXWcA2IMbk6krY6XY-o2stpE-iKYpAeq1g1JZ1kqE0T-dT2GGrQG9samkIVW3ji1-sMNeoMY7lYCCjFQmAGF5zwsGg2vgrZgJN6LOGwV7fG-evYJX5riesLILNyq-vW9gYlTWB8RWd3FVTCq3-I5SAQ6nqI2Nj0Sd5-jmYXfhyDlZetGklcCZyPZpS39_KcDxFxNwBGkMtcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a72e1a5c.mp4?token=UwAahyPSYtiXC0snjrW8iGXE7I6DPJWVu1TrX0B7RhQc6522jICdR6abiQKr1GVgwwWtKhwLHgj2WNohgXkYQEKmAwmc1zQap-8dbZdwOAe_IERGREYV6UL2viej_OhAeXdLNNfkPoFXWcA2IMbk6krY6XY-o2stpE-iKYpAeq1g1JZ1kqE0T-dT2GGrQG9samkIVW3ji1-sMNeoMY7lYCCjFQmAGF5zwsGg2vgrZgJN6LOGwV7fG-evYJX5riesLILNyq-vW9gYlTWB8RWd3FVTCq3-I5SAQ6nqI2Nj0Sd5-jmYXfhyDlZetGklcCZyPZpS39_KcDxFxNwBGkMtcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هوایی اسرائیل به ساختمانی چندطبقه در غزه
دقایقی پیش، جنگنده‌های اسرائیلی یک ساختمان چندطبقه در شهر غزه رو هدف قرار دادن. پیش از حمله، دستور تخلیه ساختمان صادر شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/73074" target="_blank">📅 22:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73073">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6e7ebfe2.mp4?token=YhEqprRZQ-3SiXWWjMYiq7jHoJSfmC895_15NFXNEK9G7oY2j9d9baJHb-kva-iWwK7ohuYjntdR3-F7-rnpRWZXuXM5wvX6rlTWSHq03ODrIZo3pQEbYqZN18YcFzh7elgHa9q6AD33YHdHdGgcv90-zRMoRe-MFkGzz6286URr5YLXPQxrLtsbC6zmfTMdRj53szn8quMulFcnfFT3U9TOyJw4CppFIPQZ7E2p7rDzZkI-_TFUSvY48lTIpL7LEO_eFyW3Fr6BIydbdylPe_AGRAM_vkUWLdqJr3OIT_RoJscJn3cy6jWZofmnN9f8xlgauLKHXP5kZK7OtvgSYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6e7ebfe2.mp4?token=YhEqprRZQ-3SiXWWjMYiq7jHoJSfmC895_15NFXNEK9G7oY2j9d9baJHb-kva-iWwK7ohuYjntdR3-F7-rnpRWZXuXM5wvX6rlTWSHq03ODrIZo3pQEbYqZN18YcFzh7elgHa9q6AD33YHdHdGgcv90-zRMoRe-MFkGzz6286URr5YLXPQxrLtsbC6zmfTMdRj53szn8quMulFcnfFT3U9TOyJw4CppFIPQZ7E2p7rDzZkI-_TFUSvY48lTIpL7LEO_eFyW3Fr6BIydbdylPe_AGRAM_vkUWLdqJr3OIT_RoJscJn3cy6jWZofmnN9f8xlgauLKHXP5kZK7OtvgSYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضرغامی: پخش خطبه‌های نماز جمعه از اشتباهات من بود!
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/73073" target="_blank">📅 22:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73072">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/be565181a8.mp4?token=rijKJeC98RgQeBA4h8j01Oe3RaOeqWnUPvd4BqCryOuoK95AFtRW15rnrKrG9DQQ-K86EqDwEYxnFSBtIC-46FMVHJI_KmgRg4BJZgJxNNC9Bfgw9i2sxMaHHlZl88vgUCs2QbbH6-hWZbnlMEmFd4vgD407_3FRsZ8VKBFe95DThDcgAp9xFJNFdmk59-JhYe2LYHCVfj_1QMJLLluHWV6LITN2AQp1xsXpkpTPk6GjAOgUVk7ks0NIuULhLdXt4b3xbCRPBRK_61w1qN77ht12zymNR-rp9uL_xIUogcLJkc0GNRi3f5ZGHcdCXoNXoS2UTmT8wLxUJ08iSOncTA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/be565181a8.mp4?token=rijKJeC98RgQeBA4h8j01Oe3RaOeqWnUPvd4BqCryOuoK95AFtRW15rnrKrG9DQQ-K86EqDwEYxnFSBtIC-46FMVHJI_KmgRg4BJZgJxNNC9Bfgw9i2sxMaHHlZl88vgUCs2QbbH6-hWZbnlMEmFd4vgD407_3FRsZ8VKBFe95DThDcgAp9xFJNFdmk59-JhYe2LYHCVfj_1QMJLLluHWV6LITN2AQp1xsXpkpTPk6GjAOgUVk7ks0NIuULhLdXt4b3xbCRPBRK_61w1qN77ht12zymNR-rp9uL_xIUogcLJkc0GNRi3f5ZGHcdCXoNXoS2UTmT8wLxUJ08iSOncTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند وقت پیش مصاحبه یه دختر 25 ساله منتشر شد که ماشین 50-60 میلیاردی سوار بود!
بهش گفتن چطوری این ماشین رو خریدی؟ گفت تلاش و استمرار!
رفتن امارش رو درآوردن، دیدن باباش حسابرس شهرداری تهرانه و دختره آقازاده‌اس!
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/73072" target="_blank">📅 21:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73071">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118178a3fa.mp4?token=r0cn0CEiA8Bxf4LT_j1CihIodQ-y2RnMHLzV-9V64pBC4o_ms_wlAy5Pdqql8bhxfFP9xMUpxa5vF652i0JZwdW4sCCnReZlLsJJr1jAWK2nCXJPpucT3nQdJbSGnkUE8J42NpkNSl-Db5-hOHF4FdG99oqBuRxlPOTZpypcWlmofPlmlu7I7uIjd8cbIF6Bslx6iQvvYaARjIIsXrNuv9t25Sl-ZfxSGodydL-ysaDWcPxgE3bspNckogbJKqjbLv7ehQpFIt5gWXShARAI6uNnulQDbIQFhoTTStKxr72WFo0yrLb690E1Iw-YC2MeHThrFob7rgkba8hdgdTDOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118178a3fa.mp4?token=r0cn0CEiA8Bxf4LT_j1CihIodQ-y2RnMHLzV-9V64pBC4o_ms_wlAy5Pdqql8bhxfFP9xMUpxa5vF652i0JZwdW4sCCnReZlLsJJr1jAWK2nCXJPpucT3nQdJbSGnkUE8J42NpkNSl-Db5-hOHF4FdG99oqBuRxlPOTZpypcWlmofPlmlu7I7uIjd8cbIF6Bslx6iQvvYaARjIIsXrNuv9t25Sl-ZfxSGodydL-ysaDWcPxgE3bspNckogbJKqjbLv7ehQpFIt5gWXShARAI6uNnulQDbIQFhoTTStKxr72WFo0yrLb690E1Iw-YC2MeHThrFob7rgkba8hdgdTDOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: زلنسکی گفته توافق نفتی شما با پوتین نشونه ضعف شماست.   ترامپ: کی اینو گفته؟  خبرنگار: زلنسکی.  ترامپ: باشه!  @News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/73071" target="_blank">📅 21:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73070">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2bf843dd2a.mp4?token=WmfNCHslyN7Qz9N4tgU-tsvL9lvRnxpHm4nv4urux2YtzrzE0SVAQp5o8SLkH2_LPCflQGgaCEYfQ_Up4qouIv8TmhzDliKF-fwYK9Va1eUUXmmYtS4bc6HWzu8h1R2vB-WJ-ux0Ucx9-yyQKNoTnumDOHQfiAqAZh_nP4voS349Q89v2ps5DfStUwuHWZMluu7XWTCABlwfwVRq7Ij7EJVdaDbPwaCBPDlyOkbYbNub4jZfU25TSseozglAdSHT-YiY98HGAC6J-9xQBlWfc0r3HqKED7HhmFGmuYPogcybXmGBa5lzQ7VlmlGQXz8s9kA5tGJP6n4Czeil77_2pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2bf843dd2a.mp4?token=WmfNCHslyN7Qz9N4tgU-tsvL9lvRnxpHm4nv4urux2YtzrzE0SVAQp5o8SLkH2_LPCflQGgaCEYfQ_Up4qouIv8TmhzDliKF-fwYK9Va1eUUXmmYtS4bc6HWzu8h1R2vB-WJ-ux0Ucx9-yyQKNoTnumDOHQfiAqAZh_nP4voS349Q89v2ps5DfStUwuHWZMluu7XWTCABlwfwVRq7Ij7EJVdaDbPwaCBPDlyOkbYbNub4jZfU25TSseozglAdSHT-YiY98HGAC6J-9xQBlWfc0r3HqKED7HhmFGmuYPogcybXmGBa5lzQ7VlmlGQXz8s9kA5tGJP6n4Czeil77_2pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه تصاویری از آتش‌سوزی گسترده و نشت نفت از یک نفتکش منتشر کرده که به گفته این نیرو، بر اثر برخورد با مین دریایی در تنگه هرمز آسیب دیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/73070" target="_blank">📅 21:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73069">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3875ef3f4f.mp4?token=fJhMP5n7bk9K_RAXPgEe62UrpqSTRb6hLFObDvAtpQVjroFv2GSO0bOdbSGjILiF-hCpdUffdIzZOB7PB5Kjjf98dIygDpJhWgNmlw33THmu6ti8DE67HVQLVBd3O4H813Y15L6znFNVhbUmdZGplZDqbNSygZrBCDK3hp5ZR11wPcNvdlV_KvxpKcpxvkUMVRoGYAtMWxQniEIlc3oWGKD11tn3j6kGHisy4I5kcKh1nXrpv_o0wuPqCeZhIzoAfL-YzajDplCpdvkUEYfi-kvsDKU-pEjgsaacW2jzVTuFYMIiP7hm2KZl0u0h6c4ETPwmzedu74EfnOZhRztQGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3875ef3f4f.mp4?token=fJhMP5n7bk9K_RAXPgEe62UrpqSTRb6hLFObDvAtpQVjroFv2GSO0bOdbSGjILiF-hCpdUffdIzZOB7PB5Kjjf98dIygDpJhWgNmlw33THmu6ti8DE67HVQLVBd3O4H813Y15L6znFNVhbUmdZGplZDqbNSygZrBCDK3hp5ZR11wPcNvdlV_KvxpKcpxvkUMVRoGYAtMWxQniEIlc3oWGKD11tn3j6kGHisy4I5kcKh1nXrpv_o0wuPqCeZhIzoAfL-YzajDplCpdvkUEYfi-kvsDKU-pEjgsaacW2jzVTuFYMIiP7hm2KZl0u0h6c4ETPwmzedu74EfnOZhRztQGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما گفته بودید تا بعد از انتخابات میان‌دوره‌ای به ایران حمله نمی‌کنید. حمله اخیر در عربستان باعث شده نظرتون عوض بشه؟
ترامپ: «بررسیش می‌کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/73069" target="_blank">📅 20:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73068">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba9c18ae3.mp4?token=sV2erhyZ1ZYbduww1A3mp-4JOYG3XTGUzk9HtoLuX9wArqLn9GbJrYAwbtxSE7EA3HlS7Jb5rUhUItw72jvjKn1JBnuxn75vDVWugs3nwPTq9oimdBKiGd2FkB53VjHxHQn3kk2-MimQ4pc6iTHogs3BVfA0k4Xxr8f0RB5oJ04r-m3gwDVQv_Bm9VsfO5nP-RAnv9wZyfO77LXCpb6F9p24GLGLOgeRJ__mCc9m3rou9Ee-5ViBSRNTVHKOmUMW0Mivbsvi673Mn_4UZCmW42q2lpPTxVHRYfBBMuX9Q1kmiFm8o9ZqeDxNB3i8lK8_afbEQ0-DMLy4fVOhLs69vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba9c18ae3.mp4?token=sV2erhyZ1ZYbduww1A3mp-4JOYG3XTGUzk9HtoLuX9wArqLn9GbJrYAwbtxSE7EA3HlS7Jb5rUhUItw72jvjKn1JBnuxn75vDVWugs3nwPTq9oimdBKiGd2FkB53VjHxHQn3kk2-MimQ4pc6iTHogs3BVfA0k4Xxr8f0RB5oJ04r-m3gwDVQv_Bm9VsfO5nP-RAnv9wZyfO77LXCpb6F9p24GLGLOgeRJ__mCc9m3rou9Ee-5ViBSRNTVHKOmUMW0Mivbsvi673Mn_4UZCmW42q2lpPTxVHRYfBBMuX9Q1kmiFm8o9ZqeDxNB3i8lK8_afbEQ0-DMLy4fVOhLs69vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در ویدیویی جدید که در تیک‌تاک منتشر کرده، در حال ورزش کردن در باشگاه دیده می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/73068" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73067">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89266c981.mp4?token=A7vNA1rpT1oqfMxSLvchlIKEE6C3mdNmbTd6Wmri2a2LdtUhbLrkkQfDdDDJxv7mwFcKtGeUNEdW0ksUd9nrmL4ff90QTkPkdb9TRKQra81L2KlNXCxMrDYxnqsKAAL6_ahtAxcqBrxrBHX3t7zSxaCu9P1rDN70oJdwpnAcujXAZ3P7ZCNieZK3UW6KdOddyYygpXo6Ci8n6kATmPlv5bo1FHvCWTaQB5usgFrFV3oFvNhuLv7qInS8dRnCALkGq9WyuC0zA07mDEVtmQ6iLm6CMk15wBB4ZBHvbukQKvLMM-LzMQzoSSjirtkywU7KuDnqfPp230kSbWjcglQVWYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89266c981.mp4?token=A7vNA1rpT1oqfMxSLvchlIKEE6C3mdNmbTd6Wmri2a2LdtUhbLrkkQfDdDDJxv7mwFcKtGeUNEdW0ksUd9nrmL4ff90QTkPkdb9TRKQra81L2KlNXCxMrDYxnqsKAAL6_ahtAxcqBrxrBHX3t7zSxaCu9P1rDN70oJdwpnAcujXAZ3P7ZCNieZK3UW6KdOddyYygpXo6Ci8n6kATmPlv5bo1FHvCWTaQB5usgFrFV3oFvNhuLv7qInS8dRnCALkGq9WyuC0zA07mDEVtmQ6iLm6CMk15wBB4ZBHvbukQKvLMM-LzMQzoSSjirtkywU7KuDnqfPp230kSbWjcglQVWYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رائفی‌پور: آمریکا را پایین کشیدن کاری ندارد.روسیه باید پالایشگاه‌های آمریکا را هدف بگیرد تا حملات اوکراین متوقف شود.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/73067" target="_blank">📅 20:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73066">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gmc9qyr64tkq-eAgpYoVYDocsLsSSq2qOLYPlY-ueQUel2iesLr3GtegyMBZ49bhNYpGSbJmMBydE1ZnSVSTQJYDRVj1K8knGSbfEn5RtgzzauqR5bO2rhjOcwhw3VQKJSyyZOZhxAZfgBGUZnAjmFUn4ED7zuMZz4Nb3_xyjSncNUAnFWPL3YLSlKldv6mY4eGjiO2LHjDjQSJ3tpcGBouEX8FP6kZolptVr1n707Mipry6caTFOHfIg1owEmqP1adiKPY0K4SUlZHITn63JLM06QciQmnRwdpJvNaJrpt_6HJay2lYo_fYPnA6ldpQT91yz4s0TI5aZb9RTgzJXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین محموله گازوئیل روسیه به مقصد آمریکا حرکت کرد؛ قبل از اعلام توافق ترامپ!
اولین محموله گازوئیل روسیه که راهی آمریکاست، ۲۲ سپتامبر از بندر سن‌پترزبورگ حرکت کرده؛ یعنی دو هفته قبل از اینکه ترامپ توافق رو اعلام کنه.
این نفتکش یونانی با نام MINERVA ZEN حدود ۲۷۵ هزار بشکه گازوئیل حمل می‌کنه و پیش‌بینی می‌شه ۱۱ یا ۱۲ اکتبر به سواحل شرقی آمریکا برسه.
تحلیلگران می‌گن حجم این محموله‌ها در مقایسه با مصرف گازوئیل و سایر سوخت‌های تقطیری آمریکا، فقط برای چند روز کافیه. از طرفی، حملات اوکراین به پالایشگاه‌های روسیه هم باعث کاهش تولید گازوئیل این کشور شده.
@News_Hut
| Clash Report</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/73066" target="_blank">📅 19:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73065">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3e4a880ec.mp4?token=VE1k6ra7PSe9kA1VDXN6BfG-bYdh8UTcCDAwqIrPKrbH_bbv3rDAFm70hMhTMDCBEpTxmjDT3z4Ns12a1pwMtzLr_OBCplQOqBVO0xWr_vXCdHpeg7ipp6TOCQh9qdCHmUrlZNTfXpkTsZb4Ap1GxltrXr6Suvvusy9fEqYH_HdKgGUZJwny7SGTWk3TI9LRF88m3Vo9M1jQiaV29x3NzoV8QQ1IRLPVbBxA5AM8vCHQLzXbupJkl5FvUayP4gFkQpAsaymtvab-W0Txn-jnTTP7LIYVFaaetWtguSRMaKLYJeeKAHnY8gmPaqTggIXcpGHMzSo5_xh0ZwsNe9M58Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3e4a880ec.mp4?token=VE1k6ra7PSe9kA1VDXN6BfG-bYdh8UTcCDAwqIrPKrbH_bbv3rDAFm70hMhTMDCBEpTxmjDT3z4Ns12a1pwMtzLr_OBCplQOqBVO0xWr_vXCdHpeg7ipp6TOCQh9qdCHmUrlZNTfXpkTsZb4Ap1GxltrXr6Suvvusy9fEqYH_HdKgGUZJwny7SGTWk3TI9LRF88m3Vo9M1jQiaV29x3NzoV8QQ1IRLPVbBxA5AM8vCHQLzXbupJkl5FvUayP4gFkQpAsaymtvab-W0Txn-jnTTP7LIYVFaaetWtguSRMaKLYJeeKAHnY8gmPaqTggIXcpGHMzSo5_xh0ZwsNe9M58Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان اجرای ارکسترال «آرش» در سالن اسپیناس تهران، در شامگاه جمعه ۱۷ مهر، تماشاگران در واکنش به صحبت‌های اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی، او را هو کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/73065" target="_blank">📅 19:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73064">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">برآوردهای اولیه از تلفات حمله به فرودگاه ریاض:
بر اساس برآوردهای فعلی، در پی اصابت یک تا دو موشک بالستیک انصارالله به ترمینال ۳ فرودگاه بین‌المللی ملک خالد در ریاض:
مجروحان: حدود ۴۰ تا ۷۰ نفر
کشته‌شدگان: حدود ۳ تا ۵ نفر
این آمار در حد برآورد اولیه است و هنوز تأیید رسمی آن مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/73064" target="_blank">📅 18:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73062">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f8abc61b.mp4?token=kbIatt-86O2qcSzykFr9rxi1KdQQfudQ5-dPTT5WP418JYH14yK9U2kXNg8rXI_rSbYXr3I13rpxbt205mftEfGu-iTPJrHEQ_H1IeyzhJ20cflNnH62GC21kkMyVK1opBmuckBT-hg36hIv-Vjs964HyCb2TaHofHiTBTDfIhkRUgXWi3-06pf7T4Q-97PHf3rtxga4zLqy-qi-XJjYdx2zNMz6-WAMLJJbt38hUTw7ZPZHp9P8tr0UH7hiThprWzEzQTN3St0mcrr2ilVirk67r_MV3Ki9vE2WNQp-VBLdxG0NOXBlf3H85mDgrOX-hC2G1a-pF46luj0KHPI36g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f8abc61b.mp4?token=kbIatt-86O2qcSzykFr9rxi1KdQQfudQ5-dPTT5WP418JYH14yK9U2kXNg8rXI_rSbYXr3I13rpxbt205mftEfGu-iTPJrHEQ_H1IeyzhJ20cflNnH62GC21kkMyVK1opBmuckBT-hg36hIv-Vjs964HyCb2TaHofHiTBTDfIhkRUgXWi3-06pf7T4Q-97PHf3rtxga4zLqy-qi-XJjYdx2zNMz6-WAMLJJbt38hUTw7ZPZHp9P8tr0UH7hiThprWzEzQTN3St0mcrr2ilVirk67r_MV3Ki9vE2WNQp-VBLdxG0NOXBlf3H85mDgrOX-hC2G1a-pF46luj0KHPI36g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از فرودگاه بین‌المللی ملک خالد در ریاض پس از حمله منتسب به حوثی‌ها (انصارالله)
در این تصاویر، آثار خون روی زمین دیده می‌شه و نیروهای امدادی گسترده‌ای در محل حضور دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/73062" target="_blank">📅 18:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73061">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گزارش‌ها از وقوع حادثه‌ای بزرگ در فرودگاه ریاض؛
گزارش‌ها حاکی از وقوع حادثه‌ای جدی در فرودگاه بین‌المللی ملک خالد در ریاضه. احتمال داده می‌شه یک موشک بالستیک حوثی‌ها (انصارالله) به این فرودگاه اصابت کرده باشه.
تعداد زیادی از نیروهای امدادی و اورژانسی به محل حادثه اعزام شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/73061" target="_blank">📅 18:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73060">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">#فوری
؛ خبرگزاری فرانسه (AFP):
خبرگزاری فرانسه به نقل از سه شاهد عینی گزارش داده که در حال تخلیه افراد از فرودگاه بین‌المللی ملک خالد در ریاض، پایتخت عربستان سعودی، هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/73060" target="_blank">📅 18:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73059">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc0bb8954.mp4?token=O6LF9Wcrlz3N9M9yAZNWIMA_yd1m1F1aptoNrcf5xJMmLy2kuGg-49dQecyo_VFdZh6Z5oEZbfCNLl_kxXO_jWcNkvn9_CHd60aNUIXllFr543GyjmVgLWgjqg7HNGS5Plx175dUY0FPZO2EHV-axOErf8zMVgUOvwz8e2o74u3tPAS6BwfhhP9IS3LA1DNsPLMwdQRYSq-TgLT4HodCrAGUbcNLoJruDO1ZGT29sY-1Fu8aLb-kL0O4pVmmsYuV-INOUACPDyss1qDJonBa_hLUzzcnTwF-z9WuLpAEDJcVI0BkpdFJuZF-i3rZpavSxhO2a8zOMpAJHuPjg_UMgXhWhMVGv1QXIUatf-LlCkNb-Qq0A4G8ArzNDQpwCcWWOiTwjP_mleIwX7MDHvnjhoT_HSOm9Ey3N4nmIhs77lv9_TO-lwvvhAq-Oc6QPauvlJ3glJYVR-_659xx0nFYs6Kd6iPVf1WnqFho32Se9drdSsHIz1deYm0Kqv-1TKov9LOyYul0HeZ_KpJxP2BaXRDh0SnN_BnuGIOISCDUt7o18EY_rTvRQv687I22tFyzeSvDap6EYfChPWcjwQNNnibF4Xn6IJJ9xAjyWH9V5vLo7t_aBNU-H_wS3zThL6Tg6D-IJCivUWx1jWda38njJ7ws1SJm-Hvts28FG9CdsKI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc0bb8954.mp4?token=O6LF9Wcrlz3N9M9yAZNWIMA_yd1m1F1aptoNrcf5xJMmLy2kuGg-49dQecyo_VFdZh6Z5oEZbfCNLl_kxXO_jWcNkvn9_CHd60aNUIXllFr543GyjmVgLWgjqg7HNGS5Plx175dUY0FPZO2EHV-axOErf8zMVgUOvwz8e2o74u3tPAS6BwfhhP9IS3LA1DNsPLMwdQRYSq-TgLT4HodCrAGUbcNLoJruDO1ZGT29sY-1Fu8aLb-kL0O4pVmmsYuV-INOUACPDyss1qDJonBa_hLUzzcnTwF-z9WuLpAEDJcVI0BkpdFJuZF-i3rZpavSxhO2a8zOMpAJHuPjg_UMgXhWhMVGv1QXIUatf-LlCkNb-Qq0A4G8ArzNDQpwCcWWOiTwjP_mleIwX7MDHvnjhoT_HSOm9Ey3N4nmIhs77lv9_TO-lwvvhAq-Oc6QPauvlJ3glJYVR-_659xx0nFYs6Kd6iPVf1WnqFho32Se9drdSsHIz1deYm0Kqv-1TKov9LOyYul0HeZ_KpJxP2BaXRDh0SnN_BnuGIOISCDUt7o18EY_rTvRQv687I22tFyzeSvDap6EYfChPWcjwQNNnibF4Xn6IJJ9xAjyWH9V5vLo7t_aBNU-H_wS3zThL6Tg6D-IJCivUWx1jWda38njJ7ws1SJm-Hvts28FG9CdsKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ملکه تایلند برای نخستین بار به تنهایی هدایت یک جنگنده گریپن سوئدی رو بر عهده گرفت و پس از فرود موفق، از پادشاه مدال دریافت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/73059" target="_blank">📅 18:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73058">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73058" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/73058" target="_blank">📅 18:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73057">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rueFUwZzHwfgNf0S4ik9jwHB81PSIMNeH9F1OOz43pe3nmH68_Of0t0bmp6KwHxmgXpuaBy5QjskJPrAliOFFEUubqnqL9aBhy_7i52u76wpxj-BUWpnrnzPwxjDd7JrZK-7D828ieo34Mhdw1TUEJlTGA5GIYoSEu8jPgAHNSbXxAeKO-MwOWSmuHpOlGe1CdCSNKtZjxMHkYw6StQT1p0Q0AIXm31o2dQe7tfY83XGSa0xba_b4RdrlRlG-r1AD1OPdy3kYXm2daVjM4bllccAEHNJw-JIKK0OfSgSkN6mpaMc9QK8-3l7lqGqBLMMudPXf1w7lrngEgt6aVZ0PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز ویارئال
🆚
رئال مادرید رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم در ۵ رویارویی اخیر:
ویارئال: ۲ برد، ۳ شکست و ۱۱ گل زده
رئال مادرید: ۳ برد، ۲ شکست و ۱۰ گل زده
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
https://TrexBet.com</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/73057" target="_blank">📅 18:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73056">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c52e5fb32c.mp4?token=Q6HeNdRA-H_-NOwIJxjyfI6qiiRshSs8hDsmRfzoND10Yy5KN1JkrLRFDDtTqxbhqwf6ZENadR5xgCQT3zOnZtvImRaTRy1lBXEfpYQPsIj9bMHht5BfdP-djqtyWaNwTQLyPA__Xsb9sQunFhL6U1M3aWFTeAAq6abIACM2237YPw7rZSmNDouBAPWnZINa9bDM4ZVCjyxMf8LiDBsqJIG2mO0ve0qBuZyjjiBxDsTFGJoaGq_J0CCwWINC_7Nzr_KOTptPL1bJ-vEv-fLlwcRjfdkRgzwSTzf1lekt9QXoP5clNW-GWZAFt0uo8upGNxAqmkGLxoIAnvbzuEQSg18h1eNiAGCjJXlenXGQi9VsvgJ3lJem0pIABcpYkeyDq167gXHA8FPso7ikgLS1kV7yasVzIwgJ9ftFa4k6E1f2ZnsjcKixoJ0WUgRijsb3rjKqcss-LNLofd9ZaShwxbRVFdEHG8mdZ-LKYl82Z8Gm6OFQHyCdAokxPRnT66MZE9dDzne26M2w0-gnvPN-1v35q4SgYz0oHnHMvOGRAqvDJmHu3klJ6DvaiuJ7us1VA7js2Hv32YWkm5BH4yjhggmKDvKpU9EyAwDO_NDovJktiQG-lobF7yCKyuYA2ijyHarOozVEgMmJzcjKsK1Jn7FK1y0k4jIIFOTbCZkvnig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c52e5fb32c.mp4?token=Q6HeNdRA-H_-NOwIJxjyfI6qiiRshSs8hDsmRfzoND10Yy5KN1JkrLRFDDtTqxbhqwf6ZENadR5xgCQT3zOnZtvImRaTRy1lBXEfpYQPsIj9bMHht5BfdP-djqtyWaNwTQLyPA__Xsb9sQunFhL6U1M3aWFTeAAq6abIACM2237YPw7rZSmNDouBAPWnZINa9bDM4ZVCjyxMf8LiDBsqJIG2mO0ve0qBuZyjjiBxDsTFGJoaGq_J0CCwWINC_7Nzr_KOTptPL1bJ-vEv-fLlwcRjfdkRgzwSTzf1lekt9QXoP5clNW-GWZAFt0uo8upGNxAqmkGLxoIAnvbzuEQSg18h1eNiAGCjJXlenXGQi9VsvgJ3lJem0pIABcpYkeyDq167gXHA8FPso7ikgLS1kV7yasVzIwgJ9ftFa4k6E1f2ZnsjcKixoJ0WUgRijsb3rjKqcss-LNLofd9ZaShwxbRVFdEHG8mdZ-LKYl82Z8Gm6OFQHyCdAokxPRnT66MZE9dDzne26M2w0-gnvPN-1v35q4SgYz0oHnHMvOGRAqvDJmHu3klJ6DvaiuJ7us1VA7js2Hv32YWkm5BH4yjhggmKDvKpU9EyAwDO_NDovJktiQG-lobF7yCKyuYA2ijyHarOozVEgMmJzcjKsK1Jn7FK1y0k4jIIFOTbCZkvnig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این دختر خانوم با این پسره تو رابطه اس و که علاوه بره پسره، سگ دوست پسرش هم عاشق دوست دختر پسره شده.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/73056" target="_blank">📅 17:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73055">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502e54151d.mp4?token=D3RWwAALgMc_6fCuWLm1XYKetfcPnoiXPHK6D5Elonb7GaY_f_pgOdLW6iwsOGKthDd1EeckU-zoVp4freeOEmFS4MyLf2gDYcs_KtNb1Ej2FkCP2QbyeCcMazeQiIZcBsIESOXYwAcSxYcY0GcHahs6p_vePWCDT7x_wWI5WQTjmfeYwKCVC80UJM8su0xvzU3GSANcf1Dy3eErDmaSau1Hn2uP732HdG8pUoDtR67PcWRfOU2Xr_48Yhml3jTCNtQHv5WkVKPs2xdxpVlP45AtOMypPy6EKhcHgHV_KHpm_-7qwmVhRepvHW2biCFWIZj9Lk5a22YwFUkZHhcmCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502e54151d.mp4?token=D3RWwAALgMc_6fCuWLm1XYKetfcPnoiXPHK6D5Elonb7GaY_f_pgOdLW6iwsOGKthDd1EeckU-zoVp4freeOEmFS4MyLf2gDYcs_KtNb1Ej2FkCP2QbyeCcMazeQiIZcBsIESOXYwAcSxYcY0GcHahs6p_vePWCDT7x_wWI5WQTjmfeYwKCVC80UJM8su0xvzU3GSANcf1Dy3eErDmaSau1Hn2uP732HdG8pUoDtR67PcWRfOU2Xr_48Yhml3jTCNtQHv5WkVKPs2xdxpVlP45AtOMypPy6EKhcHgHV_KHpm_-7qwmVhRepvHW2biCFWIZj9Lk5a22YwFUkZHhcmCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از بمباران پادگان سپاه در خرم‌آباد، استان لرستان، در جریان جنگ ۴۰روزه:
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/73055" target="_blank">📅 17:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73054">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_1kqOVWsCY_AA0MYAf7Pcb4GpTdxX2YucZwhJ01ZvoE9FssYlTQAbWO0clewYaAxB9jMOjneVtDgnkTxzqujUzxMQR6ohzJjWbDu80110Neb07cW1XrSYGGualBgj5UaSDrgzg8_jnJtwes-riNEXHGHGXLfvCU2c0UTOOgSAdIWuR5ZAXB8dJbd2Lu_hxgvdz5cI_wmhFcH-8qhGDhJq6jEt9ycOYy-6p2aA3vgxHzqff-M7k-9-2oTyYf3E1DoUx771NsOvCiIVnXdEAEh3nqeFfC3Ba5nmhIyzTP38mryfV1HEJxrCmJKSB3xJAWExrYKx8OpdObFrL3L9oytw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛
معاریو: آمریکا از اسرائیل خواسته به‌تنهایی به ایران حمله کنه!
طبق این گزارش، واشنگتن توی مذاکرات دو هفته اخیر از اسرائیل خواسته بود بدون مشارکت مستقیم آمریکا، حمله نظامی به ایران رو انجام بده.
هدف آمریکا این بوده که پیش از انتخابات میان‌دوره‌ای نوامبر، هزینه سیاسی حمله به ایران متوجه ترامپ نشه؛ درحالی‌که چنین حمله‌ای می‌تونست از نظر سیاسی به نفع نتانیاهو، پیش از انتخابات اسرائیل در ۲۷ اکتبر، تموم بشه.
ایال زامیر، رئیس ستاد ارتش اسرائیل، هشدار داده بود که ازسرگیری جنگ می‌تونه باعث تعویق انتخابات اسرائیل بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/73054" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73053">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fca26fcca.mp4?token=uAm4BSqU7sEGSTGlCFsMnqWpKfwDZn8pSapEiqs8nFxjJ7C9kHVdQ1-GL5TKkftHIp4kRz8ntWKH0gmRYzR7e_PuDA4UKn7F2qZT5GuW53-7BIt_OKaJI9uB8PWg3pnfqGX_3RdBvj5ZhqTXwel6FjN_8TGZgbOd-ZPNIpeg_NBh_R3NYnMmVmowlo-UN8Vsk-z8O4KpdbHzQmReJrBn8a1AEQL3HZ4M51672WMhiP0HxGKsY_zsP8Mo1sLRX2Lq2rik2ueu-_BPT6EgYG7VPw1sTUyIbA8-bQaMpaIYyVunVMHvAo2vK6Fl1FsVp2nf-PznRG1Bzl8Xxiy9yEEuKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fca26fcca.mp4?token=uAm4BSqU7sEGSTGlCFsMnqWpKfwDZn8pSapEiqs8nFxjJ7C9kHVdQ1-GL5TKkftHIp4kRz8ntWKH0gmRYzR7e_PuDA4UKn7F2qZT5GuW53-7BIt_OKaJI9uB8PWg3pnfqGX_3RdBvj5ZhqTXwel6FjN_8TGZgbOd-ZPNIpeg_NBh_R3NYnMmVmowlo-UN8Vsk-z8O4KpdbHzQmReJrBn8a1AEQL3HZ4M51672WMhiP0HxGKsY_zsP8Mo1sLRX2Lq2rik2ueu-_BPT6EgYG7VPw1sTUyIbA8-bQaMpaIYyVunVMHvAo2vK6Fl1FsVp2nf-PznRG1Bzl8Xxiy9yEEuKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظاتی ترسناک و باورنکردنی که امواج عظیم زیر رعد و برق یک کشتی باری غول‌پیکر را ناچیز نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/73053" target="_blank">📅 16:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73052">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xla5wut2VO_Bqg4dC0b6B2wETeBww8p5Vn-MvPxzVfT0AVRKIh5cCPtg9IvD79V5BPiJzfqIw0MkiN4d3_Fs_YX9qFXHmR7QwgNBnZ26iyPyjo8NVAqKT7aJkYTzJ3xOanz_sGcYQNEfV6Ey-bJzkDBQ0mpEFvHT5Dx-Pk5BZ3og-FLotzK9hpjRkLQ9x_x-dvrddlR4D9XD4HGZYTxebypUvsa4D5DTVH0yBf5Ta9eUMGFnUQIWx5NUeBnAkn03xGYd2cvSID2NtmzkPzcoZuz-AACtZT-cxz-nWymdMgHSrSEjeZfisfUa7Vml_ffw-j7yPt1BLuXhDAoQ-1CEug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:«من به ۸ جنگ پایان دادم و به پایان دادن یا حل‌وفصل ۲ جنگ دیگه هم نزدیکم.
همه گروگان‌های اسرائیلی، از جمله ۲۸ نفر آخر رو، چه زنده و چه کشته‌شده، برگردوندم.
صدها گروگان از کشورهای مختلف جهان رو آزاد کردم و به خونه‌هاشون برگردوندم.
در ونزوئلا در جنگ پیروز شدم و دیکتاتور خشنی رو که با بی‌رحمی اون کشور رو اداره می‌کرد، دستگیر کردم.
همچنین جلوی جمهوری اسلامی ایران، بزرگ‌ترین حامی دولتی تروریسم در جهان، رو گرفتم تا به سلاح هسته‌ای دست پیدا نکنه؛ و خیلی کارهای دیگه!
با وجود همه این کارها، نه من و نه ایالات متحده آمریکا جایزه صلح نوبل رو نگرفتیم. عجب!»
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/73052" target="_blank">📅 15:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73051">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f583eac4a.mp4?token=jJ2U36hHxM0O7IKoJXD4r9cena-Ku2BZMHvqZziC-qRGaNm_wFTH9gHtHZCXLaftItJE5aMOfba2UkImANsPT7q7SFhVDksVOUZtmr6mPjrzjnFfTN2_TGVJhT3GaVcbUlKEcGP46fiSglv3FFBShsVDHeKjz4EJvXdm9Qu9S853ZBYtMyrnqD1CrcKdYb04r3KckyWW3saC4AnAOSygemSDtuAfBGPZLHw6NdnbQzQqoFbcUNFxUh3SO2dIDUaTqnD1CwfXmJOs7uaBw-sFvoOr_WFzBYAYuNii8xJ-Xq1bg0GL1hJfWAo0J-_75cAk8DXj_YxDNGQZtOmQB5VYrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f583eac4a.mp4?token=jJ2U36hHxM0O7IKoJXD4r9cena-Ku2BZMHvqZziC-qRGaNm_wFTH9gHtHZCXLaftItJE5aMOfba2UkImANsPT7q7SFhVDksVOUZtmr6mPjrzjnFfTN2_TGVJhT3GaVcbUlKEcGP46fiSglv3FFBShsVDHeKjz4EJvXdm9Qu9S853ZBYtMyrnqD1CrcKdYb04r3KckyWW3saC4AnAOSygemSDtuAfBGPZLHw6NdnbQzQqoFbcUNFxUh3SO2dIDUaTqnD1CwfXmJOs7uaBw-sFvoOr_WFzBYAYuNii8xJ-Xq1bg0GL1hJfWAo0J-_75cAk8DXj_YxDNGQZtOmQB5VYrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهرداری خرمشهر دیده یه سرسره تو پارک شکسته، با خودشون گفتن چکارکنیم چکارنکنیم؟؟
که این نیمه شاهکار رو پیاده کردن :
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/73051" target="_blank">📅 15:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73050">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ef585e24.mp4?token=azT5rn-cfLiT7tqPYKSzibF9XWhe6dNy4fHVGJ7SXEsd92vBS5-a-JlqKv_veY7wLzw5Ud4xQYSiiL2aOJOhwwFSjHOISVHcxQRm7WLnS7SjB-9wlW2a4itOTDKqwqSUtSibfHywqOW632pvJLPwdhYMUmkqCuKQZEl6w_uRYQ4y5UYUPBjQ5MbnOMM6H2Frw6QRYb_Inif-yAGIhMlDPb0ZSHRi4spTQxDEK6Q2ZWdl-NBvcR9Fy_NqZAOFNv9T6R3okJQe5-KjXhonmpMmedQtphhO8oYoL81598zOoBWQWT0JjL5bhBIETck7Y6q_X7_2TYgB9wbC3dO0XD7AIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ef585e24.mp4?token=azT5rn-cfLiT7tqPYKSzibF9XWhe6dNy4fHVGJ7SXEsd92vBS5-a-JlqKv_veY7wLzw5Ud4xQYSiiL2aOJOhwwFSjHOISVHcxQRm7WLnS7SjB-9wlW2a4itOTDKqwqSUtSibfHywqOW632pvJLPwdhYMUmkqCuKQZEl6w_uRYQ4y5UYUPBjQ5MbnOMM6H2Frw6QRYb_Inif-yAGIhMlDPb0ZSHRi4spTQxDEK6Q2ZWdl-NBvcR9Fy_NqZAOFNv9T6R3okJQe5-KjXhonmpMmedQtphhO8oYoL81598zOoBWQWT0JjL5bhBIETck7Y6q_X7_2TYgB9wbC3dO0XD7AIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میرسلیم:
نفت ایران مال مردم نیست و متعلق به خدا و پیامبره
مردم  حکومتو انتخاب میکنن فقط و اون حکومته که تصمیم میگیره چطوری نفت استفاده بشه
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/73050" target="_blank">📅 15:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73049">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/520264f117.mp4?token=L-_XpCk9dIzfe_RlLMP52JVSPG_KUWCxSUQq9jw0GmkCJborgFwfUOcuy_uYM6KQOrweQFDz8KG9j9Tc8ihcUKxuj2Rcl2f_ebkRkRy3WEr4Goq15ciV-vZJs2nZIEp7cKjOihHWkT187_9vT-tQjkB6sF-v1l8lNcfieiV9MKLBFtojmC7mHxjkR6AQpRN1fJV56Tr1Md7aGu-CC9CvD-x4vMWd4P0jR6IXD1Iw6V7IbJTASfGpvL5HaPpRWZ85WBKGy3wBCX6-tPi9mFdhqMKxqEEkqeTVO_6-IFcwWWOfaxHS-jnTgdPwu8YUZkcmQ3WC4aLvI-b5DjTipmsTmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/520264f117.mp4?token=L-_XpCk9dIzfe_RlLMP52JVSPG_KUWCxSUQq9jw0GmkCJborgFwfUOcuy_uYM6KQOrweQFDz8KG9j9Tc8ihcUKxuj2Rcl2f_ebkRkRy3WEr4Goq15ciV-vZJs2nZIEp7cKjOihHWkT187_9vT-tQjkB6sF-v1l8lNcfieiV9MKLBFtojmC7mHxjkR6AQpRN1fJV56Tr1Md7aGu-CC9CvD-x4vMWd4P0jR6IXD1Iw6V7IbJTASfGpvL5HaPpRWZ85WBKGy3wBCX6-tPi9mFdhqMKxqEEkqeTVO_6-IFcwWWOfaxHS-jnTgdPwu8YUZkcmQ3WC4aLvI-b5DjTipmsTmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از اجرای امیرمحمد، نوجوون ارومیه‌ای داخل برنامه Kaos Show ترکیه:
+ این برنامه، عقب‌افتاده‌هایی که تو فضای مجازی معروف شدن رو دعوت میکنه تا مردم بهشون بخندن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/73049" target="_blank">📅 14:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73048">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983154ebcc.mp4?token=C4jWZVsS97ZPBaEvEZXyAKtcBe2I5eVbGsFmdxH_Mag-qZz5XRNSc1VWeGMRyRJwG2idGTSE0cdtfe9z0gWfXa-2q7If7X7QPD6P0JX5C19nziZ3P66K3A0NdiFNTJgVQHIJuVPnqHmMlgtY8j7BSoLYozywkkaplQdwibAXK2kHCL_J-WDrAEyGeoacSMrWggLSsbxVAG5cqUgqvAql44YtRFrOntUl4BBvqhv_QPaUdk4l_ikpdCctUi-7WzH_ybGAg0IzCMOY2lVjYXJnte2lXj8NHmccqk4yyUZwZPlioM4oUz6nqOr3V6kc_empT5LICS9MCWUEwZZcyWtr6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983154ebcc.mp4?token=C4jWZVsS97ZPBaEvEZXyAKtcBe2I5eVbGsFmdxH_Mag-qZz5XRNSc1VWeGMRyRJwG2idGTSE0cdtfe9z0gWfXa-2q7If7X7QPD6P0JX5C19nziZ3P66K3A0NdiFNTJgVQHIJuVPnqHmMlgtY8j7BSoLYozywkkaplQdwibAXK2kHCL_J-WDrAEyGeoacSMrWggLSsbxVAG5cqUgqvAql44YtRFrOntUl4BBvqhv_QPaUdk4l_ikpdCctUi-7WzH_ybGAg0IzCMOY2lVjYXJnte2lXj8NHmccqk4yyUZwZPlioM4oUz6nqOr3V6kc_empT5LICS9MCWUEwZZcyWtr6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله، رهبر کتلت شده حزب‌الله لبنان، ۲۷ خرداد ۱۳۸۸:
امروز در ایران چیزی به اسم تمدن پارسی وجود ندارد.
آن‌چه در ایران وجود دارد، دین محمدِ عرب است.
موسس جمهوری اسلامی هم عرب بود و عرب‌زاده. امام خامنه‌ای هم عرب است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/73048" target="_blank">📅 13:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73046">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/97e3d7ab08.mov?token=MqpKLzV03ZtHnKhJXrSzVewj5TsuGe9yIzPP5FqQW5A-sGA9vdPhfQ-D0mqXdH_qR0FKEqKhmjQ44xTy4QMbL0QWQbvAIwhsL1uyp32wu_N9p6DkO0OGk7WTGxgA7SlNeun1ZVDcnTUwy7RxcQkS-x0n9DPIZJBV2d2oR4zuHo6c-6mG96zj8U9sZdmEICchNJDEA7nhb9G9C8FYDnxqy3Kh4nPYDVygi4Ciksi30p7HZxkhZRl8HlC4g6Wjf6ueff4QOSY-H6quhWnHNZvxFNLa5h28Q85VJkTUbkpQmrZjW9OLHxLxuHpZw52VbhNjz1TjNyGvP6iu-rMoo-Pi2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/97e3d7ab08.mov?token=MqpKLzV03ZtHnKhJXrSzVewj5TsuGe9yIzPP5FqQW5A-sGA9vdPhfQ-D0mqXdH_qR0FKEqKhmjQ44xTy4QMbL0QWQbvAIwhsL1uyp32wu_N9p6DkO0OGk7WTGxgA7SlNeun1ZVDcnTUwy7RxcQkS-x0n9DPIZJBV2d2oR4zuHo6c-6mG96zj8U9sZdmEICchNJDEA7nhb9G9C8FYDnxqy3Kh4nPYDVygi4Ciksi30p7HZxkhZRl8HlC4g6Wjf6ueff4QOSY-H6quhWnHNZvxFNLa5h28Q85VJkTUbkpQmrZjW9OLHxLxuHpZw52VbhNjz1TjNyGvP6iu-rMoo-Pi2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب صدای این انفجارها توی شرق تهران شنیده شد که گویا تست پدافند بوده!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73046" target="_blank">📅 12:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73043">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/351194ef56.mp4?token=J5yudRt1lPN1-VxBLnvWUdhKwTvGMKqkUzmvVIGtNUvc1wL1rwNfi3QIQenGindDnsQ9046Sy9lUjBj8ImsjHnqVX75f4-8YsF5FRPwzk665JTMOGyI0MbtHses3VZX5JIBftdTmzKC-tWAwn2lPtCR-xYdPX3I6BU0Nhh5FIglSSmOPYbmfqQu1gSxy8kbpmcdrV6ekZ1yhUO4bwz4_QgO7xwPo7hXJePOINCI61myQcvGesq70-IplbftGmJ52Qy6ouzf6lHLO6BcbU6gQim-Gj8F5Ccc1x_Pc2eaX2vgQzFzR1M8TWDxtug5keEVYV8n5wVb4_vkOT3OS-4cVUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/351194ef56.mp4?token=J5yudRt1lPN1-VxBLnvWUdhKwTvGMKqkUzmvVIGtNUvc1wL1rwNfi3QIQenGindDnsQ9046Sy9lUjBj8ImsjHnqVX75f4-8YsF5FRPwzk665JTMOGyI0MbtHses3VZX5JIBftdTmzKC-tWAwn2lPtCR-xYdPX3I6BU0Nhh5FIglSSmOPYbmfqQu1gSxy8kbpmcdrV6ekZ1yhUO4bwz4_QgO7xwPo7hXJePOINCI61myQcvGesq70-IplbftGmJ52Qy6ouzf6lHLO6BcbU6gQim-Gj8F5Ccc1x_Pc2eaX2vgQzFzR1M8TWDxtug5keEVYV8n5wVb4_vkOT3OS-4cVUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو و هیچکس بعد از ۱۰ سال قهر و دعوا، دوباره باهم داداشی شدن و دیشب کنار هم روی استیج رفتن!
نکته جالب ماجرا این بود که سروش هیچکس فریاد «جاوید شاه» سر می‌داد و سالن رو به لرزه درآورده بود!
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/73043" target="_blank">📅 12:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73042">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73042" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/73042" target="_blank">📅 12:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73041">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cE-zT-B1M6RiadRq8ZvBSDcnadgHnAYkvz-DqM8wQcPdThpu8kBICDJCYo-nG5q0ZG3ocGuUCaH_CqM0fPU5AQ2ZdkQnKefoZo7oAd5HkegphMh1XNhY5PXjhMMy64SXDMtBkPZxbBUlE_-lFj45DdGjhbrifNf6dvGfFdTPUlLqkEgOKBqmGPJoHgWsCBFlh_hx2pXWvLeIr8lYg24nfRuSMu7imDqE1Cf35C1IK4P25r3dK1LIr6P-Y9iuW2mfY57ymtLgdVVn4gnNOk16fWHEWs87qST_4auBlq2V6WuQ_7zhGu3_MlAYo_eBcYmRCJBXNcuYmFwHT0xWIq2DOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
لیدز
🆚
آرسنال
بورنموث
🆚
چلسی
تاتنهام
🆚
منچستر یونایتد
ختافه
🆚
بارسلونا
ویارئال
🆚
رئال مادرید
بایرن مونیخ
🆚
آگزبورگ
پارما
🆚
اینتر
فروزینونه
🆚
ناپولی
لومان
🆚
پاریسن‌ژرمن
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
https://TrexBet.com</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/73041" target="_blank">📅 12:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73040">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e742ff38d.mp4?token=iqQsHemtU0G9GcpUM7Rvj8urjfqJwOovs2RzWXcOIdSVoMvFTyeNXwQjMTop5FasmTupGKRe20mKQMXsy2mUNCWzhR0FIdnpe4nfDq3WiKi8vCnCmDKo9EKF25hlZny3ElkLeR5_PHabrFWl0ngFBTiq-kFjhgbxHfB3_68uFniitbhSYY9DAYsf9j29qB1a9jSltBvKpfrLjeUjfN1FpsuvB9HxF2ubeO3FqLzahBhdw7aheiE7EgvZUBRqcyEUncYzJrvp5Drfwmfwxyh4EDFRmyyfw5Jivnh2Ua2nWMSOWr1eO8T6hyEWcIduTwvvwJ6lHwXcruraGsBSQ1UQ4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e742ff38d.mp4?token=iqQsHemtU0G9GcpUM7Rvj8urjfqJwOovs2RzWXcOIdSVoMvFTyeNXwQjMTop5FasmTupGKRe20mKQMXsy2mUNCWzhR0FIdnpe4nfDq3WiKi8vCnCmDKo9EKF25hlZny3ElkLeR5_PHabrFWl0ngFBTiq-kFjhgbxHfB3_68uFniitbhSYY9DAYsf9j29qB1a9jSltBvKpfrLjeUjfN1FpsuvB9HxF2ubeO3FqLzahBhdw7aheiE7EgvZUBRqcyEUncYzJrvp5Drfwmfwxyh4EDFRmyyfw5Jivnh2Ua2nWMSOWr1eO8T6hyEWcIduTwvvwJ6lHwXcruraGsBSQ1UQ4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میرسلیم:
مرگ مردم در تصادفات رانندگی به علت رانندگی بد آن‌ها است و ارتباطی به کیفیت خودروهای داخلی ندارد.
واردات خودرو خارجی باعث می‌شود کشور پیشرفت نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/73040" target="_blank">📅 11:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73039">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e55bfab16d.mp4?token=HtXY9v0qsqeQ-fH6XtTsP2lyyy43kzqE3HDcdOp7lG8iRm-zVa5M1Zt2KlHYQssICx1K38cGtD7K3I7rrtx8qvh6Du2oaLg6Ansoc82X2ZZXV5zllauMZPE8LVbaYJAbEkP9Ze1kFLVrafuqYKE5DRSWizAYIjuIALJxuks_4pvJr_hPv0J5WN_ad64Pn_gytbZfS1Iqde3O6aKTi3PqZj-2FJwO1kU7ukE4Qrxv9-nYtf11OmCpzk0gpwXGbMnBmWODKTD_hxIjTUs01Aw9XfIByv3yvCeKNWztZBhdDpgrz4D0XV4oYUzm3Rf1RUsaIW2Iy_6yyEZ2G-PFzGE8fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e55bfab16d.mp4?token=HtXY9v0qsqeQ-fH6XtTsP2lyyy43kzqE3HDcdOp7lG8iRm-zVa5M1Zt2KlHYQssICx1K38cGtD7K3I7rrtx8qvh6Du2oaLg6Ansoc82X2ZZXV5zllauMZPE8LVbaYJAbEkP9Ze1kFLVrafuqYKE5DRSWizAYIjuIALJxuks_4pvJr_hPv0J5WN_ad64Pn_gytbZfS1Iqde3O6aKTi3PqZj-2FJwO1kU7ukE4Qrxv9-nYtf11OmCpzk0gpwXGbMnBmWODKTD_hxIjTUs01Aw9XfIByv3yvCeKNWztZBhdDpgrz4D0XV4oYUzm3Rf1RUsaIW2Iy_6yyEZ2G-PFzGE8fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک تایسون، بوکسور افسانه‌ای:
«اگر رئیس‌جمهوری مثل دونالد ترامپ وجود نداشت، به‌هیچ‌وجه امکان نداشت امروز اینجا باشم. متشکرم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/73039" target="_blank">📅 10:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73038">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d334669b16.mp4?token=fCgO0iY6-CPRZlj3BrXi2GHwpC-MITf9Ooa5QUJcETyJuMgyWF4qH-HRcz-TMuT5myBIYjjw188ZX-oY1QiCMMTARMBztZY1t_b4_l6VHOfGz3yRt6nRdjPlhthsCKHcMhtYcawUW0ZtvFmTbj9cnvwiG85uJhIuR3eyNXjAgOg_rtK8qbQ4aBHSzVOJhGqC6SlJFXZoIYZvEHncvk5oEz-4I9Lubwd2xYBnIJaqfVV79UEts0a9OKTy8o5YeDWm7MIIKB8koz8QJCtR9nrc4r30l-eHUp53ZQdDmu3A_rwKIbehRCXjNf3ftljdESMW0Tu1QX5EqOkA7f6muMjzyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d334669b16.mp4?token=fCgO0iY6-CPRZlj3BrXi2GHwpC-MITf9Ooa5QUJcETyJuMgyWF4qH-HRcz-TMuT5myBIYjjw188ZX-oY1QiCMMTARMBztZY1t_b4_l6VHOfGz3yRt6nRdjPlhthsCKHcMhtYcawUW0ZtvFmTbj9cnvwiG85uJhIuR3eyNXjAgOg_rtK8qbQ4aBHSzVOJhGqC6SlJFXZoIYZvEHncvk5oEz-4I9Lubwd2xYBnIJaqfVV79UEts0a9OKTy8o5YeDWm7MIIKB8koz8QJCtR9nrc4r30l-eHUp53ZQdDmu3A_rwKIbehRCXjNf3ftljdESMW0Tu1QX5EqOkA7f6muMjzyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ پرزیدنت ترامپ:
«ایران یا همه‌چیز رو به ما می‌ده، یا دیگه وجود نخواهد داشت. خودشون اینو می‌دونن.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/73038" target="_blank">📅 10:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73037">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">میرسلیم:
تیبا با خودروهای خارجی ظرفیت رقابت داره
واردات خودرو باید یک در هزار بشه هموناییم که وارد میشن برای این باشه که ببینیم چطوری ساخته شدن
مجری:
الان چرا کشورای حوزه خلیج فارس همه بنز و ماشینای خارجی سوار میشن ولی ما سمند و تیبا و دنا با این قیمتای بالا سوار بشیم...؟
میرسلیم:
میل و انتخاب خودتونه دیگه
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/73037" target="_blank">📅 10:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73036">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سپاه  تصاویری از حملات پهپادهای «شاهد» و موشک‌های کروز به شناورها در تنگه هرمز منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/73036" target="_blank">📅 09:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73034">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ویدئو های وایرال شده از دعوای پشت پارک یه مدرسه دخترونه در تهرانپارس که دو تا اکیپ با دوس پسراشون رفتن داخل پارک بخاطر اینکه یکی از دخترا همزمان با 4 تا دوس پسرِ دوستاش داشته خیانت میکرده به رفیقاش و گرفتن چند نفری زدنش و دوستای دختره هم برای دفاع ازش اومدن!
نکته جالبم اینجاس که چرا دوس پسراشون ایستادن کنار نگاه میکننو نمیرن جلو جداشون کنن و گاهی تشویق هم میکنن که بیشتر بزن هم دیگه رو!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/73034" target="_blank">📅 09:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73033">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/73033" target="_blank">📅 01:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73032">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LKTrCkgIwYNjpPvGasY8yiTDZqV_KKIjhcDE1duYvYenzUZVQj9CVLLNkwW7n3V1_STyCo8mRRdT_CZQHW0YKLgyJRf1Y15TzspnYydvkEsQO9-O8BaapX4q_yU1TMgDPjxQq0BofJtuzVrEDIOAQotI-5-hdqe0qNHZxEsA5bsqJSNfGz4r4u0f4Xs9Icg32zVQQKlVqTOkzKlNiSgFKGBAGXr1RhkU1u6gd0duvrGuL0R423KG7gVXrgobclbwPBlqVrhVeqlJcf33pjG1iJ25BYventfjb4F9rqURgsbM_yGHZ1Sr_guobPHWtX46n0MMTOr0rVlEO4kZx_Tuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/73032" target="_blank">📅 01:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73031">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d4fabef22.mp4?token=s8lQxk6sWQtTKsyhYUvOZCpnP9rZL9Z8gvJ_MbCIg68uBZtUhPNk1NWd4V-RsbY23fv6AZUvEaWtKCnQoh-dPQJBh4W_7jOgE8CzMVA_FaivUCLSCEs1wme1xu2BU7SRP7MkmIrocWgJH56O1MbwOxnGgaO5Do9kx0oJPMt8bdwGNoujkpShnMiuNYWUtIws8NYQK0oOiwm5b6hasGlsqbMCwscFjYXOGFejN3rKLPBEZPFGd5eysfibT3I_rvI9H9TMrtNcLcRB0pPs6SMn1OwNu7TMvQdk-tms8v0oZQbVADZB0l0Oe9thQcsz-qhG1JFLDPZoV7N2_Syw6qOWbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d4fabef22.mp4?token=s8lQxk6sWQtTKsyhYUvOZCpnP9rZL9Z8gvJ_MbCIg68uBZtUhPNk1NWd4V-RsbY23fv6AZUvEaWtKCnQoh-dPQJBh4W_7jOgE8CzMVA_FaivUCLSCEs1wme1xu2BU7SRP7MkmIrocWgJH56O1MbwOxnGgaO5Do9kx0oJPMt8bdwGNoujkpShnMiuNYWUtIws8NYQK0oOiwm5b6hasGlsqbMCwscFjYXOGFejN3rKLPBEZPFGd5eysfibT3I_rvI9H9TMrtNcLcRB0pPs6SMn1OwNu7TMvQdk-tms8v0oZQbVADZB0l0Oe9thQcsz-qhG1JFLDPZoV7N2_Syw6qOWbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/73031" target="_blank">📅 01:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73030">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaABAE5RvGtEa58pSRKNjlxrTl_EILGz8zf_ulc2uqE-7ldKk9pJQL35ihHyqhn-jyS_Kbc86hiOcd0GL2r6mBqNifGDGnW0Qq5nFXgmGGKBBTF_ARc-DRg-aAtZdeKvAS8vOihHPe17p7WlfGnWh22Y9kizCcshlKb6gTartddeb16utBqrbGCruiRZEpWboxgmYM7UxeyFePGpHj9pWvu4aM_NLFWtHr2D654O0ejidbFHyP73gT55sIb2t3ptiU3CtVU2NZ0GXymW3oSXkPqO3_O0d3nABfqMok51FN5vPz6n7_Qb9hsduRajMjHvQe_Wf2Rlx2dikK3zZdk_EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛
هشدار امنیتیِ وزارت امور خارجه آمریکا:
به شهروندان آمریکایی هشدار می‌دیم که فورا ایران رو ترک کنن و به هیچ عنوان به این کشور سفر نکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/73030" target="_blank">📅 01:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73029">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">از سیریک چندین پهباد/موشک به سمت شناورها در تنگه هرمز شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/73029" target="_blank">📅 01:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73028">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0925073180.mp4?token=lsVkIie6v1rSGzwimettdOMcqbvI8ChWbKvMFYo9VeueOETEiXDmdo1aBRNbr192pMJAKXDqPGagXsbnx7A3fxrPVLnUwSxJKefjaF06hkD2jppUYPd04vlcCD-4zXGjTWjMzx5xOR7th-zdLJEak-JPA9UdZFR_yrs4EzItBakwWPhbAr5UEV8dh32gVDt7m-1DOxnk_4nxFYhCUdJH_n4uFIxeyMae5Qz_kkMjK4Y_002-nM7da6KxbTywzdOEOH1MKiKO3xGjl519uEDjSWXcndEQqPmbK-K7MsrN3bZMUPeZhUyBspPoIdHFOtC7UVzXmDyLI8NatbAn1MQS8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0925073180.mp4?token=lsVkIie6v1rSGzwimettdOMcqbvI8ChWbKvMFYo9VeueOETEiXDmdo1aBRNbr192pMJAKXDqPGagXsbnx7A3fxrPVLnUwSxJKefjaF06hkD2jppUYPd04vlcCD-4zXGjTWjMzx5xOR7th-zdLJEak-JPA9UdZFR_yrs4EzItBakwWPhbAr5UEV8dh32gVDt7m-1DOxnk_4nxFYhCUdJH_n4uFIxeyMae5Qz_kkMjK4Y_002-nM7da6KxbTywzdOEOH1MKiKO3xGjl519uEDjSWXcndEQqPmbK-K7MsrN3bZMUPeZhUyBspPoIdHFOtC7UVzXmDyLI8NatbAn1MQS8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: زلنسکی گفته توافق نفتی شما با پوتین نشونه ضعف شماست.
ترامپ: کی اینو گفته؟
خبرنگار: زلنسکی.
ترامپ: باشه!
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/73028" target="_blank">📅 00:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73027">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bebfa1213.mp4?token=Z2XMVlUePfHu6Cexj1SYSXuAa-XVX51fCKhHDQtJy4uubtlSeGKF_7K4haI8TmCmIoa-Cz4ORakzyN5J-MGCYJeoq-hXoLw5Pf3uYSbSiPt-JhP-7Purndlq3M4Dj2KLhycGX8LUbEqWo9EOSia7ibzyscrpWD3ZctAeuP3uboj0M5rSSqrKgP9DZ0KJTIWKky0b8MjEEW08uPdXI0jDp5Xg0srJK8TUM67vBMjcyet4Bd0y5ofbVKl29x8iLQL5KWjbfRTJekca5igOS4T-CELqS4s-ACf5azFOAUabQaNmwH14mog_lso11j2-XS301w2nSWvEWQE-VXV6vvjjQYhRHWHyyMqjI4OQpuZEFa6hOgNOQPrCGcukZ336K-nmQwxC02Ddug9E1PIJvUPGT-pIuVy5VyJG3tD1DBs1rP0X0my0ygrbt5Mif0QSosVYoAGZ6o0N2dH2gYwvs5pjus0r6LJXcjK0iJaG6VwnyVWh2_bTZYTslJjhI79DGWGAHrRpjO-Xoy_lZqdzHLXzT2LkLt-Kpf46gD1W4nn42akfQ2ViYbqmWVekaXwlO_Bnb4TefDhWFgM0msUQCvLV6BMNQFSxGb6Jyqvapvmfu4UzC7q88Py9GIlJEgiqgYJ2J_iTOcEmmeYxOpxDk4rmveCOntXfG9YnBchKyMJ82Wo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bebfa1213.mp4?token=Z2XMVlUePfHu6Cexj1SYSXuAa-XVX51fCKhHDQtJy4uubtlSeGKF_7K4haI8TmCmIoa-Cz4ORakzyN5J-MGCYJeoq-hXoLw5Pf3uYSbSiPt-JhP-7Purndlq3M4Dj2KLhycGX8LUbEqWo9EOSia7ibzyscrpWD3ZctAeuP3uboj0M5rSSqrKgP9DZ0KJTIWKky0b8MjEEW08uPdXI0jDp5Xg0srJK8TUM67vBMjcyet4Bd0y5ofbVKl29x8iLQL5KWjbfRTJekca5igOS4T-CELqS4s-ACf5azFOAUabQaNmwH14mog_lso11j2-XS301w2nSWvEWQE-VXV6vvjjQYhRHWHyyMqjI4OQpuZEFa6hOgNOQPrCGcukZ336K-nmQwxC02Ddug9E1PIJvUPGT-pIuVy5VyJG3tD1DBs1rP0X0my0ygrbt5Mif0QSosVYoAGZ6o0N2dH2gYwvs5pjus0r6LJXcjK0iJaG6VwnyVWh2_bTZYTslJjhI79DGWGAHrRpjO-Xoy_lZqdzHLXzT2LkLt-Kpf46gD1W4nn42akfQ2ViYbqmWVekaXwlO_Bnb4TefDhWFgM0msUQCvLV6BMNQFSxGb6Jyqvapvmfu4UzC7q88Py9GIlJEgiqgYJ2J_iTOcEmmeYxOpxDk4rmveCOntXfG9YnBchKyMJ82Wo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«توافق نفتی با روسیه خیلی مهمه؛ حجم عظیمی نفت وارد کشورمون می‌شه.
راستش رو بخواید، می‌خوام از رئیس‌جمهور پوتین تشکر کنم.
این نفت هم گازوئیله؛ همون چیزی که ما می‌خوایم. پس ازش تشکر می‌کنم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/73027" target="_blank">📅 00:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73026">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffadaf48ae.mp4?token=Vq8JfloKOnxnkx_MP9h3V63QjWOKQiheoYG851d_l7wcZutWatb5BGpLzQFba3BWz4ZYIR7wbXe2j28eGZa40sAU6jNh-CmE7tTwEqb6uuuqkRR-Z1ez2tii62XR56muyvdnCHq3TwubcUjO9Qn3m90X0Di4FwpqGRi_RNehi-lkTLdCNspa-13PEjBBJqJtIycUbV20bwSAJUDXdv-mWwEjApRljxS7x3VXVbWOUmEe5ttvT5ueO3UTGN7geaujqiPVIrYQe4ZhdIn0eMIsjawfPKRLh680i9BBSGZ-xlB_2BpGn7MbRU97C89L5ZJia8ZDFj4kRY13PnB1EULZ7DZePwBmU5E1e3mrTnBDwwIDAgxOx1ooh7bnrUgaIVqeK95LZP_uYllbWxyQe1zczsRzA1zP4oxOOa-JtIEMZxEW1rmM4r5xR-J4lPPdHoYhCngp_J1KFnbgKKAYCYLvU8dlUPE3rMejU8ixB9gOFRDY_5fm7Dp2kFqX9QSV-mDwEn2Et24rEMZyoUU_b8rRLPe2tzV3PK8Ua1C3Zq9QQ2Q5Awn8em0N6MM9PE4-UxYDTSat_G28YwT6nChIdSt4u12fzJBAFvMvq1Qks6_MgZY0fpG_Nzjbo5DEco0STzK101xdUrN0fuz3bC_jNvydJ5hGaYG4tv-Uo1ooKjB_PH4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffadaf48ae.mp4?token=Vq8JfloKOnxnkx_MP9h3V63QjWOKQiheoYG851d_l7wcZutWatb5BGpLzQFba3BWz4ZYIR7wbXe2j28eGZa40sAU6jNh-CmE7tTwEqb6uuuqkRR-Z1ez2tii62XR56muyvdnCHq3TwubcUjO9Qn3m90X0Di4FwpqGRi_RNehi-lkTLdCNspa-13PEjBBJqJtIycUbV20bwSAJUDXdv-mWwEjApRljxS7x3VXVbWOUmEe5ttvT5ueO3UTGN7geaujqiPVIrYQe4ZhdIn0eMIsjawfPKRLh680i9BBSGZ-xlB_2BpGn7MbRU97C89L5ZJia8ZDFj4kRY13PnB1EULZ7DZePwBmU5E1e3mrTnBDwwIDAgxOx1ooh7bnrUgaIVqeK95LZP_uYllbWxyQe1zczsRzA1zP4oxOOa-JtIEMZxEW1rmM4r5xR-J4lPPdHoYhCngp_J1KFnbgKKAYCYLvU8dlUPE3rMejU8ixB9gOFRDY_5fm7Dp2kFqX9QSV-mDwEn2Et24rEMZyoUU_b8rRLPe2tzV3PK8Ua1C3Zq9QQ2Q5Awn8em0N6MM9PE4-UxYDTSat_G28YwT6nChIdSt4u12fzJBAFvMvq1Qks6_MgZY0fpG_Nzjbo5DEco0STzK101xdUrN0fuz3bC_jNvydJ5hGaYG4tv-Uo1ooKjB_PH4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در کنار مایک تایسون در کاخ سفید:
«امروز قرار نیست باهاش مبارزه کنم، اما مدت‌هاست که طرفدارشم. مدت‌هاست با هم دوستیم. هیچ‌کس مثل اون نیست.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/73026" target="_blank">📅 00:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73025">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kugZ_JbYF5hNmu0WjdwlywV0bVTg1FYt_j8yo0x1dM3j-P5k_CMfMMwkMaRDX7E69Ck48eLbFo-IUuBeYnG3LPFCPURvoNthzpNHTYKxsZ--b5KnCuf21FgmVZWvMdONCQCXy-rq57vcngkBa2lAENsiHIuVw8GkwJy5p2J_DSNRtPFZUZCXLtxui7xsFOz895pKnJo6imnM_3wr1NnYHloeXKnNJ0yVzDLHAXbSBk_6uoq2KyiKZ0r0uj6NUIMlRlzmo2mY64FQgFjYKJ_jLmRCnqEOV-ZT7f7akGyU_I_wBwJ9g4btZfF9sw8UO0YRmsi1qgoZavB92hk5h6TRuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛وزارت خزانه‌داری ایالات متحده انجام تراکنش‌های مربوط به فروش، تحویل، تخلیه و واردات سوخت دیزل با منشأ روسیه — از جمله واردات به ایالات متحده — را تا ۷ آوریل ۲۰۲۷ به‌طور موقت مجاز اعلام کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/73025" target="_blank">📅 00:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73024">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6f11119a.mp4?token=U6Em19FiOlLqhylmrUAAj90W3GTXOxfVxcaR1Z0tJOiYNjn5Ne8qJSkFbVmf5dS1rHKjB5upZ9u_4eloleW-_IfjTI76j2MHg8iJUq_n8yivwGYNYyKUXcuStOb0kB71xTrybStmtVGkpfE0cX4J4Igsdds8IEFYVPB5JS7Fe5gXt1pGOkCw432KK3ZLLdd-74HKcwMn0iJ0VE_d5v7nbqGJojSJyP9WXdEp3DA5nvQ_q270NGLzdDYgcpCka10hRWARTY4quzC3MK_-hVppxQvlinmzuuH8EAl-beq2ExIpjZSlUe7ZKxRb06ZJeU91acNE8edZwfNwxoFIDa7-IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6f11119a.mp4?token=U6Em19FiOlLqhylmrUAAj90W3GTXOxfVxcaR1Z0tJOiYNjn5Ne8qJSkFbVmf5dS1rHKjB5upZ9u_4eloleW-_IfjTI76j2MHg8iJUq_n8yivwGYNYyKUXcuStOb0kB71xTrybStmtVGkpfE0cX4J4Igsdds8IEFYVPB5JS7Fe5gXt1pGOkCw432KK3ZLLdd-74HKcwMn0iJ0VE_d5v7nbqGJojSJyP9WXdEp3DA5nvQ_q270NGLzdDYgcpCka10hRWARTY4quzC3MK_-hVppxQvlinmzuuH8EAl-beq2ExIpjZSlUe7ZKxRb06ZJeU91acNE8edZwfNwxoFIDa7-IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سال ۱۹۵۴ بمب‌افکن B-57B Canberra نیروی هوایی آمریکا از آزمایش هسته‌ای Castle Bravo فیلم‌برداری کرد
این انفجار در آب‌سنگ مرجانی بیکینی در اقیانوس آرام با قدرت ۱۵ مگاتن انجام شد، حدود هزار برابر قوی‌تر از بمب اتمی هیروشیما.
قدرت انفجار موجب آلودگی رادیواکتیو گسترده در منطقه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/73024" target="_blank">📅 23:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73023">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9zBK5D-2cCrsWeygeMHe1ediiaRcsfOfs5AGkJGicm01J-hv78D1p96xcrQ8ieJidajZG6-Uqj4xfBOj_Pxqtct62MOMfLDzpW5c5qndGaDcQcPsI7uEebbCVaiFcHoE620zG8-hKX22ZMAnnzFouOi16PxrYDU_ohJEiV6CJjeKsjaQbQjW3wfmqhKts65DukANq9ZAGHHlZxHQefokEtXy-kXIxQ_02Gg-98dwulMsUuMJg0k0l9Ims1lWCk6zglFuqD0TydIh5VmO6idu3lAn08KxMavs2gBUTxZH_9gthIypkWQEdjlsKcb7tvwPigrinafjXTZPOsZK2Y4cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
من به‌تازگی گفتگویی بسیار موفقیت‌آمیز با ولادیمیر پوتین، رئیس‌جمهور روسیه، داشتم که طی آن توافق شد روسیه بلافاصله بیش از ۳۰۰ هزار تن سوخت دیزل برای بازار آمریکا و جهان تأمین کند؛ همچنین ۵۰۰ هزار تن دیگر در ماه نوامبر و یک میلیون تن بلافاصله پس از آن تحویل داده شود.
علاوه بر این، با توجه به وضعیت پالایشگاه‌های دیزل روسیه، این کشور در مدت‌زمانی کوتاه، ۳ میلیون تن دیگر سوخت دیزل تحویل خواهد داد. با در نظر گرفتن «کنترل کامل» ما بر تنگه هرمز و این خبر عالی درباره انرژی روسیه، قیمت دیزل برای آمریکایی‌ها و در واقع برای تمام جهان، با سرعتی بالا و به شکلی بی‌سابقه کاهش خواهد یافت!
کاهش قیمت‌ها برای آمریکایی‌ها، به‌ویژه کشاورزان، دامداران و رانندگان کامیونِ فوق‌العاده ما، بزرگ‌ترین اولویت من است. این خبری بسیار بزرگ و مهم است. همچنین باید دانست که ایران هرگز به سلاح هسته‌ای دست نخواهد یافت! از توجه شما به این موضوع سپاسگزارم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/73023" target="_blank">📅 23:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73022">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5846d15ad4.mp4?token=YzGviTn7ZLIJkO4pC6qGsyRjifrSAQT4-UTrL3vAnBP7E21pWTa-0AlR3ybp1H0V5GacWRicBIU9frTkzrW4AqWm62jRhnL_9yp0oiwjjJrkzjJwEbp5AqjKlxufEdm9q6r0YrCRrISQnzH6A_gf0wgl3dJA29pK0jRxYIbK1wSR4a7Zi2TWLmotXSczoBph_O2gPek1rt9tZf2oPoGIlVrstlrHM6NEC4LnAsMffBRXIDnfqdsx7abMmEpDK-tinLBZEpOiBc5CqfcIccSq2Y6HL6aG9JrUhIvkCaUYHsmm3fwZiK_WO1jFBWB_q4Z5Y1OIngM7jDV61uTvKohQJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5846d15ad4.mp4?token=YzGviTn7ZLIJkO4pC6qGsyRjifrSAQT4-UTrL3vAnBP7E21pWTa-0AlR3ybp1H0V5GacWRicBIU9frTkzrW4AqWm62jRhnL_9yp0oiwjjJrkzjJwEbp5AqjKlxufEdm9q6r0YrCRrISQnzH6A_gf0wgl3dJA29pK0jRxYIbK1wSR4a7Zi2TWLmotXSczoBph_O2gPek1rt9tZf2oPoGIlVrstlrHM6NEC4LnAsMffBRXIDnfqdsx7abMmEpDK-tinLBZEpOiBc5CqfcIccSq2Y6HL6aG9JrUhIvkCaUYHsmm3fwZiK_WO1jFBWB_q4Z5Y1OIngM7jDV61uTvKohQJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیده شدن پلنگ ایرانی در جاده عسلویه:
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/73022" target="_blank">📅 22:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73021">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec656b26d.mp4?token=PhkybsPERBONgDQ-UamUmIlPRAAcAZOdFL3z2yUV-jEiK3iFM5GWwaLYFW3_WTWApp8CdEjKL2a3PSXpQLzoBa-kV9da_o6otWKkV0enPdS4D3d1yjjPSkOf7ndbXuYrnWQqIxQ5MQ44xENZglCdgnE56gevUoDnyUlDTFVgTIDn4A6K_2nx_MDIWw5d4PnsJ8J0AF0XwP5AyUSgJZgtcf7vVgmnsKcp4vdGyYr5_xP9ZBO4gLs2MF27SuhamcF2sg7FxvrFcsmNkgyoXj5_FKL7USBXB7aIaT8dROMe4-S4HLZzAaaK2dEA4mSw7AD2TRZZPYHyR8kf7LosWU8HuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec656b26d.mp4?token=PhkybsPERBONgDQ-UamUmIlPRAAcAZOdFL3z2yUV-jEiK3iFM5GWwaLYFW3_WTWApp8CdEjKL2a3PSXpQLzoBa-kV9da_o6otWKkV0enPdS4D3d1yjjPSkOf7ndbXuYrnWQqIxQ5MQ44xENZglCdgnE56gevUoDnyUlDTFVgTIDn4A6K_2nx_MDIWw5d4PnsJ8J0AF0XwP5AyUSgJZgtcf7vVgmnsKcp4vdGyYr5_xP9ZBO4gLs2MF27SuhamcF2sg7FxvrFcsmNkgyoXj5_FKL7USBXB7aIaT8dROMe4-S4HLZzAaaK2dEA4mSw7AD2TRZZPYHyR8kf7LosWU8HuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه حامی حمید رسایی، سران نظام رو تهدید کرده و این‌بار گفته‌ «کاری نکنید مهرآباد را برایتان ناامن کنیم»
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/73021" target="_blank">📅 22:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73020">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/852188e7d7.mp4?token=QBA78X4S3rabzslAkygJLyeI6EYl3Y40YBHNGOn5pV9YgCfV5XqARRL3CcYHA90FcQ17daCCuQW0hpaRFXYVKz3Yi5QSEJVwb6lWkJ52RnpPe7wfkvnva1uJyrZq8S7GOxWnMe3Qw_TW7RizmOD5RF-5ZU6t_9CnMOWBfz977zxSWmHex_yGcZnf9lY4oePTdCDYtIxMVrK9McRXKVUFL2CLwhvIo-TTvqoG7vUrxAStNJjuWG3KXfhk7FlZ3bDQLW1H13OTvuS3eT9xJdbZ-3lI_cPlB65rS0u9rHbD6IM0l5gplT45vGoiymGERE_r1zOcK9ROh0LDLXcM5WQ30w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/852188e7d7.mp4?token=QBA78X4S3rabzslAkygJLyeI6EYl3Y40YBHNGOn5pV9YgCfV5XqARRL3CcYHA90FcQ17daCCuQW0hpaRFXYVKz3Yi5QSEJVwb6lWkJ52RnpPe7wfkvnva1uJyrZq8S7GOxWnMe3Qw_TW7RizmOD5RF-5ZU6t_9CnMOWBfz977zxSWmHex_yGcZnf9lY4oePTdCDYtIxMVrK9McRXKVUFL2CLwhvIo-TTvqoG7vUrxAStNJjuWG3KXfhk7FlZ3bDQLW1H13OTvuS3eT9xJdbZ-3lI_cPlB65rS0u9rHbD6IM0l5gplT45vGoiymGERE_r1zOcK9ROh0LDLXcM5WQ30w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناوگروه آماده آبی‌خاکی «مکین آیلند | Makin Island» نیروی دریایی آمریکا وارد پرل‌هاربر تو هاوایی شده؛
این ناوگروه بعد از یه توقف کوتاه تو هاوایی، مسیرش رو به سمت غرب ادامه میده و راهی خاورمیانه و منطقه تحت فرماندهی سنتکام میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/73020" target="_blank">📅 21:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73019">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فشار اقتصادی آمریکا علیه ایران؛ واشینگتن به‌دنبال قطع مسیرهای تجاری تهران؛
اسکات بسنت، وزیر خزانه‌داری آمریکا، در گفت‌وگو با شبکه نیوزمکس اعلام کرده که دولت ترامپ قصد دارد فشار اقتصادی بر ایران را به سطحی بی‌سابقه برساند. او از تشدید انزوای اقتصادی ایران و ادامه محاصره بنادر این کشور سخن گفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/73019" target="_blank">📅 21:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73018">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55ac3d9705.mp4?token=eFdsfLRrKwpspJxfhetIaXZtS_bTiy6G62oFyIlHAlEleTzbiHEIjy2epNwcXp1_fHKuzeTBikX6d7z2rncjLm1SA1vvQCZ8pr96mcKH1mR93lwIa8vA0S48q3c7_cD2F3tBpAUxRi-8N1wy8itRO0emYIv_QszaeWjN61xaZSOAy44bi3PZlXdaRTuA-SMrUJtEXbP7lWtD6ueeZbOnVMsEHynThJXoc9hTb8ytHZL8EDCKq17n-n2Kiz7Ft8mz5fLRR_oq7W59kZDu3AIwMsuZlam4SoRYhrVjDQPXYrW1snow0oAZe0vygzeFxT2IgsXh0ldrQUk5VJWgA_bt-TMr5TY_xthKEIVYrCkZBkg07CpsZSQa-QHKPdRvIOL9Dm2xVUSZjS5BfLjpfHXvqnBz_RJ8afAc9ExPGsBucw-H4_cf5SAo53f46eK0RkZ79boOXawUV2m0yQ7fpZ4FuqOWgOMkG3yrXxPkuNiATpZ1YjzkpCjzjP-ompmBQ4F6kQ9pwhUvPKtfAobHQLvIVEG7OPDI0RZwFoDZwd9OA_DltWlcNByPTLw84tF0rrRv2lWDgPZbFouRDc0zaq2kZDes7taDxpd4lwdG0Px8vg3NQnQLVtOvJ97xFRN__zR_cQx1RH8H0t0a_M2laCRcKHgisLCH-5GJw-Wf0BqjDvY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55ac3d9705.mp4?token=eFdsfLRrKwpspJxfhetIaXZtS_bTiy6G62oFyIlHAlEleTzbiHEIjy2epNwcXp1_fHKuzeTBikX6d7z2rncjLm1SA1vvQCZ8pr96mcKH1mR93lwIa8vA0S48q3c7_cD2F3tBpAUxRi-8N1wy8itRO0emYIv_QszaeWjN61xaZSOAy44bi3PZlXdaRTuA-SMrUJtEXbP7lWtD6ueeZbOnVMsEHynThJXoc9hTb8ytHZL8EDCKq17n-n2Kiz7Ft8mz5fLRR_oq7W59kZDu3AIwMsuZlam4SoRYhrVjDQPXYrW1snow0oAZe0vygzeFxT2IgsXh0ldrQUk5VJWgA_bt-TMr5TY_xthKEIVYrCkZBkg07CpsZSQa-QHKPdRvIOL9Dm2xVUSZjS5BfLjpfHXvqnBz_RJ8afAc9ExPGsBucw-H4_cf5SAo53f46eK0RkZ79boOXawUV2m0yQ7fpZ4FuqOWgOMkG3yrXxPkuNiATpZ1YjzkpCjzjP-ompmBQ4F6kQ9pwhUvPKtfAobHQLvIVEG7OPDI0RZwFoDZwd9OA_DltWlcNByPTLw84tF0rrRv2lWDgPZbFouRDc0zaq2kZDes7taDxpd4lwdG0Px8vg3NQnQLVtOvJ97xFRN__zR_cQx1RH8H0t0a_M2laCRcKHgisLCH-5GJw-Wf0BqjDvY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افزایش چشمگیر پروازهای ترابری آمریکا در ارتباط با خاورمیانه
طی ۲۴ ساعت گذشته تا همین لحظات، تحرکات گسترده هواپیماهای ترابری آمریکا در ارتباط با خاورمیانه ادامه داشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/73018" target="_blank">📅 20:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73017">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وزیر آموزش‌وپرورش: تعطیلی احتمالی مدارس بر اساس شرایط هر منطقه تعیین می‌شود
.
کاظمی:
در الگوی جدید بازگشایی مدارس، شرایط هر منطقه به‌صورت جداگانه بررسی می‌شود و در مناطقی که خطری دانش‌آموزان و کادر آموزشی را تهدید نمی‌کند، آموزش حضوری در اولویت خواهد بود!
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/73017" target="_blank">📅 20:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73016">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">#فوری
؛نحوه فعالیت مدارس هرمزگان از یکشنبه ۱۹ مهرماه ۱۴۰۵
بر اساس تصمیم جدید:
- شنبه ۱۸ مهر:
همه مقاطع در هرمزگان غیرحضوری.
از یکشنبه ۱۹ مهر به بعد:
قشم، سیریک و جاسک:
- شهرها: ترکیبی از حضوری و غیرحضوری (تعیین‌شده توسط مدیر مدرسه).
- روستاها:
حضوری اقتضایی.
بندرعباس:
- سه روز حضوری و دو روز غیرحضوری در هفته (برنامه توسط مدیر مدرسه اعلام می‌شود).
سایر شهرستان‌ها:
- حضوری.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/73016" target="_blank">📅 19:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73015">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8de0455f4c.mp4?token=JWxDiAJklsDLVv9hZ5P5fyGx0yQknR4LNdwkbXZQbNYVMy3k1sdi4CSg24slDTykYD_Z_ay2YRApYJs6eNcWfOQoAZbscN_64dwe10w3-Gr3e7_BkKFBtf3PgLM5l9YzEJNs1ojP27eydbxNTlLoV3CN7eQ_elyptEzwMB7XeUAlNLy6HRohCgtJZQDz9LyKpBCc2F6F_05ROYTfw3WpqVKpEQ6AuMlopmFkDmAxEuD973tqEFIqzC5VCm6-Y5zaEFREYaUrc0WMoW2NDsmzWFDysy2uqmKHngI1HwLChYzR9d8_u_OnT2JzvfSTPeqYUgm-3iq6e5uyKS1hCgEofIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8de0455f4c.mp4?token=JWxDiAJklsDLVv9hZ5P5fyGx0yQknR4LNdwkbXZQbNYVMy3k1sdi4CSg24slDTykYD_Z_ay2YRApYJs6eNcWfOQoAZbscN_64dwe10w3-Gr3e7_BkKFBtf3PgLM5l9YzEJNs1ojP27eydbxNTlLoV3CN7eQ_elyptEzwMB7XeUAlNLy6HRohCgtJZQDz9LyKpBCc2F6F_05ROYTfw3WpqVKpEQ6AuMlopmFkDmAxEuD973tqEFIqzC5VCm6-Y5zaEFREYaUrc0WMoW2NDsmzWFDysy2uqmKHngI1HwLChYzR9d8_u_OnT2JzvfSTPeqYUgm-3iq6e5uyKS1hCgEofIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد دانشگاه امام صادق:
دیگه هیچی برای دفاع و حمله نداریم هرچی داشتیمو زدن؛جمهوری اسلامی هیچی نداره دیگه برای حاکمیت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/73015" target="_blank">📅 19:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73012">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UqkTA3jIJvYQ_G9hQX4lOkis_4pL4h0ucark8EIvt08Vze2ps88WaxSh_bFh6mutu0k9cayGABsxKHWTeQ6Dszs-YyAqkHOpd3jg9gvVcKRoJ8-hstvOjSXp4mp7jPH_rm-NtdNRo8r8nErt18eKk-aBcRNrD9HyjN6iGHE0c5gw4mvjlCd5lTivsnA5mhismoYeWWQJwc12FaG2wN43NRMc_Jo_xSV4Lb30gVLOlbueBZoBrTE5ptb0nKursKW29_JKkYqASKtz52xGPwAF3rXa0xgSlxmZ7HRIOTOLljfuQQAnYyfeJPUz5bGqUaPZllGRqfxD1FlT0W0oqVKWIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r1gdWag1N-Wm4AmFwn32TV3smVv7cKEUmXCBiKCJg3xsFlhOfBpDSqpMv-mNYcagQRGefFv9lY3eHMuZmdJSiWl2c1k5e9JzZCJMU5Kb9LCEWj80QNU6u0lUILScp4Tddq4ibxxBN9x_5iwr8OqBmAfX2U-x2MM85pv5Nq1woQC3FJv9iQlwx4wJtOUyX4V66Q4J-xhayRMGmvjZE7EoITuK0OXmxjLKqGxKg7ba-Rxdg2leRiYI4f_iC66nXe-ufmkna4wqCL3qCaVIfGY9Pm1pSkwKsT47YKKjc0Apfe7decmKJ8EJhYsWU8bH637NJS2P-ALnfJiM7qs-Khp9-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305d802103.mp4?token=ZVbckp6u9ATms3v1_QMwDNBAUOpElqYoYU6bV-S3slguT-yBsoGsU5Zzk9vn6Gft51IEhIEce64A-2Zgiv1t0mGfbWmk8xzu_n1C2F77ir9_PVt0pk1RGf9Y4zd8AeOWE2A6fo6o5-QkOFouzUdWGupvzV4CY4kLqZtbbarwgKqCDDEAdMUSnvGr7fLnjLhGQZQm5OAlA-bd0A6a3dWZyDDlRFjFhQ7dHLfXbBp1TMKvKPNEiA_njwxsIneT5FSPvoXmp8QBlhsM0cvoVJOE2JQMYwomky8lrkCm6UGt82-Vt1XVqY0catVfyzg4XwfjA1nSvWkH2XfmpWMOzTSBoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305d802103.mp4?token=ZVbckp6u9ATms3v1_QMwDNBAUOpElqYoYU6bV-S3slguT-yBsoGsU5Zzk9vn6Gft51IEhIEce64A-2Zgiv1t0mGfbWmk8xzu_n1C2F77ir9_PVt0pk1RGf9Y4zd8AeOWE2A6fo6o5-QkOFouzUdWGupvzV4CY4kLqZtbbarwgKqCDDEAdMUSnvGr7fLnjLhGQZQm5OAlA-bd0A6a3dWZyDDlRFjFhQ7dHLfXbBp1TMKvKPNEiA_njwxsIneT5FSPvoXmp8QBlhsM0cvoVJOE2JQMYwomky8lrkCm6UGt82-Vt1XVqY0catVfyzg4XwfjA1nSvWkH2XfmpWMOzTSBoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو و تصاویر وایرال شده از آخوندفدا‌ها تو شهرستان بابل:
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/73012" target="_blank">📅 18:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73009">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gP8V8qRFT1ATjJyFUUE-RvYBxn1lPmJ3F2qTPvS7ZMLsJwmuC3papYFr0tpp2PHWQsEUeaBiX_YhtKJrYl5rLbYj_es1RQ9kCjF1US9pzNBzk1n5iPN37s508sh_JSSgU2xavfK37hKN6xokMf3eEG9hzw0l1ThJkp59ADTG8BJf6ftpJSlNT3dO_eWLfE0zslFmZZlGFW48zd04OjegCherU99Enhc0Omy_F3f-iTFqBa7GfllfV4qaYbnByhYpmAKADCwuob7ZLp2ctpXxfbhB4YgGtMYTDkp04DPlW9gDYdR2DDuoKjSbDBk2g35ZRA5Pq2Y4V2L4F0kOjwQy_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jkbUveLgjesoG7UnTTf1pvObq_Wce1wla_YmxbLytqzQQnQ-sf-83Ci3B6wee_gdS9sFjWnIf4MwLed9uP7mzsccA8B_9PVvfJLeqGl8aqmDduCSiD6LaHbGkwcW8Ev8EbwjX08mT-_OTuEmygE3iT0VU2Qyp7VguAkmklaGXGO1-SEtkDU4z8qxoPWqIMPHpfDJk_a0CVJhgEeoPDQ573lHP8OMCQUue2AKhpRHEjXabQDYOij4qReL709t1iA_Eid9xS_-7BXPS2AdTjN9fg_SbMBj4-KEgxapKQU3yC3b9DOfqYqn8sdEZUpYpicfv0GLq8zTPFFfkG5eKt0BxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c93bb666a.mp4?token=qaOjlomSfRVyRChQJx33Z0r2ZfTh2uammKC3YktfuRXXCE37-A5vhXRdTCaHybKMnGger5eueYG0rjO9eTe1fnxAY1WJEyLoLZVyALuv1YrYpPCxSlhwAjygj5OumY8AKQf2ikWCvwGATleJi559RHB-EHW9oeAJbqDZUaR8pn41LtJxH8YIBZ2mCZTOFKxluHDloXSWH549hiSkZ1X1Us0-KieKWwaNaJt5eRmg5uY33WJEZU4ElAWhOHwjzLWVHaRFqXU6UdhwFd4Iyp3AOYJoEhXiIbDtUHiExz0CKocJ5bR6XMah6Ua1T5r8iQZF40lq3JsZp0h1LdF4opys9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c93bb666a.mp4?token=qaOjlomSfRVyRChQJx33Z0r2ZfTh2uammKC3YktfuRXXCE37-A5vhXRdTCaHybKMnGger5eueYG0rjO9eTe1fnxAY1WJEyLoLZVyALuv1YrYpPCxSlhwAjygj5OumY8AKQf2ikWCvwGATleJi559RHB-EHW9oeAJbqDZUaR8pn41LtJxH8YIBZ2mCZTOFKxluHDloXSWH549hiSkZ1X1Us0-KieKWwaNaJt5eRmg5uY33WJEZU4ElAWhOHwjzLWVHaRFqXU6UdhwFd4Iyp3AOYJoEhXiIbDtUHiExz0CKocJ5bR6XMah6Ua1T5r8iQZF40lq3JsZp0h1LdF4opys9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی عربستان به صنعا پایتخت یمن:
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/73009" target="_blank">📅 17:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73008">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrL9N5NGpYAO4zBFoqP2wzVOUnQYobaHFcq5RwR82h2xWut0CL710oFRSndty7pA6OfUkbRlfqppqQetH26TVnGoVHTxIegjOVMMdOMUuZthjfZsLxkBM5jM29JT5Vm-a__1MyvvdMNJ9pLYf5_1IXEX_zeWRzO1EdwEib2F8DS6GSMtdTMpwOUftoQLstHUFt4Et3rnGu4kC_daoSbY7wgBtt4Dr-QW38prlkPhsYTLoHOdmllLCIKyOLINWuqmkrkJQlkyWgE5POcst4jTRx_TchpubW7TTprM5ulm9AtYvBxe04vkMyV54hts1HGI3YdX-TKRztC2z9jdBiikHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران:
از الان به بعد برخورد با شناورهای متخلف محدود به تنگه هرمز نخواهد بود و هر شناوری که از مسیر غیرمجاز تنگه هرمز عبور کنه در سراسر منطقه تحت تعقیب قرار‌می‌گیره و حتما تنبیه می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/73008" target="_blank">📅 17:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73007">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73007" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/73007" target="_blank">📅 17:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73006">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/medjP5Y7GLsPCPUCIODY7c3Qa_Rcnc_Mn8UeErJMuUG5k2IPIhgAsNIRuQ5VRbfnYJzGNE4HkSMiEfQ9vb2U9l6SvZM6ogcV8nGAYj-EJCW8f9j4xKBCBEmq4FKYtDQ8ZYAMUodAniR9f25g3-yGMFysN_j5SY4F9vywDU7Mhjm9r5aEctDGJquYg1mLiUtLfP9JtIJrrVOlnERSrZZRtx196Kihi2Rk9WqGYTJtOo0GZr1XkTENpzbi6E6iOCkSZ57dwRUFmy6uVoZiHxqozAIiSsaurMByMSopXk9BHMd5AvHnhOtHEBN-hF_UKIcs19ddXVZDWzy6VSm0R9UQfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/73006" target="_blank">📅 17:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73005">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0f7d86e64.mp4?token=rQ2oNLCzCqYRO6S7uXjzwcpicICKWZl3lBC7eXyPjV30FOUgVTSXusIUtWClh2wPve7P_H0_IBdyv8jOZx1Oun_FPEI1EdxtP4I9nVOpEKlQDkhhhmLDUjCKxCRb0j7oktf1258LeO_Ki3fPMge_EjoDHDELfRrGAh_OA_AETC0HSmATq-v5Y-uWuYLtAWbVojyvkRc5Nb2tlaTB147ap3aQb1clx3-svgbOm8UyRg1XqFDVLpsDhwnvc9KnAKopVOExyObK2e0_fhIW_XN1aZqIwRViyVRp8qu_Ul_48AKfZsWlJDnAxCQCTnAXRP5IUQ6Nn7-R9bqeiSCMaYym4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0f7d86e64.mp4?token=rQ2oNLCzCqYRO6S7uXjzwcpicICKWZl3lBC7eXyPjV30FOUgVTSXusIUtWClh2wPve7P_H0_IBdyv8jOZx1Oun_FPEI1EdxtP4I9nVOpEKlQDkhhhmLDUjCKxCRb0j7oktf1258LeO_Ki3fPMge_EjoDHDELfRrGAh_OA_AETC0HSmATq-v5Y-uWuYLtAWbVojyvkRc5Nb2tlaTB147ap3aQb1clx3-svgbOm8UyRg1XqFDVLpsDhwnvc9KnAKopVOExyObK2e0_fhIW_XN1aZqIwRViyVRp8qu_Ul_48AKfZsWlJDnAxCQCTnAXRP5IUQ6Nn7-R9bqeiSCMaYym4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از هواداران حکومت : رفتم تو گونی!
رفتیم جلوی مجلس تجمع کردیم پرایوت نامبر بهمون زنگ زدن
با یه شماره به من زنگ زدن از اطلاعات سپاه بهم گفتن بیا اطلاعات باید توضیح بدی
هیچکس با کسایی که هنجار شکنی میکنن و پست های زشت میزارن و کاریکاتور های زشت و زننده میزارن کاری نداره
بعد من که براساس قران عمل کردم ، منو خواستن احضار بشم
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/73005" target="_blank">📅 17:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73003">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86531200e8.mp4?token=tKuwDNxrRMjUVPAL1Zkrpf464vMmn8-eJr3bWHLavntZ6P06VoniK0cUKKQxUL1GfKHxZV0CcaHIQvNotP6x1t97blDGGXNc9TX0LjLzPtGk2gV9viZ7Yoq0yi4wo0iTb9yM1S9AUVGE1jphF4OVp6aFFhpQ3OVW5FOxrckYvCYMENjeou1fUrd-7mp3grJ4A_UaFggKO7ll-1mBm5ySr3awewdNCrtuF83B50qEAFo6M9wi4Wwaj2dTLrEUffqx0ulXeDfK0JGHy0qiXcVZGY0yFThO2CjNY9q39mqnVtxX_rJhjSlDtM9MCVd_hbH8AeevUSXKLU75T8ylNidlTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86531200e8.mp4?token=tKuwDNxrRMjUVPAL1Zkrpf464vMmn8-eJr3bWHLavntZ6P06VoniK0cUKKQxUL1GfKHxZV0CcaHIQvNotP6x1t97blDGGXNc9TX0LjLzPtGk2gV9viZ7Yoq0yi4wo0iTb9yM1S9AUVGE1jphF4OVp6aFFhpQ3OVW5FOxrckYvCYMENjeou1fUrd-7mp3grJ4A_UaFggKO7ll-1mBm5ySr3awewdNCrtuF83B50qEAFo6M9wi4Wwaj2dTLrEUffqx0ulXeDfK0JGHy0qiXcVZGY0yFThO2CjNY9q39mqnVtxX_rJhjSlDtM9MCVd_hbH8AeevUSXKLU75T8ylNidlTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛درگیری مسلحانه در چشم‌زیارت زاهدان؛ اعزام گسترده نیروهای نظامی؛
به گزارش حال‌وش، در پی حمله مسلحانه به یک خودروی حامل نیروهای نظامی در منطقه چشم‌زیارت زاهدان، ده‌ها خودروی نظامی و امنیتی به منطقه اعزام شده‌اند و پرواز یک بالگرد نظامی نیز گزارش شده است.
هم‌زمان، رسانه‌های حکومتی از انفجار بمب کنار جاده‌ای در مسیر یکی از خودروهای انتظامی استان خبر داده‌اند. برخی منابع محلی نیز از کشته‌شدن معاون اجتماعی انتظامی استان در این حادثه خبر داده‌اند؛ با این حال، جزئیات و آمار تلفات هنوز به‌طور مستقل تأیید نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/73003" target="_blank">📅 17:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73002">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6LESVukoKU5DoNJp7RXtSzqGa4m7sM1hj-9ZUXRk3nZVgTO6BiogKTadQzNl76PQmjW573lqjR-kHdSLQvRCd6WPYswCn1h4uSwBmv_8lU3xjAYPIQms5Dzki-fuq4jsTkVvKzswWF2ef2sO2G5vy3hgE39r9iZKF1xt9a4eY_l37QaVFulSjY09ju4XykDkK-VDKmCYy23rr_6FYO3VElhL96Bc0O8ucF2htfCM3Dj4ucd64NhcZFGbe6IiGwdey9FUO6uGyvWp6v2g5ry5RfZNbiofprdY5qgbwsVQOItYESJWQyMXG3-oOBg70hlxum4mLrETmKaIPas8EmI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حال‌وش: کشته‌شدن ۱۲ نیروی نظامی در حملات ۴۸ ساعت گذشته
به گزارش حال‌وش، در حملات مسلحانه اخیر در سیستان‌وبلوچستان، ۱۲ نیروی نظامی کشته شده‌اند. در حمله به دو خودروی نظامی در منطقه کرین‌دوک نیکشهر، محمدرضا اوکاتی کشته و پنج نفر مجروح شدند. همچنین سرگرد مهدی جمشیدی در فاریاب و ستوان‌سوم وحید عنایت و عباس آقایی در محور لخشک زاهدان کشته شدند.
هویت سایر کشته‌شدگان هنوز احراز نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/73002" target="_blank">📅 16:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73001">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/487ed2a10b.mp4?token=SlX-qVihEf23dywmrXQuoS9R0ZQHR1ygeJ1ARyf4gXna9H7nzJtgMk3ncgYRfGMcfLN5GqXDSfprtji7N1xrxFdlG4GiVCRRBCCMGyHeALGOK9KRep3zKU7BvwSCAtX481EkX234YugvF5wAis1xjbAYUnxPNeEzuJ1BrRHpjChJ1BJ4Sj_jExwoAPZarND2A1YFb57hkydr6wLByv6SlV2q1U-E6RQhen-oggudUIILIb22amCPm1QoXTRt9JDwCY1muJSLt-DwyLPTOOJgd_o1x-pW4x4nZsnXprwxDSo0P8nGSvH_vrvPE359nL1NFHZDVTJGLVsZ_oxTl2RmYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/487ed2a10b.mp4?token=SlX-qVihEf23dywmrXQuoS9R0ZQHR1ygeJ1ARyf4gXna9H7nzJtgMk3ncgYRfGMcfLN5GqXDSfprtji7N1xrxFdlG4GiVCRRBCCMGyHeALGOK9KRep3zKU7BvwSCAtX481EkX234YugvF5wAis1xjbAYUnxPNeEzuJ1BrRHpjChJ1BJ4Sj_jExwoAPZarND2A1YFb57hkydr6wLByv6SlV2q1U-E6RQhen-oggudUIILIb22amCPm1QoXTRt9JDwCY1muJSLt-DwyLPTOOJgd_o1x-pW4x4nZsnXprwxDSo0P8nGSvH_vrvPE359nL1NFHZDVTJGLVsZ_oxTl2RmYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف برای نامزدش یه شب رویایی رمانتیک ساخته واسش گل خریده کنارش یه ایفون 18 پرومکس ۲۵۶ گیگ هم بهش هدیه داده، دختره همون لحظه میگه ۲۵۶ گیگ چیه اخه ۱ ترابایت میخواستم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73001" target="_blank">📅 16:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73000">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb6da5f21.mp4?token=Pq6s8V78G5cDv-D7lZJPnXOSuNcPVlLNcjhFSnOj_GgEZObhamF4Sr1TznpM7bAd5pl0Pkj1HgrYIeXtcq1hGjyU6vCmpi0fdxNax1denJ14URvem8-YVLx0HpGV8s3VRn3wItZeDOUWMiQnkhqpWuPCkqFrs_RJ5zwPGoLWrFZDp0UVVXC0ye7ChEn4PyCOtWxqthtXvUU0avvPBU5lCAh_K4IfWBy0_c0MFnPOfPTUB9FzhUFLPYr5aj9IVegTc9cE9g6poGpjmGBWDPweREuadjddvoJQynoertq1KujUgyQZzXeGeTEC8cbsVHyoJzrg6Jrb1Gf6T_uYqyz_CmDT_3vEDMK3JpGV_iF0gKM_cJixRPpTtzbw_SBq2Y5He2d3JWu89AaF_Mx7ooyc3_g4OlMW11fxtmFE7i2_110vAPqoUFUOWGTvmiPZb1EEI32fAu5ogVaca7O1v3E0eTIy0YqUPqoyAiJ-OOZ7Xe0-UdBz1wuPakTjxQHWIgNKEA9McRhlz-Fc-4zAJxnEVE53spY-ULjsZmFM8UC06agc0bnc57EL37Bxbd5WQdSoQYqyKWM-dllNDN_9mOeIUHLSGogKIj_3wpejxPiC6CqM-CaevCTgH8LPcwr9bCX5wbl5PtJLGAnjY_ahJeWfkOaHZ2VzDuFJQQfgYS8r5ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb6da5f21.mp4?token=Pq6s8V78G5cDv-D7lZJPnXOSuNcPVlLNcjhFSnOj_GgEZObhamF4Sr1TznpM7bAd5pl0Pkj1HgrYIeXtcq1hGjyU6vCmpi0fdxNax1denJ14URvem8-YVLx0HpGV8s3VRn3wItZeDOUWMiQnkhqpWuPCkqFrs_RJ5zwPGoLWrFZDp0UVVXC0ye7ChEn4PyCOtWxqthtXvUU0avvPBU5lCAh_K4IfWBy0_c0MFnPOfPTUB9FzhUFLPYr5aj9IVegTc9cE9g6poGpjmGBWDPweREuadjddvoJQynoertq1KujUgyQZzXeGeTEC8cbsVHyoJzrg6Jrb1Gf6T_uYqyz_CmDT_3vEDMK3JpGV_iF0gKM_cJixRPpTtzbw_SBq2Y5He2d3JWu89AaF_Mx7ooyc3_g4OlMW11fxtmFE7i2_110vAPqoUFUOWGTvmiPZb1EEI32fAu5ogVaca7O1v3E0eTIy0YqUPqoyAiJ-OOZ7Xe0-UdBz1wuPakTjxQHWIgNKEA9McRhlz-Fc-4zAJxnEVE53spY-ULjsZmFM8UC06agc0bnc57EL37Bxbd5WQdSoQYqyKWM-dllNDN_9mOeIUHLSGogKIj_3wpejxPiC6CqM-CaevCTgH8LPcwr9bCX5wbl5PtJLGAnjY_ahJeWfkOaHZ2VzDuFJQQfgYS8r5ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های یه جراح و متخصص زنان :
این خانم 16 ساله بعد اولین رابطه‌اش تو شب اول ازدواج (شب زفاف) دچار خونریزی شدید شده ولی چون فکر می‌کرده بخاطر پارگی پرده‌‌شه، نیومده پیش دکتر و الان هموگلوبینش چندین واحد افت کرده!
در واقع شوهرش فکر می‌کرده داره کابینت نصب می‌کنه و بی‌دین زده همزمان پرده، پرینه و فورشت رو باهم پاره کرده.
اصلا پارگی پرده خونریزی زیادی نداره، هرگونه خون‌ریزی بعد رابطه رو لطفا جدی بگیرید...
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73000" target="_blank">📅 16:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72999">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bae6808a3e.mp4?token=cpcMMSV_jLF8U9UjvM8avIXbY9dMBvJZ1cvOJemlUPzyR_qSgr4aWEKoIPVyW1h6ieHxl_MK5ajysskYP-ZeXDaUMbmz4uNWToT9-174eqB88HspBW4vsDMgUjTmbgmuQZFdq0myL8ZMaJKNiFyUohT2p4MU3WY4k60oFgTVU0bq8XfPfGLp9x1Z_y7zUHWLFDDvOK3BWRYACcPHGKIPyw3G6anCVfBYCymV_aaP0eFlbAOu91l8m6Z0WEL4mPqlgF44ws4EYbnUm5pkdgzS5VR-yFhgqv0lf4itf8Y17m-u6tPlp2U8zkOkJpvzJ0JLIIOvsplGiVWB9lfWV33dnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bae6808a3e.mp4?token=cpcMMSV_jLF8U9UjvM8avIXbY9dMBvJZ1cvOJemlUPzyR_qSgr4aWEKoIPVyW1h6ieHxl_MK5ajysskYP-ZeXDaUMbmz4uNWToT9-174eqB88HspBW4vsDMgUjTmbgmuQZFdq0myL8ZMaJKNiFyUohT2p4MU3WY4k60oFgTVU0bq8XfPfGLp9x1Z_y7zUHWLFDDvOK3BWRYACcPHGKIPyw3G6anCVfBYCymV_aaP0eFlbAOu91l8m6Z0WEL4mPqlgF44ws4EYbnUm5pkdgzS5VR-yFhgqv0lf4itf8Y17m-u6tPlp2U8zkOkJpvzJ0JLIIOvsplGiVWB9lfWV33dnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله حدود ۲۰۰ میلیون دلار از ایران گرفته تا بین لبنانی‌هایی که در جنگ امسال با اسرائیل آواره شدن، کمک مالی توزیع کنه!!!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72999" target="_blank">📅 15:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72998">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed5ddc3810.mp4?token=UI-NHbsmK5rX90nE3dqRc6WdRMxGVgBXyHf7SCaMVsm8150A8JbqGR_qpXHohfM4qnL5nV-0ZKdLbuFGpsxzoWJogSBCNnAgf5yp_dJfTOvkBkdYWQDAGW8C1fwZG8ngIzYGcDvBR4XZTeRi7ifDjQ8ay74X2ziUWF7s-7VDZSPh9ns8S7R7b2H1C2WYLcYkIrgE03n47i8wpGIwvvn4jvioDQZUOdwMRGe3jT2Epj2hSo6YRgDSbTdd-Vs6hNFTBhnXDIn_hBe2k_MDnyrG01uBH3SWoes5ttNJyqM8YkTlCT8XxwTpl9GdRa4FjWyx0pdSTrNkKxNtFwvePgBt0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed5ddc3810.mp4?token=UI-NHbsmK5rX90nE3dqRc6WdRMxGVgBXyHf7SCaMVsm8150A8JbqGR_qpXHohfM4qnL5nV-0ZKdLbuFGpsxzoWJogSBCNnAgf5yp_dJfTOvkBkdYWQDAGW8C1fwZG8ngIzYGcDvBR4XZTeRi7ifDjQ8ay74X2ziUWF7s-7VDZSPh9ns8S7R7b2H1C2WYLcYkIrgE03n47i8wpGIwvvn4jvioDQZUOdwMRGe3jT2Epj2hSo6YRgDSbTdd-Vs6hNFTBhnXDIn_hBe2k_MDnyrG01uBH3SWoes5ttNJyqM8YkTlCT8XxwTpl9GdRa4FjWyx0pdSTrNkKxNtFwvePgBt0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه حمله پهپاد هرمس هرون تی پی اسرائیل به نیروهای گردان پدافند لشکر3 حمزه سیدالشهدا سپاه در آذربایجان غربی در جنگ ۴۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72998" target="_blank">📅 15:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72997">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8rPfSGIUAVqU_27s7AHn23FrgReMKvefjjO1mC6wQYtxAtzXrYEpe111GX8MsUfnrcZYEy4CYEc8sqrQBxRFM0tsgsuS3xmYqFSTJ8-AmiDjnJxxbVIPET_sgHA053xgNqXI6EDU1vle50bzUjQ8etouhTOGsC8lP8tFY77yXzBFDsceJdxb59JJmE2LdsAniDbPZdLoPe--851k0Ic14hsUHNfnQntyp7xSR0ukd45VgkRBk9ShtdbZBbISTMVWIpglONIyFkGV_urk-0YubeS-oxWZ3No3dK3b8Uhmj5LgJreEz8K9kyE8L1-4CDJUjLbwn3gSClM1V28qDxatw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار امنیتی جدید سفارت آمریکا در اردن درباره احتمال اختلال در پروازهای منطقه
؛
سفارت آمریکا در اَمان بار دیگر به شهروندان آمریکایی در خاورمیانه هشدار داد و با اشاره به احتمال تشدید تنش‌های منطقه‌ای، درباره لغو پروازها، بسته‌شدن حریم هوایی و اختلال در سفرهای هوایی هشدار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72997" target="_blank">📅 14:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72996">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a562a527a7.mp4?token=TsVctTXq-6Re4eGBX6v_R-eIKWeqfpYW95tb6w2ubKLIGVaP0deFZLcwlaMX3dpirITaQG0GHyS7w4Uem0h49lhV6SFh648GbzWubySe4zkPD_UVAQVsj8nFP0F4WXBGnsRvETT8oDeIiNCwK5yEA6q8Rc0yRwGgkMZmYjRMKhfG-w-xV5bT_LKJcXzlZ4PuJ8Y0NRo40Bl7SFRmHcUHTe-3EGk_RFyZ4byKb1KWy84WDzK5y78fKee0PMwj_r_GmGdGfjSHHqxlQYrEcJjV1xSaoenEN5p-kulJD8J7MbmcEBAXOlT6E_3AeKSgQAbFe8pYJa-bZnMfBzGaTe0_WCvPI_6XWn14X5z6US6c1tI0HlZuZanbYbkdyHHJMZ6F30jGVuDAmKVQkpcc93WUm-od2aonuLE1vXPeq51e74Gu4oVOR9TXgdBrIG5D3cWalEkGU3TPBbLFFgAEogYSTb3tU-wSxcVX2gwNhYjdhiW9LmnXMJZzk3xvhwqmM5s7QhEB5hbgbhNM6h3sW3ZZn6BoQ4sYEgBYioOTnH-4SQ8FXtvjFImZ6ZsDp5c-735rGFkXEJa5AFnln9T63afbomKTqU9hBoFycHkUdiPolCxWrgpn2bruajPUHOBC4JMCMNHuLQhpfeRiGdIj3f9jWQ3SABPFai2wiX8pmjJ9uyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a562a527a7.mp4?token=TsVctTXq-6Re4eGBX6v_R-eIKWeqfpYW95tb6w2ubKLIGVaP0deFZLcwlaMX3dpirITaQG0GHyS7w4Uem0h49lhV6SFh648GbzWubySe4zkPD_UVAQVsj8nFP0F4WXBGnsRvETT8oDeIiNCwK5yEA6q8Rc0yRwGgkMZmYjRMKhfG-w-xV5bT_LKJcXzlZ4PuJ8Y0NRo40Bl7SFRmHcUHTe-3EGk_RFyZ4byKb1KWy84WDzK5y78fKee0PMwj_r_GmGdGfjSHHqxlQYrEcJjV1xSaoenEN5p-kulJD8J7MbmcEBAXOlT6E_3AeKSgQAbFe8pYJa-bZnMfBzGaTe0_WCvPI_6XWn14X5z6US6c1tI0HlZuZanbYbkdyHHJMZ6F30jGVuDAmKVQkpcc93WUm-od2aonuLE1vXPeq51e74Gu4oVOR9TXgdBrIG5D3cWalEkGU3TPBbLFFgAEogYSTb3tU-wSxcVX2gwNhYjdhiW9LmnXMJZzk3xvhwqmM5s7QhEB5hbgbhNM6h3sW3ZZn6BoQ4sYEgBYioOTnH-4SQ8FXtvjFImZ6ZsDp5c-735rGFkXEJa5AFnln9T63afbomKTqU9hBoFycHkUdiPolCxWrgpn2bruajPUHOBC4JMCMNHuLQhpfeRiGdIj3f9jWQ3SABPFai2wiX8pmjJ9uyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرار شده ۱۱۰ هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72996" target="_blank">📅 13:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72994">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pWRvLSCkuDk143Qj7PV71_JXVit-wkdgfpN8uRp0DYV9WyjT8qCmBw3nh-NbOnptc5QxU8L4XEDcvayiASdB3MZAUXFuSQHezL2VMuzn3MJKDm60lmF_clGLCbMoknV85S9oXVyMv9z9jV5AdHb1nnqdOOa3M6gbhFzv0qrZMwmvpGXHkoPPfaKlODSU7UXEhRE8hypoaImLw3LpLzlhCgAca4hmwRgUibvShULtsZ8zkWCQtNhBzSBmf7uZThaOK0qSICHnMwsC6R5s563fIwKBLEX97pbJF5sld5dJ_MHqQG66CO63TzsobNswWvZZjoTegnA2ioVZCGjW_a383g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a9kCgnQPOOoXEmvWd07xOWVQBCmIrGRzDi67K0X8MmNui5ccGw0LSEi85SVb1U9VgQ0MWpVRkkFAr4gXYaBSVHXlS0AP6_-iHzh2SjD4K5WIitgm4R1kRq51VN1zvcRdID5cQxMeDxdIW5LyFhMegftYwUTUU-Z7lwRD7XaEMRusxbv56KZBeJliU_Ce4hvSHzSSHQ4wxNDrdo-dMLo6Cgl7c-8cSFVqiJH0PjDPl9XJMaYes_GUsqUZ2FW9t8C95wzOaPdnpUFg1ooO8hq6WoPmIDm13ASctEyotffw3ywlSk7pcVL_kvFlGLtjLMwMA8yrGE2THl3Vu5vs3YY1Og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ناو هواپیمابر آبراهام لینکلن پس از ۳۲۱ روز به خانه برگشت؛ در حالی که بدنه جزیره فرماندهی اون با نشانه‌های ثبت‌شده از اهداف منهدم‌شده در جنگ با ایران پوشیده شده.
تحلیلگران دست‌کم ۱۰۳ نماد پهپاد و ۳۴ نماد کشتی رو روی سازه بالای عرشه ناو شمردن.
گروه رزمی این ناو در جریان عملیات «خشم حماسی» (Operation Epic Fury) و محاصره بنادر ایران، ۳۶۹۳ سورتی پرواز رزمی انجام داده و ۴۵۰ موشک تاماهاوک شلیک کرده.
این گروه همچنین رکورد ۲۶۴ روز متوالی در دریا، بدون پهلو گرفتن در هیچ بندری رو ثبت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72994" target="_blank">📅 13:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72993">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57fcb1ffcb.mp4?token=pNY4qvxd1RFHDpXyRitdWiDLXxVaQGlO50SFc-rsjWlQRZpcFjVarBPLnE90ip4YywF1jbRofPBUo7C4ehYAjK38Ij3k2ayA5QfQ7rsgZlMePviMyRRTiz9PxNL_5spjCdvS7kSIvbdRMfykP_MkSvJJTfZm-3LOQSeC0rHGvfMmYVL3OOQnYRIx9oYQXjYx4bfGmex7D6kKyvhP7Wxf-hWkjXL1-Tjku0m-rF0rrmD6c_NxKPXpH0wISzcAFuvK6IeQ0jvHyhITjQNPsLGdshChOsM9ofBg_Jx939wxhXb3h9glm54m-WSL2cwF5k-AJktvU1dxSoa8JW582l8cbDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57fcb1ffcb.mp4?token=pNY4qvxd1RFHDpXyRitdWiDLXxVaQGlO50SFc-rsjWlQRZpcFjVarBPLnE90ip4YywF1jbRofPBUo7C4ehYAjK38Ij3k2ayA5QfQ7rsgZlMePviMyRRTiz9PxNL_5spjCdvS7kSIvbdRMfykP_MkSvJJTfZm-3LOQSeC0rHGvfMmYVL3OOQnYRIx9oYQXjYx4bfGmex7D6kKyvhP7Wxf-hWkjXL1-Tjku0m-rF0rrmD6c_NxKPXpH0wISzcAFuvK6IeQ0jvHyhITjQNPsLGdshChOsM9ofBg_Jx939wxhXb3h9glm54m-WSL2cwF5k-AJktvU1dxSoa8JW582l8cbDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اسلامی، رئیس سازمان انرژی اتمی ایران:
ایران هرگز از حق غنی‌سازی اورانیوم خود صرف‌نظر نخواهد کرد و ذخایر اورانیوم خود را نیز تحویل نخواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72993" target="_blank">📅 12:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72992">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a317d9a3a1.mp4?token=G-DJiuEvexDV6il6a3at9wp2XrC5fnyTNs1bVL56QjOkfwFyfoRsjiIWKHH10SFbOoAqPH_4ElEMV5cvffKYtRcQ4fVwgZR2a35flBVYiFJNSSf-pJ8Fp1WvGV1lZ0625YDVqxuP9zFAnxzFYVjMVDgVXghD1VnWmqcOkdJ5HzMSwm2Ia8AIJLvfMBEmm-7Fc3jLgF5_Uwwn7bs31fMYiBYJ9hGTXKB8y8YXnvys4qLeBxbqO4rMPPThUd9LYTZeTnf55hRqCJHY-m59chnvpTWtcjCBHaes17e-RQOpNQHTzSXbJLSr4dig9Xg0zAIvAQSntkKduDzAqZcS26hFXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a317d9a3a1.mp4?token=G-DJiuEvexDV6il6a3at9wp2XrC5fnyTNs1bVL56QjOkfwFyfoRsjiIWKHH10SFbOoAqPH_4ElEMV5cvffKYtRcQ4fVwgZR2a35flBVYiFJNSSf-pJ8Fp1WvGV1lZ0625YDVqxuP9zFAnxzFYVjMVDgVXghD1VnWmqcOkdJ5HzMSwm2Ia8AIJLvfMBEmm-7Fc3jLgF5_Uwwn7bs31fMYiBYJ9hGTXKB8y8YXnvys4qLeBxbqO4rMPPThUd9LYTZeTnf55hRqCJHY-m59chnvpTWtcjCBHaes17e-RQOpNQHTzSXbJLSr4dig9Xg0zAIvAQSntkKduDzAqZcS26hFXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه پاسداران در حال آزمایش مین‌های جهنده با انفجار هوایی است؛ مین‌هایی که برای پرتاب شدن به هوا و انفجار در ارتفاع طراحی شدن.
هدف از توسعه این فناوری، جلوگیری از عملیات هلیکوپترها و سایر هواگردهای کم‌ارتفاع برای پیاده کردن نیروهاست.
@News_Hut
| C14 News</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72992" target="_blank">📅 12:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72991">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=TiwPXS8mb5JU7WVP1SPsYDcpRTrQr6phj8tQpYgmFYornXjTFAKjbc5bMwkce_4jLeN3sHogHNGk9SCh0_3AcjoqC1I-3yAUby6fhte6x5EQPuBUf-cpcQ-0H7bVN6h0zMNxGvJiaucqm3qM2KXTWU6YdokLQmmAIqaKDetbANhYaYbV1UxWeQ1P_l6_TzD_RvDeNSnRUBuKudFgVUKTTKvGzkXul2q8LFeokiKqsNohHqhv3ziZef2Rykwp4i6e4lMa6_ynpgSv4eyJYJQx4YWiaelTODMtj7sUpWYjylO4cksWFPV3-5hj19lYQ2_dGaMFBM7AzfMph_6fLaCFEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=TiwPXS8mb5JU7WVP1SPsYDcpRTrQr6phj8tQpYgmFYornXjTFAKjbc5bMwkce_4jLeN3sHogHNGk9SCh0_3AcjoqC1I-3yAUby6fhte6x5EQPuBUf-cpcQ-0H7bVN6h0zMNxGvJiaucqm3qM2KXTWU6YdokLQmmAIqaKDetbANhYaYbV1UxWeQ1P_l6_TzD_RvDeNSnRUBuKudFgVUKTTKvGzkXul2q8LFeokiKqsNohHqhv3ziZef2Rykwp4i6e4lMa6_ynpgSv4eyJYJQx4YWiaelTODMtj7sUpWYjylO4cksWFPV3-5hj19lYQ2_dGaMFBM7AzfMph_6fLaCFEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی وایرال شده از سروش هیچکس، رضا‌ پیشرو و حسین تهی از قدیمی های رپ‌فارس در لندن:
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72991" target="_blank">📅 11:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72987">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/chwcQuf3_zRDFwQTRZogyZae2VR5-CaGtZXbeFnu_-nccW6WNuG6Q_MMCoM7v64wZhaq3rHpBaZ1HeZRzpKv0qoEES7jp0cY0tr6-U6aqI5O3e6kZdT-SE0IuRm596Iu7CYk8IsizgL08l_FzyuOKvnic_o4NI5MWBogBioGquDu_RMVnUE_GX8BoM3X5W8IQFBT57RP3oCJ0sr3RYtumkDu5Pu8n8Vn5J79jIz7sxpgYYnXS5iXBeH1J0nYMUCOeGiVnDmfHPa5AtfbjOnVXZYKRyFS90k9_j4syI1zG-icIsdv5phvshP3BaPUkuyiMoCkZnX8BZ37qQat7cjMeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vm6PY6EY-b1aBEcVx6C7UNmSLHcP4eXj5xTnsG1VaknWlmzLLkF7y6aQh_sToRhROJCXjYm1N_abM2HBOQtDQfvl7tFDKNY_XfU1LtCFFvesVYzm6zz4Iymcb-L_iVZQqpmqBCXUy2AnJU7rsO7CVjjYmJtlJeVjQ7IvoNcFuVEY0CJ2aGhJ2r1PyZ1aWleuc-uiU7dzvCKOiG7jfMMJERozqD6S669uk8o4ui5CSEncwL3Eq7h6HA-BLE5JjzKhi4Xlq5nKDW9Vd1S8bt1Ixz2BRAVLwSUB8-RveeUEbygDMn30o2a3oWs9ATA4w6cH3R8cMFXIXYznQbzdRsDVFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KjF-kV6l9TQpKTZArCNAMfffg35N8oq8PDBXXtTYzZe3fxs7o0i7pkRNu39ysUzegCpaDTpHdDhjBF4gWtJn2qZQrQDR95m3EElGKB-KQo-e9qNLtRKQDJVfbQNM_CUteE7efpEw-SuL08GbQwjynD3FsSZkaUvW__IFITc_J1QMHNypvLCrF7AYUm0O4IBcpFUMgh9TdK8CljIOFmqcuIBkdZdvuw-gnr2_W9lfwPb9xqgrTIndWMADfMhJz-ALbmRIfxiY7dZ6adFbmuf_oV9UBL8p_e1E3l6As1Nm0AvE11pfUqqSu3br0Xp4BKwLWJuj_7ajXISPEjUxt4h3KA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78275c1097.mp4?token=eLApDy0ghahRCPIJEV0Drr2yyeK8ACcmhosiRajTzytUmHift_m-yMVeG6TwqHulC1KUPDQvDJNliIbeMSPSYF3QhOQ4itTpR3avEg_zaSU1zGWswexLbS_lmllgcn861jeIUay0eBURdpMHUxo5yQYumU9MsCxeehig4jex9PBIqMIFQ8fk9t0MTZTMO1-iyhwomfvN_mvtd9CgVLZYUjXfHRITF-ZKgztE2wHT63c83wpWaXVaLB7McL8nFGOI6l7C8KZQVMZND5SPkBLqxbPGCAEj6-OLoKTN-QAhCMQkD2wJ0MuN3PJn_EiYfjHBZ_j2yHQGVThT6SVU7O-nTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78275c1097.mp4?token=eLApDy0ghahRCPIJEV0Drr2yyeK8ACcmhosiRajTzytUmHift_m-yMVeG6TwqHulC1KUPDQvDJNliIbeMSPSYF3QhOQ4itTpR3avEg_zaSU1zGWswexLbS_lmllgcn861jeIUay0eBURdpMHUxo5yQYumU9MsCxeehig4jex9PBIqMIFQ8fk9t0MTZTMO1-iyhwomfvN_mvtd9CgVLZYUjXfHRITF-ZKgztE2wHT63c83wpWaXVaLB7McL8nFGOI6l7C8KZQVMZND5SPkBLqxbPGCAEj6-OLoKTN-QAhCMQkD2wJ0MuN3PJn_EiYfjHBZ_j2yHQGVThT6SVU7O-nTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو اعتراضات فرانسه از یه نیروی پلیس که خیلی شبیه امباپه‌ست فیلم گرفتن که خیلی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72987" target="_blank">📅 11:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72986">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72986" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72986" target="_blank">📅 11:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72985">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5ynvfg-iJtz498w3rxk-7yySwEu0VTP8oCJ816FgYOQpRB4ZPHUSqJwPWgUs8F3DRf_oOZSAqe8SUE_7D4sLvb1FCtOEcYgoyrSzDqyxCd4kyuxTK7WRSuRZA7xPLzNU-3iJQphyOVh6KiEhrjLdCJYMRwEszolmMS76JKiKJf9I9_FvSYeLI2fjfwakU7OYsawbB83ZiKqIYOFQUdkRkU1xz1FS2Mf_bdTCrO92A8AmKUiG3u4mN2r8e5Ar7pz6s4uDkFtQSUK0vfGgf8rK0QgkKYPY0gD0eKH4CjsVf4_A4joN1Tbu1Kkk51hTl2ydUuHBIMuwXBIdn0tBiZM0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
اسپانیول
🆚
مالاگا
وردربرمن
🆚
دورتموند
لیون
🆚
لنس
صنعت نفت
🆚
پرسپولیس
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
https://TrexBet.com</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72985" target="_blank">📅 11:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72984">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4384f768.mp4?token=SanJBXGAGXUsFz7QD2JwiFnPeed08SMiOdTjQBR6DyUX9Mk7EX8nrONRkrL0vGpBfzsE6iQttomjbprnUXjnxvxxfZZ9L0rpayixX4Xo789fqNgYRaL3OyFy7QpVvNbeZBLtVluRkklQajhHEfAOe4RK5Jo_oDlKfiem-sbv0IQkxzHMz9AX7Ze3adun0Ot3YTjUfoDLJSGZ7fF0Q2l_1JO_FyG7qEPv7zMWK0fg0dSFUOUpcB1oCQKuKjFeZfJxtlmuAFuNIp6Os9n46ScgVRNISBqq89RsaF4tieg5BdJ3lNcmnk4QFeBXDbQxPyWvQFXE4R5aIuXP8l2YCAnf0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4384f768.mp4?token=SanJBXGAGXUsFz7QD2JwiFnPeed08SMiOdTjQBR6DyUX9Mk7EX8nrONRkrL0vGpBfzsE6iQttomjbprnUXjnxvxxfZZ9L0rpayixX4Xo789fqNgYRaL3OyFy7QpVvNbeZBLtVluRkklQajhHEfAOe4RK5Jo_oDlKfiem-sbv0IQkxzHMz9AX7Ze3adun0Ot3YTjUfoDLJSGZ7fF0Q2l_1JO_FyG7qEPv7zMWK0fg0dSFUOUpcB1oCQKuKjFeZfJxtlmuAFuNIp6Os9n46ScgVRNISBqq89RsaF4tieg5BdJ3lNcmnk4QFeBXDbQxPyWvQFXE4R5aIuXP8l2YCAnf0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری
:
زنوزی پول‌هاش رو از کجا آورده؟ رانت؟
نادر قاضی‌پور ، نمایند سابق مجلس
:
بشین سرجات مصطفی، حق نداری به شیرمرد آذربایجان توهین کنی.
شما مردم آذربایجان رو نمی‌تونی مسخره کنی، حواست جمع باشه ما ستارخان باقرخان داریم.
الغدیر مال کیه؟ به ترک‌ها توهین کنی من بلند می‌شم میرم.
سپاه، تراکتور رو هدیه داد به زنوزی! من واسطه‌ی این کار شدم.
شما تو روز روشن داری حق ما رو میخوری.
تراکتور پرطرفدارترین تیم جهانه.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72984" target="_blank">📅 11:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72983">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1beb1a36.mp4?token=KNsbE0OisX7CGUJuhs4DZEOYqZ5iUe84VOpyS4DX3oy6iQiVCBSMnbybdK2chWNKIisfT7jfwZ_SX5mzx58dr8UqtiIuwNqHtKtUogbaRn-n5o_FZvW49JIrUVzXV5fbjxlsS0tw_th0kkWRoQ2eGduOVOvJ3F4Pj6ZxR2lbGkrmOIjQ4nia6P6RMyzcSEZShzWKtFMt5eO_quit9Ri2Q2DxizGKJUsWKust_8v-swsmSkmFC5EHIrzk7WI9Z4qMm_RMyNOubTzoj834KQ6SMJ2SVMQ2LC2WYo9JepD7xmNxl7uYI8nZkcgqeZFDOFEXbGrAMqt0Pp-cmOGHvH7KBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1beb1a36.mp4?token=KNsbE0OisX7CGUJuhs4DZEOYqZ5iUe84VOpyS4DX3oy6iQiVCBSMnbybdK2chWNKIisfT7jfwZ_SX5mzx58dr8UqtiIuwNqHtKtUogbaRn-n5o_FZvW49JIrUVzXV5fbjxlsS0tw_th0kkWRoQ2eGduOVOvJ3F4Pj6ZxR2lbGkrmOIjQ4nia6P6RMyzcSEZShzWKtFMt5eO_quit9Ri2Q2DxizGKJUsWKust_8v-swsmSkmFC5EHIrzk7WI9Z4qMm_RMyNOubTzoj834KQ6SMJ2SVMQ2LC2WYo9JepD7xmNxl7uYI8nZkcgqeZFDOFEXbGrAMqt0Pp-cmOGHvH7KBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری: گاو که دلار نمی‌خورد، چرا شیر گران می‌شود؟
مدیرعامل اتحادیه لبنی: اتفاقاً دلار می‌خورد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72983" target="_blank">📅 10:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72982">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afdc8b6d86.mp4?token=JwPJQH2kOnBvpCRfiWwBV3sB-rJcr6l_UYp7a4nSbN5jwg7b_WrHVE55UHiXTxvQhEaaATOO7g6UDZFCfTduqwnpBz4dIMvzlDfqxJKJr-hD2SJ357GkRxD56yS2YXxTkc4ejDr1kkklmcJTfj8jDoZMiqVK5naXdjrnL-wCl9ogYAznU9Nl8YMed3VwB4ISqDWEA2Dre7pO_Vw5TGnMwVQP2uaqMqlWX9mmT1u09H-UvxkymPbQWC4RTlEFe05wKfdhjjnCtfBBUkNUvCGF57JoJRuoG_hNjGiZKZBQNJCjvto4t3h18Bb6GT1juLPaEzO4GmFm1GUaVy6e7YzmCn57lYZ3gXk-kEkOj3ZrBILDhxzTlWvSZYLCZqYRcP8B7GUNM0ImmjNHl-T9Cy1EX4JD75b-SLx7TBs2bdB8y9udkIYynjF818A1f1kb4n37FLKAXmEaDvk2PfC2QGFij56P-qwkm5iFHB0Twhz4U65SxCTZD7g5EsK_bnZI2JdffD0VQ1tzVndC3Giy7oKD6w0SDNgeRpcYDEUVG5ew41pMbZNgCZf5Pe6NggxWZjpMYJk4OI7l06UiZJvEc44Mxb2pU_PhBbmZ0PX6FpdwxB8bYWScsDkBusz-OKx__F-0bqmftbRUq2RRGUKR8QUyvlBjTqjGvRrdVKORo8PQtXM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afdc8b6d86.mp4?token=JwPJQH2kOnBvpCRfiWwBV3sB-rJcr6l_UYp7a4nSbN5jwg7b_WrHVE55UHiXTxvQhEaaATOO7g6UDZFCfTduqwnpBz4dIMvzlDfqxJKJr-hD2SJ357GkRxD56yS2YXxTkc4ejDr1kkklmcJTfj8jDoZMiqVK5naXdjrnL-wCl9ogYAznU9Nl8YMed3VwB4ISqDWEA2Dre7pO_Vw5TGnMwVQP2uaqMqlWX9mmT1u09H-UvxkymPbQWC4RTlEFe05wKfdhjjnCtfBBUkNUvCGF57JoJRuoG_hNjGiZKZBQNJCjvto4t3h18Bb6GT1juLPaEzO4GmFm1GUaVy6e7YzmCn57lYZ3gXk-kEkOj3ZrBILDhxzTlWvSZYLCZqYRcP8B7GUNM0ImmjNHl-T9Cy1EX4JD75b-SLx7TBs2bdB8y9udkIYynjF818A1f1kb4n37FLKAXmEaDvk2PfC2QGFij56P-qwkm5iFHB0Twhz4U65SxCTZD7g5EsK_bnZI2JdffD0VQ1tzVndC3Giy7oKD6w0SDNgeRpcYDEUVG5ew41pMbZNgCZf5Pe6NggxWZjpMYJk4OI7l06UiZJvEc44Mxb2pU_PhBbmZ0PX6FpdwxB8bYWScsDkBusz-OKx__F-0bqmftbRUq2RRGUKR8QUyvlBjTqjGvRrdVKORo8PQtXM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه میخوای بدونی رضاشاه و محمدرضا شاه پهلوی چه کشوری تحویل گرفتن و چه خدمت بزرگی برای این مملکت انجام دادن،
حتما وقت بذار و این کلیپ رو ببین.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72982" target="_blank">📅 10:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72981">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a22f39a3d.mp4?token=VPu_DvlmoBbRQZJXTaDC4JFKdjuW4EItWCsvpTCN_RR5g0Izm5UTMpPduup7YRkODOp0BB_pxip-OrPJYbgeF2G7dvoy91IpEVEJLclrDW4eA344Mb-aMlypwWS7giMLDs9giIsi4gOEwn7uaGTGT1vdfmexkqZ8VubmjjIsKH1SI5PPot0tS1d4Vyr79JTPE0p-R_ddvZW0OaMPy_NLgeL536SNetSQpS_Th2AXRIzf8XpzkpJjb4A-Wc9kjQyT1w_eWpOUJ6HWjH1vMKbySAj60JhW-hZwAgDi0wSIE7bl_TVvK6ZCCpojc3NYxt0kz0d9qcMJ2BC5OJgA6yvRaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a22f39a3d.mp4?token=VPu_DvlmoBbRQZJXTaDC4JFKdjuW4EItWCsvpTCN_RR5g0Izm5UTMpPduup7YRkODOp0BB_pxip-OrPJYbgeF2G7dvoy91IpEVEJLclrDW4eA344Mb-aMlypwWS7giMLDs9giIsi4gOEwn7uaGTGT1vdfmexkqZ8VubmjjIsKH1SI5PPot0tS1d4Vyr79JTPE0p-R_ddvZW0OaMPy_NLgeL536SNetSQpS_Th2AXRIzf8XpzkpJjb4A-Wc9kjQyT1w_eWpOUJ6HWjH1vMKbySAj60JhW-hZwAgDi0wSIE7bl_TVvK6ZCCpojc3NYxt0kz0d9qcMJ2BC5OJgA6yvRaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب تو گیلان، یه نیسان گاوی و موتوری باهم درگیری لفظی پیدا میکنن و بعد اینجوری موتوره چپ و نیسانه راست میکنن :
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72981" target="_blank">📅 09:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72980">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAy_pWhxiaDXTOX2A6wWwMAhnu4h1tz1pPAVsvYr1v_DZgJkKsNSQz7Hsd9x9hB_Nw9g9zasG6lUnYM7zd-S5XTi0-e53mcar51e1wc-PMZpwQ69jZi76OLO5cKN8iHzyKnRD63f8chPM4O6jXsEr5FWqNCMFQlj7d-R2gvMbLDrbD8rRcBm_o0YQWMAMIerv3nq8v_LkeSywIMlzUzxUV5zlXI5Fb_qf8ibSBgQSydDr1Rfixco5aYP-AFrT6HiiMHPN4vHKiZw3zcaXwXweZd_FoiGPXh0XXIq44CYTAPeaqvx3nyh9wdqOI00rX98D1yQv1AmpzY0PcVTuS_k7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌تایمز به نقل از مقام‌های آمریکایی: پنتاگون طرح‌هایی برای احتمال اجرای یک عملیات سه‌روزه با حملات شدید علیه ایران آماده کرده که شامل هدف قرار دادن زرادخانه بازسازی‌شده موشکی و پهپادی ایران، زیرساخت‌های انرژی، مراکز فرماندهی سپاه پاسداران و تأسیسات نظامی می‌شه.
انتظار می‌ره سه ناو هواپیمابر آمریکایی در خاورمیانه مستقر بشن؛ هم‌زمان واشنگتن خودش رو برای احتمال ازسرگیری عملیات نظامی گسترده آماده می‌کنه.
با این حال، ترامپ هنوز تمایلی به ازسرگیری جنگ نداره و در ماه‌های اخیر پنج پیشنهاد برای عملیات گسترده علیه ایران یا حوثی‌ها رو رد کرده. او گفته پیش از انتخابات میان‌دوره‌ای آمریکا، مجوز حمله رو صادر نخواهد کرد.
مشاوران ترامپ درباره حملات احتمالی اختلاف‌نظر دارن؛ برخی تردید دارن که حملات بیشتر بتونه موضع تهران رو تغییر بده، اما برخی دیگه معتقدن یک عملیات محدود می‌تونه فشار بر اقتصاد بحران‌زده ایران رو افزایش بده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72980" target="_blank">📅 09:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72979">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCTz8AwFVQJxiCAfL9PKgvNCZT_Xsj9Je3ng9u4c79N_bI20yZphmY7z5d7JxWF-GqbC4luyd32ouF94s2minF_uan7xEojfKsCYzW_-mfUDDCYhHdILx6sWBuX3Mrw5O0fSXbOdgFV5HTVZsdQLM2pLD0xdalQwUBem6EWC76vlWigZN6n09dwTEFagOESJWTNoXN_iOtl6yhGDDIgDBwedFZ8JLEYtrvvy1GIy_k3ol8MPjXOWBLCDdD6sauaRHwpO3vdJZP2zNqIZMXGosNV_afY8eGcHMmBmlGLPuQMyG2kYIGed4lWtP84U7VBhhsLSIZQ8R8Ny664qeFmh2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
«وزارت خزانه‌داری با قطع منابع مالی، رژیم استبدادی تهران رو از پولی که برای جنگ‌افروزی در منطقه استفاده می‌کنه، محروم می‌کنه و به افشای افرادی که به فروش نفت این رژیم کمک می‌کنن، ادامه می‌دیم.
هیچ‌کس که به ایران برای دور زدن تحریم‌ها کمک کنه، از تمام قدرت و اختیارات وزارت خزانه‌داری آمریکا در امان نخواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72979" target="_blank">📅 07:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72978">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn9jEzAuxqKTywOQMB6VVA6QZT-6ug_4qgJqKwJuawcqZs6mAdVf_SqYLEBlP5AtXoITQm1zFiS9fnDfxOIqdYRRKFOG26_iOesXi_p0Fp_orykr9XYYu79PT6Uy48IJErCea5CmmVtzit4VbV8tzcQLRukPmD2b6zPUnWP1c_vMZTqJ4DV4RhDE5fkuTrxpkomDmyeCEFdzygXVSwtLOsVXHgQzLgAPY6BzTRKkRQGlv8i1i-1d7W_3MnKgjCW6nexlWRCjLmzyqZcI6J5DP_kTLhtMC3bZzcTHg2Yk7HGMt8qzB8-cwrYmgXN9rMkKM5QLVxTYnYBTv7zaa47PwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحریم‌های جدید آمریکا علیه شبکه ناوگان سایه ایران
وزارت خزانه‌داری آمریکا از دور جدید تحریم‌ها علیه شبکه باقی‌مانده ناوگان سایه ایران خبر داد؛ این تحریم‌ها در چارچوب کارزار «عملیات مطرود اقتصادی» (Operation Economic Outcast) اعمال شدن.
در این دور از تحریم‌ها، ۲۲ کشتی، ۲۶ شرکت و ۶ فرد مرتبط با شبکه حمل‌ونقل نفت و محصولات پتروشیمی ایران هدف قرار گرفتن.
این تحریم‌ها اپراتورها و شرکت‌هایی در هند، ترکیه، چین، هنگ‌کنگ، امارات متحده عربی و بریتانیا رو هم شامل می‌شن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72978" target="_blank">📅 07:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72977">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72977" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72977" target="_blank">📅 01:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72976">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/autJEsR00yxyTGZwRvstg9ohV_DbV2IrySp4JlV3M2CT630CfHh-VGSCDeCWcc7EFwQAuL3S0Dx8vw2Ms1-4yCEkt8ZsQNIz_gnWN6EYH6-btrar6q0kLgniqQDJetdGUX32Y_fx3WYtTl-xQJ7aLC-IivrueAFkSljzPd43lay4fUx41Z0rTakX8jwI-J_Y6xJDIAj3_Uqr5xkptC7geu-WENEqcmvGmyT50N2N2fpoMKufQZzP_zCbTH_iv_OSfrY62hD08tcc_onEvPloK5DRSnmZRzqPlks14LgYxI8ZKj5HsP0Yn5TMPhaKvT_L8yzcnYBKNFHECZ5Ei_68lg.jpg" alt="photo" loading="lazy"/></div>
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
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72976" target="_blank">📅 01:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72975">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTPI8FrhOisP-3vNBLLo4aoSsvgjFaiHS1Wgro9xUlEMfmYq8GpcrZLA8vtuYexo1vpwv0ulLAJADtfTihGVXv2VlQFnbRp8bmWm_Hflmb-rsKOiTCutARq9oXzW5FTZ_cSup1zgdxUWbhXVnCbCOJ510-XADzaIOANyLOJXf6a31uqCn_aH-NNhpHzNnKvw6eCb5Oj8tpwHu_i9oa8KeGRGgvzq-ynNOxX1S_Ko-P_TIUhcQIBU31xWNu-NvYRUdEXMWcxyw2e-omHbVhbNzXHxRJFGuiGKvPp9Z1qAVbYP5H4jSm4WQrRCDsgoCeJYFIVCLNHUMMXdoFtjoCqxhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی لشکر ۸۸ زرهی نیروی زمینی ارتش:
روز پنجشنبه ۱۶ مهر، مینی‌بوس حامل کارکنان این لشکر در محدوده نیکشهر، سیستان‌ و بلوچستان، هدف حمله مسلحانه قرار گرفت.
بر اساس اطلاعیه رسمی، در این حمله محمدرضا اوکاتی کشته و سه نفر دیگر مجروح شدند.
حال‌وش از تفلات بیشتر خبر داده اما هنوز تایید رسمی نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72975" target="_blank">📅 01:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72974">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rd4wdvHPnZUXtnualooPRe90qrufBRSlxJdTfeUlw-_Bcl_uRGeLmbm-FRFZ_9ycbd-wMFxVocvl56Zb-8-vTO1fPvF6qz--esHbC3ZmM5Rcr84igER2aJhNDUtrplHMmLkCOBCDChVHC1UlQ8p5NcyD6phhNIvNLdWkYObRpcKImWVfOa3c0nAbWEkuBiLdxgvSdaYjdvIYLwSwbX91OKOEX6bTrfQaAD9-3-XxADetUOAHP9ciMLbj_9q3bObpVm9kDkcjIJ9CtOc9E9xxdD2-JrXrRilouSPGZD_EMwTDtdSKELRNJ9Pf2JRzJv_8zmL_Fna8eT4QD34Occ8Klg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.
ایران سلاح هسته‌ای نخواهد داشت!»</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72974" target="_blank">📅 01:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72972">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f430f2b57.mp4?token=N16OCL0TP-jfBERQMvOqHI0x862sSYryJQrKvGVe57L5tuaN8r8OyVY0IpYFiSvm68WX29ktJH627ffiBFc2x7YClVFX_9AQGy_-304UOUqlQb-HNXFPGFHIOznWyOV__blt_QMCs6Unu5CrF-nKBKHQB_c0d80kyNhId0hFve1cAyQv20xoC-QkZrrsuYvODuKVH8ghpMnYQnCSRxDOoGd873XWZ5-GraNWY2jYhrBIGQPU3RExfsee_ZypdwMOGwi3NdLRCLm_04qgOhG90_nMOVddxoNym_4I6sOImApDcz6MuKzz5I161HU3yZwwmE7rRMQP35B7vk37pE8GTXyt_RQ1pM-VXldgRn-5c10_Bc-AJbFmfMtG41h1zv3TriL4KgxbiwsdNA-l6M-IRb9WAlzbET4XZBw3T8tkeH1scMfOWwp-ZUoA15Bay1e2ArMovMrH6dwsNq0PzOHRu_HoQXiR2Dzaw5eQ66BMGPEJ88iEfXXpKo-3vzVYYM_NpvjL1r82bnHp76tH2hrlUc7hfl0UJTcme8T7gsuvUg1Bdg6kXrgetmJ8blVtcYofWs7OyTLDlOOrwN70DlCDOufdBKw1P9eQ-i1EEFT5aow0gs_C47tHyVqCfgw5WJhQ8qnYcKvHulY1kTM8AqxmrMmCvdlC1RjMmo1qoM8onkE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f430f2b57.mp4?token=N16OCL0TP-jfBERQMvOqHI0x862sSYryJQrKvGVe57L5tuaN8r8OyVY0IpYFiSvm68WX29ktJH627ffiBFc2x7YClVFX_9AQGy_-304UOUqlQb-HNXFPGFHIOznWyOV__blt_QMCs6Unu5CrF-nKBKHQB_c0d80kyNhId0hFve1cAyQv20xoC-QkZrrsuYvODuKVH8ghpMnYQnCSRxDOoGd873XWZ5-GraNWY2jYhrBIGQPU3RExfsee_ZypdwMOGwi3NdLRCLm_04qgOhG90_nMOVddxoNym_4I6sOImApDcz6MuKzz5I161HU3yZwwmE7rRMQP35B7vk37pE8GTXyt_RQ1pM-VXldgRn-5c10_Bc-AJbFmfMtG41h1zv3TriL4KgxbiwsdNA-l6M-IRb9WAlzbET4XZBw3T8tkeH1scMfOWwp-ZUoA15Bay1e2ArMovMrH6dwsNq0PzOHRu_HoQXiR2Dzaw5eQ66BMGPEJ88iEfXXpKo-3vzVYYM_NpvjL1r82bnHp76tH2hrlUc7hfl0UJTcme8T7gsuvUg1Bdg6kXrgetmJ8blVtcYofWs7OyTLDlOOrwN70DlCDOufdBKw1P9eQ-i1EEFT5aow0gs_C47tHyVqCfgw5WJhQ8qnYcKvHulY1kTM8AqxmrMmCvdlC1RjMmo1qoM8onkE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه به مواضع گروه‌های کرد در اقلیم کردستان عراق حملات پهبادی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72972" target="_blank">📅 01:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72971">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نیویورک تایمز: انتظار می‌ره سه ناو هواپیمابر آمریکایی در خاورمیانه مستقر بشن؛ هم‌زمان واشنگتن خودش رو برای احتمال ازسرگیری عملیات‌های نظامی گسترده آماده می‌کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72971" target="_blank">📅 00:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72970">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpNaSQ0OBjN0Uy5KFywXn2AcHxxwo63xsR-R5ujEbTIclZNiXOqQGP_vcUQfiHXVjE_RLW-HYyCDtOP4a1YDVy5AdxR_tVd9hJ9RPib2Iil4qmVniAAdr0-t6QTetF2jkHczsi9tcanFRKhzhbawdZaxJ4RKt3Pi1TD4LV4EBJbowDsoCWKFBl7D1nBDbChdDZCuWP2FvloGG34B3Grw2PfgabTBjJgY84EI3mota0ojC8jpE125vXvHKCRT_HgOuSqx46Jyj8n7eEvAKXaVNZ4b5ICjRCRwJLgjbSkBrxYGxndILnydLdJffxE5uDDfx-oiGsY8UVzD3TtWv67tNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
«رسانه‌های جعلی و دروغ‌پرداز دارن این‌طور القا می‌کنن که من از دشمن دعوت کردم به سن‌دیگو و لس‌آنجلس حمله کنه؛ در حالی که منظور من این بود که افزایش موقت قیمت بنزین، بهای کمیه که باید برای نداشتن سلاح هسته‌ای توسط ایران پرداخت کنیم.
حالا اگه می‌خواید بدونید بهای واقعی و سنگین چیه، تصور کنید اگه ایران به سن‌دیگو و/یا لس‌آنجلس حمله می‌کرد، چه اتفاقی می‌افتاد؟
تمام حرف من فقط مقایسه بین کمی بیشتر پول دادن برای بنزین، آن هم برای مدت کوتاه، با حمله به شهرهای بزرگمون بود.
همه اینو می‌دونستن؛ رسانه‌های جعلی هم می‌دونستن، اما بازم ادامه می‌دن و می‌گن من از دشمن خواستم به دو شهری که دوستشون دارم حمله کنه.
حرف من کاملاً روشنه، اما این آدم‌ها منحرف و فاسدن و فکر می‌کنن می‌تونن مدام به انتشار اخبار جعلی ادامه بدن و از زیرش در برن!»
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72970" target="_blank">📅 00:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72969">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtyTEmMPOdI47_aHk0gRwUi29B7BFtjKKOjjCE8PQ0-O3CnhOYoZICnv7adJRnvTRUgtRs5l_bW5FRJNl7ohI5qGlgFFkWfrsEaRMX78YyrIdfjrloIcDdNopcxGFXohGOLQgwn8juoTA4OeJlmIw-jzHzpo2AfdKbQnUXEmsyldws2O4uj8xpplGPTR6tt1xs0B1kONZ_vs31-Yxm1h7JgJ_3lgixRu3On2aQc8Z7cgR6M072YvYa7XXTg_07pzSHaMuZMSK_2cGQlwNBEF_9u7xVe1BlWm7tSweCJ7FonoOMOerL4pEXp5v_6el61b6BG3BSnCgtj7_sQpmpag8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز 8 October روز جهانی لزبین‌ها بود که به اساتید اهل فن تبریک میگیم
🐸
🐸
🐸
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72969" target="_blank">📅 00:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72968">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1b884ba8.mp4?token=SK__8Gjk3b-vBfi24heP6Q7aHw4NDAku6Zfl_01N6JXalQrwLsHkgNNqHKBJ2exTYpKFbQ1NWzfaulU2hgnFLoFd4sdoJm3ql41Lo3shnRy-bJSKPvyeF3jXCq3tsIKpD-St1Fq9otSGMpatiocCCEYRFl_-xyDskwY7VhnQ0jmpcHiOzV1dosRcFjWXmUCdeIPXeFfZAlBYswopBCh5sdGXDc-sKanyiDtCDPD_NVbLVsqjTsfGO0nVKJ8WmFgLVJ0NK0p7L1upcUinx-GAC0LPDqlPqsqHObbac4qo7qvabzGSTh7VHznvuLlhDHPbZTHJBE0F8TT9WHeUI0tgMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1b884ba8.mp4?token=SK__8Gjk3b-vBfi24heP6Q7aHw4NDAku6Zfl_01N6JXalQrwLsHkgNNqHKBJ2exTYpKFbQ1NWzfaulU2hgnFLoFd4sdoJm3ql41Lo3shnRy-bJSKPvyeF3jXCq3tsIKpD-St1Fq9otSGMpatiocCCEYRFl_-xyDskwY7VhnQ0jmpcHiOzV1dosRcFjWXmUCdeIPXeFfZAlBYswopBCh5sdGXDc-sKanyiDtCDPD_NVbLVsqjTsfGO0nVKJ8WmFgLVJ0NK0p7L1upcUinx-GAC0LPDqlPqsqHObbac4qo7qvabzGSTh7VHznvuLlhDHPbZTHJBE0F8TT9WHeUI0tgMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به تازگی دخترا برای پسر خوشگله زندگیشون این حرکتارو میزنن تا دلشو بدست بیارن:
بخاطرت همه پسرا رو آنفالو میکنم.
ساعت کاریتو هم درک میکنم.
حتی عکس دو نفریمون رو میذارم بک گراندم، کی دلش میاد اذیتت کنه خوشگله؟
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72968" target="_blank">📅 23:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72967">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9487485a01.mp4?token=kYuy2p_teQDBD-CYOgYnd_dCtvrN4m4HQf66TVBy_GJV4kJQZ5ulAPHj2f-ltFd-dpyMh5i6WqbIhHzPfbFuaB4SHdVcrGcadYKKZkbBbssHFkGfAVYEAxA_1Fop9lT5AznlYPtn0I7OuFiUVngGQCIaVatq3Wmx06-aROaouNCJD2eXd81y3v8fyGYYlRJh8QRC8FlsD-IV1z2--s7LyIBKbB0Ai7jHSSCTOb4xv1n3sbSViftY5GPjHKaoD0RS8XlrgjatWNkJ746F7-BCRuyMie6FrL4to9GkmlYGft39nqoIcrzwbNlEboG11aj7xa7C7XPfOsEX8-RyVgKqdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9487485a01.mp4?token=kYuy2p_teQDBD-CYOgYnd_dCtvrN4m4HQf66TVBy_GJV4kJQZ5ulAPHj2f-ltFd-dpyMh5i6WqbIhHzPfbFuaB4SHdVcrGcadYKKZkbBbssHFkGfAVYEAxA_1Fop9lT5AznlYPtn0I7OuFiUVngGQCIaVatq3Wmx06-aROaouNCJD2eXd81y3v8fyGYYlRJh8QRC8FlsD-IV1z2--s7LyIBKbB0Ai7jHSSCTOb4xv1n3sbSViftY5GPjHKaoD0RS8XlrgjatWNkJ746F7-BCRuyMie6FrL4to9GkmlYGft39nqoIcrzwbNlEboG11aj7xa7C7XPfOsEX8-RyVgKqdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مطهرنیا: آمریکا هدفش تغییر رژیم هست اما یواش یواش چون نمیخواد مثل عراق بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72967" target="_blank">📅 22:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72966">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19a7b8871.mp4?token=U-UjAL_vqPqH7HE2fKHmkNgJkihKSA076P_Wu0tbMT0OVrk_nAzv-S1UPkpnKSE_W2PIcP8qjOj3ly-fmtHrnu0PaI4-3c-3bS4LBmBZgdzjcuoqc5QK0qeAj123AwrU2FuXJ5Dvus8zqu7TNatXPpKfJiJpCBg5sWoZ676JpSnfT-5Wm0rjiWm0W8B-ImPuGsf7oboEnScnqxfPdeGu-u-gAl4OmpSUyCOiGTEx6ZsEWkPSzAC8M2L1ciZRN1pXxG26w1OivMRy5mqH-VnyKgbqG0qWncEjv-0KrTDTVTgRPIJxCIKyXvAL6fRoYVR6fxpj-9yDwh4d3HtERsleYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19a7b8871.mp4?token=U-UjAL_vqPqH7HE2fKHmkNgJkihKSA076P_Wu0tbMT0OVrk_nAzv-S1UPkpnKSE_W2PIcP8qjOj3ly-fmtHrnu0PaI4-3c-3bS4LBmBZgdzjcuoqc5QK0qeAj123AwrU2FuXJ5Dvus8zqu7TNatXPpKfJiJpCBg5sWoZ676JpSnfT-5Wm0rjiWm0W8B-ImPuGsf7oboEnScnqxfPdeGu-u-gAl4OmpSUyCOiGTEx6ZsEWkPSzAC8M2L1ciZRN1pXxG26w1OivMRy5mqH-VnyKgbqG0qWncEjv-0KrTDTVTgRPIJxCIKyXvAL6fRoYVR6fxpj-9yDwh4d3HtERsleYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا درباره ایران:
«ترامپ رئیس‌جمهوری نیست که بازی دربیاره. رئیس‌جمهوری نیست که زمان زیادی رو تلف کنه.
ترامپ دنبال صلحه، اما حاضره برای رسیدن به صلح، به شکل واقعی و تاریخی، هر کاری که لازم باشه انجام بده.
ایران با داشتن بمب هسته‌ای، اتفاق بدیه؛ نه فقط برای ما، بلکه برای کل جهان.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72966" target="_blank">📅 22:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72965">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1432e3f5f.mp4?token=tjVLQa4BfUC46Z5RvgrxQxoTqKf26QemkfnzMrLxcwuunzMbZifYyZP4-oax6eE4sNB7Qb_wcXpr5B_d080QNWSTkDDWqXxM8ZYzOSCp9GrGIid8PKX0x4Ws0FRC30bcoffZAdgKL29z5fwZJ7YNyy3ErFOoGEa-IerrdZoW9VZ2GtJYg3fohYHeZIX19__nqAXZHrkjROYkXWhAhhsv2dB-FFFRM_ija89fEHWSWGUECKWI0TeSWwMGmIhpJY_0dFVX5vWb9ZQfLW1iDkIFH67nMVsE0zIUEVzlbYHtPFDiFXXdGPe9HTAgHUU8mzMCatCujw49N46sfE2NjmVtMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1432e3f5f.mp4?token=tjVLQa4BfUC46Z5RvgrxQxoTqKf26QemkfnzMrLxcwuunzMbZifYyZP4-oax6eE4sNB7Qb_wcXpr5B_d080QNWSTkDDWqXxM8ZYzOSCp9GrGIid8PKX0x4Ws0FRC30bcoffZAdgKL29z5fwZJ7YNyy3ErFOoGEa-IerrdZoW9VZ2GtJYg3fohYHeZIX19__nqAXZHrkjROYkXWhAhhsv2dB-FFFRM_ija89fEHWSWGUECKWI0TeSWwMGmIhpJY_0dFVX5vWb9ZQfLW1iDkIFH67nMVsE0zIUEVzlbYHtPFDiFXXdGPe9HTAgHUU8mzMCatCujw49N46sfE2NjmVtMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا درباره ایران:
«ما دنبال ملت‌سازی در ایران نیستیم. نمی‌خوایم تعداد زیادی نیروی زمینی وارد ایران کنیم و کنترل مناطق رو به دست بگیریم.
ما فقط می‌خوایم به اون
رژیم، رژیم اسلام‌گرای دیوانه،
بگیم که شما هیچ‌وقت سلاح هسته‌ای نخواهید داشت.
حالا اینکه این اتفاق از راه آسون بیفته یا راه سخت، انتخاب با ایرانه؛ اما در نهایت این
رئیس‌جمهور ترامپه که تصمیم می‌گیره.
و می‌تونم بهتون تضمین بدم که اگر اون لحظه فرا برسه،
اقدام آمریکا سریع و قاطع خواهد بود.
»
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72965" target="_blank">📅 22:09 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

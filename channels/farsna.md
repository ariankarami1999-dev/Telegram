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
<img src="https://cdn4.telesco.pe/file/m-LA2pxGF-tJhsVWVm5_LwrkgQsLYWftVLy5LYNM7nMwdAMrfP-eWuBa5VUID-F-cNR-wo7yOz1Q_yzcCy2wcp34GL859vS23__Q1gEVdSF8Wkc22GirpHyfuN0cp8Qufp1xrJSvhZkdE_4eANcNKI_FgaB-lCdtXDng8kMNeSH4NK7mxm8ATl8IOjqW3FmXOEKS-g9jl0dxb8iDUilAX-IdjcVVtAudMUSnHaLN0y5MAMwM0aXNGpZui6wOT1A_tLVVHDPzw1u0E7VhJGgOZRtK96Yq6sNZ9wu-G5Im7Df1-XqCx5KGl6fTc3sZ2m-fMnXowRGV4ynoZ98U9tNNgQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-29 20:29:52</div>
<hr>

<div class="tg-post" id="msg-457251">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da04981558.mp4?token=m6ewfcG9mF8gVR5_lUuCKJQ1kvrvCEuGkmQsSa4XsBezYaiGxHM5qf5JXlO8rrtAKKcrfQ3epj36tKQjmpkVW5hO9Lqhbv-2eVaGeiJikic5WYTJfXx_W1FsCdrOBxdNhgkvK81i5hSKMNVokfs3VBhe41quFLsHl8ICtwOA8UtEk1vK7vdpyo9ot4Dp-8AGDQ_wh2TbMKsyEGUimNUBtRmqe9lrmT0eJy1AhCDVGs4hdMax-jnl8l5c6Mf9FZFcJCRxuhCF3b38b8DMXvZYLIBjfLb7RY7KdQxEAItJwhlsyJg0BH0-qFIiMz_mJUely6No9phMsioOmS8zO1zy9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da04981558.mp4?token=m6ewfcG9mF8gVR5_lUuCKJQ1kvrvCEuGkmQsSa4XsBezYaiGxHM5qf5JXlO8rrtAKKcrfQ3epj36tKQjmpkVW5hO9Lqhbv-2eVaGeiJikic5WYTJfXx_W1FsCdrOBxdNhgkvK81i5hSKMNVokfs3VBhe41quFLsHl8ICtwOA8UtEk1vK7vdpyo9ot4Dp-8AGDQ_wh2TbMKsyEGUimNUBtRmqe9lrmT0eJy1AhCDVGs4hdMax-jnl8l5c6Mf9FZFcJCRxuhCF3b38b8DMXvZYLIBjfLb7RY7KdQxEAItJwhlsyJg0BH0-qFIiMz_mJUely6No9phMsioOmS8zO1zy9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطره‌ احساسی دختربچه معروف عکس جشن فرشته‌های بیت رهبری از رهبر شهید در برنامه محفل ستاره‌ها
@Farsna</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/farsna/457251" target="_blank">📅 20:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457250">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7VaZaFgLbf2fE179lRZs26QLMW-dv1-BUhUMarjCSmN6ejpDq4ZsnLjY6O18QkXNxzWppoRTONVOCk8kCckHXrvKiIecI4o1KuOroZA5oo1E54anHddy0Tcz4kQfMm2K8br5B02wtdbwrBXZjbFy2bE6ZH71NCMVzRn0-zZliZG0GojPHyU3-2RVs0oQjbAgS91DrgQwTvd21XULjuiQRctGI2Pk56skoG3aNRrO4N6T-EQjVnTSHrP-HXKiwwRVSFEhyZVaxAkfhZOjMlxypj_906gTeN0vam4i1OrwepEZiYIKUIh1iqgfZXAAccgL8KAJ7BYgJJnmmam6p6bEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درستکار: آمریکا به یک نفر ویزا ندهد، تیم را اعزام نمی‌کنیم
🔹
سرمربی تیم ملی کشتی آزاد: برای حضور تیم ایران در مسابقات امیدهای جهان در لاس‌وگاس، اگر آمریکا حتی به یک کشتی‌گیر ویزا ندهد، تیم را اعزام نمی‌کنیم؛ چون ما یک تیم هستیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/farsna/457250" target="_blank">📅 20:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457249">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e2d1dd4c1.mp4?token=Ds5SzTL6V_d4Gz4Lh2U2KdhMjzzcWs2LTdbt_jgdgvFVLfhJzkr80rTqai81gkaVTnUeaNb9lRZ_noQ7lImOs9o5msBTlMyUpsx9xiUHMWDdzspoiXxVkfs-k4FXODxn3BpDj0bfreOI4XjpdMblsfTUlUsmI7gRNEVOIO3PeXLLD4bsLmIvHEniEjxBosRNYrivjkRVNX8tBcE1Jaj-C4Gs_8nbok8NOk-3ftFJ9mQ6ta78NxZmQIouPcb62782Z99cAE8glFNmRAMbxJsaCn-qWlj04xGeCdw3kwZngy2WE_O9Bw3r7rocVBLjrBsOzUjlolyRoLFgUiYGlRVGFVtrguAR-FWDCGVN5KYlfN91Mr7tresP4zZduZeTykdvUT-i8M7t3nkVpTqTXTvwW_XtCaYQRgeHbV5z6NTm1JIfSd21X8m2fBokKJSIUB4YRgambfbJs0wZaEXdzNCtCSsTHg2O9__7NvLWiFZtGzcE2cCwvK98ki9BqNvzBeBsbtcz81q1KhC2Hn3X7pr3P-OuZgjz0QnHA9_XKlO3PfcxTi5MZPIgrwWrRIgMeGR_eImRi68CWu7RFeAAU7xkdHfG9VEZa0aGVry4UZrfZflgJN-eRt192WuYcIAQFATjJtoz8LiOoKRDhwcg20ZPfJseAEbLT34kEXw-sIl1aeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e2d1dd4c1.mp4?token=Ds5SzTL6V_d4Gz4Lh2U2KdhMjzzcWs2LTdbt_jgdgvFVLfhJzkr80rTqai81gkaVTnUeaNb9lRZ_noQ7lImOs9o5msBTlMyUpsx9xiUHMWDdzspoiXxVkfs-k4FXODxn3BpDj0bfreOI4XjpdMblsfTUlUsmI7gRNEVOIO3PeXLLD4bsLmIvHEniEjxBosRNYrivjkRVNX8tBcE1Jaj-C4Gs_8nbok8NOk-3ftFJ9mQ6ta78NxZmQIouPcb62782Z99cAE8glFNmRAMbxJsaCn-qWlj04xGeCdw3kwZngy2WE_O9Bw3r7rocVBLjrBsOzUjlolyRoLFgUiYGlRVGFVtrguAR-FWDCGVN5KYlfN91Mr7tresP4zZduZeTykdvUT-i8M7t3nkVpTqTXTvwW_XtCaYQRgeHbV5z6NTm1JIfSd21X8m2fBokKJSIUB4YRgambfbJs0wZaEXdzNCtCSsTHg2O9__7NvLWiFZtGzcE2cCwvK98ki9BqNvzBeBsbtcz81q1KhC2Hn3X7pr3P-OuZgjz0QnHA9_XKlO3PfcxTi5MZPIgrwWrRIgMeGR_eImRi68CWu7RFeAAU7xkdHfG9VEZa0aGVry4UZrfZflgJN-eRt192WuYcIAQFATjJtoz8LiOoKRDhwcg20ZPfJseAEbLT34kEXw-sIl1aeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
حضور فرزندان رهبر شهید انقلاب در مراسم بزرگداشت چهلم ایشان  @Farsna</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/farsna/457249" target="_blank">📅 20:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457248">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzpx7xZXnIA5mcLhx4kXCNpnm0W6AuIaSdJYGG01aIWiS3aCNXzuS4lZ44AsyAicXR44oVuORBpOAxWry2XR9UgmguaE-_-4sln-asxDeR8Sn4IbIYRAJbILhcPTdTXaI3x_LJv1ciNwVyLjDkIxkqccbF4hIRfu3MG1M7hSUHtuc7OZaoUnB4EUg73txQgcNPYemGCVESjOtYI70t4AXmFxITUbCUbq9dqn23OFOa-dHUEH_gqh3KdP3FjiYd4z0rcDMQbBs79riB4CHUX7O10DLN7ktC_Lp1Cl3Hq04VvEOycyBVClRyDVyXknIX-WvzMplCZJB7oRkKxdfN-OLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حضور سیدمصطفی خامنه‌ای در مراسم بزرگداشت رهبر شهید   @Farsna</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/farsna/457248" target="_blank">📅 20:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457247">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba2666f082.mp4?token=pdyKxcTTePFVo9kUN1ywrn0d5EVlaK6IteE3OYgZMtgsVuKcotI91N7JexsZWjjhLxN6z9C13TMDfLWgQJsMXcCWTaxSGBp-NBl8KR2Idf7AKisii0mx9oO0bocYOByyqVXRMR91wI9rsY04P8grBVXTUCj2vGHNbL1VzClyHm990t_EqKI_45sXeDaXKr_v6Yz3GaxxdRpw388avanagISdwD1sLO5K0KcxcVx7g3xdbOlJqcq6r6b5VGsLqitYZ_fFsyL69dXqVIejO_5YMR2KN-tV5vh72l6BQNNJy5vmeEJEJtXPDcI_vSOX_BFVg6kIWTAubeE3ZGqKoInm8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba2666f082.mp4?token=pdyKxcTTePFVo9kUN1ywrn0d5EVlaK6IteE3OYgZMtgsVuKcotI91N7JexsZWjjhLxN6z9C13TMDfLWgQJsMXcCWTaxSGBp-NBl8KR2Idf7AKisii0mx9oO0bocYOByyqVXRMR91wI9rsY04P8grBVXTUCj2vGHNbL1VzClyHm990t_EqKI_45sXeDaXKr_v6Yz3GaxxdRpw388avanagISdwD1sLO5K0KcxcVx7g3xdbOlJqcq6r6b5VGsLqitYZ_fFsyL69dXqVIejO_5YMR2KN-tV5vh72l6BQNNJy5vmeEJEJtXPDcI_vSOX_BFVg6kIWTAubeE3ZGqKoInm8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری منتشرنشده از سخنرانی رهبر شهید انقلاب در حرم مطهر امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/farsna/457247" target="_blank">📅 20:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457246">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d1470a7d.mp4?token=uQ0szn_8kQQQRImiVTxxysfjwu0socz4MRL-sXAZG6Y4WTfWAt0NCFxGQe-eMNV8mrHVLkso1xs9UaIOiqkEBaMXEBmkQrY1jFn3_fvVwdzA9luJXP1gUVZzYy4rvqKOtfzGlEyH5KgGjkVVoOgJn2P4hcb-Fc-Dvu3h0nOJfGZFHaDNOmk4DAqfsQ4xPo8WaU6cE4n13F1O_1Tt6hxHn6WVWmVbjhPzK1qz9MlxcRCTNxdPXf2tpOl5rAEpvPkivTbAFmWt5OfmAE0UerDZ7OCr_IM4QZ93-jWgLOfpn6CjxecxJ09S8jrATrtfqU1vsIRfPVPRw4g9PNg2enImxTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d1470a7d.mp4?token=uQ0szn_8kQQQRImiVTxxysfjwu0socz4MRL-sXAZG6Y4WTfWAt0NCFxGQe-eMNV8mrHVLkso1xs9UaIOiqkEBaMXEBmkQrY1jFn3_fvVwdzA9luJXP1gUVZzYy4rvqKOtfzGlEyH5KgGjkVVoOgJn2P4hcb-Fc-Dvu3h0nOJfGZFHaDNOmk4DAqfsQ4xPo8WaU6cE4n13F1O_1Tt6hxHn6WVWmVbjhPzK1qz9MlxcRCTNxdPXf2tpOl5rAEpvPkivTbAFmWt5OfmAE0UerDZ7OCr_IM4QZ93-jWgLOfpn6CjxecxJ09S8jrATrtfqU1vsIRfPVPRw4g9PNg2enImxTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور سیدمصطفی خامنه‌ای در مراسم بزرگداشت رهبر شهید   @Farsna</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/farsna/457246" target="_blank">📅 19:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457245">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8fddb63e3.mp4?token=dxPM14Ace_ZrUNMG2gsJ9JMnM9MP2aeHrtrA1F82Ik1YJiDnfXZ5wcnt5YihPo5vnRcQkQJjBKeeB0Ox024J7nbs-TI7afDXjcO4bU6lpRvhbfgsr5iYwromqozxHLG6hDl1wb_Z6zB8mfWHgGEQrr6zfPhnUEm3eLfJGwFhNfTjU9OlMhRXvfxAymR5HsVGP-lT6uF4p9gEy_-kvpigpIUbPvHfTejjMryc-530Ki7c0pPcxKwNYIWJotScjODGFyIcysM1qC37Zpix-YANQnKJTJDnwwNRIR0kNo-6BdRuhyXMNmKUc9D0nzVbs-3JYVsEh5I5ROh_JU9FtDmtTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8fddb63e3.mp4?token=dxPM14Ace_ZrUNMG2gsJ9JMnM9MP2aeHrtrA1F82Ik1YJiDnfXZ5wcnt5YihPo5vnRcQkQJjBKeeB0Ox024J7nbs-TI7afDXjcO4bU6lpRvhbfgsr5iYwromqozxHLG6hDl1wb_Z6zB8mfWHgGEQrr6zfPhnUEm3eLfJGwFhNfTjU9OlMhRXvfxAymR5HsVGP-lT6uF4p9gEy_-kvpigpIUbPvHfTejjMryc-530Ki7c0pPcxKwNYIWJotScjODGFyIcysM1qC37Zpix-YANQnKJTJDnwwNRIR0kNo-6BdRuhyXMNmKUc9D0nzVbs-3JYVsEh5I5ROh_JU9FtDmtTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصویری از مزار نورانی «آقای شهید ایران» در چهلم تدفین ایشان  @Farsna</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/farsna/457245" target="_blank">📅 19:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457244">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeY-pbYiuWFd6ceMGMxQ7aWmGBkQqf0Tr-FudUjHrVNtXTnxYjikRw4ZoT5QUfljffl94i0Jr6jilhsA3ubapfYpAhn3_LdEUXVK2Q5M_lCisJZ4G3vmSp0PPh4WzZUYrsN2esxVrGHB-cFWNi8YwAwNHqoP3I7JBZz84DwMuzO35O6srnNA3oPRuS4vi6bCwAHRTjC8QjniN_68nYCXCJXqXoSOwNWdhvp1lFmvxJ-opZSKEjy8E9R3NUb95tfeUR3wK6DuikqAPrhZmMwHA0zPi4Hzcey7U7cO_lW2PxnlVWew2qanzu-qoXyGAz2FdwJi9a8bSTN06X8WPNlrPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رطوبت هوای بوشهر به ۱۰۰ درصد رسید
🔹
بنابر اعلام هواشناسی بوشهر دمای هوا در ۴ شهرستان دیّر، تنگستان، دشتستان و دشتی به ۵۰ درجه سانتی‌گراد رسید؛ هم‌زمان رطوبت و شرجی هوا در شهرهای ساحلی این استان تا ۱۰۰ درصد افزایش یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/farsna/457244" target="_blank">📅 19:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457243">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TD9QDWshNz2DMnA3cJPI_749zPUIAnVybNz6mevOpL6wSDiq3ugHS-Pfl8mDlrDGdXL0Jfi1yx9_8rKane98MLavjtHPX2kDD5HAXFkFliIgLnVb6PlOUVeLM63YZ4vbD2bne9_aSP9P4T9JF8-zfj5fNOPJt35uxfKgqb5N-btoyCzfH_mWW5NeZFsBS3Bp7BA3Yzr91SJlJ7Xz7zFbancLUPDHb_Ex50LgM7lw5ruktq_dqlLOhkyc9W-a2PFeg_ZAH54LB2qm4NA41pnJBVV22WaFQ5V6qN9Arqh6zTNs6f8cQrsN9AcwagklZ7PN0fyKU0214rMcUtcJ1nhdkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حال‌وهوای حرم رضوی پیش‌از آغاز مراسم بزرگداشت چهلم تدفین رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/farsna/457243" target="_blank">📅 19:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457242">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۲۳.pdf</div>
  <div class="tg-doc-extra">2.7 MB</div>
</div>
<a href="https://t.me/farsna/457242" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۲۲.pdf</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/farsna/457242" target="_blank">📅 19:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457241">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/470cf5fd23.mp4?token=uBmth7wSvuXp05kSoT16-KbnpsTQMi2_D1SkQCQl5d2w8-5IjGHv7v4f1k0JP7-2Cu8LiD01sjPpuEB_dETTuDfdO4P-WXTxqc2ZIxenRxtKElOOH3GJFAPj8dg2MkgzjQZKUydCPXuUIRyxQnXnx8Ms4fnk8-0ZwiIKLYe12WHOhaVVEw4PIOWq-wZycTzb4fR5obHVu7jiIG0OrOnFHOwUXSRb1L0RdhY_nPvVgluJgZHGJmE011U63UQr3WdsPNFLvoFAcZqOjUX_WHKOjWHsUfw_C6phV1LhvPgcU48wNKA471DmOh5aDlJE28o9lBvJ4Cxh1ccxu8JMRh5xcDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/470cf5fd23.mp4?token=uBmth7wSvuXp05kSoT16-KbnpsTQMi2_D1SkQCQl5d2w8-5IjGHv7v4f1k0JP7-2Cu8LiD01sjPpuEB_dETTuDfdO4P-WXTxqc2ZIxenRxtKElOOH3GJFAPj8dg2MkgzjQZKUydCPXuUIRyxQnXnx8Ms4fnk8-0ZwiIKLYe12WHOhaVVEw4PIOWq-wZycTzb4fR5obHVu7jiIG0OrOnFHOwUXSRb1L0RdhY_nPvVgluJgZHGJmE011U63UQr3WdsPNFLvoFAcZqOjUX_WHKOjWHsUfw_C6phV1LhvPgcU48wNKA471DmOh5aDlJE28o9lBvJ4Cxh1ccxu8JMRh5xcDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای حرم رضوی پیش‌از آغاز مراسم بزرگداشت چهلم تدفین رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/farsna/457241" target="_blank">📅 19:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457240">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ادامهٔ تجاوزات رژیم صهیونیستی به جنوب لبنان
🔹
به‌گزارش الجزیره به نقل از رسانه‌های محلی، اسرائیل منطقه الطیری در شهرستان بنت جبیل لبنان را بمباران کرده است.
🔸
ساعاتی پیش روستای المنصوری در شهرستان صور نیز هدف حملات توپخانه‌ای رژیم صهیونیستی قرار گرفته بود.
@Farsna</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/457240" target="_blank">📅 19:18 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457239">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7846e72a4c.mp4?token=o4ppe74WTVu8sTubd13_ZEvXK4830-RPwK1DcPCDa8-SsjxJITQ7b_Ep7tppKgM--B6O7Ul750m8xGtvOAHiGXdN-8_rI5OcNwG4W5ewj82T_3JP193ZlTXCLyKp1WPWbVkfX5zf3aWEEuLJdYCOvD3JAi8Gcfi3EPA39Q6BZ-j-Yt5DzFyS39ufph4tyWWf-0nnLzTc7L3sX2FMJFUncrKBFo5R0yGfNZWfsiljRwKPj9rRjl5AiqUh-I15K29xD3EMIzjrsTuhsXnlQ6PRp4-wRY8GvVRqV6c6eMCabuowACI5AlVu3x4SrNy0hScfs4i7cfXMoJqvzHS7JoJShTAcSApHtnorGEhJwY8djkuq3nIs2rGV_eKxhAfKqfhWAqgjHH_rOJ-i2w1LD_d1aWfTZIcqQVglME1F6IBMsI_TZ0oqpjGYZBWepOKGvIacWbxxS-zBdwgQ99kkDRdyLHXJTtY_jAG24fq059dP_ldReuBM5QKK0g77z47Bw1PxKWWOsJu1D6W-UwXoUU5DyELHt7XK7aYi7oTllEZvDShX3wGk_jC1rGXz24H7GLoS7EWK_d-XNm7urNBrjjU2OSuLcTuy6D82HY0sKaXdYHIM7dn9Dhk49mc82GZwT3KveEYWGUFAbgQkoc43nkBXe0yMULxDWZcSPnKMM2_83Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7846e72a4c.mp4?token=o4ppe74WTVu8sTubd13_ZEvXK4830-RPwK1DcPCDa8-SsjxJITQ7b_Ep7tppKgM--B6O7Ul750m8xGtvOAHiGXdN-8_rI5OcNwG4W5ewj82T_3JP193ZlTXCLyKp1WPWbVkfX5zf3aWEEuLJdYCOvD3JAi8Gcfi3EPA39Q6BZ-j-Yt5DzFyS39ufph4tyWWf-0nnLzTc7L3sX2FMJFUncrKBFo5R0yGfNZWfsiljRwKPj9rRjl5AiqUh-I15K29xD3EMIzjrsTuhsXnlQ6PRp4-wRY8GvVRqV6c6eMCabuowACI5AlVu3x4SrNy0hScfs4i7cfXMoJqvzHS7JoJShTAcSApHtnorGEhJwY8djkuq3nIs2rGV_eKxhAfKqfhWAqgjHH_rOJ-i2w1LD_d1aWfTZIcqQVglME1F6IBMsI_TZ0oqpjGYZBWepOKGvIacWbxxS-zBdwgQ99kkDRdyLHXJTtY_jAG24fq059dP_ldReuBM5QKK0g77z47Bw1PxKWWOsJu1D6W-UwXoUU5DyELHt7XK7aYi7oTllEZvDShX3wGk_jC1rGXz24H7GLoS7EWK_d-XNm7urNBrjjU2OSuLcTuy6D82HY0sKaXdYHIM7dn9Dhk49mc82GZwT3KveEYWGUFAbgQkoc43nkBXe0yMULxDWZcSPnKMM2_83Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور داماد رهبر شهید و پدر زهرای شهید ۱۴ ماهه در رواق دارالذکر  @Farsna</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/farsna/457239" target="_blank">📅 19:16 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457238">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17c3a1416d.mp4?token=uSNi9lvDkUvWK3ogW3Wo05Bf5uVQGyQexvmF9fyVgQYhrcuezu8e9xf2lhHVtWcd5VttoMNa_gQyArSNuYj13Q_-RqAjE5-DUiV-CbUDXArfbdliwfbgxxoM-1VMpewLI8VrpFTTDUPQvtIsBrsm0KO0cKH0jeAEkZm4ZBuon0KOXE-JOO9v8S4Oxqcl2PZsq9f51uuj9YcKnHr2oDBna3qJyKlVRpFFwSdfN_oRZ6ofKBtWbOzBwgj8X0OEezYd3QgzH1-DAaBWcqDz57EdG3mMmkYZbn2nT-xaATxU_1rX5moD8LRUXDqHIlt4nnJBCaU5MR1fIRU-VFfMElQARw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17c3a1416d.mp4?token=uSNi9lvDkUvWK3ogW3Wo05Bf5uVQGyQexvmF9fyVgQYhrcuezu8e9xf2lhHVtWcd5VttoMNa_gQyArSNuYj13Q_-RqAjE5-DUiV-CbUDXArfbdliwfbgxxoM-1VMpewLI8VrpFTTDUPQvtIsBrsm0KO0cKH0jeAEkZm4ZBuon0KOXE-JOO9v8S4Oxqcl2PZsq9f51uuj9YcKnHr2oDBna3qJyKlVRpFFwSdfN_oRZ6ofKBtWbOzBwgj8X0OEezYd3QgzH1-DAaBWcqDz57EdG3mMmkYZbn2nT-xaATxU_1rX5moD8LRUXDqHIlt4nnJBCaU5MR1fIRU-VFfMElQARw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنجشنبه ۲۹ مرداد، بعد از نماز مغرب و عشا
🔹
مشهد - حرم مطهر امام رضا(ع)</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/farsna/457238" target="_blank">📅 19:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457234">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TCuFBbgogIWPYMuTchCiLiBG2JxFFUMYzozx6fmGMCOroaa_79fW-5V12eG1rPE66Q-s18sg0kuyLF4WRgyatngAZAzC3t31YhHzTgOxC2-_qyAopRotzvVO-7dtSFudsyRLKdpqpfeTtDq7Ge1KvTPXzg0V-61pEA5Z0gvLJBp1jlVXd9BY7tOYDvsAZlsgoPUyhT-p2hOVGt1ap_pRTOnJGZjAsjgmwiZGG50iZBGpjFoU3q_evz4P6HTcc03F9N-TJ7GbUtQ1BWFtjaA5C-t5IB31qx3FhaiSyQt2L7ZYThwxyEZxHvijcbRvhz_PLNQlwJtMgROjAaokIBeHUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cp76NI6NHikvuRQP6JroF7nos4KZB934TGoaRbit3Hrg06let8tiGH0_OioboVRPPbToKoep9eR9Q6i8NVjRdWGtloBsYppKiE18kTxyMF0Rm8IfORDxGVo-qnqG6Rhlh2RoxBSIh_ubP0ibj786hBU57UQfbi6B5XoWDmn1sLng17rNXkrYVgEyyaG3IFJKeVLTdy88bLi1OqDWej5L3M_g92OsJRiN8Xj9D2pSkaXk3lq-j-nAdYSiQVqnzx7VzB99NJcTOXxZ7Nkhg9ud2MJulSgc_8eo8qlsnpImptanSko4I2gTdmDy-VUahim18kn_L2404YPKgMZ7OtIbpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PvFyemXeHAIDhw010Yl9_rCg_igLOrQ8m5tCb0LQm5Sf573kbfR06aKBVNhsew9CbjO53faSeC7uA9HjemKYnlFE8a9HVMXE13R095SXv3hlyELTk5J6X81oNG1J7mQzUeYVcggXx-Vb7AYxHWbsAzDyM3vUbeQBgMuRTAd-7e21_Z9Eh6na9GXInBuFW0OJBOo3H_yxjY8jTpwAIcO_T3wF0d5f6kZxLwOjhULynZ9NdmqsZIgNGWHRzyVfX_QMlH_Nko0GyUh-fi8_U6qoknewTRNVq5cNvvswQGtTo2CekHfRuzZO53ikMrAujeamMZveVHZct7ISEMo91MG_sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v98poQbMJIlYg1znU1lxoNJVZnaig3BnPGxz1PYi0IJFGI39wd4o7jlHmUigLL7SG59XCZIib00efyab_RjjH8aN5nNtKejhxB8LZEvBZxk6d8HB5tvo9_5RJFP2Ukjq4nOkkiAAKZbYXhQ-F42qxaGph6Pu3Q2NV7d2kIJL1jF3AU9chbsojCim9111qq6afzgZhV2ThlIv5NxNZKsKSFtfSxDnmb1YbsnKE-fpzoY-OTYIBoff68B1iP6yAVx1dlKt6A1opDWsWvYko3Sf4hICXu0ZFAnSmATZ5RJWu8rZlj8RCQaGnbAOtznynQejEeYaO-lpHZ9VmYvo7VTqJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
قالیباف: ایران و عراق نمی‌پذیرند پاورقی روایت دیگران باشند
🔹
رئیس‌مجلس در جمع مردم کربلا در مراسم چهلمین روز تدفین رهبر شهید انقلاب در واکنش به اقدام مشکوک رئیس‌مجلس عراق در انتشار نقشۀ خلیج فارس با نام جعلی گفت:
🔹
اینجانب در این جلسه حاضر شدم تا سلام گرم…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/457234" target="_blank">📅 18:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457233">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7dd4f3fdc.mp4?token=pWfVwdorb2_mqpZLyLgzvqtQLg4-OAqGBV9FFXSYyApaWx42EaN_G9UTITOMmTdveHKFM6An0JJFvs-Jc1Qtwl5kSHcd5btWiX-ZUqHTVr4MwWmWA7FfuAMy0JQYdfo84qEcx-QFzhZzRXhEsGjTgUziDoY_12g2sCP-j96jqrEzLTB6dGgA3243zCLBGkvBNZDC0Mx4Hyqum7CcvB1sU4VEcMS8KX9l_VppNClr7PMiCqpAK5oVFT4uYrZ4s4Aa68rAnIK_xN6g-QHN9cwSU9C8RqpjWNdbzzDYYHkfZiQl3IEzV4WfkdUEtPlgjqS5WyUyZF3b1kvtspiSATSkOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7dd4f3fdc.mp4?token=pWfVwdorb2_mqpZLyLgzvqtQLg4-OAqGBV9FFXSYyApaWx42EaN_G9UTITOMmTdveHKFM6An0JJFvs-Jc1Qtwl5kSHcd5btWiX-ZUqHTVr4MwWmWA7FfuAMy0JQYdfo84qEcx-QFzhZzRXhEsGjTgUziDoY_12g2sCP-j96jqrEzLTB6dGgA3243zCLBGkvBNZDC0Mx4Hyqum7CcvB1sU4VEcMS8KX9l_VppNClr7PMiCqpAK5oVFT4uYrZ4s4Aa68rAnIK_xN6g-QHN9cwSU9C8RqpjWNdbzzDYYHkfZiQl3IEzV4WfkdUEtPlgjqS5WyUyZF3b1kvtspiSATSkOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
قالیباف در جریان سفر به عراق با مشاور امنیت ملی این کشور دیدار و گفت‌وگو کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/457233" target="_blank">📅 18:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457232">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37c9075005.mp4?token=Q6GhCFYITFQ2j10v4dubfj3T-i4kFhbLQ13MxmyimXmpDN8JaKVrB3mc5SP9TKAB7NZEpVF52nHn_bE8sFw79_7C_-NJQ6d9XAUsOaKjCVFiJ8z9qm8E---k6yvDm1P1d8F3Z9QJgIJXUEfxqb_vcz42Rq0dl8D1FoFTKAyxalJXia3wZp7TFEv47KWnTQ91v4XtDfqBGxEhVNI92-7_O71w5Y0yHn_DjQe05ernhtjERaayekp1xAcjiJV3tLRHJY4Pd-IYUyFshSM6AikKGQUoqRtAYKmMVv_53ItVyMWLMkY9PizK5YzQKMY0bXVzwXXUyW4YcGjl1L2GzVO0bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37c9075005.mp4?token=Q6GhCFYITFQ2j10v4dubfj3T-i4kFhbLQ13MxmyimXmpDN8JaKVrB3mc5SP9TKAB7NZEpVF52nHn_bE8sFw79_7C_-NJQ6d9XAUsOaKjCVFiJ8z9qm8E---k6yvDm1P1d8F3Z9QJgIJXUEfxqb_vcz42Rq0dl8D1FoFTKAyxalJXia3wZp7TFEv47KWnTQ91v4XtDfqBGxEhVNI92-7_O71w5Y0yHn_DjQe05ernhtjERaayekp1xAcjiJV3tLRHJY4Pd-IYUyFshSM6AikKGQUoqRtAYKmMVv_53ItVyMWLMkY9PizK5YzQKMY0bXVzwXXUyW4YcGjl1L2GzVO0bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراسم اربعین تدفین رهبر شهید در کربلا با حضور قالیباف و مقامات عراق
@Farsna</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/457232" target="_blank">📅 18:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457231">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIOmfLd-MH8wKxZWK4O2AotMpfP_4M2ZNEvXQQGlpcDi1c4GQkMje8cpnXL3SfJ5YaKTytMwZ4wfMs9dodIZT9dzSxOJxhkVxHTo9dfiLjWHUvgxz6EIO9yB-n1TglkJvN8vMnFryxvBD6STMqK-hHhoZa-uJllPhS7Vc--zzytwPsHxj6ISFWOzXbt67UD18fWS8_RBln9QedzSamS4Ql4CBRkPb7dqUDbxCXfjryNxVdhaRzRazKUKwWtS0PY0mymb_TIFuaQvVidUFxX1VA-3ajyPDn2fkMAy147JmxxcfVj6qdgbrwaNpL1DkqRf04hy62HrACtz3AKvaNmFvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت ترامپ به تهدید‌هایی که برای ایران خاطره است
🔹
رئیس‌جمهور آمریکا شب گذشته فاز جدیدی از تهدید علیه ایران را با کلیدواژۀ «کوبنده‌ترین عملیات اقتصادی جهان» آغاز کرد.
🔹
ترامپ البته نمی‌داند اولین تحریم بانکی ایران، آبان ۱۳۵۸ کلید خورده، شروع تحریم‌های سنگین…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/457231" target="_blank">📅 18:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457230">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfMs4aFSOuBsnsSR0j5jjbLd781etX5KGympaepYBtG10qgw-YteMkF4H247YHV7KEq_kVioeTkQ7cnIkI2Blg8gtS_SwqAPj8X7adnSRsqZJl3aSC4loLHuGtfo_IElLFchjqZ6O28Q-9bWVzFIBEnW1eFS4WJ5SV90d3ZtmEZCKHAuRATaiftT7rEziMdzuHAen56La2ly-QsY8gL6udeVuXQ4mj_KSPqu_D4xpziFRqZB04rn_SQ_9Wr-yvRroEb_Yz1hJ59inLYeLpOLCTaEsfL5evwxE1IFFFvUSD4rZd9JlAcH4yzg1RoILBuP9xM3W9Qd9SNECDQZkjid5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقب‌نشینی ایرانی‌ها از خوردن مرغ
معما شد
🔹
تولید گوشت مرغ از ۲۳۰ هزار تن در خرداد ۱۴۰۴ به ۱۷۴ هزار تن در خرداد امسال رسیده، این یعنی عرضه مرغ در بازار ۲۵ درصد کاهش داشته است.
🔹
با این حال ۳ روز پیش وزیر کشاورزی در نشست خبری گفت «کشور برای همیشه از واردات گوشت مرغ بی‌نیاز شده و هم‌اکنون وارد فاز صادرات در گوشت مرغ شده است.»
🔹
با وجود عدم واردات و همزمان صادرات مرغ، کمبودی در بازار نیز دیده نمی‌شود.
🔹
با حذف ارز ترجیحی و گران شدن نهاده‌ها قیمت مرغ افزایش پیدا کرد با این حال وزارت جهاد تاکنون آماری از تغییر میزان مصرف مرغ توسط خانوار بعد حذف ارز ترجیحی منتشر نکرده است.
@Farseconomy
-
Link</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/457230" target="_blank">📅 17:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457229">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAcGB2bqINxrp0RK5BecLNCqwmCjqD36pv2KbwOwM8vR5reXcYPfFLLMIoH30mxEVs5nR3deaxNJeR_YPN5UakuA_sJpnxSVt5051iKfMQaB2cV0rNImlexmUHW1o1STTi0bq_EJSDo_662wu3dv5fvpNOBUk7l81mA_iIsWJBRFSEG1rSn6xWl_DPzRFt_Y9547jk-BGoxiRBAbeakwJSrNma8D_CdeU2889IpAbIx7X9eTSxXjbt0jWLheHsEM90yCtsurZP3x5SovDZ_Av4Zag03rgB-slyktj8-KCzM1XuYktlLP5iIXnshzi0_oZeNbh3IgQ1a136WAjh3b-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
کدام برنامه‌های صداوسیما بیشتر دیده شدند؟
🔹
شبکه سه با «کاپیتان» و «محفل» در صدر پربازدیدترین برنامه‌های تلویزیونی در تلوبیون/ کاپیتان با ۶.۷۶ میلیون بازدید رتبه اول و محفل با ۶.۰۶ میلیون بازدید رتبه دوم را به خود اختصاص داده‌اند
@Farsna</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/457229" target="_blank">📅 17:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457228">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-text">🎉
۶۶ سال همراه مردم، از گذشته تا همیشه
🏦
شصت ‌و ششمین سالگرد تأسیس بانک رفاه کارگران را گرامی می‌داریم.
#بانک_رفاه_کارگران
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/457228" target="_blank">📅 17:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457227">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/457227" target="_blank">📅 17:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457226">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">عملیات پهپادی یمن در عمق خاک عربستان
سخنگوی ​نیروهای مسلح یمن: در پاسخ به نقض حریم هوایی استان صعده توسط پهپادهای سعودی، ۲ عملیات پهپادی موفق انجام دادیم:
🔸
۱. حمله یک مرکز حساس در فرودگاه نجران
🔸
۲. حمله به تأسیسات آرامکو در نجران
@Farsna</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/457226" target="_blank">📅 17:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457225">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وزارت دفاع: تجهیزات ساخت صنایع دفاع ایران بلای جان دشمنان شد
🔹
بیانیۀ وزارت دفاع به‌مناسبت ۳۱ مرداد روز صنعت دفاعی: جنگ نشان داد هرگاه دشمن ارادۀ ملت ایران را برای دفاع از خود هدف قرار دهد، با ملتی روبه‌رو خواهد شد که نه‌تنها در میدان دفاع و مقاومت ایستادگی می‌کند، بلکه با تکیه بر توان خود، از دل هر تهدید، قدرتی تازه برای ساختن و پیشرفت می‌آفریند.
🔹
جنگ‌های تحمیلی دوم و سوم میدان واقعی آزمون توانمندی‌های دفاعی کشور بود.
🔹
آنچه طی سال‌ها با دانش و مجاهدت متخصصان ایرانی در صنعت دفاعی ساخته و توسعه یافته بود، در میدان به کار آمد و در کنار ظرفیت‌های عملیاتی نیروهای مسلح و ملت ایران، بخش مهمی از محاسبات و اهداف دشمن را با شکست مواجه کرد و آنها را متحیر ساخت.
@Farsna</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/457225" target="_blank">📅 17:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457218">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dt0Lij65J9J63dBYkTUInUpU7t2FE61d9u2zJLJeu60jQUzyu2rgnnMDsYP6Ofk0NsOGVdpyOLjHwKMK8tbq7Eb8jdtjyaL-FYAQ8oh03gtw1aJ5JefTFuov94m-p0_nPr37gN7q56PUBXIqRWP6IE2BbAISB2K6IH3lLW4Vzmc4Yje5xY-MfuVIjr29du1dmjfWHG3nPx2D3JK3zQUtu6xuTUVLOZSPCHeZwSl6xbJ5F8nD_4UJcBNKYNQjMCBIN7553YehoYb_oqOosX0lpPrOh2jBn2IeJQU8jqyTpEj518xeT6VlI2GTXObAtcwQDDI6eHESa-oOLf0rFI8T2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tSDZbRaA5Egnc9-9ZPv4TjMMl1N38bi0wpGg10J_cswB5UfmQwZRYFNkgqB5NISi_W_DisH4EbvPy9QEnIh5pXGHt9REWnf4TedJ6kVhHFX15YHNkIfTV-fXsy082wA6n2tfLMFSd8_SGro2iem9HlIWJdHu0jDHRk_3gmSOj5UVN_UG9d8ZtNtYhQ66CtAvAbgYvfNcqCc9XvwXbw2x24QA_DdRN9Z2-VspBhJ7iXHxFvE60J41q2VtPafP5E0Xa-gwzB55LaaGm98KqgYQhhm_iW9ds-8nCE10RdEJ2rM6UT1dBqGPmIMYEgJZNyG0LIHKUMsW9L_PchQTRSnhWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUrznu0lBCxHF2oMoscbWU8_wwIBMbhLGkaFbBjU6FxVv7rcSMRRZzbZwjth0bbxD-92a_xdP8TUWLzv9mHy0RDIlTwiPG8W0no7PzgOALrtzmrKIqdcw74MvZvG8ImeeXWfKByFt1DWI1ujQCXipK5oBSClcgSEnxffLIeKagOfRAnw3xO1lDRndaJgUdWzlRvpgFeD_MeDcBjzFcf1xcw-pAcCb6EswCIeVjeeujj7lLj2nn2VRUaONNGPt43JzIsrg8MiNTTETqKPzzAGNxNbNr9rMebXz_iiBhdeB8HDc4sHNHwVoHOYNlTkPmzAdQg6WWStFf3kVB8VCxy4qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KJwYtgcSYHRvXH9u31tPfUpk3XFXVdHMRJ3vb6tV99lJBrJctEpygaRaIIy2ZPVeMVu0tWndK7tgy03MaowUVnlqp6ymaaJK3VeAGKbmnFrRyS6rqF9POzlJ2-DfZbYKoB3iiZHajmIENvSTcpgDlPd4LZqH_jzbAU7SgBsUPXsOMYOKlr8WTmfKy5IMUB68rUnzgk0-grrtLjTZotH-W0ELdIDGWD-O4RwJqCPd-WhLQY1xDge8GNadrqNArn4Mi2rKiU7Fa12co1EYsJvpMgAoZYbTorKYmvPcU5vHwmZZB8tAKnEGpqy1nMzlmzCNXBiDUsiiiMJ3DL1W-B4cVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dKOfQqg-3G9CIy14_KGXMSix3OACujhFvRfevKznKyjjy7VfZbsggijQY3IPEKmJIWodu8E0YZuQFUux9Wu12VCO8N6rZ9P1Elb4-OCRI5IiR9rNUyVwJTXmI8IAuBQJiTtn4FNFmYX8gqfB4GZ5xeVBVdKQpjHLDG5X6ZXW7J0vVCZMcKlC0r4yvFurfpSD2oe7Wo6WcpCbOt2oysbPYHRRTDunpMjlSO6Fy3fKwibMojLDlvy2yG9-SXoFiuXW510zupUqYih20CQ8RsbS-2TI4Ag29BsT6KZweLeDGmdfGa8utKtqhNhCd3Rt6f3KVL9L_7v1X3HYyeO-KlHjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cIjs7yiCv93F3H7ZYFOA9YJII7iQFrRHqB5_yDFQPQGfNgTB4ouD1kmZLC1llVdTOXCIMH1Dd4Mfin3MBv-5VFSy8IsAaELktAlLg6_mm3jVFQaiDvI9O7GoQ-Bcx2Z9PEXsCL_HK1jB9xOh0x9rHwiuT5Szm3BuS4Xytsal5G-aQp1AavOJ6r2nVLSP53__zAtpdBcW2vj_I-RFFFaM-lwYVjfxcreTOX6zoV7OAuT6RR0KR07dJktRJHNh5M1yIs4FcRgS8UwsOMlkEYcstgLyKLjjxxONTwuVmSkkr-Fm5W3JKCw4eJMSDWirqpBp0CTCwur1sfkaRUCDAoPUyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ssg97nm7fsnyZ9ciTkWPAS_BiKc9w4_cO8gM66tDC039mFoJpVEMvinBAPAcznF40chwTBmtRWXwNg8UACxsfvqm1_wu_M2v9WISLkTzQX7LJ_DGGEXogiE2CVdzudLmyVfw74gaAsdzdQ1kWmgkiJt-nKP0PIgVEuNnzXx46TcZRRqv9_WKxcetMtXVRsr9njcbMzNmNmZNDAFyiXjcn3mxAS7U3YbIMahO2aBRnbzPsbrFHWKXjrtfQ15rFIx9R3jnQxqkfykoevgL3HR4nXPV-NFlk_CmV8gwGGVHeFjJdsROdaDVwzJiwcp2YxfvXwLlJ6xx0cJr4oeVJ8b1iQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پاراتنیس روی میز قهرمانی کشور
🔹
مسابقات قهرمانی کشور پاراتنیس روی میز توان‌یابان ذهنی در بخش مردان با معرفی و تقدیر از نفرات برتر به پایان رسید.
عکس:
هادی ه‍یربدوش
@Farsna</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/457218" target="_blank">📅 17:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457217">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjQD2UYVJj2xokEaYtqgs3rNrx5Tb5kHoxjvO_F5jahUDI-xfZyb4-AZ5z4-M0Thp5BvzgCb6H44BkjgGVT8OxhiuOpVVGoDQtdUPtextK8y7CwQ1oK0sC7ApBprSuUHCIe4mb1fb2xG3qkPnE5FgUiaA2mb6DVTsKgsmNtpm1ZPOFC_Lt-OASVYSDxXHfHZ6I3R5YQRJwoA6n0fJOTJS1Bvaue2vrgwDIHTk3B6PuHzq-z4iwX6iiMmuJfJtheiFZc6Xe2-yGmUQhoLeBvGPjVqYlPEhAj0e26LupZbjz3i7QveodUFaastqXEojplDB9okcPR0hwkCRZXy6tJcoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیۀ مشترک مصر، قطر و ترکیه علیه اسرائیل
🔹
مصر، قطر و ترکیه در بیانیه‌ای مشترک، حملات اخیر رژیم صهیونیستی در نوار غزه را به‌شدت محکوم کرده و از نقض مستمر آتش‌بس در این باریکه ابراز نگرانی کردند.
🔹
وزارت بهداشت فلسطین امروز اعلام کرد در شبانه‌روز گذشته ۱۰ نفر شهید و ۲۵ نفر زخمی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/457217" target="_blank">📅 16:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457216">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🎥
همتی: ۷۵ همت از اموال بانک ایران‌زمین به نفع بانک مرکزی مصادره شد
🔹
این بانک ۱۱۴ همت اضافه‌برداشت داشت که با کمک قوه‌قضائیه با آن برخورد شد. @Farsna</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/457216" target="_blank">📅 16:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457215">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYRb4swhEW1pExai0tYYxs9v1tBMq_JjXDK3OM6t7pkh9zlTVZy4oy6oKpWkUzAuHlxwYxcNYMuzJH4KxhRE7btQks5qCmUy_Tykm8mxXdsTZk-u4Q_5cwM2_UWvyZ9NPQLihuHEWmjp_cvqunThnjKDvxnn9bY0YMnir06GQprPcTmOyIjyyRCiEDmsbXWAjg0tyeQtxjrTkrIrra5oRv69oRskX_mcdEpWsQ70qQb1MMENusGGSWfyI5bqmFbLnD-v_ioZGocrRVVPVvYmcLq1l63L5zzH4g0VaDAIRmhnVfHbcmwzscruwNrNEC79E8ghdMHwT3PnoPBaAKS4Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام جهانی ۲۱۱ تیمی به‌خاطر اسرائیل
🔹
نشریۀ اتلتیک از طرح محرمانۀ اینفانتینو برای «جام جهانی زیر ۱۵ سال» با ۲۱۱ کشور یعنی تمام اعضای فیفا پرده برداشت.
🔹
رئیس فیفا در این طرح قصد داشت بازی افتتاحیه را میان دو تیم فلسطین و اسرائیل برگزار کند که مورد قبول بسیاری از اعضای فیفا قرار نگرفت.
🔹
این طرح هرچند در ظاهر منابع مالی خوبی برای ۲۱۱ عضو فیفا داشت اما در پشت‌پرده به‌دنبال عادی‌سازی روابط فلسطین و اسرائیل بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/457215" target="_blank">📅 16:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457214">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/133c6b21d3.mp4?token=Bpo4aEQHYJzbwtZnUZ7AKlTOwTKddTrAkxRXelWmJPQBILG0FkLJVTI1wu-EKwW8xIuH_krW6BlWF9FELdFATfqPQJJwaabkvRuwGXm8E5OV-jfALyQcmzGaR0AlfNTwAnLgZuxEwwUbe9bGGbcipKDkU-GNR7QCNfaPCaZq5UgWifd2-8mVMoHbBd6MJ2ABC7S_2fDmP7nEwtMxUDgllisPe-IgIjPX1RM1e50KNRjMqYyvxtQn4iqXGF-sXddTji8gz8bGleWbbKtPClbMMdEuF0ucu9PDRctswAh4uvhPgs2Ru_TDqOSAB6Yifq5OBC11TwqfeYmPpkTyrpgCSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/133c6b21d3.mp4?token=Bpo4aEQHYJzbwtZnUZ7AKlTOwTKddTrAkxRXelWmJPQBILG0FkLJVTI1wu-EKwW8xIuH_krW6BlWF9FELdFATfqPQJJwaabkvRuwGXm8E5OV-jfALyQcmzGaR0AlfNTwAnLgZuxEwwUbe9bGGbcipKDkU-GNR7QCNfaPCaZq5UgWifd2-8mVMoHbBd6MJ2ABC7S_2fDmP7nEwtMxUDgllisPe-IgIjPX1RM1e50KNRjMqYyvxtQn4iqXGF-sXddTji8gz8bGleWbbKtPClbMMdEuF0ucu9PDRctswAh4uvhPgs2Ru_TDqOSAB6Yifq5OBC11TwqfeYmPpkTyrpgCSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرودگاه بن‌گوریون تعطیل شد
🔹
اعتصاب کارکنان، فرودگاه بن‌گوریون را تعطیل و ۱۰۰ هزار مسافر را سرگردان کرد.
🔹
وزیر رژیم صهیونیستی کارگران را به گروگان‌گیری متهم کرد و خواستار مجازات آن‌ها شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/457214" target="_blank">📅 15:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457213">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5RqprwS6DZOj-MoXhIhgquO0QSINk3XJ09XkrJl_xnO13FeoURkSOgnDkMJCWBxvRkm4PjcD6R1SZDBNh_dxh-QwZ9TuxzV1eKn-Vl8nyeiS3cFvAXSzA3OMrZCTrDZoT42OPlHN8SJ_YE6p6RwfyOvZEMmK62UEKqH-Nnx3I2PnOhGTmx3Vn07P4oDEwEF9D70qujYb6hAoCOSsTLs1pnOzXNWPTshaWL4-qfIiuCihJ0BN8vgkPHAq6hjZoByVE5xGP5oE0nEKpQ1zsem5KMv_lAW4yfvmgAm5ULKn8CqjWsfWSZRmJ9e41tXUwxIziaPgLGeMHbUTw7mNtydLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یارانۀ ۴۰۰ هزار تومانی دهک‌های ۱ تا ۳ به حساب سرپرستان خانوار واریز شد.   @Farsna</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/457213" target="_blank">📅 15:41 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457212">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d13f937c0a.mp4?token=De2YVJvKxDjtvLoZU4mBGaPaYkmmiAkfz6anjBv-OBQkAmK2GDf1v2NNfefJCL0XALUipaYLu8dci46UonzeRw8SAeIkomB9n3kWyNnSwy15xYHiBZrNHtGDFTM8x_83B-fUyEwRc_mFbkAVTXOVrg2bJ6P6Hx5Fw-kaAiEN02ipxUISecZPwlmD1vX6i0eaaAPUjbKqTW7LwwdfPgpaGTMBiNMtjX8xw6defUtXfRtgPguFgV2rExKv69JAJjJ8AWeYMnrgUh0fAuk0hzMgcY1IqR2k9V-FQAcsux5i2IXOL_SSyInHko5bFEvNrn2sDhToBtRWwS7oT7JdeN-Egg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d13f937c0a.mp4?token=De2YVJvKxDjtvLoZU4mBGaPaYkmmiAkfz6anjBv-OBQkAmK2GDf1v2NNfefJCL0XALUipaYLu8dci46UonzeRw8SAeIkomB9n3kWyNnSwy15xYHiBZrNHtGDFTM8x_83B-fUyEwRc_mFbkAVTXOVrg2bJ6P6Hx5Fw-kaAiEN02ipxUISecZPwlmD1vX6i0eaaAPUjbKqTW7LwwdfPgpaGTMBiNMtjX8xw6defUtXfRtgPguFgV2rExKv69JAJjJ8AWeYMnrgUh0fAuk0hzMgcY1IqR2k9V-FQAcsux5i2IXOL_SSyInHko5bFEvNrn2sDhToBtRWwS7oT7JdeN-Egg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نایب‌رئیس مجلس:‌ دریای خزر به اندازۀ تنگۀ هرمز اهمیت دارد  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/457212" target="_blank">📅 15:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457205">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VgvOl7ddcU9WUCZKeVtKUmtsSh9tB4fjaWMxXabMU5ydAS8dySxAfcMyoY3TPP60r3OhYat_y1bGF2AdlNm8bVA7hpB-MMRjdNpo-ZQLyG1O0t0LVMmAHXabgtLb4lSpcfqfrRnjCKiGiQvVD6-sXrU2vGhha_SOmraV4HGJ2WsibmsP0O4rDEHRj8eEvO4W12Uj_0Il2DWQkZC60sgtsz2-Wr6Z7SDlilE6pfZVRgAfmatWXkVgXzQa1FZha2mK5WD77RiS_1XLA5d0VX8Oi1yy7nQtjzL1AXPjj3ND2ZKcDW_TksKZFnvFG-bkXmT_0XqDo8wrtSQthlcEnQhLkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k608Y3GyrjbSQMXPKp3HkGfTi4cYKa1zPWH6bQDZaUPm16Y12UhWfSpRr15V2bdM8ckLlPnW96usHgl3aODTqKeGsolN2podDRXA1Uta8H9e8wGy1y1KqO5V29hVpK2K-e5J3GKy9UsORUIuYYt1nbyPXEr6I4CMeDsvia79AibT7iBGCjYrmLt-iItAv4GdrYwOvzMTJr83PI57bKqM9GvgMTe9Ya-9zBwLFeWn5Ey-b88_lgxuSB0_chmTZyADi4KYxIqL0pYL9-4TU3W2_oMfWpUM2xo27KJcr1vWw7mw63R6qb8NHMqbjbKmhBiD7aVyYwv1lyfetmXp_M61QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gA90YPuxW_vJwNvExru_dMCkWJkRCFrRGjN4cgS2xUH8Y19kkTsmkQQvU5YcYs5TMzCr_AYjztV_hqJN9t52ogo6wkaJLrLrE0AkE42usaT-tRzCJWyIVa-_YC6msf9-_ZiRRtaUzn7fLwWdp53FYn9madmpcfElIlO-bbi_mw9KrWxACMfccvh1agMvSL1cGNncrAzHxAyKfQAo_0Q7osvSMIlNZTgUcApe2pNO4PoEWMu-xnD7KYQWoZmTLwYZnfY7AsPx2KpBkLukgtFEsT7LJtitGwrxemNLZI8AyjHwqvxgM2kkevDNZWoqTmuwhSGq-rNwd3V66OyNFxGW1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gI4mZm1Be7dL71JHlX-Tc7NzSNWDa5ips8w85_HcNeDMZSwW1VfJzZW4IV0XnCZ5I3OFohru_w7QWN12kl_vC6S-8ACcJknjO6YJrimIgvFhSC9aFGtEkormaEDIY6O8-RyoEVBE9QWJZo8aBGuDG_84Qg7iYCWkqy8l9HJvoLqg47HC6cMyiP_oIlXp83Sol3KLoC9rv5FqI2qWwnbai-Ddv6yMRBRBBuQmEHwnQcYc4FBma1wFTamcmbFNicFRFNtHEkGtSAZvJF9ZURqfYGOVgWSyIwbKONbLgKQSVLntBzx9OhvhSA-04aNxMCxb0npILauaGU7LU8x6muxk_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OH6uM5Gf5fVIjcXUJT7fHM4DF9HR7cJVLgn4qkDG17MCXZNnWCo0ZKYv8ux19ndd3w5bOvPLmCrGR5Ibjd7nTCrLDdFk3LmCBF9qkNItY7YD9Xp6t3WP3ifbTlVfn_sv-W-ZDZ1VL1yeida9icFzB6r6CMUuir7de2TiVgxQSbcxV_PNJFSXsB4GtMDR1xQEJU6m8bUmvZnpIbDiSgV_RXD1KdDQEMQgMnymZltePh_afn6-8sFD49V9fBNtl0DiY3uM4kO-5ZIW6TnxI4bSZW_rwlApTlCjNbe0p_xZTYnqGN1jPqC2FDYCK3ZaqwL01bePyAOed9eXU3qMc0lSsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQuVkYqOF9WAh2jvKcyLH86wbrM-QjMM9Q_JRFvcMJiYmMLTYq-xl8-b5D8v2a5C2CFiRqp0H336BsqsdttAdNbKEm7b9Qn-_I4jWr3liRlqlxk95abYtCtC0pecE9HW5vuCgSk0Bi-ZuQpnJLYC1Anf5O-BkXDu1KstTz5q8vjxSzgDLPxyreYQ2WroX3rMFCfmwk-oR261E7R6lEEosEaZXNTY_QaSXlJXDCOO7PIOUbFsgh-GY5Xx4oMjZys7p91ReDeIEAs_xMrbD84ODa4RaOzzBSry6urJpdZvanv49nTSLL2Nwx9WsEtgvNNRYBB5F66EEYT2rVYVX08YXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XsmrnYLuDXeht360NUaJ9e5iJdQHX2OEBZmQrwNarRoTDGJh6fc2_1bKahKNKdE-zQp0k2Ptl4HD9btacPL80gKBGtUBveLp1hGlgk_n4UFNaiDvXGlpQUjm1OGYDjzbEMlp1wfGgS6e_FoBDMhzIX3qSKJdJYl7WgMT08f1MnjigZWuAdBY5iL2nSDlKqgJL2RhoZn0GuKhivZn5X4d0hVLXrZo6qnpj0hLTA95u4DfooIgxBewdDxLnePshNQ4Nd6sfioS-sgWRA_MqDl9bksxgxh82_RZvE1eW107YOgv5BHp9Mzcy06RfWkAis_viJhLKgDx0jlrowTkF87lXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رواق دارالذکر، ۴۰ روز پس از تدفین رهبر شهید
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/457205" target="_blank">📅 15:16 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457204">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f42fe88d48.mp4?token=isN2PjDopaPX9sXqqadLautMKO9ynDu8U6YZD9iY7AzP-h7jY8idPzMarfClZ2eSTkf9MIFOAT5a9_4exz0keMtNGou7yZbyz_M6A6Go1ek4FYa9KNVasnhoYHQyjkpAexDESk25NavCMfLnIUvysAZ9kDjv5Y3hHDCM8gRXEfrpNOEQ3l7tDNWxajtuB8g2r04KEgjsxYPRZrovovrlJhvbV0aidPw_8MBVuztB78fxna_QwTY8nIrF0NKtzsNysxE0IXu6mXUY-UAzQnb9hqhd7UpwFGOdzlr1c_7ltTekio_FNbvW2dQwTGMzzY2-47iiOA0yBWpQP90DunQ2IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f42fe88d48.mp4?token=isN2PjDopaPX9sXqqadLautMKO9ynDu8U6YZD9iY7AzP-h7jY8idPzMarfClZ2eSTkf9MIFOAT5a9_4exz0keMtNGou7yZbyz_M6A6Go1ek4FYa9KNVasnhoYHQyjkpAexDESk25NavCMfLnIUvysAZ9kDjv5Y3hHDCM8gRXEfrpNOEQ3l7tDNWxajtuB8g2r04KEgjsxYPRZrovovrlJhvbV0aidPw_8MBVuztB78fxna_QwTY8nIrF0NKtzsNysxE0IXu6mXUY-UAzQnb9hqhd7UpwFGOdzlr1c_7ltTekio_FNbvW2dQwTGMzzY2-47iiOA0yBWpQP90DunQ2IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از خاک تا عرش
🔹
ویدیویی از مسیر پرفراز و نشیب زندگی سردار شهید علی شادمانی؛ از نخستین گام‌های کودکی تا آخرین لحظات شهادت در اتاق فرماندهی جنگ ۱۲ روزه
@Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/457204" target="_blank">📅 15:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457203">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1793614afa.mp4?token=XjxnGARPktwwHNMpwM9Lbqh5B_n5TWjLLarRY50dseohgZ1KE4OunqebXfFEnj43atxgAa9rOVzpJ7a-ZgY_gm4pboP5_utOg0PrqkJFUU6fWkKOsPqcM44F7QecaPhUTZDPo62haQ0rPnXYPUTksu0MJQa7pX5sbplAYN7Mflqos_g11G1YDXHJVGlPQosMNKucuOo_5lf3K3pLCErntMZBRd4RmRu0pz7xVgjflpivWJLmQNJn6p8S95nQTfCc79VrbfuzgcI_gHcC11_rUZuFXO_rw9dMcJehdY7pQm22VlStAQsN2OhJGH_Wtp6APImAXZPHnUgGHRFfYWBEWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1793614afa.mp4?token=XjxnGARPktwwHNMpwM9Lbqh5B_n5TWjLLarRY50dseohgZ1KE4OunqebXfFEnj43atxgAa9rOVzpJ7a-ZgY_gm4pboP5_utOg0PrqkJFUU6fWkKOsPqcM44F7QecaPhUTZDPo62haQ0rPnXYPUTksu0MJQa7pX5sbplAYN7Mflqos_g11G1YDXHJVGlPQosMNKucuOo_5lf3K3pLCErntMZBRd4RmRu0pz7xVgjflpivWJLmQNJn6p8S95nQTfCc79VrbfuzgcI_gHcC11_rUZuFXO_rw9dMcJehdY7pQm22VlStAQsN2OhJGH_Wtp6APImAXZPHnUgGHRFfYWBEWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستگاهی که پس از ۱۶ سال برای نجات بیماران سرطانی روشن شد
🔹
رئیس سازمان انرژی اتمی: قرار است تا پایان برنامۀ هفتم پیشرفت کشور، ۷ مرکز سیکلوترون یا شتاب‌دهندۀ ذرات رادیواکتیو در کشور راه‌اندازی شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/457203" target="_blank">📅 14:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457202">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مدیرکل فرودگاه هرمزگان: پروازهای مستقیم بندرعباس به رشت و گرگان پس از وقفۀ چندماهه مجدد از سر گرفته شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/457202" target="_blank">📅 14:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457201">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3e389e3f.mp4?token=fp9WGYeojoS4BGtK1oVKaLnPEar1QdcJBsgVXOIZPe4A3PF2TD7kf6HVxz03NzSXtcb-Gl1E0RPD_Z7PXns7tI1KzVjygXW_KaIBUZ6af1-L4ROmgcX5cZfz5HIUAtKU7vSokhA1qDO5dqLoVvJxdLRiitnGW2boV9QNyMtt4qEJQset7pIDFIBkrV7qQYbR_EI9cRMJgxqaApcjXrLPML3rx4eYMg6jH1J88CsPGlxKoAItJi3CgKIo-XI2cF9t6FK0BNMVK24nmtM_MCyDX7413s6B4Fzo97f0Aavb4oNVw2gvHCm0QUisTJaeFRVH7iAS_8N3v5LBILtgkXzaILOgl4WrMwxqgxdLBKv-N32g_vkk2M9vX7pG-40MJqb-mf_KMK0qwh2gVV0Pl_101ls3h4RXZIU_ZnTdO_SwgyWrfCLSBhvC_RmcwTAkVIePxiijxTFC5CfKhbZoKueG_A-GGdiZ5ay0qXIfNbboeCglILJ3p1fanWZPJo8hbToIV6ownoCacIMXNoOQkEN0V2vPODgXhkhgpvVWJSniWkqW8qOl7tpxk-9XyxBpidio1OZiUuBt9Oedb5dRfdxPab726kUqEjTwH91Zoahkka5OYS7IL_n-gG2iqvRpx83cX8zm6LdEZh9ikgsd4nXvMKmX3fEclNouJRHFf-Zd1Po" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3e389e3f.mp4?token=fp9WGYeojoS4BGtK1oVKaLnPEar1QdcJBsgVXOIZPe4A3PF2TD7kf6HVxz03NzSXtcb-Gl1E0RPD_Z7PXns7tI1KzVjygXW_KaIBUZ6af1-L4ROmgcX5cZfz5HIUAtKU7vSokhA1qDO5dqLoVvJxdLRiitnGW2boV9QNyMtt4qEJQset7pIDFIBkrV7qQYbR_EI9cRMJgxqaApcjXrLPML3rx4eYMg6jH1J88CsPGlxKoAItJi3CgKIo-XI2cF9t6FK0BNMVK24nmtM_MCyDX7413s6B4Fzo97f0Aavb4oNVw2gvHCm0QUisTJaeFRVH7iAS_8N3v5LBILtgkXzaILOgl4WrMwxqgxdLBKv-N32g_vkk2M9vX7pG-40MJqb-mf_KMK0qwh2gVV0Pl_101ls3h4RXZIU_ZnTdO_SwgyWrfCLSBhvC_RmcwTAkVIePxiijxTFC5CfKhbZoKueG_A-GGdiZ5ay0qXIfNbboeCglILJ3p1fanWZPJo8hbToIV6ownoCacIMXNoOQkEN0V2vPODgXhkhgpvVWJSniWkqW8qOl7tpxk-9XyxBpidio1OZiUuBt9Oedb5dRfdxPab726kUqEjTwH91Zoahkka5OYS7IL_n-gG2iqvRpx83cX8zm6LdEZh9ikgsd4nXvMKmX3fEclNouJRHFf-Zd1Po" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
آزمون سراسری در دانشگاه امام صادق(ع)  عکس: محمدمهدی دهقانی @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/457201" target="_blank">📅 14:13 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457200">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkigA8J0yAnL6tfUbeSRuwvk3SPckVVejGjHUzEIPpCNtVNdlpm3nlq1TSP6tVhT11kdzfHTki-COroa7hBGgtIQ0dkdtT1k1lOLvqKoPmCIzynrkyplYORnHqumWgGCAzvF2XLtDenzfyjv0GJRj8HlvvilxpAUtah-lkqiNrXi5NtqrhMJv_ElOTMO6cUKvlR-u1__zHp-pq9De9_1HwoSPmGA_kgYpEoTARuNlLvqSknTTGaNiSL7lFQRCa-2TOYOwBkFylwpW5tq9bd_OYsVg2eFDmKtuOhXzMUZ9bMeZHVV5-83fv5n8jPArrEJl_Co_Bu_7co_BJPG3obmfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رایزن فرهنگی ایران از فرانسه؛ وقتی «مهد آزادی» تاب اقدامات فرهنگی ایران را ندارد
دولت فرانسه نیلوفر شادمهری، رایزن فرهنگی جمهوری اسلامی ایران، را از این کشور اخراج کرد.
شادمهری در دوران مسئولیت خود، با برگزاری رویدادهای هنری و نمایش‌های ایرانی و اسلامی، تلاش کرد تصویری واقعی از ایران ارائه دهد و در برابر روایت‌ها و اقدامات مغرضانه علیه کشور، روایتی متفاوت و مبتنی بر واقعیت ارائه کند.
نیلوفر شادمهری پیش از این با کتاب «خاطرات سفیر» شناخته شده بود؛ کتابی با مضمون روایت تجربه یک زن مسلمان ایرانی در فرانسه که مورد توجه رهبر انقلاب قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/457200" target="_blank">📅 14:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457199">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarmaye Bank | بانک سرمایه</strong></div>
<div class="tg-text">⭕️
📊
عملکرد هشت ماهه منتهی به ۳۱ تیرماه ۱۴۰۵ بانک سرمایه در یک نگاه
📞
با ما در ارتباط باشید: ۴۳۷۳-۰۲۱
#بانک_خوب_سرمایه_است
🔽
بانک سرمایه را در شبکه های اجتماعی دنبال کنید:
📲
اینستاگرام
📱
تلگرام
👨‍💻
وبسایت
📲
بله
📲
ایتا
📲
روبیکا
💖
آپارات
📲
سروش</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/457199" target="_blank">📅 14:09 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457198">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/457198" target="_blank">📅 14:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457197">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/341e45a744.mp4?token=EdsaX_i-XJClq9FL6zUcp4oePtfMWAnn24wcYH5QkEOwy3LescyGNJfy1aDYCSIgN6KFr7uFRQwrbtKQe-1gswtNixa8ck2sONZyuZTjxEcEzOqxuHJnSRK5AoI-ValMxoYT1cltExM4Z8KPAybxypbEO5JGUSnJx8np4vj4pYaagbcND6Q6h2yqE7iZm4FVJxwDHYqnqjiSN07sbnw1tjg1A0gSZ0JrBMKSXvctkhBJB3XF4_0y01jSj8udfa8LS0gKpPYFc63n4_DeGgUmfA2YW-cRYNOfmo44DtCRlpfQrTPgt_7RrlIb5NOKtw1VJwEgDymSGhYby2zHqrqLdCzITCfLPGsJXMCTGUk6DJQqYG1icr37TTpDWry_496fr57uw0dyeS7bhyjPNSkO81TvWqN0zGcIvTiALG_cK44_q16lxgWWtbFr3kfS45Gnn2O7A9Cmgel4XwFtk1lPd2-eqkqLNu9OxJ8QKzENNIKxssYoz9XeiePAbe-PFjsIRgVq_auffHI37OCeeIe1ZjMWWS4rfyQGLW1Vukir7IH4B0KUt1MEj2TLWHoNuSfwyjTuxNyvXORBbSgfbZmZYmJ3udhEj0XYhCN4XMB3y8bGPpfhx3IzkJkejLie2ux2vOckwDfXsG1Vb5yl556ZdC7cW9uvXNdjmKWz3NaJlFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/341e45a744.mp4?token=EdsaX_i-XJClq9FL6zUcp4oePtfMWAnn24wcYH5QkEOwy3LescyGNJfy1aDYCSIgN6KFr7uFRQwrbtKQe-1gswtNixa8ck2sONZyuZTjxEcEzOqxuHJnSRK5AoI-ValMxoYT1cltExM4Z8KPAybxypbEO5JGUSnJx8np4vj4pYaagbcND6Q6h2yqE7iZm4FVJxwDHYqnqjiSN07sbnw1tjg1A0gSZ0JrBMKSXvctkhBJB3XF4_0y01jSj8udfa8LS0gKpPYFc63n4_DeGgUmfA2YW-cRYNOfmo44DtCRlpfQrTPgt_7RrlIb5NOKtw1VJwEgDymSGhYby2zHqrqLdCzITCfLPGsJXMCTGUk6DJQqYG1icr37TTpDWry_496fr57uw0dyeS7bhyjPNSkO81TvWqN0zGcIvTiALG_cK44_q16lxgWWtbFr3kfS45Gnn2O7A9Cmgel4XwFtk1lPd2-eqkqLNu9OxJ8QKzENNIKxssYoz9XeiePAbe-PFjsIRgVq_auffHI37OCeeIe1ZjMWWS4rfyQGLW1Vukir7IH4B0KUt1MEj2TLWHoNuSfwyjTuxNyvXORBbSgfbZmZYmJ3udhEj0XYhCN4XMB3y8bGPpfhx3IzkJkejLie2ux2vOckwDfXsG1Vb5yl556ZdC7cW9uvXNdjmKWz3NaJlFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای یک خواب عجیب بعد از شهادت آقا
🔹
در هرجایی به آقا توهین میکردم، اما ایشان به خوابم آمدند و...
@Fars_plus</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/457197" target="_blank">📅 13:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457196">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiFyr9838XiovIzFpy1WjlaVdC4okY6yRB7W_0ehHhfPyRgSBFOwiXywazOkUk4uk3EcptsjAGG5zmLDKXvOPD3UsWBPaiOTIFdOLdt0sGcm8S7ecgppm4GfirpXEfVCAy_yflBVp1x9flXmT_yOe9s8TwKOg0GxFcjkmgcX2M9zLlG5JkMZtRlsuVcmXCFUMxklEWw2C-2rUwKBiDbm12H1p1y6Dp8IwUQ0bXVN0_fGcAve9jI747yYUc8M_q2AswD6mwkA5upESKdwCGAID4ey10wQ3NoLLyE9TV7Qp4PuBn_sStwq1pe7IHHzcHRQXMvToNz09uVEPxyLV5QxAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت به بالای ۹۳ دلار رسید
🔹
قیمت نفت خام برنت در معاملات امروز با عبور از مرز ۹۳ دلار در هر بشکه، به بالاترین سطح خود از ماه جولای (تیرماه) سال جاری دست یافت.
🔹
این افزایش قیمت درحالی رخ داده که نگرانی‌ها دربارۀ اختلال در عرضۀ انرژی با بسته ماندن تنگه هرمز و بن‌بست در مذاکرات، بار دیگر بازارهای جهانی را تحت تأثیر قرار داده است.
🔹
به نوشتۀ الجزیره افزایش ریسک‌های مرتبط با ترانزیت نفت از تنگۀ هرمز، مهم‌ترین عامل جهش قیمت محسوب می‌شود‌.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/457196" target="_blank">📅 13:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457195">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVGqF7VrXF2kS_yv23voidq7Zxi2ckIg96QQtcT9npJ3kPA4dKGrwduRNKRY5jP_0PW3IN25a6y0nb0QOCd9ErrZW7SBLP5KrMVuhJj4NQIsOjL1bSk4v0Dmdl4g1XBwV2Rj2C4XNzlHOT1aQEE6yZnYrFhzuMHJrfTOt080lOcC3KgZwtghPzedAdymz6DKq2dTmCfKRG5vvLKghkZpVtJneZTDeMSSNJe7wf1u-eotZXLwRyw6RqUDlX3jq3vLV5hoOkjZAnexpv2FxUa56jKyWVgw2vRbFo0284P-o5ne2pLcRbn3JqDTLS0pDIafu_ByzdI_k4OdZmxTcZ9c9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثۀ دریایی برای یک نفتکش در خلیج عدن
🔹
سازمان عملیات تجارت دریایی بریتانیا اعلام کرد گزارشی دربارۀ وقوع یک حادثه در ۱۳۶ مایل دریایی شرق مُکَلّا در یمن دریافت کرده.
🔹
براساس این گزارش، یک نفتکش که به‌سمت غرب در خلیج عدن در حرکت بود، اعلام کرد که یک شناور غیرمجاز به آن نزدیک شده است.
🔹
این نهاد اعلام کرد تأییدیه‌ای دریافت کرده مبنی‌بر اینکه شش فرد مسلح وارد نفتکش شده‌ و کنترل آن را در اختیار دارند و در حال هدایتش به‌سمت سومالی هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/457195" target="_blank">📅 13:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457191">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jBtrogEf6mZsVSCk2bicyhYqKHMh-xEiEfFSIkal_4BsVRmtZJdb4jsMvAZIthrhP21Yjc7hwkKiluciLefq9scUhpMhB8kzys45z-AXqGGDKkJNh1OqDBgG4FaSL1U64balxJHeK663cMnWk_SxXpfkaAN9qOqbNFi_SELp7cQxY8XVHfkVnKMBWnFqDP8chNdGhotXwKllOYofJ1apZBpNbs_KC1xQxGNb1GYhFU6u8XwjBI168MJxO6DU3zkCTTmaoDqJYu-hPN5Ci370L6ZZ0xmXpDs2fAtiAbrE-ZpJlsJtHNS9z3s7vb3Hzq8l3-1BjuiwkEen6FbMRV1KYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WCFIdRav0jP9R6YWxoulq-EZ7KNZNTqOyO7Uwi-aTmwoO9ex_ntK-zpPJrpVNyPelnLQ-7lhMHdxDOSsQOSLhcf7RBkDKIJCnKJXsKl4JR-4T-u88A1oJARt0kF0A7dN6mVG-lQNHv_Xz2UsXn-F6Sm1ephEe3fY9E2M2YsiGXd3vS9pEmQoYBk2vOLTMf4zXbn0aRh81OD16MNTrsaaEX6PmUWqUi_HG9LXD898IX4UZKEFF9K-T5RMO7Ub3QK7zZikFTtJ35w5n3vA8vNazjITLpTtaTezAeet5MpZb7-vzpxAwvWplRGLvuzC4utkHN73pBa-1FoKHLwKLlkYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hENDmd4aEqnjgx15deDNE9hlB9EPd6t5NBfpultlfEfSXRJEHqV1rvF0AAPX28_JaTrJ3FFyfD3t0oVAezK7O1STU628-fk7nArZsq8VoBgSI7EQSjHXGi5yQFO_VQL3IplqEIdGt6taON2OGMRrbBnFhN03-5hlUg0YCZoI1uxOBQrECwyFwE7iRrzqGgWkqU8eBXLRwIqo_fECGZGAlSVTGtXaxjGGfUtXpaL3KOQJhWe2IrxGsOM4vFAoF1UySdtGvsmBr4fyMzoGmOWJqRihrmGlb0K6ibrRKTl5wa6BZP6W6oesHl5zFsYpTcoaAdhYM7dOIwNw5ArrmSBSQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d097d3b42.mp4?token=J0SUGa_lMREK1G0DDXWAZhWTVtz2yIO7rNFlYg1TZrRTncsKChCPnqSLHoEbFSv10_U3PSK3m1Sucy2Dsj7LqhXtYu4bYJ8vMBRFLVLpi7E_YhEkjSUbqRamDvutgbWgXvlzCKSa36yWGD-idt1w-AdouOwpniv60Pu3hHiSbb7jxUT8Tv979tg38jfwXrkb9MVB_v19OQFrA0NPnirDsQhRufK7B6E8tGGi67z4XqPMSmJzCYcOrTpTPx3K5JAZT6NafPEZlW4Nl4BuQddF6NH3wLAN9a_UhlfB5Tvc5aq3WBvNwWYiYbJYYIfrPU3C-QtgOUPfmb3kZptFJF8h2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d097d3b42.mp4?token=J0SUGa_lMREK1G0DDXWAZhWTVtz2yIO7rNFlYg1TZrRTncsKChCPnqSLHoEbFSv10_U3PSK3m1Sucy2Dsj7LqhXtYu4bYJ8vMBRFLVLpi7E_YhEkjSUbqRamDvutgbWgXvlzCKSa36yWGD-idt1w-AdouOwpniv60Pu3hHiSbb7jxUT8Tv979tg38jfwXrkb9MVB_v19OQFrA0NPnirDsQhRufK7B6E8tGGi67z4XqPMSmJzCYcOrTpTPx3K5JAZT6NafPEZlW4Nl4BuQddF6NH3wLAN9a_UhlfB5Tvc5aq3WBvNwWYiYbJYYIfrPU3C-QtgOUPfmb3kZptFJF8h2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تخریب برج ۱۰ طبقۀ ۲ هزار میلیاردی در اراضی ملی میگون
🔹
عملیات اجرای حکم قطعی دادگاه برای قلع‌وقمع و اعاده به وضع سابق یک ساختمان ۱۰ طبقه و ۳۰ واحدی غیرمجاز در زمینی به مساحت ۳۶۵۰ متر مربع در پلاک ۲۰ منطقۀ میگون شمیرانات آغاز شد.
🔹
ارزش این بنا بیش از ۲ هزار میلیارد تومان برآورد می‌شود. عرصۀ محل احداث بنا، جزو اراضی ملی بوده که پس از تصرف، ساخت‌وساز غیرمجاز در آن صورت گرفته.
@Farsna</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/457191" target="_blank">📅 13:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457190">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a88da1c3.mp4?token=TqXJPCSFDJcfdZqrYc0fVY9HhLHEKZARJm5iHHuIYAdIz1StsOLEjsJg_KQsRmBvRAOIpfFY6SxdipMNs1p1V-Tbd5b1bcC4Vvk-RnS8P1kpOvRc52sfGwOcpEVFvKJRchvoNBk9V6aeZQvK0T6bM4btUHJFfNTnkS2ThnOt4nPsQYH9piE7RePTKCGEQ29LEwVlc4FPml3OT2zk3AXlDLnR4Hesg9ve5TOOwAl-1XiElIDc1o6cMPEupLDfE3mf8AN6yXf_mYdJGEbTpyFWgl5sxKFR-_tC3EyqY_ApSnL2Vcw947EcAVYSH74Y8IpZvHtXgnDlBytRxwA_I7kswA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a88da1c3.mp4?token=TqXJPCSFDJcfdZqrYc0fVY9HhLHEKZARJm5iHHuIYAdIz1StsOLEjsJg_KQsRmBvRAOIpfFY6SxdipMNs1p1V-Tbd5b1bcC4Vvk-RnS8P1kpOvRc52sfGwOcpEVFvKJRchvoNBk9V6aeZQvK0T6bM4btUHJFfNTnkS2ThnOt4nPsQYH9piE7RePTKCGEQ29LEwVlc4FPml3OT2zk3AXlDLnR4Hesg9ve5TOOwAl-1XiElIDc1o6cMPEupLDfE3mf8AN6yXf_mYdJGEbTpyFWgl5sxKFR-_tC3EyqY_ApSnL2Vcw947EcAVYSH74Y8IpZvHtXgnDlBytRxwA_I7kswA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین عکس برای کارنامه
🔹
براساس یک داستان واقعی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/457190" target="_blank">📅 13:38 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457188">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bb2b16fd3.mp4?token=DY9NAZ_GHP-De6Sj0KH34YRbsSB8HIKjQ7N7qBn1jnKQTmhJNtBvQhYABUWknPwzxAt_X429C8PDmpXllXpomZWq5Yxfr1zj5Iwo7MHUn-buSn6VbpjEEeHamGziCQehQBZePLRWiBcJTKnkg7XVldWEI6UGp7qRLBZf12jdlnNNzkebh6sjijRfE1GoPF5NtqR0IvDIEGnHzODzkiT9vDuVnRwQ6B5TOhZzob6qH2vMS8DDcEGwdYzRl5RAgK1q9_2bDCmxzhZ0OJ9tizlM-JtG9JU360khmK7PeCQVd3GuIgDii9CYKvMNxos0txPqZfAiNxlBQIUEH7-8UKeXcoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bb2b16fd3.mp4?token=DY9NAZ_GHP-De6Sj0KH34YRbsSB8HIKjQ7N7qBn1jnKQTmhJNtBvQhYABUWknPwzxAt_X429C8PDmpXllXpomZWq5Yxfr1zj5Iwo7MHUn-buSn6VbpjEEeHamGziCQehQBZePLRWiBcJTKnkg7XVldWEI6UGp7qRLBZf12jdlnNNzkebh6sjijRfE1GoPF5NtqR0IvDIEGnHzODzkiT9vDuVnRwQ6B5TOhZzob6qH2vMS8DDcEGwdYzRl5RAgK1q9_2bDCmxzhZ0OJ9tizlM-JtG9JU360khmK7PeCQVd3GuIgDii9CYKvMNxos0txPqZfAiNxlBQIUEH7-8UKeXcoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یابن الحسن آجرک الله
من واسۀ اشکات بمیرم
◾️
سیاه‌پوشی حرم رضوی در سوگ شهادت امام حسن عسکری (ع)
@Farsna</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/457188" target="_blank">📅 13:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457187">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QpxnptoLqDDDfznJ5QROzEhFe-Gm_0oY9GVSfK2pexbdml-VzOp0oMZovhYv6UGCNn6zb7071J3DCeIS5BpBL4djRWbDVdAqtuEiWcnpoCPUo1MsV7Ui-KlCGRTzb-z4gAatDrT2vXlNdGj2fndbT0zEH-8xQqAy34Jq2XEo0rDITKaHQkg4k5lipLr-fHOTS-hTAQwWcX05sT9UKeUoYl_HkuaGp6YJPGcTYHQn-238xDA52A3FwIQawQ1V3XcPeikZ-9BN1uKFtb9r71HJnT5GMwqpu9bT-2U_N0Bc4sthhmquC5ULQ6LK5OZUHeTGToIXWRynmFz0dMoy_awzUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعاهای تکراری رئیس‌جمهور متوهم آمریکا؛ ترامپ مدعی آغاز جنگ اقتصادی علیه ایران شد
🔹
رئیس‌جمهور آمریکا ادعا کرد واشنگتن «خردکننده‌ترین عملیات اقتصادی تاریخ» را علیه ایران آغاز کرده است.
🔹
ترامپ با تکرار ادعاهای همیشگی خود، مدعی شد نیروی دریایی و هوایی ایران…</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/457187" target="_blank">📅 13:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457183">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WG-j8ox84LIkQstS5gNIfYJimlJ1xBDS1a087rNY6JOKVWT_2BNNZA9_Bu4JkraHPBAaJUZrpxb2xiD4yBidRxAmd9z4V30w-y2k5bz4oBHMiWaJAilGSwJRmxdhSQsPsu0YaoEQMPp34H0ah4Dqo11oVr54h3LLPtSvwYshsa5qzlVT-F0s2e2y9llVmAKODs2KtR1WPrrk4AVmGEMInppsok7ASCuDGVmWV8CFoL5J-i1OXO6sEO0nnZKRze9q1R5ak6RHBI8AhMvyjnIc6jf2DExhKZ8wId-Mutyu_W3Z2_RhRj3BsvSwhgcjrT4ccYYcuzVf6IIiJ2zQAYs1_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_ZiOzmkXMy3gg6_kaEzwJTuIyLnjayzxi-_L6f3TXhpDeQE8YEIfxstQJY49mc1VTA9yDAeT8PAN2nVPITYZJOESurqWrLYU-bOAscamA71HqXBrDG1wytuD4nyGvMI7SccQK2BBgJVkJp9RSqMiomulo_RM-K_-8J7NDXpBwOXl68HS8jjwse_alij3N-ztPsK34NQb8fXnlcwGUVHI-min65Mw1qxQqsmnXLU99mP8iQcoD2ZGunFcjRmC8Br7ThD7CeOsYuYqRCrEMWNmtb_WYBKickQtslUYcFdTHm3nW0BAGKCDb9KCoNAfNpWRJCWQKVx3b2j7he7Vjaqsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gn3PCuBoWmGK1fXv3Buc71EHqf2ZRVIOrSd0iCWo0sqh35Uf8hU1PlqcQKnpcjLcqYRFdNE-Wd_49nErA1W0sLpxLurH7qKIVWxh4ei6Mii4chFq3o_MAZSiFvboTTYcwR48asYprXbThMaZqde7a36oDE4oDmA-nOIiBcGUjdz7VGn6Ahq_k83r282eUz1-t8H08jiS7gI_fnySMdBPJIwBRXdfABbdnTH489mviOEejOPi981WKVBLLCC29Bz_xOOAJ4rimeV0MSFmnHjKgAgHGHQFf9gO1KJKilwigFTk2hdQhJOwM7IsQuBGnKWY69QGpJ0UKuDcMGUWRaH_dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l0bkjyzq-KJxW_1E-emNILkefnvdfGeoghxI1YCFMMpxW-KvH91Yp9_-KlSVYxB0CYbzIfRLBffvIgv0Ht5dLXSEIFKQzShPIvod0Fp8AvBiu2MpP-NpqRR57Oq-KDrMYnBw2ujI9svyKDnFofwazWXfNcyLEcL-r8yPaDKXIWSWjiEFYVcV0mJaDf6C3tp9hYu9_dUeJ_s4-_qqrG2nTlY73m3faRR-zSxiUH3hhOYtK2ShuNpBGcN-g2HuawuzojBr-KKuzFo5iyplwTNAE77PlU0Cj3LNcCUJ2dUM5ulKyelAZsqJLxLy4NP1m4pYXuMQ-onE77406C7WOXtoQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قالیباف: ایران و عراق دشمنان مشترکی دارند
🔹
رئیس مجلس در دیدار با نخست‌وزیر عراق: ملت ایران و عراق هم دارای اشتراکات جغرافیایی، تاریخی، دینی و مذهبی هستند و هم به عنوان دوستان و دشمنان مشترکی دارند.
🔹
ایران و عراق با نقش‌آفرینی منطقه‌ای در بین کشورهای اسلامی…</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/457183" target="_blank">📅 12:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457182">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546529e1b2.mp4?token=RrAD8-JPBVun9TOPHYcAvmIw7hWwiN5xWGrnyIjueyW4VGjMFzValjCd0OACzzxJBA5AzTLTPkOAeZ_7W3EsCi4Twn_K6viLRbQqBiHhueygFS-wP4-tngkzyIdsG5vv85o6rBTEM_ALMGk8sBtcuB9e3sR2xCw7HJIPQwN9v6e_nP22vHCvz8Yrw8XTqD1R_L6hNgeyD-iuh_S-asFJl5DY9mfYThVMJYWkgo9j4YPpi6PCd885qFW02G8_7TQQ3Sm2O93z973434D9EymMos7cvxABaLHJnHB5jyTVn6hOFTHuvh_tz2km5_H2JcSOY9FV-YmrxhFfgoR0LtKUDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546529e1b2.mp4?token=RrAD8-JPBVun9TOPHYcAvmIw7hWwiN5xWGrnyIjueyW4VGjMFzValjCd0OACzzxJBA5AzTLTPkOAeZ_7W3EsCi4Twn_K6viLRbQqBiHhueygFS-wP4-tngkzyIdsG5vv85o6rBTEM_ALMGk8sBtcuB9e3sR2xCw7HJIPQwN9v6e_nP22vHCvz8Yrw8XTqD1R_L6hNgeyD-iuh_S-asFJl5DY9mfYThVMJYWkgo9j4YPpi6PCd885qFW02G8_7TQQ3Sm2O93z973434D9EymMos7cvxABaLHJnHB5jyTVn6hOFTHuvh_tz2km5_H2JcSOY9FV-YmrxhFfgoR0LtKUDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردبیر پیشین نشریۀ خلیج‌تایمز: کشورهای منطقۀ خلیج فارس از ترس موشک‌ها و پهپادها، به تعامل با ایران روی آورده‌اند!
@Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/457182" target="_blank">📅 12:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457181">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JupuXNwozvWA-U_DrkQ4ByvfXspJbeYmH1RqPDM2JBcGTZvJOPXDtJKXA58Wa90sXp9fCQP956OlZrgaU2NMY6IVNOsiSm6F8cnHIzcsNPQoIexDXh7KZ7ijfTTEOwcS5-nWt0U4mlbRlouYZRPYAYqqqQbxW0oMVNaQrZAWrKtr5Yq9q2kxgc0_Sj_s7TQ0w-AonffJy0IeZBjTzvhSwpNuG_8UfTxWZDCc-tH4w8XggcIVbFpMGufx3eX92d2VKZPP8CfnAFlU8HkAK-vAQnYy4PA5mRwYJOE1fKvty3_wTPauSJZ6nQvzw3vKKW2KsH_xQGjAFvcWZGoegw0ZSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در راستای اجرای سیاست‌های کلان شستا و تاپیکو؛
💥
پنجمین محموله متانول فن‌آوران در رینگ بین‌الملل بورس انرژی فروخته شد
🔶
در راستای اجرای سیاست‌های کلان شستا و تاپیکو، پنجمین محموله متانول شرکت پتروشیمی فن‌آوران در رینگ بین‌الملل بورس انرژی با رقابت به فروش رسید.</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/457181" target="_blank">📅 12:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457180">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-text">⁨ ⁨
✨
شهرآسا؛ جایی که هر تراکنش، یک فرصت تازه می‌سازه…
اگر صاحب کسب‌وکار هستید، وقتش رسیده از تراکنش‌های روزانه‌تون بیشتر از همیشه بهره ببرید.
✨
با استفاده از خدمات آسان پرداخت و اتصال پایانه های فروشگاهی و یا درگاه های پرداخت اینترنتی به حساب بانک شهر، وارد دنیایی از مزایای ویژه «شهرآسا» شوید:
💳
تسهیلات ویژه با نرخ‌های متنوع و اقساط بلند مدت
🎁
جوایز نقدی، هدایای ارزشمند و تجهیزات جانبی ویژه اصناف
📈
امکان بهره‌مندی از تسهیلات برای پذیرندگان آسان‌پرداخت با میانگین یک‌ماهه و سایر پذیرندگان با میانگین سه‌ماهه تا ۷ برابر میانگین حساب و سقف ۱۰۰ میلیارد ریال تسهیلات
🏆
تقدیر از پذیرندگان برتر
✨
و هیجان‌انگیزتر از همه…
هر ماه با هر ۱۰ میلیون ریال تراکنش، یک امتیاز دریافت کنید و شانس خود را برای برنده شدن در قرعه‌کشی جوایز ارزشمند افزایش دهید.
💫
شهرآسا؛ فرصتی برای رشد کسب‌وکار، دریافت تسهیلات و کسب امتیاز، با هر تراکنش.</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/457180" target="_blank">📅 12:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457179">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/457179" target="_blank">📅 12:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457178">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krkFfkuLDpM2vfZtVuNBXPn2d-pm8Y-teJ-okxs23KKQI0mNrsDzq2mZzW9S1LIW7fiTnnonxlp6Ig1JTMVvFf-hBEg9j7qI7ljENncZRctkMxv_Xr0xfaCtr62qK9TJ0k9BEvj6fcXp2z_dEkdyYt4TBJVOITY6kZmSzlvvQlfxhR6SrKf4UoYOXtHQmE3DV8x-NJr-A4k_kErZUgpcU4ZmAWudyZKoi_NhBL2XPZGbR0J0-aUh4McZc_rs9o9CtpU5lJTZPZ30IEwcSBCyWFS_ht81t0yHqk2piWZqEY9d948kP5Xfp3ZPTGPLbkq_jis_XMvG8rlFvexlLd2hjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
اهدای دست‌نوشتۀ سردار موسوی به خانواده‌ای با ۱۱ شهید
🔹
دست‌نوشتۀ فرمانده نیروی هوافضای سپاه، به خانوادۀ اسدزاده بخشایش که ۱۱ نفر از اعضای آن در جنگ تحمیلی رمضان(۴۰ روزه) به شهادت رسیده‌اند، اهدا شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/457178" target="_blank">📅 11:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457171">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cgASHl-1huyjSODFd1ix1DQ971VPnIFIqGmaj2nDGjMLkyeRESGxHXxIn88scHnorMpWTDpGL9Xwt82OtY_92TompQEpsQS0EmJuEwq46ChonoyTHmNQfP0X171jD5GwFxBhSltipMey94FURQBkJ-GA4WfSa8VbmCGq58SzKtvF5ZtVFLUHFIg6rE2wIz7AXzmaOL-7w8EedKhrq7xoL3E3d3a-K1DoLzYXz7pw3jrADTTlyBdh6K1h0gcjQw5dSvVBrk8vcJCjwi9MpUrtmdb4QxuI-7ZBQbq2mVlPu8-xBFScBnprnxAdoobJek11JbwjzOHYmODF4JxyqW5uxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UXuFsxJkG0fXbZGg2I0vIq95lRDvjjtsK5PN6rLZf3ywKxSzaz2sbg7pLTFWDjkIMBXvlaIsW81C3AqPWMDKjff8Fh4_7uXuDKdkNz58kCBPwNGPd44B3G4911eSxVUduxblclv0YjDHuX_rqhXrFJ7I0bI5YMEdbAunuwCEu1ZDEt9ajm-hJfcKP50VqS3L6mwAjRzITTGMcBpEA6nDjR9ozQ7OJ6I1RmWJCSsoGpDgS0rWgC6ptrtfRprGm70HjYDQGSctKByW45APX5p12lembLjp1t9kFG4C1bKmN5CrWywBFnpwz5MOQSKjUpkcitmZFxhUmmKn0yqsIJ7D8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M38bEtqoxDGmOI9nqJt7p50QbETcX-vY_ZSbkXpWD6iPIdisRhemFPNz4QbjxyVYMAZjo6cubhGxFQ6dV9HF4p_WpNA4qQm8088aoPeJ9QYCl7HBv2fQkcNcyB1bvD9yPBOgptnZdO2axlHT1n2pWtpZjQiBh-zBSAM6jIApqsK11zr7SUPQqof8HsOUpC0MbcM7Q5mZq41b2h84ngpqX1HaLeKpKKSbT3H-aMl-YQERu--4ejn1PcHaJsGpR0N6HBT4GQnB2LcvRkLfCsQukZfdICmrA2s21lr21Pr2-2sdugPwDOgDzMQIeWRCLvgrX-0R0aqud-BBpAKRjiPgdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0qo29VqEz1poGbg8_bxuI7mnVn0PZ7uHUpuy4h-vPiMlOp4-xwTbtSKNusLKqw9ptvGgPTO5u-TyzLT4qPuNK_o-thnEENN46h2pRJPkjlmIAaLbC6aOY4FrEtpGAVqYyj9VKjjsrpT-ItZDHyLM1wX0Yy3NVdh7J2w2zRMb1XbTOjlhsIVBvsWKxFP4_QDkf85xv-MsHsYvZXzX34tRVuv21-A_WJEEYoArYUQDWpxuAmLHQgM2ZecmyRbC4fIklzR0iogdK7OCp0cfADINMWIM_UV8J2J_uyBOImGqQ6lHnRcspLWVpmFYMBYbYydLiTWbAbPT47gP0A68YCvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHDeMe4mHv6rL2hCiHAr28O3NUkx_2Fo6jAWXw4XNCFRkjxdCDoDOHTH4GmS5ICb-9sJ53u4CnbGTVpj5wnh002PgCQ_sejr1MGuGPNREfCX2stWg-sPHR-870_CdsHE6zTHi06Hpuba8c2xpoh4hNriZZBAyjE4RTH-IXGerZBG36g-jYs-DkHuAz8VttOI_81a4DJfo2E3YloZYRSK1zWdKGgZhhGVHl3kYAqDVtHRDCrKZQB9NiuS_X1LBX9jM86F3Zad0PGMTkSxjUS5yn4rvSuFa_arm78gJcWZhl-UdVMJNyLcO0q8N-UbVXLrSFuMD_AvG3JS3PI4g7bfWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dCZteIDMj4w-w5IRdCdI-wPzvnr1pOG1bSQhAEtneSw2sQgRD-ckSBoHXgsiaxSYZNHhndhcWq2OvnTga3KFnXW_errUxl1MSA1aRKUxwcI6lyOtvXaCJZjbr6bCWBau4C9jc9XTG2eSfH5vD8LBJwH1FMbaXOf-ioXmiS6fxf_VmmNoJJCb3fXbZ2MZuXK1-01V9EaSf8FwEWJGcM7VU5g-ViovEX_9rKBT-x2BYFa0xISo7Q1MxCIAm8nfha8w1bgSuhTBwt6SuWePeCY0yQjhCKzOcvWWjX-4l28SoEV24PHY24pJJwb6x-I6vMfzU0nk5bNKT2Dr60JjRmHmHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NfROrwGW3cLZjdYYkshjKdWhoP1f9QfBOrTrWOjtW5JVXM8MDSk4c3F4CJXcSTLht5fCwTeXeKCUWlnFzW6g30ICBp1l2MpDL3aq46wQ33DUTtmMHG8z0OVHFIE6lnK0XygNBuJncbCpRLW1jIxN6ll3TjmIoeALxgueYyiWZQnP3ujLSoWP3Qs_ICrmZMEVg5omF61qpEuHgm95mwe8fXTQ4rUPR3cRNDb6aEtddjuqg3d591D45o85h4lD63URsUiXLGGHmAo_Rbm5rQrnwYSg0RzNRIgrzhaz0fXLcQG8WvElmhvQB3dTbMiTGz1ueCinS5STdQJGu5Bj0eLPOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
وزیر علوم: بزرگ‌سال‌ترین داوطلب کنکور ۸۵ سال و جوان‌ترین‌ ۱۲ سال سن دارند.  @Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/457171" target="_blank">📅 11:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457170">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار تهران - خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f312278eb.mp4?token=ON77ZD9kevPwl7Ie3TktU2X79kAVKHSiuLwJLHkuRYbKltETIW88u2fj0o47QU79BKYWf5AxyopKbojsw9QuEVuKKOGUKsIvMFBMYxH3Y5L__vq7ifTfLEmQbjUsLjslgwtXnT0yiho3SWMlCfufyPlKHa99-b8Q_QW4QHAHTca0-Tsw5cE7Q2ZAfZCQ8XcSi95iPkhpqq6777vROwhaMcQkJHonhZGFQMgRwvOjfW8fRA-4mfuNOpZLVLMbC4Cb0BKU5fWQamhMNcDkQGh9o1tYZYtxdmlws_u3PblSPwgh6OVYYlRRgKL74N6kFQLdFOERBq9BJR3YILHtGQhbqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f312278eb.mp4?token=ON77ZD9kevPwl7Ie3TktU2X79kAVKHSiuLwJLHkuRYbKltETIW88u2fj0o47QU79BKYWf5AxyopKbojsw9QuEVuKKOGUKsIvMFBMYxH3Y5L__vq7ifTfLEmQbjUsLjslgwtXnT0yiho3SWMlCfufyPlKHa99-b8Q_QW4QHAHTca0-Tsw5cE7Q2ZAfZCQ8XcSi95iPkhpqq6777vROwhaMcQkJHonhZGFQMgRwvOjfW8fRA-4mfuNOpZLVLMbC4Cb0BKU5fWQamhMNcDkQGh9o1tYZYtxdmlws_u3PblSPwgh6OVYYlRRgKL74N6kFQLdFOERBq9BJR3YILHtGQhbqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای دود حوالی پالایشگاه تهران چه بود؟
🔹
روابط عمومی پالایشگاه نفت تهران: دو تانکر حمل و بارگیری فرآورده‌های نفتی صبح امروز در محوطه بارگیری پالایشگاه نفت تهران دچار حریق شدند که با حضور نیروهای آتش‌نشانی، آتش‌سوزی به‌طور کامل مهار شد.
🔹
تانکرهای حادثه‌دیده مربوط به حمل نفت سفید بودند و حریق در محل بارگیری رخ داده است. نیروهای آتش‌نشانی در محل حضور یافته و عملیات اطفای حریق را به‌طور کامل انجام دادند.
🔹
در این حادثه، واحدهای عملیاتی پالایشگاه نفت تهران آسیبی ندیده‌اند و فعالیت این واحدها بدون مشکل ادامه دارد. همچنین این حریق خللی در روند تولید پالایشگاه ایجاد نکرده است.
@TehranFarsnews
-
Link</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/457170" target="_blank">📅 11:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457169">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbmlP3pU_GDTs8Al-Ak7H1oT24IcnHgNoOdh1Q6xClIqCoowVnair4fJPpAgMHcLlhYVtx8DsBoRrjtn71UQL64FVivcL0gFJS4fFhku7xmWyJ8bfVIbWhXgHAgb_OxqPvfAl_vBRLanq8OP5bpbmlNc66G4gMlK-14e7KNImSrNSCBvOE5YOZZJB4mR9D7S7XRdJ3m1PrynrgqB5AQu6SXISSZgA9jopXR8CJ85VvBauLvK3eos4U8OW_1TZfZ3GfObyXGl00el0NNf5o1tJp0et4uSqeYgagB0Dr-YogrSG0eU5FBDsQc2A_o0sjpJ6HQgZO0CYeyYShWpKTg4OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی خطاب به مقامات آمریکایی: اصرار بر ادامهٔ سیاست‌های شکست‌خورده، تنها شکست‌های بیشتری به بار خواهد آورد
🔹
تهدید به «شروع عملیات اقتصادی» علیه ایران، در واقع برای انحراف افکار عمومی آمریکا از بحران‌های مالی داخلی است: یعنی بدهی‌های بی‌سابقه و افزایش…</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/457169" target="_blank">📅 11:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457168">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsM-QQeHDMFbHWFhIGdQnb6FBKp2rbNbaWoaLdn1aspwRydDbgzFRCt984B1OlCAQwuJ9u1SDNcTSAqQ5C-UZcLC90Qz-yDEIC-O8R5BSU8ch-_TNbt62Y2CKYHY7HjlpAUE8q6SSnYr-Mds88_VLkN1Yat02AAH4viRAxG5hjdbOLZokOHhnk9Gyel8hLCVbD1tD_G7m3GAT4IAbs8BJ0Y9PKzLEEb-f_uNji2BdvHDF2B1gnnEe496x6c_OGtmdm7jdr-ptL7zV4gk1JnHEmjckZSEVsP0upx2p_EbCByUd4k2XcxDLUOiei9NU4HjsGW7lDYyUEVPAdyiMToBYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترس از ایران، بازی اسرائیل در عربستان را لغو
کرد
🔹
«جام ملت‌های ورزش‌های الکترونیکی به‌دلیل ناامنی در منطقه به‌تعویق افتاد»؛ این بیانیۀ سازمان Esports Foundation از لغو مسابقات به میزبانی عربستان است.
🔹
اسرائیل در این مسابقات برای اولین‌بار در تاریخ می‌خواست یک تیم ورزشی را به ریاض عازم کند.
🔹
سایت Al-Monitor صراحتاً جنگ ایران را عامل ضربه به پروژۀ بازی‌های الکترونیکی عربستان دانست و تعویق ENC را در همین چارچوب تحلیل کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/457168" target="_blank">📅 11:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457167">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf1830b1bd.mp4?token=SKMLxpgIEWD_JcUBqPHfWrT8tNRlN8VgWqfzed3M85CbyZ8wiV_sflq4A9yP-k8MAP_PEVtBfgruHGMqj14Qqekpy9TRu7EQqdv2XVk4mQA51B4qwu6pEBv2AtmZp3_eMjRGCtXBxHsFDO-EAqu-zi7O8D_ErmOwJ27018tGWoFf_7Zn2V7yahAxRoyAlJxkCoM71UoUiRkwynh6wej8nBd0cgs5S_FclghVKLktg83h9NeouHBttNlAJXj_NpCz3D85J1_TNKILoYneVTcxjnYeOfNMrAxOLJJdWGsq3pQTe2Iko_LkDTDvvrk_xDQKwaazD5_BGg85aIoYU_hi5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf1830b1bd.mp4?token=SKMLxpgIEWD_JcUBqPHfWrT8tNRlN8VgWqfzed3M85CbyZ8wiV_sflq4A9yP-k8MAP_PEVtBfgruHGMqj14Qqekpy9TRu7EQqdv2XVk4mQA51B4qwu6pEBv2AtmZp3_eMjRGCtXBxHsFDO-EAqu-zi7O8D_ErmOwJ27018tGWoFf_7Zn2V7yahAxRoyAlJxkCoM71UoUiRkwynh6wej8nBd0cgs5S_FclghVKLktg83h9NeouHBttNlAJXj_NpCz3D85J1_TNKILoYneVTcxjnYeOfNMrAxOLJJdWGsq3pQTe2Iko_LkDTDvvrk_xDQKwaazD5_BGg85aIoYU_hi5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، کارشناس حوزهٔ مقاومت: اهمیت اصلی علی‌الطاهر لبنان، علاوه‌بر موقعیت جغرافیایی، به تأسیسات استراتژیک آن برمی‌گردد
🔹
در میدان نظامی درگیری‌ها لحظه‌ای ادامه دارد و حزب‌الله همچنان با تمام توان درحال مقابله با دشمن صهیونیستی است.
@Farsna</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/457167" target="_blank">📅 10:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457166">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار گلستان - خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o26xtEgv8007l0llC8LIAsHQxUfqCnM4ZLzMS5ug9G2VMVgmNAeOz17WXhD7YxriVSd6-IaoNgqBB6KV3Uh8akM_H0orllxt4hBK8iTk37a8E75m-TPg5AbLUqlqMLAM1R6G-OD4em4W5w-re1K-BkAo-Z_EInb1bVBupRIvICVO3clUuMMes-vQtvnXNiTgUM0UB6MUXfW0TwjJ7mdzjz8pGw8YZGEUJ6VUoq9A76o-hcFBDamMS3Mv7RNevmT6Uv4pSCjY03cMAgNKo5_1VucU7E-I9GicFmZuhRU5S1XTEZMu8U38cHVIyWx30APJGtrjYSsAgsN2mrHBdtoNsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رمضان مشت آمریکا را در حوزه نظامی باز کرد
🔹
سردار حسینی، فرمانده سپاه نینوا استان گلستان: آنچه این جنگ آشکار کرد، این بود که ادعاهای آمریکا درباره قدرت نظامی خود دیگر مانند گذشته نیست و آنچه باید از قدرت نظامی این کشور می‌دیدیم، در منطقه عیان شد.
🔹
آمریکایی‌ها در برابر مقاومت ملت‌ها و گروه‌های مقاومت نتوانستند به اهداف خود دست پیدا کنند و امروز تلاش می‌کنند از باتلاقی که خود ساخته‌اند خارج شوند.
🔹
آمریکایی‌ها همواره می‌گفتند گزینه‌های مختلف روی میز است و یکی از این گزینه‌ها نیز گزینه نظامی بود، اما امروز دیگر مشت آمریکا در حوزه نظامی باز شده و قدرت واقعی آن برای جهانیان عیان شده است.
🔹
این قدرت نظامی در برابر گروه‌های مقاومت نیز نتوانست دوام بیاورد و ادعاهای مطرح‌شده درباره توانمندی آمریکا با واقعیت میدان فاصله دارد.
@Golestan_Fars</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/457166" target="_blank">📅 10:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457165">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g62eOgKOa5B2yYaocBLWBUb7ntzvu2mxeAEyYXiKYUw7qBDEdDO89GjnS9vtHgZAOBbEDpp4cu42AuZZQhenkVw_h8BpoA6DJzumiHxloiTM0FCI1qvgtAl6RxYYW1yIAf65lAm3MQt8JqfhWw_0OIeSKYrLtgTxgN4ZaOwHA3VXvmpBXyhmv0VMvLlCfn6CeDO7LF7GoNKuVnYjQd0q1xCqsr-7Mg2hV0uSM1RBL4KVspo3cpsTTwlbRvWsfcQ84khg0fhtM0Ed2zz4o1XL1p3h0r6RYClYwZ0Ou6SKHQMGHz1eSUoOarD_x-1C5UXi0FOMpjgoVT1VwENoALiiwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: با وقوع جنگ جدید، تسلیحات مخرب‌تری به‌کار می‌گیریم
🔹
سردار محبی: قدرت تخریب سر‌های جنگی به‌کاررفته در موشک‌های سپاه بسیار فراتر از نمونه‌های استفاده‌شده در جنگ‌های پیشین است و اگر جنگی آغاز شود، تسلیحات ما در تمامی ابعاد با گذشته کاملاً متفاوت خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/457165" target="_blank">📅 10:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457164">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee294b7936.mp4?token=moTlOlcJ0r9FQhtf8pWH-h31wWNI1AY1ANgc9sB1_rJXDuwVx9-h3f2BT-Dvvyf1LxLhWtwK5PXMW6P_m5wb_m5VzwGF1c_aXMlQC4X-8Smqle1v2oeB8Xc1YvkyBV9k-Vyo5L1RinTNpHCJW8h3AD2Z2UjBz4niI2SURMfUJezHAgerUma1lFboPkhT8jjuFHfmpNyx0D3qkt1y_6eMo0uLLp49mY3-Vuy-JB60yS2W5MuEco0xJjHFHjM19XUYsaGsXzU_gACSbNWRim28Vopp5SJp4NQMVNH4xnSS_Tou7ZprV1tys175EFXzwQImfCAPTq_MrvvyKEU-eMPWGoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee294b7936.mp4?token=moTlOlcJ0r9FQhtf8pWH-h31wWNI1AY1ANgc9sB1_rJXDuwVx9-h3f2BT-Dvvyf1LxLhWtwK5PXMW6P_m5wb_m5VzwGF1c_aXMlQC4X-8Smqle1v2oeB8Xc1YvkyBV9k-Vyo5L1RinTNpHCJW8h3AD2Z2UjBz4niI2SURMfUJezHAgerUma1lFboPkhT8jjuFHfmpNyx0D3qkt1y_6eMo0uLLp49mY3-Vuy-JB60yS2W5MuEco0xJjHFHjM19XUYsaGsXzU_gACSbNWRim28Vopp5SJp4NQMVNH4xnSS_Tou7ZprV1tys175EFXzwQImfCAPTq_MrvvyKEU-eMPWGoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجدید بیعت با آرمان‌های رهبر شهید و طنین صدای مرگ بر آمریکای زائران در رواق دارالذکر
@Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/457164" target="_blank">📅 10:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457163">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwu3rUhepzaqSVmr6XmyIhiJMn8ir5ujarTn4XglMO12kI68SduAqdX7J9r-8H6uVjp5_7AEcP5cGbtIjY7x3_JzPw5zRxW7O5rhZ13Pk77CUfsJxQOJNL6rJ54QSOvamlqced4XYK9wXG8XlGqpffRCjF685OfRS36zAJbvUnciuKVflPjjxrbA9QQVynDHqLFkAWq6DCSPwin5q_jsNKKaUeotZV5afqM9y6B7vHwklmGFa3nudrTU6RodXSXrLPcWc6Nwl7BMmKD-V1uI-TKimxt5vhhOQALjYr3ej1ICfKJcKV-GqAY8-75lRBVoHtdJ-xxx4QvjEgjgU275wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
وزیر علوم: در کنکور امسال کارت ورود به جلسۀ ۴ نفر از داوطلبان صادر شده بود که در جنگ اخیر به شهادت رسیده‌اند  @Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/457163" target="_blank">📅 10:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457162">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/134c5c9f7f.mp4?token=u6tmaQmKMIrZJtMiDoTsKmCR6BTXpOrwb8eW523qTyFzAsIjConakTlGHB_tXc7acSaeeBX563C2P_cjboBFBdd7DUPBtNF3KDAmDhn3dsIQA8Dqhgdacw6FaBKFvz3X7FHJ1U_rt97YOQf1rdshWDicnvYfUPtNQp-H0dYSTwfdTfQ8dSaoZ_I7Mz5U_wT1fSmiuPXXuC6laywfXIY031d1rkh3VF7Asoa_E0QUZYB_uf5d1Hvr5w-NTzptti-WXq9epeVn2vgqtkTFjHYFc5s37o4DsThN-_TJE_5qZy9kat83RFsrYwL8ODt7aYh4cUpZZWfApybEbd-LwOja_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/134c5c9f7f.mp4?token=u6tmaQmKMIrZJtMiDoTsKmCR6BTXpOrwb8eW523qTyFzAsIjConakTlGHB_tXc7acSaeeBX563C2P_cjboBFBdd7DUPBtNF3KDAmDhn3dsIQA8Dqhgdacw6FaBKFvz3X7FHJ1U_rt97YOQf1rdshWDicnvYfUPtNQp-H0dYSTwfdTfQ8dSaoZ_I7Mz5U_wT1fSmiuPXXuC6laywfXIY031d1rkh3VF7Asoa_E0QUZYB_uf5d1Hvr5w-NTzptti-WXq9epeVn2vgqtkTFjHYFc5s37o4DsThN-_TJE_5qZy9kat83RFsrYwL8ODt7aYh4cUpZZWfApybEbd-LwOja_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو اتاق مشترک بازرگانی ایران و روسیه: توسعۀ همکاری با روس‌اتم، می‌تواند ایران را از خریدار فناوری به سازندۀ نیروگاه هسته‌ای تبدیل کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/457162" target="_blank">📅 10:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457161">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار استان یزد</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/860a438708.mp4?token=L7T3s-0NGoRXtIPxpXCptjnLG40NnyhXH7uQOFiWpcsWWdTVdVfDaCioap1VfrikjcI52_Egj-oaAWvsjIICt-SBBBVRqQAyMuhzuTM8YwztPbVFhhHVs3fYPiGLyHeTQsKigx583dTnW2ObF-pnyjkFeMj6ZmO1B7DjL7VQrgCWhdO3q8SxSLPWXwei-tG6Tb4UKHwKKE9-JqiDNO-UVX8w77tMfr-z8yHitVTNd9-XxTyDj81CyIBHODVuZzwXxRVphwMbEJH9RQfZhJFCga3o_9xJThKTVeFoBQW1yiT2l3MYER3irI9PFBJXypK88jNxLzNacCx6HKaHeAetqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/860a438708.mp4?token=L7T3s-0NGoRXtIPxpXCptjnLG40NnyhXH7uQOFiWpcsWWdTVdVfDaCioap1VfrikjcI52_Egj-oaAWvsjIICt-SBBBVRqQAyMuhzuTM8YwztPbVFhhHVs3fYPiGLyHeTQsKigx583dTnW2ObF-pnyjkFeMj6ZmO1B7DjL7VQrgCWhdO3q8SxSLPWXwei-tG6Tb4UKHwKKE9-JqiDNO-UVX8w77tMfr-z8yHitVTNd9-XxTyDj81CyIBHODVuZzwXxRVphwMbEJH9RQfZhJFCga3o_9xJThKTVeFoBQW1yiT2l3MYER3irI9PFBJXypK88jNxLzNacCx6HKaHeAetqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرغ آتش میهمان یزدی‌ها شد
🔹
فلامینگو [مرغ آتش] یکی از پرندگان شاخص تالابی و جلوه‌ای زیبا از تنوع زیستی ایران است که حضور آن در زیستگاه‌های آبی یزد، اهمیت این مناطق را برای حفاظت از پرندگان مهاجر نشان می‌دهد.
@YazdFars
-
Link</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/457161" target="_blank">📅 09:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457160">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCjz96y3gjtwB7b4_2FE9nxE27msZwqRFTO3npeFAERFFoVNUeOWBA59E3XC8vFvWjsazwJ_uNrRhbwNj6FqfLiIVkWOsRjHyDyWsnpb8V8f3L-f75KhSzzJOrlBDz9wOx4zYKIEumen5QIZqRwiZ-vRaouhInpl5O3ckFWLd-QulW4kzULep3L-ChbtY2P3vBy1ML45JNJ98H-fWaVQjco8AYs3ScyJ8pBy7H9cEUzD56_V8NZ9ns7KgZgv_zYA7weSiXyObLS1S9OaH9qWsPo0kugO_XfequfOk7QlPsYOjXehNSLb5emC3Nm8AQOxZ9RA6nr2j6webbF7q4yHSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعاهای تکراری رئیس‌جمهور متوهم آمریکا؛ ترامپ مدعی آغاز جنگ اقتصادی علیه ایران شد
🔹
رئیس‌جمهور آمریکا ادعا کرد واشنگتن «خردکننده‌ترین عملیات اقتصادی تاریخ» را علیه ایران آغاز کرده است.
🔹
ترامپ با تکرار ادعاهای همیشگی خود، مدعی شد نیروی دریایی و هوایی ایران…</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/457160" target="_blank">📅 09:38 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457159">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnp1byYvlvDuVhu6SHUCPhmWcukUxlOc6e0ZRclCniwpm5KuAKjldr6BrBCiGX-Q8GiWm5qVJ7WbNLoEqqi5Ok-Ac47lLaYB7BooM3aCT-IeOWBDZppWzwkwnfai6j6kO0ZA1U99nhb8ani6-OrXmdp-_b3BMsFGV44ziFQhtoGb0BFpx03rQranoKXPxUbp54OPKabvs1QrXMbaFATvTIlVB1nb4Nvb5dJaZHMDKPepswlmLqK4SHKDMmIOF7k1SPOadmYEVWwOGmNirdggtnNLg4U97NRdUTQGYuAbnu7sOQs_-tHbt_3c7HltYZrmA429P77aNONUcnCj0yW-_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
اعدامیان میدان علیخانی اصفهان از جنایت‌هایشان گفتند  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/457159" target="_blank">📅 09:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457158">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da020506f1.mp4?token=PPQbvLcFuJq_icTRpV-sS17unPNtIuP1ykkhBFhs2sPp-J--FtKu-Y5BUn3FeshqbQrYFGMwMUhs37LwdtlYcG5WzFPqIeXZpcSKqSFb3h-2Fs-3mGx3GVyQ_bK2onsFLlBM7pZ09zie64hzK3EVX66w7FBm7srhMI_T1r3R_evT1j_ev1oBd2Se6j3jMP3xu2wrUcqcv5CE1CoI7RRQbktJu_qxq3scE4-LT4eQfXOpYAp0E0IhgAf6MCeuHvMetVLk1qF6_XC2Yv0wsDJqT0UgaBvXrWJPNiIusQQNXlCem34EfAvoQR4ZQtQ4OrvVrIvf43hPljMyZB-QcH4_ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da020506f1.mp4?token=PPQbvLcFuJq_icTRpV-sS17unPNtIuP1ykkhBFhs2sPp-J--FtKu-Y5BUn3FeshqbQrYFGMwMUhs37LwdtlYcG5WzFPqIeXZpcSKqSFb3h-2Fs-3mGx3GVyQ_bK2onsFLlBM7pZ09zie64hzK3EVX66w7FBm7srhMI_T1r3R_evT1j_ev1oBd2Se6j3jMP3xu2wrUcqcv5CE1CoI7RRQbktJu_qxq3scE4-LT4eQfXOpYAp0E0IhgAf6MCeuHvMetVLk1qF6_XC2Yv0wsDJqT0UgaBvXrWJPNiIusQQNXlCem34EfAvoQR4ZQtQ4OrvVrIvf43hPljMyZB-QcH4_ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر علوم: در کنکور امسال کارت ورود به جلسۀ ۴ نفر از داوطلبان صادر شده بود که در جنگ اخیر به شهادت رسیده‌اند  @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/457158" target="_blank">📅 09:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457157">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc67442d1e.mp4?token=MBcpxnJvVGHCQsgLeLmLCpSgaAknsmKmgkBekCVNp4KC2CvD5a8hNBH_cZ94u3ZABvN-HvYy8Xh7m6fi32TRpvDLnzMmWlXeVABbhlgZV8z5rTRGDWhaniUcSb6hZplUk6UxWLa-PBDWnpfqI-6Abr5Dw03g50sHUQHOJH9oNBtr2xVrRmpcvU-E-lO62vn8QqEfzzYgDLqMsQljlQFyHr5_E1fLZXvAOxlDhLqqy06fNHjAcpYz4FZflLqV-Zr--ECgsncylD1mHUqNW7PzShxoqYQXVGmuxDdymnQXy9q3-qFQNh-XVB15YEN_vnDm6XKOIVwfXsv0H8AMVSEvzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc67442d1e.mp4?token=MBcpxnJvVGHCQsgLeLmLCpSgaAknsmKmgkBekCVNp4KC2CvD5a8hNBH_cZ94u3ZABvN-HvYy8Xh7m6fi32TRpvDLnzMmWlXeVABbhlgZV8z5rTRGDWhaniUcSb6hZplUk6UxWLa-PBDWnpfqI-6Abr5Dw03g50sHUQHOJH9oNBtr2xVrRmpcvU-E-lO62vn8QqEfzzYgDLqMsQljlQFyHr5_E1fLZXvAOxlDhLqqy06fNHjAcpYz4FZflLqV-Zr--ECgsncylD1mHUqNW7PzShxoqYQXVGmuxDdymnQXy9q3-qFQNh-XVB15YEN_vnDm6XKOIVwfXsv0H8AMVSEvzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران در شمال کشور
🔹
هواشناسی: در ۳ روز آینده دما در شمال و شرق کشور ۵ درجه کاهش می‌یابد.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/457157" target="_blank">📅 08:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457156">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqLtkRJrOOg-nIB5Kp4X5sCYQXkS2mCvZOQXJD11vZr85UULCc1y36wl33BNz3R9Tyr7w8II12pO1Riy8p3ULrEBK1fSRzTbqO2FbDolU7p6X_DU2cZlKwvV9BUX7nCBoU4hYe-MIBU7cVZJ-FtElzQ9mwJlDyyVHufEzLJsnJ41YgdOCG01Mn6UD8_LBGmskPgXAUuD_ZY6sYNuBrMqZia_WQjhcrAQx6natSVoHZX4vEtLld38YWXbxlck6VmeAG2LzQmzAsKX3dBdP2Om4JG4kxt9KGK4MGL9ex9C8fQWP1W94w3uSLqmDzNSYS5TXHVo8wKNj2EikWTpPyBMJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
وزیر علوم: در کنکور امسال کارت ورود به جلسۀ ۴ نفر از داوطلبان صادر شده بود که در جنگ اخیر به شهادت رسیده‌اند  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/457156" target="_blank">📅 08:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457155">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f66cdb8a28.mp4?token=KCmQgvpTVVTjzLjqWL7wBDtZy1Rm-p9lRgziOWmMrnidNgBQS61GyGDb0WiPMORaGA1IwXkA7pkE_ZJawQAM2BNAVrbIHeM82U2Btd390OaQf3td_o-rwNGdQA-Vkq0n6uyE-LKz_XLZIc1uShZ5Jg--4MK52o5YYX158iEFJw44plTeRVuHdwdCS9Z2vVADoBjmMN7Da3xKM3EjgW72aoT5KyjzONdpLKmZzU2GoLA20NOahiBpJpv5OKUc9wbwTZkY7WS6jvTMRgykcwwuefSgzwh61h0e7j_mr0B7OfykkVQAiRODOj0XgxOhjYJgcofBRGydLflmZ0F75R1v9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f66cdb8a28.mp4?token=KCmQgvpTVVTjzLjqWL7wBDtZy1Rm-p9lRgziOWmMrnidNgBQS61GyGDb0WiPMORaGA1IwXkA7pkE_ZJawQAM2BNAVrbIHeM82U2Btd390OaQf3td_o-rwNGdQA-Vkq0n6uyE-LKz_XLZIc1uShZ5Jg--4MK52o5YYX158iEFJw44plTeRVuHdwdCS9Z2vVADoBjmMN7Da3xKM3EjgW72aoT5KyjzONdpLKmZzU2GoLA20NOahiBpJpv5OKUc9wbwTZkY7WS6jvTMRgykcwwuefSgzwh61h0e7j_mr0B7OfykkVQAiRODOj0XgxOhjYJgcofBRGydLflmZ0F75R1v9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ آغاز کنکور ۱۴۰۵
🔹
آزمون تجربی صبح امروز، هنر و زبان‌های خارجی بعدازظهر امروز و ریاضی، فنی و انسانی صبح فردا برگزار می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/457155" target="_blank">📅 08:18 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457154">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🎥
رئیس سنجش: نتایج اولیۀ کنکور شهریور و نهایی نیمۀ دوم آبان اعلام می‌شود.   @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/457154" target="_blank">📅 07:59 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457153">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دریای مازندران تا شنبه تعطیل شد
🔹
مدیریت بحران استان مازندران با پیش‌بینی وزش‌باد و مواج شدن دریا، شنا و تمامی فعالیت‌های تفریحی، صیادی و قایقرانی را از عصر پنج‌شنبه امروز تا صبح شنبه ۳۱ مردادماه ممنوع اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/457153" target="_blank">📅 07:30 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457147">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tWe5RPVQdL9Gsek9mC7Er8_xS0NKiPPifXQahsfcJ4pXyUqniJNsyc8bVGJ_8pq89jHNZaIJEft929SeLUf_epn6Mp2l6CoCOBVf3qENYKlmVKxbJi_Zel8UE_9ZU0UMHaarf2tKAF4Kn7gMB5wV8yaF5xMCMXtIOr4-IAXZBBHpFH1e3pKC58eowCn90WpeT43RbebQzMgJ1u3o5tnxJCLuxGwpQ0jLxx8jeTzIgGww9DmWa3hwR-7bRsjsoyfO1jeZQgAGiMOync1Yn--7lI4YgozqiyI8grsKH1awFCcSDt-INFKzoGzr6v4quThAXJDruz-fedPrL9a8DhIulQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DZRjGHliU3NFuhJdS5-fEfLezMqGbv-7R32a8mulBRbpfsZwmc-oR612Rf2j1d9KvALvZs9lqWLsi_bqQPHd643RrFO6EWLCsIRedvWa6YT_k7m1my2jDb8uxvdvyOrloT6yl21e4Lhga8Cve9_Xw2oymyK0HlE9OlH3CVEAWpklSRvMk-X7SLouBwdZwUPYQPWPYzdTK1G82qCA1mWUjvEOGDBoqOm48dIL7ko9HlWSspGrUHpSjIFJhbTJxmM9k2SHCMFLZ-cRjOMLyOfIL4pzTbc4HuzrFXECy8ciy1HePu-6Hyz_0qpqyGGJg4SZ-S7Bg9QODKoqmlzrXns47A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_gpDsLEhwAl6-vyrCOjYWg7boZkTLqpfbGa5ZpcQ3xheeySc5G37NBrQyYjcRoVeu9vVALYwkjwfruBPfl5Is_sUxgcsnEGRrohPKIg-bbhwVXgfFBVgmM8SRHZ2bUeCuTdK56o1QWxmKvsGfBOjKbPCidCGIiZbb4z0Ny5fwfixI9o2ulJghfE8BvNaDbvGIh-1gXSlGbdWB7yFswemkbOv4CWt7pwJFoW67i4Ski_6yLiE4W-f3zuDoPaK50572jrsMW9uYGF8YtJvSLvM-i2_22nYThkjFzwIlkdnbFNUO2TP9i1M7VmdXWeY8wWuWhGcLg4OokFK_nQrlFxkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X2-x5_kUWqqlV631sruH_KxIdcdNwqZP18ZBUKWZMUUjktkbxk27FRdPOTOj8lvHbqkV4houUG5QvaCkzeRtACMZMg5GTOjzaIZtIHCf-Sp8s-SYSmKNehN1hozNXHhaNaYrWggt2tnEU7EWhHGshjMflr-mMDqw2tf8XwTp07_GTwW4BkmRX0Xywc_PY8tVNzBXN025Nlfz4jNO-D5u-HLPJrhshmJJMUMt95uljQn9OXSURFp-ANj2fxo1FLj4FMQkPNEjQgXAoeD8y0iuwX9iml3TjMm1OQz5Y5YDyQbedFB906YPCBPKBUz6fxN2nBDrEM3Vk1KqPn7jO5BWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3SxvzhTGJZ_dlO8J3ZOVro0J8-IPpT7E5ED1BgFKw7PMQmJKu6ff2_O153AFd9EGQSat57gHr8G2rO9ZfqsVY7b8fc7n3MTJPt0t9mZqNDfAk--qLhiCg7N36DjfMxSv6PA4KUhqyz3TsaoxSEGizyt4kikyeXHtpbBU_U8UkCcqV5QvXRPkW_S0fhqyr43i3eEsdft_ZpfaoDUWB5KEN8WiO6xIsk-yTl6fBX99lvbK_Y6Mi81X121xwGdWcVYSUGv3xUQCiCwD8zsm6Y9rRCG_0ppzKe_ASZzpeKDHxJ19pCWwbiD5ZM4m6ZJTZKcpg_KQ1cgT_bzIdtMbkyAHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UbXnH0Oc0WYrMpun-OfGC413ga6LeXIvMTqHadWWFRwtPk0M7nq3o4YDsVQW4gOLGuQNPC9vMwefGJo1imWPhR18HNDtrlU8QYVpcNWxDTcQcQOV48LILxuoLO45uv_rzNUhbrAjNvohNOr08UUEwLtvWxSsWiBGojkrYNM9_iygxiXxq2G2_u-2nGeq7GnRDUdY_9Z6QiD0PZfutYuPaX6TnOpxsGolTpeq0GWouvqH1zsY1A1eOoy_g2nhM5aEuElM7L8fmATlGB0UYIUE8jaH_CSy0sAifAuD9XKG8VQnko5OfCRtyBcH-ycYNzEMUnDdzzgKLG7b9cPdAsXXsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حال‌وهوای بازار سنتی تجریش
عکاس:
فاطمه جاوید
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/457147" target="_blank">📅 05:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457146">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/035dc36b79.mp4?token=Ctkq3TYukVMpgJjdv1ozOynrH51RwN9bgz8PC_0HllnM3XGE212v3whw-dIQknzYtV1AxiDl9ASihKLHfBmBS-VIyS7C9EhQl2D1HB-cmB38EY-GGDI3mOT-wLbkd_66xKDa8ghiluTEXBADccQRSaEga9qqtxo6hRko4UlcqixBNLLikHrp6OcQZjI_X5KjnDk_bvukSlWMi5k197MqbxrPqN05Ps7GZUQwOqWVs4bIeMEkkyI3HV0_nBiGcKsc2_biXa8SIrrV15R6a3UNnQj4TtCDZgWtQWZHf7jMHq8BfNPJ1MdophpZCyJP04GybXcTvtZLYP7n7zKGMr4lQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/035dc36b79.mp4?token=Ctkq3TYukVMpgJjdv1ozOynrH51RwN9bgz8PC_0HllnM3XGE212v3whw-dIQknzYtV1AxiDl9ASihKLHfBmBS-VIyS7C9EhQl2D1HB-cmB38EY-GGDI3mOT-wLbkd_66xKDa8ghiluTEXBADccQRSaEga9qqtxo6hRko4UlcqixBNLLikHrp6OcQZjI_X5KjnDk_bvukSlWMi5k197MqbxrPqN05Ps7GZUQwOqWVs4bIeMEkkyI3HV0_nBiGcKsc2_biXa8SIrrV15R6a3UNnQj4TtCDZgWtQWZHf7jMHq8BfNPJ1MdophpZCyJP04GybXcTvtZLYP7n7zKGMr4lQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیرالمومنین(ع): روزی شما ضمانت شده و شما مأمور عمل به احکام هستید
🔹
مبادا خواستن چیزی که ضمانت شده برایتان برتر از عملی باشد که انجام آن بر شما واجب است!
#اندرز_مولا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/457146" target="_blank">📅 05:18 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457144">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65aef8733d.mp4?token=gYao5GPbDaUuqDdFvSztG51DObcZessBZBk6PxsmeZ5I9TsxF1dEbFd_aGSKDPCfguiYPgDAwTh7x0C_kR3CZoT1h2k58b0q0U_03Za-nPh8aZkksXHXW4s-pxBpaKhOun4fimgqFVxSmaS2AWvXweTNXH29_ila_Jhhvi5YQheTPnaMLSYJkkt4Bu-SKw_aPZ2GqWTygfXNn1HXKkQ_0A7mTyBdG_mRWCoqiUJdDG9VM7eU1_yDP5WB7fR3t2YlyzAay2XotIy3JSq-Nv9thswSudspBt3hYun46huFRvJmu3XEru-AGET6nyeEjkc2BmRcJx11LoX21cjaP-Gs7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65aef8733d.mp4?token=gYao5GPbDaUuqDdFvSztG51DObcZessBZBk6PxsmeZ5I9TsxF1dEbFd_aGSKDPCfguiYPgDAwTh7x0C_kR3CZoT1h2k58b0q0U_03Za-nPh8aZkksXHXW4s-pxBpaKhOun4fimgqFVxSmaS2AWvXweTNXH29_ila_Jhhvi5YQheTPnaMLSYJkkt4Bu-SKw_aPZ2GqWTygfXNn1HXKkQ_0A7mTyBdG_mRWCoqiUJdDG9VM7eU1_yDP5WB7fR3t2YlyzAay2XotIy3JSq-Nv9thswSudspBt3hYun46huFRvJmu3XEru-AGET6nyeEjkc2BmRcJx11LoX21cjaP-Gs7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موشک چینی بعد از پرتاب دوباره روی زمین نشست
🔹
چین با موفقیت مرحلۀ اول موشک قابل‌استفاده مجدد «ژوچو-۳» را پس از پرتاب روی زمین فرود آورد؛ دستاوردی که می‌تواند رقابت این کشور با فناوری موشک‌های قابل‌بازیابی و کاهش هزینه‌های پرتاب‌های فضایی را وارد مرحله تازه‌ای کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/457144" target="_blank">📅 04:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457143">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSTQt232J1zHGuOh6bQaJiel1RU6j8CP36fHG9_exulHFI6d1T9dk0cF5Dks9TN5HJfRgXeQg0pJD7xIlOj4Uh6IRyhTexuWTifHQ12YxBjo6Yqis6c7B7vQ-6hscdbbCaJnXHuDYWlHxqk6R9-USzQ4Zts-t_z555IFMOE_LlFFF8rp_6MBq2tzWyEA3NDNR3ihQJgji-1_m10ac09jX-PDKmjg-IImQd-ey_eyHFAwCwoyf-lzyaEFRZOWe0yH2sHv9nswlULTewK0LP-7fA-OTlvnyNURJOMvPBGywDTO2IlWKrqcyoaJI3vrblfTZFeTYIVNAvapVw_2rt4Psw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراض نمایشی انگلیس به شروع پروژۀ جدید شهرک‌سازی صهیونیست‌ها
🔹
وزارت خارجۀ انگلیس از احضار کاردار سفارت رژیم صهیونیستی در لندن خبر داد.
🔹
این وزارتخانه در بیانیه‌ای مدعی شد ما کاردار سفارت اسرائیل را برای اعتراض به مناقصۀ پروژۀ شهرک‌سازی ای۱ در کرانۀ باختری احضار کردیم و از او خواستیم که اصرار کند کابینۀ نتانیاهو فوراً پروژۀ شهرک‌سازی ای۱ را لغو کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/457143" target="_blank">📅 04:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457140">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/062190fde9.mp4?token=vN4TIFr1W1hSfw5ZIHau7z0IpgaIsZn-IaCkqX58uqarttgxT5gv8v1jOAvXDOjGlj2sE1HuAY7vLnFIoghl42dlazRG1x91erziNo4oE89e_LAX87NBo2HcFHK01Pi3HgtkuSgeApic2PhR11goDBoR-WXgC_htvRJUiSWFsczlpJmJja1EwHVsozqEGA1eYWbYN7ILL6P7kQw2AHjs3CV406PA8qVeTyjM6_CeLq9LNy_ki5S5Z5SAsmLtM56RwcO5JI04pPTOI9z3v9vO4LRlRWLOIrqcXV9asfWdbU3xYmX8fXDeWBpww0P2CYMfQVLfMlOCUP4_1EM5WBgmjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/062190fde9.mp4?token=vN4TIFr1W1hSfw5ZIHau7z0IpgaIsZn-IaCkqX58uqarttgxT5gv8v1jOAvXDOjGlj2sE1HuAY7vLnFIoghl42dlazRG1x91erziNo4oE89e_LAX87NBo2HcFHK01Pi3HgtkuSgeApic2PhR11goDBoR-WXgC_htvRJUiSWFsczlpJmJja1EwHVsozqEGA1eYWbYN7ILL6P7kQw2AHjs3CV406PA8qVeTyjM6_CeLq9LNy_ki5S5Z5SAsmLtM56RwcO5JI04pPTOI9z3v9vO4LRlRWLOIrqcXV9asfWdbU3xYmX8fXDeWBpww0P2CYMfQVLfMlOCUP4_1EM5WBgmjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجاوزات متعدد صهیونیست‌ها به جنوب لبنان
🔹
شبکۀ «المیادین» بامداد پنجشنبه گزارش داد که جنگنده‌ها و توپخانۀ رژیم صهیونیستی مناطق «کفررمان»، «تلة الدبشة» و ارتفاعات «علی الطاهر» را هدف قرار دادند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/457140" target="_blank">📅 03:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457139">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534dbabd1d.mp4?token=GGQpxo2bko2uyjc63O7ukMM595ELud0bfUFkhlisfsItYBGSrkzEkkUXIosoYts42lxxGIRhGL3etRiWp3BDKa-OhVjseyvHfaRC5mlJi7GfGd8DzyfaLpQa6DbhE3IKnV7ilTNZFSHnO6vBxnhS1hcZjv98C6P7LgTqi6wL5qEGv8Uy7IRbyPPU-f1LxBSY3s4npaB-8K5jnZ2mEAVT30Djti6IejTqPxBuHqIFO3tyVs3N0e7CVt65RuABpLv7VPODS_BF9PQErmHwotmDKtC0dc0-QWG9LvQoAJ5lrdRyEHP1dVONjgBF8w-ehqaiQFj04cCdij53AG-wbHGyv2VOd_wkf0cViCzTQsVtC8W3K_BzRvfw-VT0IKCLY0wSQDF4gTjKEFQw2fslguhmHqtmGM3BDQr80maHsgMRLSPmhyD-LHCMcbDxMtPxKqK9Qf-119vR1m1pSt9qHn6wQwRsiGX_XXTK1-IAt505tq5x_IV1M9OcSpDeMtdhes8wue0PQtBvqHDH9gnknU0xHL6_dzOtdvoYRebFSjTbd6e2JGZ8Gd4qrAmV-dcl2gSQ97WAtvJ4KgQV6uFbtt-ZtfW7Hg5C-aEN1pIuHE24BzM-XImWZcmqUZToHrYrfnmQs-TahUGI2uwMr2sBuX8QffCTNPS6Yhst7M7J7mX9iGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534dbabd1d.mp4?token=GGQpxo2bko2uyjc63O7ukMM595ELud0bfUFkhlisfsItYBGSrkzEkkUXIosoYts42lxxGIRhGL3etRiWp3BDKa-OhVjseyvHfaRC5mlJi7GfGd8DzyfaLpQa6DbhE3IKnV7ilTNZFSHnO6vBxnhS1hcZjv98C6P7LgTqi6wL5qEGv8Uy7IRbyPPU-f1LxBSY3s4npaB-8K5jnZ2mEAVT30Djti6IejTqPxBuHqIFO3tyVs3N0e7CVt65RuABpLv7VPODS_BF9PQErmHwotmDKtC0dc0-QWG9LvQoAJ5lrdRyEHP1dVONjgBF8w-ehqaiQFj04cCdij53AG-wbHGyv2VOd_wkf0cViCzTQsVtC8W3K_BzRvfw-VT0IKCLY0wSQDF4gTjKEFQw2fslguhmHqtmGM3BDQr80maHsgMRLSPmhyD-LHCMcbDxMtPxKqK9Qf-119vR1m1pSt9qHn6wQwRsiGX_XXTK1-IAt505tq5x_IV1M9OcSpDeMtdhes8wue0PQtBvqHDH9gnknU0xHL6_dzOtdvoYRebFSjTbd6e2JGZ8Gd4qrAmV-dcl2gSQ97WAtvJ4KgQV6uFbtt-ZtfW7Hg5C-aEN1pIuHE24BzM-XImWZcmqUZToHrYrfnmQs-TahUGI2uwMr2sBuX8QffCTNPS6Yhst7M7J7mX9iGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
الیوم یوم الانتقام
◾️
مداحی محمدرضا بذری در مراسم چهلم تدفین آقای شهید ایران در حرم حضرت معصومه(س)</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/457139" target="_blank">📅 03:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457138">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rU32m3JlPq64oNiHd5j0IvNg0n1cjrk1xyDpbC8n9u--RnvzwfsFUD9_yhN3xSQ60o4fIyP4UziymUe82Yq278kQan5xPP9BokQ0HYKerWu_Swa8QUE9Nm8WtAyjIgg9OKyCGmGULX4TlvLuwjJdZ9zKokGEzxxCqLp3gzCN4nUg4Qsfy1Cf2onLHV50pl3iHTuS-4S1EgY2f0Sc0KreBnzknXc9AXJ8mkpCcrz-h6qCOGeYD8bEOeMF7v5nWdlnT4vEssK7qSS7QvLfCYmwEPO3yynBVnPFYpzCUA9SxQ12BtXnXu7Ixyuf6miGAJbrjVIFT016fSva3Wb5TaXL1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعاهای تکراری رئیس‌جمهور متوهم آمریکا؛ ترامپ مدعی آغاز جنگ اقتصادی علیه ایران شد
🔹
رئیس‌جمهور آمریکا ادعا کرد واشنگتن «خردکننده‌ترین عملیات اقتصادی تاریخ» را علیه ایران آغاز کرده است.
🔹
ترامپ با تکرار ادعاهای همیشگی خود، مدعی شد نیروی دریایی و هوایی ایران «نابود شده»، صنایع نظامی به «ویرانه» تبدیل شده و کشور در آستانۀ فروپاشی قرار دارد.
🔸
این ادعاها درحالی مطرح می‌شود که ترامپ پیش‌تر نیز بارها از «فروپاشی قریب‌الوقوع» ایران و وارد کردن «ضربه‌های تاریخی» سخن گفته بود؛ ادعاهایی که تکرار مداوم آنها، بیش از آنکه نشانۀ یک دستاورد جدید باشد، به تکرار همان جنگ روانی و تبلیغاتی علیه ایران شباهت دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/457138" target="_blank">📅 02:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457137">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfpkAq3LPaqtpeLExMGpNPWqqCmWb6yxyCQhY_Nd-hnWvXPd-uK9mdy3mI0V-wQqbWQc5CJZOfWpzAk8Q0NikYotW3Ydr-WSS00esCtKdAyosw2uqLt6rAWZjghoQbhWOX48qmmXka1Dhe1Jytho6JZAAjNLVacEXEPR2ObD14a8XIKHpyRxJihl_07z1KQJ0zVJeK0DLfm9hgIVzRANP7lO698uYuN23ZtK_4DKIE1btekHnFH5q6LG-RkiV9Q1TulaHNpm55KLZR9NQEsLDc3gh2kjrQY1DI4LPLDlZMLmwUMilnh_33uvKgFZbeWlunpDsui4R9sQtpwgc-HymQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک فالکون ۹ اسپیس‌ایکس پس از ماه‌ها سرگردانی در فضا، امروز به سطح ماه برخورد می‌کند.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/457137" target="_blank">📅 02:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457136">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQeZD2cg73u6e1ZT0NBGwIubP4w2MyZ4OXY-Nw9hs3NLSVyMj3KP6Aka8NEqS_oYHinukYss37XhkcHaEyXtm6xvimYLtU1t7sy5-rtpL0Z7JQnitWRgFRtJ9JtrotxTF4vzEFKTp28W54Po8m_GCSNicDvN9HZK_DnJhDcJ3koHwLgoBLn3SAV9Uq9rak7hCQMSxBIEpiV0wkKfpZG6OR8kKD9y6XjfmvpfZADLlTnSvtWt4XzX_g-5q1P-pQaRjUIppg59hHwLcarbagzaq7NNdF8SBDkogV-_89odwcaQZS0qixbodyW6qFNQ-Gd_6LXwo-FgDCZLdyUtHsaTyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه غول زیرآبی حمل‌کنندۀ سلاح‌ هسته‌ای آزمایش می‌کند
🔹
روسیه آزمایش‌های دریایی نخستین زیردریایی هسته‌ای «خاباروفسک» را آغاز کرده است. اما اهمیت اصلی خاباروفسک به محموله‌ای برمی‌گردد که برای حمل آن طراحی شده است: شش سامانۀ پوزیدون.
🔹
پوزیدون یک وسیلۀ نقلیۀ زیرآبی بدون‌سرنشین و مجهز به پیشران هسته‌ای است که روسیه آن را برای حمل کلاهک هسته‌ای در بردهای بسیار طولانی توسعه داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/457136" target="_blank">📅 01:59 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457135">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cefc2913b.mp4?token=Qdd03q9AiRJwh72hNPFVvfrUW3rdUntpMks2pfACUxrSbcero9sOCKLiL1C4eH-IlLHHkGtuH6AiwmAwAHe4J0V7oElv6EI44NdB1gFh0xXgISQJTOAsDFNVrz8iJLzXpf3bQNd5fgglqWGwswfI3ofe9L8JLNjti_uKlhf_IhCOCgYshFlc592vDxHcNzmpGq81KILhWgciSaxDSZVdP_ZaWnhaIhy_K6tsbHBn_me4KXpqpzbzMsV4X5SJtv06EjP-SMAzNoCF2A1cnWAcUhU2xiQfDQHMLd22Dd1TdQPeI1XEVz34LBgglvKVpmb3PM0ZO7cExIKzNkTXZxt6CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cefc2913b.mp4?token=Qdd03q9AiRJwh72hNPFVvfrUW3rdUntpMks2pfACUxrSbcero9sOCKLiL1C4eH-IlLHHkGtuH6AiwmAwAHe4J0V7oElv6EI44NdB1gFh0xXgISQJTOAsDFNVrz8iJLzXpf3bQNd5fgglqWGwswfI3ofe9L8JLNjti_uKlhf_IhCOCgYshFlc592vDxHcNzmpGq81KILhWgciSaxDSZVdP_ZaWnhaIhy_K6tsbHBn_me4KXpqpzbzMsV4X5SJtv06EjP-SMAzNoCF2A1cnWAcUhU2xiQfDQHMLd22Dd1TdQPeI1XEVz34LBgglvKVpmb3PM0ZO7cExIKzNkTXZxt6CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر تازه منتشرشده از توله‌های «هلیا» یوزپلنگ آسیایی، که آن‌ها را در سلامت و آرامش نشان می‌دهد   @Farsna - Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/457135" target="_blank">📅 01:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457134">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRqahySUDoZngEwrCOMoyjyQqb4f8XfCH-JBD1XQErDR2g1DSz10kQluHzK0nlgJYmooPhIBkbv-Xsv9bmqHE2iAE89YHwWK6t-lBgx-lTcK56xlEXQXZBCqAgzpUulm0eeVfKHuxJOMb8aCOF-Mt0kQvD7jMKNRJw9wTVMLy9ScPtNmvJAlK4ImqmlHvMQTOw6QjzdELtXqS7lC6Y6b8TqaT9_PjxB7wPvjRSVx3fS3k229KIhY5ThgCEwJ-gvl5wIUbKoIpLcLZHt582NoiES9rg1U0_jT3_7dHeZEzbsnBT9cvZIcMj4jqDdiDKhy0jlEcLJrPX2wjjBDk_noxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ: هنوز می‌توانیم ایران را تحریم کنیم
🔹
رئیس‌جمهور تروریست آمریکا مدعی شد ما چیزهایی داریم که می‌توانیم علیه ایران تحریم کنیم.
🔹
وی با تکرار توهمات مضحک خود ادعا کرد هم‌اکنون تنگۀ هرمز باز است و قایق‌های زیادی از آن عبور می‌کنند. البته ممکن است این ترددها در مقطعی آهسته شود.
🔹
رئیس‌جمهور کودک‌کش آمریکا همچنین دربارۀ افزایش بهای جهانی نفت و قیمت سوخت در ایالات متحده ادعا کرد: خطوط لولۀ زیادی برای انتقال نفت و گاز در حال ساخت است. من فکر می‌کنم تنگۀ هرمز به اندازۀ گذشته مهم نخواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/457134" target="_blank">📅 01:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457133">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حملات موشکی روسیه به پایتخت اوکراین
🔹
رسانه‌های اوکراینی از وقوع چندین انفجار مهیب در پایتخت این کشور گزارش دادند.
🔹
شهردار کی‌یف با تایید این خبر اعلام کرد که پایتخت اوکراین هدف حملۀ موشکی بالستیک روسیه قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/457133" target="_blank">📅 00:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457129">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YMe2CGZ6I6LVsJg9BtnnFavNDNLMcPpQBS7YrGPrhWJ-T13dFx2ktn-ZuYlrnZZdJHVhq6vNprZ0kQabG-PPgWSEO1XnF86DjElrAikqMfHjTXq4tf-ChMb2wuwXmFTI-6-VMUa1vnk-Wp8tqumrgdiwsyId5aemmwFmI988U9HIGLV_0Li5F8HTakxpvldZTIV_SwhrWGdX__avmesY9j7nG7zvI7bY7tpIo4WdO-UQeMb2fGFC66SvvxWXXn-PU34aSRK3dWip2wqDnsiPBsNV8Mh-oLuSywFZ4hbTu1xXgJlo6wJbHGRQ1eOOPrj21DMvQPgKCHrkABdASNP5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s8NayPsirXxwag6PJbuusmRZuW7VMxMDqmxGEizHDsdBSf3vND8-dBdEwtIOdDD98iEbTCOKoX7Cs_22Vg3Txn-cc1vpSWnN-GNoRzPZ2By29N9VCOu6KH3bFzzV899OyYEZWG8IbycfcWi-1loR0x_PZWxTVZcJT_LaHn_1jui2ph4Pab2JPnnplKW6BwoMOv3Fbc_zOarlxsDQ1qbvfc_SwxL2VsM7c09zKZNF6RrL6PNosNwwWdCxDQe_2HMyHzXEdBL4E5jj9YOFDQ8h73Ria2m_BWJyefS4Xxn7FHcIw6ws6LVRFPvr3XyMTnDty5-Ff_XCpBxjaXWh0nN5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/btlYpJM3_QY3kDjSV_yaWBGXHgjcVNBOhn2sQrI3zhJpm5Kw7fzcygFJNmC2_m2bD9NSjBFbABKl0zGbsLs2LSq6yYcfJ_7MSSyk_I1E0I1JjuLzicazjQVoCZtWB2uVJ0ZoDWpYPh16vlsxyj8aUrgKeP2PtLmdrCCzmH-2i7dUClGBrAJmsIgfR9WN7GMufmKP7d_YbPSojg4bA3zxm0xNFpeG6lMyPxHCmhhl8qr9_n3uu1eAJDKr9Bb0i4ky6KthhydPU4Z_BX-nDLHhKtBogXocX4qsLuySTVv9HAjLtYWhAoMIYpxqIZfpdhrhuFUem1rWp0IRDHQgoxt7Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZcmJkhZ3p7S6OVZWJN3kIZpGI6vOFzMY595jUjIW9y5SQGClm45PzZIQwgqgK-foipSU69P0m5Y2s3dkqvuhB2c0BkBHh-i99GePomWf66qSZgDq_a-AB2TNpxTkdQOKzZB3HsgV2YlKrSuAWnaQw_aqsCAEgzfs1-syUY6jE-upHx2VcoG7-7iOs7oJq-jXWhPHXBQ1MverG4udK8S3sgacqD6t24IxBiI9HdvzD-DdatGnZcX2dsBQRoghrok4k1OfESEFq8uKfC9XwIMaLZAVvAQsMtWLvyEt9dGOSVNjIJxl_jt6hByhnEWNyNr7HidPxogwDTCSHK8hjiMnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۲۹ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/457129" target="_blank">📅 00:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457119">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nsy2M61tAK2kTtkd1kVEmwyIihG_6rwcMbLu-VfmSGFEgXCrX_nk5qT28GQKOq3Yvzk915mGT0IOTOSmrlsZL3iG2APtmryEAS3o0-536LpSp5h64LZ1EXDZEnNd3EbHPDpjjPwnXnFRN7Ii2VJUTypPriLoff3JHmg15GOvuxgGUQyajiQyTZCDVpD5OOXoBDN-aIojCRfC8XNZ25_mVK0RJPCrtLEkNsHmUxOYcPik9pB40ABWsUicHzKz1fOdf3jZvfSef1vGNPkSVR59WggLns-T3erWpVElq6YXSyog-YXeZbj3Z4yJGkXPBRsTmViQgMTjbKzu5kWMq5Wg4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZzpKgiiYmTUQ5NcZrh0ydpB0nwTBODX2eJ0oBHt0ISnmHl7TXbCtP1q9GTdSy4iyyoEgpcSAtFBDqGuMu3WI89SoanweCeqSaKRm-aB2oiQ3wKiblmkilO6wVAgY7T30yHku9fGtLJutAGC9UyjVEh3pkIlWjnZs5s79TclSXOJ-C8CNPRleOAgdoGn9Z-zMBgX_SbvKE3TXgsbOeKpuAGvZ2pOLqG4nzd5LsBcG6HMv8URZDd4X5LX_M6A1Pi_33YDgenqf0rY1H0C7eIjXFvHSwJGM84yo9wx-P60VCjAbbeTz2TYOt6xopVodIqBdslj_YaWrGNxdVX_E3jdzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fvOrsCvxBQf6-w7wXFKjhthPSHtijHRLjpsIkPo-jAlrJQR6XOB022Txaqoi3k7-k65chUOMZcA99BzQdDcbHBXSEju78jpqTSfS594A61bNlZBXmzDMm_uQ5RcStSqSsUeOdYOLhWZrx4q9QHMfG_H5Bpl5k43Cq8cXjxxdfeEiHumbwNHYr-5Nmvmx0azVQA-DqmJLaYCfsPqE_Ihr2jm8YfdK5TK408efxyBtLruP3r-JiJDT2e4hDZo0nmHfnjksSw9JDPMpPFW3c6GHlBkrZpGKQYLNYY1tsTzK9STW0UUXf1-CkIIQjblSBVA_ovfBZoJTWzoc3Tkh7oqc3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VR3ZdrODYlvE5zzb8X7W-srRN_dySAcrFf-ENP3xbAgBuIONQk1hL9w1NC460kgyUvkHTDUaUthYoPExAcxFEQqis7vxtLiPqU6mYaQgsxFVxca0BTPLRccSbKIAIbwB-KNRCqn0x9kIKdIBfrzNoHpCqL_ef-o4YqwHqh0f9CRjSU_jK4b6Bad6RjXdDa6H03Lw7oGEh5njSAjp69QcFv930YiUbbHqC3h4Hiy2eab564Zj-8a5sAuyWeCa8NdCOfY5pkVcwAB5Ffsr5ivSZiqIogt34UoVvWzX8Y5glM8jS0uuuNpY5e1EPf567WKd01IJFy2ETezS8Qmz9LPT3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pCprFdTq20ZnCwSQVmlRDNXuhs2V9yBW_cLj3JLCF_FLdA0SpcCke7x_ljvhDPJRSVeohrxuYVstAJ4Dzn4_0tvdlJtj4DzTBc0NO2mvktYAC3bE2_kvT4ech77qrWup6OLNbizGBJpOXm5oWNPJNn6J7NbT-uUW-oO3a5T5wzYfiEGqyWshnY6poZDi1tuxzhyaodiJkHPVfoJWDrEoHjihTzMVogTd4GKIKOWq-Z1rQWCNh__N2Kw9iTtk8mgIJJNfAs_b2KAqYX9dpozKEaNjgbW-O0ZFwYa-_OetIW7KvvdK4wHQKqRCpVyouiFANa7WGsdSNdiDjzgeriO5Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLGc4w_3mk9iPrR1WQN9OpKP775dMmPzd-wQb2Nz2NScDzSW3YkxFef8XF2rwUu9ul4aMaaFSuKtBrXUzdUS72NN_BpN85EOEeASYKAefGAlUlkh5WnxUTxkfha2LjBOt_l5YTKOTsizCA8gsuIl6kVkMPePgZp2oyI7Bi5KvBa5PokUWE1mb-ax6FiIzg_bMDQq9ykBTfsw6oE3kIS95HdUakmw-bkVj8k464ak6tqQSqBhlsTsJFWXf47xGI-m3pb6ODqrqn3mK3K9SXYiCDWHyP_ArfxusBnYw0RMGbW5GTPTDxKLEOtc9zuePvt5lTwS_pDwoqmBzR8kzfD_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKlHGvl_iZCTZjjmL6iHrEMINEy-4DzmPc2ELG0G4juX0oCiD1EwQ_3Gd9II09M-X2Mlg8Ce3qYGuMKO3RXE5vXJOEIy4oM3S24ngpdK0WtTbOurczlohabOIY9m-f8QciPhe11NCa5FjuoWHxGXuvO-XZOPUc7f-ACG-vPOtqMCnGN5Jpq5S1FiwBdnPXyTLqdZ_-mSnjGtPlEitvdSK03FhRmpqyCaDJxfSZjbHunt43_vPxilRASLG37CI8YE39J8U8e5IZFZ1vVEyeh0Ic5O-rupWF7fyqyX2-bId16lTHWSiiaNNkAUNO7pAAd4MjRoOMYV89mnkuRRKSFoxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oV5Lwupi7bqtSdr-NNNcw1Qqgv9FIDJsoSnyFG1kG5BcbVCOEtOPtmVj1voTbhMGbZnvtVgqqngM4KPiQ-Q1Ak8gP1sCrtnqyiGleQ-BMXK4MwuiTBy9DKBLS6Dz1PCOp86taaOR-p3CeRepyAZ5FyJ6HHhIkv1BTMXA_aTiZgU1Jh53YmFWc_GKA57ksiD4U1uLvZb07XdJKp9rqxG8Jlud66qO_b0FS1Kc8czVYqJdIvSHToO23Okw31TT2vUCyBqPn2IQq1G5GrCWVfvhioLg7484rNGAer_CMueWctaz91Zicf86MDL6s7mLIlSWyPfzt5SNH_g5phJPwKA1wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vMRWJ15QdYr1-abl0fBL9Bo_3xl4lU92xfmK-FQSIl4DOh9mYQlYc9bw96Hq13XMuIY-k6TWuwo03jRc8rT9-9UQ_zCrP7BUZLFlktAB71OSh6YdW6W1B2Pr43KbmxbjWf597gHEL-ETQF5N7V4zj_PBHL67h_uJHlRFuAT0e1Wo5CcMkJCWWcKLIhzXyhQ9FpVwI-qxDBAc87sslutihzwKmKBIr056dfZtQK1YQGQmapbN2f9999frj5kTlNdaljuemWJO7G5gZ62toyoLsrt-D4D1xLgio2qkiNT4AD8Wo7Cm5HZccL31c160mqeuTWfWUYZki1-JvY0HcILR6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sdxgpJVkNEPjgOK3FgfjQQlTojHlv68ehMpxdZ9NJG3mrBN636zt1OqoRtEcIW4tSDGPZnFQ1O3uqn3d_Bn6Dx0GS-DbTBOqyfvlsgWDW831zpGTLLUWzadkLzHYMaUD_1koYwwmix4hJOYWkQ1IBrl4wzaCv8AW8gMBY9yAZv6JL1UUwxZTZmekznkWwSnYWrS8sHtpzGKh6Dd8h7qdeemwq2_Y2Zs24oyUDRK4w6sWcyDsA6leldr3dPxBYrx0JzRXb18XZAlKVl7aAFIcmRVyeL9ZLT2kvmzb9uKqP5x6aVXwynfVIyvQVP_ynnM3Z3A_mBpciWv2SlcxMqN3Hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/457119" target="_blank">📅 00:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457118">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPJQtmuHyEWdrqzeC-PaPcTNZ7F6sV46vaK1IT60_nV_gcvLvQBq28UwJDCJN-RC6aGbGpXSSWUa_qkFR7ho4uXhEw0__FZL_iZJv-P5shOiTeT8zeuoL4V88x0anYMRizlFpgfdgLV0CD0ubqzvzwyPLIPtTOCskMVExD-OvAtGaw-SG86ftXKvQ-irXz0z2_sbZTTMawDP3nwf5WZvKxlQ3uxgvcQJsb7rK8ACOuj9pZtCUtUKhHa8cx-X-DESyHFPz6LJJ2SzT-qDH2g-uBDZH85tGPKl1-wIm6MI4YS56rSFq-ANOG1IXYo0RATVkRXdG3GX5DTXHt6Y0R854w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاگرام اینفلوئنسر اجیر می‌کند!
🔹
مرکز پژوهشTTP در گزارش جدید خود نوشت: متا صاحب اینستاگرام، برای مقابله با موج ممنوعیت شبکه‌های اجتماعی برای افراد زیر ۱۶ سال، به اینفلوئنسرها پول می‌دهد تا از حضور نوجوانان در پلتفرم‌هایش و ابزارهای ایمنی حساب‌های نوجوانان دفاع کنند.
🔹
این مرکز در مطلبی عنوان کرد که متا در کشورها، از آسیا و خاورمیانه گرفته تا اروپا، به بازیگران، روان‌شناسان و اینفلوئنسرهای حوزۀ فرزندپروری پول پرداخته تا در برابر ممنوعیت‌های فراگیر حساب کاربری نوجوانان موضع بگیرند.
🔸
این کارزار از زمانی شتاب گرفت که استرالیا نخستین قانون ممنوعیت شبکه‌های اجتماعی برای زیر ۱۶ سال را در جهان تصویب کرد؛ اقدامی که دسترسی متا به یکی از سودآورترین گروه‌های سنی کاربران را تهدید می‌کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/457118" target="_blank">📅 00:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457111">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vjeFr5wjdMpqcsR6RHmyJ6JV109Y--C9jqngJCnqefH5vkbkR_-h9GuEA9brWSOsNf58s2TsaO0rgsuYWWL4xVRhUOpdc8qaFIRAEabIvsemuX2ztRfdPYOxbKAgnpLwG8Ygig7l7w8qAZG1VV5BLxiaLSuH1YdeUFDKfI0mqiMe-AFjO2FDeN5ZDclfBaeBDQD6u2_P006662uiY7nI1Tau2O1MiCTDOQOrKCbO2mLFTf_BjkZldueptu9OiysDcwSGhTujMpNOfeBARSomFd9L98TOMLzMDCiJ5FwdYHHvEdypSC0uDHELj424FkUNsAiiqAwmRoCRLTnxgBEygw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SnwGsDmdm-0yeIEnRHQE_fDdBzfrl3FcHtqFiWGZbxIupSE471CPaQwKRFX15HxN3bwCnenq7MCah_tLWKw6FXJUiA1BAnhpoy69DPmctFQk5MOOaPE1A-MK5XyFCqv5Wy1skd5lVYvhbJEeUbkqd9C8BGyN7A2njrjGIiU1KZIlYQ8JHl6xxb0ShdrtH_esjR0HWlhsERrTPxr5IzIY0y6ulCVejTq8oAHVrQHDcN-_WW13wCHnz7lP3uqcHEMiIy0uYEHLtNbMRkMQCqSNirZnS7ObvxYamhs11oDi4nRXqdPy65c9fiylelTaib3ICMEmD1xu1NrDPXrtYrQaGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MtiQVgs-rYBYFsphOEnahwjeAt2i1dV7riygBUGYOIzeFZOFfDmydErNidWRCB6KG0TsM5__SDr2scw2rAX8t-naximOufZ7LYmilYlnUx-xtGGNw8vuTLXSTJ2fQmvSHqziiVtn3GKDnH3y1oeeIgtNTtGU_OuykbrgF1FeAPyghzzuPOnNcu0uUXL-wemVnGSDN-ayLnYmN17j_vz1Ng7bR9-fyvfcAwlTHGvEsy6QmYaDi0QmHzu5mJOqXhp2GirLaXwfLFKTaCs7LkO7UXTkL2i6G4cQkx-zN6UFOqSszlHS_wqzGD5EQg2zn55cVFNlwECag1xZcebu9FAs6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XoXxpIPrZq6mmT7SiVEu0WzO3HN_SVEHOu4xWBD7WwusLJqa0K_BN2tZUOCq9CQtl7sjgupjSvAOx0roVqJMF-rERw8S1_4hoI7yd5_iJ3RrqQSkKP-ytqY5gclAP4BdAX5KOyuOMDlzybtlngFDhlvBWZezIOdX0F5V-UdCF5tv-EcZxA3SI1CaDcI0d-DFxeX40Gw6X6IO_hlleFfRHUG4YlBxhuWj3vZUVqVp7mlYfOMM6Gehu4mHZcJhWwyCs6pKsC8niKKwneE7-BHTI17YfSDdDcYE8j7JBrAOPkAGOL7KGroHpo_7erWK1I8N8RVHZK19O1rDxEGQxFWlJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HblBN2A9DOVJA8IGh-rEle1f4ZeSjK9RIS1VK3jcP9PZvqx9R1YrSr2ZerP9OrK2d5enXwB4oyp72UXqrh68qebwp2bgCqdFmYQf1dYQ-Rade-KvxbXzOhhyYLD0NSX80VONoHhAThAUPglRZW9qWGRMk78lhJrB9zDEwQGf8Gg3jGb3tSUt1DO_Mofi_VEYAor3t4TO-6POCV8vlqvEneMEFCprICIAPyDxN3RUsGu_RNwRA1jJ6BmsjSqQhOxGzRlPKCqCzRxHUugHKM59tJPxIEyQTxPfIT-Aj0kE7-PEO4bLdKFeMCFTu0YoSnr3w45y4NT2OYS2YbZNCx4KyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jv04V6QltzCtcxr2tdbe0pGWCqgitrOzWUF2-1p3fZ3epK2TiwLOmaTsaS9UxqzS94eCUF5tIZ8qCepPeQ9ehCUsVv_CWhfaYchHnpwke9KBU1J3vqRMdGUfpqOU4IGRasl9Q4NKTVSU8X2j2TWwq_G2Nh-3F8lpKNnoaxGkITznlfsJuX0pyAE-ke8CBOXbG9NsmitCkNOAEUxl3A_lj094MOSgXhf4XBWZ_JIi789bLJ5F7tTsLdshX5DXb1jXjY-htVcskLuifPe2yOUeZAhyG-jpzOVjcBhv6txLH8MtBdVYkcrmMBHl2A6SgZBKErDW6dXKK5aZeyxIBejhAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qV1x5zDEkEtwbuv1LaqWqgI4xM9iIWCk7j7f47hstb4k9-xsHZ0izWzfMRAjzezJpSvz65cnVBBGi8vK8BPSCkyB6aVchrvNaBRw54BewN3rRQEFxzYlEnqX_14fbuo7mW7fMvyseyjhG7Sxo-xwGDKHoeTlW4wdGLMY3a1Dl3hJBclxLStSF7f0_WwA9Zi0vl90k2kKFhICqiqW0aR6pYx7NXA-6FNXtoFGZiv2V2bxxJQ1eRCEyj_lSTn8LZpWhfossoQXXr6cSYirTcs5-4qEafXsxGcZjbCfbbSUG_qpUQjJcPJT5fqp6f8Qfgza0oPYahgmQid6j3kufV2ihw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اربعین خاک‌سپاری رهبر شهید انقلاب در اراک
عکس:
عادل عزیزی
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/457111" target="_blank">📅 23:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457110">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc99cb7a6.mp4?token=Ff97HdwAEv9om62trISBsVO372rohkU7pCv1DgFbcfPRaorAseWoFGFuGQzzmyABkCaJRWF6DB65OpUTXwummPYHiJmyIgherYLb3ug1zGPApJ59SxeIjUjwGkzcIs2Y137iTG9ejhugY23vfFPNVzkXI4xOFy8XDMoFxj_FV7Rm559MN6gHbOgeyAAQDdRNeqcWTN3s7BQ3pkqMArdGAtfNhxQJdXZ0s7GQYEcqejKGi3waKzqVaUm_DAgR_gVo5LPLwxtUpMj3dAF71WtkvNjIdPMtw-P2qRxBSvPEFogSIY1T4tuzYxrvawKzfYD5wdbajG_GplWYNBgiubYkvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc99cb7a6.mp4?token=Ff97HdwAEv9om62trISBsVO372rohkU7pCv1DgFbcfPRaorAseWoFGFuGQzzmyABkCaJRWF6DB65OpUTXwummPYHiJmyIgherYLb3ug1zGPApJ59SxeIjUjwGkzcIs2Y137iTG9ejhugY23vfFPNVzkXI4xOFy8XDMoFxj_FV7Rm559MN6gHbOgeyAAQDdRNeqcWTN3s7BQ3pkqMArdGAtfNhxQJdXZ0s7GQYEcqejKGi3waKzqVaUm_DAgR_gVo5LPLwxtUpMj3dAF71WtkvNjIdPMtw-P2qRxBSvPEFogSIY1T4tuzYxrvawKzfYD5wdbajG_GplWYNBgiubYkvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مادر شهید پاکپور: بعد از جنگ ۱۲ روزه فقط ۳ بار فرزندم را دیدم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/457110" target="_blank">📅 23:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457109">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">تکمیلی/
مرگ رئیس دستگاه اطلاعاتی اکوادور و پنج آمریکایی در سقوط بالگرد
🔹
در حالی‌که رسانه‌ها اعلام کرده بودند که در پی سقوط بالگرد در کنیا شش گردشگر کشته شده‌اند، گزارش‌ها از مرگ رئیس کل مرکز ملی اطلاعات اکوادور به همراه پنج تبعه آمریکا در این حادثه خبر می‌دهند.
🔹
به گزارش دویچه وله، میشل سنسی-کونتوجی در این حادثه جان خود را از دست داد. وی در ژانویهٔ ۲۰۲۴ به سمت ریاست اطلاعات اکوادور منصوب شد و همچنین، مدتی وزیر کشور اکوادور بود.
🔹
علاوه بر این، ان‌بی‌سی یونیورسال اعلام کرده است که خوزه آلبرتو سوارس، رئیس و مدیرکل در شبکه‌های مختلف تلموندو، از جمله کشته‌شدگان این سانحه است.
🔸
تلموندو یک شبکه تلویزیونی آمریکایی است که برنامه‌هایی به زبان اسپانیایی تولید می‌کند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/457109" target="_blank">📅 23:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457108">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در لردگان
🔹
سپاه ناحیۀ لردگان: فردا از ساعت ۸ صبح تا ۱۲ ظهر احتمال شنیده‌شدن صدای انفجار کنترل‌شده در شهرستان لردگان و حومۀ آن وجود دارد.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/457108" target="_blank">📅 23:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457107">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d50b79f5c0.mp4?token=cbnH80xASgsqxYjNk05q1F9PdwjhNLR2GjUBywgYu6OuOBaFtWIAhGW4-eEeiyE4GmJ0O85EzYOw3J4Nm0C5-BRuskySaOuFZQuDBkqOFNjfsSgT8ShsjKpmbMyh6aQGWDyWDdW-oa8GEGkqj_wwk5g2OXbfEtP97wPF6xMQGhfcJac4KpWTv9QhrJnwE7jevzjEf3nN0Wb6egLPeQ4c3bkctP2qIfmEi069BpyziNkHmoKC5OAfduUMP-Y34ejgABRaZhG7ke562oHshPY6USpwqbr08hhCJ_2c2EL4Gb_6tO2jGzOGC5e4pxu3TtZsw1dVrsQGTPgdmW8mVB_Zog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d50b79f5c0.mp4?token=cbnH80xASgsqxYjNk05q1F9PdwjhNLR2GjUBywgYu6OuOBaFtWIAhGW4-eEeiyE4GmJ0O85EzYOw3J4Nm0C5-BRuskySaOuFZQuDBkqOFNjfsSgT8ShsjKpmbMyh6aQGWDyWDdW-oa8GEGkqj_wwk5g2OXbfEtP97wPF6xMQGhfcJac4KpWTv9QhrJnwE7jevzjEf3nN0Wb6egLPeQ4c3bkctP2qIfmEi069BpyziNkHmoKC5OAfduUMP-Y34ejgABRaZhG7ke562oHshPY6USpwqbr08hhCJ_2c2EL4Gb_6tO2jGzOGC5e4pxu3TtZsw1dVrsQGTPgdmW8mVB_Zog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: ۷۵ همت از اموال بانک ایران‌زمین به نفع بانک مرکزی مصادره شد
🔹
این بانک ۱۱۴ همت اضافه‌برداشت داشت که با کمک قوه‌قضائیه با آن برخورد شد. @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/457107" target="_blank">📅 23:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457106">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e19cea5db.mp4?token=mfHBxqSgjD1d0C0q4Daw0Vo3WIbUFmlbk3r9nuwDrBCuKPSISqKoy1J4ZChkQqeE48NJVJQKy332XWClI4BZ55H1YX3UWAnbnGSNvjYG8hauy7PsQ7y7AXH7igRtG4hDGOX0gyMMDWmmdULczQrLqAF_8B9JFcBnVhBvEHhT_lKlVtAHXBTXG8zPwSrk7bMaWFyNEvwQNpY1gR08tb7tAOcKSn-ij65WTZbeVNqdB5ZeA-zJtsulE1-UMewA6sxwveJq_4Oeo1rBnWLZXuKSDQcSym2T9Tmp-mxwWz-AzafQfMK3XKCO8KKjH-QTQ8Xweh-hpC-uzoYCZqAYeqeiwGZzvlSid0u6qEMP-ChRvykBIF7eg0Z0EIvVO3yuld_UqhAS5ox3trx30S2-OlXF8Oleenji_QCG1Qk8DnJWVxGTeFp1jsB5oOE2crlb91gqHfm2BZ7hffm6r5z_OzSwkBChonrkW4ceYt1YzAlqHrtfnSmnfhAa-_GxFhC8n55F3bi1tXzdLL9W5Cl-RCChBmw0ZrHHrd15mPQSaWz40KSppOHXjuLTcgMUyqSW47w-drjXdlMbZ9UaGcEwe77mjyzuvQNSc-ZMDUu_ZLkDILDFLWRqg-HrEkfmaVQu_20MJEsQIEwCPK7LiJxUGGW401FQWRcjPLW24_17mL4XU4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e19cea5db.mp4?token=mfHBxqSgjD1d0C0q4Daw0Vo3WIbUFmlbk3r9nuwDrBCuKPSISqKoy1J4ZChkQqeE48NJVJQKy332XWClI4BZ55H1YX3UWAnbnGSNvjYG8hauy7PsQ7y7AXH7igRtG4hDGOX0gyMMDWmmdULczQrLqAF_8B9JFcBnVhBvEHhT_lKlVtAHXBTXG8zPwSrk7bMaWFyNEvwQNpY1gR08tb7tAOcKSn-ij65WTZbeVNqdB5ZeA-zJtsulE1-UMewA6sxwveJq_4Oeo1rBnWLZXuKSDQcSym2T9Tmp-mxwWz-AzafQfMK3XKCO8KKjH-QTQ8Xweh-hpC-uzoYCZqAYeqeiwGZzvlSid0u6qEMP-ChRvykBIF7eg0Z0EIvVO3yuld_UqhAS5ox3trx30S2-OlXF8Oleenji_QCG1Qk8DnJWVxGTeFp1jsB5oOE2crlb91gqHfm2BZ7hffm6r5z_OzSwkBChonrkW4ceYt1YzAlqHrtfnSmnfhAa-_GxFhC8n55F3bi1tXzdLL9W5Cl-RCChBmw0ZrHHrd15mPQSaWz40KSppOHXjuLTcgMUyqSW47w-drjXdlMbZ9UaGcEwe77mjyzuvQNSc-ZMDUu_ZLkDILDFLWRqg-HrEkfmaVQu_20MJEsQIEwCPK7LiJxUGGW401FQWRcjPLW24_17mL4XU4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریادهای مردم کرمان در شب ۱۷۲ خون‌خواهی
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/457106" target="_blank">📅 22:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457105">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a78829c1f.mp4?token=Ch-RNzzBStYu3End7F2fUxdI1bV8WlVwYIxBx-CGE-Oe7mcog0HFMhCnDjLwVOGnmy6dA4rBTGQj4S0pEbwSVh7THxnuWASzTiriJZl1rXSB06akvgOXCRJ65lD8FTr-7I0czxy2ms4LUN3080W59hTS1iXegnO1_u2JJp7nlTwBQhKwcCgy9SRbunoEhuQ78bmElAs2FEpdeUwYfGujeJmKYwxSg7qDfTNX5L2F5yo8BIrQABHnb3EodXrTDsCke_V0j4A2SMbsz1mugle2tKybOx7i0CP0ttu5qyS8zSEWpG4v4_Qsp5AwVGgWWbX7Yycjl_tZPriCTq6C6eo_3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a78829c1f.mp4?token=Ch-RNzzBStYu3End7F2fUxdI1bV8WlVwYIxBx-CGE-Oe7mcog0HFMhCnDjLwVOGnmy6dA4rBTGQj4S0pEbwSVh7THxnuWASzTiriJZl1rXSB06akvgOXCRJ65lD8FTr-7I0czxy2ms4LUN3080W59hTS1iXegnO1_u2JJp7nlTwBQhKwcCgy9SRbunoEhuQ78bmElAs2FEpdeUwYfGujeJmKYwxSg7qDfTNX5L2F5yo8BIrQABHnb3EodXrTDsCke_V0j4A2SMbsz1mugle2tKybOx7i0CP0ttu5qyS8zSEWpG4v4_Qsp5AwVGgWWbX7Yycjl_tZPriCTq6C6eo_3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: باتوجه به رشد نرخ ارز، رشد ۲۳ درصدی برای کالابرگ منطقی است  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/457105" target="_blank">📅 22:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457104">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79e7b14962.mp4?token=lMrG8EpsZQmPTUpgZ4wzsfRQJqdufhpUJTBUfTAEID6sm30KMKE1mAKvdgH-cxmmI3wB0fjODOCKTvWTtjK85E4sQFPDBCV05L4PtSCl5iIIsjuQu9nV7h5rrKE94-3gnbX_sDkblOWbroyVSDMT3Ng4mXh9XziLNfhpgvQrbWMJaXY_GwMrhULRN7bbcyp4ck5N1hrC3Q0kK4JCGobVKegSkd02zhOBQaUFFKnQ0o46eBohlh8VV-MoSZAOcB84mgPHVGQlLpdGK20JbilekvaHWlNP9y9wuwiCurDC9TcQGr247yqHrz5tONXldGOSElI2lG9RhvlUJXfVioJ8BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79e7b14962.mp4?token=lMrG8EpsZQmPTUpgZ4wzsfRQJqdufhpUJTBUfTAEID6sm30KMKE1mAKvdgH-cxmmI3wB0fjODOCKTvWTtjK85E4sQFPDBCV05L4PtSCl5iIIsjuQu9nV7h5rrKE94-3gnbX_sDkblOWbroyVSDMT3Ng4mXh9XziLNfhpgvQrbWMJaXY_GwMrhULRN7bbcyp4ck5N1hrC3Q0kK4JCGobVKegSkd02zhOBQaUFFKnQ0o46eBohlh8VV-MoSZAOcB84mgPHVGQlLpdGK20JbilekvaHWlNP9y9wuwiCurDC9TcQGr247yqHrz5tONXldGOSElI2lG9RhvlUJXfVioJ8BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فتح عظیم در راه است
🔸
سخنرانی حسین یکتا در موکب امام شهید ایران شهر لامِرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/457104" target="_blank">📅 22:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457103">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noAcn8SjWpeJIaFOWM0ArjOqZZWvEsHHgGw14Z9vuXTbKk912QchXBvjiANKYOV9WS7zkzTEwKivJ-y8tbqiTa7PquWsklkXX6c1WmsDCnjRFPoEJxPWZ3pxOIgEllOs_ho6EF-EpVH5y6bI1roaw3Zs0WAdZ9i1q_ki3IT8l3EfZJz5hI8jK3blX-F1bbqQHyN1I8yO8YqrxIcYjKUxDFGDW4r2a0AKehDLZTxA_cDMiztWvnvjCPmJHmK18glxZRm5jfrSX3Qpek7Myku0QORLhGKdzM9wQUJkRboRXPz7mycngA6CWSDaQ5w6T-jQkYwVioxuxmDJg75iqdaw1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاگردان تارتار گام دوم را هم محکم برداشتند
⚽️
پرسپولیس ۴ - ۱ استقلال خوزستان @Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/457103" target="_blank">📅 22:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457102">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4808bb6f76.mp4?token=kN_WiElumAE3MSglhAcoC641TjvBnCa5vVth30Jq-k_DlRbWMTw2CBmUXYFXE52BzUhwqkoGsAvMXZgZwK6LUw6XqSSDbAmvK7tlW490VC6WtR1PvcPQRJv7dR9ABnLuiS03yKtdfeG0Ks4-46vMGwj1Uv4ljqP-tV3H0Q-LYXxnHmHf2pDpdYCxsXhzHbx2R0yTtwe9fYazKCjef0gscGEo5CHWDve3YYQolObJ9HUZbRgK7zXaWW8nhUAkqXpgIPVX_wtpyb0F2P_bCtEpcFW_-zVB1y5h7qkSs7NxJjVInTWbyuVoS3yHFhdLyqRG1KLNY2knVPBPoFFSJtQcIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4808bb6f76.mp4?token=kN_WiElumAE3MSglhAcoC641TjvBnCa5vVth30Jq-k_DlRbWMTw2CBmUXYFXE52BzUhwqkoGsAvMXZgZwK6LUw6XqSSDbAmvK7tlW490VC6WtR1PvcPQRJv7dR9ABnLuiS03yKtdfeG0Ks4-46vMGwj1Uv4ljqP-tV3H0Q-LYXxnHmHf2pDpdYCxsXhzHbx2R0yTtwe9fYazKCjef0gscGEo5CHWDve3YYQolObJ9HUZbRgK7zXaWW8nhUAkqXpgIPVX_wtpyb0F2P_bCtEpcFW_-zVB1y5h7qkSs7NxJjVInTWbyuVoS3yHFhdLyqRG1KLNY2knVPBPoFFSJtQcIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زمزمهٔ دعای توسل در جوار مزار نورانی رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/457102" target="_blank">📅 22:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457101">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b984e842d.mp4?token=anJTfaWrK2y5wkzWNhkh-SdSGbtnkx-a-oV7A1fcEkllmgwLmm5FywrqDjPacnJ_ejBOw7v1EgQgk-xScx3384aAUi5pGnMdEc0lHcKPz8npiX5hZDL6XefjMDE3iGaUjpZOpBSo1DZG5zQsicV-vM9p2_g8k5Zdo-RrkjlH2OFqJ84MN51JnA-x0PSzXS_Csqqb4Q0Bd9bTl6nr-G0HwiqezqNICDEXyMVRzJKUYgBJ8M_I--uCubPBWfVgshQQ1UwSHbl6KgDxhR4nLhQ0uDeoRqaozxAZhkEhFvYboR04kAPuYcyW30Xtc2EEfUsRgWmHIYWYLA3wT_j5-Pcjbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b984e842d.mp4?token=anJTfaWrK2y5wkzWNhkh-SdSGbtnkx-a-oV7A1fcEkllmgwLmm5FywrqDjPacnJ_ejBOw7v1EgQgk-xScx3384aAUi5pGnMdEc0lHcKPz8npiX5hZDL6XefjMDE3iGaUjpZOpBSo1DZG5zQsicV-vM9p2_g8k5Zdo-RrkjlH2OFqJ84MN51JnA-x0PSzXS_Csqqb4Q0Bd9bTl6nr-G0HwiqezqNICDEXyMVRzJKUYgBJ8M_I--uCubPBWfVgshQQ1UwSHbl6KgDxhR4nLhQ0uDeoRqaozxAZhkEhFvYboR04kAPuYcyW30Xtc2EEfUsRgWmHIYWYLA3wT_j5-Pcjbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس بانک مرکزی: ان‌شاءالله مبلغ کالابرگ را افزایش می‌دهیم
🔹
نظر مجلس این است که کالابرگ برای دهک‌های پایین افزایش پیدا کند و دراین‌باره درحال تصمیم‌گیری هستیم. @Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/457101" target="_blank">📅 22:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457100">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55a70545bc.mp4?token=bmZxs0FqCRdL4xOMUpEHaUEhCTdAEtOhPAsGI2XKBpISGKbWhg4LgnVLdOzDbnxZASJDE-HbnnvKZb3rJecyIFD-b-MJVU3jGWsfrXEbQ6qAZT6pah-0KOxolhJId7vz19AW6xWkMpAsqUTLPeLYFOsa2C2BDCXwJRutgGRyDPjg1h4UndfEu36_R2G1jWjIAt4KVrATEvSjwis-lsqtqwFx-JogBLM88KjwOttw5amhmcLoKf4n0PRCvu_AyzOh8ePEFH6P7VpC1YbIX2MyQszhjzRvg2it8uwchKaTBAEspfZsi4gDrGSvkjhluOnQmCqPoS2kJ21B0v3jIKdmPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55a70545bc.mp4?token=bmZxs0FqCRdL4xOMUpEHaUEhCTdAEtOhPAsGI2XKBpISGKbWhg4LgnVLdOzDbnxZASJDE-HbnnvKZb3rJecyIFD-b-MJVU3jGWsfrXEbQ6qAZT6pah-0KOxolhJId7vz19AW6xWkMpAsqUTLPeLYFOsa2C2BDCXwJRutgGRyDPjg1h4UndfEu36_R2G1jWjIAt4KVrATEvSjwis-lsqtqwFx-JogBLM88KjwOttw5amhmcLoKf4n0PRCvu_AyzOh8ePEFH6P7VpC1YbIX2MyQszhjzRvg2it8uwchKaTBAEspfZsi4gDrGSvkjhluOnQmCqPoS2kJ21B0v3jIKdmPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: ماه گذشته شتاب تورم را نصف کردیم
🔹
البته این به معنای کاهش تورم نیست بلکه شتاب رشد تورم گرفته شده است؛ یعنی احتمال می‌دهیم تورم این ماه با ماه گذشته خیلی تفاوت نکند.
🔹
تورم در کالاهای اساسی هم مربوط به حذف ارز ترجیحی بود و طبیعی بود. @Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/457100" target="_blank">📅 22:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457093">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iBoPNUUwkMFmUZhczZYK_FR_eXDSqT7NJSLv796DPBYOeQh3BZ3F28zBSpWBg-TDnQYCPGYrdCGcMi-fgAhLjeCcIYyTFieu1JLnSh41MlbCJWy0sp7dMdxLcjJaH8dcoTcBgmQH3jHW9sfI02ZanbDv6pXpyT5TGTsjx2iQtlnQlYXL2POwy9Wk8SDhhIIOVBhaC8ISGT1sj1eOlfRMjPXS6HBCCNFcnBkyzCVPFQY_Rrar3LtTSccgjJK1Y5e9DWXwrukfh5ijTekpvc8HJC3Mo1keCGCsv6v9hmUQlx-cDFTWd2IeNG5VZHx8iQhXkpSOaINcqvtnGatLipkwvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RD73j2cpEpCNtIw5KylRlnikMqxAtrAnXwJ4zf5ETAvbgJ67P8Fbh9hDwScp3SdpRBA9h6jHucaTvyT8pH2Cxsa7YQvHyFDE1BgK1tUWntLuk-k9n1eXq4PkAOA18FhKwz56Ql1pxthmuwMNbGJ0EMM6Y66onOF1QZ5ecHKVFE794JATspYS-ncSqaL9t1jXoWkfuJgPG1a87r1dATMcf7sDvLYjVSJ2WTevq_sOajchliz8mGg0TzqXukQs_ltBLGmqUFPZDgMmnLutKVLoQ2Yj8kJa1mY2ho7cNPv8DlgtXAWgjyxUV7XrfbQgNubrE76lMl7jcxgJXrV4DeMD4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZiGe2IrbwDyTSyHWG3ab9LzJPoPivlG3C1pYW4uPJ8WzoHWz4CKQOmAdXQ9yEZQ6g_rNbeHdII27NNkHkVNIZltTjxHVQo8UOMw30xGmsVG22MJTxA80HbddVHv0t9zgMyTPIyJxRWW7BvF2MIBikf5AWnRyW3pRBAKgwk5qiY8O_AG0G2_NGUM3MKunwwoyrd_4cMrXhH6IG0jJgq_yLKz-wnH-X7YRXChf1LGLk6vUk9IufT_CI67zmMJpjMMz9CTs1UmSUSw30D2uR1xkVibvSnzgS4l_GhZtUDpOSVze-nPtqe_3GaxqTrk3DfaYoey0BYKkuuTniY4mcyc8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fca1k4X088f2OpkxjrP19g84lEqiYfXPcQOb5HhFiXK65iZBCCPba3h-FecevF4ftVhJf4FNj2gOpZPG2rbFAwEkNNWHeVigXLka51iCpEKdbkexe1tVnD7ct4knmQG951CSINOQPqK-EK4avU8D_wBDpeUlWY7ZZkU08GhP8d-dw_YIERjy7IC65F9JuaEmWoDpfa4oPXSg-Rl5TT84NS73x0no3v_U0jO-z0cQqGrD9sZtXOO9klwSwzCBcJ1P1ttS_O8QkWPHAK30q1Hq36V5-BB9NH80LZSfVt30o78ZM_GXsuCmBt3cGDTG0fPskWrW8I8esUsF3w96EkHrSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EdR68_bubjHUR-SkyiWhxdbLws7kQ2T6wkNZU1e5MX4dt4zkx5mVrBWYCCpYxHC2eQBO6UvI51tzPWZJajwjra20750_iP5K4sQAkizlQkSp07R0eRNCRAlIcMcDBmKEvwazLMhs9SgJb4eJo9bJ_ecW2q-QW5ojJ-z_iWhNVIE7mXdmb3VVSFZDdssxJ9RhbO9dX1YlNS6-foDZIs26gR47HBNyl_OI9XfbV6dWF4Bln2iYaxZlZzSGdFKNSNp26vHjczcZBGg0EzxtACoNjnH7JMNuFW2QGGrJ8EBp-eDawnnSRZw3HIIEZFMYU7IrqCdyBZOraAdg_kLyWWD3oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GF9m6-PRgO2opEt8eoLMEwvfQJ1sysTFDtcmSGxBEyolezhOGzJsg1mDxU9wEUwvv5_EnmmJRui7DwxLSDNzpsTNTHT-mOq_whc5Pct8YOTs2QtJUPyEmM4A1UiXzY-D2ETaFXwkUGyxRIioZ_OVWQioX9BdtgHhblw5HLcA7eWTvDcfQUhWoPYk36HtCRRsvlQTwTXJ4LngmjmSuHT87A9oHG7lXewSUZ-h9WGekKMWG5_t8Gh8D0AIqcCGgEav5K-C7zBub-UUMVZqIvyIadEvKQL60PYiVid24hosJ-DWyyD-F0ISPm7QjmDvQUDDFxNG6xa5cTUui9H_87fetw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PK3FZkBDC2XKI__TvL0QtstIsV1uAzniPjnay3ur8MO9Oi2_pXbr9FBalHAeM4pMjYsVZxgAZoeyXtJwFS5bE_HusXCFSamrA299bFEyhlzTketwre5NwGI9LyUx45yzJbJj_diMq5az9ONlPun_mZ5BIlE84LaQonw5jbjoFRc23nJVmNwMyUlp9jWwxUS59p1DUMVFDf8jkevK9o1JKlferVRMdLwOxb0pMpKy892v9ftMksQXfd1exyuQNk9CvXN3GJJwA_dM42znpb53h2YM2igyfML9G7ZGL7nVUOQJ9HQeZ4-WsQaV-XhLS3NiHRFxmB0bRXuZePJZJADBLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت چهلم رهبر شهید در قم
عکس:
حسین شاه بداغی
@Farsna</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/457093" target="_blank">📅 22:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457092">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cf0c47651.mp4?token=ZT0wKivQvoIwVE7Kl4u6PqrX1mdTZjhW9ssC5gJF3rwq2MX5xGS048BwYSXU1jaiMs5iRY9IakxbIE04ZJ2PIbpiNddFAxt0lrB3Aww4SggJu3bU3k-_z1EfqEVOdmlwLc6SITsW8muT2s3IDZKqXgWfXVhu3YJgWQDpLVz1uwMG-hM37pz6tg7i4IdkInJtTCklRJfz-yfI9KrS-7mFCarHcP-5he9sfUrq0FtLWj4rhLF55CjBFiCnc_os9yY4NXMJBSrpvlpjpoD2AS6lIYlt4cldjhCCEEXOenvfO9oK72tJLJ9yo92AWRu1ERvwu11qXf2Qi7ujVkr_vnh4jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cf0c47651.mp4?token=ZT0wKivQvoIwVE7Kl4u6PqrX1mdTZjhW9ssC5gJF3rwq2MX5xGS048BwYSXU1jaiMs5iRY9IakxbIE04ZJ2PIbpiNddFAxt0lrB3Aww4SggJu3bU3k-_z1EfqEVOdmlwLc6SITsW8muT2s3IDZKqXgWfXVhu3YJgWQDpLVz1uwMG-hM37pz6tg7i4IdkInJtTCklRJfz-yfI9KrS-7mFCarHcP-5he9sfUrq0FtLWj4rhLF55CjBFiCnc_os9yY4NXMJBSrpvlpjpoD2AS6lIYlt4cldjhCCEEXOenvfO9oK72tJLJ9yo92AWRu1ERvwu11qXf2Qi7ujVkr_vnh4jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: تاکنون چیزی از پول‌های بلوکه‌شده در راستای تفاهم‌نامه آزاد نشده است  @Farsna</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/457092" target="_blank">📅 22:32 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

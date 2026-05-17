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
<img src="https://cdn4.telesco.pe/file/akrNT6MUbyo4zgosE-HIRwpsjKINJds9zmQl1EFAETxfUz0GOaC756n4o0k0rMaQi3CJV9MToDWbdaCiWNl3BrWfhhMcigAA0mVksAkNYElSBdaHXG9ZdbKAJfGhsIBh2fRNW4cdNxgdk7r2tigzuDPhVHxGKEcLFWTV5sZm8U0iOU_MEfcJ_TO-4ZcCziRMASitLu6guf4gZFjODh1xDDgYMMFbzpzgRSXWDlm_Ff6rl7-w2IyN0ZhBJhihM8on4Cz-IN15iH5-2JUaOuNHplIXeJ_JHfd3vUrbfJ48wCHhnCYXDK_ccW_S1KyN5WIPIKDOmtDujEC-t0dMH9-Cpg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 16:29:40</div>
<hr>

<div class="tg-post" id="msg-436161">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlpPKq1ERkwtCZKTDqw4CFzULTWsU2Aho73M3CPpgKw7vAcfpp9IVjSMVlDIrB_hISoOi7ptSTyR-3gZem3ECXAH9xJZd7yyWn895gRySm5OQm5i1O_J-pE0hfyJ9vzzXpBkLQmMt34odVh2hKe3-dXPk-m8GllGZz36eprI5hd-DfQvQ1cnSjIVlNjFY2Wk2YE38D_UIb7cC5G7d9GGRJ5AtgH4p8lGPTuL6LZ7mgAsaWBZM_Jeub9HhNtTqkJaSO2vu1ijcMLZIyzWiMkaA4j0zgfzvYNqPdVh-TZ3VVhIOa2j58nFMSNGAKSUCqZEoVzzJF0tFroSACcGzq_w9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام قالیباف به‌مناسبت شهادت فرمانده گردان‌های القسام: شهادت الحداد در دوران آتش‌بس مُهر تأیید بدعهدی دشمن است
🔹
رئیس مجلس در پیامی به‌مناسبت شهادت عزالدین الحداد نوشت: بار دیگر دست جنایتکار رژیم صفاک صهیونی به خون مجاهدی بزرگ و نستوه آغشته شد و در زمانی که…</div>
<div class="tg-footer">👁️ 447 · <a href="https://t.me/farsna/436161" target="_blank">📅 16:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436160">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0c7e1bde8.mp4?token=BHBqbLc80ldHjdK3jAXyeKc7KcWNWuI17QL3Loblkm0NHjEJ7O3n0OFB58o5cc_RsdL_aarIS-6-4irkiuVVwDe_mU70yKVzNOr1d4u-q933G4e4BjxhBsV-FCYa_3KVIi0qnTjojXxsevCpqpWt2efJKbcZP0whj-tfk1pYHieAxD430871dtcypooIkP36frIKGjx_M6CLajNQixw5FKuowXPtb7gQhtDMQQEpdM3qdjEyCLO2Jjs1srG3szAUMzSmmvHmL1OpErz2jtF_L7f9xYy_icIHGidzuAGDTS5_VOm2cXm3VYIZ42f74GfzSCAqwgqB1yuPd_DaL5GCeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0c7e1bde8.mp4?token=BHBqbLc80ldHjdK3jAXyeKc7KcWNWuI17QL3Loblkm0NHjEJ7O3n0OFB58o5cc_RsdL_aarIS-6-4irkiuVVwDe_mU70yKVzNOr1d4u-q933G4e4BjxhBsV-FCYa_3KVIi0qnTjojXxsevCpqpWt2efJKbcZP0whj-tfk1pYHieAxD430871dtcypooIkP36frIKGjx_M6CLajNQixw5FKuowXPtb7gQhtDMQQEpdM3qdjEyCLO2Jjs1srG3szAUMzSmmvHmL1OpErz2jtF_L7f9xYy_icIHGidzuAGDTS5_VOm2cXm3VYIZ42f74GfzSCAqwgqB1yuPd_DaL5GCeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاجی بابایی، نایب‌رئیس مجلس: اگر دشمن به نفت ما حمله کند، کاری می‌کنیم تا مدت قابل توجهی هیچ کشور دنیا به نفت منطقه دسترسی نداشته باشد.
@Farsna</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/farsna/436160" target="_blank">📅 16:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436158">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27888157fb.mp4?token=feGI-Q2mku6F7ojTa1v_UdQkBqDG9ZxvGaXMYKvrKFhiwAShYRC0MV3DhwwV2HHl9SRiCafgHboDazfl0bpQGk5LbYiyWhYajcqux_ibGfaZL8dfASDcgnngQZEdb5S5cPG5Uwba5ZB4WGBZBXoXtxSJCBfPoqC1Dff6xALCWSSF_URXCjO5CNlIH4y01NQdEpZcQPHnsGAt6f6HecFFySYjerkk2fXT2AZHnU3CrVG_4AH5XLM7GxXXmzPXU0tYn0SwrOydZwqL173OpvkM6FzigsPG0iDGSMeJjhwVy9-xCaY14h7QjyzyMUYP0YC3FuEyAmn9Z85g_5tHoxRYoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27888157fb.mp4?token=feGI-Q2mku6F7ojTa1v_UdQkBqDG9ZxvGaXMYKvrKFhiwAShYRC0MV3DhwwV2HHl9SRiCafgHboDazfl0bpQGk5LbYiyWhYajcqux_ibGfaZL8dfASDcgnngQZEdb5S5cPG5Uwba5ZB4WGBZBXoXtxSJCBfPoqC1Dff6xALCWSSF_URXCjO5CNlIH4y01NQdEpZcQPHnsGAt6f6HecFFySYjerkk2fXT2AZHnU3CrVG_4AH5XLM7GxXXmzPXU0tYn0SwrOydZwqL173OpvkM6FzigsPG0iDGSMeJjhwVy9-xCaY14h7QjyzyMUYP0YC3FuEyAmn9Z85g_5tHoxRYoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جاری‌شدن سیلاب در خیابان‌های بجنورد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/farsna/436158" target="_blank">📅 16:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436151">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UUiYD2f20P2SnyUyJhOnQ-eEYTU2dKQamsDmKFEHm-QUr24slhcz4Bf_w00q5m6z_x8hqyDqTUsCKce03da272DO8hqQZzAEfrYiZ7aKEAglEGzEXpZ0EaHeUVKABl2I9KQbJJSAqOa3CXq0ssxPk6sbxlBETQrhnt9P8X7p4p8PTXSVHeShLo75ftNfqKOl7dSrkJ_AnQXUGefntFfKgldslYxDLE2yna7wHfTc4JU9JKRYj9_XRMFxJrlaHuSklRSsljSVDl1-5go5M14YAMzASL7ccv3vMyNILVBbHukSE4CGnQYJ9AESkNC3-TgSMLyMWPPXZPC7GHF6G-k_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xy6FL9HqkuCKx5lBL8o4ttgazjjPFQc2qeXYbrSsDRFVDjxc-EKS4aa-iVosamnnE_k_uBAEEYoOj335v1691rMbSPq9M1APDJCQnXJKQAc5-bLlT1PmG6IUP5w0QxWSEGonVxQKdbe2mFfvcG1ovY4tU-ucZc3AK4UzMneyIkV6EnmLL6F7GmMg_NcEfDbiYGJa9oLQD-wlr_mzN2re5cVGsOYNSHh7kfa-yXDZj6Gs6HPAsx3eCRYqb-oLPgfIjT2flaOttq4rC_OvxvNla7TltBx7Eppty5mg1_8dZjP39wx2iHlMWxgq66TSlA1Sl2bciRszENE79-jvuru6pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eqbkUQeN_XtMn1HX6ISR62lvuq78qCnV_rGJhIDO_ivUtloCOlE-tbOGlXaI6nqsKJYQ331LXpzqOryXAUkVNmxzk8gdLyxcAZvHTYqbepCp7T5EDfmIXLTPMbjHSxMsDtgYGVVmayZxSp0yYhD8c20zKx-iAex49Si2EgajqkS0XG7QH8XiBQgHrSOtZ57Hc24asfocZ1FfUX_5_4mxj0N0GkaYzpHDXMz5EHO-3dqm4TzdWye95K2zfC3Tk4bi76Fa_yLV_8MBNRYhwqbvG8rzEr0jNkb9F6mpO640qR0FQj8l0b52NHQGHu7_PL27u_TM-KDinPOyPWbEQ0exVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/no0hgBqH8xwzE_r9jOBzq2V-d7V5tZIomL2WeZbgq8e8Ys_ZVWpxttdTVbxLLtMy45MT6SUXAI2Pc5TmWytIWM-ZLCW4YBlPp67hoj_s5rAp26mexUYMyDtmu6nbQs9moZ-tOUdhU1WikguUm2tITHmFmWo-QNy3k63l6Y82qL27oF23-Y8dhKUHxWBvvPLg6ZZuF-LUN_Gq8LtNihLt1omLIyapQlEtmwyAUkly7mLaXrF6dHHkQy-Z4kULpmr7UXdZ_ndTzchz95ysRFFzgsuWtbR8PTU07RHAX-uPt5vtMMhOe-_Q63kmt6CaKyeKTlZDV_4UlwMNxkP1b1ZiCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h5Iug8w5xlaw8ht9HZ23aj9tSTNj-kKNErUhF8asFvmYU_DkKxtNxZwjqweP7WPcrXm3BKuI9i0oo7gfyDvyegE6Xj5CwZMrjX4WVZis8qtdP-1YAJf7uwdhHHacFC4Qm2uDIgFT2LFQqcCeBfKiHJJlQmX5qjZPes-j1s1cXGlpFSuiu4P-unuM1RTZDw8CyYGvifJJnuTDNUDnoDdWtEum0KSlWwe4-rZ09E9ytGqC_b7m1xEgDp2-aymA85fKie4nz7dkBuUvTrBNC63h5sW4mHOsfQgQNKN6lMMZQzaGpxvB9DZoLCKGbSOQ7kiKA4xL3IUevnLarjkq2v6yKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZWxHgUxCCGx8NbQzfuCA3JrToDuc9_NQwjd3mzATmUJfnmmgbIOjy7axgp92ANs5VCI9zSIrRiHBiaCE53xRtZbYcKaUcm9g-MRDETvuY2sfgxGO9BZ_NRQF1t-sNvtZgAjlJqo7Zm4VkTb86ojLyyOxCnGfauYLcyREf-k1pASNi0nsfTXvuvCiZOKyeA2NxcLyJP7xGLJ_Ixv-juSVzdRxLnfZnOAkTWQAs9JylI_b4UDBGsAwVC7cjz5vxCVFc5GffRMBPDvbAD9sa0guDbL1RFOSQVmsIeufQae9Avq_ZhswUjnQsc3Wkbmpl3B8Q7RrHxlUWJHh_lH6RlcNkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_i6wuJeyoV13JVJ_okWUr5eY1kEDTZZ0IWg80SLG9P9R4Is3X-F30entbJ4e8oQk7Bd-xLK5MAi9yI55w_yHAIKy0zTu7VCQK1BQK7PnZJ3-XYfwhVtXYWGPFuzxzsdLRTTY3YiQVE9kb4mVYff2op-aM0ajFIplyugiZA1gzoNSamF3FUIvo_iqGUCjKs0QgtO5sr3q90Ji5TnZ207C01ojUuAV2BQmg6PSd8NfLakjmvMEcMGhQRD3NdzWnnzaLTV_1ITZqh7jduKsMCU6aCXVaKLms1LxdadxW5sAffFUns0ng6L4ciB4Yq4yj1VvNkAQ4nQgPLYrRO5lssZ_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مزارع البرز غرق عطر گل محمدی
عکس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/farsna/436151" target="_blank">📅 16:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436150">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef687a9d1.mp4?token=CJrCOSPeU0V_R1Wm8etev4Vv_MIxNThblyGYRUbz9-gjpIGTBjPnxeZFbbj6_wKmd0NUDJYflnrMVs4X77TaTKUfem9k8EUIdWeYUrxnZ_-k2R7_Ti132IVYU2ide0BfTSxZAmKZJqyAJZiBrVI35YBW6UPIPTDYc5BDqAr2SW-8rPi8bSK5-Ng3wi0ZZcgxwhSiXtiO2rTZNWQCbBnygNXi0PPu-pjQz_epdY-IpDJVlBeDM0TpM3Linq32UM6NgsRT0qOf7Syk_wI_pQzUL8z6eh4DpzpOxrpNFbcHycxTYw0K88DidMIBmYbSAelXFfKDU9pA6jzl3i5d2L_Bew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef687a9d1.mp4?token=CJrCOSPeU0V_R1Wm8etev4Vv_MIxNThblyGYRUbz9-gjpIGTBjPnxeZFbbj6_wKmd0NUDJYflnrMVs4X77TaTKUfem9k8EUIdWeYUrxnZ_-k2R7_Ti132IVYU2ide0BfTSxZAmKZJqyAJZiBrVI35YBW6UPIPTDYc5BDqAr2SW-8rPi8bSK5-Ng3wi0ZZcgxwhSiXtiO2rTZNWQCbBnygNXi0PPu-pjQz_epdY-IpDJVlBeDM0TpM3Linq32UM6NgsRT0qOf7Syk_wI_pQzUL8z6eh4DpzpOxrpNFbcHycxTYw0K88DidMIBmYbSAelXFfKDU9pA6jzl3i5d2L_Bew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
|
توضیحات آیت‌الله صفایی بوشهری عضو مجلس خبرگان درباره محل درآمد رهبر شهید انقلاب
@rahbari_plus</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/farsna/436150" target="_blank">📅 16:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436149">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1IEUEMWOE2mSQWb8vITQg58GqhQ3KSS2PkZWEU3GzEplm_CUKyWBlDV6hIPaoX-bADXnZ6gLgp8o6J0sKtMuDLW7jmdGXL7YZVTLfFvnAX_wLn2OjYHsgB79gmlJRBtDUbVhhl86HenZNAcUXZjrktX4i5yARgeKZFgM5miCnPFyFa5V6VizpT5wdQ-ImS-0xASkDE3k4csZP18ZNYU2vIJdu1rb_VMLilLgnRRMX9klc1g-SwSGxF_jjXWVF6n65z9FIV0mvLE2zmk04IVcnqPgSLo5zC1FJFLOemT-iq_HmGHsMewSIzkM9lUlnan7KjWAFYgHHHsI_6z2c8A8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور برزیل: من با جنگ آمریکا علیه ایران مخالفم و ترامپ هم می‌داند
🔹
داسیلوا: ترامپ می‌داند که من با جنگ علیه ایران و مداخله در ونزوئلا مخالفم و نسل‌کشی در فلسطین را هم محکوم می‌کنم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/farsna/436149" target="_blank">📅 15:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436144">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5AnC0Qgsk_a4DTU7QrmtLnlN5FyWsspwKbFMWtASUs_MmiCeeJyBqIjzgaQIAhLGmXqQeKrMswWxL_T3p4G8HxhNz7lBLvu3BrPTbh26F60l0hqHQ5EorCqOD1NrKvyc0n6VNUA-vE2tyzhPKpXOrlyLj-jjeQuo6QAqVR3YSYi-Ai5YrsXhfCgadWFPjgGzk9jDuHUSyXz8HiPda3COOtzJiqXxTE9nksi1GqbKDjrQIo_O15eSgjLMSWyC3t8yh9fZJZ9SgwzLaS6qBN50hSNUlConKZ2qPKM7Iuef4JT1CvOXovy8Yck8TrrZubVfVE4vbze_JEeIKS2V5KC4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bM0fge9ErvbzrDy5B0Wp8JqAGYcQ4XYlFzgJHu9oFiQphIne13o865eZSOAoyETKiap8sdivZI5xehNiVKc3jdx3xPSpEIolwI8sTqA6NXrQ-VRcxq_-2oY9DWcvprLp49IpAY6EBVKWyydyC4GmaGgnOrW-vcfyKw6VMfVyc9wqougxE3Wl756Psc3K5YnOQv16zmfp0brrMIQtz78E8XC-WWWkEsmZw49XWuCdTkmaQiknBj7cwu3o9UWuNZVBCLp6KwtevhEZQKBOoC8ZeL6sE9cO4ntdLoSIIunGVtuN7hd4jmt3T7li4gYoCYY5xsYQWqn47qqBMupRWvSCeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sQfJZfL6tyc8gaSDwY6pfc23hAzUPjpQ0UhHWF9Aa3dE8OV9dA-IQhROFaP_wZmGQCustw9aXgShu_M8NhP7aAEt-3ktAQTqcGiwsd86dg7TUsRCwX3pzGUsJZ4lvwn8D-m5U_bQEolf1-fOj5HaDcMoRQyXf2Vgr6ChKsdmF5_crESB1nXvxRazWACYxIcxUs3gMLt7vGMRg8wYFKe1xGkvTDMY8w73eoQlGSsRV7gfV29OK4of8wasPBIY4pQ8WDI4wOK9VnnCfcFn_WaCCLXMCN-qD6xdGhGYH7mc8Hane7LQ19nvwwoWmQjttnOIo-yM6z3-lATxck3vAUCauA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tEuM716P4K388EMPHGSRplA_ioi9DA6Z0qn-G5cNk2oDTlOwwT-YAfurMIdZ4A2eXUnkvMFMjtCtcACuE94QwvN8JUvGsDK5m92Wv6AiKknuWS1MVTDLRDSENbhBBKQGAINsxrS5uOEKI3M596KLSdVmA7ZAoTa_X2HahSJf-yDHzPI-V0_7exueXU1MX-MMMKLB8vKQf4Ihhm0cdkGj-TQuzashb0n8P1O0fJo51zySPJYFEpccp-Fe1OQiOM4687gfN7wopViJhDYdAPxfQQXfYkFhhWWPwNTGe8bM_er98GRdfKKZsv3xn5I_YWGD_jL4u3mdcKpeZmWH4nHViw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MocvlpPdF4D28gVL-cqMZaqBVGu7Ckh1QQlgYiJwLOoQ2JjrL1CVk5ud1VH4vz5tPBFTaWN2_v-qDOxUzTP-IXtfMJrELwdyZ4dfGwlwNIg8YLKQTra-QRiDLVQWwFjhEmjHO7AgDuL9DhZPW5JqraefZ2uGfEXukpLwiuNjNCzeW6Ic9Q5q-H2i_4YGENMsXHpD6nCwyP8ZgXLXRxooHB-EzaAAgm47S-iNVipkhS9O4U6dFE9Ewn2zZ2sjyFVImBafIbNsbH4pf0mhngp3bNxcuLdoMQ3ISlujHJ9fo_1dj-soAVkAaGKWjk9hZkbPR21TK5arVFgtnUFtkaA2Hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور قلعه‌نویی در مسجد جمکران
@Farsna</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/farsna/436144" target="_blank">📅 15:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436143">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdYqMDikG0iQ1rXAB6nlxJqAPBoSwkcQfAFafDpYSVIgtONwn84nUooZMa9pPKdokqoGxdZTgg-KBfeU69wo_c2KPmGofOfrFq_esJggtHjnssLg-yAA590I199lJ8QAIKOxlnFr6RlsmXeS6Nh3OlRJ8AgiHwIMJYVl0skVB3UiHR70T8mfVjrbdkjuC2Wf5F2GnshW1ve_sr_YcGaHhH6sgulV6_XmvOEqHR93J_hkMogXlveFotRdqdTMuDNAE-VNPO8YhpjTqMwbditHT0QDfL-aJmO3c3qWTgKboHIly2r5KEmcfV6Ow3Bax4NbmB1hPfdtelRBZFxm7WxH2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریزفاکتور دور زدن محاصرهٔ آمریکا با کمک میانجی
🔹
براساس نامهٔ معاونت اتاق بازرگانی، طبق داده‌های دریافتی از سفارت ایران در پاکستان، مسیر کراچی به مرزهای ایران درحال تبدیل‌شدن به یکی از گزینه‌های جدی برای دور زدن محاصرهٔ دریایی آمریکا است.
🔹
طبق این نامه هزینه‌های این اقدام شامل هزینهٔ بندری، خط کشتیرانی، سپردهٔ تضمین، ترخیص و حمل از کراچی به مرز ریمدان است.
🔹
پاکستان همزمان سیاست کاهش تعرفه‌های بندری در گوادر را آغاز کرده است تا بخشی از بار ترانزیتی ایران را از مسیر امارات به‌سمت بنادر پاکستانی منتقل کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/farsna/436143" target="_blank">📅 15:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436142">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
حزب‌الله: تجمعی از سربازان دشمن اسرائیلی را در چادری هدف قرار دادیم و تیم‌های تخلیهٔ مجروحان دیده شدند.
@Farsna</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/farsna/436142" target="_blank">📅 15:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436141">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDIIkWYfuTfC2YBCLjknsN53C4XP7nSzQ3zaigo87GCOSwy1yOochfx_wEx-zBKC7sJnmvaYPKUBRUMul8B05W6frSkccj53oJHObHA_jc-qFEoEIGslACndPulHo6cBxtFleO474RKLQyMno5szVsqhE7r6j7HPC8dMT7inNQAtSo6FGRz89B-igrM6MIhpIuihq6ofQwl7VpMvn1WPanFmGbcXNeZVw3TZQuokOu8Ij4kLLPMorZDJ7l9ifM9_AohWNHDsPheQUPXjC2QoQh0_rfW1ekB7J5H7w6zjObpCQQ7T1_v8dXslSgzzq81ziIKA_KsIyLSmyijmw3SJfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان خواستار آتش‌بس فوری در غزه شد
🔹
رئیس‌جمهور پاکستان: خواستار آتش‌بس فوری و پایدار در غزه هستیم. رژیم صهیونیستی باید پاسخ‌گوی جنایت‌های خود باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/farsna/436141" target="_blank">📅 15:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436140">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/340656f1cd.mp4?token=DJ7jqXTonD6PZtPmVOuX0RqWUVTc0SkdJ8f5aarLpq_aTLbkfLK-xP0AV8b1EbG1aQCXxg6QcESN5kyYrsJn7uXRfNsfFxcprd7l-kypveBpX33DHu4aT8VdKlSdGMTJTYKuY4X3-GTcZqFReMCWUNzUBzhEa5GHdybch4Pu6qZmV6tUtIdwdWLnjcevxaZweJZEJos3q-K52Td9ZtQIhtRVhEEs5WDoZDW3_dZhYCX6YE4w4Z1j-xAuCP0YJFscs8gHcx63ch0wXQFs1WWqQbq88WVPDrhPu6qynO-wW1QR-zqu_MEgwraLjb85tGjZF4csu2SrM_mASoAVciYX7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/340656f1cd.mp4?token=DJ7jqXTonD6PZtPmVOuX0RqWUVTc0SkdJ8f5aarLpq_aTLbkfLK-xP0AV8b1EbG1aQCXxg6QcESN5kyYrsJn7uXRfNsfFxcprd7l-kypveBpX33DHu4aT8VdKlSdGMTJTYKuY4X3-GTcZqFReMCWUNzUBzhEa5GHdybch4Pu6qZmV6tUtIdwdWLnjcevxaZweJZEJos3q-K52Td9ZtQIhtRVhEEs5WDoZDW3_dZhYCX6YE4w4Z1j-xAuCP0YJFscs8gHcx63ch0wXQFs1WWqQbq88WVPDrhPu6qynO-wW1QR-zqu_MEgwraLjb85tGjZF4csu2SrM_mASoAVciYX7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجهیزات ارتباطی صهیونیست‌ها هم از حملات دقیق حزب‌الله در امان نیست
@Farsna</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/farsna/436140" target="_blank">📅 15:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436133">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t_wwyZ_j-BDXm42CUQ5ZegHATN3QQNTicr2OKftM7aualKZf0t06qp0VELOoPUOlCMJCBwECpAdQ_xUiuzZNtEtjKQoWUAuCbTN66uXXj1UWHLUEWz3QMWygN4sS4lNqAr2tkqV6d8GdQv4zbxuhQbOy8e43_uoIhZbBA4xWIlhNCaoqQpZ897rd-8hko9F2X6RBtDsIelAk6NMI-BfoPmk7LyNMaiQCpa-sldEVHsObiImMjD4etkpev3APKtIqwgIkugyyLczZvFrTKuHc-kKzTCmTdmR8GM2oMQYxHnhcvTJTTiwV283NO48Gj_Z_x0Dr57V06Yz-pSMuzhY_vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4EghAjnH8uiSmFThfP4KINwU-dzGYSyjJeJYWrbNF-pjICO0CqIVnDIBA3x_9b5_LPlm0cX2gxN5V38YHkBw-e82QuPh12eKArc1JzXBXtqVEQAFM_2Gbd3a6qrVbLzVyOK_jIB3efFoiUf-zOydp1qTvd3YdfG7FWfd4bMdn0lW1r2x-qAF3qvwddRbSOpMptvpc9kAiAkGOBiMBqaLd4cP-rUTnO9OXzGrdms0Wz1ziqAC5HrFmG02cL1X6teGFRS9pjtRKiIkdwNJ9bHqS8u2xJT9k_s-Ze0oMs7ccC_r1AhfCdI1p5Qzw2BF5y_BYk_qZzgs7IvErKdc5ejYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rhC1JImoH7MZKrFpjNcIAeYec1K96MbngWR3KrOcVL4ARmYE5lg2K2nB-H96tygrUFertoWCPVerHrjnG8v_sQ2QqjXlQdV-aWvr5YMrughpCMOZNHk8EoPFHel_nreKaQx3ftD4FBeI1keCanjV9-q0wX95fboE9BHegZ59JyfkICPbJGui6nA_U1NirIS_okGHDFTmPY_9KlTwKBlhbBljwporMEbCbeHYoXjkpUa_tNLvlRkDmIcVflJDnBcHIA6lNObAU2b5WOJhmUaGbIf3MHEZk4dOgH2Y3K0H4TWSRRoAiv2hQ1bJKLeLAzvsYqIWKawGI0EhAbD6UU0jpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RrScIHDMcCxgs8P8ophXfKG4UbI3TNCSsrGN5fvPIjTYwZ8-jWYOf7RFlm_bfRrRBcdjVGt4Czi2h0SpGTFqD_uT-euFJQdfxCu2DSubEDdZ7C7DAH0ThC4DlT9ArhYp5Ezwtq_ImDG3yT_wGX4RcC44R_20pXdFSCEvWbDk0XnZVwMHu8OATj552UzzwNTzWmgS4FScoJqkhPWw8FGsHZRIUlNmP55cQJ_cdIYNwTv_M3n2ddT9ziorfEByygg4aNAwnnSRERgjM3Sl-BsLppFsDMoUR7AYwYr8cuPBUHL_t_KPGIZMBVWNjrOwmC3tUYlmDGrDCLKFoLlpAm85AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JA9zqv9wTwzF8Uq18uAmNQz9Si7gvcBDQVBPhriAFH5Xnro34NJLc8P04QEZyfa9PEsioNlUGNHQ2jlAftZOf9BacU60tXr_YOlV9tUAxHv66hWd7KxYxhVMxcQGOvUZZutqpxAPgfbUa8K9o8cA_OkFhExKrkq7XhAY4M4D38BeYhYisTpBpwOF5Nz_l5iAOMvtQ56cHzYJft7pCXUVoc1KRlzc1aBPbCTJ1jqJzu0QaG5ydQB48T1brPa-srRx-i0-QPHnLmzvH669VWjQTxzqc6-ZyXl0_eHibtYFCOPAjNBCpfGg4Iz6jUyq6QzajP5jeFFXNXw-7YMT0I1a8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y-3rNaCwfmhCpl_OVhQs_26dA7IHbYDOy7w-i6dDE8N3GzhI8hh_MhBO9saE70PFSaKe65iCtKS-VqFMAJXXx-n76VG4XcE_c0qVO9YrTOmPs_jvre6Izz8085mOmHkiftg6_jYkEveYeyHJcIpv4gr2nyQBKvU3p7oHVuv2XKytGsh6q6AchwNtBLyQFGQESyRFpEkR2cbLJIYrzNxaWaCzS-k5AGGK5arCB17C6ZEezZi2BCIg5uEfan86zQ0ZCk_3HpcYdWSTXxLcBfP8h1JyiVj3W_m7tXluH1emHUXAcJKVh3IjcXJvumLdZpQA3SQjlqY2Ec09cwG-hapjfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H92rnFhDjOsCJT4OVtwyookqxYuJMArrCjyVEYeu_Hsjw_BmLGzWaIqRFsIuLsEb5Roj5QJKi_e5xb9xvgQEz7772DqfP2-1XgyJvdTP-t_Iu4ML9_aC4Sd5Ug_oRbWCeD0XM9Qr1uSoOrLU1OFal5AipqCSc3TpyFVwcY6paXLG2EjjrmdpucRse2pg3qUMpP6pgIiNzcc0aCG66zZHGg4KdHbCKHgs8YrztC35H6NK2EEzlCaom7NTUQ6ko-0WLN8ZOPfd-lP0NPu50eoI60n2mLbut2TKEUlqfgeqaxET19fmbn0Q3Ok96uQxnNZ9k5sTorObc_dG4b_x0pImoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مرمتِ باغ گیاه شناسی ارم شیراز
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/farsna/436133" target="_blank">📅 15:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436132">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44fda16571.mp4?token=fJ0TR49wWQJzao5QkQziQEpxOBHkKBFD8gWX7waVsMF87QofCPolf94t3qxI3JmApSrWhHEC17J3HWcOrUyKWPMzk2Kj6zG-ocSJCZ7o_lFaiQZ2XPUAOimQ73iJ3F4HiPgpLXFspf_1ul3FMTAMctuy6IZ5ntiel74gmrmmtcSGwRckYouVfrj574R-QkPq1N30pD6T57RUunIHAF8hXyeJbesuMIb66x9f6RoFyjlPjNDQBmmohH_5imn0csOtJdfv0rCQkmjGgvi5_ESu2H1MdGdJ0cHBfcLb1kG9iKx765_jsby69Vc_rM2lnQReNCg6gkndF-PCyO1HRb2Q8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44fda16571.mp4?token=fJ0TR49wWQJzao5QkQziQEpxOBHkKBFD8gWX7waVsMF87QofCPolf94t3qxI3JmApSrWhHEC17J3HWcOrUyKWPMzk2Kj6zG-ocSJCZ7o_lFaiQZ2XPUAOimQ73iJ3F4HiPgpLXFspf_1ul3FMTAMctuy6IZ5ntiel74gmrmmtcSGwRckYouVfrj574R-QkPq1N30pD6T57RUunIHAF8hXyeJbesuMIb66x9f6RoFyjlPjNDQBmmohH_5imn0csOtJdfv0rCQkmjGgvi5_ESu2H1MdGdJ0cHBfcLb1kG9iKx765_jsby69Vc_rM2lnQReNCg6gkndF-PCyO1HRb2Q8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رکوردشکنی وزنه‌بردار ایران
🔹
علیرضا یوسفی با مهار وزنه ۲۶۱ کیلوگرمی، ضمن شکستن رکورد دوضرب جهان، مدال طلای دوضرب، برنز یک‌ضرب و نقرۀ مجموع مسابقات قهرمانی آسیا را کسب کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/farsna/436132" target="_blank">📅 15:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436131">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3ec27fb9.mp4?token=QVvr7ohJDdCP7gn1_SH9NfBYr_966hH48N-zXN1GknZe5AaCirenWcOskq1E-cigJOEfxxgEe4D5GJlhDwyQ_mz-JZ-gM3THAyNyVTC87seucoy-KnAXQxGvU05PseuQaoaM2VXhsyMD8mydmKJVOhQkGXBH9iAWJ0U5uni6eDk5XexiR9ByhRwyW1rrBalmGYNiegGTrk5BR7eKSc96y3UEMZuVjmr1GJgzoeH3AXbAeATwlKz6cNSkiCv-g16Z5aLKKRQ2DL9-uLTEmGGgs7WFt5iDdr4TAVB0Y6ydNiy7E0PSNRlw3xz2M238vhMyHIJhq-rkZYHc9njLlV59i6vWhP0rmmn5Fe0GfTdpNOMWaOBbITXO7cORAJ4K1JpVVqgXsSSxljYxqvs3TnPGzlGzfjS4fzlElWGxCd-sh2EF_8TUMuYyTzpMkFaHrztSjUIEnriabCPm_sqsiZzO9IQjYY-2BB_jsCn-8nOS86-s2TYit0XGTZkmmRSvEYRfrai0OxXNlxYrem67LWbgBYCluByJPXkAKkjo9QxsTAwyxVwtPOwRntbbBzP_qFUvQQ1v_XefWQCprfJSkLq8H-UKMwgyEB4EOEGR8UWBoR2vJM12hmXoBCMrIXY1S90Xm3wJsKtHLqCW-fh3YSypM4nsW7dobMssCCCactY1cR4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3ec27fb9.mp4?token=QVvr7ohJDdCP7gn1_SH9NfBYr_966hH48N-zXN1GknZe5AaCirenWcOskq1E-cigJOEfxxgEe4D5GJlhDwyQ_mz-JZ-gM3THAyNyVTC87seucoy-KnAXQxGvU05PseuQaoaM2VXhsyMD8mydmKJVOhQkGXBH9iAWJ0U5uni6eDk5XexiR9ByhRwyW1rrBalmGYNiegGTrk5BR7eKSc96y3UEMZuVjmr1GJgzoeH3AXbAeATwlKz6cNSkiCv-g16Z5aLKKRQ2DL9-uLTEmGGgs7WFt5iDdr4TAVB0Y6ydNiy7E0PSNRlw3xz2M238vhMyHIJhq-rkZYHc9njLlV59i6vWhP0rmmn5Fe0GfTdpNOMWaOBbITXO7cORAJ4K1JpVVqgXsSSxljYxqvs3TnPGzlGzfjS4fzlElWGxCd-sh2EF_8TUMuYyTzpMkFaHrztSjUIEnriabCPm_sqsiZzO9IQjYY-2BB_jsCn-8nOS86-s2TYit0XGTZkmmRSvEYRfrai0OxXNlxYrem67LWbgBYCluByJPXkAKkjo9QxsTAwyxVwtPOwRntbbBzP_qFUvQQ1v_XefWQCprfJSkLq8H-UKMwgyEB4EOEGR8UWBoR2vJM12hmXoBCMrIXY1S90Xm3wJsKtHLqCW-fh3YSypM4nsW7dobMssCCCactY1cR4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاجات دنیایی را از امام جواد(ع) بخواهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/farsna/436131" target="_blank">📅 15:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436130">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/259c769a28.mp4?token=QEkmQ4NmiNy5pXG-HoSS8nWeouBPq9X-8zJIgWfcURfBIYs51a3vcdI3md1sgroYcr_WAO57r4qe1mPXJTLVOJ-2yxKtQkpiWQ6CZyqC7g9YlD278hIaqb_mgbI8ue1yZgOPC_d8PO3J7v836twWYC6EoMIntFNWXBBbNtyCl1jn4xveHDeVzWf7OSO6rDcM1GhnNnWB6S5UvCZ3YFkP7YcEqOkiC0Kmtuspo69PmJNw5mfFhCZvUqzrlQz7eRhb_KZuqKFYhocXC49TsJUbW1d-kzsTIFQFMr_dA8p3Q5ugC2_jGQuipP2jBkzsYGkOuc-EzyLgSyaTUvaEz7IHTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/259c769a28.mp4?token=QEkmQ4NmiNy5pXG-HoSS8nWeouBPq9X-8zJIgWfcURfBIYs51a3vcdI3md1sgroYcr_WAO57r4qe1mPXJTLVOJ-2yxKtQkpiWQ6CZyqC7g9YlD278hIaqb_mgbI8ue1yZgOPC_d8PO3J7v836twWYC6EoMIntFNWXBBbNtyCl1jn4xveHDeVzWf7OSO6rDcM1GhnNnWB6S5UvCZ3YFkP7YcEqOkiC0Kmtuspo69PmJNw5mfFhCZvUqzrlQz7eRhb_KZuqKFYhocXC49TsJUbW1d-kzsTIFQFMr_dA8p3Q5ugC2_jGQuipP2jBkzsYGkOuc-EzyLgSyaTUvaEz7IHTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت فرزند شهید سردار نائینی از روزهای آخر زندگی پدرش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/farsna/436130" target="_blank">📅 15:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436129">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">احتمال شنیدن صدای انفجار کنترل‌شده در اصفهان
🔹
سپاه اصفهان: به‌دلیل انفجار کنترل‌شدهٔ مهمات در محدودهٔ نصرآباد و میمه تا فردا، احتمال شنیده‌شدن صدای ناشی از این انفجارها وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/farsna/436129" target="_blank">📅 14:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436128">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6ef998be6.mp4?token=beOtilvV9CgeJp0uU1UUck5W-LLiL7jna50tpqEC-LLNcT_e1JAamhLXDVtZTJAg1Vl_xzj-8Q7EyvW0zwEAcPiAes7r_O-BONQP-JQySKGI5Q3stRBh8dxqKbEf1xqbEyEIL3IvoSTJUliKwzPf71SxBdrKRbikxyecZ0G0Msw1eEfJZTKaQ9fj-irneKfuqgdiuErTr_rkjLruhAdchtlLztLeBgLi4ejqAE9CaeRBbdr-GQB8jLe8xC4b-uhB3P1tZ0ci6YcjHhOBy6bFNIfQg95aMAKNdmqh5rA5Jv-JsbMGjTNVK2Gr4HlNiCMsLD46b130UcDSCoJZiLm0rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6ef998be6.mp4?token=beOtilvV9CgeJp0uU1UUck5W-LLiL7jna50tpqEC-LLNcT_e1JAamhLXDVtZTJAg1Vl_xzj-8Q7EyvW0zwEAcPiAes7r_O-BONQP-JQySKGI5Q3stRBh8dxqKbEf1xqbEyEIL3IvoSTJUliKwzPf71SxBdrKRbikxyecZ0G0Msw1eEfJZTKaQ9fj-irneKfuqgdiuErTr_rkjLruhAdchtlLztLeBgLi4ejqAE9CaeRBbdr-GQB8jLe8xC4b-uhB3P1tZ0ci6YcjHhOBy6bFNIfQg95aMAKNdmqh5rA5Jv-JsbMGjTNVK2Gr4HlNiCMsLD46b130UcDSCoJZiLm0rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشاورزی: امیدوارم سازمان برنامه و بودجه زودتر پول گندم‌کاران را پرداخت کند.  @Farsna</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/farsna/436128" target="_blank">📅 14:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436127">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8837ced8eb.mp4?token=XX753XY-VdD9TxTVW27hfzgrMIJGTPSn_xaziuU_TI382XppxjNTaG8IB7WMOuFTXr1LqkeWKryTyJI4691fS-2ZNFi1c784A_EphHcKVtsNahyfxfCMaynrF18QTrSV2C5be_80iWhfEnGiog0nuFg2LH3rD7-yM3zIqYz6QzfrvqxBj2vPsMiAzSRe2rP8Et5_8fUFFAeDZPZAVqess2B-NIyCpnlODg6diNIrgYO2VbK62i_ci_izkO22POlD6qvM5oxMKKybgiBLMVgQn7FqJvFsNfToAhK8Rx10OrEIIc2iSV65hrQSGo_H5rtl2rAX1lJZsfoU8roQpj7seg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8837ced8eb.mp4?token=XX753XY-VdD9TxTVW27hfzgrMIJGTPSn_xaziuU_TI382XppxjNTaG8IB7WMOuFTXr1LqkeWKryTyJI4691fS-2ZNFi1c784A_EphHcKVtsNahyfxfCMaynrF18QTrSV2C5be_80iWhfEnGiog0nuFg2LH3rD7-yM3zIqYz6QzfrvqxBj2vPsMiAzSRe2rP8Et5_8fUFFAeDZPZAVqess2B-NIyCpnlODg6diNIrgYO2VbK62i_ci_izkO22POlD6qvM5oxMKKybgiBLMVgQn7FqJvFsNfToAhK8Rx10OrEIIc2iSV65hrQSGo_H5rtl2rAX1lJZsfoU8roQpj7seg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گندم به بازار سیاه رفت!
🔹
رئیس بنیاد ملی گندم‌کاران: در حالی که وضعیت تولید گندم امسال بهتر از پارسال ارزیابی شده تا امروز یک میلیون و ۴۰۰ هزار تن از کشاورزان خریداری شده که نسبت به پارسال ۲۸۰ هزار تن کمتر خریداری شده.
🔹
کارشناس کشاورزی ابراهیم مرادزاده علاقه…</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/farsna/436127" target="_blank">📅 14:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436126">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77409e12f6.mp4?token=S_-Nu3YQHaxzYHiGzy7iA4KsPjZjSI1glruvpgJSqcKQQ-vtNOpuRtnmSmKqw7nby6UGSvTFHRAtZ_rtJxAt4QL0D1n334m5aCwgOJwgtTVCbMmVbrDt2knWyWkjMn5I78scheLQo4S5eBxdq2TV2jIaX8OvOVYSp7rd73sbRsF4PMMwI0JitrE6AvVsQOnvo63r04SJ9XSyC_cuVnq3z-9UsWZj8iZNAkHJCrRLh5VcNCQTQzd4EcwI1Ykv9lRLm03IdZlqvcwvO1kwKR8yFAexBnQw8UkQnoqVIom0DDY7QcfUVxgXFDMwe4V-P9QFbB9WBseA6QVNfhkZFB5L6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77409e12f6.mp4?token=S_-Nu3YQHaxzYHiGzy7iA4KsPjZjSI1glruvpgJSqcKQQ-vtNOpuRtnmSmKqw7nby6UGSvTFHRAtZ_rtJxAt4QL0D1n334m5aCwgOJwgtTVCbMmVbrDt2knWyWkjMn5I78scheLQo4S5eBxdq2TV2jIaX8OvOVYSp7rd73sbRsF4PMMwI0JitrE6AvVsQOnvo63r04SJ9XSyC_cuVnq3z-9UsWZj8iZNAkHJCrRLh5VcNCQTQzd4EcwI1Ykv9lRLm03IdZlqvcwvO1kwKR8yFAexBnQw8UkQnoqVIom0DDY7QcfUVxgXFDMwe4V-P9QFbB9WBseA6QVNfhkZFB5L6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشاورزی: برای اولین‌بار ۱۰۰ هزار تن محصول تولیدی کشاورزی فراسرزمینی شامل جو و روغن از قزاقستان وارد کشور شد
🔹
دستورالعمل جدیدی در پایگاه اطلاع‌رسانی وزارتخانه قرار داده شده و حتی افراد ایرانی که خارج از کشور هم هستند می‌توانند بدون مراجعه به کشور و از طریق همین پایگاه و با کمک نمایندگی‌های رسمی کشورمان در آن کشورها این فرم ها را پر بکنند و نسبت به کشاورزی فراز سرزمینی اقدام بکنند و از امتیازاتی که برای آوردن محصولات‌شان به داخل کشور، موجود است بهره‌مندشوند.
@Farsna</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/farsna/436126" target="_blank">📅 14:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436124">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lM2ELQLlSrerCypuH09a538JfLEqjCppsbgClEEGmH2-h4OrVuqsEPhC5yeBvPwghWnMCtnwNuvZOFPtVKOeggahVPg1pjZAiItO07y9K-N2eJDrzUZc2IkOdM_lCLedSSzDzO4OCY6U8M0gt0YoDGE9UdmobcS24mcf5JRupHlQ1_b27eJ34Xbga54c1FMywca-5L-qiOanImEYY43PjELg1oMoMJAXHDpbp0ENKapqzLVCFRpf5kc9szZyXlpYz70zN4RsQ3qYQqZEP5eRUCm7LkJ07u4hTQVjxq2_cYjW4L_KCm-rzi8ibgIGH1HD5UPLRlEmlRNfD3hPhOB9ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eaGLmwFkTfeN4Jl7Cz728de-UM-Kl2poxZWYQcHNMdGmFnFFE-jRWjp4ihTPMK4UBGKdR7XP2nORJuQqT4A5vti9vdH60WjknyBokf0K70bAW9FnSMVMbJf2BpMeSqZXM7cEhPVpg-AkFgHiEK1ZIooc4V9pqal1JCx2G6tWHWkt2EAaWHtc99oC6XF2g5ZOlMVoToVC6DHr_POMmZ6VbA_AvmRkb-hVA934hZW4v6kTkrEyW_XBFtcurNL8dT0IYD8pydEKPfXhXeEwmGZutS3soVk91j44w5_P11ud8eIs_C_y7bvbuFMBFIlzn9G7c8QahkZjxqKejKkXr9wdpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عاملان شهادت یک پلیس در ملارد دستگیر شدند
🔹
فرمانده انتظامی ملارد: ۲ نفر از سارقان خودرو و منزل که در جریان اغتشاشات دی‌ماه در شهادت سرهنگ دهقان مشارکت داشتند، ‌دستگیر شدند؛ در بازرسی از مخفیگاه آنان ۲ خودرو نیز کشف و توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/farsna/436124" target="_blank">📅 14:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436123">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فرمانده کل سپاه: امیر نصیرزاده نقشی کلیدی در توسعۀ صنایع دفاعی و تأمین نیازمندی‌های نیروهای مسلح داشت
🔹
موسم گرامیداشت شهادت سرلشکر خلبان عزیز نصیرزاده، وزیر دفاع و پشتیبانی نیروهای مسلح که در جنایت حمله تروریستی و جنایتکارانه دشمن امریکایی صهیونی همزمان با امام شهید و دیگر فرماندهان عالی نیروهای مسلح به شهادت رسیدند را به محضر فرمانده معظم کل قوا، خانواده معظم ایشان، نیروهای مسلح و ملت شریف و حماسه ساز ایران تبریک و  تعزیت عرض نمایم.
🔹
امیر شهید نصیرزاده، که عمر پربرکت خود را در راه دفاع از عزت و اقتدار ایران اسلامی سپری نمود، از سال ۱۳۶۱ در سنگر جهاد نظامی، خدمت خود را آغاز کرد و در دوران پرافتخار دفاع مقدس هشت‌ساله، با شجاعت و تخصص در قامت یک خلبان دلاور نیروی هوایی ارتش، حماسه‌ها آفرید.
🔹
مسئولیت‌های خطیر ایشان در دوران پس از دفاع مقدس، از جمله ریاست ستاد نیروی هوایی ارتش، فرمانده نهاجا و جانشین ستاد کل نیروهای مسلح، نشان از درایت، تعهد و شایستگی‌های برجسته علمی و عملی ایشان در عرصه‌های فرماندهی و مدیریتی بود. سپس در کسوت وزیر دفاع و پشتیبانی نیروهای مسلح تا هنگامه شهادت، با نگاهی راهبردی و تلاشی بی‌وقفه جهادی و انقلابی، در جهت ارتقاء توان دفاعی و خودکفایی نظامی کشور و ارتقای توان بازدارندگی ایران اسلامی گام برداشت و نقشی کلیدی در توسعه صنایع دفاعی و تأمین نیازمندی‌های نیروهای مسلح ایفا نمود.
🔹
سپاه پاسداران انقلاب اسلامی همرزمی با این امیر سپاه اسلام را افتخاری بزرگ برای خود می‌داند و یاد و خاطره ایثارگری‌های ایشان برای این نسل و نسل‌های آینده چراغ راهی خواهد بود که نه تنها پایوران نظامی که آحاد جوانان کشور در دفاع از میهن خود مشی ایشان را سرلوحه رشادت‌های خود قرار خواهند داد.
@Farsna</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/farsna/436123" target="_blank">📅 14:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436122">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWoE8c_45AQ26uOIvwqg49DpJ2F2tCmPxPEPXLsdVV4PZBpbtAM7zeabXGr_bD7iDpTVxVmlTvUb9NeqnkybvHnDhsITur4dU-t4tbf9h3yeBKn_enqLXWeHKVXvLYVm-Kbb8vbKFXI1zXSwQV1-Qvlz7e9mjatkaFwW9yeuCZIzgtjVraKzryY1vY4n6Rw5vkmLFfgIHg5yeyMYPFvxE6lZ21xu-eiEFk1hPBNNiaxgyU2B9dnpyyBfnbQ2ZHONeXMZB54_kZmxNdij-GHOXZxA_EpE5Lh5bJ6Rl7dsUu0li-yHndI_m40JoTb9fGxWeVBrOoTfBx4FpI0iKS06hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن فولاد: سهم فولاد در خودروی یک میلیاردی فقط ۷۰ میلیون تومان است
🔹
معاون اجرایی انجمن تولید‌کنندگان فولاد: افزایش شدید قیمت خودرو هیچ ارتباطی با قیمت فولاد ندارد و نهایتا فولاد ۱۰ درصد قیمت تمام‌شدهٔ یک خودرو را تشکیل می‌دهد.
🔹
یک خودرو که به‌طور متوسط حدود ۱۰۰۰ کیلوگرم وزن دارد، مانند کوئیک، تارا یا شاهین، حدود ۷۰ درصد آن از فولاد تشکیل شده است.
🔹
اگر قیمت یک خودرو قبلاً یک میلیارد تومان باشد، با در نظر گرفتن قیمت قبلی فولاد یعنی حدود ۱۰۰ هزار تومان برای هر کیلوگرم، سهم فولاد در این خودرو حدود ۷۰ میلیون تومان خواهد بود.
🔹
فولاد مبارکه تقریباً به همان میزانی که در گذشته ورق فولادی به خودروسازان عرضه می‌کرد، همچنان عرضه انجام داده و در اردیبهشت‌ماه نیز به‌طور کامل عرضه‌ها انجام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/farsna/436122" target="_blank">📅 14:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436121">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_Gs9voMHY_5K6Bz2GckyKLcCQEeZO1Isc0o93wHVk7Qtw78rIuO2Mbz6Xbk6WsuJr6rzwEz05StjB-VFEitdDs0cGGt2M7dN8DGdjLmvMBTh6Q_aNCX_7kdxhN7k5vj421oVLyFyzh28KzU5uhpegGLGocGqFOYKyAXyOP5r0zGQz1JFicorTEDAtTLktuDev2lCZrdowZAFD4SpbRJYWY6D2dvRVq3DjaSgYPb476cNTRJ2SJO5AhLhSi5dkW02WlGnGM6LlM95bVuIlHkXJ8GZHsMfQmiMBO_g7qsbeZyLFX-R6-siksuI8ZrlFagC8Y17vGFovClYMY6FxLFQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پیکر شهید عزالدین الحداد، فرمانده گردان‌های القسام در غزه تشییع شد
🔹
شهید الحداد دیروز به‌همراه همسر و دخترش توسط رژیم صهیونیستی به شهادت رسید. @Farsna</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/farsna/436121" target="_blank">📅 14:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436120">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c56f73861.mp4?token=IPC-sec2_SmhPFMVVMlOaheIHtbPUe2RNR-tg28knYH2L5pHp-iWM1X8FQYsZVIzvfIPk1JBmlouAidVr50O2SA91QVRdFfMCI0wVXR2jYi4zpdzOvezN3Dm_GBc8Xua9-Drq5TWm-F8B3oIT6wiH0io7-0Qe-frLdXF83LWOxpF5unDr37GLYcd1lCaTkxiOzLTYwmiWe1H4lNE3SU7FU1UIWCXxCRLAONakKWLgnzZOLcLJVAJwNgaQXjOhWzxibclyMp60u4ZMjXEfZLS55ORReBWXcHbvVEMyZ-H5iIeDhF20ZolfTZYRdEE_qjKPJ16BRunVVdDe7o5rE_JFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c56f73861.mp4?token=IPC-sec2_SmhPFMVVMlOaheIHtbPUe2RNR-tg28knYH2L5pHp-iWM1X8FQYsZVIzvfIPk1JBmlouAidVr50O2SA91QVRdFfMCI0wVXR2jYi4zpdzOvezN3Dm_GBc8Xua9-Drq5TWm-F8B3oIT6wiH0io7-0Qe-frLdXF83LWOxpF5unDr37GLYcd1lCaTkxiOzLTYwmiWe1H4lNE3SU7FU1UIWCXxCRLAONakKWLgnzZOLcLJVAJwNgaQXjOhWzxibclyMp60u4ZMjXEfZLS55ORReBWXcHbvVEMyZ-H5iIeDhF20ZolfTZYRdEE_qjKPJ16BRunVVdDe7o5rE_JFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از آب‌های شمالی تنگۀ هرمز
🔹
آرامش بر تنگۀ هرمز برقرار همچنان است
.
@Farsna</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/farsna/436120" target="_blank">📅 14:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436119">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT3pcps--fzIIXHTVEUjH_hFvUWOZNXhRhQAHtZ3Vf5kd6_tzRxBGbl-G7dpJeXa4TUsPQU7Yf0hL0RlBMRa0Atc6SIm5N4V3jWYTEmxlG5Ks0SYvsdNIIrdyktAjhYiK0liqBe1zMbAH1XYRW14naot2k4nVFF7OrrG4gqLSrZl9vS0OkK0vvVfx-ksN-WzGZ5IQets6X5at8FWeKuUaTrKdlcrVnegOoFzSFDpA8zTgjjaJ1_Bte7wh7OGWOBfquTrDXY5h4GvbZVmH9P-7XtfE0oWZDJmXJkPemxAanEfLGezmAowMZW2uIdeURrG8Xa0QFpC86VkkJSIbvRpQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیۀ دفتر حفظ و نشر آثار رهبر شهید انقلاب
در پاسخ به انتساب یک شعر به امام شهید
🔹
به گزارش پایگاه اطلاع‌رسانی دوران، به‌دنبال انتساب نادرست یک شعر به رهبر شهید انقلاب دفتر حفظ و نشر آثار رهبر شهید انقلاب در این باره اطلاعیه‌ای به شرح زیر صادر کرد:
بسمه تعالی
🔹
دفتر حفظ و نشر آثار حضرت آیت‌الله‌العظمی شهید سیدعلی خامنه‌ای قدس‌الله نفسه‌الزکیه، در پاسخ به پرسش برخی از اهالی قلم درباره‌ی صحت انتساب شعر و خاطره‌ی بازگوشده توسط یکی از علمای محترم، به اطلاع می‌رساند انتساب این شعر به امام شهید و نیز ماجرای سُرایش نقل‌شده از اساس صحت ندارد.
🔹
دفتر حفظ و نشر آثار رهبر شهید انقلاب رضوان‌الله‌علیه قدردان دقت‌نظر و حساسیت اهالی قلم و فرهنگ و عموم علاقه‌مندان آن قائد عظیم‌الشان در دقّت بر مطالب منتسب به آن امام مجاهد و شهدای خانواده‌ی ایشان می‌باشد.
@Farsna</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/farsna/436119" target="_blank">📅 14:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436118">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3ukyOTwQr-ps_lWs-3qVvqMc5nCj7Jmxzq0P0pfDL7zhYzYOo8ITED7gP3tO0FOs64oTkcsYrP8rSjmn6lJFUkSF78xMpCUVoZZp2KMSNmDNd-HPv558LCQuDE_Na_wecYymu6KTNikFUaCAfgNziP8PnLvQxrIJo4L-KSXIOf5q7mc_Oia6895ojV_uPH3rLftsCT1Nraiuhq0ft40xmXEs9ydqOsonJ1KZRwxGxk4pJgpnPONEejRAPvAGUBFmHAEKl3Sq6R_yvQlLsLJBEg2l7meio7Je6sGsJlzuIQI6kl1AdWC_xskZW3RQnky1BmclXZPRNbsXHjywJ7mtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پیام تبریک پزشکیان به‌مناسبت روز جهانی ارتباطات
🔹
در روزهای جنگ، فرزندان ما در ارتباطات و فناوری اطلاعات، شبانه‌روز ایستادند تا ارتباطات و خدمات حیاتی کشور پایدار بماند.
🔹
دسترسی باکیفیت و پایدار مردم به خدمات دیجیتال، بخشی از آرامش، پیشرفت و حق زندگی شایسته مردم عزیز ایران است. ‏روز جهانی ارتباطات را تبریک می‌گویم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/farsna/436118" target="_blank">📅 14:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436117">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پیام فرمانده سپاه به‌مناسبت روز ارتباطات و روابط عمومی
🔹
روابط‌عمومی باید با تولید محتوای کیفی، واقع بین و امیدبخش، استفاده از ابزارهای نوین رسانه‌ای و شناسایی عملیات روانی رسانه‌ای دشمن و مقابله با اخبار جعلی، خط مقدم این جهاد عظیم را با صلابت شهدایمان بایستی ادامه دهد.
در بخشی از این پیام آمده:
🔹
فرا رسیدن ۲۷ اردیبهشت ماه روز ارتباطات و روابط عمومی، را به فعالان پرتلاش عرصه ارتباطات و روابط عمومی، به‌ویژه کسانی که جان خود را در راه روشنگری و تبیین حقیقت فدا کرده‌اند، صمیمانه تبریک و تهنیت عرض می‌کنم و در طلیعه کلام یاد، نام، خاطره و نقش آفرینی‌های سترگ شهدای روابط عمومی و عرصه ارتباطات، خبر و رسانه، که چراغ راه هدایت ما در این مسیر پرافتخار و مسئولیت خطیر است، را گرامی می‌دارم.
🔹
در چنین مقطعی حساس در دفاع مقدس سوم و جنگ با دشمن اهریمنی، پیام راهبردی امروز ما برای مجاهدان عرصه ارتباطات و روابط عمومی این است:
🔹
ارتباطات، خط مقدم جهاد تبیین در عصر تقابل، و تلاشگران عرصه آن پرچمداران حقیقت، خنثی‌سازان تبلیغات دشمن و تقویت‌کنندگان وحدت و انسجام ملی هستند.
🔹
روابط عمومی باید با تولید محتوای کیفی، واقع بین و امیدبخش، استفاده از ابزارهای نوین رسانه‌ای و شناسایی عملیات روانی رسانه‌ای دشمن و مقابله با اخبار جعلی، خط مقدم این جهاد عظیم را با صلابت شهدایمان بایستی ادامه دهد.
🔹
دشمن به دنبال ایجاد تفرقه و شکاف در جامعه است. شهدا، فارغ از هرگونه اختلاف و مرزبندی‌ها، در راه دفاع از ارزش‌های مشترک و آرمان‌های مقدس ملی، انقلابی و دینی جان باختند و به ملکوت پرواز کردند.
@Farsna</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/farsna/436117" target="_blank">📅 14:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436110">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i-reWw211lYi6AjoJTBW925-52Om-zctH3iZRFApspq6Ty4njUGwC0j25B8Nwb2E-jwuHuLR91_DxTOvj9XrRvHBBDXvE-pe6AVCxGYFJ4vtJuP6jJkqvLt7MdgnCP8M0DnoeFf11_MHezh3EoDXv0LYvHv0vpIyiips1bKF8HqQIBqiW3rUjxy59qib1PfbvzxrKqpAdTkvE7wX0Eu-Pw2F__Jm7JMwmTLBFLp9jkUmCKwQEYrnR-v-u6-4pc7-efVP92YxCqNL-MTbHkqf1j6qWuxoj2MXuDqDS1qsQLO7_bR_AKO5wV4SGY8rDm3mlRfJ57Ek5O6-3fA6Dki2Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d81gVOGuxYwAEA8dj7zsx37qEPnGMAuAfuEonqNX1k9MT3UumjptWH1B8EffZ4CEjbxkCgtiVGQMMKEpzxykaQvwLeYwhLAV1c5V1knfyc1lyU9qiEZtwCQtMuI-j15Cxtcs23G5Os_w5gy1iTCS04IReCwen9GZl8tNpYI-QYdBn94jRqkZzTKEbKho8iHn2JyBVbezye0GQ-3oJEBLlyMcJIXQwxTfFhJRSxMFJQcX0yRjKOQZvyDIRnNRuz8GpdNGXy9rXvrIym4PFjprmBN6brXsUUZIpG8r0VgP6c2hS0Bs4EEdvRBaOHEPZpBW24YSjV5BWuOw_FdAhKJYRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D1wCjAdm9zkONLU0uxFftjkWYDNhSNHqWtNsQloSv6R8woprKqYiEjlU6B9wrUWPnj1YXLCHTa_qHXOUfPDfOkji_oNYTJMZNiIQLWX7SnvWRowz2ch8ViJ9jn7QUaob4-kqVMOpJPCHDnL23hDhHGsGX3zQuU_hSMxtLtkjzq4YnuWr7AOlNxUGKQukwB-zON9JjMATS7W4edg7eMSHJCzhQ64z7WSXW0RZPBQ0AmHSzUXLZ0I0JpOvGSaIxPvliZR3Gtvn3eOe78JgwbK5yS-TOKelQet8DHVh0gHiHNUaZeEA82DaMzlhv31Srua9ddqPYO_pIYmPOi4nHJ6BrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mVdFKXSfTEbOUJ_O7o2O8w74bGZSFjbp4vBzuibN6wnLJ_qtjfRODTpbKNR25Fc0JNeZfIwwIwgXANhahEWaHIUy1OH6ROC5paaXf91diUR30nwP_1ro4P1gxD3a9Ufs5-l28mfP-mzIbI3DpZ5T5WRSySAtw6J2MOkWoHKs4gxGeOS4CKg8Y0I-O8uVBJC1jPzA2W8kch_kv8qAPAbS0Edg4tDI-hZWeYntAfmMwnIPqjCKr_v3Xg9La7vc7lEI7W602i1D9cSjjadNLOaDSJKppEPzlTZH_f13RfHTqsyQ6XH26uyVw0GuZ0bOf2xs3JFWNKpPqQ9Di2l6kh2XNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pbZFSK8pg0Zog_R81GDe8QkVqT0o0zx21zzD-5bOw_V0zZd5wBf0udR8WVfDW4b_fEDLi2eE25mO5Z8x7VFWTSraZWOFWgeMCWs2-UQgD6cV8CmAnkwURF75FtZs6Zg3VrFWOIUJVoqp3gl93lkkmaL1TpN1RBjr-OIuotfc7e_hYmIw5Qxh1i7BoTtDIcvZgJ2sp4oFFioOOeePSdkkNg5OX_a_BeYCsyXQQ2raDOC0d_6MDFvbEdmux-0aDIjWohTn6v9fpGrad0YJpvKjSHKR6Deey2HxbFuN7pJYcY_Kp0QSuGsMFF2Lem6VzeVrjtO9u-2u7nu40BWqIFnLwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HGHqcBfvA-E4rnl6XTAMjs8OtPSgZr62xiXf88HsPCvEnd7xn9Lq0EaopzDyMyis4f9OxmzLbx0n9O7lfDJtVbVKMUNrBGecrQCWDLzAVuLjSd8HQ4K-qsAnJLd5K1R7gObFC5R1UpBVprPeEf77UN_ph_GxgFcTX2LXROiJ0LLdEaaiinR_MjyFgPhkOUkuwg3ttEwjNZBeVh_XuAdy-xF2jOx8vCi56e-uQXOvRsh4SvVtMuDyEzcay40SNaBxbDu8I6o4pmlUbOcU5An2f1xwKIXFu-CW5whWlnwqIohU2II4r2B5IvBhoCVMl0zBo7ldg7AGAkdKaQNKF0HD0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NsltnGudeon49ni3gtsEA0BtiQZ6fQbgku1R_9r84dTDCZs0wSd_Ky__r_oABESo1fxHJ1scsObnCoW_RbarEyXZImDL3PIjrsQZGbjJdxGz8wswmN9Cqtgi7XpfRfUyCzABKDw5urcs5SnQUoBGX6YQFCMe4tGJKnT8EgMAmPfP6xa6Hv3kkh_7BYh9os1U9hx4QqYxO4MWXiRrfWFkqZaSwXpQUzU2mWJjwi_UF43MhjOFXF_0XlCmuQtU93CAe5zcKTdcx2S4_7miGtxHUZwc57_NamGVxZU8V9GJQXIHQSac1QBU60EVnA93wulk9kZCHPRNG0v_v4A215akDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دستهٔ عزای خادمان حرم حضرت معصومه(س) در سالروز شهادت امام جواد(ع)
عکس:‌
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/436110" target="_blank">📅 13:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436109">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
وقوع چند انفجار در ابوظبی
🔹
برخی منابع خبری از انفجارهای مهیب در پایتخت امارات خبر دادند ولی علت انفجارها مشخص نیست. @Farsna</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farsna/436109" target="_blank">📅 13:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436108">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
وقوع چند انفجار در ابوظبی
🔹
برخی منابع خبری از انفجارهای مهیب در پایتخت امارات خبر دادند ولی علت انفجارها مشخص نیست.
@Farsna</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/436108" target="_blank">📅 13:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436107">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t94LM1y5vX-5aDMBcl9ZL-0MC9f45_dCTt0X-MqWMohrKcMjFo4AoWQ7Olr15PLbPu4vbeDiVY7PIZBqd9eqjy5Z-hPrrbZH6OSYJG0TOdprY9AP8lQrc1aQm10zqny3hsaRbyarYS9CpY5Ft6X1qyWvy2ivoMlSLtZ4RZP5F_lR8OtIWEaOcXiZxGy_pS5F0uLVMIb240_VD0PoIOI_B9_-HPl955LT4W1Cr1hZFy2adnfWXsra8y4cq1uwntyimhfC80Naf1yHf8GnDQXcFFKzlD0-2M-IHHm4bTxFWqyHdTezHq2zxOU0DxighjjSCXtQ9XXQ-Gc60aKbOS_CcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علت گرانی روغن موتور مشخص شد
🔹
پیگیری‌ها نشان می‌دهد ۹ اردیبهشت جلسه‌ای برای ممنوعیت یک‌ماههٔ صادرات هیدروکربن‌های روغن موتور تشکیل شد؛ اما رونوشت آن ۱۳ اردیبهشت تنظیم، ۱۹ اردیبهشت ارسال و سرانجام ۲۶ اردیبهشت ابلاغ شد!
🔹
با این تأخیر از فرصت یک‌ماههٔ تنظیم بازار تنها یک هفته برای اجرا باقی ماند؛ آن هم در شرایطی که قیمت روغن موتور با گرانی ۱۵۰ درصدی، از ۹۰۰ هزار تومان به نزدیک ۳ میلیون تومان رسیده است!
🔹
این مصوبه در شرایطی تصویب شد که به گفتهٔ مردم، در ۳ ماه گذشته به‌علت افزایش قیمت روغن موتور، هزینهٔ تعویض روغن خودرو حتی بیش از ۲ برابر نیز افزایش داشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/436107" target="_blank">📅 13:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436105">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCu0X9hDAXLt54tW9o4mZg5XhpZxFCXRPwqkIi9xIN0vtNEGA9eoNDzz1SVQnmQqcQSNyHHzoa9X-hcZEi-5nb2yCAV1LR-mprAAHZbEHbcEYEVDXqYYQbH2Jpy6oMHyyZLfnfZl952-VV68vMVuQsru7V6oBg55VmcIzZeAWUc5kw5UfeUErvVwrUsUItdj3KB-G8bZ-Bs4qCmkCVpfjIviHeinzOJ_mKHdcQLu7HWrTjGW60sUalIw2XlBEsbGrOO5KVnNq-SNin6PbJgJqDKL070esAO6r7dJladLRikY6Du6K-ODDiy0Sy9kKd-ETgLkvmrsTc92QNm6bA9E6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دومین جلسۀ مجازی مجلس یکشنبه برگزار می‌شود
🔹
سخنگوی هیئت‌رئیسهٔ مجلس: دومین جلسۀ مجازی صحن مجلس با حضور وزیر رفاه و با محوریت مشکلات معیشتی مردم و پیگیری اقدامات حمایتی از جمله کالابرگ، یکشنبه ۲۷ اردیبهشت ماه برگزار می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/436105" target="_blank">📅 13:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436104">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رئیس شورای‌شهر تهران: فعلاً طرحی برای تمدید رایگان‌بودن مترو بعداز ۲۷ اردیبهشت به شورا نیامده
🔹
هنوز طرح یا لایحه‌ای برای رایگان‌شدن حمل‌ونقل عمومی به شورای‌شهر پیشنهاد نشده و مطالب منتشرشده تا کنون اظهارنظر اعضای شوراست. @Farsna</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/436104" target="_blank">📅 13:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436103">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎥
گزارش اکونومیست از پهپادهای مرگبار ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/436103" target="_blank">📅 13:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436096">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CsvBJtQStZU4bryUt_fUy7ZrqtmhNLpY63g69KTRLi4MGjIxw8AOeBZdy1gB4ZbxYQokRJuyl8xNJT5g5bQ75FcM7BWRLBCTtEXcOWTXh8njQhuDB5UQVj3f6U7uRAxmyTIWs6e-FpbITby72wIocJv3hg9PW3wVfGErXkaAnmNqDD4mFZOFjCctEeUfjwbaqN3Ih9CPEqu21XI3K3D9r7j0q_DWGiSgWWB-cgW-gqTNWvLhsRVOwkFPATYkRYAkTzWvJdevAfpI86oW1ueFh0ZCOGupclTFZ4zULIEBanF4ZJfmNtQcOQtMqOss96j2PVFW91mThkA25nGnuhFbtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hDh_BN9THyxl1X1XnMQAQSZWhsxFR31k5tDkRVQNHgvxUlbNSg80PS-xS1p8GiJf_i-Ogew_P-yfFLKhFP-_vbrs1x0WfClEr7zJgjnz7JPBgl3o-y3bjiseOlTHTsQClg4NhO355igkCa3xMQu8u6BF7H017klrCVpszSHAP-aKZ6_rjJXXU0GmU_i4u4jW50iT4u3kcFZ1gCFso-D4-RIpn1xHnjhoh9vCLx_-mAZVMJEKwHexmZf5WrSFP6q_fHkTumPFlP9odf2t1lsDP_dEgyqIAMHFHmbebRNMHGA_jngRaFUQMeu9ODQdlBCMzv6u3AC2tijtGjpjX16xzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYXB4P5aEe-Wdg2iZ8HaCqOoveu2KIfrL2cYZcwhjQGMx3O__3eTBvBiHcsDWLDs1TWwFK6porZ8k-6r7oO-0r7ppI2r5FXVgZpntdaACi8ma0bxkBDlbpxLllKxd6UhZjVLLI8rvYGaZq5f3CGJ6IW4AkKr-QX3tFK2ruZaQOwD6BlxBrXsowVZCKVkqD6ayUcrRGAzalTOvVLE8LNLyHTM7ncFskPfRYtPEMai7JVf3xn97PPfqwRV4yMV31Ltd19K4DcH9xRCq5OamgNiGfMEVAhE1OQn8H1x1hZompUOsCHWkRlXyK3dOBmvM30upxi32cPJgDIs8EcTMKP5yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AekNRDc78bwEQ44nYagM6QD7fjtq_3FXeN2tIEpL8zDY5LVsTq05_3-I4TZn-TM6x80xo90b4M3kbCZUD_2BazQxGLkZ60qqSbibeptU_Cbx6dGNoMD0WiNgiwsfmQYxUzWJPKNGsF6V-lzW6tBc9S8ZluQOVx_OUa0KWXiYYJrcdKHA7IKlMo5VpupwrJpfASeZpxQtcYHEJGXE5bUv_XlsFW7J4TMW1QlYL3e8TFLsm1_TSz1sNwXZAQrXSNALVfS85O1lseeLK_Tqp74gsDSby0GzGEeMQrjK_aifMGIPbNzeSBDNwKNepp4HWzat3YdSRfQy2zPCixZPAEB8oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJsYtIIzPUpLkBg5on00HzFOwYQJueZZJDa0Af7Riv5poVS1qKFwmGo1OmTCuEHIKt8dYTJjvMZ6oSutXdS9cDdzEDYgZkk1J8dG3ESR4MQp5yuxV_hF5HKpaUUEFW-mkAngM405iE2lVr8pH5P1JbNkrziXmAHyRIxQk6iOx1y_hx5yBe_oD_nRWX2YUeuLU6cRQOcDkdt8pJ-prVv4YdXwNBrhWpHK4eHlXT4YMf3N1zEMMgiEe1e1hchYBCAmuVNtdyk0zUGApJ6jOR3K9EXDJBl99lYjPjEM5q-vO8UTXBCxEAT8zpAgrDvYFcdnVO58axb_9rIAt1AISaKZHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OgKctKb5plSKCanVywPipKSj2tmTQuzVmaSh_hwwhx8PWGZ0oqS6M6H-e3-w_IvFx-J_2J8WhRvtVvSB9OrmYoKzk5OVJlUFiy5lgG3zevDWbkD-i2ZeiV3RVU1aCrKZMtxcGcPvcJldNILFvkKX0zVXW5kfdeMDNoyxs9Om_YCvSl-kLlSVTXj-eocuhj6YhuBILClIwNV1OiTPcVVTLV9Qx76ul6-YV1_nBGoXqj0FL1FlF3NjmTMXBMl7u1L3_6B8X-gKnJcN_-g2cAlzUvueGxyOlQ0iKvKIL6YKZjFtig3_hgMcoeFwSAqVqmv2gKaBrH_-jDBz8FKfkmqQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DKC1CxVlktUyv2p7mg6NbSHOYU8bxeDmI2SuJq0h3uTfrGig4p7UQ_HjoLMYjECdqmqNL42LIGQRygog2c704NVoJlyUgyoWi5OT1uzvHqD1YWxCO6KUCO4rMRCS5awo40jKTpnRzWYG-lR0n5WQWQ58K5XAYFo0EfoLNm_Hy005gzdudHieDWlsQDyNthFgjD7cJTCjfZChs_dOxyOTc3kDW9LrFrDQpCndz6pq_RySTDfQ5gaeKRB6W156HULEL5t_77zb0l6fZYdBtXcjepr255fCayecR-UZbJdKrje9NniIbIB3hwO5zaI5Cd_UA3k6oyp_uChFVUkRlpsnEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
طراوت بهاری در باغ گیاه‌شناسی ملی ایران
🔸
باغ گیاه‌شناسی ملی ایران این روزها به تابلویی زنده از رنگ و طراوت تبدیل شده است؛ جایی که گونه‌های گیاهی از اقلیم‌های مختلف جهان، از جنگل‌های هیرکانی تا پوشش سبز اروپا، در دل بهار و پس از بارش‌های مناسب امسال جلوه‌ای چشم‌نواز پیدا کرده‌اند.
عکس:
#زینب_حمزه_لویی
🔗
تصاویر بیشتر
@farsimages</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/436096" target="_blank">📅 12:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436095">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">جزئیاتی از درخواست‌های آمریکا از ایران در مذاکرات
🔹
براساس شنیده‌های فارس از پاسخ آمریکا به پیشنهادهای ایران، ۵ شرط اصلی واشنگتن به این شرح اعلام شده است:
🔹
عدم پرداخت هرگونه غرامت و خسارت از سوی آمریکا
🔹
خروج و تحویل ۴۰۰ کیلوگرم اورانیوم از ایران به آمریکا
🔹
فعال‌ماندن تنها یک مجموعه از تأسیسات هسته‌ای ایران
🔹
عدم پرداخت حتی ۲۵ درصد از دارایی‌های بلوکه‌شدهٔ ایران
🔹
منوط‌شدن توقف جنگ در همه ساحتها به انجام مذاکره
🔹
این گزارش تأکید می‌کند که حتی در صورت تحقق این شرایط از سوی ایران، تهدید تجاوز آمریکا و رژیم صهیونیستی همچنان پابرجا خواهد بود.
🔹
کارشناسان معتقدند طرح پیشنهادی آمریکا به‌جای حل مشکل، درپی دستیابی به اهدافی است که این کشور نتوانسته در طول جنگ آن را محقق کند.
🔹
در مقابل، ایران انجام هرگونه مذاکره را منوط به تحقق ۵ پیش‌شرط اعتمادساز دانسته است که عبارت‌اند از:
🔹
پایان جنگ در همهٔ جبهه‌ها به‌ویژه لبنان
🔹
رفع تحریم‌های ضدایرانی
🔹
آزادسازی پول‌های بلوکه‌شده ایران
🔹
جبران خسارات ناشی از جنگ
🔹
پذیرش حق حاکمیت ایران بر تنگه هرمز
@Farsna</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/436095" target="_blank">📅 12:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436091">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/csxMVxfPcih-4S9noobmBv7W9lFYcVIZTNmetbFeHU89XT-tQdSfJ6UWUb80acHTMoGWnnxP7wLcBnRu0mo_D9Rt9NyySkO4syun6fRX5esA9LDMl_wjxyfDA4Er5BoMk4GiUkTMuHH89vcCSZo3Zaw27YqbHCPyWRfxaho1QWXMVWrprLdUxXza-Dmf174fPvYWOZepHXpKSUC1cKUzKRHueu9mueMOEjv1iekWtiK9JkPMCR0TUiPWTgsGGPCLGj1a5WZiYKCU7RwR80i3qcez-5-aT8J9U3q3QXHsKqlL0-6dfeEbx4AFceA7iaQ6hIZe6s5ZQQE8LRijybh0lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t6-yo_Ym81IekZ77ESqXOMvau0XwoJIX8yq0r4d8NDWbP2IKjzt1JOooDS3_aE7CxLBipXr8p1t2ob_bv9jY6fLVD4-s-ljsrZXJ7jHvR8srWsvhp6Xh4HXIS0ApthSTgxmGbJDnA6U9hgyjC73otI2rhTc-NqEAJ-ROOkTX8PfxR7kRimaiQDSoGnZT3D7n1XrPy0Jl8lDkczqIdO4DPGzx7LhSobBGIUOeh8WHeJzBb4IUAbJrYDRKX702Jb-AEKrVXHUBrH3dqvMPbHnrXvhk_XDiIie2CfjaxEywh8Jog8GqtdV0HPURxaxg5UL5WqQ3SG06gseAB9s4ofZJ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dd20K91-NhMJR3j-jh8QbYpZSZERR64kQqQVN5ypwyNlT-U3fH8Lw1PceEJlU9j_oZr2KhIhK1ThVf_uJnJpyYbhJizLHmRfvQPBVjypF7Pz8ttS5xLMpYM8u94PpZIFZ4t0KKZMnmqyjFTSTau2OqkC4RN3v7ljzTnWa6mBiDBtveC8i5dneip5hdXX09DUQSg6um6whcTBPM0CDzfytKvCFeHK6kGzKvPtrPYnKL2-8RUpl-cBuK8zpMcBlb_iWB4ZNPMcJM8zyYmagtdnY_KHjn8WhPwHRMTiSSAlfy8mOEQ-cbvCE3r_svUYxTt6g0JeXD1emWgmqzGVwQeWYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bngWUbRpYZA-NcMvnDW9K15l2uOrBerEI_nkzIKsf2FgmnDo7mpZF9rI05o0Z6PpCDbx7rMeoXjGoW2lBo-q5j94X4qHU5NdgIjwTiM9CCuN7Qv3-jO-RJ7YJAASUi1yMvRLiAsQS_5AG_diMmVN-ZRutzYa1bz1bdvJ5h7VRcS2TX8JbcMz11AenPz06DP4Ah2Ve_po2LaOhVb2MfGi4KZt5-IXyN8MvHe61OwXHygbUel0s4c3SEuuF2AzaZ5MR7oP4isu950FKFIafXPQRwETMx1iOO-h-3owXt-W0uWgQ6QD0j6rm0OCPnTqyw_xSPVbJJikBvI8Lna3tjIQnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: تغییر رفتار مصرفی جامعه، نیاز فوری در شرایط کنونی است
🔹
رئیس‌جمهور در بازدید میدانی از اجرای طرح «حکمرانی محله‌محور و مسجد‌محور»: تغییر الگوی رفتاری جامعه در حوزه مصرف را از ضروری‌ترین الزامات شرایط کنونی کشور است.
🔹
مساجد به‌واسطۀ برخورداری از سرمایۀ اجتماعی، اعتماد عمومی و نقش تاریخی خود در ساماندهی امور اجتماعی، می‌توانند محور اصلی ترویج فرهنگ صرفه‌جویی، مسئولیت‌پذیری اجتماعی و اصلاح سبک زندگی در کشور باشند.
🔹
اگر خواهان ایرانی مقتدر، باعزت و برخوردار از توان ایستادگی در برابر فشارهای خارجی هستیم، مسیر تحقق آن از مدیریت صحیح منابع، صرفه‌جویی، ارتقای بهره‌وری و مشارکت مسئولانه مردم در مصرف می‌گذرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/436091" target="_blank">📅 12:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436086">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPv_Vi3aNkXCqxjqVx6cA1dOsaMx9azZH1bS-ZPolCpy6lECykxaxD-apsAdVD5RXx_FeoQj2d8G2c_SDO29NqtYWp7J3dgtYxo8s30Ml-qnUX7iL9tzJQjnKFrG2EEivqInYZd07F4lBZPxxeUJfyaBdxeFxj8Dne9KChtK0ATAmZMcM4mISC75Y5cKCsZiEAMgtCgg-H_16F7Piv3GlUSKC6tIi1Zx--p2J3MrFVEJonx2rlc6deN_l8UQZPKcRhndnPCJVOTGeAGHLTz0PlsYrOQKiPoplOauZ6-1nDtlnt9v1HZCxibmue-E5EFABmF9z_I7E6unGu-er_NcFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سردار شکارچی: تکرار هرگونه حماقت آمریکا پیامدی کوبنده‌تر خواهد داشت
🔹
سخنگوی ارشد نیروهای مسلح در پاسخ به سوال خبرنگاران مبنی بر تهدیدهای مکرر و یاوه‌گویی‌های رئیس‌جمهور متوهم آمریکا علیه ایران اظهار داشت: تکرار هرگونه حماقت برای جبران بی‌آبرویی آمریکا در جنگ تحمیلی سوم علیه ایران، پیامدی جز دریافت ضربات کوبنده‌تر و شدیدتر برای آن کشور به‌دنبال نخواهد داشت.
🔹
رئیس‌جمهور مستأصل آمریکا باید بداند در صورت عملی شدن تهدیدها و تجاوز مجدد به ایران اسلامی، دارایی‌ها و ارتش مضمحل آن کشور با سناریوهای جدید، هجومی، غافلگیرکننده و طوفانی روبه‌رو خواهند شد و در باتلاق خودساخته‌ای که نتیجه سیاست‌های ماجراجویانه همان رئیس‌جمهور است، فرو خواهند رفت.
@Farsna</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/436086" target="_blank">📅 12:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436085">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jwb-TK7ZMUZq-AVzafO72TnMAwAKyipSQM9MPB2gwdtL0-Y9A32IZYtkJd9jijw5hOAt0xWFFbqUOojrrazUoY7C4zBXbCJXnfy0p7Fp2SVY4zGIZBcEnWdkpB61kqwE4TYPfy44HqjpNkWS70HlbmtqtTFBo2jmeTx6bel8J0T1dQePXRMjDYNKrFBeV6tmFS7E31i7RRwWRPWdZDnb2lmRPJED_OJ2ey8sv2xD3NnvaGBEECV6DtiVS6KyU5FdjwffyE6XKkNuZlT6yZjwz-7FKPrRVPKueX2K9JytyViPSjmSMw41VIgVz8fsNAC4n5TxicYYMwTUPITHbmeudQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
دادگاه رسیدگی به اتهامات صادق ساعدی‌نیا برگزار شد
🔹
جلسه رسیدگی به اتهامات صادق ساعدی‌نیا مدیرعامل شرکت صنعت غذایی و کافه‌های زنجیره‌ای «ساعدی‌نیا» از متهمان کودتای آمریکایی-صهیونیستی دی‌ماه ۱۴۰۴ در دادگاه انقلاب قم با حضور رئیس و مستشاران دادگاه، نماینده…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/436085" target="_blank">📅 12:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436084">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a6fce360f.mp4?token=eYRorlwGBHEWavWIzmtKpt5KwXY4dKzDazlyrn2CFt1LgqIs-DExYzPNXKcqBx8GHxv6ViQ_KucKjeCDlVBF4VnT3cXnlocGkJtfVTsculAR-8E458JomGVjqmYl5nH8S_Q0KV1D0SrTIqAW5MJZKc8cEnP7M9DCMghM3xpHcCXqf6_CDvmNky-68hxICblxz01qS8nzk9qGfE9JvX5Q4Uvqp3nX063pdZ7uPklLNvkPL8Zf4ikC46wE9hm6IfzpnSDCLEzaq8gTq2PRLuKILhqM3om11vkxzfMaeaQeQr8vMyNUoH0tj9IcVSLXYaBGf7bG-riOdF4MMpjizpmjMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a6fce360f.mp4?token=eYRorlwGBHEWavWIzmtKpt5KwXY4dKzDazlyrn2CFt1LgqIs-DExYzPNXKcqBx8GHxv6ViQ_KucKjeCDlVBF4VnT3cXnlocGkJtfVTsculAR-8E458JomGVjqmYl5nH8S_Q0KV1D0SrTIqAW5MJZKc8cEnP7M9DCMghM3xpHcCXqf6_CDvmNky-68hxICblxz01qS8nzk9qGfE9JvX5Q4Uvqp3nX063pdZ7uPklLNvkPL8Zf4ikC46wE9hm6IfzpnSDCLEzaq8gTq2PRLuKILhqM3om11vkxzfMaeaQeQr8vMyNUoH0tj9IcVSLXYaBGf7bG-riOdF4MMpjizpmjMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعدی‌نیا: خودم و پسرم اشتباه کردیم؛ از مردم می‌خواهم ما را ببخشند!
🔹
محمدعلی ساعدی‎نیا، مالک برند «ساعدی‌نیا» در نامه‌ای که با امضای او به فارس ارسال شده، ضمن اشتباه خواندن اقدام به بستن مغازه‌هایش در  ناآرامی‌های دی ۱۴۰۴ از مردم بابت این اقدام عذرخواهی کرد.…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/farsna/436084" target="_blank">📅 11:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436083">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b54d485d5.mp4?token=PhrRUjBGw3ztusdoU-UmQdUPymwptnoUSmbBrSMCdBsewPkU_kT2yYMQjPRIMYTFDQfbL4Y4CcTYm08w5qiBqZ8MfZwifwJr0x-uDo1Y7VgRT5D3mq7dUFu-oWsDx3UDdllQGq7rx3pAy2iJMDNrLTtz2xUm0nhNjWjKEBbPDagp6S1bzHpDP38LEqRpLeJ7ELNC9YsqK3VS_10ezi06LvhgwTLD8ozeNpboNXpm2GCIBkbTh8ZpLFaAgtbrga0NPHHOPi2w2g4TTQBgOxyBHKnYGJBydLB6dWM3uehfXgJ03gFVff4MlyijfKN-ClbEewnIESCkx31NSGmXqNnbSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b54d485d5.mp4?token=PhrRUjBGw3ztusdoU-UmQdUPymwptnoUSmbBrSMCdBsewPkU_kT2yYMQjPRIMYTFDQfbL4Y4CcTYm08w5qiBqZ8MfZwifwJr0x-uDo1Y7VgRT5D3mq7dUFu-oWsDx3UDdllQGq7rx3pAy2iJMDNrLTtz2xUm0nhNjWjKEBbPDagp6S1bzHpDP38LEqRpLeJ7ELNC9YsqK3VS_10ezi06LvhgwTLD8ozeNpboNXpm2GCIBkbTh8ZpLFaAgtbrga0NPHHOPi2w2g4TTQBgOxyBHKnYGJBydLB6dWM3uehfXgJ03gFVff4MlyijfKN-ClbEewnIESCkx31NSGmXqNnbSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زارع‌پور: شهید رئیسی شورای‌عالی فضایی را پس از ۱۱ سال احیا کرد
🔹
وزیر ارتباطات دولت سیزدهم: شهید رئیسی دولت را در شرایطی تحویل گرفت که عده‌ای اجازۀ پرتاب ماهواره را به این بهانه که مذاکرات را به هم می‌زند، نمی‌دادند.
🔹
شهید رئیسی اولین رئیس‌جمهوری بود که از صنعت‌های فضایی بازدید کرد و در دو سال فعالیت دولت سیزدهم، ۱۲ پرتاب فضایی انجام شد.
🔹
در دوره شهید رئیسی، پس از ۱۱ سال اولین جلسه شورای عالی فضایی کشور برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/436083" target="_blank">📅 11:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436082">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spPklL3d6I99WdY1pjp06JFtGT0IXL5TuIAqaq0uTFOBza8xMcJ6D1ZnNZWO2N42RYgmXG31qNb9ZmCHu8wJSHBTbo48ujYM8zlk4SBePZsMxoVCur8gRcKFSQcQi4BN9uFxgqekDrTyc7eKggP5af_ZdsOsGwHSubCGbX_c-SygxCd7HpnABLvOszPdl1JD5GCF4Do4qGpR1xNcLXIKTYnG8kIiY2vbbRDzvDd82IiY5ozR8tL9ieUrauRULBu9IBTMWTCoprdDQeoU5EaTnrjfA_yMmJpLNSvyH2A5hKtsBgsiy7ep5dJDKZQXm-Wv2pywph_kYdUW1___3VNZag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابلاغ سلام رهبر انقلاب به خانوادۀ سپهبد شهید موسوی
🔹
سردار سرلشکر پاسدار خلبان علی عبداللهی فرمانده قرارگاه مرکزی حضرت خاتم الانبیا (ص)، با حضور در منزل خانواده معظم سپهبد شهید سید عبدالرحیم موسوی ( رئیس ستاد کل نیروهای مسلح) در فضایی آکنده از معنویت ، با اعضای خانواده ایشان دیدار و گفت‌وگو کرد.
🔹
سرلشکر عبداللهی در این دیدار، با ابلاغ سلام رهبر عظیم‌الشأن انقلاب اسلامی و فرماندهی کل قوا (مد ظله العالی)، به خانواده مکرم سپهبد شهید موسوی و تجلیل از سال‌ها مجاهدت، مسئولیت‌پذیری، نظم، درایت و منش مردمی و فرماندهی تراز مطلوبیت‌های دینی و انقلابی آن امیر مومن، مخلص و مجاهد گفت: ویژگی‌های برجسته اخلاقی ، مدیریتی و فرماندهی شهید موسوی از جمله روحیه خستگی‌ناپذیر، نگاه راهبردی، انضباط سازمانی، پای بندی به مسئولیت و اهتمام به کرامت نیروهای انسانی همواره مورد توجه آحاد نیروهای مسلح به ویژه ارتشیان غیور و دلاور جمهوری اسلامی ایران قرار داشت.
🔹
وی سپهبد شهید موسوی را از چهره‌های اثرگذار، متین و پرصلابت عرصه خدمت به کیان کشور و مردم ایران به ویژه در دوران تصدی ریاست ستاد کل نیروهای مسلح دانست و تصریح کرد : شهید موسوی با برخورداری از شخصیتی منظم، مردمی و تربیت‌یافته در مکتب اسلام و امامین انقلاب، در مسئولیت‌های مختلف، منشأ خدمات ماندگار و راهگشا بود و نام او در حافظه خدمت‌گزاران این سرزمین با احترام و عزت باقی خواهد ماند.
🔹
وی همچنین با تاکید بر عزم و اراده نیروهای مسلح و فرماندهان و رزمندگان مدافع وطن برای ادامه راه شهید موسوی و دیگر شهدای اقتدار ایران اسلامی، افزود: تکریم خانواده‌های شخصیت‌های خدمتگزار و فداکار وطن، به ویژه فرماندهان و رزمندگان شجاع و حماسه ساز نیروهای مسلح ادای دین به سرمایه‌های معنوی کشور است و یاد و نام کسانی که عمر خود را در راه مسئولیت ، شرافت و عزت و اقتدار ایران مقتدر سپری کردند، همواره مورد تکریم تعظیم و احترام نه تنها ملت ایران بلکه آحاد امت اسلامی و و مجاهدان راه حق و حقیقت خواهد بود.
🔹
در پایان این دیدار، خانواده مکرم سپهبد شهید سید عبدالرحیم موسوی نیز با قدردانی از ابراز محبت فرمانده معظم کل قوا و حضور سرلشکر عبداللهی و همراهان ، با برشماری ویژگی‌های اخلاقی، تعهد حرفه‌ای، روحیه مردمی و اهتمام ایشان به انضباط، وظیفه‌شناسی و خدمت صادقانه به کشور و ذکر خاطراتی از آن شهید ارجمند، وی را سرباز مخلص و فدایی ولایت و ایران عزیز توصیف کردند.
@Farsna</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/436082" target="_blank">📅 11:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436081">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jz_Hu5kT9uaTU3K2pLoOt0sGGm1OiE3gjXkqeAexLt5onwB31RZA3C4KCqs_tiqBnLI5qv_8SxsGZxbFA1Qy0o2sS6_j-fT0PxHfPi2VAM-uEoOiMj_CTo8FFSxRP61w3UNlbCImPObNOgvxCdAJ3HlRo4M8tq2z4qggVTpxUlyiSzXZsRMEgcJjUM3vNEGI4T0tjjRPRU-zTJmaN3NeVeqtFNllVbB_RExqrKfsVxayG6V05eJjMMrNlSyRNP0-FoJ9-rgm9oNt7xikv7j2yHUAVkRgsWWL8mIrm9SGF-astS9RV-Z64KRBTNPzyI1XHjg4RqFioTXAJ-Yy95eowA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف نمایندۀ ویژۀ ایران در امور چین شد
🔸
پیش‌تر شهید علی لاریجانی و عبدالرضا رحمانی‌فضلی چنین مسئولیتی را برعهده داشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/436081" target="_blank">📅 11:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436080">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">قیمت تخم‌مرغ اصلاح می‌شود
🔹
وزارت کشاورزی اعلام کرد که با استناد به قانون اصلاح خرید تضمینی محصولات اساسی، دستورالعمل خرید تضمینی تخم‌مرغ را اصلاح می‌کند.
🔹
با توجه به نوسانات اخیر قیمت این محصول و نیاز به ایجاد ثبات در بازار، وزارت کشاورزی بر آن شده است تا…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/436080" target="_blank">📅 11:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436079">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJL9rYejc4-tvpU6BTk_qQjdGZh_LYh1XYAmeIiPL77991jyAC_Fy1ixq6gK2nElrrtFi65uKL6WV7dreS5hsWmXnlTSM1ib-ieRa2zVDPoASqycKoJcE5C4drUK4Acezwg8MmZNGqfNA2xuOeaYOflR_z6-1v2VjNp5JqtqLqvIQpUQA2Uo0c1IqYk9ajRdjkW-TKDqKyrMZxxZCnSUHMRd-OhAzMbPnL_LAr36YgKVsE8dnTzSfbo-U7cgFVjObzoXlZ28RV_o79eLaM0BOsPbSMajcbI1hP3pQIiPNxZHii_c82lDXRMvdmhyJthSq5rj0ueOEK0f3InA5qJ8gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقیف اموال مهدی نصیری و ۲۱ عنصر وابسته به دشمن در سمنان
🔹
با دستور قضایی اموال ۲۲ نفر از خائنین به وطن و مردم که از عناصر وابسته به رژیم صهیونسیتی و کشورهای متخاصم هستند، در راستای حفظ حقوق عامه و اجرای قانون تشدید مجازات جاسوسی و همکاری با رژیم صهیونسیتی…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/436079" target="_blank">📅 10:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436078">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
امیر سرتیپ سلیمی: شهید موسوی بر قلب‌ها حکومت می‌کرد
🔹
همرزم شهید سپهبد موسوی: اسلوب فرماندهی امیر موسوی این‌چنین بود که صلابت و قاطعیت را با فروتنی و تواضع در هم آمیخت و از همین طریق در قلب نیروها حکومت کرد.
🔹
اگرچه جسم و کالبد امیر موسوی در میان ما نیست، مرام او، مکتب او و منش او همواره در میان پرسنل ارتش زنده و پابرجا خواهد بود.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/436078" target="_blank">📅 10:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436077">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DijvTa2YFw8KNvEu4SGpC62he2CaKX7tApGUl8oqPxncpZyZ0qAoNbrTWiIvB3F5JtRBX28fHH47VTiXtvw1b7fE_Qm4MQAY_VuRJA9bUcviClIeHuEJg1_V0m9-oEdMzNzmVGOxxSD4obBdRv4qfjQkrIJdIWNwQqWN8_3s2q0StcvRDhpNHrZmF0NjGj-OSDKA-IuV12AevIXJGn9KeAxCxord4_qhUuP8bYksJfpXaSTijcwfUmXh9MFQuYE4yc9Vza2rEXNorijeib9ydkfOjBUZOjxvDZQRaRR0-7Yzxn9gKLpDBpJUyknu2MPYaPWWphr0sEUni4BbMmB2iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیانوف: حمله دوباره به ایران یعنی آمریکا و اسرائیل درس نگرفته‌اند
🔹
نماینده روسیه در سازمان‌های بین‌المللی مستقر در وین میخائیل اولیانوف در پیامی در ایکس گفت که «کارشناسان غربی معتقدند که آمریکا و اسرائیل ممکن است حملات نظامی علیه ایران را در روزهای آینده، اگر نگوییم ساعات آینده، از سر بگیرند. اگر این درست باشد، به این معنی است که آمریکا و اسرائیل از اشتباهات استراتژیک گذشته خود درس نمی‌گیرند».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/436077" target="_blank">📅 10:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436076">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دستگیریِ کارچاق‌کن مدعی نفوذ در دستگاه قضا
🔹
رئیس دادگستری مازندران: یک کلاهبردار و کارچاق‌کن حرفه‌ای متواری که با جعل اوراق قضایی و ادعای نفوذ در دستگاه قضایی فعالیت می‌کرد، با رصد اطلاعاتی دقیق دستگیر شد.
🔹
این فرد سال ۱۳۹۹ در یک فقره پروندۀ قتل با وعدۀ نفوذ در دستگاه قضایی تهران و مازندران برای برائت قاتل حدود یک میلیارد و ۶۰۰ میلیون تومان وجه‌نقد و ۷۱۲ قطعه سکه تمام بهار آزادی دریافت کرده بود.
🔹
از منزل متهم تعداد زیادی اوراق قضایی و دو دستگاه خودروی لوکس کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/436076" target="_blank">📅 09:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436075">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDI-E-ch1CaCv3-NpcCW99Z7sckb0QPilsd0b835RNJpf7kAGvVOXo3Rxu0No6ibYahgwiEewXy9TBGihQTqyyWiiCWrs5NRSnSLdsbq1w-vBx5vGA0jKX9s74TIHNBNVF8cCf5FaN_sjmPhIBHRNEXNjJ_OWJfsiyE8PPJ_V_E7i0nfQKeLAkolCC8nL25Wx5Wn7ohf6pjNj__Ij5zp9G9qC3VhkhwP7E9ACI-QMewKmjDqW4qCnMKxilwDG5xVuilkQ3my0us0kFNTYemXFAN0crZ0AIrg-DDDuBlbnkO8psRPhynsY1OWSSUcy-CBfCIqLroLkGayxigQOEapmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
هشدار تاج به آمریکا و فیفا جهانی شد
🔹
رئیس فدراسیون فوتبال کشورمان به‌تازگی برای فیفا خط‌ونشان کشید تا امروز نشریۀ اوجوگو با تیتر «شرط ایران برای حضور در جام جهانی» به این موضوع پرداخت.
🔹
طبق قانون فیفا هیچ دولت میزبان و هواداران دیگر کشورها حق اهانت به…</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/436075" target="_blank">📅 09:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436074">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آغاز صدور ویزای عمره از امروز
🔹
عربستان با تأخیر یک ماهه صدور ویزای عمره را از امروز آغاز می‌کند. وزارت حج عربستان اعلام کرده که «پذیرش زائران عمره از ۲ هفته بعد از آن آغاز خواهد شد.»
🔹
امسال زائران خارجی ۲ روز پس از پایان مناسک حج می‌توانند به عمره مشرف شوند. البته سازمان حج و زیارت کشورمان هنوز مجوزی برای اعزام زائران صادر نکرده و وضعیت بیش از ۵ میلیون دارندۀ فیش عمره در هاله‌ای از ابهام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/436074" target="_blank">📅 09:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436073">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShGPE7MSg7JykOy9mILstMqJn2ovw8HajQqEEIzs5zRtwzxrijF44k_LY42B-Gjw_XZToICuCHijYTkeXV6VHw70WhLrHoy31B1SY638BWlH4tQssQxSb5EiDUuyJ88CdBbKXo8Syh7EIOvayT6o_x2Ohb47mEAhqI8gcEPMHwMadtxAKeGszZiAL91H55b0DjXeEJqh_lhjHxS8ddrRpkhTuxtzZz0kpC-rQbWvkrmJuwAZaYXWjPGsfL_jOKyRq-tt5NAsnaGXMjDmUSxVuwtwbeU82kX4AooNFGlbFrV5LgZIwwLbCnT3SrqGEmRXNfr7-tVTE8zzfulVPLxiCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر جعفری: نهاجا برای هر مأموریتی آماده است
🔹
معاون هماهنگ‌کننده نیروی هوایی ارتش: بنده در موقعیت‌های مختلف مسئولیتی، در محضر شهید سیدعبدالرحیم موسوی حضور داشتم. ایشان در هر جایگاهی، یک فرمانده معنوی و دانش‌محور بودند که بر دل‌ها فرماندهی می‌کردند.
🔹
چه در «دفاع مقدس ۱۲روزه» و چه در «جنگ تحمیلی سوم»، مجموعه نیرو‌های مسلح با هم‌افزایی و براساس تدابیر ستاد کل و مأموریت‌های تعیین‌شده از سوی قرارگاه مرکزی خاتم‌الانبیا، نقش‌آفرینی کردند.
🔹
نیروی هوایی ارتش نیز تمامی مأموریت‌های محوله را در تمام ابعاد به انجام رساند و از این پس نیز مطابق با نقشی که قرارگاه مرکزی خاتم‌الانبیا (ص) و فرماندهی ارتش برای آن ترسیم کنند، هر زمان که لازم باشد، وارد عمل خواهد شد و مأموریت را به نحو احسن اجرا خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/436073" target="_blank">📅 09:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436072">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cf53bd474.mp4?token=Kbos3pC9HOoFFPk9as2raugFJihucgy4FEZLK4Off_zk9Bo9rZNnP796ngjV5EA__x1ThoH0yW5nxR6e2YrUze_H2hIk0oDfwRIdb9YI0PCc2CadfROSoVvvSk9ILmaO8fV76joWhvcuqZ_OeVzMTw7DwT-VtibBo5440hVXgoBiJjQ3gMyXf2d3YA8GmwmIcTV3XxmGd07QVFQ5M4JdacWWvML3aO3eB1-xKHyidPPS-Gypr0UsssulVG7YkRaTjXfRG-1JtqID2jpbsK4YXgACCH2wxXn5uVVB0Vx3dvIoqVzNaLFMiKulhmz_VGDirT3mooMDggePcOe8NA49Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cf53bd474.mp4?token=Kbos3pC9HOoFFPk9as2raugFJihucgy4FEZLK4Off_zk9Bo9rZNnP796ngjV5EA__x1ThoH0yW5nxR6e2YrUze_H2hIk0oDfwRIdb9YI0PCc2CadfROSoVvvSk9ILmaO8fV76joWhvcuqZ_OeVzMTw7DwT-VtibBo5440hVXgoBiJjQ3gMyXf2d3YA8GmwmIcTV3XxmGd07QVFQ5M4JdacWWvML3aO3eB1-xKHyidPPS-Gypr0UsssulVG7YkRaTjXfRG-1JtqID2jpbsK4YXgACCH2wxXn5uVVB0Vx3dvIoqVzNaLFMiKulhmz_VGDirT3mooMDggePcOe8NA49Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اهمیت منطقۀ محل انفجار در فلسطین اشغالی
🔹
شهر بیت‌شمش واقع در غرب بیت‌المقدس که محل وقوع انفجاری مرموز است محل استقرار کلاهک‌های هسته‌ای رژیم صهیونیستی است.
🔹
پیش از این برخی از فعالان رسانه‌ای گفته‌اند که احتمال می‌رود کلاهک‌های هسته‌ای رژیم در پایگاه هوایی…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/436072" target="_blank">📅 09:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436071">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-01PTGe2e6j1AsAnf2O0fI96x9zGBTIb_K1b1ENwYKH_YeHo0Rj-Z_o5bQkepl-cKC_mF7up6kqWd_5IUijBs8tb_vRE6NieUKL2CeSqEq6XKYAj7t12W0LBER-WfujSBhxH8F3zv2RUJ_k4nzfax_LZMR0x5-ElhNK506rqYtAkN9DIVtmyFrVPkHQpO3dJlYxgueVVv7Ky-IqDbQ6_qEczpm3U13qwk63ptXM9UhyzbrSNl_rT-A2SLhoNBgqq-nykXl0Y2v-NaC6QglrBYtB_RRCF8Pw2xxF-VZ2K-RPAPM7vh7Hj81LjNhZuvbwbGI6VdMaZR_MulA8KEsSAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حمایت نخست‌وزیر اسپانیا از یامال
🔹
پدرو سانچز: دولت نتانیاهو از یامال به‌خاطر برافراشتن پرچم فلسطین انتقاد کرده‌. ما از همین‌جا حمایت کامل خود را از یامال و مردم فلسطین اعلام و از نقض حقوق بشر و قوانین بین‌المللی توسط نتانیاهو ابراز انزجار می‌کنیم. @Farsna</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/436071" target="_blank">📅 08:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436070">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c5b035afa.mp4?token=CAPMThxLz3rcnAVwsaGQshILCv6gmNwReGOSaJBrRoN1CCJG8VlWP3RB1ksnsp1KiV8t2XCmxRWIAnoTjO9Vw843ipe_qWks1wypus1UVOR0F7sLGFqKxI3CEgioB1bMJ9P7JwOoefj3fkW4VnkRi3hFHVH4yChkbbf1xSkwz_uYbkAIt5zJAQOXa9y8wJJEE2W1OX6z3cFcZqsZBXwb80w7nuBicGPm37swDDp8uJL-r_h9ESL53w2ejr3Kcj6c1KlPCV84IFKxZP1-yg7Kng1RCEIVYANwGzmyCfgcKU1GVmrvB0r6J_idHdH7lPQLF9dv4NNM1Ov6IRRwTrOXKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c5b035afa.mp4?token=CAPMThxLz3rcnAVwsaGQshILCv6gmNwReGOSaJBrRoN1CCJG8VlWP3RB1ksnsp1KiV8t2XCmxRWIAnoTjO9Vw843ipe_qWks1wypus1UVOR0F7sLGFqKxI3CEgioB1bMJ9P7JwOoefj3fkW4VnkRi3hFHVH4yChkbbf1xSkwz_uYbkAIt5zJAQOXa9y8wJJEE2W1OX6z3cFcZqsZBXwb80w7nuBicGPm37swDDp8uJL-r_h9ESL53w2ejr3Kcj6c1KlPCV84IFKxZP1-yg7Kng1RCEIVYANwGzmyCfgcKU1GVmrvB0r6J_idHdH7lPQLF9dv4NNM1Ov6IRRwTrOXKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجسمۀ طلایی ترامپ یادآور گوسالۀ سامری شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/436070" target="_blank">📅 08:21 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436069">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سامانۀ بارشی به شمال کشور رسید
🔹
هواشناسی: امروز یکشنبه، گسترۀ بارش‌ها در آذربایجان‌غربی، آذربایجان‌شرقی، زنجان، اردبیل، سواحل دریای خزر و خراسان شمالی است.
🔹
در دامنه‌های جنوبی البرز و نوار شرقی کشور افزایش وزش باد و در برخی نقاط گردوخاک پیش‌بینی می‌شود.
🔹
امروز آسمان تهران نیمه‌ابری، در بعضی ساعت‌ها افزایش ابر و وزش باد شدید و گردوخاک با احتمال رگبار و رعدوبرق است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/436069" target="_blank">📅 08:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436068">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CR52taIybJu5INBZfudHGZ8Actph12QBnKrsV7wWhRTtKV0El8-0qcIXazyKIhamjYEXTrnG4cduFAuqy1LsrIIsw_urXLiwW3JWtBhNoAz9IcIEQ_5C6mFwjxHjX7yqCSvPu2G3RdlwBbKahAQt_wSc8I9emOLmsB6N96qamDIj9m5XaplIOv8DgZvomTL99kM-xKoK7Owg9fyO4pOZ1_NSM7fKJAB4wsbcYDo7dRiw2i7GEATymJq6_hTLzJyM7FT7U8gxb-z7sT9cOpFwZn-DHCc2PW1o63BQZQBAjH35ktUgrX5ECiwsxCLD0N1qmJslsyfEZwJbX19Mosf2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنفس قابل‌قبول هوا در پایتخت
🔹
بر اساس اعلام شرکت کنترل کیفیت هوای تهران، میانگین کیفیت هوای پایتخت هم‌اکنون با عدد ۸۷ در شرایط «قابل‌قبول» قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/436068" target="_blank">📅 08:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436058">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qr75kS_emK8sqzYmSm8KJ2gsjF22zrpIY-yfMFov3gMK8IPbXqcl9df9lib4UCPZ01tT1plUGpsMaDWZAF3Qfbkbq6uSbitxh83W4K_GyKYik5Qu5G5Ixij-_yKGwK8NbFLFzZRLtdw_msqGHOAfQQ4RgRR2XlHomdyEiyTwPg99n8huIzcz8DxqWknBdNtvmFCRf8K1uqodpB0FrCDHTWY4GPpeSz5y-I8Bdr1tpSd4y1IY0ob7R-onvm1UwHY-wUTz5KpETKI7bcO3e4zLJ-Lkj0k63P5q03L1I0uUKkDR9L88TGD_2OJPKa2tdUtdCHEQ3yrhLyblNkps2pNEwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ffSbJrwVfTP7fhXxx8SDfcMItnnbWdAGc-xu9XPRtepkCL3YpUvnULnB0HWzIlp0z-5Bg3VcRK_y5RbhMT3GlZwh7BhflgmPBaudYGiXOdBgDNEUgpaFkg_bm416Cy40CuvJXT0vFyV5hFY13DD71qFS7MzEY0b0ifKMyzw57xJSMfwRqTOX1Q_Rgto5mb1W5cQGz3hRh0dNniF1HAhxITbKqo40Ypwu59PweMCmbcognu59vQqi_kPzBSgzlDgxaPvmkiRVfyRCINpZTqe4iraoz608-UmUut9QGQihZd4H9MjqlTjwEYfLaG8j7g8FOhJ-ZLfyFNVOcgIhpGCS7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MvdQvsVzv4QI2T5_-2RfBy6cbYfQ7bSfHVJqw1APM4YgzEo8aA7UfDPYTCNbAVvN8k7ZoEoVa_YkHeAwkr8IIHEAHEjZU9wXYuq9Cg7VJKwPNzyu65beSIZQisqa7KPe3KobIMYDHun8jBQwxgbZeYumd30AhDVRKNYMrqDzIISoi8esdE-8w9sBNvUx-vZsRB-XCpAEr618UuEi7gPIF6--b62ra-lsPFPmkWbpIEUY5QiwhRhXZVWsNfsjMCGKUZCtl5WV98o1brihTxg0ioncsEADPgiF2hxsEpnfl5D2OasDwzkqYJTBdxIbTdeN5ewSFovS6QKvO1TfnjJ6GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TIDrA0DI9Gi1FhhgsRnnt4bbYFQQrfoBrryBzRts6L6BK0R-BL0TYcUNTIvPuycAl_YBW2sY2HqvFwaVK1T7Uk0KDvNsQ7Yk22jWgBQ7rfmWV2SJRyJACC0vHtjcI-h1ovSBtjYIpq1Lcm6jHLCFUQWeXlkID5rSaiPDrMoHHBPnpeYNOfJwqurx4Rye8I-UcngrtLYH1IrO2KgPF3ZvXyvk7Ml5sDxPfKQWWaeFOKAE-FglTLYB01EUL92TWl8eqPorpDhkZ9c7-Up7AglRYhf_lgEOdwPQu41nyqBrQHFoFADywUav5PlzL26vAEeKsDiBXMIbzm_OndW2d1ZMaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FwJxiOIlJV5xwc5xAMLZ0-p0atOOAjrsQC2uTqtPl1qn555Rk04SXdLRZx47zubNwTQQnM5DNWq1bL6_igZSd50j4i_QxGhPViJvi28uDLUrCHW4wE1cXjPPZgQsNa-IUhghscjPHG5PLRwOacPT-IgbFi6bY2u4aUKR78TVVp8yLV_ukYUda9G1A1Ne6W4bi34ltVdiHnEtERflXT5YfWXlWjn4ilNg1XbCICZPbk-gD2T7JWLyA2xZJavAvkZsuQaLCmmOI91IFZDh2tZWuAGM3yI93o5ntTF3TouZdQg6PZvNuWVQ8I5icHJrFq-tixLnUc62jW-cbs07WXIByw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mEFm6zNfxXD9IK35OuulMlU3L74rOsQc7CMrzJ0Qwk0EY6qntmJhENgkISd5tcmgecXhcTUdgS3wFJI5WsuLlZCsuPVsZcOXBS7m9ACBF82SAFCDcJbRUS1m_t8gjTSP_GjWxjUyPNTHm7ynBoWsPIs0_1VwqU41nIzmxl4GsbLsDzMHWwf1ChZ9XTrMKnVNLtOekf1kycFbZ5kZhtzBXHdR4wF_R4wseVzSw0Mz4Cs62H3rPwok0Y3OTXrabAlxfBUv7DIEd4MOwjCHtTP6vT9dgpoylltO-Bj89LZl7YNrD5QbepUHUTGre74BmmT4tC-BXP3gVV59M_EjlL4CwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BrG9kKP1UxZ8esefZlE76Ux92BjS2wX6PGMPi1kn9hbNmE22g1khOcB3-OpRhuPgY1koIxheepJ_JWe53uQat8Z7vNEbwKsCZKtrCfYIvLrHrpeSdakSHsVoQBy4RB8HE9mFt-1_Ze1_EO-X3QWjkHIrKTiA4wIAVEPsS7R4236v2o7V7ykK1gZLfrjjkig_nOH5Lq4Tu_NwXF9GbVAhHdcMCPQpv0VrSaQVaPQylcuzk3nEmrcGOBRNWrUR0Ct3CDJslnTHAzOzFqHXqebJdOTKVdapbkPTxBntZIDS6PekD2woTljTfPqgIvmgePfo50oIzpqatR3uJ4sXcOqexA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M2PPQe3rvPxk9lqogOT_u5YsW38zLb87rn_KI9kGBYd1yRxwyr8noivixSUaViW1HcZDCKlH7euOuHvfbWhIM42jqkpkQFeE8XkB095IfawLRcQb2qS_exgQyQGJkAZDyGfs3yKkbSYOvxBaMlv6bAi5oB4zsrMfT9AerLdxBwQrXTj9n-mceWwe1ObVPY4dcX0OM0LMwOZUB6NDef03EY1pFKg31dIWjigLMocOxh_8htABLD0E5_tbfbExKCP6K3WYlaaQmwy-3gdMnbN8vQuXweLBNDz1aaMulpxK_To59EBf7aWRqE_1MJrEFyubzjg-uNdaldogWjYrNcREQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LgIGEjtHKYU6UnaGxlu3RlbhBNCBqjVj_aIngomfAkpi4DDl8IsLeyVT5308u5h12HuTvxPYx1SEizVS8gmFylMCfYFZqf9yAIMr-aqlET8867qKN1igPKH3vjl5frd9iMWpdd4S5DZHFt9c3AQmyguknaFzCN9QDy5VpcFg6_bbZWHka7A1RGHhoPumkRuVMxUYFOx7CD-rZLxoVRbJpr_him3aWNngEG_XJ6E3ZSrQxTEQmci_hffsK2g3MHz2mfryV3pesUz0B9wOGDdK-6VsLM04ZWCszTK2THOk4eoWhwMvRScki_N-7cTNhQoUseezx1ebi3PrKgjvl_fbBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JNnJ5CMAG37nrUwjMPZ8_hDXMtAaXQcJT_oCAkfLOLCYh4Y6vXozjUclOU2GjYe6TFWz3zn9fATEsQGaJBEX8pPVnDrMXFZufZ3_3qVCs1M1XbXQOFfbVekiDzMZuZUDBjSBvcnjJB93ufluPpMfEmThpocoEJPNt_0nLNfg2FFxUi-sDOXthM385SLpvFZO7X_e6voh11e3Qni99dftOsss0NI3zN0STM5sJSaPti3AurIuSJzzhZ7OdqM1ZA8ovOCo9L4h8_vXnCdCvNWBWwBCH7drNQnpzI6aJkAItwIFHTZGxVsXeSsVxdTMwaKBDdiBG5ixFW5CeOa1zovs1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نقش‌ونگار زیبای بافت آجری دزفول
🔹
بافت آجری دزفول، با آن نقش‌ونگار گرم و کهنِ خشت‌وآجر، هنوز از زیباترین میراث‌های معماری ایران است؛ اما این هویت شهریِ کم‌نظیر امروز زیر سایۀ فرسودگی، ریزش و بی‌توجهی، بیش از همیشه در معرض فراموشی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/436058" target="_blank">📅 07:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436057">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🎥
معلم مدرسۀ شجرۀ‌طیبه میناب: هنوز بعضی از اولیای بچه‌ها تماس می‌گیرند و می‌پرسند بچه‌ام روز آخر چه می‌گفت؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farsna/436057" target="_blank">📅 07:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436056">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🎥
عکس امام شهید و رهبر انقلاب در کشتی توقیف شدۀ دشمن!
🔸
تصاویری از داخل کشتی توقیف‌شده در آب‌های خلیج‌فارس، توسط دریاداران جمهوری اسلامی ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/436056" target="_blank">📅 06:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436055">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM7NlhlYttmaY5E31fdr4tg753FbOj-iq-PgnDNa3OTzZ2fVyLzqFjtmDKoDZEeg8lgBkrPxgvazOJfNbZelGuPYeZSeYW8wgOtMVxP4BPO00sguaaKn8o43xZKjB25Q_W_Ygmbzof-twjrhjS1JQDYeG_h7ozIX6IR8L3L-nSIXoqAYMea0W_n0Bm8MRJ8wf7xH0761lru6mn-XVx-0mWsnWKQ8xEoB4BpjIoZn8yTqGxmVecnXicBJZwFCgCJuqlnWE-be4qUT9ctDWppfCnRN1ahwesoAcWL5hpESmjJ5plCu9rkttcBbS9CgeyAqXTH65vBD-3dSR-XjS0N3gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسوایی پزشکی در دانشگاه‌های آمریکا؛ فروش اجساد اهدایی برای آموزش ارتش اسرائیل
🔹
رسانه‌های آمریکا گزارش داده‌اند دو دانشگاه مطرح این کشور، اجسادی را که شهروندان برای تحقیقات پزشکی و علمی اهدا کرده بودند را در اختیار ارتش اسرائیل قرار داده‌اند.
🔹
این افشاگری باعث موجی از نگرانی‌های اخلاقی شده و اعتراض شدید خانواده‌های داغداری را به‌همراه داشته که این اقدام را «خیانت در امانت» می‌دانند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/436055" target="_blank">📅 05:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436054">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcaa9f3eaa.mp4?token=Std_8tgtfMdHuu_CXIKwUwEkLx0Q8nSI_R6gsaF37n1ZS4CaxXZeb26NKNUuNGY8AKU585EbrnJi_cUwIfXplWiaVxH2yJBcweuwUNQroPvNg2neNfvz_bJaj8K1IZYdfut9_zwd1QiVaVMqgAO3ZyVkFDTsCw_oF1RyCDETsd-Wuy28HTEUtneQBDoJzQlZTc0125oM7G-pE_1sgbZUEwYYcivlR5owvbXcoEVA9zu3FgDqepcmwCdONzuQvj_AcToekChQ0So4DbbN-UnoVWxX3v0ApDF3E1TeaJu3EOum22CUOiy_knvBh1icm6_6jClni1vKArkmMG93nsucbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcaa9f3eaa.mp4?token=Std_8tgtfMdHuu_CXIKwUwEkLx0Q8nSI_R6gsaF37n1ZS4CaxXZeb26NKNUuNGY8AKU585EbrnJi_cUwIfXplWiaVxH2yJBcweuwUNQroPvNg2neNfvz_bJaj8K1IZYdfut9_zwd1QiVaVMqgAO3ZyVkFDTsCw_oF1RyCDETsd-Wuy28HTEUtneQBDoJzQlZTc0125oM7G-pE_1sgbZUEwYYcivlR5owvbXcoEVA9zu3FgDqepcmwCdONzuQvj_AcToekChQ0So4DbbN-UnoVWxX3v0ApDF3E1TeaJu3EOum22CUOiy_knvBh1icm6_6jClni1vKArkmMG93nsucbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکوه حماسۀ خیابان در شب‌های نورانی اردبیل
@Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/436054" target="_blank">📅 04:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436053">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50621f1431.mp4?token=ivQJay-0hPv8uNB6SGrEa-1DwMUAAy6mgtL7YIwrnx51vhiqgcOAZ6G4B5FWhycYOgsNdtm7qrwh1gFJaLrTrtFb6KUOvuA2rzgUtA99oNTWXy7-XKIvfnkgdH11uIUKVKVrwffqm4OfBevm53aZulTQ_jlN16YWPOzhQi0eY9MUfjFzow06_mkkqJZqyvaMCjQnHsMN-usQ3VEpGlYjaT85ccCASGLWAOtGnSeCbVmmWuKfAXLUQfRKOxXoXZM9N4Wv1FshWhtv-kddi0KZsEdYhjnU0ykVv-Px1WC6mH13mSidccSIyx_qDOanZJecwl8roDm8FxF8Di73gDrzDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50621f1431.mp4?token=ivQJay-0hPv8uNB6SGrEa-1DwMUAAy6mgtL7YIwrnx51vhiqgcOAZ6G4B5FWhycYOgsNdtm7qrwh1gFJaLrTrtFb6KUOvuA2rzgUtA99oNTWXy7-XKIvfnkgdH11uIUKVKVrwffqm4OfBevm53aZulTQ_jlN16YWPOzhQi0eY9MUfjFzow06_mkkqJZqyvaMCjQnHsMN-usQ3VEpGlYjaT85ccCASGLWAOtGnSeCbVmmWuKfAXLUQfRKOxXoXZM9N4Wv1FshWhtv-kddi0KZsEdYhjnU0ykVv-Px1WC6mH13mSidccSIyx_qDOanZJecwl8roDm8FxF8Di73gDrzDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اثر انگشتان‌مان سند وطن‌دوستی ماست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/436053" target="_blank">📅 04:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436052">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تمدید یک‌ماهۀ اینترنت برخی مشترکان مخابرات
🔹
شرکت مخابرات اعلام کرد تاریخ انقضای سرویس برخی از مشتریان پس‌پرداخت فعال را یک ماه تمدید می‌کند.
🔹
بر این اساس، مشترکانی که موعد پایان قرارداد آن‌ها از بامداد ۲۱ اردیبهشت ۱۴۰۵ تا پایان روز ۲۰ خرداد ۱۴۰۵ باشد، به‌صورت خودکار مشمول تمدید یک‌ماهۀ سرویس خواهند شد.
🔗
جزئیات بیشتر را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/436052" target="_blank">📅 03:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436051">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2562f833e7.mp4?token=ZIsrmx3YNq8Zdyb2B0G4G9rT1EV7IxGOvFoGgV6WTpgd00k5m8KHHU_-ySIViitxsncswCBjqABTIQanUzGTsGM8ksEGqX550I6-pDxaFCBwYdaDX_r4VcWGwjh7LtHiKiNEKkyqKw1lLQ_2rDlg-ska_Y5XJm17i2D1ectOuGTtGWfqdzdSUlAoYRJyI2-llGde3GQMc7k7EflcEL5tuGd0qhGpNnCgcl7KgF4ubcYsa067uWSbimrBd5erz3M-M9qa9pXOO_ZlescKFMs972Z4hGWmVMcQlXzT7J0LZQPE0wreHMkm52_Ivpj1wltxLO00FFYbYrkZqlNbqPkUax_HcU2O7EWNidsPm0dGLHnUhLAM2r2XMc8ZPQlsn8Z61MIexC8OlQq-za0hQn5AeIgMkjAmH0c3NecTJFWLbGHqZe76qwubeCvDmgIEoAq1-Po-kJpd3y16OWd8hgeu7cnnIYHGltNMqvfrN9MyX8DeVYLg4vAbDGfU9IogztN_LbvuMzUGZKueB_tMG68CyrI9qJc5bTpuIo8Vys-KFhpwvbmlNw4pO3F4hSG-tXCW5_Uo753xzym7istu9gTDIHbicgA8nBCD3HCaCIlBpvtOH2IQgpT-qydWG-wo1VC4fvjULUSPNn4g5gRPHJ_Xuv1dcjlV9uCeyTkuT_z2QBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2562f833e7.mp4?token=ZIsrmx3YNq8Zdyb2B0G4G9rT1EV7IxGOvFoGgV6WTpgd00k5m8KHHU_-ySIViitxsncswCBjqABTIQanUzGTsGM8ksEGqX550I6-pDxaFCBwYdaDX_r4VcWGwjh7LtHiKiNEKkyqKw1lLQ_2rDlg-ska_Y5XJm17i2D1ectOuGTtGWfqdzdSUlAoYRJyI2-llGde3GQMc7k7EflcEL5tuGd0qhGpNnCgcl7KgF4ubcYsa067uWSbimrBd5erz3M-M9qa9pXOO_ZlescKFMs972Z4hGWmVMcQlXzT7J0LZQPE0wreHMkm52_Ivpj1wltxLO00FFYbYrkZqlNbqPkUax_HcU2O7EWNidsPm0dGLHnUhLAM2r2XMc8ZPQlsn8Z61MIexC8OlQq-za0hQn5AeIgMkjAmH0c3NecTJFWLbGHqZe76qwubeCvDmgIEoAq1-Po-kJpd3y16OWd8hgeu7cnnIYHGltNMqvfrN9MyX8DeVYLg4vAbDGfU9IogztN_LbvuMzUGZKueB_tMG68CyrI9qJc5bTpuIo8Vys-KFhpwvbmlNw4pO3F4hSG-tXCW5_Uo753xzym7istu9gTDIHbicgA8nBCD3HCaCIlBpvtOH2IQgpT-qydWG-wo1VC4fvjULUSPNn4g5gRPHJ_Xuv1dcjlV9uCeyTkuT_z2QBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسۀ هفتادوهفتم بجنوردی‌ها در میدان دفاع ملی، در شب شهادت جوادالائمه علیه‌السلام
@Farsna</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/436051" target="_blank">📅 03:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436050">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqO7gEIZ4idYtECnlnCTEe_W7F0gU9DLDvI_FZ12hCPm3HQFV79DROQoi90bDXyAKHo7WUKYx80reQZeV677i8G7BdVXOwZiOKdKXFCBnyF5YluznFDISBAkceFp31CEyWU2iT6zOWKhuCUeCUc3aYpST7NIcnCyBr_-dR9j8mQD76yBOV3pSmrBUEvgrD8_fhnT6Cl54OG00iaOpG-9rtZYIL_PHGT8zQf9OSjefntZwYyupbbDuvlAT43uKN0ozCqPvF4dSmmYzu1gApSpSUutPMFBaA-ZgYg8q1_Ig1Z_0zj5SbPZqdfCQiIBp-UQTRqsi5yaEtdiiVFIIvbCdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف بُن کتاب برای اقشار خاص، در نمایشگاه کتاب امسال
🔹
خانۀ کتاب‌وادبیات ایران از حذف کامل بن کتاب برای اقشار خاص در نمایشگاه مجازی کتاب خبر داد و اعلام کرد تنها تخفیف کتاب ۲۵ درصد تا سقف خرید ۲ میلیون تومان برای همه فعال است.
🔸
این درحالی است که سال‌های قبل، علاوه‌بر تخفیف برای عموم مردم، اقشار خاص مانند دانشجویان، طلاب و گروه‌های خاص از بن کتاب برخوردار بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/436050" target="_blank">📅 03:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436049">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8837b94349.mp4?token=g2enLBGAY00EojQAIhZbAb2-oy3T_0vSxnEa8kGBEEPELCOwFJ1OXcA9Z12sCAhPAKu-O5n4g97iNWE8-wp3fWIWbY5ia561XPXzvY2rEIBThvfDWQUUD0070NcgKLNFXAIJp92zzesubF1b9KgwFIE8jiWwtm-JDKvhKvQNM6tXri7UlnkhXwf08gB2kULYeidDIBYXcg2f-AFUsrQO5RhDCs330mB3qbdk1yHTLDChJM7npLrrWzAsVJdJLgvqWQsbwGE91Gtc1HTMKTg_LBufFGzpbJaXRXThmpTEic0HTRNohUkhWsAX9Dbc9gH5QShxzFgSQGzyGZlQtUD4yVcxWnwKb6_h8EDSRTf-GOOq6VHPONEF4IxkbkxsJmuGfHcgS49SnLuBrje-ntH1gaCqoPN_Oka96X6HFPDgYc9mqck5VoDrkeXA7HGtz2KsR0piyoWHWk_wZ7qrIIUmU_Ikdicz_fX6-y8jpJ_RmeXfowu0734Yn3D9O-YGJWmCwDriFchvFBONaAHafzrdbSVTAA57TE6WZQS1cV0WduY5bL1si1rxXMspWwOvq4swg6QhIAVzgEMvDy9036grYj8XzxK-4C-u41eaaPCQ9pBuyA7sUzFSbHPGYnFtjSqECVW-o6CwcttmjBC9Et-OR8kciSrRxDVK9hJylpB5D1c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8837b94349.mp4?token=g2enLBGAY00EojQAIhZbAb2-oy3T_0vSxnEa8kGBEEPELCOwFJ1OXcA9Z12sCAhPAKu-O5n4g97iNWE8-wp3fWIWbY5ia561XPXzvY2rEIBThvfDWQUUD0070NcgKLNFXAIJp92zzesubF1b9KgwFIE8jiWwtm-JDKvhKvQNM6tXri7UlnkhXwf08gB2kULYeidDIBYXcg2f-AFUsrQO5RhDCs330mB3qbdk1yHTLDChJM7npLrrWzAsVJdJLgvqWQsbwGE91Gtc1HTMKTg_LBufFGzpbJaXRXThmpTEic0HTRNohUkhWsAX9Dbc9gH5QShxzFgSQGzyGZlQtUD4yVcxWnwKb6_h8EDSRTf-GOOq6VHPONEF4IxkbkxsJmuGfHcgS49SnLuBrje-ntH1gaCqoPN_Oka96X6HFPDgYc9mqck5VoDrkeXA7HGtz2KsR0piyoWHWk_wZ7qrIIUmU_Ikdicz_fX6-y8jpJ_RmeXfowu0734Yn3D9O-YGJWmCwDriFchvFBONaAHafzrdbSVTAA57TE6WZQS1cV0WduY5bL1si1rxXMspWwOvq4swg6QhIAVzgEMvDy9036grYj8XzxK-4C-u41eaaPCQ9pBuyA7sUzFSbHPGYnFtjSqECVW-o6CwcttmjBC9Et-OR8kciSrRxDVK9hJylpB5D1c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکوه حضور مردم مشهد در حماسۀ خیابان
@Farsna</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/436049" target="_blank">📅 02:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436046">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uJqagy4uuIaTUw3r-ROCA168fwTRV1os1EKPS-rsMOw0WQux2Ifnv2IS-tb0aWELt_817hTqjN2o-bBBAIMWF9Ul0eMNxyBpQKrrl8smKYpwRnSr8reuHlrqfkuNYlN9t1dpBlmuXE2giQ_0sKtEqDTAIh_SaH7RoJjkklXeHlAwea7EQmOn2uiHUSTIwqVI1GizgUv6NXp-y_OLtabIzJ0pGOaPRpl9Unk4wP6NkfPwmnrjNyQRAphR5JgOwfP-pyR-YWk6k9Oh2a6UWUAdgPHsnoNUWvqbPl3MQUyX5PSugjdb8e6WUQNGvZWYJvyIhd3NzQqm324tcXLuNk7mjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DqMxNk2GlSPXBaiARIOC8cc-sen4A0yvcykcDpa4Opk6gWqbXoXlHYpD8taOmm9I-0ifUDh3qt4hnH2yWxsNvJbWQwc5HTZgxg1QUcvPw90HiDLddnAMJDElu6ebL2UQfeyIlmJ74k5z1gacSoV2gDxkozJkCzMapC6BQRsY7N_5h7qeQgrU5jDj0aED0EG-OCTvHoO-yHQ1cdyfeEOmo7rWBm63pcpq7yN-nD2B7EBfXoRb1zd0cmv66z9Jk3C9fb4VnljBUqJUAmjYplKAsbaP0yPABhdzOiT1yWgWPoh8IJau5ws9EIETrvLNIQmwVY1j0qRaD9EcBrju7uC8jA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2670167992.mp4?token=DRCDtLu9_Ian1DZZTB1b2hHWraCCRjlMxpegab6CL-BY9nkSKKIoXCLn7m0K3vozoPCGqglJq1wWj5Myn7FBI6dxn0jyvbeTSoPAQkKAsmD1dmnaiMGbJFxvlUtjguq4NH_6jNDfZks0oK12VmcHtt4-XMlK-xY3M3L25aSI3PPbvtBRKdYthea0wa03FftMi3mkhHrzPhMm7hd3AH9EmNe09_P0u00cKKB4rxGxbuHspjss1OPrnaWU2m4w1aFWhwMbhLPATKcZ7r4xpvgoKNQ2imqUQxxfrVur0JDTXRIq9kBkQrfWkWhyIICe5cYanauS-PyvMbkx3WQFSkKulQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2670167992.mp4?token=DRCDtLu9_Ian1DZZTB1b2hHWraCCRjlMxpegab6CL-BY9nkSKKIoXCLn7m0K3vozoPCGqglJq1wWj5Myn7FBI6dxn0jyvbeTSoPAQkKAsmD1dmnaiMGbJFxvlUtjguq4NH_6jNDfZks0oK12VmcHtt4-XMlK-xY3M3L25aSI3PPbvtBRKdYthea0wa03FftMi3mkhHrzPhMm7hd3AH9EmNe09_P0u00cKKB4rxGxbuHspjss1OPrnaWU2m4w1aFWhwMbhLPATKcZ7r4xpvgoKNQ2imqUQxxfrVur0JDTXRIq9kBkQrfWkWhyIICe5cYanauS-PyvMbkx3WQFSkKulQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله با خودرو به عابران پیاده در ایتالیا
🔹
مقامات ایتالیایی اعلام کردند در پی ورود هولناک یک خودرو به پیاده‌رویی در مرکز شهر مودنا، دست‌کم هشت‌نفر مجروح شدند که وضعیت چهارنفر از آن‌ها وخیم گزارش شده است.
🔹
پلیس اعلام کرده تحقیقات برای کشف انگیزۀ این فرد و تعیین عناوین اتهامی او ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/436046" target="_blank">📅 02:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436045">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbqwW7m1MSXOjwxC3qDOg-cyjqHDZsOr9kdKLMLlDjVkwvTowXbx9zuPCA-o0mUBrOYtNDyLQ6PXKDvb6bJ_phNWFqMo6vMwNpZM2RYc9P_0r_zA_j96-WnUwp8RrW1VakOZ7rPw7LKQe7XQtf8HX_gcJPiVBS8YVCKPB0ns1CPrTcB00M5aZjJqfTk31wpeljRqr71uRyBTgAboVBk8R0MvC_4rUUa0Y6tkyx69fpvNXZc1S3k3JnTSbKNETXTUpqHXNSb6kH3i8hhCpOczi7Lgr3tEsxH1HM4oY3FyY_IBUyJRXfxiH3uqpXlytqHI-Oodn3asqp0Q5Fop__rg7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیلی‌میل: نخست‌وزیر انگلیس قصد استعفا دارد
🔹
روزنامۀ دیلی‌میل گزارش داده نخست‌وزیر انگلیس به دوستان نزدیکش گفته که قصد دارد از سمتش استعفا دهد.
🔹
وی به‌تازگی با شورش در میان اعضای هم‌حزبی خودش روبه‌رو شده است. همچنین بیش از ۹۰ عضو حزب کارگر در روزهای گذشته از او خواسته‌اند استعفا دهد.
@Farsna</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/436045" target="_blank">📅 02:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436044">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎥
کرمانشاه، عزاخانۀ امام جواد علیه‌السلام شد
@Farsna</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/436044" target="_blank">📅 02:21 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436043">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حملات گستردۀ حزب‌الله به مواضع رژیم صهیونیستی در جنوب لبنان
🔹
حزب‌الله لبنان از حملات پهپادی و موشکی به مواضع ارتش اسرائیل در جنوب لبنان خبر داد.
🔹
بر اساس این گزارش، پادگان «یعرا» با پهپادهای انتحاری هدف حملۀ نیروهای مقاومت قرار گرفته است.
🔹
همچنین حزب‌الله مقر فرماندهی ارتش اسرائیل در منطقۀ «البیاضه» در جنوب لبنان را با دو فروند پهپاد، مورد حمله قرار داده و خودروهای زرهی اسرائیل در منطقۀ رشاف و حداثا را با مواد منفجره منهدم کرده است.
🔹
بامداد امروز نیز تجمعی از خودروهای زرهی اسرائیل در اطراف منطقۀ حداثا با موشک مورد اصابت قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/436043" target="_blank">📅 02:13 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436042">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">«افت شدید توان رزمی» دلیل عدم مشارکت انگلیس در جنگ علیه ایران
🔹
شبکۀ فاکس‌نیوز با استناد به دو گزارش رسمی از اندیشکده‌های نظامی و پارلمان بریتانیا فاش کرد، دلیل اصلی عدم مشارکت لندن در حملات تهاجمی علیه ایران، «افت شدید توان رزمی و خالی بودن انبارهای تسلیحاتی» این کشور بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/436042" target="_blank">📅 02:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436041">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🎥
مردم شهرکرد ۷۷ شب است که سنگر خیابان را رها نکرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/436041" target="_blank">📅 01:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436040">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN5IhJ0hCiT9I01SjvvnBjBhKIbCHdhpjes13h3ocXVvAStYN99MWg9ytyYkEOlfEwKBbZ8tDQ-azKkZ4oHDwpEpwyY2Q359CJCvoOnzZ8_ee1oAVrV8ll9aqI92o7n6fQ5XGFn3O6sQgJFL8o26q9k_rpUpnPfaXkUaNR9xvEwWujRXhNoXz-OPVEcH6OCWZLduRfEmx-m5l_tTlUgooAr3bhPQvyW9cXS8Y_F6-XascwSWPhhmUJSHtf3VNwyIRYqmZnPZZj5uov4N8dA9JOzViZqswuLR2kKzoXVQCHvTb34RHl-PbTNYee9HsKzw37qcKFrqeV08VTTTQhQfOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بیانیۀ وزارت امور خارجه دربارۀ ترور فرماندۀ کل گردان‌های قسام در فلسطین اشغالی
@Farsna</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/436040" target="_blank">📅 01:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436039">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b65eeb3c1.mp4?token=TTn47-Nz5APsPWDEwdZJGglhXhwCe1VGJI40m2bArrV5w2Xn4yiRWlSlmORYSHuhyVF0hEOVN7HkT4MKhZfG7ySvqyuurChlyguf6BrGKWu-qsDH12MmoHtenVUok57nEO0OqpDWrZcstwQvq59yV9b5pCVrt4ZQi8xNW5RGdWV24PvzaDQpIOP6ysvz1D0HItEuCWx29jRcJZx8pGBqLN57R0ntw3dRzNZM7flHrIOS6LKclQWSWx3rdSN7sPEuqw-mnaajgYtPljRUdEwstjUym9Z9ZOFz4kZBzvYcDrb08jd48NeJEQS8K4IaqH43RA6TXaeoU1AAATh00sHpFyG70o4gMqAbH0JBILItttagYgoQWZkeLHHuRQD1bEgdFELTHDYFnP8zNNY2mUVTHDQKsYba7-NftIV_Hmmzc6-IJB1bOEFTcqv8dGcUEA5Jdv04C8PREsqGPKf3AgkEAp0LEELRMtzassN9QcihsGDrJt0fgYrhIQPii24KhagJr78XiK74f-3wNrZIj3Eaap-DMrzwliBUnbYH2m5NsHlLajI1lpkj5oZ31XtConS4jVTVrmAXhgygRyY6uM8B05c9eiXBcAyLcJxG6jEARPCsBvSEqkapwh_r0jO3Z6T5gtFGSlrmaTwFLPj8Um1eqXdP6uAg87QzqQ1vSmQuURc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b65eeb3c1.mp4?token=TTn47-Nz5APsPWDEwdZJGglhXhwCe1VGJI40m2bArrV5w2Xn4yiRWlSlmORYSHuhyVF0hEOVN7HkT4MKhZfG7ySvqyuurChlyguf6BrGKWu-qsDH12MmoHtenVUok57nEO0OqpDWrZcstwQvq59yV9b5pCVrt4ZQi8xNW5RGdWV24PvzaDQpIOP6ysvz1D0HItEuCWx29jRcJZx8pGBqLN57R0ntw3dRzNZM7flHrIOS6LKclQWSWx3rdSN7sPEuqw-mnaajgYtPljRUdEwstjUym9Z9ZOFz4kZBzvYcDrb08jd48NeJEQS8K4IaqH43RA6TXaeoU1AAATh00sHpFyG70o4gMqAbH0JBILItttagYgoQWZkeLHHuRQD1bEgdFELTHDYFnP8zNNY2mUVTHDQKsYba7-NftIV_Hmmzc6-IJB1bOEFTcqv8dGcUEA5Jdv04C8PREsqGPKf3AgkEAp0LEELRMtzassN9QcihsGDrJt0fgYrhIQPii24KhagJr78XiK74f-3wNrZIj3Eaap-DMrzwliBUnbYH2m5NsHlLajI1lpkj5oZ31XtConS4jVTVrmAXhgygRyY6uM8B05c9eiXBcAyLcJxG6jEARPCsBvSEqkapwh_r0jO3Z6T5gtFGSlrmaTwFLPj8Um1eqXdP6uAg87QzqQ1vSmQuURc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌خوانی سرود نوستالژی توسط بوشهری‌ها
@Farsna</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/436039" target="_blank">📅 01:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436038">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfGNUYt-3IKoXMl7l4ukTpNlj7P6CoghjsWi9irJPvqd1-b7LYCRY_gzOrBbsErmcVWwpQaacqpuU2C_jSGaz4gFY0CFEiUVQRH4gUoaaFm1_YX9NPHnbHttNYTBPxUxT8m9dsfZeGl58AleqWnmDBGIpB_7Sg6o9Xbm9ejS2YN1pcf_aVhdBlHmOP12K0Id8LrBBUTtg2rRJGYLnoc2bNYEJaKJsi7j3WlTG_sb9os_PX9m10wRQ48nhTwNqNQBZ-1aUGq48P5Mk3HjS_ZPcBp5D7xB-lDZU1sndhGGZcBc9cyIrBEX8Suu22SQTwBGP2V5pR3GrWVRk_oOzh8lXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرسپولیس مشکلی برای آسیایی شدن ندارد
🔹
باوجود اینکه هنوز نمایندگان ایران برای معرفی به آسیا به‌صورت رسمی اعلام نشده‌اند اما گمانه‌زنی‌هایی در این زمینه وجود دارد.
🔹
گفته می‌شود شاید برخی از باشگاه‌ها با مشکلاتی برای کسب مجوز حرفه‌ای روبرو باشند، که از جملۀ این مشکلات، می‌توان به پرونده‌های باز مالی اشاره کرد.
🔹
حالا یکی از مسئولان ارشد پرسپولیس ادعا کرده که این باشگاه مشکلی برای کسب مجوز حرفه‌ای آسیا ندارد و درصورتی‌که شرایط رقم بخورد، این تیم می‌تواند مجوز حضور در آسیا را به دست بیاورد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/436038" target="_blank">📅 01:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436036">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2mu94z5vDXFjn49qvez8lzce-enl3rftq1ls6fqwSOlEFEhYsUx2v4Xsm6iJOJ_0k4b5gAg2gqYUOus_8cfGm-JPbyDuv_pWVNskZmRXjAkrQSdcPiE-60NwFAWGFKNl4vI7NjYqKnFHbNacEAU1CinxL3GFNCsC3BDEeX6lr_OkkVZLphnNLKqooUrBUOl1u1SiLsZ15e7Z0mxF0rS-ZTz0Ks0NaUQu0XOgtL8-KjzRk2eE0aoWRvN-IdBzhDSpwVo4tcfDE84AmhozXNXVq-o-5_ar1hoIEv5YSGnwPRlvZVFKMP6rh36FfQdOdFpOTsS_ekKixtuxJn2PUhLSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو جنجالی آمریکا سرانجام به خانه بازگشت
🔹
ناو هواپیمابر «یو.اس‌.اس جرالد آر. فورد» که آمریکایی‌ها از آن به عنوان «بزرگ‌ترین و پیشرفته‌ترین ناو جنگی جهان» یاد می‌کنند پس از ۳۲۶ روز حضور در مأموریت‌های جنگی روز شنبه به بندر نورفولک در ویرجینیا بازگشت.
🔹
این ناو که از زمان جنگ ویتنام تاکنون رکورد طولانی‌ترین استقرار عملیاتی یک ناو هواپیمابر آمریکایی را به نام خود ثبت کرده، در طول این مأموریت طاقت‌فرسا در جنگ علیه ایران و ونزوئلا مشارکت داشت.
🔹
جرالد فورد در این دوره با مشکلات متعددی از جمله آتش‌سوزی گسترده، خرابی‌های مکرر سیستم فاضلاب و اعتراض خدمه به دوری طولانی از خانواده مواجه شد.
🔹
گزارش‌ها حاکی است ناو فورد سال‌ها با تأخیر در تحویل و میلیاردها دلار بودجه مازاد روبرو بوده است.
🔹
یکی از بزرگترین رسوایی‌های تکنولوژیک این ناو، خرابی مداوم «آسانسورهای پیشرفته مهمات تسلیحاتی» (AWE) بود.
🔹
این آسانسورهای مغناطیسی که وظیفه انتقال بمب‌ها از انبار به روی عرشه را دارند، تا سال‌ها پس از تحویل ناو کار نمی‌کردند و باعث شدند منتقدان، این ابرسازه را یک «آهن‌پاره بی‌مصرف ۱۳ میلیارد دلاری» بنامند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/436036" target="_blank">📅 01:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436035">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daaaf5bf0a.mp4?token=CldW5Jg0n_ifFniW3_0BbOi3d-NMhOeMPWUyKDMREuW8nm1uyziGQAJdmcMB3LdZMiAvXIAzx23vPzdzbwfjczvTInh5G3lkL8eefhgzFAcqe5R_eaVocNvlO7abjgOQsrWbC39_NgywDIYt7NsCsgjt_uilUjLrD2oozWJ6I4vP1x10huuWvS1dT6162BmEToiYIaZJDTl2gq0dXHcrzG7MhFlvvsQan80L5M_TKhq2WUUeyrF9sdyFtB56in8bXpg4egsJpeuKVEkthZ81xfgefZYDFJnJiibw6ueTUjJbrCE9k7KPJ8cVyYDADDrCbAT0M_zc9O7GceaO-SZ8Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daaaf5bf0a.mp4?token=CldW5Jg0n_ifFniW3_0BbOi3d-NMhOeMPWUyKDMREuW8nm1uyziGQAJdmcMB3LdZMiAvXIAzx23vPzdzbwfjczvTInh5G3lkL8eefhgzFAcqe5R_eaVocNvlO7abjgOQsrWbC39_NgywDIYt7NsCsgjt_uilUjLrD2oozWJ6I4vP1x10huuWvS1dT6162BmEToiYIaZJDTl2gq0dXHcrzG7MhFlvvsQan80L5M_TKhq2WUUeyrF9sdyFtB56in8bXpg4egsJpeuKVEkthZ81xfgefZYDFJnJiibw6ueTUjJbrCE9k7KPJ8cVyYDADDrCbAT0M_zc9O7GceaO-SZ8Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شور عاشورایی تهرانی‌ها در میدان انقلاب، در شب شهادت جوادالائمه علیه‌السلام
@Farsna</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/436035" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436030">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DIgK3yzuV2BeBWcOZDEuoe0jOYkQzPct9wH_YIRp6x1t5phylkGgRyGEwIrlSDpH2yLQS0nfNxQD43w1IRfzI6sXx7c4vXAJJ_qrBNcNHfTNB-S5MH7FHmtRmP5VwM3_sojv6NoI261bacizzle2VKOXtFaHPoRihtW64K7ZK5jZR0ncbBIN5Nz38vYt3OnQ4mZY-a9kODlCK97sqj7unQTKHTFEPkveT7CsQ7vX6NKzpZSe7r_BIwq04wdmQj9HlvFh6KUGjX8snMEz5ei2hwPqoXZegcMzHTZCtlFZkTQZGjKhhsrRpfIxwiM5Z0M7PAHRGlVuhF9ge40A4sZrsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B4JyAJIys9fwRyLJ-mpznkan2aiNtM9VWNsmkOjGVhOrdqs4LYB5ZqeC3TO6pkuNev3-lxMhfyKs6RB7-sKidgaBn2Al_F5QVtwZJCrfoon8pShNiWFitwaPP0Tlbkttw-rtyX_D97TNFNza9YQlP3OaEAPVP9eiTlUUvCmQMGSEgjDlnhEjkbNBREenC-ONG8-1ndOGzvgeMP8I0A2RSPO505wag401xMJo-Qxib5lIWeSgEPMMHwYT0VndQ7CsCiBBUEqggC5xwmNa2ISwnCy4o2j5qruczhJBPBp1KOUYHje7GiCkn2jc0KalqnabJbSvj9H12xqA4Z-HyMCjvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhZyvp5_9_GaVd-HPbi6LxmoJ-3BmCd-BQIhK17nR4a8JGkx3-QE05iYTaLTLy2Wisq8RZjQGAtFs1NMj4CPJQryf4hzmecAePNOxjkI8sJPIA5bD-MywHI02eVYb22iUA-OapLq9d13tEyEDCWLbW1gpPg9B5t24csfKyzDUId1GaYWe6599tKz-TXm5wV7ywLUV4Y2WQNILZRqWSPxnZUATLS3UqqkC-oeoO_MlNhtc-RIG3X0qkrNz2Km13nsjogVyFHrYedmWZzlQYfJcL4V_kjKLzRZDAVUlJAzXA8h1VhZ_q9Wq6ptyTkZkjIDLBMR8kCFol74AW6PSwCoRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiOC2lUzPqJsC83xAvdtsbfTdjlYS9EMtfoOA_zKtxbuZ9-W8Ns50Mz6Ypn43R8c3PNk8Vg7ozlBGWNfyDhpO1XF1rJxuuYuGo-kH81XhqI2Z3n1qDty6GdM2xKjffM3N0aYD3cYS51aHEh5G1eDmfOrmrWPVFuxeRTuLsxOXdnf2znD00-zmA41lF0H1sLZ0tqfvt7qb99zZ3TtT1Q9Ju9t8GCB0TdwgBbHqF7HT7EdPGVwzsbr4B6Y6w436LXoO6hRyVJjAjzUJRrOE_aSSt1Ef4RZbz9trGnq6C_We-ZcBN9Rr645WGjZ-W2gTOJPyXFTfrWatp_EgbD69AcNTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bKKduC4IoVAbrPfMsbAyy0ASOfSLI-LAKJEblZUNzWM3pqKnMtVomO1CZ9ds_yUkJHCILmYEbLwl4e6ljKtkjJkEiBj5oPdCs6TUAhiklTauMV_oaNnIRa9A-b1EmlMXopWBI9YIt0pFD0aprfJaB3KsDDQe9bzMj7MePdGuETSNc5itX2J1JOUG3mB9pXuHGnn8SK-TDXb4yScD5iXUaEt3s8cPbQePumVJCu0inmdpkMoOirTYv4j_j12go9FgYyYtdnUFTte-1fxz-hYicaFPkPqbiL8Cl6grahw-UyROlzNw7j83on8cwGDoTLbmociqjWp0HUxYKlrrFElrhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یک‌شنبه ۲۷ اردیبهشت ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/436030" target="_blank">📅 00:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436020">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uN9dG5feGevYBznWq2KvQeVcl2qW6k-CXs54xrpkEriRnC9qEXpM2ojFM3sxB4TOUuxPbidgyBVZcKxizgSKxm3XDr3k5k67ySUeP1nbpO55_IzUqx344Ppj4JI_5NlnkSiOzKdMa5ukON3vKHyCV9d3Y0P2tGioDoCJJNdjAOUu0bzGkm5-wTlwu63BqXuZjHk_bJ_I9iYFMFqkrISTT4h2Wk4oQ1JJzUxklb4Rx7h1Ykb6C35MFWCVcD11RtuUaBZwGE7lz2ED5oiAEORdfs08KSuhNV-CvLSJRMIY-AwQshqZnrBiJ_qWwXTSVXwMNG8Jmf10N8XbNQrN97C5rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZYmeiJmTYEA4q-_UGMiO8Elda4raezFtOJA91xVFIOFtiQq2dr_96zogLChpf4jlNJN_wafKBCwQa4N47DPGCMDsq8n2os4wgiX875i90rbbDFRvl84v91n__pZFmlG6KGTwBXKITuFMi2N4iQIGyI_HKPvXggl6Pjh1qfu0CpSrar5vLKEKWS9lZU8Txyc04GMq7RBJaA8kAfOaTXUzWPOaMMLB715MQKHEH4Iq2dynDFxAN0xfHvtLE6GeY8eFQaGuRfKSwbXvrrp84gepntdMCLHnDGBzPF_fG3rDpSgTDoz-43INcf-QcvYj_grwaRkzhDBk68uX9DgG2vHpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y9TFK84mrR3nMgg1uTJsMHnpDEmH0q4KKBSseq8HW6DVhfptlYoZkwV4ax2Vrq_gIvypaf9jWep-_4sp5VygGuhrZadHfRbXCqDGSNNhYx7brg7Q9NaaGwch9Xm8ajQ437LcULvP8SaQXwkJq8cVenhSWk4csYHlRg-89gNnJYENQkzy_2c4j4kjqvYrpki-LblQE5cNwh_0m_trvlnVOUPZZWBAqvtx7eRPnusJUNwQG1OuUxzpGdVt7Cs4KRMDbVftWUe0q0ly_9SNzOwgixtR-sN_VNw_Of2bre0RXSYCM2Vvg2ch8nmWPVUYHDWxl5quh-QOeFJIuhUYr6zuZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OfSpSLPCtprlhAv6gFkjwD6XlJ8lRhWWxFOII6J9LLFqX4toYjb4431uzVjKtnhQykQCo55Z9k_tBW-pRNqXgb79y-UiDMXvDIOWqs5v68hzPimQRf_gsD-lUBSAvzt5cEjLUiPyqK3vh-P4w43nHISYCwUilWv1hoVfKEw48xiRVjs7a5BPd875tz-d7i0yJJ5gpr96kdS0WyWldkI9F6RK_3YPbR4viPlsb6-tQRoqUHAonJ_Z3su0Ba3gU_sErKH3wx5FeD9NPX88U4SWyFapqeCsPLOssb5P0KhnRDvcGAYIxwgny0K1GCuSIJdwDabOOzXdP_vvvUW0G-p4mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UOgTzrWaocC8DUnK1G8OT0u0pLLJ9BDfmZwmnZfxvJOvEaAc84lTFJXPil3gDUgT6j3dGxpV4kfby-rK__R8Rkc_gfxBdEJjEoRA9QdqfbIH8zhrSnxwrlJsOANi0LSiqukKpvv8TeHhXxHG80nbKtVGcchBqEU7QrBe8d2h8CnGlAMBMI8dYqaUsPM9eu6oRol_W0JUlBNE_1lCGq2oDXvszRJ-m8qyIJWduLDdNpM-OdKTuQnxlywqFP65TLFRsYrxy6m783wSS4x2CMMG_c_Ciavdcio2R18leIg1sgDF0aKQjm7Kgt7xiDKuLbfFc_AAGDy89lszpc3vEbZ2yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bdffc4vkQalLOcD486iZLSnKf7kZ_XxHavjzwZGPAmnpkTB8vol0QelQuHYxW7MzeYsuXj1Qknc8EJuRpSfobMxO_TqezAn6BjXVy62_2a8mUI1LsWnD8NIyymlYKyizepPbiWeUxCetG-3wuj1-qYEFidba6oFSDoiPiLB64VLd-fXReeHvdNd71Tgwhqf46eS5yKzkTXN2Ck2S2o5jyVQXh3kjrdbWPbXI_FSrhXrcqoeaBauU_cu2RM30tjnam1ij6Dn8fBbSYlVA9g9N4ACXjRD0Ogj8rC5NBZRS6LvZs0hHNabVGy2d44iZqKLRCelrHtecR9sUBq3CH8rMPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3sfW39HmcZbAXFyTD4IdPomHjRuucXcaXCGZgpZTVAUrfCo0lJSSDueZh1qvyZFWadzvr92orhAjJPvv7AnD7vRubZSN8XtveuLOPUp0zf9IXJ9l61zie4sDKV4mWW8DW5VVeqsLHUbXUPOy6LwNxDbpunURBcT8zCeoZB0-97ieYAGnFH4sVLW3SRxUzgS5aad0p5rncg5n0oGy5i-GPFNHAEzOckgks6J444s4nWPxbfeLOcHkDW3VMKqPw6sg8FwBLZhj_7ZUYIplPLHSqJDF4Syt8ArT07gVI5DgwPqvFYh4sWWSX_Oj_w5V4iPqQe3tWUr5H-HQBPPC8JoVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EAdat1ofGlrw9OrQMkAeFGXMex6qEAMfvf0vNC0OEUoVxFWDOeWhAwSGDgFR_kpGDzyZ7cC33v3N3kwjYa-1u2_TDBT-OTrM-sHon2GkJKV84cl-M_A2KyHyrlYgLCqMgJyaua9QoYqvFF5ByfBAreDNTyjwjPi4Kr7lZ1cDu-YF5uMA5M4wCJiFkfZva2MsVn_eLNP3iV0TzR6dEhz3Vcj-gzG5EHV1Lqt7xOR9SPctSWJ-Wu1mYmaFZIkEzpZCxQ7k018lt6PKjk8Ff2EYj6k5yxCvILGZeBH7QCo4lDhMIRSwhmHxXn3__HXL4VS_U_UaWXTUl7qXwZkHsreLXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6UH0Oe0t1OrwurdPB823svpIMrf0UFE_-ABsI7eCyzXUukVkmoOQLfOm2rKph5TGrlz0FDSehjzs5L7affimYrJfyVpi-kplcCLD05JAQK-r01Z6CLsQDQwZ20ABtwrINmMr50PmsIJeD5B1GB-slapZPqCqZMU9OiNXomsCRYQgvX3EdEGxDmvNRu4m2RcTLRLb6qVJ1rd6rg5gBY2Qj6azzkiYkfCzMTCS7cM7gIlppF6qZRleBqvmnptXmx1F2UCyAdp1jR-cQXg0-4XSp8vMY_xNhu-x_3abRkX1LCPc9jJNvCeLEDt9YKr6U5f544O03Fp75i0_Nf6pHBqUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ULqfX2e3NpixDRlVSAM1GmpyfXg-ncuZSpnMfgYV-CccyoIWiBRLzHjZNvY7YGP8py1DGPiZN6AmP1vjEB5uytA23jfR9bXH0O0TXutbHQxDQsHRs2kYeKEF-FjFnKkoY0f7_jSASZ_swfCVqzQsxe20t8DSu53aUMkTq2fFmTh3jQBJBYaPiQVkHlo3IXWNU-uhERUa0RYCmWN9fpS_5PUoGJqICw-l5fl4zQ27B1G7EnFsmVIeZSbw2FCzzb5xYGAS2kBFmaMqjThs1vHqUgIDLK67qXPrx2BXiaBy0ldhKpwUNNKkZzg704_ZT8FMkXdMtB8MNDAwAv6lZdDGgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/436020" target="_blank">📅 00:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436019">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_6I2ZZgVX_EUZzKN3bmXdYhYpOjo7HingeU5nUeErkTPTvnacRCd3dGTiBhnI-HQjlpRojvqR4AEfXWA5JLNcj4vKnWlC-QLjZwte4eUNodVSUYgfj7E1td8G-tpw2qqJByYoFA8kgAlwPo--ptfIob7c_D_OVngyGd0syP1J8qUZak29zTdyJW3u6KhufiPsD8kSPEMXSTmiP1fXGuXwjl-Ey7DUKMiWU4Wxc8jr8ccYMi7SVEX8Wn28Ah9b1QKPn_nTNDBJjS2NpdsI2AFHZVjlNiVexi6G_kQqqkLHM3Cv8NcfxlGHAecBKOXSOYbZOW9XIoPN8rbmlwXlOtWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ اتفاقات مشکوک در انفجار بیت‌شمش در فلسطین اشغالی
🔹
شبکۀ صهیونیستی کان مدعی شده که آتش‌سوزی مهیب در بیت‌شمش واقع در غرب بیت‌المقدس در نتیجۀ انفجار کنترل‌شده صورت گرفته است.
🔹
با این حال، کاربران فضای‌مجازی گفته‌اند که این انفجار بدون هیچ هشدار قبلی به ساکنان…</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/436019" target="_blank">📅 00:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436018">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🎥
در نتیجهٔ انفجار سهمگین در بیت‌شمش آتش همچنان شعله می‌کشد  @Farsna</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/436018" target="_blank">📅 00:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436017">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‌ ثبت‌نام وام یک‌ میلیاردی کسبۀ بازار جنت آغاز شد
🔹
مدیرعامل شرکت ساماندهی مشاغل شهر تهران: از هفتۀ آینده با کمک بنیاد مستضعفان، وام یک‌میلیاردی با بهرۀ کم و اقساط ۵ساله به کسبۀ پاساژ جنت پرداخت خواهد شد.
🔹
بازار جدید به‌صورت موقت و با نظر ۲۵۴ کسبه در نزدیکی…</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/436017" target="_blank">📅 00:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436016">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1da2602f98.mp4?token=X9Q6E_GdboJbOsXVdOraCSrF5pHUVV_g27jDBK8gHHUm9UvjpXgdfSdMVwYvAjSNclLGDNxLtEx6cjEHSc417_LmveTbF0PIPTakGZ9XKyb4Tm0QJ22AZG0ZXRDXsJrcZoeuSyaWPwGeEI9sxtG8gIT3C_Oksz9hfgjIQqVCERC2SGbHMqt88SzFumUeqpv-HPcdKTezEMB7H6vaEP88rduUm6SqieZZ8knFGMlvHvWb0353q0XLUyiYU5y8VDGhPbqyq625Ylg7QTl0Lxwz5qLbTN0LjN15UKY6I4HZqlryhEB_qL28Y2iLQ0-519zPv11JK9ha5zbXBKTkrVcDcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1da2602f98.mp4?token=X9Q6E_GdboJbOsXVdOraCSrF5pHUVV_g27jDBK8gHHUm9UvjpXgdfSdMVwYvAjSNclLGDNxLtEx6cjEHSc417_LmveTbF0PIPTakGZ9XKyb4Tm0QJ22AZG0ZXRDXsJrcZoeuSyaWPwGeEI9sxtG8gIT3C_Oksz9hfgjIQqVCERC2SGbHMqt88SzFumUeqpv-HPcdKTezEMB7H6vaEP88rduUm6SqieZZ8knFGMlvHvWb0353q0XLUyiYU5y8VDGhPbqyq625Ylg7QTl0Lxwz5qLbTN0LjN15UKY6I4HZqlryhEB_qL28Y2iLQ0-519zPv11JK9ha5zbXBKTkrVcDcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برخی منابع عبری از وقوع انفجار در منطقهٔ بیت‌شمش در اراضی اشغالی خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/436016" target="_blank">📅 00:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436015">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3Axz81fA_VJRg0yYp3kQRecYOWSG5lsRoPamKu0Q20q-vI1c9teOFgwlfjXutboguR0uzeWslS85elE-7aYGNlZZIZpFq3KSQXKmv5tfoU1S2hF-yg755PGHF3Kh8EO_Rcp7K2hj6Hphsh3Ms6xRWBdA1BiC6chw37JvWddLLo_OW-BJgXTEgu92as9Zf_-awuYlxHcKMywTXcOPWokU8cYJDA8Co8ofutE3jpIjGdupksTRvwubRLNONnTtETTHaeQNYa4VEazMAZ5KnGKaMOtksaEXsMCJ3wnrPE4LtOolJSdxaT3BdByyL1Gpw9N5rVeL4Rde3dSlmXAvwF8CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابلیس و فرعون
🔹
روزی ابلیس نزد فرعون آمد؛ درحالی‌که فرعون در کاخ خود نشسته بود و خوشه‌ای انگور در دست داشت. ابلیس به او گفت: «آیا کسی هست که بتواند این خوشه انگور را به مروارید تبدیل کند؟»
🔹
فرعون که ادعای خدایی داشت، در جواب درماند.
🔹
ابلیس بر آن خوشه انگور دمید و در یک لحظه تمام دانه‌های انگور به مرواریدهای درخشان تبدیل گشتند.
🔹
فرعون مبهوت شد و گفت: «عجب استادی هستی!»
🔹
ابلیس گفت: «با وجود این استادی و هنری که دیدی، مرا به بندگی قبول نکردند. حال در شگفتم از تو که با این همه کودنی و نادانی، چگونه جرئت کرده‌ای که ادعای «خدا بودن» کنی!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/436015" target="_blank">📅 00:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436014">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-text">هواشناسی ایران اسیر چشم کور رادارها و مدیریت غلط
🔹
سازمان هواشناسی ایران به‌عنوان متولی اصلی پایش و پیش‌بینی وضعیت جو، نقشی حیاتی در مدیریت بحران‌های طبیعی مانند سیل و طوفان‌های ویرانگر ایفا می‌کند.
🔹
با این حال، شواهد میدانی و اظهارات متخصصان نشان می‌دهد که این سازمان در ارائه پیش‌بینی‌های دقیق، به‌ویژه در بازه‌های کوتاه‌مدت و برای نقاط حساسی مانند کلانشهر تهران، با چالش‌های ساختاری و فنی عمیقی دست‌به‌گریبان است.
🔹
وضعیت نامناسب شبکه رادارهای هواشناسی، ضعف در شبکه مشاهدات جو بالا (رادیوسوند)، خلا یک مدل عددی بومی و منطقه‌ای در کنار مدیریت ضعیف از جمله نارسایی‌های گریبانگیر هواشناسی کشور است.
🔹
به‌روزرسانی و تجهیز زیرساخت‌های دیده‌بانی، سرمایه‌گذاری بر توسعه مدل‌های بومی و خروج از انفعال در برابر خطاها، ضرورتی است که تأخیر در آن می‌تواند تاوان‌های جبران‌ناپذیری به همراه داشته باشد.
https://farsnews.ir/Economy/1778961014305887280</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/436014" target="_blank">📅 23:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436013">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c50608fb5.mp4?token=klZGwmUsDvbJ0Q0HKHl0brEVksigUuFuqmIHEeR2dsGWZ7ovQ081FrVtW9fS435U2xZeFOjx3m3CjYK9J9MudBaVaD6kovHQM7SwXI1xnZ2DpAj0WcTkgQDl8W1ksvmQO9bjpKuow3-fvs46gFfYqaz6UxHUnozbUDJOSXFZArxAyGvN-XobD9SRXO7vkOZUrCjcMStrhodt4xCJqDI2xKS7cpxbnS27sL0uD061_Q66TtosQqfjmhqS_sXsCcI00awkmX-2o7SIJrvqzhTVtWDCAeQKGgqA9045jJLHUd0gLndhY4rjgHBcTuWPhRiJPeuxp1PsGL3NGqNs21ZP0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c50608fb5.mp4?token=klZGwmUsDvbJ0Q0HKHl0brEVksigUuFuqmIHEeR2dsGWZ7ovQ081FrVtW9fS435U2xZeFOjx3m3CjYK9J9MudBaVaD6kovHQM7SwXI1xnZ2DpAj0WcTkgQDl8W1ksvmQO9bjpKuow3-fvs46gFfYqaz6UxHUnozbUDJOSXFZArxAyGvN-XobD9SRXO7vkOZUrCjcMStrhodt4xCJqDI2xKS7cpxbnS27sL0uD061_Q66TtosQqfjmhqS_sXsCcI00awkmX-2o7SIJrvqzhTVtWDCAeQKGgqA9045jJLHUd0gLndhY4rjgHBcTuWPhRiJPeuxp1PsGL3NGqNs21ZP0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقامت شبانهٔ مردم مازندران به ایستگاه ۷۷ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farsna/436013" target="_blank">📅 23:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436008">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gClF8lpc8VZp2M0ddoNfhsbjgGdXftPfD9QrLgetxomtacpAN-JJ8Nl9xAsQsJP7O8xkXrwvIvpEaM076aTdHyZr8K21r1-filS4JV6amhxT9Mq6LvY6gNgHiKjurngxE_J0XCFAGkDqXkHJAHw6-3PjY3ik1iBw4-YiSmbeEtJAz80WcYgFao4ETB7hV1jT6MseqmPNFSLSanTo_u8NMnwKWUhN3NWPATJfkt6CnlMEWDlGBYU9hpWHGSjFP-4lVqHdgNOBSExrFAOkKUsaqfvT90RXdQtv5iLqIKvmqog4c1zRnxTfxMFekenEhBrEmUvdmRKYfXWps11JOQOd1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QTNkm9uxXwlJnqBQ-hUeGti8wXs3Dua-qAb3WhdWU_hJUYFuwmPm3ltvpMXHOHtAMI1SxzKenpyyR-WLiRgFKae3GcNYWJVIW2Gew5ivrUGMe_TH5KqE3TdXGvku-cSdywNjQ91he4x4hoYnUge3VSPhfE7rw5cijlGyi8vWizQMEn6wo0YndEBJaOELQVk1kjxZUK4eOolFg-ymww4naDDorpX3UtlsvRAl5oQzu9dxXJMgqDNCt6w4pt7AsquKiXrw0rKvkkK2sQYPl15MN_cFO7e6QxKVoG3DaFASfJhQPqEquzmA0KNAy-6OE7xU9o2jMMskcjYUixoc71ancw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/saClPrqEVBPlL-MY1YXnktVcfMzug1Wnd2oyVvgqyAXfGMVd8bc5hmW0mhjGIM0Au2XvsngQdaGARdrrCzqJMEp3kywrYlRkM6BIcitxzJw-8tJRTO5AOw2X6WlB6lUXWzY-dJYeyL6Gubd-z9ksjPPJhU8cqpsFil28Rz9-QPnNNPCNEGlgcQgVGjaVAEMpLrMb5oLeu9EcmI_P5diMorCJzvpi_2jBDMgPkuefCUPd1eJYXqEiBWeZ47JJc_9C6YBjfGgrw2KiT4mmjsPAMVBNDqN6a-fEi-ozYmzJMNoQyX8L0kUHxz1fGNSerPaxSOEoJI_vtVAAEwC6_1rqkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gx75Oym-QFz0U9J51NmLpi2J58sgjcGHuePbPWw3jt8ohDR2BzHEF_qRfN4brTakfIsS8v36PlufX8EcfsCDEkcLUZ1k2Qov3MZ8Q7glBo2RZQCSspX1x6ZGCzMqsOFwCXvSxqwNGNEcqe-3GHTdS0a_7UPVQTlp_jkRlXYIM0CYLn7Fj1s8PwbYEWKitadj_SXQY24GnV0oAcp7wI3OcUuRNmOpF1R4INw6R6MMvev-0r8a3Y3VvA2I5fqD77WAxLp4wIH3oIjSYqI6xpCk9wEwrNp6RbpUreC6hw-rr2XOHZN5FAMUYejCaxrtGGV570JJVCdtcqvekbAG6D9cCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pgTw24YvLTkYD_ORvbd972L0vypVrlFIGim_0wERjAXKK0k3A2atnQOef5qtAKbFOvtPUxisDejW1rB9_vrso3ltD4ws2tz7QADDsUGc7eWOraL3nmvR0ZyAyYBG3Imv8CIXA1yaE-YXudUs-c2KwlobfbDen-m72YxoQhf2_18Xf2ZSVcFTMdKTY0LDNn1PFvMoFTJOLdMtEl43ZSI_SZZzy7_MmrJaxFycV2X1Bd6zCXZo8umHNDcwRznbIDxHaEYjxM_HwUgESuFJuOqV179x0ebgnv8Vmgc_-tI9FhT0AQMgHnQZY9E9Rtopvl6spuknYfisn_FqSjPlCB3uRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حرم رضوی در عزای جوادالائمه(ع)
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/436008" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436007">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bfbd4a57.mp4?token=naBliDxYyjGUT2-c1g2A3pv-zYDf6nJnfgBPtRM7AIroYzNZFFei7QZl4-6CYU7vz46xhB0zmFgvPjlQeHKOGhJEWwZB9Y6jMdMPyhGKUqt91A_6c252-VFtoSJcoaqTkaGJ7RKKYSeYBY2mGZbjlZbRYD-GCs5pPmvBUv-TSOg-VMCmgZU9Fumc-k10fBdJpmOEg7AuthALkZtGDDHScnaDSaZJF3gmPpoA-lMDcWc44vzjMc_FpLVErZyyZOi0CksoS8Kqpuo2fosAhepE77PafPxqpedy4t87sE5gihv1P10gdPfo_RmjVcthOFCVebnHhJBUOVt-J-KTjOYfrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bfbd4a57.mp4?token=naBliDxYyjGUT2-c1g2A3pv-zYDf6nJnfgBPtRM7AIroYzNZFFei7QZl4-6CYU7vz46xhB0zmFgvPjlQeHKOGhJEWwZB9Y6jMdMPyhGKUqt91A_6c252-VFtoSJcoaqTkaGJ7RKKYSeYBY2mGZbjlZbRYD-GCs5pPmvBUv-TSOg-VMCmgZU9Fumc-k10fBdJpmOEg7AuthALkZtGDDHScnaDSaZJF3gmPpoA-lMDcWc44vzjMc_FpLVErZyyZOi0CksoS8Kqpuo2fosAhepE77PafPxqpedy4t87sE5gihv1P10gdPfo_RmjVcthOFCVebnHhJBUOVt-J-KTjOYfrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برخی منابع عبری از وقوع انفجار در منطقهٔ بیت‌شمش در اراضی اشغالی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/436007" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436006">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cfa3b05b8.mp4?token=O_GBkafjSZnSXz1h9t-tvOMcbk9ioCWEMHUl_D5wFYBKUGswbvKt6GlgzhzZAwfCGtP_fP74GTCPJKWqmhojUAjmOZJ1KVFdqeCDl3r7M16YL0McotzVUWK_X4IdpiDo_-fMsADu-myqAIbc7cd2wrpBCqMphHF-o3M5PTS2DwbromUVKdkJxJI8bPMWASep0xLjTHwCA-MvMSNS_oNZ4uOEjxjYGwROUI49CWDcgIw6LUAdFZKfn40_62RdD6RZnqWmBiuHSB9n0nPDr0eKYtYnbPpN_MerTc7-dLFEMPPc5NQadkdIyyZgFlMv3qBxD6lny8rUYcsMoW42zaKlW4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cfa3b05b8.mp4?token=O_GBkafjSZnSXz1h9t-tvOMcbk9ioCWEMHUl_D5wFYBKUGswbvKt6GlgzhzZAwfCGtP_fP74GTCPJKWqmhojUAjmOZJ1KVFdqeCDl3r7M16YL0McotzVUWK_X4IdpiDo_-fMsADu-myqAIbc7cd2wrpBCqMphHF-o3M5PTS2DwbromUVKdkJxJI8bPMWASep0xLjTHwCA-MvMSNS_oNZ4uOEjxjYGwROUI49CWDcgIw6LUAdFZKfn40_62RdD6RZnqWmBiuHSB9n0nPDr0eKYtYnbPpN_MerTc7-dLFEMPPc5NQadkdIyyZgFlMv3qBxD6lny8rUYcsMoW42zaKlW4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع پرجمعیت مردم علی‌آباد گلستان هم‌زمان با شب شهادت جوادالائمه(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/436006" target="_blank">📅 23:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436004">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🎥
سقوط درخت در نوشهر پس از تندباد شدید و رعد و برق مهیب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/436004" target="_blank">📅 23:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436003">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
بلومبرگ: آمریکا معافیت فروش نفت روسیه را متوقف کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/436003" target="_blank">📅 23:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436002">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tt_LFv4j2GisQa-aa0vr5o-Ltirp9pjAgr4CSVS0LOIp7odY40jhmjgtcv4jjh6ydekbKcbEePJpsaHp9L5DSjHj0v1TfMJ8kjpOO5dt1M3DvwCSvr-vC7kGGDiYzSd207WPmxWE-GkVHKGTtRMKC4TdfdvmaS1l27SGalkK5gNwe0XFQwqzGRBLDsWzQVaYwgHpQdjOvXQoYQGUa7QlIjSmKi76lidf38Ttanq5MbgS7KY1u7aqWtFcf5bVY-trCj9ypgRe4QEJUEnaNnErI__nIKX6byC6sWRg-PSuth4-wh4xT3T5vyIp9-CZKBS237j5AEQEvIsvZK1LQon2tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: مقاومت ملت ایران، تحول جهان را سرعت بخشید؛ آینده از آن جنوب جهانی است
🔹
جهان در آستانهٔ نظمی نوین قرار دارد. چنان‌که رئیس‌جمهور چین گفت: «تحولی که در یک قرن دیده نشده، در سراسر جهان با شتاب در حال پیشروی است»، و من تأکید می‌کنم که مقاومت ۷۰ روزهٔ ملت ایران این تحول را شتاب بخشیده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/436002" target="_blank">📅 22:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436001">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎥
بروجردی‌ها امشب برای شهادت امام جواد(ع) سوگواری کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/436001" target="_blank">📅 22:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436000">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gShIsPjckJ0Syi7hUA-97_I7MiSXZSrSJe8AbNMKvv0nNRPJkKfrKNuO9aPoVE_-iQFbymrTVV_jsYK1ISGpKMQCDL1FXYLPvl2Tq2H2UYvgoCW7uoKInoc2ukREQSaogkwNSfK_qeS9GthA3HoK3ZZTHO283jGnpci7PPmEnYhb4HxbpfFGXwmja2gfdet_NcBtsXMmv2O0WEXSunvENhdxB90EJWQN0LiFSTk9JuPJMynn8udhkVhtY-UpmFB-wbUiu2VyfeaybJ2fPUwEj7qoRhGZgArpyKbIlySxbGSyMEP2P6dXRTa9XvK_IeTGYaPk5s-mVT2f9gwAujSFBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوثری: هر تعرضی با پاسخ کوبنده مواجه خواهد شد
🔹
عضو کمیسیون امنیت ملی مجلس: اگر آمریکا یا رژیم صهیونیستی کوچکترین تعرضی انجام دهند، مردم ما، چه زن و چه مرد، در صحنه حاضر هستند.
🔹
دشمن هر توانی داشت در ۴۰ روز گذشته انجام داد، آنها نمی‌توانند به راحتی بمب‌ها و موشک‌های از دست رفته خود را جایگزین کنند، اما ما به راحتی میتوانیم جبران کنیم.
🔹
آنها در هر نقطه‌ای که حضور پیدا کنند، رزمندگان و مردم چنان ضربه‌ای میزنند که جز ذلت و خواری نصیبشان نشود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/436000" target="_blank">📅 22:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435999">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Av4yYB-12x11Z6z2e1IY_nGKhM7IQQBWcYxg79kAq7f2EuHauE2g3qgyuxOEelfvlDCey5mjktBDq-TAivlsrC6lFA2PA9BYtkjWRo2rKkvG42lBVLRpu_E3kx9zTRf2cTegG1FZD9T-ew8vIn69aFZR6i_873YjM7rnA7Va8qevVTPvwSJbhdgprIWSA9Ei1EX8qIN5LgpX6z4_cjvN0V9B-3SXcxpDy46b6TNfQPyGJaSusDAmeZryzk9kKjZ3iC7l92pDbCa6VmGRxsyNj5E-Ohf3z7XW2XIIekCGCXAYr9sGkhwW4PGWWgaO5d8YNukmQFrvlOf9xF7RwzKqTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلاکت یک نظامی صهیونیست با پهپاد انفجاری حزب‌الله
🔹
ارتش رژیم صهیونیستی از هلاکت «یسرائیل ریکانتی»، از عناصر تیپ گولانی در نتیجه اصابت مستقیم پهپاد انفجاری حزب‌الله در جنوب لبنان خبر داد.
🔹
ارتش اسرائیل با وجود سانسور بسیار شدید تلفات و خسارات این رژیم در جنگ، اذعان کرد که شمار نظامیان کُشته شده در جنوب لبنان از زمان جنگ جاری به ۲۰ نفر افزایش یافته است.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/435999" target="_blank">📅 22:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435998">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بورس آمادهٔ بازگشایی شد
🔹
سازمان بورس: آمادگی برای بازگشایی بازار سهام از اواسط هفتهٔ آینده وجود دارد. زمان دقیق بازگشایی بازار به‌زودی اعلام می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/435998" target="_blank">📅 22:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435997">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad00ffcdb.mp4?token=F2ie8ZtprLwBV2HIoq6WxN094Va3nDbNYnocj8hZ5-EiJXVkbrjkYIXiDjRHqZEJgoVsGiJivBgzcVTWoIO--htEqhf-eBZ3V3_hgslvnt2a5pF9p-nWl83v8fNvlEhq5gez0EbIV88gKZv90p4fVFSFXS8EtoytN1S8lCuV_4ldLgDg9Gzy3nGmssj8pDQDQYDN7zmrOpcxwD2OkB9UxrpZcBU6_7dqcll-sSwx7c0nWa30I1Dbz74taV5_mvGgi5I9wc66k3aYqW_Y1YxepY74qJmDVVEucwnB9LvHUEBlaxiCJ-88scj0JMlTiO7rzjTzixjdvaWAqnGbBc0-XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad00ffcdb.mp4?token=F2ie8ZtprLwBV2HIoq6WxN094Va3nDbNYnocj8hZ5-EiJXVkbrjkYIXiDjRHqZEJgoVsGiJivBgzcVTWoIO--htEqhf-eBZ3V3_hgslvnt2a5pF9p-nWl83v8fNvlEhq5gez0EbIV88gKZv90p4fVFSFXS8EtoytN1S8lCuV_4ldLgDg9Gzy3nGmssj8pDQDQYDN7zmrOpcxwD2OkB9UxrpZcBU6_7dqcll-sSwx7c0nWa30I1Dbz74taV5_mvGgi5I9wc66k3aYqW_Y1YxepY74qJmDVVEucwnB9LvHUEBlaxiCJ-88scj0JMlTiO7rzjTzixjdvaWAqnGbBc0-XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد الله اکبر مردم بندرعباس در شب ۷۷ بعثت ملی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/435997" target="_blank">📅 22:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435996">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDzXVK9hGE3Z52Yjib6fqyNtCH9uwL97-TLXGd0DG238nM8XGOu0AtBg5atFm4VaPFqTED5APakrXV6V4XVsvXEempGl3mAW_23Cmxz2kzy9ifRsAwUtFzgV7cyZn4dOTjH7LCqMnM6YmdXesagoAmvkkCwBFwYljkviSArjo5t85Q3IHav7fuJhwVk7Vsd-F3qeV_l_HmSpbaWzC4r58CxjCidf1if7JgAbJ4BpnnyAQHl6nukQlpU_4_AJ2SjG1c7fxj0yBfXQTvPJYabzonsmhNOljmLPXNDlwinDiIAdxG1d-riGyU8Ik1VZmQ4WNi9WDrjwIv98uhVtKFVhYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تارنمای بیمهٔ ایرانی تنگهٔ هرمز راه‌اندازی شد
🔹
تارنمای «هرمز سیف» (Hormuz Safe) ارائه بیمه به محموله‌های دریایی عبوری از تنگهٔ هرمز را شروع کرد.
🔹
مقررات این تارنمای بیمه می‌گوید، بیمه‌نامه‌هایی سریع و با قابلیت تایید رمزنگاری شده برای محموله‌هایی که از خلیج…</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/435996" target="_blank">📅 22:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435995">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiI3rQRj6C_r406i0dastJRhmSi4wxHuqE4S8aoTHxxmjVJdmvaqf4PIRqmW4qpmp7nmlHmArtU9jBjqyBrf9AMJttHDJki9LoYc3-_0XSHnhwbDVz_JyoSp9SCetSIaEEaRqTYHWjpgbO0L8QGNcBXAeljVoXhPgxQOHhqKRQP92uraoCxlr0B1bJjuZtnsq08GQPvXHX0MSKJK6fa1ACyOnCN5xTnZZJEGDc2zzZ9cqSo48bVBZ1un97lhdEQB7teFtIarlXRGd3cokvCw390tqFJMEK4N4pWJvRCQM6YLjtkEZz_duX6XDKEhj5NpQzisvxh6uyJn23FRgJL9kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان جای خالی امارات را برای ایران پر کرد
🔹
پاکستان با کاهش تعرفه‌های بندر گوادر خود و پذیرش اولین کشتی تغییر مسیرداده ایران، تلاش دارد انحصار امارات بر ترانزیت ایران را برای همیشه بشکند.
🔹
این تصمیم درحالی عملی می‌شود که مسیرهای مرسوم واردات و صادرات ایران از طریق امارات با اختلال مواجه شده است.
🔹
پاکستان علاوه‌بر تخفیف ۳۱ تا ۴۰ درصدی در تعرفه‌های بندری خود، یک ماه انبارداری رایگان هم برای کشتی‌ها درنظر گرفته.
🔹
کارشناسان معتقدند که اگر این روند ادامه یابد، وابستگی تاریخی ایران به بندر جبل‌علی امارات که تاکنون سهم اصلی ترانزیت ایران را در دست داشته، برای همیشه پایان می‌یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/435995" target="_blank">📅 21:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435994">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcad0f1d98.mp4?token=F5b63qwDP9o1p3DMFldSs670RLhQSkkrqFTQWOmAK5t05H88WSktyxbClk1dbefP7H54LRs32c8_yLX4KG1UYchiWRtiQ2N7oZBuoE7I7iPtSHrlZVCzjZaJk5KKgAdNOJh9euqron1RvEQnnHfNNazpeMZcr1Eibbzbw6FO4P76wDxGazRWXBTVdMr0Q4xAuHuTwgEm2XSSCHyxGDiVGEF9vk5BLo4gi56u1pPBxpeIWxA_Q__T1HWrnCeC6nn7UMjA8bY0ymywGB_pD8fcphrMbkpa5OY94UJ5XXagn1SeLBBzFw6MYrucaSHYBirAORz9r-YYrX5JO88A8vaf1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcad0f1d98.mp4?token=F5b63qwDP9o1p3DMFldSs670RLhQSkkrqFTQWOmAK5t05H88WSktyxbClk1dbefP7H54LRs32c8_yLX4KG1UYchiWRtiQ2N7oZBuoE7I7iPtSHrlZVCzjZaJk5KKgAdNOJh9euqron1RvEQnnHfNNazpeMZcr1Eibbzbw6FO4P76wDxGazRWXBTVdMr0Q4xAuHuTwgEm2XSSCHyxGDiVGEF9vk5BLo4gi56u1pPBxpeIWxA_Q__T1HWrnCeC6nn7UMjA8bY0ymywGB_pD8fcphrMbkpa5OY94UJ5XXagn1SeLBBzFw6MYrucaSHYBirAORz9r-YYrX5JO88A8vaf1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرائت دعای چهاردهم صحیفه سجادیه در مقتل رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/435994" target="_blank">📅 21:52 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/RphuTCfrxuxxe6lK-0EJ-_tqfcS_xT4QZ6cnUajj8RB4WSj2cLqX2mlmeFTMYkzS2Qisd8bmt1_IeHlbcGrLxjigrfNEvuaYQpdGvP3TNpwK7Gpbit6vnQjQNmMqNOwmblgTt3e7RqnTtgBovIbDkjXjdnSVaZ3G1-ND6_d5_jz-bIwtEOwwgVKjFPsXQLRrM-D5M-S6kLOInxOhWSXRblQEHu8ipkd_xzLRv0p-Vg5wv3cbHD2Ar6yJ60yjKUqLKAmkoF-G8exAyIZdl1UqZr-VEJzq6K9zk3npqgsY-zuXhlFMZ03ud4ywOwXnvUzpbYvrUPe0nWmMgqXpXqCaLw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 13:09:54</div>
<hr>

<div class="tg-post" id="msg-446217">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65c733269.mp4?token=tre5X-QGRtFOJgfDcKoi6aEywWvWKaUG5Rdf7p9bN-6YbNUF2BreM3cxnAjkZIJSVaUXzm3ty4T7zkpAQhpW54atySs7j_vt0ki5mSGM6ZjBfbZje_pP3GqnOVcqVZx0KWQs0Y5gSlhzfILvKWJ6tzxSCh0Fc7k_Ycax3EONtS-NTtD0Jm6i1U8FUh8N7BBLdVYi_D8hSkaiqU___6yjQxKPZ424cssmTO7NtatQhBQt03jVnWkqYUoNmTpPubbsXfjc8a6EErv5jWJNNwc7HntTSEshTOJ80Uknpw8zWeqyyCYHFuJTJsgU1dtHaRwhHUA_YuPmcrNq5iWrdCreHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65c733269.mp4?token=tre5X-QGRtFOJgfDcKoi6aEywWvWKaUG5Rdf7p9bN-6YbNUF2BreM3cxnAjkZIJSVaUXzm3ty4T7zkpAQhpW54atySs7j_vt0ki5mSGM6ZjBfbZje_pP3GqnOVcqVZx0KWQs0Y5gSlhzfILvKWJ6tzxSCh0Fc7k_Ycax3EONtS-NTtD0Jm6i1U8FUh8N7BBLdVYi_D8hSkaiqU___6yjQxKPZ424cssmTO7NtatQhBQt03jVnWkqYUoNmTpPubbsXfjc8a6EErv5jWJNNwc7HntTSEshTOJ80Uknpw8zWeqyyCYHFuJTJsgU1dtHaRwhHUA_YuPmcrNq5iWrdCreHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: قدرت نیروهای مسلح به رخ دنیا کشیده شد
🔹
اگر امروز نیروهای مسلح پرقدرت مقابل قوی‌ترین ارتش های دنیا ایستادند بخاطر تلاش‌های قائد شهید امت بود.
@Farsna</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/farsna/446217" target="_blank">📅 13:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446216">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b54d67a638.mp4?token=YThVKcyKtzxFaCJD0IYOqoc1zhKh15bB-lNxVMDnBm8yAIoKbFqlblBfdEWTH4CtKS6zkY__6C7ZvOSUWzqfzQcAUMeinv9yghnyOzdakqUI-6OMHfwQKiAYLU713cC-fizcWBAiH6LGpRKuHlYAMv7ZHdpdBsBNOg3h191Xo4DDtQZfFJt2WiyUz_uEvv36QHJSS29lppruyoaKzRc4eJ-PBw8aTooYwIHecqkW9cyAxIi0EAZXvANiRWqGm0ATyXCv14rk8MRqM3cMKLnqF4qsMvYkIIm7GHMpmsI172oYOAyE-mv0N0W53GT68isxty2-vvRk77bjvOkHhWMAdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b54d67a638.mp4?token=YThVKcyKtzxFaCJD0IYOqoc1zhKh15bB-lNxVMDnBm8yAIoKbFqlblBfdEWTH4CtKS6zkY__6C7ZvOSUWzqfzQcAUMeinv9yghnyOzdakqUI-6OMHfwQKiAYLU713cC-fizcWBAiH6LGpRKuHlYAMv7ZHdpdBsBNOg3h191Xo4DDtQZfFJt2WiyUz_uEvv36QHJSS29lppruyoaKzRc4eJ-PBw8aTooYwIHecqkW9cyAxIi0EAZXvANiRWqGm0ATyXCv14rk8MRqM3cMKLnqF4qsMvYkIIm7GHMpmsI172oYOAyE-mv0N0W53GT68isxty2-vvRk77bjvOkHhWMAdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود هیئت پاکستانی به تهران برای ادای احترام به پیکر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/farsna/446216" target="_blank">📅 13:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446215">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f6ba4e64c.mp4?token=bMmzkvUlannghmWkegzZgNpU80X2UmidSiyz_Oj0nYLzI6hkUbXVL0r794j7Kq7RQQIPm4DGENdX7Lt5XOo5eT38tJnvXNGQbGxFkjKz4rCKZKjiSkopJXyCsfJayddX-eQDopkv5upCUHj0HcO_C3stDR9DY5Xmq_Ubehz1g1ExgzjNpaV9eQ-3g0pv9Q7MmRDYGLuSROHm0-Ok3Ojdk80NafKPAt2hOwFXOZdj-spNmGrzMj08O3_ovIXECpsdtnjKEgMTzSOAUe7pKG8hzfdp4oWyZtbTk1Ii2gqpHGSJEgCHot2-ulGTeBa75yu1csS_51LR_lrADsIK5sVOXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f6ba4e64c.mp4?token=bMmzkvUlannghmWkegzZgNpU80X2UmidSiyz_Oj0nYLzI6hkUbXVL0r794j7Kq7RQQIPm4DGENdX7Lt5XOo5eT38tJnvXNGQbGxFkjKz4rCKZKjiSkopJXyCsfJayddX-eQDopkv5upCUHj0HcO_C3stDR9DY5Xmq_Ubehz1g1ExgzjNpaV9eQ-3g0pv9Q7MmRDYGLuSROHm0-Ok3Ojdk80NafKPAt2hOwFXOZdj-spNmGrzMj08O3_ovIXECpsdtnjKEgMTzSOAUe7pKG8hzfdp4oWyZtbTk1Ii2gqpHGSJEgCHot2-ulGTeBa75yu1csS_51LR_lrADsIK5sVOXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع فرماندهان ارشد نیروهای مسلح با فرماندهٔ شهید کل قوا  @Farsna</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/farsna/446215" target="_blank">📅 12:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446214">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d18ea965.mp4?token=YwbDLdy3Pr759V97IliWQb__ODFCsZjXHXZbaRFapU_Kg2FYTYeihXnPuUXKVZGJIrWRDTqfu5m1xs8lFe24TtvGbWLX7sTM-DwPIFq9ZRLenWurWd9GfOTgcGuAz7US8nNIHVu-eUAxmz529sGftmBPPuscRgJpUTI7e2PLMqHhXC_zlCf55udOqdBTczvUZXeCeIlKzXlBogyLCS6G-FSF_AyZVtoPJxWScGO9wt-yRKePOcux-j0S5tsJa3RMCkyJs_yD4YI1yhFFfun_BkCg-GzJ0R-K6AtTFh_E6x4PXf-A-m5HaP-uVBotYRnHkw8k2VQMv7-g2EVNxhN2hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d18ea965.mp4?token=YwbDLdy3Pr759V97IliWQb__ODFCsZjXHXZbaRFapU_Kg2FYTYeihXnPuUXKVZGJIrWRDTqfu5m1xs8lFe24TtvGbWLX7sTM-DwPIFq9ZRLenWurWd9GfOTgcGuAz7US8nNIHVu-eUAxmz529sGftmBPPuscRgJpUTI7e2PLMqHhXC_zlCf55udOqdBTczvUZXeCeIlKzXlBogyLCS6G-FSF_AyZVtoPJxWScGO9wt-yRKePOcux-j0S5tsJa3RMCkyJs_yD4YI1yhFFfun_BkCg-GzJ0R-K6AtTFh_E6x4PXf-A-m5HaP-uVBotYRnHkw8k2VQMv7-g2EVNxhN2hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود رئیس‌جمهور گرجستان به تهران برای مراسم وداع با رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/farsna/446214" target="_blank">📅 12:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446213">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ec925b47e.mp4?token=Zgoxj__ctjQfaUomxpu98m7dsWPYGsVlpNyXV-x1Mq1nTlIbYli93Wegq_xRhJlFDE_F3UP-ZkKbgug33vjBU1Ac-wQdB5ta88wYdJ3wqNysrgTv7NCB_eS0TlTmHu8JnYW-JmYlm5CFVV9tFDTg2Z7mcB2r7-Tn0uX9iC7_x8oUHB0moSPWGLFdbT9wAZP9eohqzpJy7RAcrLc9EGv466t-ZIN9QgnnuKomc9QW2t3sA0Eehrtm8ZHrhkfc0YkdG3ZcqPS2HGbTLH7Baom-TZ0-ojmt0JgmrxjBwnYrdvXAmIqm6jjllUQmpG6ge6volGH9F6vGDamZ-1vHq4tTgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ec925b47e.mp4?token=Zgoxj__ctjQfaUomxpu98m7dsWPYGsVlpNyXV-x1Mq1nTlIbYli93Wegq_xRhJlFDE_F3UP-ZkKbgug33vjBU1Ac-wQdB5ta88wYdJ3wqNysrgTv7NCB_eS0TlTmHu8JnYW-JmYlm5CFVV9tFDTg2Z7mcB2r7-Tn0uX9iC7_x8oUHB0moSPWGLFdbT9wAZP9eohqzpJy7RAcrLc9EGv466t-ZIN9QgnnuKomc9QW2t3sA0Eehrtm8ZHrhkfc0YkdG3ZcqPS2HGbTLH7Baom-TZ0-ojmt0JgmrxjBwnYrdvXAmIqm6jjllUQmpG6ge6volGH9F6vGDamZ-1vHq4tTgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع فرماندهان ارشد نیروهای مسلح با فرماندهٔ شهید کل قوا  @Farsna</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/farsna/446213" target="_blank">📅 12:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446212">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97aeab7b7b.mp4?token=gXoIKi524VD4VEX_Sh-ylYY8t_bjPOrSbDlTX7BZhN8jLHudLjlSbLeI4M4S7bEGE_OJpZvMlHf1ilyAo2X5sp4QwiF42ISsUkCDEH7Tk2MBAIE-rFNZruNWcSnWCfchsUH7IWyRQc2Sax6ICIswta8KoguiQPEc23St8kInp-ovcA-FEhFdtkA0qZqDnNelty1Uj1CvAc0IQ3MUlkxRgHVDU8sYjW1mKd8DrDVbsT9x7LsgmZHxXoJT6afOkluIxCRnk445Qa4o82Z_t68wO-mXUnmP61rcWGs9PKfFebKveZWrOIYAaSUQZc7o3j6Fx-WkYvZAKCPRAAdJAGQrVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97aeab7b7b.mp4?token=gXoIKi524VD4VEX_Sh-ylYY8t_bjPOrSbDlTX7BZhN8jLHudLjlSbLeI4M4S7bEGE_OJpZvMlHf1ilyAo2X5sp4QwiF42ISsUkCDEH7Tk2MBAIE-rFNZruNWcSnWCfchsUH7IWyRQc2Sax6ICIswta8KoguiQPEc23St8kInp-ovcA-FEhFdtkA0qZqDnNelty1Uj1CvAc0IQ3MUlkxRgHVDU8sYjW1mKd8DrDVbsT9x7LsgmZHxXoJT6afOkluIxCRnk445Qa4o82Z_t68wO-mXUnmP61rcWGs9PKfFebKveZWrOIYAaSUQZc7o3j6Fx-WkYvZAKCPRAAdJAGQrVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع فرماندهان ارشد نیروهای مسلح با فرماندهٔ شهید کل قوا
@Farsna</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/446212" target="_blank">📅 12:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446210">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8e6eaa98.mp4?token=Q_t8o3rrvMoKINpRUNhlV6xYrB4OwOz1cTuUs80_kg9vEfyKuBf2b0jp9tGdotlbm1C-7tCcyLd3Jft6VXHtfYyhGv0Tzm9qLwr9WIqaE0DWDWwyM3II6K_jLvu7PeAdGK7r_puzjh5EqO_E5hsxh2hyqknvK-RD0ltwcTuImsje0tKgrzaGduqrxV3CcmbsKQDB59v7Az7QjzBzl1NJqLT7rOB-IgSrWmdv_KoRbtVDcboVLko4kVc4ErHgKDYnLqeqMs2gh9HP3uL7PdTJIa4V21HRR7j6cSZJxiDfAqIujbqw3ePDEDX5Y3aG8CRyWGbVUS8ZD-O4Yffyi61BCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8e6eaa98.mp4?token=Q_t8o3rrvMoKINpRUNhlV6xYrB4OwOz1cTuUs80_kg9vEfyKuBf2b0jp9tGdotlbm1C-7tCcyLd3Jft6VXHtfYyhGv0Tzm9qLwr9WIqaE0DWDWwyM3II6K_jLvu7PeAdGK7r_puzjh5EqO_E5hsxh2hyqknvK-RD0ltwcTuImsje0tKgrzaGduqrxV3CcmbsKQDB59v7Az7QjzBzl1NJqLT7rOB-IgSrWmdv_KoRbtVDcboVLko4kVc4ErHgKDYnLqeqMs2gh9HP3uL7PdTJIa4V21HRR7j6cSZJxiDfAqIujbqw3ePDEDX5Y3aG8CRyWGbVUS8ZD-O4Yffyi61BCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون رئیس‌جمهور ترکیه برای شرکت در مراسم وداع با رهبر شهید وارد تهران شد  @Farsna</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/446210" target="_blank">📅 12:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446208">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9579cbe8.mp4?token=t1hliKlzVjpqgSnAhYf7b6nO-RbwTBJ_IGTR9_okamFFwGZ3ceJlBC2i3nIjI5L5tlSDO2nfMbt1opd2eSXbFa2Qcru-AnGQuBPe1mvGC0bN6ydCsarDH37YPvjTzfyIMEuPDGKIXxX779ZHLYffVEWDkKR_Yx-p8CIF7g-yJzKzDeqpHVlcc1JZc2_tOR0Cd-pRZSGQS8b5oJltbguI0FcirA1PbrtAphRPa29H4k7_Nv6bxxTbzWU7eDyGARu_XhSitoubxhIG_1Wgnoegirhp_wJntmilJ2_MI-qTxBxkgq1_9M4rxkLAYKbSapNfL6w0V2SpfZBilxuk_TAE0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9579cbe8.mp4?token=t1hliKlzVjpqgSnAhYf7b6nO-RbwTBJ_IGTR9_okamFFwGZ3ceJlBC2i3nIjI5L5tlSDO2nfMbt1opd2eSXbFa2Qcru-AnGQuBPe1mvGC0bN6ydCsarDH37YPvjTzfyIMEuPDGKIXxX779ZHLYffVEWDkKR_Yx-p8CIF7g-yJzKzDeqpHVlcc1JZc2_tOR0Cd-pRZSGQS8b5oJltbguI0FcirA1PbrtAphRPa29H4k7_Nv6bxxTbzWU7eDyGARu_XhSitoubxhIG_1Wgnoegirhp_wJntmilJ2_MI-qTxBxkgq1_9M4rxkLAYKbSapNfL6w0V2SpfZBilxuk_TAE0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود هیئت عمانی به تهران برای شرکت در مراسم وداع با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/446208" target="_blank">📅 12:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446207">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2919107021.mp4?token=vaz7cUUA_tJ1YIMxfawbiAEwRhsMS9QbXPaY5K5vrPufS_m6gVPBV-b8Tjl-ufvBS68ijjH3ScGNYB9nFxAVWTq9sj_P7Nh0xFyHhzRaGG1xV753FW8pmin5UBf8pFyo3j2myb_z5m6Txg2encxS7O6-6zeVtFw1Bp47jpYMQDlSUFMv3zqLbw-5F-4KQwueb4W0jXB419tnaxL-dKjDu3ZkY97Cbx7XceOMxBDKnnNthNzAxSXU2WXy_MRh5Y2kJKr1wp5ksxoQpqUdJkD0em7wPkXf9xAwqPdRgF5H5EDAYGIAcqKpgQvW2_ltHFIcDt4P4_Z9Dwd7pkrqgCvs-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2919107021.mp4?token=vaz7cUUA_tJ1YIMxfawbiAEwRhsMS9QbXPaY5K5vrPufS_m6gVPBV-b8Tjl-ufvBS68ijjH3ScGNYB9nFxAVWTq9sj_P7Nh0xFyHhzRaGG1xV753FW8pmin5UBf8pFyo3j2myb_z5m6Txg2encxS7O6-6zeVtFw1Bp47jpYMQDlSUFMv3zqLbw-5F-4KQwueb4W0jXB419tnaxL-dKjDu3ZkY97Cbx7XceOMxBDKnnNthNzAxSXU2WXy_MRh5Y2kJKr1wp5ksxoQpqUdJkD0em7wPkXf9xAwqPdRgF5H5EDAYGIAcqKpgQvW2_ltHFIcDt4P4_Z9Dwd7pkrqgCvs-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌جمهور عراق برای شرکت در مراسم ادای احترام به پیکر رهبر شهید انقلاب وارد تهران شد.  @Farsna</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/446207" target="_blank">📅 12:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446206">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb3f4182e.mp4?token=PrcUau-OZgnuk8URTMqOVd1KKaRbztGMtkFFULF3JJJmm0Z4Ca8w-_2Ux4ItYyVfFykhKVhPVsJmRiwfKwkzV8HCNvgu8A0HtN6ctRtBzEJQF_TBcF5teAgARoK2spM0q3qCTA93H7v23aLCDxrKjQ92DRXkH5_c3QkboPjQuIQiY5y0doveqqn2JB0xLrLCp_aTBCWakTvmVM9lV8XlMCa7DJ3EAcXmtzJpa6RHWyu_GCTsFOrLcA4rSkjJpcHTFSAS0Lj925YjH8vWlNVBMAVtBHR_ycj_clqvbCmrm_OGVX6z06xjco9IE5DmxDJcwZAc7xG3p2h98xU-K2DWUDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb3f4182e.mp4?token=PrcUau-OZgnuk8URTMqOVd1KKaRbztGMtkFFULF3JJJmm0Z4Ca8w-_2Ux4ItYyVfFykhKVhPVsJmRiwfKwkzV8HCNvgu8A0HtN6ctRtBzEJQF_TBcF5teAgARoK2spM0q3qCTA93H7v23aLCDxrKjQ92DRXkH5_c3QkboPjQuIQiY5y0doveqqn2JB0xLrLCp_aTBCWakTvmVM9lV8XlMCa7DJ3EAcXmtzJpa6RHWyu_GCTsFOrLcA4rSkjJpcHTFSAS0Lj925YjH8vWlNVBMAVtBHR_ycj_clqvbCmrm_OGVX6z06xjco9IE5DmxDJcwZAc7xG3p2h98xU-K2DWUDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۰ نکتهٔ مهم برای حضور در تشییع رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/446206" target="_blank">📅 12:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446205">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38064a6885.mp4?token=Dly3LsT5ZtMW7Kc0gPl-RiH8aEU292TX3EqwKtjwX4O9_PCCKv-mWQMJmOoyhDxCh4mgrwz0mj1cJctnX8dx5eJr02BPA2svoMdI5BLB82t0C96vuFKWBjjt-hOtdvtK-P6Ndwv7wZabqFf9z1X9Qjp1RJ-Qwj1j-J0px9Dr1yUaiGCk2UguOt7i1gYvZG_Fl8HhFYL7YkEYHbyDGzyox4Q725oF5a3HeqJ92txrvZM-1F43zDptK4kd_BhXLsXTsZ2BQ4ync0trOly2JVS0XkcNIsNy40iTnvOOjqq-b5Ij6PIlVoM_d7TNc6ADu26q2xKQ12-4ipZcwFjyc4sVlF8iYoUVpNi8m_zMhIRrGkz1ylWSYRlBjYFYefToP91RitX9NWPRbvA7NGSUERz6-FvAJqiiQRlXJ0FCHbrtXjhdvJTzLH9wOXp4VgpFmmQqUEi41XyqL15flp5UFHQ7BPXoD9h4rGZybASf6U12kfDHifyYAFwoE-OT-noNYOeRQmwVWfKS_wkG6ZwBPzE8laB9z2YuvvSFKgv4K-XHQtyf-RPdwbf2YrmVHdv9950n2AThrgT6a-KKEdUxLHvjPkM8y3dD82qz_GV3utFWoqluNjzGQbHyIdSEjarJ6lU1OTUBZmR5kQ62vHY-LM2XebvHnWAf4tHJKfWjUZCFdpI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38064a6885.mp4?token=Dly3LsT5ZtMW7Kc0gPl-RiH8aEU292TX3EqwKtjwX4O9_PCCKv-mWQMJmOoyhDxCh4mgrwz0mj1cJctnX8dx5eJr02BPA2svoMdI5BLB82t0C96vuFKWBjjt-hOtdvtK-P6Ndwv7wZabqFf9z1X9Qjp1RJ-Qwj1j-J0px9Dr1yUaiGCk2UguOt7i1gYvZG_Fl8HhFYL7YkEYHbyDGzyox4Q725oF5a3HeqJ92txrvZM-1F43zDptK4kd_BhXLsXTsZ2BQ4ync0trOly2JVS0XkcNIsNy40iTnvOOjqq-b5Ij6PIlVoM_d7TNc6ADu26q2xKQ12-4ipZcwFjyc4sVlF8iYoUVpNi8m_zMhIRrGkz1ylWSYRlBjYFYefToP91RitX9NWPRbvA7NGSUERz6-FvAJqiiQRlXJ0FCHbrtXjhdvJTzLH9wOXp4VgpFmmQqUEi41XyqL15flp5UFHQ7BPXoD9h4rGZybASf6U12kfDHifyYAFwoE-OT-noNYOeRQmwVWfKS_wkG6ZwBPzE8laB9z2YuvvSFKgv4K-XHQtyf-RPdwbf2YrmVHdv9950n2AThrgT6a-KKEdUxLHvjPkM8y3dD82qz_GV3utFWoqluNjzGQbHyIdSEjarJ6lU1OTUBZmR5kQ62vHY-LM2XebvHnWAf4tHJKfWjUZCFdpI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود رئیس‌جمهور تاجیکستان به تهران برای وداع با رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/farsna/446205" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446204">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اطلاعیه شماره ۲ آستان قدس رضوی ویژهٔ مراسم تشییع و تدفین رهبر شهید انقلاب
🔹
آستان قدس رضوی با اولویت قطعی تداوم جریان زیارت و خدمت‌رسانی شایسته و ایمن به زائران عزیز، تمهیدات لازم را برای برگزاری شایسته مراسم تشییع و تدفین رهبر شهید انقلاب اسلامی و دیگر شهدای گران‌قدر از خانواده معظم ایشان پیش‌بینی کرده است.
🔹
در همین چارچوب و به‌منظور فراهم‌سازی مقدمات این مراسم باشکوه و معنوی، تمهیدات و تغییراتی در فرایند تشرف به زیارت بارگاه منور رضوی مدنظر قرار گرفته است.
🔹
بر این اساس، جریان زیارت و تردد زائران در صحن‌های پیرامونی حرم مطهر به‌صورت مستمر و بدون وقفه تداوم می‌یابد و محدودیت‌های تشرف و تردد، صرفاً در صحن‌ها و رواق‌های مرکزی حرم مطهر رضوی، از ظهر چهارشنبه ۱۷ تیرماه ۱۴۰۵ به‌صورت تدریجی اعمال می‌شود و تا پایان مراسم تدفین ادامه خواهد داشت.
🔹
از زائران حضرت شمس‌الشّموس(ع) خواهشمندیم این مهم را در برنامه‌ریزی سفر به مشهد مقدس مد نظر قرار دهند و با خادمان خود در اجرای هرچه شایسته‌تر این مراسم همکاری نمایند. یقین داریم همراهی و صبر شما، همچون همیشه، پشتوانه برگزاری آیینی در شأن حرم مطهر رضوی و رهبر شهید انقلاب اسلامی خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/446204" target="_blank">📅 11:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446203">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e495a0e0.mp4?token=XMUKsmvT4idA4yh8A9ikHChduRPew7ffl6Gq3W7KzKRsn7GB68KEmnEw2IORwb5Ep9KBUadfYzdevspn-aTvGHWEfzdlaKexQoYmOLS8x4tR_5KYMDCvYu6Doa7Z-83SSF4q2x7cINSmxOVSfcOu4GhGUoTDbIoKfixcGhK9jUAQ2sHis2bTntmROqBK5LIqY2iO8DOSIAfLgu1Qel5KX75afAPZ5Rc1amfgL4L0SUTOwM3343qF6hUDg_CPLWIOmUTCy4bejBWIlP3Kn4JQYtOXbaD2zv57f_HAPXUlNZqUL5X6habPWbpk-OBttmBPLovn5ECYt6j5MRxylDEgejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e495a0e0.mp4?token=XMUKsmvT4idA4yh8A9ikHChduRPew7ffl6Gq3W7KzKRsn7GB68KEmnEw2IORwb5Ep9KBUadfYzdevspn-aTvGHWEfzdlaKexQoYmOLS8x4tR_5KYMDCvYu6Doa7Z-83SSF4q2x7cINSmxOVSfcOu4GhGUoTDbIoKfixcGhK9jUAQ2sHis2bTntmROqBK5LIqY2iO8DOSIAfLgu1Qel5KX75afAPZ5Rc1amfgL4L0SUTOwM3343qF6hUDg_CPLWIOmUTCy4bejBWIlP3Kn4JQYtOXbaD2zv57f_HAPXUlNZqUL5X6habPWbpk-OBttmBPLovn5ECYt6j5MRxylDEgejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار رئیس اقلیم کردستان عراق با پزشکیان
@Farsna</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/446203" target="_blank">📅 11:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446202">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSSJQ7uPGcb7r0flV-C8dMgfm-FF65spOUAyOqY3ZVp1BYppY-YVYY2pAvb4aI6mJr8wgLCgpqWD_tarVeiWSXxj_gML4XprDZYLqUjbVLA45l4nqu9MLWk7Iv6MEJFZFaOGQVK1etbgTqTKJv4ooZ5N7Ou_NB3vwVYYcGoHYUd2gywz7B3ioalR_yBcTs9AXjqri7AWfL3dxyj3lWlqiX6QJ2CePzte-7T5LFePQF2lZGhYKEVPq_XmsWLtzt4JawKHGofBHLCH9IFZ1M1HaWYHtc3EMcSVJq73-TF8LM8uy4sbc8nn9Q14oxlJ2_mvSO1JE13GwRr28JSjRiE-Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازداشت یک جوان اسرائیلی به اتهام جاسوسی برای ایران
🔹
روزنامه یدیعوت آحارونوت گزارش داد دادستانی منطقه قدس اشغالی علیه یک جوان ۲۱ ساله به نام الی لیوون (Eli Levon) به اتهام جاسوسی برای ایران در دادگاه منطقه‌ای قدس کیفرخواست صادر کرده است.
🔹
بر اساس این گزارش، متهم در اواخر سال ۲۰۲۵ و اوایل سال ۲۰۲۶ با دو فرد که خود را «سینا» و «الکساندر» معرفی کرده و به ادعای دادستانی برای نهادهای اطلاعاتی ایران فعالیت می‌کردند، ارتباط برقرار کرده است.
🔹
به نوشته یدیعوت، این جوان مأموریت‌هایی از جمله عکاسی از اماکنی در قدس و ثبت تصاویر ساختمانی در محله بخاری را انجام داده و در ازای اجرای این مأموریت‌ها، مبالغی پول دریافت کرده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/446202" target="_blank">📅 11:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446201">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/765d628c1d.mp4?token=oEY8yboX2ue4vrKuT4KPvIoupXGoW5KlHdN_0R7soRhaTtAANUft4jusXxWYJkOoYihaMNgMy68EZltu59E5vg8QrLnh9Muuf_TRuSeEuyVjr5bT52xH8b4e3r773bboY1t7rmhJkqdAotcKh1CQu2KiifjHFFqcOe3DnoLjwElTzJVuO4YYzI6BffgPlSCG1pWH1XGJfXvSvzSpfJHdIAzTEKAUgYwYTpTkpu-OaORsGk1m8ZF6tuvE3OTLwA02NLkiuBADBnPoYPhxsX41bcloCpjUqctfoujaQIuqNLVEenq7c7n3Jawldwv04nLo9Iwwe4NKN2z7FKtMA-jwxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/765d628c1d.mp4?token=oEY8yboX2ue4vrKuT4KPvIoupXGoW5KlHdN_0R7soRhaTtAANUft4jusXxWYJkOoYihaMNgMy68EZltu59E5vg8QrLnh9Muuf_TRuSeEuyVjr5bT52xH8b4e3r773bboY1t7rmhJkqdAotcKh1CQu2KiifjHFFqcOe3DnoLjwElTzJVuO4YYzI6BffgPlSCG1pWH1XGJfXvSvzSpfJHdIAzTEKAUgYwYTpTkpu-OaORsGk1m8ZF6tuvE3OTLwA02NLkiuBADBnPoYPhxsX41bcloCpjUqctfoujaQIuqNLVEenq7c7n3Jawldwv04nLo9Iwwe4NKN2z7FKtMA-jwxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی و وزیر خارجۀ قزاقستان دیدار کردند
@Farsna</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/446201" target="_blank">📅 11:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446199">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df2fd6009a.mp4?token=iGvQWzmPCSVtCl4L7I1qmaP6QlNAIjlp_S9nBuFlj1grigvR7Sx53ozL-_Lmqw6onsG0j9DCIuIDlDdvVjs3MWQt1SqMHkzagso7tVvDQgOzWfYxUcZkbq9PuPH1ELhdpKcb4Of2QZ9cKegWp438_WWFIgabO1hTYJngqcVA6tsMDAlnBPoo3WEmWz_zQR1kS5Mfjw1u_PPFyT_dzhIKyiQnVG9WhNdfStajDg1HcOE0GqQvljyaRp_u70C75pIPgVCx4QIgNosnDzSkq1oEz9ckPnMehvwDtwPEGdKyZyjfgiDMgnevWSay2muHR5m1_TBKlWNsK2S1k1xqFXaOkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df2fd6009a.mp4?token=iGvQWzmPCSVtCl4L7I1qmaP6QlNAIjlp_S9nBuFlj1grigvR7Sx53ozL-_Lmqw6onsG0j9DCIuIDlDdvVjs3MWQt1SqMHkzagso7tVvDQgOzWfYxUcZkbq9PuPH1ELhdpKcb4Of2QZ9cKegWp438_WWFIgabO1hTYJngqcVA6tsMDAlnBPoo3WEmWz_zQR1kS5Mfjw1u_PPFyT_dzhIKyiQnVG9WhNdfStajDg1HcOE0GqQvljyaRp_u70C75pIPgVCx4QIgNosnDzSkq1oEz9ckPnMehvwDtwPEGdKyZyjfgiDMgnevWSay2muHR5m1_TBKlWNsK2S1k1xqFXaOkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود رئیس‌جمهور گرجستان به تهران برای مراسم وداع با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/446199" target="_blank">📅 11:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446198">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حزب‌الله برای رهبر شهید، مراسم یادبود برگزار می‌کند
🔹
جنبش حزب الله از مردم لبنان خواست در مراسم یادبودی که به خاطر رهبر شهید انقلاب برگزار خواهد شد، شرکت کنند.
🔹
این مراسم قرار است شامگاه چهارشنبه آینده در ضاحیه بیروت برگزار شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/446198" target="_blank">📅 11:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446197">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705ec49c6b.mp4?token=Bw0KaHfiYktopJpnzZK4Ne9J0KzYoiXU_t4zMi_EeVLXah-U4tIJPG6AXsuywFPy8ZAOB_tiY32IinYQLXtxvP-jLQmn5fSiVbF2q0E3Btx1im5PlOec3zjylSYflZue8Pri6sIjwFzGAys8uJ9SlpMN1c1DJ5m1iLtyajiEA6vfTpW9Wbx34_oZAGhuwwbUjFz9qM58HAFbdVSMIETq0e-QNeNEHiY3k5Vp_hBywsJK7U2lupP-k80uhxBpAE62ztg-9iaEPrPrJa94j_vVZknZyVKNDQbsanKKnPVq1Mev8u3yuyrZ5l5mWhRADpBQOQDce9NnrfE5w-uOBy5RoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705ec49c6b.mp4?token=Bw0KaHfiYktopJpnzZK4Ne9J0KzYoiXU_t4zMi_EeVLXah-U4tIJPG6AXsuywFPy8ZAOB_tiY32IinYQLXtxvP-jLQmn5fSiVbF2q0E3Btx1im5PlOec3zjylSYflZue8Pri6sIjwFzGAys8uJ9SlpMN1c1DJ5m1iLtyajiEA6vfTpW9Wbx34_oZAGhuwwbUjFz9qM58HAFbdVSMIETq0e-QNeNEHiY3k5Vp_hBywsJK7U2lupP-k80uhxBpAE62ztg-9iaEPrPrJa94j_vVZknZyVKNDQbsanKKnPVq1Mev8u3yuyrZ5l5mWhRADpBQOQDce9NnrfE5w-uOBy5RoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون رئیس‌جمهور ترکیه برای شرکت در مراسم وداع با رهبر شهید وارد تهران شد
@Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/446197" target="_blank">📅 11:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446194">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a01edc6a9.mp4?token=tM_WeBOzAw1mmisT3xEx-SqL_Z7OQ9l945briaFXRHweVt8umtXQ7VOCScPUEu4JJWrxdfj1940PdzHcgN0wv6_J0D2M9_OYOKKDz5IaJEgqWl1zYDLVakEdFkx3TUT4Sk-KLod8AMQRHgaPA0ni0DcucE4EhEavv8TGln_X5XpVtKdvo6_vKDp5QWmZ5dSDZdt9ZwUSIzC7Qq7ecKLGQ9vYHbMixYCoJ9k8v9g6C87Y6c0_WZaC9bQEhiNr_1yd5-7RPDN50Wi9ROqotb_ZyK0LedUJPHztLSDEFNFbB81UVilEq6fDz8pZpEh2Z-dpDarY0KqWC8ZK17jiq8EUhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a01edc6a9.mp4?token=tM_WeBOzAw1mmisT3xEx-SqL_Z7OQ9l945briaFXRHweVt8umtXQ7VOCScPUEu4JJWrxdfj1940PdzHcgN0wv6_J0D2M9_OYOKKDz5IaJEgqWl1zYDLVakEdFkx3TUT4Sk-KLod8AMQRHgaPA0ni0DcucE4EhEavv8TGln_X5XpVtKdvo6_vKDp5QWmZ5dSDZdt9ZwUSIzC7Qq7ecKLGQ9vYHbMixYCoJ9k8v9g6C87Y6c0_WZaC9bQEhiNr_1yd5-7RPDN50Wi9ROqotb_ZyK0LedUJPHztLSDEFNFbB81UVilEq6fDz8pZpEh2Z-dpDarY0KqWC8ZK17jiq8EUhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تظاهرات ضداسرائیلی در فرانسه در هزارمین روز جنگ غزه
🔹
همزمان با فرارسیدن هزارمین روز جنگ غزه، هزاران نفر در پاریس، پایتخت فرانسه، با برگزاری راهپیمایی سکوت، یاد قربانیان این جنگ را گرامی داشتند و خواستار پایان حملات اسرائیل به نوار غزه شدند.
🔹
شرکت‌کنندگان در این مراسم با همراهی صدای طبل و در سکوت در خیابان‌های پاریس حرکت کردند تا به گفته برگزارکنندگان، نسبت به تداوم کشتار غیرنظامیان فلسطینی اعتراض کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/446194" target="_blank">📅 11:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446193">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bB9Cxz-9Bs5KHMVGHmRoiqYJ--KfJeCr-ltEnAoe2zQ2FZltitSDJZQhQ81hVJ8vmJIJgqCHlBU4sO9wHqR_-kPnukh8Q_wpJQktt8HF8AphwLGQP7TSKl1bHgaUeavUxlH4VAafRGzpLaNYL_OksNfVMJ-91B9bFg_BxjMeZM8QhhHiX6vEPmyGNfp2FEkOiZVBP0hOPUy5-2CMGRhjXEMeOjIpnbV9KeacsiNg6hElldyYpUqhE0rOKUGwc1J5wEEiZaDU5JiY5EiL_n7WxMLctlTj_7J5CtBbOVLFBxnSmHIRV_NtgVfBQjB6mz1_QRvq6H6MEYerGAV-raZTuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ورود نخست‌وزیر ارمنستان به تهران برای شرکت در مراسم وداع با رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/446193" target="_blank">📅 11:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446192">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6a3c0ca20.mp4?token=E7x6sb1tpB7j3JX47-vZUP00k7uBmLN8p0ZzLu5nxpJsQ92Nhjan75C9kut6ZwJCZj3q-4bYWeo1azbu8NYnUT1ELnhyNnoz9WtScqAJdwjxXXnfb58BJdcHeOwRy6NCO01Cpky34nCSoCg_Iwno882dBm4KJRN7ggAFzJ2Qt-9MyBTq-5kK5pgg0u6bgYVgtzDf3ivlg2W_A4DydwCa06GTihg8WXMhXOPQcKYFdoljQ7uTt9a7KcBjKtFw41d6l9tPaoafwrzmmzRBWkssqAHPaGuitI_jtUzCWvy5ugScEfuQN19BK80BuVvsYlCvRkoe0gUGDLQLLVVVgxytGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6a3c0ca20.mp4?token=E7x6sb1tpB7j3JX47-vZUP00k7uBmLN8p0ZzLu5nxpJsQ92Nhjan75C9kut6ZwJCZj3q-4bYWeo1azbu8NYnUT1ELnhyNnoz9WtScqAJdwjxXXnfb58BJdcHeOwRy6NCO01Cpky34nCSoCg_Iwno882dBm4KJRN7ggAFzJ2Qt-9MyBTq-5kK5pgg0u6bgYVgtzDf3ivlg2W_A4DydwCa06GTihg8WXMhXOPQcKYFdoljQ7uTt9a7KcBjKtFw41d6l9tPaoafwrzmmzRBWkssqAHPaGuitI_jtUzCWvy5ugScEfuQN19BK80BuVvsYlCvRkoe0gUGDLQLLVVVgxytGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام جمعی از فرماندهان مقاومت اسلامی به پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/446192" target="_blank">📅 11:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446189">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A6wpycsqhcZX56E00SmI1qesGYcAEv_rVKLYsLnZ44YdYf5KpnZXo_ooBoSLjs5YKWaF76yk2yUm9OwwA3YNUk60Z1bmFDe6VrtDwdqkXLEP2kZ18yfYl1cAkfRGzMo2xXLTIeIcdAVCAPLMAxZwOTvRpVDS5hASoL0Vny7YiVFe0JhmyPrTcCDvQ9scYkk0zHRpTjvYBhxaBiUlz1QKhujHKB2VIlBOhKgX_CXE8sCOpxwVBR38GR_iUIiO3m2UD0lJjcipuaa-xSOf67ktbDws8FaVlpTkSUZSk1JEhvDU4TlWT62d4NOZcGEMy1z8U06FDEopDkTlVErmIMS1KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bianYvflU5xg7bsBzLwNAU0vLlMEwJ5SLlFix9RrI4qaTo87PhfCDSJ3_SnWks91-n6ZZvYPI9pLPdtO7L_0PzbeJtb4bpEJ3GOcmzLK1S0dAI_vcP8dIFh1wCUaQ-wQinkXXuZo-RqrIm432V21YGVviGncGD1DBlwJJnVC7l1MoOlUtByMwx-C7-mzecwKN0ambe4ZqM7KumejZfS8P13xsjLYl6O403gMoLalyMEC-GkKG025_8s0S5ZMozrjpEZB2wCHsOh_-p8EnVvvFpSsB6Biw-bbmwsuiO1LSBuKYQNqaCFdqJpEr6jgq1NgA32oYx4s3HzM7pwtEEmovQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tvy-mSPMlNsSLoQkNtvQ3sTrFuqKAEw-w-9lTqXpP2WJOfPifDGacLVemLzAODfqoYetSRkfpe0zrTi12c8l6wTx6EKvhg4TFRrE7_U7NePTlSfSie71rVN_6qAIn32jAtUmmus6BEj1HPjsQaF4c6zbiVC0BanQs6XYWKh6FZ1KLSu8tJGJ0RNdutkNN6kmAkYN30P4qCIuu71Y7vZHBTrKvDcXvvQp4xcxqxhWJkxqJL75JvO7no9QRl3KWdaeLhahJDxfXXTzuvid0kvkJIbwdYWDDWbJgIUK2Mi87o7wGw_EATXljJ_4WqyLsEyEEaT0rwgBT9GlMhqPMmemDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار رهبر ملی ترکمنستان با پزشکیان
@Farsna</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/446189" target="_blank">📅 11:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446188">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da991e29b8.mp4?token=l4T5I6ekMuSiGN-zY1KrFOVDdcMjsvUZylBsP5k_hLSrxUOK8dbvE1peva0YBe3jUDi0mNkx39Ul2CG7I8EH0XZUGo8Jl10QQIkkrK9oo4hR74njKllHqJ3xFm-H0gc3UWoHfDHmq1GsL1cKMDkByMC_byml7xwPejduMyh0mC1JCLVb-XPA8EOL48dwWnfPp9h2aRjZ4bAxWVh3R9AaNFDPffnqKNrJHAKtn8ewi4zvZOCN-ivZd0XA7iWfh1PXvjRoF3XRiFh7sGiTUjjELos3lB4h2Mtd0DuN2WDch8pLum-LsStiLy65VzVtbueH2fAgG88vjozVw3ZEK2PMRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da991e29b8.mp4?token=l4T5I6ekMuSiGN-zY1KrFOVDdcMjsvUZylBsP5k_hLSrxUOK8dbvE1peva0YBe3jUDi0mNkx39Ul2CG7I8EH0XZUGo8Jl10QQIkkrK9oo4hR74njKllHqJ3xFm-H0gc3UWoHfDHmq1GsL1cKMDkByMC_byml7xwPejduMyh0mC1JCLVb-XPA8EOL48dwWnfPp9h2aRjZ4bAxWVh3R9AaNFDPffnqKNrJHAKtn8ewi4zvZOCN-ivZd0XA7iWfh1PXvjRoF3XRiFh7sGiTUjjELos3lB4h2Mtd0DuN2WDch8pLum-LsStiLy65VzVtbueH2fAgG88vjozVw3ZEK2PMRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام حدادعادل و جمعی از مقامات کشوری به پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/446188" target="_blank">📅 11:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446187">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01d988089.mp4?token=SWly007gxZzmupDAbckmJNVD3wVMnwcd9UqqrACU51AMXvezEFKFY96ADjpXx5i0Ch7zeJq9kptVWJuKE0dFW7279a9wMqDd_T0QOewYPeiDFXvWcaXi2de6BD6T77EOGHrjn9SLU9UkCt1R-PFPUbzpS-KOVkKhhuTe9rd4VY8N6TGIVa2tY15aCXwCKjZu5K6xuFhPQvJjSBlNWO0eisf1uDIoVDvhsrFXyRUPqB9yzkWTXD9BrMqPpn9WOFb2Gzl3pyJeg_kWxelRJx5dX6YY_y5LPYOCPZInIa42mExYJ-zY86wucIIVM3XwBtrb-mXGU1iG87gz4ClTSX_oPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01d988089.mp4?token=SWly007gxZzmupDAbckmJNVD3wVMnwcd9UqqrACU51AMXvezEFKFY96ADjpXx5i0Ch7zeJq9kptVWJuKE0dFW7279a9wMqDd_T0QOewYPeiDFXvWcaXi2de6BD6T77EOGHrjn9SLU9UkCt1R-PFPUbzpS-KOVkKhhuTe9rd4VY8N6TGIVa2tY15aCXwCKjZu5K6xuFhPQvJjSBlNWO0eisf1uDIoVDvhsrFXyRUPqB9yzkWTXD9BrMqPpn9WOFb2Gzl3pyJeg_kWxelRJx5dX6YY_y5LPYOCPZInIa42mExYJ-zY86wucIIVM3XwBtrb-mXGU1iG87gz4ClTSX_oPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام هیئتی از بانوان ‌طلاب و  فعالان عرصهٔ بین‌الملل به پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/446187" target="_blank">📅 10:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446186">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/652fcc680d.mp4?token=Gei8qOXTcA_DbcVtveAy5626d81zth4nMhBzvL9zehXrEYF-6T3aFHhg--aQrHEo_LhsWmBzOFp9hjm8R1rEO-LOGtgAQjXNJekjWIPlCIM5WsfcCT3H1RYWnTcQXJ4-Hbjs4RwNyDfCD6XKranHJyoEMvTSryOAhInOAvbFw3POb8FrbshwXvQdBiqeCadWLK9KeoRHWTVdvCQZ8-g-iwqFhZ47Ssoyc4JRwQqaWEq9y-Dfag095LW7IQ9hbhdU_jX-6Rt1z4-yOrzlfoypJ-ke7mm2u0LeBLTAjlixAP3lAyM9lPrHQvR6PFiPGu0xF93QTQ3lagzkQxD1Npe7jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/652fcc680d.mp4?token=Gei8qOXTcA_DbcVtveAy5626d81zth4nMhBzvL9zehXrEYF-6T3aFHhg--aQrHEo_LhsWmBzOFp9hjm8R1rEO-LOGtgAQjXNJekjWIPlCIM5WsfcCT3H1RYWnTcQXJ4-Hbjs4RwNyDfCD6XKranHJyoEMvTSryOAhInOAvbFw3POb8FrbshwXvQdBiqeCadWLK9KeoRHWTVdvCQZ8-g-iwqFhZ47Ssoyc4JRwQqaWEq9y-Dfag095LW7IQ9hbhdU_jX-6Rt1z4-yOrzlfoypJ-ke7mm2u0LeBLTAjlixAP3lAyM9lPrHQvR6PFiPGu0xF93QTQ3lagzkQxD1Npe7jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام هیئتی از جمعیت اسلامی کشور بنگلادش به پیکر رهبر شهید انقلاب اسلامی
.
@Farsna</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/446186" target="_blank">📅 10:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446185">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aa82a200d.mp4?token=Vh9_8v1FoewSna9LLyYelstVWeIsm8Mfr4qOrO14TTZ5RRo-abF3JfC_12Rv0u_n5hNk4cjS-MQQCInP20ozQDMvJL3iiFt7UmNTqhAg8nKebpKZwLHWy9ZlCOTm3UYLwdrvlSwF6YA17TSspsuxNdxjiFCiCOjPwvqvxbf3EdiHdDBWpn8P2n7WvPOr-V02Kz-t_UpTMFmaC3NqUsdm8sQToxTefw9BKJvOl1mbbGgSoNubUOFyG5sFnnxi_j2tEUB8ulPNjTwmhYjf72nd9g7N03ds0x7HCS-Ut36zDBIWFyak-bFLbqJicynuPd9hZNXyd8arfzQkE9CdG_S0gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aa82a200d.mp4?token=Vh9_8v1FoewSna9LLyYelstVWeIsm8Mfr4qOrO14TTZ5RRo-abF3JfC_12Rv0u_n5hNk4cjS-MQQCInP20ozQDMvJL3iiFt7UmNTqhAg8nKebpKZwLHWy9ZlCOTm3UYLwdrvlSwF6YA17TSspsuxNdxjiFCiCOjPwvqvxbf3EdiHdDBWpn8P2n7WvPOr-V02Kz-t_UpTMFmaC3NqUsdm8sQToxTefw9BKJvOl1mbbGgSoNubUOFyG5sFnnxi_j2tEUB8ulPNjTwmhYjf72nd9g7N03ds0x7HCS-Ut36zDBIWFyak-bFLbqJicynuPd9hZNXyd8arfzQkE9CdG_S0gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام هیئتی از ارمنستان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/446185" target="_blank">📅 10:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446183">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90978d21ad.mp4?token=MJFF7sFFPNgay9sm-vHwZGbhJ6KPPNXazfPcVWRE44XSi718Mw2iYDeDyX6X_AsRabpEUiRq1pwBQ-_2xeQROzZ-WLBptWWcO9jOqnpl7NnSZMT96kVxCTtdw-gyif-Z4oKI3LmHLMmRrAjEXgiq_7cC0pj3XZ1NR6L0fIpvy_tDbqV6sbaDH29_x6X_XaqiZ60sDhMCJs3_ZmP9TlrZjH0FUoZKI-I1y-EiZl4CZtZnpaF3taFn_7kSlQNyikB6VKir2UBgzud38Qwt-mcGsAbIIgSh3idE_sf_2hUMtUplORlqZTy3R3R-62Vhc0ZNAwuyQma80zPmHMbMT7n1kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90978d21ad.mp4?token=MJFF7sFFPNgay9sm-vHwZGbhJ6KPPNXazfPcVWRE44XSi718Mw2iYDeDyX6X_AsRabpEUiRq1pwBQ-_2xeQROzZ-WLBptWWcO9jOqnpl7NnSZMT96kVxCTtdw-gyif-Z4oKI3LmHLMmRrAjEXgiq_7cC0pj3XZ1NR6L0fIpvy_tDbqV6sbaDH29_x6X_XaqiZ60sDhMCJs3_ZmP9TlrZjH0FUoZKI-I1y-EiZl4CZtZnpaF3taFn_7kSlQNyikB6VKir2UBgzud38Qwt-mcGsAbIIgSh3idE_sf_2hUMtUplORlqZTy3R3R-62Vhc0ZNAwuyQma80zPmHMbMT7n1kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام جمعی از نمایندگان پارلمان عراق، شیوخ، عشایر، احزاب اسلامی و احزاب منطقهٔ کردستان عراق به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/446183" target="_blank">📅 10:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446182">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e789c04085.mp4?token=m59aXZX70nC-NrFx7mWmF4orCY03EL1Yt4Q6jxJd98JW72OiSaTSJq-YdQb2Dgw-3J3RnYFCPwYX8LXsrOueEyRVxuTGsojwW2q8dJ4NLHirjoGw7CdqdWzZbF6UISJC2YiNZJltQN_4cdLNEl8aup-AMCY74ptl1fxh102rEKYvPGPB6g2uFQjgKxvnq_KA7y1Bez7E1iTgcOOC9GmaGEjNyZqIx78MrM4StIi2WfE9eAGU7LGm81RpveHP1h8EUtpToqdIhEZBkev7u8nmEtXH3kcMAAlATl2Ckd2obiSyaRL959nvmtSHzaR5bARam0n-SdwwdYmwF1yNRQWEjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e789c04085.mp4?token=m59aXZX70nC-NrFx7mWmF4orCY03EL1Yt4Q6jxJd98JW72OiSaTSJq-YdQb2Dgw-3J3RnYFCPwYX8LXsrOueEyRVxuTGsojwW2q8dJ4NLHirjoGw7CdqdWzZbF6UISJC2YiNZJltQN_4cdLNEl8aup-AMCY74ptl1fxh102rEKYvPGPB6g2uFQjgKxvnq_KA7y1Bez7E1iTgcOOC9GmaGEjNyZqIx78MrM4StIi2WfE9eAGU7LGm81RpveHP1h8EUtpToqdIhEZBkev7u8nmEtXH3kcMAAlATl2Ckd2obiSyaRL959nvmtSHzaR5bARam0n-SdwwdYmwF1yNRQWEjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام نمایندگان احزاب ملی سیاسی لبنان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/446182" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446181">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df2cab2b78.mp4?token=FETHt_cB5d8rNff4uTaydRj2h4xHuVupgZ4HAqIf9hnYR5bvnKm2I-vJk-DM8rhIus8wXcyXPFQ_HEA9pmI-BpGQgIMy_QhqjXj44NGNjU3At4B4nMsa2-xbLxULaiIccBuPtNX14uqH6-tb69wmu_aG3ixJTWbnDSardNGDduyj8cOrMl-HnBQanXPGe1RXIAe-GnETft7cuGnXfc9J6eC_GFqtMMZbb0Gp0ohDUoN-0i_muhqgbJ4JXNWnsQYllWWTJolDsXg86jFUUP4W2SlV5-iUGisbxDXV8CsJnfWOZb4adD2owfeA7xzcCarBoTC84T9_aPO4oGiQxBnorA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df2cab2b78.mp4?token=FETHt_cB5d8rNff4uTaydRj2h4xHuVupgZ4HAqIf9hnYR5bvnKm2I-vJk-DM8rhIus8wXcyXPFQ_HEA9pmI-BpGQgIMy_QhqjXj44NGNjU3At4B4nMsa2-xbLxULaiIccBuPtNX14uqH6-tb69wmu_aG3ixJTWbnDSardNGDduyj8cOrMl-HnBQanXPGe1RXIAe-GnETft7cuGnXfc9J6eC_GFqtMMZbb0Gp0ohDUoN-0i_muhqgbJ4JXNWnsQYllWWTJolDsXg86jFUUP4W2SlV5-iUGisbxDXV8CsJnfWOZb4adD2owfeA7xzcCarBoTC84T9_aPO4oGiQxBnorA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع جمعی از اعضای حزب‌الله لبنان و خانوادهٔ سید حسن نصرالله و عماد مغنیه و فرماندهان شهید حزب‌الله با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/446181" target="_blank">📅 10:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446180">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2d477d6c.mp4?token=RBJCfEw5Hx1_7l95ODy6PSffPWTZxXm9uclEeey3A_irCFXCRjKtKB3Y7hrhdEjeRmELlQvOdfFWtPC0WWmkBl7c9zChv6_HoxZcbER0qQy8a4DjZmdHH_zE3G3mb7H42EKPCW5Qiw__KmyrrCqTvGUgADq50cFL3x_B6DvBxZFesbXKok2X7XJck8tvq6QUCstUPWf6YsYyS3m09i-k40JNXILKPKNddh6-0mUjvndM-vYxXg44Zi_KoEazMv-vQqORp8TZ-osWb0dUTLivJz2W3BwTwl1BzlpilZFixq7x-YSYc3CH4rJGlnBjE4Tjw2rky2YNlWCOmQKJ8A_oOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2d477d6c.mp4?token=RBJCfEw5Hx1_7l95ODy6PSffPWTZxXm9uclEeey3A_irCFXCRjKtKB3Y7hrhdEjeRmELlQvOdfFWtPC0WWmkBl7c9zChv6_HoxZcbER0qQy8a4DjZmdHH_zE3G3mb7H42EKPCW5Qiw__KmyrrCqTvGUgADq50cFL3x_B6DvBxZFesbXKok2X7XJck8tvq6QUCstUPWf6YsYyS3m09i-k40JNXILKPKNddh6-0mUjvndM-vYxXg44Zi_KoEazMv-vQqORp8TZ-osWb0dUTLivJz2W3BwTwl1BzlpilZFixq7x-YSYc3CH4rJGlnBjE4Tjw2rky2YNlWCOmQKJ8A_oOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع جمعی از اصحاب رسانهٔ لبنان، عراق و افغانستان با پیکر مطهر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/446180" target="_blank">📅 10:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446179">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/931974eef8.mp4?token=d0FaRZV-9jime-p8ppyf1Y_Y_k7Vwuw7HMZLyVSF-CuTMHQLgoDvVM5p0352m9kdB5BRKIblMkjlguAtQtjhZwnENFKOqj3UbW65yjh2txycEGpeGoTpNGYAAJkrifdqYXXhWy0Gsn3bHw2HriIwBf4UcCSQsCJ3h0itgPVL2rEM0gyFmCLNa9KUCC_ODGGwdBNngKRgiOszfVj_DfkeYHLtNvBOVuZIrXOzcf37COS7G2Ul7alpocRetCN50oLIwZ94WQRAoHT0VFOqJm8Gfr2eZijwn6EAONnGMvp_269qRrH-ks8shCKFQXato5aNOZiMeYk-dKg0bCshoa27fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/931974eef8.mp4?token=d0FaRZV-9jime-p8ppyf1Y_Y_k7Vwuw7HMZLyVSF-CuTMHQLgoDvVM5p0352m9kdB5BRKIblMkjlguAtQtjhZwnENFKOqj3UbW65yjh2txycEGpeGoTpNGYAAJkrifdqYXXhWy0Gsn3bHw2HriIwBf4UcCSQsCJ3h0itgPVL2rEM0gyFmCLNa9KUCC_ODGGwdBNngKRgiOszfVj_DfkeYHLtNvBOVuZIrXOzcf37COS7G2Ul7alpocRetCN50oLIwZ94WQRAoHT0VFOqJm8Gfr2eZijwn6EAONnGMvp_269qRrH-ks8shCKFQXato5aNOZiMeYk-dKg0bCshoa27fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام هیئت شعبیهٔ فلسطین به پیکر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/446179" target="_blank">📅 10:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446178">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2a90374e8.mp4?token=UU3nlRCKzsQPz6nStvjLh1BAtodOWgedCS1MgzhKto7rgTn3Oh-xpCGTISpaVq-0Jtox5bG-FoM0zMke7iS7AthMkR6OtscibbZAFwN3FyAcg8eJg0CNLWok9LDRVXLvO2jv_KpmMNs0LH7DeWDBHGjv6G1bZXmfyjK0xxlm7CsQHOYvYhiA45HWEyRGjKIMZZQVImtNuShC7-y6L3XWua24rnleN3pnn-n--RUlv5RXjRYbNzETbZ4OBUGBPxaFY6pSdBCH-DHtGV0GPTnzZAKtUV0c-CQgfjbPTaBjNMJlq0xqc7SolfvD1qDU5pSnqP2kcD6TbRZmwrt_HfCwZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2a90374e8.mp4?token=UU3nlRCKzsQPz6nStvjLh1BAtodOWgedCS1MgzhKto7rgTn3Oh-xpCGTISpaVq-0Jtox5bG-FoM0zMke7iS7AthMkR6OtscibbZAFwN3FyAcg8eJg0CNLWok9LDRVXLvO2jv_KpmMNs0LH7DeWDBHGjv6G1bZXmfyjK0xxlm7CsQHOYvYhiA45HWEyRGjKIMZZQVImtNuShC7-y6L3XWua24rnleN3pnn-n--RUlv5RXjRYbNzETbZ4OBUGBPxaFY6pSdBCH-DHtGV0GPTnzZAKtUV0c-CQgfjbPTaBjNMJlq0xqc7SolfvD1qDU5pSnqP2kcD6TbRZmwrt_HfCwZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام هیئتی از علمای فلسطین
به پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/446178" target="_blank">📅 10:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446177">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3baf406e7.mp4?token=ByJdQmpDF_tku9dlfeqRluBy2Om319w3kYfO76dvlppAUNKAcRTZi_43pyIhLFokAi_G438HUkRzdFh49e4khabotwG3FQH_pNXGMyd8C_0vWzqi2GSQc8Ock7ScyYpSPI5KYpleIDI_Df6FJOHiSVAsnDS57Rly1zsyICaNji2q3DFMFoC_7eXYm6cCq13g3fHdKr-eN5sX5nFJPr6yknk7evrj7qIpzMAv5pi0HVHE2z4XkqH_I3mz96ucsYD0Do9vjGLmfkZx5qWRg1wMxi5UyF1osyRwBZc_Rtd73GlMLDU0R-JTBRaREIfdNmzBYk2zyii88G7Vq6KKzSbEOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3baf406e7.mp4?token=ByJdQmpDF_tku9dlfeqRluBy2Om319w3kYfO76dvlppAUNKAcRTZi_43pyIhLFokAi_G438HUkRzdFh49e4khabotwG3FQH_pNXGMyd8C_0vWzqi2GSQc8Ock7ScyYpSPI5KYpleIDI_Df6FJOHiSVAsnDS57Rly1zsyICaNji2q3DFMFoC_7eXYm6cCq13g3fHdKr-eN5sX5nFJPr6yknk7evrj7qIpzMAv5pi0HVHE2z4XkqH_I3mz96ucsYD0Do9vjGLmfkZx5qWRg1wMxi5UyF1osyRwBZc_Rtd73GlMLDU0R-JTBRaREIfdNmzBYk2zyii88G7Vq6KKzSbEOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌جمهور عراق برای شرکت در مراسم ادای احترام به پیکر رهبر شهید انقلاب وارد تهران شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/446177" target="_blank">📅 10:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446176">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت باب القبله طهران</strong></div>
<div class="tg-text">نماهنگ«‌مسافر کرببلا»
قـرار بـود ما فـداشـیـم
سیـدعـلی فدای‌ما شـد
بـالاخره‌بـعـد یـه عـمـری
مـسـافـر کرببلا شـد
شعر و صدای:سیـدجواد پرئی
گروه‌سرود: بنات الحیدر
تنظیم : یوسف جهانی
کارگردان: اسماعیل بهرامی
تهیه کننده : رسانه «هیأت‌باب‌القبله‌طهران»
‌    ━━━◈❖✿❖◈━━━
اینستاگرام
|
تلگرام
|
واتساپ
|
بـله
|
روبیکا
╭━━⊰•═
🍃
═•⊱━━╮
@babolghebleh_ir
╰━━⊰•═
🍃
═•⊱━━╯</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/446176" target="_blank">📅 10:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446175">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/446175" target="_blank">📅 10:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446174">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cb65272d.mp4?token=j-aL2uPqSGltx_v73W9Cr5aE11gLL-ARZ9IV6bUhd5YJIrp34yx-DsnDpI-O8Pq8PZZ-BCrRtnxRuh_NY8FBaRRk60ZrMWjWGIzq73YPAEwJQeP5lsOb4JRtNz-rF1_Faa6DySXlsoVx0y7PO-jBsTpAUBqCLbe6Wsi9keCc-TsuLB4pb-wnVgSbONtlv489N44xgD70HHrIgMszJYn8eUzeY_qh3dSYSKDmquLSwfMhPAon12HwAOThXzl-WIh8kwDxOjtd-lcamoMFbuGWBxXmZFXnJ3IXGawxDZbO0_mALFl8g-GHCPhcwffvtdiF-zDg08_cKA_2mCX8r4nMSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cb65272d.mp4?token=j-aL2uPqSGltx_v73W9Cr5aE11gLL-ARZ9IV6bUhd5YJIrp34yx-DsnDpI-O8Pq8PZZ-BCrRtnxRuh_NY8FBaRRk60ZrMWjWGIzq73YPAEwJQeP5lsOb4JRtNz-rF1_Faa6DySXlsoVx0y7PO-jBsTpAUBqCLbe6Wsi9keCc-TsuLB4pb-wnVgSbONtlv489N44xgD70HHrIgMszJYn8eUzeY_qh3dSYSKDmquLSwfMhPAon12HwAOThXzl-WIh8kwDxOjtd-lcamoMFbuGWBxXmZFXnJ3IXGawxDZbO0_mALFl8g-GHCPhcwffvtdiF-zDg08_cKA_2mCX8r4nMSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جمعی از رهبران هندو، شیعیان تایلند و شیعیان آلمان به رهبر شهید انقلاب ادای احترام کردند
@Farsna</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/446174" target="_blank">📅 10:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446173">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e981b69479.mp4?token=ZlOk5N3ok99i27b27NSOtTTxw0CTtXfkgASXMwJQRQIHN6jjuk_9SvA6klF6CZzoBJaW7yROU3-tDa8pDq1MZpSgEICIDrmfU6wHHmQYPro_1bmjSvyguHbXQHJKHZVepHViw19MrlDKEC6CNZ91UnWRDASor-USuzpoooK1MHiIZjnej4dXmTSHP1DG6yEp3i3ZYrZHIhZGHu4ZQk4FPpJfXxVsagNtyw5ThKfn3hv3VApMv8ERQpEsJXnIOYBzy6_d4YeYHo6Z2fC6sXhPhdCe3uUBSn1JcVuqqK2nhRfGE4d7ABvANgTxuu413-c4iiuMb99L7wzZeI981cIOPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e981b69479.mp4?token=ZlOk5N3ok99i27b27NSOtTTxw0CTtXfkgASXMwJQRQIHN6jjuk_9SvA6klF6CZzoBJaW7yROU3-tDa8pDq1MZpSgEICIDrmfU6wHHmQYPro_1bmjSvyguHbXQHJKHZVepHViw19MrlDKEC6CNZ91UnWRDASor-USuzpoooK1MHiIZjnej4dXmTSHP1DG6yEp3i3ZYrZHIhZGHu4ZQk4FPpJfXxVsagNtyw5ThKfn3hv3VApMv8ERQpEsJXnIOYBzy6_d4YeYHo6Z2fC6sXhPhdCe3uUBSn1JcVuqqK2nhRfGE4d7ABvANgTxuu413-c4iiuMb99L7wzZeI981cIOPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام نمایندگان پارلمان و عضو حزب احیای جمهوری بلغارستان به پیکر رهبر شهید انقلاب اسلامی
.
@Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/446173" target="_blank">📅 10:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446172">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/351721101b.mp4?token=bfXhEUMoYPxdZ1eKt4-H-5pUKJ4y_CE0jQ9Pk4eZkPYR9lgDX8igHLmBA8peJa-IYItm_6LSju9mbNTbrCRTz1P4h_Dm4kfPkgrgYhpbP7HqhdXNjNGDc165ZC3TGdPsaggQHquxK422HFwhpYI9bl7qU98KzeNPv2X8mwmJeTFu9Rgo3vNLMR9_nTEqVH0rwOunhxNi66NDH0pWdP9oU_R55b0Pk5u_-rw8ks0Ol9BBcuMuPq9tjskjqZQ2v5v6XUzUAhLLwzuZuYeAd86aVVkFzCXGBnnyoCk78BcNvuEPHNJixqap6LL2-TqbLqPhMxyyROE17h0NOFbjY7MN5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/351721101b.mp4?token=bfXhEUMoYPxdZ1eKt4-H-5pUKJ4y_CE0jQ9Pk4eZkPYR9lgDX8igHLmBA8peJa-IYItm_6LSju9mbNTbrCRTz1P4h_Dm4kfPkgrgYhpbP7HqhdXNjNGDc165ZC3TGdPsaggQHquxK422HFwhpYI9bl7qU98KzeNPv2X8mwmJeTFu9Rgo3vNLMR9_nTEqVH0rwOunhxNi66NDH0pWdP9oU_R55b0Pk5u_-rw8ks0Ol9BBcuMuPq9tjskjqZQ2v5v6XUzUAhLLwzuZuYeAd86aVVkFzCXGBnnyoCk78BcNvuEPHNJixqap6LL2-TqbLqPhMxyyROE17h0NOFbjY7MN5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام هیئت علمای روسیه به پیکر مطهر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/446172" target="_blank">📅 10:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446171">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/905841b04a.mp4?token=gR5X67WySvBqDgt5X4NwzC-bs7c9vmXji2uk2pnyiljs5FLuBqDlrEzr4D6i0mNo86TWJNw0h62P594yv8yg75BzymE1mSJf-0TlKrIB5Gp-WBcYrfCNBRV4d1B4DhEdI8RbWZnvJX-OqozpZ_qC228fKvTSQmN4TPR_OhKcEJmzGlrILD01530pDme6QixtiDn1lvs-mEFb12WlqOllXbKfMIGqiSI4J8wIxpht0UZ1Co9E3ZLIXi8FGHjdt7aKhNZ4qUePnVu_BgXHjDV3dXnTInPy6HnGIWT8mgdNvWR5o3axlFuO-u9SizDmn4sUSKuJB3RUT46IJUixdz5-fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/905841b04a.mp4?token=gR5X67WySvBqDgt5X4NwzC-bs7c9vmXji2uk2pnyiljs5FLuBqDlrEzr4D6i0mNo86TWJNw0h62P594yv8yg75BzymE1mSJf-0TlKrIB5Gp-WBcYrfCNBRV4d1B4DhEdI8RbWZnvJX-OqozpZ_qC228fKvTSQmN4TPR_OhKcEJmzGlrILD01530pDme6QixtiDn1lvs-mEFb12WlqOllXbKfMIGqiSI4J8wIxpht0UZ1Co9E3ZLIXi8FGHjdt7aKhNZ4qUePnVu_BgXHjDV3dXnTInPy6HnGIWT8mgdNvWR5o3axlFuO-u9SizDmn4sUSKuJB3RUT46IJUixdz5-fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام هیئت احزاب ترکیه به پیکر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/446171" target="_blank">📅 10:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446170">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/116bdea616.mp4?token=UGW5WUs_1Kbz630Wcp_ywIjyaGs_aKzWbzcbZsb3lmYGPUFOgbbMgUUUh0uaNkYAHMmmdKDUnXh7sfCFvJlEHy7URDpt3tatuV4AhC4cj37NojaIuV2tJ2j-WNgTS3T9RO73Lz8xnmUpkcIGm5I0SHdQ0pHAc6xAOa0et3hUGKrqp8plFdF9EoHX-JfrKzrV9aGpY5HKMXaQpRNMfwMQR04cTTOKc_nvgWnRw3fY6GICgduqhm7QJ-XJmIRBL4_ah098WQp9nyt5hVLQRXdAARYnnmNsYoUE1Aj__Vav1zT4zQ3XgyjZpZBRZyyi6rmSmiBpsP7g8DBQgJWi-5YbOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/116bdea616.mp4?token=UGW5WUs_1Kbz630Wcp_ywIjyaGs_aKzWbzcbZsb3lmYGPUFOgbbMgUUUh0uaNkYAHMmmdKDUnXh7sfCFvJlEHy7URDpt3tatuV4AhC4cj37NojaIuV2tJ2j-WNgTS3T9RO73Lz8xnmUpkcIGm5I0SHdQ0pHAc6xAOa0et3hUGKrqp8plFdF9EoHX-JfrKzrV9aGpY5HKMXaQpRNMfwMQR04cTTOKc_nvgWnRw3fY6GICgduqhm7QJ-XJmIRBL4_ah098WQp9nyt5hVLQRXdAARYnnmNsYoUE1Aj__Vav1zT4zQ3XgyjZpZBRZyyi6rmSmiBpsP7g8DBQgJWi-5YbOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع هیئت فاطمیون افغانستان با پیکر مطهر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/446170" target="_blank">📅 10:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446169">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65551a3320.mp4?token=Sdd0DbRowV-m643PSOpLriD11C3sceNmApioao2D226C7OQWsjaV672NM_HKbFPHECRv3oACYRBklBtpmqA_uEMbdzDMTXlbBga5ALUG0sqNS3nGvBNItE-waRtBD_IGteDJbJAVZFXjxf73h26HokzsBGz2FmOKUPzB0InRRqDrUXH5LGTPM32Vv98wlgDnJtvdQWjnhOFcB2Dyt5N38IbrWvnyYZFyOQQA7fSfQlPjtrRJ2ic0Rl01PUL4zPSSz4vnRviXiKW9CeBfkfb8E0rr-3gMdYV__mn9YquleWHwtPHx4y_87WYSXq7gbYAiCJDH9h5gIR6hkCGwMpeN8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65551a3320.mp4?token=Sdd0DbRowV-m643PSOpLriD11C3sceNmApioao2D226C7OQWsjaV672NM_HKbFPHECRv3oACYRBklBtpmqA_uEMbdzDMTXlbBga5ALUG0sqNS3nGvBNItE-waRtBD_IGteDJbJAVZFXjxf73h26HokzsBGz2FmOKUPzB0InRRqDrUXH5LGTPM32Vv98wlgDnJtvdQWjnhOFcB2Dyt5N38IbrWvnyYZFyOQQA7fSfQlPjtrRJ2ic0Rl01PUL4zPSSz4vnRviXiKW9CeBfkfb8E0rr-3gMdYV__mn9YquleWHwtPHx4y_87WYSXq7gbYAiCJDH9h5gIR6hkCGwMpeN8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام هیئت اداره عالی مسلمانان گرجستان به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/446169" target="_blank">📅 10:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446168">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ab6c6104e.mp4?token=fpNfrWmD4Y1OFQjwdrophWVudXXjJOI542Ue0z4-okyCPeGoEsYdu4yIJ-hU8562BJp7-1mbMwAquoAOKqJEhi5TLtksrS9v44XSzvTk0rzoWyrhRD7ofGNqRbAyCIdWIwznF3ZsTq427xw3Onqu_afmQ9Oey8tu1zOZwfEZw-qlF_gdM72VyRAgT1MDvuXl2MKoH_WbWark1klPuKj3vVka87ePHQTPlIAvN5ZvCefh00O6l8oMuMphHESXfkp-JcuAZrpY9Eqvry3xaHVrK__sAZyM25wePaxrg1o2kCo6NV3AqOFTG_zY0evWnP1n9gVD06l_kK_XjLtEB75x_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ab6c6104e.mp4?token=fpNfrWmD4Y1OFQjwdrophWVudXXjJOI542Ue0z4-okyCPeGoEsYdu4yIJ-hU8562BJp7-1mbMwAquoAOKqJEhi5TLtksrS9v44XSzvTk0rzoWyrhRD7ofGNqRbAyCIdWIwznF3ZsTq427xw3Onqu_afmQ9Oey8tu1zOZwfEZw-qlF_gdM72VyRAgT1MDvuXl2MKoH_WbWark1klPuKj3vVka87ePHQTPlIAvN5ZvCefh00O6l8oMuMphHESXfkp-JcuAZrpY9Eqvry3xaHVrK__sAZyM25wePaxrg1o2kCo6NV3AqOFTG_zY0evWnP1n9gVD06l_kK_XjLtEB75x_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور
هیئتی از رهبران شیعهٔ پاکستان در آیین وداع با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/446168" target="_blank">📅 10:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446167">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J81Gg1nT2NQXbMHZAxpl9tQkhVXGEIdmRoMlyVD4upif7Jbn-7vUcSfhvqbyBmSZUvtANdZrA9133TlXkxPXSkrIdGG06OXwPCKuVsR_DFAOBu0b1nTaPrnDJPV9tBq1hjS1rHN6LQGZY373aGK6mhDAB2hERA1ABqiwPaeIwH0fukYbu07ePhWV__HxxVNl9cXeHpR3XN8DTlNfImX_GQW-9Q57e6CI5EuqU5Z4bwSX0w7_un8nS6yG9zkbDieNVUXHSsrfE4_frtWgbZzzeyrcOZTaSRgzoO3DDDml0nbXqDDMuPaXEknFY3sZJBGkNTQPkoCi9GQrsMQvR4kEfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش سی‌ان‌ان از بدرقه آقای شهید ایران؛ نمایش قدرت و انسجام
🔹
شبکه خبری سی‌ان‌ان در گزارشی، مراسم تشییع رهبر شهید انقلاب را حامل پیامی از اقتدار و انسجام ایران به آمریکا و جهان خواند.
🔹
سی‌ان‌ان افزود، هدف از این مراسم، ارسال این پیام به جهان و دشمنان جمهوری اسلامی ایران عنوان شده که نظام نه‌تنها از جنگی موجودیتی جان سالم به در برده، بلکه رهبر شهید خود را به نمادی از مقاومت و پایداری تبدیل خواهد کرد.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/446167" target="_blank">📅 10:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446166">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77724b4de0.mp4?token=UY8BEO3WmpQoDbZAXvzo4kAQXMgm-9bhgBVw1Qg7U0iny-bdbdg8kf2wKTJY_PhPdnYviFqukbX8liwiA6RAAkQBgP6GqJ1l2u7_RAXClmiXIfFeuCo4jKm6PE5TGrLxXZe88r-BWrb-mkdwGLwHt9_YuQxjPvJPHI-fc2fnkcHdI9lyKMdYjuiomnRpaPNrehCbBe0pPy3D8sFB2LdWUlk5vfLfuuR7dHEzNGz_9jTT2QmpjTqBoPmikZBfxaD8ynjBeR1-BahoWUVTA08gGiLsgKzUdBUlaH-4nmSm3N5rR_JzhfpPrva-d4VL8yhg7YXHwVb6A4ssm_SY9i2y1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77724b4de0.mp4?token=UY8BEO3WmpQoDbZAXvzo4kAQXMgm-9bhgBVw1Qg7U0iny-bdbdg8kf2wKTJY_PhPdnYviFqukbX8liwiA6RAAkQBgP6GqJ1l2u7_RAXClmiXIfFeuCo4jKm6PE5TGrLxXZe88r-BWrb-mkdwGLwHt9_YuQxjPvJPHI-fc2fnkcHdI9lyKMdYjuiomnRpaPNrehCbBe0pPy3D8sFB2LdWUlk5vfLfuuR7dHEzNGz_9jTT2QmpjTqBoPmikZBfxaD8ynjBeR1-BahoWUVTA08gGiLsgKzUdBUlaH-4nmSm3N5rR_JzhfpPrva-d4VL8yhg7YXHwVb6A4ssm_SY9i2y1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود رئیس‌جمهور تاجیکستان به تهران برای وداع با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/446166" target="_blank">📅 10:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446165">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9563db8921.mp4?token=l-hbTnv2RgJMvn6yIlp5xK7Pp5kJBfLeJztKDm3F2dF_RiPcJf08jrcBhvkHC5J1-FZn-NZsKoppxmUqNb0-sOBzuBUpIp0-z1EDlJ3oUDpR7jmfyyYLrMeZtGbNyYYTjugaDV7dPmaEvdL2skaAqp1JiiNmVf1SiMfmOXEINRDxeLuzunwXOHyIR_AfahN--9zFZNTsaEfSy5KK_t8BA8AorCWFrE7jsFAzb6IP09ppVUYmlphogiWOK1g3mJ0RBloLrrhALAmeJ2Q2TgvQnZrMxOz_UrW4uUG2wU8o9E2BHKI4InmzkrLKKETGEotI1ZBbxSoXoiVKYncK5SCDOQDqklcWtZZGulIw3r8LYdxOx7V-VSOrYjL5f1wqcqzROuuePEI0iSz_ROFGrxGs9f_HWo8rcwJnNycfKTMzXdKrNonqivgtFMWkmgUGMHPaXYPmnfJzwVuu318Fhii0-q-1h3gnYUDJyEBVEEc_WGHfSnqcpSsvly5_PV-K_1ND58eLbvEOAJ92c_hXXZeAcdZYCA44z0_Ta5LmE9OY7sqdwaDvgtO4x1rCzSQJjtxMOP44dz_JZeAkMzTmz11oP0tMR89bsBUN42xGUhoPdn6qoBkNJmr0KIitFjeEewrVz-a_79XiI_oo0uw2P6pqMNzPfvr2yFSbhyypnz2ntj8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9563db8921.mp4?token=l-hbTnv2RgJMvn6yIlp5xK7Pp5kJBfLeJztKDm3F2dF_RiPcJf08jrcBhvkHC5J1-FZn-NZsKoppxmUqNb0-sOBzuBUpIp0-z1EDlJ3oUDpR7jmfyyYLrMeZtGbNyYYTjugaDV7dPmaEvdL2skaAqp1JiiNmVf1SiMfmOXEINRDxeLuzunwXOHyIR_AfahN--9zFZNTsaEfSy5KK_t8BA8AorCWFrE7jsFAzb6IP09ppVUYmlphogiWOK1g3mJ0RBloLrrhALAmeJ2Q2TgvQnZrMxOz_UrW4uUG2wU8o9E2BHKI4InmzkrLKKETGEotI1ZBbxSoXoiVKYncK5SCDOQDqklcWtZZGulIw3r8LYdxOx7V-VSOrYjL5f1wqcqzROuuePEI0iSz_ROFGrxGs9f_HWo8rcwJnNycfKTMzXdKrNonqivgtFMWkmgUGMHPaXYPmnfJzwVuu318Fhii0-q-1h3gnYUDJyEBVEEc_WGHfSnqcpSsvly5_PV-K_1ND58eLbvEOAJ92c_hXXZeAcdZYCA44z0_Ta5LmE9OY7sqdwaDvgtO4x1rCzSQJjtxMOP44dz_JZeAkMzTmz11oP0tMR89bsBUN42xGUhoPdn6qoBkNJmr0KIitFjeEewrVz-a_79XiI_oo0uw2P6pqMNzPfvr2yFSbhyypnz2ntj8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شیعیان کشورهای حوزهٔ خلیج فارس به قائد امت ادای احترام کردند
@Farsna</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/446165" target="_blank">📅 10:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446164">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCJYRvmWjtfFzypkT7FRKzhZPaXh5QM4bJaXt9To2gGvO0iyNwuXnTvHPY2ak-r4HhN4DnhuZby5QaSaLDPrxbN1YC9LjpMDAJ-ZQZQXn-Hwkwoba9hjQzso4uIUiP9vAlaRCSPnAAPJtGbrmfnQDDTkPQXuDrwp5TKWs6BrAXEGZrgNNjIDaCtmgajl7ApTNTy4jYUNmRnSy0ox4nkjfZGg79FGgDq71s3vgicjvIFyP1TyIjJdgvX3i4Ab4P-Uq340kwD4ElAGlusH6kZg4Zjw5DilME8a07Dig6zXTjaaKYqoJ0MQoqzaSm72KVvCnK0AE8POyHPxADU1vQyf3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محدودیت‌های کارت سوخت حذف شد
🔹
شرکت پخش فرآورده‌های نفتی: محدودیت‌های سوخت‌گیری با کارت هوشمند سوخت در ایام تشییع رهبر شهید انقلاب برداشته شد.
🔹
صدور کارت المثنی سوخت نیز یک‌روزه انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/446164" target="_blank">📅 10:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446163">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc1efa7b7.mp4?token=p-cDbPXUa7TPFFKlLwU0cnqzY4NVLB39cEGfgun7hwJIWaJzyRkrgPNz_rbCWJ9jCazzwZkzRZgbQtVXmk9CxZf3zK3hJOLftoqoUVa6ZkIai0FkX_GgeJH9Uf_vzwWm2a9sXIBYZTE5AxL6IzlEf_6yN0oilByd03yUJn6RyXnhmTfi1GEcFa0FUYMvG9J0wYgSv-edqU86bxxaDGJjO0m1HEV2ia6GSV11LGFtiACzau8XFxyaVSlpu_TuZrDbHhx6WdqyLBPmFnhDUxNP_1CMEC_4qh4hRykV-ugFSyeB4cgOmjxtRtsS6unOavwNBFUMVU7Vc97zx3YnoLTDWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc1efa7b7.mp4?token=p-cDbPXUa7TPFFKlLwU0cnqzY4NVLB39cEGfgun7hwJIWaJzyRkrgPNz_rbCWJ9jCazzwZkzRZgbQtVXmk9CxZf3zK3hJOLftoqoUVa6ZkIai0FkX_GgeJH9Uf_vzwWm2a9sXIBYZTE5AxL6IzlEf_6yN0oilByd03yUJn6RyXnhmTfi1GEcFa0FUYMvG9J0wYgSv-edqU86bxxaDGJjO0m1HEV2ia6GSV11LGFtiACzau8XFxyaVSlpu_TuZrDbHhx6WdqyLBPmFnhDUxNP_1CMEC_4qh4hRykV-ugFSyeB4cgOmjxtRtsS6unOavwNBFUMVU7Vc97zx3YnoLTDWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور احمد مسعود و هیئتی از افغانستان برای ادای احترام به قائد شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/446163" target="_blank">📅 09:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446162">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ae670d40b.mp4?token=ZYG83jtyXg6LmrOkjohqvE4rHmSpSsTUxILDYLtHz0nA5SXTROB_vDIoWerQPey600537O9rdPGfrFjrTU74cQVfyZeGIZiduIBr8XvVD4ab1Xr637nRUSmpcm-NT73bGmGQ9Gf0472iUvKRiVrmhadu0Fiq5_I71np_3S7MZ07THlX2wl6sPfxu0npZOrTwuO47QKsC-qZ3pBEsoJgmQYK2hmIef_Rro9SQnfbQUsmwlqg5Of_w59ka72DjL7F1GFNBokVg-UUxJMGSL7A9CTbba7pm2bgbQ3hgEvnPJyNKuQhFFSaA-fUFTz02vQ4pwrB3PbzbCoS2D1gIlAIemw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ae670d40b.mp4?token=ZYG83jtyXg6LmrOkjohqvE4rHmSpSsTUxILDYLtHz0nA5SXTROB_vDIoWerQPey600537O9rdPGfrFjrTU74cQVfyZeGIZiduIBr8XvVD4ab1Xr637nRUSmpcm-NT73bGmGQ9Gf0472iUvKRiVrmhadu0Fiq5_I71np_3S7MZ07THlX2wl6sPfxu0npZOrTwuO47QKsC-qZ3pBEsoJgmQYK2hmIef_Rro9SQnfbQUsmwlqg5Of_w59ka72DjL7F1GFNBokVg-UUxJMGSL7A9CTbba7pm2bgbQ3hgEvnPJyNKuQhFFSaA-fUFTz02vQ4pwrB3PbzbCoS2D1gIlAIemw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود رئیس مجلس ازبکستان به تهران برای ادای احترام به رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/446162" target="_blank">📅 09:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446161">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3CA1cmgyUhlFNxcbjAZBCoSmH_UTXck2AxgQ3CeCugJurijH-gR58PEvZ0tMlTmt_KkziUj-aVN8fCVLmyloWquok1KNo2WwYcXYaAb0wUuR4xO9gsU0Izr-U-rgwB1hOB8p0ON2UEqO3FEi-s_Y-8Y93KzHNfXKD-yd9Zke7o7pogQy3660-yKCYai-EM8dnYWkT1yusjJ7G3DUXkOv25bTmCLJDWp6dS0F4Exj_s2m-BUToSEarxMAtyRoW8eNr2RKEES9jZ7D7cJXvtmF3dUyYeBdRxqLVjZeJJL_6-I4h5SttQdKDo030SKGygGojf8wIcYoRLj_omb8zEblw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رئیس جمهور عراق عازم تهران شد
🔹
شبکه خبری العهد گزارش داد «نزار امیدی» رئیس جمهور عراق برای شرکت در مراسم تشییع رهبر شهید، عازم تهران شده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/446161" target="_blank">📅 09:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446160">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a23fccfdd1.mp4?token=NP-mq0uCj8ABqZ6YeN7tke26D5DQiIp8rjN_4EZiqQS2IequqvPDWCXTOFTphLSZHbFnW-C4paFQYAeJWUESPdJq64HpV0TU6bG-leY6Rn-AWIho40he7UbizE2zHNeG0J5yJ61dwkp6oESVknaQ2xVrqEEhsTqrNOPnH5gltYyigM_U8peQpPppxiRv82IAAC7uFuCwi20kTs3JFTT8jqlD_XYp59ALMW1OlMXstNLwsjmmopG353njGqYEC01SZZ-xQOzD7BqbqmhJV-uZNVZbkSe_3sAfCd4MzorE9ntL0n6gLbCZnqq2X-Lp6z22mKuCXv26IOZZ_oRYbva5ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a23fccfdd1.mp4?token=NP-mq0uCj8ABqZ6YeN7tke26D5DQiIp8rjN_4EZiqQS2IequqvPDWCXTOFTphLSZHbFnW-C4paFQYAeJWUESPdJq64HpV0TU6bG-leY6Rn-AWIho40he7UbizE2zHNeG0J5yJ61dwkp6oESVknaQ2xVrqEEhsTqrNOPnH5gltYyigM_U8peQpPppxiRv82IAAC7uFuCwi20kTs3JFTT8jqlD_XYp59ALMW1OlMXstNLwsjmmopG353njGqYEC01SZZ-xQOzD7BqbqmhJV-uZNVZbkSe_3sAfCd4MzorE9ntL0n6gLbCZnqq2X-Lp6z22mKuCXv26IOZZ_oRYbva5ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام جمعی از اعضای جنبش اَمل لبنان به پیکر قائد امت
@Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/446160" target="_blank">📅 09:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446159">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bbc863f81.mp4?token=UWDuIHf0jCKHUkKY0NUdE8_z7rktosC7sD97e4rcHHHycisCT9OzngLRJPH66fDaKdN-QyLABo0mGVq-0jwONSIe7LdVG0-0AP0_M-uNVcY1fBoBKDLONU9WCcY7-JBNQGRM2Tb-cxniB0lMHTvpE-VPYicwJKb7ugeZc3ykI5WCDi6pa4B0Yo7ocncWCzqDSxJx9DOU13su7S9pJtATqo5m1_YfD-HYmaWE1CvgEqGdafOc38VjwdMA-F1T0j_pZ7TI0jw6ka4PIWedXjErd4cxcQOtVQ5zWMbg-dfa8AIK1Z9I2qwSTf9HXR4L3erHZFTSE25M-z8GorxeVhGEZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bbc863f81.mp4?token=UWDuIHf0jCKHUkKY0NUdE8_z7rktosC7sD97e4rcHHHycisCT9OzngLRJPH66fDaKdN-QyLABo0mGVq-0jwONSIe7LdVG0-0AP0_M-uNVcY1fBoBKDLONU9WCcY7-JBNQGRM2Tb-cxniB0lMHTvpE-VPYicwJKb7ugeZc3ykI5WCDi6pa4B0Yo7ocncWCzqDSxJx9DOU13su7S9pJtATqo5m1_YfD-HYmaWE1CvgEqGdafOc38VjwdMA-F1T0j_pZ7TI0jw6ka4PIWedXjErd4cxcQOtVQ5zWMbg-dfa8AIK1Z9I2qwSTf9HXR4L3erHZFTSE25M-z8GorxeVhGEZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور استانداران نجف و کربلا و شخصیت‌های مجاهد عراق در مراسم وداع با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/446159" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446158">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb955c9ba1.mp4?token=nKy0LpSMy3Wok20HoEXeyFp_4nHujuZyBejHEF0zcEV0EE2O0YhBf0BMbfagGE85tUU-tKYvk0dXUhJHPIr2Yp315Iou8AVrB_WqA7xkc6DZtjF1D9F5DTPFoG3sZE2hroT-5mYPdZYuAdXO0d7_8elxWLYa1IgcaPEvSK4TJ-QVbyBZXtoxviCyUQxoXs8RqBaNFPUT9Vr6KbPUHoHKQOIDAHY2CWwzIsS5NizY9gNFc-YErOB21LBvfSvSMgLBm0-z0qf8KGd4oUaSDE0dsXihhoPgChpSOeDQvOfbXjKzoojG3RQLaE-dCJ8RvH_3tE2cvfZ8jb8MG_vzsXBS4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb955c9ba1.mp4?token=nKy0LpSMy3Wok20HoEXeyFp_4nHujuZyBejHEF0zcEV0EE2O0YhBf0BMbfagGE85tUU-tKYvk0dXUhJHPIr2Yp315Iou8AVrB_WqA7xkc6DZtjF1D9F5DTPFoG3sZE2hroT-5mYPdZYuAdXO0d7_8elxWLYa1IgcaPEvSK4TJ-QVbyBZXtoxviCyUQxoXs8RqBaNFPUT9Vr6KbPUHoHKQOIDAHY2CWwzIsS5NizY9gNFc-YErOB21LBvfSvSMgLBm0-z0qf8KGd4oUaSDE0dsXihhoPgChpSOeDQvOfbXjKzoojG3RQLaE-dCJ8RvH_3tE2cvfZ8jb8MG_vzsXBS4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام جمعی از شخصیت‌های حشدالشعبی عراق به پیکر مطهر رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446158" target="_blank">📅 09:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446157">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f418014f0.mp4?token=A10pbiKD-RWh4XxXdsPZ5CXbfRTnRZSj0-qPzRZ7eO4J9MvmexUkuJjo_A5KBcpHQbyxCBBBPgvzV6c3NW-zacLNZu2iYj3l1I0i9RnuYGtiUIEd-WQx6tfzQL00RGl6EQYy0gDGBenu6lpPcqPElhH6j-6xTnE-Ghhy8g6R-GEdeKsQa5WIPHF0fXgZqKo9ag-oCMuirg8WnfPeVZqqd-50m2I-nfFSm1o-cofCZvTZRZPPizDJFPAd4ybry3iuY-SeEFMB13g7YtQB8YD_RB1EKNUpZ9_qFfQHJAtbZjmsFQCD5f26a83WUoCrZoU6TDO5ffUN-fn6y8n6p5PTbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f418014f0.mp4?token=A10pbiKD-RWh4XxXdsPZ5CXbfRTnRZSj0-qPzRZ7eO4J9MvmexUkuJjo_A5KBcpHQbyxCBBBPgvzV6c3NW-zacLNZu2iYj3l1I0i9RnuYGtiUIEd-WQx6tfzQL00RGl6EQYy0gDGBenu6lpPcqPElhH6j-6xTnE-Ghhy8g6R-GEdeKsQa5WIPHF0fXgZqKo9ag-oCMuirg8WnfPeVZqqd-50m2I-nfFSm1o-cofCZvTZRZPPizDJFPAd4ybry3iuY-SeEFMB13g7YtQB8YD_RB1EKNUpZ9_qFfQHJAtbZjmsFQCD5f26a83WUoCrZoU6TDO5ffUN-fn6y8n6p5PTbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام جمعی از شخصیت‌های حشدالشعبی عراق به پیکر مطهر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/446157" target="_blank">📅 09:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446156">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ba0a3539.mp4?token=Q95d3qOKbGZQLMYAGqzlZW5OqBVKjKhO9ub5hCalkYFDq8GyWWneZh61AqVZ6PfqJuWrFOWDdpY1ow6f_UjN9r5qldsyH5SV3eofuhpTjZml_KAHK3zV4fmxtP7x0-TI3LvtJy5mpKNT0zpDNq4J8kh9seI1o6QCSEQZ8MC6KLreBHmwXwlfn38lWgRnZZgFHNJEtM3G2wKAHwk-WrbGYzwQgXApPQUu_8nLic2VBrwywM7Rga6j75y488uDyQU2bhxsR_TvLFvxvrIUhTXLGEkMuTpxpGxnb0-MpH35K4DjUBYz1IomYYAVZCf5iqAvJO_WLYZqcRybKWyylvdNTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ba0a3539.mp4?token=Q95d3qOKbGZQLMYAGqzlZW5OqBVKjKhO9ub5hCalkYFDq8GyWWneZh61AqVZ6PfqJuWrFOWDdpY1ow6f_UjN9r5qldsyH5SV3eofuhpTjZml_KAHK3zV4fmxtP7x0-TI3LvtJy5mpKNT0zpDNq4J8kh9seI1o6QCSEQZ8MC6KLreBHmwXwlfn38lWgRnZZgFHNJEtM3G2wKAHwk-WrbGYzwQgXApPQUu_8nLic2VBrwywM7Rga6j75y488uDyQU2bhxsR_TvLFvxvrIUhTXLGEkMuTpxpGxnb0-MpH35K4DjUBYz1IomYYAVZCf5iqAvJO_WLYZqcRybKWyylvdNTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع جمعی از شخصیت‌های جبههٔ مقاومت عراق با قائد امت
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/446156" target="_blank">📅 09:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446155">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1fc62f1ca.mp4?token=NdV0C8kXdugNuxUdTr1iZY0NuDEnq7Tg7AzFpR0ABY3a9BBXuh5ZmJECRBAFBkcpGfPfRqJRLVilWC9Cs766pOBbmAzusukzepvebVVIvweZvvSuL-JeY2YqAPkrRTavm9N-sKp2PoDe1Eo8nv3sP88cxdtLXptca6FfIQxnzs8AKJdimBdij9VIakvTNYbrYrAEG-FevREt5feYh2EdnGKDCK49TG6iESkm0To4I-xrpnXk_eXHtrKsI7e94BWnj4YUgwa7snHBqkIfeIFh7J_YsT2HHdtCJGXC4HOqNBXrq61PeafcP0uuEtHBfITzOBZ606E-U68VPn5OnEE2xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1fc62f1ca.mp4?token=NdV0C8kXdugNuxUdTr1iZY0NuDEnq7Tg7AzFpR0ABY3a9BBXuh5ZmJECRBAFBkcpGfPfRqJRLVilWC9Cs766pOBbmAzusukzepvebVVIvweZvvSuL-JeY2YqAPkrRTavm9N-sKp2PoDe1Eo8nv3sP88cxdtLXptca6FfIQxnzs8AKJdimBdij9VIakvTNYbrYrAEG-FevREt5feYh2EdnGKDCK49TG6iESkm0To4I-xrpnXk_eXHtrKsI7e94BWnj4YUgwa7snHBqkIfeIFh7J_YsT2HHdtCJGXC4HOqNBXrq61PeafcP0uuEtHBfITzOBZ606E-U68VPn5OnEE2xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سال‌ها آرزوی شهادت؛ سرانجام اجابت شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/446155" target="_blank">📅 09:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446154">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54672fa8d3.mp4?token=CNgkCG63wz1igVkl0SWQP5lr1noVkvyOPuOfmEn7btrNcUOsLss4GI4JwyNQb_Wlc0VuMJi7Y1ljAMh_yXwsbhUhtCRrOT58eHN3YZAVFb8HV1eiK62IGjk6Ce0BLY4Tp2PkGcw5r9qXuvh-mgjeqT1pnXChJPor_BiqL9b2cB9QS-ai0WxSYy1ZAXHZXCzKDE5PZ3ZM-kdlEWXhO1P2nLmB5VbAKxYi6KJLNLkAA4PVvA4k55rIX01oq8mfgnB3Ac5RFQ1nq4IQXqhvZSe07IQwzKSvo8aM8T9WG3VHN553roal_S4N1NkOPoCujr7BhvXEdEZLLe2NIocXKcMrqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54672fa8d3.mp4?token=CNgkCG63wz1igVkl0SWQP5lr1noVkvyOPuOfmEn7btrNcUOsLss4GI4JwyNQb_Wlc0VuMJi7Y1ljAMh_yXwsbhUhtCRrOT58eHN3YZAVFb8HV1eiK62IGjk6Ce0BLY4Tp2PkGcw5r9qXuvh-mgjeqT1pnXChJPor_BiqL9b2cB9QS-ai0WxSYy1ZAXHZXCzKDE5PZ3ZM-kdlEWXhO1P2nLmB5VbAKxYi6KJLNLkAA4PVvA4k55rIX01oq8mfgnB3Ac5RFQ1nq4IQXqhvZSe07IQwzKSvo8aM8T9WG3VHN553roal_S4N1NkOPoCujr7BhvXEdEZLLe2NIocXKcMrqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود رئیس اقلیم کردستان عراق به ایران برای شرکت در مراسم تشییع و وداع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/446154" target="_blank">📅 08:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446153">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61ef459c66.mp4?token=PwXsXCuyx3XsgekkIhIXjCIl8muCQ8pvygMp6pnsymeOK94FnshJb5EzcgmXsf6IXhAEFqtSjLKyv079sO67SzLFIQxH2hZX6tfgEs5-4zEy0hF5W4KWCK___5kPi-OnIWlKx8UFvbJqWTbWGhiaysJ3aEsHT1ZYUrR6fHW__8gIbB7NVijJTbwhC9WclaCQ85dgQew8J973yZw-77YMPuZVOvuuymYOjlIgtfYy7KafKPI52AJl-r2W8tIIhXtS7CvwjjWtIUmUcjW-yBuXBvitVBtDiFHEtv-XuNJEeifnCuI3BV7wYugOSji9jihud5163YA1GQN6EdiyrpMdjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61ef459c66.mp4?token=PwXsXCuyx3XsgekkIhIXjCIl8muCQ8pvygMp6pnsymeOK94FnshJb5EzcgmXsf6IXhAEFqtSjLKyv079sO67SzLFIQxH2hZX6tfgEs5-4zEy0hF5W4KWCK___5kPi-OnIWlKx8UFvbJqWTbWGhiaysJ3aEsHT1ZYUrR6fHW__8gIbB7NVijJTbwhC9WclaCQ85dgQew8J973yZw-77YMPuZVOvuuymYOjlIgtfYy7KafKPI52AJl-r2W8tIIhXtS7CvwjjWtIUmUcjW-yBuXBvitVBtDiFHEtv-XuNJEeifnCuI3BV7wYugOSji9jihud5163YA1GQN6EdiyrpMdjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود نخست‌وزیر ارمنستان به تهران برای شرکت در مراسم وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/446153" target="_blank">📅 08:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446152">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/821f8a1804.mp4?token=ZsJ_azUBCG_FW2kNgooWCClUeTskn6CKPu7J-mq4and2r55UnV9LHaTEGan01ADkK0s2rczTCg7DExTIs-sPlJ2Ah0sakrM72wlNllT85M0sdZTNcjqeBNgGlkgX4nG88NdajuY66_v_ReF6zqEgO2OI_hyLVsarJKr_KQiCIgSkf_zW2e5ien1lNdNuC4z8MJG-F-MHW2NICyxhNEBs_jQ_wIXGVwKT8jdLBXv2oLOrpkwPJe5gG9ug-aBFu6HvTNHgg8S9pZwYZ2xQDyF9W23VKUPJyPhfDoaOPJWNFd2Q0XopnmmalpqUFwoJOJjCyfabt5s1D2cr_mnonM2Enw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/821f8a1804.mp4?token=ZsJ_azUBCG_FW2kNgooWCClUeTskn6CKPu7J-mq4and2r55UnV9LHaTEGan01ADkK0s2rczTCg7DExTIs-sPlJ2Ah0sakrM72wlNllT85M0sdZTNcjqeBNgGlkgX4nG88NdajuY66_v_ReF6zqEgO2OI_hyLVsarJKr_KQiCIgSkf_zW2e5ien1lNdNuC4z8MJG-F-MHW2NICyxhNEBs_jQ_wIXGVwKT8jdLBXv2oLOrpkwPJe5gG9ug-aBFu6HvTNHgg8S9pZwYZ2xQDyF9W23VKUPJyPhfDoaOPJWNFd2Q0XopnmmalpqUFwoJOJjCyfabt5s1D2cr_mnonM2Enw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام گروهی از مجاهدان و شخصیت‌های کتائب حزب‌الله عراق به پیکر رهبر شهید
‌
@Farsna</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/farsna/446152" target="_blank">📅 08:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446151">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa1aa9d3c.mp4?token=i7ds1Th2C0dP0LNgyxProzjLOMcHbj3Uaor7pR8o4VMYSaOHPSf80lAhmfTLOCoUS6BDbJOWW6gMGaTB3dD9y6aC-E3kSXAzD3yl-qdrXgQeAf_BD4IQ9Jwjm4PxwX-5jvf3_jdQ9U3ZaLMRGgL6MisLtgtE7X4hbs3W8Uo1rjH5g8uEh_bOtYkdZd76A3FUGAj0PjGH-rHjK5QrPMFx6Z18MVavI0SEkvcQkHIhyE3mAURPRBixMOybU5MzK7c7_Y2jisBsn_xbeSB1R2H6B1X-tg1tErCtMqHaT_z_zYew_mFjyhqNtEUO-eRx0v3EjEACEIVIAnvgYZnoTaUCBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa1aa9d3c.mp4?token=i7ds1Th2C0dP0LNgyxProzjLOMcHbj3Uaor7pR8o4VMYSaOHPSf80lAhmfTLOCoUS6BDbJOWW6gMGaTB3dD9y6aC-E3kSXAzD3yl-qdrXgQeAf_BD4IQ9Jwjm4PxwX-5jvf3_jdQ9U3ZaLMRGgL6MisLtgtE7X4hbs3W8Uo1rjH5g8uEh_bOtYkdZd76A3FUGAj0PjGH-rHjK5QrPMFx6Z18MVavI0SEkvcQkHIhyE3mAURPRBixMOybU5MzK7c7_Y2jisBsn_xbeSB1R2H6B1X-tg1tErCtMqHaT_z_zYew_mFjyhqNtEUO-eRx0v3EjEACEIVIAnvgYZnoTaUCBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام هیئت‌های خارجی به قائد شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/446151" target="_blank">📅 08:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446144">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7_hyo-1FHyOhwZDdH3l3g0mCtrU0wlBJaNDyQJQZNKAa097B6_a3WwBRsF2nGkNY-HgFJBbvCaaJE4_a__6qD01swQrtH_NCeU7JGMfkHmtlo95iYbVa_d0Qjqad7hGHNhihkNM-vZgSyad8Wp16MfmK42hTdLP0DlQsrnlkdIchGEdYnRFbx-7zKlmHGHPlAdm_TIR9omHGCpbGEE8GHvd1MZXsbkbDUCCnPhPZlgNAZNafAsTpBiM6AlFXYXV0Ztwh86KHg0t3pRS6oMbc2tnQ60SP2nPyrY7EVZWV4QhQHWpX4ZpJvFvZFsRuD5_wwmp3nqfTq3elQlOWWFIsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c7L5rymx1j8iIJ5OxLpxu-Or1VpJjpMrJfHhTAd5J62lPJlrIBL5WKfkPAYYdxhP3dfk84jSnCFBYQhuxUaVf803fJK24tqbdb1XadvFRh3Kq6vK5jfuWR1SccfPJxq2BvfmLrMX7aNXXXV6LDDS1-k0ba4BvaCe5TnRrsIU4d7VnhwC3csIA93cZB2XC1OpCGsCRqeEF40bkQ6fwPk-QhWunENpwQ5sXz-P49KU3x065A5TZa883dUj2HyX06LnrPX3V3D_GwCYhu69AQKgkWcxwdSZfWyDTGv0zpfzTdCTR98OmQa06vi3HtEdCG9JdSm5g7lPGx6bYVRQ1iZE0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cS3OQf3O6mfXSymY0guYOhnaJ-QW7droAxL_Yo6oQEYIpEZXbZbMrV8ZkbkIFcqwmf12HMUwyL8TVS8JSCCo6hYrfukC4HSo_AVoTYqPENg6vYFu42A0BxilCUqXbn2R3NBS83NoQt8y5GLSsV3ETKW3v0erVeenmeB0MTT4-ASnn1851d8T_bZK2N5KprkaQ5R82dzeLzuMfX-FvyK9MoLK3SGWgxFd_sW_IItWioo6MQJ-6jHORpM4qfLNaUjtQa0yorEKgaqnhkywROGIcSICn174oYdHvREVEr6PP4xO9ar_KtITwKJYCYpCs9vfjgwaB-4WYCJZNKeL1O6XEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/syO6rqxJywXng2gENn4B1C09dEpNJCqHXp0ijUzrsABvjZkLIXaNRpgjdVlLiQQhJS8xnG01Srq0Hqu4Nlfzq4BYlOjJ-H-EuJChTMhiydPnAN3y5B7hldiNQzwFXkPMo6J8jMehstk2NURdTXlgGBBkeFD64F4UFTm0oleQfInWQWkIYBva2mGzeBgA11HVSeavQJLzplPndDNJA4XMqRTBjl8t8V6gENPPc_4bMFAL8gXQoJnIpUn0vdEZrcbUyjZXVFTnwjhAckCzC4b5qgSTvCwC99XYy6s9O_lYTsGpimk37QJogv0jZZLmhGrhcfU5AQTkDBwumS_Fsn5MvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l6LSXLYlCcpehggQ_4T5YVa9SYQqeW4ZXxouxg15TCgCUsuXr1ip7vDBNxKovNEvfXlRTbxe0ayyAKKOMj27TfHg4SlvUceFJlco0UUVVt51ERI8HwyJlR1JFAZe7DVz4fb58jAQyRYIXe3qEcDfW8OmkJuCBnblMI8151l_-IjKMkDzF5dRtKSa9Zlc2b1DFKVG_n3CQ8_N34__CCoJ2YnXloAt8T3yvzkKV9KrUVJStrrfkLDRK3FSpuLLrmdetrUB8GxcijwtZ0y-FlhLKIQSc20NuQx61hjs8h_00nijd5aXeAP5RH7QkbQrlEPpHZHdH58QZrqGNM417HFOXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ax7P7r7hqyPi9o_I3fy23C8LQPDruXKDFrVrw5vPnOsRGvca4ERkmlUW8469pYd4MAjEJ0VicfIY03Ibku0uRg-UBSJFW9Dzy3moHVnGn7q6g6unpcXT3wzuGPMJf1T-XAyO09cTk3JFDIu8pDEGi0BEh_PYwuN624ljGq6fuaake2RCscbvPRt6iv5VcqpOu11yVkPjhp-bCqeuimUXbeYuZyYTl0FeDATQskrgs3aDzE3HHyUMZNmCNF1gUJwcFDIiJ9OU2FRtQ5YiSVnu9KTto8I8yit18Z0Bv-aZqPfk0RBEj8U1nUbwbUEpxfzbKzKdTt2xO2nK3r7yr-DEEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MzjCh5dxhGpmAhHTdTCEAONt4bg9DacBo_YLiITYLejPTUqRnJjrieT2gWCBBlqS8aQqeyUxY0M72az37_Y3YAgrmMU9hdMHwYboTFWKAfhO15DUJAnWfRr4-mCFN6K80XjBi2sXQG_3gQ1ZajplEYYy8Jmxa12TyL2tWAZc6mfB5xubD39DUYR4EWqrcqBENiniVUaLNoHVdzAI7S_Z9Eq7IJHOcWsDCHqMk5JEsiMDqOH3kMNk-Jh3bcZJ6zi8o8N7xuFQW_T8ar1s3BN_XQzWharY5knl24sk-diYWa0kL4sq73LxNbKN-0XYj5zMVOSm-0ZsernVcYTscoiG3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ادای احترام علما و فرهیختگان جهان به پیکر رهبر شهید
عکس:
زینب حمزه لویی
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/446144" target="_blank">📅 08:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446143">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gadBHjqfQi74ZkLje6xiXPEw7mDWHIL4u0RoLvJp1XdMfs94IVxvYXnHqCVO1zZ9ftNmFsjt-Yr8QSkOuVU77D6K-KPzkiPZWClKoIVNhgltjItXnW1l-4AvVxqP6l2So7DPNhFnq8y-aDzCKzehx7fNsdxyO4gq9ijEloqFN7TBu_lKqOxST4JO-LqfT0Bgu70a57QWtsaGpCdAHho0CsRAKwns9JPkTN9Mo4gOE8pLkAX8igr1D8wIKqt9NYOfNAb_bMdr3OMVw1RikCDsYdAZqo7Ef0UefZRzy2aebzJe6rMhvId_c7_0X6meUjh0c0GkZqt1xXgTgyvPVoGBjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: شهادت رهبر عظیم‌الشأن ایران، اندوهی عمیق بر دل آحاد ملت ما، امت اسلامی و همه آزادگان جهان نشاند.
‌
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/446143" target="_blank">📅 08:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446142">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b5c42b261.mp4?token=N9xsKGnOuLVheLMSNSCxEglETIHQ9zEXcxtecoa72MdEv6okpHIwWqwD9fVe1KKyVrZhonihY4WGPrlWCs4p98SY9c6CWVQQCc9IHTV4hpiYmWF0wp7wEumQwEbExjZQpjyZFoMGbFw9f0aRBEeVzqplHPQKuhisb5VBySRxqGTbeJiZx8SBDpdOyz0HnBecEZxFt-uefR8j6qznAeXVGysnpj5pjtVxsx9tPNaQeBeG3ISs5LggbH2ohQZPFpLUhqQc5yypwDZthO8FjiuY9ZJvUrX5bPX1O7PLN--bRaOenIrMwnrsajWKC7b2rpRBpW7cOpF7NuAqsHOedzWHmEx_531jnJerjQaiJDBeEZG32YsToY9Xu9xz2PRf3eDh2BCNsDbsr6X7JCdti9sqFp5ijLpydg0e9qvmswGMG7XJgMCZgg92S1VSG1gSw7jgEoeZjCz_JxIuyMRgYdOm9vr1AN4D0QmcgDQWK52Ar9PlE-F3TfJFz3eOfyAyuJEgkU7nVehhHOpk1rWzBduTorZAoLxaxegeospwvH0Cm89IQhe0SG-ViLmdDrlbFogqgPn4CicY4gKVFsIFtNZqFYr-krDzhvJq5VV_Yi0CfkF2K3P9nbElIS20MQfhQIL2somYxkb5O-Og87phx_A9WDZzl-PIKg6r-DaBzEjaY6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b5c42b261.mp4?token=N9xsKGnOuLVheLMSNSCxEglETIHQ9zEXcxtecoa72MdEv6okpHIwWqwD9fVe1KKyVrZhonihY4WGPrlWCs4p98SY9c6CWVQQCc9IHTV4hpiYmWF0wp7wEumQwEbExjZQpjyZFoMGbFw9f0aRBEeVzqplHPQKuhisb5VBySRxqGTbeJiZx8SBDpdOyz0HnBecEZxFt-uefR8j6qznAeXVGysnpj5pjtVxsx9tPNaQeBeG3ISs5LggbH2ohQZPFpLUhqQc5yypwDZthO8FjiuY9ZJvUrX5bPX1O7PLN--bRaOenIrMwnrsajWKC7b2rpRBpW7cOpF7NuAqsHOedzWHmEx_531jnJerjQaiJDBeEZG32YsToY9Xu9xz2PRf3eDh2BCNsDbsr6X7JCdti9sqFp5ijLpydg0e9qvmswGMG7XJgMCZgg92S1VSG1gSw7jgEoeZjCz_JxIuyMRgYdOm9vr1AN4D0QmcgDQWK52Ar9PlE-F3TfJFz3eOfyAyuJEgkU7nVehhHOpk1rWzBduTorZAoLxaxegeospwvH0Cm89IQhe0SG-ViLmdDrlbFogqgPn4CicY4gKVFsIFtNZqFYr-krDzhvJq5VV_Yi0CfkF2K3P9nbElIS20MQfhQIL2somYxkb5O-Og87phx_A9WDZzl-PIKg6r-DaBzEjaY6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام گروهی از فضلا، اندیشمندان و چهره‌های اثرگذار جهان اسلام از کشورهای مالزی، لبنان، افغانستان، نروژ، پاکستان، روسیه، تونس سنگال، هند و مکزیک پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/446142" target="_blank">📅 08:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446141">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2fcb14972.mp4?token=K9v66Rw9vVsskh0eAl2OX4Xvjsq-Tvyr0SnbnpQ7p9iRc9hHt076koMGtcsl8xF1nziG7rwi4z6cZ2eGMqjbLqpDIyDIchWefFs99yghm87K4aHbED-Dxy-iFPT7dX6EQQy_lEdWSd8hm1gaRvpoTq0iAiPT4G2mXJTXRJJ414eRC2lJDQqy72ufiC2hgLrrl9hshTaRtt3jdTWeUhruVLPuI8ynsY_E1LhA_icft-p_mBOdOpbFFU2WhKgQx46q9aywZWE2PfIgyGT35xcKO_FJND-OwZb6G2qTc5psqJ8DRs9XxVSAdDwj52Go2tAIyQONlzP9-Im9WkxidzUhUTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2fcb14972.mp4?token=K9v66Rw9vVsskh0eAl2OX4Xvjsq-Tvyr0SnbnpQ7p9iRc9hHt076koMGtcsl8xF1nziG7rwi4z6cZ2eGMqjbLqpDIyDIchWefFs99yghm87K4aHbED-Dxy-iFPT7dX6EQQy_lEdWSd8hm1gaRvpoTq0iAiPT4G2mXJTXRJJ414eRC2lJDQqy72ufiC2hgLrrl9hshTaRtt3jdTWeUhruVLPuI8ynsY_E1LhA_icft-p_mBOdOpbFFU2WhKgQx46q9aywZWE2PfIgyGT35xcKO_FJND-OwZb6G2qTc5psqJ8DRs9XxVSAdDwj52Go2tAIyQONlzP9-Im9WkxidzUhUTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود رئیس مجلس عراق به تهران برای وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/446141" target="_blank">📅 08:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446140">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">زخمی شدن ۳ نظامی صهیونیست در جنوب لبنان
🔹
رادیو ارتش اسرائیل خبر داد سه نظامی صهیونیست در جریان درگیری با حزب‌الله در «بنت جبیل» زخمی شدند.
🔸
این درگیری‌ها در حالی ادامه دارد که دولت غربگرای لبنان به بهانۀ توقف جنگ، با اسرائیل به توافق اولیه دست یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/446140" target="_blank">📅 07:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446139">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/404b549e82.mp4?token=rWMUu_kZ39k7o2O45ODf1xeH7tNqL8qE32EDLlIATybUEU2DVQ64L56j-O48HwuDBoXGFDweAyb5gUdiyLnkM_Kcfr4aj3IlgDxGZB1hevd-oKe4HC2GTbub7McVxt-sXNqXNI4QJPh5uOyiYcjCB-WdKOITDdiEh0xHjcGVM9k-xfxITXGco1-00uoRr0Ar6C2WbqBJShremYUcTR1nZQRAYMJN_0rORBQWHphpSRHuvdcSg8pZX6hcAUb4Z6tw-i_WGWJEhHvt7RGpHXfoQWHlEOEucU6UrmMNNZh_Abgm7zyUkbOmFc4ylCcPY1wYpC21Uj6wpdl4Voqb1793O0Hkanuuh1yI_BpHqmREsrD9bSKXUr17uNSo4EQr2-eQt40fsR-fcpnE_D1Ev6Rg0fZEwvgox--ZyH8-Fqr27dy4Je25J5hhUbtye961HbJdQs5Bnw9r6FzkYGDj7z8wYpjvxeKQykZE3V9fZPZXEH0O5SCAY-o7lQPRmq7HfQTPUB3DwStyKB6-1o6siVCv7EP094GTU39dijTPtUZ4uuaT7eteUQBGMd-bfotmNhTb4JTOJgvK5qxJG9kmvI26IrZZTQONcQhdS9QT6A9P_9KM4zEp4Tgmr5NXpZisD-_K1cH2kEwLc0d7-fz2pSbaVjDMR2bZa42vLfnjBBQODkM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/404b549e82.mp4?token=rWMUu_kZ39k7o2O45ODf1xeH7tNqL8qE32EDLlIATybUEU2DVQ64L56j-O48HwuDBoXGFDweAyb5gUdiyLnkM_Kcfr4aj3IlgDxGZB1hevd-oKe4HC2GTbub7McVxt-sXNqXNI4QJPh5uOyiYcjCB-WdKOITDdiEh0xHjcGVM9k-xfxITXGco1-00uoRr0Ar6C2WbqBJShremYUcTR1nZQRAYMJN_0rORBQWHphpSRHuvdcSg8pZX6hcAUb4Z6tw-i_WGWJEhHvt7RGpHXfoQWHlEOEucU6UrmMNNZh_Abgm7zyUkbOmFc4ylCcPY1wYpC21Uj6wpdl4Voqb1793O0Hkanuuh1yI_BpHqmREsrD9bSKXUr17uNSo4EQr2-eQt40fsR-fcpnE_D1Ev6Rg0fZEwvgox--ZyH8-Fqr27dy4Je25J5hhUbtye961HbJdQs5Bnw9r6FzkYGDj7z8wYpjvxeKQykZE3V9fZPZXEH0O5SCAY-o7lQPRmq7HfQTPUB3DwStyKB6-1o6siVCv7EP094GTU39dijTPtUZ4uuaT7eteUQBGMd-bfotmNhTb4JTOJgvK5qxJG9kmvI26IrZZTQONcQhdS9QT6A9P_9KM4zEp4Tgmr5NXpZisD-_K1cH2kEwLc0d7-fz2pSbaVjDMR2bZa42vLfnjBBQODkM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود مقامات ترکمنستانی به تهران برای وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/446139" target="_blank">📅 07:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446135">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gqnu5AfhfcHVViOldBfpwvISyTz4QoIH0dURhqtIXuay_nVI6Fd5sdDbSVIWbrc0LDHfhS0WEHE__OuP-gdDbYCXVNvweL1T1NaykrqHUCpzWnSe3L7k4MRSN4vkNS5gsCoYleouCldwvJUUUiGrB3-XKaOS1LO1XpHzjj_PVJY-vc8PxFvChSw-8dq_VkxNMKL5X5tJdg9LxrgxF7w-uvq4ihKXwCqz2BXKpKgUWhghGFZFw0IpnJVNOYa5lWUCGNxYF90D_JH3EKqePxUBdrsuEDG4ZkdJkO0e6ML-ewK5ApqXtb6WY0ib90OFSRxRqRXSuhE_CLfzVG_KDXLOkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzPCWk42OqPt07MmI28sjhit6XWqR4UmDtChooU4RUPegaMREKQl8FdB9FKAQYfI8sEubEWjQZe5P0x9Pd55LsfiS1H9QAzi55d-8-Ldq1N-dLG7Fh_rp6K26bzszSfNJ0KlUtdH3IVKD20Itg6RpJdeLW_OBNgaEQNu0S262UP5N3ISlgquJlrh4OXGSjS3Ds6cdS_ahXGrhuVXjDQcF12S4ctZu0vC6FiQrWANC-xDkOyjx6dTja6LOH1qYXk_w-BD7qIFV3ZQexrgag9a4IJk-BnKxMkIYzrXSHf4HyG-fIQ6qPkQvTlt-MTNNSDQZ2fiyQxTIcf7JYKHHt15cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-97FuZ6YYW7nn7xFE9-CfiVxKVUyG0zollVGn7k9sbyQlOsSUSjBn_-rNavfc-0wRRogSI86DQKSPukZ7Vn_pu1jrgveE1KK2rU1e6_0-JPhGg__Fj_to2EW-t0tB50jDvzrvaawtJbKuEc2TG9OtbryWNuqx4F1WTBAlEV63g6AqP4YQUqwzAaxvsvFjzp94wzNCX2i8LQJSxly0kOYqKoG0Tcu8oPHTCAZMaIK6DozAb0p7Qnb2XyqFhj11tEb1hwwbYlCtj2EvhBUwtGAMTY7NaIIRbyBkwRDHzyioI1BNX0WCxnWEXtvpYXUYyMgi_0XC7iWiZWH8-ITU2OAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKu6aaeru52WkakikwGwSNXWf8Wn3ZLkQ_xRIhEoQaNKAT-DVzsoGzbhiBxTtJqtm-xqJIrNROHDb8Nx5HYja5pI62vupi9edJVu6suqAu2Bq-AyGL0UGMi3hW3uZXDiq4QE1DTMZtNspWBCLAODBeKIGyajRl9M1NaNbHJZpbHEApjU2tbooB9ZPDLiQoqb6ydpIIJ4id-SCnizDGEK87ZqjYU51i-7AFgoGSp-IxM2SXe2Kt-ryOsFkn3Prd0D9XWaUQOewjhME39fIx_xbxo8SEzPYrTLqOC_4LbO7M4zQxX_NcRMB0ABIIFQ6Mjw6_vuRgA7FCK4djHUenNw0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
برپایی زائرشهر بزرگ مقابل مصلی امام خمینی(ره) در تهران
عکس:
فاطمه‌زهرا اربابی
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/446135" target="_blank">📅 07:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446134">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQ6miQfieaUSKeIqvvMzPl7mcp2OfXx-KjQgZeQ2ePdpnY48yiMvBkuxs7yflToFhMQTqTAr0igoKCinMPUGOrErzosiiksvWN9qyv0SXd6hgDPZjhnaaN4NggCbiizVfzI-GLsK2EMSu_M_iH-ug_Jfli9_eMe-e8jXjZ25T0hF9qWM1V2OJETfnMzk2wf1uPPL8Ko8sH-OdpDpS-7k7buVcXyoS6JsuBfqlLncV11ZmjCyLFF9pMeN7k_R0IaQuRd2gSaVcFM_Js8Pu5oBOXgFWaz0miAcBQKekOaBL5Ty8SDK92V32OPd-zih8bVzKO3Bx90ZDzorEeSqu8y5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروسی: بازرسان آژانس هنوز به ایران بازنگشته‌اند
🔹
«رافائل گروسی» مدیرکل آژانس بین‌المللی انرژی اتمی بامداد امروز گفت که بازرسان هنوز به تأسیسات هسته‌ای ایران بازنگشته‌اند.
🔹
گروسی در مصاحبه با شبکه «ریانووستی» توضیح داد: «درمورد دسترسی - دقیقاً همان چیزی است که شما پرسیدید. ما هنوز نتوانسته‌ایم به این تأسیسات برگردیم. ما چنین دسترسی‌ای را درخواست کردیم، اما هنوز نتوانسته‌ایم آن را به دست آوریم».
🔹
گروسی سپس اظهار داشت که اطلاعاتی که آژانس اتمی در اختیار دارد، مبتنی بر آخرین کار بازرسی معمول آژانس است که قبل از جنگ ۱۲ روزه در تابستان گذشته انجام شده بود.
🔹
وی همچنین افزود: «یعنی ما دقیقاً می‌دانیم که این مواد کجا بوده و می‌دانیم چه مقدار از آنها وجود داشته است. پس از آن، ما مانند هر کس دیگری، با استفاده از تصاویر ماهواره‌ای و سایر ابزارهای مشابه، اشیاء را زیر نظر گرفتیم. ما هیچ حرکت قابل توجهی را ثبت نکردیم، البته به جز اینکه این تأسیسات به شدت آسیب دیده بودند. دسترسی به برخی از آنها مسدود شده بود».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/446134" target="_blank">📅 07:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446133">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🎥
ادای احترام هیئت فرهیختگان و فعالان فرهنگی رسانه‌ای از کشورهای اسپانیا، برزیل، آرژانتین، کلمبیا، اکوادور، بولیوی و نیکاراگوئه به پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/446133" target="_blank">📅 07:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446132">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f5b54f04.mp4?token=D6m-cEQrobJa0UTjNd0YktLBasddlGRAvOAsUfbg27BVde3f5g0TrZHpDEvpG7-HjFh9CBZI5TSNMa4L_uaaJXq1TyvZ0KlZJbZY0yRnm9sd1qpd9D2tRx1lsqcDABjAblVwX4f0vgJ8AXMsNpbovV4deN4qVtmHfk1dUFvew7pcYdGVWzHYVpZFWY66NvUQTfW4TJq067K9c1cVEdsP-hYtheLS3pOTZHlATVM7RPvAE-xzxiNRy9QyA_NBbPg6D7oa7yTBBR1y-SkGmG9RaS0JgKK1yakTCLU-kcmRYUS-Kl04hMfnHA1jrEi7YOToRP-eH5zUaoJi52A0Sol56A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f5b54f04.mp4?token=D6m-cEQrobJa0UTjNd0YktLBasddlGRAvOAsUfbg27BVde3f5g0TrZHpDEvpG7-HjFh9CBZI5TSNMa4L_uaaJXq1TyvZ0KlZJbZY0yRnm9sd1qpd9D2tRx1lsqcDABjAblVwX4f0vgJ8AXMsNpbovV4deN4qVtmHfk1dUFvew7pcYdGVWzHYVpZFWY66NvUQTfW4TJq067K9c1cVEdsP-hYtheLS3pOTZHlATVM7RPvAE-xzxiNRy9QyA_NBbPg6D7oa7yTBBR1y-SkGmG9RaS0JgKK1yakTCLU-kcmRYUS-Kl04hMfnHA1jrEi7YOToRP-eH5zUaoJi52A0Sol56A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود پیکر مطهر آیت‌الله العظمی خامنه‌ای رهبر شهید انقلاب به مصلی تهران  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/446132" target="_blank">📅 07:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446129">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pH92BRFAj9s-Tcg38Op7BYN6tY1Qmtqb2xON_hpH44Whc989rS58Nw4-eJEasY5AHE8wktt_dfYP06XJcoZc7KrYyUPGtGpWo1z3kqKT-9a3f8Zzb95PyvrS43dx0xk3Oy1eDISTSg4EpuREZZSLNcmPLv4_Zs0EFyPpHu8IiPZ10M3R6NeMpzlGmDYoqWFWvab2xJBF0naoBLgFt_tpgPNXY8JDvMGSRabei6pjd9Z5ov-_JNFBe5L1ruQkuh6TGnMt09GcrqDRB8Hw3o5mNaYI7vcDOH03sJauhJJ7B5Czfs0rQ0cqoJGzB5dW8s3wf-HmUsvaKH4lt8B-x9aNog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HhF90PC-0nFWH4WWTDIRv9vXtmZ87_Uzdi1mm5x6Ns552ayhgn2REZlyjTme6VunuYTZB3HoVgEAXwX0ycH4V8gI1tXUn1l1qwm9q2PmPVap1dB7JLgc4aJio9F4cVePtJ_jvbIdOhj7FstyTjrUBn5uKVPYBgv1-aIyv2nZspLceb49DNaX2VwsOL6RsH5RARFRrXvKbyOOgqP9XQK317tspGWjs6gOGgcnUz5qTMFol-Y_-Tfj1bbAyt8JeN_EC5ibK6L5r1uwrKbrhx-g3kwN8a1eSIn4Ly2Gh7-ZymfS7fRl5cp7h2HssXv30fjCEXSNkvXYF6ztuSdnhmdvMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOATBgF7sz9T5tzw7inwvHZWSX4B7NSN_QE_GzWCBUAosAYOHMT2MfsK0QTY_DK3dTBStUGV8vkLVwuIR-jg3WOtcupd3sTimZU_oGXiqaRjm9otTbVlogE-atJtJOjChhxTN5rnbsy7LYWkXnoBDV4ZbWHiOpVcwJNL0N7Ie4CEVrGy4sao1tQGGc2MQ7uUvPmMsrTqcQDodjhXjo-KFTlnsA_QcIlaBq3dvZMb_xeJNm8eYiuL7tQfU_E5Z2CMuTicg1__yrmjKa6V-IgZFJL4iCbbiNX3Cjp5mJEfEAstGEdOx2J3Pe1OolBeadMTMVULyO5RK1Lvj3aGm5Xjwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اولین تصاویر از محل استقرار پیکر مطهر رهبر شهید انقلاب و خانوادۀ شهیدشان در مصلی تهران
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/446129" target="_blank">📅 07:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446126">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kw89uKjsOoe_izqV0s6Y56Xqhl_pixvLr8vHlemTiiPf3RE9B6UD_C9i8VD2-xjPI59-O_Lq4RHJYNWV9_zJQhn1Ga4rcad_xwMZlSf6bEIA0Wo0Jj8p4-MrHn5DBPFUDka2YcH3GQ29rApM2jnhSZbvDLqmJ2VoeWsMN5sKiPezrI8tAHSPIkupofiLLs3oEYPQ_lI4UuwtOrA5i7gai50Shwzmw9Xap6cdlkNSgvHkgBqLDnBBgLoT3e42UaV-oLLgybg1jLV_eX6zW04zAspUj4lkRt4ygF8F1xPMfzCktaDRFpFgmF55BSJGJgb13jfp0aKhOyrKzH31BI5szg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tOnmfd-PDzhma1ThT2Q6mZgXXq-YAWo1ZWT2KNeybtQaTZdsEdGX5bJjMnD7IZmgP2heshWN6rFZGG9Ep0yubxotnljQXzVfk1LLGH93WpTo_mirLb4MObeHK4DWc6dHoVb8Gki99ZLSvGkYBNyPSXOmFth0G20BrHB8ODZHFIQSGxrW2Evdk8Fhvv51MYrp78erNvZycGhn9Li9ufCFQCYN6cWPjpCVuNQpP2Yd2CSbDGr8rABNc-3DR-F7OAxuhlspQTFa53dVpjEaVs22C523D43qrjDjjL3iUgUZ0u97X1uuoM3DtZw7xyQdvcipbt_DT362o3UfxyqoDDJM9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mOP-sA9zzlCr_IHdvX-qkYM9-OMhplTprHlGAx2hT-4TYUwfLVI6aaSp6fLHnJVaLQ_g9xDxXHRA2zKrb-xDQIzXZ97WVqNQ8OLE2vAFQ_2T3VNEUut2p2sPfq-c6-4XgLm60XqGmqmFzL-4AEgBJ8bvYrkV0Pye0RCjR_qQvvx2rVfkCn6qGiz_tdC7NjZkLhKhW0ypxllgsSIiCrHKtrF_9TeV4_4tsQklxYMSFAzNY9VkOZ_d6efcZDQujitRe-nSHpqUmio8FcAVpQsKhNXdm-DBDugmMB_01N7Mt-MRAune10QyxppG2EpfzrwUlFO-ZhFHGEVPY61cmM3HWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آخرین مراحل آماده‌سازی مصلی برای آخرین دیدار
عکس:
زینب خدابخشیان
@Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/446126" target="_blank">📅 07:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446119">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vD4Sb9zI5GuJxbLVFR_UKRcVqiFxRFn0_jZtgCVu1JRJ1U4vbAmTsS5XNgBCWdE6apbUV3SrZoe52j7hi1DUJ6nljU1csAe83qmose_GTgWwbvG5xi1_6SBHKR64rEe-PB61qwH0ODaD05ciK-OKAmoiOlGfl1_dkawdAHcBALbL6M3H1cbkF0g4X2xFtL7q07X_h_THpuW1LusSHN-EEClo7C5-i3_AujEfYItChrpB9yq4AtBNYjQpQ2RrMlit83oBpbcQEwxUSBLXAKUJ2uyP0EovKMEq8jgkkxz6Ya7zeqXaLhaHQsAkTIrNYIZwc12JiQGMoyR1LUWRJWHLYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XLWHRa7Sfvfqn-VEktulVWvX7qefo6sSDXRgteewew4UmE2FYTadN4Xo6vt4mW0qXiHrtwY6oJRs_VcRSxllZ9IOB4kJdnzmiqMcNzgowKIBUucPD9Kc4bFmm5sX2MdbJ5NnhN_J7mH3S-nLS2bHnKBFDtd4MounX6-mSll0kEgW85hUW2j1jF2PLimqOZMInma8IKTP6axG2lGxaBRf6DiKX4GLHwCxfO6I0ikvcEmeYSCN-RgL4etY05QxhN1WbIq1Beuv5iOEoInSeAFzGzeDM958-nrUNDV69S4ph8QNaYuVjkw0siujXpaeBM5WJs7G3NGpiBBGtZhc2K2apQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RpAZR2ApgOSXX71FlSjExy3gq5kBjK5uGLR0W-d_dsKKobmyB4lYeh6WN8zZVGKvXSEMq9NVy_H5-epdJub8SbzmPgNgs95VJHimzuYI-dtJ13BAFcoo20O3hkGfJkmptwxysK0WU6gvR9zbvVPn_uSnfWOTsj2HfzvYU0E5fjyAwwlD89jjaxcUbvzVfjwgnXLgCoZF7WHWkXhZ7G2NBu2gx90jW93h4ZV-IMxUBMHiUC4VVLNWAY7oe55BmLfHYnOMDKU11iAUOTGHjMGYSodSYWfzR9K3SwZI0HumRYt0euWDWKcJ807T53hV3X2bbg7j-AuBdJlHWnzBse6g8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZQg2h9Yt7PIozh5Jp-1hrNZ4DmayRvBeXWqShStpp0NRfmh2lTkw5oOXd8nCFuVtcJ6Yc_rMJxUsPdKw4jSSeZ_xke8xeB10kWCnR5jZrhaVWl5iHsBvtLzra2fJL3Ah-6BiedKfLLPDXAMh3V7iGNCsjp0hcr-tAHS1COKx-bFWMg73Z_ekNnfogdK3ni9NEUBacbtk2U-10J-vFjCIe0p5W80FMxQPmywe7KQxHlEk_ddYrVA1DMn-IRGO5ASiZA6PCDRfLyUu4s-0Hmsq_jtcMLQ85eVen7GkTyjH4aaan1u34pge-t3sMhf0movpqzsTgD9vhv1_4jdVdJOA_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L_4Guq1YahqSaCD1hE3wvdiVz32mfaONoUFUs--5QJh4qJoRagtuQXIL7FeKxpqNF0v6473Z2WeQ7IaNIUR5h_xdi4itZHJoZDrQ6KTxwsyCidxhW3TPYFaKQ2KAEh3KFZBXmrP2O141TWhUw1jcB0LiVNN1g817SWAaYLGqIpu1tgjl3Rc7HVOx66tcpXFe2jtZiFqNzW5niffUFgRfGYG5tuq9uB7KMpnht3xYtVPUA6CodH3yd7EL8s8kM5lfPSs07uVkW9K_X-QvqCJyVoHAF8KuAJPwz24S_ulViuIm4jyJ6YiufsWO21RcYpPqFd3cDEGGWTK_9Y5tFPydFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m2FzOLeq126r5WKA3BfIOO5VW3o0WPwUQH_fFnlwHtFFkHdxv4iJWphrSZizA1ISI_mCYdFy3KDh2kqZkqQ0OpGawUxamdxS233GP0eDJnE6sf0omtZ9DhFQs3suz_dXjzGxaU8RKaY9Voy5S2K8h11bxbzFqd7oNE2fZr3miVIiiDyYn7rw3ZdEyUp6RHMrDlj2ANTxHMYkqcpjSxmmHJKZbfh0e15eYbe1tya4-iluK7QJM77VsNykl9XlYoPoaf4UYzwyyLkJhJlbXDikKyu_NaAGe7aGFIibsSmugZQfzKK-K2lE5ccwLS-BCheYHPuHUFPL-tacHHD2zyxWdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OzHRXfAwbre1glwrodcpwZr79PxRAnlHXhi7dCPEYKqCOeV-IToANlVcyXvOo5rQF9ggasJSYMT8B8oSgd0nph23vx-zkqKF-w7Whg-yjUtp6mElEIuOMaquHtcQQb1OuYWHdtt7h4ZluuZ3gAo419DN6AXgpXGpg7bLYxfDuJTZVff7BUYlr5INg6p-DoeNA3iZlWlTrzBGZbtmTjuG_3fMMtWIjBiN_EjMDZaZU4dgnu3zTj59dq7jZQtcRP0N-NQNyyW0fVH3414BfeLId3qKQf5SqLi6Pmduve3YdvSRti3jxEM9zWk-cyX-7wlD9_u8BlpDgqMmQ5gWJQyyIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ادای احترام فرهیختگان و هیئت‌های دینی و شخصیت‌های سیاسی و فرهنگی کشورهای جهان
عکس:
زینب حمزه لویی
@farsimages</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/446119" target="_blank">📅 07:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446111">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/174ae4008d.mp4?token=Hc9-jq_aMIB4kp7hp6OS_KgoplhSFMt8l0L5R7AS-IQIJWyDyZscahnGWvP3F9Qx13RF79cpiD6mijU-lwQlbSrnK3AyJg1T3YPMrNI3NvD6WfaAJzSk-uq33yPbis7PKfuaIkZXzvUis1MeWum1fQpn0TR6rZid41kdNItFTw-XYE1Y3Qq_PyelcQ9aECCEoSAtKzUTTnC07RR0iPrBmOMHKjU0GQA7xgfE_VS-gBYMwlMY4l-vNMnr9IVWA8jRfK2_DjJg0gVCgvxAZof2QQ2lbv7prT_MJI4OnnKPTckT5Nm93C3Psbnmq3pPpDQTkMQJ8TvqHST3nCPoJJDm9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/174ae4008d.mp4?token=Hc9-jq_aMIB4kp7hp6OS_KgoplhSFMt8l0L5R7AS-IQIJWyDyZscahnGWvP3F9Qx13RF79cpiD6mijU-lwQlbSrnK3AyJg1T3YPMrNI3NvD6WfaAJzSk-uq33yPbis7PKfuaIkZXzvUis1MeWum1fQpn0TR6rZid41kdNItFTw-XYE1Y3Qq_PyelcQ9aECCEoSAtKzUTTnC07RR0iPrBmOMHKjU0GQA7xgfE_VS-gBYMwlMY4l-vNMnr9IVWA8jRfK2_DjJg0gVCgvxAZof2QQ2lbv7prT_MJI4OnnKPTckT5Nm93C3Psbnmq3pPpDQTkMQJ8TvqHST3nCPoJJDm9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام ادیان مختلف بر پیکر رهبر مجاهد شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/446111" target="_blank">📅 07:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446110">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64cfa34cf1.mp4?token=jgmY_b_FgcsQjME-nXcrsyGMA1oGp9cquQnbNbfP82Z2IRKBC24ETjE8jdEFqiJkPUfpEhjSWRxMoP9UdAe2HnnlCVC-UbX5PJVTd1CfhLbEWXt4aXvLJ6OOY88SSE3S7ZQPVwUFe1x_9rNM9G2DfngOAiKUHmlZbFj5B7QHys7jpDAcSnOnS3eCJwdqqmpqZgZPF4YLzBtUtarZ9mhHMVh2g-yrxJwLO1DwtzqJ7YLKVyzDHtjGlkMJmeIqwL0E3LEsMzC9fKiXk4kHYRGxtUnrcRXfvShMD3KMkeHIXX7aP33BE-F_RToBykv_uYLZXQc2tR9T2s7ebQtR8sQT3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64cfa34cf1.mp4?token=jgmY_b_FgcsQjME-nXcrsyGMA1oGp9cquQnbNbfP82Z2IRKBC24ETjE8jdEFqiJkPUfpEhjSWRxMoP9UdAe2HnnlCVC-UbX5PJVTd1CfhLbEWXt4aXvLJ6OOY88SSE3S7ZQPVwUFe1x_9rNM9G2DfngOAiKUHmlZbFj5B7QHys7jpDAcSnOnS3eCJwdqqmpqZgZPF4YLzBtUtarZ9mhHMVh2g-yrxJwLO1DwtzqJ7YLKVyzDHtjGlkMJmeIqwL0E3LEsMzC9fKiXk4kHYRGxtUnrcRXfvShMD3KMkeHIXX7aP33BE-F_RToBykv_uYLZXQc2tR9T2s7ebQtR8sQT3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام علما و فرهیختگان مذهبی از اندونزی و افغانستان به پیکر آقای شهید ایران  @Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/446110" target="_blank">📅 07:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446109">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_N2t_1L3IjsiU3P64NQfOWK7WUJ4HKbQlQYNuDutxcnNRaBWkq_rrOOgzvN4VFTYZSELYtzMS5f_eshNhL2AEb-do1yf35KdhEnn6Lv5DX5rDWabrx9OTlR6hnkU398o08Ye37oOKbRHc1LzQxUUWyd3qS7QdCJpqRXz-UMeSVgP9R2Z2f8JQuYLN-E7dRj9aCvPIGvHw-nVhO0GXQtWPGX3Uq5V6ng2MJbwP6z03NSnPjA07c21s79cv-nxbsS9GAs94OhvE_Gzj7GiB-QDKBMhEYvAVd91-Zvk0YVh05F_eOKM2or5gurezVOal8QFzt00rBV7jGycEp_yw_UDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محمدرضا» خانه را وقف امام حسین کرد؛ مادر، وقف آقای ایران
🔹
چندسال پیش آمد و یک‌راست نشست کنار مادر. سرش را پایین انداخت و گفت: «اگر می‌شود دیگر طبقه پایین را اجاره ندهیم؛ دلم می‌خواهد اینجا را حسینیه کنیم!»
🔹
طبقهٔ پایین خانه‌شان سال‌ها جز عاشقان سیدالشهدا مهمانی به خودش ندید تا امروز که قرار است میزبان دوستداران آقای دیگری باشد؛ یک میزبانی در غیاب صاحبخانه...
🔗
ماجرای این میزبانی عجیب را
اینجا
بخوانید
@farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/446109" target="_blank">📅 07:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446108">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c98e3fc7.mp4?token=I6wuwPa1Bzn-kqvxoR2b9qLqwPP3poR0kYze7mP5buA7bp_BEa16sUrJ8kNO-iH6ueH4xkLMvZyFa13cpR-NQqsl_shpqcywJqVA9todC7asRjeeJqX5g-Cq45A4ODP7cX1NrJOxaf5LiyBGNxHhsy5N8LH_tOsgUZdZERdI0BTOefTz1fWWi1nbAgsgQmmBPz10LntGaph7NqGh7jVZdjpnFcfx5LlHVEep5foSuwyDn2qpVpSRB1RFOaELS7F_1o_sw3bwn5l4ajOwtwdsJLenpU_DMbuYGcN_0k6rGSStTiusQZr2VvrimRyxaqOAQ2QL3n93Wfki6we98C7tzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c98e3fc7.mp4?token=I6wuwPa1Bzn-kqvxoR2b9qLqwPP3poR0kYze7mP5buA7bp_BEa16sUrJ8kNO-iH6ueH4xkLMvZyFa13cpR-NQqsl_shpqcywJqVA9todC7asRjeeJqX5g-Cq45A4ODP7cX1NrJOxaf5LiyBGNxHhsy5N8LH_tOsgUZdZERdI0BTOefTz1fWWi1nbAgsgQmmBPz10LntGaph7NqGh7jVZdjpnFcfx5LlHVEep5foSuwyDn2qpVpSRB1RFOaELS7F_1o_sw3bwn5l4ajOwtwdsJLenpU_DMbuYGcN_0k6rGSStTiusQZr2VvrimRyxaqOAQ2QL3n93Wfki6we98C7tzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود پیکر مطهر آیت‌الله العظمی خامنه‌ای رهبر شهید انقلاب به مصلی تهران  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/446108" target="_blank">📅 06:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446107">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpkwODWFWwuYfir3RkN07uJt-cGcomtGqb60QHjOzU5C4r_PogHkjaJZiek9urP5H1Bkn7F0FAeoHj3Vah2N7GtxZtekg3Ml6lHW5aF_Cvs1KsTSiHCO4SCfausnCSon7GusMaMoD4zjbstOxmuPAw-MXrhF0SXtDRPfFJCZcg3YQXG4FXxCry9aktdzLR4gMqwcQEcfl38EqBRwWd2NVqxiAyZnD-cQdKVwEG59VcnFYARD01rwwfJ9VVD7qWA7LFFL3xjvvDJFysAEm7wEw8Y8GqldVTJT-fhokvFyns65JWeQLhja48fxaGfjNJ4KTMVxHJdtd5-_DDt9xH0IKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران آمادۀ پذیرش ۹۶۰ هزار خودرو شد
🔹
معاون شهردار تهران: با آماده‌سازی بیش از ۸۰ پارکینگ در ۱۴ نقطۀ ورودی پایتخت، تهران آمادۀ پذیرش بیش‌از ۹۶۰ هزار خودرو شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/446107" target="_blank">📅 06:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446105">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219897dc3a.mp4?token=CstJL0Gh5VC8xfp4upYrQJWh-nrRJD64OrPE7l5NY7wfqvAtUNw_BYX6gxbm6YdeKd3T_S8ysTRC6E_iubPMP9T0VkM1KvaV49Yi6RLQtvVV4jrPVEMGB4PpkmUGXQ7Y72Hw_e0iJosNxGgW8iXsNpsa6oJdlaTRY6Ec94NmvjlAYcfvZ7GQo6inT3CRjo81m6EdHmpY0KJdbcp2zg8dfab0bg-iTeuMMuj5Hv_bPnVpz0M35mXdGyBA-WIkRRp1lFIA8N3zPAmkAxN6I_woI7_-jTNHH41qbNAoxOoBjkf0ENCzNsO7FfAXunaLHnOLK5KPGMrlBBHUayE732FlhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219897dc3a.mp4?token=CstJL0Gh5VC8xfp4upYrQJWh-nrRJD64OrPE7l5NY7wfqvAtUNw_BYX6gxbm6YdeKd3T_S8ysTRC6E_iubPMP9T0VkM1KvaV49Yi6RLQtvVV4jrPVEMGB4PpkmUGXQ7Y72Hw_e0iJosNxGgW8iXsNpsa6oJdlaTRY6Ec94NmvjlAYcfvZ7GQo6inT3CRjo81m6EdHmpY0KJdbcp2zg8dfab0bg-iTeuMMuj5Hv_bPnVpz0M35mXdGyBA-WIkRRp1lFIA8N3zPAmkAxN6I_woI7_-jTNHH41qbNAoxOoBjkf0ENCzNsO7FfAXunaLHnOLK5KPGMrlBBHUayE732FlhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود پیکر مطهر
آیت‌الله العظمی خامنه‌ای رهبر شهید انقلاب به مصلی تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/446105" target="_blank">📅 06:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446101">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h8aZGOzLlxTc6wNjZLziHT_E__9fhI02J7ZCBfhG0OnIMvUpun5QUhUBnyUltCsZ2TWbtvoxEWWnQBnEWk5pyN6dcwGtBTIeUxGhHrXn6zOm7TMLRH6vSB17v8cPqsf8YbcIlR5MFAtYwat0dYWgwAG7tRWUjAot-ieM_FHJSLMN0KvVveUgZg2JU4nLgZdXe5iCjfz2nhZPBJ1fKGwBw0j4cKHmkGh5OVmUyyVBd5k7IHUKglMVSupY7SxTcvPXe_xjDbW8Tb2U_WwFzrVu9SOZRQsrAWzxHpSrav9wOiFGvpOKxH0HzjqF2XM04UuSFqdAh715WhomwS7PnD1FwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eru1vNG7MNopzZG44jghXYNN6TStoWxO2xLxo5R8qxrsYLBBBuLxvRBMGyMqKQ1o_MSkFPMKVxaY4gGQrhH80--Ja6n2V6HCStUNXMjGQgR1AglEfw9Uvu3W_-vqKE3HjoGCfin5rVM9X_sCDEZt6yB7xn01J8c97pL4xiaeGIQGaifDx7XdOZMdEMiHAwubcnviXYbfj4B61FXkgz9-IqlBTR03erk2yfwBgFHWedBf40-JGgNS0-4wBfNDJFJoaWhUcA8t_hh7KSNtWtr7fN6nMPqfjynnhq-rfMJAJsSSP4JcTvilR_c1a3qm6PYf5cCZu5gW3HVbVakIKH6b-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NjLMIHNdaLuxcyT_YXJ32f1XG0YxNOPzlWs5oFBScGOwe7D8XawxvH27Ox7kQREnYHNITxvBZdo2R0V8TDxDj9EqFsm0zJAmkbyr3A5gf1sjDsP8wTwY2PSlQ_ZtsKVOc8p1y65nJ2bYhgiLH_mx5YImoh4bvPS-yl7BR80vIZEbuzofm5DQh0VYeA-K9eDgU9H7BN37ZG7gQsgvVNDyYn92PP1unNU1qVw7m4yttCo5tirWWrhgU0TVbKs4VPQIYBT_cIaFv3sEtKYaE1sQLTM6kSSXOifu3v_EjUBa0Mea6VMwzBLaXCUAu83FTC_RYoUKAvHtTv2AM_WWgd086w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U3FYqkpzxaUb5iTVFQ4EQkSXY9BvzBy_Mnbui6WKWwk_ZCxJ3eWrOCUg3N0WuOapyRCRAnNAaPrOya0rmHfhIkhFi6-bWp8hCPwE-Aq101IDmymvXFOh0VRZwh1fErYBPZF6NSsWbknj2OiSwNQaOLb3GvjrEiPxa4NwYtPxJpwU59_m1GjJgmXCXhYXru4oaiZHPzDwsgFzhu13is7uZKlyR3TTMyPNgSQTrWxXWPzKfyZYFTGPhizPSaO-HqXSKfSAJfLlFLm_wXZncYTW67vJ8HYz3d2-KBmL0ypzyqRccowVeF_YuK4MavmJGj9XCLOoPbadHryGNPUmg217Rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تهران آمادۀ آخرین دیدار
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/446101" target="_blank">📅 05:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446100">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37ef94ed2.mp4?token=XyHx3JKoKCut9uUOzwI6JfXmLJUfM3yhGQzJBEuEg57ZZCnbPzpt5PozhImEo6M0YwwwZZABQWtUE1uxYfSXFLKubsJOH-_rkBOAvrtcH4TDUdmB65nbkXzwW3VxQ7apwExBOPINRgO69eCmUHZJMoT8OmZgBmDhPUytDDzfC0Jv8Gcq7bFdLZSc0cJLV92o2u65cdCk6kLQGqYidshU1RP4fZbckeQkb0muLLMWy2jhu7ahQ32RQjwRKhmb9ULYK3x6PIC_VpDXnDy9dt1izv5YgiE3un1WB9I5Ng2KJCtQMxja1o7USdgsx0fvkiKtiQjLv3LywMCp5h4KeYMCgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37ef94ed2.mp4?token=XyHx3JKoKCut9uUOzwI6JfXmLJUfM3yhGQzJBEuEg57ZZCnbPzpt5PozhImEo6M0YwwwZZABQWtUE1uxYfSXFLKubsJOH-_rkBOAvrtcH4TDUdmB65nbkXzwW3VxQ7apwExBOPINRgO69eCmUHZJMoT8OmZgBmDhPUytDDzfC0Jv8Gcq7bFdLZSc0cJLV92o2u65cdCk6kLQGqYidshU1RP4fZbckeQkb0muLLMWy2jhu7ahQ32RQjwRKhmb9ULYK3x6PIC_VpDXnDy9dt1izv5YgiE3un1WB9I5Ng2KJCtQMxja1o7USdgsx0fvkiKtiQjLv3LywMCp5h4KeYMCgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موشکی که با آن ماکان نصیری را هدف گرفتند
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/446100" target="_blank">📅 05:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446099">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یک معترض مقابل مقر سازمان ملل در نیویورک خود را به آتش کشید
🔹
مردی که پرچم تبت را به دور خود پیچیده بود عصر پنجشنبه به وقت واشنگتن در چند متری مقر سازمان ملل متحد در شهر نیویورک اقدام به خودسوزی کرد. این فرد پس از حادثه با وضعیت وخیم و بحرانی به بیمارستان منتقل شده است.
🎥
تصاویر دوربین‌های مداربسته ساختمان سازمان ملل نشان می‌دهد که این مرد حوالی ساعت ۷ عصر، ابتدا پرچم تبت (منطقۀ خودمختاردر غرب چین) را روی پیاده‌رو خیابان پهن کرده و سپس خود را به آتش می‌کشد.
🔹
ماموران امدادی بلافاصله این مرد را به بیمارستان منتقل کردند؛ گزارش‌های پزشکی حاکی از آن است که وی در شرایط وخیم و تحت مراقبت‌های ویژه قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/446099" target="_blank">📅 04:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446098">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIIFa0DIwyBkkk9aBYLZCwphbQre4P4Otuxt2eldA89a9y2FZwvTIjl8jqjIyFZe4-BjbVHr-aL2DTFuWhYJusdhkrfo87dlPSD5MeTVOLCc-uWizAPhHG2xRjdgfht3LJgEFoJfz7rf_xuWN2sUaNQfZR3L-eWf9BWBSnK1ZJIiUv0KeDjAd6kVa1DY3t9btH9FM2m9mDbzn8QvfunjC8QVk_Tj9kelr9zE74ZgPS790Dd5h1yienIgVHHvaXTtObK2IwJjuRUQwu7pfAhNBteYN0OTnnesKcvCy5jjsJUyoAsPEspDi68F1AQRW6cYZuVIxdFEIlu4Nismn3Ai_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان بحث‌برانگیز
خداحافظی تلخ لوکیتا با جام
جانشین رونالدو، او را نجات داد
اسپانیا پرتغال اولین فینال زودرس جام
پرتغال ۲ - ۱ کرواسی
@Sportfars</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/446098" target="_blank">📅 04:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446097">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4vtfePJLqrkNX9hIBv4jFO23ZHXKC52T4Uhsqxif4JeT59fHxgTdM8B0bi4FLMZ1ICUxVxGT_7TanT4kLYT8CNS9FE-lY7drS5AmtKfLI1BlE-AjoY1ui7nCeL2_I6mt7VXGNUpNPWK_SbZRz7-QUBMfJd-530kNJU4HDLbluiws9p8n2A_1cczbod3xq6VA6p6tmF6wx7IaRVlbaMjRoCxpTWg6d6bcjKyH465sSXjFHL8nD1WGEb0o_fzFX0PJRNZz9ADNaRy1QrLh9rnikU6YcuwL3Hsu8ehDpG0WmAO876F-WFiJvjaEix_0saXMJ3B8Zomf29uUL4YHs4pzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران آمادۀ پذیرش ۹۶۰ هزار خودرو شد
🔹
معاون شهردار تهران: با آماده‌سازی بیش از ۸۰ پارکینگ در ۱۴ نقطۀ ورودی پایتخت، تهران آمادۀ پذیرش بیش‌از ۹۶۰ هزار خودرو شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/446097" target="_blank">📅 04:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446096">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIxr4pVjKC4bElUviU8jc9OLWM56U2KDmegMWSzPt36hZ4XAF7F__bXRWVNwhbI5XbrvA27IhWHFWzagNdlDF9SWwe2SOBcAK3vbnFN3UDWulx8MeH4IaDBlmst-7KLe2E0clBfwXDqvM0qw-8N_Q-yKHVUS55HXoxzIh4dnMMMSuIrdL0abAwBI1H2VjFngVD-SMi8VRheTCW29v6BRoBr83-vinNy9evQnB9biEXp6UFzMjUQZCqrdaeZ44vvuF3v-ZWBVbYf_agkisP8IdFdK54pXmzkJJjnIqJyYIP9Rte-Iss1vNxJlpiE-Bf-XK4uAHSms77Axe1ihgn8TTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برج میلاد میزبان زائران می‌شود
🔹
هم‌زمان با برگزاری مراسم وداع و تشییع رهبر شهید و تعطیلی چهارروزۀ پایتخت، برج میلاد از امروز تعطیل خواهد بود.
🔹
براین اساس تا پایان روز پنج‌شنبه ۱۸ تیرماه امکان بازدید از سازۀ اصلی و طبقات گردشگری برج میلاد فراهم نیست و این مجموعه تنها به ارائۀ خدمات برای زائران اختصاص دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/446096" target="_blank">📅 03:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446095">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d01ae807a2.mp4?token=VcDzUN2q3eOjjqqfvtIywy55UhqQAqOTFwOt402zSPdYNHcIFM88AvgkRGG1LuzghXXmnu7G1z11GEohpr06gB1zTMOW48hVeXYRSc4tJmoAYF7Wpa5Y6TzSkzYiA8hRPkkuPx3DwbUofdKXtxXAF4rLAMUoImJVrtcgIBaRoY0LuS6nkfHHquS7cQcCXQ-HVjR8Az7AvebRNQk_WiuBHCviIm3_maYwbV07Wo0oFC1CeUrmlgJFqyIfb_pVpgZmvAYPiilEht8NGoOKfLn3Diprl7-Ft6Nu75kwWZr8srrDTCsOQdaGrbOahZvA1E_FZ18YBp_8TLIiPbkur6_GgxZq8A9Kc9IvckPEFveb1_3sDnApTTqddqyWrcYp-djFu_YZVLyh-nz5Jz4oXC3XkbdTMT-ymH99nrtGSfHIr_tJUInlqJa2eu1bL1LDzt9k9IR36WxMyHV2vlz-MtMBWp6wZMdZP-djpFgHknUzcsNkh4-P3CA_inJ5W2euy5lSAdAc-Rg1_Z8aZgFCKtFnFSgYBdl8uRJH7wmfRKSrMKYEc7aPCxcSv4DIxCHBaDHci3ac_knoVfGBmKuUrmzyrAzZmMa0w7EdIP2Dwi6Fvs71cwPRQhcLICLfYb7CLYzXcNTbe9sU2DWgFqBWZ45xMXeotEHEny2dzNjacAKo1pY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d01ae807a2.mp4?token=VcDzUN2q3eOjjqqfvtIywy55UhqQAqOTFwOt402zSPdYNHcIFM88AvgkRGG1LuzghXXmnu7G1z11GEohpr06gB1zTMOW48hVeXYRSc4tJmoAYF7Wpa5Y6TzSkzYiA8hRPkkuPx3DwbUofdKXtxXAF4rLAMUoImJVrtcgIBaRoY0LuS6nkfHHquS7cQcCXQ-HVjR8Az7AvebRNQk_WiuBHCviIm3_maYwbV07Wo0oFC1CeUrmlgJFqyIfb_pVpgZmvAYPiilEht8NGoOKfLn3Diprl7-Ft6Nu75kwWZr8srrDTCsOQdaGrbOahZvA1E_FZ18YBp_8TLIiPbkur6_GgxZq8A9Kc9IvckPEFveb1_3sDnApTTqddqyWrcYp-djFu_YZVLyh-nz5Jz4oXC3XkbdTMT-ymH99nrtGSfHIr_tJUInlqJa2eu1bL1LDzt9k9IR36WxMyHV2vlz-MtMBWp6wZMdZP-djpFgHknUzcsNkh4-P3CA_inJ5W2euy5lSAdAc-Rg1_Z8aZgFCKtFnFSgYBdl8uRJH7wmfRKSrMKYEc7aPCxcSv4DIxCHBaDHci3ac_knoVfGBmKuUrmzyrAzZmMa0w7EdIP2Dwi6Fvs71cwPRQhcLICLfYb7CLYzXcNTbe9sU2DWgFqBWZ45xMXeotEHEny2dzNjacAKo1pY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ای روضه‌دار قدیمی
دیدار ما به قیامت
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/446095" target="_blank">📅 03:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446094">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48e889c2ef.mp4?token=gOABR8GIBPkNeqfDK9sTJNZ4NFIvxHfcUEvGWgqMSS7CWI5hsWYLllsIGFcBzFob9mBGZ5nkwycOLFcEm96Fho1EglXfS6Mru-LhLX2u13etNPOUia0rhxlYjQ3BqF3xMTzgjgKYGZ-xgZwAcq2Sm_b2ZAtDennFy09iRM19Fr7-FoNFOsHhoj6S75HM1vzH2Fld_9V_XC7nuAwj0ohptu27BR4xZfpgEX76N6_MhjJ0AhlqEf6LA1Cp1T4Z4w_Edos6jGDpS0W6KUW-LLCSW2cf8KkTsh2-NAwVRUi5A_nBoUIVnN5SQWVW0-qjQj56zbh_Og0xM1uhRQ1iGCGlFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48e889c2ef.mp4?token=gOABR8GIBPkNeqfDK9sTJNZ4NFIvxHfcUEvGWgqMSS7CWI5hsWYLllsIGFcBzFob9mBGZ5nkwycOLFcEm96Fho1EglXfS6Mru-LhLX2u13etNPOUia0rhxlYjQ3BqF3xMTzgjgKYGZ-xgZwAcq2Sm_b2ZAtDennFy09iRM19Fr7-FoNFOsHhoj6S75HM1vzH2Fld_9V_XC7nuAwj0ohptu27BR4xZfpgEX76N6_MhjJ0AhlqEf6LA1Cp1T4Z4w_Edos6jGDpS0W6KUW-LLCSW2cf8KkTsh2-NAwVRUi5A_nBoUIVnN5SQWVW0-qjQj56zbh_Og0xM1uhRQ1iGCGlFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع خبری از حملات رژیم صهیونیستی به شهر صدیقین منطقۀ صور، در جنوب لبنان خبر دادند.   @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/446094" target="_blank">📅 03:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446093">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIedkx84TxUxDjndiIIX-Sb1wiH88s0WvEpIr1kM092vhSke4MFg1umQVXAojYWNYo7Y77KbVjwSgCPoXfncgNN8m0RR0loKHpIpOW_PNhY1VDGMGtKsHrhFbUJmTLl1rN4PYq_J7emUh6fAw26SlKGTqfiYBcH5euQ3FMySbpEncrrQf835CrmRBEwUsLdgE-u2S1H2X2t00ifgPSrSczl7f-K9Ry4yw1vWGaOUNGuQA-rMqc_Iwz9gpY98Mjtzt61Y7_whTKsl3gaMgDIJmdp26BP8YESRKB6GsvTH0xNjU1N3Rx0n7poAJIRByo6FjHW8ZZBXbx1gnHW1JSIcgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پرچم مقدس حرم امام حسین(ع) بر روی پیکر مطهر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/446093" target="_blank">📅 02:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446092">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11549bf726.mp4?token=JAswVRaw6iwbJv43GXHuFoeiBuSu5IT3godSYHzsStBgovnVQGJB2xT4k4qBQLbL4d1b6_Ovhb7sJi-LTIKzteAigcQmvrnp09kecvPtfSC0ErmYmSmlLvQkbu4Ex7SXXvJhCKyNM9mGJgU8y3pHjdnib3UgQUFD9VIDqO_9bFOZj9WB8DHDQOqUFre8NPLZbaZUBybD6hkJr8Jg0rjmZeyI_mxDlezZzCSQv8Mjr4zCbJaUN6EObvjKcLXegp8zcBabaoWeAxqTj0yjiWwjRZXNxiYCYO18OJGbg1jbUde_thMTui3xeRfQLsPL3pgnQ1DUL_OhhfMKc9ETMzX_wmn7ca9MxVO3z93CHqUwVfhyNiJDrdvBcxYKZwQ2Akftsc9GFO31EtWmBaSg9wkrzXekfL9FVGGVpXqtG4dgVkcenD01D6_HYwmfAU123MkczmgWAzCUIEsXEYWx-yyvltmbXHLU_PjrBXGw73ceQ4NVgd2-VTxS8ZH8qd7B3SbetXyMaLk_uHFC-nGQ8mBeHFOzBq-Hq5x_y46GdnxeDOKM4VH6XgoTzDC-9oZZ9icbHOrUCu91XXjSZBDOIIDXr9D_Ii381OzH4oodq0fxdDXkp4IATKY99BFAswDCZXOVPZib4tYFHVrIszLOZqpHpFhalkMwGV9_SAjOYTTLsaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11549bf726.mp4?token=JAswVRaw6iwbJv43GXHuFoeiBuSu5IT3godSYHzsStBgovnVQGJB2xT4k4qBQLbL4d1b6_Ovhb7sJi-LTIKzteAigcQmvrnp09kecvPtfSC0ErmYmSmlLvQkbu4Ex7SXXvJhCKyNM9mGJgU8y3pHjdnib3UgQUFD9VIDqO_9bFOZj9WB8DHDQOqUFre8NPLZbaZUBybD6hkJr8Jg0rjmZeyI_mxDlezZzCSQv8Mjr4zCbJaUN6EObvjKcLXegp8zcBabaoWeAxqTj0yjiWwjRZXNxiYCYO18OJGbg1jbUde_thMTui3xeRfQLsPL3pgnQ1DUL_OhhfMKc9ETMzX_wmn7ca9MxVO3z93CHqUwVfhyNiJDrdvBcxYKZwQ2Akftsc9GFO31EtWmBaSg9wkrzXekfL9FVGGVpXqtG4dgVkcenD01D6_HYwmfAU123MkczmgWAzCUIEsXEYWx-yyvltmbXHLU_PjrBXGw73ceQ4NVgd2-VTxS8ZH8qd7B3SbetXyMaLk_uHFC-nGQ8mBeHFOzBq-Hq5x_y46GdnxeDOKM4VH6XgoTzDC-9oZZ9icbHOrUCu91XXjSZBDOIIDXr9D_Ii381OzH4oodq0fxdDXkp4IATKY99BFAswDCZXOVPZib4tYFHVrIszLOZqpHpFhalkMwGV9_SAjOYTTLsaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دعوتید به دیدار؛ این‌بار برای وداع...
◾️
نماهنگی از ادوار مختلف حضور رهبر شهید انقلاب در مصلی تهران، و اینک دعوت برای وداع با پیکر مطهر آقای ایران
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/446092" target="_blank">📅 02:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446091">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حمل‌ونقل عمومی قم در ایام بدرقۀ رهبر شهید رایگان شد
🔹
شهردار قم: همزمان با برگزاری آیین بدرقۀ رهبر شهید، استفاده از ناوگان اتوبوسرانی شهری در روزهای ۱۵، ۱۶ و ۱۷ تیرماه رایگان خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/446091" target="_blank">📅 02:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446090">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
منابع خبری از حملات رژیم صهیونیستی به شهر صدیقین منطقۀ صور، در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/446090" target="_blank">📅 02:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446089">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05260e76fa.mp4?token=DIVMRYn3YsxHb-I0cgggKoy8b5Aai5jVPUMXM7jQJo17oPTkkHZmqnYfqcxCnkQgXmh7BnNitrvvvduOT3IWeVQ7y-ymyq0CNPJ_z2OnNQ9vq9OhCtj4GySZIxL3bGN4NwO4GIRgIjESWz9KSNhlVg9rYAZG2nTaaByMCCmOr9xlmjoOE8ZOFnx3DKnQWkzsF06G8QHGiU5-An41bsg49IS0xQd44bwi1DI5MP-wT2aP5caXe3EOps7iOufGIoAEZnim_qLx8Wjd_PxnsV5-VDwdzmvrEMWxpE1It5iaBQX3fhJESfZZhQ5oAKrCBCvhSPGxzlRGLLPzKjhezUdsVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05260e76fa.mp4?token=DIVMRYn3YsxHb-I0cgggKoy8b5Aai5jVPUMXM7jQJo17oPTkkHZmqnYfqcxCnkQgXmh7BnNitrvvvduOT3IWeVQ7y-ymyq0CNPJ_z2OnNQ9vq9OhCtj4GySZIxL3bGN4NwO4GIRgIjESWz9KSNhlVg9rYAZG2nTaaByMCCmOr9xlmjoOE8ZOFnx3DKnQWkzsF06G8QHGiU5-An41bsg49IS0xQd44bwi1DI5MP-wT2aP5caXe3EOps7iOufGIoAEZnim_qLx8Wjd_PxnsV5-VDwdzmvrEMWxpE1It5iaBQX3fhJESfZZhQ5oAKrCBCvhSPGxzlRGLLPzKjhezUdsVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید انقلاب: اِنّی سِلم لِمَن سالَمَکُم وَ حَرب لِمَن حارَبَکُم الی الیَومِ القیامَه، یعنی چه؟
🔹
یعنی کارزار میان جبهۀ حسینی و جبهۀ یزیدی تمام نشدنی است.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/446089" target="_blank">📅 02:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446088">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ادعاهای جعلی ترامپ دربارۀ ایران
🔸
ترامپ در مصاحبه با سی‌ان‌ان و شبکۀ ان‌بی‌سی به تکرار ادعاهای جعلی و گمراه‌کنندۀ خود دربارۀ ایران پرداخت.
🔹
او گفت تقابل با ایران جنگ نبوده بلکه عملیاتی برای خلع سلاح هسته‌ای بوده است.
🔹
ترامپ مدعی شد ایران با تمامی خواسته‌های ایالات متحده آمریکا موافقت کرده است
🔹
رئیس‌جمهور آمریکا تلاش برای ایجاد شکاف در داخل ایران و رهبران کنونی کشور را «عقلانی‌تر» توصیف کرد و گفت که آمریکا با آنها موافق است. ترامپ گفت این را می‌توان تغییر حکومت دانست.
🔹
او که به اذعان رسانه‌‌های آمریکایی در هدف خود برای تغییر حکومت ایران ناکام مانده گفت، به دنبال تغییر نظام حاکم نیست و تنها هدف او جلوگیری از دستیابی ایران به سلاح هسته‌ای است.
🔹
همچنین ترامپ مدعی شد که کشورش هفتۀ گذشته سیستم راداری جدید ایران را از کار انداخته و تهران در حال حاضر فاقد شبکۀ راداری است.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/446088" target="_blank">📅 01:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446087">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎥
لحظه ورود پیکر رهبر شهید انقلاب به مراسم وداع در جوار حسینیه امام خمینی(ره)  @Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/446087" target="_blank">📅 01:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446086">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔹
بارون اومده، حاج قاسم برات مهمون اومده، آقا از مقتل غرق خون اومده...
🎥
روضه‌خوانی مهدی رسولی در مراسم وداع با پیکر امام شهید انقلاب در جوار حسینیۀ امام خمینی(ره)  @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/446086" target="_blank">📅 01:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446085">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4084445af.mp4?token=HVl2PmR182hvTbEZF6O65VvwJfj9HSDoOWBlh6uhotZ-5RP6DSIfJ_-oLg1LP0e6YjiP6FcGXLC73pjgXyGC4jt52-8j4NRqVi_Lin4SSDmuT3pK4Brrfbxiscr6Ggr3O5nlXuvSPHnGpEON3p7sLZcNLJKt4DMyiuAqI62wfxfuU473ym8FEhDwd0G7IGu95YEmwBQVuqofLWsJzeoWUNrLfcTdoVFyiZOUdorv5jAr20TQ7ubP9amRnwESG1dqgelvrITymGHt9hopgs96fR-EWTZdHG3RV7bKV-FqFQcO57He7E1GLdDZB1qKYqafMKCn6p2jug2CyHSjYhi5DTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4084445af.mp4?token=HVl2PmR182hvTbEZF6O65VvwJfj9HSDoOWBlh6uhotZ-5RP6DSIfJ_-oLg1LP0e6YjiP6FcGXLC73pjgXyGC4jt52-8j4NRqVi_Lin4SSDmuT3pK4Brrfbxiscr6Ggr3O5nlXuvSPHnGpEON3p7sLZcNLJKt4DMyiuAqI62wfxfuU473ym8FEhDwd0G7IGu95YEmwBQVuqofLWsJzeoWUNrLfcTdoVFyiZOUdorv5jAr20TQ7ubP9amRnwESG1dqgelvrITymGHt9hopgs96fR-EWTZdHG3RV7bKV-FqFQcO57He7E1GLdDZB1qKYqafMKCn6p2jug2CyHSjYhi5DTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
او به آرزوی خودش رسید
◾️
تعابیر رهبر شهید انقلاب در مورد شهید حاج قاسم سلیمانی که حالا در مورد شهید سیدعلی خامنه‌ای هم صدق می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/446085" target="_blank">📅 01:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446084">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔹
بارون اومده، حاج قاسم برات مهمون اومده، آقا از مقتل غرق خون اومده...
🎥
روضه‌خوانی مهدی رسولی در مراسم وداع با پیکر امام شهید انقلاب در جوار حسینیۀ امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/446084" target="_blank">📅 01:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446083">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">هتل‌های تهران هفته آینده نیم‌بها می‌شوند
🔹
جامعه هتل‌داران تهران: تمامی هتل‌ها و مراکز اقامتی استان از جمعه تا پایان سه‌شنبه با تخفیف ۵۰ درصدی، برای اسکان زائران و شرکت‌کنندگان در مراسم تشییع آماده خدمات‌رسانی هستند. @Farsna - Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/446083" target="_blank">📅 00:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446082">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfcRMLfQQO2EG6Vl7cg8lLcVN_Np0QRQKiidhR6Ril2nGeW9W_n-ol9c56RZXtn-I_gYEmAcys8ixv3BsCoIGzaar_JMDlPjyvbf1D_RtaUeHkPxoZmGb_-wlEvQyjTT6TSrHFUccVoFcGBYN-hX60JPgnqQ_6Qrq2YFTBQizGPD0zEV7WFSw0ekLEImndC4zCRG3wOpkaFxzBa_8XCQFilE8AAxYgLslr4ySjARAKtRlvDKrIRJGLllxrteD06G1s5j61FJmSf2n0MGai9fu5bzjYaCoe2hlsQ6fny8MB9FWD4jy-c_xnWyiSEAsg8rx028cUMOOHGnadSAq2JoEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمازجمعۀ تهران، امروز به امامت آیت‌الله سید احمد خاتمی در دانشگاه تهران برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/446082" target="_blank">📅 00:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446081">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‌  خبرگزاری رسمی سوریه: شمار قربانیان انفجار دمشق به ۴ کشته و ۱۰ زخمی رسید
🔹
شبکه الاخباریه سوریه: انفجار در کافه‌ نزدیک کاخ دادگستری در دمشق، ناشی از یک وسیله انفجاری بوده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/446081" target="_blank">📅 00:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446080">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
حملۀ اسرائیل به چادرهای آوارگان در جنوب غزه
🔹
المیادین: در‌پی بمباران چادر آوارگان در شهر خان‌یونس در جنوب نوار غزه، حداقل ۳ نفر شهید و زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/446080" target="_blank">📅 00:35 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/txYmQHHOu6jWbRhCp_AArcEg3lx8ScC8N7OsG_63nb_iwSVY1rDFcBqgB-7WW03NRRQ2CdVdQU0R95jwLCibiDr-PrQGKvA1PbK_sxzWOWcU54SJWSoMHaYRg6fjtmk_MYHbTOQ6LEPzvdOSq36Qo8mvrasTKjnx4ts62ydqV0FlzFAAgV8BTF3nQ5dY8oRl_zdAFrya3b94iEfulHWcZJD5x264H0B2Q88Yq4MNIrnhx8yibWqVUhijvJYT1ku3JH3XLzfjmuvoD17yjiZCmfbAI5crK6FizqKa6ppGu82v82rwV4cEL0N1ydGZLtHd5nDe3Owpvy9k3WlaEN2IJw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 01:43:18</div>
<hr>

<div class="tg-post" id="msg-445950">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‌
🔴
برگزاری مذاکرات فنی غیرمستقیم ایران و آمریکا در دوحه
🔹
رویترز: گفت‌وگوهای فنی ایران و آمریکا به‌صورت غیرمستقیم در دوحه در حال برگزاری است و در این میان، قطر و پاکستان نقش میانجی را ایفا می‌کنند.
🔹
نمایندگان اصلیِ ترامپ در مذاکرات با ایران، یعنی کوشنر و…</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/farsna/445950" target="_blank">📅 01:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445949">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🎥
دلنوشته‌های مردم در «کشوردوست» تبدیل به نماهنگ شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/farsna/445949" target="_blank">📅 01:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445948">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrniQv1lwJXmk0fqooJjC6p4FVSMH4MHwiOSxqaIATUmQLZEKEwwI9TwJREli6NyAKCH3u5RPsOqgX-UqyQ38G89IbtX8cq_mpK4DoCfJvUJQrSMy7eR-x3dNPCBDEMk3FmVc4YZXAJKbo4mjAWqs8NByUewHBdCyEqGg_dnU2eJVxlX-VeT_q_2wNG0IMiB6U6PBabIuMniFGAUb7pSE8b2J6hAX2V2a410GnrNJpTxj1ZD94PrIS5gzO29TUEwLTRkAap1lKfKI7Tp7V-JVVXGx2l1VArj5sHmil27Mm0UNIgf4c1PA2mZyKB7Z8kxk5XaYmqYP_1lbCprdb2xnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشایی محور هراز پس از ریزش سنگ
🔹
مدیریت بحران مازندران: محدودۀ پنجاب در مسیر شمال به جنوب محور هراز که شامگاه چهارشنبه به‌دلیل ریزش سنگ ‌و به‌منظور حفظ ایمنی مسافران مسدود شده بود، بازگشایی و تردد در آن به حالت عادی بازگشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/farsna/445948" target="_blank">📅 01:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445945">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd491fc278.mp4?token=VUmSYXJVUDCPeWIsk3fbPvUQGNv45J4hGAWJxtfirNI_8HzBvBPTum_HwQny6KJXAxJB1N55nMEmzcv1FP6S5hbqV6mV7CyO7iDhOUPI3jvxhf3Hoq1R6SlX6UJZmTpyFxXXTpP1hvbnSeqOiWoBikccGOkHxVeiiKoltUBHySWq85Fezzh5k8-lfxrIaYcw6BQhLX0e1tKF5r_bfM_u2qb95C_4yMVdsP4a8lC_SNDu7-nxXajbjDVOQXLVX3mdgWpqg4-IgRWpbY9ksK3g6jwJKxV4VD-HEaqoI7z7iEvCc2rYil6N1j5M8jar4syrzbno7kcb3a0g68cw6Q-w6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd491fc278.mp4?token=VUmSYXJVUDCPeWIsk3fbPvUQGNv45J4hGAWJxtfirNI_8HzBvBPTum_HwQny6KJXAxJB1N55nMEmzcv1FP6S5hbqV6mV7CyO7iDhOUPI3jvxhf3Hoq1R6SlX6UJZmTpyFxXXTpP1hvbnSeqOiWoBikccGOkHxVeiiKoltUBHySWq85Fezzh5k8-lfxrIaYcw6BQhLX0e1tKF5r_bfM_u2qb95C_4yMVdsP4a8lC_SNDu7-nxXajbjDVOQXLVX3mdgWpqg4-IgRWpbY9ksK3g6jwJKxV4VD-HEaqoI7z7iEvCc2rYil6N1j5M8jar4syrzbno7kcb3a0g68cw6Q-w6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عراقی از وقوع چندین انفجار در یکی از مقرهای گروهک‌های ضدایرانی در اربیل عراق، پس از حملۀ موشکی و پهپادی خبر دادند. @Farsna</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/farsna/445945" target="_blank">📅 01:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445944">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/718ee7abd4.mp4?token=kWvOPEpk5ElF8M9V1AECTfmhk1aCXEVr-j8I7d2B0TNjiX3aH5JQ94qLW1LjfsIBrqKJX4XHMz3n94bay_ABk0A2fQhpTajctyQzkE9rkPUhfNIYiMzcTSavywWFv6oy58bZupfZP58Ypl67QJwuGdTmZH-tlf3YiruJkToyKMf4XdXKecgK_9UsRDOPrLm-NA-O3SFSVDQR3ZKmzEb433dgya2NKPJMF2NDxWOVRNoVKC7lXq3gYCKyidqVFD-EifnmMM4pig_bJJguoRksHRHFqfP_ds5TwYrfrUkJD8exiMzRBrW7SRJNfY2tFKmlnBFUFY_qymhuLs5zlTZrcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/718ee7abd4.mp4?token=kWvOPEpk5ElF8M9V1AECTfmhk1aCXEVr-j8I7d2B0TNjiX3aH5JQ94qLW1LjfsIBrqKJX4XHMz3n94bay_ABk0A2fQhpTajctyQzkE9rkPUhfNIYiMzcTSavywWFv6oy58bZupfZP58Ypl67QJwuGdTmZH-tlf3YiruJkToyKMf4XdXKecgK_9UsRDOPrLm-NA-O3SFSVDQR3ZKmzEb433dgya2NKPJMF2NDxWOVRNoVKC7lXq3gYCKyidqVFD-EifnmMM4pig_bJJguoRksHRHFqfP_ds5TwYrfrUkJD8exiMzRBrW7SRJNfY2tFKmlnBFUFY_qymhuLs5zlTZrcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عراقی از وقوع چندین انفجار در یکی از مقرهای گروهک‌های ضدایرانی در اربیل عراق، پس از حملۀ موشکی و پهپادی خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/farsna/445944" target="_blank">📅 00:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445941">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PyM5VwoYIJ-4RABAJD_xsG8YMOIfZag5LM9LePt1AaBFRQO6aucQAWPidPjMLgfs0VY2CV0wxX661PPMo15be7kvBwrUQSHIUCdFhJwLZ3l8jUFgYsFf2aNS2X0rt3JISdm9jdkA-M0lz7nTXMA-_sNHdhVgbKuiEWMAVBomaROCv3Qy5XiaImvdt7iS9Flvgu1-LljRI97AhjKgxPWkVBrWSWuMKQQtUcClcF2zMdkmUnxin0B8TqfoYtS4gzP3fycyK0U8bx35BVZFC1elMQdxMWqZgDdaRrZ4FpTym3rkfIGYQNPBNHck3cipHYJDQLywZ8aWKsKwNv5f7QeAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QnfokLda0HtCETJrMCVhfNPUgR4mpZZDRuR4r1VDhEh-eqFVnNuMGsDPq9RQCGdvAhDdZOz5SXNDDnp_nsCNtDaeWFqRJWA3VGs2S5lqZEjA8yiUOmVPlOB7A-IxU9kr6Wh8Wn2Qg-p1B-l6q21EStw0hdZqLqkc840ZCS0mlPAYVZCYnsl09nOYpuyWTwjLQIysnMKf35P6zfqefTAzRnBlF4PTuBYB9L3ZMLsklZ2uTkZIWCW65Twk-lniyLKePrpP9UlE5X1DES5qsx87JvjmuV2-skHl0jktEX5wlbXtJjt7fSLxX0G_DLkJbEWboM-hRoOjmzOodvwtQO2ToQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUU0SyoafYp6rBA9dyktfxuSnGGP3UQczjVj99lR8qmGlZ2QkPWPfOayLAHrCk8kFT8iPN94vatuT5VD-6HT3xK-ZVr0uxu1YZxdYQYtCIeTcGWS2VhsX1-Q24XJVXKE2dlin5kc9FBwOb2-gjuKPRN8HrOblLabiEw9EYScTtHIGNpntHZBwBDxQtFOUeuU3CryeSo4zd9SjWWq1iRP1MzEWy_xS2cS-sixHYYRzkqRF4IokI6fIUpC6J9kn3me39YH-3gRd-RaASDPilLtQtONDSgVBLlJSo5bvlQZhlaKvhAONkqVu1uxKvtliMqvXrURcMdvdF4vheUUEP57ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۱۱ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/445941" target="_blank">📅 00:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445931">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ldaXFx3l3frLFWQhgntFF2LKnPAkoaeuA_eui9rIynjG6NBGZW2hSF63-y6_i98tVhzKGRWhnfZ-Rb5H40_b9EeHz-_3wTdOdrLi4iFMYRCUF-Zo38zpjYqpUyreZBfk9DXHbxECSpAqF9y0mIgye5s0qJKx-7QCoLB6uDWPvqdkc8UXlKYjVmf7wonL7MawSrExslxcK6KrmfD0lw1Yj9MFAgNSPH-CukYhV6rGL0kYSlLW6rW7XMImZsoyTr_zaDcGKEgNUrTH5RhdMUz5ZahlEpTrpjvAHY8_qyGDXb-_bOoFT465Hatk2OxXVUa1WGtZDCP_PbLQPy4rX36lag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lKMaH2fQzGocoCBR9SVpyIOAi_bh2zZza8on8DOKCtxJHuqWLaBe4BG02Y2-93fGEhQyEZ_fNsKldX9cC5SV-N5QqVtWywip-5d09ZHX-bsIcNvhyp_riDlPehfWH445bNqw2qMMKPEby66AVryFiWouAd_2_W8iktCfBBRyPflz26kYRQwItEDny0koUhubhSUiqZr_DloPKD-vwhCCz3SmCU3xQ-32ZoI9Oo0YFNDAagAs2SwKBS5qKeGOXljZv5Sc5nKZKKvJmzb_sG9X_KP28p0shMk17VJ-mauKMdgjToNMZtI8CoPxwhB5_MIpuO3bjZjgX5F8CxR5E_Mg9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/baNMu9wI5MC5oKHuDiYfNxr8mUCm6by_AKWmVwsitxAaU4H4w9i2O9q7J78WSS4nJsHS46cYwvcEZekIzVkkep1JlUM-3EYxYCeL_lLUGWbxJ0JckjJqS1YeFsEWtNivJW1FNoyytY3tzKfRtoURKrtvNA7k4OeyxAxxBgRE6zw5exfLMq75bz4uyDPT0XY9ONE7Hpi1L0Y33W6Tj5Zh1XkApa06BNZuiQgcnn2CP5N6sw1sRz6e70HG5_F3M5dJeQMZqa8gCqI_c1-NpHghHcgPa8WG388B_3qrJ8NN9D0wAIE6PJg2meZh6meH9Y3nLggBeAJvfR46C3cDqYNqdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qEiuR4XRQ8713XBAd56l9d1FWkxeq58DQBFp4Q3ugKe3-pgWRD7fh48IlOoNnZtHvaUMwm--WcnpxDNfG2WgDSElh3eu5klURSqr5KE-FlGNa6WrMJRfUZKO2VqLEEqwSnwigPeN4NTJPO5nMsr8S8eKyr2E5NRfF4EtgHfHzXbcVAitVfPSNs2zuXSdbrx7BQYgVIp8GvVP5bE22L9UU4gpUcQKV5FxVfTmAACGgJYSj7GXpUoiC9xHJbHSTxXmPFNfdgNSGlTwxMcRcHUDELDFOF_F9aBzLTxrw3aB20WxxoiO1x5bRqXFgXEtKiN3OlCyOycjxBBuWYIUo8SLiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d4Rba6zTtg_xlTVBIgbUyfYcwAIXtFaePTqUoHGeXo-5dB5fOqlMtaDoe_OD1AmNMYAOtI5y1ejj089EWMs3eWsyjUldTqXW_KoX9hVmR9JyqCInpqwkzJyb65vL5BjlseYYZBNSXT5wc3x9U_Gmq1vnxLNU8m_JHWGpZbN7ZiJ7QdBDlWY6OXjta4I9k3u6fUEwMuMt50TDDlASJf9e_42eOv_GpSf5EiNe4v54PNITbs-UKzim-kFcbvEgh0yx7JueanFSpXywciF6d82USHfHdCQY5Nnkd-ME3mcEzR-uLa1WX9vMvAePzofSojf3993wPktxJGKctvWA-s5BUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pGETAaVtlLwdCJ9Fb2r2PKd5v8o45B79eVivmBGgZVXzK1cGvuruhWrbuujezOWi5DtkevlswoEOYj07zJeV7m0pwrIKNCn-uXebfPZHF8aOmP9aRz0IXb60v7hwEzFuO4pMm2grvc_T0E0LDtnu6KokMJaq8pZQeAIShZvoC7QYFleuD2p3OvKyvj8DZPCoXZ4uT_04efwwUPC8E6TbKa4mczPyD1OJZ0s2gR9wN_TA0II3k82V3CZmC3ouA67wJQAFtfQdC9phnMQIQ7Lsc8gNmkmSGzNwtwhQ_c-WU4e3fzYQYedso9C7IEFinISV8BNCEcrs1uG1cmVIHHRcMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ugy9CHeRMwhswj8wdorT0pyTNmpq_9ckN8N5x3Ex0k0DjlPLinvE_0-nfkT1otp8HW-hSY39VspuPSVoqDaJO7a6vjYtr7IG8QIYYrTS8iZ9jnqf1_7HFTFJg7xL4tcQv6Ik8eDQ8qPzNExjAQX-FHx6cbU1GpxZb_TLwNIzIBPKR5EAIQEnTlPi-rbIdu_ce7cFDuR6IlNTtC3syFIC8lHexuMi9YqquVetKPTe_YYwYFnNmSvxgLkNMANCGFBXXus_1JwDtaUOsFmjI2KVGkLufWASN_OqEnujbga2GNovqtyZMlwBCQ4VKR3maVNa_QqSUtHngEDQ7w2Q8MTQXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A_PCZwOc5dsS_3BKOdz5kY-vh_LJANnYVs0DxAzu8CqWpHHX_dbRlbpxuZINAf_kBl4ZuAef13t98svRshccSVMLOdOlzdjzGzuxITqJNmUxbDN7A3sibIL-M9uKbia20uL9lPW9Xcm8ZSJHZhYMLYGtsE7QL2-5aSQQyiEEMGH35B5U7KsXpo4B9t6a9EUeLBc5iznxBkSN8XWvT1E96UtTLIKWkkFVN6S0awhgf75DpATyUhj1iZhMVs9tny_W-pN73IqeeNHAMsnWFyEKxiU63ZUFngSishbYTygoFyBeS8WeK22I35F38WebfdlKdFxiJcMDr-1M9OCiXYr4RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JVR1Iq0a3eFoGGc0ZRQLmUoqu7rfNfVer4GNgM_uFwAbLxu639KdniOz29__vKhtVru19kEeq8QNZy8NZZx2selXVBesl7u0cDm6DJ2pAWE9lF4nklLlYWZ1TqMhmLwfdxqcGAjfVu_K_63m4eUK0Y7_anldWArCJeNgmG8x236htXczuwzbdZXlIGioc6H8lBIdDtC_raqkWt7CKo3aNI3zEOoLpYPS-CiHOZzlrczrJ2sckJjACxIzQW8l38CurD88wIYprcHlb9weJAtWyHlq7wUgzBzxEAOmdndeciv3EiWoiYHDkBwPG6LvAPY1lUQdZpej4cRmWS8NyM-W4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sX3PC3qKj9dVBjU7DrHpEwl8YbcvML7KI4g8aPxz4YBajMZhLiZO_r-n25ymyuTmJgDhVQMRLvrzeVnQDsXkGlnqy96TyCTsZR0xEcTi9KDjFpTLNFUoaodamh4vng8Xy0VGB7_3JcH1b2fQHm__FEtmWQINlnQnq6GLVQyrQSs7G_YKYQYwJO6n7Gt13WCzLw6jchzUEkFTAtnxT-8UJDJ_TEbKB0s2lWVQLIbLs6zWyelxchjLc8DH_DvuvarCjmvYkZXbNujLxczzSXkK7kTiueIyA42gLX7d4jNyo73gh5kTFfrjtlagWDp4LBp1tVJA2gYA3k9JtVZSnE2Xmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/farsna/445931" target="_blank">📅 00:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445930">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhPPMu2U4GXIW2PRox4KCIEhTRCLGMo0luxXftBaikF9SWQqbVkEMgvecxgjV-jxI7aJRhmk9gXYYDnlKcQ-crTPNWe9Q1g9U9FBZPUqu4D5MepYhB-Zvcz7qfvO0MNh8qzgabUGcT9_6wqVCFCINfiXBxVzG7wwe7umk-RJDeRgEQCugaO_C1YDZ8cvTmFMQxzTityRwBKROWrTWHQN19b8in0qyAh7zhYDUQnEpzmpvgBE33MzeUFo-aC5rN65llF3ZMZQyDlXY8Q5jd1hNwofKmx_b0jx6JqWrLlOf_Inf9g0IMqZ3JKetiWALJQaOadZZxjc2M4p2B9beB4rGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اهدای اراضی فلسطینی برای ساخت سفارت آمریکا به قیمت ۱ دلار
🔹
رژیم صهیونیستی و آمریکا توافقنامه‌ای را امضا کردند تا سفارت آمریکا در قدس اشغالی ساخته شود.
🔹
به گفتۀ سفیر آمریکا در اراضی اشغالی، قرارداد اجارهٔ این زمین برای ۹۹ سال است و ایالات متحده مبلغ ۱ دلار را به اسرائیل پرداخت خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/445930" target="_blank">📅 00:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445929">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lb8gATv_jxk7qB2qcqjvzTbFM_P7AKFgVE-fszocRk-hG4Z_ES_ycDHKTYW14qhegFg29hHS8yJL3ElaTEPqiCoUFGlZhSN2sY9BEovPs445v7HUHKKMTWQBnHMJmpUI2Ju8k7dkg4z9ncCQVlv_5G5sOvxDRSLYaB1lChUC8VKWIPKFu2rvscljK0Vb7A_qU99Y7DxRVK8lI9spn8CzJ8EaNwrmfArb2nVGLcDH6yyQA7gtHS8Cz6x_wySUMlcPncWzPC9kp9OBM_Qn6Xdy1TpS5MBspVj5G_3lVnop5dYIna0xW6jMUXUP1vMjmtrwIcmMI8tpi3va-gjbB2zm1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفرهٔ شراب
🔹
«منصور دوانیقی» خلیفه عباسی سفره اطعام بزرگی پهن کرد و بزرگان، اشراف و شخصیت‌های برجسته مدینه و جهان اسلام، از جمله امام صادق(ع) را به این مهمانی دعوت کرد.
🔹
امام صادق(ع) بر سر سفره نشسته بودند که یکی از حاضران درخواست آب کرد. اما خدمتکار به‌جای آب، ظرفی از شراب را آورد و به آن مرد داد.
🔹
به‌محض اینکه ظرف شراب در سفره قرار گرفت، امام صادق(ع) بدون هیچ‌گونه درنگ یا ترس از ابهت حکومت خلیفه، بلافاصله از سر سفره بلند شدند و مجلس را ترک کردند.
🔹
هرچه منصور و دیگران اصرار کردند که ایشان بمانند، امام قبول نکردند و در پاسخ به این رفتار فرمودند: رسول خدا(ص) فرموده‌اند: ملعون است و از رحمت خدا دور، کسی که بر سر سفره‌ای بنشیند که در آن شراب نوشیده می‌شود.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/445929" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445928">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f205d4e95.mp4?token=A9sdx8W5pCf3a0c0lv6Y2sFsEHpUahqdd2HtRbrla9wGLtJOIVwG-cgCtzBM9Vzf2H5Q_SH0TrEgM0GbsIG7MGkkh6NVbQSA6GBftXS7s0lfI-NkI_BI7eG19PRz974SakNxehdreybebCAJX0_LdGSlffnVUyUCgMd3YYDCLk1nRpRJ5iICSSOIR-VSpXz4xCmBTb_s56Lu87nLOG66SOORII_yk9jYy_0e8HsIZcrwPidls193LNia7_XSrfju5ea2dYK3nk1EvRHk08hKeZHANzIv2_MKNUVFY9zVFg4laX_ZH0H6XQU9pCtRokPKpZMbjQoWqjW6X67xE3mxNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f205d4e95.mp4?token=A9sdx8W5pCf3a0c0lv6Y2sFsEHpUahqdd2HtRbrla9wGLtJOIVwG-cgCtzBM9Vzf2H5Q_SH0TrEgM0GbsIG7MGkkh6NVbQSA6GBftXS7s0lfI-NkI_BI7eG19PRz974SakNxehdreybebCAJX0_LdGSlffnVUyUCgMd3YYDCLk1nRpRJ5iICSSOIR-VSpXz4xCmBTb_s56Lu87nLOG66SOORII_yk9jYy_0e8HsIZcrwPidls193LNia7_XSrfju5ea2dYK3nk1EvRHk08hKeZHANzIv2_MKNUVFY9zVFg4laX_ZH0H6XQU9pCtRokPKpZMbjQoWqjW6X67xE3mxNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری برای رهبر شهید در اجتماع مردم نیشابور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/445928" target="_blank">📅 00:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445926">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fc0b27d69.mp4?token=LQwIcQ40n_vC2UdGxBciA1vY38E-MDR9MWVcCeAZlMWCalo-uHjAB9yRfxJ4UkMMCgK51xYlo9pFJysBbUL25bZ206pkhmPw0XRJl_NLAFLdvbmQ_oE7LEJyzvvtAruqYgVMttHbSjMdTMPkXWDaTgfQXeUpsJN82cpGLo59_o80e-RRHnpy117_tgileNoDqpPQaBBDHQV_p3In_GfX6pQQXi8Uo_EUNkNDC2u31K1Io4Fj5rUssLsk1DGYWbr9EVIA1rrUN4mLiyiSykueJRTI4PuJZkJH0vo6UyHJl7G0e4DmGvWKAHVpn08VU-GdrxiH3NmK14cq22U7tr4vag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fc0b27d69.mp4?token=LQwIcQ40n_vC2UdGxBciA1vY38E-MDR9MWVcCeAZlMWCalo-uHjAB9yRfxJ4UkMMCgK51xYlo9pFJysBbUL25bZ206pkhmPw0XRJl_NLAFLdvbmQ_oE7LEJyzvvtAruqYgVMttHbSjMdTMPkXWDaTgfQXeUpsJN82cpGLo59_o80e-RRHnpy117_tgileNoDqpPQaBBDHQV_p3In_GfX6pQQXi8Uo_EUNkNDC2u31K1Io4Fj5rUssLsk1DGYWbr9EVIA1rrUN4mLiyiSykueJRTI4PuJZkJH0vo6UyHJl7G0e4DmGvWKAHVpn08VU-GdrxiH3NmK14cq22U7tr4vag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چادرملو برنده شد اما ممکن است گل‌گهر به آسیا برود!
🔹
ممبینی، دبیرکل فدراسیون فوتبال: از AFC درخواست تمدید مهلت معرفی نماینده را کرده‌ایم اما درصورت موافقت نکردن کنفدراسیون، نماینده ایران بر اساس جدول لیگ معرفی خواهد شد که گل‌گهر خواهد بود. @Farsna - Link</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farsna/445926" target="_blank">📅 23:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445925">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🎥
امشب طوفان گردوخاک هم مانع از نمایش غیرت میبدی‌ها نشد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/445925" target="_blank">📅 23:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445924">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12e8562b1c.mp4?token=AULUbs9K4miWh55XRxWH2pZcRKTB3DjcTy8hZOW9BXONUaBbvqKmwJzpNcGmnVALWUc4MOjwxYB4xznFmVdXU6Uz7WmKcV_ytjnZ63tWz-QeD-qf9nlRai463xj0X-FlK-t9MxY6SY2e2CCsFkr_m3vRfBQ7VigmF7LeP-wUMZZdz0-vxAGOyX2O_duRLA7x1KGizmmuLa0PBJ_C3I2oxxgs0L_48Knni3rU70H4w4R-dtcFXC0zvriD1qfTHP2bztpXv-RHQpJ2CeGxRwiwBfVJkJxBde2iL_m1Q77GtN8-DfTIHnqYByQ1I9Sff8puSWQgbMyAjQ_lQ5lcQ9aq2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12e8562b1c.mp4?token=AULUbs9K4miWh55XRxWH2pZcRKTB3DjcTy8hZOW9BXONUaBbvqKmwJzpNcGmnVALWUc4MOjwxYB4xznFmVdXU6Uz7WmKcV_ytjnZ63tWz-QeD-qf9nlRai463xj0X-FlK-t9MxY6SY2e2CCsFkr_m3vRfBQ7VigmF7LeP-wUMZZdz0-vxAGOyX2O_duRLA7x1KGizmmuLa0PBJ_C3I2oxxgs0L_48Knni3rU70H4w4R-dtcFXC0zvriD1qfTHP2bztpXv-RHQpJ2CeGxRwiwBfVJkJxBde2iL_m1Q77GtN8-DfTIHnqYByQ1I9Sff8puSWQgbMyAjQ_lQ5lcQ9aq2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بغض سحر امامی هنگام سخن‌گفتن از تشییع رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/445924" target="_blank">📅 23:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445923">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08336dba01.mp4?token=BD8YBiKVWaufTETLyBeNGhuVc4BOzPHG52mwW0vGyNWGpVJr8IcpiV_cBFgCLlXgoUBhoBMF0gBWHhMScd5oGee2MIBr-2ptXLfbDofy3yqClTtqL1aXixQzpxkKB9tMsc19mdc_ERpQp_KKrGIHO5h5O_up2OfrSWwwVaHn4gksbVE145xk1flGZ7UUUr95jEvVG6W4lRtlPdUMrc_LydWqUYS4SKHlGMohzMz9eRhIvPBwhXeX8C4m63TaaLzgHCDvYCTehCO8gV8vQOnLoORAoklzNTuZc7JvVMqqM8l0HD4DCz-ig7-Hrki_5rQy3rk9dgXwq73_v3a7rUULCYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08336dba01.mp4?token=BD8YBiKVWaufTETLyBeNGhuVc4BOzPHG52mwW0vGyNWGpVJr8IcpiV_cBFgCLlXgoUBhoBMF0gBWHhMScd5oGee2MIBr-2ptXLfbDofy3yqClTtqL1aXixQzpxkKB9tMsc19mdc_ERpQp_KKrGIHO5h5O_up2OfrSWwwVaHn4gksbVE145xk1flGZ7UUUr95jEvVG6W4lRtlPdUMrc_LydWqUYS4SKHlGMohzMz9eRhIvPBwhXeX8C4m63TaaLzgHCDvYCTehCO8gV8vQOnLoORAoklzNTuZc7JvVMqqM8l0HD4DCz-ig7-Hrki_5rQy3rk9dgXwq73_v3a7rUULCYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همدانی‌ها بازهم تا پاسی از شب در خیابان‌ها برای دفاع از ایران حاضر هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/445923" target="_blank">📅 23:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445922">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZ2LlairVBF0HG-GH4F48WAEciTFDbt_n51EUpgroT0Cv6cRpI0Y9tXLa59BZeaOkQF75ipZ3aL9Q8DtoioZ0r2XWj8-DYLvaS7DwUFlhUtf2bh9FOE07NaG-iU9pzbcz4upROo1mw0_j_j7hfZk7Kb27XMwDgi_bFYoLSrKLBoBxBi3gDd8lm3HxBdLafqR_e4sTlJLBgHLea-33SYJex7FxkKxcYuXNWB-x6HBX4jKbCX3w_NvXGkyQqeGqLBw90AnzMZgih9EWd-nTs_r4d99ow4GKMbB3bV87Lz5uro2gBiLruHIUhrOpd5MDBwK2f4v-KYFpGD7rU3CR3Q6nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحرکات مشکوک اسرائیل در شاخ آفریقا
🔹
شبکه المیادین گزارش داده که اسرائیل محموله‌ای مشکوک به وزن هزار کیلوگرم را به سومالی ارسال کرده است.
🔹
المیادین به نقل از منابع آگاه خود افزود که اطلاعات موجود حاکی از آن است که این محموله شامل سامانه ارتباطی پیشرفته و مدرن با کاربردهای اطلاعاتی ـ نظامی بوده است.
🔸
رژیم صهیونیستی و منطقه جدایی‌طلب «سومالی‌لند» حدود ۲ هفته پیش رسما افتتاح سفارت این منطقه در قدس اشغالی را اعلام کردند.
🔸
الحوثی، رهبر انصارالله یمن هم یک هفته پیش گفت
که یمن در قبال هرگونه حضور و استقرار احتمالی صهیونیست‌ها در سومالی‌لند که در فاصلۀ اندکی از خاک یمن دارد، دست روی دست نخواهد گذاشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farsna/445922" target="_blank">📅 23:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445920">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jk-Iq0U6QhHkBJNunM0v2nYSIGExwXJDQVhH421Q5KTW-u4cvEnESCn4kBstu3ED43ufQcKytvKj-vtc7SfKtdN0e6uet9dpGDVOpW2tZ9qlnb_0M806p3LOKRrYr9atOzjs2ER2IWd-7piWNyGj4qe_9HMVYrNcR8cFXUzEhhV77q1SkVKidu5UMkOjGaIw8arSr7IppYacBu91ht3CtANUNiqhXGXdPv8gU4ZYvQ965Y_SHoc06NRUG1pn9X3B5eUNZ1-5UPMalZtcaYjh9XUmok6sZltyj-RDT35RT2k-rB6ajQb-t900oAALNeNPYsxaSsjCmo-w8vUtSbpw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصرار دولتمردان لبنانی به تداوم مذاکرات سازشکارانه با اسرائیل
🔹
نواف سلام،  نخست‌وزیر لبنان گفته لبنان همچنان به‌دنبال  یک چارچوب توجیهی و مقدماتی برای مذاکرات است که مسیر گفت‌وگوها را مشخص می‌کند و هدف آن رسیدن به یک توافق نهایی است.
🔹
نخست‌وزیر لبنان اظهار داشت که اگر «چارچوب» اجرایی شود، منجر به عقب‌نشینی اسرائیل از مناطق اشغالی و بازگشت اهالی آواره شده به روستاها و خانه‌هایشان خواهد شد.
🔸
این سخنان نخست‌وزیر لبنان درحالی است که سران رژیم صهیونیستی از جمله نتانیاهو و کاتز در روزهای گذشته چندین‌بار به صراحت اعلام کردند که از منطقه امنیتی در جنوب لبنان به هیچ عنوان عقب‌نشینی نخواهند کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/445920" target="_blank">📅 23:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445919">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ef7922d9.mp4?token=lDvTrGoqMpKJtj6-hrALaHBB-lRHaFBB1aQnz2igw_FqPhzM6fkZ4_v56l1WOkCnnTE_TsGda3tVnzzK8QUr3-3cXI3OCsB9B6g64pqE-bYdW2TxdqlihwYfvXvnKw0VhjZ8gIgidbttg0EkJecEq_XgJvwZM-2nbijHUjPjU_U1JVnOg-tLMfzGJKGbpkDBQK4SP6xyPGRQGZeSnhS8K1Ix-7U4mNnKQleTw8SOxBHBDcjVoeZRWCrp8ZLTGMormNUKTVitE8Bf0jhIWIh6VVUMlxVCxgPGxVfObJ9x4Nol1Tok38i9mmHvc1kXLG7ERAxGET4eXeas70CXxFupgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ef7922d9.mp4?token=lDvTrGoqMpKJtj6-hrALaHBB-lRHaFBB1aQnz2igw_FqPhzM6fkZ4_v56l1WOkCnnTE_TsGda3tVnzzK8QUr3-3cXI3OCsB9B6g64pqE-bYdW2TxdqlihwYfvXvnKw0VhjZ8gIgidbttg0EkJecEq_XgJvwZM-2nbijHUjPjU_U1JVnOg-tLMfzGJKGbpkDBQK4SP6xyPGRQGZeSnhS8K1Ix-7U4mNnKQleTw8SOxBHBDcjVoeZRWCrp8ZLTGMormNUKTVitE8Bf0jhIWIh6VVUMlxVCxgPGxVfObJ9x4Nol1Tok38i9mmHvc1kXLG7ERAxGET4eXeas70CXxFupgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: کانال پاناما و سوئز باید برای ما رایگان شود
🔹
رئیس‌جمهور آمریکا در اظهار نظر جنجالی دیگری گفت: کشتی‌های نظامی و تجاری آمریکایی باید اجازۀ عبور رایگان از کانال‌های پاناما و سوئز را داشته باشند.
🔹
ترامپ افزود: از روبیو خواستم فوراً دستور عبور رایگان کشتی‌های…</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/445919" target="_blank">📅 23:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445918">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jka_cwTwM5Ji6fnwae-SGWHIXDV0ByeBR1vI6cIfFzpCd5zf-al4EvHOt912u4UDfSfGgdKUSSl4AZjPZGUJyz17dapCxFsR3_I_FbM8rKELt0uEdeUxFRbRrUn5OQMamfRPUgyWdNgjemfpW-RhgJGdnPMMajGzTG-yd7NAWw9XLgMd8qNk_i6OCZcXpSY925yiMfJtTeb0vrlF_kI-rsWqEVJ9x5EonSdJ4IGT_ODDKGoR1lJ2nleautzBupNBgP7nlST4Puzbq9LoIrj5uD0Y8k8elPnKXrkcKBWzsHCUSlkf8_RF7iB1XfgY31iJupL76Cfecz5UIrUj0GNVwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان انحصار دبی در تجارت خارجی ایران فرا رسید
🔹
جنگ اخیر و اختلال در تجارت دریایی، یک واقعیت مهم را دوباره یادآوری کرد که اقتصاد ایران نباید به یک مسیر و یک کشور وابسته بماند.
🔹
پل‌مه، دبیر انجمن کشتیرانی، دراین‌باره می‌گوید با کاهش تنش‌ها و بازگشت ترددهای دریایی، مسیرهای تجاری بین ایران و امارات دوباره به راه افتاده اما ایران نباید مانند گذشته تمام ظرفیت تجاری خود را در این کشور متمرکز کند.
🔹
او می‌گوید توقف کامل تجارت از مسیر امارات به دلیل مشکلاتی که برای فعالیت‌های اقتصادی جنوب کشور ایجاد می‌کند، امکان‌پذیر نیست اما می‌توان با توافقاتی با سایر همسایگان مثل پاکستان، عمان و عراق وابستگی تجاری ایران به امارات را کاهش داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/445918" target="_blank">📅 23:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445917">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bb1c38d9.mp4?token=HsqdVe-S9JFQ_VSboYdg8xBFzPmqQpmulz0IqhSo3tc-zMi_DWuD46CFlN3Tk2muUcA8ArO5K80eWyNPde--JUxJyzz_HOKnBxOMlbu3RMqHhfAlp8100l_av_1o8i4WIqoFpySXSnoZSxQKQpHQvi-pxnD85s99A19y4tF12uSirxHDWOl-xmp6dY38hdK3eczSKZVQHLK-5yunI3qp2sfKRdhiunly1cs13ZtFVqWZzCG94VdxQiWqhOgCcb0H_3R5r-8aj-DSavJ5TPEveGWrZ3RozRH4_DJ7WzPDfpAqDwF9bO4z_PZgALn-HM3ea266wK60-YsP1vx328lOMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bb1c38d9.mp4?token=HsqdVe-S9JFQ_VSboYdg8xBFzPmqQpmulz0IqhSo3tc-zMi_DWuD46CFlN3Tk2muUcA8ArO5K80eWyNPde--JUxJyzz_HOKnBxOMlbu3RMqHhfAlp8100l_av_1o8i4WIqoFpySXSnoZSxQKQpHQvi-pxnD85s99A19y4tF12uSirxHDWOl-xmp6dY38hdK3eczSKZVQHLK-5yunI3qp2sfKRdhiunly1cs13ZtFVqWZzCG94VdxQiWqhOgCcb0H_3R5r-8aj-DSavJ5TPEveGWrZ3RozRH4_DJ7WzPDfpAqDwF9bO4z_PZgALn-HM3ea266wK60-YsP1vx328lOMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: بحث دسترسی بازرسان آژانس به سایت‌های بمباران‌شده کذب است
🔹
ما هیچ امتیازی بیشتر از دسترسی‌هایی که شورای‌عالی امنیت ملی تعیین کرده، نمی‌دهیم.
🔹
طبق قانون، تعیین سطح دسترسی‌ها بر عهده شورای‌عالی امنیت ملی است و آن هم چارچوب آن را مشخص کرده است.
🔹
در…</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/445917" target="_blank">📅 23:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445916">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eca2186e4.mp4?token=JNA1AX7cMKOjl2-rUhigv7-g2x5cIa_OWbkgYEWVMavG8KJ2cImyGxuAz6XQ4dkh-12U_I_hvfGPDaJXriuzCvy_DMN9mXljTkIkj9oZ3QeFRDunxdgzngYN5MgLM3fkJH3AvWstiH0-Y1ilK8lXaX4lLxYWHGdsioWViYspa5-Dk9LvBRDpdesD756UlpYD4ONuTqrqHZ_xjKSa3JAqPnthjb4axxIVJoZw-AC8Wa2mqFXGyUMv5rNGF1IKq545w-IxTVq2-jtJQKE-jhXKpG-Nz8I6M8AA4xuCkGPixZwxNNlNp8nYv5V-KdntSDGPOgQTrEdEwmKYBH9KvLLWRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eca2186e4.mp4?token=JNA1AX7cMKOjl2-rUhigv7-g2x5cIa_OWbkgYEWVMavG8KJ2cImyGxuAz6XQ4dkh-12U_I_hvfGPDaJXriuzCvy_DMN9mXljTkIkj9oZ3QeFRDunxdgzngYN5MgLM3fkJH3AvWstiH0-Y1ilK8lXaX4lLxYWHGdsioWViYspa5-Dk9LvBRDpdesD756UlpYD4ONuTqrqHZ_xjKSa3JAqPnthjb4axxIVJoZw-AC8Wa2mqFXGyUMv5rNGF1IKq545w-IxTVq2-jtJQKE-jhXKpG-Nz8I6M8AA4xuCkGPixZwxNNlNp8nYv5V-KdntSDGPOgQTrEdEwmKYBH9KvLLWRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: هیچ خیمه‌ای جز خیمه ولایت، خیمه امیرالمؤمنین نیست
🔹
من وظیفه دارم برای همه مردم ایران که با هر سلیقه و دین در سایه جمهوری اسلامی زندگی می‌کنند، نوکری کنم. @Farsna</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/445916" target="_blank">📅 23:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445915">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c046bb7d.mp4?token=r-lrs4kp88MDTibTJQ2q8d0Daki_nCZNf6a9SpeilYSzXDztKAGkIS1Ate5c_VDawZ0Noa25jPLphIt1ofMeTM1OhaXFnz86z_z7YDDtH9B0eaM1Yfp7OZ1uwoFOzEY5ebiRKLtwxLti3yiItCbVPpCw9BgPqPly9VFEjhfY1k2Z121c5O7_XEEIVtJ5HXZMO3GLChvCB0ZJMcwyJC2On66LC2JN5_ZAr4lVakV8se10ZDv6g9M7SQ8YWEduB-cVgf_eHNvLwm-ezUuBoZ42RT2ANqu4s2halxdk2V7K-zSw0HooFhEUVlV79gYVex4gmKTmoph1LPR1GRvJF4Y5Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c046bb7d.mp4?token=r-lrs4kp88MDTibTJQ2q8d0Daki_nCZNf6a9SpeilYSzXDztKAGkIS1Ate5c_VDawZ0Noa25jPLphIt1ofMeTM1OhaXFnz86z_z7YDDtH9B0eaM1Yfp7OZ1uwoFOzEY5ebiRKLtwxLti3yiItCbVPpCw9BgPqPly9VFEjhfY1k2Z121c5O7_XEEIVtJ5HXZMO3GLChvCB0ZJMcwyJC2On66LC2JN5_ZAr4lVakV8se10ZDv6g9M7SQ8YWEduB-cVgf_eHNvLwm-ezUuBoZ42RT2ANqu4s2halxdk2V7K-zSw0HooFhEUVlV79gYVex4gmKTmoph1LPR1GRvJF4Y5Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: کسانی هستند که نه در دیپلماسی به کشور کمک می‌کنند و نه در جنگ اما من ایستاده‌ام تا هم بجنگم و هم دیپلماسی را انجام دهم
🔹
بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید و اجازه دهید مردم آرامش داشته باشند و به جمهوری اسلامی افتخار کنند.…</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/445915" target="_blank">📅 23:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445914">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1f29024f8.mp4?token=ROSV7UBAdufspBKTZfmo0CPEHHlI55zGZV-lxBW62yN6m952dcEo5OnItRZqT_lBb6CN1kklgiA1Wg_JsfL4zp6kFcBGu6Sb0WxVNB0R0-SLNzw6FbYcfBDLt5_9pmmdTyBrXJttbwpCcS4gbPr6rbsxwiowoa4-yAS9b93-poLmu4eNbaq0wjH_znzGmXP5R7S6eZcBHgaMp9rj_8D-LX5wKG2DdQQ_J8FXluk_RiaJPLXroJhoqUBZKBftBo0q34F8LIEz8Mgb8E6NEUfHyKP3rlStB2rCmAnTOzHQCH-4FxRUlGj_xngCZto3mOKSmuG1sU77dJFCrDk537fXDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1f29024f8.mp4?token=ROSV7UBAdufspBKTZfmo0CPEHHlI55zGZV-lxBW62yN6m952dcEo5OnItRZqT_lBb6CN1kklgiA1Wg_JsfL4zp6kFcBGu6Sb0WxVNB0R0-SLNzw6FbYcfBDLt5_9pmmdTyBrXJttbwpCcS4gbPr6rbsxwiowoa4-yAS9b93-poLmu4eNbaq0wjH_znzGmXP5R7S6eZcBHgaMp9rj_8D-LX5wKG2DdQQ_J8FXluk_RiaJPLXroJhoqUBZKBftBo0q34F8LIEz8Mgb8E6NEUfHyKP3rlStB2rCmAnTOzHQCH-4FxRUlGj_xngCZto3mOKSmuG1sU77dJFCrDk537fXDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: ۶ میلیارد دلار ما در قطر بود و ۶ میلیارد دلار بعدی را آن‌ها تقبل کردند
🔹
می‌گویند چرا سوئیس رفتید؟ خب من رفتم آن‌جا اوفک را ونس امضا کرد تا پول‌ها آزاد شود‌. @Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/445914" target="_blank">📅 22:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445913">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
آستان قدس رضوی: در خصوص موضوع محل تدفین پیکر قائد شهید، آستان تمامی تمهیدات لازم را اندیشیده و پس از تصمیم‌گیری نهایی توسط بیت شریف ایشان، جزئیات آن به استحضار ملت عزیزمان خواهد رسید.‌
@Farsna</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/445913" target="_blank">📅 22:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445912">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12cfc8a569.mp4?token=I0i02cdwZTd4iNlK8lTRI5lxBbQbquyl_ulThgps6wUytLHjVdCbfpGvVZXOLB-pkbxs4FaLj1aiu17mKn7-aNdIlJIqhFWsNx0hbYRNuBc0X6vqEq-0BlpYZMjjui5B-faqNIOubJNyLbAOxayI4NZt55kLQF__Xj-bPIhissveUN5xeF5JjQgjKXYPa2Aod6Qhtgpyg-Wz0vDPNitIVSpYubnAmjGPjir-PONaq0wvedLC-ZU8OdGTeBPwjH-vQoUTvWm4CrlJ48fEXKxuf7Wlk5ITp2vOd_LBVAkLKjEqmxIYKH_RVWbNXztHei1AYGmMkttfqmxbKpM5Jii8Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12cfc8a569.mp4?token=I0i02cdwZTd4iNlK8lTRI5lxBbQbquyl_ulThgps6wUytLHjVdCbfpGvVZXOLB-pkbxs4FaLj1aiu17mKn7-aNdIlJIqhFWsNx0hbYRNuBc0X6vqEq-0BlpYZMjjui5B-faqNIOubJNyLbAOxayI4NZt55kLQF__Xj-bPIhissveUN5xeF5JjQgjKXYPa2Aod6Qhtgpyg-Wz0vDPNitIVSpYubnAmjGPjir-PONaq0wvedLC-ZU8OdGTeBPwjH-vQoUTvWm4CrlJ48fEXKxuf7Wlk5ITp2vOd_LBVAkLKjEqmxIYKH_RVWbNXztHei1AYGmMkttfqmxbKpM5Jii8Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری: رئیس‌جمهور آمریکا گفته پول‌های بلوکه‌شده صرفاً برای خرید غلات آمریکایی آزاد می‌شود. این چقدر صحت دارد؟
🔸
قالیباف: واقعاً هیچ. @Farsna</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/445912" target="_blank">📅 22:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445911">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47669c456.mp4?token=VpaibmwPrb5K108to4oTZaCaWZJHwO3qo4G01bbHrTBb82iJXDhCNpcW1CwG0GbS3uPXsJOUJOpbwdW3U9abpAnXHZN0TVDUF3deMiE5X7zolr-gZMuz_f4iDstzg9dowS_FAaceXKevoYAPHpah4fW50WwshWwFaZws4yczfjGwi022EA_2Yi-3fYAI12Jokb2GUjXBraz_0vWvi8is2fwxXcrhhGduo9CJxiQe5jCZyNugpOgZr7EhcAflUqyNVu3rKm346xD35KKOxB24yIaBoOfhPEWQd5qMNiMBNBOcTrsJ3Jut0vQE_3U94rI3e6mrxzdwVjfMsCYe5x-Iaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47669c456.mp4?token=VpaibmwPrb5K108to4oTZaCaWZJHwO3qo4G01bbHrTBb82iJXDhCNpcW1CwG0GbS3uPXsJOUJOpbwdW3U9abpAnXHZN0TVDUF3deMiE5X7zolr-gZMuz_f4iDstzg9dowS_FAaceXKevoYAPHpah4fW50WwshWwFaZws4yczfjGwi022EA_2Yi-3fYAI12Jokb2GUjXBraz_0vWvi8is2fwxXcrhhGduo9CJxiQe5jCZyNugpOgZr7EhcAflUqyNVu3rKm346xD35KKOxB24yIaBoOfhPEWQd5qMNiMBNBOcTrsJ3Jut0vQE_3U94rI3e6mrxzdwVjfMsCYe5x-Iaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری بروجردی‌ها برای رهبر شهید در شب ۱۲۳ حماسه مردمی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/445911" target="_blank">📅 22:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445910">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c07d1174f.mp4?token=mgMu2I-AoYJTIhcvHQEnh18oqpNx-BdwOWbZLruuqErqLQUVwjQjF_UTYyTx8mV6Uq5NRA_7UC58GzVW-6fVfX__1TuxAC95JsqjOrEf5wstOcUdC6oIbY6y8MLJIVd1m3tSqt6Gmi8PnpV1k3x1P8uv8F9BC33xakGQ72Lv2WJbQwS4u0E7iLEy-o4VAHn0dTajAIy14O0YKUlcJZPbDY07FfXA2itFtyikn7RrLoLB_RFRe_OD-dPE3DISg2iURYjO-DTFWU7cr5MCKTXEYLCiwV7uG5dbpWeWLWnfFr2Bhu8vTqm5ULiO34WnaoqGQOYqIIBT2OU-24UOODtDRQ_3QScfC1QMUL7n8wxnXETsDZOt9hdxOcECwS9Q81I6Hy2NEunlqS6Kvnx0msHHD4cubSf8H98Q0wnFabksGUVHYRYNnff3pFq27a9Ja8UDKGW0V9SApBumFI0UDqJjwZxTLWi7vUx9MD1bUgUP8zKwaumS9QSHJgGreZCJvy73SC9KgwX3dTbdtdfdBhb6iJk4ThtABqY2WX9z_IMellog21nZdpstF5ALdcRkrrTXkyyvQ4ar3ZZtPT88D7Zw-w8LU3x0Iio-sFJnghBmhswIQ9NVrJwjX-DTfMR39yCu52eSynL5NfnVH64RfV1hWyGoYoxLzh0-7XtvadLm0Hc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c07d1174f.mp4?token=mgMu2I-AoYJTIhcvHQEnh18oqpNx-BdwOWbZLruuqErqLQUVwjQjF_UTYyTx8mV6Uq5NRA_7UC58GzVW-6fVfX__1TuxAC95JsqjOrEf5wstOcUdC6oIbY6y8MLJIVd1m3tSqt6Gmi8PnpV1k3x1P8uv8F9BC33xakGQ72Lv2WJbQwS4u0E7iLEy-o4VAHn0dTajAIy14O0YKUlcJZPbDY07FfXA2itFtyikn7RrLoLB_RFRe_OD-dPE3DISg2iURYjO-DTFWU7cr5MCKTXEYLCiwV7uG5dbpWeWLWnfFr2Bhu8vTqm5ULiO34WnaoqGQOYqIIBT2OU-24UOODtDRQ_3QScfC1QMUL7n8wxnXETsDZOt9hdxOcECwS9Q81I6Hy2NEunlqS6Kvnx0msHHD4cubSf8H98Q0wnFabksGUVHYRYNnff3pFq27a9Ja8UDKGW0V9SApBumFI0UDqJjwZxTLWi7vUx9MD1bUgUP8zKwaumS9QSHJgGreZCJvy73SC9KgwX3dTbdtdfdBhb6iJk4ThtABqY2WX9z_IMellog21nZdpstF5ALdcRkrrTXkyyvQ4ar3ZZtPT88D7Zw-w8LU3x0Iio-sFJnghBmhswIQ9NVrJwjX-DTfMR39yCu52eSynL5NfnVH64RfV1hWyGoYoxLzh0-7XtvadLm0Hc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین پیام از طرف مردم به آقای شهید ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/445910" target="_blank">📅 22:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445909">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🎥
نماهنگی به زبان کردی که اهالی کردستان عراق به رهبر شهید انقلاب تقدیم کردند
@Farsna</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/445909" target="_blank">📅 22:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445908">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">📷
بازگشت بازیکنان تیم ملی به کشور  عکس: محمدمهدی دهقانی @Farsna</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/445908" target="_blank">📅 22:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445907">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62044a23ee.mp4?token=gdOV9Iaq8uAg9vNJogJm8w2Nv_Q8irRyNNFNIvGeoi8OVwvt0o4TvB4NQHbaY0YhZ6s_M3hUIils-lXl4jlxWGgbSNVT3w8XMfh7FJpcZ-o8nNiw-aJmcRrWZsLgPXHhgnAazqoTFqMfgjE-bhE5blyyoZCQw2I9sptX6Wi5ngb0BLlZ0ng9kUCxT7A_dktbXZYwigkvFd4qo_-QtRIIWs-MO32_rfUedq5cULwCWY4p7rcwmF5ZNMe_6RmQQ-riEtydAnKewgKev4OdtePyRX5J04K6tlCrxiCZbfkUabx1gMs8PZx_vKESX-scwEKhu2G0JtndwxAlgwEemG1peg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62044a23ee.mp4?token=gdOV9Iaq8uAg9vNJogJm8w2Nv_Q8irRyNNFNIvGeoi8OVwvt0o4TvB4NQHbaY0YhZ6s_M3hUIils-lXl4jlxWGgbSNVT3w8XMfh7FJpcZ-o8nNiw-aJmcRrWZsLgPXHhgnAazqoTFqMfgjE-bhE5blyyoZCQw2I9sptX6Wi5ngb0BLlZ0ng9kUCxT7A_dktbXZYwigkvFd4qo_-QtRIIWs-MO32_rfUedq5cULwCWY4p7rcwmF5ZNMe_6RmQQ-riEtydAnKewgKev4OdtePyRX5J04K6tlCrxiCZbfkUabx1gMs8PZx_vKESX-scwEKhu2G0JtndwxAlgwEemG1peg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر ستاد اسکان شهرداری تهران در برنامه پرچمدار: در تمام بوستان‌های تهران برای اسکان زائران مراسم تشییع رهبر شهید، امکانات مهیا می‌شود
🔹
هلال‌احمر قرار است در فضاهای باز شهر تهران مثل پارک‌ها، برای ۲ میلیون نفر چادر بزند.
@Farsna</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/445907" target="_blank">📅 22:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445906">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41f76872e4.mp4?token=Fnwgn3nYqddkcTw_17nQ6eQIxYiXAj1aftx9njUnVRqiFO-N2rCdicORlyor6dljNF4R5lO5E54mhngJShA6x02LT6xega_lk5GzDyArmAGXuHOMcf7DZjlYBll1JFwumYbDnwK9puwkimVbW8bCHWng7L7xm6z1WTvvzHLF8wg8qAVx9cpcmMMIhOWG2KwR4MGXh0vrt2Xep9efByIoCWTQT_o_E8C4UZj84yqPtES3Bk6sKcZLCqtSp7SyeFLillbO9TswmD3sLCPxd1dSgAD7rHzC7MWlBFHg4f2Dejx09N-aLYoFZ6LC5TF9700ZUIxVLblRCNCyqc685PyL2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41f76872e4.mp4?token=Fnwgn3nYqddkcTw_17nQ6eQIxYiXAj1aftx9njUnVRqiFO-N2rCdicORlyor6dljNF4R5lO5E54mhngJShA6x02LT6xega_lk5GzDyArmAGXuHOMcf7DZjlYBll1JFwumYbDnwK9puwkimVbW8bCHWng7L7xm6z1WTvvzHLF8wg8qAVx9cpcmMMIhOWG2KwR4MGXh0vrt2Xep9efByIoCWTQT_o_E8C4UZj84yqPtES3Bk6sKcZLCqtSp7SyeFLillbO9TswmD3sLCPxd1dSgAD7rHzC7MWlBFHg4f2Dejx09N-aLYoFZ6LC5TF9700ZUIxVLblRCNCyqc685PyL2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توصیه‌های ضروری برای حضور سالمندان، کودکان، مادران باردار و بیماران خاص در مراسم تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/445906" target="_blank">📅 22:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445905">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0709561f.mp4?token=h6CrIu8GITkuMFAv8jqbtmgL7eE5Er0dby_qu7ndGBnV9K7ox-xnT1fhFak-a_G_vAguukrlljGdQG5VlaGVf1PqlnX7RhWKYnJPOwE2FPKUwNGhD8mrEc358T3rR8UieENsZgZiqljOerJXrR84hGsfuAV2RTpnmYpw4EMZGTh3-oc4eAm9KvEQ9yIfJISxtsSjtfQlF6Q4419bDmkHmoVHBPm4IIcsdB6fXIIlHhlyK7F5BtUSAoihwPBDCyXDn-95qSz1yFlPYVCnAF8xymTZIVgDk27zUyidS-33WJSdnsNkF3hUWQ4loktjhaDNbOFpOGAlnjdvT1tPMfVAag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0709561f.mp4?token=h6CrIu8GITkuMFAv8jqbtmgL7eE5Er0dby_qu7ndGBnV9K7ox-xnT1fhFak-a_G_vAguukrlljGdQG5VlaGVf1PqlnX7RhWKYnJPOwE2FPKUwNGhD8mrEc358T3rR8UieENsZgZiqljOerJXrR84hGsfuAV2RTpnmYpw4EMZGTh3-oc4eAm9KvEQ9yIfJISxtsSjtfQlF6Q4419bDmkHmoVHBPm4IIcsdB6fXIIlHhlyK7F5BtUSAoihwPBDCyXDn-95qSz1yFlPYVCnAF8xymTZIVgDk27zUyidS-33WJSdnsNkF3hUWQ4loktjhaDNbOFpOGAlnjdvT1tPMfVAag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماجرای قطع مصاحبۀ قالیباف در شبکۀ خبر
🔹
مصاحبۀ محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در گفت‌وگوی ویژۀ خبری صداوسیما پیش از پایان کامل سخنان او متوقف شد.
🔹
هم‌زمان، کانال رسمی آقای قالیباف نیز با انتشار پیامی از قطع شدن این گفت‌وگو خبر داد. این موضوع واکنش‌ها…</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/445905" target="_blank">📅 22:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445904">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🎥
خداحافظ ای مه‍ربان رهبرم
@Farsna</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/445904" target="_blank">📅 22:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445903">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5fd9f0fa9.mp4?token=FzCZPUZ5y2QofnPVTxxVRxIzWQ7w5znikGWb4jIyejlr5UaYKBNrAz5yjVB-C5FCzsjBMBHZmIdVrNgm2RhkWkU5OwWM0tfUXz3Rtk5vzG-a7ugXkyKjnPMKzUZ7fPwi8r-74TI_qLay2fz0BJUxA5Iel4b5SisZYsROnQa_P6Kt0KRLtaXx50adlIZpJeAJytNDDagefgWLPxq5Usd5R82zQjFpSlpQl3b_6V74PtSfpQHvnpWqWVgvb-94qDtsXT0pAE9h3oI-Y--3lYNJ0L0GcJo1tk66cbDIUWjNL1-cLuZPEMGavciO8u2PkoqmWaREDztZIYbvbNrXNoPkEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5fd9f0fa9.mp4?token=FzCZPUZ5y2QofnPVTxxVRxIzWQ7w5znikGWb4jIyejlr5UaYKBNrAz5yjVB-C5FCzsjBMBHZmIdVrNgm2RhkWkU5OwWM0tfUXz3Rtk5vzG-a7ugXkyKjnPMKzUZ7fPwi8r-74TI_qLay2fz0BJUxA5Iel4b5SisZYsROnQa_P6Kt0KRLtaXx50adlIZpJeAJytNDDagefgWLPxq5Usd5R82zQjFpSlpQl3b_6V74PtSfpQHvnpWqWVgvb-94qDtsXT0pAE9h3oI-Y--3lYNJ0L0GcJo1tk66cbDIUWjNL1-cLuZPEMGavciO8u2PkoqmWaREDztZIYbvbNrXNoPkEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید انقلاب: همهٔ شما فرزندان من هستید، به معنای واقعی کلمه دعایتان می‌کنم.
@Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/445903" target="_blank">📅 21:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445902">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2128c0af77.mp4?token=tuNQqWmlD3HHfWtLJrnD-ep4QAiDDIY3i0f6O-5I38bKfYPCIQ7rnkGk-plb-EbROo94fFuGsJlTwqIeI69bwrl07A_js8H4MB6lGoBdq1OP6_zHMRS0PKpSBs7lbqfWTserTNRXltWX2O1lb2L_zkhbsHhZkEwCcx0VEfA2nuYoBd6XGzVeWBImRc8MKBVhJ5aWs0WZ8Pll3Ku-t-3bjgIqFWTuEGq-ziFpuLYtL1ZTkIHoBZ2WaJU0M7cSzosloLk3_Yo-V_Z0E4tL8FAEGlVzElWlrOdNr2mg0xpU8yH_w87y5eoIfK1nNMmDlQehRNESWVdXpPv0tuYh2iQ1nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2128c0af77.mp4?token=tuNQqWmlD3HHfWtLJrnD-ep4QAiDDIY3i0f6O-5I38bKfYPCIQ7rnkGk-plb-EbROo94fFuGsJlTwqIeI69bwrl07A_js8H4MB6lGoBdq1OP6_zHMRS0PKpSBs7lbqfWTserTNRXltWX2O1lb2L_zkhbsHhZkEwCcx0VEfA2nuYoBd6XGzVeWBImRc8MKBVhJ5aWs0WZ8Pll3Ku-t-3bjgIqFWTuEGq-ziFpuLYtL1ZTkIHoBZ2WaJU0M7cSzosloLk3_Yo-V_Z0E4tL8FAEGlVzElWlrOdNr2mg0xpU8yH_w87y5eoIfK1nNMmDlQehRNESWVdXpPv0tuYh2iQ1nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما همان ملت مبعوثیم که خیابان‌ها را عرصه رزمایش اراده‌ها کرده‌ایم
@Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/445902" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445901">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‌  پزشکیان: باور من نسبت به جایگاه رهبری مبتنی بر عقل و اعتقاد است
🔹
باور من نسبت به جایگاه رهبری صرفاً یک باور احساسی یا تعبدی نیست، بلکه مبتنی بر درک و اعتقاد علمی و عقلانی است. در طول سال‌هایی که در مسئولیت‌های مختلف حضور داشته‌ام، همواره از هدایت‌ها، حمایت‌ها…</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/445901" target="_blank">📅 21:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445900">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پزشکیان: اگر رهبری دستور می‌دادند مذاکره نشود قطعاً اطاعت می‌کردیم
🔹
در جریان تصمیم‌گیری برای مذاکرات رهبری عالی‌قدر فرمودند که اگر سه‌چهارم اعضای شورای عالی امنیت ملی رای مثبت دادند همین روند را در پیش بگیرید که در جلسه‌ای که برگزار شد از ۱۳ نفر، ۱۲ نفر صرفاً…</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/445900" target="_blank">📅 21:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445899">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پزشکیان: اگر رهبری دستور می‌دادند مذاکره نشود قطعاً اطاعت می‌کردیم
🔹
در جریان تصمیم‌گیری برای مذاکرات رهبری عالی‌قدر فرمودند که اگر سه‌چهارم اعضای شورای عالی امنیت ملی رای مثبت دادند همین روند را در پیش بگیرید که در جلسه‌ای که برگزار شد از ۱۳ نفر، ۱۲ نفر صرفاً رای مثبت ندادند بلکه بحث و تبادل نظر کردند و قاطعانه حمایت کردند.
🔹
امروز عده‌ای دولت را متهم می‌کنند که شما از نظر رهبری اطاعت نکرده‌اید، درحالیکه قطعاً اگر ایشان دستور می‌دادند جلسه و مذاکره‌ای صورت نگیرد، نه جلسه می‌گذاشتیم و نه مذاکره‌ای صورت می‌گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/445899" target="_blank">📅 21:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445898">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f146f4f970.mp4?token=dqRQS-qzf_bQTRQkMjHH6LTdzObVDA_6v0HiFkCHjNq_AIOkgUm2SP1HE6Pdu5CdStM6ka7njJUrdWu_UDPgA56XnS4z4ZC_XI6rnaBKL54jKtQO4wkBlA6-mwz65JW5wPRSs4ogEZuPBxfIJplE1scRkgQlij5VylSnxUQV3UrmRxziTDxtoOHS1Ui7k79SrKRGG2z3w4JO6OfH4i75ddJYEqBKP9Z-zw8gBn_rUAi6iWnAeTZRvcEQdLgqH-x8KzCwpFu5jDJSd2h8VPyuGFhiev-ksM9S_zO3gG_ibzZRhLHBuCJ9jHnKHfU-kVJam4suWV-RJYt3pv0ev3vjSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f146f4f970.mp4?token=dqRQS-qzf_bQTRQkMjHH6LTdzObVDA_6v0HiFkCHjNq_AIOkgUm2SP1HE6Pdu5CdStM6ka7njJUrdWu_UDPgA56XnS4z4ZC_XI6rnaBKL54jKtQO4wkBlA6-mwz65JW5wPRSs4ogEZuPBxfIJplE1scRkgQlij5VylSnxUQV3UrmRxziTDxtoOHS1Ui7k79SrKRGG2z3w4JO6OfH4i75ddJYEqBKP9Z-zw8gBn_rUAi6iWnAeTZRvcEQdLgqH-x8KzCwpFu5jDJSd2h8VPyuGFhiev-ksM9S_zO3gG_ibzZRhLHBuCJ9jHnKHfU-kVJam4suWV-RJYt3pv0ev3vjSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌و‌هوای حزن‌انگیز یاسوج در آستانۀ وداعی تاریخی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/445898" target="_blank">📅 21:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445897">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پزشکیان: دفاع از نیروهای مسلح وظیفهٔ من است و با تمام توان از آنان حمایت خواهم کرد
🔹
برخی مطرح کردند که چرا اعلام شده ۲۰ میلیون بشکه نفت در اختیار فلان مجموعه قرار گرفته و این موضوع را افشای اطلاعات داخلی دانستند.
🔹
بنده معتقدم اگر بار دیگر نیز چنین شرایطی پیش بیاید، نه ۲۰ میلیون بشکه، بلکه ۱۰۰ میلیون بشکه هم در اختیار آنان قرار خواهم داد و به این حمایت افتخار می‌کنم.
@Farsna</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/445897" target="_blank">📅 21:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445896">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رهبر انقلاب درگذشت پدر دبیر شورای‌عالی امنیت ملی را تسلیت گفتند
🔹
متن پیام رهبر انقلاب اسلامی به این شرح است:
بسم الله الرّحمن الرّحیم
🔹
برادر گرامی جناب آقای دکتر محمدباقر ذوالقدر حفظه‌الله‌وایّده؛ سلام علیکم و رحمه‌الله و برکاته
🔹
خبر رحلت والد معظّم حضرتعالی واصل شد. بدین‌وسیله مراتب تسلیت خود را تقدیم می‌نمایم. امیدوارم آن‌جناب در سایه‌ی پرمهر صاحبان این ایّام صلوات الله و سلامه علیهم اجمعین مورد رحمت واسعه الهیه واقع گردند.
🔹
همچنین آرزوی سلامتی و طول عمر با مزید توفیقات ظاهری و باطنی برای جنابعالی و سایر بازماندگان دارم.
سیدمجتبی خامنه‌ای
@Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/445896" target="_blank">📅 21:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445895">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b7ee6ef08.mp4?token=ebcP81mXqujiB7BduktPaZNOZFaE_w_XI0uczmAXqhxGUC0dn7l-7OGwX3t_Nq8TCS1fiPMyFcx_ysSbIY7UfTy3jCCbjv1XvnOx6avB6aHbhl1Z6oLF1vRSXUquCOpWktXvafYLKzHYTtJg2idYBTN8qLJq8_vjBh3U7HNnMY74hCCkxR26aqOGY_-TO-ojQbE4EY2XjwPBExqyrw5D58sNheUkNknL3OmnHUg1VjTEe9U71KY2yATKgJjfdggTGd8FPa3p7yumtSoTPpHd4ZcApmpLikAaDQVX_w6jGnFnWsws2kdSgRSQwCwhiMb2C4ECjGbAtvedjIVRv0xxIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b7ee6ef08.mp4?token=ebcP81mXqujiB7BduktPaZNOZFaE_w_XI0uczmAXqhxGUC0dn7l-7OGwX3t_Nq8TCS1fiPMyFcx_ysSbIY7UfTy3jCCbjv1XvnOx6avB6aHbhl1Z6oLF1vRSXUquCOpWktXvafYLKzHYTtJg2idYBTN8qLJq8_vjBh3U7HNnMY74hCCkxR26aqOGY_-TO-ojQbE4EY2XjwPBExqyrw5D58sNheUkNknL3OmnHUg1VjTEe9U71KY2yATKgJjfdggTGd8FPa3p7yumtSoTPpHd4ZcApmpLikAaDQVX_w6jGnFnWsws2kdSgRSQwCwhiMb2C4ECjGbAtvedjIVRv0xxIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش زدن مزارع و خانه‌های مردم لبنان در دو شهرک بیت‌یاحون و حدّاثا به دست صهیونیست‌ها
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/445895" target="_blank">📅 21:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445894">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ba789f78.mp4?token=bSnJFGpACuC2mH09EEgnB00DaBXh4Q6lmeoAtBaQvvghFd2nPBkv5tcYaLvGEwTyuiFIP87UtrF2QFqjrnMB9yUCFXtCf73cHho1zOVHqf9dhHPlTtp8vaOKLhAfj9asR6dsfw48sP1rQhf8jUrFfBIZiQK9os6lRJXSBKB5M6aiK_u5v9nG8oV7FfF4Dz7JyerQrWN9PbAoR8Ur7Pnzm7F-0LL6JjNsVBJC_ykxv01HTRcnA8pamxuSN1Ge738utxzzrTRbvfs6jt4V8aONwjMzHJXQjwxoU4ZOlNPMw3mMfeCCs21AgXQU7Mf8T8nbJnWrACqyvkaDh5CFEqdeew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ba789f78.mp4?token=bSnJFGpACuC2mH09EEgnB00DaBXh4Q6lmeoAtBaQvvghFd2nPBkv5tcYaLvGEwTyuiFIP87UtrF2QFqjrnMB9yUCFXtCf73cHho1zOVHqf9dhHPlTtp8vaOKLhAfj9asR6dsfw48sP1rQhf8jUrFfBIZiQK9os6lRJXSBKB5M6aiK_u5v9nG8oV7FfF4Dz7JyerQrWN9PbAoR8Ur7Pnzm7F-0LL6JjNsVBJC_ykxv01HTRcnA8pamxuSN1Ge738utxzzrTRbvfs6jt4V8aONwjMzHJXQjwxoU4ZOlNPMw3mMfeCCs21AgXQU7Mf8T8nbJnWrACqyvkaDh5CFEqdeew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قفل دروازۀ کنگو بالاخره باز شد
🔹
گل اول انگلیس به کنگو توسط هری‌کین.
⚽️
انگلیس ۱ - ۱ کنگو @Farsna</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/445894" target="_blank">📅 21:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445893">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎥
از دفاع از فردوسی تا مجسمه والرین
🔹
رهبر شهید چگونه بزرگ‌ترین مدافع هویت و فرهنگ ایرانی بود؟
@Farsna</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/445893" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445892">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a246913bf1.mp4?token=XOmE05aML4mM4mfiaeQSEjyNPECK5tUsbXPtw25lOX1_kFdkI90kpLFn8qY7apHYAozCHEkrmNMYxfksZG5KLDDPQzkxEjdVgNGhLDv14G7w2CbZ8exwj57yTMt7S4rqZmJGhIe2_74BXB_TnTQX5DePtEYY2RNPxUfzvyWeFZbNe5Sh0xBDzzrKNVeKjBXjiLl1_Zrxpffei2DO7LThKp3vUm0PU9QSHh0vKJ-p0jpSOh9jIcLRx1CpiIrb9_vsBKJG0FNWgmn90B5yBZV2yO1slVqL0sW13MF88h1WpHgy9OWFpx4LawUJextK8vxnakAd7t75ld4tgTqwThK_6q0oAoWP51_wVRJteOCzyCaEman_BLtmlkAQIPhreuFqw8MNqXZZVevK_fJYO0o-x3p7Ki2gSJcg0_bZvCWDCjEk_evjNTqinab7b4RPM98jdNtB_UwbjlrD9ScRxEd6Ny1pXaB5XZoRxidl0A9hvykIIBWKMFdnymlE_N1fqrdeZLeqB2tnnUMfVaCaM8xWHRTnnDdIuYfvppD0kfEGnh3rZHrpPzqbjVIHHHk-Qh4iTsQjjIgUxHi9DtD1nJ5L_fQpr8QnU86ieYAtLyOOnC4q6zGBLCyF0_I8Pp76c2LOUJO3Pm2jVJoOKuTAQTIUmQuCnxap177vosIbtC2W-os" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a246913bf1.mp4?token=XOmE05aML4mM4mfiaeQSEjyNPECK5tUsbXPtw25lOX1_kFdkI90kpLFn8qY7apHYAozCHEkrmNMYxfksZG5KLDDPQzkxEjdVgNGhLDv14G7w2CbZ8exwj57yTMt7S4rqZmJGhIe2_74BXB_TnTQX5DePtEYY2RNPxUfzvyWeFZbNe5Sh0xBDzzrKNVeKjBXjiLl1_Zrxpffei2DO7LThKp3vUm0PU9QSHh0vKJ-p0jpSOh9jIcLRx1CpiIrb9_vsBKJG0FNWgmn90B5yBZV2yO1slVqL0sW13MF88h1WpHgy9OWFpx4LawUJextK8vxnakAd7t75ld4tgTqwThK_6q0oAoWP51_wVRJteOCzyCaEman_BLtmlkAQIPhreuFqw8MNqXZZVevK_fJYO0o-x3p7Ki2gSJcg0_bZvCWDCjEk_evjNTqinab7b4RPM98jdNtB_UwbjlrD9ScRxEd6Ny1pXaB5XZoRxidl0A9hvykIIBWKMFdnymlE_N1fqrdeZLeqB2tnnUMfVaCaM8xWHRTnnDdIuYfvppD0kfEGnh3rZHrpPzqbjVIHHHk-Qh4iTsQjjIgUxHi9DtD1nJ5L_fQpr8QnU86ieYAtLyOOnC4q6zGBLCyF0_I8Pp76c2LOUJO3Pm2jVJoOKuTAQTIUmQuCnxap177vosIbtC2W-os" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاکمیت ایران بر تنگه هرمز هر روز بیشتر می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/445892" target="_blank">📅 21:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445891">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f292d12ed5.mp4?token=CXt0u57Vl17iaA5AcppG33ZXS2KhPzch1xWjE14XIqwCnf6Tn-MFPz34YivKFljuaBT9P9n4jwHNHN8BpNMsogNvS5riKyo05_ZMZEH4FMjnvyJNcR_TrNPTbJbvOPsAkW85dhu3RHtN_HbiDe74yjVwKN7m_Pb3xMGHY_uXOiztJkx9Ej9nVYS9B_s0VngkXqsiQZ1MNnQLnSfbQfmA_deyYriYg32kz9Q7acoZWZlvojo6mcF69Iz9n46MBH8HViJ569jHG31pRGyO5ct9nuPtHoh8pQyIUmSKUOHnKuGqozPxUYrn3ZOmfTBx9uCl0HH9kBfFqrHs_SsFxJWpEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f292d12ed5.mp4?token=CXt0u57Vl17iaA5AcppG33ZXS2KhPzch1xWjE14XIqwCnf6Tn-MFPz34YivKFljuaBT9P9n4jwHNHN8BpNMsogNvS5riKyo05_ZMZEH4FMjnvyJNcR_TrNPTbJbvOPsAkW85dhu3RHtN_HbiDe74yjVwKN7m_Pb3xMGHY_uXOiztJkx9Ej9nVYS9B_s0VngkXqsiQZ1MNnQLnSfbQfmA_deyYriYg32kz9Q7acoZWZlvojo6mcF69Iz9n46MBH8HViJ569jHG31pRGyO5ct9nuPtHoh8pQyIUmSKUOHnKuGqozPxUYrn3ZOmfTBx9uCl0HH9kBfFqrHs_SsFxJWpEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کنگو از انگلیس پیش افتاد!
⚽️
انگلیس ۰ - ۱ کنگو @Farsna</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/445891" target="_blank">📅 21:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445890">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b78f01e3.mp4?token=c5ySgxa4fLDutQHQuS2PqF0w4Kxh3gZ6-7-B4_NAjyUgzZUn2idJ8t9htiIz_nCC8ER6MizTCakjleRePyZUeQBLaxsH_QDn6HNUxlMwnGCDKYoEMxT8qFCBK8uQVW5bsaoPtwxKCW3aDNoJqd1QObi0boFG3DfwU8x8C46GUQYVT5BUUsJI8k0fYLfvWQIDIpqrSkf7n_cj3FjxR_lfaRknzZfHCN-7-_sfyd6j3ofkGv_Pip2LVucPe9kaJK7o6LZY6i3LHVlvFjXhrIpsiwJPjUYvMtOQbdrfrsQLOQAhrrZSfFaEaFBeKRnwYgiuCXvfIAzEa-GRJeSNWgRSTKvQv5I5sPN6JtEVmqd_nXbdAIk3pnPawHODJCYHQB47fUUMQB6wDpvfhj5F3ThtmzpKgwn7wBgSPk6okE07ZIoZuJWvnapFGe-Uy1tIxNSjRr-BhshXVrrScTVvZY4xtD8DHTD-Srxhcxon9wjtkqoMfPHrNjUFmYOjTifJPoxL_uGoDHclrQ5Ri5G1jzgSQgb7tyq3EI_VEIHT-OSpnkilhMWrUl6LwsABap8hlOoKpsH_KwiH4Vrd0LNDsXiN0hO-LonlDpBxfK03PM408vSnAFpn07u2GAy06qi59hPg8HjvUwpaA7EH9GGmM_N4kY6qYfvcodRM9i9lmZj_lC4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b78f01e3.mp4?token=c5ySgxa4fLDutQHQuS2PqF0w4Kxh3gZ6-7-B4_NAjyUgzZUn2idJ8t9htiIz_nCC8ER6MizTCakjleRePyZUeQBLaxsH_QDn6HNUxlMwnGCDKYoEMxT8qFCBK8uQVW5bsaoPtwxKCW3aDNoJqd1QObi0boFG3DfwU8x8C46GUQYVT5BUUsJI8k0fYLfvWQIDIpqrSkf7n_cj3FjxR_lfaRknzZfHCN-7-_sfyd6j3ofkGv_Pip2LVucPe9kaJK7o6LZY6i3LHVlvFjXhrIpsiwJPjUYvMtOQbdrfrsQLOQAhrrZSfFaEaFBeKRnwYgiuCXvfIAzEa-GRJeSNWgRSTKvQv5I5sPN6JtEVmqd_nXbdAIk3pnPawHODJCYHQB47fUUMQB6wDpvfhj5F3ThtmzpKgwn7wBgSPk6okE07ZIoZuJWvnapFGe-Uy1tIxNSjRr-BhshXVrrScTVvZY4xtD8DHTD-Srxhcxon9wjtkqoMfPHrNjUFmYOjTifJPoxL_uGoDHclrQ5Ri5G1jzgSQgb7tyq3EI_VEIHT-OSpnkilhMWrUl6LwsABap8hlOoKpsH_KwiH4Vrd0LNDsXiN0hO-LonlDpBxfK03PM408vSnAFpn07u2GAy06qi59hPg8HjvUwpaA7EH9GGmM_N4kY6qYfvcodRM9i9lmZj_lC4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توصیه‌هایی برای حضور در مراسم تشییع رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/445890" target="_blank">📅 21:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445889">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">هشدار پلیس دربارۀ فریب با وعده رزرو اقامت و پارکینگ برای مراسم تشییع
🔹
پلیس فتا: عزاداران در ایام مراسم وداع، تشییع و تدفین پیکر مطهر قائد عزیز شهید، مراقب لینک‌های جعلی رزرو اقامت، پارکینگ یا دریافت بلیت باشند و به لینک‌های مشکوک در پیامک یا شبکه‌های اجتماعی اعتماد نکنند.
🔸
موارد مشکوک را به شماره ۰۹۶۳۸۰ یا سایت
پلیس فتا
گزارش کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/445889" target="_blank">📅 20:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445888">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44719355c2.mp4?token=RkXmncZJMf9wYGsUB7MXBDxiYdb5fTbPwYEEfvJUegJWUseRgkt-VNql1F6prdy7mYwuQFPfvP71rpG05AcUGRgbNAXpWalooyPyaeS_40dU6lmtjRTqhcnsYHOBvQAiYgbDg0uG33-mxmWXgwVXl68l1ac7lMYeR-vi2Vp1ZZr34ZS6_04bVhodETmM4uO3fgP2eHdiklrWccOH-MbaVIYaHUkz6FdDDKNEWq2wdGNN9rP_PUalqhi4Yb0fxZyDNQ3rGbfE1lw9N8wrUVqrTuetoLIdMpWOaRcwsl_gwOzLCKko9s4KaMahLGoKY17DcrYzNFmKF9-KixTHPWB-gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44719355c2.mp4?token=RkXmncZJMf9wYGsUB7MXBDxiYdb5fTbPwYEEfvJUegJWUseRgkt-VNql1F6prdy7mYwuQFPfvP71rpG05AcUGRgbNAXpWalooyPyaeS_40dU6lmtjRTqhcnsYHOBvQAiYgbDg0uG33-mxmWXgwVXl68l1ac7lMYeR-vi2Vp1ZZr34ZS6_04bVhodETmM4uO3fgP2eHdiklrWccOH-MbaVIYaHUkz6FdDDKNEWq2wdGNN9rP_PUalqhi4Yb0fxZyDNQ3rGbfE1lw9N8wrUVqrTuetoLIdMpWOaRcwsl_gwOzLCKko9s4KaMahLGoKY17DcrYzNFmKF9-KixTHPWB-gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عاقبت بی‌توجهی به فرامین ایران در تنگه هرمز
@Farsna</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/445888" target="_blank">📅 20:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445887">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b1f2f281.mp4?token=A4nPwyAjE9W4LM6_wfvJQohE6Oz2HKUUPYTF9WDBe7kE3UxhmVp6qAVbS8N1CUOIJLLSli7dwZc16p9_ISTrotAkbhf9EfJS4ITO4T5phJj64CwthKAQGlaOxoyGae-3Q-7wfMAEBGcGgp9wv-OtrfT_CzRyTMASWxGqvOr5nLxhQeBz2fKPEOMKBkR6_kwF-gHX-Ln_S_akNbwyeVYcUpP-FORUY0k9cskAWlUAFWwsooaOaJ8wnvkPa3ihAsotsDPbqKeVeVSJhe6H3GscfrBhhkuWZk_sNZS8KlLIhLPUTe9-_WDa-tgEQtbYyCQyxHb50S39NhP75VV2HHLYh44dRsuYiebon5ISs841eS9lkBjDPTPU2ZCu42UiqZgbq0pFcSJzQw4MTXA1aV55VmdI0YzrqqW1gOsHfbq2SogeY6mVT19vZ9j34h-AaT7aFEHqxAriapMADcHZIuS25ARiuCR7ZmRMtWUR41X5npFGwYLxD4e26cemnu7QvzDj5UnRrz3gkdxWlNyjO96D9QZYUwGPj_psOT3Oj0_l0Y5WPNhlFloYwncoVpuLzOlkcdh9ZXuwOwbCYIuXysgJcQgPUSI9m9ffE0_qoArGFvn5i10iRl-YSkA7Qjxe81ip_pfo5Wzbj8_902ZIFg0h5oPCo_pU8FL4iVu7hgfj1Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b1f2f281.mp4?token=A4nPwyAjE9W4LM6_wfvJQohE6Oz2HKUUPYTF9WDBe7kE3UxhmVp6qAVbS8N1CUOIJLLSli7dwZc16p9_ISTrotAkbhf9EfJS4ITO4T5phJj64CwthKAQGlaOxoyGae-3Q-7wfMAEBGcGgp9wv-OtrfT_CzRyTMASWxGqvOr5nLxhQeBz2fKPEOMKBkR6_kwF-gHX-Ln_S_akNbwyeVYcUpP-FORUY0k9cskAWlUAFWwsooaOaJ8wnvkPa3ihAsotsDPbqKeVeVSJhe6H3GscfrBhhkuWZk_sNZS8KlLIhLPUTe9-_WDa-tgEQtbYyCQyxHb50S39NhP75VV2HHLYh44dRsuYiebon5ISs841eS9lkBjDPTPU2ZCu42UiqZgbq0pFcSJzQw4MTXA1aV55VmdI0YzrqqW1gOsHfbq2SogeY6mVT19vZ9j34h-AaT7aFEHqxAriapMADcHZIuS25ARiuCR7ZmRMtWUR41X5npFGwYLxD4e26cemnu7QvzDj5UnRrz3gkdxWlNyjO96D9QZYUwGPj_psOT3Oj0_l0Y5WPNhlFloYwncoVpuLzOlkcdh9ZXuwOwbCYIuXysgJcQgPUSI9m9ffE0_qoArGFvn5i10iRl-YSkA7Qjxe81ip_pfo5Wzbj8_902ZIFg0h5oPCo_pU8FL4iVu7hgfj1Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همه برای آخرین دیدار با رهبر شهیدشان آماده می‌شوند
@Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/445887" target="_blank">📅 20:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445886">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🎥
ندانستم که این دریا چه موج خون‌فشان دارد...
@Farsna</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/445886" target="_blank">📅 20:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445884">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۸۲.pdf</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/farsna/445884" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۸۱.pdf</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/445884" target="_blank">📅 20:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445883">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89cbb42bef.mp4?token=e2Lxft8q0dmBUc1hbvnLP0C8u1y4yyCb9kPLPRuqXuSuQGgohFrDEN6JhzsortcHSppeEc2f2NqK8_YSy8hst6L6XJs-8A9cw11Wp-G28j3_gDAkHVSFlWi2U-pTM5bHAxoQrdNYPyE-tchJiwiU-v7HolplF-G69VXtQlRVl3b-dZW1AeOYeoQciPnT11oFgM2pz9HVymqOQqTB5KPwx_pOUtuQXnDCv-K12SvhQZhjqSe7nD66JSq6lDBqQLb5ZyT-l9KmBUWTHCy5TJTbue0yx4SQ98l6XTtyhT7dPSPyUDtIPxPSq7GUs8szl_82P4p-zsGOIHf6NwS91Td-oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89cbb42bef.mp4?token=e2Lxft8q0dmBUc1hbvnLP0C8u1y4yyCb9kPLPRuqXuSuQGgohFrDEN6JhzsortcHSppeEc2f2NqK8_YSy8hst6L6XJs-8A9cw11Wp-G28j3_gDAkHVSFlWi2U-pTM5bHAxoQrdNYPyE-tchJiwiU-v7HolplF-G69VXtQlRVl3b-dZW1AeOYeoQciPnT11oFgM2pz9HVymqOQqTB5KPwx_pOUtuQXnDCv-K12SvhQZhjqSe7nD66JSq6lDBqQLb5ZyT-l9KmBUWTHCy5TJTbue0yx4SQ98l6XTtyhT7dPSPyUDtIPxPSq7GUs8szl_82P4p-zsGOIHf6NwS91Td-oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنوب لبنان همچنان زیر آتش حملات اسرائیل
🔸
شبکهٔ المنار گزارش داد که رژیم صهیونیستی در ادامهٔ نقض تفاهم آتش‌بس، در حمله‌ای پهپادی، شهرک النبطیه الفوقا در جنوب لبنان را هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/445883" target="_blank">📅 20:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445882">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee5bec92ce.mp4?token=JMf1UI-WeVJhGlC3vHXvrQilp25nyRm2JkHvXpjDDqr3KfrALmQkslQ-GWhiesv9nIEXHAOXV8_ocxQO3sSWzh_NoPTd8hdGuxhRJAIZ7zZQJm-X0aXuAUr83nC696BaSvlx7sf3NlFM55XHlVpZ6XY0Bl2_dD6YHHXPBVuaQsHEOLtXdegMbwiEzKx33J3MIhWgdsSY0SltwzXV6LLKZyNe5d1GNwKrw7IGNk-eVaGuRoQ1-3Fby7dxNWJRtiR2oigQEPqEoMj0SN9yti1ANTB4jgxyKKpHaQKNliNF9VY5HqGtedLF-Og5EDeV3MRq_TzaB0RkOHLRRDpoIwu6Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee5bec92ce.mp4?token=JMf1UI-WeVJhGlC3vHXvrQilp25nyRm2JkHvXpjDDqr3KfrALmQkslQ-GWhiesv9nIEXHAOXV8_ocxQO3sSWzh_NoPTd8hdGuxhRJAIZ7zZQJm-X0aXuAUr83nC696BaSvlx7sf3NlFM55XHlVpZ6XY0Bl2_dD6YHHXPBVuaQsHEOLtXdegMbwiEzKx33J3MIhWgdsSY0SltwzXV6LLKZyNe5d1GNwKrw7IGNk-eVaGuRoQ1-3Fby7dxNWJRtiR2oigQEPqEoMj0SN9yti1ANTB4jgxyKKpHaQKNliNF9VY5HqGtedLF-Og5EDeV3MRq_TzaB0RkOHLRRDpoIwu6Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاندار تهران در برنامه پرچمدار: قرار است از همۀ مدارس تهران برای اسکان زائران و شرکت‌کنندگان در مراسم تشییع رهبر شهید استفاده شود
🔹
علاوه بر مدارس، مساجد، دانشگاه‌ها، ورزشگاه‌ها و سالن‌های ورزشی نیز برای این منظور پیش‌بینی شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/445882" target="_blank">📅 20:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445881">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c5e51114.mp4?token=TwHGaTaLeKuC1UMuFZfnk5hGSqfT34n7bua0tklZMGZw6-4saToakutaENZyFgEYUV62pJtwNhlFKx6QBX_5eKLqWxrticKtyqNvszbSGezuI-Evjwa-kQCBXXZnAQEsKhsTOm7fNgnmNcnAQUWnqyi3SjHCek10LNmxMim_xPCDHGPBACXFLaoBfX2dB7Gr5G1IxjUGxox4gpQo09YOrtAbCbs_VJo3_G4T52Y-c7dKHI8pJkN-AcgdkkMaavJg4_Vjn3wNSzcrF2klUzfdlNHgDENxkLRJd-Gnb8DWirwwlEME6WixuIYOmslw3evGqXrnHxrvFiHKu8oKscpJYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c5e51114.mp4?token=TwHGaTaLeKuC1UMuFZfnk5hGSqfT34n7bua0tklZMGZw6-4saToakutaENZyFgEYUV62pJtwNhlFKx6QBX_5eKLqWxrticKtyqNvszbSGezuI-Evjwa-kQCBXXZnAQEsKhsTOm7fNgnmNcnAQUWnqyi3SjHCek10LNmxMim_xPCDHGPBACXFLaoBfX2dB7Gr5G1IxjUGxox4gpQo09YOrtAbCbs_VJo3_G4T52Y-c7dKHI8pJkN-AcgdkkMaavJg4_Vjn3wNSzcrF2klUzfdlNHgDENxkLRJd-Gnb8DWirwwlEME6WixuIYOmslw3evGqXrnHxrvFiHKu8oKscpJYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلاش بهمن‌موتور برای تغییر کاربری ۱۲۰ هکتار زمین کشاورزی
🔹
گروه صنعتی بهمن طی ۶ ماه اخیر ۳ مرتبه برای تغییر کامل کاربری یک محدوده ۱۲۰ هکتاری زراعی در جوار روستای دانش شهرستان قدس تهران تلاش کرده است.
🔹
طبق گفته شاهدان محلی این شرکت این‌بار به بهانه ایجاد پارکینگ خودروهای مراسم وداع با رهبر شهید، این منطقه را دیوارکشی کرده و در آن اقدامات عمرانی را آغاز کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/445881" target="_blank">📅 20:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445880">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e623a8c6.mp4?token=D3KAB8xjAtjqVKwmHQ64Hr1JF6JJkVro6DPa-vxBbxaxVw5OTehHr-1aDmYgW_1EWKi1w1H7ouf8yHFNhMqoOV-3bc-bjpb-bxtRlvrCe9LjVjfB76fxGqlP8jTJH8VtelC0hX1ETRJma-AxFD6NiNRoyKXUSBaW0gNrw1bhmO-X_KlRN9mXcxTxUEkK6qZ7z5idpYhOnaRTwuwGzvrJULo5yelYOrWqAjFj6vkhaCSukFq5bL08F0QM_78fuJtjkRxSalbW5c6NNoZ8VPvrm8WQkUdsww37mekSPpxr5fKLA8N5OroSABM8dEnisv5yYx8tqnT-GWK7Ru5tnHaMew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e623a8c6.mp4?token=D3KAB8xjAtjqVKwmHQ64Hr1JF6JJkVro6DPa-vxBbxaxVw5OTehHr-1aDmYgW_1EWKi1w1H7ouf8yHFNhMqoOV-3bc-bjpb-bxtRlvrCe9LjVjfB76fxGqlP8jTJH8VtelC0hX1ETRJma-AxFD6NiNRoyKXUSBaW0gNrw1bhmO-X_KlRN9mXcxTxUEkK6qZ7z5idpYhOnaRTwuwGzvrJULo5yelYOrWqAjFj6vkhaCSukFq5bL08F0QM_78fuJtjkRxSalbW5c6NNoZ8VPvrm8WQkUdsww37mekSPpxr5fKLA8N5OroSABM8dEnisv5yYx8tqnT-GWK7Ru5tnHaMew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار حوزۀ مقاومت: دشمن در تلاش است به دستاوردهایی برسد که هنگام جنگ نتوانسته به آن دست پیدا کند.
@Farsna</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/445880" target="_blank">📅 20:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445879">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d85ac7627.mp4?token=oxTZvtlPpCB-u8_fIGWVvztw6HoBbxesk76Ib9Cfh4oshfZtWORTV6rvoD0NEo4Z3iPcesbQjEAnv4YiB4Cj9uuNBEhlUlJKv12H9sd_Oj5Lcz5903ycRQ7rpU71lW33ZDL_nVS8-GTADAEBhtEzMx0Rc94h7B2wxdMWQcM8EqYmR-tvvFbQH-G9VKW5AsOsSeQ5oA5sulLr14L9r7pj4TFwS0tuD1o0VJ4Yt0T1KpJmjKz_S9stgRuV_muHvS0Oo4Yk8thTV4S61cSlbOb6HJIhA1f89k78489vdctm2SFPv7DqaXpN_NOLyzL-eTVYe-a4Iyh5YV8th5z_UBbd5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d85ac7627.mp4?token=oxTZvtlPpCB-u8_fIGWVvztw6HoBbxesk76Ib9Cfh4oshfZtWORTV6rvoD0NEo4Z3iPcesbQjEAnv4YiB4Cj9uuNBEhlUlJKv12H9sd_Oj5Lcz5903ycRQ7rpU71lW33ZDL_nVS8-GTADAEBhtEzMx0Rc94h7B2wxdMWQcM8EqYmR-tvvFbQH-G9VKW5AsOsSeQ5oA5sulLr14L9r7pj4TFwS0tuD1o0VJ4Yt0T1KpJmjKz_S9stgRuV_muHvS0Oo4Yk8thTV4S61cSlbOb6HJIhA1f89k78489vdctm2SFPv7DqaXpN_NOLyzL-eTVYe-a4Iyh5YV8th5z_UBbd5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرسپولیس مقابل خواستهٔ اسکوچیچ کوتاه آمد
🔹
با کوتاه‌آمدن باشگاه پرسپولیس از موضع قبلی خود دربارهٔ مدت قرارداد با اسکوچیچ، به احتمال فراوان این مربی کروات در روزهای آینده به‌عنوان سرمربی جدید سرخپوشان معرفی خواهد شد.
🔸
اسکوچیچ از ابتدا خواهان عقد قراردادی ۲…</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/445879" target="_blank">📅 20:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445878">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1c113ecd4.mp4?token=BAB0mO3OeBFjFbpIXNwQpNYXhukh1jaDsZy8g6-97KNkwGzqsht__20-ZbPFQAgTS1KsBuD-WGuJJEVsZqvS46XfwXtDV9devJzBaJSsPJvhpGcQe5upTTRya_lBX7TudqV1QybQlZxWBPE_IPw1sfvT8MItulEVnlJj9ceP72f5Z7cTgH-_NPOUdcXhxmr5nQjaUHT3bmrOFJ3AGIavh_Stx2nUHTZE0JnvT-bx9s8xN72p2qiG5CKKAIcGkmtVAHqrDw-f43g7J8vSuTXqzONkoYFdubF9i4WxBkLxOJamdZ07lO0cgQ8Q56CrwgG02PTCdNkXi-WVvsmagNonEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1c113ecd4.mp4?token=BAB0mO3OeBFjFbpIXNwQpNYXhukh1jaDsZy8g6-97KNkwGzqsht__20-ZbPFQAgTS1KsBuD-WGuJJEVsZqvS46XfwXtDV9devJzBaJSsPJvhpGcQe5upTTRya_lBX7TudqV1QybQlZxWBPE_IPw1sfvT8MItulEVnlJj9ceP72f5Z7cTgH-_NPOUdcXhxmr5nQjaUHT3bmrOFJ3AGIavh_Stx2nUHTZE0JnvT-bx9s8xN72p2qiG5CKKAIcGkmtVAHqrDw-f43g7J8vSuTXqzONkoYFdubF9i4WxBkLxOJamdZ07lO0cgQ8Q56CrwgG02PTCdNkXi-WVvsmagNonEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: هم‌وطنانی که به‌صورت کاروانی یا با خودروی شخصی در مراسم تشییع رهبر شهید حضور می‌یابند، حتماً خود را به محدوده تعیین‌شده برای استان خود برسانند
🔸
برای هر استان، محل مشخصی در تهران جهت اسکان و استقرار زائران در نظر گرفته شده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/445878" target="_blank">📅 20:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445877">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7c5fed497.mp4?token=ci9efvwT2U4CBonmWIoQ2EyAoklnmREcjt9-RdVpTa1eBFntRkqxIG039FzihIOiTOwO2LxSXzRzUE4iYL-LbiZfHReqoUZi2qd86e42O0i6T5DROT1D3nRRlOI7rM979-IZLbwpK7SE-uHo5rci46cBgc8ELWvtYr13ojmeBe47_TNozIFU7nJr69_xw5UcAFXlJyHNrDqyqfBOCGCtD59c4ZSTWN5YdjPxTs78bq8npEaSt_YWvsgOI6epi8bLinwpoTDj-COZzKZ19Cszl7CoIWUq2cPWU97YlFfCHUsAhOOy5aLWgoC7EQPsit7SU2DxBaaY4uEiMEtf6QUVIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7c5fed497.mp4?token=ci9efvwT2U4CBonmWIoQ2EyAoklnmREcjt9-RdVpTa1eBFntRkqxIG039FzihIOiTOwO2LxSXzRzUE4iYL-LbiZfHReqoUZi2qd86e42O0i6T5DROT1D3nRRlOI7rM979-IZLbwpK7SE-uHo5rci46cBgc8ELWvtYr13ojmeBe47_TNozIFU7nJr69_xw5UcAFXlJyHNrDqyqfBOCGCtD59c4ZSTWN5YdjPxTs78bq8npEaSt_YWvsgOI6epi8bLinwpoTDj-COZzKZ19Cszl7CoIWUq2cPWU97YlFfCHUsAhOOy5aLWgoC7EQPsit7SU2DxBaaY4uEiMEtf6QUVIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات برنامه‌های فرهنگی مراسم وداع با رهبر شهید امت در مصلی تهران  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/445877" target="_blank">📅 20:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445876">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نماز بر پیکر مطهر رهبر شهید ۶ صبح یکشنبه اقامه می‌شود
🔹
رئیس ستاد آیین وداع، نماز و تشییع پیکر مطهر رهبر شهید: اقامۀ نماز بر پیکر مطهر ساعت ۶ صبح روز یکشنبه برگزار می‌شود و از مردم می‌خواهیم برای حضور در این مراسم زودتر در محل حاضر شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/445876" target="_blank">📅 20:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445875">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyiCOnDTu7p52BZyOv4r5GnpNHqIqkVYET2KIk8TTockZJ5EvAEDk0us3e-dB0SsQgnm_1YotlL3JC2ibZqzIoyjXqAXq-MWzQiyR9-Cjl8DsU5wsZoEthiORJPU3ttNijKfGNVArPMW0k2SAAZlEa19lWJ3lFNJQlfUp3U-BcpWom2-0JyJbQhEW05oLazpJfZad5KloAIuYKOfvBUOaAA8__6dlFyjjyIdLB4PDIX9scbE0A0yHOkKzJ1G6YWQ9utRf4YfCk0xFjvyAf0W0OLsbsZgBi4kQXFWv8QlXarbw_L547F-e4nG_XDfxwXY8J3PrB2D6MddLAIgssZfaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون سیاسی نیروی دریایی سپاه طی سانحه رانندگی درگذشت
🔹
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان جان خود را از دست داد.
🔹
پس از وقوع…</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/445875" target="_blank">📅 20:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445874">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/703007658e.mp4?token=lsiWYTUbaEbGangdS3nePtLofPF9sIhyVk2KB6fc72VI_3cHZRHVMfnu0OHs4cRNybSMzQe1ErMp018ItfEXDuS5XCmRjnU1KYxY_KyTCYYTfnnjUTGMQHLOKrWpoLJgVgJRSA9BghdHsbJqZ9r3CJsNNWSbdsbgehhMYJ2OlhkjXGHgdC-OB7Mjb-hOQx2j9pKROep0vLeOvwDhEXN9Zv5kKy9wumt5VuIqhrQccpMmB6ijU16hjeGe-5PcUbZJHjyYeNEML08zghj3ruNwIK0HRsPGHAVIa5joc7dbRIckvbQs2dE1UQyM3SAKFL1xDa4TiVwKf-ChYu4ce1B76IWy46Oxf31HEp126d6D74dA9Y78ulpF6p0xMAWDSbZYvaYM3GlNjQ8SszzreYgrtyJlD3MRtNietC6RUIfyIMGdu6zPy-mY3tOghAe1SVeKlNjfFLXSKcicq7gfh-h81SeyRkGKJjUZXActslQAjDUvY_BOxX1K33xLO1lsbrGAp2x41lTFE6w81nqjA7J1D4JIGAR7rYwf29pxBWPI5GMQewlWxLjfxCAleCS9AF3aML0xgxCP9_z6CO00MszUiuZO8fHRVuFZuyCXcH08yyPjN5bCKzggqYdoDIKRNd4aZD-9zy0WuMPzVPmk7czmJd7JAJq67nsfF533ZZnCkRE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/703007658e.mp4?token=lsiWYTUbaEbGangdS3nePtLofPF9sIhyVk2KB6fc72VI_3cHZRHVMfnu0OHs4cRNybSMzQe1ErMp018ItfEXDuS5XCmRjnU1KYxY_KyTCYYTfnnjUTGMQHLOKrWpoLJgVgJRSA9BghdHsbJqZ9r3CJsNNWSbdsbgehhMYJ2OlhkjXGHgdC-OB7Mjb-hOQx2j9pKROep0vLeOvwDhEXN9Zv5kKy9wumt5VuIqhrQccpMmB6ijU16hjeGe-5PcUbZJHjyYeNEML08zghj3ruNwIK0HRsPGHAVIa5joc7dbRIckvbQs2dE1UQyM3SAKFL1xDa4TiVwKf-ChYu4ce1B76IWy46Oxf31HEp126d6D74dA9Y78ulpF6p0xMAWDSbZYvaYM3GlNjQ8SszzreYgrtyJlD3MRtNietC6RUIfyIMGdu6zPy-mY3tOghAe1SVeKlNjfFLXSKcicq7gfh-h81SeyRkGKJjUZXActslQAjDUvY_BOxX1K33xLO1lsbrGAp2x41lTFE6w81nqjA7J1D4JIGAR7rYwf29pxBWPI5GMQewlWxLjfxCAleCS9AF3aML0xgxCP9_z6CO00MszUiuZO8fHRVuFZuyCXcH08yyPjN5bCKzggqYdoDIKRNd4aZD-9zy0WuMPzVPmk7czmJd7JAJq67nsfF533ZZnCkRE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برگزاری آیین نخل‌گردانی ششم محرم در نیاسر اصفهان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/445874" target="_blank">📅 20:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445873">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584a83a1dc.mp4?token=Kqki3_urmTcddRalcWwl57nemZpWpZbHdKAx5YHXOjhaTaqH8hLv8t4AlKCYG0uirDA0tN_wThGgrSYkDrQRrFeBszkAbH1GL9PemeMiNw58l-4szSR2xYIjhwlBdTscNC8CULWwZgfsusWssPxLtx11Sn-GDlMD2t6cbvbvgJ9zIyVmJ5BJ4wSoFFP79J2_gUiTWHymZ-Hu-Q6tCtr8JvvwkemH95o28nFzeGQTKo8-0nFZVtwtpMt-FgvDu9Wp6pJRYgge5Wt2WJG0JnheR_xJ-DQ8D69Nxh6nkxe1xsrkaTsT-Trhb0ep49wwpCm7l_HO6h30dnVhwMTx5OGyGwBTQWadlB94Li_YIf9Mgjj8NiWGwuIp3RfgznLOY_ibSZX_wV4OZjfZj_s104tdJ0cQLSVcTmg0IdrEq9RgMl13SdCnUpCKL1PvAxz7I3_twCcnmSQxCDvyMGJJgmxaZGt5ObTUtGAPMrfLXzWCF3F7k1ilPdnmN9nAAqMpIQ6rEdyE7iJ9cT4_VLnVf1vbAsFoKHRMBaStTU2Y1bTU64bKe8H0OFFlryGvQ0SqWZjkHyLeBc9_QAWJkLmDhoLPcxrNSZx-reVtUQt4-N6Yyww8ndOpQ3-UrzRJsXg0Lqu1s1lfy0Aby_-QUFPzHBbvnaMy7GLBcMQ57jGtkWKaKOc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584a83a1dc.mp4?token=Kqki3_urmTcddRalcWwl57nemZpWpZbHdKAx5YHXOjhaTaqH8hLv8t4AlKCYG0uirDA0tN_wThGgrSYkDrQRrFeBszkAbH1GL9PemeMiNw58l-4szSR2xYIjhwlBdTscNC8CULWwZgfsusWssPxLtx11Sn-GDlMD2t6cbvbvgJ9zIyVmJ5BJ4wSoFFP79J2_gUiTWHymZ-Hu-Q6tCtr8JvvwkemH95o28nFzeGQTKo8-0nFZVtwtpMt-FgvDu9Wp6pJRYgge5Wt2WJG0JnheR_xJ-DQ8D69Nxh6nkxe1xsrkaTsT-Trhb0ep49wwpCm7l_HO6h30dnVhwMTx5OGyGwBTQWadlB94Li_YIf9Mgjj8NiWGwuIp3RfgznLOY_ibSZX_wV4OZjfZj_s104tdJ0cQLSVcTmg0IdrEq9RgMl13SdCnUpCKL1PvAxz7I3_twCcnmSQxCDvyMGJJgmxaZGt5ObTUtGAPMrfLXzWCF3F7k1ilPdnmN9nAAqMpIQ6rEdyE7iJ9cT4_VLnVf1vbAsFoKHRMBaStTU2Y1bTU64bKe8H0OFFlryGvQ0SqWZjkHyLeBc9_QAWJkLmDhoLPcxrNSZx-reVtUQt4-N6Yyww8ndOpQ3-UrzRJsXg0Lqu1s1lfy0Aby_-QUFPzHBbvnaMy7GLBcMQ57jGtkWKaKOc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
می‌روی و نمی‌رود غم تو از دل
...
@Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/445873" target="_blank">📅 19:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445872">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd47bf230.mp4?token=Az4CngbvNXCIJqFrCKGh1j9w_dN_nMEVIdmczM0SchvHgsLOzrXI_byjNfKtqqgyF8QXEh1z1ypE8n6gstztdXlXC0Mpit8z5DE-93RQeoU4o6Gf2vrhQT4zHAWLNi1ehvO4eVLYx8l3li4a-WyrKqhN9ywtVKPYvI34lQ8BhYDqVWCIgg9g7i8RZ6OMNIF6WyYsnxRHqhyGBcWK1-f-oGsseMbZJ5jOHojnZwq8cwjtLoyhL9f_QWphlkVnidZmNfquzTm4uu2jbFJ9jPz3n3ERbJ4JMVkTn90B0Ly0lWCfumaWq0zc0i64GfDSkbwR_XMxKoh1Mi8-wJLlenLOKK33mJHXJgIRZCT9WH8426hbtZyQxnTalsqfggVFHTC8pX4XxK-1w0wUp2WGAaks9dHWPfoeDaCzIQPECBsfnzXweMmbg4f1YBoosPtfr92R69jFQqvoJ9i3l1FraGwF15_0tIyn7LsehVWVd5e1WbPwWKn453yssTfPtKVIIBDt8qkQZXXy9UdyP4tRtLOTU_CgSTR-3f4wHQde7FUvLFjqjQUU2scCyrbGB6PehwNHcjSrcXzaJ8ImS-OZTgSihIqHGB55b4KTQ23O2-xZiLE5oeAGIpYPbgHXG2l8adNAWBbQWy4QRZoDygjlypD0P7buav1cwuLGF75jLM-Ff58" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd47bf230.mp4?token=Az4CngbvNXCIJqFrCKGh1j9w_dN_nMEVIdmczM0SchvHgsLOzrXI_byjNfKtqqgyF8QXEh1z1ypE8n6gstztdXlXC0Mpit8z5DE-93RQeoU4o6Gf2vrhQT4zHAWLNi1ehvO4eVLYx8l3li4a-WyrKqhN9ywtVKPYvI34lQ8BhYDqVWCIgg9g7i8RZ6OMNIF6WyYsnxRHqhyGBcWK1-f-oGsseMbZJ5jOHojnZwq8cwjtLoyhL9f_QWphlkVnidZmNfquzTm4uu2jbFJ9jPz3n3ERbJ4JMVkTn90B0Ly0lWCfumaWq0zc0i64GfDSkbwR_XMxKoh1Mi8-wJLlenLOKK33mJHXJgIRZCT9WH8426hbtZyQxnTalsqfggVFHTC8pX4XxK-1w0wUp2WGAaks9dHWPfoeDaCzIQPECBsfnzXweMmbg4f1YBoosPtfr92R69jFQqvoJ9i3l1FraGwF15_0tIyn7LsehVWVd5e1WbPwWKn453yssTfPtKVIIBDt8qkQZXXy9UdyP4tRtLOTU_CgSTR-3f4wHQde7FUvLFjqjQUU2scCyrbGB6PehwNHcjSrcXzaJ8ImS-OZTgSihIqHGB55b4KTQ23O2-xZiLE5oeAGIpYPbgHXG2l8adNAWBbQWy4QRZoDygjlypD0P7buav1cwuLGF75jLM-Ff58" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عصبانیت مجری MBC عربی از دست برتر ایران
🔸
مجری شبکهٔ MBC عربی: ما این توافق‌نامه را شرم‌آور می‌دانیم، یعنی خود آمریکایی‌ها در آمریکا هم چنین دیدگاهی دارند که این توافق‌نامه کاملا به نفع ایران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/445872" target="_blank">📅 19:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445871">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQWd3TMCjJ6eqiobNB-K-XX9sRn5TJn_SeHf4e8oiZsW_OXfrKagVP8Bbcrmod1X1uRGFLXSQqmvoWdDE3QAkb4h4kbG7Q0YDKddsAh_2-VxrKIvfjdzUvHmsumeT7NUPuyLqbpEUDecgyscVqis0KDnBo8Q3xx3uW5KnnOHyRYiUSsNGClJIXKLRzQheQWiKs4N__aedeb9PG8xYdiMRWw1Ri-luI4FWpa1sAz4Z0zJreu2ZhXWIyb0xDMGAWuqTkscCEkxydYIO-CGa0HvLqFdLrMi825vQuzFYcpZ_AI82jiQz7-pez5filQ6m8pIzMU3HrxJzpy5PkVwUs53Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: به اعضای تیم ملی فوتبال کشورمان که امروز به ایران عزیز بازگشتند، خداقوت می‌گویم
@Farsna</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/445871" target="_blank">📅 19:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445870">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/341edfec61.mp4?token=AmO86IFitZDvtXGAY8R2bXAcOEGvj0iyRDoKSf7LimpZbryoYiIoTqB2XzVvCX5Q-DYZCNktWkvBTWlIe8lpIGkFpqLfwyZp0TOjwyIZmXgQ2Czr3VUZ9F9dyXBDuxuO5h6Hz4e281K-4ggqKq1pBAOW0i6Y8pkLiBfhq6_hfLU6IHAqGdmWyU7U3drK2USZv2PLiCkvcWS-AeOy5lH532o6mx0odJwTOh3g9S51xq3eXnajkyH-s-fRQLNsagFRVbQ0NKXg9uOduF2Ez-PJ4WJ504BEqiqZxLMot49biPCyJQIf-XQJK98w4N3rq_SPSORq0QxBCga7KLoBbwOpzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/341edfec61.mp4?token=AmO86IFitZDvtXGAY8R2bXAcOEGvj0iyRDoKSf7LimpZbryoYiIoTqB2XzVvCX5Q-DYZCNktWkvBTWlIe8lpIGkFpqLfwyZp0TOjwyIZmXgQ2Czr3VUZ9F9dyXBDuxuO5h6Hz4e281K-4ggqKq1pBAOW0i6Y8pkLiBfhq6_hfLU6IHAqGdmWyU7U3drK2USZv2PLiCkvcWS-AeOy5lH532o6mx0odJwTOh3g9S51xq3eXnajkyH-s-fRQLNsagFRVbQ0NKXg9uOduF2Ez-PJ4WJ504BEqiqZxLMot49biPCyJQIf-XQJK98w4N3rq_SPSORq0QxBCga7KLoBbwOpzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کنگو از انگلیس پیش افتاد!
⚽️
انگلیس ۰ - ۱ کنگو
@Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/445870" target="_blank">📅 19:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445869">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMgMiWuGsrjsRpxlR_YqB3uycX7oldKB2qjXJZuop5Q5w2o9Lo5WQuk4RJI9xEm_shOzXfHouasw708QrHRKCAiBdaJj64CX54gW9otQJQNz97yMq5-DJ60P3bZL4ePYSwU6NPIdc8CywSEvEm9nD1tWWxTHBWoiRolTHS1uO1QoJb5RVDgfJfxd_TspaYVxtHeH6gPBH0HvBAguyoxlBgk9kpDDiU03J__Xo8Az2IwarmKUkzlEZxdo4aB2BsE-COzUCiUqNJ6OwDpEpRrhFsGu3cqgxfR4rJPPhcfI2akbLEQ4IXSNf1WedA5abQmmmEfzxNh8cuoNwlo0rjcllg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
جزئیات برنامه‌های فرهنگی مراسم وداع با رهبر شهید امت در مصلی تهران  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/445869" target="_blank">📅 19:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445868">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHGVVhnUBKvUi8O08_dnIfQhneg5H68Nv164Mm3_wcUH8v08aMN21zxXJF4TY-vpZGqlBfukEPgVKjgIxdNaiCjFrofsj47Hmk65lCMJV5HGr8qXvdgjLNrLQOJUn6XQAtAimZp-exjmUlihERJSP7t7gbRwSCqneVuZrfjeXz3Dt6V7ZFGrNMKu7exosX16ZFy1D3yVoEk2ip95_JQl5nE_NQqBr5QUZbC0qLJDs55ITpDd_gTHcehnHQAUwHP2zi3pvXF6BZGP9Sdq0vUA95AczubzYmMXo3cNkttJMWnExHKgc5e3dfYoyku_uph-55wOkZ3pWS7K4uCPt95rhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفع ممنوعیت صادرات محصولات شیمیایی و پتروشیمی
🔹
گمرک: صادرات محصولات شیمیایی، پلیمری و پتروشیمی با رعایت مقررات پیش از محدودیت‌های شرایط اضطرار، بلامانع می‌باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/445868" target="_blank">📅 19:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445867">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81309983d6.mp4?token=ZAKtHZRlElRKsD1bVHC4GDCzLaXqJBNYWjpSBTUXiX65vijA257Ls-JNExZQFLi9V9QbcUaGe3liWfKydh-vPSAmBAuYQ2rHSj5mIea0wynlIPsDR8mP4q6LZOm-8Nleen9k7HinZYQ7Dc-kNNRPumBzHMbRbKKHXZoLEZL9xHT2g9wMeVSyfR6m-1sX0nUEfpRYgCXuocJkiDxDW51qGn4JBXpotNaYJGrbYK0qgM-QonK2IAsFbNYxSd_0yplFPpxfMb4W_IhOl6NPNuG246ByZ-Z9Hug-9R9EiklUpn0SNnYfEGm5q1XjZcILsxaCiuLwONcA30U51XWOBdU2jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81309983d6.mp4?token=ZAKtHZRlElRKsD1bVHC4GDCzLaXqJBNYWjpSBTUXiX65vijA257Ls-JNExZQFLi9V9QbcUaGe3liWfKydh-vPSAmBAuYQ2rHSj5mIea0wynlIPsDR8mP4q6LZOm-8Nleen9k7HinZYQ7Dc-kNNRPumBzHMbRbKKHXZoLEZL9xHT2g9wMeVSyfR6m-1sX0nUEfpRYgCXuocJkiDxDW51qGn4JBXpotNaYJGrbYK0qgM-QonK2IAsFbNYxSd_0yplFPpxfMb4W_IhOl6NPNuG246ByZ-Z9Hug-9R9EiklUpn0SNnYfEGm5q1XjZcILsxaCiuLwONcA30U51XWOBdU2jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌چادرملو آسیایی شد
🔹
چادرملو با شکست گل‌گهر در ضربات پنالتی، سهمیۀ سوم ایران در آسیا را به دست آورد.
⚽️
چادرملو  ۷ - ۶ گل‌گهر
🔸
بازی در وقت‌های معمول ۰-۰ شد. @Farsna</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/445867" target="_blank">📅 19:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445866">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac3ed8b64.mp4?token=bugk7YK2Kn5hrZ6mTZEAJnLZ8_txNtjqg3xce3-QB3l5grhOZqPOZy_TXrZCOspC8DkpK0TcnH8ld1xV9jUhvuUUOlXwSgSlrE9rTb6HmxjjicErYsdKSIfK-rIem7Cw2zg_S8sDoBgnDtLhA9IyZpeqV8eG4ZdNCpPY52Zm7VSvBfvDnFaoNDNZi1ccIjZcaFlpdOdxRD1n7qoTsPfhPuv7x0YolJSOjINnr7diy-wy34DieMD1nXEuXMSZBjl1rcRxa7N-d1Nm1Kw7mzihBieSt4wA6rlob73Mpj0P-pNqdV8puzr-kjqULSEBbPgrm-zEtfwAdc_9Ga9pgRQAEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac3ed8b64.mp4?token=bugk7YK2Kn5hrZ6mTZEAJnLZ8_txNtjqg3xce3-QB3l5grhOZqPOZy_TXrZCOspC8DkpK0TcnH8ld1xV9jUhvuUUOlXwSgSlrE9rTb6HmxjjicErYsdKSIfK-rIem7Cw2zg_S8sDoBgnDtLhA9IyZpeqV8eG4ZdNCpPY52Zm7VSvBfvDnFaoNDNZi1ccIjZcaFlpdOdxRD1n7qoTsPfhPuv7x0YolJSOjINnr7diy-wy34DieMD1nXEuXMSZBjl1rcRxa7N-d1Nm1Kw7mzihBieSt4wA6rlob73Mpj0P-pNqdV8puzr-kjqULSEBbPgrm-zEtfwAdc_9Ga9pgRQAEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلعه‌نویی: بعد از بازی با مصر خواستم بگویم فوتبال [با ما سر ناسازگاری دارد] اما اشتباهی گفتم خدا.  @Farsna</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/445866" target="_blank">📅 19:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445865">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04697378e1.mp4?token=pQajDtLlY_2VuWuwbseMABwA_8i0kIlyYJOdioy_fFjJzNtUDY1sVoSw8ltrJNjVHKencKGOodpHSp8_uLlRFoUzrcEEGz6Aqx0FaYj5-kbreue8PnBbogbTnsUcTYGSJP64dfXrdzclky4PIM-W1wH_X9D1q528NzlUTCPRQlMmjwenvpRJQh7pPmBAo_7Kx04kK0Rm6YfdPNWf9hkhyT9sB9A-9UFF9rk7b-o1vQI4fMnb2-h1vKmLH6oLuM2B-PYQ7aqCn0GW0DAwtE2OpC23CQKcQuCbssJicdAD5x_qW_cB2ZCUDMY6FkAA78OYpDc0fJskbU712bSa1aMndg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04697378e1.mp4?token=pQajDtLlY_2VuWuwbseMABwA_8i0kIlyYJOdioy_fFjJzNtUDY1sVoSw8ltrJNjVHKencKGOodpHSp8_uLlRFoUzrcEEGz6Aqx0FaYj5-kbreue8PnBbogbTnsUcTYGSJP64dfXrdzclky4PIM-W1wH_X9D1q528NzlUTCPRQlMmjwenvpRJQh7pPmBAo_7Kx04kK0Rm6YfdPNWf9hkhyT9sB9A-9UFF9rk7b-o1vQI4fMnb2-h1vKmLH6oLuM2B-PYQ7aqCn0GW0DAwtE2OpC23CQKcQuCbssJicdAD5x_qW_cB2ZCUDMY6FkAA78OYpDc0fJskbU712bSa1aMndg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیر قلعه‌نویی: بازی‌های با کیفیتی در جام‌جهانی انجام دادیم و از بازیکنان تشکر می‌کنم که بخاطر مردم ایران و شهدا جنگیدند
🔹
ما مقابل مصر بیشترین امید گل در ادوار مختلف جام‌جهانی را داشتیم و به نظر بنده گل شجاع صحیح بود. @Farsna</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/445865" target="_blank">📅 19:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445864">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skpjsAKj88idGehLndgelZp8Bdu3Zo_M0k3byHKw0-gKeSp_feww-SIhtqbnluPCP0DsEBQI0E70blaZMqfv5eHqxlnLSC2DsewoeAR1DPJs_4qxY_j2ucWRK3xq8-PNo2Oyv48ajV8BcUHEpY1SCiCX5L-owxdkdjGRS2MmpcCyp-JQ5mHqmdOp50NyIUZBlAK5Q-FwUb_yYj8njm5HYmOwXOGkrGRGJCqRHK5rWX2Zh1KIMso_VPHtyMFygelIookDEJaiLHKUlDGAEpoRVs38xgekUq88tt6MNa3rpsDy0kW2GIN9NAaE-s0ajgww5KH-I54mr9opIghkVB1dcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار نمایندگان آمریکا در مذاکرات با امیر قطر
🔹
دفتر امیر قطر در بیانیه‌ای گفته ویتکاف، فرستادهٔ ویژه رئیس‌جمهور آمریکا و جرد کوشنر، داماد ترامپ، امروز در دوحه با امیر قطر دیدار کردند.
🔹
در این بیانیه آمده که آل‌ثانی بر تعهد قطر به میانجی‌گری بین ایران و آمریکا تأکید کرده و ویتکاف و کوشنر نیز بر حمایت ایالات متحده از روند دیپلماتیک تأکید کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/445864" target="_blank">📅 19:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445857">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/irhcVpr8p-qjGKGhEoqt9AWxHGW8QL7cXjeqajzWeKuoa5EglLldAyiMYX2Vfar9WkSOkz7TlLWdnH5xiuGM4AKkW-qYXjXaTbdJk-GUzEnCeuG9X0OixHgyM5IUWjac3yd5dot5m1HUwHvNHuiJJ9f2uMsXLwwT2UpZHGWobtLORSJtSMOpBzzpUim09y8fKG9k2IgeSJkBHkIKkgi9goJrJF4bqMwo6irvO9HLtO7IzxYcwgijI7PscH4QXhHd52Ju--YiLgxpFXxZLy3--aRwp0l0EdUNnYxx4CuIXgnt1GR1CwF59lEB2SCpl8Oah0MeNIe5O-FjhD49I-T0OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vt_asyC7tGZtNglOt_tbrfEsV9eL3or9U3DvSgbCUVRlawivlhiv-w116_feYMLR-cB9Qe0AJepUszYS-UYuxYuJTCpHBz3-wiraJdaxHqLhcktwP7WvvWq_xFVF4RK2JrbZU8_ITVW-xNuO3YJFYcZLmh2_HUdk5lea5rs0ft3sQg8ZF1iom_t1kDXJYEKtHniQ4DonMpHpnJtnUs4wV2YjYgTWtaGV08xYsz19eFYYe-RZW9X5QMOkoUWjL2ETm09sC0NJ0WkZGYCUnZCJfrG_w3SrzawLrpXrUGuVjyn46c5WDtBc7Yo40kO4i1zwIFpXJXq7-M_9iOeOsMTudA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gHmNmNWEoAt3gBb97Q0mUvzUPzunnTOU9y-vGyyzTV0G6qbvGKVrR7uxuAL46JXd3chNNivCfd6dlT64V2ebIhFCk4ZPYtKKQ7fowombTfKyYVtv0ebYi-eT5knhcVaQQJpHS4YAeAC-Z1K7zEbZYC5DGKRQU0DJn2b4bS9sCWHCrB8d_BTCacNU00O_WVa2sXvZCrkdWecX1VKmKAlO5zESes_jdOY6P3juHV3uPOAplt7twhgqij4W1Ete27pSBlRj4bcTGFrBrGgq84pz0v2p8JB7wany3cQHJEwj2x3IdNwQb7pn0_G1dbIOQq6mksnnq9pObRm6vT61dpt_Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h38_FjK4P4MQvKa8IeadMfBFl9xpXNjktqLPCP2_aO7itPIgT07itrGPQe8eCaKRLFFyi5xKaaVx7KIuj-5AQEgKCXTTj8OP7rm5i2-kGIZ7jlQgrTi0lr-h8-USh3a_cX8vx29gQhk77nZ4lWlTj0TLf9IpsUxMlHuH6y1qkyNk85FvkG_gCh2GNXry7DPOP277Nv9V4sDKMu6A5-cDhd57s8fffMoxWpQ4MDvYiR_VgwiQB_0QNTNX09qxllWaJgvWuXNkR3ikY4Wt66f_eAPFkMHRoYoU1erSADkNGPIPGPyoWMbEGtYXGrZ9UtknnPs8oeicEQnMuJNRt9Offg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DMvRvozwHjwRJoOvqRCLmZVWCt5vqbQYn8mY3wHW6oZwaWwN4vuPFt81StKZ6EuJVg2lPXAzteARb27oPnG8U_BDyhUZ8qk3QVoEQmZLWn2y7OjiVwYFVXXvvRRD8dU9ymRdNqZHXHiOyrrV20Aybe5jCti-OxmdajDfvRB9bxTU0g09VzuKbWK6veuPA13Fpp92-stsJF-XJ1fxabHmDedStkazfq7ACvtxh3A4oXNRicnrLU7K2YD1PfJF1RTgvocHcf04lsJE9ZikmS0fbBCcoYsa0npg53T1noAZU1DtGopWpojAWfeto20xeQjD1NRVvblar5CiMjR_4ZeHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DSRjo0-zo3oADj7Wkvcx-i1_lCkKx4_KWvOqIL1hwN4QZPFtcBI5RlKcaK0jPV6i4VyROJvGVcPXaI6LZRcCPknjJwv99Fzl9vJJ1PuigI1yaqWwGHkVpYc1bJBmzZEwhrznRTGsQK8l1VV2zarwN5CHAlnyjgZFDzp7cUzyq4OxdNUnwgXd7Ny7p-4In0BYt5aDOy9FIpgJovvvENBF6LWyxiaPhxAb7ly4LThpB2wR9js53m2G8vp1nS4DdDnNQxd5ORSibYeGKji7AIjGDzShdGkzBWRcoU1qfch5T0KO2XT_zB5C-jXJGayOGoJ59OYMNda-wevpcyXM2pf4wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ggZZfeWa9d5hVEHQth64P_MMit8yJ5uvS0MF6yoDk4xWG1XgQy5Sb3JEsFKlOwOnrXvtyrs5mhMBF5UARYru0UTov1KhkLPL5qdn4RNahgBlfO09RMS-43aPePWgiw8haPs40OXY0vOjgEcl9O1aK94Z3RVe9ctkhk43yQkoWrs9go9zksUVnr7xa-7x-MJE4vDIpw-0mU8Q-giGudG7ukKj8SjBkQVYqxPAix5zoc54xwcgjtfga_L0sR44Z2iezbUVS9ae6eldu-opcxPXYSGtjwBoIWjD0XZZ92XRoAdCsRKNSz7CKGkoM1fhglZ1_9q7OOaOiCncg7vU_jG7Mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
کاروان تیم ملی وارد تهران شد  @Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/445857" target="_blank">📅 19:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445856">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae791b304c.mp4?token=ksjgWSG_aSTQMzZAwwIHbXCpmK1HZESE7VGYeZZOCPZue3qh-ytwSq0YXLg780YtgS6LWPrZdSOeDo8tNUczS0ad4a8b7KT5bEmL3CBBKe7YHuVEcch27hMMm6LLST3qjEd_PW4lA2Wymhbx_J1HavKB0Oygoa_xX5OtVgxKThkYwt4rofSt5i5UhCZ7vJskmreM8Le_8qRVfM2njPX1Ao9buZyyHJyp2wBe5iXg5K0jcVAsseWiBUo5DOQCQBrRevrEi7pKOhk2sll0d3kVbd16HBy07G7Gy_RBJ1V-qjkdM6rk6WaSL35agRFCkrEqeN2Vz3i-0tuoKPB-5VA0qisNMZ7yqPSlYewW4T4llREVErQ9pIEtXLS_3V-zeHVIlNejSw7i9Vo1ASEfOoFJIVDewCO5NJU2GSsY75nmL9Kq_DnXI36gDt4qq7z21GMe5C9yueo_nAmLDViZxQoxf04yzqozlLq_nz-_r8zPl3nWNy8ziTOsNqMCUyDsZAY5emnv3dkSsEde6rxQMGJXT4yQ7qrFvOnfa9FfJ7az0nC3V3kSr8JI99hvyDDkLmq5GO3Het9_9eamPDK60gHZaS-ZBbx0RoVuoSqOOT4thpDSp3YMchpRk0jkXlHEv1tQMg8gbgKUv61Rr__Mi67OMLUcoHSkKpBoHUvmrQye56M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae791b304c.mp4?token=ksjgWSG_aSTQMzZAwwIHbXCpmK1HZESE7VGYeZZOCPZue3qh-ytwSq0YXLg780YtgS6LWPrZdSOeDo8tNUczS0ad4a8b7KT5bEmL3CBBKe7YHuVEcch27hMMm6LLST3qjEd_PW4lA2Wymhbx_J1HavKB0Oygoa_xX5OtVgxKThkYwt4rofSt5i5UhCZ7vJskmreM8Le_8qRVfM2njPX1Ao9buZyyHJyp2wBe5iXg5K0jcVAsseWiBUo5DOQCQBrRevrEi7pKOhk2sll0d3kVbd16HBy07G7Gy_RBJ1V-qjkdM6rk6WaSL35agRFCkrEqeN2Vz3i-0tuoKPB-5VA0qisNMZ7yqPSlYewW4T4llREVErQ9pIEtXLS_3V-zeHVIlNejSw7i9Vo1ASEfOoFJIVDewCO5NJU2GSsY75nmL9Kq_DnXI36gDt4qq7z21GMe5C9yueo_nAmLDViZxQoxf04yzqozlLq_nz-_r8zPl3nWNy8ziTOsNqMCUyDsZAY5emnv3dkSsEde6rxQMGJXT4yQ7qrFvOnfa9FfJ7az0nC3V3kSr8JI99hvyDDkLmq5GO3Het9_9eamPDK60gHZaS-ZBbx0RoVuoSqOOT4thpDSp3YMchpRk0jkXlHEv1tQMg8gbgKUv61Rr__Mi67OMLUcoHSkKpBoHUvmrQye56M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تو رفتی و با رفتن تو ایران همیشه بی‌قراره
@Farsna</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/445856" target="_blank">📅 19:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445855">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a90331c2eb.mp4?token=CAWXZU1DAOnMnVNjGbx1VKEBWNTq2VP1dXRpgJqNfF3UB4sTeVQl5vYvLc1H9Fo3gzHfdbZhXx2-TmM38cj3Fwd51tOY8wGQvmTgNlxAkL-ulFq2IuzHzCXwCDORuUpJd1D2uq5sTZecV1BDZtzerk64hsQQMDt456OqHO5omjLpcC8JvgIWNlV7aEXU1mT8__qduTO3t6A9TeXys1TRGOOdyy7t50W1BrtJmbahrksKdfjRLUkM1rIu9KatucwCS7HiDTJzb0Gv8-sZTPp-clSkOb7-cRrdYYAw08hCafU2y1mHn5c62l32r0wmrinat7Q3pAvtAYVaKUBGsfOMag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a90331c2eb.mp4?token=CAWXZU1DAOnMnVNjGbx1VKEBWNTq2VP1dXRpgJqNfF3UB4sTeVQl5vYvLc1H9Fo3gzHfdbZhXx2-TmM38cj3Fwd51tOY8wGQvmTgNlxAkL-ulFq2IuzHzCXwCDORuUpJd1D2uq5sTZecV1BDZtzerk64hsQQMDt456OqHO5omjLpcC8JvgIWNlV7aEXU1mT8__qduTO3t6A9TeXys1TRGOOdyy7t50W1BrtJmbahrksKdfjRLUkM1rIu9KatucwCS7HiDTJzb0Gv8-sZTPp-clSkOb7-cRrdYYAw08hCafU2y1mHn5c62l32r0wmrinat7Q3pAvtAYVaKUBGsfOMag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان هواپیمایی: روز دوشنبه، هم‌زمان با تشییع رهبر شهید انقلاب، آسمان تهران به‌صورت کامل بسته خواهد شد و هیچ پروازی انجام نمی‌شود
.
@Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/445855" target="_blank">📅 18:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445854">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/190e4c608b.mp4?token=glHXTdFM-cLn3YLMSYKozIOsboR_CjPtrnxPxiMCbWhCll_7UZY_IOEbdhMZT0nnrwAvzULCFsDKBgQa5Iefmct5lz9p_LIf8evU3kBMERuy1QdPK0r3ax0kf2tJZgKO3OfUv1VZHgR24-lDAPHwKcDr64iLMqIjk0dSDPYRhCDCRlHOkYkZmvN9KayrlhXkSOPjT3ZdL433bmNxF40z7SkVT7sV6996WWFMClzEP3-lsdgjXo9Wx8GyfMJ89_TaaEDvk8-GW8YJ5tO1rzmkNB_VL7SLs47d7j4Ni9AsMN2sXepZArlp_wZaFJYNFtjBuLm1RtHvqBCSskrxrh7dGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/190e4c608b.mp4?token=glHXTdFM-cLn3YLMSYKozIOsboR_CjPtrnxPxiMCbWhCll_7UZY_IOEbdhMZT0nnrwAvzULCFsDKBgQa5Iefmct5lz9p_LIf8evU3kBMERuy1QdPK0r3ax0kf2tJZgKO3OfUv1VZHgR24-lDAPHwKcDr64iLMqIjk0dSDPYRhCDCRlHOkYkZmvN9KayrlhXkSOPjT3ZdL433bmNxF40z7SkVT7sV6996WWFMClzEP3-lsdgjXo9Wx8GyfMJ89_TaaEDvk8-GW8YJ5tO1rzmkNB_VL7SLs47d7j4Ni9AsMN2sXepZArlp_wZaFJYNFtjBuLm1RtHvqBCSskrxrh7dGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام میرهاشم حسینی: دشمن اگر بفهمد ضعیف هستید به صغیر و کبیر رحم نمی‌کند
.
@Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/445854" target="_blank">📅 18:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445853">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e519ac5c01.mp4?token=LepF4IfuGcq2J8vCYIiwJrEkoz_leRXR8tCac597BuAXaxuO-T3jXNJhltLrLHmUloSsAOi4sEOQsYoshvD6ke6OO6vpAVzfN9MPaBVQewHlCM-AUqJi5FxrtOaZvogdyxgj64Gh1N73YpnT00F5CivWMPfKxUkSrjSDTT5-YZHVRh6c5qEZi_pMaNxuwLmQj7k2SW6K09JU97mfLgTLqAlHBeEGRmvOoERQdMqJjNUduKF7XPUrgrSipxfD0sbXaZd6FZ66Q5-LNxBT12n5Up_nokfQeSg-jQz3QQbvkz8pKcUg5cjChROx9GyuHoxQgIo4gunXxFX7hvi6X-HS_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e519ac5c01.mp4?token=LepF4IfuGcq2J8vCYIiwJrEkoz_leRXR8tCac597BuAXaxuO-T3jXNJhltLrLHmUloSsAOi4sEOQsYoshvD6ke6OO6vpAVzfN9MPaBVQewHlCM-AUqJi5FxrtOaZvogdyxgj64Gh1N73YpnT00F5CivWMPfKxUkSrjSDTT5-YZHVRh6c5qEZi_pMaNxuwLmQj7k2SW6K09JU97mfLgTLqAlHBeEGRmvOoERQdMqJjNUduKF7XPUrgrSipxfD0sbXaZd6FZ66Q5-LNxBT12n5Up_nokfQeSg-jQz3QQbvkz8pKcUg5cjChROx9GyuHoxQgIo4gunXxFX7hvi6X-HS_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم امام رضا(ع) منتظر مهمان هرساله خودش است
@Farsna</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/445853" target="_blank">📅 18:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445852">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9732fd13.mp4?token=n_dU34t8gxPyIFbo7GbSnjmVmVJ3wRVpK1koL0IuaJ-CQqJ3abAhg_sWKUndK9gwo-iBapy7cAg7s051NHjzDnFkBQLEmgIznRdHg8qe0APIxM5T4iRQ3y134fQSwPhZAfWEAoCJPlw9KZp31dPtNgWMTWYAi77Yw3TTejXtdSFLBK87jrgk-KlOdNiEUlbvwWwaLoZWrRBbFY7o1QTPdoeQh2keiKcwJ7NRGDfSj2LnlrHyMLaeYhsCVooxiZIu9e2GCXm-nsl4BjAcGxHEJuFYjWySIquC697FpMKiJOXmy7ebyFvNIhg2u5f0ZGr2r0ym40ntPsXrRXMscNL0fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9732fd13.mp4?token=n_dU34t8gxPyIFbo7GbSnjmVmVJ3wRVpK1koL0IuaJ-CQqJ3abAhg_sWKUndK9gwo-iBapy7cAg7s051NHjzDnFkBQLEmgIznRdHg8qe0APIxM5T4iRQ3y134fQSwPhZAfWEAoCJPlw9KZp31dPtNgWMTWYAi77Yw3TTejXtdSFLBK87jrgk-KlOdNiEUlbvwWwaLoZWrRBbFY7o1QTPdoeQh2keiKcwJ7NRGDfSj2LnlrHyMLaeYhsCVooxiZIu9e2GCXm-nsl4BjAcGxHEJuFYjWySIquC697FpMKiJOXmy7ebyFvNIhg2u5f0ZGr2r0ym40ntPsXrRXMscNL0fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
مراحل آماده‌سازی مصلی تهران برای وداع با پیکر رهبر شهید  عکس: محمدمهدی دهقان @Farsna</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/445852" target="_blank">📅 18:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445851">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9mgt5d2XL2gysbZH_UGNcyoClXt5ACDamq1vfyxhL6W0ZQ41m7z-WaIUggSha82qTZIKPka-Y98Ha4iQOR12aOrspwY24TTiYdYz2JC0hqxxzki32LJdGLbxzHskAZmxkloEpXDwKTFbSljH_ZdFUcj-PXR1P3I-ua7sn1mLrFlXPT8w7Rla2l8d43OaPCBYvY-GauOHgBLJs-fjcLMyIjvuoFRulPx4gL7Ci9KJWfYZXID1aZMLSG3t0RmWNFfpA_IK-1TPZTitvyBpv25Ku3QTeRowjPrx503_nYr_4Aaj24GnHMCwXy8jD9BTLPNy0YqZrjzVLM7Xxajgl7BgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گسترش حضور نیروهای چهارگانه ارتش در سراسر مرزهای کشور
🔹
سخنگوی ارتش: در حوزهٔ تأمین امنیت، نیروهای زمینی، دریایی و هوایی ارتش، حضور فعال خود را در سراسر مرزهای کشور گسترش داده‌اند.
🔹
نیروی پدافند هوایی با رصد آسمان و کنترل ترافیک هوایی، امنیت کامل فضای کشور را هم‌زمان با حضور مقامات و شخصیت‌های خارجی تأمین می‌کند.
🔹
در محور خدمات رفاهی، ارتش ۴ زائرشهر در نقاط استراتژیک تهران و حومه تأسیس کرده است که از فردا عملیاتی می‌شوند.
🔹
یگان‌های بالگردی ارتش در آماده‌باش کامل قرار گرفته‌اند تا علاوه بر کنترل ترافیک، خدمات اورژانس و پزشکی را در هماهنگی کامل با سازمان امداد و نجات و هلال احمر ارائه دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/445851" target="_blank">📅 18:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445850">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bf4xcnCzYzpzacwztSEemYP0RRSyO2STJ2GUwNoT6-AdVvLKy5SV8wbfH6YZOsMqWnl4SNfAJ4i_qHX-obXghTJLc0hSmu8eaVov4UAqlIyJCfGMMd4c8Q_ODiDOy-3QFavfs2zZd_uOhaT6m7il4DFH4yt2J29xqJNjDrxY3up8vGiJgEsIAMaKtM-K0x5KbAGTvxDy7g7cFIoUtNqec3OeN2K58RsLDg6mxH9rSkn_6Mw3zK1E_o4AT6k0JweqN7XYA3rubRqGfXLABUT1WfaJA5icDDQQ1_TWzUuLKxCTQysqsM-wxzjF9qTST_t0tuzkEj_E_50XO4hHQhUqZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
همۀ آنچه باید دربارۀ تردد در مراسم وداع بدانید
@Farsna</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/445850" target="_blank">📅 18:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445849">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UeKYo4ii6aWEbq_uav9N-Qyz6fZsdjSEtlqhmcgrKcnxAYas31_I4F8iQ5pHNFjQLsZtm_9P9yc-rS94OV8J0LuhXnNBCnEHpSV--FUJ2eB_qko8kftpWf3pq04ELp1EkAckx8DiDM1FyI2MHJORgecTQQfPFcyPY1j4EMl1l0Vn18gdOgE9qLdhmdfNm-MMzGuMixF-FRgWkxLAqDCj5foVpFiORWK7Yu36HDXYZuAU68kN1umQqi8dAxH1fYVVMfrYySXCV_CT3Ri-JQ_dinX3JDFdR_lSGryg8hQ2UQWEXqhdUYYTtWJOyrcS_RTdP7PzE2y-iPsvzvin877Byg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حضور وزیر امور اقتصادی و دارایی و با برگزاری آیین تودیع و معارفه
افشین خانی مدیرعامل بانک صادرات ایران شد
🔹
با حضور وزیر امور اقتصادی و دارایی، آیین معارفه افشین خانی، مدیرعامل جدید بانک صادرات ایران برگزار و از خدمات محسن سیفی، مدیرعامل سابق این بانک قدردانی شد.
@Farsna
- Link</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/445849" target="_blank">📅 18:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445848">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cp_ygxRzDYbS-uXlfpaXpmse8YqErFY7dlaVyEwnkLS1-IlS_Ob8y1M_FimXDu9osu97uzvsZ78nr0I0YP6pQXlllEiMAmfzWYDu5dSh3isYBLZXXxKY8lN9Xdphj9Iq4TG9YFzF0mPL2Q1As1xnK9ieiUO1A89NlzpXlxIS8O7hmDiJo4jYay1UXMj1OP1gZRM8iCm8AL-xwJMu8vBUCLOUMB_IRFZcVOBouUPYWkFEGYzewwPIkim-PJa0lsvtXlTTNPQUrIx16U7wHbwkBJLdj4jV3eOqBnZKQs2Ffu6x_JpzBCZhSpEtxlcjC6Pj-xE79n7_Yx0XcvFIaq-UFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش روابط عمومی باشگاه چادرملو اردکان، امیر سیدین نماینده تام‌الاختیار مدیرعامل گروه معدنی و صنعتی چادرملو در باشگاه، شایعه معرفی تیمی غیر از چادرملو اردکان به عنوان نماینده سوم ایران در آسیا را یک شوخی بی‌معنی خواند.
سیدین گفت: در چند روز گذشته شایعه شده که فدراسیون فوتبال سهوا یا عمدا تیمی غیر از چادرملو را به کنفدراسیون فوتبال آسیا معرفی کرده است. ما این موضوع را یک شوخی بی‌جا می‌دانیم. مگر می‌شود فدراسیون اصرار بر برگزاری تورنمنت سه جانبه داشته باشد، ما را مجبور کند که بدون تمرین وارد مسابقات شویم، چند بازیکن مصدوم روی دستمان بگذارد و در نهایت بگوید این تورنمنت بی‌معنی بوده و تیم دیگری قبل از همه این ماجراها به ای‌اف‌سی معرفی شده است؟
سیدین ضمن تاکید بر دفاع از حقوق مردم اردکان و استان یزد، افزود: شنیده بودیم که در بخش مدیریتی فدراسیون فوتبال، ناکارآمدی وجود دارد اما این شایعه اگر درست باشد، فراتر از ناکارآمدی است. مراجع بالاتر باید برای سیستمی که حتی احتمال رخ‌دادن چنین فاجعه‌ای در آن باشد، فکری جدی بکنند.
وی تاکید کرد: مطمئن باشید ما زیربار چنین ظلمی نخواهیم رفت. مطمئن باشید اگر فدراسیون حق چادرملوی اردکان را ضایع کند، نه تنها از مراجع قانونی داخلی و بین‌المللی پیگیری خواهیم کرد، در مورد ادامه حضورمان در لیگ فوتبال هم ممکن است تجدیدنظر کنیم.
سیدین در پایان تاکید کرد: مطمئن باشید نه تنها مردم بزرگ اردکان و استان یزد زیر بار این حق‌کشی نخواهند رفت، که کل مردم ایران، چنین اتفاقی را به عنوان نمونه‌ای بارز از بی‌کفایتی مسئولان فوتبال کشور به خاطر خواهند سپرد.
@Chadormalu_Sc</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/445848" target="_blank">📅 18:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445847">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/445847" target="_blank">📅 18:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445846">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e91b590aa4.mp4?token=veVTYCxWg0oOVVw4b9rhOYTaD9K6QWPf4w4oq3gOK8R0RwDNtaZlj-A616taUnys0LdbTQT5e_scGxyehgBpRprhgcYcG6OOAtU_k2xf2q0ocbsWnvCWeV14GtfmXEg5M1LZSFW1c5P4kE1m7R0rmz48CLZ1vtEpyB5uM_bR2LNI9QFAKpxD0kgZ-gL_mMat3C2q2gW97MkOxDxxF-CypsLineWQ9BuDMdwjVmjhUinxFkCKyGezD2YIVDKHdgTs232yxLAOBd0A1VtDXFXTVGAvswiK8whCXAcR4QmMCOI1Cv73-qHA2Jnhk7NpFOIrDw8Lp43wu8hYh_hFByDNZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e91b590aa4.mp4?token=veVTYCxWg0oOVVw4b9rhOYTaD9K6QWPf4w4oq3gOK8R0RwDNtaZlj-A616taUnys0LdbTQT5e_scGxyehgBpRprhgcYcG6OOAtU_k2xf2q0ocbsWnvCWeV14GtfmXEg5M1LZSFW1c5P4kE1m7R0rmz48CLZ1vtEpyB5uM_bR2LNI9QFAKpxD0kgZ-gL_mMat3C2q2gW97MkOxDxxF-CypsLineWQ9BuDMdwjVmjhUinxFkCKyGezD2YIVDKHdgTs232yxLAOBd0A1VtDXFXTVGAvswiK8whCXAcR4QmMCOI1Cv73-qHA2Jnhk7NpFOIrDw8Lp43wu8hYh_hFByDNZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیرانوند: دست‌بوس همه‌تان هستم و شرمندهٔ همهٔ شما شدم  @Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/445846" target="_blank">📅 18:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445844">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a161d99d.mp4?token=Jdt2dd2p83oW1a0n1gFRNoKuw5JflQeUQPqOfnHid5rM50IGoda8l7ZnwzEHBN89J1Yklw0fmeV7vibSYR2yyO2riFuIXoXI39ZvecEOz8AYKeVkOSdeeHFPY2G1KppZKzO51a3abYwFkX84cyUt4jsOWNeMSRHnUNnrEFCogXYk38xLlF4eiFrwZvHzxzpYMkQ05xBPQZZAiQ0s3quH9bwleASRbIpB7VYD_eTFmWpzHm2EH-HVs4f__cFoS9KSd2RNu05b768ZZvuEeYxLVf8AJld0PH6aiUC0odq_iNkZAVJqSRibwZ4sE4KNq2Vgs1vbeLYMBRIKZR11Pfi2Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a161d99d.mp4?token=Jdt2dd2p83oW1a0n1gFRNoKuw5JflQeUQPqOfnHid5rM50IGoda8l7ZnwzEHBN89J1Yklw0fmeV7vibSYR2yyO2riFuIXoXI39ZvecEOz8AYKeVkOSdeeHFPY2G1KppZKzO51a3abYwFkX84cyUt4jsOWNeMSRHnUNnrEFCogXYk38xLlF4eiFrwZvHzxzpYMkQ05xBPQZZAiQ0s3quH9bwleASRbIpB7VYD_eTFmWpzHm2EH-HVs4f__cFoS9KSd2RNu05b768ZZvuEeYxLVf8AJld0PH6aiUC0odq_iNkZAVJqSRibwZ4sE4KNq2Vgs1vbeLYMBRIKZR11Pfi2Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال از ملی‌پوشان با نوای سرود ملی @Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/445844" target="_blank">📅 18:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445843">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d2d06daf4.mp4?token=PVyseZ0YUnIyp-QZGcGeDpFP35yEs25MqH_1q60nzbeVeBYjHQAJO693aS43xvc3pa_XRD4Ig21IreO-Z97HHhPlIB-u7Beel8aVZCuD0_BCEORCuvimRy9I-8nL1ji7tmGrAhYjgiuH7b2moSqM337LVoslvLSwKh-JiiG__9Ji3s7Q156LvilYXlaY3vVpVf_R36NPL-QGnbyAF5mHlK7HxebI0OFJZi8yRlhs2w7arsiON-OFEaXzQp_LS3HtYGqWt0DuGgxkiBcknz0U7tCbg1xTSjtRxXDStsVzlIwRjSR-wz-EeECQBLtVk9r_flTAvwBGVy2VURjihEivqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d2d06daf4.mp4?token=PVyseZ0YUnIyp-QZGcGeDpFP35yEs25MqH_1q60nzbeVeBYjHQAJO693aS43xvc3pa_XRD4Ig21IreO-Z97HHhPlIB-u7Beel8aVZCuD0_BCEORCuvimRy9I-8nL1ji7tmGrAhYjgiuH7b2moSqM337LVoslvLSwKh-JiiG__9Ji3s7Q156LvilYXlaY3vVpVf_R36NPL-QGnbyAF5mHlK7HxebI0OFJZi8yRlhs2w7arsiON-OFEaXzQp_LS3HtYGqWt0DuGgxkiBcknz0U7tCbg1xTSjtRxXDStsVzlIwRjSR-wz-EeECQBLtVk9r_flTAvwBGVy2VURjihEivqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال از ملی‌پوشان با نوای سرود ملی
@Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/445843" target="_blank">📅 18:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445842">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee4dc3b508.mp4?token=Ux7eHwAPYLG_9hole_HRws4icE6ifuvQHHQHy8nUwyViJqRIKUF2CQRljyRCvmceZSsPH3QuZacrB_povqxlD6s3PkNkzs5vuFok0RjeSgJ9l-cjQZlvQLbUm_gt8NGEvsSBet0CcCme_TEDKi4y_0MhVr91ZXJl6mPzu5y44CKADYTIYApMK_eRhgZibRsWqMLb2WmCXrvlsX5cv3u7jW4bPXdtbcLNsna1iFVfQFqs3z4cqMRvdJohJtXme7jhyql5_FrLVuhjxDH1MDz0NDUGQcqONxh57EExVY09KodKFSf4z-7ljVYT_aTxo7eDYrkgW1YeCMiSLgzGcNfNrDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee4dc3b508.mp4?token=Ux7eHwAPYLG_9hole_HRws4icE6ifuvQHHQHy8nUwyViJqRIKUF2CQRljyRCvmceZSsPH3QuZacrB_povqxlD6s3PkNkzs5vuFok0RjeSgJ9l-cjQZlvQLbUm_gt8NGEvsSBet0CcCme_TEDKi4y_0MhVr91ZXJl6mPzu5y44CKADYTIYApMK_eRhgZibRsWqMLb2WmCXrvlsX5cv3u7jW4bPXdtbcLNsna1iFVfQFqs3z4cqMRvdJohJtXme7jhyql5_FrLVuhjxDH1MDz0NDUGQcqONxh57EExVY09KodKFSf4z-7ljVYT_aTxo7eDYrkgW1YeCMiSLgzGcNfNrDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان تیم ملی وارد تهران شد  @Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/445842" target="_blank">📅 18:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445841">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حمایت ۵۰۰ دانش‌آموختۀ دانشگاه امام صادق از بیانیۀ خبرگان
🔹
جمعی از دانش‌آموختگان و دانشجویان دانشگاه امام صادق (ع) با صدور بیانیه‌ای، ضمن اعلام حمایت از بیانیه اخیر مجلس خبرگان رهبری، بر فصل‌الخطاب بودن نظر ولی‌فقیه، ضرورت تبعیت مسئولان از رهنمودهای رهبری و حفظ انسجام ملی تأکید کردند.
در بخشی از بیانیه آمده:
🔸
پس از تصریحات مکرر مراجع عظام تقلید بر لزوم تبعیت محض از ولی‌فقیه، این‌بار خبرگان امت در لحظه‌ای تاریخی ما را متذکر شدند که نظر ولی خدا را مباد که از جنس یک رأی در کنار سایر آراء بدانید: «در نظام ولایی نظر و دیدگاه ولی‌امر فصل‌الخطاب است و پس از اطلاع از نظر قطعی ولی‌فقیه هیچ مسئولی نمی‌تواند و نباید بر خلاف نظر ایشان اقدام نماید.»
🔸
«ما شاگردان مکتب امام صادق(ع) ضمن تشکر از این تذکرات گرانمایه، حمایت خود را از این بیانیه سترگ اعلام می‌کنیم و از ملت بزرگوار ایران بابت ماه‌ها حضور در میادین دفاع از ایران اسلامی که اثبات کردند انصارالولی به معنای واقعی کلمه هستند تشکر می‌کنیم و صاحبان تصمیم و رأی و مشورت را انذار می‌دهیم که در این میدانگاه مبارزه پیچیده با شیطان، اگر نظرتان را همنوا با ولی خدا نکنید، محال است بتوانید مسئولیت تصمیم خود را تحمل کنید.»
🔗
متن کامل بیانیه را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/445841" target="_blank">📅 17:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445840">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsQcAQ3Ui6n0yGqrSPp94eqlGab6t4TqKfILQcyFSsrspMWTPh-um8uZhFSvXuVlF7-_hgECam-daVbhjO7QLB8QG_xHcrXaY2GNRY0G0yel_oAFUvxWq8A-KytM2dPhApuzXSMUkuEl3HCQ6iPmXyE7-2KgQpD43EmJ28UBWYL4WOjqG9FhWoQDsGq2TCn5bxjacWCE-OQZ4eA-Tl63LlYKpFBv6CuN_L0uRePZ1yAktHRPfQQEknuV6VdOofafEkln4sTuj51sf-0ilIP_nu8Gxng5UvOdkXXd-DfRqVtkJvy5_2WeN9m6iV8jGGNEO78EdDP5WSg070jCNn7wEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور نمایندۀ ویژۀ پوتین در مراسم تشییع پیکر رهبر شهید انقلاب
🔹
سفارت ایران در مسکو: دیمیتری مدودف، معاون رئیس شورای امنیت روسیه، به‌عنوان فرستادۀ ویژۀ ولادیمیر پوتین در مراسم تشییع پیکر رهبر شهید انقلاب در تهران حضور خواهد یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/445840" target="_blank">📅 17:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445839">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هتل‌های تهران هفته آینده نیم‌بها می‌شوند
🔹
جامعه هتل‌داران تهران: تمامی هتل‌ها و مراکز اقامتی استان از جمعه تا پایان سه‌شنبه با تخفیف ۵۰ درصدی، برای اسکان زائران و شرکت‌کنندگان در مراسم تشییع آماده خدمات‌رسانی هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/445839" target="_blank">📅 17:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445838">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd56ad542.mp4?token=flAn2m4Lw-0yqbY4TdjUz2XGvMB3SW4_YgQSZ9x-q1f2OaPHdj4KOf9rdwk7XRis0603_K1ZoSR9u7Z7Jlhk1tTtoXMhtX3Al1gU4AbKJy1iJOdeLxXdnsaHLfGZCEJwUBzAeRAE8v8k9Olmg9kXUv-hPr6KzIz4jjO_E4ZnHivLiTNaZDpNDU-v0V-YIxt8F38E7vKmDdmjhWUq2XeJcLmghAxl1I5ZrxOr8f-QQz4tBBiYtn3VOWF9qrgPi8JaLuLU25JJRZanXMsPcI8r3gjIyMfMvi8-HLS7UX0WJlvtfhw1K15f5yRGCHgFe2CdBkIO4Tl40Z5A-acV8BTWDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd56ad542.mp4?token=flAn2m4Lw-0yqbY4TdjUz2XGvMB3SW4_YgQSZ9x-q1f2OaPHdj4KOf9rdwk7XRis0603_K1ZoSR9u7Z7Jlhk1tTtoXMhtX3Al1gU4AbKJy1iJOdeLxXdnsaHLfGZCEJwUBzAeRAE8v8k9Olmg9kXUv-hPr6KzIz4jjO_E4ZnHivLiTNaZDpNDU-v0V-YIxt8F38E7vKmDdmjhWUq2XeJcLmghAxl1I5ZrxOr8f-QQz4tBBiYtn3VOWF9qrgPi8JaLuLU25JJRZanXMsPcI8r3gjIyMfMvi8-HLS7UX0WJlvtfhw1K15f5yRGCHgFe2CdBkIO4Tl40Z5A-acV8BTWDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان تیم ملی وارد تهران شد
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/445838" target="_blank">📅 17:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445837">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1a1c6c24b.mp4?token=TRB-GtHdtZ6K0PVH1OkMX7z_2MHFnsEzZXNNpRyngLfoRstaCyHm20jeCHlOI80CU1RggAlYZ5l4Tog63QG1_U_XtlHbEGnVaghBuzP0doiIB-STBaZQFBjoNeNwHbwJLS9juCWE7i_QuejhIC2nMNjQMhUMvKwoWZmAVSADcudQXAAtcliQUqkthiVqhabcwwrZ8z5PmQHmWzp1ggxnMBvqmqf0O7vrq4UlbHvCRFQ2MrfKZTaiphpq8oCtO3igeWHywblwQDklJQ8u46eh4tM1zNGj1vwsjnX6L-Gm6-0NzlktkNVL9IsiZ6tfN9PPJvbRmvwEPcdi5JFstnit9TpnObrR5GZTAl4Yw5X8a8D8vMLVq5hjhEBD8P1Uri-bmRH08Yb8Qlgtsw_YiPT5S8Nip365fRA3oWRsovJy0Zam5YAhi0dmEs4WVeXEN_aDgFFQGJDMufOn9dbNM8i43HTUKMU6eq_edyYIahHW9xBfyxh4nAVARdToEsMhXRBUYv5_TsgalZprucKJlXSuY8SL4uw6IUbVU2nI5tJuy6msQOW-PmlQBq-KAdPdOQxffJ4v85_Q7-FjmLsWdVPHClyxgP9UkzyOL54y_P7co7ZI5GMTOHORuZB9U05isPCgoZzGDJ1BUAhXXY3_RhuY-gLKkr5FRjV5K6bQU2RLSK0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1a1c6c24b.mp4?token=TRB-GtHdtZ6K0PVH1OkMX7z_2MHFnsEzZXNNpRyngLfoRstaCyHm20jeCHlOI80CU1RggAlYZ5l4Tog63QG1_U_XtlHbEGnVaghBuzP0doiIB-STBaZQFBjoNeNwHbwJLS9juCWE7i_QuejhIC2nMNjQMhUMvKwoWZmAVSADcudQXAAtcliQUqkthiVqhabcwwrZ8z5PmQHmWzp1ggxnMBvqmqf0O7vrq4UlbHvCRFQ2MrfKZTaiphpq8oCtO3igeWHywblwQDklJQ8u46eh4tM1zNGj1vwsjnX6L-Gm6-0NzlktkNVL9IsiZ6tfN9PPJvbRmvwEPcdi5JFstnit9TpnObrR5GZTAl4Yw5X8a8D8vMLVq5hjhEBD8P1Uri-bmRH08Yb8Qlgtsw_YiPT5S8Nip365fRA3oWRsovJy0Zam5YAhi0dmEs4WVeXEN_aDgFFQGJDMufOn9dbNM8i43HTUKMU6eq_edyYIahHW9xBfyxh4nAVARdToEsMhXRBUYv5_TsgalZprucKJlXSuY8SL4uw6IUbVU2nI5tJuy6msQOW-PmlQBq-KAdPdOQxffJ4v85_Q7-FjmLsWdVPHClyxgP9UkzyOL54y_P7co7ZI5GMTOHORuZB9U05isPCgoZzGDJ1BUAhXXY3_RhuY-gLKkr5FRjV5K6bQU2RLSK0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری مصری: آمریکایی‌ها با برخوردشان با تیم ملی ایران، ذهنیت متعفن و نژادپرستانه خود را به نمایش گذاشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/445837" target="_blank">📅 17:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445835">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRVLEB-4WPXDvVkVUFH0YUmxd8jLJp70xXW8KgcrThfvF3BzDMmkHq4IJYdpYUJzsPtIProNvGe62fYwBucxEwS_1Lpl-aui30Awb5alMCRSBYCDDktKaN71Ij8nnO3AIAtfplrAbs0gl0QIUoIFomJEYQZeURPbNgs7o0wbCMiCyjxkpEMkm1eF3xoG1SBiEaAzWhSSjVFl7SFsaa4mAdpKhmVGx_o4RBazersjFvAP1d7y44zkjDyIB9egMfTrf8KGwCUxs1F8Na4sc9oSwmkXEBgxBgvQnyymf26kgN-rKJZVpTktN4TXD0itd5zKNz2NKZWUEqVTR8BEDOxzPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان مأموریت اوسمار در پرسپولیس
🗣
طبق پیگیری‌ها اوسمار برای جدایی از جمع سرخ‌پوشان با مدیران پرسپولیس به توافق نهایی دست‌یافته. به‌احتمال بسیار زیاد او امروز، توافقنامه نهایی را امضا کند تا جدایی‌اش به صورت رسمی اعلام شود.
🗣
طبق توافق صورت‌گرفته، باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/445835" target="_blank">📅 17:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445834">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlVcZlkqCC8_YI50SCG8Jgu6zaM7zk0FujQWCf6efzWWcOrMX369t3Flc4PFWXr2-eTO8NFUYeV12TtRJu54t3qOqxO6exlKsV8mGV8KvADfSVS1L2mrrV3Qd413MeIMdQqSd7NJJLrIKI1KHmqfnuum_w-_1I5VxwVYQDrSSsxxMytHbJNOElFzaFMwyr8qjiSdoz1IacJEfWDw2EDnBHNKVd-UzOo52n6t8P7j9jnQpuGisrYa-0chkkDyEKgmWUGb6PwYCjjH9-vTJKTCG78n7hOD6dXl0oXYrTqJhZmN3_V7gNQG3A0V3JmSGuq1vWRwU9DY5dew8PaRxLPVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه حبس برای شکارچیان خرس سبلان
🔹
محیط‌زیست استان اردبیل: متخلفان پروندۀ اتلاف خرس قهوه‌ای در شهرستان انگوت به اتهام ارتکاب جرم علیه حیات‌وحش به تحمل ۲۱ ماه حبس تعزیری و پرداخت جزای نقدی محکوم شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/445834" target="_blank">📅 17:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445833">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34bd0aee9.mp4?token=KxzR56TwXr9IOqJVe7Bpv63UP_W2WA8-lozip3ZlDtN2Xsh7Mu1kyNUu58GvGmMTDYpbn_srJ4fDEi6ocU4EueneplgSnHhrl7L4l7co0cGrFCP8rm2VW-Vfr-hAYb4GudR718ijFLHdG2mgMMZFMEwAoBgs2IsDAzi4mzRWpoI9X16DXXV8Hfdm2uScfkZWzGJOEtOzaP5ZMHh_hDOOw8ySIb9glaMUvyG3cowTqmKQp-YoATB7UvCHkrUNJDfM9SYqv5ja4umXxDDXIbgH-Ob_CNMWE0y99qHcX9UUACv_TrJ4YxV43LagzT9_CMNb015ziN3N_pTleD-7HKMQ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34bd0aee9.mp4?token=KxzR56TwXr9IOqJVe7Bpv63UP_W2WA8-lozip3ZlDtN2Xsh7Mu1kyNUu58GvGmMTDYpbn_srJ4fDEi6ocU4EueneplgSnHhrl7L4l7co0cGrFCP8rm2VW-Vfr-hAYb4GudR718ijFLHdG2mgMMZFMEwAoBgs2IsDAzi4mzRWpoI9X16DXXV8Hfdm2uScfkZWzGJOEtOzaP5ZMHh_hDOOw8ySIb9glaMUvyG3cowTqmKQp-YoATB7UvCHkrUNJDfM9SYqv5ja4umXxDDXIbgH-Ob_CNMWE0y99qHcX9UUACv_TrJ4YxV43LagzT9_CMNb015ziN3N_pTleD-7HKMQ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غول ترکیه به دنبال علیرضا بیرانوند
🔹
میثاقی: بشیکتاش خواستار جذب علیرضا بیرانوند شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445833" target="_blank">📅 16:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445832">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5ffdd081.mp4?token=o_sOFAKbrYPfM2d4i5dxiLP8DVeyOQ1VI6JOt5JmBRdRlYK_Km8ShyVZzTqWyrymeUsfjiqh5dOfDxRO1SdrJbqihIYh5zZOLFIxswJ_3JNG3fMkTNWkYkBytRs1eWIjHHu88Ju-oPDFhF0qURrriddBLGceGp0y-8Hh9XmGW0Rk0fzvOa5sS7z08I445A5IotAlgk2zHhZQr_WMTkYEkgjLX6ceAYBsxIOszOHB70j89EHOzJR8eVtSBRVHCGgobO-9Tylm0k83GM9sgpOBO-iuDY-YsvJ0MLkqcP2Tahlz03KPW3uOqrx7UUH9XL1E6bbWNXHl6RXsOS2DuK77rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5ffdd081.mp4?token=o_sOFAKbrYPfM2d4i5dxiLP8DVeyOQ1VI6JOt5JmBRdRlYK_Km8ShyVZzTqWyrymeUsfjiqh5dOfDxRO1SdrJbqihIYh5zZOLFIxswJ_3JNG3fMkTNWkYkBytRs1eWIjHHu88Ju-oPDFhF0qURrriddBLGceGp0y-8Hh9XmGW0Rk0fzvOa5sS7z08I445A5IotAlgk2zHhZQr_WMTkYEkgjLX6ceAYBsxIOszOHB70j89EHOzJR8eVtSBRVHCGgobO-9Tylm0k83GM9sgpOBO-iuDY-YsvJ0MLkqcP2Tahlz03KPW3uOqrx7UUH9XL1E6bbWNXHl6RXsOS2DuK77rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر سابق روابط‌عمومی دفتر رهبر شهید انقلاب: آقا از ایران‌دوست‌ترین ایرانی‌ها بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/445832" target="_blank">📅 16:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445831">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCFeuHcIzLP8yMBJbrkHbZJ7fPCTrzulS1vQ3BUfdZNcjmi-BzSn0Jk1ARJO63YD5gaWlmDl-4NYLnzqBa94-U4aSk4OUXeAy1tu09XZLK1LAMpBtFrRePsh-hgGtCRKINv758JMSCjjttQmyKVavNdrOrjX7PhqgvNT8vZ2vge23PcYm5kTvdexJxxR_ToMOJErnoj7aA3cK4iO3fbNgjynCpAt-HzZhFnBD3cpcBsmj6HE-LkzT4j31nt-XKb5KLkQvds8Rn9lzlZuP_qV9UVbDfDOELko_z-dC-xaMYTh-S1TAEmvyFzAdWEU_O68UGtABVgwfeU-j2ejJn0qWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات ایران ۶۰ درصد بنزین اسرائیل را نابود کرد
🔹
وزارت داخلی رژیم صهیونیستی سند تازه‌ای منتشر کرده است که نشان می‌دهد حملات موشکی ایران منجر به تخریب کامل مخزن اصلی بنزین پالایشگاه حیفا شده است.
🔹
در این سند آمده است که افزایش واردات و به حداکثر رساندن تولید در پالایشگاه اشدود، تنها بخشی از کمبود بنزین داخلی را جبران کرده است.
🔹
همچنین، مجتمع پالایشگاهی بازان در خلیج حیفا، بزرگ‌ترین مرکز تولید فرآورده‌های نفتی اسرائیل، تأمین‌کننده حدود ۶۰ درصد بنزین و سوخت مورد نیاز این رژیم است و در ۲ جنگ اخیر هدف حملات موشکی ایران قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/445831" target="_blank">📅 16:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445830">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTTafB_utTV07ERzOsN2M9tfmIzNKJD9zzZDinYNfon0Ulr8VgHEzcFMrbJdHKJ1800TCviFxRt3JLXGLz45figLWNqwTJ83lB2GR1btjxvryu-JoOFz50TtitghKTbNTh_KBjybJ_AI4Zjtza8FXJzkQf2GGpswTrs6C74-kcliSO26P5JNp073F9MtvyZj6DG0d5bYHOx5Sz-qL2Xw-LiUOGbQIbq9y8GSW9XrkLGiDXi9wtYO5OI1gRPqBH9ARvA6I0ccKtdaMexw-WP9JIzjyti54NXKhfguZBngiIyuOPMxen7W2dkFYHPfrxtv329UVn41Rr2G5C8i7yv0qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروندۀ استقلال در خان آخر دادگاه بین‌المللی
🔹
پیگیری‌ها از آخرین وضعیت صدور رأی محرومیت نقل‌وانتقالاتی استقلال در دادگاه حکمیت ورزش حاکی از آن است که این پرونده وارد مرحله نهایی خود شده است.
⏺
براین‌اساس باشگاه استقلال از طریق تیم حقوقی خود مستنداتش را به طور کامل در اختیار دادگاه CAS قرار داده و همچنین به طور موازی توافقات لازم با منتظر محمد، بازیکن عراقی اسبق استقلال و وکیل او انجام شده است.
⏺
در این مرحله هیئت داوری CAS نظر و لایحه نهایی فیفا را به‌عنوان یکی از طرف‌های دعوا جویا می‌شود و پس از دریافت پاسخ فیفا، رای نهایی پرونده از سوی دادگاه اعلام خواهد شد. رایی که مدیران استقلال به‌شدت امیدوارند منجر به باز شدن پنجره نقل‌وانتقالاتی باشگاه در آستانه فصل جدید شود.
🎙
یک منبع آگاه به فارس گفت: استقلال اين بار به طور کامل با ارائه مستندات از منافعش دفاع كرده است و مشكلی از بابت روند حقوقی خود ندارد. بااین‌حال پیش‌تر اشكالاتی وجود داشته كه هنوز هم می‌تواند نظرات فيفا و كاس متأثر از آنها باشد اما همچنان همه چيز در مسير خوب خود قرار دارد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/445830" target="_blank">📅 16:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445829">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اژه‌ای: خونخواهی امام شهیدمان را هیچ گاه فراموش نخواهیم کرد
پیام رئیس قوه قضاییه در آستانه مراسم وداع و تشییع پیکر مطهر امام شهید:
🔹
ملت مبعوث‌شده ایران؛ ملت سلحشور ایران؛ بشارت باد بر شما ظفر و نصرت الهی؛ شما که افزون بر چهار ماه است در سنگر خیابان، حضوری حماسی و دشمن‌شکن دارید؛ لکن قلوب‌تان داغ‌دار است.
🔹
او که به ایران اسلامی مجد و عظمت بخشید؛ او که محور مقاومت اسلامی را رهبر و طلایه‌دار بود؛ سخن از یگانه دوران است؛ سخن از نادرِ نَوادرِ ایام است. سخن از قائد شهید امّت، امام خامنه‌ای (قدس‌الله‌نفسه‌الزکیه) است.
🔹
اینک، نوبت وداع رسیده است؛ وداعی با اشک و خون. همانطور که شهید سید حسن نصرالله، شاگرد ممتاز مکتب امام خامنه‌ای شهید، فرمود: «ما با شهدای‌مان خداحافظی نمی‌کنیم؛ بلکه می‌گوییم به امید دیدار».
🔹
آقای ما که اکنون، عرش‌نشین هستید و در معیّت اجداد مطهرتان، در مقام قرب الهی به سر می‌برید؛ ما را نیز دعا فرمایید که به قافله عشق بپیوندیم و مغموم و مغبون نشویم.
🔹
اینجانب به عنوان خادمی از خدمتگزاران نظام اسلامی و مردم مبعوث‌شده، از باب تکلیف، مردم گرانقدر ایران اسلامی را به حضوری هر چه حماسی‌تر و پُرشکوه‌تر در مراسم وداع و تشییع امام شهیدمان دعوت می‌کنم.
🔹
ایضاً تصریح می‌دارم که کلیه‌ی مسئولان و کارکنان قضایی مسئولیت یافته‌اند جهت هر چه باشکوه‌تر و حماسی‌تر برگزار شدن مراسمات وداع، تشییع و تدفین امام شهید، در سراسر ایران اسلامی، نهایت مساعدت و یاری‌رسانی را به بخش‌های دست‌اندرکار و عموم مردم داشته باشند.
🔹
صد البته در جامه عمل پوشاندن به توصیه امام شهید و امام حی، مبنی بر پیگیری و احقاق حقوق تضییع‌شده مردم عزیز و صبور ایران اسلامی در جریان جنگ‌ها و تجاوزهای اخیر و اقدام تبهکارانه و وحشیانه آمریکای تروریست و رژیم صهیونیستی سفاک در به شهادت رساندن رهبر عظیم‌الشان و خانواده گرامی ایشان، بیش از گذشته و اقدامات صورت‌گرفته، تمامی ظرفیت‌ها، امکانات و ابتکارهای ممکن را به میدان عمل آورده و گریبان جنایت کاران را رها نکنیم.
🔹
ما ذَحل و خونخواهی امام شهیدمان را هیچ گاه فراموش نخواهیم کرد و ظَلمه بدانند که جنایات قساوت‌بارشان از عین‌الله مخفی نیست و دست انتقام الهی دیر یا زود گریبان آنان را خواهد گرفت.
🔹
بار دیگر با خلف صالح امام شهیدمان، حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای(حفظه‌الله‌تعالی) تجدید بیعت می‌کنیم و این مصیبت عظمی را دگربار محضرشان تسلیت و تعزیت می‌گوییم.
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/445829" target="_blank">📅 16:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445826">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/227c74837e.mp4?token=GYIcr143eAC-7hCnExR7f38Ypg8qsDF8ROzoQChwMt29N_yoaEn8AreL6IvOrg1PIisfENbhFDSVCfzXWqEaXfuayMj6TGZypONiPCydrceSGxJNYFhLtlt0cEb7-EepdToON5SU2SswHklZK3qGGsy8PHBB-3l81dSzEJdBbBGgMU55uV2L5l5x6cCIaErBwCh8q14eQP-XxLfGFd2zMx-URCbcNR75JFuGMckyZ_ZWIwUkR8hHMbEHGTg2xf5WeHU396K0HFXUouo1himT1CB33SHNTBxcxtEQM6OmQ0no0jiuS-5pkcVOZ3jnFChjsrjbO-S1b_9ihy1EAhPEGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/227c74837e.mp4?token=GYIcr143eAC-7hCnExR7f38Ypg8qsDF8ROzoQChwMt29N_yoaEn8AreL6IvOrg1PIisfENbhFDSVCfzXWqEaXfuayMj6TGZypONiPCydrceSGxJNYFhLtlt0cEb7-EepdToON5SU2SswHklZK3qGGsy8PHBB-3l81dSzEJdBbBGgMU55uV2L5l5x6cCIaErBwCh8q14eQP-XxLfGFd2zMx-URCbcNR75JFuGMckyZ_ZWIwUkR8hHMbEHGTg2xf5WeHU396K0HFXUouo1himT1CB33SHNTBxcxtEQM6OmQ0no0jiuS-5pkcVOZ3jnFChjsrjbO-S1b_9ihy1EAhPEGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غریب‌آبادی: مذاکرات برای توافق نهایی هنوز آغاز نشده
🔹
معاون وزارت خارجه که در به قطر سفر کرده، دربارهٔ شروع مذاکرات برای توافق نهایی با آمریکا گفت که «کارگروه‌های پیگیری اجرای تفاهم و مذاکره برای توافق نهایی شکل گرفته، اما هنوز مذاکره‌ای در این قالب‌ها شروع…</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/445826" target="_blank">📅 16:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445825">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVbVTlJRSbiqhHnaIr1AwtWj0QdrSOuvd13PASK8k94FD6EeZAhQtf_swYNzvzzxPi9Ff_1L0BPxdRRae415FJF4j68eVLIo43Md_mzXalzCvsAGNVzQxs3y5X2Vapmfy2ai-LZWyDGe_mORTjziZtmhR7dZQgCPTMT9TD34DaY9q0iumTMGCQE2ZBmrB9aBXVifk3Vp-iXOpg_GPk_xnO9lhL9PH8q0TDcC4_zsUmhmc4CNN8-cb15dFUAyZvjo0pi2dtZYX6My16JhcoOcMytmMTC7jD1yLGNlAHM_YBh099o7NDIQHYuc_tD8-ZHxpvPkPDNEoN3IRezneJkLWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای فایل‌های گمشدهٔ شما را پیدا و مرتب می‌کند
🔹
جمنای اسپارک، جدیدترین دستیار عامل‌محور گوگل، به اپلیکیشن جمنای در سیستم‌عامل مک‌اواس راه پیدا کرده است.
🔹
این ابزار می‌تواند به فایل‌های محلی کاربر دسترسی پیدا کند و وظایفی مانند دسته‌بندی فایل‌های دانلودشده، ساخت صفحات گسترده از اسناد موجود در رایانه و مدیریت برخی گردش‌کارها را انجام دهد.
🔹
گوگل می‌گوید در نسخه‌های بعدی، کاربران حتی از طریق تلفن همراه خود نیز قادر خواهند بود به اسپارک دستور دهند روی رایانه مک آن‌ها کارهایی را انجام دهد؛ برای مثال، پیدا کردن یک فایل مشخص و ارسال آن از طریق ایمیل.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/445825" target="_blank">📅 16:11 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

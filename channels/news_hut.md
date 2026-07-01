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
<img src="https://cdn4.telesco.pe/file/dZgscLsOJWDZJWaENpraM0Vmeti-gSV910qZ7AmchnSSzfgu5t1fm_WcOp3yVF_zQea3eJPGaBK8R2DKsUmTSgIDeJPYpYVEuuNTj_7bcUg5IPEm-j_uEWLBQIV9zNWSygz-zyE07ICylBZK_R6TY-s97Bz3gn4BFOo6kMM1udyxh3e23EYJJoE2Xf1T8L5xUu-C-gE-iIpYJUJWe4KKDjp_GhKDA0sZvSV_ULbQFGUI42J5CcOqWPN-m79qldGh451HsOZD4ELIgHcycADi3_PYervWGfulEAKfj0FTWjCwHtI5XFIO3uJivAPewBXS9xP-VVDdTYGaJArHWm99YQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 215K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 22:25:15</div>
<hr>

<div class="tg-post" id="msg-67161">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=rZudH1BrsrnPKWAgesSDejGtQsB1lakyDOPWRMo4LAkycWr-amMHuihK4NPc1UMXyEJO_FcC6ZH0bs9KWinjrliIc0qnu5fYdPhnzZLgG7ZRHn3pxibbJKE4u50o22a9URMGyafVQAJJxcBapu3_q7i2Mwe1a4leKiyXUHBEY3K_nPUJp0LIwTdgny2TLwxiMWtzCJyLFNudV8y3X2s0iGYaQR23pLcsAV-SK253moRkajXdYyRLMfLSbXjxLXd30ZAVDKSzUWktksLyqDwEZK8s0pujO0yfI5nrptisYS5uugR_7aQPgzccUzQr9IqorYUXRJAlYhBFHm_s9HFmsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=rZudH1BrsrnPKWAgesSDejGtQsB1lakyDOPWRMo4LAkycWr-amMHuihK4NPc1UMXyEJO_FcC6ZH0bs9KWinjrliIc0qnu5fYdPhnzZLgG7ZRHn3pxibbJKE4u50o22a9URMGyafVQAJJxcBapu3_q7i2Mwe1a4leKiyXUHBEY3K_nPUJp0LIwTdgny2TLwxiMWtzCJyLFNudV8y3X2s0iGYaQR23pLcsAV-SK253moRkajXdYyRLMfLSbXjxLXd30ZAVDKSzUWktksLyqDwEZK8s0pujO0yfI5nrptisYS5uugR_7aQPgzccUzQr9IqorYUXRJAlYhBFHm_s9HFmsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیروز کریمی:
قلعه نوعی 5 سانت رو تحمل کرد 10 سانت رو تحمل کرد، 30 سانت رو دیگه کجاش بذاره
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/news_hut/67161" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67160">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=G2hmaQQMk6cm6Mu-h0cBwmJs-BDvwrbVkRO6MpiSVhZMIzVKS3lNhhAdFTAItTVf_HR5d-elmbQRuLvV1XWr0bzDEuhI_VGTtQZH4EfriPttgIwiMC-ixRGx88AqSGMGFKM88G6qHfoQ8aaTjyfi38mtlFPUmpkSM1XV_yc0ZROPbCCrHsLGVb8leT4hObhoN6ZJVYFEsU6J5Y046cQ97-Dfius3VZUe2AP_j3hCxHkSRL-KY4odabqDKTam2jGSTr0EVjQOeLaQA3r_KeNUMdkeS2SwcAsjx7xIrEmJ_tRjEGAyR2bNAXCts1cDccNjJ7tVn7M2EN1YZddiVk-raw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=G2hmaQQMk6cm6Mu-h0cBwmJs-BDvwrbVkRO6MpiSVhZMIzVKS3lNhhAdFTAItTVf_HR5d-elmbQRuLvV1XWr0bzDEuhI_VGTtQZH4EfriPttgIwiMC-ixRGx88AqSGMGFKM88G6qHfoQ8aaTjyfi38mtlFPUmpkSM1XV_yc0ZROPbCCrHsLGVb8leT4hObhoN6ZJVYFEsU6J5Y046cQ97-Dfius3VZUe2AP_j3hCxHkSRL-KY4odabqDKTam2jGSTr0EVjQOeLaQA3r_KeNUMdkeS2SwcAsjx7xIrEmJ_tRjEGAyR2bNAXCts1cDccNjJ7tVn7M2EN1YZddiVk-raw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: آیا می‌توانید قول بدهید که آمریکا قبل از تمام شدن ۶۰ روز تفاهمنامه، دوباره وارد جنگ تمام‌عیار نشود؟
​
🔴
جی‌دی ونس: ترامپ تا وقتی که مجبور نباشد، نیروهای نظامی را دوباره به جنگ نمی‌فرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/news_hut/67160" target="_blank">📅 21:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67159">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل‌ از مقام آمریکایی:
در مذاکرات دوحه تفاهمی حاصل شد تا اوضاع هفته آینده آرام بماند تا در اجرای تفاهم‌نامه پیشرفت حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/news_hut/67159" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67158">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7lhaT-Ic-nzi2RP-gJ6aoXDmytJ48npqmADdjt_pvuZlI8GynlaWq6dyaWY-_xvo4RMN9JfbPQoPMz5JwlivucEEubEBlXAYXwg2KOySckxSlw7Pn2vdl0puQoqOIM9E7mOKZ_GupbKhCPNE8zeVeL9xeRXpsnw2njNO3SAMAzs1kd2h-7Oy0wwwh8pTZHH6sR9bvrZgBPthyLAxM1Z_WaAFuSF_fj4OvLgeeCG2GU8BF3gM4B2Le2gl125KkXy2nghuWQJOKQIKvXeHPUEtJJ4o1a1r586EFLAMY2UNP3uBZWm0firfaUUaTrBPIUilhXZokXyNV9dLizrUNmPBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:همزمان با از سرگیری مذاکرات در دوحه، ایالات متحده تلاش می‌کند تا ایران را از پرداخت عوارض منصرف کند.
مذاکره‌کنندگان آمریکایی و ایرانی در دوحه برای مذاکراتی با تمرکز اصلی بر تنگه هرمز حضور دارند و دولت ترامپ مدعی است که ایران از توافق هسته‌ای سود بسیار بیشتری نسبت به عوارض عبور و مرور در این تنگه خواهد برد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/news_hut/67158" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67157">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=XsgOeTfRZNAtgj1_2wzfhS15JGFW5YsLBTtdna1h08tYT7GoFF4OsROpk13MficBFPbR3zL49Z273nSAaprgaAWoyO0hwMATzqshhFq2wj5SqDq_J-vcE2ujbdGSfm-c567HHY8OP-kTbusnApPG5jd7c_Q21K-1ZypcjQTohNJa2JMw0-tMrEXk3QM9piqeZ4SdQBytcp3XXBjLZ7S4kFYj6KuUZyetEihcFbTYmsHOROJr1r49HSdAqJbHqlPDA_mbGrxLz2zEvM1fy55w31wnPtzx3hkePkOPeaW1gkuXOvvoeQUNMmr10ERLGLlN3azw7A3SF5Q_8AOP6CZ4_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=XsgOeTfRZNAtgj1_2wzfhS15JGFW5YsLBTtdna1h08tYT7GoFF4OsROpk13MficBFPbR3zL49Z273nSAaprgaAWoyO0hwMATzqshhFq2wj5SqDq_J-vcE2ujbdGSfm-c567HHY8OP-kTbusnApPG5jd7c_Q21K-1ZypcjQTohNJa2JMw0-tMrEXk3QM9piqeZ4SdQBytcp3XXBjLZ7S4kFYj6KuUZyetEihcFbTYmsHOROJr1r49HSdAqJbHqlPDA_mbGrxLz2zEvM1fy55w31wnPtzx3hkePkOPeaW1gkuXOvvoeQUNMmr10ERLGLlN3azw7A3SF5Q_8AOP6CZ4_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«روند خلع سلاح هسته‌ای ایران به‌خوبی پیش می‌رود... بازار سهام تقریباً هر روز در حال ثبت رکوردهای جدید است. قیمت نفت به‌شدت کاهش یافته است... و اکنون از زمانی که من حمله به ایران را برای جلوگیری از دستیابی آن به سلاح هسته‌ای آغاز کردم نیز پایین‌تر است.»
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/67157" target="_blank">📅 20:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67156">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1792b01078.mp4?token=YdVFFGXbuGn3SnZrpmnwSsiSVmS0ZtltsLbQ7DLbM7-KGJxZOr_6gXto7KdaeRUI-8WILn3bj2ddifVrRlXpYVhuFG9RwsGooP-AIyK1TsnHhCqPoBvcKQZgxQZcgS3sqnWRZwuUFEo-YrPHiKEGEoa5proFsCPciQGjU6ZDkMh9Pwoic-sd4BBMEOIzoOs5x1tExvFKuQ4HarK8hxbGMxhHPeILjbXKwU-fdMFV9boteggfkVylzYAKwJ1ak-cEpIh4l7wIYxDQcZ0yL_ZGgfJ1wWkBfTkSFt1cZV7x0uIWU5a9NvhWs5ARfv6SOptzU_i6L6VgIm3ymV9u0TvMAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1792b01078.mp4?token=YdVFFGXbuGn3SnZrpmnwSsiSVmS0ZtltsLbQ7DLbM7-KGJxZOr_6gXto7KdaeRUI-8WILn3bj2ddifVrRlXpYVhuFG9RwsGooP-AIyK1TsnHhCqPoBvcKQZgxQZcgS3sqnWRZwuUFEo-YrPHiKEGEoa5proFsCPciQGjU6ZDkMh9Pwoic-sd4BBMEOIzoOs5x1tExvFKuQ4HarK8hxbGMxhHPeILjbXKwU-fdMFV9boteggfkVylzYAKwJ1ak-cEpIh4l7wIYxDQcZ0yL_ZGgfJ1wWkBfTkSFt1cZV7x0uIWU5a9NvhWs5ARfv6SOptzU_i6L6VgIm3ymV9u0TvMAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قائم‌پناه، معاون پزشکیان:
اگر قرار باشد هر آنچه رهبری می‌گوید اجرا کنیم که دیگر نهادی نباید وجود داشته باشد
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/67156" target="_blank">📅 20:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67155">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=u6yLzMW0FIlFugXaN476XM-9Y-9U2ikHLmne3vpdT9sp4Jgm46xVZrvdMwBySyI5q7Hhpxj2SfezHpSZI_AsFN7lpKmoSiDqQ3X4eFXeqagYY8uq46rZ1xQMaGEITi2ulEqHOJaCTj5th6zQGQ2srb3caYSqBarjkeFCS9OXGe82cwUkcl5Oic9puslo1glcdzclP7nPYEVoeiCYhI4byVFrqnO9rBllOPM-uIS7IPAN0amwn4z0nohl5F7il3JlAdXU8sdrxeaA36g7Df-dD7G2Zn0UxJaLYrvyOsN37wBbC3HQrvgM7biFrGNsK11UL9NlytSEbIfaXxcyrzpKOaIvdZZqFnowEZrloLWKMmpHhb6YjWNEFg0pTRedWFoNcfAhMrct9pMtQrOnPWSfp8wn26lN5wZqCINYZzJZYgxilWZGVQzYn4zU__p9WXsnvFh6ci3a0w-yU7cPGJWTHi5xB_GfB_dcyI-FvIRpaEZFCSvukSlWjW_Mcysevz9oWQ1cgKXc6vHFbW0nRAeMOu_UWwOlBsVgUPm5p979bNbZ1A4oJzRjfqpm7Mq9WooX7WprgRB4T0Ka6W66wgQiEBXqnGZQ5ImKnTm9z8C9N_B2-b02iM_LZJprwbP5pxxl1v1RFxpDhOKMedtWzXRnmRiSMqxXNhUew9PbZWIAVoY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=u6yLzMW0FIlFugXaN476XM-9Y-9U2ikHLmne3vpdT9sp4Jgm46xVZrvdMwBySyI5q7Hhpxj2SfezHpSZI_AsFN7lpKmoSiDqQ3X4eFXeqagYY8uq46rZ1xQMaGEITi2ulEqHOJaCTj5th6zQGQ2srb3caYSqBarjkeFCS9OXGe82cwUkcl5Oic9puslo1glcdzclP7nPYEVoeiCYhI4byVFrqnO9rBllOPM-uIS7IPAN0amwn4z0nohl5F7il3JlAdXU8sdrxeaA36g7Df-dD7G2Zn0UxJaLYrvyOsN37wBbC3HQrvgM7biFrGNsK11UL9NlytSEbIfaXxcyrzpKOaIvdZZqFnowEZrloLWKMmpHhb6YjWNEFg0pTRedWFoNcfAhMrct9pMtQrOnPWSfp8wn26lN5wZqCINYZzJZYgxilWZGVQzYn4zU__p9WXsnvFh6ci3a0w-yU7cPGJWTHi5xB_GfB_dcyI-FvIRpaEZFCSvukSlWjW_Mcysevz9oWQ1cgKXc6vHFbW0nRAeMOu_UWwOlBsVgUPm5p979bNbZ1A4oJzRjfqpm7Mq9WooX7WprgRB4T0Ka6W66wgQiEBXqnGZQ5ImKnTm9z8C9N_B2-b02iM_LZJprwbP5pxxl1v1RFxpDhOKMedtWzXRnmRiSMqxXNhUew9PbZWIAVoY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی‌ونس:
«من واقعاً فکر می‌کنم ایالات متحده، فارغ از اینکه مذاکرات در نهایت به چه نتیجه‌ای برسد، در موقعیت بسیار خوبی قرار دارد.
اگر مذاکرات موفقیت‌آمیز باشد، که بدیهی است ما می‌خواهیم چنین باشد، با ایرانی روبه‌رو خواهیم بود که به‌طور دائمی دگرگون شده است.
از سوی دیگر، اگر ایرانی‌ها رفتار مناسبی نداشته باشند، برنامه هسته‌ای آنها همچنان نابود شده است، توان نظامی متعارف آنها همچنان از بین رفته است و ایالات متحده نیز در مقایسه با ایران همچنان در موقعیتی بسیار قدرتمندتر قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/67155" target="_blank">📅 19:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67154">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=pTZleJ4O-YnTke34vt2LDWdZ4JlnC7Gmen3tB56fTkVVhCX2QQvX48fmpbM75avOdOt8E2AM4tuaqBHUJTPpsM1SxRgLNXRo1qhwKVugskbHLvD4kefTZn8UhrkNU_kmVVstOiz2BWNIXptW0ykNjQ2UosNYn5FZugkYze8jJJXYbLZ5Wl_vEVU3hsl_cqnqTbglOVWrddFoHMrPCi6ETUJ-CS8k3C6pEMH05xVQBHeg1KiOmcwQqmKOmOLt_qiqmrb5p-_zRSRS3LkGtCggSE9oDtPHN1W0WL0iYZ5lg6vGcYOZFvnOrhPxKgEq66oJdQdpjvsJfdvdoEP0H91DRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=pTZleJ4O-YnTke34vt2LDWdZ4JlnC7Gmen3tB56fTkVVhCX2QQvX48fmpbM75avOdOt8E2AM4tuaqBHUJTPpsM1SxRgLNXRo1qhwKVugskbHLvD4kefTZn8UhrkNU_kmVVstOiz2BWNIXptW0ykNjQ2UosNYn5FZugkYze8jJJXYbLZ5Wl_vEVU3hsl_cqnqTbglOVWrddFoHMrPCi6ETUJ-CS8k3C6pEMH05xVQBHeg1KiOmcwQqmKOmOLt_qiqmrb5p-_zRSRS3LkGtCggSE9oDtPHN1W0WL0iYZ5lg6vGcYOZFvnOrhPxKgEq66oJdQdpjvsJfdvdoEP0H91DRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه عده کسخلِ پا شدن رفتن فرودگاه که از بازیکن‌های تیم میلی جمهوری اسلامی استقبال کنن. مثلا می‌خواستن شبیه هواداران تیم ملی نروژ به سبک وایکینگی تشویقشون کنن که اینطوری ریدن
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/67154" target="_blank">📅 19:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67153">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDJsvY-k3nQIop3kZT_kC77Fat9Mw5L827i1q2iH6STE7m1C4SqKsTLKAowN3o6jE_foJ9Ur1Bcbs3BpjpGC3Du-xidc_Mx2QroNjumzy6e_TB5Ppjgs-L0O8XrZZh-MfZAn36qJk5QDxYQX1VtiGdqF_PcQe-gbz_WVst-fKsh7fxrg1fxHh5kOXtsPUSzhx4i12LMH2he5Z5nwKW4W6Xc5T6i3Ea4MDPpmAjbPMJ5Pc_JqnXKcO1ekxxgSbxmDP-GiuGy0yZaBU24Kik0bi1O63fKjtReqmvkFTQAPVmyKQK6L4xGBiBa8lqseBQuA-MSgCqLn5mVQDtCigd35SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
به اعضای تیم ملی فوتبال کشورمان که امروز به ایران عزیز بازگشتند، خداقوت می‌گویم.
تلاش و مبارزه با تمام وجود و تا آخرین لحظه، مهم‌تر از پیروزی است.
کار علمی، حفظ روحیه، رویکرد تحولی و انگیزه بالا شرط پیروزی در آینده است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/67153" target="_blank">📅 18:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67152">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=BviUrXP9ErR23H58UynfnTn3cXI6U0q-dsGpzvBJ9FjXJV1XiZ9G0HvIiSsP3n8QLJXln9F_xPlcGQq-B6GwC4hdq-8gimfPRMbZH9vq3eKYbv2nkY0edVDs34VpGOGH-teYpCDnzmpB5wddZ4j4FKXhRjmEcRNdrdkJgsSr3SNmWhQtopR8N4EitbHk8Ft1YjOk3ZH8UohW0l5mP8s_kHO6femCwxSVep_AeUEgRLGfQlhXscfKPpAE_llABhWPv8qP28D1OvEXTO36iQ_Qs6oflif0uqODpFHTf0JYwZxVGLGUSqAXTioa_DL14_JsTW5jRdmPZaUdezY67bttLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=BviUrXP9ErR23H58UynfnTn3cXI6U0q-dsGpzvBJ9FjXJV1XiZ9G0HvIiSsP3n8QLJXln9F_xPlcGQq-B6GwC4hdq-8gimfPRMbZH9vq3eKYbv2nkY0edVDs34VpGOGH-teYpCDnzmpB5wddZ4j4FKXhRjmEcRNdrdkJgsSr3SNmWhQtopR8N4EitbHk8Ft1YjOk3ZH8UohW0l5mP8s_kHO6femCwxSVep_AeUEgRLGfQlhXscfKPpAE_llABhWPv8qP28D1OvEXTO36iQ_Qs6oflif0uqODpFHTf0JYwZxVGLGUSqAXTioa_DL14_JsTW5jRdmPZaUdezY67bttLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی‌ونس:
ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی، بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/67152" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67151">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=TgTgkXCCE0s0AQZ3nirTu-6KvzCqbSDPJMh3ewQn1PIht0UP7zuAaY5j7LWZlpO63rrzXO4Gwj-1MJvwjfgaBijfpd9x-KasGnv8dPQFDGlwVSlh6F2EelkaZA5OwwMKOcZUCS83CZD_gjqJ9FL-I9lJkzICa4ofVS07p315SNfebtJ9Jesq_rNzmB0HpdPru7uGGwoP7cB99RqUA-00U7tQxdFQfkyV1blswp3RRe9mU-Iu-BqizEjhkP264EndjxwWgCSl5VpDvalwmQECWnwnQyQRWpkJkxSpEzy14CorXxUEOYAedjLFnHABnFtCKBCg0VPJhuQ9A9xtF29AYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=TgTgkXCCE0s0AQZ3nirTu-6KvzCqbSDPJMh3ewQn1PIht0UP7zuAaY5j7LWZlpO63rrzXO4Gwj-1MJvwjfgaBijfpd9x-KasGnv8dPQFDGlwVSlh6F2EelkaZA5OwwMKOcZUCS83CZD_gjqJ9FL-I9lJkzICa4ofVS07p315SNfebtJ9Jesq_rNzmB0HpdPru7uGGwoP7cB99RqUA-00U7tQxdFQfkyV1blswp3RRe9mU-Iu-BqizEjhkP264EndjxwWgCSl5VpDvalwmQECWnwnQyQRWpkJkxSpEzy14CorXxUEOYAedjLFnHABnFtCKBCg0VPJhuQ9A9xtF29AYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت‌ترامپ :
روند خلع سلاح هسته‌ای ایران به‌خوبی
پیش می‌رود… بازار سهام تقریباً هر روز رکورد تازه‌ای ثبت می‌کند.
برای سه شب هم محکم بهشون حمله کردیم
الان هم روند مذاکرات خیلی خوبه.
قیمت نفت به‌شدت کاهش یافته، حتی نسبت به  زمانی که حمله به ایران را آغاز کردم ،
الان نفت رسیده به ۶۷ دلار،  پایین آمده.
هرگز به سلاح هسته‌ای دست پیدا نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/67151" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67150">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 نظر شما راجع به عملکرد پزشکیان و دولت او حول و حوش مسائل جاری در کشور چیست؟</h4>
<ul>
<li>✓ بسیار ضعیف</li>
<li>✓ فاجعه بار</li>
<li>✓ شکست مطلق</li>
<li>✓ بعدها شاهد عواقب خوب و بد خواهیم بود</li>
</ul>
</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/67150" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67149">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‼️
آخوند قاسمیان:
واشنگتن رو اشغال کنید؛ ترامپ رو دستگیر کنید و بیاریدش پیش مجتبی.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/67149" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67148">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=Y7EZ9AHCsqQj9aXeSIJ3ThS2Vk8AA3DRJ9vhovHCGVzXTtcYIQULzng4yzJn6Gz8c_AYiS0NtaCFhpf98e_EPnHKeSla0Lh2PzdeBpdmDx7P-9VWCWeyedFPzxmw1y7OlJhgEEaly0xUyG-5XQg3d3H2CIxj_VWYeb_0a-EmZQLEVcqPfmF7virdiLOK6p2wRzl6ZnTSVTJKOJRVndzywhLp8gUmbh0KnjqBXSRPZj9uOFty74ZhpCs0pG9Pzm-Y2Q3BfMxK9hmvfZfX4V5M8UbHWSjS7ZFp6zzDU9VybMxOc2nqJ7lc-9tgStTVg6cR4sTCLDDsD5wTRwPa_zFmVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=Y7EZ9AHCsqQj9aXeSIJ3ThS2Vk8AA3DRJ9vhovHCGVzXTtcYIQULzng4yzJn6Gz8c_AYiS0NtaCFhpf98e_EPnHKeSla0Lh2PzdeBpdmDx7P-9VWCWeyedFPzxmw1y7OlJhgEEaly0xUyG-5XQg3d3H2CIxj_VWYeb_0a-EmZQLEVcqPfmF7virdiLOK6p2wRzl6ZnTSVTJKOJRVndzywhLp8gUmbh0KnjqBXSRPZj9uOFty74ZhpCs0pG9Pzm-Y2Q3BfMxK9hmvfZfX4V5M8UbHWSjS7ZFp6zzDU9VybMxOc2nqJ7lc-9tgStTVg6cR4sTCLDDsD5wTRwPa_zFmVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله امروز اوکراین به پالایشگاهی در حاشیه مسکو
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/67148" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67147">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/67147" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67146">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSfTUN30H_OcR1kJxKly1chstwYJlES1lD_3V46UsGz2OClU1IVPCVqRXeegxwGVo6AKyOb-eMdfteEsM552SGz47y5l4h2Ey_5W-HrdhtFL1YG0v2LYwWxiHMFV5sNN46r4bgby17ZqvDaztIt2p0Y1K0Sb3lYz6bN0SDHbcnTG3NPvCM_xNpPv50oBthHEMgNSfLEKKycEtEgBQlJnZnFXqrYmGVeC1IiRGR_kLrzN7yPW7b3qXnXv-Vt1w0B6CnkX031JM6KtYZttwWyf7-mPf1-q5y2icPo7k923jq9qbTySEx7xxY3rQSquqzR0WV2k8zO29NxJlysDGGz43A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/67146" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67145">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=AQYcS4U2-KJZG2666sP_-BIK3DbNcBj5Ss1oh84J_MbhlnCt64rS-nPU_eKGYfMMSgJHZnpWxmFlIBgdbPvYwMJ2kYhJp9o5i6Ymdm44QWjyHz-nSS9cuwc1V7CsWEOLPu0cjCTmctQtuioZKf_M5qbeZh-PuEoiWv6daj_9xrm8mdR4GM6p6z7pYxJItrrAzHmSafUixTDDu7_mra5x_2TPInHdury4Cl0gXIoo3QnawiymSwZeiSUI64naF8-jz32XTFrCbOeV105Z4JiXt3MEMHl6DqIW8a8UpKT7_p8P6r-Z8jWvOJaXWc9NqESM_btZEj62fVAITEJeC0Akyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=AQYcS4U2-KJZG2666sP_-BIK3DbNcBj5Ss1oh84J_MbhlnCt64rS-nPU_eKGYfMMSgJHZnpWxmFlIBgdbPvYwMJ2kYhJp9o5i6Ymdm44QWjyHz-nSS9cuwc1V7CsWEOLPu0cjCTmctQtuioZKf_M5qbeZh-PuEoiWv6daj_9xrm8mdR4GM6p6z7pYxJItrrAzHmSafUixTDDu7_mra5x_2TPInHdury4Cl0gXIoo3QnawiymSwZeiSUI64naF8-jz32XTFrCbOeV105Z4JiXt3MEMHl6DqIW8a8UpKT7_p8P6r-Z8jWvOJaXWc9NqESM_btZEj62fVAITEJeC0Akyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها)
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/67145" target="_blank">📅 17:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67144">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=n8nLRibO90FhVP_XPk792WNZIyVctDAXkluffn7eav75bDK2qGt5FnrQvJwgncd9EAHBbjaAUw1pui6sgFLUVhEXH8xeuS4_IotIffnw2YCWSccvtPYxFhO5NzEcsC8Lulm-U1PuZ5qjd6KcpSS0R8XeBwFW6akRvPZlylTKoGCJVa8Uk4SEMKQ6qGOn85oo1UpuaRdvc1t8X6BZKOUhKKu35VcsJDI3xkfMdNRK--ze0gU0LvSBNgkM4prU7k_y27kROlTGCKHt7oj3PCQb2CF4QYOni2mgEftxQf4HTH27DJpJT30TVuR0QGY7GeOvxHjLlvsbe9yJly9Umo65OA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=n8nLRibO90FhVP_XPk792WNZIyVctDAXkluffn7eav75bDK2qGt5FnrQvJwgncd9EAHBbjaAUw1pui6sgFLUVhEXH8xeuS4_IotIffnw2YCWSccvtPYxFhO5NzEcsC8Lulm-U1PuZ5qjd6KcpSS0R8XeBwFW6akRvPZlylTKoGCJVa8Uk4SEMKQ6qGOn85oo1UpuaRdvc1t8X6BZKOUhKKu35VcsJDI3xkfMdNRK--ze0gU0LvSBNgkM4prU7k_y27kROlTGCKHt7oj3PCQb2CF4QYOni2mgEftxQf4HTH27DJpJT30TVuR0QGY7GeOvxHjLlvsbe9yJly9Umo65OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه جالب و جنجالی یه پسر نوجوون ایرانی که در حال وایرال شدنه:
🔴
خبرنگار: اگه یه دزد خفتت کنه، موبایلتو میدی؟
🔴
پسر بچه: آره، جونم مهم تره
🔴
خبرنگار: خب اونطوری ساعت و دستبند و هر چی داری ازت میخواد.
🔴
پسر بچه: آره ولی جونم مهم تره، اگه ندم به قتل میرسونتم.
🔴
خبرنگار: فرض کنیم آمریکا خفتگیره، الان یعنی ما بیایم موشکی و هسته‌ای رو تحویل بدیم؟
🔴
پسر بچه: وقتی چاقو زیر گلوته و زورت به خفتگیر نمی‌رسه، باید هرچی میخواد بهش بدی، اگه ندی میکُشتت و بعدش خودش وسایلتو برمیداره.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/67144" target="_blank">📅 17:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67143">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1012800172.mp4?token=k9-7fXupnsW6ab199FL12jQbi7qwSDCvJOs36cglTf0gg_06xJPDs7Sk2yAItGajoLV0OQAlqInwI3FDV0_U58flFLLiNfCZthYgqw3vRBHR6CAPJveqlRBM8tezMO9sydD_DQ2kw9nGMOFp_FvXmFBBni_tTZAWPcSNbMWfH-JXm9nEJVoQDmfHo9d8styx9A7bfxgjEaFZzGlzl2J_hL625BotYKGflyCE-2s_BTrTerwV_7SbMwJJji_pBu5APaPINGyK3-JtQ4b-gzaxsHRR0IBlHX8d4oefGjCSrjYyTBVi8fN1pdKFHgQQLbacPNd0O74vMWpQNDImc2iolw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1012800172.mp4?token=k9-7fXupnsW6ab199FL12jQbi7qwSDCvJOs36cglTf0gg_06xJPDs7Sk2yAItGajoLV0OQAlqInwI3FDV0_U58flFLLiNfCZthYgqw3vRBHR6CAPJveqlRBM8tezMO9sydD_DQ2kw9nGMOFp_FvXmFBBni_tTZAWPcSNbMWfH-JXm9nEJVoQDmfHo9d8styx9A7bfxgjEaFZzGlzl2J_hL625BotYKGflyCE-2s_BTrTerwV_7SbMwJJji_pBu5APaPINGyK3-JtQ4b-gzaxsHRR0IBlHX8d4oefGjCSrjYyTBVi8fN1pdKFHgQQLbacPNd0O74vMWpQNDImc2iolw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یک تحلیلگر ژئوپلیتیک چینی می‌گوید امضای تفاهم‌نامه توسط دونالد ترامپ، بیش از آنکه نشانه کاهش تنش باشد، تلاشی برای عبور از «گرمای تابستان» در منطقه است.
🔴
به گفته او، با وجود امضای این تفاهم، نشانه‌های میدانی حاکی از آن است که ایالات متحده همچنان در حال آماده‌سازی گزینه‌های نظامی است. این تحلیلگر معتقد است حدود ۶۰ هزار نیروی آمریکایی در منطقه مستقر شده‌اند و مقدمات لازم برای هرگونه اقدام احتمالی فراهم شده است.
🔴
و پیش‌بینی می‌کند در صورت ادامه روند کنونی، تحولات جدی ممکن است حداکثر تا مارس سال آینده اتفاق بیفتد یا حتی ممکن است از همین دسامبر شروع شود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67143" target="_blank">📅 16:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67142">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=Nsz1YdXkxRtLIcbOGvFRnCwGGqwPCeV01xQcmFIYR0acdYtKe7K7Pghu_Ktot4fX_o5Tg_EByTNhfy29e3vMqyGCfMgQn2AzBZtJo7IySvo035F8nPhPY-iTwUJnNZeDoMhZFlGM3q6qMr3sOkQTHsdsrGWW0DPptkUdZYSK32ONKnrJR46hJ8l0Ug7ByphOwDTTZeaIwzCVGcgick92LtfK5NgwWPC-FdVwkD7xKLAbzj4B8vW7hBIZkX3WVxr2VlSpp0fQelKzHUstkd1vLJdKvVXSVX15WUEFV1NgXGxqaoIwDV2FSGRlW2eyH8LabP6NwrMLO7FVxzzQtFSPVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=Nsz1YdXkxRtLIcbOGvFRnCwGGqwPCeV01xQcmFIYR0acdYtKe7K7Pghu_Ktot4fX_o5Tg_EByTNhfy29e3vMqyGCfMgQn2AzBZtJo7IySvo035F8nPhPY-iTwUJnNZeDoMhZFlGM3q6qMr3sOkQTHsdsrGWW0DPptkUdZYSK32ONKnrJR46hJ8l0Ug7ByphOwDTTZeaIwzCVGcgick92LtfK5NgwWPC-FdVwkD7xKLAbzj4B8vW7hBIZkX3WVxr2VlSpp0fQelKzHUstkd1vLJdKvVXSVX15WUEFV1NgXGxqaoIwDV2FSGRlW2eyH8LabP6NwrMLO7FVxzzQtFSPVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهریه‌خانم‌چیه؟یه‌پهباد‌ شاهد بخوره‌تو‌قلب تل‌آویو
😐
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/67142" target="_blank">📅 16:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67140">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBczA6zwqKoD-SIOPC3Ukw5SpYf16Dp1K2wcb_LJUEprG1F7PJTE9IfGP82udCaVc09RBlhKCuEhGIXFwllEc3kFWh2TGahirV5-iU_uve5V7loRf13V_7ImUyZhjK39oTGfZW15t3hH6wNzNPf_hKUBTOC_k3FhLNS69pdcbK7TlSd8-jmBtZ1bcEDOltdCByyTmc6Cl-0-wHc-FeVWCcTvsruWCYKKBjjAWqG_uY0st9mxuq8EmrywMfYEUw3rNc4tIXs8Pw--6UsegRKsGHuCvzMC9jR9Omolaov4e3vgRazPtvVugc8hSiCLiL6n_QMqnMXL4sMlGypa9P2JfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m790PfDEyPG7z95UebgSPYDB4mMWtOjzoBxO4_FAEH_w15e0zPhRUSErK0unqq9JpwGaq6x9rLfMnPxWBufRstWmPzlrg7RR_TllXCsPADrVxXD8_J6y6u3N0drA3ybZdYlGpKjDinRpaJHlEF-M3RkMxVqgBKCTR2ng2WkeAm5q0HYMxAw5GHBdRiuBg7NMqUNZl7c4n035QTyQvhJxuQjNjw52xDex56r_21DFUhWPzUzNISAjxANB7EcYWWoQYbvgkoXdhJUU9CjwBpnl852tCUlIoImwXIsDlw3O8iFXKRJjOd0iomOo8uGjrZ1Nx5ouaHhcq5dJxPCQ4MxxMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
کاتز وزیر دفاع اسرائیل:مجتبی خامنه ای برای کشته‌شدن نشان‌گذاری شده.
عباس عراقچی:هر تهدیدی علیه مردم و رهبری ما، پاسخی قدرتمند و فوری دریافت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/67140" target="_blank">📅 15:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67139">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsiVLbQJsazzVzuwH6xoB7BuqaYE8yCIluRBkjsoVTjCWwUzQZd9_F6-LgQDpMu0ZsI2mq5N-uSt76HIOTjOvPBxRar3RzuexXvDuyRKIY2miW815niNUSIJ2JTTZDSF2U4vj1kw3JM8s23ufSLWLgillXzLvh-3lKDXcXMb0GwwGXpv71TirXQvlDn7GqTwYVmbE_JBYTt17VG_JCtlQOSM4jgmTbXfkA07rXKw6UkSgcjvLA41dt6AkNijSRpDbMPA-4LupxJkzhDl2nvhXP-My7XW79IQGXLemT7FpOmi2opWkpGk80OQyQC7FSAI2cZnthzkyRD4GLGe7Jbmyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
علاوه بر ناو باکسر، ناو USS Portland (LPD 27) نیز وارد غرب آسیا شد، کاربرد اصلی این ناو انتقال خودروهای نظامی و تفنگداران از دریا به ساحل است
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67139" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67138">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unu9_kHUEv-pHOx2ibas4T55xNRWzwSor67EFsQzyHzFy0WaSFnUDBTHUZL7i_qVq3vy9r8Jddn175cwYXm2vP9fDkdz_QXfDuBqVSm9uf4JeUr7-hUGdw3axsyPN8IablLGaX1eD9D7ffMrKPb8BqUofVOcM-baYgVKMj_O4fyoSV9FBG3xqgSmsP5QhpvdQXLRzJnP-16wMevijl7K1rGHrY6n6BNmIXfiHoNu-hr6kBSnFx7ojkLxSEZVFNqpg-XJ1UKrWTNFkspnZJP3xywCPUVAwQX1KBYE0KD5o1E6EBnAhcAc8A9xOyYoSMrOlUCiUhCjiGTw9AAj03rdOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
مفاد تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است. رئیس‌جمهور آمریکا متعهد شده است که دست‌نشانده‌های خود در تل‌آویو را خفه کند. اگر آنها از ارباب خود سرپیچی کنند، ایران آنها را تربیت خواهد کرد. هرگونه تهدیدی علیه مردم و رهبری ما با پاسخ فوری و قدرتمند مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67138" target="_blank">📅 14:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67137">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aF5i1XXdQ4Cldgirh-4GFtfIBpa5btV7kbykje03ahzadrxQFmCBflHDDi7XL-NbCZsOmWRQsD2ndkfggeXLq-gL0PLkufT9Uem1OGnLiQWXGpfduczBr_ZmLftvAeKV1IIaPSLw5vhiR5HQI0m7LhobB1Bbj1L1Vjr3PdHsT_SQiIoqI0Kd8lkbPg7Wl-Y5xfk0NlbgmAMauRsNbNWZEVnPR3aZSLP1wsbU9tMsQnhdPSmqqh3zqfW54-M2Tesq5ESHaF1HYoN96DybQr4pTKdgdhHy1rakpCenN2-AozZoiU7srYvkBzvw_HwVjr1Q9ovzPJj0kpQdyXDSTERcBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران به سرعت در حال بازسازی زیرساخت‌های غیرنظامی خود، ذخیره سازی منابع حیاتی، پیشرفت سیستم‌های تسلیحاتی جدید، جایگزینی هزاران تله نابود شده، به کارگیری فناوری‌های نوظهور و گسترش شبکه پایگاه‌های زیرزمینی و مراکز فرماندهی و کنترل خود است.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67137" target="_blank">📅 13:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67136">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک منبع آگاه:
گفت‌وگوهای فنی غیرمستقیم میان آمریکا و جمهوری اسلامی در دوحه آغاز شده است
قطر و پاکستان میانجی این مذاکرات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67136" target="_blank">📅 13:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67135">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=IFiQ9FIhmZ6CXSAxWFvlpXzW96EsuWUGPKXcg88zSPZRNjZgv6QVhMtq7yo2ukkKNO0EdIHr4b2jd43ryi3AoqUI8v8ggYxD-baS4XGgO5sBkDanDSd47K-HACibQvEueIVdCu39wk2YW4oxvUfjLat3owiAZaeG2iWR0eWVv4i8vu3Y1UWO_ymNtxjooyOfE6X8UF35APAQ8yAFURbIZj7HdyTiVy47GbK5Mq1PZdNn9s2FVeHV7oZlFCksVzz6a5VisWAmzvFq_3wcwLqpxYWvGhsL5WpQ_YY_AzUP8hZYww70caHes9RtHgqcTW3z32H81k5tmtyM1_VQvKJQIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=IFiQ9FIhmZ6CXSAxWFvlpXzW96EsuWUGPKXcg88zSPZRNjZgv6QVhMtq7yo2ukkKNO0EdIHr4b2jd43ryi3AoqUI8v8ggYxD-baS4XGgO5sBkDanDSd47K-HACibQvEueIVdCu39wk2YW4oxvUfjLat3owiAZaeG2iWR0eWVv4i8vu3Y1UWO_ymNtxjooyOfE6X8UF35APAQ8yAFURbIZj7HdyTiVy47GbK5Mq1PZdNn9s2FVeHV7oZlFCksVzz6a5VisWAmzvFq_3wcwLqpxYWvGhsL5WpQ_YY_AzUP8hZYww70caHes9RtHgqcTW3z32H81k5tmtyM1_VQvKJQIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این کلیپای محرم چرا تموم نمیشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67135" target="_blank">📅 12:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67130">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKsTcmFPlVtaxzskxl3v-uSaO44U0VeWy_RIXqnW6kd6WhWKYLHs5EwdsZxfIK8iUWjGt6l2h-VoQSrqGeTbIYknztRzMXL0VrV8iVTT9syTgjJEF6CbnLTywU6TdQnAyq47TOu7SldKsiw27o8Ysj4JEc0BuiiRBJJ-eotnzEK335aUFYQtlnjUfm3KU0XhIKS7Cg8VNhz6Qsf7C_LkG1XJGs8CVayKzaxPNzCuHmxCgnwT3agvVok6UpHD68ea8p21nuno5RW4wjw4_L2zvr-ZLoRo4xRVSxRT37aSNq2W7eBIkC2k5FxpmDA1Fj6svSthe2azvw-WIHARuA58Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OPFGB-6-QNjI37pvReiXN_U3NX5ujeWZR5xy-P3ydVysN3Gqvd5iYYItY6UylOVInHK13YcEC45Eq2TAWNr2YjGE3JNLakIP6lvU_0zCIoq96QNNG6MuXUQkq2CwRlaV7LrwTv5tskMVG3QOCAVHhfzJnVc4ZMFe5HHSzli5yvQEmgbwKMgoxmpXRvTWWLSiXmyBWHC0YQc39B2ov7k9RCwRpXDx7ZZQx0yMnZRyoZuYdLb10fbyhOgKPuRnhOnMDlQR8Qg6CSSdFF2Z9C8PybIvYP_ME8E1LxBTNKtiUFA9I_TG9EN3Nr9mpc_uEyWzfWzk4EgrWTQ7_GX_ywUq5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=o0Z60brUL76qqGEe6UQyhfPKGCab4jT4TWrgQZWWyNUwB80x2OK8lRDf4-7lCVn23tO7K_wp4xI5JLC4CUKuz_7QdZ3jkMoOjZa9AjsGDmBDMSemoMgcqf5fCw6RDl6wTWEUlcGqSMgniA7p0Hcfbear3YeAXxL88Sgly2YdvVQWH96TcjgKQcCtpQ73CG7ffY4X3G1c7boLy3k0YPoEf4AtQhUgXQEXg2cip4HlDKXpHjcMLK3e4yZ_7gQjgyXR2y17blNjErUJAq3Ru-C7hcs7lvYwNu7PqG2swS8IGNOiI8hBcsCIjo5n5QllnYZFA-Zbro0_EWy_JLOgUKajjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=o0Z60brUL76qqGEe6UQyhfPKGCab4jT4TWrgQZWWyNUwB80x2OK8lRDf4-7lCVn23tO7K_wp4xI5JLC4CUKuz_7QdZ3jkMoOjZa9AjsGDmBDMSemoMgcqf5fCw6RDl6wTWEUlcGqSMgniA7p0Hcfbear3YeAXxL88Sgly2YdvVQWH96TcjgKQcCtpQ73CG7ffY4X3G1c7boLy3k0YPoEf4AtQhUgXQEXg2cip4HlDKXpHjcMLK3e4yZ_7gQjgyXR2y17blNjErUJAq3Ru-C7hcs7lvYwNu7PqG2swS8IGNOiI8hBcsCIjo5n5QllnYZFA-Zbro0_EWy_JLOgUKajjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر منتشرشده از پایتخت ونزوئلا، آسمان کاراکاس را در زمان غروب با رنگ سرخ و نارنجی پررنگ نشان می‌دهد؛ بر اساس‌گزارش‌ها، گردوغبار برخاسته از زمین پس از زمین‌لرزه‌های اخیر با پراکنده‌کردن نور خورشید،این منظره غیرمعمول را بر فراز شهر ایجاد کرده است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67130" target="_blank">📅 11:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67129">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c160c90364.mp4?token=kS4lmnuumFz4f0TGZ_wRj4ozj8MOLOlz0FTiDvx4Q2II9xbJyIbfjZghaGmIeTWJ75sBCAiRw3nzkLtPNX6lO6eyq1M3rCBTmfpMkGcmgV2dcgjks_CU0mRpnltmxbLifb1AbSwE_ZD7iX9Ht1oiGUDIAEiO6f2c_KSGOqfQxouaMzbDHAGdhKMqtpPbihZF0Qpghra4tCYMujj_e5486SpG_ZmHCJ1R_hA51fWsO7DMLpdMayiQVft_2Mca-LgDit49BfC1fkdLTwGkufIUflMMGrynws3fe3lnaHf0uguKsPRzvDuNi2ZQz9TuE7Trn4R90qCOFrJlZFEnpQMoPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c160c90364.mp4?token=kS4lmnuumFz4f0TGZ_wRj4ozj8MOLOlz0FTiDvx4Q2II9xbJyIbfjZghaGmIeTWJ75sBCAiRw3nzkLtPNX6lO6eyq1M3rCBTmfpMkGcmgV2dcgjks_CU0mRpnltmxbLifb1AbSwE_ZD7iX9Ht1oiGUDIAEiO6f2c_KSGOqfQxouaMzbDHAGdhKMqtpPbihZF0Qpghra4tCYMujj_e5486SpG_ZmHCJ1R_hA51fWsO7DMLpdMayiQVft_2Mca-LgDit49BfC1fkdLTwGkufIUflMMGrynws3fe3lnaHf0uguKsPRzvDuNi2ZQz9TuE7Trn4R90qCOFrJlZFEnpQMoPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌نویی
:
خوشحالم که بزرگان دنیا یعنی آقای مورینیو و
تریلی هانری
از تیمی که من ساختم تعریف کردن.
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67129" target="_blank">📅 11:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67128">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=SQn1N7ulpC1o4F_S5RzDX_5l9VNauFpN7XXW1nI-iycFTzBoNMCpVK-kKKWj_pRHIESybYRhNT_tmrXQ2KTNUo87_yoPMx5SIxAij1G6fkZtw1UUtfqxo7_zrM9E9Xjuy52bVdfjpnaIc70lQZKAzOOveKiJAdhnIkXOykl0uwMKtjpsUuC4bd3j1UZVfoLHAAXtmvRE1NgYhG0vA7IQt7lYw__N8b35ep5pCbNv0WUAqlSNbAYTOtT_7M9vEl1UWGCQd6yv1UTi2wRYfvf29xECQ6g5GJkr1WWYwer199Izl6nwsAkSJlrCAZDU2iwTyaL_PkjzTMdx0iqWGY0YAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=SQn1N7ulpC1o4F_S5RzDX_5l9VNauFpN7XXW1nI-iycFTzBoNMCpVK-kKKWj_pRHIESybYRhNT_tmrXQ2KTNUo87_yoPMx5SIxAij1G6fkZtw1UUtfqxo7_zrM9E9Xjuy52bVdfjpnaIc70lQZKAzOOveKiJAdhnIkXOykl0uwMKtjpsUuC4bd3j1UZVfoLHAAXtmvRE1NgYhG0vA7IQt7lYw__N8b35ep5pCbNv0WUAqlSNbAYTOtT_7M9vEl1UWGCQd6yv1UTi2wRYfvf29xECQ6g5GJkr1WWYwer199Izl6nwsAkSJlrCAZDU2iwTyaL_PkjzTMdx0iqWGY0YAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
سازمان انتقال خون باید خون‌های زنانه و مردانه را از هم جدا کند زیرا قاطی شدن این خون‌های نامحرم با هم در رگ‌ها موجب ازدیاد گناه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67128" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67127">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d22600661.mp4?token=CkvVFSGLRpqVS0vaZRO_SC0rE6D2vRoE5U0Ztdroqpx6sNW-2egRqAs3haOI8-kKMyX-AvzRUOjKVYH2EC27gb07lWWzZyVDwWFKBLy9N5Mw-Yr-351mpBuKZdBtbhnSPj-PrTK1E7Y2TwbnfP1HFeDa6FXjBnhqkj-j5m3_wzp7jrRMs1P9UmvJ5amOqw_iyNAiUvcpZ6GT1C77C8g-wIR1BcFD32RX8CcYy8u3c_WXLH8yoIratnEMzCzL7j3qiJrmrMLw-wwNpXv-7y-zK1nhsIM7f2L8WIpXrkJGF79DaAnXz-0HPa0FhxHjsp7PNT5Wngv0skzgViAxgj8Bjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d22600661.mp4?token=CkvVFSGLRpqVS0vaZRO_SC0rE6D2vRoE5U0Ztdroqpx6sNW-2egRqAs3haOI8-kKMyX-AvzRUOjKVYH2EC27gb07lWWzZyVDwWFKBLy9N5Mw-Yr-351mpBuKZdBtbhnSPj-PrTK1E7Y2TwbnfP1HFeDa6FXjBnhqkj-j5m3_wzp7jrRMs1P9UmvJ5amOqw_iyNAiUvcpZ6GT1C77C8g-wIR1BcFD32RX8CcYy8u3c_WXLH8yoIratnEMzCzL7j3qiJrmrMLw-wwNpXv-7y-zK1nhsIM7f2L8WIpXrkJGF79DaAnXz-0HPa0FhxHjsp7PNT5Wngv0skzgViAxgj8Bjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر ممدانی شهردار مسلمان نیویورک درباره مرگ خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67127" target="_blank">📅 10:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67126">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=WMaq3r-ftPHhnzq8P_z3fi2EPKS8tf9FW8MpTSIUwxpiSLXP_cbReG2toUU922WehOcTnYLBiwoAJ9thQDBqYg2D_yx8C4aHvxZHQ5bNK8VjI8rUiowQ6wePsJPau0OA0fUDcyl19l5tLzsqprTLmM7IcuT5sqBuXUEgM7ERfujtM2l3xH2ZYYfwJdomNbiFkbbz6Xo3qnQjve5jAKsZRgtNcO43UaxmFGbdVIyR-bkaIRqOVz31KS9V47OCPuySCMwcPcaFULCZldl7mWVQedF7wx_r7XrtLbYY9CuT5-_JdVqZtO8v6yGsbWR4ZiRYFNiQnd_3AQqlASkrwU6bow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=WMaq3r-ftPHhnzq8P_z3fi2EPKS8tf9FW8MpTSIUwxpiSLXP_cbReG2toUU922WehOcTnYLBiwoAJ9thQDBqYg2D_yx8C4aHvxZHQ5bNK8VjI8rUiowQ6wePsJPau0OA0fUDcyl19l5tLzsqprTLmM7IcuT5sqBuXUEgM7ERfujtM2l3xH2ZYYfwJdomNbiFkbbz6Xo3qnQjve5jAKsZRgtNcO43UaxmFGbdVIyR-bkaIRqOVz31KS9V47OCPuySCMwcPcaFULCZldl7mWVQedF7wx_r7XrtLbYY9CuT5-_JdVqZtO8v6yGsbWR4ZiRYFNiQnd_3AQqlASkrwU6bow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
نمایشی که قراره بزودی از عرازشه ببینیم:
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67126" target="_blank">📅 10:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67125">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGh3SfObMusW05xxcc6TyxvXaog9paFf2fMsanyheS8kjodsmmHCdik6wJFBHk3S5l_MhE5RTxuAWGJdCbJMs9jP-UtORqYIddVa5fBxt0k9tqh6VhWkqcMA1Vuqcaw5c1bEti-e0IkhN_ethoBV8luBPQoPwDJqWPeCqEtuKQAvh0QgHDUyGVYCX98SEBqml7tqTVP6nifRTfZb2JDTBiDK5NAzKRar96lscK9FeY6BvW0gURV9oCVcc81sDLEchqh7tliGJ9GxjNtrRSkLqHCJ300Si7-P_kajoVXaYPhMu2JO2ikroonFclcpinFhdg9Zm9kxnP6gueUoDU_SAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
به گفته مقامات آمریکایی آشنا با این بحث، رئیس جمهور ترامپ بازگشت به جنگ تمام عیار با ایران را بررسی کرده و در روزهای اخیر چندین گفتگو با وزیر دفاع پیت هگست و رئیس ستاد مشترک ارتش ژنرال دن کین در مورد حملات بیشتر داشته است، اما تصمیم گرفته است که فعلاً به مذاکرات دیپلماتیک ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67125" target="_blank">📅 09:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67124">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PF9Dr_b1T_MyWwN_D_uFVGMDTC6WM1NITiv_lCjFsJSaZCpUXLh9V6AOdyxgByrr47LbjLgyf1mMqo6SnDaku0EOqlER8pKH4vxgLPYFL0IToYJMPxbSYfvhZbxFBjpRToeNGn6_lS8ThflXkR2M59jtSbnwvQpArWtJ74-rH55tJoO7fY3EDZ4qlTdpIf9JHvflyLcztVmc8gSI7fxY9Y8HtT8rlexaAJihfw8B0ejirLhJAyZ1LDvZdHIIoxwatZg6INaYcWU9uaONBm7yRwHwyRozs6GKR4dwCpcY6WhFak2SsdseQLo8Pp306lEK71esTHbrtBnfJhiKIkOTDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
فرماندهی مرکزی ایالات متحده:ناو آبی خاکی USS Boxer آمریکا شامل ۲۲۰۰ تفنگدار دریایی وارد منطقه خاورمیانه شد.
گروه آماده به خدمت آبی-خاکی Boxer (ARG) و یازدهمین واحد اعزامی تفنگداران دریایی در حال حاضر به عنوان بخشی از یک استقرار برنامه‌ریزی شده در خاورمیانه فعالیت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67124" target="_blank">📅 09:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67123">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67123" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67122">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IQcx4q01KyaFcISZssKGRyc9oqATOVHCFx73mmt8krdmyTpmI8O6Nsr7nrl1Qzm0Zcf8iJ3sYS5JyVN8hwvnH5ZkPCnvQnqJ2v-wJ6bGMtjE4nlBrDUD75YUi2F4TK1PIu3dxRRMFzN_QGnp1QNtXVil0ZUHl9DTbEEc_uSBN5MSANA_yieOJjmXhaB2GsAkRG8IXCeIWA6xBpjnF7ujZ7s-v4mtkgy_HBPdOPHu4Dj1Skq9nm2KyxfC2kQEtqE9yoEz3SXwByZ7fnXsSD0y3NgV_yD5cFsjOdyTjSS8NPorisImFGTIN8zL-_ZZmcW5r8PE-yU8b91LOEKRT4ay6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67122" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67121">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=TqKp7nUtGF0HxUYiL4FerctzHNA2L1BZqflejDYvH5jzNIGtsEdsQoZbo2IKWaP3bbRV5RSmP6TJh4N6UoQlKMfbsPRIndwM5KPPKPXbF3NQqS-LdrHo4WmIDrqRfkH6rRWyfxGtlaYrIJAhVxTKTD-Rzf8ohMiDX4eDgWhCobuFbeh4w6vx1NLoX2_s0P9-o4cgVTftwDDz1K17mUhEby2x7jQOGZnQ2UxZF0C7iUg3-qfgHj0_I4NmWc-sgv7vidxUJlZbp8khaYkE1T8CzEyzfXiKsupmMGbwn1V0jHeDb53bWI5G3AHMQE-BkGcX4N2S3WjUbdCdM7BmUw56zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=TqKp7nUtGF0HxUYiL4FerctzHNA2L1BZqflejDYvH5jzNIGtsEdsQoZbo2IKWaP3bbRV5RSmP6TJh4N6UoQlKMfbsPRIndwM5KPPKPXbF3NQqS-LdrHo4WmIDrqRfkH6rRWyfxGtlaYrIJAhVxTKTD-Rzf8ohMiDX4eDgWhCobuFbeh4w6vx1NLoX2_s0P9-o4cgVTftwDDz1K17mUhEby2x7jQOGZnQ2UxZF0C7iUg3-qfgHj0_I4NmWc-sgv7vidxUJlZbp8khaYkE1T8CzEyzfXiKsupmMGbwn1V0jHeDb53bWI5G3AHMQE-BkGcX4N2S3WjUbdCdM7BmUw56zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
کریس رایت، وزیر انرژی ایالات متحده:
ایران هنوز به هیچ وجه همکاری نکرده است.
جریان نفت از طریق تنگه هرمز به لطف ارتش ایالات متحده است. هنوز هیچ همکاری از سوی ایران صورت نگرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67121" target="_blank">📅 02:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67120">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7UGtoY59xZuqlp_WY1VD-xpwfmXxogD1hF5oFeiPSlzxbLzAStSxp7Tq_uIabutwZueyms-DBppj-961Uh2QDMaPx6-F09M74YKvIeQ3hBgLlPJw00oMcDxIt_u7yKQkicxOADaRe0QL7NbRLqYwBiw-a1BY-I88jivATVzGtDr0ws-87ti7OG19BuaV-7lZCX2D2Xw1E6UVC1qm7jLRnkYX0McYDKxGcQwhfF6IV6wj4PsY029hyS3Q_B1w48MvP70epx9riKfWlb72v8qe9M2DVISBPtOsjRKq42IIiSI23RYzBU8X_w7rrVfp7F7iCo0zGJ47gAHapVNZ4orNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر منسوب به تابوت علی‌ خامنه‌ای و خانوادش
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67120" target="_blank">📅 01:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67119">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=I1p-l6WUXUJcBdOrSTPTz6r5QfyWk8Rej4mqXag5Ag4EfQcdeogghkz-eT0YjqCZwtQhJbziQxCVP9cReapHH2vkJRYVXvSyKcgAx4DptKcloc8RCzgQSFBMIJJ5bPcfwMGoS7IEy7JYTxHAvoToeIcjZLWy2P0sZbXSUJjDlBlIgio8LS0h9HQz3P3pcLzck_6N4AMEC1MXx3g5wwPOZLzLRVepMBtqQncIq4KRzkVbrNByulmqbGMZUXWBNDBruTOK7lfw-fTCEQqo-GQ4_6bKIqw_7IN7AfLG-KWKgzMIQBihP-DDpVcY-sOUHaE8vEqlrIzMII2vX_ApH-UnVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=I1p-l6WUXUJcBdOrSTPTz6r5QfyWk8Rej4mqXag5Ag4EfQcdeogghkz-eT0YjqCZwtQhJbziQxCVP9cReapHH2vkJRYVXvSyKcgAx4DptKcloc8RCzgQSFBMIJJ5bPcfwMGoS7IEy7JYTxHAvoToeIcjZLWy2P0sZbXSUJjDlBlIgio8LS0h9HQz3P3pcLzck_6N4AMEC1MXx3g5wwPOZLzLRVepMBtqQncIq4KRzkVbrNByulmqbGMZUXWBNDBruTOK7lfw-fTCEQqo-GQ4_6bKIqw_7IN7AfLG-KWKgzMIQBihP-DDpVcY-sOUHaE8vEqlrIzMII2vX_ApH-UnVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
بخش سانسور شده صحبت‌های قالیباف در صداوسیما:
قالیباف در قسمت پخش نشده این سوال، می پرسد: خریدهای قبلی این اقلام که در طول ۱۵ سال گذشته انجام می‌شده، از کجا بوده؟ آیا ال‌سی اینها در لندن باز می شد یا نه؟ چرا الان مهم شد و این حرف‌ها را میزنند؟
🔴
چون نمی‌خواهند بپذیرند با مجوز اوفک صادرات نفت انجام می‌شود.
​
🔴
این قدرت جمهوری اسلامی است به آن افتخار کنید و پای آن بایستید. این سند شکست آمریکاست و ما با عزت آن را انجام دادیم.
​
🔴
گویا حداقل ۲۰دقیقه از این مصاحبه پخش نشده که نکات مهمی را در خود داشته است.
​
🔴
برخی قطع صحبت رییس مجلس را با بازگشت روزی‌طلب به معاونت سیاسی مرتبط می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67119" target="_blank">📅 01:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67118">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=KvrbVObmYhS9YphYJAdi8ZsaUH92CLTpOEtlB_I9jHzb168ZDDELY0LjPCj5_JhHBtK9G7IE80_l4zRpYzniF9ZHyOmHoWsgkDpGyepzf3nn3R_VqBTTa8Trvdlb9XFBGwyEpkSiIpgpgQpcfVERQC58sp0lBtPaByyJ7jVjHSF_KCEhW6w06YLq86URXhIGreU8cSbDAFClskGM2hx_OaPs4Xt4t3-BjE_D_ANjAbjq-mgpyYXx_-SloV6MeKOhkEYhAUELDGHohK_7ERQxwe60p0qbu9qFWBvtiwx_9r3mujy9z_HAuxshyZ4MNE-VUZYcWw9jpsX6s2jfVtYe1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=KvrbVObmYhS9YphYJAdi8ZsaUH92CLTpOEtlB_I9jHzb168ZDDELY0LjPCj5_JhHBtK9G7IE80_l4zRpYzniF9ZHyOmHoWsgkDpGyepzf3nn3R_VqBTTa8Trvdlb9XFBGwyEpkSiIpgpgQpcfVERQC58sp0lBtPaByyJ7jVjHSF_KCEhW6w06YLq86URXhIGreU8cSbDAFClskGM2hx_OaPs4Xt4t3-BjE_D_ANjAbjq-mgpyYXx_-SloV6MeKOhkEYhAUELDGHohK_7ERQxwe60p0qbu9qFWBvtiwx_9r3mujy9z_HAuxshyZ4MNE-VUZYcWw9jpsX6s2jfVtYe1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
قالیباف وقتی گفت توافق خرید غلات و گندم در ازای پول های بلوکه شده برای دولت سیزدهم بوده است، مصاحبه اش در صداوسیما قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67118" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67117">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640225b559.mp4?token=ALShP1actt2wexgtl608_6TTMbtnw81u9095GKBEG_PCegho2-OUPBHxDisPkaBiDTv97l-T9bvvGnYchZNN1zXvdkXloQ8BJCkuxAGmOkz84wSpZfEkqM3ib91_NvldgVzwMmhZPpTa2DUXftvZ5iukDAfgGHdb2xkYbMx05U51Umv7lBG7KV1K0mxo5YmNfdbY3itpotIAbhJX7ZUdIsqa2VIJjlW9nBoyt_W28qjK-C2JXWiAgyTN9IsyHWikx4Ff2s5_nIxeZB0YFrDJEnOSIawKpEAdFukW1ivp0AwawZ8czq_4ZB2qRJJQzStOWMiSL8VnlgKBPFL0X40t2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640225b559.mp4?token=ALShP1actt2wexgtl608_6TTMbtnw81u9095GKBEG_PCegho2-OUPBHxDisPkaBiDTv97l-T9bvvGnYchZNN1zXvdkXloQ8BJCkuxAGmOkz84wSpZfEkqM3ib91_NvldgVzwMmhZPpTa2DUXftvZ5iukDAfgGHdb2xkYbMx05U51Umv7lBG7KV1K0mxo5YmNfdbY3itpotIAbhJX7ZUdIsqa2VIJjlW9nBoyt_W28qjK-C2JXWiAgyTN9IsyHWikx4Ff2s5_nIxeZB0YFrDJEnOSIawKpEAdFukW1ivp0AwawZ8czq_4ZB2qRJJQzStOWMiSL8VnlgKBPFL0X40t2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
لحظه قطع شدن گفتگوی محمد باقر قالیباف، توسط صدا و سیما
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67117" target="_blank">📅 00:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67116">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e29288f186.mp4?token=OBdeK72m8tGlcHKjvdpP3dJT__jLCNoVxfr_HDZgGzdy1M4ECQpS0YTXEhw3YYnSUN4sfAI2Te_4RvQnx9ufW_D9WAlBunZ48pZBGJybML0jR08bzNY2Uxdhoafn-v2_rAc75Rd6ig2xlScAUIW4KMfVCJmBTAUIuz15N79_G1I0TYglEzSPFkzPyKxlreqGqg-YElAV73GSh8TrY1hXlMVgpJIQ5NpnGBgGROLa1v07X6vx_ke0ksH679lLWePVkts8JGGdugvs-aJUWY9k8ZdxuikpMv_Ws9W3ugLk8iQewFV6K_M6Yq3-R5Wnks9BUYEUiesiaiR4mCWoK-z3yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e29288f186.mp4?token=OBdeK72m8tGlcHKjvdpP3dJT__jLCNoVxfr_HDZgGzdy1M4ECQpS0YTXEhw3YYnSUN4sfAI2Te_4RvQnx9ufW_D9WAlBunZ48pZBGJybML0jR08bzNY2Uxdhoafn-v2_rAc75Rd6ig2xlScAUIW4KMfVCJmBTAUIuz15N79_G1I0TYglEzSPFkzPyKxlreqGqg-YElAV73GSh8TrY1hXlMVgpJIQ5NpnGBgGROLa1v07X6vx_ke0ksH679lLWePVkts8JGGdugvs-aJUWY9k8ZdxuikpMv_Ws9W3ugLk8iQewFV6K_M6Yq3-R5Wnks9BUYEUiesiaiR4mCWoK-z3yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
این خانم، عالیه نصیف از چهره های وابسته به رژیم جمهوری اسلامی، شش دوره بدون وقفه نماینده پارلمان عراق است، او در رقابت‌های پارلمانی چند ماه پیش گفت: «کاری می‌کنیم فاسدان از پنجره فرار کنند». حالا خودش به دلیل فساد کلان دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67116" target="_blank">📅 00:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67115">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563023c29.mp4?token=K2fa403gzCrYZNR681EgzymCuk8OtUgHYMC3x8RDLXBhRck7TcJ0AvVNe5JpcyEZWl72dpawiQEljHqon7Pn2TUNUYxsF8Bu2ApXxl8LfKGnTbiBsF93TtzuimR70LDYFkReuRF6nnEIJu15zGJd4DEV8JwX9yEPnlnXvl3tIcBzBHoVgoJ42NWngm5xIR98ndUtOenz04tlS55Pct1SRNc6YVC8YYGkmwaEXaf7ASwNmACiOnDpLtb2_yVnGbNG9NW6FeyL8jiI4eof8M6t2dVb807XsGXX3heMvJtslyQDK0uiHiEu8tzL88oC8dw7s69UpVoq6GtAOnA2WYo3GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563023c29.mp4?token=K2fa403gzCrYZNR681EgzymCuk8OtUgHYMC3x8RDLXBhRck7TcJ0AvVNe5JpcyEZWl72dpawiQEljHqon7Pn2TUNUYxsF8Bu2ApXxl8LfKGnTbiBsF93TtzuimR70LDYFkReuRF6nnEIJu15zGJd4DEV8JwX9yEPnlnXvl3tIcBzBHoVgoJ42NWngm5xIR98ndUtOenz04tlS55Pct1SRNc6YVC8YYGkmwaEXaf7ASwNmACiOnDpLtb2_yVnGbNG9NW6FeyL8jiI4eof8M6t2dVb807XsGXX3heMvJtslyQDK0uiHiEu8tzL88oC8dw7s69UpVoq6GtAOnA2WYo3GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید آجرلو از اعضای تیم رسانه‌ای مذاکره‌کننده جمهوری اسلامی در اظهاراتی در پخش زنده شبکه خبر رویکرد علی خامنه‌ای رهبر کشته شده جمهوری اسلامی درباره مذاکرات را اشتباه خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67115" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67114">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgh0em2MWTwwZ191fK7SFdW_7kcdZMaIGtbZfO229N6k2wSF0A93WCdNWgQgrD_T8yzI9dZ-NsxP_7ovKxA_HseKtUU1BAlGruuz9LRbwqjJa6dymu-P--hhIzVwfkgu87RS2ubiHEhW9njjU0xgJ99Fkhw5iU6XjXCPFRGXD3fYcr7iVyb5qtz6bwZ9kFbiiRXS5EXAQ8kljroI9N5pl19MkUK4_gJ6U--XnYsmRTLA67LNFDC5URWUGTV9LR6LUHWFuNMWRKb8i6AvlHpPhRKYEVC1qwKCXACk1y94f-ZgqHYu-y-XAdAm46MvXaPe6TCnyFQ57ynmLwp5WNLcrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌿
جدیدترین روش ترک اعتیاد  گیاهی
بدون درد، بدون خماری، با انگیزه‌ای نو برای زندگی
🌟
✅
ترک فقط در ۵ روز
✅
درمان کاملاً طبیعی
✅
بدون داروهای شیمیایی
✅
بدون بازگشت
✅
همراه با پشتیبانی روانی و انگیزشی
💚
بازگشت به آرامش، بازگشت به خود واقعی‌ات
💪
تو می‌تونی! ما کنارت هستیم تا دوباره بدرخشی…
♦️
جهت مشاوررایگان فرم زیررا پر کنید
👇🏻
https://app.epoll.ir/74570725
عدد 6 را به شماره زیر ارسال کنید
👇🏻
🆔
@Sahar77631
☎️
09923413672</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67114" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67113">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSY643MqkpFpaEGtlJae0zTFx8rHbE2eE5jtGvP3hwPOVgZYR7psuNQuJWsLNeaB37xOPtZFof3a5rQcwwr9bW247XQBGt0IgjRbYtFKJUujdPO2IuFQKzaymaPq9OyvaOic_xGxZtrtPo-5oDCsBLmfe0ApL-d2c8_rhvPrFXdCHLBL8TXBBGkVeh3LGG2syGphEj1AUSrKWmYmxIRvEmkz_nf8Qb0yR34QftlcwLGaxlSc0N9DrjArfeKH6jGDuTnTpC0Wzqy_LIXr1ZGjHXTS2k8kcDZYm63_XHJ5dc-7YlF0amSTiHUKtaKfuy9DbrSLijzPOH5PEWpYrY9GA8Gxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSY643MqkpFpaEGtlJae0zTFx8rHbE2eE5jtGvP3hwPOVgZYR7psuNQuJWsLNeaB37xOPtZFof3a5rQcwwr9bW247XQBGt0IgjRbYtFKJUujdPO2IuFQKzaymaPq9OyvaOic_xGxZtrtPo-5oDCsBLmfe0ApL-d2c8_rhvPrFXdCHLBL8TXBBGkVeh3LGG2syGphEj1AUSrKWmYmxIRvEmkz_nf8Qb0yR34QftlcwLGaxlSc0N9DrjArfeKH6jGDuTnTpC0Wzqy_LIXr1ZGjHXTS2k8kcDZYm63_XHJ5dc-7YlF0amSTiHUKtaKfuy9DbrSLijzPOH5PEWpYrY9GA8Gxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دو موشک فلامینگو اوکراینی به یک کارخانه تسلیحاتی روسیه در ولگوگراد اصابت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67113" target="_blank">📅 23:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67112">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=u7TEkAHJa88YLYQVFXaxPX6AY8dv9dyPxkOPHccKgfwZA1BZwH_nCGkaQ-4ZPEKvWdX5cITNPe92Qd6x7JcRQ8xIRunpg0Pqn3-8nKwJowZ9toVU9hnOo82u-FyY7qVF4DPLJbg5UwysxQDkHRMMXZAKN5qEoAAa2YrPJOPxDjYXXq5tgS5PDhch8TiBnq-S2UE1SeVz2NfeiJIaMGkAnasRoPLlOtz3Ky13npK_ri4tfNgdw-W-t6DRkMd0iwsvpE76nRdNM8OOVgkB4eEQmlPvYLEHpVKr0M7u7br6UMiKKdhLfcTd4WRrJHHXfwksg0Qar_ynma37ko7ZJGRE7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=u7TEkAHJa88YLYQVFXaxPX6AY8dv9dyPxkOPHccKgfwZA1BZwH_nCGkaQ-4ZPEKvWdX5cITNPe92Qd6x7JcRQ8xIRunpg0Pqn3-8nKwJowZ9toVU9hnOo82u-FyY7qVF4DPLJbg5UwysxQDkHRMMXZAKN5qEoAAa2YrPJOPxDjYXXq5tgS5PDhch8TiBnq-S2UE1SeVz2NfeiJIaMGkAnasRoPLlOtz3Ky13npK_ri4tfNgdw-W-t6DRkMd0iwsvpE76nRdNM8OOVgkB4eEQmlPvYLEHpVKr0M7u7br6UMiKKdhLfcTd4WRrJHHXfwksg0Qar_ynma37ko7ZJGRE7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازدید بنیامین نتانیاهو از منطقه امنیتی در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67112" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67111">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=L6OEekDOGYHRdeZKNwp3ZKUI-oM0n4n4aN4V_E_t-tOFVlhofrLHaHlCyAe7wrFCfbOVUcgLpHDb9hkbM-lcdi3dwycGah9gf70dyuiwcc1ORHPxsrtX6jTyjhVfUEQ4V_0Stso9iOOMg-cJ6tRFwnxg4syFfiveQdLKYIw5V0FSdJRFVWrdNrTiyG2VRe1v_qKizHM2SOmrvslnXkFpfcD6PQZ3-DnEBh2NE1xSMLZ51I6L4sWzXEwQPrBauO0TGaWjcAc-pGeQ4qdgKH5lo41o6PwsOP27U5oETMFpmICfA0o4TO4vKnKGomnH1jDuxUBxCM1TZgwwL2XjiCWJ1S8dUB_bgnG8tq6StXCcngZ-qPbXZ35tlEy1xLGqy7l7QGG1_VE39uwEYURz04_GhNtGcDfQes_9Kp2ha3KTwpSkGDON-2pTG-WeLYsDZGMFKiMK_BmeuOpZo7ELPtWPUp0741R9nbBL3Nm6j0qckv8Tdxo3h53Cs4k3vFsmYnqOjxEqOZ1nbBFETDaSSvUm0eBoWOFK7xaAZp4Lll3uEbmVTdHFzzRWpF0R5xT8YHhmMMt1kqw-26GJ7jyCDyWim5u0pHk2awMdBom6g6sQEDJTAzglKQ2Bx1zWhIdlz6cH_4qZSTRKMzUkaJLD89Voav-Q5KRepuxE0umA9zRkgV0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=L6OEekDOGYHRdeZKNwp3ZKUI-oM0n4n4aN4V_E_t-tOFVlhofrLHaHlCyAe7wrFCfbOVUcgLpHDb9hkbM-lcdi3dwycGah9gf70dyuiwcc1ORHPxsrtX6jTyjhVfUEQ4V_0Stso9iOOMg-cJ6tRFwnxg4syFfiveQdLKYIw5V0FSdJRFVWrdNrTiyG2VRe1v_qKizHM2SOmrvslnXkFpfcD6PQZ3-DnEBh2NE1xSMLZ51I6L4sWzXEwQPrBauO0TGaWjcAc-pGeQ4qdgKH5lo41o6PwsOP27U5oETMFpmICfA0o4TO4vKnKGomnH1jDuxUBxCM1TZgwwL2XjiCWJ1S8dUB_bgnG8tq6StXCcngZ-qPbXZ35tlEy1xLGqy7l7QGG1_VE39uwEYURz04_GhNtGcDfQes_9Kp2ha3KTwpSkGDON-2pTG-WeLYsDZGMFKiMK_BmeuOpZo7ELPtWPUp0741R9nbBL3Nm6j0qckv8Tdxo3h53Cs4k3vFsmYnqOjxEqOZ1nbBFETDaSSvUm0eBoWOFK7xaAZp4Lll3uEbmVTdHFzzRWpF0R5xT8YHhmMMt1kqw-26GJ7jyCDyWim5u0pHk2awMdBom6g6sQEDJTAzglKQ2Bx1zWhIdlz6cH_4qZSTRKMzUkaJLD89Voav-Q5KRepuxE0umA9zRkgV0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف: اگر می‌توان گره ای را با دست باز کرد چرا با دندان باز کنیم؟
🔴
کسی می تواند خوب مذاکره کند که برای جنگ آماده باشد.
🔴
مذاکره با آمریکا مذاکره با یک دشمن بد عهد است که هر لحظه فرصت پیدا کند علیه ما اقدام خواهد کرد.
🔴
ما در شرایطی با جنگ و آتش اقدامات تلافی جویانه ای را علیه رژیم انجام داده ایم.
🔴
خوب است ببینیم شیخ نعیم قاسم  و مردم لبنان درباره این تفاهم چه می گویند و برخی دوستان ما در داخل چه می گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67111" target="_blank">📅 22:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67110">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c10065584.mp4?token=tEPr-c06zE0Ewb8tCH6tqswZ2VriQr8FJp4dekM3MGnWpqwGG8RLHHEAPxwAczmTfX9y_yx6Q1Q8FwNM4XfC1XsFOmRkb490PpdtL2c2GBblrTJ4K-nYJOYwxQvDBj3DVUITij1oZrXu6CVLET907k5cYMdsjYcLwNZjCn4bX5Sex0lgdOVzIH8DSE6rA-nMOKmhlSjypyNkJnWIGHnYDK0YqN5pxPCD-YwSwvnxdMHafJ88vMqnniHeZlL_059jj_OkpXQuf2a2pA7J-nYZJpaO6Q4peJtkM60fpxi0zVenKyTeHOY0dx368OOmm6b-laUxJVCjmqzSDTCvwForWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c10065584.mp4?token=tEPr-c06zE0Ewb8tCH6tqswZ2VriQr8FJp4dekM3MGnWpqwGG8RLHHEAPxwAczmTfX9y_yx6Q1Q8FwNM4XfC1XsFOmRkb490PpdtL2c2GBblrTJ4K-nYJOYwxQvDBj3DVUITij1oZrXu6CVLET907k5cYMdsjYcLwNZjCn4bX5Sex0lgdOVzIH8DSE6rA-nMOKmhlSjypyNkJnWIGHnYDK0YqN5pxPCD-YwSwvnxdMHafJ88vMqnniHeZlL_059jj_OkpXQuf2a2pA7J-nYZJpaO6Q4peJtkM60fpxi0zVenKyTeHOY0dx368OOmm6b-laUxJVCjmqzSDTCvwForWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
تعهد ما نسبت به باز کردن تنگه هرمز و ادامه مذاکرات منوط به پایان جنگ در لبنان است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67110" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67109">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
قالیباف:
غنی‌سازی حق ماست و خط قرمز ما در این زمینه مشخصه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67109" target="_blank">📅 22:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67108">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=TWVBtTlp9Fwu26igo3TS3Lx2Jf6HDzenDn5jf2UtXOMTQuIryf0rqhYGGmdv3PxDI2IqA7TtUxH8nnFeeC13YPSrH_ntUpvmL_zalXQCbrBX1HIddZYml3Yt4NnfMg92CX12rI21DLDrgN4D1m9FKtCsPFY0t4pu4e6G9HvUFsNp-9Fv8jL1LY85Z9vxqxyGP6-RnJKkdIgBswubG4Ml5FdHNfqD78UX2tTHn4JQZkV2pc6zKEzh3dBUEWwbnTZPILsmUJE9jDL3Yn3yrHamGUhRWHBCqbGh_ucmMN-PMcW4_vdFK27hK13HSducjUlBjiaNe0zx-iZivgfov3M8Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=TWVBtTlp9Fwu26igo3TS3Lx2Jf6HDzenDn5jf2UtXOMTQuIryf0rqhYGGmdv3PxDI2IqA7TtUxH8nnFeeC13YPSrH_ntUpvmL_zalXQCbrBX1HIddZYml3Yt4NnfMg92CX12rI21DLDrgN4D1m9FKtCsPFY0t4pu4e6G9HvUFsNp-9Fv8jL1LY85Z9vxqxyGP6-RnJKkdIgBswubG4Ml5FdHNfqD78UX2tTHn4JQZkV2pc6zKEzh3dBUEWwbnTZPILsmUJE9jDL3Yn3yrHamGUhRWHBCqbGh_ucmMN-PMcW4_vdFK27hK13HSducjUlBjiaNe0zx-iZivgfov3M8Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
اگر نخواهند در گفت‌وگو به تعهدات خود عمل کنند، آماده جنگ هستیم.
🔴
اتفاقات شب‌های اخیر خلیج‌فارس را نقض آتش بس می‌دانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67108" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67107">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745f2de194.mp4?token=GM5YXlgoflAlh7V1_YJUpUUfuPgljy8fzxPeNK8nebUIODDI2Z9RMcUWHp_4FXLWFTayp8ODAPREEBKVlN51NoTLJtogdchztmhj4glznsyF6BG-QXHa8OpkADIEMU3uJ6vDUBYBQvXhkiRdSvnDIVwuB0zgyr-CDVuLIJTB3saDxM_JpEwrl-P7RFtZGTERolVSehnPp451wZqqdZmi1-UKWCjBV7MPbLCMNnYGBOl5_1qzMHDKVr0c2TfpPdsH95FEDMexTKFut9che9zO-AuUYb16lP31b91LoO3SjV92tIsgs1yGMVdiMwzbo7weRe58O5lSQWpiuORPFW5fnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745f2de194.mp4?token=GM5YXlgoflAlh7V1_YJUpUUfuPgljy8fzxPeNK8nebUIODDI2Z9RMcUWHp_4FXLWFTayp8ODAPREEBKVlN51NoTLJtogdchztmhj4glznsyF6BG-QXHa8OpkADIEMU3uJ6vDUBYBQvXhkiRdSvnDIVwuB0zgyr-CDVuLIJTB3saDxM_JpEwrl-P7RFtZGTERolVSehnPp451wZqqdZmi1-UKWCjBV7MPbLCMNnYGBOl5_1qzMHDKVr0c2TfpPdsH95FEDMexTKFut9che9zO-AuUYb16lP31b91LoO3SjV92tIsgs1yGMVdiMwzbo7weRe58O5lSQWpiuORPFW5fnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
دو اقدامی که پس از امضای تفاهم‌نامه، در شامگاه ۲۴ خرداد رخ داد، اعلام پایان جنگ از سوی نخست‌وزیر پاکستان و توییت ترامپ درباره برداشته شدن محاصره دریایی بود که از اتفاقات مهم تفاهم‌نامه به شمار می‌رود.
ما در حال دنبال کردن دوران گفت‌وگو برای تحقق ماده ۱۳ تفاهم‌نامه هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67107" target="_blank">📅 22:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67105">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NAFPEml2rv0Z-qF1rtAMsjiaK618REriqVvUxYkuD7EfDWb5meJn-hTMYstXHXB1Nkenus4CKwsQUsH8OOa1sK6RF2X6VFou7YkMyZNrQTc-ZURZsLBAqkCGNIjOUTcRA-BUVvz4JeVrZFo7XZ2Za1DWREzZ4kbS06yb-mK5bwVGB6gcECpk0jrmGrAAwNPG9RmyK6agzyhswA09zg9TIy04TMc-Ovsx3kCkfwPKuYkT9_hRTtjxZfsblzLSPtR1lJP78VfNkt_s040oK-GSsXE4a_OpPiDiXTIr8s2Vkp1oOQI9bIOXCFQfXexq2XKEW80U0aJLrB7EVJkiIm0cNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYObyWQpJzoGff-y3vadA8Bdf3s9Gk-E8f70tWin94hnuuH2wqeHdu8kZN2oWQtZv-389lkhEnuQGJncKgN_EN9KQWXrdVtWRss_HrlQHcWhKMZQJAkotxt2aZlafVJkxShE1qbQRfUvAyA7iZ_XLexlvTib1OxyAitlXJZiDG_vZQahWStZe6S6axf77-o94pQRdxVP0wGsrryOi_moCLNZNxcVLZ9VowjlJsFKxiLS1EO4SSrW0eWctx8Fv7K4TSnnvL2ZkaUdOEmi75Pq1IFVv4WvltnA4FImN4SIj6GYx2IhFtH8r5dXW4PaeOdVCwN7sGGkXWP7KsVZ8HyUzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صفحه اسرائیل به فارسی:
چرا هر کجا این تصاویر به دیوار است، دزدی و فساد هم هست؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67105" target="_blank">📅 22:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67104">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ho6YuGmf-8nTGnMsyaJ7uRkm8UnHo2z5s2m8LWuMM6EpKhpKA9p1mH0cqhNugnGiz6vUGS6ihSHCFx10WnpyoW85UMNbkhtEl_8kuvZMszTDr9BrErHyA0SxAQW9NNes7AiAJYB9qPWmgk5XNDjbbBZKbFA3gzeTcjNQJVg8Iek0gvUS-Qwstui-32cB8CtyR_YZs16hEypHR_xJXzvQYveRBW8KZrVv3L7PC-XZmuN8iEmX8KZOfOkMDe5tD3FxtQmkonrtAEmpvTN7U575-XrAxHfNgG1WoeFI8tTLDPcVKB8oFT4Oh5QniDNvoWW87p92Dqprqq6qL-y8qPLvuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وال استریت ژورنال:
اختلاف نظر میان میانه‌روها و تندروهای ایران بر سر اهدافشان در مذاکرات با آمریکا، پیشرفت آنها را کند کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67104" target="_blank">📅 21:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67101">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/muC0JL43hCp__vW_aAC91-nMmbbUKaE5Bj6zBaozZXOlIxhV3iMlI9_BHLB1VtPNvyLInxmuJLPzsrf1c3oBxVsnq1NNI4rMw43HQMxNqyDRjF1e0W9eyCjbM3fMqA1Vks4nFmKKAdXI9tgj8gZ1k9TGwCghB70czEHcJXLnJIUCHx1YoAyKQkuDoI9kkA4mrLToZYUISnz5mzOLdEK-6Vk-X0kSRlv_qcAjhyFoKwtqSNy_7TG14oF5Ge4q3BRaZhJlAiY7vGCRkZ2pk_t-YzqybTsMmj4b-ef2dwmLaladeIGtZn-OcwFmFDjvZj14QvDnzmyHqXhZDygQZTv-Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ky2O9fQPJhCJj4djNICJ7-lkyB__-YJ0QJwZ1ybEK7rsA52WpRS1pa9g-uSb25L9V8zt9t7dwSx_uZcvcJVFCMDFJyJS51a7eTdmj86sf1zKQhAHu7B7jHR2eqf9Zw26fpHJ5yOkmKDlDRO05dnssaJ-gqqA9aBJvRWFT9i0wskykCU5CuSlnNzw19IJbbh73YGdVcoD_r81AiF6WK3gMqeI7q7HwLjfI-YiTdAdBjUNJ9NDAsnhLVcQOr0TiyrA-vhaUlEUZDsk5zvCAITcARz5lM7rE8uaVmfK1OD7U5-b4vFNqfnsrLwSJyYYIeFZjEug_QIG8VmthWSZNN8Jrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AfKprmbTT6EuImVQ56ajwIoUDftJjlO3p8DhVEfiyoSwvMP2tE3I1YqwBFBuIs2JOXktO7kQmuX-PLmmJQjY27LUrhs4BrfQ91uje1u-f6wYTKyic_APoeD2eVZAhYBVllUvathPQiPScJN9LTcEQ-_7O6z4xu0_dXasj8zleScbdiMxrIlkImSR_NC-lJFZiS1Q4KrBqRMFtbcDRVvqyiUvOdt2rloph2uxHIgnr0Wp-9SLp8JLK-UG2ENud2NV37KQkmPAboN7N2GyCHOYwxbnoCDzdW2JwmP5yJl9ibeLot63PkSeTJHrmpRjL7j1UK0abnEVLCDH_eAEm1AdDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سنتکام تصاویری از آموزش شبانه تفنگداران دریایی ایالات متحده در جایی در خاورمیانه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67101" target="_blank">📅 21:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67100">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=Hsz7o_iEZ4EEWzuvsmGrGd6fPh39PWUUWnvFefW8dAG0u8LVTK6ltmRcHXbZTIxk9LJWUaW-wHVBdbLWbq6f5ABcedO1VF_ebZ5JN8a8JDJBJQPxNqQoizil9QrBB4DwKOuvMRwC4ha9Ks_B4qTA6iPnUfyGw5vRa6fM6MJS9bhbHnrBmDQy06jvGFH1cDd5cKiTvQvcBh1IeqNoHIsCIhjaUTkTNEoqB2fnAWeZJyTknW-JMXHu32BYLwMa9-5YGFuFvHFCN28UBeVUhrNInfgUPnSz3FC0IMl_3yk1OU0AXFj3kio_VOItl4eTJv8qCaPp49w9s3Z4kKBCdIrplw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=Hsz7o_iEZ4EEWzuvsmGrGd6fPh39PWUUWnvFefW8dAG0u8LVTK6ltmRcHXbZTIxk9LJWUaW-wHVBdbLWbq6f5ABcedO1VF_ebZ5JN8a8JDJBJQPxNqQoizil9QrBB4DwKOuvMRwC4ha9Ks_B4qTA6iPnUfyGw5vRa6fM6MJS9bhbHnrBmDQy06jvGFH1cDd5cKiTvQvcBh1IeqNoHIsCIhjaUTkTNEoqB2fnAWeZJyTknW-JMXHu32BYLwMa9-5YGFuFvHFCN28UBeVUhrNInfgUPnSz3FC0IMl_3yk1OU0AXFj3kio_VOItl4eTJv8qCaPp49w9s3Z4kKBCdIrplw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه با مدیر داخلی بهشت
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67100" target="_blank">📅 20:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67099">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=KFAFAT4eYjBLb0-7a60bmh4ZQBSBLME7Yhuaegv-dSspNeHc4wqge9IplTwhYcrEzORTL8FJr5yBZHzlk64vwrk89SHLqKQafdkrfI69G1XvwFMRvkgf2q4cdY4KWKxnczrmvE40cKHJRlcfbnV8_BOhmFENYvI-RhxuL2w2rbCVRR1fvnzrPqJpJSiotEPc2GnZfksGhZ7vY7ob7XCaPKqJvK8FlzRfOZLQyyEj9E8JgPWLSQduxBhD-D48lDifgO8ptTeSiHXojEv3zZI2K2nhOivc4kEwBdoVOWlI3456IKScEbmhOZVgPavRbaNIAn2eYBR0M31CoHqxVQWOew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=KFAFAT4eYjBLb0-7a60bmh4ZQBSBLME7Yhuaegv-dSspNeHc4wqge9IplTwhYcrEzORTL8FJr5yBZHzlk64vwrk89SHLqKQafdkrfI69G1XvwFMRvkgf2q4cdY4KWKxnczrmvE40cKHJRlcfbnV8_BOhmFENYvI-RhxuL2w2rbCVRR1fvnzrPqJpJSiotEPc2GnZfksGhZ7vY7ob7XCaPKqJvK8FlzRfOZLQyyEj9E8JgPWLSQduxBhD-D48lDifgO8ptTeSiHXojEv3zZI2K2nhOivc4kEwBdoVOWlI3456IKScEbmhOZVgPavRbaNIAn2eYBR0M31CoHqxVQWOew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏در فضای مجازی این ویدیو به عنوان لحظه‌ی ترور خالد خالدی نیروی جمهوری اسلامی در پاوه منتشر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67099" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67098">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDZ1UrI_BZQQg7-wVst7baIl9hj2X8xyef4J4XlyViqHlP_3U35l4e6MxVtpd2C_-JIZKRZQ5JoXALOMLgL9qHlCC6rjDZDIZ47Q1xaoRxAZAo_e2MQEMZXgfg_7gxkqZmt8ZcatovWjP44by-_NcYo9Mc9C7gHWsfnVHfV9HVnM30FzJy7Vn7AQxC4TrXRSV8WvMuGLfq-B0WN9tRxWXssuCbIzshX21OgpPrg0s2Gvt4vXUWfTW9g6_AVHS8Q_CfRj_WgtyaaCqwVwDsPPyrdlE5xothgSecaqwTHvVkfYhVUZsCyWCp-ByyX4cP5DHscgvJge3F-v2b81cgDEtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
علی حسین قاضی زاده تحلیلگر اینترنشنال:
‏ایران اینترنشنال نسخه‌ای از دستورالعمل محرمانه شورای عالی امنیت ملی را مشاهده کرده است که از مدیران رسانه‌ها می‌خواهد طی ۴۸ ساعت منتهی به آغاز مراسم تشییع جنازه علی خامنه‌ای اخبار مرتبط با مذاکرات و توافق را از اولویت پوشش خارج کنند و بر پوشش مراسم متمرکز شوند.
ساده اینکه از بازماندگان نظام می‌خواهد که چند روز تکه‌تکه‌ کردن یکدیگر برای تصاحب حکومت را رها کنند و به چال کردن رهبر ملعون‌شان مشغول شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67098" target="_blank">📅 19:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67097">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEHN_A7UQIMWxpte8Q24rXzd3Hj8FiqytTRRS-OFcVr1lux-W_uqBBa2HVu28WhSju3iH2Wk0WaDRA14GVPlucoXaQfq9lerVFU6UhS_4loW65jJ3bcCMYdncyuldvTih_J4WC1-Z8RYtWb5R9-Q2vpOFI2OhOdanqQuNxPpflFnbkp1nnE7D7ZhSbuX-roe9hSZxK6i2o4zaZiLs_L0j93yz_RNYHFaldtZlnp_7eDJMlPv2NwA-OE0tvoD9wpSZragO-4NHmK-FzBq1XA1YHBjSgN8y7EDC9oAKCYmS5ei7HNR6yAIa-r0zmQr0x-ZKUM9UzHQd0Ru84-mq-wSLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ناو آبی خاکی «یو‌اس‌اس باکسر» آمریکا در حال نزدیک شدن به منطقه
🔴
بر اساس گزارش‌های منتشرشده، ناو آبی خاکی «یو‌اس‌اس باکسر» نیروی دریایی آمریکا در حال نزدیک شدن به منطقه خلیج فارس و آب‌های پیرامون رژیم جمهوری اسلامی است. تاکنون مقام‌های آمریکایی جزئیات بیشتری درباره ماموریت یا مقصد نهایی این شناور نظامی منتشر نکرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67097" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67096">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=IeFMOgRvc6I2GL-Ciqt_LzBWCdjKRiA31smg8P301sGDsS_GX87bS2LaCWz_rGF3iLpsDtMVyb_xGdN65ZMWm3oCGIVCSNaxYvPYMFL9PvKNR5SqIHx6tktPTRsWPefMVyFKQRRzT15hca3vOW3wkGjP7DyUSV9ZzXd_a9E3gwLy0GpmqfLsIsSp3FpmoHyjm4Ob8VuiZg0ZghDE_AHdNC86hAhQt64g_eNU_Mh67LJaTVP3r-puioKlOaxj_4AvF-_sDM0aNqVLMS0m1vkLH_O0R8zRHGsHwYsqm4nXU_UYxbMAfEgyRMQLvSnq27nSAx-RBY3DA44634S4Vs1DVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=IeFMOgRvc6I2GL-Ciqt_LzBWCdjKRiA31smg8P301sGDsS_GX87bS2LaCWz_rGF3iLpsDtMVyb_xGdN65ZMWm3oCGIVCSNaxYvPYMFL9PvKNR5SqIHx6tktPTRsWPefMVyFKQRRzT15hca3vOW3wkGjP7DyUSV9ZzXd_a9E3gwLy0GpmqfLsIsSp3FpmoHyjm4Ob8VuiZg0ZghDE_AHdNC86hAhQt64g_eNU_Mh67LJaTVP3r-puioKlOaxj_4AvF-_sDM0aNqVLMS0m1vkLH_O0R8zRHGsHwYsqm4nXU_UYxbMAfEgyRMQLvSnq27nSAx-RBY3DA44634S4Vs1DVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
مارکو روبیو:
تفاوت اصلی این تفاهم‌نامه با برجام اینه که برجام یک توافق واقعی با تعهدات و چارچوب مشخص بود،
اما این یکی عملاً چیزی جز یک کاغذ امضاشده نیست؛
متنی که فقط می‌گه طرفین قرار است درباره ادامه گفت‌وگوها، باز هم گفت‌وگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67096" target="_blank">📅 18:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67095">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=F6YEBTeSEdp9UNFD3LJq0ieFc6WFB8tzSRFbCxIfaZ2HuNoIxsFZSBbbyFq7MV8Bbi19EcoHvCwnhad8Aa_I63YH9dpkO9oA2HmCD1M1MHu0caz2vCl9c4fRLTFZh5O_CMzR8rVxLCWKUsaiuUnArK8XZ1SXbCzsoe6qs2uOBJMZVHspdIxRlmOLcb0kAzGsMI5ilhoQEQVv-k7cKL9eBL4KRoLE6rAqk5Yslr8Bklv29p3UNBC8bDZ3W785ufi0wr5NXrVFZY0n0HpH4o86v8CuWWnd15h-dw8-iHIsxzDdmwRm61vrtqGlH-lCD-i_EfK4zC-s7IrinyaGcAlh_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=F6YEBTeSEdp9UNFD3LJq0ieFc6WFB8tzSRFbCxIfaZ2HuNoIxsFZSBbbyFq7MV8Bbi19EcoHvCwnhad8Aa_I63YH9dpkO9oA2HmCD1M1MHu0caz2vCl9c4fRLTFZh5O_CMzR8rVxLCWKUsaiuUnArK8XZ1SXbCzsoe6qs2uOBJMZVHspdIxRlmOLcb0kAzGsMI5ilhoQEQVv-k7cKL9eBL4KRoLE6rAqk5Yslr8Bklv29p3UNBC8bDZ3W785ufi0wr5NXrVFZY0n0HpH4o86v8CuWWnd15h-dw8-iHIsxzDdmwRm61vrtqGlH-lCD-i_EfK4zC-s7IrinyaGcAlh_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی روسیه در زاپوروژیه اوکراین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67095" target="_blank">📅 18:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67094">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=BM-l0GKyyXPspc8z6DI9hceWIpDiCTd-mrsp-ZKuNLhcb8rBD7pBxoDx9K8idMLdxXnZE9QZysasAUR52m-Y543fVX6c15K6fgAMvEfLmuth7p4mEs-NaYuBIYeNQoce_aa1SZPjldrnTHmXoVT-KfmybFiOpH4elyxiFCT4zarJJo6T8XMCr_TS45m8EFJeVvT80EKOZ9X3os9qylpm5fe2rJGD1BL691QpqKazdfC5Vx84lpbvMzCzqLJshd9CPeWM8KQQqHCJR0Q4kciydpm_ryrTS0hWneKQfTUWFhYMl4B1sohmpmlBX4ei9h3vF2KZDFlZ9izOFKuOnI8yCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=BM-l0GKyyXPspc8z6DI9hceWIpDiCTd-mrsp-ZKuNLhcb8rBD7pBxoDx9K8idMLdxXnZE9QZysasAUR52m-Y543fVX6c15K6fgAMvEfLmuth7p4mEs-NaYuBIYeNQoce_aa1SZPjldrnTHmXoVT-KfmybFiOpH4elyxiFCT4zarJJo6T8XMCr_TS45m8EFJeVvT80EKOZ9X3os9qylpm5fe2rJGD1BL691QpqKazdfC5Vx84lpbvMzCzqLJshd9CPeWM8KQQqHCJR0Q4kciydpm_ryrTS0hWneKQfTUWFhYMl4B1sohmpmlBX4ei9h3vF2KZDFlZ9izOFKuOnI8yCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
پلیسا شوهر طرفو دستگیر میکنن زنه یهو میرسه به پلیسا میگه وایستید لطفا میخوام باهاش حرف بزنم یهو بعدش...
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67094" target="_blank">📅 17:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67093">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⏸
🇺🇸
نوه‌ترامپ رفته کاخ‌سفید گردی و با این ویدیو مکان‌های مختلف استقرار بابا بزرگش رو نشون مردم داده
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67093" target="_blank">📅 17:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67092">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c791837da.mp4?token=FFsI3xkrixqvuPaYd_9N6zJUyt4wEK1s8SFYWqndCGg_GbKk4npR_OEvFlJrwAmucKmYooc8HuW-g4a9lT8WrHaDZZnYIgxJWy3Dnhxck7gMd7m1yguftmIU9W7CriF2oJZSb7ce9yzouvb4CJf2xpxzmO6Q9kyBb4B2ab1QX9jaKCJrPSx107cko943DYJCb37MdPCoHKlxP_JFiLKCeeTZPfiLZrvDiBUFCYiVI0NT51HQ3n3I5NUfMROgjLSxjDqIZMz58RGZonTwT6GuA_8U1KfU4C9o82Y2-I7sKQ5IV5AOV7R3LIIw5gi7lUsVqVRjs7qdrj7RmR-Wlg5wWGkauowyyH9YpnJC69dK51Tb1QcJxHrLQvaa3foS-DJdcZkQXkG7EviY7Ef77ZQyReOhJ5JPiHntD_sJFe1uHLf14o8ux2g2SgfF5C8KidUC-M6mh-MC5truMfw4mieZV7WQzptisW7F2vsm3J3FooGNF_a8hifSnMZgV7C9mtaiCpRBBKTgLy_AU2CAEZwLCgIOQMbskbF8QCVyF7rfhOBjUiCdu69_1zEL2g_uy037wWYuM-KwOkFaWTQKHk4NpzjfYnWEo_sMAQrnlwaGQWVJJRC17imcoxo8QMHMQl2CZrIXlb630I9S4XREJB8vXJ8ThCWLPJ1PFDkGP5rPORU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c791837da.mp4?token=FFsI3xkrixqvuPaYd_9N6zJUyt4wEK1s8SFYWqndCGg_GbKk4npR_OEvFlJrwAmucKmYooc8HuW-g4a9lT8WrHaDZZnYIgxJWy3Dnhxck7gMd7m1yguftmIU9W7CriF2oJZSb7ce9yzouvb4CJf2xpxzmO6Q9kyBb4B2ab1QX9jaKCJrPSx107cko943DYJCb37MdPCoHKlxP_JFiLKCeeTZPfiLZrvDiBUFCYiVI0NT51HQ3n3I5NUfMROgjLSxjDqIZMz58RGZonTwT6GuA_8U1KfU4C9o82Y2-I7sKQ5IV5AOV7R3LIIw5gi7lUsVqVRjs7qdrj7RmR-Wlg5wWGkauowyyH9YpnJC69dK51Tb1QcJxHrLQvaa3foS-DJdcZkQXkG7EviY7Ef77ZQyReOhJ5JPiHntD_sJFe1uHLf14o8ux2g2SgfF5C8KidUC-M6mh-MC5truMfw4mieZV7WQzptisW7F2vsm3J3FooGNF_a8hifSnMZgV7C9mtaiCpRBBKTgLy_AU2CAEZwLCgIOQMbskbF8QCVyF7rfhOBjUiCdu69_1zEL2g_uy037wWYuM-KwOkFaWTQKHk4NpzjfYnWEo_sMAQrnlwaGQWVJJRC17imcoxo8QMHMQl2CZrIXlb630I9S4XREJB8vXJ8ThCWLPJ1PFDkGP5rPORU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
قمه کشی ارازل اوباش میان مردم در شب عاشورا رودبند دزفول که با دخالت پلیس خاتمه یافت
😐
😂
تاریخ ویدیو 1405/3/4 امامزاده رودبند
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67092" target="_blank">📅 17:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67091">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=Fw_wQsv9GPRtMy95lVPoda-9Zcj5pVXJmfze22YGqX6DnUorVi2hg17IfJVdsA90jTUtzcBh6WKbISwbCX9EyoCb9kbAdiomD_9O3qGu6Y5buACyX_jH4mnXxy8f0Ck8iVcG3iTFOX55IYUTA3t2TPg0VUvlnnnapg_JOcAJwJ6AyQPcmcTDvLiljBntCyxApWJD_KPHapLLIh6Gi0hn_3o-qTaKfFAa9FgKIUfuhFL0LuJIuQIcwgDwc37m1F-yPgaAd04aysmlxcNY6o7UmvHgnbV-MszfYR5JQ-f6yvI7_qGifWrhxe6xmMEWXkQ3EXdjofqDzlVvMgLds_AOxQztTJTW8IHWv2nA6oMwC1g9JIDDlekmg7gCSLND33TjtBqStjOLcIOwdja74FZsBUR2CBlS80GJ1PuoyL8v9NXFd8d0ffmlzlTQsClTL6xZs75RAG6pPFDO4ZbmmWQh8RHMVr-ZFXw5tj0FYurKH4ZnipvIQaRBiA1jeEnMW2LM6McgI1YWxaqvllA9iaYmqjqjqMlqHBpW4qP_vXJvXDHkJiDewxi5MNq-2P-sbOBgiWv5_Z-ozG1ykerDAs7UqmKtOT6xtxy1b3stVywRxo6oECDEhBSPA9GUvl3ra_L3cVIq3M5-pwkZUlYVlxbcarXxsH6e75yE7LIWw85fXlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=Fw_wQsv9GPRtMy95lVPoda-9Zcj5pVXJmfze22YGqX6DnUorVi2hg17IfJVdsA90jTUtzcBh6WKbISwbCX9EyoCb9kbAdiomD_9O3qGu6Y5buACyX_jH4mnXxy8f0Ck8iVcG3iTFOX55IYUTA3t2TPg0VUvlnnnapg_JOcAJwJ6AyQPcmcTDvLiljBntCyxApWJD_KPHapLLIh6Gi0hn_3o-qTaKfFAa9FgKIUfuhFL0LuJIuQIcwgDwc37m1F-yPgaAd04aysmlxcNY6o7UmvHgnbV-MszfYR5JQ-f6yvI7_qGifWrhxe6xmMEWXkQ3EXdjofqDzlVvMgLds_AOxQztTJTW8IHWv2nA6oMwC1g9JIDDlekmg7gCSLND33TjtBqStjOLcIOwdja74FZsBUR2CBlS80GJ1PuoyL8v9NXFd8d0ffmlzlTQsClTL6xZs75RAG6pPFDO4ZbmmWQh8RHMVr-ZFXw5tj0FYurKH4ZnipvIQaRBiA1jeEnMW2LM6McgI1YWxaqvllA9iaYmqjqjqMlqHBpW4qP_vXJvXDHkJiDewxi5MNq-2P-sbOBgiWv5_Z-ozG1ykerDAs7UqmKtOT6xtxy1b3stVywRxo6oECDEhBSPA9GUvl3ra_L3cVIq3M5-pwkZUlYVlxbcarXxsH6e75yE7LIWw85fXlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
😳
عاشورا برا این اراذل هرچه نداشته باشه یه خوبی داره و اونم اینه که تا سال‌ها سوژه میتونن دست مردم برا خنده بدن
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67091" target="_blank">📅 16:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67090">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=YdCHMMupDjfwW8PJ2yGPZGSmcP0cWrLq6baSum_kweOtlzPi-jJCjC11JPPLclSW_4nIVE4UmpGBV1vMcCXs5oyHTg5vHJeQECOAql_7jE13a4n6bPFjEN1HeotWlI2IoS2S_CfqHSSP-egP8KcMOdI8WokrnrypMmFU66kPyeamvlYCc08PgC9-iJpqAdB8uEIEfEyCKeK4HPKw2lIQbY6JUH1hEwYQzmo3Cu6vtqj7XuBj_qDXIf_IqNPAV44MDBOhzWMWEuISBWRIGZVfg6mjMCaoB2S1IDBXLtantQnj6nHbTQOOw3XoVMW0TnMK3oc7ZqqbjkVOi8Mdhnleuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=YdCHMMupDjfwW8PJ2yGPZGSmcP0cWrLq6baSum_kweOtlzPi-jJCjC11JPPLclSW_4nIVE4UmpGBV1vMcCXs5oyHTg5vHJeQECOAql_7jE13a4n6bPFjEN1HeotWlI2IoS2S_CfqHSSP-egP8KcMOdI8WokrnrypMmFU66kPyeamvlYCc08PgC9-iJpqAdB8uEIEfEyCKeK4HPKw2lIQbY6JUH1hEwYQzmo3Cu6vtqj7XuBj_qDXIf_IqNPAV44MDBOhzWMWEuISBWRIGZVfg6mjMCaoB2S1IDBXLtantQnj6nHbTQOOw3XoVMW0TnMK3oc7ZqqbjkVOi8Mdhnleuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی وزارت خارجه: اساساً برنامه‌ای برای دیدار با آمریکایی‌ها در هیچ سطحی نداشته‌ایم که بخواهیم از آن منصرف بشویم
🔴
گفت‌وگوهای دوحه دربارهٔ اجرای بندهایی از یادداشت تفاهم است و با هیئت قطری انجام خواهد شد.
🔴
اجرای بند آزادسازی دارایی‌های ایران در حال انجام است و امیدواریم کار به نتیجهٔ مطلوب برسد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67090" target="_blank">📅 16:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67089">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaXqGukL6rG_7m9HRdr86J_rAXuj2r4b9SilbawWwRo5-BZja9mT3C_jDG1ihrjIszdtDC8vbPt0sZY7f7kWNSEHl7E_7z9e9YTzFHzKihaEYLfO7m7EKSUHZWpDnhAydC-TgGkNTFZCvddL_l6Ec9pkSz5gzX9zEI27wW6m2p1teK4F1aGMdj4WVSoFWmkNL-LqLy33zqaQqFIsWfOvwCZ6-LyPFKOJReRAfiyXgb8VBz-NYUOm8jlnKdeXUnSZj32l_32MHm-ufIKhMMsyfpexvOfKup3n3mOqos_8opSnJ5QNZs4w84B0kITPScJSl9T7qhZNuUx3AA5pbzJ4rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
مذاکرات غیرمستقیم میان هیئت‌های آمریکا و ایران فردا با حضور میانجی‌ها در قطر برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67089" target="_blank">📅 15:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67088">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sq-C4Cw8Zdj4EAOALxa3A1Ft1RVwzVcpvcdGa8lQlFweqq91JLHu2_PEBNHG8Rh_1kkQljUQZlSmTbnBYQqvBcAFqQcIM7x-Y0Xl8gV1_j1CVuL_ny7SqoMdopLcnBQA-IrWhKgbQyJX3QyRSpPrHlc9u60XgYGaKBfarVd5fS4rfI64zuQ24Adj1iC3AfKMIVP1vxaSjv4rDyjGF8gvxdnBClfrwCuTex1P1B136SdU_MjLrjJw4Jq96hpeaufzq85NHCvAylUi8zKfwVdIDjkJQdhGfXmRAkgOzXhLA5v9JbNU4BB89x9TAKUAGM6QpR4Rj9s4JDYTSMVPWURATQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه همشهری با این تیتر ترامپ رو تهدید کرد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67088" target="_blank">📅 15:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67087">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=RyrnEI63sLAUzN4WTEonJPqz9Dew91zfVuOmPZc9VvZTrHbuF3JO2hPCrBE8WH9B718kWK-yPS-RBlPsez9zEFNmMQTQ-FUeHTk1Q67ZLYmCKoF2wn0dlpdLpoRoi_-lQsXw55GOqW8gN29cJLvYJ9dE-4zo5Y7zlzhYJUWYDSnDsB_SfjF-DU1dfWjJcS1KG-ENWqqMhLQrOnkHCqzgqt6naksA6fVqb0kXQkOPIsEy3BeK-YQPwKu1MUYUea03R-E2JyMuXwygDhP0iY_-puTtkYSEYZsF_AaLqFEIZeYpKh7W5pllU8jLTmUPbDuJfL_tYUsumUWpbZGRYaBV5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=RyrnEI63sLAUzN4WTEonJPqz9Dew91zfVuOmPZc9VvZTrHbuF3JO2hPCrBE8WH9B718kWK-yPS-RBlPsez9zEFNmMQTQ-FUeHTk1Q67ZLYmCKoF2wn0dlpdLpoRoi_-lQsXw55GOqW8gN29cJLvYJ9dE-4zo5Y7zlzhYJUWYDSnDsB_SfjF-DU1dfWjJcS1KG-ENWqqMhLQrOnkHCqzgqt6naksA6fVqb0kXQkOPIsEy3BeK-YQPwKu1MUYUea03R-E2JyMuXwygDhP0iY_-puTtkYSEYZsF_AaLqFEIZeYpKh7W5pllU8jLTmUPbDuJfL_tYUsumUWpbZGRYaBV5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ویدیوهای جدید از زلزله ۷.۸ ریشتری که در ۸ ژوئن ونزوئلا را لرزاند، در ساعات اخیر به سرعت در فضای مجازی پخش شده‌اند و لحظات پرتنشی را که در طول این لرزش قدرتمند تجربه شده است، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67087" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67083">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUrHRkb-mwRWiCBdVCYgKj1YUzTwlPHLbG8AT2voNGjZHe1gK_Xseubde7kwMyJ2zoZznkBXOzdiEzRhKocXQwDfrpfutnilerTuynJhs6lI0d0hoBfMlbWGHKHG-Rb0PoSKBXRZE4KRxVbLAKWJfO4IaIdu9VDdw9GsDtyG_63tirEzf32hccbOjWp_14o6phC1kCkVKtJOudl31sS35QO7_njXVX_W3Wao6_GabVGOyxDhkwb5tahqiMYDLRUx6aWKVtIFGA2moeZzAqlpkou9JypoBNRPYf0_7WNdD5zraN8uyHwrVekZDH7mnnSd-z5mru6cLiUFsmKBXq8mkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXMz8sFhnUfdE94fIqe7UtVcy3Ft1m5AvbQyFkj4RvVd_nnfTM4I_rzZQ34BYsFY_pn5K2G3D-S0XTpKNqqj1kGOsJq-Wg0xfiYjzCxU6YiGsibpIy34UFy2dWC9f4kYht1VqSq2NJtlmvUYQa_ApO_cuDgOJK8zpippgQikOL-RfeRWxTwIgyro00Lln_2RZaL53ZyXmYNffMceltPuM8fznaYPPk7tLE0alwnhpicNGLhYD3BJLTfV8H8YWs1ipG5BuUUi_yVYEFyESWOOdoy1ma6uoVxDmwbSeoOV4bLZQpnlBxkc9Rc1_dwp1QQT6Kz_yhmqD4Ecwd9iN69jKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYWqdwMOu2WZi36RPtr8ImcHWWZ66DGahqbUGXFkVn01_YMx26ca8gWG3MncfhU8BQQVRwHkrmS6VggjZT-AmQ5M1nxpwd472g3shWvrUJ4TDR2b-vtc4yPSdkt5A4OaXnBxH8PLllEdYKWBhqXYlv6COACNmOyO_W0BbS6Cn_e0ct221Fk_G65uDnXbvyXlo5qVFVBsxhNoJ_CUAtG-45ZIsIn402ZfC7XB-54XGcx5to14uc0696picbkjoj6keJM6OyIg6kxtcS-EZr2GKy7FqEqulTzoYFITGR2elWdtZJMn5zidDXUBCL1L_w34LYvCVhhBb9UvWQg8x-MJdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKSo4upw_PyqDN_Rm4ZxsRb04-InHS_f1rSoc56bh6FfDYYVJPmI8QXDiCcsYFgack1kXBOx_XSJcKuNZBflGQzJ_c-p9LCsat_eype789UriAsgHIy7IKTcZxEKcJRRKHqm9pOospg0KDTg3qUE8mnrRjCfD-T4u1vHeuDFTlUVr6fx4JAWHEmbcAJSa1SGO5gf5uAr0CoAqxSoavLf46pPboh4TutH3nXqSSVm-Vem5DSZIjoimDdiHcTMm5X7lIKM92kyg-u9HlThtA7gwjnC64PqKpK4G1IDzdettTUvsvigtpX3rtg3gfZ9023RjjjcIdvvMr1Q_v5KEgS2VQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😂
یه پسر 19ساله به اسم آقا سامیار، اومده چندتا عکس از تولد خودش به همراه دوستاش تواینستاگرام پست کرده؛
حالا به دلایلی نامعلوم، این پست تولد آقا سامیار تو اینستاگرام فارسی به شدت وایرال شده و بیش از چندمیلیون بازدید گرفته:
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67083" target="_blank">📅 14:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67082">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
⚠️
قالیباف: سوپرانقلابی هایی که هیچ غلطی برای این انقلاب نکردند، ازهمه طلبکار هستند
این ویدیو از قالیباف مربوط به سال ۱۴۰۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67082" target="_blank">📅 14:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67081">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی وزارت خارجه قطر :
هیئت ایرانی از اومدن به دوحه منصرف شدن و مذاکرات لغو شد.
۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67081" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67080">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
جرد کوشنر و استیو ویتکاف، فرستادگان آمریکا، در دوحه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67080" target="_blank">📅 14:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67079">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
هیچ نشستی در سطح عالی میان آمریکا و ایران برنامه‌ریزی نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67079" target="_blank">📅 14:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67078">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IqAe3lIZ0ZhbgicYvWwx4U202pTRl-LxHM_NqBNGRhG0Ad1xVs-Y6fF6XilUsgolp0Zn2_xE60oK7kqtrHnuvp0_CXI6QzBKxc4pfKoXH4cLGeNml9Lgj1Zcfy_y9Q7PulA4zq6zlq5UTgBfO7g8SusgcZwQcy2kT8VxeDNYytLhNI4c4Qd0KinvUC5IiZH2-Z4mZmJQiFM3-TWb792rdSVwy_wfE-dStR3Gmb4a_j98K-378xsCqwkR1Em8osJFeIjg8vvQdOKOS9gT2ffkDko94UIWOvdtSajZKa0QuMA0J8xH-ntQnt9UapJIi_UALsd1RG4050Bc-FnMK65FBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افت رتبه همه دانشگاه‌ های ایران در رتبه‌بندی کیواس ۲۰۲۶.
این فقط یک خبر آموزشی نیست؛ گزارشی از هزینه انزوای علمی کشور است.
رشد دانشگاه‌ها را با قطع اینترنت ، فیلترینگ، دیوارکشی دیجیتال و انزوای دانشجویان متوقف کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67078" target="_blank">📅 13:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67077">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d67KAyqTyNGxD0ZlN3R0g8fUfcnzaFO2_WYj3zZ5XTigup88qmvVDj1d5o2z5NG1z93voHWe76fGJJ_zE_WfrtoXiRcRv7bwo4CRBCi4PIjAM0FgylPlJC3_rer4aipAuIPD2M44TYekdmt1MU_TRT45lNlR-oLC0ss9cfpO-t0iLxYUi3-jmSEOQvsu69JJ0sETMaRmCJeEEXp_aW0NpYR4dzD6qHbZ-yUxLLufhYQ4sTPwnK2dX5Cu1QvMVQaHM3hNfeSmF3lAA5eairAM9qqIhKQZ7GHAWj9KZyTuu4UPndywDNXX7-DeQKv4yiJsOYYvPz6g0TnlaGhNW9eVOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
💢
فرماندهی حمله جهانی نیروی هوایی ایالات متحده برای اولین بار تایید کرد که یک بمب‌افکن پنهان‌کار B-2 یک موشک ضد کشتی برد بلند (LRASM) را بر فراز اقیانوس آرام شلیک کرده است. ادغام جدیدترین موشک ضد کشتی آمریکا در این بمب‌افکن تاکنون برای عموم ناشناخته بوده است.
💢
نیروی هوایی ایالات متحده اکنون توانایی انجام حملات اشباعی ضد کشتی را مستقیماً از قاره اصلی ایالات متحده دارد، در حالی که پروفایل پنهان‌کاری خود را حفظ می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67077" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67074">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmKgJjNScNObnQRGl08CcJDYjUQ5hwkYzLuGzXy6ZmMsaFF1zGwmd05v2bi5wrjtfyqpJijbM2jThbDBfLIq2wmhcrQuChmowVoEEDiD7WBkOZAeE6wYPqIepjHjG4cKRz2c5aIgpXIJb135waaS3BUkvYQtgRG8WVaI4ndNKRCEb_LAUlTtr35wHMrSPkenKPjuIYI7lMdJrn1bMtxdIB_6E0VYU4URQtFgdHEWnKSg4KiVPoU7oLjxsdI81wM20FOGB9Q_94hpMdLkBRMOhm-ZZwhil65Yl1yHSe7euBoowLdcvGeW_AxL5HuVsUffiCa5zieFsKUr9GdHcChs8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚠️
🇺🇸
مولین، وزیر امنیت داخلی آمریکا: خیلی خوشحال شدم ایران از جام جهانی حذف شد. انقدر خوشحال شدم که رقصیدم. نصف اعضای تیمشون سپاهی بودن و هربار برای ورود و خروجشون کلی اذیت میشدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67074" target="_blank">📅 12:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67071">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ed-Y-_XLeTK4KYcxNXuGt5McXaVeIrxNZPp8IpjoMMC8WxFfik1rns6lZjA_HKXbjJAZUy-24Ui-QNn7w9mF6qY9wWKP8h3wcTVkm_zQuefUiblD1yk5XHEFfHIu558A357jcKN-Gtn2FtMReWQR_KWu7s3j77gO1N4FhH7YY_TjjmdwxIeqrLJglqAXn8a6pFCSC7GPP5RbJo2euHV8XyD4wOwTTyCtpYZN8w3lXUNt7S-kmXZSTVLuBQohyDQoQkrPBSAuTi8NdZYpsct7W3GqV5oKE89AAKyCkdYQnOhFLR4V1nV0R0cN2qMqmQJQQEWNrc4dEBYM7plQMcfLXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OZ87qupjkCJgdVDx8GYjiKELBs0lZEeKXckHYCDVP17Ki1SesyJhLIxwFVBn5DeMLW8ugmHjVyDpOXdOociVvHl73TbzhDH9fy5Ox0lBQk_Qrl0L_KPuQf2BSXjZv6fThEqAwwx8kSTb8dI-mBegT8wYAMGt59opS6Obt5nFpPnC87VC1ezvgFzmFgm1IePeo-XpjRzN6ywl7ZUV-rCXCqxRrcbiaVCbc5HIDRAFqFCTbFlEP1sAtwVCp4vCKo1oWSI1PnDMxUf2qiwX--ADaiB_2KzK3TJ4dHtoE0epDMMoepjsqsp3Jtcce0kDCub14EI4QG7bDCFtzZEERS8W6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ME0sZIBBhqLX_q1ZWOzQZIH7KxKoOlbBvXum0xk2NrObsQKq_CGYe9rG0op_G021d8gCkNZkSEeB0Tlso5e4OXfnm9jmyppzWZRGvlDqutlF8PiNNTrRc0lYwTPRu0N2Q84MKLYUyAyfRteSKkcSO7murexW9kxWC3kSSj4FkIoYiio4G-y3Dj-qD1bKZlAH877bjiB6-nngnv2UN1fk6bwzrI3c6avpua-dAQiOLfuuc2aAzd4F_vYZYq3td3X_8zGf1MYkNXzCoh09SAiy7CVwgjkw7UiWcAXjPKcCxpjCoemFJxnlyuy-cTNkjhPiYLNeVyRonf7OVokKwn4UQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اشتباه نکنید، این زیرزمین خونه والتر وایت نیست، این بخشی از دلارها و طلاهای کشف‌شده در منزل یکی از نمایندگان پارلمان عراقه. حالا شما به این فکر کن توی جمهوری اسلامی از دون‌پایه‌ترین عضو  تا کله‌گنده‌ترین فرد چه اموال و میراثی از مملکت رو چپاول کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67071" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67070">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsZ4Ms5k7aOt54snQlmoww3I9iCX24OfuOJ7qmG-UHUSnms-mAWhnUPFcJYYHeqWGxoxiJ1gTtdmdaEfqX7a0pVKrtr0CuNDkCrcnB0HB8TrLaXUj8opk-Qv8v1jeOLb46HS23EvbQYVWRHnGG2AHqBIuIj7hQRwq9Dk66wHAlZRCPost5wLwywdel7bebfN_SILEu1d9iah2stqyd-QPQnvfMLSVVeoVD_koSUfMjV1ewdfIdkgWQuQ83qc0ML1ATV2YQlr2pH-j77PPxCMfW6zUIPnJg_LQPIPjgc7ii7m9bXCl1x1XuW0mBX27JtuE5-VCVdsGbs6iiOy2uJqsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
اموال کشف شده تو خونه یکی از نماینده های مجلس عراق
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67070" target="_blank">📅 10:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67069">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=hiyCCw1XRnM9Z57iv9UuVEaD3IPKeUiq55ZTtGyWx3PmQ2lCx-hCqh32SMx0fa579SHY5APmE5eosczThDUbYtGtCQjJfyeplJPZKT4eYI_fsZbYO_sIZQj2wltL7oMiEC1oaoPGn-ntHJhFeWG2N3-80N0HleTvkLcDEjk3d0gsuBlFdcjuoRxAQXNXMZqC33cDWPHNH8aQ6iB88M0evtk1GL-zKeQYIjC9ivl9MoPVXsSvhUtk11REowdiPCfl-KKOO-4MwSJlLkD0mMMfUx0F2EjAjeYKnHRv7kDEL76clGJPRLOTmjlSUeY1rk-MIYwQ1BLeELt-mI0CYvCiLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=hiyCCw1XRnM9Z57iv9UuVEaD3IPKeUiq55ZTtGyWx3PmQ2lCx-hCqh32SMx0fa579SHY5APmE5eosczThDUbYtGtCQjJfyeplJPZKT4eYI_fsZbYO_sIZQj2wltL7oMiEC1oaoPGn-ntHJhFeWG2N3-80N0HleTvkLcDEjk3d0gsuBlFdcjuoRxAQXNXMZqC33cDWPHNH8aQ6iB88M0evtk1GL-zKeQYIjC9ivl9MoPVXsSvhUtk11REowdiPCfl-KKOO-4MwSJlLkD0mMMfUx0F2EjAjeYKnHRv7kDEL76clGJPRLOTmjlSUeY1rk-MIYwQ1BLeELt-mI0CYvCiLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مداح:
رو هلیکوپترشون غیرت داشتن بهتون حمله کردن و علی خامنه‌ای رو هنوز دفن نکردید.
۱۰۰ میلیارد دلار پولتون دست اوناست، و میخوان ۶ میلیاردشو بهتون سویا و ذرت بدن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67069" target="_blank">📅 10:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67068">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=j3MVIyFlTwgCNgktsYjYb3uc22HHA7tA2ArKVSJ-kMUOoArw_y_Y0kl7AAlxQEvGA2Hew5Mu54hf-C8_lvhpHByraBOd3DgoHue6SY_5nuAoeCDLHh-IKHWM074MSebjWy7jH6m5-s4jjDCw3VlqCvtYS4theG9Z_M7S2ys6WMlUJhBmDqNoPZNknvk4piQ7l9bq_S_Zxyc5pRSAApBa6rzUIPZxu4q9pxLqExn4KS2YPZNcZnHkEh3zPEB-T63PwihGhkcZ5M6BQzEU8zXreZOQhWtObQgqw5fwOTqZZgGajXItVMWzyiAFIUXLS30GbeQOr_a9urIbe39yG3xNsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=j3MVIyFlTwgCNgktsYjYb3uc22HHA7tA2ArKVSJ-kMUOoArw_y_Y0kl7AAlxQEvGA2Hew5Mu54hf-C8_lvhpHByraBOd3DgoHue6SY_5nuAoeCDLHh-IKHWM074MSebjWy7jH6m5-s4jjDCw3VlqCvtYS4theG9Z_M7S2ys6WMlUJhBmDqNoPZNknvk4piQ7l9bq_S_Zxyc5pRSAApBa6rzUIPZxu4q9pxLqExn4KS2YPZNcZnHkEh3zPEB-T63PwihGhkcZ5M6BQzEU8zXreZOQhWtObQgqw5fwOTqZZgGajXItVMWzyiAFIUXLS30GbeQOr_a9urIbe39yG3xNsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از سخنگوی‌زن‌قرارگاه خاتم‌الانبیا هم‌رونمایی‌شد
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67068" target="_blank">📅 10:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67067">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=h-dOJ17ueadMCyJ5iKq5efwS5vZPBzmPMn1nFUFjJKIZtKGOctCUHZSMobRvqydP8csl5ATykgCP9g_ogSwObzBUn_Z_mxb0mHMSo3mIIxl1F6SJlkBCfIl1BFcpeAh_OxorTuLoeT5FY-gd0v8dbfZ_LVUWGj4G8nNvjfjySXcGdVikpkFyI-hvL7936i8I-WL_y9Mxs7pNCfIi7pVdZueICG4fvtpgcLb362lFr5DsfXeNzji3PwG-dfA0YVugOKbbrUq59uDkrpcRiKZ1_CPAtMycvPQAb9L499oS1z9X1QWHnpS_kBrostK4ZgPsR-fHRvhQ1oJCFqxPrAv7rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=h-dOJ17ueadMCyJ5iKq5efwS5vZPBzmPMn1nFUFjJKIZtKGOctCUHZSMobRvqydP8csl5ATykgCP9g_ogSwObzBUn_Z_mxb0mHMSo3mIIxl1F6SJlkBCfIl1BFcpeAh_OxorTuLoeT5FY-gd0v8dbfZ_LVUWGj4G8nNvjfjySXcGdVikpkFyI-hvL7936i8I-WL_y9Mxs7pNCfIi7pVdZueICG4fvtpgcLb362lFr5DsfXeNzji3PwG-dfA0YVugOKbbrUq59uDkrpcRiKZ1_CPAtMycvPQAb9L499oS1z9X1QWHnpS_kBrostK4ZgPsR-fHRvhQ1oJCFqxPrAv7rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس تلویزیون:
جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67067" target="_blank">📅 09:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67066">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=sP9rrJn-EsLU4aaT0H_0LAq2VS68mSWbehlB55bRz6gaZRqSGJHDpNC5e7f2QyImzo1ddF9QIIMewurcl9QiOhO3-iQZ7FFpYCtCeueKTuiVpJ7l7eoHDgWA5iPZOCoVJIp23AlPjYGzwUn4Fpkc83SbtNbyEfCigvvycKzHXnKngJ1WvUNO9xFX9OFyq_HTFgW_ry7Sg9avIQ69sAfVPAEY2D-3YiZTT7OcabN43XzMGn6JQC83f6z5RooSNSzXqCien9dI6Ax3gWgsDm75TGGwzWfHdFt5mALN7FFIKjzoKBrWQtRmtMrsqKVPzJmQItHrltWA_SYhkSt3iexmog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=sP9rrJn-EsLU4aaT0H_0LAq2VS68mSWbehlB55bRz6gaZRqSGJHDpNC5e7f2QyImzo1ddF9QIIMewurcl9QiOhO3-iQZ7FFpYCtCeueKTuiVpJ7l7eoHDgWA5iPZOCoVJIp23AlPjYGzwUn4Fpkc83SbtNbyEfCigvvycKzHXnKngJ1WvUNO9xFX9OFyq_HTFgW_ry7Sg9avIQ69sAfVPAEY2D-3YiZTT7OcabN43XzMGn6JQC83f6z5RooSNSzXqCien9dI6Ax3gWgsDm75TGGwzWfHdFt5mALN7FFIKjzoKBrWQtRmtMrsqKVPzJmQItHrltWA_SYhkSt3iexmog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسعود پزشکیان در جریان مناظره‌های انتخابات ریاست‌جمهوری ۱۴۰۳ با مقایسه وضعیت امروز و دوران قبل از انقلاب گفت:
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67066" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67065">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67065" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67064">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kmqU2ZcMrDEsAbDuq11O3qmO9SXQeykHM7iLE2BEuM9X9N2y-IHPOPj0N1-Z4dVRb8XnZmpbsEixfMAz_f7rTqCCz2-i_BRImDoDkWhC27jcWP4VCi3Vv3ERemJ5Z6MyiiyHec8FW4-BLwqqRiCaB2O7yEUGvZ_WfILTCYZU8WRqZECYQprx6QSImztHAwpTtFpVy17bI1nAQogCBwXx049FGBtnHH8M0Hc56_F6m6UpBKFDqHZTb1HsmTq9LfJj_wxqfPl5AYzz7vpuQoAMcxQ90RPbzMCxYjb6wpgfC-xnrfIJAx1TIOc3n3mavh3-Dr_XCq5Q7l-05i5XHCBR8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67064" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67063">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر جنگ اسرائیل:
احتمال دارد جنگ مجدد با ایران طی دو روز رخ دهد.
وی اعلام کرد که نیروهای دفاعی اسرائیل آماده عملیات و هدف قراردادن ایران در صورت استفاده ایران از موشک‌های بالستیک خود در راستای دفاع از لبنان هستند.
او از آماده‌باش کامل نیروهای اسرائیل خبر داد  اما خاطرنشان کرد در مذاکره و اقدامات آمریکا در راستای ایرانی‌ها دخالت نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67063" target="_blank">📅 02:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67061">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hd67o7dYAGxvkTKVWdawI-2FDDqcoio0_KJUzSDQlEFUBSz3a7PDe55Zpw4jr6f6qKHWp-gSEDfpaXy0c7eLNOBc6Bta-GF_UJ6Sa0KFaPxVCiQD8uZzajx1Fb4y8y2L9CGcNBQsh54lx6Pmgc37TCxnJWik7R8y1kVNPCgc2Om_ieo4xlZG4vLfmv_jtY8ydgTnL8X01OH9iFNdhSAEPTDTWtG29fCKGHH6X9rj9c6Z7olan9CwGGXlwSGltQnU-BgQuuMavZDsWNoRXGQwiMLZxcQ_21ua9RUfXfFgJEt2jxfHi2Euu_1z2uTx0QH8-0o6HG-wso417QbJ-AJG9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری از بیمارستان پاوه و هجوم خانواده های نیرو های امنیتی به این بیمارستان،به نظر تلفات و زخمی ها بالاست.
«کشته شدن سه پاسدار تا کنون تایید شده است.
سیروس درویشی،خالد خالدی،برهان کریسانی»
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67061" target="_blank">📅 01:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67060">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
گزارش‌ها از درگیری و حادثه امنیتی بین نیروهای کرد و نیروهای نظامی در شهر پاوه ارسال شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67060" target="_blank">📅 01:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67059">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjfpGyeB3XdbuHmum4O80deLsejIpF9rHilYGsREL-jl4Ss833aAFJ2lD6GuC8zCmbIWgB4lNTjzrMVfbSy_1EEaLTtueWlJECJX12CFu1WK2WQWvglHtvFSfOhU7ic8-cvMXhwd4sleB6Gt4ZovpRLQ-CqE1D-VoVVvFRmZheCdq2VL0FDqg-9Nxql-Cy6PGKeOOxRNJajscoQSJnyj7tc4H6F42a2Mg07iAKwLPE0wMgjFTQcYMAQsyav9q0IGGxTXB6r0WwCbthyHcg71PAPrr107sDyUNPYjfaQIfPN6O_KzH6Hza9DLAUZ7wNsXpaAQKY3_5uZgKGmzuMd92Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
تفاهم امری طرفینی است. اگر طرف آمریکایی به تفاهم نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم.
رویکرد ما در مقابل رجزخوانی‌های نامعقول و تهدیدهای بی‌پشتوانه، تکیه بر عقلانیت و کرامت انسانی در تصمیم‌گیری‌ها و دفاع قاطع و بی‌پروا به هنگام عمل است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67059" target="_blank">📅 01:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67058">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این نشست در دوحه شاید مهم باشد، شاید هم نه.
خواهیم دید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67058" target="_blank">📅 01:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67057">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15a452960e.mp4?token=BTmFqaeZPtx8C1f4Jf0aT8_dMIcq9ZMU30TFBLfu7Vdp5oLGnGWUVk0yA-7xwhSjSp3AeqsEpnzK7f8FBfOn-f3AuAYmjZ47pZSfU20Ywfa0uKpRSwahoFOBelVI18YZcJxTfBW0XdUpmdQhUUVXK9eF14AVlXjC0sZImqI59iJPiWl_XwuoL_ZWXUKLVz-Up2aFipFTRCLqtfJveRW5125Z9ovB-4xmO50QU70EAaT1RVtkACPHzkS-ebuOWqVpXwS6r8A8-ndCKCEhUc9AVr_vuvnRcBOvQ9K8v5LR2YEjTYZvIRspmFJ_YGI1-kDDHQpM21rkcxBA0RhWkV6Rfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15a452960e.mp4?token=BTmFqaeZPtx8C1f4Jf0aT8_dMIcq9ZMU30TFBLfu7Vdp5oLGnGWUVk0yA-7xwhSjSp3AeqsEpnzK7f8FBfOn-f3AuAYmjZ47pZSfU20Ywfa0uKpRSwahoFOBelVI18YZcJxTfBW0XdUpmdQhUUVXK9eF14AVlXjC0sZImqI59iJPiWl_XwuoL_ZWXUKLVz-Up2aFipFTRCLqtfJveRW5125Z9ovB-4xmO50QU70EAaT1RVtkACPHzkS-ebuOWqVpXwS6r8A8-ndCKCEhUc9AVr_vuvnRcBOvQ9K8v5LR2YEjTYZvIRspmFJ_YGI1-kDDHQpM21rkcxBA0RhWkV6Rfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ درباره کمونیسم:
این سوسیالیسم نیست؛ در واقع کمونیسم است. آن‌ها از واژه “سوسیال دموکرات” استفاده می‌کنند چون خیلی خوش‌آهنگ به نظر می‌رسد، اما در واقع درباره کمونیسم صحبت می‌کنید.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست، شاید از زمان تأسیس آن. این شامل جنگ جهانی اول، جنگ جهانی دوم، حملات ۱۱ سپتامبر و حمله پرل هاربر هم می‌شود.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست. بعضی‌ها وقتی این را می‌گویم می‌خندند، اما افراد آگاه خواهند گفت: “می‌دانید، احتمالاً حق با اوست.”
این در واقع وارد کردن کمونیسم به ایالات متحده آمریکا است. هیچ‌چیز تا این حد خطرناک نبوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67057" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67056">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJ95qMwRfKNJVwnnYDhg7OlpvVboJ8CzhSr-yKj_npJVNHf7Oi_MFsvCkwyKqiHea7qunskBOaz6A0UG7SNN7AH11ezO3zqdoNzKTEv8Kgzyuavhk7V_aVb1OW9fkkQWjwgP41Prn844SxfW3fJhxazHgxxj4QCTT-NjRbAZLk3bha29JbZOXzbPqSvf4cDd_n4B5LWs5QOAgDg7eyrsCiKEQTjw3VI3K062gBn3NoyPlzbTgK7ykimU0PqgVf-R1hh1xAaWjE4EnH5bWWgdaBz7G4WARPPw7Q3VWJlmCHPzJJwLNhMQc-RS4wRwNFvxLseGhSmFr5pK2wtbKpRL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67056" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67055">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=E70sklzQ9CW6U8i_nmec_Pew64Rd4XjEleJW7pdgLq0-2sjy9cWFfRh3sgamWoIKB2AHsy2w_l_6CLUTXtrEPmVRYKOrLmR4FRfGTKIlJl33l6FzQ5y3ICSdYz7QDInK3GSksrJ_nUVQK9TgDSmZ5rMe0tjcxBbCAJX163BlI6cs3OX4Tm4bCM1oIZgDhRqte2MdGNJwENYihqFD1-zdv46tb1w2n7imKybepFPAVECJJb_RMjQ112gxEDWZW_miK_N26mFve2zLaEoCd1TVpFiP0vkaLM4IUxH-U0L39AEle5nSKe8yrOUOw92SQrzcV2MADjGBjLombFS65oBrAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=E70sklzQ9CW6U8i_nmec_Pew64Rd4XjEleJW7pdgLq0-2sjy9cWFfRh3sgamWoIKB2AHsy2w_l_6CLUTXtrEPmVRYKOrLmR4FRfGTKIlJl33l6FzQ5y3ICSdYz7QDInK3GSksrJ_nUVQK9TgDSmZ5rMe0tjcxBbCAJX163BlI6cs3OX4Tm4bCM1oIZgDhRqte2MdGNJwENYihqFD1-zdv46tb1w2n7imKybepFPAVECJJb_RMjQ112gxEDWZW_miK_N26mFve2zLaEoCd1TVpFiP0vkaLM4IUxH-U0L39AEle5nSKe8yrOUOw92SQrzcV2MADjGBjLombFS65oBrAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67055" target="_blank">📅 00:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67054">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1336110317.mp4?token=ustBD-t0wYV-RiOTRNqRagfg8s9bGbw3FxxCLWasntvewixsXCsKqSoDdhkgQL0hE4uSnhfFZQRaHAxwyHXgnQstP_F6s5uEYsoFn8JCN7BRDw7O6dVQe9zmih56G0ycmrI1kh1V2KoSfuTRV67tYMbDBaQsPK6bbIq-DX2jseTezkuLDPWel0QH9TKyYLmZrBNDsckIpqrITLfWqmPsPemMhU_NQ_YtWU6OKPwZLjQcUn7KHU1Hx9SZkLiz8OTYc3PDD-msWCzdk5w40crl8QmQkXW84zAUiDg5dEFU8Rh-Alue5MuaBjTeelM4M024JhfRSii6S_3i9CX_B0y2UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1336110317.mp4?token=ustBD-t0wYV-RiOTRNqRagfg8s9bGbw3FxxCLWasntvewixsXCsKqSoDdhkgQL0hE4uSnhfFZQRaHAxwyHXgnQstP_F6s5uEYsoFn8JCN7BRDw7O6dVQe9zmih56G0ycmrI1kh1V2KoSfuTRV67tYMbDBaQsPK6bbIq-DX2jseTezkuLDPWel0QH9TKyYLmZrBNDsckIpqrITLfWqmPsPemMhU_NQ_YtWU6OKPwZLjQcUn7KHU1Hx9SZkLiz8OTYc3PDD-msWCzdk5w40crl8QmQkXW84zAUiDg5dEFU8Rh-Alue5MuaBjTeelM4M024JhfRSii6S_3i9CX_B0y2UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاه محاکمه ترامپ و نتانیاهو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67054" target="_blank">📅 23:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67053">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e959102c72.mp4?token=dXeSmW92isFs2NsYGnkGu61PNvnL_TpHPj-YaqV7y6VbCDWnyiO-ojJ01tI84g9ygYifpvPYQN6fej2vymCdGFB3D09vcx0iJE5kNHRvepQhH6lKoWI87leGuls01zPwBevf09_e7EaXHG-djbYWhv11LpsPfljSeoZd4-5QvVM4aa2KfFYQtMJvPLLyNtVoE-MjDAOu0l93pGiZ6LgMi9xgqtwI6OWdVXUPPCO7zlCM4Gp_mLq7bfxiNdtnPGAVX14LZegx223tUOmRmAvh-GakvAACms9gIoFIrSsq9MJotebJg78l0EWOQRRWbTx328mCVzuHKYTrf8m4c8XpOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e959102c72.mp4?token=dXeSmW92isFs2NsYGnkGu61PNvnL_TpHPj-YaqV7y6VbCDWnyiO-ojJ01tI84g9ygYifpvPYQN6fej2vymCdGFB3D09vcx0iJE5kNHRvepQhH6lKoWI87leGuls01zPwBevf09_e7EaXHG-djbYWhv11LpsPfljSeoZd4-5QvVM4aa2KfFYQtMJvPLLyNtVoE-MjDAOu0l93pGiZ6LgMi9xgqtwI6OWdVXUPPCO7zlCM4Gp_mLq7bfxiNdtnPGAVX14LZegx223tUOmRmAvh-GakvAACms9gIoFIrSsq9MJotebJg78l0EWOQRRWbTx328mCVzuHKYTrf8m4c8XpOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عزاداری پدر جاوید‌نام داوود عباسی بر سر مزار فرزندش.
جاوید‌نام داوود عباسی یکی دیگر از کشته شدگان اعتراضات ۱۸و۱۹ دی ماه ۱۴۰۴ ایران بود.
داوود عباسی روحت شاد
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67053" target="_blank">📅 23:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67052">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMSD4rQPr8dMi4cT_z-30KcnWN1Rw0lbyKfGAqyz4Mi6vDkEhvdF0OFpnh5aKMmksYczjQ2hvDUXiBczvY1QSneEtJ0jkKjWq2AetJc6B6DJCEunwJx6E-l_5ITJ2K5TZVvsri3r0qCSrjwpScR8E_kcBqxzLLmhzVmaZHs-Z-LMiaNYBkXLvD2Che5uef6DpnozzDbELIY9RB2WS9CxdgAGVMnzK2vIVguAOw_nEJKDCMcjzfgdmNRo5VcSF_ZILmaBGGgLoZ1ylcl63y6JNU-6wWBmZCC84EiCDd5lSG4LuF7C34ApPckOKztuGF-HcvdS-SvqpVgedcOa0STrfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری فارس
:
معاون سیاسی نیروی دریایی سپاه طی سانحه کشته شد
.
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67052" target="_blank">📅 22:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67051">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‼️
اسماعیل بقائی: هیئت کارشناسی ایران برای پیگیری اجرای تفاهمات عازم دوحه می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به وضعیت اجرای بندهای مختلف یادداشت تفاهم از جمله در رابطه با موضوع فروش نفت و دسترسی آزاد به دارائی‌های مسدودشده ایران گفت: در رابطه با تعهد آمریکا طبق بند ۱۰ (فروش نفت) مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم. در رابطه با بند ۱۱ (آزادشدن دارایی‌های مسدودشده ایران) نیز فرآیند اجرایی شدن آن در حال پیگیری است. در این چارچوب، همین هفته هیاتی کارشناسی از جمهوری اسلامی ایران به دوحه اعزام می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به شروع مذاکرات برای توافق نهایی در چارچوب گروه‌های کاری تعیین شده، گفت: هنوز وارد مرحله مذاکره برای توافق نهایی نشده‌ایم؛ طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ و تداوم اجرای آنها است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67051" target="_blank">📅 21:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67050">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‼️
بقائی سخنگوی وزارت خارجه: هیچ‌گونه مذاکره‌ای با طرف آمریکایی طی روزهای آینده در دستور کار نیست
🔴
طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و اینکه نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67050" target="_blank">📅 21:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67049">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=tmhSH0LLzbWqkro0DbD_WB4dG1au6vsBShRyRunQ0uLZyi9wtcOF8zepvZKIaAaj2FvjEo_3N1QnP9IzplJJ1N4B_KXgVCpAAM2HWlPku9nvsPUTXJo2HCCQKKX_QP8sNDM4kER3q3k6z5csFvx6m2Y_zjQLcaao_z7T8Xko_r2HGqVe_jXKetoND_yE6QHoMOfhth8m30So1ZawvmnKtJuG5HgUzn2wI558JUUaIBwFmsbVzOy6tSB61wIrQq6SNWWZ4zg9k2d0CfIpbhZQgMaE1hz1kaeqHDYd1XTfPjb4U4sjMSA58ZM0wcK2dmX-9EswW0olC2YmRPCRUsbSRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=tmhSH0LLzbWqkro0DbD_WB4dG1au6vsBShRyRunQ0uLZyi9wtcOF8zepvZKIaAaj2FvjEo_3N1QnP9IzplJJ1N4B_KXgVCpAAM2HWlPku9nvsPUTXJo2HCCQKKX_QP8sNDM4kER3q3k6z5csFvx6m2Y_zjQLcaao_z7T8Xko_r2HGqVe_jXKetoND_yE6QHoMOfhth8m30So1ZawvmnKtJuG5HgUzn2wI558JUUaIBwFmsbVzOy6tSB61wIrQq6SNWWZ4zg9k2d0CfIpbhZQgMaE1hz1kaeqHDYd1XTfPjb4U4sjMSA58ZM0wcK2dmX-9EswW0olC2YmRPCRUsbSRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناو آبراهام لینکن امریکا توسط سپاه غرق شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67049" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67048">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=dLu2Nwnq9w8qZHtcrDfccQxzogXHiNCD5NDvSixZCGBOZQY5aaHSrfmUbUoP8sNIr-Xhby8sNWI1D_BPTFNsqZV_PAMAKavfwKIC4l2eeRIJ-QJI30Clih0nbSZhh8Odthyo7Wb5pDuwN9NmftS8sjo7PYU5nr9AhQQxns_8ViH1_xFC1Be-YgJGbT1id_Lg4X-nnILwokKRkHyEroIH-_uIaLlffjy8QCKX6ZCIkFUwjQfwOHqwxIGEo2W8TXi8exqnYRef-LTY4VcH8UiA4yqLRzVk3cZz1dKxM21CBxfdWqusyEPVtOTn_U31PrniD9vKRVTo6XN3V6cCO1o-kC08JXKVBR7295IPlimI6EiHtmyXCEMJYKmk5L-G9qUv8Rdehf1K0Jz-JH5-MZ3NtogRFk9x9T5xp6fTgtpzs2lybGwTcL8lauronTqSuUX7OB6vfKGjh30jbBYgj6HKZ2M0Lkvh01asoQFtfvSMy1UkUImh3AY0TXWFiDKr5aEPw0gnyLUlGPnoPwIRUzlG4q2XPEWNLFdSZN-RRaxfjocHECrO0xaZcVlkZjJMeBEFISCJDDxx2uJv3B_f3owT5j5ZRC1kXyxJxuf40hbE6GJWYlYu8lZarIdwvKiffQGOKcT7mdqxjHN1EC7DXs-OthwC7PR_Y4Nhd1LhZuw9TQo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=dLu2Nwnq9w8qZHtcrDfccQxzogXHiNCD5NDvSixZCGBOZQY5aaHSrfmUbUoP8sNIr-Xhby8sNWI1D_BPTFNsqZV_PAMAKavfwKIC4l2eeRIJ-QJI30Clih0nbSZhh8Odthyo7Wb5pDuwN9NmftS8sjo7PYU5nr9AhQQxns_8ViH1_xFC1Be-YgJGbT1id_Lg4X-nnILwokKRkHyEroIH-_uIaLlffjy8QCKX6ZCIkFUwjQfwOHqwxIGEo2W8TXi8exqnYRef-LTY4VcH8UiA4yqLRzVk3cZz1dKxM21CBxfdWqusyEPVtOTn_U31PrniD9vKRVTo6XN3V6cCO1o-kC08JXKVBR7295IPlimI6EiHtmyXCEMJYKmk5L-G9qUv8Rdehf1K0Jz-JH5-MZ3NtogRFk9x9T5xp6fTgtpzs2lybGwTcL8lauronTqSuUX7OB6vfKGjh30jbBYgj6HKZ2M0Lkvh01asoQFtfvSMy1UkUImh3AY0TXWFiDKr5aEPw0gnyLUlGPnoPwIRUzlG4q2XPEWNLFdSZN-RRaxfjocHECrO0xaZcVlkZjJMeBEFISCJDDxx2uJv3B_f3owT5j5ZRC1kXyxJxuf40hbE6GJWYlYu8lZarIdwvKiffQGOKcT7mdqxjHN1EC7DXs-OthwC7PR_Y4Nhd1LhZuw9TQo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی کارشناس برنامه خط انرژی به غیرقابل شکست بودن ناوهای آمریکایی اعتراف میکند:
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67048" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67047">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nypMUrDJYZhUAjkVP_JHhXh3CETDvI-UmmKj01BxRVwbvkfRs8YQAYtgbMQVtEe99VLQSQarBy4iznwFbKAo1Sec7L62GW-A2Vfi7v9FKNMi1iBazpVaAyV9AenaUCGi3Uh1gIYZO6sSpYCmJ8U1r-HDpdl2kBgZamOgFaRrX_0h-zjynv4Q3H08k0mzR9NVhq9bHEv3nq9sr4_V1WmreN7iuub6gC_a56lv0qRXc2YDRq_YMIdEiBhUCStOCzOV_mx1u6Sodouyl8Ee-V74MSHkcIIFyK8dTcJeDToQug-fNJhH8J6sgUdb8x304sRoEh7BPedo4_dwTAgbx3GQIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67047" target="_blank">📅 20:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67046">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
نیویورک پست به نقل از یک مقام آمریکایی:
ما به ایران روشن کردیم که تا زمانی که پیشرفتی در پرونده هسته‌ای حاصل نشود، دارایی‌های مسدود شده این کشور را آزاد نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67046" target="_blank">📅 20:41 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

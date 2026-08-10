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
<img src="https://cdn4.telesco.pe/file/qCCw2ivLNQjEr2x69QSA-70FuMpS3IWDsO2q-oZjq67nf154DKoyK7cjPbI8AmVeQWjuyNqhnDok5rdA6bCrqwnyP-nO4OLxwbDXh9NxkhVTuVq06u_PFi0SN8u03NF2K5QnDYRaBQiwNZzKqJFObwK7K9hzN4F2d2c-VIrmNPsbEgzqlBsEMNCFzVvWFN7_PRj1wWg6gMImj0L0ZZvZdMOwQbpCnowFDrUxaYAF63NPXPtANj_pX_JgailNTX5tXzNH4msWv8v9APW3fv_IDK8h1oUCzg3UM89UZLWSxL1qjg4MyGRqFart62Qw_rUit15ssfcsGCxAmtJMR7BhZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 129K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 23:37:40</div>
<hr>

<div class="tg-post" id="msg-69861">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10abc62a6.mp4?token=mGN4rgbKKvwWfUgr9jG-aBEcW8fkdsgcQMf2ss5IHQa0aQ9buUVWrHfZTahKJLx3fJcPpGuasIB5suPuYRpr_IUzf9P4qAu5qOp6S3rxOgP8h9nKSh7KwEH5QQyW4JkP2ezekV5hApVTr-w9PBJtFoJ03pMwVgNb3fNuf-tsZfzQtP2CXCT-NyBu-O101sTQWTo43y_JnAXFBQ8ZB26EAWUt84YBahojZzj6Tk-pMKd9YKUDmvBWue_ziECnKdhfRxxudOsshxu6urTUR5RUxtfaptbTGvp2RtfqnGIgRQcM68TN_YMm22iYndVqQBSLGdWnoeYRwNYvLSEuqNR8Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10abc62a6.mp4?token=mGN4rgbKKvwWfUgr9jG-aBEcW8fkdsgcQMf2ss5IHQa0aQ9buUVWrHfZTahKJLx3fJcPpGuasIB5suPuYRpr_IUzf9P4qAu5qOp6S3rxOgP8h9nKSh7KwEH5QQyW4JkP2ezekV5hApVTr-w9PBJtFoJ03pMwVgNb3fNuf-tsZfzQtP2CXCT-NyBu-O101sTQWTo43y_JnAXFBQ8ZB26EAWUt84YBahojZzj6Tk-pMKd9YKUDmvBWue_ziECnKdhfRxxudOsshxu6urTUR5RUxtfaptbTGvp2RtfqnGIgRQcM68TN_YMm22iYndVqQBSLGdWnoeYRwNYvLSEuqNR8Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
پس تنگه هرمز کِی باز میشه؟
🇺🇸
ترامپ : بازه!
ما صددرصد کنترل تنگه رو در اختیار داریم.
همون طور که احتمالاً شنيديد، كل تنگه رو مین روبی کردیم. البته شاید هم نشنیده باشید.
اونا میتونن دردسر درست کنن، ولی ورشکسته‌ان؛ پولی ندارن، ایران کاملاً ورشکسته‌ست. حتى حقوق سربازهاشون رو هم نمیدن، نرخ تورمشون 309 درصده.
ایرانی ها صدها هزار نفر رو کشتن، حالا دارن تاوانش رو پس میدن.
اگه قرار باشه خسارتی پرداخت بشه به نظرم ایران باید اون خسارتها رو پرداخت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 306 · <a href="https://t.me/news_hut/69861" target="_blank">📅 23:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69860">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
گزارشگر: شما گفتید که این آخرین فرصت ایران بود. حالا چه؟
🇺🇸
ترامپ: شما متوجه خواهید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/news_hut/69860" target="_blank">📅 23:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69859">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8eb808fce.mp4?token=W4iw4kISa7IIZ07wHeRuOsb6oe8xEz8-AY1pDM2m95gfHYzlRmNaH47Ekq9XTZCkVTh-XvDYFnY0c1cpBh-SuD2-RTeOz2lJ7eSp3ZE4EBoWg_Ln3HLHqB13Y7qvQYid8eM6plvxrbA2qGCEOfWNBeMXkGnrkuAE4oQjEo8Tv5laYH8zKcdSKB5I9aBxptAWiclx9-lHcUYKhum-0j5a3OMhgbPILkEfU64A29DHg14hAg6tO7dvTTetdB1IKU0X6OoyRYz-ZiLflbFV1RytAYV7Z0og60g6UF9htYijU29RCvL3WLSzVUXSSVKBv8BEsHsS3fqti573YIqSB74siA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8eb808fce.mp4?token=W4iw4kISa7IIZ07wHeRuOsb6oe8xEz8-AY1pDM2m95gfHYzlRmNaH47Ekq9XTZCkVTh-XvDYFnY0c1cpBh-SuD2-RTeOz2lJ7eSp3ZE4EBoWg_Ln3HLHqB13Y7qvQYid8eM6plvxrbA2qGCEOfWNBeMXkGnrkuAE4oQjEo8Tv5laYH8zKcdSKB5I9aBxptAWiclx9-lHcUYKhum-0j5a3OMhgbPILkEfU64A29DHg14hAg6tO7dvTTetdB1IKU0X6OoyRYz-ZiLflbFV1RytAYV7Z0og60g6UF9htYijU29RCvL3WLSzVUXSSVKBv8BEsHsS3fqti573YIqSB74siA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
🇮🇷
عظمایی فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی:
«اگر اسرائیل، ایالات متحده، یا هر یک از همدستان آن‌ها حتی جرأت کنند نگاهی خصمانه به جزایر خلیج فارس داشته باشند، با کمک خداوند متعال؛
چشم‌هایشان را کور خواهیم کرد و خلیج فارس را گورستان آن‌ها خواهیم ساخت.
»
@News_Hut</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/news_hut/69859" target="_blank">📅 22:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69858">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15a39d1d6.mp4?token=f1ARFBATH0aq2GHz-bQBdQ__9YkI73HqizHoml-Fe6SCvkNwwUyfvJBdmRZ2PUDE6KGqhe_LJR6h_UlRJoI3hEnEbWTRR9coWuDSx64jdW4rE32hn0js4a-enbZOXbaLjiNtlwSAf2D6_WRzZBODrzeUsiFmVVPm-q_G1LCOkSr3_Ol5Zgs4ALiKnwNuPjguGHAtXp8ui_LtvJ6s5HIi36xy3TV0KnMzecQMe3Emb4KE5cnAkKYfvyQ1qrV0WDa4A6Uz4kTc2t1zMH2A3qWQOcPeHXr9NEK1gIUFdk39b_T-rHFSAmh44PZlCL67_FhPhfmuX6fxcef6uFTJMQqPPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15a39d1d6.mp4?token=f1ARFBATH0aq2GHz-bQBdQ__9YkI73HqizHoml-Fe6SCvkNwwUyfvJBdmRZ2PUDE6KGqhe_LJR6h_UlRJoI3hEnEbWTRR9coWuDSx64jdW4rE32hn0js4a-enbZOXbaLjiNtlwSAf2D6_WRzZBODrzeUsiFmVVPm-q_G1LCOkSr3_Ol5Zgs4ALiKnwNuPjguGHAtXp8ui_LtvJ6s5HIi36xy3TV0KnMzecQMe3Emb4KE5cnAkKYfvyQ1qrV0WDa4A6Uz4kTc2t1zMH2A3qWQOcPeHXr9NEK1gIUFdk39b_T-rHFSAmh44PZlCL67_FhPhfmuX6fxcef6uFTJMQqPPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشگاه مختلط تو قیطریه تهران همراه با استخر جکوزی سالن  ماساژ سالن بیلیارد سالن بولینگ و...
😟
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/69858" target="_blank">📅 22:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69857">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGK9KsCn-BfdCUhqmf0qluLV1nWj0ogpIQRWaOhfq6R47uPBdo3l8QXeNF1fpZSDNZY8pEuxoJRfXERIzelSBm_yuqGKBtagDh6ylKDvqlHYncjg3gOW4wvADun3FvQHGpM-JWRVuQXAKdHYOIyxbP3tdAozQ-fTQkXTrVNwxKE4xaKjzRji0Eg3w0XJYljDYqUZBtyA13wmq7FhkSEvdj5nIbNLHTk0vs7y4OJRJeYtTmu4uH8R8BAITyYfzXNc6_nozzp7650HayCFhxmWWuRZL-JiYcu_sURaiyuBvIFPMypUNwIS2qvrOuhLpLuBJnGVHyP-zZ6yj4kdLUdgKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ درباره ایران:   می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار غرامت بابت خسارات وارده به خود در جریان درگیری نظامی پنج ماه اخیر هستند (درگیری‌ای که آغاز شد چون آن‌ها نباید به سلاح هسته‌ای دست یابند)؛آن هم در حالی که این موضوع هرگز در…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/69857" target="_blank">📅 21:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69856">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79470446aa.mp4?token=Gh1D3Awa34H_3Sh9QspAP4-ayqgXbk00ZwwUE2JlBRUMoQYtJhxeQaujaYO0tmK-kHUpK9at7UkbTOplFnpxonCm2grViA5QD6DnZ2ZjfdPyVEF6__RKaCg9jLHTp7QOJcrRMzOtEyTuzBelCJjOdRnoQHoDrpo5HzcxnhPoDBfW0m99zwMlKzf2pGk6IBhupMdehPTSowJPE5s7ySNXJOpHQ3e-ehzW-GKA3PkOetKIEXTfZzhvJBH40-jyqUPX3-jSx8eFiE01tvhGrpm1Yn7GKPsRPyW0gcG5pzRZYCf59ALUt0HnrZ-IAFdACFqIuccpfJvYttrEPp_CsJOW3WjNPSgiUKMOkBzAcv_YbOeP93xG_8zZUYGxYWCLHTBv6Tm_8F-HKBcjcHTtZ06wpdWUSqOTzlrEMcsf1OJUWK4WpqwnS0nNDxoWFMMINaphi3ZD5sbPvVRrLzRWYzp9XRlP92ILVtHWftGFBoZAbfJH0uuTICqgQmrO1Asnz34xoK9dFoYWzer0tIfaKdNZEZFTUywZbJShg4PvkswV1FRcawunILMJvc4WdMeWqGgeRmDjWJ28SLHU-nQBe1haDg0ooldnhO1QV8kIEpK4HAgcNrYO6ccZGfXb084RClA8r4gc0ekEkWcMPsg80wrzwleQJTjEsB1GJ7dU6hROskw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79470446aa.mp4?token=Gh1D3Awa34H_3Sh9QspAP4-ayqgXbk00ZwwUE2JlBRUMoQYtJhxeQaujaYO0tmK-kHUpK9at7UkbTOplFnpxonCm2grViA5QD6DnZ2ZjfdPyVEF6__RKaCg9jLHTp7QOJcrRMzOtEyTuzBelCJjOdRnoQHoDrpo5HzcxnhPoDBfW0m99zwMlKzf2pGk6IBhupMdehPTSowJPE5s7ySNXJOpHQ3e-ehzW-GKA3PkOetKIEXTfZzhvJBH40-jyqUPX3-jSx8eFiE01tvhGrpm1Yn7GKPsRPyW0gcG5pzRZYCf59ALUt0HnrZ-IAFdACFqIuccpfJvYttrEPp_CsJOW3WjNPSgiUKMOkBzAcv_YbOeP93xG_8zZUYGxYWCLHTBv6Tm_8F-HKBcjcHTtZ06wpdWUSqOTzlrEMcsf1OJUWK4WpqwnS0nNDxoWFMMINaphi3ZD5sbPvVRrLzRWYzp9XRlP92ILVtHWftGFBoZAbfJH0uuTICqgQmrO1Asnz34xoK9dFoYWzer0tIfaKdNZEZFTUywZbJShg4PvkswV1FRcawunILMJvc4WdMeWqGgeRmDjWJ28SLHU-nQBe1haDg0ooldnhO1QV8kIEpK4HAgcNrYO6ccZGfXb084RClA8r4gc0ekEkWcMPsg80wrzwleQJTjEsB1GJ7dU6hROskw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله تند مجری صداوسیما به علی دایی:
وقتی جرائت نداری جیگر نداری به دختر اونور آبت چیزی بگی پس اینجا هم خفه شو لال شو
یه گروهی گول میخورن میریزن کف خیابون بعد از این دایی و خاله ها زیاده هشتگ نه به اعدام میزنن
یکی از این آقایون مشهور دخترش مورد دزدی قرار گرفته بود کم مونده بود دزد رو بکشن بعد همینا هشتگ نه به اعدام میزنن
بعد این وحشیا این بیشرفا جوان مردم رو به شهادت میرسونن یه عده یاد حقوق بشر میوفتن
اعدام نفرت نمیاره شماها نفرت انگیزید شماها ترحم انگیزید
ولی یه پلیس یه گلوله شلیک بکنه داد میزنن عای دیکتاتوریه عای خاک خون کشیدن
شماهایی که لال هستید همیشه لال بمونید حتی اون ور آب
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/69856" target="_blank">📅 20:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69855">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hl-F6NuwjnOYYmurdaMSQ9-VgLhhwCjIZV9RvaRLnHu-Ye8NeQkiYuRihtmBh7BIP-C-VUhQSDodgH6biYfHmyHJUOv-WX4uIAb5HazPxHf5-7s_bSnG4uSnU8fYzdsdvAdtnkWO17VYcZ2r5R36360x7e_90fyFlgyowOJ23el9mpPCBP-Gp4MuFL_TkVw84MPKbimE-_VSqs-mlZhqhkeYG5E_YoEYU-BcuTgwmtOsJ72EMt9eCwBZih7g-g9N2AJD-Vu5y_nZrAzK20TCF7KdzHpA8QeXy8DOBlD2DINkgnqKVAqloLCj4xH_UeX5aLUJcESR4UU7PEERiKE4Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ درباره ایران:
می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار غرامت بابت خسارات وارده به خود در جریان درگیری نظامی پنج ماه اخیر هستند (درگیری‌ای که آغاز شد چون آن‌ها نباید به سلاح هسته‌ای دست یابند)؛آن هم در حالی که این موضوع هرگز در هیچ‌یک از مذاکرات یا دیدارهای ما مطرح نشده بود!
اما این ایده جالبی است، چرا که من نیز اکنون متقابلاً از ایران درخواست غرامت می‌کنم؛ غرامت بابت تمام کسانی که آن‌ها با بمب‌های کنار جاده‌ای و در درگیری‌های متعدد — که به آن شهرت دارند و در ابتدا تحت هدایت ژنرال سلیمانی انجام می‌شد — به قتل رسانده یا به‌شدت مجروح کرده‌اند؛
از جمله خانواده‌های کشته‌شدگان حادثه ناو «یو‌اس‌اس کول» (USS Cole) و هزاران نفر دیگر که در میدان نبرد جان باخته‌اند. به‌علاوه، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران طی ۵۰ سال گذشته به قتل رسانده نیز غرامت پرداخت شود، چه رسد به آن ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
من به نمایندگان خود دستور داده‌ام که این موضوع را قاطعانه در تمامی مذاکرات آتی بگنجانند.
از توجه شما به این مسئله سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/69855" target="_blank">📅 20:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69854">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0at-EzimZbGx0ZkMra_Dk_TMcPXn3qqwbUjGtWsCPla95xe1iFbd40o-S_bMVir4JPUAnlg2ZpyDw3Ifoz9cMP3bNBbQLqfE1TfGMuHSsQX7_lbNwX9WMy8idjMCgtYVQqcqy7FHHJkffjhkUT9mR8gJw908IXCGxdiHH-kx8sWIQJ8uo_vpLvuNM6uhBldqLko5PcoEXVZcg640WkKe0MpnALyfVUYHckD0e4f53hIPlHvBtmNbjEK9Gg1whlu8efThAAz-RddywNyuXde1k904JOGAgCIUlBnEN_33b2GZ8Zz9t1oCzisJ-TF1SLPMCvvoU-u6CKbjh3ZUsMUuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
مرندی:
‏ایران آگاه است که نیروهای رژیم ترامپ در کویت، امارات متحده عربی، قطر، عربستان سعودی، بحرین و اردن در حال بسیج برای یک حمله برق‌آسای بالقوه - احتمالاً در کنار نیروهای اسرائیلی - علیه مردم ایران هستند. جمهوری اسلامی با پاسخی سریع و کوبنده آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/69854" target="_blank">📅 19:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69853">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🔴
🇮🇷
لیست فرماندهان جدیدی که مجتبی خامنه‌ای انتخاب کرد:
سرلشکر  علی عبداللهی به عنوان رئیس ستاد کل نیروهای مسلح
امیر کیومرث حیدری به عنوان جانشین رئیس ستاد کل نیروهای مسلح
سرلشکر احمد وحیدی به عنوان فرمانده سپاه
سرلشکر مصطفی ایزدی به عنوان جانشین فرمانده کل سپاه
حجت الاسلام طائب به عنوان رئیس سازمان بسیج مستضعفین
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/69853" target="_blank">📅 19:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69852">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1723f2a3.mp4?token=kq_zQDeBPJCZwbMGh53xLCZKTbUAuw8Iu-mdqqh-DICOEpNiHyllohxdjqCmo0Te5akG3-zNv3SMndQwgU1KmNM_E5DZmHDHKljvjelNLRPHvqCUh4YDhR6B4_0C3fJxrI7R36haKJ9XMYpTfR8LrdLBizhwLLkSsAzv9kcZgsY_vNPg07xb6l1Dx6E8dHYk2Jbo6_OxSDAe-oVnq6s2IMUZ1cmYSVF7DQD_c1n1g0FzDdwJkb4Sk_ePMYEySGxY1SDkf10jVahL4OVk57uEv31nM8d8WLsSD2N-QV7EwAOgEQ6WV1tvw4XSSAqriM4BfcW7jpFNk6eJzACFb9SzBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1723f2a3.mp4?token=kq_zQDeBPJCZwbMGh53xLCZKTbUAuw8Iu-mdqqh-DICOEpNiHyllohxdjqCmo0Te5akG3-zNv3SMndQwgU1KmNM_E5DZmHDHKljvjelNLRPHvqCUh4YDhR6B4_0C3fJxrI7R36haKJ9XMYpTfR8LrdLBizhwLLkSsAzv9kcZgsY_vNPg07xb6l1Dx6E8dHYk2Jbo6_OxSDAe-oVnq6s2IMUZ1cmYSVF7DQD_c1n1g0FzDdwJkb4Sk_ePMYEySGxY1SDkf10jVahL4OVk57uEv31nM8d8WLsSD2N-QV7EwAOgEQ6WV1tvw4XSSAqriM4BfcW7jpFNk6eJzACFb9SzBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇫
طالبان به طور رسمی برده داری جنسی زنان رو قانونی اعلام کرد تا محدودیتی از این لحاظ نداشته باشن!
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/69852" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69851">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69851" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🙄
همه بت باز های حرفه ای دنبال
🔞
شکار این بونوس ها هستن
✅
لیگ های معتبر اروپایی شروع شده بهترین فرصت برای جبران ضرر های جام جهانی
💯</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/69851" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69850">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ma1jFYgjMZ1v0HZhCD6qEZuezlQQ6i5IODLTZ4mV9hiJMfEsB_APTkXC4smrS65DXFAQrmfFl4Qae6HqITi6vFn1UPlsU2yZn5Z8DPg3McaJMNbKw159ZSqYeU95ijmny-keViwMTCcs5P-vuZTJ2XwvBEnpjzcG87rrNXVDx9yhJIbOen0pmd9WZk9x7RcjPLJf_NMpvx_yp2l8hsN-XN-D9EzDzoOupIPnoRT8UiSgcz-ggErKea8G-E0b3pY7EgFzoKsuUGEW4jOCVIqtp4qKPQW8uWJqhnQOYFDQNV3ASs94LA32Xgzo1wDL1NCrnQdtZLBW6pWSAqSYZpLy2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
شروع رسمی لیگ های اروپا
❄️
🆕
بهترین فرصت برای جبران ضرر های جام جهانی با جشنواره رویایی مرداد  ماه
⚠️
هر افزایش شارژ مساوی
2️⃣
1️⃣
🔣
شارژ بیشتر بدون محدودیت
☄️
به همراه
🤩
🤩
🔤
کش بک باخت همه روزه:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g19
@betinjabet</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/69850" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69849">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
⭕️
مجتبی خامنه‌ای تا ساعاتی‌دیگر اسامی فرماندهان جدید نظامی را پس از بیش از ۵ ماه رسما اعلام‌ خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/69849" target="_blank">📅 18:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69848">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a2288e087.mp4?token=F_9-gcadp_eQt6pOLIl1twy5kQPGlokLvXlr5N_OIRum7ktMW7MvQUsVCJ8tk5u9VvTVtDB_-IJUu7yVXfIop-ZSUnisxW1iLV4nsyTcY8JNpSwxC3FWhnLltZ_G5AdGZY6qr_9HLWsYeu9bA9Y4XnK790a7jpHWoGRaQziLtMlWErmBKZMrzMljIlmTpAgRyoe0a2KE2RCpXD_ueFOKG5louD7vtuY57jdC-lTosxSESdoUxmGtyBz519Mr5I1Vj2Ll0rrc_uO73JnCnEec3zPwIiv-BtWcTvNpDJJXhVzoRjjR1S6NixOrgdry0jquifx_zKQYmgTYe-1hHU30gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a2288e087.mp4?token=F_9-gcadp_eQt6pOLIl1twy5kQPGlokLvXlr5N_OIRum7ktMW7MvQUsVCJ8tk5u9VvTVtDB_-IJUu7yVXfIop-ZSUnisxW1iLV4nsyTcY8JNpSwxC3FWhnLltZ_G5AdGZY6qr_9HLWsYeu9bA9Y4XnK790a7jpHWoGRaQziLtMlWErmBKZMrzMljIlmTpAgRyoe0a2KE2RCpXD_ueFOKG5louD7vtuY57jdC-lTosxSESdoUxmGtyBz519Mr5I1Vj2Ll0rrc_uO73JnCnEec3zPwIiv-BtWcTvNpDJJXhVzoRjjR1S6NixOrgdry0jquifx_zKQYmgTYe-1hHU30gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان درباره مجری و کارشناس‌های برنامه به وقت ایران:
این همه علم رو از کجا آوردید؟
چندتا جوون نشستن رو صندلی و درباره اقتصاد، سیاست، جامعه شناسی، کشاورزی و... نظر میدن.
از چهارتا جا یسری اطلاعات ناقص می‌گیرن و بعد درباره‌اش حرف میزنن و نسخه می‌پیچن و جامعه رو منحرف میکنن.
من 18سال تو دانشگاه درس خوندم و استاد تمامم، الان فقط اجازه دارم درباره یه گوشه قلب که تخصصمه نظر بدم نه کلِ قلب، اونوقت اینا...
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/69848" target="_blank">📅 18:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69847">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7c4253089.mp4?token=FAHAj_pAzQuphV85Y2JI4nH6GISaPC0ndzcZbWMJyKVDPCmmD2UOpfpjqG45AOvIRD7GYMlaVCSxYAHcMVYmCXvkEAwL50Gb7uMrJORbiBdC0RjKxjLLc52KLzKaml5JIPv40YS9-rfMB-WZbSwElpfOqknucYDBOeEfxxwBHNr5PuncJYaq3rpNRcL1eZ7nV9m8IjY9HLiWJ1Kof70k3-IOir4ZYJQUBYPchBfwLYr9ERbE-SHDZp2WL4QmUik8jynsbkAf3iSl2LE0xzgnTtfHmD47uSrusB3pJkoTuryyirQqi-pQl9nx7YphJYzUEktMqr4nk8V9Frpiiwfr1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7c4253089.mp4?token=FAHAj_pAzQuphV85Y2JI4nH6GISaPC0ndzcZbWMJyKVDPCmmD2UOpfpjqG45AOvIRD7GYMlaVCSxYAHcMVYmCXvkEAwL50Gb7uMrJORbiBdC0RjKxjLLc52KLzKaml5JIPv40YS9-rfMB-WZbSwElpfOqknucYDBOeEfxxwBHNr5PuncJYaq3rpNRcL1eZ7nV9m8IjY9HLiWJ1Kof70k3-IOir4ZYJQUBYPchBfwLYr9ERbE-SHDZp2WL4QmUik8jynsbkAf3iSl2LE0xzgnTtfHmD47uSrusB3pJkoTuryyirQqi-pQl9nx7YphJYzUEktMqr4nk8V9Frpiiwfr1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی (1392):
اگه آمریکا به ما حمله کنه ما همون هفته اول هزارتا آمریکایی رو اسیر‌ میکنیم و بعد در ازای آزادی هرکدوم چند میلیارد دلار از آمریکا پول میگیریم و اینطوری مشکلات اقتصادیمون هم حل میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/69847" target="_blank">📅 17:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69846">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b47958b9.mp4?token=EOQziuA5jLhDe3I5A0FlQkMPPtNKOw74xOI4xHOwewnIgdDdnUScOmPsSK3Zwp76pImSjCU1CKOAeVK6LefHcR-XqYec-5LA7Hv0jwrSgw_nMq2c1Ak7FzQkFKQcQY8y49W-8aySsejUVEa5qOx18_IeIhtpv4u6wZA82a8XI-qAwdg5-snnNbweqUzPyvLwMym23G29HiD3zgE5svZ2Hmf6d2DqfXyOUzTzdOr-0vhV4sZ1PU9dNbbzptvHX46U78fWbz6Mk5s8f_Oi10M0yCAoCFwPqmFvqgQqOmybazBupeA6NzWgltaa6k_s1QsfX3CFmgYxEet3HaP4c_Bg7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b47958b9.mp4?token=EOQziuA5jLhDe3I5A0FlQkMPPtNKOw74xOI4xHOwewnIgdDdnUScOmPsSK3Zwp76pImSjCU1CKOAeVK6LefHcR-XqYec-5LA7Hv0jwrSgw_nMq2c1Ak7FzQkFKQcQY8y49W-8aySsejUVEa5qOx18_IeIhtpv4u6wZA82a8XI-qAwdg5-snnNbweqUzPyvLwMym23G29HiD3zgE5svZ2Hmf6d2DqfXyOUzTzdOr-0vhV4sZ1PU9dNbbzptvHX46U78fWbz6Mk5s8f_Oi10M0yCAoCFwPqmFvqgQqOmybazBupeA6NzWgltaa6k_s1QsfX3CFmgYxEet3HaP4c_Bg7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی سمه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69846" target="_blank">📅 16:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69845">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=s57URb1aBqwXwPUYm2rZTApk_64Th7bmjOpmRGKiidsJPSssrwJ305IuPp8c0hF6Uk521nZ3QbKb2sWYVyfkslz8QF7PZSeRjsn-ZO_OboPETAcQ9zaevIbW_I5M0Ayk73daTZsnkuni6JPH9KzeAaOq6d8KRMclW1voDFhms0vQMwkixXiktM3q7dwhrNRhPwQAuM2FrK3XiVZJCUhfAnPavWty8viYXfDwZ9f9ui2cjIryXNYvsVmzMfcW61f999QXXdH0mtTkSRvVxog1w80hWrIIkvUfzkAuYwrLAPOTRCZF43JFC8p0J5HIHNDZOLAcJ981crWtkoUTEA_5oqY6CcM3ahCuhbQTB_jOLwLqiFCnRY7cLZLItlBjCfE6C1YH4sDuJPOEw62LXhj82Mtw45LrOalR1LbYqmCwLDs4C5adBh_iS3nv_4B-KQ4A7J50ABar8iIR44dUQFKjiS94sYHiSgmo6vK_vujR8-5I48fPpY5d2D9N4KufO3V0Lg6HpHArvGAoiixbw6wRsrizLOHqY5xX9AyvxpgUlNOqP3tI0Jq_-yJMRlVNxshYkXFvN2GCEo69LGI5NARJoUxYoUGfri6JkpJhNhoBZeoM_ZN_2gecCgPHTfzjO5jvCsPy8p4N5EePRj_rLhwK3uvpRtKcbchtrOkEFjyYJnE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=s57URb1aBqwXwPUYm2rZTApk_64Th7bmjOpmRGKiidsJPSssrwJ305IuPp8c0hF6Uk521nZ3QbKb2sWYVyfkslz8QF7PZSeRjsn-ZO_OboPETAcQ9zaevIbW_I5M0Ayk73daTZsnkuni6JPH9KzeAaOq6d8KRMclW1voDFhms0vQMwkixXiktM3q7dwhrNRhPwQAuM2FrK3XiVZJCUhfAnPavWty8viYXfDwZ9f9ui2cjIryXNYvsVmzMfcW61f999QXXdH0mtTkSRvVxog1w80hWrIIkvUfzkAuYwrLAPOTRCZF43JFC8p0J5HIHNDZOLAcJ981crWtkoUTEA_5oqY6CcM3ahCuhbQTB_jOLwLqiFCnRY7cLZLItlBjCfE6C1YH4sDuJPOEw62LXhj82Mtw45LrOalR1LbYqmCwLDs4C5adBh_iS3nv_4B-KQ4A7J50ABar8iIR44dUQFKjiS94sYHiSgmo6vK_vujR8-5I48fPpY5d2D9N4KufO3V0Lg6HpHArvGAoiixbw6wRsrizLOHqY5xX9AyvxpgUlNOqP3tI0Jq_-yJMRlVNxshYkXFvN2GCEo69LGI5NARJoUxYoUGfri6JkpJhNhoBZeoM_ZN_2gecCgPHTfzjO5jvCsPy8p4N5EePRj_rLhwK3uvpRtKcbchtrOkEFjyYJnE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بقایی سخنگوی وزارت خارجه:
تنگه هرمز از زمان حضرت آدم تا ۹ اسفند برای همه باز بود
ادعای ساخت سلاح هسته‌ای ایران توسط نتانیاهو دروغی بیش نیست
به ترامپ بگم که ایرانیان شطرنج بازان حرفه‌ای در طول تاریخ بودن( ترامپ جنگ ایران رو به شطرنج تشبیه کرده بود)
هیچگونه مذاکره مستقیم با آمریکا نداریم
باز شدن تنگه هرمز منوط به لغو محاصره دریایی هستش
نگرانی بابت پیمان دفاعی مکه نداریم چون همسایگان ما هستن
بحث کنوانسیون دریای خزر به مجلس ختم شد و تصمیم نهایی با اونا هستش
درباره عمان نزدیک به یک تفاهم هستیم و به زودی نهایی میشه
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/69845" target="_blank">📅 16:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69844">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c431777b9a.mp4?token=lFbxv2Md6v3yaFgVJyHFvtNfM7JzIf8-0mtSPruxFmqC-hOw541rvuvtLqK9t6LulchR96PUcOEdntzdD-Cjb20f4K2Q74_2Gm-5ItTlvseQxrTLfNAo7xVGxNAkfBalVBJpFJ3eYSnOE8ZqHI0IXMxHNYrBtVZo2786mz9Ic2zZqpoMZy4kEPHBhjTvkQaUK7O9ZgyWPSaB6o_dfybG1anhUGPW5adLWdQFnbpTzuSxns3T89rWbjPmKdmSdM81KjCRf5RXzlcNfD2SSoYPYyXbrYnLS8qwS3FFi1-EDee55pprzPSlV-2RSW6eOjSi4RAaieqkg_qVkMAPE72esTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c431777b9a.mp4?token=lFbxv2Md6v3yaFgVJyHFvtNfM7JzIf8-0mtSPruxFmqC-hOw541rvuvtLqK9t6LulchR96PUcOEdntzdD-Cjb20f4K2Q74_2Gm-5ItTlvseQxrTLfNAo7xVGxNAkfBalVBJpFJ3eYSnOE8ZqHI0IXMxHNYrBtVZo2786mz9Ic2zZqpoMZy4kEPHBhjTvkQaUK7O9ZgyWPSaB6o_dfybG1anhUGPW5adLWdQFnbpTzuSxns3T89rWbjPmKdmSdM81KjCRf5RXzlcNfD2SSoYPYyXbrYnLS8qwS3FFi1-EDee55pprzPSlV-2RSW6eOjSi4RAaieqkg_qVkMAPE72esTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
پزشکیان:
با رهبر هفت ساعت دیدار داشتم و درباره مسائل مهم کشور باهم گفتگو کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/69844" target="_blank">📅 15:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69841">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sp5vCKw8H7zaRQcdWpma8dZ7yX9RCtwqRdMPswOfClLm9-dQcANTg8qc6YAkxP_f0NB8lLyXcbyahCtjxgDKYRLfDo_lI4LglvQ1SrwSJW-fMt9UTUsvF5Vc0TZOTxk1_fI_3yZnQE3ZZU9BLJEEvvtf5LxJ6a1fq5AAiGL7IFe1DYW6dXuqUIu4IflHeZVhywcaFbqf6_lY8vTcR1VAfZtrpt_q1yAdvgDQ-NTMVed-3D7XAvwEJezRC05-tJNQmVaMLSHyFs8BS4i6QcvaqQttL4nlsSd6VutRH-jBKrFouwZekXV8H96vevQqE06VxpDOi4Qrn5Mf2_74WRjKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hkp4VEIBKoteS2SnEHcbYBSSejS3XPo2YWFEgHopIuHC0epyDgxmfAlFU4bqIKWMudW7SI3De3i9dUfhRzrV_qqf1CO5X4nz7h13PvOH0Cu5ih4kK3WCwkSpF8LBgKwCxRg4QshHwyxGMszfB0VR7CjLRD4sP3OXCNPFbLM9hJvF6qSY_FPh0DamO9HuHZTasp4LZxq4Nl2qZbdk-Hkq_d1V5k0wGnNG-5JmYWV49rMLcgGvOzC5YqLNrm-PPd4p-8Fw6RRAAWLmV-Aed1qKisvaLSmK1H0wSLU52Kcqk96cxbe_wu2Mq8uC28UhT4fg9NGHtUrpvZr-y4CXo-yN_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92217bf769.mp4?token=lPmjfzlEJk1wnpcVB_VyABIPm_4d2ZYWVoTNvbY3BbibzuuRo_1xCHzX2KYhbTQPxDNjeLQocI7QlKISQh1W5Sh5OQUnWC9Y_urGPFvggpAtYdOf07VHk0rI9oNklLj3c-avDLKxgzJyR6THKx6gu4fiLqOqFn4sxszcl-Eig7TtyhROoFvubtzjQJCM-avdDzBfhJ48o-G8mB4Ijiw5666A6T0OVAttjlvrYJh7lOb_qOydZR244rKPEj012j-ZFPpQCFI3FT9hpVm0i0GjKegjj1lbzZcAEFfhE4U3SZZ8OdwK8LgP5gb-Ombi_tMSkaF6WKmEiW0bgUJD_n9MHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92217bf769.mp4?token=lPmjfzlEJk1wnpcVB_VyABIPm_4d2ZYWVoTNvbY3BbibzuuRo_1xCHzX2KYhbTQPxDNjeLQocI7QlKISQh1W5Sh5OQUnWC9Y_urGPFvggpAtYdOf07VHk0rI9oNklLj3c-avDLKxgzJyR6THKx6gu4fiLqOqFn4sxszcl-Eig7TtyhROoFvubtzjQJCM-avdDzBfhJ48o-G8mB4Ijiw5666A6T0OVAttjlvrYJh7lOb_qOydZR244rKPEj012j-ZFPpQCFI3FT9hpVm0i0GjKegjj1lbzZcAEFfhE4U3SZZ8OdwK8LgP5gb-Ombi_tMSkaF6WKmEiW0bgUJD_n9MHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
دیروز عراقچی برای مهمانان خارجی تو ساختمون وزارت خارجه بساط تعزیه راه انداخت
😳
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69841" target="_blank">📅 15:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69840">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7709b161ed.mp4?token=noiWKi9YoYtr7rq_edEOUwYBdxqSAIRm-2Z3irqTZl-x5_QFfmysv5ShBCpjH0RqctKclqYBw-HP0vWEZTtzpSVxk4zNJMgcwKWe5b5gc-ybS8OVrnWKqhJV4TcoJ5MC-YYjgTXVjdRoh2Ol5H6WRgF5QH0oem0kzBD82jr4reZQhcQ-ApralO3UQ8QY7ho7rjrSvfb9cHBlorD4mtdxtDAxIcDTrbzbKup0oGIWH4mxtmpgM9WqotnHLgkHvhBTW1l6kJbyJAd4hniVe9ic9LgG1pe5IxucJO0PFBIp8pX1SocEcDJheQpHiSQoubHLnaJpi87IiKw4ffBa9c85Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7709b161ed.mp4?token=noiWKi9YoYtr7rq_edEOUwYBdxqSAIRm-2Z3irqTZl-x5_QFfmysv5ShBCpjH0RqctKclqYBw-HP0vWEZTtzpSVxk4zNJMgcwKWe5b5gc-ybS8OVrnWKqhJV4TcoJ5MC-YYjgTXVjdRoh2Ol5H6WRgF5QH0oem0kzBD82jr4reZQhcQ-ApralO3UQ8QY7ho7rjrSvfb9cHBlorD4mtdxtDAxIcDTrbzbKup0oGIWH4mxtmpgM9WqotnHLgkHvhBTW1l6kJbyJAd4hniVe9ic9LgG1pe5IxucJO0PFBIp8pX1SocEcDJheQpHiSQoubHLnaJpi87IiKw4ffBa9c85Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وایرال شده از قیمت یک پک آرایشی که ناقابل سه میلیارد
😳
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/69840" target="_blank">📅 14:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69839">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQJPvJddN_VYXnaRk8vB3A2CqHVKB16ZuUONUsc0J5hq3wqlWPmuQL9kk7y8qUIfdMxt_fgqAWtHz7picK4_kpUCTOqBM0cGeGIHvWb3-Jj8uku1dquNIQyGyRg8jfUdENlLJTIqXmq6NMhYmE_MAgxl8xIQjrkVXKBjAkfCZkcQ31zxSrbKOnDewHyjpszrzvxaUpenX-GUjixkhjw07I9WA3tgWquE_BqHDpEDGgRtfQKmj48uLG2SALjDNUT5sNLtbE_uQk-Xj3PdnpFawyag21zUzwJ_VihaEtEDHjWsWangPqklW4FkmmO_EK8z8h8EjApUdAlINxo9nmn5UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
یک مقام ارشد آمریکایی به من گفت که کاخ سفید از اظهارات نتانیاهو درباره طرح غزه «ناراحت نیست» و آن را بخشی از فضای انتخاباتی اسرائیل می‌داند.
این مقام آمریکایی گفت: «ما نیازهای سیاسی "بی‌بی" را درک می‌کنیم. تا زمانی که او به انجام آنچه ما می‌خواهیم ادامه دهد - به‌ویژه در خصوص مهار حملات به غزه - مشکلی با این موضوع نداریم.»
به گفته یک مقام آمریکایی، نتانیاهو هفته گذشته در تماسی تلفنی با جرد کوشنر، فرستاده رئیس‌جمهور ترامپ، وعده داد که علی‌رغم تردیدهایش، به این طرح ۱۵ ماده‌ای فرصت دهد و حملات به غزه را محدود کند تا روند خلع‌سلاح این منطقه بتواند آغاز شود.
از آن زمان تاکنون، اسرائیل حملاتی علیه غزه انجام نداده و ارتش اسرائیل (IDF) به‌تدریج در حال عقب‌نشینی به سمت «خط زرد» است. هم‌زمان، آمریکا و میانجی‌گران خواستار آن هستند که حماس روند خلع‌سلاح را آغاز کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69839" target="_blank">📅 14:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69837">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d242d991d.mp4?token=rPAkqv-3x05ZThgtJvl2TYoAHLsCew5xlsipPPExJIV7EWU6FKSJJ90Z7yazBHnRppbEtK6dO-GXQwUdAKryHY02-7Hx4zuBAFgbyzvlNS0Xvy8NFW5mG2M_wkq_GqHL0y4UZfI6fjGKjz5iphDr2YDGqSrLEFDeHWaTKVgjcPf82dpFz6VPZrUA2rPh_ubrFQR75N3ytFYNNakuD51CCzEQME8C0yn1tr-PxOm77NM_OZXC70lcwN5aCQGKcSxSYU3WOCZOsJBIqg_ucSvpTOvPt78Sd04evlXeircccqSU-ZJbTkjddul5XVRYbp29s8KqRPGYpq-sZZJnAfSPKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d242d991d.mp4?token=rPAkqv-3x05ZThgtJvl2TYoAHLsCew5xlsipPPExJIV7EWU6FKSJJ90Z7yazBHnRppbEtK6dO-GXQwUdAKryHY02-7Hx4zuBAFgbyzvlNS0Xvy8NFW5mG2M_wkq_GqHL0y4UZfI6fjGKjz5iphDr2YDGqSrLEFDeHWaTKVgjcPf82dpFz6VPZrUA2rPh_ubrFQR75N3ytFYNNakuD51CCzEQME8C0yn1tr-PxOm77NM_OZXC70lcwN5aCQGKcSxSYU3WOCZOsJBIqg_ucSvpTOvPt78Sd04evlXeircccqSU-ZJbTkjddul5XVRYbp29s8KqRPGYpq-sZZJnAfSPKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فوران یک آتشفشان قدرتمند در جنوب غربی کلمبیا
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69837" target="_blank">📅 13:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69836">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81027c9c4b.mp4?token=lhBJlbcPB2lK_AdRMc2OKw6gcjHzgaJeH44PPA7cuP0CdyZZNBTWLfXY5Wh8Z_UFFmRKiZEvDv3FoNG54Vez_Z-BLKRjC7CBnN6hxD7k7OSFUTqM1b5CixO3BlSivLs3IYtG5TzOniZm3l8_Hqd3WIXakSdVw5EYsdyOvJOUPvi-xiiikJcj4ZpdMzJPSyWz7URih0AwUYMhkY_CXkqnfbM7EE52qn8bRJEEsCnqbmoVCq0G371aZXfjpWb-em6caqRqIdCDhdclJgSqrjSTfvAug97tY3yumKodIoc5JKQt9-R08a81M4jcy0gLOmJB67BYU806VYfCSYSIi06xIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81027c9c4b.mp4?token=lhBJlbcPB2lK_AdRMc2OKw6gcjHzgaJeH44PPA7cuP0CdyZZNBTWLfXY5Wh8Z_UFFmRKiZEvDv3FoNG54Vez_Z-BLKRjC7CBnN6hxD7k7OSFUTqM1b5CixO3BlSivLs3IYtG5TzOniZm3l8_Hqd3WIXakSdVw5EYsdyOvJOUPvi-xiiikJcj4ZpdMzJPSyWz7URih0AwUYMhkY_CXkqnfbM7EE52qn8bRJEEsCnqbmoVCq0G371aZXfjpWb-em6caqRqIdCDhdclJgSqrjSTfvAug97tY3yumKodIoc5JKQt9-R08a81M4jcy0gLOmJB67BYU806VYfCSYSIi06xIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشتیبانی سنگین و فوق العاده از نیروهای زمینی آمریکا در جنگ افغانستان ( طالبان ) توسط بالگرد آپاچی ۶۴ با توپ ۳۰ میلی متری M230 Chain Gun
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69836" target="_blank">📅 12:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69835">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ea33d827b.mp4?token=QQmIszP4ZkbNfK9mdXODMiMxYbgJZtgx98UvVYiGEX0jbidFKJIbN1ci4aADHxcmql7b6M42KPxZjqx-16O-a3aKxgtlolcwkzlyrvE-fhFO5WveAcnO4dNwPqarR4NDUenAt7-ByagJ6_Y-nMAGmjnV8oOz5J22ADHQwQWXP4wHH1gzi_dJn0ortzDNNNJ53fINPtQWnUiyqI4a6npNZ7RoiBO8mB0NoSAqwK3NpUEzU2wp2xHEvMLF11diBphXKSpSUeeZub_dNbkJV4A7ppvJcpO-j-W20SNsbK6C6Wnwb6Lq2SjGYPEwY-ytE-PWzLTex1hzP182ZCq0KANAKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ea33d827b.mp4?token=QQmIszP4ZkbNfK9mdXODMiMxYbgJZtgx98UvVYiGEX0jbidFKJIbN1ci4aADHxcmql7b6M42KPxZjqx-16O-a3aKxgtlolcwkzlyrvE-fhFO5WveAcnO4dNwPqarR4NDUenAt7-ByagJ6_Y-nMAGmjnV8oOz5J22ADHQwQWXP4wHH1gzi_dJn0ortzDNNNJ53fINPtQWnUiyqI4a6npNZ7RoiBO8mB0NoSAqwK3NpUEzU2wp2xHEvMLF11diBphXKSpSUeeZub_dNbkJV4A7ppvJcpO-j-W20SNsbK6C6Wnwb6Lq2SjGYPEwY-ytE-PWzLTex1hzP182ZCq0KANAKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پرستار از اتفاق عجیب شب زفاف یه زوج میگه:
ساعت ۴ صبح یه خانم با خون‌ریزی شدید به اورژانس منتقل شد و اول فکر کردیم
سقط جنین
اتفاق افتاده، اما بعد مشخص شد مربوط به
شب زفاف
بوده.
خون‌ریزی اون‌قدر شدید بوده که مجبور شدن بیمار رو
جراحی
کنن.
⏺
پرستار توصیه کرده زوج‌ها برای اولین رابطه عجله نکنن و با آرامش و احتیاط پیش برن تا به این روز نیافتن
.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69835" target="_blank">📅 11:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69834">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53aa49426e.mp4?token=En1Z16W3ceQw1DrnI_5XYBZg52qkJgoqUWqOpwsKdVYXTRSDwvtrYQjIjBNGpAoLumBFVk5RrxazBfGEi_w9ObtIQm1gX8bOE-hhc8vFBn0znyEKqL6UXl6gk1VH8gJa7Wtb2uvzYM2iYe2McpkLsPn_3plAhwYWGVMxSvFmw8mt-XEyyafzoCXuN5-WfHf0EM-GO5u-ZQ-13iVhbRlzoAHDZJWIK9JIhXAgX93qLL0fpJt5aXIH7UaTB7wfec0tjtFeDcUVYvAm0GpCSASVQyZGj9vCQtFCKka0r0OIZliYmH38sVOm-WDEOwkbfU0nHym7ASFDnUvwpdEL8V9dWTaR5otlsSZqIqAVW3pkbJoWCvXjVvaVEY1QLIorpwURr56PJY9J0i9HKoAQpHkM4zEZP5PK9uUTiFGG9jT_voiVj42KEwmO_tX3FpPlQT0tMDUswZXMOAN-iib0ye8SBjMkYm2tvxyz53B9mDpXXwa2t-k8dZRdEVMkTGQRVVx3K_2cNVyFEbZhqPlaAsr22__EcWKpmyj61iyaiP3cDYQ41ADgZbtmZ0N__IWAZvXcOzbYAVf-NQ3hXA-SyfC4P6PKq44WxWkPPVJj-JoADfMcLeqWqA4qgIAfDhOWCN-e3HdiO4xe2SJhzP4q7fyo4Wj_ue11kKdAZSDgzSNc_HM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53aa49426e.mp4?token=En1Z16W3ceQw1DrnI_5XYBZg52qkJgoqUWqOpwsKdVYXTRSDwvtrYQjIjBNGpAoLumBFVk5RrxazBfGEi_w9ObtIQm1gX8bOE-hhc8vFBn0znyEKqL6UXl6gk1VH8gJa7Wtb2uvzYM2iYe2McpkLsPn_3plAhwYWGVMxSvFmw8mt-XEyyafzoCXuN5-WfHf0EM-GO5u-ZQ-13iVhbRlzoAHDZJWIK9JIhXAgX93qLL0fpJt5aXIH7UaTB7wfec0tjtFeDcUVYvAm0GpCSASVQyZGj9vCQtFCKka0r0OIZliYmH38sVOm-WDEOwkbfU0nHym7ASFDnUvwpdEL8V9dWTaR5otlsSZqIqAVW3pkbJoWCvXjVvaVEY1QLIorpwURr56PJY9J0i9HKoAQpHkM4zEZP5PK9uUTiFGG9jT_voiVj42KEwmO_tX3FpPlQT0tMDUswZXMOAN-iib0ye8SBjMkYm2tvxyz53B9mDpXXwa2t-k8dZRdEVMkTGQRVVx3K_2cNVyFEbZhqPlaAsr22__EcWKpmyj61iyaiP3cDYQ41ADgZbtmZ0N__IWAZvXcOzbYAVf-NQ3hXA-SyfC4P6PKq44WxWkPPVJj-JoADfMcLeqWqA4qgIAfDhOWCN-e3HdiO4xe2SJhzP4q7fyo4Wj_ue11kKdAZSDgzSNc_HM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایشون هم اینطوری انتقام قتل حمیدرضا رجب‌زاده رو گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69834" target="_blank">📅 11:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69833">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=gMNSLpPY5lZzOYBt8Tmes5GaczRNVGQfCsEjvuiv2pWALv0_Ph4KAgmkUO50kWF0ZKGG5uHIZdNNXJB9rROrvSU8nvZVhoujOi1Q1-KcIU0dz3pGBmTDPq5ngS3jACEuLSmlXNNq_X95SXm9RScBWyZiELRZNjKkq-Fvb5BM6AhAmrEx8jfBesRsHeVsME9NzNMK7n9t_CTcLPCHQC49xPIUUD80gpyAgB_k8Awsj2wcVE1pOr4qj0xEPBYK7_1NvMiWlp4N9AfdeLNDf0hFF3gMozm3Xvbbg0t4nACwo5s1fCsOknKr4e7sGm0dEu6uTfKhZ7Cc-L1kfs9nvi2Sfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=gMNSLpPY5lZzOYBt8Tmes5GaczRNVGQfCsEjvuiv2pWALv0_Ph4KAgmkUO50kWF0ZKGG5uHIZdNNXJB9rROrvSU8nvZVhoujOi1Q1-KcIU0dz3pGBmTDPq5ngS3jACEuLSmlXNNq_X95SXm9RScBWyZiELRZNjKkq-Fvb5BM6AhAmrEx8jfBesRsHeVsME9NzNMK7n9t_CTcLPCHQC49xPIUUD80gpyAgB_k8Awsj2wcVE1pOr4qj0xEPBYK7_1NvMiWlp4N9AfdeLNDf0hFF3gMozm3Xvbbg0t4nACwo5s1fCsOknKr4e7sGm0dEu6uTfKhZ7Cc-L1kfs9nvi2Sfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دریک، از بزرگترین خواننده‌های دنیا؛
با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]
وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69833" target="_blank">📅 11:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69831">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d3c25ee1.mp4?token=qobJ3_VzodEnTaIqadhSkC0kdTWExLDyvDscGE5gjyjGZCSiF71XFl689C3vWkXQ4UpspULw-mKrzZnyiAI18LSiCoqAAd7mj60I4i3kInXRk3sjGTtfUlc_LGEKEy6l4K2P0gox5g6cjKhtUf3eySGKwL2RT_0nyK8PeUb8yAD38p733_zcfOWucZ-mMfvuyW2IpAg_PFeM0Q85KG3wxHTqJhDTt2wMAmzP0ir31B1MhRboU4L77TSAhRz0z9fLaLuYKpA3ynnNiwpnlS0wJw0kSV_s_hdp1ew3N6T5Bh1SsqPRXSMEvCb5l7HD7_5lH9ieKSdYKawPzsLPTyVCXURoNYmUDMEo0dwUeYd2axjlQTV_hiYSzBjOABgrLqS6Hz8xIpRyNNod5K_GpNgpP9lDqPkyXR1tVIUJWemqDa8UVilEHWsC3emfzb7Sk_lXu0ETr-moNrxsZjvP3I5ORR6ehrKHSV0jtSWmmtRGjqQ-YtpZNe90wycm5eXhKdSdVa7ChK_bYTXsE0LFwzK8nz5vmzuDAKwOR1iU1k06e5MdU-pKlACEL6eYVStCLbROx3Cxu55DIdShy3b_-MBPPIY0BBCXNSz1y9o5az3D4CzF0YIPTB5454_PWifOW9doE_q5XXZsu3mjY-EE6EGDFmawv0cC0P8FSyXy1i3BGlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d3c25ee1.mp4?token=qobJ3_VzodEnTaIqadhSkC0kdTWExLDyvDscGE5gjyjGZCSiF71XFl689C3vWkXQ4UpspULw-mKrzZnyiAI18LSiCoqAAd7mj60I4i3kInXRk3sjGTtfUlc_LGEKEy6l4K2P0gox5g6cjKhtUf3eySGKwL2RT_0nyK8PeUb8yAD38p733_zcfOWucZ-mMfvuyW2IpAg_PFeM0Q85KG3wxHTqJhDTt2wMAmzP0ir31B1MhRboU4L77TSAhRz0z9fLaLuYKpA3ynnNiwpnlS0wJw0kSV_s_hdp1ew3N6T5Bh1SsqPRXSMEvCb5l7HD7_5lH9ieKSdYKawPzsLPTyVCXURoNYmUDMEo0dwUeYd2axjlQTV_hiYSzBjOABgrLqS6Hz8xIpRyNNod5K_GpNgpP9lDqPkyXR1tVIUJWemqDa8UVilEHWsC3emfzb7Sk_lXu0ETr-moNrxsZjvP3I5ORR6ehrKHSV0jtSWmmtRGjqQ-YtpZNe90wycm5eXhKdSdVa7ChK_bYTXsE0LFwzK8nz5vmzuDAKwOR1iU1k06e5MdU-pKlACEL6eYVStCLbROx3Cxu55DIdShy3b_-MBPPIY0BBCXNSz1y9o5az3D4CzF0YIPTB5454_PWifOW9doE_q5XXZsu3mjY-EE6EGDFmawv0cC0P8FSyXy1i3BGlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی شبانه به مجموعه‌ای از اهداف در سراسر روسیه و سرزمین‌های اشغالی حمله کردند.
پهپادها مرکز خرید گالاکتیکا در ماکی‌یوکا، که قبلاً مرکز منطقه‌ای بود و در سال ۲۰۱۴ توسط نیروهای روسی تصرف شده بود، را به آتش کشیدند.
آنها همچنین پالایشگاه نفت در نیژنکامسک، تاتارستان را هدف قرار دادند، در حالی که روسیه ادعا کرد ۱۵ پهپاد در نزدیکی مسکو سرنگون شده و عملیات فرودگاه را مختل کرده است.
طبق گزارش‌ها، حملات پهپادی باعث قطع گسترده برق در ملیتوپول، بردیانسک و دونتسک شده است، در حالی که انفجارها و آتش‌سوزی‌هایی در سواستوپول و کرچ گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69831" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69830">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69830" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/69830" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69829">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=rwgRWaNaGx4XA7ZfyAOTy0V1jNGwpH4jolTzD4puVq2Kc42eKHwEi-x5eeSlIUqoZ961WDwIWG8KdTwM4NI9E0p7118NzDFlMca0-Su3FZv2d80DNAY92u-vhqpa03Xa33DPMaMOy-KR8Dmf1kenZRDSecSUnjBcwBTuBjWYJSsMgrrfytM369HCpcUdIQ0JfpOHh6QNKeWKgz0iVMPiPa53rXZ3mb5IMEixokJjCZtFOoPOaJK9BPQTimnoKrhoLK0CcVCg6GOV3BHQpJ2YgGKEDWQzm_L0Zp9Sdx9I8ovnudDrpvHMchDeukSUF74o4eFKkiqqN5_QnSXkYu4Aqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=rwgRWaNaGx4XA7ZfyAOTy0V1jNGwpH4jolTzD4puVq2Kc42eKHwEi-x5eeSlIUqoZ961WDwIWG8KdTwM4NI9E0p7118NzDFlMca0-Su3FZv2d80DNAY92u-vhqpa03Xa33DPMaMOy-KR8Dmf1kenZRDSecSUnjBcwBTuBjWYJSsMgrrfytM369HCpcUdIQ0JfpOHh6QNKeWKgz0iVMPiPa53rXZ3mb5IMEixokJjCZtFOoPOaJK9BPQTimnoKrhoLK0CcVCg6GOV3BHQpJ2YgGKEDWQzm_L0Zp9Sdx9I8ovnudDrpvHMchDeukSUF74o4eFKkiqqN5_QnSXkYu4Aqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r19
@betinjabet</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69829" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69827">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILdjXCJjzi6JqlbbrBom6CO98gbMEpxo-MHyh_En9Qv1WHCDo1E5D3e_hTd9wWQH1ZL8riBwlvq0mDtaMFJoCxhIwMI4N7rUhVmOUznEd1H3xkQHcJZiLweUcjpkHFZCxx9RmoLAJoNBUtSjqEEMOsXRribp7YkMOJn_vUCDOEk4eCXqfHiqJAosyIlvyB8pYyeJ31jooNplks_uuQkY7aXeWgOGOt-Ht3SrX_jL2TWLH3Ui6GH46PPp3KdXPw0o1-KzGY7XI-2d0bLNmiAxNBivlmgfNhf3KrMHRsbM-xvMfbnS3a8NXnU8mXep-w6YEPUjXsOKeU27Ewx2M-6v8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
شرکت آمریکایی BlackSea از پرتاب یک پهپاد FPV از روی قایق بدون‌سرنشین GARC خود رونمایی کرد
؛
این شرکت اعلام کرده است که با استفاده از تجربیات به‌دست‌آمده از جنگ، استفاده از پهپادهای FPV هدایت‌شونده با فیبر نوری را پیشنهاد می‌کند.
محفظه‌های پرتاب این سامانه قادر به حمل پهپادهای FPV در اندازه‌های ۵، ۷ و ۱۰ اینچی هستند؛ پهپادهایی که از نمونه‌های FPV مورد استفاده فعلی روسیه و اوکراین کوچک‌ترند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69827" target="_blank">📅 10:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69826">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c36a2172.mp4?token=gbg9WJT6sz1_2aixdFoa4iRrvC3lJOjc8AqYWL_NMPmecZo1UpSl1TXmjRXVxYPqfXmixKG-sMVTtIdIoNRYwBq7a1p0Ua4gpySrTZjeYEiREHw6sPXsd9B1KoZxd5TZCZxDO7Ei-orWNogq4WMjPgXmRvHZeKRwBf4R8yyTfyVwaoNThNk9Upmdl-UgTDdbtXndL3TArNZMl6ldXykD2A2JW8SEgAh3x00nqvqz_FgxSQUBGyhm2w8-g7WKChfnIpbOvXlzwZtVjYGE5cfRlHDNH6HIX3RJkB1BgZaLzDwATofiQEKkPLBHbe9luAv-FsBmyvDmgywXPTncD2VOrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c36a2172.mp4?token=gbg9WJT6sz1_2aixdFoa4iRrvC3lJOjc8AqYWL_NMPmecZo1UpSl1TXmjRXVxYPqfXmixKG-sMVTtIdIoNRYwBq7a1p0Ua4gpySrTZjeYEiREHw6sPXsd9B1KoZxd5TZCZxDO7Ei-orWNogq4WMjPgXmRvHZeKRwBf4R8yyTfyVwaoNThNk9Upmdl-UgTDdbtXndL3TArNZMl6ldXykD2A2JW8SEgAh3x00nqvqz_FgxSQUBGyhm2w8-g7WKChfnIpbOvXlzwZtVjYGE5cfRlHDNH6HIX3RJkB1BgZaLzDwATofiQEKkPLBHbe9luAv-FsBmyvDmgywXPTncD2VOrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جهانگیر، سخنگوی قوه قضائیه:
آخوند خرازی، بابت صحبتاش تحت تعقیب قرار گرفته و به دادگاه ویژه روحانیت احضار شده.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69826" target="_blank">📅 10:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69825">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🟡
📰
مراد ویسی تحلیلگر ارشد اینترنشنال: «جنگ بزرگ در خاورمیانه، برای سرنگونی جمهوری اسلامی است.»
⏺
پرسش این نیست که کدام زودتر می‌رسد؛ پاسخ روشن است:
جمهوری اسلامی سرنگون شود، مردم ایران به یک حکومت عادی می‌رسند.
جمهوری اسلامی سرنگون شود، نیابتی‌ها خشک می‌شوند.
صدام رفت، یک کانون تهدید در خلیج فارس از بین رفت — کانون دوم هنوز باقی است.
خلیج فارس می‌شود منطقه‌ی صلح، ثبات و توسعه؛ چون امارات، قطر و عربستان دنبال توسعه‌اند و ما هم دنبال جبران خرابی‌های جمهوری اسلامی.
ثبات منطقه از تهران آغاز می‌شود، نه از میز مذاکره.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69825" target="_blank">📅 09:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69824">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd241cc6.mp4?token=IDy_MP9sjUkJI2Mu9ve4Ihy1cIiKO8hymb2A9j8IaclwzkEtc_Pr9iceBv6zS4KHvEOUeQFpjTUWwgp7kQzuHLHZgp13Pqm4KeDt7tmSKr7BYNc-dlIUXihBUgeb0yrjeMOPMO5C7ZK8vEh-_-gDSeacwPgMtdGiHiCm9t2ftpUQzdL5Z3WTtLWWEVKiowWdduMtMTw2CdGb8Jmfir_gL9Yktclgr9Gs5KKjaisUNxf9cDEsK4qCmlxQevcDWDDegBd0a2cPyNs0NL3TAfLc7PqvTzNCZgTcvZSXRMT-CZ4td_CQJgcJ7x3Gq-OPYJiyJLMlRszwvjP6q4Cpd2BvVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd241cc6.mp4?token=IDy_MP9sjUkJI2Mu9ve4Ihy1cIiKO8hymb2A9j8IaclwzkEtc_Pr9iceBv6zS4KHvEOUeQFpjTUWwgp7kQzuHLHZgp13Pqm4KeDt7tmSKr7BYNc-dlIUXihBUgeb0yrjeMOPMO5C7ZK8vEh-_-gDSeacwPgMtdGiHiCm9t2ftpUQzdL5Z3WTtLWWEVKiowWdduMtMTw2CdGb8Jmfir_gL9Yktclgr9Gs5KKjaisUNxf9cDEsK4qCmlxQevcDWDDegBd0a2cPyNs0NL3TAfLc7PqvTzNCZgTcvZSXRMT-CZ4td_CQJgcJ7x3Gq-OPYJiyJLMlRszwvjP6q4Cpd2BvVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یکی از نفس‌گیرترین ویدیو های منتشر شده از جنگ؛لحظه بمباران شریعتی تهران!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69824" target="_blank">📅 09:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69823">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69823" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#بازی_پولساز
⚠️
🔥
بلک کارت جدید ترین بازی معروف جهانی هست که فقط کافیه یکمی باهوش باشی تا حریفات رو شکست بدی
👌🏼</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69823" target="_blank">📅 02:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69822">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6c003ee1.mp4?token=X-4qSlha0JrFoPLquYa39K20mwOW97yyB85QAa25Lc4TmjM0gT680SUEL0SC1-DBnBTcl86huza6QWBPaIAaMqYx_FcemPd1spNW9SSKsTNz_cxKHLdx8wGA6KBOjcUjaEOaGZzrM8xezzU29xeKcYPvTnmMwqqzFAp9qFJKtDu95MNT3bAU6dEt1ed23PJ1e2Ai-B94IDbIcUKxwnRQs5LOvOnh5m2itRWBKAZ7zxLEKtQkLxmYl_X7gIyVMq1cjD-l5PHf5vE8MEUDmhmKZp48dv682KHA3Wm6PV_PhB1cabkuOxI7xEXraiMMZNKI3l9Udw00NLS-XS5aUiMA5DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6c003ee1.mp4?token=X-4qSlha0JrFoPLquYa39K20mwOW97yyB85QAa25Lc4TmjM0gT680SUEL0SC1-DBnBTcl86huza6QWBPaIAaMqYx_FcemPd1spNW9SSKsTNz_cxKHLdx8wGA6KBOjcUjaEOaGZzrM8xezzU29xeKcYPvTnmMwqqzFAp9qFJKtDu95MNT3bAU6dEt1ed23PJ1e2Ai-B94IDbIcUKxwnRQs5LOvOnh5m2itRWBKAZ7zxLEKtQkLxmYl_X7gIyVMq1cjD-l5PHf5vE8MEUDmhmKZp48dv682KHA3Wm6PV_PhB1cabkuOxI7xEXraiMMZNKI3l9Udw00NLS-XS5aUiMA5DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😯
اگر هوشت بالاست
🗼
:
❌
👍
این ‌ویدیو‌ آموزشی رو‌ ببین و با ‌استفاده از هوش بالایی که داری پول در بیار.
🟢
بازی خیلی حرفه ای و‌
#پولساز
رو‌ از این ویدیو یاد بگیر
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
a18
@betinjabet</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/69822" target="_blank">📅 02:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69821">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:  اگه ایران از این به بعد به هر کشتی‌ ای توی تنگه هرمز شلیک کنه، فرقی هم نداره با موشک، پهپاد، راکت یا هر سلاح دیگه‌ای باشه، آمریکا در جوابش یه پل یا نیروگاه برق ایران رو میزنه حتی اگه نزدیک تهران یا داخل خود تهران باشه.  @News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69821" target="_blank">📅 01:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69819">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAalZDk8Wivp1rb54E8kcJ5VThVJ22LOTeEUOU6S6b3hnxtsvmSn_B3-2ZTka-p_FWhjDAN2Kzgdy1T-2gmjvj_nM-MD1RZ3prV_JkuDQ2LpIU7g5QK648_O1TWbn4QeQeJuKXPEqgTnd19gsyKdoDHyp8zPWZyVZ_c1VI9BKpCEfSWslM2OmHvurPdkyKBtkhcqGSbWr3OzXfTHv6LAYhX9NXR46g7266VYxYsGQ6K10fkyaey8Pv5gGYmR1K7_obWoK70-xuzLr9jdJdHeHcVxQHXwVK-cfHGRS-E0b_Aw2oG4y7Mg1v-zlKrM5QARaQ5LjU3XMdDMs8ynS0J65A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94eb35c039.mp4?token=mW-Ug_57wgUgDXLmyxDw5O-XYxVhA7S-igS2Uw8G5blNg6qF1slO0nlysQkLM1dBIBED87BiUSMu4HpQDaK93Ht1ITqiREbpCcbcWciFlpdVdpjM6Tvq6mf9bsllZOcuz3ZtEqx9ABTDUFH1WXJ40N-AlHbFSpA3f6EoOS0bson78KFXYO4vbCn6hFptWkKq60cfyhUtt5CggELQnGwvhkmpcipRbChjSjhAbgNThtP4sRmPL8Pf7p8FHV4D0xz7jcp3zj6X44dSrRItBrfUSn9MIsK1eDSLqAooeiOTLvMPWcX4nlz94x5C4bwfvxXIj0QN2ktWGIvsZJejn336FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94eb35c039.mp4?token=mW-Ug_57wgUgDXLmyxDw5O-XYxVhA7S-igS2Uw8G5blNg6qF1slO0nlysQkLM1dBIBED87BiUSMu4HpQDaK93Ht1ITqiREbpCcbcWciFlpdVdpjM6Tvq6mf9bsllZOcuz3ZtEqx9ABTDUFH1WXJ40N-AlHbFSpA3f6EoOS0bson78KFXYO4vbCn6hFptWkKq60cfyhUtt5CggELQnGwvhkmpcipRbChjSjhAbgNThtP4sRmPL8Pf7p8FHV4D0xz7jcp3zj6X44dSrRItBrfUSn9MIsK1eDSLqAooeiOTLvMPWcX4nlz94x5C4bwfvxXIj0QN2ktWGIvsZJejn336FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇨🇳
🇸🇦
یک پهباد ساخت چین متعلق به نیروی هوایی عربستان سعودی در آسمان جنوب کشور سرنگون شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69819" target="_blank">📅 01:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69818">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLT9nOrd8oXIU_faWtHmZjybtQspThvfagr1bJ6Mz7vLPjD22JbPLGvocevoaJIwo_o9_4A0LmWPRuG93DXuxQQ99b_uyNTKb27rGQU_8KszyHYoFcO0Mll5MMpWtIp_xPxHpOqVCb1oQrBrJeeixFgbTu-misf0uZHupwa7ofJHeWr5PiaWBkHkLqVs6L5V_fD6xIRSID2cO7_ls0CRWeoO3PLhGDmkiv9N5pr3R1tpXp4U6rGV8-WaT6AC88dP6WDeu79DkgaA_7b3LYPleBWoEjNCSZP9I05sUkqvzuM7navhV0YnRFDRwLKfa0CmGyGC27qBxKu0VZu5eX0QGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در تروث سوشال:
51سال رفتار نامناسب!
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69818" target="_blank">📅 00:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69817">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dbf391292.mp4?token=uFiwIsNmFueBahLa7ywmE8GVw0AkHVAgtQOR56YXdV2ewMkWgLrhbw6FPYJoJXO7UHE9KY-NyFqyp9u1oyVzA8bvYHjGs1zYJeM_J5-YHNr4R7PO859lgDMoi2bq6OOHReTsFxuqalaV_CyoTmD25CZijmkCUh_4SjWciKyauggJbNzrAFs7gpAqN2vqwKFJ1FZ7k_UXW2lhZuIXy-i2P8BBg7UN-BJb0zjMfiPk2wrFHYEv_fO2rBVMnuFmX7kPNOP9RyrWCqhpo3IPEmzfo-6FeYOW9vviOCwiaMNyH6MfMXpwkbxL4pOvYQnCa0Uz2faqAPJAwMAEu99t1giNBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dbf391292.mp4?token=uFiwIsNmFueBahLa7ywmE8GVw0AkHVAgtQOR56YXdV2ewMkWgLrhbw6FPYJoJXO7UHE9KY-NyFqyp9u1oyVzA8bvYHjGs1zYJeM_J5-YHNr4R7PO859lgDMoi2bq6OOHReTsFxuqalaV_CyoTmD25CZijmkCUh_4SjWciKyauggJbNzrAFs7gpAqN2vqwKFJ1FZ7k_UXW2lhZuIXy-i2P8BBg7UN-BJb0zjMfiPk2wrFHYEv_fO2rBVMnuFmX7kPNOP9RyrWCqhpo3IPEmzfo-6FeYOW9vviOCwiaMNyH6MfMXpwkbxL4pOvYQnCa0Uz2faqAPJAwMAEu99t1giNBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
آتش‌سوزی یک کشتی در پی حمله سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69817" target="_blank">📅 00:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69816">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه‌پاسدارن یک کشتی را در تنگه هرمز هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69816" target="_blank">📅 00:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69815">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec1565ac0.mp4?token=jHZN-e5Ju2bc8KZ04rUEH7DfSIT_gGf1QZ9vdY_FvTsl0kPcNDBhq0SHBfJdftjclz5_wZD3t_2oR4493RGl1KbJtTCKEa8KiZkkmHY71CrtiUi-eTzkCr0h83yJY1kA1I1CCAh4q99lIUX3UgnJkx-8DRMsmCBHwAB1GYNgIijyGsLlue6CP8htGoiSUwvgiXm9FpsjHIGIEluCsaGRlzRbRoOl7ACgRBLM3xIgh9RdGRJFHRy5MbI7oaPM8QpB_g885ANHJozWhnx-RKNLfKhwhyoiVIHrMDbf0tVOwdowzvE6TVXD8t_gb7RXHnAd0jJ6wdlRfVAUCQ1QEXPJsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec1565ac0.mp4?token=jHZN-e5Ju2bc8KZ04rUEH7DfSIT_gGf1QZ9vdY_FvTsl0kPcNDBhq0SHBfJdftjclz5_wZD3t_2oR4493RGl1KbJtTCKEa8KiZkkmHY71CrtiUi-eTzkCr0h83yJY1kA1I1CCAh4q99lIUX3UgnJkx-8DRMsmCBHwAB1GYNgIijyGsLlue6CP8htGoiSUwvgiXm9FpsjHIGIEluCsaGRlzRbRoOl7ACgRBLM3xIgh9RdGRJFHRy5MbI7oaPM8QpB_g885ANHJozWhnx-RKNLfKhwhyoiVIHrMDbf0tVOwdowzvE6TVXD8t_gb7RXHnAd0jJ6wdlRfVAUCQ1QEXPJsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال شده از یه پسرِ جوون تو تجمعات شبانه:
به ابالفضل راضی‌ام جنگ زمینی‌ بشه، یه تنه 500 نفرشون رو حریفم!
ایشالا روزی بشه مکه و فلسطین رو آزاد کنیم.
ایشالا روزی برسه آمریکا رو نابود کنیم و تو کاخ سفید نماز بخونیم.
نیاز به بسیجی‌ها نیست همین بچه‌لات‌ها اسرائیل رو میگیرین داداش...
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69815" target="_blank">📅 23:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69814">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b396273688.mp4?token=dYpAaZjoZPOoDWexchRQ1msAAkZAb-kB_6xg6S52yC8oWuUH82i0pHINHQHQgtuL2undFFIDqf8p5ZdOWIofKFcZNmqH4yAyKtCbGGk5-DcaQ39BmSMatXfqopyVatnByCHxCdxSgJeE--4SDE3T02UMBwxkuMmlGjpAA78QDBQJiiEYJQu0KqG1Uh862rojbeYl2KZEp_heNQGe10_VNYQXrkv9pk-jNEoXmV906gTDgXm8gwuIq-ZpkqRb9zx-eymPxMOJW8ZtifJtwOiJxcbi7-hccc0OwV_fale0cIMOVpUt9mxGUWSpl_8XUc1WUsgQIoDQMBw1vMjwiRYGwznPp-dggRC1GV0bFp8T6RCpjhNXDoFGYB0XB_KcoMTXTLREjAPn0isgxoeU2PUFRZvhucNGRaLDrZoK0WzaSGPcC9rM-0kdO2Lr0_vyqWBzC9Nw5AivU-Gv6S-YZgSmLQfQ8oVT78qcnIEu1JjuwEeevP1XYocOcuZvYuUS3pwzdRjTmA9y831sba996YCvTe8waeqqCS3UxVCVygB7RMaqQcXi7_qh6GzKE2xHP70COTCXiy360GpDqU6KgGKoYpvX7yDASSV5Q02nOTu1hmlJJHFSWfBZ6NZpegTpdDzbZV3s0UajRY1kJu4v3IjpP9v_tfdye8hl6iUqPOQ_WaM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b396273688.mp4?token=dYpAaZjoZPOoDWexchRQ1msAAkZAb-kB_6xg6S52yC8oWuUH82i0pHINHQHQgtuL2undFFIDqf8p5ZdOWIofKFcZNmqH4yAyKtCbGGk5-DcaQ39BmSMatXfqopyVatnByCHxCdxSgJeE--4SDE3T02UMBwxkuMmlGjpAA78QDBQJiiEYJQu0KqG1Uh862rojbeYl2KZEp_heNQGe10_VNYQXrkv9pk-jNEoXmV906gTDgXm8gwuIq-ZpkqRb9zx-eymPxMOJW8ZtifJtwOiJxcbi7-hccc0OwV_fale0cIMOVpUt9mxGUWSpl_8XUc1WUsgQIoDQMBw1vMjwiRYGwznPp-dggRC1GV0bFp8T6RCpjhNXDoFGYB0XB_KcoMTXTLREjAPn0isgxoeU2PUFRZvhucNGRaLDrZoK0WzaSGPcC9rM-0kdO2Lr0_vyqWBzC9Nw5AivU-Gv6S-YZgSmLQfQ8oVT78qcnIEu1JjuwEeevP1XYocOcuZvYuUS3pwzdRjTmA9y831sba996YCvTe8waeqqCS3UxVCVygB7RMaqQcXi7_qh6GzKE2xHP70COTCXiy360GpDqU6KgGKoYpvX7yDASSV5Q02nOTu1hmlJJHFSWfBZ6NZpegTpdDzbZV3s0UajRY1kJu4v3IjpP9v_tfdye8hl6iUqPOQ_WaM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خرازی:
این کلیپ ها جعلی و هوش مصنوعی است؛
من این حرف‌ها را نزدم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69814" target="_blank">📅 23:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69812">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1fdc25902c.mp4?token=jHeis5sv0QlAUUb1xJAvrmUE3m4ZHTqTISZ9Pu41vaOEh2xPGzr5kdDJGBDZQko0CtaTL1KHMcjV0wBQnctN5rrdmFVUb-wg_2e-mCXEwesa4F9UYUlcA2tQMbGNmLeyC5IRTAc5k9H4PlgjVBp78in9xFuzPOKDQ86OoCgcblAMyZhHJZDJtOzOF9XX85JKK32NFgUFxj7yvgvwePpMFbnwQCUbL-WDuAXgN1eZHbPkXtj8upg0GkjU78MURkcb31i5cxASqENAv33_db7Vu4MohawbQerWFFfe-cKggCn4kQ7UhGZpl-CUgohgWlITwDGiK7funEb5EqhfvEfWzg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1fdc25902c.mp4?token=jHeis5sv0QlAUUb1xJAvrmUE3m4ZHTqTISZ9Pu41vaOEh2xPGzr5kdDJGBDZQko0CtaTL1KHMcjV0wBQnctN5rrdmFVUb-wg_2e-mCXEwesa4F9UYUlcA2tQMbGNmLeyC5IRTAc5k9H4PlgjVBp78in9xFuzPOKDQ86OoCgcblAMyZhHJZDJtOzOF9XX85JKK32NFgUFxj7yvgvwePpMFbnwQCUbL-WDuAXgN1eZHbPkXtj8upg0GkjU78MURkcb31i5cxASqENAv33_db7Vu4MohawbQerWFFfe-cKggCn4kQ7UhGZpl-CUgohgWlITwDGiK7funEb5EqhfvEfWzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه ماجرای عجیب و تلخ که زندگی یه ورزشکار رو زیر و رو کرده
این بنده‌خدا یه ورزشکار ۱۳۰ کیلویی بوده، پرس سینه می‌زده و از بهترین راننده‌های جرثقیل هم بوده؛ ولی یه ماجرای مهریه کل زندگیشو زیر و رو کرده...
همسرش مهریه رو می‌ذاره اجرا و حکم جلبش صادر میشه. وقتی مأمور برای دستگیریش میاد، فرار می‌کنه و مأمور هم به کمرش شلیک می‌کنه؛ گلوله باعث میشه قطع نخاع بشه.
حالا با وثیقه آزاده، ولی هنوز داستان تموم نشده؛ همسرش گفته فقط یه هفته وقت داری، وگرنه دوباره باید بری زندان!
از یه آدم سالم و ورزشکار، رسیده به این وضعیت...
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69812" target="_blank">📅 22:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69811">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🇺🇸
وقوع یک حادثه امنیتی در نزدیکی باشگاه گلف ترامپ در شهر بیدمینستر، ایالت نیوجرسی؛
فرماندهی دفاع هوافضای آمریکای شمالی (NORAD) دو فروند پهپاد را که حریم هوایی محدودشده بر فراز بد‌مینستر، نیوجرسی (Bedminster, NJ) در نزدیکی باشگاه گلف ترامپ را نقض کرده بودند، رهگیری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69811" target="_blank">📅 22:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69810">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rakATZz0OLh7wdT-s7XT2HGWR4ZO5hK0C16CzOW5XCIFdnqA1OgF6PQCXYt71tmH8WrC1dYXXWtFAClvhkk-e4VDRoKqSmLbL52z2TImwIBpjmx8eZ2DYfqadZ__BwJs1NxQPfWFNzM9UMSgVrz0ywh96qlcX1oIvZWxNt39Yy2bXO3tzUQF4ODV-ZRyhrFxe4dQ1Dqfc1bUz_WKZ0hT608hD_r1DgdOIkHUv1pBsUjnHVlQvjrpzRS335h0RgVyERyrCfEyl3lIOJD4VK3SDN3AJfu96KwAG1euOWsFTdRAVnQmGLngxAyeiL6kK9_942oLYDlCHebwJRVJUI5eHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
با حکم مسعود پزشکیان محسن رضایی رسما دبیرکل شورای عالی امنیت ملی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69810" target="_blank">📅 21:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69809">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
یه فلسطینی به زور بچه شو میفرسته جلو سربازای اسرائیلی، بهشون میگه شلیک کنید بهش!
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69809" target="_blank">📅 21:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69808">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNH7yk9ZuL2t7-Z8nIoHkmTnN3XxWfqQyvvORg8t4mK_PLiXC4n2T6G8Cf_mUudGj56oJ7ijlvP-qK4_zrgJsBPoy64SZFSbakTBhI7z406Gca8k5sakL9Flbxh2AeWXwMkX1u-8Dow5UHL-Xew5QmyJzds2zZ9yF3qplWgAtrhgw_gob0UJMkiEW-eQ-39OgZbi5aizjQRPUXJA529Pz0b2bVxXx2tj1tmE-Jikc3_ORm31KwD61w9T47EjbKKxn5Nw083NHvm-JYnvFRYG6in2xcfqvBTEeNHzuRxdtoOVKwwbQrPQibCug6Jo2yZQXNQ5m3l2RHOD6c2U9ZjJvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
🇺🇸
اکسیوس به نقل از ترامپ:
ایالات متحده در رابطه با ایران «بی‌سروصدا» عمل می‌کند، که نشان می‌دهد واشنگتن فعلاً از اقدام نظامی عمده جدید خودداری می‌کند و در عین حال اجازه می‌دهد فشار اقتصادی افزایش یابد.
ترامپ با این استدلال که ایران از نظر اقتصادی «در وضعیت بسیار بدی» است و در حالی که محاصره دریایی ایالات متحده فشار را تشدید می‌کند، برای پرداخت حقوق سربازان خود با مشکل مواجه است، گفت: «این [مشکل] حل خواهد شد. همیشه حل می‌شود. مثل یک بازی شطرنج است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69808" target="_blank">📅 20:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69807">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🙂
لحظه کمیاب واژگونی کوه یخ غول‌پیکر در سواحل گرینلند؛
ویدئوی ثبت‌شده در ۲۵ ژوئیه ۲۰۲۶لحظه واژگونی یک کوه یخ عظیم در سواحل گرینلند رو نشون می‌ده.
با تغییر مرکز ثقل بر اثر آب شدن یا جدا شدن تیکه‌های یخ، این توده‌های عظیم برای رسیدن به تعادل جدید می‌چرخن.
در این فرآیند، بخش‌های آبی‌رنگ و شفافی که میلیون‌ها سال زیر آب فشرده شده بودن، برای لحظاتی در معرض دید قرار می‌گیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69807" target="_blank">📅 20:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69806">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=ftniLweDWCYrBrMVaJ_fKsvQNJAK5N1yy2GJy0vgUdstWS6etxuaBfe1Lshv15pNobWkp9OsO77A_vMywaVA8EqJh7IJK1jOwuAVqEUIiDKViqQgWCcA8NXW3Q2H3nUugQ9ts-CPLqEpbKcE41Tav8u3fN3cM6lg-1Ja8m5ES2JUO3wa_R9D4t41_PxokW4SG0u3X23h11mY5vDr_44fvGxtGtKvOEdeKVXo4AbADorTKNWmCu50f9uq6Bx1qnFkHxsi70l2bdSx3N1ciTSeXm33pN99vJh6NR9SSnFABPqxXG-zaN0rFUFRX2tzcOfdSFdAdHcPTJmqQP9DIJJAxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=ftniLweDWCYrBrMVaJ_fKsvQNJAK5N1yy2GJy0vgUdstWS6etxuaBfe1Lshv15pNobWkp9OsO77A_vMywaVA8EqJh7IJK1jOwuAVqEUIiDKViqQgWCcA8NXW3Q2H3nUugQ9ts-CPLqEpbKcE41Tav8u3fN3cM6lg-1Ja8m5ES2JUO3wa_R9D4t41_PxokW4SG0u3X23h11mY5vDr_44fvGxtGtKvOEdeKVXo4AbADorTKNWmCu50f9uq6Bx1qnFkHxsi70l2bdSx3N1ciTSeXm33pN99vJh6NR9SSnFABPqxXG-zaN0rFUFRX2tzcOfdSFdAdHcPTJmqQP9DIJJAxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
طرفدار حکومت در واکنش به کشته شدن حمیدرضا رجب‌زاده:
شما زدین مبارک شما ما زدیم مبارک خودمون
خدا سرشاهده جرائت دارید بریزید خیابون
یجوری تیکه تیکه تون بکنیم یجوری ریش ریش بکنیم شما رو تاریخ تو خودش ندیده
به جان امام شهید قسم به جان رهبر مجتبی قسم شما رو با کارتک از وسط خیابون جمع خواهند کرد
جنازه شماها رو میدیم سگ ها بخورن
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69806" target="_blank">📅 19:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69803">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d_t5SiTL96Pr5GZBq1kh3epx6siGI4C26pit36XrvJn1wFU6hRb6TL-P1xXKjFJet8J_Pe5t5xH6XypbP6gU99keBKqqdeZjD90DqVJsNHxXXFCTtJt8pFUF-YBjNxyS3GMnznhEdlAlEmmLjNYQMVW8-qiQXkdZ1Nip93HwTwX_EL6mhtG2Yo4sOD2-6KvUFZrLkLbULES9_YT8kJ9KSc8AoZM_rX2oIDTdrx-zn0ET0-P013n5fGYZlnXCEMgUidex3tGzHOi_ixFEHWsJdJQp3DVijuwP4W8Mm5AfccebZjf71XeuCAp7wGQ8iIqTVbc0N8miou16dBcgAilTew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ROj62qA_0OdyNr0NCUVm4qQMRx_EBzJRVncZJrgxYae2vp3FSYsQc9G3fD3R788etqOLCVCqYq_2ixskzjFsAtDx3Zx4AZQewc4oTCYS1uq0drhKDl1vDLjrqMrPLwyKLD1kw-SM2Xq3iQCDyKvEvhKyw666rb-6VeHQ2nHIaeb0fmcQ0EAbXhoo9T_KtpnlVkdWhcQol2zotSSqHvXcIdMXbzPL6kwuGS-pbv44LOR0CEmf-FqvqWeFeO3dtbVGyoVmBhmE_ALuXUjBZDVbl3zbOypnf35jhqaEmYjEDH1OmMfixMGDZDxUeRsayH5llDPay2gmPMIEOKv-6cYbPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rsOeS6ROrYmLCWuiW4On05TAHx4EKjstqOf74kSJtUBEYNd_V4T8UMxWix-_A8CrTwawhLDmp9kqVXrlTMH8-eIzH4WM-jYpQKdP0MaBCXgunLRzTLngEJP-XBjA5VhXbM17QgIbXO-MhpwOFsGz8Img8qzm-OzJYT0761f3lvVGfECaxOtzOWHOV3gDTeLf0WjtbyPP5Ju63Y1UK1QfrX8C6JTya81b5KZNST0QKOerrYYjrojiVqNwIlujYzYysTUbEkPNHwirRIxDborAlhMQeEQdf5ILiESFHnBCwZPy5Flody8XeiYq90H2jsfnv7HHN4VVASFg6aZPt2a8ZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ریورز یکی از مشهورترین فمنیست ها که زن رو برترین موجود میدونست و خودشم علنا لز اعلام کرده بود با یه پسر خوشگل و پولدار رفت قاطی مرغا
☺️
☺️
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69803" target="_blank">📅 19:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69802">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0cbb95dc3.mp4?token=rVbDcc_bedmkoE7abwmC_jWIE2SDxW8SKfthatFgxwz4jVfJF7b4KR4LpFATFzCXjSDY8E58QKt-5uv5KqDQJfEMQ-X_Nuj0CAG2HbuGzNVidP-WyCAJVQrgeHRYazkcn8olPySn-2WfqETeg6J17FtaWeySggoIP5n_pYuRybUGo-OW3yew39Jy0C1dYL12RpQKcLAWYqUWIDYxMgdlrHiGxEqPAa2hJFPM6eutSf67dBwp7JUU_u3ysAa_HFwiu3NVV7DrhkjczIX2s73duroqMqsU-4sagUjrnQr79xY4Sz8J_GLwWca5yXFFYYBvsDEP5hKe6o89gktGaf3WPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0cbb95dc3.mp4?token=rVbDcc_bedmkoE7abwmC_jWIE2SDxW8SKfthatFgxwz4jVfJF7b4KR4LpFATFzCXjSDY8E58QKt-5uv5KqDQJfEMQ-X_Nuj0CAG2HbuGzNVidP-WyCAJVQrgeHRYazkcn8olPySn-2WfqETeg6J17FtaWeySggoIP5n_pYuRybUGo-OW3yew39Jy0C1dYL12RpQKcLAWYqUWIDYxMgdlrHiGxEqPAa2hJFPM6eutSf67dBwp7JUU_u3ysAa_HFwiu3NVV7DrhkjczIX2s73duroqMqsU-4sagUjrnQr79xY4Sz8J_GLwWca5yXFFYYBvsDEP5hKe6o89gktGaf3WPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
یک فروند پهپاد بدون سرنشین جنگی (UCAV) نیروی هوایی ایالات متحده از نوع MQ-9A Reaper که از فرودگاه چابلی برخاسته بود، در نزدیکی گورستان چابلی در جیبوتی سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69802" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69801">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">پول درآوردن از بت دقیقا جاییه که فرق استراتژی داشتن و ادعا داشتن رو مشخص میکنه
👌
15 بازی 15 برد
✅
من به پول شما نیاز ندارم و چیزیم به شما نمیخوام بفروشم g18 لینک چنل https://t.me/+_btGj-rRAxs3NGVk https://t.me/+_btGj-rRAxs3NGVk</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/69801" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69800">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PY_dbzVBF907WIgKucCiszqHVMnQprLbsaVCZgKATC6hGP-YZvjiPVsWMIdRFdZ_B74-riZmrHWEMCNhjA9GEiu_Mg7bNit-yTd9cNzR6QYT_ML2BaIHkkwHNiRKOblnnH8TVzQikVYCQi7p9Re26jBWLzYBNiQJFHvW0sDV3TBwwL9do2w2waCxHpv9n1rEbQCc5XyJSnt7guaGE8qOtGz5qkuqIC1Jqr25NB2kxK0y38baAFVprbHLTCtJJUmWf22a4VZgSC3QJMS-PM-4LlW5bKbrWiFCTbSjq6eclvkK4n_YHHEgwv2iw7bsJ75qNl4I_KjiZWHVB_Bcan11fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پول درآوردن از بت دقیقا جاییه که فرق استراتژی داشتن و ادعا داشتن رو مشخص میکنه
👌
15 بازی 15 برد
✅
من به پول شما نیاز ندارم و چیزیم به شما نمیخوام بفروشم
g18
لینک چنل
https://t.me/+_btGj-rRAxs3NGVk
https://t.me/+_btGj-rRAxs3NGVk</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69800" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69799">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411943761d.mp4?token=TGZz0WSe2_tvG-Ikr262rpMT7y2jpxWIyW2TjNGMZuWFPiJ06prySUHAS67usx5PPpU5u96rry90Tf6GA_IhDODLw58TufeYLFFEmgj-GkqoRtVCky4Qfny1fqW0xuQwYOsxA30yKPr4-PhrvIz7WDgTWdUvm3AWojxd54dR1EFDlSuudMNm6pjdvoDssLctNbHvoEok_XrskKfy-JCf09qST_muDRnECjWIBBjMLPMFBp5EAVGKrS_jh5WlRl0Nv_A2KD51CeNXbbw1PhZ49zEjgAGyDR1hEqaoELWh2QTrnWc001BzxovYQCavj7-5eL4Gd3LeLEc1jww4c6jovQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411943761d.mp4?token=TGZz0WSe2_tvG-Ikr262rpMT7y2jpxWIyW2TjNGMZuWFPiJ06prySUHAS67usx5PPpU5u96rry90Tf6GA_IhDODLw58TufeYLFFEmgj-GkqoRtVCky4Qfny1fqW0xuQwYOsxA30yKPr4-PhrvIz7WDgTWdUvm3AWojxd54dR1EFDlSuudMNm6pjdvoDssLctNbHvoEok_XrskKfy-JCf09qST_muDRnECjWIBBjMLPMFBp5EAVGKrS_jh5WlRl0Nv_A2KD51CeNXbbw1PhZ49zEjgAGyDR1hEqaoELWh2QTrnWc001BzxovYQCavj7-5eL4Gd3LeLEc1jww4c6jovQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
آقای پزشکیان بچه‌ها یه شوخی باهاتون کردن راجب درختی که میخواستید بکارید توی پاکستان، برامون بگید قضیه چی بود؟!
🇮🇷
مسعود:
من فیلم بلد نیستم بازی کنم.
اینکه الکی یه خاکی بریزی و بگی من درخت کاشتم پس تو نکاشتی.
ما نایب رئیس بودیم توی تبریز باید ده تا درخت میکاشتیم همشو خودمون کاشتیم.
ما کشاورزی میکردیم، همین الان اگه برم مزرعه خودمون بیل رو میگیرم کار میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69799" target="_blank">📅 18:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69798">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0eb6125750.mp4?token=kwxJadV3C6WtkIiVqTQrWWKHeXeaGe39p_Aj3qJbUyMRQiyx3gSXVuIDB4e0Ii2vRMQEzsXCNryPksHWT6Ry7YYX8XgXt87hqwnE5axB0Awjn3cecEqVGTWaPRMgVKLz8gCO1WzlARcpxerpIIpRaUk3ces4EE5ZAZUZAQRwLWTjSMhUo80IZfHoZ-p74wbt0N0G1MIzkw_0NwO0X38HAPhFKNmZV6YFZdlWuzLS0tBu-OvKaxAe-aUPq-o3NHeTjkTCauDFA-Ba8kA4KLpZgA9OpQwNO5WHw2BtYvyXdR__GkNlwn3irq2o-A1NqCgBxQYlnv6rHkqNgjddfJmDlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0eb6125750.mp4?token=kwxJadV3C6WtkIiVqTQrWWKHeXeaGe39p_Aj3qJbUyMRQiyx3gSXVuIDB4e0Ii2vRMQEzsXCNryPksHWT6Ry7YYX8XgXt87hqwnE5axB0Awjn3cecEqVGTWaPRMgVKLz8gCO1WzlARcpxerpIIpRaUk3ces4EE5ZAZUZAQRwLWTjSMhUo80IZfHoZ-p74wbt0N0G1MIzkw_0NwO0X38HAPhFKNmZV6YFZdlWuzLS0tBu-OvKaxAe-aUPq-o3NHeTjkTCauDFA-Ba8kA4KLpZgA9OpQwNO5WHw2BtYvyXdR__GkNlwn3irq2o-A1NqCgBxQYlnv6rHkqNgjddfJmDlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخشی از مستند«پسرملا» روایتی از چند سال آخر زندگی روح‌الله زم:
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69798" target="_blank">📅 18:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69797">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
📰
وال‌استریت ژورنال: دونالد ترامپ، رئیس‌جمهور آمریکا، از چند هفته قبل برای اعلام پیروزی در جنگ با ایران آماده‌سازی‌هایی انجام داده است.  او به مشاوران ارشد خود گفته است که در صورت بازگشایی کامل تنگه هرمز توسط تهران، می‌تواند این درگیری را بدون دستیابی به توافق…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69797" target="_blank">📅 17:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69796">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNiUASdiea5fYQsyCgUWi13eRfPfo7yCSeRMYMhJ2uIQ2byjZNmm5kk4buEQ6sRJZ5N0Lgli46xy4OMR1UumiP1PYt33ia0-o3GsgtXxfoldMnUg5FNC_Pbn1XUOFqnaOx7j4cbSXqDjH5uUFmxNMgMPTBRMbbFhLHF1YVLwPIS36N_BkUTL6bPovezJyDG8SG8gXh78I0vNpIT_EIfDOLvsjUmKBnGujwk-CttoG-wsq2bf_ldpNTND_NMdSpdkLDIFDM_Y5kT9CUlfTLYo5qVzKrm-6ZcUFqrPb-MIMD802Mkf9nAPh0H4WkNwquDAURSk36yjDlI5qKC5BPX09g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
📰
وال‌استریت ژورنال: دونالد ترامپ، رئیس‌جمهور آمریکا، از چند هفته قبل برای اعلام پیروزی در جنگ با ایران آماده‌سازی‌هایی انجام داده است.
او به مشاوران ارشد خود گفته است که در صورت بازگشایی کامل تنگه هرمز توسط تهران، می‌تواند این درگیری را بدون دستیابی به توافق هسته‌ای به پایان برساند.
ترامپ معتقد است که ایران احتمالاً در طول دوره ریاست‌جمهوری او، برنامه هسته‌ای خود را از سر نخواهد گرفت، به ویژه پس از اینکه آمریکا سال گذشته سه مرکز هسته‌ای بزرگ را بمباران کرد. مقامات آمریکایی می‌گویند که اگر واشنگتن بتواند فعالیت‌های هسته‌ای تهران را کنترل کند و ترافیک تجاری از طریق تنگه هرمز از سر گرفته شود، ترامپ احتمالاً تمایل بیشتری به تمدید آتش‌بس فعلی به طور نامحدود و رفع محاصره بنادر ایران خواهد داشت.
مقامات آمریکایی اعلام کرده‌اند که ترامپ همچنان مایل است تا در این بن‌بست دیپلماتیک جدید صبر کند، به ویژه زمانی که قیمت بنزین نسبتاً ثابت و در حدود 4.02 دلار به ازای هر گالن باقی مانده است، در حالی که سال گذشته این قیمت 3.16 دلار بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69796" target="_blank">📅 17:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69795">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa7b5af888.mp4?token=PEcUbhNLXy12mW-C8OkswUDD7BPMtzrEwJc1GFNJjvnAjcOkdTXjZJdk7z_YKBad0bhYZoLbneBVfja47XaiJz2VfDMVK-zVjvYxe_aj-XbJqKffVmKCvhFilBJlSAQMdLjNzLsGAcpaPe7wx89z-1K8qegWrfxW9IzlNkSE6GvrSsG5nWdOKzLlJXsADXZhhLd-5uF2K5R2JhQvNBxnfQDqqUQ6rDt5VhIhZR6JyucBvvOpw_D5-wyg3Dsna3CfImjAietaVSfAubgDeH-sZGTJCuBuGAAfyGd1ECYxOHV6n2rCQlmqf95BY4yqzRgHI540kPAZkFeLYL7ksReUgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa7b5af888.mp4?token=PEcUbhNLXy12mW-C8OkswUDD7BPMtzrEwJc1GFNJjvnAjcOkdTXjZJdk7z_YKBad0bhYZoLbneBVfja47XaiJz2VfDMVK-zVjvYxe_aj-XbJqKffVmKCvhFilBJlSAQMdLjNzLsGAcpaPe7wx89z-1K8qegWrfxW9IzlNkSE6GvrSsG5nWdOKzLlJXsADXZhhLd-5uF2K5R2JhQvNBxnfQDqqUQ6rDt5VhIhZR6JyucBvvOpw_D5-wyg3Dsna3CfImjAietaVSfAubgDeH-sZGTJCuBuGAAfyGd1ECYxOHV6n2rCQlmqf95BY4yqzRgHI540kPAZkFeLYL7ksReUgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تصاویری از یک پهپاد تهاجمی اوکراینی که به طور موفقیت‌آمیزی سه بار متوالی، موشک‌های پدافند هوایی زمین به هوا از سیستم "پانتسیر" روسی را در دریای سیاه جاخالی داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69795" target="_blank">📅 17:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69794">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⏺
معاون برق و انرژی وزارت نیرو:
خاموشی‌ها در مناطق عادی ۲ ساعت یا کمتر است و مناطق گرمسیر به دلیل شرایط خاص، از تخفیفات ویژه برخوردار هستند.
همچنین برنامه داریم تا یک تا دو هفته آینده، محدودیت‌های برق را به حداقل برسانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69794" target="_blank">📅 16:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69793">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3f5dd815.mp4?token=HJMQKtL9aPe-S0PWDnU2AIfHNMaGbr8IJ7krIx1zt1l64_uT9Grx-1xAwq4nGgy3WeaVDxUSfCGmQHyU9oXfRTcqi775KadQsbd4HC_lLPjYiutXiJuKi9Yud2ZTq77t5E6f7lSttVW5_-628CvOew09Rro_ETy_sR1xqZYsgj9CR2GHKXP8z1nV6RpRBdA5l-SftU8DZ1j5eI50ngWMgGG2xt3wTGfvK_pcdD3mJrj-DcHcWc-VKSax0BgIf9ngLsjvG65Uy6LKtA-txaxf4-lQhSOhKQqJ6FSm_X-sFAhmCj9mm6nAKSjtjl-bVx3xhDSfOMcUtfLn6ub5xGbJLy7UEm48U_rOHd9P2UEj9VH9zkzGOE5Og-ZSlUKPES4qwW_EOItm4_jswQ16ujGpm8nRB1EFGLiYYQ42-ypM_P8W53F2H83BZEtGbsFsATuSO795flL6YK5VLfiEijspOXhSkavY7UIHVB-yMAcrM1G9qLvHngVMkuOqnsZdcmse1HfFIQsgkq6b-hIb4yzIqUg8cYF7uPEy38oojYlaptamgmfW3kGrHimj8nK4-wseuvzKm55kJd1FjigywzC7R-b7znYC6yO0gBMCQrmE1L3A1k3DPQkQjgp1V7pGjeD_vEcMRIwzkcDQF5JZE-lwv21GFOepMm-JWbw4EwXd3r8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3f5dd815.mp4?token=HJMQKtL9aPe-S0PWDnU2AIfHNMaGbr8IJ7krIx1zt1l64_uT9Grx-1xAwq4nGgy3WeaVDxUSfCGmQHyU9oXfRTcqi775KadQsbd4HC_lLPjYiutXiJuKi9Yud2ZTq77t5E6f7lSttVW5_-628CvOew09Rro_ETy_sR1xqZYsgj9CR2GHKXP8z1nV6RpRBdA5l-SftU8DZ1j5eI50ngWMgGG2xt3wTGfvK_pcdD3mJrj-DcHcWc-VKSax0BgIf9ngLsjvG65Uy6LKtA-txaxf4-lQhSOhKQqJ6FSm_X-sFAhmCj9mm6nAKSjtjl-bVx3xhDSfOMcUtfLn6ub5xGbJLy7UEm48U_rOHd9P2UEj9VH9zkzGOE5Og-ZSlUKPES4qwW_EOItm4_jswQ16ujGpm8nRB1EFGLiYYQ42-ypM_P8W53F2H83BZEtGbsFsATuSO795flL6YK5VLfiEijspOXhSkavY7UIHVB-yMAcrM1G9qLvHngVMkuOqnsZdcmse1HfFIQsgkq6b-hIb4yzIqUg8cYF7uPEy38oojYlaptamgmfW3kGrHimj8nK4-wseuvzKm55kJd1FjigywzC7R-b7znYC6yO0gBMCQrmE1L3A1k3DPQkQjgp1V7pGjeD_vEcMRIwzkcDQF5JZE-lwv21GFOepMm-JWbw4EwXd3r8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
به یک نکته جالب توجه کردید که ایران به همه منطقه حتی فرای منطقه حمله کرد جز اسرائیل؟
تا الان به ما حمله نکرده ممکنه تو آینده بکنه ولی میدونه جوابش چقد سنگین و دردناک میشه.
شایعاتی هست که اسرائیل عقب نشینی کرده و ضعیف شده.
این شایعات از کسایی به ما روانه میشن که میگفتن اصلا نباید عملیاتی توی لبنان و ایران بکنید.
لازم باشد بخاطر منافع ملی به بزرگ ترین دوستانمان نیز نه خواهیم گفت.
منفعت اسرائیل رو پایبند به هیچ توافقی نخواهیم کرد و ما مستقل هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69793" target="_blank">📅 16:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69792">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef1f7ed1d6.mp4?token=qxwkZPmkbrocOm4Aic6HZY13os_Bbe3n39RQF7burvH3ef4yj4OGJ0YFk8yJtfy36K--1IaR8iJH4BO0OCKk3bykuLUZWU4uo0gj2ztmC1PNtV7cbYrULV1wWaLsLRwEZpgbLUogjStk7B0rBBiRdPeJS-5C_eaJP6t_1Tm91QV_TkPp4-ZKJ-rGJ6jZcPqUFd3VBhpSkRnrheRev2FOFusMEBR5DFvUs30FyT0rWRxBXFiQo4m6JrWPvXdJVLRZV9amFehzD73F1rCcI83FFlizCBsefZNZe8j8Os89romBqEEoFVNdeV9FHf8SY38wZLe0ql70JtDe8ej6oepMug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef1f7ed1d6.mp4?token=qxwkZPmkbrocOm4Aic6HZY13os_Bbe3n39RQF7burvH3ef4yj4OGJ0YFk8yJtfy36K--1IaR8iJH4BO0OCKk3bykuLUZWU4uo0gj2ztmC1PNtV7cbYrULV1wWaLsLRwEZpgbLUogjStk7B0rBBiRdPeJS-5C_eaJP6t_1Tm91QV_TkPp4-ZKJ-rGJ6jZcPqUFd3VBhpSkRnrheRev2FOFusMEBR5DFvUs30FyT0rWRxBXFiQo4m6JrWPvXdJVLRZV9amFehzD73F1rCcI83FFlizCBsefZNZe8j8Os89romBqEEoFVNdeV9FHf8SY38wZLe0ql70JtDe8ej6oepMug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آمادگی جانفداها:
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69792" target="_blank">📅 16:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69791">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26df8fab5.mp4?token=bIq8szrHvsYkvm3V_e68T6O4PNDtT9-Vc4azlEGt5Vu4IT4zUNWI-PjtkiMeeNAO-2KeOHhucAS5Z-X7O_CzsNqZ073kTj89GTRMuzmbUkUCiDhOJ7l9EfZl4mGJOc47MA77cGxiZiMjo3Q--vRVP1uPLky2wySbmUuNo1sP6_0BeEHEekCam576omnKv0j4flDM0Dd_idGCd6mU329IAaGwc0EenhZMlOGWRAIAcqOhoDCr6fiFqnrpPO46gy4HKdmA8l_lmC-8daCYdN3RDOYevIkqByOJVqrz9onFsQxiCRnMCG9PnkT84oCBWZ66qvRUn9t0YkqN-In1bzFpvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26df8fab5.mp4?token=bIq8szrHvsYkvm3V_e68T6O4PNDtT9-Vc4azlEGt5Vu4IT4zUNWI-PjtkiMeeNAO-2KeOHhucAS5Z-X7O_CzsNqZ073kTj89GTRMuzmbUkUCiDhOJ7l9EfZl4mGJOc47MA77cGxiZiMjo3Q--vRVP1uPLky2wySbmUuNo1sP6_0BeEHEekCam576omnKv0j4flDM0Dd_idGCd6mU329IAaGwc0EenhZMlOGWRAIAcqOhoDCr6fiFqnrpPO46gy4HKdmA8l_lmC-8daCYdN3RDOYevIkqByOJVqrz9onFsQxiCRnMCG9PnkT84oCBWZ66qvRUn9t0YkqN-In1bzFpvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ژئوپولیتیک:
ایران سامانه‌های پدافند هوایی ساخت داخل خود را به عنوان جایگزینی کم‌هزینه‌تر برای سامانه‌های گران‌قیمت خارجی معرفی می‌کند.
طرفداران این سامانه‌ها مدعی‌اند که آن‌ها موفق به رهگیری هواپیماهای پیشرفته شده‌اند و استدلال می‌کنند که فناوری بومی می‌تواند بدون تحمیل هزینه‌های سنگینِ تجهیزات وارداتی، دفاعی کارآمد فراهم آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69791" target="_blank">📅 15:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69788">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pFfWiX1UfdUOCJzbE0geG6tSUQ579atdR1kwPMNNO-8avoBI-MwS6KUKu-KGb5__jUqPiEZAqF9UYV04y830qOQRF0s-EVjq3ZM6TcQTqj-fWZX0Rx7h1jFbxVfqaRnY6JrJDQgyBzoENmlRkqZ-X_L7digtcEhy4248Lu8SSr-ZPxVMzblpfT8pF5wxGff0Bcj5RoS8QZK2po5nHVZJk4kVX-xT54uxfSrEX63rGFlO8ljLRprXFoJ5X1BSlGz2XTMa_AZZHlnmAL284oxs3d3agcYb7k6Ph3AfJbtTGq-7hQoKBbK4DcFkpwWUyXpd_nsQNhJSZUmqNq5RTjKSaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rPABaZniwyBVT1r4QzLtbrlb9iG6yNVFuvscJ5mugwnIAURuQXhgGnF49zpUMjCTw5AXU9y7oAofAwQqVIIGIVEkyhI659zmGfYK5vA-f7P5rrjyIbEBQAQu_go3hYjpNrUaKVbkl_nTiXwMziNZhiHaxx47f364adAWgJXYPbckX0M1k37H8GHvJ22T2caRefSDJ-0-vS6GT_CYxC3Njep5EUUNC1KoP2A7kRwFMZqsyLAYhg8-5DBJsH0xcx3d4tkO-wLg4sXiPqnEnmuS_6Yd-hNKmh9X59GOiUA9Wtbvm9Wf6CsPS5wlAqy7NvRPXKvFj6s7QJIQId9yNOYzJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Frg_9bxoNT415QdTunheO5Ev93cRi5yj4jX_eV_jSa5v67dzB4PhfqgSNp2lDPVQPCUSPLuaIIXsE99nxdG7bBseUsyoc1rw_EZnz5qZ3rnaX1sc-5_XEFtTWSONG-Mn1TUppdf0LZHBtyeUY_d-69QBEYv-xBuuu4aXEVk7J5nds7ws9GdwdYvYfbhc-qh2cZ1NeDMgx_Nk_m4fU7uunJlix2q7L042rzhcmqxWFIJycGEVwRkA7X1GC3wZu320LUZ0nr6IEv2jb_Mo1eCoY0KZogyTORmOGoFZvh645shIumCY6M0RZ1RDpb8m1KD5JwzMVR-pRZYMnR1bMx_-og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
🔞
ابعاد جدید ماجرای قتل حمیدرضا رجب‌زاده توسط یک بلاگر دختر:
حمیدرضا رجب‌زاده، یه مداح جوون، بعد از خروج از خونه ناپدید می‌شه. پلیس در تحقیقات به یه بلاگر زن می‌رسه که قبلاً با حمیدرضا در ارتباط بوده و اون روز هم ازش برای یه ملاقات حضوری دعوت کرده بود؛ حمیدرضا به این دختره بارها بخاطر حجابش تذکر می‌داده و بهش می‌گفته بحث سیاسی نکنه
طبق اعتراف متهم‌ها، این زن با کمک پنج مرد، حمیدرضا رو به یه محل خلوت کشونده، بیهوشش کرده و بعد اون رو با ضربات چاقو به قتل رسوندن و قلبشو از سینش دراوردن و رو صورتش مایع منی ریختن، بعد هم جسد رو به اطراف پرند بردن و آتیش زدن و از صحنه قتل فیلم گرفتن؛ با اینکه چند نفرو گرفتن ولی متهم اصلی هنوز فراریه!
🔞
ویدیویی که قاتل منتشر کرد
⚠️
⚠️
حاوی صحنه های وحشتناک
⚠️
‼️
اعترافات بلاگر دختر:
من با مقتول در فضای مجازی آشنا شدم  او مرتب به من تذکر حجاب می داد و می خواست درباره مسائل سیاسی حرفی نزنم و زندگی مناسبی داشته باشم من این موضوع را با دوست پسرم درمیان گذاشتم که او پیشنهاد داد مداح جوان را با بهانه ای به محله خلوتی  بکشانم تا او با دوستانش دست به قتل بزنند او گفت که گروه های منافقین بابت قتل بسیجی ها پول پرداخت می کنند بخاطر همین بعد از اینکه مقتول کشته شد فیلمش را گرفت تا به آنها بفروشد
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69788" target="_blank">📅 15:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69787">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPIq1vJc3UOwYKpxHRwmIVgpvyKE-i2DdougzplChtOS5B592JNUrfv_5AGQEvIns5zhGjn7MzdUxytoNLLGGy1X7UyteYswxTTvaNJjCZxGNzISRoN6lEVeNQsLIQwYJpo1YEPCPzRZCSuvjoNgozZH0_I32kcoT4A1sEgof_-xXBPX-iLwRk9bB49GgUzrVtcF51JX0H4n2xlRUViViGD-tBJ6XNUVHypKuCx32DuWqiYyGIuvUAoWPc3wdu4zXqecQY4puD6CP7w6VRZCbOYnAFPCGzdjBUdSg2mJ3kLYaNtR_34aSgtHo_nlyWUMmySAKRBbYnE5tdLtNkWONQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
فرماندهی مرکزی ایالات متحده:
ملوانان آمریکایی در حال تعمیر و نگهداری هواپیماهای F/A-18E Super Hornet در عرشه پرواز ناو هواپیمابر USS Abraham Lincoln (CVN 72) هستند تا اطمینان حاصل کنند که تجهیزات گروه ضربت ناو هواپیمابر برای اجرای محاصره ایالات متحده علیه ایران آماده ماموریت هستند.
تا 8 آگوست، CENTCOM 53 کشتی تجاری را تغییر مسیر داد، 2 کشتی را از کار انداخت و 2 کشتی دیگر را نیز توقیف کرد.
🔴
ارتش ایالات متحده همچنین به بیش از 30 کشتی اجازه عبور از محاصره برای کمک‌های بشردوستانه را داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69787" target="_blank">📅 14:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69786">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
ادعای فارس:رئیس‌جمهور با رهبر معظم انقلاب دربارهٔ مسائل اقتصادی و نظامی کشور دیدار و گفت‌وگو کرد.
پزشکیان همزمان با شروع سومین سال ریاست‌جمهوری با حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای دیدار و گفت‌وگو کرد.
در این دیدار به‌تفصیل دربارهٔ مسائل و مشکلات کشور به‌ویژه تأمین نیازهای معیشتی مردم، شرایط موجود جنگ تحمیلی سوم و آیندهٔ پیش‌رو، تحولات حوزهٔ نظامی، راهکارهای ناظر به تأمین منابع و مدیریت مصارف «ریالی، ارزی و انرژی» و همچنین تعامل اقتصادی با طرف‌های خارجی تبادل نظر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69786" target="_blank">📅 14:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69785">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‼️
صحبتای این خانم در مورد کافه رفتن و پیدا کردن پسرای پولدار، خیلی وایرال و جنجالی شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69785" target="_blank">📅 14:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69784">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ab9ff0322.mp4?token=EXqy5gEJVi_VwrkQirp12BDZma0B9BzSCy9nbFPxnlgSU1eua6kwnjZzLvc41g4eafkGCe-ZIAewizEZ-14LVumrcz8pCVX738ssvSbRt6DA5MdMKWiXG0ygyDEjBTcGkE5N4K8kJdhs7DxzUHODTdx7ClwG9aqxifYu-iCpWJBwZCuez4lMw5ds0TxnRjq3WlRAcfUXRew2df-DmE9SnqEnRQfUqRfZo4TZxhOjxuzZrFjXsqUDI00nIbqOw6fZdXKQUI7FRkgx2eIaj95Mb_c77hhrS9dOer3zm0N4CAZ8Tc88pWr7WZvtm7uGHj-adcq9nk6vFDYBsMnNPtInWA5taZUlRVeVBhtFU_ZbwVRlab4F7hq17aGn-ddhuRgcFw-N7saVUd57Q9c1ilKv5XYeGgzr_OQA5LaT45J3JNJh312GM3CyMe-v4y6ZiTZKxcu1xSV2jisaGE6pN9sF80VUeVAkJZ5qShwR6TZpuE6AFjP9YBMtpEmppqk374kPelP19sqwQPZ2wK8JGuHn8BEggpiLAzG4RvWKRoG8Vr44i9WjWrfOoV-x3RZeZ6O2-NggUdKd1gN5-orQ-i-xS35uiw1MUojMCOE8-hUKhjxWcDdYza8UYG2r6GWhDqKV0mAxpac_3dBrVY2XuaYjMOql7iWK7nW22jWxb-6qeWs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ab9ff0322.mp4?token=EXqy5gEJVi_VwrkQirp12BDZma0B9BzSCy9nbFPxnlgSU1eua6kwnjZzLvc41g4eafkGCe-ZIAewizEZ-14LVumrcz8pCVX738ssvSbRt6DA5MdMKWiXG0ygyDEjBTcGkE5N4K8kJdhs7DxzUHODTdx7ClwG9aqxifYu-iCpWJBwZCuez4lMw5ds0TxnRjq3WlRAcfUXRew2df-DmE9SnqEnRQfUqRfZo4TZxhOjxuzZrFjXsqUDI00nIbqOw6fZdXKQUI7FRkgx2eIaj95Mb_c77hhrS9dOer3zm0N4CAZ8Tc88pWr7WZvtm7uGHj-adcq9nk6vFDYBsMnNPtInWA5taZUlRVeVBhtFU_ZbwVRlab4F7hq17aGn-ddhuRgcFw-N7saVUd57Q9c1ilKv5XYeGgzr_OQA5LaT45J3JNJh312GM3CyMe-v4y6ZiTZKxcu1xSV2jisaGE6pN9sF80VUeVAkJZ5qShwR6TZpuE6AFjP9YBMtpEmppqk374kPelP19sqwQPZ2wK8JGuHn8BEggpiLAzG4RvWKRoG8Vr44i9WjWrfOoV-x3RZeZ6O2-NggUdKd1gN5-orQ-i-xS35uiw1MUojMCOE8-hUKhjxWcDdYza8UYG2r6GWhDqKV0mAxpac_3dBrVY2XuaYjMOql7iWK7nW22jWxb-6qeWs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
عباس عراقچی:
اکنون هیچ مذاکره ای با آمریکا نداریم و نخواهیم داشت
شروع مذاکرات بدون پایبندی آمریکا به شروط تفاهم‌نامه غیرممکنه
ملت ما تسلیم اراده یک عده خاص نمیشه
بدون تحقق حق ملت ایران کوتاه نخواهیم آمد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69784" target="_blank">📅 13:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69783">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34556823e0.mp4?token=fT0B7YGmbam_-7JkxSzlbdJiOnzV7GhX5ACZpjZ7631iby4eAl5A7JTl-3K-8MK8WqYypq6KGzi904WkgW_YNrx8aGv6-1Si1R7XBREVzavTQj6u0PtO7Dz1mD3Iquqruv5LO8EJ4fT7HyfiAvoDdf5nTEKTnq6zS5tJbWobeTLKVNaxqK809Xt0pufjo6AbGRFilGe2gBM1L6hULoBaMIOyliiHSQswuNTyi41sUtKbJyqIweldzn2Ndf-7s1nPHhxS9gDMK1RFtpJPWJJdQdDvbERusjSDUejH3bIq7YknHZ9seGDDQF-BN8rDn-qUNjEZs8Y5DROefhN7mptkHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34556823e0.mp4?token=fT0B7YGmbam_-7JkxSzlbdJiOnzV7GhX5ACZpjZ7631iby4eAl5A7JTl-3K-8MK8WqYypq6KGzi904WkgW_YNrx8aGv6-1Si1R7XBREVzavTQj6u0PtO7Dz1mD3Iquqruv5LO8EJ4fT7HyfiAvoDdf5nTEKTnq6zS5tJbWobeTLKVNaxqK809Xt0pufjo6AbGRFilGe2gBM1L6hULoBaMIOyliiHSQswuNTyi41sUtKbJyqIweldzn2Ndf-7s1nPHhxS9gDMK1RFtpJPWJJdQdDvbERusjSDUejH3bIq7YknHZ9seGDDQF-BN8rDn-qUNjEZs8Y5DROefhN7mptkHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا متوجه بشید با قیمت الانِ یک نوشابه، تو سال ۹۵ می‌شد چه چیزایی خرید...
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69783" target="_blank">📅 12:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69779">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtJaNuZlR0-rLx0Yk91IHvFjy5OaeTCO6CsvkimY2rCCSSDJyoTaWkis0e4Ka8tPgD8XWvQVV3LBA45eHAvRjNDQ_4w_11AZv_RW4Wnif7M92YJJM9MmsG6nzbLzRZwqJOIe_juvfy06B_prAREYaRyPfetugRducTM4qMJ9Ar2xum3Qg6vneX8Azh-nbDtwWN5WVhWg9dCoaoo-9QP426zaF-rrb7OSxw8O2y3L_KBLagzgnuQWyHHvcYJQlnm6FT9kDTMFEWvV12jlJ_s7zxHOHfqrlHsiC7sQrXiL9lCooEHCaWhz26F_CDH03EIQ0sLjnEdXcPiRwGD38y8QmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5f1aeb56.mp4?token=TXB8x3w1N3MVZN8Jn2NhELp98npyQudQlNO4oBTVx3IwRzh_uxrJRmFy7RpsF7Z48C2uZyFz4vJGMXHkW5KyAaDi9hqqwnfUR0ygAL3gqsUd5XtjoRx1Or5-QXJgbGaU7LkhCQU4tPGivwfWNYDpsU6f1w-OjTifpSnJpSMgFlPLRZJRAda8Jic2sO-ZsrfbSeDAIn6ylSaHnDR64Hae6g4b57P6GhhakrX3sPC1lSYt8nY_j0gK1MZcgqS4DaSeZVqBzK0RyPKd2nvwRFKC7knfvR8EkwegoqCRRmZuWIumekrpUmNjpbNPKimfNzuEKABXGyCgn5yo5GLyTVBmsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5f1aeb56.mp4?token=TXB8x3w1N3MVZN8Jn2NhELp98npyQudQlNO4oBTVx3IwRzh_uxrJRmFy7RpsF7Z48C2uZyFz4vJGMXHkW5KyAaDi9hqqwnfUR0ygAL3gqsUd5XtjoRx1Or5-QXJgbGaU7LkhCQU4tPGivwfWNYDpsU6f1w-OjTifpSnJpSMgFlPLRZJRAda8Jic2sO-ZsrfbSeDAIn6ylSaHnDR64Hae6g4b57P6GhhakrX3sPC1lSYt8nY_j0gK1MZcgqS4DaSeZVqBzK0RyPKd2nvwRFKC7knfvR8EkwegoqCRRmZuWIumekrpUmNjpbNPKimfNzuEKABXGyCgn5yo5GLyTVBmsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی اوکراین به بلگورود
نیروهای اوکراینی شب گذشته حمله گسترده‌ای پهپادی به شهر بلگورود روسیه انجام دادند که در پی آن چندین ساختمان مسکونی هدف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69779" target="_blank">📅 12:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69778">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69778" class="tg-doc-link" target="_blank">دانلود</a>
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
r18
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69778" target="_blank">📅 12:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69777">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N33x72PvhTEWZVK69ez0p9P-HDgf4t2EBz6xUJ7kjjf_ygVVHYIK6di5MbtLrMiV1-fXagCZcyaP8X6lzLJPKKi7RkHGQZJvcIGrMqd_1hf5HuqIASxb-FS_VBXArwIQ8Fr71LeFIJq1KKkjTP4M6odd57f0PUZG_ZfYnKpQjMPperCcXdu-M8Zif2HPTlzG7BQ5FH1olhezS0GkEhHQNQNn4k3z0TnWhbPD_MuvjJZjCMpwQQL9ipQhtE3Te-z-dN3HyD3GT9Ec-avYS0Tusnk_EbzG0c1aoaae39DZ14oGFhs3J2uqj-gVuSi_ta3REd6r7sEJh6iXs9BfrnGOPQ.jpg" alt="photo" loading="lazy"/></div>
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
r18
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69777" target="_blank">📅 12:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69775">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c93de8243.mp4?token=i23MxD_HOay6ozso4HLSv9JsY507BavjpwUOHF2LmL0lmx9wTj_v5JEYcl9T8RoMhIPcH69qN-75KVRh78buJ2Uq_PVSsK5uh_2Q8m8cy9wI-VyxQ_GOW1WtBaBBmTCLugkJeIGoLwvqsvMbTxWuVqrxut0SBHkugKPRahGuNZ3-hxZioNkBGkXMF_v3_uKIryTNWIcwvCIxEea-zPUKRBCd45HuWMZoA2Ep7lv7nTipaymA6tL59wkNs8gLFU_e6w5ZpQRokyKpXzxqlusJ8_yW-Q424kNn4lr_twrfJgQ0n3Hv-fpfOvRnK49DlBh3VIQxB50dRleDuPCoPy316g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c93de8243.mp4?token=i23MxD_HOay6ozso4HLSv9JsY507BavjpwUOHF2LmL0lmx9wTj_v5JEYcl9T8RoMhIPcH69qN-75KVRh78buJ2Uq_PVSsK5uh_2Q8m8cy9wI-VyxQ_GOW1WtBaBBmTCLugkJeIGoLwvqsvMbTxWuVqrxut0SBHkugKPRahGuNZ3-hxZioNkBGkXMF_v3_uKIryTNWIcwvCIxEea-zPUKRBCd45HuWMZoA2Ep7lv7nTipaymA6tL59wkNs8gLFU_e6w5ZpQRokyKpXzxqlusJ8_yW-Q424kNn4lr_twrfJgQ0n3Hv-fpfOvRnK49DlBh3VIQxB50dRleDuPCoPy316g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
⚡️
تصاویر جالب از لحظه برخورد رعد و برق به ساختمان مرکز تجارت جهانی «اسپیرز» در نیویورک؛
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69775" target="_blank">📅 12:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69774">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b13fec044.mp4?token=bi-aUBNWuLeLKid0nhLz44JnBbv5uBoY5sEDdh2SutEh70iip3-Ydn5v88OtG7g7dxk4MrA6uvxH-e9QXdsLsedyGMeGAM9plt0q366dJXXbnIjvsdYU9tQEA4tXs2EGhayImr26dDudAATUw2JNN1HA91lwSwLhWVQ_rINO0WImwqWgjW6txXrGqaVTzsbRhj4HglS22a6EDss8fSLvf6Zkhr_bOMBo4yTQ4RkQTlMQBC7ogRchvVlbntUHVPNOnQLLCiv3wa4C1HoRHyeLDh2vJrdXw5NI28LqR2EtLr-yJ-c3EtJODB6ASMEpM_oSP6uWCtW_UA9pJwFy6GKRPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b13fec044.mp4?token=bi-aUBNWuLeLKid0nhLz44JnBbv5uBoY5sEDdh2SutEh70iip3-Ydn5v88OtG7g7dxk4MrA6uvxH-e9QXdsLsedyGMeGAM9plt0q366dJXXbnIjvsdYU9tQEA4tXs2EGhayImr26dDudAATUw2JNN1HA91lwSwLhWVQ_rINO0WImwqWgjW6txXrGqaVTzsbRhj4HglS22a6EDss8fSLvf6Zkhr_bOMBo4yTQ4RkQTlMQBC7ogRchvVlbntUHVPNOnQLLCiv3wa4C1HoRHyeLDh2vJrdXw5NI28LqR2EtLr-yJ-c3EtJODB6ASMEpM_oSP6uWCtW_UA9pJwFy6GKRPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
گوشه‌ای از سخنان وایرال شده خرازی، برادرزن مسعود خامنه‌ای:
جمهوری اسلامی یه موشکی به اسم «رستاخیز» داره که میتونه یه دور کامل دور زمین بچرخه و به راحتی خاک آمریکا رو بزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69774" target="_blank">📅 11:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69773">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0189fef147.mp4?token=qy2Q8O2MQ8zMD3rET7DsFch6MfGG54wTQhuCkB2Mpo8Hlse6h50qK9J2JGYjj_1Hq4sZixwBMNVQv84xPM7BJ4G2b8DO3AngcDjo2-4QKab8czDYxXs48eUGvKwNORv1yKEOQpGnbsvznNCRN2RKx83kLpITnSfTlCkqk0gWneroKqG2a8VTMLbpixQzvK3m8lhDcxtyYz5o6YrjNMh1lk0Wbdazyn7UgA0oBepAyryze4bi1z9YuHrGUB2vGwmLLIrbkQvjzibH8Ps_2-Xd-smkRAM2PiyePD9xtdr5URKbX7dHrqWIoD3nQKs7RQe-mJzzjiLYOJ39rmnOhyvrG2jupFZPWzsJq0oUTlXiUt1Qi29UzZosfOGnl7rCIiBPcpDYLLELAuZzKueiQUrqkbRwsHBgD9CkYZnyV8JgTpPCD4Rtwbf-RMb71riuCu1w3zJ5jVr-oezpfLreAlIH2KBqc1E4A211H53HZVihN5zQ3l1i6TY2vuQrKajhIrxgIUahig5XcpWXukPVeoZrxEVKjWZTUa7sEVwMEvp_DQDqJxmqAAwQGC389ILRJQ8P1hy4x3VCh3XQ4TSiJ9jiIy-C578Cg9Piw8DXDyBAxVRud6NyDuYjUinKGnb5FrSo4iCvEXyyZZv6_n_69xQPyJyHI4W2scCG_VwRkuXUVhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0189fef147.mp4?token=qy2Q8O2MQ8zMD3rET7DsFch6MfGG54wTQhuCkB2Mpo8Hlse6h50qK9J2JGYjj_1Hq4sZixwBMNVQv84xPM7BJ4G2b8DO3AngcDjo2-4QKab8czDYxXs48eUGvKwNORv1yKEOQpGnbsvznNCRN2RKx83kLpITnSfTlCkqk0gWneroKqG2a8VTMLbpixQzvK3m8lhDcxtyYz5o6YrjNMh1lk0Wbdazyn7UgA0oBepAyryze4bi1z9YuHrGUB2vGwmLLIrbkQvjzibH8Ps_2-Xd-smkRAM2PiyePD9xtdr5URKbX7dHrqWIoD3nQKs7RQe-mJzzjiLYOJ39rmnOhyvrG2jupFZPWzsJq0oUTlXiUt1Qi29UzZosfOGnl7rCIiBPcpDYLLELAuZzKueiQUrqkbRwsHBgD9CkYZnyV8JgTpPCD4Rtwbf-RMb71riuCu1w3zJ5jVr-oezpfLreAlIH2KBqc1E4A211H53HZVihN5zQ3l1i6TY2vuQrKajhIrxgIUahig5XcpWXukPVeoZrxEVKjWZTUa7sEVwMEvp_DQDqJxmqAAwQGC389ILRJQ8P1hy4x3VCh3XQ4TSiJ9jiIy-C578Cg9Piw8DXDyBAxVRud6NyDuYjUinKGnb5FrSo4iCvEXyyZZv6_n_69xQPyJyHI4W2scCG_VwRkuXUVhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بابای این دختره چون دخترش توی امتحان گواهینامه قبول شده براش BMW 225 خریده ناقابل ۱۲ میلیارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69773" target="_blank">📅 11:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69772">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/973161bf95.mp4?token=N4fOvLI1gPwjsHi4CjCLBAMaka9OhJXeDwbBpEsa4DZh1c1JQjSMWp3EDaNecVG8vBiARuSb9M_jc4JnYvoQVAyTj0CkneiyrtPcD8cXrhgtHBHYd3aU3RX4RomgyvSIFTIg6_U9TAMNAIdxBCWTC5IS-DJcJgkg9_O28GVYbMvWkDaSgIPcmLwK6PsvY5-8TFv7OZx15AJdcDcQ9Ciib6DQUyOl4ZPktd4PfcMoUaZcclatMp5NVBGCdkNAVTVq-33LGjvNAyl9y4FnX7PSWAcf_F79BFRINukiFCDVlQ4DPJwz_5iFRM7AuCsgRTg7kgZnA9Ob39TNfStu8OiMag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/973161bf95.mp4?token=N4fOvLI1gPwjsHi4CjCLBAMaka9OhJXeDwbBpEsa4DZh1c1JQjSMWp3EDaNecVG8vBiARuSb9M_jc4JnYvoQVAyTj0CkneiyrtPcD8cXrhgtHBHYd3aU3RX4RomgyvSIFTIg6_U9TAMNAIdxBCWTC5IS-DJcJgkg9_O28GVYbMvWkDaSgIPcmLwK6PsvY5-8TFv7OZx15AJdcDcQ9Ciib6DQUyOl4ZPktd4PfcMoUaZcclatMp5NVBGCdkNAVTVq-33LGjvNAyl9y4FnX7PSWAcf_F79BFRINukiFCDVlQ4DPJwz_5iFRM7AuCsgRTg7kgZnA9Ob39TNfStu8OiMag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
علی مطهری، نایب‌رئیس پیشین مجلس شورای اسلامی:
از همان ابتدا، هدف ما ساخت بمب‌های هسته‌ای بود و باید تا پایان ادامه می‌دادیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69772" target="_blank">📅 10:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69768">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c32fad0f32.mp4?token=iju0PNvwMvXjNXzE3MarDfh45PdcaePZ_b1inyOgUGZefNJvrl4qgpbh30ZoQ7o7xwfVdHf6_yLkbLCBZHP3zCk62G4jh0_eVIOUanTroP9Ky54nah1Ip10NCSA5maCMIjpGly3Le27ujATSQcTTEnRjxKfTJDKL8fMwruS1LcB3gXpPdZhYw_v15ToCtoOK6EDtJd3z0jMaeX-rXrlNUlBZFNP2BPGFXkzlYAeHghioyhd8HQ6T-j_er93_UVdkbqk2A-AnfXs5juMfsdI70ep5aXZoqx8FHWoDMDPgrpZfM8TB6rb7aDQHWInD9FoLlVm7FzKGYCkvfe0Eb61_JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c32fad0f32.mp4?token=iju0PNvwMvXjNXzE3MarDfh45PdcaePZ_b1inyOgUGZefNJvrl4qgpbh30ZoQ7o7xwfVdHf6_yLkbLCBZHP3zCk62G4jh0_eVIOUanTroP9Ky54nah1Ip10NCSA5maCMIjpGly3Le27ujATSQcTTEnRjxKfTJDKL8fMwruS1LcB3gXpPdZhYw_v15ToCtoOK6EDtJd3z0jMaeX-rXrlNUlBZFNP2BPGFXkzlYAeHghioyhd8HQ6T-j_er93_UVdkbqk2A-AnfXs5juMfsdI70ep5aXZoqx8FHWoDMDPgrpZfM8TB6rb7aDQHWInD9FoLlVm7FzKGYCkvfe0Eb61_JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ایشون به اسم آرش، خودشو اولین:
همجنس‌بازه، شیعه، پادشاهی خواه، دو رگه تُرک و لر معرفی کرده که پشمای همه ریخته
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69768" target="_blank">📅 10:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69767">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c02b892b.mp4?token=hgb-rvTSqx5e28xUMGdQSbYmshb_M3IRK5kAGz7uWzBKjRoFm9Cz1KSR-AdLcbNkwGJlSUiL2zjhdTW0meNrJG1z7a3gqwnRbeDwJOwQlmTCrNq9pIcgjAKqozHY0xSH9DLDdv0vWgwgQoYPeMmJKS7QEybSZOXR2OLDpeVyJUtD7CeELS2oa9YZYOHHp-xFrsD7_2nsdET9Rx3JiL8WaOcJ2x_Bd7DmGaoGnKT9dWVdn-b6B90RQsnr1CTCVn50Y1QOvY4XemkUqQtaa9IwTiFmWPxmy_iLoq3P4YfzvGrCdQ_eAyNqYg0-se_2xEyfnLF6YplywEqfCacR070jTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c02b892b.mp4?token=hgb-rvTSqx5e28xUMGdQSbYmshb_M3IRK5kAGz7uWzBKjRoFm9Cz1KSR-AdLcbNkwGJlSUiL2zjhdTW0meNrJG1z7a3gqwnRbeDwJOwQlmTCrNq9pIcgjAKqozHY0xSH9DLDdv0vWgwgQoYPeMmJKS7QEybSZOXR2OLDpeVyJUtD7CeELS2oa9YZYOHHp-xFrsD7_2nsdET9Rx3JiL8WaOcJ2x_Bd7DmGaoGnKT9dWVdn-b6B90RQsnr1CTCVn50Y1QOvY4XemkUqQtaa9IwTiFmWPxmy_iLoq3P4YfzvGrCdQ_eAyNqYg0-se_2xEyfnLF6YplywEqfCacR070jTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای یه طرفدار حکومت درباره حجاب:
آقای پزشکیان واقعا مرسی که گفتی نمیتونم قانون حجاب رو رعایت بکنم
مجلسی که ناظر هستی توام دمت گرم که اصلا فکری برا حجاب نمیکنی
پزشکیان داره میگه ععععععع مگه هنوزم گشت ارشاد هست؟؟
بحث دیگه حجاب نیست بحث پوششه پوشش و اصالت ما داره از بین میره
تو خود اروپا هم قانونی برا پوشش هست نه اینکه لخت بریزن خیابون
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69767" target="_blank">📅 09:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69766">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed36a1671.mp4?token=Z0XuYhQfrRYTsHL2FphaKwrcNA_4zN37q3jsJhLIM39NZQYnbnRZme55Cj6U_bjIwh0QPVT1i4kaiWREDueyrg0tYRpQiS_H2lZRdy2m8JNhdhDwvHdXbxdS8FW5Zx-yrtZZEiuznmchGEl7vcPxoEElXtFiOja2XjgEh-tNZIH97GULs-pxXhKHXetrLt_76QmIVAuDoQFvzDCGwD5ZqRUEGpjH7uZ92GDu2jlfjEoCiL9Olt5MItKB7Fi2aMjwfhNXMG-h0f-slW5AjYIjLU4vP3ZilQQXQX3m4yNGbY7UApLm9yAvltj76LC0VPQs3YpSw4ufG_OGUE5rGA6dyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed36a1671.mp4?token=Z0XuYhQfrRYTsHL2FphaKwrcNA_4zN37q3jsJhLIM39NZQYnbnRZme55Cj6U_bjIwh0QPVT1i4kaiWREDueyrg0tYRpQiS_H2lZRdy2m8JNhdhDwvHdXbxdS8FW5Zx-yrtZZEiuznmchGEl7vcPxoEElXtFiOja2XjgEh-tNZIH97GULs-pxXhKHXetrLt_76QmIVAuDoQFvzDCGwD5ZqRUEGpjH7uZ92GDu2jlfjEoCiL9Olt5MItKB7Fi2aMjwfhNXMG-h0f-slW5AjYIjLU4vP3ZilQQXQX3m4yNGbY7UApLm9yAvltj76LC0VPQs3YpSw4ufG_OGUE5rGA6dyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدیو وایرال شده از فردی که در زمان رفراندوم سال 57 حضور داشته
:
وقتی من روز رفراندوم رفتم بیرون و دیدم گفتن ۲۰ میلیون نفر رای دادن زنگ زدن آدما بهم گفتن بیا ببین چخبره.
اونجا رئیس حوزه آخوند بود و این بیجک های صدتایی رو میدادن دست مردم میگفتن بنداز صندوق بگو مرگ بر شاه.
جمعیت ایران اون زمان ۳۷ میلیون و ۲۰۰ هزار نفر بود.
کل کسانی که بالای ۱۶ سال بودنو و میتونستن رای بدن ۱۸ میلیون و ۷۳۲ هزار نفر بود.
آمار رو با خنده اعلام کردن ۳۰ میلیون نفر رای دادن.
توی وزارت کشور گفتن که اینطور نمیشه پس گفتن ۲۲ میلیون و ۴۰۰ هزار نفر رای دادن و ۲۰ میلیون و ۴۰۰ هزار نفر به جمهوری اسلامی بله گفتن.
اینو حساب کنید دیگه از کل ۱۸ میلیون نفر واجد شرایط مخالف بود مریض بود زندانی بود و.... از اینجا بود که من راهمو از اینا جدا کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69766" target="_blank">📅 08:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69765">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-release.apk</div>
  <div class="tg-doc-extra">4.5 MB</div>
</div>
<a href="https://t.me/news_hut/69765" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎲
همین امشب با اولین شارژ
🤩
🤩
🤩
درصد شارژ بیشتر بگیر
همین الان شانست رو با موجودی اضافی امتحان کن حتما بزنده میشی
👌
👇🏻
👇🏻
🌐
Telegram
🎲
🌐
winro.io
🎲</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69765" target="_blank">📅 01:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69764">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-Wfh5ZnAEiuj3eWixT78N8HLL07DH638eXHFNT2jjEH_OoqISaJmuC1R3ZND3n95NNC_GSRsCB2qvb473cUc060aEFsLR6v8Q2_2UhmyfvxRdW78KCr1k_AeHwJT7WRNqoMofOU5SB4KT1DG6aG5b_gzUOjn58Wno91pxp4RQTngRlFi47pYjZh78JCTP2r44F5WubqxNznZV0x_W6_nRVSxPCRl2ReiEpi783U7lJxIJrUtXElW2-ZE_1mvALNaFcSvxeFUjABA7Tbz-OnJQJWsWmSzb7UH2_1AN2SOHfptszHZYzrVpho5ZnZ3nxCyFbrdatOuMo1sXSS4w6kVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
همین حالا موجودیتو
🤩
برابر کن
❌
☑️
۲/۵ میلیون شارژ کن ۱۰ میلیون شارژ شو
✅
برای اولین واریز تا 15 شهریور ،
0️⃣
0️⃣
3️⃣
درصد بیشتر در وینرو شارژ شو
🎁
✅
به ازای هر واریز در وینرو به ترتیب 300 ، 150 ، 75 درصد بیشتر شارژ شوید
.
🔊
با شارژ اضافی بدون ریسک بازی کن سرمایتو چند برابر کن
⚡️
🎲
ثبت نام آسان و سریع کلیک کنید
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا a17
🌟
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69764" target="_blank">📅 01:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69763">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20cf5580ad.mp4?token=DYnMkolRwSnapisZ2usT0a2u7dJ8x2CzscPkv68tjMr4wWxVKN0a375autt-Pi7EIk7-EJ2uPVgxbsdXY-wdaBjzmyaGjkZ-IH_4L6tUGzVxXFCjLiew42tGCFFYLoFhL7j4ejPj7pWPYIVYwSx-qNISQZw78BXw0634httz_utMDq-WFIdczQv6JfVmhKTUZ0XoFRvL6689V3oWPutMX4-F1xbKWQVpsf2MVuqjIOPCVB8AQY4wAkinH_B6CAb7qvlKM9HtLZfgJvmt4MMG0Gm1jui1SYaVvLRi2Pk0fiKj93weW5OhC0IboBWmeJpSpm6KkHZVH-yZf1omKu0L-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20cf5580ad.mp4?token=DYnMkolRwSnapisZ2usT0a2u7dJ8x2CzscPkv68tjMr4wWxVKN0a375autt-Pi7EIk7-EJ2uPVgxbsdXY-wdaBjzmyaGjkZ-IH_4L6tUGzVxXFCjLiew42tGCFFYLoFhL7j4ejPj7pWPYIVYwSx-qNISQZw78BXw0634httz_utMDq-WFIdczQv6JfVmhKTUZ0XoFRvL6689V3oWPutMX4-F1xbKWQVpsf2MVuqjIOPCVB8AQY4wAkinH_B6CAb7qvlKM9HtLZfgJvmt4MMG0Gm1jui1SYaVvLRi2Pk0fiKj93weW5OhC0IboBWmeJpSpm6KkHZVH-yZf1omKu0L-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
سربازان روس با تفنگ موفق شدند پهباد اوکراینی رو سرنگون کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69763" target="_blank">📅 01:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69762">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
‼️
حمیدرضا رجب زاده یکی از مداح های حکومتی بوده که چند هفته پیش به قتل می‌رسه، حالا یه کانال تلگرامی مدعی شده اونا این قتل رو انجام دادن دلیلشون هم اینه بوده که این مداح تو دی‌ماه جز نیرو های سرکوبگر بوده و به سمت مردم تیر می‌زده  ویدیوی قتل که قلبشو از سینش…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69762" target="_blank">📅 00:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69760">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B38ex_-h0oEbP5etrbCacygtFVZiPLjT_kwx68P2HhPymgBeRu5ezfvY-TsjVDWiFu0zfOPLHFZKhbxYGOE8uPS_epJHgAvbUPmjM2cXR79bCe2GAfPBuDfUvN8wafngy_khE64PJK1mMc48qA56DVs0hNvsXuS-71ufeEB-yPaHrwVyLRwnceKyzfc_WjDzH5UcqlN1PEQ1JxKHKEZ0o6IQsl7OmQOQaVVmBwYuvWUtWS2jiaz--3rg5GKzFqcnx2zVRq-uuAtn4MxFtgUIR4liQTla5ryZ1sF6w1VaQpNbH8YETfOypXMc46wcjmdk8aEA1b45JuHiCcpjFyR58A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5e8a9ce1b.mp4?token=iMUUDRpXhuV0_G-GGaBoT_57osZATBCthzwkaeq5pNLwcItJBrz8_XoBucUKU3YNtp_MtRno0ogtHu9I-M0k4n5esSz_oQ2fJK4R-DRAXQezJuDk0CYDShyM4FJ6Lnghj2Rw2Kc2Xxc3qamrrCMe5SYx9WcNHdmZPlJICpK8y329OpT6q3MLWmnD6ApdNA5bgBzLKxgies3W9EVnPacoiEkmR2kouEulBENFxEObsNH0M7zMlneWelaVDgKj5AMneXmcWTPcEU18gpLsSw_6-YhLtYlm-4PoL1FFKMeszShqQz-rQBxyCWvkebYWMsmNhW7IXnh9fZa12WRmFah98Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5e8a9ce1b.mp4?token=iMUUDRpXhuV0_G-GGaBoT_57osZATBCthzwkaeq5pNLwcItJBrz8_XoBucUKU3YNtp_MtRno0ogtHu9I-M0k4n5esSz_oQ2fJK4R-DRAXQezJuDk0CYDShyM4FJ6Lnghj2Rw2Kc2Xxc3qamrrCMe5SYx9WcNHdmZPlJICpK8y329OpT6q3MLWmnD6ApdNA5bgBzLKxgies3W9EVnPacoiEkmR2kouEulBENFxEObsNH0M7zMlneWelaVDgKj5AMneXmcWTPcEU18gpLsSw_6-YhLtYlm-4PoL1FFKMeszShqQz-rQBxyCWvkebYWMsmNhW7IXnh9fZa12WRmFah98Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمیدرضا رجب زاده یکی از مداح های حکومتی بوده که چند هفته پیش به قتل می‌رسه، حالا یه کانال تلگرامی مدعی شده اونا این قتل رو انجام دادن دلیلشون هم اینه بوده که این مداح تو دی‌ماه جز نیرو های سرکوبگر بوده و به سمت مردم تیر می‌زده
ویدیوی قتل که قلبشو از سینش در میارن و رو صورتش خودارضایی می‌کنند رو هم منتشر کردند و بعد برای خونوادش فرستادن؛ چند ساعت پیش هم اعلام شد که قاتلین دستگیر شدند
🔞
مشاهده‌ی ویدیوی اول
⚠️
⚠️
مشاهده‌ی ویدیوی دوم
🔞
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69760" target="_blank">📅 00:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69758">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a034d8d108.mp4?token=tNi9d6uw9XCQRjJZqh9bjyttqQGOSK43K4BpwPh2ctOpxdvP9GPsXw4tllZGkja4h6Q7CqICWZV0R6MMjmJO-qHY_SzDR4ruyuFshPzfOtkxQz7UFHBa_fgOo-j3IfLVZm3vkEeqx3ARorGNAVT9y_9zvG6Jt0tytQoyNcttWDk3hfqb8jrgP4Sr6Zj8xJPLqND2CoLtombm9mDBqgECltGdSO4N0gYoYS_Bjg3m3ymG3SokFYACmLdhnjAgayqZAxg4WGO1FgOnXa9AXOeiDfEJHllwHtc08ZYYYs-5Io7XlNtgvAHyCLbe_qlg4alhcNqQi5MOOgMIa6Lt_zDyoJ7iubGv0az9qq9zwYQH9wXmfQaEA1NpByngd66xKw1jhEgkO1Vx0YBsbgcS5F36b8E_MMeZPgL-18IkgbDhiXXcMRv5M-FUa9MqAjkkpZEoS-Hx5BYbKRbv59R4oYbis4wTYn1fFUkTV82OF760fmlnhv10ZF25MuP1nn6bfpUUVHgXbqStlF5w5G_ckam6QYmG3qdB0BL-lsIvQHNxBwNMvcbubQMQi4EffByWs-JVB4ueMZPdZLheKjtto_Lu0BWzguNNnYZc6zkUd1JfFdMhVL7Nbmra6IXrRVwq7MADlETqK38SNLOsWDqFfmJ8FH9mlnZGuiWfB1VrQ6P4MHk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a034d8d108.mp4?token=tNi9d6uw9XCQRjJZqh9bjyttqQGOSK43K4BpwPh2ctOpxdvP9GPsXw4tllZGkja4h6Q7CqICWZV0R6MMjmJO-qHY_SzDR4ruyuFshPzfOtkxQz7UFHBa_fgOo-j3IfLVZm3vkEeqx3ARorGNAVT9y_9zvG6Jt0tytQoyNcttWDk3hfqb8jrgP4Sr6Zj8xJPLqND2CoLtombm9mDBqgECltGdSO4N0gYoYS_Bjg3m3ymG3SokFYACmLdhnjAgayqZAxg4WGO1FgOnXa9AXOeiDfEJHllwHtc08ZYYYs-5Io7XlNtgvAHyCLbe_qlg4alhcNqQi5MOOgMIa6Lt_zDyoJ7iubGv0az9qq9zwYQH9wXmfQaEA1NpByngd66xKw1jhEgkO1Vx0YBsbgcS5F36b8E_MMeZPgL-18IkgbDhiXXcMRv5M-FUa9MqAjkkpZEoS-Hx5BYbKRbv59R4oYbis4wTYn1fFUkTV82OF760fmlnhv10ZF25MuP1nn6bfpUUVHgXbqStlF5w5G_ckam6QYmG3qdB0BL-lsIvQHNxBwNMvcbubQMQi4EffByWs-JVB4ueMZPdZLheKjtto_Lu0BWzguNNnYZc6zkUd1JfFdMhVL7Nbmra6IXrRVwq7MADlETqK38SNLOsWDqFfmJ8FH9mlnZGuiWfB1VrQ6P4MHk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو این مملکت اگه پول داشته باشی، حتی کمپ ترک اعتیاد هم می‌تونه شبیه هتل چندستاره باشه!
● بعضی کمپ‌های لاکچری خدماتی مثل:
🍽️
غذای رستورانی
🏊
استخر، سونا و جکوزی
🎱
بیلیارد و پلی‌استیشن
👨‍⚕️
پزشک عمومی و روانشناس
📱
موبایل و لپ‌تاپ آزاد
🛏️
اتاق‌های VIP
ارائه میدن؛جایی که دیگه از کمپ های معمولی خیلی فاصله گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69758" target="_blank">📅 23:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69757">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a2b2f82e.mov?token=YcTlSxjjFbjLDDUP5rmC1OHw0tSfnluNJ6cdX8ssk6JdiIM_iE204NxGJt3gugsrWZE3BAAd4YFMB3HrXkzGJq5lxt9y2QP5SbCq_X_l3_6VewUhLbEiTLCXx9HjyjS_IdacHGAWqCJStkiQt9Hn2otVRGTkqC1aH5Wi8qgHmRk6nEN2rvOw8xUbN0R_gPM-HQbmycFjvbZO1-QDQdQF14MNaSrS5mMidFBUu6a7AMusEL17-MH2gA2fgUfqwjZvn0SvcCmpcYNsUKngnC-QgJhFAmpkL10tD5T0fX0PN5Ny2GDcCQdGiYyUF9GpmJ2BUpJ1b3hJtyJZFi8NPYpn-C-_HtudC_k_DWkJBle5PSbdh34iYZXR3VcOFL9HW3y3dB-Vz2WZ2ciEymeIRwi9ethiXEUBG-nN6hlhgSHh8igyg6l-_35F1cq1K6VmuXOTFqxke0CCL_TUc37Lej0cMeWxUAiNXeP72cpdEcdm4Ea_nSQudZna36BQ82mXYpNW2kubdI1RAlO0JbHbKX60qIYDpVfOlI0FT1nYKj3ZjdLcg_ERq4TxG9T6cyG0ergB7Kw86LQrTLriABS3gPZHv15l97Ab7PZs1GwG_ctQ8sGs2dFjzdFAXHouIff-zMti3wW8FynEXN3N1dRslzoklPlIpU4qD1a57MS-0tdjzyI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a2b2f82e.mov?token=YcTlSxjjFbjLDDUP5rmC1OHw0tSfnluNJ6cdX8ssk6JdiIM_iE204NxGJt3gugsrWZE3BAAd4YFMB3HrXkzGJq5lxt9y2QP5SbCq_X_l3_6VewUhLbEiTLCXx9HjyjS_IdacHGAWqCJStkiQt9Hn2otVRGTkqC1aH5Wi8qgHmRk6nEN2rvOw8xUbN0R_gPM-HQbmycFjvbZO1-QDQdQF14MNaSrS5mMidFBUu6a7AMusEL17-MH2gA2fgUfqwjZvn0SvcCmpcYNsUKngnC-QgJhFAmpkL10tD5T0fX0PN5Ny2GDcCQdGiYyUF9GpmJ2BUpJ1b3hJtyJZFi8NPYpn-C-_HtudC_k_DWkJBle5PSbdh34iYZXR3VcOFL9HW3y3dB-Vz2WZ2ciEymeIRwi9ethiXEUBG-nN6hlhgSHh8igyg6l-_35F1cq1K6VmuXOTFqxke0CCL_TUc37Lej0cMeWxUAiNXeP72cpdEcdm4Ea_nSQudZna36BQ82mXYpNW2kubdI1RAlO0JbHbKX60qIYDpVfOlI0FT1nYKj3ZjdLcg_ERq4TxG9T6cyG0ergB7Kw86LQrTLriABS3gPZHv15l97Ab7PZs1GwG_ctQ8sGs2dFjzdFAXHouIff-zMti3wW8FynEXN3N1dRslzoklPlIpU4qD1a57MS-0tdjzyI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
نیروهای روسی به هدف قرار دادن تدارکات اوکراین ادامه می‌دهند و یک لوکوموتیو دیگر را در نزدیکی ایستگاه راه‌آهن «لوزووا» در استان خارکیف منهدم کردند؛
منطقه‌ای که یک کانون کلیدی برای کی‌یف جهت انتقال تجهیزات نظامی و نیروهای کمکی به سمت دونباس محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69757" target="_blank">📅 22:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69756">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da63e2e1aa.mp4?token=oi--zJ49ckVEIT6w-JFwJxU8Q3P6P7g8GHcK1e_PVwrb9lro5EBR97qpiXDDzE09mvV2u8-U1_vf8d_Ex5HpUdofMkNKJqHsgxb5hNfawqVzSAxVnTuOZ3AC5PIk7FElwXfG28HnhoSsuhhtvBq74s68p4CpKRvkkkO_iddrn-YMCeoTZnicMx7xdWoKjEhfpfVNgjMQ8hCTZ-eFZ9KIDJY1hyTNHHO6mGy2Qrn_t-5cCVcylyp82MMC9F4KYjuCGr3HEJgWqRw7EPRCiW9IJVYO_wF8UTC-CszR-3puXVHRPSm8o4C1wApx41fUtJKqv50MwgPRKB_yGvJxjBxNkHIC-971ZviJpHzfwsZ6a08hfFGR16scKdL3jR8VJrAysilQ_6oB7SGFCkZnDTO6XQuPa77vdcnuFCqETvo9G98057XrxXBx1XiYRFkAezRm0p74kJjfq7WO9Ys_YdRBaEuP2eN3rFRBCd9V6ThX1R-8hLn7MaPvTj5MbFaquoocqRXaKwNCcwmX6YmmZVQH5oVItIv3PYu40eIepKhxb3DugkTl8aafWQh63b0H_D7p4nBimp5Utg9l6ARqzx8Im4xdJRNtpw8cmKacpPEv9jWYeljQe5094waJhaSjzofHeszVgc9hScvshxjHwYr-xLteyQz8MF0_bvExP1vwywA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da63e2e1aa.mp4?token=oi--zJ49ckVEIT6w-JFwJxU8Q3P6P7g8GHcK1e_PVwrb9lro5EBR97qpiXDDzE09mvV2u8-U1_vf8d_Ex5HpUdofMkNKJqHsgxb5hNfawqVzSAxVnTuOZ3AC5PIk7FElwXfG28HnhoSsuhhtvBq74s68p4CpKRvkkkO_iddrn-YMCeoTZnicMx7xdWoKjEhfpfVNgjMQ8hCTZ-eFZ9KIDJY1hyTNHHO6mGy2Qrn_t-5cCVcylyp82MMC9F4KYjuCGr3HEJgWqRw7EPRCiW9IJVYO_wF8UTC-CszR-3puXVHRPSm8o4C1wApx41fUtJKqv50MwgPRKB_yGvJxjBxNkHIC-971ZviJpHzfwsZ6a08hfFGR16scKdL3jR8VJrAysilQ_6oB7SGFCkZnDTO6XQuPa77vdcnuFCqETvo9G98057XrxXBx1XiYRFkAezRm0p74kJjfq7WO9Ys_YdRBaEuP2eN3rFRBCd9V6ThX1R-8hLn7MaPvTj5MbFaquoocqRXaKwNCcwmX6YmmZVQH5oVItIv3PYu40eIepKhxb3DugkTl8aafWQh63b0H_D7p4nBimp5Utg9l6ARqzx8Im4xdJRNtpw8cmKacpPEv9jWYeljQe5094waJhaSjzofHeszVgc9hScvshxjHwYr-xLteyQz8MF0_bvExP1vwywA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از مردم پرسیدن "چه فکریه که نمیذاره شب‌ها بخوابین؟"جواب‌هایی که دادن جالب و دردناک بود؛
میدونم پول دار شدن زمان‌بره ، ولی خب به این فکر میکنم که مامانم داره پیر میشه...
من چی کم داشتم که بهم خیانت کرد؟
برادرم که فوت شده، هنوز مراقبمه یا نه؟ دوسم داره یا اینکه واقعا ولم کرده؟
اینکه الان من بهش دارم فکر میکنم، اون داره به کی فکر میکنه؟
یه دختری هست که میخوام خوشبختش کنم، امیدوارم لیاقتشو داشته باشم..
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69756" target="_blank">📅 22:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69755">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⏺
ژنرال برد کوپر، فرمانده فرماندهی مرکزی ایالات متحده، در اسرائیل فرود آمد تا جلساتی را با ژنرال زمیر، رئیس ستاد، و مقامات ارشد نظامی اسرائیل برگزار کند. این مقام آمریکایی پس از برگزاری جلساتی در بحرین و امارات متحده عربی، به اسرائیل سفر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69755" target="_blank">📅 21:19 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69754">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11c35a859.mp4?token=AEQY9YTsDVb4IwuM9ND6Rd0VVryb0Pxsnti9UHgdv695MaAlWaGAqLVaPoK273lA-IBOC2R0uZV-0dUIf5iBM0hxMjAGjgSbqtKM94zxR1tKrtMnQmKn1OIXuC4YfhsmH8wYNgtKXEhd-dSob4uBz7pQln9OwrX5Hp-tClZmQ6eshsEEpxji6rZJT9rtcvPSVi2z_eQ_p7gX5q1Ghszy34o3Qc4jH5TGvJIjfmkub9gD_M3I1Xo-chL6fsPuO9A9syqyebQXoWiWPhxC11_JlYBd5TBomu1qNneBmOlTYof7nNnVCHlQmAcv_2kVZC5VLFaELGyumqcvCLi6A9MzYEZqLYELAcFUCqZi3DfAdtg5JemzQ4qOE0oo13M2BE9FX_rF5Fyx6czL4jTFW3PL0o0TM5tBjVAti5Hzc018oOjoa-3k4RGBnRjxMv18hYBKj_wJ4VBQ3EpqJUB4NcDnHttryGenrEPCqpMyXCv_9d_EkbapPlwSAELa0oBeHu9EKH62jKLpihmCtBkmBfk5L8Fs-IYnbQMdmKhzoJUWNxi0dryJvNSlsuSlZEfmZa-c5oF6dVDGcqasMHS6D3S_fez17bUYFIIm29wJYmdWkeUchg5fS1bMf6-rn4WvcKNqHnRHkfuBO8JyyAFqEtOTviL2cHeBEnev59rjBPCo38M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11c35a859.mp4?token=AEQY9YTsDVb4IwuM9ND6Rd0VVryb0Pxsnti9UHgdv695MaAlWaGAqLVaPoK273lA-IBOC2R0uZV-0dUIf5iBM0hxMjAGjgSbqtKM94zxR1tKrtMnQmKn1OIXuC4YfhsmH8wYNgtKXEhd-dSob4uBz7pQln9OwrX5Hp-tClZmQ6eshsEEpxji6rZJT9rtcvPSVi2z_eQ_p7gX5q1Ghszy34o3Qc4jH5TGvJIjfmkub9gD_M3I1Xo-chL6fsPuO9A9syqyebQXoWiWPhxC11_JlYBd5TBomu1qNneBmOlTYof7nNnVCHlQmAcv_2kVZC5VLFaELGyumqcvCLi6A9MzYEZqLYELAcFUCqZi3DfAdtg5JemzQ4qOE0oo13M2BE9FX_rF5Fyx6czL4jTFW3PL0o0TM5tBjVAti5Hzc018oOjoa-3k4RGBnRjxMv18hYBKj_wJ4VBQ3EpqJUB4NcDnHttryGenrEPCqpMyXCv_9d_EkbapPlwSAELa0oBeHu9EKH62jKLpihmCtBkmBfk5L8Fs-IYnbQMdmKhzoJUWNxi0dryJvNSlsuSlZEfmZa-c5oF6dVDGcqasMHS6D3S_fez17bUYFIIm29wJYmdWkeUchg5fS1bMf6-rn4WvcKNqHnRHkfuBO8JyyAFqEtOTviL2cHeBEnev59rjBPCo38M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
شاهنشاه آریامهر: اون روز دیگه من نیستم ولی حقیقت هست
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69754" target="_blank">📅 21:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69753">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FeNv4w_pwYOYrJV_9Cbl91_oLCYi6v6YFCrgO-FMrDLvKTDF7MITYV5Te4evIWnLMHIAWAyMnFDKHFvFbdk3W74EApKYkxsAZKr8SJVPAZorsDAI8jXqhzvjebt3ToabSTNOmng-YtKwuFP-5rwAUrgXJH37bjxgHpSed_Qjfn5JkFf5j75k7ybDA_w5xMe4e4fF_VxoZGEnkgC-CULp0BgKWUSTpt77DG3EydCyhLUGaI6WAWBcroDAMuhRECGEzIl8jzl-iLMEKmV0mNt59lDyF6SN8YIj9Es7u9flqV44SL2cr6yfPWKCMEIS7lM4lLAuCEzTlHLMi5bC5Tniow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کانال ۱۳ اسرائیل:
اسرائیل خود را برای احتمال اقدام یک‌جانبه علیه ایران آماده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69753" target="_blank">📅 20:56 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69752">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1727b3200.mp4?token=X4mujCq12u1Fc9w_f9l9qUVWTx7bE87ZCRWsLvMXqIYFaeL2AZlAP-rlduIjlCrtdls4aoV3d_f1OcHslHXry3geQPLuh7O93mLb8JEgluXrujyuFjbct0yEl0vE3cWECcAtvA1mHqG3WvZgRXZr0GPBqHMOc4NdSrQvJ0S51qI4D3E9L_0e6kjEjVOy1IqOrXpmRtBfXkXzJy3vC1rDTxgTdPvkU8rXIeQp6qiZK9w4LrB8ChdxPE2UjduaEFeRXDJ-8qeDJI8nb896yh_RImexxndNOnWJNa-n7I_HFKQv_jR59Q_VBbC9WIiY_L6vcn3hLWXz5GalqawygpLDLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1727b3200.mp4?token=X4mujCq12u1Fc9w_f9l9qUVWTx7bE87ZCRWsLvMXqIYFaeL2AZlAP-rlduIjlCrtdls4aoV3d_f1OcHslHXry3geQPLuh7O93mLb8JEgluXrujyuFjbct0yEl0vE3cWECcAtvA1mHqG3WvZgRXZr0GPBqHMOc4NdSrQvJ0S51qI4D3E9L_0e6kjEjVOy1IqOrXpmRtBfXkXzJy3vC1rDTxgTdPvkU8rXIeQp6qiZK9w4LrB8ChdxPE2UjduaEFeRXDJ-8qeDJI8nb896yh_RImexxndNOnWJNa-n7I_HFKQv_jR59Q_VBbC9WIiY_L6vcn3hLWXz5GalqawygpLDLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حاجی‌دلیگانی، نماینده مجلس:
قدرت چهارم جهانیم و حق وتو می‌خوایم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69752" target="_blank">📅 20:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69751">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8f98a7872.mp4?token=adQWVqfFdpYxs2O8mjOIEVFM91Z5e7Uhwi_BFky99i4ROuUzFV10SFioqZC0bknA5u1Ww9MRXcsfFVmEuB8SgmV2eCCxXG-RX6liX8RH6ekbQ3edNspQhV_SB9XJBh8-XIkCIbVrhYmicXuvKCQjM1lZSLBw8W-ROC35uqWGQcR2u9L_xy1ofySO2fUTcnmZhz7GVHcT14I3pGq8PYxbkYv-bZ4BQU74dQputjSMfnuOclQoG2xUfXt1zxwx5qKbxcSRNZhOUASljZb4Zn9_WT79To_2g7b1kMmMGOJbWiy_G3hIP4-tfvQj5HFDdf-as_-RxmXH2uFTKMAxmI39zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8f98a7872.mp4?token=adQWVqfFdpYxs2O8mjOIEVFM91Z5e7Uhwi_BFky99i4ROuUzFV10SFioqZC0bknA5u1Ww9MRXcsfFVmEuB8SgmV2eCCxXG-RX6liX8RH6ekbQ3edNspQhV_SB9XJBh8-XIkCIbVrhYmicXuvKCQjM1lZSLBw8W-ROC35uqWGQcR2u9L_xy1ofySO2fUTcnmZhz7GVHcT14I3pGq8PYxbkYv-bZ4BQU74dQputjSMfnuOclQoG2xUfXt1zxwx5qKbxcSRNZhOUASljZb4Zn9_WT79To_2g7b1kMmMGOJbWiy_G3hIP4-tfvQj5HFDdf-as_-RxmXH2uFTKMAxmI39zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
معاون رئیس جمهور آمریکا آیت‌الله جی‌دی ونس:
در کنفرانسی، لحظه‌ای پیش آمد که من و یکی از دوستانم داشتیم درباره مسیحیت و مذهب کاتولیک صحبت می‌کردیم.
درست در همان حینِ گفتگو، لیوانی از روی دیوار پایین افتاد.
می‌دانید، فکر می‌کنم یک فرد خداناباور (آتئیست) احتمالاً آن را این‌طور نادیده می‌گرفت که: «خب، چه اهمیتی دارد؟ لیوانی از روی دیوار افتاده است.»
اما در آن لحظه، احساس کردم که گویی خداوند سعی دارد پیامی برایم بفرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69751" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69750">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b83cf8ea7b.mp4?token=kAI-LtHlVSfRYQWqtiemL_z1xKVSJV5fBosOP-U_Q7Hn7rgkxHMV5tSi8kv0nNoXSO8DXZmpJPNqjKf7izdzb1oA0dUaH7z5PYgVAc-4sJd-A2qKZ_QwpnaSNmadTC2IKzHr6WtlVYH6eteaUK_onLmQYMn7Z3JDNOZqWcFS1z7AHvFtZjJKijrwmPy8i8ZKr6TSnp5o614SXQxE4gwQXifK8Fm4bAb0xLzH2FohO5MV9JNKSUorvIDRikj-PeyKUr_nApH6tu0Hprr4-dpVDei1gJ0vUUkT-DjFabPeuWa-yE34ryf9fw0KzD7ci_dVzAqiHOGmtpRFv5SS0TNOag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b83cf8ea7b.mp4?token=kAI-LtHlVSfRYQWqtiemL_z1xKVSJV5fBosOP-U_Q7Hn7rgkxHMV5tSi8kv0nNoXSO8DXZmpJPNqjKf7izdzb1oA0dUaH7z5PYgVAc-4sJd-A2qKZ_QwpnaSNmadTC2IKzHr6WtlVYH6eteaUK_onLmQYMn7Z3JDNOZqWcFS1z7AHvFtZjJKijrwmPy8i8ZKr6TSnp5o614SXQxE4gwQXifK8Fm4bAb0xLzH2FohO5MV9JNKSUorvIDRikj-PeyKUr_nApH6tu0Hprr4-dpVDei1gJ0vUUkT-DjFabPeuWa-yE34ryf9fw0KzD7ci_dVzAqiHOGmtpRFv5SS0TNOag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداوسیما تصاویر مربوط به هواگرهای آمریکایی و اسرائیلی که توسط سپاه منهدم شدن رو منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69750" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69749">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69749" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
با این سایت به راحتی میتونی کل ضرر های جام جهانی رو جبران کنی
بونوس هاش واقعا عالیه
👌🏼
بدون قیدوشرط
❌
با هر 1 میلیون شارژ ،
🤩
🤩
🤩
هزارتومان شارژ اضافی بگیر
🅰️
❌
❌
طرح شارژ رایگان فقط تا پایان مرداد ماه</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69749" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69748">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqxtpmUnxKVYNGd4yoJTIvfM-BZrNdAiLMB8-kLWs1Yobn7nvw45JroQ7HjtdFXvSeBsNA4RNg9NkNX-sdsXdrslO1YblHeOSLXKzI2oXkhmqwTJG4vuNXG-jPoMY4u7-q6lIAq_N2K3eWRt19V5n334AzWr4BT6HNiee3hsduFC8l8s9J6fFOcFmCIR6ehA7Eds_5rNYg5BEJfysMUbDcSz-WXy1A4_omR0ZnWRqHigr6wq43BdNld4VogeZyMNrJvDWAroILe6OwnbJV4PUQazJGuXLey-Xc72Imu8aYC9HCNogbDH4aal6I19J_Jlrp35uqiaXH_xrdiXAvmU_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛍
#اتلتیکو
Vs
#منچستر_سیتی
💰
🛍
#لیورپول
Vs
#موناکو
💰
زمان: یکشنبه ساعت ۱۴
🚨
تجربه پیشبینی مطمئن با
🤩
🤩
🅰️
شارژ اضافی و ریسک خیلی پایین در
#بت_اینجا
رو از دست نده
❌
🤩
🤩
درصد برگشت وجه در  صورت باخت:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g17
@betinjabet</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69748" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69747">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_Hy7dJ1KsRDZCTEokjWEuIPhVaP2ptygdMmJC2r15IEmlhCQaJBX2QDT6rrATWUnhuU0zrbFMFjYPAEFV5H6lhoRYtbEauqtb1L271HFXDdv33_wdRLxMMwdfsuhcxP_3480AfH_HBisnErRgLBq6pOwucl2usDw_peXoYrVp5i11MVg-c1dQMW0TxK75Dr6Pbg3jscO1zKpUr7v-nxQPNWZv99w0aPjaK77wcHKp9422o49wiJB6jiofrGrmO5HlkrAv9Pcv5E067NoPsCQKOBc6NGnBLvwsES-vIs-h98K0rEuiLhbdeRBfg4-LQYduX0RW32Bb7QRZ4_k7RPMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
بیانیه دبیرخانه شورای عالی امنیت ملی:
🔴
اگر ایالات متحده رفتار خود را اصلاح نکند، تنگه هرمز باز نخواهد شد.
اصلاح رفتار به معنای موارد زیر است:
عدم تهدید ایران به هیچ شکلی و به هیچ زبانی، و عدم توهین به مقدسات مردم ایران.
پایان دادن به جنگ و تجاوز علیه ایران و متحدان آن در لبنان، فلسطین، یمن و عراق، برای همیشه.
رفع محاصره دریایی و عقب‌نشینی نیروهای نظامی دریایی و هوایی از اطراف ایران.
پرداخت کامل غرامت خسارات وارده از دو جنگ تجاوزکارانه علیه ایران.
رفع تحریم‌های ظالمانه و غیرقانونی اعمال شده بر مردم ایران.
آزادسازی بدون قید و شرط وجوه مسدود شده و ضبط شده متعلق به مردم ایران.
🔴
اینها مطالبات مردم ایران هستند که در طول ۱۶۰ روز حضور مستمر در میدان‌های جنگ و خیابان‌ها، فریاد زده‌اند.
شورای عالی امنیت ملی هرگز عقب‌نشینی نخواهد کرد، نه در جنگ و نه در مذاکرات.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69747" target="_blank">📅 19:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69746">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YK-9173oSAPB9QoO6nzHaGxG_PqvXxLlLdcOOYUlPEKBREWEOftpCJfj9dZxtmMhB-cf2ZtcgsxiDiE9-wYCLRdCiP_q_yzMSxviSW8Sp_i5BCZzXs8cCccGr54F-ENZ2mtQoTvol2yyr5kZnJFBG5k2Qdw17_qEeAnlhsHIAMVKxl8t7agF3xt67Ukn0I0arBxKXlqKI-Dp0y3zUfbgQ-klvFRDoRqZBnanayipv9S74An_f_Z-K_U92-BUDTlA8F1azlThQPX04-q3pKOlAvo3wvMpZfRm9ESS8zjsCaw8c-I0zln7uB9m6Qv3e5HMaHO_MLrm5aTxgbtj-fQ1Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/69746" target="_blank">📅 19:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69744">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBy9ifG6q_D6rXQ80IkGFB_8i5Ytps7vWQGjIt0PGhvkBS8F-XF6Y_KFHsQ52bs2jp8nKIo-HtVZ54aeHw3t0ItCBv4BwOrb2Ko96Z5OcL8ixu37kG7Hfr-qzCeshJltp1BWJKEPu8QGPAVo-o-bq3ihiFZYmIQ3yhLws9oSggI5jplAGn16MkaCw8kZGLR1IZETD-EbNKq-fVh5oX3wKsU4uMBinsxh_rabeJC8WJWKVJ04JdGWd-Jh0-4ie1OQBMHtXirNaVOVw76T47qX_rzwzqQJ78zUpQW2rTDeWuz6vx5uJ_XbKLfX9TdCpkh88Y-Ge4DNSB-qibkMCrDOsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک تایمز:
ایران فهرستی از خواسته‌ها را ارائه کرد که این موضوع، امیدها را برای بازگشایی تنگه هرمز کمرنگ‌تر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69744" target="_blank">📅 18:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69743">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EX02IiOwiBpYcpibFhVLtDuw90dxnKfCKxRd0nqs7j3oxJEgGciDXULZ871MlHr6kpsZz2e4dE-zDOa61lSxnhdOHylZREdhBpM_TwTyIG4GzvMebaOfzEO4ZDKeL63EK0lsAmlHkrMJbonNWPvbEfcT2eXds8LMWEZzRFCmwAdm1eQf0_5FeWLLmuEBL8VpMlVUMHW4YqpPY2D-OViXzHOaw8Xj05C0LfZd07eBBt4sKyg_CZHyDJO5_saEz82rqXkO5eDOVPsg4uhEpTElrm_dbGN7AmjD_yWeMH7IYi0f2E-AD0ULT9sYU6uOjkdiTLU_35ixvUZtzbToCQ68AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان حمل و نقل دریایی بریتانیا (UKMTO):
گزارشی از حادثه‌ای در ۱۸ مایل دریایی شرق خصب، عمان دریافت کرده است.
یک منبع موثق گزارش داده است که یک کشتی مورد اصابت یک پرتابه ناشناخته قرار گرفته که باعث آتش‌سوزی شده و آتش  خاموش شده است.
هیچ گونه آسیب زیست‌محیطی گزارش نشده است. کشتی و خدمه در سلامت گزارش شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69743" target="_blank">📅 18:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69742">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/43af7e53e1.mp4?token=fb9Znwzlkdp9lUbiEx8UYrrYp3kTpq6Q4kAagPRbcxOlm23StzbGGOj1sX6SrEJD7qhttcXw0tcKp6jNRGbBvStaqT4_pxTM1UbqSVzI--BgY6PaG6XQ1DeqOPjBvm-D7ZE2A_JQttRJVnzwuaSkgf5J5CielfZ-hLT25vUJsXRDfcALv7o54HBfAAcsf8LX7juOG_Cb6oYkEEuRUlN_mhK5iVtWLwHTzDyjNK2cN_3bRRqxDgdqD64hjQ2f-gxWqk43azl7xNugzwnJeYy8MA30zEMPft9AkIpgkHW6BZJE9u426nAsxizqQw80GzRq-pnTNLyQgaOA0WR6GaxlOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/43af7e53e1.mp4?token=fb9Znwzlkdp9lUbiEx8UYrrYp3kTpq6Q4kAagPRbcxOlm23StzbGGOj1sX6SrEJD7qhttcXw0tcKp6jNRGbBvStaqT4_pxTM1UbqSVzI--BgY6PaG6XQ1DeqOPjBvm-D7ZE2A_JQttRJVnzwuaSkgf5J5CielfZ-hLT25vUJsXRDfcALv7o54HBfAAcsf8LX7juOG_Cb6oYkEEuRUlN_mhK5iVtWLwHTzDyjNK2cN_3bRRqxDgdqD64hjQ2f-gxWqk43azl7xNugzwnJeYy8MA30zEMPft9AkIpgkHW6BZJE9u426nAsxizqQw80GzRq-pnTNLyQgaOA0WR6GaxlOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبتای یه وکیل مرد:
توی تمام این سال‌ها به این نتیجه رسیدم که نود، برای پسرا معجزه می‌کنه.
پسرا عاشق اینن پارتنرشون بهشون نود بده، اصلا هم براشون مهم نیست کجان، سرکار، خونه و...
من خودم یه بار وسط دادگاه بودم و دوس دخترم برام نود فرستاد، منم گفتم این واقعا محشره، مرسی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69742" target="_blank">📅 18:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69740">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t8QFTrpmQm7nNzv5j1_6ItH2CvID-cusmNrXfiSo_j6gaA-2IH7VbX2gq5W2f2nCOiQH9az2IMIF8pVd1a-Q4b0DnKyRPGrvt4Y1fP8Nv2buHaxERJrK93ycb5_72sCKIRDZ2gttP64jM9yinnY9V3gAhAOKjw3YhfclC5brsfVzr1VqUO5il_kQk9OGu77nJrWxyONNkFGRjg2ikVFwmry1GdS8wC4qd6JNnFLOKljSIYbNF5Wt4wtmOJaVkgtlmOhUzDVV0T1ZerZ54TWU47j0s4b2FJliLuNsF-T9m2fwP5l_FrN_DC9EjmAjJsO0bCVvJyhwmhkySvHHBfL_rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c7e1449f7f.mp4?token=AecSGeVx30gezYR5bmgHJ-rvdsEQBNjtJxrQckC6AMu1hpw73W8w7ANYXx3niwt8wDMttFr3NnjGPgDY5fsvnMsgj7Jjm_a0mWFWjthvn_wVH0JLW60xgJLwEzRrKuFSYQlIN_XFhBh-J4BZasrKBZ0U-q8LeFENlpTsUHOxmLeBU68hKn7vwg_L-vQUN-GPrZp-CnEig1b_GZlH5vofjZgGKaDSlm1Xowaf5Iol_uWaVeOamR-r6pm_736K9AzDGkKBUQJmNwuRwfSgHfHjvXUqHFQbn1lXUpkvruodh9FcrgOOhoV2Ex3gyrskzOckwbpG1BunGXcfSbFKOOTPEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c7e1449f7f.mp4?token=AecSGeVx30gezYR5bmgHJ-rvdsEQBNjtJxrQckC6AMu1hpw73W8w7ANYXx3niwt8wDMttFr3NnjGPgDY5fsvnMsgj7Jjm_a0mWFWjthvn_wVH0JLW60xgJLwEzRrKuFSYQlIN_XFhBh-J4BZasrKBZ0U-q8LeFENlpTsUHOxmLeBU68hKn7vwg_L-vQUN-GPrZp-CnEig1b_GZlH5vofjZgGKaDSlm1Xowaf5Iol_uWaVeOamR-r6pm_736K9AzDGkKBUQJmNwuRwfSgHfHjvXUqHFQbn1lXUpkvruodh9FcrgOOhoV2Ex3gyrskzOckwbpG1BunGXcfSbFKOOTPEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی اوکراین به دو پالایشگاه نفت در روسیه
پهپادهای اوکراینی بار دیگر پالایشگاه نفت سیزران در استان سامارا را هدف قرار دادند که در پی آن، آتش‌سوزی گسترده‌ای در این پالایشگاه رخ داد.
در حمله‌ای جداگانه نیز پهپادهای اوکراینی به پالایشگاه نفت ایلسکی در منطقه کراسنودار حمله کردند که باعث وقوع آتش‌سوزی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69740" target="_blank">📅 17:32 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

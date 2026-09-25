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
<img src="https://cdn4.telesco.pe/file/ixCl_7hTwlV-GdJeN2zUWdxaHdnA9WeV_9_KlDpPCwBlEW-TrUh61Iu2p18HP83kaL_wrPp95HsTLIml63xGg5fbGvWc9Glvx113zT4voOkr-KX0Y2A69VIuuvgEsC6eIMTh4mzll80bV7pHsatYqG5ehHxav5sIgitZuuTtzcvE5eGnAU0YHlohFufNXxp9PY28wHOBb0vwF1a7gPY7LD73ye1hGbwIkob6uYt2dSfew1Qb4nJfFkZheBtqFSjvPCm7hlkQHj_jElyfhEVli7BjopthXgQ-zstfV-a0cjPtWR066aSUJgxOf4-8RH1nXgOGzJapB5Mi4Xlqc24IrQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 106K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 09:47:03</div>
<hr>

<div class="tg-post" id="msg-72251">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJkUNyuPQpKNv6Ba3dVzxD77T04T5ebyprA9tfNAF-He8F7IDTDdHh9u1UWqmBj8OgQZIzBOqWDtqn3XSnKggvL2sQad0VVq8kfTOcSYxSu5m1yjmWoPzoAWW_DPsAZOtVm--hG1eYDOkn8c_7xC2H_4OeaxR7lbfQ0CwjiED0zpwqWIFmAhpyzhuqa_ZLNteldWT7wf7mUEdXclfFVlP4ouurp7E4oi88ui8rvRnDqCC5nFSlbUy_DBZZbnSByefceS9hJMvVVN6nzK6n3lDdlZ1l7h9rd8qtLMg6rDMbTwQdfHwuao3kUO2oy6sM65JFjDYAt7x1CmP7P1cGY7LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ان‌بی‌سی‌ نیوز:
مسعود پزشکیان، رئیس‌جمهور ایران، اظهار داشت که تهران خواهان احیای توافق آتش‌بس خود با ایالات متحده پیش از انتخابات میان‌دوره‌ای ماه نوامبر است.
پزشکیان گفت: «ما نمی‌خواهیم کار به انتخابات میان‌دوره‌ای بکشد. ما خواهان آن هستیم که آمریکایی‌ها پیش از انتخابات میان‌دوره‌ای به تفاهم‌نامه بازگردند.»
پزشکیان همچنین اعلام کرد که ایران برای بازرسی از تأسیسات هسته‌ای خود «آمادگی دارد» و هرگونه تلاش برای ترور ترامپ یا خانواده‌اش را تکذیب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/news_hut/72251" target="_blank">📅 09:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72250">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ویدیوی کامل سخنرانی بنیامین نتانیاهو نخست وزیر اسرائیل در مجمع عمومی سازمان ملل به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/news_hut/72250" target="_blank">📅 09:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72249">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae3b513eed.mp4?token=UQPcrDpvu-EW_Zoi_8BAx5Y9gZnOe9cvnh-6RPa-Fmbu-2cz6qbwxxumq5X5h6fWlRib-RXrvRp9VACoRHXhQOkdYVntLLXpPVvdIp9iehxD3NG7mWlny7GSiyfvAUZr42IZPJO5ieQndRbDqvcyMKQljXL2bVW4gWCm2nvZWnaVttqVzXkexXV_kk68Hb0i1YIK3XQZev5YcYvQBiZHdrXw6acvvp2iFI1t9Gsyb-j4BsPRPzshUfZ1HguF_KumdUBz1RA25Kw92_dep5AfLC91gWAVS3-oTsMwsNpXdqjIy4wGMoRGdLmvYC2eo3emr-yYhVTcoNhN_NBd9xv4aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae3b513eed.mp4?token=UQPcrDpvu-EW_Zoi_8BAx5Y9gZnOe9cvnh-6RPa-Fmbu-2cz6qbwxxumq5X5h6fWlRib-RXrvRp9VACoRHXhQOkdYVntLLXpPVvdIp9iehxD3NG7mWlny7GSiyfvAUZr42IZPJO5ieQndRbDqvcyMKQljXL2bVW4gWCm2nvZWnaVttqVzXkexXV_kk68Hb0i1YIK3XQZev5YcYvQBiZHdrXw6acvvp2iFI1t9Gsyb-j4BsPRPzshUfZ1HguF_KumdUBz1RA25Kw92_dep5AfLC91gWAVS3-oTsMwsNpXdqjIy4wGMoRGdLmvYC2eo3emr-yYhVTcoNhN_NBd9xv4aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: جناب نخست وزیر پیامتون برای مردم ایران چیه؟؟
بی‌بی نتانیاهو: ما با شما هستیم نا امید نشید
@News_Hut</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/news_hut/72249" target="_blank">📅 08:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72248">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">با این جوابایی که پزشکیان به خبرنگار داد باید منتظر موج جدیدی از حملات طرفداران افراطی جمهوری اسلامی و تندرو ها به پزشکیان و دارو‌دستش باشیم.
@News_Hut</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/news_hut/72248" target="_blank">📅 07:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72247">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پزشکیان:
- انصارالله مسئول اقدامات خود است و از ما دستور نمی‌گیرد.
- ما اورانیوم غنی‌شده ۶۰ درصد را در چارچوب قوانین بین‌المللی و پیمان منع گسترش سلاح‌های هسته‌ای (NPT) واگذار خواهیم کرد.
- ما به تمامی تعهدات خود ذیل پیمان منع گسترش سلاح‌های هسته‌ای پایبند خواهیم بود.
@News_Hut</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/news_hut/72247" target="_blank">📅 07:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72246">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efefaab11b.mp4?token=mNlUuy6NJkr3vTbXI6C5SV6-AdjsmSuee2RcGQdScLU8DHb5i77tWgINJwOpr822C4feo4ZOdfVFtIB7PpYdurcp6PGkx-sYlUYgc8FRrkiLGPWYqXDuQAxA0ZT5nBLhGJuAMkofn11YCl0faAk7I6u_IRnWyft0dh3k1ZTLsSuzI7X9Exo5CVh5lnhq-TdJ4LKMqln-zS3WOD5UqYUvg3Iqd_m_YUd4fStkMjsY-3zCIat59k45KkEwxvpeOqtuCTgrRqMLXZkCfmpGLQq1zNj9PPUllEj-UoIHgrVwIrnO8Lbpm0CAJK8ooQZGf7DdTBewN027YRHhUiLrD3r-mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efefaab11b.mp4?token=mNlUuy6NJkr3vTbXI6C5SV6-AdjsmSuee2RcGQdScLU8DHb5i77tWgINJwOpr822C4feo4ZOdfVFtIB7PpYdurcp6PGkx-sYlUYgc8FRrkiLGPWYqXDuQAxA0ZT5nBLhGJuAMkofn11YCl0faAk7I6u_IRnWyft0dh3k1ZTLsSuzI7X9Exo5CVh5lnhq-TdJ4LKMqln-zS3WOD5UqYUvg3Iqd_m_YUd4fStkMjsY-3zCIat59k45KkEwxvpeOqtuCTgrRqMLXZkCfmpGLQq1zNj9PPUllEj-UoIHgrVwIrnO8Lbpm0CAJK8ooQZGf7DdTBewN027YRHhUiLrD3r-mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس‌نیوز:
آژانس بین‌المللی انرژی اتمی می‌گوید شما ۴۴۰ کیلوگرم اورانیوم غنی‌شده تا سطح ۶۰ درصد در اختیار دارید. این اورانیوم کجاست؟
پزشکیان:
آمریکا مدام می‌گوید ما همه‌چیز را نابود کرده‌ایم. خب، این ادعا یا درست است یا نادرست؛ کدام‌یک است؟
@News_Hut</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/news_hut/72246" target="_blank">📅 07:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72245">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54d65dc0d7.mp4?token=p48ArVrv7S2rzpLH0TL5HaBoz8H9eTAIrJGPKsHBGAdD0pjOywrYu6jtgkrrl98P6G2d3WPYMX_mostqehBkXA4xiezsWjMbS6pee1-R9czxccMNlT37zhEDnrO1uZhQK9K2o4yr00omEDKSvsGtMVDThtWD1KSNn5sL4sk32fu8cjN-4L8W1QFTVkd6Ez8Est9OtlI2-TdlCOdrTVWAaDggy0VqB3prB3xdfrcrVli057AcL8j1YUm6SuuXGjs-SlNzUoYRDUQM0FlKDEi2_VyT5Cl79kZIP-rcqBtvlbJlvFTlrXS_u7e3Vkjzbf47-EC-v8ddjoSEVXMBbkLnArjP_SCV0GWfCfRon80BSuaI99oMMfq7A99vutFt1MqsG3_tRVi9OwhkCZ0MjUBvz1LmVf-2N1QuGT3jD5gyWpY_bOrOoT3EzHBW39M5l5mDnbtDqrshdfiHOM1LToDPi_D1hAAlgN2XY4x1AP9yr3IzLKrDNFQS8WOMMUd2hN3wAti3cO6ucrtc-ey7h5UIfBwl6cm50EQdgp3BvMnhHHoJex8spGCyWcWkwPJ-Fzqvo8ZDh3C3m1-wNLiOU1QHXqvZqbEPSap_VZfgCGqlmkxz4GcEoF0TVA2XmJg5_-a7LeeM7KpL2xKPIHZDori4IQLOmJs070u1hFo0VGV3kBs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54d65dc0d7.mp4?token=p48ArVrv7S2rzpLH0TL5HaBoz8H9eTAIrJGPKsHBGAdD0pjOywrYu6jtgkrrl98P6G2d3WPYMX_mostqehBkXA4xiezsWjMbS6pee1-R9czxccMNlT37zhEDnrO1uZhQK9K2o4yr00omEDKSvsGtMVDThtWD1KSNn5sL4sk32fu8cjN-4L8W1QFTVkd6Ez8Est9OtlI2-TdlCOdrTVWAaDggy0VqB3prB3xdfrcrVli057AcL8j1YUm6SuuXGjs-SlNzUoYRDUQM0FlKDEi2_VyT5Cl79kZIP-rcqBtvlbJlvFTlrXS_u7e3Vkjzbf47-EC-v8ddjoSEVXMBbkLnArjP_SCV0GWfCfRon80BSuaI99oMMfq7A99vutFt1MqsG3_tRVi9OwhkCZ0MjUBvz1LmVf-2N1QuGT3jD5gyWpY_bOrOoT3EzHBW39M5l5mDnbtDqrshdfiHOM1LToDPi_D1hAAlgN2XY4x1AP9yr3IzLKrDNFQS8WOMMUd2hN3wAti3cO6ucrtc-ey7h5UIfBwl6cm50EQdgp3BvMnhHHoJex8spGCyWcWkwPJ-Fzqvo8ZDh3C3m1-wNLiOU1QHXqvZqbEPSap_VZfgCGqlmkxz4GcEoF0TVA2XmJg5_-a7LeeM7KpL2xKPIHZDori4IQLOmJs070u1hFo0VGV3kBs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
خودِ آقای ترامپ اعلام کرد که آمریکا این افراد را تجهیز و مسلح کرده بود تا حکومت ایران را سرنگون کند.
اطرافیان نتانیاهو اعلام کرده بودند که نیروهایی از استان‌های کردستان و بلوچستان به مراکز کلان‌شهری نفوذ خواهند کرد تا حکومت را ساقط کنند.
آن‌ها تصور می‌کردند که این ماجرا سه روزه تمام می‌شود و حکومت سقوط می‌کند؛ اما حکومت استوار ماند و منسجم‌تر و متحدتر شد.
حتی کسانی که به دلایل گوناگون در برابر حکومت ایران ایستاده و با ما مخالف بودند، اکنون از ایران حمایت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/news_hut/72245" target="_blank">📅 07:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72244">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=QczusUb0JT8aMl65R-WBjuCKe9jSeBznP-bQUpXCV5g71RD_tW7eUIU5hbiQXuhr4CTwrTmCudSPib_PODTSn_1RE96U0rziMiO7Rom8QYPVKrssf-aM80y9_anJDJjIUZ2COFwfdmqPQ--TkVDtHRMbVHyUxCk_2NAx6dBOkfI2XrRdziovn_Gh5WrahpR69bcVAwSoTiQrfcrg3hbpj8UMMLkLBhcBUS6Gy9G-3_0U5hFpFwmf1pAqvGNmFYNOwvYkrPRybY-2krUfd0Bl5wPBU5FqDsR_FKrQt-dQR44SiN8_mHzOVDMZqkhgyyYcagfdsDe3qmEDHF1SeiZWxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=QczusUb0JT8aMl65R-WBjuCKe9jSeBznP-bQUpXCV5g71RD_tW7eUIU5hbiQXuhr4CTwrTmCudSPib_PODTSn_1RE96U0rziMiO7Rom8QYPVKrssf-aM80y9_anJDJjIUZ2COFwfdmqPQ--TkVDtHRMbVHyUxCk_2NAx6dBOkfI2XrRdziovn_Gh5WrahpR69bcVAwSoTiQrfcrg3hbpj8UMMLkLBhcBUS6Gy9G-3_0U5hFpFwmf1pAqvGNmFYNOwvYkrPRybY-2krUfd0Bl5wPBU5FqDsR_FKrQt-dQR44SiN8_mHzOVDMZqkhgyyYcagfdsDe3qmEDHF1SeiZWxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
ما هرگز به مردم خودمان حمله نمی‌کنیم.
برت بایر (از شبکه فاکس):
اما شما این کار را کردید.
پزشکیان:
نه، نه. چه کسی علیه ما اقدامات تروریستی انجام داد؟ چه کسی مدارس ما را هدف قرار داد؟
بایر:
متوجه هستم، اما در روزهای ۸ و ۹ ژانویه، قطعاً نیروهای امنیتی شما شهروندان ایرانی را کشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/news_hut/72244" target="_blank">📅 07:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72243">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2094964f.mp4?token=kl_k9FUs9DAK2IIGf4fJSjxSyFBoFE0ydgLtvzkf2QN8P8j1Td_QwSKyZhDV9sNWdw6rRXGvC1evBY1Ql6YejImzEMRg2dAhefIGLkeRpmCDMNXRuVoAes2U6YHI8o1cqjdW2bbA0LugbMq9uukwhnK1oZkPg7O8vm4psd0vN1-kKIQL2J5i1gNZ7oyxYbELCaxU6GZDNbmJrBwONZyc0zJx9HP95_K4XGkQ-mBh0uDhRUaEpPGEoNfpbG9L81X9lKNQXoGw2PInA8C-WCWXsVES1aNC7n3_TQsBciEamHrBOipBRRWJ6EW8Pag6Q8XtA1N_47XhKyRhnbf6RW64yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2094964f.mp4?token=kl_k9FUs9DAK2IIGf4fJSjxSyFBoFE0ydgLtvzkf2QN8P8j1Td_QwSKyZhDV9sNWdw6rRXGvC1evBY1Ql6YejImzEMRg2dAhefIGLkeRpmCDMNXRuVoAes2U6YHI8o1cqjdW2bbA0LugbMq9uukwhnK1oZkPg7O8vm4psd0vN1-kKIQL2J5i1gNZ7oyxYbELCaxU6GZDNbmJrBwONZyc0zJx9HP95_K4XGkQ-mBh0uDhRUaEpPGEoNfpbG9L81X9lKNQXoGw2PInA8C-WCWXsVES1aNC7n3_TQsBciEamHrBOipBRRWJ6EW8Pag6Q8XtA1N_47XhKyRhnbf6RW64yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
رئیس‌جمهور آمریکا اعلام کرد که ما تروریست هستیم.
اما در واقعیت، همه به‌راحتی می‌توانند تشخیص دهند که ما قربانی و هدف تروریسم بوده‌ایم؛ با این حال آن‌ها می‌گویند: «نه، ما چنین کاری نکردیم.»
آن‌ها حقیقتی آشکار را انکار می‌کنند، اما در عین حال ما را به چنین اقداماتی متهم می‌سازند.
ما خواهان زندگی در صلح و آرامش در منطقه هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/news_hut/72243" target="_blank">📅 07:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72242">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb427a69c.mp4?token=R2RguHw4Y4zcMbBsx2XAG6Am43tOkazTM7EqgAoeg3981KjdRhSzj-XtJ0Wx8ukZThPJ4R6XFJUq2nAeNy585qi_yCzDbohZcPCLxcy3v54OQQWbasgAEiAJhFTTirEX3TrZEL-bGODy3oQ2phREK3kwxArj53qRYVgurkX62Z4g5sa1-Fc7OD41T_GTfQPjfHMyW35SvWSOSZXxVqLR446hF4SPDXdVkExyfuj6c5D3T-x9CCeWd-NNgO33zw2PB4u6Syw1_6ydgRaH5CILAW6SygrrtwrWSq0_iQq7_u873v672BIeFbl6XvwFpSR2QZXzzRfjhjZeQtJ3VQ_qEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb427a69c.mp4?token=R2RguHw4Y4zcMbBsx2XAG6Am43tOkazTM7EqgAoeg3981KjdRhSzj-XtJ0Wx8ukZThPJ4R6XFJUq2nAeNy585qi_yCzDbohZcPCLxcy3v54OQQWbasgAEiAJhFTTirEX3TrZEL-bGODy3oQ2phREK3kwxArj53qRYVgurkX62Z4g5sa1-Fc7OD41T_GTfQPjfHMyW35SvWSOSZXxVqLR446hF4SPDXdVkExyfuj6c5D3T-x9CCeWd-NNgO33zw2PB4u6Syw1_6ydgRaH5CILAW6SygrrtwrWSq0_iQq7_u873v672BIeFbl6XvwFpSR2QZXzzRfjhjZeQtJ3VQ_qEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
ما تا آخرین لحظه به مقاومت ادامه خواهیم داد.
بله، قطعاً مشکلات اقتصادی داریم؛ اما برای بقا، از هر سختی‌ای عبور خواهیم کرد و ایستادگی خواهیم نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/news_hut/72242" target="_blank">📅 07:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72241">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9fa81c1c3.mp4?token=cLZzkd7sE-hP6jQZJDkVL10JfxGwKRNHoZ6ngo_6XpvE-_ItD36v_Bw1Ffr0lRdJtLiO0F4Dtfv30NoX7Ow4ijNe8WTaROhpOykAQlyzXd167pm_WboPFrnwBLpQLBQCyALeK8UoP6oIOTKLY2yJSSJUF6OWFbQzWtjMf4ZfAtdD8lRAd9hktYXpoelzyyeIujoYHKwSh8D69Lt4uicih167fOIj-YAIX_JrVXJVOHMShufKsU0YhEGUd5wgGQDg-19w1GwSaSKH3WFRvU3nFFBXcadwPEVc_Rq6XOfG5vqyyWVEtotzvCvBktL4TJ47_5COPi2SnkPPG6EgqqB4mZREhauOPTQ1hElUcLmp8YnKfTk3tBbfmafssGqnYee7wlorN8DyfMPHk9IFsY8ist3a2lwYziJsr7j60OeNejUn0ARnZzTaIK2o6JWtS-tmSiDdUMzBBUAmUNdTcQuZdZZg_YkKQrDVScx5PswHHa8Y_fHIRosS9Q7QcWTBjgUFsanMCIfQKBQfxi9Bs4lIpIrndRCthSSFO1M4UGu7B1CHSE0tkgeDTF6PtT2mUrJhhd2u8CfK5GxC8u3MpCJmNT3kdpFFDDUhE8bgOyeihH_LiPEdV81LTY8-19Vz7LxnVS4gkJiCRitGwFblJNUQKrIGwliacGq4_zE--oPJEvI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9fa81c1c3.mp4?token=cLZzkd7sE-hP6jQZJDkVL10JfxGwKRNHoZ6ngo_6XpvE-_ItD36v_Bw1Ffr0lRdJtLiO0F4Dtfv30NoX7Ow4ijNe8WTaROhpOykAQlyzXd167pm_WboPFrnwBLpQLBQCyALeK8UoP6oIOTKLY2yJSSJUF6OWFbQzWtjMf4ZfAtdD8lRAd9hktYXpoelzyyeIujoYHKwSh8D69Lt4uicih167fOIj-YAIX_JrVXJVOHMShufKsU0YhEGUd5wgGQDg-19w1GwSaSKH3WFRvU3nFFBXcadwPEVc_Rq6XOfG5vqyyWVEtotzvCvBktL4TJ47_5COPi2SnkPPG6EgqqB4mZREhauOPTQ1hElUcLmp8YnKfTk3tBbfmafssGqnYee7wlorN8DyfMPHk9IFsY8ist3a2lwYziJsr7j60OeNejUn0ARnZzTaIK2o6JWtS-tmSiDdUMzBBUAmUNdTcQuZdZZg_YkKQrDVScx5PswHHa8Y_fHIRosS9Q7QcWTBjgUFsanMCIfQKBQfxi9Bs4lIpIrndRCthSSFO1M4UGu7B1CHSE0tkgeDTF6PtT2mUrJhhd2u8CfK5GxC8u3MpCJmNT3kdpFFDDUhE8bgOyeihH_LiPEdV81LTY8-19Vz7LxnVS4gkJiCRitGwFblJNUQKrIGwliacGq4_zE--oPJEvI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
ترامپ مدام می‌گفت «می‌خواهم برای مردم ایران هدیه‌ای بیاورم»، اما هدیه‌ای که آن‌ها برای ما آوردند، موشک‌های هدایت‌شونده، تسلیحات سنگین و ویرانی بود.
آنچه آن‌ها واقعاً به دنبال آن هستند، دامن زدن به وقایعی در کشور است که زمینه را برای فروپاشی نظام، جامعه و دولت فراهم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/news_hut/72241" target="_blank">📅 07:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72240">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b006ce96b.mp4?token=fhgnj4m_ex2UABJ6CaRdtMitVUStQZOgEh2a63ihg5GVTZlUBISOAWgIVIvAiVuq99fWqGRh9tJl7Iy9uhsmM8YsDyq3NqSoX4R0QieowXfnnCmDTwhbTArU5e2rqUTgyth_MdAXrbMAaRVBCPkvrVIGCYj_nKUuthPzbBA01XTHRTDQwICAQYgI3ToNa4_Ct-XewTVJ8x3_iqnzT8RvzS9ZTCL4N6VSkxK3c3081WD3d1FQ7_DF7hQ4fjpswoNOus6c4me8QVO468pzdh4NkPhjrkc2zne7AtzrrUTnxX5-UrIICgB3Joxr3Mbc2t5ySs7TleZhgFMADRBZ8qyWsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b006ce96b.mp4?token=fhgnj4m_ex2UABJ6CaRdtMitVUStQZOgEh2a63ihg5GVTZlUBISOAWgIVIvAiVuq99fWqGRh9tJl7Iy9uhsmM8YsDyq3NqSoX4R0QieowXfnnCmDTwhbTArU5e2rqUTgyth_MdAXrbMAaRVBCPkvrVIGCYj_nKUuthPzbBA01XTHRTDQwICAQYgI3ToNa4_Ct-XewTVJ8x3_iqnzT8RvzS9ZTCL4N6VSkxK3c3081WD3d1FQ7_DF7hQ4fjpswoNOus6c4me8QVO468pzdh4NkPhjrkc2zne7AtzrrUTnxX5-UrIICgB3Joxr3Mbc2t5ySs7TleZhgFMADRBZ8qyWsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
اگر دولت فعلی آمریکا بخواهد در چارچوب حقوق بین‌الملل به توافق برسد، بسیار خب.
اگر نه، چه پیش از انتخابات باشد و چه پس از آن، برای ما چه تفاوتی دارد؟
@News_Hut</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/news_hut/72240" target="_blank">📅 07:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72239">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d17a7864a.mp4?token=XfXIZHre6CBN797thr_ozbIjHlitUcmhW-lsQEKxe_eETIi8_6erLhmtVzFY16m1j6CAzM6qOYRdQmc1UJdsJFOQPPp_SaZyrD_QDKt-PA7JpOkIrsjoUDD5Zu7PHXFewK3nELSmTOWUud-eRaZ4RrOU72NVoDfQNPaDiAIuG20Q9juDv6pGQg6pxXolYvrZ-JIGOwHc5uPpZaMDi-xi9t2MKxYeZ8soeA-oIjyZnseTW3M-cejX2oZIKxklxhaoUKZ9xeR-GiJpzNwtb-Ei9qvTDe5QXj59y4zMEY7j1sELUxQo8r8BfVKRrIx_Jtpmz9Vd2reKL_CuaNi2dr6g5jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d17a7864a.mp4?token=XfXIZHre6CBN797thr_ozbIjHlitUcmhW-lsQEKxe_eETIi8_6erLhmtVzFY16m1j6CAzM6qOYRdQmc1UJdsJFOQPPp_SaZyrD_QDKt-PA7JpOkIrsjoUDD5Zu7PHXFewK3nELSmTOWUud-eRaZ4RrOU72NVoDfQNPaDiAIuG20Q9juDv6pGQg6pxXolYvrZ-JIGOwHc5uPpZaMDi-xi9t2MKxYeZ8soeA-oIjyZnseTW3M-cejX2oZIKxklxhaoUKZ9xeR-GiJpzNwtb-Ei9qvTDe5QXj59y4zMEY7j1sELUxQo8r8BfVKRrIx_Jtpmz9Vd2reKL_CuaNi2dr6g5jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
ما هرگز به دنبال جنگ نبوده‌ایم و نیستیم. من عمیقاً معتقدم که انسان‌ها نباید موجب مرگ انسان دیگری شوند.
قرار است ما موجودات برگزیده خلقت باشیم. وقتی می‌توانیم مسائل را از طریق گفتگو حل‌وفصل کنیم، نباید به کشتن یکدیگر متوسل شویم.
اما با اقداماتی که اسرائیل انجام داده، آن‌ها این جنگ را به ما تحمیل کرده‌اند.
با این حال، ما خواهان ادامه آن نیستیم. این آمریکاست که باید تصمیم بگیرد آیا می‌خواهد به این وضعیت پایان دهد یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/news_hut/72239" target="_blank">📅 07:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72238">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f631e90489.mp4?token=UHHUD0knMTefWqEIGGJW0V3ctgDBenJBWKRpGqHKZOM5PQj9hCa0SURDdOAw-inlHhbdCAVcQnFyY2MHLrmZ3WFFAFfwT3_WEckT2eoCvsDuc6xvd1q3IQrmVETArxqwnzvV-Qf4Np33KcbKY-7OcqWVLGwyfhcfC82dfDn8qTi9dlOQMs5BgO2K9WHe4BfkKzjqF4bUsmgUzlPwOkXl1l4igGePUI8G_QmbNmDYNGnqlQLeLccod0YzaTBbkNcg7YKwTdjcWWpe8lbFTfDVAlb7YYUa-xehq5eeXDTcNL67YzHUKMhClwxK8QdTpLY2sQg6Gp0iA_EWD14SmajHRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f631e90489.mp4?token=UHHUD0knMTefWqEIGGJW0V3ctgDBenJBWKRpGqHKZOM5PQj9hCa0SURDdOAw-inlHhbdCAVcQnFyY2MHLrmZ3WFFAFfwT3_WEckT2eoCvsDuc6xvd1q3IQrmVETArxqwnzvV-Qf4Np33KcbKY-7OcqWVLGwyfhcfC82dfDn8qTi9dlOQMs5BgO2K9WHe4BfkKzjqF4bUsmgUzlPwOkXl1l4igGePUI8G_QmbNmDYNGnqlQLeLccod0YzaTBbkNcg7YKwTdjcWWpe8lbFTfDVAlb7YYUa-xehq5eeXDTcNL67YzHUKMhClwxK8QdTpLY2sQg6Gp0iA_EWD14SmajHRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
یکی از مشکلاتی که با آن مواجه هستیم، مسدود بودن منابع مالی ما در چین است.
ما حتی نمی‌توانیم پول خود را از کشوری که به آن کالا صادر کرده‌ایم خارج کنیم، چه برسد به اینکه بخواهیم از آن وجوه برای پرداخت به طرفی دیگر در گوشه‌ای دیگر از جهان استفاده کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/news_hut/72238" target="_blank">📅 07:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72237">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4c8deae6.mp4?token=tmo9-5LFcMY0txhxvhtukutiDxS3_rfkzrwSNThrRnB4EViySOd4h0EfKAjNepaflUShMTj0mS6ojO1HpN9SKPCBR5ICrznR3mOhm2DCZPDhsLQI2UwAJwGPjZHX2hMcUVxqzMAs39p2FBQ-ft5z7Eowab6DhTwkSkvHRbGNFpiEjxrtdggH0g58TSAjiW8tciStZirjwW0AfX3cJ8jtxyNNSemhp6tSXNwotsrYcl5eFM7NC89wiqGI-wUOc94zqnAJB-5YKa4QbEMhBJSVtjQ2dOjZPSq9SvxP4UOj2v_tXx7umV9KUsNnIP3w6SsLUm988XBn9zGaRgvIzS5ChA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4c8deae6.mp4?token=tmo9-5LFcMY0txhxvhtukutiDxS3_rfkzrwSNThrRnB4EViySOd4h0EfKAjNepaflUShMTj0mS6ojO1HpN9SKPCBR5ICrznR3mOhm2DCZPDhsLQI2UwAJwGPjZHX2hMcUVxqzMAs39p2FBQ-ft5z7Eowab6DhTwkSkvHRbGNFpiEjxrtdggH0g58TSAjiW8tciStZirjwW0AfX3cJ8jtxyNNSemhp6tSXNwotsrYcl5eFM7NC89wiqGI-wUOc94zqnAJB-5YKa4QbEMhBJSVtjQ2dOjZPSq9SvxP4UOj2v_tXx7umV9KUsNnIP3w6SsLUm988XBn9zGaRgvIzS5ChA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان در گفتگو با خبرنگار فاکس‌نیوز:
هر کس بخواهد اعتراض کند، کاملاً حق انجام این کار را دارد.
ما با بسیاری از این کارشناسان گفتگو کرده‌ایم. اما تبدیل اعتراضات به ابزاری برای تقابل (مسلح کردن معترضان)، مقوله‌ای کاملاً متفاوت است.
@News_Hut</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/news_hut/72237" target="_blank">📅 07:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72236">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72236" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/72236" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72235">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crsJ6-onsPkUgahk7_HdlEZ2qOi7Pf7VQjruxbg6zwCWTKRwdttdcmtFpLHoUNZ_OSfFLhHgyT9mveHEzY9WkUfZha_uzrPhHqXlKf5Xq3OtFI7DLpJzrvt2-C6R1pQTqMZYfqDUZrL8rbJFwb0bb2uTrbx87b4sx4MYZpMT5Du7dJPgl4gIHq7kgcofTYv4MtXkqu8BTggkgU3r2-vQoIYud3CZsC-efF6jzXiOzzXeB8KiYKO-OXLxdaEIpICZIxlY5AkvGwHpfvADxlD--Ppai0yWt1OaQS3W12mprkGaKELGAUrHDg5rWXZYqkALQXQXBK1KDgpgBQR1bMtkbQ.jpg" alt="photo" loading="lazy"/></div>
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
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/72235" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72234">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25201994ac.mp4?token=qe7NeFvUP5E5AkHS0l2apOPp0ir-DQsas9KEuWmr0kFGbuRfKzG4sTrAMqssugxd2G1YN7AplIletOUpAjuyf3Zux_ynjcLjTx0MCHGJPJ56nnkhzS_prMnkUI1uCLbYEzti0MTqpnE3ofwfVzg0v2kesE1OT-Y-v2PJyMpcCfCUwu1_cjJhdHxFyRZn7f5IreT4GstUu0PZZo0c5SvYP136pXcKKQuf0Y3tKLD5JZmhcZgODzhUnub1upQqrAFhjpc_JT300qTsuM_qSFxQ5XuL8kMpNBYmjY-Uad8_ThLnhd7HLArfllQFBsRCzqynbm-68xRI98PkdKYvVGahxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25201994ac.mp4?token=qe7NeFvUP5E5AkHS0l2apOPp0ir-DQsas9KEuWmr0kFGbuRfKzG4sTrAMqssugxd2G1YN7AplIletOUpAjuyf3Zux_ynjcLjTx0MCHGJPJ56nnkhzS_prMnkUI1uCLbYEzti0MTqpnE3ofwfVzg0v2kesE1OT-Y-v2PJyMpcCfCUwu1_cjJhdHxFyRZn7f5IreT4GstUu0PZZo0c5SvYP136pXcKKQuf0Y3tKLD5JZmhcZgODzhUnub1upQqrAFhjpc_JT300qTsuM_qSFxQ5XuL8kMpNBYmjY-Uad8_ThLnhd7HLArfllQFBsRCzqynbm-68xRI98PkdKYvVGahxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
‼️
🇮🇷
🇮🇱
🌟
نماینده اسرائیل در سازمان ملل دستگاه «استارلینک» را به نماینده اعزامی تهران داد و درباره «کمک به مردم ایران برای سرنوشت و آزادی با این دستگاه» صحبت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/72234" target="_blank">📅 01:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72233">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7bed5269.mp4?token=RYVjW1VfREdGlmdosgsYW5A6TfWIrQ2oYoyfs62TxCt-R8pkWy0AkumW_KBJma_PoFJUfMulNK7y2PhGOa8wnJzYRo7CghBTOxwlqXnf2cYQ_F1ICcB6iS6nUhyHUKG6RoL8QDufpVfqTRIZ-Fmdevb4qWRHgVHJbh-YkMzaO8FXhCHiId_cxo_J_FmGElcpGHX3Oirm1_CF7GaSceItpKHCp_1LS51OjVXM3ugCQceu9hVy1SMv9oKMOfYS4NPUI_1IDWeuL3ExmopBe0shI2E4CDXefR1IRVQ_Fy2iGuvVj2VZfcteN0ChAUZCcL-5FnTjBho4uGjA7Gj_SwldlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7bed5269.mp4?token=RYVjW1VfREdGlmdosgsYW5A6TfWIrQ2oYoyfs62TxCt-R8pkWy0AkumW_KBJma_PoFJUfMulNK7y2PhGOa8wnJzYRo7CghBTOxwlqXnf2cYQ_F1ICcB6iS6nUhyHUKG6RoL8QDufpVfqTRIZ-Fmdevb4qWRHgVHJbh-YkMzaO8FXhCHiId_cxo_J_FmGElcpGHX3Oirm1_CF7GaSceItpKHCp_1LS51OjVXM3ugCQceu9hVy1SMv9oKMOfYS4NPUI_1IDWeuL3ExmopBe0shI2E4CDXefR1IRVQ_Fy2iGuvVj2VZfcteN0ChAUZCcL-5FnTjBho4uGjA7Gj_SwldlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مستربین ۷۱ ساله شد و جشن تولدشو با صدای بانو هایده جشن گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/72233" target="_blank">📅 00:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72230">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef647d91c.mp4?token=qFCwk9ygo1uds_KBBAl4BVGLRTG98eWAnaGmYHicQvStJCZgscbWLTzpg6MYw_RIsf6949NjoyqG-XqSeQnzew92EUxXWKwidDYwxuRvsMunxxI7m6RtGnufFL7NMHH2YNcl-o7stKVNE22t6Gbwwecf8wV-gLxgOx2_z2zsYcooY1Z-mWnfdYXTOmQotWlYA_UHugQ5bJ1bhPP1mIDabbgXJ2udpbr6gGAMys_BmfyYDhR21B9bLXyraE4JdWPdQ08q_Ie_jIzkviQ9ClpmPZB9eyDHoB_Fexu8mvvStVrX2dCbaD5qdxS5IPsH5E5RcnS2spC8Kudemh_NOCVA1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef647d91c.mp4?token=qFCwk9ygo1uds_KBBAl4BVGLRTG98eWAnaGmYHicQvStJCZgscbWLTzpg6MYw_RIsf6949NjoyqG-XqSeQnzew92EUxXWKwidDYwxuRvsMunxxI7m6RtGnufFL7NMHH2YNcl-o7stKVNE22t6Gbwwecf8wV-gLxgOx2_z2zsYcooY1Z-mWnfdYXTOmQotWlYA_UHugQ5bJ1bhPP1mIDabbgXJ2udpbr6gGAMys_BmfyYDhR21B9bLXyraE4JdWPdQ08q_Ie_jIzkviQ9ClpmPZB9eyDHoB_Fexu8mvvStVrX2dCbaD5qdxS5IPsH5E5RcnS2spC8Kudemh_NOCVA1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش جالب رئیس جمهور چین  به اقدام ترامپ برای جاگزین کردن عکس بایدن با «خودکار»
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72230" target="_blank">📅 00:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72229">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd32fc6ad7.mp4?token=YBLTEIlbgpeIEa1WQvFUzY-XHpxgzWYe_bvGAEkQ9ENiMzRR-0-1ISWlwEfwYq2dVDdOhpl-SI2e_q9grFzwWwMjPZT_4FILkArhsCoNAe7lsRJqUBdTQw68WC6_bi2BWsFFyoVFCBCt2_okSfyDowzaGyuVDZBg3BteTUzHhjHQGy1vXDJ-c-Ld8vofu7-Xhg0uDj0pB2nVmdk3d1kkqsjlA5JgMJFLn0khHkOrxEj8cmXcfWczB4yIrN8nA_OpwPHZWcVOuYb04J810gpl8S8Kq028RaZctwaja1xSNlmwW0JeBsnMswxTV97w2RmUjHaELVJebr1QZkoD8hGIpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd32fc6ad7.mp4?token=YBLTEIlbgpeIEa1WQvFUzY-XHpxgzWYe_bvGAEkQ9ENiMzRR-0-1ISWlwEfwYq2dVDdOhpl-SI2e_q9grFzwWwMjPZT_4FILkArhsCoNAe7lsRJqUBdTQw68WC6_bi2BWsFFyoVFCBCt2_okSfyDowzaGyuVDZBg3BteTUzHhjHQGy1vXDJ-c-Ld8vofu7-Xhg0uDj0pB2nVmdk3d1kkqsjlA5JgMJFLn0khHkOrxEj8cmXcfWczB4yIrN8nA_OpwPHZWcVOuYb04J810gpl8S8Kq028RaZctwaja1xSNlmwW0JeBsnMswxTV97w2RmUjHaELVJebr1QZkoD8hGIpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با این تحرکات لجستیکی و نظامی آمریکا باید توافق رو قطعی بدونیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72229" target="_blank">📅 23:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72228">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">عجب دنیاییه، پزشکیان رفت سازمان ملل از مردم غزه حمایت کرد، نتانیاهو هم رفت از مردم ایران حمایت کرد
#hjAly‌</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72228" target="_blank">📅 22:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72227">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
می‌خواهم از شما بخواهم که با دقت به حرف‌های من گوش دهید. روزی خواهد رسید، و ممکن است این روز خیلی دور نباشد، که مردم ایران آزاد خواهند شد.
این رژیم خبیث، به دلیل دروغ‌هایش، فسادش و ظلمش، سقوط خواهد کرد. این رژیم ستمگر فرو خواهد پاشید و همه ما در آن روز جشن خواهیم گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72227" target="_blank">📅 22:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72226">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
این یک دستگاه ارتباطی استارلینک است که به مردم اجازه می‌دهد به حقیقت دسترسی داشته باشند، آزادی اندیشه و آزادی بیان را تجربه کنند.
به همین دلیل است که رژیم ایران میلیاردها دلار برای سانسور اینترنت هزینه می‌کند.
آقای رئیس جمهور، من این دستگاه را پیش شما می‌گذارم تا بتوانید آن را به هیئت ایرانی بدهید.
بنابراین، وقتی آنها ناگزیر به ترک کشور شدند، آنها نیز می‌توانند آزادانه داستان خود را در رسانه‌های اجتماعی بیان کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72226" target="_blank">📅 22:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72224">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نتانیاهو: خدا باماست
سخنرانی تموم شد
#hjAly‌</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72224" target="_blank">📅 22:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72223">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نتانیاهو: روز آزادی مردم ایران رو باهم جشن می‌گیریم
#hjAly‌</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72223" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72222">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نتانیاهو: یه روزی که خیلی دیر نیست، مردم ایران آزاد می‌شن
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72222" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72221">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نتانیاهو: نیروی مردم ایران، آخوند رو شکست می‌ده
#hjAly‌</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72221" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72220">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نتانیاهو خطاب به کسایی که سالن رو ترک کردن: شما مدافعان قلابی حقوق بشرین
#hjAly‌</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72220" target="_blank">📅 22:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72219">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نتانیاهو خطاب به کسایی که سالن رو ترک کردن: وقتی آخوندا هزاران معترض رو کشتن شماها کجاها بودین؟
#hjAly‌</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72219" target="_blank">📅 22:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72218">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نتانیاهو: آخوندا می‌ترسن که مردمشون استارلینک داشته باشن
#hjAly‌</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72218" target="_blank">📅 22:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72217">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d451a336d.mp4?token=O7x9uWHAL4sg6quFNtDsCfcSfHn_QcC9vRO_83Rhba_xFe54z0DT9gF7IdlCYB9l-Z0jRw2WZin929tQmPoWzD-_lnP_Aa3YYFjg8tf9UytDPKD6uKxlQzTD2yJTbTvwxJCAdkQXb6LblKHOD1WMi9l4sTzTzUsOra5QjfwaBH-t9g64lZxPpJ09ZaZYNNplJRcVt-9-Jx6yTm-Hid5HGe6Ufc90GBpYGxyiJF2AXrjqpILzN9cR09pjskjN1MyPxjDqu-6-wczizyOEvCNRz5wKNEZjLpJsUQnhk0NsXlNdfJ-65J_ckoxqJRpzW9Xyc9eA3CUQRNW3cIHe6T_nTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d451a336d.mp4?token=O7x9uWHAL4sg6quFNtDsCfcSfHn_QcC9vRO_83Rhba_xFe54z0DT9gF7IdlCYB9l-Z0jRw2WZin929tQmPoWzD-_lnP_Aa3YYFjg8tf9UytDPKD6uKxlQzTD2yJTbTvwxJCAdkQXb6LblKHOD1WMi9l4sTzTzUsOra5QjfwaBH-t9g64lZxPpJ09ZaZYNNplJRcVt-9-Jx6yTm-Hid5HGe6Ufc90GBpYGxyiJF2AXrjqpILzN9cR09pjskjN1MyPxjDqu-6-wczizyOEvCNRz5wKNEZjLpJsUQnhk0NsXlNdfJ-65J_ckoxqJRpzW9Xyc9eA3CUQRNW3cIHe6T_nTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
اخلاقی‌ترین ارتش جهان؛ ارتش اسرائیل (IDF).»
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72217" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72216">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نتانیاهو: هرگز نسل‌کشی نکردیم
#hjAly‌</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72216" target="_blank">📅 22:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72215">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نتانیاهو: آقای ممدانی تلاش کردی من نیام نیویورک، دیدی کیر شدی؟
#hjAly‌</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72215" target="_blank">📅 22:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72214">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نتانیاهو: کیرم تو ممدانی و زنش و دوستاش
#hjAly‌</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72214" target="_blank">📅 22:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72213">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نتانیاهو: ما کلی واکسن و غذا به مردم غزه دادیم
#hjAly‌</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72213" target="_blank">📅 22:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72212">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نتانیاهو: اردوغانِ جاکش، تو هیچوقت حاکم قدس نمی‌شی
#hjAly‌</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72212" target="_blank">📅 21:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72211">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نتانیاهو: کیرم تو ترکیه
#hjAly‌</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72211" target="_blank">📅 21:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72210">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نتانیاهو: کیرم تو قطر
#hjAly‌</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72210" target="_blank">📅 21:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72209">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d2b8c0864.mp4?token=u11Kd2tBJEZwrN_-fEgOZpVoIeJhKad94kTpcwYxZixK6ptbbgMTlAzGCjtI5KyaXD2Y-bhX4seGm21RJG41yWdPCeWe_rk6M4z0jE56zoNaM1B8J9PfAgDTeCQzSDihsa7XmwbIQUGYMGZsNY9BedhnZZwRI8uzkIgKdjaYB_lB8YPKiD6OhGwW-xiDovhSxaGAU4iNVXzpuhOGf0SkSPdBArKjWDmOwIyQP1n2tSp9xJ8K_KjAs9-VLQbGdOTDO6Wc_D406eO_Ac3sfPJ9VhTZ3AmWZhLvVnqYdi-ANeNhABQTClYyh0WmzUf3Gy4Xzr_0Y_MY1jQtqJDOIMbF8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d2b8c0864.mp4?token=u11Kd2tBJEZwrN_-fEgOZpVoIeJhKad94kTpcwYxZixK6ptbbgMTlAzGCjtI5KyaXD2Y-bhX4seGm21RJG41yWdPCeWe_rk6M4z0jE56zoNaM1B8J9PfAgDTeCQzSDihsa7XmwbIQUGYMGZsNY9BedhnZZwRI8uzkIgKdjaYB_lB8YPKiD6OhGwW-xiDovhSxaGAU4iNVXzpuhOGf0SkSPdBArKjWDmOwIyQP1n2tSp9xJ8K_KjAs9-VLQbGdOTDO6Wc_D406eO_Ac3sfPJ9VhTZ3AmWZhLvVnqYdi-ANeNhABQTClYyh0WmzUf3Gy4Xzr_0Y_MY1jQtqJDOIMbF8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
با دوستان آمریکایی خوبمان، ارتش، نیروی دریایی، نیروی هوایی و تأسیسات هسته‌ای ایران را در هم کوبیدیم
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72209" target="_blank">📅 21:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72208">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6173f954c.mp4?token=T4Vl3pYhiKrAyyUdtYo1CHG1YRCfOtrXieAeX8EQvMsjQnw3gzwdPJPIiTrWRMlzR5bkuHl3ri3MdXlX-pmV7N-Zu1yAyaBF48--vPnF3dXIHrrCy7xA7PqxfX9aJeUref-m-cFTsiMqvTbO6UJhEaxcr1H2_q8lMB51ekNqWFgOFxRzp9qiq4y-klNYHaHgZ0dnGYWWW1Wxr9hbjDTSXeIN3jUz_uqRW2uifXMhfEPqZLQn30y_ILkRHUHa2N8ZBZZLwM45_lBDCMiqakAhoakbZMjANAYgBSdrY8hR4PybwNoKIUs1uYT9yVcc2l7DvCge31DuxxAo0HIV1CvJm03kRcmO-YhMcO-hFbLUKBFpHZo2YYwpjo6Owzm8V4RrqGhK96ZAHKKVh5chQ_HkKUyOlBtN8nTEJnIlwu8xLF3KpdxQ6e7jGfBTSa3ST9ySGdlhdYPnI1MDZqo99jm7K2jxX0EP_kZad7JTNlawvNrmigWUF5T2dGleKu1h7LPZRAOKbxk8CQXxuMHBOE51Fvp8hu2hkHcXSFQ0Ra0uxG5lXIVEQWM8imJBhioSPin6n_A7IqVeT6zGOjH7UWMMMY59ruuAVZwOxFWT4ZVm9k3jaFx4qs1DLo29GCQZnBOvHXWdjLfSanWXWO5Yjt0rySY6hO0WyQYkpXWV-EvoYRI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6173f954c.mp4?token=T4Vl3pYhiKrAyyUdtYo1CHG1YRCfOtrXieAeX8EQvMsjQnw3gzwdPJPIiTrWRMlzR5bkuHl3ri3MdXlX-pmV7N-Zu1yAyaBF48--vPnF3dXIHrrCy7xA7PqxfX9aJeUref-m-cFTsiMqvTbO6UJhEaxcr1H2_q8lMB51ekNqWFgOFxRzp9qiq4y-klNYHaHgZ0dnGYWWW1Wxr9hbjDTSXeIN3jUz_uqRW2uifXMhfEPqZLQn30y_ILkRHUHa2N8ZBZZLwM45_lBDCMiqakAhoakbZMjANAYgBSdrY8hR4PybwNoKIUs1uYT9yVcc2l7DvCge31DuxxAo0HIV1CvJm03kRcmO-YhMcO-hFbLUKBFpHZo2YYwpjo6Owzm8V4RrqGhK96ZAHKKVh5chQ_HkKUyOlBtN8nTEJnIlwu8xLF3KpdxQ6e7jGfBTSa3ST9ySGdlhdYPnI1MDZqo99jm7K2jxX0EP_kZad7JTNlawvNrmigWUF5T2dGleKu1h7LPZRAOKbxk8CQXxuMHBOE51Fvp8hu2hkHcXSFQ0Ra0uxG5lXIVEQWM8imJBhioSPin6n_A7IqVeT6zGOjH7UWMMMY59ruuAVZwOxFWT4ZVm9k3jaFx4qs1DLo29GCQZnBOvHXWdjLfSanWXWO5Yjt0rySY6hO0WyQYkpXWV-EvoYRI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
آنها به زنان باردار تیراندازی می‌کنند و خانواده‌های کامل را هدف قرار می‌دهند. البته هیچ‌کدام از این موارد در رسانه‌های بین‌المللی یا شبکه‌های اجتماعی پوشش داده نمی‌شود؛ هیچ‌کدام!
آنچه پوشش داده می‌شود، گروهی حدود ۱۵۰ جوان کم‌سن‌وسال بزهکار هستند که می‌روند و سنگ پرتاب می‌کنند و درختان زیتون را قطع می‌کنند.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72208" target="_blank">📅 21:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72207">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نتانیاهو: هدف فقط پیروزیه، همونطور که داداشم یونی گفت، ما مجبوریم پیروز بشیم
#hjAly‌</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/72207" target="_blank">📅 21:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72205">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نتانیاهو: دم ترامپ گرم داداشیمه
#hjAly‌</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72205" target="_blank">📅 21:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72204">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نتانیاهو: خامنه‌ای دیگه مرده
🔥
🔥
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72204" target="_blank">📅 21:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72203">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نتانیاهو: این پیجر های تو دستم رو می‌بینید؟ حزب‌اللهیا که خوب یادشونه، با همینا دهنشونو گاییدم
#hjAly‌</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72203" target="_blank">📅 21:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72202">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نتانیاهو: خدایی کیو دیدین مث ما که تو هفت جبهه همزمان بجنگه؟
#hjAly‌</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72202" target="_blank">📅 21:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72201">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نتانیاهو: مث شیر می‌جنگیم
#hjAly‌</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72201" target="_blank">📅 21:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72200">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نتانیاهو: سال‌ها پیش داداشم یونی تو جنگ با اعراب بهم گفت ما پیروز می‌شیم، الان من همینو می‌گم، ما پیروز می‌شیم
#hjAly‌</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72200" target="_blank">📅 21:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72198">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نتانیاهو: اسرائیل کوچولوعه، انگلیسی های جاکش که خودشون استعمار رو اختراع کردن به ما می‌گن استعمارگر، کیرم دهنتون
#hjAly‌</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72198" target="_blank">📅 21:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72196">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نتانیاهو: ما به کشورای زیادی کمک کردیم، یسری از همین جاکشایی که الان رفتن بیرون هم از ما تشکر کردن، کیر تو هرچی ریاکاره
#hjAly‌</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72196" target="_blank">📅 21:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72195">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نتانیاهو: نابود کردن تاسیسات هسته‌ای جمهوری اسلامی سخت بود ولی انجامش دادم، اگه این کارو نکرده بودیم همه مرده بودیم
#hjAly‌</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72195" target="_blank">📅 21:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72194">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نتانیاهو: نمی‌زارم آخوندای قاتل به سلاح هسته‌ای برسن
#hjAly‌</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72194" target="_blank">📅 21:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72193">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نتانیاهو: کیرم تو جمهوری اسلامی
#hjAly‌</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72193" target="_blank">📅 21:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72192">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نتانیاهو: بزدلا صیکشونو بزنن تا شروع کنم
#hjAly‌</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72192" target="_blank">📅 21:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72190">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سخنرانی نتانیاهو از این لحاظ که قبل از انتخابات اسرائیله مهمه، می‌تونه از جنبه‌ی جنبه‌ی تبلیغاتی این تریبون استفاده کنه، کارهایی کرده و کارهایی که می‌خواد بکنه!  این سخنرانی تا دقایقی دیگه آغاز می‌شه #hjAly‌</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72190" target="_blank">📅 21:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72189">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teFQhTuw61c7XPbiuxg3vrVTpUJcDKR9onR73Srpo4qdUbAeVi2wC1oVnC9Y6A8A_CxVwTFxU6_g2051vZIP2OKUbrL1TjV6x7PgO4SwKmJiT5NyDVwkWoLNdJ9Sk6II8e3AzihuYuDjjrHD-eyzLxDbgpqN2MsDAvy4sn0yfXqvV0qEwYEo0Pn3lNkt-RHfKHUmm3hghhM5RyPkp6yv5L1uh-O1Itq8OKIsh0QvG-wG1DaD9lqPn-9-9bU5euvLPGLD_xHsJwZCsl-moQcE23bn2ErYFzxwNxOKzp_T2B15ys6glJVI40920YUxKWyfXCErV99ZExCyrglBW4RpMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان درحال مصاحبه با فاکس‌نیوز آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72189" target="_blank">📅 21:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72188">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d7c569da6.mp4?token=kTcnO9GpZWTsbu2nvKRD0cA2NGQBYsHF18eZnSbubXBzUGdwSRSOf8YyFLPch8WuY1b4xBQELeyUiBhTatIJEmqmnxFy9ZSvQB8UhNGTXnshxch0ti6PRkQepyrlm_QHIX1UeVaryCvnljKQmweCiYgkLTnBvnnDisaeXfG1SNVijQyG4-TQ5rw_psq_1H-5sUP00jvMtChF47ozqdk3IF22nK-uqhD2e_ys8AvReZO-fR_3DyRc1E0Cnl_In3-DvFQ2j4e0INoJrTXv15wlnwQQTU_TmfFc_Dps2YHnAJlu99JBayVD1WqDDuT0Cu8OHFqhhjgTSXn64u4HOYODkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d7c569da6.mp4?token=kTcnO9GpZWTsbu2nvKRD0cA2NGQBYsHF18eZnSbubXBzUGdwSRSOf8YyFLPch8WuY1b4xBQELeyUiBhTatIJEmqmnxFy9ZSvQB8UhNGTXnshxch0ti6PRkQepyrlm_QHIX1UeVaryCvnljKQmweCiYgkLTnBvnnDisaeXfG1SNVijQyG4-TQ5rw_psq_1H-5sUP00jvMtChF47ozqdk3IF22nK-uqhD2e_ys8AvReZO-fR_3DyRc1E0Cnl_In3-DvFQ2j4e0INoJrTXv15wlnwQQTU_TmfFc_Dps2YHnAJlu99JBayVD1WqDDuT0Cu8OHFqhhjgTSXn64u4HOYODkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوزوی‌ها به روش خودشان برای بهبود چهره روحانیت در اقشار میانی جامعه کارزار به روز شدن راه انداخته‌اند؛ آنهم با «جوانگرایی»!
یک آخوند مبلغ، طلبه جوانی به نام «رضایی» را به شهربازی مشهد برده و از هر فرصتی برای مالش و ملعبه با او استفاده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72188" target="_blank">📅 21:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72187">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcfa6b3480.mp4?token=SqTtSvw1wgdHNfT12gIbFrlnQ1q7AdTf3oC-4RqKM1flRPGppklMnbrFXB9kb7W7jQ88HjiURGv5EjX2x0aILDneipuFaNYfBx00zroFodjdWwqY2mnuJEr3MA_mREpUV17eTDtrwIQvlztHKQdcacgiQPe3G-rJNkOeTemSFT0SDSAQctKerRdf1AfcJBDg63pUEKEBYJsZwbXfLpjQF2MEQ6m_gc7AlWEFwyl3OlsJaNLAqTnRo5BzPIBGLjdYHbx3OzNP-OO9AI1GyIpS2yfZL5Q6FRYqbSIBYmVmWC5ouK---x2sCHhOh66ERJvg_x3jZpo15-b9i7C9acTJtYpcHsuLEDfNwAf2vVbDp639sxkETkN_QXvZelZDtqI96TsrvEb_m36B4cCGRmS-OkfWMSwEcyMQybaAHhH_tEhT1LAeKw55Pl-fTjfcceMvZdN4zyZoD2cYIXyshrAalIRl9gcttR5iqUxUIJujEjLltvA-DejwwrTcg00ENW3ELBllxV6zFftq84DMDCyYOyRhmtRlFrUXpP91YftjI03XlrnBRQy8dZMvWj1sbTVTf-Ra-FbwyRPhm4CmYiTrkLySPAciAvpZUaMvR3jh1liLxikMXKUM8sbWl3rKzMqEKCc6qCSSxXRBhsDJL8ZqC5ioMSXMTPMcBRbDpEtPRmY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcfa6b3480.mp4?token=SqTtSvw1wgdHNfT12gIbFrlnQ1q7AdTf3oC-4RqKM1flRPGppklMnbrFXB9kb7W7jQ88HjiURGv5EjX2x0aILDneipuFaNYfBx00zroFodjdWwqY2mnuJEr3MA_mREpUV17eTDtrwIQvlztHKQdcacgiQPe3G-rJNkOeTemSFT0SDSAQctKerRdf1AfcJBDg63pUEKEBYJsZwbXfLpjQF2MEQ6m_gc7AlWEFwyl3OlsJaNLAqTnRo5BzPIBGLjdYHbx3OzNP-OO9AI1GyIpS2yfZL5Q6FRYqbSIBYmVmWC5ouK---x2sCHhOh66ERJvg_x3jZpo15-b9i7C9acTJtYpcHsuLEDfNwAf2vVbDp639sxkETkN_QXvZelZDtqI96TsrvEb_m36B4cCGRmS-OkfWMSwEcyMQybaAHhH_tEhT1LAeKw55Pl-fTjfcceMvZdN4zyZoD2cYIXyshrAalIRl9gcttR5iqUxUIJujEjLltvA-DejwwrTcg00ENW3ELBllxV6zFftq84DMDCyYOyRhmtRlFrUXpP91YftjI03XlrnBRQy8dZMvWj1sbTVTf-Ra-FbwyRPhm4CmYiTrkLySPAciAvpZUaMvR3jh1liLxikMXKUM8sbWl3rKzMqEKCc6qCSSxXRBhsDJL8ZqC5ioMSXMTPMcBRbDpEtPRmY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇮🇱
🇮🇱
شماری از نیویورکی‌ها در اعتراض به حضور بنیامین نتانیاهو در این شهر تظاهرات کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72187" target="_blank">📅 21:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72186">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سخنرانی نتانیاهو از این لحاظ که قبل از انتخابات اسرائیله مهمه، می‌تونه از جنبه‌ی جنبه‌ی تبلیغاتی این تریبون استفاده کنه، کارهایی کرده و کارهایی که می‌خواد بکنه!
این سخنرانی تا دقایقی دیگه آغاز می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/72186" target="_blank">📅 21:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72185">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90322c0135.mp4?token=W-O0XwwoZXFt6o-MkQCjFhwTYUrJEmM397zeYI2sVl3Mncp-Xs81P9tVpot69OspDBPeO-Svor87WN57CjHpuq0UamtPln6UgiFTWvcMeZWDHATxopCcIcJOTv_tHWfvbkRiozcGtWl5GbwuaoDM9HHoWbwjWe6ky_uDGsa8I8t_lcx15M7RpqmRvjYDhHfrXMm_-xGuabAYnh6vQuDP7NrZJibYZETdMlO-mCqKci_Rj6_Xk-Pgw0DNlipisfcjNz2_RzIDEEsGj5NNYPzWfDgoFnydfhwpIo2m1HwY5inG_YMB61LCuYelpauw3YITWzIIcs9HNCQLlBFzDwdqOTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90322c0135.mp4?token=W-O0XwwoZXFt6o-MkQCjFhwTYUrJEmM397zeYI2sVl3Mncp-Xs81P9tVpot69OspDBPeO-Svor87WN57CjHpuq0UamtPln6UgiFTWvcMeZWDHATxopCcIcJOTv_tHWfvbkRiozcGtWl5GbwuaoDM9HHoWbwjWe6ky_uDGsa8I8t_lcx15M7RpqmRvjYDhHfrXMm_-xGuabAYnh6vQuDP7NrZJibYZETdMlO-mCqKci_Rj6_Xk-Pgw0DNlipisfcjNz2_RzIDEEsGj5NNYPzWfDgoFnydfhwpIo2m1HwY5inG_YMB61LCuYelpauw3YITWzIIcs9HNCQLlBFzDwdqOTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇺🇸
🇺🇸
🇨🇳
دونالد ترامپ درباره شی جین‌پینگ: «شی در زمینه سنگ‌ها متخصص است و عاشق گرانیت باکیفیت است.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72185" target="_blank">📅 21:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72184">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d872351dfc.mp4?token=kHq2nMCsraU0nKS0Hli0KcXBOBYWk3FzeCvCCCcRD9fjJBQU4YTcIOtJdDBVt469ros2VUXiGG-WPETNwY2uTGtRAbcHDbuqgDwaTgQ51x6j_DEkm8yOmPr8t_h_GizTJ0c2AkSkcvlLAD3rT1Us0rRxOs1hLfj_3GWfBhUB5b4F_6m910rcaMULr5Wl3J6zhGoo9-_jibts_ee0zKQAqaJr99x6mGLMPVAsQyC9SsBfQ9q8lxmYQn4wrNqWu3EfyPkP6tKFaEIFAvlr9nYqzTZDb0AstX28OUixvKArWPpCEjwtaVfKk0emHWkVyP5l0eWk7yMi4uu8Ui6xMVaul1jDR-HvF_T6UVhMsNWUCN6aM6reudjQL0wdKxv60pee5XsdtZ65eFjrjOaunKw4CKXdeQzJ_mLSEwDuUjrKQxKl2-CPdjt6aCidOQNDCxcDbZX0TRGWb0isMjG8X1bxE4N3ucRfLz2XSOHeoY-XrGHuXaMm8u5aX8bdciQQ85QBms90b0ufkIVjXfiGUmx4jSF3Jqckv7j56Z1jxRaRcz3u2lpV1HNB_UfgHuzr1PUlu9l71wvLMU17JSPjEwI4aouH8cc9CDfKN-5r18JKJvFbnPTNlQ32sHiv5BdrpSQ2uK9XQvM6ZUQP5LA4oJ0kz0pYQtEJHc9qzsFOvX8Niak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d872351dfc.mp4?token=kHq2nMCsraU0nKS0Hli0KcXBOBYWk3FzeCvCCCcRD9fjJBQU4YTcIOtJdDBVt469ros2VUXiGG-WPETNwY2uTGtRAbcHDbuqgDwaTgQ51x6j_DEkm8yOmPr8t_h_GizTJ0c2AkSkcvlLAD3rT1Us0rRxOs1hLfj_3GWfBhUB5b4F_6m910rcaMULr5Wl3J6zhGoo9-_jibts_ee0zKQAqaJr99x6mGLMPVAsQyC9SsBfQ9q8lxmYQn4wrNqWu3EfyPkP6tKFaEIFAvlr9nYqzTZDb0AstX28OUixvKArWPpCEjwtaVfKk0emHWkVyP5l0eWk7yMi4uu8Ui6xMVaul1jDR-HvF_T6UVhMsNWUCN6aM6reudjQL0wdKxv60pee5XsdtZ65eFjrjOaunKw4CKXdeQzJ_mLSEwDuUjrKQxKl2-CPdjt6aCidOQNDCxcDbZX0TRGWb0isMjG8X1bxE4N3ucRfLz2XSOHeoY-XrGHuXaMm8u5aX8bdciQQ85QBms90b0ufkIVjXfiGUmx4jSF3Jqckv7j56Z1jxRaRcz3u2lpV1HNB_UfgHuzr1PUlu9l71wvLMU17JSPjEwI4aouH8cc9CDfKN-5r18JKJvFbnPTNlQ32sHiv5BdrpSQ2uK9XQvM6ZUQP5LA4oJ0kz0pYQtEJHc9qzsFOvX8Niak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو به مقر سازمان ملل در نیویورک می‌رسد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72184" target="_blank">📅 20:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72183">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fcd656bf7.mp4?token=d75cbENqfC4k8wlXZPWwkz0oYaB4_gEFKUauHPGKQwFb4k9c3xeiMbXmx84RVubv7Lf18JIelfX_Utdd27yexsCUxzW8U0uc58Ah2TdKdURWfFHTzQbE9gTS8luPZRco2QIeBL9PEWKFwCEKz8mbjZ-WX6liIanJmsZGENHSJHL3QfgNW43I0PZ6IrQaGPmCwgGjaZGzC-d0mONkr_TUCs5kU19rlPBhuXOpPLkT3Q0z9gDZ-qtRCZCOAyfUBZfz85OC6E5KAlYHGu12BW64nPMLJbbpfbv0YolQxKRMzad5vNkjcWNy6F8yAdHFWF1LN4cqMYrlm38i04coCjQzNKTzWvqYVO5Y4RWXMDRrE0uicTUxg7U6d0udctsqUdRc-cip_z39Fi8QhS3M4UzdNOwv787lNM1tRNjQioo3hNE8k_dOQpqilmbGEwttcC0Mw3jmCHDAQ3GKkb-zXPzQpW9D2aPYcZF1nHmBcUnPC1q4r6umFBACkw9SnHth90wI2Q2tXJQh5VdKZZD-D4eGcIly2Bt8OwLMXqRf0j8PFSmKGDWpJF1-zHFoJe27Ki2Knuu0TW35Cc-clVkhez-mI3UAj1qmBvNjUxLm7eugH2qrgbyzcWJtCqo0vCFseQDmKfzPrVOgBIhKCBe_YhICq1BHQ6B1Jjcr_8I0Gfvh-Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fcd656bf7.mp4?token=d75cbENqfC4k8wlXZPWwkz0oYaB4_gEFKUauHPGKQwFb4k9c3xeiMbXmx84RVubv7Lf18JIelfX_Utdd27yexsCUxzW8U0uc58Ah2TdKdURWfFHTzQbE9gTS8luPZRco2QIeBL9PEWKFwCEKz8mbjZ-WX6liIanJmsZGENHSJHL3QfgNW43I0PZ6IrQaGPmCwgGjaZGzC-d0mONkr_TUCs5kU19rlPBhuXOpPLkT3Q0z9gDZ-qtRCZCOAyfUBZfz85OC6E5KAlYHGu12BW64nPMLJbbpfbv0YolQxKRMzad5vNkjcWNy6F8yAdHFWF1LN4cqMYrlm38i04coCjQzNKTzWvqYVO5Y4RWXMDRrE0uicTUxg7U6d0udctsqUdRc-cip_z39Fi8QhS3M4UzdNOwv787lNM1tRNjQioo3hNE8k_dOQpqilmbGEwttcC0Mw3jmCHDAQ3GKkb-zXPzQpW9D2aPYcZF1nHmBcUnPC1q4r6umFBACkw9SnHth90wI2Q2tXJQh5VdKZZD-D4eGcIly2Bt8OwLMXqRf0j8PFSmKGDWpJF1-zHFoJe27Ki2Knuu0TW35Cc-clVkhez-mI3UAj1qmBvNjUxLm7eugH2qrgbyzcWJtCqo0vCFseQDmKfzPrVOgBIhKCBe_YhICq1BHQ6B1Jjcr_8I0Gfvh-Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز یک بمب‌افکن رادارگریز B-2 و چهار جنگنده F-35 Lightning II بر فراز کاخ سفید در جریان سفر رئیس‌جمهور شی.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72183" target="_blank">📅 18:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72182">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wj1dZ-ZAPByxSVL8ldzaTGiBXc1ecNiXQ2pgVptn847DAjjufQVcNG5U9XnbDQB_qZWdw5-lbY1BfZM8SOePdEcgVTYHySNBuJr5bMK93DheqRpjDxFemmq2crerhOKVOdqYiQpCm-YXc2qIrmYacH6GGUFD8nS4hXhCIHWShRXFXvAUqUCQ_7pOa5nekfrTYyxeBX38SnGBiLyIpTBsHX3EwJgPoow3vNG_6SW9BICVRFIRRFwYtUc5rl-4BbykiRRSQZOCUhGM1bq2na-SU2OfimAzLY-rZpVqqTQJSl960TUyeckJ7ABKZjPb2mhJbNWTKW0Iiej-J4D8ilS20w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانکر ترکرز گزارش داده است که نزدیک به شش میلیون بشکه نفت خام توقیف‌ شده ایران به ارزش حدود (600 میلیون دلار) در حال عبور از اقیانوس اطلس به سمت خاک آمریکا است!
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72182" target="_blank">📅 18:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72181">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41a961ea41.mp4?token=vqPXVLNbGG_4snu4VpeRNP-SnpDXBiXzyaQn5mW6EHgRr0B53izAtAZ0jwMNI9VkiNBWf668Xe6wKnbPrXHHd5RgtXKasvH_k8wX5MHhi85uqpRcT2u_px2SERWWFAAQctzfAM0eyvJx6tq0A-NNnL5MdQV0HdjUe5FyOkKKgPB50troSnjDeMbZCSWBrpn-6n-VefQTGCE0I-92HUC95TP9PZ6KsTFmjtKMmhm8LRSLsEi2q-iVP2yyApJ-js3VDIoF2fjRcR_Sqy_4J31VPHqszh8pfYmsS1xwMy5NCcNFWX9SYgSnkMRmci2NSx6HOnEhdzEROLhASr9ETsVzrG8A5NgucSDG0SL01EWULQef3YwDUBYJ2I2r7i-Yxz3Sy9xYNIQAM545JPNjbf0leHMsnAnYxKKp-tNRbF10Ye13Gzfx-mxa5LhgPZmsJT2yyi04ZBUj6LdVd6I_3Pyj-55_MXsowFg4sHMqtyUNS_yDVrwM1yNzBCvAjiwDuqnKisO2QI69S4FEyEYzEva_nTKGYne3x4N0oIevthSpHMMx0tY-xws_9MTufwd5MKPVdBg7qyBTe-ZlPokpfaVG6MkCYsccTUq0PF-T6rWFynkLSOha51NZvh7Jzje4RvH9fsL5ruayVSsbrZuS2XNvCVwjhUhSo3dYP8kUnJlIYIs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41a961ea41.mp4?token=vqPXVLNbGG_4snu4VpeRNP-SnpDXBiXzyaQn5mW6EHgRr0B53izAtAZ0jwMNI9VkiNBWf668Xe6wKnbPrXHHd5RgtXKasvH_k8wX5MHhi85uqpRcT2u_px2SERWWFAAQctzfAM0eyvJx6tq0A-NNnL5MdQV0HdjUe5FyOkKKgPB50troSnjDeMbZCSWBrpn-6n-VefQTGCE0I-92HUC95TP9PZ6KsTFmjtKMmhm8LRSLsEi2q-iVP2yyApJ-js3VDIoF2fjRcR_Sqy_4J31VPHqszh8pfYmsS1xwMy5NCcNFWX9SYgSnkMRmci2NSx6HOnEhdzEROLhASr9ETsVzrG8A5NgucSDG0SL01EWULQef3YwDUBYJ2I2r7i-Yxz3Sy9xYNIQAM545JPNjbf0leHMsnAnYxKKp-tNRbF10Ye13Gzfx-mxa5LhgPZmsJT2yyi04ZBUj6LdVd6I_3Pyj-55_MXsowFg4sHMqtyUNS_yDVrwM1yNzBCvAjiwDuqnKisO2QI69S4FEyEYzEva_nTKGYne3x4N0oIevthSpHMMx0tY-xws_9MTufwd5MKPVdBg7qyBTe-ZlPokpfaVG6MkCYsccTUq0PF-T6rWFynkLSOha51NZvh7Jzje4RvH9fsL5ruayVSsbrZuS2XNvCVwjhUhSo3dYP8kUnJlIYIs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ از شی جین‌پینگ در کاخ سفید استقبال می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72181" target="_blank">📅 18:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72180">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72180" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72180" target="_blank">📅 18:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72179">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZndKmgMYnYTT-Xys8WjHP1lwRRjGXobczyKni3oWtMkDuVODfPghrAJUUydQlaVoTLrAyLZoGlPKhVLO6s_m853RZViI6WP_okn1OhUrtLv4itdnYS8Fup8QQLRK-ZfClong1vytTrKV4OYpJSLbNkaGFzekDENaJcZRZecKkmgljoLeIAJTLYbwnsrtwE4cG5_P24B9irNaqcawNpF2rqVUp0bNs17zbV3Pjo0_n7W52fgCttB7YpWxt_-Rpo0M4UDpVAcExzCoON7ufDHblfPVy3RgCGPlpLDnoE-EDuST9M6-bOqkTKdXIcnX-5I0Jrb2_GBT89aEWszZB9pkUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
ولز
🆚
پرتغال
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
ولز: ۱ برد، ۳ تساوی، ۱ شکست و ۱۱ گل زده
پرتغال: ۲ برد، ۲ تساوی، ۱ شکست و ۸ کل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72179" target="_blank">📅 18:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72178">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffI3scvaGt02E_-HTGpaXT8Np8q3Co7ld2eGIPctCpUBwJrJLBfk7Y9RYn3W_jNPPxbAqX6E5tCGuZsd8tWzZZmlgJItPWAqOQFnML5QSxoQBzKNqaS8ouNQ1_eOF8nGCD_wrhYFZiw4vDMNV5RC12CBkGxKUiG2-woVS3Qj94KSyUcrLlRHVwXJHxVWIutZWZjM74YILxIQZ_FfoQCvfWAC9WLZcGBb6isoG4myjoo1Cbt796v50cKN1dkL4wt-j0QiHdqxm-RQXqnWsBwPNNDZjaz0kvMu9_ThtKOF83UCv-ba65gTbGY4_zR2Brw-HXd9A5Y5h9sFPoIxOYDU4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو برای شرکت در مجمع عمومی سازمان ملل وارد آمریکا شده است.
او قرار است امروز در نیویورک سخنرانی کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72178" target="_blank">📅 17:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72175">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fibLwHkFfUHdlLIHUrct7gbRE2vlc9kNXGalZ5rkvb1bQKgZcbQP65zqkp8x8OglCuXV42V6TOP-OQDEOxqAbec9QKJeS1e7VQTUZrZN0HXF7a3l1JAkjT26cJaGyW5xf00Dzb8pyWypfQENOcpNqKijhfs8auTBrflxBmn30UYsMK3iVHvBz0q-cZLtKS32vOhuK2ltMjm18IwYfP_Kfa02nWVVQELn3XfDsO0s9hYOM1EF0O9ewqUBBt0UmyYUwi7WTiRNiarKHD9IB-8i4-fwp8HHKYpSW0KH7z0iwV4avhK4SA-u0qdqPWGExeuVceGxPA148KvZLKuMcuYhwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YOg7OMcV7a1iJB14W-3MfQMKozDvOY_Yy9Jx4-f-7RJuAak_RBA09VIO-aS7MKXt_9mbK16sin_hPFRwISKdZVMv8TKAqYQt4kd5ZnMYpkHtgwkq68kw-G2F0HOqfXrwsQQ_J0WGcRxEz17pSou1cwDD-wM9-KnPbXiTfdcaSm2LpJImzf4HWTdd5Xy1XewK1zwhuzW7BFAmujI72wwuJiUNr1pyDpqT6RVENoeCQHxupbMk1dMc7DrE1BwEZWPa8e_ikiBflGMdThXpfqwaUw8s8j8gsb8FFBgUKstm6WkiUBZuHWlP7i_x_vLJ3u5Ega2UhjSx4la_2CHpyeLFtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e7959de70.mp4?token=ZhguuaVX9jYQROVkWS7N2tFlrrKJL6lx8pN8zJRWH1w_LQbquK40SsEN_YZ3tZdk_hElCrVtx5MdYG9zUsP16rO2mXApwSbf2j1cYrXvdf4sbEtABnCXdWxU-UQB2FtckLxkB-pb8pTRFVaMdN7usPSfFxYbnBCAmqGhi5UO5iO6Sw7Y5O9hz7bvRzljTxEbKG6NDHPWIS0EbOMpJXq_BSAPmJ7dzRGQaxv3d7E9m6X-JSXsgAqvzKRFGHQPwcGq-e1EvjOkjDA3WGwidwlYcJ37DntuuA4OcPRUCjkWHrfTT0xkYyfgjfVUFquW7ec9b4kBRJCskjXgd-c2-yB_AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e7959de70.mp4?token=ZhguuaVX9jYQROVkWS7N2tFlrrKJL6lx8pN8zJRWH1w_LQbquK40SsEN_YZ3tZdk_hElCrVtx5MdYG9zUsP16rO2mXApwSbf2j1cYrXvdf4sbEtABnCXdWxU-UQB2FtckLxkB-pb8pTRFVaMdN7usPSfFxYbnBCAmqGhi5UO5iO6Sw7Y5O9hz7bvRzljTxEbKG6NDHPWIS0EbOMpJXq_BSAPmJ7dzRGQaxv3d7E9m6X-JSXsgAqvzKRFGHQPwcGq-e1EvjOkjDA3WGwidwlYcJ37DntuuA4OcPRUCjkWHrfTT0xkYyfgjfVUFquW7ec9b4kBRJCskjXgd-c2-yB_AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هوایی اسرائیل منطقه «کفر تبنیت» در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72175" target="_blank">📅 16:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72174">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb1a6b62b.mp4?token=G1w0Ob23QLvbjIulKoZj6OijSZTMSHgjtzaFWTN3279uUjK0rUohF2po41ET-i2MC_NK-mMW9zVK0Snv7rtEAQl_PPpNipmNNZ_Iyob2SfX-5HzkL1o0APvr1UIVI7arZs14f-xNL1Nx-vy5bzih9N-JbIOG7pty1uuVl7VTitfpFrWVNeyIuuL4HKgM07A4JWV3qa78HYSZdBc9Oh7OqR6jlYJH82Q__DpKg1raq57ifuzeXIs39q4Ogljkd5P3-7VK2Acj7bYNkspeQWIaMDxKOIznj0huKF72cZcCoP5hdzsDtQT84RVvjUhvsMGFRReHYUoXoDDmylDpEMlyIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb1a6b62b.mp4?token=G1w0Ob23QLvbjIulKoZj6OijSZTMSHgjtzaFWTN3279uUjK0rUohF2po41ET-i2MC_NK-mMW9zVK0Snv7rtEAQl_PPpNipmNNZ_Iyob2SfX-5HzkL1o0APvr1UIVI7arZs14f-xNL1Nx-vy5bzih9N-JbIOG7pty1uuVl7VTitfpFrWVNeyIuuL4HKgM07A4JWV3qa78HYSZdBc9Oh7OqR6jlYJH82Q__DpKg1raq57ifuzeXIs39q4Ogljkd5P3-7VK2Acj7bYNkspeQWIaMDxKOIznj0huKF72cZcCoP5hdzsDtQT84RVvjUhvsMGFRReHYUoXoDDmylDpEMlyIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غذای مجلس ترحیم، اگر خود مرحوم. این نوع غذا رو خورده بود حداقل ده سال دیگه زنده می‌موند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72174" target="_blank">📅 16:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72173">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d6256f78.mp4?token=vebAuKPnK1yKOHVKN4cne0ZCx3PmGVudx2ln4tHbXZzgZHYWs77josXPUVIwTjBuBAvKXptVULs9l2vnBfz4NwEWBmy-3jo6zLCuGnT89Q88c-QkyKI_jh0sC1_v76vPpm9T0r8ClLigw2k0Jkh-bkmHgtpcE-v7EbNAEqQLgthjXpXIstADLwL_k-SamSZCXb3J5tFMueX5u4DFm_j3ATUhiJID_wtbSpCYSIsb9lY1l-4F75aMWdvDDi3tBaWa6ytldRQsaXgIp11lxiiXVzNfc49qyzTqnzsQlD485NfR2g8jLmqa7nSawwuKcQzEYRl7zF94AXz8Yu8oq3gwNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d6256f78.mp4?token=vebAuKPnK1yKOHVKN4cne0ZCx3PmGVudx2ln4tHbXZzgZHYWs77josXPUVIwTjBuBAvKXptVULs9l2vnBfz4NwEWBmy-3jo6zLCuGnT89Q88c-QkyKI_jh0sC1_v76vPpm9T0r8ClLigw2k0Jkh-bkmHgtpcE-v7EbNAEqQLgthjXpXIstADLwL_k-SamSZCXb3J5tFMueX5u4DFm_j3ATUhiJID_wtbSpCYSIsb9lY1l-4F75aMWdvDDi3tBaWa6ytldRQsaXgIp11lxiiXVzNfc49qyzTqnzsQlD485NfR2g8jLmqa7nSawwuKcQzEYRl7zF94AXz8Yu8oq3gwNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این آقا پسر برای تولد دوس دخترش ۲۰۶ خریده و اینجوری سورپرایزش میکنه :))
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72173" target="_blank">📅 16:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72172">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a803db071d.mp4?token=iBBWkBBuJn6PxZkaHV-KYECtaPq9jmo3PqSpW-q3Mwxg5mLU64VeVsxxXgiMuA135YzizACNuQ8wFCgmzFGvjmjO_dVcs41j9jMUzWXF2EozSoZCwIunuD06xWwNHyrfmPBgpZ6VnBWKmvveDTV1F3amDyvTkGUB_5tiTkGyfhXT1UgLhO5aT2IwzmmCmkIbQBTR0gqJX4Cg7NcHDQvY4G12oRTIPReRvpTA16lsFSqOFEB_gek4C5h5QqJGE81It5ag9s06fdgAyaNHNO9Onsl0t3jioO3Q7-e5mQB956jvOdVwXfumgfVBozOg718YDVbS1X_bnPSITYck-RPuOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a803db071d.mp4?token=iBBWkBBuJn6PxZkaHV-KYECtaPq9jmo3PqSpW-q3Mwxg5mLU64VeVsxxXgiMuA135YzizACNuQ8wFCgmzFGvjmjO_dVcs41j9jMUzWXF2EozSoZCwIunuD06xWwNHyrfmPBgpZ6VnBWKmvveDTV1F3amDyvTkGUB_5tiTkGyfhXT1UgLhO5aT2IwzmmCmkIbQBTR0gqJX4Cg7NcHDQvY4G12oRTIPReRvpTA16lsFSqOFEB_gek4C5h5QqJGE81It5ag9s06fdgAyaNHNO9Onsl0t3jioO3Q7-e5mQB956jvOdVwXfumgfVBozOg718YDVbS1X_bnPSITYck-RPuOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور هائیتی در مجمع عمومی سازمان ملل خیلی جدی، از پارچ آب نوشید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72172" target="_blank">📅 15:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72171">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b973e065b.mp4?token=RDY-lyikCQzGGj-4BveWjdKG4-b0DBTU99uLK0jN5d0In0AdJuaUr1mpUvUgj1n2GGFAEMRg5njJqKHB6cJpno52iYFp616apU0H6xqhIdoFc6Ra8Slv_JK_sWZBA_pP3EJ_td4uzVtdbaKRe0Gd1HhJdkXHoHbMcCglWeDvI0hYSx-qrKgM7m7ePX_gfS1RLYlzW-LB1N4TF7HZ1ftOIY5rnZKjBBD9GmgOoEZJh9-hsTI03mVs-QX_SPCOeoFW4m6lJBP_Zt0tsok9h4EmE1qzyqpx37Ifmet4VmPWAYTI-2eAyX_RgHgkJZyh9DBp29t1yikXH-l13Ohn4_F4DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b973e065b.mp4?token=RDY-lyikCQzGGj-4BveWjdKG4-b0DBTU99uLK0jN5d0In0AdJuaUr1mpUvUgj1n2GGFAEMRg5njJqKHB6cJpno52iYFp616apU0H6xqhIdoFc6Ra8Slv_JK_sWZBA_pP3EJ_td4uzVtdbaKRe0Gd1HhJdkXHoHbMcCglWeDvI0hYSx-qrKgM7m7ePX_gfS1RLYlzW-LB1N4TF7HZ1ftOIY5rnZKjBBD9GmgOoEZJh9-hsTI03mVs-QX_SPCOeoFW4m6lJBP_Zt0tsok9h4EmE1qzyqpx37Ifmet4VmPWAYTI-2eAyX_RgHgkJZyh9DBp29t1yikXH-l13Ohn4_F4DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشماتون بریزه، ایران شده مهد عجایب خاورمیانه؛ این آقایی که می‌بينيد لاله گوشش رو سوراخ کرده و یه مار کرده توش.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72171" target="_blank">📅 15:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72170">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e89ab3721.mp4?token=u8jqRboLJloR6GpnBr-26clB11NqByNBEh2YFaZegHIM1MsQK5nXhEcRBSIoe_6glyN7Mjsj3J-sP9kuDFD9OxnEzeMJW_b4bOQ_Muxvw_XXpDLc68MdYVJItaLK8s8fQPcN5Wy28Nmeo0Txg4kpXQSK470TavN2Bh3T2bj2OttYQYs7Fdt71-4_hlGVsGKQBqT9LXAQ8Pt0sf8xc9OVRyCcOVdtuQ_C7BjUdX_xV_cwtyrSs9IQRtTJDRQDpr20WE895vSusIBev0836t27QXcygUpySsSsbf-xUNVw8RPPl2acNT0CWIIXTWKljx68Ymi1nJId8zNRMZHU3qTdvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e89ab3721.mp4?token=u8jqRboLJloR6GpnBr-26clB11NqByNBEh2YFaZegHIM1MsQK5nXhEcRBSIoe_6glyN7Mjsj3J-sP9kuDFD9OxnEzeMJW_b4bOQ_Muxvw_XXpDLc68MdYVJItaLK8s8fQPcN5Wy28Nmeo0Txg4kpXQSK470TavN2Bh3T2bj2OttYQYs7Fdt71-4_hlGVsGKQBqT9LXAQ8Pt0sf8xc9OVRyCcOVdtuQ_C7BjUdX_xV_cwtyrSs9IQRtTJDRQDpr20WE895vSusIBev0836t27QXcygUpySsSsbf-xUNVw8RPPl2acNT0CWIIXTWKljx68Ymi1nJId8zNRMZHU3qTdvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چهره ترامپ وقتی B-1 لنسر وحشیانه از بالای سرش رد شد دیدن داره
🤣
انگار اصلاً نمی‌دونست داره میاد
😂
قیافه شی رئیس جمهور چین دیدنیه
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72170" target="_blank">📅 14:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72169">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAGwXhtDlgzUiIgpEKR_YPVkOi2wQB3JL1pFxfwQOjwOkEOI-Ilfw71Q4p_WQaYaBu69BVPMP27t80DjfkJ_mRlvfoaY-4soWt9dDwMziGQ1umZgUYf51eSjOVAnne9CnKk7JLEIF0pHKMfL2rCTYhf4rZ-KX6i7DaVSz8M5SMCzrlo3oz3EKeJystCctFu5LxPZ_oZt6woO0FNFLRUPTWjmN8jf7K1NOOuvVHqooLyamMKpDBDl6KDs8lnFX-nV-h1wCHs-o4l2Q-C2tbFutW1-IKPhE-Ji_VP2YsoiId-butUXeniayZNWdn0cRtA9koVgNbIg0ZGs9tbr-6xB2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش ایسنا و به نقل از سازمان هواپیمایی کشوری ایران، تمامی پروازهای شرکت‌های هواپیمایی ایرانی به مقصد امارات از نیمه‌شب لغو شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72169" target="_blank">📅 13:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72168">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f0e98c345.mp4?token=AO51_RrWOgivMK4hdVmIsL4TKMrLqZskGenuROzJ4xaL9yCjf1kO0Xr2U2XWFNLkR9XX9LG8qlHvA9t_cDl80uTXwwKhgRhJPv9MwqO8k9brSC4V6Y8uOQAxzRBescVbUXI_gWf901dwk1LYhH0tMRBAcECIvLUT3y1kBZWaSufnNxbSDgSSE-Lu8Wq5NVJ50fVJkkuGJD2cJW60ixyg-jH24PhFpxpSBkwURcPf2S_gpMgSxQnX5VuDZMfXFKAOwHkbm3n8P-WFxFdF_1Q6SA_dpb3SX2D2uq0JDUDFxebQJEA_xb9P6o8TzyxbXZEWpbLR3WKuojtFDsaRmbNyP173xWHKkagPR7sklOC0-U5CBBDgH6656RUqoUISP259Fon7VGUGFpuqP9NM05T3ebxPpFM6dO9lBlqbIWm7YkqFp-_Hdo2Zl0H0Bo_MobfZwsYTzNqelBUb30rvpE1_g_GGfYPB8c8oXYLmyZYeIEiYT1kNp98UKXZ9ZIw3CFMbdydT4wuVqMSLh_mKEZN40sbLnAF8BmxtCvtuI2zr3A2_RG4eGFEI20rd2mpgEslo6x094lZ2hTqUzR-G3EeQYrP-P3afV-VHzltGnyfl04dUPA8WNE1guvmtHLX8YY8WHli1_gr1FfEgb4_cxctyqAFP73ud1O4PtvM4nLBEGzI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f0e98c345.mp4?token=AO51_RrWOgivMK4hdVmIsL4TKMrLqZskGenuROzJ4xaL9yCjf1kO0Xr2U2XWFNLkR9XX9LG8qlHvA9t_cDl80uTXwwKhgRhJPv9MwqO8k9brSC4V6Y8uOQAxzRBescVbUXI_gWf901dwk1LYhH0tMRBAcECIvLUT3y1kBZWaSufnNxbSDgSSE-Lu8Wq5NVJ50fVJkkuGJD2cJW60ixyg-jH24PhFpxpSBkwURcPf2S_gpMgSxQnX5VuDZMfXFKAOwHkbm3n8P-WFxFdF_1Q6SA_dpb3SX2D2uq0JDUDFxebQJEA_xb9P6o8TzyxbXZEWpbLR3WKuojtFDsaRmbNyP173xWHKkagPR7sklOC0-U5CBBDgH6656RUqoUISP259Fon7VGUGFpuqP9NM05T3ebxPpFM6dO9lBlqbIWm7YkqFp-_Hdo2Zl0H0Bo_MobfZwsYTzNqelBUb30rvpE1_g_GGfYPB8c8oXYLmyZYeIEiYT1kNp98UKXZ9ZIw3CFMbdydT4wuVqMSLh_mKEZN40sbLnAF8BmxtCvtuI2zr3A2_RG4eGFEI20rd2mpgEslo6x094lZ2hTqUzR-G3EeQYrP-P3afV-VHzltGnyfl04dUPA8WNE1guvmtHLX8YY8WHli1_gr1FfEgb4_cxctyqAFP73ud1O4PtvM4nLBEGzI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:جمهوری اسلامی در نهایت تسلیم خواهد شد.
نمی‌دانم یک هفته طول می‌کشد، یک ماه یا دو ماه، اما آن‌ها سرانجام تسلیم خواهند شد.
هدف در اینجا می‌تواند یکی از این سه حالت باشد:
اعضای رژیم به جان هم بیفتند؛
نوعی قیام مردمی در ایران شکل بگیرد؛
یا اینکه ایرانی‌ها را متقاعد کنیم که اگر خواهان توافق هستند، به آن پایبند بمانند.
این بار، اگر توافقی حاصل شود، تضمین می‌کنم که آن‌ها به آن پایبند خواهند ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72168" target="_blank">📅 13:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72167">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb27b8d8bc.mp4?token=VbF8QtOVr-jUZJIchRw-nV-2_NPYBIMvlzAXwT8UzWT3cTpNX2Xu2j-04fd2gSO2Ziu0sFOTnlR_N2nUJHgT6CfTFldJrkK7V5P74JpXNDvOwNf-YLBDQUY3Ftgex0WkjTQbGYC0fOG_0DSQVUa3vUHvUhzDb6QD-952ZKQxHslnwYSjl9Ua3cPADiCozNap-C5IU6mKdpO6upjhY8pnr234_mEct1V8m_BM9knSr5JnLzNtQ5kb6a_FsRWQgwCuQz-7q8oNOd9ICyo5qi2t76YN7UP1AcgN-kEeQIwF9C2FeRl4VDEaEiTNWk_yFy39S8RsKG1Ujoi_ZjyegBv87A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb27b8d8bc.mp4?token=VbF8QtOVr-jUZJIchRw-nV-2_NPYBIMvlzAXwT8UzWT3cTpNX2Xu2j-04fd2gSO2Ziu0sFOTnlR_N2nUJHgT6CfTFldJrkK7V5P74JpXNDvOwNf-YLBDQUY3Ftgex0WkjTQbGYC0fOG_0DSQVUa3vUHvUhzDb6QD-952ZKQxHslnwYSjl9Ua3cPADiCozNap-C5IU6mKdpO6upjhY8pnr234_mEct1V8m_BM9knSr5JnLzNtQ5kb6a_FsRWQgwCuQz-7q8oNOd9ICyo5qi2t76YN7UP1AcgN-kEeQIwF9C2FeRl4VDEaEiTNWk_yFy39S8RsKG1Ujoi_ZjyegBv87A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی دبیر شورای عالی امنیت ملی رسما فرودگاههای کشورهای همسایه را تهدید به موشک‌باران می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72167" target="_blank">📅 12:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72166">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd3cb8e2e.mp4?token=F8YSFgrhVwUNP9NQFtsiQGzbSdrUoS6GCSHAZp3tyrOVSMAvUJMWX5t92FAJ1v5Idhg8VP8o1Q91M3_VBRfkq6ZQn9zUvDZqS5jzHcABMh9t8Qlh15J3Sjiw0m2M9odQEz6iXLmdDJkY3epu4O72BG7CkFlKjs05zFxW3q9P8HVzgT6cHc9uGpBuwN6o2W8kTIwvi7ObUXOu0AsueGTbqign9vIMgK72u5d3E062eh2DhNL3tSWTU2JZBkR1UUt0W3EpM1KZiXZGLsbRMLmjdfefCEJMI7Z6zbL7H6cruxmsgtijVbOFyqU2JUn_5-AJkUop5dU_mkvOohbtEgAgHn_N9iBlADjdWozl2plaPkfnYzt-z78-XWfNPCXLTJDLLNPgCClJutRyD-3DAGOvTQ1TTDetETGDuiYc1OHShZQDmDKnmcKO5J-fRT4G2YbWOB72TFYXpKYjKcxZniQsgdRecZFKZTzE6UhrgSnPw-axux6Pk18PT0ibnoMrun4ABdGiXrWUggiIe748vMhaPAyQVtNx2kgVZYODsl48YN8KoFQ0tyjGK7Uqfys2JvZAtdKXYjqZpeFES2xJhIFap2HQj_a4wwt2GvWTmPqGLbmKtC3wndo2gHTAQAhx-WxU3sRgO7avP13segTlrba9S3-CP2lzq-zrHdsk2MGD9JE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd3cb8e2e.mp4?token=F8YSFgrhVwUNP9NQFtsiQGzbSdrUoS6GCSHAZp3tyrOVSMAvUJMWX5t92FAJ1v5Idhg8VP8o1Q91M3_VBRfkq6ZQn9zUvDZqS5jzHcABMh9t8Qlh15J3Sjiw0m2M9odQEz6iXLmdDJkY3epu4O72BG7CkFlKjs05zFxW3q9P8HVzgT6cHc9uGpBuwN6o2W8kTIwvi7ObUXOu0AsueGTbqign9vIMgK72u5d3E062eh2DhNL3tSWTU2JZBkR1UUt0W3EpM1KZiXZGLsbRMLmjdfefCEJMI7Z6zbL7H6cruxmsgtijVbOFyqU2JUn_5-AJkUop5dU_mkvOohbtEgAgHn_N9iBlADjdWozl2plaPkfnYzt-z78-XWfNPCXLTJDLLNPgCClJutRyD-3DAGOvTQ1TTDetETGDuiYc1OHShZQDmDKnmcKO5J-fRT4G2YbWOB72TFYXpKYjKcxZniQsgdRecZFKZTzE6UhrgSnPw-axux6Pk18PT0ibnoMrun4ABdGiXrWUggiIe748vMhaPAyQVtNx2kgVZYODsl48YN8KoFQ0tyjGK7Uqfys2JvZAtdKXYjqZpeFES2xJhIFap2HQj_a4wwt2GvWTmPqGLbmKtC3wndo2gHTAQAhx-WxU3sRgO7avP13segTlrba9S3-CP2lzq-zrHdsk2MGD9JE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«پرواز هواپیمایی وارش» از «تهران» به «دوشنبه» _پایتخت تاجیکستان_ از مرز هوایی لغو شد و به فرودگاه امام خمینی بازگشت.
این هواپیما سعی داشت از مسیر جایگزین و از سمت آذربایجان وارد تاجیکستان شود که مورد موافقت این کشور نیز قرار نگرفت
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72166" target="_blank">📅 12:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72165">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72165" target="_blank">📅 12:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72164">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAwMfgMjEonGIajxScOGkVoWN7AKj6e0-dn-lklao6PrGQruqIe4tWJRJsGRjEZV-EIY6ksQWShQfKjWVbzk1X6FrxeJt5GjB8d72w-QFH-fMEJAcWuZG5cbO1oiyxqRJ9jJgXo7sJwFeK-ioUgBoLn6P_d17md5Rxn5yhBgR7FR8kSKzwhJI_WbYPwkzx-KwWbJ9lOJUA8K8ffafyoFfo0jSI3c63DcBvDPUEj5_XaAzJyhypG4TdITzWPTum8HQxkwYogTkXUvm9e2TUqxpnLb9dfM2wn0tkll1S1mJ6z4V7yaER_58tEJPCsFV-zi44ym_EBKtxPZBXNZo3OiXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آلمان
🆚
هلند
دانمارک
🆚
نروژ
ولز
🆚
پرتغال
اروگوئه
🆚
ژاپن
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
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72164" target="_blank">📅 12:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72163">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2bbdedf07b.mp4?token=EzvTNuRqbsErtQhLAQarbSXwihbqt3tBqZ4qNIFM-o9rQaa-j-0vMQw2jsgKEyzJn9GkACjwaaI8UeEINs9awPt8TrMTH4Rs7aSaMxUL0y1z7AT6qBZlBtxlwRwdYZQYtdQn-czFiDA1ScTen7C7xzn8Cbub_xgB6TAux387GVpkp7M-Z_tTH5Rr0zVlz-eYtRs_FADfc8DIeUx02DloRPgZ1VlU9x-Vo5Bfgk4BeqFDseGs7OEo8tTS0L9g9bsdaDmOaV_eGfPsRk0KAbEqfuO5iIMnewnzGX2oq4Pd67BNkbDee32hrvAHEFUZ-GCkiIR5q5MU5B-YoSwXqOMRfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2bbdedf07b.mp4?token=EzvTNuRqbsErtQhLAQarbSXwihbqt3tBqZ4qNIFM-o9rQaa-j-0vMQw2jsgKEyzJn9GkACjwaaI8UeEINs9awPt8TrMTH4Rs7aSaMxUL0y1z7AT6qBZlBtxlwRwdYZQYtdQn-czFiDA1ScTen7C7xzn8Cbub_xgB6TAux387GVpkp7M-Z_tTH5Rr0zVlz-eYtRs_FADfc8DIeUx02DloRPgZ1VlU9x-Vo5Bfgk4BeqFDseGs7OEo8tTS0L9g9bsdaDmOaV_eGfPsRk0KAbEqfuO5iIMnewnzGX2oq4Pd67BNkbDee32hrvAHEFUZ-GCkiIR5q5MU5B-YoSwXqOMRfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که یه پسر از روتینش قبل از رفتن به مدرسه منتشر کرده:
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72163" target="_blank">📅 11:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72162">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa04cd3fe8.mp4?token=jkAlnAIY0yhbw0pp9r86QDZJdwMuHwlU-3iOjUHX96cCNbUikxabycMOE1gi1peMqECsQoM9Ze-0_4pqPFSulWZYWk6fOVUcQQs1Bh0dF2cQrX5dCq-zZ_l5bkXcGIWC2JF61eLscEf2UBR8NvuT9DYVVNUJ1sxhlD16JuHV-K5S7zxxAcr84gdni-rXCLBgnu0BFHCqHmUkWj7dAbVm7PLVwNjfogBJmXXrOgd6rauRkBmviXeYPit5h5RotCubUr_ZJ68v4sV4DGYuK61CGzaz6T7axOfS2UqSVQlXCcow2TnOU39uYKrpOz4BAzLEugvTyM0aO30uuZk6bjXsSLtfcE_kIcRcWAOJrqoWZH-L0JleGEn4GUV0yxylBi98ljftbOC6RilH5mmBwCCf4qaHyKmVJ5eqPlrhK3-UDVt_WzBAr4z7h91PI6tBZaSHlj61_A1xec-W39-srsbJQe_g7NitLIxFqBgd-n22dG0wW7ltOLQP7PpsAc1y5JCrCkl-6or24WVawu0IpAbm7zbQgEuronXy4_wta5ZagW_3HXnC4dTw34dBiyl8J7EIkpiGuTl1tSGfSVyGbPeR_ZrDnt0xEOHqpwBi4QjRGEAY7HQLPlIWPaZhpahUMc84RtpVJZZYOd1Ls40KU0M2ZUZjH8G4SUIJTfPHMx11LQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa04cd3fe8.mp4?token=jkAlnAIY0yhbw0pp9r86QDZJdwMuHwlU-3iOjUHX96cCNbUikxabycMOE1gi1peMqECsQoM9Ze-0_4pqPFSulWZYWk6fOVUcQQs1Bh0dF2cQrX5dCq-zZ_l5bkXcGIWC2JF61eLscEf2UBR8NvuT9DYVVNUJ1sxhlD16JuHV-K5S7zxxAcr84gdni-rXCLBgnu0BFHCqHmUkWj7dAbVm7PLVwNjfogBJmXXrOgd6rauRkBmviXeYPit5h5RotCubUr_ZJ68v4sV4DGYuK61CGzaz6T7axOfS2UqSVQlXCcow2TnOU39uYKrpOz4BAzLEugvTyM0aO30uuZk6bjXsSLtfcE_kIcRcWAOJrqoWZH-L0JleGEn4GUV0yxylBi98ljftbOC6RilH5mmBwCCf4qaHyKmVJ5eqPlrhK3-UDVt_WzBAr4z7h91PI6tBZaSHlj61_A1xec-W39-srsbJQe_g7NitLIxFqBgd-n22dG0wW7ltOLQP7PpsAc1y5JCrCkl-6or24WVawu0IpAbm7zbQgEuronXy4_wta5ZagW_3HXnC4dTw34dBiyl8J7EIkpiGuTl1tSGfSVyGbPeR_ZrDnt0xEOHqpwBi4QjRGEAY7HQLPlIWPaZhpahUMc84RtpVJZZYOd1Ls40KU0M2ZUZjH8G4SUIJTfPHMx11LQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدیداً دوست‌دخترای مردم دارن برای پارتنراشون آیفون 18 میخرن:
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72162" target="_blank">📅 11:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72161">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دیروز صبح، تو یکی از مدرسه‌هایِ اندرزگو تهران، شروع سال تحصیلی رو اینجوری شروع کردن :
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72161" target="_blank">📅 10:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72160">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c86f2846ed.mp4?token=Pyk-n_fcvGHOrG53xkFtt7KYHYk30nvAo8jGNy-UZWHEi2m70oWG6cWf97ApLZBYocpT0v4t4N8Y1FnDg6T_fMUPtj2YELWXMIRrhEGTOGzzANPaoINwP6_UE-jkDyKQy3q0KjEszvlPA7R2IVhoU_EiBL5cB5D4iNnpYfZUZORVpcXclqmKCxoovFmcFIMENC1CphyPXsNUCL9nHMmRBiDL1F22awE0N6ier1SkuSlEppAWrjdEssy_G403UqI0fGQus4A1XVMmPTOl-rngUbDUAzxAPWAuJjvdagce92Y99s3aY-0UK0K-RGkpE11qBaBNHS3cFlTeuwx3_2ZTlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c86f2846ed.mp4?token=Pyk-n_fcvGHOrG53xkFtt7KYHYk30nvAo8jGNy-UZWHEi2m70oWG6cWf97ApLZBYocpT0v4t4N8Y1FnDg6T_fMUPtj2YELWXMIRrhEGTOGzzANPaoINwP6_UE-jkDyKQy3q0KjEszvlPA7R2IVhoU_EiBL5cB5D4iNnpYfZUZORVpcXclqmKCxoovFmcFIMENC1CphyPXsNUCL9nHMmRBiDL1F22awE0N6ier1SkuSlEppAWrjdEssy_G403UqI0fGQus4A1XVMmPTOl-rngUbDUAzxAPWAuJjvdagce92Y99s3aY-0UK0K-RGkpE11qBaBNHS3cFlTeuwx3_2ZTlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسره از خروس میترسید و رفیقاش گفتن اگه بتونی 10 ثانیه نگهش داری، بهت آیفون 18 پرومکس میدیم.
و در نهایت این شاهکار خلق شد:
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72160" target="_blank">📅 10:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72159">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/034c3c71b1.mp4?token=T1hK8oCYBwMCgvM1leGS4Y0t2wD0_oGy4CYwvRUh2EuwKTf9hW_0HyajdJdrbCH1lgGaMp0lmG0VXWMRP95MRrkoir2eCekiYPS3UmcnmqFeq-jM4bnJKjerPZiATThPa2EXBkDmcWwmRQyKIn3iMod5MEBx4_8SZ0W1G4geznhk4-62Kzd-d20dLU7bIUEy7tGMl5SG_TuGpwCrDnJ6gIPjiPkx-Ogbc1gi4d4TKx7-XqfgG-j4T2yu6HXOahdj2kJlyE7_A9uM3IqG7DXOoYtlDS4jZ-P_V3kSGwvJQWxFn9cNSzD-kzdXO_1ywP-JT2h77Ga7a1fbpMzQdRnw_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/034c3c71b1.mp4?token=T1hK8oCYBwMCgvM1leGS4Y0t2wD0_oGy4CYwvRUh2EuwKTf9hW_0HyajdJdrbCH1lgGaMp0lmG0VXWMRP95MRrkoir2eCekiYPS3UmcnmqFeq-jM4bnJKjerPZiATThPa2EXBkDmcWwmRQyKIn3iMod5MEBx4_8SZ0W1G4geznhk4-62Kzd-d20dLU7bIUEy7tGMl5SG_TuGpwCrDnJ6gIPjiPkx-Ogbc1gi4d4TKx7-XqfgG-j4T2yu6HXOahdj2kJlyE7_A9uM3IqG7DXOoYtlDS4jZ-P_V3kSGwvJQWxFn9cNSzD-kzdXO_1ywP-JT2h77Ga7a1fbpMzQdRnw_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم لحظه سقوط یک جت آموزشی RAF Hawk T2 اندکی پس از برخاستن از دره RAF در انگلیس امروز را نشان می‌دهد.
هر دو خلبان به سرعت بیرون پریدند و زنده ماندند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72159" target="_blank">📅 09:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72158">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04b2935ddd.mp4?token=uuLkWkKHFNw_uS1OtESpYjYXBM13TslGTQhakO0fLGjlu_VVl24g6XZ7WvwBd3YA3K6moCbbKsuGeLkM8QvUHRM4z9kUQEbFZZqGCto4YVOeRgAJ4eLlnDI8teRuxuEUd9WhvgPCBigWA7g-bwAZ6B3i6xi07ftjDe_Low_pH4_EPLnePDXgsS_kUZmDh6jMvp-01WY1z7Ty34A3iv10ZhrDBE0sBjpEBL4qsFZncu9z8x9CGB3Rp8qmJwCY3gWwMdRApSIzAmUq3V-a3p2wdJ3-DG9q9U3qVyiyVK-XofPtuyNnxJm5YC3iTjWUMcE13QsvlWFyP2jXTlb8W5V31w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04b2935ddd.mp4?token=uuLkWkKHFNw_uS1OtESpYjYXBM13TslGTQhakO0fLGjlu_VVl24g6XZ7WvwBd3YA3K6moCbbKsuGeLkM8QvUHRM4z9kUQEbFZZqGCto4YVOeRgAJ4eLlnDI8teRuxuEUd9WhvgPCBigWA7g-bwAZ6B3i6xi07ftjDe_Low_pH4_EPLnePDXgsS_kUZmDh6jMvp-01WY1z7Ty34A3iv10ZhrDBE0sBjpEBL4qsFZncu9z8x9CGB3Rp8qmJwCY3gWwMdRApSIzAmUq3V-a3p2wdJ3-DG9q9U3qVyiyVK-XofPtuyNnxJm5YC3iTjWUMcE13QsvlWFyP2jXTlb8W5V31w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تعجب از  عکس‌العمل بی‌تفاوت نماینده جمهوری اسلامی در سازمان ملل، به تهدیدات ترامپ در یک برنامه تلویزیونی
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72158" target="_blank">📅 09:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72157">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad1a7d8580.mp4?token=f5ovALRi_1wdNnsyorR9XcIflw7ySUNZequ9tZYxhA7oH1StKEMrubu_1-yxLUNwA_7hhqVq2R11IhnXZ3CpAO5BEIukh9rsC32WRBJja91vQfaEHb6lOJmKlQweeBZUHlQYPHSdMA-XszOJre-VZNwB2nmtTPDXQHZPJqWUMMFdIJT7paYXd5RZXW_e50Yg44AcINkadHLGAsI3SSnsJ4F-keNvg98tLT2XO5qNKPEZPglVUa_dmE4xhC0S4oHWUjIcixeiIDBE0iYb61yI4ls1pNjqkonXoeEzw1LwXjzPBz5mxiXidodPGElQ06r_N9IickayNcqIcF6NzpEtcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad1a7d8580.mp4?token=f5ovALRi_1wdNnsyorR9XcIflw7ySUNZequ9tZYxhA7oH1StKEMrubu_1-yxLUNwA_7hhqVq2R11IhnXZ3CpAO5BEIukh9rsC32WRBJja91vQfaEHb6lOJmKlQweeBZUHlQYPHSdMA-XszOJre-VZNwB2nmtTPDXQHZPJqWUMMFdIJT7paYXd5RZXW_e50Yg44AcINkadHLGAsI3SSnsJ4F-keNvg98tLT2XO5qNKPEZPglVUa_dmE4xhC0S4oHWUjIcixeiIDBE0iYb61yI4ls1pNjqkonXoeEzw1LwXjzPBz5mxiXidodPGElQ06r_N9IickayNcqIcF6NzpEtcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
ممکن است به نفتکش‌ها حمله شود؛ اما بسیاری از آن‌ها به مسیر خود ادامه می‌دهند. آن‌ها صرفاً به حرکتشان ادامه می‌دهند.
ایرانی‌ها ممکن است ۳، ۴، ۵ یا ۶ پهپاد به سمت آن‌ها روانه کنند، اما نیروی دریایی قدرتمند ما مانع آن‌ها می‌شود.
با این حال، ما روزانه بین ۱۰، ۱۵ و گاهی ۱۷ میلیون بشکه نفت صادر می‌کنیم.
برای درک بهتر این ارقام باید گفت که پیش از آغاز درگیری‌ها، این میزان ۲۰ میلیون بشکه بود؛ ضمن اینکه احتمالاً ۳ میلیون بشکه دیگر نیز از طریق روش‌های جایگزین صادر می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72157" target="_blank">📅 07:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72156">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dfe7fd741.mp4?token=vDo6_6u9mdCdCJBJLsN-FBhlSGL6a2wfjuSVo576S7pr_9VUsZAvpeQ1tdGDLFBtBjymTSEIt8c2XFKJswdLw_Q2fS0Wqu8h0enCHmOKAI_ERB7XDTWLMagHWQgjMa8ursKGIR_tOfRQVaMwrc1bbn-14pGSKlo5HcLCWEOrASx6LBXqt97qyzfATYpSj0YSN0PSyqVkaTFeaCgaZ0W38sQcAR8UBZLDWLegAtlaKCszECoW3-GiKQVXpDWs2I03sTNHWq8YQo_3KiBXtm9TvzOWOn_SnKiujpzYVXvx-a99J9qJdxXh1wC5wK4RV7EsuPDZ5VZhHIgqFLslDH0uuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dfe7fd741.mp4?token=vDo6_6u9mdCdCJBJLsN-FBhlSGL6a2wfjuSVo576S7pr_9VUsZAvpeQ1tdGDLFBtBjymTSEIt8c2XFKJswdLw_Q2fS0Wqu8h0enCHmOKAI_ERB7XDTWLMagHWQgjMa8ursKGIR_tOfRQVaMwrc1bbn-14pGSKlo5HcLCWEOrASx6LBXqt97qyzfATYpSj0YSN0PSyqVkaTFeaCgaZ0W38sQcAR8UBZLDWLegAtlaKCszECoW3-GiKQVXpDWs2I03sTNHWq8YQo_3KiBXtm9TvzOWOn_SnKiujpzYVXvx-a99J9qJdxXh1wC5wK4RV7EsuPDZ5VZhHIgqFLslDH0uuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
احتمالاً بیش از ۸۰ یا ۹۰ درصد پروازهای خارجی از مبدأ ایران متوقف شده‌اند.
مطمئن نیستم نمایندگان ایران در سازمان ملل چگونه قرار است به کشورشان بازگردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72156" target="_blank">📅 07:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72153">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c59219ac7.mp4?token=GznlR9dejEuIB7lJmDc1VY5XDjg65jQp5cOZnPEaHkn-90JFPDiLhQ5wMl2dtNdzPq7Ns6ry5eJaeWPB5_f8TGs3RhsYNsCdt7pIV2VopyzeiIJo2Fpn2jqEPl_W1w7DM79k2yPcR2JDS7sVtM1PEPvcxAtj948LfXeQDEBhE9F9ZfZmSRLbSImWYws5y_W3NFRjmVSidGB_3ZmM-V2LOIULZVNE2NrQgfXWkEq-1ox0d358DxfbBUzWiomO86CxsNe-PDBXegKgajB9GVtg9QmyXPmjW4Qr_u_A5Ciz6y7V_7Zb78zB5HBLlETxcTIb9sZzZaFyXNESPVVVp_cYNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c59219ac7.mp4?token=GznlR9dejEuIB7lJmDc1VY5XDjg65jQp5cOZnPEaHkn-90JFPDiLhQ5wMl2dtNdzPq7Ns6ry5eJaeWPB5_f8TGs3RhsYNsCdt7pIV2VopyzeiIJo2Fpn2jqEPl_W1w7DM79k2yPcR2JDS7sVtM1PEPvcxAtj948LfXeQDEBhE9F9ZfZmSRLbSImWYws5y_W3NFRjmVSidGB_3ZmM-V2LOIULZVNE2NrQgfXWkEq-1ox0d358DxfbBUzWiomO86CxsNe-PDBXegKgajB9GVtg9QmyXPmjW4Qr_u_A5Ciz6y7V_7Zb78zB5HBLlETxcTIb9sZzZaFyXNESPVVVp_cYNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فروند بمب‌افکن B-1 Lancer نیروی هوایی ایالات متحده، همزمان با استقبال پرزیدنت ترامپ از شی جین‌پینگ، رئیس‌جمهور چین، در واشنگتن، بر فراز این شهر پرواز کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72153" target="_blank">📅 01:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72152">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a5acb93e6.mp4?token=ZPOQdJ6Oto6EXoFztfqrf9qOdR7itaZ6EJhKpGzVr-sBgm1SXVY_rsj0GJI4vHnl4l02WTDeDb7u9eFnsji4Gpurz3Gz6qswTnF3nODopmEX9viZxpgn7wWD5KSEASEAlYO4qe4joXbVkdIN6KsBlEN1fBhPYENEPBNHsVQDKkJbcc4am-8gb4Uf9HYlE45HgvjW941QhwguMrYzAyb3a1hBcmfE3-n8UdPDczmheoFsfej71i7EZoMsciq-yMG6V9LzbWKdUdgU7PQDcA9K1dYkmITV6Mj451SowR504guiu9ov7GWx-89mL8bQ9rmMTihWzNBggZCQMXSlpSKkww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a5acb93e6.mp4?token=ZPOQdJ6Oto6EXoFztfqrf9qOdR7itaZ6EJhKpGzVr-sBgm1SXVY_rsj0GJI4vHnl4l02WTDeDb7u9eFnsji4Gpurz3Gz6qswTnF3nODopmEX9viZxpgn7wWD5KSEASEAlYO4qe4joXbVkdIN6KsBlEN1fBhPYENEPBNHsVQDKkJbcc4am-8gb4Uf9HYlE45HgvjW941QhwguMrYzAyb3a1hBcmfE3-n8UdPDczmheoFsfej71i7EZoMsciq-yMG6V9LzbWKdUdgU7PQDcA9K1dYkmITV6Mj451SowR504guiu9ov7GWx-89mL8bQ9rmMTihWzNBggZCQMXSlpSKkww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شنیده شدن صدای تیراندازی در جهاد‌آباد سراوان
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72152" target="_blank">📅 01:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72151">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4470cff685.mp4?token=dyg1yIyp8lY0LFnxSo8rD_hu7Ij1eujyfkX2noR8cvgCj_gr4tCfdLPglmcV18hiA0dNbOv0VJQLGOimcnXRu7o2AgGGXiw9qdPziiG_vz32z2NLAAZLFOnZNzesyVheXVD5Te9lJsoRzdLRCPAI4nmq1u1-FGkOZTtA9OaeFD3RlQt9TIkGYukUlT7NbYMdreA2IorjGX9Rk4BMGT_uSSHnBiI2kR5QYAaaaTAsIZyYF_cFDu_13BjTq-KYEUI7N7TB0wyTJBz5v_nBlXlBkdw3br0-M_SNoDupqtghyvAmvhvZglsRxHo0Lz1rn2Oela-5M-SUtxid1DYG6m-KXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4470cff685.mp4?token=dyg1yIyp8lY0LFnxSo8rD_hu7Ij1eujyfkX2noR8cvgCj_gr4tCfdLPglmcV18hiA0dNbOv0VJQLGOimcnXRu7o2AgGGXiw9qdPziiG_vz32z2NLAAZLFOnZNzesyVheXVD5Te9lJsoRzdLRCPAI4nmq1u1-FGkOZTtA9OaeFD3RlQt9TIkGYukUlT7NbYMdreA2IorjGX9Rk4BMGT_uSSHnBiI2kR5QYAaaaTAsIZyYF_cFDu_13BjTq-KYEUI7N7TB0wyTJBz5v_nBlXlBkdw3br0-M_SNoDupqtghyvAmvhvZglsRxHo0Lz1rn2Oela-5M-SUtxid1DYG6m-KXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شی جین‌پینگ رئیس جمهور چین وارد ایالات متحده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72151" target="_blank">📅 01:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72150">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رسانه‌ی حال‌وش :
دقایقی پیش تو محدوده‌ی جهادآبادِ سراوان تو سیستان و بلوچستان، درگیری مسلحانه‌ی سنگینی شکل گرفته به طوری که آرپی‌جی هم شلیک شده!
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72150" target="_blank">📅 01:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72147">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d2cde76e35.mp4?token=CnTBr4BlJ2bI1BM5B4YoI6x3tGdkQneo2bhToUJaN93Boqgn4vORv_7tas6y6ZU56SBfr92a7fzYtnC2evRkbtyh1NCOdXJekuOuZv4jAgjMi3kBA5uzKtsDk5NRV26-ZFEbJ0ZWRi5SBfvTvdvXbMHbUPCYf8D3_xM-b2abFibGed8yzoMn6pR_qLbw0k6HrQuFZp6OcyjO6OHN2OwkP2nEivDhA8IqHz-k4IG7KC34y7aCqbCZjMTVmn6NBGja_RDGmzKH754mzADucBIJbOFkIPNzCn-UUgiWL261fm5dNRe1WioAzGYS_yESmVfgveD1-GQ30s8Q7axQrGiQyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d2cde76e35.mp4?token=CnTBr4BlJ2bI1BM5B4YoI6x3tGdkQneo2bhToUJaN93Boqgn4vORv_7tas6y6ZU56SBfr92a7fzYtnC2evRkbtyh1NCOdXJekuOuZv4jAgjMi3kBA5uzKtsDk5NRV26-ZFEbJ0ZWRi5SBfvTvdvXbMHbUPCYf8D3_xM-b2abFibGed8yzoMn6pR_qLbw0k6HrQuFZp6OcyjO6OHN2OwkP2nEivDhA8IqHz-k4IG7KC34y7aCqbCZjMTVmn6NBGja_RDGmzKH754mzADucBIJbOFkIPNzCn-UUgiWL261fm5dNRe1WioAzGYS_yESmVfgveD1-GQ30s8Q7axQrGiQyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«اتحادیه دریانوردان هند» (Forward Seamen's Union of India) خبر مرگ یک دریانورد هندی را بر اثر حمله نیروی دریایی سپاه پاسداران با دو موشک کروز ضدکشتی به عرشه C و موتورخانه کشتی فله‌بر «MV CAPE DAO» اعلام کرد.
کشتی «MV CAPE DAO» متعلق به شرکت «ForthMarin Corp Ltd» است که در امارات متحده عربی مستقر می‌باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/72147" target="_blank">📅 23:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72146">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3ooH_jR1x0pgeAD_AgDfsMbk2lHw8Euf4cro23Al-vKP9wedfsujZTwY6LlKSlMVV-OlKx5qwydwGjKq2ngxSWR1hx1LGjKo_XwR__LpcgciAODeZmOnfKO61tRnIBV93wE8tOoLH5l9pzuYRSZo7DZaKDZ7wN8D8hv0r8GKGvln31E0Y1rQ2H7-cmpFYjwGE_9T13V5r5iBtGYAgrE8ifefWy8CHrZxsFpKT0dbZS9xw8tqVDmUqbv5E_VvG_KoWuWhJOJ9_HPFNrSBMHbtvx2aRcPHvsJpvMn2IKiFRE-7y8_MW5cDxDGFZWPi_mHNF8iXowsnp8p0jfS8fNr9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار ظریفی فرمانده سپاه شهرستان سراوانِ سیستان و بلوچستان، توسط افراد مسلح ناشناس کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/72146" target="_blank">📅 23:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72145">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/223e8fa625.mp4?token=CBP27CNSxqX3LPBF_ZbPM1UDqOX0HJWRIvx49S3Ghkt_0L9fUT6uXJcBoL4-afE5PQ2mJ4X8Wh4-36ZaKg89NseNvLP09XJWpygdHJ59_ttGIc-RbiYfHWPNnEhJ1xD0rHesylo30WWkvlJ-wE9EpS1tpMAGDUlYuTipw1_NJ-dYk7ADocCHB_6nGoJwvWkwGA9o6WFqBuwDp6hsipa6hFjXy2S8_T7psnYIICftsj594-l-N6FgsKeYUAon_YdpdSdtkDcB9LJtKP4-yyPnM5--zhrNGtLnaSw1-xCD2ru8N50z5d3kSd3DClc_eDVjo_4UfcxTbQR21WLL9j94Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/223e8fa625.mp4?token=CBP27CNSxqX3LPBF_ZbPM1UDqOX0HJWRIvx49S3Ghkt_0L9fUT6uXJcBoL4-afE5PQ2mJ4X8Wh4-36ZaKg89NseNvLP09XJWpygdHJ59_ttGIc-RbiYfHWPNnEhJ1xD0rHesylo30WWkvlJ-wE9EpS1tpMAGDUlYuTipw1_NJ-dYk7ADocCHB_6nGoJwvWkwGA9o6WFqBuwDp6hsipa6hFjXy2S8_T7psnYIICftsj594-l-N6FgsKeYUAon_YdpdSdtkDcB9LJtKP4-yyPnM5--zhrNGtLnaSw1-xCD2ru8N50z5d3kSd3DClc_eDVjo_4UfcxTbQR21WLL9j94Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواننده رپ آرمین رابر، برگزار کننده میتینگ های خیابانی رپ در اطراف تهران بازداشت شده است. او پیش تر نیز به دلیل اجرای قطعه آقازاده بازداشت و به حبس و جریمه نقدی محکوم شده بود...
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72145" target="_blank">📅 22:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72144">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تسنیم گرفت رو عراقچی:
تعامل عباس عراقچی، وزیر امور خارجه، با استیو ویتکاف، نماینده آمریکا، بدون مجوز یا هماهنگی با مقامات ذی‌ربط ایرانی، از جمله شورای عالی امنیت ملی، صورت گرفته است.
ادعاهایی مبنی بر اینکه این تعامل از پیش به تأیید نهادهای سیاست‌گذار ایران رسیده بوده، نادرست است.
بر این اساس ضروری است که آقای عراقچی درباره این اقدام غلط که مخالف مصالح و‌ منافع ملی است به نهادهای مربوط و ملت ایران پاسخگو باشد که با چه محاسبه‌ای این خطای بزرگ را مرتکب شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72144" target="_blank">📅 20:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72143">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d86a283f5.mp4?token=Tz6VT4IopafYc7PO_eptPRIwCWKhEHV3X6FKiRydv1njusuPUgD84fWWnFWbq2rpUyerV9kEiy48EUqDB4otbDaqVgXqnD_lUcZ5mdsYt8-ixH9vQM7OJF4QNiuS-NeZt9HH5nt4D2XvizMJdcC2zcQacwlXdEYBi6JFn9gLUbQllekvmOb40S3U0sAqXcbvSco_NwZWRYnUZtp2JE7eg-0gOyVtoDen9MbB3a-cEwTB-4GBcw6u83VZO2Akkra4Ce0E5jD_reSkNFcxUJLWLCgHFD5OnGTAJ1pl4Lwo9xigrmd6yXaXWmsziDaP21T9afAxkNQbmsgAu7jbxO2jVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d86a283f5.mp4?token=Tz6VT4IopafYc7PO_eptPRIwCWKhEHV3X6FKiRydv1njusuPUgD84fWWnFWbq2rpUyerV9kEiy48EUqDB4otbDaqVgXqnD_lUcZ5mdsYt8-ixH9vQM7OJF4QNiuS-NeZt9HH5nt4D2XvizMJdcC2zcQacwlXdEYBi6JFn9gLUbQllekvmOb40S3U0sAqXcbvSco_NwZWRYnUZtp2JE7eg-0gOyVtoDen9MbB3a-cEwTB-4GBcw6u83VZO2Akkra4Ce0E5jD_reSkNFcxUJLWLCgHFD5OnGTAJ1pl4Lwo9xigrmd6yXaXWmsziDaP21T9afAxkNQbmsgAu7jbxO2jVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنتاگون ۶ مورد دیگر از فایل هایی که در آن اشیا پرنده و ناشناس به اصطلاح UFO دیده میشه رو منتشر کرد که دو مورد اولی در خاورمیانه ثبت شده هست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72143" target="_blank">📅 20:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72142">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9819ac349a.mp4?token=CNZEO06M6N3SoRbP--Ejbf2NXtuUsd_TDe0yThM1N0z_8P5dutRByuft70BqtpubNmOzuMRP9_qjWPNbpxIzSlQMifudVYUeUosmocvo6oxAFT7pnWbJHr6t1uhQHy9fqTj_klLhKuRkZikhvjkLnzbFblr5hNlHs0jX18vUT1nH_-7gdw1L0yMTMfpEQY8GrmikmyB8ad2Jk6HinbXexJ46bYOPnoKyp4g4OUUOekxdUpqAj2wHjeCFoGmWp1XehAC0D9m1n8Qr9Rclq3HZTxc9EuBgi__Ilk0s00ViFVri4IzRQkg1q8RIfkCEW9r-CshDyeacW5voQenzoypmg4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9819ac349a.mp4?token=CNZEO06M6N3SoRbP--Ejbf2NXtuUsd_TDe0yThM1N0z_8P5dutRByuft70BqtpubNmOzuMRP9_qjWPNbpxIzSlQMifudVYUeUosmocvo6oxAFT7pnWbJHr6t1uhQHy9fqTj_klLhKuRkZikhvjkLnzbFblr5hNlHs0jX18vUT1nH_-7gdw1L0yMTMfpEQY8GrmikmyB8ad2Jk6HinbXexJ46bYOPnoKyp4g4OUUOekxdUpqAj2wHjeCFoGmWp1XehAC0D9m1n8Qr9Rclq3HZTxc9EuBgi__Ilk0s00ViFVri4IzRQkg1q8RIfkCEW9r-CshDyeacW5voQenzoypmg4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از هموطن‌ها رفته یه مرسدس بنز خریده؛
همه منتظر بودن از خریدش ذوق کنه ولی صحبت‌هایی که بعدش کرد، جالب بود :
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72142" target="_blank">📅 20:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72141">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اگه هنوز دنبال یه کانال و گروهِ «واقعی» برای پیش‌بینی می‌گردی، درست اومدی!
👑
✅
تحلیل‌های اختصاصی و رایگان
✅
ضریب‌های طلایی
✅
گروهِ فعال برای تبادل نظر  وقتت رو با کانال‌های فیک تلف نکن. حرفه‌ای شو و با ما همراه باش.
👇
[لینک کانال] https://t.me/+fyrt-rnxFjNjMmQ0…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72141" target="_blank">📅 20:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72140">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-IhVy2Y27ojjkqClq8SRL1fW2xqr417KvqwOojwM8mUatOCKB2zP0nuEkfos_BzNuQmpJBlEXs0_aXUXZHAY_RUoWEM42nV0QS02lfRH1Zp5EEgM7OqAlwEUMXblURqba1UDUuRPClhMciRK7AtgLBVebNbJWz-wCxl3MNirf0xLVC8hODvp4GKlG6UDWFu784ZvoLtyB2pNhocs3P3i5LCAqzRmWha_Dy8IBQz5DLW_c75sTADhT4Dz4iDsm-z_bU5t0dBywiikE_i3MeaJGpiCsdy57fuFYd5AI-y5UmyKetshz4YAat5PQH1c-8Kfp14Lu14H0JAeCd5WiiqKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه هنوز دنبال یه کانال و گروهِ «واقعی» برای پیش‌بینی می‌گردی، درست اومدی!
👑
✅
تحلیل‌های اختصاصی و رایگان
✅
ضریب‌های طلایی
✅
گروهِ فعال برای تبادل نظر
وقتت رو با کانال‌های فیک تلف نکن. حرفه‌ای شو و با ما همراه باش.
👇
[
لینک کانال]
https://t.me/+fyrt-rnxFjNjMmQ0
[
لینک گروه
]
https://t.me/+jpSLBx8PcgBlMWI0
#TipsterPersian
#سود_تضمینی
#شرط_بندی_فوتبال
»</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72140" target="_blank">📅 20:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72139">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fa977cc40.mp4?token=N7fpbqjr6weAq1Stj2-iRY-4j55MS-_KWxcvDBg1ENp1ii6jB7IADIateWT5jkltiyymn0WYUr8GEA27kBrO0nZcQR1-Oljs_pOUX7c7NXHxhVswtyvG7Hah32kKp0XJJE6BZy2ZvTUIZv86F-C8UTA_sEO4Ui6MO6luiA23-VgJQEluk87wHGH-NhBsnGsAANBYkVl77BoismekwAANMVAkjaRvNibnK9fZde-R9G6lEhXnf4yrRJv0yi6RDia3NCg9Xqw1XKTJSzvfaQPlnWbn2O3M03-IJaVZzJzn3x30Ob_R7grPNiDwJEruSbKh0tsBYlW37lKwM2oh9F4xHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fa977cc40.mp4?token=N7fpbqjr6weAq1Stj2-iRY-4j55MS-_KWxcvDBg1ENp1ii6jB7IADIateWT5jkltiyymn0WYUr8GEA27kBrO0nZcQR1-Oljs_pOUX7c7NXHxhVswtyvG7Hah32kKp0XJJE6BZy2ZvTUIZv86F-C8UTA_sEO4Ui6MO6luiA23-VgJQEluk87wHGH-NhBsnGsAANBYkVl77BoismekwAANMVAkjaRvNibnK9fZde-R9G6lEhXnf4yrRJv0yi6RDia3NCg9Xqw1XKTJSzvfaQPlnWbn2O3M03-IJaVZzJzn3x30Ob_R7grPNiDwJEruSbKh0tsBYlW37lKwM2oh9F4xHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتظار می‌رود سخنرانی نتانیاهو در سازمان ملل به شدت بر ایران متمرکز باشد و به گفته‌ی ایدز، این سخنرانی حاوی «غافلگیری‌های» نامشخصی خواهد بود.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72139" target="_blank">📅 20:29 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

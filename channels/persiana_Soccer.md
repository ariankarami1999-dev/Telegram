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
<img src="https://cdn4.telesco.pe/file/GBIFt5_l3E5RvyyurTKJXJqGSAxjUXZ4GtnuSkx76JLzPmlA7xjEdc551rw_WB5mWZSBIliwPzZuql9725tHLiqDL1dMvC0W4d8VeOVZ3vtqym1J35OId01CDRp9odD1MZcqGe8GXK249aiEHnVIjcH8hbHgXxkP6ga1A05gxv2usVDQcsmJzuVmuGGHbJIRAe9dq3-bjscYe5KewdUkuelfl2NqiuwmJzV-JuJQ4WmYHTtUctm1mv9VulBt2R4GPAOosvH1SaSD3IPbFkUVbaR2UNOraSHeOyyfq1GzRHU1x0u4nFqYU3gw8Z8LTYlc2eDAWIUVkf4fVjw2-QjY4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 635K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 18:14:03</div>
<hr>

<div class="tg-post" id="msg-27211">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubTWwhIfhj7243BJhAJP2bZJBvW3Q8jcHodQIKaPGR75g31-KUxX22yNOtR7psKwihuDRDVSMkYnhr5xV6f1bIH-Shv-vJq4O8Y7Xx6QPe3SLUV_FTqiAZs6skoCDyf88cnp0ZLDw-9yf3nFj1hFi5txdu-tSopH6wjYo7hF_ZRAvVsChqkB94mfQp_UuXSGWm1ufzrWs2F1s6Z3b4zXVo4XGxKQ-NWS0PKJH57H55gsSle5_UbXRVPwrLA9RKswpDhnHPbogPJazKDD_ia04sUA61z7WqFmBS89BQ76cpznVdIDY-y0av5wr8fnIsVPXkWVErHu4Z70T4bFf5UTbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
پوسترباشگاه رئال‌مادرید برای یان دیومانده ستاره جدید خود؛ قرارداد تا سال 2033 امضا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/persiana_Soccer/27211" target="_blank">📅 18:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27210">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmfT0U5j4LdyY7MwLaknAABPkU0H6HN5fImTIZnM7j2t8ROCvplmwvPIcdr3U9EnfDGkWxCuhG8GkiJbTXClf-p-L5_AEAqEWCacCEHNEhfHl7j58RheQPfNQKpSBzMRKd5s97Ld6iKpQeIkRswDYjM9ToYQ2z46_h0pxV_82GtQy-MdAkjcUl98HN1C2_H1YZmOYJUbsQn2-V2XUgKfw5U1Lf-h6UgNQigvorhdJACIzrXZFHc5OFbyriLv8k7czuTDzqCjloFRJj9oRGuLSNcX35jF1naj7XFhACdVkGFX3-k0FOAftfOpriL2f9pphS9uSd3ByXpqBMyAfLW6Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
خوزه فلیکس دیاز: رودری قطعا بازیکن رئال مادرید خواهد شد اما سران منچسترسیتی قصد بازار گرمی دارند و میخوان این‌بازیکن رو با رقم بالاتری به رئال مادرید بدهد. رودری بارها اعلام کرده جز باشگاه رئال مادرید برای هیچ باشگاهی بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/27210" target="_blank">📅 17:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27209">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmOT2p6IeYrjXNtUfYTg11WGfRLGBsYOcnKUsCytKyOSiq8u0zcYFTUvMWXSKZRCD9e-ZwKTioZpLs7mJEH0QFi6SM5xAmPoe_0SDhi7q4egqej6MOhL8YVOXShGcx_5VNf3t-cvZSAR9CpL1lk8-Vrf1U7WR6xLCqY9qB3f8MwB0wsVkScEEOYUX7lgyyL8I7mwSpJnNF5jWXmvxvDgCCYQhxqWuTRlUj8VDhzegkqZVYCeQdR-ZtbuF8-W9FRLvSFmtwV5DqOEP8_DTIQejgsLLNA8VgWdFetdE3QXCEtOGhqK4RymVFuoNiCABOveR4xepyeIgJo8huVEsxSDCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/27209" target="_blank">📅 17:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27207">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIs_l1K_XQHikWRJLnr7fPbbPw4zOxeVYZFJBMRiw_yuCT8DBKbA4JIhKRyjkyzu_0IpFonrr0xEYKBrmU5UcDMmYhQa-cWFOiRgVdNCazi1QXvP-NuQuCcbSQjDHGYlIWjW48n1OSpGyrSkr2ohv6obBlczYatlOAmNKlDJaY3nsXGLdQgLttIrL2sr_uwevxF3JlqjmEVZI4D9n9_ZkvgRCZb5sLBnVYHkOxe2jmIIbvLsSnuZOI5jtnn61EUPJyEJOAvd_uQZzVNKQUph-17N70Jc-xxDnvjs1HosWXl5VkAl00FsfFkfJvbo6LU09izjAolHtAes28XoBo6cAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
عملکردخیره‌کننده لیونل مسی دربازی بامداد امروز اینترمیامی با به‌ثمررساندن دو گل و یک پاس؛ گل‌هاش رو در کانال دوم گذاشتیم برید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/27207" target="_blank">📅 17:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27206">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f47e64799.mp4?token=JbHRbuyj6s_MPziRhzN-25xHc4mOsuESd2WP7ft2HRRfW1nQ4FH5BFokCMh0BOcxh5F8bk8ttWGKxr6V13kwuMDuQ3Lb7Wn9x46tZ2EFiJsaDuguxDnxnVqRjeV1R4JdULmAgLFMVJMe808EdbIUA0p1Ciqu83IigOB4JSwwWjcQeY2-cnHFyxfUZUVS9Ndm1UF3_6DYhDOMKHflxm3erOHRm1xfmoiEowShArTXNmXwZCvF7OTJEcvp186haA5l_GBu4Yg8NRjz3nwF-dhlCdC_W7yadl2b3UKjVY_Vv07EuW4IjAcKiQCeIf7pBXtlW9IzSUYKBL6ZUpDyMPK_-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f47e64799.mp4?token=JbHRbuyj6s_MPziRhzN-25xHc4mOsuESd2WP7ft2HRRfW1nQ4FH5BFokCMh0BOcxh5F8bk8ttWGKxr6V13kwuMDuQ3Lb7Wn9x46tZ2EFiJsaDuguxDnxnVqRjeV1R4JdULmAgLFMVJMe808EdbIUA0p1Ciqu83IigOB4JSwwWjcQeY2-cnHFyxfUZUVS9Ndm1UF3_6DYhDOMKHflxm3erOHRm1xfmoiEowShArTXNmXwZCvF7OTJEcvp186haA5l_GBu4Yg8NRjz3nwF-dhlCdC_W7yadl2b3UKjVY_Vv07EuW4IjAcKiQCeIf7pBXtlW9IzSUYKBL6ZUpDyMPK_-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
خوزه فلیکس دیاز: رودری قطعا بازیکن رئال مادرید خواهد شد اما سران منچسترسیتی قصد بازار گرمی دارند و میخوان این‌بازیکن رو با رقم بالاتری به رئال مادرید بدهد. رودری بارها اعلام کرده جز باشگاه رئال مادرید برای هیچ باشگاهی بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/27206" target="_blank">📅 16:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27205">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BF16uMZd9hSbBQLGgJIjR9mkL_-01yUygVhH-cP1JIXjJCpLsJkhhXZRQKkDtDexsh4Icm3EsBAyZocDip5i5wgCZ3qpwIpkuHZC-4fNWF4nBiNw6eT8N9iy_eM7zOdC5UXk7QJKC20Oa0HwYryTnwR9QmDAPCQx4zA909md-ltQRziyPVkE_dvgIRJSej6HImp8wdMZ7QwkiEcGl7mlEf0RlpD-VeQhsrdiiOEasaHx4tn_yu-WPVrq9Q8Yg7dEzWCspOfTaR6rMXMytYVBtn4wzBqjKlyL8EiHfxSxis8V2dydLnRGnl41gZQYaHXbogMtavhIyjx1fqIJtCDsyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیریت تیم‌استقلال باایجنت‌های دیدیه اندونگ، موسی‌چنپو،داکنزنازون و آنتونیوآدان تماس‌‌های خود را آغازکرده و اعلام‌کرده‌هرچهار بازیکن‌رو برای فصل جدید میخواهد. اندونگ، آدان و نازون آمادگی خود را برای بازگشت به تهران اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/27205" target="_blank">📅 16:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27204">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEiPxiQ0NNORQzZHdEcEEhAf1uCM6XCHz7R-eArO9r1YAAMfYh_pvpdXoX55IgWABM8fT2AKhJbGAghcWciWAh7A0Sn6ZrVmI-76Ew2cnO-xVd-KDHhWdZWO4gVO0ngELPeaTfjHRR2a5vP8OqDgW1BrazfCzDdlilxEz7RsE_6921GH96J7bySYxcyjcSKKCd3mpZbWVGlVU4E9w8US8N6KRjOvfpM3aHlYLhNBGsHItf8kGvYvhWCJmKZhIpP3vFHGU_9tTjx7gwUCgckgkrTkm8aKVAtYmG-4s73yyGiMSV-6pxdJ6Ybiyj-oTCNs8FyNS_E_FrY6B5k6-6L4xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
پابلو گاوی؛بازیکن‌اسپانیاکه‌قبل‌ازجام جهانی گفته بود اگر لاروخا قهرمان‌جهان شود موهای سرش راصورتی میکنه در روز تولدش به قولش عمل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/27204" target="_blank">📅 16:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27203">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcW98M2s8GHK1-VMTAu0AzZuDnQt0BfD7s97UrrFxpGwOxXNXvCUjck-EYdtVzZaGIivhqwFcxdtCG4JRC_BNXqFC6WUS30LIAC3wBPpDAipwp64dLudYuV26w3l1jgLcV_lUFG0EzIvgBHFfEuA0Is6yy46HvQtyEnZecTURckmXAVwBr_w0vvYRUbCjH60IpYm_bu46_p2yybileDc_qqsPml9puWFsjkAW5PNPRuMuskegfSBXJxvNG3o6tw20ImHVMnvoH-rm22sqZzkxYRJMKfLr7t8zQQnySfr0R7wabOwyX9bQdBYwEpcXMHTszAkI5QY1EdOeVKcDp2OdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی پرشیانا؛ باشگاه استقلال برای‌دیدیه اندونگ هافبک گابنی این‌تیم بلیط تهیه کرده و این‌بازیکن‌ظرف 72 ساعت آینده به تهران خواهد آمد تا بعد از تمدید قراردادش با آبی پوشان در تمدید شاگردان بختیاری زاده حضور پیدا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/27203" target="_blank">📅 15:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27202">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsD5gE_RNIl-hLUik63z368lsJoDOEurCtIreCukbnCSXUXLHdhmtt_7A4T0Pjlh1lcscmPJrQBa2pGapwCGkMbjW4ioESynwYy9Fcqo27z-2jLyJAMKwIqJzHuKagVEprT3ukiLa2qfiNqrxFvrJ2ijj0pH-boEIToaGRXv5mTJPmvpxm89YpAAJvC51tEwXrIfHfNZ4pKj7Tqbl-wMCfLy02WBRzTAwO4pLvtjJUiEwwyPSV0XOCWtwyePiQs7hyx0FsAQckJeVULji3rmu6nfJl0XjdbY-XQxg0gZZ7yuJmmaffkKmmRWbdJcHHbLLhw20DB2da-4ITdBYMtHDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق شنیده‌های پرشیانا؛ بعد از بسته ماندن پنجره نقل و انتقالاتی باشگاه استقلال؛ علی تاجرنیا شب گذشته بامدیربرنامه‌های ایرانی آنتونیو آدان گلر فصل‌قبل آبی‌ها تماس گرفته و ازاو خواسته آدان رو برای‌بازگشت‌به استقلال راضی کنه. به احتمال بسیار زیاد آدان بزودی…</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/27202" target="_blank">📅 15:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27201">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97dd42f0c8.mp4?token=XWeIK-sOwb9H3FFDVN1n9ghLAOj_SJsQDQEo8Mgq526i0Sh_idqzjbPEf5qZtNNrsr6Gh7mnxaXUKunS_XWcKD7Hnkwb86A-m3mzXSNTs6Xny0AF0_s9lxmGB_rNacKaXdt0R8NJ0ygFY8irQThaC7Okc_t2KpFc2BO2vaQ_IyQ3pt0BrBvSInf6G0qc9iFr8cho34G2Q_lHes_UUkxlFcQutnaT-yanDXzCUwtxD-qP8dLqaFmsWAJputn8wDDK_QqVtUJ4UONE_eFhMLGiPhpdYvsNzyy2bh-a4qtrOoKEeBAt3QdvDY0-fbsjGn8Nw5opKEaEG2cwFTOcfzDICw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97dd42f0c8.mp4?token=XWeIK-sOwb9H3FFDVN1n9ghLAOj_SJsQDQEo8Mgq526i0Sh_idqzjbPEf5qZtNNrsr6Gh7mnxaXUKunS_XWcKD7Hnkwb86A-m3mzXSNTs6Xny0AF0_s9lxmGB_rNacKaXdt0R8NJ0ygFY8irQThaC7Okc_t2KpFc2BO2vaQ_IyQ3pt0BrBvSInf6G0qc9iFr8cho34G2Q_lHes_UUkxlFcQutnaT-yanDXzCUwtxD-qP8dLqaFmsWAJputn8wDDK_QqVtUJ4UONE_eFhMLGiPhpdYvsNzyy2bh-a4qtrOoKEeBAt3QdvDY0-fbsjGn8Nw5opKEaEG2cwFTOcfzDICw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش پادکستر هوادار محمد صلاح به انتقال او و پیوستن به ترابزون: این چه خبر مزخرفی بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/27201" target="_blank">📅 13:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27200">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‼️
واکنش پادکستر هوادار محمد صلاح به انتقال او و پیوستن به ترابزون: این چه خبر مزخرفی بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/27200" target="_blank">📅 13:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27199">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dab647f68.mp4?token=aueVIhvA1IobEEs2f4KMcSdLZVrAMZbDECEEJZnJm_2h_cuM_sso6k0V-VUGmCjDO34FUK-WCyHertzuYSbyb9qJQXuj1mAzpgCYY5t0Iqv_VkW4zi52wOd-OoiLBLmG5uywSCJKvP82LvA8wblgrkRKhegWoTD29JiOvFYZEx2RzeBVI9cPaVRgNoRwgliCVzs4p8PtUIu9dXzGZozrQKntFYRwrIwNeQbRrMimkIRwfgUQzrZ2LNo0P4I-ueePMx2_rB4dBMsUGau8V-43ste8Rec8in9I4ztxQ4P37dZ5arj1oCNpoDLsbZ9y1RU5bBuGO29iTq-vsjyu6aVfFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dab647f68.mp4?token=aueVIhvA1IobEEs2f4KMcSdLZVrAMZbDECEEJZnJm_2h_cuM_sso6k0V-VUGmCjDO34FUK-WCyHertzuYSbyb9qJQXuj1mAzpgCYY5t0Iqv_VkW4zi52wOd-OoiLBLmG5uywSCJKvP82LvA8wblgrkRKhegWoTD29JiOvFYZEx2RzeBVI9cPaVRgNoRwgliCVzs4p8PtUIu9dXzGZozrQKntFYRwrIwNeQbRrMimkIRwfgUQzrZ2LNo0P4I-ueePMx2_rB4dBMsUGau8V-43ste8Rec8in9I4ztxQ4P37dZ5arj1oCNpoDLsbZ9y1RU5bBuGO29iTq-vsjyu6aVfFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌ تامل‌ برانگیز زنده‌یاد علی انصاریان ستاره فقید استقلال و پرسپولیس درباره حسادت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/27199" target="_blank">📅 13:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27198">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvNjLfRyeImK5bzcYjtwxIxfqUsEV7rQZmN_t7Zhrz1pQ9ggw0ZDi6Oa9lDyhLy5SCXxR-LrEBA754g0C-ttfPh9cfRKoal0PeJtksidMtgpVnFZKIKqGPK-F-e8sN9QVJQwKZTwqe9mGpX2gGN_-s4AHgdIMBxJRynKaI3n8ASQqFzdy8vEASbaesw_DsbtJ6dkic6kyJs7Fja-f1aVNCuCqu7RLcayL3xqTNu8NdGUaNXXK1lAMfWU_YNSBKOHUc22mQH2O1NOOQVKWwhYpgivlcE6MR5yas9Ugz1R0X9Rz-Akm7um2pRMVv4PVWTIWbYCbFXDqy9oRpWTj-HLrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخبار دریافتی‌رسانه پرشیانا؛ بانک شهر بودجه‌لازم رو برای پرداخت رضایت نامه دانیال ایری دراختیارمدیریت باشگاه پرسپولیس گذاشته و انتطار میرود ظرف 72 ساعت‌آینده این انتقال انجام شود و ایری با قراردادی چهار ساله رسما پرسپولیسی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/27198" target="_blank">📅 12:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27197">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bor17LPbqOR7edqSB4pHlFSty9vzknusLq-lRBVYZuQ2sWaZxDkGqmhutg3W2JZd8wJzHsWhMFBbdyLJWv3cK66JCjE9ehTdHMQnH2ab8F4iAFcGKYO82PPI7EhfVcOco_Ac7uxFHPJbuLyi44dj9Q4SNAP3foAuwzaOJjAxS0hx0bPvHu9Ngr7H5PUuY-iXXNft5qrmdFJ5JX-enP_UgxH-wmHf-WrDXvYZ2pyHnGUwMljdpCTjph-W0YNom2ix_dCkXEL8itscFXfdan_5j1y9tVscsR07d5pCTq-74djWp9RIqNHlcdM2D7sPdxXI-MvYbcZi9K8H2KKbrj5Uuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ فابریزیو رومانو: بعد از رئال مادرید، بارسلونا هم برای جذب رودری دست بکار شده و با مدیران باشگاه منچسترسیتی تماس‌گرفته و آمادگی خود را برای فعال‌کردن بند فسخ قرارداد این ستاره اعلام کرده‌اند. حالا همه چی به خودِ رودری بستگی داره که رئال مادرید رو…</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/27197" target="_blank">📅 12:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27196">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHgJo16EW8CibtxmNos93kkeU2TTG4rjnqepXUBhJX15TLYy-X9rbZli1IVBSSFSZQTcGkgWjwlmX9R2BgMuj1WugYkz78kgiKJpVm0nr-AvGAj_ZzWm9pjgiF6fPMgj8V4-kYT7lkkgvsKEYBy2A_cMh-YLb7HYlBPRbjoU3QYmRZt-ScQhDbmuOfIs5YXhxMJuBHBhIPy8jssEs3OjWRGfZ3tQx-eqMbhDd6FbyDdQ51SVIjswtJj8VIf-kk-_jhhbZkXfVz69UTqaUGeSu75LqoYW0J-LeGbkTO7PXKQQl02Nv-gkxyAM44tlBOOc7NSgCPpjTNnK69NX_Ro-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رودری ستاره اسپانیایی 30 ساله باشگاه منچسترسیتی:من‌تمام‌پیشنهاداتم‌از تیم‌های بارسلونا، پاریسن‌ژرمن و منچسترسیتی ردکرده‌ام و تنها هدفم دراین‌تابستون پیوستن به باشگاه رئال‌مادرید است و مطمئن هستم که این انتقال‌بزودی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/27196" target="_blank">📅 11:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27195">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17c93987d3.mp4?token=CZLT_WaDh2qTXF8gRXvOf0nfC5qFgmTaav-DFST65-1dAa1qZuitghKjuPsYsBGeTaXGif9ONl--x_9a505U628WuArBViyE8ggnhT765u_WkZ5n97oUp2xF7Yp7rTjWsrqtDdg9mLqnV0Cxdx52jGMR5TGFPmehDVh8RlisMjyw8MuZQEJjegBTtmtjHru2nDQIi_7LO6i8Hz0hvkos5Cr3-tKU_Nb08a182uTI-Ua6tIlM5-WkxYkjRdHX4ZXTTnjwF_b6QTMnlEjm8oMFnpfivJTBqYfousjUkNgVXeVVrBQjNnLiYi8eEsWcB91zLNiZOdshyG0m3Hr9uM7zWHHFWydoS9S7_kZ-lNA9ZHh-XvWAxFP_Yew2Lr91sPcJkc2Ly7sm2yCpzE8i35IUTvMrunvcd9iOZX-xA7KcBpvILrITcSM6O_07hzCOstxl_53YSxNt0Q292kC88jQI0GB75U4opR6Ye-KBR85dVTdIUo7tqgE5HZsJ8FzVK0FYnGMXiDbLHKL7zFOMnPVj7eXhv328vDfYhk6WbY3H1hI2VRzy1E2CkLu8aMKWcjkbCFUJk2RnHSDyA2_H5WGu8yp3_mqahhWlwuh-x0hN3_iVbxhW2kqqavlyRXX-JGJt76aaqStjXTaWTEwTMuGbWweslcQUKK4F1iZCmUKScoc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17c93987d3.mp4?token=CZLT_WaDh2qTXF8gRXvOf0nfC5qFgmTaav-DFST65-1dAa1qZuitghKjuPsYsBGeTaXGif9ONl--x_9a505U628WuArBViyE8ggnhT765u_WkZ5n97oUp2xF7Yp7rTjWsrqtDdg9mLqnV0Cxdx52jGMR5TGFPmehDVh8RlisMjyw8MuZQEJjegBTtmtjHru2nDQIi_7LO6i8Hz0hvkos5Cr3-tKU_Nb08a182uTI-Ua6tIlM5-WkxYkjRdHX4ZXTTnjwF_b6QTMnlEjm8oMFnpfivJTBqYfousjUkNgVXeVVrBQjNnLiYi8eEsWcB91zLNiZOdshyG0m3Hr9uM7zWHHFWydoS9S7_kZ-lNA9ZHh-XvWAxFP_Yew2Lr91sPcJkc2Ly7sm2yCpzE8i35IUTvMrunvcd9iOZX-xA7KcBpvILrITcSM6O_07hzCOstxl_53YSxNt0Q292kC88jQI0GB75U4opR6Ye-KBR85dVTdIUo7tqgE5HZsJ8FzVK0FYnGMXiDbLHKL7zFOMnPVj7eXhv328vDfYhk6WbY3H1hI2VRzy1E2CkLu8aMKWcjkbCFUJk2RnHSDyA2_H5WGu8yp3_mqahhWlwuh-x0hN3_iVbxhW2kqqavlyRXX-JGJt76aaqStjXTaWTEwTMuGbWweslcQUKK4F1iZCmUKScoc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخیرا دانشجویان رشته علوم ورزشی دانشگاه سنندج به مناسب فارغ التحصیلی این ویدیو زیبا رو ساختن و درپیج‌دانشگاه‌منتشر شد امابلافاصله چنان فشاری به مسئولین دانشگاه از سوی نهادهای امنیتی وارد شد که مجبور به حذف این ویدیو زیبا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/27195" target="_blank">📅 11:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27193">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fi0TfOsQGekcSfHk94eDYkg_jGNCloHsEtLOnSwcG4hqZL0EDzJxWUu3owAD7yMA_yiRP-FIWrzGkvtXvOadQvYnHbqzTWfjEDbJc6MIPwElby43KiuYO8DTeM_fTg6lJajNsUtAqIGy_8uFCfEQFDWZ0-OXfBhSvLqiWRXPCDmrmJCCVzEtXIYdXLjjZ-IjsABqqUifYxtU1v7mG1pkZ-l-zo_7q-aMJUFcDhUqnOEc4JiDELEQMaBgmDfwCUFud26nDDi7pr1jsK872g8WWpFgALZhYM4kps5SVl-s5HcagJsvi_qPtGimqq-nWs_WLNNcFaNJYroUtADMtI_1ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wxq8u3bCHbZEvvNdo2XZ4Nty1h_f1KJtItVp56i84vuqk_IpZ7VMl-Z9Hg_h01-dbDq22iZeRMLwgqZxN21lS6WM9d7qwqwQOQsPWJWaLmi-NKKq0XBNKWur9HP4sqCLxSD3xAml82Qz2MLyMtph5C3eq3kquxTWMq-VArq6pUgn19uGsc5H5VnwIxaxTi4c_LL1Lj2qd3rDlv41f6iCMSJ4PBzNRy2xW-fsf_Ffj1yrM3OSScGIK2LEYUavpvRo790DwJMp9RxBcRTaAm0BJ5d2aAExd1IE_n0L4Mxt-o12K2kOje0jeE9UnxfjFHWwREbXbLl3uTLY4LGQbhdNbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
به جورجینا هم اومدن احساس بد بدن راجع به بدنش، در جوابشون گفته: واسه من موفقیت واقعی هیچوقت این نبوده که خودم رو توی یه قالبی جا بدم که معلوم نیست اصلاً کی و چرا ساخته‌تش. موفقیت واقعی یعنی با خیال راحت زندگی کنم. کنار آدم‌هایی باشم که دوستشون دارم. حواسم به خودم و سلامتیم باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/27193" target="_blank">📅 11:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27191">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165da6fec7.mp4?token=P2T2THmIVcObx5NNIQiNuzzgkTaBWziVNZU-lrKbptTnVNumqpw0bAUg3b-erOR4-hcdqWe8Xmm97HEn_5_dn_5I44eiHUc6ixCnS-kcYLPkknTDI5cji9I0FvHQCO0bYa0-s3x7rBUMVZObrrPTjQjckKU1NpfXA3g4huOyGzcJwR-serSUzfFHXX_7Hm5A-r7qDqWIAfsIhxfWkWKEmj_bOay0ChWb2hGrWDS8dE8gstkDLTVrMyQftyYaGIF0tUbbAAet6C4WssMDVIZcAT5ZANniDrbmx6w-pAMmKqZLVLG5FRLYAsRaJfpMdISwqQ1gm-AG6Q806zt4wV0073ht0namwyTEvIUWzJiz_c5HO5oT2YkYd_ya_S8OZAFTL-vnrgrfTYDZaP8cQYKHejjKZXCExhUm9OsK7pIF06TMQQRtgtPEQXSV6ngj-eOBJqdcKTROnTus6Eqy2WAqNDpAhuZNYemAasuhKh-SVqlwXdr20GIdke99AEv58e9FeLhxD21VmD1c-hvmSiHRmiLv0d20MyOKimTgqDyP1-G-6vWzL2RkmJyeSGVTrI764s3qg1NjcdmM_PUKdLx3gB2FX-KNnRJrcnM_IluroKuXHPEslKHo1goxkEUk2dE0gbt4_aHiBR8lNAA-5A5t5FiFVFBW7vkWOY7oBfdKobQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165da6fec7.mp4?token=P2T2THmIVcObx5NNIQiNuzzgkTaBWziVNZU-lrKbptTnVNumqpw0bAUg3b-erOR4-hcdqWe8Xmm97HEn_5_dn_5I44eiHUc6ixCnS-kcYLPkknTDI5cji9I0FvHQCO0bYa0-s3x7rBUMVZObrrPTjQjckKU1NpfXA3g4huOyGzcJwR-serSUzfFHXX_7Hm5A-r7qDqWIAfsIhxfWkWKEmj_bOay0ChWb2hGrWDS8dE8gstkDLTVrMyQftyYaGIF0tUbbAAet6C4WssMDVIZcAT5ZANniDrbmx6w-pAMmKqZLVLG5FRLYAsRaJfpMdISwqQ1gm-AG6Q806zt4wV0073ht0namwyTEvIUWzJiz_c5HO5oT2YkYd_ya_S8OZAFTL-vnrgrfTYDZaP8cQYKHejjKZXCExhUm9OsK7pIF06TMQQRtgtPEQXSV6ngj-eOBJqdcKTROnTus6Eqy2WAqNDpAhuZNYemAasuhKh-SVqlwXdr20GIdke99AEv58e9FeLhxD21VmD1c-hvmSiHRmiLv0d20MyOKimTgqDyP1-G-6vWzL2RkmJyeSGVTrI764s3qg1NjcdmM_PUKdLx3gB2FX-KNnRJrcnM_IluroKuXHPEslKHo1goxkEUk2dE0gbt4_aHiBR8lNAA-5A5t5FiFVFBW7vkWOY7oBfdKobQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ محمد صلاح فوق ستاره مصری تبدیل به سومین بازیکن‌بزرگی‌شدکه‌به‌ترابزون اسپور پیوسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/27191" target="_blank">📅 10:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27190">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeYhb2jmQ6INLVbaXKEJrYf9NZ_YHpfWEJyHkNALJ1mu8V2Tex5XCMUW9EXIJMhcRFgA-YNcYFdaeyKtn7_-yKjp1BW1ezkhJYs7iS-7URtjkQBLuIA-lM3zz9o7-I4P6czWjeeaeTPn4sq5Smugo-QM4VMNDRJWhRFVvxcfT8NoTlBF3lG13QyB-W6MmsPVu9gTjS3oJdfukNq8ePCWNgS1AYppuIuWucDmKNygPx6Gp0FbBYE23ELLiS2__uCLDcEeS6RC4hozPYZC9c9KGYKi2sbgTuYhOAx4vr6ws1FdEQ2uuhM7vvGDwYd0Uof2_OhwioxdxhAqYoQqtNJHfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
عملکردخیره‌کننده لیونل مسی دربازی بامداد امروز اینترمیامی با به‌ثمررساندن دو گل و یک پاس؛ گل‌هاش رو در کانال دوم گذاشتیم برید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/27190" target="_blank">📅 10:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27189">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1ec418ed.mp4?token=po6VOI04kE1ZcndFRNZfGr71-zrg3KdVTsPj3y3VaFRbKUbr1-Du5r-yZAjHrlt0sRt9Df70M_sDL-zPs64GZpokDFxvWulOlnakiguWvc4rj4OGftecUSzyUFUj7GlnQtDaOyZk1O2GCR8XCvh2BMG_kPNNICk8vDsuGmd_LNPG2QoMwK2W9OEzJuE4zBI5s1Psd1SRi0saUsMm8HZsIg5iQZI4HH4N2KuPjHGC1FC_4oO5c_8ssRF6dNgelQlMksykY_5zl3Hk--ivLoZtyXUVaGeIJo3yb4bdB_NHnNocskmh6JGA0diRW8fThkT5X6sQ-T9BSzY52eNeKNClNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1ec418ed.mp4?token=po6VOI04kE1ZcndFRNZfGr71-zrg3KdVTsPj3y3VaFRbKUbr1-Du5r-yZAjHrlt0sRt9Df70M_sDL-zPs64GZpokDFxvWulOlnakiguWvc4rj4OGftecUSzyUFUj7GlnQtDaOyZk1O2GCR8XCvh2BMG_kPNNICk8vDsuGmd_LNPG2QoMwK2W9OEzJuE4zBI5s1Psd1SRi0saUsMm8HZsIg5iQZI4HH4N2KuPjHGC1FC_4oO5c_8ssRF6dNgelQlMksykY_5zl3Hk--ivLoZtyXUVaGeIJo3yb4bdB_NHnNocskmh6JGA0diRW8fThkT5X6sQ-T9BSzY52eNeKNClNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه بغل کردن جواد عزتی توسط یک دختر در اگران عمومی و تذکر حراست سالن به این هوادار!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/27189" target="_blank">📅 10:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27188">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33a3912563.mp4?token=Qz5LSCP02F0Mvj_MppijvdyWBayp9nJDM8VoNs08_aZds9WXdVquhJMQdqHOabEYxjQBM3Dij8NxJR6JjH31MUP8oZiJV-rOIIeGW0ogP-c-LCUb0Bo09lDr6XruZckNQuq1HnrFu4n7BjBFHPDtV4weaIYEV3dKdcHBOTrEWStF3_b5FPPVcecy0_09PHlsMIAoKMsLXeGo5fZs9iiAGIOkClGTp1R1wN9Z5363AJPxgi1ecVbtGY7ANbDR_b6SVtCA_kEHeMazW_Jzaaybf00HXKmu6zyO2TLoW6-_pqCgCfPfRbFaHyQyBix7ZzNVLtlE7O_MdsIkLSqjJrPUww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33a3912563.mp4?token=Qz5LSCP02F0Mvj_MppijvdyWBayp9nJDM8VoNs08_aZds9WXdVquhJMQdqHOabEYxjQBM3Dij8NxJR6JjH31MUP8oZiJV-rOIIeGW0ogP-c-LCUb0Bo09lDr6XruZckNQuq1HnrFu4n7BjBFHPDtV4weaIYEV3dKdcHBOTrEWStF3_b5FPPVcecy0_09PHlsMIAoKMsLXeGo5fZs9iiAGIOkClGTp1R1wN9Z5363AJPxgi1ecVbtGY7ANbDR_b6SVtCA_kEHeMazW_Jzaaybf00HXKmu6zyO2TLoW6-_pqCgCfPfRbFaHyQyBix7ZzNVLtlE7O_MdsIkLSqjJrPUww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
پابلو گاوی؛
بازیکن‌اسپانیاکه‌قبل‌ازجام جهانی گفته بود اگر لاروخا قهرمان‌جهان شود موهای سرش راصورتی میکنه در روز تولدش به قولش عمل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/27188" target="_blank">📅 10:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27187">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">چرا
3️⃣
2️⃣
1️⃣
انتخاب درستی برای شرطبندی هست؟
🔢
امنیت و اعتبار بالا
→ چون ایرانی نیست، مثل خیلی از سایت‌های داخلی آینده مبهمی نداره.
🔢
سقف برداشت
→ در ریتزوبت سقف برداشت معنی نداره و شما میتونید بدون محدودیت شرطبندی کنید.
🔢
بونوس‌های فوق‌العاده
→ اولین شارژت 100% بونوس داره، و یکشنبه‌ها هم هر مقدار شارژ کنی همونقدر جایزه می‌گیری!
🔢
فعالیت بین‌المللی
→ در کشورهای بزرگی مثل برزیل
🇧🇷
، هند
🇮🇳
ترکیه
🇹🇷
و بنگلادش
🇧🇩
فعال هست.
🔢
اپلیکیشن اختصاصی
→ با اپ اندروید سریع ‌تر شرط‌بندی کن بدون نیاز به فیلترشکن .
➖
➖
➖
➖
➖
➖
➖
➖
🚀
لینک و اپ رو همینجا براتون می‌ذارم . برای
جام جهانی
هوشمندانه انتخاب کنید
✅
⚡️
اپلیکیشن اندروید ریتزوبت
👇
🌐
RitzoBet App
⚡️
لینک سایت معتبر ریتزوبت
👇
🌐
RitzoBetLink</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/27187" target="_blank">📅 10:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27186">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WX7dUGvM5uErBXi84-fq8uVoJyh7166VCmhHrXFaSrwWuuezpEU4EqPk4ZgoOqHvjJfeKy3XwStUxvDPSBh76AzN-bzL3R1F9E2l7NM1vGU-tQo_Bf_K1xJYvR37-2gGGKn0-iXoYFiXa-f5oi1mXO17qSSTPpNQn9IlJQnVAW-rgDruXLjBxhAtjORYHm89pdDTxYQjVzMIqNxPrf2nHepxIwnlS-7Z-z66mikSUmZnlT68_vbrYI_l72iHhvUReDwVCDeMtE-rfcWYB-zmjsj4I2P-aDjLsGJybkdtmbYeOVQs5eWNoV8reJGyQ15Y9heuaKCO0Bfeu7p8Hoz2Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
نزدیکان دانیال ایری از توافق‌شخصی دانیال ایری باباشگاه‌پرسپولیس خبرمیدهند و بانک شهر این باربه‌مدیریت‌نساجی قول‌داده که بزودی رقم رضایت نامه این بازیکن رو به مازندرانی‌ها پرداخت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/27186" target="_blank">📅 09:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27185">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeR5mv4BHqSPZQ97stYlcrb9Y1Nq4lqkFUP8QQmV28ZucPPqY0HHDIgbb8Cf_hsoGFPOb_TlLD4O-SWT-5qk6KJZ2Cgg5FCul58eivrGK0eZjM7IfYG5DCkg5ur7vXRyJRlYIwXO-F5Wp-VKB1k1MCa0gbO6TvQytICyZS7vpuvseIyRoNJ2nSv5zS3nEbIgrqnOGnARcseS8qyUDQWCieRjeuPzVeKk5ADgyxv1B2nAqsmbHIsGtGG4jgm13AIPXaoDFt9aVm5kqX4k_wGBMGwwdWvjUzqLWy7xp4d9yuFLrbvTORg0eFVb7FrH1WpEHj77_F94Uy0iDvMSmlfoKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو آدان گلر سابق استقلال: هیییچ صحبتی با باشگاه برای بازگشت به استقلال نداشته ام. باشگاه استقلال به‌من‌بی‌احترامی کرد. دوبارنوتیس فرستادم اما مدیران‌باشگاه به من‌پاسخی ندادند. بر خلاف میل باطنی‌ام مجبورم از باشگاه استقلال شکایت کنم. اگر جنگ نمیشد استقلال…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/27185" target="_blank">📅 09:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27184">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rT5VCI-SrcZGqpIy_yinBUHBztA79P0FbGuFGM2Gd1oOggfOv6tflbKaWZJZhFAxDUjlDRKIijYayYQgQw_SgfKxKRzRIqWnJzHFqE3wWRL5mmiEzHwrTSPiRee5afhgKuPQUrC_xOXpg1rbJGzi49uM79qFgPpcN_GFyNyC7cgNQwmdlejOYsbNdjUhjQTE5_C4zNWe15h31JwcUgmjcQmD99eRmAt5p6A4oYu4kId7hWfr1L9imHSZ_CRiHrMy-dwfa5q3H0ZdiMV9Gn3gT7yWKtTimE55wSQReqD7fEbo6vh9DBpmzK36XYLSbhFikzEg0s1KyiLAycvm1fdABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبل لیونل مسی در اولین بازی‌ بعد از جام‌جهانی که از ابتدا در ترکیب اصلی قرار گرفته؛ همچنین لئو یه پاس گل هم از روی نقطه کرنر به ثبت رسوند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/27184" target="_blank">📅 09:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27183">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kN54es1U3C8dGcHeiUoxVMAa_5MhOi3mhGX9lAzX4ZVW6jgPjZhzaHk1HtuJX0JAC6tLmDymLnm3CCloe6A3aSaJpU1gKdri1YJ21Ddv2C45A53qJzZq0P63mPPr7ildObfb0Vth1gQcZb9DBBa1jywyzCkWfUt89FLUVQ1_PYt48hg9AGSweO4oh3qdQ9LJX6bsSWMrrgv8IoI0zgCx7ceMaEPw5cc3cNYrAj1On8yI8LQXlcO-v8DxJDuatDA9LakyCnfXrc7CWPEisD-IQY9OrQtlPP3q9MfC96RdurMi7D8cne5CRaO704dR5uWAUM64smD7YBlB-y90F6BZyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ آفر مالی رئال‌مادرید پایین‌تر از ارسنال بود اما وینیسیوس بعد از مشورت با نزدیکان خود از جمله نیمار تصمیم به موندن در رئال مادرید گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/27183" target="_blank">📅 09:26 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27181">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBzcqlvXJuNnhvFb3QNAyTAnuXZ9uUqWFZEJLLiJi8Ei4TAaC1Y87XKyCRDSDCaxZhm0U7mzuSba_mFPHxUBQqz3MhUxCei7QnHIyOat-oToHqPYBu9erL7OWygrzgaXKLtOM0UrugaG0PnC_s976Wej0Zt2rdyoLhwXN_2ehoWyhEgUH8p0eRdEDVJfYvH3BpCzLqtN-VrJV7vvYSofA6AocpuDRf0JGVXmfyohysWvAQU_yRRf0l9iaJz8OiqSKsvHlzfnI9LK9JbCM94b43Z4ulCnVxTtYaB1LjkvWWpGpBLayn7vzoQwzv0gJFgI7b4pv5-eeK71pCkJAJMYmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4684a0276e.mp4?token=Nm3rLF8TW4dK1HubfFlbVOSkX4QW6ULqo9ed3meHwHRnOs-bTb64clHvtz9QxzrD4QymVyFKv1NTKL02S1y96CwY97YbUsIEQ2_KN8xP5x9CVUg3QXI7UfjR57kJgxh37wh5UzTv92MvsfIob8vj2dEhV3k8RRakXOHWQaZIfNw2Nw2lXJ_pI0S-3rmWmeZUMZ2FZbZkf9euohgUEBUGll3Bnzj7F2dnTNxdyjsDeRP_gS-HchlRoZtxPA2o2eO55uQOUjJQCcVu7wrKmxrrq-w5cL0fD-bjEDoGkUy1-lAZx5775XM26golY9vhOCR8kq3JbOX3AK9q2ClCCBsvIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4684a0276e.mp4?token=Nm3rLF8TW4dK1HubfFlbVOSkX4QW6ULqo9ed3meHwHRnOs-bTb64clHvtz9QxzrD4QymVyFKv1NTKL02S1y96CwY97YbUsIEQ2_KN8xP5x9CVUg3QXI7UfjR57kJgxh37wh5UzTv92MvsfIob8vj2dEhV3k8RRakXOHWQaZIfNw2Nw2lXJ_pI0S-3rmWmeZUMZ2FZbZkf9euohgUEBUGll3Bnzj7F2dnTNxdyjsDeRP_gS-HchlRoZtxPA2o2eO55uQOUjJQCcVu7wrKmxrrq-w5cL0fD-bjEDoGkUy1-lAZx5775XM26golY9vhOCR8kq3JbOX3AK9q2ClCCBsvIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
محسن بنگر کاپیتان سابق پرسپولیس در کنار دخترخانمش؛ دخترخانوم بنگر دانشجوی رشته دندان پزشکی دانشگاه روسیه هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/27181" target="_blank">📅 02:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27179">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhEheoWubFcQAnkzUCH0O6iKO-dwRBi1UUZFJtK0BTK-5ZM2eOd6E_Y1wonQdCvMPgBkqvxTEpgDllq0yZtsRuFATEh47A8KgRhTSYhMzTwFmfHXAIuYq-JxBkicznn_4YAMO4eAu81nL15PWGyXVoLgu5EpFT36sgVHiU3R0c88GeNzvA6iqiY7PLFZRbANr7RuPPxQxPkZDnovsaFv-ESvqvQPza3d3fjBziVMEQw-KKZvHC_rTSxh47d4EAA-XKIsAhMbolSofFFdf-vX_V0Kdq5wTWd1QMx_NeHNe0SVSoRcgbGMdVOPWbzHnrEL-cUeJR09poCLVuY1GGUSaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ با اصرار زیاد مهدی تارتار؛ مدیریت باشگاه پرسپولیس بار دیگر بامدیریت باشگاه نساجی بر سر انتقال دانیییال ایری به جمع سرخپوشان وارد مذاکره‌‌شده‌اندوقرار شده که این بار پرسپولیس 120 میلیارد تومان پرداخت کند و این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/persiana_Soccer/27179" target="_blank">📅 01:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27178">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e55341bcb2.mp4?token=WoX70ySrdcC-BWsUIVqWP_M-mwNRBMNrJKpQPOvVMzEsg6C12P534TyEyKsB44Xhsv563HR7mNVtbbv0zceeG52xM9VfhFSM6-5CkWZ1sMnhQ6h6EeIpsJesYQdmPUSrNPs77x-8fBJvHwQ_7AUT8VDut0cplkD4e25c5Z67v_8oeVqAR1qRCsRM9vlK2AtgLKkYBBMdMdlK9vYCeVzjtP3Qoo-UQNpfIRWcR54L6JlXeYGpY1OaWqaPfPcncTul7rhPyC4bY6i_4chSrDDcMY8ddhKS1WzaTdMY-22AA6DUX4Sqg7wFyI4thKFNl_-8qE4eiWFu0kuX3e8JW-HUZV84Q8D4ElXa-uElwWxQ3VhK007wkUHAAC0sDpe-fcZiJXWXKWVT9oIeru4HG4JF7bex0u5VBjal3x4FugM8u3IEAmCFW_KIV6mWaGttyBZgJeybVGrPzrJ2sQtEKnUoRGhozftifpmx55RtMqVuNVGbVvD7kD6hrEG-8FnJZMCSx5J7dHd4nVcNjgBqNcUyYuQHhQC_mYNq5PP4nnCZ3H296nru0DDu_QWOfGNSKH2xUTzks6z6OgeLfQLZi13D65zzFrTT182yeVjvi_kxehsZFsn6q8w_bYy4JGVeC5i_1LBFhST4fRdxnbxx1cxJ4jIzTZmbC-FDEX1DTeDl4X4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e55341bcb2.mp4?token=WoX70ySrdcC-BWsUIVqWP_M-mwNRBMNrJKpQPOvVMzEsg6C12P534TyEyKsB44Xhsv563HR7mNVtbbv0zceeG52xM9VfhFSM6-5CkWZ1sMnhQ6h6EeIpsJesYQdmPUSrNPs77x-8fBJvHwQ_7AUT8VDut0cplkD4e25c5Z67v_8oeVqAR1qRCsRM9vlK2AtgLKkYBBMdMdlK9vYCeVzjtP3Qoo-UQNpfIRWcR54L6JlXeYGpY1OaWqaPfPcncTul7rhPyC4bY6i_4chSrDDcMY8ddhKS1WzaTdMY-22AA6DUX4Sqg7wFyI4thKFNl_-8qE4eiWFu0kuX3e8JW-HUZV84Q8D4ElXa-uElwWxQ3VhK007wkUHAAC0sDpe-fcZiJXWXKWVT9oIeru4HG4JF7bex0u5VBjal3x4FugM8u3IEAmCFW_KIV6mWaGttyBZgJeybVGrPzrJ2sQtEKnUoRGhozftifpmx55RtMqVuNVGbVvD7kD6hrEG-8FnJZMCSx5J7dHd4nVcNjgBqNcUyYuQHhQC_mYNq5PP4nnCZ3H296nru0DDu_QWOfGNSKH2xUTzks6z6OgeLfQLZi13D65zzFrTT182yeVjvi_kxehsZFsn6q8w_bYy4JGVeC5i_1LBFhST4fRdxnbxx1cxJ4jIzTZmbC-FDEX1DTeDl4X4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی از گل‌ های دیدنی در مستطیل سبز روی شوت‌های فوق‌سنگین‌بازیکنان؛ عالی‌بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/persiana_Soccer/27178" target="_blank">📅 01:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27176">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729a2d9732.mp4?token=s1WuGs4KSjM71S89nKYycsycmEn3LV20oVcx_PX2IJqb5NGrEbYxa5UleWacF6ifiX5MhrXrf5N8bkJ4tIj30KpqhTEd23mnpDz_MayLvjmuDwqgMwqIUb3GzclnaAq-ap9R5XbAsH0GZcqGZDvr1tGmwxtNbkMV35qXROLMsOU7JP0Tkwr36f7lUQ2Pm9vz7ef6NdfC4rw-FZ-RldybFbS91v6GpDEsczI1-K6qWRsMKPLAkX9dHQn6Y5sRxta-GMS60Gm0QSzRk4qGkJ0bUm8vMP6N1yrwdOwig7rZ_kdOHMEk7DebCD2gPOIrh3MmmCH3B4wFauQxzlPIJF9AoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729a2d9732.mp4?token=s1WuGs4KSjM71S89nKYycsycmEn3LV20oVcx_PX2IJqb5NGrEbYxa5UleWacF6ifiX5MhrXrf5N8bkJ4tIj30KpqhTEd23mnpDz_MayLvjmuDwqgMwqIUb3GzclnaAq-ap9R5XbAsH0GZcqGZDvr1tGmwxtNbkMV35qXROLMsOU7JP0Tkwr36f7lUQ2Pm9vz7ef6NdfC4rw-FZ-RldybFbS91v6GpDEsczI1-K6qWRsMKPLAkX9dHQn6Y5sRxta-GMS60Gm0QSzRk4qGkJ0bUm8vMP6N1yrwdOwig7rZ_kdOHMEk7DebCD2gPOIrh3MmmCH3B4wFauQxzlPIJF9AoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/27176" target="_blank">📅 00:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27175">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1mkK8TGGTTgMDa2ngVskWUmw2ND8k9j28PI-pkiomUpV2BzgYFw0-kJ4OopuNvCzIL5wWF63bslLufhV2MnYmTf43Scm3i6qHSJvePOZXVV-KLKkV5BzxYyVoehrzgaHX0-a301wzxZGAAa0xlCYIGLPCUWqZwCyQaQAXEu6dThdsdEM48AR10L3QML-m9F-QBfHtkZfllsfEA3tL-G2n-YdoDbjlqxTSWRXieav9ATf_OkFinzVyOq3-rUDt2g8Jd2pxXsXGhmpen1jv2cbGOFTFtxxnIzvZfJWWkuL97r5JU0jbom6oetAv4FL0SkPqbn4TEKyZCoBCUB3y0bow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه ‌‌‌‌دیدار ها‌ی ‌‌‌امروز؛
بازی یاران اللهیار صیاد منش در دور سوم پلی‌اف فصل آینده لیگ اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/27175" target="_blank">📅 00:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27174">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cp44nDugGDQN7WGqw1eCesFdZwcPf26-d5ZOoofuF7CUyNLmSZ4Qdb5ue_4_RYTd7t7Od9IPugKxJWTZslrXZeN8fMNNlb9rnpjtfEKBUmqNv_xsTq9tV4FcPLq-QV3_LsFGtrtK6ty-2nFMkMGTqJri9SXf9mzeTRNqQA3ukXfMbyMBPABHoZUYA__cn99_LyS8OoMTbhhP_VnhnNdV4wcquKGA_VmcK91tUDXoSw_UrOXf1sJbYxGZ1hZPMrlOZR50ZM-I908dqh2JwBnPFNfIzRT1xP4AlTATwGH9EWf3Sjmw91rXzYkqOPT54uHPCmP1CR2VBHTsBrlGWz7S9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای‌ دیروز؛
تساوی در دربی میلان و برتری شاگردان اسپالتی در جدال دوستانه با چلسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/27174" target="_blank">📅 00:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27173">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gd26SkgujW-vnz6cab2PZGloAXjQC-87oozRL31oJwQ9LLOPn8Q7y2N6nG-Eo0QwYpa4f_sAdFianBeV2tSGpLxX4jAmOoxxUFEKgsgWV7P1-82ZHnG_PTlJ9wU5Q5H0NFyg2IBy8-4KNDcleRcHrG-4xpatlPEn-SPcFVOHTgoTQ6nXGlyp77ewVyt_NCdisP22yMyIDpXq3LaF1kQa4ufGtSp_te4uHpWw42QoJBBzbvPxhPpO5fDj7RTa0NdtED5nzh2-bsHW_qyMXB_Vd825x7N9mB57WA-9wJewOhCNSp15kQkSJDOBJdn9x_KhunHV9E-uTrQriE3RORC0Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛بیانیه‌جدید باشگاه استقلال: تموم کارهای‌اداری‌مربوط‌به‌بازگشت داکنز نازون انجام داده ایم و منتظر بازگشت این بازیکن به ایران هستیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/persiana_Soccer/27173" target="_blank">📅 00:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27172">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QeJHsvkdfHZtnWZ5F4eBzLxtk8DdKa4eG5a-yhB26NW1jr8ltRkkPPOJzoHban9zFc8WV81FdNE6fzoK2fngSqyFE9T2LVsKS4jqO9QGAOtHpa5JleSATLMdnonM8wSIK5NWe9phxHvSu_ijiXTVOoAIg7ZfcLdE_Uwa4rllC37RamHlDlgL6QQc2cRMKJ_keeurUoELNDb5QRPKvIlKwM3Kgjz-lz2_vBuLQjera9HJX6FYmpT4T8A8YjR4todUqltBucl0rlqNkij3WIgCtE_xs-c2XtVoYjI5sRTkdFzJqRzrUwNt6t2fn9CWnmLFbPKL5KanV20SWnQmz7rRqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ با اصرار زیاد مهدی تارتار؛ مدیریت باشگاه پرسپولیس بار دیگر بامدیریت باشگاه نساجی بر سر انتقال دانیییال ایری به جمع سرخپوشان وارد مذاکره‌‌شده‌اندوقرار شده که این بار پرسپولیس 120 میلیارد تومان پرداخت کند و این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/persiana_Soccer/27172" target="_blank">📅 00:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27171">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4oXaCtkdQ9_f6towDPJTJBiopjDybnplYAd1tmKTTOkuM9ZGo8EdoG0kUNnnKCBGM5Lao40RVe1-U9qaaqely8UjQ0cy0G3DVwPfNwouhMnlK4y-nuDRBnYgRhDLtS46Tjk8_H0Q-SrgrbySeDG3yWQNwr563OApB_GkYQcZVRJit1khbEKF0UDb559u1ESoFJ82pQcWW2H4ywbhs8G-A7AHZ3E_8mp4qXzMriwrBoP3FZf1TgLAVNmYgueMDhxORSshEV5eP19MBfpo1y_syJ3g6f2tg--qB6EiXH9R8a-rhADKTLS6T3w-LCKGk4_b4maVHduJDYXxsgKVeSBfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیرو خبرچند روزپیشی‌که دادیم؛ باشگاه نساجی به احتمال زیاد به‌وعده‌اش عمل خواهد کرد و دانیال ایری رو پیش از شروع فصل خواهد فروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/persiana_Soccer/27171" target="_blank">📅 00:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27170">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPJEHP84WYf4xSs3RKYyI6DZ-mNkq6k_71yiOnM05yFpEdtBLsG81NxkrdkNCjf-GhCqfXD7MkPHBMIsfOuWvwKTeY5pwMiOsmyp--dIKzthSpk6FVYA6e77_BvW4w6zxD78x3LBN_3OfHP3ofOqBUjPHYmfTiC8VzDbEIx4T_At8gqUIVMPk5J5P781bwWNx1IUQihDJGZHkVTQuL3Ddzkl1Bvv7B6yqKwc3IM9w6h6bZonAqVIpvpEG8A2DpDsEd-CEH5X4yjUltKa7IHgOanqatepludIj3hVF881wiTPffQCYcHUH5vrEqPIKpFnDiatuZ67D1WSr8haF5ynNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
وقتیCR7 از اسباب‌بازی‌هاش رونمایی کرد؛ كريستيانو رونالدو با انتشار پستی در اینستاگرام از ماشین های لوکسش نوشت؛ اسباب بازی های من.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/persiana_Soccer/27170" target="_blank">📅 23:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27169">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2pO6GPux1Hf9Wc9nIgR6LItBJrQ166HxsmPb7e9g91hx5sMH4xFLc_DX-eXeLah5EqVHjqIgRZqrUD9_H8LuO17r_LvDKgg1LykDt3W_ePpNslJK50XcdNlZw3Lg9eM5n5TMHRvjn1SEJkzwAGZ8zLxt5FbVRvIttANGesaQaOvkDfJmL5adCYriVmV5hKoFYgZoo9vNOisyr7UWX10AzeWx3QyrasocYRg0iGE6ph3OBVoI2Bt1QgJVLzKzorkX9ZI4Fkyn9VzOytPogcwIZXwlirymOzkPDZhXoMrRepRoGteNtwUhdhVmnfoc8sqBW1fIlB37ZdFCbhiZq7FMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
توییت‌جدید علی تاجرنیا رئیس هیات مدیره استقلال که غیرمستقیم‌اعلام‌کرد که رای دادگاه عالی ورزش اعلام شد و پنجره تا نیم فصل باز نمیشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/persiana_Soccer/27169" target="_blank">📅 23:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27168">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqaqFZb5FULcpD_WcQkzkAQaksXERYmh7tzVNuBVPfIdMr3kJ3KzWyvvNl6AfLjzS7hFWMMYKWHKpG_emVE3sZTvVdwzZOSaynf7mW52tbUibnzSRV3HDQIOs6xSg6ei83nkigUEVxdPTTukI2p_Q-R7v_ofF7UzFN-wK66Nk8LbyIEhXL-vRICqetNQYUYROhfg47kdUlh3iRvgGlpaH76g4l5xVBRMGFc09QDBpxqkOtDnQ317deFyH30D0MBm_19PX3JUMnHg9yksx-6EhW16EhZHXAh0RtvUoxP6QAfWGW2Hfbqny94e57NkwxdBMSGHAbZBImv3sy71Pe3sXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
ساعتی‌قبل کارت‌بازی محمد مهدی زارع و محمدمهدی محبی دوخریدجدید پرسپولیس از اخمت گروژنی روسیه و اتحادکلبا امارات صادر شد و این دو بازیکن جوان مشکلی برای همراهی سرخ‌ها ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/27168" target="_blank">📅 23:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27167">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58266add9.mp4?token=Qqe6ljpu7PmUpjHt-AR_V4QgBiivRNcqxvl9UMMlzAm3KDwbtyFu16t_r_gGP8Ev5frsx2pPKSoigaeKmijc0A-95kI9AXGPfKIID0VZGitORai7tsetbuvoBAPPx3FI3lb8lwM4P4g2BcAXElz0TBbDYpMf9qgi-jjC2KRZ4OYC0qDm00LVondJRUp84cScrDnKK4FW7czBTLpx0UeKl60IEytciBZJaAXOAafrwE34wq2QvGpwfothqJoa3cHZIPvAMwCI5lda3cMojAa14czHec2uXITzmZGjbFNOoQ6tEk0FP04_V0Y8vrtOyYvz_9KqY2IfxfABoJ93sVvUyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58266add9.mp4?token=Qqe6ljpu7PmUpjHt-AR_V4QgBiivRNcqxvl9UMMlzAm3KDwbtyFu16t_r_gGP8Ev5frsx2pPKSoigaeKmijc0A-95kI9AXGPfKIID0VZGitORai7tsetbuvoBAPPx3FI3lb8lwM4P4g2BcAXElz0TBbDYpMf9qgi-jjC2KRZ4OYC0qDm00LVondJRUp84cScrDnKK4FW7czBTLpx0UeKl60IEytciBZJaAXOAafrwE34wq2QvGpwfothqJoa3cHZIPvAMwCI5lda3cMojAa14czHec2uXITzmZGjbFNOoQ6tEk0FP04_V0Y8vrtOyYvz_9KqY2IfxfABoJ93sVvUyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور:
🔴
اگه قرار بود که من چاپلوس و دست‌ بوس باشم الان‌صداوسیمابودم‌و نود روداشتم. چراباید دست یه مسئول رو درمقابل‌جمعیت ببوسم؟ چراچنین چیزی روباید باور کنید؟ دست کسی رو نمیبوسم. هجمه عجیبی علیه اومده. همیشه کنار مردم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27167" target="_blank">📅 22:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27166">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbd4624448.mp4?token=E4BLUzDAAhmbCeLdDDXScEnGqtfEem6mjOtuZMyTvMfrV_fFXKnFY8m-wiD4zdqv2TBFTlqdUcm6gTFPoAceO5ItQzyoG9UPxOolbc08az9O3IalITddv9j_Lu-oO8QD_hgicqpXREwVbZvwGD1erEBTS29kHAlUKlW0kc5flh9e3sJvlczLmQri36Hx85VwwrSGHLTSN9JAwxoj3bSOVE7m6eldjxamVpJ67BfzXt8lEyj_PIWlMJ0O7Z8jwLp58xfGjSbWU_2ZhA1hhxtqqfwGPPDrC6VaDIDrAyS48RUWrnGxBrOHn4ZMowbRP7a8AWUxv_Vk3C6qt3Rm0rxb1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbd4624448.mp4?token=E4BLUzDAAhmbCeLdDDXScEnGqtfEem6mjOtuZMyTvMfrV_fFXKnFY8m-wiD4zdqv2TBFTlqdUcm6gTFPoAceO5ItQzyoG9UPxOolbc08az9O3IalITddv9j_Lu-oO8QD_hgicqpXREwVbZvwGD1erEBTS29kHAlUKlW0kc5flh9e3sJvlczLmQri36Hx85VwwrSGHLTSN9JAwxoj3bSOVE7m6eldjxamVpJ67BfzXt8lEyj_PIWlMJ0O7Z8jwLp58xfGjSbWU_2ZhA1hhxtqqfwGPPDrC6VaDIDrAyS48RUWrnGxBrOHn4ZMowbRP7a8AWUxv_Vk3C6qt3Rm0rxb1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
باشگاه‌فجرسپاسی‌رقم رضایت‌نامه یادگار رستمی وینگر 22 ساله خود را 50 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27166" target="_blank">📅 22:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27165">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAAK_qC1tKOj0092CNCwlbkhnMKNtmeWDubr-n_Z90gQn-WwsNwkDFEqauEuFRRTXV5gnhqn5KLTtD-eyx8vGWqqJu59i-N8Yg1J4sh2-s_RD1Y9znV_G8OgdWBf15p5bFxqG2-UqHZTm4wBvSrjyWF10bBMYYirRDXOxVRLdGkQ3A2QD9nEmegIzkgT5VRsK_zRMgCILBDsWlVNNSrZLGzqIv8w776fwS78PPGmus4vdPNVlT21gZDvoy1hWSiHlLUFTk3TkXWnEwdAX2J02D0LKW6hz7Ladk8_fYbrgGhy6qMYqhfGIlVnlhK0D3ycmFTocw4kj8Mc-kf5d3n_WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
🔴
مدیریت باشگاه نساجی به دانیال ایری قول داده هر کدوم از دو تیم استقلال یا پرسپولیس رقم مدنظرمدیریت‌نساجی رو پرداخت کنند رضایت نامه این‌بازیکن رو برای آن‌ها صادر خواهد کرد. ایری در شرایطی به نساجی اومده بود که از مدیریت این تیم‌قول گرفته بود که او رو در…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27165" target="_blank">📅 22:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27164">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUiGdjNfzFoAArPPKML717WiUdiKHUBfdoe2XMqcmZASjs0P865qW2ZoufxBbW-ckyLnguk3Av2I_L8gWni4JVpzSFk79ucHMQzF8lVV4uvqFO698TKJEOpRjX45WINn50eEJ3UMuNnZZSgWlYc-b1Nyar6BsaSKuohxVekYnoazrYfKleu8bnAQGiL_ERraHZTungsZLK99NOCrn_EEnA9wPo9-f3veWDJ9_GUqaOrwpc4Qf2EEVvCIuMebqkjlgl7Wk0l9H6Z_rR-JNspZLW3ilDo55rBLUPwdNJyRzcgxCHyRrdKKZQVU6S8A7qJtwZwMyTrsdgIhEurRwVXiHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
🎙
محسن تنابنده:
وقتی‌حال‌مردم کشورم خوب نیست سریال‌ساختن‌ارزشی نداره. دوست داریم فصل جدید مجموعه پایتخت رو بسازیم اما شرایط جامعه به شکلی ست که هیشکی حوصله سریال دیدن نداره. هر زمانی که حال همه خوب بود میسازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/27164" target="_blank">📅 21:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27163">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAp933siHN4AlHjxSdMm2FgvQgvksZJMQC9e6_pwSuHn7bAghJcijuPs1HONI30xeL-ji1lmSxSeToik45MTJyrzCWAApVoYJSyODmR1tDFDT9nBPUtPp9Bfz0KOaAEog797XJtZyBmr5Ko_KtlJren6z9jbXBpKSjKeFDXwXpy4uKIwocb3Hz5znQinpz4sNgTPSj8iEf-11JSP61pPkBxKK_ldjnF53ps1Mc095BOzRBp5NxESFL-VBiXK2MBsmAakpOm2Le6fPMuZWaIzSc6NSEcthbMAaSj4-K5Vet1LZutCrgkO0ggVXFwJfaWQM6_oXSAD1aVbBOZ0X6B6RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اگه‌اتفاق عجیبی رخ نده؛ تموم خبرنگاران و رسانه‌های‌معتبردنیاخبراز موندن وینیسیوس جونیور در باشگاه رئال مادرید میدهند‌. گویا فلورنتینو پرز با رقم درخواستی این فوق‌ستاره موافقت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/persiana_Soccer/27163" target="_blank">📅 21:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27162">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPw6JhpXDMqdOyWJo6oxIT0qKZiexXLf4kJxDtN_zC1VE3gy6HYFxP9abShLJkKw-jnyMyT3kDBCgXL17DCT6g-0wkvyKfcIQMw5qUmsm8abvmYvdmGJtjZ_TuzR25Gk0iQ_bx-eeRNvLeUcHq5v9e2_0T5lwJowxLeGt1ii01srshDRxlK4oCq0TN-3VIL1mcRFF-foTG0uUa3Nu21kczOTao8zQbUS_I2KvtD03qg1MTtpxu0UFUruAXILHoa5vSIrC27mvbRD3xJpwUhHfjoQAYoUsgPPhLdIKo0omcvZoaw2rXfrMmAhwzm7jqJEBhML1F4jt0g0JdE29uxWyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق ادعای جدید مدیریت باشگاه استقلال؛ فردا تاظهردادگاه‌عالی‌ورزش"CAS" رای‌نهایی خود را درباره‌پنجره‌آبی‌ها صادر خواهدکرد و به صورت ایمیل به باشگاه استقلال‌ارسال‌خواهدکرد و باشگاه در بیانیه ای اعلام خواهد کرد که پنجره آبی‌ها باز شده یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27162" target="_blank">📅 20:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27161">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0ND_OBkPrmGwIr5DnBifO7ARc7Dmpjd3JDlHtsdDndeJ6YVxhUpmx5QORCBW-BGsfeoDLijUo0-6zXJV6psGTFR6waRIZRp0zuktdJ2MQAKsfO7SaaxmB2gH7vcER2yBs2CmWUXVrjiCON3drqA0S5DNmGrTRMr58UTzUg1Tc5Q0TpdDyCYYaL6wNZ4FRLsJCOUrM73dBZaNgiT1u3KHDHCPTO65kQQKdAF9dAF2TbfFgJr4Waboutm0G7pH0cfLz3F9jnDvFmB60ZcvKh-yFhO8ew3xQFEz5sjmHtDpA1JEC9-D-AUupIIDfPcEKQ_1S4YyisAo0_4eMcckaPL8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
ادعای اسکای اسپورت: وینیسیوس پس از مذاکرات با سران رئال مادرید دراین‌تیم ماندنی شده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27161" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27160">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhysrtX7e3PttxoBDDdxTU73nWL2GUadrmpR6ZyNMp9KZaqaRHZwMqU4Xu7VKxqB2koS9gJHgi7LKusjydiBD-hpNjvPI15_yd969RZZ59L8fS6LProqdx-FHectlLFpj9Mk8zndDK5sEa6Rve4noWbmTPyVFwAFCzW_XxN-313ffeHalV65DSzGtLaceU_Pa07s03G3_TPSp7-Km1KkCJB5KUjTV52VzIxJRpIXqDJ0Wr5PLe_QAmf9G9RAO4oQA9LtZJK1Xb_6ldiJlRcosQMi9QEWhYoxH-Cx42u1ymNqQCXwsVPo2shP17psWifua0zcLCxeXc6z_qaz5qHDxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
باشگاه تزابزون اسپور ترکیه با انتشار این ویدیو از محمد صلاح خریدجدید خود رسما رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27160" target="_blank">📅 19:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27159">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVQwu4272_hewISIrFAZ-KvKkybRquWvrG1tNJrUzAfCpwKDAVeV1ui4vxES7EdA3AuM7Q7r2UKbsqM41t-QlDTAdFct6fdDuL96sUC9EeyztRFVCUROjRthVm_DPCz7JnluDFDFVpAOvqJy9RVdbn_cjao4XSE1JcPsRSyJnGltHywMY3olfE718aZLiSa8tMgOyOvbpuO_dBBToiBze59fDnTk7bYjDDFIelAggbJShZ3EZEJC_j5x-slJ72MRPBsO5k4K3HRkXC9HqNqMgbgZWi0I7Er3gDrQdDG_3u4N27jFDgH3eP8cbBsZOLFy78mGjKWKPlRhO2DxpdOgig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بااعلام باشگاه استقلال؛ رامین رضاییان ستاره 36 ساله آبی‌ ها بعد از 1.5 فصل حضور در این تیم جداشد. مقصدبعدی او بزودی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27159" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27158">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9A5n7aqfwNBjYPPpQM76SdMfNcPIfZH_9qYCTfgtJrhv_y30efg_eh-WnoS5aW5ZPcSKu4JGSWiRVotSbawEgDryhLgGF2b2u6UqIFSlWdZqB8cJKvwL1IJ8NGlmiyQD1Sl-37a-8MY-IHfiA6aFDlJZmGuspogGZhu-IEeyNUL_PZ8FPfb4mpqv5I5b4b79wV2lGXY_34KL6onAA5Sl4xMU6PavgmIcdhy-ouKz3bfVlnvpGArb_Z1XCj6pi8bmPt2Nsk0M_7ZrdKUQSEM3Lk-timc1DzaLwQGRrCFNXrWXv9BZ953_fsZFuk_6Qh_DK2pe2Gj1UYpwxJGtuTgiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ امید عالیشاه کاپیتان سابق پرسپولیس باعقدقراردادی 1+1 ساله رسما به تیم گلگهر سیرجان پیوست و شاگرد سید مهدی رحمتی در این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/persiana_Soccer/27158" target="_blank">📅 18:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27157">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ez7dEhuBSR8cIz-_5R6P6n6ZXIE2LrEdDjvLbXBTyybo9_R28f9rQGQ0Yc__npLKQnEzbLug31R9avDQRm8Sui18erLNW1C7k2xY8Rp7wvZ0sfvLHq9eX55sZgQrGR_fKXvYB_yg3Cv8Hkca0oAoc7aFx73IwUPO21xCoxBZ7WJlS7npgvhhsCn41CXVA0TncFsp5IFVUs3Bjj6SqBan38OBBAW6Pk6coDKSzy9MqqKlPShV64waTLo9e1G8-MQs8iHbWqZjpXB351fxGW9ZndrOthqQlgvpIN4d_yNJ2QwEVZqER3rLOI7E8D_nAbLXdWhfmlwH27C4reZyXxrgKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
خوزه فلیکس دیاز: مدیر ورزشی آرسنال به اعضای این تیم قول داده کارهای انتقال وینیسیوس جونیور به این تیم در حال نهایی شدن است و این بازیکن فصل بعد قطعا در آرسنال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27157" target="_blank">📅 18:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27156">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxZiH9kiBZz8N16PWFKQ4dwhooKVAS7VS6zEwT_XXJF-dDVbXFg10VnyKUnmWVdtMxkEBDQ1rPFY1rEcGIWK_zdFlQLMIDPC8SCkRmEdGJQXA5BlA1OjBhHzEpdz_iOnpJbkNoLHHTGw_EwITdHfqvvw87gCK44Z3bwz4TIAAmvtFWTHP1DUOx7ssGBQTBKQP1iFaA8xY4bDgvrG9rJ_2qxztTcvEpGtIm4K49y-Y_RyEmm-PnZKotffn2TyVIN0O5cNvkDfEKtv9H5tdfi_SbpdqbXAJ_KWNwe7V2VftLpdgjLaW_GXNKinhD1d4U_Z8d_q50SLf39jbDif3mJtJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعد از کش‌وقوس‌های فراوان؛ امید عالیشاه برای عقد قراردادی دو ساله با تیم گل گهر سیرجان با مدیریت این باشگاه به توافق نهایی رسید و بزودی از او رونمایی خواهندکرد. بعد از اخباری و گودرزی این سومین خرید گل‌گهری‌ها بود که سید مهدی رحمتی شخصا با بازیکن مدنظرش…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27156" target="_blank">📅 17:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27155">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrvB9GM0urXQMY_5pjAHU8MjhimUOhuKvk64voz5ECeTXSVxq-l_p1ToVr7JK6SO0ztYfCBjQBy84WF58B835Ig-O415C5NYqc2NYD4fCuBHo1w-_3R4Sz7A3EsNKqhbsPFD3LQtahrxq6KzaA4iwE9DkRWmQGixt29SHQtjk7NdseZwR_oaJH5TAimqb5-fq7hV1YKBO54Pm01bXy0t1lwZ8rsfe7E43Svl5y7Oh2h8u6ySeXJQtwLc_DQM9qsPXWsWX7VKh7Q8WlTttD60eHl3D24vnEzgjOgGCT-WHYS1pF8eYODsZuUNodc2dPs0xv0570fmVeldIey4H0E-pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های رسانه پرشیانا؛ امیر هوشنگ سعادتی مدیربرنامه‌های رامین‌رضاییان این بازیکن رو به مدیریت باشگاه سپاهان پیشنهاد داده و مدیرعامل طلایی پوشان اعلام کرده در صورت موافقت محرم نوید کیا آماده عقد قرارداد با این بازیکن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27155" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27154">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9tcX7Ldvjynp7OYRvFcv9Vm7FVvUHDJYQw_yTHqirnG0sK0alucmG6_q2_ZKf1ouGaNM2AbngCmsSF3Lz7hNiWLZ7C1CfkB6_1QqaYVjB8ZzWq2Qkmht7acugVgEDK1bVoHx5ApUCoZyDsAnK6CxShDts7mpEJdygseiGCidbttL946Q3JKkxzwNqgxo0dtVASYsyzegQTerdE-dMk-ZplEtXvUnjNkNE1LcC6hVBq9nC2FynJ0RnjxRgOYucdBfpZtNofHPz2dInCzvBDUo0VhFK2X-Bf78DJtlsn1QQlPEOzd_IZYcima-133ANF8d83S6Oo4g6UZQVMn4ngNaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیررسانه‌ای‌باشگاه‌ماخاچ‌قلعه: ایرانی‌ها با کامنت‌های پرشماری‌که در اینستاگرام برامون داشتند حقیقتا دهنمون رو سرویس کردند‌. هر باشگاهی که با ما به توافق‌مالی برسد و حسین نژاد نیز راضی به این انتقال شود این بازیکن رو به اون باشگاه میفروشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27154" target="_blank">📅 17:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27153">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b7185f121.mp4?token=QzS6eeQlF4XJL6ppNF9YSTim4s80td2EBV85IHwpQ9bcUqFXGtLGLFViG7lcBhylDMHeEfvHjfRsQsyN-ThWaQIVUbFBusmm2QsaIPiJrEduFsu2wLBHJKvT9jy2Q24fNVu0VxSiLBccQ6uvMH0vUtuxD1m2NteNYgBkvM2wEiHT4D6W3doXpSQsmYl_LUHTVoIw4_rrvwjIUvN70drp2m4l_HmqtpSLJuIiTCBg9zdKMD5YOTvBREbuTCKBnjUkJn3B1jdn1_7qYrgTm_uCIhNKZimXkIK9nTp7sPJvb5V66uKT045JmP6Ej5JTVOuv3XTXckY9OjVDLIJqzr6pJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b7185f121.mp4?token=QzS6eeQlF4XJL6ppNF9YSTim4s80td2EBV85IHwpQ9bcUqFXGtLGLFViG7lcBhylDMHeEfvHjfRsQsyN-ThWaQIVUbFBusmm2QsaIPiJrEduFsu2wLBHJKvT9jy2Q24fNVu0VxSiLBccQ6uvMH0vUtuxD1m2NteNYgBkvM2wEiHT4D6W3doXpSQsmYl_LUHTVoIw4_rrvwjIUvN70drp2m4l_HmqtpSLJuIiTCBg9zdKMD5YOTvBREbuTCKBnjUkJn3B1jdn1_7qYrgTm_uCIhNKZimXkIK9nTp7sPJvb5V66uKT045JmP6Ej5JTVOuv3XTXckY9OjVDLIJqzr6pJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه‌دو دیداردوستانه‌امروز درتور پیش فصل؛ توقف شاگردان‌آموریم مقابل‌افعی‌ها و پیروزی راحت سیتیزن‌هامقابل‌کره‌ای‌ها در دوران پسا پپ گواردیولا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27153" target="_blank">📅 17:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27152">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drlhH2RnM-uPl444997yRYt4KIaeLqxyGiONaW4NgVUIWS7PdX5SQ9qWdoqCwwazIPXfbwMOWT-ccOsKB5X6LcQH153LziD1SIVnrPSHb3pHG132D6njfgp3XyfOhRQ6aCqURyfZeOiC462ZZSTlt9iYlTERlthW8AWtTPRASfSIHTmzOvJFt4nHpoPriUNrt4LvJ_QOm14PIpv_w-GzL8T5VCpCpXfKqj7X_cBW8PHcGfcMfNXOYcDGXRaFFYvIhDNOX2PbwLndCA4a49HhcOxNkCTJGXhzvku9sFQ0WUHLWcdWjUJl4681I4md9FnmeNbKGMmMRk83-huDWvDsCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛ازدربی‌دوستانه دلامادونینا تا دوئل شاگردان ژابی و اسپالتی در کشور هنگ کنگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27152" target="_blank">📅 16:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27151">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGftAHJGekMVwM2G9GAgjjl1qgwYGrF8b7X-5c7ypghBSBbJzKnNQm1hn1rs8rTctbSiUFY2YWwkeCXJzUwGkSWnpfixUqcv8hoUopvA_Vl3yTV-3g8eoTkjcQFkEVIMRPIJkOBi_gLuNIOk1RI7nlsXeQTxNuz-NswG3A40BPniPLZV-25Ir1R0_aoRfH4gYbLZq-zQ94h2Au-VZrIrxZdDzTkNH3DsvBFp2NWKYqkCWtpK6M_DmHZzRS8B5kWPhNMSRtnfWH43w38qNCiBqRv6S4YZXiet6HgoAoDfQL0xyu2U3hcQMdwzjsRW3eF8D_OfZzbquEHJSHVKwUf2lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
#تکمیلی؛ امروز سرنوشت وینیسیوس جونیور در رئال‌مادرید و پرونده انتقال خولیان آلوارز به‌بارسلونا تاحدود خیلی زیادی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27151" target="_blank">📅 16:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27150">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d917f67b.mp4?token=jHrM9nzXPekTwKnnBJgX2V-el3aenRPS9avfEpksMBFOIW_588QEEkMyw2tDdD2ptPQwmt2LJzclsAFf56ZixmrRk1ucVZHI0tqqUbAN7WdE67nktX7lBv9pzrlLpSbjczudTmb85gAtSHuXeU-gVi2U6yUEE2Sxfi8M5TgLHpUdyhEyNlkztnsj9Z6_SUbls2Td2BxVzLcYMtqGwYnjzj0gycu-N3hPFosq-smjOXk72Hg2LPwBevWNb9mui-GrGgqlxQx9xXzpmSTqX3gEnNe80N6rAK-7YtDj-E0BWa2qB1axC9GkynLDrPe4yaHdZe7pAUDEWg3quLBLHR-Qeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d917f67b.mp4?token=jHrM9nzXPekTwKnnBJgX2V-el3aenRPS9avfEpksMBFOIW_588QEEkMyw2tDdD2ptPQwmt2LJzclsAFf56ZixmrRk1ucVZHI0tqqUbAN7WdE67nktX7lBv9pzrlLpSbjczudTmb85gAtSHuXeU-gVi2U6yUEE2Sxfi8M5TgLHpUdyhEyNlkztnsj9Z6_SUbls2Td2BxVzLcYMtqGwYnjzj0gycu-N3hPFosq-smjOXk72Hg2LPwBevWNb9mui-GrGgqlxQx9xXzpmSTqX3gEnNe80N6rAK-7YtDj-E0BWa2qB1axC9GkynLDrPe4yaHdZe7pAUDEWg3quLBLHR-Qeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
🔥
فقط و فقط ۱۱ روز تا شروع بهترین لیگ دنیا و رقابت‌جذاب تارتتا و سهرابیولا مونده؛ برنامه دیدارهای هفته اول رقابتای لیگ برتر خلیج فارس!
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27150" target="_blank">📅 16:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27149">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHVvw0Q9NN-n10VYfCgBUh8RhLtLOVSvFuI1llEPESTu9bRWrw3XWUqaJk_dbdLW0i3xj-h8ucOfPsGLd90F1uYS7x4N3YOl__GbLcqpZMM_wvtPM2eCr_tUwpfAtxJ1khGXhpol_jr4Xxl3_BvKDvuumYy5ikKBcVUPlM30c10js4o1I2hEPuTjyScoNmM4TLwBuu0VpGtcLMn8NVSfWc1XODag7LKrCGC_GEkfOpc0-SLikruc7TCPS6y-iGBWH-Ej0Sy-VRQrt5iT95IwSyGNXrQ7wKtXMJTdUu1UBT8VhhZcTElBnc7exKjW1L-kNM-cxISVaEdsM3kONE8dQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
چه خبرهه زیر این پست محمد جواد حسین نژاد؛ استقلالی‌ها میگن بیا استقلال، پرسپولیسی‌ ها میگن بیا باشگاه‌ پرسپولیس... اون‌ ویدیو هم فن پیج‌هاش ساختند. انصافا شاه ماهی نقل و انتقالاته. هر تیمی بگیردش برد بزرگی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27149" target="_blank">📅 16:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27148">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315f795088.mp4?token=LEvRLyIp_liAwjvrJmPrUpWCOV3Lm6zXdH6KjPokkX9tzxcrURUzGJhCILsDQy0Xfp5rZdYxvIi8PM2CaWSuHj1cZMFKBY5YICeQuNsjdMhfep9mDcbGxaqe24LfhvleeSdDU0kRuK6iUczJ6pLa_8U-_rijPnewRx40gmMNWF4qrm3-fMYDXQBOhIOTeENhuzBthDWVTVjYZDQcTobDtdNjEPICn47VO-oq3biVub4EvFJ9a1xOsl2RTFEmoiqf6FmCyDiJxR0bYxVzfawenfJfBazKRR5DntnfBbXXWr1btcKBQ84lSwKonfRzglBHD_7eKQmzkASdcgbML1sH8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315f795088.mp4?token=LEvRLyIp_liAwjvrJmPrUpWCOV3Lm6zXdH6KjPokkX9tzxcrURUzGJhCILsDQy0Xfp5rZdYxvIi8PM2CaWSuHj1cZMFKBY5YICeQuNsjdMhfep9mDcbGxaqe24LfhvleeSdDU0kRuK6iUczJ6pLa_8U-_rijPnewRx40gmMNWF4qrm3-fMYDXQBOhIOTeENhuzBthDWVTVjYZDQcTobDtdNjEPICn47VO-oq3biVub4EvFJ9a1xOsl2RTFEmoiqf6FmCyDiJxR0bYxVzfawenfJfBazKRR5DntnfBbXXWr1btcKBQ84lSwKonfRzglBHD_7eKQmzkASdcgbML1sH8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
امید عالیشاه کاپیتان سابق پرسپولیس بعد از یه‌ دور مذاکره با سپاهان، فولاد و ذوب آهن حالا با مدیران صنعت‌نفت آبادان نیز درحال مذاکره هست و هر تیمی‌ رقم بالاتری پیشنهاد بدهد قرارداد میبنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27148" target="_blank">📅 16:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27147">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee60bdfdc.mp4?token=Fl_7-D9AIWSH2ZNHo8ddvDPhC_AlxiLEdyoGt2CJNge546ngPf2qlbpP5uea-5z2MY0zum4c5muBPFIjQ2wtXRRcZfQYqGuQg6phdoxq2JHvFv1tTp7vF6fHY4gqCqqFhdDAUnhLvMJ5frsbJpI83yLcB-ji4xJ-H8FNzYj04Z_4XGT5lBbKSnAzcPWwXozvgLL5JvkH985UvzxQPMQBS0pmeeQA2ttvY6j88tnPMlUqMbqI-lMwQmIJpC7TAObTr2Y6cOLn8_LYjJ6I7MZsdvAICBWdSdmm8kZ5Rc-aM-GHotxsQS_QQlY1PjFscM0HYSndYI91pJlDBO5juEYb-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee60bdfdc.mp4?token=Fl_7-D9AIWSH2ZNHo8ddvDPhC_AlxiLEdyoGt2CJNge546ngPf2qlbpP5uea-5z2MY0zum4c5muBPFIjQ2wtXRRcZfQYqGuQg6phdoxq2JHvFv1tTp7vF6fHY4gqCqqFhdDAUnhLvMJ5frsbJpI83yLcB-ji4xJ-H8FNzYj04Z_4XGT5lBbKSnAzcPWwXozvgLL5JvkH985UvzxQPMQBS0pmeeQA2ttvY6j88tnPMlUqMbqI-lMwQmIJpC7TAObTr2Y6cOLn8_LYjJ6I7MZsdvAICBWdSdmm8kZ5Rc-aM-GHotxsQS_QQlY1PjFscM0HYSndYI91pJlDBO5juEYb-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
توضیحاتی‌جالب‌درباره‌پست‌جدید کریستیانو رونالدو در کنار ماشین های لوکس و گرانقیمت خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27147" target="_blank">📅 15:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27146">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNuV5IGrww6To_in4A5ks70x0BOa5qFSQUlpsJnGzTPqDmd8qtiAaM4g9FepmQOXk09Wdhx9K8MJh3YC0O1_AbjL6d8ebgctY_y4-LHLCA5t2dV0GyI9RL77WDy2QQEgWAO2yFqOthlGeYIaGDKK3brobLgNFj2f4p50xf7jO5fr-VPWYYFN4VZryDvG5zFLo7SYqfNDAKSp2WL7vfcPt8SNEI3cLa1hwZJd0lwQU5WITlMpse7MA2htCkhmsv1-grPGXFvQz1kNpfACvb70V86NlMUhiqOOE1SfeF2KYxv0Y_NmHvPRmuwgBskA9hPdqSmv0PQYR8LRGTQrHW25Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
فرشیدباقری بادریافت14میلیاردتومان از پیکان قرار دادش رو با خودروسازان یه ساله تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27146" target="_blank">📅 14:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27145">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLcE3xxompd5lR4COvioXJdc6juC8QzWycF7r8q1zjost_5824ah_IpuuVG1IeLfgnbErXWpnSbYxwWSt-JfzI8qY2-aZdxtwGydydGtZ8KT3di7Gz2ZSqEtJDMXq5tcj5zriKrQXo7a03ik1p-xKVDgbshyoeSah3XDbyZKXdZ3iPaf1qF8FB6c_bgLy8eLkKE4vxJQMmuiAu4IZQewrOvgG0JGaOsVbRQKzs5Wyjm7SwDV_RrHNiEjXHquG8ftChbAkpXH19mM1eNZdz0ST2usvo-gT-f5jimxXqk-x1A9SSmvaAlYXN9aMgLCRZyePlftmodaRUKv-n4yi0cbFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های رسانه پرشیانا؛
امیر هوشنگ سعادتی مدیربرنامه‌های رامین‌رضاییان این بازیکن رو به مدیریت باشگاه سپاهان پیشنهاد داده و مدیرعامل طلایی پوشان اعلام کرده در صورت موافقت محرم نوید کیا آماده عقد قرارداد با این بازیکن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27145" target="_blank">📅 14:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27144">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09ea3c3b07.mp4?token=k4AMYJqc7qjn1jUPJgeWZEqmSEhtWBwySd1s2fV8T9LzKylHFhGgXlypFKTMa1pwqdr7PQnXKYCPrtWf1knF_f4pofp4SY5uRh6s5VAeFmIjFAPA_9moiZcH8vP3pKqdKlD8HcJYGoL034RG2Yjh0OS2n4ibIZSonmKCMQ9lVTBDim9yTh7Mh8pi0E06Xo0VL38fSk7DSP2i198ChJgbo9OggEmzF9TdNZcmFbgh7E_YYttpbEWmyyVS81GTbPWVZo5ioJjvixQjShME8xI90uztymxtw4WqjIbBBxEwiwoshfKV9sCFBLyMstEG_OSPSOrlgSfbDpMpW-Ul43lkp6BgUlmBPrZB-XdcdnB9HmolGgY2JIH1XobFOtIKRRF7O-QMkR8l-_Le2BIhbHzQQqXr6Vus5NXm-I_8rxdLjOLN7USRgo9L2rBbTFIjkd-ugzxVafmI1JNJZljPXCiuHKt31PL60pfId7SFhfDH-EHdlUIYYwjHJaNLz0dRb8FqT7PmsK_09NKanzZlcmtYHUu59rJ-vfiNyyZb89daONWFS3ylpBBe1Rz7KqiPTz4beUT45ynCnJoyxFJBVE-7Wz8Qpi9S9WL8Us11Rbpg0jS72lwhFPzZuyzsa0wfd8dsoaUlYv8guqAtaVsM2X4QRviYwjnth9KUWHZJEqMgGK4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09ea3c3b07.mp4?token=k4AMYJqc7qjn1jUPJgeWZEqmSEhtWBwySd1s2fV8T9LzKylHFhGgXlypFKTMa1pwqdr7PQnXKYCPrtWf1knF_f4pofp4SY5uRh6s5VAeFmIjFAPA_9moiZcH8vP3pKqdKlD8HcJYGoL034RG2Yjh0OS2n4ibIZSonmKCMQ9lVTBDim9yTh7Mh8pi0E06Xo0VL38fSk7DSP2i198ChJgbo9OggEmzF9TdNZcmFbgh7E_YYttpbEWmyyVS81GTbPWVZo5ioJjvixQjShME8xI90uztymxtw4WqjIbBBxEwiwoshfKV9sCFBLyMstEG_OSPSOrlgSfbDpMpW-Ul43lkp6BgUlmBPrZB-XdcdnB9HmolGgY2JIH1XobFOtIKRRF7O-QMkR8l-_Le2BIhbHzQQqXr6Vus5NXm-I_8rxdLjOLN7USRgo9L2rBbTFIjkd-ugzxVafmI1JNJZljPXCiuHKt31PL60pfId7SFhfDH-EHdlUIYYwjHJaNLz0dRb8FqT7PmsK_09NKanzZlcmtYHUu59rJ-vfiNyyZb89daONWFS3ylpBBe1Rz7KqiPTz4beUT45ynCnJoyxFJBVE-7Wz8Qpi9S9WL8Us11Rbpg0jS72lwhFPzZuyzsa0wfd8dsoaUlYv8guqAtaVsM2X4QRviYwjnth9KUWHZJEqMgGK4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به‌بهانه جدایی رامین رضاییان از استقلال نگاهی بیندازیم به لحظاتی‌که این بازیکن در این تیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27144" target="_blank">📅 14:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27143">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g55QY6b5tNV9cEsbZx4iEc4YJMrtwiVnv6HjF-MY309vxcI3YAPfaxVGcal4oDWHAsdHp9obngxcvC_bjEGtuFMf5hhEpB6sRDSi8Sl3KVPo0jh6-PyAIpAxMa0CPMTm4lfQ_0y5Dw8sMsF4Mlk3wN1lMvR_vzZh6mIEhEcd04dj8zyFXJbb6c8ZBnvEBFQ8W_JJ6-jXF6Q-HFawnJDGOWY28EbDifoT2rvWXewzQ5sm4dLY_z8oMDJ0jxh5pjAAHUQOQFMYu9OejKS5PMqPtT0wzDEuTIKiWIwqO8ND7FlbO5--uff9mp4VcSB1AMTrJ99A5evatjtJDLDy7CGsgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27143" target="_blank">📅 14:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27142">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‼️
اولش یه لحظه فکر کردم وحید امیری رو برده اون بالا؛ لامصب ته چهرش کپی وحید امیریه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27142" target="_blank">📅 13:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27141">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/590b770d9f.mp4?token=NGy7iWit23GEyeFT3CQoG7kQuYoDzfvVi_CoR8Imy68nv8Jo7lrYAQzss1ywD-vbOsdOwH4HA7gVCAcvatbu8PyiPIfa3LTb5tar1rgFh_mPFuVZGVM4P6Bxzu1rs8QNVsirCFL5RgJ7DEFfpJT9cDR0zpzHa95caMBfIe_5PL0MUZdvhuXHHNamSqUqf-3jQU2mMxvAgKvo4hdpJUxwb9UaQ1qB7ehNV9Plk99YkmuJWJBjDM5yxYafWf53hXOByI0rEwmsSaOF7y0EcWxSr_UzDwvSl_Bow11lpjQHCyzl7DCLJBqX5wLa2uSoVfc4xLF_LF2ZS62tnoLsBwcnZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/590b770d9f.mp4?token=NGy7iWit23GEyeFT3CQoG7kQuYoDzfvVi_CoR8Imy68nv8Jo7lrYAQzss1ywD-vbOsdOwH4HA7gVCAcvatbu8PyiPIfa3LTb5tar1rgFh_mPFuVZGVM4P6Bxzu1rs8QNVsirCFL5RgJ7DEFfpJT9cDR0zpzHa95caMBfIe_5PL0MUZdvhuXHHNamSqUqf-3jQU2mMxvAgKvo4hdpJUxwb9UaQ1qB7ehNV9Plk99YkmuJWJBjDM5yxYafWf53hXOByI0rEwmsSaOF7y0EcWxSr_UzDwvSl_Bow11lpjQHCyzl7DCLJBqX5wLa2uSoVfc4xLF_LF2ZS62tnoLsBwcnZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
ویدیویی‌زیبا بمناسبت درگذشت فرانکو بارسی اسطوره تاریخی باشگاه آث میلان و فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27141" target="_blank">📅 13:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27140">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇪🇸
🇨🇮
ویدیویی‌جالب‌ازگذشته سخت و درد ناک یان دیومانده ستاره 19 ساله و جدید باشگاه رئال‌مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27140" target="_blank">📅 12:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27139">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/varp5NowVhVG5pOZ6IzHU_t9XZQTInB_9oGbcZTdRkE12bR9DONWZwr5ZVw6BGYC0p__ybHUKVGVAkTQgS0mr2ygPT3g2jsIkVlPcueitqvuMdSvjO0TYuMIb8a_VDotLIy4byZMFpvvu3-agMs1vJDf_eiyRmqJ60x-YMfagKVXkXBjQF1-qmWZGG2QhayUdsQzCX31yWaCc7xWGRJhbovZXnXoshvwiAIj5sH_5LAZEsMiSxgpfKHxXfGjCxhpi2Xl3o5UB_d-2lKDCaQQPw6XZiMsUPEZj_VuVgaztZYZhhqQVYYEA6FaXkP0zRSXLhcmGl9ATB9D6VaVAO8q8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات|فابریزیو رومانو: با صلاح دید کادرفنی رئال مادرید؛ فرانکو ماسانتوئونو ستاره آرژانتینی رئالی‌ها در ژانویه قرضی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27139" target="_blank">📅 12:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27138">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVuyxs4MgPKOmui5EYC1S1muIJM8SHox5lnPSUVbHirM44JxjyHQPzypSgcmpkNYkQTGpsCTTJFLES2cJR6ksKrPdhyTpbSrEO2aRekuVidClf3fVubiXbLN_LWARx9QN4DYckcCc7Y_BNxwL7p6_3owhhIozmiDS6kV7WIYRQobFWspTS7JtWaPOWJcwfk70THM8bp-NVwBalRDeUcFNYck1pvysgYEkOFPbjXU1hG7QKZbhknncbR64_LakZ507Xfzi38Gj7uMUC1_7LlGw5RuciqY9lZR4JWSIShDQUiHnyIPBd-_ESOlDDywTCVTJgiwxgso3KGYHLIeXUtVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27138" target="_blank">📅 12:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27137">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1JTLspdtBjZGTKz8AN7qzq-uqcSk3o4jLIHNGAuxn0MXzobwyAk5erCTY5Er6_1-bE9wxZwgvJ8CAUbmT1Z7doZuaUsHp02ljRDmdw5_UnkBWjGyLicnwgHKx57BOrZTmoa64GAoKrj6hvoprtGUbQ5cFw6FuPB83_jmR9XiTt7sTR3itXPqPpYON0mZhIamDU0V1oqPhVs2QdIKV3objBKMlVyUucL8wZOBd5MsGbxJM6OqTVRWRhAfAtDjaAG30OdufPXj2kKD4jj1Vmi3IEP90DlDbP9S2XBQTTduhKYHYaBT33ygVWt65gjnvjji8VHcUFOAP03kRaYhy_mZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27137" target="_blank">📅 11:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27136">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca19ec3ee1.mp4?token=lLTqI3K7I7y7-udAVyEI7d-WU8g0ByH9J_3U-Y_vsF4NXCMJ0qJCUpg9-ag3J05r7YsxRn_N0AA8867CD5IF3GP24ieQep7ZxRYJ09vU_zihxkL7D_x1gUeTY_rbgtR_HcE-P2Vk_OFLNmGBsm6GY1vZRrYQof62SD97gGCuxgtIWqnrCm3f5a7HiI77oKibdsiqr0bBuhk8r-rQDvVO2Z4zNaVNWZhJnk7iUvqP0A1od7QCK6-lIzL2p4dsE5PCdnAyTqJI7RfygfbfTmVe2HY1-aUK7Rbsev_NE0KH4K5QN27bav9rXfVlcqwLaOrnyR35bYs7yhIAk45Ni6U1Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca19ec3ee1.mp4?token=lLTqI3K7I7y7-udAVyEI7d-WU8g0ByH9J_3U-Y_vsF4NXCMJ0qJCUpg9-ag3J05r7YsxRn_N0AA8867CD5IF3GP24ieQep7ZxRYJ09vU_zihxkL7D_x1gUeTY_rbgtR_HcE-P2Vk_OFLNmGBsm6GY1vZRrYQof62SD97gGCuxgtIWqnrCm3f5a7HiI77oKibdsiqr0bBuhk8r-rQDvVO2Z4zNaVNWZhJnk7iUvqP0A1od7QCK6-lIzL2p4dsE5PCdnAyTqJI7RfygfbfTmVe2HY1-aUK7Rbsev_NE0KH4K5QN27bav9rXfVlcqwLaOrnyR35bYs7yhIAk45Ni6U1Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تموم‌ شد؛ صلاح رفت سوپرلیگ ترکیه! با اعلام فابریزیو رومانو؛ محمد صلاح فوق‌ستاره مصری 34 ساله سابق لیورپول به ترابزون اسپور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27136" target="_blank">📅 11:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27135">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1ef6701e2.mp4?token=WSa7YnxBX62kEQ_CrjoNiuC9b63bqdDxVEWTN84x7-tEp1tow4hZzH43p-I33eFF3CHnXPSpw5J7XEmFgL1b-Mf54J76gGgrvgERt3AYPjURY3tXcBA-pZMvQWA1WE1XpT1IyUG0BxZ7NacW03xuIz-R3ThIC9b98Tqb_LlRudIzzm6O3_ROktfYgKbbe1X8DFMTEoK3EuaJb7NX-06MGAosl4OkWygZ0fo5-GORfyoDRc-9YzCl1Th86-hAX0SmDo6TJ1fDiRn2FgMThhecsKq_437mEmR_82IcUk9T8vSsAUWcDU4clqnRL7pb_Z20rwPw_zwjwpQxdD09q-vM1oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1ef6701e2.mp4?token=WSa7YnxBX62kEQ_CrjoNiuC9b63bqdDxVEWTN84x7-tEp1tow4hZzH43p-I33eFF3CHnXPSpw5J7XEmFgL1b-Mf54J76gGgrvgERt3AYPjURY3tXcBA-pZMvQWA1WE1XpT1IyUG0BxZ7NacW03xuIz-R3ThIC9b98Tqb_LlRudIzzm6O3_ROktfYgKbbe1X8DFMTEoK3EuaJb7NX-06MGAosl4OkWygZ0fo5-GORfyoDRc-9YzCl1Th86-hAX0SmDo6TJ1fDiRn2FgMThhecsKq_437mEmR_82IcUk9T8vSsAUWcDU4clqnRL7pb_Z20rwPw_zwjwpQxdD09q-vM1oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌تند رئیس باشگاه رمو پس از رفتار نیمار و حذف تیمش توسط سانتوس در جام حذفی برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27135" target="_blank">📅 11:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27134">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0rBjIUJKS73uDa3NPV-oG2kzH58UgIyp9FQacwMiWhT1l13YRGPq6iVFL1z05M5iVU7-SPvS0QV5OY5wgO8OwsH6jyYfoh6eaL-SjGYSh90jP3LJK6rpF0jP0mgn3rJ_EBVMrsIA1XlypS9t6GjUgxnzvEyDiyD-bd0yedASkoRcPVaY7_1qpCL6AbBz9IUxBA7I4mxDYoJhPi3JS7TTJktQtfzhnzaq2qeGJvw-kh442E1aJEM9OJqkFMa4IFbBCITGo22UhqvguUSck06mwgJBLCdlRRSzaHzFRNru1L2gwM2SWnMCbB3tdCT2G6kmYldRguanSequRjpgz4EYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
🔴
🇧🇷
باشگاه نیوکاسل پیوستن برونو گیمارش ستاره برزیلی خود به آرسنال در ازای دریافت 93 میلیون یورو ناقابل از توپچی ها رو تایید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27134" target="_blank">📅 10:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27133">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c293e9daff.mp4?token=J3BNCeYKQVRVLsiU-LnSE8rMCV9c0S_QfeW5vKcLINw1Ga3B1UoLW4G2rj5XeTFl4CytTViLgORCmV8kp9fYcHWy2CtbeVW4OFYveeKlwwPJ7NVzgcqDR8yZ5ZRbOq-gnEdKViIUYnF9dLG8oGvCSNNF1f0s4wnKbh6DknEx8x76uFFH7YjW2ugWVO3-6Tj90RTBhSv4lzhfOg0EcBhlPtqayyUFeUcN5NYTDbA4L02wx3z6UiZHHsquOTHNSbTSXWHsyR8P7W55AFWnDuKsTqd7L-vMXfaOp8aQ9Bt4JnDH4skleNJMxHXryS2z_7OvFU_wPjVtANt260TY8ZmLig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c293e9daff.mp4?token=J3BNCeYKQVRVLsiU-LnSE8rMCV9c0S_QfeW5vKcLINw1Ga3B1UoLW4G2rj5XeTFl4CytTViLgORCmV8kp9fYcHWy2CtbeVW4OFYveeKlwwPJ7NVzgcqDR8yZ5ZRbOq-gnEdKViIUYnF9dLG8oGvCSNNF1f0s4wnKbh6DknEx8x76uFFH7YjW2ugWVO3-6Tj90RTBhSv4lzhfOg0EcBhlPtqayyUFeUcN5NYTDbA4L02wx3z6UiZHHsquOTHNSbTSXWHsyR8P7W55AFWnDuKsTqd7L-vMXfaOp8aQ9Bt4JnDH4skleNJMxHXryS2z_7OvFU_wPjVtANt260TY8ZmLig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌تند رئیس باشگاه رمو پس از رفتار نیمار و حذف تیمش توسط سانتوس در جام حذفی برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27133" target="_blank">📅 10:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27132">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jABGLESZr-xSe9sW3ASd59UuFuBycnaovvRx75IRTp5yz19aI653tbDkimXo0hTUFGKgw0kjCkNsJWXmD5LCIBixVaL-p6bTXA95WawOP5NAs_g13wn5yaFs8cZUGcCK07Ru-8HQVPaI-BqPND5ARDA576HXSo5poRsnuXDb87U0MF8bqLGS3YaGd5Z7dwppyQjo5CWCzf0dw_f6vzVUhXOhhj6O_LXrzPcnVHgjx3C2WYHp-753rcpSmb7KhFcGVLV_lvEDJJfLmtBFHSAjlLnR4NUphdryaBdetNQgPhS1gUCzdD3AqrErqkyvcLM38XZHgLafWeQ9vpyktnJi8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🤩
با اعلام جرارد رومرو؛ دکو مدیرورزشی بارسلونا هم‌اکنون‌درمادرید بسر میبره و قصد داره که فردا بامدیربرنامه‌های‌ خولیان‌آلوارز جلسه مهمی بزاره تاراهی‌برای پیوستن‌این‌بازیکن به بارسا پیدا کنند. چند روز پیش مدیران باشگاه اتلتیکو گفتن آلوارز خودش رو هم بکشه…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27132" target="_blank">📅 10:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27131">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejAR0mdHjVLtlyHs_uw1P9cuI-2cnJzcoNk2-mtP91kW-q9WGgHcI2Rcn_xZd0lt7XKj413a1HAnew1odqcb04XoGFjb2386Wh_cDlaXUauLSNhbHjK7ryEWoru9i75J3APptcXHvTL8MEdyx9-RpCq_iJulBZCdVv4n_R_nXZvQ8_nmv6vMwl20EieSTkefYQpUOs1cNLtfr9hHXn9SD9fWY83FuxQFtrd2TiWaUBF9YT5nFzVvUmq4vwikRugAhg2-RqgSdxYxF9H9J3VmTPIILWDGdceyudKFwHmRlroRgdY6ZgaynjrYnqntVh8kh8s79XqvpyRG1ePD07NSEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27131" target="_blank">📅 10:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27130">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ranoe3fl93aKmTrmQ8vgU6AEmaeSmqE7y4AfwxlO8JUrUgAbbG8Q6k-nnjVgc0cbajMLc1xxe2QHiU3rWzf_2cQdZgBPdsaCwLNr3w3yviUGuKxmMbTOZSZcTEHBDuMKLDcom_J5otyy394ucm5tSqta-LGAwDkbW5wtq9-dZRBkDZw-wEx64qAIlEb0BhkoeRRYPzPAiJdi_qKOkBSkd5KT8iFxjr_aJRc-Z3LGCmXGVHGLB2VEx6ikxLAaD0h_UijlOVTJxUqFusWDEGFCpwjUvyHgSsAl6MRUq_qNzAlQIN9Oedx8Ba7Ufw1HCHqjvGMRT7VxjR6r0ZnSjmUwRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
درحالی‌تموم‌اخبار این روزهای نقل و انتقالات شده انتقال وینیسیوس به آرسنال؛ ستاره برزیلی رئال مادرید بی توجه به این اخبار با دوست دخترش در تعطیلات به سر میبرد و در حال عشق و حاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/27130" target="_blank">📅 02:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27129">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZ24lXrzom_XWFhzS_cQxInqC0US7DJiFjYeZHlIRvQMy9j-U4V0sOhm-srri6zN0WiddJZuy8sT_yqZUglyJjZiFccVonteZsu-ft4ms-SlksCQVQJnWzry2aR8lOq0Z42i929vu62VpyJtT2t4On5FuVlZR0RHMH7kQMDd2inYtGiyHx3n0pturtysbPBGdHP37e7xuP2yE3KvJEb3mCuysgnn_q5b1kNW2s7meGJwUMB3ZAIulBzyPYJ1i5zRdRPxc_V4NZk-qrr93yGI9yRkG6Hl5otvY5n-g_N82ANe6c1hqZrR0xjYr2PN9atrDsCE5NQJqXKOl93GaIy61w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بهترین‌و‌باکیفیت ترین ابزارهای هوش مصنوعی که از همه آن‌ها رایگان میشه استفاده کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/27129" target="_blank">📅 01:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27127">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAjnAIF2xi63gl3h9LU0vA4BzMRzjBpsaYqblKYeZ83VVaLPDMtSCdFTukKSa5FqZHzUA-rX3CcSNDGt8Y53EQWzOZkAN3p3Rd12PBIjwZPy0b68r2rgstzjwaDEXVCCdIrhmPtd0tc-FKbg6e8na8sekrEZk84YrFZGqRnVn8nbaKatMbShXt3linrgsQv2WAr_M0JpeMteJh7mJYhsCxPvrzb0a7MVcFkbT5JhmJQa9y3h-UvaAQRZFogJktDlMfD2cI-IbbcPKhIn9kY1Ttk1yjtVxFlEHWeTLiA6TBQ_6-zgtYTKD557DhI892C6IBqJXKeo0vxvyViYIzjy-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
ازدربی‌دوستانه دلامادونینا تا دوئل شاگردان ژابی و اسپالتی در کشور هنگ کنگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/27127" target="_blank">📅 01:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27126">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NV4mj6S5NKB-irb88czR0OooqvYViefEGZtIAN60JuzZkP97RX5SeprbcB3gdaNAAmXtYUIhnq5wsPXBEQJUz1vZ72XJy74wFf5Di1QqFrqKmiKkT6vQnxg_9JI0ZyjVle3B_22WXPTzq8m3zHVQV_shO1Spt4qkgyidhbOgvzvxryDefFbZCaTc8ehpOX92yULHMm39ynQkSY6iIoUmdJOLk-Pnb40kBZ7edXH-XV3ezNKKFAlDFLMFKSHsoXrCweaA7FCEJ2vZLCWKVBnhpyPbcGsBpDQ24CXx7wyL1BcvIDI0tdEjEHo0HiaXBlGMwg_s47LWIwph_MTpxsD5og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
از باخت ماخاچ‌ قلعه با حسین‌ نژاد تا برتری بایرن و رم در بازی‌های دوستانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27126" target="_blank">📅 01:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27124">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAngkVoT5WoTuJ-oDyQUta_2xjG6z3MwJrDy2O7IAg1Uky7fr3ivqR5QG7wfPLO_j8HlXZiVqxhFaT_N_a1OxOYKRDSo2OoIu0QuB-TruI5yIUOHXRdxypEHgsp2UT2toVDEwvcLCIt15wAGDCGUtYyF5xcKS92zap2QLVij9tg8DExkwhdAyLLyxAyHAJo2zNFIA7E27hLJgSmbMjCttO1CehXAKmVwad4MQeeVUnBKMFSHkLIVA5LD-KzfNuwCa6ivsuy2brJb_1iVNk851mgNC3UEKJKJrrx0cILX0JMHispA_MirvSIYvubmePnSx1iCdlw4_jeX_UF2hV1DYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تموم‌ شد؛ صلاح رفت سوپرلیگ ترکیه! با اعلام فابریزیو رومانو؛ محمد صلاح فوق‌ستاره مصری 34 ساله سابق لیورپول به ترابزون اسپور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27124" target="_blank">📅 01:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27123">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uomT_xO_p1zsCx5UiZlaAkfeVLpOs8poeYUREZiDtNqQJcQUMVmCI0gst6teIp6_LgMUrq-LiP9_K00tbTwmxVf_p4YjAdGbHd1aDlH16gL-K2Oo2KXlOmPQQ1_4EvczNA2KthDmEj1u57tqXv_aCrcNxk8zU0hiN6rP4egaic3hPgRzo34YNWd24h4INtKaxuaBLPttQA-VrlB3V3p32FtGIXUQ3yKmcrd4B6hvBhWax5KVxnpEjufvovRaDu7W_nK3OS9NhZWB64E3Q-SxBnyVtqi_NjbtNUAPJ6Fih0LaRHwzDXV2UUmchixGzC3DWMBw1hrWJg7-dwayHviz6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال: مسی؟ فوق‌العاده‌ست. من به نصف دستاورد هایی که او رسیده بتونم برسم بسمه. یامال برای رسیدن به نصف دستاوردهایِ لئو‌ مسی فقط به 455 گل، 205 پاس‌گل،660 تاثیر مستقیم روی گل، 22 جام، 4 توپ طلا، 3 کفش طلا، 4 پیچپیچی، 6 قهرمانی لیگ، 2 لیگ‌قهرمانان،1…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27123" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27122">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGG8ZmknMKQolZmvMzEZTiy6eNODVtUlsNBw9eJVlXHZxfyngHfhxUYKy4G9l6x1Yv214GhLqwGHduhDXw5eBmfMHRiU8sRrZBevASAobFtYra7fakS-1Ph3smpv4OIscghvxrK4uDqR29xjopcnniJ_wr4gPO003ROEv_8zCedd13TYDcCtWRb8yBbzMYNoJ6W17nNn5lOvEYwYEgSbA7XpC0OmvlxM7X2mBwF73vwxigrQc1EUNeruoOuwD-VdX5t41kCIr3W30m4ro2_oeKR66Hyk5funV-X_rQcOE2FQFW4XMnsc9uoGGVwrghL9MpT3gK-mZFrjGDOMbeC5sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سعیدفتاحی معاون‌ورزشی‌باشگاه استقلال: قرار شده بود امروز عصر آقای رامین رضاییان همراه‌ با مدیر برنامه‌هایش به ساختمان باشگاه مراجعه کنند تا ‌اقدامات مربوط به بازگشت او به این تیم رو انجام بدهیم اما برخلاف قولی که داده بودند عمل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27122" target="_blank">📅 00:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27121">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9i0Yl6TCJo63JqNn3SmbWhbUI9qg9EErroFNHB0qeBYiFthkUGiIqXLvngWpHoKDtxkuEdWQ4nkamhTWWU8E0MC2HzbrcncmVKXOW5HmBeywUKgGxhPu8qpObmJrXSBO0kaVTimCGZDjdh8FLnAKyKi8TvcxbFMU9ftJwwg5n4otQH2Z-X_p7FyZ2oeBZe_YSB8lmL_kVy4z2f6IiS_Rbxf8L1RxVWI4laIWVubS1SazWbqoL5FLrKMmV7Jd9o8rhBa03_duDzmOsJKKMTxmeWnCihwH4Kr80zuvcRWFvngw68_Hsi94tLmDWogkPNLhQ-kAA5blFj82rUzggd_qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
طبق‌اعلام‌رسانه‌های ترکیه‌ای، محمد صلاح فردا ساعت 12 ظهر به‌استانبول خواهد رسید تا کار های نهایی برای عقد قرارداد نهایی با ترابزون‌اسپور انجام شود. ازطرفی‌هم رسانه های عربستانی میگن الاتحاد میخواد بارقم بالاتری هایجک کنه صلاح رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27121" target="_blank">📅 00:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27120">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPZAvjDbLVjssze7Y_IMHGyfroXgG5ZQ2YKqS-tSAX9wLC5mhXksJJjak8jwPuBC3A17Pdtx5GYky4v_nQUV6WGWotqZvHHkS3UhB9aDvd9tat1b8RAkN3ZmP3dvLMlFt4gl0Czwp_BCq4Uqny9aPU8fyZclvNGMIxKZb71d49MWuEcalSOVOmRVBy8R9dB9VUGdrvgtxaHH5L2mTWlkh4Z-i3LeKC47eZfnhh_6fizFJFoI3O5D_hQ8yAgbcwBQT0XdAGDAZZ4Qsa4IWlmYamgnym76Ea6PiEKQPz-cqiyS96qff4gJX5gCpisvlD3X3wXwtRhKnhuYTU_YiTpVew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال:
مسی؟ فوق‌العاده‌ست. من به نصف دستاورد هایی که او رسیده بتونم برسم بسمه. یامال برای رسیدن به نصف دستاوردهایِ لئو‌ مسی فقط به 455 گل، 205 پاس‌گل،660 تاثیر مستقیم روی گل، 22 جام، 4 توپ طلا، 3 کفش طلا، 4 پیچپیچی، 6 قهرمانی لیگ، 2 لیگ‌قهرمانان،1 لاریوس نیاز داره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27120" target="_blank">📅 00:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27118">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8a21ccb63.mp4?token=jYYjhkTBRazf6Fnod49ALjYvKYjUZdsJiR37jqRs2odYmkMrmuG7ok4eTqwMIkLHA8KwZ9-Kv5FFMV0PUt7HExbnkZ2Ut-mFcn7WWOJelOk-4MiOC5CWYibhXYPo4le_bQCr3VkNW2dRvnZiaNx78sp1UWf9gv7r59_9as5roV20JTGxNpNvlW4Cmkjci8aS26gsw9yDacm6eujiFJmN240pX63x4FGlIL-ymWI56fGMZOxq64UiJ9aIGGtQMyrgDTd_0mL5Q-tOCK2RA3jSfbzfz8ZR0K5oC1NdC_5KnOl-dkatOvfb36Sb7sNVOJ-h7GL7R2TAHcL_s6eOp4dRVz8_uhrumvcBiX3PKTDl01mVezmeqrl5GfWbhY-Vs2cxCmLpQYlzzBrz5bjUJg831j3JShUd4Y-Iu_lUWXjlxk6uNpRj5Ls-HUSpxZ0pvr9kbwG0qCo-BPknPXkx8NIOoarTXNe3IVb9GvOrIZpcNoNJ9ZIVrSWCvWu8qN8PL3i57XnU_QQGtoQwD8d-jo40n80t1flPvJxsC9F7nL3AyY7v971TsxCYS-KgkMGblf4tp56rlx_3hEA71Q-_E6N6HqcgP5JQKIJzUxpseWSl-lM0X0wYZfByQFSvb035Zss1kBHf1aW9NrPD89qpOnw7cVs9cVQ0eefY5_QP_dPo-IE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8a21ccb63.mp4?token=jYYjhkTBRazf6Fnod49ALjYvKYjUZdsJiR37jqRs2odYmkMrmuG7ok4eTqwMIkLHA8KwZ9-Kv5FFMV0PUt7HExbnkZ2Ut-mFcn7WWOJelOk-4MiOC5CWYibhXYPo4le_bQCr3VkNW2dRvnZiaNx78sp1UWf9gv7r59_9as5roV20JTGxNpNvlW4Cmkjci8aS26gsw9yDacm6eujiFJmN240pX63x4FGlIL-ymWI56fGMZOxq64UiJ9aIGGtQMyrgDTd_0mL5Q-tOCK2RA3jSfbzfz8ZR0K5oC1NdC_5KnOl-dkatOvfb36Sb7sNVOJ-h7GL7R2TAHcL_s6eOp4dRVz8_uhrumvcBiX3PKTDl01mVezmeqrl5GfWbhY-Vs2cxCmLpQYlzzBrz5bjUJg831j3JShUd4Y-Iu_lUWXjlxk6uNpRj5Ls-HUSpxZ0pvr9kbwG0qCo-BPknPXkx8NIOoarTXNe3IVb9GvOrIZpcNoNJ9ZIVrSWCvWu8qN8PL3i57XnU_QQGtoQwD8d-jo40n80t1flPvJxsC9F7nL3AyY7v971TsxCYS-KgkMGblf4tp56rlx_3hEA71Q-_E6N6HqcgP5JQKIJzUxpseWSl-lM0X0wYZfByQFSvb035Zss1kBHf1aW9NrPD89qpOnw7cVs9cVQ0eefY5_QP_dPo-IE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
فدراسیون‌ والیبال‌ ترکیه‌ به‌ این‌ شکل از زهرا گونش و خانواده‌اش بعداز قهرمانی در لیگ ملت‌ ها تجلیل کرد. گونش با درخشش در لیگ ملت‌ها یک تنه تیم ملی ترکیه رو قهرمان رقابت‌ها کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27118" target="_blank">📅 23:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27117">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TW9-pYsAXhsB4E5bAGIJCOszY3lFXLmvrOTcaQILVJrz71N_vyy7GHY7hSlkzmqEQS44FgD8U82ItUJKQOSSF3b9L5wFWGs81jKJGvcsbjBpzHpEAlLtyI8UizZDKcYMuEYOJF8zakg01gT1PnWWMRfGL5vnhvCyGeY9KaCirsTAZvZnMlnqEHI9Q_AejKBRW-kQqGd4CK37rzRRLzSqHtC2IsGp_m7k5OV8nwgUTY3XPoxo-aS4AZs721IF-TL5FA4K3OmkCGVLdhR7khFMt9P3kWfI6qm6ZFUqYmefPnrlp_ytvlC5SE_6Di3pEQ9q9TZgprZqajnQHfkT0dQkfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
رئیس باشگاه اتلتیکو مادرید به زبان عامیانه گفته؛ خولیان آلوارز خودشم‌بکشه نمیزاریم از اتلتیکو جدا بشه. 100 میلیون یورو که هیچی 200 میلیون یورو هم بارسا بهمون بده آلوارز رو بهشون نمیدیم. مصاحبه های آلوارز اهمیت نداره. او موندنیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/27117" target="_blank">📅 23:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27116">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qS4SG3FCcFQns--wrHv7UK6QFJwufBxWa_eGeNI8w3tMYOeYnbpvvIM3fHrNyhvsfrH3J_EjGgP3YTNz7rjGy8nbiaD-fswILMB7yQznhDfZJ16CTJZ5So7O1839dIMVcI3LHeLMt3MtInkHhWW5hOCxF51KCK2DwmPxF1zyKa5pdqrLPlWj7-60uEriV-0mqSOc1NoAGz5IlMlZDPQ2eAoy-mEGNhG2XN9hnEBPigdsffxjXYQvNAVqLckNO2VSKuIBFSuieHanTv8prSn5OIVyNnAjHu93p26fVbd5VEi8gR9HSLy52Mn3VNuKlCdozGxn9dy2T9Ne0QPPUGPyAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/27116" target="_blank">📅 22:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27115">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52510ee628.mp4?token=V2hzponyMCtQQv4-Zm_J51rL5g2guEJuF3gUYaUb6fHOk3Jbru4sDc-5UmdHW0KAsM5pjd-X1XqMOpfKzym-cC_oHhOadS9ewWduW032eZWorjf46yv-ZGnb1ja2Xpr1r8IdPT7tgSIGdAhXYSOwcwoVmZp6Y-aiDNOJXNPHI9omE55RALXnoUBUM4x2oxn96Kqc0plorJ5ZYg3xGYm_ADgbMyK6DTAaVQrsZNCYEspgMoiFWAeMvngL2mb_mOaSP8W_ehuXvB6Ji3VBDajxbLhsAxH5_Wt1xN-lSTS4STn5Hvte834tZLMGkipByaAt__Pq2McDAf77_FoPS9OLow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52510ee628.mp4?token=V2hzponyMCtQQv4-Zm_J51rL5g2guEJuF3gUYaUb6fHOk3Jbru4sDc-5UmdHW0KAsM5pjd-X1XqMOpfKzym-cC_oHhOadS9ewWduW032eZWorjf46yv-ZGnb1ja2Xpr1r8IdPT7tgSIGdAhXYSOwcwoVmZp6Y-aiDNOJXNPHI9omE55RALXnoUBUM4x2oxn96Kqc0plorJ5ZYg3xGYm_ADgbMyK6DTAaVQrsZNCYEspgMoiFWAeMvngL2mb_mOaSP8W_ehuXvB6Ji3VBDajxbLhsAxH5_Wt1xN-lSTS4STn5Hvte834tZLMGkipByaAt__Pq2McDAf77_FoPS9OLow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
درمصاحبه‌جدیدخانواده‌نیمار؛همسر نیمار از قلب بزرگ او گفت؛ ازکمک‌هایی‌که حتی دور از چشم همه برای اطرافیان و گاهی حتی غریبه‌ها انجام می‌دهد.
‼️
البته ستاره واقعی این مصاحبه شیرین، شیطنت‌ های بامزه دخترکوچولوی فوق ستاره سابق بارسلونا بود که تمام مدت توجه‌ها را به خودش جلب کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27115" target="_blank">📅 22:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27114">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSAetAhKo8v0EuUMtp8NTckxgh6Mq_96V7ySIXlOd_STrm5UYt00hNm4jmyWwCET3cSJ4beWiBdesRVwtn16QEvbDATHOHA8eIyYJbsSoR6S_D3H-E48UVXl2_X8Kh8EoloSfYT4C2XrKe3I0g7HFnc3DLZEzynx7lrRFOI-2TS-ZXb-aLNYRqPkE1n3uGAKbKM-JrgRx2bEsjX7U21WBHtKQvtQF4PiVFFY05tJ-Ymsv89uTvc9Hv68BT1HYbVGBie70irYLGPVpn-WAgvn3Sc0x6q7Bg8-2JqndvqO8PMN76ugd-3Tu2p82CFa_GAVCBLB9AbWlcHyBBNYtIJdQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌انتقالات|نشریه‌ سان: سران آرسنال به درخواست میکل آرتتا به‌دنبال جذب یان کوتو مدافع راست 23 ساله دورتموند در پنجره ژانویه هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/27114" target="_blank">📅 21:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27113">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfXIliZj7L8MiTeVyazESDwovaj3B_QNg5kjZQgK5JlcpminZZ4Sp6CoXXYBYPiIH0eQt4hw3No3fsrHgztCt9zRFyOH6XWAO1i2f-eQBpZFJQYuHxGufVajVZZpepT9hzRFa_lvBw8I2Y3VXVcjoG1xJxVwGkAYq9Vif6sy5V5TFQBvcT7hCf8tZ5riW5d7HXDzlAttCN31F5DA44DnV-6VvNYL5tgQWVycq92oy9YanDL1IyHxI-Mx43kJJnmPHbsUmdhAzcZn-2AoEOZKYZHcLNlCr3V2ItSaQAGTIxILTjSRFevxkhVTorJQ611E6-AeLH_TDMTcctwRt8kNxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس اسپی مهاجم رئال مادرید:
الگوی من در رئال‌مادرید کریم بنزماست. میخوام با گل‌هایی که میزنم همچون او در مادرید محبوب بشم. برای دیدار مقابل بارسلونا در الکلاسیکو لحظه شماری میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/27113" target="_blank">📅 21:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27112">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlJruvSUOImFEy1Jl8lG79iAuJw64haMHF2ApYz4p19STwX7KkYwPrGXhjHMlUioGGUgIrIlXzdlvF908oFg4Vm8fr6TUDHBgkO-PJCHxG_hdCcrg7XwrcuMhwdSRCq4V_-AmJ5jmDsAZdyL8N1Biym2eMWMYmFO0S0FTWpDDw9KCh_aUrGfqvxrmZAZU2BaLLdyJ4A_tfc4_8RmRtUjLgu-K3wmkRWwD5ZntBByGcPr4wtaqLDNSXgzvBfy8yCayCshoCCDdYraGptEHg_6hm3C1i79LuRumGJc_nPSMBk5euOxG_EMwIzR_astJg9EioxP9o9itLLz2aCjHLLcCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/27112" target="_blank">📅 20:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27111">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHb8lE8sxHeRNq48ZqSGikUeMi6i3AmVy5tKOdVzHRVRfaiNtnQcgZAUDu5BtpU3BRee5Xn2V8ZoZlSsaFETTxl8pt2M1pYFWSXBWbBz2wSBNFKm5xcT_wCc-gCLvew6VFle2_IsMoS0wMQo8NWTabG3fVQY2Fll8ZnckA1o30230bu6SsxQesZ_2xqwL3TGB81Oa7cSH1JY8EFRsZrL3h9556I12dhhGk4gPhVkc1ksrQyhzA8vJIpPgsBL-EhHbW_uB8_Z0IBkqNlZSUpVbp_rxLutoWmY_rW-rOfXDhtEvbNyVJpSEbY4lLEANLgHfC6LkDtfviMISLQKK4xSaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: باشگاه ترابزون اسپور ساعاتی قبل‌پیشنهادی دوساله به محمد صلاح ستاره مصری سابق لیورپول داده و منتظر پاسخ این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/27111" target="_blank">📅 20:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27110">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFtmInMLRPmiSdJISdXLnImgy2ifNcakTHp-ezZNhyTsBRIuNowBWjArvP-UsDQ9MuUoTBIa6B46BO3Wa8mgFJSgSdRB4wyZWfRj0PCTtBFESjcFgVYVfIKepR0y39OffWBz8NL__y7T3n893kY3cmcJUwEB2sNu5_gwrZqGgY6FHQiNtw9NafrXPw1fd5_vnC1DkwK_uSdM1pVcztw3RFZ4tRQO36-Rz8N88BkTzYfTBpImtLvlBuigO-Y83WdSMip9ieZkEPVSYq8ENAwbw2v-JB2mVyXZ3psDffdX0wIicdA0sSkTjXWqFNM5arYOYJZmezCq5n7ocmJI-HIpBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
استوری جدید آلن هلیلوویچ هافبک تهاجمی کروات سابق تیم بارسا و مدنظر باشگاه پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/27110" target="_blank">📅 20:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27109">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRSakOwvKRb4oDw-3DIOQ7hkc914zciJu01Zef-_b51V8QlJpSJSN87W8z26YV8J7iNk9NL7ACDIzcyOpFhYuJgV47apF8jyN-QbuMudecVZFKsk8RcGhtXyfKDlaiTsMe0_sHHN-k5Kh7Fa5Cl8MTBLjBDChybNhVB_2viVJuBGaALBe8S1eYQP71X_rNzWHlFoW3mBkEDkFnhXWS4kS0hv-PZ3eNyLWGXvvfQQ4NPkjic1qZSm36njNRo6SWEpWfaJiaO_kYoM20gMbxO4KVUKEL5cl9K_qddxiGtiCG4PcDIpLMlu7VAEw7pNvImaiWcx1KLNFJktQVwYqD71xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
نشریه‌مارکا: انتقال رودری و یان دیومانده به باشگاه رئال مادرید نهایی شده است. بعد از رونمایی از این دو بازیکن پرز پیگیر باستونی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27109" target="_blank">📅 20:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27108">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekNdXXCLgz0ha7Ws-0qjPh3i_jtl1Gg9M7SECUB9aj7-R9s3hnkFufpHeJD8lOsIFPbWAZLtPaCU4-fyYRfvhL6QOtZ7Zfl8g3dStiU912Lkg2OyG7kowJl8j1uHcUUziZB625nIPmMSsO3d6RbxqqCAOm7Kh7Souz89HoSoHA62INLfXYCobh7ugD44vgNm8QH0l86blKepivjPfsL-9j0dyhMEy9Pa9ZvLT4NnXygSkPeTimEU4P8OsXYKxPrJZSwQzL5YB7EEacFaQA1KfxB9m9NuWcBMIrZgSZ8fID2BvHbmD5Fen7qDplj8fsiIfgOUcfUWk3a5x6ainIJ6Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
پاسخ‌نهایی باشگاه‌فولادخوزستان به پیشنهاد باشگاه‌پرسپولیس‌برای‌خریدابوالفضل رزاق‌پور مدافع چپ‌فولادی‌‌ها: 200 میلیاردتومان نقدبدهید تا ما هم رضایت نامه رزاق پور رو براتون صادر خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27108" target="_blank">📅 20:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27107">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9TPiHzHO1OPowcPhmDsAK9HNx3YiKSzIY8VYOENkeEh7fh9tDRgn9WzhVp8DdiV8b2LViBN8bxAgeJAbuuDveRLrKNFWIteusUJZsUySC02n0Vnq1thJfL-B-rpZ7CufaYWVmv1YogtRUTbG8Mcj0CXQwMeOmddTR4oDyTH9YIivO6owxsTct4rO4diyzhEx59V9S4fwS5JrhiPN1aCDkU069FqQzxumd8PAIPT-ZEegDALg8cgPRe1n-1_UZVfVrVow3r-NFOxdBe_PDc5LVCtnqqEZ8H2TCdZS5Yn6Nrzh6x3b7uLOt0CixdGBiZNnLKen_wj3ngcVWu4Md0UtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27107" target="_blank">📅 19:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27106">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6169d08e.mp4?token=dse-nkSpH9Sbo2hGtEPDxcvunf1cq8XWkyq4kfu6YOMZmnMHuWp3T-J0ImunMUkSfFi-aBrfFBQ4F_3QIceAMZIG1IzTkw84C3vPMzmSe47gi62Emt7mCo_-IhjhaUoRM2lt09u9JCPaB5rGpyvQichq1a_gxReub4_72N9jnld9a-FmX0m0H3xz4tANBe9fBXfykpR846kvimk08f1NSxS_rm53lGU-I6CackdZGJYdwn-WJBBj1viJqMkiBXFNA93m9EgDrs3Zi8rEO3TiqKyXXNVOfZ_TQAXKyi67yCJCuuSbqY4ghEYFs_1KargK2BZEM41UIbMW_T_mN6744A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6169d08e.mp4?token=dse-nkSpH9Sbo2hGtEPDxcvunf1cq8XWkyq4kfu6YOMZmnMHuWp3T-J0ImunMUkSfFi-aBrfFBQ4F_3QIceAMZIG1IzTkw84C3vPMzmSe47gi62Emt7mCo_-IhjhaUoRM2lt09u9JCPaB5rGpyvQichq1a_gxReub4_72N9jnld9a-FmX0m0H3xz4tANBe9fBXfykpR846kvimk08f1NSxS_rm53lGU-I6CackdZGJYdwn-WJBBj1viJqMkiBXFNA93m9EgDrs3Zi8rEO3TiqKyXXNVOfZ_TQAXKyi67yCJCuuSbqY4ghEYFs_1KargK2BZEM41UIbMW_T_mN6744A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی عجیب احسان علیخانی که چند سال بعد به واقعیت‌تبدیل‌شد! حدود ۱۰ سال پیش، زمانی‌ که عادل‌فردوسی‌پور و محمدحسین‌میثاقی هنوز در کناریکدیگر در برنامه«نود»فعالیت میکردند، احسان علیخانی با لحنی شوخی گفت: «میثاقی رو آوردن که‌بشوننش جای فردوسی‌پور!»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/27106" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27105">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJw-8Vn7cGFxa8WkQXC4eVHSFQL7RVlFNTi9gSn-ft345-PIxJCEsq-3DhKn9jYwvJU1uHpX_CwZBYkML_rOHRD_LLWlNedsvS5PQQf1-XmDQqWR8GtGOm4K_RvrDPoPeUGH2Dy8DRkxhs7ULQ3ccXr9Q2moJ1eUBweWEC7a4JOrUxOGc0mCkebMvKM_P2VXJFRkQnTiwzJpajy65M7jJJeZ7uDETuu3LPkvJt-fUgYT1hq9nRCVDmPbHoO3Vf-IFVijoDCXcA1T1-NyxJarvptADZO3hsPmiPjbhgTfZqgqFxM-GCJNK44EeWDaLirGOx3TL7Kj17JF3CsmEPXZjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
سانتی‌آئونا: محمد صلاح ستاره‌مصری سابق تیم لیورپول برای‌عقدقراردادی یک‌ساله به ارزش 12 میلیون‌یورو بامدیران تیم بشیکتاش به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27105" target="_blank">📅 19:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27104">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=r3Rhd6BVJ22ymEIQEuUzI4Dm1AObJRXCTyc7f0ZQxmQJyLTtgX929FvAa-k_Qy0zO_4Vn0ZGRCzf8AWx5H1FKN5oMZ3o5VineiMongZ-jIJaxD3blxct3qH9fzHnLv_i6dajyRxIRFzY7uOjF4HTC8pdhp3w8DmugrPJwX40FeUgrnIzNArOZBDo2AJA965k7wmuH9UMj7fgSDia5szWzVMZy8-FfZ0UpR0sh5MfkQ7JNXEZFLYgBm4oy556CrTGBN6OMH-89jU_00PwyBk6RujX1i7YCvuUqXmOc4639drmWYeFQT82inqZKdwDm85GjNOajZj73Bj7tkYaXEOB6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=r3Rhd6BVJ22ymEIQEuUzI4Dm1AObJRXCTyc7f0ZQxmQJyLTtgX929FvAa-k_Qy0zO_4Vn0ZGRCzf8AWx5H1FKN5oMZ3o5VineiMongZ-jIJaxD3blxct3qH9fzHnLv_i6dajyRxIRFzY7uOjF4HTC8pdhp3w8DmugrPJwX40FeUgrnIzNArOZBDo2AJA965k7wmuH9UMj7fgSDia5szWzVMZy8-FfZ0UpR0sh5MfkQ7JNXEZFLYgBm4oy556CrTGBN6OMH-89jU_00PwyBk6RujX1i7YCvuUqXmOc4639drmWYeFQT82inqZKdwDm85GjNOajZj73Bj7tkYaXEOB6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترِکپی برابر اصل نیمار جونیور!
ماوی، دختر سه‌ساله نیمار باشیطنت‌های بامزه‌اش وسط مصاحبه اجازه نداد پدرش‌راحت‌صحبت کند؛ همچنین حرکات شیرین و بازیگوشی‌های او دیشب بازتاب های زیادی در فضای مجازی داشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/27104" target="_blank">📅 17:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27103">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835360d02b.mp4?token=W6_1UsH377qQN7LFDgfYz2rl3_rxxw8GfXEtb68SX46NtdumO4UPbpM__Pzhoy8W8BZr5DLrRN_irLDNSyM4RZe0AgEIEl4M16zbqGMTGslLZ1jyNdviBmq5pOtLazK2ceAyIKURJ2iCgdwGoSarkxvsV-buoHwycLgjvp43MpFwgvGK-Rwx-jGhp6OZXKuCtYpCwgNslxCBEglIvdg6FR0l7Yj-zshFMex_RuAoUJdwdIb2lzXlzQGK622oWvCX7XAgB85e9GE2kzQa2OaA9NQAWns3FZ6blCBVONbgu1l_61BOMXRoHOSI3YFHU5j8zn5yxDUTm0pWChVxdztOXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835360d02b.mp4?token=W6_1UsH377qQN7LFDgfYz2rl3_rxxw8GfXEtb68SX46NtdumO4UPbpM__Pzhoy8W8BZr5DLrRN_irLDNSyM4RZe0AgEIEl4M16zbqGMTGslLZ1jyNdviBmq5pOtLazK2ceAyIKURJ2iCgdwGoSarkxvsV-buoHwycLgjvp43MpFwgvGK-Rwx-jGhp6OZXKuCtYpCwgNslxCBEglIvdg6FR0l7Yj-zshFMex_RuAoUJdwdIb2lzXlzQGK622oWvCX7XAgB85e9GE2kzQa2OaA9NQAWns3FZ6blCBVONbgu1l_61BOMXRoHOSI3YFHU5j8zn5yxDUTm0pWChVxdztOXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنظرم‌جذابتر از گزارشگران ماگزارش کرد در حد همین چندثانیه؛ گزارش فوق‌العاده گزارشگر زن لیگ MLS روی‌اولین‌گل‌لواندوفسکی برای شیکاگو فایر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/27103" target="_blank">📅 16:47 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

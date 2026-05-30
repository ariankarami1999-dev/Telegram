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
<img src="https://cdn4.telesco.pe/file/h-gvLBS3_WEOir7T1VuDkCGEwFaLuWplxFamZpQnQkgUs3Y228_R8MX40yoMwgHyDhewFVjaHssF5gJKvYBuyLft2g0HGO3oqRB_s8QY1cR7d6V0XCWC7Qzj6mCSI8KnlK4L4k-bp_LdOgjThIQtyZl1nG9HtCLekHpTAt-BM3Ai3YpWw77XK3Of3jTOj-wF_gQ-0uVHzTUnfrtnyHc7NrCRw4tqaQRIXeQHOJVdskspMHehlho6OH5PgfwWltzwv3RLXqc7T6Fmb9T6-s_cxs16P_60lrYZOlZgi2md6SulGr_C3Dp1J05vzSs50l3WxSIJlKNlEodCUAT5lN6QsQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 180K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 16:36:06</div>
<hr>

<div class="tg-post" id="msg-22476">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyVZ3brrj52Fkr6XAXJ2QPB5J6jZh6vtgWN_ctMidwtt_z6FdIbe9cEsXzVDhJ8oM5YydOhNJPO5BHYV0k9mODZEyGK-Mfs66tmGH8RtFKLyEDFXL8PlvoXDqQpH-UTBoKBxzjS4h_S4Pg_Y59s0M18TlnoRLTRfgoyVdOyyNxIb7hpigVS347jLOjaB4Xgjqw5A7-sC6fYeTnWCLh45gUgKB7ih4pxPgrmk4TmUcSe5T2uURzyQMGWdc_XbiRG2Qc1yK9CxQCwIMo3XrPKEC9CJ3u9CZ5Pl9ka8wuwu57Crn3cSIpOFTmwvQdvn0ZU1ckkJtQHDhcn2uqrjwJiq5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/persiana_Soccer/22476" target="_blank">📅 16:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22475">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d18fefc27.mp4?token=hidJ0j3SckPYEEv0_QvQb3xw9FgefpRHWKsPBxIJadSzOpxzVbd9Abrh1k94xh7UswOUWg9VQ_gBhhw4NEbzPUN7QK-CbDS5pdJ95Sh9iO08gnVzRlPjRh3Fgx8av9Q56DR12aNwT9Mnd5AOQzKgvff_tRT5BGoHzPzqpjI8kl5GGOLa9tf46qiysZ9laley3U1FFI1fUh8JN1cz9BOUnOQK0JKAC7btYqLqfRnuM1Gd4U2k1zJAX6V7y4iJX3WSXupFeuga6WeHYwfPtZ0SKe7vqKS2_Ybl-tLzV-kYWNtTUxte8lu8khXBpUGGvNBJLgJk_-Y-9LKHUcGajtCkuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d18fefc27.mp4?token=hidJ0j3SckPYEEv0_QvQb3xw9FgefpRHWKsPBxIJadSzOpxzVbd9Abrh1k94xh7UswOUWg9VQ_gBhhw4NEbzPUN7QK-CbDS5pdJ95Sh9iO08gnVzRlPjRh3Fgx8av9Q56DR12aNwT9Mnd5AOQzKgvff_tRT5BGoHzPzqpjI8kl5GGOLa9tf46qiysZ9laley3U1FFI1fUh8JN1cz9BOUnOQK0JKAC7btYqLqfRnuM1Gd4U2k1zJAX6V7y4iJX3WSXupFeuga6WeHYwfPtZ0SKe7vqKS2_Ybl-tLzV-kYWNtTUxte8lu8khXBpUGGvNBJLgJk_-Y-9LKHUcGajtCkuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مورینیو در اولین بازیش روی نیمکت رئال مادرید وقتی دفاع کردن ترنت الکساندر آرنولد رو میبینه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/persiana_Soccer/22475" target="_blank">📅 16:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22474">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4TMCG43B5R0YD_9dHWkWZg1KO5v8O4OZlqIELYgUSiL9fawZh8snx23KcmRjguEb66mBvECB4TS_Nd3uOaWzaxNj4TJ2KRp5sWopEikcwOLHI-AlZ_8R8q6ZCCm1rWpQWpwqohggVCMuKhk19lH1TIOF6oNOkd4yN8jO-QgEf5RLhPPS00QTVqtbOtG4SdIQuCX2oKrzaJ98DoeDiE47Sd2yV-V82p8O1oY7lRWL0BkZbVLV7LVsd3OIsaw1c3ngnZUSRMYa9_E2AfrgCQX9w7T5YJ2K9vYUJhtt4n8W-pVeT7p-CvbtWwOI_Fqzff2IXr-6Fd1X0Dg_Kdqsa-6eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|ژابی‌آلونسو سرمربی جدید تیم‌چلسی خواستارجذب آردا گولر شده است هرچند رئال‌مادرید این بازیکن راغیرقابل فروش اعلام کرده مگر اینکه رقمی بسیار نجومی پرداخت شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/persiana_Soccer/22474" target="_blank">📅 16:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22473">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvzQxe5BEwUDwSZuhgjqCwKNl8DpMKj6N4Er33mgQqOCBSc3KpjCzdR87KsOlmPVn3_UjSudZ9LDtYoPr0_ljj-06NRQczYvVV_-5Svpjn2Tk5WUlknhW4jdsw13UcUTEQP8Ms8RhpEDNiExKT1nBu9RmGowZqrIr6COhsCNQG2cwTR3et_SUN1WANJ0ZyQLTpiXuXjtf2H9xwP1k8PeYJ5ECjmj--GR-KkTU1WYjGssYhiXJd_0w_gnI6ZLZyCyt4-vd_O-XvFzpiz6gSEND9KMxs8qsz2oljVKXRZ00st6QhZOXsJvXz2lAsV2RWgzvyE8htkkpqQa1vQ2E9Xa2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکردفوق‌العاده‌داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان‌اروپا؛ رایا درصورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22473" target="_blank">📅 15:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22472">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFcS1uqV6sUBTRBBdl6_OPZrayAS7JtEVfFmZ__mjImhRRWCodZcm4YyyAZIlwvfD7qKRG2PTO8Qv-9QXP-oeqlSPJn1w15W_nQdgygCJVXmywc9Awb8OAs0-n0T1LL9nvq8__PrDvjUvwims7SHJZSLMEaOqUx0Al8HICR9GYH2UtO8mZjm3uYTnbbQlNDLnujdYyw272bvh8f2mrvjaNdwSbBFUvBy2SxBRFSKDmLwo10KYm1x0fmjDUTI02NGpd9g6dmmyois__hO48O-oHSralqaP9-4SvZ0cemIiIOHppREPrtsiyg_6gAkJd5UWZxlw6eBimFLqu9afe7n5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه بعدی اتلتیکو: هیر وی گو؛ برای پیشنهاد دوم به مشکل برخوردیم، بلیط کنسرت فردا تمام شده، بنابراین پیشنهاد قبلی را با ۶ بلیط برای کنسرت یکشنبه بهبود می‌دهیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22472" target="_blank">📅 15:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22471">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzJ4bmUsr8PB5yC5tJZGh8bYErnfsm9uKKORBwlejmLkUxt2-MKrDso87AT3sD3igkG7ocWGV1QJov7lG7ave2K2J5MOjSDNOwV4nAbxjsaMJCgmkcACiHbCcyI741-7KhQJgMZxrWWkyvkexN3bBbtnPAXeIuO9cjmXe8kpRJEVvlyFLcFhOvQ_wisTGN5tTzWsJS2_7CwMH-bs6xnXvn5cimYmRMbgrHgprGfl-PvZSlLJsnFv-USCFxQv6-IHkjNsJyXyzugytiqlM8735YTbQj2zUUYEMg1BS6THy2Qvf68UxKq0MjNp-T4ei1IgG8VpBj1lx3t47kD_YRph4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سیدمهدی رحمتی سرمربی خیبر خرم آباد بعد از اختلاف با مالک این باشگاه از هدایت این تیم استعفا داد و به احتمال فراوان فراز کمالوند یکی از بهترین مربیان ایرانی‌هدایت‌خیبر رو برعهده خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22471" target="_blank">📅 15:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22470">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRhdZaqYvOwCFAwiFePERFG5ZyEm4hv95xS_rTkgxRVR4JC2yxjOsVTwKGsKnUURlcPw7dbKX7CU2aIMGRl3wTZ1R4-Xd4HjHhVk0eQIXFEyHN-KU_xbtd0fv7yvZ-7rjs6B8eoEEhSIe915VjHSsPBa3cmbLzvvRUkz9DqNU6Oscf6mWcTUD_S6i4AfkwoKd7YTT6ZJg1TkF_uHKyOTDuGJvhNgkynJz9cuIYa4Qsvi5sazNyw86I-o4MsUCdnHKTRJzfq_4DXvkL1bop4I-KKRfmfEtG5VXvKnZOruLV4fIWPl3M4UZEfCrWQL5Rt7f7hE8ESfR4dbkFX8TDtl4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/22470" target="_blank">📅 14:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22469">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkK9XxkCrgd2eEsWxN8RqeM_Dv7T2omqsZCMmOOhsYuDGSSswbJjmBYukPgxTqnnmstLSqDhBydLm9xkGdesIdAyDaSgRkg34sLoLrHlDfHBx0LwMsYN7OkUd8EQ8cYNDuTgjO5UxCvtU8eUxhfy7EFWGVlgi2xxCLp3mhkcsgEcWGr4cKRv1V_mdxOjT6-_rEx8lPPiprOwKz9qB7VIwXWEfB2pHT-YKhgdIaTRzqGBJRBJshaKbP6_DsEE9fsWerdzJ4MivsMkuA1Cj3snzl5PLIAFGo8UB7ylSvpGXRN5cbf0-jeaEQkMdGOnxOaJROgrb7Nf8e1uEb-zuPDWaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
#فکت
؛ کریم‌ بنزما یکی از بهترین مهاجمان یک دهه‌اخیر درکل دوران فوتبالی‌اش تنها یک دوره درجام‌ جهانی برای فرانسوی‌ها حضور داشته است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/22469" target="_blank">📅 14:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22468">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDR0526y7zAjg7woTf5dIRqxl8XR_Cs1gwZGRr4Lq4vdXngZEKMRorb8GLO4zSTQPN9aknrexuj953XqINOvUVWHwW9hWbGA9481s7zRfm3NRlg_EgI-9LbybnwabpLqVORBBc-O8n05mPtEdZ3R09qpJGSFVJ4dEhwEyBjnCzzjhfSwAqCr-hBBhlDr8pO3VLGEQnuWnb9Fvb9laATb9ukVh9XsWEEfVgDccWQd18t1d5sjteyU7gJ-VBOKy_9kPdBi2NRsWkXJuuMOt0MbfYFygQOxtTPa2FpKpPIOPv7gxZFmmWmOOehk84OYv32cJekFVhSO3KUKuFmUYbhAHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇪🇸
پیش‌بینی ژاوی سرمربی‌سابق بارسا از نتیجه فینال امشب: PSG بانتیجه 3 بر 1 آرسنال رو میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/22468" target="_blank">📅 14:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22467">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRMV7MWI8Bi8WAxgqJm59O4bVTzxUAB7Q6AUXuzDgXGGV4qNAXgsXNFV9a_Xq1u18GSCCPnmWnKbSZipH93toWk9o4U-42k-LSoB9PtmwvSvI90mFstH-zdIy9Cc_y6emZsUmbh3Xyt_xuoYjMK0Ddq4l24m5PRRCcdRCfr4X3AVnExPZ2jZZq-qg24M2VaFilC57ZwFUndSHwDdPVSaKmliKIpB6_wKt_rvHanuSo4wbrYBuw_o0GnImgUSUaM9mjTepMUKFz7xZgYWzpQwpIhQ6TluZxTYEs11i7fPZ9VyW59_rYysZABV46Zl0t6BWcelJ16UreRWJGxuo5LROw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باتوجه‌به‌‌مصدومیت‌های‌پیاپی در فصل قبل؛
احتمال‌اینکه امید عالیشاه درلیست مازاد اوسمار ویرا قرار بگیره و ازجمع سرخپوشان جداشه خیلی زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/22467" target="_blank">📅 14:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22466">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAGOMxsnODGEJDxfIyeVVFI2bpNPQlSBkaygnzKdfbvFkanuLFf8xkaPe59VqBbd8_FX9-KWKcgs8nl-tZnYQpcRbIBOzcqDQ8R56znsVzlARlaa2l_02Yci20A0DSjfah5EYL5CCbo5Mkwpkff9GPViat42atvAgIZm_7ZGfZ4T8l55GDU1ZRhOpsf3HPVn8DlmKIsfLPbmkvU7eX5VhAKmUiBnJExsUfiYO2OGPoFsHUdrzNzznQbk3Y8WKGPxKHXlgs0qQQFelLi6LX4b3TuZmHRwa2JamkuxE_n4Am0R7kUnhdo3GqYm2-Xi0c_gL8WilA2QJ0SO_jrmeskJqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
ژول‌کونده مدافع میانی تیم بارسا با پلی استیشن یکش رفته اردوی تیم ملی فرانسه برای جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/persiana_Soccer/22466" target="_blank">📅 14:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22465">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gq5LRxrL-oqcgsfvOPA_cG_DeXguvlBGgoywzVcQELdKYRh6q-r9LdRpGtQ9_2bPOGqHMgK5bPR2s8NYIX3EP6dnUAU4QUXOxOFy0pc8MdcNtLsurqV-QOsjvfa-kruGZvYSAytYdSKI2YfjSYI6uMdNamPdiPxEhJsGmF-EOP3qCpICHKQWZ6lEb3HFwkuwJYqHbFQB2Sgqdi2U0rkJ1UHw0nFGAN_SWCCJgpfwBuXeYUIwTl2RMVNnh5AmUyEpqPUz-Lz4MSqRy1St8eMwwm35bzpSAWIY-G-fzP1n0sqE-Ygocebuzmlnf84oivCIU6-dHQQdRNtRCCl4Hmv1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ علی رغم تلاش علی تاجرنیا برای گرفتن مجوز رسمی فعالیت فرهاد مجیدی در لیگ برتر؛ اسطوره باشگاه استقلال به مدیریت این تیم‌اعلام‌کرده علاقه ای به بازگشت به ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/22465" target="_blank">📅 13:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22464">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjYwUAdXiXV5p1lyfXx5y0YU0DvjW4tWXfj84tT4QehDw97ymgAkWE764scUUITdnfP5MnFhMoZSiWVEw21yuBxdOeSTRTrYgnZjNtPmpP6YzcHPoBG2EOYoYUk70njPIknXR3ijWrjWKo5WvVz3DyAgcdci17PxlenyAGnwMN062-eT6qcfw9OTbi-0y0JmP1NR2WVll85nRe89m94AhJ5OkIKT5F8aktpQ1e2S7AwVwM3K8wTjJStXlEwk_lZXAkZAuYl5PHRNUx_v6B6twTTAF_avbrmbeivIXvrS4anXg0XI-ORjTYJuD5YNJUTm8ulQM8lxq1nZRatr8LXPag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ استن کرونکه مالک آرسنال در صورت قهرمانی این تیم تو چمپیونز لیگ قول داده به هر بازیکن آرسنال یه رولز-رویس فانتوم هدیه بده.
💰
این‌جایزه بین 530 تا 580 هزار دلار ارزش داره.
💵
ناصر خلافم قول داده درصورت قهرمانی پاریس به هر بازیکن این تیم یک میلیون پوند…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/22464" target="_blank">📅 13:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22463">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdhZe88b6eiFbQOF0CG9lYjchIGziQVCsqERUK9xArP2_banclm2NwSIWbPcM-_L1l9js38tITbcfyYSTwMPI-wYm6BhPLPRkCbVbTGKXtIj-dKBi3X-X3ScFbdRxTii_twwACRt7KKPp_IFjVP5m5AM005D4q2ORZCI0Af_o4GAOOndHVa8ur6jDWBNkx3_BJzshbKnMqCSSBOBIeHnvTipoRg_qTQvfj8deh6ho5U5LfyuoNoI-vSo3IwzIJ41qr5mkhk_ttDECEHl8MxSEbMR6PY_-pCDp2RQy6V_H73ZxskEISUICLpEk6C0ckymWZ-tKzEs5YA0ZDcH7Hn9zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ علی علیپور مهاجم 30 ساله پرسپولیس بزودی با حضور در ساختمان این باشگاه قرار داد خود را به مدت دو فصل تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/22463" target="_blank">📅 13:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22462">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpIgsBnyA0erTLs_DegSucNbtGUNsC89TFAICn7oaAwq0AlmtvSHepjg4fcKPL4xMi0lX7DWYZOVw7i3B7ZO0leMAk6RHGc-jX7CBna-kJhJ0syOZVrTUseDZqoM-lTDqzMT1BzKBnRBm8IoEEyvRk3bmXo3w2ed5x2R20Fgpz4XGFGyInt8xZOSL8-UiA1MpnOhS361Ymn7X8JLvioVhKbmkqmLxwDEOe4Rx3IhVhL2p7673lcXYYdozeo-c8Nte6FEzsIMlVmoqHozUJnjf0I_zexZ_Fb27dBHIflwxL8q4M4EWGT889ZRpP15HTAlBm6CcvUkYg9eHZnw7pix1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/22462" target="_blank">📅 12:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22461">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTK39JZnPlACyBJ0j-7UDNygvhd9a185IN_jSdJOt-PqtoiDN4NiSiQqi9JS37gru55Igq5QITa-pyxUwXblVyHSVvCQaluwFlcl6PO0ybdQeP8dLhFkLIJ4Y_2vsKtpCLMkTN3JouNAS-0pwvF7tXyzm26GP6z_qxqOsLHFTQXahz4gvbVfy_wNJZVRtPh1qC0EE6bHq3_56Lud-gP09NG48_UodIunVwyewo46eAGuxP2cY9fzUk1v_UriBbGqJc4IMgX0ME92eYuHyTPyqUNLuPRbw7jfyE2xckFZHFkhqrQjbEhTZgUI1qQxDQzfKfBZMkuFBj0phszIL2JE0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رسانه‌‌های‌اماراتی: علی‌رغم علاقه شدید فرهادمجیدی‌به‌استقلال و هواداران این باشگاه اما اسطوره آبی‌ها به دلیل حکومت جمهوری اسلامی قید بازگشت‌به‌تیم‌رو زد. مجیدی زمانی به این تیم باز خواهدگشت که دیگراین‌حکومت وجود نداشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/22461" target="_blank">📅 12:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22460">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OocCeQCDrfVxd2KUE_fyBh9QsZpTKwfKBFfHM4olN39H0VUsf6PPGrtiCcWg50PF5aCOWBNW4508luMd7l5wBOwYb5g_98do4k3fw8x9fkbdluhDDVIX_OZd66HkG7rogMYXLqw5IZ2mzSK31hCoGHRLiS6OkrCt0W3v8pmW5SwoUzaBoaq-1QbLe1dPrmp12dpTmyl3dtuIlFt6iuljxyq7RZ3rHFtSS94N9PRH3QO6KyBOlRFKebj23XJzOQGZ4sNrgEpCV9c2UaxWL7x386mWzR23mSp1Hbj6gOV2ybjKTK9moc_B0mBt9zftFtZuIePL5todQT3SyBbgrZ3j3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب کهکشانی و پرستاره بارسلونا هانسی فلیک در فصل‌اینده رقابت‌ها برای‌فتح UCL؛ به این ترکیب به احتمال فراوان برناردو سیلوا و کوکوریا مدافع چپ اسپانیایی باشگاه چلسی رو نیز اضافه کنید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/22460" target="_blank">📅 12:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22459">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5359012d10.mp4?token=korwIgW9R8_WX1G8PbnkJ45wWiPSgGR90w5Xa6NI1dAMDLyF0lbmkioHrJs-FTQimiYlAbQV7yMpOnEwKLOg-uu20Oe_zjzZOGF_SwqF2RTJDPqjwzaiflsn_kSXQxDgS8jt60sRB6PoPsYMbVPfMuuRd8rvb6-f3mSn1vlyFbGJ4Xz3-Goa8uEHXW6A0ARVCc7HgSAO2Pr6FA36YybWI7DBw-IoDyo8dluawKYkqEJlfOvj2Z0DDY3MSOTlyodIt62T5G0fu_BJh_XQERiI_WdR1ZjRYlOUarZsMMlwzieNam8jjGeUEAJKIi86WAP9i3AZAPWQbCx2fpakjH_oVX32girNudR4193u3jmP3YEJ4yfmkKG1ilixh-dxv4vTJyD-FtJUUQdCDZxYsaGiYSUQCOJ1ebkPz8OWKKDZtWCw_SfrXt6JVLiT7mfD5BGp4d7qupUsmWKfA3c_69M-2byvp5wP0wWwWSy-ElwcPEzIbRsLmZoIaiSxVXtgPA-voCIh0n3lRXcHamDYAPwmh3p8R6EmXLV7slyWlH3Tn5tpoGZBu_0MAfNVGAAsOLeLOqxDzbjvEPqzhGSMwAMuvOXqOFmGEr8Z-ViDHF3t2o6RJgX_XZTtCqGSqE0_66nVvcNGL6at37WK3fnq6uXGvko_yFBsuzKiV_1kIu1n-5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5359012d10.mp4?token=korwIgW9R8_WX1G8PbnkJ45wWiPSgGR90w5Xa6NI1dAMDLyF0lbmkioHrJs-FTQimiYlAbQV7yMpOnEwKLOg-uu20Oe_zjzZOGF_SwqF2RTJDPqjwzaiflsn_kSXQxDgS8jt60sRB6PoPsYMbVPfMuuRd8rvb6-f3mSn1vlyFbGJ4Xz3-Goa8uEHXW6A0ARVCc7HgSAO2Pr6FA36YybWI7DBw-IoDyo8dluawKYkqEJlfOvj2Z0DDY3MSOTlyodIt62T5G0fu_BJh_XQERiI_WdR1ZjRYlOUarZsMMlwzieNam8jjGeUEAJKIi86WAP9i3AZAPWQbCx2fpakjH_oVX32girNudR4193u3jmP3YEJ4yfmkKG1ilixh-dxv4vTJyD-FtJUUQdCDZxYsaGiYSUQCOJ1ebkPz8OWKKDZtWCw_SfrXt6JVLiT7mfD5BGp4d7qupUsmWKfA3c_69M-2byvp5wP0wWwWSy-ElwcPEzIbRsLmZoIaiSxVXtgPA-voCIh0n3lRXcHamDYAPwmh3p8R6EmXLV7slyWlH3Tn5tpoGZBu_0MAfNVGAAsOLeLOqxDzbjvEPqzhGSMwAMuvOXqOFmGEr8Z-ViDHF3t2o6RJgX_XZTtCqGSqE0_66nVvcNGL6at37WK3fnq6uXGvko_yFBsuzKiV_1kIu1n-5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پنج‌ موزیک رسمی‌جام‌جهانی دوره‌‌های اخیر؛ تنها دوازده روز تا شروع داغ رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/22459" target="_blank">📅 11:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22458">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfU_9t8iP74dFWmAKbEwklE4rKvCHf_7JyAZwhOj4QaPcCSHpSpxggwsWWPyyHWN-FXn4fHCsyfJ30lw8-lavjzEusvaFJv9_7ZCWTuAx_lcnkDBKJnmtsAuXNkREL9Gxd8WZtNQ7Y1gon_Ymyse0rVM_SDoSHieTACbmFUC8ZiHIiT-PfWqWkap62ppT08euwhIZwss9K_OO9F0pCnf79GMtU3pgrpGJuXVgJNbgSJSWPjFzZEq0BwZI840zHp6u4CC5-uz1bLvNi1KTUyqM9yjZqpLPr4l8fgp1iqRjqNIf5yD0OBJ-MWHZ4benqZmODHCKTQvJCs6jbfFRd11FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
مدیر برنامه‌های نیکو پاز: ما با باشگاه رئال مادرید بر سر تمام بندها به توافق کامل رسیده‌ایم و نیکو درپایان فصل‌جاری به این تیم بازخواهد گشت. منچسترسیتی، چلسی، اینترمیلان به دنبال جذب او بودند اما نیکو علاقه داشت به رئال مادرید برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/22458" target="_blank">📅 10:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22457">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/au0spLpXee-AaAOi2PCdRzFsbrsxpHY4eaD9J1TMowI2fOeIlmonM4br-Xzjk2Vto7xAbWfRbO4jTGSJjt8VUxWu3Gd-5POYDyQgK9yiESAYF-qVRs_Cm0q7RrH3r1jNwE00Ulop0sM7-Vk7_SLwyDG7EZkOMpgqJCwZbdmt2OQuVubetaYSAc1MtNV0jl215kxS95RO6LnIvcgUPVDR35Yp853LC0EqQm91SpFaNp41RZ_Tdn3rzeyVsYs2o6RhhrSkR8MNjt470BOD8C0MIQAm3YQ4Om8UiqkVRkpMjcWxEvtnsVn5vk1q5wBiF8IccoKlpTW9XHYENfIZWXCpPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
به‌مناسبت فینال امشب و حساس، مروری بر فهرست پرافتخارترین سرمربیان تاریخ لیگ‌قهرمانان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/22457" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22456">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mq6uqzFim3ws79eY1kPfmE2E0PGBhBQXAEZMlFzCdq43PNnuTOqYniV5G9UR4BWKBrOy3NHcokWtPQ9fWGECxhw_ZGkynpkNU0hI8WF_-KpFukvkHhRwJ-ta6j4UjlNJqx-pZLFYilkiR7omOdEe5Uo7FFd_f2iWioPb76fNh6ZKDXsNKyT4-rneUDtylYLY6tMIM15bqg84ykk-48itMxOCo5g8lqYNh7GK56WxwOsJEDwQHlIBbJvOhF7em7Lod1LiTMK6e4dr1vpQNYbUW6VrM9zfitEc5zvFkWOl5F5_S3gbuq8Oq0JrsCtwD4IttkeMg0CnB04dTnruuJJQKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لوئیز انریکه‌سرمربی‌تیم PSG: میکل آرتتا گفته قطعا آرسنال قهرمان چمپیونزلیگ میشه؟ اینا همش حرفای هیجانیه امشب‌میبینیم کی قهرمان میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/22456" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22455">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2yAwI6HyB4Zw8VI-wfVauz3_fqFVh73hFFYCYcLXd07xNMUqWMkc2SaK4IcL37j2nC2hZBJmofT1_Grr18n0P-vL-nXOuQvM-xunN5UUqkGQvD8JqsMJwFwM-wrQDHuagEjfVsAx-RSgyi_YZoCbK1yky_o238wRtsvtjzdOGEFvMAslKFPrXLcljSpGYoP5P_vmwJvcA2LwXwbnhbip37CdStBGGC9Rs7a_shcwRrwRNRXLGr2A1KVOMbVrLr9AxAZIGq7REQT4u0p_dvLwbeA7V-9W_WDWo5LCfpybsoUfZ3CnQNyG-97EY9gIrqT6j4Y59zhECncVnui-dsG4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👇
فینال لیگ قهرمانان رو
#رایگان
پیش بینی کن!
🎯
با ثبت نام در این لحظه
#وینرو
بهت
🅰️
🅰️
🅰️
هزار تومان جایزه بی قیدوشرط میده
⚠️
🤔
میتونی رایگان شرط ببندی
👍
تنها کاری که باید بکنی اینه : عضو سایت بشی و
🤩
🤩
🤩
هزار تومان جایزه بگیری بدون واریز
💖
تنها سایت مورد اعتماد ما:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r9
📱
@winro_io</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/22455" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22454">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d629612bbf.mp4?token=bpQKSAKV6kCCwJAQt1LGFJksNDOX6GUN70UchkKHL5uSIKfyAXdoJWDvt7ILfIpeAe0X633nRZNk6CbGNWIgm8ciaeSNIYc34h4WqwyY_sDWPh3Vmgi3s__D12wmU1UMXORtT2GpDdZrMnMi7_R-CxQTNPTFqJlN4vaY8F8nvt4Z9pgmD-yxLScVgixS-RMQRisMOmZBB1WtkOeugZGQGNRd4xPzqGfXEwi7iic4t0cDOB3DlfXpAZ4K79h7boFRil5gXsMBWB55Or8eA8BMiX6ck8PeRiYHopiYCxsxUmHKi0RlGhj_ISYbYOV-5eI9Ev7cjhn4FbsCKxh1fALtIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d629612bbf.mp4?token=bpQKSAKV6kCCwJAQt1LGFJksNDOX6GUN70UchkKHL5uSIKfyAXdoJWDvt7ILfIpeAe0X633nRZNk6CbGNWIgm8ciaeSNIYc34h4WqwyY_sDWPh3Vmgi3s__D12wmU1UMXORtT2GpDdZrMnMi7_R-CxQTNPTFqJlN4vaY8F8nvt4Z9pgmD-yxLScVgixS-RMQRisMOmZBB1WtkOeugZGQGNRd4xPzqGfXEwi7iic4t0cDOB3DlfXpAZ4K79h7boFRil5gXsMBWB55Or8eA8BMiX6ck8PeRiYHopiYCxsxUmHKi0RlGhj_ISYbYOV-5eI9Ev7cjhn4FbsCKxh1fALtIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پدری به‌همراه فران تورس و دوست‌دخترش رفتن شهربازی، اونوقت پدری نشسته کنار فران؛ فقط قیافه پدری که متوجه‌شد شب‌قراره تو پارک بخوابه
😂
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/22454" target="_blank">📅 09:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22453">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c867b80a08.mp4?token=dCk5isdks51yFmYoFDuUbDPZH4p-e6DYssPyDadSbDNM46DBeb3vIKxqIhaP-EqwQc5Xgm81af1W3nV2_lP549JlSadO4rQ60g11Yex7uGn48s1YVHSRRA_UqAdPL-gZ2jYVXf-3fc3Y02hoLhMyk1FiURe_sibC-RE6WPbJHG4wX67h_p57sETMLm1cgMF_47TIOEEDHKo3AoX0NmTpP3Wazb9lQk8_bRkc3Bsm_aZarPta30uJJKH6eGrQDCQo6F1k6irNblSvl1qQ_Y6wk8oLjJFC_4pG09W3MQh8slDiB7tl8cnmoGDeAyTXKIm5_MZj1ch0RW-BYHMSj2OEln7dUPTyN9wLCiJO7F-u_3b-6Rety5UdVWGK1sG6QipoZwIWFHdm_xRWx2wN-kJk4G2Q62-3fGMSq3zADzAY6bmVwsa8AQRY-jNEgJKEe99oS1NAMRph5RXHmcqUHn9PWKltN_HERJF4Ffmj6zDq0dWY_TELNOGHzZGtu77aCadKSf_DeYRT41JtHt_I0qerexIiKBEqfck0rSVPUYHZofKoG4r7PCDPP8I8NOSaZGjDBM97u36VopglL6C6kwG6ZXOKZqqpfmU_vqwbJMbZGLwHA_v3_565iklphf_SIbfgLklS5NeUmKD9k4XwMIryntX_lVtGTYTYVmGZzs1Xlq4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c867b80a08.mp4?token=dCk5isdks51yFmYoFDuUbDPZH4p-e6DYssPyDadSbDNM46DBeb3vIKxqIhaP-EqwQc5Xgm81af1W3nV2_lP549JlSadO4rQ60g11Yex7uGn48s1YVHSRRA_UqAdPL-gZ2jYVXf-3fc3Y02hoLhMyk1FiURe_sibC-RE6WPbJHG4wX67h_p57sETMLm1cgMF_47TIOEEDHKo3AoX0NmTpP3Wazb9lQk8_bRkc3Bsm_aZarPta30uJJKH6eGrQDCQo6F1k6irNblSvl1qQ_Y6wk8oLjJFC_4pG09W3MQh8slDiB7tl8cnmoGDeAyTXKIm5_MZj1ch0RW-BYHMSj2OEln7dUPTyN9wLCiJO7F-u_3b-6Rety5UdVWGK1sG6QipoZwIWFHdm_xRWx2wN-kJk4G2Q62-3fGMSq3zADzAY6bmVwsa8AQRY-jNEgJKEe99oS1NAMRph5RXHmcqUHn9PWKltN_HERJF4Ffmj6zDq0dWY_TELNOGHzZGtu77aCadKSf_DeYRT41JtHt_I0qerexIiKBEqfck0rSVPUYHZofKoG4r7PCDPP8I8NOSaZGjDBM97u36VopglL6C6kwG6ZXOKZqqpfmU_vqwbJMbZGLwHA_v3_565iklphf_SIbfgLklS5NeUmKD9k4XwMIryntX_lVtGTYTYVmGZzs1Xlq4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
موشک‌های‌گرانیت‌ژاکا بازیکن ۳۳ ساله سوئیسی سابق باشگاه‌های بایر لورکوزن و توپچی‌های لندن.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22453" target="_blank">📅 09:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22452">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/928b5d2877.mp4?token=X4QtD4EOw1OUUpnhUngjtYz97_G7ZBDlc-nMRa3thVGmlAxuRhcan-D2DTqB2Htg9V2b4Bn3EeNbsDfsCR_HtY-xiH2Ta7Y09xaF2vEM1Ot3DiFGmiQtSaeJdbgSqDji52Oo6riHxQ7UzA17XVScTKcBh2_rU8vEHvk5Xikp4_JmHDmjJ0NF4_JMORPfy5Vi8cB8utRqsi6LnmlFTuOOP_a6peBCfkpJm65C5EbALXbuB5qxNc8A5qujBDDnAXEH6ao5BAb2ee0Sr3YffrSGsIZu0xAakPM8qXRouYlJKZG-GNw30eNwynhK6Kd7dcvlHVrLSErADXlMGmefMheK3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/928b5d2877.mp4?token=X4QtD4EOw1OUUpnhUngjtYz97_G7ZBDlc-nMRa3thVGmlAxuRhcan-D2DTqB2Htg9V2b4Bn3EeNbsDfsCR_HtY-xiH2Ta7Y09xaF2vEM1Ot3DiFGmiQtSaeJdbgSqDji52Oo6riHxQ7UzA17XVScTKcBh2_rU8vEHvk5Xikp4_JmHDmjJ0NF4_JMORPfy5Vi8cB8utRqsi6LnmlFTuOOP_a6peBCfkpJm65C5EbALXbuB5qxNc8A5qujBDDnAXEH6ao5BAb2ee0Sr3YffrSGsIZu0xAakPM8qXRouYlJKZG-GNw30eNwynhK6Kd7dcvlHVrLSErADXlMGmefMheK3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لوئیز انریکه‌سرمربی‌تیم PSG
: میکل آرتتا گفته قطعا آرسنال قهرمان چمپیونزلیگ میشه؟ اینا همش حرفای هیجانیه امشب‌میبینیم کی قهرمان میشه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/22452" target="_blank">📅 09:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22451">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb17964484.mp4?token=GKHkE6u1dnSyOm1rwxaG6Rvb-inqJ0K1v-YdCOMr50JMKJlnDwwUvGQ0lyACPHzH428_lJMUvWacybrzEfBWh2zIE1wHZqeLZlhKraBViagqTeWgCTNHv0VZTuM9GLjaHaNrAAOiMpsijEzSjA6YepXZ3z7HJwIQIBLFW8BSmkpYZr6iyc19T2KtTTNxCn8dTM6XbSXfIjS5eY466-mn3KpHqeLYWI1Gvuhi3c8Rl5_O6IHbZABiLd7RtfdRZdHrnj2GqKLsI45VMvV15yMte49mXX6lqdTF1TEFpRYRUdh9qCIVqwXQ7SthO1_W2PILr3c5mdSJHmDo62RtMYCa_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb17964484.mp4?token=GKHkE6u1dnSyOm1rwxaG6Rvb-inqJ0K1v-YdCOMr50JMKJlnDwwUvGQ0lyACPHzH428_lJMUvWacybrzEfBWh2zIE1wHZqeLZlhKraBViagqTeWgCTNHv0VZTuM9GLjaHaNrAAOiMpsijEzSjA6YepXZ3z7HJwIQIBLFW8BSmkpYZr6iyc19T2KtTTNxCn8dTM6XbSXfIjS5eY466-mn3KpHqeLYWI1Gvuhi3c8Rl5_O6IHbZABiLd7RtfdRZdHrnj2GqKLsI45VMvV15yMte49mXX6lqdTF1TEFpRYRUdh9qCIVqwXQ7SthO1_W2PILr3c5mdSJHmDo62RtMYCa_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
وضعیت خوان لاپورتا مدیرعامل باشگاه بارسلونا در روزهای اخیر بعد از پیدا کردن نفت زیر نیوکمپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/22451" target="_blank">📅 09:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22450">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeP0IiXNth1VGaH_bSd71MlqkQY4lG766PZDtxnZr4aA6s96JWsPDDcadM6R9ZTuiGXwnUswExrQrdejHppmuTXVxBPgQrxQdiwsXW9H7iv5NqHtLDdyDSNKMYcIu03jC0Q3No-GqGXsZqVzbNW5xbW18yZYJWNLFYfUv3uGQVQKGaQQm4jmHnvww2jZWkeyqCnyleBq7krShf61RcnR59bsZ80ukRRnNyaTINblWra47XIJWNsE0_JNHBon2U-vS1nCSCDspkMfQ-DBF74tLUE_qsy_O1w-0OO8PhR-6w1NQzEm6Zmohpox6YwG6Z33ZvLqeCVpk9qTv7z3rjnQDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22450" target="_blank">📅 01:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22448">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkwUTfyxclzSwA1EQhuwfW9K1gLtUx3n0iOntRZbVRn2I4nvut9td74aJPGUyt6JrvslqC8HwuJKfHG_TijPHzVSsYp8wj0X3yYGvJSl0OHGhELLon4te_3hRN57gulKQv50K5YIZheFcKlGxFsF_-ZHvpK6AlPqYjacQYwwwM4IMM9YYDYOGOUbmj4O2L_SQ6WLC9r1_LO0eKVJso-Tjz9WH4B0zxjsHu8jCPFwIeebIAtdhXmvklnnF4I5i9CesAeoR1TL7Rn763wXAZfjZC6vw2kp8R4eh_KU6ER6DshEtfRj090UOLb4jrAY7JVlivF0IP0ohbSCHiuCQS4WQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه تنها بازی مهم امروز؛
پایان فصل باشگاهی 2025/26 با فینال حساس لیگ قهرمانان اروپا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22448" target="_blank">📅 01:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22447">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slsRlnx5akXn2EDuC3GUAG5qjQ7Jlyv0geISS1P3yaSV_nNv5myPcnEkU-h3rfVSjwqoFCX11Mo43EOaaFLg8gMRm_2gkWN_Ofq1iOciojHGqzeicZdOaMT3ANU9gqKyhjhmWsG-i24ZERhis2hFtpXwSRblDky5XcLy8of1ba3xAVFcQviKu5sqaIC_BeQCQzbmEIJNkBgkXbSZhfyOinGB6PO7M4jVXIfCuPhmU3bHR59SxXiNmtYMlGGg32Ds_G_I7YnmkopzqsKTnzelrqaz1eLxfiBVE-pLnynPLsDtwWkNS_iQ_wSaA2LTGoQEE1hNQLPAnzY4obvd2i6ycA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل دیدارهای دیروز؛
برد تیم‌های آسیایی در فاصله کمتر از دو هفته مانده به جام جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22447" target="_blank">📅 01:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22446">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3s9Cgh0ZPmZzSVbSmi62KjJ0r2vHDHU3AFi7b2eo53ewWdUkO6vMGykDqT_Sjzs8EPddJ6k1Im_3tOtDdu9uPYJ5AxVqc5dPkQZrNDHogi20fLTtDyf-1E4MPeWCkpb_K4eLEcrYv4ZawBAZdfSuWL1vTd3AVE6seX2A-nal25UgvyD1HYzed7KH-wvUHy6ae72X_nPyGPWC4UACFTm6709FMtwIlXpUqS30b-Hbp548dxo0d_i7ct78mBEXCzOwegEXUSfnRFeB_CgdSQZZ1iIQXVnpQa6cGd5h3dinL87wrWzWhzCWYcOv0wduIaSWaznwXm_YU1gpXv1l8QwhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فواید پیاده روی رو ببینید؛
گشاد بازی رو کنار بزارید؛ فقط یه‌ساعت پیاده روی عادی میتونه بیشتر ازاون چیزیکه فکرش رو میکنی بدنت رو تغییر بده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22446" target="_blank">📅 01:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22445">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKnLteNg5L9iuYm67FiZpzyIOsbORAnO_-AC_8U6G-GEjC7BunmralIlXbplYs6uPfSpoMlnX-kHqTGXBOq24srDLqoqgtPSxEopMyI_-3QpFMULe50-Hzuo-TjMquBWVutOqILtIHHxuo8VZul3enaCrA2ZM7gIjtHQaDmSh3BWv25OKMPwOPjuUZNoMvI7snvYxT1uXXu0fiy3-v7pLWn2Xh0XtPsBFZmd3dXfFx8VAKIlMJWdObkdeviS7o8of6iaprI0nzs3GEtO28wrsUYJEGp6_ngeKGu5xJV_CFW9tcul37zeeqLTAGwUkZd3BPD4xniWlk_GqYtWoy1r3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بازی‌فوق‌العاده‌حساس‌وتماشایی فرداشب آرسنال - پاری‌سن ژرمن رو در آپارات اسپرت ببینید. عادل خان هم بازی رو گزارش میکنه. از صداوسیما هم یکی دو دیقه جلو تره. کلا سعی کنید هیچی از این سازمان مزخرف نبینید. لینکشو فرداشب براتون میزارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/22445" target="_blank">📅 01:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22443">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bA2mk9HvN7oyNhScsCeoZj5Sz1SnxZarDAbjvtopEIxlo0zMxSA0HTY8laK1G6EtDrvqbUKpadx_ul8whBxO57D-6EQUfoK-wCfSGLUBFWH0JQ5fOGLZmzoREYYR4jHGecVfghQPX5kGARAFI_YTMqDJNy3ObRLkW1iqapRJNGlsLX6PEfQjvj_ZIQn6HrDMuw9_mRXJuoA6p1ikvSAHVp0jXQDNY-K5W4sgdtR_9vYiCcdW99oId-9jMYU_kuVfqZut7VMl0o_2FzDkwRg0XMzhrvSMYZDlZY0tZAHE62dEP3YCH7Lz2DE_jkyGEvKI-na1sylOYLCsJxSYKtzDIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو: آنتونیو رودیگر مدافع میانی رئال مادرید قرار داد خود را یک‌فصل دیگر با این تیم تمدید کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22443" target="_blank">📅 00:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22441">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IeCC26haCesUo6rx1Zas6nmmw3EdZ-ziy-LKk1bK6oHY3NL00Ha5hF-wJLfkomDcNY1L9qY4Caze_EN9J6TsMd36VjYK7fLAa1VEp7XbpBgXvSO5cE7GiYsbmFCPhoSaGNJ2d0YFLFWBNgd7F1OD04PGDQN_ZfKzSgRgI4U9srOxrk9_hAPtNgAHaN1eC0WrcNvRx4XMFSnTAaBnyZSXad6KHLSBpnm0r4T7ir7j_O1TDy-W22x9BZxQWApeBQ0bP4dq9S9cW_FVolV6OsHiWFeUo7NYrp0PzpbtJrQwwBTcH0GwBgdD-Emvx7KDxbsgWEsFJv9eam54130rPLr0OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uFgabF-o-udtLH9D3hIAEO4yW1Y7djEIEtKnUrUnUlV1nLgYmULJ9Ey3OnqItMVsv7PRgF3I4Js2-vB-0i4uvF2HKGiuX5EDRgGyfHarz8Ol-UG84nbneA1cKX2e1zzKkTm00dP-W7dTDIWqM3_3NWdDWmW3P9elQkIxdc8b5e92IUR4Xh2Tua5AziSKXV6XCIKIpiQL9Ak84PUn7bN6GrF4YwbmHyDfp_7rY3TP0F4YsVs2MTttsft9tmJ1GOK2ptzTN-HvVV2ib-uVIyjj-TUPT7Nj5P8NNuyOKnoCk3yHJXAPv-IQBDSK-mz4DEPqQyVQaiJZ6Zzuzulgwc95Kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
هایلایتی‌از عملکرداستثنایی آنتونی گوردون فوق ستاره جدید بارسلونا در فصل گذشته رقابت ها.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22441" target="_blank">📅 00:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22440">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFjgOX9vVHATKSfkTvyOQzgJeWVAoiz9cZkl_Igks6QjMQBVtHV9IOfHdSau8qOptJEtGe8EVZfk_FQz5gDbn_0Rg5Uu_dWdlSF5mkc5w5IC_pgD0S9h-PMDNYndKBeUiPrz6ydsAEA-SySOAibO2LvNA0EOzY8w-8ECBY-4X3nockSD1-eFvadctLOdFqCsJ0k25Qs7pjO3-XmF6ypP5OKl6KgjLybG8J8wbLHjIyAgoC6WXtMFz-okdHVw0wVoVw3anssOoAL7afHA9OH6MxOdBz-4NKv_kSleb1UsxdHK8GILpFGUEcZ5ElF70TKgsEUy6HAJPGb7vuO4xTRMLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22440" target="_blank">📅 00:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22439">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5-kIeNbmdSinS6dkBCcLlQS0gm3_migVkQu8nCAQR50v1LS2jQi0QH-yKc5QzHs7mo1N9xc9_5fVagcsfFdKEh4Bwcw40lhSYoFIh1hTiUcgXvKRfkZ9GrIIYuu_VTLzP-SK8D1-9Yj2K4-ecz_Yj85_2w7hu8k-U3I36rahZya-NAsUe4gWNrLmdzQhWCepkC5wYJ-R80tGifknCUBUklBvhQ1DRg8tNomGWaV-WZQMErLrw-If7u94eXIJ_Fee3pNUow3GD3AGn9rJR1bKKxbbu5L80gWqUi7uEiiJW69Si-rNbSszVSCB0daIid_IXFzqTov8VM9n9Z1JQ_auQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کدبیس سه‌شبکه‌جذاب ماهواره‌ یاهست که بعد بالااومدن نیاز به‌واردکردن‌کدبیس دارند. اولش دکمه F1 میزنید بعدپشت‌بندش‌سه تا 3 بعدش یه صفحه میاد که باید کدبیس رو وارد کنی:  کدبیس شبکه جام جهانی HD:  BISS:2585AB552585CD77  کدبیس شبکه ورزش تاجیک HD: BISS:03A01BBE20C16D4E…</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22439" target="_blank">📅 21:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22438">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCqZ4Y0Re7FDNAgRwYzr_I56nZqO0r5laKkLICS3_sCJrystS2cOBdRWJ9WvVITa8MaQ-E-NczQyiwuQLkWeY_S2VU_fY1Ot4Fu7yOVjDwKp_5ERu_o-_XmNeRdyzYvINBSrR2fSxPxelNp6sVzildayIH_XijaMBkdxR3CiNPl0uo4FYCJYFj8u1Z4VMJ-nGG2k7BAd_iMdbBR6tcXzrizvmbpjTbu5bEaWXa0heOh94s9RQXaXs99vsBrQdZjUPVv64k5MxEJpIHMKXC-PDgnAz5rW32T36MIJFPHEt37gtfHG59q5yebG-KMHtmnnPxWM6WLKpNJ1jSAluDoctw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛ ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22438" target="_blank">📅 21:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22437">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
تیم‌امیرقلعه‌نویی مقابل تیم دوم و ناقص گامبیا که در رتبه 116 ام جهان قرار داره سه - یک بازی رو برد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22437" target="_blank">📅 20:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22436">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFdYq--zN2A8X_GTd7cT_8cra7rBrnjpu-Vb0p3RzbHlTXLFGl858acrfHYbw8OBgXsUwRzf87LuH4SlFUZH_4oDKxG8YpmigV8CiPkc6-Ws8_0imPp3J5vM4yJf3_IyppLiT_ZWA-ccw3LSkuxP-ZXw_nw3Nh52AOtnSLc0mJoKAuv-g8oxnkMDRdBpDI4nc6ISP3jQpLMCPHorTxu2b57iisYR1rFS99jq_IEUT9jlqe8aiHBCUr_6XcxYeDwGverJhk-Vy0EtISVpy-9Em2hI0CC-3Ewh2lyLOR45H2yCDafXo4wtmXEW08IR-2K7ZNRC847s8qIR8_GOyVknxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|سران باشگاه منچستریونایتد به درخواست مایکل کریک سرمربی جوان خود با ارائه پیشنهادی 100 میلیون یورویی بدنبال جذب فرمین لوپز ستاره اسپانیایی باشگاه بارسلوناست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22436" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22435">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🏆
کار گرافیکی تماشایی از قهرمانان جام‌ جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22435" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22432">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQoBa07U8HfBO4QgxGvbxG7fW2sJDbHd81LhExvU7up-LG4hPVcR5_H9pfcH14kS0OgZ0IiHPH5IyDpkKb5dd9iYxetQlrr-FYQf-oCOG-OrrKYHFz0XMb21TDICWVURSi-pE9lbFdKOv0c_pzJaeYszc0DaCn8HEep5nyGRPmMIKoZSLteHjb6aXP8-WAb559WABKp7ly9Tzim8-Tl-eXAgf6sDhgrYI-f_VyKjDu3bdRivQ5vbtgkfuM4r87RjegEU-MReLSrMAOoudMmq252l7vEx1uysbVe1bQ6EWKis5JaM0ZTEEVTfb2UXzyA-wmHzhhqdMDaE2CNwPiq2Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
بیانیه عجیب اتلتیکو علیه بارسا: «هیر وی گو! ما یک فکس به همراه پیشنهاد خود به بارسلونا ارسال کرده‌ایم: ۴ بلیط برای کنسرت فردای گروه «بد بانی»، اشتراک سالانه ABC و یک کیسه تخمه آفتابگردان. مشتاقانه منتظر پاسخ هستیم تا «اعلامیه رسمی» را آماده کنیم.
⚪️
…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22432" target="_blank">📅 19:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22431">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvUA3bUdoQclWT06kc2FOSKlGNDdchNnYw8a-C7qeDeEsj9sPdHlv7lCzHri50fKpc9ASLIa9UB2DE6eX5OqNLaPaJJWR6s-XGv3Gv0cZMwMu8n2_RQX8cAWjB2waF28iC81oro3dkknQ5gTOeYac6onPV3b_nGoE_WE6WtbbKW7pgJMlPOBnvmDiNDsjPOqQ9NrBsvT9VX2ELD1cZmxr-ujhoa2xSpk72EnPRXdyeROte5CRQBnWMKnmNb5wxmnGp-yFT7s4sIEtHke8JMBHLPgdx5P2FSAFCjV71xZyVjRnhyWkqR4CQoactgBq_GUxCH4YZBsNnW1nzgWEafKRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
بیانیه عجیب اتلتیکو علیه بارسا:
«هیر وی گو! ما یک فکس به همراه پیشنهاد خود به بارسلونا ارسال کرده‌ایم: ۴ بلیط برای کنسرت فردای گروه «بد بانی»، اشتراک سالانه ABC و یک کیسه تخمه آفتابگردان. مشتاقانه منتظر پاسخ هستیم تا «اعلامیه رسمی» را آماده کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22431" target="_blank">📅 19:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22430">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLe9HHHzXIf7HHqQhHzxub-Ucyc8pq1SZB3B0hOhJuFn3sLaXtj-U91F-vg9uHeAXm4pVwNsOX0yDcwrt0_yi0GAHK7JQwnn-NOwKYoRIwgK3FT9On4MGa6T4MXEgRBg0_BOF-I85rPmlNw3KuOWg8K1Lp3dCflbgezq5YPqTyc7x3geYBB8NL2r1PGrtoOXGG0XuUUFdMeSFXBdndoFDj-1ffEWHOzawpxDPfFKC11se0BtEXk87wHG54KQsBaHCQYLVrKz2g_STVC2VAosQaYKFYxeoENT5RST0k3YVqG52MKFUj-__jYf1jgBmlTyBt63wotksSMlrBEHtJ9q4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخرین‌اخبار منتشر شده؛ باشگاه بارسا طی ساعات آینده پیشنهاد برگ ریزون 135 میلیون یورو برای جذب خولیان آلوارز به اتلتیکو ارائه خواهد کرد و این بار این باشگاه با این آفر موافقت خواهد کرد و این انتقال رسما انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22430" target="_blank">📅 19:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22429">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsmUc8ASK_LoDByDy3lJwG8YhGxtHKHECPI3PVsMCYN9AavSdY1ieFS9siGuOHJ3Ael_c--qcTUBD8X9oEFUEyyLpvwqNu7lKO1KovI5278_djizPzyDMC_fXSeys3UMPYXrpPfiwgk79e8IK16BC383wEa9FtvLopk1QxvQuRiFl7aPpuwu7b0-fTeyIEocdSyiWzMpi9gM9jjG7kgAupacDe8wdxUiDxp254QBhDIY9SmoAjwSchxTTYB5USrlK70w8wWD8G5QvFRm1XDy7EqTI2whRMeA-RVMENH9h0qPGJJcW6bEvm60bEXklD3A2XoGr9aNYQtaWyfijiKvyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام ایجنت رامین رضاییان؛ ستاره ملی پوش استقلال که نیم‌فصل دوم به فولاد پیوسته بود برای فصل اینده به جمع آبی‌ها باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22429" target="_blank">📅 17:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22428">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e99804290.mp4?token=qAWaFx1-8LKmkelJHbVJKnybWsXGuXTwnP1Kpa-E8f45QsvzAiNsDbyVkSB8EMraxOyZIsZKLtCyAfzcVx5PaaMo4UEpCvlnlJN5NBnfQewrUO6teT4ax6hk0D7WcFLezjGKhUh5GMuEga8QgUtWnpARurWwNfdc8XA3pKEIXJ7cUVhALkyLJrq8E108V3yxAUOMzo4qrxFHfaoIY0e9HL8HtalMkhOgDb8L-9JGaVe25jzLMB_FPJjCXTiB5-eYIzMsYXcA1PBoiAtXLXDxIQR3GvinF6mHIKDwFsZXV_qKCHuYYc18Z7oe4S1Na8Dwa2ccsSOVJihK1Coj12EjIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e99804290.mp4?token=qAWaFx1-8LKmkelJHbVJKnybWsXGuXTwnP1Kpa-E8f45QsvzAiNsDbyVkSB8EMraxOyZIsZKLtCyAfzcVx5PaaMo4UEpCvlnlJN5NBnfQewrUO6teT4ax6hk0D7WcFLezjGKhUh5GMuEga8QgUtWnpARurWwNfdc8XA3pKEIXJ7cUVhALkyLJrq8E108V3yxAUOMzo4qrxFHfaoIY0e9HL8HtalMkhOgDb8L-9JGaVe25jzLMB_FPJjCXTiB5-eYIzMsYXcA1PBoiAtXLXDxIQR3GvinF6mHIKDwFsZXV_qKCHuYYc18Z7oe4S1Na8Dwa2ccsSOVJihK1Coj12EjIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گل‌تماشایی هریسون رید بازیکن‌فولام به لیورپول به‌ عنوان بهترین گل فصل لیگ جزیره انتخاب شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22428" target="_blank">📅 16:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22427">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEZo9PHlWohEYpSK7Wnprllzl4p9ZmeYXQsQ39Zk03wGkTOan8GmrPiQPYONfcrwpB4aNYDZ3c7VsCH2UggZ0y1R96uRlg-ireRiBqrUVM6PbqfDlmA0DNf-EEVIxu2orqtP22AmCzq5ISzSLDfinvpUPC9T4Rdk9j2eKZ3PybPUJGT78-fQrnSWSJz6HT7WLmmu1HqLOlsamslcTZgIuqCy1wn4odcJ599YoFzAtXDdeOUqVFa9aZE7LRr1WPjm56S7Gu4fAfsRJXKpfZMrtxxZgyM3x9ia-R0Ysf69IiXJrieW6wSAx8-O15je90k1zylEq4ZzUkB439XokBOewQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22427" target="_blank">📅 16:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22426">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxO9g1lQnI_ZhnhZvDAHTY84wm_hhd4A2M5Ky5zYGsDS96ESo4kdM5uz2006svz2g-fAjOSR-cjPbx5qeMbD61l9gmC8ToI6RyXWR1Lc7n5VCBFkpTKbPmcAOa3uJdnTZ75yJxHhUTb7_7oe5VZTGCm53n_ZpSh0zZGeQbT52lwW5WxnjvRrzcTacppNUZjkHbUo4--e4YE4HQJ9xZm6W1vwvJxhFLQDZoPldLJx02YAYXHTfreQOri7digZSznw_piCaFCoN1hhOM3tW1TCrk2TAgDvNaCTvDdBuBYJB9SonO_AXMqJRw3pyKCkdbgTP1cXqYphf0ahv_Cw1x7T0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسانه پرتغالی آبولا هم مدعی شده که باشگاه بارسا در حال نهایی کردن عقد قرارداد دو ساله با برنارد سیلوا با دستمزد سالانه 8 میلیون یوروعه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22426" target="_blank">📅 16:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22425">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ccdf1c58d.mp4?token=fZXKfz2ba1_nQE7po6p0ft1JPQfOxq-uCqSyZdvCfGfItBzllbx1iFaHhcVjxMgLyomICv2j_fnbj3TOw4hUJJaIXgagsrO58ggYlMGeMnDZu3skLhsD3auW-Vug7SbFL7PKNZHC-v6JhwR-wOhh0ULWGiCfPNSM4QkKEKCYOpNvNfVPO7bnGCQNrSGEl99ICReyChIStAPntgI-rN50h7SQxE8bjZ5KUn2LzXZGtBK5gqwiO42IJZaJl0_mrc_T4EOoZX4hDTjKyTjgDkuieNEEBnSXQn7Ds7GXKK568tvD73maxHg22tKOSi4cZuZN23js8-GoCKjTmGQ7a_YYYYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ccdf1c58d.mp4?token=fZXKfz2ba1_nQE7po6p0ft1JPQfOxq-uCqSyZdvCfGfItBzllbx1iFaHhcVjxMgLyomICv2j_fnbj3TOw4hUJJaIXgagsrO58ggYlMGeMnDZu3skLhsD3auW-Vug7SbFL7PKNZHC-v6JhwR-wOhh0ULWGiCfPNSM4QkKEKCYOpNvNfVPO7bnGCQNrSGEl99ICReyChIStAPntgI-rN50h7SQxE8bjZ5KUn2LzXZGtBK5gqwiO42IJZaJl0_mrc_T4EOoZX4hDTjKyTjgDkuieNEEBnSXQn7Ds7GXKK568tvD73maxHg22tKOSi4cZuZN23js8-GoCKjTmGQ7a_YYYYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌که‌باشگاه ماخاچ قلعه روسیه از عملکرد درخشان محمد جواد حسین نژاد ستاره ایرانی خود منتشر کرد. حسین نژاد تنها یک فصل از قراردادش با این باشگاه روسی باقی مانده. درصورت باز شدن پنجره آبی‌ها مدیران این باشگاه تهرانی برای جذب قطعی این‌فوق ستاره 23 ساله اقدام خواهندکرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22425" target="_blank">📅 15:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22424">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULLWAL18ulGadl0So73rAT3UqWjKdYRDsCObnclAYNW8i7d9sQsO1WfAyscpwDshf6ejeMwTr5oRbnatrLUV0prj0uze1jww-IIA9xpQtUh3pUNyz9orgirQDRBUP1GqG6tIWiqihPtHDReXfIwcvckHP0oPFdDsqYpWZwVZZrFye3At4akzWkN-4v-uAWDosyDpb3uHIBJdCOn8TrhbEJmG9FY7Ru3KPZfwvNdxXYLp7sSCw7jUH3pNTuDeAzihKQyqWnLbqkw-ffnM86SZwvUws6eZou_ZgNh96qa7IQeF6xOHzkSqib7HH-U5l7X7HVYYH7CrFaENiJBBVtZ6CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات؛ رسانه مارکا: رودری ستاره اسپانیایی منچسترسیتی میخواد از جمع سیتیزن ها جدا شه و باقراردادی 4 ساله راهی رئال مادرید شه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22424" target="_blank">📅 14:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22423">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8HgQXXMi0u_CNxuI29JMvjOfA8TLuueiGh3g9NV9iJOSZWpXFbs1MOwWnnPUKUjmVcycffKYhmPrl3eXTNWQ1SzOnof8RR0cYu3U8mICei4Cz2-RpENrq92y_ocX3ipZ1lrxrfTHrKmry8CP6Z1866j8bn-c8RB9ORqZ2MIkHb-eqP431IfJ0G2buO_TrGsgJt_1cuXM9k2RVL6eF7qIPwkKeANverVSg_tJPQbrtojqLMkkenGa7Oc-qutZftGzTIgEXKgrl_OQCPL_L0YFg7QDv6KLjQc7qHyBgzIbW7ZbFM2pAJx_uzaQZ9LRddVfGQKEMDz3kw7vgHui_oC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جرارد رومرو: یوشکو گواردیول مدافع سیتی نیز همچون خولیان آلوارز در خواست جدایی از منچستر سیتی کرده. فلیک عملا با تماس هاش داره راه انتقال ستاره‌های مدنظر خود به نیوکمپ رو هموار میکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22423" target="_blank">📅 14:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22422">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DffSOTOuOpmmgRb5PAbqwzglYWphIal_IEGUXPHihShiT-ZFVBbDOuxt_53XyAiuTsVD4Fh--FiRqN8mBqpIQ2lqeCLsVmifOsy3aAtpNEA87T7G5qtTqgLy0Na4DXX0KuSppi8aRNY_yyNR_n7FCKBfPfLRtxvdC2UE2x39_EOo73n0TIlecG_siABhzdCH3LeKIvFwUzwH3SowkVrjIJFkfuoBdihVOc5Ll_iNQtZazkN0vMtGgZHhI65q4hISR2LgIls_iMMQbNOzy6_0Z4CyYEuoRRg4b_smYICPJKp7BynQf-2EGfwOzoaaSpa4ermdmM3LmFdF-TONoNmkqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌انتقالات|ادعای‌رسانه‌های‌انگلیسی: یوشکو گواردیول مدافع 24 ساله منچستر سیتی هدف بعدی سران بارسا بعدِ نهایی کردن قرارداد خولیات آلوارزه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22422" target="_blank">📅 13:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22421">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNrc8VpSfvi6oC3GTVBuwBds3uhZJ1dnba9pJntx4rhCNbaMdPWIk8YuJVztVpABxn8Equ4HCGyMFWNG94BNUE1_jFLwKKLFuNzVs32kzOE0vk3p67786dM254-yGYqQlBhNmVJSoc89KHMAkvq46JHRd-IqrkTR_d-ey92Anxwvkge_eNE_ufvry9xKNGGsrIbUvRI4z3mrR1xjwXWhQnU3xkHwSkVJpAen_lEq_3d_eT0HzAgWYPRcgDgSMVo1uY6lgwZiyGd5TqrfvnUSyqtTXAjueQ6CZiXbMjYemp6BxJQSlg1e9WIR9-KLRjV9kpHzKbgGtx2NB19qFt4mww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات؛ رسانه مارکا: رودری ستاره اسپانیایی منچسترسیتی میخواد از جمع سیتیزن ها جدا شه و باقراردادی 4 ساله راهی رئال مادرید شه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22421" target="_blank">📅 13:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22420">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVlWjZUGXi4u1FvgireEcVPNpJZtUnfnK510o5eaSgxM9yv1ksQC6HJkhuxqGgGyKyOD4QBOOnfZgRHY9ADgjJbNwK9aZEgxuqSKt3npNe4NvdtdRFR0nrw4UiXohcyF6jH8-U6_f2iVqnzQVKeb4K_QEKG7lUnI8VG-UYP65wJP1K6RH1KdVA8Kfs8YdDtL_lH17dYzLBCF5h9PEG_l2L1rfJd8OPut55qBeYcDaPFer8tjlEQHO_ahVtmZuIESucD4yb4PUFih6EKEyDQIQ5p5GgX5bxr7g07Viuioact7gpuZUo40jmiHDjWe_CpniU1_NFxG69AemRFoVzmtnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... یاسر آسانی ستاره آلبانیایی استقلال امروز در تماس با علی تاجرنیا اعلام کرده که فصل آینده رقابت ها نیز در تیم استقلال خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22420" target="_blank">📅 12:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22419">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHwYoQZAd3Tx7xuNAYsxncaKWCueMyNuhPp-weRmbAxu1TvqeldxAx2LEh-g0E6xPaENB_gxT3KEPw0H3cCIMOpwoj1XopTiknnqUWiSMElNwlxvo_E_IzNyWFOgbmMWtjznwGDrNUjWS7z5JBmDgVBHxjbtSQv6saECi5QgSmnAPxK5NSbC93pnFgqDzM8TOwXGudJo2uLN8kXIUuPtkeyhPQj18Co7yn5Xi5O1viZ2pyod80jRrABMTUheewjNu2hBeyB_qpDmrqUgNRXq6EHHriOdmTtpoVYis_Cd1Eu9iRUtZcBufSIySTxPYH6Sbz56ID5AEFoiEgKSVF7n4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22419" target="_blank">📅 12:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22418">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_TSJiJixeuYRY8rjg9qaUY9x-UAQhRwTLnsCknklmhiuG9CamTu-aDn007ZM0FADm-z1ry4t4SywbrY-GMnPuHCjqlDsyhnh-ear1vqFRJE79vLX-1wtkTAH9eWNMJEfRCOvCOLJncVg1PeeWxsVZMpPIX9L1pvk0s3iw0UFjMYxyNXzatcKN5wR5IyJNU0siLhtdA0aqQmFVYX6f18x3VPP186m197FjiqNp5qF_N9wM1TSVFUfctMctVac0OT8Zc5dD7E4v_YbYtGD5kHFxOvQUeiTyhHUBMHqR_LTxMqX6V8sob9enfmU4Plq8xy9FrxzurTckJiInrI0uRnWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇺
به‌مناسبت فینال لیگ‌قهرمانان اروپا نگاهی بر ۱۴ بازی گذشته PSG مقابل انگلیسی‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22418" target="_blank">📅 12:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22417">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AElSwejmDo0hgtTKD-LefDDTrMt3kJiun6Xheg6Tp1M2UWb535jzt29Ep8pY6RC0TtauFsMjaQs3wmHmseHlSC_PIwpCyMICPzqfF3_ejyWuDCwMlj2pcl6evshNdwGPqCFNk7zRCyK4gyy_VIxcbXJIEPVAxoPywsfRKpnStKc_SDtFqa3JAudEqH0w-Vyh7OD2BZl0vMCQlW8FKomDJcohxRsP92KvHSNQq5-faSYNujYn3iAeZErLWn-wNgqnviXs1VFYONBvHBPsecUsQO-sb_xmjSylbEJ0zpAa1EWzUnLPDs4J7qVVCVRqtBcg0G88sHFQO4d4wT9cLvc__g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات
|کوناته مدافع‌ فرانسوی لیورپول به‌سران این‌باشگاه اعلام کرده که پس از جام‌جهانی از جمع شاگردان اسلوت جدا میشه. از رئال‌ مادرید به عنوان مقصد احتمالی این بازیکن یاد می‌شود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22417" target="_blank">📅 11:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22416">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeIpWBhcaxIezeWRiTWN3K7tXHWfGF4AKxdgZAVnExNPgs3-k5FMohov8y4TPzD00uT0exzhwhUm7zQFKfsclsuUzy6UcsUVPWiPsYsenmkAvuzTuIecduK9JcWmwiXfA5M9Y2G1QPdFFoEmEjQhska5h0RB8OgMmvvr9Ry5SNcAyKhv_YiXQ8uRgTgTmBKsZ4E-heX4-GVyHXNchQnLKGzXPQ1Z3XMRdjSD1Zio2YjNalLyOQv3K1Ok6poFX_Z_S6mU9NUbzp5zcA0LS5GM7eM7N6fav6Y5G94oYpgNP8moh5VJycBlP_2O36FahQScKvqORQNJEPNblh-yHOeMaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22416" target="_blank">📅 11:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22415">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBJPEILBa6Kb81cfwUWGbtLxhp6mggmgPfPlJI5LRFQJzjmBcbnDvSlwtpx5epqlQFRQeqLxTLd77GmPMzTohzHVCbjJu9zCTOSnbSPn67OL3WAEjtE64kEgYbFTtIi6tfyxytkWDTKtK8-E9XuRk0kL5lcvZX9v18yG-x_O8RrWyose_sk2-e57lqqf_Oo6twggrMwGUUy4CVHWsp9ECirM4iF33nicS6OgxWrICWeDFsHP3nspxAIqrOasFicEEYEU6ugIvgMqDxMilMhq3oyB26Ir-4yTk8Jc6UQNs38zk0lGcy87oJqIZ8Y6fNrdu8xKItb_1ApSjmoLS-w6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه، انزوفرناندز، ویتیتیا و ارلینگ هالند چهار هدف جذاب انریکه ریکلمه درصورت انتخاب بعنوان رئیس‌باشگاه رئال مادرید؛ انتخابات ریاست باشگاه رئال‌مادرید روزیکشنبه 17 خردادماه در تالار بسکتبال رئال‌ مادرید برگزار خواهد شد... فلورنتینو پرز و انریکه ریکلمه…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22415" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22414">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2NCQi6xQUHkH0xf6xRBb79VpkLu1EpQf5IF0GHTPK_zTzSPuf35akCL5QJ16xV3f-Zf286h1fHhb28dnyYatypo_plxzQQz2W3U4KazBGB2Z2zjM1wDDVuIt2P3fHrMmwLtEZiBhixmLibWaopqAfJ5sLHNb5Tgthilgf_4lWCQKy7ctPjkmkn2vQYQk_oI1RCk03dwVW27tWCZvWSpt0LUGLuvbu9ynt6GUiur3ssFzcwvwwNY-j46lLCCVieiBiq4BWTwO6TU1W5fQUXzRfO9FWKijhCFh-zc3V5Fkt-Jxv9HiM37I8AHl-F-LLhxoVgBQB9vRz2ASX8yWTTeBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه جذاب عملکرد ژاوی هرناندز و زین الدین زیدان دو اسطوره تاریخ دوتیم بارسا و رئال مادرید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22414" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22412">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSmZNgbRwyfpOm8Fj4Ia11IUAZYWPzZDHWyvuabsYY_OnPILDWS2xm7FHlOy8UTvvthAqcc0mP-LcSSxc9SO2SqrzuQsJ0ipuNewTYXxJZHj5bca1tmHCGDfVVgTy7csQyfKm3JUttFoohscdf-hbXN8GtwpNiGYOpPxF2vr6xJxpAmCmCLzCN0KlFqGnig2-J3I9D8FyQ6M4fRuzagbYMWxXASAgSW9rARtsGm9sIwyxp0-84DGLDRW3kn5VOe3P8Ixw_4iGuw32ZxN4GDKonaO3qLNsJQQ85X355BE_n3j83AHf1EArR01cMLY__Im83NvqRWWn9PhRhaIG4RIPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
برخی رسانه‌‌های عربستانی؛
خبر از مذاکرات مثبت الاتحادی‌ها بانماینده یورگن‌کلوپ برای پذیرفتن هدایت طلایی پوشان جده در فصل‌آینده میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22412" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22410">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ضد حمله‌ و بیلد‌آپ های تیم رئال‌مادرید؛ طوری که زین‌الدین زیدان با رئال بر اروپا حکمرانی کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/22410" target="_blank">📅 10:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22409">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c001aed77e.mp4?token=JP6N-XimTclLmfbybgC9B83PjLZsP1rezNYz_Zx_qx0wCF61PLNkdV0GV8-1UX4OnnmwCrLAkGBGju6T1XDw2OS8qjvTE91m8dcsIETAPUo8QNL39G_86l6xRhlu0metHXhC65py6DJBddituQhPFOkLgoIknPFMTrzTLOrV-4qSgO8N5eQCGVYwkbjx_yZa2wBbmewj4CQ3vWeTvGhZFze3IiNgmbVZzPsRTLE8RNlVT0BBROcbjqJtV3dP1WGzEMeshRG5k10ZZwNGamg2XZ54gieLAIswwXUVUtJ2bThcy3xPcjV_Mjkd1XrQsLg0Gpe2s6YKFlMbFJU_0_YX8FNPyiUcqxrZlaSVWMyoPePfQeuIJfE1H988Erx6to88xQB4ACTRV4PU0K-2AChEChbm3I427gKXOkfdHX6Sfd76JbAvwug8hot9OIWcMJgd1wIFJQKvEkx5RPX3Myi1tH9eXmkf6cXJgleVR0QskF9VZ2mhN3E5TN4orecIOPRX9yQEfYah9Gs-s4ELusQi1w9xsJiDrz_u9Eg8WJfcSArTvFeGBlyhowMp-hwQ-tw74KYv-Riji5D6xQietZDAhjuY4Xp3OvRHitQDdiz6ZdIGHAFUIspnK-S7ufCDiSSHP2KlE-KO-3t0JhaeAbrlhakGiVGx6Yor6yEG9RvUzE4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c001aed77e.mp4?token=JP6N-XimTclLmfbybgC9B83PjLZsP1rezNYz_Zx_qx0wCF61PLNkdV0GV8-1UX4OnnmwCrLAkGBGju6T1XDw2OS8qjvTE91m8dcsIETAPUo8QNL39G_86l6xRhlu0metHXhC65py6DJBddituQhPFOkLgoIknPFMTrzTLOrV-4qSgO8N5eQCGVYwkbjx_yZa2wBbmewj4CQ3vWeTvGhZFze3IiNgmbVZzPsRTLE8RNlVT0BBROcbjqJtV3dP1WGzEMeshRG5k10ZZwNGamg2XZ54gieLAIswwXUVUtJ2bThcy3xPcjV_Mjkd1XrQsLg0Gpe2s6YKFlMbFJU_0_YX8FNPyiUcqxrZlaSVWMyoPePfQeuIJfE1H988Erx6to88xQB4ACTRV4PU0K-2AChEChbm3I427gKXOkfdHX6Sfd76JbAvwug8hot9OIWcMJgd1wIFJQKvEkx5RPX3Myi1tH9eXmkf6cXJgleVR0QskF9VZ2mhN3E5TN4orecIOPRX9yQEfYah9Gs-s4ELusQi1w9xsJiDrz_u9Eg8WJfcSArTvFeGBlyhowMp-hwQ-tw74KYv-Riji5D6xQietZDAhjuY4Xp3OvRHitQDdiz6ZdIGHAFUIspnK-S7ufCDiSSHP2KlE-KO-3t0JhaeAbrlhakGiVGx6Yor6yEG9RvUzE4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وویچک شزنی دروازه‌بان 36 ساله و لهستانی تیم بارسلونا، بعد از ۲ پاکت سیگار و مقداری آب...
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/22409" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22408">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3294ce3a0b.mp4?token=sVZkrofRIS-NXyIQPjdlP5XN5kr38gtFVYvQKKOuJW-o8WZRcCEYChFZZGBjXnXFS6MN5wPBBHobVO67qVGGVmuqgCcATFNAUWXPJIPQBGG_mO9fQBCmBbDdZBY8pRFV4aC8Opug5kIfGwcoqAqgRhtHuD0R1arO3Z_1Ltf7x0zXFcJ3Gy5NvCNysZoL_OZMY614JxNmaZ4kPHFlvQffXkPqhXaVu9OJjL5NzvtO90dGP8mO8DQSBDlN96pMELVJE4xSU7Ji8DNfMx2tpQ2cHerx5OSYDGgGWiD4Cf58CcHAO6drp76ZW1rgZqh38FdQ9ojzSiRe2lIVIS1sQtQ4RpS8MIGZJunx2fcwSHPN1mdLTAQlCz0PolNTBj5F-XBeij-2_F5WWRGk-pGtD61xiHWCFwwmurJnR7I9NYFgdTbqbAp5tSXc72e0P5riyC1oFsxQnelWQmHKvAj6DgsGNA1O_x0kFT8QSg4kcGTuQvUtLdqdKxkaFRcdu0EBbzrGwFQBuaKFQvMTE6cZYmlr8gdk98vzAHmtNslKm8H8WQbO2qAA1F5T5ncrGBT4qhFr9pXE9W4sZNFpXRwU1-GCyKUs_S8kgYcqpyOxzzoVa2UHNSaSVsmAMZo8y2A4Ohvydlbgz25kIDwjevC3_eN30Nhc45qPgTKAf89MoeGUeAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3294ce3a0b.mp4?token=sVZkrofRIS-NXyIQPjdlP5XN5kr38gtFVYvQKKOuJW-o8WZRcCEYChFZZGBjXnXFS6MN5wPBBHobVO67qVGGVmuqgCcATFNAUWXPJIPQBGG_mO9fQBCmBbDdZBY8pRFV4aC8Opug5kIfGwcoqAqgRhtHuD0R1arO3Z_1Ltf7x0zXFcJ3Gy5NvCNysZoL_OZMY614JxNmaZ4kPHFlvQffXkPqhXaVu9OJjL5NzvtO90dGP8mO8DQSBDlN96pMELVJE4xSU7Ji8DNfMx2tpQ2cHerx5OSYDGgGWiD4Cf58CcHAO6drp76ZW1rgZqh38FdQ9ojzSiRe2lIVIS1sQtQ4RpS8MIGZJunx2fcwSHPN1mdLTAQlCz0PolNTBj5F-XBeij-2_F5WWRGk-pGtD61xiHWCFwwmurJnR7I9NYFgdTbqbAp5tSXc72e0P5riyC1oFsxQnelWQmHKvAj6DgsGNA1O_x0kFT8QSg4kcGTuQvUtLdqdKxkaFRcdu0EBbzrGwFQBuaKFQvMTE6cZYmlr8gdk98vzAHmtNslKm8H8WQbO2qAA1F5T5ncrGBT4qhFr9pXE9W4sZNFpXRwU1-GCyKUs_S8kgYcqpyOxzzoVa2UHNSaSVsmAMZo8y2A4Ohvydlbgz25kIDwjevC3_eN30Nhc45qPgTKAf89MoeGUeAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی از مهم ترین دلایل‌موفقیت انریکه و PSG
: اون برای بازیکن‌هاش‌بجای یک پاداش بزرگ در پایان بازی، پاداش‌روبه‌بخش‌های کوچک تقسیم کرده: مثلا هر پرس = هر موفقیت = یک پاداش عصبی کوچک (دوپامین). نتیجه: انگیزه پایدار در طول بازی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22408" target="_blank">📅 09:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22407">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc6b58323b.mp4?token=KbTH4eL7DOIDf8y9q4dmjCVbV1ph9qmWA61FqAHb9831z05UFzEM-jEpMgXMJAI0JWUexi0l-TkZU8q5FrcW8MTu77agqI2Pcg3AL-NdM8q2rmREccAs2aKx-KbNKxoCVTgXtK80tCgCWwIGDridHwUwTqfLnspMxvX_lJYuW5skLAFFRXpM_0QwXBssPWYihl8_HuY5DN96Ndd9eqGgX1KUwIASRlmMqfT-NO1NE7wmv_HLiFl0O6LPOKwDGTzjk04Le1dFirbbmrG9AdR5Bzr33IOAoHN5TwA8mIQZQ1IOs_ZtKXDg0-e_ZcmGehlRnMjI5nhKzLAc5kRiiDfXqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc6b58323b.mp4?token=KbTH4eL7DOIDf8y9q4dmjCVbV1ph9qmWA61FqAHb9831z05UFzEM-jEpMgXMJAI0JWUexi0l-TkZU8q5FrcW8MTu77agqI2Pcg3AL-NdM8q2rmREccAs2aKx-KbNKxoCVTgXtK80tCgCWwIGDridHwUwTqfLnspMxvX_lJYuW5skLAFFRXpM_0QwXBssPWYihl8_HuY5DN96Ndd9eqGgX1KUwIASRlmMqfT-NO1NE7wmv_HLiFl0O6LPOKwDGTzjk04Le1dFirbbmrG9AdR5Bzr33IOAoHN5TwA8mIQZQ1IOs_ZtKXDg0-e_ZcmGehlRnMjI5nhKzLAc5kRiiDfXqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وضعیت شنبه:
آرسنال با یک گل مقابل پاری‌ سن ژرمن پیش میفته؛ داوید رایا گلر ارسنال  دقیقه 34:
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22407" target="_blank">📅 09:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22406">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8j7lcbDamyAitgfrvvBP9Q3EKr45-RO2_0JzvR__h8-xomCbaPfKZUwoQUgiQzvP2RIsRBV3TLocpV2giG9nkfeLT2Yk6UmI2kDcNe491vUyRP8ggBJGoqpGWWOd4NAuBR1tPGWLIjdVh6aQ6MkWndG8wbzujxkDUzhDRsdQ1L4iXNyLMCjbaqUjWZp5FNJx4hYX6xlq8Lfhl_Tnz9R8CXtD1DIC6RM7wp-iIVQ_niY6Uab39PuBmThgPFJFhG9SfBu0XIyF03AGf4uQ4u_ts_qvr4vUcm1boRe16zqKmgwGWOb5LaLSFeZTOuYVTy5iMu_-8qVCaTlHC_OxfhXLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22406" target="_blank">📅 09:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22405">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5jupcpTx-PkRvWzy0wy68iIzrErxTV_E-0ZhZhpRK-MJlwNmJFkkC_NUD2npPvibJvmSjj469uvj9J-GTIlD9IpXs0w_B3_Ns9pcBskxNfhZCwdwL9QN0kCHwx3-ZDHknKMkpLXoaR_d61KhUgQCrBpqCvB8cdYxe4wZi6olkw7TfSuZW7g7KgdGstCafzr7VYGrEeJChTFaPHGfwA_o2jk0cO1bJo5ANQx4in6Bu3uHqqEDJgLDcKbIkULd8kkMoEp7koKLDAyXtQLilinOjMmx_ccVjv2s5sm0K8iG1-Oo9tYq5swXWp9XMikJba10N5iRcJ6EwYd6JPxz_XBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو آموزشی‌نحوه‌واردکردن‌فرکانس جدید بصورت دستی در رسیورماهواریاهست؛ شبکه‌های یاهست که بالا معرفی کردیم همشون تاپ ترین هستن که بازیارو باگزارش‌فارسی، کیفیت فوق العاده، بدون سانسور و تبلیغات‌آزاد دهنده و جلوترازصداوسیماپخش میکنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22405" target="_blank">📅 09:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22404">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xgxo9gq5jtiWRHhOYq7EYpeEajoNTRVHdbps9yW8Lsn3eouXFRomOTej34MxZvNAIyNNkS3qm4k9e01-RHY71gN4LMRG1VNNZUxJ4wUi8rjsd2Su2_r4p555hf6oBWvreapQ0e3hh1jtAgKNY-k9W-OrMkhOoL6yf-GH74VyAEeAvXEixRACWMbFW6oktMe5CEV4nPT_cuocaNIwr2k-zUTkSGr8H2KjXuPA7Qyeq3IFrdl2UGuDrIGtl3bnde0Cfuw62l_nVen0RiZI7j3yPi2T_X_eU0IZUC8sKaFIdpGvb6Y_p6SqRVAq2CHsnaVS_ReVX5l5b6SnmN5PJlWOfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ الهیار صیادمنش مهاجم 24 ساله سابق استقلال و فعلی اوئسترلو بلژیک رسما از این باشگاه جدا شد و در حال حاضر بازیکن آزاد بشمار می‌آید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22404" target="_blank">📅 03:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22403">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRxG7Xh1PCu6I2W9Qllpe2WaPP0DiYw0NvL8OhyBKUWlOP6ir7SZYQWB6Newf6nrBWiH6YJaslwRZjKjpEaBw1wpdzrX-i2Nd7JJkYMhFVkqmugPLOBeudBLaLKqVNvJfnytAGTXHMB0ekl9TQE2RS4r4OAfAQqqAcm7fEJ9Kk2o9eKgszJI_3EVhdHVVxPhEWlWflewKtU1vby8KZ01DvHqr1HHf-XCv8fDLZvqkbzLsN0Pqcenhorjg14RPogofAfnT4MMB7k4zYiFVK4JuMUBINZRipwVMFDeW_331fLtWLkk2W1CTkGsUbIwyGiq0MDvwTxxMjtGzrStKXzJ5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لیست بازیکنان تیم ملی آرژانتین برای رقابت های جام جهانی 2026 با حضور لیونل مسی 39 ساله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22403" target="_blank">📅 03:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22402">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBHzyxcb9aausfjY-2AQBMfuMntXquj_2iSiJKB6PyUcbEQ1A8m3xfTuhDojU3Mwhr3XigjZA4Y7A1fp3Dirb5Qss340NdfOlaED1ZHnTWJwxNK8U_tawlaPtTtKQgTeJpKxx50LiZgbydzum6URocUorDrpxEp5_Cnj-xDbPnHtREM8td-2TK5nkrLEr6sRM1aLDysJ7xeqb3SuFogDSSXi9mBOugRZuoZYDyjDoc6J046OJOd9BoBO8tu45Y9c3Celzm0j3kHIXPV1TblTgf_vWsELNV45BXKur76rqnKgY133ADTtkUPlGiFzIKmTRBamZUp-yA6Dc2es4g2TKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه بازی‌های‌ امروز؛
دیدار تدارکاتی تیم قلعه‌نویی مقابل گامبیا تیم رده 116 رنکینگ فیفا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22402" target="_blank">📅 01:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22401">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDZ6lGmN5IRSs9H0bhFlh2eJMrlEnq9Bei_jI0d_RlIkHV6ja7c1ZuNJNjBFZ3j2Kol-4WCM-sAy27HQOWN0-zu4T3-Vr5xiwk-hinFafMOAEayDHI6RKmMfbUkKwzn01BKo79NLUFUuTnSIA2ELPwbSjzjltfsZzFpY9J_qcRI7CXOGZ2rbQ51n73HWyyGJBbG0_U9p9X63JyJCbUAyvNvlF9iL4Zv6dBIzyoUEDmKqd2GIRp4WgK67rlNYMG1CERpOz7vUuq5qBK8px2g_tA4YA2U-o7vIr8MpdcpvAmktN4j44QlqQx95owcll8ENN1NAagkmf7KVKGFqzuklXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
برتری مصری‌ها مقابل روسیه و شکست یاران لوپتگی در جدال با ایرلند
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22401" target="_blank">📅 01:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22400">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uN1vRXLNyswqOPY_ibbglom3t7smlGgfASds8ODY6vBCM4Zxo1VzaDDdkR1hZQHsRa_pGWjxZXZhlYS6RC28OfRjNmA7LJma9_JBoi-RVGjagZvemnKPMCQGHi9OfdHabehKyRbuz_1RIFIzKwEyaM-lzVEQzgu5_wh5M2HJZGkvsJjHkP9l8_3ZrZJ7amC5vsIGow6jXUwe0adLqQlIJxXdNJDXScMT_ITJ2iMvIV_bS9ccEWfVeocXR8Ms45fFIAileCdhItqf1qxSNHv8eNhiXETRCE0vPzaTfiLgeFwpTW5dmqpdHbavf5sGKTegRiOcgR6z1aY4-ksWOGqAXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22400" target="_blank">📅 00:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22399">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AL82k6PLSRJYx7YeX58jLfZUXC5fA0cmnwVPrbJovK1Ijla6G_wx4fxCIgQ8eWT5VCLqhCHAqRIwzWyEvXOXqI5Hsqh70dvSyiouCwGCCGASvoH0lH-lIf5YQghI5MbwaMdnk0WMg-AltvChrdCm7jWBH1_ywnEJGmE_Nvsiq4aTK5BtbhbD6rEhU4n8dptpQdjlI4wMPz49qP4MRZ9Qu9YuR-BRc0-Ufke32nCPQhRtnUjkHlmqgC-6eZljSEwbwhu_zQ5uhbGdIObUS7R6fZsSf-fzEla5-JEtCAAIK4enQV0W523coTxEaBfmZI21Q1abURsiFg7A2GUreJOfag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برای دومین فصل متوالی، کیلین امباپه فرانسوی بعنوان بهترین بازیکن فصل رئال مادرید معرفی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22399" target="_blank">📅 23:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22398">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOnK5fNVyr1sPcEQT0QuGPxrxI6gdAEfE7sbqFG6LTy_aWaLVN1QeR6KDnbxaARfD4JX1pcUAYaeQH-7PKqB2dsRRSbKQmiEhc_deMKlDZ6_2XSLolPldBg9l6P7CuT7r97ME34rhZMtGgOzH_ghiGh9qY5S0lDaDRN_dRsJfu6kLdasoRGvL8LOrjS-7_AJdG6jd0RDKM6aGMDh35OAH0lyGto8QY7-ScHWrKeB3T-_kSLBc6K_BGlJdwQbThYjilRCDRwvTgRIFfTq4e4ETFu-iJCproovBQf59Oz-DdS8Vpnk6RocsPOABAGqkeNQIej6DWpIEnUa989A8JrQew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی #فوری #اختصاصی_پرشیانا   دو باشگاه تراکتور تبریز و استقلال تهران از طریق ایجنت مونیر الحدادی به دنبال جذب حکیم زیاش هافبک تهاجمی و بازیساز سابق تیم چلسی هستند. دستمزد فعلی زیاش 750 هزار دلار در سال است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22398" target="_blank">📅 22:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22397">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=A2Hy9YTDr9bA8EE0ZXbSwlz6bMhPMV0bKDfOZ4cfmJb7HLdkcSxihdwZ-oV0b3SCLc7j4_sc3nAixJqNhLtIMdDGk3xV9GLY7ngFtU_CGT3Vf4HdcKJ3x2IfSVn9Yy_T2UwmzYZiBqDOxQvQWkA6zyI9wpczlBmS0v_MGJyFWioVQ6I2asiUM1O2n5k_sAAiGeHS6Nq2SnH9Yi9GPNLX84wptcEIoDyxAksIeZKJDotzH3pybe26JbehVGgu0xwtLPON_amliVyRKr4OUoP6mDzgmLm4jH26SsxWofwc1T51Ugu5niJg2Gy5PloMZWzcgJb_m9yq1Rt7A-trJpnpvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=A2Hy9YTDr9bA8EE0ZXbSwlz6bMhPMV0bKDfOZ4cfmJb7HLdkcSxihdwZ-oV0b3SCLc7j4_sc3nAixJqNhLtIMdDGk3xV9GLY7ngFtU_CGT3Vf4HdcKJ3x2IfSVn9Yy_T2UwmzYZiBqDOxQvQWkA6zyI9wpczlBmS0v_MGJyFWioVQ6I2asiUM1O2n5k_sAAiGeHS6Nq2SnH9Yi9GPNLX84wptcEIoDyxAksIeZKJDotzH3pybe26JbehVGgu0xwtLPON_amliVyRKr4OUoP6mDzgmLm4jH26SsxWofwc1T51Ugu5niJg2Gy5PloMZWzcgJb_m9yq1Rt7A-trJpnpvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نت بلاکس: این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22397" target="_blank">📅 21:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22396">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIoIXTA85XyindnnjwDF7cRAAMSkp-3Y8YHAzY7-Km23IH6aScRoN7r7xOQci8LHmw8QcX52nng3ATkuiN9G200mAfYPYhoPkPGVrOoZloqD8QEqd5DwAWwQGuFHE9m8F1dzDHQIePMRaG0X4oAFIDlZAQsnADEHsvPxFZjuJGqi3Mw7rbrnm7Po6ukKSNhUXbBl893Ae784-xwF33lPh86KOTAtFzHQpLMinlDY6fCFmLtRz2fv0WbX5t-wrQpdqgDv8a2zUJ6MRO80R10aw5esdLRKmAeRz8L6-A17YDqK3hIXAA7HU9IN_SHX5VCKVDQdRtSWSogmyhAOBRgsGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22396" target="_blank">📅 19:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22395">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7629a35090.mp4?token=ihbwJzbJKj_vl21ROKkhgSfp8bxEVojbDB9eYQBprFOTPOrA2ubQaEgN2Ek6MPYuPDdO1tUMpFXwOtKkh7K0LqsoYoh9knd2oZIam0WBOUWI6hdOPByIEC_5PCxj-nAgKfQLIsZL1wgpVTzCpLu_i863YIbBEq7qYALNHAQ-bG6r-lgp7m5Oxx3Hr92Bi_Tm3Pqq6UYJbJPh-Dr_mBvz9cSifX9iB8t2H9k41aUADGViH418YeBNcISyV4RtIbHYfexZGMXmpdW_4tZnUP_ERN3MMGPXusvjRl-53oMk_Fs95bZKnBrXmCBdmK4eWV9wtpfAoB9CANNFw79iGsHexg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7629a35090.mp4?token=ihbwJzbJKj_vl21ROKkhgSfp8bxEVojbDB9eYQBprFOTPOrA2ubQaEgN2Ek6MPYuPDdO1tUMpFXwOtKkh7K0LqsoYoh9knd2oZIam0WBOUWI6hdOPByIEC_5PCxj-nAgKfQLIsZL1wgpVTzCpLu_i863YIbBEq7qYALNHAQ-bG6r-lgp7m5Oxx3Hr92Bi_Tm3Pqq6UYJbJPh-Dr_mBvz9cSifX9iB8t2H9k41aUADGViH418YeBNcISyV4RtIbHYfexZGMXmpdW_4tZnUP_ERN3MMGPXusvjRl-53oMk_Fs95bZKnBrXmCBdmK4eWV9wtpfAoB9CANNFw79iGsHexg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیست کامل شبکه‌های رایگان پخش مسابقات جذاب جام جهانی؛ بنطرم از صداوسیما نبینید. اگه ماهواره دارید از یاهست این فرکانس هارو سرچ بزنید لذتش روببرید اگرم ندارید روز بازیا خودمون لینک پخش زنده میزاریم ولی واقعا از صداوسیما نگاه نکنید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22395" target="_blank">📅 18:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22394">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8d402777.mp4?token=fY-22HFq6eRNPAfmcKMSJBrMQmIAHC8FzYqrpmtV_S5GrNTyhBVSqSL21-wRB2Jql0JJtUiBuWe9g-eQo8wjN_nshO3ipHj30L9GlY86PEYmkFTpK06QjNYhys8vGSZ9BrNQEDxplIn6yEPKZXka0il-PgE_oQkDS35v0RtDf2HBw4kDKM4HfoOh_iw8fxe2EW82Rn9XmCKLxfNQKwjaglYkXSmFuZcEVTjbMa_EzR6gcv0FegVnM1F9cDK0vqy57zpZczQOpU57xmI_wgU976k9X5GePFpECSuJfLgPZGKc3DdCEOG2PKsX7e_alYq9p9fXCMq49Y5sOuUxsK-vETrSwTf5kCHvKnuu6ledI4i3KYOEuVZ5Ne6J_YcAhkRMRntulivIm0gYlE0PrMLRxTnm0R5o-r5Zn7Id3dr_fIZoODF1bsk58l7mBQPmrklxulV5JCKyjB6b9DKNLBPIlOVXt7yZply8NFYwmyp3Hv8Fz3onb7z2trOBX9sMkmaQbiR7Pqmc4u91BzEZqxgjuNigQCIdxCvliTeIBstyVuuiNxNHZC1XrY5wR93xysGPpzLcTmq7hEwRREmddYpihQ8ZsxJ-Gt_x5RNrTualh3O4UJiMhwXNw-18u6wKIPRpwDn8r6RZlnMMDNWiuPPEKjZg2fDVPJbEhY_X9BrvSso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8d402777.mp4?token=fY-22HFq6eRNPAfmcKMSJBrMQmIAHC8FzYqrpmtV_S5GrNTyhBVSqSL21-wRB2Jql0JJtUiBuWe9g-eQo8wjN_nshO3ipHj30L9GlY86PEYmkFTpK06QjNYhys8vGSZ9BrNQEDxplIn6yEPKZXka0il-PgE_oQkDS35v0RtDf2HBw4kDKM4HfoOh_iw8fxe2EW82Rn9XmCKLxfNQKwjaglYkXSmFuZcEVTjbMa_EzR6gcv0FegVnM1F9cDK0vqy57zpZczQOpU57xmI_wgU976k9X5GePFpECSuJfLgPZGKc3DdCEOG2PKsX7e_alYq9p9fXCMq49Y5sOuUxsK-vETrSwTf5kCHvKnuu6ledI4i3KYOEuVZ5Ne6J_YcAhkRMRntulivIm0gYlE0PrMLRxTnm0R5o-r5Zn7Id3dr_fIZoODF1bsk58l7mBQPmrklxulV5JCKyjB6b9DKNLBPIlOVXt7yZply8NFYwmyp3Hv8Fz3onb7z2trOBX9sMkmaQbiR7Pqmc4u91BzEZqxgjuNigQCIdxCvliTeIBstyVuuiNxNHZC1XrY5wR93xysGPpzLcTmq7hEwRREmddYpihQ8ZsxJ-Gt_x5RNrTualh3O4UJiMhwXNw-18u6wKIPRpwDn8r6RZlnMMDNWiuPPEKjZg2fDVPJbEhY_X9BrvSso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ببینید از تکنیک‌ناب نیمار جونیور؛ فقط ببینید چه بلایی سر بازیکنان حریف میاره‌. خدایی حیف شد همچین بازیکنی توپ طلا نگرفت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22394" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22393">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GA77N_roNEuWGhZcLfZibPOq5JfdQSWCLogcX1Z_wi1pttMhwVysDhjcXSUqofxMjLIhF01zilmceXUgxznrkkk7Jq9ZUUfihqd4KmCvPkuud16zUQr36gkiid0QyezGVz5weqVVXlXfdiVjWefDHM7K00VJz0jFaHO8KPnm4TrM_oKyyBLneXOb9KBMXd6oSTxm0XSRQ9kuwQGSMl0Em3wgiyzuSVwPtEgHg6ivZPi-x6GddkHD8PZfuI8JyxwiEw_h0BPWkayozRJuGbnqBVH0XV5RXH-wXe33khIBRnuRAf2LohmTKlSgbg8AK8EBri8ubfl-mIFvs_ZqsV21LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه چوروم اسپور برای جذب مامه تیام 150 هزار دلار به به باشگاه‌ایوپ‌اسپور پرداخت کرده بود و 750 هزاردلارهم به تیام برای 1.5 فصل؛ روی هم جذب این ستاره زیر یک میلیون دلار هزینه داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22393" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22391">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwH9t7X6YH0aGQg2FXCCpklOEuoEuy3vI-o1MzFEfXap2AS8xto-rduDdpm3H0RoW6sEV0XJHpXueBqvEzhSJxv-3EzmriWRsHOVQxyPhhQKxRA-_BfAUhNkB1rl6uqRIdeWxK7qpSf7Nec9TwuIdPAxvn8dksPFiKqkY7Rm1jTHWqc4iyyHh10VmOTUFyHrZXY7GBHZ5QqNsFwXMxewJGL9WdklbPldAgyP7aVHBp_xisGCj9H3AMo4T2G0vt7ACR1OAqWETh7_1PcmoH0lPfPcvXY4tQHGMSIKdgAJ4l-pHhlOKg8IQMptqz6oZdPQBGyIkn-Dx1JhrKyaNO8tVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛رسانه‌های‌فرانسوی: کیلیان امباپه، مایکل اولیسه رومتقاعدکرده تابافشار به سران بایرن مونیخ موافقت‌خود را باانتقال‌این ستاره 23 به رئال مادرید در پنجره نقل و انتقالات تابستاتی اعلام کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22391" target="_blank">📅 18:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22390">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWz1WJLa6247FBuvKyeZUVTJeKpgiv5N1Qka6OeVRPKhJf5qa0zOOw770HyBVNMdoL87ejmTSG3kdrpTJgnNaFvN_cXIaxAYjwPqJcqaaGnluPEKcNDtMGUnzh69Cih4Klml_656W-WeGomFO15uvtDZP6I6g86LPaeF4THiySZXqQfye5J4sZfOQguxwdJLo6PEc4dWYC8mr_1jsHGg_2LziTMDaZPLW9c_FFipJdfurQKWR0p7IiF3pbIB1bchUrxLlXNqyzXzLGAoCM4YdOPeXE-UltUERQBG_9NEfvwX9nivkIWq7Ctx_l4zCrVe-3xFHu6wg9LeQS4AuVyvvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس:
این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22390" target="_blank">📅 18:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22389">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dog-dM_Fzh257qoiLJW_FBmMOPmSRPGSFLjhWlfa_7eOl9ujntdKvJw76jxMzmxGrd7DC_q3n4BWsVa2CVqQSOeFQJOgYQI9XerVT7B619_Nc3OhJX6QHyceoJMvQyzc_JJ4YcGGGHK8hKRLE3B7hwrwZIXd84Dr7cVBiN5SPoZGiUS7AAez62X92tV510G-XXxrXaKUVxLwNDMFY3oR9MstXzr2UJOHUABmh6q2n2EzMMFymxzXFKKz4r8fl6dgrJnzfLYzCi1_wLtMjio6olTyUmKqLx-0OBhNdz1o-TQOWBhBk3IT0iZ-joHj90VeasgtHKvnqHTp1lq_Uz0EPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22389" target="_blank">📅 17:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22388">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsmRoRUdPmwQfZ6cTgOfOfdgTx3OaKP-hbc6cs2GZPNVo3L80ATWqhe4qDk76GOxq8pA9ilIgtcPU69vzzvoo18jLTb6oyPdFQcOyZR8NvkJKLsDptbkFTL0kTWCLQ4nM2nAUfh4Bq5pvPdH50-pAYlalbZIsg6KGsWlS_5Z_Yl9Lf-IVR11Fu7NvoPymfU5paNVKY4iRq9e4e4jhUkynZL84BbVF_XyQfBE6SI7t8CcGA0p_w33iN20f1velysRlwVddnL_aEhbWkcUaf6x6PLWUMSvrAY3n-68GWhwvT7iKnbAT9grlkgvvJscLphAMGqNjU7hEeSmkq95Mdd_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعدازجذب آنتونی گوردون؛ هدف بعدی سران تیم بارسلونا به خدمت گرفتن خولیان آلوارز آرژانتینیه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22388" target="_blank">📅 17:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22387">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSpKTnLGB6Q7jt5HQZoOhfcJma-9tJfuKKvyzVgtIcV8odQVXD-X2WYnvYVRs2UWBPLc10KCZfuRfaA4F9WYmuWI7hVdH8_a1g1VsFETaY8ga3lNAhNWoMgRhD-XuV_YjGiPPWTW6iRP9Tpa8dfEtiNP2-4aqhIVYfYxPVD9xxE1Q8GaETSOzA7xylAi2qnO74RPKaUIivY_3F8Qx1fsw1Y2OncpoF0q3WUcmyenAI6CCy8N7BsbtE38KEGwSEF7jnKrBIPLdQ93ej7Nx7J6pK4Z3reW2MDmhDJKT7GqXs2g9P-ub5zyHNmnlH5MnRGSvItACwvHZXAjcxO6x4T50g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22387" target="_blank">📅 17:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22386">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66baeb4dd4.mp4?token=D2t8TBbqC8WcHObphAzrPzAd9IV6HZ13Cd971pFr8DsF7qUHVUbvEiwY8R6RWRLs_Fvf7d-FM60TUu3HH1xrwRN8lpJI1ZbEQJoZBFBqSKOwSruBAObtyPg0Z5k0uTabP6b5vZQYGUdDOGlOFqOzwwH0x7l1iPZJZvC080eW-ft3CGohaRlAWRII2YBiq-egpvhDH6yrm7jjdXZaBgLSP6nUsB2rJUoy7M8s65HMBYg5tlYhZumBwh3BGAGulwGAcz8qKq0mBK7RtkuLWoUrGFbQXJZN1Cj39kEoRMnXUBaq_gCP67qxu6iQlQk6xjA34B4UBsg6Jvbo0Gb-49mlEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66baeb4dd4.mp4?token=D2t8TBbqC8WcHObphAzrPzAd9IV6HZ13Cd971pFr8DsF7qUHVUbvEiwY8R6RWRLs_Fvf7d-FM60TUu3HH1xrwRN8lpJI1ZbEQJoZBFBqSKOwSruBAObtyPg0Z5k0uTabP6b5vZQYGUdDOGlOFqOzwwH0x7l1iPZJZvC080eW-ft3CGohaRlAWRII2YBiq-egpvhDH6yrm7jjdXZaBgLSP6nUsB2rJUoy7M8s65HMBYg5tlYhZumBwh3BGAGulwGAcz8qKq0mBK7RtkuLWoUrGFbQXJZN1Cj39kEoRMnXUBaq_gCP67qxu6iQlQk6xjA34B4UBsg6Jvbo0Gb-49mlEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اگه‌چشتون‌خیلی‌ضعیفه‌هیچوقت عینک رو از رو چشاتون برندارید که نتیجش میشه همچین چیزی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22386" target="_blank">📅 16:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22385">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0eb9ae9a4.mp4?token=XvpII-DW4XXMkqLwbqNlmy4ufP9BlEvJDoS7ywTHr5ki6oaAnvfDFGMokzy6UFGUSMhAB6glS0msDm-GxVIVBIqKFPxSqysiYvOjrGLSpuvV7SrKDjSMPHfHlx9As3LVFQSExXdnJyILdndTU-8F2z2VveSbQTAZ_5cgzd44LQcMAc_UqhbMGq1RM3x3xtZGpF_FK3aLSrRTyoEhrdUIAM-f6DQKpZO65bFnTBw-E22Sm6y8CCLNmButeU7HZ9-JfajvyV3L_5Ohkqi-7sKQxA6OBxx9KvKnLeGd-0ccgNtI7iirIln17tVE51yV4mItQfFcbB51na7J6tH8x2HQZYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0eb9ae9a4.mp4?token=XvpII-DW4XXMkqLwbqNlmy4ufP9BlEvJDoS7ywTHr5ki6oaAnvfDFGMokzy6UFGUSMhAB6glS0msDm-GxVIVBIqKFPxSqysiYvOjrGLSpuvV7SrKDjSMPHfHlx9As3LVFQSExXdnJyILdndTU-8F2z2VveSbQTAZ_5cgzd44LQcMAc_UqhbMGq1RM3x3xtZGpF_FK3aLSrRTyoEhrdUIAM-f6DQKpZO65bFnTBw-E22Sm6y8CCLNmButeU7HZ9-JfajvyV3L_5Ohkqi-7sKQxA6OBxx9KvKnLeGd-0ccgNtI7iirIln17tVE51yV4mItQfFcbB51na7J6tH8x2HQZYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هایلایتی‌از عملکرداستثنایی آنتونی گوردون فوق ستاره جدید بارسلونا در فصل گذشته رقابت ها.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22385" target="_blank">📅 16:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22384">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bamc762C-hHSWSEYggVjDDBelG59kkLudAQMPT2anhf8tBaJGjhOhbGhva2ELN1L4sjbom57SE1lbhUnpSmM2Or2mY8BUGZh1s39IPTBKLdZBJCRJjii_V6tC8mOeS7xo6Ul23yLtrPlvGwqJhWvSyh_ES62zEdw7SQvy-3gQVvo67FtKfehqGMPVcWoXimgyYW1gP-P0X4NkpNZ9tRXPeqLg4W7x1o297GXhX8jxtfVRsObNPX-QYNFkwUeH8qXpUlwkZgtJQ_3pvOVn8gE1aMlDJPMCcxPIdhXUFnbzP1zzZS18_mJn1Q8xx2lJh_HSFCC-OLolnhwLxzppwbhAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست کامل شبکه‌های رایگان پخش مسابقات جذاب جام جهانی؛ بنطرم از صداوسیما نبینید. اگه ماهواره دارید از یاهست این فرکانس هارو سرچ بزنید لذتش روببرید اگرم ندارید روز بازیا خودمون لینک پخش زنده میزاریم ولی واقعا از صداوسیما نگاه نکنید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22384" target="_blank">📅 16:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22383">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoYaJFsc91ZOetVNAsi1yw3QaFvplhqK2ukPdz2Ysk1gwzFUbzDl-XuJDFtA-u1mFITgf0jESVchInbvceuX3mtUhhVObYVlmSooGpGatMELD6Rr7GinvfTkSSuXiSUgAOAj4fT6R3_wS96yExiqFIfQ8Ce_xHe8RFXXHe58g92DuuRPy8J19OURl04or8byyDPpCOpoegvFNkzyBUi_a6Mn65KJWofXy-pOxRlv_tLRrh7QG4iA7wCNbi6unPY0tFEUBsQZujDI6tjOxDbEAQEwYHdDLwHLV5USHQA0tnvNnxfID8V6xHwveYnY9wGggWeSs6kXPxpnFkvup-nBow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق شنیده‌های پرشیانا از مدیران باشگاه استقلال و طبق آخرین‌پیگیری‌های علی‌تاجرنیا مدیر عامل آبی‌ها پنجره نقل و انتقالاتی تیم در تابستان باز خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22383" target="_blank">📅 15:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22382">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uq52U1Xex7G7cZuvPjp7YQLiH85kyBUNrg5wkMtIz-SqFvvDJbcdSzMcXCTpPgCNJbQaLTDQqqQOPL5bxrllHs69gKRFaUPegFYwB0G0d3hr20d2NzqXSOxt1C3K11cDqnQw7JjnQYItxOEGtC0n0gBuFQKPguHlQXUFqvlucMQoYM5le0OrsRv5lFnlQ0OHSF-G23RKp_KPLgaLklWJfqWm8LpobctzZ578Pyv1-fDVH_Y6QZ9kMADOftCauhoaFfajufpjns6npDt3M1XYGWIj90uLAKxa60GzAUuay3ZlVB3d1sGyaULFVZjZMcKMfXNnQBhpZA9mBZUw9PhYYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که پیش‌تر گفتیم؛ اللهیار صیادمنش و علی قلی‌زاده درپایان‌ فصل قراردادشون با باشگاه‌هاشون به پایان میرسه و درصورت توافق با خودِبازیکن‌سرخابی‌ها میتونن درهمین پنجره با آن‌ها قرارداد امضاکنند و باعث‌میشه‌تیم‌هاشون با دریافتی مبلغی موافقتشون…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22382" target="_blank">📅 15:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22381">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZybB6Yewkwcn2yRmLBPq_xCAJg80tP5TmWBmG6UHde1LYNkOMB1A25j90m-9Z4kK02gtIFFeSSCCJ8xgo9gL_1CCn1oPxyrcsgfXUsSmRBNoaR45W8sfpXRTRM8f_3AhGvxVEnfpA3qFHO0LU5a6xjqUsW_A7aQCLOOPH0045sTo9rqXgQMv9hj2SGnRqrhrop8nI5VJ4Oc-teBSIZHdTduiZsqQsoSSHTu6RTu3dOswFQlhS6suTmT_8Jb2mNrRzOzGoGsZp718ZWonQ5vjEI075l-L6TeBmL451t8rNEiuWD_nd0Sd-FCPcPvR5A0D7Ewjv_tfgbu_7BKrbleQ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جلال‌الدین ماشاریپوف کاپیتان 31 ساله تیم ملی ازبکستان در گفتگو با رسانه‌های ازبکستانی اعلام کرد که با تیم استقلال قرارداد داره و در این تیم میمونه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22381" target="_blank">📅 13:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22380">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">▶️
#تقویم
؛ 15 سال قبل در چنین روزی
؛ بارسلونا با پیروزی مقابل منچستر یونایتد در فینال لیگ قهرمانان اروپا برای چهارمین‌بار قهرمان این مسابقات شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22380" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22379">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUgnVo3vN5lMUZP88GsM3Z1X65CcntC26uPwER4hZup5Rau2VLir1BRVcMFRta-v1MTIGjYaV38Xz2pic5EnQ68TD8mhQwETjqbOgY3mUGNRflUsnEi4lraz13iJqaQBPFu091fDS1oamnT4OV7JR1hXlpz8OlYaHPsEk7l2DcWM1y6chVwVKsAgy4Iofj71Rjl3FfDhyDCFK3XiJG1U4lQqQ17hYTfl1LY33bFErisS1-zqNTwx9Q5BVdEhZI39oyIQCCZdxe6rjmkxVztUBD7FkfvBoHBL-wXzdlEzEJd2hMxmMWz02ClxBbh2a6Hmo4OpdFdLuuH4zKBPpYOgCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ محمد امین‌ حزباوی 25 میلیارد تومان از باشگاه فولادمبارکه سپاهان طلب داره که از طریق ایجنت او اعلام‌کرده حاضره در قبال دریافت رضایت نامه‌اش ازطلایی‌پوشان اصفهانی طلبش رو ببخشد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22379" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22377">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=mycjuTcPjMkI7qpi-nNiHncDdM0XdVxU_glE8vemqCo9uKy3ZGPyLnYp1KGY-_7GELDBr76AUAJ2tQrLtkl4_32LmWJgzCXL-sb3QvlzJJYzJK6x3lPXjgo_E9RhvkbngFaBrFLMmlei8PgBdSvQ5uupq_cJFqyqhB6Z1jS4-AgjcG6x_x88vCmUcK1FFM_3Ok7J7feNMxUzhOipwRWBBGqZDv3ehybjgfYm6ubZmOZqjiJKIXAyyEVEqN9628Wqfws9yFYlNM90pRs7sKslx83GwIZAofpQqCwBgRekosLcyeYfo-LMKaufrdpSS48g396eC5vyu7oG-UIA5CAPPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=mycjuTcPjMkI7qpi-nNiHncDdM0XdVxU_glE8vemqCo9uKy3ZGPyLnYp1KGY-_7GELDBr76AUAJ2tQrLtkl4_32LmWJgzCXL-sb3QvlzJJYzJK6x3lPXjgo_E9RhvkbngFaBrFLMmlei8PgBdSvQ5uupq_cJFqyqhB6Z1jS4-AgjcG6x_x88vCmUcK1FFM_3Ok7J7feNMxUzhOipwRWBBGqZDv3ehybjgfYm6ubZmOZqjiJKIXAyyEVEqN9628Wqfws9yFYlNM90pRs7sKslx83GwIZAofpQqCwBgRekosLcyeYfo-LMKaufrdpSS48g396eC5vyu7oG-UIA5CAPPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
نروژ ویدیویی از لحظات پایانی رقابت علیرضا فیروز جا، استاد بزرگ ایرانی‌ تبار شطرنج فرانسه با حریف هندی را منتشر کرده. به گفته فدراسیون شطرنج نروژ، پس از تساوی دو حریف در رقابت کلاسیک، فیروزجا با تکنیک آخر‌الزمانی و با چند حرکت حریف صاحب‌نام هندی را شکست داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22377" target="_blank">📅 11:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22376">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYTye_DI0WaLIWrL4aVmqR0EPxd48Rbytj2GjMQF246zDWrwAgoabMGnpjV8BsV0QIgSoYIxDkZKXoofI6aexgQyKC0zeUtwVqbIBrlIasG9brD-PMbriaHBsaeYQETjDvGD0129esigmdV0gg_S3JD3byqRClBadSCUm2KdCN_nrV184uTKYTvg8heavbe3ct-PCi3vAYYyAg1nQ8IpB5uMJRjVARoItO81734DufbrcCHbGr2NcVFFE_L69hX8lfZOqmhRkOCJPuXfcf1iADLaSXw0l4bBsIpOplDlQg1tdDpqdJs2sLF6VlKHFeo5uvmfYE7mjh9dUsH0KEHUTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار فعلی مهاجمان خط‌حمله بارسلونا که ممکن است آلوارز نیز به این فهرست اضافه شود
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22376" target="_blank">📅 11:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22375">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZyHtoyOauHDBMNRxwH-79jMktc4Nl6PmB-brcg08o1jDZ8zXBbTMO5xihBCG9OqLN4u13t_M0TpDzcL5LavNk-uYGfxOkDl5qb7oJCp1tWoup8mrMKUM3xT9FxxxrZWw5gn-GVQjxannjjFDi29pzR4FnWEkgrnCmxZuIejkGS2GYPimpX3ofdGF55oIBTGNe7CTl00pivem2V2TAoqFKqaItmvM1AguxTYXoSpUPFUl5PvIGOtvgZqwuPj2i_N0vBAGzdEDD0kjD7JNouCYNyvbQpsOlX8aAjHnl4PviStgbCB34-_SP4Gatd2icxKoSiGj77XBGWeMq7lkFPTcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپانسرهای پیراهن تیم‌های حاضر در جام‌جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22375" target="_blank">📅 10:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22374">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1-sw72AZk1Rf8UrrPa1qFw5SPZxNdQ5Hyj4BaDySOWs_gLoIfeNf33ZtwhAg7Xg1fS-VdBeMdQVRDbDU_T6jZnESsqRni3fy2VarxFHY5Y_OwBlUF-d4lbE4fFqzRqu1ADQY1jNfvGb3Do6bOTBVbDMlKS03ePgcqNz74yDAID6GghOOMqi-2KP4NG2K8F7K2YGS95mIw8nB9cItVF7DJBk14f7i7LSq8R_VNDwj_5HELxzDAUL1lUvXWs1Jy82wE-qNBh_bCF7JDkmVmh1Yi6rZT58FUEUErwbXU2Hef8P2BDH_D1LWk_4pqcHoPCaoP3uYUsQWve08lTb6ss2og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ کاسمیرو هافبک برزیلی تیم مچستر یونایتد، آخرین بازی خودش با پیراهن این باشگاه را انجام داد و پس‌از بازی‌از هواداران خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22374" target="_blank">📅 09:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22373">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/re_1zNPcHbYADHfAg7NoWZMh7qWIn_NXYOxiVrUVqmJWx8N1RBQPGd3Po5f2QXkuFyfPxghv9PN71yF12MPSAAaMSQR9M0j7oCzth5j9rt9HTPFiWR1AkT09eVboyFVI3FVAt6RCMv8PrSG-FTUUH0Ot2Tzr1IBok8UdGNJWLfcWSPfDBEK2PxNRXUuyeJNFbLyVVXK9Ks0Z_g7tuB0mumpdZETH3WBPR_O8-A36O-hof4h4GZcxg0_I_dF8Xdqdbl9ZTBECjoUhadiSSFmcY1ACE8k5LnwwUVqV9YSpw-KfppgHe2fpOLqRrygeTuK2lrPz1R-8r8fiArAx20Msjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کافو تنهابازیکن‌تاریخ‌فوتباله‌که‌ توانسته 3 دوره به فینال جام‌جهانی دست‌یابد. حالا لیونل‌مسی و امباپه این فرصت را دارند که در کنار کافو تاریخ‌ساز شوند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22373" target="_blank">📅 08:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22372">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=kaFYZh_7mFlk4QUnIAV1MbZUvOYCAm54z178DXa5aQ7O6-ypIWcWegrRHCuBtxfDD9J9_vLT11aXAFklwx1LbzXuo4TGJPtlLkJjEyPVVteonxUI0LgyJJQJBViQCL898IarrfKrT2-p8PSPu26501RBegOFV8J3cvul5HJnl3-QogV7L-QEyKUhP1Pg0QLr3MkN0hZXq3whJy3iIDXPPDfGOn8SA0aDgP_hvfqO2jSWLBJsFwNvBbmC3naOf1cic-_846ykEMdKoU8UsWqiL3jpeiFrK_y9BbuXpWGHodOJG8m7Bb436gTl-x_5XeMbvVvL8UU_IQFBrQ7zn76q3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=kaFYZh_7mFlk4QUnIAV1MbZUvOYCAm54z178DXa5aQ7O6-ypIWcWegrRHCuBtxfDD9J9_vLT11aXAFklwx1LbzXuo4TGJPtlLkJjEyPVVteonxUI0LgyJJQJBViQCL898IarrfKrT2-p8PSPu26501RBegOFV8J3cvul5HJnl3-QogV7L-QEyKUhP1Pg0QLr3MkN0hZXq3whJy3iIDXPPDfGOn8SA0aDgP_hvfqO2jSWLBJsFwNvBbmC3naOf1cic-_846ykEMdKoU8UsWqiL3jpeiFrK_y9BbuXpWGHodOJG8m7Bb436gTl-x_5XeMbvVvL8UU_IQFBrQ7zn76q3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های طعنه دار ابوطالب حسینی به وصل شدن اینترنت برخی از کابران بعد از حدود 90 روز. خیلیا هنوز نتونستن وصل شن. از 70 هزار نفری که همیشه پستارو میدیدن 30 هزارتا آنلاین شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22372" target="_blank">📅 08:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22370">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uM9q0JSrMfhdxTyKgmZULwgZS6DGKnzb8_ODvNawx2wwa0G9DpO0SizyZm1nCOvMBt2rS3U1W-o4fXS5IZIF54U1WEVvzVAe5bedBwP3W9u4fdCwT0YQWCidN0HJdTsw0cy6ogIQEMDlm0jO3cSkC4-6JVTQbhfAwi0gc9l2ASP_iWH5XChtmXV7e204W28CzFWilY7cWsKDsDecc9RE9G8PygP4Jyno7pga-Wo0_g9V6XBs3etTKln_MVv7JCI2HcJa9i_OuTsyxI-STaFbMqeed1VVQArpn-mxiERF05umHcZ-duAln_U_dfuKk5wYnFGE1CYWaoCGCB3ut7EK3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
نبرد یاران‌صلاح با روسیه در بازی‌های دوستانه ملی پیش‌ از جام‌جهانی 2026
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22370" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22369">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvJ8o76keBKPtZiW0fS8j4DNyAIN4LaIU396FPZY3gFhcXOWpN3YdNmSR4GmmW7qL6ZWPO1rQirIPMhrGm8LdnDxV-429FYUsnHlbceSw4GE04qn5jE3rSow9dDZ_5oOtdS_5rt5Jd4-7kV9ko2OihbnGEP2rMWvQRNTgphDdaWnslUf_il_IRfqEYKG79jHCHViXllg6U2gUwx3QndXWaQxIqlTm-nQq29_M797XHSUorys_j1RqJ7MV4EGJ3ZQt5_ZRXLufyshJwWXitVLcU2ZHYfxik3d0d6qUqhI5VGqr20EokN00hv589Ce2yz5vj4xEzAF8U8xHkdyAIJrWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه تنها دیدار دیروز؛
قهرمانی شاگردان الیور گلاسنر در لیگ کنفرانس اروپا با تک گل ماتتا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22369" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22368">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUyfm5miyBEnLvChsp4mxXd_cGZ4Ta4W6OW5cd3Y6x0mU9KugwtSxEfL87U0-xieWeYv6ZzZSo_QvId22tYHlaqN1Q0ytMPKpYQCrxzg453cVs5vBFL_DysvAhKLi23eX0jCVeL7Bg2fJg5Sry4e91tn0QxyG8vggA6yVpoI9xFWRVdpPGHCkJGdtdxW0Dg8Aofqmnm2vZlXLv_SfvWMUKkcV6dvGureHGaZ2J1X55KAZsFT8Hh2jYPygz4XtpuXG5s9e88UBaE_iJ6n8DeOCB0J9_frAD0hAPEVcjsKlbkX3yfzNb__Wi2R-A9d0KaFk4Ic76T65iRYvt8uFDDwlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
اوستون اورونوف ستاره‌ازبکستانی و تکنیکی تیم پرسپولیس درگفتگوبارسانه‌های ازبکستانی اعلام کرد که در باشگاه پرسپولیس تهران خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22368" target="_blank">📅 00:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22367">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=fVDZeF0ZM3HULC0dnJa6S9auCJ4Em9T1OvmS5zsyobvX635AKzZXrrmPbdY7zI-uG3Mp1V_Y5bSfzZbB48_Qduyv2SgSXJob4_LVNK6qBCHEISkcauNQv6o4KQt1vdMwAKxeMKNybXoxy-VhGalzJS5gOAZN8SmyNV7RZkuigDhZaVi1N26x0JTb5k1FGoRUrDIYPmXI-CRSlQ4-JD_zJyv7Kt9yS_8DLYArNiLPgU39oi6OdmssHAMCgQq_OSPSXR3eJE-7gSrZjwnQW-yZ9XoFiPNWl8Lf95t_KlgGjCet6Fayne4_dgYdonMUDzM7NnRnm4MZW-xy3ilbou6icg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=fVDZeF0ZM3HULC0dnJa6S9auCJ4Em9T1OvmS5zsyobvX635AKzZXrrmPbdY7zI-uG3Mp1V_Y5bSfzZbB48_Qduyv2SgSXJob4_LVNK6qBCHEISkcauNQv6o4KQt1vdMwAKxeMKNybXoxy-VhGalzJS5gOAZN8SmyNV7RZkuigDhZaVi1N26x0JTb5k1FGoRUrDIYPmXI-CRSlQ4-JD_zJyv7Kt9yS_8DLYArNiLPgU39oi6OdmssHAMCgQq_OSPSXR3eJE-7gSrZjwnQW-yZ9XoFiPNWl8Lf95t_KlgGjCet6Fayne4_dgYdonMUDzM7NnRnm4MZW-xy3ilbou6icg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تعدادی‌از فوق ستاره‌هایی که جام جهانی 2026 آمریکا آخرین‌جام‌جهانی‌خواهدبود که در آن بوده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22367" target="_blank">📅 00:40 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

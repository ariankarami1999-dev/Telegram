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
<img src="https://cdn4.telesco.pe/file/osdWt1GLC7NyW_x5VFgBwooyo6rUnF4bJBGE1lSt8yaqkk6BKtJolol1lI9i1kG7WeTmX8XWljmYa-KpL3jSyaNLhhuh5CmDIFMJwOHf-gD_A2r0ZprT7MEiRCGtX6KVubnCivqRF4xpLOI0nFBtVVu5F7_1NYAf36t1E14Xed-7-uyyTD9CLVtFjwHYMnOMgU3vqi3nPutrGcxPpcoKAffnIzn2Lu93C_kyJiu6ro5bNQm6J0n1rCF9guBQOQrHYE1XHxWJI4UdMCnm2jLnP8-X2b_vEORvuaVG06XtwoOPWdYW10UAXRf923PCYBK6M-EftC36TwPbqKerLh7Rjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 338K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 14:39:20</div>
<hr>

<div class="tg-post" id="msg-16629">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d3acaa8f.mp4?token=jKn1qspfKlQV9SPg6HabDCepb2lnBJPyiYA6W9fQ_cvOwC5U25vi99pB2yDxNKcgSmASYq2uPlLKMzJMZtphCba3NO_UaUAfysiomBbfn5cEl32CFyxfI68N04ZnlayQo-RHP6Maxt9uXpFBgta4hHqx_cdC-KT2NnaTxKbwahnK_V3JR6azXF3Vc1pYSWf72Cmd3u95B8fCCBSYMvGfzy83XBTqrLiDntrWxZY4-EQ7WjARB_6XbH1Iv6ZGClRjvcFjzagT3FlujPTqSSHiTsPyIy7lbtX7xnt8S_0cn6lguWt1bK-VLuf-NOZN0Fg17w1YOxDOFTUzGR27iHIafRirPbCVKW3R0Dg3EuoIpaXLIRBKWP3rOw1c1q8yOe2LO9eZ_KMmxumBkRbIXaEOnxSQesHNZ2MKN8z5dqFH69_tE21Uzr-Mn1KBxBnWHFDhRXNia8pg9_nJOcvTiDeyJQEvb_aASzkeoN5bx-ZD0D-NAT3cZgM3IoC3JU90VzLATvRvnFutaa2mCNOj1FM1DGvzWjqFNBwHMxSyfSH6apR8aC1-QqQo-hFTj9GOI2blu3eG_pI5y8BmwRIIVeQDSSdk0R50kwt8Vvv5yy9pPHGzLA3xQ9yye9qzg5eLTGgTStGQ-JXMln5hc7xlrBN9SfHVQqwcV8zakcH_kfB3OTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d3acaa8f.mp4?token=jKn1qspfKlQV9SPg6HabDCepb2lnBJPyiYA6W9fQ_cvOwC5U25vi99pB2yDxNKcgSmASYq2uPlLKMzJMZtphCba3NO_UaUAfysiomBbfn5cEl32CFyxfI68N04ZnlayQo-RHP6Maxt9uXpFBgta4hHqx_cdC-KT2NnaTxKbwahnK_V3JR6azXF3Vc1pYSWf72Cmd3u95B8fCCBSYMvGfzy83XBTqrLiDntrWxZY4-EQ7WjARB_6XbH1Iv6ZGClRjvcFjzagT3FlujPTqSSHiTsPyIy7lbtX7xnt8S_0cn6lguWt1bK-VLuf-NOZN0Fg17w1YOxDOFTUzGR27iHIafRirPbCVKW3R0Dg3EuoIpaXLIRBKWP3rOw1c1q8yOe2LO9eZ_KMmxumBkRbIXaEOnxSQesHNZ2MKN8z5dqFH69_tE21Uzr-Mn1KBxBnWHFDhRXNia8pg9_nJOcvTiDeyJQEvb_aASzkeoN5bx-ZD0D-NAT3cZgM3IoC3JU90VzLATvRvnFutaa2mCNOj1FM1DGvzWjqFNBwHMxSyfSH6apR8aC1-QqQo-hFTj9GOI2blu3eG_pI5y8BmwRIIVeQDSSdk0R50kwt8Vvv5yy9pPHGzLA3xQ9yye9qzg5eLTGgTStGQ-JXMln5hc7xlrBN9SfHVQqwcV8zakcH_kfB3OTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ همکنون در آنکارا به زمین نشست
@withyashar</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/withyashar/16629" target="_blank">📅 14:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16628">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رئیس‌جمهور آمریکا برای شرکت در اجلاس سران ناتو، وارد پایتخت ترکیه آنکارا شد
@withyashar</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/withyashar/16628" target="_blank">📅 14:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16627">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZ7ifgJwnfVggHDzuGrwCtfTBIRHRseHYALbntKxnGDxdjfpti0YqA6ZH6gMzteZjls7haUnJ___PKyglNM3Z9kug88f1bWP21LA8O6CXifaeTA7nxK1u5bF3En6sjrETOBuGXNaQydouTaz-zxQHVJAPlybol6HJKcFAYmaEf9E67Gnsbt4Jyo8oj_dhZRTq6OjxpuZbVKq4CahdE4zlX2y58fIIyTVmKwMMMK6T6ZwWor-TJyM_e5oCZNjjk0V7lDbuvmlTTQw0YfIgXVzrsYWxyhyd6d7OnRChLl_9zoEPGskgpRqjWDziU3S3X_LHULPRFfIyleyD_oEVXAkzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با هواپیمای ایرفورس وان جدید هم اکنون در حال ورود به آسمان استانبول است و حدود چهل دقیقه دیگر در فرودگاه آنکارا به زمین مینشیند.
@withyashar</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/withyashar/16627" target="_blank">📅 13:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16626">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">منابع امنیت دریایی: یک نفتکش نفت خام با پرچم عربستان سعودی در نزدیکی تنگه هرمز در نزدیکی عمان آسیب دید، پس از آنکه یک نفتکش LNG در همان منطقه مورد اصابت قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/withyashar/16626" target="_blank">📅 13:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16625">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfVLnW7NAwiGyT79VHbsUTxo_iUfVUG-T19k13EW6Iz4U0eBY2aIM9n-cKOCf6cMESGRY3f7aKE_F-BQAzi7jUfzmEjwhRyQUCNNB_vr0XqezeRLefX9LXAB8i3JtwzmkKe49xL30B-NVA31p04QRPbkXd_MEs3q6qmNuZq6ROQlD1upzDkM8SzohFHxRDegENXQ4SVjLQ4R4kNiOeHsqLt38qbySIbiyQeQKrLICGvMWobUsC56pP-SqPJzBUzYN6k5S-532Fv-La5yYkdd2n_p7E0YoocEFz55aDHkJ62Z9wP6CQXq5M_RBE5izYrm0m3BBkX6pRaR6wOveOZqsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدونم چرا هر وقت این کامیون عجیب و ماجرای تابوتهای یخچالدار را میبینیم ، یاد فیلم «سرباز جهانی» محصول سال ۱۹۹۲ می افتم که داستان دو سرباز آمریکایی را روایت می‌کند که در جنگ ویتنام کشته می‌شوند، اما اجسادشان در قالب یک پروژه فوق‌محرمانه ارتش بازسازی شده و به سربازانی با توانایی‌های فرا انسانی تبدیل می‌شوند. این نیروها با یک کامیون بسیار پیشرفته و مجهز جابه‌جا می‌شوند که درون آن محفظه‌های سرمایشی یخی ویژه قرار دارد و سربازان هنگام نداشتن مأموریت در آن‌ها به حالت ریکاوری نگهداری می‌شوند چون گرما ضعف این پروژه بود.
امیدوارم موشتبی خامنه ای‌ رو هیچوقت نبینیم و زنده نشه
😂
@withyashar</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/withyashar/16625" target="_blank">📅 13:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16623">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7801177f00.mp4?token=o2Mm8k3tbLEtRW2wsM0bnQihkectOsfUhrUuC2TOjBe6QiGzlhbglgi0SYbDmX70Wc0AL_veIKqlnSQLWq_cSIZzzm61m_y_xNlaXWZ9lfa_3oiA-e8dT-OVa7wNbLQg5siqI86IQxxX8e2QSDcZGNNk4nlw7jA5gCp7y-GZkpTKO6sAI843ppuFpEmN_2-Uz4bMn108jVU0TZqIP7EJ1TTM2Y21CgNhZZXNM9a3K08RMNP__oWt8AyCkq5OkUMAK9_2Hb0R21A2I_I98UoKuPa-5-5D4pSLd4fTZsNBYrALeMP5kGqdJhnSNzyZm5ZA7I2Tpq2RTGbPTFarsAgUpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7801177f00.mp4?token=o2Mm8k3tbLEtRW2wsM0bnQihkectOsfUhrUuC2TOjBe6QiGzlhbglgi0SYbDmX70Wc0AL_veIKqlnSQLWq_cSIZzzm61m_y_xNlaXWZ9lfa_3oiA-e8dT-OVa7wNbLQg5siqI86IQxxX8e2QSDcZGNNk4nlw7jA5gCp7y-GZkpTKO6sAI843ppuFpEmN_2-Uz4bMn108jVU0TZqIP7EJ1TTM2Y21CgNhZZXNM9a3K08RMNP__oWt8AyCkq5OkUMAK9_2Hb0R21A2I_I98UoKuPa-5-5D4pSLd4fTZsNBYrALeMP5kGqdJhnSNzyZm5ZA7I2Tpq2RTGbPTFarsAgUpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارشات بالاخره تپه علی الطاهر در جنوب لبنان توسط ارتش اسرائیل فتح شد
@withyashar</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/withyashar/16623" target="_blank">📅 12:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16622">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0122a2f81d.mp4?token=NHeMmQ9Ytv5kKTYRdRQ_OLvPLNhJlfI_3lYUypLGsR0UUL-ntkklOTy5yFSdOkhL_HVt_69DheuVxJwt9cLzPxJz70EYxAt0vwueTC6t30MhZjm3Gqsfp7QtKRKAKlMwlGltsplHPV8Tw0OQFPT90FWt9CFEIowM87QZ65zNv56eGFnAigElbSkJyymGJtQQIR27Nik-HXgDvgJogeXfslhbs-uipJJ0b6TO26mMqx_S2RPuaIhN5EM0Vi6TXefRxNWQyrxZQCDaJgSrnkndVf5zCSTklxyklsVo6NspAzgwSKIbWo_av7gLKgyJL5et74PA0m9-HcFthunK5KhquQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0122a2f81d.mp4?token=NHeMmQ9Ytv5kKTYRdRQ_OLvPLNhJlfI_3lYUypLGsR0UUL-ntkklOTy5yFSdOkhL_HVt_69DheuVxJwt9cLzPxJz70EYxAt0vwueTC6t30MhZjm3Gqsfp7QtKRKAKlMwlGltsplHPV8Tw0OQFPT90FWt9CFEIowM87QZ65zNv56eGFnAigElbSkJyymGJtQQIR27Nik-HXgDvgJogeXfslhbs-uipJJ0b6TO26mMqx_S2RPuaIhN5EM0Vi6TXefRxNWQyrxZQCDaJgSrnkndVf5zCSTklxyklsVo6NspAzgwSKIbWo_av7gLKgyJL5et74PA0m9-HcFthunK5KhquQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم مثل تهران دیدن جمعیت کمه
در مسیر فیلم خورش خوب نیست کامیون ضریحی جنازه ها رو از وسط راه اصلی خارج کردن و از یه مسیر فرعی بردن
@withyashar</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/withyashar/16622" target="_blank">📅 12:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16621">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مقام ارشد آمریکایی به آکسیوس:
ایالات متحده با حملاتی علیه اهداف ایرانی،انتقام حمله به نفتکش ها در تنگه هرمز را خواهد گرفت
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/withyashar/16621" target="_blank">📅 12:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16620">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a7de57d9.mp4?token=fE2AN4K-764v2P0ZZBIIzNREcD4-eUk_az_0cr-NGFSU2uaDGDfYTLNUobrBjjcUbkokBGW8Zrz0AX34m97rQ6ahBR2YB8mtR7DcPqCgf6l4s2NOrNBtO9lgME-Ftpw5QfmD6J88qNrvhN75oMAz88aN0L7TA-Fdids4bo_7pXdSM79mrcgB6EHaWEhIN87dl1LcVAGkoEdMOf7eYoFig61KtVltPmpL3hRt5nV1T5I6CbcB0m3OAVTZREFqIpYMwmeRG4TZN7wH2pE-nkE2rKDJi838I7zMe4w5BYnBGX1Po4Pt8JftjzqQbmwRtE8kRb7yNmLSDpTJJSUuyh_vbgx2WoVrNQrPVJCNNQjt0CemiOsqWEWwZWAjRTyKkiZO63MXkGI88--iAbKNm9UED3xO-7ys6x3QD-adxU2H4apaOu_xPRkpJZQ-pbvuENXv6G4rp8xjwDeqyHHSUs1XsXXRA5lo_cxycAwZLY1qbVxqXqHQlkoGtUJBjJakB_UnmU32zEJWU2yk-yMzdQgeh9AXYKH0DDiMxawrIsGZTHa7VYZB_DH5qY8_-pyxT1TM1W9flUz6sZMfcGYko21s9DT833fKlobeNq3CbCLU5yeQujCnSO2L3HSBUG6wqrZvXJVW_96zCIz0aIDp_sQ53f59ws0xAO-vEu0629QFBvI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a7de57d9.mp4?token=fE2AN4K-764v2P0ZZBIIzNREcD4-eUk_az_0cr-NGFSU2uaDGDfYTLNUobrBjjcUbkokBGW8Zrz0AX34m97rQ6ahBR2YB8mtR7DcPqCgf6l4s2NOrNBtO9lgME-Ftpw5QfmD6J88qNrvhN75oMAz88aN0L7TA-Fdids4bo_7pXdSM79mrcgB6EHaWEhIN87dl1LcVAGkoEdMOf7eYoFig61KtVltPmpL3hRt5nV1T5I6CbcB0m3OAVTZREFqIpYMwmeRG4TZN7wH2pE-nkE2rKDJi838I7zMe4w5BYnBGX1Po4Pt8JftjzqQbmwRtE8kRb7yNmLSDpTJJSUuyh_vbgx2WoVrNQrPVJCNNQjt0CemiOsqWEWwZWAjRTyKkiZO63MXkGI88--iAbKNm9UED3xO-7ys6x3QD-adxU2H4apaOu_xPRkpJZQ-pbvuENXv6G4rp8xjwDeqyHHSUs1XsXXRA5lo_cxycAwZLY1qbVxqXqHQlkoGtUJBjJakB_UnmU32zEJWU2yk-yMzdQgeh9AXYKH0DDiMxawrIsGZTHa7VYZB_DH5qY8_-pyxT1TM1W9flUz6sZMfcGYko21s9DT833fKlobeNq3CbCLU5yeQujCnSO2L3HSBUG6wqrZvXJVW_96zCIz0aIDp_sQ53f59ws0xAO-vEu0629QFBvI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس شبکه ۱۴ اسرائیل، درباره مجتبی خامنه‌ای : اون هنوز زنده‌ست
- از مخفیگاهش بیرون نمیاد و می‌ترسه، اما تو دورِ بعدی درگیری‌، یه بمب اسرائیلی به سراغش میاد
@withyashar</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/withyashar/16620" target="_blank">📅 12:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16619">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">جنازه خامنه ای برای همیشه تهران را ترک و برای شروع تور ‌کنسرت ها کمی پیش به قم رسید @withyashar</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/16619" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16618">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">به ادعای رسانه ها دولت مصر با یک تصمیم سیاسی، تمام برنامه‌های سالگرد درگذشت محمدرضا شاه پهلوی شاهنشاه فقید ایران را که همه ساله در مسجد الرفاعی برگزار می‌شد لغو کرده است.
‏همچنین گزارش شد که از سوی مقام‌های مصری به وزارت خارجه این کشور ابلاغ شده اجازه ورود چهره سرشناس مخالف حکومت ایران به قاهره داده نشود.
@withyashar</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/withyashar/16618" target="_blank">📅 11:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16617">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ: کنگره باید بودجه ۳۵۰ میلیارد دلاری دفاعی را تصویب کند
@withyashar</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/withyashar/16617" target="_blank">📅 11:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16616">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">شبکه الخدث عربستان سعودی گزارش می‌دهد که رئیس‌جمهور ماکرون، ربع ساعت قبل از وقوع انفجار، هتلی را که در دمشق اقامت داشت، ترک کرده است.
در سوریه‌ نیز گزارش شده است که رئیس‌جمهور احمد الشرع، دقایقی پیش از رئیس‌جمهور ماکرون در کاخ ریاست‌جمهوری در دمشق استقبال کرد.
@withyashar</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/withyashar/16616" target="_blank">📅 11:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16615">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4093af6c8.mp4?token=h3cYolUcr2Tbjp6IpKSfwb1iUzZOvRB_uRYXMtqkFe9Hgkh-5eFvI5zRND-1IkUWq-ZRjpPUmzmfNPbbmJLCpSRVyJux9KSnUK2_qczidlQVHl7diKV1RqNRYpfDjFqa59XA-2Sv_zUcArfwoPCM183xj9b7D1JsYFbx4vKlDJsdufGO0iAHzoUfbzbFf-ygQzb1c1qID6I9ZaLYdbJ64tXvAMXDlzUMxYiUWr1FyC2-P9VhIgpG_dHv-A5smqYatpL5SUWu5yBQQV3-mqo9oT6Vrw9i7-cDOokL0F_zVIvzucYq8Dd91Y5M_m4V8ucQkj5aRAc-yEO2NKoFQKZT6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4093af6c8.mp4?token=h3cYolUcr2Tbjp6IpKSfwb1iUzZOvRB_uRYXMtqkFe9Hgkh-5eFvI5zRND-1IkUWq-ZRjpPUmzmfNPbbmJLCpSRVyJux9KSnUK2_qczidlQVHl7diKV1RqNRYpfDjFqa59XA-2Sv_zUcArfwoPCM183xj9b7D1JsYFbx4vKlDJsdufGO0iAHzoUfbzbFf-ygQzb1c1qID6I9ZaLYdbJ64tXvAMXDlzUMxYiUWr1FyC2-P9VhIgpG_dHv-A5smqYatpL5SUWu5yBQQV3-mqo9oT6Vrw9i7-cDOokL0F_zVIvzucYq8Dd91Y5M_m4V8ucQkj5aRAc-yEO2NKoFQKZT6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تصاویر ماهواره‌ای رویترز از تهران در بهترین ارزیابی حدود چند صد هزار نفر را نشان میدهد
@withyashar</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/16615" target="_blank">📅 11:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16614">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd6db78ff3.mp4?token=LkU70ypk24I5dGRNROX-Y3668KJiJlfgYjxQbm2lqj0m1rcE6wTDjsvR1TZO3wKRtLgJWE8hNfgj_VoVNVHC4JemmY3eOjfqmz8IPytU2Tkv-ZQT4tZZZIw2zinNXQm_KcaMNrOINqTTRJvU9BxjEP9HdCgHrArlsQJvN0YTUy6cmbkOjKbvcSg2QP-kawPGvut_Jr81jiOrpaeNXadxxMmnsSBzsqwbiovCSORVwWgMpesww40Nf-r0XkjoRwbhCR4-rypClYfh1FmDmH4jKcRIaaVywixtY_FpvG6SnZu32edLkDvaKDvkf4wh8gzWztn5s3H-u2KrE_Tbqh5ZMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd6db78ff3.mp4?token=LkU70ypk24I5dGRNROX-Y3668KJiJlfgYjxQbm2lqj0m1rcE6wTDjsvR1TZO3wKRtLgJWE8hNfgj_VoVNVHC4JemmY3eOjfqmz8IPytU2Tkv-ZQT4tZZZIw2zinNXQm_KcaMNrOINqTTRJvU9BxjEP9HdCgHrArlsQJvN0YTUy6cmbkOjKbvcSg2QP-kawPGvut_Jr81jiOrpaeNXadxxMmnsSBzsqwbiovCSORVwWgMpesww40Nf-r0XkjoRwbhCR4-rypClYfh1FmDmH4jKcRIaaVywixtY_FpvG6SnZu32edLkDvaKDvkf4wh8gzWztn5s3H-u2KrE_Tbqh5ZMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند انفجار در دمشق، در نزدیکی هتلی که رئیس‌جمهور فرانسه، ماکرون، در آن اقامت دارد.
@withyashar</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/withyashar/16614" target="_blank">📅 11:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16613">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یک منبع امنیتی ارشد لبنانی امروز به روزنامه "ال-جوماهوریه" لبنان گفت:
"ما در صحنه، هیچ اقدامی از سوی اسرائیل ندیدیم که نشان‌دهنده عقب‌نشینی از مناطق مشخص شده در توافق‌نامه باشد. برعکس، شاهد تشدید عمدی تنش‌ها هستیم."
@withyashar</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/withyashar/16613" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16612">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رویترز به نقل از یک منبع امنیتی: انفجاری با استفاده از تعدادی مواد منفجره در نزدیکی هتلی که ماکرون در آن اقامت دارد، در دمشق رخ داد.
@withyashar</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/16612" target="_blank">📅 11:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16611">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">صداوسیما : نفتکش هدف‌گرفته‌شده در تنگه هرمز پس از نادیده گرفتن هشدارهای مکرر مورد اصابت قرار گرفته است
@withyashar</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/withyashar/16611" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16610">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a464e4c27.mp4?token=IjRupySFkfV_gddBm9hsyQrXZ0XHDmx1usUC1NbWJOw4Yq_8MjEReq0uY2qZhPZFQthI_SOeVbTTVkpEedTKir7eKVrDtftvZfelkDUnfPGvq8FayfTubz8Kl68UmzxP-LjFu6gzlMDpzgaQZ49pJOsDsgdhahfCi6tGoDw3dG0sQoWukfW9n0HKOgc9lHUAIbHluyotBGRPIAXO9-OscCcqS79MAeUCOEjG-m6oEcNhduWerkaxgdmW1YFGUFdGwBUflg5xN7EOg3tgGBh7qW0T9dc_MSE_xMoGrR8MMD73jOLwMHf7_wzGfk7hqC87WXcUc0wystNtHjqq3m_HuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a464e4c27.mp4?token=IjRupySFkfV_gddBm9hsyQrXZ0XHDmx1usUC1NbWJOw4Yq_8MjEReq0uY2qZhPZFQthI_SOeVbTTVkpEedTKir7eKVrDtftvZfelkDUnfPGvq8FayfTubz8Kl68UmzxP-LjFu6gzlMDpzgaQZ49pJOsDsgdhahfCi6tGoDw3dG0sQoWukfW9n0HKOgc9lHUAIbHluyotBGRPIAXO9-OscCcqS79MAeUCOEjG-m6oEcNhduWerkaxgdmW1YFGUFdGwBUflg5xN7EOg3tgGBh7qW0T9dc_MSE_xMoGrR8MMD73jOLwMHf7_wzGfk7hqC87WXcUc0wystNtHjqq3m_HuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره ای از ۶ ژوئیه دیروز ، چند هزار نفر را نشان می‌دهد که در نزدیکی برج آزادی در تهران، ایران، برای مراسم تشییع، جمع شده‌اند که کاملا برخلاف ادعا های میلیونی رژیم است
@withyashar</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/16610" target="_blank">📅 10:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16609">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IN3m7ICGIsYpIddRTA2xNyw-bbHsM1twKEyGpQNh5bBuXCe4djNA-p317rxqoGnWTm2iXSy9P_PzUbaiQGGyupzO8nyK6_zUJLWCpnOv33GjvxohuZSTvXCKaM4dfL-VpN5sk1NsxOgDbhkT4v7ZPO-tMsVHxl469MqzUCr1USK4zFpBON8gie-tpfFJ4W5AaQDj7V0TsByB-YkL8G5biQ75BlnkNJhNnB1niI3mE4WP8CKgnSdAQ5acPJXnD9pCcnMDJl9-X4XL1OkKQX2aKu8b47GUQrcEibMWUnpXGpo-7-9FSwZgL3rdjhbjgzAM5AxkILkECMmyGtcUZV6KIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدل ایست نیوز : تصاویر ماهواره‌ای نشان می‌دهد ناو هواپیمابر امریکایی «آبراهام لینکلن» از دریای عمان خارج شده و در دریای عرب مستقر شده است
@withyashar</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/16609" target="_blank">📅 10:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16608">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kB7GtZtQ7gV2uuFzx8a-JytthMDbpAGtclfZtfJWGIy3tTi5fgWCw20SFYmebTBADpKX_XMun_OxHolXDqLZbnsgOX8FNdrIjLh4sfxJRogIxIPumfdSdZkx2ArHo-AN5l4ofYWzkulfMU6AsBy8QKtUXcKY55w7wdnTE9lDVo87M1CW7gXk3p_83LCBGMZEmgGwnslIHSXn0lTbXbE5mEmxTXWWbSUUkOXTZBFYS4jgNJE_utRAB7ZC0z47Qdl8OlvGaDqAdal5EehyiJFizwvQAhxYaQSSxsvIj7OKJ_a7Gq-xeHhgoc_-Jp4wkd7EkpUm_Y_2L6UL5KLlI5p8dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز: انتظار می‌رود ترامپ به اردوغان اطلاع دهد که مایل به فروش جنگنده‌های اف-۳۵ به ترکیه است، اگرچه هنوز مشخص نیست چنین معامله‌ای چه زمانی یا چگونه انجام خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/16608" target="_blank">📅 10:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16607">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">عراقچی به ترامپ: به امضای خود پایبند باشید
تا زمانی که تهدید‌ها علیه ایران ادامه داشته باشد، مذاکرات برای دستیابی به توافق نهایی آغاز نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/16607" target="_blank">📅 09:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16606">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یک منبع امنیتی اسرائیلی به وب‌سایت والا گفت:
حماس هیچ قصدی برای خلع سلاح شدن، تسلیم کردن سلاح‌های خود، یا تخریب تونل‌ها ندارد.
استعفای دولت حماس یک اقدام نمادین است که با هدف نشان دادن تغییر به واشنگتن و شورای صلح انجام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/withyashar/16606" target="_blank">📅 09:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16605">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آکسیوس به نقل از یک مقام آمریکایی: سپاه پاسداران دست‌کم دو موشک به سمت کشتی‌های تجاری که در حال عبور از تنگه هرمز بودند، شلیک کرد.
@withyashar</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/withyashar/16605" target="_blank">📅 09:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16604">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTWHSiItylAfhanwHch8it4yaJZ7xRwr1IQKt9jhu4Qwury5nNTQI8vtxn5mTvklhN8fwSe_65zFXNys0eQagcyLlidvovB9DNcsDMvateWaaaZkHta0g2oYTNnIA8Bu4ONw00SwmT4_kuU5h_yWVMkrVfu6kXiJcy2-EI5WMLe9lJqYTc7qGKgtA5pb8IW8w1lz3dHnYu4hg6Vd3u6ALGnnfXgdBqssQhiSNmFN_83A0SKhu6lo9kMcabzG5Z-gfEQ0rdSwac1oF1cirUsW0iOYuoGkzlyOjU71fDgOASD9zDWnKZMhv4cnL34rv-ulMM0pv0DR2d2VzF_awmHc4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک نفتکش در تنگه هرمز هدف حمله قرار گرفته است
مرکز عملیات تجاری دریایی بریتانیا: یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است
گفته شده نفتکش مذکور حامل گاز صادراتی قطر بوده است
@withyashar</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/withyashar/16604" target="_blank">📅 09:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16603">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd75af4e28.mp4?token=BguXC3BvyVmGH50YCg2xkEoJvHOrX7ocJLHaO2JXxOdWOVIxXYbqI-sQW_PFSVH87axDWRIYPv5EIfdaAJTxKGLRwASmT9be_l5r4iV5n09ceBR5gru_ZY0jJSMv9E5e-OYS1b1zcP5gcBpAKYdko02evZLt_3g9kJixSWw6wIJrwp0ZgwrTuMeAQt-Yix84b1Te3xzR64Mwj3YPQaSztuNN1dp76xRD47B0K4CmS8whPH7tTMU6x6fZU7HwCNnw9oENxRcq_uzV1l-lAZ3urUJ28LNJfjTOiKhTTTXeMrws8DDBe-e9KMsOYaUcrFCyCkmkGxgsbJh-vofLqXtkzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd75af4e28.mp4?token=BguXC3BvyVmGH50YCg2xkEoJvHOrX7ocJLHaO2JXxOdWOVIxXYbqI-sQW_PFSVH87axDWRIYPv5EIfdaAJTxKGLRwASmT9be_l5r4iV5n09ceBR5gru_ZY0jJSMv9E5e-OYS1b1zcP5gcBpAKYdko02evZLt_3g9kJixSWw6wIJrwp0ZgwrTuMeAQt-Yix84b1Te3xzR64Mwj3YPQaSztuNN1dp76xRD47B0K4CmS8whPH7tTMU6x6fZU7HwCNnw9oENxRcq_uzV1l-lAZ3urUJ28LNJfjTOiKhTTTXeMrws8DDBe-e9KMsOYaUcrFCyCkmkGxgsbJh-vofLqXtkzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوایی که ما تنفس میکنیم سیاسی هستش !
@withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/16603" target="_blank">📅 02:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16602">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd4aa6711.mp4?token=anLyq1cqxsBOOwSTmQ5LFVqInnim43coJB3AoVZEywDFgJw38XA1cAmrszd94GyICN0lG1nSh9kU2z9Tqj0UBdnYvydnykELsRJmOnQ6YuC6d1dhAOCLGV1L7YKfyyeuRUSXxT9IVfkBQw8wZFZS3D1rZW3VYNPa0ZNEng7yTT6A0DLlJfvQ0I2gU6glGZpDi_ASec9Vre0wXmf5-1YDuzKmnYApAtxnhwSn-FU0WNY_K73tWyKDHuwVZ8MEEHxlO-BH2WcbOE7oNo_O1cvAgu4q-uAWohjbjrgYP3OoCKZ4xzMYaBi2rfcWI8KpCCSrM6kOxELvegGm9rjp0BsBBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd4aa6711.mp4?token=anLyq1cqxsBOOwSTmQ5LFVqInnim43coJB3AoVZEywDFgJw38XA1cAmrszd94GyICN0lG1nSh9kU2z9Tqj0UBdnYvydnykELsRJmOnQ6YuC6d1dhAOCLGV1L7YKfyyeuRUSXxT9IVfkBQw8wZFZS3D1rZW3VYNPa0ZNEng7yTT6A0DLlJfvQ0I2gU6glGZpDi_ASec9Vre0wXmf5-1YDuzKmnYApAtxnhwSn-FU0WNY_K73tWyKDHuwVZ8MEEHxlO-BH2WcbOE7oNo_O1cvAgu4q-uAWohjbjrgYP3OoCKZ4xzMYaBi2rfcWI8KpCCSrM6kOxELvegGm9rjp0BsBBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک پمپئو، وزیر خارجه آمریکا در دوره اول ترامپ: حکومت ایران عمداً چهارم جولای (روز استقلال آمریکا) را برای مراسم تشییع جنازه انتخاب کرد تا نفرت خود را از هر آنچه آمریکا نماینده آن است نشان دهد.
@withyashar</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/16602" target="_blank">📅 01:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16601">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDNVcoHcnzyCFw4e4eytzPPncgycHWpYwLBXsBZSH8RYh-sFbnATMKK7oOQBYY2XXszdNDdq5nli3RjpbdKhn-REWpiV1lYnVclIh7ADtCLUSfxwK2GLEiYQzm6NWd7vPKJZK_5MulrNBHH9KiU5tJ7GTLcZYN92KZd-sRMFFIo_B-sKw0MtB1SPE4S9QQo47xrVXA3WMN-dw51caOwTsBryxSXuHgXQGD2Rw1-T7SpH13tadfN7JffzivH2l7C893H5VOzYRswM7zTkTzIARBPiqxuLcRExG1ynujdlo21sBVtqKzI8ySOajn0HJgEsUQ6M-mPEqXaVm1RA6kEqvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر هوایی از گشت زنی امروز گروهی از قایق های تندروی نیروی دریایی سپاه در تنگه هرمز
این شناورها در دو گروه مجزا به حرکت درآمده‌اند؛ اقدامی که توجه و دقت برخی رسانه های خارجی را به خود جلب کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/16601" target="_blank">📅 01:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16600">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وزیر امور خارجه آلمان:
ایران باید تمام هزینه عملیات‌های بین‌المللی برای پاک‌سازی تنگه‌هرمز از مین‌های دریایی را پرداخت کند
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/16600" target="_blank">📅 01:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16599">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c696b52038.mp4?token=Kg7_W9hIjqlGYATWyHS7_DPhd5x_cU5ZBXIaKReFjEufWJg6M5LIkH97PqqSYZ9PKDYNvgYYDA50Atib5fNsBZagMAtO5fXGB6VET31GUtbLvTBxUMIFgsnq1rfoJwfyW98g_VoIZY08KlnvNwDWVYtKV9WmvC8zRerFjWdAUr4p4dQtAa1IBchGGFaYWw4A66BdNu7VyyIXa2aBWuepsOJOnPuhF4LNxOD1pFfpV_UPULw5CEEDUq-8G1jhl8UwzUbgXSlRwR_nzugNdfu7ah0kCeQtI06ttH2FucNjRCF3kXNyWQ-1TYPVsOlUpzSi_FpK-mqptGAXKHc_G7u9_ldLk23xozue226t0OImGPWZclq8dVA9nUmz_AWM3ZtcztHGD4ICFO0mej3sx3xAUgaKOD005j6d-YaqslYFiBxgE-CdtvcqVvijTsCQKj_br9gd5uhHiNRTCy5xMECNTzu26-kvaagt1zkySv0YvbLP7i16Gt-vdvFlypR7bThYNlXGimFu9-h4sXtDMImf67IE4O08594QJQETkNo2qAqW8GSwpWRuFC_0t2umAraMm1VVkRDzhL5_OV42HK3HXvsVhiVX_MCCueDEyvrOJhn8XIsAjonnP0UvLElvYMPE_07qWoKj8I0X7EJEfng-X_CEIP5MKDsusqOvb8GHfD4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c696b52038.mp4?token=Kg7_W9hIjqlGYATWyHS7_DPhd5x_cU5ZBXIaKReFjEufWJg6M5LIkH97PqqSYZ9PKDYNvgYYDA50Atib5fNsBZagMAtO5fXGB6VET31GUtbLvTBxUMIFgsnq1rfoJwfyW98g_VoIZY08KlnvNwDWVYtKV9WmvC8zRerFjWdAUr4p4dQtAa1IBchGGFaYWw4A66BdNu7VyyIXa2aBWuepsOJOnPuhF4LNxOD1pFfpV_UPULw5CEEDUq-8G1jhl8UwzUbgXSlRwR_nzugNdfu7ah0kCeQtI06ttH2FucNjRCF3kXNyWQ-1TYPVsOlUpzSi_FpK-mqptGAXKHc_G7u9_ldLk23xozue226t0OImGPWZclq8dVA9nUmz_AWM3ZtcztHGD4ICFO0mej3sx3xAUgaKOD005j6d-YaqslYFiBxgE-CdtvcqVvijTsCQKj_br9gd5uhHiNRTCy5xMECNTzu26-kvaagt1zkySv0YvbLP7i16Gt-vdvFlypR7bThYNlXGimFu9-h4sXtDMImf67IE4O08594QJQETkNo2qAqW8GSwpWRuFC_0t2umAraMm1VVkRDzhL5_OV42HK3HXvsVhiVX_MCCueDEyvrOJhn8XIsAjonnP0UvLElvYMPE_07qWoKj8I0X7EJEfng-X_CEIP5MKDsusqOvb8GHfD4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رونالدو لوئیز نازاریو دلیما</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/16599" target="_blank">📅 00:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16598">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">طرفدار کدوم اسطوره ای شما اقا یاشار؟؟؟</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/16598" target="_blank">📅 00:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16597">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from~‌🇭🇦‌‌🇦🇳‌~,</strong></div>
<div class="tg-text">طرفدار کدوم اسطوره ای شما اقا یاشار؟؟؟</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/16597" target="_blank">📅 00:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16596">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نانا کوآکو بونسام، جادوگر مشهور غنایی : کیپ‌ورد آرژانتین رو حذف میکنه، من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود! @withyashar</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/16596" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16595">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Up-Fq7812k6gyJifo6kWmAQdMraZaNEAdAc0DXDhL3m2t8nUnu4VJ538H61hsCWzeI7uOKaD90UK01ivUI98RK-pnX-E6jcHSou9YXmh8VsdR1kGApPVROqL3JXz4QMIcB1fjKzb2nAHGPbzvAQMYhVHz91xJarxRNcgYhmSRxXk9ZewrGJarN7AbNUWmC146WGZ73u-rolQkawunBm_mbk_pN6zovK3B6NUO-gFpYQ2oO4_sXM_DjEdngDtJxo2bQzCzfEGezDbDrJfpR-HCUIs1jhtEy2h4Ke0TBlqiZ_kXgpbPPjsMQpnpYxL8fhcgt7Zmku1hymrvDQiO0e_Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرهنگ پاسدار صفدر سلطانی جانشین سپاه پاوه در مسیر بازگشت از مراسم تشییع توسط یک خودروی ناشناس منحرف و دچار سانحه تصادف گردید و کشته شد
@withyashar
🚨
🚨
🚨
🚨
سربازان گمنام حضرت موسی بد فرمون دادن</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/16595" target="_blank">📅 00:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16594">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آکسیوس : نتانیاهو در تماس تلفنی با ترامپ؛
- خواسته که به اردوغان «تذکر جدی بده» یا «جلوی رفتارش رو بگیره»
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/16594" target="_blank">📅 00:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16593">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">شاهزاده رضا پهلوی : ‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی هایم، تصویری نادرست و گمراه‌کننده ارائه کرده است. @withyashar</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/16593" target="_blank">📅 00:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16592">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">استان هایی که تاکنون سه شنبه ١۶ تیر را تعطیل اعلام کرده‌اند:
استان تهران
استان قم
استان سمنان
استان خوزستان
استان مازندران
استان اصفهان(شهرستان های آران و بیدگل و کاشان)
استان یزد
استان مرکزی
استان بوشهر
استان لرستان
استان هرمزگان
@withyashar</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/16592" target="_blank">📅 23:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16590">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دیوید کیس مشاور نتانیاهو:
بمباران مراسم ؟
شوخی میکنید؟
صدها مامور موساد توی اون مراسمه!
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/16590" target="_blank">📅 22:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16589">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21b93d61ac.mp4?token=IWyWkvx5O7NAZwDfyN7Wcn6MBwDe1sEr7yPW44yHtGSRfs1btOTtk-u4qW_nR13LIFDI-8A4UW0xhsRthJpoSJQ8IXPnQry7xKBj-rKJegkn4f5nlDCAi68kb3A1HzNxzFDNoFPiVGFxji2mRCAeQQ8wR2-cVAziHFd21XLhgFk67NRhdfOArdzuU7I8dPgini_vg8ijEfYqNl-Wv40fku9OYQ5yd512sR8V9ZmCGvmbWqStrY-pMKcJLFapK16ixv14c9v2R6gLgTzA0d2adfvmGNZ3-swcj4uGXF9e3pyCdSzSrzh5VeY6mxsBtoNfvDnvlExCZiVvStAR8SgWDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21b93d61ac.mp4?token=IWyWkvx5O7NAZwDfyN7Wcn6MBwDe1sEr7yPW44yHtGSRfs1btOTtk-u4qW_nR13LIFDI-8A4UW0xhsRthJpoSJQ8IXPnQry7xKBj-rKJegkn4f5nlDCAi68kb3A1HzNxzFDNoFPiVGFxji2mRCAeQQ8wR2-cVAziHFd21XLhgFk67NRhdfOArdzuU7I8dPgini_vg8ijEfYqNl-Wv40fku9OYQ5yd512sR8V9ZmCGvmbWqStrY-pMKcJLFapK16ixv14c9v2R6gLgTzA0d2adfvmGNZ3-swcj4uGXF9e3pyCdSzSrzh5VeY6mxsBtoNfvDnvlExCZiVvStAR8SgWDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش هایی از حمله و درگیری بسیجی ها با قالیباف در میدان آزادی  @withyashar</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/16589" target="_blank">📅 22:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16588">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">برخی رسانه های رژیم از حضور جمعیت ۱۵ الی ۲۰ میلیونی در مراسم تشییع صحبت میکنن ولی اگه مراسم حج امسال در عربستان که فقط ۱ میلیون ۷۰۰ هزار نفر توش شرکت کرده بودن رو نگاه کنیم میبینم جمعیت چند میلیونی خیلی خیلی بیشتر تر از چیزیه که فکر میکنیم. @withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/16588" target="_blank">📅 21:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16587">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36f95eb134.mp4?token=S7G6KcQLGCCJCh3MyUhOxq4u65TWf1_1tUv4tONCbOykYgaklOPMkFxf3HKfUH-FqdK-V5zlEzn5zMd55M_W73xzf1T6pfZ4Kj4fanw3KD9OQFMS-2F9FOusYdlCuVpZaUTIX6pykN8cJZ10gBl4tYNISv2K2Ja_C2_3PuHs7dimkl7WjCZgMqa0_RqxIAp97yPtUWTkGVuvrtjoggxjfBCwlLNHLqmAkT3PZVVlihCfIb22fMwq44_viKs4JoRLgwOs0jeMDqcZr_6hKECXWrnFKnJiK_0_XTQi_yyrH6KaDgUrlq0_NdBPy_IhHgFo04w2l6KzuMm_N3lgUQ6MYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36f95eb134.mp4?token=S7G6KcQLGCCJCh3MyUhOxq4u65TWf1_1tUv4tONCbOykYgaklOPMkFxf3HKfUH-FqdK-V5zlEzn5zMd55M_W73xzf1T6pfZ4Kj4fanw3KD9OQFMS-2F9FOusYdlCuVpZaUTIX6pykN8cJZ10gBl4tYNISv2K2Ja_C2_3PuHs7dimkl7WjCZgMqa0_RqxIAp97yPtUWTkGVuvrtjoggxjfBCwlLNHLqmAkT3PZVVlihCfIb22fMwq44_viKs4JoRLgwOs0jeMDqcZr_6hKECXWrnFKnJiK_0_XTQi_yyrH6KaDgUrlq0_NdBPy_IhHgFo04w2l6KzuMm_N3lgUQ6MYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکرون با عینک آفتابی معروفش که ترامپ مسخرش میکنه وارد سوریه شد
@withyashar</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/16587" target="_blank">📅 21:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16586">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رئیس‌جمهور فرانسه پس از ۱۸ سال وارد سوریه شد
یک منبع ریاست‌جمهوری فرانسه اعلام کرد که سفر رئیس‌جمهور این کشور به دمشق با هدف از سرگیری همکاری‌های اقتصادی و تجاری با سوریه انجام می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/16586" target="_blank">📅 20:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16585">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a3ca4796.mp4?token=lGW1ZniRVT5tVJVXbnwlEoHL4DgHBXnSoQA4NDeWxT_p-XkoYyfcKbe1dUItkYMtVCojMpMj2HDbuB3rA7D_WwE_zdhOaBJjccxPdLaLf-LBht_B-RyzIqCGGF3XN-1p6EVM3GXrLEgsN7-op9tNoaOrMFEORdTaFKKd8lFLlbfw59bWE2p0dAXmPoHacGJh9KV37jG_YBdhqq2t0lgWU2ZsPrSBqbiE0HzSj2Sz3F_75O42hxmpiFux8yMmWz_hsRvmVCessRwpbWvCBUgYjzPEmji-cj4YzMX8TU32Dx5bz7_xJ2-oV1-gq6r678DEBpAc1Gogho54AtQwhrrOqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a3ca4796.mp4?token=lGW1ZniRVT5tVJVXbnwlEoHL4DgHBXnSoQA4NDeWxT_p-XkoYyfcKbe1dUItkYMtVCojMpMj2HDbuB3rA7D_WwE_zdhOaBJjccxPdLaLf-LBht_B-RyzIqCGGF3XN-1p6EVM3GXrLEgsN7-op9tNoaOrMFEORdTaFKKd8lFLlbfw59bWE2p0dAXmPoHacGJh9KV37jG_YBdhqq2t0lgWU2ZsPrSBqbiE0HzSj2Sz3F_75O42hxmpiFux8yMmWz_hsRvmVCessRwpbWvCBUgYjzPEmji-cj4YzMX8TU32Dx5bz7_xJ2-oV1-gq6r678DEBpAc1Gogho54AtQwhrrOqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنازه خامنه ای برای همیشه تهران را ترک و برای شروع تور ‌کنسرت ها کمی پیش به قم رسید
@withyashar</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/16585" target="_blank">📅 20:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16584">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34927b66b.mp4?token=lfSKNQqUmD11BvQUw6DLJEA0VI5fHdQS6ypNP51v38ng1YyFRQAOtDad7wJXsHQ4pnm_ys5LG4Z1L_YafYCZC7YnZwNc24bfYE0JzVDM8E9vhmi7DIrdKCDKgMPff2L7uHL-sABDHMUKSaCKNWNP15s5IK_vLFdx3YMMFXKJpm36tD-SZPY50aTmIDaZSmxBg6TDrC1VQWKGuvmXNcWpSw7Q7u4l0_jV5qqcd6Gd3gErBbr8-p-z3Kv_zEZRKxyQ7GWx8xoRu-EVsnZe5GQ-RjNB7q8QeOT-3KH-d7TDA4CGE5dhUjehnhxR00VZSdParS9g1pYU2ybhnlmPlB7Nwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34927b66b.mp4?token=lfSKNQqUmD11BvQUw6DLJEA0VI5fHdQS6ypNP51v38ng1YyFRQAOtDad7wJXsHQ4pnm_ys5LG4Z1L_YafYCZC7YnZwNc24bfYE0JzVDM8E9vhmi7DIrdKCDKgMPff2L7uHL-sABDHMUKSaCKNWNP15s5IK_vLFdx3YMMFXKJpm36tD-SZPY50aTmIDaZSmxBg6TDrC1VQWKGuvmXNcWpSw7Q7u4l0_jV5qqcd6Gd3gErBbr8-p-z3Kv_zEZRKxyQ7GWx8xoRu-EVsnZe5GQ-RjNB7q8QeOT-3KH-d7TDA4CGE5dhUjehnhxR00VZSdParS9g1pYU2ybhnlmPlB7Nwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این نسل چی میخواد از جون ما ؟
اومده تخم مرغ آبپزشو بگیره…
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/16584" target="_blank">📅 20:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16583">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8667c144e.mp4?token=qWPGzXijIEG2TSxn4XcDHv5rfbqE2BoYuLZN6AqUnia_ZP74GwcA7-yotbBemcIueJCSKwMVjoq6fvn7Iwi-Rvj5n3l4U5tXLqSeVZmm8vnJkz32J2_bruOS-FPiOrCXM4IAg45HPppV62Ma4q16foqzkIbNgK9W5sByOn3Out_ea9MhFXSJeQm-h9Nz3pWsyoxOOx3BxRNEynT8w4j1bkPuJKGMDVmpg2JBWYc4a5M2ZFeocrEqFgRaxRamc34IMdSFFQjqTXhtVmUMCAf7XJJbXMBy1I5JKHo6E9oNCifw2pUS0E0SqMZfz5JfB0__VcIlH-5s_tFStc77XHFgFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8667c144e.mp4?token=qWPGzXijIEG2TSxn4XcDHv5rfbqE2BoYuLZN6AqUnia_ZP74GwcA7-yotbBemcIueJCSKwMVjoq6fvn7Iwi-Rvj5n3l4U5tXLqSeVZmm8vnJkz32J2_bruOS-FPiOrCXM4IAg45HPppV62Ma4q16foqzkIbNgK9W5sByOn3Out_ea9MhFXSJeQm-h9Nz3pWsyoxOOx3BxRNEynT8w4j1bkPuJKGMDVmpg2JBWYc4a5M2ZFeocrEqFgRaxRamc34IMdSFFQjqTXhtVmUMCAf7XJJbXMBy1I5JKHo6E9oNCifw2pUS0E0SqMZfz5JfB0__VcIlH-5s_tFStc77XHFgFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش هایی از حمله و درگیری بسیجی ها با قالیباف در میدان آزادی  @withyashar</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/16583" target="_blank">📅 19:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16582">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiOBNdlHcj2u7by0c4i4-lxjxQ63elvO7pHn28CxBpMxmkSdBgm70TGz9Fl9yWgWHr7xr6wzhBTtuezc94YEZ5WkDFHJXW4bnr5xogobq8Em1sYHqL9JVFeLLtTljoxu1iarqdS712jB9FVNWXsX4UM4jIqWM_FQ8GIBMl6L4jg9kZHPeCsXNGDkEWctlfAbZasGa9atOUPtsyddS5a570zWXU-b6AuaenMOsiNIPOtoOHQR82x8sDJeltZZeelVtqm4-z4HKEaZ_pKA7Zxnw4oLgJcjhEel9qfwOlExMSb4jcC00gi96D0yE932DCfKuer5lw7iXjdthyGwz1uZSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهام شرکت دل پس از اظهارنظر دونالد ترامپ مبنی بر اینکه «بروید و یک کامپیوتر دل بخرید» ۸.۳ درصد افزایش یافت
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/16582" target="_blank">📅 19:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16581">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ : ما از ایران امتیازاتی گرفتیم و آنها باید به آنها پایبند باشند و ما همچنین اورانیوم غنی‌شده با خلوص بالای ایران را دریافت خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/16581" target="_blank">📅 18:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16580">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2ae96c363.mp4?token=cmmPNKE5I2zG8nc56EnY60tWVZc36fezl1KT7qzG4yZx_MutWlD32sy57PcmYm161QaOiVSWffQcGB7LsP2a44DN091NflZoBWc-C1J3v0k1VnNcKCqJOFRe6iS_mNm_RanUF0lsVnkKOnP7DayEB2UNJ0J7239WirLqyIlTlLAhlnhk3F98NL1da_WsuDOyaTGoUnR38_W3m8HmoBPDPt457nSxgJ9BZvCORaS9OT2E6Gatkj-sutVKEzcIi6_tne0r48qkPyVrtyo-sTNNXRI4Cec7Kp7MBWxC3aZSwSzZNYL5YSeUaz_XyoIQGtzGf3CH0Bq5ycyf5Qn7iSb1lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2ae96c363.mp4?token=cmmPNKE5I2zG8nc56EnY60tWVZc36fezl1KT7qzG4yZx_MutWlD32sy57PcmYm161QaOiVSWffQcGB7LsP2a44DN091NflZoBWc-C1J3v0k1VnNcKCqJOFRe6iS_mNm_RanUF0lsVnkKOnP7DayEB2UNJ0J7239WirLqyIlTlLAhlnhk3F98NL1da_WsuDOyaTGoUnR38_W3m8HmoBPDPt457nSxgJ9BZvCORaS9OT2E6Gatkj-sutVKEzcIi6_tne0r48qkPyVrtyo-sTNNXRI4Cec7Kp7MBWxC3aZSwSzZNYL5YSeUaz_XyoIQGtzGf3CH0Bq5ycyf5Qn7iSb1lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بررسی ترافیک کشتی‌های تجاری از طریق تنگه هرمز طی ۲۴ ساعت گذشته که از طریق مرین ترافیک قابل مشاهده است، نشان می‌دهد که اکثریت قریب به اتفاق کشتی‌ها همچنان از طریق طرح جداسازی ترافیک (شمالی) ایران عبور می‌کنند و تنها تعداد کمی از آنها کریدور جنوبی تحت حمایت ایالات متحده از طریق آب‌های عمان را انتخاب می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/16580" target="_blank">📅 18:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16579">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39cbbf8bec.mp4?token=L0-jp0NcQOu_5AQ-49UNtekpl6eWdBr6J0bjD9VKzvZPQEex6Lct-XnMoOt4H_R0vTkgdJ1pp7ia8CL83Aivl02mBIwnZyJVLuXQvT6ztjktSeWZWO7mAAYy8PdeJUL8y_nrRPVB4JPNasP0x242m7putGZ4ATMzuGJrpQT915C6B3QtRXHQ5sCGUZvXULRNSwcvB2oTiWNoqT2uLBdSju_4dm3fY8m8niFelzSIhLMc6AFOav2oCFm6782PGKG5oE8Q04xzt_oZL8zfHQYgBkptdisxnPR0mywaU49Ul9Cnl7AYGQbprJWR59LnjPRrGi252DQoFmzMsj4UPEGIZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39cbbf8bec.mp4?token=L0-jp0NcQOu_5AQ-49UNtekpl6eWdBr6J0bjD9VKzvZPQEex6Lct-XnMoOt4H_R0vTkgdJ1pp7ia8CL83Aivl02mBIwnZyJVLuXQvT6ztjktSeWZWO7mAAYy8PdeJUL8y_nrRPVB4JPNasP0x242m7putGZ4ATMzuGJrpQT915C6B3QtRXHQ5sCGUZvXULRNSwcvB2oTiWNoqT2uLBdSju_4dm3fY8m8niFelzSIhLMc6AFOav2oCFm6782PGKG5oE8Q04xzt_oZL8zfHQYgBkptdisxnPR0mywaU49Ul9Cnl7AYGQbprJWR59LnjPRrGi252DQoFmzMsj4UPEGIZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد جنگهای پهپادی: چه کسی فکر می‌کرد که پهپادها به چنین عاملی تبدیل می‌شوند؟ آن‌ها ماشین‌های کشنده هستند.
شگفت‌انگیز است.
شما پشت درختی پنهان می‌شوید و آن می‌آید و شما را می‌گیرد.
و من صحنه‌هایی را دیده‌ام که نمی‌خواهم ببینم و نمی‌خواهم شما هم ببینید.
@withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/16579" target="_blank">📅 18:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16578">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ: نیروی دریایی ایالات متحده بزرگترین محاصره‌ای را که جهان تاکنون دیده است، علیه ایران اعمال کرد و حتی یک کشتی هم نتوانست از آن عبور کند.
هیچ پولی به ایران نمی‌دهیم
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/16578" target="_blank">📅 18:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16577">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d1c3a4bd0.mp4?token=Jo3SCNgV-LyMDC1EexTV8CLgt-rj_2Ty1qrpxuYOz7pcWfIR4E4UkA7EAMhplhIJJ-kHgAZwGDK4Nx-NsWF-670q6K20NfV6Hj_QJXISVcX5sqOHk2F_UizHhPlINxmw22R_mqcCODBQjQo_q3CJ_NfHaQxLXwPcgy9WbRY7_Ubve_s33Km0Kcr9hGg9uedzBYe37Jz-LFtzwM0dJGJ2vzHL7YD3znCmeIGtE2K_RF5GK3evZ5a8OosUq2pV_tSnJWtJlwMPietvkbmwnRlhsJqMWRePf_Qfx-k1YuzaJjQPsqE7QJkOUuAV1XNDo7sf8TV5gwee0Zesf3El6JTQgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d1c3a4bd0.mp4?token=Jo3SCNgV-LyMDC1EexTV8CLgt-rj_2Ty1qrpxuYOz7pcWfIR4E4UkA7EAMhplhIJJ-kHgAZwGDK4Nx-NsWF-670q6K20NfV6Hj_QJXISVcX5sqOHk2F_UizHhPlINxmw22R_mqcCODBQjQo_q3CJ_NfHaQxLXwPcgy9WbRY7_Ubve_s33Km0Kcr9hGg9uedzBYe37Jz-LFtzwM0dJGJ2vzHL7YD3znCmeIGtE2K_RF5GK3evZ5a8OosUq2pV_tSnJWtJlwMPietvkbmwnRlhsJqMWRePf_Qfx-k1YuzaJjQPsqE7QJkOUuAV1XNDo7sf8TV5gwee0Zesf3El6JTQgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره اورانیوم غنی شده در ایران:
ما قرار است چیزی را که من به آن گرد و غبار می‌گویم، یعنی مواد غنی‌شده، به دست آوریم. من به آن گرد و غبار هسته‌ای می‌گویم.
من به یک دلیل بسیار قوی وارد عمل شدم و آن این است که ایران نباید سلاح هسته‌ای داشته باشد. من به دنبال تغییر رژیم نیستم، هرچند این همان تغییر رژیم است.
رژیم اول رفته است. رژیم دوم رفته است. و من فکر می‌کنم رژیم سوم منطقی‌تر است، اما خواهیم دید.
@withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/16577" target="_blank">📅 18:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16576">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6831709af6.mp4?token=CsGo6TgMBV1RLY1eNxz_Waqi2BJx9zhWbTBJ-B-JflETU7IptKrvvu-OyQjjHt6orva74QlUvZYc0M8pzHgQ87cUnYIUtOfcBV0bvtg9u_I_IxPrMspwSdZoyE9Mbta_pTTWCZW-6G7QsdH4rdXDWtVKH93lXdBEJ1THa6V2MTx4mOhKv0xS0EXPyCG6b4av6LUE9jglAcjzk0I8tkKpVUIf3lFLNuJ0FNhfSkRTdBgP3wwrhwPoxy4SUSXX74gn0lvgSARmbtSChVTN60UUnwjebNIx4bS3O576uGrDkWvqw9T4mk0so9DvBKWAZEI8DO8iL6bbmPDGMyxRW9WePH-cec0AMmXm5OUrNrrhfxefIuPzUPP2vBqJcN0YkPn7_iSv8plZqZPYaOdmbY3PLEbAR4PvQQ4WUnWHz7t19fPk7wNsKG9B2s3HhX30pRTu3Itff-rMMXV5U1nxt0S6-knlWD1R2UMjLNbGgDfJTlDGWv221MpIauFmtBtZSMBslkataI1BYqnUBbkLuW59Y662Y8vd7T7AhUeua77w1yXZ_Htx2jauxEjr_UnG0Kz1Ujc7lJ6iUGChQkjtzUEcPOOG7LeE1xQA6hKh6u5a3TMciLHnEbTxP3dvqCRsGimPPtEXCORTZVlmw516OKNuhZ1EeC__8XdsEdhET3OCzAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6831709af6.mp4?token=CsGo6TgMBV1RLY1eNxz_Waqi2BJx9zhWbTBJ-B-JflETU7IptKrvvu-OyQjjHt6orva74QlUvZYc0M8pzHgQ87cUnYIUtOfcBV0bvtg9u_I_IxPrMspwSdZoyE9Mbta_pTTWCZW-6G7QsdH4rdXDWtVKH93lXdBEJ1THa6V2MTx4mOhKv0xS0EXPyCG6b4av6LUE9jglAcjzk0I8tkKpVUIf3lFLNuJ0FNhfSkRTdBgP3wwrhwPoxy4SUSXX74gn0lvgSARmbtSChVTN60UUnwjebNIx4bS3O576uGrDkWvqw9T4mk0so9DvBKWAZEI8DO8iL6bbmPDGMyxRW9WePH-cec0AMmXm5OUrNrrhfxefIuPzUPP2vBqJcN0YkPn7_iSv8plZqZPYaOdmbY3PLEbAR4PvQQ4WUnWHz7t19fPk7wNsKG9B2s3HhX30pRTu3Itff-rMMXV5U1nxt0S6-knlWD1R2UMjLNbGgDfJTlDGWv221MpIauFmtBtZSMBslkataI1BYqnUBbkLuW59Y662Y8vd7T7AhUeua77w1yXZ_Htx2jauxEjr_UnG0Kz1Ujc7lJ6iUGChQkjtzUEcPOOG7LeE1xQA6hKh6u5a3TMciLHnEbTxP3dvqCRsGimPPtEXCORTZVlmw516OKNuhZ1EeC__8XdsEdhET3OCzAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : یا توافق میکنیم یا کار رو تموم می‌کنیم، تمام کردن کار سخت نخواهد بود.
من ترجیح می‌دهم توافق کنیم چون نمی‌خوام به ۹۱ میلیون نفر آسیب بزنم. می‌تونیم پل‌هایشان رو در یک ساعت خراب کنیم.
می‌تونیم تأمین انرژی‌شان رو قطع کنیم، تمام کارخانه‌های بزرگ که ساختن، کارخانه‌های بزرگ، زیبا و مدرنی که پول زیادی هزینه شده بود. حالا دیگر پولی هم ندارن. ما پولی به آن‌ها نداده‌ایم.
می‌توانیم برق و نیروگاه‌های تولید انرژی‌شان رو، به قول من، در بخش کوچکی از یک بعدازظهر از کار بیندازیم. هر نیروگاهی از بین خواهد رفت و آن‌ها این رو می‌دانند.
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/16576" target="_blank">📅 18:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16575">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ:من به دنبال تغییر رژیم در ایران نیستم و ترجیح می‌دهم به توافق برسیم زیرا نمی‌خواهم به ۹۱ میلیون نفر آسیبی برسد.
@withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/16575" target="_blank">📅 17:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16574">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کانال ۱۴اسرائیل: مأموران اطلاعاتی خارجی، مجتبی خامنه‌ای را در جریان مراسم تشییع امروز در نزدیکی میدان آزادی شناسایی کردند.
گزارش‌ها حاکی از آن است که وی با پنهان شدن در میان گروهی از افراد حاضر در جمعیت، تلاش کرد از ردیابی بگریزد.
@withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/16574" target="_blank">📅 17:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16573">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTQIjo_WOR_AajmoPLMMGrkdabLHYMnaLBJfxOdPSc9QOS1Re_wdTk5cyIjjEUl212lrf3lCnRuyPrFBZ9YNLg_X_nbHFlEhr8sHbSemX_YkGCgQ_T2mFkL4l8WmyRzdUVxn9bvQ5ZxZ1cwAsnePvkEMROu3NRGevTTcL5KPwfTCDbkJiOy-Mz28YynHHG4Jf20J38Rh3FGU6BpY7BKNfSNbdxYCPx6blspQHI4Jm1ZydkfXBxLukjmSiktDcveqVNP9YeWIm_4HuEjaisA2yhbV2VyjdUuQ7ssJLNRRzSUshZD74xwSKzlV6N-SbHf_XpROBtwNBn0GCYua3q0C-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن چاه وشی این استوری حقیرانه را منتشر کرد …
@withyashar</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/16573" target="_blank">📅 16:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16572">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مجری فاکس
:
چرا این حکومت هنوز توی ایران سرِ پاست؟
نتانیاهو : چون چند صد هزار نفر نیروی سرکوب داره که وسط روز آدم می‌کشن و شب هم مردم خودشون رو به قتل می‌رسونن
@withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/16572" target="_blank">📅 16:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16571">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a33dabae78.mp4?token=bN6AZA8yWS4ECfFtdpxqLKYNduc_XkxUlXCLHEn1pPcisxoSKjRSHf1oLItbM1iewtNm3NM1zQHVKVsZw3IrJLx22K7A7Dvat3jlC00VvA_Ow6pdTJF4NXdVYKDr3vynqkAeKKcz3r38itV6vn3B3U8bQ89FLilJVzUQWDC-uuk8yLDSixWr7vuUbQXTYtQeLl94IJuV3RmVVcQYoHOm_5o6ZgILblepYqPnwdyhToZWsSKGoIBVAoAo3F-iAZN7dl-M04tmwH4x4a6MDifZlTMEkW7Of40pNOaRe3PBDyHL31iWCzwNErck5lTqaLxAgA53LAdMkQqHZr03k4zwnD48OLxc7cmJgcrAjiuQJKhdHKS7mMpQqHcw0ow-zUeCTmhP6vN3BKKoSbuWYPhonZrjVeR1spPax6iVbprRxHzPjNEMVjlaTC5HTqP1jobENF4siGbeDQQY8rKJFFiujQ-rvN97OdFPrhQyX4rMIcarTGwnYSGeiE6iZ6LDsFi_A7-BVtiyvzA00_S4s2-tir2PW7FTta4jR1OiL8HArCWbkRmXeZAjZ-ELnkH_Onir4moWUtWoc0iU83Me1YZCW4sSrSv7gMYG-IO6omqxJtIxkgpsjQmSI-NOFWbR-YJyuBvmff80UzfOavAUERM69aGbtirHfe4z6DS_K51p9uM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a33dabae78.mp4?token=bN6AZA8yWS4ECfFtdpxqLKYNduc_XkxUlXCLHEn1pPcisxoSKjRSHf1oLItbM1iewtNm3NM1zQHVKVsZw3IrJLx22K7A7Dvat3jlC00VvA_Ow6pdTJF4NXdVYKDr3vynqkAeKKcz3r38itV6vn3B3U8bQ89FLilJVzUQWDC-uuk8yLDSixWr7vuUbQXTYtQeLl94IJuV3RmVVcQYoHOm_5o6ZgILblepYqPnwdyhToZWsSKGoIBVAoAo3F-iAZN7dl-M04tmwH4x4a6MDifZlTMEkW7Of40pNOaRe3PBDyHL31iWCzwNErck5lTqaLxAgA53LAdMkQqHZr03k4zwnD48OLxc7cmJgcrAjiuQJKhdHKS7mMpQqHcw0ow-zUeCTmhP6vN3BKKoSbuWYPhonZrjVeR1spPax6iVbprRxHzPjNEMVjlaTC5HTqP1jobENF4siGbeDQQY8rKJFFiujQ-rvN97OdFPrhQyX4rMIcarTGwnYSGeiE6iZ6LDsFi_A7-BVtiyvzA00_S4s2-tir2PW7FTta4jR1OiL8HArCWbkRmXeZAjZ-ELnkH_Onir4moWUtWoc0iU83Me1YZCW4sSrSv7gMYG-IO6omqxJtIxkgpsjQmSI-NOFWbR-YJyuBvmff80UzfOavAUERM69aGbtirHfe4z6DS_K51p9uM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‎نتانیاهو به فاکس : ایران حدود ۹۰ میلیون جمعیت داره
- به نظر من حدود ۸۰ درصد مردم از این حکومت خوششون نمیاد و مخالفشن
- ولی بازم چند میلیون نفر هستن که حکومت می‌تونه بیاره تو خیابون
- اون‌ها هم شعار "مرگ بر ترامپ" و البته "مرگ بر من" سر می‌دن
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/16571" target="_blank">📅 16:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16570">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حماس: رئیس کمیته پیگیری امور دولتی استعفا کرد و این کمیته منحل شد. همچنین اختیارات این نهاد به «کمیته ملی اداره غزه» منتقل شده و تمامی مقدمات برای واگذاری مدیریت نوار غزه به پایان رسیده است. @withyashar
🚨</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/16570" target="_blank">📅 16:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16569">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwuoRGQ8XfDkuN1d18gpw_DS8HnHachji7PD10S8iPVpPPS1Wvp3ZI1AlU_7b0b8Qd0U2Cg8LwLJc_mtDt6MiiNpbiIJzmacEVtXj-q9OD1eWYVkRHlBul1BkYrzHPXqrilzrs7SMXn_nSg08WOmDx45_QkPw2xN25_AFtQGYHcbDVfbfTPa9lC8eVngXs3SQyH9D3vgGvQLTJWF55jAkO7PkinjRdwkZUh2pu-VykblquACTyhTP5khd2r-Xa85tvgOoft_alzEoIecwRKyHW-x5m5-DdTmWFAvYci28OYr1EFTOIloshI7PZWlqyhRYG5r43AelrEJmnTzfiLO_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور میم معروف این روزها در مراسم @withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/16569" target="_blank">📅 15:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16568">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">روزنامه الاخبار خبر داد: پرواز دومین هواپیمای ایرانی به صنعا در ساعات آینده
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/16568" target="_blank">📅 14:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16567">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92eb08c456.mp4?token=A6InYeofK0ZI8fnWQ_4a1JxtUlMMyNUwnNOo3R_1P-dTbcBPxK5vmgJYANOA-GYGTtM7fbng0bCChJgOctVag80vWO8Mxz17LsGDhSjr0RGd5XlqwP2nn4z_S7q8mzFjB0Wpzb0e6BWYDxQ00kwK3uzTusnb2BuvEQAZhEgPn39p7l76BI-PH0_H63HIJqtl90twX1brzlwnrdHzbnfEfpHf8Wk3NkmKx1woe_tVytIl5uEtMIFVeWLWkiuO_zcn3ngauw4nvBs9wv-V5DIlzK7aWpatlpW2vc7jZk-juTfN9PHK0e5DXkW2G2KaObd3LUPQtnBxaA_CC6RyZYkNaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92eb08c456.mp4?token=A6InYeofK0ZI8fnWQ_4a1JxtUlMMyNUwnNOo3R_1P-dTbcBPxK5vmgJYANOA-GYGTtM7fbng0bCChJgOctVag80vWO8Mxz17LsGDhSjr0RGd5XlqwP2nn4z_S7q8mzFjB0Wpzb0e6BWYDxQ00kwK3uzTusnb2BuvEQAZhEgPn39p7l76BI-PH0_H63HIJqtl90twX1brzlwnrdHzbnfEfpHf8Wk3NkmKx1woe_tVytIl5uEtMIFVeWLWkiuO_zcn3ngauw4nvBs9wv-V5DIlzK7aWpatlpW2vc7jZk-juTfN9PHK0e5DXkW2G2KaObd3LUPQtnBxaA_CC6RyZYkNaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیه در مسیر تبدیل شدن به جمهوری اسلامی تخت گاز پیش میرود
: ویدیو تعداد زیادی از مردم ترکیه در یک تجمع اعتراضی که هدف آن، وارد کردن یک ضربه به کیسه بوکس با تصویر نتانیاهو برای نشان همبستگی با ساکنان غزه  است
@withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/16567" target="_blank">📅 14:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16566">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گزارش هایی از حمله و درگیری بسیجی ها با قالیباف در میدان آزادی
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/16566" target="_blank">📅 14:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16564">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcXuxXPdyL73FrW2LOfHnWRNJzdIOu2YT_8JwPdI5t8NAZLff1p7r2nEPNnxCys46fl73Blf_mgzM40iQb0MZeZT1a36A7V2QGcPZkLhGVW6kDZ1rXMwg0tZXMaqfuGTFHjheI0vhQvPdLcxMSSQdoe_HGF1rnftU5xNddH8Bn2lqHCTe9K1czOa-vYhhplI6Q3UP15ciC3ol4jNieKWf7oerGktOHN3cnNEu3NuSHRzUJAC2BMAn4J8QcPupEmmxeL7i-tDZN26tB8w8kwcbh_pXqUIAnGCrCJ-1Mr9jemZSsJIEgu2A7k3hgg1z9D8qRpVFlhqQMB8-DCBMrp1yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5278196c6e.mp4?token=n9nZjdbG5bSTpIaJL4YLWSGpglnwi39fKUjJXF02xab74g91vnFcEviW26tm5n8h_kJJzS5EQgYp5KgZM7XSs9sZiMBU9_aVktuw0BW3_YaVvUC1qyBW43bYOfjPdIxFjmFOJY8FrC0zeWfc45gb-XT0nO54qHdw-zKtoIWS6qMlcVPwcTHAI83gnKhDbIUwQVPLrEOWitLPU4MUemJz5ByCvb5qs1-jLVZNH_gz_lSpMNKxgJYyJU6yy8m4LxrzJaXwjlIIdeW6DKlp4URc9kwW17wc5c9mI9gaFVsfDukE6fg0oec7aI12XYrEKRpklVOsntOv7XdRzc5L4NR2IlI3MBNPgDPeTb52OKuVKoxPYPLs49LvbbxqxaJo6fth8vkw4Ya7jYgX-1GuzdA1aDWDC9rUVJDCAujsyqCsj4O81KOGq7-dTieX_O5FaLo6ZBZh_D9SNJzzqqpu6VxH99u7dq9BrgjuoIgjFuL7IPPg8n5UWxoP7chLi699VnbHEavr44kSSuXIdtzTSJmzcExGD48k3RZq7Sn6W-vQ5bVstF6-NnCq4XzWacirwv-GjxpaqrKPoPGzLwKt8dEuCjxqgGPJBFPxBpDqlXZpVqGhjmrYG3H6GqWbRww15k1uq5vjT6tRyCuBMZdzRvcrgs6zuxEbvmOtOjLtzjRLUUU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5278196c6e.mp4?token=n9nZjdbG5bSTpIaJL4YLWSGpglnwi39fKUjJXF02xab74g91vnFcEviW26tm5n8h_kJJzS5EQgYp5KgZM7XSs9sZiMBU9_aVktuw0BW3_YaVvUC1qyBW43bYOfjPdIxFjmFOJY8FrC0zeWfc45gb-XT0nO54qHdw-zKtoIWS6qMlcVPwcTHAI83gnKhDbIUwQVPLrEOWitLPU4MUemJz5ByCvb5qs1-jLVZNH_gz_lSpMNKxgJYyJU6yy8m4LxrzJaXwjlIIdeW6DKlp4URc9kwW17wc5c9mI9gaFVsfDukE6fg0oec7aI12XYrEKRpklVOsntOv7XdRzc5L4NR2IlI3MBNPgDPeTb52OKuVKoxPYPLs49LvbbxqxaJo6fth8vkw4Ya7jYgX-1GuzdA1aDWDC9rUVJDCAujsyqCsj4O81KOGq7-dTieX_O5FaLo6ZBZh_D9SNJzzqqpu6VxH99u7dq9BrgjuoIgjFuL7IPPg8n5UWxoP7chLi699VnbHEavr44kSSuXIdtzTSJmzcExGD48k3RZq7Sn6W-vQ5bVstF6-NnCq4XzWacirwv-GjxpaqrKPoPGzLwKt8dEuCjxqgGPJBFPxBpDqlXZpVqGhjmrYG3H6GqWbRww15k1uq5vjT6tRyCuBMZdzRvcrgs6zuxEbvmOtOjLtzjRLUUU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخی رسانه های رژیم از حضور جمعیت ۱۵ الی ۲۰ میلیونی در مراسم تشییع صحبت میکنن ولی اگه مراسم حج امسال در عربستان که فقط ۱ میلیون ۷۰۰ هزار نفر توش شرکت کرده بودن رو نگاه کنیم میبینم جمعیت چند میلیونی خیلی خیلی بیشتر تر از چیزیه که فکر میکنیم.
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/16564" target="_blank">📅 14:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16563">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پاکستان آبزرور : احتمالم میرود برگزاری دور سوم مذاکرات ایران و آمریکا در اسلام‌آباد در روزهای ۱۴ و ۱۵ ژوئیه (۲۴ و ۲۵ تیر) شروع شود
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/16563" target="_blank">📅 14:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16562">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">توافق اوپک پلاس برای افزایش محدود تولید همزمان با بازگشت قیمت نفت به سطح قبل از جنگ
هفت کشور عضو ائتلاف اوپک پلاس توافق کردند تولید مجموع نفت خود را در ماه اوت به طور محدود و روزانه ۱۸۸ هزار بشکه افزایش دهند، همزمان که قیمت نفت خام به سطح پیش از جنگ ایران سقوط کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/16562" target="_blank">📅 14:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16561">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qodOCrS0DzX4xBjMuyVe9QPymTWJcMVpWjxWmgNYEa-MvQesAio6uzjW7HwdTwyGGMFCj5nn9uFTUPANBHNx6iHx9uQvbKkXkO1_lFt4ZW2acBc9VyGwVsuzsmUas3uYMMxitQwVRTdf103iXdtwg8NVgMfeY5vlaTzr8ZGcADs2VQTypCc-166xnvDF8KidwSuWUgIkjxaA70944ZPIajuKnuT3zWKQDBGODsapj9VDl36JNP9cHRF4QBBRNHh4JP240PDu-A08vrQ1mg0uAsF1yg0J_6bUpW5UB5bcGvfJ361OLu41XaJLkVpF25Kx6N7C2fhWtKdAdRwZWYyvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: جمهوری اسلامی همچنان با مشکل فروش نفت روبه رو است
@withyashar
طبق این گزارش ایران ۵۸ میلیون بشکه نفت روی دریا دارد که ۹۰ درصدش رو هنوز نتوانسته بفروشد
از دلایل مهم این موضوع کاهش واردات چین است. از دیگر دلایل هند نفت ایران را یا روسیه جایگزین کرده است
اروپا هم در شرایط فعلی باتوجه به نگرانی از فعال شدن مجدد تحریم‌های نفتی از خرید نفت ایران خودداری می‌کند</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/16561" target="_blank">📅 13:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16560">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کره‌ جنوبی:ایران برای مراسم وداع با رهبرش از ما دعوت کرد ولی زمانی که میخواستیم هیئتی برای مراسم بفرستیم به ما پیام داد و دعوتشو پس گرفت و اعلام کرد حق حضور تو مراسمو نداریم
@withyashar</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/16560" target="_blank">📅 13:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16559">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZfQoBneBMF34sf1szxrM-Kk_j4E9qi3uK0oh-rsCm3QcOOu3rrb4gFeaInQJRsHxYHFh-4dXDwvAyI5cKyDrBLJyZiA_J6_dEnPplg8qeR9jn0BAm7-m81OTZJMi-cr60d4c6Y4CrCRui11mSsX4hGKNpr9D13K0UWBV8vfB-Z2yltAaxh6OV2A9khPPsBQBAkHBGK9h4v_VFYVSI2XHRftTrqnfX75Ahf-1UBAApHQeBH1INO6OL6EUjzb1OpUI_HQL17LKnxQbZAKRc1bRnaAvQPoiWeJ1vSLxn-Ph6zYb4DGGVuHPhiDSzmm9eYlm8xnAWd5Mi2YCFlVpmLeFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور میم معروف این روزها در مراسم
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/16559" target="_blank">📅 13:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16558">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دفتر رسانه‌ای دولتی غزه(تحت مدیریت و کنترل حماس): تمامی آمادگی‌ها و ترتیبات قانونی برای فرآیند تحویل و تسلیم سیستم دولتی، انجام شده است. @withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/16558" target="_blank">📅 13:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16557">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دفتر رسانه‌ای دولتی غزه(تحت مدیریت و کنترل حماس): تمامی آمادگی‌ها و ترتیبات قانونی برای فرآیند تحویل و تسلیم سیستم دولتی، انجام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/16557" target="_blank">📅 13:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16556">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3uq4QuTS59XH0-RIn22L0I6xgRmUZGwKaI4Ih2D5xkao1ZLS8-R61J2PI96JCVZYg4utD7rskDyYax75O9Ny49mFxwT0fNVfXKexP4ZxgCHmvHZS7qApn1WYTvrDKOHfkhyfMl6JO-vq8BmpH8DVmFX8JZ10MjtCe0nr6YnjNM89dIMjAD8Som4UHXp10uCm8xlw6ImtJclDs75y2CPUDMFB944zuD9aV7NMChL3Pk3VY3Aek13GGcvPvBCPsUV3BiaPcpegK1kwLMoOXae7TniKSw8vq_lUajK__5TP3xwMp2vp-g_b3NTHi8wAwFMmjWisViBfrsxpkWTLYCsFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حمله پهپادی هدفمند اسرائیل در جنوب لبنان.
@withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/16556" target="_blank">📅 13:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16555">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59bbec746d.mp4?token=PI2lAHm38-uW8czy1YbinDxRj5HYj8YKWgvpABDDsYDBBN-nlNt6jJs1ockFi9fBDJWRRoDCHgbl9Jnv0CanW2oM6M_wmBwjVNpO-3CoOgFQeQ8_YdUtFK6sUZA1sMBiAyl78Zow4gEeH1xUjCx6-_XifPJPsie056yRDhQ0FBsLVNQxPIWyBS3hwME59dwS4JB8WTW-mNIFbbaJZcp6-W6vXADhlKDQPP1rVyBD45lBIjN6XO38F0xK8yPr_Ulod7NBBKEViGco4NWW_WU02sIE6PYsF-br_QERlSML99x5yNhLq9iMz75GvmP_-HI1sTMPKgt0Hj-4y9KvKEBRZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59bbec746d.mp4?token=PI2lAHm38-uW8czy1YbinDxRj5HYj8YKWgvpABDDsYDBBN-nlNt6jJs1ockFi9fBDJWRRoDCHgbl9Jnv0CanW2oM6M_wmBwjVNpO-3CoOgFQeQ8_YdUtFK6sUZA1sMBiAyl78Zow4gEeH1xUjCx6-_XifPJPsie056yRDhQ0FBsLVNQxPIWyBS3hwME59dwS4JB8WTW-mNIFbbaJZcp6-W6vXADhlKDQPP1rVyBD45lBIjN6XO38F0xK8yPr_Ulod7NBBKEViGco4NWW_WU02sIE6PYsF-br_QERlSML99x5yNhLq9iMz75GvmP_-HI1sTMPKgt0Hj-4y9KvKEBRZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویر ماهواره‌ای انبار مهمات پایگاه هشتم شکاری اصفهان که توسط BBC منتشر شده است، انهدام کامل ۴۶ انبار مهمات و سازه این پایگاه را نشان می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/16555" target="_blank">📅 13:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16554">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خبرگزاری مهر: پزشکیان، قالیباف و فرزند رهبر انقلاب فردا در مراسم تشییع عراق شرکت می‌کنند
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/16554" target="_blank">📅 13:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16553">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کاتز وزیر جنگ اسرائیل:
خامنه‌ای که مراسم تشییع جنازه‌اش اکنون درحال برگزاری است توسط ما کشته شده زیرا او طرحی را با هدف نابودی اسرائیل آغاز و رهبری کرده ، اگر رهبر جدید هم از عاقبت پدر خود عبرت نگیرد به سرنوشت آن دچار خواهد شد
﻿﻿﻿﻿
@withyashar</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/16553" target="_blank">📅 13:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16552">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0de6a03c0.mp4?token=W75svexWKDfOmr_INmaVV9lwy0FK7-gnfHD1AAlCkQFODZIfrJiOZhkgafwEO6KKW1YNyl05FnXUmiy8QEujJjdVLxmrRkEpWt1uUl-QJTRalfZKdN7V-ukBkVsgm1eDwn_hZgaLm-WIYUeooVVvzJzENIEG2A7RadPJmVUBy5kOse5d-PWjquOuObwsMiBP7De43uRWxETwS5fJf6X4XJXjS5iJoOUP5GPGNZc8Zdm8UDFU9OxTJnKaANWGKQEFvJwOBl9HmEDx68EbpCHSzPsi6AcXzaKYaZWYZnu312AUUTia92fMwuTH2rNEeYLWlIrZiNnrZ_JOBsaRKl7FyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0de6a03c0.mp4?token=W75svexWKDfOmr_INmaVV9lwy0FK7-gnfHD1AAlCkQFODZIfrJiOZhkgafwEO6KKW1YNyl05FnXUmiy8QEujJjdVLxmrRkEpWt1uUl-QJTRalfZKdN7V-ukBkVsgm1eDwn_hZgaLm-WIYUeooVVvzJzENIEG2A7RadPJmVUBy5kOse5d-PWjquOuObwsMiBP7De43uRWxETwS5fJf6X4XJXjS5iJoOUP5GPGNZc8Zdm8UDFU9OxTJnKaANWGKQEFvJwOBl9HmEDx68EbpCHSzPsi6AcXzaKYaZWYZnu312AUUTia92fMwuTH2rNEeYLWlIrZiNnrZ_JOBsaRKl7FyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با شما : یاشار جان سلام امروز تو مصلی بعد از پایان نماز ، بلندگو ورود مجتبی رو اعلام کرد اما بلافاصله هم صدای مجری قطع شد و بلافاصله آنتن ها برای مدتی قطع شد... @withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/16552" target="_blank">📅 12:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16551">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIw0zTJkN1UXC2XUrdAMS-iZ5QXqPX_vozlwQKzLlXmDL3EUwGwf4DUuaoQD0k8f076MP7sE8y1giah-0vAtxLl3M1Pb6swEZpvR0HF4DUoG9a73zrhGZ__v0BQNzBk4Kutw42P1kvO1SM1gRsOJLtH0qCYrsKKENG7KmpExAEGsnbFspTHNdKFZfeuAUnDd-FJX8xf_FBFv3SU17X5tnKFFVFD7UEMCceGpj-VMFP6vT_Yt6pYzN54mD41HkNkwtce5CBqY9hM7wxoVlQkq1-nMWvDe-Sf0qVa6OLbkF1lHrY_HStxdLGs2tZxUO8F7dUSnNqTysJXsfUCJ8JWanw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به حملات خود در جنوب لبنان ادامه می‌دهد.
انفجاری در پی فعالیت ارتش اسرائیل در منطقه بنت جبیل رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/16551" target="_blank">📅 12:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16550">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/061472f621.mp4?token=nk1PFcLxAa38xy9Qyg3fCGO4Q1Nu13xpmeiuO8olfPdAOVuOYquFjsxuITPTWU1l5ejI9oQwUp8Jb1yaJu7fbl49iperYPItENkZ0QrK1af3DS8KV66KtwCsvRGvMfkO7a-VyZLrB7HICbgsFDX3kNvLsh141XbQGJk0AMWSFk_sqprDlWmJZxZVjBQfEvjwFEmuOPJ2bDshGhmG0Dke65w6_W-tQUQ6tk29Tj_TyBchZi11JYyyOVhaZWZdSmd19gzeV2qTux2OJqzzN71Bc4hrFr0ghWwEcoo49sohj3yQT6aPi8043dCnHgEsoykMdvojoRmTk6QhkO9IwbpiVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/061472f621.mp4?token=nk1PFcLxAa38xy9Qyg3fCGO4Q1Nu13xpmeiuO8olfPdAOVuOYquFjsxuITPTWU1l5ejI9oQwUp8Jb1yaJu7fbl49iperYPItENkZ0QrK1af3DS8KV66KtwCsvRGvMfkO7a-VyZLrB7HICbgsFDX3kNvLsh141XbQGJk0AMWSFk_sqprDlWmJZxZVjBQfEvjwFEmuOPJ2bDshGhmG0Dke65w6_W-tQUQ6tk29Tj_TyBchZi11JYyyOVhaZWZdSmd19gzeV2qTux2OJqzzN71Bc4hrFr0ghWwEcoo49sohj3yQT6aPi8043dCnHgEsoykMdvojoRmTk6QhkO9IwbpiVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور دایناسور جنتی
@withyashar
انگار دارن به ۱۸ چرخ فرمون میدن
😂</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/16550" target="_blank">📅 12:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16549">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ab53f55a.mp4?token=jWyvPrmEt7oj3OPGTPV4UYrkTjcEF7paSt-m6l-3o4Ayg3sCfRmrTrTMkyvyHRfqlKAW3OKxDibGDIApVDbivIhKWegLVyI9jQ0IzHMEOA-Bmw54ubVUxlgLs7gVoD8qIGqX99MpgUV-Jr8PhST5alG2zMl_Yz0Ak6ZwNtem08svjXoiSYHqUBGOY_ld3bZZ4NIqjAPGXz5RGH-5O4mBRHS1UTSP9sCEEbQLzkFGvY09dBx3KEkhOx5b3SPZMmfYWqMoVMSxPyFwwnkTzvlWs1zQI1gTC9sbHpx69yh0VWrjrbGwwdEoEUH-D9WtsSEXUHKP6Zyct59gqD5gUnvXOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ab53f55a.mp4?token=jWyvPrmEt7oj3OPGTPV4UYrkTjcEF7paSt-m6l-3o4Ayg3sCfRmrTrTMkyvyHRfqlKAW3OKxDibGDIApVDbivIhKWegLVyI9jQ0IzHMEOA-Bmw54ubVUxlgLs7gVoD8qIGqX99MpgUV-Jr8PhST5alG2zMl_Yz0Ak6ZwNtem08svjXoiSYHqUBGOY_ld3bZZ4NIqjAPGXz5RGH-5O4mBRHS1UTSP9sCEEbQLzkFGvY09dBx3KEkhOx5b3SPZMmfYWqMoVMSxPyFwwnkTzvlWs1zQI1gTC9sbHpx69yh0VWrjrbGwwdEoEUH-D9WtsSEXUHKP6Zyct59gqD5gUnvXOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین ویدیو از احمدی نژاد
@withyashar
یاشار: من چیکار کنم کاپشن پوشیده ! روانی ها
🤦🏻‍♂️
😂</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/16549" target="_blank">📅 11:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16548">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c911eae2a5.mp4?token=DW9FL4Srscmh8_gnfRuSA_sxsfqqfJZrlE9Vcm_WXXiHX8-miou2HVHKHt7fdjSt8Uq9nhling5TWurGK858nfuqG78326nLdtYPrvdYEGvOdzEHqOBNmFxFwDNgvRm8Cwi9dCWTKN1j996UkaiZY25E8m0QgVMwTGpcyL1xO68HH17oirWEIt8IMJS5N_ryG0HG9EnMBmS_iNWB1LT7Yqf0fG25Ahpf7QZsys5HU5tVd0XWQcIHKwLqp3rfF-54FC08jOrR_g11xeVdDLR66WqqLzVZG9YpybKsH9hqHhpyBoldxmsWgMGbuGgtztJl1OtN_UL_YL-cxREroRijFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c911eae2a5.mp4?token=DW9FL4Srscmh8_gnfRuSA_sxsfqqfJZrlE9Vcm_WXXiHX8-miou2HVHKHt7fdjSt8Uq9nhling5TWurGK858nfuqG78326nLdtYPrvdYEGvOdzEHqOBNmFxFwDNgvRm8Cwi9dCWTKN1j996UkaiZY25E8m0QgVMwTGpcyL1xO68HH17oirWEIt8IMJS5N_ryG0HG9EnMBmS_iNWB1LT7Yqf0fG25Ahpf7QZsys5HU5tVd0XWQcIHKwLqp3rfF-54FC08jOrR_g11xeVdDLR66WqqLzVZG9YpybKsH9hqHhpyBoldxmsWgMGbuGgtztJl1OtN_UL_YL-cxREroRijFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودرو ضریحی عظما
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/16548" target="_blank">📅 11:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16547">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddbc5efdc9.mp4?token=iY1Xn7thkriQALYOnVoHv-a0Yq6AfIwM6uaWatvoM62zoqB8u3nDklkMGahrQdg9q52tUxrwogb7vll1Ip3Bn6CSIJsBbu0wNCJYEw7htK2lhUQC5xdxwezBsn3yIELMrTktv5lNKmCj7RryRb-ZBGmPdo_yPdxIzCJNZSsBVeqp-cow3FKg77pOeO7CEd2oEEjHuaSaeLJOO1N1JQYjdZeU2887h4hrCdWn4e_kvdzgmoRl_PkqvwjVft4PDeUSc-6tRBKW8AR0eGNUyskSsuzpn-KMldbabH4bc_sW9SzQHlyDoTpfXKzjvUXbACdeMkc_b-ZihUXPxVQ9WsP5Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddbc5efdc9.mp4?token=iY1Xn7thkriQALYOnVoHv-a0Yq6AfIwM6uaWatvoM62zoqB8u3nDklkMGahrQdg9q52tUxrwogb7vll1Ip3Bn6CSIJsBbu0wNCJYEw7htK2lhUQC5xdxwezBsn3yIELMrTktv5lNKmCj7RryRb-ZBGmPdo_yPdxIzCJNZSsBVeqp-cow3FKg77pOeO7CEd2oEEjHuaSaeLJOO1N1JQYjdZeU2887h4hrCdWn4e_kvdzgmoRl_PkqvwjVft4PDeUSc-6tRBKW8AR0eGNUyskSsuzpn-KMldbabH4bc_sW9SzQHlyDoTpfXKzjvUXbACdeMkc_b-ZihUXPxVQ9WsP5Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ورود وحیدی‌ با موتور
😂
@withyashar</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/16547" target="_blank">📅 11:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16546">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">الاخبار لبنان: یمن در حال بررسی بستن تنگه باب‌المندب به روی کشتی‌های سعودی جهت فشار به این کشور است
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/16546" target="_blank">📅 10:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16545">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxxkILhczYpz9B8LRoPmwNnStB0GrqJxmAllYCvEHuh8ApiMdssJYglfz6N1d5eu0Vap_X9NW7kDfn3ofp56Y8WRjpf336rd_gIdiVwylA9EmLYbSKEqKpLH6nAJR52nvsMaHbFALzsl5VLmSBEAhznfbx_U6M55CzOSdGAEYE3pb-GGVizjaUdRhi_NAsnZfZSvui62svQI-HAbKiR8pNw6GeNsb5TzRLHfXeYp92NE-tuGqbPC_BmR76m3nSV0jYiJXxcC7DAVZDhAiWX2C2sn4q_OZh0z8hxA66epiLZn3_J2kFlWpH6wSj-lVqrnQ_39tmiTjBdnoCMS-pYRTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از انتشار گزارش‌هایی مبنی بر اینکه اسرائیل و آمریکا قصد داشتند او را در طول جنگ، به قدرت اول ایران برسانند : محمود احمدی‌نژاد، رئیس‌جمهور سابق ایران، در مراسم تشییع جنازه علی خامنه‌ای شرکت کرد.
@withyashar</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/16545" target="_blank">📅 10:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16543">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k_-XFXwFRNjYvYPLCO7dUTyO2vRL22UrxRvCsLkdRqpLmzkyqEskDivV0HTxPNNrr4BvKNNj9V4ipSJqGv3I95Wr-6dOk68FBtkFzLc0PYaHIc61bHk7_ylMnYHYEN76wqBpzGPlwJq8-hT3g_uFaQPRMtAYNoo2W4kU_ioevffj3WE9SGIuSTzfqrdx2hdxoEjgK1KHINbQSpBiiEeGqw_i_-iTIvT3z5GWni8soKIJYJe09kRWx1JqLYrwGV4uVNtvl72n4pQMQxZFX74D6q3_iu4klkCii1V6-fI-PXpRTxLDx7ROdRU_qLj3YLn1yhUpGB3ulW4nqCp1IeY2Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CQuyKgGatsdRtKhoameq3nre5WRCfjoADb9wit7f0WIEtxQXXN4bfLYajVnaNV_PMlemwN9rElWkHn_nrX9GCwZ65Kt_tIq1eYNFdJLfMrpa8G3SebpiPUE6uUstnadHLWMmx_0QTnYlfnQWFqlaYcrGmsnLb6yNh8hXJp_o2Lyh_vsW36TSgyNyJa5aIFKM_97cSJ8BNA3kQJ6XD0JtXjpwaugByE7kvNm7f6oVJDWtxC4DyT72nlTRsuukrWkRt0xTWtNyrfkq8iWK8d84uS4P6iGiWM3kqc9i1wJrp1XPQcxSkP4lp8k2YENnEqRcRKqYa4lP2Jvsdx8HF_7A9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمایش قدرت در برابر اردوغان: ارتش اسرائیل در تمرین مشترک با ارتش یونان.
در طول این تمرین، هواپیمای تانکر اسرائیلی در حال سوخت‌رسانی به هواپیمای F16 یونانی بر فراز دریای اژه فیلم‌برداری شد. ارتش اسرائیل گفت : "این همکاری بخشی از یک برنامه استراتژیک گسترده است، در دوره‌ای که ترکیه تلاش می‌کند قدرت بازدارندگی خود را تقویت کند."
@withyashar</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/16543" target="_blank">📅 10:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16542">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">این آخرین تلاشمه …
@withyashar
⚠️
یاشار : عرزشی ها اومدن ریکشن فیک زدن رو این پست ، اتفاقاً این کار ارزش این ویدیو رو بیشتر می‌کنه و نشون میده چقدر سوختن</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/withyashar/16542" target="_blank">📅 02:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16541">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnRAc_y2OqurP_Z0A5aVCxVefvlCNIbbgcgQTu_lcBXjFv_JQkCPfQ8UQxVFft0k1M7n2Xckdj_smgmHq6ISfGfEREGippN2sg_IBcxT-nxxceSiPUb6U5FR1Aa7ozztg2jNhhkjsYE0Vdan9Mse4lHt7KKQImECs8n-z91H9e6cAa6_2olj31powFHOYStBRJAQlcee8J3S7qHi_NvI0nlW5ggVDVuF68EmvU0aELG6d2fzzeBPqxe9i4m7YBgmQsPDkUyVErsq96GR-xLEbASrAHcp6MRxliqUzhIIWgUoML_8eM3dZdfuTHwBzZkhXq3YWkieWptNkKozH0IMtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوگواری شبانه روزی نیرو هوایی آمریکا در‌ تکیه تنگه هرمز در غم عظما
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16541" target="_blank">📅 01:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16540">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLW_Ws6ZYzGPuvi56BD-oaKuaedHqYxOqyzfhML5RaFeyLRfdGyqJp_SgevCY6aWR90a3mfqXszypNiuW8G5QvLUB7TMW2HqINSWPwmIHQLPITXUbPptnm3CeBNRqgYyZtOr5FbkW7x30evuIXPZpxuskiDMsXcRJCY7WUCym5JjwSkG6F6UtONcjvyL9ktoyVqZSPXjPNDeOyenNX8qRzdmpMzNojKMn6kUpdEJhmkmlm05mQybQj_4I0NDvRGYWhIc_LKMhSSzsHZNLyLGZjTHXN1BbH5ATFhNORbHV1geDHtc_A62HBZdXFRTVRtLPArryoD8_YbMsi4fg-ATrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قفلی جدید
😁
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16540" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16538">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارش ها از آغاز درگیری شدید میان حوثی ها و ارتش یمن تحت حمایت عربستان در جنوب یمن،ده ها کشته از هر دو طرف تا کنون مخابره شده است.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16538" target="_blank">📅 01:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16537">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D42fa2S-p_ABZxP4k6P8t0eTkdlQj3f7ovesGU_r7GkXQFBQBbYI5I3vvEOahTtLxGBwtAVPmEho2TbnE4-eU2XIJ6H2r_ddSEnCzGpaF2qY6n4vO4Fb5c5slhvlnZD1jfeMOgVebnTubKonJ4Ep8_RiUuBGO1yZYpEJgs99uzG65aGimSzZhBOrtG2tnqVLOsleXfwZHrOBpofux3gr-piXkvbLp9lj4X1rWR2tskEcoHsWrEzx7kA5HLSJsUyA1isfKn93I2F3nU67sgAzOIqxs-JZSRvsv-YyKCJCbUz_RV8IEaxvhCfqlZ_q98EmHMCkjklV8LJ2O-LsywYLQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ پستی از خانواده خودش در سال ۱۹۱۵ (۱۲۹۴) منتشر کرد و نوشت : پدرم، پدربزرگ و مادربزرگم، عمو و عمه‌ام!
@withyashar
یاشار : میخواد بگه ما از قدیم پولدار و با اصل و نسب هستیم</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16537" target="_blank">📅 00:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16536">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zve6MIJpYnlgcBVKBET06QhlRnMsgScG0pskxqrnTs7UISJa3PGAF5HHYoOuR7sm9Eox5snVjOiw3c4OabqKZW3U1sPR-4pDdGKDT42xpXL-N5o7p-WPzMDs73hvpOnccPxY4dY8vIBb9mbeE5U7wHW_zFDVQeMY0cfqEZOmLxSGi_wNDbyb6xP77NB6KcDka2BLsEAJpevS4dTUQyEQ4OV6IlLVbxyEO0RPa1LTFwdN9xVtXEFIfKvBOf7cEkV5UMdpyCIPBk3KAaGLIXV1DBby9MgItoYRlv5LRvFBknxFCciUhY4h7n4NMcyLcmeUX_TBzdDi-ZZufmYuDKqktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهیه غذای «هانی» اسپانسر تشیع موشلی , دسر هم حتما با «میهن» بوده!
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16536" target="_blank">📅 00:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16535">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aw-gNv_sT3wlUhZPaauknAqA7SZLyesQld1HN9tOVbNaRlaKoq047K25anJw6koRe8fe-YEHhHfQu8rnl7gk2m6VB0VjFuBH05U6DMj1sbQKeWLvi96_c7W91AuIRE6gc1eX4euh4AGLc2Emh4iiBF5Mw3pZdKq9v2uGUNRP2HT2ZKwHplEOHde5ynXNpIMVjrd44cp4RKeauXglNWaEX1kth_-ThA1M6MzrH-Zvw5cT5DXtuzj-hK9L4Z3tIrUqOBGmfJuv_r0zvqDKgjWp_J9jN6yAaKlYfs18A_e40iy-U3lA-SNTgd8Xzp3jnbLSc7qVXlp3sr1rolXcFKY9mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پستانداران انقلاب اسلامی
وضعیت بدنی نیروهای محافظتی امروز در مصلای تهران
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16535" target="_blank">📅 00:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16534">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">در پی گزارش‌های منتشر شده از عربستان سعودی، منابعی در نوار غزه که از جزئیات ماجرا اطلاع دارند، به کانال۱۲ تأیید می‌کنند: حماس احتمالاً فردا اعلام خواهد کرد که کمیته‌های اضطراری دولتی منحل شده و یک جانشین برای مدیریت این کمیته منصوب خواهد شد. این موضوع تا زمانی که کمیته متخصصان وارد نوار غزه شود و اختیارات مربوط به اداره ادارات دولتی را به دست گیرد، ادامه خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/16534" target="_blank">📅 00:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16533">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خاستگاری‌جنجالی نوک برج امپایر استیت دو شهروند روس پس از بالا رفتن از نوک آسمان‌خراش «امپایر استیت» در نیویورک، در همان محل مراسم خواستگاری برگزار کردند، اما پس از پایین آمدن از ساختمان توسط پلیس دستگیر شدند @withyashar</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/16533" target="_blank">📅 00:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16532">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0LtEpTidH6vOMjjZ6whK5EdJ-apmfOlfuwUomiQrO6gxjcWOYLCFkxjSH2bm_kGYWJEkExJiaPP7DIqfBPTUAJA3ibZwsFezB3KiEvF1onHfgJ6hLOHIDlkEkg5c2CJalymvGUJ2qJWf4bS38o8g4-dmKSFcxV1p5nv45lE1uD54B_5eHODvL7S7FW0nxeGYO8p2RKaFoyfav5CaU29sbnV51ccc0xeWscECtqdnJkSTV07MMd2FcsUSvHV6B58TnbCCJeX63gpSZRKA7TEiwFEouDdVENahIphHQM-q4hia8GjPJGk_JnOTx0PVs8Gc6s5mO_R8aVtqSdaRA-UTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از حدود ۲۴ تا ۳۳ هزار سال از انقراض آخرین نئاندرتال‌‌هایی که در منطقهٔ جبل الطارق دوام آوردند ، امروز یک نمونه در
تشیع جنازهٔ آقای موش علی دیده شد.
@withyashar</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/16532" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16531">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uq_3xFuNtPAgHzqRjO-oLo0r8X3EwzB8i2qe1Emh47rc9Olmt_TBiPyj1GV_FchGW7J1Xg_COPHxnAfqlVj8LIAMY8bYXaaW6vhr5kOvQ7h0bQpqHVap0UUx-G8rqYhZpKMc6GDfNFpyzr2X8RwtoNDNlVHeCpBYlKn1_6vkIbg-qLJFx0n5IHA3sV1bCLVZFsngubsVBpNbWivavR678G1x2q-748JyqQlYPgAT9JUfsmZ7ZcoYc8L84r6aZzo5dMPSk6dqYyKP3PNJVuoseRz41ReQKqLBnCBJCaQtKDHB1xBlfv_pq2_SFyeYEnbT9vCL_OiEf8P1iQFwIuRhsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/16531" target="_blank">📅 23:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16529">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J86wmNSyg0Ci1S1JbJh3WkSlj0S603L1aHuGCD8EHSkkKzx-zI3khk6LYLkd7KYRaqfR_EpbDXe_eoxh-0bk6paYpMQQo1wqU8errqCxNUgnDf4u7-_RWl_T1nSATVQhN5feb_7NCt4t0RWGKMJc_PCQulqzMzwSM5cxrTomDZ1jZ_DDqKTKD7Ki7OUrRKqvphpMjhfwMQEo5bQWYOJbpc87kpu9ZBhFTw685XMXsNJgsL93NE6WgOJDL_UQ0JCLghqBoh3BdqaV3ng1eyU-i5JTr9BAc7pIFeiU9BlASwSmNZm8vz190AXx_uOINIIl_FVRYFVeTz_QcCNFTd0Oew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏شرکت هواپیمایی سعودی اعلام کرد که هواپیماهای بوئینگ 777-200ER از رده خارج شده خود را مستقیماً به ایران نفروخته است.
‏این شرکت در بیانیه‌ای توضیح داده که این هواپیماها در تاریخ ٧ ژوئن ٢٠٢٣ به شرکتی واسطه خارج از عربستان سعودی فروخته شده‌اند. پس از اتمام این معامله این شرکت دیگر هیچ ارتباط عملیاتی یا تجاری با این هواپیماها ندارد و برایشان اهمیتی هم ندارد آن واسطه این هواپیماهارا به که فروخته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/16529" target="_blank">📅 23:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16528">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mfd5FomYQUa2Z4FgL2EpmBwrqaXidKHGRbyAlo7LpSbQlMKSBEXDnFHQL8Ra3tC8tysiFQnwnM5PoYU0z0yriWiayTFL2VRhHWjiAe7tulh8igLtWJmnu9FX_x6opuCaUuWCaP_Jkiezm6gj-55xybr2EvnLEvrHQqDzRfcsy81G20dw6zIQkJK9Jkth0SvV7PxQL5DvXmqduW1z9DYo-BijoQlaMPxvCF4SiOar56Q1OMXNVk00T7VDYGYc2fN2etq_0JLyB5u5LdCusEpIh8I_7FNOtbCc83-hl0lK7jLLR50iSuFoKpgr9X0dlqsbEPz0Cj6Kw81f2stghZFMEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ته مانده جمهوری اسلامی …
🗑️
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/16528" target="_blank">📅 23:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16527">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">صابرین نیوز: محمود احمدی‌نژاد، حسن روحانی، محمد خاتمی، محمدجواد ظریف و اسحاق جهانگیری در مراسم وداع رهبر شهید انقلاب شرکت نکردن
@withyashar</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/16527" target="_blank">📅 23:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16526">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کریستیانو رونالدو به گمانه‌زنی‌ها پیرامون آینده‌اش با تیم ملی پرتغال پایان داد و به طور واضح اعلام کرد که جام جهانی ۲۰۲۶ آخرین جام جهانی او خواهد بود. این بازیکن ۴۱ ساله فوتبال در کنفرانس مطبوعاتی پیش از این مسابقات گفت که قصد شرکت در جام جهانی بعدی را ندارد، اما تأکید کرد که هنوز قصد بازنشستگی از فوتبال را ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/16526" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16525">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یک مقام ارشد کاخ سفید گفت که دونالد ترامپ، رئیس جمهور آمریکا، در دیدارهای خود با رهبران در اجلاس ناتو در ترکیه، موضوع حفاظت از ترافیک دریایی در تنگه هرمز را مطرح خواهد کرد و خاطرنشان کرد که متحدان پیش از این تمایل خود را برای شرکت در این تلاش ابراز کرده‌اند. با این حال، وی گفت که بسیاری از آنها کشتی‌ها یا منابع لازم برای مشارکت در یک تلاش دریایی قابل توجه را ندارند. وی افزود که واشنگتن همچنان به متحدان خود فشار می‌آورد تا قابلیت‌های خود را تقویت کرده و در دفاع از خود سرمایه‌گذاری بیشتری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/16525" target="_blank">📅 22:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16524">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⚠️
ادمین کانال تلگرامی به نام کیان ملی در تاریخ ۵ خرداد(۲۶ می) دستگیر شد و  از تاریخ ۱۷ خرداد(۷ ژوئن) این چنل توسط افراد اطلاعات سپاه کنترل میشود و مطالبی ضد انقلاب شیر و خورشید منتشر میکند. به هیچ وجه به این چنل دایرکتی نفرستید و از آن خارج شوید.
⚠️
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/16524" target="_blank">📅 21:51 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

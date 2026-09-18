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
<img src="https://cdn1.telesco.pe/file/qjGSm_7rwnSNmYOJHtVnbYMhCO5LStcok0MSb6WQm4GWYnW7snzCC0HREB7hcRActfkqVWjLc1SZbVWRkH9IvuqnqXuM2dqVQnuckm9U5gtHI95q4t9wqJ-uj_weAajzxtvLOcWxR1K5gwOw8nPB2KgeBn7VWIUckIE6NIWIJnQUcIk1dBmxZ7kmT61SX6w_iX_APkhyGZaIf5gl77en7GF-xEPq4wawLAP3ykZU1xYndqUfqL-hXVjAFz8MlLB8NtJA21M5BnQjIgylshQNI6DYvVqz9_sj4kNw37zcphiBNW270Tva0vQg3upPN9_9yYiLdvVkbHTQPE0a4tGYJw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.4M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 22:49:51</div>
<hr>

<div class="tg-post" id="msg-78444">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29e74749d1.mp4?token=TPrzoF0Qzg8VNxkVfB_rmGcpQulVD5lrFe1HgjGdGJH9J3puboQ_wDyQ39vLgRrW3LZQNckLBybUgiPD7XarYLhU3vYkVcxYwBGleH8OofQXuTdIkoSvHb7NchQnHsIyykG_yv-Vi-HfT31KBofXtd5VY7LMxb3SUZ9z6Tu5iQTxl2FgNbXES6DcFQ1qb1gRROfef8ltcwYAexFQJ6Gt2EPozntK3Suhqtublks90X2bJaKVDEj5QnAYFwzOY_FypMmF0pm09Rt5zjzORdsS0szI6ArucYafMOHmIYYbNXQVHupPMkHOMOtvaL__PcIzvcZmqVVVqm1INDTwUE-ieQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29e74749d1.mp4?token=TPrzoF0Qzg8VNxkVfB_rmGcpQulVD5lrFe1HgjGdGJH9J3puboQ_wDyQ39vLgRrW3LZQNckLBybUgiPD7XarYLhU3vYkVcxYwBGleH8OofQXuTdIkoSvHb7NchQnHsIyykG_yv-Vi-HfT31KBofXtd5VY7LMxb3SUZ9z6Tu5iQTxl2FgNbXES6DcFQ1qb1gRROfef8ltcwYAexFQJ6Gt2EPozntK3Suhqtublks90X2bJaKVDEj5QnAYFwzOY_FypMmF0pm09Rt5zjzORdsS0szI6ArucYafMOHmIYYbNXQVHupPMkHOMOtvaL__PcIzvcZmqVVVqm1INDTwUE-ieQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌زمان با برگزاری
رزمایش "جان‌فدایان"
تصاویر بالا رو هم تولید کردند:
مسابقه دوی ۱۰ کیلومتر تهران روز جمعه ۲۷ شهریور با حضور گسترده زنان برگزار شد.
در تصاویر منتشرشده از این رویداد، زنان با پوشش‌های متنوع و اختیاری[تر از قبل] دیده می‌شوند.
رقابت امروز در «بوستان ولایت» و در دو بخش جداگان زنان و مردان انجام شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 201K · <a href="https://t.me/VahidOnline/78444" target="_blank">📅 16:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78434">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Yu6qga-vJG5_OR_2uejnUEo0jGKC9JMzgBPwS6oRzQae0HBs64UBV5MpI-HBam4HM6vuK-sGYNzPQew6MLun42pA9-0mlSgsQ2m8WdjuQ7kmru0NY9uAym1JtA-mUBNSpoPUj25hbqIxJff56_eOJCAU26wrUUrvW1TGyj60RVcm4hodZTQrfj_Y5xscPnUMhMQiJ2J7Ztgv8pYLqOJDAxbDqqNV2AHZfztOojyvKcrjjele76WDr1CO1DDeO5JXqe3_kTCPNFSRMmge_4pTogQfrq8THFEfvY4yKFKKLIsJdiYhX80fxPFrq2LRTUwVqxpvkQ3YvEwA8e3O85_tIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bMUv5y3F0hD4p71GHld9JmIPmsR2z-yPZcVrHb_zh_vBNPM4woNM0Cj0snEhQSShgFkl-NSthd3vTZtzj-ZqGCaXLyNus4dIN0dfq793FBE5v49U1lHPB3WyLU4-QmRm9NjDxhglVbraVjRk_L67-onYhCsB--lkwRAvmXwtoje_nOmYc89sfF1gCPZW_5RtK1kB3fW12NNRyHiFdRft2dlSPy98nu3gSbeAicHzVUZJHkqXip6fub0ZKFQP7Ou4K_W6vo3didnzCiZ9oYeaEMJEeJ_ieyB2i2Ck0wB74TWkD7f-ZdFqns_oBzwjMrEtmX6o4ol_c__VUq4AcZD-5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oFB2VZYIOwk0FBkoUYXkTsqmuU6E443TUuvm-a_cN6wrAQsuepOoG9EJKs-9ezYgDo8y_PZzM-SDNNjbuNJyYzIOSpcj5KHVfVv8jHm3g6JqKl1a4-ThiGvIsc6ZK0EMrFThxF4T6tcE2LsWEFZHF4umVcArkNf7rc8NfmTc2w9FCN7_hXqYxCEScbk2yKdjDq0laNBAVoOh0OQNj9tOVVdAkK1T4TyYmtjSqNWvXcoQQvdr7_3kzfv5D4fZ6yxzr9UXVKiN5CPWYPTxLxIew0qdRiiz_0t9qyTQhiiLCnHBi6Rr749dsfDCbMH_HTwto1EpmpBJo-ZfrLGw6ujt5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/epcJH3WWOv7o22ykXgyJDjSMEt8ypQDOMROsQqiQaCBpiUp3MiuhOvX9Va4fxUTZnRswhQ6RTaaEbpeMAqeMb4F7WjjZQcbmfQpc-iYBqqTdnZkIJTseg-N-WPfStBejRcQ5YG2Dj0dhSIwI-hMuua48iK2k_hSjveKm8wdD9ns8AfwsvbpFkT3_pLHZQmpLmv6RcKBPuNSslx5DjXV5VR1FkXkskm1rz4gPOSYWSbmEGDbG6jQW_P7rPws3V9NXBPrgWXmaM3hwAFB7pV1i30MEMI3z2XFnmCGxEykas4INhcTSQ79dwsrV1XMnTX5ngKI_nwoIRI-QJpr0Wa9lvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e40dc6c35c.mp4?token=pz5Culr2m5h_2L1wRDN51vgJvnrEBZNZbnLuw2EKVnDr0BDRwwgNGU40oAdMjm2BeDP_8-h_LYsQ6hV9wUgjlMcHJ3_Olv9NT6gouWCyhkaYnGekGnFuaXVA4ANOYPV6cxLivScVE0uXQGcg_nGDIR7ngkmimHrzD4Mv_dsfAqoiBUWjytVJ47TPTNYI9IKZ4umzqZOTjFmAJuiLG7KHJ5TPLfK-pEP0eKJUh9fj5DJAEvE4Ddi4gh_Tg7v2ayAGRWOtRnHNdfokaFU0Gq7x0rHELpqsv3X6xIJGgeg0bXcKE4_LB0ZlHkgtrJfwJ2rRchWhleBZD1yO9O1iF-0UXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e40dc6c35c.mp4?token=pz5Culr2m5h_2L1wRDN51vgJvnrEBZNZbnLuw2EKVnDr0BDRwwgNGU40oAdMjm2BeDP_8-h_LYsQ6hV9wUgjlMcHJ3_Olv9NT6gouWCyhkaYnGekGnFuaXVA4ANOYPV6cxLivScVE0uXQGcg_nGDIR7ngkmimHrzD4Mv_dsfAqoiBUWjytVJ47TPTNYI9IKZ4umzqZOTjFmAJuiLG7KHJ5TPLfK-pEP0eKJUh9fj5DJAEvE4Ddi4gh_Tg7v2ayAGRWOtRnHNdfokaFU0Gq7x0rHELpqsv3X6xIJGgeg0bXcKE4_LB0ZlHkgtrJfwJ2rRchWhleBZD1yO9O1iF-0UXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین طائب، رئیس سازمان بسیج مستضعفین، اعلام کرد صدها هزار نفر از ثبت‌نام‌کنندگان پویش حکومتی «جان‌فدا» در تهران سازماندهی شده‌اند و روند الحاق آنها به گردان‌ها و یگان‌های دفاعی جمهوری اسلامی آغاز شده است.
طائب روز جمعه ۲۷ شهریور در جریان رزمایش موسوم به «۳۱۳ هزار نفری جان‌فدایان ایران» در تهران گفت برای این افراد دوره‌های آموزشی مقدماتی و تکمیلی در حوزه‌های زمینی، هوایی و دریایی در نظر گرفته شده است.
این رزمایش از صبح جمعه در مسیر میدان امام حسین تا میدان انقلاب تهران برگزار شد.
@
VahidHeadline
حسین طائب، رییس سازمان بسیج، جمعه ۲۷ شهریور در همایش «جانفدایان ایران» اعلام کرد نیروهای آمریکایی «به‌زودی با شکست از منطقه خارج خواهند شد.»
رییس سازمان بسیج گفت: «جمهوری اسلامی از تمام ظرفیت‌های راهبردی و تنگه‌های دفاعی خود، از جمله تنگه هرمز، با قاطعیت حراست کرده و دشمن را وادار به تسلیم خواهد کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 197K · <a href="https://t.me/VahidOnline/78434" target="_blank">📅 16:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78433">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZizVrRMGHW2yppRLcET-x9hjVWRe1K-m9xeLHQO78waKmTJHsgKeKkSQFwd_sb5C3WY0L7S4OwxmXwdn3Jmt8V3Gtarer1D04psFCElPRjYDSwSpnuNTJn-wbY1CBZdiw32zKXyw-yoGW-dqt_M2c_3tzcHZXB0kVbRcOB1xFmYYEEybyYUTSe9TtUgjZaQ8CYLv6wk5HU0yP-88A0uoY6EDd4m8Pk8wGc8dfBjpJMUhJBGx2noX4yiVJZf4y4Ykc-GgPAektiZovGUYg2rcFJt7s9q2HHOvNr5SNxqf0b6fHOoAoaZ8y1ArCcVPs52J8-Yxc1-OQZI9tKOHhRcp2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور کره جنوبی اعزام نیرو یا تجهیزات نظامی به خاورمیانه را در صورتی که به مشارکت سئول در جنگ منجر شود رد کرد، اما گفت کشورش ممکن است برای حفاظت از کشتیرانی تجاری و انتقال نفت در منطقه نقش بیشتری بر عهده بگیرد.
لی جائه میونگ روز جمعه ۲۷ شهریور در یک نشست خبری گفت: «هیچ اعزامی که به ورود یا مشارکت در جنگ منجر شود، انجام نخواهد شد.» او تأکید کرد کره جنوبی برای چنین هدفی «به هیچ شکلی» تجهیزات نظامی اعزام نخواهد کرد.
او در عین حال گفت سئول باید مانند دیگر کشورها «حداقل اقدامات لازم» را برای حفاظت از کشتی‌های تجاری، انتقال نفت خام و امنیت شهروندان خود انجام دهد.
دولت کره جنوبی در هفته‌های اخیر در حال بررسی احتمال اعزام نیرو یا تجهیزات نظامی برای کمک به تأمین امنیت کشتیرانی در تنگه هرمز بود.
دونالد ترامپ، رئیس‌جمهور آمریکا، از سئول به دلیل آنچه حمایت ناکافی از تلاش‌های آمریکا در ارتباط با جنگ ایران خوانده، انتقاد کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/78433" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78432">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QY05ZUFhKQtUEEDPgyZbVeW7enfKO_XV3k4ZqCnlQtHLm2KIYG4Us4CXXXdIJBQw_CKRCYEMENvN3qFdgs5me38XCXHFrOYtfE_75uGu-tqCdL9KR1-u31VxCmOvy1o-YyCVqMcZThw4jXFM0l2H58tSS4tOC8Ilr1ZS6ZGce-NeAy8Zx7V9NhuJECyaKL5vrPGR58rztw7yeKgwQj_k9wz-ETzH2gmzH8XMI6pUMcBQCuntj3QGmbxoSxWl0bNE0fS2WXRpvnCRUsN8R9OgBoT0QiNDRKIwMMDmeLPvno3Ti1Q2KiAGoBajfV--IODgR1mkwMHHyYu-BtLE3qCiNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد یک نفتکش با پرچم توگو را هنگام عبور از تنگه هرمز هدف قرار داده و مدعی شد این شناور پس از اصابت و آتش‌سوزی متوقف شده است.
@
VahidHeadline
UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی درباره وقوع یک حادثه در تنگه هرمز دریافت کرده است.
افسر امنیتی شرکت (CSO) یک شناور گزارش داده است که یک نفتکش با پرتابه‌ای ناشناس مورد اصابت قرار گرفته و این برخورد باعث آتش‌سوزی در عرشه شده که اکنون مهار و خاموش شده است.
گزارش شده که همه خدمه در سلامت هستند و در حال حاضر تأثیرات زیست‌محیطی این حادثه تأیید نشده است.
UK_MTO
در گزارشی دیگر نوشتند:
مرکز عملیات تجارت دریایی بریتانیا (UKMTO) یک گزارش تأییدشده اما با تأخیر زمانی درباره حادثه‌ای دریافت کرده است که در ۱۶ سپتامبر ۲۰۲۶ رخ داده و طی آن یک نفتکش هنگام خروج از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
گزارش شده که خدمه در سلامت هستند. گزارشی درباره ارزیابی خسارات و تأثیرات زیست‌محیطی منتشر نشده است.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/VahidOnline/78432" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78431">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsNMfHSkokqtiyykg6_sW3f0AMRcujY5oitFDTudGB19XOA2WEWXXIBNPrgu2eC7EAaOQ20_qyF2lIVNos78K77pZ7sHu9-vsbHf_M6f6CroGn_PL00i_0IQEtNyrFOe-sf-XM1g_FURGz-YIt20a8__0XzK8-m_Oe01DNy0zCeIttR2sqJ8J8JYgoNZOQAQRif5N7Tcr5SOrEpVV3V30B7GTBz6HXC08_PKEqUVKQg_YH_Ms6G0vTQPKOGKB8PTjOYgNiJXf07USfuiAfB8atC3K9HTOSk5p1uMy0X7R9CSyAAIwWFpRxsMG2AgWvwozrZhjetOCaRy5fZysYLkPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد کرمی‌اسد، جانشین پلیس راهور فراجا از جان‌باختن بیش از ۱۶۰۹ نفر در تصادفات جاده‌های برون‌شهری در شهریورماه خبر داد.
به گفته این مقام فراجا، این آمار به‌طور میانگین به بیش از ۵۰ نفر در روز می‌رسد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/VahidOnline/78431" target="_blank">📅 15:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78426">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mw8gRf_aIrMXIbiz8ZPzwacm-a99nyzjd7dyLAFqIT6hzZhC0e9gdNVNT_oZkDnMgBuBNQPbkfjmYYod7nqWHNZ1Rge1CaBDYA0qDyTYamnDhHreCSUNOv3Dm-XBqEW1Yf5-nADn0L1mv7xQTMeE9V_-4-XtIkcXwvySQv5qTWS2EZWyPhlAudDfw57KLqVhAQ89VjNxfxPX36Sw3VcbuIol84hvQChvxWrI-7xY5OIceRWV1oLtHIyZkahY-Y60IrBJmC3JUDm1TjFZncxiepN4WXzF2HE_JEGF3-UFkGLw0lpDfFUBe2dikX-oiGqqCWhKQ6EmvYhwTAPHuhm_FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e616598ff4.mp4?token=OE7Y4azYEVUom0iHq7Qgc3FljqpEquiVU1YP8uwbX4487U1sPwHiDXPK-h5AjHKrYjcVzpmSKFkKuxkib0OeqWheIKJxiRiB5yG-LgXD1ujRIz10DpVa98yJL7jBHBlRefBoUxlMDaBc6B1SVjX42yO0kpDMi6r8YnEueb1wjBttFuNaDgPLgcL4E5oZIinJkOWXFqOPSbnBpJ5bcLn9qsWWZI8GUXKwlCGSjB1V8V7deJEW2NDWJH-yqMhweNT3nngRLFWep_dVpZ42yLXgB7Z6seWv7U1fk4Z1HWF1tSBipODO4fKRoPpo6IWzlqJmfv6tuROjSymO1Q9IguCyvg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e616598ff4.mp4?token=OE7Y4azYEVUom0iHq7Qgc3FljqpEquiVU1YP8uwbX4487U1sPwHiDXPK-h5AjHKrYjcVzpmSKFkKuxkib0OeqWheIKJxiRiB5yG-LgXD1ujRIz10DpVa98yJL7jBHBlRefBoUxlMDaBc6B1SVjX42yO0kpDMi6r8YnEueb1wjBttFuNaDgPLgcL4E5oZIinJkOWXFqOPSbnBpJ5bcLn9qsWWZI8GUXKwlCGSjB1V8V7deJEW2NDWJH-yqMhweNT3nngRLFWep_dVpZ42yLXgB7Z6seWv7U1fk4Z1HWF1tSBipODO4fKRoPpo6IWzlqJmfv6tuROjSymO1Q9IguCyvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با انتشار ویدئوها و تصاویر مختلفی در شبکه‌های اجتماعی از وقوع درگیری مسلحانه در بامداد جمعه ۲۷ شهریور در شهر زاهدان، خبرگزاری برنا از کشته شدن یک مأمور نیروی انتظامی در این درگیری خبر داد.
ساعتی بعد خبرگزاری فارس اعلام کرد که در جریان این درگیری دو نفر از مهاجمان کشته شدند و یک نفر از آن‌ها دستگیر شده است.
وب‌سایت «حال‌وش» هم که اخبار سیستان و بلوچستان را منتشر می‌کند، می‌گوید از حوالی ساعت ۳۰ دقیقه بامداد جمعه در محدوده خیابان دانشگاه و اطراف خیابان دانشجو زاهدان به مدت دو ساعت تیراندازی رگباری رخ داد و سرنشینان یک خودرو پژو ۴۰۵ هدف حمله قرار گرفتند.
این رسانه به نقل از منابع خود همچنین افزود در این درگیری «یک فرد مسلح، سه نیروی نظامی و دو زن رهگذر مجروح شدند و چندین آمبولانس به محدوده خیابان دانشگاه و اطراف خیابان دانشجو اعزام و در برخی خیابان‌ها ایست‌های بازرسی برپا شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/78426" target="_blank">📅 06:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78425">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3Qekq9icDmVgzAbWPi74UzNogNZLdzgoh3KV_oz7qJMtZTGOrp6M_bpjGpgt0vmOJOwMNPY1Ub5iX_8yhWGqBB0IEI5jHGMn4hCSG6qxU7UXzUV0BhjmXNVmR-9aeeKA4qsm5xMJP5W-h1CbMtoGu0h_Pd4tB6sNnk--W89PtbyUbMQJx9XqprfHdYzBmxTjEwu1vTCYWzfDMsByEjFn9udDiwRqRGd7RYFHQsdTwcjnphZdg6qDXPrScqFSZN8FYKAB_jPjtQAjaSplspkauU18d6mt-eV3XrCRhv2Mx-VZCONlLjWBtB-1EV-V7T8GO_pYLygb_rGJ7wASjYEiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران بامداد جمعه ۲۷ شهریور در بیانیه‌ای اعلام کرد نفتکش «ترند» با پرچم کشور توگو، شب گذشته هنگام تلاش برای عبور از تنگه هرمز هدف قرار گرفته و پس از آتش‌سوزی متوقف شده است.
سپاه پاسداران در این بیانیه گفت که این نفتکش قصد «عبور غیرقانونی» از این آبراه بین‌المللی را داشته و هشدار داده است شناورهایی که به این شکل عبور کنند، با «نابودی» روبه‌رو خواهند شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/78425" target="_blank">📅 02:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78424">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eQGZENOv__w246AKts-YnozSbxnbKmxvBPV2231hzPv1aPdThRLbyUcrXvlqyCoOjh_Lutv6belzI9ia05O2jzZzm9su7UKhrG5ATsof-CmjJCmnYWXTju8RxqpUfccFgmV4-YrWY-pRwaZgH1F1U9hGmjLT5934Bo-miu97ZclNHkdIyX_RJTNKdnOrMvrS6pddIcha-VfkO4Ro6e-YG0yi9s8kRpM6GJDGizh2VutGan1LvODTY4D8SHtmzbDlVR4bvdmf8SK59zq3yEuOJ5BY_ulWHFO3npBT-PqwqYwUQgZUQo8dmOMK31a0je4DPOsJMPk-oinyct0gTShIgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا  گزارشی از یک حادثه امنیتی در تنگه هرمز، در ۱۶ مایل دریایی شمال‌شرقی خصبِ عمان، دریافت کرده است. گزارش شده که خدمه در سلامت هستند. تا زمان انتشار این گزارش، هیچ پیامد زیست‌محیطی تأیید نشده است. مقامات در حال تحقیق هستند.
به شناورها توصیه می‌شود با احتیاط تردد کنند و هرگونه فعالیت مشکوک را به UKMTO گزارش دهند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78424" target="_blank">📅 23:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78423">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pOwhqOc-teV0kQAq89RxFed2CZ8jEKsg_xXkovCxAvT24GDE5LEjUjZCnfz8fjPrUi-QGXP1VcsgXHQGa2yfYL6KmxjjBPmET9b9kdp8jyCFBaG16BTZjw9b0JKLRj9hC8k9pyTdImpxPBmt0QqyUpyry_wX005IEbLWVdG54ef07R9cjXlGuNoiBByb97Hvr-w4Hj8BtapaQwwfFCAMQPoXZYZn8pkGrsP1LMZzIMg28su615bxmFa3nCdnJRH-wAtYGQgUlHNvUJtNFzaJv-yJGcMJtx2kBsH-mNor-wj_YDism_kOppeQmAecJxuJk_-7YILqJ-pyNyAL28sUfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس می‌گوید در جنگ ایران به یک دوراهی بزرگ نزدیک می‌شود
ترجمه ماشین:
رئیس‌جمهور ترامپ روز پنج‌شنبه به اکسیوس گفت که در جنگ ایران به نقطه‌ای حساس نزدیک می‌شود و باید تصمیم بگیرد آیا برای پایان دادن به درگیری، حملات گسترده را از سر بگیرد یا نه.
▪️
«تصمیم بزرگی پیش رو دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است. هر اتفاقی ممکن است برای من بیفتد.»
چرا مهم است:
اگرچه ترامپ پیش از این نیز تهدیدهای مشابهی مطرح کرده، اظهارات تازه او در آستانه دیداری برنامه‌ریزی‌شده در روز سه‌شنبه با رهبران شش کشور خلیج فارس در حاشیه مجمع عمومی سازمان ملل متحد در نیویورک بیان شده است.
▪️
این دیدار می‌تواند مرحله بعدی جنگ را شکل دهد، از جمله اینکه آیا بار دیگر برای دیپلماسی تلاش شود یا اقدامات نظامی تشدید شود. اگر ترامپ بخواهد عملیات رزمی گسترده را از سر بگیرد، به همراهی متحدان منطقه‌ای خود نیاز خواهد داشت.
▪️
رئیس‌جمهور در روزهای اخیر چند بار گفته است که جنگ به‌زودی پایان خواهد یافت. برخی مقام‌های آمریکایی هشدار می‌دهند که این درگیری به بن‌بستی ناپایدار و «نه جنگ، نه صلح» رسیده است و معتقدند اگر تا آن زمان توافقی حاصل نشود، ترامپ ممکن است پس از انتخابات میان‌دوره‌ای دوباره به عملیات رزمی گسترده روی آورد.
آنچه او می‌گوید:
ترامپ در این مصاحبه روشن کرد که می‌خواهد از نشست سازمان ملل برای شنیدن مستقیم نظر متحدان منطقه‌ای درباره گام‌های بعدی جنگ استفاده کند.
▪️
ترامپ گفت: «می‌خواهم بفهمم در چه وضعیتی هستند و اوضاعشان چطور است. ما خیلی از آن‌ها محافظت کرده‌ایم.»
▪️
کشورهای شرکت‌کننده عربستان سعودی، امارات متحده عربی، قطر، بحرین، کویت و عمان هستند.
▪️
ترامپ از گفتن اینکه تصمیمش درباره مسیر پیش رو را قبل یا بعد از انتخابات میان‌دوره‌ای خواهد گرفت، خودداری کرد.
زمینه خبر:
در اوایل اوت، ترامپ پس از آن از ازسرگیری عملیات رزمی گسترده خودداری کرد که عربستان سعودی و قطر ابراز نگرانی کردند ایران در اقدامی تلافی‌جویانه تأسیسات نفت و گاز عربستان را بمباران کند.
▪️
از آن زمان، ترامپ رویکردی «کم‌سروصدا» در پیش گرفته است: تعلیق مذاکرات با ایران، آغاز کارزار تازه تحریم‌های اقتصادی، ادامه محاصره دریایی بنادر ایران و متمرکز کردن ارتش آمریکا بر بازگشایی تنگه هرمز و افزایش جریان نفت به بازار جهانی انرژی.
▪️
ارتش آمریکا عبور نفتکش‌ها و کشتی‌های حامل گاز از تنگه را به‌طور قابل‌توجهی افزایش داده است. با این حال، ترافیک همچنان پایین‌تر از سطح پیش از جنگ است و قیمت نفت نیز همچنان بالاست.
وضعیت فعلی:
به گفته مقام‌های آمریکایی، ترامپ و پیت هگست، وزیر دفاع، به ارتش دستور داده‌اند سطح نیروهای خود در خاورمیانه را تا پایان سال حفظ کند تا برای احتمال بازگشت به نبرد تمام‌عیار آماده بماند.
▪️
این مقام‌ها می‌گویند ترامپ باید به‌زودی درباره مسیر پیش رو تصمیم بگیرد، بخشی از دلیل آن این است که ارتش آمریکا نمی‌تواند خیلی بیشتر در وضعیت فعلیِ انتظار باقی بماند. یکی از این مقام‌ها گفت: «بالاخره در مقطعی باید تصمیم بگیرید که هدف نهایی چیست.»
▪️
ترامپ به اکسیوس گفت از اینکه محاصره دریایی مانع صادرات نفت ایران شده، بسیار راضی است. او گفت: «از وقتی شروع کردیم، حتی یک کشتی هم به ایران نرفته است. تلاش کردند و ما آن‌ها را منفجر کردیم.»
▪️
رئیس‌جمهور افزود که ایران مستقیماً با آمریکا در تماس است و گفت ایرانی‌ها همچنان خواهان دستیابی به توافق هستند.
تصویر کلی:
کاخ سفید همچنین در حال کار روی یک راهبرد پس از جنگ است که خواستار تلاشی منطقه‌ای برای مهار ایران و هم‌زمان گسترش عادی‌سازی روابط میان اسرائیل و همسایگانش است.
▪️
هرچند این طرح هنوز در مراحل ابتدایی تدوین قرار دارد، هدف آن هدایت رویکرد آمریکا در خاورمیانه پس از پایان جنگ ایران و در دو سال پایانی دوره ریاست‌جمهوری ترامپ است. دو رویداد بزرگ بر این برنامه‌ریزی سایه انداخته‌اند: انتخابات ۲۷ اکتبر در اسرائیل و انتخابات میان‌دوره‌ای آمریکا در نوامبر.
چه چیزی را باید زیر نظر داشت:
وقتی از ترامپ پرسیده شد آیا هفته آینده در نیویورک با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد، گفت: «شاید.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78423" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78422">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrMC9jfOOiFP3iQZajymI5yv6N-yQet0h0Q36Vk9ROLQc0JF1MbDOjLlw7Lc2qA89w17myfma6Xpi8aTCYhDGZg80any_Md_boY2gH8XM2Dxu7AZ_LRRgowtEo8ohz_V40uJiSYqbCT3P1GUDka6XGK27GT6YDAMw7PXVhGvazo_lto8QfqOcJLGNrSH6phgdCk943PCebW3LfhD2yr8RRG8WwK1DkKxSlkyT6TS7JLUyj_Qh5CY9wjKIlFtPnlqHSaGAMazcCnqZcafoHhPVTzG-hKl5N3huyC7dQ6J_cP0MkCcujjKHAfb4kAn2jirjidb0H8XfxHZld5ivaR3TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس نیوز پنج‌شنبه ۲۶ شهریور به نقل از مقام‌های آمریکایی گزارش داد نیروهای جمهوری اسلامی در روزهای اخیر دست‌کم دو پهپاد ام‌کیو-۱ آمریکا را سرنگون کردند.
مقام‌های آمریکایی که به شرط فاش نشدن نامشان با سی‌بی‌اس نیوز گفت‌وگو کردند، مشخص نکردند این پهپادها در کدام بخش منطقه سرنگون شدند و از کدام مدل ام‌کیو-۱ بودند.
این پهپادها برای ماموریت‌های اطلاعاتی، شناسایی و نظارتی طراحی شده‌اند و قابلیت حمل موشک‌های هلفایر را نیز دارند. سی‌بی‌اس نیوز نوشت این پهپادها در تنگه هرمز می‌توانند برای نظارت مستمر بر آبراه، رصد فعالیت‌های نظامی جمهوری اسلامی و شناسایی تهدیدها علیه نیروهای آمریکا و کشتیرانی تجاری به کار گرفته شوند.
بر اساس گزارش دفتر بودجه کنگره آمریکا، از آغاز جنگ آمریکا علیه جمهوری اسلامی دست‌کم ۲۴ پهپاد ام‌کیو-۹ ریپر به ارزش تقریبی ۷۲۰ میلیون دلار از دست رفته‌اند. یک پهپاد ام‌کیو-۴سی تریتون به ارزش حدود ۱۵۰ میلیون دلار نیز منهدم شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/78422" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78420">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X93wLR1J3cWiy6XovazHW3uil2E2w2QbJyiIM04rLQrKZsi7yOhOddl4MoiCiQg6_iZno5ViT9X-DboR71rTeDZISe_nkxhtqftIif4Q0dmbfTcRVQWcQcBCLoE0KCBaTq7Ja3ORtt8gn0CcaiRuaALuqgB7LQ_Z1JnhR-4kri97qFCqE8RYxKOHAkVDrPGncDiVokESlgqX4_yAM8UTvANs1pH4pxj3FvOLYr2fXoomcM4iwER-wBbB5_VsCsjaj2CD0qVjYbaIOBKiqpPL4OpjBkzOxyTTfrwfCOKTGuuw-tsf2h9EbhlH3pINMVaJLlRLHdhWgm9560PVHTGjWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37ae7c8ac7.mp4?token=H5TtkAzEQ1DAeO1XVieKcLR5NfwwZRvuHXvfu5Y71zEsTNkNqiKIivxBoirF43-J1M8araUaH9tK75QInKOGEjAqbLi6oy1S_l5eWrLJDnquatujmgir_hcL1YZHHW0KuLhNwTbFsdlj3FvcIanfs3M6kfoGUrWaHQculLk3mXJvND8aho9xvjyxcxHbCD7wxrNXCe041oTTbHeWQyiYt2CjZGSVn2Uu9Kl6jlU-AVDfkTLGgOYMHkceeATMjhFboiudoAkYEYiMwg_awFMOf9BC4KGoARGoGXFK_sK4U6ugi451FRPFqRaxuubRWZzsLA9RGaMLuYPfr5j8x4idNg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37ae7c8ac7.mp4?token=H5TtkAzEQ1DAeO1XVieKcLR5NfwwZRvuHXvfu5Y71zEsTNkNqiKIivxBoirF43-J1M8araUaH9tK75QInKOGEjAqbLi6oy1S_l5eWrLJDnquatujmgir_hcL1YZHHW0KuLhNwTbFsdlj3FvcIanfs3M6kfoGUrWaHQculLk3mXJvND8aho9xvjyxcxHbCD7wxrNXCe041oTTbHeWQyiYt2CjZGSVn2Uu9Kl6jlU-AVDfkTLGgOYMHkceeATMjhFboiudoAkYEYiMwg_awFMOf9BC4KGoARGoGXFK_sK4U6ugi451FRPFqRaxuubRWZzsLA9RGaMLuYPfr5j8x4idNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز پنجشنبه ۲۶ شهریورماه در مراسم تقدیر از کارکنان برگزیده شاباک در بیت‌المقدس گفت اسرائیل بخش عمده ماموریت خود در برابر جمهوری اسلامی و گروه‌های متحد آن را انجام داده، اما این ماموریت هنوز به پایان نرسیده است. او گفت توانایی ایران و متحدانش برای آسیب رساندن به اسرائیل به‌شدت کاهش یافته است.
نتانیاهو با اشاره به ادامه عملیات اسرائیل گفت: «هنوز کارهایی برای تکمیل باقی مانده است و ما آن را به پایان خواهیم رساند.» او سپس تاکید کرد که اسرائیل حماس را از بین خواهد برد و در مورد جمهوری اسلامی گفت: «حکومت ایران را شکست خواهیم داد. آن را سرنگون خواهیم کرد؛ سرنگون خواهد شد.» او همچنین گفت اسرائیل به اقدامات خود علیه حزب‌الله ادامه خواهد داد.
نخست‌وزیر اسرائیل همچنین گفت خواست ایران و گروه‌های متحدش برای نابودی اسرائیل از بین نرفته، اما به گفته او، توانایی آن‌ها برای تحقق این هدف به‌شدت تضعیف شده است. این اظهارات در مراسم تقدیر از کارکنان برگزیده شاباک برای سال ۲۰۲۵ مطرح شد که با حضور اسحاق هرتزوگ، رئیس‌جمهوری اسرائیل، و داوید زینی، رئیس شاباک، برگزار شد.
@
VahidOOnLine
یسرائیل کاتز، وزیر دفاع اسرائیل، در شبکه اجتماعی اکس نوشت کارزار نظامی اسرائیل هنوز پایان نیافته و این کشور «اهداف مهمی» در برابر ایران و جبهه‌های دیگر دارد.
او گفت اسرائیل برای دستیابی به این اهداف «با قدرت نظامی و تدبیر سیاسی» اقدام خواهد کرد.
کاتز روز پنجشنبه ۲۶ شهریورماه با اشاره به غزه گفت سیاستی که همراه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دنبال می‌کند بر سلب توانایی گروه‌های جهادی برای حفظ قلمرو، زیرساخت‌ها، فرماندهان و تجدید قوا متمرکز است. او افزود اسرائیل این رویکرد را در غزه، لبنان و شمال کرانه باختری اجرا کرده است.
وزیر دفاع اسرائیل همچنین گفت این کشور فرماندهان «سپاه فلسطین» در ایران را هدف قرار داده و اجازه نخواهد داد ایران یا هیچ طرف دیگری حماس را دوباره مسلح کند. او تاکید کرد اسرائیل به عملیات خود برای تحقق اهداف امنیتی و جلوگیری از تکرار حمله‌ای مشابه هفتم اکتبر ادامه خواهد داد.
کاتز همچنین رجب طیب اردوغان، رئیس‌جمهوری ترکیه، را خطاب قرار داد و گفت اگر می‌خواهد به همفکرانش در غزه کمک کند، می‌تواند آن‌ها را به آنتالیا دعوت کند، اما «قدم به غزه نخواهد گذاشت».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/78420" target="_blank">📅 21:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78419">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D464MfHi6ZhPUSi7RGBDOgwWlsgP_v4nbBs0AlCu3tncVM-07wxwNWkiFVvXw8fz4bq3hSe4KonxCiVgeW15X53gTcLcUIGPfCOfra6uBbSnhIOXgbYoDENBE-Pitmp4Qb9m2QWJzCvgAVCQeO8Fnb1TO9QmSq_F1DZQ5fZ5IXq4IoZOc5bLGWaLtEZHyEEmrcOZj-DTd3roQTSx9ELJTJZs0gcrQRKvnATcO9yyytONBMJ4z-oNItIG3y_UwL1KebsBy8-w1wSqZG1L0PSXF9X9J-cNZtwAjXbCo1hG_6-mUsQRGI5_q9QO_CUsJTB_cmpsUZaLfkFFa8fhGJdAQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیات حقیقت‌یاب مستقل بین‌المللی سازمان ملل درباره ایران در تازه‌ترین گزارش خود اعلام کرد دلایل معقولی برای این باور وجود دارد که آمریکا در جریان جنگ با جمهوری اسلامی، در دو حمله هوایی به ایران مرتکب «جنایت جنگی» شده است. بر اساس این گزارش، این حملات دست‌کم ۱۷۸ غیرنظامی، از جمله زنان و کودکان، را کشت.
این هیات در گزارشی که به شورای حقوق بشر سازمان ملل ارائه شد، حملات آمریکا و اسرائیل به ایران در ۹ اسفند ۱۴۰۴ را بررسی کرد و به این نتیجه رسید که آمریکا در دو مورد حملاتی بدون تمایز انجام داده که به کشته یا زخمی شدن غیرنظامیان و آسیب به اماکن غیرنظامی منجر شده است.
بر اساس یافته‌های هیات حقیقت‌یاب، در یکی از این موارد، موشک‌های تاماهاوک به دبستان شجره طیبه در میناب اصابت کردند. این هیات اعلام کرد این مدرسه به وضوح قابل شناسایی بوده و در این حمله بیش از ۱۵۰ نفر، از جمله حدود ۱۲۰ کودک، کشته شدند.
در موردی دیگر، آمریکا با استفاده از موشک‌های تهاجمی دقیق، ساچمه‌های تنگستن را بر فراز یک مجموعه ورزشی و منطقه مسکونی در لامرد پراکنده کرد. بر اساس گزارش، این حمله ۲۲ زن و مرد غیرنظامی را کشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/78419" target="_blank">📅 21:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78418">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilQLjfQD6L_hW1MxZss8TRSCCeiBFzXxTIyADpV7f0YyRwLnS2JpdKFny3UjN9tt0Mu45AP0AGzzC-_Ge_hwEcXgfc7SslhG72WzJQo29lCM9TGe6iT_NaXlETcvfkDcDnn71BSOOc7Wue9ierqxJfBNYgI0KQkrBYa4dN21LmENPv4AFnOSY_YHuo8X6EwFph9b1RLbTdMCd5kF3WvY8u8zLvIkRmYrMAjAg6NFoW3HmU13grs2S4-qbYsE_MBaA_zQm3nB9dPxM-p_2dw0w6UTt3q7GGiCUltSENiYMwjZXP39XWlFPxp3leY4i1lNv52a3huugePNLD4R4P8k1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه و چین روز پنجشنبه، ۲۶ شهریور، در نشست شورای امنیت سازمان ملل متحد، پیش‌نویس قطعنامه پیشنهادی ایالات متحده برای تمدید ماموریت هیات کارشناسان کمیته تحریم‌های ۱۷۳۷ علیه جمهوری اسلامی ایران را وتو کردند.
این نشست با ابتکار فرانسه که در ماه سپتامبر ریاست دوره‌ای شورای امنیت را بر عهده دارد، در چارچوب دستورکار «منع اشاعه» برگزار شد. در جریان رای‌گیری میان ۱۵ عضو شورای امنیت، این قطعنامه ۱۱ رای مثبت کسب کرد، اما با مخالفت صریح (وتو) مسکو و پکن و همچنین رای ممتنع پاکستان و سومالی مواجه شد. برای تصویب یک قطعنامه در این شورا، علاوه بر کسب حداقل ۹ رای موافق، وتو نکردن اعضای دائم الزامی است.
دیپلمات‌ها پیش‌تر از مخالفت قطعی روسیه و چین با این طرح خبر داده بودند. مسکو و پکن معتقدند که با انقضای قطعی قطعنامه ۲۲۳۱ برجام در اکتبر ۲۰۲۵، تمامی سازوکارهای تحریمی پیشین از جمله کمیته ۱۷۳۷ فاقد هرگونه اعتبار و اثر حقوقی هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/78418" target="_blank">📅 18:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78417">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/caed21affc.mp4?token=aFDrLXyD9icESI4a1BKUSD-g2X4Ej5CSI7DwEiOqBFu8C8BQ7ifNVjzqLpBqav0o9-dy3WLa_WV-5jrVjROz3PSl43bof1g2va28mVXP-iOyEjRPlZDFTvPX5Osr0JZ09NcQo8ccZ8cCyn2WXvxof4P0687hJiYUZCPHyja6VhB2Jxncvp6gOSiX0Jt4w2aeITWJK3egZfqTQIv1eS2905DVuNJziXtojPoP0OWB3vQ66xT_hKmgihVaCWN_FpZbJ3y_aAQm-QbQjaoq0DRRtlB9cnKPYyhYkyqmKzhECOId3jmVdBvXa2Wc_nxjZ105pPLJlzYVabxfJMLG9G-jqw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/caed21affc.mp4?token=aFDrLXyD9icESI4a1BKUSD-g2X4Ej5CSI7DwEiOqBFu8C8BQ7ifNVjzqLpBqav0o9-dy3WLa_WV-5jrVjROz3PSl43bof1g2va28mVXP-iOyEjRPlZDFTvPX5Osr0JZ09NcQo8ccZ8cCyn2WXvxof4P0687hJiYUZCPHyja6VhB2Jxncvp6gOSiX0Jt4w2aeITWJK3egZfqTQIv1eS2905DVuNJziXtojPoP0OWB3vQ66xT_hKmgihVaCWN_FpZbJ3y_aAQm-QbQjaoq0DRRtlB9cnKPYyhYkyqmKzhECOId3jmVdBvXa2Wc_nxjZ105pPLJlzYVabxfJMLG9G-jqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">(
⚠️
خشونت و آزار جنسی)
ویدیو نشان می‌دهد ماموران فرماندهی انتظامی جمهوری اسلامی ایران یک نوجوان را مورد ضرب و شتم و آزار جنسی قرار داده‌اند.
این ویدیو خشم بسیاری از کاربران را برانگیخته است. برخی  گفته‌اند که «وقتی پلیس مقابل دوربین دست به چنین کارهایی می‌زند، معلوم نیست در بازداشتگاه و پشت درهای بسته چه به سر بازداشت‌شدگان می‌آورد.»
فرمانده انتظامی آذربایجان شرقی گفته که این اتفاق ۱۴ خرداد ۱۴۰۵ در جریان یک نزاع خیابانی در تبریز رخ داده است.
برخی هم با اشاره به انتشار این ویدیو در چهارمین سالگرد کشته شدن مهسا (ژینا) امینی در بازداشت گشت ارشاد، به تداوم خشونت پلیس در سایه نبود قوانین بازدارنده اشاره کرده‌اند.
پس از پربازدید شدن این ویدیو، فرمانده انتظامی استان آذربایجان شرقی گفت که ماموران حاضر در ویدیو «تنبیه انضباطی» شده‌اند.
علی محمدی به خبرگزاری فارس گفت که این افراد «تنبیه و انتظار خدمت» شده‌اند و «اقدامات تنبیهی تکمیلی» در مورد آنها در دست اقدام است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/78417" target="_blank">📅 17:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78416">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xw5M7__arRQ1kdwo6wR8zu8bAdxfqtWPlzjtjtGad3v1cAAOfiVZWyAsHOY5snVU1bcNpSkQTCT2FfFFM0OLSfjHwJpH-XC7Yq8LXO4V6Oz12lTKfCG9WDZperpUycD70XKJknzlJS9tat3g8N841IeLD5ZIM32IGeC75T0xB5WVOf9EMJtHxYDXKRccexiB4iPHlHNDBmncPTEarRn11J6Xp4K5sO0mVuNYZrrISnjpcLMOVFXKfAp8Zp3X8o5L3hK4TPHn9iuj3CkMUtMiV4AvpA0GADwvMiV4J6xA11V4o1PmD1J3RVi_BqucvK915EXwCFZT2JLv7JVxuTJCGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، مدعی شده است جمهوری اسلامی مستقیما با دولت او تماس گرفته و «بسیار» خواهان دستیابی به توافق با ایالات متحده است. او همچنین ابراز امیدواری کرده جنگ نزدیک به پایان باشد.
ترامپ بامداد پنج‌شنبه ۲۶ شهریور ۱۴۰۵، پس از ورود به ایالت کارولینای شمالی، در پاسخ به پرسش خبرنگاران درباره مرحله کنونی جنگ گفت: «امیدوارم به پایان جنگ نزدیک شده باشیم.»
او سپس درباره احتمال دستیابی به توافق با جمهوری اسلامی گفت: «آن‌ها می‌خواهند توافق کنند و خواهیم دید چگونه پیش می‌رود.» ترامپ در پاسخ به این پرسش که آیا پیام ایران از طریق میانجی‌ها منتقل شده یا تماس مستقیمی صورت گرفته است، گفت این تماس «مستقیم» بوده، اما درباره زمان، سطح و محتوای آن توضیح بیشتری نداد.
رییس‌جمهوری آمریکا ساعاتی بعد در یک گردهمایی انتخاباتی در شهر گاستونیا در کارولینای شمالی، بار دیگر گفت جنگ با ایران به‌زودی پایان خواهد یافت و «پایان واقعا خوبی» خواهد داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/78416" target="_blank">📅 03:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78415">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M5G8g75UUZDI0QnsvSbjhy1-j7EfCqc0jZtVKW0Rc0gye47LmbxDSyk07xSk0GYOpoYYC4blaGXDhKoCIWhJ3vnaSNZeDkivYyAusOmw8BIatczhJxPGl18DarhhYB9eNdDTk3jTzwwxSYXSTteo5w5dtSbq0u6d-XDGhi42cK5Y80JheFdwdhY6iR2SY-j4g9d3SSEzcFC6pZZw3HN8t57HqRmdqCoysayrM4cmZ4d-zA_Hl-NUJ3TdT3048Zzjr85MuRbeWJ0OjVy6Ivpk2BT8D5BArf4dVsIzfWwtDkMSrnFyDqOafqkUORpvJ8uQzdcfFXmC8FB75DyuPseosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت هواپیمایی ماهان چهارشنبه ۲۵ شهریور در اطلاعیه‌ای اعلام کرد پروازهای این شرکت در مسیر تهران-مسقط-تهران از ۲۶ شهریور، برابر با ۱۷ سپتامبر، تا اطلاع ثانوی لغو خواهد شد.
ماهان دلیل لغو این پروازها را اعلام مراجع هوانوردی عمان عنوان کرد.
این شرکت همچنین در اطلاعیه‌ای جداگانه اعلام کرد بنا بر اعلام مراجع هوانوردی ترکیه، پروازهای ماهان از ایران به مقصد ترکیه، شامل استانبول، آنکارا و بالعکس، از ۳۰ شهریور، برابر با ۲۱ سپتامبر، تا اطلاع ثانوی لغو خواهد شد.
ماهان افزود آخرین پروازهای این شرکت در مسیرهای تهران-استانبول، تهران-آنکارا و بالعکس روز ۲۹ شهریور انجام خواهد شد.
خبرگزاری عصر ایران نیز سه‌شنبه ۲۴ شهریور به نقل از یک منبع آگاه گزارش داده بود دولت گرجستان در پی تحریم‌های جدید آمریکا، پرواز همه شرکت‌های هواپیمایی ایرانی به این کشور را از دوشنبه آینده متوقف می‌کند.
عصر ایران افزود بررسی این رسانه از چند آژانس گردشگری نشان می‌دهد فروش تورهای گرجستان نیز تنها تا یکشنبه ۲۹ شهریور انجام می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/78415" target="_blank">📅 17:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78414">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DLn2g57B1SDJnTfcGffF7qKPFY_i1Y5qpzH-WOrTNjFEMnwMaisq4FDcaFRMgwIn5Lfkl_dZ4Nr0xGnAuK0NF6x-Z8f-_bmX-TktXCutM7kI7PD24rWeOkIN9rV_r3lwmlSloikeO6HNkcV-BeghUQ2mTjExeYyJE5Gc9hKY62I3DU2zoFJ08oWG9vMpQ4P9GhJfJqHJb0KH8-PhKIOClVPPx7RZ1dKkZ419Zj2j-Pige3sPQ14KO3Q7Q7bgyTlyJcimZ_yv7SvbEYwVmKsLSJ8baBLE4t_e7koNRnqwewaxGNZx5bfgjjGWEw1DvVVyR1ngzuPBgaE4Ic8xMbhMQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل قدیانی، زندانی سیاسی محبوس در زندان اوین، روایت جمهوری اسلامی درباره نقش «تروریست‌های وابسته به بیگانگان» در کشتن معترضان دی‌ماه ۱۴۰۴ را رد کرد و نیروهای حکومتی را مسئول «قتل عام» آن‌ها دانست.
قدیانی در بیانیه‌ای که روز ۲۴ شهریور از بند هفت زندان اوین نوشته، با اشاره به راهپیمایی ۲۲ بهمن و تجمعات حکومتی ماه‌های گذشته پرسیده است اگر عاملان تیراندازی به معترضان، آن‌گونه که حکومت می‌گوید، «تروریست» بوده‌اند، چرا در تجمعات حکومتی که در امنیت برگزار شده‌اند، اثری از آنها نبوده است.
او از رسانه‌ها و نهادهای حقوق بشری خواسته است درباره این تناقض در روایت جمهوری اسلامی پرسشگری کنند و نوشته است: «تروریستی در کار نبوده و نیست و قاتلان [...] همان نیروهای [...] حاکمیت‌اند.»
قدیانی همچنین در این بیانیه علی خامنه‌ای و پسرش مجتبی خامنه‌ای را مسئول این «جنایت سهمگین» دانسته و نیروهای حکومتی را به تیراندازی به معترضان متهم کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78414" target="_blank">📅 17:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78413">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIIbskmGHfoMjEiVGXBGzq-gUBIek8PrlVMwn83qG0lvbwps-SQXhd07zA5K3PuZhT89Y-QvSee2fl5SJeh8emoND_jMNalpXbwcwFYUFWLtGumtTLYZEOSoE4OM0QafGHI05YmQuoQ-rFfAqrERcGDKSHHGK0A_6H8Un50GaP71LLPoloZFcpHPD7Fie5z9-8dyGvuZaMqdAIf5Dn17HjySPs8ArJzxbmP_eCTon-SjUWnicCJIdisb-CmKzVT0gT4wBgNCep6NDG4yomX9LTfzU7HZKQLqtEHvCyElN1aVOM4dhvt-SOJYuZVpLTwXsEPu1lH8niDRnPEzJEHqIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین با صدور بیانیه‌ای اعلام کرد که وانگ ئی، وزیر امور خارجه این کشور، روز چهارشنبه در دیدار با عباس عراقچی در پکن گفت:
چین، ایران و ایالات متحده را تشویق می‌کند تا عقلانیت خود را حفظ کرده، خویشتن‌داری نشان دهند، به یادداشت تفاهم اسلام‌آباد بازگردند و «در گفتگوهای ماهوی درباره مسائل مورد علاقه طرفین مشارکت کنند.
براساس این گزارش، وانگ با بیان اینکه چین «نمی‌خواهد شاهد سرایت بیشتر تنش‌های منطقه‌ای به یمن و دریای سرخ باشد» افزود: «ما از همه طرف‌ها می‌خواهیم اقدامات موثری برای بازگشایی هرچه سریع‌تر تنگه هرمز انجام دهند.»
وانگ همچنین گفت که سیاست چین در قبال ایران همواره ثابت و پایدار بوده و چین مایل است ارتباطات و هماهنگی‌های خود را با تهران تقویت کند.
@
VahidOOnLine
عباس عراقچی، وزیر خارجه جمهوری اسلامی، چهارشنبه، ۲۵ شهریور در سفر به پکن با وانگ یی، وزیر خارجه چین، دیدار کرد و بر گسترش روابط تهران و پکن در چارچوب مشارکت جامع راهبردی تاکید کرد.
عراقچی شرایط کنونی منطقه را ناشی از حملات نظامی آمریکا و اسرائیل به ایران دانست و از مواضع چین در محکوم کردن اقدامات این دو کشور قدردانی کرد.
او گفت: «جمهوری اسلامی ضمن آمادگی کامل برای دفاع مقتدرانه از حاکمیت ملی و تمامیت سرزمینی و صیانت از امنیت و منافع ملی ایران در مقابل متجاوزان، از راه‌حل‌های دیپلماتیک که حقوق ملت ایران را تامین کند، استقبال می‌کند.»
عراقچی همچنین گفت شرایط منطقه پس از جنگ ایران تغییر کرده است و در نظم جدید منطقه‌ای که با گفت‌وگو و همکاری کشورهای منطقه همراه خواهد بود، جایی برای حضور و دخالت نیروهای خارجی وجود ندارد.
او با اشاره به آنچه نقض مکرر تعهدات از سوی آمریکا خواند، گفت جمهوری اسلامی خواهان بازگشت آرامش به منطقه و روابط دوستانه با همسایگان است و در همین راستا گفت‌وگو با کشورهای منطقه را آغاز کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/78413" target="_blank">📅 17:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78412">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MNmUshLrGVrTjTPRItdoDukHWm2jaqkpXZ5HAWCTnGMQhievbhTAnXsomxC-8VylKT3WGoZvoqvxbPL3L4actxevWTE-Pzc3_nyyzX1FlfLbutf3aR0lJQcbqFk0KBhSrJH7lf2pY6khYT_Ahfh_rk8OZFVolbWuh4YwVhXJ6d_zLx07f0QDF77z00ySzakcnf0JXYI5NtufBveF7SHb6YwfsluUmnswmNvoOC-1RlMaVUG46l2Zx1cjeFibmw_ljmyRAeu99R_a2KrxXdGeQOzUQvfspZBQfXFj7UIpaKHc4gJkJ1-1DWW4BvW4GdHQv3h0mYzdQ9A8Gzdbu_rezg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز روز چهارشنبه ۲۵ شهریورماه به نقل از پنج منبع آگاه گزارش کرد که مقام‌های ایالات متحده آخر هفته گذشته (روزهای شنبه یا یکشنبه) با نمایندگان شورشیان حوثی مورد حمایت جمهوری اسلامی ایران، دیدار کرده‌اند.
براساس این گزارش سه تن از این منابع که خواستند نامشان فاش نشود گفتند این دیدار که رسانه‌ای نشده بود، در سفارت آمریکا در مسقط برگزار شد. دو منبع دیگر نیز اشاره کردند که دولت عمان، به عنوان میانجی باسابقه منطقه‌ای، به برگزاری این نشست کمک کرده است.
دونالد ترامپ در سال ۲۰۲۵ و پس از بازگشت به قدرت حوثی‌ها را در فهرست «سازمان‌های تروریستی خارجی» قرار داد و هرگونه حمایت از این گروه را جرم‌انگاری کرد.
ترامپ روز شنبه گفت حوثی‌ها با دولت او تماس تلفنی داشته و از ایالات متحده خواسته‌اند از جنگ یمن دور بماند. جی‌دی ونس، معاون رئیس‌جمهوری هم روز دوشنبه بدون ارائه جزئیات تاکید کرد که ایالات متحده در تماس مستقیم با این گروه است.
دو منبع آگاه اعلام کردند در این نشست که به گفته یکی از آن‌ها روز یکشنبه برگزار شد، حوثی‌ها به مقام‌های آمریکایی گفته‌اند قصد حمله به شناورهای آمریکایی را ندارند و به آتش‌بس سال ۲۰۲۵ با آمریکا متعهد هستند.
یکی از این منابع که یک یمنی است، گفت این گروه همچنین اعلام کرده‌اند که به کشتی‌های اسرائیلی یا هرگونه کشتی تجاری دیگر، به‌جز کشتی‌های متعلق به عربستان سعودی، حمله نخواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/78412" target="_blank">📅 17:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78411">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlE_KsfOdjafwCepo64eaHcf9s8CklygUVP0uNUkucMl5XFYfHHadf4j0dpIFRCSdgsawR00L8TwIgMM2rokHpd_Mmt4RYFxE3-iRYN37GNwHBSrfZRf8ysxIi_ae7QhtZR8iHmX5hGWVbgNOA3PjoeJVz7-gO2VX5FCSC8AZUwFQyxY5ho3zpuoMndIjFd8KhW1xH0sFgwuWvLmQVLsSTfcg6yXZrQwnIU3rPKjjaJ0ivcpFyamWna6-VUxZowvnn38miCMyODodd5eG25HrerkcIJEsIchQuYarJCTA6X_o8pYCXsb8CywRjea4XHP0bLmQbhxNcklrcah6tFDOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«جی‌دی ونس‌»، معاون رییس‌جمهوری آمریکا، گفته است جنگ با جمهوری اسلامی طی «یکی دو ماه آینده» وارد مرحله‌ای کاملا متفاوت خواهد شد و واشنگتن در مرحله بعدی باید مانع بازسازی توانایی‌های هسته‌ای و نظامی حکومت ایران شود.
ونس همچنین با پیش‌بینی «دونالد ترامپ» همراه شده است که جنگ پس از انتخابات میان‌دوره‌ای آمریکا پایان خواهد یافت؛ هرچند توضیح نداده منظور از «مرحله متفاوت» تشدید عملیات نظامی، کاهش درگیری‌ها یا آغاز روندی دیپلماتیک است.
معاون رییس‌جمهوری آمریکا در گفت‌وگو با نیویورک‌پست که روز سه‌شنبه ۲۴ شهریور ۱۴۰۵ منتشر شد، گفت: «نمی‌توانیم آینده را پیش‌بینی کنیم، اما فکر می‌کنم رییس‌جمهوری درست می‌گوید که این مسئله طی یکی دو ماه آینده وارد مرحله‌ای کاملا متفاوت خواهد شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/78411" target="_blank">📅 17:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78410">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CGYn_oi0e2-0LJoVPp-buNqokrJR3hwF1l4pcM_73xmRXss_kF5VRXlUsgi2CEEHN6w_xw0WIhDl8_V9pspr6bmZkXMf7QptUK-ND-ZXpD6-qDmfxh2qonsDWrdRx3AYNw6sb4x4JkXtB3RX49BqhHAqCHGTV8kFYj0kizLAo8IgisKaHeeeZ2ulv5YgfLMT6aY3GUUOTonqDsg8RIagAzM7evqsI1vK9CKS3hHpryj8HQjYfLkCOsIocKkXboNnhXKjO36d0y0MN-VP4YSdyKhrfUI2zeO1IJ27R3AOAjNO53I3h-ydLyOhD8Ck-S-Twx8C5fcVuigrTv_1cUnoiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین قشقایی، همسرش سارا شمسایی و ابوالفضل قشقایی، برادر حسین، از معترضان دی‌ماه، پنجشنبه ۱۹ شهریور بازداشت شدند.
حسین قشقایی و سارا شمسایی در لاهیجان به دست نیروهای وزارت اطلاعات بازداشت و به اراک منتقل شده‌اند.
محل دقیق نگهداری آنها مشخص نیست و احتمال می‌رود در بازداشتگاه اداره اطلاعات اراک باشند.
ابوالفضل قشقایی نیز همان روز در زرندیه ساوه بازداشت و به اراک منتقل شد. به گفته یک منبع مطلع، ماموران هنگام بازداشت با خشونت وارد منزل شدند و گوشی‌های تلفن، تبلت و لپ‌تاپ اعضای خانواده را با خود بردند.
حسین قشقایی با اتهام‌هایی از جمله «فعالیت تبلیغی علیه نظام»، «اغوا و تحریک به جهت برهم زدن امنیت کشور به جنگ و کشتار»، «نشر اکاذیب در فضای مجازی» و «اجتماع و تبانی علیه امنیت ملی» روبه‌رو است.
درباره اتهام ابوالفضل تاکنون اطلاعاتی به خانواده اعلام نشده و پرونده این سه نفر هنوز به شعبه‌ای ارجاع نشده است.
از دی‌ماه، سیم‌کارت‌های حسین و سارا و حساب بانکی حسین نیز مسدود شده بود. آنها ماه گذشته به دادسرای عمومی و انقلاب زرندیه احضار شده بودند، اما در مهلت پنج‌روزه تعیین‌شده حاضر نشدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/78410" target="_blank">📅 17:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78405">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fe85f5293.mp4?token=Klb6jxPWqvVBpqTMI0jNEvU7sXe3jb3gVtV48m5M-W-ZtfzXmtMgfqZfGEthexyoJDBziKkIZHTLp98MAPe3O15gpvgIdVVKJxXE-v7p2fEYJACfCK37N1SOfE0aBj6pBQP4ZPiqgmH__bY98yNeX73IVl2D1tBA6gT7Fzj_TsncNioU2CTVKDNJc-uTdSrnze_CX8Udtieia4JlA86ztLZEHH-UPaP9NY57Nghp2Dq_m9Xf-LWV4r6vu3PM_By4v_RAoN97IIfpiHd-TE_UXqCdA_Dk4BmDbbpnj12UcH4dGYkB5slbFGBwpPnuWenDGq4H2ff_Z26fAEUc7-O__3xirlmpbcJKRBc-_9GQi5OzU_N_TxSzKjmmj5tTr6-_YLU-rqATS4axqMMM5C1I59yGSWr6T1c8vs2NoxY-UxNIewJeI5jBO7yZi0nk3BAJtaF6SuKinSl1zRhqCLZ3ecIyo1dl6WmzPRdhORcoDge2oj-SH4wsVH9QG7-o4xhYf0nV1CdrYYHOBcqK5S8RBfxyDKIb9T3-aIVE-kcaP1KTQ9-uP_FaDiwf_r-8eUwPobOIRubqIQ_5EpCtmibMbc3T0NY-xmRzmqSoCti4i2xu41i0pE6sP6JK462uI5oIP75alLq1ie-eaFcf9qDcK90mcA_FisPuZRsmii4t3w8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fe85f5293.mp4?token=Klb6jxPWqvVBpqTMI0jNEvU7sXe3jb3gVtV48m5M-W-ZtfzXmtMgfqZfGEthexyoJDBziKkIZHTLp98MAPe3O15gpvgIdVVKJxXE-v7p2fEYJACfCK37N1SOfE0aBj6pBQP4ZPiqgmH__bY98yNeX73IVl2D1tBA6gT7Fzj_TsncNioU2CTVKDNJc-uTdSrnze_CX8Udtieia4JlA86ztLZEHH-UPaP9NY57Nghp2Dq_m9Xf-LWV4r6vu3PM_By4v_RAoN97IIfpiHd-TE_UXqCdA_Dk4BmDbbpnj12UcH4dGYkB5slbFGBwpPnuWenDGq4H2ff_Z26fAEUc7-O__3xirlmpbcJKRBc-_9GQi5OzU_N_TxSzKjmmj5tTr6-_YLU-rqATS4axqMMM5C1I59yGSWr6T1c8vs2NoxY-UxNIewJeI5jBO7yZi0nk3BAJtaF6SuKinSl1zRhqCLZ3ecIyo1dl6WmzPRdhORcoDge2oj-SH4wsVH9QG7-o4xhYf0nV1CdrYYHOBcqK5S8RBfxyDKIb9T3-aIVE-kcaP1KTQ9-uP_FaDiwf_r-8eUwPobOIRubqIQ_5EpCtmibMbc3T0NY-xmRzmqSoCti4i2xu41i0pE6sP6JK462uI5oIP75alLq1ie-eaFcf9qDcK90mcA_FisPuZRsmii4t3w8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی فراخوان ائتلاف نیروهای سیاسی کردستان ایران، همزمان با چهارمین سالگرد قتل حکومتی مهسا ژینا امینی و آغاز جنبش «زن، زندگی، آزادی»، کسبه و بازاریان شماری از شهرهای کردنشین اعتصاب کردند و مغازه‌های خود را بسته نگه داشتند.
از صبح تا ظهر چهارشنبه ۲۵ شهریور، اعتصاب و بسته بودن مغازه‌ها و بازار در دست‌کم ۲۰ شهر، از جمله ارومیه، اشنویه، بانه، بوکان، بیجار، پاوه، پیرانشهر، ثلاث باباجانی، جوانرود، دیواندره، روانسر، سقز، سنندج، قروه، کامیاران، کرمانشاه، کرند، مریوان، مهاباد و میاندوآب گزارش شده است.
@
VahidOOnLine
وب‌سایت‌ها و منابع خبری مختلف که اخبار کردستان را منتشر می‌کنند، از جمله هانا، کردپا، کولبرنیوز، زاگرس ۲۴ و شبکه حقوق بشر کردستان نیز گزارش‌ها و تصاویری از تعطیلی مغازه‌ها در شهرهای مختلف کردنشین منتشر کردند.
در همین حال تصاویر و گزارش‌های مختلفی از برقراری فضای امنیتی شدید و استقرار نیروهای نظامی و انتظامی با سلاح‌های سنگین در شهرهای مختلف کردنشین منتشر شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/78405" target="_blank">📅 17:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78399">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b6m5YOeYvCmDtRTgP2ViWxjwV1bCmUWl8B8E0T5nyILzXK-qNVQEsyFlQj9LmBWHGjtffWhzEgQwOgEORo4B7Z_Hj37b1-r3OMZdLerP8I7XonfUWHdzafu43zM6F4zb4xYdoReIZlh7w1t0LxRC7UtHBNfbtWMsNXQfOVL6qqZF9mnrn2DKMgfGJRgANXdS91qlLYYfuMXhJ64VoDihd9Oi5eAmAcSp7w43O2ZBb5i35joJimrOKYQPTe_PG3ce7KVJeIlYawPoDxuhjflRxjAd5P4UpKSyK1vayQALFKnKX5AdNy5ewmnO_xvyxI45PQAED3Bx6geoYACQfFEPKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sUrIrUFXBeLVlBk7fTSVD0ENiPVe3y-D2poECjhBFrrsuRudpqLKxuKf4fMWPGqWiMdVoZqMID7yhW_wYlqnweCU4PAj6lnRnPiRojyqZC1FD7bMj-m_RdqfgCX0QtJ5t5rWRx-ZSAjbQmeYfw8VmOYAay5kgydHwprfBa22vb_ng1IjQwSA8TV3mdfIGrqWQb8oWxTD1mAxWhTGQF9HoYiIyBoqmA3hVkvpuAVH7RLLtydriTqneIbFW81Y0co6aa1YdVnL4J03IsXDLgMT38e0dnT7CGPhlOprIVDMKf3KCkH88jZHj2wTkNc0kBvDfBOLTLIKcSuRUq16P2v4jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NiObqe8rrsJdL-rE5LfFeCyc88biqNnVymlMGTAdu9MrS9GflO0zn-JtPXFAFT-RNLi8jzv0pRCYmWGh5CvGSt-JQzZocBAmtzHrLK01jLCFsokvRLwsfGWe-flh9Ar8aB_RC7rcpYLLWIJFWYZEZnAQjckgl7xrP6Y3Zxp5sz86QyScwKjnEKaW3Qpv40N7LhlkFiikOl4vJ_HrCrtF3ekCTgnDctN2jslv-1S4FY9I6uj0n0s0HHiTOhNY1Qm2pgyN5rjm05HKSwEMDvrHyim5qw7mhYG59HIRs4idQ85sKDMTNYNdmV9TP3BNc-2BB2hm7ZAXnjpW46WqAKltBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cCelNVNR_i3shEB9Q4B7l3R5fqDXMTpRw72r8oP4aufEO2IU9GS3_8Ki5k3kcbbT_D1eQv5esurP-pwg9ji5QF5gfuy63st5xxo9FNx5fAAc-Nw6w9uVvs9UcJgpbkL66H8mZ8xNlzfpLUmlKeffkWwlAUf0MvxOMEGnw7aFkwT13g-seaFZFIFWgoSE2nsRWfJq6JfsWJR9FIGGc-aGBgFep44Tr5LmPPXVKl6t60rpE1h649ioUL_gWcVrFpqcx6mL951mkNpDikhRknxA0wa8E_ANJZXfYUjryLxvobGlTmhMLcaXS53ov1IsVzbaYegL_tVLxQrFbfZ0cSyucg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rUAvbcS8oCmqvq-SW0c3KN1oENW2yuI_WUwtfU9zusMIZqK2FWWXq52k9wTfgN4JOIxxqWpPp8PT6g0oCXQACCGbcXHhEruESbwKZEMTbUISYlfxyOsi4k6eVCKhodS_7Hj2Kz_IT1pL_Ymp7onOiZoG6w9dTMjExZ8PFqGZmN3AJ0J1wcuPV27fqFx78gFyBAFu8d3EdPjAJ3q-wfNfMPcrhKpdusyge6WZgDy0JJ2tRaxo0T9Gzm1MzVh5uGMKGosuhTc3-fadfPgtOVl66_AMN-u6zflSEZjs8q7CmT8bd7yhyFwpt4glbmAfvakPtrEUFQLZ1jnDS821w09xCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GGZvMX9ktJyZbuNC7QrRl3jkf-2JhRUV4lvpH8oP9E-RyP0qz2khjNTcoWX2qOKueIIJKpB4-sd3sX_aXo0_pOXCX0HmxfC_Kp46txc48gPpnRRw9OhwaHQOdVnqxuCV28JEwVwjzDC8MoSesGXoTrvt90uClrs7RnCAySud2pI7pFHEgGgrUGYL_8pGcPcgi8CwLhWAsSRuOsq8RHw3-PNOU3-ixyHDRxXL6bPj4QeVotep0HkWOLpmAbxDY2TzMSO-qKEYGkPhL56Mdjount55rtEhDeWaReVAVAp_N4LWzZaaYJH10Qow9O7DsQoaV3oWdE_iuOzFIGwA0TpyKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سی‌بی‌اس‌نیوز گزارش داد تصاویر جدیدی که به‌طور اختصاصی به دست آورده، برای نخستین بار گستردگی خسارت حملات موشکی و پهپادی جمهوری اسلامی به چند موضع نظامی آمریکا در خاورمیانه را نشان می‌دهد.
این تصاویر را نظامیان آمریکایی در اختیار سی‌بی‌اس‌نیوز قرار داده‌اند. یکی از آنها گفت خسارت گسترده به پایگاه‌های آمریکا به اطلاع مردم این کشور نرسیده است.
در تصویری از پایگاه هوایی شاهزاده سلطان در عربستان سعودی، یک هواپیمای چهارموتوره بویینگ ای-۳ سنتری دیده می‌شود که موشک به بخش عقبی آن اصابت کرده و دم هواپیما از بدنه سوخته جدا شده است.
تصاویر دیگری از این پایگاه، ساختمان‌ها و آسایشگاه‌هایی را نشان می‌دهند که بخش‌های داخلی آنها تخریب شده است.
سی‌بی‌اس‌نیوز همچنین از ثبت خسارت‌های مشابه در کمپ بوهرینگ در کویت خبر داد؛ پایگاهی که محل استقرار و آماده‌سازی نیروهای زمینی، خودروهای زرهی و شماری از هواپیماهای ارتش آمریکاست.
پنتاگون به درخواست سی‌بی‌اس‌نیوز برای اظهارنظر درباره این گزارش پاسخ نداد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78399" target="_blank">📅 04:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78398">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cF4DMEdrMMk_lzG2fZCbjA0fYRvLIZjCAkiYvWg69nNKbJuBl_kRVwfWiv4OezvRzAkMN2bdzaF8ME0UZi3TZZcAeaIJX6KMATpcMnfyHhosJZUhERNCKdc6NldGQr_ZL8ZR24kVpBQgmVZQ6CyFt9zVyPGfPqGKt9T2ACEJf7HJNe22zzXsiscj9H0tz7j7XW_QOZeMhVSIsjHIXJA9yq1eyCudykv4369JRh2FMzoRxEG5fbbuTCypdhQMxSF9FSSw87G_SDOi9zK5yIof4DC0qNld-e25W_jyhv_mPuTekugLcJpbQ70vH35_RMJJp_lWV680S3zl09bw9fUz8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی در یمن اعلام کرد پدافند هوایی این ائتلاف یک فروند پهپاد پرتاب‌شده از سوی حوثی‌ها را که قصد ورود به حریم هوایی مکه را داشت، رهگیری و منهدم کرده است.
به گزارش خبرگزاری رویترز، ترکی المالکی، سخنگوی ائتلاف، در بیانیه‌ای گفت این دومین تلاش حوثی‌ها برای هدف قرار دادن مکه بوده است.
به گفته ائتلاف، پیش از این نیز حدود ۹ سال قبل یک فروند موشک بالستیک به سوی مکه شلیک شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78398" target="_blank">📅 03:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78397">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r8iGxrB7DezDdI34zSlacFaogYc_NtO0Bfu-Wn2-Jt72BLfOojyYrF5EbIBrRcBf8w7qqXUZt_1mQY96Ck6EX_vkjuTMCkIrQSXkcBS4yElbzmTrJ_GZEJBrY7g8zpjSffPFSDCSvIKsw2AUlOh7pTxls4QpxBCOEitKnHkewQAVaNLR0w1naz5hbGUx_bPSTSvYKVxjP3vu3iX8QHlJzin_7D_sivdNtgNjJvGndpizd7JM_E2ZfOllOWd_Y7lG856Ky_U_mJjBMVfjR1DVxqNaTYar3hDjHwOGCYfIFAv5mAxOlgOW-_z8qQGoMkT1jg51kB717qFGI-K6gl_pZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از دو مقام اسرائیلی گزارش داد فرماندهان ارشد نظامی آمریکا، اسرائیل، عربستان سعودی، امارات متحده عربی، بحرین، کویت، قطر، اردن و مصر هفته گذشته در نشستی محرمانه در آلمان درباره جنگ با جمهوری اسلامی و تنش‌های منطقه گفت‌وگو کردند.
اکسیوس گزارش داد نشست محرمانه فرماندهان نظامی در آلمان به ابتکار برد کوپر، فرمانده سنتکام، برگزار شد.
به گزارش اکسیوس، برد کوپر در نشست محرمانه آلمان، فرماندهان نظامی اسرائیل و کشورهای عربی را در جریان برنامه آمریکا برای افزایش تردد کشتی‌ها در تنگه هرمز قرار داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78397" target="_blank">📅 21:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78396">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86139d3a31.mp4?token=b8BRXheFgzb2xf4zCJsoIfgMqP8hO7--qPqHyvpRRySe8evp4C1p1PWN8j2Zwxel9Nx94F9gKG33QECup5hkMLYFi0KqBa2jriE7Qib6e51Ttb4Nyn-B8ULcUUICq-nTB6s1NXxitaTZh88EJ1ujhlQCLmwDZ8mGHyIqNvr_jK7dgpO5aEGo_4ld1QahOiU2qzluYdf7lOn4Uo_zV4TvXM0G5i6DcM5IpHHJu9Fjjsw_tAKgKToqzQw4QWFt9XHmdMKxotb--GydAUGo3Vq7RNDi1hovZxMCI1XWer4tht-CJVWLR3JQk1vJES183_wDPqsFS6HFOQGVHrfTNt7CIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86139d3a31.mp4?token=b8BRXheFgzb2xf4zCJsoIfgMqP8hO7--qPqHyvpRRySe8evp4C1p1PWN8j2Zwxel9Nx94F9gKG33QECup5hkMLYFi0KqBa2jriE7Qib6e51Ttb4Nyn-B8ULcUUICq-nTB6s1NXxitaTZh88EJ1ujhlQCLmwDZ8mGHyIqNvr_jK7dgpO5aEGo_4ld1QahOiU2qzluYdf7lOn4Uo_zV4TvXM0G5i6DcM5IpHHJu9Fjjsw_tAKgKToqzQw4QWFt9XHmdMKxotb--GydAUGo3Vq7RNDi1hovZxMCI1XWer4tht-CJVWLR3JQk1vJES183_wDPqsFS6HFOQGVHrfTNt7CIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده در جلسه سالانه درباره وضعیت اقتصادی آمریکا و سیستم مالی بین‌المللی با دفاع از سیاست‌های دولت دونالد ترامپ در قبال ایران، گفت رئیس‌جمهوری آمریکا اقدامی را انجام داده که به گفته او، رؤسای‌جمهور پیشین آمریکا سال‌ها از انجام آن خودداری کرده بودند.
اسکات بسنت با اشاره به جمهوری اسلامی گفت: رژیمی که خود را وقف شعار "مرگ بر آمریکا" کرده و به‌دنبال دستیابی به سلاح هسته‌ای برای تحقق همین هدف است، اکنون با سیاستی متفاوت از سوی آمریکا روبه‌رو شده است.
او افزود: تحت رهبری رئیس‌جمهور ترامپ، آمریکا دیگر صرفا در حال مدیریت تهدید ایران نیست؛ ما در حال پایان دادن به آن هستیم.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78396" target="_blank">📅 21:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78395">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/spjhaiK3jxPZe9YP80ur4_Ju76N002kiCKYjxPw6SbMhA-t_qIHRmCCRRrLZohItWbbXOG3ewgnQhKRHoQfvoRNX16ryyOMfF4s2b8PI-ogiHJ1Q32-mqz88DrddPESX35DjjtkH2fZqJqdY7m7eheuOrFmeTeefg3V8Dj6rIxEeRg5SECp44vDuytiLGT8hKPnmfTX0sH1RhUN6ekxQrna4SRvX1GkpoKbmp5qLPN2Vdr_zf21FuT6i1Bu9eCI_yKXluYQyFgmu4h529yRQ-Poz29lZ4mSR-Mye1xgq_PoVctMQVAQIqnePt26m4kH0Mdq5ntCTbiZQm6xoMvck4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درباره خبری که تسنیم با شرح
حمله به قایق‌های صیادی
منتشر کرده بود:
وبسایت اکسیوس به نقل از مقام‌های آمریکایی گزارش داد ارتش ایالات متحده روز دوشنبه ۲۳ شهریور ۱۴۰۵، دو قایق کوچک ایرانی را پس از تلاش نیروهای سپاه پاسداران برای تصرف یک پهپاد نیروی دریایی آمریکا در تنگه هرمز منهدم کرده است.
به گزارش اکسیوس، نیروهای سپاه با استفاده از این قایق‌ها تلاش کردند یک شناور بدون‌سرنشین آمریکایی را که برای گشت‌زنی در تنگه هرمز مورد استفاده قرار می‌گیرد، تصرف کنند.
پس از شناسایی این تلاش، یک پهپاد آمریکایی دو موشک به سمت قایق‌ها شلیک کرد که به انهدام آنها و کشته‌شدن بیشتر سرنشینان منجر شد.
تیم هاوکینز، سخنگوی سنتکام، تلاش نیروهای ایرانی برای تصرف شناور آمریکایی را تایید کرد و گفت این قایق‌ها «تلاش کردند یک شناور سطحی بدون‌سرنشین آمریکا را تصرف کنند، اما پس از واکنش قاطع نیروهای سنتکام موفق نشدند». او تأکید کرد این شناور همچنان تحت کنترل عملیاتی ارتش آمریکا قرار دارد.
این در حالی است که رسانه‌های ایران حمله به دو قایق را به شکل حمله پهپادی به «قایق‌های صیادی» گزارش کرده‌اند.
به نوشته اکسیوس، این دو قایق در نزدیکی بندر کرگان و جزیره لارک در استان هرمزگان هدف قرار گرفتند و احمد نفیسی، معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان، حمله را به ارتش آمریکا نسبت داده و از مفقود شدن شماری از صیادان و آغاز عملیات جست‌وجو و نجات خبر داده است.
این حادثه در شرایطی رخ داده که ارتش آمریکا تلاش می‌کند با افزایش تردد کشتی‌های تجاری در تنگه هرمز، عبور و مرور دریایی در این مسیر را به وضعیت عادی نزدیک کند.
یک مقام آمریکایی به اکسیوس گفت ارتش آمریکا و کشورهای عربی خلیج فارس در ماه‌های اخیر تردد نفتکش‌ها از تنگه را در طول روز نیز آغاز کرده‌اند، در حالی که پیش‌تر این عبورها عمدتا شبانه انجام می‌شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78395" target="_blank">📅 19:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78394">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d82b868f8b.mp4?token=BrtNmDv8ZOtIpweM5lpycS4D_DzaVgOhQlOGdvGQvHbbZzyl-sNrRYxPwj8GMDhbdRZ8TDigNR5R5-Yg1ZUM96ktdZ0J0daG1ta6Tyd2K0_fDnt3Y_PDgXtXaXQIg55xHvcjJSZ_3ey-gKopGMUVDFz21uRg-CA7qQnSIkObPmsJM70gwtEwtswvfh9Syy5PBBJlTjhxAgPpNuWynuqSFzWbykvplxd0PGWl1-d4pcw18--9vqiSJSIBcvk81JKIFso7Kj7e1UA6UEuRTFuVTKAmN8yceB2wC_QJktZRDbXclruBx-Cfkab5P0ApYXgF-ClnOZONmCpsmLmuRcVFjg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d82b868f8b.mp4?token=BrtNmDv8ZOtIpweM5lpycS4D_DzaVgOhQlOGdvGQvHbbZzyl-sNrRYxPwj8GMDhbdRZ8TDigNR5R5-Yg1ZUM96ktdZ0J0daG1ta6Tyd2K0_fDnt3Y_PDgXtXaXQIg55xHvcjJSZ_3ey-gKopGMUVDFz21uRg-CA7qQnSIkObPmsJM70gwtEwtswvfh9Syy5PBBJlTjhxAgPpNuWynuqSFzWbykvplxd0PGWl1-d4pcw18--9vqiSJSIBcvk81JKIFso7Kj7e1UA6UEuRTFuVTKAmN8yceB2wC_QJktZRDbXclruBx-Cfkab5P0ApYXgF-ClnOZONmCpsmLmuRcVFjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیوی منتشرشده در خبرگزاری رکنا، لحظات پراضطراب داخل هواپیمای بوئینگ ۷۳۷ شرکت سپهران را نشان می‌دهد که دوشنبه ۲۳ شهریور پس از برخاستن از فرودگاه مشهد به مقصد کرمانشاه، با ترکیدگی لاستیک مواجه شد و با گزارش آسیب به موتور، مجبور شد به فرودگاه مشهد بازگردد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/78394" target="_blank">📅 17:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78393">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NjfMmaBRxmvyTqbIsFruiD1A9peewuO9abBNRuStX5mHgpZQDnHEsAhqeofawataXx1eLpbP0Pwlk6FDVyRepL68nQtP_X0ZnhXAQl9d7nNTLx440tE1gvt91e1Wpy70rSf0BQW18CZWAz0NxstN7rth_fwBXGoSFMaigDJIL1HkbPzsHEGU8PTGFRlyF9CW5wrzcpJooMOXtBIlz7_oQzdt0RuNd8-7t0tWMRxyVEHpD10yx-a-0mmEEbgRr6yVHWxm4alxBQgm9hhfLhBQZudXi0j3BXYMbmKR1EpEX6ViBC1-QUdNNZiuu1JtSy6GFMt44r_DoqyE4NUxIoO-Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر رئیسیان، وکیل دادگستری روز سه‌شنبه ۲۴ شهریورماه با انتشار پیامی در اکس، از تشکیل پرونده کیفری برای رضا درمیشیان، کارگردان سینما و تئاتر ایران خبر داد.
به گفته رئیسیان، سپاه با شکایت از رضا درمیشیان  به اتهام تبلیغ علیه نظام پرونده قضایی تشکیل داده رسیدگی به شکایت از او در شعبه هفتم دادگاه انقلاب تهران در جریان  است.»
رئیسیان با اعلام این خبر گفت در دادسرا برای رضا درمیشیان قرار جلب صادر شده و سپاه پاسداران به عنوان شاکی، تقاضای توقیف اموال او را کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78393" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78392">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvx-dlt_bvpBC0qkAPCvRCl_gxH_VzAU-bWS0O1-iUPUX1QaPz8X6vCYnjxKMlbp_2t6M8LqgbKaJN8--HpdLiK4OuN4U36GCqON4xcdAa9AH6pvJ03xPKXevT7v4ivn3JiPFxRZuZr8LtFPil1GUCY4TlA9zeHObsdvPd3bWJ-C1fjhcoMfMrWphAcUoLidbADZh4nok2m9fk-KTKl6azGjb7iIFhz1sOom5PXfYE9z75nloV961OOV1Kzc-AK78JW94ewnJfWvt_EDYwQM6lqzYD0wvX8-6AqSmDs0a_VsTqHJYTykFfH0CW0b1PpJ-Dk1NfAgYP-jILpoXwtB3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استودیوی «کارگاه» با انتشار عکسی از آزادی «آریا کسایی»، طراح گرافیک و یکی از بنیان‌گذاران این استودیو، پس از نزدیک به دوماه بازداشت خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/78392" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78391">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mAkkpwESQ50fJfFO8PfiWdK6dAe2sMWDDr0epihTWYGwJ5FYu9yBN3EvBMOEnhy4KQEraLdXmlcassUUtM95QzBauqwId2XxGoDTkeuz6bp3lrtex8LEIO5psF2kFX8r66eHrBUt0kDY3t_UEjVK6hXjJ3wZBet5l-zDIxy8xzWoyX-52utw6e6RhLmq_S9mwldMvXWm8DM3PaOywVjAaHQx1PnCFqdt9kKcTe2fiHCLfeM2TJfFknjJ9Og9Ira-BNeidz3WnBxL5VzakaDt2ixyIln2Dte8SqNhooOz2OzPhHy5BpMfHbpjvrHI-NiFg4iXzj3J9SjkWPb9sPgQdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس تهران می‌گوید فردی را بازداشت کرده است که شامگاه دوشنبه ۲۳ شهریور به سمت «جمعیت حاضر» در میدان پونک تهران سه کوکتل مولوتوف پرتاب کرده بود.
میدان پونک از جمله میدان‌های تهران است که از زمان آغاز جنگ ۴۰ روزه تجمعات شبانهٔ حکومتی در آن برگزار می‌شود.
بر اساس بیانیه‌ای که فرماندهی نیروی انتظامی تهران منتشر کرده، «این فرد حوالی ساعت ۲۱:۳۰ از بالای ساختمانی به سمت جمعیت سه کوکتل مولوتوف پرتاب کرده و پس از آن گریخته است».
در این بیانیه ادعا شده که این فرد «قصد خروج غیرقانونی از مرزهای غربی کشور داشته اما ماموران با شلیک گلوله از ناحیه پای راست او را دستگیر و به بیمارستان منتقل کردند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/78391" target="_blank">📅 15:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78390">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bKQ1Bc6kNlwVy9C6T6kKtpeUA7gqzqUK933BArbtyrgFktL-DDHpkwe2dWdV_YVpQNLeDQ1EUx9LJTQpzQ35VKM-YPaYWmNPD2z2d3JP6isR2TcNwjguTdIIr698bKJ3KPvBjHCo2tNsNvwOP5mM_yTDnUHJs_FzJdOFmtsKMQnG0PdcvwdujIynElxl9ZzmgeXuWnft_rmLt9BDUGFtdzobbtPT0wsfT1tlkuUwWaDZ7XoLH0ZMNQz10assMfYAZ0bZRpC2llyrEUxp7ujQIwdfEcsS5R7g_XWb9aK5DArSgqmBjAYoZtyERjKUnfvG49drkvzY6F-8IcXbPuFVmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش رسمی آمریکا از هزینه‌ها و خسارت‌های جنگ با ایران منتشر شد
یک گزارش رسمی نهادهای نظارتی دولت آمریکا می‌گوید جنگ با ایران به «کمبودهای راهبردی» در ذخایر برخی تسلیحات پیشرفتهٔ ایالات متحده منجر شده است.
نخستین گزارش رسمی نهادهای بازرسی دولت آمریکا دربارهٔ عملیات «خشم حماسی» که روز دوشنبه ۲۳ شهریور به‌طور عمومی منتشر شد، می‌گوید مصرف گستردهٔ تسلیحات در جنگ با ایران «به کمبودهای راهبردی در موجودی‌ها منجر شده و گلوگاه‌های پایهٔ صنعتی برای تأمین مجدد مهمات را آشکار کرده است».
بر اساس این ارزیابی، پنتاگون برای مقابله با این مشکل در تلاش است روند خرید تسلیحات و زمان تولید را کاهش دهد و ذخایر مواد و قطعات حیاتی و برخی مهمات را افزایش دهد تا در شرایط اضطراری امکان افزایش سریع تولید وجود داشته باشد.
این گزارش همچنین نشان می‌دهد آمریکا تا ۲۹ ژوئن (۸ تیر) حدود ۳۳ میلیارد و ۴۰۰ میلیون دلار برای جنگ هزینه کرده است. نزدیک به دو سوم این مبلغ مربوط به مهمات مصرف‌شده بوده و ۳ میلیارد و ۷۰۰ میلیون دلار به تجهیزات از دست‌رفته اختصاص داشته است. بر اساس این گزارش، ۷ میلیارد و ۴۰۰ میلیون دلار دیگر نیز در ردیف سایر هزینه‌ها قرار گرفته است.
پیت هگست، وزیر دفاع آمریکا، اواخر ژوئیه (اوایل مرداد) هزینهٔ جنگ تا آن زمان را ۳۷ میلیارد و ۵۰۰ میلیون دلار اعلام کرده بود. شبکهٔ ان‌بی‌سی نیوز نیز پیشتر به نقل از مقام‌ها و افراد مطلع از برآوردهای داخلی گزارش داده بود که با احتساب هزینه‌های گسترده‌تر، رقم واقعی جنگ می‌تواند به ۸۰ تا ۱۰۰ میلیارد دلار رسیده باشد.
دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه و همزمان با انتشار گزارش ارزیابی «عملیات خشم حماسی»، در شبکهٔ اجتماعی تروث سوشال نوشت آمریکا اکنون بیش از هر زمان دیگری در تاریخ خود تسلیحات پیشرفته تولید می‌کند و این تجهیزات به‌طور روزانه در اختیار نیروهای آمریکایی در خاورمیانه و دیگر مناطق قرار می‌گیرند
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/78390" target="_blank">📅 15:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78389">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAAm9K7YU6w9L1U1MNs4ODhWPtCAH0zLPglFuizfZ2ea7mwWKNTytm5J6VjrzuSCkXE10_y2pbr5azIdRCciDfJMB-1uV4L2ki6RnmQHfhucT3I45tRarXOXqOoR9GGQ6y17xNYaWz3hSOpBPOQDukTdq7BHn93kMjlCNVxpmy1xQ3G7m4Ly6geFwgfrFcQVQTioiXNSk3hoaYDR-GPo-qipCSdxGByVOxUHDX2G1j-nN8qH6k7KNFSzW1w3hLZUZkz4YH1_dKh8Ti7zbu_IxK3JD1-7XFfR3memCd9lIXLuhx1iEJJESe2FWieH7MGJnJOFEOkbJwhLfLbc8dcZ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پروژه امنیتی با نام «علاج» با انتشار اطلاعات شخصی شماری از ایرانیان خارج از کشور، از شهروندان خواسته است افراد بیشتری را شناسایی و به این سامانه گزارش کنند. صداوسیمای جمهوری اسلامی نیز به تبلیغ این پروژه پرداخته؛ پروژه‌ای که مشخص نیست چه نهاد امنیتی یا حکومتی آن را اداره می‌کند و اطلاعات هویتی منتشرشده در آن از چه طریقی به دست آمده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/78389" target="_blank">📅 15:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78383">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Wi4lCW3cAemDRpfkG2sVS4WNH43YwWu-ivGqS543Pm4_a10e_KuAS9zoWHu4MxpqOdI34y159gKYKOW-zHDKC50c15hbUjmZkmiu43JHN2VO4LLkSTAd74quT1w9zCzLrYmGeGN4n6YBEdmJJ5yKidsg0F9xeKUL5Tp-lojgTSUIwLBpDNScbOhrr-IQ-Cu-IY1mS36lLCacjLxhjwT7YTOEFRPeJFJ6XR_Lk5MuaU1MDQVCcBruLs8uBPy6mY9xd6JTW51yLHNm2LymmJ7PlYXEc50gbFiJYLkrlwnfgexQQobkn-UKtcg259ugdyB83zaED6bsHvFets0VAxYWTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HKQipCadXqvDtXFT4__VDtTCV_qV9ZRQteWf3B_ie9fhao-Plhs_Jn8qWMyrHQq9yyob3fFwGledYOTBt5Sq24UE6NNEUQx1LMES9hfc_-GksACGKDyeKvbduytTaQ0IDx9dELXcnAMNr9joePLVtv17RpZ9enBIQH3y3bpcYECo2WeBH95pjRdhNLlpEvAuQu9gRnqk9yZEBz7ykOlQJVg-GtgOD_PnakAT911thYSNuZnDhyFYOWrBrnx_3cBRXaoToVX6bBNwyAQnwjQkTZoiEndRMJjMM-rzdx88mkmNYymeIimSGKuIO82AaNCmYYJTIbcJWMpzBNB8xWmU3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i-iUzhluvMi5moeaSlWBb_yw10pzgZD7oG8_BjiyGHLLGB-a3tCsebheqfqRLenhxrwaHAWRgifmibPMxGAk99nzeqsHqXyLFNtny0FkXZnJXdpkWlEtcy68PDbcYDmdC5cTVoVCMnXKhtQGPc_s3P-7lN7uG909_OFBQkGjDNksnzOYI1ZBKDTKMASCuw_Lycxojfqtu6JZqJbiEv58sqKIoURwiZtj7kl9uFmmGIaxPBW9QV4xxEAJTTmCMgfEn0e3qD6CtE3vn_myJ2nVWNX1Nfr4YFhy27IhlGolu-HbifBFVmIPyvRJwLce8d8Gv5v3rebcSNKqhEFEvwbYDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QCTZns6glHuv2IDaAG_6OFfKjMjNwrBiM0H6-pWTyWJ5LjvPwvBrsr0ns066NALvEHPxRJftTpu2YFnpTE8cvoRO4cBNVbLkIpV_MxleIcp0wrTN2EM41NCmHpwmLfBym6cHmmAYzW-wdinxi1TyIzV0sllJPNWJmBUvcStQXwWn1bDBr6-CZlTuSafBg1mdnepQLaDxk9rtKiUpa-d5Y7pCnde-feq4Wka46oTKgtF6CGA3e0yzUC8ivTI4MLVS6DLovJP0G9eBFt3w24ufUIq4zWxNvcx0Dwv_lmkWp9LM-G28MN7_3_T99Q6i175o-7olTpQltqjOJBcgS37iPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hTJ36oIe2xa1R5TWVYKLP9o6gG914s2ZBS4ZL_wixC2cKepD1yvyvu2wFx4IMt2FOLhQyGkOpo2QJ_lZZrnNOLsnR4_EYfPU_zw51q7lK2s4rdesB4U6ueP7rKDCngXTrMtQap1iLyPZyJH_uC7gnGRasrdb_myeuRiFnR058x97uMf2L2ZQs0hYA1zvuB3K6uEZXWABavGQqex1ow87miA84rGVkt1a1G9JoZKXcRstqmvi6MSnvd2cNkMdMZ3fl0K1CAwzd3BEH81uTuy-6VGL12F1PWSSZVOGzDWzg2rADRT3CoIrE_ORrcJRqyh5L9Usx_gIWlyJCESC43LNzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dJTqrCfsqR50ZaQ216Hh7PSbYkPo8aVPJ1ooq0yqSTXcC9y2s5Mr4BmZnmRgDytEMC3CfTvrJ21xYn_K25i9WfJ09TO66jehmaK-bV4t_avlAL64B7QhL3kmxES2noc_qXZs12EMIpTKnZc9eSKy0nxus5kvpfBNtJpoa5CiyqL2uD83897hBlGXvO48uydGCFlabR3MC2k7Jxk8Exq15HtjCOaGv5Z_nOusbkS6JqiAj2WgcRiVqvSBLGyd5NoSmEEKxEHah7J9EjTPrRbUia7ASdMiV0YYo3iDq8Ird3uC7oDub_XiRVsoOUfkss81HyHcCD9XGlnidGuj8AjQ9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«پویش جان‌فدا»، کارزاری وابسته به نهادهای تبلیغاتی سپاه پاسداران، ارسال پیامک برای ثبت‌نام شهروندان در دوره‌های «آموزش نظامی و امدادی» و سازماندهی آن‌ها در قالب «گردان‌های مردمی» را آغاز کرده است.
در پیامکی که برای شماری از شهروندان ارسال شده از مخاطبان خواسته شده از ساعت ۱۷ سه‌شنبه ۲۴شهریور برای شرکت در «دوره‌های آموزش نظامی و امدادی یگان‌های مردمی جان‌فدا» ثبت‌نام کنند.
پویش «جان‌فدا» از ۸فروردین۱۴۰۵ با محوریت «قرارگاه فرهنگی و اجتماعی قرب بقیه‌الله»، از نهادهای وابسته به سپاه پاسداران، راه‌اندازی شد. سامانه‌های اینترنتی، پیامکی، تلفنی و ثبت‌نام حضوری برای جذب افراد بالای ۱۲ سال در این پویش در نظر گرفته شده بود.
@
VahidHeadline
دیروز کلی پیام دریافت کرده بودم از شهروندانی که می‌گفتند در این پویش ثبت‌نام نکرده‌اند ولی اون پیامک براشون ارسال شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/78383" target="_blank">📅 15:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78382">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zzh5itYX3Jae1w1y6A36ckO429ZjW6f_POL2eE9k8IoQXzwt7liJcKDuEtaM52aEuFgsC3QK7Aa-7ivlZZQg4LtleERW7IhxrthcRVq056RhDZ0GOGnqApUiWJzxV9Xy2xdoK1fPFGaNLBtQbqZuPvG4dUI9VJRmpJf8sXPMgwVIGpqSA64a-gYCVT8WD7qcpwoZYrHkUSxW9P4ai2GmwjbfXuyKIjoHBqwNtQJ8nkx0a_d3mxH8uMTI7Vi-IEFUX7PYHf4UhPvyznUUSn07cvJ7_o41f3DNp3QI4ZDJm_yNMB92vbhH8398nDvv3YOEutsLZlIfmUm4R488-fUdMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌دادگاه فدرال آمریکا روز دوشنبه، ۲۳ شهریورماه، به عدم اجرای دستور دولت دونالد ترامپ برای محدود کردن مدت اقامت دانشجویان و خبرنگاران خارجی در ایالات متحده حکم داد.
‌این دستور که به گفته قاضی دادگاه به دلیل «استدلال‌های بسیار ضعیف» دولت صادر شده، قرار بود روز سه‌شنبه به دست وزارت امنیت داخلی آمریکا اجرا شود.
‌بر اساس قانونی که دولت ترامپ سعی دارد به اجرا بگذارد، روادید دانشجویان خارجی و روادید افرادی که با برنامه‌های فرهنگی در آمریکا اقامت می‌گیرند، به چهار سال محدود می‌شود.
‌این قانون همچنین می‌گوید که روادید خبرنگاران نیز نباید از ۲۴۰ روز فراتر رود.
‌هر سه گروه، بر اساس قانونی که اکنون دادگاه جلو اجرای آن را گرفته، برای اقامت بیشتر باید بار دیگر اقدام کرده و روادید خود را تمدید کنند.
‌به گفته قاضی دادگاه فدرال، اجرای قانون جدید تعداد دانشجویان خارجی و روزنامه‌نگاران و خبرنگاران در ایالات متحده را به شکل قابل توجهی «محدود خواهد کرد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/78382" target="_blank">📅 15:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78381">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxrCLeXGoQyrL5AtlML9o9a7s9W9EKeWoMJYcC0s4ix8hXsMfYgd-D1w8-13E5BZaEOAcEwxQV8g_r2caaQeDB_CK3ejkTlPXJOliaNO_5E2U5dmhVruegltqN7dvqQ3VbS-DGWwmNQA4jlKjHDRHtFzCZAwt6EVgOorvaAvF3bWbQLueH8NHJ-Zt6-Sh2ssRjUXOvekILjraBjTgw9tG5N66KqjX3LXvh9NJtl44NwNW1nbIupLOaPhDdh0zJwOKlpRaST_MQoHlRQaDxTIShLsJRdZHtVX8f0UKJk9IgKqKpw6PMJ7ehLS5ZSa3mhNuKDTm_TvX8bP4Cxk1wt-Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه اتریش اعلام کرد برای سفر محمد اسلامی، رئیس سازمان انرژی اتمی جمهوری اسلامی، درخواست معافیت از ممنوعیت سفر سازمان ملل داده بود، اما درخواست رد شد.
بنابر اعلام این وزارتخانه، رئیس شورای امنیت سازمان ملل به وین اطلاع داد که درخواست به دلیل نبود اجماع رد شده است.
وزارت امور خارجه اتریش افزود با توجه به تعهدات بین‌المللی این کشور، ورود اسلامی امکان‌پذیر نیست.
اسلامی در راه وین برای شرکت در کنفرانس عمومی سالانه آژانس بین‌المللی انرژی اتمی بود که اجازه حضور پیدا نکرد. او از سال ۲۰۲۱ در همه کنفرانس‌های عمومی آژانس شرکت کرده بود.
ممنوعیت سفر از سازوکار «اسنپ‌بک» ناشی می‌شود که تحریم‌های سازمان ملل علیه جمهوری اسلامی را بازگرداند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/78381" target="_blank">📅 15:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78380">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j-aq5rDUWT02sCWGpnrbtStEVPlcjD8gazFAZF-ahP2TCbm5oDTjcXkjaDuaecUXVfo53iDEhdmyrC7YsdKofrh9L3SgT6s7Y-wuVE4Qy8la4TgzEEIeMd_f-PmWJAaRvFDOn0enX9X6bVx692JAkkR0_5MqXMURWkMJcGS-DUFwgApsrrZjDGU2PKcHc7Rf175x1oGMhz1unFlZhgTfjAFyN8QTB7wimoULamvkZ3Ss6sSXgrRJxiBPxmnrza8Bd-dCapc-BDAIvTbLXI7YjjSmO6TY-5hMQmidUVZASIYpUiZbNKeRwfnBCoSozC_Q01BhloWIO3wTK-__J3HDsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش الغایا پس از حمله در سواحل عمان و آتش‌سوزی در موتورخانه، به یکی از بنادر این کشور یدک‌کشی می‌شود.
بر پایه گزارش رویترز به نقل از مقام‌های عمانی، ۲۳ خدمه از شناور تخلیه شده‌اند و دو نفر همچنان مفقودند.
روایت‌ها درباره علت حادثه متناقض است.
سپاه پاسداران اعلام کرد الغایا با پرچم پاناما هنگام عبور از «منطقه ممنوعه» جنوب تنگه هرمز با مین دریایی برخورد کرده است.
فرماندهی مرکزی آمریکا ادعا را نادرست خواند و گفت شناور «ماه گذشته با موشک ایرانی زده شد و از کار افتاد».
سازمان بین‌المللی دریانوردی گزارش داده بود الغایا روز شنبه آسیب دید، بدون آنکه علت را مشخص کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/78380" target="_blank">📅 15:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78379">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k4emnIEVT2GCTMjf_mTZHGOMYksMutgYRotixuLj-Ry0mZ2CtkrvKbnd_I7zixuFVyb3LJvs2SRPVw5tTRGsfPx_wh5TTxtjJGroAWglC-HryecveNIYXC94d-OzyVtVICW30NRYGfRSyIZiCQxXJZniTKl8S441yT7Yx42IHZKoJdthXl_jhKba8CLJPV5R6zgFtyjDb1f8TMvDuH7-RMY-A02m6PJqZKE7sSEymu3-IM1xTPxxwf_G16n2hzLYThTpEy6sE8FQPVQxR5QixBflSXgPG3FooH6_wEyt2ccPwD2ckXP63Sg_cV1oMWi4goWum3KKYDN4VRaEjlXapQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست‌کم ۱۰۰ معترض در ۱۳ استان ایران در خطر اعدام هستند
سازمان "حقوق بشر ایران" اعلام کرد دست‌کم ۱۰۰ نفر از بازداشت‌شدگان اعتراضات دی‌ماه در ۱۳ استان ایران با حکم اعدام روبه‌رو هستند؛ بیشترین شمار این افراد با ۴۶ نفر مربوط به استان اصفهان است.
بر اساس فهرست منتشرشده، پس از اصفهان، ۲۲ نفر در استان‌های تهران و البرز قرار دارند.
همچنین ۱۰ نفر در فارس، هفت نفر در خراسان رضوی، پنج نفر در مرکزی، سه نفر در یزد و دو نفر در سمنان در این فهرست ثبت شده‌اند. در استان‌های خراسان شمالی، گیلان، اردبیل، ایلام و قزوین نیز هر کدام یک نفر با حکم اعدام روبه‌رو است.
این سازمان می‌گوید فهرست منتشرشده تنها شامل معترضانی است که دست‌کم در مرحله بدوی حکم اعدام دریافت کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78379" target="_blank">📅 15:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78378">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TYzWu4Dx_E3uqjKMoaWoEmN9KE0JyrRDkiSifbdXXnamS6X4cacjjLJBZK_Ir9GODWLNbeEl6DnPwXvCtq4qOkJnMxKA9EempYGUHYTCpWaWUvkbNTAtCi2TrX5o9YphzUdrOGaInKrcxve7wgWewwf9-i8mSSm8Ff_wFoFrd0GN7HsfdFewfp2-Us-6Pfw75bIxutnSNqWBu2YDJPJ02RCxc4LXx9VibwzNBXM8dV_AQ5Hb5O0mLtYjtdz8K2IMtqHTQz8WsNkACst50KTjyOh4Tv5G0_hPT_l2f71FsvB4eCfakGiUFT741JRi4Xk8vPqP67qc9s2sNzTpcANOgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، شامگاه دوشنبه ۲۳ شهریور ۱۴۰۵، از حمله پهپادی به دو «قایق صیادی» در حوالی بندر کرگان در آب‌های خلیج فارس خبر داد.
بر اساس این گزارش، در پی این حمله که تسنیم آن را به «آمریکا» نسبت داده، تعدادی از صیادان حاضر در این دو قایق مفقود شده‌اند.
عملیات جست‌وجو و امداد رسانی برای یافتن مفقود شدگان آغاز شده و نیروهای امدادی و دستگاه‌های مسوول در محدوده حادثه در حال جست‌وجو و نجات هستند.
تسنیم نوشته است جزییات بیشتر درباره این حادثه و وضعیت صیادان پس از دریافت گزارش‌های رسمی اعلام خواهد شد.
@
VahidHeadline
آپدیت:
اکسیوس: آمریکا دو قایق سپاه پاسداران را منهدم کرد
@
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78378" target="_blank">📅 03:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78377">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dja8JLja3L67Z5OUwknDrRjZIqxmk6SvCPC_5dvZJywoIHOlZPbEEqZnr9472Oe_8ixCrND_g6CbriX_ulZ4otsnbcwU7jcNxB2HgJF96jJ_n_FGGJXXauPnORUaamWDTLw88Nn9h7wCunDMKP_VMv3whPNslNZk_UZvH-SCbBav7xPIQJGyG1F3io6yzvdzNhtSoAW0m44VKPGt7jw1rCYS1uhgfxGmOGxZyWGHsWogf58BF9xfDggsnGz1BQbQKUeM1wgFNGjiFZB4vLD3H43_pN0L_v1Qn1emQH9_jD4d_M5uAzodhV-UeXEjJL6nXFgQUXgJGXhYDNP_LfhfjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی نیروی دریایی سپاه می‌گوید یک ابرنفتکش که به گفتهٔ آن قصد عبور از «منطقهٔ ممنوعه در جنوب تنگهٔ هرمز» را داشت، «بر اثر برخورد با مین دریایی منفجر شد».
خبرگزاری‌های ایران شامگاه دوشنبه ۲۳ شهریور با انتشار بیانیه سپاه، نام این ابرنفتکش را «اِل گایا» به شماره دریانوردی «۹۳۲۵۳۳۶» اعلام کرده و افزودند که «تلاش برای مهار آتش بی‌نتیجه بوده و کل نفتکش در شعله‌های آتش گرفتار شده است».
فرماندهی مرکزی آمریکا (سنتکام) این ادعا را «نادرست» خوانده و گفته که نفتکش «اِل‌ گایا» که با پرچم پاناما حرکت می‌کرد، ماه گذشته هدف موشک ایران قرار گرفت و از کار افتاد.
@
VahidHeadline
پست سنتکام، ترجمه ماشین:
🚫
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی است یک نفتکش با پرچم پاناما اخیراً در تنگه هرمز با یک مین دریایی برخورد کرده است. این ادعا کذب است.
✅
واقعیت: نفتکش «El Gaia» با پرچم پاناما ماه گذشته هدف یک موشک ایرانی قرار گرفت و از کار افتاد. آخر هفته گذشته، ایران بار دیگر این نفتکش را در حالی که در آب‌های ساحلی عمان قرار داشت، با یک پهپاد هدف قرار داد. این نفتکش در حال حاضر توسط یکی از شرکای منطقه‌ای یدک‌کش می‌شود.
ادعای کذب سپاه پاسداران نمونه دیگری از دروغ‌ها و تلاش‌های آن برای ارعاب است؛ آن هم در حالی که می‌کوشد مانع تردد کشتی‌های تجاری در تنگه شود
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/78377" target="_blank">📅 23:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78375">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hs2agcmW5QmFnhb8cX44w_8CHdDebEkJglYYJnHZjsbbDaZibwUaZ3o3ZSJgjw9LarWnfsFZagcTIRsfv258VEPO4VqkKYmkaRo8mdQkWrC5-R7kJx5S6AH8z2Mzr3lHNO6-liTq-RQ1Ud3Hz9q8mxT3AAFK977xhBdphWbYUxjjpFV5k2ZUKR7ydaK3gkAWJdJbOxkzZxLMVDXdhzE4fiUwY8nbuSptD3fviBW3WxfEe6rlNOyKKyOyxBTHSetjuTm_k-HuYgt2URHJqppsHsERcLa-AdLDLjvwOBnUFAxlRfYfX4_6iw8yH38ZB29Istsfbd1RsJNU-zCiNvuKCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PcVl6z-ZvFTr1PY4W5NGaivxBH72CCy3CmCe3MyeTdcWkcTefiM1n0RkjQeOy65fNCDzhLTaWmt1yL4DgewccSaCq1QWFHggY0CxqeU4rmdhPdVoX8kttMpGushG2VVSZDKFAzI_U7ENAZDBRWh47ckL_0hYAtyuOGjbQ6TfuMziGmffmKegTmVlzurvBFRS44IHo9peeJXBMGU7w38KcJIAJWOkFIZZngam1yNdw8iyOYzVZ2mY7vMGK59fXc3LxkNS875reyEsg7FidcovGEqX5RHHsmH0Ynh9MiNFLO4xms6Twx511Zi6K4s0aF0uFfLA352i9ViGRGRUrqT6Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ در پیامی در شبکه اجتماعی تروث سوشال تاکید کرد که افزایش قیمت‌ها در سراسر آمریکا ناشی از سیاست‌های جو بایدن و دولت او بوده است.
او نوشت که حتی بهای نفت نیز در دوران بایدن بالاتر از سطح کنونی بوده و دولت او مانع از دستیابی جمهوری اسلامی ایران به سلاح هسته‌ای نیز شده است.
ترامپ با اشاره به اینکه قیمت سایر کالاها به شدت در حال کاهش است، افزود که بهای نفت نیز به محض پایان یافتن درگیری نظامی با ایران—که به گفته وی زمان زیادی تا آن باقی نمانده است—مانند یک سنگ سقوط خواهد کرد.
در دوران ریاست‌جمهوری بایدن، به‌دنبال وقوع جنگ روسیه و اوکراین و بحران‌های بازار انرژی، قیمت نفت در بهار ۲۰۲۲ به بالاترین سطح خود رسید؛ به طوری که قیمت نفت برنت تا حدود ۱۲۷ دلار برای هر بشکه افزایش یافت.
@
VahidOOnLine
رئیس‌جمهور آمریکا در شبکه اجتماعی تروث سوشال از کشورهای جهان خواست پس از پایان درگیری‌ها، هزینه‌های ایالات متحده را برای حمایت از کشتی‌ها و کمک به عبور محموله‌های نفتی از تنگه هرمز بازگردانند.
ترامپ با اشاره به اینکه نفت در حال عبور از این آبراه است، تاکید کرد کشورهایی که هیچ کمکی به آمریکا نکرده‌اند، باید خسارات و هزینه‌های این اقدامات را جبران کنند؛ زیرا واشنگتن این ماموریت را بیشتر به نفع دیگران انجام می‌دهد تا خودش.
پیش‌تر کریس رایت، وزیر انرژی آمریکا، اعلام کرده بود میانگین تعداد محموله‌های نفتی که با حمایت نیروی دریایی این کشور از تنگه هرمز عبور می‌کنند، رو به افزایش است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/78375" target="_blank">📅 23:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78374">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G9GB6JnqXWch3ej6jw8genRssxgVnRYTRjxUqnpfaXkQ5Anc7at2JvGpw-FTAkcsWsvL_7wpmvLPvuigfnj9IW2SNLo9JctI5Xl4UiW7q0QSHDPTceiaLru_hgQ17jOE1k0CuU5yjqumH9WraS9mk9uZgBbVm0bGzLz3ugv_EtJamqO3opouMzxvA2n56H3aEsW4NkaBsqE9KzQwZlk_8zyTF0Xj4INYqbSczxnV71MFwkznqebgT-voBJsdm4EOCzZ1Wz_Q_ZAJhMm8y3ouOxRXcx19jnKq7E7pbg-3G8MmZsJ_ZHuuzsEqwLxxMzMQBa6AMKT6LHGReIqoqnrH5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایرانِ شکست‌خورده می‌خواهد خیلی سریع و به‌شدت به توافق برسد.
من تصمیم خواهم گرفت که آیا ایالات متحده آمریکا وارد مذاکره بشود یا نه — ایده‌ای که نسبت به آن آمادگی داریم. از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
ترامپ نوشت: کشور در حال ورشکسته‌شدن ایران می‌خواهد سریع و به‌شدت به توافق برسد. من تعیین خواهم کرد که آیا ایالات متحده آمریکا وارد این داستان خواهد شد یا نه؛ چیزی که ما نسبت به آن نگاه باز داریم.
پس از انتشار این پست قیمت نفت اندکی کاهش یافت.
اظهارنظر اخیر رئیس‌جمهور ایالات متحده در حالی است که ایران گفته برنامه‌ای برای مذاکره با آمریکا ندارد و شروط متعددی را برای توافق با واشینگتن اعلام کرده است.
در همین حال، اسکات بسنت، وزیر خزانه‌داری آمریکا در راستای برنامه فشار اقتصادی بر ایران موسوم به «عملیات طرد اقتصادی» از همه افشاگران خواست تا چنانچه اطلاعاتی درباره «تسهیل‌گران تروریسم ایران» دارند در اختیار وزارتخانه تحت امرش قرار دهند.
او با انتشار پیامی در شبکهٔ اجتماعی ایکس خطاب به کسانی که در سراسر دنیا اطلاعاتی درباره شریان‌های حیاتی اقتصاد ایران دارند، نوشت: «این شانس شماست. اگر اطلاعات قابل پیگیری برای وزارت خزانه‌داری دارید، ممکن است واجد شرایط دریافت جایزه باشید، صرف‌نظر از این‌که کجا زندگی می‌کنید یا چه کسی فیش حقوقی شما را امضا می‌کند. اگر چیزی دیدید، بگویید».
او همچنین بار دیگر تاکید کرد که وزارت خزانه‌داری آمریکا عملیات طرد اقتصادی را «برای قطع تمام شریان‌های مالی رژیم ایران و حامیانش» آغاز کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/78374" target="_blank">📅 19:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78372">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/078a1aea27.mp4?token=iEq3bB-VCzxwNt6_S9WJ9BfOReNHBXW1pX4lXtqVr913rg4YiEsdzHuGmKhQtFt_jmgwsy9FApANj_MhlD5BL4G9ZteuvEFMpQ48q9YcYTIEQrjsEor6sBWRrjUDyC71Y2mtXT7pTNGSdzD-dQPzd63St5x68E34EmmyLgcK7uxlBSrOpUBjdrUih7l8PdnqfafmI4fLyz5yv4TGYAOJhhOGrg1Y7zs7TbnmHOMZz7NglrotWulotFUKnuUrBfyJJjeNBiY6KsH8fOHvpLOfxzFBx-aFv5pLa9Z90hlMPxeNvsIIWHirkjrVEpSfumjen_E00SNTMbUqB9YenQK8iA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/078a1aea27.mp4?token=iEq3bB-VCzxwNt6_S9WJ9BfOReNHBXW1pX4lXtqVr913rg4YiEsdzHuGmKhQtFt_jmgwsy9FApANj_MhlD5BL4G9ZteuvEFMpQ48q9YcYTIEQrjsEor6sBWRrjUDyC71Y2mtXT7pTNGSdzD-dQPzd63St5x68E34EmmyLgcK7uxlBSrOpUBjdrUih7l8PdnqfafmI4fLyz5yv4TGYAOJhhOGrg1Y7zs7TbnmHOMZz7NglrotWulotFUKnuUrBfyJJjeNBiY6KsH8fOHvpLOfxzFBx-aFv5pLa9Z90hlMPxeNvsIIWHirkjrVEpSfumjen_E00SNTMbUqB9YenQK8iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رشت، حامیان حکومت شبانه به آشکده سحرخیزان حمله کردند.
در ویدیویی که آشکده سحرخیزان منتشر کرده بود، عبارت "آش برای افراد با حجاب رایگان است"، به دیوار نصب شده بود و در چرخش دوربین، چندین مرد محجبه در صف ایستادند.
همین بهانه‌ای شد برای یورش و تخریب مغازه.
این اتفاق یکشنبه، ۲۲ شهریور ۴۰۵ رخ داد.
دادستان بلافاصله علیه آن اعلام جرم کرد و مدیر رستوران بازداشت و خود رستوران پلمب شد. ولی انگار این واکنش از نظر لباس شخصی‌ها کافی نبود و دیشب ریختن رستوران رو تخریب کردند.
via
pkhwshhal
,
yaghma_fashkham
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/78372" target="_blank">📅 18:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78371">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشگاه تهران - دانشجو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuUN4M74OCkJGyaLd7T6FecSpKTiT764c-NVtC5ftiLu5VbVlKJUJdyoEcY97r2hDi3w0Kk_OHNjGjuP1e4sIr77T2LQb28GKEUqMffc597Px8i-WqajaAC_CSt4Nnw_j2o8dLSvALwytUuVlT5cETglPR5CQOCmU0szA35FyXZnjbtoi7wbZSMLVVT3lN-8T2yv2zRkQ9w-JLCZYBjHQZaJYLaoxkI-nidvkveaFFmIra8CxkosSTn5YOsM44HciTuhbgMY4jzCkK1XVRC-Be7jULDYhIFrkuI5JoYyycdd0Hh8_9jDzXE0v7IexHsTxSUz0wK8qEcPqIxZXRkXCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
اتهام «بغی» برای محمدپارسا گلچین، دانشجوی دانشگاه تهران و دارندهٔ مدال طلای المپیاد!
بنابر گزارش‌های رسیده به تهران-دانشجو،
#محمدپارسا_گلچین
، دانشجوی ورودی ۱۴۰۳ کارشناسی ادبیات دانشگاه تهران و دارندهٔ مدال طلای المپیاد ادبی، به «عضویت در گروه
باغی
» متهم شده است.
همچنین، «اجتماع و تبانی علیه امنیت داخلی» و «اقدام تبلیغی بر خلاف امنیت ملی» دیگر اتهاماتی‌ست که به این دانشجوی نخبه وارد گشته است. او در جهت دفاع برابر عناوین مذکور، به شعبهٔ ۲۶۸ بازپرسی دادسرای عمومی و انقلاب مشهد احضار شده است.
محمدپارسا گلچین، شنبه ۲۲ فروردین ۱۴۰۵ به همراه جمعی ۱۸ نفره از دانشجویان در جریان یک بازدید دوستانه، توسط مامورین مسلح و به‌طرز خشونت‌آمیزی بازداشت شده بود
. پرونده سایر بازداشت‌شدگان نیز در جریان است و در انتظار دریافت حکم و احضاریه هستند. درصورت دریافت اطلاعات تکمیلی، گزارش پرونده‌های سایر دانشجویان متعاقبا در تهران-دانشجو منتشر خواهد شد.
#سرکوب
#بازداشت
#دانشجوی_زندانی
دانشگاه تهران-دانشجو
اینستاگرام
🆔
@Daneshjo_UT</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78371" target="_blank">📅 17:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78370">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d288c0bbe.mp4?token=MMjX94WmSgAqZ6j1pkUF2wg3tfTdZE0TtGkPsMb2j_eKTMCXwHAsiituBaqrrYDiDCHg899JHQNtAy8YF2ICAWVL_Y-TQO1GPeo_NSNQEf4Wzxz8wpeaZWyyS0NQpbvOQ8XOKv9_JXzWJMAsSMGGwJDB5_jW0yHvAzj-maiyddZTU-_k5x-u6iMcEq4hPSNAeFlwBSNSKoGwbDO6vCTRZQC5RxjL8mn8EMLfllAnanAfqcR1R3LQ4_TEl0nK6GWQ0YbVHoSDSiBZFquKHSJo4AxyEwl8LvPlVHYGX-W17ePx7TtCVWqVUi0iXbEj0_SFyQcmMKv8MkC6EUpsEBIAPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d288c0bbe.mp4?token=MMjX94WmSgAqZ6j1pkUF2wg3tfTdZE0TtGkPsMb2j_eKTMCXwHAsiituBaqrrYDiDCHg899JHQNtAy8YF2ICAWVL_Y-TQO1GPeo_NSNQEf4Wzxz8wpeaZWyyS0NQpbvOQ8XOKv9_JXzWJMAsSMGGwJDB5_jW0yHvAzj-maiyddZTU-_k5x-u6iMcEq4hPSNAeFlwBSNSKoGwbDO6vCTRZQC5RxjL8mn8EMLfllAnanAfqcR1R3LQ4_TEl0nK6GWQ0YbVHoSDSiBZFquKHSJo4AxyEwl8LvPlVHYGX-W17ePx7TtCVWqVUi0iXbEj0_SFyQcmMKv8MkC6EUpsEBIAPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صفحه اینستاگرام رستوران «دستپخت بی بی» در تهران، به دلیل انتشار یک استوری با نوشته «هیچی کتلت بی بی نمیشه» به همراه موسیقی متن «بی بی گل» از معین، به اتهام «انتشار محتوای مجرمانه»، با دستور قضایی مسدود شد.
پیش‌تر نیز در سال ۱۴۰۱ نواب ابراهیمی، آشپز، در پی انتشار دستور پخت کتلت در اینستاگرام خود همزمان با سالگرد کشته شدن قاسم سلیمانی، بازداشت شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78370" target="_blank">📅 17:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78368">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jCvDjSARdB2KG1pVHQCyHa80CGnV3u8vIrJWcdoVc4oWbeqUrfpxESlxDy_cUtCbwMSocCVK5GLFIrAqmdeRSm1aKtHDbiWQuxFHTTEF45xr-RUTHSJYNKN1xmbYSqQT6PuIbOVwLoEMRNtz4D55s9X7lWeaAKngOQM_3irdeKX_H8u6Fw40o6TaNSXh3ak8TluygjZD6QfankdHUeILn_Dkp3Xzr_BYAFYwBaIwPpJ4gOM-q2mGIzDo8nBR6_FD0WArQXfS-5TzQH7-ObMZI4gypy-PMDeqW_JZt8tS8m92eRciydBkv8GqsnXc8sa1bhYUUATHTgFEQgM-gQ-rEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BxewM0iUx1mttOZoYCr6WW7ukm1Z5dy6cW64i6YK6dBtD6gCE275fhsL7GzkdPhcstIaNQj0CoOvvfm4f5ShTqJdZDuOUgF5-Vuff0rV8-usWnVnmz1Ko46Gg9VoPxrQz3qFBy7us6qMKc2ezSWe3y4RIFYg_fWEeGZhY7HnqY_Nk6aPHNYGfrJ4UrnJwPXEGfhHKJGdMxHN3yIV6jU-8pWghlKVK_byKWUmrfPSbND2Z-w9OFoRwH7I6hjyBF4MTzFU-OTV-21YK8JjA7U9cvuAt3PvXeLFYfZrbSacrtbcFamAPlic-UQjFp5L2_HCmp_tNNnOZzefBwTfTIfyyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«یحیی سریع»، سخنگوی نظامی حوثی‌های مورد حمایت جمهوری اسلامی، از انجام عملیاتی گسترده با ده‌ها پهپاد و موشک بالستیک علیه اهداف نظامی در منطقه خمیس مشیط عربستان سعودی خبر داد.
سریع گفت پایگاه هوایی «ملک خالد» در این منطقه هدف حمله قرار گرفته و آشیانه‌های جنگنده‌ها، رادارها، باندهای پرواز و انبارهای مهمات از جمله اهداف حوثی‌ها بوده‌اند.
سخنگوی نظامی حوثی‌ها این عملیات را پاسخی به حملات هوایی عربستان سعودی به یمن دانست.
@
VahidHeadline
«محمد بن سلمان»، ولیعهد عربستان سعودی، امروز دوشنبه ۲۳شهریور۱۴۰۵ در جده با دریاسالار «برد کوپر»، فرمانده فرماندهی مرکزی آمریکا، سنتکام، دیدار و درباره تحولات اخیر منطقه گفت‌وگو کرد.
خبرگزاری «رویترز» به نقل از رسانه‌های دولتی عربستان سعودی گزارش داد این دیدار در شرایطی انجام شده که درگیری میان عربستان و حوثی‌های مورد حمایت جمهوری اسلامی در یمن شدت گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/78368" target="_blank">📅 16:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78367">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oybm5_aFyAhpK2_lANmoqkw18lDbIzUkxmJNgqJXZn22HVPs00GiinmFrZ_wiPTD3Uc_PagHUEtapxNXsnZiUP-sLzHSKoa4ZsYDl24WXPp883F9FYLMxQOHLFZVpmpcmbMfmA7wQoZiyDoZdkjGAcOjiaI3ZzkvJ7o9YujUrqRv0Sybs5Mgb3Kn8J9t2RMC5x4zHg3piSMbCzEJ6oR7Or6_txj9Z795bs0gg81d7ja9RYVvLuA2UEumkcwrUftpqoqvQ2Q0WigwTSkg6Tmwp7_bm453KhGla9rgvCCCKoYO-QpiuUd_SetHnqfwGyD5ELYPt2DmxGJXQXx4HrojJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین امروز دوشنبه ۲۳شهریور۱۴۰۵ گزارش‌ها درباره کمک نهادهای چینی به جمهوری اسلامی برای هدف قرار دادن یک پایگاه نظامی آمریکا در اردن را تکذیب کرد.
خبرگزاری رویترز به نقل از وزارت امور خارجه چین گزارش داد پکن «قاطعانه با این اتهامات بی‌اساس مخالف است».
این واکنش پس از آن مطرح شد که روزنامه «وال‌استریت جورنال» به نقل از مقام‌های آمریکایی که نام‌شان فاش نشده است، گزارش داد جمهوری اسلامی پیش از حمله موشکی ۱۷شهریور به پایگاه «موفق‌السلطی» در اردن، تصاویر ماهواره‌ای این پایگاه را از نهادهایی در چین دریافت کرده بود.
در حمله موشکی جمهوری اسلامی به این پایگاه نظامی آمریکا، سه نظامی آمریکایی کشته شدند.
براساس گزارش «وال‌استریت ژورنال»، مقام‌های آمریکایی نام نهادهای چینی را که گفته می‌شود تصاویر ماهواره‌ای پایگاه را در اختیار جمهوری اسلامی قرار داده‌اند، اعلام نکرده‌اند. این مقام‌ها همچنین دولت چین را به مشارکت یا دخالت مستقیم در این اقدام متهم نکرده‌اند.
«دونالد ترامپ»، رییس‌جمهوری آمریکا، نیز روز یکشنبه ۲۲شهریور۱۴۰۵ به گزارش‌ها درباره دسترسی جمهوری اسلامی به تصاویر ماهواره‌ای یک پایگاه نظامی آمریکا در اردن از طریق نهادهای چینی واکنش نشان داد.
ترامپ گزارش مربوط به دستیابی جمهوری اسلامی به این تصاویر، پیش از حمله‌ای را که به کشته شدن سه نظامی آمریکایی منجر شد، «کم‌اهمیت» دانست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/78367" target="_blank">📅 16:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78365">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dA2_niAiydzhPYp_kc6_0YihX0Cno65mNAueck75-PzRjodZudrJk5Aka9YT69-azn1Gs0E6iaszBUGbogNGKRJltqaVPyDnfHgtX18-OlDXGD2GO0rqX6zpkovpPTSdUvL-ffVjah4-cPW0f5UW4dAmSb8m4LTmG2D2DOC_QihLzOVjXcrhE9qgUUvzsykZiB6LnH5DGbD_LsW_fXl0t8p2sbtnlIIYm9Lioeeg7gAocM0498Zs2BJA_825sb8oP1ofR1UuojKp-bLTqm-2GsjqnaTCyAHr1V-lMaoW-bIfrYIQtF61KPeAFXScJWwReQKPhsLcKzUcE-l_Md2d4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f2Jp3fynDSdzGAy8bhAlhgx7hGSpemHPBYMZxefDkUjXFLhQygw7R5kDAv5QQwJmw24QXb6WG_3J9gCRq0F5ECx9cqgG55mn4g9SvX-jkH6q2vMwPjKt6l7meV6sTg0f13-BoGzcWyEAWNIbJ1QfHAaVBeytSRkmiWzDjSoqGn1X2oD-qAwTnwf1ooMYQSlQLRr9tJg4NOHNRSCvXzugTyAhe5xa-yuSTrk-jDY758V8GDETuUEM6MsuI7aRyQTvUC9SBhiCbWSyMw1g0Dr9Yae8Cws0mu2vKvwSnK8TDfi3iteH_VuF9uC3XXYlwtScIFJ2n0CtSOfpb0WOTFTFkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی روز دوشنبه و پس از اعلام خبر صادر نشدن ویزا برای محمد اسلامی، رئیس سازمان انرژی اتمی ایران برای شرکت در نشست مجمع عمومی آژانس بین‌المللی انرژی هسته‌ای در وین، از احضار کاردار اتریش در تهران خبر داد.
بقایی با اعلام این خبر گفت می‌دانیم که این تصمیم تحت فشار آمریکا گرفته شده است اما این واقعیت، چیزی از مسئولیت اتریش کم نمی‌کند.
@
VahidOOnLine
پیش‌تر:
به گفته یک مقام آگاه که با اسوشیتدپرس گفتگو کرده، محمد اسلامی، رییس سازمان انرژی اتمی ایران، برای نخستین بار در چند سال گذشته احتمالا در نشست سالانه کشورهای عضو نهاد ناظر هسته‌ای سازمان ملل متحد در وین شرکت نخواهد کرد، زیرا از سفرهای بین‌المللی منع شده است.
این مقام گفت اتریش از کمیته تحریم‌های سازمان ملل خواسته بود برای اسلامی معافیت از ممنوعیت سفر صادر شود، اما این درخواست پذیرفته نشد.
این مقام که اجازه اظهارنظر درباره این موضوع حساس را نداشت، به شرط ناشناس ماندن صحبت کرد.
اتریش به عنوان میزبان سازمان ملل متحد در وین می‌تواند برای مقام‌های تحریم‌شده درخواست معافیت از ممنوعیت سفر کند تا آنها بتوانند در نشست‌های بین‌المللی سازمان ملل حضور یابند.
به نوشته این خبرگزاری آمریکایی، حضور نیافتن اسلامی در کنفرانس آژانس بین‌المللی انرژی اتمی نشانه دیگری از وخیم‌تر شدن سریع روابط ایران و کشورهای غربی است.
از زمانی که اسرائیل و آمریکا در جریان جنگ ۱۲روزه به تاسیسات هسته‌ای ایران حمله کردند، جمهوری اسلامی اجازه دسترسی بازرسان آژانس به تاسیسات هسته‌ای آسیب‌دیده در این حملات را نداده است؛ این در حالی است که تهران بر اساس تعهدات خود در چارچوب پیمان منع گسترش سلاح‌های هسته‌ای، از نظر حقوقی موظف به همکاری با آژانس است.
آژانس همچنین نتوانسته است وضعیت ذخایر اورانیوم ایران با غنای نزدیک به سطح مورد نیاز برای ساخت سلاح هسته‌ای را راستی‌آزمایی کند.
تحریم‌های سازمان ملل که دوباره برقرار شدند، شامل ممنوعیت سفر، تحریم تسلیحاتی متعارف، محدودیت‌های مربوط به توسعه موشک‌های بالستیک، مسدود کردن دارایی‌ها و ممنوعیت تولید فناوری‌های مرتبط با برنامه هسته‌ای است.
با وجود اظهارات این مقام درباره احتمال عدم حضور اسلامی در کنفرانس، خبرگزاری دولتی ایرنا روز شنبه گزارش داد که اسلامی تهران را به مقصد وین ترک کرده است تا در کنفرانس آژانس شرکت کند و با نمایندگان کشورهای مختلف دیدار داشته باشد.
مقام‌های ارشد کشورهای عضو آژانس بین‌المللی انرژی اتمی قرار است از دوشنبه تا جمعه در مقر این نهاد در وین گرد هم بیایند.
آنها درباره بودجه آژانس تصمیم‌گیری و آن را تصویب خواهند کرد و درباره دیگر مسائل سیاست‌گذاری، از جمله پادمان‌های هسته‌ای در خاورمیانه، گفت‌وگو خواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/78365" target="_blank">📅 16:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78364">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gc9HgvEgdlc27IugF22jI4bgy-FV_4e5B618DB0WhPs7wnCx5la4oxVB-gc27bWas-neLihD7EPw0PN9eRiJ6Hb0y-zfeQwyKaQRCNsRYiFyd5Elj-r07CkCbxBaLZI_cnUUW3_l3LHIu-vN_F1rL47NwHt0j-MLhpKySB5ErwIsfA9eYB42VFwGpzk5ChFrLfyC2HtSBxAsfhWjGKosBVLJKH-4nGC6y1fmTqSpTIHVadLFyMTgzWpmOBnINtc_ZwV19gBQI0vFEHAwm5E2jIb5DnseyQt3TN6dfJ8zYMvMMWasLk0GJhoYqbU1smKx8vdYf2mBWXmkhDhQ9ApTmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آستانه چهارمین سالگرد قتل حکومتی مهسا ژینا امینی از اصفهان، رشت، فومن، مشهد و نیشابور ‌خبر از تشدید فشار برای تحمیل حجاب اجباری و حضور دوباره گشت ارشاد، حجاب‌بان‌ها و نیروهای لباس‌شخصی در خیابان‌ها می‌دهند.
یک شهروند گفت در میدان علیخانی اصفهان ون گشت ارشاد مستقر شده‌ است و ماموران «بدون تذکر قبلی»، زنانی را که حجاب اجباری ندارند بازداشت می‌کنند و با خود می‌برند.
شهروند دیگری فضای اصفهان را «به شدت امنیتی» توصیف کرد و گفت نیروهای گشت ارشاد در مناطقی چون جلفا، مرداویج، چهارباغ و میدان نقش جهان مستقر شده‌اند و با زنان بدون شال و روسری، برخورد می‌کنند.
یکی دیگر نوشت: «در اصفهان دیگر ون گشت ارشاد نیست، اتوبوس است. با اتوبوس دختران را جمع می‌کنند و می‌برند.
...
در مشهد نیز شامگاه ۲۲ شهریور، نیروهای مسلح وارد پارک ملت شدند و به زنان تذکر حجاب دادند.
شماری از شهروندان از رشت گزارش دادند برخوردهای قهری درباره حجاب اجباری در این شهر شدت گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/78364" target="_blank">📅 16:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78362">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bc68687ab7.mp4?token=uLVHm9Hq3tIUT3M9Z5rrDWRpQYItp_UKQaoBh7zClMMtzyMK1WmzK8g4PtDgSuGMsrq1BhCD4LIM4EpCx7RuHq8l6KPb1v6QMZhoXlg3-GQTMR51_SiacAcQQiktOceMUlNMILZd81Hc0Fpj8SFWTUlqCqt-2b7Pl5nC-yfVwJYsyRLHKjudA7LYP-NeCh0yoBqNhv8-K5VwKCKRYd0zxuCH3uiia1UuOueMaOL8gEeOrBEN6XSYsjDlF1bp7gIGZKYeSaagblyeqdY4j2p_P55XNM__ciXs40zfOiLDl8xGUK8kW-55RRmLDJnNWetIsV9b9jPe1bprAwLuePbuYg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bc68687ab7.mp4?token=uLVHm9Hq3tIUT3M9Z5rrDWRpQYItp_UKQaoBh7zClMMtzyMK1WmzK8g4PtDgSuGMsrq1BhCD4LIM4EpCx7RuHq8l6KPb1v6QMZhoXlg3-GQTMR51_SiacAcQQiktOceMUlNMILZd81Hc0Fpj8SFWTUlqCqt-2b7Pl5nC-yfVwJYsyRLHKjudA7LYP-NeCh0yoBqNhv8-K5VwKCKRYd0zxuCH3uiia1UuOueMaOL8gEeOrBEN6XSYsjDlF1bp7gIGZKYeSaagblyeqdY4j2p_P55XNM__ciXs40zfOiLDl8xGUK8kW-55RRmLDJnNWetIsV9b9jPe1bprAwLuePbuYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ویدیوی نجات خلبان آمریکایی در ایران
۲- یک نفر از ۷ نفر سوت موشک که داره به سمتشون میاد رو می فهمه.
سعی می کنه به نفراتش خبر بده اما نمی دونه کدوم طرف بدوئه. در نهایت یک انفجار هر ۷ نفر رو می بلعه.
A_z_im
سی‌بی‌اس پس از پنج ماه با یکی از دو افسر ارتش آمریکا گفتگو کرده است که در نیمه فروردین‌ماه هواپیمایشان در اطراف اصفهان سرنگون شد.
این افسر که براوو معرفی شده، لحظه برخورد موشک دوش‌پرتاب با جنگنده اف-۱۵ آنها را مانند برخورد یک قطار باری توصیف کرد و گفت به همراه خلبان که در این گزارش «آلفا» معرفی شده، تلاش کردند هواپیما را نجات دهند اما خیلی زود دریافتند که امکان نجات هواپیما نیست و باید خروج اضطراری انجام دهند.
پس از خروج اضطراری (ایجکت)، آلفا و براوو در حالی روی زمین در بیابان ناهموار در ایران فرود آمدند که حدود هشت کیلومتر از یکدیگر فاصله داشتند و هرکدام تنها بودند.
آلفا سالم فرود آمد، اما براوو خوش‌شانس بود که زنده ماند.
براوو گفت: چتر نجاتم در حمله اولیه آسیب دیده بود. یک لحظه به بالا نگاه کردم و دیدم چتری وجود ندارد؛ ترسناک‌ترین چیزی بود که در تمام عمرم دیده بودم. همان‌جا مکث کردم و دعا کردم: «خداوندا، اراده تو انجام شود. اما اگر قرار است از این ماجرا جان سالم به در ببرم، به کمک نیاز دارم.»
او در پاسخ به این پرسش که «فکر می‌کنید هنگام برخورد با زمین با چه سرعتی حرکت می‌کردید؟» گفت: براساس توضیحاتی که دادم و جراحاتی که داشتم، متخصصان معتقدند با سرعتی بین ۱۱۳ تا ۱۶۱ کیلومتر در ساعت با زمین برخورد کردم.
او افزود: یک معجزه در روزگار مدرن بود. باور دارم این اتفاق گواهی بر لطف خداوند در زندگی من است که باعث شد از آن لحظه عبور کنم؛ به‌گونه‌ای که هرچند دچار جراحت شدم، اما آسیب‌های فاجعه‌باری که می‌توانست توانایی‌ام برای زنده‌ماندن را از بین ببرد، متحمل نشدم.
این سقوط باعث شکستگی کمر براوو شد. او همچنین دست و شانه‌اش شکست، مچ پایش پیچ خورد و سر و صورتش بر اثر بریدگی و خراش خون‌آلود شد.
براوو گفت، مجروح بودم، اما همه ما آموزش دیده‌ایم که با شرایطی که با آن مواجه می‌شویم سازگار شویم و بر آنها غلبه کنیم. با وجود جراحات، تا جایی که می‌توانستم سریع از محل فرودم دور شدم.
براوو به سی‌بی‌اس گفت امن‌ترین جایی که می‌توانست به آن برود، ارتفاعات بود.
بنابراین با وجود شکستگی استخوان‌هایش تصمیم گرفت از مسیر کوه بالا برود و خود را به خط‌الرسی در ارتفاع حدود ۲۱۰۰ متر، برساند.
@
VahidOOnLine
چیزی که می‌بینم رسانه‌ها و کاربران فارسی‌زبان دقت نمی‌کنن اینه که این مصاحبه نمی‌گه که افسر آمریکایی با دست و پای شکسته کوه ۷ هزار پایی رو بالا رفته؛ بلکه می‌گه خودش رو به ارتفاع ۷ هزارپایی رسونده. بین این دو تا خیلی فرق هست.
در نظر داشته باشید که خود اصفهان بین ۱۶۰۰ تا ۲۰۰۰ متر از سطح دریا فاصله داره. یعنی ممکنه ایشون فقط با صد متر صعود خودش رو به ارتفاع ۷ هزار پایی برسونه.
Ardeshir
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/78362" target="_blank">📅 08:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78361">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cWp4cT457BLK9s6Cluz-nb7szEsSPib7b0gZdS6-Xx523KZUihVYjKCXAVZ4yUHidPjIzl0gDLuqd8AJpB6oqKx46iNxlV6g-kx5TWyY0YFyBL6DMDDL5DnBt47cqH39CoW_A4fG-dMiR5biNq45x4rNwx4sC2M_UVQ1Q0-w4qZbNHqIcBzo2n_WQa7TLXHESfPpIAkUxHIasp28OjuPwx2zzlv0xXNg9GiRUCgmDPLg3y9sd4A4wXRfGFYz9sLnQU8qTNC81AanLCAsMuriWL1IFu1N-7_euE_8YBIOdNVOLPjXwFNEg4pR45xyU_yQpb9jGJ-it53WKo3oGF-hIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه عمان از تعویق‌ نشست ایران و کشورهای حوزه خلیج فارس و منطقه خبر داد؛ نشستی که قرار بود روز دوشنبه ۲۳ شهریور در شهر صلاله عمان با محوریت وضعیت تنگه هرمز برگزار شود.
بدر بوسعیدی، وزیر خارجه عمان، روز یکشنبه ۲۲ شهریور در شبکه ایکس نوشت که این نشست «به منظور دستیابی به اجماع» به تعویق افتاده است.
او تاکید کرد عمان همچنان به تقویت گفت‌وگوهایی که به «ثبات و همکاری پایدار در منطقه» کمک کند، متعهد است.
عباس عراقچی، وزیر خارجه جمهوری اسلامی، پیشتر گفته بود که روز دوشنبه در نشست هشت‌جانبه وزرای خارجه کشورهای ساحلی خلیج فارس و دریای عمان در صلاله شرکت خواهد کرد.
قرار بود در این نشست درباره طرح ایران و عمان برای ایجاد سازوکاری جهت تردد امن کشتی‌ها در تنگه هرمز گفت‌وگو شود.
تعویق این نشست در حالی اعلام شده است که آمریکا پیشتر تاکید کرده بود در مذاکرات مربوط به تنگه هرمز مشارکت نخواهد کرد و هرگونه مذاکره مستقیم با جمهوری اسلامی را بر پرونده هسته‌ای متمرکز می‌کند.
مقام‌های آمریکایی به کشورهای منطقه گفته‌اند واشنگتن درباره وضعیت تنگه هرمز مذاکره نخواهد کرد و موضوع اصلی مذاکرات احتمالی با تهران باید برنامه هسته‌ای جمهوری اسلامی باشد.
مارکو روبیو، وزیر خارجه آمریکا، نیز پیشتر گفته بود تنگه هرمز نباید تحت کنترل جمهوری اسلامی باشد و آمریکا برای تضمین امنیت کشتیرانی در این مسیر اقدام خواهد کرد.
در مقابل، جمهوری اسلامی و عمان تلاش کرده‌اند کشورهای منطقه را در گفت‌وگو درباره سازوکار تردد کشتی‌ها در تنگه هرمز وارد کنند.
قرار بود نتایج رایزنی‌های تهران و مسقط درباره مسیرهای امن کشتیرانی در این نشست به کشورهای منطقه ارایه شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78361" target="_blank">📅 22:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78360">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhXL9HBEIBJM0_zZ6S8Zxs69qAWHGrMnTHVT1r6msziha4MMbBjDFSBF1FSpeIOF1HGEZTh3MsBRZfZcD8bLOR7ag_3lnbEWNPpAVHcljE52S8mo3Hqe-k_fX2sXbxd4LY0_ZNjQh6b9W7tLeDaX0lJ8GJEi6elzWg2cxtFj0Y4wGrqiGO6g52KAjpdhrNejtzTi9P-iFmZ96b4nHzIEC_uynbjI9mjK5zJuh68Ls_nPic9F30MOAf1VWyoji1N6stQj04WYiDfwQeU16TkTbtiiLpff_lwxtOMI__-NYf4k4j_lnqyYvrOt6_WEZ43AXqMHZXWFHR5u5i8pk_-ifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه نیویورک تایمز روز یکشنبه ۲۲ شهریور ماه در گزارشی به نقل از چند مقام ایرانی نوشت، مسعود پزشکیان، پس از حمله نیروهای سپاه پاسداران به سه کشتی تجاری در تنگه هرمز در اوایل تیرماه گذشته، به‌شدت خشمگین شده و این اقدام را «بی‌پروایانه و غیرمسئولانه» خوانده است.
این حمله‌ها که منجر به آتش‌سوزی یک نفت‌کش حامل گاز مایع قطر و آسیب به شناورهای دیگر شد، درست زمانی رخ داد که ایران به توافقی با ایالات متحده برای پایان دادن به درگیری‌ها نزدیک شده بود.
بر اساس این گزارش که فرناز فصیحی به نقل از مقامات ایرانی نوشته است، پزشکیان پس از آگاهی از این ماجرا با احمد وحیدی، فرمانده کل سپاه پاسداران، تماس گرفته و با لحنی تند خواستار پاسخگویی شده است. با این حال، وحیدی ضمن سلب مسئولیت و ابراز بی‌اطلاعی، به رئیس‌جمهوری اعلام کرده که نه مجوزی برای این اقدام صادر کرده و نه شورای عالی امنیت ملی از این عملیات مطلع بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/78360" target="_blank">📅 22:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78358">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/930e263d13.mp4?token=nsqooaPMx8l3kzmznwk3CbccRilnZVaWRmy8gHCy47gSyLS_BDnwKhUY7fUQYC38W_2qiXVTfGJmj7gS0jiPPOc3nN8rfZGOLg3i4l3rFXaNauT0c56Z7-P51iP5sRTSR_kvBxKBRJpLXznWFWuLOEgOp6FvR9YPyzram4Uxd33xXxuO5mwcI24ROC_rmyBqB0lqxLa4hicjrmnzyqR02NaHMM0d6x_L9k8YOpzHFAsYkzDP-CIk0dSIuMMNI6YelVkagSk-S6uK4Ch24uLRcNop3j4k-5NZZE56YoM8LKUTUKCbO_YEc20X8YPKdHMPIf1X5F_8GemCpo7NIjGNCg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/930e263d13.mp4?token=nsqooaPMx8l3kzmznwk3CbccRilnZVaWRmy8gHCy47gSyLS_BDnwKhUY7fUQYC38W_2qiXVTfGJmj7gS0jiPPOc3nN8rfZGOLg3i4l3rFXaNauT0c56Z7-P51iP5sRTSR_kvBxKBRJpLXznWFWuLOEgOp6FvR9YPyzram4Uxd33xXxuO5mwcI24ROC_rmyBqB0lqxLa4hicjrmnzyqR02NaHMM0d6x_L9k8YOpzHFAsYkzDP-CIk0dSIuMMNI6YelVkagSk-S6uK4Ch24uLRcNop3j4k-5NZZE56YoM8LKUTUKCbO_YEc20X8YPKdHMPIf1X5F_8GemCpo7NIjGNCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز پیش، پس از اعلام نرخ سوم بنزین در ایران، تصاویری واقعی در شبکه‌های اجتماعی منتشر شده بود درباره اینکه بعضی از تلمبه‌ها در جایگاه‌های سوخت (پمپ بنزین) امکان نمایش همه ارقام بنزین ۱۰ هزارتومنی رو ندارند و مجبور شدند در ادامه نمایشگر یک صفر بچسبونند روی بدنه تلمبه.
حالا محمدباقر قالیباف، رئیس "مجلس شورای اسلامی" در «ایران»، اون انیمیشن رو پست کرده.
ولی درباره قیمت سوخت در یک کشور دیگه:
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78358" target="_blank">📅 21:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78357">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkTgsLcrNnGL9KhEl5-OrMJ3eS2lN0lxiyoiCDxVfJMfHIhLrFslMx4p0hUi0f4zwUS6YnG11wR6zBrhAptPztNw9djLCMkxX2Vx3ogBUauP5jlRTlTd3poh_m7AcBst4cSQCDslsRgSIJLYR0pmppAFAFK4f1Sn5gspAUxemHKkcuaJ0jtWe2MNZiX2DG-UgEoROybSaZC8Y39xBcLMYkiRMSjmHlFKXyFs4vSDhv1RcwuMCuLQoh56H0qLPWwF6Y_KXdw4iemq-qDNJ0to8AjNVaRjAgIoRA6dMeplndXXzOJ43qRm9lUL5lWU3mN7UoQCwXbWA-inTYmNYs4yxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین رسولی‌نسب، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در شاندیز، به اتهام «محاربه» از سوی دادگاه انقلاب مشهد به اعدام محکوم شده است. او در حال حاضر در زندان وکیل‌آباد مشهد نگهداری می‌شود.
خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، روز یکشنبه ۲۲ شهریور ۱۴۰۵، گزارش داد حسین رسولی‌نسب به «محاربه از طریق مشارکت در تخریب اموال عمومی» و «اجتماع و تبانی علیه امنیت کشور» متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78357" target="_blank">📅 18:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78355">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kmM9b4hsR6wS4BsN616fPY0WcINHxftSSc7iY3YwjOaMAAsA8hL7R416f8Zh7oUGq7O1lx9FV0_tAcEPrRcK9ahlZptHqoFs7gyecDb3IdLyZ_Hje6OeWyuSOHxGRQdyIqR7B1zSg4LqrKwRTNsPUDdTIp2LBua_2V0sPRjC6avUzZ0TXn9p9vf1ZNhwKEPd16Q9TNlD80vLildDQi_7Odi8Y9Vew5Xg-SSK57GreF1EqMqlO0MsgcV0-CSdVQFw58qhhatkNIx7wx4VqSpnsKgUoNOOtBUNtoU1Nti73WB-DDtt-faupP_y1VbLNpGKOzzdG2E9wpKPNHOcZCt3hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DJurdsyQzW2FgDe_4_emQdXU95Htu6XEm_nmkYYCVgcQmryiX6ZwA_pGqNMPWqW0mFtPmTg6JomaMYprsYMu8dY0UC-z8wdCdVXxDSEyDEaXnBv3A3frr8drCI0qu28qLX6cujy8EADAYrz4KefXTQkAXHJlqE3H2_-DYNdk0Ji1QSjZllPK-p_qK8knfcBqX95vwcBl52WKeeC9ilZRJfO7puwpyeQYwv48LQUgMM9pNeI_BsrPtBc3D95bflP56xJeU5HOyXQH24A_02GDc9PRmIpqWr6Mkx7QK0zlYWqqQIu-nNVWuk9LI3HdY7jisWveHl7P6jcsq2R9vTSztQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان ثبت احوال: در کارت ملی‌های جدید از هوش مصنوعی و بلاکچین استفاده کرده‌ایم
quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78355" target="_blank">📅 18:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78354">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FPx4NcM8D-a1f2LRCtyGJ4Z5OzqzJNoF0jALPAqa-3zdmS_hljrVjyOE9kygPCRByhzcVM0geMmjSj3sjZDLHuHkDdNx1ateI_DLe2g1J1RLNVJfq5jjLOk0_mm20TpsAH0g6YEJGGLBjHcnAAnMJcvIA4EmG-J-rYxLE5IEBgaMHOAJ7wnEkuouxrvqIbfuXA-n2rPM9Q63lK6_2Rcc9Nf4_NFK-b7KR-aBjARs5TshvWckyenXffCW6IvWYEY7Ui_uPJGItRrc3AuWe3ZXp1LHVa_qw5E2a5g7-HtFafVURGnujLRzPLwjLNdwOZC_uS8zcZx6EGH9rdZ_EthSOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز یکشنبه ۲۲ شهریور۱۴۰۵، گفت «موضوع ایران» ممکن است پیش از انتخابات میان‌دوره‌ای آمریکا پایان یابد، اما در هر صورت جنگ با ایران بلافاصله پس از این انتخابات تمام خواهد شد.
ترامپ در جریان سفر به ایرلند و در حاشیه مسابقات گلف اوپن ایرلند، درباره احتمال توافق با جمهوری اسلامی گفت ایران به‌شدت خواهان توافق است و به‌طور مداوم با آمریکا تماس می‌گیرد، اما واشنگتن تنها توافقی را می‌پذیرد که به گفته او «درست» و مطلوب باشد.
او همچنین در پاسخ به پرسشی درباره دیدار وزرای خارجه کشورهای خلیج فارس و دریای عمان با ایران گفت این موضوع برای آمریکا اهمیتی ندارد و تصمیم درباره دیدار با جمهوری اسلامی به خود این کشورها مربوط است.
قرار است این نشست روز دوشنبه در عمان برگزار شود. ایران می‌گوید یکی از موضوعات مورد گفت‌وگو در این نشست، مسیر جدید تردد در تنگه هرمز خواهد بود.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، نیز بار دیگر گفته است شرط ایران برای بازگشایی تنگه هرمز، بازگشت آمریکا به تعهدات خود در تفاهم‌نامه اسلام‌آباد است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78354" target="_blank">📅 17:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78352">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rDJAjMDn-DZJWwJzsSQmgapvkF9mXpxLmr-rT00cQb8FswhgkDe0oDJwPcGV3vh1A344TFNRTtKGAGqard69vx52AV1FG3xsPT_p5oTPxKokvupQ03rusdA0rt48RjBavQy0qELvI3J6raj3n3_dbnk0wuSYW_epeow8mzUaZLW80PSoSre_Lp7NIJ99nYOcX4fdMqA-SXa9d3PxRehVC6IHwNEmyBh3waMvP8wtzvymX-OU98VUXUQ5YoTVK2I9Rs1FK8829kU0KWsGpBAHKPRem9zjF-nnpg4KBFlq5UQK_16yCmfEQMd51e4oo74oye4U9CNjZSV-Eenmvuu4Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AZFCuioIyMuB1SX1lrrdEFs0ggHKEDPRLeuU1iZmIPENI63VWMDSBQG1TF8uHwEJ4wbm7ODxgmiRs8_PcR2pwUMMaHUjmRBZTHMFAAfzQ5JOXzrmkhrHlx3lC0qp9neiFda7AH8ud4OylmVHHo5wOb8Fpfjd70kqgFfEHFzcz7tmHLn7m3Tai1-UYS9Idae1icdttqCS9RJ9MWPr0sejEaHn7clykimJbL61E0unBYEp-x-pwO-F7A0Amnx2GY95f8B4F27Ih5vnqNHo0CDbIlrXlZpIlJuM667jWQBswJz2kaTCmej5U9jj0byBOdvMuy5hkJ1synQ1dYpeu7mQlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) روز شنبه، با صدور یک هشدار امنیتی، از هدف قرار گرفتن یک کشتی در تنگه هرمز خبر داد.
این نهاد نظارتی دریایی اعلام کرد: «گزارشی مبنی بر وقوع یک حادثه در محدوده تنگه هرمز دریافت شده است. یک کشتی هنگام عبور از تنگه هرمز هدف اصابت یک پرتابه ناشناس قرار گرفته است.»
@
VahidOOnLine
امیر تیموری، فرماندار شهرستان قشم، اعلام کرد یک کشتی تجاری حدود ساعت ۵ صبح امروز در محدوده جزیره هنگام و ساحل شیب‌دراز جزیره قشم هدف قرار گرفته است.
به گفته فرماندار قشم، در این حادثه یک نفر کشته و سه نفر دیگر مجروح شده‌اند.
تیموری عامل این حمله را آمریکا اعلام کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78352" target="_blank">📅 15:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78351">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddbff18bf8.mp4?token=Yc5uJeYgmokNkDUJ1ZNzZB_dH4NIryQxcKjpYqm21xobOWd4uV0RMuqB0YCUlNdXMaze1CLsgi7SpnjmT9r26-QZK3q0MDyESlodlSgfX-wur5KvRWL7tGOi_1OMit_NFTO7W_R-pJ39NMK1FvG7ALMf-iNo7Dp4RipkXgHBUQRpl0P3pyFxJ6uMsjo7-SQwZfMgCe1i9wUtpk4LZOwdhEx6ANie0z8J01vh_92cOS-5q6Rj3u0qG0LmpkNAOnDi5yVkEGNn_eEGDhKeUmB8RoNGNQAeemE4IZoNdClUmJXCHmadRUDEK9C6QunnnqMWSTxrv3sReq-eSSXB8x_SOzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddbff18bf8.mp4?token=Yc5uJeYgmokNkDUJ1ZNzZB_dH4NIryQxcKjpYqm21xobOWd4uV0RMuqB0YCUlNdXMaze1CLsgi7SpnjmT9r26-QZK3q0MDyESlodlSgfX-wur5KvRWL7tGOi_1OMit_NFTO7W_R-pJ39NMK1FvG7ALMf-iNo7Dp4RipkXgHBUQRpl0P3pyFxJ6uMsjo7-SQwZfMgCe1i9wUtpk4LZOwdhEx6ANie0z8J01vh_92cOS-5q6Rj3u0qG0LmpkNAOnDi5yVkEGNn_eEGDhKeUmB8RoNGNQAeemE4IZoNdClUmJXCHmadRUDEK9C6QunnnqMWSTxrv3sReq-eSSXB8x_SOzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تور اجبارى اتاق شلاق براى "عبرت" متهمان
یکی از شهروندان با ارسال ویدیویی که مخفیانه از اتاق اجرای احکام شلاق ثبت کرده، مشاهدات و تجربه مستقیم خود را با بنیاد عبدالرحمن برومند در میان گذاشته است؛ روایتی که به‌زودی در قالب یک شهادت‌نامه تفصیلی منتشر خواهد شد.
او درباره انگیزه خود از انتشار این ویدیو پس از چند سال می‌گوید:
«آنچه در جریان بازداشت و صدور این حکم بر من گذشت، در برابر حجم بی‌پایان ظلم و بی‌عدالتی شاید اهمیتی نداشته باشد؛ آنچه برای من اهمیت دارد، تاباندن نور بر گوشه‌ای از این سازوکار مخوف است تا همگان ببینند مردم ایران برای داشتن یک زندگی معمولی با چه مجازات‌های تحقیرآمیزی روبرو می‌شوند.»
@
IranRights
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78351" target="_blank">📅 15:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78350">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9047a957c6.mp4?token=jQ7iBvZ-BrO82c1MdQv7o5HyLjGiMny3ouPRAbvmYDXgQhuYNS5zD3BA6V_88TBbvJjRweS4cqCkOx5LHJGCnnZ1KFRXmeG0mNfZnjk_iva-7JmeBEHUj6f8sYK4eqddvB3Ffs2wyXzsibgGtvu2pAEoh3dLo_FABBp35gvdMR2hjzcPA3IMjLl2PFdIKk8K7l_4EqTfP1aQJwoCM2mfSpAS72PGNpfKD-ul6ITLN0vFH1U2zUg5XQfzHoiIQF3aHZfFUPPY1M1rkheUQMgbAZ3Y6ZVoSZB9yW0xGAChEzvekxVzoJcDo_1bKkaUK1GeFtF43OzM4GhXINiWaQ1m0w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9047a957c6.mp4?token=jQ7iBvZ-BrO82c1MdQv7o5HyLjGiMny3ouPRAbvmYDXgQhuYNS5zD3BA6V_88TBbvJjRweS4cqCkOx5LHJGCnnZ1KFRXmeG0mNfZnjk_iva-7JmeBEHUj6f8sYK4eqddvB3Ffs2wyXzsibgGtvu2pAEoh3dLo_FABBp35gvdMR2hjzcPA3IMjLl2PFdIKk8K7l_4EqTfP1aQJwoCM2mfSpAS72PGNpfKD-ul6ITLN0vFH1U2zUg5XQfzHoiIQF3aHZfFUPPY1M1rkheUQMgbAZ3Y6ZVoSZB9yW0xGAChEzvekxVzoJcDo_1bKkaUK1GeFtF43OzM4GhXINiWaQ1m0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهوری آمریکا در جریان دیدار با مایکل مارتین، نخست‌وزیر ایرلند، در دوبلین بر اعمال کنترل مقتدرانه و یک «محاصره دریایی باورنکردنی» بر تنگه هرمز تاکید کرد و گفت این اقدامات مانع از جهش شدید بهای جهانی نفت شده است.
دونالد ترامپ همچنین گفت نیروهای سنتکام به‌طور میانگین روزانه ۲۵ شناور و قایق را متوقف و توقیف می‌کنند؛ اقداماتی که به گفته او بیشتر آن‌ها در تاریکی شب و در جریان گشت‌های شبانه انجام می‌گیرد.
این در حالی است فرماندهی مرکزی آمریکا، سنتکام،
امروز
اعلام کرد طی ۶۰ روز گذشته و از زمان ازسرگیری «محاصره دیوار فولادی» ایران، مسیر ۱۰۰ کشتی تجاری را تغییر داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78350" target="_blank">📅 23:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78349">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3mMjfgzhBk9GBjqDihP6jr-olKMuubNhreA7bqxGvZAHCtkcIwLQfasFf9-R3TwNNG5TkhWWpBnKxOfRi6K-_ljhNh1MSeL3ODLsEJkmVNV2ZH5asZOHlYwZFtWc5zrDtYfns_1eY7sGEF5Ui6BBBrz9fBpIrhwg46b_kQ3fdZ9sBhZ_mYy2CS6lpKxjatWaCPAZMOveMyiMHdBhRpux2PdpXz7_WYCdciRmN5RZ1eETBzhP1IxF2F5VGiwPQ9ZjJYf0_U2iITgq17A4DE3hRpFOZawStyAemnVOm-TwGlctp0FvGp0jz6E_yx9GuDhsmZC1Y4MqwSHKN55CQFQ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واژگونی یک دستگاه اتوبوس حامل کارگران مجتمع مس سرچشمه، در صبح شنبه ۲۱ شهریور، یک کشته و ۳۸ مصدوم برجا گذاشت.
سید محسن مرتضوی، رییس مرکز فوریت‌های پزشکی رفسنجان، با تایید این خبر گفت ۳۸ مصدوم این حادثه برای دریافت خدمات درمانی به بیمارستان منتقل شده‌اند. به گفته او، بررسی‌های اولیه نشان می‌دهد ورود یک دستگاه ون به مسیر حرکت اتوبوس باعث انحراف و سپس واژگونی آن شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/78349" target="_blank">📅 21:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78348">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh928axT8g1irXaQtRjid8QbaqsKQSMrTtcHFo9I3_yNq27ga_qZD6FoGtdntYZfP3yB3AQnlLX630YNWJiCGxVI9vqn5bKdBKVKsQT78tCKpKC0AHDD4YFNK50XeQ3PmyXH7zy2inGB-LJQ3eR2_TFjcTJpuqRNwQYTlMaRH6q48rgyiVmxzlq7JE12xYqhyJGInTBpW-WpDPjTk-uwB174v_X6XyNCCrykpYu2RTkIaWifgrTZRTuYXDSoKQFMU2lioQ8K8xEcHOHevB9Fg5bSm-B9mmAtVBZSftAr_E56QiY4uCyI3de4pA3yYtqdfQj4HaclTkRkT1UQo-kR8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع امنیتی عراق به خبرگزاری فرانسه گفتند نیروهای امنیتی این کشور سکوهای پرتاب پهپاد را منطقه دورافتاده الطیب در استان میسان در جنوب عراق و در نزدیکی مرز با ایران کشف کرده‌اند.
همزمان خبرگزاری رویترز به نقل از دو منبع نظامی در عراق اعلام کرد این منطقه مرزی پس از کشف سکوهای پرتاب پهپاد بسته شده است.
کشف این سکوها پس از حمله به خط لوله نفت عربستان سعودی انجام شده است؛ حمله‌ای که ریاض و بغداد گفته‌اند از خاک عراق انجام شده است. بغداد روز شنبه گذرگاه‌های مرزی شلمچه و چذابه را نیز بسته بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78348" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78347">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZvvmjbZcFmq1_tyOOzb-kp3NuiraRmT_V7OQx7KjOHFmToN2O0XcgoeWQm5nsQYkYyiVtBGSpplK_HAtZWPxlvsHAV0TSpn74eXk8aJSnOw8CLurC4VPB-7qczJFULR0gEfVYpMdYPjEOHV4ON_-N-AUcCqNJx5rqIx0oTinuzK7GIot4If1aZEnN5UyDOld3iYWhMv2mMI5tjMvp2u-H_2zo8yOxnb_2QWDz9HhP2pSxqFaG7keruxN15MqSKYYAuyuBTgIMQYwfvohXszNQ2jyd0oD_bmnKgNlqYwJY1Vmtp-ni48UKZb6gwnQdBAq6kjjadCxN909aK-EJ49LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، به نقل از یک منبع آگاه گزارش داد تفاهم نهایی جمهوری اسلامی و عمان درباره مسیرهای جدید کشتیرانی، به معنای بازگشایی تنگه هرمز نیست و باز شدن این تنگه به اجرای هفت شرط تهران از سوی آمریکا بستگی دارد.
این منبع گفت تهران و مسقط پس از گفت‌وگوهای فنی و دیپلماتیک، در اوایل شهریور درباره جزییات مسیرهای جدید ورود به خلیج فارس و خروج از آن به توافق نهایی رسیدند و قرار است این تفاهم به‌زودی با حضور وزیران خارجه کشورهای منطقه اعلام شود.
بر اساس این گزارش، تفاهم تنها میان جمهوری اسلامی و عمان است و کشورهای دیگر، از جمله عراق و کشورهای ساحلی خلیج فارس، برای اطلاع از جزییات مسیرها و ترتیبات تردد در نشست حضور خواهند داشت.
مهر نوشت مسیر ورود به خلیج فارس به‌طور کامل و بخشی از مسیر خروج از آن در آب‌های سرزمینی ایران قرار خواهد داشت و تردد در این مسیرها بر اساس ترتیبات تعیین‌شده از سوی جمهوری اسلامی انجام خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/78347" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78346">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0c0eda53bf.mp4?token=LufavVIyAacY2vXHtFH19cMP2Fm2h7OSxYLgDtveaqUObKN_CddCMU5PQ11Y4pXrdxihlH56Ql-Fh7uKkVm8VPdJZjg902BZySpLPjw2IgSSWFtw67ZQYKPNgnHkruOr3eXotlXabGnoOdLCnjs0FZRzXFhw86BKegHpOvMfR1QtTwJYiaTH7gIBqHgy17Qll1icBHZ9DZAPM5WB5__L5yfKFZ7JO-Lir-VKi6E5MQ1I8a4-RyhLkmSLmAWcbXUKiGTiNVCqrtMbgCtXHHBEs9dLaCw0nwtlPvR75XXP9zV8rOUozGnPgOGiOUKuBwhGKjpFNiftgdkndbIflyGYIg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0c0eda53bf.mp4?token=LufavVIyAacY2vXHtFH19cMP2Fm2h7OSxYLgDtveaqUObKN_CddCMU5PQ11Y4pXrdxihlH56Ql-Fh7uKkVm8VPdJZjg902BZySpLPjw2IgSSWFtw67ZQYKPNgnHkruOr3eXotlXabGnoOdLCnjs0FZRzXFhw86BKegHpOvMfR1QtTwJYiaTH7gIBqHgy17Qll1icBHZ9DZAPM5WB5__L5yfKFZ7JO-Lir-VKi6E5MQ1I8a4-RyhLkmSLmAWcbXUKiGTiNVCqrtMbgCtXHHBEs9dLaCw0nwtlPvR75XXP9zV8rOUozGnPgOGiOUKuBwhGKjpFNiftgdkndbIflyGYIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت امور خارجه، روز شنبه ۲۱ شهریور ماه گفت اطلاعات تهران نشان می‌دهد حمله موشکی آمریکا به لامرد از خاک یکی از کشورهای حاشیه جنوبی خلیج فارس نیز انجام شده است.
اسماعیل بقایی در گفتگو با رسانه‌های دولتی ایران گفت این موضوع نشان می‌دهد آمریکا «برخلاف همه قواعد و اصول حقوق بین‌الملل» از خاک و حاکمیت ملی کشورهای دیگر برای حمله به ایران استفاده کرده است.
او تاکید کرد ایرانیان این موضوع را پیگیری خواهند کرد.
بقایی همچنین گفت برخی کشورهای همسایه، برخلاف «اصل حسن همجواری»، اجازه داده‌اند از قلمرو آنها برای حمله به ایران و «ارتکاب جنایت جنگی علیه مردم» استفاده شود.
در نهم اسفند ۱۴۰۴، یک سالن ورزشی در لامرد فارس، مورد حمله دو موشک قرار گرفت که منجر به کشته شدن حداقل ۲۱ نفر، از جمله ۴ کودک، و زخمی شدن ۱۰۰ نفر شد. این حمله اندکی پس از حمله هوایی به مدرسه شجره طیبه میناب رخ داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/78346" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78345">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0EMnT-_hSXmtxuJDM3n40C-obh9Re5PXvBYJYTgUHtnG-N4VZ8XhNASAEKuYVIOmJHEx3DH2BdaDqRFPro8V_jdOWDvAvOUxUrsKpyAC_P7Yy49NA3ceFPXwup69w692TafvQxT4t-6sklh66pt3_p8hCRlXq_jVS08zDWmIhzly_6kroUfrlcNtuGI8fetcpV9T7Pqk3m3dRCUkxPo1PoFlCdvx2VTaOxe6u5iFL4mKVMzOh50oBA37dNgsAHw9T6V72tlwGbFevI9N-LgFeUGkmcXWOO3s5NhI0QX-I5ifTgN_C77ADGZt8ytWl0JzCZtGMPSm4ELlcv9gftx2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت احتمالاً جمهوری اسلامی مسئول حمله هوایی به عربستان سعودی بوده که به تعطیلی خط لوله شرق به غرب انجامید.
او روز شنبه در دوبلین و در پاسخ به پرسش خبرنگاران درباره مسئولیت ایران گفت: «فکر می‌کنم مسئول‌اند، احتمالاً خودشان‌اند.»
ترامپ افزود با محمد بن سلمان، ولیعهد عربستان، گفت‌وگو کرده و او را «دوست خوب» خواند.
رئیس‌جمهوری آمریکا همچنین گفت حوثی‌های همسو با جمهوری اسلامی با دولت او تماس گرفته‌اند و اعلام کرده‌اند نمی‌خواهند آمریکا مستقیماً وارد درگیری شود.
او گفت: «آنها به‌مراتب ترجیح می‌دهند ما درگیر نباشیم و بیشتر شناورها را عبور می‌دهند. فقط یک کشور هست که از آن راضی نیستند و ترتیبش را می‌دهیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78345" target="_blank">📅 15:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78344">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/243b69b1d1.mp4?token=I9FnNA6Q-bPdTQfJDBcXzQ8bFMmjisyXmms0HOMGEFjBlVVALCoeEelFjtqlxFdoxX20dxcAAd2C5bYsGPotTatW7DudT2Y5R3yzIIaggL-uBuGEv6VrLoh4BITyrdDd4C8Xd5-1383Z7-J3Yx5spY2h9RvLk3j6QcjukSvsQAB_Ui_OnQh4CoYErjbC2ElIq5TdGFa22cpP3_dUeKvYCo6w5JUjMTv5BXgSO2wVnff2Ap1pqO9GKS-sRVhOK61HdoUNzO1w8ToGKrFMZXCmhJIwy5hCZWvanEepF6lzU_VyBK2Nb7ZRgcAiKDVkBmgwngI9I95Bxur6IO5jQVrNEw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/243b69b1d1.mp4?token=I9FnNA6Q-bPdTQfJDBcXzQ8bFMmjisyXmms0HOMGEFjBlVVALCoeEelFjtqlxFdoxX20dxcAAd2C5bYsGPotTatW7DudT2Y5R3yzIIaggL-uBuGEv6VrLoh4BITyrdDd4C8Xd5-1383Z7-J3Yx5spY2h9RvLk3j6QcjukSvsQAB_Ui_OnQh4CoYErjbC2ElIq5TdGFa22cpP3_dUeKvYCo6w5JUjMTv5BXgSO2wVnff2Ap1pqO9GKS-sRVhOK61HdoUNzO1w8ToGKrFMZXCmhJIwy5hCZWvanEepF6lzU_VyBK2Nb7ZRgcAiKDVkBmgwngI9I95Bxur6IO5jQVrNEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای منتشرشده در رسانه‌های اجتماعی نشان‌دهنده ازدحام در خروجی مرز بازرگان است.
برخی گزارش‌ها دلیل اختلال در تردد از این گذرگاه مرزی را «محدودیت‌های ظرفیت پذیرش در سمت ترکیه» عنوان می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78344" target="_blank">📅 15:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78343">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yf1xbwMyD8BMVK0fke1o4iUnfWu8wEVGZJfYW1nQqnagEj9NG4HkK9ZRTBpCnGtqtiSdppk5t8KbC7qmVMFxzpSUn_ISNqPvERCpcnD8b2vhWVkixrCR3MOKnaL3bWa6SQh9dR1muccP03pYnVmOU1RynOzWyh71udJgbIKwAViPK9_UFfOdmJhfvZD2ToxwVCqIYtUlM1V5EH2KU5bP0paQxq1KVTfsgX0cJJL81HGNW0NVzaeOvI4GG-n_v2NY9yt6cSObjxTomv4k6kU-sPtVyLtHa6KxV78nZsjpdZlAHj6yTspISlMUYOl0LRpsTBMwuVDJJVz71JupHSJ70A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون استاندار خوزستان اعلام کرد مرز چذابه نیز همچون شلمچه از بامداد امروز با اعلام مقام‌های عراق تا اطلاع ثانوی بسته شد. بنابر اعلام ولی‌الله حیاتی، هیچ تردد کالا و مسافری از این مرزها انجام نمی‌شود.
ساعتی پیش رویترز بع نقل از دو منبع امنیتی نوشت عراق پس از تازه‌ترین حملات پهپادی صورت‌گرفته به عربستان سعودی، دستور بستن گذرگاه مرزی شلمچه بین عراق و ایران را به عنوان یک اقدام احتیاطی صادر کرد.
مرز چذابه در استان میسان عراق قرار دارد و دفتر نخست‌وزیری عراق بامداد شنبه فرمانده عملیاتش را برکنار کرد. این برکناری پس از آن انجام شد که تحقیقات تأیید کرد آخرین حملات پهپادی به عربستان سعودی از خاک عراق انجام شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78343" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78341">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sCilMmD7_cBBJCSa9HpIUlIfSoGRRe4J_g0-W5LimI3FpjVprFSgzxnuVBP6FL7UBNb3_bHJbWP1P5Bp14wXfXZcDmIFDU-L9hHTd2ryxNiBDbbfiwvAIdd5Q4rI6toT9QWm153v1hlX3dSpAZ5oZjLskbxPNDk1OjsTtX5wzDuuUUkDnEfte69TpQ_BVR5RA_TLm3izfdbYd2dg8bsLcpD3q3qUe64bQAj9eEExr9hWxJRyd2TIgl_gPhSkm6rdRXRcusVKjhLk34_Ph6eU--Q2svfr1cG9FBKqmDMyU4-t-zU2fuV614v7yTLJYfs5mtyXWk-MSPdBKGM3N0BiHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pLd-Dmw6pu_IMllLuGrgfVzZyuf3Cb-MPlnYJY6cjtd_ykGohPC2CYwJ1qrZ-bNf13X2I61uF5Lw_J2EYrUhLsZOe_zIHZUTUOq93YWsYzmkFOmABRq49XbmBhygOr7ZQ3Rc_EPnu-qfEblH_NGmgKw86fw8NLz5MDu1g_PWLgx9mfe0tjRAlJ5_ll-O6siplLPLFG2FrL6l6rdJt0amYuMnTcbwsR1gdFLzXFyUfNVuazP3HXwZwey5zUZdooI826bNMWXJcGk1itTi81h8Oab6rS8RYwpv-lpEBZr81AqP-0JLQC2sUqgjr-HozokOlfCzWCD3OYiCG8m3Yr-npA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درگیری میان نیروهای نظامی و امنیتی جمهوری اسلامی و افراد مسلح در منطقه «بخشان» سراوان، پس از بیش از هفت ساعت همچنان ادامه دارد. «شیوار نیوز» از حمله به نیروهای حکومتی از دو محور، شکسته‌شدن بخشی از حلقه محاصره و خروج شماری از افراد مسلح از محدوده درگیری خبر داده است.
این درگیری حدود ساعت چهار بامداد شنبه ۲۱ شهریور ۱۴۰۵ و پس از محاصره یک خانه مسکونی آغاز شد. شبکه اسناد حقوق بشر بلوچستان پیش‌تر از استقرار گسترده نیروهای نظامی و امنیتی و استفاده از سلاح‌های سبک و سنگین در این منطقه خبر داده بود.
براساس اطلاعات منتشر شده از سوی شیوار نیوز، نیروهای نظامی و امنیتی پس از آغاز درگیری، محدوده حضور افراد مسلح را محاصره و مسیرهای منتهی به محل را مسدود کردند. بااین‌حال، در ادامه افرادی از خارج محدوده محاصره، نیروهای حکومتی را از دو محور هدف قرار دادند.
@
VahidHeadline
قرارگاه قدس نیروی زمینی سپاه پاسداران اعلام کرد در جریان درگیری با افراد مسلح در شهرستان سراوان در استان سیستان و بلوچستان، سه نفر از نیروهای سپاه کشته شده‌اند.
بر اساس اطلاعیه این قرارگاه، این سه نفر با عنوان «پاسداران گمنام امام زمان» معرفی شده‌اند.
قرارگاه قدس همچنین اعلام کرد که تا پیش از ظهر روز شنبه، چهار نفر از افراد مسلح ناشناس نیز در جریان این درگیری کشته شده‌اند.
این اطلاعیه جزئیات بیشتری درباره هویت افراد مسلح، گروه یا سازمان وابسته به آنها، محل دقیق درگیری و چگونگی آغاز درگیری منتشر نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/78341" target="_blank">📅 15:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78340">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qavvoXmi7lDbh-BNz1l_vx8qtvr045FuVFuSrc0GbMajsi3yZhrRIw-lu_HnqxnRmluXk-V6NC6iTWRGFiGvLyjQkkT58HiRQwDJnKo72LCExuPuTYX689Eke47qvjNc9-u0ieWogMy8UHmZVCCITIbtpwXOGP0NwGpsoZbhRlgvQZszoQ64epydf1X1oDwWX1V0UJbjEXRctFezdq38tdqzLMUzlrLAykQGxID5HqnwFrPnJJxlOAFVqVz0fgoIxEHB0feNnW2bVpYtVxqxutV6zCMTWuMKOmD2qOfR0yfK-hc68QDZhBP400nE7FxjNtteW5tm0x2FK2kTT7sR4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سودا ابراهیمی شمس‌آبادی، بلاگر ۳۳ ساله اهل بندرعباس، که از ۹ فروردین در بازداشت به سر می‌برد، به اعدام محکوم شده است.
بر اساس این اطلاعات، شعبه سوم دادگاه انقلاب بندرعباس به ریاست قاضی خواجه‌حسنی، سودا ابراهیمی شمس‌آبادی را با اتهام‌هایی از جمله «توهین به رهبری»، «فعالیت رسانه‌ای و تبلیغی برخلاف امنیت ملی»، «اقدام اطلاعاتی و امنیتی به نفع دولت‌های متخاصم» و «عکسبرداری و ارسال تصاویر برای رسانه‌های فارسی‌زبان خارج از کشور» به اعدام محکوم کرده است.
دادگاه همچنین او را به دو تا پنج سال حبس، محرومیت از برخی خدمات دولتی و مصادره اموال محکوم کرده است.
حکم اعدام سودا ابراهیمی شمس‌آبادی روز اول شهریور به وکیل او ابلاغ شده است.
بر اساس اطلاعات رسیده، ابراهیمی شمس‌آبادی در جریان دوران بازداشت، به مدت ۲۰ روز در سلول انفرادی نگهداری شده و در دوران بازجویی تحت فشار شدید قرار داشته است. خانواده او در این مدت از محل نگهداری و وضعیتش اطلاعی نداشتند.
قاضی خواجه‌حسنی که این حکم را صادر کرده پیشتر در سال ۱۴۰۲ از سوی مقام‌های قوه قضاییه در زمینه‌هایی از جمله صدور بیشترین احکام و جدیت در انجام کار مورد تقدیر به عنوان قاضی نمونه قرار گرفته بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/78340" target="_blank">📅 15:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78337">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AoMy192i0Q_KYGZ2EeCcgFNoHCjZCFVzZbaTkDtB6IUBVY-KYpq6vNCLUWtWQmQ57maIq69TFVxEvQsTVDzCyBfcVDtqSZe2UyzXKWL-yciiLCy3RMGhmFqnIWsx6qMOzq3_5saO2muJ2C2Uy73z0N4C-WHeVXIP3pDRr_TByzXdszcLN7DDUTAeObNAsymo-hcbByukIBv-kB6TEM4ResyTdGYfezOpW3erU1BcVJR1AK5KEMmZ6g9o8knqv6D9aocXPSLvViPzQaV0rAfs4PFnwR_3-XsuuvprR1tHEocdDZXQKsKfKevapexldN2GQs9zi2YtQAxZeo0zAJpVxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d70-WMKwH9gqRTF4LvKw6uYT_q2-QJh1GDVZ-a-Sn7VuDf8VpZ-2Ja-IWDW1iZyfk8dpGnX_nGvl5KEaWG_lZxG6eaYRXeD8PEYiNg47XYnCkw0uR4FAaGND-gmbeKxXizHN7aBLzO4MYhp0muKxxGN8iSv1eggDrjJ4H9CqnTZcRv_aBKsG2eJwL779BLditMRhh6FpEXHyKUoUqA8V3JQV5_YUcG4AROQd3cIShxJ7W63gP0eG-a7vuihyYmu4BAvG8elq-UwGo470LMGqyCJdyCQm4kkWBOY8fkX4h_YhD8c6SmAAO-a6bN9R-zYex5cWnub1aZETC7aDpkxP6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E5inxQ7iTs7GglVKuIIwT8TDaCO4dpmQu7pZmwsFcJpA34JFE-cuA27QlSiWpplSQIgDC8lEvtNS3Vco5pUcEYxdbOmcXLBZpRsIlNCfbGlDp2LN-IYdqaX9OB1KkExO-uj28MRQraJsw-w0jBEbmW4mLCuF78N0EEUOGuROeaATHTBEFSYE6tq6TaXXCxzAGcqz0GuuOft2db1Fz2z5nD4vXZUP9zoruiS49vMp199AQmpGOVJibauYmw3kC26k2kg0k7hNJ5iD5RoiqjJOtiDUwverkYWUEqfp2Fhb8ji_o5F8whUl9nebXyKQR4XGvrs__hYpn5XeCsR_yuAPeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت انرژی عربستان سعودی روز جمعه ۲۰ شهریور با انتشار بیانیه‌ای اعلام کرد که خط لوله انتقال نفت «شرق-غرب» (واقع در مناطق ریاض و مدینه) صبح پنجشنبه هدف چندین حمله قرار گرفته است.
در این بیانیه آمده است که به دنبال این حملات، عملیات انتقال نفت در خط لوله مذکور به صورت احتیاطی متوقف شد.
این رویداد همچنین منجر به مصدومیت تعدادی از افراد شد که خدمات درمانی و مراقبت‌های پزشکی لازم به آن‌ها ارائه گردید.
@
VahidOOnLine
وزارت خارجه عربستان سعودی اعلام کرد خط لوله نفتی شرق به غرب این کشور با پهپادهایی که از عراق پرتاب شده بودند، هدف حمله قرار گرفت.
وزارت خارجه عربستان سعودی افزود بنا به درخواست نخست‌وزیر عراق، در این مرحله تصمیم گرفته است اقدام تلافی‌جویانه انجام ندهد.
@
VahidOOnLine
خبرگزاری رویترز گزارش کرده که بغداد دستور تعطیلی گذرگاه مرزی شلمچه میان عراق و ایران را صادر کرده است.
دو منبع امنیتی عراقی به این خبرگزاری اعلام کردند که عراق این گذرگاه را به عنوان اقدامی احتیاطی و در پی حمله پهپادی از مبدأ عراق به خط لوله نفت شرق-غرب عربستان سعودی، بسته است.
گذرگاه مرزی شلمچه یکی از مسیرهای زمینی اصلی میان ایران و عراق است.
براساس گزارش‌ها پهپاد شلیک شده به عربستان از استان میسان عراق شلیک شده است. این استان در قسمت جنوب شرقی عراق و هم مرز با ایران است که مرکز اداری آن شهر عماره است.
@
VahidHeadline
رویترز نوشت: به گفته این دو منبع، عملیاتی گسترده برای تعقیب و پیگرد عاملان این حمله به عربستان در جریان است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/78337" target="_blank">📅 05:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78336">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/78336" target="_blank">📅 22:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78335">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBLyj5UcCN6z2OJizmV-t7YM8HIgdutGkrkTI4cBZaGffLmRcokeTTc7osle-nFa9sKYNmqejVjO6-WuY7y5NFtrrlHkuDI3su8uvQh1y-iCkX6qd7nEMhpSpiMBawc7wjauZ_rVg3h1wGJN441FeSnDawV8SHdLg2cZs0Go7hjInXUBgte0Esq02xaCOrlzI8O2Aa6Xl7QcrUz6vph7UZaiaY69tJjQDn9F8_LcuWT1Xi00H0HU08l9F4rkmvSgKTBfCyJUTz46k2t-NAfb3HdONpcagu7V5vrePxYsNc8_Q7cgNc7TNrbTHvwjdOUb1hR39kxa2ebGiw2xwjxLOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس دولت چهاردهم جمهوری اسلامی که به هند سفر کرده است روز جمعه ۲۰شهریور۱۴۰۵ در پایتخت این کشور اذعان کرد که فشارهای آمریکا بر ایران به مرحله «دشوار و خطرناک» رسیده است.
او با اشاره به این که جهان امروز در یکی از «پیچیده‌ترین مقاطع خود» است، خواستار «همکاری عملیاتی» کشورهای عضو بریکس شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78335" target="_blank">📅 20:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78334">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=TY0AVA-XF86Na7wDXWZpSN-GwDbQ5xR4PSyxCZqQPgCPB68DbV6DP_6y0_uh3Ke9SC-3cju1MbZExOTociqcBVH-eobPqywWCRiiiAypti13mVy63c90p0HpXYzJ94vy87G1Lryrek2zLYCpnX_asuAZBmBwLtIK_LwMhiNuu-hlFbJGBIUp8HFvVu3xPWsicpu3uMSfGfPfEalRbMGKOyKe7td_yYV-c3tLhTmhEZM1iCqxMoZ3-OZ8z3O4T5WuaDG_hLGARRKW98yaKIpQW31dmcaWBnOp-jZqrbdh564qUMh0D9GNSB01ZkUQd1Rvgu03gcO_jFrkwCGKy11qsw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=TY0AVA-XF86Na7wDXWZpSN-GwDbQ5xR4PSyxCZqQPgCPB68DbV6DP_6y0_uh3Ke9SC-3cju1MbZExOTociqcBVH-eobPqywWCRiiiAypti13mVy63c90p0HpXYzJ94vy87G1Lryrek2zLYCpnX_asuAZBmBwLtIK_LwMhiNuu-hlFbJGBIUp8HFvVu3xPWsicpu3uMSfGfPfEalRbMGKOyKe7td_yYV-c3tLhTmhEZM1iCqxMoZ3-OZ8z3O4T5WuaDG_hLGARRKW98yaKIpQW31dmcaWBnOp-jZqrbdh564qUMh0D9GNSB01ZkUQd1Rvgu03gcO_jFrkwCGKy11qsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواهر امیرمحمد شاه‌کرمی با انتشار ویدیویی در صفحه اینستاگرام خود، از حضورش در مکانی خبر داد که به گفته او، برادرش آخرین لحظات حضورش در آنجا را پیش از بازداشت سپری کرده بود.
او در توضیح این ویدیو نوشت: «۱۸ شهریور، برگشتم به همان خیابانی که آخرین نگاه‌های برادرم آنجا بود؛ تا صدایش را از همان‌جا دوباره بلند کنم. این‌بار ایستادم برای صدا زدن نام امیرمحمد شاه‌کرمی.»
در این ویدیو، خواهر امیرمحمد با در دست داشتن تصویری از برادرش، نام او را در همان خیابان فریاد می‌زند.
امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، در ۱۸ دی‌ماه در شهر قدس بازداشت شد و پیکر او حدود ۶۰ روز بعد به خانواده‌اش تحویل داده شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/78334" target="_blank">📅 17:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78333">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/957af9390d.mp4?token=gUoyFBdfBFpyizw8B5rPp2zuygoKu6Jtz7j8gzEbyBVLBya--T2YF5wgZ2oyzvitOyY95fbI7-YGaiUJDG-nJi8AZZFUk_ZuFVLhfA7KXmaq5EXhlU-W-nB2-kbdVHo74PrE_8-3M5vwKSQwZxrDsEIl_I5-Oq4zYxNcXt9zGiPIUklXU2IsbcNLQaDPBE2cGxpoaWUuM8oPysA-o1_87DM-1-RAihjfrIT_lGRvRXKpb08V609eMr0N_66nntagh2ibI67nQiJc5SCIyNffdLH3PCxw0ZtktJJR6BKyHZNMiZs6794lWYRUhvYWhR0fIz4Yzor2x4NbDUzv2xbKOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/957af9390d.mp4?token=gUoyFBdfBFpyizw8B5rPp2zuygoKu6Jtz7j8gzEbyBVLBya--T2YF5wgZ2oyzvitOyY95fbI7-YGaiUJDG-nJi8AZZFUk_ZuFVLhfA7KXmaq5EXhlU-W-nB2-kbdVHo74PrE_8-3M5vwKSQwZxrDsEIl_I5-Oq4zYxNcXt9zGiPIUklXU2IsbcNLQaDPBE2cGxpoaWUuM8oPysA-o1_87DM-1-RAihjfrIT_lGRvRXKpb08V609eMr0N_66nntagh2ibI67nQiJc5SCIyNffdLH3PCxw0ZtktJJR6BKyHZNMiZs6794lWYRUhvYWhR0fIz4Yzor2x4NbDUzv2xbKOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: تسلیحات کشف‌شده در علی الطاهر را ایران برای حزب‌الله فرستاده بود
نخست‌وزیر اسرائیل روز جمعه ۲۰ شهریور اعلام کرد نیروهای اسرائیلی در جریان عملیات در ارتفاعات علی الطاهر در جنوب لبنان، مقادیر زیادی تسلیحات را از زیرساخت‌های حزب‌الله خارج کرده‌اند.
بنیامین نتانیاهو با اشاره به تسلیحات کشف‌شده گفت: «مقادیر بسیار زیادی سلاح از آنجا خارج کردیم که سال‌ها توسط ایران سازماندهی و تامین مالی شده بود.»
ارتش اسرائیل پیشتر با انتشار ویدیویی اعلام کرده بود، نیروهایش پس از به دست گرفتن کنترل عملیاتی ارتفاعات علی الطاهر، زیرساخت‌های زیرزمینی و روی زمین را منهدم کرده‌اند. به گفته ارتش اسرائیل، این شبکه بیش از دو کیلومتر امتداد داشت و شامل ده‌ها راکت، موشک و پهپاد و همچنین موشک‌های ضدتانک، مین و مواد منفجره بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78333" target="_blank">📅 17:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78332">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqXAf4OZuSKYiIcMNkfj51V5uGZqZleDmSSIykPSVV7uissuIzEal6pHmOm8X7E9eIn24zULtxcrvteRGrX46P2vDI_mwgLp41wTwpgdewcmH_ZMtfKYGB9XDnxZ90W3QsFnv3ZH7jWU6Y3x7fc8__ijlci_PTrDPwsLEB283xUiZTn5Q9YMHuVaxYElJlfs1SPylCPEmumFs3syPlQJqghOWcfrsd-Nh-i1HRJWN3r7xuakPDZXoe9Ppf3qcCQaYQx40RxJ7qgQ5Lln9P17xPhYy9uFzne5oQJzpIRSzGqAkXgQWFreQNiDIUPplpr2wzi5K4e_tsyN60Qu0Z0b5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، گزارش‌های رسانه‌ای مبنی بر آسیب‌دیدن هواپیماهای آمریکایی در جریان حملات موشکی اخیر جمهوری اسلامی به اردن را رد کرد.
او پنج‌شنبه ۱۹ شهریور در مصاحبه با شبکه نیوزنیشن، در پاسخ به سؤالی درباره این گزارش‌ها، گفت: «نه. هیچ خسارتی وارد نشده است. هیچ اتفاقی نیفتاده است.»
کمی قبل از اظهارات ترامپ، شبکه خبری فاکس به نقل از یک مقام ارشد آمریکایی نوشته بود که موشک‌های بالستیک ایرانی در جریان حمله گسترده موشکی سه‌شنبه، ۱۷ شهریور، به هواپیماهای جنگی آمریکا مستقر در اردن، آسیب زده‌اند.
فاکس‌نیوز این خبر را به گزارش جنیفر گریفین، خبرنگار ارشد خود منتشر کرده است.
شبکۀ خبری سی‌بی‌اِس برای نخستین‌بار این موضوع را منتشر کرده بود که در جریان حملات موشکی ایران به پایگاه نیروهای آمریکایی در اردن، «چندین هواپیمای نظامی ایالات متحده، آسیب دیده‌اند».
ارتش اردن روز چهارشنبه ۱۸ شهریورماه با صدور بیانیه‌ای گفته بود که ایران در طول شب قبل، ۲۰ موشک بالستیک به سمت اردن شلیک کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/78332" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78331">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R1m9rsHS2clrUmHnCYHP1OuKB1EmG34dBbTZorEGTpcp9FfEDih2r4IKII0NJaaoZgHGBSyU4HXHuVXhwN1aZsKKOB8ogaD0w7FhAPOZU-As1Lpi3GOZqyFBp6a4N5pCgsnbhOCe9G8vgFbmgh9UhvcLpoSKIy-eiE_TbLJn6WkVs28o2-yr2YoekNoXwm-4rgnvZp6_KpderleCTCPcxHaa3zLjyD1xwcPTzTDrFnjOyKd0t_XQCtFMBC_gGqoQ88HxBpztA-cP1v24ByjEXqzEdBif1wbDGXRgpcesObndYuX6yKzFxU4ZXL4qYsTPAgDZN2PxGHu_gAj3qD52bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت آمریکایی «آنتروپیک» اعلام کرده است که سه عملیات مرتبط با حکومت ایران را شناسایی و مختل کرده که در آن‌ها از مدل هوش مصنوعی «کلود» برای تولید و انتشار محتوای تبلیغاتی، طراحی سامانه‌های نظارتی و تهیه اطلاعات مرتبط با هدف‌گیری نیروهای دریایی آمریکا استفاده شده است.
این شرکت روز پنج‌شنبه ۱۹ شهریور در تازه‌ترین گزارش اطلاعات تهدید خود، مجموعه‌ای از موارد سوءاستفاده از مدل‌های هوش مصنوعی آنتروپیک را تشریح کرد. این گزارش فعالیت‌های شناسایی‌شده و مختل‌شده از دسامبر ۲۰۲۵ تا اوت ۲۰۲۶ را پوشش می‌دهد و علاوه بر ایران، مواردی مرتبط با چین، روسیه و کشورهای دیگر را نیز بررسی کرده است.
بر اساس این گزارش، آنتروپیک حساب‌هایی را شناسایی و مسدود کرده که از «کلود» برای اجرای عملیات نفوذ با هدف تاثیرگذاری بر افکار عمومی استفاده می‌کردند. سه مورد از این عملیات به عوامل همسو با حکومت جمهوری اسلامی مرتبط بوده است.
آنتروپیک می‌گوید هر یک از این عملیات از سوی فرد یا مجموعه‌ای انجام شده که یا مستقیما در یک نهاد تبلیغاتی حکومتی ایران فعالیت داشته یا به نمایندگی از چنین نهادی کار می‌کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78331" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78330">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzoeeDXbvWoOCXrwFEBkj_llvJX5Fg395Sjr1LWxpyMHzTEOWAsxqg5cPlv8Pda_CenQl9jPrPAorAjBiYqzaJfxDcfmL_Dh-kv03J54-ZxXc3m4f63o-oRWYoEFOUhPa_eoI-fu_JR1OHs4W3b3wV81vDS7nnmZ07IdzWLSqEnZBV6AvHtOZvysromgBqq4MJALSaCiGlxFg22oFH-D_yfXcnsoGafqa44UBDFf_Gj1jVKGO9Ul9qk3wtwCNhRDMqF3Q6PQznQJ5l4mBh-ltTn4Obku9969DTgusAXqMCoHLX7s7f0pEiMEq23XItDibYSgekiiHOMgkQr3mU4CCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت مخابرات ایران با انتشار اطلاعیه‌ای در سامانه کدال (سامانه اطلاعات جامع شرکت‌های پذیرفته شده فهرست شده در بورس) اعلام کرد هزینه مکالمه تلفن ثابت با تلفن‌های همراه از روز جمعه ۲۰ شهریور ۴۵ درصد افزایش می‌یابد.
به گزارش انتخاب، بر اساس این اطلاعیه، سقف هزینه مکالمه تلفن ثابت با تلفن همراه از ۶۲۵ ریال به ۹۰۶ ریال افزایش یافته است. این تغییر در پی ابلاغ دستورالعمل افزایش هزینه تماس تلفن ثابت با تلفن همراه، تماس میان تلفن‌های همراه و پیامک اعمال می‌شود.
شرکت مخابرات ایران اعلام کرد میزان دقیق تاثیر این افزایش بر درآمد شرکت هنوز مشخص نیست و آثار مالی آن در گزارش‌های دوره‌ای منتشر خواهد شد.
این شرکت در خردادماه نیز هزینه ثابت ماهانه تلفن ثابت را ۴۵ درصد افزایش داده بود. هزینه ثابت ماهانه مشترکان خانگی در تهران و کلان‌شهرها به ۴۳ هزار و ۵۰۰ تومان، در مراکز استان‌ها به ۳۲ هزار و ۶۲۵ تومان و در سایر شهرها به ۲۴ هزار و ۶۵۰ تومان رسیده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/78330" target="_blank">📅 17:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78329">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb8399ab74.mp4?token=lRPpcl2jJOU-S9k1XQt9txoUQUinLozWYI3ui6TImGZAyT2lOYabBYHGOoAYRrn4urYftIXwUvBc7RrC0T65v0gTJqC4fwFg3JpWKkO1ZjAntHdlXCWbxaquV-1UHKfaBENuW17i5GvwRrbcn7C6sLwS28MLoC5Xv7qsBUuYaVeeZwpUyFDVMuFrfDUWDqrMm6FxsfEzqUc2wzX_6Rx2sPoH55X1JbPNuzlxfW6JJXwU5gqpYhVvHE7EwA9FTn2JRSNO3vEc8tGoZWYSShAkJ8JPqr9hIE7QEwDOo4baFRwXUFX_Jjvc5P1_bY33OOcZcjfsidmX6lfk-UdbCejvmw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb8399ab74.mp4?token=lRPpcl2jJOU-S9k1XQt9txoUQUinLozWYI3ui6TImGZAyT2lOYabBYHGOoAYRrn4urYftIXwUvBc7RrC0T65v0gTJqC4fwFg3JpWKkO1ZjAntHdlXCWbxaquV-1UHKfaBENuW17i5GvwRrbcn7C6sLwS28MLoC5Xv7qsBUuYaVeeZwpUyFDVMuFrfDUWDqrMm6FxsfEzqUc2wzX_6Rx2sPoH55X1JbPNuzlxfW6JJXwU5gqpYhVvHE7EwA9FTn2JRSNO3vEc8tGoZWYSShAkJ8JPqr9hIE7QEwDOo4baFRwXUFX_Jjvc5P1_bY33OOcZcjfsidmX6lfk-UdbCejvmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی زارعی دوز دره سی، زندانی سیاسی و یکی از آسیب دیدگان اعتراضات سراسری ۱۴۰۱ که در زندان قزلحصار کرج محبوس است، توسط شعبه ۲۳ دادگاه انقلاب تهران از بابت اتهام «افساد فی‌الارض» به اعدام محکوم شده است.  بر اساس اطلاعات دریافتی هرانا، حکم اعدام آقای زارعی دوزدره‌سی…</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78329" target="_blank">📅 17:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78328">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78328" target="_blank">📅 07:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78327">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZmOcGcnuhFMX2HX07Bo01rbDx2nxBZXagqCZrE2dlwkCwxNpa6jWMAa6_LeK4xIzeURQFuMTphcIxVl_uAoCD5fm7vi-MfdOhxCzBHSDcudV4F8d6Hh427N4Pfdd0zua9tM79tPXyUDxTZes4qjDHWfPDxdpU1HRfDAZLywdkeKauaNDd3kIKvErWvxpgzeguQSYle3klc-UVUx_-f2c7iVS-ywPJ0DnT_P0Idj58ZhxQI1u47OGgufu7YJGKburB0hMJtXBf_tx-9TPBOn58Y2MgbFKrt61QqndpDyXHdNzAoDm1UWsgaI_2rbStr8Ns34YBneN7VpYSaf9XF39g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا در دومین شب گردهمایی انتخاباتی میان‌دوره‌ای جمهوری‌خواهان که در دالاس در حال برگزاری است، بار دیگر، تنگه هرمز را «تنگه ترامپ» خواند و گفت «ما تنگه ترامپ را کنترل می‌کنیم». رئیس‌جمهوری آمریکا بار دیگر تاکید کرد که هرگز نمی‌توانیم به ایران اجازه دهیم سلاح هسته ای داشته باشد و نخواهد داشت. او گفت که ایران در حال عقب‌نشینی از همه جا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78327" target="_blank">📅 07:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78326">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAqywIACMCYImDRrSL3Gyee9J3Tp_iAJTPNSgZIplK3_gFxW0Kb210XK8t3-RLbjRYPiYqs5HM8Kwz091R3Q0pmo2f5758_cgXixnuVcOQ8WDuOxKS_TbHx-II9gjLBZ14laty5mdQpElcs3l4tLvv-CsQcEPAg39XhPIIqnDDalR9g6d4iWlQX-jN7dGmYZYCDIC8yDO83GtnND8YFUUAUzUTZSvnQBVqVrtoO7nDDmxiVK8JXZASLwQRHSpJcFw4RlPMStF15PyL3Kb-dDm-ckRKXCzYdkpE8s_8SIXasEZSfOQ8JHXVBtqzXFUUqtQVC2A1B83N4HzJalyGszOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هانگ کائو، سرپرست وزارت نیروی دریایی آمریکا، به اپک تایمز گفت نیروهای جمهوری اسلامی خسارت گسترده‌ای به پایگاه پشتیبانی نیروی دریایی آمریکا در بحرین، محل استقرار ناوگان پنجم این کشور، وارد کرده‌اند.
کائو در توضیح استقرار اخیر ناو هواپیمابر یواس‌اس آبراهام لینکلن و الزامات لجستیکی عملیات طولانی‌مدت گفت خسارت واردشده به پایگاه بحرین بر امکان پشتیبانی از این ناو تاثیر گذاشته است.
او گفت: «خدمه این ناو جایی برای پهلو گرفتن نداشتند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78326" target="_blank">📅 07:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78325">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Loel6a-1jRvLf9kknU1mE8J3IPuh9BhfcLBB0vlssx9D0ttk6CgYBplWMUOkMz5UTJ7ZVpYpc1Ayif7UTnIGxCiueKsIUUs5L3PdyDBhTPp5fmCimZpREcC5G86L3H37lXoxKdiUPH2SlKAAWZ6K2cJDBY52U9CLUP1LnolQz-xvuMHbMTR3Ox4m6OvGQag1bgVtm9VzDS8FesqSz_qXg4UqsLJi8J1DAmR7EpxlOGlD4UznsGof0Uf0mkTsYiNWu6NbVzN0w1mM3hiqrxeohXMjtJqTH9FhN6WUT88DQsF3e_F9g7XBX-y0DVsnAm31mJ8zg_-IKJbe1nkzQyeUug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت پنج‌شنبه ۱۹ شهریور هم‌زمان با تشدید درگیری‌ها در منطقه و افزایش نگرانی‌ها درباره اختلال در عرضه انرژی، بیش از شش درصد جهش کرد و نفت برنت به ۱۰۷ دلار و ۶۳ سنت در هر بشکه رسید. نفت خام وست تگزاس اینترمدیت نیز از مرز ۱۰۰ دلار عبور کرد.
بر اساس داده‌های اویل‌پرایس، قیمت نفت موربان با بیش از پنج درصد افزایش به ۱۲۲ دلار و ۴۸ سنت رسید و سبد نفتی اوپک نیز با بیش از چهار درصد افزایش، ۱۱۲ دلار و ۲۵ سنت قیمت‌گذاری شد.
افزایش قیمت‌ها پس از حملات به نفتکش‌ها در خلیج فارس و دریای عمان و پیشروی حوثی‌ها در سواحل دریای سرخ رخ داد. رویترز گزارش داد تصرف بندر مخا و پیشروی حوثی‌ها به سوی جزایر حنیش، نگرانی‌ها درباره امنیت تنگه باب‌المندب و مسیر صادرات نفت عربستان سعودی را افزایش داده است.
هم‌زمان، تردد کشتی‌ها از تنگه هرمز به‌شدت کاهش یافته و داده‌های اولیه نشان می‌دهد ۱۸ شهریور تنها هفت کشتی از این آبراه عبور کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78325" target="_blank">📅 03:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78324">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/09d9c8c443.mp4?token=pqsNLDNb0lAC_iMLL-LYMId6Wcnj2BXpZPkilwTLpOGJ5yPBRfspgbE3GPFUpL26eNlwc_M_BRg71o8xLFtFSDYbtBOAFHWSi0f5y7mW8w2O8pJFA6AoqNJbQhn9Rb-uyWmIvNwJ13vP2vGyM6udMiW28dektkFQ7IO30YiAv2Tb6M9Zr7Ud0jEV_s8MSWbRPDqX33SuM42_xn_Y6AdDmVrk8HK2KKPAMXKOHaNTIvI9fG2Hb7lD9A4_9uIl8_AqAcAc72HyHu_BsP-tjxxZZjv_D-xenwPn0NCl7oyo1WdNDBB2-Io13BzsclIo_aKhHV7E3ZQ-zrMfMwCZxslFTA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/09d9c8c443.mp4?token=pqsNLDNb0lAC_iMLL-LYMId6Wcnj2BXpZPkilwTLpOGJ5yPBRfspgbE3GPFUpL26eNlwc_M_BRg71o8xLFtFSDYbtBOAFHWSi0f5y7mW8w2O8pJFA6AoqNJbQhn9Rb-uyWmIvNwJ13vP2vGyM6udMiW28dektkFQ7IO30YiAv2Tb6M9Zr7Ud0jEV_s8MSWbRPDqX33SuM42_xn_Y6AdDmVrk8HK2KKPAMXKOHaNTIvI9fG2Hb7lD9A4_9uIl8_AqAcAc72HyHu_BsP-tjxxZZjv_D-xenwPn0NCl7oyo1WdNDBB2-Io13BzsclIo_aKhHV7E3ZQ-zrMfMwCZxslFTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتشار ویدیویی در شبکه اجتماعی ایکس نوشت
:
امشب بزرگ‌ترین پایگاه ایران در خارج از ایران، یعنی تونل‌های علی‌الطاهر در لبنان را نابود کردیم. در حال تکمیل مأموریت هستیم. سال نو مبارک!
پیش‌تر ارتش اسرائیل اعلام کرد شبکه تونلی حزب‌الله در ارتفاعات علی‌الطاهر را با استفاده از بیش از هزار و ۱۰۰ تن مواد منفجره تخریب کرده است.
به گفته ارتش، در این تونل‌ها که طول آن‌ها بیش از دو کیلومتر اعلام شده، ده‌ها موشک، راکت، پهپاد، سلاح‌های سبک، موشک‌های ضدزره، صدها مین و مقادیر زیادی مواد منفجره کشف شده است.
بر اساس اعلام ارتش اسرائیل، با انهدام این سایت، عملیات تخریب شبکه‌ای متشکل از هشت تونل به طول مجموع ۵٫۴ کیلومتر در منطقه علی‌الطاهر و قلعه شقیف تکمیل شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/78324" target="_blank">📅 01:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78323">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WarTS1TwyoqiyCJrUT5vKpFgYdQcSX5bb3UZtclNGXU5mL6NxMP6a0dKIgD1Cld3sU99bMeg42T6UXY7ygDW7cRrb6bKiqXQnZLTg0dSCVVd1_MltrksWW5-I7L4T6q88kdeZuCU-H7ixRcqTrNzabumot79RAkbdsqZHXJF-QN29rjzFbruW1VzFtf4Ct3TSipFectf2zerNaaKxnbsskxUd40NxI9jUJu2iXbFRYCIA38IcqeQZ_QrrRRPU1WSLXrR4HTPEeMojSfgUTtuzCfyS88xric_IbdYHzdcPol-jiyybpPiLfyLkbKxreOieVTXU0LWUddXXjO_o3IJdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا، یوکی‌ام‌تی‌او، عصر پنج‌شنبه به وقت واشنگتن از برخورد چند «پرتابه» به دو شناور در نزدیکی سواحل عمان خبر داد.
بر اساس این گزارش، این برخوردها در فاصله چهار مایل دریایی غرب شهر خصب، در استان مسندم عمان، روی داده است.
طبق این گزارش، کاپیتان یک شناور اعلام کرد که شاهد آن بود که چهار پرتابه نامشخص به دو شناور نامشخص اصابت کردند.
در پی این اصابت‌ها، یکی از شناورها دچار آتش‌سوزی شد و از وضعیت شناور دوم اطلاعی در دست نیست.
مقامات عمانی در حال بررسی این واقعه هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78323" target="_blank">📅 01:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78322">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c378ed4e1d.mp4?token=Le8nbTWJs74NceCED6p3sxiT5s_Pi6p5L4GbPwea3WRkGyliT60ubr5JAcQdDcuWIsWwgkOBLif6wxriqygHq6JxXLioBvw6WPgyAcGACnJ9UCIevW9OqaqVCaR1Gr1XDQYnMLV5oTbldj-Wzx9WiJn1OmbCVq1-Chd1kJqlXuHIs8YkZlw-RsLdT6lgLLywgEsTTSTMgrPB0XzPH97DuL2YJ4slfiGIvOH86cib9kPyuNmkc2Bmojm4n4_tdndGPuWud_cifkW3pTQYrQ4AnDhjw__51ILHhE4ocae_h56UYOGkKOuAmSkKWgRVSSVRaxyU9PIoakzALKbebZ-Csw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c378ed4e1d.mp4?token=Le8nbTWJs74NceCED6p3sxiT5s_Pi6p5L4GbPwea3WRkGyliT60ubr5JAcQdDcuWIsWwgkOBLif6wxriqygHq6JxXLioBvw6WPgyAcGACnJ9UCIevW9OqaqVCaR1Gr1XDQYnMLV5oTbldj-Wzx9WiJn1OmbCVq1-Chd1kJqlXuHIs8YkZlw-RsLdT6lgLLywgEsTTSTMgrPB0XzPH97DuL2YJ4slfiGIvOH86cib9kPyuNmkc2Bmojm4n4_tdndGPuWud_cifkW3pTQYrQ4AnDhjw__51ILHhE4ocae_h56UYOGkKOuAmSkKWgRVSSVRaxyU9PIoakzALKbebZ-Csw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران روز پنجشنبه ۱۹ شهریورماه تصاویری منتشر کرد که به گفته این نیرو، هدف قرار دادن یک شناور بدون‌سرنشین آمریکایی در ورودی تنگه هرمز را نشان می‌دهد. سپاه اعلام کرد این شناور با شماره بدنه ۵۸۳۸ و از نوع «سیل‌درون» بوده است.
علی عظمایی، فرمانده نیروی دریایی سپاه پاسداران، گفت این شناور بدون‌سرنشین «جاسوسی» متعلق به ارتش آمریکا در تنگه هرمز مورد اصابت قرار گرفته است. او همچنین گفت: «تنگه هرمز مسدود و تحت اشراف اطلاعاتی و کنترل هوشمند ماست و هرگونه تحرک خصمانه مورد هدف قرار می‌گیرد.»
نیروی دریایی سپاه در بیانیه‌ای اعلام کرد ارتش آمریکا طی روزهای گذشته شناورهای بدون‌سرنشین خود را به تنگه هرمز اعزام کرده است. مقام‌های آمریکایی تاکنون درباره این گزارش اظهارنظری نکرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78322" target="_blank">📅 22:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78321">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IC6Tqnjp3aODrQu7UDugRAPwsfkTt4SLQvD-q-ctokQdAk7DH6s22dCRnUd_2KBOg38CsLVS1FIGb273wt1hB4qWB0rsxGrsSZJQcLRNePVOiHzNWd7D9qDCxR8G_VTIGFAvZBJBBFTWQ9elCjNmxR7MMjSmmWBffN4uwZbFuXJHAXJ2_yWtXPz0lTA2Vy-8dBSJyl1F7CAct2cky2CVgHssKMMduxUSEXk-zPpfUtmvaWapL4UDbl7v_inMv5a9RDQ1b5e-korgnHB0GvaK5m5oQLq6zuf9vPqJeyphbw4K_-U2D2PflzlFBhdo6qRNx2olVH0WydcPKO7snNn1qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، روز پنجشنبه ۱۹ شهریور در گفتگو با بلومبرگ اعلام کرد این سازمان بر اساس تصاویر ماهواره‌ای، شاهد تحرکات ساخت‌وساز در سایت بسیار مستحکم «کوه کلنگ‌گزلا» (Pickaxe Mountain) در جنوب مجتمع اصلی غنی‌سازی ایران بوده است.
گروسی با اشاره به اینکه بازرسان آژانس هنوز موفق به بازرسی از داخل این تونل‌های عمیق نشده‌اند، گفت: «نشانه زنده از تحرکات در اطراف این سایت ساخت‌وساز وجود دارد، اما اطلاعات دقیقی از فعالیت‌های درون آن در دست نیست.» او یادآور شد که ایران پیش‌تر قصد خود را برای انتقال تجهیزات به زیر کوه جهت «مصون‌سازی در برابر حملات» اعلام کرده بود.
این اظهارات در پی ارجاع پرونده هسته‌ای ایران به شورای امنیت سازمان ملل مطرح می‌شود. بر اساس گزارش‌ها، آژانس از ژوئن ۲۰۲۵ و پس از حملات نظامی آمریکا و اسرائیل به تاسیسات هسته‌ای ایران، امکان راستی‌آزمایی وضعیت ذخایر اورانیوم با غنای بالا را نداشته است.
دونالد ترامپ، رئیس‌جمهوری آمریکا، بار دیگر با اشاره به این سایت زیرزمینی، نسبت به هرگونه اقدام ایران هشدار داد و در یک تجمع انتخاباتی گفت: «ما متوجه فعالیت‌های مختصری در کوه کلنگ شده‌ایم. به ایران توصیه می‌کنم دست از پا خطا نکند، چرا که مجبور خواهیم شد ضربه بسیار سختی به آن‌ها وارد کنیم.»
از سوی دیگر، سی‌ان‌ان روز گذشته به نقل از منابع خود گزارش داد که ایالات متحده در حال توسعه سلاحی با نفوذ بیشتر با قابلیت تخریب اهدافی در زمین‌های سخت مانند کوه کلنگ‌گزلا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78321" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78320">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aC2IkLRUd3JKv3SPjdbh2kHvWoI2r-Pil5WvaTe6eycLRtrelp49rwWrnl-p870mT2gtRbHUL0LuV8PrTL6afkuIPYSGFT3uTX2Qejtj9zqXobDZiTivmcHk2wiEucMPw1vi9JWDrfOttyiQXgksEyOTJ7XkyUd8UBC51iyivkSpTxJXcOJdbBR_zZVPMvqsbq-2Mj802Vfk7G4el4HUZwvVjoYqIr9RIlhnfr3tIDxc4ASxB6jXlazmSY4eyI-WwXCx8aY_alUf5sRbv7h8O3RsYORvGPH5OY54Lrni_QYAYOmHJnBIOc2mFD9qnFPGsvhGg9MASxSN86Xdi6GR1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه قبل ماموران امنیتی به منزل خانواده «کیاوش میرقاسمی» از کشته‌شدگان اعتراضات دی‌ماه۱۴۰۴ یورش برده و «سمانه عصاران» مادر او را بازداشت کردند.
به‌‌دنبال تشدید فشارها بر خانواده میرقاسمی حالا صفحه اینستاگرامی مادر او از دسترس خارج و کنترل آن به اجبار به دست نهادهای امنیتی افتاده است.
تمامی پست‌های پیشین این صفحه حذف شده و تنها یک پست به دستور مقامات قضایی در این صفحه قرار دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/78320" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78319">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9gnK75cMbQ65VBxMyoSioAuBGIVgItLYkOZwFuQwNaiwA9lNoAbFXoQuuBEM0ygKC4n7a78sE3XC874G98xOUXrlLzN6GUDKDW_S_yxgALcJ65WoumlrEyYetQdTlxDxM_4JL3ZDlAqHmLcck2jJkUr8fYZk2_uS3TApSxMkKRjTrnn-CjvQiF2nMHuJ3R8Dg0LVzH0nfwlNAwwFGoGQoI6ZX58ADEZ1Oeqak1Q2t1V7oVe5p6Jfflgyo0d_BXgMPCwvgqWcojxA9TQFq6FtKx8iDSj1jmq6Tm19yU0nHkF5LnODmkZ1g2TagUyjnssWvcYZtaN6KRRN0iZCwljnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس بریتانیا دو نفر را به ظن ارتکاب جرائم مرتبط با ایران و نقض قانون امنیت ملی بریتانیا بازداشت کرد.
این دو فرد در لندن پایتخت بریتانیا و در جریان تحقیقات مربوط به فعالیت‌های مرتبط با ایران بازداشت شده‌اند.
پلیس متروپولیتن لندن با صدور بیانیه‌ای تأکید کرد که این تحقیقات، با هیچ‌یک از حوادث ماه‌های اخیر که در اماکن و ساختمان‌های مربوط به یهودیان و جامعۀ ایرانیان مقیم بریتانیا رخ داده بود، ارتباطی ندارد.
هنوز جزئیات بیشتری از هویت افراد بازداشتی یا ماهیت اتهام‌های منسوب به آنها منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78319" target="_blank">📅 18:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78317">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CflkR-Lu3xeMckU63pXu3hl-PAnNbwTIUd3LqfIxEaWOQo2EkcuO675ahIwPhPFWJr3pXwhrIoRf5RCIro8T2n_BRem3YmmHku24H77p5ndQDJFdhsCShmNt93-Xg5Jd5MHGhPkQmWEgVystHyXuqupPvGySzwzvcUlX2hAxgQKdLSZOzIPOyQu8NvGB8xnhhul2vehRgdRRQgECvV8bEZfvZs58iFA183DmM16EU182TZwjz1zCsGiCqzLj96r4VJWIFvNgNPP-0U5IbEpFZUeMzeoh0O0AqWXSuRSIDDJgYge6pxb6z71Yinz9JNw_QkUVB8ftJtR5LJnBxJwZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WpmqYN-5NRQnLHa5_x0WWWO3G5pTaWuIVzPWIVUYx9pCrlzlc7gE6QxYTdG53mmxCldCrFSewWm_xzRjM6I7Vb9zH8Nb3eFOohf26jkGyf9fV-QLVJWLsXskMy2cr0zYsS9aX5jSuDT-OPusyp_T-cNQvEAmJymY4G4NEG_PjVJP06IAhAtgQgw9QturSChuAxO5P71gz9QZj4qpU32QYgC7XYHcMhXMB_TBLl7JjB_Pu9lXAuRrLxRDrhaIDUMMkSZsJv13JsdmlheB8DMhtUnWGhSpH9NoNYuKhc7XM86_91nLnYjq9lhMbV3xkM7cAgxmpQE5L8gm9XWZwv50Ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اکانتش در توییتر:
MaryamAzimih
مریم عظیمی، مهندس ایرانی اپل، که پیش‌تر از بازداشت و انتقال خود با چشم‌بند در خودروی نیروهای اطلاعاتی جمهوری اسلامی در مشهد و تصور مرگ قریب‌الوقوع نوشته بود، در مراسم جهانی رونمایی اپل، یکی از فناوری‌های جدید دوربین آیفون ۱۸ پرو و پرومکس را معرفی کرد.
عظیمی در ویدیوی از پیش ضبط‌شده اپل به‌عنوان مهندس کیفیت تصویر معرفی شد.
او در بخش مربوط به دوربین آیفون ۱۸ پرو، قابلیتی به نام «تصویر مرجع اپل» را ارائه کرد.
اپل دوربین این مدل را پیشرفته‌ترین دوربین خود تا امروز توصیف کرده است.
حضور عظیمی از دو جهت در میان ایرانیان مورد توجه قرار گرفت: نقش او در توسعه فناوری تصویربرداری در یکی از بزرگ‌ترین شرکت‌های جهان و مخالفت علنی‌اش با جمهوری اسلامی، از جمله روایت شخصی او از دوران بازداشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/78317" target="_blank">📅 17:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78315">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eHeRj02rh5vPmOzIF6evn0BFaK22TcoVDxgSTi1iRWrHjj9UUfzwWIBfDFwnh8SmdkBiuzPEnQzWsYSmjOr6oy0EBqWoL4v3iltHWF2T3cuqoCHl0m_Xh5cu6QxmBvwpwh1gW8wiuzgETfFNGY_paZFHVXYcsQ7bQhy6vPPn06wrR7w8CZLoWBYRuXHtljtfJt6Z3IkMPvmpoZSD9NTWIzDZzZv14eC6clgETC9-qsGXKM4EjB_arJQh9oO0y_4OArI_s_SrCog3FCcgxhPXXRa7jn_nnApIEQXWYkmDzvq0V3viIUVU2JjiFQF9xFDfFJABcgPTBo3t3I9nIcEulA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U4CjZ9HSJ-RkXi-ov5SNcComNF4ej1qjvIlkMjjtV3yUodAuHgGG3EsCSO9ZIcD5i07C-h9S_RSL4jqML0UJdqVVJmYOo3JutJ7vBXQEtvJJMBlkuaTCUqpHMvovqa8e01VMHVMZvrsCdJDIOcuWaonbrXMB5cMHCvuHhk0xl4yrSEjwNWEIpmQhMekrhyioYsn7CCq8GzXPHZKxW5tdJRZ3BG45oxazeJE1WfJXzgxpMJMUiEPv_aYrvOJUUFJMrj9220V2n2272OZsrKKyvay_tXFGQngA66EaeF4khpnZ9IfQqr-o1dJ9PlpJXos75GJqZDjd0qHFCvSDPcjPog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/78315" target="_blank">📅 16:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78314">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kVkg-OtGNg3Ja6aOJqYJG8sEfDRq0SCHU8x2kjyFDXX2xtTz1vIc1WjJuHeVqCQvGwk4d07qPCHUl5VcHQJs0kcUYdwFHcKcDUybsj1awpdExhSpXApnxqYKHQHHdSzhBdrZAXe8Aq6FrF2Retd6PMZzDVgrqPUZIiznjdRQfqhujJ89nJqcQeU_NCn3rPkdesOtRjSpQOcFjRKP8CyF6QgaG32l8WkRgceftsDroaqXvFfLoGIv74HWf78h8hDUq2u_XFI_NxnlRekt3dkNn3qcLwgPmsBbJBiXbQEpF5UiZJvRzkYG6z0yjE6pm4bJ0jdaLLgxQvN5jTTu8gT4Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند افزایش روزانه قیمت ارز در بازار تهران روز پنجشنبه ۱۹ شهریور (۱۰ سپتامبر) ادامه یافت و بهای دلار به ۲۳۵ هزار و ۷۰۰ تومان رسید.
dw_persian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78314" target="_blank">📅 16:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78313">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOLAkghGq4GNsYS310N21SFW52eD4rCxdEnkgNic291BX6NTdltW-X9x40fKRZwO7wcXC1yV2SNx405xTThGyyJcTCIHvQthR61l3NrqMV-tW3b8N_gApKZ6S5B9CH9LLgbh6VZPDrLYXWcMQcfXjEKcUtTfYXGx-OkIH37O_s1m8FzNOzqbDD4ftNEU0tCvlc7o-AYeeIlAlUTkQnwAh9BTx32eGbHMYhqjeaUsX1nRgjroXbTizg1oUw4XaDz01tj3N_ZAlM9rtdt-60oIgxvg8tjZm7IvBSCWJG4QYAotKhD_hB0iSB28byith3Uqv34154PS6IzHK5zsvvOInw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی افزایش تنش‌ها در خاورمیانه، قیمت نفت شاخص برنت روز پنج‌شنبه از ۱۰۲ دلار عبور کرد که نسبت به روز گذشته حدود یک درصد و نسبت به ابتدای ماه حدود ۸ درصد رشد نشان می‌دهد.
طبق برآورد اداره اطلاعات انرژی آمریکا، ماه گذشته تولید روزانه نفت ایران به خاطر اعمال مجدد محاصره دریایی آمریکا ۸۰۰ هزار بشکه نسبت به ماه ژوئیه افت کرده، اما هم‌زمان تشدید حملات جمهوری اسلامی به کشتی‌ها در تنگه هرمز و آغاز حملات حوثی‌ها در دریای سرخ و باب‌المندب به نفتکش‌های عربستان نیز باعث شده متوسط تولید روزانه نفت کشورهای عرب منطقه در ماه گذشته ۹۴۰ هزار بشکه نسبت به ماه ژوئیه کاهش یابد.
مجموع تولید نفت ایران و کشورهای عرب منطقه در ماه گذشته ۶.۷ میلیون بشکه کمتر از دوران پیش از جنگ خاورمیانه بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/78313" target="_blank">📅 16:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78312">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaF_O6hYfv3bp8_veLODCq_GKKhDuWM6CLXzDL4a-vjh3TOnrTz83IJpsZt_g5rRdhM0ZNwK2OC04G0SnW6avOTizILLICdkLZWn3NnmO2qY_eUL2YVRrDcqB28dyAGwSD4Hydmok9yMTpBfxlLkAyhoqoTNP9E6mhSyeLx4OLzfa4VDLZBxLrnsYaiJpogfhIQRIQZ2CxszrgTpe3XkMSxDeRgMyLXR24uIHjDE5JY4eCM8XAykee2TVUtDw4Iy8G1Os5HP76YF0bDHW4ElGEmmyRU7JPalNqYeKH5wtedE5NM8heYfjmfOvttJWM2BZtwIJCGPsaashAZuuf55og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع ارشد ایرانی و سه فرد مطلع می‌گوید حکومت ایران با استفاده از سازوکاری شبیه تهاتر و با دور زدن تحریم‌ها، در حال وارد کردن میلیاردها دلار کالا از جمله تجهیزات نظامی از چین است.
در این گزارش که روز پنجشنبه ۱۹ شهریور منتشر شد، منابعی که نام‌شان اعلام نشده گفته‌اند بر اساس این سازوکار تجاری مخفی، نفت ایران در ازای اعتبار برای واردات از چین در سال‌های اخیر، یک شریان حیاتی مالی برای تهران همزمان با افزایش فشارهای اقتصادی و نظامی ایالات متحده فراهم کرده است.
آن‌ها گفته‌اند که این سازوکار همچنین به چین، بزرگ‌ترین واردکنندهٔ نفت خام جهان، کمک کرده است تا به نفت تخفیف‌دار ایران دسترسی داشته باشد.
به نوشتهٔ رویترز و به نقل از منابع طرف گفت‌وگو با آن، ایران از این سازوکار برای خرید دارو، وسایل نقلیه و تجهیزات ارتباطی از چین نیز استفاده کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/78312" target="_blank">📅 16:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78311">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b2c630a3b3.mp4?token=jdMnhRXq11lEucifxj89uaAoKyjJcKYJmXATM7oN6wVPsEFefBgE6IlVZaSqQ_XMIAL3rN5NtozR2jg-p7mxt-2yizcHwJ1LHYGJ6cM-oqmjvPPvUbab8qChb_GzDyOgzwhzWVHXJA0mj2s8ykaSxggTfyNiDs2XtfO_hj6wQeRP7W7z8V-DE5QK9p_cCRa3GmqevZYwdEpCMXoxsclJLBGsj9gUEmZTmzxKBxJc5L_ZnZ0FF68qKXWvXGqXLN0iwRcwJ7JFMbrO2EyFj8jzQv-m2UsuHusoMxmqbe9XP4GcqOfaqN3h_IkVilBO7eu78vbZEZM4wnhz9ioG8jQd4g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b2c630a3b3.mp4?token=jdMnhRXq11lEucifxj89uaAoKyjJcKYJmXATM7oN6wVPsEFefBgE6IlVZaSqQ_XMIAL3rN5NtozR2jg-p7mxt-2yizcHwJ1LHYGJ6cM-oqmjvPPvUbab8qChb_GzDyOgzwhzWVHXJA0mj2s8ykaSxggTfyNiDs2XtfO_hj6wQeRP7W7z8V-DE5QK9p_cCRa3GmqevZYwdEpCMXoxsclJLBGsj9gUEmZTmzxKBxJc5L_ZnZ0FF68qKXWvXGqXLN0iwRcwJ7JFMbrO2EyFj8jzQv-m2UsuHusoMxmqbe9XP4GcqOfaqN3h_IkVilBO7eu78vbZEZM4wnhz9ioG8jQd4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تخریب «کاروانسرای روس‌ها» در سبزوار:
quotes
خانه واجد ارزش تاریخی «تومانیان» معروف به «پادگان روس‌ها» در سبزوار روز چهارشنبه در روز روشن با لودر تخریب شد و اعتراض گسترده فعالان میراث فرهنگی را به همراه داشت.
تصاویر منتشر شده در شبکه‌های اجتماعی نشان می‌دهد که یک دستگاه لودر روز چهارشنبه ۱۸ شهریور بخشی از یک بنای تاریخی معروف به «پادگان روس‌ها» در سبزوار را تخریب کرده است.
«پادگان روس‌ها» یا خانه «تومانیان» در سبزوار با وجود آنکه در فهرست آثار ملی ثبت نشده بود اما از سوی میراث فرهنگی به عنوان یک بنای واجد ارزش تاریخی اعلام شده بود.
معماری این بنا متعلق به دوره پهلوی اول بوده و در زمان اشغال ایران توسط روس‌ها، ارتش روسیه مدتی در این بنا مستقر شده و به همین دلیل به «پادگان روس‌ها» مشهور شده است.
مجتبی کاویان، مدیرکل میراث فرهنگی و مدیر پایگاه بافت تاریخی سبزوار در گفت‌وگو با صدای میراث گفت: این اثر بدون هماهنگی و بدون مجوز میراث فرهنگی تخریب شده و اعلام جرم علیه تخریب کنندگان این اثر واجد ارزش تاریخی قطعی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78311" target="_blank">📅 16:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78309">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ac8H8giI6fWgLL5ivnqELislMoEsNfrayPdxMx1vdM5E16pBUh0I4fp9bvZxMzCZrRy9nowQv0-TxNLckDLUVTVtl0Gcej0srrCSBy1vAO2mTLcsteEJ4yShCsZ4CKQ2_gMc9DRGfkWBDy7V1FEvXcI149SRhVRmcPs0s5KFr40d1kgAbogyakhKgzGXc12O5inuxyeDvjre7daDNY8NF7y34TgcMxKenrROYm5P4mozilNgHnjH0Sk9W0I9VgKF4_ypNiMdrwpi_kHz8-1yj7jaN56ruW-jGV1kmlxmL9q8bwhiuK4hn7md8wDZIPpvHZ6UEcaZyDncp7lPPQQT7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eQ2Xls9oi0gVhgNUEwtC-i6Q0-byE477qQE2jWfoFCOoi54Lj9PLQ_bXhiHpDHpwtnR5WoKNxuJOPoDnfVr_1sXbs31Lc2963MtnUsWnUAs9rnyFMjS4yeGN64td-d7jtavsPFdZ0_T21KAZ14_JtJpAHitPFYgCP5WwQEJYkA4oA6WoPTK0ExOHlCjkCPh1c33SXXZ5-lBOVugkw2xA4QR6wbAZYLR3l7cUALzttLbrmyXVTCPWPwN_82LQWLHlGNVnsqtf_8Ty7V4mEfrGqqDTCNHMkIgHgwInfwMKBIbsYvEt-ksDCpmqHls7FUlqTAzcBu4nWbTHb8GnARDykA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ از مشاهده «تحرکاتی» در کوه کلنگ‌گزلا خبر داد و به جمهوری اسلامی ایران هشدار داد: «توصیه می‌کنم ایران زرنگ‌بازی درنیاورد، زیرا مجبور خواهیم شد بسیار سخت به آن حمله کنیم.»
ترامپ در ادامه از حاضران پرسید آیا ایران باید سلاح هسته‌ای داشته باشد و پس از پاسخ منفی جمعیت گفت دولت‌های پیشین دهه‌ها تلاش کرده‌اند جمهوری اسلامی را از دستیابی به سلاح هسته‌ای منصرف کنند، اما به گفته او، مقام‌های جمهوری اسلامی ایران «زبان گفتگو را نمی‌فهمند.آن‌ها فقط یک چیز را می‌فهمند و اکنون به مقدار زیادی از همان نصیبشان می‌شود».
@
VahidOOnLine
رییس‌جمهوری آمریکا، در گردهمایی جمهوری‌خواهان در دالاس گفت جنگ با جمهوری اسلامی مدت کوتاهی پس از انتخابات میان‌دوره‌ای سوم نوامبر پایان خواهد یافت و تهران خواهان توافق با دموکرات‌ها است.
ترامپ برجام را «یکی از بدترین توافق‌ها» خواند و گفت جمهوری اسلامی در مسیر دستیابی به سلاح هسته‌ای قرار داشت.
او افزود: «اگر من برجام را لغو نکرده بودم و اگر با بمب‌افکن‌های زیبای بی-۲ آنها را هدف قرار نداده بودیم، اکنون سلاح هسته‌ای داشتند.»
ترامپ گفت در آن صورت مجبور بود با رهبر جمهوری اسلامی تماس بگیرد و بگوید: «جناب رهبر، حالتان چطور است قربان؟ کاری هست که بتوانیم برایتان انجام دهیم؟»
ترامپ در ادامه تاکید کرد: «ما نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. موضوع بسیار ساده است. نمی‌توانیم اجازه دهیم آنها سلاح هسته‌ای داشته باشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/78309" target="_blank">📅 06:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78308">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78308" target="_blank">📅 06:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78307">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78307" target="_blank">📅 06:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78306">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78306" target="_blank">📅 06:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78305">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پیام‌های دریافتی:
سلام الان ساعت ۰۰:۲۵ قشم صدای انفجار اومد
قشم صدای انفجار اومد
وحید قشم بد زدن تمام خونه لرزید
#قشم
00:24 نوزدهم شهریور
صدای انفجار و لرزش
قشم صدای شدید
شیشه ها لرزید
موج انفجار شدید همین الان قشم 00:25
وحید قشم یه صدایی اومد
شیشه ها لرزید
صدای یک انفجار بندرعباس
وحید جان انفجار شدید ساعت 12:25 قشم
سلام صدای وحشتناک باعث لرزش شیشه خونه شد
سلام قشمو بد زد کل ساختمون لرزید
همین الان نزدیک قشم صدا انفجار اومد.
خونه لرزید.
صدای انفجار به بندرعباس رسید لب ساحل نمیدونم کجا زدن
درود به آقا وحید شبت بخیر ساعت 0:25 انفجار سنگین از سمت دریا نمیدونم قشم بود یا جای دیگه ولی بندرعباس به شدت حس شد
قشم لرزید
موجش قوی بود
شدید بود خیلی
توی دریا بود انگار
سلام داداش وحید .صدای انفجار مهیب در قشم شنیدیم
خیلی مهیب بود ..
۰۰:۲۶ بندرعباس انفجار رخ داد
فقط صدا نبود
در و پنجرها هم تکون خوردن
صداش انقدر جدید بود ما داریم میگردیم میگیم لابد اسانسور ساختمونمون ول شده
🤦‍♀️
صدای انفجار در خونه لرزيد قشم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/78305" target="_blank">📅 00:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78304">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/692967643d.mp4?token=WTHDGLCEg8qAYRy4dDPaObawGyJ9C8M6KaPLyjx2AQZZzFKP9rLKKzas2aBzfablvpj90mgwX5qve5bMhN8KuU1i038Z3TH0jjUvCqE7EgWu2omW1_fJPE87KXe6AyU9JML5c5sWdVgye5HH-4LN15q3GWrmqgcDHxMpDr4JzoxS8ZvDn_rmpdDfCRiYo_YRWdDZ34KzeE8bs6ZWkzN56SZaQ6R2_3wpMCCmMSwm70dA1U5E-66WJAWnq0VrTcZKKNaNksw75_N0D74M_bHrxNTeZEhKznnjCL0W9mig1LQjcpodKKNYbAVt3l1vZOCVqWLmjk1V8WkDhGfyny5e6g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/692967643d.mp4?token=WTHDGLCEg8qAYRy4dDPaObawGyJ9C8M6KaPLyjx2AQZZzFKP9rLKKzas2aBzfablvpj90mgwX5qve5bMhN8KuU1i038Z3TH0jjUvCqE7EgWu2omW1_fJPE87KXe6AyU9JML5c5sWdVgye5HH-4LN15q3GWrmqgcDHxMpDr4JzoxS8ZvDn_rmpdDfCRiYo_YRWdDZ34KzeE8bs6ZWkzN56SZaQ6R2_3wpMCCmMSwm70dA1U5E-66WJAWnq0VrTcZKKNaNksw75_N0D74M_bHrxNTeZEhKznnjCL0W9mig1LQjcpodKKNYbAVt3l1vZOCVqWLmjk1V8WkDhGfyny5e6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز چهارشنبه ۱۸ شهریور گفت که از دید او جنگ با ایران «بلافاصله» بعد از انتخابات میان‌دوره‌ای آمریکا پایان خواهد یافت.
دونالد ترامپ پیش از عزیمت به سمت شهر دالاس برای شرکت در اجلاس حزب جمهوری‌خواه به خبرنگاران گفت: «فکر می‌کنم جنگ بلافاصله بعد از انتخابات تمام خواهد شد. چون آن‌ها (ایران) دیگر نمی‌توانند دوام بیاورند».
ترامپ درباره وضعیت ایران افزود: «آن‌ها مستأصل هستند و تلاش می‌کنند بر انتخابات تأثیر بگذارند».
ترامپ در پاسخ به پرسشی درباره حملات گسترده طرفین در اطراف تنگهٔ هرمز گفت: «حملات توسط ما انجام شد. ما ۹ نفتکش آن‌ها را زدیم. قرار است حملات بیشتری انجام شود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/78304" target="_blank">📅 23:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78303">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/739c863db9.mp4?token=HIC3deqIumcgElwjnuA8gBwy4cycFDJk9fAUrTUUmPJikAGr6fgRitrhfjdKX2m4sZKqFDINp5yjOsH6wVNbi6WxzgQdHnVfFepegQsVZ3rIG4gW3QE4qn9H3NgZh75pzAdR_CkPa3azTuu1mEvfnp7ib5O_18w6YNwckKr0B036zSkxk4pPrkiFIrRyQViT00tvzdtg83Ba_42TRvEpZHCisBpsvBBy7f85TKfUXF4d_0lS97_L6i4SHFkJImS6MQPA4R8qr17v5uaUqB8OZUHlvYBzYJ3eonAOT5sxAm_wDw41kyKsUifN7HyNRFdLLWg9QAzg3C5Qz8JDLcuN5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/739c863db9.mp4?token=HIC3deqIumcgElwjnuA8gBwy4cycFDJk9fAUrTUUmPJikAGr6fgRitrhfjdKX2m4sZKqFDINp5yjOsH6wVNbi6WxzgQdHnVfFepegQsVZ3rIG4gW3QE4qn9H3NgZh75pzAdR_CkPa3azTuu1mEvfnp7ib5O_18w6YNwckKr0B036zSkxk4pPrkiFIrRyQViT00tvzdtg83Ba_42TRvEpZHCisBpsvBBy7f85TKfUXF4d_0lS97_L6i4SHFkJImS6MQPA4R8qr17v5uaUqB8OZUHlvYBzYJ3eonAOT5sxAm_wDw41kyKsUifN7HyNRFdLLWg9QAzg3C5Qz8JDLcuN5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامعلی حداد عادل می‌گوید حکومت فعلا نمی‌تواند «به علت شرایط جنگ آن‌طور که باید وارد جبهه حجاب» شود.
این عضو شورای عالی انقلاب فرهنگی و مجمع تشخیص مصلحت نظام در ادامه می‌گوید شرایط کنونی کشور از نظر حجاب «بسیار سخت‌تر از سال ۶۰ است که شروع به کار کرده بودیم».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/78303" target="_blank">📅 21:32 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

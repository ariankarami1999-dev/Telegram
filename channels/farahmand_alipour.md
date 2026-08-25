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
<img src="https://cdn4.telesco.pe/file/ts9Awj9HwA4gwCu0LhF6_e48pOiNQm7oyRYRmDe-S6R10ICIFkf05ef-TnslDPb4UTm6lCgarctch_g3OKJVhEKa6PaAg2nH7UuxBamR5Rs5iKXAeUlOjN80_nKKRNpTvg6MDPpe_u3y8euzME-LE0PKPsHKTc95dNIvFqi8vMDHXkKpk1RfKOoWiqLhQ40w-_sxVRb_oizbGDsWpzBEEZwGUvw5tnP2GE_I6dwKZjmg8H7ZCofp6qBeBMbnUlBWkYllnqctz0OWtYKXRTAzTKVtJFxrtqQCN7vb13wjveD5HY-i4OBeAk1Iq2TrXQvalWwx_ZqD-Jsv1n_oDcp1Ww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 09:25:02</div>
<hr>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
اسکات بسنت، وزیر خزانه‌داری آمریکا :
‏
🔺
امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است.
کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
‏
🔺
خطاب به رهبران جهان می‌گویم؛ امروز زمان انتخاب است، یا آمریکا و یا جمهوری اسلامی.
‏
🔺
هر کشوری که با ایران تجارت کند، خود نیز منزوی خواهد شد. هر کسی که تصمیم بگیرد با ما همکاری کند، سود خواهد برد.
‏
🔺
به عنوان مثال تمام شعب بانک «ملی» باید تعطیل شوند.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=RSjxp_QkCWfrBxfRxSZ67ZM_VnQBSd_s9dm4kj2K-oj3SQE0Y9P_Pb_aJTKJAhm3xZDzkCukKlITGBuCgzGQu6qUgLuCR9OgBe_5Pf7qQJCB5YpK1OauU1NSaFLc0ZkXQPxFu98bC6haP2H-tqzBv-72Tjks-aft_hFIB4WGjIfX6EClEFLZsost7VAFngvTgEyw1EOiUhzKcwy-ZCkp5XuVuZk-ZYruAKw7rw2ZvdiTEfw6KdjYC-kdGZFizcgetnxAKzs11saxhckAjtMA4xa_jpP6cCmWaCE1Hp5AghiGuL77IOQkP6tN6YfmEaEe2TBnwogpzSs5YG5FRpYpKKkekdBFEj9XkHDzjWJ6nUkHYvvh84TGU1QFQ9a6j1AnaELBYeMcyxLXp4OwSDCTslvQ2ALagU2xxjwOryIRT29kj_Qf3YYeLj7nwjPWfbMyyUQ6SNi_JR_5KkHmYjnvKbSiJvMqa2HbL-ygOl0mvNNawohYWGekKeFHs-5w7IBXP-kWjLpjiVRJZ_UVgAby0A5rwpGG_ETiRdv8A5rpNb6zYjIDS7iDOmQRbG1-lmH8C0FmjuqhAsfXO3LZj_2fipS43djHRl4hY44hgubCg4eo6Y4s-4thNVK3uxn2_kLxsoXWp9RLzNNR98cHGl807QjUIqGg2Of2h8mTibq8dbs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=RSjxp_QkCWfrBxfRxSZ67ZM_VnQBSd_s9dm4kj2K-oj3SQE0Y9P_Pb_aJTKJAhm3xZDzkCukKlITGBuCgzGQu6qUgLuCR9OgBe_5Pf7qQJCB5YpK1OauU1NSaFLc0ZkXQPxFu98bC6haP2H-tqzBv-72Tjks-aft_hFIB4WGjIfX6EClEFLZsost7VAFngvTgEyw1EOiUhzKcwy-ZCkp5XuVuZk-ZYruAKw7rw2ZvdiTEfw6KdjYC-kdGZFizcgetnxAKzs11saxhckAjtMA4xa_jpP6cCmWaCE1Hp5AghiGuL77IOQkP6tN6YfmEaEe2TBnwogpzSs5YG5FRpYpKKkekdBFEj9XkHDzjWJ6nUkHYvvh84TGU1QFQ9a6j1AnaELBYeMcyxLXp4OwSDCTslvQ2ALagU2xxjwOryIRT29kj_Qf3YYeLj7nwjPWfbMyyUQ6SNi_JR_5KkHmYjnvKbSiJvMqa2HbL-ygOl0mvNNawohYWGekKeFHs-5w7IBXP-kWjLpjiVRJZ_UVgAby0A5rwpGG_ETiRdv8A5rpNb6zYjIDS7iDOmQRbG1-lmH8C0FmjuqhAsfXO3LZj_2fipS43djHRl4hY44hgubCg4eo6Y4s-4thNVK3uxn2_kLxsoXWp9RLzNNR98cHGl807QjUIqGg2Of2h8mTibq8dbs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-s_hNTRpFxXoQDEZl29bVjmpgeoGizdfpHnIU6RHLmz2IKgR2tCfmGFYAd07G3jiKIxVEtp3rRoFKdZLKbTpaUy7h7DgxSLsv9ck7X6y1jo0VgMAJQdD12DIlcQ1h4OUckJnsKEIFpBUIa2VE977DbokMUTl-8S2HfnDsKdoO49C4V0sKdNJqVdB4uMUHOgdbH8Xo91S5dwzRm963T-79eyeQLzT9L1suunMTujIQOXoSUEsSOH19fPYCXLxMzvHHYu2Ci_fXbYiEjvExA9sSPYhdSI5QORstWQKIyWwgPinHH2dtcTroQZXeVgGCz-8-KDY4cYBnrS5wSx1VpnQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=buTYCjKvH5q8ubsoFkyczlXNKGqZWPoOEY63HQnVj4okQ0OpIzAglVAlEL2PZctoPvymVNDeDrBVVEonkkRYjEtlS_qy9WA2pvSq3DxGYsEil0cPaFEouzDs9KpV06GJp_8vnnrF120-fV0feq-YFefwJBXJgA9dqz1LZXLcXWLWB4JR_pGyg_lZk9_idVB_qlqTcjzv00aE8mEjpRxzgSlRBzQq_SXqFs4GpjjN6bJnPSIVlTUsev9RE2Ppq82KG6xJaX-Kzy1VjDMRXItLjCGv7XeQajVlcEbSoFJY0HB8YNMRYbPmbyIVLb28pwOuFbasKMIrWzWV-lXeoEV_WzKBR1iexkIeZENmt1cfbc4rqfHpPl4VbIVEyhfmZh9MP0vFvpA1HKCVzJlJed7BmV6idt6qWOW10Rgiq7HITw_IibpVbNN9RuTshx9MmSJ1ZnLLXJJ8Yq_8UC6UFjO-6J-Vr3w6Kb90QRH2Alvv5bxiuqCZ-SV2jHbvrUQ0XocNbvjRZFabf7pnkpqVQB2ZgzMEjV17HTuwotPh6jDup87Caa9beq1-lulV330IzJkYM8CaIQrZQ9DP4hCW_VArJ1PcD1z-ugit42z3oSrYKrhkfDd__YeD1nvqPOazPjdJQqLS8vG0Gs-FFDpGgFfo8_XgytxPZGYxE0YiEG6SFvo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=buTYCjKvH5q8ubsoFkyczlXNKGqZWPoOEY63HQnVj4okQ0OpIzAglVAlEL2PZctoPvymVNDeDrBVVEonkkRYjEtlS_qy9WA2pvSq3DxGYsEil0cPaFEouzDs9KpV06GJp_8vnnrF120-fV0feq-YFefwJBXJgA9dqz1LZXLcXWLWB4JR_pGyg_lZk9_idVB_qlqTcjzv00aE8mEjpRxzgSlRBzQq_SXqFs4GpjjN6bJnPSIVlTUsev9RE2Ppq82KG6xJaX-Kzy1VjDMRXItLjCGv7XeQajVlcEbSoFJY0HB8YNMRYbPmbyIVLb28pwOuFbasKMIrWzWV-lXeoEV_WzKBR1iexkIeZENmt1cfbc4rqfHpPl4VbIVEyhfmZh9MP0vFvpA1HKCVzJlJed7BmV6idt6qWOW10Rgiq7HITw_IibpVbNN9RuTshx9MmSJ1ZnLLXJJ8Yq_8UC6UFjO-6J-Vr3w6Kb90QRH2Alvv5bxiuqCZ-SV2jHbvrUQ0XocNbvjRZFabf7pnkpqVQB2ZgzMEjV17HTuwotPh6jDup87Caa9beq1-lulV330IzJkYM8CaIQrZQ9DP4hCW_VArJ1PcD1z-ugit42z3oSrYKrhkfDd__YeD1nvqPOazPjdJQqLS8vG0Gs-FFDpGgFfo8_XgytxPZGYxE0YiEG6SFvo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxSWozM_lvuMkJckYPu8r77r709n2aU8cI5Yh8Uar8vpqpL2A7msYErCE38MjNI1SxxzPOU2v3vmpQqzq2Qa7M0f8IF96H4WU_555oxQ2YinVo_mFdlT15BlNfqwWpvW4Gv7oa9FcxRP5xv16VoSlNVClgwujQ-W-S9l0g0B4OfpPgfRTlCws2Gzmg-h2nu3wXxgui6ErG2G-WCTSOSquKpIuoBB26XLW5V4Lm70LQclP4HqCf4ErLAXydZ9kqlpkkl2ARMF6iaNly2lFV8_6PD-Zu09ja3hsC-7V3FuMmrGcofTA_1_GjFqjty_vLY_fSa8FnqHVutt7P4ALVXI8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLlcmSIf2qMfRgBGYy2Y9PAJV1ezIFJNctO0KlFL79F_vJc4x4h5j5wss9RyQG2PBum4RBUvd6WdPE_9X9rx2DHFqXGmMlyFRtu94cu6_1A60Z3FafB53gZEao82KsXS1VzAVpG1tNUvaqmKTjJZ7RYqSrgwxDL4tJu3jLb3K4lc9L0Bf3IISGzyFY-lq7at90wFcZ5sZW_jOhxJS1llJUKgBeRarWCjugh19x071c-GjlEDPliTyMQmOB10KKKJKc4WZaJ59bPxtSO8_Pnd1BbotCR_ttX88qxpqmp6jeooqQQHBoPqcbg6Oipm_6RNfENrMkFmKDI54J9UXeZvUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5rJ6k7w087meD8CB_MkqP4L2j4XMn_8f1UCE1WGh8hm-QmqoXIpc0WOE9RR9i-y5vb42xzsKcak4VAHppy9nMwkNi7c4VFchxhb0UkTrs-NlToWK4nZ133Oxq_xKyv6YOXmHwMqOUFMND4t4KEHj99TSQ6GiH1L_R-CL1oGJSP4ChoKRTJxm2632BeCB_tUv1_t5Ymtus52ulVZwL-8dP-cT0tvPGAAIiAZbMgTBLIms6RtVK7Gtcd8cozdkKDKYvlNz5-WJ6_SxsmPCZ1F-LHX7S__uGjGDErFQHWxYLNbvlPBA6Q3WZfVCoW0o3b0pTH0nA8-eN1Y_85D1kbYvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQYEyJpvkhVQGCK4KkWmcHJ0Sin3XkvJCl_rH3L3JfVrAE_T1GowMMuPMvtkjg41ryptTOhCAy-Nmuq5vXFTBb8Hr5DtItQfXWmbX7_ncYV_Gjr4jVe3_Ao8AadGB-oFhRs2VIdPk596sNejkXlORvXhU3u6CAEYev20mCuItuYqztHGeo4DdSLr1RVd4UMDEglSmj1IA41niND_N-fD0ZvRCyeDtFu4i9J5nkGunM6gxqk-Ih5KEvGmiH-0sxtVVzAfeADv-qy1lRrcgBtJKp1uYz8hn1PhbQzxEssZxtgCkCKthr_DeluY-qgPOoOxhUMze1QQPThIa-V0d-zNCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsvyqUDZAVSpzZ10XA3LQWQPB3LfQgwI1DL2kAyA2M7imANT_RSXDVcQJpHMyuzL5c5ddlmgZUHr0lwXgm5YLUS9-LbBzT4F6VKX59VdLmtxyUueO3M_K1mjncbR35xkGrzLw0qhjpv1BOEKIbPhAn-Vl2LRwDpxkkB1XRDPXUhYMT8vixWB4tZU68sO5o0PeZQX5S2JG-S8dN9abnL4LZ_WZ6M6Bj9I0KHaHm-BzsFXuGQ3dY6XkZhi1emP6-ML9OyIkM_uACXKJVi8DbXjfuHo9JlSU9imX-6xwWrQLLXHFPoK1UPSyWmxJvwbnGZYp1DKaF_5PNfxkdnlSXoCLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkA2qH4heAOaCTAzJyEqZfwkEnTUkmggaa3ZAPU1iIZUykVOiXFGkT9KcXK8Vmk18QHdjsqDcxgM9vJp4J3NAxwCvGguLAnq5hlRfS-Xtji3S1_PQK9U_SI405JpcR3-TqEqUNUAJ5v3TVrOQLG0LX8opRhN4db5AydBQP0rOb1Og4PdYn-pAst1Rm3qM8gVvTbBDAXpW7wTenmzkT9do3i5UjiwpNUuNVtensDTIokrFS7rKiJZr-tnHZy96xPnlEQ2jh0PjN87b-qild5re1BOc7dhbK-Y6xxjdKajIp4bHKOHpGdlTThZswm94ll7WsVv8MLsOFOgjSnkQiasjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHadWMzUce1dg1Sg0M3NkcIc461OHlNzxJhvtd6tOA0PotsEElqh3W9kYRk3GRaB-hKmYhLt34aIgGUuOQVvdhhCKx1YTybRedezRBPzHhb90-Qb7ie81lqudWOr0zmKOzXzog5vNJH-C0HipiZ7LaL5iHpO347vywtDmh2Od9jqERTY0gSgYYK957VGPhAfDPjH7qBdt3flbKDdT_8RWE2CwbAk9I_MCqIKJehKOZXcE9-catXbGzx1NVS3KkqQMTIzJJIZBjidUDo5tHiBOquIqSRTDRRfxE3eNcorlQizs5pP1ilYxCYNqrQDR0iNGVRfAJAzvM_MqZilI2eHLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-im1Ify6RVrtlO2UAtY5uO_V-YnfPzxxxm2Z60KnOJR-fXC2WWfT3wRL3Wldj3Zcz3aBQ-YeTSH99tswJx8bFna6ZIAQsrVuLKgI4uFKrqE2y_cBKFkP_uv0M9gtTXyPP2ZIMzuJujOQyy-JCovX_nTmXNe7BtnO1gHm1IC6by0szUgzQKl1w2RHumPUtv0IoNdxOk71zm_88n2mAPO7osQgCRcJiWnSCX7taIyNrGUGsUSA3cqTwm3AZrc5v4nT8q5B7sTuW0IT4KVtHd_UA8HSR4SEiD7CgR9sXztC3ZJrTgklTM-IsdkmW2dFnWObDNBqHDJUYiZYmif-FvNTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rplBNNSLJI62acA7YzllK5JrEsxZPCffqDIr0rEGJ84zILk31FhkzMSHINnxy5Kkq-_C1KOMxvNKTNtk-GMkSjQ01CAuyoefTEs8m6YZp8hwtkB9U2eBc12C_SsMkHRMGfhU2QTUflbY0-5WB1lVXugCHOI-lA6Yq51gY0fMP2oL-jQeRbKUh_Fv-jCu22urSTzfzJ2TWIPSvg1vDKahFZq7QaVprfLamU8nNSEeWeG1pW2xXxm_kGi-_cgOR0loXWqwykZaICmsYrbrG-QYh8sCDOdhlq0pAa8YtD-3WSfN3J6wvrXfQHPUEJvaqDH2cYVjCwGIo1Hg332ABCmkFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKPi67lZWWzCS4U9iZp01Z4IhFc367ClRGAkUrw0DhWXuplvMbbWAufNLaC3AXKeMXagmXKjOwR89-qGYn-rExolZ_yA2A5buNt2fu3ocRmMAySV-yhWGTN6vufQCUfbQYqEEyyG3W7gggeXsreR6GBNt0A2xJXsOx1hDJGtewBkMbutwFPqyngeU3fcJBqcWd2onEgt1MpoDnsrofI_kZzHv649RP6uWCXsI4_fqqrDwZR2PnvMVqdnTvKdERm7rWUva-uP7bYYZACEUa6rZ7cdAvbolJZcrgStz3ISDHTNT6Q-ayw7zMKspCF2-xXi7coLSCH_MgkS-wu4HCeNwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAs-qVEseRyoUj5002XjhEC9aVnpKYqf249ZiftnBqxk1HP0_T0EMNwi0y5afCyIMpJT5v2w0wyZ6Cx06qa7Ff99xqBJIVYBH8OCA10OJ2aX3uU7yud-HSsWoz1vrDVBFsjnMcCmYKdvMXogIRuVlMfWg_64QKLopuSMsU3IXjenHT-wqjV_2y2lFokA1xsMrIH_upPsUXPgHJ14Eq-t-mcOC6pfMkmZwdo9U32coTNh5hoh3c89PwlL3SmHRHW2PIJgK3h8Jk04VfciC5IM_0RteCOSJVSLeB23KIWa6PIGEet37FuEHSIgyt-Osmgzy_V1j6hC3O-zdx9rkx6iqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDKpAzYGWf8DvElvQLRRhE7pjY1HWeKFMwGgLpmRvqqk2bJytA-cSF052N9uDFOsqTqlHxZDbrtEt0rgh2faleK7Qh5BgDCpJl1bVGJOOlo5xFz5bhJjEJQy7me1Bpe_ydbjDoKve-ARo-3uOER3y9yzeW_Puh79HXV8jB1vKd68rRYHGb45IZ00hvtbUUIYZW7tWtiMB7o2So3J93VMFwbsK22J-cyfZY2AwaF_Yl_Riyk3sNZ1KiKmRtZGNuqtqwvaXxM8gKjOSo6UEeh1JN5_N1uvHSenjzLJqbUnL_BrEB1mTt77o_UyOEZIVZoo9gQLu3ynYI-A1LrbFTgCwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NksrDtyV403_Q-dPAOqOJEUUt5JvR6N6lDMwJ9AbcG15q8GONYuUkOfI3kZh_DGRkuFbuidUTLqNcXEJlFblNk4p2C1JecXhq3_Pii9qK_USySJOqH-i0Y4BAEZ9tOKrCG0bO8oLIvChWZbK6IP626pk53JUHhdrSPH6ISkh1BK8K2qOhKqZwXfcDjpICK1vgzqub5usyht3fSKgsdhJYJ2zEoJO--yV9sNZRDhgik4iedP6FxxGeiDsVcH10znCO078VIw-GFEhj0aFAEl7gUdDjUNHvekbfuiK1UaizZF1Fnz_6cngk8QaDESUPJH8YXxtUT8Z1ngXBIZEcLSDEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nd9HQBZJm7TBpfHPv7_Fb8FQ0Y5gyYSWE0pfzrIiUpUp90do60LwebxOvrsYIlluWqZAt50AbxJ0iiKaWJTIic4n363IlkuoF4DxdCQybhj1NDijMTRvq-HSfNlLXMSlwqtReuB5BvvcB0TCgSBXiqX1AmpE2B6likN3u0uErzNCf-XAqLuDaJS1od4tfTZfjjtbKe053v07AxAhs0pe8DwK8pKsaPrMznbHWUcmTWbVnA-UbAzUvnGHgO87K1RJdFRhEGxUMjLkbWLJMji019Denq48pxHpNyTAQT3WkYtOA1S6RXahj9V7AAfS5fo7ETmmpAurRl2LKeog0lFh1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند
«مصدق علیه دیکتاتوری شاه بود
و شاه علیه او کودتا کرد.»
ولی یه سوال! قبل از اینکه شاه حکم
عزل مصدق رو صادر کنه،
چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند
و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟
بله! یکی از آنها «حسین مکی» بود!
او نماینده ویژه مصدق در خلع ید انگلیس
در صنعت نفت ایران بود! به او «مرد پولادین» دولت مصدق می‌گفتند
به او «سردار ملی» می‌گفتند!
او دست راست مصدق بود! او مسئول اجرایی  ملی کردن صنعت نفت بود!
اما علیه مصدق شد! چرا؟؟ چه شد؟؟</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVf7QJqe39_AWF8bR6ox21cqheDqHL7Xq6v795zCb1cNSq7didpJXnI7v6W-E1_rEGcM7276VG55Hfr2HWH1pfkFuTMC9YbJja49MIP25ryhbCoQCOANgak3sCu6lJzrq99x9BUXOXb9LemSFPPIsewMIMI62Y-3QNkAovmaFkWIicCI4fEdSe4DZZZfUGGPho9Lm4xDlvxr1dULZK81U7q5iDOYqZlXUj-pD_nHlHy-KfHu8M1-x6iOR4kmW5zLrd8rSFuds7VZVxFSCE_84lPRxCOH2Zs0pqW8VEhWooew9WeLi3MX87gZDdxJD7rroJhDzYjWxsOLXMtLvG0Esw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdyB8x1oGOqae1gFiW7JPpX4cTbAWlPIrIhQnhFbcRUmQLz0yK3abGDnnAh3fxdAs5hdt-F3pg84kpMUYGDe6rNMpon96RlAHDcTV4OFmX324_cLFLIokf_yhU73n1Sx5RoyR5kEJn_Sd5gPHS1Yb-eQdGtMrWDetN5SEp9AZDDzNwqpLY_iaT_zW2oYa_54HR6VVyexUR5iHPHG4-ZPtH1Bo1ZEB-jYkTX9W3Uub5tx8m9F6CPJ9j85Wm8HTclvX0aWU6gn3Wq-XGincm-RodIQf3lcx9dXTIoKqaZslc6QI24r0PSwN6mRFkAtW1HK_VS5hSaQqXSlYYN8Rc5GkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AxxtYR81Wh0bPLjFxHZNiMPC7UzHb1IzGMSL9JQP-f_7Sqf1S4axL_pWrpetXaIMVI7OVhmthxIDhDt__ACNuV_fPX0T_9515bZwnyijOZFh1kPlL4ZQTmNJugJqRYtckHtESUBguR-9aUB5-58dqMlToUoi1MZSp7iLtdYPExOW39DrNlQj-l2b2kkiQbMILpzUaoU0SG2eqHH6dCrB2pyJENgXWP6MesxrYvhWcs4yCGVJmeeH6D3GRDeB0llym5BPEqqtGY0X-XrH537syUXvShyNe8VYlz-hxYPVM-iE61eLloegXCrHxzVVZMsIqnYEgdltmX3kZ0GaO9NRXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Atm0S4s-e8YcKZx2R0UY-1pTy6idaS1TVxGKNiRj0DgR2Qng7kke1rZ30BmTBndJPewFW817sBFV_H2u4SUzMY1pG9P5yeMQMnObqOBelM5Vb9nGvREO0X2L9Pia1dBiejT-MeAcZM0cAzeC7fRXntynHKu-UqPVrk0z1zr7U0S4sf6d1g1XSsYyQId7an98xYaxCHXpUlOaiuxshb5TqOGAB5clFqzch_HgIqsJfQ4xu3NTcRuCkjnTJLMd4IEqcpisrO0caNNHPdHJ32spXvu75GtWw8xZcPmqGzPHAVKjq7lJC1z4428qfKxNlb28FPnNK3KX3Rk9HH1eeFbeHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNNq1Rb51L58g6dvN_lHwmUt0_4wRX2rZWk10pURfL8J_-oC7L1F4-jrf09VM_5adqe_O7xx2kS3j5toC1H1iNhKxLY993uEvF4vmTuvhFIz1RHu9b6bzH2dYEENaxcTzhRn9Rsj620ygTchtAnG-Asz_X9mzf4AQDPds4aXtTQY-c-THTZYJsZFRUQva2ScmsFOGmlpglP2azKQSnsMn20ycWey8GmOBzHbR4kOiwsXP5glsiMUokEse2OjLSSiniNCJL6PSUR9cLkHDm1U7g9VplAx-4vRHbgy_74_sY95e5YFFmKjDHRgfnwTkeU58sG0QC9I-gJMo9Bo12BE4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOjIL1yycZV9IpoztBcOWUZ0r7oPqNHy36Xs6QchR9hVKonf2SBpuj-JgruePoqq3r61oDeezyurScisKVWo8UBBzEZu6S4W5tpYFxd57suS8RX-3wrXTqNxSE7J1nkVywh403F_CswJt-sI59ArguOPXx4FJ6X8u1YoLqw3dh6RbfLoyPxTcHUwUJ5JddVrsNuW8D_71C00HO4DbaXz_ZPtMmF3K-cHk0_mXbVgJldz5IZrp_upkz3vnwS8CuaDLmf94jV9pa0kxmtNwR-Ix_RCs9COuVCue1pU-5oHEbLekicm6GEKTE-rsuCjYCnWxyhy5ISHejbWYKX73Xwc-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxORJrTvaeCPQzpIwVeOZt7qwJz8cNL3YxTmf1agXWCigrtXHM5khEvBf3oToq97ojbVm1nxjnUo-eAMwoeu7HGxbiqEu7gdb70Gc2vRAFfYe68jNVykpxPJ2Uc5oX3gCj5kF_VGn99MYEWTsK44Faf4M4YVAKKrReVtm7zmSBm6Uf7q-4ttuSNfjFhOtrv32YaMhX0h3ZYe3DOnjPCWJhbrQ3A6vPVtK-t2YQBu2JTc8hXpwr4M2tMGKgKQKQu2eMeSEHP9hQ6YkTXnXnAEQE9aHnvk6nRyhleIOb5zuF44kCXRxXoD10pzPTQcLzJVtW10ePupFGwwDAGD6psL_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_d4pfbcpoeR3n3IEFcQrRQOzmq2OBHdC8DW3g-mMgztdPwDjcPsZcJWD_qWgFPxFdGMQ2fZzUBbS3KCk-ov0qJ4WJyXZny7OWFSjvGDFiGm9DFPxuc0vYHDA9hCn5pXZS26Lat-MheQ0-tf-UsY2WI9GN6qOLPwBwWjS0UTMQ1cCBn0KZiVBqpvhB0cgojKl98QpGhncoK25dByvq1VZEr6eKxL6aWogpYd47f92Qa1cPdFRXXctAwwTLwdqgNhn4A-P84HsjZXZcSJkZ9sfWK5SFmBTykA_DueT3VLtoeqnkT7gkCrCXndrAwhD5a1tGY-ffg-C862KzcSWDRWzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqlCEOw_i8vOWmf43No_j81i0sLus8c5wtJjWXh2dD9wZ32ggZ52Rr36e_qi73fkV_g3pId8YVk1sxHS9XxTWQkqfqe0KNp10Zw5n6wrNBXkwjhnwLV9GCgC7OjmiwI90J1-a7HcS8flL_Hyee9pEJ3vYX6qSkrkrgcFvVMnUnT6ejBGLANL1tZZXmbCp8cLsMbfKQIkPTuXkCWe2ctSitUsAMFL6oM7QQLF0gI56vnLDI1LWWIeyfloD7T8QVaM7Iir4Us8CLtJkg3L9fCaHG3DjMrehnopzH1DXN4fUqZhsSCaR13ISof2En4yBD4vc2TR89HUbY9WShTzQecf2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRqiGWGKn9tLeNSGRGbFN1SSqeZGcWwuLJ-B3vV_A1lRxvNZMf-sTvsxldkQDVKQb0ayr5GWTgY0uDHDQ88pISnQYI_pKzUjubwXwKrLnXjnlT8sza8CUVymArRfFOYcnCK7CZHcHv3IM2ptee4Upvd5LTaHRF1oi7GO6Gtx3hO8hQ5da2JpgSUSRw-ntqO7cDuuhToYZ9dgksob_oI2ATTfeJTiExX7dNBfwUBVMTuEwnEqdxXjbqeJWPq2O1bgJXAA6JNgnpSy4GDVL6DkXTFpIi-XJoUYbvGTdGWn1DIJQNNq6-OFR7e7r3s9V97fSJm-oMBdRHQdpYLdqqeG1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoEh2jALidIdwA0PJE9COwAN7vznjKpyTTNygHK-IpG3OSF9KmTtihew1JCuGUSJxYYjaz1KUAnVTibKhtlo2b-BACu8F0UXUVHRRDCg7dXTK277-iX_hAe6L_Mmw2OQMVqpZINbwYZCSE7mL-lZLkMQszg1pDytrFc8zr6_ckqk0wzFPjH2Y-IFIj93dozH8V6P2yaAYU6zxxXxOklyMNVwtOvpYNpkGHaBupdEZbXml1-GGXZT8_WoL9koMbG_PQItZ-7DDKyyWmgqs5qNlPVLgC1cL-xkpOppFgTfTG9EApxp1bqVnU3O-VrhW6CpvfgTdLMpLQ6uPIK1apGWWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6XeX_HGmtogMIBBM2tfNouwt_NlyfmEHlgp4XrlfFKuB33eR2ifCo4ms1Y57EvL29twRHOdFVOW2JKLbRdWGtElk-W3qPtTI6Kl3azppT-abjD13UZOH8F58nEBlcbeRz5Jc5Y5Bh4GSRNEJYbHsDLmLXlj4MwNzCZkB4DIXB7anb9LQZCDc1CA3uwEV4raWzlvVbK4LqODvyFcUli3v4TxVWjcTH5ET7X-U9Dkmflc6oYwaUJUW4cSxE18Fi8raN44RT3oh8i1_jcIRb-J5Hq7ZQl2-SrNDzk0IJWaBFuR5KFTB2HHTBs19qIoCzOM8kxGGAYHVRabCw1z0SOoBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0lB4slgrnv80iC7HjmXvjwL76UMVDhZULacF-mcgxi-FDD-K64Ip7ttebCfMaFCvkI1qP6vgalIFJ57ACh8YnU3z0A8b7h73hI-TIKb1jg8vAznKENf__kFgpXvKvRXvWkcRWur4y9fLjyKK5Q4RcSyz7XnYQ3qb-6_EUeyHCv-6uOwwmQUB9Cndp6xpPZasOfan3GiepIXNVoEwN6hXhBDTEMAtpj5YCEQX-_e3taUzzeJqAtfTI0D92n_6uno7SkPp2HvkT5CpxJEgAfmNtjKu1hU3K0Vjmq_hS52xua0NmSmGOw3BSNKE97zEFSMojM51GAgxW78YsJbZBXP-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4HY8tbra6QqTy8wjZM3v2N_J5MmHDqF4dV1OVDt314elWkVV6aj6HlPZkMazchVDPHKm4HToB5b21KdKtp0QZgFy4hOW5VMTsf0fjl1TYYdV5fuQzNjnyfcBL3527-D3iY7cS8MlhAM2-qlZICeSRRa2gNM1dbMAhUtT1VpMTo96yqs7CcGLqS34PpGS0APrj_b8epOsBMz2tVpGXP0GxJwEAE8wgeP1b079_X8ZQtRJb32dhXPxqvQEa-NBH2TkcWpxz0ym-LYbz-2FQoU_wgx_PoY9KlRsz0Mjl3CzYqLbTz8kihkGPLIGkXW1q5IOUo9b4xnT_guCSkeUCZ05Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5tzitEPzvxCTn9IAqL2HupzAWOqzAH74QiDskaJaiUjy19Xdb30zJbs6hpZOTMlk-YfNJDjRvNXAwgsR2OdN4I-VJRphSKsX9mjUUYMguaXUSH8PQZAIZcqz-ptDozkzMIi1xjHxcJdp_FKwsCtZtyxI1E7TIPv5ZnOP_kbvKYq_czs6sw3n_TZS5DDwecqJ3xlPvLNS_lWFKb3CHh-yW_AerT2ZWXdpny1rEiWgA8YJpQLvp3moLO6kyTJefKUy6mmcxaSLlSB8q4EwflFf3icoKQFljpCyNyHWNDFhTWyH7VTYb2gjsEGskVQF-Tk_DztG6JdvOaFOeukkgY5Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNojMCm3HUx26xYYIevPmP5tW3NRGMIJQqFPtl9fFnMo9EMosXLT0djTUq5x0Wb58uxzi2BnA0H-TKdJ1rWbt30FprqeB_nYoLEGGuv3GmxkREcscpFaX6mDsqt-a1wsZP5IEXOqg0ACEsbSO6_syNkUQOU1yhJqM7XyrGZR93U_f_WsvCFYPZEExSaZN3dFI8wpV0bfEk9x8WDXzxW5GdQ1v_w7-lDvAPM1P1KXFZKtOmJH1A7G6n-QwZQ_hPQVt-ZoOzRcAXe_wAyeECO5yAPYrhVvtKJbdj3YAY28S98zcqJzCmfeYgd_6fu78HJahKaAWppuuxbbCPlj89HC2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRE4qFcDX9wIsWnOauGgLzDRdVYdkiK0wPRurEHTdK1e8QFn68lWa6Fang3dRnAra0Zk5CgptvudhXbRRgmFsOGVNFaYvIQNrfZ5qtAkX81texQT_awwJgYYGpWRS1JOs6fHmNnvsOEJDVC0ZV6XR1DjZQlZ-POJpZsRvhSUbKzJrHc-PRENlxJbF2kf3hQ_yuNlXJxUWr_xb-FFPfNNwLNwMI8OiFMSQ6ZlW15U2bBls3LW522x4tYgMY1tRFi1c6sjH8BeRE4-EZTZFIC5XhBUblAY-8oGvF3aEcBW7oO083CZGZC-yDNXDIsmcLT6yqpWD0aDVoyUFjsYqTFnGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GC2c31DGb-niBqMsv00lN456nIjcOOCDSMx7yPFp7t2IZQ1MsgObN_uaSDYHYjlLnu5YfMlx0x-oXxIl0JjpW71sBrdH9Du7yYFbpScMejgo3WchaK0pI6ENZnFOYjW-aTtz_BMuLch2QERibMwtqvlOxhLZOmAMwBUx2k8CWkhSfTIeQWQBYyw8WWNhEJRTq5tICHO_Tiqp8qCDk9aVZaRPrtl0qiwUIxcnAY1-SaBZMBL-Eh0Y5M0RbXCcYWmehDMAbzg5zxWjmEt_e4_b3UxH4VbIFyog336lLmOC3rYXXEfzLXyqZ-n080sDh9PdGSdrc8izXvQDZPJuA8_WZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d29FGcSfJd4EcEj9qw58rjKlc0Kr97eh9_XOvv-mcwjRkD36czSaPRMdOfVsip1sx9g4A716i34J7bAY9D__nbW9LcGMk42qk56CrXXzFPP05pnREBhPoXhD-GW-Cx_tuv2KIzLppRAn15cu7q5f7Cibi2xYO_ucL32-yngk7Ln8ZKOf9Vn25gQZ714mMysB5KRkLGtVn75-BauKOg3mxeCpv-QjvOpW8FHLQ4v_Yldali_gf7vNg9GS8Lu4U7FYZq9OWIorEVzb664t9oyAg5-yt6QfjTrs_Gkd18IBElyjrrR-MyY3BdvB30IXuPc04nvYiV5M6_n13YaboHLCCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت.
ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى،
چه كسى میگفت؟
این حرف‌ها را مصدق میزد.
مصدق حتی اقدام رضاشاه در آسفالت
خیابان‌های تهران را به درخواست
انگلیسی‌ها می‌دانست!
او ۱۰ سال پیش از آنکه با محمدرضاشاه در بیفتد، یعنی در سال ۱۳۲۲ ، نطقی در مجلس داشت از آزادی حجاب در زمان رضاشاه و تغییر چهره شهرهای ایران و آبادی آنها انتقاد کرد  و از جمله گفت :« رفع حجاب از زنان پیر
و بی‌تدبیر چه نفعی برای ما داشت؟
اگر خیابان‌ها آسفالت نمی‌بود چه می‌شد؟  و اگر عمارت‌ها و مهمان‌خانه‌ها [هتل] ساخته نشده بود به کجا ضرر می‌رسید؟»</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSFXjeh6EnO9Sc7ix1WLBDAl60mQ_I7TU0_pXj2bZAzMHtbxW3S8qsDRe85oGpn24dKRKBncsDTW-VeDWp15ZzflUPM7IUm-R1SVmlHe54fHfnIoG8ygQwwCL-_TjPosj1yQu2TFFXaSSeoCQ69xjzg6-dsaOsBIlH_kgKrTwjkDvVRp8to6iEiuNONQ3PbYoBiCMi8TjY358VPPETX1BhYro4RsSfVpy3Dplnh31Qp5_DlKMdUyEVr2E4Ln90-A2rYmOeif_EIEBcdB69FQMiFAIHHvb4hZ12JTMcz_9M2rSbAoVKI4gKYkx_W5z4xSNVZsgLVU__Pi12nOyXI8lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز نچیروان بارزانی
رئیس اقلیم کردستان عراق رسما درخواست داده بود که بین ج‌ا و آمریکا میانجی‌گری کنه.
خوشبختانه جمهوری اسلامی
همون دیشب با پهپاد به دفتر نخست وزیر
اقلیم حمله کرد، تا یادآوری بشه چه موجوداتی
در ایران حاکم هستند!
کار خوبی کردید، قطر و پاکستان رو هم بزنید!
قطر رو ولی حتی بیشتر!
که اون شبکه الجزیره‌اش
کپی صدا و سیمای خودتونه!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=LcVXh_hc5LRvpcEV9CcXKemVvnXDr7MfX0UjAO5JMK6RuMXZsZmDDtRszgskISLZkb590T82OwE3hmHiQKeNGXSJvTGWdzyjnUziRiFxPDiyMVtGwWdcF21p5vm1WFPzmmmdGK-csVfOoPsCFUBaIux7uBOJjNpo1FUI_cArwjRZFwtPBQ4kTvm1rgmHrXe6lEytEjztoNCV47Uhe-ZhOfCjI75vGulhh52fxMQMRBalHsCwBpAzRziCj5x6LOXDfM0pMcfNhOVBeVrF-empGQs64TEEDturF1wFDsibuDAO4DVXlNMYioKziKJGDNSFDu9UxKIpPuzARSqQ_RtQSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=LcVXh_hc5LRvpcEV9CcXKemVvnXDr7MfX0UjAO5JMK6RuMXZsZmDDtRszgskISLZkb590T82OwE3hmHiQKeNGXSJvTGWdzyjnUziRiFxPDiyMVtGwWdcF21p5vm1WFPzmmmdGK-csVfOoPsCFUBaIux7uBOJjNpo1FUI_cArwjRZFwtPBQ4kTvm1rgmHrXe6lEytEjztoNCV47Uhe-ZhOfCjI75vGulhh52fxMQMRBalHsCwBpAzRziCj5x6LOXDfM0pMcfNhOVBeVrF-empGQs64TEEDturF1wFDsibuDAO4DVXlNMYioKziKJGDNSFDu9UxKIpPuzARSqQ_RtQSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنبش شعوبیه یه چیزی توی این مایه‌ها بود
اعراب فاتح، ایرانیان رو تحقیر میکردن،
زنان و دخترهاشون رو توی بازارها می‌فروختن.
می‌زدن توی سرشون و ازشون جزیه می‌گرفتن.
ولی ایرانی‌ها گفتن اصلا ما خودمون از شما مسلمون‌تریم!  و در اسلامگرایی از عربها جلوتریم!
انقلاب اسلامی در هیچ کشوری عربی رخ نداد، در ایران رخ داد!
جمهوری اسلامی توی قانونش نوشته بی‌حجابی ۷۰ ضربه شلاق داره، نه فقط نوشته که اجرا هم میکنه.
هر روز پلمب کافه‌ها و... رو داریم.
هر صبح اعدام داریم، هنوز چند ماه از یک قتل عام نگذشته. اینها اما برای موشک‌های جمهوری اسلامی قر میدن و میرقصن.
البته که مردم ایران آگاه‌ترین مردم جهان نسبت به تاریخ و هویتشون هستن! خیلی!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpXQYjvQKVmfJL80a1jqm99FKfI4MRMeEErfH1f4zSOjL1YBB5iUWqnwI35T9dm9OluX-drCPFjSvuv3hcDuNSUKvNdJLuaVXa-TSM8noE24L_k8RD3xC6qn6IXwBrq6mwwKr5w1B9_GZCWomQ-F6FIcj4jxgzhr0gk99mO93mhLLVRGfm3e0LqLDF3gHO-_w5_y4ggFblFKZQhbU_BNnlZk8r7KoFuGm2xI5GwKHRGyH1OyEzCQTuMVw2CTAUYV0VPPXq5dlCWo0f7KfwVggZwjWPBDE6PgsS7dtRFPfnpEKUB3KD5swcaPIh8V0zHomtNNThXZZlQ68_C4ioPGvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=TxPhFl89a5MqRiucm-Xxy8lXl46WCkyzy4jUExz5AnAtcWEgRObSDCkZ8DSr9Q7fgF9ExUoIEP-zcgnxsQuYXbLgfI2B9WRAig-mQM45_nXE97wJzZgW_csvoNd0_yAxRxOfT4K6MYy9wKT0RjzRe6-OD5lq5dI_QOwMHiJPPaTFm9YCXCOEyJxe_Pi0ZrhDDYR5MWRfgHobcJgdfRqETjjfQFEa5cX8frYNyihFci-fLxeQ9uJ8gVzp2wi97in2HB37vdvETAyA7EKNsRKoqhGHsX46YLeKtaduz9OUwiSSVVZMW0m6Zv1GcmuQO5yS8hZorX7REXa7hQ0-q-4zFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=TxPhFl89a5MqRiucm-Xxy8lXl46WCkyzy4jUExz5AnAtcWEgRObSDCkZ8DSr9Q7fgF9ExUoIEP-zcgnxsQuYXbLgfI2B9WRAig-mQM45_nXE97wJzZgW_csvoNd0_yAxRxOfT4K6MYy9wKT0RjzRe6-OD5lq5dI_QOwMHiJPPaTFm9YCXCOEyJxe_Pi0ZrhDDYR5MWRfgHobcJgdfRqETjjfQFEa5cX8frYNyihFci-fLxeQ9uJ8gVzp2wi97in2HB37vdvETAyA7EKNsRKoqhGHsX46YLeKtaduz9OUwiSSVVZMW0m6Zv1GcmuQO5yS8hZorX7REXa7hQ0-q-4zFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgZ651M0HLo0m5QqlECpAw4DMb4y0GsDuYICplm3oGMRI7MF49EOZv7GhK6rVvT3fgm9RMj4CJMymGyjwUzeqTabYA9O2ryhnjj-NTuFzrtedeoEoSMEIY5FC-NkkJZSLoOGWq2gnjSsuPFrprEmmrH3IOQHJv1czf0wiKOaL4vlbNIbj3dl4gMM8gt4CMIO0SRvAQDIsJ6XVgQK3nSPzQ0eNFOr0717VBLL92ZL9uNmhc2A2UWxJs746V_7RG-GX3kfjRylMSm0viuuIur3wtYi3E3k9J9mNdLtVFgYajkktdVyYiJQj5j3T3PtJvO0MDle1Nu9J-EdNPeBC1nnPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhL_dVDHwTtIE10yQOsv2GoAaxS0_7AoN8p09W8DwpBJC4BUzOIoHXGECunvqe1uH7jf4e6x-2QeUXMarLvc_ViejwaVg6TzMKfjdToAg9-U7TmWprHS9QWqdqvNxm175N5DMUUvOKcRCwN5Hzs-UKE2TMaE6W3zswBE-Phh3d8jK_tN1iYE-ymRX8QaB3GlBmNLAPxEcHHtodgqtVP5RL4u9n0GqoJmsdaY490Qyzol10ksuJFG_Xg_6mv8FfdlKmceE_hSTGXCque45IFaSmxqM_x2RznR5yn3Ob6lM0cW36jEpt2CQPX6gBQWKx8oAmySQnPRzlcnFrzT8CQEfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=ThYKjwN8FiE0n6b3vo4_NLtu-7Rnr_VvG6MaJVB32BJc-W07bzk2zafBRovk0lSeMJFR7BZrtUmnk1fqzjeR9YDsGLOa6Ry_h1sWBmRYQnARk0jjm2EIYtg_UeGd5qYd3ifwwH2m1q7cDIsqhhKVbcG8KLKCytkWAiZTTHls7jJdTni6vsi5Gq3uzQ4rcJepqaFDj4qg1BMdjRHhQMlpsVZBQM8wFWDfveCk5CtiVEoywwQwQzhA-Ewd03WLGZYX-CZcmD9fhME70twG9nCYo2aqim20iqbnN1gfqNfNizumX_kIDgfQhA204rt_dGzDiZdHiaTiYMoCQUXqKzNmaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=ThYKjwN8FiE0n6b3vo4_NLtu-7Rnr_VvG6MaJVB32BJc-W07bzk2zafBRovk0lSeMJFR7BZrtUmnk1fqzjeR9YDsGLOa6Ry_h1sWBmRYQnARk0jjm2EIYtg_UeGd5qYd3ifwwH2m1q7cDIsqhhKVbcG8KLKCytkWAiZTTHls7jJdTni6vsi5Gq3uzQ4rcJepqaFDj4qg1BMdjRHhQMlpsVZBQM8wFWDfveCk5CtiVEoywwQwQzhA-Ewd03WLGZYX-CZcmD9fhME70twG9nCYo2aqim20iqbnN1gfqNfNizumX_kIDgfQhA204rt_dGzDiZdHiaTiYMoCQUXqKzNmaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lL0uW4h1MDvUu9Hph3pk8xL3N7VMJLLjU1eBJQnrbWPUanUBL5SkpYtsr6Y9DleQeMZyqe6sNSYSIQdlqDSX_YzXL6wekGRLrj-NLZg5tCyRFJ-8p6YFtFMuX9SDV8dFjJBWSSnPG5YoY8lx_-esLi9N6auZTmHEfTv9rmDZX1Qc6mijDpltXc5ACclCfbsoa2MhCiQb6dNTyCQ5hrYBDFraX5IpNDvX8osxHBd_VaFv5IW6fpxPuwRtoUzWgQaOl9cpXKyU011Z0ozvPGOPlDJ6Ac_NjVvO7R4BYZ-UyM66UVHEuLz5uougAge3vMg7mjhJGeOxR4zkbyhz5VUf8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtMX_NKQuiyfgiIvnhSK0BbdllAwgtkeKGWmAQ-lFntMAREqmiRalRKilKWpJcvivPWbVeQKLMt_eVoneNAZQSABDemVndCmgWrzCd3eVBKH7rwtQtaHBYIb4tO7D-AX2tkCUQTw22uoceLuEYHcwavrPPbFQBqnW5Y9ZMiYYSnZNY20FULnsBMoy-pO4ApLoVroDfzXUV6PNniYvSpqPOc4_z_YVCbkzmVzFmWr6m2d5AinIcdBTSjh1kSTq1-UxlqearixZ_FhxOv50Jp72JP7bVUhS1yZurm0zPtXfNCPJf0hEurq9fx9Q997dZhz_AoWZY3bMFo14oJG5JdHeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBxlgmlXZXCyN08zZUlFda85UChipFrd9f4-6shiU1BiIqpDpJ9Fgc43c5Bvroh2kcyMRV7y2zH5wWvdZeZTdXuNOKTxjA88s_b0ppSco6HKcu7j9H4Nr_GKFA6pa72U9zJ_WlcqbXJB7pgTG4L35wk8LoAu7wZWUo5pbTH2Dn3j3SDvzMtYAikEks-s23Pmxvjs597G0ejVwY_gLVyleSRMQiv154vfsjHnzL7LdxYAiahk_ggbfsVualfhxKaO9kYLuHaxnQ8q-flq-0AKaIGJHzF1AYZ99sRHod_ADlgzYs1o8tK6OoUITQbcLRQg1ouI_NGtk9jyX26GXtvfGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=jVjO-v0Rnq8iV5kI2C6FFhq4sSwEu5CAYrUeJfIUzX8eDTRMUqWUXMgs22usXFXHRDhIpZ5BHxfxsPJfbpRBEXcSxm8PhAp0P5VRjnVPiicHwF_zLcNvBJcnSbm0TOaoANgGaQzbQ0EbmUM4yy8Jticpb5Mf4R27cmnsHm2SOqp-JfThZcUD2tDphgsBxSHEadHziw6PUgRQ-S8AyeuxLl28bfOOUJ835OnYkWzzVpZvQkIehySBI9qYSRWnS3d5acPL66ddk5HS7FhorSyf9me7qh7alvJho97v4UB3SYW3bCB8anFvCygLIaG3hA7RMbIWv0kQV37233mMJDOQaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=jVjO-v0Rnq8iV5kI2C6FFhq4sSwEu5CAYrUeJfIUzX8eDTRMUqWUXMgs22usXFXHRDhIpZ5BHxfxsPJfbpRBEXcSxm8PhAp0P5VRjnVPiicHwF_zLcNvBJcnSbm0TOaoANgGaQzbQ0EbmUM4yy8Jticpb5Mf4R27cmnsHm2SOqp-JfThZcUD2tDphgsBxSHEadHziw6PUgRQ-S8AyeuxLl28bfOOUJ835OnYkWzzVpZvQkIehySBI9qYSRWnS3d5acPL66ddk5HS7FhorSyf9me7qh7alvJho97v4UB3SYW3bCB8anFvCygLIaG3hA7RMbIWv0kQV37233mMJDOQaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=thZEeM3ZlKXmIEZVssMtO-HmNR5v9YXjU_ECZdWmO76w0PK3Xo2iM3kDDR62ILO6xa5b2_0ovm5cfFphAmQr219rdO2cQUtgiNU7Kwb7jdWQjgITQSedgriCF2ua4UMTWJRkpz-oQkYOX-zIt1_Z6zIp3d6btQJHAypLOhQCZ9lU-Myx7lZ0pQ1tFfxeNq3EE2N83aCrKCqlPqlt57dc9za86ITeGhxYBWGLFEGuBZYM04UUau7Y84C1QAb3M6-_ZxU0BF12QkTegpIgK6ZnpJ3tLuRle6wszhJba67qtV7MmSwODrjFM-Ij6aPRy8dolnPd0yHWPpWiY2Lqx7cQjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=thZEeM3ZlKXmIEZVssMtO-HmNR5v9YXjU_ECZdWmO76w0PK3Xo2iM3kDDR62ILO6xa5b2_0ovm5cfFphAmQr219rdO2cQUtgiNU7Kwb7jdWQjgITQSedgriCF2ua4UMTWJRkpz-oQkYOX-zIt1_Z6zIp3d6btQJHAypLOhQCZ9lU-Myx7lZ0pQ1tFfxeNq3EE2N83aCrKCqlPqlt57dc9za86ITeGhxYBWGLFEGuBZYM04UUau7Y84C1QAb3M6-_ZxU0BF12QkTegpIgK6ZnpJ3tLuRle6wszhJba67qtV7MmSwODrjFM-Ij6aPRy8dolnPd0yHWPpWiY2Lqx7cQjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cc7Y7GLSmr9coFYtVcvt-G3KKMruASoW_aGjblpQbtXMrK0-b3oY37hEpxIOJEiZT5hP5zrPS79YZVhOp1RjakA7CZSYa6yxssqS2lReK2DN5gyKQtXUoOeAjdC0DxPh2f6qvfEtCw5obfXuS25duziE21XKhJfUw2xvcrlgTYr8XgUM0y5J8NyGR9-3_bmE5gXQgq7yDIMCMitk690Uc-DmjSx9widuZotyfxoNItiydDNoibXgZyIAyPbxHeodoPz7Zk-QnkHw53sugChH-USdvMpBb1y5pRdrauqiuwaurAs4bvMvqYScrBs5C-vaXBxsMU7mbuttissctS0ZBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا اون روز رو نیاره!
همین ایران و غزه و جنوب لبنان
که حاکم شدید کافیه!
همین افغانستان بسه!
میخوام ۷۰۰ سال سیاه گروه تروریستی حماس نتونه حکومت اسلامی در غزه ایجاد کنه!
میخوام ۸۰۰ سال سیاه گروه تروریستی
حزب‌الله در «دکترین ضاحیه» بمونه!
و رهبر شما هم از زیر گودال و چاهِ حقارت،
«علی الاصول» بنویسه براتون!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6574" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ll06rcyQYEWhdKLLDwiY86qy7VlixYWwPhV9Ri_A1taS-VNzqqYaKVy6VqvFYQxxznWyuF1WTwBGxydqiKmfewRK6OW33A4HifD29DwziCgsUZ5-zlplKtHv1pMFY1ALYEIaZqtaRjejqILdbPadR_3VbXnXwv8mvBkU3jioZrMIkp3r-HGD2xIAqzIbhD_JCThNR-tkYeRruWYebzGTNcf-LvZwRHDsSWcaRwdDUmIN-NsMpLVTnjKecXBHo7f9S5FZpGTnxu15NGBFwTMNbiT3_XsmXwLwhlcP7Q80uU0av92WavVDImwYfrkB1PCvUbwV116lYGEhskNdv0Nb1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jh8uzRhrukAJe_YwJePGEAticTwn56K8Pr3FF1qYSroDinaUWjW_04HEEEHkdBChYVprLYVKM1VoTouhHWaXBua_5ctNOJPgTrXVf9M4t1cWnQeqNjLZ2f3RlHbJHpgw1KAR_IXJ7oPgkp2NRFVIr9y3ENmqnsfY00jiF0Nye0q1TwgudJxWY-FNVKK8gH8W_17ynnGntn4EbKlaaGHBguFL-NicepX4FeCtk9avy7orEyNRmOWh2gIlueJwFudIBlNRVzERTYl8a7Eor0qR-ZhWV-o49Ecv40LlGMjZ8LTc1gmNmHks0wBSbZ8GC3L4XQakmUYzNCXyedwxuti93g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pG1aUxAZi9_bb8CSUrr6P9Fal-YD8PLka9x3TwaRvjzU9GYasrsKJbNm_WDT5bp9XRMggnonpdMGczqpmvY9HrXhluIGFWn4KGqc0o5HvI4i6AVhfzrFmfjzt7f1UWYTSgh8iROhFrT6jipuTz_GrEq459aDfy4Dx_j6TxMOIWkcUSP4O9HrBfDnvg47Z87N2IjqQjIrea0fJsvQ209kekkSvSm5mDZnHdFxyPzgl67JtgiRZdmsuTOr3jX2l-Jthrc36xj3vnQGVlC5sz3qIJ9lnap2uTd8RgXIOAWa5vHpTM1eBmsUYYadOrA3f_KUIQ8JWTGjt9hrBelRvOvIBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6nyVzEIVF_mTdJpnmTWTAkw7wNF2rssLfxOCM58HAzFYzFRTrRfOOBc3B4C4VBoi2A-yymTJQZpoSSca-8v361KsklzLdoF6_EYdfH6oVpK3mQbrA8tnD9IbMbcdYYwmb7F105N2RRmTYimfLTLXXSTY8zqydCYFZsraCLlwqI5886_dW44Z4FD4nsD2oB2csSjfHnyhAtMV4FfGylt3tz-uMveqVdvevdaukkOu7O_fhLOk4ySRR1mAMH8aPds1ONbmi0Wr5yZaEtMp1fZ4GiuIg5flfruAttGx6Jb1ZuhwxN9FPyy2y1MbIB5wYNGyTIntbvQVi5-GCMs3LIm6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNPY3otxobU5wN1aBvvQFm8HFsYT2dz6Js0EFQVh8uli4-Nt3EVB9hqLfBmcf0ES9cnxZeoeDtOGn1Q49D974JdFDK5DMuUyll8Qd37Y_qnwnV5EnGP--sX5uorWiqD9fwPjRVShJN5-QNf-EkrVtw01vUG9Ah08DE_pNggwf3USeqiq-udP4R_dufX0eoZVml9hULa6T8ufWcG9ad9he8r6jLhpC4NNDv85OnC-CAVISw9FCUbhjFdN03EUvtiXelq-NfDbdiWW_FcoGdvt6JMpxQYQz1f5ygRc4jsa2OVcrl21uj2aSTm4Y85QSD5Ui3Ym0RT0TXrRm2CtAGSRAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbWUa8CAjjRReoJP7WFKBOtfRVINlW_meF2VbaYEGtG9_DkxU6UtAeiT19_wwJuYvqkhe-ZHQs4Gh1-Rl8ONwaSm1onqrwG15_eD6TTMs_wA_ZnQXuu6dnodOJW3eADfR_QvF1UJhS-Mzk5zLbmbBAtZ_hfiqR1rJUKViNiKMRUeehuWH_gP62XOrg3NdeAp6v0uxLHsoCptDbMk1NThr5u1g_Bh1Y8vIw53HPUTW54oNy_hxLVQlJqthSJuw4lvlpF3_EURbUiCbA_vYrDsgonCW1pYpezOANLb6QZkM3ZLs0aYtXjhRWQdZ7-S1m0FHdkgzW1d0g0cU2hq6tq2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=jgrOoLILx2e8oGQ9C7JD5asvtgD90WYPXxOa3SL5uUXtUZlwyZ8qFi6HJb5qBxzEosYREYXtNZ99aLcJzsqf8vBNqfzTPub0EK8HeTBT0S0DDyq7VGTd0A56T0INT23y3Ap8GSno--nE__yZMtyr_625DZU_puD2hFGglJJoG7F4Jk1KomYNBH4OgkKXeiiem_8msD_FcQdf1VAhNT1Mx6QpVkX8G708M_YVSsFieaxtRgAaU9T5r8hAbTbXbJHtyZNMh1xKcIIH0Y_CRupCMkrmAtKI2ZmXloFGyr96mQJc47fscSYHVwDHX51CA9VdfXoE5AT8V1fWNcPhB85LtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=jgrOoLILx2e8oGQ9C7JD5asvtgD90WYPXxOa3SL5uUXtUZlwyZ8qFi6HJb5qBxzEosYREYXtNZ99aLcJzsqf8vBNqfzTPub0EK8HeTBT0S0DDyq7VGTd0A56T0INT23y3Ap8GSno--nE__yZMtyr_625DZU_puD2hFGglJJoG7F4Jk1KomYNBH4OgkKXeiiem_8msD_FcQdf1VAhNT1Mx6QpVkX8G708M_YVSsFieaxtRgAaU9T5r8hAbTbXbJHtyZNMh1xKcIIH0Y_CRupCMkrmAtKI2ZmXloFGyr96mQJc47fscSYHVwDHX51CA9VdfXoE5AT8V1fWNcPhB85LtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مریم، عروس «معصومه ابتکار» در نامه‌اش
به مقامات آمریکایی نوشته که مادرشوهرم
[معصومه ابتکار] فقط مترجم بود!!
در حالی که چنین چیزی واقعیت نداره!
او «سخنگوی گروگانگیران» بود! که برای ۴۴۴ روز دیپلمات‌های آمریکایی رو به گروگان گرفتند
و واضحا تهدیدشون می‌کرد.
میگفت شخصا می‌تونه اسلحه رو بگذره
روی سر یکی از گروگان‌ها و اونو  بکشه.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6565" target="_blank">📅 09:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=IhvIGXRZmte49RNQjY9jyRvEIuKyYSqnK2SC5xloUcuud1nM7DZxVdEqbiHxRDePQmBhN5p2910yCd1VYUMwL2Of0ogz0Ry8as7VQ9W9WCOr3Ligj9RHyX1OatGID_TPrzfqiS9wWEEb9_S9876K3blPwa3xmdH_oikjrxnigOlahZc-hbz5k77HhhQNVuz2-j0NqwUYHy_NEtWpeEQ0dQynttEG5ZVsU1edcEZ-e-2FcyNJgqbxnBFlWPOITenfBR9AKR_mmxHPzW_XR2JvfSlEWSpPZ-CXhklW5fpdiSdIQlLzylIBT812fwUAkMAVzlC8fI6dWd17oIStPqTN2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=IhvIGXRZmte49RNQjY9jyRvEIuKyYSqnK2SC5xloUcuud1nM7DZxVdEqbiHxRDePQmBhN5p2910yCd1VYUMwL2Of0ogz0Ry8as7VQ9W9WCOr3Ligj9RHyX1OatGID_TPrzfqiS9wWEEb9_S9876K3blPwa3xmdH_oikjrxnigOlahZc-hbz5k77HhhQNVuz2-j0NqwUYHy_NEtWpeEQ0dQynttEG5ZVsU1edcEZ-e-2FcyNJgqbxnBFlWPOITenfBR9AKR_mmxHPzW_XR2JvfSlEWSpPZ-CXhklW5fpdiSdIQlLzylIBT812fwUAkMAVzlC8fI6dWd17oIStPqTN2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=lVgjwybxgseUniF1FLfNXidPnMyS2m5lw4A4x0W2-hcQTb9SGymgOw1Wr5jXU-a-lpl4h4pLhLPAmIK62ne4r4Rfs0k-4wKrKqNOxcmKMibeQ4godmwMakP8F1cs79GEgBozjaVE1WqcrhARfQqrnWu5cAS27GcIyILvNyFpGBVpy_LhJAccdyi_5QL4sTBzeFRv5vuGDfGdYV_wlIDlWLRAoJjVTwKldpwLg1QNnjj5D4jC_DH_e5CNrsxaQzFTalzvOY4anIPRuNALjAnxS1xpxyQoWfuLAyg7uUG_2exqrc7HEMmeRMNomAuiQ7UZ2o1QgAYOw7B58OAStBXe1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=lVgjwybxgseUniF1FLfNXidPnMyS2m5lw4A4x0W2-hcQTb9SGymgOw1Wr5jXU-a-lpl4h4pLhLPAmIK62ne4r4Rfs0k-4wKrKqNOxcmKMibeQ4godmwMakP8F1cs79GEgBozjaVE1WqcrhARfQqrnWu5cAS27GcIyILvNyFpGBVpy_LhJAccdyi_5QL4sTBzeFRv5vuGDfGdYV_wlIDlWLRAoJjVTwKldpwLg1QNnjj5D4jC_DH_e5CNrsxaQzFTalzvOY4anIPRuNALjAnxS1xpxyQoWfuLAyg7uUG_2exqrc7HEMmeRMNomAuiQ7UZ2o1QgAYOw7B58OAStBXe1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=Ty4w7D68UbPd5SWgSxKywZ_JkNjhqYg4k2fZewFE25xsLgKXFeZQh66ITAIwIIclxMxlWYGHrUpsGTz1DdHGOQZ5E232zn1x2RVx5Pjn4OLesRt-iQKIvhLsF9AYKU9DjYUqzXzCFV85WjsixbnsD_uQ03Zgk15uA7d8sckTuY7amInfXmfvcUj4j9UNnfkAVsrVUJIGYFh39u7Bfu-W-gjaOwFUhGBBVCKhr_nUfYmercuLu4Qka70cMmyTSl4c697I4YVueVHT6itjFAsXnwLZ-w0xXyX-Y3iwfnn3TF2RsKtdAFyfiGAlkniXFIBqYwaOzYRrelbXsIVG6ZEKEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=Ty4w7D68UbPd5SWgSxKywZ_JkNjhqYg4k2fZewFE25xsLgKXFeZQh66ITAIwIIclxMxlWYGHrUpsGTz1DdHGOQZ5E232zn1x2RVx5Pjn4OLesRt-iQKIvhLsF9AYKU9DjYUqzXzCFV85WjsixbnsD_uQ03Zgk15uA7d8sckTuY7amInfXmfvcUj4j9UNnfkAVsrVUJIGYFh39u7Bfu-W-gjaOwFUhGBBVCKhr_nUfYmercuLu4Qka70cMmyTSl4c697I4YVueVHT6itjFAsXnwLZ-w0xXyX-Y3iwfnn3TF2RsKtdAFyfiGAlkniXFIBqYwaOzYRrelbXsIVG6ZEKEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=mkOQ5-7HHA5PIxv-DLvoxJjs6jklY2wyjKQ3UQWNPk5GSoPkAIGN9F5xD1uVePbTeQ5Ir5GFztuJwXvnluikGuzF6sLJwjiCnxTl-NnJ_p8P39sDcTNBUO4OpCNE8OCwQVhPTSgRYGIyGQneyDZJ7UATfoWaXSg8nAlqrRElFEmmXgAV-tDYDpimtOn8W32LSmrgq8Du1Owh05hDsrNd8hnqErgqLcHUDE6qBmdJbihIdiDMQV1KCetp5yApLU-yp4BLe9kQGvv5icbNKSf0sSMd9bG9i2HXjOyAWTZftb-Np38PKEvSfiHNV_p_s1yM-oS6WXN-UeQoApf2ydubLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=mkOQ5-7HHA5PIxv-DLvoxJjs6jklY2wyjKQ3UQWNPk5GSoPkAIGN9F5xD1uVePbTeQ5Ir5GFztuJwXvnluikGuzF6sLJwjiCnxTl-NnJ_p8P39sDcTNBUO4OpCNE8OCwQVhPTSgRYGIyGQneyDZJ7UATfoWaXSg8nAlqrRElFEmmXgAV-tDYDpimtOn8W32LSmrgq8Du1Owh05hDsrNd8hnqErgqLcHUDE6qBmdJbihIdiDMQV1KCetp5yApLU-yp4BLe9kQGvv5icbNKSf0sSMd9bG9i2HXjOyAWTZftb-Np38PKEvSfiHNV_p_s1yM-oS6WXN-UeQoApf2ydubLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=EaKj6dOMO_QRcOv_ElwitbOBpscv-sMsbnKgMOitKh56MmzfEtJzJyJrM-brr_MK48YCD0DeJqu8wxpMDce3Ciz5TDW6-3hN76RX6_7SeXjLrzCWoIKHtwU_-KqPaTCzDRySm6BPa7-N9bhehoOlrIqLrAFAzz8g6NJQNezSrI5y-F9hfhPFVbc0rJCZLHuR_ycEOOZJEbmhcj5ZTcfrIomHwT5UyxZ950SxfQn7cNz_c_1HxgFFORV8_pvMfRX2Pk612QZKSm6xDZU51KQkWJVOAAMRm6jhZb9ouPjxuK_KqMRYmyjRGSoGCsz1nhLuwD7XPsNeK6ObnoMOXItLYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=EaKj6dOMO_QRcOv_ElwitbOBpscv-sMsbnKgMOitKh56MmzfEtJzJyJrM-brr_MK48YCD0DeJqu8wxpMDce3Ciz5TDW6-3hN76RX6_7SeXjLrzCWoIKHtwU_-KqPaTCzDRySm6BPa7-N9bhehoOlrIqLrAFAzz8g6NJQNezSrI5y-F9hfhPFVbc0rJCZLHuR_ycEOOZJEbmhcj5ZTcfrIomHwT5UyxZ950SxfQn7cNz_c_1HxgFFORV8_pvMfRX2Pk612QZKSm6xDZU51KQkWJVOAAMRm6jhZb9ouPjxuK_KqMRYmyjRGSoGCsz1nhLuwD7XPsNeK6ObnoMOXItLYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=D6NKZ0tn_kJhPqTVr5snCPMiDbIrubwe6NGDIdZsvvZTAz3Br5JDVhLi4flGUfV_RQkNo8QHLWBNT7roicxcWxTSA5agw3rPJBnaPe46Fa7xNKO6zmVfCy-hAD1UKyEgXiWMnDSElghQQMaQMtuxSbXT6sr938Us_klN0XkLQCYPbLTS4i1iuO3DunwL7tq_ZisIDWSJ0ORX5eYdAnkJjHOS8wZ_40EkibXbkJN3-BXJNWXq5ZkZ3OlLVILmWS7BlIZMgj4fNZCPr3JjYSTa0ZTPCD3bVm0U_GV4Il6-NqRJGpzsXyXX-VrfHON8ZS5s_PtmOs8jAtmeXp7Mhmyhrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=D6NKZ0tn_kJhPqTVr5snCPMiDbIrubwe6NGDIdZsvvZTAz3Br5JDVhLi4flGUfV_RQkNo8QHLWBNT7roicxcWxTSA5agw3rPJBnaPe46Fa7xNKO6zmVfCy-hAD1UKyEgXiWMnDSElghQQMaQMtuxSbXT6sr938Us_klN0XkLQCYPbLTS4i1iuO3DunwL7tq_ZisIDWSJ0ORX5eYdAnkJjHOS8wZ_40EkibXbkJN3-BXJNWXq5ZkZ3OlLVILmWS7BlIZMgj4fNZCPr3JjYSTa0ZTPCD3bVm0U_GV4Il6-NqRJGpzsXyXX-VrfHON8ZS5s_PtmOs8jAtmeXp7Mhmyhrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlCTpHYFosiMe2mb9Owy-I6MnTv8x2mFWH15YYHu_F6177MH0OBkv5moG0CgUz026WVK8thgne89nQZyNbsbcG0g9x_ekudjsVQsivalRE61wEF91g5pqO9ltt39SvY3izHM-H1Wvd-r_2ViZpVGabhcStjjfkntsmW00-rk2YS2356pHXgGZPHJ2mZGuQ5MJggbbFYcshuihYFrf1Nhh_1huL-PhREVx_ivUw9PYFysEuMT2MS39R7zYzXb_HCVI71Z-FphgdIObrwcFax95RzskkzehzfsF8rKGzikfa9ib2eZ_sM_Z28FYR_qyYQOLLBdHiOYxZWG3KdY8g1J7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=dY4hWlmZdIhMTvXGnc3kXm54wQjnoELipGgNNCdjV7zOmPs9FXhhNxp9iW1_h5U6GliXEiRDxRz6wTQtPq9HH-x7iyd0Y74bLg8jKoMm9TFcOc7b_uDX5Fd2MUrpV81zJ-ahsukECPc-dn-GAQn_DXxi6hqQEOAamSAhvK9lfJu69e6_WVgM3pNfyvmBbnTvD9eC3G5snl1uK7-p-UV3zMTHupBN9WvbssUMv6-XxiEOcpCGZgFNcCs5fdqfrBdcg9m2sQcwr2mqiX7ReAMD_z4lUU1S5YqD3XJfhjLgnIqX8ihpguojqCkg7bZL4vgJVgqF16p_3dzz6Fler1TA9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=dY4hWlmZdIhMTvXGnc3kXm54wQjnoELipGgNNCdjV7zOmPs9FXhhNxp9iW1_h5U6GliXEiRDxRz6wTQtPq9HH-x7iyd0Y74bLg8jKoMm9TFcOc7b_uDX5Fd2MUrpV81zJ-ahsukECPc-dn-GAQn_DXxi6hqQEOAamSAhvK9lfJu69e6_WVgM3pNfyvmBbnTvD9eC3G5snl1uK7-p-UV3zMTHupBN9WvbssUMv6-XxiEOcpCGZgFNcCs5fdqfrBdcg9m2sQcwr2mqiX7ReAMD_z4lUU1S5YqD3XJfhjLgnIqX8ihpguojqCkg7bZL4vgJVgqF16p_3dzz6Fler1TA9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSm95devtZ7HqfptsudeFksKAeReriyZH60GCpsGsMtTyzksw2ZG-9s3PgBqZQFhoI-8UOO0teNkFYl2x39gXDp-yuNRSeBHCA74oWLQIgYWeXOv8Q09DXrVehqhnsSfSwGXLxewGeiVxn2uDHnDv9k0GG3-Kn17NzgkRUfKLrih22m9wdhgZoJHntWn7gLMqqbb5SuC1L1lF3CZkqIIFxzvHhuXwwK_89Dr8BergXYG9_deIMAiVNtsJK2yGNhf6cecJM1jqZ0U7kmpvjJEp7-Gov_yFw3WtFbSz_OymKWzF2rkKwd-P9vBxeOJ0uyi89eXq53JllGLjwDtvDUfjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.  جلوی دوربین‌ها وارد هواپیما شد،  اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!  نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6550" target="_blank">📅 10:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGcHXMtwP0HMdhctxcRDmM-QDW8E5I_p1GaXZdU9ST4akK28L3hfLjul4vzuf2CTjDGp3J5L9ePuFXdJnMh_FfOrAax7H6Osfa3_7DxA72BNg6ib7WOdII_xuAqEUm890Cvefkr6pD9DjS1JQ-_fsGXDKd4KPCBPzDfkudFFF38DWKSplWf54n_aONlI11JajfI6Opt4csFc8R90HWqvkGZjZLYBQZ7BUviqNGi5sAiK_LR0Iii-puw-sSLUUcpjGa8ZFlsYzJaEIdeqn6j1IOmY9nIycjP1OfELFectpdfQjhrrinZE-YqXmaQYL06i2pQFHFcbYO3wOPPRVsvvCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لکه نفتی به جنگل حرا رسیده
و حیات درختان این جنگل به خطر افتاده.
اما این لکه نفتی که تهدیدی برای سواحل قشم شده از کجا اومده؟
جمهوری اسلامی ۱۲ مرداد (۳ آگوست)
به یک کشتی باربر (و نه نفتکش) حمله موشکی یا پهپادی انجام داد. کشتی داشت از آب‌های ساحلی عمان عبور می‌کرد.
پرتابه به موتورخانه کشتی «مینوان پایونیر» اصابت کرد و نشت نفت رخ داد. این لکه نفتی رو موج‌ها آوردند به ساحل ایران.
سخنگوی وزارت خارجه ج‌ا (بقایی) هم تایید کرد
که این لکه نفتی ناشی از یک کشتی‌فله‌بر است،
گرچه نگفت هنر دست خودشونه که برای بستن تنگه هرکز به کشتی‌هایی که در سواحل عمان حرکت میکنن، حمله می‌کنن.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6549" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Imm-rhfULQqRm8CPB-ak6HqmDSEoBynisJ7JRYmQXrZ6l1D9sybU3NgOY6IKDN1eY4q7mT_UYVrYNAMqcC9HPy1660JEXxSAX2Iy7CUQLv2aEIUpvhlUx6mGqj1xFwid_ErNW1rQmFE-N_7IBO4APr21rVGi_FJa8gEoWR2L2pEdXhP9cT1tTZqKcJFwshpV3yiCh0ywvxVZF3RsWTzC7oC--wjlGxj7iTV2q1ONRyzTazIANupgF9ojiKcQR4Qkmxn2j86mEy6oZQt1FaFR3p22frsBeOIxq6xMyJBmDdZZcvqAuw5hXXkStQ8pSgxGau1GdRsbbZu7arDXJ1KZYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بنزین در کرمان ۸۷ هزار و ۲۰۰ تومان!
میخوان آروم آروم و استان به استان
قیمت بنزین رو گرون کنن که بتونن
با تفرقه انداختن بین مردم جلوی اعتراضات رو بگیرن و قیمت بنزین
رو
۱۵۴۰٪
افزایش بدن!!!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6548" target="_blank">📅 21:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHN-ZnEUKL5uUDlSUcKbprYWtOF4506FyWOGDcEM1rJX-a2uedZcEmz8Piqmg7yDiALEvm-qt_qwDGg4FAS7146NZ5KiZ0-gRNuGXSz4nCy7Qs62p7P4d93FgboshWRGd2QVq42HPSOt9SqhyKTSCzgC7nq_xocl0eIaceaQmT7wHFqpcdXcVeizUIBTrAWa6LwhF7kzRpm4QxJgyKYqBMq_EEwzejMo8_c8paI0dhsfb3s8FCK-dP8ruBVVTTCp9Uu4Oiw2-BA_C7ESGpdFdsb_w1CWVcmb7LAXUmirTB8czd4NITGHcwID0s7uz7RdJZJncP3T2A0mpjes0VBj8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=b4KlUAe8VCJjDxuo7VYKu0LLMDrSRrv3O31HWTjCqMmTkxnDV80tsqmj8y80Ygo3RroDmknENdqq9VhkMTSzJ2JYXzzI3vr_j5eLQJ6k1EcxTc1XsgFleemXlkn4v9B0z71lh_6jrt4y-b_67vC9l1upIkVxOGrG26moNM8sv6ww3mNOISeGztFLRJHN1ozqsturfzjrlR1kQ5aC4oQGGUJbj2Uyxgxw8lcswebtWmnCsGGcJKDw31vN2hnMoo3H3uy3daCzw6Sny4xm6cRRfvgZcla8ME3XF1w0n-rAOVp82u7OMTruxN_GC6KQ7Izk1HIh2o4-OWpiP3jX7siK2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=b4KlUAe8VCJjDxuo7VYKu0LLMDrSRrv3O31HWTjCqMmTkxnDV80tsqmj8y80Ygo3RroDmknENdqq9VhkMTSzJ2JYXzzI3vr_j5eLQJ6k1EcxTc1XsgFleemXlkn4v9B0z71lh_6jrt4y-b_67vC9l1upIkVxOGrG26moNM8sv6ww3mNOISeGztFLRJHN1ozqsturfzjrlR1kQ5aC4oQGGUJbj2Uyxgxw8lcswebtWmnCsGGcJKDw31vN2hnMoo3H3uy3daCzw6Sny4xm6cRRfvgZcla8ME3XF1w0n-rAOVp82u7OMTruxN_GC6KQ7Izk1HIh2o4-OWpiP3jX7siK2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی میگه :
۱- موشک مستقیم خورد به خونه مجتبی
۲- مجتبی خودش هدف بوده
۳- زنش کشته شده!
اگه مجتبی هدف بوده و موشک خورده
به خونه، قطعا همون لحظه مجتبی کشته شده!
اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید
که دست اسرائیل (دست خدا) عیان شد
و خامنه‌ای جوان شد، ولی از قرار معلوم میخوان آروم آروم بگن که دست خدا، هر دو رو از زمین برداشت.
موشک خورده به خونه و زخمی شده  باشه :))</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6546" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tR05KlxGl1XfjepMZeZsiVYOLqPdQpWJuUlj0hsukV4RxGt-zGPu5F-_qbVXNCSYWkWBiyFQBDTiT0FAzgtrfXz8GGxtWT2fV82xb6qJGkmPRfpCUSB3RfLuP-OnnvLlNzXHyCYftHAN6F1ljb4T50MLS8OqJf5ZBs99u58CkgAKo5zwVAAgM7k3oCzFbcpMayqTJl7Wg9rqvOoDLnOxhhc4gWcesY2-yxiJl-o2sV90GcQ8UzGIhjZYpr3kx_3oG4F-qgMNbFwTRSLNGFFVzl5BXt0faY85UalZtOj9E_DId0cF1GM5lwz2vyLElJMTI25XCeH7nDYATtlc2fOg3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=Hn1omL0TTS1B-1gRDV2zpd2m5Ej-OnsAGqfBtClA4xZJhRhGXZbgMnd9pqMd56rtQavLpIO6Uvi7ZinYngnZPt6GtPHQ47ThG81bDeEwj2eht0DUKQQdg6IjcAbveLvGI9LibAdSVdOPG0fHvTLKlyGN57YILZhifUGyyPzP_E2fyd9OLz5-5JSBiECbZHBQeROQYbEkVgRNRPnhD10BUmSQZdTzzYM1kD3Z9O5c_Q0FQ9OaJ9-fz0kkTlQQL7t5JtUk4EsQKTM2etPFo6EBRVtNXoddgIoIFrAsv2a8LXnc4jSJEea4pHoyKxVCbMipE3S-K7eJQu99l2gWNg8byg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=Hn1omL0TTS1B-1gRDV2zpd2m5Ej-OnsAGqfBtClA4xZJhRhGXZbgMnd9pqMd56rtQavLpIO6Uvi7ZinYngnZPt6GtPHQ47ThG81bDeEwj2eht0DUKQQdg6IjcAbveLvGI9LibAdSVdOPG0fHvTLKlyGN57YILZhifUGyyPzP_E2fyd9OLz5-5JSBiECbZHBQeROQYbEkVgRNRPnhD10BUmSQZdTzzYM1kD3Z9O5c_Q0FQ9OaJ9-fz0kkTlQQL7t5JtUk4EsQKTM2etPFo6EBRVtNXoddgIoIFrAsv2a8LXnc4jSJEea4pHoyKxVCbMipE3S-K7eJQu99l2gWNg8byg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.
جلوی دوربین‌ها وارد هواپیما شد،
اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!
نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31726f423.mp4?token=lKTZuVwPh5-GFRdx-sMfRUXsT8izCkcArUXzffXuWNaXxEVXkB4Fhan-qYSDeHask69N77UysUn45djDrKkR_PHQh6Re_fqEDf69KraE-zPP8Ld_t2CYuB6lznl3oq8NhI1xVu6cWxH8_bwFGfNO-LFGKL9gdIYNbN9Djw0LQUKgz39Znf5OWj_X_QweGHB22o90lFSdJsISliI0KrRbLL-cAjTlonls1p1WCzpZjT7t0pKdieQ3rLmvLfSYFDN4evN0zTCfp5XMUyjWfRSJ6F1hnkUwz3_orHIgDBBczCyoVWjEca0o88Wu23UBlpmiZq8Q3GvXLx991B21Slf0qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31726f423.mp4?token=lKTZuVwPh5-GFRdx-sMfRUXsT8izCkcArUXzffXuWNaXxEVXkB4Fhan-qYSDeHask69N77UysUn45djDrKkR_PHQh6Re_fqEDf69KraE-zPP8Ld_t2CYuB6lznl3oq8NhI1xVu6cWxH8_bwFGfNO-LFGKL9gdIYNbN9Djw0LQUKgz39Znf5OWj_X_QweGHB22o90lFSdJsISliI0KrRbLL-cAjTlonls1p1WCzpZjT7t0pKdieQ3rLmvLfSYFDN4evN0zTCfp5XMUyjWfRSJ6F1hnkUwz3_orHIgDBBczCyoVWjEca0o88Wu23UBlpmiZq8Q3GvXLx991B21Slf0qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون (نیروی شبه نظامی تحت کنترل سپاه ) در تجمع افغانستانی‌ها در ایران ؛
هر کسی گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDOTP4vVPiLwBHoNprawo-nVk6j2u4PfNKb4xBTjDp0LS5HIp0qzQD9QkT44oYXNe-_bQACOkcwhVIl0zffCUOB0aTuPL_L_8bXcEEE9hJnWkHeBihwMS99DFDbR6hQUwrpJLu9I8JwyqbJkCbrszYaYdKKILpRNaslQn7jIUnN5CbrgiuK3is3E06beViq2B2nvUiwS4eAh4a7yGEAP81eKhx4sEafqkSfBZJuP8mHhWpTckC3FZMIfyoacJyEYaR9ugvXQpZf-zWQy0IquwcwQ7GTwGoWvWIzLH3FNVPkRfS--C_GVsW59iMIHS4m6Nzy0vDebbLupBy1FabiLMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCj-SUbAjNiqGWTtrfNU211Z4A7obukaGbj5vWHuum7itN-CUK0pPaTK6IuOT3pSNVI_y5B1A2Rt5s2K0LSDgdzH43DPxxo-bA3QRzldI9CGXjuiISNrCGRyeaNoVWUfvRk3NfBsoRN1tjPJhTXNeM0r4V0eKq0GE2_0K_9VWzjD-iER50eNjFHDUzv8UcnA0Abv44PeZyHme4d8LNj0T23vGC-cNeOL2JPv2Gft5SoxAYJ5YE28kYnfQ8z-5dbauFR_LhmjF2XU5tdHBjKm9P-VEFssnYD3gR1gtyl64Obh-n6WbCVqoyVIGL0GBfxZZa8fzneltK8rAN5UpTREPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTPhRgryGpO9CWN3qZsNOffF9BVeK25dWO6qoCmAvA_YS55khiM3VXMqX59XY7O4ny9patzzvSZDUYf8NiHjg91yvOcKLwdC6biE9iZCKQQjqt69swlcHtiDBkudn3uOnhVaeQGG6-QG2MvuOGJMutg-5U-2vmVAN3dL557-oOqSwKmUZuRCxu4IN5Lx-Ah1tbjsFY3Z7gtSRD5J06xnyoBEmZC9EVjDUSIc5Q0yc-0TVd_q5uwF0_s_LhFoKtPBBG90BHl2YsYSp7qpe9f70k8YPCt4whw5dU5VjXk4bBgbjzB9McN_Rw6kXK6KBAnUCYgR8atoIp0_R9Ig0FkwFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=YSwTKLDA-kJAVa83P7TM0fMLX8tDPPXOZzlXfQWs5226LYRkQokS84KpwSWvKLtMWTqFU1UjtA8C__E-NEGxW4SFgEXnssf0fB71YhxZsB5AyoDt7aXpkeVxLlbmSnYx6d5GRpLPYHfZgwznBQR81Z3IVd05R0XbkRDdHGyeJw4TRqJ9yRe55LOnqnC-kq-5-INsN6D4_QYANHzLFMFjolBeZ9Czg6TR81c2SHijmhclumRPQjpvhWewa0XPSLTbogLFq9kc1Jvd9_t18Xt1OK21Y2CJLKLhOg663Yo0pHrhjbKYjC8E2XPJ9qS1TdcHeiLZoIKByHYOn1sOBr14ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=YSwTKLDA-kJAVa83P7TM0fMLX8tDPPXOZzlXfQWs5226LYRkQokS84KpwSWvKLtMWTqFU1UjtA8C__E-NEGxW4SFgEXnssf0fB71YhxZsB5AyoDt7aXpkeVxLlbmSnYx6d5GRpLPYHfZgwznBQR81Z3IVd05R0XbkRDdHGyeJw4TRqJ9yRe55LOnqnC-kq-5-INsN6D4_QYANHzLFMFjolBeZ9Czg6TR81c2SHijmhclumRPQjpvhWewa0XPSLTbogLFq9kc1Jvd9_t18Xt1OK21Y2CJLKLhOg663Yo0pHrhjbKYjC8E2XPJ9qS1TdcHeiLZoIKByHYOn1sOBr14ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل کوثری :
‏سردار کوثری: شمخانی برای جلسه فرماندهان در بیت بسیار اصرار کرد
‏سردار رادان جلسه را نیامد و سردار پاکپور هم نمی‌خواست جلسه را بیاید اما دستور شمخانی برای حضور بود؛
‏وزیر دفاع با معاونینش در جلسه حاضر شد؛</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

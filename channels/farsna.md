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
<img src="https://cdn4.telesco.pe/file/RT0Y9vEDMtXt0auRdWvIaSKaml12EhoownyGZce2DqM5mz336LwSiJuMv0L425Zd5r7PRyy71QxaSsNOFL0tXpFbxa_0HNQB3NyxJmufBZLjo6Q-MCCcNtPsHOaWydS4sRKWTv3Cs4pX24SA4pplzAoEVzulG0fka03fgo2likFgUzsIi6232vZ20Mry7w27YxjV8CKxOfSBOTYRItkdClZFcTZz06ppjJZaRiDUB34Qa_LKSmLxvBAPZxxUMa2Nv5tttUtxOhp_jywkklYRqi7RCPc7hvNqR-OLJhyzhhzVYvP2elKKNqrZKgqaytWEtg4oUDGZcOJpTCA_2iOh5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 23:33:35</div>
<hr>

<div class="tg-post" id="msg-436950">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شهادت یک پلیس در سراوانِ سیستان‌وبلوچستان
🔹
پلیس سیستان‌وبلوچستان: ساعتی پیش، سرنشینان مسلح یک دستگاه خودروی سواری به سمت خادمان امنیت در یکی از جاده‌های شهرستان سراوان تیراندازی کردند که متأسفانه ستوان سوم امیرحسین شهرکی به شهادت رسید.
🔹
اشرار مسلح تحت تعقیب…</div>
<div class="tg-footer">👁️ 658 · <a href="https://t.me/farsna/436950" target="_blank">📅 23:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436949">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">احتمال اصلاح برنامهٔ توسعه و بودجه ۱۴۰۵
🔹
رئیس کمیسیون زیربنایی مجمع تشخیص: باتوجه‌به شرایط جنگ در راستای اصلاح برنامه ۵ ‌ساله و بودجه ۱۴۰۵ بررسی‌هایی انجام و پیشنهادهایی آماده شده است.
🔹
همچنین جلساتی برای تهیه پیشنهادها جهت تدوین پیش‌نویس سیاست‌های کلی پساجنگ برای بازسازی و اصلاح برنامه‌ها برگزار شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 664 · <a href="https://t.me/farsna/436949" target="_blank">📅 23:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436948">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0PG1ZXHX-o6KlsTiP4ESW4XiJiPmQWrHM-rjAsgQw5Fq1qCaJvGMvA67EkxK0OlrbsrITMCJmYXuxIIobohxWHuyaEqbfN6kvF915HuGQV5hhjhWvNatlJTThohHfwRcAKo7af5XEYhpL7lzEZkyabP7Eg2j0jMxuCC7fCGCFJ64I2GbfR9y6DmcN0bcFwY_RMzLLmyeqCkOH0XmSESuQNVRXWjckI-opEfuRAYHc0Ajlpdki_oUqlQiD-FAOeatdOMpv237_Vip0N1_cTkY1w_ObZoU7PWd6BiwzZEPANTRXSA83TC6kgptClhgniGNO5Zoznz0p8wXYdfunsVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد تمدید خودکار قراردادهای اجاره‌خانه روی میز سران قوا
🔹
وزیر راه‌و‌شهرسازی: پیش‌نویس مصوبه‌ای شامل تعیین سقف برای افزایش اجاره‌خانه‌ها و تمدید خودکار قراردادها تهیه و به نشست سران ۳ قوه ارسال شده است که در صورت تصویب، بلافاصله ابلاغ و اجرایی خواهد شد.
🔹
تعیین نرخ دقیق در استان‌های مختلف برعهده شورای مسکن استان‌ها خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/farsna/436948" target="_blank">📅 23:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436947">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🎥
هنوز چراغ حضور مردم جهرم خاموش نشده
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/farsna/436947" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436946">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
ارتش اسرائیل: ۷ نظامی ما ازجمله ۲ افسر و ۵ سرباز در اثر حمله پهپادی حزب‌الله به‌شدت زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/farsna/436946" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436945">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzsRr8PIODU7Cj7rJSRfUhXMcxY449oXSZqe2jycl9zEta2XMnKF4wNpmT_JbPl4qvZ7xI_iWrRjgvG-q1H_MrN3FOXIOy8qI7rpVLyRPHiQhYX3If8X1YcshVPcq3-dUCSTSlrO7P3rgOmvjb8i1jZPhtva0YugE-YFDH1GnMZBtX3Uf1aMWiK4b8dsgvBhN8qTCjn8YVJZRkN2g0Vx8RK7FMsCrGj8IE1q92Rm45jhYzrD9KDVB8mhiKBmjw-sPgjP8DYvRuQNm1ABWIiGer8pi5U_FAd0D6wC_S_l0Qbm1g0PI09ZqFSsjPh8d3J8PZ4vSX-xWjRj-764qk7otA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
جزئیات برنامۀ تیم ملی در ترکیه و سفر به آمریکا
🔹
نبی، مدیر تیم ملی: ۸ خرداد در ترکیه با گامبیا بازی داریم و یک دیدار دیگر نیز برای ۱۴ خرداد برنامه‌ریزی کرده‌ایم که تا چند روز دیگر بازی با این تیم خوب هم قطعی می‌شود‌.
🔹
تیم ملی ۱۵ خرداد عازم کمپ خود در آریزونا…</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/farsna/436945" target="_blank">📅 22:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436944">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17c21b8367.mp4?token=Kw7uxuTvUak_o2xnzHtzm4mo7G4zRKid6xT8i3SaoDljAo_S8t2wIzMM3HWyTyO09Qm0_wt5MsBOPW0cr8SadDC_0yot0dYo3jHsprTJUILHTije6gnBpJDs5icChcs1-7t9SlGvh9BshfeK8mIDyMjxhccgRaYMefq-8rli2lfzru0059ACssCLYpsuFO9W0IaDlfNjowjBVDZEYchoFYKsqN7TfA-G4qWw5FbLmO4OD5Wp-VwP7ScOU41OC3bE_pLUibRpvWnFEOyvi_3jbnIs_PlBsGwwn8zH5HBIE-bjhlUl-QhTYJ14wNGKQAeKRf4xZirxoZQ7FHlBXBXvYld9mE7hpAbzFC0XQI5CtwAG99mpkoyOiwpTIl_vp_9aOvpJrCQVARVMOmiY_26m3W0drrW-v81vfX-cbcIB0lkRoCLxGfd-sXYx_qDKYbVAgZ7AGIoJINY9BL9NvG1ETShfjMl7Xn1JUeLUDqRT8Vhm3rfR7lBTd0BSoPxtGLPZUPhy6_uSXrYkhTCWLWj30ApIw-di01sQRR7qBPkv5XEgMIu0705YG8_GoFOfa5fCYCrjgQ6sgwtNuMvhpVB7mE7fMgIHJ8Bz5h-87M_LiBWKW4V9RPfA9UnX-gIs1GjcjzKPFDKl2P_JIuljQgqAEZM1XCClcx_825Tj00RjI40" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17c21b8367.mp4?token=Kw7uxuTvUak_o2xnzHtzm4mo7G4zRKid6xT8i3SaoDljAo_S8t2wIzMM3HWyTyO09Qm0_wt5MsBOPW0cr8SadDC_0yot0dYo3jHsprTJUILHTije6gnBpJDs5icChcs1-7t9SlGvh9BshfeK8mIDyMjxhccgRaYMefq-8rli2lfzru0059ACssCLYpsuFO9W0IaDlfNjowjBVDZEYchoFYKsqN7TfA-G4qWw5FbLmO4OD5Wp-VwP7ScOU41OC3bE_pLUibRpvWnFEOyvi_3jbnIs_PlBsGwwn8zH5HBIE-bjhlUl-QhTYJ14wNGKQAeKRf4xZirxoZQ7FHlBXBXvYld9mE7hpAbzFC0XQI5CtwAG99mpkoyOiwpTIl_vp_9aOvpJrCQVARVMOmiY_26m3W0drrW-v81vfX-cbcIB0lkRoCLxGfd-sXYx_qDKYbVAgZ7AGIoJINY9BL9NvG1ETShfjMl7Xn1JUeLUDqRT8Vhm3rfR7lBTd0BSoPxtGLPZUPhy6_uSXrYkhTCWLWj30ApIw-di01sQRR7qBPkv5XEgMIu0705YG8_GoFOfa5fCYCrjgQ6sgwtNuMvhpVB7mE7fMgIHJ8Bz5h-87M_LiBWKW4V9RPfA9UnX-gIs1GjcjzKPFDKl2P_JIuljQgqAEZM1XCClcx_825Tj00RjI40" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کولاک دهه‌نودی‌های کرمانی در بیعت با رهبر انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/farsna/436944" target="_blank">📅 22:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436942">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPPdOph8q3ETCmPv6ZTMj8hZ54OkJD9NIWmMl_kaUDAvWWNh9ItWV5RidUoIdsgmQWhh1PcjTnN5FK7aaq0YSS-fXUMBfMh9kXJoXPdjEKB79IGPRaYHp0M49B2Z7ZrJglZlempbp-LzgR7IrvKE3AuNsq8EwmqI9MT3cdmrsCjAFg_apqWKKt-hXSw9cY-tEaAyGHzzFs3K3zcwUFPYOp6QLZMwK-y6CyCc9HqJ4jSh1vUZOOz8jJRsYPJmB9u-YHHfEmdjxauFlLPsNByShQKWww5l2k-hw7BCTpi0SigDPj5xXz8Qf7cDIkpqoNNCeGNw6s0oHpBYm9BZvxkC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سردار قاآنی: پیروزی‌های ناوگان صمود ادامه دارد
🔹
دیوارهای تزویر آزادی‌های تمدن غرب را  فروریخت و فاشیست صهیونیست را بیش‌از‌پیش رسوا ساخت.
🔹
فلسطین را باز به کانون توجه جهانیان بازگرداند.
🔹
رژیم صهیونیستی مغلوب را که به تشدید سرکوب و جنایاتگری دست زده، سریع‌تر از قبل به نقطه پایان نزدیک کرد.
@Farsna</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/farsna/436942" target="_blank">📅 22:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436938">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G-fMp709wz2M-XIfstPr8JcG3PJdUdLlkgPV5rT5i4XqD40kApC4NY3ckGVM3JSUp9Gi376fljZqHNZvv4yXutXCeF0OoofY3OEC5y_pz2NQ0AA5mf3RWt-dUVg6u2Z1uHH2ZU91mwECfuJ0f8bAYPsC5jDfhZgvfFiiSv9trPY-qF58UYFDSxYlX_h5NSvv_rbN0KwFaenXHOSOraDQFXcIUs3Day-MPjpIJAqnTnnS08MVaJTDLU1qdX4fgTKKhJMhhEZTcV7EqwHu25nzxjeiSGOb0mGeNgWfPBELPzTDz2L9jCVqE2w-itaXDFZvTgE5QozbS191WYPMg9J6_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EmdPDLktL20t39X7nYHZSeNarMtunvV6zI7I2yA6Tt0-lOVfiqu7UysWd9Hrn8Gw5EpUCce-2UABflPuxLkEgiVk7DgH9hACnaNBl8BZdgxNljs5apzl44uaEb7hm0HSAcsAB6o0iAirYKGPIaCFmlzTDMiBBPo-LgwXNFWguRDCHsDjEMrkgxFg9LTm4XYXECueHYsT5V7nUJSX19Z3TgQVKJ0tidqT9BByVDmN_xD3pSHvb4QcLoCFIFpjs0VAu1E-Qu96VdixydMAjmCLmZ9RIUxPTWN0fAJFQ8dBp3FWmXhQiSlNwB2tV1Kka53yxLXlrlu8VaFBlXV0fh0UKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPZzI7pnHnLJEqxgFDXJD67SagMIyTnnECx9Eytt94yDJcXcdmb3HY6J5YzQ9TkuTKYzfex2oX3dTwS2gzefQcEGdoyc3peFZg2NqtJJmOoOCJMLw4Ufhg7R0wPY6FTHydfVyRjR4eMzqbt6FSAkZsjMIutfCSqKREI6ciuKCYOFQtrC6Npjwq9MdMUTEp7q0zMR9-rn0KsI7_1B4o1ki-beR7UqlIB_-g0bv1mHQ17q7ApW0pjPhBFRtXeggodZ5ybFFto96RVkvyuCqjZXQ6GGf2-YNwdPFz1TtwHgkjTzahrjmwKMmXhNEyQteThDxRKXYwTifRBC_WKjZJTWKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jbuebz_1s5pznjLg0jwN2PYkbnK24X4TPM9ie1_24ppO5IUi2n2_1lLJayxshf52NMwFFtHZYbrbL89jS9YVbns1aXmTPySQE1ARIkFCs56FEzytUSbGtLWskY2RMnBoIR8J4CEiUkyzS1KvF4DxErusXOWCGInFo9gCTiswGRGAXbDeKHOy2t1Q4n4jnL4GQKKB0erNARW9iC3N0D_YqC3XE4OGR9_kRcWaYyDhwKwgh9MCo5S603MXRJlabzQ78WhLytwzcQk9I8lPdfhnMfYm5cI0Q1auEC1UY36nAFTlQKH5_fgeUj_BFaABO_hA04Q9zTxZQJ43YFrDRkC2Fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شیراز در حصار ریزگردها
🔹
با ورود سامانه گردوغبار به استان فارس، امروز وضعیت شاخص آلودگی هوای شیراز با ثبت عدد ۴۵۰ در وضعیت خطرناک قرار گرفت.
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/farsna/436938" target="_blank">📅 22:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436937">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🎥
خاطراتی از عزیز مردم
🔸
فرزند شهید آل‌هاشم از پدر خود می‌گوید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/farsna/436937" target="_blank">📅 22:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436936">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8o7-2OsaaSALYFEZtUbqG8uEVWc15LOKs7hzQPl3E9VRhWxqGZ_Z4WVLXcPDGm3fVJDXY08nzol8Gy0V1yTbveW7jw1gqr5GW9pgbg1t7HZhxFq-ERpyIKFdcY1lYXPFW4IynXK3mjuPs6RwWbJEuBv3HwxoYXXXYUOqlAHUHMO4uKNq1OEuscdNgVb58Eht853orm2y7SUkraNubkBsM7M4pMI6mqYDXd4A13PdrbwIFgBQ8RF7Wqq5fc_9x5jRVjtjX1NKnfPyVNbNMEQ1XLXoUWNhhq34S5nIhJg6ToK84ceQMWirkWyoy0jH7Rrh51xq1hqHTajexHCm3a_wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: به تسلیم واداشتن ایران از طریق زور توهمی بیش نیست
🔹
ایران همواره بر تمام عهدهایش پایبند بوده و تمام راه‌های پرهیز از جنگ را هم آزموده. همه راه‌ها از طرف ایران باز است. به تسلیم واداشتن ایران از طریق زور توهمی بیش نیست.
🔹
دیپلماسیِ مبتنی بر احترام متقابل،  کم‌هزینه‌تر، عاقلانه‌تر و ماندگارتر از جنگ است که ایران سال‌ها بر آن تاکید دارد.
@Farsna</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/farsna/436936" target="_blank">📅 22:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436935">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🎥
شب ۸۱ اعلام وفاداری آبیکی‌ها به ایران اسلامی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/farsna/436935" target="_blank">📅 22:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436934">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40641a8da3.mp4?token=ts6kcIiMpSEUrLPsSnJhvxgfgwoo5kmnAfH0w286cZx2VoqKqpFKkU7STGYiurvpSJPpcNYfdY93iHrvVyKcQ27dcUKAGD0-tgBnQd88QyjCtI06Dyx8Dbp-yBatldJ1xS1q-vma8YqJR-VUZntWskfZxGpw_vgWuLG7XrTk3yGnrQU2-aF40CW3rjhBn6IubvlPaEPofPj47345cxPQGr4alZWnYcBQS81LZZa21fXFhipCPioCLAGQNelYhacnU6WVpGBdtJ1q82LpTSYxH8ckIWeQE-MIqHkEcV6Qhx2PpTPE3WGtk75LBkMXaA9Qr70Jf8Zp5KGKueUmykVUSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40641a8da3.mp4?token=ts6kcIiMpSEUrLPsSnJhvxgfgwoo5kmnAfH0w286cZx2VoqKqpFKkU7STGYiurvpSJPpcNYfdY93iHrvVyKcQ27dcUKAGD0-tgBnQd88QyjCtI06Dyx8Dbp-yBatldJ1xS1q-vma8YqJR-VUZntWskfZxGpw_vgWuLG7XrTk3yGnrQU2-aF40CW3rjhBn6IubvlPaEPofPj47345cxPQGr4alZWnYcBQS81LZZa21fXFhipCPioCLAGQNelYhacnU6WVpGBdtJ1q82LpTSYxH8ckIWeQE-MIqHkEcV6Qhx2PpTPE3WGtk75LBkMXaA9Qr70Jf8Zp5KGKueUmykVUSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
وزیر خارجۀ عربستان از ترامپ تشکر کرد
🔹
فیصل بن فرحان: عربستان سعودی از تصمیم ترامپ برای دادن فرصت به دیپلماسی جهت دستیابی به توافقی قابل قبول قدردانی می‌کند؛ توافقی که به جنگ پایان دهد، امنیت و آزادی کشتیرانی در تنگهٔ هرمز را به وضعیت پیش از ۲۸ فوریه ۲۰۲۶…</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/farsna/436934" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436933">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b238b716.mp4?token=ZdFB-XLGq0eImpoONyeN3uW_G7YzzHzLyaRVuWFdgVaW163wiAwfJAjtsGNRhlnfP9w6Cfnpet4s7YhY2cqKqGjS2HShnB8lGGEckq6w72ybjgVO82IXqpgwnG46r_ZL3SkNnT9qvwYn41AgLOS4ONiHogM_UNW0RLAaoIB-EvKhIyI3DzzzOyuIw6bywE7NXJQZs6mOAQYHzJIpliezNH0-a8UC7bI4qRzkESkTh1PtAeXb0M_krKgtyfrWmthsI5cIp7Q_81HLK9TvO6eRgBDum-kIlx6X9QGtb0tJ5MGhc696tsBZ_5a958nyrkej2JJF_kH1naFgbIvrtVGDUooqlsBGLAdMcWamQxV3QcV7Yp9zBrhHX3u5p9LG6n7yo25WgksQRww5vi25EYfHUTrUy_wsR4vdZ2ggqNqBLPBrBEZ3HmZUmBqhIu11Xa7JFl4MQUHqw1tJz5HSL-ewvGkQpPvsqA2dYFTpA4HfBqRu6RvWfXfIlL1m61sqz-Sfe03LiLKa9ymOzPgi1RWGT4AHzs0F_6rYNb9hO-pOXnxW8UlqgS5EGNUOJBP8puXoi0BmT5jLTndCzyuBSex-kV13Jhlsnnfzr2wSdCyrpmZf0LAirPr0YGtVcSC5TtDPaGWHqEFHV_cdqEpHk7CSzsn_f88TuVBLz8zCu1UjD0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b238b716.mp4?token=ZdFB-XLGq0eImpoONyeN3uW_G7YzzHzLyaRVuWFdgVaW163wiAwfJAjtsGNRhlnfP9w6Cfnpet4s7YhY2cqKqGjS2HShnB8lGGEckq6w72ybjgVO82IXqpgwnG46r_ZL3SkNnT9qvwYn41AgLOS4ONiHogM_UNW0RLAaoIB-EvKhIyI3DzzzOyuIw6bywE7NXJQZs6mOAQYHzJIpliezNH0-a8UC7bI4qRzkESkTh1PtAeXb0M_krKgtyfrWmthsI5cIp7Q_81HLK9TvO6eRgBDum-kIlx6X9QGtb0tJ5MGhc696tsBZ_5a958nyrkej2JJF_kH1naFgbIvrtVGDUooqlsBGLAdMcWamQxV3QcV7Yp9zBrhHX3u5p9LG6n7yo25WgksQRww5vi25EYfHUTrUy_wsR4vdZ2ggqNqBLPBrBEZ3HmZUmBqhIu11Xa7JFl4MQUHqw1tJz5HSL-ewvGkQpPvsqA2dYFTpA4HfBqRu6RvWfXfIlL1m61sqz-Sfe03LiLKa9ymOzPgi1RWGT4AHzs0F_6rYNb9hO-pOXnxW8UlqgS5EGNUOJBP8puXoi0BmT5jLTndCzyuBSex-kV13Jhlsnnfzr2wSdCyrpmZf0LAirPr0YGtVcSC5TtDPaGWHqEFHV_cdqEpHk7CSzsn_f88TuVBLz8zCu1UjD0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۸۱ و تداوم حضور پرشکوه گرگانی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/farsna/436933" target="_blank">📅 22:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436932">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/599fbd495f.mp4?token=HCk7LUPzXMZfdCcXiCORX5MvmVZQyEhIn6K4yueFFhQ9DQvnLVr568skkzFpOAhL5HtiHCc5hoe2KRtZulfK2TGv13RgxCRL5vcpJJQjHZHicpKazacOaCQ3Rzf6_uh4pXfeyq1T93yjNrJnC8LlmWJ2yM1Cfy6xMm_pX7ngOr59W_m-DNUl2z3-ALRtwUiJ1ARmrxtlQI6ikb5MsDx-TsJmyhcVeQc_g_iu8gYzm24YuVPeLDyswTMK4Cdbua1Hy6b5B2P8PFEquwDjYNmA1nRID5K1wtdO5PvfklrEuQQtLFfHQTZDkv7JeLY7A7_d8YRZxrwY_QeQ-oaArYkRHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/599fbd495f.mp4?token=HCk7LUPzXMZfdCcXiCORX5MvmVZQyEhIn6K4yueFFhQ9DQvnLVr568skkzFpOAhL5HtiHCc5hoe2KRtZulfK2TGv13RgxCRL5vcpJJQjHZHicpKazacOaCQ3Rzf6_uh4pXfeyq1T93yjNrJnC8LlmWJ2yM1Cfy6xMm_pX7ngOr59W_m-DNUl2z3-ALRtwUiJ1ARmrxtlQI6ikb5MsDx-TsJmyhcVeQc_g_iu8gYzm24YuVPeLDyswTMK4Cdbua1Hy6b5B2P8PFEquwDjYNmA1nRID5K1wtdO5PvfklrEuQQtLFfHQTZDkv7JeLY7A7_d8YRZxrwY_QeQ-oaArYkRHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یاد شهید جمهور در هشتادویکمین اجتماع اقتدار کوهبنان در استان کرمان
@Farsna</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/farsna/436932" target="_blank">📅 22:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436931">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a44ad4f2e.mp4?token=e9PTYJtkr0hQYYwrTsE59dvt64rJifTV-IGHuQx15-UrsHuJLF6F2qH8eH67ssCeKhQuXLc8p9E18nJSM2bJpm8NKgiKdpL7r9l6EITRcN_9Zd6t0tYBvsL_ECfFDvkElFekpwv-4OpoA3jGW1zFr7xodRkMg_drJ-hsDkR3K9ITTziHTvkYR6CBSAXHB81JsnTUbzUMGLQTdAqFNmsaxIiOwouOVFK8XCX6JyW5YslLdIEvKo3nxnuGHYHK0JdUE-Iiz2rPYbK5eVpa3klIheQ2tRvhGO979hAgiGwRA1cq_09s4Mr0Lod0n6IfiGtb-ELdKxccKuQFh8fsP2Kdvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a44ad4f2e.mp4?token=e9PTYJtkr0hQYYwrTsE59dvt64rJifTV-IGHuQx15-UrsHuJLF6F2qH8eH67ssCeKhQuXLc8p9E18nJSM2bJpm8NKgiKdpL7r9l6EITRcN_9Zd6t0tYBvsL_ECfFDvkElFekpwv-4OpoA3jGW1zFr7xodRkMg_drJ-hsDkR3K9ITTziHTvkYR6CBSAXHB81JsnTUbzUMGLQTdAqFNmsaxIiOwouOVFK8XCX6JyW5YslLdIEvKo3nxnuGHYHK0JdUE-Iiz2rPYbK5eVpa3klIheQ2tRvhGO979hAgiGwRA1cq_09s4Mr0Lod0n6IfiGtb-ELdKxccKuQFh8fsP2Kdvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدومیت روزبه چشمی در تمرین امروز تیم‌ملی فوتبال
🔹
طبق برآوردهای ابتدایی مصدومیت کاپیتان استقلال از ناحیه همسترینگ پای چپ است و او به‌زودی برای تشخیص دقیق میزان آسیب‌دیدگی خود باید ام‌ار‌آی بدهد.
🔹
بااین‌وجود باید دید پس از اعلام جواب ام‌آر‌آی، این بازیکن چه‌قدر برای حضور در جام جهانی شانس دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/farsna/436931" target="_blank">📅 22:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436930">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6be29ce9f1.mp4?token=lt18IItOORp3cFOb4ATzJCVZD0Qz-i6HbGHsAPyrgBuQBmg-LFSruHuuddNBY0wM3TOcolU_PpPWlIAouCKsAneeiC5LYIzIQU5n0FmH4zITYVjSZxmiwxRWtNOyk5iL9OKI7kzF3d3MGCPGfFE7zvrxKYBMuW2h1gUHHMmwrjcNKpMIaG9WyVymnCRW8ZMfGWMkGCQZIIWpoupldGImgG901s9pGqJ_6hZjrH_aIqG8jHPHUJpZQhFSZreBnlj9rHSwUMn95f1nDEYI9ArY-LPMU1I5sf3pXYtYug3Le_noOXQW6-q3rBhuwm4PMdBhVdiljeV5aQw0kUrBe_mziw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6be29ce9f1.mp4?token=lt18IItOORp3cFOb4ATzJCVZD0Qz-i6HbGHsAPyrgBuQBmg-LFSruHuuddNBY0wM3TOcolU_PpPWlIAouCKsAneeiC5LYIzIQU5n0FmH4zITYVjSZxmiwxRWtNOyk5iL9OKI7kzF3d3MGCPGfFE7zvrxKYBMuW2h1gUHHMmwrjcNKpMIaG9WyVymnCRW8ZMfGWMkGCQZIIWpoupldGImgG901s9pGqJ_6hZjrH_aIqG8jHPHUJpZQhFSZreBnlj9rHSwUMn95f1nDEYI9ArY-LPMU1I5sf3pXYtYug3Le_noOXQW6-q3rBhuwm4PMdBhVdiljeV5aQw0kUrBe_mziw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایش‌ ماهواره‌ای تردد از تنگهٔ هرمز
🔹
امروز نیروی دریایی سپاه از عبور ۲۶ فروند کشتی از تنگه هرمز با مجوز و هماهنگی سپاه پاسداران خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/farsna/436930" target="_blank">📅 22:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436929">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckyBnDXNqAh5j2SQXzsO1jQABRXdFY5lR8mqEeNq9qnrNB644WMKumQQS9wjHSF8a1Tjcjmze4LN0FWOMLR12nr-I2a1NRa4cozOvRPoqXBmpWrZRr1PxpJnHYcbINb2jbZp278usvxZgaVX2ZPGUu4kWDjNcl8PkKMEFcoLkF_dwHT2KFlhcYbYK14SBTNUqzDDmHClvIZTlCV4sbLrX88ZzyD5ziEBCnI_W1_GKAQOzdY52qQvMQ4zzWefM-cXr5vPyObt4wjpLJwMPsess3jt5RpKgCtO-bIqfHfRqDG6FUrNxZVH2o6goNNoQQ3FeNXRhm4JiBdihz7_m4xwBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف کامل دلار از مبادلات روسیه و چین
🔹
وزیر خارجهٔ روسیه: مسکو و پکن درحال حاضر معاملات خود را به‌طور کامل به روبل و یوان انجام می‌دهند.
🔹
ما در هر صورت به اهداف عملیات ویژه نظامی در اوکراین دست خواهیم یافت.
🔹
اگر واشنگتن آمادهٔ ازسرگیری گفت‌وگو باشد، ما برای مذاکرات دربارهٔ اوکراین آماده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/farsna/436929" target="_blank">📅 21:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436928">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35d20c0838.mp4?token=qM2ye7vSCofYAaHMtOk_TUeg1IbCX9tJCfQTkg7yDP2eU-qZY3SU07aWbnaFAhqM-WDibZzNt1Zvah4bA5NVRJmdg-GzC3lZkiudMO-cDQokN0v94r29Dwdw1eDDxyoHYUVJxyfI9FcZpz9SJK1cXzvMo-DJFGa-v182BLQ9cWZMcxaIC0WGgrJ4m-78WL7O8f71mpyVbJZacwAihEXMUZ0KIPXbyNrxvnAJjSZY5QHy4ceDHHYEaeVtdlxWz_WDAwV9X9QM2UACjfZBx94ZSOmjrSjqsWspxgt832pBM_TnX0RIo7mlmzyTROrV0PFhbL-h8OZ3aPcEtXLTqKDQpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35d20c0838.mp4?token=qM2ye7vSCofYAaHMtOk_TUeg1IbCX9tJCfQTkg7yDP2eU-qZY3SU07aWbnaFAhqM-WDibZzNt1Zvah4bA5NVRJmdg-GzC3lZkiudMO-cDQokN0v94r29Dwdw1eDDxyoHYUVJxyfI9FcZpz9SJK1cXzvMo-DJFGa-v182BLQ9cWZMcxaIC0WGgrJ4m-78WL7O8f71mpyVbJZacwAihEXMUZ0KIPXbyNrxvnAJjSZY5QHy4ceDHHYEaeVtdlxWz_WDAwV9X9QM2UACjfZBx94ZSOmjrSjqsWspxgt832pBM_TnX0RIo7mlmzyTROrV0PFhbL-h8OZ3aPcEtXLTqKDQpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیاتی از پرونده و حکم قصاص قاتل الهه حسین نژاد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/farsna/436928" target="_blank">📅 21:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436923">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ccd4d563e.mp4?token=bCrwRv8UK21CnrbAX0qcNV2PxBra173Rov5ggHhBYxJ-o5wz4GHMsj_sEkW53ef5ovEOBrUaVJNU4bkug18U9sgOwaMj8MznzkOM4xXUXFWnklTxgReFWDJMs7sjbywXy3pNIP0Wje9cm4oZGeF4vfMOAmzYiiv8mErmYs31N2bqIWWa5vNRBlQ9DWsx7Flrz3y9USPFjYyv5GmBG19kKqfUdUwsCSgMs3BC93c-ybnhEdAZP_WhJYb97WrIbSdOfTCNqK3HjFFKm6TLvE7tCmQb2QR1XkJtFe0h_iXr3xPEPK9YprojRHb0zaf_AymYCHD4Cxsbuze4phtQU7yPWovlkeJ6gD-MvjtVODg79R_Ew27djk7sT5Gz-LrrbfD8_f0PLoSrDj3HBUzzdVWQ8eNVkbTIqCtVsofX3v0oP5-rvlpfrbnRqU-My4dTQC0KlK-URN8Ei774y5qjhfXzqNlI91Xh62sWcwoBpGGDY7QUE8S3SXYhvo43F_JY3vvplIGYcaw-7k3lSiSN3wk7iWwwAkcqhe5jTE4LNS5q8bK2WC288wfbXb93iQVoAIrE7cGIYMKjyD2_s4Vji7xle4soIcD3h4V-z7MwndnGPb1PpuvVI0k4EnnMgRfPS4FEjYb_ks_0e0Re6Sjs0qrM5b3XHSzqVXiEtRoDqAUAESI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ccd4d563e.mp4?token=bCrwRv8UK21CnrbAX0qcNV2PxBra173Rov5ggHhBYxJ-o5wz4GHMsj_sEkW53ef5ovEOBrUaVJNU4bkug18U9sgOwaMj8MznzkOM4xXUXFWnklTxgReFWDJMs7sjbywXy3pNIP0Wje9cm4oZGeF4vfMOAmzYiiv8mErmYs31N2bqIWWa5vNRBlQ9DWsx7Flrz3y9USPFjYyv5GmBG19kKqfUdUwsCSgMs3BC93c-ybnhEdAZP_WhJYb97WrIbSdOfTCNqK3HjFFKm6TLvE7tCmQb2QR1XkJtFe0h_iXr3xPEPK9YprojRHb0zaf_AymYCHD4Cxsbuze4phtQU7yPWovlkeJ6gD-MvjtVODg79R_Ew27djk7sT5Gz-LrrbfD8_f0PLoSrDj3HBUzzdVWQ8eNVkbTIqCtVsofX3v0oP5-rvlpfrbnRqU-My4dTQC0KlK-URN8Ei774y5qjhfXzqNlI91Xh62sWcwoBpGGDY7QUE8S3SXYhvo43F_JY3vvplIGYcaw-7k3lSiSN3wk7iWwwAkcqhe5jTE4LNS5q8bK2WC288wfbXb93iQVoAIrE7cGIYMKjyD2_s4Vji7xle4soIcD3h4V-z7MwndnGPb1PpuvVI0k4EnnMgRfPS4FEjYb_ks_0e0Re6Sjs0qrM5b3XHSzqVXiEtRoDqAUAESI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفت‌وگوی تلفنی رهبر شهید انقلاب حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه با همسر شهید رئیسی، پس از حادثه سقوط بالگرد
@Farsna</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/farsna/436923" target="_blank">📅 21:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436922">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‌
🔴
حزب‌الله: مواضع توپخانه‌ای ارتش دشمن اسرائیلی در شهرهای یارون و بنت جبیل و تجمعی از خودروها و سربازان رژیم صهیونیستی در شهر دیر سوریان با حملات موشکی و پهپادی هدف قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/farsna/436922" target="_blank">📅 21:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436921">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b5494635.mp4?token=UIeNKSAL4rLauN03hnQnuvtUf_bMuZP3TSuFSs_ih6SmAfFvstJnuLjmx2_Rd3SQ2ZUjN31-_JK6VKa4Z-GtqWZaXT5ZQqhIHChueA-d3N7eWN5FYCXdNvyMa7ES-k0hsa-01uRjn1xUuZ4gmeI5qlzfyH_y5fyBOhs4xdS1w64RvpMmGGZiUpp7Ww8p7NteEpDl6x5-ji8mXQ8lfaDprY53H5yEbkIcb8OPljHBVnGtVlgDqeaffnGJK7VBy44qEnLE0N07fCNGWwvQcXBZTIDxR9WnzM2YrDZVd-2iyyE60fe1uq-YaLCRmVgFucz8__uvyI8MOPmyJ8SxBF4lYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b5494635.mp4?token=UIeNKSAL4rLauN03hnQnuvtUf_bMuZP3TSuFSs_ih6SmAfFvstJnuLjmx2_Rd3SQ2ZUjN31-_JK6VKa4Z-GtqWZaXT5ZQqhIHChueA-d3N7eWN5FYCXdNvyMa7ES-k0hsa-01uRjn1xUuZ4gmeI5qlzfyH_y5fyBOhs4xdS1w64RvpMmGGZiUpp7Ww8p7NteEpDl6x5-ji8mXQ8lfaDprY53H5yEbkIcb8OPljHBVnGtVlgDqeaffnGJK7VBy44qEnLE0N07fCNGWwvQcXBZTIDxR9WnzM2YrDZVd-2iyyE60fe1uq-YaLCRmVgFucz8__uvyI8MOPmyJ8SxBF4lYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سکوهای آنلاین معاملات مسکن روی قیمت خانه‌ها تاثیر می‌گذارند یا نه؟
@Farsna</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/farsna/436921" target="_blank">📅 21:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436914">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YlKYRt4bThcqETkdlNb32Sfk1m2WIMGidFbSl-lMTa5m2MLVf3TVa6lHmlgejnWbeiGKVTkF3tFY_5Hwc3j72z0x448D4Y1l8CxIYVMd8oYLnKMP3eZl3B13CPGrG_stsc80acDQNuRXkpNPlSgviKb4BwSApyPmd9IxhyPJWGTYJ_sVFmub9ELiEtPrc_TJ5dVKO5TzL_eNyuqQjBbGquLlCgXdTR9iYMSUwV85fouXULJSbLV4IiVXFqVqy4xHQPSfEJLX8420eLxLaUqyym5n_WXXBF3jPZy5R-m6aJIoak6lGg0TkF3HMmWHaPo2vzpr1YDURXKy5Yj0YrYIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hpXNBkoHadMpFCmoFs3ueJ_vWxxIGb1INBLIyBh2Rb1FJ-YM21RLVSpvEGo2YBetCe43dbOz5QgsebC6l0cFr44JrtTa8V6Ed8HbRLjr5y4jN_-AnPPn36xaKFFYxICtHiV7hWfh2QqyAP2gP5sDpj7KpxSx5iItpEitjjxkFvw2GUnciRFFqBuhchKkUqNi9TA1QCs3izYirijmvhGjVri-pydQiBpbgOV7YXV-K5Q2SW3fkx3f5tMRIjev8TWn7I6qAwO28Qyr3GIiUTlTMBC2178_xInHoMHuB1wbZUHDn-kNgLGSaVeoGYlr-7Ab3eB4K0JQB1fDZUjhC5dRAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DLNGJafR3n5ZebtrgmcTQ-9pDr0-9Rd0wdQdchiPqRG-OlRH26X5iECLb-shYt62qqiTgmcR-A-QZsVh6vCpvAxBKrbuzjx2JSbSPeMzUdG_2SsqSV7NDTjw_lb9SvV4vYpN4bqkaY0E4OkjU-Z2JUwIfsbzpWOtCtbT7VL-GaCZNJLlNjMpeAcZGIh0YOUwOAnxOgmUIZSY7dMznyyi37SLV6NWf3sAUpe5wlfQya0a-RLATzEQM_1TpVvQM6MRuPCcAhaFsDa0sfLH9M9rJc-RmNqEV62GlxNuTEQXhaUcxL8bH4v5dXHkNrJREr4huIP6It2UeIj_EtWCZcXzEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LPjVMbzB6SMIt4CW7Tbz8ddGMADMIF0q5VeRkxjDOWyIlcug2P6vDLCLLLBPRVTrN-aD6bQJh-418HRK1NCH4HhbdtUh1mpD66ZIpSshcA-I32G9l3jhurCAzs6LowxdGVofjK0zI5ZUmA2f8p5xWYM0qKPPw1VMshBwY3uQUUB4sJQz7p619rLapd_VfIDpKqOteUqzFHWZGSgvNK6Z6zhF4EEXe7cIaZYA4OE3ev3ihiHqyhOj8gy5m7DvWGk9W1uHOfA9CKCkJczBvOl9Lwd3RHSP60WP1wIJJ6xVfwzcj6EMM3omWzuBg4xnAcsMV1BdpEZezOJ5lJfJ2r3Dpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A9Vjdz60uQbQSr5lccvCn-jEdUjTf2Qdy8nI2DLr6lZ0NedoxaByDlBdoPUZrgEdxIXu-lm6UnPwqW7qeJOtc9uZ7RCx7X3pXQwklfR2owdyOA6gwQxxQsFL73mROne2ZVOcwBC2gWn2lbxyoyX-VMAz--8uUu0chcYnW83YQQl4iXv_H64p10P35Nipo0iMlq2kAe9ZUuP_RlBMjPU3hGdWsv4ThzJ6lA0aUKEFVyA-CxVYCDA53EgWNNCUMoMn4wbMAU7a-y6vkEtf5AwLcGlVrOlkZiQCQcIWIpVPFmbW833eEbGhSgvq0HYsmd825psQBFS1lkEM-r203aYExw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bCZZlMwOU_o9SNIsvrrjH1K7bs2lnFqHnWSvEZCMzxsWuK_JhTtfTJ3v_WCX0G-4RTbZVh-mMcvAjx9HdI8JCQyAFu8na_LuHFewSBfcQ_Q6T38IGn6mxf4z9OmEMguzkqOK-yj7kyLP1nQ-wEA7Rw1GyFbgigfqByVF2c4l9HZ06y9JoAXvX34jOYw2Kpzi23EhA2cy8ji7OwwzZZIagJTeUanORoMy05M6X4jjb6NUx7RRfIgXp2jynMgk46U2-y58bq3TX96yvoz5z-bW5c9zXpDG-q2hF7zDGGm2lLdxG1xr0GSyi3YXyoxhLJN8CPURhdWJcu5p48AKRc8zrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nP0JU9dbum0o3Y_HPBC64G2mvdLxY25XBHclNlEoJ8Mr5UpLUdQ_luoijSsUNaAgcw9fZyFLhbUHhxrtH0mtPSj7xehRY_R52zr5G45e9fYubbjg4QVNYv041Q92S6HmH6N3fELT8NDaA263X__TzT47xRAoTzF9PXQlPIg0D_ob2_cxkBLLgqWqflcFyrcJhlXXV9JUwMOxkxMIVwv280tL2O6yRP65Pr15RA0LCj3reOSjqNmAL2gOstee-t-2mAYU566b7FCUrNw_DoVGk5o3Wq-joGOn4BKGzEmWW6zTMvXggpwt3n-ymZn3oh6UFfxCmwLgf1khAU0MZSGm_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عقد زیر پرچم ایران
عکس:
سیدمهدی پناهی
@Farsna</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/farsna/436914" target="_blank">📅 21:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436913">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0ee278bd4.mp4?token=V5R0SZPcP300vdw4bIm287lp2ZrPZSPBgCFbidaeoGwted-KNXqrRTSKyPfpK7AyLQqGtSyXoPluO1Y2gYN1kTkXr5UN_9Sa6P4qlA23KCI9U5hHghhwjj-DGDIyZri2GiWD9CXCnGn6TrT658vQ8La4YUkHgFBQD07heV0zLFLTLc7dHjKza54V752c6OJCJk0oB8EHZG89cTbCOU9KFpB7lFZ9Seg9-gMyLjtacxKp0qDUXNZ-QBHp8U97kYgImrrvhZRluYrMJdpI_uDk_DlgPelAOFlx3dA8tlnxC13npLIJ9K9rb4EXPByHUc2xyQpEf5ETGd0koliq2zG4cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0ee278bd4.mp4?token=V5R0SZPcP300vdw4bIm287lp2ZrPZSPBgCFbidaeoGwted-KNXqrRTSKyPfpK7AyLQqGtSyXoPluO1Y2gYN1kTkXr5UN_9Sa6P4qlA23KCI9U5hHghhwjj-DGDIyZri2GiWD9CXCnGn6TrT658vQ8La4YUkHgFBQD07heV0zLFLTLc7dHjKza54V752c6OJCJk0oB8EHZG89cTbCOU9KFpB7lFZ9Seg9-gMyLjtacxKp0qDUXNZ-QBHp8U97kYgImrrvhZRluYrMJdpI_uDk_DlgPelAOFlx3dA8tlnxC13npLIJ9K9rb4EXPByHUc2xyQpEf5ETGd0koliq2zG4cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مولتن، عضو کنگرهٔ آمریکا: ما درحال باختن به ایران هستیم
🔸
مولتن خطاب به فرمانده سنتکام: برنامه فعلی‌تان برای پیروزی واقعی در این جنگ چیست؟ چون به نظر می‌رسد که ما درحال باختن هستیم؛ نه توافق هسته‌ای داریم، نه تنگهٔ هرمز باز است، و رئیس‌جمهور هم خواستار تسلیم…</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/farsna/436913" target="_blank">📅 21:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436912">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f35fdf8ca.mp4?token=boD4VkdrqhxKnXUYHsU8dfxs5RT79wDUmg46Nzdlkq3cuPh0FhZk_tijhmc1kc4NhMMgJW-_AH6xXNx41WInDyfodeygw06Uk_2e4a_v3qcdtxCh6h9U7bTkXGzbubEzN_U-XHrIPWjo4hhHXXlnT70Y_YGJSjz35w4n675B3qzhpCzIA1tY_a50ywlQ9GwXyAtMii7fojaqN59zkjKA7HWMxN27mFi3YYhRWleR3gAbO9t4VT4IRDzhcKsgXb3iNib4JrWGNI-1YnkK9Sdoj_brccXVKk8DzCqk0F_9AY_zk2cNVj4UvVcEVP3SNNTQWwwHmj5RwChD2iMlXfRd8HCiiagSIrPXRPFPXLNCJhs9l-Cex5PME8u63bB6e9yMd8IGh1LFRi_Yg2LMLUy8JTn0lINOqn8eL0eoRIsLsVcyxVvPwBDS6Z8mrkb6BA3M_WAAyMrvSWuHUFzVNOgDuj1bQG3DGFkjRpcQUI1fxkHJRnELo_pz0s8iWM6a6g5vdXBDrsDF2TBbRIh2halW3cLCwsxTleybwbEnu8ZqBzukqYzB-PLycrkCyYu47GN7p2VOEvgFuVcaVbd-NNAsdzGCzMhyWtmDOD2_G5jUGbFFXed6R02yTL2LV3oZcKvRtQrL4BHlI7UYN9MBylTy3Mz1hkHxWFsUu28ghhOWVmY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f35fdf8ca.mp4?token=boD4VkdrqhxKnXUYHsU8dfxs5RT79wDUmg46Nzdlkq3cuPh0FhZk_tijhmc1kc4NhMMgJW-_AH6xXNx41WInDyfodeygw06Uk_2e4a_v3qcdtxCh6h9U7bTkXGzbubEzN_U-XHrIPWjo4hhHXXlnT70Y_YGJSjz35w4n675B3qzhpCzIA1tY_a50ywlQ9GwXyAtMii7fojaqN59zkjKA7HWMxN27mFi3YYhRWleR3gAbO9t4VT4IRDzhcKsgXb3iNib4JrWGNI-1YnkK9Sdoj_brccXVKk8DzCqk0F_9AY_zk2cNVj4UvVcEVP3SNNTQWwwHmj5RwChD2iMlXfRd8HCiiagSIrPXRPFPXLNCJhs9l-Cex5PME8u63bB6e9yMd8IGh1LFRi_Yg2LMLUy8JTn0lINOqn8eL0eoRIsLsVcyxVvPwBDS6Z8mrkb6BA3M_WAAyMrvSWuHUFzVNOgDuj1bQG3DGFkjRpcQUI1fxkHJRnELo_pz0s8iWM6a6g5vdXBDrsDF2TBbRIh2halW3cLCwsxTleybwbEnu8ZqBzukqYzB-PLycrkCyYu47GN7p2VOEvgFuVcaVbd-NNAsdzGCzMhyWtmDOD2_G5jUGbFFXed6R02yTL2LV3oZcKvRtQrL4BHlI7UYN9MBylTy3Mz1hkHxWFsUu28ghhOWVmY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفت‌وگو با دختر چفیه‌قرمز که در میدان انقلاب معروف شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/farsna/436912" target="_blank">📅 21:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436911">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/527c36a23a.mp4?token=R3Re-6ZaYFPXI3WLpq7oSYhmFyP9MgWOEHr4oAoDtadw7Vsbm01KyFtUJ_re0A_ewvduvkj5eI9E1g1_XgnccFkCgmm_El8tRILm61VALS2rUOeAeu703XjuDJVpcMp0_OHaZ1yk3hZri1-q3MOBbAUg4H7n68QDHAtKi2cYtCL7a5_t9L8hAsGQJQCGnQTNb_3R6_AiWJluqc07Gf7K2wAuXnKgQQerLW8A7XINNd45DYOCpGUF3UwElsKz53ITpQnhyPMqRidEuM4XOCaSp194UV-ih_YOyTRph7TZeqGKvm48ilTqerBD2OIkUMbBuDwltrEheWHwSdGLoaZSv7pJaYOHxPCyNCQu9RZ2B6sIM7obPyNeJ9drPAMl-w-oDq9Xfm6qNxgBhDRubRm6NyFc-i8MAN5-jxmyGx9d27XUeI2whMVLAXVM1QsaBzf2N8EEhIGmDeNXw3-vZu4BK1RG4aM_bhmHmT236VkJHzizTFJf0YDjozdncgzqCXQEh5MS1CJpaNknROoAd70IdLHPZMbR4ZPPqheRI0shkt5TITOvnpvlT7UcBOGriuHmc7Q0rNULdeRWgafEN169vcWz-z3bDKjwFrZLDOdRrKmjRpVSOYBnLg3_AK2U_D6FRxVShCveoa6nC4HpZ2FYNObyFmmTDyXE6quhS6Kc8sE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/527c36a23a.mp4?token=R3Re-6ZaYFPXI3WLpq7oSYhmFyP9MgWOEHr4oAoDtadw7Vsbm01KyFtUJ_re0A_ewvduvkj5eI9E1g1_XgnccFkCgmm_El8tRILm61VALS2rUOeAeu703XjuDJVpcMp0_OHaZ1yk3hZri1-q3MOBbAUg4H7n68QDHAtKi2cYtCL7a5_t9L8hAsGQJQCGnQTNb_3R6_AiWJluqc07Gf7K2wAuXnKgQQerLW8A7XINNd45DYOCpGUF3UwElsKz53ITpQnhyPMqRidEuM4XOCaSp194UV-ih_YOyTRph7TZeqGKvm48ilTqerBD2OIkUMbBuDwltrEheWHwSdGLoaZSv7pJaYOHxPCyNCQu9RZ2B6sIM7obPyNeJ9drPAMl-w-oDq9Xfm6qNxgBhDRubRm6NyFc-i8MAN5-jxmyGx9d27XUeI2whMVLAXVM1QsaBzf2N8EEhIGmDeNXw3-vZu4BK1RG4aM_bhmHmT236VkJHzizTFJf0YDjozdncgzqCXQEh5MS1CJpaNknROoAd70IdLHPZMbR4ZPPqheRI0shkt5TITOvnpvlT7UcBOGriuHmc7Q0rNULdeRWgafEN169vcWz-z3bDKjwFrZLDOdRrKmjRpVSOYBnLg3_AK2U_D6FRxVShCveoa6nC4HpZ2FYNObyFmmTDyXE6quhS6Kc8sE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شاهرگ اقتصاد دیجیتال دنیا زیر تیغ ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/farsna/436911" target="_blank">📅 21:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436910">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d685e8dcc5.mp4?token=uQHoNP4iRKY02w9idqbWYPQffDSOUpZldQoMC3SdmeprV7jOWR3bj3TLFO2G3S-c4bAqc-If2aq4FfG4iD8Hrp0cwbA-e2o8rdruWyn5fr6VvrQIdgWbXw3BregN1D8J5NxfBYLABAW_EvcykJf6q65JOhX02XiwvgS0Ag13njkp15zmCLBd2VPUvcFMvMacHq7nf4hDTraLZ6-5M8N1G3vmshyNb5HnAb33Yh5-YWN1tq1K6Yw52NttpUE0RINEOtKWilJE3JTnqIBgOkGuEuA5HWnVvRQerYqxOp_R-KapJwF_X4pxu9hl7FdsLi4Y9hGkH0NeSrukuZG_uSL6aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d685e8dcc5.mp4?token=uQHoNP4iRKY02w9idqbWYPQffDSOUpZldQoMC3SdmeprV7jOWR3bj3TLFO2G3S-c4bAqc-If2aq4FfG4iD8Hrp0cwbA-e2o8rdruWyn5fr6VvrQIdgWbXw3BregN1D8J5NxfBYLABAW_EvcykJf6q65JOhX02XiwvgS0Ag13njkp15zmCLBd2VPUvcFMvMacHq7nf4hDTraLZ6-5M8N1G3vmshyNb5HnAb33Yh5-YWN1tq1K6Yw52NttpUE0RINEOtKWilJE3JTnqIBgOkGuEuA5HWnVvRQerYqxOp_R-KapJwF_X4pxu9hl7FdsLi4Y9hGkH0NeSrukuZG_uSL6aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دختر شهید رئیسی: هیچ سفر خارجی با پدرم نرفتم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/farsna/436910" target="_blank">📅 21:17 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436909">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2139c31a3e.mp4?token=WKMmmLBxbmtZI9zRDrFciHFdHLycPqNogmaAvi8f2kyftBEF_0lltwb0j-sdODpENlpLrEoNazHE07kT4LRBAFnGS5qhfrzg2AIKl4EVhP7biOHRZ1A22-vgZayJHUoXSImpbvWHBXr9veM92kHnje_EVBSRCOoetBTfHQnrdJ7p8wk76AeYf1CmwxE8rymMRNG4I2kk1wMzX8Y-hLMZETYw6qQBoEwTtKDH0SJ1jCp1M5iB8_yqXGqjceOK5K1pE3GhXebRQ1zWTVP5hzsf-XMcnAYwO4Zu69JV9pIScx9VUHm9TLtPuEY_7dLZktOMFAR-2kZIDA8bs_JjCz-qMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2139c31a3e.mp4?token=WKMmmLBxbmtZI9zRDrFciHFdHLycPqNogmaAvi8f2kyftBEF_0lltwb0j-sdODpENlpLrEoNazHE07kT4LRBAFnGS5qhfrzg2AIKl4EVhP7biOHRZ1A22-vgZayJHUoXSImpbvWHBXr9veM92kHnje_EVBSRCOoetBTfHQnrdJ7p8wk76AeYf1CmwxE8rymMRNG4I2kk1wMzX8Y-hLMZETYw6qQBoEwTtKDH0SJ1jCp1M5iB8_yqXGqjceOK5K1pE3GhXebRQ1zWTVP5hzsf-XMcnAYwO4Zu69JV9pIScx9VUHm9TLtPuEY_7dLZktOMFAR-2kZIDA8bs_JjCz-qMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو: در تهران هنوز بیش از ۳۷ درصد از نظر بارش‌ها عقب هستیم.
@Farsna</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/farsna/436909" target="_blank">📅 21:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436908">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b0109abff.mp4?token=oUBBYO0Wx7QGr4piR7P1BCFgE1SsnyZ5FtbAMbA3M7805JnN8d2vNKQTd6hCUarGXGi0GBF3csWtF3_ppefXXzIDUQ9xVjIp6V65ktommeHKRw-DI4pmlkP1kjlUDlzM0rXeaQhP5zq6bTcyhSr8FMt6eEOAD_tkI3mGe734rQhWoDDHMxZXTFDblk33RWZLNMFrxVIYjWtwRexO9tRAoAeKegOirPzvHDX6ItZe28pIXIDGblJNHfTx724i0YzjXInv6SHw-eb6mog8I6yOkaCzLTqc8RvzQnqmpKgE4SuykajsOxWZ1Lsc7rKZkoohQL65hp68FG7B3WyLxNTsaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b0109abff.mp4?token=oUBBYO0Wx7QGr4piR7P1BCFgE1SsnyZ5FtbAMbA3M7805JnN8d2vNKQTd6hCUarGXGi0GBF3csWtF3_ppefXXzIDUQ9xVjIp6V65ktommeHKRw-DI4pmlkP1kjlUDlzM0rXeaQhP5zq6bTcyhSr8FMt6eEOAD_tkI3mGe734rQhWoDDHMxZXTFDblk33RWZLNMFrxVIYjWtwRexO9tRAoAeKegOirPzvHDX6ItZe28pIXIDGblJNHfTx724i0YzjXInv6SHw-eb6mog8I6yOkaCzLTqc8RvzQnqmpKgE4SuykajsOxWZ1Lsc7rKZkoohQL65hp68FG7B3WyLxNTsaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گرامیداشت دومین سالگرد «شهیدِ جمهور» در حرم حضرت معصومه(س)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/farsna/436908" target="_blank">📅 21:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436907">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe088cec1b.mp4?token=Qv9O5OPiR7w6kHLXqN2vsfsj6PwGN5zdx0U9pkgKHt2jERCSdo12qrIpMfTvtugZDwWVDnSAuN3bIul-94rTptiKrVnDERIlZs02H7KXmnu_nBiZ2SFLp6a8ExnWF19r3nwiJvYroBfn5ALEXk2f50EE5sQUQ4AfTl3NxRLJUWtyV11_pCjeWdHoR4VOmobVwD0OGjbb0TxHBkZqJkEGRiCYC5IS8FfX2e1WFAa57HG88G1l3SX-bHVDktW7f0JeSj3pR5PD2s_2P7wbpK0PKCrvQGJyctht7qw8ug4c-wBHPi7aQlB21REuafRkVkNEK5-MekesChibYmBN0BJocA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe088cec1b.mp4?token=Qv9O5OPiR7w6kHLXqN2vsfsj6PwGN5zdx0U9pkgKHt2jERCSdo12qrIpMfTvtugZDwWVDnSAuN3bIul-94rTptiKrVnDERIlZs02H7KXmnu_nBiZ2SFLp6a8ExnWF19r3nwiJvYroBfn5ALEXk2f50EE5sQUQ4AfTl3NxRLJUWtyV11_pCjeWdHoR4VOmobVwD0OGjbb0TxHBkZqJkEGRiCYC5IS8FfX2e1WFAa57HG88G1l3SX-bHVDktW7f0JeSj3pR5PD2s_2P7wbpK0PKCrvQGJyctht7qw8ug4c-wBHPi7aQlB21REuafRkVkNEK5-MekesChibYmBN0BJocA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار وزیر کشور پاکستان با پزشکیان
@Faesna
-
Link</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/farsna/436907" target="_blank">📅 21:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436906">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🎥
مهاجم تیم ملی: انگیزه صعود داریم و آقای قلعه‌نویی می‌گوید باید ۲ مرحله صعود کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/farsna/436906" target="_blank">📅 20:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436905">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajUIj7zrob6A-XrVmSEKdzdnGoVlQkI426qHhlT_cQzAsTfi_SOG1S2slmY9-ChpIN3OBRs1gPjfB41xweBP_mWMPQ0G4Rd0O28gxe0E12KGjw9G_9O_CkCfv8Bn9m_PrqnXwNnR2A_Fg6A1P9Qsn9b0PjLlmtuxWMZRzAHqnZiuiQgNUUXmzABleApKhYTzSdW4pnCPk066oPfnu8cEmRzUM3gIXDduO5y0BW-BJCsaxDEXeGyc5FUxCrfWcgmZAmfXHEP-At0IHNpE8v56CoQbkhFH3D8cYZX7hogYqJdiidYH8Wo25Uk0kWcedg7mozbmvAwA7ZYR9YoH4kiABw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشای گستردۀ اطلاعات ‌فوق‌محرمانه دولت آمریکا
🔹
پژوهشگران امنیت سایبری از افشای گسترده اطلاعات محرمانه دولت آمریکا خبر داده‌اند؛ رخدادی که برخی آن را یکی از بدترین نشت‌های اطلاعاتی تاریخ دولت آمریکا توصیف کرده‌اند.
🔹
ماجرا از زمانی آغاز شد که «گیوم والدون» پژوهشگر امنیتی، متوجه یک مخزن عمومی در گیت‌هاب با نام «پرایوت-سیسا» شد؛ مخزنی که به‌صورت عمومی در دسترس بود و حاوی اطلاعات فوق‌العاده حساس مربوط به آژانس امنیت سایبری و امنیت زیرساخت آمریکا بود. این مخزن توسط پیمانکار دولتی «نایت‌وینگ» مدیریت می‌شد.
🔹
در میان فایل‌های افشاشده، کلیدهای مدیریتی سرویس ابری «ای‌دبلیو‌اس گاوکلاود»، توکن‌های دسترسی، نام‌های کاربری و رمزعبورهای داخلی، کلیدهای SSH و حتی فایل‌هایی حاوی اطلاعات ورود کارکنان دیده می‌شد. همچنین اطلاعات مربوط به سامانه‌های داخلی توسعه نرم‌افزار و زیرساخت‌های امنیتی دولت آمریکا نیز داخل این مخزن قرار داشت.
🔹
«والدون» در نامه‌ای اعلام کرد ابتدا تصور می‌کرد این داده‌ها جعلی هستند، چون حجم و حساسیت اطلاعات افشاشده غیرقابل‌باور به نظر می‌رسید. او این اتفاق را «بدترین نشت اطلاعاتی دوران کاری خود» توصیف کرد و گفت این مخزن حتی جزئیات نحوه ساخت و استقرار نرم‌افزارهای داخلی دولت آمریکا را هم آشکار می‌کرد.
🔹
پس از اطلاع‌رسانی پژوهشگران، مخزن گیت‌هاب قفل و از دسترس خارج شد و شرکت «نایت‌وینگ» نیز از اظهار نظر مستقیم خودداری کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/farsna/436905" target="_blank">📅 20:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436904">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41d3788cc5.mp4?token=iATidZOiHStD4H4dNIaCtVaJ9UDtFN3tDEGpEpvFdudDQKRKvkMrIALPDWCvOrmMbIIAFIb1FCgd1mMyrBkplXt7-PQ-nUTQsfOfx9_4whiSspRx0tzbsy3sT18PR0Yc0FEZWtLesc--u0c2sfi7IXcHMzE9QmWcQMecWEutpJLDeE1QkFGAl692c7YCfcXpHM1-DYtpUvO61wOZO9WDbCcF1L0cAqvcgptXTDPUFLvf45WW0aae1K4K9xsDSvl2pHiRelobsLTSN4US0q6q6Yyr0bKL1TT6QgWtPUVaeAwQGTYyihTit_4jGFfCsx2MCKh0VJK7VWLxFuU0Hxs0ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41d3788cc5.mp4?token=iATidZOiHStD4H4dNIaCtVaJ9UDtFN3tDEGpEpvFdudDQKRKvkMrIALPDWCvOrmMbIIAFIb1FCgd1mMyrBkplXt7-PQ-nUTQsfOfx9_4whiSspRx0tzbsy3sT18PR0Yc0FEZWtLesc--u0c2sfi7IXcHMzE9QmWcQMecWEutpJLDeE1QkFGAl692c7YCfcXpHM1-DYtpUvO61wOZO9WDbCcF1L0cAqvcgptXTDPUFLvf45WW0aae1K4K9xsDSvl2pHiRelobsLTSN4US0q6q6Yyr0bKL1TT6QgWtPUVaeAwQGTYyihTit_4jGFfCsx2MCKh0VJK7VWLxFuU0Hxs0ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای بنر رئیسی مرسی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/farsna/436904" target="_blank">📅 20:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436903">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258c32847c.mp4?token=rywiLfBC86-CuJtZeNVAoLZ6Rh9WIf7EtKVSev5QeCt1YBWCrLqzh9REq26F9_UhrDE5w79um2pQDpjIkiqGJuR29tbOoni7jKzwREiMB5ovylsJQb63FqNxE8tYY6NO5fKTs8m0jnAYmNlyXN2Je_YaMNbEYfDp4FiP05nk84tE4edq4rKnvx2rQ6aROC2j-bhc2KGCV3XUmO1vGJ1iNNQ-RI4ulZ3gtf7duDGQNbOAHIQNhIw7QzQ2YTMgbDdjgajS_JuGs6eNIikmeL0JBEpi82uZA0Bo7kBPm6vl5xpPck0YZNv1Tkkrn2CAKMWOrjhc7eeTrO7yBhfpcTQLFoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258c32847c.mp4?token=rywiLfBC86-CuJtZeNVAoLZ6Rh9WIf7EtKVSev5QeCt1YBWCrLqzh9REq26F9_UhrDE5w79um2pQDpjIkiqGJuR29tbOoni7jKzwREiMB5ovylsJQb63FqNxE8tYY6NO5fKTs8m0jnAYmNlyXN2Je_YaMNbEYfDp4FiP05nk84tE4edq4rKnvx2rQ6aROC2j-bhc2KGCV3XUmO1vGJ1iNNQ-RI4ulZ3gtf7duDGQNbOAHIQNhIw7QzQ2YTMgbDdjgajS_JuGs6eNIikmeL0JBEpi82uZA0Bo7kBPm6vl5xpPck0YZNv1Tkkrn2CAKMWOrjhc7eeTrO7yBhfpcTQLFoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلتنگی پسر برای پدر پهپادسوار آسمانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/farsna/436903" target="_blank">📅 20:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436901">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‌ سخنگوی وزارت خارجه: نسبت به موضوع حاکمیت ایران بر تنگه هرمز تاکید داریم
🔹
قاعدتا هزینه تامین امنیت دریانوردی تنگه هرمز نیز باید پرداخت شود.
🔹
طبق حقوق بین‌الملل مجاز هستیم که تنگه هرمز را برای کشورهایی که آن‌ها را برای خود تهدید می‌دانیم باز نکنیم. @Farsna</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/farsna/436901" target="_blank">📅 20:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436900">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حنظله: در صورت خطای دشمنان به شبکه‌های دیجیتال و انرژی آنها حمله می‌کنیم
🔹
گروه هکری حنظله: در صورت ارتکاب هرگونه تجاوز یا بی‌مبالاتی از سوی آمریکا و رژیم صهیونیستی، حملات سایبری ویرانگر فراملیتی علیه زیرساخت‌های انرژی و دیجیتال کشورهای خصم اجرا خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/farsna/436900" target="_blank">📅 20:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436899">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‌ بقائی: ما با سوءظن و حسن‌نیت به تبادل پیام می‌پردازیم
🔹
صحبت‌کردن از اولتیماتوم و ضرب‌الاجل دربارۀ ایران مضحک است. @Farsna</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/farsna/436899" target="_blank">📅 20:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436898">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4420d08a0c.mp4?token=E4pm8s32csuYzXGom1y64kbDmaJVxovKLvKWnELz0Yi_WOe5hfilka8QDA9vaiqpBo2NNYKP4-eincoDv4zTCUp0N2468-LW-QX9pPh4vsM_ep_eSrH28lrFmtcL7P-fd-FL9BHdF2h2p34UauruW5Kf4nx7Ls9-2v7G8nqIOpUl8RKNyXNcHA8YeoMK8ttk1GMONlZKY03ilWh2_avp99lstkEu7ZSTfhyX8_jyageMrNCITkPCz89wITUH7kDKWm8hd6YsS1whlvZXZ0_1IbHcw1LlyjqhBMczLA-Qqfn1QMVp-52RjI6OW--9rassbEd8MARY4ZAg-EH319mamA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4420d08a0c.mp4?token=E4pm8s32csuYzXGom1y64kbDmaJVxovKLvKWnELz0Yi_WOe5hfilka8QDA9vaiqpBo2NNYKP4-eincoDv4zTCUp0N2468-LW-QX9pPh4vsM_ep_eSrH28lrFmtcL7P-fd-FL9BHdF2h2p34UauruW5Kf4nx7Ls9-2v7G8nqIOpUl8RKNyXNcHA8YeoMK8ttk1GMONlZKY03ilWh2_avp99lstkEu7ZSTfhyX8_jyageMrNCITkPCz89wITUH7kDKWm8hd6YsS1whlvZXZ0_1IbHcw1LlyjqhBMczLA-Qqfn1QMVp-52RjI6OW--9rassbEd8MARY4ZAg-EH319mamA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما اسم فرزند آینده‌تون که قراره به ایران جان تازه بده چی می‌ذارید؟
🔹
خیلی‌ها توی پویش «جان ایران» شرکت کردند از جوان‌هایی که ذوق فرزنددارشدن دارن تا پدر و مادرهایی که اسم بچه آینده‌شون رو انتخاب کردن.
🔹
شما هم می‌تونید نام فرزند عزیزتون که قراره به ایران جان بده رو به شماره ۳۰۰۰۱۴۱۳ پیامک کنید.
@Farsna</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/farsna/436898" target="_blank">📅 20:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436897">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tW24Ibmqt29DtvFHtZtLVYJ1hwS97mYt7TJ0jpeSHM6fFpT-rd-uPUPjSVh6pdlU7aTS9N_mpC39GbNj4FIaL3ucUueG4uBTO09QEiKwwY2Y3GMGva7oSSsSfkWfGu_rJ96CZOT2nFXNxn_1lDd4p1cFn_7yAIZOir5OPHltuiCuCX-0xaTaEktIw0btiFVHpaPY8tFEE4BvT-2cKmh-JtUsuDqJOld2CtnsZuJwk6vZmIb3ZKMDaiPXqGKuCXT3CcuPCmHUzysEdnFbrToZec7CXPrk7y2wpqz5rsUWjhjoeVZ9FmA7e7fAqZsUWvhqdAnZRDrFsG8Ydq-zOqcaMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با هفته جمعیت، پویش ملی «جان ایران» با رونمایی از بیلبوردهای شهری، پیام تازه‌ای از امید و آینده را به تصویر کشید
🔹
کمپینی که هر تولد را نه فقط آغاز یک زندگی، بلکه ادامه تپشِ ایران می‌داند.
@Farsna</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/farsna/436897" target="_blank">📅 20:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436896">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_RnPYD13nVT7hy5Uzm1LS3htkshiO19xlM2UpBk-yjarrI-bWJCG_VnT7hvP9KKe4XBA6pE-2uZ9DUy7LRGywY00Vv3IO0l0T0PamcnLv0N3jDCPbq70_IObeEM6rNYolSYPXObai3yRioBybYU9NTHB4SURWrNXKXVTSI5lLR2Xd476T1Dp4tsWbGyNJVibaZb-Xh_iaWxHAfF-ACr2br29uf_l9w6-94T7AUdXA2x6Zcx4LI_PZ6GxsnCU7xfyiIpnq75ENc1Gh3kHNOeLDpnFAMo4NzPCnal7zxhFHhsMjatkJXS1xBSGHp95ERb_tTPd22Tat_yz648zQgWnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با سالروز شهادت شهید سید ابراهیم رئیسی طرحی از شهدای پرواز اردیبهشت در کنار رهبرشهید انقلاب برروی دیوارنگاره میدان انقلاب تهران اکران شد.
@Farsna</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/farsna/436896" target="_blank">📅 20:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436895">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZhNJv8jTlRyHSHVn5h6xXDjIdXc5dpl-prwu7Gv-kgo9i-p21dYUanOTarFMaD2Qs-pxNCXo0EalvfNVC-jfmV6MowWOom_p9qwJdJCMQ9aqwHmyFWJizdudCVXOgnlZIg2ahX7h6WCx5fu0AErnsl0ve74ZmQYu4WzlytHfBOQJD0pMeon21eLi_l1x5xctyMsZR2KZw82p0zAB4Q1GXufCoL-rHQvz1ZD_3EaOV8HSxjtJSB6TcYVlgEad36ARme0yOAs0icvsCrRZ7gchPVEr-Mp-6sWzQ0HPsmzI96D4fdU_kijB4dynS0K9UJBbaP-ENEAfG41O1SvGZB-9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">*
🌐
ثبت‌نام خودروهای وارداتی با حساب وکالتی بانک رفاه کارگران*
🔹️
مشتریان بانک رفاه کارگران می‌توانند به صورت غیرحضوری و یا از طریق مراجعه به شعب این بانک، نسبت به وکالتی کردن حساب‌های خود اقدام و در طرح فروش خودروهای وارداتی شرکت مگفا شرکت کنند.
🔹️
مشتریان متقاضی خرید محصولات این شرکت تا پایان روز پنج‌شنبه 31 اردیبهشت ماه سال جاری فرصت دارند با مراجعه به سامانه محور (
https://mehvar.rb24.ir
) یا مراجعه حضوری به شعب این بانک در سراسر کشور (با رعایت حداقل مانده حساب ۵ میلیارد ریال)، نسبت به وکالتی کردن حساب‌های خود اقدام و در این طرح شرکت کنند.
🔹️
استفاده از سامانه‌های فرا رفاه و رفاه‌پلاس موبایل بانک رفاه و سایت بانک رفاه کارگران، دیگر روش‌های غیرحضوری است که مشتریان این بانک می‌توانند از طریق آنها نسبت به وکالتی کردن حساب‌های خود و شرکت در این طرح اقدام کنند.
@bankrefahkargaran
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/farsna/436895" target="_blank">📅 20:17 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436894">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/farsna/436894" target="_blank">📅 20:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436893">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: تبادل پیام‌ها بین طرف ایرانی و آمریکایی براساس متن ۱۴بندی ایران ادامه دارد.
🔹
حضور وزیر کشور پاکستان برای تسهیل مبادلۀ پیام‌هاست. @Farsna</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/farsna/436893" target="_blank">📅 20:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436892">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: تبادل پیام‌ها بین طرف ایرانی و آمریکایی براساس متن ۱۴بندی ایران ادامه دارد.
🔹
حضور وزیر کشور پاکستان برای تسهیل مبادلۀ پیام‌هاست.
@Farsna</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/farsna/436892" target="_blank">📅 20:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436891">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4893f2908.mp4?token=SJJZ2SiPnrrE42pl3OM_nDTy6JdjxFslldklbPqgL8eo9V-G6tiAl0UxDJbxpPiBAoQPc7u3OCzaX3KqgyC4cYW6A_8GePeDuzIP9mOe-XWVj_TMvVMh6WVj4cRnyhBAhAKlve7HW-JL-lrd8CB6yi9V0t3Sf4cLjE64fzbFV8bBBdBMfmvHxpQhALnHmD4wK2ZZbxxp0XkEAgebNvli9kVt6sRRQXtOYGisw24bfiotE8tm9v92i4yrwR2nlt6LLHvcriqm4qR4BckWT8d09j8P20iAgngtUk7OdLfV8a-ztN0slNyc2PHv6TWk35IzqSE27C8TIOA7QapxFGCuWT07LCFze4-T2LxSK9YarKtrcwTvwLkvmlwg51jIqA7VAynzziZO8GGCDHy-vA265iExv3cI7PdRSfl9dl1fs0YtwNfBp_6IpfmRmzbAPVdCW9pRcyl9KDwKtt3zlXO5ITyAYBSOgMmVVfBADuQgz8ssXoilviiERzslXOZjjQGNcH33GidyJsdQ6YLtKaFy32ZeJIAQsaN0G3QeWvuoiGeOARtMmdc6J_mnN9gRyvSSxNTwM2NdlBW7qqP5AHiHjbIy-4EiW48fnPFhKxIvKUqFARdAZY-9bFLzo10smPWjhTvdAeSuRswhgM0W4dL9mfDWaSN91_ts7y0mwMLiYFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4893f2908.mp4?token=SJJZ2SiPnrrE42pl3OM_nDTy6JdjxFslldklbPqgL8eo9V-G6tiAl0UxDJbxpPiBAoQPc7u3OCzaX3KqgyC4cYW6A_8GePeDuzIP9mOe-XWVj_TMvVMh6WVj4cRnyhBAhAKlve7HW-JL-lrd8CB6yi9V0t3Sf4cLjE64fzbFV8bBBdBMfmvHxpQhALnHmD4wK2ZZbxxp0XkEAgebNvli9kVt6sRRQXtOYGisw24bfiotE8tm9v92i4yrwR2nlt6LLHvcriqm4qR4BckWT8d09j8P20iAgngtUk7OdLfV8a-ztN0slNyc2PHv6TWk35IzqSE27C8TIOA7QapxFGCuWT07LCFze4-T2LxSK9YarKtrcwTvwLkvmlwg51jIqA7VAynzziZO8GGCDHy-vA265iExv3cI7PdRSfl9dl1fs0YtwNfBp_6IpfmRmzbAPVdCW9pRcyl9KDwKtt3zlXO5ITyAYBSOgMmVVfBADuQgz8ssXoilviiERzslXOZjjQGNcH33GidyJsdQ6YLtKaFy32ZeJIAQsaN0G3QeWvuoiGeOARtMmdc6J_mnN9gRyvSSxNTwM2NdlBW7qqP5AHiHjbIy-4EiW48fnPFhKxIvKUqFARdAZY-9bFLzo10smPWjhTvdAeSuRswhgM0W4dL9mfDWaSN91_ts7y0mwMLiYFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان مگر جای ازدواج است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/farsna/436891" target="_blank">📅 19:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436890">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‌
🔴
حزب‌الله: یک تانک مرکاوا در شهر الطیبه را با یک حملهٔ انتحاری هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/farsna/436890" target="_blank">📅 19:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436889">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04c242af4.mp4?token=GJXSBQh_lAoFsafSoXEDuxfdb7x531jlUluKP18_fuPiVDQ4Foc49zUNKVU0QbMN86cn_sCJ7TCQNOvme-Kz3dv5ntdGvMyAa5rKgKzdys-Ds-ThH-yZNv3vO1pdAT5QKb2N5HBiJkdfyk0LBykiripvyD0wDm91bDwAQ0hC9eyk99Nqr95BGWuyLh9LJIyAz-WW4Y5Xi3ySX5MQf-nFspet_eFCOaENDxpSSm9kyiGxj1E9C8qnuF6OayWIgyDzEFSL11tejJBQJY2XpQbgeg8EBE3xDGlW6W4wnd8u8qXK7cJMIrauC27SIZATO2S2PdBo-04011fpBt5anstmgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04c242af4.mp4?token=GJXSBQh_lAoFsafSoXEDuxfdb7x531jlUluKP18_fuPiVDQ4Foc49zUNKVU0QbMN86cn_sCJ7TCQNOvme-Kz3dv5ntdGvMyAa5rKgKzdys-Ds-ThH-yZNv3vO1pdAT5QKb2N5HBiJkdfyk0LBykiripvyD0wDm91bDwAQ0hC9eyk99Nqr95BGWuyLh9LJIyAz-WW4Y5Xi3ySX5MQf-nFspet_eFCOaENDxpSSm9kyiGxj1E9C8qnuF6OayWIgyDzEFSL11tejJBQJY2XpQbgeg8EBE3xDGlW6W4wnd8u8qXK7cJMIrauC27SIZATO2S2PdBo-04011fpBt5anstmgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: شهید رئیسی تا سرحد توان برای خدمت به مردم تلاش می‌کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farsna/436889" target="_blank">📅 19:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436888">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb30e93732.mp4?token=ahWavFSjIAH7Iaql36oIrL--sjc-aYdx7dbN4CjMtc1tdC-vL_VkyOexXTlGiszXcFYxceVPb_nh75LMPj04LEVpEST_SSKswlFm4x4Mk8mmO0CM06n7sCWKERGa8kwcuhOgEtb2Emxfg3UHUOgTYwlU7f9t2Qqj4IvpYvJe4tYGmIoBC6MFOQCBcWxXNobVncs-b04OrbyGTU-Uvdq-zWN0VvQ4gv4HxaPx_ANr5rvh1ZpIkHU3enKMvAbRdyqkAI9lq0nrm11fP8sPXIeeaXS1yoKWGZLxfOPYPiX0QLr6VlixA0Xdafdi-_0uwnM6SQp4Irlx4C3IkJx87rf2JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb30e93732.mp4?token=ahWavFSjIAH7Iaql36oIrL--sjc-aYdx7dbN4CjMtc1tdC-vL_VkyOexXTlGiszXcFYxceVPb_nh75LMPj04LEVpEST_SSKswlFm4x4Mk8mmO0CM06n7sCWKERGa8kwcuhOgEtb2Emxfg3UHUOgTYwlU7f9t2Qqj4IvpYvJe4tYGmIoBC6MFOQCBcWxXNobVncs-b04OrbyGTU-Uvdq-zWN0VvQ4gv4HxaPx_ANr5rvh1ZpIkHU3enKMvAbRdyqkAI9lq0nrm11fP8sPXIeeaXS1yoKWGZLxfOPYPiX0QLr6VlixA0Xdafdi-_0uwnM6SQp4Irlx4C3IkJx87rf2JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط جنگنده پاکستانی
🔹
یک هواپیمای آموزشی نیروی هوایی پاکستان امروز در جریان یک عملیات آموزشی در ایالت پنجاپ سقوط کرد.
🔹
هر ۲ خلبان قبل از برخورد هواپیما به زمین با موفقیت از هواپیما خارج شدند.
@Farsna</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/farsna/436888" target="_blank">📅 19:49 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436887">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f1cb3975a.mp4?token=p58G8Mcq7QMUkVbeINvqVjYEdCjFQVoEEqv7m0uV0YyfXdt9FZcqzO8QZcKHhjcplSkzSvYEY7a9MHK1MfytTNhPcS1EATSwQd6ql6uppk-c4RE6CybTOgpJ8-Eo7usw6XA2_GE68CU4eMwf66BXqHVfDmMm1S2gbWMh1LX36q6Syw9QFon7uLOV1FQ-mpafyFrMR0v8x14rZT7Lz__8Hpjr9DpcQAYD5qqAabSVf6W70eOoSa5Ge28p51-rAvhIkggvi_WoYXH6DjDlSf6G8HiE313Po599UaQ7Y1OP9nkH0BCIL9Cs4pdahnA1jJTiGhGwfXlZNsesTYBAx4bnzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f1cb3975a.mp4?token=p58G8Mcq7QMUkVbeINvqVjYEdCjFQVoEEqv7m0uV0YyfXdt9FZcqzO8QZcKHhjcplSkzSvYEY7a9MHK1MfytTNhPcS1EATSwQd6ql6uppk-c4RE6CybTOgpJ8-Eo7usw6XA2_GE68CU4eMwf66BXqHVfDmMm1S2gbWMh1LX36q6Syw9QFon7uLOV1FQ-mpafyFrMR0v8x14rZT7Lz__8Hpjr9DpcQAYD5qqAabSVf6W70eOoSa5Ge28p51-rAvhIkggvi_WoYXH6DjDlSf6G8HiE313Po599UaQ7Y1OP9nkH0BCIL9Cs4pdahnA1jJTiGhGwfXlZNsesTYBAx4bnzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گوشه‌هایی از تمرین بدنی ملی‌پوشان
@Sportfars</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/farsna/436887" target="_blank">📅 19:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436886">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شهادت یک پلیس در سراوانِ سیستان‌وبلوچستان
🔹
پلیس سیستان‌وبلوچستان: ساعتی پیش، سرنشینان مسلح یک دستگاه خودروی سواری به سمت خادمان امنیت در یکی از جاده‌های شهرستان سراوان تیراندازی کردند که متأسفانه ستوان سوم امیرحسین شهرکی به شهادت رسید.
🔹
اشرار مسلح تحت تعقیب پلیس هستند و در منطقه طرح امنیتی-انتظامی درحال اجراست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/farsna/436886" target="_blank">📅 19:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436885">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🎥
حملهٔ وزیر امنیت داخلی رژیم صهیونیستی به اعضای دستگیرشدهٔ ناوگان صمود  @Farsna</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farsna/436885" target="_blank">📅 19:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436884">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcmKEjh1lKxslzyqoIN_cHPrCwOvaq9rpfeRyUSQcQcTYRUQOJbUDpN4sERl-sTZr5IHpce4TcrDKFheW7_8uP5D9Tu-O7szOkmaAeB8yn1e_uBAhH2_903b0bhqv8UsrTcOywK_ytw6TzbCgGDVwal-YZ851aF8v0j56cw5rXgPnBhrHTq3Ibl5KkKQhSpp-DLaH2osIRziE2BwMcJnkW-c9DfzLshEnFgZfZryf8-gncphAi8ntbJUTUrdSTOc5UHxw3KvllcuYPCeRmIi0H7WYhbLZio4zq9FTmnBPYGSDXVy1BPdmexhZlAfeEkpoDD7-wPWQgRvz9LiDp4Mnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خنثی‌سازی بیش از ۸۵۰ مهمات در هرمزگان
🔹
سپاه هرمزگان: طی انجام بیش ۲۵۰ مورد عملیات خنثی‌سازی و انهدام، بیش از ۶۰۰ عدد بمبلت را که در جریان بمباران‌های هوایی جنگنده‌های متخاصم و با هدف آلوده‌سازی برخی مکان‌های حساس و مهم استان به‌صورت مین‌ریزی هوایی و با استفاده از بمب‌های خوشه‌ای در چند نقطه پراکنده شده بود، کشف و خنثی شد.
🔹
همچنین در این عملیات‌ها، انواع موشک‌های کروز از جمله مدل‌های GASSM و تاماهاوک و نیز موشک‌های پرتابی از جنگنده‌ها مانند GBU و BLU که در اثر اصابت به برخی مکان‌های حساس عمل نکرده یا دچار نقص عملکرد و انفجار ناقص شده بودند، شناسایی و خنثی‌سازی شدند.
🔹
در بخش دیگری از این اقدامات، بیش از ۱۲۵ فروند انواع پرنده انتحاری شامل اوربیتر، هاروپ و لوکاس کشف و خنثی شد.
🔹
علاوه بر این، بسیاری از اقلام و تجهیزات الکترونیکی که توسط دشمن برای اهداف مختلف در دریا و خشکی رها شده بود نیز توسط نیروهای متخصص شناسایی و جمع‌آوری شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farsna/436884" target="_blank">📅 19:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436883">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‌
🔴
وزیر امورخارجهٔ فرانسه از احضار سفیر رژیم صهیونیستی به وزارت امورخارجهٔ این کشور خبر داد.
🔹
بارو با اشاره به رفتار وزیر امنیت رژیم صهیونیست با اعضای کاروان صمود گفت: اقدامات بن‌گویر در قبال سرنشینان کاروان جهانی صمود غیرقابل قبول است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/436883" target="_blank">📅 19:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436882">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68fb73b61e.mp4?token=argcVmRz6LnUuAtWqI2h0p_F4e_pGUFiSSmWXT4PvroZV5m-qSVlzATKYkfcRUfC5jtVCGji5ktHbSxn0FuKZJSGMnFJSFH8yW-Ah7aMXsrNTcaZdpomvuiZfu4oMLZe94oNYahNE7KnHzQl8GpzCyCGsug9MqKpEljNayWvDWQGeEYikhjR2BQruLHaJj7AufNK0XDLYkGkfvVKsLVT65k4ywZMyUSkzjRML-bHZh_9iVgeLiAv0JdnOZ_C3W6MqsT2YxqQUtm3zM1lBBJhUtde_tmdtBQqli7MCHKfbHmG4IgmyYOy2jbz_qTVD3zji2CtIFwBTrRrcJpIa-a7kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68fb73b61e.mp4?token=argcVmRz6LnUuAtWqI2h0p_F4e_pGUFiSSmWXT4PvroZV5m-qSVlzATKYkfcRUfC5jtVCGji5ktHbSxn0FuKZJSGMnFJSFH8yW-Ah7aMXsrNTcaZdpomvuiZfu4oMLZe94oNYahNE7KnHzQl8GpzCyCGsug9MqKpEljNayWvDWQGeEYikhjR2BQruLHaJj7AufNK0XDLYkGkfvVKsLVT65k4ywZMyUSkzjRML-bHZh_9iVgeLiAv0JdnOZ_C3W6MqsT2YxqQUtm3zM1lBBJhUtde_tmdtBQqli7MCHKfbHmG4IgmyYOy2jbz_qTVD3zji2CtIFwBTrRrcJpIa-a7kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ به‌دنبال نخست‌وزیری در اسرائیل
🔹
رئیس‌جمهور آمریکا: من الان ۹۹٪ در اسرائیل محبوبیت دارم؛ پس شاید بعد از انجام این کار، به اسرائیل رفته و برای نخست‌وزیری نامزد شوم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/farsna/436882" target="_blank">📅 19:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436881">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpLHFS4ZisjfSPS-ufLAFgQRf6N8AtjjayBckt6TAiRUJiiS84DazXeRcATUXKrDF-5R_Yfv-gHHmjTHHP0EXbNZN4FzgA687dIWsvgsBGj0_rGd49D81F3n-wrbHa11nmvLDZuygBPcXP8BsQu6g7bJRrQySUF5pnZRNK5nB47n0jBA1D5jV0SkHByIzwsaqP6RAX9gsYbHpAxtP1i6gzaztM4BxHDnpm4lGuLHbrsmSeeQI3hPk38-6QwcIDui4WPAYvy3myNHUjhA5lrnGSVbZkm47ZtldxGRunut6hi1UIaWBgAgiz7jl4_qQz5g3sEhl3_wPzkhhzaw5Fc7xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادر فولاد کشور به یک بانک دولتی فروخته شد
🔹
رئیس هیئت‌مدیرۀ انجمن تولیدکنندگان فولاد: با تصمیم وزارت کار، ذوب‌آهن اصفهان به بانک رفاه واگذار شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/436881" target="_blank">📅 18:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436880">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKbC6ekJfvDPwzGdnLaim4OfWPvfyWH3InSY6hO_SCLab8whtJtMGmc2sT1g7-Vc4IcuGdsRyeXdJVLRl3SMqMqINIhgRRYD60tEJggiCoG6TIPM2HcVCz5Fs8b-kQAfGZafUYme4CYmUvIz2wPWvWGVs9fxZxWW4jkmBNRLOyBsaktLwgC29TqtlYYFWm-TpNIHXujlpaFp2_EUuESEHuO5WoStBvE4fgGja8YQC92Kdo0buJV-u2HxXMkPih-PlvIE7rrhiZUS7KAp7q5dv7SdnpZqEEaAtuInvxpfehBfLH4p7dDmZ7F2gwB0l5G7Ij8OAU2ikf8OrdGjb-D0ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز فروش بلیط قطار اردبیل-مشهد از امروز
🔹
استاندار اردبیل: با آماده‌سازی ایستگاه‌ها و انجام اقدامات نهایی، راه‌آهن اردبیل در اختیار مردم قرار گرفت و بلیط‌فروشی اولین سفر ریلی به مشهد از امروز آغاز شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/436880" target="_blank">📅 18:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436879">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‌  ایتالیا سفیر اسرائیل را احضار کرد
🔹
ایتالیا در واکنش به توقیف ناوگان جهانی صمود و آنچه «برخورد غیرقابل‌قبول» اسرائیل با فعالان صلح‌طلب خواند، سفیر این رژیم را برای ارائهٔ توضیحات رسمی احضار کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/436879" target="_blank">📅 18:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436878">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNJLGUl8q03yzy4RN4Aim1vriHlNXLvsJg0QxrYTrW6hi3EMVJH7ptC3wl9nQGnWmCI2McTWrGCMjzKLoTs0lkXzh9XfHHFRTQ54bGXEEzHgTFmIZkevJ8mlAaDKw7j5S0810gOe4LC7ETU5TyVSlBMc9ApwI9YaZmkUUIL81A1z9X5CcSj5_MuKW3ZOF0ED7VBK4PbnNaaLhKb8ASuQo5Eu0Es8hWUn1q2j2Xo_0Th5EmLgrFj3ZL1LT5rjxCufU2eKvfz5yoKLgtnfg8aOCRcFSBscSn5obd4SW7xJHkOO5PGk5HlrNu7wtLgVYKrCV_2dF0Y7mwk17SK_NOQk3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت بنزین در آمریکا باز رکورد زد
🔹
به گزارش انجمن خودروی آمریکا، میانگین قیمت بنزین در ۷ ایالت آمریکا از مرز ۵ دلار برای هر گالن عبور کرده است؛ موضوعی که نشان‌دهندهٔ تداوم فشارهای تورمی و افزایش هزینه‌های انرژی در ایالات متحده است.
🔹
انجمن خودرو آمریکا ۲ روز پیش اعلام‌کرده بود میانگین قیمت بنزین در ایالات متحده به ۴.۵۵ دلار به ازای هر گالن رسیده است و در برخی ایالت‌ها این رقم از ۶ دلار هم فراتر رفته است.
🔹
بر اساس داده‌های منتشر شده، کالیفرنیا با ۶.۱۶ دلار، واشنگتن با ۵.۷۰ دلار و اورگن با ۵.۳۰ دلار گران‌ترین ایالت‌های آمریکا هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/436878" target="_blank">📅 18:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436877">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ct4QISMywCn7bss64deXpwpmCJAwbvB4HMj-xyOccLjQ99FFfzWtZmowadpb1GOfpmVor99M-7x2DRCpkJrozTcBApfG7kPUQ0P3fYkQBi8WldgxtkwJ-kTuco1e4cHNs-QSGcATOYfokqaWFEKV2LgaLIyfDsELLM_WpibHMtd11MnjTmCU7ql399F6VhUfbtnrPOUcgGjfs75HYFrwMlV4fQyY_eqlLvStSsSYUFNHOYmKxAqtOiVPAzvm6rFxIfvONJYCS-1W4oydW-gBE0eVfXjwEwojyD7OiqKPhGLq_NZ1IH7ImJ4mKkLUNlQkT3BG2__l62QIp4cwNE6dzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع عبری: فرمانده اسرائیلی در حملۀ حزب‌الله به‌شدت مجروح شده است
🔹
مایر بیدرمن، فرماندهٔ تیپ زرهی ۴۰۱، در جریان انفجار یک پهپاد انتحاری در لبنان به شدت زخمی شده است. یک افسر نیز به‌طور متوسط زخمی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/farsna/436877" target="_blank">📅 18:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436876">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyNV5AX170R3Mv3gCAUUnTy_bQGBU5G3-kBvui2uSky_wJ8mJWucaUOyNjtvo1-oA4KzOEVOcbPlkbFkDYwuSkgsaRbB0RdhkrGTLHAzNcFufPQ7csCUXtgpN206nbpIxNSD_7vKWpiSj9TAir1FkLE1LOcjEZbxxCPwGmBH3DqoFyqO5rCM11J_oK2kJMmAyqBAkBDTLdXnNWHEaLlZxeMQvPiJFZ_1P4cECnHim4TsOI2SC6VcPUyhiDrQfy5ve3fnXUACcVD-wPCbMqiMjdVPwy7teyf0V1GFvrUV3NvbGXx0oOOSl7BtJWZ7d40ENC9qfmFlvU_1U-So0CIETg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ بازهم عقب‌نشینی کرد
🔹
ترامپ: حمله نظامی به ایران که برای فردا برنامه‌ریزی شده بود را به درخواست ولی‌عهد عربستان سعودی، رئیس امارات و امیر قطر متوقف کردم. @Farsna</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/436876" target="_blank">📅 18:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436875">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-41.pdf</div>
  <div class="tg-doc-extra">3.3 MB</div>
</div>
<a href="https://t.me/farsna/436875" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📎
دستِ پُر به میدان بروید
🔹
اگر برای اجتماعات انقلابی به‌دنبال شعر، شعار یا تک‌بیت‌های روز هستید، ویژه‌نامهٔ «خط» پاسخگوی نیاز شماست.
@Farsna</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/436875" target="_blank">📅 18:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436874">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d045ee94bb.mp4?token=g4KrLwVnIqDmjxSr3IhYPklIXcgj8mPcIQ8wSDUt8_lDRj3tLJbgkui95q7Em52lc83XiWIKgMzVVrregLKD50onnnbLPU90Keu6dGmkFVfdehdiK4-yVF8IuKqvKY6m2Ucbx7bBQE4erkHYGU5oIbSjRw17kdITnCecp1QOMX4kl79oMPtmYlSqKt_ONbV2_HCtqIyS1fHDgKY87g5sl5OmwL5y_T3MXaJa9peVnc6cuilzwxhBhCeqa8MvarK5s5aoXDRUfnf1LuncAC_dBdlnu198L_mZYpWTtXQtG_M4umQRZ6TxWUzP0kyZd3-dYjKeRopeObLlFctrgIUpt6tk0Wg-1ai4P8YlC1Dy1BEqR7lk7vehYsHjzjj87Jhz5bqHeURk4f2_0_bzHOdY1iytjekvXHvA_1TEHmNNa5yH0s6uhzvdImu01IokydkjeQL-GLVVqFROLuP2jxnNtdOlnwcN2WKTrUXPDknBFFxhvUcOUsU5hUke5J5gcSZAB8lgfOjARwNTeI-7xeZdaStdymQrHSvQjVJNeE98Tv1oWXQedEnOuejmXYqmdymBhtztFxefPnj9yrH6P-eudJvYNVin43EFVDpPcu-bfqJ4Nnn6eyHHm7lCbkH1ef6jVzNGFPFLfUPbCElnMTKSgzrMqjRYkjk2j-ImwLsvHj0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d045ee94bb.mp4?token=g4KrLwVnIqDmjxSr3IhYPklIXcgj8mPcIQ8wSDUt8_lDRj3tLJbgkui95q7Em52lc83XiWIKgMzVVrregLKD50onnnbLPU90Keu6dGmkFVfdehdiK4-yVF8IuKqvKY6m2Ucbx7bBQE4erkHYGU5oIbSjRw17kdITnCecp1QOMX4kl79oMPtmYlSqKt_ONbV2_HCtqIyS1fHDgKY87g5sl5OmwL5y_T3MXaJa9peVnc6cuilzwxhBhCeqa8MvarK5s5aoXDRUfnf1LuncAC_dBdlnu198L_mZYpWTtXQtG_M4umQRZ6TxWUzP0kyZd3-dYjKeRopeObLlFctrgIUpt6tk0Wg-1ai4P8YlC1Dy1BEqR7lk7vehYsHjzjj87Jhz5bqHeURk4f2_0_bzHOdY1iytjekvXHvA_1TEHmNNa5yH0s6uhzvdImu01IokydkjeQL-GLVVqFROLuP2jxnNtdOlnwcN2WKTrUXPDknBFFxhvUcOUsU5hUke5J5gcSZAB8lgfOjARwNTeI-7xeZdaStdymQrHSvQjVJNeE98Tv1oWXQedEnOuejmXYqmdymBhtztFxefPnj9yrH6P-eudJvYNVin43EFVDpPcu-bfqJ4Nnn6eyHHm7lCbkH1ef6jVzNGFPFLfUPbCElnMTKSgzrMqjRYkjk2j-ImwLsvHj0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جان مرشایمر: تنها راه پایان جنگ، توافق است اما ترامپ حاضر نیست تن به پذیرش پیروزی ایران بدهد
.
@Farsna</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/436874" target="_blank">📅 17:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436871">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQ4o1sUvFIxWlBIe9Zl866IcmWEBeRKgtBaTbYwDEFFf-zeZAWQsu38ezMC6UL6ELthVpIX9npJsO9PX2-3Qi59Sgv-lWVOukJJ4npP1y8GPcf8z3Ro0bryqE81GhnLAr5JcbyrWFWHakTbMAhh8B_NR-tcFd3YQApSqLWSDKhzlKMfS25bWW6JlZTClMItoQjiLUyoKwicvAqYWlUfVyv7SlGzX4BMH9ygi-iA11Dx6VzMN-XzzGgzZTrrqUdwaD5i6thlnAoB0T0aVqp0R9oU8SnC8bE3t3j1RVUS2u-OMegqfLGqlzRsgNIfAePB_F5RYk9-1b5f2VvGFA2yuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: راه شهید رئیسی، چراغِ خدمت در میدان نبرد پیچیدۀ امروز است
🔹
بیانیه سپاه پاسداران در گرامیداشت دومین سالروز شهادت رئیس‌جمهور شهید: آیت الله رئیسی نمونه کامل «عالم عامل» و «مدیر متعهدی» بود که مدیریت را امانتی الهی و مسئولیت را پلی برای خدمت می‌دانست؛ او در اوج مسئولیت، ساده‌زیست، متواضع و در میان مردم نفس می‌کشید.
🔹
امروز که دشمنان انقلاب با تمام توان در میدان نبرد نامتقارن و جنگ شناختی علیه ملت ایران صف‌آرایی کرده‌اند، بازخوانی سیره شهید رئیسی - که تصمیماتش را بر پایه تکلیف، عقلانیت، صداقت و توکل اتخاذ می‌کرد - یک ضرورت راهبردی به ویژه برای کارگزاران و مدیران کشور است.
🔹
خادم الرضا شهید رئیسی، در سخت‌ترین شرایط با مجاهدت‌های صادقانه و بی‌منت در متن مردم، امید را در جان جامعه زنده نگه می داشت و در نگاهش پیشرفت نه یک شعار که مسیری روشن برای عزت ملی و شکوفه‌هایی استعدادهای این سرزمین بود، او با برافراشته نگه داشتن پرچم مسئولیت پذیری، باور به راهبرد "ما می‌توانیم"، را سرمایه گران بهای کشور برای استمرار حرکت انقلاب و پیش برندگی توقف ناپذیر "ایران قوی" به سمت آرمان‌های تمدن ساز و ناکام سازی راهبردها و سیاست‌های اهریمنی و ضد ایرانی دشمنان علیه این سرزمین قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/436871" target="_blank">📅 17:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436870">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiSFL2t-xaUAe3IidXCgVKD8GG3LPjIOV5bD0mDoVEtsNLqXX8USWGZjiWs9I6FJIQjCCx5GPDZZeEoBQQc-1xV3Ws0QKfhkoAGOiDpXp5JEMlH-tHEpFqlmfTuRcU87AJARh2yk55FvAR48RXuYTx3HDYbM9lL0s9_ydGKHDfOtGomwiSx6Wg5naUEM7i6jty1mIlooMbE70_FfqdS8Z8KMScQYTHrSYxOBSjBs1vK-e9tljflHpbA4a0-fAI8SOEn_YmPLYglwIuSahpTcV3uAOdHj-Dhvz-21rzg76aKjopAscQbw7iQ9WR3WZWpncdmbnH6GNUAQS6s1lDEgbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار انجمن اسقاط درباره تخلف در شماره‌گذاری خودروهای نو
🔹
نایب‌رئیس انجمن صنفی مراکز اسقاط خودروهای فرسوده: طبق قانون مقرر شده است در ازای از رده خارج‌شدن یک خودروی فرسوده، ۴ خودروی جدید شماره‌گذاری شود.
🔹
شواهد نشان می‌دهد درحال‌حاضر این عدد به ۱۲ خودرو افزایش یافته که مصداق بارز تخلف از قانون‌گذار است.
🔹
علت اصلی این کاهش، با وجود قوانین به‌روز، نداشتن یک آئین‌نامه مصرح و صحیح است که موجب شده سیاست‌گذاری‌ها در این حوزه به درستی اجرا نشود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farsna/436870" target="_blank">📅 17:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436869">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38474ee2e6.mp4?token=UE9PfvPTO4X6b_R93Kpita3YG9Fc7TduOr9XFlFiUvEQXru_nU26FERjj7AER8KF3oA35dGXWM6U1FheuX4c0YvI-bqS3KrjP-HPwNqiXrbNscgzqpUjE_CDpN6XpCVlKxggSPpja9iWyJ31_o3pKj-oPKs6TdeD7VWkT6R_GKowpU2JQcPpo8YlahDFREYeCtrqHntAgdAM9QdLhRhlv3QFUlYdkUj_9LUOsZ4TGF18W-GXo2KfImWULmD3Y4i7AuoQNDObhJ_Tf3rA5_x_c0gZ3x8s4V28y-OFMPrXBNd0YVHEQyQ3EEG291RZLZ4ApH8emEzTBT4q9yzZ-HfarA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38474ee2e6.mp4?token=UE9PfvPTO4X6b_R93Kpita3YG9Fc7TduOr9XFlFiUvEQXru_nU26FERjj7AER8KF3oA35dGXWM6U1FheuX4c0YvI-bqS3KrjP-HPwNqiXrbNscgzqpUjE_CDpN6XpCVlKxggSPpja9iWyJ31_o3pKj-oPKs6TdeD7VWkT6R_GKowpU2JQcPpo8YlahDFREYeCtrqHntAgdAM9QdLhRhlv3QFUlYdkUj_9LUOsZ4TGF18W-GXo2KfImWULmD3Y4i7AuoQNDObhJ_Tf3rA5_x_c0gZ3x8s4V28y-OFMPrXBNd0YVHEQyQ3EEG291RZLZ4ApH8emEzTBT4q9yzZ-HfarA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیال‌بافی ترامپ در مورد ایران ادامه دارد
🔹
ترامپ: ما کنترل ونزوئلا را به دست گرفتیم، اساساً کنترل ایران را هم به دست گرفتیم! ما آن‌ها را تارومار کرده‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/436869" target="_blank">📅 17:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436868">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1112f38c2a.mp4?token=swx1RBasR7tx4VRv0_iKqskg-_ugEpfXAlZOSIcAWsYj97JLvQWjrZdVLYlBpzSmquKiLFH-u8Jk59qzMRgkmtXU2-m4h9P_iJGkgWHHHKZj7KZwDRvTocV37UGzwOgCkTAm2CYvhMe2Avcx-tFjZ5ygkwXh_0RAy3Y3FNC4YJSaGH6IF1b9ofokzCOaaexvY9usNXozUyqrG8cVJ4-SFndSeAAVwHp4nnnzCVEfOv5X7fbRTdRq4GRtEsJnzfRhAYaf-55OOPa5G-4W0O2jJJWe8T1GeShP55gqgRU3zArGrWtcGfwlnpeIwq19OmwPJMS-DU0Hvjoebo688kZuVWf4ocrB6EgiASAcRj5_yMqpLFsU43ZTc5wQn6MN8Rp_avcuj9Lxa-0TJTvjsUeQaPTvnaaMKcS2LZMGzkHYTfRl8K5Ty8bXurVucSr9-ukv_Be0F6QVURa5Z1fZIU5jZYg2ofvw73Yc93sKKJyNY5zMtcv6aO_UTT_3fUXMAkzw8WNyFAWZOCPpiuge_gWHAVmPTkci9dNlXi9upPlC0UY5tOJKvJyfTmsPBOpoCUfJ2j7VY62b2mf2Y0j6JljHqusy1G7w-DZ4lBbi5UE9WKaSBof64iIn74c8T6mPMmsxETwzkoQ_Mv_vd7Mqjf2hvglp90ipZXY9rzkKDX3fOKs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1112f38c2a.mp4?token=swx1RBasR7tx4VRv0_iKqskg-_ugEpfXAlZOSIcAWsYj97JLvQWjrZdVLYlBpzSmquKiLFH-u8Jk59qzMRgkmtXU2-m4h9P_iJGkgWHHHKZj7KZwDRvTocV37UGzwOgCkTAm2CYvhMe2Avcx-tFjZ5ygkwXh_0RAy3Y3FNC4YJSaGH6IF1b9ofokzCOaaexvY9usNXozUyqrG8cVJ4-SFndSeAAVwHp4nnnzCVEfOv5X7fbRTdRq4GRtEsJnzfRhAYaf-55OOPa5G-4W0O2jJJWe8T1GeShP55gqgRU3zArGrWtcGfwlnpeIwq19OmwPJMS-DU0Hvjoebo688kZuVWf4ocrB6EgiASAcRj5_yMqpLFsU43ZTc5wQn6MN8Rp_avcuj9Lxa-0TJTvjsUeQaPTvnaaMKcS2LZMGzkHYTfRl8K5Ty8bXurVucSr9-ukv_Be0F6QVURa5Z1fZIU5jZYg2ofvw73Yc93sKKJyNY5zMtcv6aO_UTT_3fUXMAkzw8WNyFAWZOCPpiuge_gWHAVmPTkci9dNlXi9upPlC0UY5tOJKvJyfTmsPBOpoCUfJ2j7VY62b2mf2Y0j6JljHqusy1G7w-DZ4lBbi5UE9WKaSBof64iIn74c8T6mPMmsxETwzkoQ_Mv_vd7Mqjf2hvglp90ipZXY9rzkKDX3fOKs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: نتانیاهو هر کاری من بخواهم انجام می‌دهد
🔹
دونالد ترامپ، رئیس‌جمهور آمریکا امروز چهارشنبه تلاش‌ کرد به انتقادهایی که او را بابت راه‌اندازی جنگ علیه ایران بنا به خواست اسرائیل مورد سرزنش قرار می‌دهند پاسخ دهد.
🔹
او گفت: «نتانیاهو کارهایی که من بخواهم…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/436868" target="_blank">📅 17:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436867">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izEyyi2Vti-W1z_QK6SHzPyZFysQc246ZdzLpaIgKjV4lqivzjyaJJKcCAybgMEdluWLqwMVb89NgpiDIGGdogDhQzTPX6Wi3r-HFAwI5WXx2NOQn9zyo1FNSa5hEPCsS-vSeecnIO7KesnC9g67gBBC_ZuHSA-aX2nMDDIDS__shZW0llX3WAID0XAWF5iWA6WrHJw3rdUGd6woW7YA5bbavZKT2l4B-d9mq4mFi7M2H1BCy3txXbi3hl36JpULuSU5bbxuKdzsu5MLIwP6atinEc5N8mKq2CMtzZiuvqhweTeJIWJBQtrulZL_CJAtu3DE5dm43sH4MODUyZRRsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: نتانیاهو هر کاری من بخواهم انجام می‌دهد
🔹
دونالد ترامپ، رئیس‌جمهور آمریکا امروز چهارشنبه تلاش‌ کرد به انتقادهایی که او را بابت راه‌اندازی جنگ علیه ایران بنا به خواست اسرائیل مورد سرزنش قرار می‌دهند پاسخ دهد.
🔹
او گفت: «نتانیاهو کارهایی که من بخواهم را انجام خواهد داد.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/farsna/436867" target="_blank">📅 17:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436866">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rxbs8aN3-vW6h7qWS1RZlklbxE2BbMDv61Nk_aKystE-4CNmg__c5Gg1C1TqIjNowo7o1qBGX_wD5ZRaoRKKMcqA938dVKsGMogybhM8Bq7R9wmWv-UQXDFRAUjTaYx9yTtL8i9KtyZw4AFbSVJWOiz1ei2TbxRXaEJ0qd-bjsad-mnoi4c_Jsv5AILcPZtRqsRdaDecgJVopOXP6mziPEhpqvKKifuHT1bqePLfK-LbInphGYpcNV3hm2Pj8gE00LfTvcyQ7jvN_CNyq6X9ruVynwxnJvMYTCVqGmz5Z19Rddb6Fbj9B0bJA6Sx7cpxCiWLRA2ohAdLy-Qq9mDWaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استعفای مقام ارشد اطلاعاتی دولت ترامپ به‌دلیل مخالفت با جنگ ایران
🔹
واشنگتن‌پست: آماریلیس فاکس کندی، یکی از مقامات ارشد اطلاعاتی دولت ترامپ و متحد تولسی گابارد، مدیر اطلاعات ملی، این هفته از ۲ سمت کلیدی دولتی کناره‌گیری می‌کند.
🔹
خروج آماریلیس فاکس کندی به‌گفتۀ یک منبع، تا حدی به‌دلیل مخالفت او با اقدام نظامی ترامپ در ایران بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farsna/436866" target="_blank">📅 17:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436865">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌
🔴
قالیباف: در شرایط جنگ اقتصادی روش‌های عادی کافی نیستند و وزارتخانه‌های اقتصادی باید با روش‌های خلاقانه دنبال حل مشکلات باشند. @Farsna</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/436865" target="_blank">📅 17:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436864">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌
🔴
قالیباف: متاسفانه برخی با انگیزه‌های سیاسی و به بهانۀ گرانی‌ها بدون درنظر گرفتن واقعیت‌ها، انگشت اتهام را فقط به سوی دولت یا رئیس‌جمهور می‌گیرند.
🔸
برخی انتقادها از دولت به‌گونه‌ای است که گویی جنگی اتفاق نیفتاده است.
🔸
من منکر برخی ضعف‌های مدیریتی نیستم…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/farsna/436864" target="_blank">📅 17:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436863">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‌
🔴
قالیباف: مردم انتظار دارند همه مسئولان هم‌راستا با بعثت اعجازگونۀ مردم برای حل مشکلات معیشتی به صورت جهادی تلاش کنند. @Farsna</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/436863" target="_blank">📅 17:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436862">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌
🔴
قالیباف: از جهش قیمت‌ها و بالا رفتن هزینه‌های زندگی مردم اطلاع دارم
🔹
دشمن تصور می‌کند اگر زندگی مردم سخت‌تر شود، انسجام ملی تضعیف می‌شود اما مردم ثابت کردند که هم‌چنان در میدان مبارزه با دشمن حضور دارند و انتظار دارند که مسئولان مشکلات را حل کنند.  @Farsna</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/436862" target="_blank">📅 17:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436861">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‌
🔴
قالیباف: دشمن هنوز نفهمیده که ملت ایران در هر شرایطی در برابر زور سر خم نمی‌کند. @Farsna</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farsna/436861" target="_blank">📅 17:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436860">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‌
🔴
قالیباف: باید با تقویت آمادگی برای پاسخ موثر به حملات احتمالی و همچنین با افزایش تاب‌آوری اقتصادی، دشمن را از خطای محاسباتی بیرون بیاوریم و ناامیدش کنیم. @Farsna</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farsna/436860" target="_blank">📅 17:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436859">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌
🔴
قالیباف: دشمن هنوز به تسلیم‌شدن ملت ایران امیدوار است و به غلط فکر می‌کند می‌تواند با تداوم محاصره و ازسرگیری جنگ ایران را مجاب کند که به زیاده‌خواهی آمریکا پاسخ مثبت دهد. @Farsna</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/436859" target="_blank">📅 17:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436858">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‌
🔴
قالیباف: دشمن را از تعرض مجدد به ایران پشیمان خواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/farsna/436858" target="_blank">📅 16:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436857">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‌
🔴
قالیباف: مردم اطمینان داشته باشند نیروهای نظامی ما از فرصت آتش‌بس به بهترین شکل برای بازسازی توان خود استفاده کردند. @Farsna</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/436857" target="_blank">📅 16:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436856">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
قالیباف: تحرکات آشکار و پنهان دشمن نشان می‌دهد که به‌دنبال دور جدید جنگ است.  @Farsna</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/farsna/436856" target="_blank">📅 16:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436855">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
قالیباف: تحرکات آشکار و پنهان دشمن نشان می‌دهد که به‌دنبال دور جدید جنگ است.
@Farsna</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/436855" target="_blank">📅 16:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436854">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/783ffb553a.mp4?token=MGlHCVqZYYh3uUs86vY8Tm_YpPTJ9wZtNr8lk4g-3FBFeEY6wrXceS4kMbUUg7m5D-qAJ4ZfiitezIyz1OEAJFFsTHX6QO1xBjurGz526YxpYs5pXSyHpk8q-Bf7BOKSV0tuGIydGllqDBQLOIhCXSPnSbqYfIzR8ihqyHje8iluGSp5DzVpeYqkPK1QRYCl1rz1xd8VNNz2PjXR-8pkZisN2TzjboHztqqB7ncudnXxRPfo56mCAHqWf2en6mTUBWLEcgryQl8DrGPN7xgfSjMNiOnXlCTj61bIMadqbZJCqqpBljZXQ9oHxsqb6N33o4jtA1j5K2BmDTigupj1MFc3gVqDB7yy6OhWhkszkHBP78azZEsAQUQRxqVxaPfqV-zp7SYfGGshnNrBlscc0al-ilNe3vshVTCqz2GUndpHKKrMzQHURYUoHirAaSIry-uZcqs1PZ-w6bxu63Us1rH7nYlbPCVGvPDFmJhdI_QArhm8wp1x4DvhTJC5B1JcwHYD6P5hIt4TOzf_71hI8X3RHCkcOnn-xIr60ze4TqUg5953BiQICvBMXgnVl0Z0VEiabpEYDcML82xBub8Nj-TRv-XFQR7GbbyTr1-VmOU-iisQcIYddGoNVF-ulJxqOJ6zhfWZ39HPMf4BpEJOWjwbZVMcOoaFyexe7SyawfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/783ffb553a.mp4?token=MGlHCVqZYYh3uUs86vY8Tm_YpPTJ9wZtNr8lk4g-3FBFeEY6wrXceS4kMbUUg7m5D-qAJ4ZfiitezIyz1OEAJFFsTHX6QO1xBjurGz526YxpYs5pXSyHpk8q-Bf7BOKSV0tuGIydGllqDBQLOIhCXSPnSbqYfIzR8ihqyHje8iluGSp5DzVpeYqkPK1QRYCl1rz1xd8VNNz2PjXR-8pkZisN2TzjboHztqqB7ncudnXxRPfo56mCAHqWf2en6mTUBWLEcgryQl8DrGPN7xgfSjMNiOnXlCTj61bIMadqbZJCqqpBljZXQ9oHxsqb6N33o4jtA1j5K2BmDTigupj1MFc3gVqDB7yy6OhWhkszkHBP78azZEsAQUQRxqVxaPfqV-zp7SYfGGshnNrBlscc0al-ilNe3vshVTCqz2GUndpHKKrMzQHURYUoHirAaSIry-uZcqs1PZ-w6bxu63Us1rH7nYlbPCVGvPDFmJhdI_QArhm8wp1x4DvhTJC5B1JcwHYD6P5hIt4TOzf_71hI8X3RHCkcOnn-xIr60ze4TqUg5953BiQICvBMXgnVl0Z0VEiabpEYDcML82xBub8Nj-TRv-XFQR7GbbyTr1-VmOU-iisQcIYddGoNVF-ulJxqOJ6zhfWZ39HPMf4BpEJOWjwbZVMcOoaFyexe7SyawfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: بیشترین آمار وزیر شهید، مربوط به وزارت خارجه است
🔹
همۀ مدیران وزارت خارجه در زمان جنگ در محل کارشان حاضر بودند. دشمن خیلی تلاش کرد اما حتی یک مورد پناهندگی در هیچ‌یک از نمایندگی‌هایمان نداشتیم و حتی یک دیپلمات هم محل کارش را ترک نکرد. @Farsna</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/436854" target="_blank">📅 16:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436853">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9abe99cec4.mp4?token=S2c3yyqEVCGBLMDdsBBS4uJuKG2ReQFngy9KZVD17gTzbsXV8XUtzBxfZqyObitLPu9_vZigDpYzGuk1UbMXAuY6daniL6lZbbmmrJ-0T0oYk4i01oPq6A51nBMc93CDYVlslnGUAEYZsQe0v5DPbEAdhxbUPyyi6V0QrMlHKA9YPBEezIt_Z5dWscALFW0XrXMIu6wKS9cCeDqAPGev7g6EtUIqHou5TqEcLnugXX0ErkPNcXjKGWD0TEZHAoWE6SBXfEcJ1rCtpXzzsXNFA3DdAidOMdNDE2Rhf4StYI_9FXjufqMuzF2HIrRD4KL7JssgpSk-tFn7esmd4TsOtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9abe99cec4.mp4?token=S2c3yyqEVCGBLMDdsBBS4uJuKG2ReQFngy9KZVD17gTzbsXV8XUtzBxfZqyObitLPu9_vZigDpYzGuk1UbMXAuY6daniL6lZbbmmrJ-0T0oYk4i01oPq6A51nBMc93CDYVlslnGUAEYZsQe0v5DPbEAdhxbUPyyi6V0QrMlHKA9YPBEezIt_Z5dWscALFW0XrXMIu6wKS9cCeDqAPGev7g6EtUIqHou5TqEcLnugXX0ErkPNcXjKGWD0TEZHAoWE6SBXfEcJ1rCtpXzzsXNFA3DdAidOMdNDE2Rhf4StYI_9FXjufqMuzF2HIrRD4KL7JssgpSk-tFn7esmd4TsOtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: وزارت خارجه با فرماندهان نظامی هماهنگ است
🔹
دیپلمات‌های کشور در صورت تغییر نقش، با همان صلابت پشت لانچرهای دفاعی قرار می‌گیرند و نیروهای نظامی نیز در صورت اقتضا، با همان اقتدار پشت میز مذاکره خواهند نشست؛ چراکه تمامی نهادها هدفی مشترک را در یک مسیر…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/farsna/436853" target="_blank">📅 16:51 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436852">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQnME-4JR7oNZMDmfLziUIpUj1jf6qPLyU8mK0kNyjAyc06aypcmuZnTxWFZLlwN3LxaOeUsHLNWeDgnyqff2In1dkzadrtIjUPoUqlN2-meJ5vEM4NRLQoQ9YlARHrM4Lo_rqQn9x3qmI_f7eV-T1jkBThDsBxgCh0y2iZk8Y_NtQ1i2-SjxYbW4Ruhiq72tUJrRb1u42WvhJy3N3dMqq981UK7d3L_5X_-Y9CfzGu8gFC1WC_EnX6f_oKl8s7NHwzVBVd-0yFYatyTX7LTcNlW_ry24D8Gbo5oilcW3OM42tYBGt3tq_U1yqbRhtw4ezHbin_eMG9fg24MtIWbxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: آمریکا دوباره در جنگی بی‌پایان که در آن امکان پیروزی ندارد گیر خواهد افتاد
🔹
رئیس مجلس در صفحهٔ خود عبارتی از فصل ۱۱ کتاب خاطرات ونس، معاون رئیس‌جمهور آمریکا نقل کرد: «ما احساس می‌کردیم در دو جنگ بی‌پایان و بدون امکان برد گیر افتاده‌ایم و سهم نامتناسبی از سربازان از محله خودمان (محله فقرا) آمده بود.»
🔹
قالیباف در ادامه نوشت: این وضعیت (گیر افتادن آمریکا در جنگی که نمی‌توانند ببرند) دوباره درحال تکرارشدن است. این‌بار فقرا و فراموش‌شدگان آمریکایی باید هزینهٔ جنگ‌افروزی الیگارش‌های نزدیک به کاخ سفید، افراد شیطان‌صفتی همچون جیمی دیمون و لابی تاجران جنگ در واشینگتن را بپردازند.
🔸
گفتنی است جیمی دیمون، مدیرعامل موسسه مالی و بانک جی‌پی مورگان، در آمریکا و از مهم‌ترین چهره‌های حلقهٔ تامین‌کنندگان مالی جنگ آمریکا با ایران است که به‌تازگی نیز علیه ایران لفاظی کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farsna/436852" target="_blank">📅 16:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436851">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUmrsOgwpM6GxPD6SGwSiHNawkxkmRESgA63ZB8Lk55or7A1ePuB6fMPjDD6I1hZQL3GGoWBa9n3bwLmfAL3ZKyUgPpy24GrVob8yaR0VuUp08VPOk_dg8Ln8PfVl5Sg4BbomBgMk8B0AbaVzLBw972Bil-7dLRRG6DDMpJokjkXDTk2ixEX87WIvDMAo1N5nP37JdEkNUR9wdvW53onR8EHrX9x3zpiZ1EaplItzA6fnPeMrstRWRrvn5hYI3JHiOKBz31iEJRb1HOz8vE_8C1WV7JriQZ5_jMV1VKZASj9d5ceH871gyQHsoKSadKPUbV3bZ2geR7LuNF6KVwRmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور انتشارات فارس در نمایشگاه مجازی کتاب تهران
🔹
انتشارات خبرگزاری فارس با کتاب‌هایی با موضوعات رسانه، علوم شناختی، هوش مصنوعی و سیاست خارجی در هفتمین نمایشگاه مجازی کتاب حضور دارد.
🔹
کتاب‌ها را می‌توانید آنلاین از
صفحهٔ نمایشگاه
تهیه کنید.
🔹
ضمناً، علاقه‌مندان می‌توانند کتاب‌ها به‌صورت حضوری در «خیابان انقلاب، روبه‌روی دانشگاه تهران» با همان تخفیف‌ها تهیه کنند و از آثار ۷۰ ناشر حوزه رسانه نیز بازدید نمایند.
@Farsna</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/farsna/436851" target="_blank">📅 16:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436850">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kadhEgyh3XUktXiJ3kUoCz_PZLgAhp7DtAVV1iX3ZBZsSnC4FrTSHdI9_z7xRawswbnxNFkQIOzgSP1m4bF39u5ch9orn1YlHHv0T0rEmMYHiHxX_rTU5AVtARV9a3yEuXX49rXQW2zw4ccFZckPFEnnv3Yitwc7tQnsL60B6p5dt2bBeMzpQ4n72YDCeUiA0slqNYJlPHheEhJx_lzpK8F9ukCm4qjHJ6DFNQcc-4j_k70Wi3Pf7Xx1wGsYEsJDJPq78vPY5KY9yBH2cYDFSBwTyYW3axUdDYXGwkUMIJf0RvERvCzBkN9txzzbS6ktjMiXxCAClXa8prH0BYi1cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هتل‌های خالی آمریکا در جام‌جهانی
🔹
انجمن هتل‌ها و اقامتگاه‌های آمریکا (AHLA): ۷۰درصد از اتاق‌های رزرو شده در بوستون، دالاس، لس‌آنجلس، فیلادلفیا و سیاتل لغو شده‌اند.
🔹
طبق گزارش‌های منتشر شده در ماه گذشته از سوی صنعت گردشگری آمریکا، بیش از ۳۸۰۰۰ رزرو هتل مرتبط با جامجهانی ۲۰۲۶ در ایالات متحده ماه‌ها قبل از مسابقات لغو شده است.
🔹
حالا برنامه‌ریزی ترامپ با همکاری اینفانتینو و تبلیغ مداوم برای جام جهانی آمریکا کمتر از یک ماه به آغاز این تورنمنت با مشکل جدی مواجه شده و آمار فیفا از ۵۰ میلیون درخواست برای حضور در جام جهانی با هتل‌های خالی متضاد است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/farsna/436850" target="_blank">📅 16:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436849">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">عراقچی: وزارت خارجه با فرماندهان نظامی هماهنگ است
🔹
دیپلمات‌های کشور در صورت تغییر نقش، با همان صلابت پشت لانچرهای دفاعی قرار می‌گیرند و نیروهای نظامی نیز در صورت اقتضا، با همان اقتدار پشت میز مذاکره خواهند نشست؛ چراکه تمامی نهادها هدفی مشترک را در یک مسیر واحد دنبال می‌کنند.
🔹
نیروهای مسلح همواره قهرمانان ما هستند. در مسیر تحقق آرمان‌های کشور برخی جان خود را فدا می‌کنند و برخی دیگر از نام و آبروی خویش می‌گذرند.
🔹
ارتباط و هماهنگی مستمر و روزانه میان وزارت خارجه و فرماندهان نیروهای مسلح در سطوح مختلف جریان دارد.
@Farsna</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/farsna/436849" target="_blank">📅 16:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436848">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🎥
حملهٔ وزیر امنیت داخلی رژیم صهیونیستی به اعضای دستگیرشدهٔ ناوگان صمود  @Farsna</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/farsna/436848" target="_blank">📅 16:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436847">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGaSVcmzL7WedypBGW3CYO3IogFm9DM0Vntm0mFkL_0DoDtII9lnqChZzqT5vnGZ9T296T1rd4LBXcHQrh3b-2AANNQJDEEC4_FIRH-OvlruW0swMFi3dl-awM7fk4aIPld5Cj3hmWeOktLzuiRdWXNv45j93yxuKuDkIPNCZbUqONDDPHOx8uqQSQ7xTgW-fJDc1kfoA6_GDu2-DAg8hHIZ6a8gDGgUVMpDgljBiwtqdrlfyD8thxuIegcNmdL5PSSnzPBYsBVjzkctLXcXfeP8UTF8OQO-HP_Ikw5KGr6q2IlLQSk_03aYbHYSXUWMp5mIy4XKumJcbBWf8f2jhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: شهید رئیسی راه حل مشکلات کشور را در بازگشت به آرمان‌های انقلاب می‌دانست
🔹
پیام رئیس‌مجلس به‌مناسبت دومین سالروز شهادت آیت‌الله رئیسی و دیگر شهدای خدمت: در میان شهدای پرواز اردیبهشت، فقدان برادر متدین، صادق، ولایت‌مدار، پرکار، مردم‌دار و عدالت‌طلب…</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/farsna/436847" target="_blank">📅 16:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436846">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWo3TDcWxcuWUyEwd3TMrRQbfDItnS9PhqLet1SmNvom77-BRZrP1qDGfzukgb5xok9CBmjNJn-ejM4qB-6iH8oJveHR8Pyd4pwkDKc-gp9WQlmaVcCFcQjQUMMuuos6QCXY5lQ1O8vegZ5ik4-yUWW88Ltdf_nBq6wZ2QpDW6GFUtjLDDEk1Se6kOi67Fdsywry2Nf64jdXVjE8xo5qMkm2a0QKxuV9Hv6O32nvpibjABIpEeiMKk5MLDsnWWAlVd1_CJFpVRIBgTxeS71BVVbpFrN3WHZbF94rdO0Ver7iYfJCbdNS_v9RS8fmCRTXBV1jMeHoKaLHWtxxZwkLqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار ارتش اسرائیل: با کمبود ۱۲ هزار نیرو روبرو هستیم
🔹
سرتیپ شای طیب، رئیس شعبه برنامه‌ریزی و مدیریت نیروی انسانی ارتش رژیم اشغالگر، نسبت به تشدید بحران جذب نیرو در مؤسسه نظامی این رژیم هشدار داد و وضعیت فعلی را «مشکلی هنجاری و قانونی» توصیف کرد که نیازهای عملیاتی را تهدید می‌کند.
🔹
به نقل از المیادین، طیب در جریان گفتگویی در کمیسیون روابط خارجی و امنیت کنست (پارلمان اسرائیل) در مورد قانون معافیت از خدمت سربازی، اظهار داشت که ارتش به طور فوری به حدود ۱۲ هزار نظامی دیگر نیاز دارد که ۷۵۰۰ نفر از آنها نیروی رزمی برای پر کردن شکاف‌های میدانی هستند.
🔹
روزنامه یدیعوت آحارونوت گزارش داد، این مقام نظامی، به حدود ۳۲ هزار نفر که در حال حاضر از خدمت سربازی غایب هستند، علاوه بر بیش از ۵۰ هزار نفری که تحت عنوان «دستورالعمل دوازدهم» قرار می‌گیرند، (کسانی که مراحل خدمت را گذرانده‌اند) اشاره کرد و ابراز تأسف نمود که بخش زیادی از آنها به زودی به غایبین از خدمت تبدیل خواهند شد، مگر اینکه همکاری نشان دهند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/436846" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436845">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcW1CSEY1Ww8sdSCbIxxgp1iAddI6pvyNPzGtDdJ-0tTvMK7kaQ0JNgB_F47vsRX8RTSV-FX5B5fOw3JcPn7FC-KWkkJnK0QPiQaHNxQ7YVOmWy8M74L20MEilnpsSlPR_oKXkOQV46Z7S3ArvUJnxYFRJXNsf9eQ8Iy6xyzy2zERz8S3fALiwFWPsgKPHpqB4q9-fDnEPA3s10oElkqdnKZzVs1Ty378OpRhTMH72CQm4lP0qSuW1uH-Ed2bkGImWURCskP7dNQ3KAz5Mxgt57M9hRYiJf_XeEh-yli1xkfcwNgWt6HbZIB5uwTKzEF5BwEOsrcCBWLu3FT6Pifsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری قوه‌قضائیه: [رشید مظاهری] بازیکن سابق فوتبال هنگام خروج غیرقانونی از کشور بازداشت شده است
🔹
خبرگزاری قوه‌قضائیه نوشت: «در روزهای اخیر همسر بازیکن سابق فوتبال، در فضای مجازی ادعاهایی را در رابطه با همسر خود مطرح کرده است.
🔹
پیگیری‌ها نشان می‌دهد نامبرده…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/436845" target="_blank">📅 16:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436844">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBVaBqaROAE5ydJCCuTRqZzUATdezbDYZC6vxowqkOqC2L1cqC7caonBezxzbNZp9nBk61Kb67ds6MjnoHhwlgTql4UptyucSIFvL8J1fm8W6rv_ABBwakZQgds832QU3FsEbOztsKf1QQFBVKz_m2jE3epLniM505uA55DMXzvMOXS3VpXGBGV3QQ4I-HEy619CjnZYhXOfDfjKrwrFqvfSzpMcPq8jL1uQuNg9DfxnYauINrYIvxcK0e2yuAprFY7sD7_aUSQxQxGVFT-qhUI1sBZWf4eHI_x96sOUWHC1oktawKZ9bt8n-yYK8XauU-I3Az0CEdxjH5PDqmBPiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: ۲۶ کشتی با هماهنگی نیرودریایی سپاه عبور کردند
🔹
فرماندهی نیروی دریایی سپاه: در شبانه‌روز گذشته ۲۶ فروند کشتی اعم از نفتکش، کانتینر‌بر و سایر کشتی‌های تجاری با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگهٔ هرمز عبور کردند.
🔹
تردد از تنگهٔ هرمز با کسب مجوز و با هماهنگی نیروی دریایی سپاه درحال انجام است.
@Farsna</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/436844" target="_blank">📅 15:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436843">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43e5a15433.mp4?token=kddohwS9CL2sm53-aqXm1SlTTOFfH6j-2Apl7gZmxJdFPTk8YjeQ_bO--t4T1pgnKEMK11knBVpFyNehk3IqjQfB9sNtFyKKqSklrqdM_uNlVav4CZ-iT_ywWfxQGSeh5dm_9tn2xa-xamCMAncPEAu-ZcMbQw7XtCF25PDd0Blht4VEkc2xG4GuzuA6yWbGZklIFw9vnox3vdt-QytO2VEWxvUj8HkgGRhqxqPlIqs5U4vLiwPP4p2yMfzZrGHjfs3QdK06rTeeTord_e9IvGU6clzopN-QCambsHu3oMd3mvWwGFBBOio5c9icgW7JpwKgJgw52VR0zy6h7ugN9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43e5a15433.mp4?token=kddohwS9CL2sm53-aqXm1SlTTOFfH6j-2Apl7gZmxJdFPTk8YjeQ_bO--t4T1pgnKEMK11knBVpFyNehk3IqjQfB9sNtFyKKqSklrqdM_uNlVav4CZ-iT_ywWfxQGSeh5dm_9tn2xa-xamCMAncPEAu-ZcMbQw7XtCF25PDd0Blht4VEkc2xG4GuzuA6yWbGZklIFw9vnox3vdt-QytO2VEWxvUj8HkgGRhqxqPlIqs5U4vLiwPP4p2yMfzZrGHjfs3QdK06rTeeTord_e9IvGU6clzopN-QCambsHu3oMd3mvWwGFBBOio5c9icgW7JpwKgJgw52VR0zy6h7ugN9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستیار ویژۀ وزیر کشور: در صورت تعرض به ایران، باب‌المندب به معادلات جنگ وارد می‌شود
🔹
سرتیپ نامی: ۳ تنگۀ هرمز، مالاکا و باب‌المندب مهم‌ترین چک پوینت‌های استراتژی جهان هستند. تا الان بنا به‌دلایلی فقط از ظرفیت تنگۀ هرمز استفاده کردیم.
🔹
اگر زمانی مجبور شویم…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/436843" target="_blank">📅 15:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436842">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5536424c44.mp4?token=eDypT9CcIHWEdkXIsJF0blIVQAYRVDfj_jh8J40YLXXj098-E4rIFR62wxmCxVjao5Pb3rLE0qTVGWHtTsEjrKii1B3Rx4t2LDgQf9NNfgQAXoAvfeflM6BLcB0xDQBtdcKfe0TNhShD8GYQVDczI-vAR4yNmfiyAGAxjXvUhp2RSFuuM7omGf_mDh4YqEfRt4-tOB9SIsybzPI32MbcV_oHw0KUV459jRXlhe8VZLoxGJDsKsWa1nFYXnCbIYtAv2TLOTbkv5a7j0VGcFHoBQO05oT53LYuQaYPuG4DshxcM5uqXYEspKcszkNqeAgNUqyk49ivTiBxU938WVKKow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5536424c44.mp4?token=eDypT9CcIHWEdkXIsJF0blIVQAYRVDfj_jh8J40YLXXj098-E4rIFR62wxmCxVjao5Pb3rLE0qTVGWHtTsEjrKii1B3Rx4t2LDgQf9NNfgQAXoAvfeflM6BLcB0xDQBtdcKfe0TNhShD8GYQVDczI-vAR4yNmfiyAGAxjXvUhp2RSFuuM7omGf_mDh4YqEfRt4-tOB9SIsybzPI32MbcV_oHw0KUV459jRXlhe8VZLoxGJDsKsWa1nFYXnCbIYtAv2TLOTbkv5a7j0VGcFHoBQO05oT53LYuQaYPuG4DshxcM5uqXYEspKcszkNqeAgNUqyk49ivTiBxU938WVKKow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکار یک سکوی گنبد آهنین توسط حزب‌الله
@Farsna</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/farsna/436842" target="_blank">📅 15:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436841">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‌
🔴
حزب‌الله: تجمعی از خودروها و سربازان ارتش رژیم صهیونیستی را در مسیر رودخانه در حاشیهٔ شهر دیر سریان با گلوله‌های توپخانه هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/436841" target="_blank">📅 15:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436840">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af878bb26d.mp4?token=AK_OmdEfcC65YXnaFIvEdjkAVa4i6etvke0JzdkvOIQsQneXL-8TmZXOkv5OpvvdN-UMJkmMWTjkKLMzQlPSkgzwKlccEesupdd0WqWzV9m7mj_cbI_1pyoTpkk177MjyGm1Br7D5i6sms7NKPZnjQzuzD13OvsDtZQF8y838-N2ap9GjceZysCW6sPjKPmvjOS9SVhOx73vEmGQN19_oCfo8HJ_B9mnr9-v6kRlGwJJ8iWA9pNBNYmTkCSCnaLINMaH2wBU8ikVvzRU7LJGH3bwLZn_RP5-aT_K-VXUwcK6Tbolt9LfoWtT7BxZI-j8MUTTrsrU_n8HhtXbyRoBRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af878bb26d.mp4?token=AK_OmdEfcC65YXnaFIvEdjkAVa4i6etvke0JzdkvOIQsQneXL-8TmZXOkv5OpvvdN-UMJkmMWTjkKLMzQlPSkgzwKlccEesupdd0WqWzV9m7mj_cbI_1pyoTpkk177MjyGm1Br7D5i6sms7NKPZnjQzuzD13OvsDtZQF8y838-N2ap9GjceZysCW6sPjKPmvjOS9SVhOx73vEmGQN19_oCfo8HJ_B9mnr9-v6kRlGwJJ8iWA9pNBNYmTkCSCnaLINMaH2wBU8ikVvzRU7LJGH3bwLZn_RP5-aT_K-VXUwcK6Tbolt9LfoWtT7BxZI-j8MUTTrsrU_n8HhtXbyRoBRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فعال اصلاح‌طلب: مردم‌داری شهید رئیسی در تاریخ ماندگار ‌شد
🔹
باقری، دبیرکل حزب عهد ایران: اگر رؤسای جمهور ادوار را بخواهیم مرور کنیم، شهید رئیسی از حیث مردم‌دار بودن، پروتکل نداشتن، هدف قراردادن منافع مردم و توده‌های مردم، خصوصاً توده‌های کمتر برخوردار یک ویژگی بارزی داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/436840" target="_blank">📅 15:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436839">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
حزب‌الله: تجمع نظامیان و خودروهای رژیم صهیونیستی در شهرهای دبل و رشاف را با حملات موشکی هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/436839" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436838">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IM_wSbaaAMySCX6z5k6tcNvfaKJFAPoWyhoQLYLVxvfWCfwgG3PSohxKq9lpNXa5JNVga6GDiAVLgYgk4VsCCvDo0ttMIUNXhug0GaSaKOVpXMDR2ihMxKD-osByo9cVs2bdRokR1-wChBM0QtyjPu3PfY3Nii_4MOtxoU2iqV6ENUA0Fu6u8kaKr7mpqzPnSt3iimpIXc5gaKw6Do0-sgdjG5a8mVURcw4LqNg8K_sDHow7iRL3Ye-rLG3R8OMR3LLjwGB7bWdpeXKmp7w8PJruH0U7pqAXOEWEbgYuedomWdckBse-hS5eFLPJbir292kmLiPq9Es-MElfZVzqGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت بنزین سوپر ایرانی به جایگاه‌ها
🔹
دولت به پالایشگاه‌های کشور دستور داد، تولید بنزین باکیفیت موسوم به بنزین سوپر را از سر بگیرند.
🔹
از سال ۹۸ کمبود تولید بنزین نسبت به مصرف سبب شده بود تا تولید بنزین سوپر متوقف شود.
🔸
بنزین سوپر نوعی بنزین با عدد اکتان بالاتر نسبت به بنزین معمولی است که برای کاهش پدیدهٔ ناک (احتراق زودرس) و بهبود عملکرد موتورهای با نسبت تراکم بالاتر استفاده می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/436838" target="_blank">📅 15:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436837">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3ac56848f.mp4?token=pfWRZtlhxvIcf874Jj9YqvB70Ap63J-Xocy6Vc3o-C5KayXlTP4byT6NW4lN4l4-eoxhDBKr5yynmx-Nag5gP-QRtSgMwOYPeYT4pDqr99P3BZjvPHaLJNGAgh9bCe5ggCopHWQztPNq5Bz1Hdt7IABy5zbul9p0wV90st4hEYpIoKjqpbyDQeRyfylGe9QkKdqTmVX8AB1b18YZq7bpR-psBCvrZCNLWnG5LsrcbsSf_A7p7p6xD9z6BxHLHPr9F8CZB6MwfOQoHbW1bbUOV84io9QHmtFrKczBXErPuM8Qchr4itGtEAvB9paRRrOMgxkAeVeqRg7Vcf4y9jsDew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3ac56848f.mp4?token=pfWRZtlhxvIcf874Jj9YqvB70Ap63J-Xocy6Vc3o-C5KayXlTP4byT6NW4lN4l4-eoxhDBKr5yynmx-Nag5gP-QRtSgMwOYPeYT4pDqr99P3BZjvPHaLJNGAgh9bCe5ggCopHWQztPNq5Bz1Hdt7IABy5zbul9p0wV90st4hEYpIoKjqpbyDQeRyfylGe9QkKdqTmVX8AB1b18YZq7bpR-psBCvrZCNLWnG5LsrcbsSf_A7p7p6xD9z6BxHLHPr9F8CZB6MwfOQoHbW1bbUOV84io9QHmtFrKczBXErPuM8Qchr4itGtEAvB9paRRrOMgxkAeVeqRg7Vcf4y9jsDew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تکمیل دزدی دریایی صهیونیست‌ها علیه ناوگان جهانی صمود
🔹
نیروی دریایی رژیم صهیونیستی ساعاتی پیش به کشتی‌ها و قایق‌های باقی‌مانده ناوگان صمود که برای درهم شکستن محاصره به سوی نوار غزه در حال عزیمت بودند در آب‌های بین‌المللی حمله و آن را توقیف کرد.
🔸
نظامیان صهیونیست…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/436837" target="_blank">📅 15:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436836">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a162fc100d.mp4?token=bf2sPjNxk5edQrZ1lb8c_0fw_uKSbdkMDQ1lfWjyoRc48aK-idnOQJy48GCP0xFPVuCOal-kQ8b_wt95gxfSEzEb4p5J3vCFS3V7GdMG1Khua_ntC4pvN-iLvqQz0-lxf4boQ--8Uj2rEl6OcDPcEhBqts8M54Cdz1xvHpOaUGMOiiudp4Vpp2MxqQ31yckPoR1eo01SmqXppiYJDpK030S4B47VZXUIKMBHOYCqyFCj5lS-IWGPHrcYtS4HHwuPpvFumvIHw5GQ1MAU0ipdQTSVKcj3J4_cbLF65uIQEsKH72cdLPJNul54y8rCwGRk5C1sgCOLA0htkt0aRI5rWoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a162fc100d.mp4?token=bf2sPjNxk5edQrZ1lb8c_0fw_uKSbdkMDQ1lfWjyoRc48aK-idnOQJy48GCP0xFPVuCOal-kQ8b_wt95gxfSEzEb4p5J3vCFS3V7GdMG1Khua_ntC4pvN-iLvqQz0-lxf4boQ--8Uj2rEl6OcDPcEhBqts8M54Cdz1xvHpOaUGMOiiudp4Vpp2MxqQ31yckPoR1eo01SmqXppiYJDpK030S4B47VZXUIKMBHOYCqyFCj5lS-IWGPHrcYtS4HHwuPpvFumvIHw5GQ1MAU0ipdQTSVKcj3J4_cbLF65uIQEsKH72cdLPJNul54y8rCwGRk5C1sgCOLA0htkt0aRI5rWoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور: با روش‌های گذشته نمی‌توان بر همۀ مسائل امروز کشور غلبه کرد
🔹
پزشکیان در نشست سراسری استانداران کشور: روش‌هایی که تاکنون برای اداره کشور مورد استفاده قرار گرفته، در شرایط فعلی به‌تنهایی پاسخگوی همه مسایل نیست.
🔹
ضروری است با نگاهی نو، روش‌های جدید…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/436836" target="_blank">📅 14:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436835">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ساعت‌های سرنوشت‌ساز برای انحلال پارلمان اسرائیل
🔹
در بحبوحهٔ افزایش تنش‌ها در ائتلاف حاکم رژیم صهیونیستی به رهبری نتانیاهو و تشدید بحران قانون معافیت حریدی‌ها از خدمت نظامی، کنست امروز در بررسی مقدماتی، به طرح‌های قانونی با هدف انحلال آن رأی می‌دهد.
🔹
کانال…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/436835" target="_blank">📅 14:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436834">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14687e4509.mp4?token=P0a9XJaH_4ZxtVXqKioZtnym7QRaCdC7Jnr93HuL8eJ_K0_vLWPkCyTXSnUvHsPmYofkwvEMOwSQQJZccmVmf44Vw6oshqZB83MG7Ub_xKAvkiAdbC-cMQ59iRUH2NmE1cAKkeLOKvykilZjma8nkUINBgCc4ERvhHSNSu6MMe3156euAMg-8qNDP6Qe9DD-ovkgSWRqx68Kg0MXvn3vw1eV1ILV-7lvcgOOi3L7Kww2lafrxDePCgYWLXWRk8229DGZgDEo3IAqCX4XythL9q7GIwEJzPpmbYn6h2bon4dAYIydGWqWum-JxSxQxx0W2WGFQwoq0c7jmI1q8Cm1TZDHdTJpindjvvz53_0VnDDi76AvlzBDlmvOgWQ3pTVXQOMaWn9AjVG0Zs_vcMPesVI-T9clR8PmWIyiEnWoBcUHWHxxjKDIiNKWijNR82nhrO1nhESg2hDeLoIWzfufgEiEn440BvuoEFW9Xi4J_LeBEZzlw5BgzcRQtXZ295cBNhZWRlem7z_muXJVvV4CcJuauL-LdDsAb706k8eFeoRrHWQdQeH4GQugBQgPmXDrxnrFXrDWfzSzdmOmecC-SyILNk0AhHtNyYYKEnQs4SP1n6YiVfibWOIpxqwPhzqU4lu5zhVj90ze4GVD2V_RRcOXGq27K3DH9HytiKC0-Z0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14687e4509.mp4?token=P0a9XJaH_4ZxtVXqKioZtnym7QRaCdC7Jnr93HuL8eJ_K0_vLWPkCyTXSnUvHsPmYofkwvEMOwSQQJZccmVmf44Vw6oshqZB83MG7Ub_xKAvkiAdbC-cMQ59iRUH2NmE1cAKkeLOKvykilZjma8nkUINBgCc4ERvhHSNSu6MMe3156euAMg-8qNDP6Qe9DD-ovkgSWRqx68Kg0MXvn3vw1eV1ILV-7lvcgOOi3L7Kww2lafrxDePCgYWLXWRk8229DGZgDEo3IAqCX4XythL9q7GIwEJzPpmbYn6h2bon4dAYIydGWqWum-JxSxQxx0W2WGFQwoq0c7jmI1q8Cm1TZDHdTJpindjvvz53_0VnDDi76AvlzBDlmvOgWQ3pTVXQOMaWn9AjVG0Zs_vcMPesVI-T9clR8PmWIyiEnWoBcUHWHxxjKDIiNKWijNR82nhrO1nhESg2hDeLoIWzfufgEiEn440BvuoEFW9Xi4J_LeBEZzlw5BgzcRQtXZ295cBNhZWRlem7z_muXJVvV4CcJuauL-LdDsAb706k8eFeoRrHWQdQeH4GQugBQgPmXDrxnrFXrDWfzSzdmOmecC-SyILNk0AhHtNyYYKEnQs4SP1n6YiVfibWOIpxqwPhzqU4lu5zhVj90ze4GVD2V_RRcOXGq27K3DH9HytiKC0-Z0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر: قلب ما برای بچه‌های فوتبال است. دعا می‌کنم تیم ملی از گروهش صعود کند.
🔹
۹۵ درصد ایرانی‌های خارج از کشور بی‌نظیرند. نگاه به درپیت‌های اینترنشنال نکنید که می‌رقصند. آن‌ها برای ۲۰ دلار پشتک می‌زنند.
🔹
ایرانی‌های واقعی در آمریکا نگذارند کسی بیاید تیم ملی فوتبال را اذیت کند.
@Sportfars</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/436834" target="_blank">📅 14:35 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

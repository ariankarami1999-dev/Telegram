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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 17:31:58</div>
<hr>

<div class="tg-post" id="msg-436868">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 408 · <a href="https://t.me/farsna/436868" target="_blank">📅 17:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436867">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izEyyi2Vti-W1z_QK6SHzPyZFysQc246ZdzLpaIgKjV4lqivzjyaJJKcCAybgMEdluWLqwMVb89NgpiDIGGdogDhQzTPX6Wi3r-HFAwI5WXx2NOQn9zyo1FNSa5hEPCsS-vSeecnIO7KesnC9g67gBBC_ZuHSA-aX2nMDDIDS__shZW0llX3WAID0XAWF5iWA6WrHJw3rdUGd6woW7YA5bbavZKT2l4B-d9mq4mFi7M2H1BCy3txXbi3hl36JpULuSU5bbxuKdzsu5MLIwP6atinEc5N8mKq2CMtzZiuvqhweTeJIWJBQtrulZL_CJAtu3DE5dm43sH4MODUyZRRsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: نتانیاهو هر کاری من بخواهم انجام می‌دهد
🔹
دونالد ترامپ، رئیس‌جمهور آمریکا امروز چهارشنبه تلاش‌ کرد به انتقادهایی که او را بابت راه‌اندازی جنگ علیه ایران بنا به خواست اسرائیل مورد سرزنش قرار می‌دهند پاسخ دهد.
🔹
او گفت: «نتانیاهو کارهایی که من بخواهم را انجام خواهد داد.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/farsna/436867" target="_blank">📅 17:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436866">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rxbs8aN3-vW6h7qWS1RZlklbxE2BbMDv61Nk_aKystE-4CNmg__c5Gg1C1TqIjNowo7o1qBGX_wD5ZRaoRKKMcqA938dVKsGMogybhM8Bq7R9wmWv-UQXDFRAUjTaYx9yTtL8i9KtyZw4AFbSVJWOiz1ei2TbxRXaEJ0qd-bjsad-mnoi4c_Jsv5AILcPZtRqsRdaDecgJVopOXP6mziPEhpqvKKifuHT1bqePLfK-LbInphGYpcNV3hm2Pj8gE00LfTvcyQ7jvN_CNyq6X9ruVynwxnJvMYTCVqGmz5Z19Rddb6Fbj9B0bJA6Sx7cpxCiWLRA2ohAdLy-Qq9mDWaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استعفای مقام ارشد اطلاعاتی دولت ترامپ به‌دلیل مخالفت با جنگ ایران
🔹
واشنگتن‌پست: آماریلیس فاکس کندی، یکی از مقامات ارشد اطلاعاتی دولت ترامپ و متحد تولسی گابارد، مدیر اطلاعات ملی، این هفته از ۲ سمت کلیدی دولتی کناره‌گیری می‌کند.
🔹
خروج آماریلیس فاکس کندی به‌گفتۀ یک منبع، تا حدی به‌دلیل مخالفت او با اقدام نظامی ترامپ در ایران بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/farsna/436866" target="_blank">📅 17:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436865">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‌
🔴
قالیباف: در شرایط جنگ اقتصادی روش‌های عادی کافی نیستند و وزارتخانه‌های اقتصادی باید با روش‌های خلاقانه دنبال حل مشکلات باشند. @Farsna</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/farsna/436865" target="_blank">📅 17:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436864">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‌
🔴
قالیباف: متاسفانه برخی با انگیزه‌های سیاسی و به بهانۀ گرانی‌ها بدون درنظر گرفتن واقعیت‌ها، انگشت اتهام را فقط به سوی دولت یا رئیس‌جمهور می‌گیرند.
🔸
برخی انتقادها از دولت به‌گونه‌ای است که گویی جنگی اتفاق نیفتاده است.
🔸
من منکر برخی ضعف‌های مدیریتی نیستم…</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/farsna/436864" target="_blank">📅 17:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436863">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‌
🔴
قالیباف: مردم انتظار دارند همه مسئولان هم‌راستا با بعثت اعجازگونۀ مردم برای حل مشکلات معیشتی به صورت جهادی تلاش کنند. @Farsna</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/farsna/436863" target="_blank">📅 17:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436862">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‌
🔴
قالیباف: از جهش قیمت‌ها و بالا رفتن هزینه‌های زندگی مردم اطلاع دارم
🔹
دشمن تصور می‌کند اگر زندگی مردم سخت‌تر شود، انسجام ملی تضعیف می‌شود اما مردم ثابت کردند که هم‌چنان در میدان مبارزه با دشمن حضور دارند و انتظار دارند که مسئولان مشکلات را حل کنند.  @Farsna</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/farsna/436862" target="_blank">📅 17:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436861">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‌
🔴
قالیباف: دشمن هنوز نفهمیده که ملت ایران در هر شرایطی در برابر زور سر خم نمی‌کند. @Farsna</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/farsna/436861" target="_blank">📅 17:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436860">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‌
🔴
قالیباف: باید با تقویت آمادگی برای پاسخ موثر به حملات احتمالی و همچنین با افزایش تاب‌آوری اقتصادی، دشمن را از خطای محاسباتی بیرون بیاوریم و ناامیدش کنیم. @Farsna</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/farsna/436860" target="_blank">📅 17:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436859">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌
🔴
قالیباف: دشمن هنوز به تسلیم‌شدن ملت ایران امیدوار است و به غلط فکر می‌کند می‌تواند با تداوم محاصره و ازسرگیری جنگ ایران را مجاب کند که به زیاده‌خواهی آمریکا پاسخ مثبت دهد. @Farsna</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/farsna/436859" target="_blank">📅 17:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436858">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‌
🔴
قالیباف: دشمن را از تعرض مجدد به ایران پشیمان خواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/farsna/436858" target="_blank">📅 16:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436857">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‌
🔴
قالیباف: مردم اطمینان داشته باشند نیروهای نظامی ما از فرصت آتش‌بس به بهترین شکل برای بازسازی توان خود استفاده کردند. @Farsna</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/farsna/436857" target="_blank">📅 16:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436856">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
قالیباف: تحرکات آشکار و پنهان دشمن نشان می‌دهد که به‌دنبال دور جدید جنگ است.  @Farsna</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/farsna/436856" target="_blank">📅 16:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436855">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
قالیباف: تحرکات آشکار و پنهان دشمن نشان می‌دهد که به‌دنبال دور جدید جنگ است.
@Farsna</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/farsna/436855" target="_blank">📅 16:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436854">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/farsna/436854" target="_blank">📅 16:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436853">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/farsna/436853" target="_blank">📅 16:51 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436852">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQnME-4JR7oNZMDmfLziUIpUj1jf6qPLyU8mK0kNyjAyc06aypcmuZnTxWFZLlwN3LxaOeUsHLNWeDgnyqff2In1dkzadrtIjUPoUqlN2-meJ5vEM4NRLQoQ9YlARHrM4Lo_rqQn9x3qmI_f7eV-T1jkBThDsBxgCh0y2iZk8Y_NtQ1i2-SjxYbW4Ruhiq72tUJrRb1u42WvhJy3N3dMqq981UK7d3L_5X_-Y9CfzGu8gFC1WC_EnX6f_oKl8s7NHwzVBVd-0yFYatyTX7LTcNlW_ry24D8Gbo5oilcW3OM42tYBGt3tq_U1yqbRhtw4ezHbin_eMG9fg24MtIWbxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: آمریکا دوباره در جنگی بی‌پایان که در آن امکان پیروزی ندارد گیر خواهد افتاد
🔹
رئیس مجلس در صفحهٔ خود عبارتی از فصل ۱۱ کتاب خاطرات ونس، معاون رئیس‌جمهور آمریکا نقل کرد: «ما احساس می‌کردیم در دو جنگ بی‌پایان و بدون امکان برد گیر افتاده‌ایم و سهم نامتناسبی از سربازان از محله خودمان (محله فقرا) آمده بود.»
🔹
قالیباف در ادامه نوشت: این وضعیت (گیر افتادن آمریکا در جنگی که نمی‌توانند ببرند) دوباره درحال تکرارشدن است. این‌بار فقرا و فراموش‌شدگان آمریکایی باید هزینهٔ جنگ‌افروزی الیگارش‌های نزدیک به کاخ سفید، افراد شیطان‌صفتی همچون جیمی دیمون و لابی تاجران جنگ در واشینگتن را بپردازند.
🔸
گفتنی است جیمی دیمون، مدیرعامل موسسه مالی و بانک جی‌پی مورگان، در آمریکا و از مهم‌ترین چهره‌های حلقهٔ تامین‌کنندگان مالی جنگ آمریکا با ایران است که به‌تازگی نیز علیه ایران لفاظی کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/farsna/436852" target="_blank">📅 16:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436851">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/farsna/436851" target="_blank">📅 16:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436850">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/farsna/436850" target="_blank">📅 16:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436849">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عراقچی: وزارت خارجه با فرماندهان نظامی هماهنگ است
🔹
دیپلمات‌های کشور در صورت تغییر نقش، با همان صلابت پشت لانچرهای دفاعی قرار می‌گیرند و نیروهای نظامی نیز در صورت اقتضا، با همان اقتدار پشت میز مذاکره خواهند نشست؛ چراکه تمامی نهادها هدفی مشترک را در یک مسیر واحد دنبال می‌کنند.
🔹
نیروهای مسلح همواره قهرمانان ما هستند. در مسیر تحقق آرمان‌های کشور برخی جان خود را فدا می‌کنند و برخی دیگر از نام و آبروی خویش می‌گذرند.
🔹
ارتباط و هماهنگی مستمر و روزانه میان وزارت خارجه و فرماندهان نیروهای مسلح در سطوح مختلف جریان دارد.
@Farsna</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/farsna/436849" target="_blank">📅 16:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436848">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🎥
حملهٔ وزیر امنیت داخلی رژیم صهیونیستی به اعضای دستگیرشدهٔ ناوگان صمود  @Farsna</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/farsna/436848" target="_blank">📅 16:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436847">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGaSVcmzL7WedypBGW3CYO3IogFm9DM0Vntm0mFkL_0DoDtII9lnqChZzqT5vnGZ9T296T1rd4LBXcHQrh3b-2AANNQJDEEC4_FIRH-OvlruW0swMFi3dl-awM7fk4aIPld5Cj3hmWeOktLzuiRdWXNv45j93yxuKuDkIPNCZbUqONDDPHOx8uqQSQ7xTgW-fJDc1kfoA6_GDu2-DAg8hHIZ6a8gDGgUVMpDgljBiwtqdrlfyD8thxuIegcNmdL5PSSnzPBYsBVjzkctLXcXfeP8UTF8OQO-HP_Ikw5KGr6q2IlLQSk_03aYbHYSXUWMp5mIy4XKumJcbBWf8f2jhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: شهید رئیسی راه حل مشکلات کشور را در بازگشت به آرمان‌های انقلاب می‌دانست
🔹
پیام رئیس‌مجلس به‌مناسبت دومین سالروز شهادت آیت‌الله رئیسی و دیگر شهدای خدمت: در میان شهدای پرواز اردیبهشت، فقدان برادر متدین، صادق، ولایت‌مدار، پرکار، مردم‌دار و عدالت‌طلب…</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/farsna/436847" target="_blank">📅 16:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436846">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/farsna/436846" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436845">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcW1CSEY1Ww8sdSCbIxxgp1iAddI6pvyNPzGtDdJ-0tTvMK7kaQ0JNgB_F47vsRX8RTSV-FX5B5fOw3JcPn7FC-KWkkJnK0QPiQaHNxQ7YVOmWy8M74L20MEilnpsSlPR_oKXkOQV46Z7S3ArvUJnxYFRJXNsf9eQ8Iy6xyzy2zERz8S3fALiwFWPsgKPHpqB4q9-fDnEPA3s10oElkqdnKZzVs1Ty378OpRhTMH72CQm4lP0qSuW1uH-Ed2bkGImWURCskP7dNQ3KAz5Mxgt57M9hRYiJf_XeEh-yli1xkfcwNgWt6HbZIB5uwTKzEF5BwEOsrcCBWLu3FT6Pifsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری قوه‌قضائیه: [رشید مظاهری] بازیکن سابق فوتبال هنگام خروج غیرقانونی از کشور بازداشت شده است
🔹
خبرگزاری قوه‌قضائیه نوشت: «در روزهای اخیر همسر بازیکن سابق فوتبال، در فضای مجازی ادعاهایی را در رابطه با همسر خود مطرح کرده است.
🔹
پیگیری‌ها نشان می‌دهد نامبرده…</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/farsna/436845" target="_blank">📅 16:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436844">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBVaBqaROAE5ydJCCuTRqZzUATdezbDYZC6vxowqkOqC2L1cqC7caonBezxzbNZp9nBk61Kb67ds6MjnoHhwlgTql4UptyucSIFvL8J1fm8W6rv_ABBwakZQgds832QU3FsEbOztsKf1QQFBVKz_m2jE3epLniM505uA55DMXzvMOXS3VpXGBGV3QQ4I-HEy619CjnZYhXOfDfjKrwrFqvfSzpMcPq8jL1uQuNg9DfxnYauINrYIvxcK0e2yuAprFY7sD7_aUSQxQxGVFT-qhUI1sBZWf4eHI_x96sOUWHC1oktawKZ9bt8n-yYK8XauU-I3Az0CEdxjH5PDqmBPiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: ۲۶ کشتی با هماهنگی نیرودریایی سپاه عبور کردند
🔹
فرماندهی نیروی دریایی سپاه: در شبانه‌روز گذشته ۲۶ فروند کشتی اعم از نفتکش، کانتینر‌بر و سایر کشتی‌های تجاری با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگهٔ هرمز عبور کردند.
🔹
تردد از تنگهٔ هرمز با کسب مجوز و با هماهنگی نیروی دریایی سپاه درحال انجام است.
@Farsna</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/farsna/436844" target="_blank">📅 15:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436843">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/farsna/436843" target="_blank">📅 15:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436842">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/farsna/436842" target="_blank">📅 15:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436841">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‌
🔴
حزب‌الله: تجمعی از خودروها و سربازان ارتش رژیم صهیونیستی را در مسیر رودخانه در حاشیهٔ شهر دیر سریان با گلوله‌های توپخانه هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/farsna/436841" target="_blank">📅 15:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436840">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/farsna/436840" target="_blank">📅 15:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436839">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
حزب‌الله: تجمع نظامیان و خودروهای رژیم صهیونیستی در شهرهای دبل و رشاف را با حملات موشکی هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farsna/436839" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436838">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/farsna/436838" target="_blank">📅 15:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436837">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/farsna/436837" target="_blank">📅 15:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436836">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/farsna/436836" target="_blank">📅 14:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436835">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ساعت‌های سرنوشت‌ساز برای انحلال پارلمان اسرائیل
🔹
در بحبوحهٔ افزایش تنش‌ها در ائتلاف حاکم رژیم صهیونیستی به رهبری نتانیاهو و تشدید بحران قانون معافیت حریدی‌ها از خدمت نظامی، کنست امروز در بررسی مقدماتی، به طرح‌های قانونی با هدف انحلال آن رأی می‌دهد.
🔹
کانال…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/farsna/436835" target="_blank">📅 14:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436834">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/farsna/436834" target="_blank">📅 14:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436833">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94271ae1b3.mp4?token=vOXFWF522DZdoPVt5v_BKUZp_BIocc0YePIeBBbEuaZCkVKEaL-ez2CgT-WlacAX1_IZzGvwtPr6Z6SuEPdSSvD7e7gA4KdSiILvJAHt1yQQCl3at694JRCdXYejvEoZrPFl0QxiNruBRSgveZ99gzK9v4lwI_QwBR6qZusguFZgm_XQiZEVdMWF0dffwA92kuusJRTSp4lRMPvfn09KlPwJ0yVzoypq6ZzkDlcSln7lmhjiv45KmIwDpS-AFiXLsuQCABlIYpWjnO3uh1M6D4owkDEs2lU5NlA_jOMLCA9Og6DJZL_7x3VzSae6ccP61KEbaG14Cbbc-0CVKkg8Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94271ae1b3.mp4?token=vOXFWF522DZdoPVt5v_BKUZp_BIocc0YePIeBBbEuaZCkVKEaL-ez2CgT-WlacAX1_IZzGvwtPr6Z6SuEPdSSvD7e7gA4KdSiILvJAHt1yQQCl3at694JRCdXYejvEoZrPFl0QxiNruBRSgveZ99gzK9v4lwI_QwBR6qZusguFZgm_XQiZEVdMWF0dffwA92kuusJRTSp4lRMPvfn09KlPwJ0yVzoypq6ZzkDlcSln7lmhjiv45KmIwDpS-AFiXLsuQCABlIYpWjnO3uh1M6D4owkDEs2lU5NlA_jOMLCA9Og6DJZL_7x3VzSae6ccP61KEbaG14Cbbc-0CVKkg8Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عبور شناورهای ملیت‌های مختلف به‌ویژه شرق آسیا از تنگۀ هرمز بیشتر شد
🔹
خبرنگار صداوسیما در تنگه هرمز: سفیدپوشان نیروی دریایی ارتش در عمق تا شمال اقیانوس هند آرایش و بازآرایی متناسب گرفتند و از این سو سبزپوشان نیروی دریایی سپاه در همۀ سواحل و جزایر برای دفاع در اوج آمادگی به‌سر می‌برند.
@Farsna</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/farsna/436833" target="_blank">📅 14:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436832">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27322a441a.mp4?token=l8-mGeVpl1a_U7ZjFBVP7e8divUr8SvXxT7LHrg7mjshVv5lYwRPLgLHh5BlHr_cfKuToenuXA4VutNWyrRX59huH5SVmTBKiB7bV3uginxXO4l0Knmbq6YdgTdJ3Oie4BGZKYVVVEMFB_Jr7y-hYSqvwsntr7ngS6q0S8WaQcXhH6UHetYLizvKxu-B5wjsAVTvFOYdTY3qv70uQpwMXzilmfsNp4zejyLX4OcqtnBLSTFQy55_JLCAWZalKzewhKf-FG2AJH8loZyAZ8UlAS77E8bYEW2z9EP6eAjjVCXhLvHefBb6XUwcHWgxDCCEdMcuqK5znD4xPj4H8AHbAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27322a441a.mp4?token=l8-mGeVpl1a_U7ZjFBVP7e8divUr8SvXxT7LHrg7mjshVv5lYwRPLgLHh5BlHr_cfKuToenuXA4VutNWyrRX59huH5SVmTBKiB7bV3uginxXO4l0Knmbq6YdgTdJ3Oie4BGZKYVVVEMFB_Jr7y-hYSqvwsntr7ngS6q0S8WaQcXhH6UHetYLizvKxu-B5wjsAVTvFOYdTY3qv70uQpwMXzilmfsNp4zejyLX4OcqtnBLSTFQy55_JLCAWZalKzewhKf-FG2AJH8loZyAZ8UlAS77E8bYEW2z9EP6eAjjVCXhLvHefBb6XUwcHWgxDCCEdMcuqK5znD4xPj4H8AHbAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام رهبر انقلاب اسلامی به‌مناسبت دومین سالگرد شهادت شهید رئیسی و بزرگداشت شهدای خدمت
🔹
گرامیداشت شهدای پرواز اردیبهشت و در رأس آنان رئیس‌جمهور شهید حجت‌الاسلام والمسلمین رئیسی، یادآور شهادت خیل شهیدان خدمتگزار در جمهوری اسلامی ایران است؛ از مطهری و بهشتی…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/farsna/436832" target="_blank">📅 14:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436831">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پیام رهبر انقلاب اسلامی به‌مناسبت دومین سالگرد شهادت شهید رئیسی و بزرگداشت شهدای خدمت
🔹
گرامیداشت شهدای پرواز اردیبهشت و در رأس آنان رئیس‌جمهور شهید حجت‌الاسلام والمسلمین رئیسی، یادآور شهادت خیل شهیدان خدمتگزار در جمهوری اسلامی ایران است؛ از مطهری و بهشتی…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/farsna/436831" target="_blank">📅 14:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436830">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhnLQYgqwRlhA0od9xwcf9Lwg7YqNH5JNETIaMCVt8V8rnSJCng9YPc5Ih6iMrjJWto4Pn7VuNpjJYV2OLXZgjs5le1KE0DCOVTO49pawWo5rOF3ekw_hTyUP3HgLw-eHL8c5aQmKuaZruHgrSadXQrm2ZYFbl99IAABoKDjh6MyuFezfeYJNOlH890fuQL-62ZATZlQOuHTGDooMAB90URSAyDP8QS6TpTf1SknNfXNizWAJRHgNKsyhNZByQmAauiOhtj_mwyR5b14tHk3sw4KACQRJIdY4bRipBZsoxppnHmcl59vUZftrG390hj4lIUsWeifwxhZ1mea0jvlhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تا ساعتی دیگر پیام رهبر انقلاب به‌مناسبت دومین سالگرد شهادت شهید رئیسی و بزرگداشت شهدای خدمت منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/436830" target="_blank">📅 14:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436829">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/078eb7e4b1.mp4?token=cwikG9LSDzH_OpOvB_xMRPZ2UOo_Tuufa3V-I0cafk75R-rvgca6iGk0QxI3JRnomnJNRGdUljZGnSiu3Qmecjby8tuS4iCjFH2PVrIM_Ri7WKaF5IcrUtDCNcxvqCDqXWzVf-Cm3g8GUK989eHgYlTNzhe6Wkd0dDHYx2A4HWxW_iXyFe3NZhVTueHuTX6z9hDOY6llbmauixle08FX_J_1rmT4ACwC7Omk-Ybgb9IXcnRtgYCZ7KET9EtFTo00CIom5SSyZG921fCaKOl9QS6CEuhirX51Fqw1FuUNqKC8CLzNJ-FQVEYL3m1oXmnuI2Opr--aMSVClv1NwQXpsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/078eb7e4b1.mp4?token=cwikG9LSDzH_OpOvB_xMRPZ2UOo_Tuufa3V-I0cafk75R-rvgca6iGk0QxI3JRnomnJNRGdUljZGnSiu3Qmecjby8tuS4iCjFH2PVrIM_Ri7WKaF5IcrUtDCNcxvqCDqXWzVf-Cm3g8GUK989eHgYlTNzhe6Wkd0dDHYx2A4HWxW_iXyFe3NZhVTueHuTX6z9hDOY6llbmauixle08FX_J_1rmT4ACwC7Omk-Ybgb9IXcnRtgYCZ7KET9EtFTo00CIom5SSyZG921fCaKOl9QS6CEuhirX51Fqw1FuUNqKC8CLzNJ-FQVEYL3m1oXmnuI2Opr--aMSVClv1NwQXpsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احتکار ۱۴۰۰ تنی مرغ منجمد در شیراز
🔹
تعزیرات حکومتی فارس: در بازرسی از یک کشتارگاه در شیراز، ۱۴۰۰ تن مرغ کشف شد که از ابتدای جنگ تحمیلی در ۹ سردخانه احتکار شده بود.
🔸
یک محمولهٔ مرغ منجمد ۹۰۰ تنی دیگر نیز روز گذشته در شیراز کشف شده بود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/farsna/436829" target="_blank">📅 13:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436828">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJwFbjd6g8k9ia0LLOzh7lt0xZqKhajaHhfSL1xFTeo2a3Bjuq_MDa4UYkwzV1B69DB2o8CzsKNd_IGHA55YxOye4eJyKC2YObgQ6ZB-51gHEC-grQHs3UaDVeydAFrYcuVqQn_Qy1yfCeSBvzCS2npqK_EV7qZZDRso2efvuOFxsSPiOpED-F3rr_X2ZE5TjLQ2l0HY8vCfanDlc-1cO2HBkf_JmslYDWcmdCCZbblrYJ3fTtI3epgWEcNktIC3DlI6YuowWzAQ9KdEaZqOv8SNQ5aPCWKyomOUvNdLStaz7PkO09-caOqrfQzADdyMSbPVkqaKjZu2qDHyu3nTVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس اولین روز بعداز جنگ را مثبت تمام کرد
🔹
شاخص کل بورس در پایان معاملات امروز با رشد ۲۵۰۰ واحدی به ۳ میلیون و ۷۱۶ هزار واحد رسید. @Farsna</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/436828" target="_blank">📅 13:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436827">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خبرگزاری قوه‌قضائیه: [رشید مظاهری] بازیکن سابق فوتبال هنگام خروج غیرقانونی از کشور بازداشت شده است
🔹
خبرگزاری قوه‌قضائیه نوشت: «در روزهای اخیر همسر بازیکن سابق فوتبال، در فضای مجازی ادعاهایی را در رابطه با همسر خود مطرح کرده است.
🔹
پیگیری‌ها نشان می‌دهد نامبرده قصد داشته با تغییر چهره و پرداخت رشوه به ماموران مرزبانی از مرزهای غربی به صورت غیرقانونی از کشور خارج شود که در هنگام خروج‌‌ بازداشت شده است.
🔹
همچنین ادعای نگهداری متهم در سلول انفرادی نیز صحت ندارد و نامبرده در بند عمومی زندان حضور دارد تا به اتهامات او از جمله پرداخت رشوه به مامور دولت، فعالیت تبلیغی برخلاف امنیت ملی کشور در شرایط جنگی و اقدام به عبور غیرمجاز از مرز رسیدگی شود.»
@Farsna</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/436827" target="_blank">📅 13:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436826">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8f77da65.mp4?token=oFCpistVBZ-2VU5ICpUIo8zQC0-QuSHmhMAIb7GzP53WT_6OJfgiKGQ3_d6Zek-bOrkFuiB5WveAFQhL2SAmzYMDu6BUYOxAMLcYSXE_vYQpkxdOBnys6OOt3Xr87ZYA2vEn5zUZiRtQD1WGBcPQkPOXDSvyLqBjL5j8OE80cBfGd6heeuP2diIq9Pj8N29XJN-qsNayVe8162_Qnr4BxFqcq5BH5viIHJeKgLcdWxzaiQ4d6BLfbYkoIIooy9QZW3GigljQD-oU8cj6QlYUz7wuxo2EO6opRk7TSIDPjz4wwf57SHsYBsCS2GvXciAGG2Puqfta10NzwoQ3ppTpkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8f77da65.mp4?token=oFCpistVBZ-2VU5ICpUIo8zQC0-QuSHmhMAIb7GzP53WT_6OJfgiKGQ3_d6Zek-bOrkFuiB5WveAFQhL2SAmzYMDu6BUYOxAMLcYSXE_vYQpkxdOBnys6OOt3Xr87ZYA2vEn5zUZiRtQD1WGBcPQkPOXDSvyLqBjL5j8OE80cBfGd6heeuP2diIq9Pj8N29XJN-qsNayVe8162_Qnr4BxFqcq5BH5viIHJeKgLcdWxzaiQ4d6BLfbYkoIIooy9QZW3GigljQD-oU8cj6QlYUz7wuxo2EO6opRk7TSIDPjz4wwf57SHsYBsCS2GvXciAGG2Puqfta10NzwoQ3ppTpkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستیار ویژۀ وزیر کشور: در صورت تعرض به ایران، باب‌المندب به معادلات جنگ وارد می‌شود
🔹
سرتیپ نامی: ۳ تنگۀ هرمز، مالاکا و باب‌المندب مهم‌ترین چک پوینت‌های استراتژی جهان هستند. تا الان بنا به‌دلایلی فقط از ظرفیت تنگۀ هرمز استفاده کردیم.
🔹
اگر زمانی مجبور شویم از تنگه باب‌المندب استفاده کنیم، قیمت نفت به بالای ۲۰۰ تا ۲۵۰ دلار می‌رسد.
@Farsna</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/436826" target="_blank">📅 13:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436824">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmL62fDGFzOXJoJouvhXrmKPbPIRXdlVXTx0cyeXIATCRVP_h7oWQs8de__Pe7cm6pTZNHUhdVZO4IhO-0zTMtOvEXPxLmrp_IPZi9suqjUjhRCZDDQOLD5sYhFXWzKV-Naz6aolPvix8KjOh9BHMPNHY97oLYDjgBxVNsypGTp_LLh9idjXCLXFD13Tvey7_DsaGGVLE7KYbi-maJR1Vs1Ot-CPyNdaZVAmu0YVaxG1x9Cs3rjBmDi9vESTpsMnVb1azFKcVNRpaXgluj8-zgddf7Db5s1WATR8q0el-ShGw6dvmFMfitQzf6gXmWJbB31ZvKC3w3reD9p-DUbkCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تا ساعتی دیگر پیام رهبر انقلاب به‌مناسبت دومین سالگرد شهادت شهید رئیسی و بزرگداشت شهدای خدمت منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/436824" target="_blank">📅 13:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436823">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ae425b97d.mp4?token=DIjCclr1PsknrZXXfIvmEWaGpyIRmPozhtEpHoB_O77Lw0Mx4YW5QL3zw91qA_0QgppIZz8Gh8vxzUlmgNWg053Gb5nA2Pdih56Buh86AVKnUm-Du1dXCKLogAJ8jJnfazLRffjgHZX85AjQlILIivNvrry8zGwnmyEnbJutHxBm-WYW1aHcnR3W5rmczXvUvdAiRlatfnWutv9_OPpJFyHnADwbHUv7wS111HzWkfnuOlPoPITBFK1Odmj-Yfui1MX2p6Inp5lwNrybvLzDGrpt6BnpcKxFjE9JzePIZhJWwhGhD04NoxXiukyVnDQuBJi2rhdjWonEvOhh_BV8KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ae425b97d.mp4?token=DIjCclr1PsknrZXXfIvmEWaGpyIRmPozhtEpHoB_O77Lw0Mx4YW5QL3zw91qA_0QgppIZz8Gh8vxzUlmgNWg053Gb5nA2Pdih56Buh86AVKnUm-Du1dXCKLogAJ8jJnfazLRffjgHZX85AjQlILIivNvrry8zGwnmyEnbJutHxBm-WYW1aHcnR3W5rmczXvUvdAiRlatfnWutv9_OPpJFyHnADwbHUv7wS111HzWkfnuOlPoPITBFK1Odmj-Yfui1MX2p6Inp5lwNrybvLzDGrpt6BnpcKxFjE9JzePIZhJWwhGhD04NoxXiukyVnDQuBJi2rhdjWonEvOhh_BV8KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تعجب زن اسرائیلی از حماقت سلطنت‌طلبان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/436823" target="_blank">📅 12:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436822">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjDN2zP-mPdHC9l_ZlyCbBLyt2J0h0UUpLsQWCcb8k41vE5f8bRKpC-sVc9NEr9bI7ob73DXQySLT--EpNoDYFqqJdSMnnKVN754zppm0Ydh7BSwIIJM9MxB0a05-Mpq5Ps8PSSqyPDqm8rOGD7ZtM2yztjEhU0apS--Q5yyohZgmu8OMQXbX1Jg9UF_Y7o2HrWj6cNegTNdqdxyJuuKO8Ql7X4lthDP06tQrGopNupScyOLQzw3wwo1ZQhz-RDO6uF-EKWwkj2DF5D84hnU7gdH_k7mcby94uva5DKbhas7Iu8FZ052LVACgNvDdMNXorZAskH3zdjtYen5Etuabw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ علنی پرسپولیس سر سهیمه آسیایی
🔹
‼️
شایعات از احتمال لغو ادامه لیگ برتر و معرفی مستقیم نمایندگان ایران به آسیا حکایت دارد. باشگاه پرسپولیس با این اقدام مخالفت کرده و آن را غیرمنصفانه و غیرفوتبالی خوانده است.
🎙
یکی از مسئولان ارشد باشگاه پرسپولیس گفت:
🗣
ما…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/farsna/436822" target="_blank">📅 12:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436821">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1vqbOhE38yQq2PtEurDW_lGto9v8wvBCXgI9pc3ec4Gnr6LfSfbwc8IhcM24Pk6ES5kW9T92tmLe2FnhCr6KM4kMXEclv3rM80DWMpIqJuJiphirgdys1yRhGiMASOVSB8iwIThkRY03UBcnZOrobj3c7V_RxCEHVbV0quJE4Ctwv4NLmNGy-OGMFFFENLQ8apC6KA_5PCE2UyyOHmWW0rcCatzKmlHxiXV3PyfGLK9gtC8VjxsronSEuO4wShr5CXiaQ4N3-djXbBakrfSXV8yRJCN3KFqWRoGjee3iWorK7Y-0IesO0akod4iFt7gtHufVOI01J9VgppD_hVfZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
«درخشش روابط عمومی شرکت صنعت فولاد شادگان در جشنواره سلام خوزستان با کسب ۲ عنوان برگزیده»
🔹
روابط عمومی شرکت صنعت فولاد شادگان
در ششمین جشنواره «سلام خوزستان» با کسب ۲ عنوان برگزیده خوش درخشید.
🔹
این جشنواره با حضور ۷۰ روابط عمومی از ادارات، سازمان‌ها و شرکت‌های استان خوزستان برگزار شد و آثار ارسالی در ۱۲ بخش تخصصی مورد ارزیابی هیئت داوران قرار گرفت.
🔹
در این رویداد، روابط عمومی شرکت صنعت فولاد شادگان در بخش‌های «تولید موسیقی و ترانه‌های حماسی» و «هوش مصنوعی» موفق به کسب عنوان برگزیده شد.
🔹
آیین اختتامیه ششمین جشنواره «سلام خوزستان» روز سه‌شنبه ۲۹ اردیبهشت‌ماه ۱۴۰۵ در اهواز برگزار شد و در پایان از برگزیدگان این دوره با اهدای تندیس، لوح تقدیر و جوایز تجلیل به عمل آمد.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/436821" target="_blank">📅 12:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436820">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsrxsZvJZ-zRjc7jx8gq1yYRCbToIcFvLql5yA-U2h7NOYQqp5Mcjf3gKJZA2kf1spj6-H9ERNSg0jlRMnG6i9LgxAXWS7kER8iVuj6SBhNTiG1o4MQrzSXSUhXKn4sNAtiFSX4AV0FuLlf4oPeD_x45yyN6yTs3JQ3OjH6BSPcsYm_Bo3_6jp4KYRnGwmbA_atNqPsMYywI1s2fkHTwZTDSZ2fiDkuL50ky89AC0AFqLT-92Xk8OSRSm35sr2QEXcu77_WUhnnZJ7G0R-tfni_QXdaWXdItbomR0VH5FTabgbfz53n7YU5FTdD7GEbhtBKwMeXpG4028ADg1LPM3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">*
🌐
سامانه فرارفاه بانک رفاه کارگران به‌روزرسانی شد*
🔹️
با هدف توسعه بانکداری الکترونیک و به منظور ارائه خدمات مطلوب و متمایز به مشتریان، سامانه "فرارفاه" (مبتنی بر سیستم‌عامل‌های Android و iOS) بانک رفاه کارگران به‌روزرسانی شد.
🔹️
"درخواست کارت رفاهی متصل به اوراق گام"، "خرید بسته اینترنت اعتباری یا دائمی"، "فعال‌سازی حساب کاربری" و... از جمله قابلیت‌های نگارش 1.5.6 سامانه فرارفاه مبتنی بر سیستم عامل Android و نگارش 1.17.0 مبتنی بر سیستم عامل iOS است.
🔹️
سامانه فرارفاه از طریق پورتال اطلاع‌رسانی بانک رفاه کارگران (
https://www.refah-bank.ir/fararefah
) در دسترس قرار دارد.
@bankrefahkargaran
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/farsna/436820" target="_blank">📅 12:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436819">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/farsna/436819" target="_blank">📅 12:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436818">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62fe7d131d.mp4?token=u4shJ7VfCqCFk48-SBbpzr6Xjruo9cqiix5nAD2qwTsE93Ltwl1SvqYRwNDvffR8jO6DQbT0dJ-ojRp1OrHFXoqnvz1220DvIwZPfprgW5H7IuAaG6MYNm9qIzZkqxzhXPtli9DJCPHPZsa0S_sRWj6EI7zRxuw8u1q8yKlRAjMMX435rSu2j3hJYOguBkmonziC4wrCiJt2kkmDzMAq0abk0sNRDLDo4LEEZIC4oy7r-4qCVkLr_uLXkhXiqx4M3Tg_sgbd8_jKq5h-q3I1N0fZxtWIUWpWcLOWN5PBHF0Iw3wQlbCpoQf-DtEQoAk43F1AFmCZoMo4Qo9WUM4u3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62fe7d131d.mp4?token=u4shJ7VfCqCFk48-SBbpzr6Xjruo9cqiix5nAD2qwTsE93Ltwl1SvqYRwNDvffR8jO6DQbT0dJ-ojRp1OrHFXoqnvz1220DvIwZPfprgW5H7IuAaG6MYNm9qIzZkqxzhXPtli9DJCPHPZsa0S_sRWj6EI7zRxuw8u1q8yKlRAjMMX435rSu2j3hJYOguBkmonziC4wrCiJt2kkmDzMAq0abk0sNRDLDo4LEEZIC4oy7r-4qCVkLr_uLXkhXiqx4M3Tg_sgbd8_jKq5h-q3I1N0fZxtWIUWpWcLOWN5PBHF0Iw3wQlbCpoQf-DtEQoAk43F1AFmCZoMo4Qo9WUM4u3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تحلیل‌گر مسائل ژئوپلیتیک: بازگشایی نظامی تنگهٔ هرمز غیرممکن است
🔹
کمپف: نمی‌توان تنگه هرمز را با توسل به زور بازگشایی کرد؛ همه دیگر توهم تغییر رژیم، سرنگونی حکومت و امثال آن را کنار گذاشته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/farsna/436818" target="_blank">📅 12:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436817">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fa09da100.mp4?token=vyNfJjyUxS6j1rSmVBFv6U8EH4llmcmy8bSO7bFiJvigGmHprMn1TL4zAHbgSi1ttt9rbYBFtgJLox-70H1ZPmxNRUiomQch_UBsPldHvfIprr4JJQ7uaNACfQOO2-RqMmbY2PJP1RawGVRHA9xNKrtcEhw570xc_Wd7ToYanHGIILYHtnL8JieWQCSsB75eLnnftpm2tytH5zvfg8JKyZvPv4hbw4IidYUgrN6hH1GK-9pj06ULl1yOBilX9YTgcT-ilXjP8nFwS7hV7bWL53sG4wHcmsMIQeqIusbqufzCuqmbdBx6gNSwzNgNmz1vHxiGOEzcwkW0V-N6sXQpDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fa09da100.mp4?token=vyNfJjyUxS6j1rSmVBFv6U8EH4llmcmy8bSO7bFiJvigGmHprMn1TL4zAHbgSi1ttt9rbYBFtgJLox-70H1ZPmxNRUiomQch_UBsPldHvfIprr4JJQ7uaNACfQOO2-RqMmbY2PJP1RawGVRHA9xNKrtcEhw570xc_Wd7ToYanHGIILYHtnL8JieWQCSsB75eLnnftpm2tytH5zvfg8JKyZvPv4hbw4IidYUgrN6hH1GK-9pj06ULl1yOBilX9YTgcT-ilXjP8nFwS7hV7bWL53sG4wHcmsMIQeqIusbqufzCuqmbdBx6gNSwzNgNmz1vHxiGOEzcwkW0V-N6sXQpDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرار فرمانده سنتکام از پاسخگویی دربارهٔ جنایت مدرسهٔ میناب
🔹
خبرنگار شبکهٔ اسکای‎نیوز خطاب به فرمانده سنتکام: تا کی می‌خواهید پشت این ادعا که «تحقیقات ادامه دارد» پنهان شوید؟
🔹
تیمی از شبکهٔ اسکای‌نیوز همین الان در میناب هستند. آنچه آنجا رخ داد را دیده‌اند. هیچ مدرکی دال بر وجود پایگاه موشکی در آنجا وجود ندارد.
🔹
تا کی میخواهید پشت این ادعا که تحقیقات در جریان است قایم شوید؟ حداقل بگویید تحقیقات چه زمانی پایان خواهد یافت؟
🔹
فرمانده سنتکام به‌جای پاسخگویی مسیر حرکت خود را تغییر داد و تلاش کرد با کمک محافظانش از دست خبرنگار فرار کند!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/436817" target="_blank">📅 12:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436816">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Da05Mgi9PDMbg6QlgEh5RujgZ2Ges4n11dXmLhyJq-N4YFzN5KhWCF_K0H-H9BdOyZgiP5ophdClZRvBpnwWaDAN-AnHThLVGNq5qjxPBSeREgSn-B_0PdHuOgJHmxxRgYOUC4sOBIClnTe_rrc9XHbDcxQKWqOMhVD5H4UVOLjz1wyY2RV82IQarxjBelvvZh9i7WFOaRQBGc7QZCcZP6T556BaN23QQ_nziG7jt5q6xPTpBulKG9A9Nj7Iw4xor-oDuXoashUE7yhAWJrBMsMwx_xV9uSz4TfqHRcIW3E-iwOpDfTOkKRggcjkUweR1FjhdA16iCZYEn7GOOchNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تداوم بازداشت ۴۱ عالم شیعی در زندان‌های بحرین
🔹
جمعیت وفاق ملی اسلامی بحرین: از زمان قطع ارتباط با ۴۱ عالم شیعی بازداشت‌شده بیش از ۷۲ ساعت می‌گذرد؛ امری که نشانگر ادامه جنگ سیستماتیک علیه شیعیان در بحرین است.
🔹
رژیم بحرین همچنین ۱۰ شهروند را در پرونده‌های…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/farsna/436816" target="_blank">📅 12:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436815">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس نوجوان‌</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0486d5e9bd.mp4?token=scblDeOmmDFKYLaESSU8fh6HvGomkR4ZZyvv_7f8zJvJ_w5uTZ-B90mvK3tmv_D75vlgJariWBkdMvFzvh-EuBsV494bYFFm-bErJXCbqbl8DZZsAPZHoevZ4Gl3dfyzDhQ9WBlWMY0bNpFl1EcpkZi6N9L5q5tdQQ2Pnl_FDL-Y335JtelVHMkfimb-SrWPfgnp84a56jQ8273wLZ-vJAlpZjVxT8SiXu2FCdxNN1KlxVRJQdoDBgbFM5CwEwFke9sZKaIZIrgqhnqq2aGIr6jpQgGdNOvhakLbsw1GEiFtpkFI8i69zWgJsNhXxWPaC2p8OctV0GbaHBbtsb_nBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0486d5e9bd.mp4?token=scblDeOmmDFKYLaESSU8fh6HvGomkR4ZZyvv_7f8zJvJ_w5uTZ-B90mvK3tmv_D75vlgJariWBkdMvFzvh-EuBsV494bYFFm-bErJXCbqbl8DZZsAPZHoevZ4Gl3dfyzDhQ9WBlWMY0bNpFl1EcpkZi6N9L5q5tdQQ2Pnl_FDL-Y335JtelVHMkfimb-SrWPfgnp84a56jQ8273wLZ-vJAlpZjVxT8SiXu2FCdxNN1KlxVRJQdoDBgbFM5CwEwFke9sZKaIZIrgqhnqq2aGIr6jpQgGdNOvhakLbsw1GEiFtpkFI8i69zWgJsNhXxWPaC2p8OctV0GbaHBbtsb_nBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگر دوستمون تو ایام جنگ احساس ناامیدی و شکست داشت وظیفه ما چیه؟
به نظر شما چرا بعضی ها نمی‌تونن واقعیت صحنه جنگ رو ببینند؟
جوابش رو اینجا بخونید
.
@Fars_Nojavan</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/farsna/436815" target="_blank">📅 11:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436814">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeQXVz1vwaWydDDZ3tf-HwVH7t13FF903OKbwEoZF0PDXR6KxumeOXy6yjCTtiJOuBDeaa2GSmfbvTrXVZ3I77f6yw2UfzpDLLL46IMhu45CLj-y12Xlk6Tf3z0EFSpJpBsfD0HE-PqVNfYoxKK19S5mYhco09xujRqk0a9cL7c35SV9sd3LkD0bDjijy8OFqbzF9L_I0Fk_hIaFQWLi7eREYjzC4xXj0VjFxPz-KOgY6BbsxwI0nQ04s_teU0OYSaJEXfOWKFC53xEGCXRRSZPkOVfWRPowxBlB9Wq9bKlhQJIynx2TAbG10WKzmZVs0lprf2FIXyUdaRiBj4vQIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصوبهٔ جدید قیمت چای اعلام شد
🔹
براساس مصوبهٔ جدید کارگروه تنظیم بازار کالاهای کشاورزی، تشکل‌های مرتبط موظف شدند با هماهنگی سازمان حمایت، قیمت انواع چای را به‌صورت دوره‌ای تعیین و اعلام کنند؛ دولت همچنین بانک مرکزی و وزارتخانه‌های صمت و راه را مکلف به کنترل بازار چای کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/436814" target="_blank">📅 11:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436813">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiwIlKZqCCa6Ku0qdb8Q3ZcVKb98RLLEGa5834EhvtUIkc9hZUy4-J-Pgv7EjtUgFlsmpZGzEQyU8CPfOHt3slz-ybVEUOBNsQGZzRLNzlEwvLBTScGcgM1QC3fgWvMUcHgGQ-Zb6nnpAX09VoveSPlIIH4Ygh3qyeWGjqUsltoy4nhhYQqR4R2Sz3LIuknUz-_FppRiOExema1utTXTQuH5xmqrAItz0dS1O7-X-eiQHeeKZ_0RK_Ap8TO8YCBXkszfKcP92QNaVbzcbVMx_JpnHVfj1wcMmn6EX1umFbbmcL8zPIMGVeEt6-CyEzZUObLNP9P_vHgQEN_0PPa42A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شی و پوتین حملات آمریکا و اسرائیل به ایران را محکوم کردند
🔹
رئیس‌جمهور روسیه ولادیمیر پوتین و همتای چینی شی جین‌پینگ امروز در بیانیه‌ای مشترک حملات نظامی آمریکا و اسرائیل به ایران را محکوم کردند.
🔹
در این بیانیه آمده است «طرفین اتفاق نظر دارند که حملات نظامی آمریکا و اسرائیل به ایران، ناقض حقوق بین‌الملل و اصول اساسی روابط بین‌الملل است و به‌طور جدی ثبات در خاورمیانه را تضعیف می‌کنند».
🔹
دو طرف در بیانیه مذکور، بر ضرورت بازگشت هرچه سریع‌تر طرف‌های درگیر به گفت‌وگو و مذاکرات با هدف جلوگیری از گسترش دامنه درگیری، تأکید کردند.
🔹
آنها همچنین از جامعه بین‌المللی خواستند موضعی عینی و بی‌طرفانه اتخاذ کند، به کاهش تنش‌ها در منطقه غرب آسیا کمک کند و به‌طور مشترک از اصول بنیادی روابط بین‌الملل حفاظت کند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/farsna/436813" target="_blank">📅 11:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436812">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjLL6LocSXjjw8ujAxiQPEt0pBqQnOI1ZXTEJ2KihcPj-cHFVWbBDppJyxdRC0ThWtkT4krOjSxj9U_sNcidHxETXqLPEHcGrcPVK_0bS0a8XC3tEvbI9KtTgL4Q9kOzAOHGcACIBBk7L_Vmt2pAEXgDf1YT6tkDtG82gudr6g6QThcEhzEGl7cE_BAsT7ciqwkEXiqYm73yzL-8wk-VQyVMK-g5B7bwbEGNrRBvWq9jiepx9JF1aVQfIdilBY0JY1TAwzwL8WJ4OtYBrT6tWqXdxYq-pYtcKLWI0vUgrcB-fp77k5uHFF4A06ARij9aVAgijtS4oKBDoMYMChY8WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خشخاش به مزارع ایران برمی‌گردد؟
🔹
شهریاری، عضو کمیسیون امنیت‌ ملی مجلس از بازگشت دوبارۀ خشخاش به مزارع خبر داده و گفته «خشخاش ارزآوری خوبی دارد».
🔹
سالانه ۴۰۰ تن تریاک برای تولید دارو‌های ضروری نیاز است که به ارزش ۷۲ همت و عمدتا از کشور همسایه وارد می‌شود.…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/farsna/436812" target="_blank">📅 11:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436811">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkrAxqZoym1ucVtrjzTb_knN6avyxAUkrMrOTEgHVoe5sDyvNChvJktKxNg54_bozjrQV9zb34bgKBUIVVYYrLjZ0G9MToGCtvPqRHlwPRMG2zcY7_IHx5JBQ_5x4zxSJl0o433qv0BxW6qLaSkmOtibBK4KFRRJEyH5ntP5U-cOzFeJvT0shlIdGxBwhSbQ6sI2Yc9Tm--cbySX2XnA0wsKg_dH818uQLe8X81Kq_-Hkpd_nDpnHbDhbN4NLrpOad0clC1UlI18yNxliPpE2KoS2Fcd6_J5_4xGhMlhL6LYcLCKTtlEb-slvFI6SiytITg2_Tu9F8nnszP47KMy1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس اپوزیسیون اسرائیل: روند انحلال کنست را آغاز می‌کنیم
🔹
یائیر لاپید در شبکه ایکس نوشت: «با همکاری سایر جناح‌های اپوزیسیون، اخیراً تمام لوایح پیشنهادی را از دستورکار کنست (پارلمان رژیم اشغالگر) خارج کرده‌ایم. در غیاب اکثریت، ائتلاف قادر به تصویب حتی قوانین…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/farsna/436811" target="_blank">📅 11:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436810">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoYSskMuQeo3G3AAwReidsjY8qrFX8MLrkeqAoiLN12eYY5WbFGNPzW-OkILLESm2_cKXAxS_bgifVUMmZW-td0qiBfb5le9g8ujM8NvLu89hu9SWjXg2ZYoZCIRof9Ux9TB8PNZ4mDnxSuFx3RgVMSV8xrQYGYjNe5Tedm3IGY1hmcYN8lzI1ZpIPzJFP5DEbiSsUbXrjFRMdwrmakdZtqOgT5djUG6DmKV1dPrZ79roAMvg95A31s78KlYqkfWRRgl2VZqlBaC0SM59Rx9UeqRqjqrLoVRjaQGtAmMN4jodUgkXRvMZBcufJB6VsGvVj3aFaOIAgAVa99v8GcB3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده قرارگاه مرکزی خاتم‌الانبیا: شهید رئیسی با روحیه‌ای خستگی‌ناپذیر، میدان خدمت را بر هر مصلحت شخصی ترجیح می‌داد
🔹
پیام سرلشکر خلبان علی عبداللهی به‌مناسبت سالروز شهادت آیت‌الله سید ابراهیم رئیسی: آنان دل در گرو مردم داشتند؛ ساده زیستند، بی‌ادعا کوشیدند…</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/farsna/436810" target="_blank">📅 11:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436809">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
حزب‌الله: تجمع نظامیان و خودروهای رژیم صهیونیستی در شهرهای دبل و رشاف را با حملات موشکی هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/farsna/436809" target="_blank">📅 11:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436808">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromانتشارات فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTJcqX7o7EszH-4gkJRA-FV0-ZuCV59yjUldkGx125xzr4VqsnFlrV0BOZB3VzmyRWA5f2lz7lnxPBVIf43NabgxiOD7Yn-ctR7nr5_5haVe_wPfFz0hS7O8MtT-gqN7ZxjYk1Ce5i8aqiNcX5Wk5qW7QfLiFui1iOhHxNNbE9zgQgxY-KGaqyC9HdHyaue0wJTw3IwEOYC5gBwCHkVQ85H51Ejk-UkxoAd7P7ZTgQs8XX0iLHkGQkR1BL2wDpjLQ0PAEfx7SMZsOaunvWjzou-x_u19aV5HsPKTRwo0D34srcS4yvBKiDeW0kWXUW_cw5iYJhpoNsvXv7uF3yFdLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
۱۱ بسته تخفیفی انتشارات فارس؛ فرصتی استثنایی برای خرید کتاب‌های رسانه‌ای
🎯
انتشارات خبرگزاری فارس در هفتمین نمایشگاه مجازی کتاب تهران، با
۱۱ بسته موضوع‌محور
و تخفیف ویژه مهمان شماست.
📖
این بسته‌ها شامل حوزه‌های تخصصی و عمومی:
✔️
آموزش رسانه | روایت‌گری | خبرنویسی
✔️
خانواده و رسانه | برنامه‌سازی | تدوین
✔️
دولت هوشمند
✔️
جریان‌سازی در آمریکا و ایران
✔️
صهیونیسم‌شناسی
✔️
علوم شناختی
✔️
تاریخ انقلاب
🎁
مناسب برای دانشجویان، اساتید، فعالان رسانه و همه علاقه‌مندان به کتاب
🛍
با قیمتی مقرون‌به‌صرفه، کتاب‌های موردنظرتان را راحت‌تر تهیه کنید.
🛒
نحوه خرید:
🔗
لینک خریدآنلاین از سایت رسمی نمایشگاه
https://book.icfi.ir
📌
روش‌های خریدکتاب از انتشارات فارس:
🔹
ارسال پیامک عنوان کتاب به شماره ۵۰۰۰۱۶۷۶
🔹
تماس با ۶۶۹۷۳۹۹۶ و ۶۶۹۷۳۹۷۴
🔹
مراجعه به سایت
انتشارات خبرگزاری فارس
🔹
حضوری: خیابان انقلاب، روبروی دانشگاه تهران
✅
انتشارات فارس مرکز جامع کتب رسانه
#انتشارات_فارس
#نمایشگاه_مجازی_کتاب
#بسته_تخفیفی
#کتاب_رسانه</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/farsna/436808" target="_blank">📅 11:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436806">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
سپاه پاسداران: با تکرار تجاوز دشمن، جنگ را فرامنطقه‌ای می‌کنیم
🔹
بیانیه سپاه پاسداران: دشمن آمریکایی‌صهیونی که از شکست‌های بزرگ و راهبردی مکرر از انقلاب اسلامی درس نگرفته و بار دیگر زبان به تهدید گشوده بداند، اگرچه آنها با تمام توانایی‌های دو ارتش که پرهزینه‌ترین ارتش‌های جهان هستند به ما حمله کردند اما ما همهٔ ظرفیت‌های انقلاب اسلامی را علیه آنان وارد عمل نکردیم.
🔹
اما اینک اگر تجاوز به ایران تکرار شود جنگ منطقه‌ای که وعده داده شده بود، این‌بار به فراتر از منطقه کشیده خواهد شد و ضربات کوبندهٔ ما در جاهایی که تصور آن را ندارید شما را به خاک سیاه خواهد نشاند.
🔹
ما مرد جنگیم و قدرت ما را در میدان نبرد خواهید دید و نه در بیانیه‌های توخالی و صفحات مجازی.
@Farsna</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/436806" target="_blank">📅 10:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436805">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">افزایش وام ازدواج و فرزندآوری در بودجۀ ۱۴۰۵
🔹
سخنگوی کمیسیون تلفیق بودجه از افزایش ۱۰۰ همتی سقف تسهیلات ازدواج و فرزندآوری خبر داد.
🔹
بر این اساس سقف این تسهیلات از ۲۷۰ همت به ۳۷۰ همت در سال ۱۴۰۵ می‌رسد.
🔹
هدف این افزایش، جمع‌آوری صف حدود یک میلیون متقاضی…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/farsna/436805" target="_blank">📅 10:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436804">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8vGUTZOJdEdIPTiHlXHozvQ1C0OmKBrtQAeyMRk1mXZ2mo4FNUrIaKkeBQmjrPcq7xE8WcWk1Dd0bomrQ9dYra1FOwRzk6TGj850M0b9JuBc-uhWTVD2Ls2YzjWJCgUPfB-ZaEzLnBrjId424hmHy6HsfoixDuU9Q1rDX2D-ghXpXKrc7YEVqod1Dv5H5e6sWgVmwq2SUaa-_z2d_9I06FlnKkGlLTqdpkENc8IGvyYRXUhLefPy5qSVYNDplnDo4an0hw8D3m0Nls9502eK9spdcgfzrpXFbLzkf3tA5phYCwXv93jx52b0ubUwGwtgOhLLHH-LJcGlwgtee2lpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
همکاری همراه اول و پژوهشگاه زلزله برای توسعه هشدار سریع
🔹
همراه اول و پژوهشگاه بین‌المللی زلزله‌شناسی و مهندسی زلزله با هدف تقویت زیرساخت‌های ارتباطی در شرایط بحران و توسعه سامانه هشدار سریع زلزله، تفاهم‌نامه همکاری امضا کردند.
🔹
در قالب این همکاری، از زیرساخت‌های ارتباطی همراه اول برای انتقال داده‌های شبکه‌های لرزه‌نگاری استفاده می‌شود و پژوهش‌های مشترکی نیز در حوزه هوش مصنوعی برای بهینه‌سازی زمان صدور هشدار انجام خواهد شد.
http://mci.ir/-F4RHS6
@mcinews</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/farsna/436804" target="_blank">📅 10:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436803">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">#ببینید
منطقه آزاد ارس؛ تسهیل‌ گر تأمین کالاهای اساسی کشور
در شرایطی که سرعت، دقت و هماهنگی در زنجیره تأمین بیش از هر زمان دیگری اهمیت دارد، منطقه آزاد ارس با همکاری دستگاه‌ های اجرایی و فعالان اقتصادی، نقش مؤثری در تسهیل واردات و ترخیص کالاهای اساسی ایفا کرده است.
کاهش هزینه‌ ها، روان‌ سازی فرایندهای گمرکی و حمایت از واردکنندگان، گامی مؤثر در مسیر پایداری تأمین اقلام ضروری و تقویت امنیت اقتصادی کشور است.
#منطقه_آزاد_ارس
#کالاهای_اساسی
#تسهیل_واردات
#گمرک
#اقتصاد_ملی
#حمایت_از_تولید
#زنجیره_تأمین
#ارس</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/farsna/436803" target="_blank">📅 10:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436802">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/farsna/436802" target="_blank">📅 10:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436801">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085abd4b23.mp4?token=A9CoDG50RB4l1fVvz74xtm9Pf6H80hQ03V6YK_bxrzz8dIt49oNkU0MMo8joU5qWEVt89csTDZ6j-3LSgQX_5mQlHyZTo7e2rxevYjHUQwCpawjoP3osjb1P9IajweRL2NTcHIo8kGdbJVdVygMb5Z7Xxy2wbG7tk6-e4FoLBIcR_TqWu4W26ayufTpi1ivSsCUVFRSt3qS6S6MWvxISHSah8PsOUuybdiFSoYBYYpQPFAGpNCTbJqiWNebbp5VkXTwmBi07kn7Xw-wJZ4xj-a0tK_v_gNk27Ju3kVpGksdWCXhoyW-jb8YX5MULemMqc_9NdCEFGdtVac69Fz_dLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085abd4b23.mp4?token=A9CoDG50RB4l1fVvz74xtm9Pf6H80hQ03V6YK_bxrzz8dIt49oNkU0MMo8joU5qWEVt89csTDZ6j-3LSgQX_5mQlHyZTo7e2rxevYjHUQwCpawjoP3osjb1P9IajweRL2NTcHIo8kGdbJVdVygMb5Z7Xxy2wbG7tk6-e4FoLBIcR_TqWu4W26ayufTpi1ivSsCUVFRSt3qS6S6MWvxISHSah8PsOUuybdiFSoYBYYpQPFAGpNCTbJqiWNebbp5VkXTwmBi07kn7Xw-wJZ4xj-a0tK_v_gNk27Ju3kVpGksdWCXhoyW-jb8YX5MULemMqc_9NdCEFGdtVac69Fz_dLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود ۱۵ اتوبوس ۱۸ متری تازه‌نفس به خطوط تندروی تهران
🔹
مدیرعامل شرکت واحد اتوبوسرانی تهران: با پیوستن این ۱۵ دستگاه به ناوگان، مجموع اتوبوس‌های جدید وارد شده به ۵۰ دستگاه رسید.
🔹
از مجموع قرارداد اولیه، تاکنون ۱۰۰ دستگاه وارد کشور شده و مراحل عملیاتی شدن آن‌ها طی شده. همچنین ۵۱ دستگاه دیگر الان در گمرک بندرعباس مستقر هستند که به‌زودی به تهران منتقل خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/436801" target="_blank">📅 10:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436800">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">iran</div>
  <div class="tg-doc-extra">Hesam Seraj</div>
</div>
<a href="https://t.me/farsna/436800" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔸
وطنم ایران پاینده مانی
🔸
به رهت بنهم سروتن، دل‌وجان، تا زنده مانی
🎙
حسام‌الدین سراج برای ایران خواند
@Farsna</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/farsna/436800" target="_blank">📅 10:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436799">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktkk2V7CchRX7VTUYVkzyCW7h-1kFTR8RFy7aJSxh4g5-LZQGgaZX7tB_1gY4gSbVD5i8dnvjGmw-QuarCDHubdTk7WP3_UBUca2mCLjEJV_v7xgGuL_veY2NYQnj4kxnCzSNcwymigv8ucVxIHecdmHTUsZR3k343lV20wgku4mFJFhX2ijH-2HBI6mzh-QaimhSKyCC2oCAZTOVyRAbBAgstVMiE9KwQ4ItjwHTYrTa-ywdCn4kDAZ2483fk9hWSoSk5__xFQPrmX7W8Jt4QauCyPATpxZ6APqQrGeDFrQQjneEcBc2Q83_UYd_czaqee56X3VpyQdGlgNm50Axw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده قرارگاه مرکزی خاتم‌الانبیا: شهید رئیسی با روحیه‌ای خستگی‌ناپذیر، میدان خدمت را بر هر مصلحت شخصی ترجیح می‌داد
🔹
پیام سرلشکر خلبان علی عبداللهی به‌مناسبت سالروز شهادت آیت‌الله سید ابراهیم رئیسی: آنان دل در گرو مردم داشتند؛ ساده زیستند، بی‌ادعا کوشیدند و در سخت‌ترین شرایط، امید را در جان جامعه زنده نگاه داشتند و   همچون مردانی بودند که مسئولیت را امانتی الهی می‌دانستند و خدمت را والاترین شأنِ مدیریت.
🔹
خادم الرضا شهید آیت‌الله رئیسی با روحیه‌ای خستگی‌ناپذیر، میدان خدمت را بر هر مصلحت شخصی ترجیح می‌داد و منش مدیریتی او بر سه ستون استوار بود:"عدالت، کارآمدی و مردمی‌بودن"
🔹
شهید رئیسی عدالت را در توزیع فرصت‌ها و توجه به اقشار مختلف جامعه جست‌وجو می‌کرد؛ کارآمدی را در پیگیری مستمر امور و حضور میدانی معنا می‌بخشید؛ و مردمی‌بودن را نه در کلام، که در رفتار و سلوک روزانه خویش جلوه‌گر می‌ساخت.
🔹
شهید رئیسی نشان داد که می‌توان در بالاترین سطوح مسئولیت ایستاد و در عین حال، فروتن و پاسخ‌گو باقی ماند.
@Farsna</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/436799" target="_blank">📅 10:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436798">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
روایت احیای واحدهای تولیدی و کارخانه‌ها توسط شهید رئیسی
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/farsna/436798" target="_blank">📅 10:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436797">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eadf181797.mp4?token=fzMALwRcsemEGMNO3VC4GlPgm9S_q-ZWo_OPmP26fPn7W8-YyvBpGiDsu0ugngOJe8HEvASpVocjWxnYXkDVfVuFiIDBt5adom6Dwba5Ceyqg3Z1uyw8lvAxZv-5UNBtVOPoZNIagOXsQUpbpQPdv6GEPZXyULYwToJ2qIvkv_FWOZ9Bhv3WleeHwEYBM1NNIF5m3FoG4n10x9FDhtCo2KXDbLwquJ7u_vyNUh-kzK-paWY484E0Z6JY4oiKn56UJ5XIYqa0ThrZpt11Obr5WaT_zEeTQaEIwr1196V30dJJpgLvCsWK8PxKZkOwR83-jyuYfMdGwfSBON-woyxnvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eadf181797.mp4?token=fzMALwRcsemEGMNO3VC4GlPgm9S_q-ZWo_OPmP26fPn7W8-YyvBpGiDsu0ugngOJe8HEvASpVocjWxnYXkDVfVuFiIDBt5adom6Dwba5Ceyqg3Z1uyw8lvAxZv-5UNBtVOPoZNIagOXsQUpbpQPdv6GEPZXyULYwToJ2qIvkv_FWOZ9Bhv3WleeHwEYBM1NNIF5m3FoG4n10x9FDhtCo2KXDbLwquJ7u_vyNUh-kzK-paWY484E0Z6JY4oiKn56UJ5XIYqa0ThrZpt11Obr5WaT_zEeTQaEIwr1196V30dJJpgLvCsWK8PxKZkOwR83-jyuYfMdGwfSBON-woyxnvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور چین: جنگ در خاورمیانه باید فوراً متوقف شود
🔹
شی در دیدار با پوتین: اوضاع در خاورمیانه در مرحله‌ای حساس قرار دارد و به گذار از جنگ به صلح نزدیک می‌شود. خصومت‌ها باید فوراً متوقف شود.
🔹
دستیابی سریع به آتش‌بس عاملی برای کاهش موانع پیش روی تأمین انرژی…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farsna/436797" target="_blank">📅 10:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436796">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhbO5TtEEPZkkFgHT0tWzHF1cKhDo3qHHWFwQlN8cXA0mOu8KpjnxqKol9uJzF9TCOEtepQvKi294DL9mbBeTulO5JQzjZpmXhWuBkhIG9FHUmjcvM-vU9vH_VfmoSIA1HnZ_RQDxd-Gu81iObmfub37Y-zvLZj3m3i_edLrrX0LmSDVhMhs6I2qHxgrB-uIBArCQKoywRkBdpEYKV_p4MXGl89Bprg7Cc5CC_H60Vz883FQtOQPDLfYJOxvTkJZLnlo75VDXa5B-RDKnmxm3yLbliLIN-K_di3cnjLDbCyi8kdr0aFYsOTXBXVUO9rxY1X0aZDfODVHcvN9lVXumw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور کیفرخواست پروندۀ قاچاق خودروهای تویوتا در گلستان
🔹
رئیس دادگستری گلستان: برای سه متهم پروندۀ باند قاچاق سازمان‌یافته خودروهای تویوتا کیفرخواست صادر شد. پرونده برای صدور رأی به دادگاه انقلاب گرگان ارسال شده.
🔹
متهمان خودروهای تویوتا لندکروز و تویوتا هایلوکس را عمدتاً از مناطق مرزی کشور به شکل قاچاق وارد می‌کردند و مشخصات و اسناد خودروهای فرسوده و قدیمی را روی خودروهای جدید ثبت و سپس آن‌ها را در بازار به فروش می‌رساندند.
🔹
در رابطه با قاچاق سازمان یافته خودروهای تویوتا، سه باند دستگیر شده بودند که پروندۀ مربوط به ۲ باند دیگر همچنان در دادسرا در حال رسیدگی است.
@Farsna</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farsna/436796" target="_blank">📅 10:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436795">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaWe5G1FwXHgsv24cRUmIhfsfFooMaDT5Hvt56qnWWPGKZ2prXk1UuNt1J_E9HCVwfb_kUk2R4KsykWf43J5p-ZO0cfG7FIDdN6wiWTzdoUa-nfTeroT17jjzd4ovN75DdWRTOgE3xGcT6JAithDLDn8eVDJlF4NtSYdi_kcANyXBoUcbckj8ZH5WeZQnRTIb0PXrHav67bNBYgiMqO6LRKosDm2M_VMqq__3nzygPEbdJODQAZ-Akea7JWW_ZSJTOIl77XaZN1rtAqMkVWO6_mrD-hwa2ak_vuIP28nPeQjsTTm8teijFyGfS4CoDxLkoAuK9uH0bxkC17uwlwtgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ راهکار برای کشیدن افسار افزایش قیمت لبنیات
🔹
بازار لبنیات این روزها در تب‌وتاب افزایش قیمت‌هاست. برندهای بزرگ طی هفته‌های گذشته نرخ محصولات خود را بالا برده‌اند و برخی دیگر از تولیدکنندگان نیز در صف انتظار برای اعلام نرخ‌های جدید هستند.
🔹
در سوی دیگر، اتحادیۀ…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/436795" target="_blank">📅 09:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436794">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">انفجار پهپاد حزب‌الله در ساختمان محل حضور نظامیان صهیونیست در جنوب لبنان
🔹
رسانه‌های عبری گزارش دادند، یک پهپاد انتحاری متعلق به حزب‌الله که با فناوری فیبر نوری عمل می‌کند، در داخل ساختمانی در جنوب لبنان که نیروهای ارتش اشغالگر اسرائیل در آن سنگر گرفته بودند، منفجر شد.
🔹
این انفجار منجر به زخمی شدن فرمانده لشکر ۴۰۱ و تعدادی از نظامیان شد که با هلیکوپتر به بیمارستان‌ها منتقل می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/436794" target="_blank">📅 09:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436787">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VkrQKl5TC3MhR_TDGK7q-WS4a3C6TuHRxf9CMHCYb8z3bGFQBAcyKUCW-J5MIZrmbh04YqB85wPq1Ev_xap228lL-nT96BZJK6j1UWr_xXlsbiertxkxUTpM-rST3oYFM-QfE22veLFhJqH7fdbCSnomPxUwm6hwfdco4xa_PnKb1C0qx1R8iaIXRq0bHrRDXsJeqTR38QB2PMROEdwrYKwBIIEsLFKFle3zfosMYbT9PDaaHpTcWHXrFLaJklJbERZu9-jWZE2tgR95syxLANJad31K8gkOwItJxa8dXiGmx6kBMNLIlIqr3LXUScLi_-qJT5PDpQOtMqiWKN5ifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X6qGhEZFqKVuYiQ0wF68vJAhc-pVjlcIgRjYpE_hh8RxjMNZ2tYIU8Mbxvt2-ce3cvwPZkEArZES5jqi-D7abuVv6I8ntjp_9zMo6XA4Eu0LQdNVp8SEAdhLWrB5dsrxJK-8SgiAbJBAFbfhV3EeIBs37h-oAIPy8BHR4S8G9B4_iIC4e55T7PmgAwV3Ddz_ePcYVfR-KV22axf2A8vqKyRoed9kWY8wSU3x39MojeRp4OQ6E5GbgZ9EniXzVLyUJFF41vJPREGJUpelA1GN-8oiKH1g8T-cFDL1xDoXaC6UJbqHJeLQic7kACPvOfAtgJi5qDpDMX0QFJC7a9-Q7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXWPiIs3UnVQ0RAQXIiU4KIguBZ7H_snrZ64BOnKJi2dsV4Qn19E3h2kT40MjUO0WVNHvV3FdaJHBxCySfRdySY8awE8Q2B4vSuo6-UNqmPJwL9t26JyCtzGBcjd1glSy3Y3OIlVisKDazkXL5gxhAm9lfpFE0Fof6YbHFas3eKVxKKo9HKFHUxDfgK9hY9Pl7AL5uHVoNwSrf7FzMbiC-2sSUu4yxQHiObZdAgimrl_iqA0jDVoKJxfFfl-pagF_aQmk5wabF9PIazAQJdOL3ApowvWdAbno1FIjMh5C-1woNuU0MuxX5XFxlbNv6liMCYI8W5sY02piRoeUTFlyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H-nYIhOg8yyu3Gr0Be6sJy2Wpgz2sWZ_0-36gXPXdS7FF3Cn2lCITLhKbOpANmdMhZwepej0sITNz8b-mR85VShbIkNgthu6Y4CkXN_3g-RZlN-6zHobxaXuH8KJrTBIk8uyzxzqOXNBxBnYx4omkc_vCn8eP6Qm-XRJGEYDJX0ZstLxRANFal1QFXNKSk8JKiM77kXPQLyI_wYY3gj5ho5xMhv-REdmUGux-kHfNPposaLK1hdyUoUWSg8m2nlUyAi7jPt7zAa5soGnmXQF85P4BUC5lBHKWQjvPL6iM_uEzxAHYYnDvRAqiZO1yShf2_u15M0uT5nvG_gSAqHTRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tCYCTTRU2HOgp7lW3ByMDNINt07fDP3v04qn0z--2wuMWIu5tB4ufBisogI53shD1iKOxTiM0h24yzgDK1aBDQ48IdifChYbaWPZXAFqo6-tq9NOjdJcP_ACu_yIEprYJKTnNDHdNG0sLJLFfuN38g_JILFrWTeVM1T4uN-avqC9osowFt0rzDuwElnpQ7BOJW-7vPOhw1723QCjjLrWYBym2dz8FtjhoKPpII3SDc7QJCOXBpT7CfuhHTslEXxJeqgEvoCrrDIfScf0EWJWXXiyrZ_k_A1jDs_foOD6HAuApTmc6vlNfdJ35wkA-Kk0DwONmZANJaY7BKy_cS-qnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gIjqefDxGIa5h__QdFBL7J7eYnfctNcJqGhpTQtHNGMFs7cxOSUUSQ24EeW2fOVHrzchK6dErWUjU-2cYpQOGItj80-rVEePVXUytIeyMzVaCXyj6mUJJ32guZQbZ4s4wttBYppwiGnZXGMKprn8XnNJkx8TqaAskZ2gRYyPl6I41rTL6cm8QPWkwh2zmv3_eiPsgyzWnrxMbkCGmq2StcHjwrZ7ECQsjlwsUwT_hsHENFDmUeNI-rLAtc2J-WpMOXQeLvVkgypa7vHtOYxHhh99wmQoH-V9PTIwbs_qlQ5eKuev-5uRImsVoOiLeFPAms1y1ssZXCoVwpTYibFyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YHncBNJvAE4HNan7LFuebP8uQ7nex8tN7A3h25p03Cu6FvBfGkkfeZvi_rJMMsK3r3N_SZCWasTSC78QVGZaHlbFx7hVirs9DOo0ObCQtAzSYzm53zTv26tOvgiFSv0a8qZOQi5XW0YCCMsnsGIT6Y6xWu8rUlfVvF_lmKsy5s9q_A1HlGTPBW-fWr-_4xhA8_oO2jWWAy94YypNBLlSBB0OQNa-gAnJUppDsw7tutT6LiXQJKMK1buqWmtXP6cZ_qGkkCHUFWXaKUpBS42UtcFCuqpbZ9JsC5jSisN3mzPvLBaH0pUSJ443eqRoXvduTmz0ZqrJ2D7AHtfz4nVCiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس‌جمهور: با روش‌های گذشته نمی‌توان بر همۀ مسائل امروز کشور غلبه کرد
🔹
پزشکیان در نشست سراسری استانداران کشور: روش‌هایی که تاکنون برای اداره کشور مورد استفاده قرار گرفته، در شرایط فعلی به‌تنهایی پاسخگوی همه مسایل نیست.
🔹
ضروری است با نگاهی نو، روش‌های جدید و راهکارهای خلاقانه برای عبور از مشکلات طراحی شود.
🔹
یا راهی پیدا خواهیم کرد یا راهی تازه خواهیم ساخت؛ اما لازمه این مسیر، رها شدن از قالب‌های ذهنی محدودکننده و نگاه‌های محدود در تصمیم‌گیری است.
🔹
اگر روش‌های پیشین به‌تنهایی قادر به حل مسایل بود، بسیاری از مشکلات تاکنون برطرف شده بود.
🔹
اگر برای مدیریت مصرف آب، برق، گاز و بنزین برنامه‌ریزی دقیق نداشته باشیم، در ادامه با مشکلات مواجه خواهیم شد.
🔹
باید مردم را برای صرفه‌جویی و مدیریت مصرف به همکاری دعوت کنیم تا بتوانیم کشور را با عزت و اقتدار از شرایط فعلی عبور دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/436787" target="_blank">📅 09:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436786">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cF7akLwf00GOuW4YmEJXUI7ferePREWMgibnlUprzkKlIhCo67VNMdDhp3SlU6ozOl1vXuWWo7gfJ5NcRA97Ru2DjI_TevmoVCpahfV8cHggjqaV67hzXjWRd6o3zG-HyA0brV2NEhOat8_KiX479winMcZJfp64j8uCAKERquO6UxPDq3s0V4h5IqOhxSBemCSj_mY8s54ieUrY9HT3DZB-iESN00Pz3R2nMlW8GqVhfjv7GzLsHWk4ua5Osz8aMTpl5icDGKy9To8HzykwXotNCMBNlxaugUt7Kb_hiMbOrw0ersPC1lePLhwDY2sokkPS8DVJ5f3zuyEQwiKBYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گواردیولا: آرسنال شایستۀ قهرمانی بود
🔹
تبریک پپ گواردیولا به آرسنال پس از قهرمانی: به میکل آرتتا، کادر فنی‌اش، بازیکنان و هوادارانش برای قهرمانی در لیگ‌ برتر تبریک می‌گویم. آن‌ها قطعا شایسته‌اش هستند.
🔸
آرسنال پس از ۳ سال نایب‌قهرمانی پشت سر هم و پس از ۲۲ سال قهرمان لیگ برتر انگلیس شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/436786" target="_blank">📅 09:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436785">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/660ce9d7be.mp4?token=FIcqKNs30HBAqf7OaN2yYncT35klWblOal0yXsVzEuxh1CJ317CA-7E0aE1jjD3NjEtBzQ_t_JUmmX74L4JiU1u6csqhnW2ztHCWdMKy4a7i_tJ4bKCfHrEo7IFWJBxooSTXY2EYlVgU6PGR5HHEqp-XDLw3OgrQqVmOnSw08uRMKPBZI_qcmPGn7lYOtPhd33pUOp9j9tYuTRS5Ffpfvph8ybLZvy-nbYANkDMdtJzvfEJn2e6PhaGulYYpTZcsPc3WgdgPMd4JHrCv8Wgj0B5OVwMx-wqtorW8ORzZAzZBDp1FXtGi4trsGp5uED2xxzQ2PNAXXzu5CvNYCMQnDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/660ce9d7be.mp4?token=FIcqKNs30HBAqf7OaN2yYncT35klWblOal0yXsVzEuxh1CJ317CA-7E0aE1jjD3NjEtBzQ_t_JUmmX74L4JiU1u6csqhnW2ztHCWdMKy4a7i_tJ4bKCfHrEo7IFWJBxooSTXY2EYlVgU6PGR5HHEqp-XDLw3OgrQqVmOnSw08uRMKPBZI_qcmPGn7lYOtPhd33pUOp9j9tYuTRS5Ffpfvph8ybLZvy-nbYANkDMdtJzvfEJn2e6PhaGulYYpTZcsPc3WgdgPMd4JHrCv8Wgj0B5OVwMx-wqtorW8ORzZAzZBDp1FXtGi4trsGp5uED2xxzQ2PNAXXzu5CvNYCMQnDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: هشدار سطح نارنجی برای شرق مازندران، گلستان، خراسان‌شمالی، ارتفاعات شمال شرقی تهران و سمنان صادر شد
.
@Farsna</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/436785" target="_blank">📅 08:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436784">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hskQqzU62d5wOorfg4x8Yw3jiUyyY9-2JTbW8ooSVHLCbdg4fxDVPhj660pawCXJ1GN-0309SamrjNSYotUObEK0Dr3HqW-u11i2WRTQj-RqcBdi7945GVHX27LFjEurOCP8R1ZWdP9W56BtenINp0BPkx08nncHpmH5_ewj7zN6Ho7yNOmGJJOtzcP4oiHiFpUDmF-vFEWMF09n42Z-cjcw-9J9Hna11O2kf2PukbVjkRPsuWEIcDyi2KczxCIp05Wc0Bzm-B1gkoVLQspk9xmzJF8G6Kv1dUSiY1DnynTtDhOHzXnu0MxdVPQNYSKa2Qi1m3bFFtxefkB4BZ_chQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوم‌گردی بسازید؛ برای هر شغل ۴۰۰ میلیون وام بگیرید
🔹
مدت‌هاست فعالان حوزهٔ بومگردی خواستار افزایش وام برای ایجاد این واحدها هستند و حالا معاون گردشگری کشور از ۲ برابرشدن وام آن‌ها خبر می‌دهد.
🔹
محسنی بندپی، معاون گردشگری کشور، به فارس اعلام کرد: «در سال ۱۴۰۵ مقرر شده است به ازای هر شغلی که در قالب احداث اقامتگاه بوم‌گردی ایجاد شود، ۴۰۰ میلیون تومان وام به متقاضی پرداخت شود».
🔹
این رقم سال گذشته ۲۵۰ میلیون تومان به ازای هر نفر بود و فعالان بوم‌گردی بر افزایش آن تأکید داشتند. اهمیت بوم‌گردی‌ها به‌حدی است که در ایام جنگ رمضان بیش از ۴ میلیون نفر در آنها اسکان داده شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/436784" target="_blank">📅 08:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436783">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6e2f3eeaa.mp4?token=IY1zMeX6v_p1k0zYsM0XoXP2xq3JwaNyLP4WODHwQxa5dOD4ERRPwixcsLS1m7U0d3-Q22AR74A4yItBF8gpnwZa93RqBGnwERtURXgzeALk87THM-iO9Wzuh02pn5SY7klv2IN_HRSuQ2SjS4eBUxBJETNk0Aqn1ZpTAsQYkyPlgBuONchfqkdroPuIPNI3e7KKHwW5QAvi0Efkomd4B68_MbuOUdJCxFnIas9dxdxAJ9nMB0wKUj5hhB8jNq7wzBS6VYjYEj2sfFlp14Rg3Ak9miqaMoQ0LngRXkypM3zT-aVr0RAJWppAHR1DTXgb8yPpBSgC7OuCksLqAchO3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6e2f3eeaa.mp4?token=IY1zMeX6v_p1k0zYsM0XoXP2xq3JwaNyLP4WODHwQxa5dOD4ERRPwixcsLS1m7U0d3-Q22AR74A4yItBF8gpnwZa93RqBGnwERtURXgzeALk87THM-iO9Wzuh02pn5SY7klv2IN_HRSuQ2SjS4eBUxBJETNk0Aqn1ZpTAsQYkyPlgBuONchfqkdroPuIPNI3e7KKHwW5QAvi0Efkomd4B68_MbuOUdJCxFnIas9dxdxAJ9nMB0wKUj5hhB8jNq7wzBS6VYjYEj2sfFlp14Rg3Ak9miqaMoQ0LngRXkypM3zT-aVr0RAJWppAHR1DTXgb8yPpBSgC7OuCksLqAchO3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فسادستیزی شهید رئیسی از دستگاه قضا تا ریاست‌جمهوری
@Farsna</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/436783" target="_blank">📅 08:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436782">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2ZuoddDJ8Qv5d66_3YMuTSeD8w0p4FXBmh9cSAnYPpwvUA6TS_YkFbUmyANgPYeKzxMh7w_4W1TwqVt4Vh2w4gkpXD0EvfGKUwb7RL60Eb35J7NTCVzJLQ57q3QHMPa24WoYillgR8982SUnKq7qFDOKDGdS5sZ9dD_Z6-5Mcnq9IiBPUatYLHKHhz1ztXvOZL8CkltzaxFynRkxv7UTV83Sq_fqlUCOAc6lKzQNHXLjdxQeOi-W1mZSdTQVKK9XVMPtQpMOW0o--cBCeVc7pkJPshzBiwxnO6bSD8JuUDyhvFCwHnLzp5ysDN_nls887gRfogGXsPKODi_fNy9Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تصاویری از استقبال رسمی شی جین‌پینگ از پوتین و ورود به «تالار بزرگ خلق»   @FarsNewsInt</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/436782" target="_blank">📅 08:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436781">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کرمان امروز تعطیل شد
🔹
استانداری کرمان: به‌دلیل هجوم ریزگردها و آلودگی هوا، اداره‌ها و دستگاه‌های دولتی استان به استثنای مراکز امدای و خدماتی امروز تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/436781" target="_blank">📅 08:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436780">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nl-7LaErpqkuCJJzEZN357K2rmPK1CVkfvieQps9bY2byJcU82Z_8370t7KC_4vFI2PB19fXG4-s-YZRSVaHqtbXBIjtlfjRlNCwqW5ZlC6mRAfKlchhsbm5PoJbxOeVJREPunPjjwp68v3ph8wpCvUHezSFgEKQJWqklsdmypvlXsjwoD21fabSz5iY0yqV51FVHSzCHdjHu687SjB8qafDrCei5JHTWqMAcfK4QU3cZ9CTVMef01cucE7F9jgC761TtU8HYQUZymFfLkjklCSavPmSY7lghh96vzOTlqMdyOBeoFxBWQAOyAso5573UI8vCmBOVOaUGjJ-rc6G7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروسی به منطقۀ غرب آسیا سفر می‌کند
🔹
مدیرکل آژانس بین‌المللی انرژی اتمی: از سال گذشته، آژانس اتمی در حال جمع‌آوری اطلاعات، تجزیه و تحلیل و ارزیابی آمادگی و توانایی‌های واکنش در شرایط اضطراری بوده است. من به‌زودی برای ادامۀ این‌کار مشترک مهم به منطقۀ خلیج‌فارس سفر خواهم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/436780" target="_blank">📅 08:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436772">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4930b0111.mp4?token=HXLDZgGZRuhfCDi7ksXhIuJ4DhaDmXbm5BM3Gw_EVh_VuYszB5nfLtq7lvRyguU-qgD6V-oOGjZE6z4wucqcybTJB7-sUbQaKo8PodqmwuCfLt2wfBhNqtwph5Xn-P8F98YXVPKMXRnSQtm-eiFAQp5RMX5l_3iz0yC41gsBHKSp3yPG-QZ6crGeqGnI87xbQqWZBFqirXPsVzxClpccV8MCgmLeA9FCct_Kj9CP3WvCLw7hEv3VNl9xxdgtCIhbIWRytgtx0DMtYdObC-uC0lQw5cVSGYBH_O3kSvpvPOP1QylTnYn1ZWqw18gZMBx0SboYSeIp4BT3K8Pw92_lWxnT4aqBMU2O5J3PWuK-SSblgqr5G7S45O9XC0YeJJRLCuEx6y7IpPbsmY0zzO0wAx4dBgzQcgrvSQcyDdg3jc2I45o3_xL6trwe2DF3YAWR0BAXI54WxKmIM-uIiya_T9fiRUHQ2GIzrJ0oMYcAgudwe1TDaG7YmhFTKcHiS9OtaZrTXljqvKUeJ5POQeHKzWJoMd_ZMLi7BrD_0u9O2VBF2Bd36neJ-R9qheHnNc1pA_bA1-c5QIAoDSIbF1Pf2UkkzrBWbPGbYsRGrGarqrzl9HcOeY-wTCMFXqrORVtJc6lLzJkp-bW2zHoFIUz_ydjG6SeA2ZlKy2ShJn_c90U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4930b0111.mp4?token=HXLDZgGZRuhfCDi7ksXhIuJ4DhaDmXbm5BM3Gw_EVh_VuYszB5nfLtq7lvRyguU-qgD6V-oOGjZE6z4wucqcybTJB7-sUbQaKo8PodqmwuCfLt2wfBhNqtwph5Xn-P8F98YXVPKMXRnSQtm-eiFAQp5RMX5l_3iz0yC41gsBHKSp3yPG-QZ6crGeqGnI87xbQqWZBFqirXPsVzxClpccV8MCgmLeA9FCct_Kj9CP3WvCLw7hEv3VNl9xxdgtCIhbIWRytgtx0DMtYdObC-uC0lQw5cVSGYBH_O3kSvpvPOP1QylTnYn1ZWqw18gZMBx0SboYSeIp4BT3K8Pw92_lWxnT4aqBMU2O5J3PWuK-SSblgqr5G7S45O9XC0YeJJRLCuEx6y7IpPbsmY0zzO0wAx4dBgzQcgrvSQcyDdg3jc2I45o3_xL6trwe2DF3YAWR0BAXI54WxKmIM-uIiya_T9fiRUHQ2GIzrJ0oMYcAgudwe1TDaG7YmhFTKcHiS9OtaZrTXljqvKUeJ5POQeHKzWJoMd_ZMLi7BrD_0u9O2VBF2Bd36neJ-R9qheHnNc1pA_bA1-c5QIAoDSIbF1Pf2UkkzrBWbPGbYsRGrGarqrzl9HcOeY-wTCMFXqrORVtJc6lLzJkp-bW2zHoFIUz_ydjG6SeA2ZlKy2ShJn_c90U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از استقبال رسمی شی جین‌پینگ از پوتین و ورود به «تالار بزرگ خلق»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/farsna/436772" target="_blank">📅 08:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436771">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiW4wH6ysjNA7kMqqCyIkIDEpWbFUJt50XA-FhFU958Itz9GScC5hjiz-J9Ft9aWAIOGbrZ_pkhl7rfwiuM_VanCWxj1LZE6xZPL4IkXtuIynRFTDv8TJgHrL1F63-MCd-mLeZ3LyXfYpMmdfg2QKo-oOXWikm2jyxY5SOQEctCa1IpwsX3zm_azy2xjiMjnd9-YOKSLFPdrS-LeNo-KmfCcrM_gnXGa6IYCblF-CVVWGs94HyDmQp7rwJVgs-tbPOhvRWLZnS5U5iBpRUnh8EeN_XgJ0bUMcuwGyjQcM6vGphRCDNVfp3wyA4DWoJbWD64dARlR3NZKLUFr8n9IyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل خط هوایی فرار جنایتکارانش را راه انداخت
🔹
اسرائیل که این روزها سربازانش در فرودگاه‌های جهان در معرض بازجویی و خطر دستگیری به اتهام جنایات جنگی در غزه هستند، حالا یک خط هوایی مستقیم به آرژانتین راه انداخته است. خطی که تحلیلگران آن را «پرواز فرار از دادگاه لاهه» می‌نامند.
🔹
یک تحلیلگر برزیلی می‌گوید هدف اصلی از این کار، فرار از بازجویی‌های امنیتی در فرودگاه‌های بین‌المللی است. سربازان اسرائیلی که در جنایات غزه نقش داشته‌اند، در بسیاری از کشورها ممکن است دستگیر شوند. پرواز مستقیم به آرژانتین این خطر را کاهش می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/farsna/436771" target="_blank">📅 07:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436766">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NoxUIrwcsb0gdp2v0Ah61VlQ-VhkQxGvYPE5hYTz6wS-60pLkhIH7N_eS3wHHsPVi_BNUi7qcEN6CnLO24ldqKfYUmMzQFTwvnllUM48EHJLdIgHqvGSeCXZGic7i9lhvfrHjT4UNLrs7QT_20jwZ0kyIT2eLgW6cwQ1guN6qljvmsBMBbpvXGX7SWQEDwoOvZ1zaxL1cAcETymulxxYLpUnWzHP73enH310Y_B2uuQaIdOi2ZjtbV97K6euT4oVmuttPmz8QNul3k7DcD1m5lMtoTX3JdkgyYxFOti1hB6mpUSSBsRNyu_0SJMmGTU0kCH380go4bg45yCf5__kyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pr30wMM9V-ijAex-nokI7_CyUEGIT5mDgttXN1XcvuSQFblyAx4aUBbgvK3dO3ALvRQq0Rz7oONyTqLtvOMev289bJrHZk8QoW1khzFY12R7iReG0sXhDSU1HGx6ih58jt_t1GHFQmm0W9nN8ALim5lhzi1MYZD-D9UAd3_Nob5m-eeq7noADJexqPuryaJfzpSv0Lyr9hRgP-I-3js3KLrQ-Fxb3b4scs7sNmuAPDlC7ARch1HGinOidrPTVYiGeghxGZgkziaeo4wnQg7jVpBr-z_QIQ8yAwgIZ49DFXdsKyg4loeTGhg41JMgs_EQIDDMrCZmctOq6EaqWf0o_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kl44EMq1Xtr-5J1ycLYwyut_q7fz6nmV9X8xeYKMtxCu-31hh1vusDkWJhqrBuc1RckLUpcciFca4a64uO-h_V7naPAOUtgN3oMzwSfxRP95aNs0UrE2YGOAHzOrhC-zBh8XWy01fWEaNvx0XehDjsWfJSB67njwU5w7fJ-siNGZ2F1vitX2AsnHUdCPK85xijOZeJafqiLbu2vz-vXscYhQKHYiHcTQOd78vUMorfUU9MmGNquo-i4iBlzjUmJhmXPstIh1K3nooGIfJvyXtRu94LG4TILLfSj0WfkvcB2uLPmZrj5H6I1TLMWCATF_obHhi4UGX4WMgjXFwvmRYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUENccEy7BMpNGMfb7YqqtbC8F9gB6nZ2wxdD3a6YiVyIFXNyN-qh5_bRQdfEWskZsaisRWrH4Q2qfh9u5XVq_o4CKJxWvQVKD8ibsMGsFfcc3CSbSSx_5URqNZ8c_5g_cQg_7jkhOLDiZVNfdgmJuLFPFM0GbJRpQ9w5HFEMbEwNaurf1_deSH86LBhWtvUnBuCYIQwVv7TcSg327qnJ60B0fz9_zKO_zGnbsEiEpaIRNpY808QUJooF4X-aLOqGsfj23Jwtglq_vZFlxfkFmhJF_DIa7myk4jznLB7VAvu6Fh2izqvPaTQvoPiOduSyEsDW_eQf-SPIci8STo7eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jHsYXcxoDZfpgq3S1LImNiplzeAj2gVrCJRyw3hwGw08VNOqI-zR3_dDVejDTeTES2EALTSjzYlsobOv__jns4utwfcAYOqcebj8X-YAJRfu4AW8aUXJs0-D29hLueQViMQ99_5VPy4OxwawiaoyEG3RKfKaDV2p4Mfuwh1CCmUYCfH0SapmM5ps3ZcNZow__jF90PjNpPNWAyLqZVK5Q9A6UdWldFuj44OE-pIVr9t8M97PX7S3Y95MrMUKK0j_ztuEnlsgVwof75r3ZAcBC2oYOB_DT5eCPJzR_uVbNdK_x9xlqngWOw6g14pc6I_iAIYnwrUKorUaScZzspkq7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
۳۰ اردیبهشت روز جهانی زنبورعسل
عکس:
مهدی لطفی
@Farsna</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/436766" target="_blank">📅 07:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436765">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3erD6V5ne4qL3ua5obzpGk_HMQtEivLK9plI7ryPPbmEatmveoW7-wJGyxFIMAuSAxZzmQBO4nT3v1EEOFvqopszYjbDPPxhI9dT1RAWjdZNbc7LmJfVJoHq8GOGJFoNKyf6hUTRwm8erp3WoH1xTTZed0Fu9dFmqQ69H9ydm3C81rT8kGXU2zwYbio4XwK-nrhqr9OEJ9WXtuM-J6vvPWhEqez4c6sRBGysmJa2CqtN0WVtQ6aMQCcNnpfbk9n7QJ5iZyxDngvOzXSaD4hvvkqTK_GV8V4y-SrRuqEd_YjU9QA1q1_UZTS4yH34MJMZsM-F-CdEUWC4yb0vmbdig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم قصاص قاتل الهه حسین‌نژاد اجرا شد
🔹
با درخواست اولیای دم، پس از طی تمامی مراحل قانونی و تایید حکم در دیوان عالی کشور، حکم قصاص قاتل الهه حسین‌نژاد اجرا شد.
🔸
خردادماه سال گذشته، مرحومه الهه حسین‌نژاد برای بازگشت به منزل سوار یک دستگاه خودرو شده بود، اما راننده او را به قتل رسانده و پیکرش را در بیابان‌های اطراف تهران رها کرده بود.
@Farsna</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/436765" target="_blank">📅 06:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436764">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🎥
حاج منصور ارضی هم از تنگۀهرمز خواند
@Farsna</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/436764" target="_blank">📅 05:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436763">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCkIYGRum-lgzQi3DHI1FFYYTmXUz5EEHV779KuSUtqQeZ7fXf2UzyU2zuLFdoTb7-Ggf0f0qfr715pfmnzAm-1eFsJxaIOdLRtXM7nCNYtYhG5AusLzmkhjU0RcStT_Vhp9XW4eJ6eC9858mgKfC99JvaLGTMngWNTPJYkZLZ2esCbWpl00vDDOf30UUSUJA9jla1KKtwWqvZqruIqKA1098m-8U_GY2--i1zqdIJmTyJec9-W-3IR2qVb9H7D_uRimRkNKRAZOhQlfIxWH5hopHoa-shD-fykImK9aac8c5qZBIFTzbj0nkSaBXZAJrlpCjA1AouiRE0Qcakf6MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸۰۰۰ کارمند متا اخراج می‌شوند
🔹
بلومبرگ: شرکت متا قصد دارد ۱۰ درصد از کارکنان خود یا تقریباً ۸۰۰۰ کارمند را تعدیل کند.
🔹
این شرکت در یک یادداشت داخلی به کارکنان خود اعلام کرده که این تعدیل‌ها از ۲۰ می (۳۰ اردیبهشت ماه) اجرایی خواهد شد.
🔹
متا همچنین اعلام کرده…</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/436763" target="_blank">📅 05:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436762">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11174b560e.mp4?token=WZQ154isPI14GdTJFXekNaQWSJ3J_X7wrUkfJ7f4vT_0GJSOd_g4qEFlQH0P6BAP_OHVYj6voQYbsImK1e6lV2WNvM31NsfWWIEpdiBMkz_ML5PD-Nkn9iUfKfWl1W0JLR5tC7EQUv2ZJFr2-os3JUfGEE9zT_u62YPLLQ2b0QN6_5oycsiMzJCpdrtbwQYpSw57PZB2IRMN1IJeeoJ26N0FxPzTZe_JgkUBE9_aSDxGeNiGk-lOO9jSkc7-SdxWxg4w4wPXnyIjcnOSSChms8BW2sltuF8CCwr9mvpcXNiE-IeMMlfjUf3W_6nuOmyhjZCTQ-4zgKK3TN7uW6rqNUkAjKPIchLpEl-aJRCoFnjxpUz5dORuZL_JedtBRsmqzCtXT4xCWp7BmC3QXHYT2xvMmQ9WDL5R4mWr8dE1nK56ANezdKAP1lyz7y9_jwunhTV3-ami42l42uN7_vvOGVlIlpg_lvASmwWnCdHNh_67uyB_3DF9LGibhGS_5EnizbUyhSHkuezplXbD65635sJD3f8L--FTwyoHnaSfKOiiQbk8ufVmUaAo-f6Ame6-u1oD07y664zcEPb4pfWw_jr0XyWYnz74mrH0mv4HhDfbVS-hXmIVBBq0vDOnBTynypNKrw74VOUHLBv9UxgKXGcijFwNSaQX3vtMvid6wJk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11174b560e.mp4?token=WZQ154isPI14GdTJFXekNaQWSJ3J_X7wrUkfJ7f4vT_0GJSOd_g4qEFlQH0P6BAP_OHVYj6voQYbsImK1e6lV2WNvM31NsfWWIEpdiBMkz_ML5PD-Nkn9iUfKfWl1W0JLR5tC7EQUv2ZJFr2-os3JUfGEE9zT_u62YPLLQ2b0QN6_5oycsiMzJCpdrtbwQYpSw57PZB2IRMN1IJeeoJ26N0FxPzTZe_JgkUBE9_aSDxGeNiGk-lOO9jSkc7-SdxWxg4w4wPXnyIjcnOSSChms8BW2sltuF8CCwr9mvpcXNiE-IeMMlfjUf3W_6nuOmyhjZCTQ-4zgKK3TN7uW6rqNUkAjKPIchLpEl-aJRCoFnjxpUz5dORuZL_JedtBRsmqzCtXT4xCWp7BmC3QXHYT2xvMmQ9WDL5R4mWr8dE1nK56ANezdKAP1lyz7y9_jwunhTV3-ami42l42uN7_vvOGVlIlpg_lvASmwWnCdHNh_67uyB_3DF9LGibhGS_5EnizbUyhSHkuezplXbD65635sJD3f8L--FTwyoHnaSfKOiiQbk8ufVmUaAo-f6Ame6-u1oD07y664zcEPb4pfWw_jr0XyWYnz74mrH0mv4HhDfbVS-hXmIVBBq0vDOnBTynypNKrw74VOUHLBv9UxgKXGcijFwNSaQX3vtMvid6wJk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۸۰ شب حضور لردگانی‌ها در میدان خیابان
@Farsna</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/436762" target="_blank">📅 04:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436761">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXnygv4exQcVUGIsHCE9aGjKa8qsJlI716bFeGGYpio665j-gqF_NGqkkmghsTsKppygGqHRVJP48JxxSQ4QHOV8lI-gu9KUrxukA-66M5dA33W0EjnuBRJoA49680iSCLdM8ptg7x8MLJyrAEtA59UoOeISi0b4R2D-P3w2tIfnqQYHWpSd4zvKGoIQhJQStSHQIQLwxO8Qy_Ec2ot_kRIosXTmVeCNDDxDbIKI5XCX8RmWxeopgaG0vqGJVpfvuDaB2aha79PnhZJLnGKQ__1igSriYO64ePrEaVBxzNMnm_K-jR79Zia9gGJihqjDkGKsDVwrXNuRJlyxfwGzzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام حماس: اسرائیل از ورود دارو به غزه جلوگیری می‌کند
🔹
مرداوی، عضو ارشد حماس: رژیم‌صهیونیستی به مفاد آتش‌بس در غزه پایبند نیست و اجازۀ بازسازی بیمارستان‌ها را نمی‌دهد.
🔹
بیشتر کسانی که توسط اشغالگران در غزه کشته شده‌اند، غیرنظامی هستند. اسرائیل به مفاد توافق پایبند نیست.
🔹
اشغالگران اجازۀ بازسازی بیمارستان‌ها یا ورود دارو و اسکان موقت به نوار غزه را نداده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/436761" target="_blank">📅 03:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436760">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">زلزلۀ ۴.۷ ریشتری بخش‌هایی از استان هرمزگان را لرزاند
🔹
دقایقی قبل زمین‌‌لرزه در بخش‌هایی از قشم، هرمز و مناطق روستایی بندرعباس احساس شد.
🔹
بزرگی این زمین لرزه ۴.۷ دهم ریشتر و کانون آن حوالی بندر لافت، در عمق ۲۰ کیلومتری زمین گزارش شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/436760" target="_blank">📅 03:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436759">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8e149b765.mp4?token=QO4EpPoBvnzBpaTMlp848GO3cVE6rd7wQCsE7jUA_05EdqzlODtnGpX3OSeNSnI1osBPgN80Lkt0jYe-xrTw4nVOL_luQba8OeWQ17FdNyQ7sOYsg3mo_gmGJQEX2bemwxcIoTCHSadZjoAtYBbuHK4RDEXwSxtI-GSdNfKRNDNsAGsuL0ABUPFCBSH2TB6ggyT6gmBX4e0gIMroFA7_ea8jfvtGfRgEjThym7AwoPonKBvddiOFYQ2KnLi-7jjnWnvgWR26EgwX3eDtgiw7qGzswq1sV26JHYZPYkUs-mJT-paBm_joHMJvqzSCGc5-aJ8-dna3nusgmFt1lNdTXb8tbCMU96uf--30_Q3ArycbQ3Qf8jwxPj2bG78irF7SHGoeqXud0CLFtXsLRltLV5zWgcavSVzxkGjJfggZ4Jip5QG0nw-meGmb3rwgbdK6r7Ik97ivtMaTaTsXf-psiIA9-aydYEtG48nenfUeYdQ-cTpYNHe-o1WukaGMukOixpmdpDoAWoYfuYGeDPtzLDuesChvDTrCQAIUa9VXWuZPttOZrfqgNS4IZPLbbSwOiBBMKlx0dzCQyk_mnmz1Pzc5VEj5EB2hH_fWJdYFgsIAEAeEe_-yvfJUUrPHZGA7cMVdsjIy4fDEoN3S-SWz1UZpweVk0GTp_ShIg5qWGbs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8e149b765.mp4?token=QO4EpPoBvnzBpaTMlp848GO3cVE6rd7wQCsE7jUA_05EdqzlODtnGpX3OSeNSnI1osBPgN80Lkt0jYe-xrTw4nVOL_luQba8OeWQ17FdNyQ7sOYsg3mo_gmGJQEX2bemwxcIoTCHSadZjoAtYBbuHK4RDEXwSxtI-GSdNfKRNDNsAGsuL0ABUPFCBSH2TB6ggyT6gmBX4e0gIMroFA7_ea8jfvtGfRgEjThym7AwoPonKBvddiOFYQ2KnLi-7jjnWnvgWR26EgwX3eDtgiw7qGzswq1sV26JHYZPYkUs-mJT-paBm_joHMJvqzSCGc5-aJ8-dna3nusgmFt1lNdTXb8tbCMU96uf--30_Q3ArycbQ3Qf8jwxPj2bG78irF7SHGoeqXud0CLFtXsLRltLV5zWgcavSVzxkGjJfggZ4Jip5QG0nw-meGmb3rwgbdK6r7Ik97ivtMaTaTsXf-psiIA9-aydYEtG48nenfUeYdQ-cTpYNHe-o1WukaGMukOixpmdpDoAWoYfuYGeDPtzLDuesChvDTrCQAIUa9VXWuZPttOZrfqgNS4IZPLbbSwOiBBMKlx0dzCQyk_mnmz1Pzc5VEj5EB2hH_fWJdYFgsIAEAeEe_-yvfJUUrPHZGA7cMVdsjIy4fDEoN3S-SWz1UZpweVk0GTp_ShIg5qWGbs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا اصالت، زیر آوار هم زنده است
🔹
روایتی از پیرمردی که با سر خونی، رسم مهمان‌نوازی را تمام کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/436759" target="_blank">📅 03:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436758">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVM85LzHi9TgKzaG6HKey3d7BGizh0VWhSAOxRBhMBoVCPkIdXrVlBUS4xitKci3j1asMWHZbqPdsevKQXJZCKYWTX5pjAqWjbPjjbpiGFrBzatClibFJeDgwgqritRAXUud5DkXAfMF0_gxI7ahwlskETy4J1cfECywQqr1sSZ5arMU6zlZudUnB0-23vqeI2V9miyJD9l3K4HKQ3Y42q0NmsbvRbzJRt_2LIcfw3qNOUdEaYiAujprCe53WvPJK79EUrX8BzUApdqyTFW4-p8zaheJYsxWiJOmg9U3PUT-MUN80eCYoE7pH8JjhomCzI9EhWN_hb3SDwxTmAtT1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ دربارۀ تعویق حمله به درخواست سران عربی دروغ از آب ‌درآمد
🔹
وال‌استریت‌ژورنال: چند مقام از کشورهایی که ترامپ از درخواست آن‌ها برای تعویق حمله به ایران خبر داده ‌بود، گفتند که از طرح ادعایی او برای حملۀ قریب‌الوقوع به ایران اطلاعی نداشتند.
🔹
پیشتر…</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/436758" target="_blank">📅 02:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436757">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎥
هشتادمین حماسۀ مردم شهرکرد با یاد شهید جمهور، آیت‌الله رئیسی رقم خورد
@Farsna</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/436757" target="_blank">📅 02:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436756">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پیشرفت طرح پایان جنگ ایران در سنای آمریکا
🔹
سناتورهای آمریکایی بامداد سه‌شنبه با ۵۰ رأی موافق و ۴۷ رأی مخالف، با پیشرفت طرح محدود کردن اختیارات جنگی رئیس جمهور این کشور علیه ایران موافقت کردند.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/436756" target="_blank">📅 02:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436755">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uADSiX_tDO2nAJMzLTi3z-9o0FWqgfQvhXHZm8u7NXd5thXHJhb3rHUhAvyEcXPkRS6zH76n0zdap8XnW4HjvZSDkMbZEO-aUvYcx25UhqfchSRn455N0v0aETwKJKFvaouqswcn55_qTarrXtdniwhsnFISPq1LxqddDmxQrV9HDNNZoZLNlcPHor7PPCQInjktQpNdcQs38irDJmm9OHgzelYA0cHRqzTuetrS7KDJ5g5kRN0cwQ8ws5D-ru7nQmWX9S_GUwRoL7W-CQ1NMu509QyXV7km0gCj3j2IMfVfPd-_YDoIFyJxQkmERSeadv8HnjsxOfahsG4U1dEjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشرفت طرح پایان جنگ ایران در سنای آمریکا
🔹
سناتورهای آمریکایی بامداد سه‌شنبه با ۵۰ رأی موافق و ۴۷ رأی مخالف، با پیشرفت طرح محدود کردن اختیارات جنگی رئیس جمهور این کشور علیه ایران موافقت کردند.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/436755" target="_blank">📅 01:49 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436753">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec04452baa.mp4?token=VEd7soLd4CEjGw9DY5cMGPc5UgO8R-2WXl7tyKZuzWiLKJvwqc1yx6AQSqwhoHy_zrVUAjhLlu0-fmMNcwlcIUcqnKqHUYvzAIwypYE-PhNkV6t46685VufqfZok1vouaHbCT8leZxnjoy5xN6nMGfvebc4ziCkCJsyaM_fxt3VBol401nvc-SOwZPi3zEIz1DjDBJVU03LlTMy3F2gZd5-R3vm8ruuW5hVBN7xKSN89FKKg7eu9qJgioMspZkH6uZs2RSTBrw1YQxsPCpETronu0_7MCmJi-OwwONAYieUK6mnNBzOrVvvamM9F2sE9W665C2uPGW1cu95SANxU8oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec04452baa.mp4?token=VEd7soLd4CEjGw9DY5cMGPc5UgO8R-2WXl7tyKZuzWiLKJvwqc1yx6AQSqwhoHy_zrVUAjhLlu0-fmMNcwlcIUcqnKqHUYvzAIwypYE-PhNkV6t46685VufqfZok1vouaHbCT8leZxnjoy5xN6nMGfvebc4ziCkCJsyaM_fxt3VBol401nvc-SOwZPi3zEIz1DjDBJVU03LlTMy3F2gZd5-R3vm8ruuW5hVBN7xKSN89FKKg7eu9qJgioMspZkH6uZs2RSTBrw1YQxsPCpETronu0_7MCmJi-OwwONAYieUK6mnNBzOrVvvamM9F2sE9W665C2uPGW1cu95SANxU8oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهپادهای آبی و صورتی به میان مردم تهران در میدان آزادی آمدند
@Farsna</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/436753" target="_blank">📅 01:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436752">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a3c43e84e.mp4?token=oN8h2xHGyWBCuMzoNQ7onE_8SZmKP02sJgaEZQX4HRjghGvDHQCrI4CXjqOJg17CV7HjMtIItCyjnlvW6f1PZmZct-MVGR3kR5iG4Q7QkGfm8c0DPMOqPLfIyrK2EL6tVibDS8eR9Ua0y6Do8OV7DwXdL603e1DAAbvEuNO3UJ8g6KFtL0bwVTTSb4Ywb-_jH0uH2ibwKJD6nJCItHF_8GiX1GG7HKA5fHhUK1WDNBnV2kMFS5oCPumZFuwW2iYREEIiseJhda5iZx9976C2o5hpnif0QrM2HidFKcFX4Mlh1y1KQFg0HE1KgqHCYsNVlhc3nfgm1ztwOPgpI9X3ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a3c43e84e.mp4?token=oN8h2xHGyWBCuMzoNQ7onE_8SZmKP02sJgaEZQX4HRjghGvDHQCrI4CXjqOJg17CV7HjMtIItCyjnlvW6f1PZmZct-MVGR3kR5iG4Q7QkGfm8c0DPMOqPLfIyrK2EL6tVibDS8eR9Ua0y6Do8OV7DwXdL603e1DAAbvEuNO3UJ8g6KFtL0bwVTTSb4Ywb-_jH0uH2ibwKJD6nJCItHF_8GiX1GG7HKA5fHhUK1WDNBnV2kMFS5oCPumZFuwW2iYREEIiseJhda5iZx9976C2o5hpnif0QrM2HidFKcFX4Mlh1y1KQFg0HE1KgqHCYsNVlhc3nfgm1ztwOPgpI9X3ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوال نماینده کنگره آمریکا از فرمانده سنتکام: گزارش‌های عمومی متعددی وجود دارد مبنی بر اینکه ایران بسیاری از سایت‌های موشکی بمباران‌شدهٔ خود را بازسازی و احیا کرده است. آیا این هم بخشی از برنامهٔ شما بود؟
🔹
فرمانده سنتکام: این گزارش‌ها دقیق نیستند.
🔸
مولتن:…</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/436752" target="_blank">📅 01:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436751">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKATwcGQTG9c1Vx8ThIP-cLBMn6EsjxPC-2PHv5777nBoHZ_aIb0irFOWSz6EgriQNSXkAMCY7jKIST2U_oDRAZd5xMEoOvS-8tiAeAt7_4Kco9XfqWhWRQkU8D50Vv1CTM_us3H3HEwePHVxB03jR6fLo8unxLkCWUXr3B91gIL_cUQGA3jTYReKPNpC2u2qRYQr1foGKvAGsU4V0ACxx74gWUsYDMtHM90-HFhhIYTPvNqXcIJrEYqwPz_r9xiWaztk59i8DVI85doMYXxW1NQkMK4HF1o_mqbLp_hSEozmCNU4EDhR2q1bkfV15VD5i19nIGCY7-mV5JXTtdtuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهان چگونه دسترسی به شبکه‌های اجتماعی را مدیریت می‌کند؟
🔹
در کشورهای مختلف جهان، دسترسی به شبکه‌های اجتماعی خارجی یکسان نیست و هر کشور با توجه به قوانین و شرایط داخلی خود، سطح متفاوتی از تنظیم‌گری را برای این پلتفرم‌ها در نظر گرفته است.
🔹
از استرالیا، فرانسه، دانمارک و اسپانیا که دسترسی به تیک‌تاک، یوتیوب، اینستاگرام و فیسبوک را برای نوجوانان ممنوع اعلام کرده‌اند، تا ژاپن که شبکه‌های اجتماعی را ملزم به ایجاد سیستم‌های شفاف برای حذف محتوای غیرقانونی نموده است.
🔗
ملاحظات امنیتی یا فرهنگی سایر کشورها در مدیریت شبکۀ اجتماعی چیست؟
اینجا بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/436751" target="_blank">📅 01:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436750">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vL1yKoE3ji_T9UVOX2auc6yvXlKGzBiD_m5dTGw1MjykXfVlHBCIu6oYuiRDvErlMD9G6uofTkh7BaXaP1f6sg1uOC-rbQdXeEJ-F-5WZGoVywIqRfofZHVf7yT2fhRLfT-44eSFClhuVWulnGxuY-FKJlDaHQPCZm97lDWOS_iNBdiFaqGnFjiScu7bJPFsgoS1B_rdUVJIwfUPyLv67KqSzX1BP1DZ4YUN0OKZWXKy9u1dmXpa-DmU0MqU_sqBuyrIV8hqaodoYe7oNdcsQ0D2ejSGIVU255LFzSqb-UbwFPD28cPURGe0DMmBWD7-oKVV3hl9Nka62wCH818_Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز هم یک نظامی صهیونیست خودکشی کرد
🔹
سازمان رادیو و تلویزیون اسرائیل گزارش داد که جسد یک نظامی ارتش این رژیم در سرویس‌بهداشتی موسسۀ امنیتی در منطقۀ کریا واقع در تل‌آویو پیدا شده است.
🔸
رادیو و تلویزیون اسرائیل تصریح کرد که گمانه‌زنی‌های اولیه حاکی از آن است که این نظامی صهیونیست اقدام به خودکشی کرده است.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/436750" target="_blank">📅 00:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436749">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KatHlJQeClFJPOvT7_136Kr-eb1ZnDkvJv_uUzt4KQTaLKyrCbHcN9FJyYmzmDhFSiPCBthqNqSHRD0EDF9xIvhrCWSQtmSFSpOIC-yxYYr-E5j27VGaDwxwrCtSgsY6ouDYijk-k-YNOR2tpAc2Apap1OF2Gd_Wg86byNC9-reiWIHIY75oN_F0XpkV19ugU4HQHAZW-XGZ4B_mbrc9MeLoJE0EMV6u1FPBMabv7W2l0uKYK8rb5EGHq9Jxq2S81F1mzFOvvlmRUQ_2kPEXV7kgpSvqfwctHqXxH7T2qipAEbv72M44hKfcCh71nArMapGu4Jk9Gb_ExsvUG3iTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی وزارت خارجه: تقلای شرم‌آور آمریکا برای توجیه جنایت میناب، نمی‌تواند ماهیت این جنایت را مخفی کند
🔹
ادعای فرمانده سنتکام مبنی‌ بر اینکه مدرسۀ ابتدایی شجرۀ طیبۀ میناب در محدودۀ یک مرکز موشکی بوده است، کاملاً بی‌اساس و انحرافی است. این تحریف آشکار، تلاشی واضح برای پنهان‌کردن ماهیت واقعی حملات موشکی ۲۸ فوریه است که موجب قتل عام بیش از ۱۷۰ دانش‌آموز و معلمان‌شان شد.
🔹
هدف قراردادن یک مرکز آموزشی فعال در ساعات مدرسه، نقض فاحش حقوق بشر و مصداق بارز جنایت جنگی به شمار می‌رود.
🔹
ماهیت غیرنظامی این مکان را نمی‌توان با توجیهات فنی و بازی با کلمات پوشاند. فرماندهان نظامی و مقامات آمریکایی که مسئول صدور دستور و اجرای این حملۀ فاجعه‌بار بوده‌اند، باید طبق قوانین بین‌المللی پاسخ‌گو و محاکمه شوند.
@Farsna</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/436749" target="_blank">📅 00:47 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

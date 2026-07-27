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
<img src="https://cdn4.telesco.pe/file/ngeaSjEY-Bk6lkVQrM2DNVsS2TFr68xIjm-N_h19ntFQSn_JI8um0gSyj-Jqk81FnpG0uZ5EPEkuX63CpgE5nVjVWUBUMHLvDCNFhzmWtzX8RVVMCAUaEV4hJkbR0PODEu9axZ-Cu4XFiF2UQFVIvnsFkoOkduRpame_MM4yJZ_CuWWAMkMNsz09MhavSOab4434WFPtUzSvJ5OxleDfR55qJa8ril9AlIoblo1sGywD1hkxPH1ZifQP53m5aFmPnmhJJuBxl9bzvugJj00Lo6EKjFF3yD5CuETAqBkdNlwZDxKW_f57ZiniybA29AnTGpVFYh7ovIR3fbpkhPERFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 12:21:40</div>
<hr>

<div class="tg-post" id="msg-452887">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">انهدام مهمات عمل‌نکرده در خوزستان
🔹
فرمانداری امیدیهٔ خوزستان: درپی انهدام مهمات عمل‌نکرده در شهرستان، احتمال شنیدن صدای انفجار در امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 636 · <a href="https://t.me/farsna/452887" target="_blank">📅 12:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452886">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e838ab80d.mp4?token=tjCbFNlKaS8GjAp9lOgau-9z-XMFplBTWD7OCzY6dOf8Hq3aSZsSgXaWcbePdygv8eNiHYgIVgCl9m0nQJFXAa13bhlljd5Q9Use31SRyoCj5Im0CRPsU8lvkcGNQY8CYJ_p7nCla8h6U3UOWcrP-ay7Ntz094uWzsrwb5ffw0Gh_sVESwvy7eOPC7i9frpFEbLfKIBFs8eA_lysxnyMll-Namy8zAzcnzJEqxWeI2YjrWLEI9F7LqOfLWx7CSAL2-vV47Qa-JndYGA3jRu2JaaoBqMgGBXSg3ZgXQiX1jGvo4l3qj1dj44UL70taDuEPC74Ad0X7NN_TppuiwDxUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e838ab80d.mp4?token=tjCbFNlKaS8GjAp9lOgau-9z-XMFplBTWD7OCzY6dOf8Hq3aSZsSgXaWcbePdygv8eNiHYgIVgCl9m0nQJFXAa13bhlljd5Q9Use31SRyoCj5Im0CRPsU8lvkcGNQY8CYJ_p7nCla8h6U3UOWcrP-ay7Ntz094uWzsrwb5ffw0Gh_sVESwvy7eOPC7i9frpFEbLfKIBFs8eA_lysxnyMll-Namy8zAzcnzJEqxWeI2YjrWLEI9F7LqOfLWx7CSAL2-vV47Qa-JndYGA3jRu2JaaoBqMgGBXSg3ZgXQiX1jGvo4l3qj1dj44UL70taDuEPC74Ad0X7NN_TppuiwDxUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ سقوط پهپاد ترکیه‌ای «بیرقدار» متعلق به نیروهای سعودی در یمن  @Farsna</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/farsna/452886" target="_blank">📅 12:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452885">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d96a362192.mp4?token=BuCKqNJnARzG0lJKWB9JtkmjcOt71FAMRg_o9_nZe--kkcJSk448rZZXQgR7cwcCuRRefR060AUGiA6-eiwLhKeQWTsDOW85J1abrFUsRHPsPT9KKoZhJ7ZOV_vN7hv9NX60jk3WHrVqzpHEM3S0wcFP94bxY2s4PwUKWbzhbnHr4bGcipv4-UMzM2Py-MKU7u_GHAXasrXaRbkxpemrpjI5M1iYzqLBKBAZBfquE5wxNYEHQYWaToAqiV_qyeg9gSZLkIjfdlPvwO-U91mlwftmGzdrJ00qoArtEy4_D029xnmY-mScTqwFmE3uD2HYbNFgEJnO9Gm5-L_oqKI9Q4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d96a362192.mp4?token=BuCKqNJnARzG0lJKWB9JtkmjcOt71FAMRg_o9_nZe--kkcJSk448rZZXQgR7cwcCuRRefR060AUGiA6-eiwLhKeQWTsDOW85J1abrFUsRHPsPT9KKoZhJ7ZOV_vN7hv9NX60jk3WHrVqzpHEM3S0wcFP94bxY2s4PwUKWbzhbnHr4bGcipv4-UMzM2Py-MKU7u_GHAXasrXaRbkxpemrpjI5M1iYzqLBKBAZBfquE5wxNYEHQYWaToAqiV_qyeg9gSZLkIjfdlPvwO-U91mlwftmGzdrJ00qoArtEy4_D029xnmY-mScTqwFmE3uD2HYbNFgEJnO9Gm5-L_oqKI9Q4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیاده‌روی عشاق اباعبدالله(ع) در مناطق جنوبی عراق
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/farsna/452885" target="_blank">📅 12:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452884">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc523b2083.mp4?token=lILDiFV-TIXVA84TKKWD3mQ1P7Mod1tYedfuoFN_XjNc3gA1nrT7NdrwfwGCpzsm4hSgNiHW4nCyZewcv89Mb3BDQF4jhiCe4b82cDUgf5n-K658PYi-aEKzPzMtM5VLoPRYFZGT9iVaZkfv5J6QRBfadSsZ5oXW7mCyNY1pkF9egvp59sQ2XOas_CBGJNChQuaGiR39Xd8afKcqKC9m-tLadujsxbOqocknkYHvpYaPaVwkUVgqDM4hBGFMelCR3JOKXmixmIBAUBlgypJTD8PmUD2OiU7YlTfqGpgON2xWqyvtEMkurGIwYkqx2dInYCLAYHm0NBnuS8kGiTMBHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc523b2083.mp4?token=lILDiFV-TIXVA84TKKWD3mQ1P7Mod1tYedfuoFN_XjNc3gA1nrT7NdrwfwGCpzsm4hSgNiHW4nCyZewcv89Mb3BDQF4jhiCe4b82cDUgf5n-K658PYi-aEKzPzMtM5VLoPRYFZGT9iVaZkfv5J6QRBfadSsZ5oXW7mCyNY1pkF9egvp59sQ2XOas_CBGJNChQuaGiR39Xd8afKcqKC9m-tLadujsxbOqocknkYHvpYaPaVwkUVgqDM4hBGFMelCR3JOKXmixmIBAUBlgypJTD8PmUD2OiU7YlTfqGpgON2xWqyvtEMkurGIwYkqx2dInYCLAYHm0NBnuS8kGiTMBHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
✨
✨
حسابتو طلایی کن
✨
✨
✨
‌
🟡
۶۶۶۶ سکه طلا برای ۳۳۳۳ نفر
و میلیاردها ریال جوایز نقدی دیگر ...
‌
✨
جشنواره بزرگ قرعه‌کشی حساب‌های قرض‌الحسنه بانک سپه
✨
‌
#بانک_سپه
#نخستین_بانک_ایرانی
‌
🌐
https://omidbank.ir
‌
🌐
https://banksepah.ir
‌
📲
@banksepahofficial</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/farsna/452884" target="_blank">📅 12:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452882">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gahxNfsGZXesgXrr6grd9mW8xdGGyKohggNb6_42P1Hbo8xzQGNghioGB9URVDWhDuMeKDqx3kvcz8Zkul_RiSkeN1RTeXTtzkX4q3w6fsEWTRTU6aax7TW1ZgtoqVdQKnBX29OdlqT_b3XKYZX3TpH5nnunD3MrUk4GCugaQvkmLYdLW-1OSvKCM6IOw5fNzKajHyc-_1bVfgTN-qidFqoIpkvIoxamFv5z-QrTTV-T1ZdSCpYS0s-_EdJ3vkVFwcXjIjfCvjFy7hUvc9hHPs-qtG2d_jAQucCjyWGM2X7WhinSPDihH_hJ1b7S0vuy8VvxJBqEIO84l4lHKlHbXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاوره درمانی ۴۰۳۰ با تماس رایگان از عراق برای زوار اربعین
🔹️
سامانه ۴۰۳۰ به صورت رایگان و ۲۴ ساعته آماده مشاوره در زمینه‌ سلامت، تغذیه، لیست داروهای ممنوعه و معرفی نزدیک‌ترین موکب درمانی به زوار است.
🔹
زائران می توانند با شماره گیری 4030 بدون نیاز به پیش شماره از عراق به صورت رایگان، تلفنی تماس بگیرند و یا با شماره گیری  *4030# (ستاره چهل‌سی مربع) اطلاعات را به صورت پیامکی دریافت کنند.
@Farsna</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/farsna/452882" target="_blank">📅 12:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452881">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/farsna/452881" target="_blank">📅 11:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452880">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jxyrq5p2-sNsfJVhwj0DqN9LtqyJ9zQKLQZGOiMvjky7IiABF8_RaDxASGOUZrtzJWsVhQsIxCcdZVFj8acHJwEf1axHeOlBTmj2vy07VPp7p1zRcfHOyNsH5ZAy4u4M0OgtIH4mTm53TUQ5X6l_xNYISKvUlQMKE3CNCodz1Yo110i2QezfHIYN9XJIjj2LYGv6cidm2LGnlh-jQi4npAPuYCJlCL0WPiCd8pKyZNMU-PUjv2Dp0MDLfT1gCcm9mT0aE2LtbDCvn7JJ_KB0RM6sR1eQoId6a3AwX52GIPn7xD2lCk2H-R8pZ4GxlnhAK7POTuPgT915wczDJHay5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اژه‌ای: اگر کسی در قوه‌قضائیه دچار فساد بشود، در برخورد با او رحم نخواهیم داشت
🔹
اعتقاد راسخ ما این است که هر مسئولی باید در قبال زیرمجموعهٔ خود نهایت صیانت را داشته باشد. باید نظارت‌ها و هشدار‌ها و تذکرات به‌قدری وسیع و عمیق و سازمان‌یافته باشد که اساساً امکان حرکت به‌سمت فساد برای یک مسئول و نیروی یک نهاد حکومتی و دولتی وجود نداشته باشد.
🔹
چنانچه باوجود تمام این نظارت‌ها و هشدارها، فردی در درون قوه قضائیه یا بیرون از آن مرتکب فساد شد، فی‌المثل رشوه‌ای دریافت کرد یا آلوده به سایر مفاسد شد، مطمئن باشد که هیچگونه ارفاق و اغماضی در قبال او وجود نخواهد داشت.
🔹
ترحم به چنین فردی، در درجهٔ اول، ظلم به خود او و دستگاه متبوع او و در درجهٔ بعدی، ظلم به مردم است و ما هرگز چنین نمی‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/farsna/452880" target="_blank">📅 11:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452879">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e21ed4d2f.mp4?token=QS2WSyDGDwP3T5OV8UwxK2fVpMVTM2RJrLYKPCiuSABZDbxUjfC-b5wfmqX5IGEReSb1R22jDkyA1DF-aLdpqdD58QmXrz-5L_MDkA-Jj3NvJIueI1NCAxe5-xgmQUKXYsfcbZl7zV2kKlq3xU-JuIMpRVeLdcEbjNsbu1qkkOqocBNvbb5aNqaiLqsQJzrSJUj070Mf0iKRnea8gsLmupneP21dTUDtYX9gkZQKfO08ezsNc6d82bHKzJfr0BuJGpKIHJAvv3Uy7cG-FyzempqPyd41MLKg7_MzLKjLgDJq2C7hLXpOvtQxMUpWUjVcKhAvxGhsth7u-CbHpHVtRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e21ed4d2f.mp4?token=QS2WSyDGDwP3T5OV8UwxK2fVpMVTM2RJrLYKPCiuSABZDbxUjfC-b5wfmqX5IGEReSb1R22jDkyA1DF-aLdpqdD58QmXrz-5L_MDkA-Jj3NvJIueI1NCAxe5-xgmQUKXYsfcbZl7zV2kKlq3xU-JuIMpRVeLdcEbjNsbu1qkkOqocBNvbb5aNqaiLqsQJzrSJUj070Mf0iKRnea8gsLmupneP21dTUDtYX9gkZQKfO08ezsNc6d82bHKzJfr0BuJGpKIHJAvv3Uy7cG-FyzempqPyd41MLKg7_MzLKjLgDJq2C7hLXpOvtQxMUpWUjVcKhAvxGhsth7u-CbHpHVtRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: آمریکا در ۲۰ روز کل تفاهم‌نامه را نقض کرد؛ ما از اصول امنیت ملی‌مان کوتاه نخواهیم آمد.  @Farsna</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/farsna/452879" target="_blank">📅 11:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452878">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5d6db134c.mp4?token=Kj_CMVfT-3zv2CpInQG11HGUrOgFvDLZ3WQlpb3UelMggDpDOvgU7e3j1FnVtE6DorOYGm17Hkbyoq0XEWVhismoUfzg1uERx_md0fn_Db6vNvmJqjWqxu2YFjXLkQA6QPXgtRZu_Z-ljaP69bmgDdyDsLGGCmbPgq5_5Y6EKUhw60qrlHb-DEUV4-9Ngkba6DPnJLs_qQ6UJcwljWOOLc7_KcYkk2ZJWeEdwyVfmBbAaR5B9zBbU5fZAatIaGRnzWRZgacJOLH2Ji8akAUaM76Hoxzv36fBGtiIAu0AcvtlkyENOKwrFUK2HM6ifMuV3PqpxOqz7VCfRKMqWZUtKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5d6db134c.mp4?token=Kj_CMVfT-3zv2CpInQG11HGUrOgFvDLZ3WQlpb3UelMggDpDOvgU7e3j1FnVtE6DorOYGm17Hkbyoq0XEWVhismoUfzg1uERx_md0fn_Db6vNvmJqjWqxu2YFjXLkQA6QPXgtRZu_Z-ljaP69bmgDdyDsLGGCmbPgq5_5Y6EKUhw60qrlHb-DEUV4-9Ngkba6DPnJLs_qQ6UJcwljWOOLc7_KcYkk2ZJWeEdwyVfmBbAaR5B9zBbU5fZAatIaGRnzWRZgacJOLH2Ji8akAUaM76Hoxzv36fBGtiIAu0AcvtlkyENOKwrFUK2HM6ifMuV3PqpxOqz7VCfRKMqWZUtKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: جمعه و شنبه چند دور مذاکره بین ایران و عمان برای مدیریت تنگهٔ هرمز برگزار شد که مذاکرات خوبی بود؛ وضعیت تردد در تنگهٔ هرمز هیچ تغییری نکرده است.  @Farsna</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/farsna/452878" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452877">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b543b1687.mp4?token=H7OLdT4VUvSAg7vCXrfqMqFor-R8bSgsFuEiGRFiWJV3lWl3nVnukh3plxT7mU6lHzPtzMZ_b_7GaJMWX1502F6yfPyjZqgigsP3yuoaj3N7Powl3x0oBNRRT2246mDuA-ASTjna3frvjRp9DHu1MrnFRAxWZK8F5xOE-RZWc5iUziazx0OajQV6pGXX0a4pbWehb-nfNtJPWA1V94qG_lYKL1wOS14imlnyD4bzbK5Nq6f_7_LDXxVK3ahFldO1elYr4Xd8pG2OQ2U7Uaq8nrlsIdRpZfG7GNIb3wuMydfuRYvVuDZeZesLTTbebKxw_H_yTjB4E-8KZYlvW7OoVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b543b1687.mp4?token=H7OLdT4VUvSAg7vCXrfqMqFor-R8bSgsFuEiGRFiWJV3lWl3nVnukh3plxT7mU6lHzPtzMZ_b_7GaJMWX1502F6yfPyjZqgigsP3yuoaj3N7Powl3x0oBNRRT2246mDuA-ASTjna3frvjRp9DHu1MrnFRAxWZK8F5xOE-RZWc5iUziazx0OajQV6pGXX0a4pbWehb-nfNtJPWA1V94qG_lYKL1wOS14imlnyD4bzbK5Nq6f_7_LDXxVK3ahFldO1elYr4Xd8pG2OQ2U7Uaq8nrlsIdRpZfG7GNIb3wuMydfuRYvVuDZeZesLTTbebKxw_H_yTjB4E-8KZYlvW7OoVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: فرانسه با پوشش سفارتخانه و به‌بهانهٔ ارتباط با جامعهٔ مدنی در امور داخلی ما دخالت کرده و باید عذرخواهی کند
🔹
دیروز هم سفیر فرانسه به وزارت خارجه احضار شد و صراحتاً اعلام کردیم که این کشور باید از چنین مداخلاتی در امور ایران با عنوان‌های…</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/farsna/452877" target="_blank">📅 11:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452876">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
ارتش اسرائیل مدعی انهدام ۲ پهپاد در مرز اردن شد. گزارشی درباره منشأ این پهپادها منتشر نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/farsna/452876" target="_blank">📅 11:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452875">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0f6ac7d6.mp4?token=EWAo79GT6DGHSK898mQs-u2KVFwynQ7dyr5hOXcuob6rOp9SpNvu-XtaR4FQM4wdFaO5C6EC1G29cyGyYlOCQn2BmRt7VrvVgEsb0pi8FSSUJmnJNz_A-DAknDjzvFtNhFlFoQyCz-lhZMqOBuP-JXEJjymVMx0Kbz3zC-cwr6FvwTxdfyq73aZMRUzx_q4gLX324IM4JkZU_ZA-yq9tN9Sv_V07kPnXBcm53e9IbT-ERylsNhiA_1MnunjruyeMBDsQ8nqT18OQFtFx5jGFKpDQywNmCFWWvgACzO9ZZ975E0LqR1CEBTj84NVuR1xuy2Pi1kcBCfT4a7JEJ7GxUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0f6ac7d6.mp4?token=EWAo79GT6DGHSK898mQs-u2KVFwynQ7dyr5hOXcuob6rOp9SpNvu-XtaR4FQM4wdFaO5C6EC1G29cyGyYlOCQn2BmRt7VrvVgEsb0pi8FSSUJmnJNz_A-DAknDjzvFtNhFlFoQyCz-lhZMqOBuP-JXEJjymVMx0Kbz3zC-cwr6FvwTxdfyq73aZMRUzx_q4gLX324IM4JkZU_ZA-yq9tN9Sv_V07kPnXBcm53e9IbT-ERylsNhiA_1MnunjruyeMBDsQ8nqT18OQFtFx5jGFKpDQywNmCFWWvgACzO9ZZ975E0LqR1CEBTj84NVuR1xuy2Pi1kcBCfT4a7JEJ7GxUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: بزرگترهای زلنسکی مراقب باشند که پیامدهای اقداماتش دامن‌گیرشان نشود
🔹
رژیم اوکراین از ۴ سال پیش کشورش را در حد ابزار دعوای ژئوپولیتیک بین قدرت‌ها پایین آورد و به‌جای نجات کشورش از جنگی که بر شرق اروپا تحمیل کرده، مدام دیگران را شماتت کرده…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/452875" target="_blank">📅 11:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452874">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30b0f07414.mp4?token=HSUyG79PYUQNyLfxJOQXISu8u1UEmYpVtG3IPHzUymrV5gnnsfOwnqF5oeQ22UzzGO_moQvfNEKEuxHbD8XS3MUh2ujPQQ_YzNuh3JuJESMnwFGU0tPrOAyg31LwjQy7GZi5FnsatkDllvwXbDCS7YT1N9qW8YFuBmd204iy--FkiqxpD2UuIksQ0Nd215QQ38-A5BrymmpOVxQpzyK3FgoNIHeoN00JvYG4cmKrsmjHupmNl2EOwOY4p6EF1bmuJrxD6DD926M6MmPAOlrU7RmpjPg9RT1RFO-0SXDv61fw9TT0sVfBvdYWpdpLtfHYuCi0DZ87zMkpQqmrVLxdhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30b0f07414.mp4?token=HSUyG79PYUQNyLfxJOQXISu8u1UEmYpVtG3IPHzUymrV5gnnsfOwnqF5oeQ22UzzGO_moQvfNEKEuxHbD8XS3MUh2ujPQQ_YzNuh3JuJESMnwFGU0tPrOAyg31LwjQy7GZi5FnsatkDllvwXbDCS7YT1N9qW8YFuBmd204iy--FkiqxpD2UuIksQ0Nd215QQ38-A5BrymmpOVxQpzyK3FgoNIHeoN00JvYG4cmKrsmjHupmNl2EOwOY4p6EF1bmuJrxD6DD926M6MmPAOlrU7RmpjPg9RT1RFO-0SXDv61fw9TT0sVfBvdYWpdpLtfHYuCi0DZ87zMkpQqmrVLxdhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی بزرگ کارخانه‌های اسرائیل در نزدیک غزه
🔹
آتش‌سوزی مهیبی صبح امروز منطقهٔ صنعتی شهرک صهیونیستی سدیروت در شمال غزه را فراگرفت و با سرایت شعله‌ها به چندین کارخانه مجاور، خسارات سنگینی به تاسیسات تولیدی این منطقه وارد کرد.
🔹
برخی منابع محلی احتمال می‌دهند که این حریق بر اثر اصابت ترکش‌های موشکی از نوار غزه رخ داده باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/farsna/452874" target="_blank">📅 11:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452873">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRaThNNDMoDrbts0ME7KekQrCWJ7j8wVgefNSO6YSVqmWTRyDgk_ZemGoH7Lfb7ZBNL3BKAPEsE4J69dssJDJsdZALZ8MiT4CfPqxxp-lC1Fit6uLKiNjO8MNy1F9Qpdq82AP5ld1pIZRyu-RkCxzB6lGrx1vW1nZmQMtIcHdivtyyyE9YuV--sVmcPvNbMJ3MWJ-rkGyREFP_VyPt6be1gT5mbM4kUzBsdTfxY7UWL8K6ty8sGrAQM7Pj9hE08hff4iuVMhLHMuiFMmaOCmOz9XTHDwVIm9VlruGpwl7PSeq5TRyz6BfAiOpRpuBV-4XJniYERZ88ornSnxBrdIMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجمع هلدینگ خلیج فارس لغو شد
🔹
مجمع عادی هلدینگ خلیج فارس که بنا بود امروز هیئت‌مدیرهٔ جدید را معرفی کند، به‌دلیل آنچه عدم اعلام حضور نمایندگان سهام عدالت عنوان شد، از نصاب افتاد و لغو شد.
🔸
این درحالی‌ست که نمایندگان سهام عدالت ساعتی قبل در مجمع فوق‌العادهٔ هلدینگ برای افزایش سرمایه حاضر شده و رای داده بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/452873" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452872">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f262d61d8.mp4?token=OSaDtDBkSfn1-edeofTQZrbT8T-XshuzgdiDVWnhtsTZCQa-QKgusj8LGG4OSJvwyKv31KATtnA0w8JQTG3UkcPVbfbEq8Y08rRKVTFF4H_R8rvgp3D3QEi3-VePFx63qjnvI3MLDhxf3-bfC6eZxIeymF0mdWWvbQm2NFRCghYpgVpbOWoHcoLfJ8LdsSVjkJcw3EYsHKUEeV6NfC-tArMCDZd5DudEppBEussahpZTiUD6dfJ0dLsr-nAXFamtsGQfih-gx8F5kNBUFjiTRJTIajfJ7nffbdDGCJEkg7JaILof_76W4eKedslg1enwbpI-K8fwb8VvIrx-8aLwOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f262d61d8.mp4?token=OSaDtDBkSfn1-edeofTQZrbT8T-XshuzgdiDVWnhtsTZCQa-QKgusj8LGG4OSJvwyKv31KATtnA0w8JQTG3UkcPVbfbEq8Y08rRKVTFF4H_R8rvgp3D3QEi3-VePFx63qjnvI3MLDhxf3-bfC6eZxIeymF0mdWWvbQm2NFRCghYpgVpbOWoHcoLfJ8LdsSVjkJcw3EYsHKUEeV6NfC-tArMCDZd5DudEppBEussahpZTiUD6dfJ0dLsr-nAXFamtsGQfih-gx8F5kNBUFjiTRJTIajfJ7nffbdDGCJEkg7JaILof_76W4eKedslg1enwbpI-K8fwb8VvIrx-8aLwOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: آمریکا می‌خواست در ۳ روز ایران را تسلیم کند اما حالا بعداز ۵ ماه در باتلاق خودساخته گیر کرده
🔹
تصمیم‌گیری دربارهٔ منافع ملی کشور معادله‌ای چندمجهولی است که در یک روند مشخص با مشارکت همهٔ دستگاه‌های تصمیم‌گیر انجام می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/452872" target="_blank">📅 11:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452871">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/op1kY1Fo5fJL_lvYxconhmaDL_HoiNLBwWiAvlYtEhbdJINJIbdMocMloNqDm201ckKzRF5LkCx_SRALSlgYjYPccWxTVDW16WE1m7Upf5eF8D1OycDgA2VEKjdMsj7TmM0aoKIpR9peFxhCbX35N8zs8v83h-garpOcGsD3aVwp6oKuFloHABZ2o3FAxGHHpsGMsicOle9ZlRSanJdx9NGN06hgwzYviKMXaAhZS13iAbRB3HelJZp6V4HpWQ8bpqe67lMtiYzZtXDBoCcSgy1ITcUfm8mkv_3uyEF8cg6LSw7KLuWtnKxFSyoFZVNC9vIoqEM1m5rUlNmJ5GiTLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ مسیر ویژه برای زیارت مرقد رهبر شهید ایجاد شد
🔹
با تغییرات جدید و گشوده‌شدن رواق دارالذکر به روی زائران ۴ مسیر ویژه زیارت مرقد رهبر شهید در حرم رضوی ایجاد شد.
🔹
در مسیر نخست، زائران آقا از صحن آزادی وارد رواق دارالسرور شده و پس از عبور به روضۀ منوره مشرف می‌شوند و در ادامه از مسیر دارالعزه به رواق دارالذکر هدایت خواهند شد.
🔹
مسیر دوم نیز آقایان از طریق مسجد گوهرشاد و شبستان گرم، به رواق دارالعزه و سپس رواق دارالذکر هدایت می‌شوند.
🔹
برای بانوان هم زائران از صحن بعثت وارد رواق دارالعباده شده و سپس از طریق رواق دارالزهد به رواق دارالذکر مشرف می‌شوند.
🔹
مسیر دوم بانوان نیز از طریق مسجد گوهرشاد، شبستان گرم و سپس رواق دارالزهد، به رواق دارالذکر ختم می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/452871" target="_blank">📅 11:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452870">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e738b35e9c.mp4?token=czy7XaZwxDIv-6CrgV_2pw4DWg5DK9bWCzyuADwGcgqqHyPao4aM3OW19DUsWL5-Rnwe0JlHBTTylaenkUJCvYoHVN27hlz38oSqaxQu_xIeTEj9HR9k3Q2k7qs4-NAFjQP3-Xu7gVZkDwgIC1IF3uMdnXYzs05VRqJfB6eAvk8b9Te1sai36_JZIRoCFM1xPwjpWNxM_VuKYo0Ycg0Tm_i6o70zwzjajYd-KfKjFh7afWSR4e0EwOH9HrhU4uZ1lRjGLOXVx75MxM8WfRappyRUu42W9JLmWYtNxCVMSWDg4e7YriVfB5W0IbLjaFv-8nK0QZEkHDmjXgNicFH_2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e738b35e9c.mp4?token=czy7XaZwxDIv-6CrgV_2pw4DWg5DK9bWCzyuADwGcgqqHyPao4aM3OW19DUsWL5-Rnwe0JlHBTTylaenkUJCvYoHVN27hlz38oSqaxQu_xIeTEj9HR9k3Q2k7qs4-NAFjQP3-Xu7gVZkDwgIC1IF3uMdnXYzs05VRqJfB6eAvk8b9Te1sai36_JZIRoCFM1xPwjpWNxM_VuKYo0Ycg0Tm_i6o70zwzjajYd-KfKjFh7afWSR4e0EwOH9HrhU4uZ1lRjGLOXVx75MxM8WfRappyRUu42W9JLmWYtNxCVMSWDg4e7YriVfB5W0IbLjaFv-8nK0QZEkHDmjXgNicFH_2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه خطاب به اتحادیهٔ اروپا: شما که هرازچندگاهی به بهانهٔ حقوق بشر بیانیه‌ای علیه ایران صادر می‌کنید! آیا کودکان میناب ایرانی نبودند؟!  @Farsna</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/452870" target="_blank">📅 11:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452869">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da97f47adf.mp4?token=EH_USHbJQUsyLp1zXwZWQe9_awZIbZmkDtVvHZ_bSuu1N-UCpSs6g_OFaBP9yC0ejQJfs0re8CFm0h1s_ySKr7pB5VKlEDdqMGRvSFO5IC3MCCft-coghmPumHQLxBH0zDwXqWEssZeCZiojTmJut0KV7g6XlXy5xJ7VSVisuogJ6Ie0Y1mAjhta7ldUQSv552vGhtkRpxNb2sGrqut1zl8scFeSKl-Fpgxx5ZXVM9UDLK973YZAiJgzZU78gwOhTC2RIJCKONy9_8ozq74uFzLEUQYJapOGS-F3o3R1zB56loR7R8osyQ_FLfKMoOqOz_Ze8aJC8TK5kJJkeu0rGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da97f47adf.mp4?token=EH_USHbJQUsyLp1zXwZWQe9_awZIbZmkDtVvHZ_bSuu1N-UCpSs6g_OFaBP9yC0ejQJfs0re8CFm0h1s_ySKr7pB5VKlEDdqMGRvSFO5IC3MCCft-coghmPumHQLxBH0zDwXqWEssZeCZiojTmJut0KV7g6XlXy5xJ7VSVisuogJ6Ie0Y1mAjhta7ldUQSv552vGhtkRpxNb2sGrqut1zl8scFeSKl-Fpgxx5ZXVM9UDLK973YZAiJgzZU78gwOhTC2RIJCKONy9_8ozq74uFzLEUQYJapOGS-F3o3R1zB56loR7R8osyQ_FLfKMoOqOz_Ze8aJC8TK5kJJkeu0rGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه خطاب به اتحادیهٔ اروپا: شما که هرازچندگاهی به بهانهٔ حقوق بشر بیانیه‌ای علیه ایران صادر می‌کنید! آیا کودکان میناب ایرانی نبودند؟!
@Farsna</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/452869" target="_blank">📅 10:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452868">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کشف جسد یک نظامی زن در مرکز فلسطین اشغالی
🔹
پلیس تحقیقات نظامی رژیم صهیونیستی از کشف جسد یک نظامی زن در پایگاهی در مرکز فلسطین اشغالی خبر داد؛ به گفتهٔ این نهاد، تحقیقات در این باره آغاز شده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/452868" target="_blank">📅 10:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452867">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40df3041a.mp4?token=J_U13S9JmeMvT0ojMEsQPEa3i2UjC1UAyXwRr7I6W8GJMnOr_hOTRWcPZmD-Q1VcgmQGfxzyLgkli64GSJivfXhmBmzWUtfrApmQooFPTmsvsQr8u5EPXjWRlYKpVVnZSEl6ECGq1g8v3sQDCeA6seepRhjTGezFb7h-wCcfYTgxi5fMrP2-WUA4qqx7hqJMxpIC5aCkuqUo2PGvCYMPa-LF_hje9YILNs3ebwFLIMDngOVVIPhUJwR9yDwGNU07I52ujfHDg7xjOfN4_t46pJ0dx4UvhDzAO1YJzuUr4Gbm6XlanXoWITjXxtTOYWvmH5aQTd6xnD7aFB3nk0TfCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40df3041a.mp4?token=J_U13S9JmeMvT0ojMEsQPEa3i2UjC1UAyXwRr7I6W8GJMnOr_hOTRWcPZmD-Q1VcgmQGfxzyLgkli64GSJivfXhmBmzWUtfrApmQooFPTmsvsQr8u5EPXjWRlYKpVVnZSEl6ECGq1g8v3sQDCeA6seepRhjTGezFb7h-wCcfYTgxi5fMrP2-WUA4qqx7hqJMxpIC5aCkuqUo2PGvCYMPa-LF_hje9YILNs3ebwFLIMDngOVVIPhUJwR9yDwGNU07I52ujfHDg7xjOfN4_t46pJ0dx4UvhDzAO1YJzuUr4Gbm6XlanXoWITjXxtTOYWvmH5aQTd6xnD7aFB3nk0TfCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قدم‌زنان به‌سوی نینوا
@Farsna</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/452867" target="_blank">📅 10:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452866">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ابلاغ نسخهٔ جدید دستورالعمل واگذاری اموال مازاد بانک‌ها به شبکهٔ بانکی
🔹
براساس اصلاحات جدید بانک مرکزی، علاوه بر مزایده، روش‌هایی مانند استفاده از سازوکارهای بازار سرمایه، واگذاری به شرکت مدیریت دارایی‌های شبکهٔ بانکی، توکنایزکردن دارایی‌ها و در برخی موارد مذاکره و معاوضه نیز برای واگذاری اموال مازاد مجاز شده است.
🔹
همچنین امکان فروش نسیهٔ دفعی در کنار فروش نقدی و اقساطی پیش‌بینی شده و بانک‌ها موظف شده‌اند دستورالعمل جدید را به تمامی واحدهای مرتبط ابلاغ و بر اجرای دقیق آن نظارت کنند.
@Farsna</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/452866" target="_blank">📅 10:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452865">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72e331961.mp4?token=SeFnXVEgkq2d4QRdJveT1cH4zfKCMHF-r3nLgxfvIj989Wsv46tKGQ8gKF4FCget7HC3j9dq_6Kd3AlaBvzyZtl27kgrjUrzcqAsGAwXzmw0TL_lMwzY--hHzeBU2Up8AYbWO2ISQeH1XofPp5qCQsUbnHdV5yxY8PoB5OyxZ1Txc5jerulNvXg5k20OHlnxno_LpZlgGPD4IcmHaqxT3JKTuFxzt-q6opk4xf2Cv_7bKTCPxSOHQiHwH4UiqwlPY3LU1xFJw6QdkXNotXVtkfVU_hPl7_maQMVpg9n8HtNQMJa56vRxml9w5ea59Jk9HmY46dJ6-bgh7_BjfOdExw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72e331961.mp4?token=SeFnXVEgkq2d4QRdJveT1cH4zfKCMHF-r3nLgxfvIj989Wsv46tKGQ8gKF4FCget7HC3j9dq_6Kd3AlaBvzyZtl27kgrjUrzcqAsGAwXzmw0TL_lMwzY--hHzeBU2Up8AYbWO2ISQeH1XofPp5qCQsUbnHdV5yxY8PoB5OyxZ1Txc5jerulNvXg5k20OHlnxno_LpZlgGPD4IcmHaqxT3JKTuFxzt-q6opk4xf2Cv_7bKTCPxSOHQiHwH4UiqwlPY3LU1xFJw6QdkXNotXVtkfVU_hPl7_maQMVpg9n8HtNQMJa56vRxml9w5ea59Jk9HmY46dJ6-bgh7_BjfOdExw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ زنبورها یک مسابقهٔ فوتبال را متوقف کرد!
🔹
حملهٔ ناگهانی دسته‌ای از زنبورها، فینال فوتبال زیر ۲۰ سال برزیل را برای دقایقی متوقف کرد و بازیکنان و داوران برای فرار از نیش حشرات روی زمین دراز کشیدند.
@Farsna</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/452865" target="_blank">📅 10:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452864">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سپاه: عملیات مرصاد درس بزرگی به خائنین داد که هوس هرگونه تجاوز را از سر بیرون کنند
🔹
سپاه پاسداران در بیانیه‌ای به مناسبت سالروز عملیات مرصاد: در پنجم مرداد سال ۱۳۶۷، ملت ایران با تارومار کردن منافقین فریب‌خورده، درس بزرگی به خائنین به ملت و میهن اسلامی داد…</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/452864" target="_blank">📅 10:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452863">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">انهدام ۲ مرحله‌ای مهمات عمل‌نکرده در پاکدشت
🔹
سپاه استان تهران: انهدام مهمات عمل‌نکرده در پاکدشت امروز در ۲ مرحله از ساعت ۹ تا ۱۱ و ۱۴ تا ۱۷ انجام می‌‍شود؛ احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/452863" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452862">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-Vvh9KmwWcecI697_GvkdWojVtIAk4s1Y5ZiQ5F38JjSHcat7G6ZW8z1R0sWiIBgOcJ2hBy8ouPpuo_nn08T6YVZ6KMEDjz8zTl3ZUe6SldeeFG1NgwDrbwrB0yOrujnjcPUsTweMPfYOFsOysYGPYb9EVo_6qLgQvagIAFpRRv1i5MebBj5xJqj64A4Z2MQf__cuKOzcIIiBfvXxvM0janooON0bETCh_caDqhriKahE_Nt6uojSG66BS_ZKTB-1IVMi5wew147IFeJ_96HM19DJZP2Q0jTUu9968FCjLDcTUFjcB26_KYX9RcoxsjeU7hM6xpvAXOqIkBz9kTSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن ۳ نفتکش سعودی را هدف قرار داد
🔹
المیادین: نیروهای مسلح یمن طی ۴۸ ساعت گذشته ۳ نفتکش سعودی را هدف قرار داده‌اند.
🔹
تعداد کشتی‌های عربستانی که از دوشنبه گذشته تا امروز برگشت داده شده‌اند به ۱۶ کشتی رسیده است.
🔹
این منبع همچنین خبر داده که  از زمان آغاز محاصره…</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/452862" target="_blank">📅 09:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452860">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xt0MUbpMjaiJJtf6nZOwMBfpxunNDoBuRT-LQ6q_7vznQ7TDyJkppzEmgFpT0JUkp5QMK18JFF-d5MqSUMem_GgnJ-I7dMKEn3iUrHNxuoYnwUvZr0wVoNxSWtcM7s9DfM79KTjBfp0dOhY_mM759gu1btC1CJmEaotcK44DrEoUZWWd-eEs_33dA5AnafJfzsntRi7Nrvzfo5ryniWeKma1A-njCeZPhVv_E45rsdQ95XSjRePPLspWBZY2vnc-A1juORU1M2Kw6KbH9WujWMaggBjaYRMznoDIlt4Ppt20umPSPcRyZKQfL7MLoDmfwBMHN7xP_x9SS05xk3PEgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mnLNZ_FaNtlsBK1WmznQSnId0DyEmZ7a4BNZz1NlqjyXDpMvEWPntbdHw4F1EeuqCyGNloVdy7UVMUcRiXzg4Lr9NKQtCJymtd6Oi9kYFQmchluU1cOuoJM1r_L2dPDPgtsw6w2DXkH1d5v_hNtmStY06FEYVjrrcR8vbCUE1dmB8k7N2yNpfJJn-Y-pYDUY5nPHpP6jhucQ1eyj8-PPRmYV2ZvT406v8d4Wktd_1U_XYEsN4lqUyBxulgxMSQca2GN2DMD-HheM4fh8L0AduKiQ5I2Q1jGJgHTFzIpLAHYbPvXlBmvrW0IBm7L6iDWc3a1ZGaApDahVzQ-l6fJjEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ضرر ۳.۸ هزار میلیاردی مدیران دولتی روی دست بازنشستگان
🔹
طبق جدیدترین صورت‌های مالی شرکت سرمایه‌گذاری تأمین اجتماعی (شستا) این شرکت نه‌تنها در پایان سال گذشته سودی کسب نکرده، بلکه زیان خالص آن از ۲.۲ هزار میلیارد تومان به ۳.۸ هزار میلیارد تومان افزایش یافته است.
🔹
معاون پیشین وزیر کار علیرضا عسگریان می‌گوید شستا بین ۲ تا ۳ هزار عضو هیئت‌مدیره دارد که «۸۰ درصد آن‌ها سقف حقوق را دریافت می‌کنند و برخی حتی با تخلف، بیش از سقف حقوق می‌گیرند.
🔹
گزارش تحقیق و تفحص مجلس از شستا در سال ۱۴۰۳، ریشۀ تخلفات و سوءمدیریت در تعدادی از شرکت‌های زیرمجموعه را به‌کارگیری مدیران فاقد صلاحیت، تعارض منافع و ضعف عملکرد هیئت‌مدیره‌ها عنوان کرده بود.
🔹
شستا در مجموع ۶۲ شرکت زیرمجموعه دارد که از جمله آن‌ها می‌توان به بانک رفاه، شرکت ملی صنایع مس، شرکت ملی نفتکش ایران، لاستیک ارگ کرمان، پتروشیمی ایلام، شرکت نفت ستاره خلیج فارس، سیمان شاهرود و سیمان فارس و خوزستان اشاره کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/452860" target="_blank">📅 09:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452859">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5z-YOkjU2BqHU7dTTnrPRtGvztd9ZFuvRRRK_yGmVr8LLlJLvp0qJQn4F6oeivgp3pUEo7Qo2qUl5lY4PrzJEbbiyt1m8YVO-0v4daRWG3arg9VkZ2HGE5sDDQMMxVVdLy_0c3C8iSwATS783y-h9TbvcYI9NMS4ikulfrdy3bWx0zmca-OO4UA3-2BP95fRXsXR8VmP7djeWi7nnme9aUQ-OHXPYXOM7h8240qDad27Z0ZP6ldcvYiPHgRHq6dpnWugqaO28DM40dptvrjhh4hfEejKp9m8Ofhc0k69ohp6gKbe7qCa_dr-GQfdaFkejMkFl4pTpm7DcQWiTuMjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ ساعت صف برای چند دقیقه زیارت ضریح امام علی(ع)
🔹
ورودی بانوان حرم علوی به یک مسیر محدود شده و زائران باید ساعت‌ها در صف بایستند و از میان مسیرهای نرده‌کشی‌شده عبور کنند تا به ضریح برسند.
🔹
حسین العباد، یکی از خادمان حرم می‌گوید: برای اینکه جمعیت یک‌باره به‌سمت ضریح نرود، زائران را مرحله‌به‌مرحله وارد می‌کنیم.
🔹
بانوان پس از ورود به مسیر تعیین‌شده باید صف‌های طولانی و چندمرحله‌ای را پشت سر بگذارند که در روزهای شلوغ اربعین، این مسیر گاهی بیش از ۴ ساعت تا رسیدن به ضریح طول می‌کشد. پس از آن هم زائران باید بلافاصله محدودۀ ضریح را ترک کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/452859" target="_blank">📅 09:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452858">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ffb7c01e9.mp4?token=cVdNtEtD92aPr2BI1iywDuCFxO2_vMhP3OtneXdnQM4UnlHCUye1cBuKmSO3n4lc5lGT6n27mef-8g0fBkON6LNULXeG-cYRa9pRTdM5_aTbwOSAaNfbaiD7D3w8CGavNT_G9fHox0jyt104oI7FfCrxkCK26AxuKKbVcDpmOSOq9OXXa0yMh6_boJY_pJkgzNSzbNjMmMzOn0B3yqR0d-qGrJS1wklUghdMmYD8SyV7ky9WtF8pgucNO0S6SPH-YAEB1X9b4rMJS7h84Q3fskFGtehKH8TvkwpvZtIBH-d3l8c4Vhd6oB249Eoi78Z_0rifTDaG5S1RfbxGc8xnfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ffb7c01e9.mp4?token=cVdNtEtD92aPr2BI1iywDuCFxO2_vMhP3OtneXdnQM4UnlHCUye1cBuKmSO3n4lc5lGT6n27mef-8g0fBkON6LNULXeG-cYRa9pRTdM5_aTbwOSAaNfbaiD7D3w8CGavNT_G9fHox0jyt104oI7FfCrxkCK26AxuKKbVcDpmOSOq9OXXa0yMh6_boJY_pJkgzNSzbNjMmMzOn0B3yqR0d-qGrJS1wklUghdMmYD8SyV7ky9WtF8pgucNO0S6SPH-YAEB1X9b4rMJS7h84Q3fskFGtehKH8TvkwpvZtIBH-d3l8c4Vhd6oB249Eoi78Z_0rifTDaG5S1RfbxGc8xnfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: از فردا باید منتظر کاهش دما در نیمۀ شمالی کشور باشیم
🔹
امروز در بیشتر مناطق کشور هوا گرم خواهد بود. دمای هوای تهران به ۴۰ درجه می‌رسد.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/452858" target="_blank">📅 08:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452857">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48f62fbaa4.mp4?token=gDUhT5CMWjCSllyFG4BN1QK-oT8g3o69llWPT9nCm8nx7kO6WK0sxgY4UfeeIo6OIspOcuB1Lb-3KSJS01Xr5Gssx-lOEcnwz19vShYsrMtaLOoMS3R82v-Irl8xgx86UGatQTR0tRlPI_Eqpj6k2YO_voKsJ5IObAf0ckNbfGW9pzNakU5ec3fkrijSMCk1K6sarfpByxrdkVTfyD_ARFtQcUB6fGRBKlC_tEccHrWKvGPuTL5zLJpz1buf8CCMyUW3P0Py6ebn4l7q40YZCPz-gk-DCIY3JdS2SuYjyEy-Y4EeIUcn802KutAExSirtsE9YtZKIbkK_C85QxoYXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48f62fbaa4.mp4?token=gDUhT5CMWjCSllyFG4BN1QK-oT8g3o69llWPT9nCm8nx7kO6WK0sxgY4UfeeIo6OIspOcuB1Lb-3KSJS01Xr5Gssx-lOEcnwz19vShYsrMtaLOoMS3R82v-Irl8xgx86UGatQTR0tRlPI_Eqpj6k2YO_voKsJ5IObAf0ckNbfGW9pzNakU5ec3fkrijSMCk1K6sarfpByxrdkVTfyD_ARFtQcUB6fGRBKlC_tEccHrWKvGPuTL5zLJpz1buf8CCMyUW3P0Py6ebn4l7q40YZCPz-gk-DCIY3JdS2SuYjyEy-Y4EeIUcn802KutAExSirtsE9YtZKIbkK_C85QxoYXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پنل‌های خورشیدی به دادِ کشاورزان بویین‌میاندشت اصفهان رسید
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/452857" target="_blank">📅 08:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452856">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
مدیریت قاطع ایران در تنگۀ هرمز/ حادثه برای یک کشتی
🔹
یک مقام آگاه: ساعاتی پیش و در ساعات اولیۀ بامداد امروز، ۶ فروند کشتی متخلف با خاموش نمودن سامانه‌های ناوبری و موقعیت‌یاب خود و نیز با تحریک ارتش کودک‌کش و تروریستی آمریکا قصد عبور از مسیر غیرقانونی و ناایمن جنوب تنگۀ هرمز را داشتند که یکی از آن‌ها دچار حادثه شده و بقیه تحت مدیریت قاطع ایران به خلیج‌فارس برگردانده شدند.
🔹
همان‌گونه که قبلا هم اعلام شده بود مسیر تردد در تنگۀ هرمز مسیر مشخص شده توسط ایران است‌ و مابقی مسیرها آلوده است و راه به‌جایی ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/452856" target="_blank">📅 07:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452854">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caa96a9605.mp4?token=pLyd_SJyQfpBCTLXu5_f-fl2S82RQGTnf9AtX4VUn5q6iC9tvNa6-TqwABLtjEMzA8acFirBZdOs20erM98-DCuJDZdK2_NuyQXfcV1aXUejCtAkatSXO9ziuRxh5pvQfTVQeMy-PErCjYl9IuVsUYZr8oDEwTsz4Q229ltQCZgQzIs8I7NTkit0_lZy76WCGGImunSyvb6-snHdIo_AzvB2nGDMPiYVSLFs6QYfRizYvsdeVbcZ5AnWsg7lbYBwShAzZM1JvlIZBxpgXySh9RRsvp8eh_TJbpMFtAXUs1vUjM51BhQ8XVbVR-cWBvBUMPZtOfphcwhbn_9x7s59KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caa96a9605.mp4?token=pLyd_SJyQfpBCTLXu5_f-fl2S82RQGTnf9AtX4VUn5q6iC9tvNa6-TqwABLtjEMzA8acFirBZdOs20erM98-DCuJDZdK2_NuyQXfcV1aXUejCtAkatSXO9ziuRxh5pvQfTVQeMy-PErCjYl9IuVsUYZr8oDEwTsz4Q229ltQCZgQzIs8I7NTkit0_lZy76WCGGImunSyvb6-snHdIo_AzvB2nGDMPiYVSLFs6QYfRizYvsdeVbcZ5AnWsg7lbYBwShAzZM1JvlIZBxpgXySh9RRsvp8eh_TJbpMFtAXUs1vUjM51BhQ8XVbVR-cWBvBUMPZtOfphcwhbn_9x7s59KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی مرگبار در سیاتل؛ ۲ کشته و چندین زخمی
🔹
در پی تیراندازی در یک جشنواره غذا در شهر سیاتل آمریکا، دو نفر جان باختند و دست‌کم چهار نفر دیگر، از جمله یک کودک دو ساله، زخمی و به بیمارستان منتقل شدند.
🔹
به گزارش سی‌ان‌ان، مقامات آمریکایی تاکنون اطلاعاتی درباره هویت یا انگیزه عامل تیراندازی منتشر نکرده‌اند و مشخص نیست که آیا فرد یا افرادی بازداشت شده‌اند یا خیر.
🔸
بر اساس آمار سازمان «آرشیو خشونت مسلحانه» (Gun Violence Archive)، این تیراندازی دست‌کم دویست‌وهفتاد‌ویکمین تیراندازی جمعی در آمریکا از ابتدای سال جاری به شمار می‌رود.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/452854" target="_blank">📅 07:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452853">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">امروز هوای پایتخت ناسالم است
🔹
بر اساس اعلام شرکت کنترل کیفیت هوا، شاخص کیفیت هوای پایتخت امروز روی عدد ۱۰۳ قرار گرفته و در وضعیت ناسالم برای گروه‌های حساس است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/452853" target="_blank">📅 07:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452852">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbdFyAKyj68FB6nZtjyMmHdDCClfey9paqlvbOeSnFaTGmz3BHPNzMxfu25BCCc60RokO-vepzXoJQ7yjcoTKVUMInshwZdswGtvS8QOcASJD-tAUwtIfLEfhSo5cgSfg8QZqOYK1JMm_IaN72jcQtC9KldhF5EtLSYHlCh2fzndmIHvmA73JSy1PgZNTSCKrCKC-Z16fNXl5Prhq-bMVU-EodYIjtFT0C65u2ChTDHUptxY5pl7C2PlcLkjvjl_DiDFsNVFbTjxfzxGeZe_uUmwAfyFdC2-ddj55tbl3s_eUZr9nc2FaYiW0IxJ5A-tqBXHhrHjwIR_mAq_Ad2SwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وسایل گمشدۀ زائران اربعین به خانه پست می‌شود
🔹
سال گذشته برای نخستین‌بار، وسایل گمشدۀ زائران در عراق که دارای کد شناسایی سماح بودند و صاحبان‌شان در مسیر پیدا نشده بودند، به نشانی ثبت‌شده در سامانه ارسال شدند.
🔹
امسال هم این طرح ادامه دارد؛ زائران باید پس از ثبت‌نام در سامانۀ سماح، کیوآرکد شناسایی خود را روی وسایل شخصی و حتی تلفن‌همراه نصب کنند تا اگر وسیله‌ای در عراق گم شد، یک اسکن ساده آن را به صاحبش برساند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/452852" target="_blank">📅 06:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452847">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uh52dQlzT0pO6YBxyIIVKYkx2WcSkswY4x7J_Osd_jUVYoXCFCEWoZ57-XIcixz3Xj4oCBrAfs-5nRjxoPstsi9FeVuNrVUlqKP-sV2Wrt8cvLmxichM5mVQaeSsjdF1u6xgdPLiydNTHQ0rovy6MWAGRQOi0dS99n-qJYR7rjdCT9vZxwKHzpJzMBWx4t_FJR3WPTxCOMORCmOH2xgwRci78ze4crYFDXpAf-SlsOcDdoV2riRbHzsihfjK9G8EcErIdnPZ5kF5LtSxtBwV3TWVcynotwdT_nTKDWWZCgNbRSIn072RTFb7iRozMUBOzPIx1aTrzcdcwO76qNss_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jVZNq9vkD6OYIneO2KCMSxZ5YkE7NTEhSQMaGyXfZhDpeCCCM-QnFlnKoCV96SM3tVExtAoEtZ5SfR6eet6B2VODGEZ3LAV-l-DS7Tdl9ZFsxsdQQ_4BkvRpzLgZxfqrt_bCrjdwwZJYqRiKyKmm29cFceYs3-JxHMAeIs6rI8Nf6PuABoD8ePFnNmJSDAJPR6iMhz9_ScoQwsa3YAA4-pntckITblOoX6bTrpgyS_fToBBZ_g7MGWGVgurAVQcuwxpBmGSLZeUxxo7wRmvjb06pnD3o_yK_3bGjX2GAeeh6QgyvuJCi7TReoKzcgM3d5Eues8eH3PdPde4OsTz2aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lIJSboXnDBV50nZXyo_EC5YrlprOTZQfCRJj-5Bsu5CeCrJtGtQgdKxRt5SkhXTB2eqCZfy80vBpwT0QxnZZreK0vpx1G3oQHYoHk3DKnrkokMYkR8EZkiSDFYkPnTovrIwP0Oh3nmgm2HnT5sP7binJ2YeaFFyy59GGC_icKAh8Qq1qvH4XSFOgEFuTejwMjPGcWI8_giIqc5yZeooSpqD-FoXG0StkTLOJEczxnSJ_X2ctxHf5t3txUVDEw0_sR6lklMsxgsRY3YWs8m5zIhCJaP2xVT1MPqzeMzNuLInrLYgZQz_oL--Xdd2mPnISFJKKUHzrkcFxXZLF8t0n4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EoyyZnwDHSoB9q06B84dUM8rTVjepyEO2VdU268zVHQiBv6PTmThzvE8CYrPpk6XmyDwN3Ilo17TMWQBmCfCx-1mFRT3Jl3TIinK3zpdBKwZWmVr1OisVICmUQKIiM0li543jwvbN0cT1Kqt630dO7Sw8KY6st68cbWIHCFDTpFg4z9hiqlV9nNKrOp48_9aWzarPgncwUESuwfS04BQrqysIi62zAVDIFp7N-NlaeG0-QnwnCZfMtbTt9USQ17XodrwEWgx_-dzqbPc1IVHGQMIAlJQrc4U1riWhbw5zNPNKjFZq_YpObjGAt_jQsGx_mR-7yxTJ-3yvmfBtQrFEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N41IFuWC_cTSrD_j5OPx-04TgEaxLB8jEKhdiak_FsAN1KbfnuN0F9d-lMDWqcLayGV5TrK64jlvXp9zSPKu0S4hZdh97m7wVBdzl0ykz7-oSRJuYEeYJdSMKkHkiOw7r7M5QeOM-UpyQsE8JP28F-tItBOYZTUH2WcfAdiJltREorZI2GmxiqnPE42B0RoZGxNrDMwrTjoAT_22SDmIaFfct7vudOgG612IVOB7GaGWpv-0fq_igpFqmVIKxCXBlKKa3LuVt-FI4U_IYhN5doJnvxYkS0E-CSV0Eeq6g4TcLvJRUqnbEhn3sheIE_BLS48p7TsHxjD5Uz7sg-gpRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زیارت خانه پدری
عکس:
دانیال همتی
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/452847" target="_blank">📅 05:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452846">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-oe5GyyVjGMEiUyXIz71W7foAJjmOfjhz-uu3fh-dO0ch6pAMDRvXpvsA7wzny7_XDX2M0XHSuPvgcBIw6inMxx6TYtIYJBxDmId28ap99FixfrR_E9rUTZ54llrQ-A1rDrdOs8hNaMLU05pjnA7OK0rVDTP-yC1hJpvqT0WuZEJgwqHeF40RUNEaDJQzDq0BWe3ZvCt9kkV90LPmx3N0SfTplV7b3fzsypxhQ7LIxeZWW3nTlMyGVoWSAm6mG_zSuQL0ghiGhG9CJoesPOaeEbiol854qwaBxsyqKaTsIueIC2jbItRw5ersEwxDJEVZYumY9yz6pIl2nIbvT7Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگرانی زلنسکی از باز شدن جبهۀ جدید جنگ با ایران
🔹
رئیس‌جمهور اوکراین، در توجیه حملۀ پهپادی به یک شناور ایرانی در دریای خزر که به شهادت یک ملوان منجر شد ادعا کرد ایران قبل‌تر با ارسال تسلیحات به روسیه، علیه کشورش اقدام کرده است.
🔸
البته این درحالی است که ایران تاکنون بارها هرگونه مشارکت در جنگ علیه اوکراین را رد کرده است.
🔹
زلنسکی با ابراز نگرانی از هرگونه حملۀ ایران به اوکراین گفت: باید محتاط باشیم و هر کاری انجام دهیم تا جبهۀ جدیدی در جنگ گشوده نشود، اما باید واقع‌بین باشیم. امیدوارم ایران حملات خود را افزایش ندهد، با این حال باید برای هر احتمالی آماده باشیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/452846" target="_blank">📅 04:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452843">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a5PaX55NpEYHjeAj5A-4uWw5ZSIrvaSzBV5AhTC_JoZD97KeS-FP2Kp6VyS6r7qixgCValQAG_jAx4FWyfqIHJHle01xuPzKpyXGbsPI2bJ8XwYlHKDqjovLAr43rstBCeEZi-mU08uqX2ZhgS_8oQy9oZflFdomNvuKJgzydW6qc3KGwoMJSe4qkQNkkfAOWvdWl8JyLo70tzbGP6M5EyRjd3qeYqT_WtWssvx1zvinkTOzzJcWynjx06r0mwMD1itdQsczMS6YHMKYwoJJenT4MPCt1FyLIQ919kQ4ia5xzjB2wH2oq1HGxUTDbj2YbJc9e3k_W9W4trw3D2PyNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TZcbSwhaVXN74h4bE4KZEUclvhG0c9mCBE5QTJ3dIwy3VN653s4OYcTzNY5WPAhv1Hu4vnMg6flo8965euKx6-PFs7cwBXVNNqMF_XFk8RiJd8pPKGo7cRAAG-4cd5uN4kYhGfW4-eCfmEDOffHJQa3tP8un0tnLJn54GBIcw0QuixOuKNdEV0bDFAfQpdjt49FtJkm4pJeuORQE6HVvasKaS7bu--R2xb6AKVKDdaRZURuYZezMXRUA6XxtRY4dXDKK7NLZghDig6kaG8nJrdhUStJyP9OyNkBSJho26kmKWyZWJRaLzNdqxrEQR9WyAgWQxid_3lUmwWMcT5oawg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ac7IFDpjvRIFkYXwAuQh3-nmmdcT1Hl1nirSFRtMJksflBV27LUIQtU_9jgjH-FBguMohfh_htiI75yO6TNpydBfOp0yoHrEkNPg-VlWbtqc-7g1cJUTZMU7OgHuGZdMRTjz7ebjxAz7HP6Bfaeo10wanL_VkZ7D8iLlzC2VaT76F1Yu6Cf4T6plZ_J3AbabSRKSQtYjKvllTgrFtqEEwqBAtAwGxRoFDyGxRgOnGxwCBdzcZWPWU2Vwspt82NCTlx72ki6Cwrc9-uTDMxFkwxpEB8ZSgQVS1CZTy3ZYcTEebfmx5wo6pPMYbTTM_OMc4TAucIk_NbCw6-hZatA8MQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیویورک تایمز: آمریکا در باتلاق ایران گرفتار شده است
روزنامه نیویورک تایمز در تحلیلی درباره گزینه‌های ترامپ در قبال ایران نوشت، رئیس‌جمهوری که تصور می‌کرد قدرتش هیچ مرزی نمی‌شناسد، اکنون دریافته است که با محدودیت‌های متعددی روبه‌روست؛ محدودیت‌هایی که او را بیش از گذشته سرخورده، آشفته و در تصمیم‌گیری و رفتار، غیرقابل پیش‌بینی کرده‌ است.
مشروح این گزارش تحلیلی را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/452843" target="_blank">📅 04:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452842">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7231578114.mp4?token=fuvnPhpPsgCk0YZ9V3Jp1r5bvtYsEBlLlSNKuAPn_kDciQy3C6NCnnkwEJYMkly0hyONL2Kgd90CzZ8JVj5x2SiTJDWyEwpcTMdQ3z-uLtnbHsoVZMNtKDewdIfhyQ3vuTExf9DuTOStd-xwPdczU5HW6EEmvSmp9rSpPTHaUybdSIl3SM_fKQGkbDYePWlEl69s70g65BBe9HkueYWR1fZqng6fn9aYQJnjuqd5h5l6kHpsZNswvXE-WA7RJoh_GSC9V3sg_X0PdsUPp6m8JIlXHSGQGzsatvQ8kG87g3kDfTRXtq_c5FiCXaNOL5nysaFAgre1Vaiqf3zBgsxnmYkBik1kwzajSCzI6u6jj_xVJlJNQ31tKWjcgfqVOSrsZLdRGtEP0nUQ4ZNjNKcBMAU_9ANXmLTD6z-BbdonBN7YkG0t1yOEaJHL6johTocei3EXC9_pXhweRIhmPhwiYTtdoB4vItKS4-Uxr7iCouhl8JihWRt7e6jxUjJnL_WIAc2bkuOKy2E6UZ5PpTxB7xymdvHNKjF7YhS-zTAq0GwOYxz_-Uy_PND9QxTv_2ZBwmgGgZ3pubQyMjbE66QlGFiszENdOwTlSk6hdTUwzLEitvcGqU0vCIG8nQOpMyVZbraMjj5pasIYbZHMmgz4yaDF8i9DTX2Usas3ss8payo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7231578114.mp4?token=fuvnPhpPsgCk0YZ9V3Jp1r5bvtYsEBlLlSNKuAPn_kDciQy3C6NCnnkwEJYMkly0hyONL2Kgd90CzZ8JVj5x2SiTJDWyEwpcTMdQ3z-uLtnbHsoVZMNtKDewdIfhyQ3vuTExf9DuTOStd-xwPdczU5HW6EEmvSmp9rSpPTHaUybdSIl3SM_fKQGkbDYePWlEl69s70g65BBe9HkueYWR1fZqng6fn9aYQJnjuqd5h5l6kHpsZNswvXE-WA7RJoh_GSC9V3sg_X0PdsUPp6m8JIlXHSGQGzsatvQ8kG87g3kDfTRXtq_c5FiCXaNOL5nysaFAgre1Vaiqf3zBgsxnmYkBik1kwzajSCzI6u6jj_xVJlJNQ31tKWjcgfqVOSrsZLdRGtEP0nUQ4ZNjNKcBMAU_9ANXmLTD6z-BbdonBN7YkG0t1yOEaJHL6johTocei3EXC9_pXhweRIhmPhwiYTtdoB4vItKS4-Uxr7iCouhl8JihWRt7e6jxUjJnL_WIAc2bkuOKy2E6UZ5PpTxB7xymdvHNKjF7YhS-zTAq0GwOYxz_-Uy_PND9QxTv_2ZBwmgGgZ3pubQyMjbE66QlGFiszENdOwTlSk6hdTUwzLEitvcGqU0vCIG8nQOpMyVZbraMjj5pasIYbZHMmgz4yaDF8i9DTX2Usas3ss8payo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در مسیر کربلا مقصد یکی، اما نیت قدم‌ها و سختی‌ها متفاوت است؛ شما به چه نیتی قدم برمی‌دارید؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/452842" target="_blank">📅 02:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452841">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0b00bd17c.mp4?token=O0_kwwY8Sad9J06QZeOqPqdu3a6bAMKsevIKJcVnfG4Cvj4B15xwcQSWFYiFwqN70RvIlddhI05LqKRzdG5vdATJOE0WFD_1UtK50n_7mi2BxZicT5HcPnM55Wuu0seel8cosyxpfphQTC9meuPMOKPqOWB-C5MysF5_4zXFjvRO9HkUABQAoM6PoskMqpsl6ZBz-54_ohmH18HI62mQyZyxDqOob58iutJbcKG3a_nXBJmCZiWQrGOhx2YxqmTqY8qx2P-hN9PHOZhT2_B_74-o5M85Nf-6shtIooIsqtccYfpsh2O0P1NAZmPOULGqVbqO_Oie6TF2aQhB9GSTFjw1_wb8hQkQwzNiQCfDQQvWCdl-xAIVlJnkP0EHUsJyqFmjXkZ7creiJl611wXxA2CM-xD1Iywz8LMgtLNWoCn8zGRcwc_lPC47EZowxNbFw1UhHzOFSCVY-E3-VqSGdgr_4gG3ckAZ-rrV7aML06vdtpfsn7q-V_6qwKUisTUIIyzICM1SqEx02cE4UlyNh8hvNkmBhqfKFQVY5su0ZGE_-yxGefJyMpOE05DN9Pk7ojm3pRyn9jM6W2UzHspy5EUyptvI8pgMMgIhclaCLKWjEOG4jjHJCh-dBiP3pLcYs2948ozS5PTR2kqRCnx71pAfTL0xCVdx62_a0TP50nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0b00bd17c.mp4?token=O0_kwwY8Sad9J06QZeOqPqdu3a6bAMKsevIKJcVnfG4Cvj4B15xwcQSWFYiFwqN70RvIlddhI05LqKRzdG5vdATJOE0WFD_1UtK50n_7mi2BxZicT5HcPnM55Wuu0seel8cosyxpfphQTC9meuPMOKPqOWB-C5MysF5_4zXFjvRO9HkUABQAoM6PoskMqpsl6ZBz-54_ohmH18HI62mQyZyxDqOob58iutJbcKG3a_nXBJmCZiWQrGOhx2YxqmTqY8qx2P-hN9PHOZhT2_B_74-o5M85Nf-6shtIooIsqtccYfpsh2O0P1NAZmPOULGqVbqO_Oie6TF2aQhB9GSTFjw1_wb8hQkQwzNiQCfDQQvWCdl-xAIVlJnkP0EHUsJyqFmjXkZ7creiJl611wXxA2CM-xD1Iywz8LMgtLNWoCn8zGRcwc_lPC47EZowxNbFw1UhHzOFSCVY-E3-VqSGdgr_4gG3ckAZ-rrV7aML06vdtpfsn7q-V_6qwKUisTUIIyzICM1SqEx02cE4UlyNh8hvNkmBhqfKFQVY5su0ZGE_-yxGefJyMpOE05DN9Pk7ojm3pRyn9jM6W2UzHspy5EUyptvI8pgMMgIhclaCLKWjEOG4jjHJCh-dBiP3pLcYs2948ozS5PTR2kqRCnx71pAfTL0xCVdx62_a0TP50nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای رواق دارالذکر حرم مطهر رضوی و حضور زائران در جوار مزار مطهر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/452841" target="_blank">📅 01:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452840">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shohFFtIFUodKhTtKZWTLdpFQGbtuvhp5ayjG_Qf9PCKfZT14M2_o_WWZofr4t5XJhmttCanj-PuBFRpRaU70lUOYmhkV7JF0aG2mh9HT4xN4EEEq3siCUtGrWvUUik8hr_kW7vC9Hmb_yn2tw2kqNf6ujGfBOqFiVIGjKgVg5usRejHph151DWDMyZlW5TGzK1mv-x6uZz7T6bIYgOJLQu3Q-PMVVhDUM84ER7pYB7xE2quvo6N89E7b4mrgDHDnI0os-WT-iEqrpbxfhZmUEDML8_ffi-3vM5dkSrUq3axWfJIQEtmBck3oQfO4V_9hUdQrdyqF2BcG4BefaXtFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز دلایل اصلی توقف حملات آمریکا را فاش کرد
🔹
روزنامۀ نیویورک‌تایمز به نقل از مقام‌های دولت آمریکا گزارش داد که دونالد ترامپ، دست‌کم در مقطع کنونی برنامه‌های خود برای گسترش عملیات نظامی علیه ایران را کنار گذاشته است.
🔹
زیرا تشدید جنگ می‌تواند ذخایر…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/452840" target="_blank">📅 01:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452839">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b0730aca5.mp4?token=Wt_J4SUpApnEVmt3IG5nCV3jDe5gvP1Njo3HNhrzx3ztSbDX-B57hAIvDi1aRhJGFfJvT3SYLgz8JV2DocoFFQwNdboU1qR2KZGUKtqyt46Lb6xOeWG2IGvyP2XrpkYmuexW87-FGoFqGegWZD4o4ZSGDejY6VomdxRXw6vpee6-1BYjL52Pu6aIbIKC-AV5IWGF61Jg51_7584pdRmrygk5LndUXQX0HEu8J8j0SQET-vcl_9X-IvCFN2rfBkGoFg2X6koezQpSBfTkP6cmXXBiHPkZfxMZIby3mrMxg2rGWutvVAAisoXKZ4c9572EOkfi5iLTMrXCFqM1snCozZ2s69JxZYZTtW-OStvdsxZ_kMQ2DGzPtWrlIEIzoxgE2oCytPpa0FvdP3jqe9ft7IqNLir0fZjKln-TTdqXurqXTvXMMfHqfd1pEiVL1yNIPEL7tQ4p-He1xZ_PyI_gOyviqm2BxkpfhsO0gtaX3HLxr6PNWMOITYK-GTEb0_ZjlO2dp3RQQxOMvcX1ZsFQex2YOllPCq0EO58U6_ghAMCBsDje6oDyuvTxstnphdkfEK84CxdtEqg7xLF84wKTqUou4nyVClvYpM_XHeAUQl4mSgILh2eMypTffAjs27WxrgRtkh0p_nZXA0vQVRvihk13Js8QCb2cBpe-xJnBshE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b0730aca5.mp4?token=Wt_J4SUpApnEVmt3IG5nCV3jDe5gvP1Njo3HNhrzx3ztSbDX-B57hAIvDi1aRhJGFfJvT3SYLgz8JV2DocoFFQwNdboU1qR2KZGUKtqyt46Lb6xOeWG2IGvyP2XrpkYmuexW87-FGoFqGegWZD4o4ZSGDejY6VomdxRXw6vpee6-1BYjL52Pu6aIbIKC-AV5IWGF61Jg51_7584pdRmrygk5LndUXQX0HEu8J8j0SQET-vcl_9X-IvCFN2rfBkGoFg2X6koezQpSBfTkP6cmXXBiHPkZfxMZIby3mrMxg2rGWutvVAAisoXKZ4c9572EOkfi5iLTMrXCFqM1snCozZ2s69JxZYZTtW-OStvdsxZ_kMQ2DGzPtWrlIEIzoxgE2oCytPpa0FvdP3jqe9ft7IqNLir0fZjKln-TTdqXurqXTvXMMfHqfd1pEiVL1yNIPEL7tQ4p-He1xZ_PyI_gOyviqm2BxkpfhsO0gtaX3HLxr6PNWMOITYK-GTEb0_ZjlO2dp3RQQxOMvcX1ZsFQex2YOllPCq0EO58U6_ghAMCBsDje6oDyuvTxstnphdkfEK84CxdtEqg7xLF84wKTqUou4nyVClvYpM_XHeAUQl4mSgILh2eMypTffAjs27WxrgRtkh0p_nZXA0vQVRvihk13Js8QCb2cBpe-xJnBshE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ناگفته‌هایی از چگونگی انهدام اهداف آمریکایی
🔹
چطور هواپیماهای آمریکایی روی رمپ هدف قرار می‌گرفتند؟
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/452839" target="_blank">📅 01:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452834">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cZlpuhfKo5SmanHTZYy17H0N1y6T17DwIVYnax0laRh3LfeUBlr4Nr4lkMSmYB42lOBmpEbYZhmtL8jj-h_Ufj41SRIfQiTPMLHB4RH2NurM4bn7im7YJpht2DpTn8R9vCGxXdSX__o61Oc7WPnK6j4bzbibSgw9ZaDxLjdyOukLr5uXXupXoI1umCqc2WgB9F_qxVn3GBmh0guC8UABqQsvfmemUIP1vAT5EPdGdqpKSa6kitsJZ7ecsw4HSU68hfzN5zVB0Pt2z9zwjwJ8H0XrfinJEekL8-Uki7N_sML9csoKh3dgpkMbykJSF0FBi_5g7AU8oJx82XW6MswXpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HGV9A41K2Zs5dupJY8CNlcy7iL4coUvGnoT1eGZDWiqkutlF9M0cSRv-rKGX2kzVcGiVA2Ro489Y6PqcColQ4QF3L5gbM49PHjK0GzUinrkc70lTaat4tlrAgbs-Gwt5qWwAadZW0em8CWVibiGXZEucECZXv6CQ9IYmd9GFSy56n4oK34A92H8zk78ChtJbjozhdrFtlKmG50sL0_HRDFG6X9P6wyTI4S0OROpBfDvE9sRobPRFlK0DODiEZeXLnWYtw_eFsDE5T3fKf-25Xp5DcYXbD8Suk1q5x4DZ6mn_Pklu4dopj75fZfR32QfiXKCDIxMk714zfDo9_H6zmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uJ6kG4QtQJ1p2FK9pdX-nemka-CH3ss92D4RD5GwPCmQXdl90YxsHjot1iJ4Djn0As2Zm6-7oT5032l5E4ycMjAKSqXDoenpepmH1u2BmTt6sxSAwsTvsFWRQBTgDqwtkdv79sHkjaEhSNplxcYDuwf59gNd3YxbduNwyvLP2c3tkc9NNKaLqXLOARYvqZfj38cBwYHZqYq_JpIuwqQ_wQJAddLWkANRky6pabKa9s02vRDawyjaw7RQx8PaR8Oc3jxP8AvwnxecUZOpnjCAQfLvFyMOTyIDfU3g--k9_0vh-3-gjBQMrlq2NV9gkapq8QalX1jax8p3y67tbr9ZzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dw0gv3RE8pFUphxuEBQYLYNPZ3IToNJ0u8_Yq7a-sEmIf3D_K34onS_3xgW_xc0mhzQfFsJvPoyOSh4_kY2ktyaU2o2HSD6BIwmfncVxzJr-CYPid5189Z2cBV1ARHz5bZrs8hwjCN7RELNLMJ6FIvNqX4iIYGzNDccektknxW97dtWmI2i45UP3qrfSUXwCeFfn7o_3IPK-WkoyUOc_5Dw8UaXdWiD4E_cTHXNza_Jc1ZJWbRL07cnLRilcgnZGFcgvHNvSt0_Dv_gtAm-weQY6TdVbz-kyXAEEtwrMVP4Pl55sAvnbXOniijFdLaKnf2aLGP0GTNg5HqRoTwk9nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EVG80nPfjgwpRCju4o-FWfw7_qpPGydzq_5LUqkMp-89UuWIm3Aa9JNPyz3x4KLgEfgaHHUnduy1rcwYFtTj6BpSIVL8HlNBN0f6ozAq4DqH-5Xn9nBj2svee6Je8TBh7HTa5WjqSqcJ7gBFnaMo6xzRurzl_mB26l5gRCvegscmLg_6tluwrXQqUO8DkGWMRT-eMxCCma8IZkddihWgWe_Zc87v-Duab6-63a9R4JaafXqAuCs1WQCJBYMT3Rn9-lvlTXVrI-enpyZLGvDz0oQqtdzuqf4cI5YRMtx4StiPjjggWrvrEM1iQidRI80xKmTOzE6lFHMwC6prFV8LWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۵ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/452834" target="_blank">📅 00:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452824">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FwnuSC37F_0NO53vLPtXjTI6sHmt5cyOTQQfaubW5sMqzMSQJ4h5Mt8SyTOGmz2BIfeiAaLFXNO3hS-zIB9y2PLtTKQi7dxBCudp7ckYpLrOBnXcwVVA5Fyo6RQPcQrYimc-D7RmgcFXiTknkr-RgGXF3eiv8JDnOvcLglZEaMrCCwA7uZze0B4v7vDyLo3S6pjTTQoSDBSwschlz2BCaXedu38YXnVNEVtQtI5myCkGjzfTWj9XcK4S1rfLJgPp5nYfyk3ZuCPUaQShGFWWzC8GKojm4NxBUh3Gd-0l2sN7_MZngCHOlZttrEE6E78GZVSV5MBnA3J2xQyc_29r-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mTLOkpM2BtKnMpMe4TXIDtvEGNoPTaHQf-YWUC3SDUvh-KSevBQ683SOaOtPPewYh2dMCa7BjYNlk2dLe9hVTa1EXElqPhAWCuzVTf-VtGzp3-f9DZ_JYqTLT6_sCxdIerDPo7My3GmKe0PkPUznJ9q42X2fk0Pmo9HgqbCHrEJunt1GMfpd_X0s-VjJo-sl_wS7vJv7OVc0i_dEPe_dz_Mv6kofAz-osDxAUuf1XYvDeWoZzLIFut0aJQXrZo_mUFD4rJSQOao0xDvB4vkLWtosBmkCxaXnR_JIM-hfmZqWWmnYDn_3igpVFv1PkC0EV0kvTPqettWW5ZnHHpcN1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P1rQW8Lf9Z-eTSXD4EG2ITFu6IdHGgku_nGYqg-50-yxp8_OsB0q0PdXkkXOcF5kTnVKlWEffQIqqBat1YJpVpjaETTNKkQutUmMbkrjPD5To4btxBVjdjcmysf9pfPScmKaddmu73EXqSUOaloKDJxs6oxhlkvBMop5og2jxAkJnXZWY8adIrbHs5of2xk950lCqy2It6WQE_2szBy4wFItnHgq4tdfURAkNE_Q0Ii2s-IB2ZNn9tiM3n-E5zfbvdAz3Kef9QTnXfEjVA6_CyK7ZLie2JX8tvA4pGJIyfdp0JXxkKNkF-P7J79AvV--ol6M2ZdkvTad865VDegtmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bYqNtLx9o0pM1Z_55oMo7QplO1TmDjbTD1wNvrw2mqbpX2OdG7_wjf9WW80R_WCJB-dbPtFYMWJEuJQ4gSPcPoV9Zu8N3M8AwpH-QU2Gm2yKvPel4HIRfzp523CzXgqrpX1PnydAznUwMLofwx9tLQx2YqQEaeh24hoLNaYTW6edQAj3EmmR7r7ygpqI5MvADe6iP6zoeDfvvJyQuNkQBkSPe6TVpaMtIzFSFZ1TT4esa3wixTCT548jYQo3F0bvodSaXTLVMcsIIeQ05BT_liA9UJ3HJUCfmUtQ3oGzxMoEPXL9J9HKNG2SpqQKbtabseHDER-TV0h7DSKtrUQjXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PCL23lmQQa3e5i_6ix1HXoE316xZAF1uN7SKhy0S_TmoAtECjLjp0nnm8znZyVs6mg4_wH7hbP80ZxdoGzBUqsir8-nerY64sz2XLDWI6pz_HMj_kPhy3-s2AKzZ2Kl9_zqPuA3IgcaMQSeBhv94QKXsCn2l-ZQsIBiJPaojD3zoQtILwopi60CXKeVCO9OnJyKNR4kG0XK_hZt9Q4uefni3uaNBnacVJ4hlu7elMJQrfSPOcAqbNlvMTfGV2RqQkx1JUddUjoPLq_EhRKRwBxPYmIF63UVNJ0Jt9psWcEZHUtpA-GFaCRfq9uPw9kZdYgIynDMBKLXf--POITgzHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rw1qBmyStSJdAB1tRBe-pn4mC4vlY_Lj8eV2QnJzzFVZeYD5VnYt0Qi3J5XKAT5IhhJWV2Xnxt4UYOuiAg7Mi1tZJkGr51ozj9vyG_adqOuiKBPpFl4HdIdR2GqwhxtEs1XUTz9IttBM-3J9mPJbcClrno20fX2yKDg-PD8M7pUqGSVmh2IUnM0HETbiAxm9HLkOLVPyVTE4DHRCylyjNUx4DNNdC9HZM9X1hT38MsmdvBRDwU5lVFRFL7BJgMDJGuuMuE1X45ZyKwl1OxnRC-iHFCRYHKOlUqzjYgFvrE96wjX42HRPSJDkRrLNjNpl1wSuOmBFbbDUzxAVQVWEeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-3j4WN-rSS0Kp-65TundbzCbClTz4CDbZfCbFTFXV7aDj1AbiQObJifb1T0Up7hmyry56xSvI18Vx0Zk4qd8JG79lUgGrvjo6aeMBMSFTVRUQvPsS2kMIbwmmup5Knhgo_aBlGkJeneoUcF8zTLYz0Xc3_SpugnNgrFMqbeyWu9PBtPYcKM4ocl6aFXmn2tCbLiiWU5OUPLSRxx9plej3HeBwEMNCFhd4SHJcdZn3jj_34Wam33_xh_HY_LfWtsv0dYf0p71VHjGowmhnMPNzMLfvBVUfGV_55J0KekH19G62slHB1GikIzkEpy57ofWEjZwo60iIXBbm3NJ0wE3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bfEKrE1k4EJQwyPp6UKHvJzj_HqZXxtHr5fGWtDpmi9e9m5SbuJQRayO3Dow2npE5rCATAj_KqQ7Sc-zELHHV5UvVKfHO9tiy_oowCx9m63C_B-Hcciqx_pOstnyf8QL8WPPk5rue3gk6Og8A0y_yEkykXAovoKoAQrd3ejyLMDh_0nkVPLAoa8EsXCbBFIh_48etc6x5uoOFr-MEMWbO6aKOtA4o2EIb5aTop0WQ3RvpmGcSPpzy1MGvtzANqjrKr7pFnbpI4rqyhx1eEz_mSPhLOXOMQQLBWFrzXB-xsijR0nxdBryIiQ9DeV0wfkmm1qaXc9ISOmxYXR8so0VBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lRtzY3CA8Yav3d9jDqhntf1XHlR2Z2kIqLKFH2ven9el9nNwmz4LyRnWyfJqzN-iNPv55negLg4QZx8o-Zg_-fEksow0wTUxBGzNVkfTgBtmwIXvmn3X_LtnZERyxpzqoTXpDuq7UupzPEEBCngJ7qkJzqo_D5goELL8NrdVOyLSCQ7tFb_S1OZS8bcpxUg-PIjiYS7b6WmpZY7FOWCJzg4sUKMw84prlU9ZsT1Ox55pR8OfkaO0fcq0YicMkQKzPPtypYaphbadFEnaGSQ2NI6JhoFNX5gXcY0_2z_Pl4ArU6Fnufa9u8JykGG7qUeBDgP5u6uT880gxUgyLXIvLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a4NXkg9cKb3sG67mKupE4OKlK-0GLxQ-s2cAML9GyutJL7BG_7BP8zAk5zvRGtiADD2opqygX_DuqglvwQ49ui0UtDqlh7gqmlNHiOaW-spjit7387_66b7B7FSfwr04ZSSowsczTNvG4sYRn6bG8RuVO8QjqlsQQqWTkARN9dDMryj0qgnttQa6dpPhwXCygUnlvpnuGf8c_yWDnhD4AGaFUrGB97KfA74WV2o9FR86eC0xZ4R4fZ1EwM4ugmZfp8236_vbRew29cziA4rvW2zY_GlPx6AV32IAE2E5YhTrr7909CkijN9mcI42W-ghGZCn_OID14OFKqq3Pxq7oA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/452824" target="_blank">📅 00:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452823">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTKwEPWNhkDCC3-csdleasqGauwgo3R1rBCnWVz4aaCnv6zLH-4JT34jonzZ3dqAqJeVJ-QlD1ZxznlriiAHKJYva7PQL58Maasstxu4HM6KrYo2BhxVxmUSnsWFLishsAaCsECDMFUMFd2bjCVtz8Bmmbhnupg4Z2Ly5Ik0tNscIayvM2lfZccsDCAu7BKsGD3o_eve-SqqLufdcmJ4DZeCCMxU5mNQK2RpJQglNMben1yseTruUI1Q0I8ZzNdlKRPTRrTcuOKhsAP7giBFHJg4TNISlz4LX0xKP9OaxUNFak9rr8QFxNMdoKY794oBYGUQ5YQJsPXr83y7J5OmVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطالبات معوق کالابرگ، سرمایه فروشندگان را قفل کرد
🔹
طرح کالابرگ الکترونیکی که با هدف حمایت از معیشت خانوارها اجرا شد، حالا برای برخی فروشندگان به دغدغه‌ای جدی تبدیل شده است.
🔹
مغازه‌دارانی که کالاهای اساسی را در اختیار مردم قرار داده‌اند، اما به دلیل تأخیر در تسویۀ مطالبات، با کاهش نقدینگی، انباشت بدهی و حتی چک‌های برگشتی مواجه شده‌اند.
🔹
فروشندگان کالابرگ حالا بیش از هر چیز خواستار شفافیت هستند؛ اینکه چه نهادی مسئول پرداخت است، دلیل تأخیر چیست و مطالبات چه زمانی به حساب آنها واریز خواهد شد.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/452823" target="_blank">📅 00:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452822">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8CB_jN5iWEC9pWZLXgBYiiwidyhwvJS7_6QSIMm9w3Szo7CBql1gYe3gHQNZGCd8OJnXpwF7P1HiWos2lVDVtZkLumTA1oX5d3w8Z9Nt4ke-jbCYkWWssmEjrUWXtppqDjWmN8GNHlHkPl69Uw7TYherYUwkfj5jhIOyCvLunbiJ8jM1hjoyKLflWkpsRC2K0DJtwV75LTnnM5ndTHKXxeu8dwWJ_uvEFyjyE-aqtKpPOs2HWOT5oaX4t3qrxlXVVQFxZbmhZBrkxxZtmQvMikewXNMizAGzS1HuOU0vGnnlhQMfEhB5AM821WbBuDvJh9KkhI1Xuxfp9wS9xLEuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با کمک هوش مصنوعی از تنگۀهرمز عبور کرد!
🔹
رئیس‌جمهور تروریست آمریکا طی ساعات گذشته پست‌های مختلفی با کمک هوش مصنوعی در حساب خود در تروث سوشال منتشر کرده است.
🔹
انتشار این پست‌های مضحک، ترامپ را به سوژۀ شبکه‌های اجتماعی تبدیل کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/452822" target="_blank">📅 00:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452821">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تردد ۵۰۰ هزار زائر از مرز مهران
🔹
استاندار ایلام: مجموع تردد زائران از مرز بین‌المللی مهران از ابتدای ماه صفر تاکنون از ۵۰۰ هزار نفر گذشته و خدمات‌رسانی در این مرز به‌صورت شبانه‌روزی ادامه دارد.
🔹
ظرفیت پارکینگ‌های این شهر برای پذیرش حدود ۱۵۰ هزار دستگاه خودرو…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/452821" target="_blank">📅 00:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452820">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f4ecd59a.mp4?token=rBcEBqN0PJXTx3FV06ICCLxPncEF5C3beMFY3WLRQvEa5aKAXYCXUbZLTTjctrS1d5WmS7l3MjNCPXxcGp59lGPl5qoB-w1qQo9FhLC23vBs0nLRrsvbWJ_QYNsqHgdZDOYCLh6HD7BdJdy5onM5Rj81_F-h7QEpM-05QoVz8x5rATh8TQIXHCrpXMVzDqypzn36QQLPNj8oyFbLydLi-DgvSWgInDd1ZmtEgCcPytVXtGDR2c_vQSDm-MXCRhfBd8Bs7HCSZ3r9q9Hyo2kLFYYbQoDOHHX0mld9QkI1tUfqclbZnHe3CKPvxVUv9AF5k_2-w70L919W06e6FknYPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f4ecd59a.mp4?token=rBcEBqN0PJXTx3FV06ICCLxPncEF5C3beMFY3WLRQvEa5aKAXYCXUbZLTTjctrS1d5WmS7l3MjNCPXxcGp59lGPl5qoB-w1qQo9FhLC23vBs0nLRrsvbWJ_QYNsqHgdZDOYCLh6HD7BdJdy5onM5Rj81_F-h7QEpM-05QoVz8x5rATh8TQIXHCrpXMVzDqypzn36QQLPNj8oyFbLydLi-DgvSWgInDd1ZmtEgCcPytVXtGDR2c_vQSDm-MXCRhfBd8Bs7HCSZ3r9q9Hyo2kLFYYbQoDOHHX0mld9QkI1tUfqclbZnHe3CKPvxVUv9AF5k_2-w70L919W06e6FknYPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدرالحسینی، کارشناس روابط بین‌الملل: اگر اروپا در اقدامات آمریکا علیه ایران همراهی کند، جمهوری اسلامی آمادگی پاسخ متقابل را دارد
🔹
تهدیدهای ایران در مورد برخی کشورهای اروپایی معتبر است و توانایی داریم که پاسخ دشمنی آن‌ها را بدهیم. @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/452820" target="_blank">📅 23:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452819">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d2b72f70b.mp4?token=XiOPYvWoKyg3Uora3_8AV6x8uqSyOkRpxIDEhlt5uZ47BRtaO042jej-8mavkWU1oYXPCPiYlTcd4EkHgXitdIurqK2C9b8LjGqBu3czgvA4tqnqiWH0-kQ3iWT8vMlbUjITgrsjTA13mEcqRZG5MdOpHWRH8o5dp-0I5twWjlsTW5Hexb0u-2-TPgEvmgzy2nRZum27ExaIspfWDcNTRHbQ7vu48v0H_dKdwqQxfTFBGUvNBqzaSBjfECV9dIGQaCTt7Mu_Pns9S16LiKBL0HxAwplRRT6jucO4p8SB8vGBfpXAVTyTCVNrYrJwj4JKnscvVuXwb1c66wNgGPDLnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d2b72f70b.mp4?token=XiOPYvWoKyg3Uora3_8AV6x8uqSyOkRpxIDEhlt5uZ47BRtaO042jej-8mavkWU1oYXPCPiYlTcd4EkHgXitdIurqK2C9b8LjGqBu3czgvA4tqnqiWH0-kQ3iWT8vMlbUjITgrsjTA13mEcqRZG5MdOpHWRH8o5dp-0I5twWjlsTW5Hexb0u-2-TPgEvmgzy2nRZum27ExaIspfWDcNTRHbQ7vu48v0H_dKdwqQxfTFBGUvNBqzaSBjfECV9dIGQaCTt7Mu_Pns9S16LiKBL0HxAwplRRT6jucO4p8SB8vGBfpXAVTyTCVNrYrJwj4JKnscvVuXwb1c66wNgGPDLnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدرالحسینی، کارشناس روابط بین‌الملل: اگر اروپا در اقدامات آمریکا علیه ایران همراهی کند، جمهوری اسلامی آمادگی پاسخ متقابل را دارد
🔹
تهدیدهای ایران در مورد برخی کشورهای اروپایی معتبر است و توانایی داریم که پاسخ دشمنی آن‌ها را بدهیم.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/452819" target="_blank">📅 23:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452818">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp7vW8S3xvw_ze39oC38bYPAnQ_tzoS_DKawvCLWWNz77Mxl7buyymMJO2ZPU6Sf_DN8NiYYlTnetSFjcsqWRuNq5_Nyjn9HHu8oXn-20cL93sw7fm5ysik7OfexhzI767GtdghvRn76qPUA8_PBHYNNVS--hMUzhvO3obumvKPTglzaEqGUZKgJ5HQDy1zRucMIzrHWwgPUBDH1UFA6GHSN1uDO9yHsP2eX1ZUSoUOGYorlfBkTA7yXx5g-FfXsU15y8m5csm50J3SoBp0KYeZnL8WVhzP9K4L_AMx7xoIPM3_AoO4dCGUDZ-SAltDRFuAFJ1k6eEpjF6QtTW_PUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹️
رضا شاه، بزرگترین زمین‌خوار ایران
@Fars_plus</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/452818" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452817">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4de6a51b.mp4?token=oE2iozIeNH1Fkmre3NCspAmlxzJqoe3audEtfNkcFR99oPFCqOFXhWVvFvZWM2a78hyOXFd86UPkkMe5WvZhmC-Qn4t284JibInOccm0NRdU2NXt9A4EBKIykNwv4GY2jSOQevup3Fe17i-drhD5h4NlLy8vHGeNAXBv1DfTeC_sXzk5Shs_RpS9wfQ0ZgXy1RPqQDtByOyHRy9yhUTxCTVR3PgvvZBt17ssd5ZXDWwaAmQFwctjnGKk__fxo3_iv2PG8zyyKvi0rr2bGIzOFQmTHCNto9RYb35G0wyajG5CBNw-5wwvSOdX5ow8g_DB8LJJSkvQOKl64mdge1zKzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4de6a51b.mp4?token=oE2iozIeNH1Fkmre3NCspAmlxzJqoe3audEtfNkcFR99oPFCqOFXhWVvFvZWM2a78hyOXFd86UPkkMe5WvZhmC-Qn4t284JibInOccm0NRdU2NXt9A4EBKIykNwv4GY2jSOQevup3Fe17i-drhD5h4NlLy8vHGeNAXBv1DfTeC_sXzk5Shs_RpS9wfQ0ZgXy1RPqQDtByOyHRy9yhUTxCTVR3PgvvZBt17ssd5ZXDWwaAmQFwctjnGKk__fxo3_iv2PG8zyyKvi0rr2bGIzOFQmTHCNto9RYb35G0wyajG5CBNw-5wwvSOdX5ow8g_DB8LJJSkvQOKl64mdge1zKzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک: رژیم صهیونسیتی از صبح امروز حملات توپخانه‌ای را علیه جنوب لبنان آغاز کرده است
🔹
در این حملات ۵۵ شهرک در جنوب رودخانه لیتانی کاملا از بین‌ رفته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/452817" target="_blank">📅 23:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452816">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a2d1b2945.mp4?token=GOGOzhuM3aCQUdwz7JZnDFh7fL-theHeBTpqaWj1Ghtgyu67-AslaNIqw9fU_T97nDO71UjLGqM5wDKwZpdzjzp7CuFheucC9wrCET3xUr3Ux0K5rpxOCnW8y3byvRTOXjh1Fqpa_aVv44Rvg52MJOURuJxX8uMwUs4Hk-iUCcHO6O5LhYXJEFNOXTGy5AVRIIyN55_xjcBc67QNJLAPbc9z_2_nrFE0H_gIAwFTNQ87_d8a-RheCJtVBTsNZJ0i_xs_vWz1HtK-JeVt8BnhlRdaX1Z2IgEQ6bMzVkTIadaxc5iAXipov4P1ZBsrtcPYVv7xKnZJttMEeax6_5lav0R_nKWT0VLkdJ1PJl2tdMRpSHf9NUqVAQ2pzUyMKDhC-P-fzQwN-41HRusgAEBrQCwvH-vcnojy9xnxsXYDzSKUUaaJw2Vrd01KIBlnAY2ivgwExWAasMPO8yAaJxy0tK7r5ZdNr0EJEF79ScAn4Q4TUX-BJfP3JyDCblabMAqeyRx1IpUJSDIrzl0dmwnKdhn5jLXk7xPWLOVmCxDPycD45G_mUaMl4CE5m9Pem1a0EveItUEj-MkAfCZg1iqYxqdVvAxZ1ncMQIZvEVAqKdK3PqYj6kVsQVS2pdNfDSlFb4cLZJnClRmEwTcs2EQvobOujDAu1vHa5ufk5gAktHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a2d1b2945.mp4?token=GOGOzhuM3aCQUdwz7JZnDFh7fL-theHeBTpqaWj1Ghtgyu67-AslaNIqw9fU_T97nDO71UjLGqM5wDKwZpdzjzp7CuFheucC9wrCET3xUr3Ux0K5rpxOCnW8y3byvRTOXjh1Fqpa_aVv44Rvg52MJOURuJxX8uMwUs4Hk-iUCcHO6O5LhYXJEFNOXTGy5AVRIIyN55_xjcBc67QNJLAPbc9z_2_nrFE0H_gIAwFTNQ87_d8a-RheCJtVBTsNZJ0i_xs_vWz1HtK-JeVt8BnhlRdaX1Z2IgEQ6bMzVkTIadaxc5iAXipov4P1ZBsrtcPYVv7xKnZJttMEeax6_5lav0R_nKWT0VLkdJ1PJl2tdMRpSHf9NUqVAQ2pzUyMKDhC-P-fzQwN-41HRusgAEBrQCwvH-vcnojy9xnxsXYDzSKUUaaJw2Vrd01KIBlnAY2ivgwExWAasMPO8yAaJxy0tK7r5ZdNr0EJEF79ScAn4Q4TUX-BJfP3JyDCblabMAqeyRx1IpUJSDIrzl0dmwnKdhn5jLXk7xPWLOVmCxDPycD45G_mUaMl4CE5m9Pem1a0EveItUEj-MkAfCZg1iqYxqdVvAxZ1ncMQIZvEVAqKdK3PqYj6kVsQVS2pdNfDSlFb4cLZJnClRmEwTcs2EQvobOujDAu1vHa5ufk5gAktHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۴۸ شب میدان‌داری مرزنشینان آستارا در حمایت از انقلاب و رهبری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/452816" target="_blank">📅 23:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452815">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/605deef080.mp4?token=Ixnt8MwCEe1ECwO2-zzdyo5s5DJmlEUN1nv9Q82fykuwj-vQ15C1fHsTVF1Za8J7hoqYdPvJQWNJ4VQ2kD6KhlaP3YCN1ARc7cnxGN1rfk-FhJXJZCvPsk7R4vHaZDB1D5ezDu6F_oZSCZbfHu89iDzdUMjZBD8ugiG0VwdugLMFOj5hOsj-2VTt2yxRqUInmxoY7OnhqETkKA6f1V8_wBm2c_nDwijf3Io8fNVdfvK1UfvAnv3qjUSxExRiUmsMwHgFF5T_YLolSbTbV_umW1O2itBIwUzAkyCypmdSDpFXE2amZe3L1lSh6qOGCSb9aZgygpmZNdTMYMpP-sikb37HzOfe4rg7xmy4g9cLqscHQMv3Eo9Be1K2iY52JE8JOAiRwXJslyJt0_FPkNj0KlSgKsPEMndPq82bwah-RVJUJnS0nliqb5u1r-zAfgTxRHDW8dT2pUuriQkJrIAO-4ny8c-vUXTP7x4ZK3Bxu7ABneYtKSlhxHMvN2dWVlE2t0IZcLR5U3hSmpxLHW68DnXNGsZ3dusQjJXwQW_AnPLtcrYHh3zFvypTO2GsgqFaZxTESwi3t6PCYllnGCDYZRIjzqIGZI98QcpWguVaMONKVNsgL3mC1AXVf2xoq1vueG8cPI5gnso5odeumpMlZ83U4OUg8TIRmsYfarTMbxI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/605deef080.mp4?token=Ixnt8MwCEe1ECwO2-zzdyo5s5DJmlEUN1nv9Q82fykuwj-vQ15C1fHsTVF1Za8J7hoqYdPvJQWNJ4VQ2kD6KhlaP3YCN1ARc7cnxGN1rfk-FhJXJZCvPsk7R4vHaZDB1D5ezDu6F_oZSCZbfHu89iDzdUMjZBD8ugiG0VwdugLMFOj5hOsj-2VTt2yxRqUInmxoY7OnhqETkKA6f1V8_wBm2c_nDwijf3Io8fNVdfvK1UfvAnv3qjUSxExRiUmsMwHgFF5T_YLolSbTbV_umW1O2itBIwUzAkyCypmdSDpFXE2amZe3L1lSh6qOGCSb9aZgygpmZNdTMYMpP-sikb37HzOfe4rg7xmy4g9cLqscHQMv3Eo9Be1K2iY52JE8JOAiRwXJslyJt0_FPkNj0KlSgKsPEMndPq82bwah-RVJUJnS0nliqb5u1r-zAfgTxRHDW8dT2pUuriQkJrIAO-4ny8c-vUXTP7x4ZK3Bxu7ABneYtKSlhxHMvN2dWVlE2t0IZcLR5U3hSmpxLHW68DnXNGsZ3dusQjJXwQW_AnPLtcrYHh3zFvypTO2GsgqFaZxTESwi3t6PCYllnGCDYZRIjzqIGZI98QcpWguVaMONKVNsgL3mC1AXVf2xoq1vueG8cPI5gnso5odeumpMlZ83U4OUg8TIRmsYfarTMbxI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نبض مقاومت مردم کاشمر در ۱۴۸ قرار شبانه همچنان می‌تپد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/452815" target="_blank">📅 23:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452814">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0NIyqCO3hDzTa99vwHNaNz-dAF3E55dUTTv_ntnk_i0nRx4finJc23GL2MTMdudKQ-DFbkrPMiHMlm4DrYFishYhJRHemCvHJYXfiP5OixHCpwU_UXNmnDCifCPagwWhVLQiE7bHJn1y3EMfPO3ZAJ3reVTwEFXHN2JSnjUeeLkHCDxyQxxzqPgJ1LcFdbLNuEVqBOmOCrXw77EU7wDqmTeonCxYGt4mCual5f_jpxR9rgbfhSWct7CN82NR3c-JLtqyz4YuPEsU_alX3ud67gQk8rNXWwatqVZaTfDm3gb6SQOXjRcRtVNGZey1eLp5iecJ9Z1xCj3UlQx3cj3UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: آمریکایی‌ها در حال تبادل پیام هستند اما اولویت ما دفاع از ایران است
🔹
سخنگوی وزارت خارجه: آمریکایی‌ها در حال تبادل پیام هستند اما اولویت برای ما دفاع از حاکمیت، تمامیت ارضی و حفاظت از مردم‌مان در برابر جنایت‌های جنگی است که آمریکا مرتکب می‌شود. @Farsna…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/452814" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452813">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4cb366f32.mp4?token=Opgf4qsofHvgkc23Pieb7LlL1W4G7yQiJudccQwL377L9pb4GDuD9mV9MiOZjC4hucDVYMx1_AdW5AYBr4U4lmcqLLu8jeGnqjng_QJ9eUR0KhLez5fQZIkiv-cX3puXA3I0zliojJKmO8vya6OzQRIashcgxfRFugQKdJ22Z_dhkv9lGB2q7fcyBhXYMKyW93L34SpG-Xkfk25K-f-wglabaFCHYi6OAm8vj3mt_GukxnzfN6qqPbHA7wEuel_pfAlPq8Hj1G1ysBRQwBL07_6zpyHSLbnTfjmMCPbkaTbV-3kLoTOcMHWAxekoGVLAgXNM4UZlcadCDfeSP0LBeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4cb366f32.mp4?token=Opgf4qsofHvgkc23Pieb7LlL1W4G7yQiJudccQwL377L9pb4GDuD9mV9MiOZjC4hucDVYMx1_AdW5AYBr4U4lmcqLLu8jeGnqjng_QJ9eUR0KhLez5fQZIkiv-cX3puXA3I0zliojJKmO8vya6OzQRIashcgxfRFugQKdJ22Z_dhkv9lGB2q7fcyBhXYMKyW93L34SpG-Xkfk25K-f-wglabaFCHYi6OAm8vj3mt_GukxnzfN6qqPbHA7wEuel_pfAlPq8Hj1G1ysBRQwBL07_6zpyHSLbnTfjmMCPbkaTbV-3kLoTOcMHWAxekoGVLAgXNM4UZlcadCDfeSP0LBeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بازرسی: ۲۱۹ شرکت خصوصی به‌دلیل عدم رفع تعهدات ارزی ۲۳ میلیارد یورویی به مرجع قضایی معرفی شده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/452813" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452812">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVgXRfAjlR4KlGosbdSBUhKnlBeCg0OKZATMN_uXcSH567Z7m1e7ZJWBSfIq2Rn8ELmJN3Ujnt4VUi9pln9QhBm_SS_sYwUl5knN5kar2x-VyhWrJLwbYQ17lSXHVdKCbf-w9I1ZgIe-YqfD4bPH2x_M20sutPR4p_evuC6Kdnho1FteaYhVE5n_UlDJwTuhYE4c47B-TOmVFGnTLTYBh4sYiVCVim8tcAm_y57gdLA6VVpdY_xNaV_PlP4IXTwTwuaCiFSIdkIfjFVNFXKY-3nZItlHf-q6mrybUhluWw1Pg_6RCBKucjMeiFmKhoosR0A8OjpZ-kT4y9rbo8_mWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: آمریکایی‌ها در حال تبادل پیام هستند اما اولویت ما دفاع از ایران است
🔹
سخنگوی وزارت خارجه: آمریکایی‌ها در حال تبادل پیام هستند اما اولویت برای ما دفاع از حاکمیت، تمامیت ارضی و حفاظت از مردم‌مان در برابر جنایت‌های جنگی است که آمریکا مرتکب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/452812" target="_blank">📅 23:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452811">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87101cb2e0.mp4?token=kc13o4qCeOD5cmcf-4C7g3STRmMyP5cVPvPYs6dNZ5VC9e-yOzLD_jTdk-qGcwtEjxe_F419aX4jwIQ_tX7LqpqIx9HfDfbOHq38vqiC_3TURz0SGREiUpLjx_GBEQTVeojmK0vsLArI4AR-WpRWwHg9um_-ASorHJSsMlRofZNutXMcNZYhuz-RDqDgBXuc9ESjnMz3vFzsHKtLx7dU7vjSERy0-njqH0gHAxXItJvS-sbZIrOX5eLFlo2umv2iucWovx_ZMzjGGN7OqbmWsmSZpqHQU8piwZGihpnPpigiW6ejBHQThUXXFbFgySRRreTlbol-BJR7R0Li8tNykJLRcYxuaLWSHh88D5kh_241bG6hu-h5Bs65fLgJpBdCNwLRDljkKRLfLEDIrry0iB06Zyf38-ZetecY5hTrwxfRGkNWotdSMaEXOCyOf8f9nZ7uvtANDeUXhmSXmsC7u09S_zdtdUEALxEku_qS97qWoOMB5vvCNRMDif0WZghledX5N6Q-nj4ki-HOCk4gY03TQl4iPOeyqn1Aq9Jzgv-uYINMrkKuY9zNjX4TyNjuxe5Oj-t1KtTCqCohjZbpld2fBPV3DwvGxDMD43d9-_WLYSthVm-Aa_ME3cLnZZ9vF6uk8xlL70NxjqU-z7GKtm1ekzN0TYpI2qKK0TlPwzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87101cb2e0.mp4?token=kc13o4qCeOD5cmcf-4C7g3STRmMyP5cVPvPYs6dNZ5VC9e-yOzLD_jTdk-qGcwtEjxe_F419aX4jwIQ_tX7LqpqIx9HfDfbOHq38vqiC_3TURz0SGREiUpLjx_GBEQTVeojmK0vsLArI4AR-WpRWwHg9um_-ASorHJSsMlRofZNutXMcNZYhuz-RDqDgBXuc9ESjnMz3vFzsHKtLx7dU7vjSERy0-njqH0gHAxXItJvS-sbZIrOX5eLFlo2umv2iucWovx_ZMzjGGN7OqbmWsmSZpqHQU8piwZGihpnPpigiW6ejBHQThUXXFbFgySRRreTlbol-BJR7R0Li8tNykJLRcYxuaLWSHh88D5kh_241bG6hu-h5Bs65fLgJpBdCNwLRDljkKRLfLEDIrry0iB06Zyf38-ZetecY5hTrwxfRGkNWotdSMaEXOCyOf8f9nZ7uvtANDeUXhmSXmsC7u09S_zdtdUEALxEku_qS97qWoOMB5vvCNRMDif0WZghledX5N6Q-nj4ki-HOCk4gY03TQl4iPOeyqn1Aq9Jzgv-uYINMrkKuY9zNjX4TyNjuxe5Oj-t1KtTCqCohjZbpld2fBPV3DwvGxDMD43d9-_WLYSthVm-Aa_ME3cLnZZ9vF6uk8xlL70NxjqU-z7GKtm1ekzN0TYpI2qKK0TlPwzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بندری‌ها ۱۴۸ شب همچنان در میدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/452811" target="_blank">📅 22:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452810">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/847aab2d4f.mp4?token=lCR_nX8O78qZ9FTx44G-YfCS9d9DZio6WM9QTXFPbodDtvNsAhsoG5Cmne4vONzZbj2RGUfhxPdIbtxIc1JWvsFcmYbiEmctGbohNrU3AMIuONk6ucS7mr1ol77MTP3PQdJ1OWtD7ypqndHdMkT3RukQ3E1TrVzG72qgCGzRjwY3JWaUPGOIR49NzcQ3gYVMRSrnPWgPW-3LJXubzK6eiK6mlnGuDgAF5LOjA_zesxvd8tqFb0LfxLy6FfjI6C0emADPL_bOo1DQaDKfaQMwNs9gG6DVKlNwV1OZoES12hy7DQi0v6_6CMd7h_wAwcw45CDxOOWMYxNU-eK0M5hBAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/847aab2d4f.mp4?token=lCR_nX8O78qZ9FTx44G-YfCS9d9DZio6WM9QTXFPbodDtvNsAhsoG5Cmne4vONzZbj2RGUfhxPdIbtxIc1JWvsFcmYbiEmctGbohNrU3AMIuONk6ucS7mr1ol77MTP3PQdJ1OWtD7ypqndHdMkT3RukQ3E1TrVzG72qgCGzRjwY3JWaUPGOIR49NzcQ3gYVMRSrnPWgPW-3LJXubzK6eiK6mlnGuDgAF5LOjA_zesxvd8tqFb0LfxLy6FfjI6C0emADPL_bOo1DQaDKfaQMwNs9gG6DVKlNwV1OZoES12hy7DQi0v6_6CMd7h_wAwcw45CDxOOWMYxNU-eK0M5hBAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بازرسی: برخی تراستی‌ها خیانت کردند
🔹
یک تراستی ۲۰۰ میلیون دلار از سرمایۀ کشور را برنگرداند و از کشور هم خارج شد. @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/452810" target="_blank">📅 22:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452809">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cf60d3589.mp4?token=CjrN3EXrhulXmMOHXJe4U_pPnpeWEZ1WWR-NLxC_7ETGGM-YKrCeW4zuOuw-791yVXs7m8UO3Fy_kDJG8ucF7PZDStv8i-yFXkZnYRurHfhl-ytbIONKgxzeFnMVerbd4sZIVwjLBjoBeoSE8RAeQopPuEZfoVPThunVEq4J4HWwnMBe68tBPEzxkTR6MPobjuwAkBIS_JaTipfQU2pe7_WhUaYrSkGVrzeMmzszhoVFvbOSDHekNFgwYUH9V09ODyJOUtqVI87igLGiIwNeEmG_KO9n4pIw_GS0sl_0fr6nRPXMfSzsaollK_KuiOp9dX8-5lsdUndXOMZ3hZz9cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cf60d3589.mp4?token=CjrN3EXrhulXmMOHXJe4U_pPnpeWEZ1WWR-NLxC_7ETGGM-YKrCeW4zuOuw-791yVXs7m8UO3Fy_kDJG8ucF7PZDStv8i-yFXkZnYRurHfhl-ytbIONKgxzeFnMVerbd4sZIVwjLBjoBeoSE8RAeQopPuEZfoVPThunVEq4J4HWwnMBe68tBPEzxkTR6MPobjuwAkBIS_JaTipfQU2pe7_WhUaYrSkGVrzeMmzszhoVFvbOSDHekNFgwYUH9V09ODyJOUtqVI87igLGiIwNeEmG_KO9n4pIw_GS0sl_0fr6nRPXMfSzsaollK_KuiOp9dX8-5lsdUndXOMZ3hZz9cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بازرسی: بیش از ۲۰ هزار شخص حقیقی و حقوقی در مجموع دارای ۹۴ میلیارد یورو تعهدات ارزی رفع‌نشده هستند.  @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/452809" target="_blank">📅 22:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452807">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/def8f2e12f.mp4?token=dxiqmcVjmt_RjHWWRm5m_3oKXxx8THw2bCj9gRZdF5ev52iizFLX7IWjkN6EOoDyN0d-cB44wB-jXmpT8q5U1smAKnrjP0n8RD0Vn5Jt3ggWCbRoYdv4PhTJcRzyJotIm7N8VRI2hs5xE212aGnGhmhmJ2yEu63irkyXd3f8FhnxekFVT7hybyoIRTI6_kt56e8O1j-lsWEvxh59UWRqbHGzHf9_RWwq1UaSTfQVM4T89c-1QtzDTsRl4GumF2OFLP9yZbQYCprwHKspclX2mm2A107K-q20q2G1Oj3n2vsvir8QSLvb6pg2tbwJg0uj5Uj2AcTpTwEZrZjFQ5VbgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/def8f2e12f.mp4?token=dxiqmcVjmt_RjHWWRm5m_3oKXxx8THw2bCj9gRZdF5ev52iizFLX7IWjkN6EOoDyN0d-cB44wB-jXmpT8q5U1smAKnrjP0n8RD0Vn5Jt3ggWCbRoYdv4PhTJcRzyJotIm7N8VRI2hs5xE212aGnGhmhmJ2yEu63irkyXd3f8FhnxekFVT7hybyoIRTI6_kt56e8O1j-lsWEvxh59UWRqbHGzHf9_RWwq1UaSTfQVM4T89c-1QtzDTsRl4GumF2OFLP9yZbQYCprwHKspclX2mm2A107K-q20q2G1Oj3n2vsvir8QSLvb6pg2tbwJg0uj5Uj2AcTpTwEZrZjFQ5VbgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بازرسی: بیش از ۲۰ هزار شخص حقیقی و حقوقی در مجموع دارای ۹۴ میلیارد یورو تعهدات ارزی رفع‌نشده هستند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/452807" target="_blank">📅 22:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452799">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KRJQZgQHZ40QQH1Flls6SAKsPSP3TD9q_TGZ7LAZMJkXCAl1abxmYacM7vQjW8JCnCcbgV061DW4pp90g8aoOJuzeVxMDZx4i_HQblAirQvLGQZXVvr0sOhO1nSej4ry2CixHsK5HkSwiGO4lCSaEz3xOm2QZiYZ9Jov2tg22AuHUrQGmN_eAWmVS_0NfvWCLXMglEN5Fn2CA6nPryZd_l52RrW9T0kpK4rpdT617LMlJBp3rBhk3oCs1YPyuJEFJg9wfLNBlxqVSOnq4kI_tME6iAW28TBsOQG_vFtKSFd1Jm_WRRfbRhb_Gd7KTj_MWcXxvZwu1xHq07QnPlAH0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/su5Bblta4zMnBUWCn3aboS01OkEdTjv6Qr4A27DkqLVkg_8rNz4WNs9ze50ZK5UUJBCt9lVBNjOxA9Rj84Oy8gaj1jyUaHNCD_vHStUPhij5mO6uz3A1SHKHEQXj6JWMTndHYTycPSGxMQeuNuzYUgbTE2N52a9DSG55dLSgLEs5bpxRr6-V9HA1tcMioyV3DK6wThoKrYla11alkTzUk_JjBASyqYMB5mYbWDzBgAQ7uCDHgG6iV801s8U3qZI-BqgdgVM_l8zOO4BsX9ZvZuZWBY0MRj0LFWvPPO7gIaOPTFE_DPvsTQt0HbALZHwuP4n-QAjaUmuewdZWEJ4SOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pIMB-PJKj6550zPvnsjrU_m_442XytWAfRK9qvvki9NR086a_kQzuB095FyZFmU-mnB0Tuzd68CtF2-ZyZ8_2ONQk4uB8Ou7RpP6jG36p9U6x0h7Tb2C-dP7iN7plnzajuPuv4Ixa4tEa76C3CgfKUyhAAFGSoiKf4w6PpTjccb67mVlyiRpKHeEF5REy5vRqNXW35EOqIVYxo95ph9p6isPDmLaAtesth41wuYiS4nuCn1vOGbeZGrlbITeo-XgDtUp-B21gQEBSxQ5wcwADPf9FGjIyLjG9x2Rf8T1qh-WWdRtQvBE08NGivuLkRC7fQzePI6oJFuyETxOsD4K7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uL9grupyuwhnNgMVrHF-aKSBXpP94ktp0TgtMZiIOvfsIYApSWUYwhjCOGNECPWRpx4LRQwz6oKe7J4ib_ONwWh0p_Fu3bZ_W5XHn-4rgwX0GuZgRoxY5mRnduZ9f78tKI1SO_xVUibqXVIB8f9MNsKDP2p2T-CnnEn7W6axG8rCUMvsAicEgRzbuB3FLn5vYW48YJFhIuGljeLC0TgT2xY4zDJcAKx7dEFBHNZaFvKeWAyvImUBiy5Mr72o_P3oYVaRTJgiDZNP7eoyAF6lyPta-nu5VfumbTDlRDjb_ykUDef-6F5eJ0lYNCykqVozudtCSV8lDb-aGU-5_-8yHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/enLoERWrs6GO_5roakQ0GENNFe_PYI4c31cENrrdaAaeJAuptik3v0MDynUQDgq3GV6AFvWDHnimO1n7nc2CwU5GlYA1_KHrLlOv7sAQzvVQksLdPS-8GmBBvNIhS76Fg4MrfBFgbCfKIFajS7_pie6arfPXaawEBt8JgiS7BLFtjEv4jl2qQ6_-YbtNsIQsFW6jOt0WzoR4oYQqMiQpXuo-nKUWHSnTXKeOMraoUGtS1supvjNgS5BmH6SH58oR7_nQHIjuuRZr0KeakZqOsbwOBh5BS-2NSTD-lv1y9fDEGUfVCecoHZdlw8g5oMJMRKe2wB4R0eWBF0tJlSA8ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G6ufPCTgS4WDHSP2Go9rDhJQCozPLXH2yvFpk4Qu5htwhwoMcy83lK4n8VDpMf2jLIak8-5Bx34U8QNHz3xb0f769p9gOwzj1WoloR-snGIorZkVuGh2X6BUx-63lhQglzD9Pi_opxogWUmcn3RP2Yjz-quGHLp5x-ChwDRw8xzK8_zWQMtFnBeORteL-m4ez31S83yyOL5Shnh8SQDcCy4E81A-ldjontmSdXvkuNh5hE1jL4hUy2D5Hu0dVm1-EPfOBYK9IVMmA9LutfJp9Dgh9nYghWTWDeVEcJq9zdO57BZv1zapGfAC07l0zsPFXzXUCkRakGWbibBxU3bXwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMkHOsQqFOh-DkSVKV2spOAi2dZY7oHdVJpZfeS85yimv4EfmNP1Af_a1WEgGe-HzFpC3LF3GpqijEiVKGq06XspUaf0PHceX2PFd5ema3sKZTt8ZDUuTP0wGgvdm10751HYgoBBm60mL8pmQAi9VDr-p2A22-bststMZqSHkFxBB5EwGsxYuul60aT2yPDoJSVjihnHH3q9u7efs5LovgjDtpKnvg67spgcn3eUzM6BtOkN3y11ll2KTx7b_G8OB8VGRTfJS6At8ytZeP8TmTgKE_QZdbNujhvexnyPyNn6HkUqH6nKWmPaRpsC5NEKLbOABioG48fSXGOWHq2huQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تجلیل از پهلوانان زورخانه‌ای تهران
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/452799" target="_blank">📅 22:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452798">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfe770a69f.mp4?token=DzfFDrZnyNoboQcwsQo_eHwVK5IPzRC5bJ-8EO77r8Q1BiK7rEvwd0iYeZ41CXgSrv_Q5cJC8JEjHdqPOPU8-1mWW24S5BggYvMNTffsLGKADRbXMqo9JaopUBQOcNxEqcweJ3OsbaCyeHUY6tr6BEkjFLaW4Fk8XMNf9BSNiDNd8OJMywhIi0ey3vo4pO6ajkO8S2moy5t1bs11gF8QYqLm-6JtTnyWE7UBZW0eIhHFinjejIMfUZoRkHv2eA1yOQp7TTuGhyk8FzCrg5Z_hFP1wAlqXipFF-ceafcjWZ8YiAMrlYcAxYCTwswqSZq1d-F50T1DRti-MgjFTQJ4FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfe770a69f.mp4?token=DzfFDrZnyNoboQcwsQo_eHwVK5IPzRC5bJ-8EO77r8Q1BiK7rEvwd0iYeZ41CXgSrv_Q5cJC8JEjHdqPOPU8-1mWW24S5BggYvMNTffsLGKADRbXMqo9JaopUBQOcNxEqcweJ3OsbaCyeHUY6tr6BEkjFLaW4Fk8XMNf9BSNiDNd8OJMywhIi0ey3vo4pO6ajkO8S2moy5t1bs11gF8QYqLm-6JtTnyWE7UBZW0eIhHFinjejIMfUZoRkHv2eA1yOQp7TTuGhyk8FzCrg5Z_hFP1wAlqXipFF-ceafcjWZ8YiAMrlYcAxYCTwswqSZq1d-F50T1DRti-MgjFTQJ4FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بجنوردی‌ها امشب: لبیک یا خامنه‌ای لبیک یا حسین است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/452798" target="_blank">📅 22:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452797">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4689a10913.mp4?token=Ag10z6Gp3lDMMA9kUWdm53rVIVknK1q7FLGlNxXQktjomy-zs6B_P0kEwXMr3Rtf809LyRzDmDfIs_fQhAgoA0mxzFHLzB1dLSmU0DL9lx1ERf3Pi8_JUlN91wua9EnnVPon3neTC-j-nfgTAsVIK48nymNOP6RD1hjnJoU3amrTL2Rp_4XFxyqc1tm2kdcQrquf1EZ-OcdDTNYZ1VsB0a6FKhnldbHAjMSQ45Yo1y2Gx9Ud80TfXMLv4_7AiUEKvMSmY1mvi0WHSnXQPmMYstNPB6A0yZcrHzaOL9XlkX1Op2QhzrP8o1i8g12_YARVc6Ftu05qASxoShvhnYGV_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4689a10913.mp4?token=Ag10z6Gp3lDMMA9kUWdm53rVIVknK1q7FLGlNxXQktjomy-zs6B_P0kEwXMr3Rtf809LyRzDmDfIs_fQhAgoA0mxzFHLzB1dLSmU0DL9lx1ERf3Pi8_JUlN91wua9EnnVPon3neTC-j-nfgTAsVIK48nymNOP6RD1hjnJoU3amrTL2Rp_4XFxyqc1tm2kdcQrquf1EZ-OcdDTNYZ1VsB0a6FKhnldbHAjMSQ45Yo1y2Gx9Ud80TfXMLv4_7AiUEKvMSmY1mvi0WHSnXQPmMYstNPB6A0yZcrHzaOL9XlkX1Op2QhzrP8o1i8g12_YARVc6Ftu05qASxoShvhnYGV_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ سقوط پهپاد ترکیه‌ای «بیرقدار» متعلق به نیروهای سعودی در یمن
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/452797" target="_blank">📅 22:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452796">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbf4462493.mp4?token=ACvL6Z1VGpFi3vl7rzEMXv7oGL6vkjC-LdSyw7DumtP1hdC-ht8jMweOybpMExffIqd-hqplkSlXCrmdgnYR7s2T5ZJH1sUP-0Nj6yFDfJ5YVnehoO6wlyqsw-UTvdGs_KdGRvDI13cQGgipsWJ_OVo2ZcYM7t0hsgoFk-CMkLzqeDb5C-2fgMHZE9uVSDl2_YoYkY4hUIlwX3rST2Jm7ebkQ3SaYNUq_5AdPbLqSfcXgku0iJe0HIBOws1Z601CgfU-00iF8WAAo5Lth7GWdLi9RQ__SoGjgOeFgcDOWnaRAaom9Uszc0hn_5ESbTTBRNqUr_yXhS752z2yecFUeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbf4462493.mp4?token=ACvL6Z1VGpFi3vl7rzEMXv7oGL6vkjC-LdSyw7DumtP1hdC-ht8jMweOybpMExffIqd-hqplkSlXCrmdgnYR7s2T5ZJH1sUP-0Nj6yFDfJ5YVnehoO6wlyqsw-UTvdGs_KdGRvDI13cQGgipsWJ_OVo2ZcYM7t0hsgoFk-CMkLzqeDb5C-2fgMHZE9uVSDl2_YoYkY4hUIlwX3rST2Jm7ebkQ3SaYNUq_5AdPbLqSfcXgku0iJe0HIBOws1Z601CgfU-00iF8WAAo5Lth7GWdLi9RQ__SoGjgOeFgcDOWnaRAaom9Uszc0hn_5ESbTTBRNqUr_yXhS752z2yecFUeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد انتقام‌خواهی مردم بسطام استان سمنان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/452796" target="_blank">📅 22:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452795">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJP8xZ7rSuD_SX_gtzkk3_3wVc_RxaOlZnZoGpEjxlcWap_sYISGzFucvUVP-4x8Z283I7v8ZOCwqy4Tbjk78PMRFR2aoEPbgqg9pWsBS1mX9ShbVL-DaAbeq4MNSIj_SnQoPyRjLbYwa2d0dZfqBgjoMC3X-0ZqS3Jb-n3LIA0kINOYMXsIyZeh3HDEgFsPj50s1K0_iU3L35F6vNufMuLxCLxpJUnXpI1lMKznZBtTYfWCmLrtHZ17YPXTPPGDEEpNiL4jbY9AuC-47J7gogu89_iDhl3zM05jAQ-aEmtFOm2aTLwQdNpukS0TAl7JxjTSfo6TtlPBk61-UV_cDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار رئیس سازمان بازرسی به متخلفان تعهدات ارزی
🔹
رئیس سازمان بازرسی: با کسانی که به تعهدات خود در موضوع بازگرداندن ارز عمل نمی‌کنند به‌شدت برخورد خواهد شد و دستگاه قضائی در این زمینه کوتاه نخواهد آمد.
🔹
تاکنون ۲۱۹ نفر برای بازنگرداندن ارز به دستگاه قضا معرفی شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/452795" target="_blank">📅 22:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452794">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dc9526c05.mp4?token=CPfqEyJtqr5qLy-zDF2uLv7pl_NrlTBPIMuWMrzLSuUjNECYI0OPzmaY5DPP75MFLDC1ZUwWhzC1pXkjXcmUGqV0o2b17uaxbgF_YhDhiJAKj0_FNUW9veSz2fKtaiw_ZqNqSoW622PSgDhO3ZSwDmNuMGizjXtlAZwI3D2fEWTDzGBTwJjKR2Ey9K8F3IVLNM_xd82uR2W0GGBV0kzQRJJeKmVo17Z6DcmmB6Kq4i-weWA9dUDB_eKB-p2H7ifTBYa9YnLDzquvBfnlkcgZjvsintXauhhxYnOpIrrEgipR19TuVsS6jYvTR_yCkHXjwKo-GX6cSUbui7y7sEISAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dc9526c05.mp4?token=CPfqEyJtqr5qLy-zDF2uLv7pl_NrlTBPIMuWMrzLSuUjNECYI0OPzmaY5DPP75MFLDC1ZUwWhzC1pXkjXcmUGqV0o2b17uaxbgF_YhDhiJAKj0_FNUW9veSz2fKtaiw_ZqNqSoW622PSgDhO3ZSwDmNuMGizjXtlAZwI3D2fEWTDzGBTwJjKR2Ey9K8F3IVLNM_xd82uR2W0GGBV0kzQRJJeKmVo17Z6DcmmB6Kq4i-weWA9dUDB_eKB-p2H7ifTBYa9YnLDzquvBfnlkcgZjvsintXauhhxYnOpIrrEgipR19TuVsS6jYvTR_yCkHXjwKo-GX6cSUbui7y7sEISAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حواشی دیدار یک یوتیوبر با هوادارنش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/452794" target="_blank">📅 22:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452793">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ac8177e97.mp4?token=p3E1P2dHgVZMajsLKpyDnjtHfxql3T48oMKlDI_aletzcn9w3SPkEi63mqJZ1atBUt4833apM_4cTxgYnQcIGiUBTm30lgglhBO3MOZ_zFY9_MZwPkFwb8N1X5WK6p-cr1coDLrEBB2VlCIeoMojhrnfXaakHlv3Ssn7wPVmEMicy9u1kY-2A2oP_HPLiOIHlNdjOiZloR6FwmjtfmM_KwG4ygxzvWb_6CKeY-EWWfw6zxJ5gEGmW6JcpkRcRRjxsh89iZXSPtiC_evWzlvrCSrI7aDgTpUDMAw4J7F1YzAXuJgf15rEj5g8gwt3axJY5zjLain4tVVoo2rSaeFBFCAzW6AcSfiauUZV-P3IbPGJskVQg20sqn3Bt8YSZ_gWpxv7rxjUe6qkfeC5algk4Xv5HDb4MpNzex-EoeiwCxV7x-P2XbCOd892sG3TXBfG_PH3oKxbk77KfbTzaGvLUxpWxr-7BRY9GkkbPiOAbnQzYbTx8bqtrsS-5_vRND65lgxv3C6WE6PXiZgrqJ0yIXSIw7jGnwplvUJgI1Wtk_A9-NLfldjJfp9CW3VOn8Q18RkL_hXgm3YtFKht0a3MabBk9hjFe6YxeAYRYLXZfSOhhDNSjTBRToaMwkRqOFsgA8xKzQXNP4y6qs_zXG3tjqnWn6qxl1kVXPLd8y4wjJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ac8177e97.mp4?token=p3E1P2dHgVZMajsLKpyDnjtHfxql3T48oMKlDI_aletzcn9w3SPkEi63mqJZ1atBUt4833apM_4cTxgYnQcIGiUBTm30lgglhBO3MOZ_zFY9_MZwPkFwb8N1X5WK6p-cr1coDLrEBB2VlCIeoMojhrnfXaakHlv3Ssn7wPVmEMicy9u1kY-2A2oP_HPLiOIHlNdjOiZloR6FwmjtfmM_KwG4ygxzvWb_6CKeY-EWWfw6zxJ5gEGmW6JcpkRcRRjxsh89iZXSPtiC_evWzlvrCSrI7aDgTpUDMAw4J7F1YzAXuJgf15rEj5g8gwt3axJY5zjLain4tVVoo2rSaeFBFCAzW6AcSfiauUZV-P3IbPGJskVQg20sqn3Bt8YSZ_gWpxv7rxjUe6qkfeC5algk4Xv5HDb4MpNzex-EoeiwCxV7x-P2XbCOd892sG3TXBfG_PH3oKxbk77KfbTzaGvLUxpWxr-7BRY9GkkbPiOAbnQzYbTx8bqtrsS-5_vRND65lgxv3C6WE6PXiZgrqJ0yIXSIw7jGnwplvUJgI1Wtk_A9-NLfldjJfp9CW3VOn8Q18RkL_hXgm3YtFKht0a3MabBk9hjFe6YxeAYRYLXZfSOhhDNSjTBRToaMwkRqOFsgA8xKzQXNP4y6qs_zXG3tjqnWn6qxl1kVXPLd8y4wjJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رایزنی عراقچی و لاوروف درباره حمله اوکراین به کشتی ایرانی
🔹
وزیر امور خارجه در گفت‌وگوی تلفنی با همتای روس اقدام اوکراین در حمله به شناور تجاری ایرانی را ماجراجویی خطرناک‌ و تعرض آشکار به اصول بنیادین منشور سازمان ملل خواند و گفت: «قاطعانه از امنیت و منافع…</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/452793" target="_blank">📅 22:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452786">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IjNPvjUFHWvr-Am7sKi9Ruho1y-DCLaAX0nJf6p66mslX4MDCgDCWyv5_2T8vcJKp2xQCsBNUHsTXtwgrO9BgDjvoXujtGx1xUGZwJktYGV2PypNm1eTsmsxhWqP3dY_tuezjFRnqPiuajq1CULaz8gp2ksx26BAEFV0OuoyR5ljh2_-2gmI1N63JuItpFCPIXhyNDwMDSW_reCpjqDcMNceCN_5htLRkTrp3ae192VDIsIa-NvfFqPVyZDeyzT3VwMhl448kTAKtXt3N8uq4tuzK0gOiqkcv1icoaxDitHJU8EbZQtPUSpbZ7S4CCMfuRfIQen5M2lUbZX0QFf2Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lKo_XRnDYm59wu9NviqUPCe7wMiR37BAMRvi5bEJqDPq9Rid2HnhIahOCYgmRNnjaCraY7wfaUepL1i3A5N7psIg1ezLg__xPVrjpRpcxHyNlpf4ksqNssElMYa4z3jQYHf0CGOFZSx5XCH2y749PvJeyVWmyaFleN4axhBn67Gp5htZ3a0FLKp4G1qZ8JD1BuevgVTIV3XS1HfldfgYQGCVovRQrpmd-99nDAoz84nqRQ7TO2M6OcMkQ7lTuhD71hrsZqaRqA7cP7687NkV5IKCiqrfFEPFBrdEsv78Audd9roiFpALiGTramiUvNdZ0VlkNH9KwmdY3ePgX49LJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hKWlzJwVGCEGd9HTeTmtSgEPvBdW1jfRu21R-mOGlBj4me9KGVdJcPc7qZ6iyUB-0zrZbC6tdQzB79yL2sXUDMNBMA6i2To2tnrawFYkdcj_hwJxQWMs25KIa3Ot-gsuoDyJ_RCBt9i4ZmOm0XTsb1nO_t2_LnIRvVc2WIFckyyJseaZ32ulj99zFsiXdsL5N2dllGcT73-pYxi2PWhI3tfSes_W-lAp-qNrz_DymjQklmWgbgPfH3k8hwuZgNvBv1HtYYCaEgIOxe4IHQAOxTObxxd-uqn_7rQ5DoYVozn1hDN1bPmXpkAwJUxIfP27YpusQS_Qd_ySCwOcqa1rVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ikkwn570r-ZlbkiSFYIP60LkoH32eOI7pA1EWyUAo8wfty2HAYcfsiXS0dSHrI8-2k6rPwoMv_9aex2I5B5SfYewzY9PP70ta9h_GbIvHRePj1FQfQUhZ4VTXZYpRSwGVswmKMAOpqx3KYcBF784ERXf0eWLz_q7O7f30UgQNsDNutG6faV6whiKfftELLTvr25ZD6XQa8kIq_Z5puuVRZyZBDWQGtdUbm312ePPfSkVUBpFFyInQIE55wUxuZf9NBEYYOHiL78ZtXvq3MvY_Kc9Uc5UAb3veoTq8A9iwOMWnahhVcJfxdmjzUjn04vZU-_8Or1gNfmgVJhNt6-BRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c6s81vaY8IINRxxO7TKx_CY7kQZy2QhABjHKMwuoAOQmQAgV_DbKD20mdh5KkqUteULF1JD0ZJaVgglAaa-5DM_n-2n7N1IQNp0vqnz9KSiw3ZB1bVJloeS8d1N-7YeWVjt6nOKlJWJEGoEEumlcG-TkryXj1x-oDhNkXpN4L7ZxW1Xkw69JTbqczbyVSc2sn5-2nMzMLtqfJbAvjnDC6JxLLHBlCBlhbWWDZl9bcG0SVbGYvZpKhgZpbt6onny2xKVVDW0PX7qDnD3c3jMd1xYdXSr88OO_5eWVd2r-9-p6PKq8fOBgbfEQTQCVuDpd5a09RY6kQIUORnrvkKmz5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XDei53wh85AiNhrY_breAD-QcnZoXLhdqhMExXF0wwaPR80_rFqLNhC-yTixeHp3j9qSv88_gqZpPDJf-bH9xxSWox8g1BjP4scMoOXFy6YAH_3Zz0vO3kjK8KI71ZTN0gCk86MtfjEv_vewbnOttwwumykvpmMR5A_O7ymkVzeDsnz1ElVYGCvyyU9hMa6s5LmUmno_Zy4vieLmHnR_UX7DAWe4n6ZN9HPx2tm1UV_1CWK64IyroVM3Czt6OLK5joO0PiR6eKmxZ6hkJDASP2JRbWyzNMC9fdCAevGMucKGPELcsxspj4blsbpKkkZPvHcoidASxN9Dfzi4fBMung.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXQagv95EsaI6nGuKSvtK6ZqVaMZ2Ragbk-pDSMtnid1dC9hCVyAqmiACr7gdoNGY1jvLodncfVVcw50f1AOu3B5UpVaaXmqDTAwRm5m8-1d77MyypSmYkYKAd_0FyNyoY-vUzhYulW6TITSZjoLCPdsFKxrDkc7V2yg5cFgaJQd5hAlMIDuBwcMFutoOJBGu6nSloScxutil9M5VqUbBGnuIeGPZp0iP0Qym4z13u0C0_-VScxZ-5GkyN5vLZCFF9i05KcOY64Lh9pzTUqopI4ml9Qms6RYfbGjT6EsU3c6NQh-xya_7ZrPdwAmi0sC3EfuZecT4njDLMp_7jMYNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
ثبت جهانی دژی که قرن‌ها شکوه معماری ایران را روایت کرد
🔸
امروز در اجلاس جهانی یونسکو، قلعهٔ الموت و استحکامات وابسته به‌عنوان سی‌امین اثر ایران در فهرست میراث جهانی به‌ثبت رسید. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/452786" target="_blank">📅 22:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452785">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYuOpQQKJskwlbBcSmnVAKGwPsbsb7rqJYmc2OGNv4ZlKj_dEKth2um-L5klqJBDHmE3qDKvimFao2ZNbzSC08xNNnuXe1d8fM623TMbHb5eieNkGSFJ5dR5oeU4NniPjW323GD7ug7x_HtaeyJlIn-XqzXtm-Zs-qKHlo3LwagqzTLzEq1ADwmX88I4xY22mpzxOjOM5suB2MhRMJ209BmjAo-EaaXW51fATIAX2olCO9dP-x0AVMgL5QKoYRR1VnXnqWc2rZtYxZgFkePdXCkI4xBi7Vl-OrLz28QHu8-pH_cFl_aUywMfvfeukITva-YsNANbkeiehbOzUv5KGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی به کمیسیون صنایع مجلس فراخوانده شد
🔹
پوردهقان، عضو کمیسیون صنایع مجلس از حضور رئیس بانک مرکزی در نشست فردای این کمیسیون خبر داد.
🔹
پوردهقان گفته «وضعیت ارزهای بازنگشته حاصل از صادرات»، «نحوه تخصیص ارز به خودروهای وارداتی» و «احتمال افزایش نرخ سود تسهیلات بانکی» ۳ محور اصلی گفت‌وگوی نمایندگان با همتی خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/452785" target="_blank">📅 22:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452784">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d8655195.mp4?token=kBfbFXiHqdB6f4gdjqXN9BBllM3iQRgCvbCdoMfRe2iNljpf131oYtGJ5-UM8LVfL2029qvP-4MsjmdBmF9eHEsM9KgPTZyV4-AHSeL1T4E_Ggd76g2nku-q-OJ6NHvemR-PY3Y2dBoz5SD9mKRndPXzZjzBYpfk2B6vXpf1PaTbhXXdYILEeYZ-TOlg0uFYbxFUY6rW2xnkSf4heEpod0NsV2o8Yku-wveXwiQVW_qvgTegm_BfAyp-Yl0z98ZTqwomtHPVCGN4mnm7rAPKpiUCHmMkT0oE6yu9bYh9CNAyKX8V5dVvxPpMcqJX6S1t_GJbGNY7m-XlsPubNo2sPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d8655195.mp4?token=kBfbFXiHqdB6f4gdjqXN9BBllM3iQRgCvbCdoMfRe2iNljpf131oYtGJ5-UM8LVfL2029qvP-4MsjmdBmF9eHEsM9KgPTZyV4-AHSeL1T4E_Ggd76g2nku-q-OJ6NHvemR-PY3Y2dBoz5SD9mKRndPXzZjzBYpfk2B6vXpf1PaTbhXXdYILEeYZ-TOlg0uFYbxFUY6rW2xnkSf4heEpod0NsV2o8Yku-wveXwiQVW_qvgTegm_BfAyp-Yl0z98ZTqwomtHPVCGN4mnm7rAPKpiUCHmMkT0oE6yu9bYh9CNAyKX8V5dVvxPpMcqJX6S1t_GJbGNY7m-XlsPubNo2sPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بزرگداشت رهبر شهید به میزبانی اهالی رسانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/452784" target="_blank">📅 22:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452783">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انفجار کنترل‌شده در جهرم
🔹
سپاه استان فارس: انهدام تعدادی بمب عمل‌نکرده از فردا تا آخر هفته در ساعت ۷صبح تا ۱۲ ظهر انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/452783" target="_blank">📅 22:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452782">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d0014135.mp4?token=a1EcBeIdiYSYwKuQQz1j6Ma22zcGVqJjvUv7_xFFvgPUEqCUo9WUobP6E9hNoPuL7QCOmtMloC1GZG7cQDJP_Dy13bCnd5qAVanI5rETDKDl-23wBOb_tnSDjwep2-mqFmt9mROj5AX_x7AskImZ8gYJFp4jP8mxV3ihJlog2LBsuUhH3_zV9vAl4AmSjTvRmzSdpHfgR6Nzigo61Foub6SM1TRtq-iXG4emZjncd9rgz5D84M3YFXV-FZWLxIXNyeVs7MgMVDkZweZ2A09WM1XFKcLt12mZ7vLKk59cne6VAm0tJrwFpygX0B0-sZXivAautSXykKBiC22lKUQxNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d0014135.mp4?token=a1EcBeIdiYSYwKuQQz1j6Ma22zcGVqJjvUv7_xFFvgPUEqCUo9WUobP6E9hNoPuL7QCOmtMloC1GZG7cQDJP_Dy13bCnd5qAVanI5rETDKDl-23wBOb_tnSDjwep2-mqFmt9mROj5AX_x7AskImZ8gYJFp4jP8mxV3ihJlog2LBsuUhH3_zV9vAl4AmSjTvRmzSdpHfgR6Nzigo61Foub6SM1TRtq-iXG4emZjncd9rgz5D84M3YFXV-FZWLxIXNyeVs7MgMVDkZweZ2A09WM1XFKcLt12mZ7vLKk59cne6VAm0tJrwFpygX0B0-sZXivAautSXykKBiC22lKUQxNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت ده‌نمکی از دل‌نازکی اکبر عبدی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/452782" target="_blank">📅 22:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452781">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22b05e30d2.mp4?token=UDYjKxsXdKQvT_cdhSHHLRl9AqWyk0Dp2sSM6fk92NFEWJXQzjzeCrMjFH_kd7zPKs9JxlL2IauF9kjpfSa5dWULXI0RezKSxpQcFyjd_RwFDN8vX76vKQ-AW4zIlcDlkj2ZqO27CAoJWSIuAqs6K2FT8xtFzu_wKpU6fZB0POsRtmcnxD-fowFU_JkO_KCr5HhaSBvyaDw-PpFNhzjMufALEMTpl8AKA0fLdeOzwhNUt6YoBJYgYzfZw8xJVsbjEyP4mPWaEjiFFpBuLXbpqebPDLXphLPlHNbjOhB1yR75AFGNcoDR_ulIWcV-xateC0jKYugrCRAxe6tVHucp4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22b05e30d2.mp4?token=UDYjKxsXdKQvT_cdhSHHLRl9AqWyk0Dp2sSM6fk92NFEWJXQzjzeCrMjFH_kd7zPKs9JxlL2IauF9kjpfSa5dWULXI0RezKSxpQcFyjd_RwFDN8vX76vKQ-AW4zIlcDlkj2ZqO27CAoJWSIuAqs6K2FT8xtFzu_wKpU6fZB0POsRtmcnxD-fowFU_JkO_KCr5HhaSBvyaDw-PpFNhzjMufALEMTpl8AKA0fLdeOzwhNUt6YoBJYgYzfZw8xJVsbjEyP4mPWaEjiFFpBuLXbpqebPDLXphLPlHNbjOhB1yR75AFGNcoDR_ulIWcV-xateC0jKYugrCRAxe6tVHucp4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی صنعت آب: هنوز در تهران، کرج، مشهد، اراک و ساوه نیاز به مدیریت مصرف داریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/452781" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452774">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKFl1ngN3NeoDk55unFewe-WVS5BbaiLU81THekcFPJUTltbDDP4fIbjuBtE5lkF4aiKRKGxiBqvfJFgCiruTpwt7H686zaItihbctgcPXooPygH3ehuyQ7QuCn-RaUfVJkKW_REwvBB36a8xlUauVL0Wq8FK9pZrYw1yZepn3G8elS76EHIxTl8QpLBaW9RCUzDbJmtdacgT1vdxiz-M_qt7kLC6qsTpa-kIMKwdh0ScBgnnplGeq0FEFmdS8i6gE5MrLs4hYnz6QFZ5OsjZBP-KsnrVkgMU-Lb_smXnrPVOiZrfvXsBlOHgfzHmkQm0l6CHyXtTn1b9yPhUvHhiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bOoUE28OYop0Yo5W_qJ_pEO4lNBCrAIeuMLVHT8cqdRazye0P-DFCJJ99EGFTD20KG76OgAYNm0O6HcEYm7XdfHDkH-sNTdcXxphYIbVyhXBZLzMfcbWE0DQ_NVScc23g6n8xQ9HUpbmoU1vtq11eC8lyzLwrUZYGFdPdBSS9pm-IbzJs_WLARaRK_ro8Cqg2xFDoGW6w0qbalqD69oXxpjkdziwWYhUsuU2-xd0-UfAyuR4HwFosHA83En9c0yQMXIjfhK9M80SJGAOtEy5jK2uFCLOtnetJtOaJW1Wy_dTZ67IdgUKJLaGYI4L0ToqhkljT5z2JXPVg25EqDeLTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wf5KkCbp5OCyCr0f-QyV_HFviNk0yvnU6TxTftTmROeJl01DCJs70fKmC-mr6j8w37zmgNXfWKrL0gfMV-ZE-h2M7U4KY_jQZOF-oeublx6gZMbImLlIBH9xqhKAUmaCKcQh6Xs4aK49jHO0hLRFkAJrj4jNI2fJYFGH3iMbYQp8cIQB9-i7Mu1g9nKo0ZYDDqB_igtX_caJqnEhYG783o8trIj9XnkTaHOKJXVCqhFjDV-MGL0fklUaL-eOpsqCmaLj6JIA7q8oG7rnpbo52BJ-Qdp0XaWtINJm7j2uWu-C7rirHp1MXv_SSmG2CPQtyoyLP4HvMeRnyUoT1QmWLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tYzM5XEWJU_PZ6WligVMI-eAyg0_YSXEoWcvowGCGI1VNJMQRzoi4APQZm06qHmWK_oKkEaECDEfnVPGEQE3Bov-W-g_AD1fhgULly7LGeeVs1-AA5Ku1RQk_dDD8ygbS5MYMZqM5grvJHCuKJUeeDpqEaFSnkLv1n0zWZh8WxyfhB3IpV7cCxuLEC0znNBpcMz1AFEXnmi4R8iiTIZ-FRKcxtYdakA__5uAgxii2VvhiFNw94HIbcWRUxYg5wpWfgT19yk5EuFBHg3JiU6BcbWz824a5balvSNIBuu2Liy5mkDBsnpOMfTuF_68BgjUqsXqZE4-nfIV-AWppNVygw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rF_ir7IV0t0fO-i96H4hoJ45jW-4Kd_rh8Fne0tw0gePxfqfb91SxunMk76f5TUoMSXKt0wdHzFUirMg9GcYzPvl_gexe6mRnynuJMYvN9dp7nIbLZSQRFCCKlHG98cNasTkv9JtgCfVzeSgl5TvqWhKbC5YVb7pVV1mW99qokNS1d1iYEAPBkLQPKhnPOWWbBwzXmFbDGzIDch8lNqRTuyr-oT3Em54vpK6CCNN0ocSPLQal_3FIwiFF5ParGN4U4gnXLXA9ojCO8j0fYxYxuXBH2r7IOacGCsl89Db6rWDTLToy8RqQWI8j7bc5-ZmMiw5-R4HiAyPmRtfulTSnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DGgzRIOyTnonIQetxYBUq8ULalhUN2alfmaXvQlpsc__YGjrpanBtNbrGjfee_J5DMh-YGAVFhgtUTFJZ9TOC91hzxmW7ivMHlDZWxwgpT0qFjJwmMQPSmPczJ3JVlQb7aXYmhvtMcPv-f9MPJRjsaFYudoDzVIX2DIi6F_icL6tCvEL0S3gVACPbw0rxZVFMokqka89RwMquPQ-Ebp5OKe2bkTIRe1JkJ2cRgrsC7djx8Yr-DCmy00PbkqNKRFZckIxiutXbbBDmFSyJ-tHzyjoor_3nyBH3jE1H9TWsWb71IvSsBldyVNA66Z4LF6LKa-BQXOTyrvsoHA5paJiTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZxlShdztL7lY0j4A9hh--F8DVnYrdrmQ99_GkTdlNr0lTAKs3Lsa3foGuOViQBTYTYxEWdzgzAh3lbBwTeu5i37GMrGbj9JJrE9Xzu_FOn8YR6NmasYoeNlA-LcB_KSQJM9OvEz84IGy_axNfuNremXgffDU1sFSg6fPYtDyS0c5fmugf8SJPS46N5tnF3oNYGX5VttBtnwj7K438EN7U8TM6hQSzFosUalNfzKt0m5xY0WeWPDS8FhnxhmtWd-j8KclumyWLLRWkz0EToEOxzkt6eno8srEYkRaiwkEyWGh7RMeaYHFoykpsq2fvqSxU5W0LjgrIZu7hSg9KfYkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
میزبانی گرم عراقی‌ها از زائران ایرانی در مرز منذریه
عکاس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/452774" target="_blank">📅 21:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452773">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یمن ۳ نفتکش سعودی را هدف قرار داد
🔹
المیادین: نیروهای مسلح یمن طی ۴۸ ساعت گذشته ۳ نفتکش سعودی را هدف قرار داده‌اند.
🔹
تعداد کشتی‌های عربستانی که از دوشنبه گذشته تا امروز برگشت داده شده‌اند به ۱۶ کشتی رسیده است.
🔹
این منبع همچنین خبر داده که  از زمان آغاز محاصره یمن، تاکنون هیچ نفتکش سعودی از باب‌المندب عبور نکرده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/452773" target="_blank">📅 21:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452772">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec381246f.mp4?token=f3YRH6vNBU7g_FdOewCu6NDxaukCFIb7c94Pp7vtz5Pn3zBEtf09gs_2snpTdRmFHPqGO5sdqChSgCY8eAl1WmT4Ru6cJ3UmnEuMEy4WY_fS87erkqMiwQ97dl9i5TotFg1QODjRcVAjnr7npIO-HoTltxuitN7SWrU_C8bv-dlRmQ2VYfV2As_vV2SVCFx4SzOsuJmnIvXA0f_GzRsQGKtJQ1oW9o9FifKU0uQ001gY-aWA9joU444FzJcFUJZuSGncXd13EcsStO6uq98Doj-UigT45RRQEHuvMv0yFH-fJOpGUUpA97xXpu5z18FvNoN8SpY_oo6TlP-o49yjXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec381246f.mp4?token=f3YRH6vNBU7g_FdOewCu6NDxaukCFIb7c94Pp7vtz5Pn3zBEtf09gs_2snpTdRmFHPqGO5sdqChSgCY8eAl1WmT4Ru6cJ3UmnEuMEy4WY_fS87erkqMiwQ97dl9i5TotFg1QODjRcVAjnr7npIO-HoTltxuitN7SWrU_C8bv-dlRmQ2VYfV2As_vV2SVCFx4SzOsuJmnIvXA0f_GzRsQGKtJQ1oW9o9FifKU0uQ001gY-aWA9joU444FzJcFUJZuSGncXd13EcsStO6uq98Doj-UigT45RRQEHuvMv0yFH-fJOpGUUpA97xXpu5z18FvNoN8SpY_oo6TlP-o49yjXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم بجنورد بدون خستگی در میدان حاضر می‌شوند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/452772" target="_blank">📅 21:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452771">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a84e97bfb4.mp4?token=AzCH-7ewIsdT00T-r9xsaMxSfghu9UQ-6otkvbnl0ofUIBu2kL8upgO3e9yUOG5LvdfMq0bbBXkHl_I9TXsP-R6PHxVz-gyZbddlQzAheEtApYzkTD8oa0G84ww01IoqexGMGxVoSFQpCwI9QnuXZqsH6Y2ckJyMReGWXpLFYol6OAG1CXo2-24QESR7NdMRn1C1yKldlsuWPW44Dg3SWx2ce5ai2ZqIztLf9hMZ_0ftBJgSKfowqSM_mxuocrXcBi-iLyfvn03DSvc5CP7OYA1Hu6BON1xqFgqnrJLeeVbUFIiwX4beJZC_jxZQJGacq58TKw-h270LFzvbXYLcCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a84e97bfb4.mp4?token=AzCH-7ewIsdT00T-r9xsaMxSfghu9UQ-6otkvbnl0ofUIBu2kL8upgO3e9yUOG5LvdfMq0bbBXkHl_I9TXsP-R6PHxVz-gyZbddlQzAheEtApYzkTD8oa0G84ww01IoqexGMGxVoSFQpCwI9QnuXZqsH6Y2ckJyMReGWXpLFYol6OAG1CXo2-24QESR7NdMRn1C1yKldlsuWPW44Dg3SWx2ce5ai2ZqIztLf9hMZ_0ftBJgSKfowqSM_mxuocrXcBi-iLyfvn03DSvc5CP7OYA1Hu6BON1xqFgqnrJLeeVbUFIiwX4beJZC_jxZQJGacq58TKw-h270LFzvbXYLcCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک شب به‌یادماندنی برای بچه‌ها؛ دعوت احسان مهدی به «سر سفره خدا» در محرم شهر
اگر به دنبال یک برنامه متفاوت برای فرزندانتان هستید، «محرم شهر» هر شب تا اربعین در میدان آزادی با بخش‌های متنوع و ویژه کودکان و خانواده‌ها میزبان شهروندان است.
@Farsna</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/452771" target="_blank">📅 21:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452770">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43066ca80b.mp4?token=qFkTmzizy2jfWAlF12trIq_SuxRW9tofARpAUYpwbqdQCvGEapN-X6P2aBZ1CSLeV7EKg_0XMfph2lWt1MbP1q-jFOk7YJAx9j9zzV8FLuyWQc1EVsBy6nDmMmdu-CiuVKZ_1EOP8ou21_bo-7MgOlTXo15LgKHKKwuncBJPaeFrWfz37G5oj1AI9lgmxRIXdE_OI5_f_WedDlvJPuf8Bbai2kiuvtCzLF4ZjUIYzUYIU8FeHOfOcRbv2z8y5-9Vf4t8jww4j2UBXaL7oKyxVCft7hCYnF0nMoX87HRXM_9uqKyNA8KbfEtS8_7zxOekadtwl3FTzK8tQADmMHlmB1O00HHzP1Xb02QPVtKIgsqHICKcU0EjWG2NQ-NpAC8E6nMjcKZdjYSSdSxeoKICOhTM9ytexbJ5S_j5hRbOKaxbAWJxZHhvhHPcrZHrqLugrLCMKlv80E4Enh60vcM53iACimR_rNI49PugIxEjoZSfv1G_7Y4tKfHbJJN1pB0yMS5QdaGBrUq24h1y4YCOXZ5roih0dWimdhUKm0AB2F4jLx4F0YaOKZ1OOyfvO6fPealuP65LeNIebPIfYCJWvTnDoiROVm6j90RiAgkJ09TNZukaQuVHq8tB9DM6o7d4gkMgdxfJeW85eVwynyk_tlKcfdvY40OStP_db8TRNJE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43066ca80b.mp4?token=qFkTmzizy2jfWAlF12trIq_SuxRW9tofARpAUYpwbqdQCvGEapN-X6P2aBZ1CSLeV7EKg_0XMfph2lWt1MbP1q-jFOk7YJAx9j9zzV8FLuyWQc1EVsBy6nDmMmdu-CiuVKZ_1EOP8ou21_bo-7MgOlTXo15LgKHKKwuncBJPaeFrWfz37G5oj1AI9lgmxRIXdE_OI5_f_WedDlvJPuf8Bbai2kiuvtCzLF4ZjUIYzUYIU8FeHOfOcRbv2z8y5-9Vf4t8jww4j2UBXaL7oKyxVCft7hCYnF0nMoX87HRXM_9uqKyNA8KbfEtS8_7zxOekadtwl3FTzK8tQADmMHlmB1O00HHzP1Xb02QPVtKIgsqHICKcU0EjWG2NQ-NpAC8E6nMjcKZdjYSSdSxeoKICOhTM9ytexbJ5S_j5hRbOKaxbAWJxZHhvhHPcrZHrqLugrLCMKlv80E4Enh60vcM53iACimR_rNI49PugIxEjoZSfv1G_7Y4tKfHbJJN1pB0yMS5QdaGBrUq24h1y4YCOXZ5roih0dWimdhUKm0AB2F4jLx4F0YaOKZ1OOyfvO6fPealuP65LeNIebPIfYCJWvTnDoiROVm6j90RiAgkJ09TNZukaQuVHq8tB9DM6o7d4gkMgdxfJeW85eVwynyk_tlKcfdvY40OStP_db8TRNJE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
اربعین، روایت همدلی و خدمت است.
⭐️
موکب بانک شهر با حضور کارکنان خود در مرزهای کشور، افتخار خدمت‌رسانی به زائران حضرت اباعبدالله الحسین(ع) را دارد و با ارائه خدمات، همراه آنان در این مسیر نورانی است</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/452770" target="_blank">📅 21:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452769">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/452769" target="_blank">📅 21:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452768">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGwZhNVGXxA3OsuIBPNi3pDP9jou3EiX2UInTvgZq0phQucichTeASy8o17FGHTCiPHzRPHrT2CQbVryt0sGuByIYgOR7iuUERzz7HGCtJ3G0vao4h3h3W08WO3BCfiQ5HB5lQlzc970I01NFlKes_KnVqBEgv0skSoRjeM4N0pmDYPhcZSThfdwB3yOR14ZbpEn7WAzP7_fJxUPzYq6u3c9z-tb6qR4p927eh491-y3Yk8OjyQIMBlrB_T0XDDOA9LIC17ABw9-hWdGf4PZXgUCUXtQEiWIjBFWGIJW9_WE8ISH6vxVgdwKrMamkR7odjD8DWbmh80JGPnmVSt7JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: اقدام «فرصت‌طلبِ مستقر در اوکراین» بی‌پاسخ نخواهند ماند
🔹
زلنسکی به یک کشتی تجاری ایرانی حمله کرده و یک ملوان را کشته است. این اقدامی است که به‌وضوح منشور سازمان ملل را نقض می‌کند و به تحریک اسرائیل انجام شده تا اروپا را به جنگ آن بکشاند. @Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/452768" target="_blank">📅 21:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452767">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S47atVLXKZ0drR275DEvQQfsnjmw79eSYpvWnNb85WCGF-g7ht-TvuSBxhaJ5Kq8uYafYhQ6cWotzXZrp7rCVJRXoU8Q6-w_xqGkHgohbvQgSaT1jxmvQv8kRBJIW3o28VmPmgNCZKXjEq8kJ5oax8oTd2cwXuyoFXWdhO8wwXqbGwSQArajRA3Zp8dLI1vtIw2dVZiJ008lb3vER7VDiXCxJ193ytsuLs08hUNYKx1spKAEyRgONZw47xsRdLbyfa2B2jd2zvPLtFsl47_bk8C1oViv3kfESs8HDk1J9ErV5h4xztI9uEHlP2CRNdN7QDVn0S6ULyOQQfVJaMeWGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۳۸ ماینر از یک کارگاه صنعتی در تبریز
🔹
شرکت برق تبریز: از یک کارگاه صنعتی، ۳۸ دستگاه غیرمجاز استخراج رمزارز کشف شد؛ هر ماینر به‌طور متوسط معادل برق ۱۰ واحد مسکونی را مصرف می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/452767" target="_blank">📅 21:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452762">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D88axhyG-2034I3oqSK-x7OFAQxeltqN5r-38RVVVtOr_ouUG_OhucKkwfqsJtnHGYshZ-zBB4IYQ95CDuMtIj1wW6u117k-6J4qndisbDRd4AtF-IGsXfir3HCz59I_Sfij9TZCKs4Dg0IFR9bY1H2xL8iqwI3Wno2TZT6sIZspT_cHXLyr9xJ8uXw5GfLbpqPHBtG8qLC2odt1JTqbtQTGZ4p4b83gaQJCh21N5QmmkveKEJpUGupyFuUsX4caJNTmFiapEiNY5J0awpOUgQ0_EhGtnsqvtMshTtxa1UCaHLu8Bq_i903uVjYURBe0yUZw6OGbhfe9cjQOrNQrsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t3I7gygl4fF-cKs1K5mK_ESX70wBaZZUGMDVT2Ie8tZUgsJEzFql28OfhE9xNkVO_KLsiLVaEjat5ghAnLOcZ8lsFcA386Xyli3fgDZ_NPJg2LKpm2mpAZjykz8E63Ctdtn-GR4GFWyJ1gdeQFen4vCWrTNFR_bbeVnvJtJYi2cjrq1RE7dIS_5u7vz_gORojhG0FYY0lj1DWou9Hvk386hzF2pUhcxAbCQuyvbthKXCHm5c4xtOee2IvExhWlWBbS_Mg-45IeFpqZxKZwGC7WzVijYdYfBQrw958fjz8UBfLqMVPY6sSK3bcoOJkgvIsg-VmZB4ihHWiRrGUx3MQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DgvK7iJMJ3zLpKhCPWhdR4uyY4Po-DfCqPuFXhKt_Y_n0ECa5fBh0m7l_r33RSvW0URjyUZWndwsBIQ_UJHiR0BgxytGYN4maqiRr0Dhd2tBKIM69pBpRpQs9gidT7ztIPlMc-WE2sCXwvFtsmqALCgidC-AbRmXkwUaUFmuWhk5rXrCFTyK4lQ5xceUYa26qoQw6LCEfwkMtjKweNW5RF1695vn_13Vd77uR81f4zWtxzHSf7rLwj1bFD_bc-CVZUUBgcU7EDgF4974-4otk4UdzH6PM-u6Hg9cDoUUCaGfC0Ky_3AzwXC8HMuXukR5ZxLuJY1jqKuOs5xNuEvTEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oYJUXE-sbEVTZL4C1uDBJGyxriViHVUAPi343mv9llckwREn5a1Lk3macD0yysPF6_ux49FvSEcALTgC_X5yjRLUzvN1nd6uXsQQbpphCX8Q-Nts6YsXTEXGzGXwZsBeyHvpAR9hgMn1ZpPOChxxpB6hpbwARKBgn3lAW46Iy28E7u4ZeIlqmgFqbiGA9PSOlVhT-qERB0AKIUbeKks1HDfQzn66rTjx8mXlXPlBQTYXypyWAzItgskVdVJwH18dNy-HUMPo7cd5gxqE7NJkYv1nXF3odgg_hIcH-u0byKCWORX1VGBO0VMxr3Ykm4_LfxOGlarmY7qP9bDkUPPriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aTNlMACFXxq3timMb72AD61om9hbTKSSsMPL8mj-ZIQdwO-wHbgT9nsbDI5gSvlx-0XMICJ5hQcN3ROfh2JwO79wfrExwL3mtr7nMEo95-e3Jbp_J2On0TEQ19Ywd1p-C_OTrmCPromTkxFkyojXogO7ihCjM3jXWqQNRcyGUsnJGoW1OqP6QrVQKa-tgRnkmEbZ-H6xCyaejsa_5jZhUzse4UcnCYrn0xV3AvaUyvZ23iWRJ5NTPKr3PzSP_uALO6Hsdr5fhrjGe6Jqu_vs8iowdqTqduUSaOMVg4RsHm06XRJFIvroMxynWTEt-il63bQZmQD1A0kckx7eb3yk2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
تصاویری از سرنگونی پهپاد «بیرقدار» متعلق به نیروهای سعودی در استان «الجوف» یمن
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/452762" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452761">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPNm257xmRoksmKI1oeZIutg4Bj3xtsSiEWG-sMaZ0cJYcNmfElNYDrDMq6ZDyMdP-aoNRHa9B7rUYcVSlFl76XdsVEb6V44lDaYHtkSZIYCZLMJuQfn92pwXZr-KBQf1IdvqZfHfp7zB-o1AFVV9ypNYOCt3SQOEek0Ft19hkaiIA2GDUqdBKo5ykHHKRSoCwVqUBHnC8wkctbGYedAdwSh_YUO8Bhml1FLNMeFu1KHfRmO7xGpiBGNmfEWro_nZadRewQ_IsVei9Kkmwm364xoIUHjpT6zV5NBW9bMPFRnl7ChxwfEUbWcYzpzpggE16_BKQo2FnR7fKjPh5QohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیدجلال سورپرایز قلعه‌نویی برای نیمکت تیم ملی؟
⚽️
شنیده‌ها حاکی از آن است که سرمربی تیم ملی بی‌میل نیست سیدجلال حسینی را به جمع اعضای کادر فنی خود برای جام ملت‌های ۲۰۲۷ اضافه کند.
⚽️
گفته می‌شود در روزهای اخیر نیز گفت‌وگوهایی در این خصوص انجام شده و طرفین درباره این موضوع تبادل نظر کرده‌اند.
⚽️
بااین‌حال، باید دید در ادامه این مذاکرات به نتیجه خواهد رسید و حسینی در نهایت به کادر فنی تیم ملی اضافه می‌شود یا خیر.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/452761" target="_blank">📅 21:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452759">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/np_yh6oM6oGLxALhdktBLbFZX3PVXy_3iMnp9KAMXskMsZjtpFcBy_7KPlw8MZkc1N3IOSARVXumtrgQip2oUZkk-8Z6OWbaaAgDOWYey5jtGMU_uvFapuHmMXtEDYXDBZjnT6VhY6A76e3ggY9Sx7fY12ETF4sWKm8JsywofyuK97Rp7ESmUggaCLkh0NaULbkcHuX99HVRerubOzX7B0ZQmZBdWRjC2I4ojLoo14wzn8DvIoYaQbW_y5pSz8-zvCs2Lz78wi2hK7kTympjgZYgeMWCc1k19AEjzsQRmDpQjxWpxSjJIcqLAtq0uteGxg8Df-OZdKScfNECXdY_wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وکیل پژمان جمشیدی: موکلم از اتهام تجاوز تبرئه شد
🔹
وکیل جمشیدی در گفت‌وگو با فارس: رای نهایی در پروندۀ پژمان جمشیدی اعلام شده و او از اتهام تجاوز به عنف و اتهام زنا تبرئه شده است.
🔹
جمشیدی تنها در خصوص اتهام رابطه نامشروع (رابطه غیرزنا) به تحمل ۹۹ ضربه شلاق محکوم شده است.
🔹
به این حکم هم اعتراض خواهیم کرد زیرا معتقدیم در صورت احراز چنین اتهامی، مطابق قانون باید درباره هر ۲ طرف رابطه حکم صادر شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/452759" target="_blank">📅 21:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452758">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e6ce6e816.mp4?token=g9T4LWELTSN0T27bcDDPKD7mxWxbtfDqyHFXbjGp0iQTDAlrwEcz_Lc8cwGYt5RGQn4YOGGEESht1y949P2AK7Z_l8i-ZQA7r2TKEAuSE0jZzYo6XjUKabgAFVlTOwl28Gycnc3xmlkyajpucSFVFg7B3AdKW9llWKPL70mit5DuOdeaCKBFuWbkt9WuIzMH3NAAaQsUukZMiaokLvqUuYVcI87BmOlt6Q6-EapAR32TggL5myEMreh-WdFIAyUHBltNi6TOvU80BUPrnBSXPSlIszwcxM9ACuHznCkU9qydhmXrsVfJjiZ4FibCy4tJTYDYXeFVK39Qk63zgc1wLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e6ce6e816.mp4?token=g9T4LWELTSN0T27bcDDPKD7mxWxbtfDqyHFXbjGp0iQTDAlrwEcz_Lc8cwGYt5RGQn4YOGGEESht1y949P2AK7Z_l8i-ZQA7r2TKEAuSE0jZzYo6XjUKabgAFVlTOwl28Gycnc3xmlkyajpucSFVFg7B3AdKW9llWKPL70mit5DuOdeaCKBFuWbkt9WuIzMH3NAAaQsUukZMiaokLvqUuYVcI87BmOlt6Q6-EapAR32TggL5myEMreh-WdFIAyUHBltNi6TOvU80BUPrnBSXPSlIszwcxM9ACuHznCkU9qydhmXrsVfJjiZ4FibCy4tJTYDYXeFVK39Qk63zgc1wLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
رواق دارالذکر به‌روی زائران آغوش گشود
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/452758" target="_blank">📅 21:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452757">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VB1qZMW8kSi1Pjvbau6URFHGodFEwLPHtl9slNgjpHLKQZTLSf7-brZnGZwHR_khhw3fzpfrbLqbKqfLVa-FcsYUiXLSWPV7fckwt3JeLL0lPi4zUJYfuA8KjeYD7UqGlepW863qEhXUTzp2z2S-AHIGI6I79LY7vjSNJWIv7t2WCQBram54ob5SDDkf6H-c9IAooUGNuJB5vGWyBDaFigjeVc5dWzpbVEC1eF1Oj0Lwx4K6l8SqDRThYZf5UJJrSvaX5S82yCVd3k1cRHRQEE9j5J7LI3LrjKF6d1bhBhz_actb2siDQ7xizBKZ4Hly-uel1TqCtcvtG8I-pG3LLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
لطفا عدم واریز وجه کالابرگ برای کسبه را پیگیری کنید. خیلی از فروشگاه‌ها کالابرگ را غیرفعال کردند، ما هم به زور ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/452757" target="_blank">📅 21:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452755">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سپاه: عملیات مرصاد درس بزرگی به خائنین داد که هوس هرگونه تجاوز را از سر بیرون کنند
🔹
سپاه پاسداران در بیانیه‌ای به مناسبت سالروز عملیات مرصاد: در پنجم مرداد سال ۱۳۶۷، ملت ایران با تارومار کردن منافقین فریب‌خورده، درس بزرگی به خائنین به ملت و میهن اسلامی داد که تا همیشه هوس هرگونه تجاوز را از سر بیرون کنند.
🔹
منافقین همواره به‌عنوان پیاده نظام و ستون پنجم دشمنان ایران و ایرانی عمل کرده و از هیچ خیانتی فروگزار نکرده و در فتنه‌های کور سال‌های اخیر از جمله کودتای نافرجام ۱۸ و ۱۹ دی ماه ۱۴۰۴ نقش موثر و پر رنگی داشته است.
🔹
در  شرایط کنونی دشمنان انقلاب تمامی ظرفیت‌های خود را برای تسلیم ملت ایران ازجمله این گروهک جنایت پیشه را به میدان آورده است.
🔹
بی تردید هوشیاری، هوشمندی و بصیرت مردم مبعوث شده در حفظ وحدت و یکپارچگی ملی، اقتدار و صلابت کشور را حفظ و پروژه خدعه و نیرنگ جبهه نفاق و معاند را ابتر خواهد گذاشت.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/452755" target="_blank">📅 20:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452754">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRvecIXOYPtGKjBWRcI6dax-NyKHPEPomM4Tt6QKNTYAsQ8DT9RKOCX8ot7agaestIVC_g_4lcoIA7lXwU8GVGS9x98yGtnNSKzQJJjMWL3vmzq4Jxo8ui0uJHc4qOj2HNyBbPI_lJFjLyE8UzEwx3Q5CY7ng0jSu27_iUAApUWpFD-2YLDyN0MRnwUBk-40DvDN1Zw7tyuU1TRNETRTGMZsVB6GCO4bOqxu09EJioQO34FxTEjXF7r2BbSiOryMJCAJfc50g6i9bi4J-dSyC-vsPbi_ojqLIE_P_7fB-q0KRN8oIb4VlpnjkTMVYKaeXfmN4w6ovW-NnlRjlSeiZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدا بر روح ملکوتی سیّدالشّهدای حزب‌الله سیّدحسن نصرالله و همه‌ی فرماندهان سَلَف مقاومت و یاران شهیدش</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/452754" target="_blank">📅 20:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452753">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a982009c3.mp4?token=CjIJVqVnYLpRSSneyUZ9iYv7pTRFsBLWtZNyXpUVNR73qiKCOPkiHzYL0hdCvcjVl-OHjOI8VvyVGUj3X1uh9KcZ_MjfYVamjeUg0XwI1N0V5IqCAYhsTWUznOHMfumJrwXcRrQuuH-uPC83cBkInhB5mi8AS4xJKeocmQMUahkW56QNeJh1DwT4VXaeRrHf23hZ8U-CSoM7X6p4jLNzdRDTzGkcJJUKJ4j-fkyI_GEFGXjQN__8tbE8aracjiiA4Ya7Mf3QcIZB5KaY8qdKzpQTzYjXrXshtGxgEujMgK6n2ms7oHoVi8imkxKoFEQdHiRJhtYUmmRAiw-1n6oLMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a982009c3.mp4?token=CjIJVqVnYLpRSSneyUZ9iYv7pTRFsBLWtZNyXpUVNR73qiKCOPkiHzYL0hdCvcjVl-OHjOI8VvyVGUj3X1uh9KcZ_MjfYVamjeUg0XwI1N0V5IqCAYhsTWUznOHMfumJrwXcRrQuuH-uPC83cBkInhB5mi8AS4xJKeocmQMUahkW56QNeJh1DwT4VXaeRrHf23hZ8U-CSoM7X6p4jLNzdRDTzGkcJJUKJ4j-fkyI_GEFGXjQN__8tbE8aracjiiA4Ya7Mf3QcIZB5KaY8qdKzpQTzYjXrXshtGxgEujMgK6n2ms7oHoVi8imkxKoFEQdHiRJhtYUmmRAiw-1n6oLMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تمامی کنار گذر پل‌های حملهٔ آمریکا به هرمزگان آسفالت شد
🔹
مدیرکل راهداری هرمزگان: همۀ ۹ پلی که در حملۀ آمریکا به هرمزگان موردحمله قرار گرفتند از ساعات اول از طریق کنارگذرها فعال شدند که اکنون این کنارگذرها آسفالت شده است.
🔹
کار بازسازی پل‌ها نیز در تمامی نقاط آغاز شده و در کم‌ترین زمان ممکن انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/452753" target="_blank">📅 20:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452752">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">رهبر انقلاب: جهاد شهدا، مقاومت اسلامی را به درختی تنومند تبدیل کرده و عزت لبنان را رقم زده‌ است
🔹
صلوات و رحمت خدای متعال بر شهدا و مجروحین و خانواده‌های صبور آنان، مهاجران فی‌سبیل‌الله که تحمّل مصائب را بر خود هموار کردند. سلام خدا بر روح ملکوتی سیّدالشّهدای…</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/452752" target="_blank">📅 20:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452749">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IeV4auuCACVDFGSDoU4xPUZbl9VG4EIAHmzgQ8esdN1US46rAWrnANDhVyJbY27Q7p8DM3qaUJ9rn2wZo2VYzCTcZk5Qcx_a_Tp7MKo9XpPAHtqIHKc6zWdE4HDMg1T_owg6q6K1wYOVE10pIeYglh7rTxLsvHAF7RhWHkxFvRkVGJhFG0hqmA-leOOMJCrmsNSFIyJPumQOLVpUz47-Ufg8_j3016kbKlw6aQbBMr_XNxNARCC520YeJk1OQGgov3gdQgCLFn_pZpRoltcJ7GNnMocdTyqF7PEr2LT6wXqPSn52mTi-DkvMHT5scq1ADMfet3eYmqKsDs0dIfyHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e5d6_ycwSfqZ3n2_UMBj2wA7X9sy1IXEgMCsjQ_JNWWTa4FQqz7Z-TTuvTsC7bvE5dwN-0USeaHSZierwxwwspX-hzi002APaQB1SRp5ZCVONZZrgEhWaiEVhEme-1M-jz1GpD90kS0YQxsLGNn7sggJBdFDdigieuoMWKvtlFcr-gfdIbUMRJXJsaBHKndLrA_RbFuchp7_fw-3FS1wx4D39Ftn-q7KCCnbMWc8mRzwqYK3OpaW_cMklq41s6_-SwW5EbdfgKU6dqto-lyIIb0z0ISMCaQB4JJHe6dm8j3P3kaND2U2kvnOUACSWeWqJsMXYHNctuvtfuQ9N5tvwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-L0FfwHBqe9KwEzTf_wLBxx-no9fBAq6qoDoNT4vtye4_ozXGO3IOzGQ5UWdHlFgz4PYH1Aa6w6e5EvjSzJG-Zbrn6XzpKEo4TBd7JOOpUcjDwdGSeE1IpokzHqBh49AVIZhORb-vzvIifboL1sRtWX6RUpEyjD0E0yUCSLViPgRFzWuZ6m3I0TpaVtWhx6M8fRBGpoPcbrOq0mpwKSWNvi2NHpbdyQw8qUgq1RQuW1CFNbHk75tvQg9XnUVx5PtFdp9VeCDHLioN9zTFGuEs86Tv8slA5lTea8LrnI6yT5Xn1hdVsTKsDpGhWWQDAS-nbEMcseO4sdrokgGCxGLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
۸۳ درصد جوانان آمریکایی خواهان اتمام فوری جنگ با ایران
🔹
سی‌بی‌اس‌نیوز در یک نظرسنجی نظرات عموم مردم آمریکا دربارۀ جنگ با ایران را بررسی کرده است.
طبق آمار منتشرشده از این نظرسنجی:
🔹
۸۳ درصد جوانان ۱۸ تا ۲۹ سالۀ آمریکایی خواهان پایان فوری جنگ با ایران هستند.
🔹
۷۶ درصد مردم آمریکا فکر می‌کنند جنگ با ایران سخت‌تر چیزی بوده که دولت ترامپ قبل از جنگ پیش‌بینی کرده است.
🔹
۶۰ درصد مردم آمریکا معتقدند ترامپ مسائل مربوط به جنگ با ایران را بهتر از چیزی که واقعیت دارد نشان می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/452749" target="_blank">📅 20:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452748">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFVSOreiiI35ber_Xzj45I4Ua9rI7RTU1BsoG7xZl9DxQG7VN4hksp-OUBipg7JNU0szWXRF_HczdfrupfEzozyUHgJoYkbYt_hXw9PmUAcUwg4VJt4us0Edv7n0INU3GOpXLFUF3IHNIeZCQYyk14ElSKQAcy3US4bAfTIsD_Cz-dkSGSb9rX4quFwrjvi-iJx40soPv8fHyamr_4_yqDyVYKt6yu2tjaDDVfpnoNQ2Enu_fhNRwkS0XBTHP5cMJOkj2srmRGRblzrwaq7_06N5-HnR1NEzqb0N7jzR33WMJsJSvwnxL_Lgm7ewwVZzMFZO3W3NhUCq9DZyUQfGbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  رهبر انقلاب: جمهوری اسلامی دفاع از مجاهدان لبنان را به عنوان سیاست راهبردی خود تعیین کرده است
🔹
اکنون که حزب‌الله لبنان به‌عنوان پیش‌گام گروه‌های جهادی در برابر هجوم سَبُعانۀ رژیم صهیونیستی و حامیانش، چون صخره‌ای ستبر ایستاده است، این پایداری پیامی الهام‌بخش…</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/452748" target="_blank">📅 20:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452747">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‌ پاسخ رهبر معظم انقلاب به نامه دبیرکل و رزمندگان حزب‌الله: پایداری در راه مقاومت، نصرت الهی را در پی دارد
🔹
نامه‌ی شما برادران و فرزندانم، رزمندگان مؤمن و شجاع حزب‌الله سرافراز که حامل پیام پایداری و استقامت برای اعتلای کلمة‌‌الله و باورمندی به وعده‌های…</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/452747" target="_blank">📅 20:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452746">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">📝
تا دقایقی دیگر؛ پاسخ رهبر انقلاب اسلامی به نامه بیعت دبیرکل و رزمندگان حزب‌الله لبنان منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/452746" target="_blank">📅 20:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452745">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e2d2a86a3.mp4?token=AcGj2iKieq5mHqodC4-YWplvbvmGNPQQO7PWbjyzSFBRs98LELIWEQ8LT57ikL5nXDop4c8uA8vk4qFdK6zI6b7NtKpCJFAlW-Djo3lCHgr5Tm_QQOUPPkEqWIeJSOBl7gmgWR0gQUpQSQ3GwG2gHKoEuWMhinmmczROLwEevXtDy1K7F8LbZxRCdLMafJ79y02qpQpLKeqKG7YmAVkyXdQ_oA458Kg1N46mI1LReAr875BBglbg_s5ea51uUKeXX8m0-XW46TxdRZaHJZRvZN9MSSrR185UwtBVpIovgTQOk_ANxN7N36dxRPx8cXuNTGak7QkTsr6RqHLSAjoZPiO0I5J8cWNkCPaXwhz4LtByLUO2AbOtcZ_l1BDbkkNYBhn35xYTvojpo2uXUX8I-rhM3wS1SA0lf7Cj7nGQqm_n_biu6ZaS_eqjoK0Lzh74OqXQlXIDtj1LLG10JnIUK3VJTyUhM6R6VgplkOhF_cXIq1Vuq919BuP_MtYd6uOtm67PBja3ywpY5wlbWobkDC3bUpcLiUcPPWds0nIL8yxcLiIukhycmno7ceaUSnN1vi-6ILrTghcdxr3RAwcEmytoC0eJuYbhut2r9HooBN5qYmU1GNtSUFIsQ0qw7Pf0BnM--afz54PuopTNdCqruYnNBn5XKFMF_62m8ltz9JU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e2d2a86a3.mp4?token=AcGj2iKieq5mHqodC4-YWplvbvmGNPQQO7PWbjyzSFBRs98LELIWEQ8LT57ikL5nXDop4c8uA8vk4qFdK6zI6b7NtKpCJFAlW-Djo3lCHgr5Tm_QQOUPPkEqWIeJSOBl7gmgWR0gQUpQSQ3GwG2gHKoEuWMhinmmczROLwEevXtDy1K7F8LbZxRCdLMafJ79y02qpQpLKeqKG7YmAVkyXdQ_oA458Kg1N46mI1LReAr875BBglbg_s5ea51uUKeXX8m0-XW46TxdRZaHJZRvZN9MSSrR185UwtBVpIovgTQOk_ANxN7N36dxRPx8cXuNTGak7QkTsr6RqHLSAjoZPiO0I5J8cWNkCPaXwhz4LtByLUO2AbOtcZ_l1BDbkkNYBhn35xYTvojpo2uXUX8I-rhM3wS1SA0lf7Cj7nGQqm_n_biu6ZaS_eqjoK0Lzh74OqXQlXIDtj1LLG10JnIUK3VJTyUhM6R6VgplkOhF_cXIq1Vuq919BuP_MtYd6uOtm67PBja3ywpY5wlbWobkDC3bUpcLiUcPPWds0nIL8yxcLiIukhycmno7ceaUSnN1vi-6ILrTghcdxr3RAwcEmytoC0eJuYbhut2r9HooBN5qYmU1GNtSUFIsQ0qw7Pf0BnM--afz54PuopTNdCqruYnNBn5XKFMF_62m8ltz9JU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله جوادی آملی: به جایی رسیده‌ایم که ۲ ابرقدرت به ما حمله کرده‌اند و مانده‌اند! این معجزه نیست؟ معجزه حتماً این است که یک سنگ حرف بزند؟
🔸
هیچ فکر می‌کردیم که ما دو ابرقدرت را چُماله کنیم؟ (درهم بکوبیم؟)
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/452745" target="_blank">📅 20:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452744">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jogcMKtqdC2CwwQdiY87fOv7cOHRO56csDZam4xxBczkTwtzfW7xXHJhYougdTAVF5H4wIWCMJ1H1wh3cwsrsmS0uw5wQySePTZeSuxTn-JMMj6GGIa1P01o-g81va5o3YSCYyH52iCRxDguW1EoRt3L2Uiz9qr0K7gXb7q-Yl6Mx3d3EXcU6qx9Km6lx5F4380tAqL3EukuNnIXnX84u9Iq5dEDO8cWq9r1blIjfyPN_0Cq7wcslD_J_CRArg1IWnVYDrEvon2zWIMbig0RaQt1l9Fl7wvcnloeOM-_Td1AgFEN8eSkIq7nLsUzVHZzDTwmLymiD85HBXHuROlY6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فتاح: آمریکا نتوانست حس شکست را به مردم ایران تحمیل کند
🔹
رئیس ستاد اجرایی فرمان امام: امروز قدرتمندترین ابرقدرت تاریخ با پیشرفته‌ترین تجهیزات نظامی و تسلیحاتی در برابر جمهوری اسلامی قرار گرفته اما نتوانسته به اهداف خود دست یابد. همین مسئله موجب شکسته‌شدن هیمنۀ آمریکا شده است.
🔹
امروز مردم با وجود مشاهده خرابی‌ها و آسیب‌ها، احساس شکست ندارند و این سرمایه مهمی است که باید حفظ شود.
🔹
هنر جمهوری اسلامی این است که با تکیه بر نیروی انسانی مؤمن و متحد، در برابر قدرت‌های بزرگ ایستادگی کرده است.
🔹
در منطق قرآن نیز پیروزی صرفاً به تجهیزات و امکانات وابسته نیست، بلکه ایمان، صبر و استقامت مؤمنان عامل اصلی نصرت الهی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/452744" target="_blank">📅 20:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452743">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c11c9aaf.mp4?token=pOqc6T_BRZJeRnXtS33O7Z7bvFFzswdGKBg8maCYcZmn-ruDKeShEKSn-sReKiQSuJgp9GOD7z0Blo_E3MJdFsqnsmWMz82TvVikmV2gkgVCQDYz3IuNoMb53dCtNNQgyGqqf9sfyG8HdEbgtR_tqT24Jac6xy9MEiriRe3XKVx8JZ9XKdQr-OXdfD9N-xx2g7GVuWtPtU_EHfW2sOK4KiFrJtn62-p4ZXqbz7vvg2Y4nqokgExz60KpOTV-1OV9ZGI3Wa7DjiDKt69aTprkedphVk72ask7IaA1cvk7OALu37ZQTPN3Tz3HDOFV-tCDCaTnjMssaf21SJVESmQ8Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c11c9aaf.mp4?token=pOqc6T_BRZJeRnXtS33O7Z7bvFFzswdGKBg8maCYcZmn-ruDKeShEKSn-sReKiQSuJgp9GOD7z0Blo_E3MJdFsqnsmWMz82TvVikmV2gkgVCQDYz3IuNoMb53dCtNNQgyGqqf9sfyG8HdEbgtR_tqT24Jac6xy9MEiriRe3XKVx8JZ9XKdQr-OXdfD9N-xx2g7GVuWtPtU_EHfW2sOK4KiFrJtn62-p4ZXqbz7vvg2Y4nqokgExz60KpOTV-1OV9ZGI3Wa7DjiDKt69aTprkedphVk72ask7IaA1cvk7OALu37ZQTPN3Tz3HDOFV-tCDCaTnjMssaf21SJVESmQ8Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توصیۀ تحلیلگر لبنانی به فعال سعودی: ایران را به‌دور از کینه‌توزی و تعصب تحلیل کنید، دشمن اصلی خود را بشناسید و پایگاه‌های آمریکایی را از سرزمین‌های خود برچینید
@Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/452743" target="_blank">📅 20:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452742">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faa4898b44.mp4?token=TpLFPjTS_T-32UCQU_SNdj73tpddKUFsyuj6SYtWcnurkDLxUuNXYoHbkF1H_eJr2FtUDFutcrojoyaetX7nhisj-7N8gRAzdzXHKXdt0AYQ0lRPao-h8QlKwFD2L-IvxYnuDvQucXlWe78Vc7UzedKhPLaViyNdvDUmE7Z9Wkhf6ZzUf0pOE-ZFvGmvRYiPU_d3yIufGzLQQFmP7DzyN0AKLb_eU3HuIpd3ELIQYvk0pQ7f5KXEvW1gVOoU7Pcqywx3ZvoPRgdSSfzNgF93Vs88RnBJHVV2C3rYFF-s2vr3asf3xNav312Wz0oOctaBdnxjie6brrYnzQwgBYD0mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faa4898b44.mp4?token=TpLFPjTS_T-32UCQU_SNdj73tpddKUFsyuj6SYtWcnurkDLxUuNXYoHbkF1H_eJr2FtUDFutcrojoyaetX7nhisj-7N8gRAzdzXHKXdt0AYQ0lRPao-h8QlKwFD2L-IvxYnuDvQucXlWe78Vc7UzedKhPLaViyNdvDUmE7Z9Wkhf6ZzUf0pOE-ZFvGmvRYiPU_d3yIufGzLQQFmP7DzyN0AKLb_eU3HuIpd3ELIQYvk0pQ7f5KXEvW1gVOoU7Pcqywx3ZvoPRgdSSfzNgF93Vs88RnBJHVV2C3rYFF-s2vr3asf3xNav312Wz0oOctaBdnxjie6brrYnzQwgBYD0mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه: حرف آخر حرف رهبر انقلاب است
🔹
سران قوا با جدیت به‌دنبال اجرای منویات رهبر انقلاب هستند و وظایف خود را تحت امر ولایت فقیه انجام می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/452742" target="_blank">📅 20:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452741">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">📝
تا دقایقی دیگر؛ پاسخ رهبر انقلاب اسلامی به نامه بیعت دبیرکل و رزمندگان حزب‌الله لبنان منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/452741" target="_blank">📅 20:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452740">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gifcw4Ctuyxa2PKN81Afs6bPXrgEQDmQxzFWOQGBwutYZWwOjd46eOFWD8YPqa-sb0SWkzh8YM4gJr6DXnoSfLiQPO2iyDLEeCVrlXU8vTVDWkEYSSEBH7oOvIQSVhnKygWWmvVTKSktWj9BPFCHMtqRXPcAHcpRu8QQCElV6Xa_o55eRY-WYkebu0C0LkxwhbfcKoi03ulgmH4mJpODaIdTrFMEUrEqhBBBnnjwmRtLU1-xWknvcBtz6JbajMLHfosHICtBFd8AwFEhWsDM6XkUlRWhs-waQSjoVZWWjiNRzU0t6OAFKuaBqvPIgr11nHS7XTkMPTBirEcqmg0GaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: جنگ با ایران، تک‌حزبی‌ترین جنگ تاریخ آمریکا است
🔹
خبرگزاری سی‌ان‌ان در گزارشی نوشته:  درحالی که ترامپ ده‌ها میلیارد دلار بودجۀ دیگر برای تأمین هزینه‌های جنگ با ایران درخواست کرده، دموکرات‌ها در کنگره صریحا با این موضوع مخالفت کرده‌اند.
🔹
جنگ علیه ایران اکنون به جناحی‌ترین جنگ در تاریخ آمریکا تبدیل شده و این اولین‌بار است که یک حزب همۀ درخواست‌های بودجۀ جنگی ازسوی فرمانده کل قوا را رد می‌کند.
🔸
حتی در زمان جنگ آمریکا علیه عراق که توسط بوش به‌عنوان یک رئیس‌جمهور جمهوری‌خواه فرماندهی می‌شد بیش از ۵۰ درصد دموکرات‌های سنا از جنگ پشتیبانی می‌کردند اما الان اصلا اینگونه نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/452740" target="_blank">📅 20:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452732">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QW9hKNLr9y45deE9zCiNpbM-Xoi4hvcul9mZsMgBeEqM9FFbOnzb7QqMDE7lVHCxg0XzuawrFoioV5Z1lEW2T9yh0kUGNnxhQPJ6yWPMWR_HhvKtLhJER5-lPHk0JJvaitwonwSOMvA_uIIVth9j57MdMbTxTFHdYtw6oYJM3IAcpHLoAOPR8S5Nu30SoDrO0lqMukV-qFYABUdcY62umtRQk9DTpWcdNX7gs8pBj8oP1xb0zTh03AKBNF6ySP21Erduox6xuAm18ydrU-OJTKxg7v4Ys2iA8WkU_3IBYxv0KGtfQHIwavhzuApvTbxrKduAIZb5hLcTkadRmTb5Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقلالِ تاجرنیا شفاف نیست
🔹
در حالی که مدیریت استقلال در ماه‌های اخیر بارها بر شفافیت و صداقت با هواداران تاکید کرده‌، قرار گرفتن وضعیت نماد این باشگاه در تابلوی نارنجی بازار پایه فرابورس و روند افشای اطلاعات این باشگاه، پرسش‌هایی جدی را درباره میزان پایبندی علی تاجرنیا به این شعارها ایجاد کرده است.
⏺
باشگاه استقلال به عنوان یک شرکت بورسی، مطابق مقررات بازار سرمایه موظف است اطلاعات مالی و رویدادهای بااهمیت خود را در سامانه کدال منتشر کند تا سهامداران و هواداران بتوانند از وضعیت واقعی باشگاه مطلع شوند. با این حال عملکرد این باشگاه در حوزه افشای اطلاعات طی ماه‌های گذشته با انتقادهای فراوانی روبه‌رو بوده است.
⏺
باشگاه استقلال در دوره مدیریت تاجرنیا، بعد از اعلام تغییر در ترکیب اعضای هیئت مدیره به تاریخ اول مهر ۱۴۰۴، به مدت ۸ ماه از ارائه اطلاعات مالی خودداری کرد تا اینکه صورت‌های سال مالی منتهی به تیر ۱۴۰۴ به عجیب‌ترین حالت ممکن و در دقیقه ۹۰ مهلت معین بارگذاری شد. اسنادی که ابهامات فراوانی پیرامون تایید و بررسی یک روزه آن توسط حسابرس وجود دارد و مشخص نیست آیا اگر  پای مجوز حرفه‌ای و الزام آن در میان نبود، مدیریت استقلال باز هم صورت‌های مالی سالیانه می‌کرد یا خیر.
🖥
گزارش کامل را
در فارس بخوانید
@Sportfars</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/452732" target="_blank">📅 19:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452731">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eaae38011.mp4?token=iXWTQAKuA05Qim1mSo9l_8qF5SrUXM9JqOT5IuVcXCWh2VgLDmQWZtxa_HcikLyiI0RAwLszzPXdpXJLLGEsf-maQMHzxqTxu2IeK1JkRsPyfVW0QDFXqvKQZ1SVXBS8cp9zr20ZFp0Ug0-B8UeP95DjIi5HTnqon_xhXo8PYQLRV60tJEiec2VUWwMe4-z-tmrGyCrzjiavI1ADgO6RZWnilZVJd7tjgTTIzXNJ9OeE36PD0It1FZW-bDFOYoMiJK5omlSVbyCiy7s4XTrsbBSELG4fkfc67IwRcgNI79Bg2PMGSvgDPr_-CCLAi5aY6WfEdSmzI-AZQqcWTKNS7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eaae38011.mp4?token=iXWTQAKuA05Qim1mSo9l_8qF5SrUXM9JqOT5IuVcXCWh2VgLDmQWZtxa_HcikLyiI0RAwLszzPXdpXJLLGEsf-maQMHzxqTxu2IeK1JkRsPyfVW0QDFXqvKQZ1SVXBS8cp9zr20ZFp0Ug0-B8UeP95DjIi5HTnqon_xhXo8PYQLRV60tJEiec2VUWwMe4-z-tmrGyCrzjiavI1ADgO6RZWnilZVJd7tjgTTIzXNJ9OeE36PD0It1FZW-bDFOYoMiJK5omlSVbyCiy7s4XTrsbBSELG4fkfc67IwRcgNI79Bg2PMGSvgDPr_-CCLAi5aY6WfEdSmzI-AZQqcWTKNS7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چذابه؛ گذرگاه عاشقان کربلا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/452731" target="_blank">📅 19:43 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

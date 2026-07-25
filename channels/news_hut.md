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
<img src="https://cdn4.telesco.pe/file/BC-mhdXhf2ejNninwu1tvFgBvD0nsx_gHeooRZ-GCUq-b51D7xteGBusRQoY7NZ-GAm1uVS_tvZlD19jremcmI5C_cmgv8BjGMaglf2e9jGWS3Uo8MR-x0sGxXmShgmBqrpj5feCFKiYYwnKWUwHLCt27MoEOJbnlkgPm_0rlEO9uQUsY6fu_XmRzXtSlurxkgjE1YpqprBtgXcjO3M_XiFh0gHuwV3QnIwZuwcB7QMP-AToBqPLAug2GetDhNEgelrT3r6PAAw9c6f3FfWhB0kx-x2IgeZgKRMeuTjAu75S25oFFXsxnRbLOwZ4XexJZrA5-QK6kuGEgumxy_ktuQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 150K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 11:01:25</div>
<hr>

<div class="tg-post" id="msg-68973">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=dIQj7mIsfpe9rn5KFKFpYcc51iViqR-AlrO8eNyAuFNmCx-iT7AsaNY-jm-rSS4xdXKiLW5Zns3MctgIeOjdbmhlic9Z6hNHvJldvLRpQmYbUeJlXwg8_AnnhdwzY7HNrAQGbu-mKM5f3DJbuZCWnp6NPMBKsWsnPM4UZpPXBgDFW8ntYXQeRDE9dnnGwSF8TZr_NjeL2n5H2caMrd7UiJv6dyHIJGfuwH55TiOwxobr85Ehf35saKjQzjgvEvRdsCPf7S8F-E2lnV4IZd03PCruAscpQmPZz_7tg19V015v5BLrMhbr-5VSmt0BLlQti2XV96x2gT1iT3i8q39bKDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=dIQj7mIsfpe9rn5KFKFpYcc51iViqR-AlrO8eNyAuFNmCx-iT7AsaNY-jm-rSS4xdXKiLW5Zns3MctgIeOjdbmhlic9Z6hNHvJldvLRpQmYbUeJlXwg8_AnnhdwzY7HNrAQGbu-mKM5f3DJbuZCWnp6NPMBKsWsnPM4UZpPXBgDFW8ntYXQeRDE9dnnGwSF8TZr_NjeL2n5H2caMrd7UiJv6dyHIJGfuwH55TiOwxobr85Ehf35saKjQzjgvEvRdsCPf7S8F-E2lnV4IZd03PCruAscpQmPZz_7tg19V015v5BLrMhbr-5VSmt0BLlQti2XV96x2gT1iT3i8q39bKDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از یک تحلیلگر سیاسی که زمان پهلوی هم بوده:
یه نفر نشسته بود تو کاباره داشت ویسکی میخورد.
طرف کی بود ؟ قصاب بود !
به بغل دستیش میگه ما ک اینجا نشستیم داریم ویسکی میخوریم بعد تو ببین اون بالاسری های فلان فلان شده چه کیفی میکنن و چه بساطی دارن پس.
اینطوری ناراضی بودن مردم از پهلوی!
مردم رو اینطوری ناراضی کرده بودن روشنفکرا.
بهشون گفته بودن میدونید شما خیلی بالاتر از اینها هستید.
انقلاب رو روستایی ها نکردن انقلاب رو روشنفکرا و دانشگاهی ها کردن بعد اولین ضربه رو هم خودشون خوردن.
به مردم گفتن عاای شما وضع اقتصادیتون خیلی بهتر از اینا باید باشه ببینید اون سرمایه دارها چیا دارن که این همه خورد خوراک به شما رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/news_hut/68973" target="_blank">📅 10:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68972">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=TZmpOkGjsKh-mvm2cFH34z8tpTwNssfLVJ7T5U7CVeHTY_sJ2A0h92p_SAsVcXeaOoOwwbo-V33UiPiI3JPoVD0ixsLR5MpL2HlmR2-xN-TjuHwuzE_DIPFP_Swj4uns6uYL5jYwOXolwYtdGCM5R5zUqIPsHbYK_5Jt_pZifmEJu7wrmd3iV9lhmCjZX5PjC-N8hJTE2nTWFT50b2Ou2tJ0HGfYc-QM6Cmg2PhPKy-pwv400Tisl-iG4v6HR3jL6oGMB4ArEXkdc8GJr6jGN7Y3R2-T1lusvycIr0IuCL8HlviiF0VqvHg6z2evP71sK5qGJ1_5n1dwNKEveFilHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=TZmpOkGjsKh-mvm2cFH34z8tpTwNssfLVJ7T5U7CVeHTY_sJ2A0h92p_SAsVcXeaOoOwwbo-V33UiPiI3JPoVD0ixsLR5MpL2HlmR2-xN-TjuHwuzE_DIPFP_Swj4uns6uYL5jYwOXolwYtdGCM5R5zUqIPsHbYK_5Jt_pZifmEJu7wrmd3iV9lhmCjZX5PjC-N8hJTE2nTWFT50b2Ou2tJ0HGfYc-QM6Cmg2PhPKy-pwv400Tisl-iG4v6HR3jL6oGMB4ArEXkdc8GJr6jGN7Y3R2-T1lusvycIr0IuCL8HlviiF0VqvHg6z2evP71sK5qGJ1_5n1dwNKEveFilHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره رهبری ایران:
«حالا که همه اهالی رسانه اینجا یک‌جا جمع هستند، باید بگویم که ما به دستاوردهای فوق‌العاده‌ای رسیده‌ایم که رسانه‌ها هرگز درباره‌شان حرفی نمی‌زنند؛
برای مثال، در دوران دولت من، رژیمی که زمانی قدرتمند و هراس‌انگیز بود و بی‌وقفه به آمریکا حمله می‌کرد، سرانجام سرنگون شد
رهبران پیشین آن کنار زده شدند
و اکنون توسط یک دیکتاتور گی(همجنسگرا)اداره می‌شود که با اختلافات داخلی دست‌به‌گریبان است.
با این حال، من شخصاً برای باری وایس در شبکه CBS آرزوی موفقیت دارم. او زن فوق‌العاده‌ای است.»
@News_Hut</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/news_hut/68972" target="_blank">📅 09:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68971">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=GFr1gtf-1OD5Dv07qRAZrmyfDu5yyCOHFSwzKUZPww3rCqriy3ZZmsJGhuLTSUcyxTIwbvG7qbTJZIE7sCtWFeIHx2edEHdbL7I_pmd3fW8HXH4JXU-AZk7KvCJ9tBOn581XTY-FkRAb4ainiR2uLGbWwYvvleONZsNtOEGb5hAHjdSOtfDPuYot-MpIzEfOWdsnb0gS8i1X5icOoEQGpMI6gFS155XA8mSGN9Jhf9dtQGfR59jTkviQhAAp7FVu17r8txpoNFh4RwD0hNPyCcvbYuUEXssyMdR6CMvspL-by4tKcIIIHDn8uJM2aeuBwKdrxwqJuzVEL4i12bv_cKmHsmBPwelJEM2WyKJ84SupmZ2afN_RiBUrmJs6vt7WUjbccigXf3MCRuo_uVP6HfollzU3zqERAvCkkdyr3L-OrS0igFoAlBW49WfmlRLnkS887qpqCTXPbkUhFpYxucSsM3TH6Jhn4Uawfyqroeqz72JOE--v5H6QVXSBxfjkroCcqyaedF4cnn3ErxxJ3kMmYYuhCx9r3EETb9W_RLP-9k39dEmjs23JyeB54IGG-ag6F13v6t8t8G5nk8otRGz2QTNNz3tJudsbCVV1gWiW35Nbr5IltasS64xfV4BfzB65ZNnU9koCX7YxIYGu730vAXqOWHPQq7AH555GUos" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=GFr1gtf-1OD5Dv07qRAZrmyfDu5yyCOHFSwzKUZPww3rCqriy3ZZmsJGhuLTSUcyxTIwbvG7qbTJZIE7sCtWFeIHx2edEHdbL7I_pmd3fW8HXH4JXU-AZk7KvCJ9tBOn581XTY-FkRAb4ainiR2uLGbWwYvvleONZsNtOEGb5hAHjdSOtfDPuYot-MpIzEfOWdsnb0gS8i1X5icOoEQGpMI6gFS155XA8mSGN9Jhf9dtQGfR59jTkviQhAAp7FVu17r8txpoNFh4RwD0hNPyCcvbYuUEXssyMdR6CMvspL-by4tKcIIIHDn8uJM2aeuBwKdrxwqJuzVEL4i12bv_cKmHsmBPwelJEM2WyKJ84SupmZ2afN_RiBUrmJs6vt7WUjbccigXf3MCRuo_uVP6HfollzU3zqERAvCkkdyr3L-OrS0igFoAlBW49WfmlRLnkS887qpqCTXPbkUhFpYxucSsM3TH6Jhn4Uawfyqroeqz72JOE--v5H6QVXSBxfjkroCcqyaedF4cnn3ErxxJ3kMmYYuhCx9r3EETb9W_RLP-9k39dEmjs23JyeB54IGG-ag6F13v6t8t8G5nk8otRGz2QTNNz3tJudsbCVV1gWiW35Nbr5IltasS64xfV4BfzB65ZNnU9koCX7YxIYGu730vAXqOWHPQq7AH555GUos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بررسی اهداف احتمالی حملات آمریکا توسط فاکس نیوز زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/68971" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68970">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بعد از سیزده شب، امشب جنوب آرومه و خبری از انفجار نیست، و متاسفانه این آرامش، ترسناک تره!
#hjAly‌</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68970" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68969">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9CZvSGD712qutDCEn-IWPe6A-_8f8LEDaqR-dMbb6NLy0hjLIcqjCwL-3Szo-4qBQRgMO7-dSqXtQNDq2fGI5nyYdpprxxIYMxKmxvzoSlKaJ656Vr1X3La4b76yktqXsrV7M5MhxpBA3NQheTWBFDADpRjsxNFtcVGDio09RAyUWRNEUes7hWeUFiRS0j_haXqFnLh8Xz4cMh7Tyz1F2pCh3fM4ZYB7WDMvgC9ZcuvvgqVRBAaggYce4QskGv5nJvMPEoHsMREYB-6xkas1v_UarhB2Y9VgZMHuJ8UKWV8AFfVEhe8Eyr5p8fDXfVhadrCQRtnW6_hOcdnt5qFxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه فایتوکس به نقل از مقامات اروپایی:
در اروپا این اجماع رو به افزایش است که ترامپ پیش از کاهش تنش، آن را تشدید خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68969" target="_blank">📅 03:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68968">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=Y637e86oqfy4Zqj_JBkteg6XCvO3Lomls-nOgyrqu2TbGUCYcvhFGkLHEC37Fuxblwu6sq9t8zqWRqY4Vp6TjNdrqaTBKf4yCH_vPJe1c4XwJeu4kIYQjyt1HqeYPvpt7UPPnTbnxwasLZ5I4RnIPLToxWvRQNYTdFSLplStWT9AdGQ1JDyBKWvxBUJgfIKm8dumYw_FggCdviECV0JNRuSY70Lw07J9A-nyTijSw1_BWAKTpoAxIvzS18x9bvIcQfwajSF9_v5yooLpOQEDzYxmlcBO26okmmXVAWJSoudWlo9L1wgsPrL7lMyT05ECCIlE5s3ynH19JpD2jRc4vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=Y637e86oqfy4Zqj_JBkteg6XCvO3Lomls-nOgyrqu2TbGUCYcvhFGkLHEC37Fuxblwu6sq9t8zqWRqY4Vp6TjNdrqaTBKf4yCH_vPJe1c4XwJeu4kIYQjyt1HqeYPvpt7UPPnTbnxwasLZ5I4RnIPLToxWvRQNYTdFSLplStWT9AdGQ1JDyBKWvxBUJgfIKm8dumYw_FggCdviECV0JNRuSY70Lw07J9A-nyTijSw1_BWAKTpoAxIvzS18x9bvIcQfwajSF9_v5yooLpOQEDzYxmlcBO26okmmXVAWJSoudWlo9L1wgsPrL7lMyT05ECCIlE5s3ynH19JpD2jRc4vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پدافند هوایی روسیه یک پهپاد اوکراینی را بر فراز انبار «وایلدبریز» در سن‌پترزبورگ سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68968" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68967">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g57WqUUzg8LwHxQH3VGR2fBvYfyJv_R1xsqeLQG1ucOJp-mJPk0CdZhqTxy-4Ek5-A3l5UdLGB-LLedcnfWtCcf-nY-S0QtLypTtZhIG9ip7qMLoe3u6MhtJuG9zuiYGGjGdPQO1FiNmMu9v6S5D0ftMf-1NR18dB_0YtByfeQH3ulvHx-gD3QEzGMGI4wP7199i-aIREfdUGec0DggmSpE9Jhauvmeij8awIQ_1IbPvFU5_tZTK63BxOfLYJu7pMcbbxYWXinIGkwxPrWv9RXfKV9FnbRmSu0EUVFqQYHpfqR2g2ax7LOnFKuzaLBETqsgyuW9kYm7gm_l4Zw7Z4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ارتش‌آمریکا: یک‌کشتی مرتبط با ایران که سعی در نقض محاصره دریایی داشت رو منهدم کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68967" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68966">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGpCGD5xQCsEQ4kUQ_77MIELxttBZ7uijsFU5HJ1mBe9aXNJ-Ib-RJo5zXyOAmWCMmjXsjDeEDJCNaxT9LfYriJ3GPRWROTMJk2iRUOhTFpLb75fJrIN70q2cAkzZ0YYC24AGXVTCgpRPr9YOjxmXLxiOpqhXwR7vztxXQrEzod8XA02g1GcDa80mhTqLxIwv596C8Wz1I2sZXDkZ7583uSue8xahXWaGZDZoNgvgkuFzy9zpC0rT9XL91b6uzvYqkKewcMtKLNia2RXk5O5nh6oo0vTLLiU3jqY1-LoQzfHLuI3ELB8vmKjFdHOr2SjelobZSlytsREppL7VHoR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68966" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68965">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JY2iY2032c8-Blgxzx_NC-nPqp6ZXmHRHKnRXryQ6MHMz5fBhEcKXkwx-M8WrtxsS-88dDh7_gzmmLVclC4vbf_J3cFlVH785bMsl7v4J_4l3CDFtBpN3ptvlYZPLmBjllZJYk-kjjYC_9wqk9JL8HFdO-XqbPmRcGp3huTa9H0wWb3Q7HrSCAf1bgDZ1WdZAVKmV2Gv4IE-meXpG0vtGF0V7Hc2pFTToNY_IJULnecsr2DYrv0xcuenYSu1XyVFGsS0B7ye7kUzGSrAMkcQByWOQBCcr6QuUX0DXQsWv3I_gEM1XGVUqoFmKa2xpg5yxUFy5NslM3cccsoC4Xvcog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
رکوردهایی که ترامپ تو این مدت تو مصاحبه‌هاش ثبت کرده؛
«ما ایران رو شکست دادیم.» - 106 بار
«ما ایران رو نابود کردیم.» - 95 بار
«توافق با ایران نزدیکه.» - 88 بار
«تنگه هرمز بازه.» - 75 بار
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68965" target="_blank">📅 00:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68964">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiTIvqjpeDRmUBybUp-t3ol7m0Xnx9_UTFjFt1H7_vU1LECwMRgN_cks5RgnfTWd2Rg4Fcp3-GHDe2OZn2yzfjqiUbK9wAty2iD8T1njvuchOEOpwPYsYkmrrPXcuqXscZZX2eXcv5TI3dm3J6a2l_hQPTZuinkFSzhVZcVKcoAPODrHmEwmCRKQxatVBG0RBlLB4REwYZCUjOUTwNHVGXZ4feDR2eXPXz2xUKiBniodM_dFVawFmvVqH40_J7yfOI0YKFaZrniVJHaurUaKd6PzWBLJ41y-TRKkpj9Jzu4318DDfCcAu9uN4pWKPjzlh41G3GxE-RbuBquFokD1ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
عربستان دقایقی پیش به بندر حدیده یمن حمله کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68964" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68963">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🎙
خبرنگار:
آیا شما در حال بررسی یک حمله گسترده به ایران هستید؟
🔴
🇺🇸
پرزیدنت ترامپ:
"ما آماده حمله هستیم. ما کاملا مسلح و آماده حمله هستیم. ما با آنها صحبت می‌کنیم. شاید یک نقطه عطف وجود داشته باشد یا نباشد... در حال حاضر، ما به طور جدی با آنها صحبت می‌کنیم. اما به نظر نمی‌رسد که بتوانند به آنجا برسند، شاید اکنون بتوانند."
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68963" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68962">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68962" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68958">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlVgYXdiY0BC8c6JDSHPT6dtXYLQQJ9xddJPddzDViIjbbNFWpfRGImDsLnDm2DQuA1USXQdBYX-4rcObjd9mqJ4pYWPxzNBi2TAOK7fvXSB4KQDkefavYF6KW_MZaoWezRwLjYEgfj6W2S8mmx2d6E_ubNJdZCiWmeZUeeLTg0khnS8V4CbTDeuD1K-rRtnRR0nT_2gfCUTPgh7tYh0bixWksP3EOWLQ1JVogjyT7PUk30AivvLMjl_h3fvxwDfe6yb7NB3vCwebDQtsSaXv8UGc6LooBbzUICP5XDTiDTDd_CEqBfAAkH961dWK0FXWhSCXM5hSZq0-AXej4X32w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WFrCKb0XLuf15IazFSe_y7D6vjuZSCFQ0L9yQL10xu-vkAExyH0EhVtLazHie_zhlTpkC3MMcd6NxcZMMd0ZC2dnrf01dMoQyqO9PVvAKFFvqdAKnDaD8jcr8loQIIWWU19XcAtNvTt-BqGyvrlt9EOCsIZzSByxrDLMC7OeKg2SGl2voMNcuunEQ93MXqSl4gx0h-VsiRCutfwqTQ8_m1jH4X2_IrUEQuNpaf7pul3eKNWmfxvA4lHPrcLw74PhlKf1GI1ot0j3qgalx2yRvkUmXdlsWmS1WtaIQTuxEaoj7V7iHZfCslScpp-myn4diKmbT7--OLm0tONDnZLvYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=fWHAgN6jaLCfH6C-91HtrfEsM1zEGOqk573WaKmoGYLyWy0pcWB_31pVNkLLqtbj1JLTwRJUDDfgZZA_TwN1giz0J0ryQNa6Y5Cy3DjQXS7Uxc-a9ekim-cJirCdGnUsVudHnODH2LBKH2CwovSpbTzDd9a1659o-lUDKU2iBtuL_suA9FPr5mb6omHm0q7L41Aik_NEZ_Elv1uWDeFP2brPco2cienQHLN8hVVFhQbg4UVIYA19F0cz4dARuUS6q-1a-J1BoarXIqd6OIflzGNWX3qesBGNQBgOM5NWnOSrnxcDSmWzJVPopVpj-NBt1UdFczE8d30-OIuHJhXYRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=fWHAgN6jaLCfH6C-91HtrfEsM1zEGOqk573WaKmoGYLyWy0pcWB_31pVNkLLqtbj1JLTwRJUDDfgZZA_TwN1giz0J0ryQNa6Y5Cy3DjQXS7Uxc-a9ekim-cJirCdGnUsVudHnODH2LBKH2CwovSpbTzDd9a1659o-lUDKU2iBtuL_suA9FPr5mb6omHm0q7L41Aik_NEZ_Elv1uWDeFP2brPco2cienQHLN8hVVFhQbg4UVIYA19F0cz4dARuUS6q-1a-J1BoarXIqd6OIflzGNWX3qesBGNQBgOM5NWnOSrnxcDSmWzJVPopVpj-NBt1UdFczE8d30-OIuHJhXYRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
❌
🇷🇺
یک حمله دیگر با استفاده از پهپادهای اوکراینی به مرکز لجستیکی ویلبریز (Wildberries) در شهر سن پترزبورگ، روسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68958" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68957">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=TnHD4MSGCj8UgjcUImrOx4f-AT_aV0yGMflr-X4WGouYrg9G9HSm0FtCxnPbuNhIUUS4chTIGfwiZBDEl_FkqPszvnRhyEWPMnTdKx4t8jSU5J377JtpqNyB4ZYCj5CSc60M4SK55OSZitdPt2kFilKxept7w9Tc3_OIooB1RQtSukQ1LjDHPyhcad4jz1ayhXMi029cNIB62G6Xrhp1U9atzYlN5rin1LBQxSBoo8UPUmPDrLWyc89BVqwKmM6O0W1JiU57UsE8Qrx9-zHst79fAnOsKbzfqQ5FSY6vEOnvSUsl_kH1Df274nksfJ84F-S0nmtqmW2qNfdX6dZ6hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=TnHD4MSGCj8UgjcUImrOx4f-AT_aV0yGMflr-X4WGouYrg9G9HSm0FtCxnPbuNhIUUS4chTIGfwiZBDEl_FkqPszvnRhyEWPMnTdKx4t8jSU5J377JtpqNyB4ZYCj5CSc60M4SK55OSZitdPt2kFilKxept7w9Tc3_OIooB1RQtSukQ1LjDHPyhcad4jz1ayhXMi029cNIB62G6Xrhp1U9atzYlN5rin1LBQxSBoo8UPUmPDrLWyc89BVqwKmM6O0W1JiU57UsE8Qrx9-zHst79fAnOsKbzfqQ5FSY6vEOnvSUsl_kH1Df274nksfJ84F-S0nmtqmW2qNfdX6dZ6hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ :
وقتی توی یه جنگ
داری قاطعانه برنده می‌شی
، باید چیکار کنی؟ دست از جنگ بکشی؟
ما با اختلاف زیادی
داریم این جنگ رو می‌بریم.
همین الان هم در حال مذاکره با ایرانی‌ها هستیم و اونا
آماده انجام کارهایین که قبلاً حتی حاضر نبودن بهش فکر کنن.
🎙
خبرنگار:
شما به آکسیوس گفتید در حال بررسی یک
«حمله گسترده»
به ایران هستید. نقطه‌ای که تصمیم نهایی رو می‌گیرید چیه؟
🇺🇸
ترامپ:
ما در حال مذاکره باهاشون هستیم. شاید اصلاً به اون نقطه نرسیم، شاید هم برسیم.
🎙
خبرنگار:
ایران کی بالاخره کوتاه میاد و پای میز مذاکره می‌شینه؟
🇺🇸
ترامپ:
شاید کوتاه بیان، شاید هم برن توی یه غار و همون‌جا قایم بشن.
اونا غارهای خیلی عمیقی دارن که می‌تونن توش پنهان بشن.
ایران، باورنکردنیه، ولی شروع کرد به شلیک به همه جای خاورمیانه.
اگه سلاح هسته‌ای داشت، حتماً از اون هم استفاده می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68957" target="_blank">📅 23:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68956">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=P_7xWwNzaw6cz8Ck_92kGJBu1aQfbZ4jKSKy76bO5vQ8-yDXfs6yOM1dRX41nxR1YkTckm0nv-OjgBldH0r0ucaXBq9xZS_1hTG7spwb8SWZJ3aqPLaLMXLAfzaoMYI9hjFVRkGx_QhlnrG8U7GBr_OGiNtx6_OiV-ua_-npgxy1T3EUlpsnCI2n4lG3EUhJtNtJ5H4ACRt4XD-WO-eKEVDh1T-mwmDqlmFAEw37es_BKR5NxDvWTJlrsJhzflIXrIulfHDQ9rSbtaMu-F_Qu29Ufk6OwRlo0eYsxPd_D75sL9Y2ZQwcrQNOlUO0KqSaS01PqRpHyVnFon_MW5A-fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=P_7xWwNzaw6cz8Ck_92kGJBu1aQfbZ4jKSKy76bO5vQ8-yDXfs6yOM1dRX41nxR1YkTckm0nv-OjgBldH0r0ucaXBq9xZS_1hTG7spwb8SWZJ3aqPLaLMXLAfzaoMYI9hjFVRkGx_QhlnrG8U7GBr_OGiNtx6_OiV-ua_-npgxy1T3EUlpsnCI2n4lG3EUhJtNtJ5H4ACRt4XD-WO-eKEVDh1T-mwmDqlmFAEw37es_BKR5NxDvWTJlrsJhzflIXrIulfHDQ9rSbtaMu-F_Qu29Ufk6OwRlo0eYsxPd_D75sL9Y2ZQwcrQNOlUO0KqSaS01PqRpHyVnFon_MW5A-fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
یه انگل هست که باعث اسهال شدید مردم آمریکا میشه. کی دوباره میشه کاهو خورد؟
🇺🇸
ترامپ:
نمیدونم. بهش فکر نکردم. پیتر، زیاد کاهو میخوری؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68956" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68955">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=u2ivBJJaRADSOtJ8oEaTR8UwrwcvVvi0CKzsE7RiU9T_olX-C2PG8FoiwQCuBPJa6ZwZesHgxeIDBql3ErW7RVoBT34FMGZHEns9KeWTfWCGcZqMyFq-7BKOySJ0SNutLSRo2LwGyYNAVbVXBo6Tm1TafKFhBIh-Wtqa7VrGKZb6ALFeUkZ_VuAQtf4PjSCtW5eQkwO3M8yN9tFfP6LwEYbw-NkzlDjRWpuLDps-3PgwkfFlyFVrWxHr-xf7N_Q7B0IIz_55UevTaeK7qCZg9Gf7mkBDTRUi_IRFrIEB0-2jv4U04jfjkj3inQeCS7TqPZcC7nBdzR1aMRrVLhxpWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=u2ivBJJaRADSOtJ8oEaTR8UwrwcvVvi0CKzsE7RiU9T_olX-C2PG8FoiwQCuBPJa6ZwZesHgxeIDBql3ErW7RVoBT34FMGZHEns9KeWTfWCGcZqMyFq-7BKOySJ0SNutLSRo2LwGyYNAVbVXBo6Tm1TafKFhBIh-Wtqa7VrGKZb6ALFeUkZ_VuAQtf4PjSCtW5eQkwO3M8yN9tFfP6LwEYbw-NkzlDjRWpuLDps-3PgwkfFlyFVrWxHr-xf7N_Q7B0IIz_55UevTaeK7qCZg9Gf7mkBDTRUi_IRFrIEB0-2jv4U04jfjkj3inQeCS7TqPZcC7nBdzR1aMRrVLhxpWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند. اما دو روز بعد، آن‌ها گفتند: «وای، این فوق‌العاده است.»
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68955" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68954">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=HSsKfbG6yjTEMlQvpVJ2RLO96VeCQY66FGGnc5BoEl1Yr8ASzjpLRztAHYoR1EeB-Q1wFx_Tso3CTiczZnx7-9gLn-9UF0-9IsVWVmaoVALG1kAQfPTBZsKxh0LtJac_C7psjWQyYaV_HjDYvsqoRYYHI1yEz90Wew2ZYcOrJsreGx0tcEbomtP4Y6uCVnD_Ck4--oLN5DfmUWdtsgsz2HNjJJvyDs92T-zcXoXPxJfwFPbauaZ0cl-KP4ym4RhH4LYCg1NfPdoy06s7CEhl1MsHnSFDt4z19wLT3s__kg8VLslxA-t4PIKkM6jYIY7QDQc8dHKknHgDgR_otck-wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=HSsKfbG6yjTEMlQvpVJ2RLO96VeCQY66FGGnc5BoEl1Yr8ASzjpLRztAHYoR1EeB-Q1wFx_Tso3CTiczZnx7-9gLn-9UF0-9IsVWVmaoVALG1kAQfPTBZsKxh0LtJac_C7psjWQyYaV_HjDYvsqoRYYHI1yEz90Wew2ZYcOrJsreGx0tcEbomtP4Y6uCVnD_Ck4--oLN5DfmUWdtsgsz2HNjJJvyDs92T-zcXoXPxJfwFPbauaZ0cl-KP4ym4RhH4LYCg1NfPdoy06s7CEhl1MsHnSFDt4z19wLT3s__kg8VLslxA-t4PIKkM6jYIY7QDQc8dHKknHgDgR_otck-wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همین الان هم در حال مذاکره باهاشون هستیم. به نظرم هر روز که می‌گذره،
دارن جدی‌تر می‌شن.
من معتقدم
توافق، راه عاقلانه‌تره
؛ اما کاری که الان داریم انجام میدیم،
راه ساده‌تره.
همه‌چیز آماده‌ست و هر لحظه می‌تونیم اقدام کنیم.
وقتی وارد ونزوئلا شدم، همه مخالف بودن. اما فقط دو روز بعد می‌گفتن:
«وای، فوق‌العاده بود!»
الان هم خیلی‌ها دارن همین حرف رو درباره ایران میزنن.
به نظرم،
ایرانی‌ها تا اینجای کار از همیشه جدی‌تر به نظر می‌رسن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68954" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68953">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=m2_tYk8N5ab1Ct2tFVffz85uPdj2Qyz-g9Vnwa1eZROXE-AwLAySAG6o9-wSCXCG7vUSbSqFifxKtaEZptZtZnMTafGW3XPsv49iZliZ0YNylUGLZ2VprgX1RJ7xqrFoDvvB7Gq5Jv-EHCwJ__LZdXX6xGO3tw1sAjOIGMqbTwoZujqWU5pOTFoZWM8GuUyyIkprnBOzJ-ZKHcYo9XrpHaVZ_L-qd2Rf01aP66rw8G4TSqmvV3GaKOksaAzFp5LL6qYZUN8g-e54mgGHZO4GFqtoGAS-DNqdnOY_lBTFluIN23uynwtCFBQc5aDX6IUz2KNmXb-o9Ou1VGA8aIR3yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=m2_tYk8N5ab1Ct2tFVffz85uPdj2Qyz-g9Vnwa1eZROXE-AwLAySAG6o9-wSCXCG7vUSbSqFifxKtaEZptZtZnMTafGW3XPsv49iZliZ0YNylUGLZ2VprgX1RJ7xqrFoDvvB7Gq5Jv-EHCwJ__LZdXX6xGO3tw1sAjOIGMqbTwoZujqWU5pOTFoZWM8GuUyyIkprnBOzJ-ZKHcYo9XrpHaVZ_L-qd2Rf01aP66rw8G4TSqmvV3GaKOksaAzFp5LL6qYZUN8g-e54mgGHZO4GFqtoGAS-DNqdnOY_lBTFluIN23uynwtCFBQc5aDX6IUz2KNmXb-o9Ou1VGA8aIR3yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما درباره بمباران نیروگاه‌های برق غیرنظامی و پل‌ها صحبت می‌کنید. بخش بزرگی از جهان این کار رو جنایت جنگی می‌دونه. شما هم همین نظر رو دارید؟
🇺🇸
ترامپ:
به این سؤال جواب نمیدم. شما از کدوم رسانه‌ای هستید؟
🎙
خبرنگار:
نیویورک تایمز.
🇺🇸
ترامپ:
حدسش رو زده بودم؛ نیویورک تایمزِ ورشکسته!
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68953" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68952">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEEgnEewKE4UslcEgzbabMID-mn_5eBMUY5qvQbxJiKS5oqmVotiSIdz6JpeFKdl_WbE8zmZbMt7jZMQdREe5_JVhi4dYqQ0Y9XTBJpEzA2K2hh_zrrnAU7KWiC0DwFWKJSH_7kxBG1454Mi-_NzbiLYKkS4WFmgpIh25536NNAZc9_yQwy0C0V-Vyw8q6GrpmXzYyMuWt6tEiUABIKENM748cVt0Ig7YxPC6eIswl6kq_IndBs6Fg3pJxBBsIVNb3G7AVxW2iMBr-0Ezpv6rbHiBCSzzC4ajGvdqFQXpPux6YE2mEip1o-8uPIUChf4_MXynlHzxmBQdSdSumSqYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
صداوسیما:
دشمن آمریکایی دو موشک شلیک کرد که یک نفتکش (یا تانکر) حامل گاز را هدف قرار دادند؛ شناوری که از دریای عمان می‌آمد و قصد ورود به منطقه را داشت.
نیروهای آمریکایی گمان می‌کردند که این شناور قصد حمل گاز ایران را دارد. اصابت دو موشک به آن منجر به کشته شدن دو تن از خدمه و آسیب دیدن موتور شناور و در نتیجه توقف آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68952" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68951">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⏺
ثابتی خطاب به شهریاری:
تو دیپلمات وزارت خارجه بودی چجوری شدی استاندار؟
اصلا بچه شمال شرقی، چجوری الان استاندار در شمال غرب شدی.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68951" target="_blank">📅 22:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68950">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🇺🇸
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا بر این باورند که رهبر عالی جدید ایران، آیت‌الله مجتبی خامنه‌ای، بسیار بیش از پدر و سلف خود به دستیابی به سلاح هسته‌ای تمایل دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68950" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68949">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u21hxE6TBKmi5QqsWR6ujBfbVtUfs4cORZt8lx1lNeuQnDNXmHIjfP_5n9QVYFhkOJkk2LH2WvR_heJfr0luf5pB8kJSfem8WJdodX6jMj52J8gw6HI9hWC0kwUms_88phIVVCsSTKl0eFQW1Ad__PvdSmYG6Rhs1wpaGKLFrnLKpicR1MCxmj-mXEebaNxGl-ymc1x0UL2f5wOPLluV1fBGSCjS11kGGRvGGKzqOYXQbJL9cJUDUdmnadm_zEpa_-BYq_WQKyXh-V_bnRhR-0w-IUA5OlsdRGbXAR332nqL4DZsSuEpg-6NaXLQ5qcXtqYWYMDAjwd34J5joFZuaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک‌تایمز:
رئیس‌جمهور ترامپ روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه خود دیدار کرد تا درباره تشدید حمله نظامی علیه ایران تصمیم‌گیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68949" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68948">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7Mh_vlyTE37MFQDkyfLJVwubVzlwM9u7uuXzcx9UMU6Ud8ZXyVswaKTI-EM7-z4nTve0I1TGjD3TM3SgZev_e-8-ZzgzrgPTAR04lW3r3WtCAm-bK7sbSssUH9MhnWKNLy09V-GljXz-rL9Gj9GZXr6d_BnaLJCs8Vbakn2qxb451Rtrr2lPEviX_cnN8WrdZfbAmj8jmG5s4dhQp_AvYjgSr5lcbt45PfMfh7JTyHxWQxD5aUs5RQxNpwvTkaYGNMHpQeSUL3xPMRPfMwdw_HSyolO98yAltOJ1ENgDSu4RRzuknaixBuqre_UHE1069xffQiBSK_ijFltSjQwBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68948" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68947">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c449631.mp4?token=U9Y_K_e88nQ_ZSiaf2dKFRplKIqPK0jiUvWxuvYeq__mU2XR1I3ID0z36-xzyE9iWMsI_pfZvwrbyyG5kd7iqnUXsCNnu3eREPPLUWQtESOBdVtEwrElCtDSh6XalPqa4sDTnpIDP2Nyw0NUxTbYU2lnQkz3sMCUmVc-Fxw7DkzAXJ0TTKp_bl-SUJp6kenr8agxwXkXCshiOgBXixdl8MuhqT9YfgNh3pDQJ-kaR_fPHT-htJshswuAkuFqynxEHHGUMCQNC4RuUaJ0Xq-B44U2rI5jzDYgQPpkWw_NH4odCQ0X39IWWu-CMPN83n4KuNbKIsi14YcmyNzN0w3ixw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c449631.mp4?token=U9Y_K_e88nQ_ZSiaf2dKFRplKIqPK0jiUvWxuvYeq__mU2XR1I3ID0z36-xzyE9iWMsI_pfZvwrbyyG5kd7iqnUXsCNnu3eREPPLUWQtESOBdVtEwrElCtDSh6XalPqa4sDTnpIDP2Nyw0NUxTbYU2lnQkz3sMCUmVc-Fxw7DkzAXJ0TTKp_bl-SUJp6kenr8agxwXkXCshiOgBXixdl8MuhqT9YfgNh3pDQJ-kaR_fPHT-htJshswuAkuFqynxEHHGUMCQNC4RuUaJ0Xq-B44U2rI5jzDYgQPpkWw_NH4odCQ0X39IWWu-CMPN83n4KuNbKIsi14YcmyNzN0w3ixw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
آخرین مصاحبه اکبرعبدی با گریه:
ماهی یک میلیون تومن به خانواده ها پول میدن
وقتی روغن یک میلیون و هفتصده ، این یک میلیون روغن برای چی میخوان مردم ؟ برای جق جق در خونشون میخوان که بریزن صدا نده ؟
حالا روغن خرید ؛ باهاش چی بخره که چیزی درست کنه ؟
نمیدونم این خدا هم حرف گوش نمیکنه ، من با کسی حرفی ندارم فقط از خدا میخوام به همه کمک کنه
فرقی نمیکنه فقط به ایرانی کمک کنه
به هممون کمک کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68947" target="_blank">📅 21:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68946">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNpXn-_RhbulEH-gBH3Gukv_StnQjI7WbkhoXfhX_idZkhA_yH39wKZddKz3ZQycBgVHvxi2b9Hqz-rCI9P42yl9I8PlB8fouknuJNgyJeoHJl_bvKSpMu8qQ6Se4OCEOJRpMMXZENhr4WZOoj-GTDFI9bSJDpHuWQZ9KVHRlYW-y8rMfcVILzTFizToBL_mchhv5cCSWDyOB03Em0wi42NOdKGMYgdJeOHvy_st46PW2PRm_AvYVM3ycJnun0LaOoWmMcCIeNuGhO_v6dtJAbVPavLmyZ-OyGYfmJKo_9aaklfHym4XPYitfMVlkcWoW6moMt9T9DvbT_R7xfMxCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون، در سن 66 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68946" target="_blank">📅 21:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68945">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnZTGdNnLP8UfQYOIY5sDGZdSgwsAS8lNLreJeSU890R_7wLAiZiP4Yw-aDd7MKPGIqmets7WzjFxH1Onpp1npsx_K94WffFC8qwY60odu475hxItTx1O5XTIyZ1O2fE5Juvgf_rfeU5tfTMcJSwalzjGp9x5HdZSjJ6-HjRXLMj7ThVfEn0xmD-fj5FiLizvXCLNtdCSy4Q0jmPE9M36O1BYXvOr_KAbqniurxJqine6l8Z07FX1efiY-XXe9sMKTGhXRG2y8XUdQPoLjHEHhXkouhIaQgtwl8ONc1SM0Zz3c4R4i15WR-jebkij0gFB2hrDJuwVM5QLZQFtZA-EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
علی عبدالهی فرمانده قرارگاه خاتم الانبیا:
از این به بعد به ازای هر شهیدی که از ما بگیرید یدونه امریکایی رو به درک واصل میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68945" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68944">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066d70166.mp4?token=d4mYT9k21vLbdJnfHSedmHBQNm27pIxDSgIl-m5e1_YjVnzd_gLx6rzCrunw5xHcACfFWAr8a9dHhfBiK3QXSbadQvrqLf9SlU1V4jUr91XmUhWU8UjgBjLC_Dm5UoyBjgogQIg2qP2BrAjy4fwpW1EDdhk-OomBlh-Gz27-b6q8vgMB5rZDNZYAZfAzrYn3uq4G41mRj8xDVfw9v13T94lJcSNcy6PmXxyZXKtIC3VOrr49Vl6nQGzHSGnCDT7s3KdvLgAIsP4KqqdRwZSO5tIaQGxZonoLdGGkLvwzO00DgTv8DifoprJsoVHESICcbFKDejvsGrWpMyc4klUdTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066d70166.mp4?token=d4mYT9k21vLbdJnfHSedmHBQNm27pIxDSgIl-m5e1_YjVnzd_gLx6rzCrunw5xHcACfFWAr8a9dHhfBiK3QXSbadQvrqLf9SlU1V4jUr91XmUhWU8UjgBjLC_Dm5UoyBjgogQIg2qP2BrAjy4fwpW1EDdhk-OomBlh-Gz27-b6q8vgMB5rZDNZYAZfAzrYn3uq4G41mRj8xDVfw9v13T94lJcSNcy6PmXxyZXKtIC3VOrr49Vl6nQGzHSGnCDT7s3KdvLgAIsP4KqqdRwZSO5tIaQGxZonoLdGGkLvwzO00DgTv8DifoprJsoVHESICcbFKDejvsGrWpMyc4klUdTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما از یه بازی فکری رونمایی کرده که توش باید
بچه‌های جزیره اپستین
رو نجات بدی و ببری
بیمارستان خاتم‌الانبیا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68944" target="_blank">📅 20:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68943">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2RPDkiriB_WUbRPPJcZQGtUvOsBM0WylXl_BYW8NMCdxgSDZYVfAyhVhSSkrYKAlkJOi9xOGkcOJZtngKaEAGMZqlemrkte6sJeeN518U32hkbNBibc4ipjIZyefjtVztVnET-KpKcbE7H-bcTaTWB5YepXK2jcyYLlkvLDqEGEwpwmD2WI_vZ9BDCCFOWrGBCDt9BvXukF0yON_Yc0qsFZ8MXzVDs2m7TX-ZrR168TciGGDfdA2Oac5EKAl3q9ZhjcxVZSB9aGd5vM38jaJTxj1Tcpiz85K8sIvhZRxucHJdlvdYuqRY91iBoCt369UT80nEilyAPqSgl1PFtEYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ:
رئیس‌جمهور شی در دیدار اخیرمان در پکنِ چین، به من گفت که تحت هیچ شرایطی به جمهوری اسلامی ایران سلاح نخواهد داد یا نخواهد فروخت؛ و این گفته شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، من به حرف او اعتماد دارم؛
ضمن اینکه خودم هم لطف‌های بسیار بزرگی در حق او انجام می‌دهم.
به همین ترتیب، رئیس‌جمهور پوتین نیز با وجود جنگ هولناکی که در اوکراین جریان دارد (و روابط همچنان برقرار است، همان‌طور که با رئیس‌جمهور زلنسکی نیز چنین است)، به من گفت که به ایران سلاح نخواهد فروخت.
او درک می‌کند که من به اوکراین سلاح نمی‌فروشم، بلکه به کشورهای عضو ناتو می‌فروشم. آن‌ها بهای کامل را می‌پردازند و من هیچ اطلاعی ندارم که آن سلاح‌ها چگونه توزیع می‌شوند.
بنابراین، به عقیده من، دو کشور عمده‌ای که اغلب در ارتباط با موضوع ایران از آن‌ها نام برده می‌شود، در این کار مشارکت ندارند. اگر چنین می‌کردند، برایشان بسیار بد تمام می‌شد؛ و قطعاً به نفعشان نبود.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68943" target="_blank">📅 19:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68939">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BohdNpcFEHDLtgiF77Zd0y_P-uKG_SgVzmb0jWt7-fIuIfInZyCg9v-1-Qt_nQdclGEyMiH8p5xvQSnCwr7vg5DnwOOe7Zhq0GNfK3tZkxvDfhdftX7Jg0Oc7YL4zi0X5936MZ4lCyHsqbNMUTOwMW5S2jlYBk8nkm6pJoxxC1DR8z24N06Pu061hXMW_zpCwgiXYHt2GYVekbMppXH5VKoi3U1EfWfWD1iyvbl7NqYpP67yYo-yGnSer1hcB22ZUdCAnW0rkgbgAruX1Qrc5FqT5RDokfbVpN6SUsZPe-jme49vsg_3Qf-9b34EvXnfIyV3ZOn7KjHVXBf4TYCN5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aYXKLhzNkBrgoZZCKmio6fvj-Y8l70W8Cy5mBW4hujzD7hopl1RyQ8zq_N9Qf28Bwem49Dsj_ZzSxZh2LbzeGad7OahnkoA-oM1IkcDu5Mq6NpS-RRjx-9GeozkUY6RzMqtG_2Gd7X5MSAHPLtT5OrKeIEwY5uJclwv7iMdNnyC8I1exK9glZ4OASidvipoZkRq4U9wqmUqwrYPiCq3LRAnz_hMJoOIybbommhh2A2-3-J6-qI_Uq4-Iu_L0MJoNwz5K4FJ0wYDs2BCIR1q9hzyP0kD78yJ38ujSbZCyTDW1w5hySZsDA3NeP6LmPv_G41H4XCobj7auC334uFnVwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d-e7s_oqzMpRSJx0yNYDL_KOGbYRHJl47Ayu5o135dtT0Ejf1Bl2Hu445h11tKqNR2QaD2N5_Wq4OQTguYnYpszvvxasj0CVCOIylp4U3bN-9-n6PyNREYyL2SOrZywSwFT3pH5Y8tU7OqYIVlsQXeKvteJhG4tmPnIBBzLg6qiadz477Vlm3IqZJEnvHc4qjeDJOIXY8hyoGTjYeBOk-Gtfc-X23ns-cSQhghGIUZtBiI9GasDUgqOTHNDZie_Z7NXC52T-wAgib6MT_Gtn43QMdW0drD69Sv_qmgt-pjn4xM3htVJn_KRbITklBA3WuuH3_px0Hz9YYV2WxLx4lA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=sNIGGzvHjwqF9K8jf4aAY36yBbcXLPCS7UZsGU1rPVPh5u4XbugFTXlSKfmU7e6FvzK4eEZQ2VnUM6800TKtPsF0weR3YcMQ2HeUKhD9hrgl8vARDa3Eu-QVtkBFxc6PiZoyz-lTW3TAhtiL4YsHv6rAWG-y4vBs2SSndJg1AKLuL3s2pzHsoQyCinE4yX1rtsUnJokbU9dvZsss9tppzW0P1Igfjea1m1U2w2bN6XWgkXusVjRaxkIEksDZ0pVzlwQXRg7zrYIKsOKKnE7r5y7MhfT0PlEViJxfwWOz5yyoCk1mDlllOzsl1AR8ZfBvoiMnXbQEftSEujpwJnnIpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=sNIGGzvHjwqF9K8jf4aAY36yBbcXLPCS7UZsGU1rPVPh5u4XbugFTXlSKfmU7e6FvzK4eEZQ2VnUM6800TKtPsF0weR3YcMQ2HeUKhD9hrgl8vARDa3Eu-QVtkBFxc6PiZoyz-lTW3TAhtiL4YsHv6rAWG-y4vBs2SSndJg1AKLuL3s2pzHsoQyCinE4yX1rtsUnJokbU9dvZsss9tppzW0P1Igfjea1m1U2w2bN6XWgkXusVjRaxkIEksDZ0pVzlwQXRg7zrYIKsOKKnE7r5y7MhfT0PlEViJxfwWOz5yyoCk1mDlllOzsl1AR8ZfBvoiMnXbQEftSEujpwJnnIpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ویدیو ای از بمب‌افکن(B-1 Lancer)که گفته میشه در حملات شب های گذشته علیه اهداف نظامی در خاک ایران شرکت داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68939" target="_blank">📅 19:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68938">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=Vnl4TS2pQodfoVkymFX7mqG_fzGX7VHJmMlznV13NI8yNI4Y7TOm3e4f9_fIuDx_VMOcqZGqx4SJqFv1e5k6mXhrE-65B9Cm8sNzEN0eVDyfTxeJSToaT6CgPQZHQPy9cltIPx5BCOnEhwmfmbInQt9zE_skQujoUfHE2bMkeX_F-06rvJTD8iwqid90OLSyALVy7kmmIXoEPIxpCPvss9nwjYZd0vNZFwGw1QFLzprBS4b8U3n5bjuzzdGP-l5cu1pqa0m8Le5DZEHa1R_1-DgvVaJcJ5fEpRlCkTXpsHrZXyKuJacj2HLOYkt5ib2hsaO3iwmS2lf9zPr0rNEc3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=Vnl4TS2pQodfoVkymFX7mqG_fzGX7VHJmMlznV13NI8yNI4Y7TOm3e4f9_fIuDx_VMOcqZGqx4SJqFv1e5k6mXhrE-65B9Cm8sNzEN0eVDyfTxeJSToaT6CgPQZHQPy9cltIPx5BCOnEhwmfmbInQt9zE_skQujoUfHE2bMkeX_F-06rvJTD8iwqid90OLSyALVy7kmmIXoEPIxpCPvss9nwjYZd0vNZFwGw1QFLzprBS4b8U3n5bjuzzdGP-l5cu1pqa0m8Le5DZEHa1R_1-DgvVaJcJ5fEpRlCkTXpsHrZXyKuJacj2HLOYkt5ib2hsaO3iwmS2lf9zPr0rNEc3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
در هفته‌های اخیر، آشیانه خصوصی وابسته به سپاه در جزیره خارک هدف حمله قرار گرفت. در این حمله، چهار فروند بالگرد آگوستا وستلند AW109E که توسط شرکت خصوصی بالگردی خلیج فارس بهره‌برداری می‌شدند، منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68938" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68937">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEZ82PqCAF4RNKh18RXaVEZeGKnZ2U4ccFZX_K-79RwlZ5yKolNZJef3zpqbcS_m1af6TLmAJ8qbkDUYIRcqtBw3Ft50LFGl9YDO7V2TrxrtjaEIKrnknWep3CGEKMyyBRk-Ln3xlxBi0lcyw19_6lf1DWA1v_4Zv-yOEyBPsSHxLvs8LfyaEaBtFQWZOFCvdMXnE63MWeZ2pd2_TGAmhFnoeE7vIozFoZChRywdh1sA0Jr2PPu_S2MiNdxC-WRitQtfnW5VP8A3h9R4gh8kdf6FZrNJ-32JVGHoh3adj4nrdkT-rJCrxD-t_LK4M43IqrBdrEDDJk4kea4xM7d8tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رئیس‌جمهور ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68937" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887792c366.mp4?token=S6bbXlU28kKB01ZfqIF3sZ3fvkQMv0qUVnhXJVEpGdbsx8Ue6B3VzN8CHW9JiKwkBMnAEvO0ZGfBJ5nxcEM4eRcqyrN62nEs2eTeXwSyvaCbwjy0n2pIDAi9xGvpja60nKD9Ixomv3NDxUjJOYt_nyYizATIU9DfdzjMGesMMITJD3u-6UUPzNlmcJTfzVNRXBe7BwbUo7w99V5yXJZmpxeAjo9_pVm3edmEM9wn_2vTw2F1pbmcP1wEdXnJ6DEOLzr9kFpGqI43jAw56DTFiO_VIj5d8cot4yifYs3P2yiMTZZVcyUsMuqW81PedVLaYufpdmazy44TfJsPaDvQOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887792c366.mp4?token=S6bbXlU28kKB01ZfqIF3sZ3fvkQMv0qUVnhXJVEpGdbsx8Ue6B3VzN8CHW9JiKwkBMnAEvO0ZGfBJ5nxcEM4eRcqyrN62nEs2eTeXwSyvaCbwjy0n2pIDAi9xGvpja60nKD9Ixomv3NDxUjJOYt_nyYizATIU9DfdzjMGesMMITJD3u-6UUPzNlmcJTfzVNRXBe7BwbUo7w99V5yXJZmpxeAjo9_pVm3edmEM9wn_2vTw2F1pbmcP1wEdXnJ6DEOLzr9kFpGqI43jAw56DTFiO_VIj5d8cot4yifYs3P2yiMTZZVcyUsMuqW81PedVLaYufpdmazy44TfJsPaDvQOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
❌
👑
مقایسه تسلط زبان خارجه:
وزیر امور خارجه کنونی دارای دکتری علوم سیاسی از انگلیس
با
نخست وزیر ۵۰ سال قبل ایران دارای مدرک کارشناسی علوم سیاسی از بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68936" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68935">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=gHmHnkLUVG29Q7k8G12m-pFZgzTcBDpZYsw1ctcXjHTRLg6RUNqIIlDJCN5Fz2nvUX4gSEsQCbkG4TZah6az1wrfKsDCK_ZEHVAaAhNL5uJlavkCdkew_KGQP0S4P8vW7U-yJxMycLevOUir8MjpR8z5C8u8Rx5UkyKJtGN7saoWEw5tbIvPekv80wSsfw_hCiCYHFd3ZBOcNSHZUX6LA3e8oDhQuUqes7CLNY1ZodUtEjbXjrKhIOOOkntY6b8-grp56m6vc2B4Ca0YTSqGveHqhkawp1mPS7tLNRLhXGuaCpsBmN6252zxdP1-K8bRGgbkTwle7kd9oJjPkjKzSR-fFPZ7cZT6O7-XW6NnL5aT7mvhilz2gK1C_RqNGMjyeswoxWn3insyxQ9nnFtiOc4aUjm74rYqJD634fHKyEK8no9C8O7joGh-qWoah8ZNgu3G0r2AuGPAf4EIrPMPQskjr9XxoSXS6c_ckccsGjo309InI61SX1qLiPRFMA6QxouYLZmETJGUIoc4H0lWyhw52w5V2eEaMh_DDsSALw6YBmo9uoJ9reet8JDFKCTt77LR6bWyyu2Lb62uFowNaLo9zsdsb5T74gfogTw5L236_xGlko3UmSS0Y_uve1xe60kC1H4fPvyz9HyaerhZXAKOF-i2LT4ibcRLZg1JM_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=gHmHnkLUVG29Q7k8G12m-pFZgzTcBDpZYsw1ctcXjHTRLg6RUNqIIlDJCN5Fz2nvUX4gSEsQCbkG4TZah6az1wrfKsDCK_ZEHVAaAhNL5uJlavkCdkew_KGQP0S4P8vW7U-yJxMycLevOUir8MjpR8z5C8u8Rx5UkyKJtGN7saoWEw5tbIvPekv80wSsfw_hCiCYHFd3ZBOcNSHZUX6LA3e8oDhQuUqes7CLNY1ZodUtEjbXjrKhIOOOkntY6b8-grp56m6vc2B4Ca0YTSqGveHqhkawp1mPS7tLNRLhXGuaCpsBmN6252zxdP1-K8bRGgbkTwle7kd9oJjPkjKzSR-fFPZ7cZT6O7-XW6NnL5aT7mvhilz2gK1C_RqNGMjyeswoxWn3insyxQ9nnFtiOc4aUjm74rYqJD634fHKyEK8no9C8O7joGh-qWoah8ZNgu3G0r2AuGPAf4EIrPMPQskjr9XxoSXS6c_ckccsGjo309InI61SX1qLiPRFMA6QxouYLZmETJGUIoc4H0lWyhw52w5V2eEaMh_DDsSALw6YBmo9uoJ9reet8JDFKCTt77LR6bWyyu2Lb62uFowNaLo9zsdsb5T74gfogTw5L236_xGlko3UmSS0Y_uve1xe60kC1H4fPvyz9HyaerhZXAKOF-i2LT4ibcRLZg1JM_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عباس:
چهل روز جنگ و محاصره بود هیچ کالایی کم نیومد
بله قیمت ها یکم افزایش پیدا کرد که طبیعیه
یکی از مهمون های عالی رتبه ما اومد ایران و تهران گفت من وقتی شهر دیدم تعجب کردم
گفتم این همون شهریه که جنگیده و محاصره کشیده ؟ من فک کردم الان بیام تهران شهر مفلوکیه
همه دنیا داره به ما احترام میزاره جز خودمون
من رفتم عراق حرم اونجا استقبالی که عراقی ها ازم کردن عجیب غریب بود اونم ساعت 2 شب
این استقبال از من نبود از وزیر خارجه جمهوری اسلامی اونا به من میگفتن قهرمان
عراقی ها این همه شور و شوق داشتن اونوقت صداسیما یدونشم پخش نکرد
یه نفرم اون وسط تو حرم گفت مرگ بر سازشگر
با مرگ بر عراقچی مگه مشکل حل میشه ؟ من اگه وزیرخارجه نبودم باور کن پشت لانچر بودم الان.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68935" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68934">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn5QQnV6zuTFsYpRQPS05KlYZTnBmspQVqUzM04t_aA_N-2Cg56NaNbNOzhPNrPdU2xkvgp0k8wpOuqDDc-J0XwmaknS0s9Nv-6jTUhQxuB2nwwILEDlhywbxPE2DHNfYd3A7v-Va0hMOFs-SsgeKPPrVqL0U_fHu0IZd7PHcRuEZr_xKJL51qMfRMgpqCOGFhD5vP1y_BZ9FanI83dP1-s4ARNVk_o2D_Arw4gpHYV-IAQ9YEGV8INGJd9SK_yP4AsVN8u8s9Rq6Yj3uQph4bSXkV5A9TaL6i9l7XvKjCzNvXt2GO0KEb3_YthVF_1yi6PcWXxbT-oy2SA87BxTqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8y8dSOFhGftEFtB2GkYZJSkSMbSOoffc1yMeKnwrZVB4YC-zx9S6kY4kd48NALGw_ZP4t561nDZeJcBt8kduQ2zt_L5a3DGp8k72cgQ-jjJ_lFLz4-2hpeTXjnONWXxICQiQsdvRLRZrLQ9b9f2w0KHSr6MFfxn5lQb8HeRAIwgZJSAtzAIn--Go-LJjkwOmtCna5gzgt5YDOYx5TW_UfuIeDeHr5TnCPj719EoYmhrCb4wi0sLFngfgSP1Woye5Hz4o7IFjVd1SKStUQLtjQSJ3-pMGHUKQ_YF2qN9gh5U5FOxUVLF_JjKryok0-lukT7uQV9wf-UFaLE-KpHoYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HALS0fGIfVd9PhNCGqVVmTXLUQgF3X62dxWrhnLZMq8hM3nWUjPezmmOm775PCof3EYdgt5YbZCzUnzPlajb5pjzBMGf_OYppsZ81yoBvGgqOagrKgf156ZSi100wLnmfSHHGsHRw23TyVm6rtF9ZauHdCTZnKNI6GirJduOVrXwnwcNgEqkcE3AvtHqnSbghQMHSGjOro2Ina88QjaPTpW4hdvqgBXwLYF81tc08bCZ_mBWKKaB6d-u9ptDYevCv9Lp_fppJf9--wSiIIqBPUiDpWd2_KrdoNhIbG9y-QMPunZX48d51S1ieFFD_I-tKeOvnkfu5UCvkS0iAw-E2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRJ7TTGs2Ofl8jong2j-sno1zEHUBkmLj_Gl2EPO-WxYj9RrPG9LOR5ewe0cepztxxUHGHwf-QG0Ba6a329KNdVOkcUMnEGYJhNZnktH5usS7NmgMpJRfSJRkJEw5xY0AXkThUCDk4xSQ0sJZmmBLcW0Dmm7SsB9_9C8ABIjXtyyHjWLtEj1lL1TenIaefrqC4juhpTeAT7URNk8ZqsTqjk4zrh8HFcT-yjzDw61Q_GlJmznveAi6GhtC8EtBLOClaVrmaqFCU1A1YXtn4elZSQMv_ravXg3jDCU5u-I2YIGgqDtPpBsQFWiYurVzbSlxhfyHQX-nr5fHW1vTuY7eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=PoMfqO5j-3kzg8TyBBSTL2kwQ4e5X-v1Du48cFatYAU5__MJ3zPuixctrQlcbLjo01h9F_4Y2DPnRyFfQa4zEl2-ou8e5XiMjnXIo8vppQObRTXC-C5SJhNDex9dqpETmpKceY1N87UudMUT1iT_IOVePJbzTVS4V3O2CHAnz10y332_9RuMLCuXoT275kWAQGSPEagiZZpnjbyPx8taw2NmO7B7pcsIz_u5S2iFyGVGqd2uCZP3ZA3e7v60vgcxMn8xhFbCRmVzOyOQ5FrgdA8Vcl7baU-BHHijK9icMw2xcIe0_fdcvtUNOX8T97buz_nbPvSV9CervjB1NI18vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=PoMfqO5j-3kzg8TyBBSTL2kwQ4e5X-v1Du48cFatYAU5__MJ3zPuixctrQlcbLjo01h9F_4Y2DPnRyFfQa4zEl2-ou8e5XiMjnXIo8vppQObRTXC-C5SJhNDex9dqpETmpKceY1N87UudMUT1iT_IOVePJbzTVS4V3O2CHAnz10y332_9RuMLCuXoT275kWAQGSPEagiZZpnjbyPx8taw2NmO7B7pcsIz_u5S2iFyGVGqd2uCZP3ZA3e7v60vgcxMn8xhFbCRmVzOyOQ5FrgdA8Vcl7baU-BHHijK9icMw2xcIe0_fdcvtUNOX8T97buz_nbPvSV9CervjB1NI18vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی:
کتاب نوشتم، «قدرت مذاکره». نتیجه‌اش هم داریم می‌بینیم.
همین دیشب یکی از وزرای خارجه آفریقایی به من زنگ زد و گفت میخواهیم دیپلمات‌های مان را بفرستیم ایران، برای آموزش!
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3fy9fIMDxuRpv9yRDPTzHQQ7t-MlN-PcFaW9ZWZmxLjjJKhLvLE7mO6LTs6B2o3mpcELMMdaI4spp8pgiuOTWjqCpVSo9olV7-EOx2gGMpeGLIY-824eC9wz87xSkrTo6Wl7q_67ddu2S5lzZgh4eLCN-xNL0UhoKBvOC1VSRiK1sCPal4gnEidG5DNicHBLipo4HCHV9T3UXwb4NfmEMsqqKdw1Yd34I2gAXP4ko6iO1BcaegQpHbQJ-n9phT4gVPLDc5TloB9D_tYGCzlQBvWjfl1JPez7_b-rzqfD17dhzUAHT8TAKIiv_DOUVRKpFAZ280uRWBiq_QbBscsXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu2hOnPx64uZ14BlnG_XdAIq6OuRaiFLMJeGDch5BhSLWaEfOfpfQBbmI1tdOiSCXOYWtmOMymi1gYCIEd040oT_XSlRgAnH35tquTTwk3tE7y4dfxiYo__Ff28b7hCyVNjeb_a8EkeB14sRc1euE73lEOX3Lzw_6wZgoc1HTfsyxChWEN_eX7Tp34h1sI_B8BbB7O7d1J2d3NDiVVaI4o3JNUqiTR0l-w6NZ3_bvWOjZL_SEW9s5r-l-RRlr0pimuvY-vBLMEAAzDQtqV3l6UEyBXViiZDw6mZzQeIpbKaOsLyUBfY3gkt5V8I1TFGGkADN1ztD7mai_sJJA58Fxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
جیک تورکس خبرنگار یهودی کاخ سفید:
نمی‌دانم چطور بگویم، اما من در خودِ «کاخ سفید» کار می‌کنم. از اطلاعاتی آگاهم که افراد زیادی به آن دسترسی ندارند و با اطمینان کامل به شما می‌گویم که آمریکا برنامه‌ای برای شکست دادن رژیم ایران دارد.
آن «کارشناسان» حسابی غافلگیر خواهند شد؛ هرچند بعدش وانمود می‌کنند که از همان اول هم می‌دانستند، پس... بگذریم.
به هر حال، خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68926" target="_blank">📅 12:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68925">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=EaChnUoo6Isd7r73__CLtmWSlrfe6ZEps5DsbMMJVkSL5vZzAAYqXwDQ26EtSlMlwi8toeXw1nhdmLsY_-Qh5znEyl9f9tqNx_z6nc2jMnYmcoh4qjj4faUbU5qTuylgvmjknWcD0Kma9agb9lQcYttxKo6EWRO-ouEK6js2xVjyIecAcUWPlrytsSVP51BFQ1NiJwzpDkBfUXG7LOV2l99bdtzcuXIRQU4LQ8MlP55ZfUqOV9i9N5QNQldUuYirBwLFf_H1r6RPeceFjJlr6XaJKRDZPNTGhAEt0bDGgJGu13mkYAGo1AHyGsm2tDC95d0qI5Z9HW0c7oh_BjP9tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=EaChnUoo6Isd7r73__CLtmWSlrfe6ZEps5DsbMMJVkSL5vZzAAYqXwDQ26EtSlMlwi8toeXw1nhdmLsY_-Qh5znEyl9f9tqNx_z6nc2jMnYmcoh4qjj4faUbU5qTuylgvmjknWcD0Kma9agb9lQcYttxKo6EWRO-ouEK6js2xVjyIecAcUWPlrytsSVP51BFQ1NiJwzpDkBfUXG7LOV2l99bdtzcuXIRQU4LQ8MlP55ZfUqOV9i9N5QNQldUuYirBwLFf_H1r6RPeceFjJlr6XaJKRDZPNTGhAEt0bDGgJGu13mkYAGo1AHyGsm2tDC95d0qI5Z9HW0c7oh_BjP9tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حملات ایالات متحده به ایران برای سیزدهمین شب متوالی ادامه یافت.
در این حملات، محل‌های گزارش‌شده‌ای از موشک‌ها در یزد، انبارهای سلاح در اهواز و چندین نقطه دیگر در مناطق جنوب و غرب ایران مورد هدف قرار گرفتند.
در پاسخ به این حملات، ایران صبح امروز چندین موشک را به سمت اردن، بحرین و منطقه اربیل در کردستان عراق شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68925" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68924">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=gffN4nA4NYQ_geiOs5MfbXwKoquRHt-JsOowBDGKeHMLAALrv414y9BFunBRIrOo0-johMIF4ocut5ydvG2mRRVwjl0zNqn8LkNRbP8k2aikeJXCaEAVPa1_jQ5nmG6Iik0ZRxvQXJE7WCLCutseUXeu0kuoD0Qfz3k2n86bnn9VVglcgrljvr5EuPdWwx1f8SPbn4KaE5KYTPcBx4m6ZSUwSQ8kGuk5mEXwGKRiyvybx7lnxzIVMp1sbcQvbheiqRy54xTyl6BdGRpsPg6X0SKrLsIgkfUNIwIDnLg76TsQrDRTmuXkMM9ALcpiDHKsVK1qoOCh_oOzMJxT1D8lfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=gffN4nA4NYQ_geiOs5MfbXwKoquRHt-JsOowBDGKeHMLAALrv414y9BFunBRIrOo0-johMIF4ocut5ydvG2mRRVwjl0zNqn8LkNRbP8k2aikeJXCaEAVPa1_jQ5nmG6Iik0ZRxvQXJE7WCLCutseUXeu0kuoD0Qfz3k2n86bnn9VVglcgrljvr5EuPdWwx1f8SPbn4KaE5KYTPcBx4m6ZSUwSQ8kGuk5mEXwGKRiyvybx7lnxzIVMp1sbcQvbheiqRy54xTyl6BdGRpsPg6X0SKrLsIgkfUNIwIDnLg76TsQrDRTmuXkMM9ALcpiDHKsVK1qoOCh_oOzMJxT1D8lfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به اسم ناصر نوری گوشت سگ به مردم می‌فروخته!حالا مردم متوجه شدن و مجبورش کردن خودش بشینه تمام گوشت سگ‌هایی که داشته رو بخوره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68924" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=DtZ7Gq_kjfI6lpY7Suy98XIReDKYVwgf7okSSJ1pL7S3w7RAK8tijDb1_548Xq5_4Yjy_xL0y2k04wVLLyEbbvae3xaiSSoaQAb40fXHQhWESNyc1B5QmlQDR-lYkvtviyH6YbyZMrRIAhjIr-Nc2kaAU2c2_3caLp0Ku2GWfx9JcTWMx3x7NT6LL4TYdkrJ0taYlz3vEU8SeMR6o9rxM7V52M2lBqMlayiD3mYqLrj5mB8x6-ItYhmWrZoKFjIvgL-JJHhl7NTDG3q-196JfDlSnIENkfbhVIOguwDPK7acB2Q0LauzDrES8FYic3TBxQDplO7dNJwxrcAIL0gN6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=DtZ7Gq_kjfI6lpY7Suy98XIReDKYVwgf7okSSJ1pL7S3w7RAK8tijDb1_548Xq5_4Yjy_xL0y2k04wVLLyEbbvae3xaiSSoaQAb40fXHQhWESNyc1B5QmlQDR-lYkvtviyH6YbyZMrRIAhjIr-Nc2kaAU2c2_3caLp0Ku2GWfx9JcTWMx3x7NT6LL4TYdkrJ0taYlz3vEU8SeMR6o9rxM7V52M2lBqMlayiD3mYqLrj5mB8x6-ItYhmWrZoKFjIvgL-JJHhl7NTDG3q-196JfDlSnIENkfbhVIOguwDPK7acB2Q0LauzDrES8FYic3TBxQDplO7dNJwxrcAIL0gN6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از سخنرانی ترامپ درباره ایران زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=MTwqjsuJBa2v_74dPudk5Vq3lEdiKhfgHjOaunIaCDBglrgqX7akucu0TYg3zrU5p3NX1yWA50Wls7bkJ_zDoAr-tsqhffNGS0pHQUutBfMGhmDP-WLq_tlNP6FI3knkJh4NBbF95huhRJrtpvLpgdKYG9jqLjeKCtEpZZVLBsVU1HZizfZr4BidnfZ4s6DeH1WGTljkv7x1PffXT5xbxojNICmXOuUIKuzksTdvT-UmH3MouFmm3p5YxWQX7GBtgrtHD7Do7OSYsQQgDyMeiG2DpmnacjupOGSonx0OCVyyWu9wzl2NLPxuTcE1Q2uMdjnHI4N1igCY7WuET6SWKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=MTwqjsuJBa2v_74dPudk5Vq3lEdiKhfgHjOaunIaCDBglrgqX7akucu0TYg3zrU5p3NX1yWA50Wls7bkJ_zDoAr-tsqhffNGS0pHQUutBfMGhmDP-WLq_tlNP6FI3knkJh4NBbF95huhRJrtpvLpgdKYG9jqLjeKCtEpZZVLBsVU1HZizfZr4BidnfZ4s6DeH1WGTljkv7x1PffXT5xbxojNICmXOuUIKuzksTdvT-UmH3MouFmm3p5YxWQX7GBtgrtHD7Do7OSYsQQgDyMeiG2DpmnacjupOGSonx0OCVyyWu9wzl2NLPxuTcE1Q2uMdjnHI4N1igCY7WuET6SWKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری به ثابتی:
تنگه رو بدیم بررررره؟؟؟ مگه مال ننت بوده که بدیم بره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=D8Nzzh5MWp-gB3D8bMicQzdQx6PEQ1EoH1oHMm_D1nUMTPwppwm6jo4BnzCkqm9jyUm7WRlXxxbZ1MznndfjtpAZVtwQwianKYDTCgKt6rsLtyKc6QGFgPugCA5STU6vgZcR10b7R0JLk8gAxA7SR9ZgK3LSRdYZNm4jJmRpeRQYi6Tiy-G9ieq0zrMTtjvDHlAb9rH-A5z9qUxaIhn_xWALp4biucDUu-QhM5pou6SFi3sGbyyS5S8kTnB8avvdeMa37IH-3nsj4ZqSZb4e-DK8Fd_6RV8j3JqCiOS_C_9KsxtpDxVObBmEcmwcuvzvc_9OvvWzKlyggNKFE_hgLw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=D8Nzzh5MWp-gB3D8bMicQzdQx6PEQ1EoH1oHMm_D1nUMTPwppwm6jo4BnzCkqm9jyUm7WRlXxxbZ1MznndfjtpAZVtwQwianKYDTCgKt6rsLtyKc6QGFgPugCA5STU6vgZcR10b7R0JLk8gAxA7SR9ZgK3LSRdYZNm4jJmRpeRQYi6Tiy-G9ieq0zrMTtjvDHlAb9rH-A5z9qUxaIhn_xWALp4biucDUu-QhM5pou6SFi3sGbyyS5S8kTnB8avvdeMa37IH-3nsj4ZqSZb4e-DK8Fd_6RV8j3JqCiOS_C_9KsxtpDxVObBmEcmwcuvzvc_9OvvWzKlyggNKFE_hgLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جواد اوجی وزیر نفت دولت رئیسی:
ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز را زدیم. ۵ دقیقه بعد دوستان از دیسپاچینگ گاز به بنده زنگ زدند و همین خبر را تایید کردند.
تا لباس بپوشم، موساد دوباره زنگ زد و از من پرسید ۴+۵ چند می‌شود؟ من گفتم ۹، گفت خط نهم سراسری گاز را هم منفجر کردیم. سومین خط را هم زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68921" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68920">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=qG6UTyN_M81YHqVPE_NlGQivQtb162sR-nr5HsUSxQhhZ62xI1PRCAjAN6MZSIRSH4pDRggfhriysUf4NqXNlgWfq9YHQBNGkoRAetjdIo5R1O6sFi3deT_JpP56wuLFjg1vGAS5qRtFN0h6Jua1qVzfVXzPkl7ukOrlTRjGG_D5-DfT3jOVEOK-U4nFAp-iv7H7by5JeI9PsGh25ywXhfi44QRvNHxoJMlhX0DWw-ZJEaWIWI-EULkSWGNI6Vg5sMkA8su54D2QSPFdK18S1jxpdDSlgc_CZcuFiDsnsOuWWM54Sv1dheObTMLIDRkQ1g6dF89GxqE-nSdxvqGcpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=qG6UTyN_M81YHqVPE_NlGQivQtb162sR-nr5HsUSxQhhZ62xI1PRCAjAN6MZSIRSH4pDRggfhriysUf4NqXNlgWfq9YHQBNGkoRAetjdIo5R1O6sFi3deT_JpP56wuLFjg1vGAS5qRtFN0h6Jua1qVzfVXzPkl7ukOrlTRjGG_D5-DfT3jOVEOK-U4nFAp-iv7H7by5JeI9PsGh25ywXhfi44QRvNHxoJMlhX0DWw-ZJEaWIWI-EULkSWGNI6Vg5sMkA8su54D2QSPFdK18S1jxpdDSlgc_CZcuFiDsnsOuWWM54Sv1dheObTMLIDRkQ1g6dF89GxqE-nSdxvqGcpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68918" target="_blank">📅 04:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68917">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWckFxEaVYdfqd36lYDfJGyml6QaH3MFMkEqKhh9-I0ufkz1w3NoOH5dEYgIqwwfL5kX6Zh2bQaCXcnCAgBoBS1HgySJ-utxHQ85mp-bJzf2_eiHCuqHZ5JWQ5VH5hcICfI26b57mdVvkTf9hhvQSKD6XcDZYEqwf1ck89R8F7uTWWasORFYyAIZHtwH5xlIf7FkD6UKvRJSOgS4iIYvAm0BrQ9ofR2a8miE3Fl44pB_HFO1nZD-IzYXyhmkdavfgK0hIxkkWuSDcSan2bIIPzIezNjtLVCuKlIgtBpx6OH9ES82YzKC26jVey2-khK0_glUwgLdRQWIq3etFJ9xxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la8nJkVM-wuCHHT8xB3H19YqjjzhKWTfPaU_lNBciCxArw_9ZC2lIRmslkAcp6ELoiGnDDBc0LNzDAqDix1EW-hu2kABDsx8yquJBe-kUx_HgHeNRywFs382FR8uHsY7lPvWTGkKwJVg0RL5OI4D-0gp8AM9ONGvJHXwZXVTE5zlpPMbQgPPA4UEeep0JK7lNUe7LLcByR_g7db1ZQDqzJdIz-7Fa-BROixPYtC7kkJo8a4bOMdKnLjmaxkg3e7dFgsceC-gn885Y1FGOUoaqR094tRW9XGwSni3xlZFYeDEH6ktFvsbNIQfEG6YjKymCixsWbaZjQnlh8UdEsMBwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68915" target="_blank">📅 03:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68914">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
برق مناطقی از بندرعباس قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68914" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68913">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtWDNwtu31kVZXCIbdCY1mRjbtv_-LCufgd9Uk1fX0FL80gFo9yV4qGkKcUEczs0bykWd13HAUHZOVY9PaOq1Lrj0puMP-r4xAL7WyVXLeZ1mSSJm869pZ_eSDjxwU4YfYwGcfE3YZRt4rZnUXw9h8VZrwNTHlMvPLCYHMLAIUqPyM6X8NB7jiZMXbWPvFrMbzdJ2cvqw_GK4ZXgAuuMxltoGzalwg1-Ber8GMIpYY5jKHHXOrafsdLhNR3ncCn30b5ukatNx_O5cr2_JVgtcF9PuQKpnlhYzCOeidlqr5T0gdHcNJlhJNw5NdQdfeu_KLMh5_bjJ-P1R22DTV8bUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بندرعباس؛ امشب  @News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68913" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68912">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇺🇸
منابع آمریکایی: ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68912" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68911">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=QdCZ7erDDPdduNQWUXNj4j_LWOV9MX9lMavV3N21UG70JsilJXDq1KlZqKBPzMnFTvGfYQ6yimwRGfKXcEs9rrtWV3KAavABY2X0HnI5s9VUJd5WF3NAhlfEdJ6pYNdY2FArwSddFAgOIMck8QJsZf86Ki_PYIb4GYct9hNAS7cqm6Zw9WecuBMx0ZWKQWKJ1nBEtWUDjHFfkKaZyyUi2UzT_Lj00oNx28MsO4d88Bd-PDxsTxqDZZY3GD1szZDQNhAhXt3Rh_WlBAhKqLWSxm24hiN2jkCHEVSV1UTlyCcnxMcVlT8OJlrLFuOn8S1q3WzPxBKDFNwKYexqLIL0fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=QdCZ7erDDPdduNQWUXNj4j_LWOV9MX9lMavV3N21UG70JsilJXDq1KlZqKBPzMnFTvGfYQ6yimwRGfKXcEs9rrtWV3KAavABY2X0HnI5s9VUJd5WF3NAhlfEdJ6pYNdY2FArwSddFAgOIMck8QJsZf86Ki_PYIb4GYct9hNAS7cqm6Zw9WecuBMx0ZWKQWKJ1nBEtWUDjHFfkKaZyyUi2UzT_Lj00oNx28MsO4d88Bd-PDxsTxqDZZY3GD1szZDQNhAhXt3Rh_WlBAhKqLWSxm24hiN2jkCHEVSV1UTlyCcnxMcVlT8OJlrLFuOn8S1q3WzPxBKDFNwKYexqLIL0fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بندرعباس؛ امشب
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68911" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68910">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
دقایقی پیش صدای انفجارهایی در قشم امیدیه و اندیمشک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68910" target="_blank">📅 03:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68909">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=V5PPU7bQw2Mbds88spf6Y3oiqIybDIw44UNlAxwnT6aN6vJrVkyXAjPLnoFJNTHpRb7-Iu3QMJg4a9Cllq6AP0E1YMxWF0FxoauMPIREz6SZL7ifpvaqgOBHmcPwgVcks2D-CO9A-5GsL-uPszML2x1tHxrE346zQ2zRXgM1lI_lCKiewxLZLBtyk6Ro08NSeuRl4wBlOww_eeRuzq1-JzIsBXv2yckWJfCWmepaj1jIuxa_1CIZd7N5T_7akanKQ-UOM79ZbJlmBvl_dtZS54gEEhdoWgfKRatws8TtUkzzwAJ4CHpESAM5IK6CiIunP9nYjnQJVyz8dueLpPfZEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=V5PPU7bQw2Mbds88spf6Y3oiqIybDIw44UNlAxwnT6aN6vJrVkyXAjPLnoFJNTHpRb7-Iu3QMJg4a9Cllq6AP0E1YMxWF0FxoauMPIREz6SZL7ifpvaqgOBHmcPwgVcks2D-CO9A-5GsL-uPszML2x1tHxrE346zQ2zRXgM1lI_lCKiewxLZLBtyk6Ro08NSeuRl4wBlOww_eeRuzq1-JzIsBXv2yckWJfCWmepaj1jIuxa_1CIZd7N5T_7akanKQ-UOM79ZbJlmBvl_dtZS54gEEhdoWgfKRatws8TtUkzzwAJ4CHpESAM5IK6CiIunP9nYjnQJVyz8dueLpPfZEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68909" target="_blank">📅 03:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68908">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=UfJHb7Ym4NpVt4bFKHlcvGTiICRPOZK184kTJP6MfGr8ABz-c_0KOF19QUG9Ta_bI74SWFeS1PDflGLRZgrdcqQSNdFUAcrxcbBe_2cKfL3kdPyPpLkFxHy_qfyUCQu9py-Y5lodKYeIeMsEkA65smseAFPysCtFdHFDq9rJEDpdpgxysTOVAd1ZOzSigJkYpFEjt5XjfoC3WtW1GsdjT9CCgulx28vtApjDgsBA8lbZkwtBLtk9xtjhcSB-bOfIMBjGuBsrCT73afr54Vi_DydU_9FQsmmu1uuacFfdU0k6_p9p8iQyseg711-o7wgg77OurXd3TCL0GEpnXUViNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=UfJHb7Ym4NpVt4bFKHlcvGTiICRPOZK184kTJP6MfGr8ABz-c_0KOF19QUG9Ta_bI74SWFeS1PDflGLRZgrdcqQSNdFUAcrxcbBe_2cKfL3kdPyPpLkFxHy_qfyUCQu9py-Y5lodKYeIeMsEkA65smseAFPysCtFdHFDq9rJEDpdpgxysTOVAd1ZOzSigJkYpFEjt5XjfoC3WtW1GsdjT9CCgulx28vtApjDgsBA8lbZkwtBLtk9xtjhcSB-bOfIMBjGuBsrCT73afr54Vi_DydU_9FQsmmu1uuacFfdU0k6_p9p8iQyseg711-o7wgg77OurXd3TCL0GEpnXUViNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
لحظه وقوع انفجارها در تپه الله اکبردر بندرعباس، دقایقی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68908" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68907">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUwxFQLliw5Kh0ZRk8k6oZKPjLYJPuca09UqkzSBCqBeuLMn8s6GiRBAo-PmEj3RRMo8O8r1OXeIVSS9XXNcolAap2IvEXgJ7eYXa_YvXU8j1YD6RCuA0jUt4inK_FX-LHGAQK5TOSFi79l103KqQSFj05DHm25ynypn3wf8UW_47aZS2i8UM9eU-zPFvMdg8ICxYrHJXTGD1oBvIDmCQlaPz5meLFr2Q3rBrXjYxprSKlrLcIEbgpkctkyFUIJanNMkJplDjddYM9e7Fpw77qiCbtHA2ZqwV6diqI0uJWioFLTCUc0LhvokAp1WFLzjEVp2moH7_WYyweiSm207cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68907" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68906">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی  @News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68906" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68905">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=If5R_F9N-oVV6FmSPBML8pkVYL9_rwx2vJYyBPszC5a4olPvG-Pbptk0JTU-Njd8jSJ_agcVJEix1PM9l4oe2vgImar_a3MBm7MouqzD8kELSEidgNB7VA5xFiL-0-napud5MpWk06Y6SRrwodUFiaqXvosPmWV0_7QtU7zR2p3xz-Kt2X5xWe39HXXf53W6qnJCNFrXIs2bmb9yukU7xTj-t-hU1KZg6HKeEYqZ1KVElT1IcZbZnqKCJNIsVQpl9Ur9wooLY1_TVgEH4W9IXXcSeEj32PZhJZdwRzSKJrI54zXF3k-puhaQhUHWEd2M04w5C6ssjJTkicuJM1ikJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=If5R_F9N-oVV6FmSPBML8pkVYL9_rwx2vJYyBPszC5a4olPvG-Pbptk0JTU-Njd8jSJ_agcVJEix1PM9l4oe2vgImar_a3MBm7MouqzD8kELSEidgNB7VA5xFiL-0-napud5MpWk06Y6SRrwodUFiaqXvosPmWV0_7QtU7zR2p3xz-Kt2X5xWe39HXXf53W6qnJCNFrXIs2bmb9yukU7xTj-t-hU1KZg6HKeEYqZ1KVElT1IcZbZnqKCJNIsVQpl9Ur9wooLY1_TVgEH4W9IXXcSeEj32PZhJZdwRzSKJrI54zXF3k-puhaQhUHWEd2M04w5C6ssjJTkicuJM1ikJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68905" target="_blank">📅 02:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68903">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=EWiXrd8kvMyroLDEFxISvIf9bu1FbZIp1OVL_MZywsxtyIyP-I5Y9HtE5gEn0A6d34myHOMeE5UUk6ySZWLS5fk-3WiaUfen5T0QkVUbg5OzZbwnHGINYm4RNC1ks9QnDO3IUHhRV7855FeDoDh4bEQ0HvsiF7vxVei0eOnas-Igo3UwgEOKuifwzSBxp1E5JevuxxVfLnmNxJ7kRl2Bs3vBmUdfnPgX_c1AZQMvbdj6dFgC4Hl14zj_ChHNDHEsowL9McJP13XSNDjNWLNdl07xPByeWNeSKCiBlQnlqVkOLHtAGXaiJP0rlB56MN_fRhOByRv_FU_zaPxC79zZeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=EWiXrd8kvMyroLDEFxISvIf9bu1FbZIp1OVL_MZywsxtyIyP-I5Y9HtE5gEn0A6d34myHOMeE5UUk6ySZWLS5fk-3WiaUfen5T0QkVUbg5OzZbwnHGINYm4RNC1ks9QnDO3IUHhRV7855FeDoDh4bEQ0HvsiF7vxVei0eOnas-Igo3UwgEOKuifwzSBxp1E5JevuxxVfLnmNxJ7kRl2Bs3vBmUdfnPgX_c1AZQMvbdj6dFgC4Hl14zj_ChHNDHEsowL9McJP13XSNDjNWLNdl07xPByeWNeSKCiBlQnlqVkOLHtAGXaiJP0rlB56MN_fRhOByRv_FU_zaPxC79zZeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68903" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68902">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxggBTY6ikpfjMfg7mjglRUEw__q-ZtaFYssNpcLRtrFZyI2CMyRLtnZx43Lb1eOAEz9bsAC6Qgp-qx6law1NDh37kQYqaDYvPloS07yyJOk7N4ArcZbHk1_XZkXEGNy-PxpvL--nhev4NJ5KAhbCQ3cK76A712aGPCez0C4uMCUQayB1prktGYYr5WJ6Davjgxd-2rhD69yoj8gBmc_LrR9EAWRBaNuC-CoTM2B05aqCc0yQMyegZGwb8QNKpUa6mCu-0d9YFiWN5Ms8m0snxEohD3CLmxgdKgVBSwMdRbZvNdvJ-LIauIK9HUrObY86b8bxHEzYqXe0Ck4Xeax9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی امروز ساعت ۶:۴۵ بعدازظهر (به وقت شرقی)، دور دیگری از حملات شبانه علیه اهداف نظامی ایران را آغاز کردند. این سیزدهمین شبِ پیاپیِ حملاتی است که با هدف پاسخگو کردن ایران و کاهش تهدیدات سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68902" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68901">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدیدی از حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68901" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68900">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
چندین انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68900" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68898">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=dV0fZiDDVx5a4mhnFELE68K5Ihk05VAQLA_haQ7gwRnu6vAb2WtI3GQulMp7och7V7ep6-MPw8ZADbZIvXO_1ElnOg4hx_nq2pAiUQmCMwuKqcQ_V0kz1Acqb7NsQ5wCdWo_yhzlIkG3UA5uopPFe8OmPwGLLU89c8gOXMSXFTKQ1vod5ABnQ71JElf2L2ZhIWb6v7AZUD5lcQ6DzA0pX3XMWtQyVu51nI-53kMx-tCzHO_TUaCAA8G6GtBxDmTF1MD8YJWq4h2mW93QDyn5RoxB98ua0Xu73cdyYoi4MezmQ0FVFSG8be6o4NoSynl8fCzNGMuaLkmvZ6799HCsng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=dV0fZiDDVx5a4mhnFELE68K5Ihk05VAQLA_haQ7gwRnu6vAb2WtI3GQulMp7och7V7ep6-MPw8ZADbZIvXO_1ElnOg4hx_nq2pAiUQmCMwuKqcQ_V0kz1Acqb7NsQ5wCdWo_yhzlIkG3UA5uopPFe8OmPwGLLU89c8gOXMSXFTKQ1vod5ABnQ71JElf2L2ZhIWb6v7AZUD5lcQ6DzA0pX3XMWtQyVu51nI-53kMx-tCzHO_TUaCAA8G6GtBxDmTF1MD8YJWq4h2mW93QDyn5RoxB98ua0Xu73cdyYoi4MezmQ0FVFSG8be6o4NoSynl8fCzNGMuaLkmvZ6799HCsng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران اهداف توسط ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68898" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68897">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=iRdYat0E9WZgHaYDJWJqkCWeUh7gcNxPjhrzc47VABVrt_m28chwCtBQMK6oN8XOuoONT9SPQXv-FM18LA6PbcFtDBFd9QBYy0YQapCyjmtkR2SA2BnaBpGx5QFYLaTEsSMMaZVf6-AQw-PW-s9ULqFqFwN06h5qT2JOnPlwIljLdOqT18vT7THsRw0yin1DexYo14XwWDy3HQJpnTbq2_4HdxY349oXg90eZT6y7MGZSpvA4rRHSjYl3Q6GkMREgOa7ZD9zq8ZjNr6W86nFg9qj_UhE4ghUFhRpnjTRIiUidY-ozGNBTZUE2fb6QZduJz9diCo-Od-R99MaLlywlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=iRdYat0E9WZgHaYDJWJqkCWeUh7gcNxPjhrzc47VABVrt_m28chwCtBQMK6oN8XOuoONT9SPQXv-FM18LA6PbcFtDBFd9QBYy0YQapCyjmtkR2SA2BnaBpGx5QFYLaTEsSMMaZVf6-AQw-PW-s9ULqFqFwN06h5qT2JOnPlwIljLdOqT18vT7THsRw0yin1DexYo14XwWDy3HQJpnTbq2_4HdxY349oXg90eZT6y7MGZSpvA4rRHSjYl3Q6GkMREgOa7ZD9zq8ZjNr6W86nFg9qj_UhE4ghUFhRpnjTRIiUidY-ozGNBTZUE2fb6QZduJz9diCo-Od-R99MaLlywlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین به اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68897" target="_blank">📅 02:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68896">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3266056eac.mp4?token=GeMkTD3pL2R_YZanUpg8rUiGsYz8l1Oav6pBjUSafGQy1M3xh20sRZsEmnGGGcQA7oIFSkmD1_Gq-kahysNWaROpS-NBoH1JbA9m3uGRNJ8oS8StIyDlRlgC3CUmt8QcTZd--ykPd2wYOdr0LouB0-p6iA6r31Q81YYLctfnYXWkFvhLK-IgMoUxh3sDikMMXVIbFUJFWozIWVT8KtZ93qW9rmUQiublDoqbr5uuhYHd1tbSWwkbIj0QArT2H8kiQC4apUQ-qjDipEdtxTAvxVLdBvF8h6Yos-LQACQwRS93j5Fa4cYR7MjJ6PaYDAhUa4daq1mczc3KKO3g8efUWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3266056eac.mp4?token=GeMkTD3pL2R_YZanUpg8rUiGsYz8l1Oav6pBjUSafGQy1M3xh20sRZsEmnGGGcQA7oIFSkmD1_Gq-kahysNWaROpS-NBoH1JbA9m3uGRNJ8oS8StIyDlRlgC3CUmt8QcTZd--ykPd2wYOdr0LouB0-p6iA6r31Q81YYLctfnYXWkFvhLK-IgMoUxh3sDikMMXVIbFUJFWozIWVT8KtZ93qW9rmUQiublDoqbr5uuhYHd1tbSWwkbIj0QArT2H8kiQC4apUQ-qjDipEdtxTAvxVLdBvF8h6Yos-LQACQwRS93j5Fa4cYR7MjJ6PaYDAhUa4daq1mczc3KKO3g8efUWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بمباران سنگین اهداف نظامی در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68896" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68895">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از بمباران سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68895" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68894">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
فارس:
گزارش‌های اولیه از سقوط یک هواپیما در آسمان جزیرۀ قشم حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68894" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68893">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68893" target="_blank">📅 01:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68892">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نیویورک تایمز عملاً تبدیل شده به فارس و تسنیم
😐
آخ که چقد این چپ‌ها ولدزنا و حرومی هستن
#hjAly‌</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68892" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68891">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68891" target="_blank">📅 01:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68890">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMPilfn20E3_ki06a2Ik74hvBADJGu2RDNIsL8gLXpCSbluVMW5mwB98zab82bAEtoDPqfmdMrkcx1nQvnUx2v9Krq9JDg56MnXqnOcNR8ZIEbFvQ8RcvycEwXKcHhb_p4jI0xzjPDhAEIsk8dkY79eY3g-L1oz3r8Ez8X3vuo5x--azALaP2iuPtyEVOKhfgNFZg_SITNhQfwm9tr9ifo34UQXISEecRCCpUJV1mll6wKFwQNNIc69QIKPZ9_IqrVmyUUj0BZlnrV4Keyrj9kxY9wFlhvLP8jMjZuTgKL7OO_ay3gph6-rC0UcHoD6akAHxGIDWEUmJWa4W5P4axA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:
لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد.
اگرچه ممکن است این خسارات بسیار سنگین باشد، اما با این حال، این اقدامی عادلانه و منصفانه است.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68890" target="_blank">📅 01:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68889">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=Dc2oBsNqbVx-J3Q5D7kwsdeW0513EzG332_Vrkkv9HcLn69lyeV_5d-ONbhluBWrjCpl80CMV8PLT98acd_saywA6q8yBH_WeE3kX46j8M2aK2q9h4qeclG8Fod0SGOXTkJmGT6ys1u1nf4x69RBunwUj5uL2iZT7tcraV8zT9O-_W3fWrTEGsVpAgmBpo3XVFLmbOh4agO9R7t9YnGs89BuWXhbeOYT6YfJlGp1iWfPtZFVo-AeGKpe9Y7TGozRV3pvqIpdpeyzFOkIzuU_o91NUNemlSgfalGh-60uv_Wpr85DfXg88DaFZgj_r9VyNYjNwUDs3j8TMu0sJloHKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=Dc2oBsNqbVx-J3Q5D7kwsdeW0513EzG332_Vrkkv9HcLn69lyeV_5d-ONbhluBWrjCpl80CMV8PLT98acd_saywA6q8yBH_WeE3kX46j8M2aK2q9h4qeclG8Fod0SGOXTkJmGT6ys1u1nf4x69RBunwUj5uL2iZT7tcraV8zT9O-_W3fWrTEGsVpAgmBpo3XVFLmbOh4agO9R7t9YnGs89BuWXhbeOYT6YfJlGp1iWfPtZFVo-AeGKpe9Y7TGozRV3pvqIpdpeyzFOkIzuU_o91NUNemlSgfalGh-60uv_Wpr85DfXg88DaFZgj_r9VyNYjNwUDs3j8TMu0sJloHKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
مقدار قابل توجهی از هواپیماهای باری نیروی هوایی ایالات متحده (مدل‌های C-17 و سایر هواپیماهای سنگین‌بار) امروز از اروپا به سمت خاورمیانه در حال پرواز هستند.
برای توافق دارن میان
😃
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68889" target="_blank">📅 00:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68888">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
دقایقی قبل دو فروند موشک در جریان حمله  آمریکا به محدوده روستای مسن در جزیره قشم اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68888" target="_blank">📅 00:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68887">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b133a06016.mp4?token=EKgSHH9kbThy_23-kIXOCEw2p4ooziL0chRIV02zPC00oGnb0exiWsnugnTQPmqogEypJ399-bjZ5jbaBtwEE5lG1Edr823QqNqn7z_zFbi2tv-_QUu4ONmC4vODEYrqbmAnn3Bp24ixPeQbCQPcFLLGlCoNQ3gSWRnRZzyptHj1w8VIlfRC3qwXE0ipfQ5BN8mdVJs_OF2mqyTtoSTUk2iEqh6iNn8YXrOwPhU0r_VLb4zGD-8m2qv3DmmEjVzm5MMAU9b-Rai_9KeK7SlZjNQHDY5q9BXh5yHoHwXY-qnUos-Or5con1bH5nFAKhZUashuS0qQo5tyJB7nPHFDpYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b133a06016.mp4?token=EKgSHH9kbThy_23-kIXOCEw2p4ooziL0chRIV02zPC00oGnb0exiWsnugnTQPmqogEypJ399-bjZ5jbaBtwEE5lG1Edr823QqNqn7z_zFbi2tv-_QUu4ONmC4vODEYrqbmAnn3Bp24ixPeQbCQPcFLLGlCoNQ3gSWRnRZzyptHj1w8VIlfRC3qwXE0ipfQ5BN8mdVJs_OF2mqyTtoSTUk2iEqh6iNn8YXrOwPhU0r_VLb4zGD-8m2qv3DmmEjVzm5MMAU9b-Rai_9KeK7SlZjNQHDY5q9BXh5yHoHwXY-qnUos-Or5con1bH5nFAKhZUashuS0qQo5tyJB7nPHFDpYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امشب تو میدان ازادی تهران
زیردریایی سپاه و سامانه‌ موشکی ذوالفقار بسیج
به نمایش گذاشتن
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68887" target="_blank">📅 23:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68886">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBbj56N4Nqi7VLPYNCrWXAZIKizmv13dOnrgxMH8UjH41FU7lihp9LotHgQ92mcnDrr7UyhKP0mFok-exkgSFJncGuIiRUdQqXCbdcxM7zrAm-uIB40ZwTXXg8D2CJXnj9TNVhwnsKO7JYya__DhCItF36Ou1IqYsM-86PJdrfUYP-kZokhnmd4LzXrueK9PrG95m8JJqHw0Uwu1m8LBifXA-Yf37MMYozpiLm-9cO9mSJ5lk1fGacAY6hbcc5MSzwERYXp6Kxztf75uizmJynPHtAFVQfa2QxYTObID_CxknRa_G_7mYjBxTLzUq2QhJt6fC47U_mJY-3Z2RYmISA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک دیپلمات آلمانی در گفتگو با شبکه «فایتوکس» (Faytuks) می‌گوید کارکنان سفارت این کشور در ایران خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68886" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68885">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن  @News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68885" target="_blank">📅 22:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68884">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68884" target="_blank">📅 22:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68880">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QGoKtxW0S5fxA8XL40kJuaHDkq59tUlOTjoGAuVNGyx8L0Yd5t7x5ogtJSPCsS83SnVKThHr9xFcRUzHvuIYgDS0bxqH0oEu71xGSQzt9OihdZyl3U7yu5vkkk-fD64sDCpb5y1IUHeNfcM-ppZdoFZ_7ciUGYHbCjUvMTFqiSHatRGETmoq1xJpHJJdDI2H7zhaMa2wutnbrAirbzEs9XGv1eZDscCAkDFsPL5k06QHiC3QUJYtEtSv6duiQ_HFb1ByC3ecyH1f2G8czSbXNAOfOUZELfkWbRyMNfgWYCaEfY9uCbXiV6P4bgXKNSIfcnAqcFxB001CfeptNDoPzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p9O4WWMkx7vPPZvHb4j08ICocv_74PT3-FVCkJWpwXikSBvGMA4TiSCaF4dwTDxgq8qjEQhm_04kfakrofl2A0AJ0bqyAHfwxjp3hLXqzHB9vmy7gnBWsMV190WVoVkHdjQjTLhXNZTwYrLShd72ytwDiUnGGCIdJRUrb2itg2CMZxCVL_JD9sxafLReREnkbUUHPQa3Al5a6pEv9gDq4xaHFQVMr1Y0PIPVEfh75TUPDwsYjgYEuYtweeF9bjvIxyyzqN_1x2OrYsXBfbApiK4z-bpsHix9l7gg0x_POX5aETkgGzTqtiW62IbNxxdRaGfm0iAlqlmbxqLsAx6sSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=TIrawls7nyVy-AxKLOk02KCLzM5U27yBunjGzcAFKX5rSWkFd2iuSIuhxY4qOcbIyXmHbvVkBmNweXKcX125kipcCcBOC7c1MsMXG8EOsvl71Y-rNGfPT96wkmHzOoQm1rOf1SNEYZu7eH8YxXeRGCZ3A2JrcNO44iHWJuTpVUDgVP886zYGN5SuWqD5JiHO3O1c3q8zdLffmo4Rs_rN_HJlZ-T7CAxyEU-TBeHleSzlBW9rc8yzD1sxDlDan2nt9siPpwyXXy4J0Ph3HcsuXS_kuPknFYyL-Y38T7HLSMcRNtsHWsdMQx-OXZNH3nZWmIwRT6NHtn3Hq0oJ6-Segw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=TIrawls7nyVy-AxKLOk02KCLzM5U27yBunjGzcAFKX5rSWkFd2iuSIuhxY4qOcbIyXmHbvVkBmNweXKcX125kipcCcBOC7c1MsMXG8EOsvl71Y-rNGfPT96wkmHzOoQm1rOf1SNEYZu7eH8YxXeRGCZ3A2JrcNO44iHWJuTpVUDgVP886zYGN5SuWqD5JiHO3O1c3q8zdLffmo4Rs_rN_HJlZ-T7CAxyEU-TBeHleSzlBW9rc8yzD1sxDlDan2nt9siPpwyXXy4J0Ph3HcsuXS_kuPknFYyL-Y38T7HLSMcRNtsHWsdMQx-OXZNH3nZWmIwRT6NHtn3Hq0oJ6-Segw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای تهاجمی اوکراین در یکی از بزرگترین حملات از لحاظ حجم آتش شرکت بزرگ تجارت الکترونیک روسیه، Wildberries، را هدف قرار دادند.
این تأسیسات که در شهر کراسنودار واقع شده، به‌طور کامل در آتش فرو رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68880" target="_blank">📅 22:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68879">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇺🇸
ترامپ:
کیرم
تو هرچی کمونیسته
#hjAly‌</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68879" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68878">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند  @News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68878" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68877">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68877" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68876">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">همین الانم ترامپ داره حرف می‌زنه
#hjAly‌</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68876" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68875">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اگه امروز این قطعنامه رای میاورد، ترامپ مجبور بود جنگ رو تموم کنه، یا اینکه قطعنامه رو وتو کنه! #hjAly‌</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68875" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68874">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.  اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68874" target="_blank">📅 22:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68873">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=fv9oPNEuKk-Ul5rFTfrL9dM-0V6v7iKLEG2YJLzxcEctwFGtqAqi30LBOmkhfhLeALzQUZtov8IdblrPUvJlLZBjIW_XeTDj5q9y0R10SptvtLV3srcbyq3uLaFQ5ELmUyGIulzt-S3seLsQpv3BhLKmoJ8cJ7biiN-_8VCLyM7ljNl1Me6JrNtSCZZPFVq-ddQJ5SWeeKQyNLvfbRBz_BZGQCxWczOCxIg9wja-I5phPGftX-EGiBfrLnmjY-iG3h5zsaUO35qiSYrRg_syCbTIx5vO09CKB08653Nsc1Q_OPt5iv5Tf9UetjbiVGTzJyUPHmliDJ3ajVP7quiAJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=fv9oPNEuKk-Ul5rFTfrL9dM-0V6v7iKLEG2YJLzxcEctwFGtqAqi30LBOmkhfhLeALzQUZtov8IdblrPUvJlLZBjIW_XeTDj5q9y0R10SptvtLV3srcbyq3uLaFQ5ELmUyGIulzt-S3seLsQpv3BhLKmoJ8cJ7biiN-_8VCLyM7ljNl1Me6JrNtSCZZPFVq-ddQJ5SWeeKQyNLvfbRBz_BZGQCxWczOCxIg9wja-I5phPGftX-EGiBfrLnmjY-iG3h5zsaUO35qiSYrRg_syCbTIx5vO09CKB08653Nsc1Q_OPt5iv5Tf9UetjbiVGTzJyUPHmliDJ3ajVP7quiAJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.
اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول از کنگره مجوز می‌گرفت. اما با رد شدنش، چنین محدودیتی اعمال نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68873" target="_blank">📅 22:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68871">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKjTXg9Ba3tgg42vBZAQDRRbejfFw5sVMwdgNeVi1UEVD0fmm4-mVqWfKyhXAwx3BXrqAhpk0QceuHLVXriUpdumpoWxYp_ECGpUSxPar7_y0-5y6yEUIosAQg6HczlAcuECLO-FiOX992drHzSfbVd2BDatv4Mp0RDenT9jse12HCqelgqq2ghG5oYQzMGnu2kAcJAK1ogxSm_p_e7AtHJFcDfOaegGRXc_6ZCV6iFXv544qsRsknIBp--qD77cDWIm5zd3AXPGxlnpc4ZFbtmrMRMjwSIVd_MFxkO01NBAjarTGouzeWy9pf4UHB7193Leh_mNbL77EtxuLnjYmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=qD9DFfkchW0jxmgTBzG0r5iHgTOk-SLlHzRqnwy3xcnna7YsbWkmDp4c93hwjEkxOvPu6cNcgNBlb4xM6QzVPcdfcC3eselpNacTbtGrEBMx06UUiOeBaja6K-jBzDIHomYRsQYOvB7GAkEoP2fEfrbKBLfyrMGlmzsgb1OfA_Rb8Gqm73qNoSeQVUQFljPInOP9YSQrvHhW2qhy726tdwj7q6h8PxrherE7gBKLPM862J65fw_0SmpX53gmjphjHivAnMR38ppg-DGOdg0PUq6UsO-oJbPIIEtQlAFT0kJbwojnmH3IQApmYlxOa6jAxZRhJDgA0dlRT-89kwBrkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=qD9DFfkchW0jxmgTBzG0r5iHgTOk-SLlHzRqnwy3xcnna7YsbWkmDp4c93hwjEkxOvPu6cNcgNBlb4xM6QzVPcdfcC3eselpNacTbtGrEBMx06UUiOeBaja6K-jBzDIHomYRsQYOvB7GAkEoP2fEfrbKBLfyrMGlmzsgb1OfA_Rb8Gqm73qNoSeQVUQFljPInOP9YSQrvHhW2qhy726tdwj7q6h8PxrherE7gBKLPM862J65fw_0SmpX53gmjphjHivAnMR38ppg-DGOdg0PUq6UsO-oJbPIIEtQlAFT0kJbwojnmH3IQApmYlxOa6jAxZRhJDgA0dlRT-89kwBrkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ساعاتی قبل سپاه پاسداران یک نیروگاه برق در کویت را هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68871" target="_blank">📅 21:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68870">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=FkknCCUV6kXiCIs-6Pl_j0a9KwAj-mFOohDW32h6XpCUJ2n2UblFThQUaMSA9KJNYaotylgtLjHNVHxdquPsAqDQL85YjR3Yerp8NxA7NKC8RytTehl_eI4VD9a_ODceya4W1alQx5xMzi_VLPrcuQCCDaa1LzoVBOEouHvlTFkVwFKI-_TE3CmxqS-hBE5y06uvO18pc_AbQ4iccpqSA4iOSyM2Jk92Acxah-tQ_M7U542FsiDXbsJUpKIEz3LMwC-Ikjxte5eVvI0biOErf4Q37ZF0sVeuKU33dIXcqBT65Eu9rjsrHrC_-66p5S_nrIom4JJuER1M357MXo1rdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=FkknCCUV6kXiCIs-6Pl_j0a9KwAj-mFOohDW32h6XpCUJ2n2UblFThQUaMSA9KJNYaotylgtLjHNVHxdquPsAqDQL85YjR3Yerp8NxA7NKC8RytTehl_eI4VD9a_ODceya4W1alQx5xMzi_VLPrcuQCCDaa1LzoVBOEouHvlTFkVwFKI-_TE3CmxqS-hBE5y06uvO18pc_AbQ4iccpqSA4iOSyM2Jk92Acxah-tQ_M7U542FsiDXbsJUpKIEz3LMwC-Ikjxte5eVvI0biOErf4Q37ZF0sVeuKU33dIXcqBT65Eu9rjsrHrC_-66p5S_nrIom4JJuER1M357MXo1rdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب یه دلقکی اینجوری پشت ترامپ اداشو درمیاورد که حسابی وایرال شده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68870" target="_blank">📅 20:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68869">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=YmQiEMn9nj-X2AOAahnoBRPzCtV6lBVA5xa727PY8N5ghM709Kr6_vFXdsqYyBI9_1h0tJQ5iztdv20-rGhUIOPedX3nNCOBK6Jz5OdL6LofQKXonNzTLRzLEJoVrElsjZTEupKOiuJOVdGpR0M_VSA97t-gPD8e7ICEjbJ0ZiIqOMXPb7ZC_doaNCDw7or-KXMAzH3j9Jch2sPkuuQkQXoVoHX5HnahBn6EJGoOiH6vbRYECPnKpVCMDTy52Ws3e9ZfM9GigsRm0B_hwBjjkGEzkUuLUGp3lvRsiXtdaEBXO8a7MRYWPQ9GqyRnsFiRWQpnp2TwwIRMdkN6Fbs__H8-IkelfLgFNObgqapGSoUnEKln7PuPU4ebiwhrwshGolNyMhS_hRieITgELhTXMhtJHTqeU5KJLDTxEe2JSPp5GmGy7CAXZ75hHAmyrnexsHiUEIIt4SV8VtKnUsUKcEpBQMI1QDsMfkQ1-44va8AhyPeSPlO4QN9LEVT8yxMnPGVnoFkrnY28RxINRJRd4sCGpF9ZAApivvaZwluY4SpA9MltDF7JhL4qs5dih36xrhdmtOrCLwGUQd3qT4ukkGyIKa6GcT10mPsekjDXVVGPsfmszT___d1jE-UO4CVqPud3Ck-WALGCF53CRo-ewcXPzrAFQ2pPt__ufCq6A5E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=YmQiEMn9nj-X2AOAahnoBRPzCtV6lBVA5xa727PY8N5ghM709Kr6_vFXdsqYyBI9_1h0tJQ5iztdv20-rGhUIOPedX3nNCOBK6Jz5OdL6LofQKXonNzTLRzLEJoVrElsjZTEupKOiuJOVdGpR0M_VSA97t-gPD8e7ICEjbJ0ZiIqOMXPb7ZC_doaNCDw7or-KXMAzH3j9Jch2sPkuuQkQXoVoHX5HnahBn6EJGoOiH6vbRYECPnKpVCMDTy52Ws3e9ZfM9GigsRm0B_hwBjjkGEzkUuLUGp3lvRsiXtdaEBXO8a7MRYWPQ9GqyRnsFiRWQpnp2TwwIRMdkN6Fbs__H8-IkelfLgFNObgqapGSoUnEKln7PuPU4ebiwhrwshGolNyMhS_hRieITgELhTXMhtJHTqeU5KJLDTxEe2JSPp5GmGy7CAXZ75hHAmyrnexsHiUEIIt4SV8VtKnUsUKcEpBQMI1QDsMfkQ1-44va8AhyPeSPlO4QN9LEVT8yxMnPGVnoFkrnY28RxINRJRd4sCGpF9ZAApivvaZwluY4SpA9MltDF7JhL4qs5dih36xrhdmtOrCLwGUQd3qT4ukkGyIKa6GcT10mPsekjDXVVGPsfmszT___d1jE-UO4CVqPud3Ck-WALGCF53CRo-ewcXPzrAFQ2pPt__ufCq6A5E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فاکس‌نیوز در حال بررسی فهرستی از اهداف زیرساختی احتمالی در ایران است که ممکن است مورد حمله ایالات متحده قرار گیرند؛ اینکه کدام نیروگاه‌ها ممکن است هدف قرار داده شوند؟
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68869" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68868">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuaIffL_op790hyP-KbpctSh1QJtcaVP00ijajpyL3bXaEnqFIuMv1t-2e8MBwKoLh4n9G_SW8HdU59Q3B36y0pEkbOBImbwjZ6jjW5WpxT64TftkPlGiZRNkw2nr-UmTfnBhO7uvZHn7EQ3qtYgoNP54-_KZilPN7x620G2tcey42bZ5DyY8CFHccqvto1GjNStvyy3G_0_22rT0-_14wHQt79b0ECjY5RNUPvee3rqA9-qHSSY1F46gjbkDRGqj0cDq4Ds-F3co6WSehOAlQr9fQ9hWFWWiqec3E29hyk4KwGhf5GDgv_vUHQnQymnYFEZpSJ6PCf4jnHqORzc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68868" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68867">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xpm4WywicaRpd9Dru-PZ_RAGqDtt9jkwDvBdXYPNP7DJCyBe6ipJ7iBEWP7vkDaKO8qh8Y3jPswpF7RXj9L1hCM186SdbADHNlMVpckaklMktkKFenjGJCTrYXhrAl173Jy904TpLMG8zyVG_72VOOTNUPmTP89J4wwu4Oku_Gf4Kp893fXJd-JRBzXMawdpIQ22hFVy5wFbxDW8F9ifnwEOZXoFppRyuTYvpa9DLiUKthK2it3u1vd6xE4kwCw9-EPegejE7rMUyLQqBLSSZucjP2g2w3sldRXEPx_zbZ3_Vn-2JrQP-zdZetYQDVy4nPT81N5D5Xlqw_7rScLV6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
آنها می‌خواستند ایران را تنبیه کنند. در عوض، خودشان را با نفت سه رقمی تنبیه کردند.
استراتژی ۱۰/۱۰
👏
👏
👏
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68867" target="_blank">📅 19:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68866">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=arQBBstylnJu01zD8LURjP3OjVFOgytc2Og00fn6vUtjlwqzESBdfU9jkKErCLm2LCY1QkQW1oG0mmrv_B6RksNyCKQ8uMtEaUAPw_XbNyszBNt4C7GCwpC4UG48GY6Fy4Won5YE8qXf77q8UO_ijcuLWZIJmur78yIGuHVJaYCs34nqGubIeZdWtX6gALoqPU-k9caHqitTf2wTXOqkiAHDZoR7k5y3LrvuDc1LpEKFvEsvcYgkGfAcfUeqXzhdwF17M1fSG4nGeKHGAsml07hb6O3rQQmVyyZp4e7aFBXt8FP8CtOkN-hA5F7jRni7vHVlLOVdCn_DhGhrmR-MMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=arQBBstylnJu01zD8LURjP3OjVFOgytc2Og00fn6vUtjlwqzESBdfU9jkKErCLm2LCY1QkQW1oG0mmrv_B6RksNyCKQ8uMtEaUAPw_XbNyszBNt4C7GCwpC4UG48GY6Fy4Won5YE8qXf77q8UO_ijcuLWZIJmur78yIGuHVJaYCs34nqGubIeZdWtX6gALoqPU-k9caHqitTf2wTXOqkiAHDZoR7k5y3LrvuDc1LpEKFvEsvcYgkGfAcfUeqXzhdwF17M1fSG4nGeKHGAsml07hb6O3rQQmVyyZp4e7aFBXt8FP8CtOkN-hA5F7jRni7vHVlLOVdCn_DhGhrmR-MMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العدید هم که تخلیه شده، بنظرم خودمون رو آماده کنیم... #hjAly‌</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68866" target="_blank">📅 19:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68865">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MF5YD_4kmyVHcjrvotC6cCCRfWTdDVGjp9VYy_MdA4iv9kuFt0LMmHK0WCSPvtSHJ0sCmEJw_0nGURSS_DTAka4b3LS3QWUE017XVg5C2k6VSDJtZ-rLiem7opDn2mY1suhO9v14dg4q01hm-_Hqn3qITLkKc0opfq23DW8TlNU5kdncnPOBRSWU4XoE7xr9Ip2X_QsxpUQzPDPO4X-5RQ20rX4YwhmWKgp8VE1IUQo-5_nb4ANeAVYfH6LEV47-PH6dNYYWNiPvhzGFXRU3Fjb-Y7mcMEu7a-adb2QBaGrnpGsbMOa_0byO5FbrmiDqy-UQ9HRU80JiPAZ_4PyL3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین نشونه های نزدیک بودن حمله، تخلیه پایگاه هاست</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68865" target="_blank">📅 19:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68864">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ همچنین گفت:  همه چیز برای این حمله آماده است. اگر از اسرائیل بخواهم ظرف دو دقیقه به ما ملحق میشود اما ما به هیچکس نیاز نداریم.  @News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68864" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68863">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری؛پرزیدنت ترامپ به کانال 12 اسرائیل:   من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.   @News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68863" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68862">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O79Unxxcj_M-52V-voewblwtvbwGltb1bVbmIp95q_j0BwisfRd4zC5rvq3WmrHdt_Mj4mZciy2YXgcOD_Iks9RNK1ubNzf-_n4OQVEYbvVC_zeqTG41F7IDw3uXQ-VIgtVBemXa0FTKWIrnQ9WUS9mgrVLDbGBOLB1O50r5FR4oaE5j1epgM3tRimYcWBYoGYvgekPl0vcwBqPx7yWF8fL5crtlUtwtaZdXthhgb2LHOdOCsqmb5HVDgtwehu7wa0ixb4zb-8JRR-qR3DDolNRGEubkBh3Dnttg9RzMB8SO7OFTDyy0mUBOkLuXZXreYEG5OVTdUShcLnc6REJc-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری
؛پرزیدنت ترامپ به کانال 12 اسرائیل:
من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68862" target="_blank">📅 19:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68861">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a86f5d96ba.mp4?token=H8tdC9nt9AStmOjbubxiW--cniKXcroNHePoeW2o2neeCo5dTS2UhOSWsmiLQBWFuolJ9j5EsSjlCHOVqdgWRiIeu7mR1ydLSsu-KN_wbCGPanuNbbJi2l4z0MMsqllfTkrpdYup9vgmRYbx1x-cTaQ_azPVwRjuMgDX9sea6vL7m8gz5qfcTMuuWmealfBe8ojq3kWZpu2kusTkiKXOD4hzgGn0GSA8qLqAlGs78mKVA_-lMBq-cluh7uQ5JLpiVBYMQ-iG8NZlUeF002PMivKIWBAjZjMwEk2jpWYUSlIUUeo0lduAnJBel8ffYxEpKFpll6qouTcPmfNb88LS2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a86f5d96ba.mp4?token=H8tdC9nt9AStmOjbubxiW--cniKXcroNHePoeW2o2neeCo5dTS2UhOSWsmiLQBWFuolJ9j5EsSjlCHOVqdgWRiIeu7mR1ydLSsu-KN_wbCGPanuNbbJi2l4z0MMsqllfTkrpdYup9vgmRYbx1x-cTaQ_azPVwRjuMgDX9sea6vL7m8gz5qfcTMuuWmealfBe8ojq3kWZpu2kusTkiKXOD4hzgGn0GSA8qLqAlGs78mKVA_-lMBq-cluh7uQ5JLpiVBYMQ-iG8NZlUeF002PMivKIWBAjZjMwEk2jpWYUSlIUUeo0lduAnJBel8ffYxEpKFpll6qouTcPmfNb88LS2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
من بلافاصله پس از انتخابات به دیدار ترامپ رفتم و با هفت اسلاید بزرگ به آنجا رفتم.
اسلاید اول، اسلاید دوم، اسلاید سوم، اسلاید چهارم. "این کاری است که ما انجام خواهیم داد."
نه اینکه بپرسیم "آیا به ما اجازه می‌دهید یا نه؟" بلکه من به او گفتم: "این کاری است که ما انجام خواهیم داد." و ما به اسلاید آخر رسیدیم و من گفتم: "این پیشنهادی است که به شما ارائه می‌دهم."
شما بمب‌افکن‌های B-2 دارید – این بمب‌افکن‌های بسیار بزرگ. یک مکان به نام فوردو وجود دارد. اگر لازم باشد، ما خودمان نیز علیه آن اقدام خواهیم کرد. اما بسیار موثرتر است اگر شما بیایید و به سادگی بمب‌های سنگین خود را آنجا بیندازید.
او گوش داد و در نهایت موافقت کرد. من بسیار خوشحال بودم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68861" target="_blank">📅 18:59 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

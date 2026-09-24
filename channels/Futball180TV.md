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
<img src="https://cdn5.telesco.pe/file/Ea51rqoYYKdDhSbQGqDh9u9M7e6EALwsRwsWS0-UrwH7TET7HZpN9iHY2VJzlWKBcBMpR_WvLonOZuuUSSiJ4spYe86oMqCYYhx69vL2WNQbSOVObdfjks7SAWpmUvbuJ_8UgElFj4cKEg0lrQSeSx_7H4Ku3JXvP5XCsUtPGgoziMKYAGx_gTUquQzdoR3UjyTx2FMQap5vbjBQOoaqbthsSt4TIGA10l9DVhZ_cHKE5x58Ti6gI0JjYr3__wbT8QkeL3C-eeFW30J5jnfmOQ1-qpngYgBKt70jWejVSrWX9eYM4cLtQTByMrgmc4jwKa4BBbkmHxa4I00DHhxH1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 402K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 14:17:46</div>
<hr>

<div class="tg-post" id="msg-107175">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_9fDMeU9m9MAIiDfVJZHTheArLCh0xoxAU0tQDUnMKbmbHyWZiE1IInGaMGeo6MAo99xUlA_4E53CXPGtVaL9y_scoqb4An3fAUQFgT2NGt_lyacX5u0qpFcKpo3BQ6Hsdc00IRzx8OSM-lv2CX52reRlA1Joa_E2pSZFjdBe0HVZQtYoYWK9S20YI3ztq4768KviJ8WvQqKqu-y4OQj1_1B_T2vr6tZle4TjpamTy7z684K5dlDrnVb7Dn8dfXtP3xgE6zYCXRGnIcwtDCNFLsDhB1JSfuCrAF2_wmNpV_BVpDWUA141mmZne0UO24XC1TN-MXiquUv2NfPooIVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🤩
علیرضا فغانی از استرالیا و موعود بنیادی‌فر از ایران به عنوان داور در جام‌ملت‌های آسیا قضاوت خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/Futball180TV/107175" target="_blank">📅 14:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107174">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a03c344b.mp4?token=ZTaB1tWBzbGb66SFqs-LoNK7jfhC-brqPXdzhjbSNgO0D2Lr60i6dUF3fCNcBsKfZOdIpmVvY3sm_20InAep-kozuW5bX7fh2aLsD_PTVc_fMRu6DW2Wdl54V4dme60KbaHZ8Rl0Hum6PoPiGBTMcMKUSeX9r4D9KCeXYA8ADdWvik9JM38HwnCoJd5Nh1AZB3kweTSS2Aw5KaffFkHQDs9sk7I5Coco30JpktyNdyVGpzcuTbZIs6INsg0UDFoLbtoOC_8XrES5dw84hhvSQ5yTrdlpUxrKj-VEMwtS3W3fHQrn1tHAR_NhpLgemUFOMQK-QWil3yW2_B0hAiWlpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a03c344b.mp4?token=ZTaB1tWBzbGb66SFqs-LoNK7jfhC-brqPXdzhjbSNgO0D2Lr60i6dUF3fCNcBsKfZOdIpmVvY3sm_20InAep-kozuW5bX7fh2aLsD_PTVc_fMRu6DW2Wdl54V4dme60KbaHZ8Rl0Hum6PoPiGBTMcMKUSeX9r4D9KCeXYA8ADdWvik9JM38HwnCoJd5Nh1AZB3kweTSS2Aw5KaffFkHQDs9sk7I5Coco30JpktyNdyVGpzcuTbZIs6INsg0UDFoLbtoOC_8XrES5dw84hhvSQ5yTrdlpUxrKj-VEMwtS3W3fHQrn1tHAR_NhpLgemUFOMQK-QWil3yW2_B0hAiWlpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
شاید حق با پیمان یوسفی بوده باشه
❌
🎙
پیمان یوسفی پیش از شروع لیگ برتر در برنامه تلویزیونی خطاب به سخنگوی فدراسیون فوتبال: زمین و تماشاگر که ندارید، لیگ را پلی استیشنی برگزار کنید
🎮
دیروز: قهرمانی تاریخی پلی‌استیشن بازان ایران در آسیا و حذف تیم ملی امید از مرحله گروهی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/Futball180TV/107174" target="_blank">📅 14:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107173">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383a3af1e5.mp4?token=p_vc_O3P8Ksl6I4xrTlMXQI7xeGQoO0da-LpWyuw42pXfSktrPRsHkEKvlUjZz7XN_KAvwGJOUcEwRbcRyb124bZ_BVpIrCW7AihHaZI5V98A-dNm3Phh_uWrqtg32v9qRcwVx2yhcHfuCsXphHrU7jVNsndFZJsOpJuIuape5C0xGL-Z89qu0HgO-OVBURAxYZx_vO4fVuUvFLq6CrhHN_PHMZu4gwkwk8_SbJwsANshO4H6jcBjdpa8UjWIR1rM4v-cjC5cEOFa3epnEsHQY9uiU801gFTC1ufwnjqBMI1WtVYJf8D5W9w0e-SQ8vmL6IpDM0Cc-2TKmP-hqGDpoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383a3af1e5.mp4?token=p_vc_O3P8Ksl6I4xrTlMXQI7xeGQoO0da-LpWyuw42pXfSktrPRsHkEKvlUjZz7XN_KAvwGJOUcEwRbcRyb124bZ_BVpIrCW7AihHaZI5V98A-dNm3Phh_uWrqtg32v9qRcwVx2yhcHfuCsXphHrU7jVNsndFZJsOpJuIuape5C0xGL-Z89qu0HgO-OVBURAxYZx_vO4fVuUvFLq6CrhHN_PHMZu4gwkwk8_SbJwsANshO4H6jcBjdpa8UjWIR1rM4v-cjC5cEOFa3epnEsHQY9uiU801gFTC1ufwnjqBMI1WtVYJf8D5W9w0e-SQ8vmL6IpDM0Cc-2TKmP-hqGDpoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت های جنجالی هاشم بیگ زاده درباره ستارگان تیم امید ایران؛ از انتقال به پرسپولیس، ده میلیارد هم نصیب دانیال ایری نشده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/Futball180TV/107173" target="_blank">📅 13:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107172">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
⭕️
بازگشت پرواز تهران به تاجیکستان از مرز هوایی بدلیل آغاز رسمی محاصره هوایی  «پرواز هواپیمایی وارش» از تهران به «شهر دوشنبه»؛ پایتخت تاجیکستان؛ از مرزِ هوایی لغو شد و به فرودگاه خمینی بازگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/Futball180TV/107172" target="_blank">📅 13:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107171">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5bd37ffa3.mp4?token=oraqsowHlI7xdYxR4bJe1xadZC3F-HXl1u0g2l9zzq9PAlYLSRREibXVE2u1pYUG8dxtKqtV1UTlSCSr3Pa94E1ceGnekIOyuIqrppdTYDiZB2LzTmN84hU-q0QpFXut_xH6fKc3wKX_tPQ1DQsrYusv_V4X0CpfKSDCoYVZVsRy2_IX7SGWzpQYucm8xEGZSqksVQuuF2ZUY3p7qzQn0tAl20eLO78TZ8pq2_lOglQGfY5_m95fE704OCF7aWz5kbDUX8XxugyQLjWDyRJZ8cseVzQPz3uCq8z6nl4Vugwtx-qsRm81GoInqXpXGFf_Sqz2dBn8OGw1miXoDq1Z0H4EYmmvOPkf4QnvAQX4b_PxLckAUqTyktvM6BZPAD12VxzSl4JozX_ofs1kEynjjywvjbuMTY8P7g2kyFl9FvSc9gOBlSogoCYBor_XVhLfqVxFYEqLfoQBbCQ7a5HDlEJDGDjDqhuRgbuYzjqpTZmW-zuaR2NLDzXntS5TdnOx9DL4uTXys4DyiziQbTrLBtjaS75mLOadp7tKghvx3B95b-5Q_oopXl7Qi5De0ftZ2as-CnRsvt00XofXKwZKX3g4smrwiI0lM30PqJBWBJa9Y7PPExpjiT88TjFwCl_6PfuG4XInElGM2hrdj6_YbvMwKok4zMbeKYUgXHqcf7c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5bd37ffa3.mp4?token=oraqsowHlI7xdYxR4bJe1xadZC3F-HXl1u0g2l9zzq9PAlYLSRREibXVE2u1pYUG8dxtKqtV1UTlSCSr3Pa94E1ceGnekIOyuIqrppdTYDiZB2LzTmN84hU-q0QpFXut_xH6fKc3wKX_tPQ1DQsrYusv_V4X0CpfKSDCoYVZVsRy2_IX7SGWzpQYucm8xEGZSqksVQuuF2ZUY3p7qzQn0tAl20eLO78TZ8pq2_lOglQGfY5_m95fE704OCF7aWz5kbDUX8XxugyQLjWDyRJZ8cseVzQPz3uCq8z6nl4Vugwtx-qsRm81GoInqXpXGFf_Sqz2dBn8OGw1miXoDq1Z0H4EYmmvOPkf4QnvAQX4b_PxLckAUqTyktvM6BZPAD12VxzSl4JozX_ofs1kEynjjywvjbuMTY8P7g2kyFl9FvSc9gOBlSogoCYBor_XVhLfqVxFYEqLfoQBbCQ7a5HDlEJDGDjDqhuRgbuYzjqpTZmW-zuaR2NLDzXntS5TdnOx9DL4uTXys4DyiziQbTrLBtjaS75mLOadp7tKghvx3B95b-5Q_oopXl7Qi5De0ftZ2as-CnRsvt00XofXKwZKX3g4smrwiI0lM30PqJBWBJa9Y7PPExpjiT88TjFwCl_6PfuG4XInElGM2hrdj6_YbvMwKok4zMbeKYUgXHqcf7c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
بازگشت پرواز تهران به تاجیکستان از مرز هوایی بدلیل آغاز رسمی محاصره هوایی
«پرواز هواپیمایی وارش» از تهران به «شهر دوشنبه»؛ پایتخت تاجیکستان؛ از مرزِ هوایی لغو شد و به فرودگاه خمینی بازگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/Futball180TV/107171" target="_blank">📅 13:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107170">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1178f7a6a1.mp4?token=nLERqcPp9tFoPgn2X9st_jguj_ZhMMhhAzk6qzrE0eNCmvg2p_sTzhXx8-ilk8GT9E5m0FRjubVIAyfBOuEqvrB3F90NCmqfXp81zX2V7U99JbhESCks9jlHT51SuBTVMdnMwQ4CJRA07_Fb99SsmwRaGiFbS4BUbxhpRpJ72Lh_iClQGFP2xRLBqQkdFDzPrrehpgaHKLy2ZkISKMqu6GznU1ntNYFR73ib_lsXfKvkpcbrWPAcA2TKxzeiacevZ5UsLe7LOi9Y6VAjw3lG_pcWKy_LWs-mj1J6s3U4hNu1EBuCpNyyyT2HbLrNSzYzOHSsiN2EbvFYiDZMPlHAboO6IgINvlBvF-Htu9dsk15DX9UUAnPpYqnyttdcxN7DVtXwTZKoduqcXwM1omHypeGI2PNs_D3H6B8cv4t8vrJzlmEoQkVNT0WfPNs414JCbih7JZbAmC835ltdCP1U0AGN8Rf_usNac-unStB6YDCoJ77B-L2Rkw-HeQNYD79axhNxvKZaEV0DZBYKWOYp0xV3zfbyPRy8OikVaoZ9TyolU65HPkyv6Kcv2ENYqynZrW-rKkphdRFz-QYmrvayGjysy9eg6tI_shxdGXtGyUGVR4sSf9gLIrGBLY2h0kyUipNlz48r_ylxHW0-ck4NtsGBfrk25UWwjWiCDLiJ3uE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1178f7a6a1.mp4?token=nLERqcPp9tFoPgn2X9st_jguj_ZhMMhhAzk6qzrE0eNCmvg2p_sTzhXx8-ilk8GT9E5m0FRjubVIAyfBOuEqvrB3F90NCmqfXp81zX2V7U99JbhESCks9jlHT51SuBTVMdnMwQ4CJRA07_Fb99SsmwRaGiFbS4BUbxhpRpJ72Lh_iClQGFP2xRLBqQkdFDzPrrehpgaHKLy2ZkISKMqu6GznU1ntNYFR73ib_lsXfKvkpcbrWPAcA2TKxzeiacevZ5UsLe7LOi9Y6VAjw3lG_pcWKy_LWs-mj1J6s3U4hNu1EBuCpNyyyT2HbLrNSzYzOHSsiN2EbvFYiDZMPlHAboO6IgINvlBvF-Htu9dsk15DX9UUAnPpYqnyttdcxN7DVtXwTZKoduqcXwM1omHypeGI2PNs_D3H6B8cv4t8vrJzlmEoQkVNT0WfPNs414JCbih7JZbAmC835ltdCP1U0AGN8Rf_usNac-unStB6YDCoJ77B-L2Rkw-HeQNYD79axhNxvKZaEV0DZBYKWOYp0xV3zfbyPRy8OikVaoZ9TyolU65HPkyv6Kcv2ENYqynZrW-rKkphdRFz-QYmrvayGjysy9eg6tI_shxdGXtGyUGVR4sSf9gLIrGBLY2h0kyUipNlz48r_ylxHW0-ck4NtsGBfrk25UWwjWiCDLiJ3uE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
🔸
مرگ مغزی فوتبال ایران طی دو دهه...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/Futball180TV/107170" target="_blank">📅 12:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107169">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261876d28b.mp4?token=mXWq8y58JhrKD63lXjPJPXH-Lf_yG6Xv8ZY_TMcHiUFMZum5rLqkQhBORXN0IvFNWKVDj362gP1PVxwbU1VD5zuve0xmDRctGxQ1Pudnv8u90jbotsUP8PeSz_8sZ3RSqDoZM1yztIY1YHOHYAmR4NboL6WNmoHpY0du6XUDtm9KMbyzSu2uZIGhHWboa3_aM75VS4w9X2o-gac9bcrkD8RQQ12ckGyhxoBlyQa6Ri5eKaISf_tHdsuoMJtQYy4sB-gHutZEtB1c9rHNgmgIv2c6_ozlC9FMWIipnxe2YdBLWAHg6AtfGWYMQj6LztUjHfgG6Zue36x2xKcaJc2o-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261876d28b.mp4?token=mXWq8y58JhrKD63lXjPJPXH-Lf_yG6Xv8ZY_TMcHiUFMZum5rLqkQhBORXN0IvFNWKVDj362gP1PVxwbU1VD5zuve0xmDRctGxQ1Pudnv8u90jbotsUP8PeSz_8sZ3RSqDoZM1yztIY1YHOHYAmR4NboL6WNmoHpY0du6XUDtm9KMbyzSu2uZIGhHWboa3_aM75VS4w9X2o-gac9bcrkD8RQQ12ckGyhxoBlyQa6Ri5eKaISf_tHdsuoMJtQYy4sB-gHutZEtB1c9rHNgmgIv2c6_ozlC9FMWIipnxe2YdBLWAHg6AtfGWYMQj6LztUjHfgG6Zue36x2xKcaJc2o-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
🇩🇪
هلند - آلمان⁣ امشب ساعت ۲۲:۱۵⁣
🔻
اولین تجربه یورگن کلوپ و ژاوی روی نیمکت دو رقیب سنتی⁣؛ کلوپ: شرایط هر دو تیم مثل همه اما من نسبت به ژاوی بازیکنای بیشتری رو در تیم ملی هلند میشناسم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/Futball180TV/107169" target="_blank">📅 12:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107168">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e89ae843.mp4?token=Wc3MG__VJ-YbKxdPlVj-D5WWFjqJB_9zefPT66ue4pzZKe-TY0yjSxYNBXYJOHfig8yOU9AJiJpTAqdnujI221r0SYM3oesmNvcHd0bhhxcaqHlEsmfk-87-L7T5JfTwXRf49CcvbEEBzvTWz4PHPo5c1-RokEIVf6rR1b2sniS408FzPzfTMTBoqscMAA9d75k3FStHsS2jHr38_2uvlaORTrBCNz0wT73-CegXOKwthpDlWiRQHkfYXQQ1uWSZdd1cMHSMKNcUdvAHrH4WBl50tr9mKKevT6NjSYFnOJ5l6LHPI3Sz1EgqvK_i0QOM-oPq64BIGTdNrIv-fLUNT7HOpqR9hbmUK-e7y-5NbwCDm3Ooo1wRsEG-1TYvbcHEO1J1yfg6bq4PRxCiXh5kjXAzgCmI4XGhPlaFfukPcW7wx5Dop8NufAYO24ltAH7Z0raolFDxJacVzOPPC2AcaFZa1cB83VFOr4zeHA7gglFiuD60R-Z9rUeUlMiggG1zRWF3T5I45RLoA0jXa1_A7OKwgtSy6-zHq9FOl5pulIXSQmWQsqaJXsXlHLXCTofPQslyLRcXJ4Dwf9cB6Qhlro-pMfzb2q6IAHT7iBNa1WW2f7k8_8YBQK-eHcxCWwoCBhCg7M7D-0XNXWinPTX2uM96-JKzLBGh9MKijO4ZxtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e89ae843.mp4?token=Wc3MG__VJ-YbKxdPlVj-D5WWFjqJB_9zefPT66ue4pzZKe-TY0yjSxYNBXYJOHfig8yOU9AJiJpTAqdnujI221r0SYM3oesmNvcHd0bhhxcaqHlEsmfk-87-L7T5JfTwXRf49CcvbEEBzvTWz4PHPo5c1-RokEIVf6rR1b2sniS408FzPzfTMTBoqscMAA9d75k3FStHsS2jHr38_2uvlaORTrBCNz0wT73-CegXOKwthpDlWiRQHkfYXQQ1uWSZdd1cMHSMKNcUdvAHrH4WBl50tr9mKKevT6NjSYFnOJ5l6LHPI3Sz1EgqvK_i0QOM-oPq64BIGTdNrIv-fLUNT7HOpqR9hbmUK-e7y-5NbwCDm3Ooo1wRsEG-1TYvbcHEO1J1yfg6bq4PRxCiXh5kjXAzgCmI4XGhPlaFfukPcW7wx5Dop8NufAYO24ltAH7Z0raolFDxJacVzOPPC2AcaFZa1cB83VFOr4zeHA7gglFiuD60R-Z9rUeUlMiggG1zRWF3T5I45RLoA0jXa1_A7OKwgtSy6-zHq9FOl5pulIXSQmWQsqaJXsXlHLXCTofPQslyLRcXJ4Dwf9cB6Qhlro-pMfzb2q6IAHT7iBNa1WW2f7k8_8YBQK-eHcxCWwoCBhCg7M7D-0XNXWinPTX2uM96-JKzLBGh9MKijO4ZxtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇪🇸
آنالیز ویژه برای درک قدرت بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/Futball180TV/107168" target="_blank">📅 11:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107167">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-ehimdCifZ0Ca3RR7ZxGEcX8Ade8_VhPq-NNcXgpKk1gvkrQfARLYt6AZSFRS1-q9j4pcqTivFdGJkh1ckgMhrzB0ManxTqC8MxifSTWEs4Lwi4HaJ_XuYUZBpMZ29QXrHwHwXKK_XfVD7pO8RM5l3CJ_GFB8rHVYbXhhOi_H0DAY9gqVP_IzX64Z9yl9DlhT-EdMuTbIFk0E0Z9fJH4T4ZSummVSglzDkiQiCLM1JWgZiVqJGqvWxw39-trxtxlmjU8SVXjhXt4MHvqQpHeM9G0kzVc9ySrYWvqifMdqj7TSBlemoA7GY_Px9Tjm1Tb33bQb02hSCRFx41mJ_a3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
5 بازیکن برتر از نظر تعداد گل‌ها و پاس گل در لیگ‌های معتبر اروپایی تا به امروز:
🔻
رافینیا دیاز – 17 مشارکت (گل و پاس گل).
🔻
لامین یامال – 14 مشارکت (گل و پاس گل).
🔹
کیلیان امباپه – 10 مشارکت (گل و پاس گل).
🔻
مایکل اولیسه – 8 مشارکت (گل و پاس گل).
🔺
فران تورس – 7 مشارکت (گل و پاس گل).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/107167" target="_blank">📅 11:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107166">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107166" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/Futball180TV/107166" target="_blank">📅 11:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107165">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmpyqLS2veDegP46-1rnTKlspx58bd6FkFyXyvOpPBceWM9rMVQV6qoh02XFjuh0dVgS3bd8QySgxl2463GxuO3MwmP9l_ObSPoAdNJWa8CFd8yZ0xQphadpoBYpKxzee44_Adf34OjKDisUFjEAHjZYrw-Hyvzz8omt50Tf_7tltpgW2ypjVCUqE8SVIjc9PthuYUBpIM1X-IRf3WlMmIEdBT5--RCCbx19sK4CBW2Jp3i3wqdxdM-furB4owl5VVIG4y6_uitM5Af7eJ1Hzt6JHcJZiHI1951mL3n0raptEyFXGOdJdPzA_7oa1o3rPguL_kSiiug9H1SfEKmZAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/107165" target="_blank">📅 11:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107164">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwpcrcaeaXhCrY7ipgdlHZM6VRO7V027AcXIU1GAKrk90JSTfofyVAyY0MK4hd3-PwKYAR0L6WszizBmTlw0C8y0IkOH5iuzIBMAxnwMzBdiWe7OGXFnKP8Xu4FKVmwFD4F9HwmVu2wp4uZvjss-Haw_3qi3veWuPY5okFzeG-VvF4my49TemEKJakXvjjCm4EgANWErYhHSY3q7GJTrvEwgOsWMHwxFjf8SPUgI9fmqLXXj0jCqcMzcjNjbQbMXrziyld4KrItFjzTECnmJNAxb-OceFD3MrYVseHwKQYE9u7zxv39acwrG3DgYAoTtTv0cmLw9IZpUfugp2-EnWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✔️
🔥
بیشترین تعداد گل/پاس‌گل در لیگ‌های برتر اروپا از ابتدای سال 2026:
🇪🇸
لامینه یامال - 24
🇩🇪
اولیسه - 24
🇩🇪
کین - 23
🇮🇹
مالن - 22
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برونو فرناندز - 22
🇪🇸
رافینیا - 21
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/Futball180TV/107164" target="_blank">📅 11:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107163">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f3392248d.mp4?token=sq7DQMhwsI71il9hKXx0Fbeeg6t_O2nhrFsBHwE6kKaG93pGSZI1RDrvtVrhMXZ2Ol9ahcS0p0oqJEVsdWdqiYL7Hq4WqDfAf43KoBaMA1CmpIEOzu9wppnuvIPC_Irm2L6X_YwEMgQ1SBsoxzPPwD0CaRytguoL0qIwnPys8-Ct0vhhxkQ9tNB1IjkAEGovn5offSvm9HU4hDqCm_rSP7dTbnzeUwa7m_mVvuB3JSeysQMoW7kaHiYsBHdaVRjUL4R1F02IGMknAKAz9dH1IKynvu9VTXAzv652WpHE5OWM21PitJ0eGO0rdpzC3Ng0RJcYPXPdzegfdshe1_4pFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f3392248d.mp4?token=sq7DQMhwsI71il9hKXx0Fbeeg6t_O2nhrFsBHwE6kKaG93pGSZI1RDrvtVrhMXZ2Ol9ahcS0p0oqJEVsdWdqiYL7Hq4WqDfAf43KoBaMA1CmpIEOzu9wppnuvIPC_Irm2L6X_YwEMgQ1SBsoxzPPwD0CaRytguoL0qIwnPys8-Ct0vhhxkQ9tNB1IjkAEGovn5offSvm9HU4hDqCm_rSP7dTbnzeUwa7m_mVvuB3JSeysQMoW7kaHiYsBHdaVRjUL4R1F02IGMknAKAz9dH1IKynvu9VTXAzv652WpHE5OWM21PitJ0eGO0rdpzC3Ng0RJcYPXPdzegfdshe1_4pFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
صحبت‌های جالب دکتر محمدحسین پور غریب درباره اهمیت ورزش: ورزش اوقات فراغت نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/Futball180TV/107163" target="_blank">📅 10:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107162">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d50e15c35.mp4?token=C8ZMOk-jkfSrCcstcYuRDVQvz18qPwvdeW5eewEvWd7j6ZSZitR690WiH_3AVIbQcsWS_x3GC21ETt-DmmmBuK75fZXdpFii3iYsMH5QvTpX_5m_ebL7VWghh94kuvXaAd_9pohMVjcE_3A6t_LVdHT0DLUL77NMnWP6IIPXNW0L4kzucm3mEyj9Ej8AYDVtajcMnV4BMnZbf58q3BkZ8W4D3VsQdgBmvIZ06jQ7f7qtzYYwUtyezga5g3zHSWgeUOe7a_Gu31bHLAs3EqvHl9x-qAlfDjj5Cu19XoT1-NsQPGhJDWUjEE1KYUTWE39uOAo2voCgS_Tu5DdoP1E4ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d50e15c35.mp4?token=C8ZMOk-jkfSrCcstcYuRDVQvz18qPwvdeW5eewEvWd7j6ZSZitR690WiH_3AVIbQcsWS_x3GC21ETt-DmmmBuK75fZXdpFii3iYsMH5QvTpX_5m_ebL7VWghh94kuvXaAd_9pohMVjcE_3A6t_LVdHT0DLUL77NMnWP6IIPXNW0L4kzucm3mEyj9Ej8AYDVtajcMnV4BMnZbf58q3BkZ8W4D3VsQdgBmvIZ06jQ7f7qtzYYwUtyezga5g3zHSWgeUOe7a_Gu31bHLAs3EqvHl9x-qAlfDjj5Cu19XoT1-NsQPGhJDWUjEE1KYUTWE39uOAo2voCgS_Tu5DdoP1E4ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اول مهر به روایت تصویر؛ صادقانه ترین مصاحبه مربوط به سال تحصیلی جدید
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/107162" target="_blank">📅 10:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107161">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9544f249c.mp4?token=CX5IAZmLeGeKF9EMrH8HxnoVXStZDgQKcLXilRV8xHkq0zJIkQlkQKoSgrd7omHyWgxVy6n_cm3G0UTq1dtVRLTaC5nWREohN00Oyyg9t53OjELvbuVfsp_nnsGiVW75kkPthgaMRrqWXJOo-JQpYw0ZcgytGZFF91R5T3rToZzEx5jJogydR_2CMf-ReqzMXw0i_4giaV58nCGPbIRVElavzD9jUkR_nLSHLN03JCMJFGb7jWnn_b2BlSEd3FR5j3unpyXkRWn505mFFwECgpjfidLdYCXCdgrOcYkpupfih2DEiT4QDQwzNPrijDdgIF3kNBkq_AjfIrphN6ExGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9544f249c.mp4?token=CX5IAZmLeGeKF9EMrH8HxnoVXStZDgQKcLXilRV8xHkq0zJIkQlkQKoSgrd7omHyWgxVy6n_cm3G0UTq1dtVRLTaC5nWREohN00Oyyg9t53OjELvbuVfsp_nnsGiVW75kkPthgaMRrqWXJOo-JQpYw0ZcgytGZFF91R5T3rToZzEx5jJogydR_2CMf-ReqzMXw0i_4giaV58nCGPbIRVElavzD9jUkR_nLSHLN03JCMJFGb7jWnn_b2BlSEd3FR5j3unpyXkRWn505mFFwECgpjfidLdYCXCdgrOcYkpupfih2DEiT4QDQwzNPrijDdgIF3kNBkq_AjfIrphN6ExGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو از یک‌تئاتر با حضور مهرداد صدیقیان و فاطمه مسعودی که حواشی زیادی داشته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/107161" target="_blank">📅 09:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107160">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5567bbdad8.mp4?token=SdDXXZYw0r2GpGaMJcA2ym6e13aWJBgpWQ6Nzyg1hnkXJWu4WQul7kK8oAFPCD1n4Axp6Y2XgPI9fPpklxILeywdGFgWezhpQ4J7NQcz7I0JhFwGylemWC-jHcq7eIFCCM94xj6olbjm2vOL9IYBFHFuL0pitH65cpU0TErH7w0s70I4bQVhEn2Oad-DpVbBRdvUgjqoObEsV7e1YpkURjgdOMTaSkDc98fv2oaBD2ZEI4Y4nw4MpRBjnxMUBk-B8ez-V-cyKl-eFXusrNHC95NdzXI4lhn5KZurx2gJM2tWY7sY63UldLLaW_Tt0jklLp51jJLkkjZpRKQitoaMEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5567bbdad8.mp4?token=SdDXXZYw0r2GpGaMJcA2ym6e13aWJBgpWQ6Nzyg1hnkXJWu4WQul7kK8oAFPCD1n4Axp6Y2XgPI9fPpklxILeywdGFgWezhpQ4J7NQcz7I0JhFwGylemWC-jHcq7eIFCCM94xj6olbjm2vOL9IYBFHFuL0pitH65cpU0TErH7w0s70I4bQVhEn2Oad-DpVbBRdvUgjqoObEsV7e1YpkURjgdOMTaSkDc98fv2oaBD2ZEI4Y4nw4MpRBjnxMUBk-B8ez-V-cyKl-eFXusrNHC95NdzXI4lhn5KZurx2gJM2tWY7sY63UldLLaW_Tt0jklLp51jJLkkjZpRKQitoaMEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
«پسر بد» در روز اول مهر الگوی دانش‌آموزان!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/107160" target="_blank">📅 09:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107159">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9d6b05a55.mp4?token=rfmtjYp6BnuAMgSIJCyOO8lTtB5MoMsVk19BZC34GHbJ65MDWl6Rr8FVRiF27dZkxP5H8A6gNpAF21CMzpmbo7QQb_0HyHpRQGUp8_QXvWeQmPEF_QEyOfe7puJw9mHQuK3uKE2EYHozALkRC-1HrvAfmw8UvXku_6PvUJKi-7qWxVJG22nA3p0lh7QHRLTtOQ4gJf8UVIXLsQMocOm2Oe6fsIBbB390kOTkObg_YPAZmp-Y3pC6QBzjYnfO8Eq-cCYQR5gJK86q10pWBVzm5FvbHusbQZpRBLPGNITN10cilzcWSe6IR-t4Fcxm_VdkgPfG2m4PfyaxaYMLOcl8tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9d6b05a55.mp4?token=rfmtjYp6BnuAMgSIJCyOO8lTtB5MoMsVk19BZC34GHbJ65MDWl6Rr8FVRiF27dZkxP5H8A6gNpAF21CMzpmbo7QQb_0HyHpRQGUp8_QXvWeQmPEF_QEyOfe7puJw9mHQuK3uKE2EYHozALkRC-1HrvAfmw8UvXku_6PvUJKi-7qWxVJG22nA3p0lh7QHRLTtOQ4gJf8UVIXLsQMocOm2Oe6fsIBbB390kOTkObg_YPAZmp-Y3pC6QBzjYnfO8Eq-cCYQR5gJK86q10pWBVzm5FvbHusbQZpRBLPGNITN10cilzcWSe6IR-t4Fcxm_VdkgPfG2m4PfyaxaYMLOcl8tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
علت‌احتمالی عدم‌دعوت قایدی به تیم‌ملی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/107159" target="_blank">📅 09:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107158">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKtX1CnBvLG75i3lVVgmubd05odZE6d2Ab2KBYMzvchu_pFwTFiV7ehd8t6EjsI_qxqA_UKTgIpyJR0r3C7-6NxN8g1OJDretzpBquLn6_k9RgohyfDnVDXJNRsNbcSdewGdyBMomK1dgQKopHBvuC41yLJqCeT3uuF8_VLsnukIrRuu6p0tdpBGv3roscLBjn_IAjLgmHpW92poBtY30inkcqqPJK3KDTkphG3V7x9f4urke3WR4mAZQKYvy5cYPDCoR-IbReYXLo3ziprnKbT8Zm9sQnSW1oAeoNuRAYpOF4ejX4lkhr-dUD7bIU_FJyTlUfTLARZrXZcN7NHX5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
آخرین پیراهن آدیداس برای آلمان پس از ۷۲ سال
؛ از ژانویه ۲۰۲۶ کمپانی نایک اسپانسر ژرمن‌ها میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107158" target="_blank">📅 08:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107157">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107157" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107157" target="_blank">📅 01:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107156">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NogNAHJ821GyP1Dbve0wQiPpYVoq-lYUDaTbHYaSXhYWznh0tG1shQy8YV4Mo6J_b--ja27dQWbV7nUI-nlLigoW4JF2Iz5pkwTw4DYadOC79MO9vl4_JxB25GcXeYunfEn6Q-KY-NZsc0D4K8ix55bk__9NjCT6r2mQddPirQ013Bes_i_7rVBn8VBJ11YJTlkKwjOgnmChzpN-ig3-W7gC41wXLkoZ2RvLYgLVa1OGjYSYyNKfwKPakY-geBU2lQAvsfGVLHqZqdq8sv9Ddf2oByV9tjvp7eYxO0RrhZQPH2nR8LYkSTgg3yN9g8o-ZtCfeqlDmQyAwMN5UTG2gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107156" target="_blank">📅 01:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107155">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E018_kEzcgc2HGTFqX1TxUxbnfEjCCOwoIw9uzyiqI7mmMPEwlvUF7HDyDeGO3iZdJKeGHKtOE2dGNbEoPtROYKbQks7CQgph7PgNqRLw359-kX_SHpyAkkdR94HjsrBBha-zQZlPvIM6rSCGVRemM_sNDI46a9GEC-47ABCiwizduN87OjgflIJij-W3qts34mhnTeCLm6WccQd-8mTJIi66h5VXL5d2MLoshhwOpID7-IwAOYIPSzN2_t0zuuCozfThlWDyerxga1iXSfgVBmLqJc6leOD_bQ7tYh3WSxCng4WkDl_ZUNDd7N9CHbmHLpEiKQijTvUW5R6BEXJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
ژوآئو فلیکس: درسته امباپه و کین فصل فوتبالی خوبی رو داشتن ولی به نظرم لامین یامال خود فوتباله و کسیه که مستحق دریافت توپ طلاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107155" target="_blank">📅 01:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107154">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
دیدار استقلال و تراکتور بجای ۱۶ مهر قرار است روز ۱۵ مهر برگزار شود. این اتفاق احتمالا بزودی از سوی سازمان‌لیگ‌ اعلام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107154" target="_blank">📅 00:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107153">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IswTuVo_pttjK5MubWPB0pPXHTXUyGtVxXOEZA9fdKFC5ONzm21hEQu__Mdz8nxOzDoZHk75SGjT0zzMVKLyRu-en6b5ffAMQ2X_ebtovxTAFGfpLiIR2iuy8wO9Ng4vxXcz5hMjnyuOoMTwM1e0jj_SD1ryHIj-XHGNg0VD1mnVPJ-ZVxoUrN2Uvs6kDgwEQ3kh_w5_3VTPbSexXg0G9DMtQ_ilfNcjwExazfp7DjnNv4sqFda85CXTn4he55qhVxZP7ioyF5F2DKsgXmw9iSqw261tv1OpOOXmSppkjp4zfpqhy4p8U6Uas8hGKMYe6nmSwG-jZ6DtJ0PRA8AQ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
دیدیه‌اندونگ بازیکن سابق استقلال در لیست خرید جواد نکونام برای تقویت تراکتور قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107153" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107152">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd6935b14.mp4?token=LXUd7U0rbkKPOPNageBcpWQgjINKbD3UvA25ig6GhY6c5tffUWY5AYhYXZ8OGqDAKH_pqApFqDbaYoGTUVoxWDoRmxUYmvhHSPyLZiLFInYT1XET9WCGwtpEKWMP9nNqavFt1xsL0Ty-dzRNgDWym4UOZyMQLee1tpJxgoJpPnnublwyuRGji6d_MIJZFAr8kdmszdUvyDG3i5zEmvzg4-3kGBTtuwzOTvziJbo9VDX5y9NxCJRvLmU8a1yg6OVir77r7wrV8yLnPByGlWEEKrcM3XoyT0HqWqubr4n1lJOYGqZqrGz6jHn6hkmn5iAQwhy5vKQabVeDV2gd2G5dOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd6935b14.mp4?token=LXUd7U0rbkKPOPNageBcpWQgjINKbD3UvA25ig6GhY6c5tffUWY5AYhYXZ8OGqDAKH_pqApFqDbaYoGTUVoxWDoRmxUYmvhHSPyLZiLFInYT1XET9WCGwtpEKWMP9nNqavFt1xsL0Ty-dzRNgDWym4UOZyMQLee1tpJxgoJpPnnublwyuRGji6d_MIJZFAr8kdmszdUvyDG3i5zEmvzg4-3kGBTtuwzOTvziJbo9VDX5y9NxCJRvLmU8a1yg6OVir77r7wrV8yLnPByGlWEEKrcM3XoyT0HqWqubr4n1lJOYGqZqrGz6jHn6hkmn5iAQwhy5vKQabVeDV2gd2G5dOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اکسپلور گردی احمدالشرع رئیس دولت سوریه وسط سخنرانی‌ها در سازمان‌ملل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107152" target="_blank">📅 22:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107151">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1cBvc3WMr7s-Vel_4SghPzCxkm-NhjU-7jVoDk2ypFsaXVvc-0_T5QcNECKLJHIjb5KncQvHasjk7Na3gokyZcuTZru4Oo_l_VIVQFB1K0lXSv4dplZuCAhm68tvsvSZeYk_VuGD03M7QqF1v0OaOjezArl2XPZlWYrEPl9B4qS4roBqf061_6SqdimH-ECJXZGZmXmfbR0ueT-C6SNwCnO8m_32diXPhkO-ctmyhX61BJDzCD5bZ8SPuyHSkfd1cLkpXxl0dHL2oihpZE1lO2AST_TPZ7WdRq230hpEEH6OUm5YTO14bifT0Lc6C_phRPac5nmIEEBdmB9D9K7Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
آخرین بخش صحبت رونالدو در کنفرانس خبری خطاب به رسانه‌ها:
بعضی رسانه‌ها عاشق حمله کردن به من هستن؛ اونا سال‌هاست که سعی دارن من رو از پا در بیارن (بکشن)، اما این کار هرگز روی من جواب نمی‌ده. شاید با یک شات‌گان جواب بده، اما حتی در اون صورت هم من می‌تونم از گلوله جاخالی بدم.
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107151" target="_blank">📅 21:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107150">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddf19637c.mp4?token=do-1j2vXiQ3SsMvWppx-CdNiwWi0o79KWGseRuVbORIHb-sRqKIwliP_t21uJ3XthsMqP43IP8GUrl9jQPCI4CiZDcnZESJUiIm93sBXHeHyRA4KrLHFTNRphDw5dqTD1Yf6s38RFlhfjPOjqkMWiOqANR6R7ohKixz1Iu_vyVQ8ayhNk4998HWwYLHyBpcHvGcbGlOz1JMskotYkS94oACuNUebIA1oVepH2bJvFE7D4Rh9zhH56KcvsOi8eUvVlWnKw9hKsAFGUNw-fOFB359CoVdMfs4yTavz_MqcHuOSHtvERxjeahHBhoo07HzuioAjTZEElPtz5CVDbSJ28w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddf19637c.mp4?token=do-1j2vXiQ3SsMvWppx-CdNiwWi0o79KWGseRuVbORIHb-sRqKIwliP_t21uJ3XthsMqP43IP8GUrl9jQPCI4CiZDcnZESJUiIm93sBXHeHyRA4KrLHFTNRphDw5dqTD1Yf6s38RFlhfjPOjqkMWiOqANR6R7ohKixz1Iu_vyVQ8ayhNk4998HWwYLHyBpcHvGcbGlOz1JMskotYkS94oACuNUebIA1oVepH2bJvFE7D4Rh9zhH56KcvsOi8eUvVlWnKw9hKsAFGUNw-fOFB359CoVdMfs4yTavz_MqcHuOSHtvERxjeahHBhoo07HzuioAjTZEElPtz5CVDbSJ28w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇮🇷
🇮🇷
کنعانی در دربی سامان فلاح رو تهدید کرده بود، حالا خودش به تیم ملی دعوت نشده است: «نمی‌ذارم پاتو بذاری تیم ملی!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/107150" target="_blank">📅 21:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107149">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHIiUhZy5s6ZhEEOzkCZv611ej7A6KTuid1n6-6kfmOdF-MZVF0kjpy8XHVMQiXJbv-3jNa51oNxX6bb-3hBJHgm-3Cb3DhbnhYvCpjJ5ONJwiLIcu5ACEx9ZUit69ZSyKhNoDrqWi1Q0iJGeekrTM4OwJtFy3UvR6m4y3-LUDO_QrhYEdtibUYFg3gv2W9on23zwqPH0yTJfmi7FNOD1ZP5ml7L7SMlGaWh2EoPHOpnY0KfenB9JJ8E5aOaIa6kb980DNuw2DrDuCdsp3w4JTtICL21OLc2kjwXtDrPoLeOFlRSFDO3NENsBK9orQq4izn6yeBJKZcOd_2pUo3d5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
اپدیت جدید تلگرام از میانگین زمان سین زدن و جواب دادن به پیام پیوی ها !
اینجوریه که مثلا وقتی وارد پروفایل یک شخص میشید اون قسمت بالای  شمارش میزنه بطور میانگین، چقدر سریع به پیام‌ها پاسخ میده مثلا 5 دقیقه، 2 ساعت یا 3 روز!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107149" target="_blank">📅 20:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107148">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c700c8bb.mp4?token=JfbGazzy6ExbnLQkQsOw6AJleK4bsKzZds2ZDKhvYte8dblmpv3S6k5_2VrXbHWHv8_qy-plz4uq2JxVkW67p1OVrzESlmnT_LQrdJNLFfzn9MH_8_gelWfqJiGJ7PEOGHNrhXuH69fkXS2J9UXvKeqf_U79fBQ1e2nxoX34mSHLnZfMhHeW7McIXAAWOa1SBe0zQUtO-sEXVNKepj-7qhcWgjQya9IFPkGdUgW8-xUuEeB86qlPkjmBHJg2aqb-K1oio6CGhOmUmuzvgWtrTa4PIJMZ0csA2rkOZs8fvWG9rcqrwK-skIW9Iruhc3Z2wh0RxWrLVYNODWbChlTqhSNIqdiNyvD45NHgHmJHp-0dx4a5Pe3ef9uNcVP4tdViDeTxt0En5TGRCwUsX4Ypp7Bjuu8TSNo9Mqc3kOSF4Uc1ap2CDtm4L7v3kW8cCmZrPM25u7oEWJdfEjJvwyIx8LXjeX51WgwF7OACaAecXmLS6WPEPyGbqA1vbtZBqAAREp7uT-dHiFhgevBxyZoMEWMKaU9osAHnYi8l3MywGgGI-2Jtpg6OQnadewJALfXS1jmZ5b9QQz5MOxXuajurSG5GXtBOQSPtFkrqL2tyNYh_ZojXHuQy2WawQWzTfSfnn3xCUoVqU0NQfZ5IhpRH6FJOllLH_uZFJIzixsmZKvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c700c8bb.mp4?token=JfbGazzy6ExbnLQkQsOw6AJleK4bsKzZds2ZDKhvYte8dblmpv3S6k5_2VrXbHWHv8_qy-plz4uq2JxVkW67p1OVrzESlmnT_LQrdJNLFfzn9MH_8_gelWfqJiGJ7PEOGHNrhXuH69fkXS2J9UXvKeqf_U79fBQ1e2nxoX34mSHLnZfMhHeW7McIXAAWOa1SBe0zQUtO-sEXVNKepj-7qhcWgjQya9IFPkGdUgW8-xUuEeB86qlPkjmBHJg2aqb-K1oio6CGhOmUmuzvgWtrTa4PIJMZ0csA2rkOZs8fvWG9rcqrwK-skIW9Iruhc3Z2wh0RxWrLVYNODWbChlTqhSNIqdiNyvD45NHgHmJHp-0dx4a5Pe3ef9uNcVP4tdViDeTxt0En5TGRCwUsX4Ypp7Bjuu8TSNo9Mqc3kOSF4Uc1ap2CDtm4L7v3kW8cCmZrPM25u7oEWJdfEjJvwyIx8LXjeX51WgwF7OACaAecXmLS6WPEPyGbqA1vbtZBqAAREp7uT-dHiFhgevBxyZoMEWMKaU9osAHnYi8l3MywGgGI-2Jtpg6OQnadewJALfXS1jmZ5b9QQz5MOxXuajurSG5GXtBOQSPtFkrqL2tyNYh_ZojXHuQy2WawQWzTfSfnn3xCUoVqU0NQfZ5IhpRH6FJOllLH_uZFJIzixsmZKvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✅
چهار عمل کاربردی در نسل‌جدید گوشی‌های سامسونگ که حسابی به‌دردتون میخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107148" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107147">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c1442263.mp4?token=CQ7TRjfrHuSLsiD1EhhaRo7pq0JEvLTPZ1yewTgeOC4RjNsSpTGYat2cv9bPC4iDLZhodAn_cnrKhr5PUNR-iHjLHnxdgFW06MW3tCz3n88F_1objD1T5IFKJi4aNZp_-KeFvbWIcDcGBvHZ-xV6A1zf3Zmf69SCwtPElx0ivG-B7SI-TTkPlH1OHnGn1XE5svqjnkjhqjM7nnOqGOOtxNKp0SSWmJll-nS4dDDFxWFCOodG0ivVJde637fxzQt-StkteFQCO5q4CtvhK0POzJ2pCuciM71nUFI-t3-IokM2HHtDbPtMwBXK2xcNkC35c3dqA-oexGieTo8IdxeGeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c1442263.mp4?token=CQ7TRjfrHuSLsiD1EhhaRo7pq0JEvLTPZ1yewTgeOC4RjNsSpTGYat2cv9bPC4iDLZhodAn_cnrKhr5PUNR-iHjLHnxdgFW06MW3tCz3n88F_1objD1T5IFKJi4aNZp_-KeFvbWIcDcGBvHZ-xV6A1zf3Zmf69SCwtPElx0ivG-B7SI-TTkPlH1OHnGn1XE5svqjnkjhqjM7nnOqGOOtxNKp0SSWmJll-nS4dDDFxWFCOodG0ivVJde637fxzQt-StkteFQCO5q4CtvhK0POzJ2pCuciM71nUFI-t3-IokM2HHtDbPtMwBXK2xcNkC35c3dqA-oexGieTo8IdxeGeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
‼️
مصاحبه‌سمی یک دانش‌آموز از اول‌مهرماه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107147" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107146">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107146" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107145">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1cW94FALM0IgokBt630ROeEiiPGtMvTJEXnMJ-do4Ni6ubweTEjhWeY0JfCDxVq9cdv4FXFApXVgmT1lhpIwJjxsJH1BdiYTP7ig8s8wkwoN7E7RbS4GNU9AHu4wkbgmWAzxQO3OF9azKQwz8psM7XJ1iVgzC0rnNt3Uh7qwyCNuTe2w4V3ZuWOb5FZBNVxwVbkIpwpfOrP70WufndT1cWDmFE4KXs1k88NavJAvjEjY4QEmayv6yW7I8_1fgoFZpkzlz4gOxjn1_6MR9HsOea8gKKGs0zhJFwv7UnZ5YV9rg3D5Xrwg7pGn1LhFJ7AiG1g3FKBOySh5p4B8cCLJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107145" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107144">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c1442263.mp4?token=DhfXFeDGGkv61P0YU_Pk6LxDQZG0hYomlJpYUxjLaTwV70DZ1SmLtMC6w5Lrqh95HQTbOHn2W4c0eWvSTqywTSYOK4OuTXCc9Clvo6fLERUSXhwkKXlsaxAN0EkxMtrpKOAF7ngu-kiGKVBGvo1AMl_t0uT1UvXNEmqho1S_XZOPC0taZ-jY5fOw1JtSBxkapbbFtnTRUmdel1XyGxB4j_ziY7SSt9ul6pSMOGCPfuMe-ToAIPuKyCkIJslCQOy8IUHvYwDEi8TxCwnUVfA00TyxKkQtQEPVfk9AXHZ0aqZkygxG6abirmHKh0uxiTqpnDhXqzzKPCeSMBiXeEkSzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c1442263.mp4?token=DhfXFeDGGkv61P0YU_Pk6LxDQZG0hYomlJpYUxjLaTwV70DZ1SmLtMC6w5Lrqh95HQTbOHn2W4c0eWvSTqywTSYOK4OuTXCc9Clvo6fLERUSXhwkKXlsaxAN0EkxMtrpKOAF7ngu-kiGKVBGvo1AMl_t0uT1UvXNEmqho1S_XZOPC0taZ-jY5fOw1JtSBxkapbbFtnTRUmdel1XyGxB4j_ziY7SSt9ul6pSMOGCPfuMe-ToAIPuKyCkIJslCQOy8IUHvYwDEi8TxCwnUVfA00TyxKkQtQEPVfk9AXHZ0aqZkygxG6abirmHKh0uxiTqpnDhXqzzKPCeSMBiXeEkSzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
‼️
مصاحبه‌سمی یک دانش‌آموز از اول‌مهرماه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107144" target="_blank">📅 20:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107143">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😆
😆
😆
رپ‌خونی سمی ابوطالب برای تیزر برنامه جدیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107143" target="_blank">📅 20:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107142">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d24115e06f.mp4?token=s_o6fI4MqxHx6vh2gMtG62MxARiF8-sNufMutTC2a7WkJtIShWFZGmVrh2T-2viMpQiT9GQ7cVPuLPoraQogoaJ58-HY5lZhsS9f8IvNKVRZtYknWLqt4jpTdfLP0ORHvOxdI2uUE2wde6ym3OiIWPx3wN_NHIp6twjy39bSsWuxsuc02gE-QeBri4TD09v1rSKQS87HdHYnS0IU9w7GmN7unHgrRe60VEzA_PlE0rMi8xvJtDN0XvNJFEJHSfWKzGUlrftgbqfCM5BsENavAMzj0XL3xR_VSxX681lYSJSON-5njmSkUteKCpm0glKuxJnm-dOqa-tf9iJXmUavUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d24115e06f.mp4?token=s_o6fI4MqxHx6vh2gMtG62MxARiF8-sNufMutTC2a7WkJtIShWFZGmVrh2T-2viMpQiT9GQ7cVPuLPoraQogoaJ58-HY5lZhsS9f8IvNKVRZtYknWLqt4jpTdfLP0ORHvOxdI2uUE2wde6ym3OiIWPx3wN_NHIp6twjy39bSsWuxsuc02gE-QeBri4TD09v1rSKQS87HdHYnS0IU9w7GmN7unHgrRe60VEzA_PlE0rMi8xvJtDN0XvNJFEJHSfWKzGUlrftgbqfCM5BsENavAMzj0XL3xR_VSxX681lYSJSON-5njmSkUteKCpm0glKuxJnm-dOqa-tf9iJXmUavUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش پیمان طالبی مجری شبکه سه به شکست چهار گله تیم فوتبال امید از کره شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107142" target="_blank">📅 20:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107141">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEbhNe75Ce3m-qbez9Gwz_DZZMpr5wChlMbK2JpCu-8padRKO3IS_W1aOj7mfvUrtBkJQsm5gRssZwxko8RZsjF9XAG0nQSOPBOrzeREE3qM9uoI6JiMGu7W5cgHookmWuylXOa3NlkadgHGCnKR-ptzv25txtYb9nDoJ_oONKeqQge4LyxqHIW8rQvdZWTqSu6uuxdXkhQrEM-VkB2aWOvgfENtaQbR5KJw3eBguIYgV7Ea-G0Spq2x4w3ncKcnS5OLmUKHC4MIm3fN4Cw-R0VXSW4JTjaAOT5yuYBnDPpis3BvoEjp_1cfD4jFDeQM9znGVziZaUjX6VNiHTgINQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
📱
استوری‌جالب زبیر‌نیک‌نفس بازیکن سابق استقلال به شکست ایران مقابل کره‌شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107141" target="_blank">📅 19:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107140">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ig_sovyGH4Je52HKsVPkHUFzOsE1d6IBkBGWpA1hznaeZwpsBtGJLnQYMZMlili_CwoSwuBTudyBTzuZ77mceUXaRwjRYW86MRlALI7_4DgHwUjyzZJYbKdbZNazNLNWqdU0dLgiOBMYFAttTrXIe59P69qVcewj9Y1wEzrm6TBiEhuEnSczxtodlmhu7x4Y4NJ0CVmLwhGzjyklH6g5CQU8Z0VvhxRfFTQr2Js7aZmEniuFgny7hUH9-60LIxsB19UGKtKsicL7r8-VP0F__eucAFfaex6U5ZegKZ9Va5OoeJf4D2apjr5ySwtgqnwM6yim_14iexbuD_7bE7qIKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
بهترین استارت یک‌فصل بازیکنان بارسلونا در تاریخ این تیم با صدرنشینی اسطوره ابدی مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107140" target="_blank">📅 19:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107139">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‼️
آنالیز جذاب از بازی‌هفته‌قبل برایتون و آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107139" target="_blank">📅 18:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107138">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441f0e0f4e.mp4?token=LwluP6pgqtvjsT_psrpFbEJMDW9eWs7PhLHhg71Ek45eJWtczf5WHzTyvsZ2W5G09uSF3HEgQ18f2jkQMDY6JY8TzTnn-NOcK7JaHeyqgbykSgpr0vm3oW-fSp36BqwEqP-B_TLEZsjvZgU2ysaMHjDB6-PhzfgUk6Kqg5a9okNXCKynhza6JpXR0AtLePhuYyGQiB2jOxvt6nwQ_xX4MglKFPiP9VxBJVhLvGwDQWnqpG_Yd829DoY_9A-Lf7AyRWsIyW0-NZuKH2FxwBtmMlj7txkwvb1wk-cS1tkrSxuyQP4YSWP1ZX-mRH9CWjt5nGo_37nn0nSmhYQH6wZG9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441f0e0f4e.mp4?token=LwluP6pgqtvjsT_psrpFbEJMDW9eWs7PhLHhg71Ek45eJWtczf5WHzTyvsZ2W5G09uSF3HEgQ18f2jkQMDY6JY8TzTnn-NOcK7JaHeyqgbykSgpr0vm3oW-fSp36BqwEqP-B_TLEZsjvZgU2ysaMHjDB6-PhzfgUk6Kqg5a9okNXCKynhza6JpXR0AtLePhuYyGQiB2jOxvt6nwQ_xX4MglKFPiP9VxBJVhLvGwDQWnqpG_Yd829DoY_9A-Lf7AyRWsIyW0-NZuKH2FxwBtmMlj7txkwvb1wk-cS1tkrSxuyQP4YSWP1ZX-mRH9CWjt5nGo_37nn0nSmhYQH6wZG9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😢
تشویق مسعود پزشکیان توسط عباس عراقچی و... پس از پایان سخنرانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107138" target="_blank">📅 18:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107137">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
⭕️
🇮🇷
پزشکیان: انرژی هسته‌ای حق مسلم ماست و برای درمان و کشاورزی نیاز داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107137" target="_blank">📅 17:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107136">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5081a6f90.mp4?token=OlGEgekhinFFIbqSFABERgJ-JeGU3TqtlD13EqYv0xdI7uN3M2sovUhgTFBB3NPKlMtYKTlFIWKaNyvwO_OkG5Eo3zi4ehdLNQIOb4bRiUq8yhqrfrO7ggHHr47Ri96bqEegiPFsaz1q4601PPABx4OyyPc9F_b7idEj2b9IggmoiK4nzcry5JB2F23UFL9qWlWawFdxBzmmEc_8nKPcR4AjqtkDJnl72HlO9r_bGlotA6sY9S38DIkcMLQS71ystt2PSEFJpxk9yCzH0c2iZVG5BErcvo8056foR0Ysnoz_BqAzCENUbKsCxA9DS-UqF9hMvJuwiHolcd9eOoLQY5KF1HVT8mdKb2Xl5fyBWFgnPs0oTWak_TMRs1l5mZejfcnrcpWaHy8OYS6ATvBXy9KXHxhuGI7yT1XE0ElWmQiFTgsmiRj37tDhJ0aaIMsZTcccwwyNOOkVws4_eEh2l00nCcB-Uzyf6JV-71IAUlfnF-EXXbOI2MzW2wkAP9V80E_0iovYCC_G4iFqwu6ItXQb4Ei8AHikhKTH0gL6TLSHfC4EhQP7MSVp1TZAE-pmJZyKC1S-erGXP4MWOiX-pcXmBV-IB8PltMz3wTf7PWCjpGG69lEDZdFLt9TiWdqBzMF1ODdjK8nUWSSWLQdyjzXszKgAJxcU0O9OJ_cI9c8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5081a6f90.mp4?token=OlGEgekhinFFIbqSFABERgJ-JeGU3TqtlD13EqYv0xdI7uN3M2sovUhgTFBB3NPKlMtYKTlFIWKaNyvwO_OkG5Eo3zi4ehdLNQIOb4bRiUq8yhqrfrO7ggHHr47Ri96bqEegiPFsaz1q4601PPABx4OyyPc9F_b7idEj2b9IggmoiK4nzcry5JB2F23UFL9qWlWawFdxBzmmEc_8nKPcR4AjqtkDJnl72HlO9r_bGlotA6sY9S38DIkcMLQS71ystt2PSEFJpxk9yCzH0c2iZVG5BErcvo8056foR0Ysnoz_BqAzCENUbKsCxA9DS-UqF9hMvJuwiHolcd9eOoLQY5KF1HVT8mdKb2Xl5fyBWFgnPs0oTWak_TMRs1l5mZejfcnrcpWaHy8OYS6ATvBXy9KXHxhuGI7yT1XE0ElWmQiFTgsmiRj37tDhJ0aaIMsZTcccwwyNOOkVws4_eEh2l00nCcB-Uzyf6JV-71IAUlfnF-EXXbOI2MzW2wkAP9V80E_0iovYCC_G4iFqwu6ItXQb4Ei8AHikhKTH0gL6TLSHfC4EhQP7MSVp1TZAE-pmJZyKC1S-erGXP4MWOiX-pcXmBV-IB8PltMz3wTf7PWCjpGG69lEDZdFLt9TiWdqBzMF1ODdjK8nUWSSWLQdyjzXszKgAJxcU0O9OJ_cI9c8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
‼️
پزشکیان: اسرائیل هر محله‌ای را در هر شهری و در هر استانی هدف قرار می‌دهد و عملیات ترور انجام می‌دهد، درست مانند گروه‌های تروریستی واقعی. در غزه، بیش از 80 هزار غیرنظامی بی‌گناه به طرز وحشیانه‌ای کشته شده‌اند
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107136" target="_blank">📅 17:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107135">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1f06c6df.mp4?token=Idz-RQ7Tdg3xCPYowa9v27UU2WkKqWb70-MEyawS7am1_uUbL14zDyiX_P97_XhD_Fr2H5ro-WQVP7pxw1FqdFqTPjYjadPvk1RrihMUo5cPkpbRnbF2Rv2IuDoPZ2ePRXtKoQ_XOpeCLtewz6qdSluPlP4cE81JLcQAoalTAmNqzbj0cO4LzdQfzdDwJv7DBfo3zVd5eNgiM0fZGBHNxR-yf1qQ2Akr6SA3V9Bgjo9-YoRCNtzj2ElZZAnBE0O9ud46o3UuBUpKH4rjnXoSNbcMV0ppc_NRG9Yq41gVkPIICK-ZTO6nuMqY5JSvnqgXhO-nzxUUpXvRLy4NMhMKuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1f06c6df.mp4?token=Idz-RQ7Tdg3xCPYowa9v27UU2WkKqWb70-MEyawS7am1_uUbL14zDyiX_P97_XhD_Fr2H5ro-WQVP7pxw1FqdFqTPjYjadPvk1RrihMUo5cPkpbRnbF2Rv2IuDoPZ2ePRXtKoQ_XOpeCLtewz6qdSluPlP4cE81JLcQAoalTAmNqzbj0cO4LzdQfzdDwJv7DBfo3zVd5eNgiM0fZGBHNxR-yf1qQ2Akr6SA3V9Bgjo9-YoRCNtzj2ElZZAnBE0O9ud46o3UuBUpKH4rjnXoSNbcMV0ppc_NRG9Yq41gVkPIICK-ZTO6nuMqY5JSvnqgXhO-nzxUUpXvRLy4NMhMKuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
خروج هیئت کشور آمریکا حین سخنرانی پزشکیان در سازمان‌ملل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107135" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107134">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/12488a1f46.mp4?token=CjeNwi0x434gPdr0XiWL_bOgTT99wBpEUja-7qDR1n0IecuCiqjjmlYgYpmLkQQ0Xp0K6N-SnVjopk53HHd_pJe2YH28re4y2y7SvCCDtMQvGiX3A6jSDWhgvpXZpbE8gea07hj-l_Apg2xmdNJ_cpyqvNuNMvIzXmlsB_uZoBIp_LRg7LQoJMzVazLCD5XEYpgMs5qk83NjjdWI2nn1VWZGLQv90WeRPiDqdYRBjWI8r2nOq4QIf_SCaRYO6hN_O2_lVH-YDKXAOzQJDt278Pqi_1K0t2exMWPCdQ4C739xz-deFsjJ8sL--Facnn6WdEyA-Gr8D87id98xWSPWpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/12488a1f46.mp4?token=CjeNwi0x434gPdr0XiWL_bOgTT99wBpEUja-7qDR1n0IecuCiqjjmlYgYpmLkQQ0Xp0K6N-SnVjopk53HHd_pJe2YH28re4y2y7SvCCDtMQvGiX3A6jSDWhgvpXZpbE8gea07hj-l_Apg2xmdNJ_cpyqvNuNMvIzXmlsB_uZoBIp_LRg7LQoJMzVazLCD5XEYpgMs5qk83NjjdWI2nn1VWZGLQv90WeRPiDqdYRBjWI8r2nOq4QIf_SCaRYO6hN_O2_lVH-YDKXAOzQJDt278Pqi_1K0t2exMWPCdQ4C739xz-deFsjJ8sL--Facnn6WdEyA-Gr8D87id98xWSPWpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⭕️
پزشکیان: این بچه‌هارو می‌بینید؟ اینارو بمباران کردند و کشتند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107134" target="_blank">📅 17:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107133">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/091ba5b08c.mp4?token=fs7VGNCWvQp8WCVCsPdgVQKpaepk7UunM6eWIdd84DOtfYDlpqPwKCktQhG3cIJJ2RJw1CWilCSUS75tMGaY65P8qgtPeBqpTZ6JZvF4hDhMgSSlhnpW0nQYlkLs7oofXrp86fff01gxWFTvtU0OVthpmiqFD9ny7YV8K6pF8Z6R7rAyoqNSBvQZyTnOo9YNmLOXcrTbOD4hqBPQh0HYkr1AVekYiPXhGhOgoCiNlIO5GR7KKEA9R91-8zlVE-UXhMWlVfRfROOUneziyb8DwDJ89v_l3MR12dQx7blXfOKkhC8Uj5r4DRSqlYJPbGqUYkct9bEVi0zLQd4FHuTDDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/091ba5b08c.mp4?token=fs7VGNCWvQp8WCVCsPdgVQKpaepk7UunM6eWIdd84DOtfYDlpqPwKCktQhG3cIJJ2RJw1CWilCSUS75tMGaY65P8qgtPeBqpTZ6JZvF4hDhMgSSlhnpW0nQYlkLs7oofXrp86fff01gxWFTvtU0OVthpmiqFD9ny7YV8K6pF8Z6R7rAyoqNSBvQZyTnOo9YNmLOXcrTbOD4hqBPQh0HYkr1AVekYiPXhGhOgoCiNlIO5GR7KKEA9R91-8zlVE-UXhMWlVfRfROOUneziyb8DwDJ89v_l3MR12dQx7blXfOKkhC8Uj5r4DRSqlYJPbGqUYkct9bEVi0zLQd4FHuTDDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نشان دادن تصویر خامنه‌ای توسط پزشکیان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107133" target="_blank">📅 17:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107132">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXQCL49NzoKo3Cs5Sjk8I4pfbsnGPPYlxWAvp6zQTsCyujICcbsklFZ1R2_JIXYJwpfepIxL-bPMnYNcoXgBTc8S_rpFhzZeckn2GrFOoeaoTDMDXGqXWgBlCUiawYtfdsd-GTF99xPIaBl-hcPSVoXtCEKU7QJm-NY4z-wi8PMW_al2_xnDdse5f3NIGKMGyVoiC31hzs7dLoajlKe5JzoUQihFfXqVr-1rrfIntKnhsYmbme7gQqM8-hWVuk2Z2CcAzHbubElpr5tx7EOKzmvPmlYIJ_yNbXBwFTIlyFgQNtM2hW335t69c33Xhzy2-xuU-b1Mpns6C5WV-a97ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
مسعود پزشکیان در مقر سازمان ملل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107132" target="_blank">📅 17:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107131">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7461ab4ecc.mp4?token=lcG6-pvpy4Z3p5jMhLszFQZQ45mou64D3Ssb9b9rkQg4EnP256nsWYd4mVZ2-Nu25jbTpruuZek6hMUSslbN_VbFvZORrKvYX6rRUWArgxse7VQ-tMQPyx8ACOQPPDuow66mko_dXlzL5BiMWqNNcT1kn7VybLTwn4pg-Ly1ARt8jdkEIFL6ohfeOh_wPAOYefqYKIvHT1GslWu3szjA3OfD5QewhGmHnyZyRpChB1tkdOAtIoYjFFERQziSKLH_ldttZAiWibqbY-AMtXk1thDwLWqvkCzLOzzTTtMBRIdQFzSpoP5A7b-UyxoTghRqTTfPHrOltNTyck1k9jCClA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7461ab4ecc.mp4?token=lcG6-pvpy4Z3p5jMhLszFQZQ45mou64D3Ssb9b9rkQg4EnP256nsWYd4mVZ2-Nu25jbTpruuZek6hMUSslbN_VbFvZORrKvYX6rRUWArgxse7VQ-tMQPyx8ACOQPPDuow66mko_dXlzL5BiMWqNNcT1kn7VybLTwn4pg-Ly1ARt8jdkEIFL6ohfeOh_wPAOYefqYKIvHT1GslWu3szjA3OfD5QewhGmHnyZyRpChB1tkdOAtIoYjFFERQziSKLH_ldttZAiWibqbY-AMtXk1thDwLWqvkCzLOzzTTtMBRIdQFzSpoP5A7b-UyxoTghRqTTfPHrOltNTyck1k9jCClA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
پست جدید عارف‌غلامی مدافع سابق استقلال:
شجاع تر از آنچه ميپنداريم، كمي دورتر برانيد ، زني درحال فتح ترس هايش است ، ١ مهر به ياد تمام دانش آموزان و دانشجوياني كه ميتوانستند در بين ما باشند اما نيستند ، روحشان شاد يادشان گرامي
🖤
🥀
💔
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107131" target="_blank">📅 17:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107130">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107130" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107130" target="_blank">📅 17:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107129">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGJkykgZD7lKoYgdBaBydWHPODaP6JpivLi_uRlqrZZlxOdrr14NibOpfzPzFMQV6rwqM6Qa23h7QkUIRaHnlx0aSkS1flKpixFExbfme7jh7Ig8uNM1GBa2QevvtIH8rZxnxAG78Lx3LU2uAIYmwuTrBss68xY0DDzUalLE1bBO8g8twFS8r2piMJnWyWcSd5xim8Mf0KOYWcE-vBlmWU6H4M_OJRwo8FDicdG5lJXUwwrB3VM4wg1iZvDmzIgaZIR2hbP4S-K09DG83tVmcntcc5Bw6VDP000hj20Z3zLnonbB9AUOARqWyX_u2cX2axK09dcOLWZhNU7VBiyaDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107129" target="_blank">📅 17:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107128">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTnZusq1WliZ_-EDD-jB5Q8aT2Aiu21apSU4zjpABDBwnOrRbrFmVn9QfzUhRCAMzC0hlorF8q6UEZ8cqqCDhYS5WVhz2duBv4fAjE6Y3EVnzy34i9ZYMK2o2NhyAsSfMSN7K8YXtFsI2aOUkOg2wLkbwSZrkc4AeyoqE9BvAWqpvMSzPdk1ydZXU5JKeN2A298oZlXX61gTFG8Plw__0Xh6sr-Vp-jN35fPvxDxg0B-rJvPeM5qGIRVrhBUXh4SalTgucD4XYLhiDroYEskxOP31Y1MMc3BrbUMM6b1Xg1JO5vErWvwQR50o1_g-zxObMqkYx9s0NDWQKB0C-xfLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
اسطوره محسن‌رضایی: به لطف تلاش‌های ترامپ، ایران اکنون قدرت چهارم جهان است و بزودی با تلاش‌های خود به قدرت اول تبدیل می‌شویم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107128" target="_blank">📅 17:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107127">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0y6Vqtc2B1HpknsVNG1ISz4435iswwsKTMBfZ1YWmkZbXK_AQr4mmpmFN21O6NIjKJETPLZjZy_PZI3o_kCZeLyRFNYSSLwfLPyI3UoYaxASd1Fqt3RF9jlK5U2hhlBmAUrrGvAIfVEs6VT4Yt8Gx7cZJlqzXrhbWCO8O3cKkkBrePOjzkG28PQOpmFOFUnMjIVy9pRTB3wBN3Bmym94wmhsWUL7ZKrfn7fH9Af3md8ss8lKott1Eq-OOeXaFporlj-SabS4nckZub-ik1WBJVUvmzboNTa94670xIB58GdbWXVclb6UFKKTTYW68uanbEoDkBSKSX7usuhpvnGSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
کنایه‌های خداداد عزیزی به فدراسیون فوتبال پس از حذف تیم‌ملی امید از مسابقات ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107127" target="_blank">📅 16:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107126">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrEM0nwXmMQWpgbydJmI1QPNFbBYLCexeXXDk6LTAsYkzs493If0dqwfBfCbV9CKFaako6PKyX_LQVh6lW_e6aWSRQVIL6REXruVF15xKKy-VGmBRyE9ohOBqmRVNhQonO1wloniOvlS5CwXeXRaSrnP9LB2MkTLLn75IoJOzGTCLuLGpWKYDamCL1ArgNDuGGj9TGG4-hA5I5csmcjzsGo_QYkRrP14m9nZve2qf9YgltANqbU_7UUrXll9ZcWAH4GEYO4uWSDXl3lbcKtpd1ALUzmakDYe0tPg537_5lhHaPzQmojpGi3_TImrUFdtxn9q2XqacBxFzbtKStMl0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🙂
در فیفادی فعلی و از اسکواد بارسلونا، فقط ۵ بازیکن برای تمرینات در دسترس فلیک هستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107126" target="_blank">📅 16:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107125">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bed3c9448.mp4?token=AAMV4fUyIPk4E061mJkijQ5sNc8FwywASXAd-P1KMG5AZAIdm8_gGvknBj1tLZfKVNYx7VJda0DeRkpis6KWV85l40VgfkbNzUvt9okTyNnB61ppAoCZFE0CcjlQ9Ih9bfvyCFMQ_0A0_drMiwsyb8bXmG52bQ62j63L1UG5gCjVDGoJCMYU4GliCjW67ZgdmiG8XBoRHbQLyJFwW2mZeTpYs9gQ9Hu8EyoRJDgP5QxjrSWiG1QzVOkV9oll0gQK5L0k6vhrbOkne1m24BMzJk1DkWn1xEO8kX1EW85YG0UqHmFuOWHV-EOqK0q7bKuoQl7L1MGyL1ebTNinjn6QOILoLMmFxemrcD2VqVRUc9cnG17jXLqbHRlcIC6uhAPEyg0O0LbHJEhRXCnwDGsOc0NfWTePzlOruLel3RGntH05ciCuPkIHQnQVQy7R6HNOPPByLLnS4LzLgBvpTgU8EhBLXm0JrQdai7WTI8w4xEuEUNLyvsJM7WRPYTpE4_0zPq4Hc24UlS20ws9AYkXXB1lKLGmz0PYgmV-09XgKgFj6pLf65lJj81Bdogne_K2iOmnBPmAC2DWf15p6RHs9CRU78Y_5NBZRZY-3lyxz8P7ge1kw_YmA7p_hnaJX09m22bw1G0rBlmOE-9QoPH8Sdph_QkPxaYdutAPaPctMxCU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bed3c9448.mp4?token=AAMV4fUyIPk4E061mJkijQ5sNc8FwywASXAd-P1KMG5AZAIdm8_gGvknBj1tLZfKVNYx7VJda0DeRkpis6KWV85l40VgfkbNzUvt9okTyNnB61ppAoCZFE0CcjlQ9Ih9bfvyCFMQ_0A0_drMiwsyb8bXmG52bQ62j63L1UG5gCjVDGoJCMYU4GliCjW67ZgdmiG8XBoRHbQLyJFwW2mZeTpYs9gQ9Hu8EyoRJDgP5QxjrSWiG1QzVOkV9oll0gQK5L0k6vhrbOkne1m24BMzJk1DkWn1xEO8kX1EW85YG0UqHmFuOWHV-EOqK0q7bKuoQl7L1MGyL1ebTNinjn6QOILoLMmFxemrcD2VqVRUc9cnG17jXLqbHRlcIC6uhAPEyg0O0LbHJEhRXCnwDGsOc0NfWTePzlOruLel3RGntH05ciCuPkIHQnQVQy7R6HNOPPByLLnS4LzLgBvpTgU8EhBLXm0JrQdai7WTI8w4xEuEUNLyvsJM7WRPYTpE4_0zPq4Hc24UlS20ws9AYkXXB1lKLGmz0PYgmV-09XgKgFj6pLf65lJj81Bdogne_K2iOmnBPmAC2DWf15p6RHs9CRU78Y_5NBZRZY-3lyxz8P7ge1kw_YmA7p_hnaJX09m22bw1G0rBlmOE-9QoPH8Sdph_QkPxaYdutAPaPctMxCU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امان از دست رامین رضاییان و اداهاش
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107125" target="_blank">📅 16:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107124">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9325345835.mp4?token=p0UcUH5lpZyZo6ZVvOUHqKdQE72bysmt5m6G4edGifqm52OxlC2FIDfrFfrUgmG5GeQCeAgnEnbayWjVmo6tlTzML7u9125h-9pMRsuQRVxUtlYAC4-YpGP6Sb9qziCENVHmmKmT8K3NBLwnQkugcdMiSroMvaIoCabKkXkTd1TJRFAKwYBWMtEKgqWVWEktIBF2uN5tHUAUm_4midq1dpq_ac1NAhBUtg6tSBOF5caPIL9C5QXaG_EJpaQ43OA2meCaivu4_clJeSdPxwdTXgBgaduDyJynk0cBUtxiH5CTkamlwSQKAVSvMGp26hPe0erfKL8LCqsFOo76Hqq4xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9325345835.mp4?token=p0UcUH5lpZyZo6ZVvOUHqKdQE72bysmt5m6G4edGifqm52OxlC2FIDfrFfrUgmG5GeQCeAgnEnbayWjVmo6tlTzML7u9125h-9pMRsuQRVxUtlYAC4-YpGP6Sb9qziCENVHmmKmT8K3NBLwnQkugcdMiSroMvaIoCabKkXkTd1TJRFAKwYBWMtEKgqWVWEktIBF2uN5tHUAUm_4midq1dpq_ac1NAhBUtg6tSBOF5caPIL9C5QXaG_EJpaQ43OA2meCaivu4_clJeSdPxwdTXgBgaduDyJynk0cBUtxiH5CTkamlwSQKAVSvMGp26hPe0erfKL8LCqsFOo76Hqq4xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
شوخی‌های بامزه ابوطالب با پرسپولیسی‌ها!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107124" target="_blank">📅 15:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107123">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c20b429d2.mp4?token=ZsyMgaaDMcdiZ7bnvS2_3P6nYMIU5Tzr30K9rGqlddYiAkKWFOcd0uQGnNaVGY6ZKkt6Zx7eaTEMyE6UdNRrE0A-42bKoE3o1_-wkW_KbWOJvmSb-BOCluqGHaf8q1G4Dal4SWGv9lQ0d9nevsaGdHxVN_irbexWQAXTuHJfmHXvg9IOKrNRiqWRrbbpNGUhwF_5lDSPK4BGJoJ-cJIPnF2QW-hY8fa0BDfE9_d4V9Cf37XBgA-OPMbFbxBK7-sWBNGLl3F9wx4jVakgd_pcuD8T2_jFzy0c4d5NU4gM983uc5LA4oUhkoYOYLsG0BkOAYwA6tbJa5lbkDgaCCdcQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c20b429d2.mp4?token=ZsyMgaaDMcdiZ7bnvS2_3P6nYMIU5Tzr30K9rGqlddYiAkKWFOcd0uQGnNaVGY6ZKkt6Zx7eaTEMyE6UdNRrE0A-42bKoE3o1_-wkW_KbWOJvmSb-BOCluqGHaf8q1G4Dal4SWGv9lQ0d9nevsaGdHxVN_irbexWQAXTuHJfmHXvg9IOKrNRiqWRrbbpNGUhwF_5lDSPK4BGJoJ-cJIPnF2QW-hY8fa0BDfE9_d4V9Cf37XBgA-OPMbFbxBK7-sWBNGLl3F9wx4jVakgd_pcuD8T2_jFzy0c4d5NU4gM983uc5LA4oUhkoYOYLsG0BkOAYwA6tbJa5lbkDgaCCdcQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
جدیدترین صحبت‌های رامین‌رضاییان درباره عشق‌وحال با توصیه به بازیکنان رده‌های پایه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/107123" target="_blank">📅 15:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107122">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caee7469d9.mp4?token=CNtHqkW37lMzlV99nET7-HPARYpLToDeQR51i36UKIJqdHPGY3_jj6AmzfQQ26h06cqzg7q0mzMkBwNnByA6nuqqXieqZFekC9vAuDVNls63Ja8N3UphWbWk9Y23IPeLbwTfdZ7rsROZloKSjyOrXAP7rdR6Pz2GIi653HnPki8ZpbtgShWavGFAwFzj3Tf1cOmIl3wTyk8ZUZKCPkawoC5w4dAB5zeASz-R15Qhhdj3Skb5Fw6cdVb-l0QDpFhgNGpsoVA3aQdbHWqnWJnnVqBmczqHl3rnS3fH0f67qSxWPQ8y0AIh1dPs3R39nBL3L6KCBozx1RLq1KR1C3JWKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caee7469d9.mp4?token=CNtHqkW37lMzlV99nET7-HPARYpLToDeQR51i36UKIJqdHPGY3_jj6AmzfQQ26h06cqzg7q0mzMkBwNnByA6nuqqXieqZFekC9vAuDVNls63Ja8N3UphWbWk9Y23IPeLbwTfdZ7rsROZloKSjyOrXAP7rdR6Pz2GIi653HnPki8ZpbtgShWavGFAwFzj3Tf1cOmIl3wTyk8ZUZKCPkawoC5w4dAB5zeASz-R15Qhhdj3Skb5Fw6cdVb-l0QDpFhgNGpsoVA3aQdbHWqnWJnnVqBmczqHl3rnS3fH0f67qSxWPQ8y0AIh1dPs3R39nBL3L6KCBozx1RLq1KR1C3JWKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
مقایسه فوق‌العاده سمی ابوطالب حسینی از فحاشی تاریخی مرتضی فنونی‌زاده و خداداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107122" target="_blank">📅 14:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107121">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3ddf2805.mp4?token=X3BV40JBrF9ShH3uZfjaJ9KOEdY56lVbCTHZVN-xQQEyerGobEX9t-88SYX8Q59U2Xfggf-IUe_CtQM-pJyWt2ZwnPpSvlHrF43vXFzfTwPQqK5xI5M4ksNdNRY5-NgjdERscqewH18St9LjygHpIgwyPpjof-9JBmW_w2ptBFYZFwpgUsB9jKF6cKcewvYxPD9msWfCXMNj-T8hvQkUu4PoPDi6LeEqzscnL87rvpmHwMwe18AKAEJhkQX9wtJwdPGtPTArHE4JdKsvuCtNsOVlSD9uo5nag-biBGah0CGGIs3kU3NDF7czQTjwov4rSzymTC4HhPhYyRTTN0CV5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3ddf2805.mp4?token=X3BV40JBrF9ShH3uZfjaJ9KOEdY56lVbCTHZVN-xQQEyerGobEX9t-88SYX8Q59U2Xfggf-IUe_CtQM-pJyWt2ZwnPpSvlHrF43vXFzfTwPQqK5xI5M4ksNdNRY5-NgjdERscqewH18St9LjygHpIgwyPpjof-9JBmW_w2ptBFYZFwpgUsB9jKF6cKcewvYxPD9msWfCXMNj-T8hvQkUu4PoPDi6LeEqzscnL87rvpmHwMwe18AKAEJhkQX9wtJwdPGtPTArHE4JdKsvuCtNsOVlSD9uo5nag-biBGah0CGGIs3kU3NDF7czQTjwov4rSzymTC4HhPhYyRTTN0CV5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
خداداد عزیزی مدعی شده که یک‌سری افراد میخوان این یابو‌ رو حذف کنن ولی حذف شدنی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107121" target="_blank">📅 14:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107120">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1086d9a961.mp4?token=fdJL4xiE9rKkfV6cILCQuDm2zfHLLukjG0eNF3qXwKTPZqtHBD_hIwWbOOlzrsJgNfakWc7KF6jfrNrQrpzgJFECx7BRAWZRKzy0ybiDopyHEFDRQK_r_8HPMtIJKmFxQW5IPuqyRc0ji2MXULbnoOBN80oWJNxYKd3AZJGIH8hyy6W__2CY7pDuYOSyVIDaOAA6uqrsUPS_3xyu49GqoPBslslGicjQ3n2HX1ktyWez9h7-Uw3Drd0QSFw1v9UYuDrgIb4SKTNVaeWyLfo3Sats1wmNdWxAsDXqqgnJN-oth76wawTzFhgjCdFLLy8ZQFMzwVqFLOtw_h1h9AN9LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1086d9a961.mp4?token=fdJL4xiE9rKkfV6cILCQuDm2zfHLLukjG0eNF3qXwKTPZqtHBD_hIwWbOOlzrsJgNfakWc7KF6jfrNrQrpzgJFECx7BRAWZRKzy0ybiDopyHEFDRQK_r_8HPMtIJKmFxQW5IPuqyRc0ji2MXULbnoOBN80oWJNxYKd3AZJGIH8hyy6W__2CY7pDuYOSyVIDaOAA6uqrsUPS_3xyu49GqoPBslslGicjQ3n2HX1ktyWez9h7-Uw3Drd0QSFw1v9UYuDrgIb4SKTNVaeWyLfo3Sats1wmNdWxAsDXqqgnJN-oth76wawTzFhgjCdFLLy8ZQFMzwVqFLOtw_h1h9AN9LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لحظه‌ای که سیمئونه شورت امباپه رو کشید پایین؛ سیمئونه گفته اگه قوانین اجازه می‌داد حتی اون‌شورت دومیش هم پایین میکشیدم
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107120" target="_blank">📅 14:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107119">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2053a9052c.mp4?token=bY6ghoDk4wEeg8H_ZLgpvmyITD3Nf-_ztxBNj--3dDLzo6uWz6hh7kKMSM6OUmu_RndnCOyl4pBBCUujTywBnnDlq8tD33-SKrHAb2XoB8MpwGKrqvvUqXcQK2vJFob1OooV-ECFK84mMmr7GJcf3w4964UZXDp-O3tA81-tgXbNdWUXJSv42zbAlqHWfSEYDBLByiXtrbRGjvRmx06sGecxGujQn_37QuZLdlfD2kyqN_6g5juLv1gRq94FtISgsnb-mEbcBZdDdPynkOdkm70n8RHGW7sAPPD4JRC-T9ClAhS9pHwBzYqENEeexYy0m2iHCXvuY8ee__h-wBU4Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2053a9052c.mp4?token=bY6ghoDk4wEeg8H_ZLgpvmyITD3Nf-_ztxBNj--3dDLzo6uWz6hh7kKMSM6OUmu_RndnCOyl4pBBCUujTywBnnDlq8tD33-SKrHAb2XoB8MpwGKrqvvUqXcQK2vJFob1OooV-ECFK84mMmr7GJcf3w4964UZXDp-O3tA81-tgXbNdWUXJSv42zbAlqHWfSEYDBLByiXtrbRGjvRmx06sGecxGujQn_37QuZLdlfD2kyqN_6g5juLv1gRq94FtISgsnb-mEbcBZdDdPynkOdkm70n8RHGW7sAPPD4JRC-T9ClAhS9pHwBzYqENEeexYy0m2iHCXvuY8ee__h-wBU4Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه دردناک سرقت تلفن‌همراه پاکبان در مشهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107119" target="_blank">📅 13:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107118">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wi0Yo-amh9BiwvkzPfQvN3wXows9BO9ntNoM4RHg6leA-c44mJasz64XqcVLmFKIRJ6SsE2nXeHvJxJNuVF1Y-DnZ7tmC4DSQ8qxZ_VPXYnGxHapnmNR5EdvpIpzQDNAUGWZIUfKUu4ZFp19VADGBSqzb3mJOwIBrnQBZBvGoSl5dkd6iTePdtz7lwLWrkF3QMdqJZ8EurZsi6juOWhjbtQP9yH4F5CN2MCZKWkxGeJ_scdMLSNfK0NY_1HKvdB6-aEJ0x0DgeCTv76ujApG5yiioO-9KaFNBRVmGxwgr3iS9u4HD7tziWmCnwOd167MdidJGnbu8-Oj2-lBLpkWyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
📊
5 بازیکن برتر در زمینه خلق موقعیت گلزنی در لیگ‌های معتبر اروپایی تا به امروز:
🇪🇸
لامین یامال – 6 پاس گل.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مورگان راجرز – 5 پاس گل.
🇫🇷
خاویر هرناندز – 4 پاس گل.
🇮🇹
پائولو دیبالا – 4 پاس گل.
🇪🇸
آنتونی گوردون – 4 پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107118" target="_blank">📅 13:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107117">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9qNQZYtWMHtiin9_WA9OoV5QplssT1KfcHjx1aV6UQl5oXQv5HmW4d2oW1Brf7Ymeph7e-n_dtA3ojuAkXWv68ww0MuFrfJRubUDYqdAXBuL37XnfetWB9g6CCpjVYcp_e83TetgBo37WWNG6HZc3cTWyLh44Hci7WvtRrdDIMBLDGoAoR4bm2XeR8cWPVHs_MNaa1dmZjj__elYpPswjXjLICCdbLsft5LB5761QJgMJWo1InJ3ZbrZ6sqVghPgmBtNc-11Z4trrksDTmjXHxHeJOK126J6q39XxNfGRF9unxU9XGULZG7Bh0U9TBhMUr9-T6x1l8GhTTBGyzZtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خاویر آگیره سرمربی تیم والنسیا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107117" target="_blank">📅 12:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107116">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5MTZWWnJaq6V6phR6aAVQmFzfmG4ikMbSGsEh5cdDMOjKwMaUN14hJZ1gJLEXRNjOru-fTkoVZLpbCRa9bVSlJnAi0oh9c53IW2Rj4U_y0_OCs5L79udxyyo39amjbWqsyzwTXY8b-eRRcXClNRwL6LaGt-1g3Ls9fpnIbi2ixNUATFLHIEu2eQAa58Tg9XobnXdFQUfTEG8D7Z54E6qbLHOcDNwLJidv28W0cdAeG-3ABoLSD12umKALR-3f6Y2ot3-F91Pauk7tcUvvRVwwl_1JMItofQ2J7BenKVEaJAYxDOpdMz2cy7WzJcCaiO3VAyVo4T1ayVxZ-Ddt_vFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⭕️
#اختصاصی_فوتبال‌180
🔹
با تصمیم اعضای فدراسیون فوتبال، حسین‌عبدی پس از رقم زدن فاجعه در ناگویا، طی روزهای آینده از هدایت تیم‌ملی امید برکنار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107116" target="_blank">📅 12:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107115">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvTiKjcsUHmpl4kVyxLxqulYGofAwPcgl6geVQWga8sjRAFn8m3qgrtWWw3YmNZ-r3G8DStji7rBJZQAwyN_MGIndQykK9MgQMTYxmDmN7sEpO2rMOEK3CJ4rYfWR_XW3hwlDxNwrmt3QbPk-kH2KGLTATcgM-za2j3khKG8U7k9ZHtoixBZjqXihv2a7CNE76n-KaH6sTdKe29w4UGrwvECCBrQbcQqkNm1_hOuwxeF787xRFjO482J8YWTWNwn-CUT0FSS2DyUVTAc3fVsTfIobYJUgNHtrJwnQSYEEHliYmpO35LfVvZ_PNXgXodDK8PAokeF2_Pus7PNJvH5oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خداداد عزیزی از اونجایی که خیلی الگوی خوبی برای بچه‌هاست بردنش یه مدرسه تو مشهد تا زنگ آغاز سال تحصیلی هم بزنه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107115" target="_blank">📅 12:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107114">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6MkRcuylzLyuX-tDjJ_Esu3gxaZLLPHSNA54iRexoOdx8GPDuxmgvSKEIJylwqosiquzLBa4cOHw0-kl7WP2abgCpNjsujsww9Y31rcXdxLYjhq9345d0ip4Q5QfUZmZVWkSLBkPBaNzqHkPVX-Lskios09M8Xnsycqu564URO79LuVZLHo8ZZD5POx-xNAq8BVPt8nnwJAj9IG9Kv1mufaGWtdV-a963zTthqmEQ9vcwaUaa54M00kSvHdTk3b5GqFr3LzbsA053WmRNjKCyWaS5u6TZ0oqBC5FJsm7ncG49YShb8e3VCSeEdaG-IFMAJMU9D522rslKKSVw6S1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
کیلیان امباپه:
🔹
"من نظر شخصی، سال فوق‌العاده‌ای را سپری کردم و این مهم‌ترین معیار برای جایزه توپ طلایی است.
🔹
من نسبت به توپ طلایی امسال خوش‌بین هستم ولی اگر برنده نشوم، ناامید خواهم شد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107114" target="_blank">📅 11:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107113">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53478857b1.mp4?token=AowtP6OmqcUPhOzr3lYw5fN-K9jHwzBnn0daLnEjflRaKwIySu1u-r4uHEOZgBHOEeZmu-1Ic53znCfWnv8Ld-EEt_vZVGTyHNKfSQ6MCmi2mnsPRHXVGRnJgH1tGzk7W26cOnkleAszMXSabEHF7EBxeljNp-zHAk73HYiD-b97JbjHhaH039EaBdAFk9fIkyZrJrM8tnmWPrwEMgKjfY_7_tSz25GiWrxVTFUw7utf14U93YIixJKNMmlMkAxO3KR0QNKcHvz-tbxRDLnA79AAI5_FJJk6SaOHLjUIxlWZf8GsuKmccF29k_M90hY4jARjbf0hXwWOIOVaWhiLSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53478857b1.mp4?token=AowtP6OmqcUPhOzr3lYw5fN-K9jHwzBnn0daLnEjflRaKwIySu1u-r4uHEOZgBHOEeZmu-1Ic53znCfWnv8Ld-EEt_vZVGTyHNKfSQ6MCmi2mnsPRHXVGRnJgH1tGzk7W26cOnkleAszMXSabEHF7EBxeljNp-zHAk73HYiD-b97JbjHhaH039EaBdAFk9fIkyZrJrM8tnmWPrwEMgKjfY_7_tSz25GiWrxVTFUw7utf14U93YIixJKNMmlMkAxO3KR0QNKcHvz-tbxRDLnA79AAI5_FJJk6SaOHLjUIxlWZf8GsuKmccF29k_M90hY4jARjbf0hXwWOIOVaWhiLSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کنایه گزارشگر صداوسیما به قلعه‌نویی و عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107113" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107112">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUnT10bd5dFwgPCChu5QaFglOiR7uGR19Un7UrmVUH9z2jjKnJdertByTktQJyUtbvtTwWv-EkLrU-pXMIdOvZnwVMrStOz2bbpY8AYm2-sQbvj7heGxAluY9CbiYpYaRo4Cr0eWVorl_bC-X8UB_d5FehfHW0gXpEUGvAzkx_4mZG7U4RozTL-hqCSWSUCCUwbMBRKUOAsNE0w6AZkjRSTOZGq1fvxJpUG_sUmypf7s1SwusITBOa-dc9UgQHR1Y5aOrsoXRzUuAzIb5tw06-z4SXlqZXSw30dIrPa6zOfUIGcUokcXcbj7EhTBL-uw9U0LL9XPNKxQDfRe6boAEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
رافینیا:
🔻
"به نظر من، لامین یامال باید بدون شک برنده توپ طلایی شود. او آمار فوق‌العاده، افتخارات، جذابیت و کاریزمایی را دارد که او را برای این جایزه واجد شرایط می‌کند.
🔻
به نظر من، عملکردی که او با بارسلونا و تیم ملی اسپانیا داشته، این موضوع را کاملاً واضح می‌کند و او شایسته این جایزه است."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107112" target="_blank">📅 11:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107111">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107111" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107111" target="_blank">📅 11:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107110">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frH6bi7ztzzxYym43Z9T-jnTnaUbmNFLRv1dJ6LukVoGbMNcA4aohGoOU1dHWNEzjKjtUwhCBIQBhyHb3uCaFfDZqD9iRLDzC7c7mgKqrWqM5IhaHER0uh3Z-iAy5O9v_t_V-tat44BnVL9QRKeCLa08XJjwPXhjkZpFPJjgMhxcB80NNE-HwOL2lrnZjTIm2cWZ-hA4U3iGW-UavWheYs6pe70UbhdFAbtMWBbz2SQIomkmfXNkx2GxjMOjVQZ2W7Qamq20AXSzGkFzVoeWOK0M4T589umieXwpeXYKQbU3BY1O2D5I0b7struLTqx9b6SVFBAFj0I-bLtypJqNyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
هیجان مسابقات DOTA 2 را زنده در
TrexBet
دنبال کنید و با پیش‌بینی دقیق نتایج برنده شوید!
🦖
پوشش کامل تمام بازی‌های محبوب Esports:
‏CS2, DOTA 2, Valorant و ده‌ها گیم جذاب دیگر...
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107110" target="_blank">📅 11:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107108">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9548a0e3ec.mp4?token=O_FrYYSS8d3Q2tAJXiCMPezzHxS2QZaeFIuwb6DXe16q2VIR6TazCroMJhTqLlNr2J1ouRpmhIOwGgUylZl4WofTJQVb8qeMJ6Us49D6IpzVHRpXvyuZDlRIcHlM4AK_E93HRyiRFWQGcErfb_hYwgdwikAYjep6_2Af5VHL0k3BxoYV2JANgFReS437M4X033Xhjksiljq9PJc_qG-iZZGHMcRbNyfBnUD6NlxQImMiyHb1TR-O6bJGrtg0caahKr3voznK77sHfXi9Ko_LTpCWuM8_9fImXn1FgtoCeZM07IHoS76QmF8LlJvUpLErKSWk6EkYaedYH3AG1OG7DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9548a0e3ec.mp4?token=O_FrYYSS8d3Q2tAJXiCMPezzHxS2QZaeFIuwb6DXe16q2VIR6TazCroMJhTqLlNr2J1ouRpmhIOwGgUylZl4WofTJQVb8qeMJ6Us49D6IpzVHRpXvyuZDlRIcHlM4AK_E93HRyiRFWQGcErfb_hYwgdwikAYjep6_2Af5VHL0k3BxoYV2JANgFReS437M4X033Xhjksiljq9PJc_qG-iZZGHMcRbNyfBnUD6NlxQImMiyHb1TR-O6bJGrtg0caahKr3voznK77sHfXi9Ko_LTpCWuM8_9fImXn1FgtoCeZM07IHoS76QmF8LlJvUpLErKSWk6EkYaedYH3AG1OG7DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دیدنی تیم فوتبال الکترونیک ایران به حریف ژاپنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107108" target="_blank">📅 11:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107107">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HX6fJ06zYwKZkXvG1SZ1RQZ6AusCdyhi-me_F9aEj8coFM-H3HlmAXYJ7EKJ-KDFBPi98CY1zJNX2PqescC8qssWrqlYrxiRrrDjK77tdY8Pd7xeZmw2emzn3y8_msFSCZgvxucRKPky4_zwQ382iJrkIvH39gYWp-2XqjMaDe0TVMrGtfjoYEnHTXUOwIN6ZslyDtZdtbnOld3cf8MRXJ9IP9MS0_dhmyYmHhHyO5R0FEBH_j09f_SxfFD2axAgLm88xnPEd0bNGaL3eLg4W8L1N8Q5Mps7WER0WwrfdFUeKTUOsuRKCgTDB9u-njIpUVTRsxjRY-XXGsCEEaURFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⭕️
#اختصاصی_فوتبال‌180
🔹
با تصمیم اعضای فدراسیون فوتبال، حسین‌عبدی پس از رقم زدن فاجعه در ناگویا، طی روزهای آینده از هدایت تیم‌ملی امید برکنار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107107" target="_blank">📅 10:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107106">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g79s9z-WR0eb7pG6Y_-1UhM9WYcz5WZla6pBs-cX-MTz8iNVS9mZKoMlHOetzxbcOYp-vUqoHGkePntsPeYHnE9wRfl129Mvnc1Ulv1kFK1azx7jSyatWXVTwQQU-g5-nuv-mghNVTMdD_OOrPFT-zn_GqC_Ap836vXWitkZlOh0eLSkmxWcdf0GNn6H7hteAzQmlG4O6Jb51gglNuXOr2KTHafKsmQMib_QXw93W7oISJjgBLFyue03QxepPN8JEBaeh4fdE98D1sm9ptdrA82Bydgobk8LHSMzbf5Uvm6tVoYl9FAeJLc0ZvnVemQm514j5ZDEP9RwIrGgWtHZgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پایان‌بازی|شاهکار حسین‌عبدی پرادعا در ناگویا؛ ایران با شکست سنگین مقابل پسران کیم‌جونگ‌اون از صعود به مرحله حذفی بازماند
🇮🇷
ایران
😃
-
😀
کره‌شمالی
🇰🇵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107106" target="_blank">📅 10:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107105">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HD9WYO4-cczQI3TUu4OVWU0HjprzccWmEJGvEKnpIhPiKv2MyrqUK-z9lwmS4jFthsOevheR_xe9WIVbxZ7S6Xg30lgOSooFCnwsIuqKRmwfk4QKJsqrBHCiEUHjLBRArnNdGqR7H5P3Uo469t2zD08nYRRT0bUCMAbKLOIoLtVdTiO_-E7x9rT3NaRgDvw-_D9ogF1Py8llR-W-P1SZpLC3ElyDgXISpLiCnVVshS7Fon5sD_IQZvTSvihI8z8RjZBitdb5N-R5kR0hSWkSMDHY6cd1ecHArmcQoNlhM6IE07pbRZzCZdAVUzvrdM_wOPQeVjZJoFCaVprEuuTbYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پایان‌بازی|شاهکار حسین‌عبدی پرادعا در ناگویا؛ ایران با شکست سنگین مقابل پسران کیم‌جونگ‌اون از صعود به مرحله حذفی بازماند
🇮🇷
ایران
😃
-
😀
کره‌شمالی
🇰🇵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107105" target="_blank">📅 10:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107104">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65dff3514a.mp4?token=Tyi2iMNgj4aT4LWy8MnR2gHw_aIC88wDZih4F1N_8C4jLg5oKDkcLVvfPbIhYUU50Abu0Dp6akOO0Tsu5lflCUjufVzx68oJkdJR8dT8-kIs0xTRTrEysgrP1H0PMLFBcbquy5GujvJSQIHJW2tpjS6sSLcfg16IO5-A366eBUIAydxO4w3Ua5sSCRsgeJ9a4DIDBsdeRoOP5GVUPac1H3JP4NtSbzY4R9t05NiJ6UKXU6OTIoH2Y2XT5QqIdbe1AoIJOmjPj7i2196PjKHfEfwwrjXBUPETTDu101wKUUzk-F9a_qRjGpuM90UUICFGLhgukybm4YqqpwXiI0z12A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65dff3514a.mp4?token=Tyi2iMNgj4aT4LWy8MnR2gHw_aIC88wDZih4F1N_8C4jLg5oKDkcLVvfPbIhYUU50Abu0Dp6akOO0Tsu5lflCUjufVzx68oJkdJR8dT8-kIs0xTRTrEysgrP1H0PMLFBcbquy5GujvJSQIHJW2tpjS6sSLcfg16IO5-A366eBUIAydxO4w3Ua5sSCRsgeJ9a4DIDBsdeRoOP5GVUPac1H3JP4NtSbzY4R9t05NiJ6UKXU6OTIoH2Y2XT5QqIdbe1AoIJOmjPj7i2196PjKHfEfwwrjXBUPETTDu101wKUUzk-F9a_qRjGpuM90UUICFGLhgukybm4YqqpwXiI0z12A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل چهارم کره شمالی به ایران توسط چونگ سونگ(68)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107104" target="_blank">📅 10:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107103">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گلگگلگل چهارم کره‌شمالی
😐
😐
😐
😐
🚨</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107103" target="_blank">📅 10:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107102">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c68b593c8.mp4?token=oZYkXCqq8qy62HouozPZAaLF1GEv7ELjoNN91nhNC1n2nffKKz5Fa8i_rbp6dOCiWJAl4usoVTiVKloSCgiL0tEByqNnlS2uMAAoUeHx4L17VeMgW0UFC1tRG9HpKXWG_lu_nsU6yVpJ1a5Kl-nV2qbNPXXYbpJYLfSnr4WtgJjum0Eja3YeoL1TrUXKkf3p7ek3h6o13uHw5Lldau5atcTOruqe0u4eIsnRU46qMgIlmKOoKX2xezju6ItceOCdVMphYW3HTHj8peblSpZRi2TPiutlQW_HjKcZQ9deqcEtUbOOQFSruXGvFgsgR0-rGrBH0q-gsS2_Op8GbBfWeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c68b593c8.mp4?token=oZYkXCqq8qy62HouozPZAaLF1GEv7ELjoNN91nhNC1n2nffKKz5Fa8i_rbp6dOCiWJAl4usoVTiVKloSCgiL0tEByqNnlS2uMAAoUeHx4L17VeMgW0UFC1tRG9HpKXWG_lu_nsU6yVpJ1a5Kl-nV2qbNPXXYbpJYLfSnr4WtgJjum0Eja3YeoL1TrUXKkf3p7ek3h6o13uHw5Lldau5atcTOruqe0u4eIsnRU46qMgIlmKOoKX2xezju6ItceOCdVMphYW3HTHj8peblSpZRi2TPiutlQW_HjKcZQ9deqcEtUbOOQFSruXGvFgsgR0-rGrBH0q-gsS2_Op8GbBfWeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇰🇵
گل دوم امید کره شمالی | را میونگ سونگ '44 امید ایران 1 - امید کره شمالی 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107102" target="_blank">📅 10:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107101">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23009325d2.mp4?token=urp2hmC2evpuEwwbQ2zEyrm9Nl2mGCS_Ej1G1lyLoPbZleahSVKA-w1BeuP3aymfwG9XE0S8Hs48POj1lfHoCgpLEoVyVhoL6_wS0afpnYUa2-3TrXqSBRPBmgaqKHXn2Hd3R16w0z6RuqHLAb6lWXtQ-UdCvj3wgxstpqi5fDE0sxykc5qf58Rzh9Kox6YxhGPpWUr-k7OoITRjy0GMwhJMfKPIukNSMv8na7VtY0jSC6Deh6tZXs9sSrS_yBJ8XhK9Hh8aaUKC5FXQ9R8iLC2YWZE9kqVDd9Wt1Z_hGW78BtrqkwmcPvxFjRHGNAqOewSrs_0fLjjkgpZxnypB1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23009325d2.mp4?token=urp2hmC2evpuEwwbQ2zEyrm9Nl2mGCS_Ej1G1lyLoPbZleahSVKA-w1BeuP3aymfwG9XE0S8Hs48POj1lfHoCgpLEoVyVhoL6_wS0afpnYUa2-3TrXqSBRPBmgaqKHXn2Hd3R16w0z6RuqHLAb6lWXtQ-UdCvj3wgxstpqi5fDE0sxykc5qf58Rzh9Kox6YxhGPpWUr-k7OoITRjy0GMwhJMfKPIukNSMv8na7VtY0jSC6Deh6tZXs9sSrS_yBJ8XhK9Hh8aaUKC5FXQ9R8iLC2YWZE9kqVDd9Wt1Z_hGW78BtrqkwmcPvxFjRHGNAqOewSrs_0fLjjkgpZxnypB1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇰🇵
گل اول امید کره شمالی | چو کوک '41 امید ایران 1 - امید کره شمالی 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107101" target="_blank">📅 10:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107100">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/663cefc9c1.mp4?token=K74FD_4HSq901mH5Kp7a59wfSmP2hJ4JGKL23LrVK9ULK3_EHH6TLrH858LH41-Fa1d9OMrqr36hjgwpF5eE2I0tZdGuWajCJtU7dILFSPGeWrDuFelWBtaK9zeRnNj1Zeuey4v19M8WiAXC49WLn2VlPPwbNdxqGA7E9IMM12FgQdqK0-ELl77O5tFyPDBg-QQ-QRE335gnHBfgW3JhImi6s6ZkLMhCtp7wfkK8ZhzBB2hRxyEVgF_EwudibmtFIq5-Ae03mlIKpy-syBgBjS9RGHrt-tPifdwHdln3jtpFT6QRX7lfMuxqhrkUvA7ttXG_p6smKjowScYtIP4cCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/663cefc9c1.mp4?token=K74FD_4HSq901mH5Kp7a59wfSmP2hJ4JGKL23LrVK9ULK3_EHH6TLrH858LH41-Fa1d9OMrqr36hjgwpF5eE2I0tZdGuWajCJtU7dILFSPGeWrDuFelWBtaK9zeRnNj1Zeuey4v19M8WiAXC49WLn2VlPPwbNdxqGA7E9IMM12FgQdqK0-ELl77O5tFyPDBg-QQ-QRE335gnHBfgW3JhImi6s6ZkLMhCtp7wfkK8ZhzBB2hRxyEVgF_EwudibmtFIq5-Ae03mlIKpy-syBgBjS9RGHrt-tPifdwHdln3jtpFT6QRX7lfMuxqhrkUvA7ttXG_p6smKjowScYtIP4cCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇰🇵
گل اول امید کره شمالی | چو کوک '41
امید ایران 1 - امید کره شمالی 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107100" target="_blank">📅 10:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107098">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b315f04dc.mp4?token=qBzq7oLsYW2QHesYNCtqBqmW8EhmEVjH9xrEcPlBfyCeiH4rEsJ-hWUC9WvjpKROJtM5efR6Vl7yhh3aZ8E81UgVBNYYsLDg1nS5sWm2sxqORhIoop7S17kru38YgQbfIZFLq1lSQSk7v_082PNZmMr1okhx1VHsc1Ynhr2fnBzbps2dIJJCfs8qTbV6VSDPNLRgAtCzOOg8q3uW4-tA20p1_emDTBaWWAPtGS3BTr9Qxc86q7ovyQRt2OmXTmy-y7qfh0FK8HnDSmCG_nucVh7y2RRMZVm-vYp9ESowObWZ7QYBXNrpgqUlVHbA1MqxTFoDxaZa14sBY3B5ZivefQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b315f04dc.mp4?token=qBzq7oLsYW2QHesYNCtqBqmW8EhmEVjH9xrEcPlBfyCeiH4rEsJ-hWUC9WvjpKROJtM5efR6Vl7yhh3aZ8E81UgVBNYYsLDg1nS5sWm2sxqORhIoop7S17kru38YgQbfIZFLq1lSQSk7v_082PNZmMr1okhx1VHsc1Ynhr2fnBzbps2dIJJCfs8qTbV6VSDPNLRgAtCzOOg8q3uW4-tA20p1_emDTBaWWAPtGS3BTr9Qxc86q7ovyQRt2OmXTmy-y7qfh0FK8HnDSmCG_nucVh7y2RRMZVm-vYp9ESowObWZ7QYBXNrpgqUlVHbA1MqxTFoDxaZa14sBY3B5ZivefQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل‌اول ایران به کره‌شمالی توسط حسین‌زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107098" target="_blank">📅 09:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107097">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1971f21e3.mp4?token=tHr5hB_NWQmRbrXWt_P9FQPxYcehtmPSqghgwWO0dFzWlu-X9mlxoHQnyDgY5GxtQFsb1ebR9BCHeO7NWHmnSjC_gfkq6Kv2O2PgFpNGo9GwcRLcKeOUMkmI8OKX6jaLfmMpw1Itu5w_GZcTISm-qXQYhOx9Ukd9MUqVc_Wn4gSdK8uzcJ578y104iY2C_JTALvj3mD_IVyqfMtIRB7Wei-Pdcuw1f7IyJB5V-_8q3i4Pvw1PvpIP9KQspk_yRXw7cmD7nly-FZYPIbTs-XuxO58AwLyZnDnEx1Qxh3viQLph0zxH0jTEqoX9YYZucG6pSc4Ega9jbxXXnL6tAsYKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1971f21e3.mp4?token=tHr5hB_NWQmRbrXWt_P9FQPxYcehtmPSqghgwWO0dFzWlu-X9mlxoHQnyDgY5GxtQFsb1ebR9BCHeO7NWHmnSjC_gfkq6Kv2O2PgFpNGo9GwcRLcKeOUMkmI8OKX6jaLfmMpw1Itu5w_GZcTISm-qXQYhOx9Ukd9MUqVc_Wn4gSdK8uzcJ578y104iY2C_JTALvj3mD_IVyqfMtIRB7Wei-Pdcuw1f7IyJB5V-_8q3i4Pvw1PvpIP9KQspk_yRXw7cmD7nly-FZYPIbTs-XuxO58AwLyZnDnEx1Qxh3viQLph0zxH0jTEqoX9YYZucG6pSc4Ega9jbxXXnL6tAsYKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
دلقک‌ترین استاد کسخل در تاریخ سرزمین ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107097" target="_blank">📅 09:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107096">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/625edd4ac9.mp4?token=fzIJmVl0Ak3tUAIQA3SgSUGMo4VIxRQfCRzNBf1t3PwHm3FkizzOreDoUG3vDNlorYK60KQeBzNuUb7HTGEQB_JI76DO-Xbil8AzaR5jkTE7ZTACOuYf5oFduSKC_B0e6RyiDFU5I97Wv3wLx11hMCIVb2D9EltDIrIyYuVqYK3p-QoGUPLR7NrDkVkASHkoot5-EqDSWTT7N1XsNHzgcicxr4XQRrcyoD3zEDt508sQiSQZihKukesZk1PjYZ_78XnL5Pas4cWWfqG6_Ch0AA_noAlic-krL1lWLbbbWTkpoO2j6jVD7wakNJ1wZyZwMHMYkdTEaci6qdTGAYnLMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/625edd4ac9.mp4?token=fzIJmVl0Ak3tUAIQA3SgSUGMo4VIxRQfCRzNBf1t3PwHm3FkizzOreDoUG3vDNlorYK60KQeBzNuUb7HTGEQB_JI76DO-Xbil8AzaR5jkTE7ZTACOuYf5oFduSKC_B0e6RyiDFU5I97Wv3wLx11hMCIVb2D9EltDIrIyYuVqYK3p-QoGUPLR7NrDkVkASHkoot5-EqDSWTT7N1XsNHzgcicxr4XQRrcyoD3zEDt508sQiSQZihKukesZk1PjYZ_78XnL5Pas4cWWfqG6_Ch0AA_noAlic-krL1lWLbbbWTkpoO2j6jVD7wakNJ1wZyZwMHMYkdTEaci6qdTGAYnLMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
هیچکس نباید قهرمان شود؛ خیابانی: فصل گذشته باید از تاریخچه حذف شود
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107096" target="_blank">📅 09:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107095">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107095" target="_blank">📅 01:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107094">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/107094" target="_blank">📅 01:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107093">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TS6JS4AwssD3MjMeCQKX1p2GLgrw1CPNNZeR_nirh2vcB5lKDAg37nHYE_H0oiGJuu2cOgsNqGEvKIxjXKCIh-dNWf3buOYMymd0LYTQkCV_1YCx0P__e0DCJWeI0QQAEPwpxisHH85DGyBSgHFhq6NVKZLYZr9PjvtIr-DaFLQd1MmmUbzGJXOhNyRaxC9WhonJ7Mg9s9CZyRfMvZJGu3PtPBWVs_qtUpC1jT_LY6FNW40ss5_xbyLC4X9avmbDoike0zJ6O2RjYU4ujvit--CjbfgVoz8UOmIaqrA5p9TWV82bfqi7imalOoKWOkGaCPAU5rXRTSYD3eqVTksLPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو اعلام کرد: قرارداد آرتتا با آرسنال به مدت ۴ فصل تمدید خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/107093" target="_blank">📅 01:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107092">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5Wxah3Ohgr6rsrMLMD7gKsgSKdXsaerzOk9LXujUOIMoQAF4QM67JD0YnKQbmLvRK-_iVscFtLK4Q8zKpFanePJKBWQOHLHBw_xB5nUOA9TkOTjUlhjsYZ5_ulxVejOsu2lP3_jpyBL7uJPqQ-4PXk6d592OlSsD0DSWy36JNdDgFn0SjFPASLzeEhfLGHQDwgq9l9dxPUnacQ1XP4GG8ZCkCErdSaGg_SSL6fw3w7snRANsV_Z5kOmjSr48KiMooA8k97B7IXM6pvpp5k0ohpayWONUzzhI3Bxu-1Fhs4JxCVrqC0FHFl5Rw7HJUWKaStF1huq6zB0fnnwfqfn2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🔥
بعد فیفا دی عجب روزایی داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/107092" target="_blank">📅 01:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107091">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ka4oRmJuo5rjaT4lRt2LAezqc5a04yBZhcMLwbBQZl94N5S9LZ0F67Zhey7W_HXJsmfCPzVRn8-6usmxi8Zd_yVn5irRuW9EGNKADP8EC6yPWZaNtpNeh2ANZvJVg-GDej-iFLXY8LxvVPljsdAZrMOcHCVufBTtCSTQ_X2Z9cUEeDIiWGFe8wXUJzh0sSHf7R0X6v2KJrCueDFTNGkDlCn9dlFb-VDZXKMbeYBCuyV9eZzSu5JGk1DIeQ-bOTyeh49i5J-jGLiORpsXCrmrUC6tSBqzUoiTvLvTO4pJqMhLPrpjcHo4V6o4YLrSqCsL-uekJEkxQJAA49MCGXTstA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیفو سکسی عربستانی‌ها برای بازی فرداشب با کویت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/107091" target="_blank">📅 00:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107090">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_ovsDT_H_rS0d2GdiiU6l9mj04MiGqkad4_x44pYY8usjq73Eh2F4IpFvvszGmBYoVbwovk79564oJbEed8k4n3LJpbadEuJ82Pl7Fmlp4ryhB3N0beIsJ99oe4hut8nvsPQAAG3JjV6O3eg2HXW6lRlNyJ04BblFA3WUtenKxUJRNd7A6pYXxbMdU-1HRBSOM9utZppUnVyCexbGEYOyGR7ptZ0cFbsdkMXQq78bdVbgJXFdligQ1XhdJucjEFtWPHoiQ2O5xNsQjP_-0n-sSyaD3X53WiZzBTVJnCYM2AjgO8QQtCOVH1fHicxrvyctBYZ4pbairgEw1wZKc7PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
عراقچی و ویتکاف در حاشیه نشست امروز سازمان‌ملل با هم دیدار کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/107090" target="_blank">📅 23:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107089">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eec872952d.mp4?token=bL-W7lkCpgHUOvYzfADqM3TR5JimlhwC-zH7m5XuovqSfGI5JBtNtc8rT8kJ24RmrAt4y3BLchRTbj40ja9ydqgzk5mFNe5pEQwQocEgpZ_ts2KzsSXlZyEr8x-4fz65KwP7CVUmYhazYQ_00rVBOJnVZEL3bavuPfPc3XuaIBEJUckX_FgBcw2m9JpVjQJYppq5D8trDzs7fsg0h1u0h5t4QA5hkvBGqFURBp7mScwGWYkAElVEHihAMe291J4wogomtIxA73ldPO8PRna9Ia1HjY27607aLFomJXBJU0Hy-Lj7fLtXS5PLLhfpgL414Bhv7aArsCt1AgaRqLdhPzbQ-BnUjF0L3jhQ7MPiaUyBfK6I4UF1djFlFmr09eufRLtjswNdg3XnEBINYRaG6OeEgOyZODsMRK2aX3HqHYY-yYzFkxIHF7kgdcyFv1PZVNMt--UBYwS5PBU0GzmYzeYrVdRtlKq9D-Kvy640Uo1wA9cq5ZhaLXsRoJVbsU3RjP3JV1NZq15FDYIuo-3NfgqV9wt8Vb9v0qbGv9rxT_G1E9shQehQb1llhhYjJAybJDwaNK8EOsHUr4ap92y73SQd2_HnXym5pUThGp5wEKUSnrCUqF_6BBuJ7UM-5lxiJ48jDWdJdhGnZUdQUOmprp6Egy-XVd3MjCgDPt6rp94" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eec872952d.mp4?token=bL-W7lkCpgHUOvYzfADqM3TR5JimlhwC-zH7m5XuovqSfGI5JBtNtc8rT8kJ24RmrAt4y3BLchRTbj40ja9ydqgzk5mFNe5pEQwQocEgpZ_ts2KzsSXlZyEr8x-4fz65KwP7CVUmYhazYQ_00rVBOJnVZEL3bavuPfPc3XuaIBEJUckX_FgBcw2m9JpVjQJYppq5D8trDzs7fsg0h1u0h5t4QA5hkvBGqFURBp7mScwGWYkAElVEHihAMe291J4wogomtIxA73ldPO8PRna9Ia1HjY27607aLFomJXBJU0Hy-Lj7fLtXS5PLLhfpgL414Bhv7aArsCt1AgaRqLdhPzbQ-BnUjF0L3jhQ7MPiaUyBfK6I4UF1djFlFmr09eufRLtjswNdg3XnEBINYRaG6OeEgOyZODsMRK2aX3HqHYY-yYzFkxIHF7kgdcyFv1PZVNMt--UBYwS5PBU0GzmYzeYrVdRtlKq9D-Kvy640Uo1wA9cq5ZhaLXsRoJVbsU3RjP3JV1NZq15FDYIuo-3NfgqV9wt8Vb9v0qbGv9rxT_G1E9shQehQb1llhhYjJAybJDwaNK8EOsHUr4ap92y73SQd2_HnXym5pUThGp5wEKUSnrCUqF_6BBuJ7UM-5lxiJ48jDWdJdhGnZUdQUOmprp6Egy-XVd3MjCgDPt6rp94" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇫🇷
اولین تمرین خروس‌ها زیر نظر زیدان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/107089" target="_blank">📅 22:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107088">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53976f40f7.mp4?token=tDsEzMlVyV69unu6E9VJYF3_-xU-V3kshLjds6iKmi7YxDnRtjiLgaiVQwVrXm1rbDV6f5SBaXO2iCR9nqW8aI7hcAPrTnUKUFXraDP65XNSDcWmRWLyTnfhbcpOegbaX4WucujRtbQ-zk1VU2MjPi-zsEmUQqcD7CGcM_LkfvNLSWIKFn-M7WJgenO9vASRt3_WL_5kFbiKR6A3gyk7vvJpJNkm2-twyS71IB_fHPn-N1ceYtLhzrH0IuJpJFr3GLwyKeKouazrc4PIWTRfAfP4DPB_LTbTEk615uX64irdywV7Y30Sbh9WWWAY5oXxNAz2tyqJ90JBec6w-gMYg6deHNT6lF2KfwZALBWQ7LS9R2N9iPhEiF9CPAfSuadKjU4rwHOjQ0jiMz6T8xcH2lZEJ0_iOB92CT1QcqifuOFqrXLCl9UdJeqVCx06RjUiygzUwejOcmqGmJcgulz3hiY8UjHCNkEkX10ktOTjbyXjnYfRmna7n7yzm6nP7nrgnnaT1016B4yRWm3PYoIl5GVMhyG6zSiqmOGXsucvCTO5H8AL4nvAzfBLT9A7lCxCYujzCzgt6STopVDShoGNcqic6L1RQjiNs0SS_3WMwrugMFBQmJ03GhtX1EAB8EwofLHN9XW2Sax56NXMyizqB_OK9sRhK5oXKePScPgSz-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53976f40f7.mp4?token=tDsEzMlVyV69unu6E9VJYF3_-xU-V3kshLjds6iKmi7YxDnRtjiLgaiVQwVrXm1rbDV6f5SBaXO2iCR9nqW8aI7hcAPrTnUKUFXraDP65XNSDcWmRWLyTnfhbcpOegbaX4WucujRtbQ-zk1VU2MjPi-zsEmUQqcD7CGcM_LkfvNLSWIKFn-M7WJgenO9vASRt3_WL_5kFbiKR6A3gyk7vvJpJNkm2-twyS71IB_fHPn-N1ceYtLhzrH0IuJpJFr3GLwyKeKouazrc4PIWTRfAfP4DPB_LTbTEk615uX64irdywV7Y30Sbh9WWWAY5oXxNAz2tyqJ90JBec6w-gMYg6deHNT6lF2KfwZALBWQ7LS9R2N9iPhEiF9CPAfSuadKjU4rwHOjQ0jiMz6T8xcH2lZEJ0_iOB92CT1QcqifuOFqrXLCl9UdJeqVCx06RjUiygzUwejOcmqGmJcgulz3hiY8UjHCNkEkX10ktOTjbyXjnYfRmna7n7yzm6nP7nrgnnaT1016B4yRWm3PYoIl5GVMhyG6zSiqmOGXsucvCTO5H8AL4nvAzfBLT9A7lCxCYujzCzgt6STopVDShoGNcqic6L1RQjiNs0SS_3WMwrugMFBQmJ03GhtX1EAB8EwofLHN9XW2Sax56NXMyizqB_OK9sRhK5oXKePScPgSz-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
توضیحات بازگشا سخنگوی پرسپولیس درباره شکایت از آسانی به کمیته استیناف
🔻
فردا به آقای تاج و فدراسیون فوتبال نامه می‌زنیم و سه درخواست داریم. حضور وکلای پرسپولیس، ضبط جلسه و پخش آنلاین جلسه رسیدگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/107088" target="_blank">📅 22:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107087">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpJGWSaIKZlh2vTau79HSLSHOolHZ14vd9tAtzaQ5ITA6_euEHozTwZNTU7GtyZJUPMKuyDtVU2nZxYVhbF0myX6Y5QCxmdZLEywXM8AM5sS9ywmz-gt4UoNLhDa4UVH7J1Ubr8M4yfthyg0jn4gZESpuBO9wh-Zrl_wXauSJf3mfgtijkusPWuc1Rd4vsarUIB1Cep2V3EIaWafxJrQnga-uw6Ti2UTqekKULzNLLd76lqrxJtgkTslehZO-src5ee_Kc9C7_PY3nBt4nEqFIn6FlwpCcq7XGPOS6bi3RAZ_3aUEkTRa6p4WQegqB3odbxuzx6-7z4TNtR48EV1AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
جمهوری آذربایجان رسماً پروازها به ایران را تا اطلاع ثانوی متوقف کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/107087" target="_blank">📅 21:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107086">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91400e175a.mp4?token=jzu22tKZPuEPnQoq3WAeOcmtUn5WXzCBCdYcYFFAVCXZWgrKFivDU9hsJH5sjqdY8YGKIQXjnN4ZNOBRHd0qhR_jSRgrlwCylagnLsKOj7X3r04Iht--gjjtdqGId43MbLrypQ986wWjEbmFCYC5aonIFz2NqEfCya7JhDfvjNe-CRz_LhF3qG5HFY6iiF6e6rUGbzxgRa9lTmPSIalXDrcztu47eLwstgL-BDdDplvgsHVSPSSvSCYaUclebIWIb02zaFxpk4eSmzhOh-ljIUGX-HmWxJqkrPEZD6FUaKpFk2VAzeL-ndhb4XyXnaeVZFEmsGqmYQdEbfyGNjk96Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91400e175a.mp4?token=jzu22tKZPuEPnQoq3WAeOcmtUn5WXzCBCdYcYFFAVCXZWgrKFivDU9hsJH5sjqdY8YGKIQXjnN4ZNOBRHd0qhR_jSRgrlwCylagnLsKOj7X3r04Iht--gjjtdqGId43MbLrypQ986wWjEbmFCYC5aonIFz2NqEfCya7JhDfvjNe-CRz_LhF3qG5HFY6iiF6e6rUGbzxgRa9lTmPSIalXDrcztu47eLwstgL-BDdDplvgsHVSPSSvSCYaUclebIWIb02zaFxpk4eSmzhOh-ljIUGX-HmWxJqkrPEZD6FUaKpFk2VAzeL-ndhb4XyXnaeVZFEmsGqmYQdEbfyGNjk96Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد چلغوز گودرزی رو داشته باشید که دوباره تصمیم گرفته بره مقبره کوروش
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/107086" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107085">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
تمرین تیم‌ملی فرانسه
✔️
کلاس آموزشی تیپ زدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/107085" target="_blank">📅 21:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107084">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🙂
💥
مسکات حلال‌خور اتلتیکو مینیرو برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/107084" target="_blank">📅 20:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107083">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8c040c455.mp4?token=f04NnNpnfm5SM2sFtTJvb_mHp0Isz9B_vDO8zUB3NvM-aHXTT_pSlRHiJlub22-g6MhWCOtMHRwweeq_n5UAEkUzHz0ez1zbq2-Ywn7tNrwX3AnS3khM_YI_ltEEf7lYaR0RYMKU6-5t3bk5VS4EM3l0LSecWVm5iFiSIUX0__LP5CMHKO8bLdzpSueG-Tg9PwgiHBXcjqA8A9UiFFKiAto6WH_GcYQBBcoMPyi5r9rJRnZbtGI4pCJ41lDbNGppV53X7onINcruQAcKqKXERM_pk0kwdBbYGLgh3mKqOow2WqPYa-XZb9rmf1p1eHTb3nvN4MMFLLZuYljspKUEhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8c040c455.mp4?token=f04NnNpnfm5SM2sFtTJvb_mHp0Isz9B_vDO8zUB3NvM-aHXTT_pSlRHiJlub22-g6MhWCOtMHRwweeq_n5UAEkUzHz0ez1zbq2-Ywn7tNrwX3AnS3khM_YI_ltEEf7lYaR0RYMKU6-5t3bk5VS4EM3l0LSecWVm5iFiSIUX0__LP5CMHKO8bLdzpSueG-Tg9PwgiHBXcjqA8A9UiFFKiAto6WH_GcYQBBcoMPyi5r9rJRnZbtGI4pCJ41lDbNGppV53X7onINcruQAcKqKXERM_pk0kwdBbYGLgh3mKqOow2WqPYa-XZb9rmf1p1eHTb3nvN4MMFLLZuYljspKUEhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
🇮🇷
پیش بینی چند هوش مصنوعی مختلف از قهرمان فصل گذشته لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/107083" target="_blank">📅 19:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107082">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=Ec1il8ykawONxDzJKELzvO2jEGzvcYao58yIBGnL-D45PwAkFZFL4hhput7g6JxYULmMcn4_610CCGD-5Vs_SgO21yva9qcAefeJRbNJ7GgiZtGqWJoID2Zi9TPCSHpb2SUWVUFFNz_5m8OYtb2ZAKEvQxWZKizpoOecJO6zSwVrK0NbC9NvxDUjLoEPMZyj60vrYrkdTz3jrACoKyuPCpr6-Oj0MhVUWouoV-G0jQvezynhgMTglQOu9_4xxd4VlK5rREU_oCllAN728diC5imHx9953YUFK84WfFi_f6H8Jbeg4NYY0QhU-6FRVNG7Exwqq9FEY86FsVsHvcYf4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=Ec1il8ykawONxDzJKELzvO2jEGzvcYao58yIBGnL-D45PwAkFZFL4hhput7g6JxYULmMcn4_610CCGD-5Vs_SgO21yva9qcAefeJRbNJ7GgiZtGqWJoID2Zi9TPCSHpb2SUWVUFFNz_5m8OYtb2ZAKEvQxWZKizpoOecJO6zSwVrK0NbC9NvxDUjLoEPMZyj60vrYrkdTz3jrACoKyuPCpr6-Oj0MhVUWouoV-G0jQvezynhgMTglQOu9_4xxd4VlK5rREU_oCllAN728diC5imHx9953YUFK84WfFi_f6H8Jbeg4NYY0QhU-6FRVNG7Exwqq9FEY86FsVsHvcYf4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
ترامپ: آمریکا و ایران قطعاً به نتیجه خواهند رسید؛ به هر طریقی که باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/107082" target="_blank">📅 18:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107081">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=ikZ86Wee6DTh3bM_2TMhniT0VxonXUEkrKe7aCAoPT74mWUeW7sh20ZQiYJnz1G_Aon9yUOCG5Gp0Wk_npTbK9KijvSBCjhpWUVP7EetzyWGn6b9Tq_uCn0-7-7s35L94kIYQdJuihho9ipp0LqI_lAzvxsdoRhbxHx4kF8dW-W0KciR-bnZeIC-yFybZ38asgH5DPRWXqzF-Gu713tuTgJHcTfAhdwKUZjunO4yOhhjw4eC2WNYnmjPOa7l6fwv-KPzrXQSROtoqGiOPMCYPCyl43R5gHamSX6SPOJOkf59dkVhKq62QXuJOymeXvuyiePlLsKxlYfr4sjNYlFFGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=ikZ86Wee6DTh3bM_2TMhniT0VxonXUEkrKe7aCAoPT74mWUeW7sh20ZQiYJnz1G_Aon9yUOCG5Gp0Wk_npTbK9KijvSBCjhpWUVP7EetzyWGn6b9Tq_uCn0-7-7s35L94kIYQdJuihho9ipp0LqI_lAzvxsdoRhbxHx4kF8dW-W0KciR-bnZeIC-yFybZ38asgH5DPRWXqzF-Gu713tuTgJHcTfAhdwKUZjunO4yOhhjw4eC2WNYnmjPOa7l6fwv-KPzrXQSROtoqGiOPMCYPCyl43R5gHamSX6SPOJOkf59dkVhKq62QXuJOymeXvuyiePlLsKxlYfr4sjNYlFFGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
ترامپ: انتخابات هیچ تأثیری بر تصمیم من درباره ایران ندارد و تنها تمرکز من بر عدم دستیابی این کشور به سلاح هسته‌ای است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/107081" target="_blank">📅 18:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107080">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
⭕️
⭕️
ترامپ: باید تصمیم بزرگی بگیرم درباره اینکه آیا می‌خواهم ایران را نابود کنم یا اجازه دهم به حیات و شکوفایی خود ادامه دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/107080" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107079">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e271237b80.mp4?token=J49ngYmexRuOtn1Bjq_RQZVeySFvgRGjTLtoy9cheaNoTkPi1--RiyV8PYjSj-CoSQN_fvC2esK_qqt5BFhU8bLEi1zrAcxk262Ol-qhK_qqJ-GjGBADJ6OjkqZYrMJtULbXW0RYOuW992rBUNmvxImN7k6BCzwgHXjyisTia87uLpkzE_ouXRao9zKb2Y9q41czhSEzovbGwt_W2yOqv37FevcHSHvGll9RYow1ToKUPLWISu3jnVfiIwAl2Ian3wUnnvVbeq7kX2AvWx2oMl5_2LTnOrm1586uVVKP8QRRQTr43_WHSXs8F3oajgWNcIjx6Jndpv0bBRS4q_Xrwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e271237b80.mp4?token=J49ngYmexRuOtn1Bjq_RQZVeySFvgRGjTLtoy9cheaNoTkPi1--RiyV8PYjSj-CoSQN_fvC2esK_qqt5BFhU8bLEi1zrAcxk262Ol-qhK_qqJ-GjGBADJ6OjkqZYrMJtULbXW0RYOuW992rBUNmvxImN7k6BCzwgHXjyisTia87uLpkzE_ouXRao9zKb2Y9q41czhSEzovbGwt_W2yOqv37FevcHSHvGll9RYow1ToKUPLWISu3jnVfiIwAl2Ian3wUnnvVbeq7kX2AvWx2oMl5_2LTnOrm1586uVVKP8QRRQTr43_WHSXs8F3oajgWNcIjx6Jndpv0bBRS4q_Xrwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
ترامپ: ایران موشکی با قابلیت هدف قرار دادن اروپا ساخته بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/107079" target="_blank">📅 18:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107078">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=ZQGkCcaDwFrfoCCojQxdU7OQDW0NnPfWfMB-ZoL3f7zmcZd75VoSXjSfqN-9y_OE6lKUOlFzcIoNhEKHLhWj8umbNDbXANUMdY4sceYk3xvQcGgrz7dmTsS5_iDJlbAZmUklKvAw8KafftGYDIQj1iVFdTzE8LtrGRFZJy_kbF5xK9NoA2M5FKfMIsAQJKGqBlzoU_noUbasRQL6Xq38VJe4ferOXHjpmy_-7zAypPSlf4GQtN5joEm-cz-pDDG2_ER3JvSc1f9isIKQ0LbVJf-BeFJECvt9alRv9-I_1viCH9IYB4RQ-LPQtn66gbKM6Zp2cOI4_qS-9VLLhQQD3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=ZQGkCcaDwFrfoCCojQxdU7OQDW0NnPfWfMB-ZoL3f7zmcZd75VoSXjSfqN-9y_OE6lKUOlFzcIoNhEKHLhWj8umbNDbXANUMdY4sceYk3xvQcGgrz7dmTsS5_iDJlbAZmUklKvAw8KafftGYDIQj1iVFdTzE8LtrGRFZJy_kbF5xK9NoA2M5FKfMIsAQJKGqBlzoU_noUbasRQL6Xq38VJe4ferOXHjpmy_-7zAypPSlf4GQtN5joEm-cz-pDDG2_ER3JvSc1f9isIKQ0LbVJf-BeFJECvt9alRv9-I_1viCH9IYB4RQ-LPQtn66gbKM6Zp2cOI4_qS-9VLLhQQD3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
ترامپ در سازمان ملل: به ایران در ازای پایان برنامه هسته‌ای و حمایت از تروریسم، همکاری کامل اقتصادی پیشنهاد دادم؛ اما نپذیرفتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/107078" target="_blank">📅 18:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107077">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4439db1dc.mp4?token=WmykRrCslfzCm8uLjOftM_pYKajN4tEWPbjPwJ_JTcKiYkJLOel3OgKhlILT4QRkP8LL3AhfGzLeYDakT-gxLT7zurHMv_S3Ci_QrjFXjDfsJIQk7KF1s1IG9bSIHFCcRHq8f6j1GtSXtYxkkNIdkD65yPjr9py3KEUjXrOl4NflBtt9aZVUqffetnYtT3WBcqdmWNyqFYlTuF5lnCVI8uZscg5osCihDiVs4Rq4yRvHvYzq4QDCsOpEFSueClP3MJLP8DDMAA0N5ZIegBYqswov50UdZeEPv2unXHmRRKhmsTPH6XD1pV-5crBMzcG3vZRUh0N-botjIs395HnSUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4439db1dc.mp4?token=WmykRrCslfzCm8uLjOftM_pYKajN4tEWPbjPwJ_JTcKiYkJLOel3OgKhlILT4QRkP8LL3AhfGzLeYDakT-gxLT7zurHMv_S3Ci_QrjFXjDfsJIQk7KF1s1IG9bSIHFCcRHq8f6j1GtSXtYxkkNIdkD65yPjr9py3KEUjXrOl4NflBtt9aZVUqffetnYtT3WBcqdmWNyqFYlTuF5lnCVI8uZscg5osCihDiVs4Rq4yRvHvYzq4QDCsOpEFSueClP3MJLP8DDMAA0N5ZIegBYqswov50UdZeEPv2unXHmRRKhmsTPH6XD1pV-5crBMzcG3vZRUh0N-botjIs395HnSUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
تعریف عجیب علیرضا علیزاده از نوید عاشوری که موجب پاره شدن دوباره عادل شد: گفتم ازدواج نکرده بودی، با هم زندگی می‌کردیم!
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107077" target="_blank">📅 18:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107076">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e179f3429.mp4?token=YkPI1qDU_1FuDQ-kQja_eOzDhHEQkDooNyfnzYmMTkprnO5tTSjiLCN72xss6JcboxifoqnnA9TSQZGr_6AE6vjUGTrfQD9urgFXPjwjuBlP1GYDBQOmymzn5VL9wsij_th6tJanjTbMPsLyywBugdTaWWMFrUNuhMat6bSiajbBM8C7Tuy4fkTl_TRHIEKVivY9fTG9MP_sLq4YSwy2QYJD2xqXfPOL5c--tqUtt0THNcAOT677q_O1Q1qFSHwV0AirHaIZLPmswZ85KgnVcVWCEEeD2ZxJmY8wh53xrIE_xXqt78aqp3AQ8z0WZ51gRcP3csvvw_vSKzfTkfO9Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e179f3429.mp4?token=YkPI1qDU_1FuDQ-kQja_eOzDhHEQkDooNyfnzYmMTkprnO5tTSjiLCN72xss6JcboxifoqnnA9TSQZGr_6AE6vjUGTrfQD9urgFXPjwjuBlP1GYDBQOmymzn5VL9wsij_th6tJanjTbMPsLyywBugdTaWWMFrUNuhMat6bSiajbBM8C7Tuy4fkTl_TRHIEKVivY9fTG9MP_sLq4YSwy2QYJD2xqXfPOL5c--tqUtt0THNcAOT677q_O1Q1qFSHwV0AirHaIZLPmswZ85KgnVcVWCEEeD2ZxJmY8wh53xrIE_xXqt78aqp3AQ8z0WZ51gRcP3csvvw_vSKzfTkfO9Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعضی‌وقتا آدم فکر میکنه لیونل‌مسی تو زمین فوتبال بیشتر از دوتا چشم داره
😐
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107076" target="_blank">📅 17:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107075">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107075" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107075" target="_blank">📅 17:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107074">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPumuOW20X51-UbQBR3sATy7ywKK0zxs67OSFsNMdHdgX8UenJCQniL2ESYM0yQdnZ_hc7v6rbata5QaL20ataohDlkgCDfoX-klh4pXWfJaIornD9pCpsPY6xvI1VogcKF3Rrpouef30r3kyje-w4wdftS7LNpBaLEzi_5ZgU7VpY7A30L1oVKfZbSApEWr_9isF6EJCYDGTd2m4mw76XLqJ4qlQtNETEYX9AsNdx5FqD_BGZLuLS5pMp7m11fzcDSyaGiy7HIjJSqHNVwi8keWa0rPB-e_vtU6Bqxf8nUPpaVVFUjtQFTp8z2eHUt-1QILuHLeoQkNW56sZ9Xu9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مسابقات
UFC Fight Night
شروع شد!
🦖
یک شب پر از مبارزات هیجان‌انگیز، رقابت‌های نزدیک و لحظه‌هایی که نتیجه می‌تونه در چند ثانیه تغییر کنه.
مبارزات رو زنده دنبال کن، عملکرد فایترها رو بررسی کن و پیش‌بینی خودت رو در
TrexBet
ثبت کن.
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107074" target="_blank">📅 17:18 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

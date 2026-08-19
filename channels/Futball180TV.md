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
<img src="https://cdn5.telesco.pe/file/g7U6J1HxP7dtU5I_fruOC8dRL6CcPjl6zk-sNX2_7oCO78tif3bvlPiL2wvkcDJJmtqwZfbYGrCFoc2uSBsoVPLUwN63cgpYtEvrR8qNVS9brIsIV5qIq_AOSdAxGLi_z0SoyGw9CbDoZwkkssoGxGHEbYA5HT9lHjcHHnW4XGUNZBb5kYnJB2Qbf9iK4ubYhXSllWdsrwPPU2crrUZ6WBYgewllJJWiDqll4EqlUT2uz3lA_06Hky5FEVxx2Od4lesGODVNn9CpXj4fWpiA79tH0ZZy_6Cen8910t2G3EOYKtZgKriZDMAf8f7hNQHhMXmRAUI_QHKh1E1iZ1x0PA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 456K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 22:30:02</div>
<hr>

<div class="tg-post" id="msg-104186">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a4eaad83a.mp4?token=TXXxS3Wu7RjCnJDyOvpAVXM3cl1XpFBqGUh3v72BcjZpNm7SUltOgyh957R_wqa1NMeT0B1gqTEQ5sF87QyaLVNYcrhFouqvWAFC9hisXo2Qdz2d8oysEQuIUm_r2enEgKiO3NDQGH0Bb6MlbiWlhib8eDjQy6liHuzUHHy0c9Y0xFpFnULMQ8U8KFCz6gxlKHz-OoSeysfEwuSkzDZH6dXc6N0UAtYuDBDLk_PxYx3OJwo1yrnDPvQIzBFf2utFhfYRynqNZSCAJ8QSkxQY_orgQO-Aq43UzGJmcGsO0hh405judpr5eAHi5Jv92W0lF57oIaFYDzEIifUbTmf8Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a4eaad83a.mp4?token=TXXxS3Wu7RjCnJDyOvpAVXM3cl1XpFBqGUh3v72BcjZpNm7SUltOgyh957R_wqa1NMeT0B1gqTEQ5sF87QyaLVNYcrhFouqvWAFC9hisXo2Qdz2d8oysEQuIUm_r2enEgKiO3NDQGH0Bb6MlbiWlhib8eDjQy6liHuzUHHy0c9Y0xFpFnULMQ8U8KFCz6gxlKHz-OoSeysfEwuSkzDZH6dXc6N0UAtYuDBDLk_PxYx3OJwo1yrnDPvQIzBFf2utFhfYRynqNZSCAJ8QSkxQY_orgQO-Aq43UzGJmcGsO0hh405judpr5eAHi5Jv92W0lF57oIaFYDzEIifUbTmf8Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
علی بازگشا، سخنگوی باشگاه پرسپولیس: اگر تضمین بدهند در بازی برگشت با تراکتور هواداران حضور داشته باشند، آنوقت می‌توانیم تصمیم بگیریم که بازی رفت با تماشاگر باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/Futball180TV/104186" target="_blank">📅 22:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104185">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85bc3fae83.mp4?token=Iv-4X5QqyGclTTNVbYPh_wgjEZEs9lxYtAqdJodrUQONVVJ-l5MG2sCmp6DX09OVNKR_aMr-1nA90sR2hjGGwnNlfq2AxeO6U40pnKJUhaKq5iME1z89k-AsLrYge5C28byMO3RNK_u1j_L0_TibNJX4eL5IXrq6vFKwV2sEi-XApxzrDqBrMj3f_yK2Un0QMXTpRxQtX9bWhZVoSehMvGfzpGC21kZezh1nqazfNV-7KJmBNkfgPRYDeEmqi7vgQPWznMnP7jNQvHDUhXn-Gfj96OQyxvpH7Qw54dOq1_H0IBUAn0Sm6lcOyJZerMVzG4Dr4GAkDLTHPz1lVEa8kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85bc3fae83.mp4?token=Iv-4X5QqyGclTTNVbYPh_wgjEZEs9lxYtAqdJodrUQONVVJ-l5MG2sCmp6DX09OVNKR_aMr-1nA90sR2hjGGwnNlfq2AxeO6U40pnKJUhaKq5iME1z89k-AsLrYge5C28byMO3RNK_u1j_L0_TibNJX4eL5IXrq6vFKwV2sEi-XApxzrDqBrMj3f_yK2Un0QMXTpRxQtX9bWhZVoSehMvGfzpGC21kZezh1nqazfNV-7KJmBNkfgPRYDeEmqi7vgQPWznMnP7jNQvHDUhXn-Gfj96OQyxvpH7Qw54dOq1_H0IBUAn0Sm6lcOyJZerMVzG4Dr4GAkDLTHPz1lVEa8kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🇮🇷
شهرآبادی، بازیکن پرسپولیس: امسال هدفمان قهرمانی است/ سال قبل تر از حضورم در استقلال به پرسپولیس رفتم اما قسمتم نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/Futball180TV/104185" target="_blank">📅 22:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104184">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43972e9198.mp4?token=WvANpy0bRkqSUYONNGZv--6CN2eceN1TT4YKgsG8j1SH50VfH1svEOzpRHP9F1oAF2yoPjdJGidJsq2_h_q3WkOuSDuLwPpIHC8-rU6YQ5h06fFHi4YZIPMXynAGypEdK_5ALZEU29tSw6s-thmoqQY0j7wtMpZ62mkG9NvhX46blrDf5vaqtgd4kLWesKpsmG_SdOr6ZOQSm2MsB02hdj1jzzwye5KZXtr3LQg4FxHzXdEyLZHRm544SUnUC-hMc_dhFxyMxO81nm1395rRnXUpIUxTQs46RECZXP2EwfCXN6LdXeS4BNXOAr5YmnMuCHSso5X31_jb_80QLFd2Lm4tDPzhPxYvPZsIg_OvmZz1JxnX5t5biP8pAUPA_CnjLCd9o_E30Iq29zQS2K4psNpyS1Ff6XkwE9Tf-MJoVpyZswzzm6kB3mcN_pQ55Qxou8IOJxygGY4r549RsphrkcqZhX4gGAqlqXyimqvXHTZvRk5zF1kTIQY4j1ShBC-DNA92nquXo-4Ls2dwOVFNuKeo5CWnNKjMqfqku5P834c8x5TaxKeChjFlijSVA86MSERxGfhttdEUoQCa-oTbdZc_WHxRC7CdxPDpAdgQBZegCha84zToTVhYpoHclUrZwYe47Nhes3qX42nMk3UlRs5IiOozGE2uuAQzZG6teXI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43972e9198.mp4?token=WvANpy0bRkqSUYONNGZv--6CN2eceN1TT4YKgsG8j1SH50VfH1svEOzpRHP9F1oAF2yoPjdJGidJsq2_h_q3WkOuSDuLwPpIHC8-rU6YQ5h06fFHi4YZIPMXynAGypEdK_5ALZEU29tSw6s-thmoqQY0j7wtMpZ62mkG9NvhX46blrDf5vaqtgd4kLWesKpsmG_SdOr6ZOQSm2MsB02hdj1jzzwye5KZXtr3LQg4FxHzXdEyLZHRm544SUnUC-hMc_dhFxyMxO81nm1395rRnXUpIUxTQs46RECZXP2EwfCXN6LdXeS4BNXOAr5YmnMuCHSso5X31_jb_80QLFd2Lm4tDPzhPxYvPZsIg_OvmZz1JxnX5t5biP8pAUPA_CnjLCd9o_E30Iq29zQS2K4psNpyS1Ff6XkwE9Tf-MJoVpyZswzzm6kB3mcN_pQ55Qxou8IOJxygGY4r549RsphrkcqZhX4gGAqlqXyimqvXHTZvRk5zF1kTIQY4j1ShBC-DNA92nquXo-4Ls2dwOVFNuKeo5CWnNKjMqfqku5P834c8x5TaxKeChjFlijSVA86MSERxGfhttdEUoQCa-oTbdZc_WHxRC7CdxPDpAdgQBZegCha84zToTVhYpoHclUrZwYe47Nhes3qX42nMk3UlRs5IiOozGE2uuAQzZG6teXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🇮🇷
سوپرگل‌فولاد خوزستان مقابل شمس‌آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/Futball180TV/104184" target="_blank">📅 21:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104183">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">▶️
🚨
🚨
🇮🇷
🇮🇷
خلاصه بازی پرگل و جذاب و دیدنی پرسپولیس و استقلال خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/Futball180TV/104183" target="_blank">📅 21:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104182">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3E7K96he6uK078du3jbHRFFftKJXQ1ZuUXcGdkedfsxMkRsMeJ8lx6a7QLhpdyKFPZKZ2YTZ-P4OiFglHa7T83fxeZx0haIUuUAifwDRJ7O7vQthlt4usC8cxpAtix_P9z-dxsrwofhmpjtXURYNQ74dpovT3yz9ZjUUc7vw15XyPRQFsoetwwVKGnEYLxoXuEy2_Op3X28KLyHDtbFwuv4iHt4Xl0kTofphxgV1M3mu1__GCN_k36bFF4C6TbYsjSKQgG29mIT8ItYfX39sva9SvzUe2j7KkxNhu-MOJi762LiENwSsWduAicKwxMP92QQ0TozsoKzGp7Vg83WOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
پایان‌بازی‌هفته‌دوم لیگ‌برتر ایران؛ بازی چشم‌نواز در شهر قدس؛ تیم تارتار برای رقبایش خط و نشان کشید
🇮🇷
پرسپولیس
😀
-
😃
استقلال خوزستان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/104182" target="_blank">📅 21:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104181">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a62ef1f46.mp4?token=NePGekeNuzoVID_TksyM1pDiFa9RN9SkN1l8FPHchJE6FBAgrgt2UPfX25WwZMmqNwAyp6EkS0tksymvAeLpYEjg6qvVdaOgXLHciKWxNmdU_j4f5L9vFN4gA3BynFP7FQQNSdT_KMOb4bGYr0jViSIW0Xwsziz5hXtpwAmh1SK85vgeuzpLv0ZKeXdK_sH_8UQ9PNglR6CQgC2K54ZNOsXYlZOUdZdeCi0mzOjWwCFVTUy38cR3QhRPLj8dyeWF9JZnRGGTreATFMRBcVJFKGfaZgmsnCuFY0f6B4RyyEv-wW6cjZrc3Ho5pqCc9KoJ0HOz4Ab5gXyWFsd__0GfLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a62ef1f46.mp4?token=NePGekeNuzoVID_TksyM1pDiFa9RN9SkN1l8FPHchJE6FBAgrgt2UPfX25WwZMmqNwAyp6EkS0tksymvAeLpYEjg6qvVdaOgXLHciKWxNmdU_j4f5L9vFN4gA3BynFP7FQQNSdT_KMOb4bGYr0jViSIW0Xwsziz5hXtpwAmh1SK85vgeuzpLv0ZKeXdK_sH_8UQ9PNglR6CQgC2K54ZNOsXYlZOUdZdeCi0mzOjWwCFVTUy38cR3QhRPLj8dyeWF9JZnRGGTreATFMRBcVJFKGfaZgmsnCuFY0f6B4RyyEv-wW6cjZrc3Ho5pqCc9KoJ0HOz4Ab5gXyWFsd__0GfLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇷
گل چهارم پرسپولیس به استقلال خوزستان توسط شهرآبادی(90+3)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/104181" target="_blank">📅 21:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104180">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b2857b1d.mp4?token=jYvewFgpk2pBXPHgDOejLRYOCttjLza-IyV96CH0u7JLM_U9xZ_XDG-aX00LCsoA3P25QhPKlBbG5N34FVTL1wUwJ-V9JX9v9iYzvZiPjfFZR2RLvwZpNJs4kmbE1-VuB1ZX3BVk7zUW7f6TDVRqIRgRn8u3j_04hVUclurcxAYM3aNfxeaoe1j4TstezyE4eJxFZI6PUmWIBiSZN4aDjtphWguSNAcNdVXTJDaLRcbSmoP1HZpZOckYkz-2P6uJVPrWu7GOHmu672LTJ4Lsq2GCQpbSfJB3D8_MatW5Fuq4G-Fx5hIVElZvsfe3TPpj3pNPpccxIcPE1hBLUn3iCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b2857b1d.mp4?token=jYvewFgpk2pBXPHgDOejLRYOCttjLza-IyV96CH0u7JLM_U9xZ_XDG-aX00LCsoA3P25QhPKlBbG5N34FVTL1wUwJ-V9JX9v9iYzvZiPjfFZR2RLvwZpNJs4kmbE1-VuB1ZX3BVk7zUW7f6TDVRqIRgRn8u3j_04hVUclurcxAYM3aNfxeaoe1j4TstezyE4eJxFZI6PUmWIBiSZN4aDjtphWguSNAcNdVXTJDaLRcbSmoP1HZpZOckYkz-2P6uJVPrWu7GOHmu672LTJ4Lsq2GCQpbSfJB3D8_MatW5Fuq4G-Fx5hIVElZvsfe3TPpj3pNPpccxIcPE1hBLUn3iCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇮🇷
گل‌زیبای ملوان مقابل ذوب‌آهن دقیقه ۸۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/104180" target="_blank">📅 21:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104179">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohWzDp8dxcl1ismcGc10GSLYCjS2A6gegFAAcvcXAiYpLOK5wf9h79FVsspAkq7Wyz0RWkDidgOIU4aZ_YutG5MeqpomEeTd04eKCjEshfYYJEPQ9cTPShhGpViTEQZa8cWaUFj1U80l5hEbm9WS6gc7S4cDrfrlzkucHjwiRZmbvT0PdDj7W0FKj1JxlA8zWpNwzTW6DxGJkDHqM_IwEuLt9POLWibzxVHVJCU054zHDyOFaUHtnjjpunxWuhdzjppkE-CZune7v5_vjoHXL00aV3cbxqXpop7dDLopDFiNMw3HtBTeAJkO87sFKJ_DkiTF2DHYiRPdRQA9QpN2_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته‌اول لالیگا؛ ترکیب اتلتیکومادرید مقابل مالاگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/104179" target="_blank">📅 21:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104178">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543b2ef6fe.mp4?token=rzs6qp5Dwfx_d79oLdtrpXBcYgZEiTmUEmEpZS3xZiacUDbP1PzjIJIkIwKrFck8blhzYkzmqx64vLicCzuNBD84IKb85Imme6IoIdOi02Tyix9iIPAHuObNOo-du8wiTq7ciVR7pPQ7T7QfKHiyz2H0VpZu_WmYc2saGA3tFhnxMnRO3ZuDkYoBvELsPlyJ3mGxVCVNbSQwWJ0aTmXTF0IVxtTsQw15K3vIj341Y97hk0tDud2yZ-A3boXbNzm5i4gZQ7LFFJJhXJOTY-zax-iTt5BFC3tQgpuBPeqRc2klkT60h4XA1lGbwQBjflRXc6F4uJVo_zW89w2B6eNLfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543b2ef6fe.mp4?token=rzs6qp5Dwfx_d79oLdtrpXBcYgZEiTmUEmEpZS3xZiacUDbP1PzjIJIkIwKrFck8blhzYkzmqx64vLicCzuNBD84IKb85Imme6IoIdOi02Tyix9iIPAHuObNOo-du8wiTq7ciVR7pPQ7T7QfKHiyz2H0VpZu_WmYc2saGA3tFhnxMnRO3ZuDkYoBvELsPlyJ3mGxVCVNbSQwWJ0aTmXTF0IVxtTsQw15K3vIj341Y97hk0tDud2yZ-A3boXbNzm5i4gZQ7LFFJJhXJOTY-zax-iTt5BFC3tQgpuBPeqRc2klkT60h4XA1lGbwQBjflRXc6F4uJVo_zW89w2B6eNLfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🔥
🔥
🔥
🔥
سوپرگل پشم‌ریزون زبیر نیک‌نفس در بازی امشب مس‌شهربابک؛ یه لحظه روح مسی درون نیک‌نفس ظهور کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/104178" target="_blank">📅 21:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104177">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58ba1302f.mp4?token=O52MRBtHJgQkK1ZkFNU9geW6bPK-fVq-Hkwv_N3l-oBRIQ1sii_Vv80wwfcCf05vRid5TnfR0dMKcAMiw3X5LJ5uQ69kUP9c3G_BHKPJSMJOt_BraoOA9dnn5BZmMDoEGWIxAO7DwN40al4SweCxe9-7O4nj9Z7jsvXOtSTQNawuVGUjW76QkfYCFzsvrr93X-SbNW4QHlfNpEKkJhcKXVDNk07aBYfVvamGqKgqqdqS0xljhZB3r7ZRTZP9oagpbGeUvDABigXPmWw2fxZ8pRR-d28bDYnE7vQOPUXLzo-ze9dmXgdVgfgYOZtLPGYgDUwrJiMC7MMMcl003q573Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58ba1302f.mp4?token=O52MRBtHJgQkK1ZkFNU9geW6bPK-fVq-Hkwv_N3l-oBRIQ1sii_Vv80wwfcCf05vRid5TnfR0dMKcAMiw3X5LJ5uQ69kUP9c3G_BHKPJSMJOt_BraoOA9dnn5BZmMDoEGWIxAO7DwN40al4SweCxe9-7O4nj9Z7jsvXOtSTQNawuVGUjW76QkfYCFzsvrr93X-SbNW4QHlfNpEKkJhcKXVDNk07aBYfVvamGqKgqqdqS0xljhZB3r7ZRTZP9oagpbGeUvDABigXPmWw2fxZ8pRR-d28bDYnE7vQOPUXLzo-ze9dmXgdVgfgYOZtLPGYgDUwrJiMC7MMMcl003q573Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل اول استقلال خوزستان به پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/104177" target="_blank">📅 20:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104176">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvvqeTFCQVxcHmpx9Az8LY_jjXYfqDsvTAI_AgToGKHfzGSfU1ld_cjgeyWA9COkrr9pht3dmDCivjK6YXV96bprt21wa_Pabot0CPyXY-syDoT62dQtNKMm83NbmRTFwGzYNw7J9ZHdBtw5b8ZRpVxJ6eTgLb4u0G96sOO4U3u0nZKJLVry8CcbhaG4KKzsIuPiNnbrxKnuZZW8s4VfukJkNlHT1qsnALBDvfdRXLdT8XxqdEAlEAVBLR5D7m8nQVyNQn7g8nI6dP1tV4YWk_E4JqoZDeKkzsT2JVGY1PnFrqk9OQq4m3AMqNB0xTyfUSEqiQexbcF4Lz3NMpVtbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
استایل ساده‌زیست بالنسیاگا رامین‌رضاییان در ورزشگاه فولاد آره‌نا پیش از بازی فولاد
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/104176" target="_blank">📅 20:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104175">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔥
🇪🇸
انفجار نیوکمپ پس از اعلام نام رودری و ورود این بازیکن به زمین چمن ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/104175" target="_blank">📅 20:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104174">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_2Zf9gXICr2-_qBGliotzqtugqZ8fyoUWXrsvMLlUFlsW0KA4LZHVBYWSKEYp3d_tDEGlw5RcG0sIzibdqqjYnOO9-YCmp-H5hLQawlh6yNWiojpqFG6pGZBJ9HSdIkL1akzrt7EY-ak5EvOsKsE_Q7dbPL5-IwUBggiG3rLonqp5PN5BNqNR6vMkWqXfWjBIUQy0LJndv9JawWQJ5pOcCnj3-BzRBRLwUJKWemSurhGDP32TLCoe0bNtDyprAMoi6m7UTPOSdy-vqR5Vg42ssMFQHBMHnGMqwqoWFnqhrB68GDez4tzvFwiuAURNvy3dt4_7hvQyI-i_xvIexM-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
😳
🚨
🚨
🚨
تفاوت آلوارز تو عکس‌های رسمی فصل های قبلی و این فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/104174" target="_blank">📅 20:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104173">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41445f46c8.mp4?token=ePr2231flg_rgt-ZO3G4BDPqujL5srrG1gcqLsmj5lZSRwy9uzC_huatsNYEuijYVErtf_sBNCneHgcCifXXbUfqfJbVp2vLIlSwOu8LgmFi82lYB-twaoRCI_bSQn_vJOBgC7ytWSMsoi_byTYp35e9wpD4MO2bfjRGVGdjdT1ArOVpgAZX-UgH_KCo9x9ICy0MK7mxXdf2Pl-wUvusCofxyJuhngMrRPCRja84NERCyKcT0px__8SjS_-r39al7if4utzpaxkujv_1P--THjZonL9dAfjD7YRfWBynPkEMEzLD2jZipcMMJzvSKGPW-hYR8Vt2wW2DfVl1r8aCRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41445f46c8.mp4?token=ePr2231flg_rgt-ZO3G4BDPqujL5srrG1gcqLsmj5lZSRwy9uzC_huatsNYEuijYVErtf_sBNCneHgcCifXXbUfqfJbVp2vLIlSwOu8LgmFi82lYB-twaoRCI_bSQn_vJOBgC7ytWSMsoi_byTYp35e9wpD4MO2bfjRGVGdjdT1ArOVpgAZX-UgH_KCo9x9ICy0MK7mxXdf2Pl-wUvusCofxyJuhngMrRPCRja84NERCyKcT0px__8SjS_-r39al7if4utzpaxkujv_1P--THjZonL9dAfjD7YRfWBynPkEMEzLD2jZipcMMJzvSKGPW-hYR8Vt2wW2DfVl1r8aCRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✅
سیاوش یزدانی، مدافع پیشین گل‌گهر سیرجان به الطلبه عراق پیوست و‌ شاگرد علیرضا منصوریان شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/104173" target="_blank">📅 20:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104172">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d92806f40.mp4?token=FGETWwt0z2vLMJT-TXMC0fM4pmOOVN9AeFkx2bLdZeuulCj0u4N3OjFFEZqIPxVvNYcc5uH8jMgdP8VCTuWRfP066QAA7htM0M5hDlzOJGZ_KNw3QO5PF0YeUPNjOiYLM3xtnTt9LOdKj7tdF-1Mw7Nja7SoQvBCdj0ne--mvO0vCHqoBDzia5HyitSbteD6S93JNpv9JorGuF3wWy244-2In5kMp20e99uV6rwjg5nGFIP0nni6XTMc27zp7Slub9UOM0LUlVZ5TsGVDcZv5LpT8uzXxW6j61NH9DAIexPugDOHy3PU8MRVjawRU7T3MWHG16p8QYG0SBk-JCYX5L9ab9AY5URJDucFXL3LPxPECFIAceIdQZMrb3OzoU-YSnUbLqP9IbFr7KdFjUBQR5QRKcN65Zdc7qjY7m5MR8pV5q0-Gb2v9mO-_sunIveasAgWrCSzxy8clkSr_XH2k1ndmxMgSgb-447gU4U4JtTbNX71VWZXplKDF8KHHd0Wwz72MpDobsJ71E7lHXupTUBYgR-BEH8I70yYkJknR0AZe6673zfFmDbWX61iBjuPo538tyeVc2znsSCnFl5-WXEUMmVHQVREs7mz8173TOHGQWrS5ipVCpBfQFuey1dDuC2YpX1-zqhun2R9yV2QFumwd8cUkOlknlOeenF2kAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d92806f40.mp4?token=FGETWwt0z2vLMJT-TXMC0fM4pmOOVN9AeFkx2bLdZeuulCj0u4N3OjFFEZqIPxVvNYcc5uH8jMgdP8VCTuWRfP066QAA7htM0M5hDlzOJGZ_KNw3QO5PF0YeUPNjOiYLM3xtnTt9LOdKj7tdF-1Mw7Nja7SoQvBCdj0ne--mvO0vCHqoBDzia5HyitSbteD6S93JNpv9JorGuF3wWy244-2In5kMp20e99uV6rwjg5nGFIP0nni6XTMc27zp7Slub9UOM0LUlVZ5TsGVDcZv5LpT8uzXxW6j61NH9DAIexPugDOHy3PU8MRVjawRU7T3MWHG16p8QYG0SBk-JCYX5L9ab9AY5URJDucFXL3LPxPECFIAceIdQZMrb3OzoU-YSnUbLqP9IbFr7KdFjUBQR5QRKcN65Zdc7qjY7m5MR8pV5q0-Gb2v9mO-_sunIveasAgWrCSzxy8clkSr_XH2k1ndmxMgSgb-447gU4U4JtTbNX71VWZXplKDF8KHHd0Wwz72MpDobsJ71E7lHXupTUBYgR-BEH8I70yYkJknR0AZe6673zfFmDbWX61iBjuPo538tyeVc2znsSCnFl5-WXEUMmVHQVREs7mz8173TOHGQWrS5ipVCpBfQFuey1dDuC2YpX1-zqhun2R9yV2QFumwd8cUkOlknlOeenF2kAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇷
گل سوم پرسپولیس توسط ایگور سرگیف در دقیقه (48)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/104172" target="_blank">📅 20:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104171">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnRpzMJkmsvMJIMfuBMgajzNa9FUQgClCq-yQCkrX-aTt-eyfjNMgYkUw5h0yX6nz1apsHCdDNfeoRuAAGLNuY_nktzoTKbeNZZxa6bxdk6D-WTpBKOx1pCWJEErOFHkUnFSfFVk9EPcDMefy9c2Apd6Y8x-Tq0rNqUiaywZEKqymj5KFmSoAWJYXbm0ub05N6yOXgOcyDtPF1u1O8izYLkwb4_9JagowxPB-C_9ppDQ-0vP9vtti3qU3LXFWTNFVRD6HIBabv6lPXWRyuvB7Rfjw-5ZBFTfvPC3whHNu4EPmeUXBrwGGQ55QwLIE_mrYPGIwPRzBqgYegkJ3ZxBRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمق خط هافبک بارسا
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/104171" target="_blank">📅 20:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104170">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeAi3Ij0FIV98HgYURiZxG2Sl0q9xciUDgAzO9ln-xtz5N3Hd4OR-1Pfs9SKJf-s1-fRjeZFqn3DBQqeu4NXxJNjhP1CmcVmEu518zrGV50TC6q4ncRP5B9yQ5gI22ZbC9tiditHYti_o9grC4knbJKE736LnhE5cZnFYiIFFRSW59ihvLa6RDr6hr426IsZ0GdEAfaePCXnLWU_gVWQAhyKSr05UfyntVeJ2j23i3fA3wbbZTjqjhxcSCWySWymHZMotKZt9HTrMnjsDPUZ2XJ5k7qpnjBBT-4OD_DN59fKBdWgyGfyiWsQ-8gOdUDVHrB6Bd2PgMC54EkFgC_dEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جام خوان گمپر
🇪🇸
بارسلونا
🆚
الاهلی مصر
🍗
🗓
ساعت ۲۱:۳۰
🔴
انواع آپشن پیش‌بینی برای این بازی در بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/104170" target="_blank">📅 20:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104169">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd2bcc49ca.mp4?token=rDdHCGF6kumg0PYJ1c-ukxflMaq4M5WebiKD6f_4SneE8ZUUyxn0Jlx_E2bQ8ot622s1bWK0IxS5uAWIlFJB1TL_yFBu5VcotUpUlhxqUVV6DbbYgvT_xG5H24fYQ1oZdDkXJldjda9fvC6b8nBkeIrWIbmxjGyr42oAlMRpLhQb_NZ7sY31gb2fcIrlHdJsfsGyVukgz_HcP5l_H8rUI4MMHJxLaekhhpFjLgBAQSO1QuItBsNFnXyfZ9wocbtc3S1Y_VNULqTweb6M4qxCrYsTZXlxEVvP72CZc__z9uMpuW4gLiD9rumoYNafec6coNY_L8QGVuaLbbTqCnkd1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd2bcc49ca.mp4?token=rDdHCGF6kumg0PYJ1c-ukxflMaq4M5WebiKD6f_4SneE8ZUUyxn0Jlx_E2bQ8ot622s1bWK0IxS5uAWIlFJB1TL_yFBu5VcotUpUlhxqUVV6DbbYgvT_xG5H24fYQ1oZdDkXJldjda9fvC6b8nBkeIrWIbmxjGyr42oAlMRpLhQb_NZ7sY31gb2fcIrlHdJsfsGyVukgz_HcP5l_H8rUI4MMHJxLaekhhpFjLgBAQSO1QuItBsNFnXyfZ9wocbtc3S1Y_VNULqTweb6M4qxCrYsTZXlxEVvP72CZc__z9uMpuW4gLiD9rumoYNafec6coNY_L8QGVuaLbbTqCnkd1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🤕
ابوالفضل جلالی در دقیقه 26 مصدوم شد و از زمین بیرون رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/104169" target="_blank">📅 19:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104168">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXZBhTIBCrfFuGrNwPz9fdGrn8qFggfbS5JBGiODaeiLYs0ISwWJoTaTfNUn0SywbO5fhWxzFH9S_GJN0K5m3XQJTLbDmqfgVyF-q660GQdD3jUf4rx3z52uQRYz43vi2ccPLsBrk9zLfOQnD_BpDASS03nbCy1MH0bHdb6VX2yR-oNH588CbaCKVpKo_GRu--fTAZK_8Jn-fA9xv-q9OBoJaaRc_aYDU1H3oTLArynki1bCq_VBWImqTwoVcCK6whre-HVx856tavSeh9vLVynh72FfSC0bVCJ9AH1riLfSUDCIzPC_FTk3zRzlIZhqoXx0JXkh_bqePKKEFwSiLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
ترکیب رسمی بارسا مقابل الاهلی؛ ساعت ۲۱:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/104168" target="_blank">📅 19:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104167">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b73b9b3bf6.mp4?token=hTJZZF4jDdPqnejAdia2irun5lxZTIFdF5gLISXZwaXVKmPq1fovfH7t1qw3UUFurbWBxykmNcmEdUM6x6YzTF934bvsQSb5y4sYgOgkKwZXaX21-37rHaca-hJYRLTHVQdXrvfR6-0CXA3fxxK20dYRUlxdP5-l409gS_KB5cjjWS5_nVEEXK_nBU26Wj-qeiR7VaNOexjtjyDaJ1pPCh_jDFjsd5b3gI0-ZiAixsP8w2sNncCQAfooy4ZKWpACzuo_ukZpomUHatFeTwtd0OrfclOUj7FDImFGrmh_VuE7f0J2P3aJMckfyYrWJcaYWYQQ2l70rP2y9p04B_seiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b73b9b3bf6.mp4?token=hTJZZF4jDdPqnejAdia2irun5lxZTIFdF5gLISXZwaXVKmPq1fovfH7t1qw3UUFurbWBxykmNcmEdUM6x6YzTF934bvsQSb5y4sYgOgkKwZXaX21-37rHaca-hJYRLTHVQdXrvfR6-0CXA3fxxK20dYRUlxdP5-l409gS_KB5cjjWS5_nVEEXK_nBU26Wj-qeiR7VaNOexjtjyDaJ1pPCh_jDFjsd5b3gI0-ZiAixsP8w2sNncCQAfooy4ZKWpACzuo_ukZpomUHatFeTwtd0OrfclOUj7FDImFGrmh_VuE7f0J2P3aJMckfyYrWJcaYWYQQ2l70rP2y9p04B_seiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇷
گل دوم پرسپولیس به استقلال خوزستان توسط علی علیپور 20
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/104167" target="_blank">📅 19:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104166">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtXk5qmdpMTYlWnhVldEIhqsnn2WWYwFzeNilih8R3CdthqE_hV0tyRiieaQ2jK6gBMjBD6mqEnkrIOiF-COkdUDj88PXGsOipPFx555wV-_ZsKQqJ0cFDEhCUjvtGIoow3TBGn7ojtFSBCd4KUJOsSjDfn2CZ3jbdixLAf1f0jnIFEqQLjkd6mQb0ABZbZ3dd9tXH2RBWFVwa-V-D9wKwnd2yg0ihEBiERnrXONvfOCg6zPLh6twB5KoLaMPf85MxOelivUy4vi4VPTMw77olKVZiEDjeE-Hu9HEscFu0ASX250cCMV4lIhPkYqRJvj2B6Ca-7VH31yKDrnDEMqLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
جرارد رومرو:
لائوتارو گزینه ای که بارسا انتخاب کرده و تا پایان نقل انتقالات برای جذبش تلاش میکنه
✅
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/104166" target="_blank">📅 19:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104165">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6842cf509a.mp4?token=Cje-vgDOe3W-Xq1e8eNi5IjxoG0HTx4XBmJFTAIJWncat82m--U-UVl8RY7amius7_P2h2kPEUjZJJArbmmAYlnt0NvjGkFWiKCuDOnO9E9VyQWLqrs86nybVPXiRacue22cckUKHojMJxegEJD_R8RYOV0LoMEaGEKE_5eC5OyaXLOB75cjCCWgDClCDwG_38KYDIsc8beHD-KSQJwH1GNUAbIaAUFa5yZUGNs1clHLBg34i8oNC89IMhTBHsP-U12MK0cRYUkSrEHLySN1ZvD4i9yxHh4l1oTd2UHkI9UMz_mIq3BoGe7z8Nwu0k1uOrRKpfQaeXYekOSrqTRnoUnmkp4TkEmaPwMhPLuUyzbD8h-_uQbKtTCMZmqNDh8YFqAf86VJ29oJZV_H8L-7DvJSrlnQyjhuMovy62kTVg1Zy63MN5uHThxcgCn8NMH6ElyOqZiDQuSsQHGmYOEqVeOoO8p5jRAUYKVESHfpUFMXZKHQD041tEh2USUZ0Wh_hi-2hP7OArdm2uE5NN4muTmPLLsdBVqiTOPElrhaUhwtJKi0dnFX0LaOFM06NC5O2ZLErCs1Y6ZwOkaeEflwR9h9v9BBLg1h1L_mbWOw8Wg83LpzQuCndXQurYNApXrFDQ5nTD3vLzdwcHJyelxdM24-ROZLoJK0n2OWIXmiQ74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6842cf509a.mp4?token=Cje-vgDOe3W-Xq1e8eNi5IjxoG0HTx4XBmJFTAIJWncat82m--U-UVl8RY7amius7_P2h2kPEUjZJJArbmmAYlnt0NvjGkFWiKCuDOnO9E9VyQWLqrs86nybVPXiRacue22cckUKHojMJxegEJD_R8RYOV0LoMEaGEKE_5eC5OyaXLOB75cjCCWgDClCDwG_38KYDIsc8beHD-KSQJwH1GNUAbIaAUFa5yZUGNs1clHLBg34i8oNC89IMhTBHsP-U12MK0cRYUkSrEHLySN1ZvD4i9yxHh4l1oTd2UHkI9UMz_mIq3BoGe7z8Nwu0k1uOrRKpfQaeXYekOSrqTRnoUnmkp4TkEmaPwMhPLuUyzbD8h-_uQbKtTCMZmqNDh8YFqAf86VJ29oJZV_H8L-7DvJSrlnQyjhuMovy62kTVg1Zy63MN5uHThxcgCn8NMH6ElyOqZiDQuSsQHGmYOEqVeOoO8p5jRAUYKVESHfpUFMXZKHQD041tEh2USUZ0Wh_hi-2hP7OArdm2uE5NN4muTmPLLsdBVqiTOPElrhaUhwtJKi0dnFX0LaOFM06NC5O2ZLErCs1Y6ZwOkaeEflwR9h9v9BBLg1h1L_mbWOw8Wg83LpzQuCndXQurYNApXrFDQ5nTD3vLzdwcHJyelxdM24-ROZLoJK0n2OWIXmiQ74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
گل اول پرسپولیس توسط خدابنده‌لو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/104165" target="_blank">📅 19:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104164">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
رومانو خبر جدیدی راجب آلوارز نذاشته و اخبار منتشر شده دقایق اخیر فیکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/104164" target="_blank">📅 19:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104161">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e03b3c710.mp4?token=aLHydTjihNiJPXRTciyymVvtDSAci2TqzIzkGi3IkON2vQk_IZhuG9CIdGWXzDuqUog5_gxmhsKUj3x-sQVLNNqc8lvDL19oPiGyYn-aLML6Yhwz_3BzEUHQFWy-JqfBrC4Oaej6N4kVpMksH--71VwN6ROeydb_imlD23n8obvb3KCxlFax4l0ZnG_DJGXC1naOhwOeQp_Xs_cfeInK1gUfQT-5QhAA_JArgiyzYdi2joSwritoNhTr8-Kgdok73k_1XoSOtP9DC9Ne8_0Je2q06ycD6Km5sHAiHKOH_9ZLiKU7RTwyw93ciZi7XFsiG_Ca8_fzn4z0mvHuqS1wvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e03b3c710.mp4?token=aLHydTjihNiJPXRTciyymVvtDSAci2TqzIzkGi3IkON2vQk_IZhuG9CIdGWXzDuqUog5_gxmhsKUj3x-sQVLNNqc8lvDL19oPiGyYn-aLML6Yhwz_3BzEUHQFWy-JqfBrC4Oaej6N4kVpMksH--71VwN6ROeydb_imlD23n8obvb3KCxlFax4l0ZnG_DJGXC1naOhwOeQp_Xs_cfeInK1gUfQT-5QhAA_JArgiyzYdi2joSwritoNhTr8-Kgdok73k_1XoSOtP9DC9Ne8_0Je2q06ycD6Km5sHAiHKOH_9ZLiKU7RTwyw93ciZi7XFsiG_Ca8_fzn4z0mvHuqS1wvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✅
تیجانی ریندرز، هافبک 28 ساله منچستر سیتی با قراردادی به ارزش 61 میلیون یورو به القادسیه عربستان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/104161" target="_blank">📅 18:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104160">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUkBL4LABJy9wJRpb2G9LqjtQIu1RtZhJA8lOCP3jcJQbUfNwOe_7yFyWwxow7Jbd_rnK1t8dT7jDdiInVSZ4a4OMsWtcR80mQytcftDtWnsW3zqz_HATynf29LwAWMH1edz-qit678iizdeKvesgfptk-5TQEBuLin-bmWN4yxS_i3ljMssF4NJ-z_aUDoyoAqOATI-wuMqktBQc9lnG_39rIWwXjJerqlrYUkehn3qD6wF-_uoZ8wvQFuhQwlhKdtUHlnVMlys9WTjuFnaDpCidWXdbv5Ng48KBEcQwvoMsysMYtSKMRdA2vD3baqjArZt4j7xEy-ZZ85Dz2XBiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
✅
شماتیک ترکیب امروز پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/104160" target="_blank">📅 18:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104159">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5pMCg-jXVPJM24L8Zdl1o7JrtvoWkcQU07xEKZaj4uw4OOzqZiuzAG4zPbWwNkYeoaR_B6yaXD-PHEWPHhxIngnmbfLwgpHxHtPa5UI9UDfhvReYW7f1QmcbgDeWbhin4fiuQUOu8y_CQGR32jz58BVRBv0HGxBnETWS6b6m1Ji1WCTXBqTwLNF-IfviFbaaeoQQoVMrDfSMWUJZgFhSkIxXM3oIfUzAld7Von2ufmMIf3rbv1cMDJVffL9xT8uWhGkJ8O5N3skL2pnZf5Kh25KDz43VVzjJS_gmEfDWI2M7hQx6VVJ01Fug6gD2c_D5-IdElwoEOMeRsvBsDP-MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
🇮🇷
🇮🇷
لیست بازیکنان اصلی و ذخیره پرسپولیس و استقلال خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/104159" target="_blank">📅 18:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104158">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35d63f7a79.mp4?token=YFRMYE39Y1JMh8XmNeFEi_HTC_BHBoCEifkD6f8qu3XeUwYVig1XcJNVFCgXuxz5hzZWXTZ_8hDiaCdNlCZWRPYpidK7XiButkOctLnJVR2my4jWtqCOzpN6h6gjTtlXwdZi46fterazrLzjxtR04EQH_a8CHCH5uLU6c3_iygfgJXvQC_J3dV11T7pbw100rvmAEV_fvD6AtToiAOY4lF28dlXJljrCEamW--WVc6EqB15jzJtgNh1-Dw_ccLTQqnd6OcwbyAZkMJnLtz31tdRDtkOBVs30z6UVfMrrMT0PSht7Va29GEcMCNOsAX6Wc1U2gNcDrxMkoiJsWs8HYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35d63f7a79.mp4?token=YFRMYE39Y1JMh8XmNeFEi_HTC_BHBoCEifkD6f8qu3XeUwYVig1XcJNVFCgXuxz5hzZWXTZ_8hDiaCdNlCZWRPYpidK7XiButkOctLnJVR2my4jWtqCOzpN6h6gjTtlXwdZi46fterazrLzjxtR04EQH_a8CHCH5uLU6c3_iygfgJXvQC_J3dV11T7pbw100rvmAEV_fvD6AtToiAOY4lF28dlXJljrCEamW--WVc6EqB15jzJtgNh1-Dw_ccLTQqnd6OcwbyAZkMJnLtz31tdRDtkOBVs30z6UVfMrrMT0PSht7Va29GEcMCNOsAX6Wc1U2gNcDrxMkoiJsWs8HYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
🇮🇷
بانوی هوادار پرسپولیس: یاغی خوبی گیرمون اومد، استقلالیا قدر جلالی رو ندونستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/104158" target="_blank">📅 18:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104157">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-PpH8g-e9H0nTPha-0yW9zedjjBpVSB2tSWair8AubpoUWgWLwjcapLv02LTljv9uBWDBsnLwuf2Liuw6Q0Lqu_2Jusd98-YXKXv3kV3oV5khKCtO78woia8MbA3XDKgSh5HbZ291GXGyNa0dIAe6EKvcaJE-iiHU3jjHTJpan0EgssDrsCO8X-BSjlsktyhvZSOO5HfMva-2eHlGSXh8_suZuxiq7AYW0MAvXjxxzPtR-WKQrdJ4ayLvrqggUhPGxZhFfo_8Mn9rz-7_1twd9t89g4myzICxyE_4nlmio0KLUR79dzw_n6mabiA_rbrx8-3ACa3tMWa3dMowSgMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
روزنامه‌اسپورت: منچستریونایتد پیشنهاد ۴۰ میلیون یورویی برای جذب گاوی به بارسلونا ارسال کرده که هم باشگاه و هم بازیکن این پیشنهاد رو فورا رد کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/104157" target="_blank">📅 18:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104156">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d137678386.mp4?token=W3QkPL8_CvP0SGMvSZNeMjAv4sEEyMPsohPIASR7YsfJ9DfapUijW6egVrAMYSxdTJ-_JH46rbOwhtCuDS9VwScmEtQfh6aUQAFdDwHeNRERzm3MudeWn0EA1DXijfCw3HdG1cvfJXO--JahCqLVt17-RGckZBCMKD0u0_oLFthw7jfYb8jHTWN7nqLiIE_7H0ZfSbChANleOlSEPZyTaPBbpUdGZqv2E7DYD_ct437P3e8U0fWPGo5--pIq8850u3MXwJw7j1uWhU2I6cs6XAWWvTRwKIuMhXHlDI54i9yyWUw1FgngSWoKZ6s-1JfPlqdFI88qv6E7OF9jWgMfwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d137678386.mp4?token=W3QkPL8_CvP0SGMvSZNeMjAv4sEEyMPsohPIASR7YsfJ9DfapUijW6egVrAMYSxdTJ-_JH46rbOwhtCuDS9VwScmEtQfh6aUQAFdDwHeNRERzm3MudeWn0EA1DXijfCw3HdG1cvfJXO--JahCqLVt17-RGckZBCMKD0u0_oLFthw7jfYb8jHTWN7nqLiIE_7H0ZfSbChANleOlSEPZyTaPBbpUdGZqv2E7DYD_ct437P3e8U0fWPGo5--pIq8850u3MXwJw7j1uWhU2I6cs6XAWWvTRwKIuMhXHlDI54i9yyWUw1FgngSWoKZ6s-1JfPlqdFI88qv6E7OF9jWgMfwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
هوادار پرسپولیس: تیمی که ۷ گل خورده و دسته سه رفته، به ما نمی‌خوره! فینال آسیا واقعی رو ما دیدیم. استقلال بره آسیا ۷ تا بخوره، خوشحال میشیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/104156" target="_blank">📅 18:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104155">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxjIxIewqys96OXftZ7TtAWPHcFZOY7ahT70ljH_egx6JhQILDd-yiccUW9PnL26Zqa5pwCDsifTGfVoRLJihNrkj-gcCOWZEft4wHMLweN8PBG_zmg0b1NFZI2XotNoM4bnSEKzqEaCeB4MkwSPPp0lO8xUds3HoGr6I-5btTYR2VaC6EjfsjdDRV1ViuWJTaXl203JNIMrZ_KQSuvKNTriG0YhVDb7C-5eriAyQt3dMoyjkw9dLyIFx_5yr2KzxAiknoZ7uBkRk0MSDyk-Vfp1m4VJDo4scaGWKuIfDZx6LhcJGxCLzWi2Ri-L1gc9SOCcbKFbX-XCS1VDMcRvtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
بارسلونا بزودی با عقد قراردادی لیواکوویچ سنگربان تیم‌ملی کرواسی رو جذب میکنه و یک فصل قرضی به تیم دیگه‌ای میده تا از تابستان ۲۰۲۷ جانشین شزنی در کاتالان‌ها بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/104155" target="_blank">📅 18:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104154">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NitVS53nRMdOdM4BKUIgEIE0H8DglZ5sDVQtuRsgOZJCESozZA-NZifz5wpTWEFd8AzVQTDWse-2Ud6JXHGag2ABCt5kG73OH2FcOsYuupUi6oFnLt-_Uul9FbYX-VtPHYci0tqJ17IpO3Gys9KmRs4NgOoWmJsHxJLqTZTFbZ02pTt4NbQCB-DjBsy2nK8_mhGwr3wdEt30EuGlLTqBhnmaGPRWxkJdgG0WkZAL0cAuo2X_ndDZiWMRD18QMd10Bf_MtEiBS97c7WRk8G6Hlmfe-ZGuXAgnbGfI0D5WWp3E_dYX7KT02d86gej8OgUaIJsm82CkJMclRYOgfkhC7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
خولیان آلوارز باید یه سالی بره تراپی تا به وضعیت نرمال برگرده
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/104154" target="_blank">📅 18:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104153">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPVMfu9weTxBB4a84gtxwO_hA5zk9gozyWBWBKZHXlnGVAGrr2KDNV31qq2PTLYrRtS0UDpIVdEI94kuiabY-2chl4LQsZhsunI1IdSq8OE_sX2Abj4xp8oCtF4_9cTQG7yswBKlg6-Nlf8vuI4lxcsw7jxj-ia0nds5-buwh2mxkvf70J4tosC6r6YgUjFBq1Q0GcrX_JvWFLc8rPH_h747wb4DJHS-cwc9NuWHETKNYXUcaFchW6OghGLYjs24zodkkzAkJGp-QuGO_sTGJ7CS7dPYiSxKu3Aet5zYxSkcbMKNVBJu4dYaM5JcorQFXysx15fb-ZvhVINNLRVdXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
هری‌کین ستاره تیم‌فوتبال بایرن‌مونیخ جایزه کفش‌طلای فصل‌گذشته اروپا رو دریافت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/104153" target="_blank">📅 18:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104152">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82988d8dce.mp4?token=ON-nKQ-2xa92jK0J7m___dvEGSWuS3Q672cfOfZlman-LJ0kL_OFDzaQ2iYDy3__m4c3fUCOwulZotwJyEMPoUN22tk6o1b3qmGAAIn7-rrJKGzUfi2l04c4ILWtMwT-QMBEPe5cxMhJlXRK_qX6Aq-w58VvGftzdPFKxRVgtQxMKCht7XOjUeTcR2mA10jspEbDQot777ByAlZEAxhA-LMDLfSo96J2xfdopNHLmI4TgMgqJYj9wdR9n22u1VoFQ8igrXRq08PwFSSkri7Ao3A58-3Isd-KRYfR8GrbJiJ8CRROvnqocvtqsfCAGaCWRgUgVKkodLHFZMUWP36mDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82988d8dce.mp4?token=ON-nKQ-2xa92jK0J7m___dvEGSWuS3Q672cfOfZlman-LJ0kL_OFDzaQ2iYDy3__m4c3fUCOwulZotwJyEMPoUN22tk6o1b3qmGAAIn7-rrJKGzUfi2l04c4ILWtMwT-QMBEPe5cxMhJlXRK_qX6Aq-w58VvGftzdPFKxRVgtQxMKCht7XOjUeTcR2mA10jspEbDQot777ByAlZEAxhA-LMDLfSo96J2xfdopNHLmI4TgMgqJYj9wdR9n22u1VoFQ8igrXRq08PwFSSkri7Ao3A58-3Isd-KRYfR8GrbJiJ8CRROvnqocvtqsfCAGaCWRgUgVKkodLHFZMUWP36mDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🇮🇷
کری خوانی جنجالی هواداران پرسپولیس برای تراکتور
: همون تیمی که 10 سال اومده لیگ؟! به خدا کری با آنها نداریم. ما برابر بایرن مونیخ هم برای برد رفتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/104152" target="_blank">📅 18:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104151">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e37442fd.mp4?token=Fj8rv0Zuk8Eu_XcirF0cgtgSRymKvlR9iNz-OaoJTXEhO2yQEFYE9ft-zMk-_vY2lZomEEKJ38q15pkKnwQsit06cNS7NsflspO_1WY28OCD_Xx7INDoCg_ip5dTz0ekzg_1EEXkUky_XWH2YGwaTdz6lost4bDTqDGcq1dr0GDGkqP_Ao7bjOncfWg07RSvsQpI9O92cuC5QtnSURqBsfphh21zdr1k0ooQ0lu__YrJEvNNiX_MBTQ01c-zSmeSkIa4QNzmmiP_3DZyPlXhBLjjBria3Fek8YKRwW5Dc-DC8gux5OidZ6mAIHJOgU_LAEqxRJ1IyTwIE9TIOsQCdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e37442fd.mp4?token=Fj8rv0Zuk8Eu_XcirF0cgtgSRymKvlR9iNz-OaoJTXEhO2yQEFYE9ft-zMk-_vY2lZomEEKJ38q15pkKnwQsit06cNS7NsflspO_1WY28OCD_Xx7INDoCg_ip5dTz0ekzg_1EEXkUky_XWH2YGwaTdz6lost4bDTqDGcq1dr0GDGkqP_Ao7bjOncfWg07RSvsQpI9O92cuC5QtnSURqBsfphh21zdr1k0ooQ0lu__YrJEvNNiX_MBTQ01c-zSmeSkIa4QNzmmiP_3DZyPlXhBLjjBria3Fek8YKRwW5Dc-DC8gux5OidZ6mAIHJOgU_LAEqxRJ1IyTwIE9TIOsQCdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇩🇪
جمال موسیالا: یک اختلال عصبی دارم و اتفاقی که در دوبازی اخیر برام رخ داده کاملا طبیعیه. امیدوارم هرچه سریعتر بهبود پیدا کنم و‌ نگرانی خاصی وجود نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/104151" target="_blank">📅 18:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104150">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">💎
برداشت بدون محدودیت داره حتی ۱۰ میلیارد تومان هم برنده بشی بدون دردسر برداشت میکنی.
✅
🎁
برای مبالغ بالا ۱۰۰۰۰ دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ ۱۰۰۰ دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/104150" target="_blank">📅 18:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104149">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari (3).apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/104149" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر WEPARI
😀
😃
😄
😁
🔥
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 120% اولین واریز
‼️
🔥
بونوس برای 4 واریز اول
‼️
⚽️
بونوس ورزشی هر دوشنبه و چهار شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🔥
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
📌
آموزش نصب برای IOS
g28
✔
https://t.me/WePariFarsi</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/104149" target="_blank">📅 18:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104148">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13852c35e9.mp4?token=pqGhL1-xg5XLU6_bSley5T8WoqLNrsmCwLz1OL7I-lI6cj87fKmRlB0nSXaOywYmUILhDRGbN1wMa7-4TfDiYJgrkyLON_eFr2bXVrRnq98GQ9YkX9bFMRi6ntNSgGoitcufMHSEd5irs5k3FclYAunT_hP-gW1LCCFrJ_SqSJvVFsiPA3hss0ZdfAajDFu-h9RCyOyICVEpoocEH_MoMVMoyld66Ug7IBvO_b2AaL-IRbcsGuoGPRGcfCSFxACAXHh0PE4XyqXwgBObk-fYuyaTTkAorsBZ6pBM05yJrQ_8JRpYwXaOXswpDWv8rp1sWqmE2oycEzR6TnVZKE2KAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13852c35e9.mp4?token=pqGhL1-xg5XLU6_bSley5T8WoqLNrsmCwLz1OL7I-lI6cj87fKmRlB0nSXaOywYmUILhDRGbN1wMa7-4TfDiYJgrkyLON_eFr2bXVrRnq98GQ9YkX9bFMRi6ntNSgGoitcufMHSEd5irs5k3FclYAunT_hP-gW1LCCFrJ_SqSJvVFsiPA3hss0ZdfAajDFu-h9RCyOyICVEpoocEH_MoMVMoyld66Ug7IBvO_b2AaL-IRbcsGuoGPRGcfCSFxACAXHh0PE4XyqXwgBObk-fYuyaTTkAorsBZ6pBM05yJrQ_8JRpYwXaOXswpDWv8rp1sWqmE2oycEzR6TnVZKE2KAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جی-جی اوکوچا در پاسخ به سوال مسی یا رونالدو: "رونالدو یه بازیکن خاصه. اما برای من، اون فقط یه گلزنه. اون یه گلزنه؛ درست مثل هالند."
👀
"مسی تو یه سیاره دیگه‌ست. مسی اصلاً به دنیا اومده که فوتبال بازی کنه. فکر کنم مسی اگه فوتبال بازی نکنه مریض میشه! اون یه نابغه‌ست."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/104148" target="_blank">📅 17:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104147">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K33f9jivFZyyWidRXCjThfglj1F0oGr9NxCU-cVVTpBAkm763dcsxaijomODrB_D1KrlFGV8Ggcpk53SaXous_-6H8TbPpX28Ga_jAlr0J5e4kguoFp1oOaaCiZT91EKe3KApfj3d5bdJ4YtaHdjtlikPPcpUA3ICyTBTryyBnfPTLQB2N750-s0zrmBrH0krh1w0f67iLhiqmllj0dtj_dSRNi8yrlpRR7TTSLh3P-20vYWgg8v-ESzDLLGO-d_ohuafeKxm8IwzBPS4IyQnFRRV62F3QlhjL67FlLbuSvBxFR98Ckzqdy_4n97UHjaTsvKQW0N5kTxn_ycSZlwTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
جرارد رومرو: بعد منتفی شدن خولیان آلوارز، بارسلونا به صورت جدی درحال بررسی گزینه خرید نیکولو تریسولدی مهاجم نوک کلوب بروژ بلژیک هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/104147" target="_blank">📅 17:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104146">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CykHgzcVOl0QmUUhbuGrsUKqaL4_eWJvYqlV5WNT7QP2SqRq00s8-cOBWlp5PiimE4NUGyb4cxS1RBoR3dzM-QCR5I6RukM1ba7I-u1qFcjOSxnen-RJAbuvaWWrvfdiLSMd54HVYJ0OsWJeRIbrl8z2GQkOOhBhhd8LalhmpMosHsxReXgxZuGO_uf9XvlIfQk0yeXWGOkQ-QhMt3Q1uJsf6fzWArtb_lElKnBEMZMftnv2pN6edJqHADPC2RqayO81_klEvdnkKCLJMp_W9x8k4rskMbRi4r0bg0gRCgPvL8nrhtjy6FiezrcwnPNBBvBYYl3xbTQf2MQxDWMBkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از دیوید اورنشتین: دو باشگاه آرسنال و استون‌ویلا برای کونسا به توافق ۵۰ میلیون یورویی رسیدن و بزودی تست‌های‌پزشکی خرید جدید آرسنال انجام میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/104146" target="_blank">📅 17:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104145">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vfl9bPEOmr3NEy0c8nJ8WOC4EA_G7nSDzwwRu3-7hYblMQJLipZXMy2Owligr4O3k9irZOg63DKoHCkHOpbshV1HzEm5bfCegaaabEOszQVyavgIr7yD4iq8AK2ncEsrFRolVqk_yOi6gCAX4ynPG-_tZgXeWdG94aLZwr4AHxrlbOrggK5cpg1E-rDTPDi_1DBNl_GObGJ-Mt-cL36rkzwnUM-w0DUudle9iX_MbHpWlyFV4rcZjijBteKeWCov5h5wVfzWwhrgufpc_D4IZ_01DEjLge0BDOLYvfMHtN4S5AxOCsXi-oLEkKUOmSj1UGuE2kkHuk5b4cKFJL-ucg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از دیوید اورنشتین: دو باشگاه آرسنال و استون‌ویلا برای کونسا به توافق ۵۰ میلیون یورویی رسیدن و بزودی تست‌های‌پزشکی خرید جدید آرسنال انجام میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/104145" target="_blank">📅 17:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104144">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🇪🇸
انریکه سرز‌و (رئیس اتلتیکو مادرید):
«نمی‌دانم خولیان عذرخواهی خواهد کرد یا نه، اما فقط با دو بازی می‌تواند دوباره دل هواداران را به دست بیاورد. ما از همان ابتدا به بارسلونا گفتیم که می‌خواهیم خولیان را حفظ کنیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/104144" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104143">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0844b0d9d0.mp4?token=LsTr2qLv3_xKdD_JeNiZW7h5KSy4pf0gD0m2aUC1s9QHo1Z1ZVDRMbvO4rHLcF2wkH9d-lfFBRhsXfQ4DDpthWa-HpCHT1yFa_7Ay8wi-Jah1d3prX6FXG4-2UEvMhQgySs_grbmJwGOMxKcfdia_yioC6TLI_PSTe9F3KRcBA909uterYnm_OGfeCZbwLsZVD6xK8rAf7njtTqlji0UmRF-qHe_pbbtGwy_b_6vqO9-q5aGtqHn6ia-t_uxAmk37i2ExE5p1HEg5nVCyJhVLculP3s3882wS-ULBqdExNvkJrih0CGCjpsav8fdkiSQ_vGm0i7jRkx62Cay0Iq4nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0844b0d9d0.mp4?token=LsTr2qLv3_xKdD_JeNiZW7h5KSy4pf0gD0m2aUC1s9QHo1Z1ZVDRMbvO4rHLcF2wkH9d-lfFBRhsXfQ4DDpthWa-HpCHT1yFa_7Ay8wi-Jah1d3prX6FXG4-2UEvMhQgySs_grbmJwGOMxKcfdia_yioC6TLI_PSTe9F3KRcBA909uterYnm_OGfeCZbwLsZVD6xK8rAf7njtTqlji0UmRF-qHe_pbbtGwy_b_6vqO9-q5aGtqHn6ia-t_uxAmk37i2ExE5p1HEg5nVCyJhVLculP3s3882wS-ULBqdExNvkJrih0CGCjpsav8fdkiSQ_vGm0i7jRkx62Cay0Iq4nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇪🇸
مراسم معارفه رسمی ژوزه مورینیو به‌عنوان سرمربی جدید رئال مادرید برگزار شد؛ بازگشتی که خودش آن را «بازگشت به خانه» توصیف کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/104143" target="_blank">📅 16:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104142">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ad88532c.mp4?token=QZB92f6270voGqvA0P8exmVHXQ8yjkVuzCYlMNVqDd6UKOytN_RvOPj79I6wYy0Za8Wx_x0Q8kmHoWVEeyMXcnpIc08Q3b77UKsVnpC6M_72Rh-8gvqECLCUTqwgkTJOpGXKz5bDb_FGNl0h4xFPY1QVG3g81aVH_eKWWVYcl8OTMbyGBh6AnSv_WEp-7SX_iP1OluV0-nbxbuoJbwR3i55jVEm9CaVkRCHEFGwXMBhPqtM3PVWbmRp6z0ZNQRZerSvEo7DiOJr80n83_HQ02bD5aIiaB7XwIx9J3jlZCr51AsqGPt2i0M1wbinFEdolE1oChKB9Bp-oWisD0KWY2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ad88532c.mp4?token=QZB92f6270voGqvA0P8exmVHXQ8yjkVuzCYlMNVqDd6UKOytN_RvOPj79I6wYy0Za8Wx_x0Q8kmHoWVEeyMXcnpIc08Q3b77UKsVnpC6M_72Rh-8gvqECLCUTqwgkTJOpGXKz5bDb_FGNl0h4xFPY1QVG3g81aVH_eKWWVYcl8OTMbyGBh6AnSv_WEp-7SX_iP1OluV0-nbxbuoJbwR3i55jVEm9CaVkRCHEFGwXMBhPqtM3PVWbmRp6z0ZNQRZerSvEo7DiOJr80n83_HQ02bD5aIiaB7XwIx9J3jlZCr51AsqGPt2i0M1wbinFEdolE1oChKB9Bp-oWisD0KWY2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
شعار «وقتی بقیه خوابن تمرین کن» احتمالاً بزرگ‌ترین اشتباهی است که به ورزشکاران آموزش داده شده!
✔️
علم روز پزشکی ورزشی ثابت کرده که خواب، مؤثرترین و در عین حال قانونی‌ترین دوپینگ جهان است. اگر خواب باکیفیت نداشته باشید، سخت‌ترین تمرینات و گران‌ترین مکمل‌ها هم نمی‌توانند جلوی افت عملکرد یا آسیب‌دیدگی شما را بگیرند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104142" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104141">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e19dd4c082.mp4?token=pts9kbN8lj3cGWj152p4hdOGKrgU9ximhXCAG9AmITvT3b4RoUK3280LQEm2C0URtiGgU7xgOc9hmBSly9xwcFIwRVN_8a4v0a7H6vEJbxJWbo8_VQcAm3nVEQzhNbqJbcobbukkhw_uQ1c9JnqC-IP8r8ZcjBFkyPJYSCgKJqg5JdKxoHV8RS8RJZA5DhhRWdy-8pi-NChyVmnsPJ-XFN1kRqQEHqTN0LSYlE-wPp3Vfg6wtTHiApF2I8kYCaYUkPa9QsVZSE2fE_R9vz6VD4DAnoZ7y7aoDySJxHNGyxRYO0L4zt9qY4dtgaFx3jvv6a6JC1Verdq4lZrUYPk3rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e19dd4c082.mp4?token=pts9kbN8lj3cGWj152p4hdOGKrgU9ximhXCAG9AmITvT3b4RoUK3280LQEm2C0URtiGgU7xgOc9hmBSly9xwcFIwRVN_8a4v0a7H6vEJbxJWbo8_VQcAm3nVEQzhNbqJbcobbukkhw_uQ1c9JnqC-IP8r8ZcjBFkyPJYSCgKJqg5JdKxoHV8RS8RJZA5DhhRWdy-8pi-NChyVmnsPJ-XFN1kRqQEHqTN0LSYlE-wPp3Vfg6wtTHiApF2I8kYCaYUkPa9QsVZSE2fE_R9vz6VD4DAnoZ7y7aoDySJxHNGyxRYO0L4zt9qY4dtgaFx3jvv6a6JC1Verdq4lZrUYPk3rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
‼️
🎙
رحمتی: کیفیت بازی‌ها در کشور ما مهم نیست؛ مهم نیست کشته می‌دهد یا جانباز!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/104141" target="_blank">📅 16:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104140">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b52b455aa.mp4?token=tSMy9NlTuMgMFC4kSc-xkSJwAO6rnEtKB6OC_P6zAnRWbP7daQOHiQR3bmdh80_b9H1trrj6F0YXPnUU7NTPQ0hnApYNvEyqD39pcHdyigR99ncU0XsZW4meHSKxjqBwvd6LgESb2ywutXf9or942TPeQN6QXaB8VCiGXCTiBwX6jdYknXRupze9XzhbapJCbtxNGgf1qCqCjJ59JfYrFHZ3d3q2jDpZI58N8eU43nWSP7ksEIubsTOgLP80CY0aHJ_tCOJ_VGMKDjCEPTriIIagBl5Jw5hwXSlCM48qrdql751y4QR4tBtwEBYeZTNftM4IOCPbu_xLT2NqRcdrQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b52b455aa.mp4?token=tSMy9NlTuMgMFC4kSc-xkSJwAO6rnEtKB6OC_P6zAnRWbP7daQOHiQR3bmdh80_b9H1trrj6F0YXPnUU7NTPQ0hnApYNvEyqD39pcHdyigR99ncU0XsZW4meHSKxjqBwvd6LgESb2ywutXf9or942TPeQN6QXaB8VCiGXCTiBwX6jdYknXRupze9XzhbapJCbtxNGgf1qCqCjJ59JfYrFHZ3d3q2jDpZI58N8eU43nWSP7ksEIubsTOgLP80CY0aHJ_tCOJ_VGMKDjCEPTriIIagBl5Jw5hwXSlCM48qrdql751y4QR4tBtwEBYeZTNftM4IOCPbu_xLT2NqRcdrQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
واکنش شجاع به خوشحالی جنجالی بعد از گل دوم تراکتور: طبیعیه؛ خیلی خوشحال می‌شم اینطوری می‌شه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/104140" target="_blank">📅 15:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104139">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e36fbbeae0.mp4?token=XImNlDao4YnFZN-g_cFhYjyzV84IWqLMOa7aFY1zJc9ZaONljw_H1twc71_tTxcbeGz9cHKCZPBYIItNsba0QAozh6-N_xBfoEubmJ6f9I2RBQy5jSlGFJpJZNNS-pII9iWrvwLQSrT6-PvIb7YvOIvhMJmmi4m-ZybSu4uwozcakj9t0Ij3FAwOnnUKLlMaRI6qQeda6d5j4LmPJmAut0ihB-xFk1Me5FTW-8zQBW_OeRfTWbaokc3yDd4x0QJgApaOnZCV197aswwU5wrwoGPKlbGWtHbnqWW4vHocuXf957_mU5XUJR7J0QfvCF1vVygmKiaZiSDLfnSh9UyjPXLvHGAHk32UC90rcoBYG2apRHIShzYX-tB0_d8tkNpD-E43Kbr8lF5OLmn-kfJV8pbK1jtsMfS_uDtvb5psJP19IVPeaKMt38rzz8RbaKgKk5jpBrsGwrwAWqNqnQBGEXtpVygnBhlbFfOD126WZQrlG6NxaJNbidLss3ZcnWKyGn-_jMy7V4VX6Hm_sNK0PTmMJiRwDqys8lwQHt1DVZQStyUnQb6zgMHS5AS86uicHou7oDZw40cA973xqE8aB9Xkv7SpCU-H-YWDPS74ywR15NLl6arHrsRAsIRjZUjJgwGu1Yo8gnybIIu27_sM1oyZWKpjGqoK0hiM-rVXfqc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e36fbbeae0.mp4?token=XImNlDao4YnFZN-g_cFhYjyzV84IWqLMOa7aFY1zJc9ZaONljw_H1twc71_tTxcbeGz9cHKCZPBYIItNsba0QAozh6-N_xBfoEubmJ6f9I2RBQy5jSlGFJpJZNNS-pII9iWrvwLQSrT6-PvIb7YvOIvhMJmmi4m-ZybSu4uwozcakj9t0Ij3FAwOnnUKLlMaRI6qQeda6d5j4LmPJmAut0ihB-xFk1Me5FTW-8zQBW_OeRfTWbaokc3yDd4x0QJgApaOnZCV197aswwU5wrwoGPKlbGWtHbnqWW4vHocuXf957_mU5XUJR7J0QfvCF1vVygmKiaZiSDLfnSh9UyjPXLvHGAHk32UC90rcoBYG2apRHIShzYX-tB0_d8tkNpD-E43Kbr8lF5OLmn-kfJV8pbK1jtsMfS_uDtvb5psJP19IVPeaKMt38rzz8RbaKgKk5jpBrsGwrwAWqNqnQBGEXtpVygnBhlbFfOD126WZQrlG6NxaJNbidLss3ZcnWKyGn-_jMy7V4VX6Hm_sNK0PTmMJiRwDqys8lwQHt1DVZQStyUnQb6zgMHS5AS86uicHou7oDZw40cA973xqE8aB9Xkv7SpCU-H-YWDPS74ywR15NLl6arHrsRAsIRjZUjJgwGu1Yo8gnybIIu27_sM1oyZWKpjGqoK0hiM-rVXfqc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😞
وضعیت فوق‌کیری نیکولاس‌زوله ستاره همین چند ماه پیش دورتمند و سابق بایرن‌مونیخ که از فوتبال خداحافظی کرده و اینجوری وزن اضافه کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/104139" target="_blank">📅 15:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104138">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0708d4aa6.mp4?token=tGgJjEaq-PpxiguF6HVLu841x_bzroM4FJYr8SGz2Vzf7I5oCAD8OYRFPpoxw32BBVkxBAB4VDt5J0pfiHrME254YxTla8KUwOiNQSuJ5mcTjJgxQs4HWJf8gKbBSQQbwr2Lyu7f0d2C-1lEUjkBTgnvggzhrCA6NQ-hyCPmPYZZeRuXdEjPUn9rfEsh3_RcqRu0riUlyRrsdOW5k_tOwEzRkWeRxO6oPpKdXFa0vfwf-GmJpzoIGrtpAJIq-e_5zg1vGUWf7yx5_6Iu5Kepjj8Y2Hry1dVZLMl-sz2yMymVaqZCrgGFS48h6giAyFRWsttsoR-fhSM7_VPKVKydUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0708d4aa6.mp4?token=tGgJjEaq-PpxiguF6HVLu841x_bzroM4FJYr8SGz2Vzf7I5oCAD8OYRFPpoxw32BBVkxBAB4VDt5J0pfiHrME254YxTla8KUwOiNQSuJ5mcTjJgxQs4HWJf8gKbBSQQbwr2Lyu7f0d2C-1lEUjkBTgnvggzhrCA6NQ-hyCPmPYZZeRuXdEjPUn9rfEsh3_RcqRu0riUlyRrsdOW5k_tOwEzRkWeRxO6oPpKdXFa0vfwf-GmJpzoIGrtpAJIq-e_5zg1vGUWf7yx5_6Iu5Kepjj8Y2Hry1dVZLMl-sz2yMymVaqZCrgGFS48h6giAyFRWsttsoR-fhSM7_VPKVKydUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🇮🇷
😢
مهدی‌تارتار: بازی مالکانه را از پپ، بازی دفاعی را از سیمئونه یاد میگیرم. ضربات ایستگاهی را از آرتتا و پرس را از کلوپ یاد میگیرم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104138" target="_blank">📅 14:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104137">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f2ef998c3.mp4?token=ZRLgVX6tyeYY0uR5j-xwtpP_g5YwATCxhcUueCeKEVcRpHPN_-uCZ6iMjTS0IuFcalw3ZH8TEgPj8KIVGWMo_zLc-90Wg2Bm5xjp6yxZKww1TWx9PIMMHc1fhxxt_WRLdpgEuGfONmQPUjUEUTGei_QdUoW1rlkqZLoMYAz781szW45nU9_sbivTso05u2_quq2xdhwi2PXhN1tAdErUUs1_N4UHhyJfrRdFzrmkw6hx32-Ujr_VsPc8XaWB5IxgD30TtpSuHnqArMc5xLgWAJTJfLzmXES8gsJPmVGXwvgA3UkvbtH9teU3pYT2DdAiJ-S9VD1IZlMqG50GQO8YMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f2ef998c3.mp4?token=ZRLgVX6tyeYY0uR5j-xwtpP_g5YwATCxhcUueCeKEVcRpHPN_-uCZ6iMjTS0IuFcalw3ZH8TEgPj8KIVGWMo_zLc-90Wg2Bm5xjp6yxZKww1TWx9PIMMHc1fhxxt_WRLdpgEuGfONmQPUjUEUTGei_QdUoW1rlkqZLoMYAz781szW45nU9_sbivTso05u2_quq2xdhwi2PXhN1tAdErUUs1_N4UHhyJfrRdFzrmkw6hx32-Ujr_VsPc8XaWB5IxgD30TtpSuHnqArMc5xLgWAJTJfLzmXES8gsJPmVGXwvgA3UkvbtH9teU3pYT2DdAiJ-S9VD1IZlMqG50GQO8YMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نمایی دیگر از حرکت جنجالی شجاع خلیل‌زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/104137" target="_blank">📅 14:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104136">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34bfc2ef34.mp4?token=j1zO9VvaDHSY3tNEdSwSN-S5cNeMGoW9rrhuh3ka8Kwccu7kBtlMEVuITo25CGFZo8cqQ_u8lsR_8foGQOMmpopP5fsFYDxf-K-yuAHWpkoN00qWY2gdkR28OkbWQMupQ04MW5bwywOsPWU0hAYU-xDN98MvfwBBGMDCmTMkyOQJyyFU72SAelQv8o96sCm3G0Jt8ly56gcbtbV6g63Uj6hwO5GWiV7B1cuXh8dqeOkI27sJ3Ei8K9ga79umNTLtaoQ4jdOExK2uAbWimyiOYYn6aFkaNLdU3AQ8-2NHzTZprZHqqNfnV3DUbW8LRFvn9S30BoU3CeA6w60RnZauVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34bfc2ef34.mp4?token=j1zO9VvaDHSY3tNEdSwSN-S5cNeMGoW9rrhuh3ka8Kwccu7kBtlMEVuITo25CGFZo8cqQ_u8lsR_8foGQOMmpopP5fsFYDxf-K-yuAHWpkoN00qWY2gdkR28OkbWQMupQ04MW5bwywOsPWU0hAYU-xDN98MvfwBBGMDCmTMkyOQJyyFU72SAelQv8o96sCm3G0Jt8ly56gcbtbV6g63Uj6hwO5GWiV7B1cuXh8dqeOkI27sJ3Ei8K9ga79umNTLtaoQ4jdOExK2uAbWimyiOYYn6aFkaNLdU3AQ8-2NHzTZprZHqqNfnV3DUbW8LRFvn9S30BoU3CeA6w60RnZauVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ممیزی متهم گریخت، ۲۱ سال پس از اولین پخش  که هم‌اکنون در شبکه آی‌فیلم پخش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104136" target="_blank">📅 14:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104135">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbee7be849.mp4?token=hgCsP_ZFqbmXGLIM0Pro9BxCGS_-DbBrfHTiirKswkewWjCgMvGsG75H_tzroFWYT3-5e4t4QlwTzPx76gNyHBZafVCedt7RC1uGVg6Yuqhmu4gmwjWfs6k_SP04gqrf-aNwhV3J3pUDJ9TsGc78ONIJSnmkzQ6QpOPZWL5BcOeNeL0WGi8cCP3wfCoCL6KwZt336-6th7F8WAiXLH93jiq1E8U6raq4Q5pI9NBXAZN-dhXmgAb08k84Kf5kLnVMI-PfIqRIHpf_fYXpw2m1Dh5924admLcKq49UqwBZdxUb3O3biAB-rNjEQ6Ocus-mx7XVWTebZLfZyf8Raf0FKFpQrRXCdVLzosidMByNrzwZ4pegqN9WTu6QOK05maKA76GtggrSeqzuNAnCX9U0IH11ghpfRMxh1v-XiYh8JqgqMreTPXT54DvHCv7dBqBKV3e9Tek5W0UVZo0-PgQNkQryFxr7MRW3x8k2MPFZ_qaDvJd1BhH5GfZW_N0F1bkjySCn_grirYEbpJ1e6eSdpCO8MciarV2QuFIUpWQi8fgYp4InOUe3AGU3nPhPYzpZA0BI-WRPzqY0XSwUJ4e67w5BS5s8EBOTY5y2HjQz_OFuXZX5T9dqofzBCtTUzH2tQv3yIuxdLUl_IxLgwByJV4diUhjx5vxKYEp3qv5Op1k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbee7be849.mp4?token=hgCsP_ZFqbmXGLIM0Pro9BxCGS_-DbBrfHTiirKswkewWjCgMvGsG75H_tzroFWYT3-5e4t4QlwTzPx76gNyHBZafVCedt7RC1uGVg6Yuqhmu4gmwjWfs6k_SP04gqrf-aNwhV3J3pUDJ9TsGc78ONIJSnmkzQ6QpOPZWL5BcOeNeL0WGi8cCP3wfCoCL6KwZt336-6th7F8WAiXLH93jiq1E8U6raq4Q5pI9NBXAZN-dhXmgAb08k84Kf5kLnVMI-PfIqRIHpf_fYXpw2m1Dh5924admLcKq49UqwBZdxUb3O3biAB-rNjEQ6Ocus-mx7XVWTebZLfZyf8Raf0FKFpQrRXCdVLzosidMByNrzwZ4pegqN9WTu6QOK05maKA76GtggrSeqzuNAnCX9U0IH11ghpfRMxh1v-XiYh8JqgqMreTPXT54DvHCv7dBqBKV3e9Tek5W0UVZo0-PgQNkQryFxr7MRW3x8k2MPFZ_qaDvJd1BhH5GfZW_N0F1bkjySCn_grirYEbpJ1e6eSdpCO8MciarV2QuFIUpWQi8fgYp4InOUe3AGU3nPhPYzpZA0BI-WRPzqY0XSwUJ4e67w5BS5s8EBOTY5y2HjQz_OFuXZX5T9dqofzBCtTUzH2tQv3yIuxdLUl_IxLgwByJV4diUhjx5vxKYEp3qv5Op1k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
اخباری، سرمربی چادرملو: نه تنها از ما عذرخواهی نکردند، تهدید هم شدیم. از این‌که جای تیم ما به آسیا می‌روند از خودشان بدشان نمی‌آید؟ امیدوارم باعث‌و‌بانی شرایط روحی تیم من شب راحت بخوابد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/104135" target="_blank">📅 13:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104133">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJAmBud0tpMfccagx67_mrM-7r8tpZPRdLDZPRyJp13H9ru-aHImHuNjfY_C3MdbbMRHVTEeq6ay-04YxIqbuTUx-dsddvuzAqsEZph3lgyLs2I4KI0_x0xzQYkZVTGlDAJ_locwD7wPXy3LkVZniISxdgPoK39yXS47XEjA0M5iuZ7-uzQWz7pFLCnFM3bQW-_sL5ApdokuJZhdveQ2OHvdEQl8Efo9adoK1iCMX-DsnIHFfCps8Aat7oo3CUSqZ9IwAowSHvcTc_1UfYREQU9MjHh6I6fNU16Hl85vcXf1DNQFI3M8s271_pbC61grB0jjIiTGu1XvEYbXLRDgJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
استوری جدید رضا علیپور : جنوب لبنان که چیزی نیست تمام دنیا فدای یک وجب از خاک ایران.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/104133" target="_blank">📅 13:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104132">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947d3a1948.mp4?token=KLw418Dh4gqalxXvQ9b-fLoQVLT-bmdtqzd7XzABeMw0u48omZDsa7XM6bZR9BHc-qO3OfjRkqQZzaaWU4eFOgmjTlP7NWEUR6hBN0yjAzMMwws17oMAtvXAZozuhQugxnfRjM2UlP0jU4z_V4PqJ0sB0GmSGF0CkQVh1Ov6SHq_9vXAfthYkFZlyB2T-G6TXtdtBu10u8iGGBZbJxrVZOEG3wXZgp13j9v4Z4aitrBgI2iVcoOW46q5MKpW-kC890bojThoxCxHr9nBJc-FDMdmd7GEKag0rbVfuqz4UUHzWwFfC5haRWJQG4Ab8HghmRFJHQNH7rOwUXMDYMZdIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947d3a1948.mp4?token=KLw418Dh4gqalxXvQ9b-fLoQVLT-bmdtqzd7XzABeMw0u48omZDsa7XM6bZR9BHc-qO3OfjRkqQZzaaWU4eFOgmjTlP7NWEUR6hBN0yjAzMMwws17oMAtvXAZozuhQugxnfRjM2UlP0jU4z_V4PqJ0sB0GmSGF0CkQVh1Ov6SHq_9vXAfthYkFZlyB2T-G6TXtdtBu10u8iGGBZbJxrVZOEG3wXZgp13j9v4Z4aitrBgI2iVcoOW46q5MKpW-kC890bojThoxCxHr9nBJc-FDMdmd7GEKag0rbVfuqz4UUHzWwFfC5haRWJQG4Ab8HghmRFJHQNH7rOwUXMDYMZdIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❗️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تصاویر تازه منتشر شده از صحبت‌های پپ گواردیولا در رختکن منچسترسیتی، پس از باخت ۲ بر ۰ برابر دورتموند در چمپیونزلیگ⁣
پپ: احساس حماقت می‌کنم. می‌دونید قراره چی بشه؟ قراره یه مربی جدید داشته باشید. از این عملکردتون خسته‌ام و احساس تنهایی می‌کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/104132" target="_blank">📅 13:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104131">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🇮🇷
❌
سرپرست باشگاه نساجی: تا این لحظه مدیریت باشگاه تصمیمی برای شکایت از استقلال بابت بازی دادن به یاسر‌آسانی نگرفته است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/104131" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104130">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGMnbTmoFf_Ta6_LklA_hD5FWP5VJm1fHpBtpQpzmdUY4yiDRSw86Ys7zTU7lJNcRvrdD_wqPwys2u-Iik_C-aNnNVvIuehzBXNjXzr4QeraMFVI8NGPEavk9gRZM5A-jtVVewvQ5tKbo4n7u67XiB21bm91D1ewNX-H72PtdTaTPXnCLfCv5kLyurrMLK15hH8qbSQ04E_ZqFOUPYSDGV5dy2tXv88F8Iq5rha9a-egElgiq83X-8F_6l-zEepF_dRRpLTiofCxgaxYBWZoj8FKK1ZdmsdrP7rFav_qj3bNWZr8Bf0xGcl4XN73BaERzEHtSvEoJGhK0ffo_DOG0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتین: یونایتد برای جذب کارلوس بالبا از برایتون با رقم ۶۵ میلیون پوند به توافق نهایی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/104130" target="_blank">📅 12:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104129">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxQbMkZfKYsD5KU82szAqlddDg3TMlirJ0Ze_zqcaR54N0NB56Nln4kC_vxwSOPUmvLvpVg-vy5dj-0HRfbim_vcBPlOAeH7C9MhzNiLzk8wZ5FEznj-fNCtd-pUN0XS9-BuZM-G9Egvf9G8lU6l9XkRMNS6SsXjb5InO1M0i96V31sA73ESkDvjYx05drchXu0w1e59CAXG1x9nvDouk1_Ly3NuHbL-PdlPYZ5pFNeYUKX42c9wJkDHZ_92qIID73zgZKVGlp4ag9H6glI8KkwvcM88nZ8V1sfWTiiLvBZ-GTeTy-onIyRv8FkvymYgBueSNr98lX2B68ArOLFM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: ژائو پدرو قرارداد خودشو تا سال 2032 با چلسی تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/104129" target="_blank">📅 12:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104128">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🇮🇷
❌
سرپرست باشگاه نساجی: تا این لحظه مدیریت باشگاه تصمیمی برای شکایت از استقلال بابت بازی دادن به یاسر‌آسانی نگرفته است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104128" target="_blank">📅 12:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104127">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3V0_R6iTYiUCuM0fktnnQOUrbO5XTDYf8ymJr648NHwWP9f5gKiLUvIyH2vWR3idPBhb8Mk627AAMhznFVt8LM3R8Xy4ea1D8fSrjn373ka5QBmcwAx7Pia7Rfu2Glu5uxufbX2qNv4sJl_s7PGt1bpjxWzvjMAoDmtmXJA30GdcXVbjvf3sYDjqNbaR02rV28RZa_6KjD3q74VdQwWZ-2ftqzsubEzQwvuXDNN6kfl4K2YsrT8cxiV0IXbj5cd7V8WcmhHF7UC0w3lsLC-oRCzrOJeezDubehpHaUCzjPyPW_P5FLXf9xZjb6larkmAMD29bOhY3cw9He8kskdYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇫🇷
#رسمیییییی
؛ باشگاه موناکو به صورت توافقی قرارداد با پل‌پوگبا رو فسخ کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104127" target="_blank">📅 11:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104126">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctUMxCUdFAGSGETaMG_V8TBu3ZCXHLE_cZCD21ogZoUFyvgfaVOlqdkZSfkFtASRlHaS69igrXwsIt9G3QidYWPfz0sjx76EkuU-saQu9yMiacq0ZkssVcWOCv-pK2xeGRO4tGrg6kU9Z60YvScwcbPr36vt-ap3tkYC_IkmFf3uMBOl7zCChnIm4Vn8XJEJEEqd2p-F-kYZpJIw1vowbMqQox8e4Du9JnbLw-5-aRX7yPPCSl8kN1B7CkGCSmFmYeMRJZqLpsPV-5OHck3J_JqyKVTVnr2gRdQq82UILUhbqEDesxQcxJylnxKyG0tDHqyE4BbSjfdadcnvJa1QmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
روجری مدافع اتلتیکومادرید و سوزوکی سنگربان تیم‌ملی ژاپن به استون‌ویلا پیوستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/104126" target="_blank">📅 11:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104125">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1154898c2a.mp4?token=JtG-A6906QxkRJdsVGe68L24Tn2VlxiqG11fU_jovIqHNT0FYP4FrfU6IT_FHPndLs7Yhvi9XtfvruBfNECIEKziN8lO_NsGS4RojDG0_0vN4u9WAxZArmLtR48X6UMbkoWy7pfBLJneSOIuHkwlluBZ29N0nhmwROVCrrvnaXffKDIWjiwWnu169i2DMySxLn5U_-oF_VLZFVIfSNK-WJea13cb1w8VcLkY-DVcdI7Ec_u7Jg7Zff4v4ixyE420KzDNeo1nLVQ60XV-QvgDTG7K9IjDee2uNHL2IG7_UIDVGMkd5rYqkxQUyG_eC5lxdSSBzKOky3ZhFJ2ODWVtVLS02T2t5CHUltvV__CEfTX7yapcS3Iv2gboZWdp3_oG_me7_QzhQXL9O0I4SU8u7B-eTXAq8ZS7p3a_I4O4O_Ga5eu1Eh4lwSMI9GNXDof8wK0qnuEJA7RqZ-uBZsYrJuTyttsM7enpuNsIeNPf_n71q5eluWkvRd7DsVt-I_TXrukJ68GKJdq3VxDvJ9ztj7F0iaRVM-KtjgT1Zn5qgt_UMSc_-fDrflZCB64_zOTN5eNjA6I-0z9ZGSKXO2GslmRizLJmecOiBBqUkRNwl3c2xj-s-lPh2x0nQrgYuHz4CCUVTQN8zr-6iVkxkM_2hUw0Yl_zy3cMRndo_xOY_-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1154898c2a.mp4?token=JtG-A6906QxkRJdsVGe68L24Tn2VlxiqG11fU_jovIqHNT0FYP4FrfU6IT_FHPndLs7Yhvi9XtfvruBfNECIEKziN8lO_NsGS4RojDG0_0vN4u9WAxZArmLtR48X6UMbkoWy7pfBLJneSOIuHkwlluBZ29N0nhmwROVCrrvnaXffKDIWjiwWnu169i2DMySxLn5U_-oF_VLZFVIfSNK-WJea13cb1w8VcLkY-DVcdI7Ec_u7Jg7Zff4v4ixyE420KzDNeo1nLVQ60XV-QvgDTG7K9IjDee2uNHL2IG7_UIDVGMkd5rYqkxQUyG_eC5lxdSSBzKOky3ZhFJ2ODWVtVLS02T2t5CHUltvV__CEfTX7yapcS3Iv2gboZWdp3_oG_me7_QzhQXL9O0I4SU8u7B-eTXAq8ZS7p3a_I4O4O_Ga5eu1Eh4lwSMI9GNXDof8wK0qnuEJA7RqZ-uBZsYrJuTyttsM7enpuNsIeNPf_n71q5eluWkvRd7DsVt-I_TXrukJ68GKJdq3VxDvJ9ztj7F0iaRVM-KtjgT1Zn5qgt_UMSc_-fDrflZCB64_zOTN5eNjA6I-0z9ZGSKXO2GslmRizLJmecOiBBqUkRNwl3c2xj-s-lPh2x0nQrgYuHz4CCUVTQN8zr-6iVkxkM_2hUw0Yl_zy3cMRndo_xOY_-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
خیانت در رفاقت؛ افشاگری محمود فکری علیه قلعه‌نویی؛ فکری مدعی شد در چند مقطع گزینه مربیگری بوده، اما بعد از مطرح شدن نامش، امیر قلعه‌نویی فرد دیگری را به‌عنوان گزینه معرفی کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/104125" target="_blank">📅 11:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104124">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/104124" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/104124" target="_blank">📅 11:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104123">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iC9bZvBl8Sn29pdznUw9zfHe_jO6eSYZ9-oii1WtYYdi7u0zI8BpW68xHt87jRb7YJimtQk7zJDJfdilL-D_fq_u0Bj9yAe3_679-wOqNgGQsLJlptyJxuCU0KYNp1Pr7adZVxM8zJx52uD7367M8tyQnQoWN3_zpX5MZ28VdzP3LC1GNWY81eKnwoKa8Sjec68SaO-GO9UNt9KtEypc3SK3GufQGBJVs3q6edEmzi9XTZ0bRr9zJ_JmAouLSRiZBx1Yx0UTL6v-d51k396b3h9iDRkeKAX36cTIB8Z9bc5Z83PhPvYcywliVq4F20wE11VLWlswSttzq8ohre3z2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سایت جهانی  و معتبر
#Melbet
🔴
بازی های مهم 27 مرداد
🆗
ثبت نام آسان و سریع کلیک کنید
🆗
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
پخش زنده ی تمام مسابقات
✅
درگاه اختصاصی برای کاربران
👍
پشتیبانی 24 ساعته فارسی
🎟
Promo Code: MELBET90
🇩🇪
دانلود اپلیکیشن MELBET
📱
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r28
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/104123" target="_blank">📅 11:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104121">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86c426300.mp4?token=grYdrIkQ2deeJ07FDU_ZfY2-rTjHOL-kFWezNM1Oa81pzC07YEXjMY3camhLEGBk3LTHKCupFuPDnjSf6QdD_k0wywUkd-qRsssH4FfVskgybP0yk8XxUGItry7kOJ7amE-hBNujMoKcjvNhkwAAqwGSQ8IfthsZGQeNSf6YyT4uXpebglJ_3xrMJGV4U7XttDF1orfUO_JsfwmX1y8l1K_aTV06g_tzLvwCSm4KEo7llBrwnZk10rWLM70bMwvox2m33tt7HiOWOCvAjE4zczv9FqwqvxwCCzpfrTcITh_m9WJoq6eb7BMW3O86iVhPiaI0Mb0LNrdPZefYy3UPPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86c426300.mp4?token=grYdrIkQ2deeJ07FDU_ZfY2-rTjHOL-kFWezNM1Oa81pzC07YEXjMY3camhLEGBk3LTHKCupFuPDnjSf6QdD_k0wywUkd-qRsssH4FfVskgybP0yk8XxUGItry7kOJ7amE-hBNujMoKcjvNhkwAAqwGSQ8IfthsZGQeNSf6YyT4uXpebglJ_3xrMJGV4U7XttDF1orfUO_JsfwmX1y8l1K_aTV06g_tzLvwCSm4KEo7llBrwnZk10rWLM70bMwvox2m33tt7HiOWOCvAjE4zczv9FqwqvxwCCzpfrTcITh_m9WJoq6eb7BMW3O86iVhPiaI0Mb0LNrdPZefYy3UPPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🎙
حمله مجتبی‌پوربخش به صحبت‌های اخیر نوید محمدزاده درباره فلسطین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/104121" target="_blank">📅 11:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104120">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66827eb6c.mp4?token=XegqWIdU7pu2CvQ4aaYFfcWGIV1FPyA97zei90Beae-zmRMXB_-ATMwbnidUeCRjg-52lT9duYv5McpzrJHIRB2Wm3bjYYjyu7dOn-YHqaIEYnayjxILtQqdTcv34_xXyouaQpY7uZVWgq48KbP9QTuKK0RwqrHLL0kc1xRCvy7QtCYE6jc9HE6jGJIMLv0gyd25jzNf3GHJDHtPEpfJw8T2METZcBNB-QgYt-79_jU5Z801nD2T26kh-dhD-ZB9Slw28iOxehkxjYlzNDIIwfS_5SPAXG2B1QPRsiYRII__ZH5NN6CkXBS3diSEaAtO3ys6d0mSFOIVrorjzzA_tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66827eb6c.mp4?token=XegqWIdU7pu2CvQ4aaYFfcWGIV1FPyA97zei90Beae-zmRMXB_-ATMwbnidUeCRjg-52lT9duYv5McpzrJHIRB2Wm3bjYYjyu7dOn-YHqaIEYnayjxILtQqdTcv34_xXyouaQpY7uZVWgq48KbP9QTuKK0RwqrHLL0kc1xRCvy7QtCYE6jc9HE6jGJIMLv0gyd25jzNf3GHJDHtPEpfJw8T2METZcBNB-QgYt-79_jU5Z801nD2T26kh-dhD-ZB9Slw28iOxehkxjYlzNDIIwfS_5SPAXG2B1QPRsiYRII__ZH5NN6CkXBS3diSEaAtO3ys6d0mSFOIVrorjzzA_tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
✅
نورپردازی جذاب اطراف استادیوم نیوکمپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/104120" target="_blank">📅 11:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104119">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhIdRW6bQeaXf1cWoOSCi4H_32yyHS3dIAhhc1YKerwJ0Ifex6BR-ri0__nXnI8MjtpnHFC6Ws3SCuRHfclsKrLR1NQrOg59wnNV2nLmupfGqVa_Xvcmh54RD-Emvzlj1BUQRKx1DoW-ZGlMVDVSUr40i2AaQUMnPAHW9I17UrcOoqHZ7JX8ErdV3901X08jECHeXyPOG2AOh6Xmocw1dWadSCozHxSIFDUagIVODCUjvWO8bzTjtLrNdhHo0U8aMCOMyOJyjMGZutOi-jIF_ImB5ah1L4lgd5jZ_2EEvH5eX53BoMSgMhDGwIhCpvLApPiNIeZp5WyvVEW73jOEIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
🇮🇷
🇮🇷
پوستر ذوب‌آهن برای بازی با ملوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/104119" target="_blank">📅 10:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104118">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SU6MuZFRUhjzI57QLTl3Qnmn9k7XUOv3Vxh5-52haeWpNcIm1cosyBkHwQxv10HN01FJVI_n6O0Q8i9SYDWjbk5dsakH686OiuDLnoXQACGOgK1Qa7ym6WybMpdvGJJ8TVchL9S1nk_LLFv53oZdbLzLYZpgbm-eFn5bY_kfAVmEJ-VQmPjuTJH0MPue9k_RwQy5CGL9q2vQVHxu2hPteCfaJIRrqC3iAUW5XTEOrxQIOwG9r_sI4v4B2um97owapwfmaQCtogqe0cDbyil-VODFipIjJyPMFAdWOqy2DgqgdDhT6X5DYSWj2NB8AHrh6lp_UhxPn8i0KDDkqtyiiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇪🇸
ژوزه مورینیو سرمربی رئال‌مادرید:
🔻
«چندین بار با رودری صحبت کردم. رئال مادرید پیشنهاد مهمی به او ارائه داده بود و رودری هم تردیدهایی داشت. همین تردیدهایی که او داشت، باعث شد من هم دچار تردید شوم.»
🔻
«رودری بازیکن فوق‌العاده‌ای است و در تعامل با ما کاملا محترمانه رفتار کرد. هیچ نکته منفی‌ای ندارم که درباره او بگویم. اما فکر می‌کنم باشگاهی در حد و اندازه رئال مادرید نمی‌تواند بازیکنانی را جذب کند که برای پیوستن تردید دارند و دو بار فکر می‌کنند. با این حال، او رفتار بسیار محترمانه‌ای با ما داشت و برایش آرزوی موفقیت می‌کنم البته نه موفقیت خیلی زیاد!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/104118" target="_blank">📅 10:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104117">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dc45d865c.mp4?token=IxpGMcXnrmpKOhI7r7TWIg1sA_zhq12uPbOG4Cp9YcMoZrI_Ce6G765r4OB29cOIdwnWXQT8dFERk07Vk3Uf7Wk4MO6FDFT7BGq6oW1WN_mvv7_bosMhvZPFl8jCV4-y6Wv0QwuQQiom-rLLDmXKg57TJgHQ_R3gmRFNVPgjmYl2x1ZG9Uby_39NT1mt4C8RLkJj0Egr5ZXzgaw-FX0fVGBKjmcdy83sgnI50CJkCfVXM93agQrQEngdE1aolr5eS6GGG-Tdzr83nnBDp8SMAaIb2Usb-ytqK-TJwTsQe_5c-Bl3h_VpZt10Gg0tqVHbm0MOBWFQVujo95XjtfLBgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dc45d865c.mp4?token=IxpGMcXnrmpKOhI7r7TWIg1sA_zhq12uPbOG4Cp9YcMoZrI_Ce6G765r4OB29cOIdwnWXQT8dFERk07Vk3Uf7Wk4MO6FDFT7BGq6oW1WN_mvv7_bosMhvZPFl8jCV4-y6Wv0QwuQQiom-rLLDmXKg57TJgHQ_R3gmRFNVPgjmYl2x1ZG9Uby_39NT1mt4C8RLkJj0Egr5ZXzgaw-FX0fVGBKjmcdy83sgnI50CJkCfVXM93agQrQEngdE1aolr5eS6GGG-Tdzr83nnBDp8SMAaIb2Usb-ytqK-TJwTsQe_5c-Bl3h_VpZt10Gg0tqVHbm0MOBWFQVujo95XjtfLBgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی‌کنیم از قهقهه تاریخی منصوریان روی آنتن زنده در جواب صحبت‌های مهدی‌رحمتی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/104117" target="_blank">📅 10:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104116">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a6bb2643.mp4?token=gIkv9LnBts1gbuALVSv0ZQilyv0GWwnEWp8pKi25ghMbAcdr-TNuNKX4VZhBHU_ha-oV_PANrPG2ixRNE6wP0sIHIirpplIL2_TY0Czbe4vUEQM89acyWmTZd_be6M_LkP-LgN_vMlbmJm7skY0o1rZkDwEomV4HU_CsqzF7n_L2DypljzqeQUDQggazH96Xza2ccH3ehKGjFgmM_vNNOQ6qwEemCCTTIDBGLDajlf5CLi606fy-0uBJg6ICj98Rvm1qLK5qBCT8B9V_Rb2LNtAFIohdxECo31LKOI7nQ6vSyHlUArdTpeY6fpvQK7o7GgESN82LjAB7pFDaAAyDghWwJpzHzMR7WlzkWttdYOti-hPuJWH5OHOuTwLqOLGurpJbtNuwmjSc9gGBjyeNVvtJmUqgPtMRbbx1Rg1muHKKBXMt4gFYB8dcu19vMgJERaorSI8dfB0oYsRY-QbvfpJ4WI5lkM1o3iBXn5UAyUihsxZKPPsezESy1EpivqmfOnWlg59vedwTd2TOBzjKmBtbdUOH49_8727aT1tXQbO88vYfzMk8iGjol-_9nPgw-aBqLDbx2YHCsD_P-nMyo5SLmhdRep8aP8KNtxiQDn6XnboniQArCQvlVRNF429p23oWPoxnl7zcpuomMPm-0Z1gmY3euH3PHvzqCU88Ykw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a6bb2643.mp4?token=gIkv9LnBts1gbuALVSv0ZQilyv0GWwnEWp8pKi25ghMbAcdr-TNuNKX4VZhBHU_ha-oV_PANrPG2ixRNE6wP0sIHIirpplIL2_TY0Czbe4vUEQM89acyWmTZd_be6M_LkP-LgN_vMlbmJm7skY0o1rZkDwEomV4HU_CsqzF7n_L2DypljzqeQUDQggazH96Xza2ccH3ehKGjFgmM_vNNOQ6qwEemCCTTIDBGLDajlf5CLi606fy-0uBJg6ICj98Rvm1qLK5qBCT8B9V_Rb2LNtAFIohdxECo31LKOI7nQ6vSyHlUArdTpeY6fpvQK7o7GgESN82LjAB7pFDaAAyDghWwJpzHzMR7WlzkWttdYOti-hPuJWH5OHOuTwLqOLGurpJbtNuwmjSc9gGBjyeNVvtJmUqgPtMRbbx1Rg1muHKKBXMt4gFYB8dcu19vMgJERaorSI8dfB0oYsRY-QbvfpJ4WI5lkM1o3iBXn5UAyUihsxZKPPsezESy1EpivqmfOnWlg59vedwTd2TOBzjKmBtbdUOH49_8727aT1tXQbO88vYfzMk8iGjol-_9nPgw-aBqLDbx2YHCsD_P-nMyo5SLmhdRep8aP8KNtxiQDn6XnboniQArCQvlVRNF429p23oWPoxnl7zcpuomMPm-0Z1gmY3euH3PHvzqCU88Ykw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
🇮🇷
دیروز و رویت اسپایدرمن در ورزشگاه وطنی شهر قائمشهر
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104116" target="_blank">📅 10:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104115">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9xjQBMd6CtDf0I1hDTkXttMjPwzySU_zNB-RMlisGrz3oh8CK4EQX6E8M46iCXcDnACyvQkeIpA1-cWYKCwNR2ldpmGerPHGE2q5An6aGvT-IjGhSFl7f9-cS61J7-J049tv2TIzzlFL_HhuBuDtxut1oijYwE_eRfYDGZ5frefcCcsa-lndbjLJubjeTEzPqa17pSHh3D2PTLaEFYMpMYhxv9_Hix4PZ_VW9XYSVVOh8bW3X51SewEZt012PeqG6IkclFIrXUOuSEphWk7eyKrRRdFwVzy46LX23fzIlxNdlezvwT2YhskjCQK_3pV12lVw4M6gAqb9tWyiR7Hbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
پوستر باشگاه پرسپولیس برای دیدار امروز با استقلال خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/104115" target="_blank">📅 09:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104114">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05a7ace3b6.mp4?token=YHkxDd0-Wfp7lZlSEYiRF18RC9drJgvraZQ-GhyVaL2dVq1PnVkE9c-ejmjO8I4o5CsKf2BaMlpP2foLTOxC1ZJfV3tA4QlxaRpHBH7z1tJrQiV_oWMHfnU9grZs4uiH3aeINGSI1YvN10wKEKtSGK9qPbeb_CVh81fZesEqt171PUtFyS5ZxpkhtUwA2bwYO7sbVnECv3fAL_CmQjKcmf6prwryHb6hQIDkyQjCPRTLcFn5FvY9fK3PAIBUWTjcgjWMwnjfAmcEj_06qFcatvdrkwv6f4S0JDq64W7heAFoxHJtUow6riuW8wT6KKfCrcrVe_-AGEjp7PovMy5beQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05a7ace3b6.mp4?token=YHkxDd0-Wfp7lZlSEYiRF18RC9drJgvraZQ-GhyVaL2dVq1PnVkE9c-ejmjO8I4o5CsKf2BaMlpP2foLTOxC1ZJfV3tA4QlxaRpHBH7z1tJrQiV_oWMHfnU9grZs4uiH3aeINGSI1YvN10wKEKtSGK9qPbeb_CVh81fZesEqt171PUtFyS5ZxpkhtUwA2bwYO7sbVnECv3fAL_CmQjKcmf6prwryHb6hQIDkyQjCPRTLcFn5FvY9fK3PAIBUWTjcgjWMwnjfAmcEj_06qFcatvdrkwv6f4S0JDq64W7heAFoxHJtUow6riuW8wT6KKfCrcrVe_-AGEjp7PovMy5beQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
🇪🇸
وضعیت روزهای اخیر بندگان خدا رئالیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/104114" target="_blank">📅 09:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104113">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8433cd6af6.mp4?token=FhqZVMOe9rdmLF6imPFiUCab696Zp2FGIeKhr1kcWrfcRWlryhAQvpxN4Ac-G6k19GfO9d9JNcrB-1FJhtl-gSqNxNYb8UKE04_l6sjCwb3KmUg0cy1fSaiV8g5TFoRcp7s5SEWj0m3AQ4-XxWILxtPd9G_4gqmnvs4pzHn7uQpZWT6jrG9_64nWtk9VSI1HTsh9pCQdieoVUjY84qKJerpmN1vNqQmQXMiKOn1awcs7PtG0uX-8a-woxym2QlcNVeVaV6LpyNPsdrAL97A8N0b6dL_KnEx6G8CftZGC-L6UckpNe2x2Pws6zag4Jjmu9S3Phxw2Md6ZBjjo2ZmWBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8433cd6af6.mp4?token=FhqZVMOe9rdmLF6imPFiUCab696Zp2FGIeKhr1kcWrfcRWlryhAQvpxN4Ac-G6k19GfO9d9JNcrB-1FJhtl-gSqNxNYb8UKE04_l6sjCwb3KmUg0cy1fSaiV8g5TFoRcp7s5SEWj0m3AQ4-XxWILxtPd9G_4gqmnvs4pzHn7uQpZWT6jrG9_64nWtk9VSI1HTsh9pCQdieoVUjY84qKJerpmN1vNqQmQXMiKOn1awcs7PtG0uX-8a-woxym2QlcNVeVaV6LpyNPsdrAL97A8N0b6dL_KnEx6G8CftZGC-L6UckpNe2x2Pws6zag4Jjmu9S3Phxw2Md6ZBjjo2ZmWBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💦
بارساییا چند روزه حسابی دارن ارضا میشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/104113" target="_blank">📅 09:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104112">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d73d093cc.mp4?token=Emv32Nw5kokELbOGkj5-ILE4uqpT_tg3WXQjy122SqFtW3rhXVjJi61C-DMkSjVh95VcgHpIGP8JFF_4RRi04T83t-DRGyON7x9NMgTd7C4GLXLrUdghlezDzmQF3zkHl0vqJBenX-_B1QPCstetR8Kp7rbgb12-Sr2QrnTozj7kwaMQy9rTvfP5d0tgHCON-iu3lpuUEsJE9__jqE4jZ0xIN5yxuHXWvkkqNP45PxmtY60q8paed0AOt_HD4fGFADq0SJZ-P2Kx5kCh6-TlsIO4L78QhsrJkFQCGy7wGKwJ6HLHe2pmWR4TM9plbZT-6MHNBqPuVt1hW9VkZniFuoS49ezJowYrwcYqFneklFfxkLdD1CNk2VeGJBo30Hxrjgc7vRuVXH5pCXh0-hRo8A4crd-UBnkhI6y9wifxELvADBEPpG_oy-CIvw7tDcwJDJ7FWZbL54O-T39I3u5jYJqXJ6S9EFj81O9cP7mmf3RqXyB8IfOqwUJIUoCu18I06M18jDAws6blLxfzz8nPgxBqTQZ50DVBYevX_ca4FqAl8VRSPSAXaXuOOEZ70IdmUcyPKdQ5KQDnZ7sv0UPWPzp3zhS58zzeE-VA8FIQfuL5bhFqLHyJligw1o-DX6y1D9BoYW5wDy22EXc07qdeUX_399a1xYTeJyR4luc-gRE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d73d093cc.mp4?token=Emv32Nw5kokELbOGkj5-ILE4uqpT_tg3WXQjy122SqFtW3rhXVjJi61C-DMkSjVh95VcgHpIGP8JFF_4RRi04T83t-DRGyON7x9NMgTd7C4GLXLrUdghlezDzmQF3zkHl0vqJBenX-_B1QPCstetR8Kp7rbgb12-Sr2QrnTozj7kwaMQy9rTvfP5d0tgHCON-iu3lpuUEsJE9__jqE4jZ0xIN5yxuHXWvkkqNP45PxmtY60q8paed0AOt_HD4fGFADq0SJZ-P2Kx5kCh6-TlsIO4L78QhsrJkFQCGy7wGKwJ6HLHe2pmWR4TM9plbZT-6MHNBqPuVt1hW9VkZniFuoS49ezJowYrwcYqFneklFfxkLdD1CNk2VeGJBo30Hxrjgc7vRuVXH5pCXh0-hRo8A4crd-UBnkhI6y9wifxELvADBEPpG_oy-CIvw7tDcwJDJ7FWZbL54O-T39I3u5jYJqXJ6S9EFj81O9cP7mmf3RqXyB8IfOqwUJIUoCu18I06M18jDAws6blLxfzz8nPgxBqTQZ50DVBYevX_ca4FqAl8VRSPSAXaXuOOEZ70IdmUcyPKdQ5KQDnZ7sv0UPWPzp3zhS58zzeE-VA8FIQfuL5bhFqLHyJligw1o-DX6y1D9BoYW5wDy22EXc07qdeUX_399a1xYTeJyR4luc-gRE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمرینات مشترک وریا غفوری و امیرحسین حسین‌زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/104112" target="_blank">📅 09:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104111">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffae02c927.mp4?token=LncmiRhbq8B17C0VZ_oefA5DXCMW3XO_zRcZW6G6bpP6uo7xZB4Oo44nkeKowiw-nTet4OnmO97CduesQoF1fGIMpF2DkyheWOMxJDbgxlPgldSQeq--pCpJ5YGgKza70Vw7kCakt44nieVcRz5S-JvQ2OFzGmzjS4rjhgsnWShaBEvhPSAC9XufOhwKUoXmwt897--rKmZ0_sbhWb1z75-EDZvScesyEypL4YZTJ-0lxqtsa0WXGaGnr0DpxehIAE6TVc68CQ5myjP_PIdQqi-txd-ZGeg7_GhAvp98EjYJAexUC9Ky2f6LeNe0kG2jD2Dp_UY99dvvePX41eDNgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffae02c927.mp4?token=LncmiRhbq8B17C0VZ_oefA5DXCMW3XO_zRcZW6G6bpP6uo7xZB4Oo44nkeKowiw-nTet4OnmO97CduesQoF1fGIMpF2DkyheWOMxJDbgxlPgldSQeq--pCpJ5YGgKza70Vw7kCakt44nieVcRz5S-JvQ2OFzGmzjS4rjhgsnWShaBEvhPSAC9XufOhwKUoXmwt897--rKmZ0_sbhWb1z75-EDZvScesyEypL4YZTJ-0lxqtsa0WXGaGnr0DpxehIAE6TVc68CQ5myjP_PIdQqi-txd-ZGeg7_GhAvp98EjYJAexUC9Ky2f6LeNe0kG2jD2Dp_UY99dvvePX41eDNgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حسام‌حسن سرمربی خایه‌مال تیم‌ملی مصر دیشب یه مراسم تولد میگیره برای خودش که زن اول و دومش هم دعوت میشن. این دوتا زن وسط عروسی دعواشون بالا میگیره و حسابی همو کتک میزنن که باعث میشه شوهرشون غش کنه و بفرستنش بیمارستان
😂
😐
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/104111" target="_blank">📅 02:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104110">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b18e42b10.mp4?token=tLJf8-eKaY_zDvvOhuEsER9IaxCurGvHdj3PKq-oK1GSLxbzlq4uq0fPnr9st2LLDWZRS2JmDY4Mw49_Ke-38CbjEtiLEVp-87c96mY1BLEZGHmkWsylCgsxp476q7mR9IUtd9lh5f279Bh1MManP9gK6Rs8Op7EeKmNQ-6h_tV_BBYl475l85htChSOWRKLB4PO6c-m1ZoVNES_ZaKn1U5S3t_uSW7xChp4p63J8CgA-NBVur4CQq0xUoNuuOFiC-uRweRvCM2gb6Mw1XRVy_FHG4fg-7VbuDtm7scffQ6FZftNIQFdEPEEoJ2gd8ZMgkJTQq33y3gIcq6I_mTieQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b18e42b10.mp4?token=tLJf8-eKaY_zDvvOhuEsER9IaxCurGvHdj3PKq-oK1GSLxbzlq4uq0fPnr9st2LLDWZRS2JmDY4Mw49_Ke-38CbjEtiLEVp-87c96mY1BLEZGHmkWsylCgsxp476q7mR9IUtd9lh5f279Bh1MManP9gK6Rs8Op7EeKmNQ-6h_tV_BBYl475l85htChSOWRKLB4PO6c-m1ZoVNES_ZaKn1U5S3t_uSW7xChp4p63J8CgA-NBVur4CQq0xUoNuuOFiC-uRweRvCM2gb6Mw1XRVy_FHG4fg-7VbuDtm7scffQ6FZftNIQFdEPEEoJ2gd8ZMgkJTQq33y3gIcq6I_mTieQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✔️
🙂
تو میدون انقلاب تبریز یه پسر برای یه دختر ایجاد مزاحمت میکنه بعداز تذکر کسبه باهاشون دهن به دهن میشه و در نهایت کسبه میگیرن میکننش تو سطل زباله
...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/104110" target="_blank">📅 01:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104109">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
عجیب‌ترین هوادار بازی امروز استقلال و نساجی و مصاحبه سراسر سمی‌ش
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/104109" target="_blank">📅 01:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104108">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mB_fOQmCEl_L_XuiD8ZtX2R-unUDWG-gYqaQOi4G1o4ICCelND3lhqLASHPlv9X11V1Rcq1RGxe_8cx2hc1bqf1piF_mq_LTRc8ZekUMEKrhY13yBKIl1GTSn7vY75yqrL_YUvi0kygeHBpVlOu_ISePpbQMssHBpK09cJR_W9EOCCSYGt4hTqztTS3WWRlz13yFf722hytGUs2LrkvmilQGIGGL6G_vifyxbEaOev7Thqtm_PxyKWYKxPAyTHRrebAo00QbU7_Y6NESYhuG7PEDAXMxARG2m3ICxQakcF-BYZ-KjCWarmBUPOP-iKpgmmROqH4um1EtEHui0RfCdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇪🇸
باشگاه بارسلونا در تاریخ خودش سه تا از بهترین هافبک‌دفاعی‌های تاریخ رو در ترکیب داشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/104108" target="_blank">📅 01:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104107">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKEkAQCFaU4BQ1vqrarBKHtD13NtcWIZn04q23a2GGO0EgN85-SkGTLXDUV4g6tpNFeb-otvwqob9xzSMO03pi0dSVhLOENkyK8_Ycv_HOK6BN2ZYL6jtFLCokSpYCEQ7YZizo4hjnfRWPH3asuJIbYMKODlG8cYXJPXa4dIpsf_-_ubO8LiCE-D92er5K9gtYfegyRhSS1Rhf4ROgzQ-Um-aLtr-ng5slyLPubcWWuF5NwWIPWjmOUlbwjKh65-5Wzoi8hZn5dnpafe69zuOic3cXm0XMtkjZ4Dl_fFPcQzCwdS6AW8DuoUvjnLZnE5qvHwOwz3n6tearZRghopPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو: الهلال اولین پیشنهاد خودش برای جذب واتکینز رو به مبلغ ۴۵ میلیون یورو به استون‌ویلا فرستاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/104107" target="_blank">📅 01:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104102">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7I4yRjO5f_W3z5n_fgJmi3pIqpgPIkhKzuVx1SaiicFAJnHoY15EpQFmPk-vg-19MtxG16H9-syox1S6hMJF-Ccxk4FVC2cxb1WGD7VagQM2kMVFH1zurrMwmrF-XxDX3eaDO-KidRp_S1AbDz0TU_arkM6pzmZrOzWYYIwUd0-khuzSfZFP8oAw2zcg2L15miS9S0EfhMn1EjvQTWceOjnzblfPUAOk3BQEqd5bs58Sq1OTif7jHI_h_FYTIylHs_8eHTVBGBQGfdN9erIHwcwkZFMIIeV3laQuGj5B2Oc9qx_vvtB6qtwb0rKZnb4qB6nC3DWWmzO0KjqOVGFPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SLSTAL7WxYZ4WMRDxWfmFtButWNYruxyyqef1Rnp3mJDVyOmCKYG_xS3WK-O5wYoTTXuJg-crSpaTvQpYhFL9md1Z6odxr-XBaW6I-BI7AX8z0zY9E2c84wBsxg3CvqUZz80JJSzwunH0b7DxAYuJOBmvmcglgJtGVWKIW8hDfeJAEeFUNj5GAra2J1oizRtnYj9jY_hU2_qbmc3zGIaqstKH2oUKLG9DCmwHE5uR2NBd2uPVyGI60NGs-mQLOc32kosIg1XTrFYtsjLErkITKyQI3pnElXQZ0-f3iblM-1UJH0kHyMKCBoHa1EGuzHP9d4yEJrzWWdGAl4UMBmYSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDpt2VRbIzbDz6vL9WtyKSWa_uYKt9a-mHi_tYMSweeoX6DzHN4xvKPMpmlDQTRdvZfvHimCr7qe0yD-hoPnTVASft1wXmFe_DNf-ILiIEncaOPR69V56tt5o4Qo3vvbOMklzepghWzs57z4OSzERhOypVrvJyKXLa74eoz_GqV_kxQ8Dw_0UaAq99K1OEFKN_x6l6oWk2EDSUfjRuVfyEK6DGPz3dtzlqkdWXlKCrHMlTxUu81AJtq5NHCWhC7nnZchqkzHt4Ge2L5I3GC-R4FuI39rRgIKpX2GMzJoYWDWShxgI9-y6HzK81rbnGhC7CPvXnPxK0QZOux8pRbvCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روبرتو کارلوس نه تنها مسلمان شد بلکه برای بار هشتم ازدواج کرد؛ بازیکن سابق رئال مادرید پس از هفت ازدواج ناموفق، این بار با زن مسلمانی به نام "سهیلا طاهری" که اهل لبنان هم هستش ازدواج کرد.
این ازدواج طبق آداب اسلامی انجام شد و با خواندنِ شهادت مسلمان شد، عکس عروسی مربوط به ماه ژانویه 2026 است اما امروز لو رفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/104102" target="_blank">📅 00:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104099">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3OXQCmSy_2m_H6IE49b1W1UQziAQ8PpL_hswMTYSEo2BXnOLsVeX7m0bAiW3pvN2IxiuYWeRz8X0wBi4AidZ-TU-MPJyI-9etCUiAtWPu6CuPyqha-jT2Ggf87L4ocQ2Y2qXOC__-iNDIwNJN7VvFobqhWAtLpvQhW4KY46274SCG0X0gMk1-T8vN_dYeePusdbjTE7KLqJNiuK3ZG6D3EViZAXY_7IlelM9mpPX5XEkKCDA1rriFypPSjbWyy3aqQPhqRLBS7lpW_Tc1avvO50LYRy0WtZy_n-7tZnBmweeJpDsMc0-qGD0Ll7SQmdOCiU5k0tXHTN2dgzOFvixg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
رومانو: توافق نهایی بین منچسترسیتی و لیل برای ایوب‌بوعدی بسیار نزدیکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/104099" target="_blank">📅 00:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104098">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loZQWpBQCRfa45VnyKyDxGTg930wyNwGdpL1wOKlnyyt0yETRkRBud8IPk05lz61RuTT2k8rXA029oigDxz9nmXY_QzMjGds6q4tJjC0wonAquDkBBM4OxsMDbZ-JaojXJcLcCmywZoy6RZz7Yx7jYKWcp0mvH04M2rhWGGjVzjLa4ugpE26DMeweEAMiD8kpkn3frNGiNs5DZ3jJF3bI_3yjTUa1l7F9OZ3uPWT528U8T7GBgRakkoQEMvVU4G5uVRo3TFkT_WhL0QsUCgk6oApyfgIc8mDbOzNX1o1dqQ4Peb1JrVLM_9OTYY9xGPZzc53NRXVf4EFHYeAuuAXmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو: الهلال اولین پیشنهاد خودش برای جذب واتکینز رو به مبلغ ۴۵ میلیون یورو به استون‌ویلا فرستاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/104098" target="_blank">📅 00:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104097">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/160d28a24f.mp4?token=N4uS4dkOga0RAZXrQLAgEYi7olZz_HqEzN7J9kFHUI3NmaQ_uINYMX8OTkDzzYVQzXEq6g89deb2P0wzCo5sbEFEWR72RooHgQv0ZsNCwVbE-NOT9lZUwhXKVvZNwt2SvABsrLzA5667PvC0wkRWM_9AqCLT1DmJxMxrs18t8Ry2MgiNdSdEYVA002mu_2Knq5Vm8eVQHFObRj1VdAle2C4vE7jE25Ziafx55aLlZeilUFNLYsETv9d4g5gGoSw-wBlQW90jx2dkg5oxqgNvIW8Okj4oAAJg2WYpKBaT70NLhDi1i97UV05Zv4VIFSXearD1KOCjIsLMTr450dxf1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/160d28a24f.mp4?token=N4uS4dkOga0RAZXrQLAgEYi7olZz_HqEzN7J9kFHUI3NmaQ_uINYMX8OTkDzzYVQzXEq6g89deb2P0wzCo5sbEFEWR72RooHgQv0ZsNCwVbE-NOT9lZUwhXKVvZNwt2SvABsrLzA5667PvC0wkRWM_9AqCLT1DmJxMxrs18t8Ry2MgiNdSdEYVA002mu_2Knq5Vm8eVQHFObRj1VdAle2C4vE7jE25Ziafx55aLlZeilUFNLYsETv9d4g5gGoSw-wBlQW90jx2dkg5oxqgNvIW8Okj4oAAJg2WYpKBaT70NLhDi1i97UV05Zv4VIFSXearD1KOCjIsLMTr450dxf1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
شجاع خلیل‌زاده و بازم حرکت جنجالی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/104097" target="_blank">📅 23:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104096">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
‼️
🇮🇷
حسینی، دروازه‌بان سپاهان: توپ‌ها جدید است و تازه دیروز رسیده
بازی کاملا یکطرفه بود/ از کادر فنی و هواداران سپاهان عذرخواهی می‌کنم/ اشتباه من، تعیین‌کننده بود و امیدوارم جبران کنم/ توپ تغییر مسیر داد و باعث شد من اشتباه کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/104096" target="_blank">📅 23:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104095">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/123f073b10.mp4?token=mzuMmyhT8uIwLdGIy2gelZ8sY2XGeNab3AjzJTeegnrghMUyF_GYv7hKmXALDVnHHWYJqgKOQZ8bVUjnM5XIqXGfXSm0nTwE4yeDiiDcAQK3NRcxyc0phyZXM_Acpi7XT0CXUrsL6zTeR_PvHfCmehXDzAW8m7qNGN9fLVNRDX9TiHVsyDWpbCvLzWAgFCAGZ1fNrjdpDRlryXPpPu4j5Pyd5VSkYEi0ndo8kYGRrutPUq3_ag_YUKvG2MC7no5T9mCOHrKrUBvhGYzk0EcmToVJDYICyzbeIo9AEUrtUFzzNGKTMjBr7N1M9PSPPiayaxKvrg-wilEux2I1o0sXS1rFN7eLXtQB5V0hpM8mSkGfsIWJLX0KgHPMN2YnLHMz0v2-ufUHHnCWI-voVt7vSgblKt4lOFnCzaS8EjqLizcrRhZawgjU-ZIZwbno93v1J8Y2-AH7Bb7haL-bf8XtVrX1SIwww7-DT1mtpvXL1RVDy-PlXpMMu97PVrMqrXHl7uxdmLAGl2mq3Cq9LaZ5F_-q2VM6FUGvPsjMc1AyJVmA1ENl9oO0SJKpE0uxckMDmrGlZO5vi4RG1Q28Sqi6_YCyg44wwVaa-lsFk_E33y6Qy-gmOXX3RH43wKWokOvlWmYGrSpYK2VoSbRaRT2LI_DuNtpPLak23hwPsk-pPHU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/123f073b10.mp4?token=mzuMmyhT8uIwLdGIy2gelZ8sY2XGeNab3AjzJTeegnrghMUyF_GYv7hKmXALDVnHHWYJqgKOQZ8bVUjnM5XIqXGfXSm0nTwE4yeDiiDcAQK3NRcxyc0phyZXM_Acpi7XT0CXUrsL6zTeR_PvHfCmehXDzAW8m7qNGN9fLVNRDX9TiHVsyDWpbCvLzWAgFCAGZ1fNrjdpDRlryXPpPu4j5Pyd5VSkYEi0ndo8kYGRrutPUq3_ag_YUKvG2MC7no5T9mCOHrKrUBvhGYzk0EcmToVJDYICyzbeIo9AEUrtUFzzNGKTMjBr7N1M9PSPPiayaxKvrg-wilEux2I1o0sXS1rFN7eLXtQB5V0hpM8mSkGfsIWJLX0KgHPMN2YnLHMz0v2-ufUHHnCWI-voVt7vSgblKt4lOFnCzaS8EjqLizcrRhZawgjU-ZIZwbno93v1J8Y2-AH7Bb7haL-bf8XtVrX1SIwww7-DT1mtpvXL1RVDy-PlXpMMu97PVrMqrXHl7uxdmLAGl2mq3Cq9LaZ5F_-q2VM6FUGvPsjMc1AyJVmA1ENl9oO0SJKpE0uxckMDmrGlZO5vi4RG1Q28Sqi6_YCyg44wwVaa-lsFk_E33y6Qy-gmOXX3RH43wKWokOvlWmYGrSpYK2VoSbRaRT2LI_DuNtpPLak23hwPsk-pPHU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🇮🇷
🇮🇷
پیش‌بینی کاملا درست نتیجه بازی سپاهان - تراکتور و حتی گلزنان این بازی توسط هوادار تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/104095" target="_blank">📅 22:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104094">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9b2a3476b.mp4?token=rGKv-ud_pniSuWE-0wLH6W_w1HdbEJBtnHeumjZrnI-Uc1tPFGnncS0Rjy_KmBf2gF8RdctPbd6dPSLmJ48QWSO8yfJC2nCzT9xcJniTA_APEv0CKjkFsN8ytzU1gWJB30XnEyVluHnmpwBCFlERquBDoGACRzNJ-UVrDA6eXA1iQokam9tSveJ6zkTcPf7d9aEJvVw6vH6oAWx0Gdpiic0f57QenfHKjUp54pXyOUgyO2E2lbJi2_quG5kjAxl3WU6a__0zxtnijlon5bSnhen4CkR4nvhdr2bz7i9_9oZd5fuADG9CqXk-2CX0ij47LY5-zVlgJXCNIhLBmFfqNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9b2a3476b.mp4?token=rGKv-ud_pniSuWE-0wLH6W_w1HdbEJBtnHeumjZrnI-Uc1tPFGnncS0Rjy_KmBf2gF8RdctPbd6dPSLmJ48QWSO8yfJC2nCzT9xcJniTA_APEv0CKjkFsN8ytzU1gWJB30XnEyVluHnmpwBCFlERquBDoGACRzNJ-UVrDA6eXA1iQokam9tSveJ6zkTcPf7d9aEJvVw6vH6oAWx0Gdpiic0f57QenfHKjUp54pXyOUgyO2E2lbJi2_quG5kjAxl3WU6a__0zxtnijlon5bSnhen4CkR4nvhdr2bz7i9_9oZd5fuADG9CqXk-2CX0ij47LY5-zVlgJXCNIhLBmFfqNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جشن ۲نفره جواد و بیرو مقابل اشتباه حسینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/104094" target="_blank">📅 22:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104093">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nG0rKEmkCGXBWp5C0m1ICfhw0ktl2lDQUuPhE5_nAvW220r-CDNlvj8D_4nnKqZWocvbINAhJQSu2GXiHqc1rdWNWpHA-wowpAd34RywcKgVAYIfEPNvrsu7jB3QMgY7bt00dtrRyrCNI1t67CJWvXln9knSoQVxg0BnRHz6OMsm7B3EkfebPNo4_DODv6yKNaownoGXcrlTPmN4g8q1CUR_WBxZVVzxivapPUPnu-zS-7ekL-BLcx5i5CEL7u3FzpUEiMtL9Id0opLR6oqINuQFiTApB6xL6MVT681gGKd-NE69J8GogxpiqE_NBnDu3n4ZUgffvlJ--XXopgqm0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
👀
🙂
روبرتو کارلوس پس از ازدواج با یک زن مراکشی رسما اعلام کرد که مسلمون شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/104093" target="_blank">📅 22:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104092">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ldun07sCYuUfc4sSuo5V35xbkjS_voLc-jbEJtwTyA4xRqTYpftAuMmOJ-LLJeaLJ_yofY0VY-QESi4s1xSc9itVspom1JFSFRs6cnrf4rD2bfzUKoL0Ivz3IRJdXle06RUrmZNKIRco5RbvTCI9UyFV7c6LNziubj9lZGaQAZXZoJXG6hoKt1Vo4xwiLAO6IqFUCyUV2lyCukZBiG4meinpBc_VBY_B99VJ77oVikwpIKqWxp1COMhQ9UMixesL7Q0KF9WW656tM1hmwwEsDr6wS4NJvqDwgFMzsAnL_D_7GmpMO21ZIbkdUfdBZFqItFBeL_M6CqUsQd-JKMCZyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
پایان‌بازی‌هفته‌دوم لیگ‌برتر؛ نبرد جذاب هفته به سود نکونام؛ حسینی نفس سپاهان را گرفت و تیمش را بازنده کرد!
🇮🇷
سپاهان
😏
-
😀
تراکتور
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/104092" target="_blank">📅 22:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104091">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNSGVvAoYZkRiLePazWGi0xmn1_LIpyzhSQI7-bpVmFwgrF9Vl9hXLyTfnZw49R8cpmLGyW3G2zmB-Oa6kusqBF4lcfv344i5XkaxSzvEXKFGWLGcvKObQxvtLc-uzvkyZBA78PrSY9ivdjBdKKyjcA69HnaLyX2C0dvOBjjZ9EwuNJilEKyiIbtIJa-fTkE5hlbfin7WrhOmfxR4iPVVwGmVbYlqufyf-Clpy-EWVNiVxPK_BC8WGXYrElZbDSMthd44VBPjdwX2aP2vVuwW0Bc0JWPc3Hn-zfnWQhtQGV0PfbdsHlJAuDHDfPPeMmzvscZfCWIhk1fLx8VpVAIVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
پایان‌بازی‌هفته‌دوم لیگ‌برتر؛ نبرد جذاب هفته به سود نکونام؛ حسینی نفس سپاهان را گرفت و تیمش را بازنده کرد!
🇮🇷
سپاهان
😏
-
😀
تراکتور
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/104091" target="_blank">📅 22:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104090">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50e5746901.mp4?token=FNwwlWkjXtOboyGVHGxN0zTWW3wHFTAI1YBeGgCn9tR57qqh1f_l6vV7-Do4WlZjs5fa3j0goqZi5MuqQAoOEPno2MNw-MHT_Re334rQM4BMn8Bt-PDzu3CXIDpLPV495KA6xMyrJuQWDu_Twh0qtnSs6jszHli4tGjWAldGRGWGSk6NjNfpaYXsrl8wZ4MZQLkTXNn5ZUNIWP9Ihx4Hl2lhr4WRatFNdDdxwjdQ-B4we13LImld4oYZjpEt9W7unqVRUkyEf2Cn9ZOpAanMXEJ5inyk2Stm3J1CAL95yaKQ_9pK5qD-lrdh5ZZndGwQPMFknaz0up0_iBS_jtiQFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50e5746901.mp4?token=FNwwlWkjXtOboyGVHGxN0zTWW3wHFTAI1YBeGgCn9tR57qqh1f_l6vV7-Do4WlZjs5fa3j0goqZi5MuqQAoOEPno2MNw-MHT_Re334rQM4BMn8Bt-PDzu3CXIDpLPV495KA6xMyrJuQWDu_Twh0qtnSs6jszHli4tGjWAldGRGWGSk6NjNfpaYXsrl8wZ4MZQLkTXNn5ZUNIWP9Ihx4Hl2lhr4WRatFNdDdxwjdQ-B4we13LImld4oYZjpEt9W7unqVRUkyEf2Cn9ZOpAanMXEJ5inyk2Stm3J1CAL95yaKQ_9pK5qD-lrdh5ZZndGwQPMFknaz0up0_iBS_jtiQFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
دبل اميرحسين حسین‌زاده مقابل سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/104090" target="_blank">📅 21:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104089">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گللگلگلگلگلگلگل دوم هم تراکتور زدددددد</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/104089" target="_blank">📅 21:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104088">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34e506a7f6.mp4?token=SCZMVPXmWMsCEjMl_qnOysEXBD6ZCX_jwtn4pE8g4O7xrXRYQxHmJx-izwSPjgD-AOV3CjXeeFReSB3jJ8xJiF_3fLlyPauqsi57vCU-z4Oc4ledYKZ_DXRrn7k2-igKGiz93XdJrNcnTPGFE5YrjdzoSYNvUfGxYaokMbD8cro_gbx9Uhj1PJoMkEheaVv_EqO9zw05tSthYfnFeQ3cE6ruzmUikVblqQm_MCLdlpBLeZU9RW2RB1cA_8lsTT7d0VIl8vJftmB7JvGXDgk0tf1gWkt8Gqcc2Gq3SWQVjTWZAuc1_Wqc9fYeVDT-GUbdRIAkBrV8slvYa23peExing" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34e506a7f6.mp4?token=SCZMVPXmWMsCEjMl_qnOysEXBD6ZCX_jwtn4pE8g4O7xrXRYQxHmJx-izwSPjgD-AOV3CjXeeFReSB3jJ8xJiF_3fLlyPauqsi57vCU-z4Oc4ledYKZ_DXRrn7k2-igKGiz93XdJrNcnTPGFE5YrjdzoSYNvUfGxYaokMbD8cro_gbx9Uhj1PJoMkEheaVv_EqO9zw05tSthYfnFeQ3cE6ruzmUikVblqQm_MCLdlpBLeZU9RW2RB1cA_8lsTT7d0VIl8vJftmB7JvGXDgk0tf1gWkt8Gqcc2Gq3SWQVjTWZAuc1_Wqc9fYeVDT-GUbdRIAkBrV8slvYa23peExing" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
حسین‌حسینی رسما و شرعا ریدددددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/104088" target="_blank">📅 21:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104087">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d2cc7d25d.mp4?token=c49X7HpOJ_rP-pa194UDeSJ0SPs6hoY3J0JVne23Oky-nBM-stkyiDQDYN28PFOs3Zegsf39h6qyKvuu_CXoqYK5RE8dkdubZ43uIlJP2PkZTHCRAip7hb8wVxA7U4OlcFIYejq3KJbIdchduSIC_GetZIgrE1cp80DsqdszZqfC4oA6IeTUCKtEzt_49SCIcAS_WadqlKmN0L45mdE2Wr1LUXfaBO0maa2txZyXGaOVC5wek0pYyi0k-g9UYiiDzumSMiJfe9Hf5qrp2-mCEQPd0DlT7J-2SjYkBZjjbhenVsgq79IAnldW1IPEwe5zhpbcqxsVZiW0V8gMCse7cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d2cc7d25d.mp4?token=c49X7HpOJ_rP-pa194UDeSJ0SPs6hoY3J0JVne23Oky-nBM-stkyiDQDYN28PFOs3Zegsf39h6qyKvuu_CXoqYK5RE8dkdubZ43uIlJP2PkZTHCRAip7hb8wVxA7U4OlcFIYejq3KJbIdchduSIC_GetZIgrE1cp80DsqdszZqfC4oA6IeTUCKtEzt_49SCIcAS_WadqlKmN0L45mdE2Wr1LUXfaBO0maa2txZyXGaOVC5wek0pYyi0k-g9UYiiDzumSMiJfe9Hf5qrp2-mCEQPd0DlT7J-2SjYkBZjjbhenVsgq79IAnldW1IPEwe5zhpbcqxsVZiW0V8gMCse7cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
گل‌اول تراکتور به سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/104087" target="_blank">📅 21:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104086">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تراکتور یه گل به سپاهان زد روی ریدمان حسینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/104086" target="_blank">📅 21:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104085">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBmcjQDqdCufG79Qqn-Su12wLM8rcwiSIXpuOJJ7rh5uUUPH3ideev9C20hFmqX8Gp6n8NaAgXqDLg9XRbKKGNO59jY4L_kYd-Rb1jRRx7JkCDxDlRRlW1a5Qnq6fqoKG7N5UP5E9SKmL0DG1Itb1b7bsKLYIlW22DXz5SI1mbaPMXwEZoQQqc0UAAbstZK-g5IsXe9tGTtlG5AAI6tdLAzdjP5F956pnt-peQqudKVvPaorK9dcdV5tGDdgh1QxMhUwU1UxpBWJDJyYJyO6SRJbpf-ysv4De41tpuZLxebCwwICxIJUJnY_ggRIGIDI5Bjb9P5vpiea08A1YYfdnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇩🇪
گرمازدگی جمال موسیالا در بازی اخیر بایرن که با خوش‌شانسی خطر رفع شد  درحالی‌که دمای هوا آلمان حین بازی ۳۰ درجه بوده! واکنش مردم جنوب با دمای ۶۰ درجه:
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/104085" target="_blank">📅 21:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104084">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
به دلیل عدم‌حضور بختیاری زاده در کنفرانس پیش از مسابقه، خبرنگاران مازندرانی کنفرانس مربی استقلال را تحریم کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/104084" target="_blank">📅 21:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104083">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818201b984.mp4?token=Ubu3pckXWg2AIuTuaLiQD83YY-qbKqVkw5LGxE1pGblIAjDRAx8jCfSKr1oMGKdYppzRXDcLyIEXvv88shJAQ95I1sXWm_L4WYB1hUHAFumB2xhRrafOhfpa0YnKk5buJGyInyF-eXioesRHWBuW5NqebtpJAMabaJay1CP0dh7EfnYD0o31fqZSxWQ38zYRi0Spsmg7GYM1m_vuIZ1uBvdzBUULBlqnJVwkbYGDFRuMcmAFSvUQXrO-fuS1YEiNPY5dgcamX31TxSllEhVTCMotf6K_jnElxqTadf5fuYPLnYFJHAD3ArkRaOuJ4sE9z5dloDMNqHlFvP8U8cdHXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818201b984.mp4?token=Ubu3pckXWg2AIuTuaLiQD83YY-qbKqVkw5LGxE1pGblIAjDRAx8jCfSKr1oMGKdYppzRXDcLyIEXvv88shJAQ95I1sXWm_L4WYB1hUHAFumB2xhRrafOhfpa0YnKk5buJGyInyF-eXioesRHWBuW5NqebtpJAMabaJay1CP0dh7EfnYD0o31fqZSxWQ38zYRi0Spsmg7GYM1m_vuIZ1uBvdzBUULBlqnJVwkbYGDFRuMcmAFSvUQXrO-fuS1YEiNPY5dgcamX31TxSllEhVTCMotf6K_jnElxqTadf5fuYPLnYFJHAD3ArkRaOuJ4sE9z5dloDMNqHlFvP8U8cdHXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
🚨
🚨
🚨
گریه‌های محمدرضا آزادی پس از گلزنی امشب در بازی مقابل نساجی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/104083" target="_blank">📅 21:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104082">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slMFw1to23eWWLH04uPSR3cyZiuKt5K9C7tQhEdNiUGZWDziI2iVhkhKjfvUi203o5h0n95NI_JdCWVf3F5lL070J5BGioLYz4ro4WsA5mZ-rLUacdMK2FW4rYGcmIj5VAinRAsFb78CpPR_6X6uq4rO1F_KpAEcMZMKXjqD_lzMExGiT65CZrxgeLDu2qjstG1kRsanUBNi8SSk55rXtKUfQdeKU8Hn1qfPm53SuNDru1J8jPKLAnC3_s8UHGwlcHqnmWckXqNOzAZL0ApbdzIwQboZhOPhHQgiypcyESV89QCSLxGibVrfuf8pG07r8RC3hDqZiaSeGSdXgSUPeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
پایان‌بازی هفته دوم لیگ‌برتر؛ استقلال به سختی برنده شد؛ فرشته نجات سهراب، محمدرضا آزادی بود! آبی‌ها با برد شیرین به استقبال سپاهان می‌روند
🇮🇷
استقلال
😃
-
😏
نساجی
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/104082" target="_blank">📅 21:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104081">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66e078a045.mp4?token=oOHHSPyQSqI4PExpYpInXcKP_AUjNAEX8IR_8ZjYCGahp66XwJkXTS6Xn4hJZIf1sbtFVboUxhnSwqALrFoyLFvlf6ix_AdqbtdemuyokSyAv-CadIxdEAi5zr4WUbip05NYVwZAilphSFQm8VYUKW1JjMIiT9Yygfq2b8MFClB9eZuL0qeTox-VGb_W_uzr9cTIHVnG4bqBWCRdEnKBQMx-2yy11Zmmk0ANQ7JXPalnpFow7w1EoOTvDpBf4FUR9uJh2cMMlNtt7JlQNhfk5cL1Z-PscybKZtdOgpZZwmYUrX-OoFaHhoG43BvGY1J3zvyIpR9XiaMjpSYwWMQl-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66e078a045.mp4?token=oOHHSPyQSqI4PExpYpInXcKP_AUjNAEX8IR_8ZjYCGahp66XwJkXTS6Xn4hJZIf1sbtFVboUxhnSwqALrFoyLFvlf6ix_AdqbtdemuyokSyAv-CadIxdEAi5zr4WUbip05NYVwZAilphSFQm8VYUKW1JjMIiT9Yygfq2b8MFClB9eZuL0qeTox-VGb_W_uzr9cTIHVnG4bqBWCRdEnKBQMx-2yy11Zmmk0ANQ7JXPalnpFow7w1EoOTvDpBf4FUR9uJh2cMMlNtt7JlQNhfk5cL1Z-PscybKZtdOgpZZwmYUrX-OoFaHhoG43BvGY1J3zvyIpR9XiaMjpSYwWMQl-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
گل اول استقلال به نساجی توسط محمدرضا آزادی
82
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/104081" target="_blank">📅 21:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104080">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">محمدرضا آزادی برا استفلال گل زد
😆
😆
😆
😆
😆
😆</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/104080" target="_blank">📅 20:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104079">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔻
#فوووووری
از دیوید اورنشتین: باشگاه نیوکاسل درحال مذاکره با سیتیزن‌ها برای جذب نیکو گونزالز است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/104079" target="_blank">📅 20:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104078">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJWcxcH2wB1cg-kMN3F-8evw84hxAz32trxFBtH7I86xxrdOgcJj45659F-4CuwMXuwuwETitQpIP_3aifvLWEKzHLcMmaCB064_wvwm_fyH6RURmLyZ-luzNdqBMruM6oqC5bnprDVECa0qM1DOPk_GAjkW8hWx_Satpr5_yPrjn-tHbEFDQ-MhLS4o1_6lkfoJuX-uhhrfNlbGVTeHsPfnSspI0IWnY2d7HX8UKtePCdTc4B-bIaddEgc9roJDQFouyhfArRcPek3wkvYqAEG5ZjrSq4Xbz-E9vxFFJp1z-iavQ0MK0ZW5etsr9dTwtOUVdkYBs6irCpmffBDd2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
رودری:
"گزینه‌های دیگری هم داشتم با حقوق بسیار بیشتر، اما بارسلونا انتخاب اول من بود، و این را به وضوح بیان کردم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/104078" target="_blank">📅 20:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104077">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWIcKocdOQihQOCY58JW7_1-_MqoaKMmptrkTe46U07Eu2V3GKBUvyzj_GcKEPpJkiClu1Z65aFiqycix_IBm8oOvqB63vqEBrLWKWVgksoMZNIfXZDI-KbIiZoTkq_UYSjMYwK5HHFlfQD4KQCisthaFpKMbmUKntsTwyLQWFumTiNfG7GLlkOMNLnqOCh1mHJ4zdsnitIwb33dOYPQQJJZj30JGfn7npYFifF4ZNvXJs1pMs1ecamAD0B6TNEdRKx9xDHfH9_YDgaQp3ilFntQ8c9MCrd4yUEK5LdRAGzonf5QuXIrPCRChQgApSZeK8bYFOqOkLBYsZ-0TetShA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
رودری در کنار مدیران بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/104077" target="_blank">📅 20:21 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

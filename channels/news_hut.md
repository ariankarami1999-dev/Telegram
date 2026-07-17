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
<img src="https://cdn4.telesco.pe/file/IyB3zwg63yVXxj-TvHvl4uTXH648JNkwsWEjyWXL4h4iHNuhSh0qhnvbHwmcjly3aLcKHNp5dSm7s35HJ0W2HUnMz0Rn0l3oftAfWieCAPcZ_4az6EDHp5fJVTjEpAJiTZjR7lazRbuoHe9FvfQez7NbH8SzhhkLPYT6pWUKeHGZif7ZY141EQtjTkcB9F6JQFidq0AF7_ig5CPsExUp1i921XuthlOylNMlaNTTiTx2bbD_66qA0e8ZqzM_cKwa5M0HMHGpi8VDMNaijFLR4XN0uXOsaf3fPqnt9L6JND-mafSBJPZoFWKWReBQxXf_kYwpOcbaaTJ7ZRZs6_nxLA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 167K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 09:43:41</div>
<hr>

<div class="tg-post" id="msg-68329">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47f00f211.mp4?token=IhPoOaYUXpRgSRN8spWbhoWVHb0lLtcQixHeLGZwEld_9fFPa34dqc1f-2IJ4YowEBW_cOmFYPW2AZFRqAAmSnoKJ6Hphx4FXldKA3OEvRjeBznfWlsUf69wRf_6PjZSiKJqB2VznAoUAj1v9b6_NHab_JKPkwcWBRdLvuG7HNZVxcrJffjzdGFLzX_C1rW-1dM1gR6FPBOMImoBzvcL63Qt3nFF0onvDf7_mUpqDfHYEwceKwLqwbGT1u8bP8N-GVgQ5DIBBN0VcCf105tyRNslWzauayZIRGyPuFjpT1RdxuwUZv9zstuCFCtEe-PNhdyL_ZI7vLy6jlACcdji2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47f00f211.mp4?token=IhPoOaYUXpRgSRN8spWbhoWVHb0lLtcQixHeLGZwEld_9fFPa34dqc1f-2IJ4YowEBW_cOmFYPW2AZFRqAAmSnoKJ6Hphx4FXldKA3OEvRjeBznfWlsUf69wRf_6PjZSiKJqB2VznAoUAj1v9b6_NHab_JKPkwcWBRdLvuG7HNZVxcrJffjzdGFLzX_C1rW-1dM1gR6FPBOMImoBzvcL63Qt3nFF0onvDf7_mUpqDfHYEwceKwLqwbGT1u8bP8N-GVgQ5DIBBN0VcCf105tyRNslWzauayZIRGyPuFjpT1RdxuwUZv9zstuCFCtEe-PNhdyL_ZI7vLy6jlACcdji2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تصاویر ماهواره‌ای نشان می‌دهند که آثار سوختگی در محل حضور یک سامانه پدافندی پاتریوت آمریکایی در فرودگاه اربیل عراق وجود داشته و احتمالا این سامانه  بالاخره توسط پهپادهای شاهد منهدم شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/news_hut/68329" target="_blank">📅 09:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68328">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/68328" target="_blank">📅 03:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68327">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SPm_UAYh2Gd1MRgikMhNpExMzyyghabpA8rKv8rKVj2M6BIAdiPeyb4AaPMwVhjBNVVFeiFmqEUMyHK3virBFfmNMFlknWGzmSu6Ufn7mRnX6HAV-m8d2kYUQuImEX0PDaWUs4HjEA3uFNuBei5Hq0eiDRBfBApxidBUpSHvKXpTB1-zLm-9k8APPb0pIpZMrIlZvdGE85bIGFmdG58bpa9kC025WrvIvJLuUqG70t2WdvlrGZCsZsEbw6W0jUWMapaBka3xQFyZsy7Da-dmJwP_jvKLxtCraVulb3WF7X8z4BgPYC7UjAv5bjA7D0EOgW1C5ZJG6i3qqaA_6zpiOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/68327" target="_blank">📅 03:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68326">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
از سایت موشکی جم چندین موشک شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/68326" target="_blank">📅 03:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68325">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bee400515.mp4?token=I-3_bA4tZw3LmCHDitAtBatEZrZxYYdMEsmMHfcobmWxuyFnuEu3nFZXRiZp6Pqs14uFZTT7rEcdJ5gYhvHYh9levga85I-B-dBVa4wPOMDOMTOlby1SmarY77DrkqsarOOPDvMT4eIsK9iELVsYM_Lo8hBuR9X9nwflmt8pBz0fjqLjNtIr6g6J2UBP9lv3w5ATXOjHX7EBVlBUxheu3jlnFmKYn748P-HW2fYU7CpC8ltYt0EXYgvKMsX-41ijEVP2j1cvfelHnqYNAFrvM_NEfreCKTPKuWA2Pc3geNTni3MtySI3_mLys3n3UQWw_tpeBIGPgMTcyZ0Wd-y-rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bee400515.mp4?token=I-3_bA4tZw3LmCHDitAtBatEZrZxYYdMEsmMHfcobmWxuyFnuEu3nFZXRiZp6Pqs14uFZTT7rEcdJ5gYhvHYh9levga85I-B-dBVa4wPOMDOMTOlby1SmarY77DrkqsarOOPDvMT4eIsK9iELVsYM_Lo8hBuR9X9nwflmt8pBz0fjqLjNtIr6g6J2UBP9lv3w5ATXOjHX7EBVlBUxheu3jlnFmKYn748P-HW2fYU7CpC8ltYt0EXYgvKMsX-41ijEVP2j1cvfelHnqYNAFrvM_NEfreCKTPKuWA2Pc3geNTni3MtySI3_mLys3n3UQWw_tpeBIGPgMTcyZ0Wd-y-rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/68325" target="_blank">📅 03:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68324">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه پاسداران به بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/68324" target="_blank">📅 03:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68323">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">روز‌ها و هفته‌ی آینده بشدت مهمه، مردم خیلی بیشتر از جنگ ۴۰ روزه ترسیدن، و مسئولین علاوه بر ترس، بشدت سردرگمن، امکان یه قمبل‌قهرمانانه‌ی دیگه وجود داره #hjAly‌</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/68323" target="_blank">📅 02:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68322">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.  #hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/68322" target="_blank">📅 02:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68321">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g53QVvz594KOjZjlDBgVrF5SvZDZpPCG-7XKGcwFq-UF14Y8UZG-Ly6sXguZF_QWGxha8_E4UonkIeyYpkmH26WnNAIcuVfH2E-uGGwTLgqgNl89510MF2bay9tavUbRgUNvV75s05HYuCmJ0OkVwxZipzoyRZ-69ZVfuKhLqcqj-DTc63TE-WhVCJUfvklxWngppK0DLMyh2noHezxhNmjD_RjThaVjrLBB8TvbbGnH3GQs7kcWuUKcr8oP8Xj-KeHFLpuFM673VQLhBJy1Ffbh2EgkfuZXY7Ak5BpaFw2mxJ1gfBhDrzHNkJxex2d9XMFne78JDxAZkdo0N6QhuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68321" target="_blank">📅 02:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68320">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=Rp1DA2SUkQUihrkFHDbVqwmO_rtP0PbEuKKKRZYVs0HJIWWrCkNxIyN8Z_fdYoPHZb_OD4zL7Kk75xT8BQc12UqrUiH4Ny7lIBB5c7TQpQmLcu_qnI_Yul9BRIkBpvibhR7rU8r_F-qr2Q4eTKrcipXVa4Pfnj8jwcu4NUGJyPjzkrz9ByxhiDZlqyo4mQksgYVOjOGo45MQkvVr18874ncXpfI2D9qrVGv8n2PeiH86Ys3KIpVsoV4IntVwPSZcKwjwUthu8UrT3jzIJdRR71zGJm5gdxeMt0yPszJmVBTwTq0LD1eKkDV0ZVc3doYZSSGqlQK2cPP5H6xQ6fKU3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=Rp1DA2SUkQUihrkFHDbVqwmO_rtP0PbEuKKKRZYVs0HJIWWrCkNxIyN8Z_fdYoPHZb_OD4zL7Kk75xT8BQc12UqrUiH4Ny7lIBB5c7TQpQmLcu_qnI_Yul9BRIkBpvibhR7rU8r_F-qr2Q4eTKrcipXVa4Pfnj8jwcu4NUGJyPjzkrz9ByxhiDZlqyo4mQksgYVOjOGo45MQkvVr18874ncXpfI2D9qrVGv8n2PeiH86Ys3KIpVsoV4IntVwPSZcKwjwUthu8UrT3jzIJdRR71zGJm5gdxeMt0yPszJmVBTwTq0LD1eKkDV0ZVc3doYZSSGqlQK2cPP5H6xQ6fKU3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68320" target="_blank">📅 02:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68319">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a3e60cce.mp4?token=XW4OYRDWEIcvDgby5FG0PCYp22hGunylWu6C6JmcfnRZxboMG9jcLT4J23qluMbBi3rf9Cpw8eVzENMzMdbiUOpqgabXeJKKoLeKdTG_kBimy_HnxI9D46G4xxLZZbqRXmct5mkxZV_laz4g1OrfUxdXYWedna397Mi-zJwBb5UudaTldDb7A0C4VqV-1OTLRmt-apW8MfUCdpWQ3AKIMiKt4ezdB49iftIPyzXerxFDrjbXLR7ConQV432rUb9E0GgfW1Vv-km-bXpZvvZ_9wt2x3hatPMe4z8eQnkGE353CbUKxPDI4lUKfUIEr7ch-6Cvhw5UeSnwOlowDFpSmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a3e60cce.mp4?token=XW4OYRDWEIcvDgby5FG0PCYp22hGunylWu6C6JmcfnRZxboMG9jcLT4J23qluMbBi3rf9Cpw8eVzENMzMdbiUOpqgabXeJKKoLeKdTG_kBimy_HnxI9D46G4xxLZZbqRXmct5mkxZV_laz4g1OrfUxdXYWedna397Mi-zJwBb5UudaTldDb7A0C4VqV-1OTLRmt-apW8MfUCdpWQ3AKIMiKt4ezdB49iftIPyzXerxFDrjbXLR7ConQV432rUb9E0GgfW1Vv-km-bXpZvvZ_9wt2x3hatPMe4z8eQnkGE353CbUKxPDI4lUKfUIEr7ch-6Cvhw5UeSnwOlowDFpSmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
حملات موشکی و پهبادی سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68319" target="_blank">📅 01:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68318">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
در حملۀ دقایقی پیش به بوشهر چند فروند موشک آمریکایی به پایگاه هوایی و پایگاه دریایی بوشهر اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68318" target="_blank">📅 01:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68317">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
فارس:
دقایقی پیش دشمن آمریکایی یک نقطه از بخش ویسیان شهرستان چگنی در استان لرستان را مورد حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68317" target="_blank">📅 01:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68316">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed596f3009.mp4?token=IwVrbsOYV7AidQTZ_ovWmsou52Hfj0D2eAcW6f73M-kS6O0hKv879wV_Jcm8zQ9sj-qrs5nkNYb3ZAmYfLzrM0gjVQ39te5YS4Rkcz8D6iHLEsuCZ1CN1f402RtoCqxM4Ny3ShCEYfE7XoK9WgbXGyi2MAqjaKZAl4-85psx66-Ypo2MGCnnreqiGZm801KKWr9WvRV8MEH3OhOoxuawOhpp2glFvSTcbpR0cytt5yzEZHuRYY6Jojn4vU8FZ1MDFDvMBh0XWohSFUFIvJBRqPNqsMEXZHi5DNYWlkfqbzVcwWpNSTTdMYSDV25uZbhJa3Bw9Bw6Ov6Gdg0mpWCCjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed596f3009.mp4?token=IwVrbsOYV7AidQTZ_ovWmsou52Hfj0D2eAcW6f73M-kS6O0hKv879wV_Jcm8zQ9sj-qrs5nkNYb3ZAmYfLzrM0gjVQ39te5YS4Rkcz8D6iHLEsuCZ1CN1f402RtoCqxM4Ny3ShCEYfE7XoK9WgbXGyi2MAqjaKZAl4-85psx66-Ypo2MGCnnreqiGZm801KKWr9WvRV8MEH3OhOoxuawOhpp2glFvSTcbpR0cytt5yzEZHuRYY6Jojn4vU8FZ1MDFDvMBh0XWohSFUFIvJBRqPNqsMEXZHi5DNYWlkfqbzVcwWpNSTTdMYSDV25uZbhJa3Bw9Bw6Ov6Gdg0mpWCCjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68316" target="_blank">📅 01:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68315">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68315" target="_blank">📅 01:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68314">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68314" target="_blank">📅 01:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68313">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5f29b590.mp4?token=OePmuX4dWSXmS7BT8CaxiMy7QK5ILANFuk3ZhDu0VKFtH349m859jothFu7G7aRJrJ9m_VOJmraqhduMnhoFCPxdWIhtC0D_buFw5Da5_1WhfRObw_EfqGKVZWkBZUpk2XrgI3BwaHva49ElSjpjSon2c32YAJPeBbTl7Sa8BcdGCjgJS6G-gkkCYyntSaJ3Kx2Rykqr-7SXAFAz3Pk8g9oQnwitZHH0tTzsZep4vNZbvrSu2H0hY_jjQzP8Rafm_w1jp0-gs08aBg2ruYO7Rqlir2BcuutAz7jT58VP3miYfXUOHmV6ykY0y3siZJvdEGnAXe6w9lmYD7qs3QNGjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5f29b590.mp4?token=OePmuX4dWSXmS7BT8CaxiMy7QK5ILANFuk3ZhDu0VKFtH349m859jothFu7G7aRJrJ9m_VOJmraqhduMnhoFCPxdWIhtC0D_buFw5Da5_1WhfRObw_EfqGKVZWkBZUpk2XrgI3BwaHva49ElSjpjSon2c32YAJPeBbTl7Sa8BcdGCjgJS6G-gkkCYyntSaJ3Kx2Rykqr-7SXAFAz3Pk8g9oQnwitZHH0tTzsZep4vNZbvrSu2H0hY_jjQzP8Rafm_w1jp0-gs08aBg2ruYO7Rqlir2BcuutAz7jT58VP3miYfXUOHmV6ykY0y3siZJvdEGnAXe6w9lmYD7qs3QNGjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو وایرال شده از حمله وحشتناک آمریکا به بوشهر
شیشه های ماشین فیلمبردار درجا ترکید!
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68313" target="_blank">📅 01:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68312">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d811948267.mp4?token=psNCTgVd6LmQ2mVrbbsyEe8dKcKutWQrSJlz3S15hEZsotlJrBJoyb8DINqELnImz1GK-r4a77dz-oRseAxBliKwJbNs9BpCzx7SoNAwwFFr02GFd_n_L94a-gK0TxSmOJfc-N7abpOW4td_qp4iZY1D4GFbmVjEb_e4UpB82MkVRVdEKe7qxmLJhvxTeAyXxaYUZ3Se59_MKmgnY9xTMQcUIi58VGdhMHN7I8KYp4nSVINp39THDgAS7JNV2HzKOqW5NAuZmb9jfjrF6_x5xJJ6GGWemAhxFbRe0SiOLT7BxD6QM9TtqyZAoWPqTrBzr2RkxelRsLC8uPCgo-qGznq1IPOsVjEKtM_DZa7xP9J_EeFESAdVVi4dmKWO70LiucszqzqVR73GOaN7fKnHZh2kSdA7IaeYFl3Cb9E7OygrhNxonCZ31M3aKpnzAbCImNipL0V4U5pGb4OsFl5nd4sWVPHxO0szdTfcO-3MMJBYGgh1mcCIgqSGCITCa4emfZ8mqsQlw3wx8o_Dhw76KXVkH6qFox8OJYgFxkbvXUZCcPDZmJNi0mXzKulsQzQsH-lEy6pvAHEpy53XzH61fUEIvPilCjbCnfIfKEM477TCoh_ewCf8BPkV0LT4A8sxI0wkYJSWH3JfZ11FdRX0EJJ0hTTaoYlRq6ozmfZRrJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d811948267.mp4?token=psNCTgVd6LmQ2mVrbbsyEe8dKcKutWQrSJlz3S15hEZsotlJrBJoyb8DINqELnImz1GK-r4a77dz-oRseAxBliKwJbNs9BpCzx7SoNAwwFFr02GFd_n_L94a-gK0TxSmOJfc-N7abpOW4td_qp4iZY1D4GFbmVjEb_e4UpB82MkVRVdEKe7qxmLJhvxTeAyXxaYUZ3Se59_MKmgnY9xTMQcUIi58VGdhMHN7I8KYp4nSVINp39THDgAS7JNV2HzKOqW5NAuZmb9jfjrF6_x5xJJ6GGWemAhxFbRe0SiOLT7BxD6QM9TtqyZAoWPqTrBzr2RkxelRsLC8uPCgo-qGznq1IPOsVjEKtM_DZa7xP9J_EeFESAdVVi4dmKWO70LiucszqzqVR73GOaN7fKnHZh2kSdA7IaeYFl3Cb9E7OygrhNxonCZ31M3aKpnzAbCImNipL0V4U5pGb4OsFl5nd4sWVPHxO0szdTfcO-3MMJBYGgh1mcCIgqSGCITCa4emfZ8mqsQlw3wx8o_Dhw76KXVkH6qFox8OJYgFxkbvXUZCcPDZmJNi0mXzKulsQzQsH-lEy6pvAHEpy53XzH61fUEIvPilCjbCnfIfKEM477TCoh_ewCf8BPkV0LT4A8sxI0wkYJSWH3JfZ11FdRX0EJJ0hTTaoYlRq6ozmfZRrJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده آمریکا، دقایقی پیش تصاویری از عملیاتی که دیروز بر روی یک نفتکش ایرانی انجام شد، منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68312" target="_blank">📅 01:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68311">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دیشب که داشتم با دوستای جنوبیم حرف می‌زدم، می‌گفتن حملات بیشتر داره به سمت پادگان و و قرارگاه های نیروی زمینی کشیده می‌شه، حتی دیشب مثل اینکه به پایگاه لشکر ۹۲ زرهی هم حملاتی شده...
امشب هم که خودمون با چشم دیدیم ته حمله به پل‌ها آغاز شده...
حالا سوال همه الان اینه که آیا قراره بهمون حمله زمینی شه؟!
اولاً اینکه ما در جایگاه تحلیلگر نیستیم که به این سوال، جواب دقیقی بدیم، ولی شواهد اولیه داره اینو تایید می‌کنه، اما وقتی کمی عمیق به مسئله نگاه می‌کنیم خیلی موضوع فرا تر از چند تا کلمه‌ست و عملا داریم از یه لشکر حداقل ۱۵۰ هزار نفری حرف می‌زنیم، حمله زمینی به خاک ایران، برای آمریکا بشدت پرریسک و پر از تلفات انسانی خواهد بود، ولی اینکه دارند شرایط رو برای تصرف جزایری مثل خارک فراهم می‌کنند
اون هم به قصد فشار بر جمهوری اسلامی،
یک موضوع دیگه و موضوعی محتمله.
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68311" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68310">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/861fef7828.mp4?token=JGeVRq8SXeDEHI3DbqDseJi0f2ISUy-66rKO4ipPnoaUbBsJgojIInUXfzlqxjoRRd_VSz7l1L-vtUNdXqcBLO84DG5Wj2DGFMgr7LJjRtDjQRbBsMsHzr605k1sF0bEfqCwKoTW_telJbNNpWhqHM5SaSQAQQdYN9eTTzbyUZyzLJXtT1UdqFj5ptMAQBGOUb1F54HomyMR0nIpfkOz8OZF1bA2G41WesnupgOgf-pHuJdlO5eyuYiMqqrEsnEm1JyIzdnZSvavFK86vdwkCW0-4wLwcaSxtMsmUxjesDmRciOAVntrciSk6xZupq25G9WHbn0xYKCsjSiwJ9U-gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/861fef7828.mp4?token=JGeVRq8SXeDEHI3DbqDseJi0f2ISUy-66rKO4ipPnoaUbBsJgojIInUXfzlqxjoRRd_VSz7l1L-vtUNdXqcBLO84DG5Wj2DGFMgr7LJjRtDjQRbBsMsHzr605k1sF0bEfqCwKoTW_telJbNNpWhqHM5SaSQAQQdYN9eTTzbyUZyzLJXtT1UdqFj5ptMAQBGOUb1F54HomyMR0nIpfkOz8OZF1bA2G41WesnupgOgf-pHuJdlO5eyuYiMqqrEsnEm1JyIzdnZSvavFK86vdwkCW0-4wLwcaSxtMsmUxjesDmRciOAVntrciSk6xZupq25G9WHbn0xYKCsjSiwJ9U-gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
تفنگداران دریایی ایالات متحده از «یگان یازدهم اعزامی تفنگداران دریایی» در تاریخ ۱۶ ژوئیه، عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «وِن یائو» (Wen Yao) در دریای عمان اجرا کردند.
تا به امروز، نیروهای آمریکایی مسیر سه کشتی تجاری را که قصد عبور از سد محاصره را داشتند تغییر داده، یک کشتی را که از دستورات پیروی نکرده بود از کار انداخته و برای اطمینان از رعایت کامل محاصره دریایی جاری ایالات متحده علیه ایران، وارد یک کشتی دیگر شده‌اند.
تنگه هرمز و آب‌های پیرامونی آن همچنان آزاد و باز هستند؛ مگر برای کشتی‌هایی که قصد نقض محاصره آهنین آمریکا را دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68310" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68309">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
چندین انفجار سنگین در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68309" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68308">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gR8K_mSzHaHcZCOcphnjNDPoOcsiRdMk97wglXx1Uo9n8c1_aJrM8oiSOSBMD02NY3Y2E3iD1Bp_6uGkhlIrPGFEBVbK6IoLmyh43ejkx2AmfbbFhF6McWDOcqd-k08LAS9WyGyLrDDVcgOJx9kwWCJCn89NavPbj3BBxIf3OXY_Trd_pP3dTyMTIiDCQHPYg_MpCyjmRLT4xtgth1Zsxo1bPNvwlvJYfZSNVPlunoiiIW7WybblMDVjyyu2yLtpTek8n74PkML80D89YmjJZBB7adNCA9xHMdeIriJwD7EjlHpoLzfVft4bAKirlcFdsLAfOHyolvlj1zQYxXfyEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تمامی پل هایی که بندر خمیر را به بندرعباس متصل می کرد توسط ارتش آمریکا مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68308" target="_blank">📅 00:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68307">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
دفتر فرماندار هرمزگان اعلام کرد که تا اطلاع بعدی، جاده‌های زیر مسدود خواهند بود:
جاده بندرعباس - خمير - لار به طور کامل مسدود است.
جاده کشار - کاهورستان نیز مسدود است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68307" target="_blank">📅 00:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68306">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6vcJ7g2RIZVUL1Q4Zht1HwImYHTNuZ0Md37-Zf4cb79FwVhV89qbTUqgqMiuP4OLuNgp4pW3MHBnjEsJMjfI9BjlIJ3k48h-rfS-c1kly0qujIJN-1o4XEckiLBaUXsOub5JFNb3cT0muaZ-uV8LB7xkwkAt_Xpigd2uuBBLO2nag2Vc7EVcI4FFcgEE0aWdD3yombZVBQR0USk7qsduR8E6Y40sX975nahEEy-uCnuOMizMPEQHq3OyuIcpQmZtbeEKislmvSuFRaqHJdiO0l2MVEexeHtcUPCuOcUDJrj3g-CNXRRLLMRaYEyfJgPS9sbnOeR6ys4PJDm7wVvHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رشیدی کوچی :
⏺
«حمله زمینی به ایران از سمت جنوب رو قطعی میدونم و به نظرم تنها دلیل تأخیرش، گرمای شدید هواست.
به نظرم تمرکز حملات آمریکا روی مناطق جنوبی هم در همین راستاست و ایران هم تا الان با هدف قرار دادن عقبه دشمن در کویت و بحرین، اجازه ایجاد مراکز پشتیبانی رو نداده.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68306" target="_blank">📅 00:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68305">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPK4eZYmGok05cgBzhTORQ-3wb3m-WAVV3lwY4Gkm6vl4Urh_8UQ7Tyrp9thdKxBSZWJT1Zl8qQz4L3desyQvUsGUZS5IiXZP6FeqswL2STc1ZOgMp9t7zh_czBLVkBenTrpHCMoIH5s3WPX4bcznvkfY_XFXRAX1NhfcB8jOws2Fkh2X1e86DiCBu-9wlzjGhtEZkGQXLRKybUgrvgrkiLtPES3UB1shw2isTFecsJVoNtp2Y8GMJlVHaERm6kWckgzFHH6F9_KTTKFTAPIv8GmWt7987lOdphqbhgA1R4MSJKxe4dfrx_MozRQbKm74samDCVU8zc02icmKa2irg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وضعیت پل کهورستان، محور اتصال بندرعباس به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68305" target="_blank">📅 00:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68304">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0BxBL-OgiON7-UHvbfjcVx45dzphl-nSEjcq4JBjSGutjDMMRxqKWleoZYRYqsNSDf_-AZUEoMbPD6k_88UUr-wXMwyPsu188mwAsBzIE3TVrLGc1rHGqt3kbCOqxY17xYNfkl2tDRfRUf-QOzoqpNM0DZzWrfCiXBg2P_uWi7iqn0sybGul8u49oyrHjNuQWpCGNVWfoJfDFKbq9EY1pbUhhKFhGOoZqd18PeeE5q06r2OXEo-sw3Ias2rpxEoSQ2IueT619zOwOhJYn5VXeYUXYyeelaMqCk2di-yL7CnN-BrB3_yDX4oqki3GTpHYIuk010yhgni6mF63pmMNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
راه‌آهن بندرعباس مورد اصابت قرار گرفت   @News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68304" target="_blank">📅 00:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68303">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
راه‌آهن بندرعباس مورد اصابت قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68303" target="_blank">📅 00:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68302">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f357e145.mp4?token=fJZ44tloNEcBh1TwOnWfqRsU83elKTndUTqR3BqCxCl1gCO2lLXCAja-agrHRLiymumqxPkbNBUHTd7s-ZuyOoOKNhnQMLiopV_gR7eH4d9s5HdFOfEwZUI6uJ1B0iBZ18TZl7-R4-g8JZasxEP6rX0FnFUu-xBNZFHUGWJnw02dWa-DK5wkxhRe6NT9pu6ybEHxZoCtxcdSx3HmwUMlPhUd87cDfdXK_NvzDvfyKo7H7GOCpvra620j6ugkaxFsqCqDtm5uOzH2sqX-9sT3hqrT0k1kchmesCxcj4esTAHUNNfJ0TIIXKninC6KKnp5nHNovKGOuRfCkMaE1oE9pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f357e145.mp4?token=fJZ44tloNEcBh1TwOnWfqRsU83elKTndUTqR3BqCxCl1gCO2lLXCAja-agrHRLiymumqxPkbNBUHTd7s-ZuyOoOKNhnQMLiopV_gR7eH4d9s5HdFOfEwZUI6uJ1B0iBZ18TZl7-R4-g8JZasxEP6rX0FnFUu-xBNZFHUGWJnw02dWa-DK5wkxhRe6NT9pu6ybEHxZoCtxcdSx3HmwUMlPhUd87cDfdXK_NvzDvfyKo7H7GOCpvra620j6ugkaxFsqCqDtm5uOzH2sqX-9sT3hqrT0k1kchmesCxcj4esTAHUNNfJ0TIIXKninC6KKnp5nHNovKGOuRfCkMaE1oE9pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو دیگر از پل کهورستان
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68302" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68301">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
تسنیم:
آمریکا شروع به زدن زیرساخت ها و پل ها کرده.
اونا به شهرستان بندرخمیر و بخش کهورستان حمله کردن و پل ارتباطی بندرعباس به شیراز که معروف به پل بندرعباس - کهورستان - لار هست رو هدف قرار دادن.برق مناطقی از کهورستان هم قطع شده
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68301" target="_blank">📅 23:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68300">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=DzUfq1q5T5pWd6Ld8ob87_6RwXNsGm0jj-VFguU8pUzjBqVvtfCgjeCkwiA3NnnExouhiVjNwYL9xexKzc4piNqSe-3P1bJklkxarJG5cc_-2XANd9TKPwCiE4dHuSQZZikqA9qldwMPJgJA0MepP1K-JyrrUEb6iXLGoBbUshwYj0AN_TPgVGZpRZTwz6mAsvHgA3-eK4S--9iTGQZC7Zk0UQPhNU7bO7b9S-nzVWF4kGJnsxdljPg7E-BSsRkRaugZX6VleRkcP6LTaTOEwpmFmhRiqCFWtzOserVucaiGCv-A35N3xgm0UD489RqZvWCn_nlNqynDiML5JOzytA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=DzUfq1q5T5pWd6Ld8ob87_6RwXNsGm0jj-VFguU8pUzjBqVvtfCgjeCkwiA3NnnExouhiVjNwYL9xexKzc4piNqSe-3P1bJklkxarJG5cc_-2XANd9TKPwCiE4dHuSQZZikqA9qldwMPJgJA0MepP1K-JyrrUEb6iXLGoBbUshwYj0AN_TPgVGZpRZTwz6mAsvHgA3-eK4S--9iTGQZC7Zk0UQPhNU7bO7b9S-nzVWF4kGJnsxdljPg7E-BSsRkRaugZX6VleRkcP6LTaTOEwpmFmhRiqCFWtzOserVucaiGCv-A35N3xgm0UD489RqZvWCn_nlNqynDiML5JOzytA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
در کهورستان بندرعباس یک پل هدف گرفته شده.
موشک خورد به وسط پل، تانکر سوخت نابود شد، راننده مرد، یک تیکه از پل نیست، کسی این طرفی نیاد...
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68300" target="_blank">📅 23:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68299">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
پل ارتباطی بندرعباس به شیراز و معروف به پل بندرعباس - کهورستان - لار مورد اصابت قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68299" target="_blank">📅 23:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68298">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a71beb824.mp4?token=p5veEIsCHG0zNKjylD0VfUgsCu3BdlSFtIh8lCDh8XfLhSvm0yaVJ30MwO9_TYLT5_p1AzpIRj-afys7w_2umo7wEqk2NPcaTh64qlMw5jcaGZ4wQe6y3gcx2DjyuS_A6lWVtoVpb7GZn06FoPSbwKbeID8853jzsIE5ynR3BTHigjQ1iBfduVECYFKcWv_0ZT7A1Hb8SMfjw5gCDaoZNyOUBLdMWgixTtEbs3XP9f9aSDsKZNyGWiLLrMx6wClm6bGl0aTgRqErEiCfJbrtQCWwzc2egxC7AAJKpUZXa8lpDMCeFYiInxNZ0Ifw7dzsdmyn2PZI6ZtSJxy-3mhXYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a71beb824.mp4?token=p5veEIsCHG0zNKjylD0VfUgsCu3BdlSFtIh8lCDh8XfLhSvm0yaVJ30MwO9_TYLT5_p1AzpIRj-afys7w_2umo7wEqk2NPcaTh64qlMw5jcaGZ4wQe6y3gcx2DjyuS_A6lWVtoVpb7GZn06FoPSbwKbeID8853jzsIE5ynR3BTHigjQ1iBfduVECYFKcWv_0ZT7A1Hb8SMfjw5gCDaoZNyOUBLdMWgixTtEbs3XP9f9aSDsKZNyGWiLLrMx6wClm6bGl0aTgRqErEiCfJbrtQCWwzc2egxC7AAJKpUZXa8lpDMCeFYiInxNZ0Ifw7dzsdmyn2PZI6ZtSJxy-3mhXYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملهٔ آمریکا به یک پل در بندرعباس.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68298" target="_blank">📅 23:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68297">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
طبق گزارشات اولیه، یک پل در بندرعباس هدف قرار گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68297" target="_blank">📅 23:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68296">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
به گزارش ممبرا ساختمان مخابرات بندرعباس هدف حمله قرار گرفته
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68296" target="_blank">📅 23:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68295">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
حمله به ایرانشهر سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68295" target="_blank">📅 23:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68294">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bzi3s8Lj-85q_zS5fgUdDfiFW8R50TZDmtAAtxN-SvhZJJnGw_mDZPTKRfG3IDXLSONOdH7IW4NMisHWmxT0oL8gqmDK1qkWC6aC8N5m60Fna4fK1fOSAbb5yK9k3cbK7ucaqe6an9JpKYYxgbGbpjGeufVyj2qGRk47INAgD5r2gYNq7f7Y9n35C7LM9wRco6uAEwDps7VwNiZCDHYj5OyjZh02YMAMSwb93ieALQixABNqjqeS_0tIaqgS0AKgzdWxy-qFnsFscCm0D_iLSHbgvAiORRPek2TYMVEEBJqj5M2NgSdn-WKGjIrHyUSCRG6cTp3uSkarlQyqbnXOag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68294" target="_blank">📅 23:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68293">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JM8Gb-zkOhL8IQfP8H5-Kc1sK9cue1-tCIHB7fBY5T_dxYM3gAJ3EP1tRNknEjwTtuOrIXXwUvlh_Cfo3i0k9AjUsxhqrjw6x5c34wJA20dEipLk_hBZIRtgkOCsi3CDvDIZTqD8BgDf__GMHgLnjnhQZhtCe7MBgwwTqYSfu_2gyHi1HPO-QngwlfZnK8kRLeVg1RxBDW7gdQrj-1gOqpkze673kn7qVPT-fm5jewMdNAJ09y8ZWmLJsfLO9FTf6htxWD1SaMMBe4kcJ9gtIH-HIcPUhhoHe4I5XBfuuAuV_hQrAEmy2wxU3S1rBUcrk0bbN41hfLoLa1bFHg61IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وزارت دفاع کویت:امروز جمهوری اسلامی چندین تاسیسات حیاتیمون رو هدف قرار داد.
از سپیده دم امروز، نیروهای مسلح 32 پهپاد متخاصم را در حریم هوایی کویت شناسایی کرده‌اند؛
این پهپادها رهگیری و با آنها مقابله شده است
این تجاوز شنیع ایران چندین تأسیسات حیاتی در کشور را هدف قرار داد.
علاوه بر این، رهگیری اهداف متخاصم منجر به سقوط آوار در مناطق مسکونی مختلف شد که خسارات مادی به بار آورد، اما خوشبختانه تلفات انسانی نداشت.
نیروهای مسلح بر تعهد مداوم خود به انجام وظایف و تکالیف خود با کارایی و شایستگی، حفظ آمادگی و آمادگی مداوم برای تقویت امنیت ملی و حفظ ایمنی شهروندان و ساکنان تأکید می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68293" target="_blank">📅 23:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68292">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
پنج انفجار مهیب در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68292" target="_blank">📅 23:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68291">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به قشم و بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68291" target="_blank">📅 23:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68290">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS-</strong></div>
<div class="tg-text">داداش ما الان تو کوچه ایم تو اهواز بچه کوچیکا ذوق صدا بمب رو دارن</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68290" target="_blank">📅 22:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68289">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
اهواز رو دارن شدید میزنن همچنان  @News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68289" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68288">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=eLGO42v9pobprWoIXd2YTapzKDptvDJu0TCq0xRjmiLUZxzr_7mUfrsOtTkuiP8oVbk49aZndUk_o6vInSJ8zInfYHiyG4XdfZxH60twziRfPYUOOwLLyWbP1RBdI-fwG-tqfPJnwNVzEnM93H8jQZruyO9GsdjEN83yP4NmFc39RFUZPu4XMihqJT4j8CwAWLBU4FTz5I7mpKutVEXFzlCFABhlb5N4HIGN_Ku8ZkUDXNDL9KTgEYc4bB1CLkg7Axed3Uzg9g9AiR_VEQqcJt6AIjghrM3PXVZHXqDBK9d1q-O3Lmc8bdEPJ61hxl2Cu0NJf1jv7k74pvaNp9diJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=eLGO42v9pobprWoIXd2YTapzKDptvDJu0TCq0xRjmiLUZxzr_7mUfrsOtTkuiP8oVbk49aZndUk_o6vInSJ8zInfYHiyG4XdfZxH60twziRfPYUOOwLLyWbP1RBdI-fwG-tqfPJnwNVzEnM93H8jQZruyO9GsdjEN83yP4NmFc39RFUZPu4XMihqJT4j8CwAWLBU4FTz5I7mpKutVEXFzlCFABhlb5N4HIGN_Ku8ZkUDXNDL9KTgEYc4bB1CLkg7Axed3Uzg9g9AiR_VEQqcJt6AIjghrM3PXVZHXqDBK9d1q-O3Lmc8bdEPJ61hxl2Cu0NJf1jv7k74pvaNp9diJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک از کویت به خاک ایران
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68288" target="_blank">📅 22:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68287">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
اهواز رو دارن شدید میزنن همچنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68287" target="_blank">📅 22:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68286">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
دو انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68286" target="_blank">📅 22:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68285">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=E-8a5Za0N_BDXJJW4XpM-xtaMR9WTa5CeqTR2FG1mcjhDsT5VJkHgHsJZyETyMY1q3o1kbLf7vxfLNdX6VX14pjozYakMnDzbCycRvCra-6wnnWte0LMRqvAGhjqcZWjjWiElcOJKPCglCFdaeg2zOZvTVtXb19PqdbfA1iSN9Hp3fZvhYDnCBG4OpHHWk64mSpOibJYs-uOxqSrInd02JRdGfYmuiFd7-fUwGG1Kq5DWqrT6E0AEXQSWtNWZFpW2za3pH4DO25PZaJiVTZMG76QRhRzHxYKk64twAVU-W16yfw2_TTU47_CoF9YwbuJpuCMEJpXeM3eVQ7xqr0m2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=E-8a5Za0N_BDXJJW4XpM-xtaMR9WTa5CeqTR2FG1mcjhDsT5VJkHgHsJZyETyMY1q3o1kbLf7vxfLNdX6VX14pjozYakMnDzbCycRvCra-6wnnWte0LMRqvAGhjqcZWjjWiElcOJKPCglCFdaeg2zOZvTVtXb19PqdbfA1iSN9Hp3fZvhYDnCBG4OpHHWk64mSpOibJYs-uOxqSrInd02JRdGfYmuiFd7-fUwGG1Kq5DWqrT6E0AEXQSWtNWZFpW2za3pH4DO25PZaJiVTZMG76QRhRzHxYKk64twAVU-W16yfw2_TTU47_CoF9YwbuJpuCMEJpXeM3eVQ7xqr0m2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68285" target="_blank">📅 22:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68284">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68284" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68283">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npwQr0vSocSX1Lc3tHZzlBVLRstZeYkIJd1h0laziPpp3jTvJOW_vDSIFYxcNHayL4n29FAv654JL8M4AkMYHEWogsTQy0bEh8LPDiTMnvuZXSlA1mgneLjIEZ3wh8EwO5V75nr4jmVU-HPadXxrzdl25XBvWXXU2lVSY4XID5uWcdlWFZgZe_BnWbGliWwtYxwP0wtCoycay-uj2N-vewbmCqKG89X90zrSrZkYduBF9qXByVWXdUi7VDX623D8crIz0UDjKoAZWphnFcCeYFIrToz4rP5CQDOI-wBIz4JHM7TJ0rtY32IomQZ8AnVqehtDqmnuBm1nTnp6qJacZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگه آنلاین‌شاپ‌ داری این خبر مخصوص خودته!
اگر فروشگاهت تو تلگرام، اینستاگرام یا بقیه‌ی شبکه‌های اجتماعی فعاله، حالا می‌تونی بدون نیاز به سایت درگاه پرداخت اسنپ‌پی را فعال کنی.
✨
امکان خرید ۴ قسطه برای مشتریات
✅
فعال‌سازی در کمتر از یک هفته
✅
افزایش اعتماد مشتری به پرداخت
✅
بدون نگرانی از فیش‌های واریزی نامعتبر
🔥
همین حالا ثبت‌نام کن ‌و درگاه پرداخت اسنپ‌پی رو به فروشگاهت اضافه کن:
👇🏻
https://l.snpy.ir/i1ekm</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68283" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68282">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c56cad1a2.mp4?token=tNMRH0PzmNG7XypId6EH2vYHD92fynQrdEpTfR5Ss9Pi4YcSSLUipCQY4TRyT1spHeKMRJ2VuHREhJeXTNT34eqdco8adEIi7vcAopy7eAAOn5SZshmWgm-eNd1h0bENHmcxgrfoZBxdx7y0fabi1mk0fE_MF3Ay4FLeJAshDP8G17Lmimv8GsyO5K1pqdTtIBl-drdiwL47YkJhbFY_dp1c2Fo0njocRdKG84vvtF6_MnnG34yIu_IA61Zsnwa301vBlkTEDYbemAUgLvcXoqBy1A0WEPLa0Js9criqXiwFuZDrQVZo337mBumSK5TaUZDT-QTbsPeMPSn0xPpl8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c56cad1a2.mp4?token=tNMRH0PzmNG7XypId6EH2vYHD92fynQrdEpTfR5Ss9Pi4YcSSLUipCQY4TRyT1spHeKMRJ2VuHREhJeXTNT34eqdco8adEIi7vcAopy7eAAOn5SZshmWgm-eNd1h0bENHmcxgrfoZBxdx7y0fabi1mk0fE_MF3Ay4FLeJAshDP8G17Lmimv8GsyO5K1pqdTtIBl-drdiwL47YkJhbFY_dp1c2Fo0njocRdKG84vvtF6_MnnG34yIu_IA61Zsnwa301vBlkTEDYbemAUgLvcXoqBy1A0WEPLa0Js9criqXiwFuZDrQVZo337mBumSK5TaUZDT-QTbsPeMPSn0xPpl8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68282" target="_blank">📅 22:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68281">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTYecorRSosNXd5Tvop3m22fdoMsrDdPU2iJxcDbJvA4XbIeMkQDq7AEWB75IkLI3SX5RjeRLrHtjs01KA25QCRtFYtw1VhmaYHJU0UWJM8hb6-n_IqXAyS0c0ZE-h-9HNDEEPU5i5PN8y_2IHSbY50yzKHF1-9_3r5lKKzHrzF3UIQ5WIGaZ1AtSKWnSSMRVL_k4ZLxpReTRqk1s0udwywJfyxSQN9A3Nnwsu1Qahh3ocySVG4qYbGvFQWH61ceEPNcy0ZZe0cyvaB1g0I3bjcbQ6qRHGaiwiVEwysq9n9c8_E6qtZUscafCwiJKNKrpHt4JezCrFsnWY1Wmf1JuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۲ بعدازظهر به وقت شرقی، نیروهای آمریکایی برای پنجمین شب پیاپی موج جدیدی از حملات را علیه ایران آغاز کردند تا توانمندی‌های نظامی ایران را بیش از پیش تضعیف کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68281" target="_blank">📅 22:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68280">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🇺🇸
رسما دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68280" target="_blank">📅 22:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68279">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68279" target="_blank">📅 22:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68278">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
پنج انفجار در بندرعباس گزارش شده
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68278" target="_blank">📅 21:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68277">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
گزارش های اولیه از انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68277" target="_blank">📅 21:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68276">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4cdbbb0c4.mp4?token=uxhzjVUfBL64tWV8qjJpI9vmdbcWOHJKxVM44cOfMNLPA7GNV5_QL3uJN5AGLFYOrT1oJu9J3C1jNwTQ1pbNUuUBKjTnt0itquS0bWgkGKUdsNs219ShrcvXV5yX76-1BhIBWSUcB7WVsjs4n8zR4WSuUPgHj9xQJ_-SzrabsrAYa-WsaIQscYOgSI1rEPI66PHp2HqC4yS3-OZGGlqh3ZbRqxywL42yY2Cs-dV7LOF40hS91ieCnexBLdWatbJXVEBfy2cxbzVvpSl9gAl0hfdxtp78QgvT4jgPwS9APi2e6ba-zBK7Jkqrl9uc9KuaJjPOGDNlDu_vsURMFoOtWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4cdbbb0c4.mp4?token=uxhzjVUfBL64tWV8qjJpI9vmdbcWOHJKxVM44cOfMNLPA7GNV5_QL3uJN5AGLFYOrT1oJu9J3C1jNwTQ1pbNUuUBKjTnt0itquS0bWgkGKUdsNs219ShrcvXV5yX76-1BhIBWSUcB7WVsjs4n8zR4WSuUPgHj9xQJ_-SzrabsrAYa-WsaIQscYOgSI1rEPI66PHp2HqC4yS3-OZGGlqh3ZbRqxywL42yY2Cs-dV7LOF40hS91ieCnexBLdWatbJXVEBfy2cxbzVvpSl9gAl0hfdxtp78QgvT4jgPwS9APi2e6ba-zBK7Jkqrl9uc9KuaJjPOGDNlDu_vsURMFoOtWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کارولین لیویت سخنگوی سفید کاخ سفید:
«ایران همچنان به شدت با ایالات متحده آمریکا در حال گفتگو است و ابراز می‌کند که خواهان توافق با ماست، زیرا آنها از سوی نیروی نظامی ایالات متحده ضربات ویرانگری را متحمل می‌شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68276" target="_blank">📅 21:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68275">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8bf2cd6a1.mp4?token=eOVj37TVQMWCcEeGJYLAvI_fuZcH0Q41Du7Kx0eeVeGUI8JNfmN3zB94i-Hez0fu0wT9K9ROkJLqMjdpUbFCOKOxfTwTTE22WD988Q2Pn2xquguuHePpCIMCpapmgacrY1SpnRtQ9G5fvOA-5XhkjVrbUyZtinaUXxPtKiY83tR-2q4-eHLYvJqCHgGGvj44tpMmds-YYN75HUtpaXpOjulP53nzgJ2vIT3yNWEU_lSAUi71eKhL39-r2v-KhsbqLrHbqGxlClUsf-6l0sQqnlcEjMLl3vrHsbQDUIJezogF6eU89hIkm8wZ83UW2rY2KBt2OPduPZyooYjGPe9jnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8bf2cd6a1.mp4?token=eOVj37TVQMWCcEeGJYLAvI_fuZcH0Q41Du7Kx0eeVeGUI8JNfmN3zB94i-Hez0fu0wT9K9ROkJLqMjdpUbFCOKOxfTwTTE22WD988Q2Pn2xquguuHePpCIMCpapmgacrY1SpnRtQ9G5fvOA-5XhkjVrbUyZtinaUXxPtKiY83tR-2q4-eHLYvJqCHgGGvj44tpMmds-YYN75HUtpaXpOjulP53nzgJ2vIT3yNWEU_lSAUi71eKhL39-r2v-KhsbqLrHbqGxlClUsf-6l0sQqnlcEjMLl3vrHsbQDUIJezogF6eU89hIkm8wZ83UW2rY2KBt2OPduPZyooYjGPe9jnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز ظهر تو خیابون ولیعصر تهران،یه اتوبوس تندرو بی‌آر‌تی بدون راننده و مسافر به دلایل نامعلومی شروع به حرکت میکنه!
این اتوبوس میوفته تو مسیر سرپایینی و با ۶ موتور سیکلت و ۲ ماشین سواری برخورد میکنه که نهایتا ۶ نفر مصدوم میشن!
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68275" target="_blank">📅 21:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68274">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8F0fkB9MLFRL3vXMd7nMnvaSs96bpEEtutX90L3vKV4dXqco24rQX-CiPVyi7IKhAwFmAVgwyZitreMdxaRIw_mnfL7LeP7ab_Hw8QIXp74jH7QkBCpSVdIJsO_F6fDLJFmbmJ-kkPCvn94YVSmjOojkw2N4dJNb311IvHvuxh-cmBsnGjJE1HwYIKZI6hI-ZsNepbGNhFHYGniTR8b1GNZiP7JAwloOsKaep3TGjBByjuOq6Rh-yVVtWFVDhspgOYU6aEd4E4XckiML1g6Y_1BcpWIeysCbxsRQ-88NgFdHuEdHcBb90ufQlv6D-k6jXazO--CsvbnaKIPtr5RQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کپی ترید خودکار
— فارکس و کریپتو
⚡
اجرای آنی
— بدون تاخیر، بدون دردسر
💎
رفرال
— با دعوت دوستان درآمد جداگانه داری
💻
پشتیبانی ۲۴/۷
— همیشه در دسترس
🎞
آموزش شارژ حساب</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/68274" target="_blank">📅 21:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68273">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pxk2WDXljtfixxXR24bu491Nr4Xh2pc1i2BohCmiE-PR47-o4B0GpnzzCUQBo_Y7As_zpcg9SWlQWG_bC5ZhIkGz6SFXu8EJrdhknWKd1V5VulvqqmOyfQi5DC9UyHQjE1mbixxLPBD0v_p5AQ8QwB0qMdZeXjixs50XpgKG48HGlyvw-r2dujhB0ksS5LdGllJFb7UdfSKyQ9Wv2ZQWYef_wEZq78hv3pXIKvVcghFm1OHQC4boqdld9LREgKtibsYO3EhQoea5SC4H8I0vaEpfy_TRnS7rjKjBJkUU2GG--epQBSJRAPiQKYG9eRn0MIe29KtMUW0YSoyw492wMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏شاهزاده رضا پهلوی:
در حالی که جنگ‌افروزان جمهوری اسلامی در تهران و پناهگاه‌های امن خود پنهان شده‌اند، سربازان وظیفه و نیروهای جوان را در پادگان‌هایی بی‌دفاع رها کرده‌اند، بی‌آنکه حتی توان حفاظت از این نیروها را داشته باشند. این رژیم بار دیگر نشان داده است که میان جان فرزندان ایران و بقای خود، همواره بقای خود را انتخاب می‌کند.
جمهوری اسلامی این جنگ را بر ملت ایران تحمیل کرده است و مسئولیت جان همه قربانیان آن، از جمله‌ سربازان در پادگان بمپور، بر عهده همین حکومت است. آرزوی همه ما، صلح، امنیت و آرامش برای تمامی ایرانیان است، اما تا زمانی که این رژیم بر سر کار باشد، نه امنیتی پایدار ممکن است و نه صلحی واقعی.
این رژیم تبهکار بیش از آنکه دل‌نگران امنیت مردم ایران باشد، نگران حفظ حزب‌الله لبنان و دیگر نیروهای نیابتی خود در منطقه است. برای این رژیم، بقای بازوهای تروریستی‌اش از امنیت و جان مردم اهواز، زاهدان، بندرعباس، بوشهر، چابهار و سراسر ایران مهم‌تر است.
خطاب من به سربازان، افسران و همه نیروهای میهن‌دوست است. جان خود را برای بقای جمهوری اسلامی به خطر نیندازید. سوگند شما به ایران است، نه به رژیمی که در لحظه خطر، سرکردگانش می‌گریزند و شما را بی‌پناه رها می‌کنند.
من با خانواده‌های داغدار سربازان وظیفه که در حملات اخیر به مراکز نظامی جمهوری اسلامی جان باختند، عمیقأ هم‌دردی می‌‌کنم، و از خانواده‌های همه سربازان وظیفه می‌خواهم تا آنجا که در توان دارند، اجازه ندهند فرزندانشان در این شرایط خطرناک به خدمت سربازی اعزام شوند. هیچ پدر و مادری نباید فرزند خود را به پادگان‌هایی بفرستد که امروز به جای محل خدمت، به میدان مرگ تبدیل شده‌اند.
این جوانان، فرزندان این سرزمین هستند، نه سپر انسانی جمهوری اسلامی. آنها نباید بهای بقای حکومتی درمانده را با جان خود بپردازند.
هم‌چنین از مردم شریف ایرانشهر و زاهدان که برای اهدای خون و یاری رساندن به سربازان مجروح پادگان بمپور شتافتند، صمیمانه سپاسگزارم. این همبستگی ملی یادآور این حقیقت است که مردم ایران، حتی در سخت‌ترین روزها، فرزندان خود را تنها نمی‌گذارند.
ایران به فرزندانش زنده نیاز دارد، برای ساختن آینده‌ای آزاد، آباد و سربلند
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68273" target="_blank">📅 20:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68272">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
فارس:
حوالی ساعت های ۱۹ و ۱۹:۲۰ نقاطی در  بندر عباس مورد اصابت پرتابه‌های دشمن قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68272" target="_blank">📅 20:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68270">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7ad056e14.mp4?token=jS9mfH4D6aeHG64tMw_ZoMWRSyfLszNsdAKTfPi_ki_PVg3S6xRCWCh2UuY9cP2s1PCaLjq0SaNCcHcxNB9uOidFzmznxd_mTS7zX2LtZnE94Xdr95GIalZ3K_HJ3mQk95FW9Mu3rxmeoaXu8IZQtZN6IkJz33IwtsCMK1C_8eqBbKwE_XIopd-dyY0eL5_zoiXH3QSJD4mpKyUAD4g84VC9h5JBVWS8Ey31y_7nK6pbZS_GtrcttxhRPEUbZ4A1-7Yp9h5dDHLbneMUmV_qE48VONsYpqx1cj1HOi0yEMnkWfE0H-apBtS05jRE0Y6sHgSwaDW7kVn5G2Rh8NaMKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7ad056e14.mp4?token=jS9mfH4D6aeHG64tMw_ZoMWRSyfLszNsdAKTfPi_ki_PVg3S6xRCWCh2UuY9cP2s1PCaLjq0SaNCcHcxNB9uOidFzmznxd_mTS7zX2LtZnE94Xdr95GIalZ3K_HJ3mQk95FW9Mu3rxmeoaXu8IZQtZN6IkJz33IwtsCMK1C_8eqBbKwE_XIopd-dyY0eL5_zoiXH3QSJD4mpKyUAD4g84VC9h5JBVWS8Ey31y_7nK6pbZS_GtrcttxhRPEUbZ4A1-7Yp9h5dDHLbneMUmV_qE48VONsYpqx1cj1HOi0yEMnkWfE0H-apBtS05jRE0Y6sHgSwaDW7kVn5G2Rh8NaMKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در بهبهان استان خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68270" target="_blank">📅 19:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68269">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ebc1ab26.mp4?token=XGBPzDGvgAvMXbK5Bi4ZBrxh8dNGC3zh0j2YJL2Doq0TIf2494hIWlSTeapGK4tmg7yoQVt5tOQ5-uxfLkwztl6i_R_A3g07Lr4GrZjmkrFdJKBTDLEcGUxg6Kj3JDEs_5wi7Qo6yaOrwQElu5_so26BdIWU-w4nFnuEXHL4w7iQvAiX4MylCLdcthQcoO0afr2tObqN45JTSPJhofxCxwjigcHb70aV58fTlvcynd7HbsqiKWMsNrPXIOdxu-0MSUVwDVtjtyjt-a_sgMGij3tRWppuqNKHD0WGRyDdbQE5jol6Dsp0sifOOX2k5-zXZsuZTukbB4TkzDqNBsPA-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ebc1ab26.mp4?token=XGBPzDGvgAvMXbK5Bi4ZBrxh8dNGC3zh0j2YJL2Doq0TIf2494hIWlSTeapGK4tmg7yoQVt5tOQ5-uxfLkwztl6i_R_A3g07Lr4GrZjmkrFdJKBTDLEcGUxg6Kj3JDEs_5wi7Qo6yaOrwQElu5_so26BdIWU-w4nFnuEXHL4w7iQvAiX4MylCLdcthQcoO0afr2tObqN45JTSPJhofxCxwjigcHb70aV58fTlvcynd7HbsqiKWMsNrPXIOdxu-0MSUVwDVtjtyjt-a_sgMGij3tRWppuqNKHD0WGRyDdbQE5jol6Dsp0sifOOX2k5-zXZsuZTukbB4TkzDqNBsPA-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محسن رضایی: مسیری که در ذهن آقامجتبی هست، بهتر از مسیری بود که شورای عالی امنیت‌ ملی رفت.
مجری: چه مسیری بود؟
محسن رضایی: نمی‌دونم، نمیتونم ذهن خونی کنم
😆
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68269" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68268">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7Oxg1HrGi7-8UTjgBAkcHzAZr75gpcNGhkHfhwG7a-iS0BTQVRUOYKfxc7iBFosu2MK78eANdmO-BcBVTDgP0OyXZ6zB5CtDQgpJNiZa0JRb6OmOFjg9pueZDUXTd951MsyaIpjWQlmytpWfhPmcy8Ck1tCENA7hiF3daM9IP-ibdWh9-uBMwJmPtjKIwaafiOPXU1iovphm-qO21dOdPtVtM1PKdjOXiNhMXpSn76pFjs998QAValvH5ld8mpYrA0kAhY0r_sRGh8rMeT01NoY5NU7PaNO_KV9Wl3pvPBsxKkQ-8vJ-EGPflbqIX2JYr38uGwphn8VJh0k0IC0og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سازگار با تمام اپراتور‌ها
✅
لینک ساب اختصاصی
✅
مناسب برای گیم
💵
20 گیگ — 120 تومان
💵
30 گیگ — 150 تومان
💵
نامحدود — 200 تومان
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn
چنل رضایت مشتری‌ها
⬇️
@kavianivpn</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68268" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68267">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Prwi-zfgwY6nw7hKOFuWm97YqZ20uBuFvWJLbTsioCzirI3HIqGBtqEvWhY8ortcRvCg-QspNRGZ4q3Cpo09WX5vYpuOPPTK-GYD9nv2SoVWZ0T4TmJgKB_Rc_YMYkgqe-K8xzUYwukHNao_rNeD5r1zWeuNOfIAoGxj-JUqVvpe58scPo_ghaHjivbO1ljOK9KfYCsVQrI8YMZWTzvjYgulr3wHpqEe-7KGPJitZF9m46KKqWjsdwfVIMcALEar6DBS1L3xEdkNq0Q_8FPUTwcojXnd4qOWO0NXJhjj4HQ4yaHLJmJv6z_3Qk4pZuwCZjgneInhGCI52hxEqoGlkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی به آرایش ناوگان آمریکا در محاصره دریایی ایران؛ هر چهار ناو لینکلن، بوش، باکسر و تریپولی در منطقه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68267" target="_blank">📅 19:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68266">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06389032d8.mp4?token=tZCNlel5jKzQ2AdbtCW3WgGQAhDymIBVIAgF8iH2jahZfrNFZFTD0aW8sS1JaNO5wi3YGsKcixW_7Qx8PpG3Y-KzKOnMISDKePluiFCX7YsgXv1WWmVDAjyBDDCTMwHqZmsQI2lyZIiiOw0htG_wRSoW1FdHsf4sTawi7NMMx1vV54n6crSCOl0DUcawMvhHtASUisGcFaFBTPGLMYs-z6aH6gjaXMXheI2tRX7HikvXVQC1Ghm_3ftOIjylo1umtSAA4GvaUD8bWtpt5pNRndwgevoWFLFrng_eTb8sidgTsyhoeubNFo7G_3eXSgCc2mcgLOoN13pVPJNw_epcNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06389032d8.mp4?token=tZCNlel5jKzQ2AdbtCW3WgGQAhDymIBVIAgF8iH2jahZfrNFZFTD0aW8sS1JaNO5wi3YGsKcixW_7Qx8PpG3Y-KzKOnMISDKePluiFCX7YsgXv1WWmVDAjyBDDCTMwHqZmsQI2lyZIiiOw0htG_wRSoW1FdHsf4sTawi7NMMx1vV54n6crSCOl0DUcawMvhHtASUisGcFaFBTPGLMYs-z6aH6gjaXMXheI2tRX7HikvXVQC1Ghm_3ftOIjylo1umtSAA4GvaUD8bWtpt5pNRndwgevoWFLFrng_eTb8sidgTsyhoeubNFo7G_3eXSgCc2mcgLOoN13pVPJNw_epcNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جی‌دی ونس، درباره ایران:
اگر مردم ایران بخواهند قیام کنند و حکومتشان را تغییر دهند، این تصمیم با خودشان است.
اما ما قرار نیست ۱۵۰ هزار نیروی زمینی برای تغییر رژیم اعزام کنیم، مگر اینکه خودِ مردمِ حاضر در میدان بخواهند به چنین نتیجه‌ای برسند.
البته ما در هر صورت قصد اعزام نیرو نداریم، اما پیشنهادِ اعزام نیرو عملاً به این معناست که ارتش آمریکا باید این کار را برای مردم ایران انجام دهد.
ما دیگر دنبال چنین کارهایی نیستیم؛ واقعاً نیستیم
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68266" target="_blank">📅 18:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68265">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwK1O-t8oZaj6EIk3Pn6Kx_Z6TDtRKS_shEO4PeAkChk6vaKOLaz4xEq44D_tEWEhl_iA-YL_2iT5bIMZrmmjMEoqvpHECXFmOJgETnYGMb3eXtmle1-UbtdeC7hpgN5YhJKXYdLwtML9qP1ciW5UEmk0QFRCC-kEgAM7sUk4KFrGINqYj1aXS8CR6zkqxkAgrTDoxtpvazhY25kVyhK6JGfvJdBB2o0OpYQ7u8UqtA6s5H5y36zsS9IlVGVBbG8YvdeW9J5CumjQi1UtNDKeqgoCD0SAuGLNJPp3JO_nRHfUeA-aM2D0UYM-M-STtDTSdPC2jj_w1yCHFNK0VRh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
لاشه پهپاد انتحاری آمریکایی FLM-136 LUCAS در نزدیکی بندرعباس
پهپاد LUCAS در واقع همتای آمریکایی پهپاد ایرانی «شاهد-۱۳۶» و یک پهپاد تهاجمی یک‌طرفه (انتحاری) و کم‌هزینه است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68265" target="_blank">📅 17:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68263">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55dfc7018b.mp4?token=aul-at9UxWvtAChMG4PDoIRvErdT8Skf5cZ6CupUBv0RH3nZVCA-r9f-9p6UamyiEIF3juZGQN9nFztUJYxNRVneFWg7_hCpSef2SVlv8z1bL1_-hKL0pGK4FMC660SZlqFz_Ul78f3HYy20850DBPaCbFwy8A5BtXsDYuTJD1khRWLq3eAUMNWDJI-rcaz76NlliiAhR9IksYBEbMHsMAT_vzqKx1_fyUyIJpGPTnnzewNJVmEwyBT286fp5OrmFi4gzsw6ibC14RN0Ba9VMwHpDp9gT-1JnZkseKF8XyaL0XV95qzjNP74oQ1jKmtR0VKBqJB1Fb6OAAn4XC6T3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55dfc7018b.mp4?token=aul-at9UxWvtAChMG4PDoIRvErdT8Skf5cZ6CupUBv0RH3nZVCA-r9f-9p6UamyiEIF3juZGQN9nFztUJYxNRVneFWg7_hCpSef2SVlv8z1bL1_-hKL0pGK4FMC660SZlqFz_Ul78f3HYy20850DBPaCbFwy8A5BtXsDYuTJD1khRWLq3eAUMNWDJI-rcaz76NlliiAhR9IksYBEbMHsMAT_vzqKx1_fyUyIJpGPTnnzewNJVmEwyBT286fp5OrmFi4gzsw6ibC14RN0Ba9VMwHpDp9gT-1JnZkseKF8XyaL0XV95qzjNP74oQ1jKmtR0VKBqJB1Fb6OAAn4XC6T3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عموپورنگ هم اینطوری بصورت دردناک برای مادرش گریه کرد:
من دیگه مامان ندارم...
دیگه در باز کنم کی بگه چی اوردی برام؟
💔
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68263" target="_blank">📅 17:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68262">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c15a1c1db.mp4?token=W1GQTsJwSZvSVda77aaVmMfQuorQjER4wHCgXSeE34vPbtlXbU3sqLjjnXXcHLd7_VCH52OUoAedUSK0-qPdjFUo6A5ChRCZzgq1OmX8nN7rXB4MKtrpnJt6oKLcvVl_OONEZvsVEaBzdiSn-O-dQWZVb9cGPPsinYQJjEgqdEnM-9b6SYzp8PWVzoMnd-hWR4hSn-7AzEn_uRxIeG7EYRdbGFTtbPHdSe2YSLKFa8njBblpj9trxKEQcSE82U0g0ARty9YCZDQQrKOTMkFPhRZzP5YYjdwb9g3L3bCGHqj-D9bD_maIhT1lrhOZpojUcPjTaTQJKXxVtSxDq30oBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c15a1c1db.mp4?token=W1GQTsJwSZvSVda77aaVmMfQuorQjER4wHCgXSeE34vPbtlXbU3sqLjjnXXcHLd7_VCH52OUoAedUSK0-qPdjFUo6A5ChRCZzgq1OmX8nN7rXB4MKtrpnJt6oKLcvVl_OONEZvsVEaBzdiSn-O-dQWZVb9cGPPsinYQJjEgqdEnM-9b6SYzp8PWVzoMnd-hWR4hSn-7AzEn_uRxIeG7EYRdbGFTtbPHdSe2YSLKFa8njBblpj9trxKEQcSE82U0g0ARty9YCZDQQrKOTMkFPhRZzP5YYjdwb9g3L3bCGHqj-D9bD_maIhT1lrhOZpojUcPjTaTQJKXxVtSxDq30oBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنت‌کام:
هواپیماهای جنگنده F-35A متعلق به نیروی هوایی ایالات متحده در حال سوخت‌گیری توسط هواپیمای تانکر KC-135 هستند، در حالی که در حال انجام گشت‌های هوایی بر فراز خاورمیانه می‌باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68262" target="_blank">📅 16:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68261">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TelU1vXxBNiqvpOtYuEsZyqgPd1ZKIH7hPkCXgohdiLHlcmyVleZ2eu99vDZpdRY7TGBuIfvnwzKF-z2Rx8Vbn8ox7KT3ZFiKftk8c3foHokqnKfVV3ANbQ-a_815IDBHcuFqEyW0bau-mkef0jN-yoIXoMEvUAgBKh05Nwknm4zmR9_xEO3oaCxg8sFISiHi8tVdLmHtRW_cRtbYJCLJnVBXJsoVqNMIj3LB_uPymFRoEINkzC-HnhXMqyfJhPql_9LKBmOw1URS7fEL_VgefiPFAjuCv8w3XGJJfDmQfYfRH_E1uDZyAH_HbsfN5mTKp0Jru_Z0YJIbU_-HuePLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو سال ۱۲۸۷، محمدعلی شاه قاجار مجلس رو بخاطر مخالفتش با ایدئولوژیِ مشروطیت با کمکِ روس‌های حرومی، به توپ بست، و بعد از اون
دوره‌ی دیکتاتوری و استبداد سنگینی
تو ایران شکل گرفت و
آزادی‌خواهان کشته می‌شدند
یک‌سال بعد با اینکه ستارخان تو محاصره شدید بود ولی جبهه هایی شکل گرفت و شمالی‌ها از گیلان و بختیاری‌ها از جنوب به سمت تهران لشکر کشی کردند، و بعد از به‌هم پیوستنشون، سه روز درگیری خیابونی شکل گرفت و در نهایت، روز ۲۵ تیر ۱۲۸۸ محمدعلی شاه به سفارت روسیه فرار کرد و تهران فتح شد
خلاصه که مردم حتی بعد از
یک سرکوب و کشتار سنگین
باز هم ناامید نشدند
و پس از اتحاد اقوام ایرانی
، در
نهایت به خواسته‌شون رسیدند
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68261" target="_blank">📅 16:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68260">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دیشب تو اوج حملات، ترامپ از جمهوری اسلامی بابت آزادکردن یک شهروند آمریکایی که تو سال ۲۰۲۴ بازداشت شده بود، تشکر کرد
خلاصه اگه امشب حمله‌ای نشد یا شدت حملات کم بود دلیلش رو بدونید
#hjAly‌</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68260" target="_blank">📅 16:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68259">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DblqGxbHhG9SGKTZLYxLZfo2keg1i9oPpUr5C8b1h4d5cnU89r6Izr4oXvdpaZ7yPqEodOIGHOKPb9AuXpYbAjJNR-evS8n3gK8sK8QA5up0WRmk_UIpxvBGUZUnzYpnM55TxzLaA7AASQq710RG3eL8hertBa61_uJDnf6nqKeONPzCQ1ulUCgHhFMCsHGStpI5OcmnSoYoszpaUFk9o7c09xaZ9oJcG37HQKzO5I4AdfE_hc-d8MMPUw44DP-8BegNTXk56HGChX-YhUTEeo4Om6bdBSA-Dm_Tu_ufnph2BPOBjCMuw93M-ZOyaHG5VUP1YAexRUvrqZeJBPj2Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوارنگاره جدید میدان ولیعصر تهران که نوشته «who is D nexT one»و هشتگ لیندسی گراهام هم زیرش قرار داره.
همچنین ‌حروفDT- اول نام دونالد ترامپ رو برجسته نوشتن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68259" target="_blank">📅 15:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68258">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">💢
مرد پاکستانی ، عاشق محمدرضاشاه
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68258" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68257">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2UvBAffc8QdtR15R1TFo9V2x9Bw-x93nO3CibuwBfr5VaGP8as8W6O_fBedWDEaSo8fYSSi8Z_717u4PhLb6cq5S2eniPj8umkPstwlglMmnJ4QDnAY0CMtEfa2k4c3GTE4G41DYD8oJmHK0YJcBrxPU4bo7tQq8EvY0wfB8kRrK0SGr1iBDWM_3xy066Sv138-etGzuWqhKZg1dcWtYLv23iXgKHxd8rBuQPNKEcShw2beRGhfSECGOWx2-Vu6KNJuJF_OOpf-CacRPKllvew0Dk6jDlHKv8EOf3GPV3reUgoicPCsfXdMMhvn_2lY-U9bmWE6IHqBUl3fwDchGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نتانیاهو سفر برنامه‌ریزی‌شده خود به ایالات متحده را به تعویق انداخت؛ این تصمیم پس از آن اتخاذ شد که مراسم خاکسپاری سناتور سابق، لیندزی گراهام، به زمانی دیگر در اواخر ماه جاری موکول گردید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68257" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68256">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b50f05a056.mp4?token=N2adigLFu-wLTjzVL8P91BBxW2ymqNVDk4YOGMNfToNPWmDO5csYMk4MTWoRJ0wcHU5l4gKUE-6XQFZ4LKUH7G8WCdeS1agf05V9fGR_zwWfCiwQGpwhkor64sh-01w7ALA07QIYfQANrGQW6CsJmI54vrEzUlq8Is2iNnmuW_wwcdmoHWhFG_JH0B1snMbCNWAAbumYSrhzcYTY498Sf31S_TZ3VVq25ClVsmuwYGNT4xYwHkhTnPc16EGeDtaqcAalmJFHhdWEkRfUtR2QpFHrxteLRFfYLvoSmc6Ox0Rt6RQ9i5AxtDsxd7AcRzNBDpcSWrl0KImXf3iOL_6RPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b50f05a056.mp4?token=N2adigLFu-wLTjzVL8P91BBxW2ymqNVDk4YOGMNfToNPWmDO5csYMk4MTWoRJ0wcHU5l4gKUE-6XQFZ4LKUH7G8WCdeS1agf05V9fGR_zwWfCiwQGpwhkor64sh-01w7ALA07QIYfQANrGQW6CsJmI54vrEzUlq8Is2iNnmuW_wwcdmoHWhFG_JH0B1snMbCNWAAbumYSrhzcYTY498Sf31S_TZ3VVq25ClVsmuwYGNT4xYwHkhTnPc16EGeDtaqcAalmJFHhdWEkRfUtR2QpFHrxteLRFfYLvoSmc6Ox0Rt6RQ9i5AxtDsxd7AcRzNBDpcSWrl0KImXf3iOL_6RPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش مجری‌ها وقتی یارو میگه تشییع خامنه‌ای ۴۰ میلیون نفر حضور داشتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68256" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68255">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTckDIuahV_8ltX1HL6Vg95dZQeh9rvQ54_hASKTk_eM9aVc5HJpVqOPpmykEYCVYd63LUfE1bpyMueQsLeJJB_Lb4TVPxNs21o5xpeCM2umVIk6iZMj46dLtC8mjEaUiBcqIuli_vTRV7e9VkbF-kYSNLg5qZXlFufZPWTnFLjI0xhzKkASbl1r6hAbxWf6QnCQTbWTLsi4o6gfCyynkn8_1cLiLKBYCtc3L66pyxf96BiUnUo4gpPJxtWFfEz80nWQGgXxPdmrodQWO8dkfCuCrEfTxoY4EeEXOKzyX2Ibw57ucVhY6deKRcaJcpTAo2zDI8wV1cO_ythVbe-O3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فینال جام جهانی 28 تیر (یکشنبه) ساعت ده و نیم شبه؛
- یازدهمی‌ها فرداش عربی نهایی دارن
- دوازدهمی‌ها هم دو روز بعدش عربی نهایی دارن
بهترین راه اینه که فینال رو با گزارش عربی نگاه کنید
دیگه عذاب وجدان نمی‌گیرید
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68255" target="_blank">📅 13:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68254">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvVbk-ro6sbrwbl09WT5TYlmPI2CqBDxPCJo6xHRTyykAJfELQbVjcTBXLyso7CwnmgxUK-5KEfqT7FNE8ufuohllhfcwcHPVRNoT8ai7JokVnnvMTwjMo5pwVBVxyot1xbDOa3u8utyZlHCdpD3KlFcNo7EZ9ZYPjkztDE2YTnPb9a-0lI4y4ttr6vdd6ePSJZ7t-rlFcLZ_B928HLH2Ad2swsGq6kp87g8ZOaSKeXwrO5sMFEpCEuOqLXah8Hqp0JsXAb5KQcB8cBtSAE8bTCxtxICAUtpA-dj12hRZydkGDizmD2JZcrO1DRvzOjnbO6zYuU4R5n0q7YBfEN2WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تسنیم:  کارگاه قیرسازی حرم آتیش گرفته!  @News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68254" target="_blank">📅 13:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68253">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34bb460b32.mp4?token=qqkW-tJnqwrAjjtAFCc8Gk7BHxBVcok273oizp4gXyiw6KkdFeCAeOkPIR3AR_I1NOL6wdCoAkHAcuH_ArIVieyWOrQE_mKa3nOqQ8uWB7e8ReStPUAQg1tqzDdkV1coMbWTt8ZVrIRXqnN53qahgElfnmdbThIf1yXgIDPwYgqdANm32cZq5UTtFCo_JQnyGoZrYb8zZwqo7vKnKZvI-IBJNhk600Rpja9v-GieCv72UTjb2jKUb1ah1pVYiNL1zubH-yBAOwTTuqD2G9gi5CaN4Y1XhdKBsa2UZaAxbiZxIKobXdOx9UHg6oiQdY1DjFOt3OHGxUSx7-5CivJb5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34bb460b32.mp4?token=qqkW-tJnqwrAjjtAFCc8Gk7BHxBVcok273oizp4gXyiw6KkdFeCAeOkPIR3AR_I1NOL6wdCoAkHAcuH_ArIVieyWOrQE_mKa3nOqQ8uWB7e8ReStPUAQg1tqzDdkV1coMbWTt8ZVrIRXqnN53qahgElfnmdbThIf1yXgIDPwYgqdANm32cZq5UTtFCo_JQnyGoZrYb8zZwqo7vKnKZvI-IBJNhk600Rpja9v-GieCv72UTjb2jKUb1ah1pVYiNL1zubH-yBAOwTTuqD2G9gi5CaN4Y1XhdKBsa2UZaAxbiZxIKobXdOx9UHg6oiQdY1DjFOt3OHGxUSx7-5CivJb5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تسنیم:
کارگاه قیرسازی حرم آتیش گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68253" target="_blank">📅 12:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68252">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBj5cFgzogfMJZWoZ53XKs0gQDbAu-Q-gs-1lIvCAww1rBj4P8qj6Ap1Lhh3Pu5gVNAKaqfsU1CuYlTeSVs_11PQPvvMyCIEEl7hDkiZvSMnfg5qbISwWguwtRsUO2XIpnMaOaNiLKKJpuZPWwYZVhCzBfHR3USU1T083wdD5qeg77mW_Ta54x4UYRTbX1-yRt1DNySO16XMG0kc_SOkgsVzz5fRlBFFbzadzS02riIzskjXF9gGAqWcadwc5IaSFrIhgHzZazCPs22JU13AKpC2lS4p03-AuA_284Zzl7JwpDks_KgI2LbvEZtdRc7jogEcgFVfpFXePrVu5XM8Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتش‌سوزی در حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68252" target="_blank">📅 12:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68251">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/314324694e.mp4?token=gqFdjQWDp54FrN5nLFu9uLpvVZCREA20_5-D-Y9bmVJoeeYIxIdD0hxTuz4w1-9Gefa8qM54Lrdzp9rJHHqD3MG2iJHPRNla1IONCdtPYT-W6gtIYKzmvY-8xPnvLqLmIg6lUFywNv0m4xiBQRiKja8W1C96jSqXXc4JR5J4A8iIyz0qNN5c_M-f97egAmRq2H35qVHlWMVTyfeXoduFKWPCUq-9ho4RmFA7MkA0NHe0AcIl_Fm4VMhlbxMcclkkSrVBuUTeOVzIHTDvKpbX5LYYOisgK_SxXLycRToPIDa3ZrpXF1W_rKLs7T1Gsp2FNfnE6JhIG4biw2ZYK6s2zoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/314324694e.mp4?token=gqFdjQWDp54FrN5nLFu9uLpvVZCREA20_5-D-Y9bmVJoeeYIxIdD0hxTuz4w1-9Gefa8qM54Lrdzp9rJHHqD3MG2iJHPRNla1IONCdtPYT-W6gtIYKzmvY-8xPnvLqLmIg6lUFywNv0m4xiBQRiKja8W1C96jSqXXc4JR5J4A8iIyz0qNN5c_M-f97egAmRq2H35qVHlWMVTyfeXoduFKWPCUq-9ho4RmFA7MkA0NHe0AcIl_Fm4VMhlbxMcclkkSrVBuUTeOVzIHTDvKpbX5LYYOisgK_SxXLycRToPIDa3ZrpXF1W_rKLs7T1Gsp2FNfnE6JhIG4biw2ZYK6s2zoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام تصاویری از حملات به ایران منتشر کرده است.
این تصاویر شامل برخاستن جنگنده‌های «اف/ای-۱۸ئی سوپر هورنت» نیروی دریایی ایالات متحده از ناو هواپیمابر کلاس نیمیتز «یو‌اس‌اس آبراهام لینکلن» و شلیک موشک‌های کروز «بی‌جی‌ام-۱۰۹ تاماهاوک» از ناوشکن‌های موشک‌انداز کلاس «آرلی برک» است.
اهداف مورد حمله شامل پرتابگرهای متحرک موشک (TEL)، سایت‌های پرتاب پهپاد، هواپیماهایی که پیش‌تر قطعاتشان جدا و از رده خارج شده بودند، و یک دکل مخابراتی بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68251" target="_blank">📅 12:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68250">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GohGMoDA-ZHDRWHg0qmB8d4WCaDKgqzYJXTW25asSOJ2sm6RZdInMoNgyvww5iOZORQtJIl95Je60vy3ips-3vFwr-nExY98RCqrS6L0b4y7tWDPEG209dwDDxn2G0glE38IsqGXES2yPsVpnApY1hr9HnkCmrWqmBAo0lVTUrY4fWIqZluOhlaj-lqSz4sJdSd6__xldS-o52Yuv5Se-iTx1DS7DZcpwo4-wM33rKFCwYt7N04egAL1YwF-0uy0Fo9ksPGkVDi0yaUH42AJ6-0d3jtvM0j1-bUXDEvPth4ajMGJoJkbXdBWQnuhh0n1eOYN1VYvtXjNxYZTuOBKMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ترامپ:
ایران اجازه داده یک شهروند آمریکایی که در دسامبر ۲۰۲۴ و در دوران ریاست‌جمهوری جو بایدن بازداشت شده بود، از کشور خارج شود.
این زن اکنون در سلامت کامل و شرایطی مناسب خارج از ایران قرار دارد. آمریکا از این اقدام مبتنی بر حسن نیت ایران قدردانی می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68250" target="_blank">📅 11:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68249">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bc13721f.mp4?token=pK49GmQvMqmQtXHTnVfhTWZFhQmtNtKFMXhAJlZrak5uD9-6MWAh6RdhjaSkA--nPdOGI_Z8bqRcdoRuwWwjCCciL6I44ACcBw9odnd-1RyC0f8T6b1cVU9JSw2FCxnI3fpSAcISYDgs5fOSECULlc-UZZlB9TTXYvKJ3AtTXZ6AhFS5n5l2PLSJy37mB4UoZqvwuDePEvy7EY4Oxej-tl-C8p60WreVDmNow9q4HpBwpBwLLqKKenQpgL8O6oexdT1zruC4LAJiCWRkSfjz27lTAomLsPKIEZfbFoTT3wqZsvBO1UYc1D9R2NODZzrUkmz-jbxsb1ObVzRUhP27tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bc13721f.mp4?token=pK49GmQvMqmQtXHTnVfhTWZFhQmtNtKFMXhAJlZrak5uD9-6MWAh6RdhjaSkA--nPdOGI_Z8bqRcdoRuwWwjCCciL6I44ACcBw9odnd-1RyC0f8T6b1cVU9JSw2FCxnI3fpSAcISYDgs5fOSECULlc-UZZlB9TTXYvKJ3AtTXZ6AhFS5n5l2PLSJy37mB4UoZqvwuDePEvy7EY4Oxej-tl-C8p60WreVDmNow9q4HpBwpBwLLqKKenQpgL8O6oexdT1zruC4LAJiCWRkSfjz27lTAomLsPKIEZfbFoTT3wqZsvBO1UYc1D9R2NODZzrUkmz-jbxsb1ObVzRUhP27tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پهباد شاهد در حال رفتن به سمت پایگاه های آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68249" target="_blank">📅 11:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68248">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b8221101a.mp4?token=KhZo0yPoMkhOG_Ho8mdM0d6iQJETmJwVTjKYq7FGF5u3pq4Yp6Pz7FhKrvR6NyK2tcepNWmkcSviW3vYHqB9zqAP6QaAhAzVx7k-JWVCN2wKE_8PDCfxFMwKFquwWEynRRz4-cLUzLUk2Cms9AcJ9Umsc-ox0OHjEeJmVGC1XY2wKVPImUhY7sGAQSuE7hz4u2ssBYHr2FDhifLmknuJeAGZXsBJoCxpSNB4xFz3e1QLmbP_7YSnHElb8ijy9DC0SEQuPSETOziImIaRhOP6TbmIe1X_qUHX23vCXOEfwr_sDka0htY3RlqSB7MZfu_B9e53_8weSekap2KmuUXDTngb0LkJ7GeaIU4xOxV8M2b-wH2XW6SpMKVsVlOhawH1KkFetQwe3-indDTVrbz9Pa5D3Vpa-1cgTKeHK3zNPA0PfXsrAlZqouE-Xqh7eoURfAZXuSog91CPuphT8liY6qBFd9BRgwp0BqHIPfiRYBRSJRac-4bOPWxxmvxYe45d3IYnRkM6hB3vxjj93RFIARDlYjI44cbN2LI_MBGMOnYLXX0DApOYWVVNbizVNY80azxFS0MrT3k0JncEBrH_zc6rO7NHCwtlivEQcXAQX5JXVzWCNSrSwHUn3WIiXSStP2b-RVkAs5u1oPWWq4y7gnfm9ClFK1h5JdaQ4BmReks" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b8221101a.mp4?token=KhZo0yPoMkhOG_Ho8mdM0d6iQJETmJwVTjKYq7FGF5u3pq4Yp6Pz7FhKrvR6NyK2tcepNWmkcSviW3vYHqB9zqAP6QaAhAzVx7k-JWVCN2wKE_8PDCfxFMwKFquwWEynRRz4-cLUzLUk2Cms9AcJ9Umsc-ox0OHjEeJmVGC1XY2wKVPImUhY7sGAQSuE7hz4u2ssBYHr2FDhifLmknuJeAGZXsBJoCxpSNB4xFz3e1QLmbP_7YSnHElb8ijy9DC0SEQuPSETOziImIaRhOP6TbmIe1X_qUHX23vCXOEfwr_sDka0htY3RlqSB7MZfu_B9e53_8weSekap2KmuUXDTngb0LkJ7GeaIU4xOxV8M2b-wH2XW6SpMKVsVlOhawH1KkFetQwe3-indDTVrbz9Pa5D3Vpa-1cgTKeHK3zNPA0PfXsrAlZqouE-Xqh7eoURfAZXuSog91CPuphT8liY6qBFd9BRgwp0BqHIPfiRYBRSJRac-4bOPWxxmvxYe45d3IYnRkM6hB3vxjj93RFIARDlYjI44cbN2LI_MBGMOnYLXX0DApOYWVVNbizVNY80azxFS0MrT3k0JncEBrH_zc6rO7NHCwtlivEQcXAQX5JXVzWCNSrSwHUn3WIiXSStP2b-RVkAs5u1oPWWq4y7gnfm9ClFK1h5JdaQ4BmReks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو وایرال شده از یک جوون طرفدار حکومت:
من الان شرایط ازدواج ندارم چون نه خونه دارم نه ماشین
بدیهی ترین چیز برای ازدواج اینه حداقل ماشین و خونه داشته باشی اما خب من ندارم و پدرمم پول نداره که بخره
دلیل وضعیت الان بخوام کوتاه توضیح بدم ؛ سخنان حضرت اقا یک طرف ، وضعیتی که مسئولین درست کردن یک طرف
الان ما باید تا30 سالگی بدوویم تا بتونیم یک زندگی متوسط درست کنیم
الان یک میلیارد طوریه ک ما شما با هفت الی هشت سال کار هم نمیتونی بهش برسی و انقدر هم پول کمیه که شما باهاش نمیتونی یک واحد اپارتمان بخری
با این اوضاع 50 شبه کف خیابونم و هیچ ربطی بهم ندارن.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68248" target="_blank">📅 10:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68247">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⏺
صحبت های روح‌الله زم درباره حلقه نارمک و جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68247" target="_blank">📅 10:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68246">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ay5AsmetGIzVcVtplPKEdMdxORBTp4Na-cfvCN-y156jRO2fRFEVv2mauYEUKEn9eOJEh5GF52IC8V81AZ017CMrksZvW1_9Cpl3NXPpo-_qewnJ9e7KbZjv1U5SAupHk40IH92OQrrXpu_HMAaveOPy2_6wMUFeUsQ_FoObT35dNdK_kgANgjdOKtwusSCwl8KjBsPTsvzbFMMu27x508P40NpMYwjs8S6hmmui0BFK39nk1kVcoEsrV0hdyfm-MLMVGtosg7V1z8zRz4aehevEIxuVtLlOZve1h2wc-EOnwiiy-tDO5tYbZOdDMvrs-967c4-JnOiGHtEVSS0-LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سی‌ان‌ان به نقل از دو منبع آگاه:
دونالد ترامپ، رییس‌جمهوری آمریکا، در حال بررسی گزینه‌های گسترش عملیات نظامی علیه جمهوری اسلامی است. به گفته این منابع، در نشست سه‌شنبه اتاق وضعیت کاخ سفید، راه‌های تشدید فشار بر حکومت ایران برای کاهش کنترل آن بر تنگه هرمز بررسی شد.
بر اساس این گزارش، ترامپ احتمال عملیات برای تصرف جزیره خارک، مهم‌ترین پایانه صادرات نفت ایران، و حمله به تاسیسات زیرزمینی کوه «پیک‌اکس» که گفته می‌شود با برنامه هسته‌ای جمهوری اسلامی مرتبط است را بررسی می‌کند. با این حال، او گفته است ممکن است عملیات زمینی برای تصرف جزیره خارک را کشور دیگری انجام دهد.
سی‌ان‌ان همچنین گزارش داد جی‌دی ونس، معاون رییس‌جمهوری آمریکا، در گفت‌وگویی تاکید کرده است که جنگ تنها با ابزار نظامی به نتیجه نمی‌رسد و در کنار فشار نظامی، گفت‌وگو برای حل بحران نیز ضروری است.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68246" target="_blank">📅 09:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68245">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68245" target="_blank">📅 03:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68244">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KRtlzhi_Y3xdn5W1PQWAmctqqHsTVjpFX5vUH-48Ohr0x3CUK7FxMsejtEiPZPv8gKfqBKqUlUnhlNj62OMQgME7ioBJAdwKvSBNSV86-BEXcJURWiaJaDRLM173LIEt2ikNxZG2G-iyfXKEyOmUmv1Q0yH39IHYDqJq2gkOwdTnq4pd_n3KmYLMT2u42WLN25MkgC6qpV0b2Ir3_Yb6pY3mXPRuIzVwU4DbBN3R7nJ1FaxpRlpYzXgbHxb6HjQE-dCETQ5emfjRGmuXSvKpZFkoINHDjmJvsqjcqNaUVz-3qsL8PDqQt3X3z_aLSj2kbKI2AqFln46LBc0lRf7R5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68244" target="_blank">📅 03:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68243">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4873db94b.mp4?token=t01O5MDke84_K0BOT4tshgEaPXxQYOyaK9XEImvn40i8mVBu4gBe3WAXgcxhL3iFDtgcnS3W7vrXwrejY9eaPPT9-PCTc74FAxLXmdg1haCzRgo4c-jsi7tlRqIOwMzXriY52eogNn7_UJq6XbpZ2XG-ziPj-UIQs-x8SVrfTqZuBZSQcQqvaamCzB8o5lLkD0yLngKpjkcw8Y_LfNFnLCH2wtkyBE_tTb7rVaFJ4R8_mIhj4A9EgzrnWETEIZeOUufBlK7Y3hZWp3RZ2y0KI8OJYCmQDZYx9STPduXiYdItyV5Arp_U0hgd74xvkbF0rPp_dFdtAJHuBtXGkzWc0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4873db94b.mp4?token=t01O5MDke84_K0BOT4tshgEaPXxQYOyaK9XEImvn40i8mVBu4gBe3WAXgcxhL3iFDtgcnS3W7vrXwrejY9eaPPT9-PCTc74FAxLXmdg1haCzRgo4c-jsi7tlRqIOwMzXriY52eogNn7_UJq6XbpZ2XG-ziPj-UIQs-x8SVrfTqZuBZSQcQqvaamCzB8o5lLkD0yLngKpjkcw8Y_LfNFnLCH2wtkyBE_tTb7rVaFJ4R8_mIhj4A9EgzrnWETEIZeOUufBlK7Y3hZWp3RZ2y0KI8OJYCmQDZYx9STPduXiYdItyV5Arp_U0hgd74xvkbF0rPp_dFdtAJHuBtXGkzWc0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پرتاب‌های متعدد موشک‌های پدافندی پاتریوت به سمت پهپادهای ایرانی:
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68243" target="_blank">📅 02:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68242">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1519c2ac09.mp4?token=smqIOWqqdAJvM73kbIVl8twFHhPfOtwXTTMABzcolVII-MZjq5jKX-lw9oUHYbi6Rd1o8GDifUCeDtzvYoLCWRH877H6Gi8ZgyzhhMchMqSMMLxNSxq0fsP7bcFxDGuAwDphbMrEWCb563dC0Zo1329WvbCnATqU3uY7qI7nDfp-xc0oMpGAibDb5UEE-ijSmuehGn5rl8QRBuKWR7MXnKoZh1nmG9GYxhI9ncswWdU5bDLQccOE3cRC7RFvHkVGRTMTnlnCHwHaion0v5HVmkUW48fDYNxufNT1HfpoXBVc3GfCxNX4zLi7rWX1udVPTbHnQ6KqCtRFbk3jyLZYDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1519c2ac09.mp4?token=smqIOWqqdAJvM73kbIVl8twFHhPfOtwXTTMABzcolVII-MZjq5jKX-lw9oUHYbi6Rd1o8GDifUCeDtzvYoLCWRH877H6Gi8ZgyzhhMchMqSMMLxNSxq0fsP7bcFxDGuAwDphbMrEWCb563dC0Zo1329WvbCnATqU3uY7qI7nDfp-xc0oMpGAibDb5UEE-ijSmuehGn5rl8QRBuKWR7MXnKoZh1nmG9GYxhI9ncswWdU5bDLQccOE3cRC7RFvHkVGRTMTnlnCHwHaion0v5HVmkUW48fDYNxufNT1HfpoXBVc3GfCxNX4zLi7rWX1udVPTbHnQ6KqCtRFbk3jyLZYDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68242" target="_blank">📅 02:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68241">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYFQKe6UCAcIFc7rvftWyLaVCsDgaCUVU_NqSgKGqPjQjPBa9GvIShKWkuPuC9zJ3gN9q2OhYFYjJpy9JEsobtr8ASSHfcYHLpqgLEXBvgIwToi20M_RG41L5I4N7z7f5eLDaRpBrlUeZ8Z-_aZVKclc8O5d-OnhCgL01ESTYYBfmyRcKxLdxo3uwhvQefI34uWATYdZlfbVHc7fxOo2H2-aHANKxOUE6Ktwxfx54kev5trs0Z2BbfROdRsYwjQOegau-qDbDDkbfYkFXY8Ld-ONLivzomgd-BG15Eggj9pON-7suqTAPB23_3XMuiwBWdc_52Iv_KSWYS6Q3lICiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68241" target="_blank">📅 01:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68240">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68240" target="_blank">📅 01:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68239">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd7e59689.mp4?token=sR93TwZEkuA6R6pvbK9xvE_Gu6Kip-rjO6ktKceTlVeF-tXZbPpkLzqYX_hf5KI_MDujlbq80NhTVZEvXqlhkK-ga87sZIYHgdqRteiJGXjQ6WlY4chv-o1J2xyZwZN0HkCmhPcMatTBqu3p3DiC1mUjZLSZrwLyC_nUK1snH-giB0_dDlx3dFfmYBwlt3KP2PuEvj5Hiyvjvkt736ALwlgEgD3gge8SynSeVHrkgAQIjxI6ul1YRR28u0tDhWgDHVbq1ej_pZKv0hS7QCxM4aij8vVWG3sDg-01JUgDkWj7ImFKLkntItYQyLUfI7eJuiEDT425afNKAiDbU7ACRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd7e59689.mp4?token=sR93TwZEkuA6R6pvbK9xvE_Gu6Kip-rjO6ktKceTlVeF-tXZbPpkLzqYX_hf5KI_MDujlbq80NhTVZEvXqlhkK-ga87sZIYHgdqRteiJGXjQ6WlY4chv-o1J2xyZwZN0HkCmhPcMatTBqu3p3DiC1mUjZLSZrwLyC_nUK1snH-giB0_dDlx3dFfmYBwlt3KP2PuEvj5Hiyvjvkt736ALwlgEgD3gge8SynSeVHrkgAQIjxI6ul1YRR28u0tDhWgDHVbq1ej_pZKv0hS7QCxM4aij8vVWG3sDg-01JUgDkWj7ImFKLkntItYQyLUfI7eJuiEDT425afNKAiDbU7ACRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سنتکام تصاویری از اصابت چندین موشک هلفایر به موتورخانه نفتکش M/T Belma که در خلیج فارس در حال حرکت به سمت جزیره خارگ بود را منتشر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68239" target="_blank">📅 01:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68238">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
بندرعباس بوووم
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68238" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68237">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fl130Dciwjfec5BPveJ-EXquxF0UdjUaW6x0JwwGCcIjnN1Vx5mNMxBNuJX3idEJ2woXqIeiYUEJCvfkIPJbjsiqBAZ7Xln4ok17ZbicAS-G_-JwIh91O5l9egjA9LbUEbCPi_vRwaJzmj1lvbVkWfuKDbc5KNLIZp-NrsqubKnup_7-24R37Hmt3MN2NqNvtE2MHweILqZzDSzkbbYFXdyHcH9pGUZiu8Avkg7CyZEju--1xBrBTNyDwssori948P-epI3sLNw1FLf7rnRTpimRwoa1ox6ycwxgalHRIRORYVaMyaPflFm2jO9G_8F_zQDY9mL1AC80HN6UuP6mFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی| امشب روح فوتبال ارضا شد
🇦🇷
آرژانتین
😀
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/68237" target="_blank">📅 01:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68236">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68236" target="_blank">📅 00:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68235">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J4YyIlfG-npUHdNxk1VUYUhWPvU6q1lNnyC8X8CZb8l4OSh8ZjdYplzUz04F4FKHo_uL7Cz7yQGfEHgJ0JZKTukhqOqKsmd9x87QCFitLjYN77_SsBxgjQ7nwkti5ZTDAj2LGmHxbNyBld-_nK4NT8TL7OpHxL0fr83w40-i2JRY5S_vbWNFwK4GpG2_W4fVSfVRD-MCAv9uPK91Qz6HPkebdYZ1sQmLXfcTmxXBZle5kMy2sO7tHR7kbqa4CYjtyq77A6-24Wen-PzaZ_8fBco5Ff-ArCMFF3I8HxKA35FAndNUWGdmuAq8RRajPCB8oEZvlazydsW56liYCPpJZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی| امشب روح فوتبال ارضا شد
🇦🇷
آرژانتین
😀
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68235" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68234">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">من خودم رئالیم ولی برای مسی باید ایستاده دست زد
😑
#hjAly‌</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68234" target="_blank">📅 00:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68233">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d327baf32e.mp4?token=F5bgmKiqUzHzthe38Mrz1VGQfSg7duodJUNrK8JNqup4vlYPvNlH_6akooUP5HOF0pNrgebaIyCyfcREXBIxVJKeguWny5tuNVovSukx85vONN-nkRVgePX6cnBcaBCu8EZ5DVn-cW2LYrmkWbiTOur4934xMNFnB7RfxR7GrTO5-Wz0B5Q2ooQON2WrcBKGmaGhKX9Y8U6eKJkNP345rKwP_Cky7VlEwaMJkNSbAuakcw1L8lIK-xlHV3wTZLBU_U2adrSLpQisH-qMJQG83esvYJFNS35KlBLsJg1Q1Ln9SXWRvhDCiKCS9aWX6DCr2C3muLBBTf5RtrGkbswfSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d327baf32e.mp4?token=F5bgmKiqUzHzthe38Mrz1VGQfSg7duodJUNrK8JNqup4vlYPvNlH_6akooUP5HOF0pNrgebaIyCyfcREXBIxVJKeguWny5tuNVovSukx85vONN-nkRVgePX6cnBcaBCu8EZ5DVn-cW2LYrmkWbiTOur4934xMNFnB7RfxR7GrTO5-Wz0B5Q2ooQON2WrcBKGmaGhKX9Y8U6eKJkNP345rKwP_Cky7VlEwaMJkNSbAuakcw1L8lIK-xlHV3wTZLBU_U2adrSLpQisH-qMJQG83esvYJFNS35KlBLsJg1Q1Ln9SXWRvhDCiKCS9aWX6DCr2C3muLBBTf5RtrGkbswfSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#hjAly‌</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68233" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68232">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گللل دومممم آرژانتین
💢
💢
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68232" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68231">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گگیایایتیلیاایایاااللل دوممممم</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68231" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68230">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گلللللل تساوی آرژانتین به انگلیسِ کثیف
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68230" target="_blank">📅 00:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68229">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گلللللل تساوی آرژانتین به انگلیسِ کثیف
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68229" target="_blank">📅 00:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68228">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">درووود بر روح پاک مارادونااااااا درود بر بیبییی</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68228" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

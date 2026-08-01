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
<img src="https://cdn4.telesco.pe/file/Gp3qmQy6DC_021UOMH26IRfSipgIgLWN7FYgSfbCq5M2Dx78dIXXYe3fE_LWgMkUTS2C0etB6YMRUfNa_ZAubv2ofnXIPCg1LRl3kGbQyoJXawEayspiS1FqUQnbmulePoIvaaP7MJr-1w_9Ohxd7q_kdmoD9QqymROvreta6cR_XOkATh2fpaDtZy83-u_iNZ7_CAH94akpM0bgEZ9gO_a3ejpmsLxZWDuyV3y3CEV-qvsiQ9jA3W_kbWBAncPnUzKbekGXkLTcXuZibti09wnzIm3OM68KrVAXsbUefAcz8QqD9uyNCW6Wtc1k3ZrcPiy05pMNijZsWpC18pACrQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 20:20:57</div>
<hr>

<div class="tg-post" id="msg-453888">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a7e74c10c.mp4?token=aJAYCfG3O8wBV7nSp4vRvkTwle_SGJj_J9DLc4SaVIbw1oJV1VLtmG1FaLqamlWq_m2Wr7_zBg99D94oX0Hs9brllMp7WJbT4TIxhkIz1kUnyPt2P_ri3uu88GTSDnUDseI4-BBWFSo0yP3s3xRSK7dbtRYlReU0tLTCQ9AwVWdQvWrxaRTWqlq-ZFdcUoMDZJISESWY57r0O_NV2X-MHldv3Kdr1aw55vkFGT-AbsBhtxGXZXIvWz4Kc0pkE9EG5K-AqIIp60eCmjAAzGQbgjC4xGSamrWwhEB2m3JKYiTyUNPFbM2Y3o0WsobRQqsPhvYm2C8SNGSvCzUwvYQ-dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a7e74c10c.mp4?token=aJAYCfG3O8wBV7nSp4vRvkTwle_SGJj_J9DLc4SaVIbw1oJV1VLtmG1FaLqamlWq_m2Wr7_zBg99D94oX0Hs9brllMp7WJbT4TIxhkIz1kUnyPt2P_ri3uu88GTSDnUDseI4-BBWFSo0yP3s3xRSK7dbtRYlReU0tLTCQ9AwVWdQvWrxaRTWqlq-ZFdcUoMDZJISESWY57r0O_NV2X-MHldv3Kdr1aw55vkFGT-AbsBhtxGXZXIvWz4Kc0pkE9EG5K-AqIIp60eCmjAAzGQbgjC4xGSamrWwhEB2m3JKYiTyUNPFbM2Y3o0WsobRQqsPhvYm2C8SNGSvCzUwvYQ-dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیگیری تلفنی پزشکیان برای پرداخت حقوق اعضای هیئت علمی: این تاخیر ۱۰ روزه واقعاً قابل قبول نیست. کاری کنید که اساتید بیش از این ناراضی نشوند
@Farsna</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/farsna/453888" target="_blank">📅 20:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453887">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcfb546460.mp4?token=s1GSMbdDW3jWPGfb7GYb2AVsTZsAj196FqCk1_TrIg4AGiyhb8DLGsxH09Zx1rDXRLPtApPEG6O8TziHE8X_AdzZH1cByhRjT84TzMK4pVv6EML97wrfHrJurqAETpWuRGd9Jw87HwAm5scoISBKLiY6usGvzWEzZ4Qk2nhNzsAP0VTeLThavKTU2We0lYpTQXwMYbmwnAaJ0DCAYs4mDWTxDWOFtg7zdc4wt3-nOSaRtQt2U5IzQ8U3NFrAaI13nPCqDD5Rrxd8BUihVATRlrOEJ1ktw0aSvCC3o8pLcwXCTvnWK8rl19_ThfR3tVPBoTveUNw_cLKtxAtZ5tDOaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcfb546460.mp4?token=s1GSMbdDW3jWPGfb7GYb2AVsTZsAj196FqCk1_TrIg4AGiyhb8DLGsxH09Zx1rDXRLPtApPEG6O8TziHE8X_AdzZH1cByhRjT84TzMK4pVv6EML97wrfHrJurqAETpWuRGd9Jw87HwAm5scoISBKLiY6usGvzWEzZ4Qk2nhNzsAP0VTeLThavKTU2We0lYpTQXwMYbmwnAaJ0DCAYs4mDWTxDWOFtg7zdc4wt3-nOSaRtQt2U5IzQ8U3NFrAaI13nPCqDD5Rrxd8BUihVATRlrOEJ1ktw0aSvCC3o8pLcwXCTvnWK8rl19_ThfR3tVPBoTveUNw_cLKtxAtZ5tDOaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع پیکر سرهنگ شهید یونس حاج‌عزیزی در تویسرکان
🔹
خلبان حاج‌عزیزی، شامگاه هشتم مرداد در جریان حملۀ دشمن آمریکایی به کرمانشاه به  شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/farsna/453887" target="_blank">📅 19:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453886">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f2e72ce2a.mp4?token=iwXevjXQ6FnCp-x_WEgUT5cAhxNd_l_YN5PcwXoRAaJuKrjKFu_PZoh1W4amX1AKqe5QnENzM7FgXm22Nc49jf5aJh847qnMuEZ_ctLKlTBDCNme2AtG3G2CgvVGzI9YTk4pp7j6eOiUoDrGbgGoYOO25rdl5wbLQJirWR1Y2VZpaOIc8K1hDbYgZnT3rk4Tu1emFLWexreYUTgtSSehv_ThXgP_RrkM1QsWao7wXeAWP3DH5ZJnBx8vM6XB_2kyacZpKctGFwxvxRomiA4Bu5RXvdDL31d0y4RVkz2dSv68KEmfkaM6ZuaKaV_0gyGPXSfxKstYPtI6IX7NfW7fYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f2e72ce2a.mp4?token=iwXevjXQ6FnCp-x_WEgUT5cAhxNd_l_YN5PcwXoRAaJuKrjKFu_PZoh1W4amX1AKqe5QnENzM7FgXm22Nc49jf5aJh847qnMuEZ_ctLKlTBDCNme2AtG3G2CgvVGzI9YTk4pp7j6eOiUoDrGbgGoYOO25rdl5wbLQJirWR1Y2VZpaOIc8K1hDbYgZnT3rk4Tu1emFLWexreYUTgtSSehv_ThXgP_RrkM1QsWao7wXeAWP3DH5ZJnBx8vM6XB_2kyacZpKctGFwxvxRomiA4Bu5RXvdDL31d0y4RVkz2dSv68KEmfkaM6ZuaKaV_0gyGPXSfxKstYPtI6IX7NfW7fYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تردد در مرز مهران، ۳ روز مانده به اربعین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/453886" target="_blank">📅 19:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453885">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiYeFz51KGCkUi5XJG6qJrl382T3tqiKPZXTOBVOsQW0qQRfy0g2DO5OHjqkm92Xf5ve5tCqvTTN9wIX66crqjqyzHNvB4yjjjWY3SQBsYJrn10jqmtdumAjM3uVeEnQhlQIfluEGl8wRaslEmPUs27IN3cvA8CvTunVk846GZNKj_IJ9aRcnwUa7ihMY8Nz37Bf1kCqFgOBqcj7Wto0bZodDQ0aJBoNNIcS6chANlAs6tp_r2cl9lLvBbODBAWPzmNMSX9AaNfMYZr8K96OIweM6DKrg6f4tL1JC6H8LohHdKjtZ8pRUnvkzXoPaysZzWphYNtyDEBeJ4PdPzZ38g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لغو واگذاری ۹۵ درصد سهام هفت‌تپه از طریق بورس
🔹
در پی دستور وزیر امور اقتصادی و دارایی و مصوبه هیئت واگذاری، واگذاری ۹۵ درصد سهام شرکت کشت و صنعت هفت‌تپه از طریق بورس لغو شد.
🔹
نماینده مردم شوش و کرخه: اجازه ندادیم تا پیش از تعیین تکلیف شفاف و قانونی مالکیت هفت‌تپه حقوق کارگران نادیده گرفته شود.
🔹
بر اساس تصمیم اتخاذشده، سهام شرکت کشت و صنعت هفت‌تپه به بانک‌های ملی و صادرات واگذار شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/farsna/453885" target="_blank">📅 19:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453884">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فوت ۲ کارگر در معدن مس محلات
🔹
فرماندار محلات: دو کارگر در معدن مس محمدآباد شهرستان محلات در اثر حادثه فوت کردند.
🔸
طی هفته‌های گذشته نیز یک نفر در اثر ترکیدگی لاستیک کامیون معدن (دامپتراک) در همین معدن فوت کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/453884" target="_blank">📅 19:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453883">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/588f00e937.mp4?token=QBSCstsknbtNykzFlDecpuG3daTM4QfcmrTbPgDH1LOEhOwaaGA85MeBddKh5Fq18KWyQD3nCGHr1ZJI71NESsEpT_wZXNClu4rTxIGZk6NcZQrzQA9SzyRYqHJh9S3TxaAWulZEHx2ZeE2QD3fxANmTc9tbCV2CThbnjSKu2KBeMSqOqz4Qgxrbjv2JvEMWoVHi4JXubklOrsGjtxBe0L-Ng90WhDkVfIN2dYlvkGwuw_E0Rq8nModnyu-vfU5p9aJk0m-JelXpzP0HHHQYWO_IMsGbcG9tLWWLwcOeobf5lcQm3qYOrXFBg-d3HmBGuI2XZDssdGbtVCtUNBLxQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/588f00e937.mp4?token=QBSCstsknbtNykzFlDecpuG3daTM4QfcmrTbPgDH1LOEhOwaaGA85MeBddKh5Fq18KWyQD3nCGHr1ZJI71NESsEpT_wZXNClu4rTxIGZk6NcZQrzQA9SzyRYqHJh9S3TxaAWulZEHx2ZeE2QD3fxANmTc9tbCV2CThbnjSKu2KBeMSqOqz4Qgxrbjv2JvEMWoVHi4JXubklOrsGjtxBe0L-Ng90WhDkVfIN2dYlvkGwuw_E0Rq8nModnyu-vfU5p9aJk0m-JelXpzP0HHHQYWO_IMsGbcG9tLWWLwcOeobf5lcQm3qYOrXFBg-d3HmBGuI2XZDssdGbtVCtUNBLxQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پلیس گذرنامه عراق به صاحب این عکس افتخار می‌کند
@Farsna</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/453883" target="_blank">📅 19:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453882">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoXgWRVWcZ8f-kUfONiOBeq7KvTjYjnmQ7LyxnHBNJj218twfN8r2DpOS9DRWUbz_rkf1ekdXVPKEVLYrLyceKGb_j3GlmBd7ARehYPbogDu0fNiYGyNN9S1BUZ6epmg5FLr2HepQoaZ-SBGaBFEzqiw2SyTjyRv7p0IA-xWwGNIZgiFWwC9uHpXNsVu5ZJu4rxVMKUadJJlzenpAMTDRVNWdo7AKmDSyQHnvzUoY-nnskndbVWhtqMe7bGBDBd1DV9Ock7Reyp1gMYyIEtDk2z03AtxAWyoYykumB5Bx4kqdJznRX7Ud437zVJiKLQ8noZlFVVQF-vwUJLAYqG27A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ مدال رنگارنگ کشتی‌گیران نوجوان ایران در رقابت‌های جهانی
🔹
در پایان رقابت‌های رده‌بندی و فینال ۵ وزن اول کشتی آزاد نوجوانان قهرمانی جهان در شهر باکو، امیرعلی فراستی به مدال طلا دست یافت و آرمان الهی و سام ارشد صاحب مدال برنز شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/453882" target="_blank">📅 19:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453881">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e6e2dece.mp4?token=ZULemshEbKh9mZCWfeZ9ehcCtKI5XafrnuRYPpD12HZ79znjig-x1adXgT8RPPKDCflDsgiD1yMesWOhJTiGSAjIbWuhyAzYqnGAc4fBwr1-MEiZRgY6pXCLob21DJe17s5IdVCsU-N1RzNT616cW0-HLORfu8DkD3wxJQPCXA4k0oSTEMZeq6GJfYqNrXBQ3HDAYLLPark3WEicYZnKb2ev4EJvRcykw9aFzrPPAGlpFNyCmsQpCWIodTBglLgEkzmWjBzNwg4mjqLO9T6Wc1VsMUAkjwXvMooOlFlBM9TxRXlJ8i7CRCkWWAxAKJ33R1_1MqYBLOjzkhX4x6AJMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e6e2dece.mp4?token=ZULemshEbKh9mZCWfeZ9ehcCtKI5XafrnuRYPpD12HZ79znjig-x1adXgT8RPPKDCflDsgiD1yMesWOhJTiGSAjIbWuhyAzYqnGAc4fBwr1-MEiZRgY6pXCLob21DJe17s5IdVCsU-N1RzNT616cW0-HLORfu8DkD3wxJQPCXA4k0oSTEMZeq6GJfYqNrXBQ3HDAYLLPark3WEicYZnKb2ev4EJvRcykw9aFzrPPAGlpFNyCmsQpCWIodTBglLgEkzmWjBzNwg4mjqLO9T6Wc1VsMUAkjwXvMooOlFlBM9TxRXlJ8i7CRCkWWAxAKJ33R1_1MqYBLOjzkhX4x6AJMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در سلیمانیه عراق و بلندشدن ستون دود از پایگاه‌های تجزیه‌طلبان خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/453881" target="_blank">📅 18:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453880">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEKq1mwTgM4MWKd3ufu9Mh9thzrbwUSr6StGdyzgNJN9yLpwp6wyjSNypa5FiyNFIBOoS3wuQ2ssZgp4QLheZzj7kQ93ENsyqVe_knNopmKloyjCteS9_zZ9YLuEhoSQt6JW8hYzK2w9Zt13fri9mZ27NVJcricCtW6NEjgqcQBr6qzZmvzXIc7e3rN2Igl8EmCWr3HIvFVHkJ-gGVaO6J3cTi94IGxT1NUA_ZhXHL4G7xv29vbqwXK1apsJD6t23jADO3vv0BVARUuwOL_hriDYRdNfvvYvW3LpzHMoIR_3msojQYjQqcByVblKKSxcHjxRuqF_INWAG7Zs-fu0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پیام عراقی‌ها برای زائران ایرانی
🔸
آسمان‌مان برای موشکهایتان و زمین‌مان برای زائرانتان
@Farsna</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/453880" target="_blank">📅 18:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453879">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C52tB3GQuspeq2oAuzOsCNJzcTSiiz-SKhiqQ-NNglT5cmJIxZT4M9OqNGf5bz8e6EUkxDMUkbNPzjVLsxgXP1Ox5EtsRx_nbFSO5c_zGA4oTxeS9H6TuF4983EsnOd4u1A3QqyXm0p5-Dw9wd6efB2qLZ-SXWLH08VjB5iwPFMwOTEdaOffQuruHmAdiMqvF8XUjULSOGOl6LH_fMFkqAdVtPOMp_csQ7aYXM7G8HTSBivnYR8M9Acwrhmw7lUd1hR2xNZIgSYZYETbYnGcxRO6-HFu2lQ_9uoK0gj5XQqtonOH200qi9mxz3brObUqpIm7vIf6m-ZqmRX9AwGzyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مخبر: زیرساخت‌های ایران خط قرمز است
🔹
محمد مخبر در واکنش به تهدیدهای ترامپ علیه ملت ایران: شما با معادلات نظامی محاسبه می‌کنید، اما ما با منطق تاریخ پاسخ می‌دهیم.
🔹
تعرض به زیرساخت‌های ایران، مستقیماً گسل‌هایی را بیدار می‌کند که ۲۵۰ سال معماری هژمونی شما روی آن‌ها بنا شده است.
🔹
وقتی ستون‌های این سیستم فروبریزد، دیگر نه مرکزی برای فرماندهی می‌ماند و نه بازاری برای غارت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/453879" target="_blank">📅 18:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453878">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9XvfwL22vyT2slWsu8IThx7G9J2beieTxKadzuXvCYEonDObCc2Jgq4HAg8ZoOFU11aoYD6Vgd7r6kXv8Q4lZ3X5eQs2Mwy0aL59clabxQNfl3Gds9-bputwEvBtqL1kyFFHNG47Sr_XdycHlzxNawj90A-9Lj_ihwvEZDZ6vj1cwNBLnP0M6MZW3vDXDYii3VDUCgvG9IfN2qZjHKkSlYRaqpRNDIHuIkcLTm_g427YEMVef_YpuStcvQc_lDxbvqmGFHtqGkPq6WPSFnsywn8DaYnPTMaV6aakah_2lZcfbkJAUFmGrC76k1gROTFA7l66GN7KpCgAw_icsWazg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای جدید از آتش‌سوزی پالایشگاه جازان عربستان
🔹
ستون‌های دود در این پالایشگاه پس‌از گذشت ۳ روز از حملات یمن همچنان بالا می‌رود. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/453878" target="_blank">📅 18:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453877">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRn97nUncvSg1eqAvkL68sKJaeie9YOUJaUDGPHu7OJ3anNx2QxoghOmGEN2YVJTU8qOIG_V0gTUF2HnWI8qr0bBiH71InSxAVuk_TWz4RgewFcBXm4eWJysK7GLOWQ_jTVNQFtC1jTlpey-9niRbTyVPYKVGQVk9_unQxZl0nvbfB_vrVKzqG-A6IRrOgxEbHjwfyDz9-efBnx1P6u6-aXJRBZGEHeP1hx5y7VJ4I6czWa-GEpCtb6OnLL1WrgCRbla-UhWAxLAAb6dQqwbt-eJmvgAItomTc-h31PoRs_EjgfZlL9PfM2RQsyIl_71fZmn-_igF6E-nvjulKuzKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایپا قیمت پراید وانت را بالا برد
🔹
سایپا قیمت کارخانه‌ای وانت ۱۵۱ ارتقایافته را افزایش داد. قیمت پایۀ این خودرو بسته به تیپ، به حدود ۷۶۳ تا ۷۷۵ میلیون تومان رسیده است.
🔹
این قیمت‌ها نهایی نیست و هزینه‌هایی مانند مالیات و بیمه به آن اضافه می‌شود.
🔹
خریدارانی که تسویۀ کامل کرده‌اند یا تاریخ تحویل خودروی‌شان گذشته، مشمول این افزایش قیمت نخواهند شد.
🔹
سایپا اعلام کرده از محل این افزایش قیمت، حدود ۶ هزار و ۶۰۵ میلیارد تومان درآمد جدید کسب خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/453877" target="_blank">📅 18:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453876">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d52c5baf.mp4?token=hk81UDew1Tsvo_SL-oO61wwS2mSsjahPBCEC73MW5bd35fXWTJfVFrmtmsJlZSmQ-gNBjGDX94FiQ1EI5hfW-zLBH1fl7NNpfxxfSiz32rF5DsFTUzoBPirSE2cFpZKpTLSG7u75TT6txS4eFyEAZw4GTxDnAtGmpFW_ykzQJzVBwJgj6q7JfyhtfZByp8yLHfoF7gNzULWS_04m5oSYBEwQ2IotHuVYG6_UzhVW3yv-7Jw8okHiAU48z5Ev5_PvXLZMq3avSDjRRyfM40B5NTq-Ku1ph0WiNJv0eeOWG6adZzDY2LbF8Kz_3VC47fHMfj6154gmpwq5Ilj1ia9fZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d52c5baf.mp4?token=hk81UDew1Tsvo_SL-oO61wwS2mSsjahPBCEC73MW5bd35fXWTJfVFrmtmsJlZSmQ-gNBjGDX94FiQ1EI5hfW-zLBH1fl7NNpfxxfSiz32rF5DsFTUzoBPirSE2cFpZKpTLSG7u75TT6txS4eFyEAZw4GTxDnAtGmpFW_ykzQJzVBwJgj6q7JfyhtfZByp8yLHfoF7gNzULWS_04m5oSYBEwQ2IotHuVYG6_UzhVW3yv-7Jw8okHiAU48z5Ev5_PvXLZMq3avSDjRRyfM40B5NTq-Ku1ph0WiNJv0eeOWG6adZzDY2LbF8Kz_3VC47fHMfj6154gmpwq5Ilj1ia9fZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت شهادت جنین ۶ ماهه در حمله به مدرسه میناب در برنامه پرچمدار
@Farsna</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/453876" target="_blank">📅 18:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453875">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در سلیمانیه عراق و بلندشدن ستون دود از پایگاه‌های تجزیه‌طلبان خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/453875" target="_blank">📅 18:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453874">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">آخرین تیر ترکش فدراسیون برای احیای سهمیه چادرملو
سخنگوی فدراسیون فوتبال:
💬
مقرر شد هیئتی متشکل از فدراسیون فوتبال و باشگاه چادرملو راهی مقر کنفدراسیون فوتبال آسیا شوند تا به‌صورت میدانی مواردی را که با AFC مکاتبه شده با مقامات کنفدراسیون فوتبال آسیا در میان بگذارند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/453874" target="_blank">📅 17:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453873">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJfZLEfkpa5C9qBBmPL9U9rWVU72ttYYKCfp30Yd1YjK7J39Y856RdlqNaMHTuLndZ-12d2YhF42UZ2oydz7pEnE04BH8uBX5LlCF5TPyDcjjWrUyW9m2ZoV2WsnfpXEvpBXQ8xm-cdQijFyiJ4iET-3dPvqhtTHqHPHc-BXjxyKxIc0VN1l8SCqxkuL7OzHwQ3_FyrsmKB_pm7JcAXKDhKwhfCSmKssMA9FRjKKa70SD69FMFxp8BJH87_xseN7kWLzXkYlriZgZeVw8MPxvS5Kc9hpUDrHE_uJnVLuWpRvFEPZ20bc6sIWHOkcMMYk5T2R7ZWrd5-jzpOb9q7DYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
یادمان شهدای مدرسۀ میناب در شارع‌الرسول نجف اشرف
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/453873" target="_blank">📅 17:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453872">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psWBDzClH7FLIodlfyo_Rk09bI3huGVMjdOkXI6edy-0BXXW84BvM923ynoTN6LbjO4FY6tMu_7p-Cvjjg4u9VF5haYuIY3gZ2o3NkQtrQfawv1cW7vB42V3NOAH73TXrS7J9OzHegEkIQS0X_inT7BWlMnaBUy-p06NZVhLho8kXizGOL-O1Vbs5QOTZaAHA25OT781cIMQLKa263CC0z91QV7fV7eReXUc1VwXZEhLOjzRZoLUuzJeQYfszSRSDG6d-5mXvxTGbhL57gcof2YIDZw7rmzc_gwlZPK-KOaZGBZYYp0SHYPqTbdTvGvBlO7oGyuGWPtgzGN-eKX9NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تداوم اقدامات حمایتی بانک صادرات ایران همزمان با پایداری سامانه‌ها/ جریمه اقساط تسهیلات در دوره اختلال حذف شد
🔹
بانک صادرات ایران با هدف جلب رضایت مشتریان تسهیلاتی و دارندگان کارت‌های اعتباری، جریمه تاخیر در پرداخت اقساط مربوط به دوره ناپایداری سامانه‌ها را حذف کرد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/453872" target="_blank">📅 17:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453871">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0x1YisiHeXjSgYcuF_-SG_vl89l8JpzMDYLr0RU7T3jbc-cqAmdaLCQugDSjJTXVnfrNpXxSbqmoD_brzV7ZrF_cZA5i7uBbgUi7JSnDcUlRajY3y3gmnDElz45mRFP7u-8orQCseVaRZvSPI3UPDhQe04zVPT9EIo3PpcK0j9Bp6y8MyzWoDGapTQmssCqhhr69Fzvrfq1lAMu36Feb-gIuDVPVUeQWX0l3-JewbjZtr9pEH6oU9TshUd3fIyexDYzfUiKrsGt2WhPdsGm_o7Aq5TZ8I0YL1Ygc5f9HytQ49CUYtGyCaJc9mnlvhxeGev_11zuqKOD5SZoh5iWzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح امداد جاده‌ای کرمان موتور ویژه اربعین ۱۴۰۵
امداد جاده‌ای کرمان موتور ویژه اربعین ۱۴۰۵ از سه‌شنبه ۶ مرداد تا چهارشنبه ۱۴ مرداد اجرا می‌شود.
در این طرح، خودروهای امدادی کرمان موتور در مسیرهای پرتردد و منتهی به مرزهای غربی کشور مستقر هستند تا خدمات امدادی را با سرعت و سهولت بیشتری به مشتریان ارائه دهند.
شماره تماس و سایت امداد کرمان موتور:
٠٢١-۴٢٧٢۴
emdad.kermanmotor.com</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/453871" target="_blank">📅 17:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453870">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/453870" target="_blank">📅 17:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453869">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMzUfRn8q7MpC1MlQcnx6s6nPMjMjRDLbn8WSC6K6f5mAZ7CdI2nuYyHCUtNR-AcY4BuheGbppgM08zDDBsZj3B6CLfJOaDGG1EdFS14LWI5GjYiQfDVtlvMQIeG-ltRvMAtch38sJW4rwuciwHblE3Wd4KnhiQDlEHylDVKCpWIwWa-dyktSjfKEkDWfF-pZZb9feG29OBAMdjCoYpk5h0tKvOM_S8sJ-VnGh1AHI5ChEe3JgVtKcEwxEQ1njCtN0hNssU3BrpSh_6Sf45qgcXRV-Q4WxEHey1ks6RP4OLt-Iw_ojJ-Li2RcKY6b8bIAP8rVRIMAG2KIiuTrv2D6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از پیکر شهید ۲ سالۀ جنایت آمریکا در قشم
🔹
سینا جعفری به‌همراه پدر و مادرش بامداد امروز در حملۀ آمریکای جنایتکار به قشم آسمانی شدند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/453869" target="_blank">📅 17:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453868">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgVar7OaIXpNfzmG-8XGFSnRqVmeOUw_g2ZNUQSORJlTZ1OYx0VaOilAdX4wt4heoALvq03EJSVSPLiW71mxQgNkMgVqjd0GbIbWj6ttR_ZbY1EyxpNM0wWn4i0agGbKV-CBHu-c3vf4qTxCtXHucJL60-sPN_4375sbROWYtiqr5FWQj6NCuTD7Lg89I1bx2D3OLNhk5r0VuHi4ScmJqJYCanol0ONS1u-EZUIzRIvIFniWT3CvQx1pexVVBQJdy3k4gCaK0j5dDWFePEPQG0hdrKrnVpyyNUO_0az4L8Ejdq768AuyUpiuF3BFbnGffZ5Z9L82kAtMIp9-MkzImA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حادثۀ دریایی در دریای عمان
🔹
مرکز عملیات تجارت دریایی انگلیس: در پی اصابت یک پرتابه به یک نفتکش در نزدیکی سواحل عمان، موتورخانه این شناور دچار آسیب شد و کنترل خود را از دست داد.  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/453868" target="_blank">📅 17:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453867">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_QBrYMojyc7NPizgDJ0hhjO78nXo5BpPsCktW72t0RjWrqLb2nLTEjaps4iWaP5cNUi-cn9-W4qhysgRtsHYWjNALAY9BV3A1DbylB254FmU9lWZXDU3SV6HeZT9HNNTn_iK7QW0uj9xpgmbTA2nru63LjcDIp3fmFgV2oj-au56vI9X-AKHTz6MJqgIFMIQDRlTXs_m6mdZOIx-FhDgHhtdN-cHSBxeDIlrvuSmjDCMkReZwhbBEEPMXe10ZHGrxXVgOq8XCUb8fbkwQ-X1thPgJyns4FT5-lQ_SXkMJLc5RNx64JT5Re6yxpuWD86s6kv82Yz0W1zlL9NoXGyPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: آیندهٔ ایران را مردم رقم خواهند زد
.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/453867" target="_blank">📅 16:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453866">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e45f1261a.mp4?token=qy3mZwX8ljDesOMXeci-GZ1x4X-wCJ283EQ9UrcmHs9bu-RmD6k_0j66w7SqESDZR-XPplKSki64I5jwRhnJZova4FmosW1Am25fKoSCu7Jy2eWOrpq1NMiVDYMwBo5FjmwZ1KsGNJbGs2ihUncLz01Tlg-95RsJqKlx0UQ3q7tiz4eGYYhqWh0YhFatnr91VhX5q5EoFvMA_p63_fw3fCdWPBbQ9oRTuSzlKkTpSzP2RoESOcaZjzoCHjW0oDOFv4w82xVUrC-MsMO5TV_GJwFjK5-NIovqcYLXwKUR4EcOg3u4HycK6gzlZEL35b2_kwuYLBqOFAdIHll03ZLtsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e45f1261a.mp4?token=qy3mZwX8ljDesOMXeci-GZ1x4X-wCJ283EQ9UrcmHs9bu-RmD6k_0j66w7SqESDZR-XPplKSki64I5jwRhnJZova4FmosW1Am25fKoSCu7Jy2eWOrpq1NMiVDYMwBo5FjmwZ1KsGNJbGs2ihUncLz01Tlg-95RsJqKlx0UQ3q7tiz4eGYYhqWh0YhFatnr91VhX5q5EoFvMA_p63_fw3fCdWPBbQ9oRTuSzlKkTpSzP2RoESOcaZjzoCHjW0oDOFv4w82xVUrC-MsMO5TV_GJwFjK5-NIovqcYLXwKUR4EcOg3u4HycK6gzlZEL35b2_kwuYLBqOFAdIHll03ZLtsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شاهنامه‌خوانی مهدیس، شهید ۷ ساله مدرسه میناب  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/453866" target="_blank">📅 16:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453856">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PQ9gVVmTQBt5pHVr6QNAG-zWKLdrakYTVr3WB5ZodJA5EzhbXHaOaH0omSjHM0qjWrTHkoDoM2-EOrkY4oIhLFVn_mNLKDEebKm8RQx_QdREwC_jlecHQIvhfYTFEKpUsdXvv08d3e5Pz32lu5E-6Si-9GJMyRbYjK3SLhD4RMb4wocJ-S2BCbB_Bve-G7CnstbRScvep7IxV5_dVdU2I-6VbQh76RORtOEA6WTh7yakFf3WzJLuPDSzK-G-FgQReds13wcP9p6kGe5i-XFQnuA4ypDR0mA_KwU-EnX2UFSuqxvf4QrMvbcm1uVADoMH3dVRPrNqGHAGxB-DpKPZeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZpvWrh3dQPhtXW-lPHMoNMj0EAZ5Wmyg7d9NOpjZGIOdLBW3czaxzqdg7vwD-8a2aO2q1MCIVx-GFEMewJQlxDjvQ1uMrxom9o7mPKKsDkb_wmgK10Ut9PPlQ2y3tgcoNbhp0e85GM-3Z1shjzBFOn6i7GdVm_fv7c9Nb_jLtfFbKHRIjQdrL2DlCweBxo-Cb-ep3Bz7mMnikwNtCCRFY7zDJ9X4IofNXnULpGcx2loIceR2iUHpigKifCjG_lHqY9tVYkCXMKN0kHgXHq_h9qz64oT46lFyHIV8QDQh5mbDIuoZuyOdrR7T-i6txTiX_B3xu8PvNb4L9jq8o4TNEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ENrXQ9AssSWxJb0XWYD1QDwBEfLw84MsulMm3Y87_HtFqvkXjByeuy1jaFX7kMMGCsFEo8VcWmfHqnlUBh8-Qh-fVERsSHtGoOTsYyuCVtCzr5PjpW58apCz2350U_xgreh52w7pM8WQ-hzYdHDoy83v-dwsCxUwkq_nT5vLws4fzwMu-OGZvShXQN2e_9EK96EeMRKgjnLCx8zdKCHVI0BUESgQzW5uSNDea-swXnGPUTDJGDNidRPH6JxUeRLB4XbGe0AYNIBixXmPwu5q6JeeyVWYhYPLMjiZwFHC_r-K_mOG3TFcU-jYbd9sfBpqiP6YyjPVgtZCTa_rKW6IbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tgKCAo_wKLbs8XMvgm8w9vqOKHBJhP03XpyeCIZ-Zuqwy4pRwiXIxVvNAGR6cGtiSalQ7hlE-BgVNOi79NdCo2ETjCx7WgeOLD_t0BxrNSLcx6e2GjFdXB0L12I1Z4oHOPsh9CmwRegvTiVB-cTEEAoK6Hqsv2vLN9KTF6pFKp59fC1NgEBBnLRm9d7mfa3djR3dDyQfOhR9U0nEJZIv3K2-mBuNNr6lnj4yyFWZ2QmjuyLqc3i6rHxh_PXSfczsYC3XmbEivvNVNWVKs-XJleJHJU9wjlj5aXHYPavtl44biu4DyLtlRseGr_lciPIHlP_krv-iVb1Yu0Oc6kgK4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mTnPy0bGfONjpOh8l0m5uPB0xEvoGtz2Tnz-PPK0SSXmB3Qr_0-i-wK9ePbsRvzn00lfKpMr0I8mmPgzDAdK0_9tCvNEyhDr3b4W_pqKB4YrnNU5fqVnfIhhJfwCfaguh1kKmNmxaoQCr-b1ULBz1nVtzVyV7ZmEzO7IsluzQKfhmYzHMZEBRaykaHfAlxqvo2zd4jhbooCkN79bDtHbQrsS6XSS98PLvNT5eCfZ_icEhkjrDn3JUkAXnwjEokf9gsG1w_10QPqJErwZUSIMpwKa29NgPDjR2XQe8KscvE-PknKqorI1KTtJNjAEOdhsHBOWocoohAAQoR_VIhud1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qd5wU95xySPbZ0Y0h-NEOm0-S1eGFqPEI1aPy4qcfQPYJqU8m9uQ-2I2PV_UJA9-kFth2dbY2_tHPGZ60Vy9WbpsLzHLL4vfPJdxAKUFuq_6alAYIW2smbRCjxZADl-P9Z-DqEoaG6Dhz3ANNsHAK7MXBGwWWKwHgPFlX2bxJ9oHzXYTaTT3-nkzSNYAJdhv8ABn-Bl1WN6m7P9piOrTWQrKrO0X30Ye4g3tl2_ydIexr07u2sFzIGFSjjYbOiUOg36XbooxJ8OAbQMqmOsPd2jZCqdQ79Fbb-t30QbBFZS_mAWXN1DiS6RlT08G1dFGmrFV9RhNPdv4T4tCbhmEQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rG0Z0cf1xCAxoQnYfyeAwYCAP8sCTP9jFc9Djs86fPxJXczK4CjanQOoJY1_hXL1bGnZrqCTbd9heVjB4qW1x2hJsC5xgrtikg9qM8SnkxotU_3tl1tHthdP_5KwsgpBeTy1rfbaDWh-C0u976qCSnECCiFQEM__SSA3-CBjLGMlf8A5rb-VI90i4E7sHY2UgdKBAbpAcMoNT-LJLJZ9WoxSMYGUDWAud9JTi4i4O9Cjnf7Z1GfAmBNdDxVFOwiEXI02bur7wMMwiufAIirJMSaDZCMMoFrhV6OfhvyFyBmKzHJVE0qPkGiQslhwJGLvqFB8tzkb7OAEIvJ-09NvWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RN7xKOH2BlONSWYEBvkzVS1HmhFg0OXW0xo4ZX4eUquP6MdzYTqekSQwIYZPLa6n9nPE9fLsiXostSZzlqLnJbj4CAOE3nT3U0LRHVsfb5CCrrx9AJJe3fOwDin-tFiDprjO8GDSYAHrNt3nDyRBGU5_UwJboiFQM1fOOCR81BtFp6Lc9sgCMrrDSbUeas_597phcldTOz4Udd2121klYXvX8FNZa2lA8-76F2uDHLzli9Z72BOF2a6VSMvDKmauFE7o_Qd0TXfYDLam86U5W-nXD5j3epIVLoRMaXf6j2ADbRFxZPc8nPib2YdQ_pGVPrWHxczSq6VoM7XuW-cY_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHPWy6EbyXIP0gck0EtbkoTA9kHOaoukwRT3AEmgfEE_QndEDccjRrOaIoc3M4YZ-bvnw-DSiNB94KQhk2DkP8Oz2wR3f3E76iGv5xa4OAqCz9u3tF6jTtJJLTWJ0Wc4lC2ycfZJter1ltxpCL-tkOClWOSNuLvZzBkK74DYm2rP8qQCXMocSQXNMbTasaeeLUl40iWveAKzaW_60_lGaqlBZ_OSZolh9nKlW-LJf3Gam1NTD7SMDeyjY4gmSvyWgsfXKGO6-N8Oz4y23Z__wh6fvqU8blu0hb0ieCAc-fLXkaFdqG3HxrYUQ4I014ecrefF1gtYmB_UySVBYbCYxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gTCC1QFSS2BW4aXs3eY5EmBk4xS6kC_yxpKK_dBQvDfZWzxhUJo_ZP3edF7BcjHPPoAVR53dFEByyD5Tjzci6XL6AUKp4irGcULBPUHr6TtWztOoI6pSjqcwHJuO_qWkUNiWvmvqd6XFVMe-2Tbdox315ApQZ8i_0CLducXoDQW0wqUbievqtpDsN-GsLYATK_23U9AL6Yc4jMI8mELfIwQ2Z9mcje04VkjDGpHFH6s_QLqFKRbaPR9xg7VfLljdaX49b-eR60LOh50cuy9F31CBLTBOcSMYZbk6P-FjdqcXyAEdBPTT3vobJFWg6lFTJyCu4uZUhSnxKg8Ssnl3dA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
راهپیمایی زائران اربعین به یاد آقای شهید ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/453856" target="_blank">📅 16:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453855">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42e469cb3.mp4?token=XGk-76qQVZZss42U6_goZ6mKGHxDXiWIVYDLxr64DzqhyBEYaqPvLis_JoKb6A3ld-IkPnjyzurcztWYERxY-HHc8yCDNNgytXglJ7jKLGHjnNG0oRdvXYjFv1WPILj9CDSh84X_YNm8W_euXr9bpqjXYTMFbSreXX_4drMxAgMKC0V4Hk6NeCWL6aqOtHN-ORahk2WCdWL6vyjgUiNO-6uqYrnAMHJtyu8wMCL1xVTrYK0OtICIPYUUh3JfBvmWc4JpLz3eAxZ5Ur1-0cjWAcBF4PjgCg8wC-o2Ng4lddubb94vNQM8E0ieRTIzvda-sukqjxH9UuT9DdsWlypSmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42e469cb3.mp4?token=XGk-76qQVZZss42U6_goZ6mKGHxDXiWIVYDLxr64DzqhyBEYaqPvLis_JoKb6A3ld-IkPnjyzurcztWYERxY-HHc8yCDNNgytXglJ7jKLGHjnNG0oRdvXYjFv1WPILj9CDSh84X_YNm8W_euXr9bpqjXYTMFbSreXX_4drMxAgMKC0V4Hk6NeCWL6aqOtHN-ORahk2WCdWL6vyjgUiNO-6uqYrnAMHJtyu8wMCL1xVTrYK0OtICIPYUUh3JfBvmWc4JpLz3eAxZ5Ur1-0cjWAcBF4PjgCg8wC-o2Ng4lddubb94vNQM8E0ieRTIzvda-sukqjxH9UuT9DdsWlypSmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصویری از پیکر شهید ۲ سالۀ جنایت آمریکا در قشم
🔹
سینا جعفری به‌همراه پدر و مادرش بامداد امروز در حملۀ آمریکای جنایتکار به قشم آسمانی شدند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/453855" target="_blank">📅 16:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453854">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_zCU1KjWjG1dl4ER7KnDbTk_ePtXEbTTlcDT0Bo4Bdboy1B8z_5DNo_y3Vg9RDREp-dv5qTHyqwJu1JwLSsgF0My69eLvrZBUR5oG_ctvZutb-tcjKEAF5LqbOeWPDcdOK7P6aHqhcC61d2Ezge9S1nzSQ03fEJ4TCGhSq57wrjArc-r-sgn0gas3TnyroZ0PmwYqphf4hNfgqxcp70Pyudzz_KIxPmnTotchilS6Np46ZxF-hcxgliObPWWQ8J_UiYHR8nJbBUnidR7DU_utXqORKgU3Y1tgApyCOUvvfI8fcvo7NyIQoXuJDukUxMjE95eAeS4Ar7IyekybEqHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
تأکید مدیرعامل ایرانسل بر تبدیل مدل‌های سنتی به شراکت راهبردی با تأمین‌کنندگان
🔸
همایش «تقویت شراکت راهبردی با تأمین‌کنندگان ایرانسل برای خلق ارزش مشترک»، هشتم مرداد، با هدف تحکیم ارتباط با تأمین‌کنندگان داخلی، تأکید بر تقویت تولید داخل، گفت‌وگو و شنیدن بی‌واسطه دغدغه‌های شرکت‌های همکار، با حضور مدیرعامل، معاونان، مدیران ارشد و جمعی از مدیران شرکت‌های پیمانکار و تأمین‌کنندگان ایرانسل، در مرکز همایش‌های ساختمان مرکزی ایرانسل برگزار شد.
🔸
مدیرعامل ایرانسل در این رویداد، بر تغییر نگاه از رابطه سنتی کارفرما و پیمانکار به شراکت راهبردی تأکید کرد و گفت همکاری باید برای هر دو طرف ارزش‌آفرین، حرفه‌ای و سودآور باشد تا به توسعه پایدار و ارتقای کیفیت خدمات منجر شود.
🔸
سلیمانیان اعتمادسازی، تسریع در اجرای پروژه‌ها و شفافیت در تعامل با تأمین‌کنندگان را از اولویت‌های ایرانسل برشمرد و با اشاره به شرایط اقتصادی و افزایش هزینه‌های صنعت ارتباطات، بر اصلاح فرایندها، کاهش بروکراسی و تقویت ظرفیت سرمایه‌گذاری برای توسعه زیرساخت‌های ارتباطی تأکید کرد.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/453854" target="_blank">📅 16:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453853">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c664582a4d.mp4?token=aq07bcKvRT_PScSIpwPlLDvAbbdAfzfY3UaRi2hYznok7fXuFgWppyW6TgGoFpfHNckG9dcj4iEehvMLqoxm1tzqZgNxoiWi6WDFsSaZMzoWUkYsY47X8fx7eMb9YzuLC5S6Pvp3MOpPQNXM35A2TRbUCCzuzK7IH9PISM07SvaIN049rmGyZV7SFtyhPY3G3fQd257b-5wtM-mMNr3yYZ0zWig0OkmqiuJDNd5sr30MjRdRNrN4I-fam34uUpAneI63VgQ8oGAdalQj4VSZHt7FAzP_VBRExxNuPYkYLzjmRBbEhw0CL5v8ghOeMYDrxzlieUZfVZ19fbnFGu5QaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c664582a4d.mp4?token=aq07bcKvRT_PScSIpwPlLDvAbbdAfzfY3UaRi2hYznok7fXuFgWppyW6TgGoFpfHNckG9dcj4iEehvMLqoxm1tzqZgNxoiWi6WDFsSaZMzoWUkYsY47X8fx7eMb9YzuLC5S6Pvp3MOpPQNXM35A2TRbUCCzuzK7IH9PISM07SvaIN049rmGyZV7SFtyhPY3G3fQd257b-5wtM-mMNr3yYZ0zWig0OkmqiuJDNd5sr30MjRdRNrN4I-fam34uUpAneI63VgQ8oGAdalQj4VSZHt7FAzP_VBRExxNuPYkYLzjmRBbEhw0CL5v8ghOeMYDrxzlieUZfVZ19fbnFGu5QaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
#تماشاکنید
🔄
خدمات جامع چک در همراه بانک تجارت
✅
از رصد چک‌های وصولی و چک‌های صادره تا مشاهده زنجیره واگذاری چک‌ها،
همه چیز در اختیار شماست.
📱
همراه بانک تجارت، ابزاری کارآمد برای شفافیت و اطمینان در معاملات
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/453853" target="_blank">📅 16:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453852">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/453852" target="_blank">📅 16:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453851">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b36Q3JL8FExdDU2yXw0_GrRD9XsUuash4qJbuYjDTkg-wM--jKx5yJi-RnlbCj3dyW6sXzE8w7r439wnaxlyPFeMWrbbh1usmYpY4wOs-ZHof3rUbT2JUMN2IbYZrFfmVwv5ImdfnqixWN1w0cqVeEXziDtIcqcMkx-fFufz6k_IGCu_18U06gHHK4_aQqeXYYu1a-R8gxJnoe7h37DApR2X8ax7exH5-QzMVrtTnVlfQZfyiVqYB84pIu5Xoxe3s6dLR-SRL6S8-OQuE-SHGf503RgFDplrCNnp301jI5wCjumUlK3r3cr5qy4u_M6t7ynSwqDvtee7CczixrSD6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ نگرانی سناتور آمریکایی از جنگ با ایران
🔹
در نشست بررسی بودجۀ تکمیلی وزارت جنگ آمریکا، «جف مارکلی» سناتور دموکرات، در تشریح پیامدهای احتمالی جنگ با ایران، گفت: ایران می‌تواند علی‌رغم ادعای نابودی نیروی دریایی، تنگه هرمز را ببندد. ایران توانایی حمله به سراسر خاورمیانه را دارد.
🔹
او همچنین گفته: در صورت وقوع جنگ، مواضع تندروها تقویت و اصلاح‌طلبان تضعیف خواهند شد.
🔹
یکی از ایده‌های اصلی جریان اصلاحات، حل اختلافات با آمریکا از مسیر مذاکره و تنش‌زدایی است. اما در سال‌های اخیر، هر دو جنگ آمریکا علیه ایران، درحالی رخ داده که در دولت اصلاح‌طلب مذاکرات میان دو طرف در جریان بوده و حتی ایران در موضوع هسته‌ای نیز امتیازاتی را پذیرفته بود.
🔹
بنابراین، جنگ با نشان‌دادن ناکارآمدی ایدۀ محوری اصلاح‌طلبان، آن را تضعیف می‌کند.
🖼
اما چرا مقامات آمریکایی نگران تضعیف اصلاح‌طلبان شده‌اند؟
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/453851" target="_blank">📅 16:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453850">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQxXSDIohrrq83Z501erWogaUrjKY7o2_fkjYMgIrzKmrRkGA5JcjuWgAXl5ojCNEEb5POL2HrEJJ4ViBNkT4loP5y4yxTTh6mxAyVS5yOV7untJ_zA1CwZ5Qk1AfGe1-ZXrN2hw1HJkTr6CA6NALteVajVPsVTih3EpoS9wPP3eAtXniQCk2kz04L0_DCipwT7nIKpXeFXEtVFnGVefCPLbA9AFblctCMIhIyQQj2GCLWS6053h7qHqkSIGJ7j2AAI2Z_yGOHv23N-ynbknQZCv14dg5JeCxDsyNX_-QIoSBn0T9RWMyuwwO8TJHALvUD968GVZoLp7dBqOiRkGaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عارف: افزایش نرخ ارز به سرعت در قیمت کالاها اثر می‌گذارد، اما با کاهش نرخ ارز، قیمت‌ها متناسب با آن کاهش نمی‌یابد و این روند باید اصلاح شود.  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/453850" target="_blank">📅 15:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453849">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ab26368ef.mp4?token=LgxaCoaqrmYteQYWWc45Rb4UW_C9WPNPp5vhwW4EW6CC8hXbmWMWKLojm6dFxS6d56h3fsV49m08oJ5IuX18qkq_SjAdTCcBIcckfsys_Fw99wxXF4sLfb60bbbeZvS0FCSc-G2YwGouEL_BATGzH7LUuBd_phAzFBu23mmlvO70lvZVJlOK5EfJAaEeu8bOzwuqGi63VtRmgiI0xgL6Hc146WpwpFZuBZ-rdweXqGbpvo9jl9GPvGyp1KyT6db8cY5kcfQhyvxIDkPoC5Cjs8VWQmqZoJQIX4vHO16OU859RwB7MndQjBswXeVr0V_11IFe5ED-f1e7aqsVRYtRlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ab26368ef.mp4?token=LgxaCoaqrmYteQYWWc45Rb4UW_C9WPNPp5vhwW4EW6CC8hXbmWMWKLojm6dFxS6d56h3fsV49m08oJ5IuX18qkq_SjAdTCcBIcckfsys_Fw99wxXF4sLfb60bbbeZvS0FCSc-G2YwGouEL_BATGzH7LUuBd_phAzFBu23mmlvO70lvZVJlOK5EfJAaEeu8bOzwuqGi63VtRmgiI0xgL6Hc146WpwpFZuBZ-rdweXqGbpvo9jl9GPvGyp1KyT6db8cY5kcfQhyvxIDkPoC5Cjs8VWQmqZoJQIX4vHO16OU859RwB7MndQjBswXeVr0V_11IFe5ED-f1e7aqsVRYtRlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلب تپندۀ پتروشیمی‌ها کمتر از ۳ماه به مدار بازگشت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/453849" target="_blank">📅 15:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453848">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-WbKjE6CV84DTS2-Mmss_7-xUkQBsnILV6Pdhhcj98Gd0tf67mMvWhojV97K7_K7KnvkI5k9xIOsBSVQWofFf2dgZaUj6Bltms-HeWH1PrIwbTKjBwc8t8m1VrC3OkEFnalCC-yojRzv62myD5Q5TNMKwog06cO2OYlzJuoWyPeBYaNGUxR_gGOA2ci8wiriHK4kzbw2U9o1O7p-GdDUofsUvBMRiDVugsgFp5MNn17lLNlzjRHjv4wmkSln2pyLHt0axKUBWc02NLjpdLg6H9JijhYsqIWMBXPty45Q95rTs3gBov6tWEhJEPntHtI3QeRzx9zc2DHhBq-4yUFqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
زیارت اربعین جلوه‌ای از «حُبُّ‌ الحسین یَجمَعُنا»
🔸
تصویری از حضور رهبر معظم انقلاب در زیارت اربعین ۱۴۰۳
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/453848" target="_blank">📅 15:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453847">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca485d3e1.mp4?token=oI50lj6-pl1GMs4-LhhPGXN9-FqvbX3tDpgqfr29_5q5zddo9Xzw-YdDp4BSbn-SmGdeTqNgm1plhyJzU_gjBqiGacuCHfzjxFHNCyItoPfTNTZYRSifmc7FMppvrMRr4c9r7IndFno9ZCvcLkzVzgGbHE_ewt2YTI1cm-3fBMyeFndqQ8H6s27erLKWJrwLMVmlqLIZX0O7EJjRwxB6ckF-qnCMia_Cc2JH_LucwDMDbeFSF_x5oGFcjS7e9ZzfjYdHHDbN9BycXgByyrLUEEMqxT4ofkef2ehe_cpkeOnXZdLcen4eKBPlfs-p_lCZ2tOvO3CGVKd4JxNVAMO_kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca485d3e1.mp4?token=oI50lj6-pl1GMs4-LhhPGXN9-FqvbX3tDpgqfr29_5q5zddo9Xzw-YdDp4BSbn-SmGdeTqNgm1plhyJzU_gjBqiGacuCHfzjxFHNCyItoPfTNTZYRSifmc7FMppvrMRr4c9r7IndFno9ZCvcLkzVzgGbHE_ewt2YTI1cm-3fBMyeFndqQ8H6s27erLKWJrwLMVmlqLIZX0O7EJjRwxB6ckF-qnCMia_Cc2JH_LucwDMDbeFSF_x5oGFcjS7e9ZzfjYdHHDbN9BycXgByyrLUEEMqxT4ofkef2ehe_cpkeOnXZdLcen4eKBPlfs-p_lCZ2tOvO3CGVKd4JxNVAMO_kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام موسوی‌مطلق: تشییع رهبر شهید در عراق، بی‌نظیرترین بدرقه تاریخ عراق و بلکه تاریخ اسلام بود
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/453847" target="_blank">📅 14:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453846">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZ1XU7J1A4pGfqRYyqvWqcf2APjqSWfxenrcztXoUQt8ldUPcw47jZHS5WKI6R58HAqwHIoHuXe6mbUS1on62i1s-BeJ4FSFsZiOXfeGiG6mCoa_xCOY_8Vr73StKaPC3QA1maDCvmDdB7TuLW6E8VxzQ2bpJjR4kJWT_JAsM9QCK-mAlDkwgoVzZgshU4-JNJlrVMQnIe2CqlBbnZg7L1ZRVzApo_e6JIADLqk77K68h9of5OsFfiWx49hwo_QBFxM0h8tjfam8KmsaFIMeMstzuvwNNjpl0yCsSqJ4_zz64b4_WcEUo5H1Vk3YqwCa8XA-ngb3R5gfF57Rmhzv1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلاکت پدافند هوایی اوکراین، فقط یک بالستیک شکار شد
🔹
رئیس‌جمهور اوکراین امروز با اذعان به اینکه پدافند هوایی اوکراین در جریان حمله گسترده شب گذشته روسیه تنها موفق به رهگیری یک موشک بالستیک شد، بار دیگر از متحدان کی‌یف خواست برای تقویت سامانه‌های دفاع هوایی، کمک‌های فوری در اختیار اوکراین قرار دهند.
🔹
به گفته ولودیمیر زلنسکی، نیروهای روسیه در جریان حمله شبانه، ۳۵ موشک از جمله ۲۷ موشک بالستیک و ۱۸۵ پهپاد تهاجمی از انواع مختلف را به سوی اوکراین شلیک کردند که کی‌یف هدف اصلی این حملات بود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/453846" target="_blank">📅 14:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453845">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85d89446ce.mp4?token=eFgNWveJl6ZF9ZwQT5vpUUlv_pUwEeXsQkPFHFcbFGcK5fFfWa8tF_ub7-XJOacFvsnqDWiXB2Nl5z_5QEGSZ5UIBPEM1WS06I9vmjQYCD9GIP-iFdGfx1klVvhB94tNA7GxjXLJ4C1piGej46PKexRr0gXjpaoOIJ6dY5dObDUSzSRfMQ67ljRF5JEdO_ABnC9U4tbL8kzdC6Jw2hIPSVWN0c1V1HO2FArsDM-smZLzSqCWPLjEO6vBdPLNsn_8Wx2bs1HKd8cOC0uvN9zJDr536eGWBeqeVzVU0Vd7Wb_NjbXfxL6dzgHiP7hm-lRAH4aGr0ejDYp4bf0Cw9J_wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85d89446ce.mp4?token=eFgNWveJl6ZF9ZwQT5vpUUlv_pUwEeXsQkPFHFcbFGcK5fFfWa8tF_ub7-XJOacFvsnqDWiXB2Nl5z_5QEGSZ5UIBPEM1WS06I9vmjQYCD9GIP-iFdGfx1klVvhB94tNA7GxjXLJ4C1piGej46PKexRr0gXjpaoOIJ6dY5dObDUSzSRfMQ67ljRF5JEdO_ABnC9U4tbL8kzdC6Jw2hIPSVWN0c1V1HO2FArsDM-smZLzSqCWPLjEO6vBdPLNsn_8Wx2bs1HKd8cOC0uvN9zJDr536eGWBeqeVzVU0Vd7Wb_NjbXfxL6dzgHiP7hm-lRAH4aGr0ejDYp4bf0Cw9J_wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عارف: افزایش نرخ ارز به سرعت در قیمت کالاها اثر می‌گذارد، اما با کاهش نرخ ارز، قیمت‌ها متناسب با آن کاهش نمی‌یابد و این روند باید اصلاح شود.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/453845" target="_blank">📅 14:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453844">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب کرمانشاه
🔹
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست. @Farsna - Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/453844" target="_blank">📅 14:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453843">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde6d95b25.mp4?token=bFgt5j88scSXKxgiS065eNMzFaZC14XFC-6h-kLV7O0PM-M0t8Oj1TpHgXzPq91lnTpHG8dJklclVwJ9PUBpRne82U8SNaqDqiGAPHKHnFcPiEmvk7DR_Iz2GIhKwT17-DBIFzw6JPzH5OoWhA1cCHHsvq7muhds7VvpWrGDXadqj_t0yuP1iUkIZJ-QywYfMeFmU9eZC9ShrikzWqN4O3xkCS8ZEmN1dWR5lwDT9mPGt1_arh1_NkWREg8HMvW3bUP6C7eW5kQp6MtVYUu9ufttHgQCWiZCeGxhx29eDi8677Fe60jvhk6Y4yNr15if27dZlPtyweMInDRqiPWYLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde6d95b25.mp4?token=bFgt5j88scSXKxgiS065eNMzFaZC14XFC-6h-kLV7O0PM-M0t8Oj1TpHgXzPq91lnTpHG8dJklclVwJ9PUBpRne82U8SNaqDqiGAPHKHnFcPiEmvk7DR_Iz2GIhKwT17-DBIFzw6JPzH5OoWhA1cCHHsvq7muhds7VvpWrGDXadqj_t0yuP1iUkIZJ-QywYfMeFmU9eZC9ShrikzWqN4O3xkCS8ZEmN1dWR5lwDT9mPGt1_arh1_NkWREg8HMvW3bUP6C7eW5kQp6MtVYUu9ufttHgQCWiZCeGxhx29eDi8677Fe60jvhk6Y4yNr15if27dZlPtyweMInDRqiPWYLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردِ تنگۀ هرمز کیست؟
🔹
تصاویری از شناور متخلفی که در آتش اعتماد به آمریکایی‌ها در تنگۀ هرمز درحال سوختن است.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/453843" target="_blank">📅 14:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453842">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب کرمانشاه
🔹
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/453842" target="_blank">📅 13:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453841">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vF4sd0Mdluv0VpI7E9wU55v9ROZh9b5umrPNmbyMqlTDkEnpXw2ScoG_0lizcny7S9TZ0ZMBKSa4Cl9CSroiINocv561r3KKoHhHq08LYLSzWr293omJBsVJ8K1LLnmnfqe9dDE_bmy3rBbCorAWw0zJMNwhlKxSGeya54CI_qoBePdc4brcb-M7KcZowbFicqzDgLHq51uxeWOBV85uJ7KkiLIiZcVImymKqOg0TpwKVYk-KZT8JEeQSV3oM1LlOyA9btU5kAI7nLGYYfc1yVHQ9s2bTeUBNSbu3yt78NKn876l7BnxpEfYmFeg2xRhRZkpL5J3zpwjtf2NGOFwzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
جزئیات بازداشت عامل انتشار لایو ضرب‌وجرح دختر جوان  @Farsna - Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/453841" target="_blank">📅 13:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453840">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDkNZ1hwjkdboz8bc7QAqFeHrbJEJcsF1F7RusN-m38kO9IUwBoT05-s-4fVi9IsUPcklB_PM_YUN_EekpEkFfJr6LMH3XiqtAQhzssn1M2ejjiEKs87Xur-5JB_2G6m9Fj7QqWD2mHMUcvboBPS3Fmap5QdUnrWGSwhaJuTNZPM5n1J5YcQ9Pc9UcPp_hLdCm2OmTjSoyEMCKPb8uupvqJ_LnghGWZ80mrDlkpTx-VRCtn0mRh5PUjcR6eQ2V-_1N9BT4iaQjAXfDmsVzYEH_lipB-Ny09FPO5ypaHSivD-pnSbRpA4e5DcMhP7b6jywkWHtf9fDRuuWG9SM60bGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قشقاوی: بررسی طرح مدیریت تنگۀ هرمز در کمیسیون امنیت ملی آغاز شد
🔹
سخنگوی کمیسیون امنیت ملی مجلس: محور اصلی بررسی‌های طرح، حفظ منافع ملی و تأمین امنیت ملی کشور است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/453840" target="_blank">📅 13:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453839">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ffa6b3220.mp4?token=AM9zWh34nJE7SAiobiQAC4m1Qher6cdA3XkgF4lZgtHcQM-eTEVXxq9_lU8iJ_UanStKGtlggGqqhF-cEh7R9mAV4Hk5ruB1VHvPcx756Zj2eFm8eQktHKWftGdJ28opuaYK4F-iI76z4Ahf4m9C9K9X7o0q1KawofGdLa_aXE6XhlAmtr4png8t1V9CghZLJoF3jz0KPIgWqgtAROAXMNRjeyZQrVD5a_Qt43ArxN-hqYCPTRJKzgrZSbThrCIueWnadVnr_iAmF0WQF-wrk9yz-nfXtY0on6AtJTKuUdNaqm2xUOPfvHL6TeKTAMKOrCHEdbyp7pM-l0nXaEUsSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ffa6b3220.mp4?token=AM9zWh34nJE7SAiobiQAC4m1Qher6cdA3XkgF4lZgtHcQM-eTEVXxq9_lU8iJ_UanStKGtlggGqqhF-cEh7R9mAV4Hk5ruB1VHvPcx756Zj2eFm8eQktHKWftGdJ28opuaYK4F-iI76z4Ahf4m9C9K9X7o0q1KawofGdLa_aXE6XhlAmtr4png8t1V9CghZLJoF3jz0KPIgWqgtAROAXMNRjeyZQrVD5a_Qt43ArxN-hqYCPTRJKzgrZSbThrCIueWnadVnr_iAmF0WQF-wrk9yz-nfXtY0on6AtJTKuUdNaqm2xUOPfvHL6TeKTAMKOrCHEdbyp7pM-l0nXaEUsSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع عراقی تصاویری از آتش‌سوزی گسترده و بلندشدن ستون دود در یک پالایشگاه نفت در اربیل منتشر کردند
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/453839" target="_blank">📅 13:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453838">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار اصفهان</strong></div>
<div class="tg-text">🎥
باند حرفه‌ای ربایندگان طلافروش در اصفهان متلاشی شد
🔹
فرمانده انتظامی اصفهان: در پی وقوع سرقت همراه با آدم‌ربایی، ۴ نفر از عاملان اصلی سرقت و آدم‌ربایی به‌همراه یک مالخر اموال مسروقه دستگیر شدند.
🔹
در بازرسی از مخفیگاه متهمان، یک قبضه سلاح شکاری وینچستر، یک قبضه کلت کمری، ۳۴ فشنگ جنگی و بخشی از اموال مرتبط با پرونده کشف و ضبط شد.
@isffarsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/453838" target="_blank">📅 13:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453831">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mv5D5nTmV1KjsxneBPt-KIsZpnBb-JxoRpy_uRZnbNCwOwIyv9bRFb2zmlor0eLdzGuEYThphiFRVhQWEfrXAcWNwj-dqMz8LfiflpjR8fPGiGarCJ157B5Zp8JzbcHg4fztqxQCBLyyMYwp66Eshmsvhe6NAg7zc0cQ3gOgCRBOWqAyJEPI55OjuTBcx1kY1xKvYWfGUgAy6xLzcJdb82c6cFBhN2qeAhnz_Z2qhBa70Cpo2Rkl8yZxdwsd_RWtfELHo1-5ZmvATAI4kwEjd_ze1hCEhIo9uTPaH2iaP7t2sREPNg5jnTouIuv55uF8dqIOkKiaREMXijBBwTnKQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lDvutuRca8eGs-PB_VWyDxp-5z2HXPrLKBk17KnwYHK3I0RXHkk8FtmzbQlBoKN1kwgWBgVJHtK9l1gTNVRNYLl3GkPxBE3J7U8IEH6fAOWU7wV8qYx2JH8jEuuMTeBn7Jb-_QJRRIV6G988OHKKkRWGz6dhgT1d8bnnrKsR6XRUos9P4sfwzRZ0uhluJGs5rmoSRMLsxD8Ce7e_doJtn1zRW86qp79ULXacg7gQGdIuTEhny25QwMD1sMndAy3zWlBH_SC5A6tWN7NYiodcEBu9Ti_w0M7DR5JU_PiqfUK0tWkLi6ojXYWKzo9pFIVFRGd6diQ0awpmlB79Iqp9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rLDnuApLq8raMftDbRVZWXzMwKz57iP-V-d1--ZeNAIs0_KKhyDzPH47uQTo7mFePd8zKGBbtAEgCmEryFVWhot0mFXhP0UzmsD7dzmsYKGec8UrM-yjjO1gQKUiSAuVeeS0qB8R0mONKkACMhJA_ZkSBb8HMOojoexAMHiZVRPql0cYbdfFUUdiBBjv-d1iR5zCTVgpibYH0V6_0iNDudjPKJY9Gta-KoIj7yojygYZ4GcROm_Q4aTVI1rdaNluTD3Ncx5uGeqJDGte6F7fYnRCUUPcaJa2BvqewyHCwXT1fpkJKSMqCrCyz7F7mHAXJNd2eLmQcdwiZM3iki_Cjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xc45aO7409_Jv7J10H-EwNaCxhfeJZgm38fNjYTavBr7Roqfx4CEm8hkcibWfRFrj4vMoiUvAQLmlusmueUxaaT4_oN2YG4ERM4al3PACF_6mtQAwECkf8eIIUmXlHkwAfPwN0fvNxa4W83nguz3Dmh3EP54GXSlfhKU4o3BionXfNHN-71rtUJv08u8ADy-bDT6pqWzqwjJPJVrXlA7hjlNy5GRQ3ZD5VG9OOkdiQmlLzEG-S-hhQfZj-2dDNNC_2XjlOPyV6S1YScfcCx3-s_64AotKn7QR6q7hrEAdtA0UrialiglKZWX0n2yfcrfv5g7pXnZHTVsBQqA__iL_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V4-5FTO-fmDBIOv-kPMj8pyDCTyA_X02Z0lfEqUDRAbnnWg-FeuiS8O0BynqG-gwkvexVEVYA0SF_4TNtohemBiYll-R0KWZNnHDJEOZKHBkyjiZQU9Z_o5xgjBQBT9FWsB8wdpwPZrIXuHgQDxkofEaYhfKw5-JvLsaxJmkAwCpJ1owZD6jTSVg16wWmOzGDvvyFepmIjC57w3e6hHmn5zcYgOJ8IU_KmoO_HTCdLs9l0FhWb1XeVu0Kgn2AfTfj2p_bTKJmTlPU4BX--8CBaFuEzBt7Hd2CJvkwCz6oJ5dSgfxB5DTQ8WCL9RxIi9edpeFvv6AIsBVLH0Vz3VV2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jb0QDamUGvtEfeMrj3V0USjLib0szBiCj95EwkDQ14CdGt5ayGaMsXDv1RVE1akhkIhIn0PypDbS9-T6UJW72AwmUKm2dU0pXMUiv_G361s5_0Ms1ByqjJYsjuXfN3AP5mzInOucJGheQnPoRuh83zqRUuWgGVz_0gpEm514s-jYuVlW8HQaCOkRxi3qCzNtbDEfuNUQSDygDdw2-KL0dZQiOj28ElQcgfdFn_BUVnWgv_EFLKcmrYXGkaTkb_sqIfpGnYFz74jHNmzhiv2cSzG-rK8_NypQdpuL9QwEP3slZZZbU8J8-jBUpnQNiGRuVTRbPhrtLxoEhfTU_FBY-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIl4_D80T2PEGGMFm69Apj05cdLRNpnzA41Aw3x-MP35-HEjt_Ur8kA35KfDNu9hRIvfZWOB-lvGzm_xV1Utzb999WL7Vfc-ShppPB9EMkEwIolAn2ZUxgYp2fkwCzpltmS656GNctWvdsbf0REvY-GmOpWx4C748lvqLhXwaWR_jkJ8wJLNFxJ_xIea0T4CQ2riogz85QSjdXS8XcQVtA6RPOliCAXkTk0nGecgIv2ZtHqdxlwKQ6XrXgl73zXCIO_BI7RD4JupvOc_2axLOAa2kHrVaMDJKRkwSVEuMUWQKybqZ9l8rlnO6UcnLxNyLo5wDB6lSCf5UBFRLhPadg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اردوی تیم‌ ملی ترامپولین در همدان
عکس:
امیرحسین ترکمن
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/453831" target="_blank">📅 12:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453830">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSVpmz83t4fHPlO6B1h1K6Z6Kgnw_Y2EtvvVYkYn-VoLaofk4kCFsUHsvZyuvIXgpJorAPz6sX62uKhPKZtDf28fwWZu_s5NG2a2yaKwqVrmevKV1FBhMDOOT7DLZ6ym2L0mx05iGXT2-v3AdViAdR533FnLUdG5dFiQ4ZQ9dXqdWI8cBDRJen9GBk3E1W-B1laN-Tk7_HkntfvwsiT3JeK5na-vGmdCSzW3G4jPUEi75OvdhlTL-BE0w5285XT3FkqO3FmwuIy6VjqqRcyeCFqzmfjs0yuIlhHUzOK_-7BrtF-pGQIBqjN8viU0hZd-NTRhHdqxdLvcT8ne1OI_Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
جدیدترین تصاویر ماهواره‌ای از خسارت یمنی‌ها به تأسیسات ینبع عربستان
🔹
تصاویر ماهواره‌ای نشان می‌دهد مخازن تحت فشار ینبع همچنان در آتش می‌سوزد و حدود ۲۵۰ هزار بشکه در روز دیگر از ظرفیت تولید از مدار خارج خواهد شد.
🔸
نیروهای مسلح یمن بامداد شنبه تأسیسات آرامکو…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/453830" target="_blank">📅 12:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453829">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0H1NfX4x_NBjhhJQQ7FxEU-8utmbNGl1oAJPwNFsNqUuoDQOZrOt7l7L9pDO7NNudqqBTxqk5XDikm-0-3VkCj1szZIv6YYZzA2KmhYanbqU8XII_-w8OZ9HIJ_28SEmqg0iIUrnDPJUGfawEdBHmRAh_-1-Qmi1gAHcQ3eKPMjWKh42L0aSH_Q_4SrdnkIiWVAJDy3Rya8DPhwmSKYMcxKSC_YYT-tt20PBgJOr6IR5-3c35LR7Oph_H82mYlaSed8cIoYPZ0UeumvZ7LJkJUmBqgzwlUughK8cRWc9YP4qMc1m_HZVeN7NhVXBKrg4YuhJr09wbj3J3LG4yvMRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با کاهش ۲۰ هزار واحدی به ۵ میلیون و ۵۵ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/453829" target="_blank">📅 12:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453828">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mftouGBosYJxu60Gb5ej1JkyjxmDKyQToxlijxRsPVTB0CAWE1acumqnhDeXHgHSpWv92Q1AQGhi9Kr8J8v3JH0M9YUSM8W94YL9ygAWmxbtnz5ohvJ4QJ-ETlngD5AsNtDqANk7_S1J37ZKSjYzWiKsdi45M_V3BRBslBRypoGw__QkKBkCMtAfRpzhldrZxwanS2CAYMRU0TB1jXYF_3Gv0RGP4TCD--EDOUO0Cvv5JogxZB_dejYbXgPkU638gKYSrF0rKC4TipsjGawn-p-eCIJNU7p-UTrclUmHzODqsJHIUjy_fCE80Q77Ws-RY49Zt10kUqriSQh9TVufXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارت آمریکا در اردن: آمریکایی‌ها برای بسته‌شدن حریم هوایی آماده باشند!
🔹
سفارت آمریکا در اردن، در اطلاعیه‌ای دربارهٔ «احتمال تشدید تنش‌های پیش‌بینی نشده» در غرب آسیا وجود هشدار داد.
🔹
این سفارتخانه افزود: «آمریکایی‌های حاضر در خاورمیانه باید برای لغو پروازها، بسته‌شدن دوره‌ای حریم هوایی و اختلالات احتمالی سفر آماده باشند.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/453828" target="_blank">📅 12:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453827">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iU26YigLgl_8y8oS4kmGgLw8S1m6JQlZ06nXqqXxA_vLCfDNHgwgON83_5WaKbVocmowhMnt_OsWFhasMWOa--SI6vSGXyQx8ylgJUUtppZOACHxldRRAOOVG1ELmfTabp4noBmOcOVKQPmejqYfcfhPNeg9Z8fBStav6WPWZirHmfPFKA23S3l_IB9VHUwKF_QxSeZiGFb1L0UEXeYY5tWNjzw6bF_6Uj66X-cfA5NHaIXkNXCt-3ijE0e9iMeDmNB0L25OY91Auzz2yyAIb5BldXRNuuyp9Xt5s2_wpuilcVBxGJehpuupnjCENgRMQUNS0AJSTlheKRtumXwhKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی ترمز سود دلاری یک بانک دولتی را کشید
🔹
بانک تجارت ۱۰ هزار میلیارد تومان از سودی را که از افزایش نرخ ارز در صورت‌های مالی خود ثبت کرده بود، با تذکر بانک‌مرکزی حذف کرد.
🔹
طبق نامۀ همتی به سازمان بورس، بانک‌مرکزی برگزاری مجمع عمومی بانک را نیز منوط به اعمال این اصلاحات کرده بود.
🔸
بانک‌مرکزی اردیبهشت‌ماه با ابلاغ دستورالعملی به بانک‌ها اعلام کرد که اگر وصول مطالبات ارزی یک بانک با ابهام روبه‌رو باشد یا بانک به دارایی ارزی خود دسترسی نداشته باشد نباید با افزایش نرخ ارز از آن سود شناسایی کند.
🔹
با این حال بررسی توضیحات حسابرس در صورت‌های مالی بانک تجارت نشان می‌دهد بخش مهمی از سودی که بانک از افزایش نرخ ارز ثبت کرده، مربوط به ارزی بوده که بانک به عنوان تسهیلات پرداخت کرده اما به بانک برنگشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/453827" target="_blank">📅 11:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453825">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e157b43618.mp4?token=d994-eEAk1f3doQetfQIzV_kPDRTBtCK-WsOdhJq4PBlF8rM4UyfDem6m1g1yNob74-Y13dzDMazSuBFWG_JkorZhk9O__EJo2tYC-jHQZ70FOFKSnZmIkY9TrsoI64ufG0pm-hsc04ErCdy_W3ep5M_ImwREs2DR3pxRlrsSq5syF4AYNg9q5TcP3KfhZ5CVMl09nofhUoPDAbgKvwlTjbbAS79VO2ViKqzGdWKqBHZaPlhVnH6I6Za8w2_41MIQH6zkU0XqMa6j5x9mB3m2jhljpgRORIxldTGC6oZio0T0TwM_rau2RHn_mFSkjElUeyPjyNdSPn-lq4VMVmrLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e157b43618.mp4?token=d994-eEAk1f3doQetfQIzV_kPDRTBtCK-WsOdhJq4PBlF8rM4UyfDem6m1g1yNob74-Y13dzDMazSuBFWG_JkorZhk9O__EJo2tYC-jHQZ70FOFKSnZmIkY9TrsoI64ufG0pm-hsc04ErCdy_W3ep5M_ImwREs2DR3pxRlrsSq5syF4AYNg9q5TcP3KfhZ5CVMl09nofhUoPDAbgKvwlTjbbAS79VO2ViKqzGdWKqBHZaPlhVnH6I6Za8w2_41MIQH6zkU0XqMa6j5x9mB3m2jhljpgRORIxldTGC6oZio0T0TwM_rau2RHn_mFSkjElUeyPjyNdSPn-lq4VMVmrLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: گرینلند تا ۲۰۲۹ مال ماست!
🔹
رئیس‌جمهور آمریکا که از بدو ورود به کاخ سفید به‌دنبال تصاحب مناطق مختلف جهان بوده، این‌بار گفته که گرینلند دانمارک را پیش‌از پایان دوران ریاست‌جمهوری‌اش تحت‌کنترل آمریکا درخواهد آورد.
🔹
ترامپ در یک مصاحبهٔ تلفنی گفت: «مردم گرینلند می‌خواهند کاری انجام شود؛ گرینلند از دیدگاه ما مهم است.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/453825" target="_blank">📅 11:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453824">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
سرلشکر عبداللهی: هر کشوری با آمریکا همکاری کند، در آتش جنگ خواهد سوخت
🔹
فرمانده قرارگاه مرکزی خاتم‌الانبیا: آمریکا با شتابی فزاینده، مسیر آتش‌افروزی فراگیر در جنگ منطقه‌ای را دنبال می‌کند. این رویکرد، برآیند یک راهبرد خطرناک با هدف توسعه و سلطه نامشروع در کل منطقه است.
🔹
آمریکای جنایتکار در جنگ اخیر علیه ایران اسلامی ثابت نمود که در مسیر دستیابی به مقاصد و اهداف شیطانی خود، از هیچ‌گونه شرارت و ویرانگری علیه منافع و منابع مسلمانان پرهیز نمی‌کند.
🔹
کشورهای مسلمان منطقه باید بدانند که آمریکا با بهره‌گیری از سرمایه، ثروت، زیرساخت‌های حیاتی و منابع راهبردی آنان، به عنوان سپر دفاعی ارتش فرسوده خود و همزمان تقویت ماشین جنگی و امنیت رژیم کودک‌کش و تروریست صهیونیستی بهره می‌برد.
🔹
جمهوری اسلامی ایران و فرزندان شجاع و قهرمان ملت در نیروهای مسلح و جبهه مقاومت ثابت کرده‌اند که موازنه قدرت در منطقه دیگر از مختصات پیشین پیروی نمی‌کند و ناتوانی آمریکا در تحقق راهبردهای تجاوزکارانه و نامشروع علیه ایران اسلامی، باعث گردیده است که ارتش مضمحل آمریکا و رژیم جعلی صهیونیستی از پشت خاکریزهای کشورهای مسلمان، اقدام به جنگ، خون‌ریزی و شرارت نمایند و هزینه جنگ را بر دولت‌های منطقه تحمیل کنند.
🔹
به صراحت اعلام می‌گردد؛ کشورهای مسلمان بایستی با دوراندیشی، جنایات آمریکا را زیر نظر داشته باشند و در همکاری و همراهی با آمریکا تجدیدنظر نمایند؛ که در غیر این صورت، هر کشوری که خود را سپر دفاعی آمریکای جنایتکار و متجاوز قرار دهد، در آتش جنگ خواهد سوخت.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/453824" target="_blank">📅 11:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453823">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REFFgBSx9ku297Yrwp4_km1QfmBMTFhk5WvwBC2iG9szP_lnde-GwROwWMDwlrJIouOHdZIDAtQVfA2T9P05tr2ATfGx9ga7bahcYuYdDeI268SciSJ-8-U2-y8pK8Hj6LnED28OqWeF3sNr1-JIgo5w66fwE512o3x7iRWpFss5QtSQ2TTyXyDn3kXNmJso5MjCsHLU71mnoA3r8DPeTk3ZvSdyA5Teuv2Iqlp7oE8ZkOiXv1HpD1e_lkssqPvcqROdRX3W01sFq3HrXkihhnQZF5r81zOtoawoRBQxqPIxz4pTgwd1QEWdiK011rCjqh0xLiNMg6s8rprYIGhV9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوفا، فیفا را تحریم کرد
🔹
اتحادیۀ فوتبال اروپا و ۵۵ عضو آن در واکنش به پیشنهاد فروش سهام فیفا به سرمایه‌گذاران خصوصی، بیانیه‌ای منتشر کردند و اعلام کردند که در صورت انجام این‌کار در مسابقات جام جهانی ٢٠٣٠ شرکت نخواهند کرد.  @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/453823" target="_blank">📅 11:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453822">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWymxOJIgG9-nTpAoWAGICS_bCAh0h3bTdK6ozUQr9S1wUoq7v3-ORm-vK0x_rs0e0V70PNCQp9_XXa2s0PD3vg9bDphHU12rIWiZmt4TH6kPCNPsxu3t3SMeEFdxxTxdm2LdVbCTNmEzo3ztmA0Mv5GUDd_HwnNlNWI7Gaz5oOlNi8M1hToYL979HuXCgzFvtzTe2438tEnXQet9iIVKUd8Ij3wJRBz-SM4yjI45CFJag5rGyLiK_76ExBnJ4dpIaNBnf0N5Ch8PZUrdKXjMdYONhErfypXOh7YB_uRRGlEOX5-0sUiklfocZZlrBgfDQpvvfXbT9SmbfKwwTJkzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ بازی خاطره‌انگیز آتاری، فیلم می‌شوند
🔹
ددلاین، از معتبرترین رسانه‌های تخصصی صنعت سرگرمی در آمریکا، گزارش داده که شرکت آتاری در همکاری با Entertainment 360، قراردادی با یونیورسال پیکچرز امضا کرده که در آن، این استودیو حق توسعهٔ سینمایی ۱۰ بازی کلاسیک آتاری را در قالب فیلم‌های سینمایی اکشن و ماجراجویانه دریافت می‌کند.
🔹
فیلمنامهٔ این پروژه را «مت رایلی» و «کارل همپه» نوشته‌اند و هر دو علاوه بر نویسندگی، در مقام تهیه‌کننده نیز حضور دارند.
🔹
وید روزن، رئیس هیئت‌مدیره و مدیرعامل آتاری، با تأیید این خبر گفت «بیش از ۵ دهه است که آتاری بازی‌ها و دنیاهایی خلق کرده که مدت‌ها پس‌از انتشار اولیه همچنان بخشی از فرهنگ عامه باقی مانده‌اند. از همکاری با یونیورسال و Entertainment 360 برای انتقال روح برند و بازی‌های نمادین آتاری به رسانه‌ای جدید هیجان‌زده هستیم.»
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/453822" target="_blank">📅 10:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453821">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/440afe73b7.mp4?token=uNVZazudwGHRKs5ToCADE-zt2dmIOIH2xAgllMTjEyKt7Cju6EmqPpsR8YvPtJibLo4tbIWeaPPu0S9PptMCzxZGBmaQbbCobN-_NiEl5JPQiP3yBU6FHFeVuiPYaqiJiZtVmgDwEpYS5C47L0UoFrb58-ftRySiYrbr7jFRuSJs442LVfeZSRhWBkN9Arm-muuRv6P9vwCgc6KaXc-PsZTbFu5eGSYC6Fa9glhidhI6r-dI_yEqidGVCtMwNcdOXukxi1cOLX3xRkjUrUmjbts4boYoMpkX6iVrISHIQ7ZEKapFV5EzT5rOD6rwIsdFi0P0TG8vbXBRlD8jS0N-ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/440afe73b7.mp4?token=uNVZazudwGHRKs5ToCADE-zt2dmIOIH2xAgllMTjEyKt7Cju6EmqPpsR8YvPtJibLo4tbIWeaPPu0S9PptMCzxZGBmaQbbCobN-_NiEl5JPQiP3yBU6FHFeVuiPYaqiJiZtVmgDwEpYS5C47L0UoFrb58-ftRySiYrbr7jFRuSJs442LVfeZSRhWBkN9Arm-muuRv6P9vwCgc6KaXc-PsZTbFu5eGSYC6Fa9glhidhI6r-dI_yEqidGVCtMwNcdOXukxi1cOLX3xRkjUrUmjbts4boYoMpkX6iVrISHIQ7ZEKapFV5EzT5rOD6rwIsdFi0P0TG8vbXBRlD8jS0N-ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت قالیباف از چگونگی شکل‌گیری میدانی به‌نام خیابان در جنگ تحمیلی سوم  @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/453821" target="_blank">📅 10:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453820">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656e493994.mp4?token=tm7rI-9yQoz6HcpV6DqbGwV-bVreLQWcwCvuDvBtxU08X0LvrPtiX7JDuNbXeStsMMXG-Uu6YqMTmnoTmjb1o7AfKzFsIg-nKstjnPG6tJwe1KQUB40JMSXjZthtmXQS49Re5FJp_X8XQxQEOqwnEHfAKgSdxMx2IGDKx1S4yImVowcrWCuJQZ4ote5yceXNefQJnEUNRY87VCNQPkJXUkWwwEmF5zy5JWrIYb57fV3EnylVmT-8_Icu5dr-thIPCg5ZWNQ6fnAHcn2lKtS-fpw9sl4fAZwbLKbV1ieGD65-3mQ7vpaWYNwpwLSH893usdPgnKAi7UGPmU-LZ8gQOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656e493994.mp4?token=tm7rI-9yQoz6HcpV6DqbGwV-bVreLQWcwCvuDvBtxU08X0LvrPtiX7JDuNbXeStsMMXG-Uu6YqMTmnoTmjb1o7AfKzFsIg-nKstjnPG6tJwe1KQUB40JMSXjZthtmXQS49Re5FJp_X8XQxQEOqwnEHfAKgSdxMx2IGDKx1S4yImVowcrWCuJQZ4ote5yceXNefQJnEUNRY87VCNQPkJXUkWwwEmF5zy5JWrIYb57fV3EnylVmT-8_Icu5dr-thIPCg5ZWNQ6fnAHcn2lKtS-fpw9sl4fAZwbLKbV1ieGD65-3mQ7vpaWYNwpwLSH893usdPgnKAi7UGPmU-LZ8gQOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: سرنوشت ۳ خلبان حاضر در عملیات ۱۱ اسفند ارتش هنوز مشخص نیست
🔹
پیگیری‌های ما ادامه دارد. طرف قطری اظهار بی‌اطلاعی کرده؛ از ارتش و دولت قطر می‌خواهیم که با مسئولیت‌پذیری بهتر برابر با کنوانسیون‌های بین‌المللی اقدام کنند. @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/453820" target="_blank">📅 10:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453819">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8bc7642af.mp4?token=X9QGQjF42dlKbWDALadFwn5oyEXNr9c4Sf7CwHITZ-HPjT90iG_AQ3WuvfXY94JF65WxxWBCeOVo14EyalOFD_Flmbe3yfYxRskuHeAKiHPHhWs-itawpu-3-ghwBP1FxbcmxhMv_pEFznwbanGv3JqkWEbqay7pVMZhIV0mMh3f65m3suF1SuXPZxWH-BIByvKVekEgUw7IJRVZrXj9RUv2qP4yC6AbSZeBxNX8B8Oeb-nXpmoyOB4QsMWRpg9FCZE30Gj1R5D_ZaafyPRDTujScqs_iDpF7tsZK3qK_ENDE_tQc1fxZchJdRXIKJ9dxiCC0Qkru1Jjcw-7ZRhztQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8bc7642af.mp4?token=X9QGQjF42dlKbWDALadFwn5oyEXNr9c4Sf7CwHITZ-HPjT90iG_AQ3WuvfXY94JF65WxxWBCeOVo14EyalOFD_Flmbe3yfYxRskuHeAKiHPHhWs-itawpu-3-ghwBP1FxbcmxhMv_pEFznwbanGv3JqkWEbqay7pVMZhIV0mMh3f65m3suF1SuXPZxWH-BIByvKVekEgUw7IJRVZrXj9RUv2qP4yC6AbSZeBxNX8B8Oeb-nXpmoyOB4QsMWRpg9FCZE30Gj1R5D_ZaafyPRDTujScqs_iDpF7tsZK3qK_ENDE_tQc1fxZchJdRXIKJ9dxiCC0Qkru1Jjcw-7ZRhztQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۴ خلبان سوخو ۲۴ ارتش چگونه پایگاه العدید آمریکا را به آتش کشیدند؟
🔹
۱۱ اسفند سال گذشته، ۲ فروند بمب‌افکن سوخو ۲۴ نیروی هوایی ارتش ایران، در پاسخ به حملات ارتش آمریکا و رژیم صهیونی، در عملیاتی از پایگاه هوایی شهید دوران شیراز برخاستند و پس از عبور از سد سامانه‌های…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/453819" target="_blank">📅 10:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453817">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-jmEXHeiY_ch88t2fPHEEsLXocfnZyYDc0b1wuV8Xe2vMhda6TRAAcf5oWhC0sOMHw_UZhSuPCKOjyr0u45WA1qYaIJofVryV-AsDMdS-eHSzo7eeMno2g9ag1fVKrMGUlui920vKpZnktLUcfyrY-Upm4RVfr8aBLgqBvpd8R64Pfvl1iPnneKOq2p4q67znWRSEgXsBrwJxDz9qvX7mYfWjP5snzAHNUGIbBSNH-v6Y9CkwgI7UhW-cIopETR7jj6nW1ENjhXvZfen-RDDnkthF1EdvrJlGptqA68DhSLSNnPLwoOklVyvD5SW0bM74ILgmeJPjc7l2kjz_kG_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار افغانستان در تسخیر کالاهای ایرانی
🔹
بانک جهانی اعلام کرد در پی اختلال در مسیر تجاری پاکستان، تجارت افغانستان به‌طور قابل توجهی به‌سمت ایران و کشورهای آسیای مرکزی تغییر مسیر داده است.
🔹
براساس گزارش بانک جهانی، ۴۸ درصد از واردات افغانستان از طریق کریدورهای آسیای مرکزی و ۴۶ درصد از مسیر ایران انجام شده، درحالی که سهم مسیر پاکستان از واردات این کشور تقریباً به صفر رسیده.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/453817" target="_blank">📅 10:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453816">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
ارتش کویت از درگیری پدافند با پهپادهای «متخاصم» خبر داد
🔹
ستادکل ارتش کویت اعلام کرد که سامانه‌های پدافندی این کشور در حال مقابله با «پهپادهای متخاصم» هستند.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/453816" target="_blank">📅 10:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453814">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvjlIM3m7zhz9yNwPMg3a1Xlr4xLkz37jkZGEHrAQtZFvoPEmKMxgtTDcIjR7oCnw45GXW6VoTOdADcYPMYLZYY_eABbAXx9Fud01DMMam_Tov0gCV22NbkZDSQRxlW0BoDlmsKnWCTv0wlLjsAH-nefih2FcajZ60enKVQc_WXEske2fXlSsKH8mCErVbCbhd4gannl_TfmU2bTuWyMGekpxvZP7-vnisyPAORXaH_qSevvUuM3q9xYYahy6tyvaQIrw--6kwpZQ4MnfuckfrdssbI8mtVi1IaP2dwyohqOVmy2cZJF9nCErq4CLAkmckvcXtmIY5G-b4qa2k1bAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از شهید مصباح‌الهدی در کنار رهبر شهید انقلاب
🔹
این عکس متعلق به آرشیو شخصی خانم سیده هدی حسینی خامنه‌ای است.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/453814" target="_blank">📅 09:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453813">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oROnfMLAFzKjJJ66pJixdkQjjpu3dQjFoGXrrw63TiYtJNwR1XQLt15h6gcn2SmzlcAL54Z8H9ZQGnl9t11lzuD0EfehjztZ5PGYSmCm59p00GXj6K8iv6hEzf4gwCErib5PouDcX9XlhMkoa4olKj2wpHsXUxzbuY1ytLigB3LVWMUgRBgtSnrjvkzng6jETX_gwB01np67sixxJTLNsTV0yhr8B_dlqxzaYeFZbmzgUGx1qlgRnnJqowhwzLmPNwPiASenjPb0zucSxf66w-siGmxJil2QfBrm_CKUHufdbHAbI-ZiCVPzOXxkWPCdT2EMVt4pepV0AuZ_xmA_wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تراژدی در ارتفاع ۸ هزار متری پاکستان
🔹
یک بهمن سهمگین در ارتفاعات برودپیک پاکستان، یکی از تلخ‌ترین حوادث سال‌های اخیر دنیای کوهنوردی را رقم زد؛ جایی که یک تیم بین‌المللی ۱۰ نفره در ارتفاعات این قله ۸ هزارمتری گرفتار شد و سرنوشت چندین کوهنورد همچنان در هاله‌ای از ابهام قرار دارد.
🔹
در میان افراد این تیم، نام نیرمال «نیـمس» پورجا، اسطوره نپالی کوهنوردی جهان و رکورددار صعود سریع به ۱۴ قله بالای ۸ هزار متر، بیش از همه توجه‌ها را به خود جلب کرده است.
🔹
برودپیک با ارتفاع حدود ۸۰۵۱ متر، دوازدهمین کوه بلند جهان و یکی از دشوارترین قله‌ها محسوب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/453813" target="_blank">📅 09:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453812">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UK_NxCotUJ_Rk7Q8SK1XbuBipN5TohrMyydLmWIWGC_MRQPIQAfzJ4j6l5SogpvtTwSioRCfWPjoK7fjRAhToGxu-bhHCOAaRgaykESAovOJZHRStfMipo2ZOCn_f3rYULICWc6gPJOmbd6KB8mLsssaGYxDFpY5TP4mOQyRTzgZant7bmZeZ3ZRWnGR7pPjIwYDlJYm781v937ShpJsnhyG80XORVVwKc8uJd2oJfFWbxhP6vdRxvBs0-dmQCpPz4vmwrViL2_2Ysx9glGb2vFq8rQvGxoAbEdKlSg8nLWt4CRhdBbI6NX_4stNxtOsD3vJZWuIGXmVZT0GGA9Z8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متروباس ۳۰۰ نفره به تهران رسید
🔹
شهردار تهران امروز با اشاره به خرید متروباس برای خط آزادی-تهرانپارس گفت: تاکنون ۵۰ دستگاه از این اتوبوس‌ها وارد کشور شده و روند تکمیل ناوگان ادامه خواهد داشت.
🔸
متروباس که در واقع نسل جدید اتوبوس‌های تندرو (BRT) است، به‌دلیل…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/453812" target="_blank">📅 09:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453811">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ثبت‌نام کنکور ارشد علوم پزشکی به تعویق افتاد
🔹
ثبت‌نام آزمون کارشناسی ارشد رشته‌های علوم پزشکی که قرار بود از امروز آغاز شود، به‌دلیل مشکلات فنی حداکثر یک هفته به تعویق افتاد و زمان جدید آن متعاقباً از سوی وزارت بهداشت اعلام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/453811" target="_blank">📅 09:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453810">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1732ea92f.mp4?token=ScifpMjbFkVjaKkn7lPnr0SnhAlEpg4H634Qzmn_-E46C7Uwcki1sFHpx1hTcuVDJ3QtHTAmTAU0aIHq3G0RXUiwIgH5I0jX6I9rTYZB13ag3U2pScrid-61tOdufGw-4Vc5CXPjm1QZzl0xFKOGemvAJAUUmxndS8vIHLxKPvxR7ye9W7Qnc17ZDUUsQ3LLwgOTtTpujSXoDV-6JncR7uCKttF7ESh89Xzr0KM-AqhyCcq_W4rUUg_ozHLS7Fp0HYGtQ5m2mdkIM7Qu3-uaSD71N7S2sVWscpS75IujlwRUlXKAFaCihrN9Lvw72OHPIX-ywAScPDQEsnX0eqyewgtrlyuYYW6P33xHghRDQvNduRkaX6wOH9rPDaDsh9cAQa6-e_7EzVRCpO6SwplKy7qIO-u6IF9BDvJCxl4VL6Yd1yKr9FmI8_xLbIL3G7K_0j1rcYttkW804GERF03m9CA1CbV2XTN6cSHQ3693nEiDtVDGgmGy1SMRGhbczdX2lDeh34AoxkAFrkcNewLHmhz3OgVVAWVbEogz7WQshwZbQzkgdHwYe1ab_bCaoQNMAEu2xTvu7LNKlTQYwK_kYYMX_3Rm5Z-lKAAt1cNUqnxYBbu_ZB5sk7xHxhoLI4_e5v65kBVJMy93hhlZbL4OF3YsaIryi5WZfnX_eIlLTN8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1732ea92f.mp4?token=ScifpMjbFkVjaKkn7lPnr0SnhAlEpg4H634Qzmn_-E46C7Uwcki1sFHpx1hTcuVDJ3QtHTAmTAU0aIHq3G0RXUiwIgH5I0jX6I9rTYZB13ag3U2pScrid-61tOdufGw-4Vc5CXPjm1QZzl0xFKOGemvAJAUUmxndS8vIHLxKPvxR7ye9W7Qnc17ZDUUsQ3LLwgOTtTpujSXoDV-6JncR7uCKttF7ESh89Xzr0KM-AqhyCcq_W4rUUg_ozHLS7Fp0HYGtQ5m2mdkIM7Qu3-uaSD71N7S2sVWscpS75IujlwRUlXKAFaCihrN9Lvw72OHPIX-ywAScPDQEsnX0eqyewgtrlyuYYW6P33xHghRDQvNduRkaX6wOH9rPDaDsh9cAQa6-e_7EzVRCpO6SwplKy7qIO-u6IF9BDvJCxl4VL6Yd1yKr9FmI8_xLbIL3G7K_0j1rcYttkW804GERF03m9CA1CbV2XTN6cSHQ3693nEiDtVDGgmGy1SMRGhbczdX2lDeh34AoxkAFrkcNewLHmhz3OgVVAWVbEogz7WQshwZbQzkgdHwYe1ab_bCaoQNMAEu2xTvu7LNKlTQYwK_kYYMX_3Rm5Z-lKAAt1cNUqnxYBbu_ZB5sk7xHxhoLI4_e5v65kBVJMy93hhlZbL4OF3YsaIryi5WZfnX_eIlLTN8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: شرط ایران قوی وحدت حول محور ولایت است
🔹
در دورۀ سوم انقلاب، قوی شدن ایران موضوع اول است، بعد از شهادت سردار سلیمانی، امام شهید ما متمرکز بر ایران قوی بودند و به آن تأکید داشتند. در گام دوم انقلاب باید متمرکز بر این قوی شدن باشیم که یک شرط آن وحدت…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/453810" target="_blank">📅 09:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453809">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a503cf789.mp4?token=EZclU0wJLV8_FmVaUuXlZx4ZwN0f3tqf1kEEQOPf52LF716qgtu6Re0B-9MdSO5-aBmRayUg_DbPD3NWtIi9H0jqDo_TNmzC01ocJxyH_pAZ838GTR1W6UfWsB-ZFLQx3hQHkM9ahpXAEt3hzQ3_2-xux2wbjiWrQMi-yjABSQlOMElOn1UMBz5HF2ctk2lv9gqYX4DaKbbZluHXBuf5Ilfv8qaqblUvVrC5RWHNJQQV9huMyKQvTQ1XPH9fvM0TerJXvymL5ykK5m9WpM5e5UYldg5kkcnDVo1EnGsYNXgRiVDvtF2XbdYZ2MrtcyVMLHHdkVCb4ejwfvn4yfkuJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a503cf789.mp4?token=EZclU0wJLV8_FmVaUuXlZx4ZwN0f3tqf1kEEQOPf52LF716qgtu6Re0B-9MdSO5-aBmRayUg_DbPD3NWtIi9H0jqDo_TNmzC01ocJxyH_pAZ838GTR1W6UfWsB-ZFLQx3hQHkM9ahpXAEt3hzQ3_2-xux2wbjiWrQMi-yjABSQlOMElOn1UMBz5HF2ctk2lv9gqYX4DaKbbZluHXBuf5Ilfv8qaqblUvVrC5RWHNJQQV9huMyKQvTQ1XPH9fvM0TerJXvymL5ykK5m9WpM5e5UYldg5kkcnDVo1EnGsYNXgRiVDvtF2XbdYZ2MrtcyVMLHHdkVCb4ejwfvn4yfkuJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف:
شرط ایران قوی وحدت حول محور ولایت است
🔹
در دورۀ سوم انقلاب، قوی شدن ایران موضوع اول است، بعد از شهادت سردار سلیمانی، امام شهید ما متمرکز بر ایران قوی بودند و به آن تأکید داشتند. در گام دوم انقلاب باید متمرکز بر این قوی شدن باشیم که یک شرط آن وحدت حول محور ولایت است.
🔹
ما مسئولان در درجۀ اول باید بسط ید برای ولایت فقیه ایجاد کنیم اگر می‌خواهیم ایران قوی داشته باشیم باید از این نقطه شروع شود.
🔹
ما جنگ را پیروز شدیم ولی باید پیروزی را تثبیت و ثبت کنیم و حتما کشور هم باید امید به آینده داشته باشد و چشم‌انداز آینده آن روشن باشد.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/453809" target="_blank">📅 09:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453802">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S0ppQ2TlZxwl9RZjXH1xY9zfa6dPuOzkIRKEoYxlMNGTyb8TINimePZ-rLJMDFY7DB4Dc-pKZac0TEjXEicsNBKrJKQEqZSNb_W2d5xLQpdC95M4B_FiHt5dmc2riI_eKCHX53VWmjNEdi0ajNDl77GdDjOx2qcHhRWmNapc5nBrH8CODNmrDEFx36mC7mLsNTMIqkP2cOBPAp00Pt1D2cdT-snhhr8NX9EluHt_ZnPEaUoUFV3Xey7PdAg6uA7tYa_pVgKWxqK22ipJ6mXKircqXPSQJCQLfdVsxrFV7QbrQHGoVeMGaamWvxPQN-Vu4Phque-zlijlazC1QQlfgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J85qqIHnaCyxmRTmKCCYuLfeuedbE-S8lZosURnw4YdzpgGAJNr8CpfgtYlKbMj6zo9kw7gue1ZxNsdRQTQXzjL4Z_L221wc970ZoLh8iupOVHfg5bIKOGpJnpydYkLiSx5cTzE-Vjprc6O1Kr4cY7CGcXYqXO_-dazb61aWsWlqK7ph4CLLuR5QXEbJkwp1HZgWlWPC45z7XShUfNQofLebxztPMUdHUfxt5Qzc4uTcA0HDDYvb1SazVZXCKXMKjTA5mCz9Vy94csRYRs8vDHZ6JArGMMTuYmaoIP9A7TTMAxGE8qXhN7Zs6Y2Rlyqhc1kTVVsOBmp3hXPYSH5mYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R3GYH3rVtzOmY1p4ASR7LmsWufa-Vsl5ODnTm-cnMGi_VYepOveIFWu9D-nPjVyIpSIDA6lOFCEtN1YF2assPWtSgco8D6SvGRMUj17Zy3QFr0EWRA18glRbvIFDNk4BgO7zjlQ--IjECAl6bc-ayBbUUKn76jkrmIeO6G_58EdAsmXYUqDTEfP3jLUYPeL7ObVzHBfAk8QK-u6quRO3iVCLWy9gpjKULg4fI8mltgfN-y8Y56M5fAN-uuOAlp13l28Kpmo3i80OHiza6VY_3AEtxkpi1FbtKQh9sN5o7QsGqNQ2jbKBLlw6wG6od8ZNMhAoJZ1twbQ-LyomMMkC6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xq4hTXl-HkW9jzA9gu9E7HdLmslIMK_sDO3L8Z2KJWkDhMcZICdQHFytzHSqwZNdR1PWloKreUseBp-nt2EldxW1P5oFex4xZNjmCRBPZImk_tImttKjyb9aBTg8SAWY_sHKtcwJiEwK5gAPY9a4G6-1IwtF-tWtLgkTnuLmGeIN2GEKwJEYpbwTIDuJwCy7QFKtycrjb6SQNdVQCg-RbL6qyWqrcxXQ9UAcpZrLw40bAtYsnzUyGPA0WOWBjO9J4Qde5BNdAUD39hV0PFg_r3J1Pihn1tVerB-a17gUc_iR5SknQiDxqvD271FbxP3g8CZqGONi6ITmUwf0cDVP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d7m2dcwuMrDEcQRs0uDCjL54T1gErBo5voRjcIgFQ3mY3e-HDUWhH0gBRRF6vN9Vx6BFMr1V64_nxUb8pzciWIo39E6rPazHbbm327rlwoFBe1g2k1wUa6tDwlFVUOxi2DnPi1WSwEfpROV298CtZhDsvIUn7Rloqr9EsG2zPgKGtiXAx6C8LZTuDqOzn77eT4LGKN9r9pZZ-zoS3LXPGYv9d-A9wRGvBt5Y5NpYdDh0NkOo6eSmIfOJ-vW0_1aY6ucYWxLqvHS4fZ_2QEaQI9RHBZWl3FI5PETscWR30cXil24IAImRBDuUV53YefXP53edxnSllJ1_mACqikYFpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hvBO8-TZx39tyj8ODFGTVIcWCxnobM3Q9rOPJfgau8kz3FeIFGmdQLIF4ld5l4bm3ZGN89psbmiFjGfotYANbVd8x4gqAFX156P8SXq_14332GB_j_z6ns7nz1wGaGAITY0ri8wAvH2jcV4TC8tGUXzugQPzzVWBFCE2ys9eTmALWB8F2aRGFAm0qBq8qOlSHu-LhhU_aeAPSCuBE_A3r41Y9sm0cnkMUgRHICqGGS4hPeWoB2CpPOAJyIZVfND-TJAhWNZlKVc_1ivgeXcfHEB4lqJ_5M2X1xvkVOD1g0JwE-h0c-A3qBd_kFGaLZ7G-_dSY0qx8KBtYIrc6MWRkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NWeXtnyQTiJ2-2InJgMaMiiR79hnjK-zlMMrTr1qfBA9Ypvt5TmLTacjh5MGpSTKWgvR-S91sZBIa4DwoiFKf7Gq81DNfowu9rZO9TXv10DcS0RnBeyv8qdLwM-ejVOwN1hPxpsLR_uOeWNXjVaGg32E5YxRbqmH-pfnFL-v2ICR90jrVgz_Sb6hZ6k2yEEepgDi_8kFBUyvY2LfqmKD-Uo32NZZfxf69cSZBVQiG-sy5Oq3x2DBuwz5rGlh7KCyHb1h4SNBM-1MxwpnWFqa1bVNvR3SQZGfVHNHaIkZ2PYBsQjjjOlXEyVIdlwQl304K_duYI9x61wxOLfZpMLtSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
طریق‌الحسین با یاد و خون‌خواهی رهبر شهید
عکس: مهدی ایمانی
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/453802" target="_blank">📅 08:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453801">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/605ec7287f.mp4?token=GsR_2TrBbfJmptReFFQiuI_N0ls6komVcPtsm1pXxOrWTdzavZrF0mTjlIQPmwhkxPOHTfVqrgQ4xQ5ybvWKE-Ie7lsW5QEbNPr2rNbtulGUnbjmBvZ28yJIjFHgpaK4lMmoBSW23eG035akljSEmJWTc_akwYRXWKvPFreU2JUrt1v5u6QJFfv4BIrUXmi0hmEPvtx3zxAkUyxVKyUMWytol6xMi8C8BTnGUf6-FSGPUzABTAR7BRisTq2XhHpxjzqPKdZo45CUSibKFJBzdbXOy1lt55FaNHOonmFUViSsRM5ese-JoW6ZNhClXvCo25FpPaazd2Tifatygyvnfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/605ec7287f.mp4?token=GsR_2TrBbfJmptReFFQiuI_N0ls6komVcPtsm1pXxOrWTdzavZrF0mTjlIQPmwhkxPOHTfVqrgQ4xQ5ybvWKE-Ie7lsW5QEbNPr2rNbtulGUnbjmBvZ28yJIjFHgpaK4lMmoBSW23eG035akljSEmJWTc_akwYRXWKvPFreU2JUrt1v5u6QJFfv4BIrUXmi0hmEPvtx3zxAkUyxVKyUMWytol6xMi8C8BTnGUf6-FSGPUzABTAR7BRisTq2XhHpxjzqPKdZo45CUSibKFJBzdbXOy1lt55FaNHOonmFUViSsRM5ese-JoW6ZNhClXvCo25FpPaazd2Tifatygyvnfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اَبَرپرچم باید برخاست در مسیر عاشقی
🔹
هنرمند اراکی با خلق اَبَرپرچمی با عنوان باید برخاست روایت تازه‌ای از عاشورا و خون‌خواهی را راهی مسیر اربعین کرد.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/453801" target="_blank">📅 08:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453800">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اعزام رایگان زائران‌ تهرانی به مرز ‌مهران، از امروز
🔹
شهرداری تهران: از ساعت ۱۶ امروز، ۶۰ دستگاه ون زائران اربعین را به‌صورت رایگان از میدان آزادی به مرز مهران منتقل می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farsna/453800" target="_blank">📅 07:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453799">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">منابع خبری از وقوع انفجارهای شدید در کی‌یف پایتخت اوکراین، خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/453799" target="_blank">📅 07:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453798">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/199ab599f9.mp4?token=qQTAUiJ8fcUqcTkt_tZuFH_kWc8H-ZCFo-CvZT9XXdXDynOhnSJkrGCJNhkZ7iSA6gwE18ArOK8o254TWlgSWJ0WE_w4GJhN5q-xbSpuVZ-2rbJFFqjO64666v_d3hOghz1L1JOUpLZB0tqOXgbpXIIlvW7crSxT-qKZ3lR_T5QsD2OzqqOXKu1Mv-6Iva-SVdfzBJ8jXHqaEopO4ZD-zyiTrY64AQ_xLall-bcGBM6iLnBP7hzm4ddoOtAjCO7CeGMjj61rwtLJ88zBEpzJT-PDdEbczq4sNVonPsWiyhk6uCKwyLI5l5V04vHKye99rZ-EWJiP93LM0-dbpBJ920b9Hhi3Q_hz-JRC0FqVj2lcLmzMWCH8hU2lgbBsMdPHpU9l8lzPGXcwFXP0-dlyrlfudTyExhtBfv6uwLD-RZfpj2CEFSOPy9HBH_a-oRzhnsFaHIa-UP0tAqi7tq-FgLrdAH983GDuztTzQC-ZAe6RJJw_xC_NqhkjWs4kJUg0r0THpWdPRceSC6osoW929djzZpSsbeOpsyiq8yzqk-JrNK5o0kLLGx7Fl57KMsyRdK7ewrOoWfUI4r8J2xZTZdMC28hgjuLxG6WXIRQ37zLrKFqj8cBnwomuMDIyTGJ1wbt3FWIEvcp1xtm01WjW_k2Mzu-w5ohuKnDrL5QqNUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/199ab599f9.mp4?token=qQTAUiJ8fcUqcTkt_tZuFH_kWc8H-ZCFo-CvZT9XXdXDynOhnSJkrGCJNhkZ7iSA6gwE18ArOK8o254TWlgSWJ0WE_w4GJhN5q-xbSpuVZ-2rbJFFqjO64666v_d3hOghz1L1JOUpLZB0tqOXgbpXIIlvW7crSxT-qKZ3lR_T5QsD2OzqqOXKu1Mv-6Iva-SVdfzBJ8jXHqaEopO4ZD-zyiTrY64AQ_xLall-bcGBM6iLnBP7hzm4ddoOtAjCO7CeGMjj61rwtLJ88zBEpzJT-PDdEbczq4sNVonPsWiyhk6uCKwyLI5l5V04vHKye99rZ-EWJiP93LM0-dbpBJ920b9Hhi3Q_hz-JRC0FqVj2lcLmzMWCH8hU2lgbBsMdPHpU9l8lzPGXcwFXP0-dlyrlfudTyExhtBfv6uwLD-RZfpj2CEFSOPy9HBH_a-oRzhnsFaHIa-UP0tAqi7tq-FgLrdAH983GDuztTzQC-ZAe6RJJw_xC_NqhkjWs4kJUg0r0THpWdPRceSC6osoW929djzZpSsbeOpsyiq8yzqk-JrNK5o0kLLGx7Fl57KMsyRdK7ewrOoWfUI4r8J2xZTZdMC28hgjuLxG6WXIRQ37zLrKFqj8cBnwomuMDIyTGJ1wbt3FWIEvcp1xtm01WjW_k2Mzu-w5ohuKnDrL5QqNUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائران اربعین در عمود ۱۴۴۸
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/453798" target="_blank">📅 07:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453797">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxfdN1Vs-C_Al8NNb4J8woVRivRqhiZaPzyOq4JiFJAJdMZQO4P2nN5DdpKkfy4o1ov2UeOdJPhdmHMauKsACWuXZHH4pwe3by2-1wGeRM8k0xunRt8aiRH_yPbKZHHhroKR46icbo-u9SL0zSbNttOnLdJLLCAtCrCgLipEGzmcPXXmgs_vTJS4m_eQQkQd6mYnURnbjGp12QJqojudSIc5QT9ikJzSlR-SBNcix2b_FQ6KnA43HCOxu2y_nPXU9X85qAyJ4ouhW1cVs4IRC2497s-yTRpefHUJhkw7mNa-ChNSNLJpFtP1Dm59Bn1WvZ4oiSbbaRqJmfK5YEIGtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش سی‌ان‌ان از عصبانیت و ناامیدی ترامپ از عدم پذیرش خواسته‌هایش توسط ایران
🔹
سی‌ان‌ان نوشت: با وجود ادعای ترامپ مبنی بر اینکه ایران برای رسیدن به توافق «التماس می‌کند»، برخی مقام‌های آمریکایی نگران‌اند که مقام‌های ایرانی بیش از هر زمان دیگری مصمم باشند از کنترل بر تنگۀ هرمز به‌عنوان اهرم فشار استفاده کنند و همچنین به سمت نیروهای آمریکایی موشک شلیک کنند.
🔹
به گفتۀ مقام‌های آمریکایی، ترامپ از خودداری تهران در پذیرش خواسته‌هایش به‌شدت ناامید شده و این موضوع به برگزاری نشست‌های پرتنش پشت درهای بسته و تماس‌های تلفنی همراه با الفاظ تند با متحدانش منجر شده است.
🔹
همچنین تهدیدهای مداوم ایران، ترامپ را وادار کرده است برنامه‌های شخصی خود را نیز تغییر دهد؛ از جمله تعویض هواپیمای ایرفورس وان در مسیر بازگشت از ترکیه در اوایل همین ماه. به گفته مقام‌ها، این تغییر به دلیل افزایش تهدیدهای ناشی از ایران انجام شد و انتشار گزارش‌های مربوط به آن، رئیس‌جمهور آمریکا را خشمگین و شرمنده کرد.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/453797" target="_blank">📅 07:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453796">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnUXwRZMcXvEGiFRFxVmYTc7hQPJQ5Ifa1hStV9FujzpEV1ZwBx5q4zDuKilbHj7vm_oxQm_8UhlItXHoByl00d2DLoZ52UuJZAPZl2smuY4n3-aKgTeO-LI6m6Qgz4tFVUWccd7sNH0_qrX6Dx3z87FS_Ftxo3RdSFsOsSLpeVAylNCfqdGC0wbKN4hul5AWpuQ4WtRzYqcYUHNWQmr6zENc44QyvBAGJ810C1KKfA3O83vqVTsCkovvOBq4dGIc2uzRDenp6lbtF18REPnrY7gLZki8_BSE4AYqYHUHgKJXDU8lAVR42KP2uF71iqgCAONDpli2VZY_YT_-Pb5lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حادثۀ دریایی در دریای عمان
🔹
مرکز عملیات تجارت دریایی انگلیس: در پی اصابت یک پرتابه به یک نفتکش در نزدیکی سواحل عمان، موتورخانه این شناور دچار آسیب شد و کنترل خود را از دست داد.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/453796" target="_blank">📅 06:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453795">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca23ce6aa7.mp4?token=nIt2Ich2bxgrv1DENJEtDh7vRAXxIhzvkYDxVO6lFgrlcSgys-8ogWIJRTZSgiYNalCJ48CKl2yBIcdblS-MD4-dsUwf0VQRfyjDNOZZK93T0fJ6uWvKyVJJKr9HAKfL1rCWozav6Wt04PKqy3QIt_IbbO7pUthIon4yMhjJVPRCJ0CXvVG_ISn1bx7KivSsx8TccHnrx_sAmxeXDoELvi7rd5oatrp0Wj3RynYTg_lD1lYF3Lgh8iIRABgYIwYOZN_peMfHr0DBYn60A5gc7Lgd-KYKr8h2nk6fgSh9SZ72IHnBLg5EPCuzwYwj3Z9UDcQyPbmsW3XZoVazlznNcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca23ce6aa7.mp4?token=nIt2Ich2bxgrv1DENJEtDh7vRAXxIhzvkYDxVO6lFgrlcSgys-8ogWIJRTZSgiYNalCJ48CKl2yBIcdblS-MD4-dsUwf0VQRfyjDNOZZK93T0fJ6uWvKyVJJKr9HAKfL1rCWozav6Wt04PKqy3QIt_IbbO7pUthIon4yMhjJVPRCJ0CXvVG_ISn1bx7KivSsx8TccHnrx_sAmxeXDoELvi7rd5oatrp0Wj3RynYTg_lD1lYF3Lgh8iIRABgYIwYOZN_peMfHr0DBYn60A5gc7Lgd-KYKr8h2nk6fgSh9SZ72IHnBLg5EPCuzwYwj3Z9UDcQyPbmsW3XZoVazlznNcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقی‌ها هم در حمایت از ایران، پرچم خونخواهی امام شهید را به دست گرفتند
@Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/453795" target="_blank">📅 05:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453794">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رسانه‌های صهیونیستی از وقوع یک حادثۀ امنیتی برای ارتش این رژیم خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/453794" target="_blank">📅 04:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453793">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رسانه‌های آمریکایی از بسته ‌شدن بخشی از فرودگاه بین‌المللی دنور به دلیل یک تهدید امنیتی احتمالی خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farsna/453793" target="_blank">📅 03:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453792">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">حملۀ اسرائیل به یک فروشگاه متعلق به اردوگاه آوارگان در غزه
🔹
المیادین: جنگنده‌های رژیم صهیونیستی یک فروشگاه تجاری متعلق به اردوگاه آوارگان در غرب بیمارستان شهدای الاقصی در نوار غزه را هدف قرار دادند.
@Farsna</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farsna/453792" target="_blank">📅 03:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453791">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">واکنش عراقچی به رویکرد انگلیس در جنگ تحمیلی علیه ایران
🔹
عراقچی در گفت‌وگوی تلفنی با همتای انگلیسی: رویکرد ناشایست انگلیس در رابطه با ایران از جمله مصوبۀ اخیر این کشور در برچسب‌زنی علیه نیروهای مسلح جمهوری اسلامی ایران و همچنین همدستی انگلیس در ‌دو جنگ تحمیلی…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farsna/453791" target="_blank">📅 02:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453790">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">واکنش عراقچی به رویکرد انگلیس در جنگ تحمیلی علیه ایران
🔹
عراقچی در گفت‌وگوی تلفنی با همتای انگلیسی: رویکرد ناشایست انگلیس در رابطه با ایران از جمله مصوبۀ اخیر این کشور در برچسب‌زنی علیه نیروهای مسلح جمهوری اسلامی ایران و همچنین همدستی انگلیس در ‌دو جنگ تحمیلی آمریکا و رژیم صهیونیستی علیه ایران را محکوم کرده و بر ضرورت تجدید نظر دولت انگلیس در این زمینه تأکید می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farsna/453790" target="_blank">📅 02:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453789">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🎥
اجتماع خون‌خواهی دیّری‌ها در شب ۱۵۳ حماسۀ میدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farsna/453789" target="_blank">📅 02:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453788">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">منابع خبری از وقوع انفجارهای شدید در کی‌یف پایتخت اوکراین، خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farsna/453788" target="_blank">📅 02:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453787">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مهم‌ترین تأسیسات انرژی جهان در تیررس موشک‌های ایرانی
🔹
در طول جنگ ۴۰ روزه وقتی تأسیسات پارس جنوبی هدف قرار گرفت، ایران مهمترین پالایشگاه گازی جهان در قطر را بمباران کرد و بلافاصله ترامپ در توییتی از ایران عذرخواهی و تاکید کرد که «دیگر تکرار نمی‌شود».
🔹
حالا…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farsna/453787" target="_blank">📅 02:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453786">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مهم‌ترین تأسیسات انرژی جهان در تیررس موشک‌های ایرانی
🔹
در طول جنگ ۴۰ روزه وقتی تأسیسات پارس جنوبی هدف قرار گرفت، ایران مهمترین پالایشگاه گازی جهان در قطر را بمباران کرد و بلافاصله ترامپ در توییتی از ایران عذرخواهی و تاکید کرد که «دیگر تکرار نمی‌شود».
🔹
حالا در میانۀ تهدید ایران، آمریکا به خوبی می‌داند، مهم‌ترین تأسیسات انرژی جهان واقع در کشورهای عربی و اسرائیل در تیررس موشک‌های نقطه‌زن و مخرب ایران است.
🔸
میدان نفتی غوار در عربستان
⤴️
غوار ستون فقرات تولید عربستان است و هر گونه اختلال در آن، بیش از ۵ درصد از کل عرضۀ نفت جهان را به خطر می‌اندازد.
🔹
تأسیسات ابقیق و خریص عربستان
⤴️
قلب ماشین صادراتی عربستان که نفت خام میادین غوار، خریص و شیبه را تثبیت و برای صادرات آماده می‌کند.
⤴️
ابقیق نیز تنها نقطه‌ای است که بیش از ۷ میلیون بشکه در روز از آن عبور می‌کند و هرگونه آسیب به آن، علاوه بر ایجاد بحران در صادرات نفت عربستان، زنجیرۀ تامین پتروشیمی‌ها و نیروگاه‌های داخلی و حتی آب‌شیرین‌کن‌ها را مختل می‌کند.
🔸
پالایشگاه الرویس و میدان نفتی زاکوم در امارات
⤴️
زاکوم دومین میدان بزرگ فراساحلی جهان و صاحب صادرات روزانه بیش از ۱ میلیون بشکه نفت خام است.
🔹
میدان گازی گنبد شمالی و تأسیسات ال‌ان‌جی راس‌لفان قطر
⤴️
بزرگ‌ترین میدان گازی جهان با ۲۵ درصد ذخایر اثبات‌شدۀ جهان؛ راس لفان تک‌مهم‌ترین پایانۀ صادراتی ال‌ان‌جی جهان و مسئول حدود ۲۰٪ از کل تجارت جهانی ال‌ان‌جی است.
🔸
میدان نفتی برقان کویت
⤴️
بزرگ‌ترین میدان نفتی کویت با ذخیرۀ حدود ۶۷ میلیارد بشکه؛ برقان یکی از میادین کلیدی است که در بحران اخیر، ۲ میلیون بشکه در روز از تولید کویت را از مدار خارج کرد.
🔹
پالایشگاه ستره و تأسیسات المعامیر بحرین
⤴️
بحرین به دلیل وابستگی شدید به این تاسیسات، آسیب‌پذیرترین کشورهای شورای همکاری خلیج‌فارس در برابر اختلالات انرژی محسوب می‌شود
🔸
میدان‌های گازی لویاتان و تامار اسرائیل
⤴️
لویاتان بزرگ‌ترین میدان گازی اسرائیل و تامار دومین میدان بزرگ آن رژیم است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farsna/453786" target="_blank">📅 02:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453785">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qADXkQgJn1hr6JVVBfCp9UMIzJGaq76FE2rPcmAR7dd6Pilfzfd5a1QJqJg-0Bq4dLWoLmPNR7UP2wV73aMBc5eqkidCRNt1S_T8yFb0jrOZClLoksKH1vZJJSuFMeESU7w1aMM8x3QOOFY3hxl8OUHugbBxa63xkgyi_l3TwTV0b0i0PA9HIe8Wyx8roei-L_WKwzZ-Q5KmPWBPSPLpQkypMjpLfSEhI0EUZyNTeXGIONfUWohMh5ByDUY1IIEpvNqEQn7PQeuhRvi70EYW8P0K0aI22uXbbxXKlKmeruaUNRGD_MU34ynizw2jnYndmGsy8M5vb6PLvRNHnLXD9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرنوشت مدافع پرسپولیس در هاله‌ای از ابهام
🔹
در حالی که قرار بود روز گذشته مرتضی پورعلی‌گنجی، مدافع  پرسپولیس، با مدیرعامل باشگاه پرسپولیس، جلسه‌ای برای تعیین تکلیف وضعیت خود برگزار کند، اما این نشست انجام نشد.
🔹
پورعلی‌گنجی که در فهرست مازاد مهدی تارتار قرار گرفته، در آستانۀ جدایی از پرسپولیس است. در صورتی که قرارداد این مدافع با پرسپولیس به صورت توافقی فسخ شود، او راهی تیم دیگری خواهد شد تا فوتبالش را در باشگاهی جدید ادامه دهد.
🔹
تکلیف نهایی این بازیکن پرسپولیس پس از برگزاری مذاکرات میان نمایندۀ قانونی او و مدیران باشگاه در روزهای آینده مشخص خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/453785" target="_blank">📅 01:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453784">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd2a1c1bc5.mp4?token=af4z5MhrLQHUwGF0hu1rN8LuzhqQ8fjUuhro9U8GVlBg-2L-4LxxsF0hdHRUQLT4RtwbXJUIAN3GP-ED8EDIp4ZsyM2mjWXUEK9YGRifeQFEXHLCAcPbYIf-cP3OGPIISwQTw4GN0l8ab2z12F8YkNpmG_7Z2_KoqMLaj-xXW7QIM6jEmgzoEKEE9wZiKcAdjFNRvNmNhwG6bXUDvMQIfngAfI6MpX0Nu0M_Rnaj-b3yoHy4aY6XSw5rE_j8Mf6i209fBgHt26FyEecHKgqg1A1Zo8MT1pnJkuGAKZc9J5KCP5HMcZsr7cb9xXPGsIdYWK1on10iybhHbvM_qIYAEljzDznBf2TZS5q-WsuOmwy5IC2_g7c-XJ5jtvQis-GudTd032Tw5Yn646TIwPIJGpCDgrlcRcka4OQSpUC3eVkGZOCdtXDnW4vp3NPyfugwqdUT6VHTvS6oE0UnRyspmH2IHYw6wehhasvoEyXT7_xo7VB8XEyhHJCRJH-Sa_5p3nxh4Xkwk74_NM6e0jTtWnjBb3SHZ7pNEXbAGMYBD0kCY8SkhFucN1CVgvnEVx114rXzzaQHLEnqlqEl1KlcYYLIRgumzymHcnxwsZ5-UopIKaB-yAW4hx9qOV1xviuigpXSNCtS_3NFsfRh-LUIyLLg97G8x6SlZCWoTY88s7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd2a1c1bc5.mp4?token=af4z5MhrLQHUwGF0hu1rN8LuzhqQ8fjUuhro9U8GVlBg-2L-4LxxsF0hdHRUQLT4RtwbXJUIAN3GP-ED8EDIp4ZsyM2mjWXUEK9YGRifeQFEXHLCAcPbYIf-cP3OGPIISwQTw4GN0l8ab2z12F8YkNpmG_7Z2_KoqMLaj-xXW7QIM6jEmgzoEKEE9wZiKcAdjFNRvNmNhwG6bXUDvMQIfngAfI6MpX0Nu0M_Rnaj-b3yoHy4aY6XSw5rE_j8Mf6i209fBgHt26FyEecHKgqg1A1Zo8MT1pnJkuGAKZc9J5KCP5HMcZsr7cb9xXPGsIdYWK1on10iybhHbvM_qIYAEljzDznBf2TZS5q-WsuOmwy5IC2_g7c-XJ5jtvQis-GudTd032Tw5Yn646TIwPIJGpCDgrlcRcka4OQSpUC3eVkGZOCdtXDnW4vp3NPyfugwqdUT6VHTvS6oE0UnRyspmH2IHYw6wehhasvoEyXT7_xo7VB8XEyhHJCRJH-Sa_5p3nxh4Xkwk74_NM6e0jTtWnjBb3SHZ7pNEXbAGMYBD0kCY8SkhFucN1CVgvnEVx114rXzzaQHLEnqlqEl1KlcYYLIRgumzymHcnxwsZ5-UopIKaB-yAW4hx9qOV1xviuigpXSNCtS_3NFsfRh-LUIyLLg97G8x6SlZCWoTY88s7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع شبانۀ ایرانی‌ها در کربلای معلی، مجاور سرکنسولگری ایران
@Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/453784" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453783">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJNpdY_996N7M6EdJ98DHTRyKrbU7luc20OVVwzjQhHTADr-o6mOXLCg_4Q9MNuLwvkEbkvDO1KitpyXUdvjpKBs_AZ6EWVrEtW6j2v3LtirXkkoacGrX-ICPSXRqinKA-K9L5W8fcUHh03o5jZKWSpVfIEEn5hwaP_ZzX54ou0pTSHdXAA6GDezSGsTzi4i_GLD6Z1Uu5-4iTldMD54B5i5EoBoRiJai7bEHU4UNafAfFOsa4hoFRCcrzGQzUsqSczmuzcFUHghsSr4eIkImWPyHi7EUZkyQu0QLcsriw7504DoskJG6HWdfqV16hlrg9MtQwkFDaipraBzFFujgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای وال‌استریت ژورنال: ترامپ دستور حملۀ جدید به ایران را صادر کرده است
🔹
روزنامۀ وال‌استریت ژورنال مدعی شد رئیس‌جمهور تروریست آمریکا دستور اجرای دور تازه‌ای از حملات نظامی علیه ایران را صادر کرده و این عملیات ممکن است از پایان هفتۀ جاری میلادی آغاز شود.
🔹
این روزنامه مدعی شده هدف از این حملات، ازسرگیری فشارهای نظامی گسترده برای وادار کردن تهران به تسلیم و بازگرداندن ایران به میز مذاکرات است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farsna/453783" target="_blank">📅 01:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453782">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiuQCFID-BAFWjMT_xv9SmXAiW3bXQlRu2wKlTnMkxQXUfpLq7WWoZNLIMT4F3CKLnNcEz1tFqcC2HuGlEnhDodiYgykPu3CYVLYbPr0UZUXWCcMd0eqaxYzoYbOR6VwtduJz_aVlhwSiShYGq4EiuDN_ThUgc2esT3_yMLPU7Ls8mzy2epqie7DaGvsC4fUEJyk4U39e3PAP2VDlXHfygfGr8XVu-i0-A6EFajXehsWeMGg6FPN3a_YNd2ulvClpbw5jjh5jXCSRFb84CWJuO2I1WVbQuKElup5LaizaMNeFKJiFpAjcG3V3x3-tMdJQz_WUm2r3_IKsQi_ciWlwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی: ادامۀ آتش‌افروزی آمریکا قفل تنگۀ هرمز را محکم‌تر می‌کند
🔹
محمدباقر ذوالقدر: ادامۀ محاصرۀ دریایی و آتش‌افروزی رژیم آمریکا، هم قفل تنگۀ هرمز را محکم‌تر می‌کند و هم تنگه‌ها و گلوگاه‌های دیگر را می‌بندد؛ و تاوان آن‌ را اقتصاد جهانی، بازار انرژی و رای‌دهندگان آمریکایی خواهند داد.
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/453782" target="_blank">📅 01:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453777">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GRvniMkjOvpJs-yK65WdTo_kslCu1qG2sP1Y5Ra1X-m3Z_MRJhUEC1lXyuEgN83CTgHFucuIebyDTyXSuPrC5I_W2j3jV7_UbCtXuH3ADaapGRwhtG0UVOjGCdLOWKr2OwXj7jXCIuLh6caUoIP8cC2KJjvU7pN1VqvufoCMdDhf4S2L3Lr4Mbg5_EaiBHJWBrTeFN5qnAjqqZrm0ZFIKSXyDlcYlsYTwunwl3DLaU1SINY7qwklTdF6Y6ImqJ28tlcfAdphUV6_DpQcy3JKE-Jc_50JodPLOsGaoZd2cGP-lzAkTZqkaWTPl4uaImUe3Wtq2UG0hAo7WPnKSe6cCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ILf-r4DtQDv68hGG4xMoCcDSkyTkRgl-KX2J31WSL6ocZCXxINpV0PetNYr9v8KY20eBlIFUnpT-omzOAR0xNRvjJRyGTNkOnS-gpbErusj2gi1xzkLlzx7rlSpFzuNPQKjkvCqKCrcQ_id-5nOrIEaiIDVS4bKcIQ6n1CpMSKPS28e-LipmOArJMk4bcskyNRE_gYxOJ1_tnKJCoTmy1YRPw6D6tDBbsWEAT8Maj17Eu6N10bJ5meFgfGiX73IhvrPkwpuZnc1RW2XvVAJgk6QevepZBZ6X9S41b8bP4S5VfAZJxteculX6Ta1dabvnCHMEi0Nhk3xcub-cJDqK7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBMNwuzK1niC0q076boLM_oOwSNq0w-9qjovnLWYv-5Tyw0WwYTVElz34-KM6JeLzfsqKtbTbZyi_4BnG1zIXixtc0Ksf5Kco1q6zbakbHAjahiMSn0kauDmJowB1-KxTq1WxlHhfok7vT0YLlu_DqS6Ba75ueQma_Etz6LUm12vZMYnoYEEK2N7vNlZpDfR3Fvfa-eupLmkcu7m8xq1MmtxrG7Sj33_Bz0x12jHdYS8UaS3kX4PqMo_bytF8fGCfE3a-LzDKv6KbvehOcrK4CKG6NP6OTLy4dRQKysCZQ1BCez0mNWfvj-X27WpVe4WyzAshO9zjCwooKJhGtbi5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vIEaRK9jhP9Pj9Oj18WPoysl99QNuBDqqS5exbzZIRbNyUkF0s807pRjlAVIBqoD6HlOmUnIUp_Zcy9Srd4Dkm2kbYiueY5-my00gYZk4zsuj60uuG8Q48rMI6y9LdndotCkuyqRzYpke-UzaJOS3Xci-4a76ljrmSS9EGztfwbQt8mNZoJ3STOMr77FpTFgeth8CktsXzBgJoqYilAUfHbpx4d3KikKSo8Kp0GH42nh43rFL5FLb7grkdz7YvKGySqpBshos3MJHZ_jKXA6UTQmgbn66XTACvtm7YqjESJwTo4H_N8gUgucTw8Mbax90ctMzvFEWbDAZgWG4DSMXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HI13V-y6hCSce2RMPQX-UfKQL14bUEzGdVKI1PoXrpUHh4Iq3_oRLN6bY6slZeCiIGeioFs-J2ZXZQeL5gyievIyHu8dzHR-FI9YraQe-iB6DRARll62RrdfH4comSdze1FBP61ZyRLDmrre6otWvGPHzxRX75GIoaLALVJitNiCLjyKljOEndCr8mGOAcyNhROPzjNqNQG4OU0qpbwF0Gw7sS7Xax_yddaA1rbfJBXuYRLT5bbDs4m3sF9r7zB6FXgUtxlSbznec1zqGBWIZ0YDUrzNEW6P-mocSkvZ5BWDZwMWlhjWHJZx5zVzjTzsAQ1K8GkMY05E2fNiOeKRGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۱۰ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/453777" target="_blank">📅 01:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453767">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PZFW-WZLdx3S42U2dhJt3vKqqiFu_R20Dn_DeZN0dbYudd1CoXZuMAq_e9ICmhnIFYtb7iQPDHZOOftbuLOjLR_vDZREM0uF_K9vsJ_p-qtUt42aL0Ws8mm53OAc2g6sWxC6gU1pT7Sw19R5rU45eDGY-bVw4AqQIYavX0dSS6oWw3-DaE8Hl7bWQxANspsoVQGr1r_8OJgJPT4D2zaDKLyXMN7U0BEa8apTEn1-U3isEkTXbU4yqLDgIddyf77uw3Mzv0X1P_JgYV_lKEWEMjNmS8ruWS_cLG1aFosP5l2LZi2DSJMvrsi4SfLeDobGwyM8XPbWv7SgNc1dJpo1Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bYjFu3N1e43t8yvAxtlVMRJ4VwuhITPKTiUwDVlM-OH2Pn9yIuO-DmCGrm2Utd5YY-q6Hr1ZAcAVoRSG_LABAuCwGCdyFSKboepslpS2RWn-5xJu6z5gMGAy7okwThjCb2peeG-AqL8q4tDqEfrXX7wAe_rutp3Mv9VlOkfD1lDAJh0OfUmUFwJc9kdh_dB7aJuVmc0oIzOzKdSGRG4--TLCPCCiYsRH6hkLQR9HO5ufO85M4P6AN1nHmRL_Vi92HICSLeArDAyn5sAUeZpx3C8fwdl5PiPadkuaPo0D29fEbOl-2g2V2pz3jpj3k2eoU0mQWwQ2pIKC_YNKtLwkIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fiWabQGJzwSQO2t3fnw66Th2mm_CePNzsXjXQgvha9gJHJmRbDdEys5NYCQBaqMP1VMyvvcu2nBRzfE6FAgJzVUS0cga2eDcrOg3_j-ng3FHWmU1cfbXOcrhJT9t6boWFsxg3OAfk-hSrvIjOMYRhbGjKv9IsS-9i_JSe-Mo1y8q3w2jmiYKd7bf6i1Aa8hQeAVHoY2IPvp3z1tGcYKjLe_ObGfgWqo0-6JOCBAugecLdEyuzJ9tpvkiEWHzaZ4N17oNTO8IxeL47KdU3-z8a8KyZaay3z0-JCdY5VWnZuEbnXrVVgmlgPDPsLxF4fUPn9mhpczhm0KUWZxS5zdo0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MtPrD4GfLRLw195sfqyb-efXcjew4J0aRFjCPuuGCoEm8wIHoubSCauJupPnjl8BiLq_mqLIya8s1PcuUsIk2zfr69KpTva78jOs6YB-Yb9IKXkh5OJSsx18EUm4CbRHJCIhWhggAzZL-gGWnKC2dqkMLgcrFsBntWclKtWveE7GCRRVTQN3DDgabngGP5ndBGSjYa5DVZB_ge_x78GSI62KkJaSATwbFScavufNWQvjpNdWCzh56oe-Crzmjh8Tdrg4GmxMiYEYO9Fwrf1pFJwCEgnb0uMh5spjIF1AaLZVJy-D175nPhE7ukO_pWvGMVFJ4YVgKAq4nnCAgWCB-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQJHqprAR9WlSV1i0Pf3xLHy8ihHLzZTq8onKommuQ6iEj11sMeeT1wUPEiR_66BogIZt-K_WO43n0JkOaDd_a7Ca0BKS7yN_biU3E_uhQy9eDOERloekP9_PNDubxPjOuuXnw7BWqU0NFBxWdBSaXwIVta-zb3kfuSytc8lYfBy7riPRfqLfcX0IqMDMJJGFjvHXwVkjEJ96v6Q2hqScwh8sLlNAdRsylNKt1Jl0mwj9SYdO4lwDQZDireWC7aKCyjLQ1GPggOCl5lPArmfIE1RhmYrdOZCXg3KaP3s9amhqNlNAPNBVCpeZ7cVETSQ6wdBozh7A_dgLh7HA5DFyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TALu2dQTK1V4h9ixei77c2uvmMzkJfp0exuCdwPe6xfGIkBESnxcXsbQl8irIloygp8BNDM2gjLOLO-yV3R250-cZKXy_EBhJzQl7XOL7p7EjhXkLHk9neIpntmmtxKtqFBJx2avOpjTXzXbeketh8sxtAN_MD56chVPXMUz9YC366obuk_xAZYqd5UogCZCzEl5P_FNpkh8zhejKe2FwFfZxSoCsOtAA9vkzaJN49nGY_H3mAJrwBKke6PeOx1D4DXFfzLorGBq1stsP6gff4RHb7ylBs5fsOYTU9ZGCUy33NT0GS4MoWbfh0quGDIaev45Ag6b9yEe3lBEXRrXHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kwOyMUNs9_R4jwkiNfZh3aGZoPzX9Jcqe1HQmgunrWdynjADZZSWTZcIAURmVGHWKVxjNRh12yF9X8ZgrHHhJrrtl1MeQ79yXZfrW4fKMFOpBcV-L4hMNO3RQNZCGkq5fU-8SgrmJUk3XDnupAqAPwzgtdoTnq9hEu_9Cpr4WEdizz02pZxPXD0vX_THFcu4UwuYnWNHcg2WeKkc5hNZnEU_m_bGFUaXdNkdqzSKn-m6VtYYhujwy9O-pGdOJmA1XJ28MfyL1boYt6D-GEVghaw40_5NKYOuYHECnBV3mnBQguKEu8OQMlptPJoqsVXTkRR7DB1PQF1NHyJKkpz4ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NuktP_i9bcsi-RGp0Sl9jvWSUjOuAe1rNJ2xy6DOfXG0j7B5n_DMfHCIWtfylwDkOlIu9qy6sOA1zedMT3-RLwtFB2fCi8VGy6BKNhrkLPwH1kz1_KOAeTObTAzI0xbJK7UhSEnbCdlMpsEUNScklopQJgRndL6aNBCzn_t98B8X6o4aHpqaRIxbMJgeePI--s5c8-S3FD7KAecTUjlZHny0DYLtg3hhUMbbM0a2AWgnQqW5uz9ddaJ7NB2sICtI6GyQOfupgwDIpam9gE7Dmy0kbCurz7XKVsiTq8JRJVQnFl20H-w692Hi_LPAHCOHAItbPk61_k8GgQF7uCyRSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJ9JQvgmn_kz_SV7Jm8S015OhcpSkqweQO8kutlPb0uUOKDF_1MiEvEKsH6uT6ryX7oTGmPu5_h5LbGnwkfFAy4GLxJP5phJqbPr5Yi-qDEzV-XmtlTolg8xyztaLkKeGJpgLa5G9z7P2A3xzNWFi43aJNeBDLK338KRUQ6tWuumoPgXI3bUxfY1Sr1mDgRsIvuwxlgUdTTIfyvWyfOE5e_mFHgC_KEinh9Fo12QnMdMEMtU2JeBvqXz8s0WduqsTwbTqP_ThREYpbMxIRhwqBVus7xjb1em2RLwModiH4fHoLFI_Hp3yL09BPXpgUwYcaDoJcHSNH01d1TLONx7gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/In0xXLBDVAcmXx2GAIssg5YjuYlaIE1ZJoMiPAULQIOe9Kp-mDFCc1D3H5Abwl9-lMW1yfzKD_1rKlYXVS-2pACmR3PAAyVXmd8LfveJN2p1AggUszFCyESk2jjCkYDcjg4dgOL08KVE7QcwZXtQUZRPML4E0hRKXycHveUC-SSvfthC8dkEKjOt7v3QkRxSrtzdH7gSi8fuJJDBkNArhIlDLIxzRkJd6Htq6aannTvydvgk5xhfpAxt0hK1UDacoqZ7KD-dbNUyADFjptl0HQaYLzFnVwVc4dnJan9JVfUfx4HTTWQC6CoTSW6NmPHZpHSxUzuEANDzi2kqca6zmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/453767" target="_blank">📅 01:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453766">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00813dee2d.mp4?token=HqVx3sZTXEYdkL6bWDYuTGP_EfgceEn2NKwvQx_PksoLO8TFVJIDSJ2csvBGMh7VCkA85LLrsZYubcbRVmcdshzL7xyETftKNfWS9I1pmTSFanmJnfjJUefdP31boR_xkjEIFFm3b0uD0DkRcFAQJuWnRKGfiXFECmnW5Fy5PWpfd4LMWCL1c9JAOcxXPR5CudyabalDn_KocfBzABzbIf11g68o0ZWL3FG3g9uT3xsoJw_FWZJtDIdGP3nxPnb3C_cKvnFBKEUmsqvBYAi9BjTwdvoVPeYhTq9E6qh9AU5AIFGwWLu67iBKW5wSRjEA-1d-LPi-eyZguD4u3R8-KDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00813dee2d.mp4?token=HqVx3sZTXEYdkL6bWDYuTGP_EfgceEn2NKwvQx_PksoLO8TFVJIDSJ2csvBGMh7VCkA85LLrsZYubcbRVmcdshzL7xyETftKNfWS9I1pmTSFanmJnfjJUefdP31boR_xkjEIFFm3b0uD0DkRcFAQJuWnRKGfiXFECmnW5Fy5PWpfd4LMWCL1c9JAOcxXPR5CudyabalDn_KocfBzABzbIf11g68o0ZWL3FG3g9uT3xsoJw_FWZJtDIdGP3nxPnb3C_cKvnFBKEUmsqvBYAi9BjTwdvoVPeYhTq9E6qh9AU5AIFGwWLu67iBKW5wSRjEA-1d-LPi-eyZguD4u3R8-KDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مکالمۀ اخطار نیروی دریایی سپاه به کشتی‌های متخلف، و بازگرداندن نفتکش‌ها از مسیر غیرقانونی
🔹
تنگۀ هرمز بسته است و هرگونه عبورومرور صرفا با هماهنگی نیروی دریایی سپاه امکان‌پذیر خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/453766" target="_blank">📅 00:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453765">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‌ تعداد مأموران شهید درگیری مسلحانهٔ دیروز در شادگان به ۳ نفر رسید
🔹
فرمانده انتظامی خوزستان: شهید علیرضا فتحی که دیروز در مأموریت مقابله با قاچاقچیان مسلح مجروح شده بود، با وجود تلاش کادر درمان، بر اثر شدت جراحات به شهادت رسید.
🔸
پیش‌تر هم شهید مهدی مهدوی‌کیا…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/453765" target="_blank">📅 00:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453764">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd902523ca.mp4?token=V1n4-S5SCfa-z_BO6G66xi4qP0-KgzMvEB6PDB6acLVh30UQr1GowRZuCD43x2tJlRaqmBxrey3gHJR7rfVTJgzBJ1Gw-qGQjyDG_cKY9bJWEVTlN8kGSKAV0EvRs0OpCd5SWtUexJb4vj_8XjnmqgpTqr314QE7OKqujv_5B87eAHkIkR5ipfppAcsZu_2iCvNvCpjOHfOeIAJpuJmiUYEbJv27Qrtxw8GnEIEb96TK22QmXs8BMN0nFy2SWqNy7v4bEhIhtCatId6vUcjOES4MKUi6fJaF_2v3wsZ5vRsnEJf8XUzRGxPeSyV0UqE8L6NJJqXVpsMIxUrAQz-gyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd902523ca.mp4?token=V1n4-S5SCfa-z_BO6G66xi4qP0-KgzMvEB6PDB6acLVh30UQr1GowRZuCD43x2tJlRaqmBxrey3gHJR7rfVTJgzBJ1Gw-qGQjyDG_cKY9bJWEVTlN8kGSKAV0EvRs0OpCd5SWtUexJb4vj_8XjnmqgpTqr314QE7OKqujv_5B87eAHkIkR5ipfppAcsZu_2iCvNvCpjOHfOeIAJpuJmiUYEbJv27Qrtxw8GnEIEb96TK22QmXs8BMN0nFy2SWqNy7v4bEhIhtCatId6vUcjOES4MKUi6fJaF_2v3wsZ5vRsnEJf8XUzRGxPeSyV0UqE8L6NJJqXVpsMIxUrAQz-gyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار تجمعات شبانه به حرم امیرالمومنین(ع) رسید
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/453764" target="_blank">📅 00:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453763">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1c_UJ_4K1_fGgkA9mOI0bbrOHbua4txticXJ8UNEWYQFwCIDzFDRjBIZAM3VTw5ADxgIvygc3EzTVFXtYtDWhemSMGVbVGa3mAwkur2ZawQ_mqXuIidLfhmsu9gYiCZFVkYnJbHb9XvDbRNTZ1GzHKTIeTp-1mvJwpCdh_r-RK89v6DVGUwBprhftxD6pw2rraAAohRledSMMO_Z_ao8TDlXe5SA2V9X4ErpYBRK6kaqhGB395zPIL7wRmTzxBB-qZ5BiLQKtXDnCPQXjkt8oovWn6vQ4hRH0wzHnr8iOndCHyTJ6zSgxODiZJ7mlziWEDk_46Rfiz9VVwmku6stg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: ۸ نفتکش سعودی مجبور به تغییر مسیر شدند
🔹
یحیی سریع، سخنگوی نیروهای مسلح یمن: در راستای تثبیت معادلۀ محاصره در برابر محاصره، ۸ فروند نفت‌کش سعودی مجبور به بازگشت و تغییر مسیر خود شدند.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/453763" target="_blank">📅 00:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453762">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شهادت یک مامور در درگیری با سارقان مسلح شادگان
🔹
فرمانده انتظامی شادگان: در پی درگیری مسلحانه میان مأموران و سارقان در شهرستان شادگان، یکی از قاچاقچیان به‌طور ناگهانی به‌سمت ماموران پلیس تیراندازی کرد.
🔹
یکی از کارکنان پلیس در این اقدام ناجوانمردانه به شهادت…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/453762" target="_blank">📅 23:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453761">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58b7691d1c.mp4?token=Pc1rdIcx33wza_6s7YBqI5BL2vT60XlnrRv2NR5CUOTGEJQiSNRytrPYbUtN9Z-iUgF18V7nkGbmJujcA6LkD2ESo7CzJfAzkB8oCFLeh7N-4asmDIT4-VYpOfdt5aOiiGNptDtWN9TxHbIwNrT2e0z6zeVXj-j8HVWjuwhsx4FghamnAVNbxHs9WyR36w5_BaDp_varEJGnpiTQaDbGb6Csvd-ISsS8lcmUGHlyx0Kh2ZTHu6Lj7TXQLOySDkUINc3g5p64fP_1w91Oov60wKBTmHOSAIMRBzxmNT1j8g28_ceHdNwhiU94H_r6ZS0BLAc-qHbFUMYAX4TIaRgaAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58b7691d1c.mp4?token=Pc1rdIcx33wza_6s7YBqI5BL2vT60XlnrRv2NR5CUOTGEJQiSNRytrPYbUtN9Z-iUgF18V7nkGbmJujcA6LkD2ESo7CzJfAzkB8oCFLeh7N-4asmDIT4-VYpOfdt5aOiiGNptDtWN9TxHbIwNrT2e0z6zeVXj-j8HVWjuwhsx4FghamnAVNbxHs9WyR36w5_BaDp_varEJGnpiTQaDbGb6Csvd-ISsS8lcmUGHlyx0Kh2ZTHu6Lj7TXQLOySDkUINc3g5p64fP_1w91Oov60wKBTmHOSAIMRBzxmNT1j8g28_ceHdNwhiU94H_r6ZS0BLAc-qHbFUMYAX4TIaRgaAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مرگ بر آمریکا و مرگ بر اسرائیل زائران نجف در موکب امام رضا آستان قدس رضوی
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/453761" target="_blank">📅 23:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453760">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88b386fe25.mp4?token=nJtmjSTO2gUEq_mUko9AuVKfj37nyLv89caGrwbEQIlUIA7fmEt-MdD3qp_SKEFlYwEl8SlfcnrBhcDPxZxtqYYoA9nZKadEc7AMPIWCC1p12Fl8BdHtwZVsI84yw2Wq7VaiS5mUdWyrcbQL35QtvSnBJyA8yTOqDahXY0ngPJJ8djcM3_Ezq81h89o2Ofs7t_TaQTD38g5CbRBP2SItzhfNbnwH9BZbyxlhT_WihsOecy3OUx4mPJItQUPchGvmqKDFvbHwocIIoSMLgvjMew8ZBkuFuS8-02L9z0_y3jYs2RTi1WQvXWiVVPD45IT4Ya55agJr34gS-JhrwLNWHT9fu7mNDf6ZHJf0Wsw69sawEzpgo45ot7pPPun3LtjWQFRpbwL8GUsws2t9M3HvlPaFGrhpiIyAJZ-AJwHunJQomkeIRNA6RHnbwEn2P2GJRnvv1ob2bxY7ejlLBeCPJVlzF3D2Rpj9hppMScVRjJVqcecqQwS9i8q-ZlVt8TgkSaFBX749fsUD9vwJ_Q4XBsduPBpBJI_X9kaFFRRNjUUexcwiuz8DZtymJskJkM1aBQ-7rQjgYmDjpuC9xbb5zzrqw3lERNYsRS9XpiPDLKXEQ1ySqbp_sf20px2_2Tq2fPUf9aI4DaBGkAohh8EAUQwyMXZiOUWJC63A9QGK_Fc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88b386fe25.mp4?token=nJtmjSTO2gUEq_mUko9AuVKfj37nyLv89caGrwbEQIlUIA7fmEt-MdD3qp_SKEFlYwEl8SlfcnrBhcDPxZxtqYYoA9nZKadEc7AMPIWCC1p12Fl8BdHtwZVsI84yw2Wq7VaiS5mUdWyrcbQL35QtvSnBJyA8yTOqDahXY0ngPJJ8djcM3_Ezq81h89o2Ofs7t_TaQTD38g5CbRBP2SItzhfNbnwH9BZbyxlhT_WihsOecy3OUx4mPJItQUPchGvmqKDFvbHwocIIoSMLgvjMew8ZBkuFuS8-02L9z0_y3jYs2RTi1WQvXWiVVPD45IT4Ya55agJr34gS-JhrwLNWHT9fu7mNDf6ZHJf0Wsw69sawEzpgo45ot7pPPun3LtjWQFRpbwL8GUsws2t9M3HvlPaFGrhpiIyAJZ-AJwHunJQomkeIRNA6RHnbwEn2P2GJRnvv1ob2bxY7ejlLBeCPJVlzF3D2Rpj9hppMScVRjJVqcecqQwS9i8q-ZlVt8TgkSaFBX749fsUD9vwJ_Q4XBsduPBpBJI_X9kaFFRRNjUUexcwiuz8DZtymJskJkM1aBQ-7rQjgYmDjpuC9xbb5zzrqw3lERNYsRS9XpiPDLKXEQ1ySqbp_sf20px2_2Tq2fPUf9aI4DaBGkAohh8EAUQwyMXZiOUWJC63A9QGK_Fc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقی‌ها دوست دارند روی موشک‌های ایرانی چه بنویسند
🔸
درخواست مردم عراق از سردار سیدمجید موسوی و نیروهای پای لانچر
@Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/453760" target="_blank">📅 23:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453759">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/155545352e.mp4?token=OH1s21KiyTwKt3Dqvo406cibR0Q0z7eBw4fuzsMPN884d6u3XqKZ8YSTfY_e6BYumVXRUrDuVcsX--OnE6VIm1niR4bL20rZQ8o4Lk3bwNAuUAHxRVipXgagxvuH_Y2BcywsQ5Ug6g82JZ2UgNP_gk9VNfaNSyKTzNcn9T4IvztHwzCXdEF8Vr8b-skxom_ETCkYOc3_WeneXj2QI3C6Psm-rLeSBe52RS72sy0coINQXBwOAsEA7hLed40v_MreV7YQByclODQepZaFf_3rvDq3jPxmXEmE84NRxtno6ZlhRMfD8bxToPNiEMsSQCbZ36f6bytJLox_6o7AxsQUog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/155545352e.mp4?token=OH1s21KiyTwKt3Dqvo406cibR0Q0z7eBw4fuzsMPN884d6u3XqKZ8YSTfY_e6BYumVXRUrDuVcsX--OnE6VIm1niR4bL20rZQ8o4Lk3bwNAuUAHxRVipXgagxvuH_Y2BcywsQ5Ug6g82JZ2UgNP_gk9VNfaNSyKTzNcn9T4IvztHwzCXdEF8Vr8b-skxom_ETCkYOc3_WeneXj2QI3C6Psm-rLeSBe52RS72sy0coINQXBwOAsEA7hLed40v_MreV7YQByclODQepZaFf_3rvDq3jPxmXEmE84NRxtno6ZlhRMfD8bxToPNiEMsSQCbZ36f6bytJLox_6o7AxsQUog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عطر غذای متبرک رضوی در مسیر اربعین
🔹
آشپزخانهٔ مرکزی آستان قدس رضوی این روزها در مرز مهران بی‌وقفه مشغول آماده‌سازی وعده‌های غذای گرم جهت توزیع بین زائران اربعین در موکب‌های امام رضا(ع) است.
@Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/453759" target="_blank">📅 22:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453758">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78c8ea306a.mp4?token=cZBRMvUdspbrQnnbaKBpIH1rd3Sly3UIhe--POL4bOfeCYP1FIQFElJwqPyrs3BO1_afmteVfDgQ1Ep7Q1UjlLgkcDCo_qjyMff1ynBHmVmwwPR-d942dVkIClY7FAIV-F-tRY3ppwUj4mxOjeXB14qqeR6kqlUhwVm0RanhfbwNc21Qx-20BpYBXrPgN0wmk-_FDAsCMvcQVyo00ojCWeqg_TRJ5nuDfYtlCyTsZbH7T3h0c1vkI0m8bsQVfGVxidJV5x-ioi8xEPFEVEm_orp1mWtCsKXWfR8QIpiSksdoFTKxDS1gldEWyVJsJafE1lrSMqXwLTmzbaVq5YwFIgHcHH5EF35LOATnDFTPV9LbOPoimhSZPpAFeldj8DBYV5fwnha1f7BkXUzQB0b_wlmt7V0ubKi_CQhq_HKUlgTFJ9IGfknsX9hlOWIz9FOI5rqohwRup-eIIdeKaYciwHg3LPAqk71ZOc_XDaqg1fEgMn8Y9FzKbGJ2WQPyYQWj3p3NPNIOB0oyWUxjv_qF4SwccnsqUpdHw_5i1fvQfz7V8JvTy0Bn_R8iLC-tAu0p5qfxjKsw0Ti8qKDpEpgnfqf-vNcrYk42ecAbOQOkpbRhNrCeLcLCaOt9g_HmOgylB86zUaDqWwObVWYfI3Azo73WNUrVUx6p3gCwMAJhosY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78c8ea306a.mp4?token=cZBRMvUdspbrQnnbaKBpIH1rd3Sly3UIhe--POL4bOfeCYP1FIQFElJwqPyrs3BO1_afmteVfDgQ1Ep7Q1UjlLgkcDCo_qjyMff1ynBHmVmwwPR-d942dVkIClY7FAIV-F-tRY3ppwUj4mxOjeXB14qqeR6kqlUhwVm0RanhfbwNc21Qx-20BpYBXrPgN0wmk-_FDAsCMvcQVyo00ojCWeqg_TRJ5nuDfYtlCyTsZbH7T3h0c1vkI0m8bsQVfGVxidJV5x-ioi8xEPFEVEm_orp1mWtCsKXWfR8QIpiSksdoFTKxDS1gldEWyVJsJafE1lrSMqXwLTmzbaVq5YwFIgHcHH5EF35LOATnDFTPV9LbOPoimhSZPpAFeldj8DBYV5fwnha1f7BkXUzQB0b_wlmt7V0ubKi_CQhq_HKUlgTFJ9IGfknsX9hlOWIz9FOI5rqohwRup-eIIdeKaYciwHg3LPAqk71ZOc_XDaqg1fEgMn8Y9FzKbGJ2WQPyYQWj3p3NPNIOB0oyWUxjv_qF4SwccnsqUpdHw_5i1fvQfz7V8JvTy0Bn_R8iLC-tAu0p5qfxjKsw0Ti8qKDpEpgnfqf-vNcrYk42ecAbOQOkpbRhNrCeLcLCaOt9g_HmOgylB86zUaDqWwObVWYfI3Azo73WNUrVUx6p3gCwMAJhosY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رجزخوانی مرد عراقی برای ترامپ که در رسانه‌های عراقی بازخوردهای فراوانی دریافت کرده
🔹
در هر دورانی افرادی همچون امام حسین و یزید هستند؛ در این دوران امام خامنه‌ای شهید، امام‌حسین بود و ترامپ، یزید زمانه. کودکان ایرانی که شهید شدند، ادامه‌دهندهٔ راه علی‌اصغر شیرخوار هستند و ما خون آن‌ها را فراموش نمی‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/453758" target="_blank">📅 22:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453757">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/132371cca5.mp4?token=R76eK7GoretdnaD8u60LnB2p1pD0IDXNNShU_otDbeh1_miJngrP_nDvttpgkE4VVaLKS9UG5z-j5GhYRLV7_5gq8x0eoTJKffFer3fA34f0ohKRgTWtDBM8CtPpHSf7RAX-Ha7Y-31LKKo_75dvXCrchY41KI-uo1XJT7kTlHOR-c5vuSy8OVDLt-XarJzvIhAifZRnA59vmjH0F1RiMbpYMFiItWOf1ZX_FrCvcofg6jaDBV3Ge7evR9_RRsgbqeIl8a-rDf4l5l0FX785kJp9H4Xz6L173VJdkGrFUVFtd3jkj1-Fm2VUiriqI8hnx-g0d10s5imfk14p7FK2lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/132371cca5.mp4?token=R76eK7GoretdnaD8u60LnB2p1pD0IDXNNShU_otDbeh1_miJngrP_nDvttpgkE4VVaLKS9UG5z-j5GhYRLV7_5gq8x0eoTJKffFer3fA34f0ohKRgTWtDBM8CtPpHSf7RAX-Ha7Y-31LKKo_75dvXCrchY41KI-uo1XJT7kTlHOR-c5vuSy8OVDLt-XarJzvIhAifZRnA59vmjH0F1RiMbpYMFiItWOf1ZX_FrCvcofg6jaDBV3Ge7evR9_RRsgbqeIl8a-rDf4l5l0FX785kJp9H4Xz6L173VJdkGrFUVFtd3jkj1-Fm2VUiriqI8hnx-g0d10s5imfk14p7FK2lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازگشت زائران از مرز مهران با بوسه بر پرچم ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/453757" target="_blank">📅 22:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453755">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۰۹.pdf</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/farsna/453755" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۰۸.pdf</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/453755" target="_blank">📅 21:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453754">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7590dc25b1.mp4?token=ddUaEccCKgJyfVswQHay66G15FxvJKgLR1MvvAamdUbq1ebr1X-9J-IfFFSDDe89Z8VvDv5ZujdhnLR0o4R4Ao_yppTGuM8IhNylj19qf2MzlvsPyJp_xPWwFQmn9vTGrw3vtJwnFiIpQfd9JIE-_bCAIFTSrkgRjb7PVZX8YdaE_HAnDFsR6VyNZQ_dtRyAgBL9qxH4qBgsXp0XcEDiQt8rnqfHYofz_QnxlSKIuhU6DILFFCzqiO2cF2pHp8eTqd1IN1a1dMtCjdRKIYdTHrujtJLa2_lbp7g8qyeyV_mtS2vpAM8UZEvM7w5lRt4vQtqjoMGQygEIIow_iGsIMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7590dc25b1.mp4?token=ddUaEccCKgJyfVswQHay66G15FxvJKgLR1MvvAamdUbq1ebr1X-9J-IfFFSDDe89Z8VvDv5ZujdhnLR0o4R4Ao_yppTGuM8IhNylj19qf2MzlvsPyJp_xPWwFQmn9vTGrw3vtJwnFiIpQfd9JIE-_bCAIFTSrkgRjb7PVZX8YdaE_HAnDFsR6VyNZQ_dtRyAgBL9qxH4qBgsXp0XcEDiQt8rnqfHYofz_QnxlSKIuhU6DILFFCzqiO2cF2pHp8eTqd1IN1a1dMtCjdRKIYdTHrujtJLa2_lbp7g8qyeyV_mtS2vpAM8UZEvM7w5lRt4vQtqjoMGQygEIIow_iGsIMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط اف-۳۵ آمریکایی در سن‌دیگو
🔹
یک جنگندهٔ اف-۳۵ در پایگاه هوایی میرامار سن‌دیگو دچار سانحه شد و بقایای این جنگندهٔ بیش از ۱۰۰ میلیون دلاری هنوز در آتش می‌سوزد.
@Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/453754" target="_blank">📅 21:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453753">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515709c4e4.mp4?token=Sx-3evW5GPVBEbxQPZHvg04rbisxLKXBS_7S5hrOzZtxOoiJRKEyR7rRS2wZgaAwLCLdV2RHIvGGeKpvJ3Q160RxhQ4w0EpXCLBmeBAcn4vZQatR9LFIRG1Kpq10y4ydPuE2uXJnwPovdHsAkmIDmkNP2h-Dyqv54JcBqiLB3eZVce6PJZ84DnA3JZJrPcehUF33BDhlqkIuqiMi3arwCDFFYIvda4jnb7LoaipIxHjUiixH1F2I6QnfF2GM7WnsQ4O7wJGVHxUJfZHtsu94hqnYsxTrU81-B_28BRLDEoLPwO4HcTnJRBwU1zp-9vaaKJqcPaMugr9hqkjC7acPNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515709c4e4.mp4?token=Sx-3evW5GPVBEbxQPZHvg04rbisxLKXBS_7S5hrOzZtxOoiJRKEyR7rRS2wZgaAwLCLdV2RHIvGGeKpvJ3Q160RxhQ4w0EpXCLBmeBAcn4vZQatR9LFIRG1Kpq10y4ydPuE2uXJnwPovdHsAkmIDmkNP2h-Dyqv54JcBqiLB3eZVce6PJZ84DnA3JZJrPcehUF33BDhlqkIuqiMi3arwCDFFYIvda4jnb7LoaipIxHjUiixH1F2I6QnfF2GM7WnsQ4O7wJGVHxUJfZHtsu94hqnYsxTrU81-B_28BRLDEoLPwO4HcTnJRBwU1zp-9vaaKJqcPaMugr9hqkjC7acPNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده عملیات هوایی حمله به پایگاه آمریکا: به ما گفتند که دو گردان پاتریوت در مسیرمان است و هیچ برگشتی وجود ندارد
🔹
برای جلوگیری از رهگیری مجبور بودیم از بین دره‌ها با ارتفاع‌های کمتر از ۱۰۰ پا و ۵۰ پا پرواز می‌کردیم.
🔹
وقتی روی پایگاه آمریکا شیرجه زدیم…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/453753" target="_blank">📅 21:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453752">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4c1af480.mp4?token=HVgA3jnTFZdspoOwMjaQH_AeuqFwCHCk5CfTqWL2iwaT2LoLsG6eaeJcdxeCdkNn3HRKPoCbmzIk_ZWFpAkd9bvZKQi5U69AvRUE31MHKWzy9VX3O6v17iopOmvstHK0IRmtZ2E0jxUStRt6bYAQgvixY_7bVLExpnBz0vm6JtZr15fqovlQUOPpLCVKhhd9uhwsakAC7M9yXAgqruzYuhr0f6IoKBr39kLaUrXWeD-GStxjELmGcBbqIN1EE6AUC60cNYW2mEovX60_TK1SUool9ako-6oTr1vyKJug0MUWXgJmBhLVZbRs77yMjkxc9tzl60EPTERFzfEU3LxRlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4c1af480.mp4?token=HVgA3jnTFZdspoOwMjaQH_AeuqFwCHCk5CfTqWL2iwaT2LoLsG6eaeJcdxeCdkNn3HRKPoCbmzIk_ZWFpAkd9bvZKQi5U69AvRUE31MHKWzy9VX3O6v17iopOmvstHK0IRmtZ2E0jxUStRt6bYAQgvixY_7bVLExpnBz0vm6JtZr15fqovlQUOPpLCVKhhd9uhwsakAC7M9yXAgqruzYuhr0f6IoKBr39kLaUrXWeD-GStxjELmGcBbqIN1EE6AUC60cNYW2mEovX60_TK1SUool9ako-6oTr1vyKJug0MUWXgJmBhLVZbRs77yMjkxc9tzl60EPTERFzfEU3LxRlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدون‌تعارف با دلاورمردان نیروی هوایی ارتش همراه با تصاویر منتشرنشده از حملهٔ عقابان تیزپرواز نیروی هوایی به پایگاه آمریکا  @Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/453752" target="_blank">📅 21:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453751">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🎥
بدون‌تعارف با دلاورمردان نیروی هوایی ارتش همراه با تصاویر منتشرنشده از حملهٔ عقابان تیزپرواز نیروی هوایی به پایگاه آمریکا
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/453751" target="_blank">📅 21:07 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

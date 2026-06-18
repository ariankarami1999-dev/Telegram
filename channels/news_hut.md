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
<img src="https://cdn4.telesco.pe/file/v8PzzxOhu63Ov8gWZOYVU5XEFB8I1Z4hdBsEm4_1oC0ucECtjQETqvyHUnSn_yVwAa34DdiKiE5xLQDaQVkD0w_biQgmBK4-BGx0zxBSOTfYOCN8v2-J-LyuJkdzLEmZ1ZNWBsIIpDlRZTbJitdfg-U4-n_XcFUq4EzlKYb1SAfDf-D8QJNFyCGABOtPDItlJ0r9MQNnaeNAQqrdFA-1Ok7e0ygyyPOEXfceZPvzYVSy7n-VdrhWts68XkcF_vOiweg5IWyhhzQzV6WV5Ise40vNrOTYsbwKan6TX5RYHX0AYx-y4mvnU4TMjmVTM6IboyhP_Ieer1YDDk53r-_QXg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 223K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 17:57:40</div>
<hr>

<div class="tg-post" id="msg-66432">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGmNRpuCsFSi7AGSfZTytcknBCI-BJbe5Zr1v62AE0CQM1g-vHcZPApcHsxWNidbfOTU6OgmSdFUFGEhZ6NImoM9T695iO8i_tQkmWwQ8vhpmlgkYt48fRM2W3r16Wb5lFQxWkHeSzXjV6vPs0hqpP1ssrtTPnF1T_-48ynnUqcFGZq-TovohedG-Jso44L6bI7sTWU-JCyLU7XaYK_BkuiqSCHyvhO6kxYeUiXVr7UFvCS6fs91ykVwLnVmYIsQWFrt-Z43f76GqpWX4zoSdoFal-y-ynrPnLb21RrSFR8UrSIGYq2jDg4QIGqR1sxyT3GwC3g8cOzv4yHMjwknRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mpy5lw7UdiS3Ytv_erCydNIMwxbcc9wKVqnZnuWbyn6jtgkEKKrvETP0yz60MEa5NvkOabJNJ2Br61lvEqYg92ISUtN6xPFsRAACTgCKt0f9HwycnDC5Lmtb9BH92SqcY85iI0VogYsNFrRuZ85GcbRnQkfxU6-jRaCJOak8JezdeyUyAS8wPWjd_kOz2x0fXk_wIAjzqjK4GXCYK20AtaIZ_HCUifw33c4cVQ3TVEeI7xJOVnyVLPegVYeUtYPU0teT5qswB9Sr15O1fS06N3CZ6eMy1obOdAeZjg7KwumCntJaWgaL-kZ15dZlW04XlD7KbikMKZ8c7krxDxx-UQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13c6e64c5c.mp4?token=NVBbkKC4xTo6btyNpJPS0PTCLP5M0F-D-JLHLrRYQ0embx9sh0y2qZCDeBKjSsP8q7bMi_CNgzygoQywXxA3L_adczDdrIL3vHRQx_9KxxMK8NffdRwCt83Tjq8I6VkDlNgbyXg_Pex2cvi7iHlAspKzlSVTZlznRyiZYx0vx1HTCI-mhYLg-w8B69K1sOmSdIwYZRd6CqB2Z8xptFD-K5UfsYdl_HO8ejp8LdQplEgY8YaN4VUZDsdZlTRVCcpR_raBSqD1JeMcG3UAa2CGv3DOauTeJfKK6plfuyhOlVYFQdBa6dXmvL8dwaDXCMSoN1u38GobHUJdFn6jRkFFXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13c6e64c5c.mp4?token=NVBbkKC4xTo6btyNpJPS0PTCLP5M0F-D-JLHLrRYQ0embx9sh0y2qZCDeBKjSsP8q7bMi_CNgzygoQywXxA3L_adczDdrIL3vHRQx_9KxxMK8NffdRwCt83Tjq8I6VkDlNgbyXg_Pex2cvi7iHlAspKzlSVTZlznRyiZYx0vx1HTCI-mhYLg-w8B69K1sOmSdIwYZRd6CqB2Z8xptFD-K5UfsYdl_HO8ejp8LdQplEgY8YaN4VUZDsdZlTRVCcpR_raBSqD1JeMcG3UAa2CGv3DOauTeJfKK6plfuyhOlVYFQdBa6dXmvL8dwaDXCMSoN1u38GobHUJdFn6jRkFFXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پختو پز اوکراین در مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/news_hut/66432" target="_blank">📅 17:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66431">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bf3ba597d.mp4?token=RL6fttWafvWD0G-OeeJOKTBniBl9kAaNIQhejhvKH78WsJC5tWD_Zc3L1W-dP3W1LcfnVVg9-NA9ezi8TOlj7myu9q3lspmWUE4vtdSOnvFEeFBGSpq6NUQvho7hymIKxhaGynWjbX9_MxY-RZ2eS807dBgv06QNGNi5SG_duOzRJMEj_J2YNKxkx9HuSX3KMFptm4j5VkkhoHwPMUbM-NLksB0Kh05trC2615k8JxTeJfVUKZHyRbg7kKRKFKQG73u5EVpsljcXT_w8kHHiXkKuIStFyV6YtU1h1OfAuRgH7iD_Q24Xy525p9jWwHMLVnnS3CefiHlSLdEfOZIUJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bf3ba597d.mp4?token=RL6fttWafvWD0G-OeeJOKTBniBl9kAaNIQhejhvKH78WsJC5tWD_Zc3L1W-dP3W1LcfnVVg9-NA9ezi8TOlj7myu9q3lspmWUE4vtdSOnvFEeFBGSpq6NUQvho7hymIKxhaGynWjbX9_MxY-RZ2eS807dBgv06QNGNi5SG_duOzRJMEj_J2YNKxkx9HuSX3KMFptm4j5VkkhoHwPMUbM-NLksB0Kh05trC2615k8JxTeJfVUKZHyRbg7kKRKFKQG73u5EVpsljcXT_w8kHHiXkKuIStFyV6YtU1h1OfAuRgH7iD_Q24Xy525p9jWwHMLVnnS3CefiHlSLdEfOZIUJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد کشتی ها در تنگه هرمز پس از امضای توافق
@News_Hut</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/news_hut/66431" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66430">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XItwumGMDwcydpWj8T0NxamqJfLOvtkYqIu_jYiYZVEaeeT5Mq8fjDqsxIokzCjdRwQLIFi8ggz7-oExapo9TLX-8I8jX8kk0Mit47Wov_xtGjcfDFEkiuMIvRXdw-0IdurmPDX0yyWhyNsH22H9ZtXFj85VBK8WHba1cy5gjdq0wdtxINTUgU3dlIvpCyyHJT0VGM6eUQlX1Mxc-Cd7R40c6Aj5wMfdac-INvR2tFoRAx-5aupfui-AihBTqSaJpP8lGsbZo6GLYecJiptQy7vNSK95ZcEQoEuW-4y2REteeaGm5S4pqh_99qTZhVa69v-gsnl-PQHDxSdQ5YvxGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ارتش اسرائیل؛منطقه امنیتی فوری در جنوب لبنان:
نقشه منطقه‌ای که نیروهای دفاعی اسرائیل در جنوب لبنان در آن فعالیت می‌کنند
بر اساس نیازهای عملیاتی، نیروهای دفاعی اسرائیل در منطقه امنیتی واقع در حدود 10 کیلومتری داخل خاک لبنان مستقر شده‌اند.
نیروهای ارتش اسرائیل در منطقه عملیاتی جنوب لبنان مستقر شده‌اند و به تلاش برای از بین بردن تهدیدها و بهبود دفاع از جمعیت شمالی ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/news_hut/66430" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66429">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFEl8X_4L3vWxiHXcQ1g7XelgTj0ekjIqDgJKbAyPx6ylvlDxdIjNC5tYkNNoLJFSljU-lB5_qtBUFnJCgPpx1CkUZeqL2aJP6qPv_KJEtMzybF_qP613zp9BhKtLKo18Wfk63VJx3BaYHVcm3VU4P_Vr21W9BrP4734uGRtWuD9UrAgRPlDo5VGMVmJ3mh_Ts0XkVU1FNN-TjoYTdFOntBSlh24-0G7-eyhzUVi3vzyRRTC7vtvX3VycGNZmFvdpeDP85djZHWPslEMw0KQsEK0Qmsshwo6bfzHwsOcDWK4p6FtQVXDXHoBIMj_bX68gjHODzuSOeW-sB5LI217zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان؛این یک سند تاریخی و پیامی از ایران مقتدر است:
صلح در سایه احترام متقابل تحقق خواهد یافت.
جمهوری اسلامی ایران به صلح جهانی با حفظ عزت و استقلال، پیشرفت و همکاری منطقه‌ای همواره متعهد و پایبند است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/66429" target="_blank">📅 16:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66428">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622db6728d.mp4?token=gtWnFjzNDHDfIpzEotTKx_JBicrSnbLtRYepdU2Ihb5ykBqubzuvAmbO7nd6GSOZYf5-BvPtiGwZuEFGmhfoBuY5z8yIj6eomrQPPg28b6AK8kSB07Eq--MlgawE_J66-WD3di4Lw2dw9_WX8bofVmf4XRzC1ueKgiQsQcyxW8ykWha6EeZEuNmKNAUFgMTVUOKka2L8YJ92ejOnA42W7_Lw_ms0WVabrxUx0HNMJhnUv9u3jkrriR1W2vkNKTv9NFNLqq21Rk5UktoB70zPiXHlQqR1gWMhjNWSzEKH3frjVDd6XxPDIveDt2nxToZNhmSraXW9vUt5SUM-UshXLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622db6728d.mp4?token=gtWnFjzNDHDfIpzEotTKx_JBicrSnbLtRYepdU2Ihb5ykBqubzuvAmbO7nd6GSOZYf5-BvPtiGwZuEFGmhfoBuY5z8yIj6eomrQPPg28b6AK8kSB07Eq--MlgawE_J66-WD3di4Lw2dw9_WX8bofVmf4XRzC1ueKgiQsQcyxW8ykWha6EeZEuNmKNAUFgMTVUOKka2L8YJ92ejOnA42W7_Lw_ms0WVabrxUx0HNMJhnUv9u3jkrriR1W2vkNKTv9NFNLqq21Rk5UktoB70zPiXHlQqR1gWMhjNWSzEKH3frjVDd6XxPDIveDt2nxToZNhmSraXW9vUt5SUM-UshXLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بعد سه ماه هرشب توی خیابون موندن و پرچم تکون دادن ، بهت میگن اقلیتی تندرو و خون رهبرتم پایمال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/66428" target="_blank">📅 15:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66425">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4faedc1ad.mp4?token=plV2bf25e_WXFgL6s3sOwJjTlO37xaKk8ODBlJphUhCrupfnh80zEKjij7gGw_smJQr9Y8jbVc6iRbl_CdeDoHbUuTWCbwMxy9m6hQXnObHaioMwRqUjDKq_JelW3cX4tReZzYc-NUJA56-KPpohGZxaSRKz4422AHT2vrphEVFOYTOdRTvC4qdcsXbLMWZNJFHfvpXzFBTz2L44L8UqVCXQLlZknzuiNHyIlEcSVRb97o6CPR_HAA4nbnVCFzNKXd7etUttJX6KSpCuCr9Wf1pRCT0EaordpJbPYH_hpylbFOvI7yFk92YfkKn80OInSjX-0lJSL8h--NtxvbxUBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4faedc1ad.mp4?token=plV2bf25e_WXFgL6s3sOwJjTlO37xaKk8ODBlJphUhCrupfnh80zEKjij7gGw_smJQr9Y8jbVc6iRbl_CdeDoHbUuTWCbwMxy9m6hQXnObHaioMwRqUjDKq_JelW3cX4tReZzYc-NUJA56-KPpohGZxaSRKz4422AHT2vrphEVFOYTOdRTvC4qdcsXbLMWZNJFHfvpXzFBTz2L44L8UqVCXQLlZknzuiNHyIlEcSVRb97o6CPR_HAA4nbnVCFzNKXd7etUttJX6KSpCuCr9Wf1pRCT0EaordpJbPYH_hpylbFOvI7yFk92YfkKn80OInSjX-0lJSL8h--NtxvbxUBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات سنگین اوکراین به مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/66425" target="_blank">📅 14:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66424">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92b0722cb.mp4?token=MK8nQH1OIYmj_2DOSI4QGOEqTN-2izHtnEPY92uDptApHNV03XKQhdSdxsHdzPOrGWMzOtpapbYM_2osqa6GQFlqBcbGJbB7db9COQfHIkq1OBG429ZWfAl6utwZ3U1lyhgjBrM5j7qIGL2tf3yAGREr-DoaZqIvy2r4xwAkHkDFsUX5rYbvzLKk8yGr09FsMwYfzb-XiaDtLZZKy5Nb0wtoJSGK1e1GHyFaecNf1V7VTozeV4B05prVGsXmK-oHQ5Tqzv5qo7o5OYSZMpL2it2ThvYay5JoKm1JPbvtFgUogv-YU0DVfceKXcgvtti3i_JTeyB9b6O_hVGQy7kvLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92b0722cb.mp4?token=MK8nQH1OIYmj_2DOSI4QGOEqTN-2izHtnEPY92uDptApHNV03XKQhdSdxsHdzPOrGWMzOtpapbYM_2osqa6GQFlqBcbGJbB7db9COQfHIkq1OBG429ZWfAl6utwZ3U1lyhgjBrM5j7qIGL2tf3yAGREr-DoaZqIvy2r4xwAkHkDFsUX5rYbvzLKk8yGr09FsMwYfzb-XiaDtLZZKy5Nb0wtoJSGK1e1GHyFaecNf1V7VTozeV4B05prVGsXmK-oHQ5Tqzv5qo7o5OYSZMpL2it2ThvYay5JoKm1JPbvtFgUogv-YU0DVfceKXcgvtti3i_JTeyB9b6O_hVGQy7kvLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏جی دی ونس در مورد مسلح کردن معترضان ایرانی:
در واقع تا حدودی دشوار است. می‌دانید، نمی‌توانید همین‌طوری از آسمان سلاح پرتاب کنید. واقعاً زیرساخت لازم برای رساندن سلاح به قلب مردم ایران وجود ندارد.
یکی از چیزهایی که رئیس جمهور خیلی نگرانش بود، همه این معترضان بی‌گناهی بودند که توسط افرادی که چند ماه پیش مسئول بودند، قتل عام می‌شدند.
آن افراد اکنون رفته‌اند. اما خواهیم دید: آیا این رهبران جدید با مردم متفاوت رفتار می‌کنند؟ مطمئناً امیدواریم که اینطور باشد.
و اگر اینطور نباشد، می‌توانیم وقتی رفتار واقعی آنها را ببینیم، بفهمیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/66424" target="_blank">📅 14:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66423">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uw872ibYpjMJoSRZEuRV5LmU_jErSt1HQn0mGTvFhYwF78SHm7x-rVvyrl3doHMNn2mXmEIVr_Escqys5s0LVeg3Mo-cVgfz50UcT4TSP5JUN-Z5I_h-xb4nAMrc2D2dVJjrd2zNnnZZnBONPLjJHVZjEhFNWF2mxLTEV69KXkzLIQ4dO5FyIl9teE_mVIaD-F-4tnoQqNCtefRYY2N3tgVHOJC1MFh6Kc_MRJTXZH2F2RyQREuFC9tVtCgf3WdesSzBHcMik6taKSTEpeYocmhpNM9OdaziP6e75MMNGDGREE-UWgtlwPHxKL7ov6wsARSehdKeLT8B2vgmXJzWGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حملات اسرائیل به جنوب لبنان همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/66423" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66422">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66422" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/66422" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66421">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLgi1N-_1djW0HHzwd3kZ3WU4mIBG5kPplN35-CH9DTx6l_o1mJZpKa-MQyTj2h6jFnYr4PRk3vK-pxGJK1GPR8NTd7yFE0JpqtQGK5rqIDP65uNZUf2CAeJD38ogV6EXGglfwJESnr0_rsYLH5mBhH0Ym9d4Nd3b7JwlpNmK9nVRHTwxjaPC5E2AhNfBbaAnxFvM5fJ0_DfFMCnxUY1xPIuhXjdmRM0Id35DR0MeqtHJAWgrYNQ0KjrGfFo24jNvKpKQ_kKqrY_rbTQOLSOyIlrRaRtrKxqeDGmYNDe-kH6NDov-XaRhGIyFQ3O1PPMuIjoiZwteS7y-6oNt7R3VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/66421" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66420">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZUv8dTG9ngk2piIBTJbnZQ7taen2jP-TTHzhSdAvtLWUYhMbf0OKMhplwudhckKNs-45VRqCjr5WkP-GHHIBguCGZP6gPqjGk4xkAe_nh4evq3MrN7KhQmQmInuC_L1S6UtB1aBPR8wEUIfbIladax6bE2t9i9UPYxQeBvEKVpOvQW8N-wIod7YYKnJRS-7uosZiircEemgfmon9eIdNABcfVXjnS0iU4snoy_XyyybBhW1stvW2HZRlxVCJvAWfQoSpvLRAXhsFKQEqzg5phQvyq-f4F6Z_7foNUJAKx4vFhQsGuzVJDlEM5LVBd-IXlq-ntavyuB17XauwtUmnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امضای پزشکیان از نزدیک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66420" target="_blank">📅 13:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66419">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1890fc432.mp4?token=Oox6I3GNtMkCy4biwbIjycAJFAmF-z5NwHs1aiDwAHw_L9Wp3qRU3DIhc4K3fA47ZEoRwfIgpkcPlEwOFzd50Qc6O453atqm9xvXIejaFaKLk_4qZh_xSDqLlc3wMJB7Wev_zV5ArTinj1rZp5yph2Q8gV0016eVps40QFOgc8ZZOTu9-WwvaqN-Q_70orMwyukJoCfSpbBP5NaLJCqSDdKpWAtz_2U_vBupkM2fHD3m6NLnCUdU5ARfGJybJxFsNscJHVeCX_h5V-z0ytjVlcnJTiwqXBjodI7rBnAafW7hFZnixCsL0HL4Lmcj2Hg2AdlSEJ8fYUKjG70ue8cq5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1890fc432.mp4?token=Oox6I3GNtMkCy4biwbIjycAJFAmF-z5NwHs1aiDwAHw_L9Wp3qRU3DIhc4K3fA47ZEoRwfIgpkcPlEwOFzd50Qc6O453atqm9xvXIejaFaKLk_4qZh_xSDqLlc3wMJB7Wev_zV5ArTinj1rZp5yph2Q8gV0016eVps40QFOgc8ZZOTu9-WwvaqN-Q_70orMwyukJoCfSpbBP5NaLJCqSDdKpWAtz_2U_vBupkM2fHD3m6NLnCUdU5ARfGJybJxFsNscJHVeCX_h5V-z0ytjVlcnJTiwqXBjodI7rBnAafW7hFZnixCsL0HL4Lmcj2Hg2AdlSEJ8fYUKjG70ue8cq5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظه امضای تفاهم‌نامه توسط شهباز شریف نخست وزیر پاکستان
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66419" target="_blank">📅 13:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66418">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fdfa7aaf.mp4?token=smoRAa-ik6AL-anpBw0K-K7kGq4fh86ieKEPYPjbSL6B3vJtSU_jvzt04FWWf7tOhyBV1B-dYUvR6aRhQUNHUsDIpuDx_o4QT52f563nEWRETLRGouscImHAKldGGY_vrg7U-gmLVcUwUVCp8XqrQwX7Pxo076iuSDqhv2M-clJlWDRwLEkA57ZHmYY2o9TmsQISFvtk3gjk_yNjm34XgGFUsdDj-LwHDXx196_yr9S6Xm3O7Z9VIeLRBQcIfHRPIJfoiPdUI3bJzDQl6QQQd_H1iHP65u_LcysjINWb4ntpXFRZIehNwCQUlpOcJ5mOValx9rsjvgqSOE_0FHziMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fdfa7aaf.mp4?token=smoRAa-ik6AL-anpBw0K-K7kGq4fh86ieKEPYPjbSL6B3vJtSU_jvzt04FWWf7tOhyBV1B-dYUvR6aRhQUNHUsDIpuDx_o4QT52f563nEWRETLRGouscImHAKldGGY_vrg7U-gmLVcUwUVCp8XqrQwX7Pxo076iuSDqhv2M-clJlWDRwLEkA57ZHmYY2o9TmsQISFvtk3gjk_yNjm34XgGFUsdDj-LwHDXx196_yr9S6Xm3O7Z9VIeLRBQcIfHRPIJfoiPdUI3bJzDQl6QQQd_H1iHP65u_LcysjINWb4ntpXFRZIehNwCQUlpOcJ5mOValx9rsjvgqSOE_0FHziMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیرزن کسخل مکرون دیروز موقع عکس یادگاری سران گروه 7 نزدیک بود زمین بخوره و شانس آورد ترامپ بغل دستش بود گرفتش
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66418" target="_blank">📅 12:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66417">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">قطار پیشرفت آموزش و پرورش کشور خدایا شکرت   @sammfoott</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66417" target="_blank">📅 12:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66416">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgGBba6OaRmlo_ftAL7LnLEzvBvwfningnMk2gWSkq5Ne0TDOQEHHqjTn7VSNt-G3Dml9WbYESg6Ga3-kNf_aaYkFXxLvkLlk2Cvfu_-RkvXZ1qBh9WPbPDG41aLaue2SVvwqxc2ySf7hzwVuMUhIw-ORQj5grfdCRAiv-gcjF6oyl4MkNNZ_hwCuuV32sFMEg_zsSPBUKpnjtYkrKhPmB483rBcDmPQznwpkQV55QbTZm66vJHkJ-TDAwTSPcGRvkE2nt5Kn4Vae3d8AXqcqFzTQ7W1ekgR6nUkkt3p8NbMDKSZyT74r9hWXElHyVeMhjxq8CIa42NQJom0k-Lzrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«این احمق‌هایی که فکر می‌کنند من با ایران به اندازه کافی قاطع نبودم، در حالی که بازار سهام به تازگی به سطح بی‌سابقه‌ای رسیده و قیمت نفت در حال «سقوط» است، یا حسودند، یا آدم‌های بدی هستند، یا احمق. بیایید دوباره آمریکا را بزرگ کنیم!!!»
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66416" target="_blank">📅 12:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66415">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16c0579b45.mp4?token=r30Vxe7y8o7N3VrRVu7LAP_wTc4fJZQQi4ZOrrh4l1yccF8rjCcfMnicARTfVX4M5EI21R0UC_U2E2QwliwgKoKs2ErUqxBNG6odgxEDUbo00mmboOsmdKOTRHKNYHx4kbz2gxiqh-tftpgC6kJS0XavJl3WmQYR6w-nCRFbLP2M4VEqMaIfC9qNU1Pe4BfAHQxZHq8ZsEvyVEnheKWWkJ33fcgOLt_jKAgk6kWfY_hhTOe9ygtIlD3em4crcqJDVB5PD6qxECJUmAW9yXkG3smX9lgqeK9_rh_uSoJO2CID2z8yf7PmZHE5nvfI-pEY9VgyOO1BKvlKxv9oPDY45g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16c0579b45.mp4?token=r30Vxe7y8o7N3VrRVu7LAP_wTc4fJZQQi4ZOrrh4l1yccF8rjCcfMnicARTfVX4M5EI21R0UC_U2E2QwliwgKoKs2ErUqxBNG6odgxEDUbo00mmboOsmdKOTRHKNYHx4kbz2gxiqh-tftpgC6kJS0XavJl3WmQYR6w-nCRFbLP2M4VEqMaIfC9qNU1Pe4BfAHQxZHq8ZsEvyVEnheKWWkJ33fcgOLt_jKAgk6kWfY_hhTOe9ygtIlD3em4crcqJDVB5PD6qxECJUmAW9yXkG3smX9lgqeK9_rh_uSoJO2CID2z8yf7PmZHE5nvfI-pEY9VgyOO1BKvlKxv9oPDY45g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط اونجاش که یه موز و دوتا پرتقال بود
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66415" target="_blank">📅 12:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66414">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb19ef0a8a.mp4?token=joR1uzloC7Lo0h7pYOySDEhNelCQfvoPTyFF3xWiXh6RQmPBq_gypfegU354kC0krhiKvesrEWeLDONV6nCdvO5mjd2d0iMdMm7ua99B_QXk_NcOTyjNU8nqXTUEtpEI3o7USKitJ9nk0wLQx0u2typdIh6JvL05ia5w6zuPrrD0bWi7SBTxrNOdUi4aJUOmHT_7DW6epmwOht4yZ-tezuAoeHTvgHCPNxarpz7ksemS0nUSqYhRvgmGilcyGxkOaWfd27qKjpLq-L4G2e39g0B0aHICZGk9IpE6-lNAtZysmyZkpNfI7VxzkfMTBWOcbF-KqT3rQOQKKj01eqYptA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb19ef0a8a.mp4?token=joR1uzloC7Lo0h7pYOySDEhNelCQfvoPTyFF3xWiXh6RQmPBq_gypfegU354kC0krhiKvesrEWeLDONV6nCdvO5mjd2d0iMdMm7ua99B_QXk_NcOTyjNU8nqXTUEtpEI3o7USKitJ9nk0wLQx0u2typdIh6JvL05ia5w6zuPrrD0bWi7SBTxrNOdUi4aJUOmHT_7DW6epmwOht4yZ-tezuAoeHTvgHCPNxarpz7ksemS0nUSqYhRvgmGilcyGxkOaWfd27qKjpLq-L4G2e39g0B0aHICZGk9IpE6-lNAtZysmyZkpNfI7VxzkfMTBWOcbF-KqT3rQOQKKj01eqYptA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
با همچین عزیزانی تو ممکلت هموطنیم :(
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66414" target="_blank">📅 11:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66413">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6af0a234cf.mp4?token=fVQ80bg3nn6ms4bj_gkHCv65704WVDpuIE4OK1QYB-TwqfyRB2YnHmz8YAqSEQdK7hv99TNu-twZN2fQvXOO2BfLiu5pz1W9wlpC4tWEzW0NIzKuezShKsS7FrSCh291W13SGMDjl-Mk_ohPmwTU_ef1SKfIPjV-3AN4NcqTlbPAJaDGYrhJOOZOJhMG4cyYSVuKBM0JU7dcdirqqruoLpZS4HMpuaomLT6kze0DIhMkwZKifv8KLHW3xzEpiKtKZ7HPaSjSPk4-4XYKnYu9j3nrJG4iBr4sCZ7vWfntNXsV7x-XsOcvHolUc8nGrtchyAw5KIasfsP89cAuqrjsuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6af0a234cf.mp4?token=fVQ80bg3nn6ms4bj_gkHCv65704WVDpuIE4OK1QYB-TwqfyRB2YnHmz8YAqSEQdK7hv99TNu-twZN2fQvXOO2BfLiu5pz1W9wlpC4tWEzW0NIzKuezShKsS7FrSCh291W13SGMDjl-Mk_ohPmwTU_ef1SKfIPjV-3AN4NcqTlbPAJaDGYrhJOOZOJhMG4cyYSVuKBM0JU7dcdirqqruoLpZS4HMpuaomLT6kze0DIhMkwZKifv8KLHW3xzEpiKtKZ7HPaSjSPk4-4XYKnYu9j3nrJG4iBr4sCZ7vWfntNXsV7x-XsOcvHolUc8nGrtchyAw5KIasfsP89cAuqrjsuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
برشی از سخنان تند شب‌گذشته قالیباف خطاب به ارزشی‌ها و تندروهای کسمغز
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66413" target="_blank">📅 11:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66412">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04da6f24fd.mp4?token=lEfrVQXeGv-RNJ6qcQUqE53NWscNb1RECFu_B-3zEZi1Lh1ET6xjRKuanIEZENapz_QhnxhAbJVkVP_Ek3vAf-fgFzIlfUQP2SzaElIDCmp29Wexr8OUA5WLLXZDmxNF0dqnTxJhorq4K0_dXJF-SYwGmRljVzlIFWLWJMGwGHDhIsKOrL82HsmKoyUMpxxTAr-pATqUQ2A_zY9mz8szb6IBeIYn8s-bgj8yfZeRQfhk6hcF-Lz0mUxplGtw1HInDiH6owSq9s9OiG-pVxi78sb_VK6IHU4CLc_BN8z4kmE-pkX6U4e-IC2KHkquNULXRKIlaNJVa4dFeGhj0iWWvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04da6f24fd.mp4?token=lEfrVQXeGv-RNJ6qcQUqE53NWscNb1RECFu_B-3zEZi1Lh1ET6xjRKuanIEZENapz_QhnxhAbJVkVP_Ek3vAf-fgFzIlfUQP2SzaElIDCmp29Wexr8OUA5WLLXZDmxNF0dqnTxJhorq4K0_dXJF-SYwGmRljVzlIFWLWJMGwGHDhIsKOrL82HsmKoyUMpxxTAr-pATqUQ2A_zY9mz8szb6IBeIYn8s-bgj8yfZeRQfhk6hcF-Lz0mUxplGtw1HInDiH6owSq9s9OiG-pVxi78sb_VK6IHU4CLc_BN8z4kmE-pkX6U4e-IC2KHkquNULXRKIlaNJVa4dFeGhj0iWWvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66412" target="_blank">📅 10:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66411">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc5db481b.mp4?token=oXk7vLVA8TNaCORddxHZ-CHxkkiVDjjRapBRLlewqr_YWTjLwuJsU52wG4Pp69BadSqiXeVuHJUU7g8C04e9dcTMIDX6QgMLaSMtz2PD55fRP6R6Y8chOeqgnQCrShg2V9bRoZL3wWb5KOUVtmrWyqVRDRcqPJjDyC2E8sBruB3KwNBj_BAXjTzAC0bcD58zqq0RoVLC_f50eo-itwSbd1bMqw-hn9p32THm4kVTFfwXYkoWnzgNpoTxwB5mSt8Kw_HNPM9fABKBJKDGwa5-e9TPYAMDbsBHqDkDIVbwEqaIYEaHcy1uQogEwl67OJrK__2QlSoU4AA1YYTK_U1JNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc5db481b.mp4?token=oXk7vLVA8TNaCORddxHZ-CHxkkiVDjjRapBRLlewqr_YWTjLwuJsU52wG4Pp69BadSqiXeVuHJUU7g8C04e9dcTMIDX6QgMLaSMtz2PD55fRP6R6Y8chOeqgnQCrShg2V9bRoZL3wWb5KOUVtmrWyqVRDRcqPJjDyC2E8sBruB3KwNBj_BAXjTzAC0bcD58zqq0RoVLC_f50eo-itwSbd1bMqw-hn9p32THm4kVTFfwXYkoWnzgNpoTxwB5mSt8Kw_HNPM9fABKBJKDGwa5-e9TPYAMDbsBHqDkDIVbwEqaIYEaHcy1uQogEwl67OJrK__2QlSoU4AA1YYTK_U1JNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی عجیب دو سال قبل شاهین نجفی درباره قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66411" target="_blank">📅 10:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66410">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f1770ac7.mp4?token=ko_UF_Blnh8Lua6u-1sluIf9L0vFmEJRBNWeYCqoeB2ZeJHpUMOwZj4KHTlQMRLP1ROJYMS7nz4YPqMYSaYyAV217MBVysJCYtfQmfpZSAUWrpMILyCWbVbSQNaeHr1Oe0_Qxb-plPCiZgBVKiE1ZJczLAugCfran1nGPobI8oMwd2mq1IkpGZUYhYw1OeNmaUvtSO86G7TEQaaRmjAJTw7zk8s28sieaXvJlxHcV9qQIPb2zJVtWz62hmlbu-vae9TS7bbUjlSu_HqbLym5CbmBdfbEZcUmRWbNNYbvpCDZoctOgfDYXDij83ce5yRNXqViFpOk2uQgMxPyamUsIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f1770ac7.mp4?token=ko_UF_Blnh8Lua6u-1sluIf9L0vFmEJRBNWeYCqoeB2ZeJHpUMOwZj4KHTlQMRLP1ROJYMS7nz4YPqMYSaYyAV217MBVysJCYtfQmfpZSAUWrpMILyCWbVbSQNaeHr1Oe0_Qxb-plPCiZgBVKiE1ZJczLAugCfran1nGPobI8oMwd2mq1IkpGZUYhYw1OeNmaUvtSO86G7TEQaaRmjAJTw7zk8s28sieaXvJlxHcV9qQIPb2zJVtWz62hmlbu-vae9TS7bbUjlSu_HqbLym5CbmBdfbEZcUmRWbNNYbvpCDZoctOgfDYXDij83ce5yRNXqViFpOk2uQgMxPyamUsIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
10ثانیه تراپی روح و روان
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66410" target="_blank">📅 09:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66409">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95de07e4f.mp4?token=aY25ma_ec1fAxlAILYufLFjCQKDUfAi9ZfQORghAaChN-8kKAJZRa_-5cCGqaOYnylr8Sa7ePWSWWamej2JNgpbvdQDgvRwYGMPm2m_72ov-GwOtBvwC6vgms5bO-rbcZRzbHNnKW6S8KtJmdGKK7EqUNOKmidTL2dGGI7TuA9qgEQoi49WqGwgg7DMe6LFLi2r_lVlTuwUHrqrwS7nszoWfOYG7vMjDSRppTXhb1GF6to_T1fn1GhRIPvcgAQxSppBnDPBSpSFHNqh5CcM-Csx2yB_enhnG1jyZElZKxAfm-UsAaiIUzF6rQ3KsMkbM8BQUMZKTNs7ClrBgwn9eog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95de07e4f.mp4?token=aY25ma_ec1fAxlAILYufLFjCQKDUfAi9ZfQORghAaChN-8kKAJZRa_-5cCGqaOYnylr8Sa7ePWSWWamej2JNgpbvdQDgvRwYGMPm2m_72ov-GwOtBvwC6vgms5bO-rbcZRzbHNnKW6S8KtJmdGKK7EqUNOKmidTL2dGGI7TuA9qgEQoi49WqGwgg7DMe6LFLi2r_lVlTuwUHrqrwS7nszoWfOYG7vMjDSRppTXhb1GF6to_T1fn1GhRIPvcgAQxSppBnDPBSpSFHNqh5CcM-Csx2yB_enhnG1jyZElZKxAfm-UsAaiIUzF6rQ3KsMkbM8BQUMZKTNs7ClrBgwn9eog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: چه مدت نیروهای نظامی آمریکا را در خلیج فارس نگه می‌دارید؟
ترامپ: هنوز به آن فکر نکرده‌ایم. احتمالاً برای مدتی، جای خوبی برای ماندن است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66409" target="_blank">📅 09:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66405">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XclirMHnNPE9R583h4viXvbz7HW7Q38VvbEQbTGyYbC_BjT5jiXKfs3I6fmdKWZ6wBki7BB6T5CgISULXMk2kdzOqxCEGigC8IlFT_goZxGtVGVgvmHxnuTz2Hju-50FYu8OyZn1ZGjlTAXdSQXzp2ti0nxHspzgOMUApW5b1ParLuCdlFWOWxR1ht9MYsVwxrXsR8hgJ9SKu0tMZacPaoiAXUpLwRv9JNiF99fAL1Gsy9IsUCDGflvRJWm8w8JZjTGO_ric1M_zrTpmYLiQ0CMKSiF2WKKOrAc267yDNbtd0725NZffoDyPqqNF73SNErm8de8k0Sv0FUQ0ksFxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2zvO4LwLmrNzgQJsnup5OL3O30UtJLPwVd03F_O7sFwQ3FaQGCVWoUV6whj8kbED3AdKAB65GcYKnHnsXs259ykHGavUpQ_fJCvdQDR6WxLWW6z-LocmwVphYhKrG5ynXx2a3PgLeAwwxcochuu4ia5k-KHIRBoYfuUks9OY1QBIFDOdWvva53Tq15WA4wBoAz1xtaHFqy6svmVo3M5DQhHL21AwhQKRifNNCpEjYTIg5am9OS012ZqHkZCI2bou4zd7KoC7VbaaRNFvUZCMnSxXZem2dd809PPIwpg2wYaj0FlvtLA5_QAruRQjR4h7pB9IT2-opvWZM-u-wbsjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ElTazy-5BOPY7ylHRgF2hpz6dc3ouocGlEmiFeDWRW_7dPAGcRBqqN0FCQVE3USmf6BXm8fLRWV2DZtoSygb8pmoF5z4EH6je66wvDMtbxn2iRff8OvS9Zqbxd1PJ3z6KVhDmN-Q1YFMLRmPN5fHwSeEPmutPMaHACwZTvTPc5hz3gogSVH8dok4gpwcDGJemW7dwjfQM91-2T1K9gYbO702F0q9ZkchF_sAoB-eP5xW184sRtzt8c1TXKsvKJpBjpn_Kz9DLCLAZSSaeunevFnjAKIX11pcMYlgo56cOQPWnbAYwkORFwgU8mFIbKm6AHG6jIZuL52OwKCqOEM9mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇺🇸
#فوری؛ تفاهم نامه صلح توسط ترامپ و پزشکیان امضا شد  @News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66405" target="_blank">📅 04:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66403">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4qBHKK1Nts3NFWhk4pl9QPH8JMgXAxc0oQhcpiwXM05bEvFZvFagTRr2pwghYgdLHES8dKZi7rAHcW1xz9a8qtZMbPpnRIH9kJKRD7mhf9DnV7xlNtwnqsEDe4W_UW0Twp3DnBFvlSAhGHT4fkylRVRCKXtYiseEBmIjB1HWPl7RIOZOn2m2MRh8wn5tRXzpQaLidJOatYRhDCEylkz7T__dLOspD5hli1C9FNsUKPAfS5R8xLBMrL6eDjItpI7etlowgpjo3ksliU3EQKx-wMXzWcVOO4o6I3KODapGg64Y3At4wvGiF8rcCNloyANuvXGgKJPK_9pxCqAGilzRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be88e9229.mp4?token=cgDOqzV1DS52gAgwC_CPbVRF8rh80MZa6xk5439NEgNvyGe2tf_yE0ZELCtiIMZE-uGkuz_eGBZnc1noNUwpVhGlnWcQ5tTsYdHwfVPXK-9QylPHuxj2a2Mw9F3vbUfS_uuml2ouCEItQtMh1yL2_TPX02mo0ijUN6xhEfZy7yzPLjbYHhBc8aZUOvlYzRGI4pjPkJYB6wqO_oL_Cvg35OE-m7SyIvzagFz9ZEULhXXld_Iukgnyfqo6KokzilwdJ_f4oFNJllhlluHRK99G7f49VfiJ2pOZWPDwho892dIJGxPwWEpFjXEZBHxtHa6PZ_N2ElQpYVJjN0ebtGEojQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be88e9229.mp4?token=cgDOqzV1DS52gAgwC_CPbVRF8rh80MZa6xk5439NEgNvyGe2tf_yE0ZELCtiIMZE-uGkuz_eGBZnc1noNUwpVhGlnWcQ5tTsYdHwfVPXK-9QylPHuxj2a2Mw9F3vbUfS_uuml2ouCEItQtMh1yL2_TPX02mo0ijUN6xhEfZy7yzPLjbYHhBc8aZUOvlYzRGI4pjPkJYB6wqO_oL_Cvg35OE-m7SyIvzagFz9ZEULhXXld_Iukgnyfqo6KokzilwdJ_f4oFNJllhlluHRK99G7f49VfiJ2pOZWPDwho892dIJGxPwWEpFjXEZBHxtHa6PZ_N2ElQpYVJjN0ebtGEojQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇺🇸
#فوری
؛ تفاهم نامه صلح توسط ترامپ و پزشکیان امضا شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66403" target="_blank">📅 04:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66402">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66402" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66401">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OJzZUQJoOkroGCBz0Bdj3BsyvsRWPEYuNYDB5ZQ3xzt_hKKFI1keglF0RhslfVzARwJtr3itfi70ZT6mE7koM7XcqrNyRr0e7BLlV-RpWdJQh5I7DaxcFRbnsZtVj8dbGjVmdJ9prfevy1G39TvKiub4sYYpnYgULreCrAPxLMnMldtKCOrf2nLrjG3P-jAgYgEn07U7Kma6SjfAr0O3LyXs6sOlS73WVigu5J_LzdgGQEEsL0joLUrljHtTKDyFrQyJ2e0xXC7ijVlHfo-KdtnuAg68cZpAH46sjXQ53jJyGiJ3IUe9zmdQXaWLiF63HXBQuRWys4OD-eYJtjFi9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66401" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66400">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/gFUFe9CkSJfz6VcSNLU8d9Ie6e7cpyS4bxl7dzURuKoeBQuFiDhEBFK13KZaOqTL8emfl-aUeGe-tPtyVJKJBhU7zRJgvImBsKzWiG6wnegDrEd-UMDm1mWvdER1lSRvH6sWL2MtVereZit5OtSrXndCalYEwVfJ2thQlqb0sLOiUCm-dBHZKyukftcDrsKXScltSsALJQlkTelBTCunTHd8D-fdW5TS_ythtn7K3oOIJM7M6wV0yShMyyy2EZiY5r3wmcR_PVhOa4SLi9ZmvZqOKckIedSDtncNGPfzsHiHiBQpZHV4C1_fkzxgq16tYp08pKNM2ts9-QQd662pDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66400" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66399">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
متن تفاهمنامه جمهوری اسلامی و آمریکا:
🔴
1⃣
توقف فوری و دائمی خصومت‌ها بین ایالات متحده، ایران و متحدانشان در تمام جبهه‌ها، از جمله لبنان.
🔴
2⃣
هر دو طرف متعهد به احترام به حاکمیت، تمامیت ارضی و امور داخلی یکدیگر هستند.
🔴
3⃣
توافق جامع باید ظرف ۶۰ روز مذاکره شود، با امکان تمدید به توافق متقابل.
🔴
4⃣
ایالات متحده بلافاصله محدودیت‌های دریایی خود بر ایران را لغو خواهد کرد، در حالی که ایران به تدریج ترافیک دریایی را باز خواهد گرداند. نیروهای آمریکایی در نزدیکی ظرف ۳۰ روز پس از توافق نهایی عقب‌نشینی خواهند کرد.
🔴
5⃣
ایران تضمین خواهد کرد که ناوبری تجاری امن از طریق خلیج فارس و خلیج عمان انجام شود، با بازگردانی کامل ترافیک پس از عملیات پاکسازی مین.
🔴
6⃣
ایران و عمان درباره مدیریت آینده و چارچوب دریایی تنگه هرمز گفتگو خواهند کرد.
🔴
7⃣
ایالات متحده و شرکای منطقه‌ای ابتکار بازسازی اقتصادی و سرمایه‌گذاری برای ایران به ارزش حداقل ۳۰۰ میلیارد دلار را آغاز خواهند کرد.
🔴
8⃣
تمام تحریم‌ها علیه ایران، از جمله تحریم‌های ایالات متحده، سازمان ملل و آژانس بین‌المللی انرژی اتمی، طبق نقشه راه توافق شده برداشته خواهند شد.
🔴
9⃣
ایران مجدداً تأکید می‌کند که به دنبال سلاح هسته‌ای نخواهد بود. مسئله ذخایر اورانیوم غنی‌شده از طریق مکانیزمی که توسط هر دو طرف توافق شده، حل خواهد شد.
🔴
🔟
تا رسیدن به توافق نهایی، ایران موضع هسته‌ای فعلی خود را حفظ خواهد کرد، در حالی که ایالات متحده از اعمال تحریم‌های جدید یا استقرار نیروهای اضافی خودداری خواهد کرد.
🔴
1⃣
1⃣
صادرات نفت ایران همراه با خدمات بانکی، حمل و نقل و بیمه مرتبط، معافیت‌های تحریمی فوری دریافت خواهند کرد.
🔴
2⃣
1⃣
دارایی‌های مسدود شده ایران به تدریج طبق رویه‌های توافق شده متقابل آزاد خواهند شد.
🔴
3⃣
1⃣
یک نهاد نظارتی مشترک اجرای یادداشت تفاهم و هر توافق آینده را نظارت خواهد کرد.
🔴
4⃣
1⃣
انتظار می‌رود توافق نهایی از طریق قطعنامه شورای امنیت سازمان ملل رسمی شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66399" target="_blank">📅 02:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66398">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛بقایی سخنگوی وزارت خارجه:
تفاهم‌نامه به‌صورت الکترونیکی بین پزشکیان و ترامپ امضا شده. جمعه هم خبری از مراسم رسمی نیست و فقط هیئت‌های ایران و آمریکا به سرپرستی قالیباف و جی‌دی ونس تو سوئیس دور اول مذاکرات فنی 60 روزه برای اجرای تفاهم‌نامه رو شروع می‌کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/66398" target="_blank">📅 01:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66397">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
سخنگوی وزارت خارجه جمهوری اسلامی: متن توافق با آمریکا نهایی شده و به امضا رسیده
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/66397" target="_blank">📅 01:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66396">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac08f5fbc.mp4?token=H3d82wSZCz-dL0UqLIUQ1r1ODLTSEd6_7pa_HM45nvckiqV1HDzjYrFCDrQgYAFX1PHFYTlGbWNNxPPjnX5FfntNhP_QqeEfKQ-bTKWdjKNuuPr-tcT0qiw8OfQbC2rPuQGp2DVBJg5GF1LYoe_khpRYvlPnK3dNuG0m9C1VFv1pgvIru73MMUJPUQx5P8zTz2htmTJ1eMdGGeNZXZ6sNKQflGMAa0URAKCtA_8oD7e6AAR3I8AvCJCzCUSZVtOBKk50QXTrfxHR1XWm4r_AC7uyZID2SWDSkUz4yYIWUQg9GOfCIDy-brdWDJ-zwOzChIXrw7jvV-RnyhtiBoy0vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac08f5fbc.mp4?token=H3d82wSZCz-dL0UqLIUQ1r1ODLTSEd6_7pa_HM45nvckiqV1HDzjYrFCDrQgYAFX1PHFYTlGbWNNxPPjnX5FfntNhP_QqeEfKQ-bTKWdjKNuuPr-tcT0qiw8OfQbC2rPuQGp2DVBJg5GF1LYoe_khpRYvlPnK3dNuG0m9C1VFv1pgvIru73MMUJPUQx5P8zTz2htmTJ1eMdGGeNZXZ6sNKQflGMAa0URAKCtA_8oD7e6AAR3I8AvCJCzCUSZVtOBKk50QXTrfxHR1XWm4r_AC7uyZID2SWDSkUz4yYIWUQg9GOfCIDy-brdWDJ-zwOzChIXrw7jvV-RnyhtiBoy0vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
به محض اینکه آتش‌بس برقرار شد، دیدید که دشمن در خلیج فارس اقداماتی انجام داد و ما بلافاصله پاسخ دادیم.
آخرین نمونه آن حادثه مربوط به بالگرد آمریکایی‌ها بود.
علاوه بر این، دو ناو جنگی دشمن که قصد عبور از تنگه هرمز را داشتند، مورد اصابت قرار گرفتند و دچار آتش‌سوزی گسترده شدند - موضوعی که تصاویر ماهواره‌ای نیز آن را تأیید کرد.
از سوی دیگر، هر فرودگاهی در هر کشوری که جنگنده‌های دشمن از آن برخاسته بودند، هدف قرار می‌گرفت. همه این اتفاقات در حالی رخ داد که ما همزمان مشغول مذاکره بودیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/66396" target="_blank">📅 23:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66395">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df75a39b35.mp4?token=oWOq-3ZJRz7N8jduIkdAWxixMw3I-ji-MeC0uBLk2RVQEyU-odnkf9-uDn4vqhgysRgqWuMpMI7lj_wo8WEx11D5R873Mkysg67sOXGw7zebmniRIPk0fbFwuFMmLKoOK-fnsciKJC1ro9MlI4e4hH-RAvubPJavmU-QB2CzRaVkwg1O6YawWh69hbV81g0oLJF87aDRod3QnIY8-eNkvnTA3gOT3GNyUtgU9om_DuPCl4gGDu5-7p9ri5lYxXDv9Wek0Qcl1uBee2SnCkD2W2xjsOvsUwNpkbay9vTNM1h6L1CSN62-iTcXdOFONhLodKTLEaShq6dR4ovXd14UEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df75a39b35.mp4?token=oWOq-3ZJRz7N8jduIkdAWxixMw3I-ji-MeC0uBLk2RVQEyU-odnkf9-uDn4vqhgysRgqWuMpMI7lj_wo8WEx11D5R873Mkysg67sOXGw7zebmniRIPk0fbFwuFMmLKoOK-fnsciKJC1ro9MlI4e4hH-RAvubPJavmU-QB2CzRaVkwg1O6YawWh69hbV81g0oLJF87aDRod3QnIY8-eNkvnTA3gOT3GNyUtgU9om_DuPCl4gGDu5-7p9ri5lYxXDv9Wek0Qcl1uBee2SnCkD2W2xjsOvsUwNpkbay9vTNM1h6L1CSN62-iTcXdOFONhLodKTLEaShq6dR4ovXd14UEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏قالیباف:
نه تنها خودم برای حضور در تیم مذاکره‌کننده داوطلب نشدم، بلکه واقعاً از پذیرفتن آن هم اکراه داشتم. پیش از قبول مسئولیت مذاکرات، هر کاری از دستم برمی‌آمد انجام دادم تا این مسئولیت به من واگذار نشود.
یکی از دلایلی که نمی‌خواستم این مسئولیت را بپذیرم این بود که دونالد ترامپ طراح، فرمانده و ناظر ترور قاسم سلیمانی بود.
سردار سلیمانی برای کل جهان اسلام عزیز بود، اما برای من به‌طور شخصی معنای متفاوتی داشت. آیا فکر می‌کنید برای من آسان است که با چنین فردی بنشینم و متنی را نهایی کنم؟
با این حال، وقتی دیدم هیچ‌یک از مسئولان فرد دیگری را پیشنهاد نمی‌دهند و پیشنهادهای خودم هم پذیرفته نمی‌شود، مجبور شدم وظیفه‌ای را که به من محول شده بود انجام دهم.
ما قرار نیست فقط کاری را انجام دهیم که دوست داریم؛ بلکه باید کاری را انجام دهیم که وظیفه‌مان ایجاب می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66395" target="_blank">📅 23:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66394">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6d42bdbd.mp4?token=UT6HyBUQTsZdJoVnNzRKm7_Ux7LWkFwb-JW4waix0VT7YAy7cT4jiWfhppAtdyq6TS4vpLKJdy-yeKJqq0QQiZRwVHsOql5WW5KmmoRUFGLHFC9noX5BOnnLowRIpkaM0MPZL9lsbi8ggbdEMLaSmfrd4MvN3QlLsa_iMqyzxagaW62mVnGvylSGmPbXTAEprmuQrzYUfJE9NKSCcx9P9xfk2MQbXJUdYmvMt0edkyboiaQIK4Fv1kCGdcZ97ZN-p7zzjSoimh1eUASbJR92Gn6TWmMfGFOFBtAaGjN1LZAgL-DsIDvovyInmVjLWDQyF0l-HxWY-HPiREwzyz1xCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6d42bdbd.mp4?token=UT6HyBUQTsZdJoVnNzRKm7_Ux7LWkFwb-JW4waix0VT7YAy7cT4jiWfhppAtdyq6TS4vpLKJdy-yeKJqq0QQiZRwVHsOql5WW5KmmoRUFGLHFC9noX5BOnnLowRIpkaM0MPZL9lsbi8ggbdEMLaSmfrd4MvN3QlLsa_iMqyzxagaW62mVnGvylSGmPbXTAEprmuQrzYUfJE9NKSCcx9P9xfk2MQbXJUdYmvMt0edkyboiaQIK4Fv1kCGdcZ97ZN-p7zzjSoimh1eUASbJR92Gn6TWmMfGFOFBtAaGjN1LZAgL-DsIDvovyInmVjLWDQyF0l-HxWY-HPiREwzyz1xCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
لبنان بخشی از جبهه مقاومت است. طبق توافق، ایران از جبهه مقاومت حمایت می‌کند، در حالی که ایالات متحده حامی و متحد رژیم اسرائیل است.
بنابراین، طبیعی است که وقتی آتش‌بس برقرار می‌شود، باید در همه جبهه‌ها، به ویژه در لبنان، رعایت شود.
باید از مردم عزیز لبنان، به ویژه شیعیان و حزب‌الله، که در طول تجاوز آمریکا و اسرائیل به ایران ایستادگی کردند و نزدیک به ۴۰۰۰ شهید تقدیم کردند، تشکر کنم.
در حالی که ما در شرایط آتش‌بس بودیم، آنها به جنگ ادامه دادند و همچنان تلفات دادند.
وقتی رژیم اسرائیل ضاحیه را هدف قرار داد، ما ایالات متحده را تهدید کردیم و اولتیماتوم دادیم که خواسته‌های ما باید پذیرفته شود؛ در غیر این صورت، ما پاسخ خواهیم داد.
ترامپ مجبور شد در شبکه‌های اجتماعی پست بگذارد و به نتانیاهو بگوید که حملات باید متوقف شود و دیگر نمی‌توان ضاحیه را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66394" target="_blank">📅 23:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66393">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed9265802.mp4?token=rDMRBKUJNaLDW32OUrHzAwYX4GQT-vouuhyaoGaDHO7yzt7-dhe3nMh3nItb0S621iinBWBMSyRmjp3_OsJAzWK47AWBkBGA55Ro_KbuStleCavC-eFCKMbyIW1b4xs1XxzM_XBqGz4WSKsblG3WtzmIOgPysbPEzGz2scZvFPeaWLRAlNUEb6wDl6iHmvFZO8Vg9C9SstTn6-dlTSZ66FnvqnyoHpn4qYpe39iCdS3byx8e6et-x2nkQTxeAK2rBYf68y9Litiel_y6ZTjT7LYKzs8-sgOgXvjj6MYmuvwvylAMNbSheUtU8gMaoLgUD6v-MLCY4qZlgs_TV4Yz4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed9265802.mp4?token=rDMRBKUJNaLDW32OUrHzAwYX4GQT-vouuhyaoGaDHO7yzt7-dhe3nMh3nItb0S621iinBWBMSyRmjp3_OsJAzWK47AWBkBGA55Ro_KbuStleCavC-eFCKMbyIW1b4xs1XxzM_XBqGz4WSKsblG3WtzmIOgPysbPEzGz2scZvFPeaWLRAlNUEb6wDl6iHmvFZO8Vg9C9SstTn6-dlTSZ66FnvqnyoHpn4qYpe39iCdS3byx8e6et-x2nkQTxeAK2rBYf68y9Litiel_y6ZTjT7LYKzs8-sgOgXvjj6MYmuvwvylAMNbSheUtU8gMaoLgUD6v-MLCY4qZlgs_TV4Yz4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
بدبینی و بی‌اعتمادی من به ایالات متحده از هر کس دیگری بیشتر است.
حتی اگر توافق نهایی حاصل شود و توسط قطعنامه شورای امنیت سازمان ملل متحد تأیید شود، باز هم قابل اعتماد نیست. تضمین ما قدرت ایران است
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66393" target="_blank">📅 23:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66392">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afb769475.mp4?token=LfK5hgOR43E-BwC8BSMpYDmukf4YKAZLCrl_EUIQuUrk-4Si94VU9nK0OwnvJAzKMH-BY7sMvMgrPAtZFNymdNYlf2ihsWG8xQkd3x_2MwnUMQCpQilJ0K3QNpW-k0GPDbukNd9XDhil_gbcLzyNzBMsfA_JRv_AiKTUcB9Rvt4kgoPhuFMdXerMYXjgePRRkFEbkVjFjEayBDqNu4ZIwBtJNpkqIWk_Jo37IRvBplNUjzi-VzKQNj4_Ao01v7VVq8XQmrlqd4EQqOiWLZD-2NPFbO1MW5iJ6MBQ-7g8PkHz0c4AN1mYghr6KCPk723HeKbUx30RBOD1CIlhwiQw5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afb769475.mp4?token=LfK5hgOR43E-BwC8BSMpYDmukf4YKAZLCrl_EUIQuUrk-4Si94VU9nK0OwnvJAzKMH-BY7sMvMgrPAtZFNymdNYlf2ihsWG8xQkd3x_2MwnUMQCpQilJ0K3QNpW-k0GPDbukNd9XDhil_gbcLzyNzBMsfA_JRv_AiKTUcB9Rvt4kgoPhuFMdXerMYXjgePRRkFEbkVjFjEayBDqNu4ZIwBtJNpkqIWk_Jo37IRvBplNUjzi-VzKQNj4_Ao01v7VVq8XQmrlqd4EQqOiWLZD-2NPFbO1MW5iJ6MBQ-7g8PkHz0c4AN1mYghr6KCPk723HeKbUx30RBOD1CIlhwiQw5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
ما بر ایالات متحده و رژیم صهیونیستی، که قدرت‌های نظامی پیشرو در جهان هستند، پیروز شدیم و اجازه ندادیم که آنها به هیچ یک از 9 هدفی که اعلام کرده بودند، دست یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66392" target="_blank">📅 23:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66391">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a462c62e6a.mp4?token=JA-EgcK8WCBdeqJ1JeCkbPnkazxPsdr7eE1faeoJVtzIh3zS6AHjL7-JJfXJIWCgGCgCcnZczpcGj11oIV2swgXNu3ungUDQMhHUZ5mnCgEr9BGJIdB6RQPI1zbGJzpqNy4dd4kHe4xXq95v7mCcNGO61J2nCWcVUGJC3RKmi68qO3fBdrMA9RxblUpJym-Sf7-1BtpDmgas69EYt6-u_s7DNTPhJdsMFkgRBfdmSZir76OGpgX8piCD1FJEdp3Z_-nL3JP_fSgH-ve7gPO71EMkP_6JFqABw2l0op6E2z4nz2MhJWOBrASqWKoW6Slrx_HtdWy46AT7yYZTbtWWsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a462c62e6a.mp4?token=JA-EgcK8WCBdeqJ1JeCkbPnkazxPsdr7eE1faeoJVtzIh3zS6AHjL7-JJfXJIWCgGCgCcnZczpcGj11oIV2swgXNu3ungUDQMhHUZ5mnCgEr9BGJIdB6RQPI1zbGJzpqNy4dd4kHe4xXq95v7mCcNGO61J2nCWcVUGJC3RKmi68qO3fBdrMA9RxblUpJym-Sf7-1BtpDmgas69EYt6-u_s7DNTPhJdsMFkgRBfdmSZir76OGpgX8piCD1FJEdp3Z_-nL3JP_fSgH-ve7gPO71EMkP_6JFqABw2l0op6E2z4nz2MhJWOBrASqWKoW6Slrx_HtdWy46AT7yYZTbtWWsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
تفاوت بین مذاکرات فعلی و دورهای قبلی این است که امروز دانش و دستاوردهای پیروزی در میدان نبرد به عنوان پشتوانه دیپلماسی عمل می‌کند.
در مذاکراتی که به عنوان نوعی مبارزه انجام می‌شود، نه تسلیم وجود دارد و نه شعارهای توخالی.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66391" target="_blank">📅 23:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66390">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7aRj6EsqBwRZ2yWpvO4kNOr6XeOTVnQb-9h0r_CkSo0Bopenb-vEByfWUAEmV5nPNXE5yO4q-XzUVSMq05IgI75DkTr7n-Y5F0P8khnKElmDFUixvnrNTv9VK5_T3H2xCYFn0UCyJTnR1bD0hW_EeYa3oAS0r2fPW3WXxOeOJmkJoYYBH5vSUOzaDdOriHuvTrbSNSFyihV8lccmD49U6BaD1Sg663Vto0QKktJ1sn9F1S9rwERdPo6b2dIKDIQjxN2RhE_dNluV2zYBiAnWTuAba2EaesNn3Y0CY0D8EjW3id--bQ-GFGuARxmRRCDpTSGPk9zk6lEQRWG0CT7Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شبکه خبر:
مصاحبه اختصاصی رئیس مجلس درباره تفاهم‌نامه پایان جنگ تا دقایقی دیگر
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66390" target="_blank">📅 22:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66389">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d9400b7a.mp4?token=Q72PHse5CWKbbVneo_lkvMFuupiWGbuYCO-_k0qj7wrTOvxT6NVmkkDIbBilvlbsKmeEYh5qU1QCOgqsOsav19qumIgJ32NWwy6u0ooCPL2ikuGuywUgdQhPGQU0-N7wJn2bLOY3AYCGsJFEOmuAJL-vFjWdDuYd0LgmjhTdNPxliZetLOQQLb9R1BEQEjdH2jtRaQDAaSCHRQ7N844ICwHDWt1UJa15u1aKBM3G7BUxNO0OKsqf1Wy3PfLKuuYe55lCLRnpklFdUtWCKk3Djc6gbMB5rDxC9oRNbanLl0R_gUIMqZyHtZ_Q76PH7qJL-xRXGCmDX2COehie5damZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d9400b7a.mp4?token=Q72PHse5CWKbbVneo_lkvMFuupiWGbuYCO-_k0qj7wrTOvxT6NVmkkDIbBilvlbsKmeEYh5qU1QCOgqsOsav19qumIgJ32NWwy6u0ooCPL2ikuGuywUgdQhPGQU0-N7wJn2bLOY3AYCGsJFEOmuAJL-vFjWdDuYd0LgmjhTdNPxliZetLOQQLb9R1BEQEjdH2jtRaQDAaSCHRQ7N844ICwHDWt1UJa15u1aKBM3G7BUxNO0OKsqf1Wy3PfLKuuYe55lCLRnpklFdUtWCKk3Djc6gbMB5rDxC9oRNbanLl0R_gUIMqZyHtZ_Q76PH7qJL-xRXGCmDX2COehie5damZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آتش‌سوزی گسترده انباری در سن-سن-دنی، پاریس
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66389" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66388">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2ipt0hToHEohQpnZKqZAKkLJz3Hc9hL11XiovI3w82lV8LOe0rhpr17WuWTqCqdUU-6nQmDTOekkK3OVADWsjfhoOhH41Xvq6KJ9ry95mwPMGEDp1gRZBGqlS-jRpTTQrk8NL5yDMg2pQMUVMQRIyWr6WQlw5JYasduJw_wQ_4N-G68_1qomvBJxkC5KWaNnyn--4QhXOoqJyM18VBtJhIt43EpLlw3hnwgZCxCdH3qzmEhfJy6oQq1XBeF-8SK-YI2apAP65eS-Px-nooTxJDbfH2jMTdXbf2VNuabz7a10kSCuY8unu_N7HiNBv8TWXh_gSXtS_YMO0T__3F-0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیندزی گراهام: من همین الان یک بحث بسیار طولانی و سازنده با ویتکاف  در مورد ایران داشتم.
بعد از این بحث، به نظر من امضای تفاهم‌نامه برای ایالات متحده مفید خواهد بود، تا جایی که تنگه هرمز شروع به باز شدن کند و خصومت‌ها با ایران متوقف شود.اینکه آیا ایالات متحده می‌تواند در مورد برنامه هسته‌ای و سایر مسائل به یک توافق قابل قبول و قابل تأیید با ایران برسد یا خیر، هنوز مشخص نیست، اما من جنبه منفی کمی برای تلاش کردن می‌بینم
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66388" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66387">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b1096f4de.mp4?token=hM8Y78g4YBGHcdAekbv1otyG1BO21R-gnsaLCieRsdQvYYm_UpOQCjs1rwHXUdk_nASacyV2ILxig8ZQBAL3eazJfgm2tzfM6QmTOMf5KYr6PI-QIJ2j-F_6SgLbR4C44_l1f-QN5e_gS5G75wGUy7Ib1QFpW2Oyq15t5toAZmW9THrdTekpnyi7lKQCJp-Wdtq3FgRpB4IlN_o-NQSTe6KG4nJdvgatCMueyj5tvXWun3B7ToRCvZMlS57hBmHXMKaHzNKztST3c_TcG1MOqFv80I9g2qlZCNHaSAnQGWNomBUfrjblaiVDeR3ptT4uXviicOJulRs-Ucbh-QWiQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b1096f4de.mp4?token=hM8Y78g4YBGHcdAekbv1otyG1BO21R-gnsaLCieRsdQvYYm_UpOQCjs1rwHXUdk_nASacyV2ILxig8ZQBAL3eazJfgm2tzfM6QmTOMf5KYr6PI-QIJ2j-F_6SgLbR4C44_l1f-QN5e_gS5G75wGUy7Ib1QFpW2Oyq15t5toAZmW9THrdTekpnyi7lKQCJp-Wdtq3FgRpB4IlN_o-NQSTe6KG4nJdvgatCMueyj5tvXWun3B7ToRCvZMlS57hBmHXMKaHzNKztST3c_TcG1MOqFv80I9g2qlZCNHaSAnQGWNomBUfrjblaiVDeR3ptT4uXviicOJulRs-Ucbh-QWiQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف؛ آن روزی که من پا در میدان دیپلماسی گذاشتم گفتم:
من اینجا آمده‌ام که هم آبرو بدهم، هم خونِ دل بخورم و هم خون بدهم؛ اما اگر کسی فکر کند که از مسیر امام شهید، مسیر انقلاب و عقلانیت ذره‌ای فاصله می‌گیرم، هرگز!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66387" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66386">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a579da34fb.mp4?token=dXweQDOZyiC37SQ1HbWX0R7JAaknw2gyCu_RPCnKqBL95pBAArpst22IbNSopfWWNIi4sOpt9r_EysJcQpTmTVFidDQKyaS_xYmNq3UODWGf0X861MD5jT3uPODhUCE3UytV19swHg6OkB3os5NUlFoi8OiixgFvqWEjCwt5W5Wep-fdHMsNwExg6qABsZiJ_CUaJCiYW-_Fuk0PjLU3AWLKw-KBFz-3F91RQv9W-TrvnqseQkbR2xnLcJaITcnz0pnAimNLRVinklhdxZIT8dj13hPuv3Qin29z_VEVA9TYAwc7c4P9AYsrcQGuG30bLwK-rGgVuPwHup3OB8CZ-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a579da34fb.mp4?token=dXweQDOZyiC37SQ1HbWX0R7JAaknw2gyCu_RPCnKqBL95pBAArpst22IbNSopfWWNIi4sOpt9r_EysJcQpTmTVFidDQKyaS_xYmNq3UODWGf0X861MD5jT3uPODhUCE3UytV19swHg6OkB3os5NUlFoi8OiixgFvqWEjCwt5W5Wep-fdHMsNwExg6qABsZiJ_CUaJCiYW-_Fuk0PjLU3AWLKw-KBFz-3F91RQv9W-TrvnqseQkbR2xnLcJaITcnz0pnAimNLRVinklhdxZIT8dj13hPuv3Qin29z_VEVA9TYAwc7c4P9AYsrcQGuG30bLwK-rGgVuPwHup3OB8CZ-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
وقتشه که سنگر رو از بچه های لانچر تحویل بگیریم و یه زندگی خوب برای مردم بسازیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66386" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66385">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36c7f8ec39.mp4?token=NiTdwCe1Q2dXJCpU4QrvcwYtt-cumMkW0fINulGZvQuteExv5V0AwEEg799HLyQPmE5M8bEQE8UP3uiV1jSbvK3h1uEAWGhRSl-1vLr1Ul27N7lZnijX2RDz7R0GWpvnaLjC49YlMxo1fsQP3qCmF8pRzAXr3FyNDJ_BvhHsqvM2b7_lk0ywPp8BnuukCuhgFROywvsA5_Y6_bxT4wE9ectA59BOFJD7T7fImbqj8ZM2M32wksL2sb1lgV8boyeDk9Ht3oFmZZTLPGvqcHbnm-fG_K5SdapMZhyuPbDrX9LKiIWJeSb2evlK8KlwDRwgAMkMGWjIJ7yhnLClJzUbFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36c7f8ec39.mp4?token=NiTdwCe1Q2dXJCpU4QrvcwYtt-cumMkW0fINulGZvQuteExv5V0AwEEg799HLyQPmE5M8bEQE8UP3uiV1jSbvK3h1uEAWGhRSl-1vLr1Ul27N7lZnijX2RDz7R0GWpvnaLjC49YlMxo1fsQP3qCmF8pRzAXr3FyNDJ_BvhHsqvM2b7_lk0ywPp8BnuukCuhgFROywvsA5_Y6_bxT4wE9ectA59BOFJD7T7fImbqj8ZM2M32wksL2sb1lgV8boyeDk9Ht3oFmZZTLPGvqcHbnm-fG_K5SdapMZhyuPbDrX9LKiIWJeSb2evlK8KlwDRwgAMkMGWjIJ7yhnLClJzUbFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس در مورد پرونده اپستین:
ما نمی‌توانیم فقط به این دلیل که فکر می‌کنیم چیزی اشتباه است، مردم را تحت پیگرد قانونی قرار دهیم.
شما فقط می‌توانید مردم را در صورتی تحت پیگرد قانونی قرار دهید که مدارکی برای اثبات تخلف آنها داشته باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66385" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66383">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه جمهوری اسلامی:
در یادداشت تفاهم ۳بار ذکر شده باید جنگ در همه جبهه ها از جمله لبنان پایان یابد.
همچنین بر حاکمیت لبنان تاکید شد و حضور ارتش اسرائیل با آن در تضاد است.ادامه اشغال اسرائیل از جنوب لبنان نقض تفاهم‌نامه است و اقدامات لازم را اتخاذ خواهیم کرد.
یکی از بندها تایید میکند که آغاز مذاکره و ادامه آن مشروط به اجرای تعهدات است ازجمله توقف جنگ که شامل لبنان هم میشود.جنگ بایددر همه جبهه ها از جمله لبنان متوقف شود تا مرحله مذاکره آغاز گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66383" target="_blank">📅 21:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66382">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a620bba5be.mp4?token=iguNQtu1f890elobEjQkqYMOLH-UcXlvvxN0laKyf7bp0UnhnfP3gRNtueGDNm67HcxvrcWk18lvcZ2Qpia3s7qWWrKP-smYc-E-1RqPYnRrUJmddsoM3JcI9AGkLUJJonTbUnJ40y54GEcDlUvlWv8niN7kn1ZlhGQN5opxw2Fm4BACRVGnW5gW10n0wSOrFj4EA6g_dOqP6henl2UJOS3Ts1X_dCt72lEpA5UXsbSKYCiOz280QAICXjDMMh3GDJ2UTxxTHLW5UMnCCLhz9XadnTzd3EM0hsp5L1koWpqR8pETEOwZ6cX0UJ3hq2WsqDYzBzS0xVbQ-FS8TQWhIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a620bba5be.mp4?token=iguNQtu1f890elobEjQkqYMOLH-UcXlvvxN0laKyf7bp0UnhnfP3gRNtueGDNm67HcxvrcWk18lvcZ2Qpia3s7qWWrKP-smYc-E-1RqPYnRrUJmddsoM3JcI9AGkLUJJonTbUnJ40y54GEcDlUvlWv8niN7kn1ZlhGQN5opxw2Fm4BACRVGnW5gW10n0wSOrFj4EA6g_dOqP6henl2UJOS3Ts1X_dCt72lEpA5UXsbSKYCiOz280QAICXjDMMh3GDJ2UTxxTHLW5UMnCCLhz9XadnTzd3EM0hsp5L1koWpqR8pETEOwZ6cX0UJ3hq2WsqDYzBzS0xVbQ-FS8TQWhIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره محمد بن زاید:
محمد در امارات متحده عربی یک جنگجوی باورنکردنی است.
هفته پیش بمب می‌ریخت، گفتم «کی داره این همه بمب می‌ندازه؟» امارات بود. او یک جنگجوی خوب است
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66382" target="_blank">📅 21:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66381">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byekd1NT4IFSZugfAjwMHxRdydgXSiceE-9JF7S6mt_-Wnd6rpJX1_bRbO86lNrVriYB5KDdPOvSbt3R7SrnXqFyQBYjMfsOeQenZpSmPjF5ZBC8FccaOpWWCxknWSCZBPpBdWjk-GAxpkV12jJ1nkNKx3VeKq_4gtf6A1JQdSCPdWbryP_9EmrfCTlvWKTf1CIr5LJpcDzfdoyTE0MIjxSflczmryyC3znePRZSkErJRDMjfFE_0Cnc84IHQqncCoVowi3XCaO4Wv5pNXg0x2PlzaDbsDjDxQLRHKyWbyGEcibwaCofRD74KXV7D0Vq7t_x0Dpz7fs1F5Vy9_FuLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛الجزیره به نقل از وزارت امور خارجه ایران:
ما در حال حاضر در حال بررسی ایده امضای یادداشت تفاهم از راه دور توسط روسای جمهور ایران و ایالات متحده هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66381" target="_blank">📅 21:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66380">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729c69207c.mp4?token=Bpf40GK9JmkvSFz6fDedaMRJw64tX2jtJkrUtvyFAaeIxiw8P1zRP6-6sK1az0etraRREphb4nbcHidANvcchfpgu2cemLMoL1IRv5okdWnZMKkkIJ1o3mCY8BH5HERYOrvxidsrLa8AAIqzSH-FJG90Qq2H8CjyVMvb8IC9KS5u9pxzCQkXOTXkXOkE1JlXMLugFqCuYtpuRkHFCVv8DQ3CSphX6q7XRWXvXaMs-909pFwbAwOIyRf1CCz5Qlw9oU4ru_gT6N-PsKtiqfzL0oe70QgsaDThZxJGeYuVI2jNnZpyMlvkfnQehdWd6GjJCWd2WM6HNJu2NXd-6d3ddg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729c69207c.mp4?token=Bpf40GK9JmkvSFz6fDedaMRJw64tX2jtJkrUtvyFAaeIxiw8P1zRP6-6sK1az0etraRREphb4nbcHidANvcchfpgu2cemLMoL1IRv5okdWnZMKkkIJ1o3mCY8BH5HERYOrvxidsrLa8AAIqzSH-FJG90Qq2H8CjyVMvb8IC9KS5u9pxzCQkXOTXkXOkE1JlXMLugFqCuYtpuRkHFCVv8DQ3CSphX6q7XRWXvXaMs-909pFwbAwOIyRf1CCz5Qlw9oU4ru_gT6N-PsKtiqfzL0oe70QgsaDThZxJGeYuVI2jNnZpyMlvkfnQehdWd6GjJCWd2WM6HNJu2NXd-6d3ddg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگر آنها به توافق‌نامه پایبند نباشند، یا برخی موارد حتی در توافق‌نامه ذکر نشده باشد - این یک یادداشت تفاهم است، اما ما بدون نوشتن آن، از برخی موارد درک داریم - و، اگر آنها به آن پایبند نباشند، احتمالاً به بمباران آنها تا زمانی که به آن پایبند باشند، برمی‌گردیم.
می‌دانید، شگفت‌انگیز است که بمب‌ها چه کارهایی می‌توانند انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66380" target="_blank">📅 21:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66379">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
#مهم؛ پس از روی کار آمدن مجتبی خامنه‌ای به‌جای علی خامنه‌ای، #سعید‌_جلیلی نماینده‌ی سابق علی خامنه‌‌ای در شورای عالی امنیت ملی عزل شده و #علی_باقری‌کنی( برادر مصباح‌الهدی، داماد علی خامنه‌ای ) جایگزین وی شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66379" target="_blank">📅 21:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66378">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533e14dcfc.mp4?token=ajUJI9NYhRSmtxUD_FEhWzEwRwZIsRcJqo3qFFzZc0FtbzxT4kODN6_8WZv-HMcvscuMp0v3nHmF4sYGqPSV4AOTNOXef_Czf5As8A4fxp-o7BqioM3vln6aha96agwwVnulhaXvuX6_dJSs2-4O58pAciWGOzbWoreGU_omYm2_LVc0tgc2koe41XUiJkNXQkHt8EQXRiNQ3aoSrkWGuCtN7-8ph7HrC-8wlrjsKTObAxYc7P-EGPPgJm9NHVKyi5QKCPIMolgVj-6TfSKrLxZ_DZKP9ryzdk9fgKaj5898FlA4jNrkXNmSFSGfGnK-u6g6qSw9wXyF1XwM7t_iJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533e14dcfc.mp4?token=ajUJI9NYhRSmtxUD_FEhWzEwRwZIsRcJqo3qFFzZc0FtbzxT4kODN6_8WZv-HMcvscuMp0v3nHmF4sYGqPSV4AOTNOXef_Czf5As8A4fxp-o7BqioM3vln6aha96agwwVnulhaXvuX6_dJSs2-4O58pAciWGOzbWoreGU_omYm2_LVc0tgc2koe41XUiJkNXQkHt8EQXRiNQ3aoSrkWGuCtN7-8ph7HrC-8wlrjsKTObAxYc7P-EGPPgJm9NHVKyi5QKCPIMolgVj-6TfSKrLxZ_DZKP9ryzdk9fgKaj5898FlA4jNrkXNmSFSGfGnK-u6g6qSw9wXyF1XwM7t_iJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
مردم از من می‌خواهند پل‌ها را بمباران کنم.
من قبلاً این کار را کردم، چون می‌دانید، آنها به یکی از وعده‌هایشان عمل نکردند و من بزرگترین پل آنها را بمباران کردم، معادل پل جورج واشنگتن ایران.
اما ما آن پل را بمباران کردیم، دیدید که
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66378" target="_blank">📅 20:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66377">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea27fd13ab.mp4?token=dGJ2u2bZzF_D3_AGFe5SC_qmq1X76sJdneRi-49Y_vdZlp402dcuTxvQ-xNGnZku834hZcgdj1M3nLJ9Fva0AUXr22QCMeo5GEIbUYa83QjuhVh8tNC7-dwMoKTPHELn2TAyswr3hQdT5LyanzznTYjkqx4fpWMyhGmdU_2m8ZXKIZaNm7yzJrP3lMcN71lqQ2LAf0vmVnItLlEGqULEkBJuO2GOENA_UVZK9SYeahx5G-1PnxVGEhx6n2elGI23EFk9bEtnik23R_OG042ELEDjTwlculQfEhDPI-IRJ8koFq-5y8TEHJVk5-_fWXxPfwEGu8Pwfzyl2tTuswurQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea27fd13ab.mp4?token=dGJ2u2bZzF_D3_AGFe5SC_qmq1X76sJdneRi-49Y_vdZlp402dcuTxvQ-xNGnZku834hZcgdj1M3nLJ9Fva0AUXr22QCMeo5GEIbUYa83QjuhVh8tNC7-dwMoKTPHELn2TAyswr3hQdT5LyanzznTYjkqx4fpWMyhGmdU_2m8ZXKIZaNm7yzJrP3lMcN71lqQ2LAf0vmVnItLlEGqULEkBJuO2GOENA_UVZK9SYeahx5G-1PnxVGEhx6n2elGI23EFk9bEtnik23R_OG042ELEDjTwlculQfEhDPI-IRJ8koFq-5y8TEHJVk5-_fWXxPfwEGu8Pwfzyl2tTuswurQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
گسترش توافق‌نامه‌های ابراهیم چیز دیگری است که امیدواریم به آن دست یابیم.
و من فکر می‌کنم اگر عربستان سعودی پیشگام شود، لطف بزرگی به خودش می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66377" target="_blank">📅 20:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66376">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0cf6ba4c.mp4?token=LHNe2yl-sRsszF-6DxPd1WBuYOdwpojYDVtzMatqgNVBv8xzCWkIUpUm7ID6OBFerQkoZatKe9Vi24eHBN_3wLEGBZCXbEuJYgTrvoqav686Csziuzu6bY34Nzj9qJk-tYmPXd6xsDB13QooKt7Al35WHcTQjnfb2HKgJrNk4G2hiYiJVLCbDI94SV_30cSgNXtz6WYdw0H7eIU5gozNV91kiYGsNpi9PKjB8RmH5IrtDLQHeFDvxtdgR_kXMUlZ-CgCj_MEZR0yP2yPOHClkioKHuaCZnHOZu5yPLSF9OY9HjhHAPI6KLZoFayV3-aMKrxmEb68EZbIPrkJbeGJcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0cf6ba4c.mp4?token=LHNe2yl-sRsszF-6DxPd1WBuYOdwpojYDVtzMatqgNVBv8xzCWkIUpUm7ID6OBFerQkoZatKe9Vi24eHBN_3wLEGBZCXbEuJYgTrvoqav686Csziuzu6bY34Nzj9qJk-tYmPXd6xsDB13QooKt7Al35WHcTQjnfb2HKgJrNk4G2hiYiJVLCbDI94SV_30cSgNXtz6WYdw0H7eIU5gozNV91kiYGsNpi9PKjB8RmH5IrtDLQHeFDvxtdgR_kXMUlZ-CgCj_MEZR0yP2yPOHClkioKHuaCZnHOZu5yPLSF9OY9HjhHAPI6KLZoFayV3-aMKrxmEb68EZbIPrkJbeGJcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد اورانیوم:
هیچ‌کس نمی‌تواند به آن دست یابد، بنابراین مهم نیست که ما این کار را به سرعت انجام دهیم، اما می‌توانیم آن را نسبتاً سریع انجام دهیم. هیچ‌کس نمی‌تواند این کار را انجام دهد. و اگر آنها این کار را انجام دهند، ما با موشک‌های پاتریوت به آنها ضربه خواهیم زد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66376" target="_blank">📅 20:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66375">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07c3e1404.mp4?token=RUzlUkbF5LbrXG_6z0pkXAn_wBiyf9sJpR6f66Ir5FfK8wKCpXSRU1jkuudRT0h9TZPRYNyTKd_tvSDdvxNHWSjweVH45CargIRhtwXjCxSERXIOf5P7YMN_HZ_MNspg9H-sX6X3KN7jC7DHI4AKwagAmvzAMepgd90JzAwTV7iTe2O3MG3LAdxxXs126XkL1iNeyS0DwUYAMQNcOAfDObR915J4CfA3WAJ4x6DCaBGvlLeaDYut-FVMNCntvP6ECL3WOCz4Sij_BLpnjzhk-cUXOcd8PDBR_P8G2JbkOs-jckJmH8cXaeSiubsCTT0PvNu5rvDIYyuAhwAapPYQeaMY207d-SVIIcYevTGp2b7RHombc_x8Bo3HgvnQxtG5qmCqFkDvVWqbqPLjP2U_QL5-EW6vQVpfg7Ch7X8M2uKjHjAVKxY1k9kbMVyj9qkWWAYPDQFWd1MPKnApJLc0G5XINeoojdb5jNf_uUeBDEJ0wdUeFyvcuNS3ehVxkvSRhukkNKHt-bz2X-TcIK5G3756NopFLpLo-Q0vt60eUlSf5CqSLP1CWM0IFpHWslJr3kcB0hp1A37EFWCvXRv9wcFdBDD60szJKUgY6-jLgR1nJQG6BAoByqp_n59-p9H1fF8O4W6Mf9bCtfsRL7ZHOG4FD5hBWigA9AH8gZYFYKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07c3e1404.mp4?token=RUzlUkbF5LbrXG_6z0pkXAn_wBiyf9sJpR6f66Ir5FfK8wKCpXSRU1jkuudRT0h9TZPRYNyTKd_tvSDdvxNHWSjweVH45CargIRhtwXjCxSERXIOf5P7YMN_HZ_MNspg9H-sX6X3KN7jC7DHI4AKwagAmvzAMepgd90JzAwTV7iTe2O3MG3LAdxxXs126XkL1iNeyS0DwUYAMQNcOAfDObR915J4CfA3WAJ4x6DCaBGvlLeaDYut-FVMNCntvP6ECL3WOCz4Sij_BLpnjzhk-cUXOcd8PDBR_P8G2JbkOs-jckJmH8cXaeSiubsCTT0PvNu5rvDIYyuAhwAapPYQeaMY207d-SVIIcYevTGp2b7RHombc_x8Bo3HgvnQxtG5qmCqFkDvVWqbqPLjP2U_QL5-EW6vQVpfg7Ch7X8M2uKjHjAVKxY1k9kbMVyj9qkWWAYPDQFWd1MPKnApJLc0G5XINeoojdb5jNf_uUeBDEJ0wdUeFyvcuNS3ehVxkvSRhukkNKHt-bz2X-TcIK5G3756NopFLpLo-Q0vt60eUlSf5CqSLP1CWM0IFpHWslJr3kcB0hp1A37EFWCvXRv9wcFdBDD60szJKUgY6-jLgR1nJQG6BAoByqp_n59-p9H1fF8O4W6Mf9bCtfsRL7ZHOG4FD5hBWigA9AH8gZYFYKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
💥
پرزیدنت ترامپ:
هیچ‌کس سخت‌گیرتر از من نبود. هیچ‌کس سلیمانی را نشانه نرفت.
می‌دانید، وقتی من سلیمانی را هدف قرار دادم، مردم فکر می‌کردند این بزرگترین اتفاقی است که در خاورمیانه در ۵۰ سال گذشته رخ داده است. این بزرگترین رویداد بود.
او رئیس ایران بود و مورد احترام، اما او یک نابغه دیوانه بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66375" target="_blank">📅 19:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66374">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9392768ed3.mp4?token=VDdu8J7Sw9kWcd7sdHwNB9-kA-I8rWT8-EFyVdS2GecxPwtMTyuIVSdTUBt45sacOcoPEzr9Tt3U6zB1FwjwSwgiiR4Q8Ffi1vQYWqvzNVpgyLiNBvVoD4sXGhlHHBp6WyBWXdSVxUOWyO1Pc2BxsH67N9CDVghxqHjzehfvej7DZIYd5VeuhhtjIFFHo5PzZylwi0x80MH1TynFfYoET-ZgMFIVQV2bzDBm-vnaeBRO4nP9UE1ggxTLxfSIxKJfBNbmev-7B7BD_nmAMwJSg2TPvHPRJb6c7lLlt3r7i7E4BxuitM8hHRy5Kmc46M2CGpgZWAjx2-zZLUuHJtbgpEhaSLHPrzvjGAlNEAuq9uBET1I5B409wb3RsQCj0lmTDmJXILRvgZwwjvi50g9Su1Alkos9Ucbe3cBiBKqIbMD8iyCWBGppXcnJlhddSWUmFZB56PNImfHarI2Xa2lw4kazlkv0F0kUO8CV02zhu3LfZ_CYwWPmQQs-r7pxunMZmNdzDotCjQNmaq67d6AP3hVQ-Ueukl-PuSOtXBnBpPMv3WTJeteKNoHC2z9YODQFCS16G8yOFm6hkDAoBxI8aFdyQDuxqYRD9NM0tbhscOwQqcHTejzF9FE3ngmYj-YZWvE9npZItX_RU2bMduZOAVXImpFIFNdNPIxAauUx2Ho" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9392768ed3.mp4?token=VDdu8J7Sw9kWcd7sdHwNB9-kA-I8rWT8-EFyVdS2GecxPwtMTyuIVSdTUBt45sacOcoPEzr9Tt3U6zB1FwjwSwgiiR4Q8Ffi1vQYWqvzNVpgyLiNBvVoD4sXGhlHHBp6WyBWXdSVxUOWyO1Pc2BxsH67N9CDVghxqHjzehfvej7DZIYd5VeuhhtjIFFHo5PzZylwi0x80MH1TynFfYoET-ZgMFIVQV2bzDBm-vnaeBRO4nP9UE1ggxTLxfSIxKJfBNbmev-7B7BD_nmAMwJSg2TPvHPRJb6c7lLlt3r7i7E4BxuitM8hHRy5Kmc46M2CGpgZWAjx2-zZLUuHJtbgpEhaSLHPrzvjGAlNEAuq9uBET1I5B409wb3RsQCj0lmTDmJXILRvgZwwjvi50g9Su1Alkos9Ucbe3cBiBKqIbMD8iyCWBGppXcnJlhddSWUmFZB56PNImfHarI2Xa2lw4kazlkv0F0kUO8CV02zhu3LfZ_CYwWPmQQs-r7pxunMZmNdzDotCjQNmaq67d6AP3hVQ-Ueukl-PuSOtXBnBpPMv3WTJeteKNoHC2z9YODQFCS16G8yOFm6hkDAoBxI8aFdyQDuxqYRD9NM0tbhscOwQqcHTejzF9FE3ngmYj-YZWvE9npZItX_RU2bMduZOAVXImpFIFNdNPIxAauUx2Ho" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ :
رهبران جدید ایران باهوش هستند، بسیار باهوش.
آن‌ها بسیار کمتر تندرو شده‌اند. فکر می‌کنم آن‌ها خوب هستند و واقعاً کشورشان را دوست دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66374" target="_blank">📅 19:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66373">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885ecefd64.mp4?token=mY2pRtF9eztwNkCbCLktnTAS7w5FRAlgZfqptuf7q59SNq0bttkZ32Gb7WKjhNIqS8IW6bJDMtMMuw3Awmd8F8wODoEStGhDNuIjowdjiSqG1f8jWC4OB8rZjbSCumGm3_-OHu1h8YUJ8_NpacQey-jxrxVODTdtf_KuMtXCY8Os9Qpg95ynL4o8yW1kmQjFQ_t0LIPfUqEiGGowYenXo0fPJn2_rZ08VJc19N9UKh52SGKISMqNW856rm5923dUoDnOe84wYDMMwWbBmhQ9tN8vET7ohMuNY0eA5GkcQKGrIDjxfpUNZ47iK1yW55DZkpPkXhpJO3v0ZBV-yXsWSF7xXZRhKjutn-hqS7aeCtPHg5_mQxWPub1GnNEj889GmvMRRUgxuCTlbNQmi8lcKi9YMsdqnmH02IhBzLM43KIRRWbLkGTWme5ocF5h-nAJCSfSD83jTXNXyend1QNN7Pk2O8tmmdhWws7RCq_kyEteRGniyv4vDcx083w6bPGjsnOj1S21PVt7vsKTVqtaqmfmeqdcga7U34jB5E4Ni4Qw8Hkg-S1Kc-e97Yv_kj_LgaCKEovyRW53dxSdDlVPOMTCR2w2xpYUgJbNqGXhhZ75ThsrYlo79h8E-qfzpsz0fZz4w3CDZpNW8WEePSRHaI9SbxSo2-e7fvmqZ_EDfZ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885ecefd64.mp4?token=mY2pRtF9eztwNkCbCLktnTAS7w5FRAlgZfqptuf7q59SNq0bttkZ32Gb7WKjhNIqS8IW6bJDMtMMuw3Awmd8F8wODoEStGhDNuIjowdjiSqG1f8jWC4OB8rZjbSCumGm3_-OHu1h8YUJ8_NpacQey-jxrxVODTdtf_KuMtXCY8Os9Qpg95ynL4o8yW1kmQjFQ_t0LIPfUqEiGGowYenXo0fPJn2_rZ08VJc19N9UKh52SGKISMqNW856rm5923dUoDnOe84wYDMMwWbBmhQ9tN8vET7ohMuNY0eA5GkcQKGrIDjxfpUNZ47iK1yW55DZkpPkXhpJO3v0ZBV-yXsWSF7xXZRhKjutn-hqS7aeCtPHg5_mQxWPub1GnNEj889GmvMRRUgxuCTlbNQmi8lcKi9YMsdqnmH02IhBzLM43KIRRWbLkGTWme5ocF5h-nAJCSfSD83jTXNXyend1QNN7Pk2O8tmmdhWws7RCq_kyEteRGniyv4vDcx083w6bPGjsnOj1S21PVt7vsKTVqtaqmfmeqdcga7U34jB5E4Ni4Qw8Hkg-S1Kc-e97Yv_kj_LgaCKEovyRW53dxSdDlVPOMTCR2w2xpYUgJbNqGXhhZ75ThsrYlo79h8E-qfzpsz0fZz4w3CDZpNW8WEePSRHaI9SbxSo2-e7fvmqZ_EDfZ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پرزیدنت ترامپ:
روز یکشنبه، ما به توافقی با ایران دست یافتیم که به همه چیزهایی که در نظر داشتیم دست پیدا می کند - همه چیز و خیلی بیشتر. جلوگیری از دستیابی ایران به سلاح هسته ای همه چیز در مورد همین بود. این حدود 99 درصد بود. آنها نمی توانند آن را توسعه دهند یا بخرند. آنها هرگز نمی توانند سلاح هسته ای داشته باشند
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66373" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66372">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/66372" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66372" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66371">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1h1HT91rQtw-B5iFGd4KY0zgsKlqebtopzm70OsxHjDOMZtRsL8QKcX3F_uVHVUa4b9BZb8TN3Z22LKqTQ6dmhPfYwuyoG16DLTPyfLubXWNh6EJlBvzgUz9PuyFCE4Abi3GYil6yiWKGrnMWGfW-2yXJetyH8fOPTSZA2lLhkOumLxxC_ntyFVZVwGSLG5SV-Yc-qmT86muXIbEyeyXbvMbE_Q6LA9eyVMKOMVVPYFjs_9eFOZNDM3vAMgEKy6YStgSvp_DheDFwpMdoRcEAKHIS4Wc88BVp5STY0MI3YONVGcF4EcbY-bRdyhCvTfZ_-JGpKE2cZH0hi0weRh4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66371" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66369">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkLNolsWox4kIEzT2r3qSLyJa95V4SVqBfhsx9-nYiKIuk8eZGE9r1KRFPYgmront2CWR3jbEkra6icdLr7vdZvuDtJiZPthMAY8oXHjh0X4ykOLfNA3F_QWbnfn3sPdHb-L1V1_H1QgWjAh8vPq-wG6P2FY6wpACmS-m_RUDRc9sT4K4F1lqe42tkBNoO7vhQ2di6ki8w5kTLWxHcbS9bZAGG1_T1LkKBoftClcPiPJDVvCa8oIIMFBWkHDeLwLbpdMcY_DJtqzgXnHANclnfiv4yjG0akmYa6cF_PzT7w2cZZiwtPheA4v1MyNJ25WHCyCv4ttw3YkFDxwZubNmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
توییت قالیباف:
تعهد ایران به همکاری برد-برد که بر پایه مشارکت استراتژیک جامع با چین بنا شده، قاطع است.
در جلسه‌ام با اتاق بازرگانی ایران تأکید کردم: ما مصمم هستیم که اجماع استراتژیک خود را تحت GDI به نتایج عملی تبدیل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66369" target="_blank">📅 19:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66368">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53224e4497.mp4?token=oQmzosc0rop95sPNvCzAwDGbH2CZAbMZXF6K0D_TUj7xw3CZb_X72nFTrNNWYck1iIf90jxalacqnylpOIgSsTPMgK1fgIJyXv3Yx_UNbenWKJoB2M3_dyaenyjyQZUKJG38O7UyTP1-W3F7OLRGYjPKVDVP-ZEqgb3mPytyznuamykdfUcGe0ty08JUMoWLel8wuCsUJk0DEL_noZT9AMRcKUAI48pLWHXfnFxQSOHF6Xo_PrD-Kl7jfoG2GoInUfSmLiJ2VpdhlBIp1k7FvHpYVq7CHAW3F949OTPM1KExZpCuCSlN2Yars8jLtvLG2zCx30rkexDghCHd75vmZC57IDTtFxpHp9dLXoINO2VJ0Yt1VcCLN0ceNxgpSYP2s6QNCyoMstUrwG17oWXWG6a5u-mtknx_yPh6_l9mPhdq-T-JbfOG4aG25A4HXsYZ-N-LMkdiewmooJgJETzbNV4S017VNZ7NQ_m4hBiYV0EhNmSgzY4BvIZZsXCqnpexZhxaR92_ZVAa8k0coHLK2im1X4Wg0S8HSWc4ZhsRz1Mc_q5vBC5qOUkRG9WGZunU6psW6EClOirpVIWDGMauLM0oM_S-cSz7ePfafSn3LGsBEdNoH0gFgE-lf-OCQgapBvqdz_xY1AS69px_15tpFkHAmKaDaClw5gphXSNhGGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53224e4497.mp4?token=oQmzosc0rop95sPNvCzAwDGbH2CZAbMZXF6K0D_TUj7xw3CZb_X72nFTrNNWYck1iIf90jxalacqnylpOIgSsTPMgK1fgIJyXv3Yx_UNbenWKJoB2M3_dyaenyjyQZUKJG38O7UyTP1-W3F7OLRGYjPKVDVP-ZEqgb3mPytyznuamykdfUcGe0ty08JUMoWLel8wuCsUJk0DEL_noZT9AMRcKUAI48pLWHXfnFxQSOHF6Xo_PrD-Kl7jfoG2GoInUfSmLiJ2VpdhlBIp1k7FvHpYVq7CHAW3F949OTPM1KExZpCuCSlN2Yars8jLtvLG2zCx30rkexDghCHd75vmZC57IDTtFxpHp9dLXoINO2VJ0Yt1VcCLN0ceNxgpSYP2s6QNCyoMstUrwG17oWXWG6a5u-mtknx_yPh6_l9mPhdq-T-JbfOG4aG25A4HXsYZ-N-LMkdiewmooJgJETzbNV4S017VNZ7NQ_m4hBiYV0EhNmSgzY4BvIZZsXCqnpexZhxaR92_ZVAa8k0coHLK2im1X4Wg0S8HSWc4ZhsRz1Mc_q5vBC5qOUkRG9WGZunU6psW6EClOirpVIWDGMauLM0oM_S-cSz7ePfafSn3LGsBEdNoH0gFgE-lf-OCQgapBvqdz_xY1AS69px_15tpFkHAmKaDaClw5gphXSNhGGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ درباره ایران:
معامله‌ها شگفت‌انگیزند. من تمام عمرم معامله کرده‌ام. وارد معامله‌هایی شده‌ام که صد درصد قطعی بودند، اما اتفاق نیفتادند. وارد معامله‌هایی شده‌ام که هیچ شانسی برای انجام‌شان نبود، اما انجام شدند و به آسانی انجام شدند.
پس هرگز نمی‌توانی درباره معامله‌ها مطمئن باشی. اما خیلی زود متوجه خواهی شد. فکر می‌کنم انجام خواهد شد.
آنها می‌خواهند امضا کنند  می‌خواهند به زندگی عادی بازگردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66368" target="_blank">📅 19:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66367">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ca2e02c1.mp4?token=KJ-eOEpoY9oKrtMBJkDSFhLYjpHzgTigifAhwE7_XdVrUGVYWFym_3C6auDCpDSTgGZgjhhJ8syX8nNkP6M8ZjIPKzP0pgfRs4A5Z6HkPcPAtMqf2G5cc0q_5xhs3gjAY_lX-pvfT_hWkHl-FY4vVndkEAMwTUGs3u530B1KbHNs3ErDRojz8op8c3fZ4omoXXmaj6LT8q8MKs9g2lZ2hcFRYpzVGufQetG-FjucfDl4L_wZxGQLfs1-tcGfk_ulvqhBUbNKbVr08XVt8mO84RmsxP9JcGVs6BdWxoA7CoTosEdV3OLpw65rvTGLj97uT_ibLJwhgibx93_RuJAgkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ca2e02c1.mp4?token=KJ-eOEpoY9oKrtMBJkDSFhLYjpHzgTigifAhwE7_XdVrUGVYWFym_3C6auDCpDSTgGZgjhhJ8syX8nNkP6M8ZjIPKzP0pgfRs4A5Z6HkPcPAtMqf2G5cc0q_5xhs3gjAY_lX-pvfT_hWkHl-FY4vVndkEAMwTUGs3u530B1KbHNs3ErDRojz8op8c3fZ4omoXXmaj6LT8q8MKs9g2lZ2hcFRYpzVGufQetG-FjucfDl4L_wZxGQLfs1-tcGfk_ulvqhBUbNKbVr08XVt8mO84RmsxP9JcGVs6BdWxoA7CoTosEdV3OLpw65rvTGLj97uT_ibLJwhgibx93_RuJAgkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار: آیا می‌خواهید اروپایی‌ها مین‌روب‌ها را به هرمز بفرستند؟
ترامپ: ما به آن نیاز نداریم، اما اگر بخواهند بفرستند، خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66367" target="_blank">📅 18:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66366">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06239668e.mp4?token=j0YCWDBX-r9pOe0kNaJik2ic1d4QKaUB-Vs5oEg1e-bAYPM1kLdCa5RjCKIoSHCbksdkubfcXgCjBFspziLORUlneP2qWA9GMB--uKiVrf6JHy7OUHi-oKYdi5RMU-tQYNUcdFnxxIczN7-vNZ6BomIglo8XBq3dVTgLwSFKY770Y7TsNOx2p3QzT1NxpihbCJ4Qfju-o_JVp6PzGGW_jFVh7TPWR-qjV1tsvVlOG99PBKAK2XpGD6WYJn9ABHTvg5Tnzrdi4xTaRU1x1qe-3sZQB6RRiQnWIANmq-IVC24Sf7f5ciWGzx5SGvleqGSvvEp4NeAYVmEqM62RCIcSlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06239668e.mp4?token=j0YCWDBX-r9pOe0kNaJik2ic1d4QKaUB-Vs5oEg1e-bAYPM1kLdCa5RjCKIoSHCbksdkubfcXgCjBFspziLORUlneP2qWA9GMB--uKiVrf6JHy7OUHi-oKYdi5RMU-tQYNUcdFnxxIczN7-vNZ6BomIglo8XBq3dVTgLwSFKY770Y7TsNOx2p3QzT1NxpihbCJ4Qfju-o_JVp6PzGGW_jFVh7TPWR-qjV1tsvVlOG99PBKAK2XpGD6WYJn9ABHTvg5Tnzrdi4xTaRU1x1qe-3sZQB6RRiQnWIANmq-IVC24Sf7f5ciWGzx5SGvleqGSvvEp4NeAYVmEqM62RCIcSlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: آیا می‌خواهید اسرائیل عملیات نظامی خود را متوقف کند؟
ترامپ: من می‌خواهم اسرائیل بتواند از خود دفاع کند، اما همچنین می‌خواهم از تصمیم درست استفاده کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66366" target="_blank">📅 18:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66365">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1zwL0K7S73h2bAQJ3oDs8f_tg6ngJFrjt01JnVQmQ-WvivPv9KqHdBsgRAWNB9k-K5LZ3PFrVofUQBsF_OlaP5d-94S94NNWSE840FuK8gacqwKEX3ay2RNdhQElOwJ2STv_4libWu1uCS3yNoJ2EmZ9ngFE_zm1B6nqLTG21cki-vkTKYWh-ANyH_zzi-GXIWsFlHRLTEeLk3J7vhHRi5pGucgM28BiPtp3qe2umMYTs56cDKhNbzHIQglyF9uZ8lrGlX3LZPZjEiHw8UL01OnMkJZZNbu7SIni7eQgoJz12ABXh8kKsfd64BWx64w05v0q8gnKtelL_6qrUIPvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دولت سوئیس:
بیش از ۲۰۰۰ سرباز امنیت محل امضای توافق ایران و آمریکا را تأمین خواهند کرد و منطقه پرواز ممنوع برای تضمین امنیت اعمال خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66365" target="_blank">📅 18:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66364">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljYj1yIMbmGWhfgQ5pQg4xD7cecn6szXfFC8F_4OY8QlXOUX-H_FiA1mmRZHAchjiHQA5fib7XoBxb2tJANGjt8JXkG45VNDOe9hDFYK-H508_e1T3fBbHFgtiGs0Mc7F6d_euXrAO57rMxgRBGyX4eLdQKfNKOfJGZ6kxwhO9QpqmIpGgsvmpScvRz7-xncduW0h8nQvTWFiOcn0DN83hOwmadZWnjg0Nl9v8aBFKQETfev1NycORQKnzDoFdernuYj8RgiwFTjnvKv8wLaWVoLPCWtbEUAmbSnBu_J__HKm5TT4Mp2NwRajRYhPN-b1YG9lJVOt3qBbuo6ssbusw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزی ۹۰ میلیون سود از جام جهانی
⚽️
برای پولدار شدن تو ایران چنل زیر فالو کنید
⭐
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
1 دقیقه لینک برمیدارم
❌
❌
❌
سریع بپیوندید
🖱
سایت های شرطبندی به دنبال ترورش هستن ، به عشق مردم داره میگادشون
💀
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66364" target="_blank">📅 18:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66363">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njXDPylZRxaVbT8quDdSPABlyFDWFMWM237_vbHGgho-SM74C2YEQ23D60w0Y1_1BoovI95p-S3pPFQHu32LetaG7SzFPkdKddHF-6Gvo90C7d33IbP_MX-7ZpM6FDKOWdk4wr2BlcrEiur7ZLLx0Z_KJClZgpbiNU-sn7xcFKUXum9vRdl6fESbl4Wt2Rhn96PLAfpa6wiuwDtKMli852JyxD5y1KQoXGcPuwDTSwciQzmsY8fb1oHhJudJJ3rEKqH1K4UjhUXUWfAUhj0AC7h-5dbRKXl1muhePDIGpk_q4lFI48NL6u075La0ZDDjDp8AJ87CBUoj5MOd89SBFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ در تروث سوشال:
۴۵ دقیقه دیگر از فرانسه یک کنفرانس مطبوعاتی خواهم داشت. سپس برای شام با رهبران فرانسه و دیگر رهبران اروپایی به ورسای می‌روم و امشب به خانه برمی‌گردم! این سفر موفقیت بزرگی بود، اما چیزی که بیشتر مردم می‌خواستند در مورد آن صحبت کنند این واقعیت بود که ایران سلاح هسته‌ای نخواهد داشت و تنگه هرمز فوراً باز خواهد شد! اعداد و ارقام بزرگی در همه دسته‌بندی‌ها برای اقتصاد ایالات متحده با تعداد افراد شاغل بیشتر از هر زمان دیگری در گذشته. بیش از ۱۹.۱ تریلیون دلار در ایالات متحده سرمایه‌گذاری شده است، کارخانه‌ها و هر چیز دیگری در حال وقوع است، اما مهمتر از همه، اعداد و ارقام اخیر بازار سهام به دلیل توافق بسیار بالا هستند و به همین ترتیب، قیمت نفت در حال سقوط است!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66363" target="_blank">📅 18:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66362">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a882497b26.mp4?token=DRGTJRisqKX3n6BHGnP3_G7l7aGULsmhirj_oXTn254QbP3BzgGdNAb371p1bCi-C3_uj8OukIdYFIV8GCx4R94kPggw0wZCDL8Radah08GYX57a3Ew2HHblARkPl3bVcnYSCB5btjqElRBGNXWtrwyzesCsaclQpYxAL1_bJxr3WUCBO5SYyu_efEMkM1IgaSYv9cAdBKWFSlBnFHC6c_skCk82BSiqw6KoYB7j2CkTQ_elSqGkGkYWEbzUiXiIAQKS3iA-cBFKCB1Eu72N1i02U-wXlDjsAK31tWXZqux94i-wdC4ylR1VrcDhvA4SE6TozJ-84nCZsHme0L03Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a882497b26.mp4?token=DRGTJRisqKX3n6BHGnP3_G7l7aGULsmhirj_oXTn254QbP3BzgGdNAb371p1bCi-C3_uj8OukIdYFIV8GCx4R94kPggw0wZCDL8Radah08GYX57a3Ew2HHblARkPl3bVcnYSCB5btjqElRBGNXWtrwyzesCsaclQpYxAL1_bJxr3WUCBO5SYyu_efEMkM1IgaSYv9cAdBKWFSlBnFHC6c_skCk82BSiqw6KoYB7j2CkTQ_elSqGkGkYWEbzUiXiIAQKS3iA-cBFKCB1Eu72N1i02U-wXlDjsAK31tWXZqux94i-wdC4ylR1VrcDhvA4SE6TozJ-84nCZsHme0L03Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نه از دوست شانس آوردیم نه از دوژمن
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66362" target="_blank">📅 17:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66361">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7f967b0a.mp4?token=aFW4N9Ya90A6pL32P8VRQNsGQtD0EYHKyVjXtoqchmtTm1R48FfGsmvgojJtvQswui6UVICyVHX7MpOtYhig7N3CM7ccCiEGdlUxnKYYzJrT9WJYvMwpCZbhgir5hc5mcA1bGWuWlKuSpMR7wYZCsfdQ98TIb-QXV_xJTkv8kbiFad-edB_jz30UCiEvN53RUjPQH_ET0YYlQS7OG8s2kHYaSn9F26um_ZrS-KO0zmVWACjl6aI2t_3kzA4X9RJdWMpcV1v51Exuw_O-fmHSOICy37QN_yRB14PaEZH46lFdZCJKoQl6cjLEOmRERSCw_uQxiJEjIFrAiHWIqXHaDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7f967b0a.mp4?token=aFW4N9Ya90A6pL32P8VRQNsGQtD0EYHKyVjXtoqchmtTm1R48FfGsmvgojJtvQswui6UVICyVHX7MpOtYhig7N3CM7ccCiEGdlUxnKYYzJrT9WJYvMwpCZbhgir5hc5mcA1bGWuWlKuSpMR7wYZCsfdQ98TIb-QXV_xJTkv8kbiFad-edB_jz30UCiEvN53RUjPQH_ET0YYlQS7OG8s2kHYaSn9F26um_ZrS-KO0zmVWACjl6aI2t_3kzA4X9RJdWMpcV1v51Exuw_O-fmHSOICy37QN_yRB14PaEZH46lFdZCJKoQl6cjLEOmRERSCw_uQxiJEjIFrAiHWIqXHaDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده رضا پهلوی: «صرف‌نظر از نتیجه این به اصطلاح مذاکرات، این توافق پایدار نخواهد بود»
شاهزاده با رد مشروعیت هرگونه توافقی که بقای رژیم تروریستی جمهوری اسلامی را تضمین کند، تأکید کردند: «صرف نظر از نتیجه این به اصطلاح مذاکرات، این توافق پایدار نخواهد بود... بقایای این رژیم هرگز در نظر مردم ایران قابل قبول یا مشروع نخواهند بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66361" target="_blank">📅 17:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66359">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e17877e6a5.mp4?token=DrzU_CDYHc1FzYPyaEcIKzD8Ol49ZHwC4mNgTqc7IS508BVGqEy-OU0hkrWD3g55oa4FVcU_u1kekf0pderlyGuGD4iMMF9YEkQKg37Bhe_4sx196Vj4SmHKRIKM6Oog2x-7QdqvQHbfW2P3Yn9Hg-dAJ2HZEewDL6iMo-Qnad-UhjFptNQZZ1PYufL8qTs-1Y5sk4OHdXNCaPXNh_l-5H0gyi1aKKkMQTU2mBZHUhW3499Eu4Zqay5qvhXSvOgl5Y6iekid0F4CjUNSlMJ_nETrOKdy5l0aUTHQC2TTAVyoJ8yEDbgsmO6k-bsbkfU0IRKjmqRaGTjf2P0S0OUVi6mb6yqoQcK0HJvHx9kNJcnmrEX505lcEB-x9143-T_-2PAZ31hOubeJdcm1gAR_JTQbwcWf89wB6Y_ZrrXTm7W2p8xFGZKgpJe2AMKVje7xar-D6ICtCX5X3ApSmQIDD3KObryyyl2ikgdmQub2yc6QB49wb25qyS-c3J264v8s6yoDfiZdwU1b7VT_FgGjHsNvsOm4n4BeTJ0QOCv36QbTIm7VPJW1Vu-ietO6mDexKqLXBHoKOTiKBOVl0x1-8361P4wtMp9O-e9yIqF7-cOPZIqPT5Hclsa3qyor2fJFyEXb3xhBLlrb09q3H3FA7tN86Yf3afGDE3XC7aOI5MU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e17877e6a5.mp4?token=DrzU_CDYHc1FzYPyaEcIKzD8Ol49ZHwC4mNgTqc7IS508BVGqEy-OU0hkrWD3g55oa4FVcU_u1kekf0pderlyGuGD4iMMF9YEkQKg37Bhe_4sx196Vj4SmHKRIKM6Oog2x-7QdqvQHbfW2P3Yn9Hg-dAJ2HZEewDL6iMo-Qnad-UhjFptNQZZ1PYufL8qTs-1Y5sk4OHdXNCaPXNh_l-5H0gyi1aKKkMQTU2mBZHUhW3499Eu4Zqay5qvhXSvOgl5Y6iekid0F4CjUNSlMJ_nETrOKdy5l0aUTHQC2TTAVyoJ8yEDbgsmO6k-bsbkfU0IRKjmqRaGTjf2P0S0OUVi6mb6yqoQcK0HJvHx9kNJcnmrEX505lcEB-x9143-T_-2PAZ31hOubeJdcm1gAR_JTQbwcWf89wB6Y_ZrrXTm7W2p8xFGZKgpJe2AMKVje7xar-D6ICtCX5X3ApSmQIDD3KObryyyl2ikgdmQub2yc6QB49wb25qyS-c3J264v8s6yoDfiZdwU1b7VT_FgGjHsNvsOm4n4BeTJ0QOCv36QbTIm7VPJW1Vu-ietO6mDexKqLXBHoKOTiKBOVl0x1-8361P4wtMp9O-e9yIqF7-cOPZIqPT5Hclsa3qyor2fJFyEXb3xhBLlrb09q3H3FA7tN86Yf3afGDE3XC7aOI5MU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای وایرال شده از ایونت های شبانه تهران
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66359" target="_blank">📅 16:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66357">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyUJQ-vKzfkECmdoMWOjGOe1_Xogs_O-jWJl9zvDFLTpeeC-ZqI_dc1719jmkYPhz_nnJ8Oot6TZIz11yszmlxJ5uGB7p800vT51j7xQ4HOUCUwATSf9295PqHawRS6dcz5G0_9AfWbwbwRh0ILexoNphu2nSMGCnp_u6fmFVHdx2EnxOU6XQ4fiTMlrfHu_Fk9p5b6RwpQsy9Dqm1KMBnypGid8zLmzuFYYNy2sg0kLozus8SixnaFrhDjuxU2nTFAplZVZh6CATwcBmMpwb63e9lJol1oSCjzV1HUb4GjBny1WnSgnCSoddzoAK6j2dfZhVm-n9wrQKHq9sirOZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/145629d21c.mp4?token=oekLfEcIVukOh72xD3UF147nCUDI1yED32Y5fpDXNNhYAtmR-cvk9c4bELrb3ZjxSZYy6WdmcVeUykQBY3PYK8Ro8rj4XF7FpJ4BXACmiR3eBuz1d0_-cdusO6WTlstPvpXs8vbNJ-oLfBVVx_bGII_w0QqSAW7pIGQVOhSIiAwSVQ9oKmopSDpG4eAUyckn7-Yg3EaLagf-q9Py0KJ63lYBJClCRbqv5b-yS8PTfE-KzdSAV-_HqzjOKTcMApa_iV1F4iOnHhyCS6oeGgkw9B1IHpQS1mj9C9Fv-WpKKRnEl7UqNcntHEJvtVrMjgVuPpZU3-BIaH7Y3opa_E2wSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/145629d21c.mp4?token=oekLfEcIVukOh72xD3UF147nCUDI1yED32Y5fpDXNNhYAtmR-cvk9c4bELrb3ZjxSZYy6WdmcVeUykQBY3PYK8Ro8rj4XF7FpJ4BXACmiR3eBuz1d0_-cdusO6WTlstPvpXs8vbNJ-oLfBVVx_bGII_w0QqSAW7pIGQVOhSIiAwSVQ9oKmopSDpG4eAUyckn7-Yg3EaLagf-q9Py0KJ63lYBJClCRbqv5b-yS8PTfE-KzdSAV-_HqzjOKTcMApa_iV1F4iOnHhyCS6oeGgkw9B1IHpQS1mj9C9Fv-WpKKRnEl7UqNcntHEJvtVrMjgVuPpZU3-BIaH7Y3opa_E2wSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جنگنده‌های اسرائیلی مناطقی در نزدیکی کفر تبنیت در جنوب لبنان را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66357" target="_blank">📅 15:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66356">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2f9733be.mp4?token=TURWPMAZ0lhLgwaTXqbT5iCNMDnvB3nTRgkfoNdf3qXOn9EPJoUexlDFFNDiJIi0A0MkXW4V77PMkSwwG8IMBUrknFvP0UX1SkFdTbV-yUR5Y9sueotVz9eBqQL0ljyjWCbGOQDf8pQOcbX4TiIsP57VHu4wqHKt3peLf34GfptbDHUcgRAuPattlnhLi0lheSz5zWxdLk19S-TyDXL2xyWN2vNvU5qdcEWYuWx1aTEm-2pzGxPkCDsPOq8WSM95iUanh5gnFbeT0YZRgcH6rQuNCKSdcTV4lsD9LyJYK5W25en934cMKD4JbaDmEW3RnEPPYzsly1l86XLHlia8eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2f9733be.mp4?token=TURWPMAZ0lhLgwaTXqbT5iCNMDnvB3nTRgkfoNdf3qXOn9EPJoUexlDFFNDiJIi0A0MkXW4V77PMkSwwG8IMBUrknFvP0UX1SkFdTbV-yUR5Y9sueotVz9eBqQL0ljyjWCbGOQDf8pQOcbX4TiIsP57VHu4wqHKt3peLf34GfptbDHUcgRAuPattlnhLi0lheSz5zWxdLk19S-TyDXL2xyWN2vNvU5qdcEWYuWx1aTEm-2pzGxPkCDsPOq8WSM95iUanh5gnFbeT0YZRgcH6rQuNCKSdcTV4lsD9LyJYK5W25en934cMKD4JbaDmEW3RnEPPYzsly1l86XLHlia8eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
فراموش نکنید، هیچ‌کس تا این حد در مورد ایران سخت‌گیر نبوده است.
این کار باید توسط کلینتون و باراک حسین اوباما انجام می‌شد. این کار باید توسط بایدن، بوش و بسیاری دیگر از افراد انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66356" target="_blank">📅 15:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66355">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048f0eb68f.mp4?token=Y60DX2Dx879-8k_zQRh0hhjDi3FzkeQTgtoLdYhmZ9vOVZzdH8NhhGusYcjR1fxRUBD27BWzd0ZJSzJrtttych7WobKjRRChuCTQDhuoSVG2Al2O6Bi-HKfMiWpqhRsG1unZzugk-ORjfSy13LE58uIuFFiSwJjBVKtValFq2n9s4VA4uJrIFqSx9AyT-37qXtoacBWB10_awFzREHWGo7rHRH7Zw2pQu8J7DN3iuQROSxQ73TdWYvtdqavKq0Ut5S6ZjnXNfIbaMQzUP835KqxVsoUmNMJ766vrVPB1-nWRs5MOJRaiG3OSeQOKGUDGG6QO7KsI3UgHPevgHCyykQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048f0eb68f.mp4?token=Y60DX2Dx879-8k_zQRh0hhjDi3FzkeQTgtoLdYhmZ9vOVZzdH8NhhGusYcjR1fxRUBD27BWzd0ZJSzJrtttych7WobKjRRChuCTQDhuoSVG2Al2O6Bi-HKfMiWpqhRsG1unZzugk-ORjfSy13LE58uIuFFiSwJjBVKtValFq2n9s4VA4uJrIFqSx9AyT-37qXtoacBWB10_awFzREHWGo7rHRH7Zw2pQu8J7DN3iuQROSxQ73TdWYvtdqavKq0Ut5S6ZjnXNfIbaMQzUP835KqxVsoUmNMJ766vrVPB1-nWRs5MOJRaiG3OSeQOKGUDGG6QO7KsI3UgHPevgHCyykQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: نیروی دریایی آمریکا هر شب بین ۱۵ تا ۲۵ کشتی را متوقف می‌کرد
دلیل پایین ماندن قیمت نفت این است که ما هر شب کشتی‌هایی را که شما حتی از آن‌ها خبر نداشتید، خارج میکردیم. دو روز پیش، سه روز پیش و حتی یک ماه پیش، ما ۲۲ کشتی را خارج کردیم. به طور متوسط هر شب بین ۱۵ تا ۲۵ کشتی داشتیم و هیچ‌کس از این موضوع خبر نداشت. نیروی دریایی ما کار بزرگی انجام داد و به همین دلیل قیمت نفت به ۳۰۰ دلار در هر بشکه نرسید. قیمت‌ها به ۱۲۵ تا ۱۵۰ دلار رسید و اکنون حدود ۷۲ تا ۷۳ دلار است و حتی شنیده‌ام از این هم پایین‌تر آمده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66355" target="_blank">📅 14:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66354">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7384906c.mp4?token=DaTzBbux7CWQD4v6LVSTJzdPhIwfQ-1JrU0Fx_ziqYjl6ygZFDsVlI90uVQNm6_CBwnFS6A1Hgb0wKwizNVO9e0reIzs73k2Z_ZaRKk4KfXgTMDD1xm9ABxJ84q4pvv5Z18AwfB2d7kSaHlTVftFLbcxbSWDXvZb34LC1JkinW8FQoHcZUd86LQS2vtvoSfdB0dM2GozpNoKVkq7-8V_OfqbqUc6WlBFI02I0vbcZodzjuP4YeuTpFyw2LhIG5z3n6qVZ49duyAhTNihx4XmUh6002Urfzi4WDnTIHEzTs4bxFwYEoTPPW2i5w-OlVQCSx6OrKH5dCspleUfuvnYOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7384906c.mp4?token=DaTzBbux7CWQD4v6LVSTJzdPhIwfQ-1JrU0Fx_ziqYjl6ygZFDsVlI90uVQNm6_CBwnFS6A1Hgb0wKwizNVO9e0reIzs73k2Z_ZaRKk4KfXgTMDD1xm9ABxJ84q4pvv5Z18AwfB2d7kSaHlTVftFLbcxbSWDXvZb34LC1JkinW8FQoHcZUd86LQS2vtvoSfdB0dM2GozpNoKVkq7-8V_OfqbqUc6WlBFI02I0vbcZodzjuP4YeuTpFyw2LhIG5z3n6qVZ49duyAhTNihx4XmUh6002Urfzi4WDnTIHEzTs4bxFwYEoTPPW2i5w-OlVQCSx6OrKH5dCspleUfuvnYOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: «می‌دانید ایرانی‌ها چه کار کردند؟ آن‌ها به اوباما خندیدند و به او گفتند احمقِ مادرجنده.»
پرزیدنت ترامپ با اشاره به نحوه برخورد رژیم جمهوری اسلامی با دولت باراک اوباما، گفت که مقامات این رژیم به اوباما خندیدند و او را «احمقِ مادرجنده» خطاب کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66354" target="_blank">📅 14:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66353">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bba81d7fe.mp4?token=HCPG8bvJnQL3dq6G3cuLMVWA472mMLLb-9x6sSRrOaHRIKv6K8RZABH0AHwI_WKHI9aX9C0bHFuTnXFgVaIB_S9oxQ2Dv59oT6oI7VLBu_2fU7yAY6thximPFJE-Drhu9B6_DHLSAq5qfxXGW_T0X-qcYZID59g2YlCY2QaX1oI_JyLJ6m3tZV-z4BHCVZQ3HMzFI3cvupBXjnk0AOBIZxG8N0FIZUnZdQ6QWEXch26fSluioDqOuCssfjPLyh7wq_6UKtvtxTGSP2jYx_r1Q-LXRC5P-Cp3FLyCwQuspKWwvbbTf68W6C3n7l8sHSPF0dUxDwJwF4N6LzY_GhKPUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bba81d7fe.mp4?token=HCPG8bvJnQL3dq6G3cuLMVWA472mMLLb-9x6sSRrOaHRIKv6K8RZABH0AHwI_WKHI9aX9C0bHFuTnXFgVaIB_S9oxQ2Dv59oT6oI7VLBu_2fU7yAY6thximPFJE-Drhu9B6_DHLSAq5qfxXGW_T0X-qcYZID59g2YlCY2QaX1oI_JyLJ6m3tZV-z4BHCVZQ3HMzFI3cvupBXjnk0AOBIZxG8N0FIZUnZdQ6QWEXch26fSluioDqOuCssfjPLyh7wq_6UKtvtxTGSP2jYx_r1Q-LXRC5P-Cp3FLyCwQuspKWwvbbTf68W6C3n7l8sHSPF0dUxDwJwF4N6LzY_GhKPUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
ما مردی به نام سلیمانی را از بین بردیم. فکر می‌کنید اگر او زنده بود، این اتفاق می‌افتاد؟او یک نابغه شیطانی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66353" target="_blank">📅 14:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66352">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff72e5160c.mp4?token=qsOt0zAd377znxytNFgDwInoKPONkJIfasNJEPrs5_S7y3Fum4l-GEsHYabE5nrI1KrSVBvV55hPWZMy7fj8JhLiRAe3goR-hJoaWRBjpSucRTMHhnN-5HK89MdmuNW7HVDOB4BN9YperdOgitm5LtkUAUs52GdycplpsXdWiNuPEPHl7MqwKt3I05QLv0nZbGnHecdqy4wo8szHZkOqUPWrdVKg0ZQKyA5ebJcSI0572t1fL8ab1qZEhfcEGQdOYoKrEWEuCA_3L_fGOmduXSg0mnJtM_R3EH0FZbB5G-nTzhET47Z6gwAlOZALnyW41WGsRyaW6mLgawA8lkqxzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff72e5160c.mp4?token=qsOt0zAd377znxytNFgDwInoKPONkJIfasNJEPrs5_S7y3Fum4l-GEsHYabE5nrI1KrSVBvV55hPWZMy7fj8JhLiRAe3goR-hJoaWRBjpSucRTMHhnN-5HK89MdmuNW7HVDOB4BN9YperdOgitm5LtkUAUs52GdycplpsXdWiNuPEPHl7MqwKt3I05QLv0nZbGnHecdqy4wo8szHZkOqUPWrdVKg0ZQKyA5ebJcSI0572t1fL8ab1qZEhfcEGQdOYoKrEWEuCA_3L_fGOmduXSg0mnJtM_R3EH0FZbB5G-nTzhET47Z6gwAlOZALnyW41WGsRyaW6mLgawA8lkqxzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: بازار از توافق با رژیم جمهوری اسلامی خوشحال است
«چه کسی واقعاً خوشحال است؟ بازار... بازار در حال نوسان است و قیمت نفت سقوط کرده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66352" target="_blank">📅 14:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66351">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a231223e.mp4?token=pZzrC-e-YrNSWqU81_pPQTWSw3eqtVUp_RPw4v6VueqsJPefw-fZRn21qPqcZZTWuPeEFZ0QIfWsisH92a8wLmFni94yOkaMnX9uj2gSlSNk6OqIiXTwDCWKHP0Mao9BiaXNM2MfZyFJEpmYfbBAsahMOIwvMh6bivIPQJI_ZBEC0zEB9C8i2qrb2x9C-yCDDFm2iCAIsNZkAACQTOobpxIGgnqFVNRbvkRYa-UuKcIlkR7oAkGlzMYoHYDt7iT03wOIZMajMlyMCr0Szbxn8v1jp2d7gB4kaEeIInZb0TZLT4IiiUt0qw5zvOtU-DCi7RifE5rrqHzNNPZGWfNlAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a231223e.mp4?token=pZzrC-e-YrNSWqU81_pPQTWSw3eqtVUp_RPw4v6VueqsJPefw-fZRn21qPqcZZTWuPeEFZ0QIfWsisH92a8wLmFni94yOkaMnX9uj2gSlSNk6OqIiXTwDCWKHP0Mao9BiaXNM2MfZyFJEpmYfbBAsahMOIwvMh6bivIPQJI_ZBEC0zEB9C8i2qrb2x9C-yCDDFm2iCAIsNZkAACQTOobpxIGgnqFVNRbvkRYa-UuKcIlkR7oAkGlzMYoHYDt7iT03wOIZMajMlyMCr0Szbxn8v1jp2d7gB4kaEeIInZb0TZLT4IiiUt0qw5zvOtU-DCi7RifE5rrqHzNNPZGWfNlAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد توافق ایران:متن نهایی نیست؛ این یک یادداشت تفاهم است.
اگر من آن را دوست نداشته باشم، ما به پرتاب بمب روی سرشان برمی‌گردیم.اگر آنها رفتار مناسبی نداشته باشند، ما دوباره به پرتاب بمب برمی‌گردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66351" target="_blank">📅 14:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66350">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7653e74d56.mp4?token=FJEhi5OmujtWaYpVQ5b8ZU1I41Ij9tehmifah3-HNh7F3psGOZd4qM1QwsZwvNXG__7O1R38PM498izF8Ck8qO1GKOZcYmXlQF5T8mqo9sLQ6WShTFermMh-X51dsXamvyi3E21xTfmQ6_R5DxuBRHgLyGhkZKzPqU9NodlzlpyJ6kgKqIhBs3jBOGQ1hMmxplmQqlSL4TunUjNs2n9Z0DZorLxx5hT8M_WcdQ_1rC6B_nqesrsm0IcV5ZZJGLkuXfMuNxmPfaljoOYePwonsXeCqwfK0ORmdhEkSdzYNi0yLZ9lakVimvCWYfhik1_LonzuwWRM_qcyYMpNpWdDzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7653e74d56.mp4?token=FJEhi5OmujtWaYpVQ5b8ZU1I41Ij9tehmifah3-HNh7F3psGOZd4qM1QwsZwvNXG__7O1R38PM498izF8Ck8qO1GKOZcYmXlQF5T8mqo9sLQ6WShTFermMh-X51dsXamvyi3E21xTfmQ6_R5DxuBRHgLyGhkZKzPqU9NodlzlpyJ6kgKqIhBs3jBOGQ1hMmxplmQqlSL4TunUjNs2n9Z0DZorLxx5hT8M_WcdQ_1rC6B_nqesrsm0IcV5ZZJGLkuXfMuNxmPfaljoOYePwonsXeCqwfK0ORmdhEkSdzYNi0yLZ9lakVimvCWYfhik1_LonzuwWRM_qcyYMpNpWdDzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد توافق ایران:
هیچ‌کس نمی‌داند این چیست، اما توافق بسیار قوی‌ای است.
به نظر می‌رسد اکثر مردم بسیار خوشحال هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66350" target="_blank">📅 14:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66349">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8de3b6155.mp4?token=N_Py0KvUbOHt-3Ov4KzfzHL1sTy1L9hi-GYChN4riGDn8ZW81GNNSDMwFtmTTdpGRoFCjGJra0_AwSpO6tMDB7E1siNTZMBi0qXIxjLWgVK8JGbHgNjkoJxLenGOMo3G4Q3irxvDpEirpqw8lTI3DSQg6oq-Hxpce3DH1qTDmgxc8I22XQJiKMH_3M2rDZN25z451FQClvnHvYhk1zShmGrTVOfWVKcoooxoQmkrTaexFv1w7_dPEYcq2QI5mIa-QN5qlkpU5f0BbSKNEI3fyOA2JpNtz1cctwCLcIYpQgj0eNozq67dP-kV0hYwk8Oink9OAHz3yU89oAF8jl4hWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8de3b6155.mp4?token=N_Py0KvUbOHt-3Ov4KzfzHL1sTy1L9hi-GYChN4riGDn8ZW81GNNSDMwFtmTTdpGRoFCjGJra0_AwSpO6tMDB7E1siNTZMBi0qXIxjLWgVK8JGbHgNjkoJxLenGOMo3G4Q3irxvDpEirpqw8lTI3DSQg6oq-Hxpce3DH1qTDmgxc8I22XQJiKMH_3M2rDZN25z451FQClvnHvYhk1zShmGrTVOfWVKcoooxoQmkrTaexFv1w7_dPEYcq2QI5mIa-QN5qlkpU5f0BbSKNEI3fyOA2JpNtz1cctwCLcIYpQgj0eNozq67dP-kV0hYwk8Oink9OAHz3yU89oAF8jl4hWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یسرائیل کاتز: هر کسی علیه اسرائیل اقدام کند، بهای سنگینی خواهد پرداخت
🔴
وزیر جنگ اسرائیل هشدار داد: «هر کسی که علیه دولت اسرائیل انگشت و دست بلند کند، چه در غزه، چه در لبنان، چه در سوریه و یا هر نقطه دیگری، می‌داند که باید بهای آن را بپردازد. اول از همه، آنها زمین خود را از دست می‌دهند و خانه‌های خود را از دست می‌دهند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66349" target="_blank">📅 14:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66348">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/831548d977.mp4?token=AputEPk6kerXhF1SU-QzpW2J1Jez9WD3NEmvANJr7WO910kyVX-tCJcvouaF5Ky95bRk8pMMQfoYmZm4cXQJHsetJkMiybWvk55_Wy92uAfK3Psma0nOG_jZu9GB4MWtISi91dlfaNNXJerTIOZRrC_V7KJnBT9wYAtX5BDurv5_gj3MTLb-FK9-Tpn0ej8r9whe9VeXt6PG9HylZE7PKkqNqWrUnXwrYZzlDRqWLkfsBpl_pSzaOEhCi8Ga4Y-kjGXrg8pzZqrLoQTssz83qzLP9RkjnqAi8rjs6PqpZMnuv8SjWYadgjj02nkyGTuWVBfMEN0_J_tsXYMPJu63Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/831548d977.mp4?token=AputEPk6kerXhF1SU-QzpW2J1Jez9WD3NEmvANJr7WO910kyVX-tCJcvouaF5Ky95bRk8pMMQfoYmZm4cXQJHsetJkMiybWvk55_Wy92uAfK3Psma0nOG_jZu9GB4MWtISi91dlfaNNXJerTIOZRrC_V7KJnBT9wYAtX5BDurv5_gj3MTLb-FK9-Tpn0ej8r9whe9VeXt6PG9HylZE7PKkqNqWrUnXwrYZzlDRqWLkfsBpl_pSzaOEhCi8Ga4Y-kjGXrg8pzZqrLoQTssz83qzLP9RkjnqAi8rjs6PqpZMnuv8SjWYadgjj02nkyGTuWVBfMEN0_J_tsXYMPJu63Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس و دیسبک بازی مسعود با خودش
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66348" target="_blank">📅 13:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66347">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51823a43bc.mp4?token=P14xslpExgT4BxhpyVHSGTRlbYe1llxHOmy_PDj5EXtCfdhP-evg1K8Alx46ceHhpfNwCzpyfZVYnarSZo-ESe4UVmDiksA4AaPjZ7I9O7z28AtL8ngFZZxsDDkbG87yTvCHLhD-7XCA6xaGmx4y_HxniMbALPLcnTcix6n2rVbTTyCqhssVUq5bBzUFOw5Cgd0uFjCwWI5-wNQ1bssF5pwK4javzDmf3BHOcKNFxggmAvZSjjH3snxW6xTcj36d_TIoE6k8DGFqnR1KX5FXkxXZ1iG2U70EnMT71m6AStTuvM5CyIqXO2fvlXIZnZEQtH7zKvkWDBdZStgEEs9fGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51823a43bc.mp4?token=P14xslpExgT4BxhpyVHSGTRlbYe1llxHOmy_PDj5EXtCfdhP-evg1K8Alx46ceHhpfNwCzpyfZVYnarSZo-ESe4UVmDiksA4AaPjZ7I9O7z28AtL8ngFZZxsDDkbG87yTvCHLhD-7XCA6xaGmx4y_HxniMbALPLcnTcix6n2rVbTTyCqhssVUq5bBzUFOw5Cgd0uFjCwWI5-wNQ1bssF5pwK4javzDmf3BHOcKNFxggmAvZSjjH3snxW6xTcj36d_TIoE6k8DGFqnR1KX5FXkxXZ1iG2U70EnMT71m6AStTuvM5CyIqXO2fvlXIZnZEQtH7zKvkWDBdZStgEEs9fGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاوره اخذ مدارک دانشگاه آزاد
واحدهای معتبر تهران
کارشناسی، کارشناسی ارشد، دکترا
با استعلام
💥
(
بدون پیش پرداخت
)
💥
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
Telegram :
👇
👇
👇
👇
@irantahsilat_iau
Instagram :
👇
👇
👇
👇
Https://instagram.com/uni.irantahsilat
جهت ارتباط با ادمین
👇
:
@madrakuni</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66347" target="_blank">📅 13:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66346">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1725e10790.mp4?token=UKJ4DgW0HQ8f1zXDMO7jEmgetQanr2-nIkOa1Fr7Qw1SoKtgRA0C4wpVRHj6r_IXxGm1iEWx0Gc6_aepzLhfuvpEpttGv3qV78UwTwK9L8mcpi704F5XZvQkU3kpskUv_pLvWm25cdKuPwhcN8jw4iqwHwfJM_9kth64_otn5YsUbcyWtPfL-2FTv8OLTC2LU835E7xVPCvf1FwfFA2hKutwXBeRIUP3lTJYrmuyrX197zbmqR85QnTwCyRYSu8X6XmxoM9qZfhOFb4Rjt6ZnvByb3_nwSNIC7j6OVtlphqGr1lu11ojINAkUG9mOxhdaITGKzU_oSIeGf3ZTtmnqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1725e10790.mp4?token=UKJ4DgW0HQ8f1zXDMO7jEmgetQanr2-nIkOa1Fr7Qw1SoKtgRA0C4wpVRHj6r_IXxGm1iEWx0Gc6_aepzLhfuvpEpttGv3qV78UwTwK9L8mcpi704F5XZvQkU3kpskUv_pLvWm25cdKuPwhcN8jw4iqwHwfJM_9kth64_otn5YsUbcyWtPfL-2FTv8OLTC2LU835E7xVPCvf1FwfFA2hKutwXBeRIUP3lTJYrmuyrX197zbmqR85QnTwCyRYSu8X6XmxoM9qZfhOFb4Rjt6ZnvByb3_nwSNIC7j6OVtlphqGr1lu11ojINAkUG9mOxhdaITGKzU_oSIeGf3ZTtmnqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
بالگرد کاموف ۵۲ روسیه برای رهگیری پهپاد انتحاری اوکراین بر فراز مسکو به پرواز درآمد:
در جریان موج حملات پهپادی صبح امروز اوکراین به سمت مسکو، یک بالگرد تهاجمی کاموف ۵۲ روسیه تلاش کرد یک پهپاد انتحاری اوکراینی را در آسمان رهگیری و منهدم کند. این تصاویر بار دیگر نشان می‌دهد که جنگ پهپادها تا قلب پایتخت روسیه کشیده شده و مسکو بیش از گذشته برای مقابله با تهدیدهای هوایی به ابزارهای غیرمتعارف و واحدهای هوانیروز متکی شده است. حملات پهپادی اوکراین در ماه‌های اخیر به زیرساخت‌ها و مناطق اطراف مسکو شدت گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66346" target="_blank">📅 13:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66345">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1vXXMdH8Sm1ij1Cg7vqMiiRNqiD67EVI1xIaSiB7zKqxKtlcNZ455Fw8Fv13nsUydsi53aHlONjQkdb98yVjJQVRzMWJ9g2Ku6o1EqvPCXeF_c31TvqSR9KLmGvc8_qOSKy5dYTIu7AaRhR0UuSvQ9W92Cl6sPgzH94KsnzNNkYh6MVquHUx1UiXiXhnKgM3o5XWPKdNcdsKkYVVoEBh5IWIYGluEndBTfXYI-hu_rksyFaryinyrbDXFNfxd-tSiK-yYlz1G5KqvQtVHMjnfxlpjKHqr69V-ww1tsl6BfPOxmTPphwMMEdvDhyL2PppdW9507hY1AekD9P_pccSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت مارکو روبیو بعد از شنیدن خبر توافق
😔
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66345" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66344">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66344" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66344" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66343">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMW2fK5UQ1OSFF10LCl_1YEt1ALJlPFQOWFpwt2yKpeF2T2eHZV79_-Q_5DEvLr1iIDneJzwMNYIHLnvV_FchnOPh6rT_VfLlM_7pwAQNmO9mur6c7-EmmRtg0Adfr3qGfFNuna5-fctPC8o_uQrakP4irnUJ45z9u1GM8xiydFOzQqV7sevzXGIevzv3GBvARbDG5zEZ9KEajBftixqdzXok627FLtUfdNm8b3J6_Js3ELyxkFUZtSydEJLGBFC2CPkXBB52wZ4zZd3NaHMjaysfcihU2Zd6UsC0B478FoEa9iBYakk4UbWSas6IknaEkYACqHZf0Es67wI8uRyug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66343" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66342">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgpzdSyY_br1ri7sgkkjRfmkHp0q2_L1e3-w2h7dQjlUMRc86GEJYQXFP2qxpPE_ms85_ia_rSC9k8jgxxEimV6UbEVl_fgIh_pzgsR4yM9xcgrR-kPq-FObwLFiR2vFzzeFaUUWwLJfeSx9Evw7pgdbFZYaub81W5LkYpQ7k8ZDj3z6BKtIFNwmCH-zN3HcxyuuAD83GmZPap4weat3h0XDuVvjPFAy1N_2aSn605ZDTJNHxKLknUnHaGi-zLprHEAl6WxOt6m0cRxNlKTr8wf0owI9z0Tk-gSEIFixoGeoLxuDLJwUg9d7u5HJKw6OaJgDJNHu2yOBKGzi582AWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
شبکه ان‌بی‌سی به نقل از یک مقام آمریکایی:
رژیم تروریستی جمهوری اسلامی با وجود اعلام یادداشت تفاهم با ایالات متحده، همچنان تعداد زیادی پهپاد به سمت شناورهای تجاری در تنگه هرمز پرتاب کرده است. بر اساس این گزارش، سپاه پاسداران از زمان امضای الکترونیکی این تفاهم‌نامه در روز یکشنبه، هر شب اقدام به پرتاب پهپاد کرده اما نیروهای آمریکایی موفق شده‌اند آن‌ها را پیش از تبدیل شدن به تهدیدی برای کشتی‌های تجاری، شناورهای نظامی و خدمه حاضر در منطقه رهگیری کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66342" target="_blank">📅 12:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66341">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uF5iai_GwUIR8790mIe9i__KaRmvB0A8IASN0ygJTkSfOYqjxg7ASNDqCYyc4uSea1nFz0DQ4ilSJDttxVl8KIDSZCD1up1_tcqs0X5Y4U9S-9AlniQfhBLFUBX84ci6CIagkNAHgeuzebdTIvUKLbEhxNDvdPv8UNu2YEOusGOIcB2rz-8eJm1cOdFV1aUrufc2lnqPa9dT2hbBlc3PIa1p-q754AzPMopqsGwmr2xXJf0S3vXEUSg5IXeLC9NVGpaDftHoDf8GHrNomVoKuOGFKacU0GpXxuI24M9AJBTvrb-yFqBd9pAuFqCX5x2xn8F1Nr0ydqoCTZiKH5JvXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تغییر چهره پسر ترامپ طی یکسال
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66341" target="_blank">📅 12:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66340">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d976a7f361.mp4?token=npspN0IWaokJdenge9DTBKK4kULHdOc6klyz_1cdqA9cvE9xi_b_zqVFOEoXjtnH9MAygthK9biVRlEbt3bgM5Y0YClB1W3uYKfkADNvqsGHvSR2CxUoY9EfE7SB2Jo9nHCiSJFywVC7rxCIcOOTGpzogKlUQFzKXF-sdFgnHMW9H_JMyCjyCf3hVFFI28eRfsV5GDuhSlX61wZGWcwzCjZ32OWAhlCwl9Yg-bI4KTn77YJhOmkj1lKr3_SJYm9tG70rxUDb4y5fODNYj12NtTbZsMVVTLageiUAlkLLel31uJws6LrJ0GaaViy8KmzuBNQUN2utwV0qlv_Os3G7ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d976a7f361.mp4?token=npspN0IWaokJdenge9DTBKK4kULHdOc6klyz_1cdqA9cvE9xi_b_zqVFOEoXjtnH9MAygthK9biVRlEbt3bgM5Y0YClB1W3uYKfkADNvqsGHvSR2CxUoY9EfE7SB2Jo9nHCiSJFywVC7rxCIcOOTGpzogKlUQFzKXF-sdFgnHMW9H_JMyCjyCf3hVFFI28eRfsV5GDuhSlX61wZGWcwzCjZ32OWAhlCwl9Yg-bI4KTn77YJhOmkj1lKr3_SJYm9tG70rxUDb4y5fODNYj12NtTbZsMVVTLageiUAlkLLel31uJws6LrJ0GaaViy8KmzuBNQUN2utwV0qlv_Os3G7ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تداوم حملات ارتش اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66340" target="_blank">📅 11:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66339">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac69a7be8e.mp4?token=LYD4nJau_1zyUWkPTMmLQFWYBzUOwrXCNtoWN3_xS0o6OIHLZQPOnaCiwJNfPUAMP93_9_LcyKukT-rmHZVxV-UytR76BCmh4chxNYC_cdbgQO71ljWYt8S6Ws2jPiRpNtp3LrenD5OfoQRl6WzjfzbfsCnI1IGSETq1pvdhzxGfKYyHD2gHsWAG1s_iKayKDX4uldroqk2wgs4SaURzamB3WAN5eA1bQpjtPejBU8zYuEKDsMxRwFp1oQGCH3N5YkYqEyjbgBrebHLNDf3WAhS74xvurKXPS2DvSrLnAvnSpGGMIU_9Zgm8ism4OoLyGUTxzhvELy5ySogX1VVbXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac69a7be8e.mp4?token=LYD4nJau_1zyUWkPTMmLQFWYBzUOwrXCNtoWN3_xS0o6OIHLZQPOnaCiwJNfPUAMP93_9_LcyKukT-rmHZVxV-UytR76BCmh4chxNYC_cdbgQO71ljWYt8S6Ws2jPiRpNtp3LrenD5OfoQRl6WzjfzbfsCnI1IGSETq1pvdhzxGfKYyHD2gHsWAG1s_iKayKDX4uldroqk2wgs4SaURzamB3WAN5eA1bQpjtPejBU8zYuEKDsMxRwFp1oQGCH3N5YkYqEyjbgBrebHLNDf3WAhS74xvurKXPS2DvSrLnAvnSpGGMIU_9Zgm8ism4OoLyGUTxzhvELy5ySogX1VVbXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
مایک پنس، معاون سابق ترامپ:
به جای توافق، باید اجازه داد نیروهای آمریکایی کار را یکسره کنند، تنگه هرمز را باز کنند، توان نظامی تهاجمی رژیم ایران را از بین ببرند و به مردم ایران یک فرصت واقعی برای آزادی بدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66339" target="_blank">📅 11:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66338">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ba759cb9.mp4?token=C_YPYS2ssyGhG6x9tY1rKk5ouurPtB8wctqppbJVvazHrj1X-6a94pb9XrdzrHptvNboxu9uRHnt9FpTtRb3c2OKuxFGFqeAancMzQkoMdo28K0963PmhK6cXuEPrAtXy548UQZXS_dPN4tgQE8oGwrNkT-ejfd08FqC3VAz-6A9I4RFEcHLkNynenUxC0gYWeptlmsNV0NwC0pBtAUBTXA5-Nb4LVf8iOY2TmU96QLWw2qDzDWnoaokmRY3JJuuD9IEE5loBBn3WnJI3JkJy8GgmUEg5GC-Il_hnPQc-acfrUYM9lZPfTOQKYmIYUTYURVdVhJDJcJ2MyOzvD5E4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ba759cb9.mp4?token=C_YPYS2ssyGhG6x9tY1rKk5ouurPtB8wctqppbJVvazHrj1X-6a94pb9XrdzrHptvNboxu9uRHnt9FpTtRb3c2OKuxFGFqeAancMzQkoMdo28K0963PmhK6cXuEPrAtXy548UQZXS_dPN4tgQE8oGwrNkT-ejfd08FqC3VAz-6A9I4RFEcHLkNynenUxC0gYWeptlmsNV0NwC0pBtAUBTXA5-Nb4LVf8iOY2TmU96QLWw2qDzDWnoaokmRY3JJuuD9IEE5loBBn3WnJI3JkJy8GgmUEg5GC-Il_hnPQc-acfrUYM9lZPfTOQKYmIYUTYURVdVhJDJcJ2MyOzvD5E4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسایی نماینده مجلس:
اگه کسی ذره ای عقل داشته باشه به جانشین شدن فرزند رهبری میخنده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66338" target="_blank">📅 10:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66337">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6FlT96s8dAfTOSGXm30vbHAKPTHFN3GsO2UPtZNdljgeSjf9VeiU3GJzZOt4t21-Gj0SEQ4U_EyleqYveU0ejWM_8T5RkwCxHe2VH1JmXJAdP31UWOkiyJpQU_fvbIgKO4r4JiPsl6Yjtw2m42GiRE6IE1ctsTls1WEXPMKb0i5F95aUB6TNyryWeNnmzFkktRh_s8ORhnFC-dae4q674McktTYywNgLKOxSObI-VH_US2eA-sseLPpakIyGQb-afiZwMjAfIGL-rhjOsN_Bwju00vTRlyHgLvhagk9eAaaxjpM_42nvqVsiiEXPrPKfa6MLazWVVwgOZ0Fa8morA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
مجلس سنای آمریکا طرح محدود شدن اختیارات ترامپ در جنگ با ایران را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66337" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66336">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0d9bfbe9c.mp4?token=Gu4veErVJqOhiahd8Gm3LF7677aIxGceziG5iSa49hemvazBecJK5jETb7w-rc-GR01m0iJ0BGw5gB7CAd9V5cpjv2FpVO5CB6w6tnEhjPfOW6salUW8ex2HLhPPxvjapYm7vTtPDQmEeh5jeEHRCYpQp-VE5kJx4YWtIJ5uJO2R-m-fA84HlTnTHCvwTQzOtbmuIR2x9k1nSZdmUrh_PxOSTznR3yZZS_S9iwc99bFSkGwjsbSXL2OcgnmI8bcTN-39dx-EUotVMRHtiMicUtgUCj9fBwdNxVD5PlpZY9u_9jRgeXo36xUgeX7anJYhyoJnkasb6sbC1GCVisQAWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0d9bfbe9c.mp4?token=Gu4veErVJqOhiahd8Gm3LF7677aIxGceziG5iSa49hemvazBecJK5jETb7w-rc-GR01m0iJ0BGw5gB7CAd9V5cpjv2FpVO5CB6w6tnEhjPfOW6salUW8ex2HLhPPxvjapYm7vTtPDQmEeh5jeEHRCYpQp-VE5kJx4YWtIJ5uJO2R-m-fA84HlTnTHCvwTQzOtbmuIR2x9k1nSZdmUrh_PxOSTznR3yZZS_S9iwc99bFSkGwjsbSXL2OcgnmI8bcTN-39dx-EUotVMRHtiMicUtgUCj9fBwdNxVD5PlpZY9u_9jRgeXo36xUgeX7anJYhyoJnkasb6sbC1GCVisQAWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس درباره ایران:
اگر دونالد ترامپ به عنوان رهبر ایران انتخاب می‌شد، دموکرات‌ها همچنان می‌گفتند که ایالات متحده باخته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66336" target="_blank">📅 09:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66335">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/555366529c.mp4?token=QXm4tARoomFHtE49lkSDOF4dS-Rjt9XXXDFN2kGBCdmkLzITGOY1m6I_EEiqVUz4CZ5YlRTLwncFWB2ss8_6chra17grLgBdzmc6jcgeiVt6_kgh-nKGIRvPb_9Hu7jtY9E9WjaQtvb6lRl7A7llcfqUesh6u5QjckSqZopxFyF8VfC1fX9266vxFFknpxeFkBWUv8eFV8qC6ae8H1dZ33gOP6b7ceEfSI7ljjy_XRPDDCJTjszE6JWmWagg8F4orYxHr80sll19ysyw9bOcItjPgyMor6QZF8gj62RbqrHtSh1EWd-I5GFu74gMWMzGropA_ZFVduTOY4ELF2ugZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/555366529c.mp4?token=QXm4tARoomFHtE49lkSDOF4dS-Rjt9XXXDFN2kGBCdmkLzITGOY1m6I_EEiqVUz4CZ5YlRTLwncFWB2ss8_6chra17grLgBdzmc6jcgeiVt6_kgh-nKGIRvPb_9Hu7jtY9E9WjaQtvb6lRl7A7llcfqUesh6u5QjckSqZopxFyF8VfC1fX9266vxFFknpxeFkBWUv8eFV8qC6ae8H1dZ33gOP6b7ceEfSI7ljjy_XRPDDCJTjszE6JWmWagg8F4orYxHr80sll19ysyw9bOcItjPgyMor6QZF8gj62RbqrHtSh1EWd-I5GFu74gMWMzGropA_ZFVduTOY4ELF2ugZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وقتی نماینده میخواد ثابت کنه زندگی ساده ای داره و اونجور که همه فکر میکنن نیست
😂
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66335" target="_blank">📅 09:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66334">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66334" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66333">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JLT0Frc4kU9_3VpfTAVS5YENnLz2ZjZoMnJgQ0WUWbBevhg2FpDwAoQTz4h-EmO0bqFqPBMozdjmBkvgzntXd--VO0pmhkZMIX7J7YmezM-lUahF6Am8OZBbUVFexMRpZoWrAzWU1W9IkQK8xWsMrQYru7GGJ0uzDsVRbtbkg_oMSq15G6ZEEQl9rUxH52zaZ8AlHAwtF5WogkX4XJiDOVzVR9KpE44eeXLq9Duc_i4vwVzMuS_HuCGLXEcsyhg9uICSPEVts7lwboXdMeMjYCP4J_bwXP0awMDsERyr1w1JcJ9KQLHNEhZ3HVVKyoCrdptCzTIUfOUb1MbdyVfJtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66333" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66331">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
به ادعای باراک راوید مفاد توافق ایران و آمریکا به شکل زیر است:
ایران، ایالات متحده و متحدانشان خصومت‌ها را متوقف خواهند کرد، از جمله در لبنان.
ایران تعهد خود را به عدم توسعه یا دستیابی به سلاح‌های هسته‌ای مجدداً تأکید می‌کند
ایالات متحده و ایران متعهد می‌شوند مسئله دفع ذخایر اورانیوم غنی‌شده ایران را حل کنند.
ایالات متحده و ایران درباره غنی‌سازی اورانیوم و نیازهای انرژی هسته‌ای غیرنظامی ایران گفتگو خواهند کرد.
ایران وضعیت موجود برنامه هسته‌ای خود را در طول مدت مذاکرات حفظ خواهد کرد.
ایالات متحده محاصره دریایی را برمی‌دارد، از تحمیل تحریم‌های جدید خودداری می‌کند و در طول مذاکرات حضور نظامی خود در منطقه را افزایش نخواهد داد.
ایران ترتیبات لازم را برای تضمین عبور ایمن کشتی‌های تجاری از تنگه هرمز، بدون هزینه، به مدت ۶۰ روز فراهم خواهد کرد.
ایالات متحده متعهد می‌شود دارایی‌های منجمد شده ایران را پس از اجرای تفاهم‌نامه در دسترس قرار دهد.
اگر توافق نهایی حاصل شود، ایالات متحده نیروهای خود را ظرف ۳۰ روز خارج کرده و تمام تحریم‌ها علیه ایران را لغو خواهد کرد
.
هر توافق نهایی شامل برنامه‌ای برای ایجاد صندوق ۳۰۰ میلیارد دلاری برای بازسازی ایران خواهد بود
ایالات متحده به ایران معافیت‌های موقتی تحریمی برای اجازه فروش نفت در دوره مذاکرات اعطا خواهد کرد
مذاکرات بین ایران و عمان با مشارکت کشورهای خلیج فارس برگزار خواهد شد تا ترتیبات مربوط به حمل و نقل و خدمات دریایی تعیین شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66331" target="_blank">📅 00:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66330">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9122af9759.mp4?token=rHoiHagQq1ugz0OtPtIsDynhdSjl0icgZIbFKgmsrCYQo8hnVtWDQ6VsA6YA1fywDrhaM12_W2QGJV86ZYYU-wGynZwZ4NbkAzo7XjuHzCGBCChuZPHZTzpWOeSV9PxtiRsGgZY1kMX7xkVX3XW_UaeK1PP5xg_rD_7bD8sWiSG1Djjn67bt3Mfec8CwjFOH9O6nJVbRlzP6S1LqxQEjyvz5BWqm2agvIt60j0hE7p0lgENC2vPLzy7CmrlV2i0O3IzK4OWrQ4hEmIOcia3YoSSgpUOxieFd1dCt12U-OvEbWf5cRMWPeWiMxbmK9CTLRGXI8EvZeo8N6rLmKl_cH77NXczX7MefBnjxKVmcyNVvdY80hw8TnO_C8SdpUfURkEsVgCqJ6HRkn96EhcIs373iMElVs5kUuE1Mm6XpLeOHnFdlj8YuMtLZNewR60ElXgfrbPW9EC__oAsd107tNgl7hSagwL3fhGC5YHDhYjRIqZ-i7iutadNuEyGmmGFMkFEGXY904bTfk9DI7vP1LFaohyECn-61be0FR4K27HjI4Nic3Lbb4szLeoCUI4ZkghLa8FI_npX-xIDc6gPqhHI4ZZP9yHQlsDGU9O7hba9j8RaXOhB-UxYs5oh1SObQl-_ha4F-Q2FIX6_HL7mXyAzsPnEz9FM4q40snCg82I4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9122af9759.mp4?token=rHoiHagQq1ugz0OtPtIsDynhdSjl0icgZIbFKgmsrCYQo8hnVtWDQ6VsA6YA1fywDrhaM12_W2QGJV86ZYYU-wGynZwZ4NbkAzo7XjuHzCGBCChuZPHZTzpWOeSV9PxtiRsGgZY1kMX7xkVX3XW_UaeK1PP5xg_rD_7bD8sWiSG1Djjn67bt3Mfec8CwjFOH9O6nJVbRlzP6S1LqxQEjyvz5BWqm2agvIt60j0hE7p0lgENC2vPLzy7CmrlV2i0O3IzK4OWrQ4hEmIOcia3YoSSgpUOxieFd1dCt12U-OvEbWf5cRMWPeWiMxbmK9CTLRGXI8EvZeo8N6rLmKl_cH77NXczX7MefBnjxKVmcyNVvdY80hw8TnO_C8SdpUfURkEsVgCqJ6HRkn96EhcIs373iMElVs5kUuE1Mm6XpLeOHnFdlj8YuMtLZNewR60ElXgfrbPW9EC__oAsd107tNgl7hSagwL3fhGC5YHDhYjRIqZ-i7iutadNuEyGmmGFMkFEGXY904bTfk9DI7vP1LFaohyECn-61be0FR4K27HjI4Nic3Lbb4szLeoCUI4ZkghLa8FI_npX-xIDc6gPqhHI4ZZP9yHQlsDGU9O7hba9j8RaXOhB-UxYs5oh1SObQl-_ha4F-Q2FIX6_HL7mXyAzsPnEz9FM4q40snCg82I4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
جی‌دی ونس درباره ایران:
🔻
ترامپ هیچ‌وقت نگفته که هدفش این است که رضا پهلوی را به عنوان رهبر جدید ایران منصوب کند. چیزی که او گفته این است که اگر مردم ایران بخواهند قیام کنند، عالی است. این کار خودشان است. این موضوع بین آنها و دولتشان است.
چیزی که ما می‌خواهیم، توقف برنامه هسته‌ای ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66330" target="_blank">📅 00:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66329">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
جی‌دی ونس:
🔻
فرض کنید امارات متحده عربی که یکی از بهترین متحدان ما در منطقه است، بخواهد در یک نیروگاه هسته‌ای در ایران سرمایه‌گذاری کند. عملاً بدون اینکه ما بعضی از تحریم‌های موجود در سیستم مالی جهانی را برداریم، این کار ممکن نیست.
🔴
حالا سؤال این است: آیا اماراتی‌ها در ایران سرمایه‌گذاری می‌کنند؟ یا آمریکا اجازه می‌دهد اماراتی‌ها در ایران سرمایه‌گذاری کنند؟ نه.
🔴
برخی می‌گویند خب، شما به ایران پول می‌دهید. نه، نه، نه. ما می‌گوییم فقط اجازه می‌دهیم برخی از این کشورهای دیگر در بازسازی کشورشان سرمایه‌گذاری کنند و برای مردمشان رفاه ایجاد کنند. این چیز خوبی است، مگر نه؟
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66329" target="_blank">📅 00:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66328">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400d2a3a78.mp4?token=h87LZXQahcEujqSbiZSityWmw4aayzE9hNmHSFMB5hWFkpGi4WBW3NIkilMyVPsQTTKcGpD4FsET_qre-4lJGaW9zOEYCNJyyYuO4DJLQcxZYo5y2tccR-uDzmzYRajBRUMsRBdgbB6tWoqLMnyO4jcIm2VT7_3s9guc81UwK1kq6Yq2l59zqhp-twHxe15KpgtAVkoOpOph4_sUSxv3n3OOIfHVmFp8jXyPMYMb1pdtrVwmD13MNAeS3tVkTZlcyfsuK1daR3yezLdphbd6epf4Hlk_6-devv0kMOtceLC2kxTU0xFwsooEbhwal6vBp9EDZ1ZQuKQkdQSDnJrLeIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400d2a3a78.mp4?token=h87LZXQahcEujqSbiZSityWmw4aayzE9hNmHSFMB5hWFkpGi4WBW3NIkilMyVPsQTTKcGpD4FsET_qre-4lJGaW9zOEYCNJyyYuO4DJLQcxZYo5y2tccR-uDzmzYRajBRUMsRBdgbB6tWoqLMnyO4jcIm2VT7_3s9guc81UwK1kq6Yq2l59zqhp-twHxe15KpgtAVkoOpOph4_sUSxv3n3OOIfHVmFp8jXyPMYMb1pdtrVwmD13MNAeS3tVkTZlcyfsuK1daR3yezLdphbd6epf4Hlk_6-devv0kMOtceLC2kxTU0xFwsooEbhwal6vBp9EDZ1ZQuKQkdQSDnJrLeIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🎙
جی‌دی ونس:
🔻
یک نفر گفت - یادم نیست کی - که این توافق مثل اجرای طرح مارشال وقتی نازی‌ها هنوز سر کار هستند، می‌ماند. این حرف از چند جهت غلط است.
🔴
اول اینکه طرح مارشال با پول مالیات مردم آمریکا انجام شد، اما اینجا قرار نیست پول آمریکا خرج شود.
🔴
دوم اینکه ما می‌گوییم فقط وقتی از مزایای این توافق بهره‌مند می‌شوید که رفتارتان را عوض کنید.
🔻
(البته کسی که این حرف را زد، سناتور لیندسی گراهام بود.)
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66328" target="_blank">📅 00:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66327">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7276198054.mp4?token=Ath49wWsqFK6l-q4L1Qfm8VsHEvKD3LsTh9ppysB34gxJseQ_d2y9WbIuBm1QbNnMyjsXJzwxKJEwRs3SyD6ykDgk_DZ-zXojtbrTemPklVlHxyfztXeIctRWFaKnjxv5CltaAWAkT1Z7eU_XDvXGI3xUMvIkxz7skUSVCS-YbhSgbu1JqRUJKisKzmZMSbUP_qcWlyFdS13lQ6I04Tb10ihECMJpMB2QTpTVzyjrRVMMnY3KbFuEn3nV2z0Z6A2aZkN-DoOBozLMKuFewZCM9vi6UuO5--Xd7bkLdD_AOJwpJHVjCw8gLHgfPp4copVKM6wywXLEDL56SOMe8447Hz9KF14X8ebsF6pon1MgnxW8XWfFn2ULJW27olcvyrG2pki03kyoYhkWkfPvWWMzjl-8ZHf6kmDTkYkdVxg3tdBV4qLmnH8EkJ-GhJUDVpi4vOR8tiWZPrX_Dv3s6u4KeUiYg6Nk4wGXuRhTLd_odefe1N6NxikqSHgULxtREzHAaJhwUin0NL0p2Ll5gf_wQlPCFM6c5iXsob4zaGCdIf1sqDavcDVwdGkSCprKdJlk3M01THSoHX_QBNCEXk1TL-_pA1pl5ZJNVqbjkNBTpXhDT_PYFQdeo-kGbLA2pPsbK9I_eLR8079jwhpjSTHA73coxwpzOl50S5LvrxxiEU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7276198054.mp4?token=Ath49wWsqFK6l-q4L1Qfm8VsHEvKD3LsTh9ppysB34gxJseQ_d2y9WbIuBm1QbNnMyjsXJzwxKJEwRs3SyD6ykDgk_DZ-zXojtbrTemPklVlHxyfztXeIctRWFaKnjxv5CltaAWAkT1Z7eU_XDvXGI3xUMvIkxz7skUSVCS-YbhSgbu1JqRUJKisKzmZMSbUP_qcWlyFdS13lQ6I04Tb10ihECMJpMB2QTpTVzyjrRVMMnY3KbFuEn3nV2z0Z6A2aZkN-DoOBozLMKuFewZCM9vi6UuO5--Xd7bkLdD_AOJwpJHVjCw8gLHgfPp4copVKM6wywXLEDL56SOMe8447Hz9KF14X8ebsF6pon1MgnxW8XWfFn2ULJW27olcvyrG2pki03kyoYhkWkfPvWWMzjl-8ZHf6kmDTkYkdVxg3tdBV4qLmnH8EkJ-GhJUDVpi4vOR8tiWZPrX_Dv3s6u4KeUiYg6Nk4wGXuRhTLd_odefe1N6NxikqSHgULxtREzHAaJhwUin0NL0p2Ll5gf_wQlPCFM6c5iXsob4zaGCdIf1sqDavcDVwdGkSCprKdJlk3M01THSoHX_QBNCEXk1TL-_pA1pl5ZJNVqbjkNBTpXhDT_PYFQdeo-kGbLA2pPsbK9I_eLR8079jwhpjSTHA73coxwpzOl50S5LvrxxiEU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇱🇧
جی‌دی ونس
:
🔻
اگر ایران حزب‌الله را تامین مالی می‌کند، ما اجازه نخواهیم داد که مجموعه‌ای از دارایی‌های بلوکه شده به ایرانی‌ها منتقل شود
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66327" target="_blank">📅 00:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66326">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8b2573c92.mp4?token=vHSuzLyuJe3cCZNSxFcbfOrfqeQjWUuTBEW3z1jAx75oyQYS6ZMPLJ_sa8WeNAbcPSfpTDT3Xiizi3tbpbJm88vS8bjgpjAnvcY_79WHvvzp0S3UN_oxqI0uNKful1Cqgjh8blvw77hxFoBQ88OI-ji7pOO9O9ZnUVZN84_AQMBCLW4l-E1LXc6-GG3z4QB4sev5hTEPeiJIZPwDkkR_vvtSMycUXpWuZDrbia-IHTOLyOs3Iji0wL-yOWT1OrR9kQZ49c77Ji7osLnsS_YLrAZ42CcuE4RPW0wZ9L9eXsYznjMGU1vlTtTMnje38IX8xQnI9hkEpxDwSFbfuGDhJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8b2573c92.mp4?token=vHSuzLyuJe3cCZNSxFcbfOrfqeQjWUuTBEW3z1jAx75oyQYS6ZMPLJ_sa8WeNAbcPSfpTDT3Xiizi3tbpbJm88vS8bjgpjAnvcY_79WHvvzp0S3UN_oxqI0uNKful1Cqgjh8blvw77hxFoBQ88OI-ji7pOO9O9ZnUVZN84_AQMBCLW4l-E1LXc6-GG3z4QB4sev5hTEPeiJIZPwDkkR_vvtSMycUXpWuZDrbia-IHTOLyOs3Iji0wL-yOWT1OrR9kQZ49c77Ji7osLnsS_YLrAZ42CcuE4RPW0wZ9L9eXsYznjMGU1vlTtTMnje38IX8xQnI9hkEpxDwSFbfuGDhJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوند و تعریف و تمجید از ترامپ
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66326" target="_blank">📅 00:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66325">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1190f45b0e.mp4?token=dIqHc4CigJo0LF_QWJPK4QAc3RE8XuiC5AIvBptTA6PeMJJG_7S6ta57XB2LHIh9QdbVZpJnGs0BXBwHMgwCuZJe0HdsmXCyOVSSANbjHxSbTw0eK3YOlgebw82qWVsSh2E5y_laTae5wZoTX_V8yMlw-w77nH9YhV12QDU0TSCFKPnCl2MOooSvBHynvK3ioVhdpZr8vvyvqj09h_qHf2lGzshEu38LABmNKZSAhOpZRrJVZUHLph04j6HtXWHZDuqYBAQ1-UiwxKfc2ESdKdv_DgZUPQoNMz7CxU5Y95ELrTsXcXkvWAAVJlK_ufY1-Uugtk-3JHlQnd19itw1og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1190f45b0e.mp4?token=dIqHc4CigJo0LF_QWJPK4QAc3RE8XuiC5AIvBptTA6PeMJJG_7S6ta57XB2LHIh9QdbVZpJnGs0BXBwHMgwCuZJe0HdsmXCyOVSSANbjHxSbTw0eK3YOlgebw82qWVsSh2E5y_laTae5wZoTX_V8yMlw-w77nH9YhV12QDU0TSCFKPnCl2MOooSvBHynvK3ioVhdpZr8vvyvqj09h_qHf2lGzshEu38LABmNKZSAhOpZRrJVZUHLph04j6HtXWHZDuqYBAQ1-UiwxKfc2ESdKdv_DgZUPQoNMz7CxU5Y95ELrTsXcXkvWAAVJlK_ufY1-Uugtk-3JHlQnd19itw1og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان بازیکن تیم جمهوری اسلامی به خبرنگار خارجی:
مسائل داخلی ایران به شما ربطی ندارد؛ مسائل خارج از فوتبال، بین خود ماست و خودمان آن را حل خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66325" target="_blank">📅 23:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66324">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcce5ba4b.mp4?token=hUqt3Bzu527ApV_nst7sZm9x0y-9jhn_0K0_o2XHEHQXDt5NPO6sExzzI-lse4UB9-AA2ImCbVqorseVOfubyr95nWet63-02P2olh8yWlO-coCyVrUQhKU8wNhLMben6Zn-8KTiTe4ZQ7zGdRdTi89WFY7s-r0b0DcGlAT-R5gW6l1sriXQPYbCl6cCCg7HUMU6LXYHSbw5Wc_3FIibAJA93bJNM_uCv-XEV-C0LeI8apY7mmGx51jYJ2GYdu7soXHoONYphbt25M-YdfRuyi7IWw-ff7akNbBSxyJPNAokvLD0lX3AiCWQvodhhbpQfde79oQoUKOiJCJyFFgsTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcce5ba4b.mp4?token=hUqt3Bzu527ApV_nst7sZm9x0y-9jhn_0K0_o2XHEHQXDt5NPO6sExzzI-lse4UB9-AA2ImCbVqorseVOfubyr95nWet63-02P2olh8yWlO-coCyVrUQhKU8wNhLMben6Zn-8KTiTe4ZQ7zGdRdTi89WFY7s-r0b0DcGlAT-R5gW6l1sriXQPYbCl6cCCg7HUMU6LXYHSbw5Wc_3FIibAJA93bJNM_uCv-XEV-C0LeI8apY7mmGx51jYJ2GYdu7soXHoONYphbt25M-YdfRuyi7IWw-ff7akNbBSxyJPNAokvLD0lX3AiCWQvodhhbpQfde79oQoUKOiJCJyFFgsTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرزیدنت پزشکیان:
مشکلات خودتون رو خودتون حل کنید، من سیاستمدار نیستم من دکترم، برا سلامت مردم اومدم
😔
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66324" target="_blank">📅 23:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66323">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9ab7bce46.mp4?token=rsCtSkldwduOGydyDpRebAL2vwprfq68SRdJli-84PAzrSEUP4tDe1CXu1_pKTWRX6CqAafdJD1ACMJ810uuauMrB1VNiWRf5b2bBvKzADPbfDildAbHT3S8POz0LeEiOM39oDgG7zN7k9pAq-TJdQzvwzrHuPCKm1bPFYUeZ8zErFgsPRG_EsEgvjg5zjuCrjaBOnUksNqNfB9T_wtAo3BBnl9WfdiyeG1xiwRZ7aJqkFgGNyobuQEWT_wGoWihVrs8kprWMfe6w8MtCEsCgA6ThQth7TuslaSTCvVJMag-cdRVMguxt__FvzLsDJuDC7jaNbB_V0NAFH0zk1NFPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9ab7bce46.mp4?token=rsCtSkldwduOGydyDpRebAL2vwprfq68SRdJli-84PAzrSEUP4tDe1CXu1_pKTWRX6CqAafdJD1ACMJ810uuauMrB1VNiWRf5b2bBvKzADPbfDildAbHT3S8POz0LeEiOM39oDgG7zN7k9pAq-TJdQzvwzrHuPCKm1bPFYUeZ8zErFgsPRG_EsEgvjg5zjuCrjaBOnUksNqNfB9T_wtAo3BBnl9WfdiyeG1xiwRZ7aJqkFgGNyobuQEWT_wGoWihVrs8kprWMfe6w8MtCEsCgA6ThQth7TuslaSTCvVJMag-cdRVMguxt__FvzLsDJuDC7jaNbB_V0NAFH0zk1NFPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عرزشی:
چرا با کسی که به رهبر عزیزمون اتهام جنسی میزنه مذاکره میکنید
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66323" target="_blank">📅 22:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66322">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
ارتش اسرائیل، طی دو روز گذشته پس از اعلام پایان جنگ از سوی ترامپ، «۸۴ بار آتش‌بس در جنوب لبنان را نقض کرده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66322" target="_blank">📅 22:13 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

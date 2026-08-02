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
<img src="https://cdn4.telesco.pe/file/fbIiqgv3pg1s4j9uWSr-UFKnstlmQ3nlvj6AUWjMygjYexED5GJwlY6nRr5in-gFmaFyBZUaJyRAAjRCcHLVcrA_aw-Uk0iRMNGNK-GRYvMKxb7zk8z6yCmiWldVHbAQZZgEPYX7DZ2Vk4Q1g4tMYYAJaKrXah1EDNHIiZB7EJ2NJZyWI1LlcBdfF6vEvPR-howDOMlHMRgYNNn9x_IVLlF-J_fPqj5zZBZjdVuBpLNZFTJ4U4HMbdUmb3CK_qK0UQwCz43dSktXKePaS_G-e7vXZLCCJxJP0MNQnvFQXqa7gqevXKXM3CnQWmKwfaowB-knrD8BA4RhQSp_tJcBkA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 23:37:37</div>
<hr>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=QlRKxm2ajft7DlLfR1eCkoCcbaotfpYJm5SZQG3QZ2BGIGm8xPnI2W9W7V0K74LBDgWq7i5XbuY-fWiapOxwr6yZq1jCaivNAzTOUXUuMcjYNr-lOKZ0YmB5TAI5UI4eOKhr3AtrI6WQJ7v3pfeH2SPH3EASLbLQ7SJfxccApO-fTfJ74FgxVDcZIffVn0YWPlU7IeLauCb4wepp6ogGBKuVle5tfzQJtP9fnQ7HDBSt596qLXGmmqvBCXfoRHLHmShIRawNB-xjoj1sd6HxQF2rdV5Gi4bZcGh9fodi2_vvBMVtwF8cPWj5fndcAfY4YOBf029xOiD1vOlD8Wvv8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=QlRKxm2ajft7DlLfR1eCkoCcbaotfpYJm5SZQG3QZ2BGIGm8xPnI2W9W7V0K74LBDgWq7i5XbuY-fWiapOxwr6yZq1jCaivNAzTOUXUuMcjYNr-lOKZ0YmB5TAI5UI4eOKhr3AtrI6WQJ7v3pfeH2SPH3EASLbLQ7SJfxccApO-fTfJ74FgxVDcZIffVn0YWPlU7IeLauCb4wepp6ogGBKuVle5tfzQJtP9fnQ7HDBSt596qLXGmmqvBCXfoRHLHmShIRawNB-xjoj1sd6HxQF2rdV5Gi4bZcGh9fodi2_vvBMVtwF8cPWj5fndcAfY4YOBf029xOiD1vOlD8Wvv8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EifKuCTpulCT_OFZUREqD3ESfwlMzcXjU6VZy4p0oPHFb9pUSQ8Al2ieOxiT7EUr7emJ0u0_VsspBkcDTR5uGCk0ppGBrbsXGxEMG23-HtMAHVh5L_WsiTLzy-5wRT6lVvUFjudduAaef9kGeAxoXqHF02XnlKgXTsCKdXK_DXCm0QukG7Qwx7FtPr-c-YT18gHmOZvJWOfdHUJBA3xvW4rBC3UhBKeJjBVE6B-xccGUwCqlLm-lYmNE_GmtWqae5ogqbzVsTJ-8YiIzXU_fOTbJOqkYjs8CRUpDMNI-9Uawlwj6FV81ZloTVxm6v7C2frbJjSaaqjfmgH0x3j2SdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vf2ze1vR_vgLrIsaAeU6BGjbceIx_2osoh4kYx9PNzeEXniSEY5a7oBsrCBNFGJG1V1X4JogfSdrv8aNiOz3Knku-3ty8C4f9xgCH9W2LHGJwTbOFMIDUn7IhjATJCE3ZYNjsG6Dkdt_VFI_dxCRRAqLn2zv_pgfw1gCkI6gynmrg9IATZ2hTQOaKWNmgKFfvsIMav8JhsA5oQo--PzFG6hGp27zPgldHYHL_HswS3ZRWtUx8p0BFvBmf7RlXt0n39GMjmsNx44nefVzMhgxP06L7jkvJxqFLNLpUIinGl94egTYFwd-QH7IFVjTaZRjuOlyDKlEnHfEq196zokKIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZHG79sJfk1HrKHU4l7ii6713U9t5HhqYmsyezxN74VrrS_0Wfk4AODeESUxvBlXCAxfdgL34C6m48QO1y8W4MOTUwuyugrHXriYc8mgORpq_NwTqLW0fc0wlHSTlSyT9cd_hDht5CUQuksOQP8yUtTbPHtHjlDH0zrdXqthLAG3wuEJV9-AiQdkh4Y-fwqYrAS_0TRX8WJubKM96rkSVYskRn_-U-1F13hbS_ydJv57JuvA7goB6HpEdK5i6viK9W4Y38GlpNYX7kBmYP_igM4O5f_GMjAnjF7Mu-A38A8eoDGkCreDvYqtTrxVterCxt3IscOX9ERQlQaa5L7ovQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SRenryfa2oG2KZlxHJuw8UXZjm_Nj9EMBcaWqm2TXhMJ_MqgyMofWueYuIbi5LIHFxz3HNzUObmJBK-5b_wPZ11Ldr1CTOGEddN2avyvsGr2WbhYmDKP3WTpvQJ-97BDr0g8RE1BJTMkXLdaUBVj3MegXmV4drogOFR40s45S2AdsF2OmflcWFhE2xxkzpLX7nxiKQPYCcrOso1geNWq4jMXH6NF7HadDV-c0qVUpG2jm58eHAC99kfujr4cchoTdjwTBCeoQG7_HUMkqi-cCybASQXzcsEHxL79GyPWbD5kTa1xhcoB-h8MfR2sp2vEILfi6jd_I62tOlwEgA1e7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUt-cL8RVIYSXGymqenW4r4nRgsCxoGW-79_wktf6DfSRe5Lxm2TS1P2XTnwDVtUU9JZSJttsqEeydmviaa_6V7wUUVL8oNwNCI3CMsydnNdFMmrR1lE6AZ5cWXCN4EgxdkbA25bfstfUAAM6fmb7y9xSb5_0BsJdsza7VoqgWnHlXHxXStjKVrepZzcswLIVtZupfhl-NlAxz0nEt5kMT761-SxMSwwCBUQZLBOrWcs09vrR5rfZd4OQ7FP4_TZ0MqsqVAG0kXRhnLMLi6t8ndI25GTcSq8CWj4BtF7qU5JBXA5L9rX-fcnEVCkPM8y5-6fHkUXQhU0hYUrh9TYZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Df1C1__G8fN99ec4J187IBtQKmX6CK_xNVDSNa8JXuHMCZKpWEBiWPcKgl4-OnYTs2o8jLYs9j9pwqnFnfohl0CnAHq1q-5we_Kphb3tvMU7R4282dG870pHJcrnu3LFQvZf5SYlWrOg8M4C6dzXZCopGpa5NUsmWhk9sdQ7na9XBWrp3uZ8y-CPSayqyRjFJ5m3qfVmZerXtLxPtAq6Tq478AfkzfFUZX6fHGNipgWDQ3ETWRlm9NORAQL9MD-gwVMVfZk2G-KZimfZe3glUFXfKKseH-2q_XBpVQRfQAOQ0dLGVJifDmH8aGdeQ2e5wLNbZ1rYvkkXdqYSMdBoog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDqbOYiJYXCh8Yae38LV3ZmE0EyBLt5cM9ii2SARa5TpampEXW3iXGsadIrY7JCcTNPPDaY95X2EICgZummecTXQQ_7YvDQKsLGogT2mZYLpPeg4Jx0K1PK3XClORSk-cqktJEbuKDT3lx7wCe4hke4ctdNmLoJD6PDv6Oog-RE6Medww2LJlunJxlWDoy7A6mM4VkAcbmuozPV_MzJkewOLrdg1930w-ptaByqU92-EtBHLdRrCpZUCrH0lswdodZklta1xgmv27BKqgHISaLmJpNghtGUJ47dVtozuSPM-7SLnQmqWzFYnrjDxwys3STTo7JSSmL0zvjLZM8TV_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LR80kl-ehPDj7T_Z_P3rCPuxYS5Lt40K4u-zSO4b_6s616jiYU4lrzGpIgI--_QHuCGUudwvzXMIAJL8xnEXr00GghyUJIshpv592u369HfiEV6M_ZczqWex_5dVOCG9yEyJQmtsQTKAZOGNxVek5vYO94ONJrR7MQhGAypu8YhSn5J7YAal2bs8rZAFz2EoPwBZ-mft4QqkxOTDgEsG3hKjEOs0ByjJk2tplvU9vR9CHVxiTns4J9Ycmn76FSHzFovEw5bn1fViIv1-MTjDLZfluRUt7-CVrey-FequiskSg1oXFCwT-VfsHMbJ1-BT_ERP0E7Quda4TVdxp3b88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANNRkG3p4dH8Xk7aL86TclRYXwj-3GN0TF5Q3WuRz6qR8iKhvTMfMySVz1MBvwJUf2bVWxj1Vgcf1KW2h8ElBrBKAJsJDEn1EPSWHI6QUMsQnKhd78uvVs1bueLtthhiesPPAQvkA4Le6-s_nOpMgKVWP9C_X5_MFcbirNGuR--yEvKZmBQxxg5hTJDuClXwUKO6dpl78dipDR8oOZA8eZRxFrt4yicetIwHMHwbHp0hn-NRSMmkGUJyo0HQPHgQ141vydSPK4024-C6i5IzGmvKEBtGDl3e3GwGDzd0soTEffSSaFR92fe7xjUH1Vr6mJnju5cBZK8xh3_l4iCMuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرعون، جسد نخست زاده خود
را در دست دارد، زن فرعون گریه می‌کند
و موسی و هارون،
در گوشه‌ای از تصویر دیده می‌شوند.
برای مجازات فرعون، پسر او،
و نخست زادگان «همه مصری‌ها»،
«حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس
که در زندان بود.» همگی کشته شدند!
حتی! حتی نخست زادگان گاو و گوسفندهای مردم مصر!
و این تصمیم و اراده خدا بود!</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xta_htQ33m12TeqtZXOM07H964tNvvfGQ0KAT_J0Tv0pxtjTLbegR78EBQbdU41qSRdTiwjcjTRF3tn41FYgGPnH6RyBUArktoL6NS4tgnHzoMxr2iCKv-SpMPLrda7JKcrmzbskSzckvUD-hTFyBLqrZ4xiezKmd3kUvDspxKObrCh0Izchc8LN1F8tuXH5-ydO0hDfUk7mUG_ovsyzjSshzSxdCpWcwCvpOnPRWMxj5eBbywCmrKcUIFyY5F930auXBruep4pqDQHWKyf_7vICRklvc-RRDphTC7nHzGEkDhMEt5yjSen3CLe9uZZisRK7NmVKPth2FJA7qqDqPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJqfKRlv2BOeE9q4D5rRs1gsu32nkNwRRJ8E5cmO03m7t0Z8aCjy4oMjZd3sh-SBggCrC-0qkRcLPnDnNaZXxs0jfUP3K6x1I-KkStPmRFGzLs8vh6_qit-y_Z6Q3dwXzHo9g5ftoyLNumy29QXMS5JPfFzBflT77zDvw5I4mMmSzJDk9Ui3x8jXzdO1MmkB4w_z1us3V_H3Q9c6SB3a6d6IbYktn05LWO279uXm4h1A9G55P4u0clMwH_HgwO6ZqyWvcY_sOPVta1iCUbkXsPr-7iupv9NdCucknyyAbvy3yfN4fECa72AWBRix3sV_hLjbO7iCQ5JSaHK8p2ivLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e18V3Bg-Uy-bo9ikhRI0ztV_Z2nDVyHXyMnW9nG6K0TxMznHD0rcUCZKC8bpW91Wi7oUyLfbE4b7zZzvjQ1CBgGdhjWfeqPDznc5DxCHNy7wC_TvNVSbzahUQhl0RqLJiIn8ijtw2v2X7YxwWwHc2abfIGvwqxd51n3CsFGqO6znkVEkSQgkry0GMCPli_rSy4PBCdSjCwluqoWE8gUA2xoaQx43eMagC36ef0x2bL45tycuf06HG6581-ZHGiFjpxgDuFgeBeE_Azeb9lQLoaHlykgHNtYlZJgjVmD0Qag3-ZYkTtnzC6cYoEsnQKYn7X7FzkvPg-g44o5Ir-1t6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ct7ma52ttEcB1SPI1sXDrLV0ImmVQwbFIscb0v8r7ImER-Sl-ZQU6he43rN67jPMWxTMHGevUmsZAqIweLUunPqlRP5B843UzpeWHVjT-kSdYOombDc2Ns0rwhLygOrzNYFZCUzS3wmk2gXr2nZq3YsW00LVUts7qfj_jJfhgUDrnWeeDDP-iwyfkiBcMcoI27uUBA7bJCxmiaRyrUt_8C0qdo6r4HORUm3l9iaZH44CDq9MZGyKAkjAIGspmmKFGiUWabZu8CBlOkjAnAm2hrCUKT4mhOKIbF1Oz64EO50x5zy_pRt2v8wXqAj5QVjvahRASo4jkdkQjjfEJt4edg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -
سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!
تباه در تباه!
خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».
احمد شاملو - غلامحسین ساعدی - اسماعیل خوئی - منوچهر هزارخانی - هوشنگ گلشیری - باقر پرهام - محمد علی سپانلو
اینها روشنفکران ما بودن،
جامعه آرمانی اینها، ترکیب کمونیسم و اسلامگرایی بود!
از مسببان انقلاب تباه ۵۷.
از مسببان گمراهی یک نسل از ایرانیان،
از‌مسببان  تنبیه نسل‌هایی از ایرانیان که هنوز  به دنیا نیامده بودند!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcHrcZwJ3QjDmpcqSCYCA6Hwu2XC2rG9CoiCFaFGiMLDqW0Jl5GYIgOItzigcbbG8X9PcQCfkoDybWXPv_5FzGcW3Ka6rT5T2bV6CyEqD0vn9gTDx4eu6RWwoMz3TBZGIor3ZeGc39thl-PgEinmxXvkKdoypD-l608DFqJQOnRnkuNCBj-z9jJShgSGx-GqdGDZ1kqVceOoTxyPY8EbwrGeIesVmW3QZFSqw_zb_kgZFUI7mD4FP0_LyVYN4eNLf8uzW4TG3cKIuGrdtzGmzvWSRqJFJvetbBMmRwA7ENDC32Ggflt-Z1FTe9GkCT4IzxpTkL7up7aad-uy4KSYag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=m76Me_b3qC6orRKw8pQV_Z8AVxH0M5X2c1WCCl_Aez5P8oDogCd0JQxwBAYAjTxzTsd8XBAN2nB_030CYTk1tssaQrh5UMhWt6I9zW4F6_k_rIpja-y3d5BWeYWAxNZcP3OzNG6dJ-lIKI3edopur4spffv_yOR3H90FXUWq1hBUabpLk73_IEB7QhC9zRL6g2pz6U4g-WsSLSCYFktNE5vnJ3FD_FNKxCGR_Ak5BYRDAqmBcJgfqbAPc0jo3M_ZnAR5VJnSEnNjKiUFWD_F_PBEhWsbKwp0w2hfnDkqYHYYt1NYmRwhRJDzQdjRYruq0oGhq0XVb1BSJY9wps_G1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=m76Me_b3qC6orRKw8pQV_Z8AVxH0M5X2c1WCCl_Aez5P8oDogCd0JQxwBAYAjTxzTsd8XBAN2nB_030CYTk1tssaQrh5UMhWt6I9zW4F6_k_rIpja-y3d5BWeYWAxNZcP3OzNG6dJ-lIKI3edopur4spffv_yOR3H90FXUWq1hBUabpLk73_IEB7QhC9zRL6g2pz6U4g-WsSLSCYFktNE5vnJ3FD_FNKxCGR_Ak5BYRDAqmBcJgfqbAPc0jo3M_ZnAR5VJnSEnNjKiUFWD_F_PBEhWsbKwp0w2hfnDkqYHYYt1NYmRwhRJDzQdjRYruq0oGhq0XVb1BSJY9wps_G1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rie3AQP4dmNq1HVw1llkQzRxdNmR1Y3dFfJw0LD_2_mZR7Uenv1IHplnKxMPkzHBUtdCDzC_PJ6xoeZ_b5keL8lyEqfOAqFtc06P4WNufx8Hd9oHq9IOHNOIL8ALlixE_kyvXX4pmRSsoUuJSvkAp9FkZkm0UDoETCcp3x8fOrGNgRSE6ZaMcrQuhZXhFexJrYXkarR6pzvm0O5NH0KNaJRheqhC2oF6z2XCgJV7UDX2eMeHXFho4EK1JmOa0lUxqvBZVoVDL3lJmDkae46WxQz3faYY1FaoiBXzLntBscRAJrGBqGFp2eJnrNTmyyinDldq6RF4D4NUBaS_8dYVPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qp-uWfFXcnmLv-0yLX9U0HSaaUUxpVEYsNA35IzA3RZ-mM09Z8qB8OWIInZRV5Fe5j1ZjlLlWA0DazcSD2o0xu8nMZ3ylh3dgmLYJw4cWa_sQc0zyzCin0Qbvx1roTzR6johL1kwCcTY9qRTifFt9OubskB7kzNkKy_yiCe2wjUf4Rim-bMz2KZahHQ25ckWSh3Nebd1taY4UxIihZQn7f69pMlL-EJplk5JVhn2Yw4agFirJiH4DSJsR70EE6oEzkzw_d9MyyExhc_W7tCeH3FiKLjiprPnDrY5dfw_ZNe1cvNuh7Bq8f0xN8kOgk6fnqMRLOmKSOo82voIFrZTHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjUcCmckFhian4fxZ1CPt_X04Yk4G8LvzCk76rPDE6hZ-lP3sq3DRxi0vaxhA4hl8M9pNUa3QUNtth4SqRQZqUIcLA74UnsK_BPTS6Bgf7GNfkE5jfk1PNSoy0Z-Nal6KoKmZzYgnrEcipTB5LCSysETkY2UCmtC9W_frZ5AJU0WJUbf8SwLP3_WtodCIrf5oxk6gnE5v71AFZdHvikJAyCVbnur0zKhhuZcRbMvD7lj0cBlxQbcUSRVRelz6dp9KuB31v_i6bCWRUBIL4QRyPXcyCyFwRlkaDQCAZxiOHi68xsZNv_V0yoVkKiRfa_AR3IN29c3dY7Mmhjk_EPy-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqO-Ys6gM-aP5jJ39DyrDfIOz_WvT__lYsUOOfNVDjCafVBWPxNBVKEcinUVULN8b0pPCRt8ObUDfCnBnApslp8GWPTmLU4q5AwZNkPAn9pJAHRUVQE-RNB6fUBQoZO5eYPT9vnzINL10TcNQIrBTurHdh4GJ1TLHpLIdABKD67WzlHsNnOxWFDgsIXgdapNtfS0QmF9BkqvTdf2sFtv-SzHHjczl54HLu6holMnn2xgi70kgeuwf1CFHDXGwe2EfUoczZ3PSKeGT6mgOvrX222s9ejiWoOQOBICNMJHy-CIi6lDEIAFb7uPtRfkgi7GyGELP1yO-6_1j22DKY-AfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-73ak1rf6cE9XU2Rxhe6foWf9IfvhvYyNTPdLsO9GOK9kawPzMSjU_DFHy0VFhlgymYTNNmxBHntyZlwzsajr-Kg06xHTCT0QqjT8ExMFPAnidUQhKpv06U2A7Wy3n4x3kE-HuZdQL4PrJS0qwWiYByuQomvNaN70SIrcGxZTgFeni563eQvllKobegXUvtTVq6_DZR2EDXYyEA8w7CN2V30H5BAdEcemNhCxoDBDStYo-_oWecl7lhL0X56KOlsJ5PcJ8Gh8NB0Kp-D6B24PgoLabisOx7ZsuzpMPKTqMab52Ckthnv-0wOAE0RGSkmX7MzrmXkpm2eLgIvldjNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZWXiG9Pm2zdfjszEwuYn5iU5V_EP7mO1aAFznmjNvBb4vK53U9R-oc_LyVwBBrHhHuR-sBwCy_jc0Nea476C6z8iHttZJMPGlvQDHTrIYkiCVt8S2P-rH09MTF1o4g2cIp_jW7QQ5Vq0oKEl-WaohwfhDfBBVgP1uPt5CvybKOE3aKnxLp7jEBWCjbfLFsUoHaxeC5rgQ9eNgdhv8wSn6CO7_muNTtjWMvoU5HWziOdqHYqVW_g34aNwrjnYbmYRYGEoaLV4e-cpxhzDxThA1KlocF6jW-Rle3XzG_ji0cCRQd4_grYiy2z9D3A7SqjvHvn3ptLnRPiI_30yogJQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eo_IqMKFX8OgRbLEyw8rO2mEHMGLx_WmMsGQDl1n5_3kN3eSCTlCD11f1NHr7rnYvypYaGN1AXY05fm56NvWd9FF5Q-49tQZLNAnxGKdOArZKot470ndZRggLwjgbOmeEom13tvgoCpOC6eqMoPNrLYoPrijUXuqcUdC8jo1RMpKR_YDklvUL7PlFaxj0_QsnMKXaaieAk-juF6zrsUhy24-t9KH0iWUrPnGtQ5uIuXBX1B9iFrtbAqaqULCopqrLPROUPcbSSqaq4EoapGn8D2s4_Hd2ZXbzNYR8C7y67bUAF3aysWc_-uNoGDmPO-1MlT9Zbpko4JymG84l7IQQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYQCPHXybhWESnN_N3sKphbleBEbmb1zBLzjQN5La70MUVs5MLZWaGpPhMSM61y2UI5AyHIiTLQGGEH6C4eBtFXNlN7F6m2tTrbLJcTbtvWEn9ttLXsGsao978IslL9JcEGN_YHsWj5yX1DWtY_e39FO7i3ZtCj5mm6QT0BYnwZYYmEzj6xk1CT9uFLd7zZB4NgZZRiCP20deg3WmFXOO3aZ-JlGt2Jcf-WDjwyf-qrMHP4lnOQW6tUY4egvq2Jtr_sNzkidfgUCOniD4SNS4MOWcCP-_eGJQMndWVEmVgKfynWZLjcCvVin5eLm3HilPRPrH7HGwuhnA_CpcmzYJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دولت ایتالیا آزادی رفت و آمد هوایی و دریایی
بین ایتالیا و اسپانیا رو به طور موقت لغو کرد!
این بدین معناست که تا اطلاع ثانوی،
پروازهایی که از اسپانیا به مقصد ایتالیا است،
دولت ایتالیا مسافران آن را کنترل خواهد کرد.
اقدام دولت راستگرای خانم ملونی،
فشار بر دولت چپگرای اسپانیا را افزایش می‌دهد.
دولت پدرو سانچز هم اکنون نیز دارای کمترین حمایت شده و پیش‌بینی‌ها حکایت از آن دارند که در انتخابات سال آینده از قدرت کنار خواهد رفت
گرچه برخی از راستگرایان امیدوارند با انجام انتخابات زودهنگام، انتقال قدرت سریعتر انجام شود.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=GH-voRMiAQVI5Y1lxhUPgVol7OMha4y-eRHnKBtGU0velpyDlh8qhhHs6a8RhjZk1dOxRqZwmSelZ_iHnQ8H_fTCdKvF7wX6UHLszpxo2fzSazSsezyxJ6sPHBEJ93xiZjgCk_C6356fBq8nsYJmlRyO6zEvruK0Bo7uPGhFeatc4zwAVSuPi7haizCOylhnRraYG-3Fod6tty7bdKoO3zdFzLb8x4jbCU0t_-LSlx_KVjlCDgzLRrZD89SA9mKMGhL2bWnhfaOpgwGXI4UcHfFPtyGx6r0hHvumrErUBFqmFInvCF13WBBGdMNwh6TGJxXoKk8tBQRkb0WiD5JtAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=GH-voRMiAQVI5Y1lxhUPgVol7OMha4y-eRHnKBtGU0velpyDlh8qhhHs6a8RhjZk1dOxRqZwmSelZ_iHnQ8H_fTCdKvF7wX6UHLszpxo2fzSazSsezyxJ6sPHBEJ93xiZjgCk_C6356fBq8nsYJmlRyO6zEvruK0Bo7uPGhFeatc4zwAVSuPi7haizCOylhnRraYG-3Fod6tty7bdKoO3zdFzLb8x4jbCU0t_-LSlx_KVjlCDgzLRrZD89SA9mKMGhL2bWnhfaOpgwGXI4UcHfFPtyGx6r0hHvumrErUBFqmFInvCF13WBBGdMNwh6TGJxXoKk8tBQRkb0WiD5JtAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1YIZFIamsV-7503AQPiZZx7_7ERE6biaOHkoBgo0JaHJ_p8srBH4OqzHdWMdArufNqmtgFM0UwrrgY7YBVjtLwtnPwj4RaZS8WNkJ1zB-d7rSxhqWYAcO3V0SXgv-JH1MWdaK60g7nPb9Wlr16Mq3eb94kHwco43EfZdgr-51b4Wzx8uSXBtt5CFWUrIlLJ56xw4I--UrBlyCyfNaA_-VYcmWGliG5l8DuIUPXPkjrsIlrPsw9OWpIVj8xlsRe-JWYk_3U51RWokpr57aYpP_mnmc8hm3PPYvECeXpS2oKJAzniIqR0VTmIbxbejAs_417n-gjouftXZQLQEQZ-ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWUGkrs15ZjWk5J8BftqzGL2DMdUbU0Mm63HGSRmdBRgOui3zbfc51MMFwfK5o1dMi-uD3rZZENLqItLn9q0KbAeAUdXNZFioDxzAafnY2G0hu3Eh_ZblJfSm_NkaBx1rG2V1skLoLsumEg9OYnP3SfZiqkEp6tBSdhbHFqgv6wi3a5RGa8UEuD_V8kovNB5DTEvGb3TZDjCzbFJ1Qg7Z42jsv9Fw7lP7rmuTK3-t1CFf77cW8-SdTnhzq9JwUyfTyzj5ZwLhcWdtA9irDtORzVa8RlwdDiSxJ4vQlzoRamIRCkPjJfqh6QetonBrHSEZnb_6GLg1BDsaHaDjJH9Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Be3cpTqWGYzvikbvguIaNwDHOdmp1MECqKlg8cyZpYzpVnsUASWVMJoHUMtIQWD1Pf_EM6re5nmYjVYUyLavveSkY-7toIL2ks_qhDzK3g32l2hHSUou-j9Qh6jn2D7yvaECrVXVcDGSbXIMCn-RvPLGrW2rCbO1RHI3ebTvA67YY0FSyZRLGP5im_tKxV1I7Sw0acdOD9iSv3TE56Km_nZSbrUYMBakGce_6Hy4d2IgiLSxEUyAbljy1NtOaOBZOh3aM4kQtnjgq4K9Ya20EEy41t2jjno7d3Mjaw5HYEi2-x24Z4H63MOMM8RtDqN1iW7zEnm6NMAbSUAfEs9umg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVjeJYtqErrHXaFCPqEf6FMTIvmkfRi4UuJcAm89VIYgNzXgBbycfDJe90rhtuycn5YIx7mY0pUq0lNhzAO1SzOGFEfInu0qXmm-2kekhfTOAIWURvIsUR7Rmh4TgBo4zYNZ4DzEV_FL8kRQuSFXN1TuTBNSGgdyvtOaDdZ_2oMW_F--baxuAHPZTAwtcjA8fiQcdBHkQP3rBRYvtb7K9t1ftJA1kMJmPzpvS0kFlw5p2p_Exh2DHI-dA71T-6eShK2yULZ08s9nH4zLU56_GwcbDejAeKxNCjCJbV9SoHD09HQIe06pcViXqHr1s4S92y_As7WsFuoyNtcgzrxqWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIxgXCS3nkDfswr-Qqs8xtENfHaGZTH95dgiagCmBM7KPacsiS3Ws6ZMPH-YjoeYzaCiNdUS9ZNiy6btDeEemrUuG-Gm4Ch57QMz6bEP4PwoE5rZP_l4njZzhENabcBe91dcPiwnF4TEdso4W5MpUvsLvtlRZZbSEjGuFKH0pFC6GBmZXdz2h267k6YRDvOr5IpNSqC6mgxIqfnDHZPQbwGWhP4ioOmQ6IkFkjpsIsOcIBcSG9Sxmo9_7S2CZcotrxEPW7U9WF-QX9WXoxS9R-GEF4hcaOtHW5mabtPnqA3zbFABr6WPZRIMBE0X1XdkJsbsoFqLQevv0Y7OZF7AaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEEXibjOJQ-BVtisjPQBn_oFUrVJiHj0agWkaYIM46a7Q20CxpC2sVogUmudLYPWrinYONi0v1jU2Fpb8QyyS0lmCuqc-eTJdYuzSiZBMQrk3JWTtmzJyBRgDUsTWCMedG51O097QIN_ZsGTUL7ZAwaqOtkK4n9d2rXgz29hp1Gw6ohzQqzMIlmDHLxsW3fEH-QuEqI58OyBxI4k_Ffn2hYx6Oa4zAEq1kFXhRFksDrfxdlF8JHjx9X-APUnRf84tugVGdus74Ntn__2Ii0GMLURM4LourqD0PA2tvvQB7LhD5tysIr88W4Z7zGj8AZN-QTbhV6Vjb0HLiOaSaNY3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_ZOeOGbaHop7Ww9TssCPLUErMjXCLd3RhgO2DE7p9e8E929F_I88ojmms_f3bnkj1lW07QdRvf-s0HKTK6kN_5JYcls9JnAl2lKuEpynRlq3V4NO1Olg04jjA6i3XLD9pjvflQ1gMd7MiWCMFnQei43vfNcOaaSuQHYf_04Qj1zIplaUPd8WnipIk9ZFOe94aicX9qeNpMgJWJlakersdP_8KokoN8mp_QLHAbA-mDTuoF1hVt-f84F5fRdY8JO3RLHSMfdYP_VjQEW6zdO9h5XO04FSVTNMbLkiDhegutJowRCEwnGkLRLVl6EcH_06fzxcodNFX4VK3I4vLRzjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=uenjnKuZARgsGOnYT5WbyK6Xrp7n8hLreFPK6wY4QQ4_gKRQ2oxPJMkO69S4pk8hRgBLWSXLjhOAgtHYXIFudxU1wmOjw8sTS-72TQDSxM92se1AbQwGumj6mK4Je4ze8J7pm8tSvpZw_GFF6C6MWyVPhsQqTYZIcoX-MYzDwS_lx5OVyY-qU1tAqjDMr7RNCUBz6pgWy3aZcbBs6zyaBLC1JRM2uQ7iFroBkSiF7pP24v_JflbJfwcJ8G9_F7Vl57dO1of_6UNL6UVltsk6mR4veJyo2f5p-fsR0wMBDAhrcOaO3hW-nKbDnkYXAsCbWkH6Xi7Nu-b5YN2F9_u0B6EusH4o5lpqkyg49H8nGx7LfuUY3lTL_q4bYw_Z0G1Mu3GAHA7i_cnkmKuJzsvpVsehqgH8C_3bETNWp1xqD4W5kqL80jbCunt7IZ9I7i7DqoiiZwTAen_Lc5D2dXAxvPyfaerVwCHQx9MSzROy9AYaKVoqUBja0QFsPnQQtjnEhLZz81k7TdB8GQQvs74dqt-WFTMv0aduPhBPSuMAjVdvAOcMahq6LEOnWdYu9QL4_8cOZKf0XnFoW_u9S9fsvQFMnASirxmV22vLoS9c4_D2Xc6LvOypIKKqlZcHqvSvD7eWuQ8WylqRnjglAev6I9kXek9mSh7dIaVpEKsQNJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=uenjnKuZARgsGOnYT5WbyK6Xrp7n8hLreFPK6wY4QQ4_gKRQ2oxPJMkO69S4pk8hRgBLWSXLjhOAgtHYXIFudxU1wmOjw8sTS-72TQDSxM92se1AbQwGumj6mK4Je4ze8J7pm8tSvpZw_GFF6C6MWyVPhsQqTYZIcoX-MYzDwS_lx5OVyY-qU1tAqjDMr7RNCUBz6pgWy3aZcbBs6zyaBLC1JRM2uQ7iFroBkSiF7pP24v_JflbJfwcJ8G9_F7Vl57dO1of_6UNL6UVltsk6mR4veJyo2f5p-fsR0wMBDAhrcOaO3hW-nKbDnkYXAsCbWkH6Xi7Nu-b5YN2F9_u0B6EusH4o5lpqkyg49H8nGx7LfuUY3lTL_q4bYw_Z0G1Mu3GAHA7i_cnkmKuJzsvpVsehqgH8C_3bETNWp1xqD4W5kqL80jbCunt7IZ9I7i7DqoiiZwTAen_Lc5D2dXAxvPyfaerVwCHQx9MSzROy9AYaKVoqUBja0QFsPnQQtjnEhLZz81k7TdB8GQQvs74dqt-WFTMv0aduPhBPSuMAjVdvAOcMahq6LEOnWdYu9QL4_8cOZKf0XnFoW_u9S9fsvQFMnASirxmV22vLoS9c4_D2Xc6LvOypIKKqlZcHqvSvD7eWuQ8WylqRnjglAev6I9kXek9mSh7dIaVpEKsQNJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=S3QynlXW8l6udMbkwrCZLQaKcVurINIP8yyyUousJX2r6BwBJNGifk9EbGlc4Usog-DEnKd9bjtxAUba8qhiXiBoMQhcGlryxYAJTXeq5icwIdD1UbX87IOedBTS3y7g143gmFQghnNcL1Wr7jQuGpjhzS_194XFYRRJSf_ZO7dgKiIRxwp1sMW11xwooaa9wwk5X0PYy6G6QDSOIgdgZtyPa74Cnp-8DXXQvwX67KMobB_7-k2djvF078onO9VOsfXmlCWCDCT18d3Wb4aprYxoSLmJ2pmvadbO-DmfMnJ9YFAqhIm3h2sbassyB2v-PrraPvnEb_-xMBiLBccRcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=S3QynlXW8l6udMbkwrCZLQaKcVurINIP8yyyUousJX2r6BwBJNGifk9EbGlc4Usog-DEnKd9bjtxAUba8qhiXiBoMQhcGlryxYAJTXeq5icwIdD1UbX87IOedBTS3y7g143gmFQghnNcL1Wr7jQuGpjhzS_194XFYRRJSf_ZO7dgKiIRxwp1sMW11xwooaa9wwk5X0PYy6G6QDSOIgdgZtyPa74Cnp-8DXXQvwX67KMobB_7-k2djvF078onO9VOsfXmlCWCDCT18d3Wb4aprYxoSLmJ2pmvadbO-DmfMnJ9YFAqhIm3h2sbassyB2v-PrraPvnEb_-xMBiLBccRcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mu1Lm7i6lJA7lap_2nmzVaHrO6HGP_FS3YjVcKhNewFR33DJzT51oE2UDk9VeYrJnU9NMxtLFckqK38k_NFsf2o3jMIJrX5x8U8643hfLK2YUKcDt2EOZhPBELfpxkCT6i3X689cjAb6GLHwAJpEgOciH9m8h2-uyKatTC0oZS1dak-Auw9wXwcaV6Npms_SbRQvpdLCvp7MugHK8FnXwpwvVqc7PckPdx6SVN2igb8VGVttij7qecHPDsDkdCKqNQzRRaUPGuGSeOIolSzF-vV7i3zU5Ru4vO88N1D7QOhZUgIUwTWNvlhiXqm3hPEJ1XDJjM7xFeTBmFKnQhPnFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOIUcWAFaTQZxs8wyMfE7PYQurGC94ZeoelOR4qDo72KobQ2hiILeqWXnLRx97Edrt0hOpGvzl3prCgj85p7ZCk8U-F-BrCcdKtPIgs_92tmdQR5kczIPLnoz0r50ANjm_24JlT2YsJt0uO0yD6KegfhGA1PVgx5PeMKZlroaMKwcvZTEgMGguurArBRIjiiH-lkeXxRHkY8cIw4HyJnqh8ovtiP34YwZzkEtWB8ikax3QYNf5XbSA7pCLuMYbLnJ6z_YSFjJ62Wa6_rLtFUn5X5tOtaBKefSor7uXWr2lI_mBtWisIm5EhB6FIpj6BZ3RAycKUwTMy_-ammcwCjtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=NzRILWaA4rAJ6uaBxoXZrWeBJT2K-cVlE9_tsYYb37uSJOT0FP1BrvKCTsJIc6AFt7RLSnySWhoH_KSxv8qkNOa3Xkmb2O9OC6s0VdfnDed-PKsGNNM_GHrp58jjJZR3gw-KcHIP3kO5rmKpFkpjTdImSrh2ie9Vlz3E0IueZQbE3k3ZRA94VDPv0tjNvjkianKLtQnnQ9uUBLCtW44hVYStkp2AUHlXTYAvc_uRxAxpVRi_rGFIYcUnXoQZKS7r14V_pAvVveiFOxAQsNn4KBs72DUbKjVv9_mpZKJ752JVNy57rSKa1yhAqKBKls1ufkMl7wWZIJHTrgG7F2nvnDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=NzRILWaA4rAJ6uaBxoXZrWeBJT2K-cVlE9_tsYYb37uSJOT0FP1BrvKCTsJIc6AFt7RLSnySWhoH_KSxv8qkNOa3Xkmb2O9OC6s0VdfnDed-PKsGNNM_GHrp58jjJZR3gw-KcHIP3kO5rmKpFkpjTdImSrh2ie9Vlz3E0IueZQbE3k3ZRA94VDPv0tjNvjkianKLtQnnQ9uUBLCtW44hVYStkp2AUHlXTYAvc_uRxAxpVRi_rGFIYcUnXoQZKS7r14V_pAvVveiFOxAQsNn4KBs72DUbKjVv9_mpZKJ752JVNy57rSKa1yhAqKBKls1ufkMl7wWZIJHTrgG7F2nvnDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkRFG11FtWnKe733h90j5oYtAYBqv9WcrcSo10yfuhkcduk9bL22ExVHF78cvNGoIHSbBwEeRt0i1PXgvcs2D6F1SNKpG_KWZQYhzjaydhCXNEWgXp_v6eRq2Of7RYv7P-1WvbYxmn74GBRYnIf9l61jdYIF4lZltlCmztYfS1oXHKP5_nQSnG1s2lpanMXu4MFh8z04Ty4vo92s6Zl5kFCQVx284JOx_q6qjhrjM8lrL_MtQawfPE7fzIEcSW8gdkVFqrsXCaEgJeAy9SFDC-SmFmF4_DciLBRwBUKFobQc7CvXOo2LM7YDkwE4EKS4o_jdfair8qftZ8h_p90ERg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی ۶-۷ جمله نوشته که خط به خطش دروغه!
نوشته که مصر یک شریک مهم منطقه‌ای برای ماست و نمی‌دونم امنیتش برای ما فوق‌العاده مهمه!
در حالی که مصر و جمهوری اسلامی ۴۷ ساله هیچ رابطه‌ای ندارن و مصر حتی ویزای توریستی هم به شهروندان ایرانی نمیده!
همون موقع که پروازهای جهانی در اوج بود، حتی یک پرواز بین دو کشور هم نبود!
نوشته که اسرائیل علیه اتحاد و همبستگی اسلامی است!!
مصر حتی برای کشته شدن خامنه‌ای، یک خط تسلیت هم نفرستاد! براش این اندازه هم اهمیتی نداشت! کدوم همبستگی؟؟!
🔺
دیروز به دو کشتی حامل گاز مایع در مصر حمله پهپادی شد، دو تن از مقامات ج‌ا به روباز گفتن این فقط یک هشدار بوده از سوی ما.
دمپایی پوشان یمنی هم گفتن کار ما نبوده!
حالا این اومده میگه ما روابط مهمی داریم و همبستگی اسلامی!!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLLOGONvRbMPbBA2xFUlLyCQzdzsUGusUnUiyPOjyyLt1T7MOeIUIaOZYc8cSmCOo72RcOyPcxyTwk26DGQrgNmTA0kA0tx-BOeYwjNdGhEggnoLAL1S-AWxzLQAtsuVPgnIrBR3PvvKM17BjdnY28KG0IbGQX-f6RLbsjX4Fny5Y3E2DTJZ7VwHaH4ScTfYYylNCUSt_m25KJbdY2nVJlU7QoIl5nf1hgE20NM1VLN85ojeuHIUD1aXqYvmZFa5adubxjRYfcnNLYUuyTd2BJtWuqOmP3bOBr1j1Wt0LavMSG3-BPaAXqZxvdzOVhtM943bhgJZxY_-o811CsijEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrYXdUPAizCpggj9X0Say73uu3YpKh2lsiovdEfPaKkgSwN5P1qtdMnnL4vlddn45qp1YCqP-iWdVkRKJLtDGuqA5S9a1CAqgddTBEka8KVgGdzzz4bBin1LakjZ-btCAl1gh-2ZPvog8Uqqekz-ywy3w-1AoRAinlLU7ZSnNKhWsBHO2HfZs_biuDehcnoph3HmqG9fqGLMdaQ6mEbpT3C-VQ53SDj_FqK95Hmzn4r_5FEmLa8ory6OnA1hXH6cUe0KB4uKeDJTnUVo6oKZwss73UL5ajHO8oPHZjjiYoVwZlAhijGEW9r0Fk4H5Z1kKiFiddqmyuM9nX623BciVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cV5FD9VYZ4xU2t2v-1kWjwTenfMtmSkqjHBjtikZOY3W-71joSl3W_k1Vag4jhT4Jq5E1ArvFSfQw_Ep_3GZ0Rz-8FyvAsa8KK8Bld3e2ojtS2D_TvxnhhiaF8lac2fcbInTh1Ha1zmwXlYjoSbi4fp-bVD4Q0lubVfgU6nAvP0cedJZTDgdZ46Y8skQnopEYYuaOl5kl87i4Rn2AVg_pl3zpzv84gZXrSes2tgh2oZFq0_AP-fyjZEhToVW99l9awgCjpwptlnOVlqzcyhXFDXm3mBj2kFsL1qpDmqJ9HF8RInzqL3DieqFkKehdIBYtfb2_cXoEk1E3pnuKRJ5DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بار هم درباره حجاب نوشتم،
در حالی که اکثر زنان جهان اسلام
(نمیگم همه‌شون، ولی اکثریتشون)
دوست دارند مثل زن‌های غربی لباس بپوشن و…..
زنان غربی هیچ تمایل و انگیزه ای
به لباس‌های زنان کشورهای اسلامی و چادر و مقنعه
و عبا و نقاب و برقع و پوشیه و ……. ندارند!
نیاز نیست حاصل تمدنی که اسلام
و جامعه‌ای که ساخته رو در ده تا کتاب قطور جستجو کرد! همینکه جمهوری اسلامی با حکم
«۷۰ ضربه شلاق» و «گشت ارشاد» و بگیر و ببند و پلمب، ظاهر حکومت و فرهنگ اسلامی رو حفظ میکنه، نشون میده، این تمدنی که میگن،  یک آدم برفی و یک توهم بیش نیست!  که به سرعت آب میشه و میره!
فعلا پول نفت پشت سرشه و بگیر و ببند!
حاصل ۱۴۰۰ سال عمر و ریختن ثروت و اموال مردم ده‌ها
کشور برای صدها سال به پای این درخت، هیچی نبوده!
نه هنر، نه علوم انسانی، نه صنعت، هیچی!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfFsH6MCewOe2vb3hfyAjhI_MjsRsJl6UUlt8WH9E8Sfn06qnLKfxJvnZGoAWAhjohZm4IfHQXcrcehrTRBkl-gQ0Eb5tGXUKDCLHyFsm0bRk1y2tP7_9o3jvO4BP2CFusHtTy39mhNyZNS2PnxWVtw9KRvH3-lKYi0rbaCKu6ixWxMOoKSypsdezEwHRXdl4dvN4sNHAUwErgFPkggya4Iqdk5QzR7_6hc5_rEaxZ0WY1WfD2KijQb0ptzc0Fj0CXXodhcOJaUEZBq5FIsY1kmbpiV0vAqaQ7abRGxbRqlV9jKAYuSTO9gONwM6uJX8zutrL-n0E_0lg0omS7HwsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJQgqdAG-m66GAPZSaMOD4dOHcTxeWHXwDVaJTN9-tmxw_uoemwRrb_tycahJrp4ftqPOqA9Hgrr3la7L9cEheKVWmOEhMy2-A4aqw8l2RfwPDeYWMiGcNyzMlkWmoOJ0LWi7h68aP23bW18UAJtisWOM2gaoKt4updwL-8t5OzqfdV-t9d9vXhL_mK4jeX2HdZ1b4pJOnsM2ndFTRM71XzQTleiiMIR0BdHk9aYBMVSyomeCa4wq6ns2zd46Ex5C4toBA8hPZjbmgJ-zQiRR8wkSfz3-oeILu2kAAPe_T2EuErXcUwjjUfZ8fMCTvi20ohw6MTTkhdNzTnbDNurCrmk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJQgqdAG-m66GAPZSaMOD4dOHcTxeWHXwDVaJTN9-tmxw_uoemwRrb_tycahJrp4ftqPOqA9Hgrr3la7L9cEheKVWmOEhMy2-A4aqw8l2RfwPDeYWMiGcNyzMlkWmoOJ0LWi7h68aP23bW18UAJtisWOM2gaoKt4updwL-8t5OzqfdV-t9d9vXhL_mK4jeX2HdZ1b4pJOnsM2ndFTRM71XzQTleiiMIR0BdHk9aYBMVSyomeCa4wq6ns2zd46Ex5C4toBA8hPZjbmgJ-zQiRR8wkSfz3-oeILu2kAAPe_T2EuErXcUwjjUfZ8fMCTvi20ohw6MTTkhdNzTnbDNurCrmk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnGlQ6bfPd3ot-JB5i__mVvlvnhDJGtnNY-OrVTL72jZbO7dxihIKbZhkehjPmcYzBT5Vcx-4_UQXtlpl0OtNikbV7ZBty7RTO2bhpLsmdEwvPsS7JtEiYuwwqnMbdj_0yBY2LPorffX4YjQtiWZBrzOvPvE5COlW8pxVc_LWKC8hgJtvesXlxmEo0aVtZFNZfiL2BahusIRmZONkM-cHSCcZcUgxcudXCF7P2amrMtqp0aPPXcUh3NhmOCnjBBhG_TUVCPI1R8maf2R2jxCrg0FOVUg-ekDvmrIu2qxM_tIzTs4VWLQslQCg33pbXI5QnIdfpHr6UpaSfDo_m5RkZF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnGlQ6bfPd3ot-JB5i__mVvlvnhDJGtnNY-OrVTL72jZbO7dxihIKbZhkehjPmcYzBT5Vcx-4_UQXtlpl0OtNikbV7ZBty7RTO2bhpLsmdEwvPsS7JtEiYuwwqnMbdj_0yBY2LPorffX4YjQtiWZBrzOvPvE5COlW8pxVc_LWKC8hgJtvesXlxmEo0aVtZFNZfiL2BahusIRmZONkM-cHSCcZcUgxcudXCF7P2amrMtqp0aPPXcUh3NhmOCnjBBhG_TUVCPI1R8maf2R2jxCrg0FOVUg-ekDvmrIu2qxM_tIzTs4VWLQslQCg33pbXI5QnIdfpHr6UpaSfDo_m5RkZF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=aWlN4HDO2ZLdWBW4svUHZzM1D-zixk5nw48ERvAb4r-8FDh6FW-aiZhPoKU1qYyIJnIF4wYebgbMTWLUpCEvA6M0u1wF5-TRqh4keH2mNZFOJJytI4N70M7ugyu_mVlmwyeNgpq4mef7jZMORZwv9pQLwldIrgzBTlhUcmuGHIwH9-riiRBQVouUiOUJqI13OHR0M4D4RwM724U8BWiL89ObGvMzu7Xnt84v7-Dqbbdmdn77_4lQAtTcPXeiAVhEieg9VhoHF-dpoASdRLJQ0vqnKzZoN5o7PXUteQMNqUBwVVUdMIYZsBxo3lEWCa0n9iF9Jl-cAxJ_CXdXIPbzdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=aWlN4HDO2ZLdWBW4svUHZzM1D-zixk5nw48ERvAb4r-8FDh6FW-aiZhPoKU1qYyIJnIF4wYebgbMTWLUpCEvA6M0u1wF5-TRqh4keH2mNZFOJJytI4N70M7ugyu_mVlmwyeNgpq4mef7jZMORZwv9pQLwldIrgzBTlhUcmuGHIwH9-riiRBQVouUiOUJqI13OHR0M4D4RwM724U8BWiL89ObGvMzu7Xnt84v7-Dqbbdmdn77_4lQAtTcPXeiAVhEieg9VhoHF-dpoASdRLJQ0vqnKzZoN5o7PXUteQMNqUBwVVUdMIYZsBxo3lEWCa0n9iF9Jl-cAxJ_CXdXIPbzdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kv0vQNlQqOLO7fr4SLMPQN8BCjrjEcpmx-iInc6MWRimkDPbRA8IhvjfvH785MDrXR8ldqrPzV9Xznx5ZVGyXr8tfwppbThkPmWEoBkO_BBHPKVHKYMEDHA2iy_OUGzFz92hryimuxCBnuT7gz8tYIXTPg6H6XWhxX_7t8cdYAEsbMF---OHhWyauFsnkA8UCumBiTZBOXm2z5Y6Hmekf95ZiwCDnKF4UeQZfnefFig0DEYhQA1i0KGsmze5j3XqOo-UK9ZcYro8k37tZKsWDCjEzTalLcfSC36uex0CeQ85ttKluoByuRtJWvK1hdbPOok7781boObwiFAYddrEFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxObLk0OybezYnvZtGjaxs70RHuHChyPlnTlufH3Mfls6_4ZNWxriooJ7n8ef-C-z566ltERm-wP2iSGCiuixnek_v8r06EoYVNFQClnoqb0DdmnbfdobDalPgmOYaUH1wLtV1T8Q80IMef8boGmr0sJsmzDk8fbc8qejRBCcgyAsFORh5rkJh-Avizsq7TjvhNPC3U8Yi8dHAKIF8tgybZk-eVbOHV-zTMu9tP-wJ2zs6dxl4FPCVqnZQQSiLmQuIrUfD1NyjIAaPauB4pC8y-_Li_RSUN-LDFEaN8ZHPftx7TcygjLpVq10LsEglMeL2doImM5GQ2DqlkUYwI58g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=KnOUuqlwXs---oGyVgKob0lwrltKg6VvdD0LZUhPIkEYp_JTsBdBbu_xYIuRxRoUs7XD51gyDCrRPMJpjpL6-F6RqcZJeUKzxSb3wQQExosI8_FuE57ZIM21bU4JtKasDFNjuHDNo2kyUPxDoaq_RcxJedLzvayw3qKoT85LvmOSUJzVTEkxUFacosxNWRb5wMCQSDg4X3IbtEwMB0FoQEJaIA0atCtzUZLSVMTuEUE2ODCsF8yZ0jc-UGCbK7-FJnfaQYjHgsibNLaN7MMhQQ8XkhWLAXfP1OcV2lkXSK85f941wvZID-5WlQLi83SjhqH6AbrU8rn4zO4hO6SJDQ-a2uUw_KyevF7TVGjdys65UducZZ0qghVf-NpoAOH9CKmUdR_MEtGTJVzwQH30eRl8gB0mdwhmDvSAmGw_g2N_PHkHVLsK1SkWofkczOB4DmJOBTM4AaFNegdAQP5xHrhWmxf-19_XF6oeDe10GvkOd_QIkmxyNwemN9p7e__krgeFiHH2rze6lV0HwVQWtBiJY8liWc5UZK9yeUHidoxe-zMiGlPEKB17nbk7dJOcxl-G4RITeTfjt0W8yrlxiBgVYSV720H-ZziLKjbuJp1JI5XYknNAa1bKmTmvnkQKnr1R5FLiqJsoeAVa1EqglDjRkhMaujBZFDVwfNUsk5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=KnOUuqlwXs---oGyVgKob0lwrltKg6VvdD0LZUhPIkEYp_JTsBdBbu_xYIuRxRoUs7XD51gyDCrRPMJpjpL6-F6RqcZJeUKzxSb3wQQExosI8_FuE57ZIM21bU4JtKasDFNjuHDNo2kyUPxDoaq_RcxJedLzvayw3qKoT85LvmOSUJzVTEkxUFacosxNWRb5wMCQSDg4X3IbtEwMB0FoQEJaIA0atCtzUZLSVMTuEUE2ODCsF8yZ0jc-UGCbK7-FJnfaQYjHgsibNLaN7MMhQQ8XkhWLAXfP1OcV2lkXSK85f941wvZID-5WlQLi83SjhqH6AbrU8rn4zO4hO6SJDQ-a2uUw_KyevF7TVGjdys65UducZZ0qghVf-NpoAOH9CKmUdR_MEtGTJVzwQH30eRl8gB0mdwhmDvSAmGw_g2N_PHkHVLsK1SkWofkczOB4DmJOBTM4AaFNegdAQP5xHrhWmxf-19_XF6oeDe10GvkOd_QIkmxyNwemN9p7e__krgeFiHH2rze6lV0HwVQWtBiJY8liWc5UZK9yeUHidoxe-zMiGlPEKB17nbk7dJOcxl-G4RITeTfjt0W8yrlxiBgVYSV720H-ZziLKjbuJp1JI5XYknNAa1bKmTmvnkQKnr1R5FLiqJsoeAVa1EqglDjRkhMaujBZFDVwfNUsk5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=FtNMhFXwdS29Oty6OGVgMZUYL1UtulC36uDjBJLjeO7KAFoF6Sa4MOwvKUApAKa5UNjTmsjq275ZN5_4lh6MBlcBfhPLUkYBNpoErqhXeTaQSyW5iHiFuJnysWTZ7MulcsRkD-Q4Ry-JQOcByAMq3dH5yDstTLZnGo7sBl5Zngjoswht_iPIByqiwf875KO9yXDKMZREuWweDQSbpPLuu6v-IHH2TpcY1neHccuOdB-kCuMTgNcpuVoBVBCt6inT9FS2TtKauHTtuz8Hsy7DZ0PnvZFwhZxf97FCs8HzinGqi4EkG69wRqir8w0GnL0XH3TJjRmFLNxQWD22_0kIhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=FtNMhFXwdS29Oty6OGVgMZUYL1UtulC36uDjBJLjeO7KAFoF6Sa4MOwvKUApAKa5UNjTmsjq275ZN5_4lh6MBlcBfhPLUkYBNpoErqhXeTaQSyW5iHiFuJnysWTZ7MulcsRkD-Q4Ry-JQOcByAMq3dH5yDstTLZnGo7sBl5Zngjoswht_iPIByqiwf875KO9yXDKMZREuWweDQSbpPLuu6v-IHH2TpcY1neHccuOdB-kCuMTgNcpuVoBVBCt6inT9FS2TtKauHTtuz8Hsy7DZ0PnvZFwhZxf97FCs8HzinGqi4EkG69wRqir8w0GnL0XH3TJjRmFLNxQWD22_0kIhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLntC048w5w7f0XS-v9WVbfTWIUy_apa4wB6nMmU4neXNH1A3EBG6MJFIeldDuMGehfdiA9KIRs9rlDHmF9C5YxG-tB4EqMXYvKEqhKeBwc_39Bvm0HpOiYQo-bFNlrkFF0eSHebsdq8JC_Uf0EoyfqjoalGbHcvo5-TquCc91HUANRme-yVPHZtr_EPcmJNhXnnYfjUVr8tASUnRb_0FF-WunbIFbdFt4vb4WA5IZFUEdIe0ndM6BIhBveKU4A8mvcsHJH1PiG7aFc-7Ba-Kry9jTLHrnW3AF4GpXEEfQ93Y0EcUYtt52Xhmv9aS7jh40w5dHJV9KSSRhGueBJbBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C5pGbsMN8vPlNGibuUenrG7CfB7R7mBXNXCBSmzQLrrFDqLKsBh9YMfl30s5gVn3_k6OvDpRR_q2wEpXQ4yx516ITAMrJrldYL-u0ipcy1IkoguelhsxNSPPrTwoETtVqfN2pPxV2zlQsk2bs5c4sFanxYrd0ULhJE7LimCm2q6pW0SwjEvk22vKWeGPjtmU_2g5AnS5ouoNW9Q6bxSV3TWIOag3q_QFHxhTgNNj2NyxN3E3-Wz-r81jt-RtG1-WUCuabJV074a64-J0ms0Zxiv6TgHe1X2Eunj-ZmQAqhrtZB0i072dWoJMO1I12dWxhpXeNWbD8S8JKF9lF9aeMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1X3cIB4fRkNav_1Vj23UghKcj_cCWMZZQn0J-0gf8B2w7O2SONoRbdAb0Lb4rU2PyRe_-SKj9L3ezA50rRDOga62PtZUzC2WTvdn4rBVP4MLCS9r_1pQWbN37-Yx3pDi2d2rTp8F9jtHW6q2TEaQGGlImie5O_2-tW-bo9T00ac5vlOemIRaOUqmnBfFMc4rEpMCDvBtZctXwAFqXs1RWY0EsB1jqaXe4sHEcUHb9BRbaronf_J1frejQR1s6xZQRPQozcB2vx_AmtREoCuzp7r6aTOT3HBsS0H7IKMqZNYbJrRSV5WOdWIVGJd2RaVmfqUMqBJoXJT0yT3wwOKLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=P9fWsvSjz0TXLU6hUvVs5mqxGLKjqRASDGFmkn5Edi8JlEE_OOs3lhGNEvJUtdAhW8CwlV-oR-XGlZQ2daA6tEn39vPguuZn_ZprzV80MTjCizve8TVQPyd8A-VdFJD1Z8g6a1q2tel4B6KGV8ZycG4Vd8IGm7yYb9OZ4HH_8zHvbtu63vGoCDo5Z4ePg2wAeGG7OaSMraELDGbVL8eTiKxvTkH_HbhwYXL_tmq_5mUU31-0AMoR2VIakuEWDIEbwlmD76GelZCS3WV8uIsPcAMC9YsCovSubflVVNKS5Xks2a_u_gdd8Td1RfxOEq3KfVPj31rPcCDaWDNw2AkmHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=P9fWsvSjz0TXLU6hUvVs5mqxGLKjqRASDGFmkn5Edi8JlEE_OOs3lhGNEvJUtdAhW8CwlV-oR-XGlZQ2daA6tEn39vPguuZn_ZprzV80MTjCizve8TVQPyd8A-VdFJD1Z8g6a1q2tel4B6KGV8ZycG4Vd8IGm7yYb9OZ4HH_8zHvbtu63vGoCDo5Z4ePg2wAeGG7OaSMraELDGbVL8eTiKxvTkH_HbhwYXL_tmq_5mUU31-0AMoR2VIakuEWDIEbwlmD76GelZCS3WV8uIsPcAMC9YsCovSubflVVNKS5Xks2a_u_gdd8Td1RfxOEq3KfVPj31rPcCDaWDNw2AkmHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=v9WxFKSrLWvrX9boZgbEdp_yt3sDNJ4rrjzZ5nZ2DsmVc7EToZ0_qdNRT8QhGzJXbUWAu9WPAzUpyFhZ07B2FNLPyGMi1TYemDTSnQKAR_Y5MVsoDTcqfLxSkRc6E3ZIyPPo3C09AX0WcdAaomwwRAehdCQa_n-j0aWU6bq9l1cacm7zPkkN3R70JqJAKrqeSJHnTrFVFej6G7qy9bbAFW09jIqg-ZKd788y3-__4hTrjsyMljZDXdz8kUYfVpZB9YOunDSfb4jl-HsRTb5yZ9fll2zQYEafVUTwuOSLuMGlGfN4ugTQ7mkTZguAmovAEmlWaxPl38cbMkxIfH4xg0gWBf5-krI-Eli3svx7c0gnP-rsnHN9rKGL_s5uVEP6OCoF0ZU8sCXY1V5LLq2EFNTo6uaNTcyhXfJdDt27wcyxoVHnVU9jjoWBTJYIHlexs4Fgn7lhn7JW6Bp9PBeX30dpffQ7AX2xflx9Sa0DeHUN9nwUsbjniD9mWcuscFkxxUAVVcWiat4Ss-BpBqyVJOdub_PK4Zynu5r8C0uT5dx3lh0VLXAEEkSNih4vfc2HsmL5w3OgYwFOgoF-S-xH4t9GT_7w8MGgxTVBU8lA630d6tJP4sO_em-MK21rM5fBz8RgT5-4TToxHGoIG1giFAqbPiPj57sc2fyIJLrAtHY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=v9WxFKSrLWvrX9boZgbEdp_yt3sDNJ4rrjzZ5nZ2DsmVc7EToZ0_qdNRT8QhGzJXbUWAu9WPAzUpyFhZ07B2FNLPyGMi1TYemDTSnQKAR_Y5MVsoDTcqfLxSkRc6E3ZIyPPo3C09AX0WcdAaomwwRAehdCQa_n-j0aWU6bq9l1cacm7zPkkN3R70JqJAKrqeSJHnTrFVFej6G7qy9bbAFW09jIqg-ZKd788y3-__4hTrjsyMljZDXdz8kUYfVpZB9YOunDSfb4jl-HsRTb5yZ9fll2zQYEafVUTwuOSLuMGlGfN4ugTQ7mkTZguAmovAEmlWaxPl38cbMkxIfH4xg0gWBf5-krI-Eli3svx7c0gnP-rsnHN9rKGL_s5uVEP6OCoF0ZU8sCXY1V5LLq2EFNTo6uaNTcyhXfJdDt27wcyxoVHnVU9jjoWBTJYIHlexs4Fgn7lhn7JW6Bp9PBeX30dpffQ7AX2xflx9Sa0DeHUN9nwUsbjniD9mWcuscFkxxUAVVcWiat4Ss-BpBqyVJOdub_PK4Zynu5r8C0uT5dx3lh0VLXAEEkSNih4vfc2HsmL5w3OgYwFOgoF-S-xH4t9GT_7w8MGgxTVBU8lA630d6tJP4sO_em-MK21rM5fBz8RgT5-4TToxHGoIG1giFAqbPiPj57sc2fyIJLrAtHY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLpTBNln2l5FE4MAGu54yrtxHYP-4V6a_4ofHOBbGpPwiHtfRxWmANpZosmUZjLwhc0ZhRgWz8UkoAVWhW_tR-ci3oI-Qb9wGnSL_uQBg8uoPAe879JLpYZgsjVYdRtYItcCStRVE2ihlZXbHTLd2qOioMxqaPY4CE_SNwqMFcl0dgcpVr7i4apStOwcUkR7pcjG0HNQh2NgIeGsFDDh1EhnDOrNXDG2AgtWdmh7U1-FGeN99BtuwA2Htr_IwCkhu0-yNlYl4b4uloUnoHV1a0jfH4swNc6XIaf8GQ7X7I4YckZV5yQFCeI_DL_Bct0C122NmVH7LkSVEnCql76hSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTdq-XPJeJkZZIkDEx2nuqFLv_0TGExOQ8TMYZNlglS62kGpECnkAeohGi6CdgF1JSVM_PmIXIw--MDTBIe1r5J-3eDIxMRFCxFdYk3lRO8T6mFhryTVUAN-e_45MoQ3Q52cnbzB1hdXH-GKwwUO0MO9i1YzdLdH1z4-PbUhtd9oZAfF1TrS-wZZxEzrGxcym6cqvqpgP3M76vLNuaiZ5vAX1vzXod2wuI0srkzeZKqx4Lj0SIhDBE35ccddcazqOXT5J3Iv1Yk3rK4NDEIsmRD-wpUlNE6nwImDjj-xybYre8edDaapGDHSS_kdPrnLcnw2vlRs2GxPNPdxv2GEIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=ESXBrM8_fpsieI-J-A68qnugeS8nSHDZ28V1T2HRhR8KT1z-1Sl0N0JtswYjwBu0jsOpTEz2R8JQ3XXxWcUqCFzMHhaJiF47uL4SCE75KFFlE6UzMORvq14wyL9xZ0Az35qTLuGR4ewjLGdnRGQ1aK7QvddaAba5mOSyvuYuD_zqINqPVLw9S9VQVDMimahF2eHJzk9u3k9Y_D1wvOB4fHbK7WW0z7rFziTKZRuYAe09-HAxooUU_xQVotdXUf36DPUP6YqZWP2Q8ENpUOy-iU7Kaq01uqghFKalq0Mp3vVPa_JWUe6CxnkrpuVYTlfifxi0Xwo2hIM9MFWFBYM5Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=ESXBrM8_fpsieI-J-A68qnugeS8nSHDZ28V1T2HRhR8KT1z-1Sl0N0JtswYjwBu0jsOpTEz2R8JQ3XXxWcUqCFzMHhaJiF47uL4SCE75KFFlE6UzMORvq14wyL9xZ0Az35qTLuGR4ewjLGdnRGQ1aK7QvddaAba5mOSyvuYuD_zqINqPVLw9S9VQVDMimahF2eHJzk9u3k9Y_D1wvOB4fHbK7WW0z7rFziTKZRuYAe09-HAxooUU_xQVotdXUf36DPUP6YqZWP2Q8ENpUOy-iU7Kaq01uqghFKalq0Mp3vVPa_JWUe6CxnkrpuVYTlfifxi0Xwo2hIM9MFWFBYM5Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_fjatpfT2aLOIAdA9wyA6cjb7B3T9daa_LY6SxEOjaVXziS_4dPmZYVKefPpYQIkd_HaWs_e9LvJ8lavTvBU0p5Wr8cZB263DhM-XTFV-ZYM4t9ufBHMHyaWQpEhk1simjWm2HLH7XqPd5smDQrP10A9Jn0jshrB4LUB_1uHJs2H1rTgRqTLmLdWzMZUjf6a_qZatxDo9ns7-ooI5sUPpdYVQcOZk4QuyPxjMhr2glfLQJi3OSzzIwR0Kk0gQNFTfMhwO42TYbx_8PiaKIC4aq67I8n7gOFVqQOB1UenVRfqY0HoUaryrseeSHlCYoHpwrJ3tjBGgQkIZktWa99mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRxpSpx0K7NXN3NHPYgh2aIXeLiQu_ZwqE9zCtBA-qDP77bXXUyvya1lucTVct1lHhFuF6OR9_MArIsZQXoP8bLrmHQfMuJBX7o-cIi1lVPXbnp-HlN_nYO_KqHepVg4lKA_Yu4RZkjT8POifq1FheEIBCRkpGoR8pnWBbXh6UDomEDfnuK-6ekEhLUv3BKpUpVAka03T1q4c_3So1d9uIMWnR2qLtFZblQF8JGD5W4XEqLvyUzL9I-L95sXoDIXUzOXDx1MjNsNEbxgJiTG-_Jx2ms5qbl3KTWnopOu4N4ntMTVG7b-DGRjb1gqS-y_Yhs_cgQjiNgaWyfdgUrT_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6417">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
حملات موشکی آمریکا
به چند نقطه در اطراف آبادان.
شنیده شدن صدای انفجارهایی
در قشم، بوشهر، کازرون.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6417" target="_blank">📅 04:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6416">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
ترامپ : ایرانی‌ها می‌دونن که ما امروز شدیدا بهشون حمله میکنیم. اکنون نوبت ماست. ضربه سختی به آنها خواهیم زد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyXuzi7qy8c8MWwlt7kSd3ad4ZXk8bPNxFaXJNv10Gm7F9CdXpcksPn-h_sVLdxgz0_ftygFGFx8LT1jdPEmkS9IqyD-ESNneV8YITF7MXujVkisHQYfo7Q4mqYpH-7vl9Q8ON0AMSU2z7JaLQhBeB2RwQh0dvGO5NgJydVj5qHvvekyb38fNldoqdNRs7tp5C6yuHVc0Ox8ZrnA9y4T-2NHA0vnOu0jrQYkreJn3WmeiaMNsukA8X_tDt35RJmvgXi231lb6DsaIecRH3xs9jR7XN5VDVBZJ-P1OEmhKc3jVU5prqn6smzwNEEx3h9W4DaF5pZLhK_pYj2bXhU1fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLXqNkw-tKuuejnqpFjdQJjm4LAyuw7ch2Rf6xqqdzi3KOasHo-mM_lVqwT-D4GbHUpACS6JXoSONHWyN170jT9zjV8e6i_WjlM_E0BozpS9mKgtj5zQ1BedKiG2JYsHBReywu0sA88mRzKcDyNRecjR1ThejajfGbzFu9enGxuaFh6G_8zxG5-RqOrytpIjSgooxO7WkLFtuvjdZY3H1_zi1p9ghnsB9TPi8_4xEqC3YCvOlv0RWT5GbK2jEB6KhlUHpq7R4ItmKlUBMpfpoieYvq8wTD45mtaT_xAjX1ExDz3XJufFZh3mK2MbpX5_Hpoq8TnUpbSlC1S1bL-I0m9I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=u7upMfX1E4hXA5sNZbH9MPZseef-5TqLgntayvo-2jj5y_Znolm_7Jedti2ttL5k4PtOvGwHkY3LFPTL7e9i0OqRnRQChlv4n2ufY21FC9UPcHjbpc_eSUmGmO9yiPpzgZRG0FKc1Zp3QMF6v7CGDcxK8yrH4HlTF1bf24QRYnCrhELnmG_fSuB0CXifs87Up4a5mIBktfZMg5CfgV0CxYCoo5ORfFHRhi6C0XNvD9GeNyYgKWvs-X3aUlDa9mMW4sbYg2lKfaEvMJp5Nria1mrFZP6ZJU4cmFkF41NSuj4w7wsv4JXQm2a0x1_lGLgGTVGEniF0vlO6aUPAA81hLXqNkw-tKuuejnqpFjdQJjm4LAyuw7ch2Rf6xqqdzi3KOasHo-mM_lVqwT-D4GbHUpACS6JXoSONHWyN170jT9zjV8e6i_WjlM_E0BozpS9mKgtj5zQ1BedKiG2JYsHBReywu0sA88mRzKcDyNRecjR1ThejajfGbzFu9enGxuaFh6G_8zxG5-RqOrytpIjSgooxO7WkLFtuvjdZY3H1_zi1p9ghnsB9TPi8_4xEqC3YCvOlv0RWT5GbK2jEB6KhlUHpq7R4ItmKlUBMpfpoieYvq8wTD45mtaT_xAjX1ExDz3XJufFZh3mK2MbpX5_Hpoq8TnUpbSlC1S1bL-I0m9I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CBaVyG9Bt4WMWMuWb87S4ZRKizTxiwR01Hk7iv0BfNRfHHECKsz1odkZGimD1jqHSjg1ieoPuQwY6asFdRqqzs-aDGb8j03YNOEbYikJQZ9axfQ2lR3AvHfDL2-ilvPMVxOKaZLlyw510EV8nUfkz1UW5as0c01zq94Pk6S_ArkRQm0bsb1AI5aRUMRj2zRwTO7IlfT5FHI0uLOQ9o_Yo1Wny2YALmE9FxJpPzCZAibNSXj7lDKTzHd7EPKtS8A5mc2J2LfQYY7WDfOnHON2J9_lpMHkAqk6SSp_WrfvO3j7U5uBtf6JxcIfXEe9U4CeyPAjp0_iPcbS4lrIglJpNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHlhZ4ar5GgFoY6I0xIkUmLw9Stb2-KyrXIBWiRcOXOWzK8xtWPnrnLxxrl0x9W4n4EivpuTmnL3SixBKh58rac4nYCXPAuXagHPdtoQSbcUZaF4sXNBTO-l53VcEfzJ_xMlMnAcFpjIYKBf4ueyEf1RqGbGe8ql7VUT3SW1J-mTPsK3zFr3B_Wv6gE8TkTD3Tk_6FSAW9eVTghWTbnummQSkbhPcyxOui388ugPqyeGr1aRCUFoHxvmvKyWlBjl-DeLVVKgqK3uqAg3FNEJJEI7s4RsIAqP-JZenK6cFIXt7fOX23abqG3W-BMYuAioZg38TNFoy9yAettBouDEvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی از کشته شدن ۴ پاسدار در جریان حملات شب گذشته آمریکا و عربستان به مواضع گروه تروریستی حشدالشعبی در عراق خبر می‌دهند، تصویری که جماران منتشر کرده اما ۵ تابوت را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6412" target="_blank">📅 18:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=PkuoUvAQA6ML_KQ35iSkLANBsdiDIOxzevalxXXHBGV86Ae1UbC3SIq0tCs5prqYtOb-iQX5NmussrrE-BabMuzvy8YyDwU2UVjVfZRycMGY4WuktjvmctACpPutcnXcwFjW7vVDGNdQpc45HEE_9d-hLZ2zIlN6xbA4lE44XcGFGCau3gD34Kwq5MRFwn0zUHhZsR9ikr-M6kkhpo8kFsuiDft8n4enSjDbfXJw0WSm_la6ApDiQyGdmCeiPTsYnwmMXZYImDtlWcyu9PRCQFmirT2WbepwtRCTsYvJL3V8DdM58JKurIgBtTYTRrCnBRVwkXhkSzD0WRCVaEEsMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=PkuoUvAQA6ML_KQ35iSkLANBsdiDIOxzevalxXXHBGV86Ae1UbC3SIq0tCs5prqYtOb-iQX5NmussrrE-BabMuzvy8YyDwU2UVjVfZRycMGY4WuktjvmctACpPutcnXcwFjW7vVDGNdQpc45HEE_9d-hLZ2zIlN6xbA4lE44XcGFGCau3gD34Kwq5MRFwn0zUHhZsR9ikr-M6kkhpo8kFsuiDft8n4enSjDbfXJw0WSm_la6ApDiQyGdmCeiPTsYnwmMXZYImDtlWcyu9PRCQFmirT2WbepwtRCTsYvJL3V8DdM58JKurIgBtTYTRrCnBRVwkXhkSzD0WRCVaEEsMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=kTxYW_lI49chDvBAs2a3pEybcVuioIMW906g5RbplzLfdS0M8Tl-XTLX5eTXZwv9VnGxZpSsha_qgU7R232UEnmQhPX04uGxJvL3kFGTFt6e-Wh5hQj0Yanxj_NVm6nqp2PQehkjcI9OALwFOwZwyofS5lUxMurp840f92p7SWno_NqqLPWjWLyF54SRFi2TtmShIGDSj-VZ_mGGsjRbZZ6rgJPdAMn2oK0K_aSjpvQcH__0_O0hz_5XM7-8ux0Z0uwAi2usvmZ7Z7O41Z_3YXW-hC5nz5JGlqDhhQqHkKPRR7GBy3gloqZNmsTlTvMFJJX25NCvtPYycQAEYB1EmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=kTxYW_lI49chDvBAs2a3pEybcVuioIMW906g5RbplzLfdS0M8Tl-XTLX5eTXZwv9VnGxZpSsha_qgU7R232UEnmQhPX04uGxJvL3kFGTFt6e-Wh5hQj0Yanxj_NVm6nqp2PQehkjcI9OALwFOwZwyofS5lUxMurp840f92p7SWno_NqqLPWjWLyF54SRFi2TtmShIGDSj-VZ_mGGsjRbZZ6rgJPdAMn2oK0K_aSjpvQcH__0_O0hz_5XM7-8ux0Z0uwAi2usvmZ7Z7O41Z_3YXW-hC5nz5JGlqDhhQqHkKPRR7GBy3gloqZNmsTlTvMFJJX25NCvtPYycQAEYB1EmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWAixJcLg7dvQQMKHWSd2CZ86e2xLKjZnOaz4QjiadyDz1jfpqLpt5386AzZAj6S_05ZlyHjt7QQjj9hUXZPOZa5yPgbP2OdmeXnBGLeeFSHDwo-r0_dOwR-gnOJlfouXrhZjqy9eEzqpXBG-THx9s8hWNbR8YELN7NrS9EVgDiVfVioIQiqQTYVMR-Or8pwLYx29xIT6O5A3iyeh6r1grO5k0RinHwMvbCOhBBCkRRrjOihz0rTONFfGZnHe8os0O_yb5-WkIhlcgBYkabNzoeWJi5O898b7tIp9IKHSSqMcJMRzVGxeck_Y56X2YE0rJKKlVsLVW-QqboJY9xcSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGakh__iq6kfcF42uSzUa3Pl5r87CNPpjS3oZWVzRyuPnrz8SVLXvNSCeyagFr2TeX74BRe0p3ERNcWqt_ZgkO3zHzx1J60tP9nKqAl75Ll0K5nrTtk9caEEQUIfrGcRHM9hG_pgoqmZX8nCwTkpTl_03tY-A-F90utMl6YWk9DFBvfCdxo-GDIy4_EQJ__NsmRUKDKTKF5AYRuw-Ellv7OJSGhV1AoxleTCg6A1IPcjVsIjHY7EagH2sRNMY2wRAnPUfq20rxbgW746i0BGnqz20AodZ5-G2pzS0e2LTfFF3CfwczDVk6NUUo7YOuuzhFaqfkdzDNp8JYrvdR4HNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=KSy1kk3ErCGtvMytU2-_mKxfMOfWNVoOSZpi82_gTKaZtbbwORLTdCjVF2uNv45WbDcozSIU_u0BIXL2ok0lLPymMKZcd-m6GUztcZgoly8eLCVU7us5Y_G2eAPdXylcUmUuPXY1rq-7mdH0fgA1PqssxTh7KkfhvT6dgqGEPI-GbbhYSzeJHBmrsdB9IYlF6GJT5lFfTemH-ytGN2UoOQS8OBmFxsXo4IZbU55sHjlsOeQn3RAIVbI7QWKNmyYS4ZVWcThmwaTMPCXs1SogDoyIYPko3wSIX1xXuteN4VqtcIRKLGTkGDA5zhtoS_MjdHF8-Melps8OPC1d8lngdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=KSy1kk3ErCGtvMytU2-_mKxfMOfWNVoOSZpi82_gTKaZtbbwORLTdCjVF2uNv45WbDcozSIU_u0BIXL2ok0lLPymMKZcd-m6GUztcZgoly8eLCVU7us5Y_G2eAPdXylcUmUuPXY1rq-7mdH0fgA1PqssxTh7KkfhvT6dgqGEPI-GbbhYSzeJHBmrsdB9IYlF6GJT5lFfTemH-ytGN2UoOQS8OBmFxsXo4IZbU55sHjlsOeQn3RAIVbI7QWKNmyYS4ZVWcThmwaTMPCXs1SogDoyIYPko3wSIX1xXuteN4VqtcIRKLGTkGDA5zhtoS_MjdHF8-Melps8OPC1d8lngdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا و عربستان شب گذشته
به چندین مقر گروه تروریستی حشد الشعبی
در عراق حمله کردند و تاکنون اعلام شده که ۳۲ تن از این نیروهای وابسته به ج‌ا کشته شده‌اند!
حملات به مقرهای حشدالشعبی در ۷ استان عراق صورت گرفت بصره، کربلا، نینوا، کرکوک ،
دیالی و واسط.
در ۷۲ ساعت اخیر حشد الشعبی بیش از ۳۰ حمله پهپادی به عربستان انجام داده بود.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=MEcI6Rv5WPRbYiF9FvFa51ijNR1lAry6Jn0E46SUtQZK4lYfPUd4-zuKb-3cBPctCzvVqLYKm-IVioE4ts66K6BEtkEhULU2gLaAA91PxGvd9EwmB8VAKfUlvsrq-dVQdmjhlYTI4PxUl-vYGGosFYpPU0vwX95ja4yZ3-Ay8f3nvyKsIM737-VoRMLL_XRkxL9J9V9JenoSKYzd9xCJIumtvnGMoFI_wkvLS_ohjTDGxyYFkdv108VKaT_pCldL_RFLUzjksuKXj_akFPYxzOiRmDPgM7HMTadcI_So4QfpeKaH20kwxZAP6UJef11ALDUBz1MtoWfyfv3XxWpOZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=MEcI6Rv5WPRbYiF9FvFa51ijNR1lAry6Jn0E46SUtQZK4lYfPUd4-zuKb-3cBPctCzvVqLYKm-IVioE4ts66K6BEtkEhULU2gLaAA91PxGvd9EwmB8VAKfUlvsrq-dVQdmjhlYTI4PxUl-vYGGosFYpPU0vwX95ja4yZ3-Ay8f3nvyKsIM737-VoRMLL_XRkxL9J9V9JenoSKYzd9xCJIumtvnGMoFI_wkvLS_ohjTDGxyYFkdv108VKaT_pCldL_RFLUzjksuKXj_akFPYxzOiRmDPgM7HMTadcI_So4QfpeKaH20kwxZAP6UJef11ALDUBz1MtoWfyfv3XxWpOZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wjdq0fwXhCfGx-96Fl1xiZYPSa8zCE1tNKM7vsHsAz4aLuj9KRXSg54ZZ5uOkvwBkeg-Qku1rgwoJTBldOR-_Yqh5zbsbVDaOV1w5nQ7djJMVz6jDfnzlyy2Vgru-obNnT5yGfhxVtdSQHgnCCJdekR8buhfPzNReXqorQypXW242G98OP0owJZEe6UGymkk8CmM63BmXGbECN6mwQNH2Pqoo3SP4VqSWivxIvwvamwfFabORxeE3pveJ32s1K1GQq6s-LZRT3Ujppiw92WjB8Zq5VGKhEUS8iVjjukjHLno41RfpL_dm3-8DDBMbBQAKEt8lIy1jqgsjBMZbkSn3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟
این تجمعات شبانه دست کیه
که هم دولت و وزیرخارجه ازش
ناراحته و گلایه داره و هم سپاه!!
کی بهشون یاد میداد که بگن «بزن» «بزن»؟
کی موشک میزد به ۳ تا کشتی در روز
و توی خبرگزاری خودش (فارس و تسنیم)
می‌نوشت : «به تیر غیب» گرفتار شدن؟؟
مگه معاون سیاسی سپاه در یکی از همین تجمعات سخنرانی نکرد و نگفت
: حملات آمریکا به ما «واکنشی» است! یعنی ما اول میزنیم و آمریکا پاسخ میده.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMjIyRyNab3VOicmp0wF8WragFlhQ_6AXCV3ssVcmH8IJxw6mFfWnWpwKaub42PfNBY5plfX5PP7ifoaHP_1f84YSfvCIjKIaGf4M5Qan2ADee7_Wn2hQA6nXLuu9_2CsWYT7iLepSEZraKTDycd8HCWD4Qf7LdElB5BFJSumEzQHA_c1UHeMeOIvrgw929CY_E42mOznG5wzxRKDZRklDLv96NjOg17fZqA_A5LGIP0_7txtfkJu3vn3znArZ0Oea4VIQJa85JjnjJKt79KaLj6KHZLcUE27gz3vg0ToSfj_DlFDdzPj-PSzEQoF5elMSGLLIuaTI2RKY0gqrHuHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLaBflsDavmD5BcaYMHhoF8DMCzoiZn2s4ZtCQLI87p-NZahYnNZ_u369-Pdx4rX0guIVqOlFf_sPzc3jiTSDtIJoEnUQrMvimXD6PyBPlXNSuc2U7WgF04i3JrVRWWg1-oZXB5wu1G8f28-3io6FQjeNpJWRmyQToYtY2tWsgO9otRZuyFQG92AJM0JdL6gMy6QKeuICOzQrsEYbwX84N6-qeZVqUY5nhm8CZ8GlYfpaWiZzFwegen2ZSk84bbVPu05XQGm_nJOXJD4hijGT6L5Kx0xjTPZMt4ux1IWRIOLy9Sn826D-hH2Qt38lbKoFJqX10GzKN0EAiXE-6WfvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grlY77W1GackKxE_PkoUAt3RkQr0wBroGNS9QGCTraoYpAe0Rxsw6GwpansqT0eWZScp1GJgWARwLjcjb_z1RXrmolH7goIa0Jzd0mAjOU9Fndz8lqYaphfrdB5jgFC3_VhzHC_7uCXGNw3iZws9Zioptu5LiTISsv4yMXEinCIbtHM4cmLK7JuHy4kgGq3EmvlcPHf7YqbLwebiTgKnEiIyMN7fmTD9jTesJlParS6ilemh-L_jnD0ZoTWz9Bxm35KgwpIBpKwjmsKEIig1HDbmRMiv2Y0pLb4v4nsKz__5_1ys2RcKZBrnruvlEQTC1_PpsXwrycP-_GWBSdbkrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jCsnpQlTlij6Z4wTpAqxzgaCwijrBie3pTNCzb33vbHZZvci7CUbYN_2WFKE0TbLTS5nAAX41CYi9Qd7-F1dMNPp-3TNg6d9QP3yfndPnhe3IYI_OlSYblHaUTBrmHX1njiGsX2oNEzgS1Zd3Yq59aKFuWp21zPtCy0anZN5iMsodNuvLjQM61vmZ962BdDgiTJYUyj3W-UuQYpP-lKOyyqI0WNW_h4-zae4_lPMyVTTgHI_7Acu1gAUB8vQ20FT7YSmLonFXZbaAdDQRCFVkyDnxte5T2Xw8XhP8XbHtITHnZDxPneTe7xhe28UVtp-Kp3kSssxGTCVVZD1jUKEFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2DKyVZk92HF39J-8bxcWdu0zla0EQadouZhavJCZxPWPcsXnC5WQE9jcpBT_ycHvwR2TzzRmOs5MnFDREBO9tDv2UMfKzrpa5l1xIhlPDEt9WgkcYVUA3db-c9BuWqNh3a4FGNaI0M4sri_OnmPlXA973EqONwOixJFZ4VXHLYjWQJMUXgxh7VxznFiso_yHnyQNCKBuYBrld7klmflxIHWGXP2oPMk4WjX1mjYB_nlm51yoAv6Zo4VPy5ZhHQYdY_O_xmWEEYfMMX-NVzgig0ES3yeJFK61Q9hg7jlk5uxqBE50h8s0-t91Pf-45NRanZUTy_IZ8ylDg_ih3MZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s5TB2mbhmY2uhH21UOteZwwzruVm78KzkAyht5UjVWQD-Y1HnBs1ByqMRKfBUrA6DyUGRJPj1h5P3JEUxZ05IowFC8iMG6olpzvZAF8RdQsXuyGBo9G6PmVQMTQvqmP1efJc2YVLieUP_pxu_xpDlJGSnWOXqG78GZYUW8DS5ZQ3mDBl6QLuEzOlR4BY3UGL0E-g2HweiODrYdA-gQ4Xrwzqp2Dz2JGfXckUqBS4XSMFs6uFTlG0VUJFRcLsPqTDJ1UyB8QeyabBZDBXOzbX-6VHO4ItohNvYSyva72BN9z4c6bMymn8sO3Mw3dd0JceFsuqcR62FtvZesLYlKKC7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O3vTlZQMtcv3FQ3BvQ-dh9QA3u5kt50HtNTAZPARzu5ycOjEhwkpHKIiPx4gIRCJqoejBEH99jqheLTMh6GYXm5ZWCSSnyHgPK3c_FO2MTSKgQpvnAJoVgqlMLT7MuPF2363aE0XydFCu1vD6masDdHPyRSOePKfUd63pa8upqJF0PpHJoXZNN1hPBnnZpr0wcIkgJINpszjb1TWwxpi9U5JhYf0auBxorDPOhTIiEKRin4-Ch5CVUc3_0Y2sDA5TIsfwqjnX7mGipbgwx7rwQx79BA5T3S84LDeXqMWrMOYphBKVKdM6uT1gyBb_9pr62gTwgj6CZqQK5yU5eue0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">میگه ۷۰ سال پیش ما در خفت بودیم
که وقتی اسرائیل به مصر حمله کرد
حق دعا برای مصر هم نداشتم!
اما امروز باید خدا رو شکر کنیم
که از اون وضعیت به جایی رسیدیم
که آمریکا و اسرائیل مستقیم به ایران حمله کردن!
اینها از اینکه به مرکز فتنه و جنگ تبدیل شدن
احساس غرور و افتخار میکنن!
امروز با مصر قطع رابطه هستند
اسرائیل و مصر دوست هستند،
اسرائیل و آمریکا روی سر ایران بمب میریزن.
زمان شاه که در خفت بودیم هم مصر با ما دوست بود هم آمریکا، هم اسرائیل! معجزه آخوندها !</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bz-dKFM0i3bJ8P7wKoNb5US2y7qHLvEKPJTxelvw043YL1KWY9972N_85pg-fXLjbzDjSbOddFsQktEyHIUsCKMcpGpcsd5ut0AWZq9aUFIMud6VFTvTvETh3mfthkgAAWhPkXbZ-4hHuF5wsxJUUx38RxRiPJERJsAsDCFCsFEfX3o_cCHHPfWVP-SjOX1kIPzXjrsYz_-SOUpglS5l7fc5_y2EOWw3ljZtKySZPoZuSGbtDos0Yn3y2ySmrh8ylD5e8CPds40SAVJ1Cf42ZLzy5ahqtKSN_qIm7u-Wnaq8SY2DQCIxqGbQLGVy5eslVUtouyZTTsRwPkWjSQ40DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4hDjj5KSqiOELArWAhkJH-w3HiKEIL6Ts8KclXrC4NwR2TJrsBdCxWdFLZRKQgfgNq22xBR7H_LGocTOBowjlv9lDHdy-loRNMbFaN4BU7pVviPF2_fIIeNqHzEoPNYQ52H332ad7_Xjkfe56589X_l4zg5b_qbVgkc50RI8wIhDj0gbBvwqgHj_HlXFL8gc2xs8sQIYMuXn-b0hZ3qwJJv33OilbgzPxJ8JZvjcXolyyMzEclBHNcM-R6H7LLQq0GfjyU9OCnBxNIUfW5vf1SalfhVFZaQk_q2behvzza293nIFJINVLt2HZdITi2xEblCYhRiLx-eXM_72FNX7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=tph32EqA1hfdDNTKItQhYVts6_yF3mmpCmhcXsSuM2qKFHFKA6RFyjVxkUPScA-Svz4S4oVS7DqW5AjsFtPN0QwdqlSY8yMMYiDhfZONrXSBRsNe2p7DCHHJKJECOBG2ftty94EpSON8LOMvnwP7FDMDjqAerLbUIjcPm7zvkPZwSmWXsCwL8bzbUwYxJk8SLq-N1jzAhZPsazN6TAfgO5aMRyLTdrp7RuCRZzlbaJgeXykZ2Gwq6ETV2ATHiTIjABC8vyHEGTTfk89VDcv-S_hoiAgsQMNvoaVZWGUvc1Ir0an0GfzANlN4SxrAjkzzT6q_5myHgQ9e3BvX4ovDsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=tph32EqA1hfdDNTKItQhYVts6_yF3mmpCmhcXsSuM2qKFHFKA6RFyjVxkUPScA-Svz4S4oVS7DqW5AjsFtPN0QwdqlSY8yMMYiDhfZONrXSBRsNe2p7DCHHJKJECOBG2ftty94EpSON8LOMvnwP7FDMDjqAerLbUIjcPm7zvkPZwSmWXsCwL8bzbUwYxJk8SLq-N1jzAhZPsazN6TAfgO5aMRyLTdrp7RuCRZzlbaJgeXykZ2Gwq6ETV2ATHiTIjABC8vyHEGTTfk89VDcv-S_hoiAgsQMNvoaVZWGUvc1Ir0an0GfzANlN4SxrAjkzzT6q_5myHgQ9e3BvX4ovDsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=pJDE1_8B1c0plxzZOXiYGCVPhrw_gd45jxPdgamf9SySXg402tVJvGSjhWq46ScCJ8LLtF1UowA4xMh6Efg4XXXUlNqlWIOwL873puS8pr81qQbcTUSN2yfJNyJDn1YKeGR-nQXVhZLDntXlZbMH0VdaJUcHbc8iJIEuV0RBHsrdpFNyQ-GknuckVEQKffGjFMwo2hBh9xeu2-kMqW84uU_BcVAI3faN5MpXkhsCAkJYIjPk5yaEU0j93-NF8yqLMUm2y4CPix1mdehyymwJqoofrdQf7taxVEgsVJQKPMYLBS_ZTMM20h0F_NNIHPH3w5tB--Y3lLIAAYLHsCn9vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=pJDE1_8B1c0plxzZOXiYGCVPhrw_gd45jxPdgamf9SySXg402tVJvGSjhWq46ScCJ8LLtF1UowA4xMh6Efg4XXXUlNqlWIOwL873puS8pr81qQbcTUSN2yfJNyJDn1YKeGR-nQXVhZLDntXlZbMH0VdaJUcHbc8iJIEuV0RBHsrdpFNyQ-GknuckVEQKffGjFMwo2hBh9xeu2-kMqW84uU_BcVAI3faN5MpXkhsCAkJYIjPk5yaEU0j93-NF8yqLMUm2y4CPix1mdehyymwJqoofrdQf7taxVEgsVJQKPMYLBS_ZTMM20h0F_NNIHPH3w5tB--Y3lLIAAYLHsCn9vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

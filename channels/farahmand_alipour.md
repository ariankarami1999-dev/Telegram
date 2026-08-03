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
<img src="https://cdn4.telesco.pe/file/SES8NjRJR1AAGWRoj30pF7867y7pcPsp0VY-EoBWzTZ60yy85BLJk6RGteDAFem2QP-Y80I3M8Evs_eFsBn2uvpRGBdKpklxWkYV4S8zvRRfVyWX5raq1MMbKZaJyD5McCNdLBc3EbU0PYijm135FY00HKMhtYd4mOMCeITR8y9mYTsT6jKkbqPVkJtKMZdHwZFVgYQU6Y1ECjg0ZkF4InRpUN5AuvHOig0TQxg87-V7QLPa6ln7uzCu0L6oQf1poUrRHXWHTNRDYKqrq7QAH_CZ1HYLEkRPJcndMOrhVFgq73RlTNftIaE65cqR5DAZ5epjzMYKhL_yo1teIxhUQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 11:56:10</div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EifKuCTpulCT_OFZUREqD3ESfwlMzcXjU6VZy4p0oPHFb9pUSQ8Al2ieOxiT7EUr7emJ0u0_VsspBkcDTR5uGCk0ppGBrbsXGxEMG23-HtMAHVh5L_WsiTLzy-5wRT6lVvUFjudduAaef9kGeAxoXqHF02XnlKgXTsCKdXK_DXCm0QukG7Qwx7FtPr-c-YT18gHmOZvJWOfdHUJBA3xvW4rBC3UhBKeJjBVE6B-xccGUwCqlLm-lYmNE_GmtWqae5ogqbzVsTJ-8YiIzXU_fOTbJOqkYjs8CRUpDMNI-9Uawlwj6FV81ZloTVxm6v7C2frbJjSaaqjfmgH0x3j2SdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vf2ze1vR_vgLrIsaAeU6BGjbceIx_2osoh4kYx9PNzeEXniSEY5a7oBsrCBNFGJG1V1X4JogfSdrv8aNiOz3Knku-3ty8C4f9xgCH9W2LHGJwTbOFMIDUn7IhjATJCE3ZYNjsG6Dkdt_VFI_dxCRRAqLn2zv_pgfw1gCkI6gynmrg9IATZ2hTQOaKWNmgKFfvsIMav8JhsA5oQo--PzFG6hGp27zPgldHYHL_HswS3ZRWtUx8p0BFvBmf7RlXt0n39GMjmsNx44nefVzMhgxP06L7jkvJxqFLNLpUIinGl94egTYFwd-QH7IFVjTaZRjuOlyDKlEnHfEq196zokKIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZHG79sJfk1HrKHU4l7ii6713U9t5HhqYmsyezxN74VrrS_0Wfk4AODeESUxvBlXCAxfdgL34C6m48QO1y8W4MOTUwuyugrHXriYc8mgORpq_NwTqLW0fc0wlHSTlSyT9cd_hDht5CUQuksOQP8yUtTbPHtHjlDH0zrdXqthLAG3wuEJV9-AiQdkh4Y-fwqYrAS_0TRX8WJubKM96rkSVYskRn_-U-1F13hbS_ydJv57JuvA7goB6HpEdK5i6viK9W4Y38GlpNYX7kBmYP_igM4O5f_GMjAnjF7Mu-A38A8eoDGkCreDvYqtTrxVterCxt3IscOX9ERQlQaa5L7ovQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SRenryfa2oG2KZlxHJuw8UXZjm_Nj9EMBcaWqm2TXhMJ_MqgyMofWueYuIbi5LIHFxz3HNzUObmJBK-5b_wPZ11Ldr1CTOGEddN2avyvsGr2WbhYmDKP3WTpvQJ-97BDr0g8RE1BJTMkXLdaUBVj3MegXmV4drogOFR40s45S2AdsF2OmflcWFhE2xxkzpLX7nxiKQPYCcrOso1geNWq4jMXH6NF7HadDV-c0qVUpG2jm58eHAC99kfujr4cchoTdjwTBCeoQG7_HUMkqi-cCybASQXzcsEHxL79GyPWbD5kTa1xhcoB-h8MfR2sp2vEILfi6jd_I62tOlwEgA1e7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUt-cL8RVIYSXGymqenW4r4nRgsCxoGW-79_wktf6DfSRe5Lxm2TS1P2XTnwDVtUU9JZSJttsqEeydmviaa_6V7wUUVL8oNwNCI3CMsydnNdFMmrR1lE6AZ5cWXCN4EgxdkbA25bfstfUAAM6fmb7y9xSb5_0BsJdsza7VoqgWnHlXHxXStjKVrepZzcswLIVtZupfhl-NlAxz0nEt5kMT761-SxMSwwCBUQZLBOrWcs09vrR5rfZd4OQ7FP4_TZ0MqsqVAG0kXRhnLMLi6t8ndI25GTcSq8CWj4BtF7qU5JBXA5L9rX-fcnEVCkPM8y5-6fHkUXQhU0hYUrh9TYZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Df1C1__G8fN99ec4J187IBtQKmX6CK_xNVDSNa8JXuHMCZKpWEBiWPcKgl4-OnYTs2o8jLYs9j9pwqnFnfohl0CnAHq1q-5we_Kphb3tvMU7R4282dG870pHJcrnu3LFQvZf5SYlWrOg8M4C6dzXZCopGpa5NUsmWhk9sdQ7na9XBWrp3uZ8y-CPSayqyRjFJ5m3qfVmZerXtLxPtAq6Tq478AfkzfFUZX6fHGNipgWDQ3ETWRlm9NORAQL9MD-gwVMVfZk2G-KZimfZe3glUFXfKKseH-2q_XBpVQRfQAOQ0dLGVJifDmH8aGdeQ2e5wLNbZ1rYvkkXdqYSMdBoog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDqbOYiJYXCh8Yae38LV3ZmE0EyBLt5cM9ii2SARa5TpampEXW3iXGsadIrY7JCcTNPPDaY95X2EICgZummecTXQQ_7YvDQKsLGogT2mZYLpPeg4Jx0K1PK3XClORSk-cqktJEbuKDT3lx7wCe4hke4ctdNmLoJD6PDv6Oog-RE6Medww2LJlunJxlWDoy7A6mM4VkAcbmuozPV_MzJkewOLrdg1930w-ptaByqU92-EtBHLdRrCpZUCrH0lswdodZklta1xgmv27BKqgHISaLmJpNghtGUJ47dVtozuSPM-7SLnQmqWzFYnrjDxwys3STTo7JSSmL0zvjLZM8TV_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LR80kl-ehPDj7T_Z_P3rCPuxYS5Lt40K4u-zSO4b_6s616jiYU4lrzGpIgI--_QHuCGUudwvzXMIAJL8xnEXr00GghyUJIshpv592u369HfiEV6M_ZczqWex_5dVOCG9yEyJQmtsQTKAZOGNxVek5vYO94ONJrR7MQhGAypu8YhSn5J7YAal2bs8rZAFz2EoPwBZ-mft4QqkxOTDgEsG3hKjEOs0ByjJk2tplvU9vR9CHVxiTns4J9Ycmn76FSHzFovEw5bn1fViIv1-MTjDLZfluRUt7-CVrey-FequiskSg1oXFCwT-VfsHMbJ1-BT_ERP0E7Quda4TVdxp3b88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xta_htQ33m12TeqtZXOM07H964tNvvfGQ0KAT_J0Tv0pxtjTLbegR78EBQbdU41qSRdTiwjcjTRF3tn41FYgGPnH6RyBUArktoL6NS4tgnHzoMxr2iCKv-SpMPLrda7JKcrmzbskSzckvUD-hTFyBLqrZ4xiezKmd3kUvDspxKObrCh0Izchc8LN1F8tuXH5-ydO0hDfUk7mUG_ovsyzjSshzSxdCpWcwCvpOnPRWMxj5eBbywCmrKcUIFyY5F930auXBruep4pqDQHWKyf_7vICRklvc-RRDphTC7nHzGEkDhMEt5yjSen3CLe9uZZisRK7NmVKPth2FJA7qqDqPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e18V3Bg-Uy-bo9ikhRI0ztV_Z2nDVyHXyMnW9nG6K0TxMznHD0rcUCZKC8bpW91Wi7oUyLfbE4b7zZzvjQ1CBgGdhjWfeqPDznc5DxCHNy7wC_TvNVSbzahUQhl0RqLJiIn8ijtw2v2X7YxwWwHc2abfIGvwqxd51n3CsFGqO6znkVEkSQgkry0GMCPli_rSy4PBCdSjCwluqoWE8gUA2xoaQx43eMagC36ef0x2bL45tycuf06HG6581-ZHGiFjpxgDuFgeBeE_Azeb9lQLoaHlykgHNtYlZJgjVmD0Qag3-ZYkTtnzC6cYoEsnQKYn7X7FzkvPg-g44o5Ir-1t6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYed9fUA93dhYdfNmttVcm-2lUMw13RTbLImI-z9mIYAp3Fn2k2kwxWO1ig3HF9kt__Qd30l4m1S2SDDhtjk5O0OQsidkXQ07ucDS_PfMsyPqIF9ZhT1o8M2Cxsd_EbJQdDbi9aBA4SfwyLGuP6nOffLvRWw7t8OIr385KWwqDP63fknUcx9lGhmSwZ20KPLmq_5e37EHVefD9YRhdJu6ixoSXKTToGezCK0UiQndY6nkAU_-eRTxFwse4feS584QcekMbB0tAYzlBdDkGKmgpvLIimfjExjasGpdPQADAzfOTbty7ziR-RNmt2mTKBDmtYnfK69_5xd6506jVO7-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qp-uWfFXcnmLv-0yLX9U0HSaaUUxpVEYsNA35IzA3RZ-mM09Z8qB8OWIInZRV5Fe5j1ZjlLlWA0DazcSD2o0xu8nMZ3ylh3dgmLYJw4cWa_sQc0zyzCin0Qbvx1roTzR6johL1kwCcTY9qRTifFt9OubskB7kzNkKy_yiCe2wjUf4Rim-bMz2KZahHQ25ckWSh3Nebd1taY4UxIihZQn7f69pMlL-EJplk5JVhn2Yw4agFirJiH4DSJsR70EE6oEzkzw_d9MyyExhc_W7tCeH3FiKLjiprPnDrY5dfw_ZNe1cvNuh7Bq8f0xN8kOgk6fnqMRLOmKSOo82voIFrZTHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjUcCmckFhian4fxZ1CPt_X04Yk4G8LvzCk76rPDE6hZ-lP3sq3DRxi0vaxhA4hl8M9pNUa3QUNtth4SqRQZqUIcLA74UnsK_BPTS6Bgf7GNfkE5jfk1PNSoy0Z-Nal6KoKmZzYgnrEcipTB5LCSysETkY2UCmtC9W_frZ5AJU0WJUbf8SwLP3_WtodCIrf5oxk6gnE5v71AFZdHvikJAyCVbnur0zKhhuZcRbMvD7lj0cBlxQbcUSRVRelz6dp9KuB31v_i6bCWRUBIL4QRyPXcyCyFwRlkaDQCAZxiOHi68xsZNv_V0yoVkKiRfa_AR3IN29c3dY7Mmhjk_EPy-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqO-Ys6gM-aP5jJ39DyrDfIOz_WvT__lYsUOOfNVDjCafVBWPxNBVKEcinUVULN8b0pPCRt8ObUDfCnBnApslp8GWPTmLU4q5AwZNkPAn9pJAHRUVQE-RNB6fUBQoZO5eYPT9vnzINL10TcNQIrBTurHdh4GJ1TLHpLIdABKD67WzlHsNnOxWFDgsIXgdapNtfS0QmF9BkqvTdf2sFtv-SzHHjczl54HLu6holMnn2xgi70kgeuwf1CFHDXGwe2EfUoczZ3PSKeGT6mgOvrX222s9ejiWoOQOBICNMJHy-CIi6lDEIAFb7uPtRfkgi7GyGELP1yO-6_1j22DKY-AfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-73ak1rf6cE9XU2Rxhe6foWf9IfvhvYyNTPdLsO9GOK9kawPzMSjU_DFHy0VFhlgymYTNNmxBHntyZlwzsajr-Kg06xHTCT0QqjT8ExMFPAnidUQhKpv06U2A7Wy3n4x3kE-HuZdQL4PrJS0qwWiYByuQomvNaN70SIrcGxZTgFeni563eQvllKobegXUvtTVq6_DZR2EDXYyEA8w7CN2V30H5BAdEcemNhCxoDBDStYo-_oWecl7lhL0X56KOlsJ5PcJ8Gh8NB0Kp-D6B24PgoLabisOx7ZsuzpMPKTqMab52Ckthnv-0wOAE0RGSkmX7MzrmXkpm2eLgIvldjNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxkK-CCasKkcoXE3RB0h7RQziXoIRJS9dMQwVSiwRkhRzLNJBdDWy_iTjLyyKTEpMY9h37fq3pCkwgdsiIfNDujvtLl2AyaP9b9WrnggLfQHiDTbPjbffbt9w-qNrEMcl0CwMl4vWZx1Lec29zbFRV89ceT3p-z27PFOGZRkRtHvjAHRYo4GyfK0vDbnW_PaliowM6toxl5KqumREeY3amn-R9oEZk0CYrcdd2NZpGt-VOpnTuwWxvWLHAK5gvpWoCEYsuxjtZYQj7vUEQyvtC9Je_AzJOMzX5W7SvV8zQDs4XUuPHF9OevueXyClLwz8O_FqHirtMzvFSrluhoiyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/an4bQwbH9DK9tyWUdlI-W8eG5Pk02g3DCB6DR1P5YqbwmbjVIggYb4A1n7pIIx1lv7UBeKelYAja6WEJmctJVwJA9Mphq1CAFp5VnxTfMj0N8ySY_H1ah4Z4Ijb8vkZi34NA1EYDS5qc_xj0eoaCwPYgwyI391dctoQ1f_cE2V_MxCyoGTDEJONqMoygnHzokmJ7dpiasCgP8c8Wh0qQXzqmV7JQVclttTtMbbTDbfVmvXGDH2JPQbGoy1dRkyh_okIA9ZFmqNRssxIK0vJMH4KN7-2VHTv6qdhuEpXrjnVTq-A4NN03-4m7vPtXRnXUtNi0QNElOMWkZxleookR7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDVpzzvjVCLMyacbCMHI2m9ao-dKDXy6RwEqfmpdJvcSI_lPFQ3c1JgRKa_pAFhS3TcyLviGFSd6CsgCyFoOjQnpfgnsEaic5Gh0zW57AfRZx84fJTwgio6SyxEP3pkiNPvm0__6xObxKtrr_Au8nwwlX-AqIdv3GXD3Ch38XJkYA6pcx9SNp5jWSM73XdW6chYBS8i3sg408fxbL2YvfGGcT7LhFCrwAxRoqoTyDhEArawIsWqZopb2b-TEmcbnwDYUfxzIqLVVWI6EXY2NaoGMiCTYN79qi5_axbU9KpVUCOa-R_4-lm37xI5nOkeJOblUNfrwT3XD5ox9u9_ZcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=f-2vbsxokxga5ciV1rvafSAf06Jr8_C9yHcakTviDSD5Pms9pODbBl4T-UDwrvwa7RA89-LUueKQygoZ7XIz0iSeHGPNFafiMcNaA86al48ttRvBo7MjQgY5FsfD-RV_Nq_YNLcAqgsN3FU32_Go5YNIwVEiC9s68saPvKeVJmnub_q_yALw5pcDqQhpgP-M10ekQIKmE1BoUdckHs0-QIWRZG6DxJzD2cA85PnowVVNljWTh-E77XarpWFpVu5htpwoYgHY-KQLM0qLT9MGaD5XKolXNBiyRRo1EhRy-qS0HgRsrGFH2jJtPK97OUBqzSneD3vN7GROOoQBqlL9og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=f-2vbsxokxga5ciV1rvafSAf06Jr8_C9yHcakTviDSD5Pms9pODbBl4T-UDwrvwa7RA89-LUueKQygoZ7XIz0iSeHGPNFafiMcNaA86al48ttRvBo7MjQgY5FsfD-RV_Nq_YNLcAqgsN3FU32_Go5YNIwVEiC9s68saPvKeVJmnub_q_yALw5pcDqQhpgP-M10ekQIKmE1BoUdckHs0-QIWRZG6DxJzD2cA85PnowVVNljWTh-E77XarpWFpVu5htpwoYgHY-KQLM0qLT9MGaD5XKolXNBiyRRo1EhRy-qS0HgRsrGFH2jJtPK97OUBqzSneD3vN7GROOoQBqlL9og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBn5hjLbiEi23BGIMt2xMZ_nfH4E77Ri0qIgP-CaXIakKNh-d3MGdIk5A5_bSQ9nGjZ2H21NIoE_8vML6Uja4qeTQG0VWkgr98k5Z0uWhs8iPSqwLlZKR9Jf4AbqC3KJ2xUZapJ8lQrYZWUS7jCAm5wlpk9sYV-2OHkXsyYP6j3Z3sl4eU8ezLncAxVzw0y-mbJ9MX3PV-h5ipHawfoBm245X-9kUGjgfmkwImAlzuUZtoABlmH2wQaAJCfZKhjPahAIwUsr-69Iwv6mQj7iidoEB-isUFuZpv5EHEFh98al_TwlvOY7ktHgkV7lMTY0j7vKqep22VZe35cyrJM_Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4NEcaPiVSWHpYBNb2JFjUOnBwzQ-zkoUHmwhCbPlKCgz5ClPm4bj-vDw3SIdRC_LG4hziuJAv-BPjzEM6ozWrS3c1jQqHDZOd8XdD5WqdsxCUjoXOLasa5nFW6JKHxVj_rZk2gGOuV0Cpv5rEBUfIPKmBn5HgA62ttzs7YgQLgmo1HTHAvfwda0n8nXzZiM0vbhtLtYYY3lG6cGRDjuJ9-T4IXYommSN6GrBmxFqwpMBqqpsVhC09GEnB4GT9w4GkEYT8c5OXw8oGsHuYfyD50vdLGaL_11Cqq7SXVCp7pEUdRAe8qtBmpJPU07KDKvvVP1zx-na3g8U4l5PY_u7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Be3cpTqWGYzvikbvguIaNwDHOdmp1MECqKlg8cyZpYzpVnsUASWVMJoHUMtIQWD1Pf_EM6re5nmYjVYUyLavveSkY-7toIL2ks_qhDzK3g32l2hHSUou-j9Qh6jn2D7yvaECrVXVcDGSbXIMCn-RvPLGrW2rCbO1RHI3ebTvA67YY0FSyZRLGP5im_tKxV1I7Sw0acdOD9iSv3TE56Km_nZSbrUYMBakGce_6Hy4d2IgiLSxEUyAbljy1NtOaOBZOh3aM4kQtnjgq4K9Ya20EEy41t2jjno7d3Mjaw5HYEi2-x24Z4H63MOMM8RtDqN1iW7zEnm6NMAbSUAfEs9umg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVjeJYtqErrHXaFCPqEf6FMTIvmkfRi4UuJcAm89VIYgNzXgBbycfDJe90rhtuycn5YIx7mY0pUq0lNhzAO1SzOGFEfInu0qXmm-2kekhfTOAIWURvIsUR7Rmh4TgBo4zYNZ4DzEV_FL8kRQuSFXN1TuTBNSGgdyvtOaDdZ_2oMW_F--baxuAHPZTAwtcjA8fiQcdBHkQP3rBRYvtb7K9t1ftJA1kMJmPzpvS0kFlw5p2p_Exh2DHI-dA71T-6eShK2yULZ08s9nH4zLU56_GwcbDejAeKxNCjCJbV9SoHD09HQIe06pcViXqHr1s4S92y_As7WsFuoyNtcgzrxqWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDr3pzWLw-6ss0Ti6uOdLaDKNGNaJ-kNf4H_P_XsgLKeRwBK8p25PB-6eKpAWQ6GSUtfnlu0WBhJ_TrR9PJCnjM3xQPM1KKnlr9qdeE1oD1OhOoKLWx2ojkLQtDdMs2Sbrig0PU28nk_NgzesTFf2FYzKj7PBW90n47vSFoM4a3czgiLHy2iEJzlkStU69RFIw9HJUPRBWhOMdIv9j-ERayM846nTdnmwSvI1WGUgWOCDQl6Dcxc9QV1pBdYymyol-OQjWRI7QTYYHqFCDooarSuEP-L89kZPte8ZejcBTjdV1LQoiAqSea5NXcpWrfuGOMapDlpjpQNXOSfDXqeNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEEXibjOJQ-BVtisjPQBn_oFUrVJiHj0agWkaYIM46a7Q20CxpC2sVogUmudLYPWrinYONi0v1jU2Fpb8QyyS0lmCuqc-eTJdYuzSiZBMQrk3JWTtmzJyBRgDUsTWCMedG51O097QIN_ZsGTUL7ZAwaqOtkK4n9d2rXgz29hp1Gw6ohzQqzMIlmDHLxsW3fEH-QuEqI58OyBxI4k_Ffn2hYx6Oa4zAEq1kFXhRFksDrfxdlF8JHjx9X-APUnRf84tugVGdus74Ntn__2Ii0GMLURM4LourqD0PA2tvvQB7LhD5tysIr88W4Z7zGj8AZN-QTbhV6Vjb0HLiOaSaNY3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYMr0WmSen2oYYkvV2qtYGOtureW12BeyOSWZTaZpuQDOvvpc_wwYSYYeogN79ZlDXFGIBNsxYONphpDnRAumfPgkNbCHC08ZDeqCYfad28R0RGfPrlIfdFEezEWcgp-xO83mRbwH-h1CFL77eJ9YFViOl5Mkd6ZoDI0KjKH3baRr2BV73RjVgc3uShqVZ4sqbbaVTntgTAOEk92KII6gMJbr5sUU9CjHDigvFPKEB1hRsfHxAO0i4xJuI2b5HbKKSq3mJPs3-dD-chjhBPLmGp_iFhj196PsPDrg0ugJsx5xuP2hoBHm0n5dDjEJGFiq3j1mrHb2ysC4f0v4ijTiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=HENlsCa8Lo_Bmg1x4aY_Ubd7hDav5zXcY1KiP4ovbyD37h8rXhpmhM5LD4xEbzmQxOz1LY2a0ml8vMDWzmOGbzEs0EbGYF4KAFINWMSWlXi65t89XLBpBiUudTIRJ4cjbd5ptpprNiApRVP2a_0ANyyfiiMGMes_jdIYF-qXhWOcssp-3ZkD8JIIDcRuee9MjdrbBpyRKS2tbLKwKzLcAu1BU9udpDFJ5hncYSDi3wl3-gw-Qpza-PKCnCLQAuWkJ4oHwMcdB8D_CV-ifXuL9ngGYQ9VjhjatGzW9ANLtpSIv9rrYUWoXbOC0JNNnNjFaET9Gh2HC8GQsTTijKxCey784bQ8nVBTMknTzLJrhwuPeMdxyOYggEP1PFfI5KOAZ5AF5x77T2tw67BW2k_JuOhoz1EM05sRtCYmjM3z-oyyOE_LY4ohSWxWvcglGPSxOG0-Wzdm7YHMPrVEaGHTO2eRHKsUSQXcF0NeFPCDcEYxtNoG_dodn7EO7c0g5fk396As6dge8ATDIEHiH7hezO3vA46MhtJknAVEf3Yen4ZDlBpyFV5ZF2zM1x09mFH4z1bqxt-rXUuNHS5fiHtFUjBvkZOG52w1uLQurYE4SWdX8D7PknIKvz4V8IkbWnS_iDT_fVLhB7Zern82VdTi2T4lOZXCkEaoolhc9oerKOc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=HENlsCa8Lo_Bmg1x4aY_Ubd7hDav5zXcY1KiP4ovbyD37h8rXhpmhM5LD4xEbzmQxOz1LY2a0ml8vMDWzmOGbzEs0EbGYF4KAFINWMSWlXi65t89XLBpBiUudTIRJ4cjbd5ptpprNiApRVP2a_0ANyyfiiMGMes_jdIYF-qXhWOcssp-3ZkD8JIIDcRuee9MjdrbBpyRKS2tbLKwKzLcAu1BU9udpDFJ5hncYSDi3wl3-gw-Qpza-PKCnCLQAuWkJ4oHwMcdB8D_CV-ifXuL9ngGYQ9VjhjatGzW9ANLtpSIv9rrYUWoXbOC0JNNnNjFaET9Gh2HC8GQsTTijKxCey784bQ8nVBTMknTzLJrhwuPeMdxyOYggEP1PFfI5KOAZ5AF5x77T2tw67BW2k_JuOhoz1EM05sRtCYmjM3z-oyyOE_LY4ohSWxWvcglGPSxOG0-Wzdm7YHMPrVEaGHTO2eRHKsUSQXcF0NeFPCDcEYxtNoG_dodn7EO7c0g5fk396As6dge8ATDIEHiH7hezO3vA46MhtJknAVEf3Yen4ZDlBpyFV5ZF2zM1x09mFH4z1bqxt-rXUuNHS5fiHtFUjBvkZOG52w1uLQurYE4SWdX8D7PknIKvz4V8IkbWnS_iDT_fVLhB7Zern82VdTi2T4lOZXCkEaoolhc9oerKOc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=fYc7nw4ZB3xCB4rvmTy6oQQCKOhxp6ItO-19Ge2-a3Ojc1xmuzd56m8dBJ2h-WJjRB22_I7E1sIV-VYxvwVvVY2JA5TIqSwMlzmucikAjdIW3UQY1QocExg0LiqA-gFrbgxyH-w2UMCgsoOhO3cnj0FoxMYxITGFd2aj-cgIj2Ec9Hxts8cFIEm8zbLg8NhSm53ceqJ_g0K1T6OsFSH7x1BROdzFmhV_kUAfT9OpDXo0dh5ShKGrkMCCm52eoJCcG4wbWkAat3b9_3Y7I7wAcEJkQbbRbeUBYJ9_4KGlV2rj4dmHuPcvQuzpRL30TZl8Ks-F0nZhlAkJUeQGN0pltA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=fYc7nw4ZB3xCB4rvmTy6oQQCKOhxp6ItO-19Ge2-a3Ojc1xmuzd56m8dBJ2h-WJjRB22_I7E1sIV-VYxvwVvVY2JA5TIqSwMlzmucikAjdIW3UQY1QocExg0LiqA-gFrbgxyH-w2UMCgsoOhO3cnj0FoxMYxITGFd2aj-cgIj2Ec9Hxts8cFIEm8zbLg8NhSm53ceqJ_g0K1T6OsFSH7x1BROdzFmhV_kUAfT9OpDXo0dh5ShKGrkMCCm52eoJCcG4wbWkAat3b9_3Y7I7wAcEJkQbbRbeUBYJ9_4KGlV2rj4dmHuPcvQuzpRL30TZl8Ks-F0nZhlAkJUeQGN0pltA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCNKbDkGezD25eQK0bVWnkv5_UbC4N90eUKTP9PmcvnOQA2J2AevpYpVaNRWZU4FhG1z4hH5TsaeoQqGD3-OBzw8FujQnJ7R_GfM3BIp4Vtj0rXGLZSLtt3ldG7yNcQ9e4uwwKka59b5hy7meLohMvNnzMIWCd9mXDYg3FyVLomsqTk5tac7My-WMdBGMtZaF7PXPaGqKIfMWFYPswx2NNZXj7gTZg_kJ1nwxzHbeaKRuP2kC1kYdLhDGMWhs-WMTJynG8_bYc1MqHVtlreHN9sx3kUUqds5NYm5esVrpH7558DGh4G1muNTB24NIaBft9Tbf4wtzzl5XsutNiiVrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoKmvAegS6XsSPVxfdJkJlIjNAPUYGJcxW5JrRLnbvk17P136tMQnQm6Mho9Q9tS2jbRD70pJ2Ra5dczgzeIUApJRv93orm2DEaQLmH5mPcw0b97ZB7j1ALhF-GoPcCrRXhSHnjSlqqVGBdnlDMBwV5D_PLkV9LgXJIMvOvFT-r6MKUhvPKIA2nRrFp4tlOsvkjzB6FCnWx3HoDU5EQUs0NdGcqT-TrHEV2gyVrznCxRiEhAW0iApuG-SV0weJj19IlaA3dqBV1ZlPxMP6BDlo0TZfqzHf2VKlIPbT1S-KuQHXkL40I4cohsCNvm5FfH9JEMlr0RQZxj9EJX_zVAOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=ZMp9vYmUmx0ngBcohJnjbR4eU5urq8IpngRMv3TygR4Z4lR6pr6uBmJZfnP6oqhcSvd8kKEY9qtxjlEYGYrhu4hC5DR5I5rvTpYMXadx30tgKv-sVg3s-mgSSQhLBKErFDRMfKKD4juhkFsoLUrL_mUgs6tmhBX0ISPO4haK0yGFYxZZk1UqJDdMsaIWKbOKgT1DAOaXDhn_W-sjt46H_WBzbN5LKLLNkpHwugIpRXK_sw_kdkQIAvls-X3xkqCNb1LjZ65UVtZDZm67-4KhQIO_DYoINe7yVIzz-ej6Bf_Y5pP5TxYVpsLNPjiUZnj5KFrB5hQOIDhDqGO1ZQG_fTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=ZMp9vYmUmx0ngBcohJnjbR4eU5urq8IpngRMv3TygR4Z4lR6pr6uBmJZfnP6oqhcSvd8kKEY9qtxjlEYGYrhu4hC5DR5I5rvTpYMXadx30tgKv-sVg3s-mgSSQhLBKErFDRMfKKD4juhkFsoLUrL_mUgs6tmhBX0ISPO4haK0yGFYxZZk1UqJDdMsaIWKbOKgT1DAOaXDhn_W-sjt46H_WBzbN5LKLLNkpHwugIpRXK_sw_kdkQIAvls-X3xkqCNb1LjZ65UVtZDZm67-4KhQIO_DYoINe7yVIzz-ej6Bf_Y5pP5TxYVpsLNPjiUZnj5KFrB5hQOIDhDqGO1ZQG_fTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZM_Lj5Jo78u2Ft0D44IqK2SvpXVm2zG_wojay3XacOtJ5NUk4XEyAglXqS2sZRlRqQIPh-KnLo_0P1vYMY4ewUEf12U8kjC7V4dcq97WMnEllUJWrAJEsw5j_BJo-QsABC0NPGnhxU5J9xOnHZ4nqF6mshZtTRj6NGzpJQ42zfKBcRySvrMphtLu9ai0p5KgLBsKliMpFklpqpMFdesc9g_U9JO7EcCRLqTDcCIR_PQ_eZ-yQNx_HH4KuvTW7TEZyTEofh0-EUICfZwqfRtG4fWKAPeAmhAmEhl6Y-gn6HwTYB_h2Q5bJkOGvRMFcSf34kJz79iZtb-w0T9oPAmZlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhvjNkG0TvYxf39ohelG8TnvmZNh30_2FOsIlVawk7FTTpESzC72jBpJoYS7nJLCcZ9UTY7lmzRYc3XwvkYUg5H2xrwdXDuupFKkngCZK3gFA5-p0E3AiR9CzMfPO-7dD1HHPA4qGVyifbdPQz-F8cwbjI9zN6TNiz1PNFpKYlm_3IOazlIFCdOo4VlClU_bGBF9Lty0-prthw0h___w0l4O9Rsl9sh7GP1giz0oqx353zTZBHe-otdsOKqoCmsogk6JXIzc0jcEmHiRYZDFRTNcfQp_OS0kBa-i95l2avAle1UoKvNV_0MLfrg9Pf0RnR6iLIlnXso1qXszBfWwRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTgn0KXWky9upL303FrSZ0cy6eXfEEpZxMbpaHGpoiWWPky84lTYUatc_GJ3CG6-go6wubf8dYifKAFxR-fCRELyrxTEeO1qrjrJspKqDMdxKRmPhCBlWqXs5ogVIWvVZqEXUPb4wEhZR__9mDGlc-eyz7xCvVvNYbCbx3PR9vf9zrXSS_bxaSwerGKdHPwfaWdzmd-kt10Tnr1IXKJTpaxLyYxwIjKR9Mo-H_Lh3ym-v8Pmv4zZEm18Pg42WWlkYp_UENobxtSyWSARzfj0-WIN1j60pPhmaLwvICTff4fDZOmOVlAdmyTgMBkgUtQ3XnxG7KyEMiTn0kot20b1Ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UN4xYmIbd72XO879S-HrcCBJdnPSovAjlMyU3cucbQ1_DfyJy7wH6i6EJTnztqB8yw1mFmPlf6hxAoZWOOL1BAu0qyY7EZTi2oqkUbBXtErpDbXg7-JEmaiblaARkZ71wDwafyt-iDNI-55urvTv9ctFsWCMdJn6iCL_fAIDFcH79ZNqaD-NhCyPiwpxOQTkTSTHdS3dkStqTi-ioiVNAYR3jKO6WR8I5RGJ_u0Mb6iC1gicfhYVZvOE9nZ1HxxDAIZWhEnD-ZmkiArG5L1aaLVzfKWx13L_ZUvtu_PixKHieofWoyPtYsTn4LlA0dy3lzbk6TCYaIUK-hPHliJsgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjfYx634gV_WvWX90Dae4KB5juArqzhsPnpm2f6LTUPPV5SEZkh9l_nttd7cOLdg4ixeVaNNDe6rXA4Itl7J2f6dKArQOhHzQlpwg_H6yo2xbv5jX_mxmu45M5QK-ZnYVx3AR6hHceqXK01oS0jv9Z7P_SEpFcetiZ4zzXNqQ6TbNafsYbPuUQRasHaVS5J17-LXSa2Q9DeUAqtZZPV1g15NukTO9dLameo1JjMM0RFkZr-T_tUzNEXp1cAFvptKuSUQrIRu8VLx-DdhUDVIJS1RwixjAcrD5zpQ9XHrqs72L7HyEwfzUwockM2r0qxD3OHKSkUXgXkbKnGJ5_Jc3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJQPgtDhP0LPXT1brpXNwyHkxktIniMtHpP5YcqlFxmo7MJlCTpJE50-sj7uK3gQk7wTvw6GDSe1h50Qth33AyErfH5rzIywZlmgL36oZ1jMkPZc-U2alvfXFkhs9TElUYiiWpGmFU7kyhjfq7QlDucyfQeMHNVqfN9CoSDqry-QR3js7GG4Mw4GiQbWl9s7K2V56tJ6cMHNB6w_VxMOlBEGmEW11Vq145BVyZRKJ-cJWGVgKKX9sl-7tUw2rT3cH7bc0FCNKfVOgiHC8iheGbyPF-cAtKCW5oGMxcCQIZekrWXsAlnyoy2DY6Bsg4WmNCqZ9B_Z0hx9FFf7ZRKUdkvI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJQPgtDhP0LPXT1brpXNwyHkxktIniMtHpP5YcqlFxmo7MJlCTpJE50-sj7uK3gQk7wTvw6GDSe1h50Qth33AyErfH5rzIywZlmgL36oZ1jMkPZc-U2alvfXFkhs9TElUYiiWpGmFU7kyhjfq7QlDucyfQeMHNVqfN9CoSDqry-QR3js7GG4Mw4GiQbWl9s7K2V56tJ6cMHNB6w_VxMOlBEGmEW11Vq145BVyZRKJ-cJWGVgKKX9sl-7tUw2rT3cH7bc0FCNKfVOgiHC8iheGbyPF-cAtKCW5oGMxcCQIZekrWXsAlnyoy2DY6Bsg4WmNCqZ9B_Z0hx9FFf7ZRKUdkvI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnCrOjYOk9uCvh0eKi2-YG97DWfOVkyV5VQom9ioSslOm1gDc4gZUdy4yqRblCfrPaTKf7GRP-RsK_9poI8d0UeWQdTWnh0do1GWs23l80NYMa-pLHGRGmUd1Zomf01QzKDSadMzMaNqmzNPSAZtlJB2GjNi6Hgt3SjZ1e5nUiJz-KJ5B9rToWoQ0_8Q0XuuxBA5qR4ZlOBrHf0behzuj2zeO4hBNM1MfYdhqSdUzUC-2UxVFIBMpfXZAV2RLrsdnWTKQt0FgUOFKN1gnLUSDhjpX2oly8SubcHfVYsGgmZoRTkENvucs6TErDi2euG5FoGWPZ8FDY3X8mw_-c20sreU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnCrOjYOk9uCvh0eKi2-YG97DWfOVkyV5VQom9ioSslOm1gDc4gZUdy4yqRblCfrPaTKf7GRP-RsK_9poI8d0UeWQdTWnh0do1GWs23l80NYMa-pLHGRGmUd1Zomf01QzKDSadMzMaNqmzNPSAZtlJB2GjNi6Hgt3SjZ1e5nUiJz-KJ5B9rToWoQ0_8Q0XuuxBA5qR4ZlOBrHf0behzuj2zeO4hBNM1MfYdhqSdUzUC-2UxVFIBMpfXZAV2RLrsdnWTKQt0FgUOFKN1gnLUSDhjpX2oly8SubcHfVYsGgmZoRTkENvucs6TErDi2euG5FoGWPZ8FDY3X8mw_-c20sreU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=lefgs1aYKrq5y8iBCX7qcPoi3P_Nr4lzDd3zkAO2XZ0CoyMhDwzJRGKqnMFWbGoASO6ZDq1aKoFrBRouMbK4xIIg04jXpWlDTpZayRmAqTZ799wiPOq-3spXqEizs8F7vaDsZAJzYFvSqeJkH7-RA0empqvD91VSZgQ0Ufr2Bush5M3zlocsjrRFFFPt-gjyLOnx8L9-_4_o38SZMhlDU5W63fLlRF62DnaTBiVRWTHLkKfX7xMISQ6DRp0oE5pdeCa2s9aeZM8ZjdW0GZFb33dipBODG4JEpnDZ1HrcfOjsImTfeIcBGsP3FMnlnRPYWhVwEvN4hgWAsDtZc29Euw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=lefgs1aYKrq5y8iBCX7qcPoi3P_Nr4lzDd3zkAO2XZ0CoyMhDwzJRGKqnMFWbGoASO6ZDq1aKoFrBRouMbK4xIIg04jXpWlDTpZayRmAqTZ799wiPOq-3spXqEizs8F7vaDsZAJzYFvSqeJkH7-RA0empqvD91VSZgQ0Ufr2Bush5M3zlocsjrRFFFPt-gjyLOnx8L9-_4_o38SZMhlDU5W63fLlRF62DnaTBiVRWTHLkKfX7xMISQ6DRp0oE5pdeCa2s9aeZM8ZjdW0GZFb33dipBODG4JEpnDZ1HrcfOjsImTfeIcBGsP3FMnlnRPYWhVwEvN4hgWAsDtZc29Euw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIAzXvVuEj2Hm_6TUnKzmx_TAnUQrhEt2JfzU2plaeKC4Ra5vhIyNum881u4DOUEjXUydz5l60gLHlnzutkf__e-qKKjlIFMLwk28yHnGRUoVey57deaE4XoH0Yg_eNad0LHqUF-DnF5pqzTmLCgPm9hZwrljuYhLvy_whoMq2VnCW18l9GmbS4CpTa00wiTyRslXo9wEHdmLBAX3dRm4Qx0BsOXSkqAXPUlWW8X4Ibh0h79I4-_B6N-OiEdEYcn-QCkAeM4aYGRAyjYYdYXyHa1hkuvSGdtdvDzwKgvi3q2RHTk334m-gC5XB6y5HKVVPiC6ftUajgNjTDDuIs8sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpwAqpp16x7f1CDVgnV3B-o_Pg5lzKFyXPBe_-NZ7pFQvXEUoOIvLHWBpiKp7Lhq1XF2sULse6bFGczDGU7n7iHgAwEvAICHSLd0MzIgdWResRIhTvhDpRfqBbAK0ezbYa8dExc4TBGuTryAt9mU2oTNHuiQM5B1WAwXDKPfQe28jF6n5kQkugDCudvhKlOPc8HlUMWvgcm1BXOpH7N7lpw79EJkD2IL696ZpKkdbb__fK41TPwhK54XeLACFNix87mEIU7AHY9RZHz4cpouN2iFiirpsHKrWZKcS3lVK2lQ-zd2uMyaaXSahqepGEbUXPESBcJUQmyhopIlUfEM6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=M0IkC75CmWa-Gva_CLy3k95vDkZJy31-3Gos11eXraVQw4c1zBv8i2pQX4kZusD-9h-XExOehwnl5rDT77GupEc5S95NFmowilE77Moz5GBxOYjiavmuUgrI8SIJf0AHNbQba_QBbgKj98agyTjqZP2C1SMeRw2z42tXHb6-eoW0DeP3OeLLcrkB0_BUP6DFE0vQLlVMQmTSV97Jyvb0k4wLRxZpHbGDGU_2pMvP7F-L1soH5RZUVxQGqEdYk9EmyqQ5esp3n2ff2pKC4axppjnzoSGmwHisYJAsBK9CuSDpRoF2LiwxHz___tV4sX5-v9nMqR1Hv2Tnd1DFbXVAdqnCr734eIFM6wMQ8EO_7E3JvUGzDjJc-keb8b2F1zI0mvdm-wekiWy9Mfgf_nCEjbd7t48po9cTuc8ZqRR_85mPID8B1GTk5-t0E5DgAgrAUff3KfT_8Or3DKho9S7YlJLu0hkB54NaNox2vN6yTS24FW4W8dnwUWmBYAqbpPkxLWid-jFib3PxvTTSN3IFnJ1YlwTQkcvSFCb3mj_PBPfHE4ZnJ_KBILnhMu70rpqH3vdI7Yr2bl3TE4JXLGuxxjkYJ-M3JsWH8WZjlnte2o3zK7zndnJAOoGWy5rA44ZTxR-u16JWX6T4DSdHcJt6zO0eVtZNs5IuSrA1miLU2gY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=M0IkC75CmWa-Gva_CLy3k95vDkZJy31-3Gos11eXraVQw4c1zBv8i2pQX4kZusD-9h-XExOehwnl5rDT77GupEc5S95NFmowilE77Moz5GBxOYjiavmuUgrI8SIJf0AHNbQba_QBbgKj98agyTjqZP2C1SMeRw2z42tXHb6-eoW0DeP3OeLLcrkB0_BUP6DFE0vQLlVMQmTSV97Jyvb0k4wLRxZpHbGDGU_2pMvP7F-L1soH5RZUVxQGqEdYk9EmyqQ5esp3n2ff2pKC4axppjnzoSGmwHisYJAsBK9CuSDpRoF2LiwxHz___tV4sX5-v9nMqR1Hv2Tnd1DFbXVAdqnCr734eIFM6wMQ8EO_7E3JvUGzDjJc-keb8b2F1zI0mvdm-wekiWy9Mfgf_nCEjbd7t48po9cTuc8ZqRR_85mPID8B1GTk5-t0E5DgAgrAUff3KfT_8Or3DKho9S7YlJLu0hkB54NaNox2vN6yTS24FW4W8dnwUWmBYAqbpPkxLWid-jFib3PxvTTSN3IFnJ1YlwTQkcvSFCb3mj_PBPfHE4ZnJ_KBILnhMu70rpqH3vdI7Yr2bl3TE4JXLGuxxjkYJ-M3JsWH8WZjlnte2o3zK7zndnJAOoGWy5rA44ZTxR-u16JWX6T4DSdHcJt6zO0eVtZNs5IuSrA1miLU2gY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=gi6hiKVLLkOXF5D--7cNnIWkM1nT8s7fIRh2Gi5qKoKTNteI9MewOaAeylJzXMlbbTPopPxvGD6B-HxCM_nLAWnzkUw0d_namk4Tk1ntxvHISv5wVF9jrPsmdURoylCcS3xCwpGxDIqoyU_8eTvOSmSUHgLuVujS46niJezLietLX_Dvlj6Ufnk_fU4wl-mrBes8Ll6_lvToDSItNpQ_rqVl05GnpCZjHXuLrx1XGNPGiGky02Vrkh_OveKmXyMsD6vXUgTq5j1BPwuzFdRm8nsHkWSRG_O-HPz1e5mbWIxYGJyMCtaN3SCPqeRoLiRRyUF-QAcXJd2KPgc9xXreBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=gi6hiKVLLkOXF5D--7cNnIWkM1nT8s7fIRh2Gi5qKoKTNteI9MewOaAeylJzXMlbbTPopPxvGD6B-HxCM_nLAWnzkUw0d_namk4Tk1ntxvHISv5wVF9jrPsmdURoylCcS3xCwpGxDIqoyU_8eTvOSmSUHgLuVujS46niJezLietLX_Dvlj6Ufnk_fU4wl-mrBes8Ll6_lvToDSItNpQ_rqVl05GnpCZjHXuLrx1XGNPGiGky02Vrkh_OveKmXyMsD6vXUgTq5j1BPwuzFdRm8nsHkWSRG_O-HPz1e5mbWIxYGJyMCtaN3SCPqeRoLiRRyUF-QAcXJd2KPgc9xXreBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E43smOZ9VlAnfIruDfaoGItHBs4XNI8eTFnp-Pae8mWYt6LysD5tbECpa4a-CP2RMIehbEFt3RgTKB68QvjmpyxV-rVymBjA-X5BpfuKNCzZ3JENaV8PqMY5UnlVrfjVdjxU7EDxTJwcbC23er_TR9phkUbThOZicVWhQheEkhDlfqFBthtvlcuBAvBWQRFh2sb6IYfxHEnG3XxYdSRAkt8x-Wrt7pM6Ll85MxYe7Lipto17QhuNEQOsj4lhfSSc2dMgtJBeZpVQ8nbpXd3ZHnRl8q-14DyQJEJMIJB5Ae5TkkdnmYkbaDDtRNtzOCsnXGyW8heWuK3IeoYxMWdfjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D9s5ebdPz8wrasWlVoZMTLhDdfvnwHEX9Pg5LQW8Oxc1AYf1j0Gx3379W6XIC5IspwtUmoA60Lkh8sDOqzpwNM0wD8ql5G3e7bIxPaUbU2Ig3CMYF1a5Lu8D5PBKuoLmW-0GBiWcFoTqNBk2WlFSM9ql3OPSJNlUu3AEAhObjCWZK3i_G_A7u4rbgALWonGblDXRjRKjbmfuXstzmMXqF1zSxxtvK7dIJGU_wTjoznPa5GG1FZfvIhK1ubwRDtPFlgqQ3aNk2PzyhNa_OZckkmvUMDnvvwUK9tnvqG1XpY2BxyBjjnjZgjroSIctWwz6bc_JCN4ynwFYbkUwbhwEyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jsiHleQr6vYb5nU8m5qPQDNWZeKFz7YNeHXGpbwL7nvM-xCrhZHBYqctnXX9N0ciuZt17asaCXTHcvuifpLPuCj8yl4_4aBRp_3dYLF3mmEA_fYTZH9J4vF1IZXDbKiyR3E5NzyBepwDNuM2mSj2xSjt3hTfQW3p8cznRCl3bFjO_Qls-kpAVGFADy3DpEZVYQl8OcapZcjnNlUaqr8ugWEOIlIdMmBQglexf-kSo9wXql5PIxgnTRPJxmOG4ZjB3VBAIy1c_uZHz6r4R14qRIDPFvS4GdBHWzfAOlt_MFdZaFF4ZKGZ2Fpng1JRAz73Zz1gZKqNdvZ6hwxK15LgZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=QePbXmQNXiaKT7VN3x4Wz8LMDTkuoSxW8nudVd4Oev7HnMBIhlXwj2I4P-2Sxe322IIJyn0IX7XfORYwWjpkjxP07KCW9-nQEtnnmvxA_EDR3r3nYNlO-qVE6S3hHeSwsZYpsMGxVrvA_MxHjorQJhbdMKurHokXJAf2Wi9JX0D1pX2mMw-hbcNBjbwdBjSYDSdf5DgddXajfEg901k2liuo3sX2Gjmzyh41KOC_BlpyN7xC9MksvlBaavCvdnSX3V5csckFm_A8ieb6F_P8bwcLOETyhZmV5om3yBpXhf9OgsWGp2qXABKJoS974C9bkDz6py6w_Sith8jpzqjs9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=QePbXmQNXiaKT7VN3x4Wz8LMDTkuoSxW8nudVd4Oev7HnMBIhlXwj2I4P-2Sxe322IIJyn0IX7XfORYwWjpkjxP07KCW9-nQEtnnmvxA_EDR3r3nYNlO-qVE6S3hHeSwsZYpsMGxVrvA_MxHjorQJhbdMKurHokXJAf2Wi9JX0D1pX2mMw-hbcNBjbwdBjSYDSdf5DgddXajfEg901k2liuo3sX2Gjmzyh41KOC_BlpyN7xC9MksvlBaavCvdnSX3V5csckFm_A8ieb6F_P8bwcLOETyhZmV5om3yBpXhf9OgsWGp2qXABKJoS974C9bkDz6py6w_Sith8jpzqjs9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=L6OYTWOXDgSf_Pn3yQANubKYMrUgdVQgQ9n2gkL5JLYlaBbs1-4tGz79gcRGRiBOnoJM0PwJDuuK-iJw_w-TWcSI_ws3DZUG3G2rhdIXeM8VfmhyZLCNrFOQtZttLt7Cf-vPIKKlAMjkiw-iaikz19f2CHCnn7Sb7KQgOZknE8msVrBL5d243fVtDY395HCkNsYk0NktgIDtwpjEi-8e10-1jwva4FAh72UAcvVImVMFo2ZWo6ptwP0IVIpJmZxjhKlEPqRWZUf-FIkLhfbaFXoLqUV2EhNkKE5pOJI26dx1stm6ol5fG9x0VkrehzisqJB1GL0U0Wv4uZoulWI8x4olO4kjXzQRpp1PGgiIzf14wNV4H6sMEJV7sBr4IXQtsW77iK5v_NVfJCyDi2K_U9TEStjJEE1zrQAOuzPCsfr4wP6Cqq3dOjza8FdJaUnbo2GsM5XwNQEPD_si0y7WoIYjnzjF8OI8ViNaznjfIUiJDvAl8YxcblOeacUnKV8PIr_oAiqUKIXAgzYdEOfytV0TeYasxs0QnoHZmRKO9cIsAqK9oKriY0UBumANJJRNgb4IlK9BqwCXcb6santHsXj7yh3Gm8B4yodkiVO9Y97iptZ7YmadRboPCgMEjD_EGoy1uKVIMnOFC0rcGJ1xTNs560UFwK2QH-uHevBSdz0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=L6OYTWOXDgSf_Pn3yQANubKYMrUgdVQgQ9n2gkL5JLYlaBbs1-4tGz79gcRGRiBOnoJM0PwJDuuK-iJw_w-TWcSI_ws3DZUG3G2rhdIXeM8VfmhyZLCNrFOQtZttLt7Cf-vPIKKlAMjkiw-iaikz19f2CHCnn7Sb7KQgOZknE8msVrBL5d243fVtDY395HCkNsYk0NktgIDtwpjEi-8e10-1jwva4FAh72UAcvVImVMFo2ZWo6ptwP0IVIpJmZxjhKlEPqRWZUf-FIkLhfbaFXoLqUV2EhNkKE5pOJI26dx1stm6ol5fG9x0VkrehzisqJB1GL0U0Wv4uZoulWI8x4olO4kjXzQRpp1PGgiIzf14wNV4H6sMEJV7sBr4IXQtsW77iK5v_NVfJCyDi2K_U9TEStjJEE1zrQAOuzPCsfr4wP6Cqq3dOjza8FdJaUnbo2GsM5XwNQEPD_si0y7WoIYjnzjF8OI8ViNaznjfIUiJDvAl8YxcblOeacUnKV8PIr_oAiqUKIXAgzYdEOfytV0TeYasxs0QnoHZmRKO9cIsAqK9oKriY0UBumANJJRNgb4IlK9BqwCXcb6santHsXj7yh3Gm8B4yodkiVO9Y97iptZ7YmadRboPCgMEjD_EGoy1uKVIMnOFC0rcGJ1xTNs560UFwK2QH-uHevBSdz0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6424">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rN9nrx1GEkfqlV4xrQnBZlYIl5fVpmy6d0cGxyUHVwXL9-LIwxDozF0fcxjEr-pO7ts_n7NUWrQcbWG4KmfZe-NweX5hwH_Nfv2QOSCFm1nU3pkF6CMizBz0e49pbWo0XuokN6fL1liFzY5v0f7uQ3jyjnv28aCQevz9T-nxCF5uuKl0KSyZ3cfJvPyZp7JO-qmLwFrbuahU-_0YNyAVzpJ8Ztd1UQ2mvDeh8H3a-3lgl5smOcE1z_k9rBtbEp0q16CD5_SlleXeSaiROso9Ygth4zSomPQ_ibl6FgoyrDwBDRN9FjbLFvkpQ4Od2njTMqUybFYtNGfJjBA3LSKuAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6423">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،  ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6423" target="_blank">📅 11:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6422">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_eZrrMljwqsXDOmsUgh1O2faZho2RsEWBhJNVLOAj0_lCmzUF_Ll47SY3ZuJRREj7D6S5vvDZWngardldvrqIKOZtkway27bpEhOsWDUOr19dfdGdz5SZQl17jqROs76TKObo3AaBOjW8Iq2BO4NyOOXf616FmvBfdTE_SV_pQAx3rXj7h9Dyxp6Q2MGmNGUvaHQLatqv75keclcokaVIFHJDLvkwAcd10cuXIeM-ffDEbeaUUb4tuxVe4lEhtlGeK4NdNmWIpvVmi7j5BSB6x5gDxVn8P1hgSCfnCyeXGna9FV94qpYGztOx2nm7mBZPL3O2Qsyk6UoAIHvAAflg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاوید نام «امیرحسین صفری»
که جمهوری اسلامی دیروز او را در
اصفهان اعدام کرد،
فرزند شهید بوده.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6422" target="_blank">📅 11:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6421">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=Rhk9xjbYEwRbI_NG-UdrUKZeFMg4hAp3GbA_GDKeQKy-ZaCutCO24BQ6KvYynmqr_AQD91SFYW1iFWr4sZL7kMR10nxPuEJstz-8YMvNF2lSScMdmxW4k9rAXg9VmaCYw4sRt88o8qSC-cbMkuyCXRYjv8AxsWqrq6ylUfa5J300OD_ml_-brlSOKupU4G95XLXrIYS3L-FW6yNnIzkxgLawj3DcHySDYQWwt3EcWs_GiidJlT6uEuLCiCz2DifLX3RDQvGmbhiaqHRJ5xtNJMDPnkGlOrp7JTPZNy5Qaiw5hzwLvo0sMJYmGPP2kKuYNRVjnmtcFd4lGv1zLLM_XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=Rhk9xjbYEwRbI_NG-UdrUKZeFMg4hAp3GbA_GDKeQKy-ZaCutCO24BQ6KvYynmqr_AQD91SFYW1iFWr4sZL7kMR10nxPuEJstz-8YMvNF2lSScMdmxW4k9rAXg9VmaCYw4sRt88o8qSC-cbMkuyCXRYjv8AxsWqrq6ylUfa5J300OD_ml_-brlSOKupU4G95XLXrIYS3L-FW6yNnIzkxgLawj3DcHySDYQWwt3EcWs_GiidJlT6uEuLCiCz2DifLX3RDQvGmbhiaqHRJ5xtNJMDPnkGlOrp7JTPZNy5Qaiw5hzwLvo0sMJYmGPP2kKuYNRVjnmtcFd4lGv1zLLM_XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که در جریان حملات شب گذشته آمریکا، ساختمان «اطلاعات ۳ پ»
اهواز مورد حمله قرار گرفت  و ویران شد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6421" target="_blank">📅 11:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6420">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
سپاه:
به حول و قوه الهی، امروز مجازات متجاوزین اعمال خواهد شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6420" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6419">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cl479ZKedXf41ycQRNEGSGp9Mx_KIOkYGfMQPJTACJTMgKnYpTUGHgUG636hkRuP10ReEdCWsYb94CKx8cqF_jZAP-b4QPssGpsohtvhGo_8JQp73dUSjUUI33TetwDr8uyAfRX-ukAAWt0ecEsXQOH072quYh5HA0iqVnGeth0Pn2VS5O9E7awkumCX0ucBC29OuObbtTUdB-UFBH4_rBoeNSrNQHp9txmiRxqzN5smYjY-1AxacNC8zAxbzkPVEAxj37hsHjx7quk3wPfuyb08bivxgZrC4kjK9A7_7ClAZTt-707F93fkAsSWJEmAabUI96KEsL-KyoE4vqk2ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cY-RAIOUEQXJiM7HigKCSjwt9jQthw3POvi8f3q17phtsK7Qrg967Wbo5j4VvmYMTcXJ41e2uWP3nbqAsrXJjrQEdetANfWHYm6ZblImNzzRVulNwQaDez26h6wdVGZU1zWUlF9c6dJsoDM9UuyhAu4EdYou4ztm3w-zib-tEc5vi3VWKC0aeRQqsk4osj3JXrIsz1xgmNS-8NukCpyDeI_M-P8ZqU3pjE-b3QLgolc1H9wqZ8EkznHjAkAkqJzpOP700hHoP4ZSW0srdHY3tnlGqglMr16MIyyFF-swXl0_93sMeznFA4gBPXGOgnou1Dd5__CZZTo_Ho6fDWZgaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز صبح گفتن به سه کشتی حمله کردن
امروز صبح به دو کشتی</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6418" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6416" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6415">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8swXcKg1K1q5YMQ8LtMuNQ8_Rtnxd1HmLOxtHAEOO3M5HKajpz_JYuxIHpQeAaVhhEElQHKIhz_Hr7ZHS5rCvtkG7jAhC4XSAGqU6GJBqTTyDfiuabGiFHaQlgL29QiTV-vCbDvWcPW7P4Ll79994wIjd1EobUqPe-GOp585jsX6YxQXGrnMfii5J2Zw0PuNwn8ScS76BjpeBEQ8ghxvfN8Ho3ksBTsVPCWWvkXyEVfSpVM1REDSlfEkTE0K_9Rg_LH8s5c05-AJXru99EDT4mChleW_3iNdt1HvWD4I6i68kBkq03ehtT43HHL8DxbQFi7i1Y1XKwgpmglBdzB7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تعداد تلفات گروه تروریستی حشدالشعبی به ۸۰ کشته و ۲۷۰ زخمی رسید!
ایالات متحده و عربستان شب گذشته در پاسخ به حملات پهپادی گروه‌های وابسته به جمهوری اسلامی به عربستان،
به مواضع حشدالشعبی در ۷ استان عراق حمله کردند.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6415" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6414">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9IwAqchGQym1PnAOjhgKLaUUK6RUID5ZOQCqvvFkyBaPiF6pSJJqsKnkBr_GKURFI2KnehRNf3dW6HcIr0ebY92GIn1n5aX8v92Pe6TPrCXogmpPf_rSyTGbiAEi6PUy9Jo_wwI5CaEm6Hb0piqrNb83KWvdzvaXqnsZSiIWayvlr2vR7eYmqGgq3bjr2zFCWhJY8-_Uzw3tZ5i2UnYz5h-AUXJ-woZTgeKwj_vQWJc3Qf4DpP8zcr6ZW-tjVrQG4sH9IfAtAHiqgBs2DVrU6wnrgzd73ICmcQWtfqaCygr-kFVRp7J_Kq676bT3Rp1FRwur_dggtmyqD8ug05vSoDX4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9IwAqchGQym1PnAOjhgKLaUUK6RUID5ZOQCqvvFkyBaPiF6pSJJqsKnkBr_GKURFI2KnehRNf3dW6HcIr0ebY92GIn1n5aX8v92Pe6TPrCXogmpPf_rSyTGbiAEi6PUy9Jo_wwI5CaEm6Hb0piqrNb83KWvdzvaXqnsZSiIWayvlr2vR7eYmqGgq3bjr2zFCWhJY8-_Uzw3tZ5i2UnYz5h-AUXJ-woZTgeKwj_vQWJc3Qf4DpP8zcr6ZW-tjVrQG4sH9IfAtAHiqgBs2DVrU6wnrgzd73ICmcQWtfqaCygr-kFVRp7J_Kq676bT3Rp1FRwur_dggtmyqD8ug05vSoDX4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eTJvrkmvhx8Wv-ycSDGl9_MZ67Umi3TTQOa9YNaIjR9hYCyMo5MDTmjGiOR06foil1kX8y1hXvvSVKpd3sxBbbBO6bk-rXl6Jz8DwRvFY-lDFEwHkAe9v5F51pYpeEAi4xBsnnOxsCOjpKcCTIOL9QkLTl_xx_joHonc0zW7OV8BPlbfST8esSgwYPEsGdIvYC0aphipGkQeakZJrbbSI2znQn1dObhP6L9DqmnnRvj2DoEA-EJ2kuIxyb9AXQlmp0ZP_2kzC3_VjdVf3OYW7VshlcYjCpqUUOzFIorVtvEwK1Brs_OXWRt8qFoo_3i7BiFcDY7_DRL15QxWRbPtvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bmVymx71S1Ds8jRG9x5XS-x9NPc5vKA4sFeQcaRy4RsX3DsZuY-ZpjmJF85uAUcr6Xb1Qz-A7zYPZNnYF8tGxFSZ76jzo6jhZHAugvkOj6-jzJ4mnM0wVrfXRb6q6uWAsyCpvGHMzSVgHhYKuqD_zAPWHjhlBVpWfr5mlHff8yPGqaUs8rkqgdepsXUQyvCyLrAXo3EsC3nqx2L2qPZkN8b1J62_eMjDbQOsXQgqCcmRzSCLfLU7XcUXVQ5ZYRbNXqr8yRhh6ZSOQVVeiP1RYvNmAMZsoTlJP1Ex0ZDagdToxG8KEUYrMFSTDLNMQbXlkYKq7M-zzTOZrNtQ8W9Q4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=p_J-knsr4ph6G_U8jcZpTbydJqU8gABqKmtB0vKf9RCVhjVV82Hk92E6DNUb0wxQwEJm96LVYMJR2n0547CxAQBDru40vx_lppdGd61CsRKdKAulel29Uk-NLTJooyitXNExUJRQOEEA4qkj9kl7Vg2sxmpFQoDERfmB20jZMAqm1Im-EN2uYbwiR_Y0iILbdYwnod1Rsjqizn2R4h4T6aksahhUUm9hlt3PRPh1DFIk9FS6wIBqDCGUNpV_RDsNiryPEHfB8hrbFNXjjNDdMGfvEdfvxNXsrl3D8ayX-8epfHp74od2jL69eyNzUJdgLD-hd-3jeaTQFMxoasFxAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=p_J-knsr4ph6G_U8jcZpTbydJqU8gABqKmtB0vKf9RCVhjVV82Hk92E6DNUb0wxQwEJm96LVYMJR2n0547CxAQBDru40vx_lppdGd61CsRKdKAulel29Uk-NLTJooyitXNExUJRQOEEA4qkj9kl7Vg2sxmpFQoDERfmB20jZMAqm1Im-EN2uYbwiR_Y0iILbdYwnod1Rsjqizn2R4h4T6aksahhUUm9hlt3PRPh1DFIk9FS6wIBqDCGUNpV_RDsNiryPEHfB8hrbFNXjjNDdMGfvEdfvxNXsrl3D8ayX-8epfHp74od2jL69eyNzUJdgLD-hd-3jeaTQFMxoasFxAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=vzwDCkf0aQYs38RLJVMGKzBKOw2l-xO4ppc9vqDZdkHirspHzuzuzToc0MxvF023xVdS2SkC3IxsXwh9FgggAWrvDZeBy961U6XLrL9EgjZPYkf4o1klzHXhRzjEUgf_kAxHlTQz2zvii-VuWqvasMX-r1cPl3FVCjq9cuyAvaLak9rvVhPJp6vEAq_OK8PpkHFbm8M1_784zogku59mn4FoKIFYwRulNWS03KNgVaP-I9KZxxL-207ugY-8GndDLaQnNqbPkjXxrxTsvhdF3zI6Hh2aJST9qhawK8ttO1Gc0r4BCZFgFQE8ENrnJJbod7h7pXsHMlZaIaxusazndQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=vzwDCkf0aQYs38RLJVMGKzBKOw2l-xO4ppc9vqDZdkHirspHzuzuzToc0MxvF023xVdS2SkC3IxsXwh9FgggAWrvDZeBy961U6XLrL9EgjZPYkf4o1klzHXhRzjEUgf_kAxHlTQz2zvii-VuWqvasMX-r1cPl3FVCjq9cuyAvaLak9rvVhPJp6vEAq_OK8PpkHFbm8M1_784zogku59mn4FoKIFYwRulNWS03KNgVaP-I9KZxxL-207ugY-8GndDLaQnNqbPkjXxrxTsvhdF3zI6Hh2aJST9qhawK8ttO1Gc0r4BCZFgFQE8ENrnJJbod7h7pXsHMlZaIaxusazndQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6cZcBnJk46xA7nt1I7auit4jyNS_BJPKLDO-tAE5m60HTDBam-DYPRS0INCf7ugvFC_2qOQoS7XEjXV8dOA6nVFxlurQcD4tPOeOZ20JdfwQmiTTaIGvYzOoQjsu3wYtWqRvkci74_BBCMSctqW_VxEp_fiV9NcvZBNGeLtY8HdnxdX4N9Vnp0nKrgjeVBAco1B6DNqhK_93HhnSNZqQ2uSvGfPTDOBXb5hFI2tEELDUr5O_uutyfhXkwopFYKMApPFrFUj-1UNsaO8nL0s8Iamhk7CplMaupvqqqhLg2LrRJqV7r4KitRIb1H2N-Pz7SrjQBr0_EDErwyRReGs-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQ4_RwVyBeAYLpmll_-hdX_IvkygUrrcsxNWrf36KPL5cBAt4yh8sT5wijjjtUcikHnRP6CVNMLP6epFiHu_Uv8uasbgEmXne-I9BsvsBgHU2K5-UYMldRzK_PrOX0gSKTw0hr_vdtkvEVAtBFHlo7KFW0q0YaIifDMW4wjwinneEP38LIhgbnXzO1mls3lQ53UrmtSQTxwvJHAqr62XWzxZlm8LLAnt6YAIgInHrMVDWSqfNEjE1tl84aYkf_AMqLMGNHmmEpg9NVqDDM8503NAZ3aZdWR64rSaLMj4C8Mt4kWp-OHCchUrgVH2dO21YAl2E1Om8fYD83SGCEQFKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=jvXyGz1DaUkwxIeXOTjvIgDq3bCHR_-O5walC23Gfd8ynv5IN7gwS5sFYVO-heqEs28CkuT9RZEqbzLdWFTQ83HmjAM7bJ8_c42w5VOuucGPGZrFap4deM6SFKRPqc68p5EBtqG_1AJOgN0sLTFYwi2qTJ3Qv686xSnvT2mQbWOsvt0pwgnS5YGKakOZjzLNzWbY7BhCPkuSV1DIfpFVAq1v3nykRMggjgQ4F1M-7GQ1wFvMWHufUdekgboENFjUaVg5WrbueN8ug3HLG6skVFe7cBQrIxmWXWmU3gmEi0eJQHYzwa43xw7n-yaArwIWQnPExSGZE3wHyIwvYVasiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=jvXyGz1DaUkwxIeXOTjvIgDq3bCHR_-O5walC23Gfd8ynv5IN7gwS5sFYVO-heqEs28CkuT9RZEqbzLdWFTQ83HmjAM7bJ8_c42w5VOuucGPGZrFap4deM6SFKRPqc68p5EBtqG_1AJOgN0sLTFYwi2qTJ3Qv686xSnvT2mQbWOsvt0pwgnS5YGKakOZjzLNzWbY7BhCPkuSV1DIfpFVAq1v3nykRMggjgQ4F1M-7GQ1wFvMWHufUdekgboENFjUaVg5WrbueN8ug3HLG6skVFe7cBQrIxmWXWmU3gmEi0eJQHYzwa43xw7n-yaArwIWQnPExSGZE3wHyIwvYVasiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=jr1-nZmWN9fAtV-stdVOQ98RG5fZYA06JF9bqwRVQibE0wl5dnGPCU3o8J1q73j597bRNS_142hXLOQBGE4FDe9SzTbPVtdl5xYzd-xYU_B2p-2pflSWCqXnFic8OBeZFJYNA38Nbio9tBfT0u4_JH6eSGuU18F1Ky6wWkXXmvtSUpCj2GrwQqGo_B0aqJo3UJlyWfoHS1TYsqmnlcOeRKytVKkL1o4umICsbJjELpEi9EMgLBZPOPyG65KbgC0L0os_mUsmiMotY4erAGDqZl8fZUe_nLSGGC_Zp7F1lVFWDlVkPcO7f7YnLSwsxT56GRMAV5hGVGazyDuoymckaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=jr1-nZmWN9fAtV-stdVOQ98RG5fZYA06JF9bqwRVQibE0wl5dnGPCU3o8J1q73j597bRNS_142hXLOQBGE4FDe9SzTbPVtdl5xYzd-xYU_B2p-2pflSWCqXnFic8OBeZFJYNA38Nbio9tBfT0u4_JH6eSGuU18F1Ky6wWkXXmvtSUpCj2GrwQqGo_B0aqJo3UJlyWfoHS1TYsqmnlcOeRKytVKkL1o4umICsbJjELpEi9EMgLBZPOPyG65KbgC0L0os_mUsmiMotY4erAGDqZl8fZUe_nLSGGC_Zp7F1lVFWDlVkPcO7f7YnLSwsxT56GRMAV5hGVGazyDuoymckaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FT4SrVqnvOHBcbSXoobi8WjpW2uOkA0a__liAb0B_VczcJEq_5D-OGJROYQP5BU2Ebhn-_hAJF7wPRl_is_AO4QZdhaH4Mv53WQ62f0ZCh4O-IGJtdsWOMDSmmGLy0P2-Gb-OEPZW0AhFY6s5sJFYz19MEWy0cHmJBuaQP17ii6KH9IsutbfWoMS7VAsSGM_gArKfEF_7GdrCoH-iRC4ZOqsfY8OaBXboDxgp09vBHb19WDDJq9J1zkb3sA5hRk5XcyDYfOy1Tkzp2WeviuqH-kH8VJOTPHNv0jHKzUrFUzuFiKWBsSVh3-O3TczOa2dgPit59HxYXKNuTTQNRygYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9ruBQFsd6X8qOCPq9aWvobjLmQbTD5gEUXtGghfoRvQJ3XK3z69fF-WXOqjVfsBaHDzjjw-bpFuAERU0RRgr6hdFoVTGBP1ln5EE0Mp6zj1feCCjnk8IM0AYqHm8AbrAHG9ylm5CQ1VOYmluC0vNG_s8Y_QSWi_qgT1BstbpUACeRn_he9HGibWLs9Bbta35RRaqR1BnAsAlABAMiME4BzUXM3qcS5ln2as55KV1erAlLT6ahm2wAxi7XjSqqTUVKxnFYjajOWCxaXXpCgkFIicwIfT94I-SGH_xUNX2DEcfIKmm95EQzjxjydowQBhvYtfmHMRiFkRsjf6N-necw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RreEyxX4G9_trrLTL1XiBDSzbmUJcuKZbvhZ0seM2TuEfjKlskJqvHRNGLtHUjDwmPJectIlOWGMIDgdIl6AKPhU4H4ENV8TiylQxgwtOogNJaXNQBsjS97fHbqBY9dZMyj8G_ANanj8VXRJYhQQa2G_HgEAWuLpsITtgFoU4XT5O9Mhk4yulyE2Lo_Yj9loWvjesu3ec1NKIgGYerwk7kks0Mkg9BP6on7bc1Pggt9LarZ16PGKK5nvD8yYkrMW9OBLiz_nnzuVygzbYWuENNlTa5dYKg297kks3yONU01sEMBUVgjDg4GLcjsvqROWpO7F-bKQlIC7Iy-OxPEItQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKjREEHp1o-5-S8XRnYu8A1xYnhwqipa62kd7lGt8-vbDjW3F6R8o--gYZ5hmTRU8PjFD2UVg5QnYm5GitLcNk8j1udXIh_7mHkeoDYi37pRX5A8xtM68V3rNUw0mXxv8Mhn69eKA7DimHStfwV0D8W-Rm4njig_YiXmuTYDAYBCHTAk0kMPyp_rz_mHfBr-Ge-5eSTObK3gEoRhhvWvn0EE9iQyTKNpmXL-ISQ5fYK9H3cHzckvNm9Qw1Ov2emGfo9km17gKDyFImFRkfRPXA7FF6veKowAJohWx_8Wp0OpKUb2bmlmhM_NKK-jTlt_HerxFzMnXEkY9g-XJrP44A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XVm1ROInHp63VE8gYLmbc61D5-CoiUcBP8Mp9OuZZF_N949yJ2dCM4oZCwjSZdOh7gE4b4QqiLgfP1DgneHSX-iqhmhd1HE3EJO3Af1Rh2d-F_wOdiKCr33yoCd0lxzUKwe9G_0_oKHEhvoH06mcI2wv_Cz-thAa1yntOFNyTerBOMa4rNgrbVVOu9XLcn3jxAkcp_kZPRa53_unKuBBNVqxzGKMe-zjmr4Yx1NjN_l38sV4F8Grxfd2GfQvjakNGm7PInVD-6XiOaQ8iIGto4fCiAXMq1vADAXIoajnMAQ4StWupYDaQ3sXCOjbE3YCI-AuoKogdTIhMswmwPDbxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IdJYc6Ko5tBVorpQ0yTm_8phh227U9YXS5MCAgSbPmFpyjIkuQoTY1osqaJMRzc8KRmDwzq8_6S1Lfxl0FlMf-fjpXJsYv6XtajjYRBPakEtWqPY5OXo1OLcPxtN_ztMolVeOy4bZ9yOb1NyplvQpw51ropOzuO3jOSiESAoW-bZAaRRK-3_4JQpe-26Sw3DV8KftSw74zLF9INLyqfBlltqqHOv18bgxb8SwqVICYg_7kSl422ZGM1UCTAps-Id2Utr2hsiupNImy0vM2L0P1zpt8_Fci_xlp1oVsGpRiWQWQTZgL-Dg_gh2jtPqOajLHcYnkH7aLhHj9hkAXM-_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sQD26PAmiN2kIjuAN1DaRNrShdA_uEQ5yIaQJ6A9ncWN7pW-sn3tIopcDcHqz6GJS72WbXZzPH9w5dwZL0WKxD9W1HYZt9d8oYm0Yvnptt6ZGU5LUIUN-zgLwKgKRb4QUzsj3_xDS1rtFx14p-RNceU5EJB9E0_4bRo8XEgmPRX6p0xaiUfb3QHKTa68uinfoIncqSvG1KqN_I0scjM2mWklyEkTLTFUNUdq-kmc3aiXNRrR6vWhHOsn_PSei3ltU4IG0HpyeJT0WPE1LwCcOTDjbsrKmSlWJwSR5AnPiu7kw6QknMSUdhfGpsS520uMZjp9jHPIFcv-C5uJGQUU9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o42P7WZLca6F-HMKByv_aAMWIeL3OCxvfoKrI28HwIjoGxu2AcGteY005cOqBmSB7uFtJlE4GtD0dq-1r18D7ZtgeaLF8qThXpR2c7eF0-rWZT5Ryd9FV0ytDi-Lm7nV5Ke2mzeYS602eMv92DE0WHncTmdEuhjM3z3yHi3NnBQeRdhyOeVGg8l7d1TjLjuhChu9He-OFUjy1ql7fH7I8ABlCK434yy-bewnK_RvKD4rkscqcKPv43w-31mru43HvvIALdM1_XTEjnSoOmumMUgZ59zy-y0EyX69KhSJbfO0QMXOyLsjKivxUFRNzmnp-gjLmEJC9qf0C8s8V-S9yA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfZMMRx8wWPEFdgip31-D6zBhTb87hR16coMLSmgvPMGqb5pq24-kjhY62UIfIVO0x98hbm9HNIedG8-CnAa-sVy8EGcoTxuJOrEe-UTJJyA4Bm1NQRKNIWzG1foOzop278YPE8d6ecxdXh9WrSOUwJY8xv1osy7L3waT7Rs1ADqypNaNWqyai6ZD1Gzy6eG8wV672v7qWjvoTE0oMTNqkgifjGTGksoNNywYmDmUkOUN62HO50bqRAHnHVItOKRkRNDaM6DDDjtxqEO3UTUr7uDC58ahEB85619EWFL6025epKl4CD0gTFBfOzAbFlhQG_Xi1JY_sqoL7kvaK5Q_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y88DNOityGYTDvYaHz10dOimvoj15PZ5OIU5YHPeC2CuWuXa36gEEvFDtRyl6W64QkP4DuqQ90v96-8sFXfcnfRZU_ZTND0oh3s70sFBELA2og-YfbDxdL5Hi3HLAz1p8lH1q5Qc3AOiBZ89J4zCOLiZQTv_4zJz_YPmhbMFIRqeMzml1PXErkvE2n-Pesd-RkJRswCVdpQBVKr1t1LO76xKMXBwM5113zD7Q3bVzljfiYCXORF61tbs0pZ4dmCg-kVSuGpbVCrx3Bv8yE7FOuWaqViz-ZPEIkm2HtgpkRZq-Xw6NP6dU7JtPp6uPD06ZhkdyUyK-r8_9MH9NoAHCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=Zd88POvyyTj0Z4ekKjzduiUaSRrwuw41yZqRd4Cl0w5hrMr-3g9ozMtZvzKraV5TEjvZUJ5UmOWXJnH6VtnG7dOQOcZAAhi9vNaXQ6hbA1PhHXPxOg_b2ja4DcJP1hUfAOovvWu3BV0HyGM8o16yiuvndc_bUg9bTsmeyCkzqWKJBD7bXN7DRo1ZfghRMV-x1XaeFGRgOGKvFxia-YnhC6t8hK2uTt1y2kM-sC1dXenbM0cjoAf0Svgm8Z6iJ4PTW4hUuNeRSJpkYcEFAwWiEDzuPm3cPoCcfvGTuhq6oQg7HiRBzPI4MIH0csRC9Q0e420ggXIVqxl_060UPcsFmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=Zd88POvyyTj0Z4ekKjzduiUaSRrwuw41yZqRd4Cl0w5hrMr-3g9ozMtZvzKraV5TEjvZUJ5UmOWXJnH6VtnG7dOQOcZAAhi9vNaXQ6hbA1PhHXPxOg_b2ja4DcJP1hUfAOovvWu3BV0HyGM8o16yiuvndc_bUg9bTsmeyCkzqWKJBD7bXN7DRo1ZfghRMV-x1XaeFGRgOGKvFxia-YnhC6t8hK2uTt1y2kM-sC1dXenbM0cjoAf0Svgm8Z6iJ4PTW4hUuNeRSJpkYcEFAwWiEDzuPm3cPoCcfvGTuhq6oQg7HiRBzPI4MIH0csRC9Q0e420ggXIVqxl_060UPcsFmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=OVkIrAEZlCmNT5RCjmC84SA8bI8VmMF3dda4-dKTVx9rg9OD-NtFHyurA9YgQ09LvExkbrmi7RSqMnpxm0z_NxY9jOGhShuB_bKs6K4oyKhMn75J7vLJj-_xeVf12AYt4GM_6UQxr211GIpp-SYYc8tiuIudltbtxhULYDjID8qak9pbRWJSu7Gt-9dffRoyxPe16BLbkuu1iLGkk4S06qAPuV74NmmCYrhmeDMZ-vUYZMtutZmTLKX9APCclu6EXZaf1VX-CMy2dYCz1Z_ujBjVb0XraolAnXojUgkrkNYRY6t2jCaeWQgDmRWpiFmAzwsJtpWVSJlOrEMJf3bARg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=OVkIrAEZlCmNT5RCjmC84SA8bI8VmMF3dda4-dKTVx9rg9OD-NtFHyurA9YgQ09LvExkbrmi7RSqMnpxm0z_NxY9jOGhShuB_bKs6K4oyKhMn75J7vLJj-_xeVf12AYt4GM_6UQxr211GIpp-SYYc8tiuIudltbtxhULYDjID8qak9pbRWJSu7Gt-9dffRoyxPe16BLbkuu1iLGkk4S06qAPuV74NmmCYrhmeDMZ-vUYZMtutZmTLKX9APCclu6EXZaf1VX-CMy2dYCz1Z_ujBjVb0XraolAnXojUgkrkNYRY6t2jCaeWQgDmRWpiFmAzwsJtpWVSJlOrEMJf3bARg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
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

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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 15:23:35</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EifKuCTpulCT_OFZUREqD3ESfwlMzcXjU6VZy4p0oPHFb9pUSQ8Al2ieOxiT7EUr7emJ0u0_VsspBkcDTR5uGCk0ppGBrbsXGxEMG23-HtMAHVh5L_WsiTLzy-5wRT6lVvUFjudduAaef9kGeAxoXqHF02XnlKgXTsCKdXK_DXCm0QukG7Qwx7FtPr-c-YT18gHmOZvJWOfdHUJBA3xvW4rBC3UhBKeJjBVE6B-xccGUwCqlLm-lYmNE_GmtWqae5ogqbzVsTJ-8YiIzXU_fOTbJOqkYjs8CRUpDMNI-9Uawlwj6FV81ZloTVxm6v7C2frbJjSaaqjfmgH0x3j2SdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vf2ze1vR_vgLrIsaAeU6BGjbceIx_2osoh4kYx9PNzeEXniSEY5a7oBsrCBNFGJG1V1X4JogfSdrv8aNiOz3Knku-3ty8C4f9xgCH9W2LHGJwTbOFMIDUn7IhjATJCE3ZYNjsG6Dkdt_VFI_dxCRRAqLn2zv_pgfw1gCkI6gynmrg9IATZ2hTQOaKWNmgKFfvsIMav8JhsA5oQo--PzFG6hGp27zPgldHYHL_HswS3ZRWtUx8p0BFvBmf7RlXt0n39GMjmsNx44nefVzMhgxP06L7jkvJxqFLNLpUIinGl94egTYFwd-QH7IFVjTaZRjuOlyDKlEnHfEq196zokKIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZHG79sJfk1HrKHU4l7ii6713U9t5HhqYmsyezxN74VrrS_0Wfk4AODeESUxvBlXCAxfdgL34C6m48QO1y8W4MOTUwuyugrHXriYc8mgORpq_NwTqLW0fc0wlHSTlSyT9cd_hDht5CUQuksOQP8yUtTbPHtHjlDH0zrdXqthLAG3wuEJV9-AiQdkh4Y-fwqYrAS_0TRX8WJubKM96rkSVYskRn_-U-1F13hbS_ydJv57JuvA7goB6HpEdK5i6viK9W4Y38GlpNYX7kBmYP_igM4O5f_GMjAnjF7Mu-A38A8eoDGkCreDvYqtTrxVterCxt3IscOX9ERQlQaa5L7ovQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SRenryfa2oG2KZlxHJuw8UXZjm_Nj9EMBcaWqm2TXhMJ_MqgyMofWueYuIbi5LIHFxz3HNzUObmJBK-5b_wPZ11Ldr1CTOGEddN2avyvsGr2WbhYmDKP3WTpvQJ-97BDr0g8RE1BJTMkXLdaUBVj3MegXmV4drogOFR40s45S2AdsF2OmflcWFhE2xxkzpLX7nxiKQPYCcrOso1geNWq4jMXH6NF7HadDV-c0qVUpG2jm58eHAC99kfujr4cchoTdjwTBCeoQG7_HUMkqi-cCybASQXzcsEHxL79GyPWbD5kTa1xhcoB-h8MfR2sp2vEILfi6jd_I62tOlwEgA1e7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUt-cL8RVIYSXGymqenW4r4nRgsCxoGW-79_wktf6DfSRe5Lxm2TS1P2XTnwDVtUU9JZSJttsqEeydmviaa_6V7wUUVL8oNwNCI3CMsydnNdFMmrR1lE6AZ5cWXCN4EgxdkbA25bfstfUAAM6fmb7y9xSb5_0BsJdsza7VoqgWnHlXHxXStjKVrepZzcswLIVtZupfhl-NlAxz0nEt5kMT761-SxMSwwCBUQZLBOrWcs09vrR5rfZd4OQ7FP4_TZ0MqsqVAG0kXRhnLMLi6t8ndI25GTcSq8CWj4BtF7qU5JBXA5L9rX-fcnEVCkPM8y5-6fHkUXQhU0hYUrh9TYZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Df1C1__G8fN99ec4J187IBtQKmX6CK_xNVDSNa8JXuHMCZKpWEBiWPcKgl4-OnYTs2o8jLYs9j9pwqnFnfohl0CnAHq1q-5we_Kphb3tvMU7R4282dG870pHJcrnu3LFQvZf5SYlWrOg8M4C6dzXZCopGpa5NUsmWhk9sdQ7na9XBWrp3uZ8y-CPSayqyRjFJ5m3qfVmZerXtLxPtAq6Tq478AfkzfFUZX6fHGNipgWDQ3ETWRlm9NORAQL9MD-gwVMVfZk2G-KZimfZe3glUFXfKKseH-2q_XBpVQRfQAOQ0dLGVJifDmH8aGdeQ2e5wLNbZ1rYvkkXdqYSMdBoog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDqbOYiJYXCh8Yae38LV3ZmE0EyBLt5cM9ii2SARa5TpampEXW3iXGsadIrY7JCcTNPPDaY95X2EICgZummecTXQQ_7YvDQKsLGogT2mZYLpPeg4Jx0K1PK3XClORSk-cqktJEbuKDT3lx7wCe4hke4ctdNmLoJD6PDv6Oog-RE6Medww2LJlunJxlWDoy7A6mM4VkAcbmuozPV_MzJkewOLrdg1930w-ptaByqU92-EtBHLdRrCpZUCrH0lswdodZklta1xgmv27BKqgHISaLmJpNghtGUJ47dVtozuSPM-7SLnQmqWzFYnrjDxwys3STTo7JSSmL0zvjLZM8TV_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LR80kl-ehPDj7T_Z_P3rCPuxYS5Lt40K4u-zSO4b_6s616jiYU4lrzGpIgI--_QHuCGUudwvzXMIAJL8xnEXr00GghyUJIshpv592u369HfiEV6M_ZczqWex_5dVOCG9yEyJQmtsQTKAZOGNxVek5vYO94ONJrR7MQhGAypu8YhSn5J7YAal2bs8rZAFz2EoPwBZ-mft4QqkxOTDgEsG3hKjEOs0ByjJk2tplvU9vR9CHVxiTns4J9Ycmn76FSHzFovEw5bn1fViIv1-MTjDLZfluRUt7-CVrey-FequiskSg1oXFCwT-VfsHMbJ1-BT_ERP0E7Quda4TVdxp3b88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQegXSkgHUzyOVrtA0fNECy1Chq-PphCRQzuGM-rwjVgubTBuKwruLlNOWXqx7WUpl3gKezgRdHNLUi6Tji6Yi7RBHZYhR7ROJ22COXcZ1q0wiyyl2G3YpAWE2F46gsRfXxoUQGknD1slmCIXHno__Skjc_qkA9cZ3vhWWCdiSQI5u9r9LjNOQ1UhPJqhFEtmwI2jNpF0tSHznMPEAIkxR0bz1nrO3cKrMSxtvh8VtUAkRx9GT16UBNeOLnoyVtKjjWqWKtq8eygoSDCwVLvL32qCtJt1HMC13KnXu54JPPXIzjumA6pLev7mcqL7wHT1RKBQh6vQe5DPr05dxnBBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0MWkowWQmmdyAMvkgGh1G5mVkxL23MFrlfWmxa-mAjG5h1MTm0Ex_YBAxpHAt1MzgLwLboeQaDNpQofypn1txFukyzvpHRiwb0FYtHz7kwHcrrDaFDPRPqluHN3Sq6Zk5ASwVbkcJgNSLVzhADvGjKC1XScYUNlaaXxcisj7euuiooq-nVPvcM7OxIWsdnPp8GeTmxtjCA1i56GFxlZBgAmD8Ti-kAu9WZv54MzLppT4fAYEn4fj7YrrjbCPXyn-al6z6x4mj0Jh8plSmyCYTyMLKLHCgKxOItC-KgMLYjCpmki_wEK4IuMop8HOYNvtN_ZQyW73Yia6-rqu8xU_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b21yOC7U1ZrtHxdvG74FKnhw4Gma9Uwo_1czO3uuqx_lMKWFl75WI_un87Qp7QW0PgrHkPjQ3AqW9-jdETdUntk9pt0h-_eP-aur04vnASBnP-v4uKe7OhGfKd_NifryRio2iexFZP_z4_qi_YDh6yBLRxf71iTEp9cuI8pOf99G-9swQExaGoaWi8eUR7Q5WG7OzxrotLyFjH0Nu8IdhruUCP0WpAbp9eJQWWabTKEgwXEVUh64RoV4dH0WlIdfgKXpRD6G7xs4exwH8UPS71_Zy2YdhAwpNB4xCblX13arKJvYeuf8_RyBRqzNRP_wQkagP9SaL4agXMr8yCK88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIGxKpEutFmgVZOI2g92HD0QFQp-OutM3DTMaM01HPUcTF7kUJ_RhWOAQ_bYYFkVfejmLFVhHuabFkzayJHQr9ibZoeZ_Jo0s-WWYfrOxdIjyQivOpmjEjOkR0M3P7kOJlRW1QfT8dxGvXz03YQwFklrBkslJVZbPAHsr9mnrI90wth6D5PrV4CCvve3w3Cf2W7Hvi8jxkO0kNmynNinjz-Mgl_KZBvE1qfw80A9mGFub3BQN0_mMC6IYYMwzKIv4rXCUtvOAn-jn0I7sA5I9hQtnVWS-MjSc98oP8HVKkwiu_Xl2JbfaYhOP0d61XVeGa-pFZw8xSz1hrUIHvDMbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAmdDjgu3QxQoyMSX5jGg8eiTvSaGamEepQINQUNbttda4ZrTfLcIA1UWvZzMqWT5ICRWFMOK0P8H1vZLfNmcFm10RK8ok8wQJbXNOmTmwBKVokfIbAqeMqO1r3ANxVbdukxFVNc23QcJNjrZ602bQfx1_8ZjokpcTv0r9reIVEF1afW59xh8Bqtl0FCNkyYfROiZXjmJuX9JtpHaxv0PKCQ087XupiwuL0sg-ZbLK_k5shEdZ8tfa9tPfCP_9rpPLfESSx8iMCez5HE25mIFczY0-ziE0_8oiEu6x9IR0ueabn1yVOT9MTlJk0PevLogIZ7QFwt6KW59JZdQRaxiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=ioJIej5YbayuKcU0qJRr1UBTfDm4_Rli3nzplhdDHmxj-vSEMO-Hw-WYHumtYq1U1fqH9OzEouaXtoAuWu01e5viEp5JQbwHaXPqbPgBCC6bH6TCsf8UwkxeDTRa6Byb0nEp1ICKe-5pZ6Vpghsso5uqhH_W_-tVFDFyQIL6Roj151iUZejFn1J-4RGgJ_nl-5x1ty841n5AbT1z1FtGhNPNW1S1V2ri9KfDN5R8uhBM4TkzE05gxeFgv3qWJ9tQEUfmRqf5TOtzOQEi-JVw_UAqWXrx0U8B0U_hNZhwFcoTr_pxcTKjC4MBrwcuU-KbiXe_1CmOBGn5GZuOKyiP6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=ioJIej5YbayuKcU0qJRr1UBTfDm4_Rli3nzplhdDHmxj-vSEMO-Hw-WYHumtYq1U1fqH9OzEouaXtoAuWu01e5viEp5JQbwHaXPqbPgBCC6bH6TCsf8UwkxeDTRa6Byb0nEp1ICKe-5pZ6Vpghsso5uqhH_W_-tVFDFyQIL6Roj151iUZejFn1J-4RGgJ_nl-5x1ty841n5AbT1z1FtGhNPNW1S1V2ri9KfDN5R8uhBM4TkzE05gxeFgv3qWJ9tQEUfmRqf5TOtzOQEi-JVw_UAqWXrx0U8B0U_hNZhwFcoTr_pxcTKjC4MBrwcuU-KbiXe_1CmOBGn5GZuOKyiP6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYed9fUA93dhYdfNmttVcm-2lUMw13RTbLImI-z9mIYAp3Fn2k2kwxWO1ig3HF9kt__Qd30l4m1S2SDDhtjk5O0OQsidkXQ07ucDS_PfMsyPqIF9ZhT1o8M2Cxsd_EbJQdDbi9aBA4SfwyLGuP6nOffLvRWw7t8OIr385KWwqDP63fknUcx9lGhmSwZ20KPLmq_5e37EHVefD9YRhdJu6ixoSXKTToGezCK0UiQndY6nkAU_-eRTxFwse4feS584QcekMbB0tAYzlBdDkGKmgpvLIimfjExjasGpdPQADAzfOTbty7ziR-RNmt2mTKBDmtYnfK69_5xd6506jVO7-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qp-uWfFXcnmLv-0yLX9U0HSaaUUxpVEYsNA35IzA3RZ-mM09Z8qB8OWIInZRV5Fe5j1ZjlLlWA0DazcSD2o0xu8nMZ3ylh3dgmLYJw4cWa_sQc0zyzCin0Qbvx1roTzR6johL1kwCcTY9qRTifFt9OubskB7kzNkKy_yiCe2wjUf4Rim-bMz2KZahHQ25ckWSh3Nebd1taY4UxIihZQn7f69pMlL-EJplk5JVhn2Yw4agFirJiH4DSJsR70EE6oEzkzw_d9MyyExhc_W7tCeH3FiKLjiprPnDrY5dfw_ZNe1cvNuh7Bq8f0xN8kOgk6fnqMRLOmKSOo82voIFrZTHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjUcCmckFhian4fxZ1CPt_X04Yk4G8LvzCk76rPDE6hZ-lP3sq3DRxi0vaxhA4hl8M9pNUa3QUNtth4SqRQZqUIcLA74UnsK_BPTS6Bgf7GNfkE5jfk1PNSoy0Z-Nal6KoKmZzYgnrEcipTB5LCSysETkY2UCmtC9W_frZ5AJU0WJUbf8SwLP3_WtodCIrf5oxk6gnE5v71AFZdHvikJAyCVbnur0zKhhuZcRbMvD7lj0cBlxQbcUSRVRelz6dp9KuB31v_i6bCWRUBIL4QRyPXcyCyFwRlkaDQCAZxiOHi68xsZNv_V0yoVkKiRfa_AR3IN29c3dY7Mmhjk_EPy-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWQBxjYn7_xb8RuNGQqaAd78zCR3QafmE8yU_QS-kXLaC30_uLvZ5HZYKKj3JIa2hsXUZnsRUyOQnt7I40X9So5IbSk4dEDuj7pg818iLSzTLDEvT-QtDH2HmKY57pmbb20KTW7LTw4dIOTllNWYt35zT_p3Ao8giILZezoUCNWl9gsWrpwLRYvQwGU6jcIaLqASZztvzmMxwhc9BFSd0YSq64GCGO0URIi8ODB22Rgy8JB0mnoCJlRJJYqw7w-pd1uRlwpL993IWcmPFjfepejgQXyyg8BZCKjC6Yb4FHczqdMe4jQ3AjEY5lwToL4IORxuGiPHAoOMwECCN10vZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8Hfzp7yvCb2c256gU4MEaYAkjji7Xwyd3qiGfKvZRWigbon6lXd4fhMgigRVWmGmWylNnff7nGEOSWsuAUwA6cJUI_Y5wRPGTBGH91X5KTvUqwiB3OAgDPFJ2iD0_1SvcjAg0wB5Zdqmh6kCP5cKc8nrVM_PsxDhNmZZ2QCzMMvza8p6NVI3To-r0HrdBNBU0aLsPohk9Qb6z8kN3M6g81fGRTNrzDgT8P5uYmYFYKBZZW0CqM2eUfk7zA_bUJodqf1T5zJXXsUxG42BL9sy8hgAopx9H9V6NErPRMsd4pftVfaSLPbpcwTIBq6ZkiG17K7tL6tTWrK3PNtfkb6NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skSQ2uQRhuYkPxVNnSR6UiScod1H1c847IQv1EL4JyX7zth7V_pgO48CcnUjrFHuKPQegbbWbdXpAKcot4BWhdyToerVzQVhOFtoBDTu_ZjpKI5nrTXQrtbv-mTZ0RDhkk2GgsboFgLUS1K3ZZaykxK0LCloOj47cKjnXbKnTxtyNj1Vl3W0nSU2nUrZfx_CeoQfpma5gXQYa9Zo7RM8coCE0Es_w1_oIMQnqm9eiE3_zLRqnRPJBTAtu1XFhBWCLxPNtIauw4F_q1HG8m1Pzb42joa4MSEWFQEFuXLWdRC_TJP6U8UufijVdq5BQswh6zAojN9blHYDtXJcxoAgxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEyodjps_bm2yA99yBgWdx2zSaa1wR_aQw6i6ImDrK0RNnNWXWo43EO2boAb2GfVyvBn5hpPNYvM2mOwZFsY6HO3neusGmwCt17sV74wvXjE0agIGQ1MBg1LBCeHQG6Ceo3lmK5tIW4N77AmG1agcW6DOroYToAuuSxzUkxRKqe32A4H7_y-e7-VlpS7cWKRWbai7QFGxUNkwMctQ4q5DH-Xc4aU_vwxoMfaTy3g8pulNnQqc4MKswQubIhzfyFDxsecjIYRMKeSrrbEtQu4jVlj2nUf2rdlNc7fKpoluWnENxrdBNRZkxsAY_Jjei4jtha1EObITALVCRMeVf_gJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoSYGKdvEWeygf71bzeJbli69nMWFZDneHlBTnrE-y_gws3eQPJ-vcENxgo-RtEbIzjRH222YUHgrRZo3ndaszxG4_Mc2zvYMGHapXcROVxPVxw2FobFwGwfKV5NgUtV0-3rwFu2d7h9MxTwAZgKwL2ImwQQNPyY3ybsPehrjuuQQlkATbcJK44KUFQXPM2DwkhrED-9FcfTRDUFguCHcKDInX6DabRWI16B2cUGaw7x-SUGU_CsPb0PCB45tKB2YJFVDrhcZV5LE0h_YOmiyYz7hQRxv1r3aRrBW_zbIA5pEXOM6vnYJ-Y60HwICyMgfyr5pMOVkKnNMy9nP5O0nA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=gJddnz2ReT3wQwYhHOyAjIADkSlh5NEy5VFl3twg_nw0r6HP02woKGRCTj1RI9eD5JcskVo767yiqqa4dsmoOj81SNacN4k8M-nDRvyzeboWkkqJN3OQXSOxuRKTzIfkyc0Vwnu7QbE5jTr0-u6v3GBk-PSIFm_3K864L0UqlA1prASlYomon2y_Q32UGfTdDtS1m1Z8T1SW3tDLny1IJsnj2BsCoaqIMfas6iVYzV3sMtgfsqXHzMVmSl4CXelNKnbZIYBqxK_r1VokY1DHHAPTm-P3F7k7CTOWPldRsmGE5bBsb19tUceXpEOT20cc2hMoA5vywJDQa780glJCnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=gJddnz2ReT3wQwYhHOyAjIADkSlh5NEy5VFl3twg_nw0r6HP02woKGRCTj1RI9eD5JcskVo767yiqqa4dsmoOj81SNacN4k8M-nDRvyzeboWkkqJN3OQXSOxuRKTzIfkyc0Vwnu7QbE5jTr0-u6v3GBk-PSIFm_3K864L0UqlA1prASlYomon2y_Q32UGfTdDtS1m1Z8T1SW3tDLny1IJsnj2BsCoaqIMfas6iVYzV3sMtgfsqXHzMVmSl4CXelNKnbZIYBqxK_r1VokY1DHHAPTm-P3F7k7CTOWPldRsmGE5bBsb19tUceXpEOT20cc2hMoA5vywJDQa780glJCnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSO7l5vLBqg7vbIhfILVmyFBsaLBe5U0-bhsyuljyoUAAS3HZPuLZzYW_xrV6rbJ0bNF_jk8x5SSpEv2yVeqZ9MiE7iqe_vSxSJbut72Qlnq3naeEjaPgMpHR3aaL2uJp00p6AneC88pz-jL2xwC2eTEit3NeBQfFBtq3-f6Zx3NFh_AJMLuL6_H_vt8Xx2VnUaT7s6jLwTumc8f2-HSlALFtVc9LsxqmA1TUUxLq_aCyGJ1wYM8UEKj8ua9kwPNZqbfrtNBgPY3Hrw8W_nmN4A5VeRnKNPfl7iCQHdkKB22bXc_moWloGZmkOUBVGxYpsWdEKopiu3O8urLnVw-yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crLttD4m9EjzIgzFz8wckB4r1mjU8_tyCHK_quFjAYUOqgmuMFpKBTHIcIYdErs7mA25MQ-uPjNF6SUb8RMJjJyokTu-hRSwMmLpKvk2TF3NaZDLj3NUS3TDLKuMNWsV6LbUQC_68gY7ernEYCNx-XEB3hTXv7AKCQ9ixJuVV678v7oH4BQtVxXaPDK7vTvL3lWDhulI1qEYXPtMCz66SEzOliUPhbqUSppGrrBCp0xIMaDenooejM8cbt0w4nxVF64kT1A_PVANZVl5W2usWS5C-ZHsiX2ftngRXZG7BN9Fd2F4wt72abHJh9hDHGUDva4TeLhcRafsLHY8yiDDSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqE6BXTwIOt1mZhetMmCaN85mlv-YqBF15mQ5HvAePYO69PUqwAAY9Nsus6dI9_BTPCAILqN2nUsO7osx47AzLs-QIv8kgcxQ6Ewk2gLRNcbMFDSlwygaN1aZsei8pD72l2BcgyrzrvjJKY5ECw8X_hDrlCtljdXkkJ0Iv3sdg0u0NCaB8VAllbSQeYY4hpv4aFRGhfxfKeNpAhbFFmNMoKoWIDeyQtoByaWp5F-THefjoT-_wVnkmahMkDTy9ZqzVRcSQ_xjUjOHUD3ts8vHR76dv9AtqF9s1NQXOUACZ95bcN3sEG4YC4uq-r32QfRanHBVW7SkzQmw7T1UdG32w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYDaIVjob9FVHn_AMRHbwuCYt1-Wg5GS0_Qod7Bnb7xRGGf3ULcnzyVM3aZgs3iGcjbHJKg7EHjp-eYFkhcO028S81vcxuuUjpaXgR78Ff-Jynrjo2UW3Vd09xpk2oTyzsxvTTumJ7aGdttnYwSWt-w8E6k90XhDuws1Q-ZC1U8bSxP0na622T6dtY_2UsTzK4fJ9D2JAVcklIEHM2Idq2xZAz0lrXrXwCDU_Nt6YXp-H_OMoiAo5SNPL3IQ_PzIy-iZdc1XjLeG2gP89On9ow2DnI5iK9J3v9egRFblcnAYdqhtibd7n2sGCD05AVvZCls1OKzwaCsGMX5CQm45IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVnHdD6Vw6OxLdMwKQ8fLWQkmdQYCIz1NS8NPbsXMJgpPjGu8OCW2xvs7sTdjRp8wAirAQ4TTxfA1Ov5VfFjG7_K-_ewzU8t-36C7HRwOFDvJKH8zVbUOoD5Gzu3_lXwDAciW7HlNsZEnmLKCOWhExUgjvnrDydfi5Bmwf_N7CurnA4n1vM3XdfpQh9tkOuDkakMA8vLPnJIYARGDXyAmngiGreuwi2M3pDkQyZIIt0xgj0zj8Grd8iVsk3m7R3rFdZBV6DClr6O6V9I9bTYAGvxBzm1xhkN6pq1fmL9A5HGGM6ugZ-r2CqBW8WYTq1IG9biP6tchldXRVXvIF0C0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZ9d1NHrsf_8bd6foWRYLShSF0Q0qc-c5k_ewOsZEO-tdhGUIG211rmZYuppOSpDadrgcid9mT48L0C1UHHR2HEAzpFVFLqqXrrdj2rosCFMiDBFmhMJMHCgPOi1eeHSt7yBRO5LinT7JTs-7o9a6-4hEJluP2Z42b94vCVHAvkWWAetN0hte60jCAGtmVbZuA98s5z7rZoNWRO74dew3xzw99vrkjh_pV790U8r3R1XLfrOMS2HJU5CfyrAcOtD69wbfVbm4rx04TjcMs0hxsNlMuRQFVgqwyLsPZdV2dsCBNr34JakQOOGVXNIBGKCBHs5fplwiAyNgqwv2YAU_w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=fkVY5tdSLynOsVsIHY9p3h3_o2hdfRS55UjND_Pwtk2hIr8ySORdDMXN9BkePZeJsEgbzRWu6hEIcNBpVHvYnGl9GQJ3NPMIp0ZlfoXbPRszA_NW-g6DwzBpS0QOKBLKCqzFCcxRMlF8x4Nc00KSuDSNEWDUpn8nvsGcITTXunA2eSrFJ5tmkq4RcG0BygZOCOpjxx4djCDscp1AjcicvvVE5-Lrp5veDUt6mGNXPCcj6f9GdK-DcLKdp1G1fxc-u7VyCwbEE9bBgVAdmOptS17QzDLjSIORMQE3Q6tckKxbMTLinc1Qw4DG11KHQOiJCJ80dF7TqaoXi154G44BwxiqX1SYYeQitUxTcMyZl5hPIMDvlYYYtf0CG3VeAD9gB5m1Q3HLrDHuEp2_zz4Yhnyrkx7guYtHXNJjajkkFWHTCqLLhMZ7BC-v2h9zVQuuHsEbblLyTm2ZL-fpn5z3UbjroOcYyr3hinxGgsi5hvQV9GISUKfd_LdXAdPKyqOAdshpeLckbib1o8Rw2ShqYeuh7AUWowWM2zKluV4KR6FdS9YWbJWqiuIQp6DNnilplhTn5rjreuvi8JJP81fdyWLWrgQUO23KG8sg7whl6MuA5WDWeZDgRqg4kRrHLCcfg_28MpJRrs59iMkRJUkccs1pSEwiH36Lqym6WIZDsJc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=fkVY5tdSLynOsVsIHY9p3h3_o2hdfRS55UjND_Pwtk2hIr8ySORdDMXN9BkePZeJsEgbzRWu6hEIcNBpVHvYnGl9GQJ3NPMIp0ZlfoXbPRszA_NW-g6DwzBpS0QOKBLKCqzFCcxRMlF8x4Nc00KSuDSNEWDUpn8nvsGcITTXunA2eSrFJ5tmkq4RcG0BygZOCOpjxx4djCDscp1AjcicvvVE5-Lrp5veDUt6mGNXPCcj6f9GdK-DcLKdp1G1fxc-u7VyCwbEE9bBgVAdmOptS17QzDLjSIORMQE3Q6tckKxbMTLinc1Qw4DG11KHQOiJCJ80dF7TqaoXi154G44BwxiqX1SYYeQitUxTcMyZl5hPIMDvlYYYtf0CG3VeAD9gB5m1Q3HLrDHuEp2_zz4Yhnyrkx7guYtHXNJjajkkFWHTCqLLhMZ7BC-v2h9zVQuuHsEbblLyTm2ZL-fpn5z3UbjroOcYyr3hinxGgsi5hvQV9GISUKfd_LdXAdPKyqOAdshpeLckbib1o8Rw2ShqYeuh7AUWowWM2zKluV4KR6FdS9YWbJWqiuIQp6DNnilplhTn5rjreuvi8JJP81fdyWLWrgQUO23KG8sg7whl6MuA5WDWeZDgRqg4kRrHLCcfg_28MpJRrs59iMkRJUkccs1pSEwiH36Lqym6WIZDsJc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=dVe3CIZOd3ymDUDpITPNRxxqNuDwQTOCT1HAmeW3JqS_S9R0EeR2lUVlNlMFqWDLZ7PwZ-ZMxW2cQAoxbwZG7lTedRNRfSImziIEd7_BYAyJC4rONG0MZV-u8-wo3z1Aws6uxsxOK-FjzEdwWVQj4i4mjrJpKsSzEXw9TIPAFA_mKoFwPEJOWd_UZunU-A5qq_NV0CGixL0k1ggpZNlW5tk3UtFi37GoAVZF6blHBK2nFozJOuEqkc6Cp4Bo_MnpLqiW_0y-GCgUe-MgmPRUZn-1wbcAKhtCBNYIzqz_jPwumqt5wiuslqUfSYsSAWyg8u6P4KKLW10zgTwEk5mviQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=dVe3CIZOd3ymDUDpITPNRxxqNuDwQTOCT1HAmeW3JqS_S9R0EeR2lUVlNlMFqWDLZ7PwZ-ZMxW2cQAoxbwZG7lTedRNRfSImziIEd7_BYAyJC4rONG0MZV-u8-wo3z1Aws6uxsxOK-FjzEdwWVQj4i4mjrJpKsSzEXw9TIPAFA_mKoFwPEJOWd_UZunU-A5qq_NV0CGixL0k1ggpZNlW5tk3UtFi37GoAVZF6blHBK2nFozJOuEqkc6Cp4Bo_MnpLqiW_0y-GCgUe-MgmPRUZn-1wbcAKhtCBNYIzqz_jPwumqt5wiuslqUfSYsSAWyg8u6P4KKLW10zgTwEk5mviQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UriO3xoBjk5hTp1rDJ7ND_HQt-zHUiCsdanN_lsMn6tpwBy8LxYFVCbeDisjfEnjDehaIwB-BjXuPZOeLR6iMfpUnyWAuddVZNZdvSQhXL7E3mMej-GVIRNujYTB7J9L3yVPKaLjbu1ndzbn_GIcNoHEZIDqqZoUiPr5Be7ZAj7I7C2gzKSr-I37TUmDb7N9_MIjPxQBd01rPi3BVdXO9rocaiBfoqNjC6pYJuQq4_iP98tnEkJ9brJgFhI_NhBcepDKrhnUbZgydtAXhhMGUfPnsr1hMfe1ehupBSxrewz_aoinyOZtGb6YNHmnoBU00hWhvOH46AC4-P314VtjwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4-gZ5b0ovkPbmSG-x7nLI80tzhIFCwML_P3_9k7FFpYBmo6_ujSa8nxq12FetvGhgpA5nfmKOo2qdyUSSlUpOUAJgPBS-dLc_siAR5NQ8OnjPa_8DoxcD7FB9_e2vLRlP4rKrXrNGYGhCE3NPSl8WzOtYL-7yz01f-xWcj22r3-IIo_nTfc0plqVzjB5Ixl7jW8Fcvh79apzheN7Od0MsgiauY2FpowdGpk_bybKXZ5YaEKtscqaVgLmpTIJSj1WYE8HP56A4YHUn3_f-hOJk7LFlCfIT07KAY4hQFQye88lu65XkCdw4B6rEKUOiTWgOXGUskzlskqyO2BKM5GLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=HLj3C_zdOByIKajX82eSha9V5TGrUWPgFeDMel2rsipLZp85UeAhaLjrx6YFGgOXz88bDBmxrBjf-tI6Sd2vdsxNHvTyEiej3W_qwtb_aBXmvPC-K7PH2dJ58KjX15msZhLhVmiteoO5h_z3Kwlrjudn315RFqthQ_yHJXPbZpLtT7uEOz7v5Ea2YjTLKukNeMsc4FsSRIF6ZaVXktAbs4Jv3XZdGQsX6wq75gMXo7Cad_4Q-7pbj65xdrWw0E4DOlXRbk-Y70xWH9YoEn4WgFvDBwVNyQ3tPZFpFe4X7ID7F1sz8B3KT30QJlyBOC9YXEDJ12zgH_w8EIKr1iyGPzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=HLj3C_zdOByIKajX82eSha9V5TGrUWPgFeDMel2rsipLZp85UeAhaLjrx6YFGgOXz88bDBmxrBjf-tI6Sd2vdsxNHvTyEiej3W_qwtb_aBXmvPC-K7PH2dJ58KjX15msZhLhVmiteoO5h_z3Kwlrjudn315RFqthQ_yHJXPbZpLtT7uEOz7v5Ea2YjTLKukNeMsc4FsSRIF6ZaVXktAbs4Jv3XZdGQsX6wq75gMXo7Cad_4Q-7pbj65xdrWw0E4DOlXRbk-Y70xWH9YoEn4WgFvDBwVNyQ3tPZFpFe4X7ID7F1sz8B3KT30QJlyBOC9YXEDJ12zgH_w8EIKr1iyGPzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfxOYYkz8_Cox3_E4jm-VNSc6xRFcNzDEu9390sJsos5qc2Qm4KMKxPAkhhwT9wXECmPI-aLbByPY0ZWQyMR9Ek1ggcsFmCu69GmJfUpQmCXFtPkDoMoQ30U7ET8VxR4KIoNn9tVghSqfMrP7g_3ObzHaenQSXqAx1gFTwtdnoZs76wBrG86tAEdRMvCAxtepdAOjQbUMZCm3XiPrM8cvH_yJ9Gnu3QMfmph38_Z_7nAYd_W2kNsPW6FLwITRxxcBVKpiYoqCp-H37xujLO-DpP8NxONqWJvT-15yUvXFmbfjxaccyEY5aWICsniqXXO_jLKKfNVYqR7V4VeQa8uXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vc0OkvddhF-UUmp9NtzyE8MC2eQE1X1OPobi192HEp4uujj7PXHeSsSPoqDGFIaDfVkN9SbkhXn4gzkcRZSIGKDkL-Ak0ARcvHpYF9EiateomerGLJxDF5uh2KRfwKEk_Me9l7NQCfbFwq80qs6522fe0vrWWdzC1nCq07UUEBqsbDogIy2VaUqs6D9K2HFsfDDgv6DQ0D8y_SITSSnPhIKE56V-paofLu3uz1svHKlcaEC4hFv8-PjRvdAZ1Q9V_1y4Aq1xFdpfI7moWaTsrNRJXEr5TLssvK6hwB1kjXVJjUV6V3w5Gy4pE3niQjTw1fT4btigqpMsPIrWpKX9gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efX3ZIabGNMrCXP2xXvB6zxPzHL_3H94Ev0_EI3PLrdjIUXuQnn2uZDvX1ShdD5swW1WChtHvXd1JgJLetug5a8UOTPI2YdQzBSg3lEd31YmjsW0QoifF8hf11FrccpmrfnxgWJT_p2MRrJ-fvScJerKznY6of2_TbayYvxQW5OVMt33ORWoDHmwc04sK3pckWKut9B84jIXP23_p7Y_tAVGJO3sb5Cnb6J1pwlCtrOYYuugmv5iDyrsFeapMjYb2dwAjYhWmmz7h8CCWqsxnzHiJyJpXSEy9wgKchzTW1E3oznqJOjA6C8mt9S4n1ijO9NLhcx2zJYjw0yHDKGysw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmaLNRGAP6OWFNCYc4DHwuLCxVA7X4Kl9VYsV0RGa63Wu7JtlFNfsCQDBaVyDSXGAODU4Ag7wcZQwkPIq9uQX8AhNM_T-SJdAYa1JZY9G4DHEFPRmm72ELcH1j8QAKB2Uvj8e6tbP0N1lxwR0X0occieRtMIGU21YOS-dkZSECJA5bdtnp0s1GOZbtPrWRJeIKvPGOvxvjasANGMx3NUj2hvSwbjsoImCfTPjQzi0D1xoYF0dntUZjuJXMY-MpFwryTQhzDEErWbsBb4RNfkavBOGixe3MZTFN6choCe3wIQt4wKJR5K6jS4xaVejYqijUWitTNMUFP827D8a7P2Cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCZ9umlfdrHUWO8j9hWFLJES9XfTTEbV_1b9Kp8k0p6HrctALaGcVPtFhFDgoREV-v2-SgHlouQj3ZIJc9Dch632PLl3URPKNksM-VbZ0TbbR23QMiJX2M753u2IvaLr0NpTY536ecvmPGcWgeH07yHqEZtP3K5AbfVVSXeMraeVzlGRg4MqryrSKlq4g63MZp3d9XdNi24-FJIszIak-jCL2IMrLee24oljS1XUekOulyoov6MS6OamVXaBEyjf58JzzyYXk6mVS76CfyGlVaG2Df7cBss8YPoH-PnMOGrkxhYXE3T8XLgGnywJ-HDMQn09Ghv-nwCTBhwZMjnkxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJb8oUPf9BHOsypij8oJSkUo4dPhXWI78AxWym6rmQ_oNeaTBRWIh-pnRVzr4Dfu-fbuVm2cC-y5nTTggXqGZDDk9dqVZ0fHjPjEtwWZG1aLAPZlMTqXmGGzkWE7SUvJl4GBwYGkBf8H4Rs0f47zxuolrAQNb5V5jAed6_ljdkyyGN_fYtT2ABRYg2ITSUH_XrN_SWfXm0gSQStUBqow4ALvtn034tHmn3ONf_0mt7pSqwINHeYFcAVZSrauoBayAPUd82LHcuvc4Upzp2-U0XD_51ygPuZfv7C4RYc7qzn1RoJ46M7Wg44eIOi3sxss187FhmnnwPIZ32ZL6k5HBv1Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJb8oUPf9BHOsypij8oJSkUo4dPhXWI78AxWym6rmQ_oNeaTBRWIh-pnRVzr4Dfu-fbuVm2cC-y5nTTggXqGZDDk9dqVZ0fHjPjEtwWZG1aLAPZlMTqXmGGzkWE7SUvJl4GBwYGkBf8H4Rs0f47zxuolrAQNb5V5jAed6_ljdkyyGN_fYtT2ABRYg2ITSUH_XrN_SWfXm0gSQStUBqow4ALvtn034tHmn3ONf_0mt7pSqwINHeYFcAVZSrauoBayAPUd82LHcuvc4Upzp2-U0XD_51ygPuZfv7C4RYc7qzn1RoJ46M7Wg44eIOi3sxss187FhmnnwPIZ32ZL6k5HBv1Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRf0mJqxCbkQU96vRiLNUi3XcClFXwWLtQv8eJRco0dzyQ1RFdYezXiFab-I4nkhOIE4J_G-pfEraw-T8TraD0k1RdgmhhuauDx16yTtOStoWrqsJmpXoxutenRt3GBVU_CcEm9EAMmfw9gPPWpy-RyaF9hTQEsQFUB6TfZMaURJEOc4y_eVaMsQVgklkfQA873m0ceL3OgmqYZ33bNVZNyB0GCL6LZzAEvBXWlQ90m2NTb-JNth7Reib3G0GpFzyXLWjws0DAgvvCU8pcPkpuQ6NHHfpU70pJdl_xEjlRQhv97b4odKUFbQMX6jnTxjgTyuebpjfS7RVkYt6YbmBeuHI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRf0mJqxCbkQU96vRiLNUi3XcClFXwWLtQv8eJRco0dzyQ1RFdYezXiFab-I4nkhOIE4J_G-pfEraw-T8TraD0k1RdgmhhuauDx16yTtOStoWrqsJmpXoxutenRt3GBVU_CcEm9EAMmfw9gPPWpy-RyaF9hTQEsQFUB6TfZMaURJEOc4y_eVaMsQVgklkfQA873m0ceL3OgmqYZ33bNVZNyB0GCL6LZzAEvBXWlQ90m2NTb-JNth7Reib3G0GpFzyXLWjws0DAgvvCU8pcPkpuQ6NHHfpU70pJdl_xEjlRQhv97b4odKUFbQMX6jnTxjgTyuebpjfS7RVkYt6YbmBeuHI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=c2j3WfY1HZ340n3l5yoen8XZ78AJ1-XZ5bZxVG7aMjUyCAm2gOw-3uXYOXF70GHYrS-q0hbPHwaQtdjC1vpeIa2NjfEnY20ChFwzFAyv6w7hFMzz6-EqzUiB3C4wE5X0LeFgzVMQ5PaetxzVRr9O1l-CuMyXeqJksvYZSsJi9dGWKo-oX6amM4OWFkcpzBsr0djSkrY6FxPOGFCVCE_00J7ZQhm0rrpVz_SdTUBe6iBJgaJn7mvkDrOFFzd-7L3EZClcmgllWtipUhJ07wTsvpR5CVu7IdAfpTPPYf2Tgpmh4_8wsJWZP4g5fCm_q6M58A9HJJRcZ0dEVNPmz1hEMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=c2j3WfY1HZ340n3l5yoen8XZ78AJ1-XZ5bZxVG7aMjUyCAm2gOw-3uXYOXF70GHYrS-q0hbPHwaQtdjC1vpeIa2NjfEnY20ChFwzFAyv6w7hFMzz6-EqzUiB3C4wE5X0LeFgzVMQ5PaetxzVRr9O1l-CuMyXeqJksvYZSsJi9dGWKo-oX6amM4OWFkcpzBsr0djSkrY6FxPOGFCVCE_00J7ZQhm0rrpVz_SdTUBe6iBJgaJn7mvkDrOFFzd-7L3EZClcmgllWtipUhJ07wTsvpR5CVu7IdAfpTPPYf2Tgpmh4_8wsJWZP4g5fCm_q6M58A9HJJRcZ0dEVNPmz1hEMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEgmcGazuPveeW3VozWGHzm73dJfB7yAYV0cTdR05gtqJ6kUv8QIkk4Vv65de5tzehqjtcGH5t6f3TPMJnbV9bjH5nSkUQtkGJXuSH6x8h6jidNluwV1fJmTTLQvaE5U6IK1T7iaeNzcdsaCF12q2-Sr8L5ALIKag68IpGVnbWUAtN-3u-cmjx_Xdqt2cuIY2XcjOXJSIw4SmJmdYow4MwmmdR4eBDNzeUET_USiyFCPITA70-Hygh12OEeufwFOTjjdWaqV1iUfFaZI_m2gdi3dDiEQrSKCS4qNGgKDflr3zz9HJrRshX8basl7iP9OL3HvGuDxzf9F7d7Bb_gCxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cz10rS3PvvWpbYkYqnYNMNX2aJpoGNwcVv9v4mCzXPHofUjOobZ0ia1foUr-FdqSGP5eKHSWn5Xl5HDRrAbBousgvIyokWoX3zrIaodY9SEaWtk1259ViRGsXLrRKtK2SlRUiuyiuRQeYqO56Ye32b1AcIO_TxI5OWmRTPrTMAyjI6XD6SOugOG6TBw7AkA7bqqRQzunsuTvR4zWu9Vpfn1T_Mytti0j8ESqI0U_NqDW6QwLNhlCUeYKAYL2bo6LXbEWSaDggLCj33_-rc4uW7oQ9fqVr6g9WBMiPZyxzGEh4xRMs2VoIzKmw3i9XU2yGqZjVpT4PBUnwgCgYd6iBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=NzD2RS9vlurlg48p3MCpuY08-mt4fkDV0L5UO85LwWfmcrdv_ZQMXa2qL1yQAuWSQKKgrUH5oFlcAdP7-Xlsg7mtZDVLQTc_5QyDFPetvuTocoLO4EPJkWEGaKovn9rgaFc3SDncZfpOj_SiFS0QUAHpZoEy8_y76CVooiOSVmTDSxLm_7DwWiKHHvDkrppQzpviu5FE30a94gEbqPJ3wZQa4t1u__wFMmzNEfC8T_3TEHi8ytMbyZGkd1DeOCyZwT8ic7V4Z4tIGCPq6FZWrjfmYlLUJ5g0cd9qZljfXy73eYGyW4_dh7gWH7YJ3hS0A2UagGLBlBCzwKp0kvX6Cmyw9uInXDLDXEucBEbN3AbaqE9_fRgSvQNbBvB9N8GInqulrUZ1f98Ko25Ve_xn-JOQn98EStet7b_JfuMbVZ_IjLyZUGisLHRpGvlLz6Ydd5h9mNuEcOI1P9miCUAurvSUWSYDs7-IcuEfsnmpPpNwIlwmDtHrSDikZ6D12b8y0JA_ZjMV7RYbkljCZtHbT_A2iRnJaR5fw5DyhPfkVLiVhwbiQjNoSyk9jTZDMqdVWFLkILCAHoN59ORAFav_FY6GKx_6CgxcLpD5L04hdV_EFmMxAfCYqlnDpe6gHgGeQ-ko_RRzWUy6Hebt2lJDC2XbLDy0TKDzZ6drY7oxcis" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=NzD2RS9vlurlg48p3MCpuY08-mt4fkDV0L5UO85LwWfmcrdv_ZQMXa2qL1yQAuWSQKKgrUH5oFlcAdP7-Xlsg7mtZDVLQTc_5QyDFPetvuTocoLO4EPJkWEGaKovn9rgaFc3SDncZfpOj_SiFS0QUAHpZoEy8_y76CVooiOSVmTDSxLm_7DwWiKHHvDkrppQzpviu5FE30a94gEbqPJ3wZQa4t1u__wFMmzNEfC8T_3TEHi8ytMbyZGkd1DeOCyZwT8ic7V4Z4tIGCPq6FZWrjfmYlLUJ5g0cd9qZljfXy73eYGyW4_dh7gWH7YJ3hS0A2UagGLBlBCzwKp0kvX6Cmyw9uInXDLDXEucBEbN3AbaqE9_fRgSvQNbBvB9N8GInqulrUZ1f98Ko25Ve_xn-JOQn98EStet7b_JfuMbVZ_IjLyZUGisLHRpGvlLz6Ydd5h9mNuEcOI1P9miCUAurvSUWSYDs7-IcuEfsnmpPpNwIlwmDtHrSDikZ6D12b8y0JA_ZjMV7RYbkljCZtHbT_A2iRnJaR5fw5DyhPfkVLiVhwbiQjNoSyk9jTZDMqdVWFLkILCAHoN59ORAFav_FY6GKx_6CgxcLpD5L04hdV_EFmMxAfCYqlnDpe6gHgGeQ-ko_RRzWUy6Hebt2lJDC2XbLDy0TKDzZ6drY7oxcis" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=rxFBzU69vCmcOxvEFKpnVNuhTc7hBR287dg2NHkho-TjJeRSGFY4mWQ-FwBfMsiRIZ4D0q0YYgN91Nawvyl3ND25YrUl5B_QLXGDORWus_x194Dctje325UvFwDfJtW-YebkNLS2bzn_rCjLVWohi4dfT_1FglGrzGt_EoJxXDND6il0Xr1RUquIq4Y3W0xoKXYsbPNOfW024yiC121PwoC9v27OH_fQohQeUME65k26-8nGgKv2S-Wil6kRXl-bYUZ_-U4ZXtz_AHsQavcOp4mTw-mVK5cGGzKNdUjoLrlK0p-LpySXfwHmktD7JRpUCm1zf50oaqBqzBQcqPeZBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=rxFBzU69vCmcOxvEFKpnVNuhTc7hBR287dg2NHkho-TjJeRSGFY4mWQ-FwBfMsiRIZ4D0q0YYgN91Nawvyl3ND25YrUl5B_QLXGDORWus_x194Dctje325UvFwDfJtW-YebkNLS2bzn_rCjLVWohi4dfT_1FglGrzGt_EoJxXDND6il0Xr1RUquIq4Y3W0xoKXYsbPNOfW024yiC121PwoC9v27OH_fQohQeUME65k26-8nGgKv2S-Wil6kRXl-bYUZ_-U4ZXtz_AHsQavcOp4mTw-mVK5cGGzKNdUjoLrlK0p-LpySXfwHmktD7JRpUCm1zf50oaqBqzBQcqPeZBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3noUEPbS9mOkW3Lv34lyqIfnKA3RpttVxzplhHf74ed3IHq9dM9vAbFv4d8vV2_Pz_bIHRA4Iz5Nx2mO9SPprIt1Wbi-4AtcTF8jmYSHNNg_pSXOEzKt2VvJkRppHqISZrUxai7m7JqKFvgnhdxj9E9l1CKYmdoUJIDKA6GJV3nGGk1h5K7S6VUcp7N1KXJltSjmM9ija4n_jNiIXnuOhm-biO97WVat0QvKFnmRrA1qCdCE3vjT12Cu6sHWLRnIB0sonY33V_a_KCWT1Wudgm9EdvncOumPyxMaPYYorgWeaU05Jmjhtav59ZgmNcqMzX397EjDUcvKTPaldKAXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2fyTtQmod-iEPmpCMe-skqf7RHpIW85iY0aOvnnbf7hR3EXs4KFtgjHvaoA64_LbWBWWPTeTMcLXCkLp_u92KkjvCXG0CfdoUilnzzdum9_39Ijdj-Yx2XKNGtDWBMp3d_bAgVPGMRT5rZsFC2Ax2v33a7kD3IR6tMNgGlKAYT_n5_XTQs2GMGbYMwBW7F1fbQqFv-9QrRkHSSChIokafjyZ8jurWaYbcf77Ckf5qytyxfeOE0CclItuE_J9juJpOoPVeoEaHEZ6BEXBTMSZuCTx0-aT8Z9F-o2cM8VQ6_8DACGVJyhtXnMY8tb3e_SmJxIcaEr4CpfbdaoWzVWLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bCfjlky0_Pv4uELqCcC1qT6NQykGEW651PWRTnFKjkKwHCUAG314LzAXl7tKW7SbgawHc5ls-jeZkf5i8vZLoaQEE2AXmE5aIjgv4ZwMOBRMv2z-tUvEwnbtVKVR21zJk3lRFWxqP4rpjgxeb96eaIpN5Y1DZctFViPnPSusjtcNCMA4zyOOb7UjlmASuI5tzVThqUVipyYsyAyvF2VONU6nu5TCKEjpHgZJWUDhimi3DW3G0OWJGC_K3i_jti_3y1vYdyNRHBiOCATqVYMlsN67igkbAW2LhXcl9nQTf0Vw6NqHxSDqeSLFclHPtbTzXhYpFRiNm3Lo2hiQtXj39g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=F3tYX91VPwdUUwWtYMYTS_eAIrnXaj1PDOEoIzzD0fJtwtjK33t_IVWUI3sDHWximnwcuhp6KkehrMMnxhLeU5-F-tO_qWYTLjSdNecj5p_PbxP4Iw-_srRdsT6NJFNpL3boFP7p4OP_qWxLyP_YxoLcmeVjiiLN6ptiG0WMvEXqocl7BOHpeqEBAJLC8d5xfrTqSvgINmWgj1N-cm96Xh0JDXU7OKwFJ8EzjYBnJsjVITAJPWvhvMWDFvqFg0X39jdcwb5oFFYU5oOOgK2lZHR5Rlq81hcu5Ikr219fvEvU_ZHmpIZAKajTB1eAhL2Yh9bcbOqYR7Mu8tjF3mtJYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=F3tYX91VPwdUUwWtYMYTS_eAIrnXaj1PDOEoIzzD0fJtwtjK33t_IVWUI3sDHWximnwcuhp6KkehrMMnxhLeU5-F-tO_qWYTLjSdNecj5p_PbxP4Iw-_srRdsT6NJFNpL3boFP7p4OP_qWxLyP_YxoLcmeVjiiLN6ptiG0WMvEXqocl7BOHpeqEBAJLC8d5xfrTqSvgINmWgj1N-cm96Xh0JDXU7OKwFJ8EzjYBnJsjVITAJPWvhvMWDFvqFg0X39jdcwb5oFFYU5oOOgK2lZHR5Rlq81hcu5Ikr219fvEvU_ZHmpIZAKajTB1eAhL2Yh9bcbOqYR7Mu8tjF3mtJYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=b9fnp2KPb9Nhsdvi-Ea15DyaYT5rx9auUH4SsybKbIEEd4aC6DNxaJHlpOgGgiOTJ-bEnJn2-87Vg93GDu3XZDxjhl6IpbJyROFOTL--7sQD3atMhxSwwCsVMQhg45siSXJZbdqt33mUVo7hjZBXbtz8-k4HiCftJA27ib7wXWiLZTCsiK8YmXHFZsun5fjUA9odfO7G8slQZWTQJ5l6fTF-nOS-IUoiSD8h8DrxAM9N86guUrLvxfjOOFqgYh8sUwJT99HGlpXeSFpBje0XdV-AgIQ3xzUKOY9m3zNob9aWRO-UsdH4tOfYf_DvhOOyXejHnF-TGqHYfsbr22hpkrAda5i_PfA0uDyQKFe_AuJmSSg_gIgb5ZOOyMnHzj-EGFntFAs-QuCw_6Nug93T_8SxtSmWljcSHSKCUE2Uxk2HwKqeAKfW2HOTBG783eIKnbddNSPexQS4gp9GoWiNnUL071HPFiAothTPGic9mV2u7YhAWxIeDBOc8ihXu5sr01B6t8mdhZ1b5pz79f5XRNsBTsuo3hgIP88XGeU3qk00lrrOskn0mfZzVR9SO5IqaYJ9BrXS5PyYI2PU-6ktYx_u4z7IrHxrhk8R-MfjQgbFm4EuvtX-BiZWehTUjcj545y_d264CTz2hTg8uDW2gKouNgZAtNS9wmV5cyOS1mI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=b9fnp2KPb9Nhsdvi-Ea15DyaYT5rx9auUH4SsybKbIEEd4aC6DNxaJHlpOgGgiOTJ-bEnJn2-87Vg93GDu3XZDxjhl6IpbJyROFOTL--7sQD3atMhxSwwCsVMQhg45siSXJZbdqt33mUVo7hjZBXbtz8-k4HiCftJA27ib7wXWiLZTCsiK8YmXHFZsun5fjUA9odfO7G8slQZWTQJ5l6fTF-nOS-IUoiSD8h8DrxAM9N86guUrLvxfjOOFqgYh8sUwJT99HGlpXeSFpBje0XdV-AgIQ3xzUKOY9m3zNob9aWRO-UsdH4tOfYf_DvhOOyXejHnF-TGqHYfsbr22hpkrAda5i_PfA0uDyQKFe_AuJmSSg_gIgb5ZOOyMnHzj-EGFntFAs-QuCw_6Nug93T_8SxtSmWljcSHSKCUE2Uxk2HwKqeAKfW2HOTBG783eIKnbddNSPexQS4gp9GoWiNnUL071HPFiAothTPGic9mV2u7YhAWxIeDBOc8ihXu5sr01B6t8mdhZ1b5pz79f5XRNsBTsuo3hgIP88XGeU3qk00lrrOskn0mfZzVR9SO5IqaYJ9BrXS5PyYI2PU-6ktYx_u4z7IrHxrhk8R-MfjQgbFm4EuvtX-BiZWehTUjcj545y_d264CTz2hTg8uDW2gKouNgZAtNS9wmV5cyOS1mI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjW4NPKkbT540SBE1yOBVeF7U0GH1LXwnvvWEqOm4j33TMoNw3zTwRIHi9uo-5zLx3f1W1O3kt9-WOLIHQ6O5VIQCSYw3G1C5o0QKDFPQhGs9on588AnFxSkA1RWUi6rSe9aWGuj1EhsROMbXJO7UDa3-BmgpbRneArgX-5fyk2f0wyVUM-xiYlIwcwENqNMrWnDZtTHONVXwvT1Fno8ZJGFEej3ak10VGz3ylyV9mWiiSjPZ5PRjPMSkPU72lTXZ9QW9VrwSuM0Elh3H1UQ8ECkB_CmXS2qarK_gU72hUV2qWm7KoKhGtVJCUqdrBgZ-SNU9xppJn2ySsNgFb7-qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رهبر شیعه، هر دو مبارز علیه آمریکا،
هر دو حامی سرسخت فلسطین
هر دو خود را پیرو مکتب حسین معرفی میکنن،
هر دو اتفاقا دشمن پهلوی،
هر دو هم در غیبت به سر می‌برن
و پیروانشون در انتظار ظهور!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6424" target="_blank">📅 14:27 · 08 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlLV1E1b5Mpa8orddzXLMimRox9G5O1EGi4dRSRf5NASqCs27wO80pIC4ZFHkvIOGrsRZa29Pbi2e4Y18UYGRA8nIXdo9G-LQthcQJY1J5XTHglbT9b7VKmdtfQyvSFibFmRjH_uN-VAKUA8JtRSaIFFrPAc_XJoRN8wD3XnWaS5aDKxdFTAilL0VuG6KKMahvzhYQeEoU1kHAiX_nk3Gg1lH5MNEFkE5my8RhAdhnMhKM6dzLW_HjEXoskqgbdmeLgJCne33I176YuMCJLiPPO4K08UVfD-CAuFMcD5KDDexXVUgJF--borxUIQvK3V5yfYHqobObHQkdH2tOz6Ig.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=FIhrsysj5-am9AQdqesm0DNRw9DCkQRvTeBbq-3l_Je0EPetHjFBR0yQROmd4RsuOKTSUNqebJoJJQrOeLN2Wq2YqZA2NyP13RnqUgPKism34S2V5oO-d-HjfW9C92N5u1z6RPDRyYOhiA3LO3X1p9ypW4H-YSZ9SNJUzXEHirdw2Ir5MUrGrJIpCuRgg71joFPDqz6FhOkf--KWkkYC075BhCR1u0SBPnm3fNwDlrreBOHs8w6CFXJpuqH8n2_HeS5cAk4qBSg_NtIWR7_qgKRmI7sJug2h74FgzsOpCjp7zRFMUokYLPnnNsorK70N4sik_2ekIFxYU_BKzLE6kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dca15fd7a.mp4?token=FIhrsysj5-am9AQdqesm0DNRw9DCkQRvTeBbq-3l_Je0EPetHjFBR0yQROmd4RsuOKTSUNqebJoJJQrOeLN2Wq2YqZA2NyP13RnqUgPKism34S2V5oO-d-HjfW9C92N5u1z6RPDRyYOhiA3LO3X1p9ypW4H-YSZ9SNJUzXEHirdw2Ir5MUrGrJIpCuRgg71joFPDqz6FhOkf--KWkkYC075BhCR1u0SBPnm3fNwDlrreBOHs8w6CFXJpuqH8n2_HeS5cAk4qBSg_NtIWR7_qgKRmI7sJug2h74FgzsOpCjp7zRFMUokYLPnnNsorK70N4sik_2ekIFxYU_BKzLE6kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcTmWTva_xm3KGh-lwxVTG7LIx0vA6z4FA_lj7A3KS6sEoAiha_LFPngDVoxpYiID1nMByGrnnMHq4Uhh7HytlmBD30iApcCTzU1C5oUZ6AkdwTeiAGyihly7RRMDd73CYRE_VEjDlPb2PNagFQzF_2tXPA10irYZa_-0bAnUqPRuHT53iot_CFkApNsWwZ4daFAae6GpkK2DPUh4gJfCRFHJ6hZZtqJnaxWligpprG1Lf97jEZLWeGV_l_2GUI9rVPdfwPR2ypugPpZ_Qb9Jiaj9wLevMdHZp72zIfZ3jkDS6ZOBAwngV9DV7cWQE2Aw1OV15uO0uqPmNjPsemywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دیروز جمهوری اسلامی با پهپاد به دو کشتی حامل گاز مایع در مصر حمله کرد.
امروز دو تن از مقامات جمهوری اسلامی به روزنامه نیویورک تایمز گفتند که این فقط یک هشدار بود.
(که علاوه بر تنگه هرمز و باب‌المندب،
می‌تونیم در مصر و کانال سوئز هم تاثیرگذار باشیم)
🔺
صبح امروز هم سپاه بیانیه‌ای صادر کرد و از حمله به دو کشتی در تنگه هرمز خبر داد که قصد داشتند از طریق آب‌های ساحلی عمان از تنگه عبور کنند.
🔺
دیروز صبح هم به سه کشتی در تنگه هزمز حمله کردند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6419" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6418">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvZJQGUZOo_q8WCYBBHdWJF_iKsMTehKEhrVeCtZMyy7KNzSIBbc6zHNBD4cFbobtRg6r2C1H3UJz1Mpo_EVsMRzXOtgfNurclCpMLE9dL5dNmStk5SCLX_NKMAPKSnWB47x29i6MHfOlatmCeyiyQ12bVjl-hnKj7HJKTl29kLhCWtZT30tuZpdUAPpTwmMF_lbLtxh2gQY-Kh59Fm1BhZ5wJi6MF7vszozp0d-FFwSf_RDPM3ytFawoEZSGRNOR2rR555EwKoiKlRUHZE3_op-VSfor7NZ8d7DpoHxwT23up669BzGkyq-aHO4YlTMt2uLaK5Cn-ynl7HJCwpUzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fbu84mrge-1izY8PN4rflK1SvJWG-jsgEcvvvUlT4Wl4fsDANN_T3xXLOGKapzYhNtdLsE99NQHOxm5K2R41hJG3oc1KtWyLcrdg8NoRRrpswqwAGEoYywBqKNy_hxStwYH4iyWrDBAdCwU-0EK_A8xuHkpnsGBOB_nNM0oYOBFiE7D4UrO2AzE30m5bYST2lf9CmnRPT_KhSYZHPQ5Y4DBnzf2iAws4GUbnb1ChEltSezF8ArMSUONVxZWjOUSfYWIH25MGlTO2ROW0sRdxZn2mH9vmiMy6GrB_ooz1u4jTyjz7inawz_mLsNnOasMYDp4T1VJL6YRsXLpWCSB4ig.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I3VA5RoXe7IELxmRzTOwoQ1WzD8MOG7ljxLu6myGrKw5Dcws2ymsCqZL_fFzfMwUqHW2Tgo3n3lFrEHj0JoZXpqoMHY8L0E_EDZA9Aenxg01yacDCC1zF6pe0xBiVYrdPC64Zl438BSkYJEVxhj8Zv6ZOz0-9to04y48GZHUCCxANbk8Nd-yqBucvoeHUf4cR-cpsdD4cBWWM4YRJrbAvtB4vDB-a_2qiBJ9jjh1kY3BFdEVi_SWW47R_9Se32ZcOmUKlcbIK3JxO84MXToeKcjP9hna-STLtTS4up27PgVEAPgOz_Tofkxd4lkshkVvwSHayWjolkB9tc2OB_CQFnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b85006cf0.mp4?token=XS_tUOrRPbAETX8JRJ9ZmrtScVvT9LXRHWRPwBYG8OvM7DAvLV9d9UIUPwSLOJFbSjdL4nsbqvHNkABvAT0cLQGLfKQLTN-gVfd6U9sa9NdddkocZcrZcpPH_wG2x4NrjzDGXrHWKdcq-fOz7i-wHmZzF8eO2obgpBgCak3yeb1ViFchwdlnILggkgqdlns76Qj4VCJeMPuBCc84I5nudPH6uH7JkHawXFNtaex7T0awcU0yNtUa5PGeL7xfeH8c3HmtvCpW0dp98jGsUp6B1-32xCYONADiQFKlUK97fzb_XNBraI67tCWUJ3DiV8jfNqovmrXq_mXKWsSu8Ky9I3VA5RoXe7IELxmRzTOwoQ1WzD8MOG7ljxLu6myGrKw5Dcws2ymsCqZL_fFzfMwUqHW2Tgo3n3lFrEHj0JoZXpqoMHY8L0E_EDZA9Aenxg01yacDCC1zF6pe0xBiVYrdPC64Zl438BSkYJEVxhj8Zv6ZOz0-9to04y48GZHUCCxANbk8Nd-yqBucvoeHUf4cR-cpsdD4cBWWM4YRJrbAvtB4vDB-a_2qiBJ9jjh1kY3BFdEVi_SWW47R_9Se32ZcOmUKlcbIK3JxO84MXToeKcjP9hna-STLtTS4up27PgVEAPgOz_Tofkxd4lkshkVvwSHayWjolkB9tc2OB_CQFnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسی، طایفه «آل العرعیر» -  غزه</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6414" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6412">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h8nHCU1Ue2PfiS3B1u9gJdeThxL0abjGz8NUHDXQsmasclqiGdoTGvutRuclVOZ9VCxobQY9E3olXNvolTUkJ9VdDKaU_zVmydSl_J42BEo7N3UTkVcern149fT4y5sZEDdNKcSfCZjHKs1mWT97U9IGJSTK0fmcjk1c2Voh7oeNtJ7-uXiZM2Xj3-uk6Xy1wuUZ4c1o-wF0VnSmHoBnlzBwd4z35OHmj9umnw22Oh1-XcujMbh9nn_c8quJe4Vp7F9trWOqow8Gq6tDIPFDB-OCvv2GgjIU-ka5aOi4Uk989g3m7o3OPfclzvtHA5k-5_nTNzkGUbqo0YdiscReEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qGudGaWFS2fTbxOmtT9EEz2F_5vpRotgJRzRs_5m6uEMAINJNdmanzoD8oVaWSJqN7N4Xj2MuL5zdOinoyejrMV6eH2XcxKX4e9VAtnQ37kWoW61OejjRAGfnh0a3AVE9ACf5i353lbp07Fz4_NzbEamXz1GE7a8VEw4cnib3z4xrp5MgX_Q9QKNehslz-vG1wHpuEa6LYcDCuaRsvR8YCE2DrjQQmi7IFNikMIoUaBdlXUhwc72PUNEgq9lMgvnGWu4D2kCPQdHaKwt_qAo8EAbvpANlnQsicQqMl7he0fBsGXp0n-jkLFhJYOlZrWrWMS6IP2z3OD7sG7Zj84y5Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=AfcwXeISP-9D6e8mscWo8jK29mEZz7o-oQ7VnpOuAaAj8WhI_al-Ptv2E54TSyd1G45Z5KcQr3I0DMn-90F8gR5t8ppooPSVobM1zQlO7PFhWQi_NU1az0PWg3c_eUQxYMLhB43jB4TjshbDi4eCsR4xyEda7UAgAgEIlqyvE_-m6Qlg-_MXuk0Ucq0cgHJPgrWiza1aIdd-sRAbBTzLZkuy9R_rMB-z_CGvB7UpUYWS1EVzk9fg7SOSe1HTtg5rrOFdP9DKxdP3vGKltK3IWDIKsKi2XVkDVBc3mzEUPdv2iVq6wxn04sape5tyUI0sRgrW_K4FpG91edti36VH8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=AfcwXeISP-9D6e8mscWo8jK29mEZz7o-oQ7VnpOuAaAj8WhI_al-Ptv2E54TSyd1G45Z5KcQr3I0DMn-90F8gR5t8ppooPSVobM1zQlO7PFhWQi_NU1az0PWg3c_eUQxYMLhB43jB4TjshbDi4eCsR4xyEda7UAgAgEIlqyvE_-m6Qlg-_MXuk0Ucq0cgHJPgrWiza1aIdd-sRAbBTzLZkuy9R_rMB-z_CGvB7UpUYWS1EVzk9fg7SOSe1HTtg5rrOFdP9DKxdP3vGKltK3IWDIKsKi2XVkDVBc3mzEUPdv2iVq6wxn04sape5tyUI0sRgrW_K4FpG91edti36VH8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=Mj1em5Pgy9VKUr9gifMxrMF_o2DNf9QAMHWGR-ReNEcKs2tZ3xfGcV_FQmuIdba_yW9apASnhg_X_iRntP3GBIGcPokMTxBMpHbrIdKBlgnp8iUt-CvtySnRgWAoUX_X2Ffr1IMDyxDBElJLWIdAG-D_t6ScTPlZCjKya_rWAALzbCttfXrjlpBBmtzFmfsTD0PgW5eOkT_8fW3IKpyIoVTZIseLiuevxHPjsVhkO5CW7IZSl9Pqu0aGn00Q1BH34qcKiqB4AtpDnSAPBBKTI3522PNNG8D2OVHIID5xyaHbvahPZX1ESDouQjKBQZIxO-HM2m3kI5-I_cKEJPeeeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=Mj1em5Pgy9VKUr9gifMxrMF_o2DNf9QAMHWGR-ReNEcKs2tZ3xfGcV_FQmuIdba_yW9apASnhg_X_iRntP3GBIGcPokMTxBMpHbrIdKBlgnp8iUt-CvtySnRgWAoUX_X2Ffr1IMDyxDBElJLWIdAG-D_t6ScTPlZCjKya_rWAALzbCttfXrjlpBBmtzFmfsTD0PgW5eOkT_8fW3IKpyIoVTZIseLiuevxHPjsVhkO5CW7IZSl9Pqu0aGn00Q1BH34qcKiqB4AtpDnSAPBBKTI3522PNNG8D2OVHIID5xyaHbvahPZX1ESDouQjKBQZIxO-HM2m3kI5-I_cKEJPeeeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXG3piXWGXdX0uUYj5A1rNO1sKvK8GrkfJSg6VeVqHMZ5FudP-jwybHR-I7yZ6V6SxSEFx_Hb13pJo_wybnKQ-_SGR2VkzZt3NM7J9zXhtga2WKP1uiNBJsOpbY9iGbcNAUodj_YoTLYsXnrMLCZy8DuY1SdikJcZJp-l_H_XawMH_pZ-xBEqy-Z6TfG-Ws_PuWu7vmk9NsagggDsjMmOG_v5LLtHuHYiQt0u2y7qmEptwXqkGMDS1r2E_Hj9IkcElhggHqbXJUG3K0i80Qscwu5zr6xwBFfBmZeqsvA-Uqjm1CaA6Er5qS_xe_tNxcbENTvSVi4cUTx9JPAAEdqEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RA8HDCQhSCRAXlSFNZv1cuIlxwSCUXzbRjn87s1vzJgPRrj_yCL8RWpdHZHdfzlm_t1W-xaV2AfrhE5v5cCrx8LghTW_ws1WSkiVLy55oCgVhCiNQVzXT5Aagaklxkq66Hf37D3yCg2uTJkoW7b5tJ_LDIdR3neSfcvzhYW02wpBGKSI1OPjX0LD6n8Ej9B4rkjAcI_0AB_Cx0Gsm-l69q89Bwju-_yUrX-5561d4q36u3kz2zGZYzDCeB2JbbdNdqSYCOmfZ-nDX_ZRsFLN-WaPIJVTXXDoYIFMtUwyzW-IQ-O914rNbFA6rU3S6R7zaupRIBDhHqtmWg3ZezwgOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=qrdR_3pq-NsFdm8H1RlLpd2WhwMDJNMVLqArFQrR4lBf6v8rrg99ohsT1zjScxWdJpwsEFUt_BKwRo9T3ueppCIQLl9FDmURVTsEKVZS8J7yL4Gh28rPH_-4opH_YcdMUbRI5wggywCl5Bt50TBu9X_ETRZrIucCHm_1Bw3VMQqedWTSsT6QUxkE7tEoEjFuKIfmzvRm_VFs78mHPdxmMwAaZiNXavjk6rFbzUGHppkApyyku6MzOMDVDODI-KBMJMXmjHU6jvNq_2zv_pe2GJtfOLRNVahc6ZCsd0qeYkhhf0hQw4lmFuQNlrcQLNLrCxon8fuKuv3ybxY5H91GHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=qrdR_3pq-NsFdm8H1RlLpd2WhwMDJNMVLqArFQrR4lBf6v8rrg99ohsT1zjScxWdJpwsEFUt_BKwRo9T3ueppCIQLl9FDmURVTsEKVZS8J7yL4Gh28rPH_-4opH_YcdMUbRI5wggywCl5Bt50TBu9X_ETRZrIucCHm_1Bw3VMQqedWTSsT6QUxkE7tEoEjFuKIfmzvRm_VFs78mHPdxmMwAaZiNXavjk6rFbzUGHppkApyyku6MzOMDVDODI-KBMJMXmjHU6jvNq_2zv_pe2GJtfOLRNVahc6ZCsd0qeYkhhf0hQw4lmFuQNlrcQLNLrCxon8fuKuv3ybxY5H91GHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=QxvsgbAxOWJVH8_HU2eKteD8sR8KtLL1Fw8x9fKiJ_Q4orfkIyZ7XsrxoYT6W8CLWhOcJ42cQkIoIbeA4zAAJZhF4zzEa1xXaUFp2dQ7p7wMERhK0TTvz3yttgXvNELBqk2ar3fmWDOUstEIu18j0H-G4CozAhUkfUYAih1b6dCq_APL6APM3FKhklJ8NPu0kCKOvcSaSSklmv1MTSJPVndr2j6LwZPU40z_cSlPMh53NI1ARXUnjVwQqi7qmcZppIr45l0e-iqBvDNpg2tT5JVlaZLF83Lz0dCnsQus2B269QyxTqT3WPyn3vmXW3ozKrn0AcF98Lpa2obZGv8EHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=QxvsgbAxOWJVH8_HU2eKteD8sR8KtLL1Fw8x9fKiJ_Q4orfkIyZ7XsrxoYT6W8CLWhOcJ42cQkIoIbeA4zAAJZhF4zzEa1xXaUFp2dQ7p7wMERhK0TTvz3yttgXvNELBqk2ar3fmWDOUstEIu18j0H-G4CozAhUkfUYAih1b6dCq_APL6APM3FKhklJ8NPu0kCKOvcSaSSklmv1MTSJPVndr2j6LwZPU40z_cSlPMh53NI1ARXUnjVwQqi7qmcZppIr45l0e-iqBvDNpg2tT5JVlaZLF83Lz0dCnsQus2B269QyxTqT3WPyn3vmXW3ozKrn0AcF98Lpa2obZGv8EHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HF8caP2t3QSGcZ9wkycFQOHShWeBdcXEvpJn1H_WPj9WfkiJB58RDSrszok_J_Tpq9F1oDU3978U_t8O9SgonXJHiL77JRgcV2uCnna_oJDlIWy8ZAeQdY8s1nIBy0lsI8iDLRADBAT8jSCJ2H7ib-SR5BfdLu2x1AM92dEI2-Ymx6zeZ8JxxF8inFqkAvCit_U7DFp7hv9dmMpbSXTLGbaL1ZgQmmJbI5Ya2AAriBCl5AxdlYknSw3o76InL8gSNyhhNMhF_lNpdmoyr4n7XPE1Vs1pWtSOHJKBCXoPaZ2yw2NS6x1exfzzmaGsJWvouFgLhLcsHoJ6j_-_YsT7zQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzJy-F_ehLlqRBZ6lcio5uaPVlOmXjDZ_bo_TcoQmVPY1_7Pa4nqV-CCchQZ_GDrUHa-1mVIwXzyB1-ylivVVsk0F_zbZd1xpYbZ9pdmyZOr_xL_NWN30T8uV_kIEhMIT8D9IOD8csfyAuenMmDJhMLcYvCBWl5l0xNr1QBvVmycwHIuZ7gbvkXJhD1-lBA1siBeojax5TrBJNMS7_Dv5sfacPvXcnkUUYcLQK_JDRKUXQ8OEjX6WMDfcrmu2kvkzEKqxZft3uUOJ0uAW7N-0LShlqIFmmhtiOr-A4VuK9hVPkO7SgETjhE5G0LZETCVa1FrloVKrJCn82emqORkxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwx9Md_bOUpQKQcLxzW7fhQAuT9SUAuOqPrknPLYbJYEpyj-oIkM2FrCeS_RvU8UW-bNaF_EZlwsiFeBjZvz8mK7lYDEYug3Me356Xhw3bY6h3fvaWES_xaown3e4e-653WMT8sW5zNBH4rTzfkIHBzp2Xvu17P8gWIx07tMFityUJBt80_wJCkckG0GxP6wxrNSzT0vXt3bue-ei6fub0R53LSYZz9yZHDMpCS-HZcjWf5rYQFdtOtR1wrAeWOVxlp2l1d4Muvc112QiqmgwMWwYAhM1XBPhigBjffl_H5WFEVh7d9juKPkjAX4zDr7tzNsgdzHEdJi2-Klb8eBpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuAZ5X7IBQlvO_6NIuS1xOylhlczVP0eWH2tmj53XISHTgMl43wD811rXTuURF5LrnELqjYzYVEZ5XSD_CIcCUZS7ClMHCd5y806VLarh9kxmSsovFIRg6Hc_XxOTvYy3M-t9odhLqLisC0CkwEdlCG60f7g3KwCmyOcKExiUO90kOOQl8o-84K2T5gqdv91lVuFZlfWiPe7k0_udZt9_RszT5M_VDMkdJ8go2EBrq-ywgOeAl9zXRrlUhIpWVgyxhHdyZqddAAYQCCqHILR0W76fMgmZN3NppNFyQUaQgymLHF64538VN0p5hIJWF1tKLVBzz8wSVzfRHlpnVCzjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WAVyRFNXaU4EeOi7J1GwgxyHyEE3tbzT5aBaeSWgNgta6NSsuUXOBXq_LM0Z9K4BBiRPMVTb-hRBasgGTY7eZgT5amqzAF8cDegXelDy1jnepUtCk7njrMkFyd8KG5RpMH-_PQy4HQZPdzZnh8dXkMmiWqQPbOjQqehe6Hnr0gVsg5Xb049K-JT8CIBvYi-eEf7zntWTe80SAyajp4EIUFYGDwxpYL9Sd8ALYmwSzAO9ZPlGdu2m-aHDJ7Fajaq7jnxQ7tGa4YZMT_pC3rlDA0gp3KOPTPKcDQ-CUtw0bHYQqPyEZbloMRmoIFDC-f2lhetWOJOQyPYIxt8d8XAJzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NQXtV-dLkI2E5yqA9Fkt_gBYvlWzWnJ1Ff9pkxw-JU17vhI5ExXxuwywDyhHz7hyorlGGyIFYW0JCNaztN6nolRixTEQUYT56PAr3z4id8-dJ2tl4UYSq2trqg2h1yZMfkmxV3Y5EYLzT5PuZw-oKI1ufyIdIewdrzRA1LMtAo6FJCi_UkZna_H5BjE3oSBGfE7iKWCYw3RAb9zgLc071TIHSmNvZpTvJg8UR_RJsKb4ZKMHRp54Q3jk50AQNo2F0yCZAgA4vKLZ8jfzWSK-TdYHYyBKwyJPWmgKh3aYzyBlTcMVj7TnRJbHXAOyrzpGUZCDzYI-wGCEgxLTSeqCrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bZZfERJyxQWVXEITfGgqae-XAGf-ZF138075O5gFbrdrH9x_Q-DyrrTkHDd5FVFzuop0vtEzMbxmSEAx4WL-Ynqzzw4w8NFeyRvFVSHDsPMOprHTFRyU6zAq57Qp9Eqy6D6Y1p3pVnuRhl_DhLMUoveb2qSQ8RoQIh8mLkmmltEiM8Y1gD62yAYHdw93HE30AeVXoNWQRW3wdBR7gdU6fqqFK2TyBtrIi5LnqJHiSr3xPAqEinR1GDiQb657IdkNoAjpKgQy_b3BO80sKhxAoPWqPcf8QqSa45e2BLWtn91CmzRX5EV_Iqltjl_x934ZUzB15xrqmebDI8VHo3K3pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/byUb3ZDJbsq8mvlbdXgs0ibP6M2QfHoFG4bHPANvvz6plEzplwd2X_Ybk52gSPaPGnKOOrOumWkLWP-qpvVhG7HQrNhvBciEb0rbyxRPUMOisHU89a5Cki1hSxPSualZAMbrwIW0Mzqttb3pdPvTR9E0XSVWP5b_dshDCKQ0H_qS2Vj9WANkTWkAFdcAtJYX_UVhPREwb2_JxUlmHvFfoihfevH5jV0niVoHxvI0iBKq_TBOu6mgFEryJ7j8F1DdQu9WEAz6wBTm8xZ1LcztXl1NY8j_bEXABRpjVT7TxeMg8k9NjNtUM_jgQ9Mv6fQaGjWQ2n2qJKkf2BCCkD93dw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEkJmKHuXmU4_ScpKLeFDK3D-bvy7D99en5dhFjL4IKlac55hz4IcXNwvnbKNjVmmNcO_Qrg283PfO4MbF9r9P-XBZU6etTh86osEkHi3S8DCU5F74z9sDPCppNwPeZ70PeA1kWhlONvE9yy5w0Cg75Jlg_oH_gKDzD9CzmUcNv6Yy9ZIcpNHPm1yM6euwRYREdrajMy7VdovObYGLKW-Vo8MOTwoIVnHolTUmgZ13QDSBkUfZFNYUhKktKg3s3En3TD09eNwCyuDk5i333Npo0_KzJaCyyqoDCFwq9whiLLMeJG5g8Cg6nJTe31ujoQjkcAOJ1c9W9jz5T8F1Rm0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wps0t2bgqStIHud7T0KyDWDU8a9bVzydWV3pvqZHXfn-S5Cd5FJGtVEWoZnAMb8MZHapNk9lQCiPSrehUDN1JyTC5CljQ2MNemkQCQDE_JIJ96myKcrEHfTRNZCVtzemjn6_TaeE3wdeF6itaARKkCt7e20ZuKT-oLqAo_713PVPU_O7eP3YY0BjWrReEk8D5D3XtX_9CdgylLa6E-a90qUn-78tWWSShENsuTJyRmkfZerWcccd9EwZSHyXorpIRbq4_X784wx8RdiWhcZp-BdA0UnLgvNqD1xTLclwBsd_Vtdh5itWsIogcCMXrxZtCWsE9PX8UfK9SVMJgLFtTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=BCSRMyADeuusKREioBLTGQEQQgGtJfvkZT2Qtb29-wiENb-wRKlOtic-PfcMkFzTMSs7dVFkk6CZw5pabmIauvTTVUiDYLIHQLYGEfOqBnyQLwPhlAO46sags2yEhMF_WaJqtcPfbKD5wRHaVbTX1j46--c5jbiCTw4LcNnTPYv7Q4ykP1Ur5zLqG_Af8uTfY1M0RrpPaHszTncR0Q1Jug-cU_CSOUf_IWGn8msLHtJ5dy2p5cWVrMcOfnJkVaI3FBw49P2CSr0bOZpDeq6U457rzEKkaUYh4RyQMdiXEwFCXyAZ77ZLTyi4YggPXQnZPv00vot8cd-adund0vSSNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=BCSRMyADeuusKREioBLTGQEQQgGtJfvkZT2Qtb29-wiENb-wRKlOtic-PfcMkFzTMSs7dVFkk6CZw5pabmIauvTTVUiDYLIHQLYGEfOqBnyQLwPhlAO46sags2yEhMF_WaJqtcPfbKD5wRHaVbTX1j46--c5jbiCTw4LcNnTPYv7Q4ykP1Ur5zLqG_Af8uTfY1M0RrpPaHszTncR0Q1Jug-cU_CSOUf_IWGn8msLHtJ5dy2p5cWVrMcOfnJkVaI3FBw49P2CSr0bOZpDeq6U457rzEKkaUYh4RyQMdiXEwFCXyAZ77ZLTyi4YggPXQnZPv00vot8cd-adund0vSSNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=RRyXH6bROcqPxjU_qFxvb8eoaPwW7sRFAYysKfw9l-YIgnwKOaxGPHrMklsDpmpuFmpd00xFVofIJsU7fGHNOktBmVPd6LfPut0wGIBOUJlOiMi5MF0bcHZcAfkd9pa0JPsxrsYLL5PZQSqqI6PRci6C6L0PG3B6-vzoB97QnxlkD7sz-U-PHzZaiYPGWBYbbSrKsx5KEm0qPF501txsdQq5Am7UfvJfFvOwgHSRXpQAgpxdbxvH5BMzVESf7vByG6PfLVm5n4xCvwI6JzD5-aURIBEfpxlSgsqI8wZ_ivzpVxzz_OId99C1aNfQbZhPz2lHQNDZ0yztJH8PBHVqKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=RRyXH6bROcqPxjU_qFxvb8eoaPwW7sRFAYysKfw9l-YIgnwKOaxGPHrMklsDpmpuFmpd00xFVofIJsU7fGHNOktBmVPd6LfPut0wGIBOUJlOiMi5MF0bcHZcAfkd9pa0JPsxrsYLL5PZQSqqI6PRci6C6L0PG3B6-vzoB97QnxlkD7sz-U-PHzZaiYPGWBYbbSrKsx5KEm0qPF501txsdQq5Am7UfvJfFvOwgHSRXpQAgpxdbxvH5BMzVESf7vByG6PfLVm5n4xCvwI6JzD5-aURIBEfpxlSgsqI8wZ_ivzpVxzz_OId99C1aNfQbZhPz2lHQNDZ0yztJH8PBHVqKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
